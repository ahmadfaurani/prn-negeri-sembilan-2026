#!/usr/bin/env python3
"""
Negeri Sembilan PRN 2026 - Source-Attributed Entity Extraction
================================================================
CVS STANDARD: All extracted entities must be source-attributed.
              No pattern-inferred entities.

This extractor emits ONLY entities whose surface form literally appears
in a collected source file. Every emitted entity is attributed to:
  - source_file   : the collected .md file
  - source_outlet : the news outlet (parsed from filename)
  - context       : the verbatim source line/span where the surface form occurs
  - occurrences   : number of grounded occurrences across the corpus

Gazetteers (party aliases, known politicians, known NS constituencies,
organisations, issues, events, locations) are used as PRECISION match
keys -- a gazetteer entry is only emitted if its surface form is actually
present in the source text. Nothing is fabricated or inferred from
context. This eliminates loose-pattern false positives (e.g. "bersama")
that the original regex script produced.

Usage:
    python3 ns_entity_extraction_sourced.py
"""
import json
import os
import re
import glob
from collections import defaultdict

WORKSPACE = "/home/p62operator/.openclaw/workspace-ns"
RAW_DIR = os.path.join(WORKSPACE, "04-DATA-AND-SOURCES/raw-scrapes")
OUT_DIR = os.path.join(WORKSPACE, "04-DATA-AND-SOURCES/processed-entities")

# ------------------------------------------------------------------ #
#  DATE STAMP: use the most recent collection directory
# ------------------------------------------------------------------ #
def find_collection_dir():
    dirs = sorted(
        [d for d in glob.glob(os.path.join(RAW_DIR, "*")) if os.path.isdir(d)],
        reverse=True,
    )
    if not dirs:
        raise SystemExit("No collection directory found under " + RAW_DIR)
    return dirs[0], os.path.basename(dirs[0])

# ------------------------------------------------------------------ #
#  GAZETTEERS -- precision match keys.  Each entry:
#    canonical : the standard name to record
#    surfaces  : list of surface forms that, if present in text, count
#                as a grounded occurrence of this entity.
#  Surfaces are matched case-insensitively BUT short all-caps
#  abbreviations (<=4 chars) are matched with a word boundary and
#  require the exact-case token OR standalone usage to avoid false hits.
# ------------------------------------------------------------------ #

PARTIES = [
    {"canonical": "Pakatan Harapan (PH)", "surfaces": ["Pakatan Harapan", "PH"]},
    {"canonical": "Barisan Nasional (BN)", "surfaces": ["Barisan Nasional", "BN"]},
    {"canonical": "Perikatan Nasional (PN)", "surfaces": ["Perikatan Nasional", "PN"]},
    {"canonical": "UMNO", "surfaces": ["UMNO", "Umno"]},
    {"canonical": "PKR", "surfaces": ["PKR"]},
    {"canonical": "DAP", "surfaces": ["DAP"]},
    {"canonical": "PAS", "surfaces": ["PAS", "Pas"]},
    {"canonical": "Bersatu (PPBM)", "surfaces": ["Bersatu", "BERSATU", "PPBM"]},
    {"canonical": "MUDA", "surfaces": ["MUDA"]},
    {"canonical": "AMANAH", "surfaces": ["Amanah", "AMANAH"]},
    {"canonical": "GERAKAN", "surfaces": ["Gerakan", "GERAKAN"]},
    {"canonical": "WARISAN", "surfaces": ["Warisan", "WARISAN"]},
    {"canonical": "PBM", "surfaces": ["PBM"]},
    {"canonical": "KITA", "surfaces": ["Parti KITA", "KITA"]},
]

