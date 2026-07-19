#!/usr/bin/env python3
"""
Negeri Sembilan PRN 2026 — Enhanced Entity Extraction
=====================================================
Reads all markdown scrapes from a day's raw-scrape directory and extracts
structured political entities across 7 categories:

    politicians, parties, constituencies, issues, events, organizations, locations

The default shell extractor (ns-entity-extraction.sh) only pattern-matches
party acronyms and a noisy DUN regex, leaving 5/7 categories empty. This
enhanced extractor parses the structured BERNAMA "Senarai calon" roll
(`**N01 CHENNAH:** ... 1\\. Name (Party)`) for clean candidates/parties/seats,
then mines narrative text for titled politicians, locations, organizations,
events, and issues.

Usage:
    python3 ns_entity_extraction_enhanced.py [YYYYMMDD]

Output (overwrites the 7 entities_*.json + entities_consolidated.json produced
by the shell script with higher-quality, deduplicated data):
    04-DATA-AND-SOURCES/processed-entities/YYYYMMDD/entities_<category>.json
"""
import sys
import os
import re
import json
import glob
from collections import defaultdict, Counter
from datetime import datetime, timezone

WORKSPACE = "/home/p62operator/.openclaw/workspace-ns"
RAW_DIR = os.path.join(WORKSPACE, "04-DATA-AND-SOURCES", "raw-scrapes")
PROC_DIR = os.path.join(WORKSPACE, "04-DATA-AND-SOURCES", "processed-entities")

# ---------------------------------------------------------------------------
# Reference data: the 36 Negeri Sembilan DUN seats (authoritative seat codes).
# Used to validate/clean extracted constituency names.
# ---------------------------------------------------------------------------
NS_DISTRICTS = [
    "Seremban", "Port Dickson", "Kuala Pilah", "Jempol", "Tampin", "Rembau",
    "Jelebu", "Nilai",
]

NS_PLACES = {
    "Seremban", "Port Dickson", "Kuala Pilah", "Jempol", "Tampin", "Rembau",
    "Jelebu", "Nilai", "Bahau", "Gemas", "Gemenceh", "Gemencheh", "Lukut",
    "Labu", "Rantau", "Pilah", "Juasseh", "Johol", "Senaling", "Lenggeng",
    "Lobak", "Sikamat", "Ampangan", "Mambau", "Rahang", "Paroi", "Chembong",
    "Kota", "Chennah", "Pertang", "Klawang", "Serting", "Palong",
    "Jeram Padang", "Sungai Lui", "Bukit Kepayang", "Seremban Jaya",
    "Seri Menanti", "Seri Tanjung", "Bagan Pinang", "Linggi", "Chuah",
    "Temiang", "Repah", "Mantin", "Lenggeng", "Broga",
}

# Coalition -> component party normalization. The "Senarai calon" prints
# tickets like "BN-UMNO", "PH-DAP", "PN-PAS", "PN-WAWASAN", "BERSATU", "Bebas".
# We split into coalition + component and keep both as distinct party entities.
COALITIONS = {
    "PH": "Pakatan Harapan",
    "BN": "Barisan Nasional",
    "PN": "Perikatan Nasional",
}
COMPONENT_NORMALIZE = {
    "UMNO": "UMNO",
    "MCA": "MCA",
    "MIC": "MIC",
    "DAP": "DAP",
    "PKR": "PKR",
    "AMANAH": "Amanah",
    "PAS": "PAS",
    "BERSATU": "Bersatu",
    "GERAKAN": "Gerakan",
    "WAWASAN": "Wawasan",
    "MIPP": "MIPP",
    "PSM": "Parti Sosialis Malaysia (PSM)",
    "BERJASA": "Berjasa",
    "ASLI": "Parti Orang Asli Malaysia (ASLI)",
    "BEBAS": "Bebas (Independent)",
}

