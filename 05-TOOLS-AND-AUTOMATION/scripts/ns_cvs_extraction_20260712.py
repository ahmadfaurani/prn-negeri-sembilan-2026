#!/usr/bin/env python3
# Negeri Sembilan PRN 2026 - CVS-Compliant Source-Attributed Entity Extraction
# Date: 20260712
# Classification: TLP:AMBER
# CVS Standard: All entities source-attributed. No pattern-inferred entities.
import json, os
from datetime import datetime, timezone

WORKSPACE = "/home/p62operator/.openclaw/workspace-ns"
OUTDIR = f"{WORKSPACE}/04-DATA-AND-SOURCES/processed-entities/20260712"
DATE = "20260712"
TS = datetime.now(timezone.utc).isoformat()
os.makedirs(OUTDIR, exist_ok=True)

# ---------------------------------------------------------------------------
# Source-attributed verified entities (manual review of raw/20260712/*.md)
# Every entity below is backed by an exact string in the cited source file.
# ---------------------------------------------------------------------------
verified = {
    "politicians": [
        {"name": "Baharudin", "role": "Johor PRN candidate (won highest majority)", "source": "astroawanicom_20260712_053155.md", "context": "PRN Johor: Baharudin raih majoriti tertinggi, Simpang Renggam majoriti rendah", "ns_relevant": False},
        {"name": "Syed Saddiq", "role": "MUDA president (Kes Dana Armada defendant)", "source": "astroawanicom_20260712_053155.md", "context": "Kes Dana Armada: Nasib Syed Saddiq diketahui esok", "ns_relevant": False},
        {"name": "President Tharman", "role": "President of Singapore (foreign head of state)", "source": "thestarcommy_20260712_053155.md", "context": "Singapore, Malaysia partnership driven by mutual respect ... President Tharman", "ns_relevant": False, "note": "Foreign head of state"},
    ],
    "parties": [],  # No Malaysian party is referenced in article prose. See compliance_audit + borderline_references.
    "constituencies": [
        {"name": "Simpang Renggam", "state": "Johor", "source": "astroawanicom_20260712_053155.md", "context": "PRN Johor: ... Simpang Renggam majoriti rendah", "ns_relevant": False, "note": "Johor DUN, NOT one of NS 36 DUN"},
    ],
    "issues": [
        {"name": "PRN Johor results (majoriti tertinggi/rendah, 55 calon hilang deposit)", "source": "astroawanicom_20260712_053155.md", "context": "PRN Johor: Baharudin raih majoriti tertinggi / PRN Johor: 55 calon hilang deposit", "ns_relevant": False},
        {"name": "Kes Dana Armada (Syed Saddiq court verdict pending)", "source": "astroawanicom_20260712_053155.md", "context": "Kes Dana Armada: Nasib Syed Saddiq diketahui esok", "ns_relevant": False},
        {"name": "Kontroversi logo Visit Truly Terengganu 2027", "source": "astroawanicom_20260712_053155.md", "context": "Kontroversi logo 'Visit Truly Terengganu 2027', ini penjelasan Exco", "ns_relevant": False, "note": "Terengganu, not NS"},
        {"name": "Iran closure of Strait of Hormuz", "source": "astroawanicom_20260712_053155.md", "context": "Iran umum tutup Selat Hormuz", "ns_relevant": False, "note": "Foreign/geopolitical"},
        {"name": "CIMB debit card service disruption (18 Julai)", "source": "astroawanicom_20260712_053155.md", "context": "Perkhidmatan kad debit CIMB tergendala sementara 18 Julai ini", "ns_relevant": False, "note": "National banking, not NS-specific"},
        {"name": "AI-generated ad labelling (Google)", "source": "astroawanicom_20260712_053155.md", "context": "Google mula label iklan dijana AI", "ns_relevant": False},
        {"name": "Toronto festival shooting (2 dead, 6 injured)", "source": "astroawanicom_20260712_053155.md", "context": "Dua maut, enam cedera dalam insiden tembakan di festival tarian di Toronto", "ns_relevant": False, "note": "Foreign crime"},
        {"name": "Singapore-Malaysia bilateral partnership", "source": "thestarcommy_20260712_053155.md", "context": "Singapore, Malaysia partnership driven by mutual respect ... President Tharman", "ns_relevant": False, "note": "Bilateral, not NS-specific"},
    ],
    "events": [
        {"name": "PRN Johor 2026 (results day)", "date": "2026-07-12", "source": "astroawanicom_20260712_053155.md", "context": "PRN Johor: Baharudin raih majoriti tertinggi ... / PRN Johor: 55 calon hilang deposit", "ns_relevant": False, "note": "Johor state election results, not NS"},
        {"name": "Piala Dunia FIFA 2026 (Argentina v Switzerland, quarter-final)", "source": "astroawanicom_20260712_053155.md", "context": "Piala Dunia 2026: Argentina perlukan 120 minit tewaskan Switzerland", "ns_relevant": False},
        {"name": "UFC 329 (McGregor v Holloway)", "source": "astroawanicom_20260712_053155.md; thestarcommy_20260712_053155.md", "context": "UFC 329: Lutut terpelecok, McGregor tewas di pusingan pertama dengan Holloway / McGregor's UFC return halted by knee injury", "ns_relevant": False},
        {"name": "Kes Dana Armada verdict (upcoming/esok)", "date": "pending", "source": "astroawanicom_20260712_053155.md", "context": "Kes Dana Armada: Nasib Syed Saddiq diketahui esok", "ns_relevant": False},
        {"name": "Hari Keputeraan Ke-77 Yang di-Pertuan Besar Negeri Sembilan", "date": "2025-01 (past)", "source": "ohbulancom_20260712_053155.md", "context": "Suki, Waris Dikurniakan Anugerah Sempena Hari Keputeraan Ke-77 Yang Dipertuan Besar Negeri Sembilan", "ns_relevant": True, "note": "NS royalty event; past (Jan 2025); NOT election-related"},
    ],
    "organizations": [
        {"name": "CIMB", "source": "astroawanicom_20260712_053155.md", "context": "Perkhidmatan kad debit CIMB tergendala sementara", "ns_relevant": False, "note": "Banking"},
        {"name": "Google", "source": "astroawanicom_20260712_053155.md", "context": "Google mula label iklan dijana AI", "ns_relevant": False},
        {"name": "FIFA", "source": "astroawanicom_20260712_053155.md", "context": "Piala Dunia 2026: Argentina ...", "ns_relevant": False},
        {"name": "UFC", "source": "astroawanicom_20260712_053155.md; thestarcommy_20260712_053155.md", "context": "UFC 329 ...", "ns_relevant": False},
        {"name": "Star Media Group Berhad", "source": "thestarcommy_20260712_053155.md", "context": "Copyright (c) 1995- Star Media Group Berhad", "ns_relevant": False, "note": "Publisher"},
        {"name": "Media Mulia Sdn Bhd", "source": "kosmocommy_20260712_053155.md; utusancommy_20260712_053155.md", "context": "Hak cipta terpelihara (c) 2026 Media Mulia Sdn Bhd", "ns_relevant": False, "note": "Publisher"},
        {"name": "McDonald's Malaysia (Tampin branch)", "source": "ohbulancom_20260712_053155.md", "context": "McDonald's Malaysia Rasmi Cawangan Baru Di Tampin, Negeri Sembilan", "ns_relevant": True, "note": "NS location (Tampin); commercial, not political"},
        {"name": "Persatuan Kebajikan Ronald McDonald (RHMC)", "source": "ohbulancom_20260712_053155.md", "context": "Persatuan Kebajikan Ronald McDonald (RHMC) Malaysia", "ns_relevant": False},
        {"name": "KFC", "source": "ohbulancom_20260712_053155.md", "context": "Kita semua bersatu untuk menikmati hidangan KFC", "ns_relevant": False},
        {"name": "Reuters", "source": "astroawanicom_20260712_053155.md", "context": "REUTERS/Cole Burston; REUTERS/Stringer (image credits)", "ns_relevant": False, "note": "News agency (image attribution)"},
    ],
    "locations": [
        {"name": "Johor", "source": "astroawanicom_20260712_053155.md", "context": "PRN Johor", "ns_relevant": False},
        {"name": "Simpang Renggam", "source": "astroawanicom_20260712_053155.md", "context": "Simpang Renggam majoriti rendah", "ns_relevant": False, "note": "Johor"},
        {"name": "Toronto", "source": "astroawanicom_20260712_053155.md", "context": "tembakan di festival tarian di Toronto", "ns_relevant": False},
        {"name": "Terengganu", "source": "astroawanicom_20260712_053155.md", "context": "Kontroversi logo Visit Truly Terengganu 2027", "ns_relevant": False},
        {"name": "Kansas City", "source": "astroawanicom_20260712_053155.md", "context": "Kansas City Stadium, Kansas City, Missouri (FIFA QF)", "ns_relevant": False},
        {"name": "Argentina", "source": "astroawanicom_20260712_053155.md", "context": "Argentina perlukan 120 minit tewaskan Switzerland", "ns_relevant": False},
        {"name": "Switzerland", "source": "astroawanicom_20260712_053155.md", "context": "tewaskan Switzerland", "ns_relevant": False},
        {"name": "Las Vegas", "source": "astroawanicom_20260712_053155.md", "context": "Las Vegas, Nevada, USA (UFC 329)", "ns_relevant": False},
        {"name": "Nevada", "source": "astroawanicom_20260712_053155.md", "context": "Las Vegas, Nevada, USA (UFC 329)", "ns_relevant": False},
        {"name": "Selat Hormuz", "source": "astroawanicom_20260712_053155.md", "context": "Iran umum tutup Selat Hormuz", "ns_relevant": False},
        {"name": "Iran", "source": "astroawanicom_20260712_053155.md", "context": "Iran umum tutup Selat Hormuz", "ns_relevant": False},
        {"name": "Oman", "source": "astroawanicom_20260712_053155.md", "context": "Strait of Hormuz as seen from Musandam, Oman (image caption)", "ns_relevant": False},
        {"name": "Negeri Sembilan", "source": "ohbulancom_20260712_053155.md", "context": "negeri sembilan (tag page); ... Negeri Sembilan", "ns_relevant": True, "note": "NS state mentioned; entertainment tag page, not election"},
        {"name": "Tampin", "source": "ohbulancom_20260712_053155.md", "context": "Cawangan Baru Di Tampin, Negeri Sembilan", "ns_relevant": True, "note": "NS location/town; also parliamentary constituency P132 (not one of 36 DUN)"},
        {"name": "Port Dickson (PD)", "source": "ohbulancom_20260712_053155.md", "context": "Didakwa Bercuti Di PD, Aeril Jelaskan Pergi Negeri Sembilan", "ns_relevant": True, "note": "NS location; celebrity gossip context"},
        {"name": "Singapore", "source": "thestarcommy_20260712_053155.md", "context": "Singapore, Malaysia partnership ... President Tharman", "ns_relevant": False},
        {"name": "Malaysia", "source": "thestarcommy_20260712_053155.md", "context": "Singapore, Malaysia partnership", "ns_relevant": False},
        {"name": "Bhutan", "source": "thestarcommy_20260712_053155.md", "context": "Bhutan battles 'existential' population crisis", "ns_relevant": False},
        {"name": "London", "source": "kosmocommy_20260712_053155.md", "context": "Polis London kagum tengok pasport baharu Malaysia", "ns_relevant": False},
    ],
}