# Known Malaysian politicians likely to feature in PRN NS coverage.
# Emitted ONLY if a surface form literally appears in a source file.
POLITICIANS = [
    {"canonical": "Anwar Ibrahim", "surfaces": ["Anwar Ibrahim", "Anwar"]},
    {"canonical": "Ahmad Zahid Hamidi", "surfaces": ["Ahmad Zahid Hamidi", "Zahid Hamidi", "Zahid"]},
    {"canonical": "Muhyiddin Yassin", "surfaces": ["Muhyiddin Yassin", "Muhyiddin"]},
    {"canonical": "Syed Saddiq Syed Abdul Rahman", "surfaces": ["Syed Saddiq Syed Abdul Rahman", "Syed Saddiq"]},
    {"canonical": "Ong Kian Ming", "surfaces": ["Ong Kian Ming"]},
    {"canonical": "Ahmad Fadhli Shaari", "surfaces": ["Ahmad Fadhli Shaari", "Fadhli Shaari"]},
    {"canonical": "Zambry Abdul Kadir", "surfaces": ["Zambry Abdul Kadir", "Zambry"]},
    {"canonical": "Akmal Nasrullah", "surfaces": ["Akmal Nasrullah"]},
    {"canonical": "Dzulkefly Ahmad", "surfaces": ["Dzulkefly"]},
    {"canonical": "Sultan Ibrahim (King of Malaysia)", "surfaces": ["Sultan Ibrahim"]},
    {"canonical": "Aminuddin Harun (Menteri Besar NS)", "surfaces": ["Aminuddin Harun", "Aminuddin"]},
    {"canonical": "Mohamad Hasan", "surfaces": ["Mohamad Hasan", "Mat Hasan"]},
    {"canonical": "Khairy Jamaluddin", "surfaces": ["Khairy Jamaluddin", "Khairy"]},
    {"canonical": "Tharman Shanmugaratnam", "surfaces": ["Tharman"]},
]

# Negeri Sembilan constituencies / seats.  Emitted ONLY if the surface
# form literally appears in a source file (so no fabrication of the full
# 36-DUN list when the corpus does not mention them).
NS_CONSTITUENCIES = [
    {"canonical": "Negeri Sembilan (state)", "surfaces": ["Negeri Sembilan", "Negri Sembilan", "Negeri Sembilan"]},
    {"canonical": "Port Dickson (P132)", "surfaces": ["Port Dickson", "Port Dickson "]},
    {"canonical": "Tampin (P134)", "surfaces": ["Tampin"]},
    {"canonical": "Rembau (P133)", "surfaces": ["Rembau"]},
    {"canonical": "Rasah (P130)", "surfaces": ["Rasah"]},
    {"canonical": "Seremban (P137)", "surfaces": ["Seremban"]},
    {"canonical": "Jelebu (P135)", "surfaces": ["Jelebu"]},
    {"canonical": "Jempol (P136)", "surfaces": ["Jempol"]},
    {"canonical": "Kuala Pilah (P131)", "surfaces": ["Kuala Pilah"]},
    {"canonical": "Linggi (DUN)", "surfaces": ["Linggi"]},
    {"canonical": "Rantau (DUN)", "surfaces": ["Rantau"]},
    {"canonical": "Chembong (DUN)", "surfaces": ["Chembong"]},
    {"canonical": "Kota (DUN)", "surfaces": ["Kota "]},
    {"canonical": "Paroi (DUN)", "surfaces": ["Paroi"]},
    {"canonical": "Pilah (DUN)", "surfaces": ["Pilah"]},
    {"canonical": "Lenggeng (DUN)", "surfaces": ["Lenggeng"]},
    {"canonical": "Mantin (DUN)", "surfaces": ["Mantin"]},
    {"canonical": "Lobak (DUN)", "surfaces": ["Lobak"]},
    {"canonical": "Rahang (DUN)", "surfaces": ["Rahang"]},
    {"canonical": "Seremban Jaya (DUN)", "surfaces": ["Seremban Jaya"]},
    {"canonical": "Temiang (DUN)", "surfaces": ["Temiang"]},
    {"canonical": "Senawang (DUN)", "surfaces": ["Senawang"]},
    {"canonical": "Lukut (DUN)", "surfaces": ["Lukut"]},
    {"canonical": "Chuah (DUN)", "surfaces": ["Chuah"]},
    {"canonical": "Bagan Pinang (DUN)", "surfaces": ["Bagan Pinang"]},
    {"canonical": "Sikamat (DUN)", "surfaces": ["Sikamat"]},
    {"canonical": "Ampangan (DUN)", "surfaces": ["Ampangan"]},
    {"canonical": "Klawang (DUN)", "surfaces": ["Klawang"]},
    {"canonical": "Sungai Lui (DUN)", "surfaces": ["Sungai Lui"]},
    {"canonical": "Kemenah (DUN)", "surfaces": ["Kemenah"]},
    {"canonical": "Jeram Padang (DUN)", "surfaces": ["Jeram Padang"]},
    {"canonical": "Johol (DUN)", "surfaces": ["Johol"]},
    {"canonical": "Serting (DUN)", "surfaces": ["Serting"]},
    {"canonical": "Palong (DUN)", "surfaces": ["Palong"]},
    {"canonical": "Gemencheh (DUN)", "surfaces": ["Gemencheh"]},
    {"canonical": "Gemas (DUN)", "surfaces": ["Gemas"]},
    {"canonical": "Repah (DUN)", "surfaces": ["Repah"]},
    # NS royalty-linked place (parliamentary Tampin area)
    {"canonical": "Port Dickson / PD", "surfaces": ["PD"]},
    # Pagoh is Johor (context re Muhyiddin) -- kept as a constituency mention
    {"canonical": "Pagoh (Johor, parliamentary)", "surfaces": ["Pagoh"]},
]