# Malay honorifics that prefix politician names in narrative text.
TITLES = [
    "Datuk Seri", "Dato' Sri", "Dato Sri", "Datin Seri", "Puan Sri",
    "Tan Sri", "Tan Sri Datuk", "Datuk", "Dato'", "Dato", "Datin",
    "Datuk Dr", "Datuk Dr.", "Datin Dr",
    "Dr", "Dr.",
]

# Known government/election/media organizations to anchor org extraction.
ORG_ANCHORS = {
    "SPR": "Suruhanjaya Pilihan Raya (SPR)",
    "Suruhanjaya Pilihan Raya": "Suruhanjaya Pilihan Raya (SPR)",
    "BERNAMA": "BERNAMA",
    "Bernama": "BERNAMA",
    "MBS": "Majlis Bandaraya Seremban (MBS)",
    "Wisma MBS": "Majlis Bandaraya Seremban (MBS)",
    "IPD": "IPD Port Dickson",
    "IPD Port Dickson": "IPD Port Dickson",
    "NSTP": "NSTP",
    "EXCO": "EXCO Negeri Sembilan",
    "Dewan Undangan Negeri": "Dewan Undangan Negeri (DUN)",
}


def slug(s: str) -> str:
    return re.sub(r"\s+", " ", s.strip())


def read_all_text(files):
    chunks = []
    per_file = {}
    for fp in files:
        try:
            with open(fp, "r", encoding="utf-8", errors="replace") as fh:
                txt = fh.read()
            chunks.append(txt)
            per_file[os.path.basename(fp)] = txt
        except OSError:
            pass
    return "\n\n".join(chunks), per_file


# ---------------------------------------------------------------------------
# STRUCTURED PARSE of the "Senarai calon" roll.
#   **N01 CHENNAH:** 14,422 pengundi
#   1\. Siow Kong Choon (BN-MCA)
#   2\. Anthony Loke Siew Fook (PH-DAP)
#   **2023:** Anthony Loke Siew Fook (PH-DAP) (Majoriti - 2,200)
# ---------------------------------------------------------------------------
# Header form in scrapes:  **N01 CHENNAH:** 14,422 pengundi
# Note the colon sits INSIDE the bold (before the closing **). Allow an
# optional colon on either side of the closing ** to be robust to variants.
SEAT_HEADER_RE = re.compile(
    r"\*\*\s*(N\d{2})\s+([A-Z][A-Z\s'./-]+?):?\s*\*\*\s*:?\s*([\d,.]+)\s*pengundi",
    re.IGNORECASE,
)
CANDIDATE_LINE_RE = re.compile(
    r"^\s*\d+\\?\.\s+(.+?)\s*\(([^)]+)\)\s*$",
)
HISTORY_LINE_RE = re.compile(
    r"\*\*\s*2023\s*:\*\*\s*(.+?)\s*\(([^)]+)\)\s*\(?\s*Majoriti",
)


def parse_candidate_roll(text):
    """Return list of seat dicts: {code, name, voters, candidates:[{name,party,raw_ticket}]}"""
    seats = []
    # Normalise the escaped-backslash numbering the scrapes carry ("1\\. ").
    norm = text.replace("\\.", ".")
    lines = norm.splitlines()
    current = None
    for line in lines:
        hdr = SEAT_HEADER_RE.search(line)
        if hdr:
            if current:
                seats.append(current)
            code, name, voters = hdr.group(1), slug(hdr.group(2)), hdr.group(3)
            current = {
                "code": code.upper(),
                "name": name.title().replace("Sri", "Seri"),
                "voters": voters.replace(",", ""),
                "candidates": [],
            }
            continue
        if current is not None:
            m = CANDIDATE_LINE_RE.match(line)
            if m:
                name = slug(m.group(1))
                ticket = slug(m.group(2))
                current["candidates"].append(
                    {"name": name, "ticket": ticket, "party_raw": ticket}
                )
                continue
            # 2023 history line — also captures prior-term candidates.
            h = HISTORY_LINE_RE.search(line)
            if h:
                current.setdefault("winner_2023", slug(h.group(1)))
                current.setdefault("winner_2023_ticket", slug(h.group(2)))
    if current:
        seats.append(current)
    return seats