# Non-political named persons found in sources (excluded from politicians count for CVS accuracy)
non_political_persons = [
    {"name": "Conor McGregor", "role": "UFC fighter", "source": "astroawanicom_20260712_053155.md; thestarcommy_20260712_053155.md", "context": "McGregor tewas / McGregor's UFC return halted", "note": "Sports, not politician"},
    {"name": "Max Holloway", "role": "UFC fighter", "source": "astroawanicom_20260712_053155.md", "context": "fights Max Holloway ... dengan Holloway", "note": "Sports, not politician"},
    {"name": "Nabil Ahmad", "role": "pengacara/penyampai radio", "source": "ohbulancom_20260712_053155.md", "context": "Ceroboh Rumah Nabil Ahmad", "note": "Entertainer, not politician"},
    {"name": "Waris", "role": "penyanyi", "source": "ohbulancom_20260712_053155.md", "context": "Penyanyi Waris dan Suki Low dikurniakan anugerah", "note": "Singer, not politician"},
    {"name": "Suki Low", "role": "penyanyi", "source": "ohbulancom_20260712_053155.md", "context": "Penyanyi Waris dan Suki Low dikurniakan anugerah", "note": "Singer, not politician"},
    {"name": "Aeril Zafrel", "role": "selebriti", "source": "ohbulancom_20260712_053155.md", "context": "pasangan selebriti Aeril Zafrel dan Wawa Zainal", "note": "Celebrity, not politician"},
    {"name": "Wawa Zainal", "role": "selebriti", "source": "ohbulancom_20260712_053155.md", "context": "pasangan selebriti Aeril Zafrel dan Wawa Zainal", "note": "Celebrity, not politician"},
]