ORGANIZATIONS = [
    {"canonical": "Defence Ministry", "surfaces": ["Defence Ministry", "Kementerian Pertahanan"]},
    {"canonical": "Health Ministry", "surfaces": ["Health Ministry", "Kementerian Kesihatan"]},
    {"canonical": "National Registration Department (NRD)", "surfaces": ["National Registration Department", "NRD", "JPN"]},
    {"canonical": "Armed Forces Fund Board (LTAT)", "surfaces": ["Armed Forces Fund Board", "LTAT"]},
    {"canonical": "Malaysian Maritime Enforcement Agency (MMEA/APMM)", "surfaces": ["Malaysian Maritime Enforcement Agency", "MMEA", "APMM"]},
    {"canonical": "Malaysian Media Council (MMM)", "surfaces": ["Malaysian Media Council", "MMM"]},
    {"canonical": "UNHCR", "surfaces": ["UNHCR", "United Nations High Commissioner for Refugees"]},
    {"canonical": "Ketech Asia Sdn Bhd", "surfaces": ["Ketech Asia"]},
    {"canonical": "Air Selangor", "surfaces": ["Air Selangor"]},
    {"canonical": "McDonald's Malaysia", "surfaces": ["McDonald's Malaysia", "McDonald\u2019s Malaysia", "McDonalds Malaysia"]},
    {"canonical": "Persatuan Kebajikan Ronald McDonald (RHMC)", "surfaces": ["Persatuan Kebajikan Ronald McDonald", "RHMC"]},
    {"canonical": "BERNAMA", "surfaces": ["BERNAMA", "Bernama"]},
    {"canonical": "PDRM", "surfaces": ["PDRM"]},
    {"canonical": "Armed Forces (Malaysia)", "surfaces": ["Armed Forces"]},
    {"canonical": "Dewan Rakyat", "surfaces": ["Dewan Rakyat"]},
    {"canonical": "Parliament", "surfaces": ["Parliament", "parliament"]},
    {"canonical": "Sessions Court", "surfaces": ["Sessions Court"]},
    {"canonical": "Attorney-General / Public Prosecutor", "surfaces": ["Attorney-General", "Public Prosecutor"]},
    {"canonical": "Star Media Group", "surfaces": ["Star Media Group"]},
    {"canonical": "Media Mulia Sdn Bhd", "surfaces": ["Media Mulia"]},
    {"canonical": "Special Select Committee", "surfaces": ["Special Select Committee"]},
    {"canonical": "AKPS", "surfaces": ["AKPS"]},
]

EVENTS = [
    {"canonical": "Negeri Sembilan state election (PRN NS 2026)", "surfaces": ["Negri Sembilan election", "Negeri Sembilan election", "Negri Sembilan state election", "state election"]},
    {"canonical": "Johor state election (PRN Johor)", "surfaces": ["PRN Johor", "Johor election", "Keputusan-PRN-Johor"]},
    {"canonical": "FIFA World Cup 2026 / Piala Dunia 2026", "surfaces": ["World Cup", "Piala Dunia"]},
    {"canonical": "Jelajah Wira Madani", "surfaces": ["Jelajah Wira Madani", "Wira Madani"]},
    {"canonical": "Hari Keputeraan Ke-77 Yang di-Pertuan Besar Negeri Sembilan", "surfaces": ["Hari Keputeraan", "Yang di-Pertuan Besar Negeri Sembilan", "Yang Dipertuan Besar Negeri Sembilan"]},
    {"canonical": "Qatar official mourning", "surfaces": ["Qatar's official mourning", "official mourning"]},
    {"canonical": "Muhyiddin trial (Nepturis)", "surfaces": ["Muhyiddin trial", "Nepturis"]},
    {"canonical": "Syed Saddiq acquittal", "surfaces": ["Syed Saddiq walks free", "six-year legal battle", "acquitted"]},
    {"canonical": "Dewan Rakyat sitting", "surfaces": ["Dewan Rakyat hari ini", "tumpuan Dewan Rakyat"]},
]