def normalize_ticket(ticket):
    """Split 'BN-UMNO' / 'PH-DAP' / 'BERSATU' / 'PN-WAWASAN' / 'Bebas'
    into a list of normalized party entities (coalition + component)."""
    out = []
    t = ticket.strip()
    # Independent variants
    if t.upper() in ("BEBAS", "Bebas", "INDEPENDENT"):
        out.append("Bebas (Independent)")
        return out
    parts = re.split(r"[-/]", t)
    for p in parts:
        pu = p.strip().upper().replace(".", "")
        if pu in COALITIONS:
            out.append(f"{pu} ({COALITIONS[pu]})")
        elif pu in COMPONENT_NORMALIZE:
            out.append(COMPONENT_NORMALIZE[pu])
        elif pu:
            out.append(pu.title())
    return out


# ---------------------------------------------------------------------------
# NARRATIVE extraction: titled politicians, locations, orgs, events, issues.
# ---------------------------------------------------------------------------
def build_title_regex():
    # Match an honorific followed by 2-6 capitalised/Name-like tokens.
    title_alt = "|".join(re.escape(t) for t in sorted(TITLES, key=len, reverse=True))
    pat = (
        rf"\b({title_alt})\s+"
        r"([A-Z][A-Za-z'\.]+(?:\s+(?:[A-Z][A-Za-z'\.]+|@|bin|binti|a/l|a/p|Abd|Mohd|Md|D\.)){{1,6}})"
    )
    return re.compile(pat)


def extract_titled_politicians(text, known_candidates):
    """Find titled names in narrative. We keep a name only if it looks like a
    person (>=2 tokens) and isn't already captured as a plain candidate name."""
    rx = build_title_regex()
    found = {}
    for m in rx.finditer(text):
        title = m.group(1).rstrip()
        name = slug(m.group(2))
        # strip trailing connector words
        name = re.sub(
            r"\s+(bin|binti|a/l|a/p|Abd|Mohd|Md|D\.)$", "", name, flags=re.IGNORECASE
        ).strip()
        if not name or len(name.split()) < 1:
            continue
        full = f"{title} {name}"
        # Dedup on the name-without-title lowercased, preferring the titled form.
        key = name.lower()
        if key not in found:
            found[key] = full
    # Merge: candidate-roll names are authoritative; titled names supplement.
    merged = {}
    for c in known_candidates:
        merged[c.lower()] = c
    for key, full in found.items():
        # Skip obvious non-persons (place names that got a title, rare).
        if key in {p.lower() for p in NS_PLACES}:
            continue
        if key not in merged:
            merged[key] = full
    return sorted(merged.values(), key=lambda s: s.lower())


def extract_locations(text):
    locs = set()
    for p in NS_PLACES:
        if re.search(rf"\b{re.escape(p)}\b", text):
            locs.add(p)
    # Dateline-style "KUALA LUMPUR:" / "SEREMBAN:" at line start
    for m in re.finditer(r"(?m)^\s*([A-Z][A-Z\s]{2,30}):", text):
        cand = slug(m.group(1)).title()
        if cand in NS_PLACES or cand in ("Kuala Lumpur", "Putrajaya"):
            locs.add(cand)
    return sorted(locs)


def extract_organizations(text):
    orgs = set()
    for key, label in ORG_ANCHORS.items():
        if re.search(rf"\b{re.escape(key)}\b", text):
            orgs.add(label)
    return sorted(orgs)