# Borderline / weak references excluded from verified parties to match prior CVS standard (prose-only)
borderline_references = [
    {"name": "Perikatan Nasional (PN)", "source": "astroawanicom_20260712_053155.md", "reason": "Appears ONLY as image asset filename '41767104723_PerikatanNasional.jpg' accompanying 'PRN Johor: 55 calon hilang deposit', not in article prose; Johor PRN context, not NS. Excluded from verified parties (image-filename-only attribution, consistent with 20260711 standard)."},
]

# Source quality
source_quality = {
    "total_files": 9,
    "substantive_content_files": 3,
    "404_or_minimal_pages": 6,
    "files_with_404_or_minimal_content": [
        "malaysiakinicom_20260712_053155.md",
        "mstarcommy_20260712_053155.md",
        "utusancommy_20260712_053155.md",
        "kosmocommy_20260712_053155.md",
        "sinarhariancommy_20260712_053155.md",
        "sinarhariancommy_20260712_052935.md",
    ],
    "files_with_substantive_content": [
        "astroawanicom_20260712_053155.md",
        "ohbulancom_20260712_053155.md",
        "thestarcommy_20260712_053155.md",
    ],
    "ns_specific_files": 1,
    "ns_specific_file": "ohbulancom_20260712_053155.md (Negeri Sembilan tag page; old 2019-2025 entertainment/lifestyle/royalty content)",
    "dominant_topic": "PRN Johor 2026 results day (12 Julai 2026)",
}

