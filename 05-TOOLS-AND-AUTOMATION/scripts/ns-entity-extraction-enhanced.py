#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Negeri Sembilan PRN 2026 - Enhanced Entity Extraction (v2)
==========================================================
Workspace: /home/p62operator/.openclaw/workspace-ns/
Classification: TLP:AMBER

This script supersedes the inline-Python in ns-entity-extraction.sh, which only
had extraction patterns for `parties` and `constituencies` (5 of 7 categories
returned empty). This v2 extractor covers all 7 categories with:
  - Malay-honorific name regex + a known-politician dictionary (deduped)
  - Canonical party dictionary (merges abbreviations + full names, no case dupes)
  - NS DUN/parliament constituency matching against the 36-seat master list,
    PLUS a "DUN <name-list>" parser that catches seats missing from the master
    list (e.g. Sri Tanjung, Seremban Jaya, Nilai) -> flags master-list gaps
  - Issue / event detection from keyword patterns with relevance tagging
  - Organization + location dictionaries
Each entity records its occurrence count and the source files it appeared in,
so results are traceable to the raw scrapes.

Input : 04-DATA-AND-SOURCES/raw-scrapes/YYYYMMDD/*.md
Output: 04-DATA-AND-SOURCES/processed-entities/YYYYMMDD/entities_<category>.json
        + entities_consolidated.json (full summary)
"""

import sys
import os
import re
import json
import glob
from collections import defaultdict

WORKSPACE = "/home/p62operator/.openclaw/workspace-ns"
RAW_DIR = os.path.join(WORKSPACE, "04-DATA-AND-SOURCES", "raw-scrapes")
PROCESSED_DIR = os.path.join(WORKSPACE, "04-DATA-AND-SOURCES", "processed-entities")
LOG_DIR = os.path.join(WORKSPACE, "06-INFRASTRUCTURE")


def clean_text(t):
    """Normalize markdown so entity matching is not polluted by URL slugs, while
    PRESERVING link display text and image alt-text (news captions often name
    people, DUN seats and organizations, e.g. the Astro Awani nomination-centre
    caption listing 'DUN Lenggeng, Nilai, Lobak, Temiang, Sikamat dan Ampangan')."""
    t = re.sub(r'!\[([^\]]*)\]\([^)]*\)', r'\1', t)      # images ![alt](url) -> keep alt
    t = re.sub(r'\[([^\]]*)\]\(([^)]*)\)', r'\1', t)       # links [text](url) -> keep text
    t = re.sub(r'https?://\S+', ' ', t)                   # bare URLs
    t = re.sub(r'\[\^[^\]]*\]', ' ', t)                  # footnote refs
    t = re.sub(r'\\\s*', ' ', t)                         # trailing backslash escapes
    t = re.sub(r'\s+', ' ', t)
    return t


# ---------------------------------------------------------------------------
# Reference dictionaries
# ---------------------------------------------------------------------------

# 36 NS DUN seats (from 00-OPERATIONS/dun-master-list.md, baseline 2026-07-10)
DUN_SEATS = [
    "Kuala Klawang", "Pertang", "Sungai Lui", "Klawang",          # P126 Jelebu
    "Serting", "Palong", "Bahau", "Rompin",                       # P127 Jempol
    "Rahang", "Temiang", "Sikamat", "Labu", "Bukit Kepayang", "Nilam",  # P128 Seremban
    "Juasseh", "Seri Menanti", "Pilah", "Johol",                  # P129 Kuala Pilah
    "Kota", "Chembong", "Lenggeng", "Pantai",                     # P130 Rembau
    "Lukut", "Chuah", "Si Rusa", "Telok Kemang",                  # P131 Port Dickson
    "Repah", "Gemencheh", "Gemensah", "Batu Kikir",              # P132 Tampin
    "Bagan Pinang", "Linggi", "Pasir Panjang", "Terentang",       # P133 Teluk Kemang
]
PARLIAMENT_SEATS = ["Jelebu", "Jempol", "Seremban", "Kuala Pilah",
                    "Rembau", "Port Dickson", "Tampin", "Teluk Kemang"]

# Seats detected in scrapes but ABSENT from the master list (flagged as gaps).
# Populated at runtime; seeded with known discrepancies discovered during review.
SEAT_GAP_NOTES = {
    "Sri Tanjung": "Named as a DUN seat in Utusan article ('MIC menang di DUN Sri Tanjung dan Seremban Jaya') but missing from 36-seat master list (dun-master-list.md).",
    "Seremban Jaya": "Named as a DUN seat in Utusan article but missing from 36-seat master list.",
    "Nilai": "Listed among DUNs in Astro Awani nomination-centre caption ('DUN Lenggeng, Nilai, Lobak, Temiang, Sikamat dan Ampangan') but master list has 'Nilam' (N14) instead. Possible master-list error or distinct seat.",
    "Chennah": "Named in Utusan article as a mixed DUN ('Chennah, Temiang dan Nilai') but missing from 36-seat master list.",
}

# Canonical parties: display name -> list of regex alternatives (IGNORECASE, \b)
PARTIES = {
    "Pakatan Harapan (PH)": [r'\bPakatan\s+Harapan\b', r'\bPH\b'],
    "Barisan Nasional (BN)": [r'\bBarisan\s+Nasional\b', r'\bBN\b'],
    "Perikatan Nasional (PN)": [r'\bPerikatan\s+Nasional\b', r'\bPN\b'],
    "UMNO": [r'\bUMNO\b'],
    "PKR": [r'\bPKR\b'],
    "DAP": [r'\bDAP\b'],
    "PAS": [r'\bPAS\b'],
    "Bersatu (PPBM)": [r'\bBersatu\b', r'\bParti\s+Pribumi\s+Bersatu\s+Malaysia\b', r'\bPPBM\b'],
    "MCA": [r'\bMCA\b'],
    "MIC": [r'\bMIC\b'],
    "Amanah": [r'\bAmanah\b'],
    "Warisan": [r'\bWarisan\b', r'\bParti\s+Warisan\b'],
    "Wawasan": [r'\bWawasan\b'],
    "MUDA": [r'\bMUDA\b'],
    "Gerakan": [r'\bGerakan\b'],
}

# Organizations / institutions
ORGANIZATIONS = {
    "Suruhanjaya Pilihan Raya (SPR/EC)": [r'\bSuruhanjaya\s+Pilihan\s+Raya\b', r'\bSPR\b', r'\bElection\s+Commission\b', r'\bEC\b'],
    "Polis Diraja Malaysia (PDRM)": [r'\bPolis\s+Diraja\s+Malaysia\b', r'\bPDRM\b', r'\bpolice\b', r'\bpolis\b'],
    "Majlis Bandaraya Seremban (MBS)": [r'\bMajlis\s+Bandaraya\s+Seremban\b', r'\bMBS\b'],
    "Dewan Undangan Negeri (DUN)": [r'\bDewan\s+Undangan\s+Negeri\b', r'\bDUN\b'],
    "BERNAMA": [r'\bBERNAMA\b'],
    "New Straits Times Press (NSTP)": [r'\bNew\s+Straits\s+Times\s+Press\b', r'\bNSTP\b'],
    "Star Media Group": [r'\bStar\s+Media\s+Group\b'],
    "Kabinet / Cabinet": [r'\bKabinet\b', r'\bCabinet\b'],
    "Majlis Tertinggi (PN Supreme Council)": [r'\bMajlis\s+Tertinggi\b', r'\bSupreme\s+Council\b'],
    "Media Mulia Sdn Bhd": [r'\bMedia\s+Mulia\b'],
    "Majlis Perbandaran / Local Authority": [r'\blocal\s+authorit(?:y|ies)\b', r'\bpihak\s+berkuasa\s+tempatan\b'],
}

# Locations: NS towns/districts + other Malaysian states/cities + key international
LOCATIONS = {
    # NS cities/towns/districts
    "Seremban": [r'\bSeremban\b'],
    "Nilai": [r'\bNilai\b'],
    "Port Dickson": [r'\bPort\s+Dickson\b'],
    "Tampin": [r'\bTampin\b'],
    "Rembau": [r'\bRembau\b'],
    "Jelebu": [r'\bJelebu\b'],
    "Jempol": [r'\bJempol\b'],
    "Kuala Pilah": [r'\bKuala\s+Pilah\b'],
    "Bahau": [r'\bBahau\b'],
    "Forest Heights": [r'\bForest\s+Heights\b'],
    # Other Malaysian states/cities
    "Kuala Lumpur": [r'\bKuala\s+Lumpur\b'],
    "Petaling Jaya": [r'\bPetaling\s+Jaya\b'],
    "Kajang": [r'\bKajang\b'],
    "Johor Baru": [r'\bJohor\s+Baru\b', r'\bJohor\s+Bahru\b'],
    "George Town": [r'\bGeorge\s+Town\b'],
    "Kota Baru": [r'\bKota\s+Baru\b', r'\bKota\s+Bharu\b'],
    "Kota Kinabalu": [r'\bKota\s+Kinabalu\b'],
    "Setapak": [r'\bSetapak\b'],
    "Cyberjaya": [r'\bCyberjaya\b'],
    "Cameron Highlands": [r'\bCameron\s+Highlands\b'],
    "Tapah": [r'\bTapah\b'],
    "Sungai Buloh": [r'\bSungai\s+Buloh\b'],
    "Kota Damansara": [r'\bKota\s+Damansara\b'],
    "Forest City": [r'\bForest\s+City\b'],
    "Melaka": [r'\bMelaka\b', r'\bMalacca\b'],
    "Pahang": [r'\bPahang\b'],
    "Johor": [r'\bJohor\b'],
    "Kedah": [r'\bKedah\b'],
    "Sabah": [r'\bSabah\b'],
    "Sarawak": [r'\bSarawak\b'],
    "Penang": [r'\bPenang\b'],
    "Selangor": [r'\bSelangor\b'],
    "Perak": [r'\bPerak\b'],
    "Kelantan": [r'\bKelantan\b'],
    "Terengganu": [r'\bTerengganu\b'],
    "Putrajaya": [r'\bPutrajaya\b'],
    "Maran": [r'\bMaran\b'],
    "Sungai Sedim": [r'\bSungai\s+Sedim\b'],
    # International (present in today's corpus)
    "Taiwan": [r'\bTaiwan\b'],
    "United States": [r'\bUnited\s+States\b'],
    "Iran": [r'\bIran\b'],
    "Hong Kong": [r'\bHong\s+Kong\b'],
    "Spain": [r'\bSpain\b', r'\bSepanyol\b'],
    "Argentina": [r'\bArgentina\b'],
    "France": [r'\bFrance\b', r'\bPerancis\b'],
    "England": [r'\bEngland\b'],
    "Turkiye": [r'\bTurkiye\b', r'\bTurki\b'],
    "Arab Saudi": [r'\bArab\s+Saudi\b'],
}

# Known politicians (canonical display -> regex alternatives, IGNORECASE)
KNOWN_POLITICIANS = {
    "Tan Sri Muhyiddin Yassin (Bersatu President)": [r'\bMuhyiddin\s+Yassin\b', r'\bMuhyiddin\b'],
    "Datuk Seri Anwar Ibrahim (PM)": [r'\bAnwar\s+Ibrahim\b', r'\bDatuk\s+Seri\s+Anwar\b'],
    "Tan Sri Abdul Hadi Awang (PAS President)": [r'\bAbdul\s+Hadi\s+Awang\b', r'\bHadi\s+Awang\b'],
    "Datuk Seri Dr. Ahmad Samsuri Mokhtar (PN Chairman)": [r'\bAhmad\s+Samsuri\s+Mokhtar\b', r'\bAhmad\s+Samsuri\b'],
    "Datuk Mustapha Nagoor (UMNO NS Sec)": [r'\bMustapha\s+Nagoor\b'],
    "Kamarol Ridzuan Mohd. Zain (PAS NS Deputy Comm.)": [r'\bKamarol\s+Ridzuan\s+Mohd\.?\s*Zain\b', r'\bKamarol\s+Ridzuan\b'],
    "P. Supramanium (MIC NS Chairman)": [r'\bP\.?\s*Supramanium\b', r'\bSupramanium\b'],
    "Datuk Seri R. Ramanan (Sungai Buloh MP)": [r'\bR\.?\s*Ramanan\b', r'\bRamanan\b'],
    "Datuk Seri Ramlan Harun (EC Chairman)": [r'\bRamlan\s+Harun\b'],
    "Aminuddin Harun (NS Menteri Besar)": [r'\bAminuddin\s+Harun\b', r'\bAminuddin\b'],
    "Datuk Seri Ahmad Zahid Hamidi (UMNO Pres.)": [r'\bAhmad\s+Zahid\s+Hamidi\b', r'\bZahid\b'],
    "Datuk Mubarak Dohak (former Undang Sungei Ujong)": [r'\bMubarak\s+Dohak\b'],
    "Tunku Nadzaruddin (YDP candidate)": [r'\bTunku\s+Nadzaruddin\b', r'\bNadzaruddin\b'],
    "Asyraf Wajdi": [r'\bAsyraf\s+Wajdi\b'],
    "Azalina Othman Said": [r'\bAzalina\b'],
    "Kamil Munim": [r'\bKamil\s+Munim\b'],
    "Onn Hafiz (Johor MB)": [r'\bOnn\s+Hafiz\b'],
    "Syed Saddiq (MUDA)": [r'\bSyed\s+Saddiq\b'],
    "Veerapan (DAP - Repah 2023)": [r'\bVeerapan\b'],
    "Khairy Jamaluddin": [r'\bKhairy\s+Jamaluddin\b', r'\bKhairy\b'],
}

# Events: canonical label -> regex alternatives
EVENTS = {
    "PRN NS Nomination Day (18 Jul 2026)": [r'\bnomination\s+day\b', r'\bpenamaan\s+calon\b', r'\bhar[i]\s+penamaan\b', r'\bsimulasi\s+proses\s+penamaan\b'],
    "PRN NS Polling Day (1 Aug 2026)": [r'\bAug\s*1\s+polls\b', r'\b1\s+Ogos\b', r'\bpolling\s+day\b', r'\bhar[i]\s+pengundian\b', r'\bpoll\s+date\b'],
    "PRN Negeri Sembilan (State Election)": [r'\bPilihan\s+Raya\s+Negeri\b', r'\bPRN\s*Negeri\s+Sembilan\b', r'\bPRN\s*NS\b', r'\bstate\s+election\b', r'\bNegri\s+Sembilan\s+(?:state\s+)?polls?\b', r'\bNegeri\s+Sembilan\s+election\b', r'\bN\.?\s*Sembilan\s+polls\b', r'\bstate\s+polls?\b'],
    "Campaign Period": [r'\bkempen\s+PRN\b', r'\bkempen\s+Negeri\b', r'\bcampaign\s+period\b', r'\bkempen\s+pilihan\s+raya\b', r'\bnomination\s+papers\b'],
}

# Issues: canonical label -> (regex alternatives, relevance)
ISSUES = {
    "BN-PN electoral pact / seat negotiation": ([r'\belectoral\s+pact\b', r'\bpembahagian\s+kerusi\b', r'\brundingan\s+kerusi\b', r'\btidak\s+meletakkan\s+calon\b', r'\bkerjasama.*?kerusi\b'], "ns"),
    "PAS-Bersatu rift": ([r'\brift\b', r'\bperselisihan\b', r'\bberpecah\b', r'\bclash(?:es)?\b', r'\bgo\s+head-to-head\b', r'\bface\s+(?:Pas|Bersatu)\b'], "ns"),
    "Royal succession crisis": ([r'\broyal\s+(?:crisis|succession)\b', r'\bkrisis\s+diraja\b', r'\bUndang\b', r'\bUndang\s+of\s+Sungei\s+Ujong\b'], "ns"),
    "Malay vote unity": ([r'\bpenyatuan\s+undi\s+Melayu\b', r'\bundi\s+Melayu\b', r'\bMalay\s+(?:unity|votes?)\b'], "ns"),
    "Bersatu new coalition/bloc": ([r'\bnew\s+(?:coalition|bloc|alliance)\b', r'\bform\s+a\s+new\s+(?:alliance|coalition|bloc)\b'], "ns"),
    "KWAP / eFishery investment fraud": ([r'\bKWAP\b', r'\beFishery\b', r'\bpenipuan\s+pelaburan\b'], "national"),
    "Corporate mafia / RCI": ([r'\bcorporate\s+mafia\b', r'\bRCI\b', r'\bRoyal\s+Commission\s+of\s+Inquiry\b'], "national"),
    "Data centre concerns (Kota Damansara)": ([r'\bdata\s+centre\b', r'\bpusat\s+data\b'], "national"),
    "Orang Asli land dispute (Kg Sungai Cot)": ([r'\bOrang\s+Asli\b', r'\bKampung\s+Sungai\s+Cot\b', r'\btanah\s+orang\s+asli\b'], "national"),
    "Forest City Network School controversy": ([r'\bNetwork\s+School\b', r'\bForest\s+City\s+Network\s+School\b'], "johor"),
    "Social-media monitoring / slander during polls": ([r'\bmonitor\s+social\s+media\b', r'\bspreading\s+slander\b', r'\bfitnah\b', r'\bpujukan\s+fitnah\b'], "ns"),
    "AI / national identity (PM)": ([r'\bcaptive\s+mind\b', r'\bartificial\s+intelligence\b', r'\bnational\s+identity\b'], "national"),
}


# ---------------------------------------------------------------------------
# Matching helpers
# ---------------------------------------------------------------------------

# Single-word proper nouns whose lowercase form is a common Malay/English word
# (bersatu=united, nilai=value, perak=silver, amanah=trust, warisan=heritage,
# gerakan=movement, wawasan=vision). For these we accept a case-insensitive match
# only when the matched string starts with an uppercase letter, so 'bersatu'
# (the adjective) is rejected while 'Bersatu' and all-caps 'BERSATU' are kept.
COMMON_WORD_RISK = {"Bersatu", "Amanah", "Warisan", "Gerakan", "Wawasan",
                    "Nilai", "Perak"}


def count_matches(patterns, text, ignorecase=True):
    """Return (count, set_of_matched_strings) for a list of regex patterns.

    Pure two-letter all-caps abbreviation patterns (e.g. r'\\bPH\\b', r'\\bEC\\b')
    are matched CASE-SENSITIVELY so that common words like 'as'/'us' do not inflate
    counts; longer patterns use the requested ignorecase flag. Single-word
    common-word-risk patterns additionally require an uppercase first char."""
    matched = set()
    total = 0
    for pat in patterns:
        core = pat.replace("\\b", "")
        is_2cap_abbr = bool(re.fullmatch(r"[A-Z]{2}", core))
        is_common_word = core in COMMON_WORD_RISK
        flags = 0 if is_2cap_abbr else (re.IGNORECASE if ignorecase else 0)
        for m in re.finditer(pat, text, flags):
            if is_common_word and not m.group(0)[:1].isupper():
                continue
            total += 1
            matched.add(m.group(0))
    return total, matched


def find_sources_for_dict(dictionary, file_texts):
    """For a {display: [patterns]} dict, return list of {name, count, sources, matches}."""
    out = []
    for name, patterns in dictionary.items():
        count = 0
        srcs = set()
        all_matches = set()
        for fname, text in file_texts.items():
            c, ms = count_matches(patterns, text)
            if c:
                count += c
                srcs.add(fname)
                all_matches |= ms
        if count > 0:
            out.append({
                "name": name,
                "count": count,
                "sources": sorted(srcs),
                "variants": sorted(all_matches)[:12],
            })
    out.sort(key=lambda x: (-x["count"], x["name"]))
    return out


# ---------------------------------------------------------------------------
# Politician extraction (honorific regex + known dict, deduped)
# ---------------------------------------------------------------------------

HONORIFICS = (r"Tun|Toh\s+Puan|Tan\s+Sri\s+Dato['\u2019]?|Tan\s+Sri|"
              r"Datuk\s+Seri|Dato['\u2019]?\s+Seri|Datuk\s+Amar|Datuk|Dato['\u2019]?|"
              r"Datin\s+Paduka|Datin\s+Seri|Datin|Tengku|Tunku|Raja|Syed")
NAME_TOKEN = r"[A-Z][A-Za-z.\u2019'\-]+"
POLITICIAN_RE = re.compile(
    r"\b(" + HONORIFICS + r")\s+"
    r"((?:Prof\.?\s+)?(?:Dr\.?\s+)?" + NAME_TOKEN + r"(?:\s+" + NAME_TOKEN + r"){0,4})"
)

TITLE_WORDS = {"tun", "toh", "puan", "tan", "sri", "seri", "datuk", "dato", "datu", "datin",
               "amar", "paduka", "tengku", "tunku", "raja", "syed", "prof", "dr", "haji", "hajah",
               "hj", "hjh", "tuan", "encik", "bandar", "besar", "menteri",
               "pesuruhjaya", "pengerusi", "setiausaha", "presiden", "timbalan",
               "ahli", "dewan", "undangan", "negeri", "malaysia", "kerajaan",
               "perdana", "gabenor", "sultan", "yang", "di", "kepada", "oleh",
               "bagi", "dan", "atau", "serta", "ini", "itu", "akan", "telah"}


BYLINE_NOISE = {"nation", "bernama", "reuters", "afp", "photo", "pix", "foto",
                "jul", "jun", "aug", "sep", "sept", "oct", "nov", "dec",
                "jan", "feb", "mar", "apr", "may", "says", "adds", "by",
                "the", "and", "on", "in", "of", "to", "for"}


def normalize_name_key(s):
    """Normalize a politician display to a dedup key: lowercase, strip
    parenthetical role suffixes and honorifics/titles, drop single-letter
    initials and periods."""
    s = re.sub(r"\([^)]*\)", " ", s)        # drop role suffixes like "(Bersatu President)"
    s = s.lower()
    s = re.sub(r"['\u2019]", "", s)         # straighten apostrophes
    s = re.sub(r"\b\w\b", " ", s)          # drop single-char tokens (initials)
    toks = [t for t in re.split(r"[.\s]+", s) if t and t not in TITLE_WORDS]
    return " ".join(toks).strip()


def extract_politicians(file_texts):
    """Combine honorific-regex hits with the known-politician dict, dedup by
    normalized name key. Returns list of {name, count, sources, aliases}."""
    buckets = defaultdict(lambda: {"name": "", "count": 0, "sources": set(), "aliases": set()})

    # 1) Known-politician dictionary (authoritative display names)
    for display, patterns in KNOWN_POLITICIANS.items():
        key = normalize_name_key(display)
        if not key:
            continue
        b = buckets[key]
        if not b["name"]:
            b["name"] = display
        for fname, text in file_texts.items():
            c, ms = count_matches(patterns, text)
            if c:
                b["count"] += c
                b["sources"].add(fname)
                b["aliases"] |= ms

    # Build a lookup of known canonical displays keyed by normalized name, so a
    # honorific hit like "Tan Sri Muhyiddin Yassin" resolves to the richer known
    # display "Tan Sri Muhyiddin Yassin (Bersatu President)".
    known_by_key = {normalize_name_key(d): d for d in KNOWN_POLITICIANS}

    # 2) Honorific-regex hits over cleaned text
    for fname, text in file_texts.items():
        for m in POLITICIAN_RE.finditer(text):
            full = re.sub(r"\s+", " ", m.group(0)).strip()
            # skip honorific matches that are actually an institution's namesake
            # (e.g. 'SMKA Tun Datu Mustapha' is a Kota Kinabalu school, not a person)
            pre = text[max(0, m.start() - 24):m.start()]
            if re.search(r"\b(SMKA|SMK|SK|Sekolah|Universiti|Uni\.?|Kolej|Institut|Pusat|MRSM|MARA|Tadika)\s*$", pre):
                continue
            # strip a leading honorific cluster to get the bare name for keying
            bare = re.sub(r"^(?:" + HONORIFICS + r"\s+)+", "", full)
            bare = re.sub(r"^(?:Prof\.?\s+|Dr\.?\s+)+", "", bare).strip()
            key = normalize_name_key(bare)
            if not key or len(key) < 3:
                continue
            # skip pure-title captures (e.g. "Datuk Bandar", "Tan Sri Sultan")
            if all(t in TITLE_WORDS for t in key.split()):
                continue
            # skip royal-office references that are not a known figure
            if re.search(r"\b(yang\s+di-?pertuan|undang|sultan)\b", key) and key not in known_by_key:
                continue
            # skip byline / photo-credit garbage from 404 pages (e.g. nst's
            # 'Datuk Seri R.... Nation Jul 17, 2026' where 'Nation' is a breadcrumb)
            if key not in known_by_key and any(t in BYLINE_NOISE for t in key.split()):
                continue
            # require at least one alphabetic name token >= 3 chars (drop 'R....')
            if not any(len(t) >= 3 and t.isalpha() for t in key.split()):
                continue
            b = buckets[key]
            b["count"] += 1
            b["sources"].add(fname)
            b["aliases"].add(full)
            # choose display: authoritative known form wins; else the longest alias
            if not b["name"]:
                b["name"] = known_by_key.get(key, full)
            elif key in known_by_key and known_by_key[key] not in b["aliases"]:
                b["name"] = known_by_key[key]

    out = []
    for key, b in buckets.items():
        if b["count"] == 0:
            continue
        # if we never assigned a name (shouldn't happen), use key
        name = b["name"] or key.title()
        out.append({
            "name": name,
            "count": b["count"],
            "sources": sorted(b["sources"]),
            "aliases": sorted(b["aliases"])[:12],
        })
    out.sort(key=lambda x: (-x["count"], x["name"]))
    return out


# ---------------------------------------------------------------------------
# Constituency extraction (master-list match + DUN-list parser)
# ---------------------------------------------------------------------------

# Compounds where "Kota" is NOT the NS seat N19 Kota
KOTA_NEG = r"(?!\s+(?:Damansara|Baru|Bharu|Kinabalu|Tinggi|Laksamana|Raja|Belia|Sultan|Lumpur))"
# Generic non-seat words that the DUN-list parser must reject
SEAT_REJECT = TITLE_WORDS | {"dewan", "kerusi", "calon", "pilihan", "raya", "prn",
                             "bn", "pn", "ph", "umno", "pas", "dap", "bersatu",
                             "mca", "mic", "pk", "ppbm", "warisan", "amanah", "muda",
                             "di", "ke", "dari", "untuk", "pada", "bagi", "yang", "akan",
                             "telah", "oleh", "ini", "itu", "dan", "atau", "serta",
                             "dll", "dsb", "rm", "no", "n", "p", "sembilan", "n9", "ns",
                             "iaitu", "empat", "tiga", "dua", "tiga", "lima", "enam"}
# A constituency name never starts with an honorific/title. "Sri"/"Seri" are
# allowed as starts because real seats use them (Sri Tanjung, Seri Menanti).
HONORIFIC_START = {"datuk", "dato", "datin", "tan", "tun", "tunku", "tengku",
                   "raja", "syed", "prof", "dr", "yang", "haji", "hajah", "hj",
                   "hjh", "tuan", "puan", "encik", "toh", "kepada", "oleh", "yang"}


def build_seat_regex(name):
    if name == "Kota":
        return r"\bKota" + KOTA_NEG + r"\b"
    return r"\b" + re.escape(name) + r"\b"

_NAMEGRP = r"[A-Z][A-Za-z\u2019'\-]+(?:\s+[A-Z][A-Za-z\u2019'\-]+)*"
# A name group is one or more consecutive capitalized tokens (handles multi-word
# seats like 'Sri Tanjung', 'Seremban Jaya', 'Bukit Kepayang').
_SEP = r"\s*(?:,|dan|atau|serta|&)\s*"
# Triggers: 'DUN' (optionally with a following ')', as in '(DUN) Lenggeng, Nilai, ...')
# or 'iaitu' (Malay 'namely', which introduces seat lists in Utusan analysis).
_DUN_LIST_RE = re.compile(r"\b(?:DUN\)?|[Ii]aitu)\s+(" + _NAMEGRP + r")((?:" + _SEP + _NAMEGRP + r")*)")


def parse_dun_lists(text):
    """Parse 'DUN <Name1>, <Name2> dan <Name3>' style lists and return the
    capitalized seat names found. Handles multi-word seats like 'Sri Tanjung'
    and 'Seremban Jaya', and '(DUN) Lenggeng, Nilai, Lobak, ... dan Ampangan'."""
    seats = set()
    for m in _DUN_LIST_RE.finditer(text):
        candidates = [m.group(1)]
        # re-extract each subsequent name group from the tail
        for nm in re.findall(_NAMEGRP, m.group(2)):
            candidates.append(nm)
        for nm in candidates:
            nm = nm.strip(" .,")
            if len(nm) >= 3 and not _is_reject_name(nm):
                seats.add(nm)
    return seats


def _is_reject_name(nm):
    toks = [t for t in re.split(r"\s+", nm) if t]
    if not toks:
        return True
    # NS DUN seats are at most two words (Sri Tanjung, Seremban Jaya, Bukit
    # Kepayang, Kuala Klawang, ...). Reject parser-detected candidates with
    # 3+ tokens -- these are almost always a real seat name glued to an
    # adjacent candidate's name in a photo caption (e.g. 'Sungai Lui Zainal
    # Fikri Abd Kadir', 'Pertang Mohd Umry Abdul Khois', 'Klawang Bakri
    # Sawir'). The genuine seat underneath is still captured independently
    # by the master-list dictionary match or by a comma-separated
    # 'DUN a, b, c' list, so this cap loses no real seat.
    if len(toks) > 2:
        return True
    low = [t.lower().strip(".'") for t in toks]
    if all(t in SEAT_REJECT for t in low):
        return True
    # reject single tokens that are generic/stop words
    if len(toks) == 1 and low[0] in SEAT_REJECT:
        return True
    # a constituency never starts with an honorific/title word (catches
    # person-name false positives from 'iaitu Datuk ...'); but 'Sri'/'Seri'
    # are allowed (real seats: Sri Tanjung, Seri Menanti).
    if low[0] in HONORIFIC_START:
        return True
    return False


def extract_constituencies(file_texts):
    seats_hits = {}   # name -> {count, sources, in_master}
    # 1) master-list DUN + parliament seats (dictionary match, IGNORECASE)
    master_names = set(DUN_SEATS) | set(PARLIAMENT_SEATS)
    for name in master_names:
        rx = build_seat_regex(name)
        count = 0
        srcs = set()
        for fname, text in file_texts.items():
            for m in re.finditer(rx, text, re.IGNORECASE):
                count += 1
                srcs.add(fname)
        if count:
            seats_hits[name] = {"count": count, "sources": srcs,
                                "in_master": True, "type": "DUN" if name in DUN_SEATS else "Parliament"}
    # 2) DUN-list parser (catches seats missing from master list).
    #    Skip our own analyst summary files here: their ops/prose lines
    #    (e.g. 'DUN War Rooms, Intelligence Cell -> Telegram') falsely trigger
    #    the 'DUN <list>' / 'iaitu <list>' parser. Master-list seats named in
    #    summaries are still captured by the dictionary match above; only the
    #    heuristic list-parser is restricted to raw news scrapes, so no genuine
    #    seat (which also appears in the raw scrapes) is lost.
    for fname, text in file_texts.items():
        if fname.startswith("nomination-day-summary-"):
            continue
        for seat in parse_dun_lists(text):
            # dedup case-insensitively against master
            canon = next((m for m in master_names if m.lower() == seat.lower()), None)
            key = canon or seat
            if key not in seats_hits:
                seats_hits[key] = {"count": 0, "sources": set(), "in_master": key in master_names, "type": "DUN (detected)"}
            seats_hits[key]["count"] += 1
            seats_hits[key]["sources"].add(fname)
            if not seats_hits[key]["in_master"]:
                seats_hits[key]["type"] = "DUN (not in master list - GAP)"
    out = []
    for name, info in seats_hits.items():
        out.append({
            "name": name,
            "count": info["count"],
            "sources": sorted(info["sources"]),
            "type": info["type"],
            "in_master_list": info["in_master"],
            "master_list_gap_note": SEAT_GAP_NOTES.get(name, "") if not info["in_master"] else "",
        })
    out.sort(key=lambda x: (-x["count"], x["name"]))
    return out


# ---------------------------------------------------------------------------
# Issues & events
# ---------------------------------------------------------------------------

def extract_events(file_texts):
    out = []
    for label, patterns in EVENTS.items():
        count = 0
        srcs = set()
        for fname, text in file_texts.items():
            c, _ = count_matches(patterns, text)
            if c:
                count += c
                srcs.add(fname)
        if count:
            out.append({"name": label, "count": count, "sources": sorted(srcs)})
    out.sort(key=lambda x: (-x["count"], x["name"]))
    return out


def extract_issues(file_texts):
    out = []
    for label, (patterns, relevance) in ISSUES.items():
        count = 0
        srcs = set()
        for fname, text in file_texts.items():
            c, _ = count_matches(patterns, text)
            if c:
                count += c
                srcs.add(fname)
        if count:
            out.append({"name": label, "count": count, "sources": sorted(srcs), "relevance": relevance})
    out.sort(key=lambda x: (-x["count"], x["name"]))
    return out


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    import datetime
    date_stamp = datetime.date.today().strftime("%Y%m%d")
    collection_dir = os.path.join(RAW_DIR, date_stamp)
    if not os.path.isdir(collection_dir):
        # fall back to most recent collection
        dirs = sorted(glob.glob(os.path.join(RAW_DIR, "*/")), reverse=True)
        if not dirs:
            print("[FATAL] No raw-scrape collections found.")
            sys.exit(1)
        collection_dir = dirs[0].rstrip("/")
        date_stamp = os.path.basename(collection_dir)
    out_dir = os.path.join(PROCESSED_DIR, date_stamp)
    os.makedirs(out_dir, exist_ok=True)

    md_files = sorted(glob.glob(os.path.join(collection_dir, "*.md")))
    if not md_files:
        print(f"[FATAL] No .md files in {collection_dir}")
        sys.exit(1)

    print(f"=== NS PRN 2026 Enhanced Entity Extraction ===")
    print(f"Date stamp : {date_stamp}")
    print(f"Collection : {collection_dir}")
    print(f"Source files: {len(md_files)}")
    print()

    # build cleaned per-file texts
    file_texts = {}
    raw_meta = {}
    for f in md_files:
        with open(f, "r", encoding="utf-8", errors="replace") as fh:
            raw = fh.read()
        raw_meta[os.path.basename(f)] = len(raw)
        file_texts[os.path.basename(f)] = clean_text(raw)

    errors = []

    def write_category(cat, entities):
        path = os.path.join(out_dir, f"entities_{cat}.json")
        payload = {
            "date": date_stamp,
            "timestamp": datetime.datetime.now().astimezone().isoformat(),
            "source_count": len(md_files),
            "entity_type": cat,
            "extraction_method": "enhanced-pattern-dictionary v2",
            "entity_count": len(entities),
            "entities": entities,
        }
        try:
            with open(path, "w", encoding="utf-8") as fh:
                json.dump(payload, fh, indent=2, ensure_ascii=False)
            print(f"  + {cat:14s} -> {len(entities):3d} entities  ({path})")
            return len(entities)
        except Exception as e:
            errors.append(f"{cat}: {e}")
            print(f"  x {cat:14s} FAILED: {e}")
            return 0

    print("Extracting entities by category...")
    counts = {}
    counts["politicians"] = write_category("politicians", extract_politicians(file_texts))
    counts["parties"] = write_category("parties", find_sources_for_dict(PARTIES, file_texts))
    counts["constituencies"] = write_category("constituencies", extract_constituencies(file_texts))
    counts["organizations"] = write_category("organizations", find_sources_for_dict(ORGANIZATIONS, file_texts))
    counts["locations"] = write_category("locations", find_sources_for_dict(LOCATIONS, file_texts))
    counts["events"] = write_category("events", extract_events(file_texts))
    counts["issues"] = write_category("issues", extract_issues(file_texts))

    # master-list gaps among detected constituencies
    cons_path = os.path.join(out_dir, "entities_constituencies.json")
    gap_names = []
    if os.path.exists(cons_path):
        with open(cons_path, "r", encoding="utf-8") as fh:
            cons_data = json.load(fh)
        gap_names = [e["name"] for e in cons_data["entities"] if not e["in_master_list"]]

    total = sum(counts.values())
    consolidated = {
        "date": date_stamp,
        "timestamp": datetime.datetime.now().astimezone().isoformat(),
        "source_count": len(md_files),
        "source_files": list(file_texts.keys()),
        "extraction_completed": True,
        "extraction_method": "enhanced-pattern-dictionary v2",
        "categories": counts,
        "total_entities": total,
        "constituency_master_list_gaps": gap_names,
        "notes": [
            "Extractor v2 supersedes ns-entity-extraction.sh inline Python, which only populated parties & constituencies.",
            "Constituencies matched against 36-seat DUN master list + a 'DUN <list>' parser; seats absent from the master list are flagged as gaps.",
            "Politicians extracted via Malay-honorific regex + known-figure dictionary, deduped by normalized name.",
            "Parties canonicalized (abbreviations merged with full names; no case-variant duplicates).",
            "Each entity records occurrence count + source files for traceability.",
        ],
        "errors": errors,
    }
    cons_out = os.path.join(out_dir, "entities_consolidated.json")
    with open(cons_out, "w", encoding="utf-8") as fh:
        json.dump(consolidated, fh, indent=2, ensure_ascii=False)

    print()
    print("=== Summary ===")
    for k, v in counts.items():
        print(f"  {k:14s}: {v}")
    print(f"  TOTAL          : {total}")
    if gap_names:
        print(f"  Master-list gaps detected: {', '.join(gap_names)}")
    if errors:
        print(f"  Errors: {errors}")
    print(f"  Consolidated: {cons_out}")
    print("Done.")

    # also write a machine-readable summary line for the ops log
    try:
        os.makedirs(LOG_DIR, exist_ok=True)
        log_path = os.path.join(LOG_DIR, f"extraction_{date_stamp}.log")
        with open(log_path, "a", encoding="utf-8") as fh:
            fh.write(f"[{datetime.datetime.now().astimezone().isoformat()}] "
                     f"enhanced v2 sources={len(md_files)} "
                     f"politicians={counts['politicians']} parties={counts['parties']} "
                     f"constituencies={counts['constituencies']} organizations={counts['organizations']} "
                     f"locations={counts['locations']} events={counts['events']} issues={counts['issues']} "
                     f"total={total} gaps={len(gap_names)} errors={len(errors)}\n")
    except Exception as e:
        print(f"  (log write failed: {e})")


if __name__ == "__main__":
    main()