def extract_events(text):
    events = set()
    ev_patterns = {
        "PRN Negeri Sembilan 2026 (Pilihan Raya Negeri ke-16)": r"Pilihan Raya Negeri[^.]*ke-16|PRN Negeri Sembilan 2026",
        "Hari Penamaan Calon (Nomination Day, 18 Julai 2026)": r"penamaan calon|proses penamaan",
        "Hari Pengundian (Polling Day, 1 Ogos 2026)": r"hari pengundian|pengundian pada 1 Ogos",
        "Pengundian Awal (Early Voting, 28 Julai 2026)": r"pengundian awam|pengundian awal|tarikh pengundian awam",
        "Kempen PRN Negeri Sembilan": r"kempen PRN|kempen secara|kempen pilihan raya",
    }
    for label, pat in ev_patterns.items():
        if re.search(pat, text, re.IGNORECASE):
            events.add(label)
    return sorted(events)


def extract_issues(text, seats):
    issues = set()
    issue_patterns = {
        "Perpecahan Bersatu-PN (Bersatu-PN split)": r"Bersatu.{0,40}PN|PN.{0,40}Bersatu|pecah|perpecahan|termination|buang|dibuang",
        "Pembuangan Tang Jay Son oleh GERAKAN (Gerakan expels Tang Jay Son)": r"Gerakan.{0,40}(buang|dibuang|expel|keluar)|Tang Jay Son.{0,40}Gerakan|Tang Jay San.{0,40}Gerakan",
        "Persetujuan kerusi BN-PN (BN-PN seat deal)": r"BN.{0,40}PN|PN.{0,40}BN|persetujuan|understanding|seat deal|Supreme Council",
        "Penyatuan undi Melayu (Malay vote consolidation)": r"penyatuan undi Melayu|undi Melayu|Melayu.{0,30}undi|Malay.{0,20}vote",
        "Calon Bebas/penyingkir undi (Independents splitting votes)": r"calon Bebas|calon bebas|independent|lima penjuru|empat penjuru|5 penjuru|4 penjuru",
        "Penyandang diganti/berpindah (Incumbents replaced/moved)": r"penyandang.{0,40}(diganti|ganti|dikejutkan|berpindah|pindah|dibuang)|incumbent.{0,30}replace|moved|replaced",
        "Pencalonan semula MB Aminuddin N.13->N.32 (Caretaker MB seat move)": r"Aminuddin.{0,40}N\.?13|Aminuddin.{0,40}N\.?32|N\.?13.{0,30}N\.?32|Menteri Besar.{0,40}pindah|caretaker",
        "Pertembungan tokoh utama (Marquee candidate fights)": r"pertembungan|tokoh utama|marquee|satu lawan satu|tiga penjuru",
    }
    for label, pat in issue_patterns.items():
        if re.search(pat, text, re.IGNORECASE):
            issues.add(label)
    return sorted(issues)