# Script raw output (from ns-entity-extraction.sh run)
script_raw_counts = {
    "politicians": 0, "parties": 1, "constituencies": 0, "issues": 0,
    "events": 0, "organizations": 0, "locations": 0,
}

# Verified counts
verified_counts = {k: len(v) for k, v in verified.items()}
verified_counts["total_verified"] = sum(len(v) for v in verified.values())

ns_relevant = []
for k, v in verified.items():
    for e in v:
        if e.get("ns_relevant"):
            ns_relevant.append(f"{e['name']} ({k})")

# ---------------------------------------------------------------------------
# Write per-category source-attributed entity files (replace non-compliant script output)
# ---------------------------------------------------------------------------
cat_map = {
    "politicians": "entities_politicians.json",
    "parties": "entities_parties.json",
    "constituencies": "entities_constituencies.json",
    "issues": "entities_issues.json",
    "events": "entities_events.json",
    "organizations": "entities_organizations.json",
    "locations": "entities_locations.json",
}
for cat, fname in cat_map.items():
    ents = verified[cat]
    doc = {
        "date": TS,
        "source_count": source_quality["total_files"],
        "entity_type": cat,
        "method": "manual_source_attributed_review",
        "cvs_standard": "All entities source-attributed. No pattern-inferred entities.",
        "entities": [e["name"] for e in ents],
        "entities_detailed": ents,
    }
    with open(os.path.join(OUTDIR, fname), "w") as f:
        json.dump(doc, f, indent=2, ensure_ascii=False)

# ---------------------------------------------------------------------------
# Write consolidated file
# ---------------------------------------------------------------------------
consolidated = {
    "date": DATE,
    "timestamp": TS,
    "source_count": source_quality["total_files"],
    "extraction_completed": True,
    "method": "manual_source_attributed_review (CVS-compliant)",
    "cvs_standard": "All entities source-attributed. No pattern-inferred entities.",
    "entity_categories": list(cat_map.keys()),
    "verified_counts": verified_counts,
    "ns_relevant_entities_count": len(ns_relevant),
}
with open(os.path.join(OUTDIR, "entities_consolidated.json"), "w") as f:
    json.dump(consolidated, f, indent=2, ensure_ascii=False)