ISSUES = [
    {"canonical": "Marginal seats / election competitiveness", "surfaces": ["marginal seats", "tighter race", "tighter races", "unpredictable state election"]},
    {"canonical": "Umno-Pas alliance", "surfaces": ["Umno-Pas alliance", "Umno-Pas", "Formal Umno-Pas alliance"]},
    {"canonical": "Cost of living", "surfaces": ["kos sara hidup", "cost of living", "kos sara"]},
    {"canonical": "Climate change law", "surfaces": ["Climate Change Bill", "climate law"]},
    {"canonical": "Floods (banjir)", "surfaces": ["banjir", "Mangsa banjir", "flood"]},
    {"canonical": "Cyberbullying", "surfaces": ["cyberbullying", "cyberbully"]},
    {"canonical": "Fuel supply / oil market volatility", "surfaces": ["fuel supply", "oil market volatility", "Brent crude"]},
    {"canonical": "AG-Public Prosecutor separation", "surfaces": ["AG-public prosecutor separation", "separation of roles", "separation of the Attorney-General"]},
    {"canonical": "Freedom of Information Bill (FOI Bill)", "surfaces": ["FOI Bill", "Freedom of Information"]},
    {"canonical": "Johor-Singapore SEZ (JS-SEZ)", "surfaces": ["JS-SEZ", "Johor-Singapore Special Economic Zone"]},
    {"canonical": "Net Disposable Income (NDI) welfare model", "surfaces": ["Net Disposable Income", "NDI"]},
    {"canonical": "LINDUNG scheme", "surfaces": ["LINDUNG"]},
    {"canonical": "Corruption / money laundering (Syed Saddiq case)", "surfaces": ["corruption and money laundering"]},
    {"canonical": "Pension fund dividend (LTAT/ASSAR)", "surfaces": ["dividend", "pension fund"]},
    {"canonical": "MyKAS / citizenship", "surfaces": ["MyKas", "kad pengenalan", "warganegara"]},
    {"canonical": "Selat Hormuz / Gulf conflict", "surfaces": ["Selat Hormuz", "Strait of Hormuz", "Gulf conflict"]},
    {"canonical": "Imigration enforcement", "surfaces": ["operasi bersepadu imigresen", "imigresen"]},
]

LOCATIONS = [
    {"canonical": "Negeri Sembilan", "surfaces": ["Negeri Sembilan", "Negri Sembilan"]},
    {"canonical": "Kuala Lumpur", "surfaces": ["Kuala Lumpur"]},
    {"canonical": "Petaling Jaya", "surfaces": ["Petaling Jaya"]},
    {"canonical": "Putrajaya", "surfaces": ["Putrajaya"]},
    {"canonical": "Johor", "surfaces": ["Johor"]},
    {"canonical": "Johor Baru", "surfaces": ["Johor Baru"]},
    {"canonical": "Melaka", "surfaces": ["Melaka"]},
    {"canonical": "Selangor", "surfaces": ["Selangor"]},
    {"canonical": "Sabah", "surfaces": ["Sabah"]},
    {"canonical": "Sarawak", "surfaces": ["Sarawak"]},
    {"canonical": "Penang / Pulau Pinang", "surfaces": ["Penang", "Pulau Pinang"]},
    {"canonical": "Kuching", "surfaces": ["Kuching"]},
    {"canonical": "George Town", "surfaces": ["George Town"]},
    {"canonical": "Kota Kinabalu", "surfaces": ["Kota Kinabalu"]},
    {"canonical": "Kota Baru", "surfaces": ["Kota Baru", "Kota Bharu"]},
    {"canonical": "Kuantan", "surfaces": ["Kuantan"]},
    {"canonical": "Beaufort", "surfaces": ["Beaufort"]},
    {"canonical": "Tampin", "surfaces": ["Tampin"]},
    {"canonical": "Port Dickson", "surfaces": ["Port Dickson"]},
    {"canonical": "Pagoh", "surfaces": ["Pagoh"]},
    {"canonical": "Denai Alam", "surfaces": ["Denai Alam"]},
    {"canonical": "Muar", "surfaces": ["Muar"]},
    {"canonical": "Bangi", "surfaces": ["Bangi"]},
]