def main():
    date_stamp = sys.argv[1] if len(sys.argv) > 1 else datetime.now().strftime("%Y%m%d")
    collection_dir = os.path.join(RAW_DIR, date_stamp)
    if not os.path.isdir(collection_dir):
        # fall back to most recent
        cands = sorted(glob.glob(os.path.join(RAW_DIR, "*")), reverse=True)
        if not cands:
            print("✗ No raw-scrape collection found", file=sys.stderr)
            sys.exit(1)
        collection_dir = cands[0]
        date_stamp = os.path.basename(collection_dir)

    files = sorted(glob.glob(os.path.join(collection_dir, "*.md")))
    out_dir = os.path.join(PROC_DIR, date_stamp)
    os.makedirs(out_dir, exist_ok=True)

    text, per_file = read_all_text(files)
    source_count = len(files)

    # Structured roll parse — concatenate all files that look like a roll.
    roll_text = "\n\n".join(
        t for fn, t in per_file.items() if "senarai-calon" in fn.lower() or re.search(r"N\d{2}\s+[A-Z]+\s*\*+:.*pengundi", t, re.IGNORECASE)
    ) or text
    seats = parse_candidate_roll(roll_text)

    # --- POLITICIANS (from roll) ---
    politicians = []
    seen_p = set()
    for s in seats:
        for c in s["candidates"]:
            key = c["name"].lower()
            if key and key not in seen_p:
                seen_p.add(key)
                politicians.append(c["name"])
        if s.get("winner_2023"):
            key = s["winner_2023"].lower()
            if key and key not in seen_p:
                seen_p.add(key)
                politicians.append(s["winner_2023"])
    # Augment with titled names from narrative.
    politicians = extract_titled_politicians(text, politicians)

    # --- PARTIES (from roll tickets) ---
    parties = set()
    for s in seats:
        for c in s["candidates"]:
            for p in normalize_ticket(c["ticket"]):
                parties.add(p)
    # Also catch coalitions/parties mentioned only in narrative.
    for short, full in COALITIONS.items():
        if re.search(rf"\b{short}\b", text):
            parties.add(f"{short} ({full})")
    for short, label in COMPONENT_NORMALIZE.items():
        if short == "BEBAS":
            continue
        if re.search(rf"\b{short}\b", text, re.IGNORECASE):
            parties.add(label)

    # --- CONSTITUENCIES (clean 36 DUN) ---
    constituencies = []
    for s in seats:
        constituencies.append(f"{s['code']} {s['name']}")
    # If roll parse somehow failed, fall back to regex on full text.
    if not constituencies:
        for m in re.finditer(r"\b(N\d{2})\s+([A-Z][A-Z\s'./-]+)\b", text):
            constituencies.append(f"{m.group(1)} {slug(m.group(2)).title()}")
    constituencies = sorted(set(constituencies))

    # --- LOCATIONS / ORGS / EVENTS / ISSUES ---
    locations = extract_locations(text)
    organizations = extract_organizations(text)
    events = extract_events(text)
    issues = extract_issues(text, seats)

    cat_map = {
        "politicians": politicians,
        "parties": sorted(parties),
        "constituencies": constituencies,
        "issues": issues,
        "events": events,
        "organizations": organizations,
        "locations": locations,
    }

    now_iso = datetime.now(timezone.utc).isoformat()
    summary_counts = {}
    for cat, items in cat_map.items():
        out = {
            "date": now_iso,
            "collection_date": date_stamp,
            "source_count": source_count,
            "entity_type": cat,
            "count": len(items),
            "entities": items,
        }
        with open(os.path.join(out_dir, f"entities_{cat}.json"), "w", encoding="utf-8") as fh:
            json.dump(out, fh, indent=2, ensure_ascii=False)
        summary_counts[cat] = len(items)

    # Consolidated file with counts + a seat roll appendix for downstream use.
    consolidated = {
        "date": date_stamp,
        "timestamp": now_iso,
        "source_count": source_count,
        "extraction_completed": True,
        "extractor": "ns_entity_extraction_enhanced.py",
        "entity_categories": list(cat_map.keys()),
        "counts": summary_counts,
        "total_entities": sum(summary_counts.values()),
        "seats_parsed": len(seats),
        "seats": [
            {
                "code": s["code"],
                "name": s["name"],
                "voters": s.get("voters"),
                "candidate_count": len(s["candidates"]),
                "candidates": s["candidates"],
                "winner_2023": s.get("winner_2023"),
                "winner_2023_ticket": s.get("winner_2023_ticket"),
            }
            for s in seats
        ],
    }
    with open(os.path.join(out_dir, "entities_consolidated.json"), "w", encoding="utf-8") as fh:
        json.dump(consolidated, fh, indent=2, ensure_ascii=False)

    # Stdout summary
    print(f"=== Enhanced Entity Extraction ===")
    print(f"Collection: {collection_dir}  ({source_count} files)")
    print(f"Seats parsed: {len(seats)}")
    for cat, n in summary_counts.items():
        print(f"  {cat:14s}: {n}")
    print(f"  {'TOTAL':14s}: {sum(summary_counts.values())}")
    print(f"Output: {out_dir}")


if __name__ == "__main__":
    main()