# ---------------------------------------------------------------------------
# Write the verified CVS-compliant master file
# ---------------------------------------------------------------------------
master = {
    "extraction_id": "ns-prn-2026-entity-extraction-20260712",
    "date": DATE,
    "timestamp": TS,
    "collection": "04-DATA-AND-SOURCES/raw-scrapes/20260712",
    "source_count": source_quality["total_files"],
    "method": "manual_source_attributed_review",
    "cvs_standard": "All entities source-attributed. No pattern-inferred entities.",
    "classification": "TLP:AMBER",
    "script_run": {
        "script": "05-TOOLS-AND-AUTOMATION/scripts/ns-entity-extraction.sh",
        "exit_code": 0,
        "raw_output_counts": script_raw_counts,
        "script_compliance_audit": {
            "pattern_inferred_false_positives": [
                {"entity": "bersatu", "reason": "Matched Malay verb 'to unite' in KFC article (ohbulan line 93: 'kita semua bersatu untuk menikmati hidangan KFC'), NOT the Bersatu party. This is the script's sole '1 parties' output."},
            ],
            "categories_with_no_extraction_logic": ["politicians", "issues", "events", "organizations", "locations"],
            "constituency_regex_zero_hits": "No NS DUN names matched; script produced 0 constituencies.",
            "verdict": "Script output is NON-COMPLIANT with CVS standard (pattern-inferred false positive, no source attribution, 5/7 categories empty by design). The single extracted entity ('bersatu') is a false positive."
        },
    },
    "verified_entities": verified,
    "non_political_persons_found": non_political_persons,
    "borderline_references_excluded": borderline_references,
    "verified_counts": verified_counts,
    "ns_relevant_entities_count": len(ns_relevant),
    "ns_relevant_entities": ns_relevant,
    "key_finding": (
        "ZERO entities related to Negeri Sembilan PRN 2026 (state election) were found in the 20260712 collection. "
        "The collection is dominated by PRN JOHOR results day (12 Julai 2026: Baharudin majoriti tertinggi, 55 calon hilang deposit), "
        "Piala Dunia FIFA 2026 (Argentina v Switzerland quarter-final), UFC 329 (McGregor knee injury), Kes Dana Armada (Syed Saddiq), "
        "and 404/paywall error pages. The only Negeri Sembilan-tagged source (ohbulan) contains old (2019-2025) "
        "entertainment/lifestyle/royalty articles with no election content. None of NS's 36 DUN constituencies, "
        "no NS state politicians, and no NS election issues appear in any source. "
        "This is the SECOND consecutive day (20260711 and 20260712) with zero NS election content - a systemic collection targeting failure. "
        "NS PRN 2026 is scheduled for 1 August 2026 (per DUN_MASTER_LIST.md) - approximately 20 days away - yet collection is capturing "
        "zero NS election intelligence, representing a CRITICAL intelligence gap."
    ),
    "source_quality": source_quality,
    "sentiment_analysis_readiness": {
        "ready": False,
        "reason": "No Negeri Sembilan election-relevant entities found to analyze. Sentiment analysis on the current collection would measure Johor election results sentiment, World Cup/UFC sports coverage, and Kes Dana Armada sentiment - not NS PRN 2026.",
        "recommendation": "Collection script (ns-daily-collection.sh) is querying source URLs that return 404/paywall pages and/or Johor-focused landing pages rather than Negeri Sembilan-specific election content. This is the 2nd consecutive day of failure. Collection targeting must be fixed (point at NS-specific sections/tags, PRN NS candidate pages, local NS political reporting) before useful NS entity extraction or sentiment analysis is possible."
    },
}
with open(os.path.join(OUTDIR, "entities_verified_cvs_compliant.json"), "w") as f:
    json.dump(master, f, indent=2, ensure_ascii=False)

# ---------------------------------------------------------------------------
# Print summary
# ---------------------------------------------------------------------------
print("=== CVS-Compliant Source-Attributed Extraction Complete ===")
print(f"Output dir: {OUTDIR}")
print(f"Timestamp: {TS}")
print()
print("Verified counts per category:")
for k, v in verified_counts.items():
    print(f"  {k}: {v}")
print()
print(f"NS-relevant entities: {len(ns_relevant)}")
for e in ns_relevant:
    print(f"  - {e}")
print()
print("Non-compliant script false positive: ['bersatu'] (Malay verb in KFC article)")
print("Sentiment analysis ready: FALSE (no NS election entities)")
print("Files written:")
for fname in list(cat_map.values()) + ["entities_consolidated.json", "entities_verified_cvs_compliant.json"]:
    p = os.path.join(OUTDIR, fname)
    print(f"  {fname} ({os.path.getsize(p)} bytes)")