CATEGORY_GAZETTEERS = {
    "politicians": POLITICIANS,
    "parties": PARTIES,
    "constituencies": NS_CONSTITUENCIES,
    "organizations": ORGANIZATIONS,
    "events": EVENTS,
    "issues": ISSUES,
    "locations": LOCATIONS,
}

# Surfaces that are short all-caps abbreviations and need exact-case or
# strict word-boundary matching to avoid false positives.
STRICT_ABBREV = {"PH", "BN", "PN", "DAP", "PKR", "PAS", "UMNO", "MUDA", "AMANAH",
                 "GERAKAN", "WARISAN", "PBM", "KITA", "PPBM", "NRD", "LTAT",
                 "MMEA", "APMM", "MMM", "UNHCR", "PDRM", "AKPS", "NDI", "FOI",
                 "PD", "JS-SEZ", "LINDUNG", "MyKas", "RHMC"}

# Per-surface overrides to suppress common-word false positives and so
# honour the CVS "no pattern-inferred entities" rule.
#  - SURFACE_CASE_SENSITIVE : match case-sensitively (capital form required)
#    e.g. 'Bersatu' (the party) vs lowercase 'bersatu' (Malay verb 'to unite').
#  - SURFACE_EXCLUDE_AFTER  : reject a surface when immediately followed by a
#    given token, e.g. 'Amanah' followed by 'Saham' = Amanah Saham Sarawak
#    (a unit-trust fund), NOT the AMANAH political party.
SURFACE_CASE_SENSITIVE = {"Bersatu", "BERSATU"}
SURFACE_EXCLUDE_AFTER = {"Amanah": "Saham"}


def surface_to_regex(surface):
    """Build a regex for a surface form.

    Short abbreviations (STRICT_ABBREV) and case-sensitive surfaces are
    matched case-sensitively with word boundaries. SURFACE_EXCLUDE_AFTER
    appends a negative lookahead so a surface is rejected when followed by
    a disambiguating token (preventing common-word false positives)."""
    s = re.escape(surface)
    excl = SURFACE_EXCLUDE_AFTER.get(surface)
    tail = r"(?!\s*" + re.escape(excl) + r")" if excl else ""
    if surface in STRICT_ABBREV or surface in SURFACE_CASE_SENSITIVE:
        # case-sensitive, word-bounded
        return re.compile(r"(?<![A-Za-z0-9])" + s + r"(?![A-Za-z0-9])" + tail)
    # case-insensitive, word-bounded
    return re.compile(r"(?<![A-Za-z0-9])" + s + r"(?![A-Za-z0-9])" + tail,
                      re.IGNORECASE)


def outlet_from_filename(fname):
    base = os.path.basename(fname)
    # e.g. thestarcommy_20260714_010109.md -> thestar.com.my
    name = base.split("_")[0]
    mapping = {
        "thestarcommy": "thestar.com.my",
        "nstcommy": "nst.com.my",
        "bhariancommy": "bharian.com.my",
        "malaysiakinicom": "malaysiakini.com",
        "astroawanicom": "astroawani.com",
        "kosmocommy": "kosmo.com.my",
        "mstarcommy": "mstar.com.my",
        "utusancommy": "utusan.com.my",
        "ohbulancom": "ohbulan.com",
    }
    return mapping.get(name, name)


def clean_context(line, maxlen=240):
    """Trim and lightly clean a context line for attribution."""
    t = line.strip()
    t = re.sub(r"\s+", " ", t)
    if len(t) > maxlen:
        t = t[:maxlen].rstrip() + "..."
    return t


def main():
    coll_dir, date_stamp = find_collection_dir()
    out_subdir = os.path.join(OUT_DIR, date_stamp)
    os.makedirs(out_subdir, exist_ok=True)

    md_files = sorted(glob.glob(os.path.join(coll_dir, "*.md")))
    print("=== NS PRN 2026 - Source-Attributed Entity Extraction ===")
    print("Collection dir :", coll_dir)
    print("Date stamp     :", date_stamp)
    print("Source files   :", len(md_files))
    print()

    # Pre-compile regexes per surface.
    compiled = {}  # category -> list of (canonical, surface, regex)
    for cat, gaz in CATEGORY_GAZETTEERS.items():
        compiled[cat] = []
        for entry in gaz:
            for surf in entry["surfaces"]:
                compiled[cat].append((entry["canonical"], surf, surface_to_regex(surf)))

    # results[category][canonical] = {surface_forms:set, sources:set, contexts:list, count:int}
    results = {cat: defaultdict(lambda: {
        "surface_forms": set(),
        "sources": set(),
        "outlets": set(),
        "contexts": [],
        "count": 0,
    }) for cat in CATEGORY_GAZETTEERS}

    sources_meta = []
    for f in md_files:
        outlet = outlet_from_filename(f)
        try:
            with open(f, encoding="utf-8", errors="replace") as fh:
                content = fh.read()
        except OSError as e:
            print("  ! could not read", f, e)
            continue

        # crude signal: is this a 404 / empty page?
        is_404 = bool(re.search(r"404|Halaman Tidak Dijumpai|tidak ditemui|tidak wujud|page you are looking for|Maafkan Kami|Oops", content, re.IGNORECASE))
        sources_meta.append({
            "source_file": os.path.basename(f),
            "outlet": outlet,
            "chars": len(content),
            "appears_404": is_404,
        })

        lines = content.splitlines()
        for cat, entries in compiled.items():
            for canonical, surf, rx in entries:
                # search line by line for grounded context attribution
                hit = False
                for ln in lines:
                    if rx.search(ln):
                        hit = True
                        rec = results[cat][canonical]
                        rec["surface_forms"].add(surf)
                        rec["sources"].add(os.path.basename(f))
                        rec["outlets"].add(outlet)
                        ctx = clean_context(ln)
                        if len(rec["contexts"]) < 3:
                            rec["contexts"].append(ctx)
                        rec["count"] += 1
                # (if no hit, nothing is emitted -- no inference)

    # ------------------------------------------------------------------ #
    #  Write per-category JSON (source-attributed)
    # ------------------------------------------------------------------ #
    summary = {}
    for cat in CATEGORY_GAZETTEERS:
        out = []
        for canonical, rec in results[cat].items():
            out.append({
                "entity": canonical,
                "surface_forms": sorted(rec["surface_forms"]),
                "occurrences": rec["count"],
                "source_files": sorted(rec["sources"]),
                "source_outlets": sorted(rec["outlets"]),
                "context_samples": rec["contexts"],
            })
        out.sort(key=lambda x: (-x["occurrences"], x["entity"]))
        payload = {
            "date": date_stamp,
            "category": cat,
            "method": "gazetteer-grounded, source-attributed (verbatim surface match)",
            "cvs_standard": "TLP:AMBER - all entities source-attributed; no pattern-inferred entities",
            "source_count": len(md_files),
            "entity_count": len(out),
            "entities": out,
        }
        fname = os.path.join(out_subdir, "sourced_entities_%s.json" % cat)
        with open(fname, "w", encoding="utf-8") as fh:
            json.dump(payload, fh, indent=2, ensure_ascii=False)
        summary[cat] = len(out)
        print("  -> %-16s %3d entities  (%s)" % (cat, len(out), fname))

    # ------------------------------------------------------------------ #
    #  Consolidated file
    # ------------------------------------------------------------------ #
    consolidated = {
        "date": date_stamp,
        "method": "gazetteer-grounded, source-attributed (verbatim surface match)",
        "cvs_standard": "TLP:AMBER - all entities source-attributed; no pattern-inferred entities",
        "source_count": len(md_files),
        "sources": sources_meta,
        "entity_counts": summary,
        "total_entities": sum(summary.values()),
        "categories": list(CATEGORY_GAZETTEERS.keys()),
        "note": ("Only entities whose surface form literally appears in a "
                 "collected source file are emitted. Each entity carries its "
                 "source file(s), outlet(s), and verbatim context sample(s). "
                 "Categories with 0 entities indicate the corpus did not "
                 "mention any matching surface form (data gap), not extraction "
                 "failure of the engine."),
    }
    with open(os.path.join(out_subdir, "sourced_entities_consolidated.json"), "w", encoding="utf-8") as fh:
        json.dump(consolidated, fh, indent=2, ensure_ascii=False)

    print()
    print("=== Source-Attributed Extraction Summary ===")
    print("Date            :", date_stamp)
    print("Sources         :", len(md_files))
    for cat in CATEGORY_GAZETTEERS:
        print("  %-16s : %d" % (cat, summary[cat]))
    print("Total entities  :", sum(summary.values()))
    print("Output dir      :", out_subdir)
    print("Done.")


if __name__ == "__main__":
    main()
