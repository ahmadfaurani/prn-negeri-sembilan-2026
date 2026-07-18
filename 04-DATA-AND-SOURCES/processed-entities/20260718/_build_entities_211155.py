#!/usr/bin/env python3
"""
PRN Negeri Sembilan 2026 — Entity Extraction Agent (cron build script, run 211155 UTC).
CONFIRMATION / STABILITY BUILD — carries forward entities_190215.json.

Cycle window ingested: 194028 (19:40 UTC / 03:40 MYT 19 Jul) + 205755 (20:57 UTC / 04:57 MYT 19 Jul).
These are the 3rd and (counting 182751) 4th consecutive ZERO-DELTA overnight confirmation passes
following the 170837 PIR-06 escalation ingested by entities_190215.json.

RIGOROUS DELTA VERIFICATION (this agent, not just carried over from collector):
  - Programmatic normalized title set-difference of _scrape_results priority_titles:
      * 182751 -> 194028: +1 title ("103 candidates confirmed for 36-seat Negri Sembilan election",
        NST English) / -1 title ("PN may continue BN cooperation ... says Samsuri", rotated off
        NST gnews top-60 but already captured at 170837 and present in entities_190215).
      * 194028 -> 205755: 0 new / 0 dropped (exactly matches collector's automated delta claim).
      * 182751 -> 205755: +1 / -1 (same as above; the two passes are content-identical).
  - The +1 "new" NST English title is NOT a new fact: "103 calon sah bertanding rebut 36 kerusi DUN – SPR"
    (Kosmo Malay) was already captured earlier, and the 103-candidate / 36-seat figures are already
    in entities_190215 counts (candidate_persons_unique=103, seats_parsed=36). It is logged here as
    an English-language CORROBORATING SOURCE for an already-counted fact.
  - The -1 "dropped" Samsuri title is already-captured PIR-06/PIR-07 content (Samsuri's post-election
    BN-cooperation signal, first captured 170837); it merely rotated off a gnews top-60 set. No loss.
  - priority_files_written_this_cycle = 0 in both 194028 and 205755 (all priority_* files are from the
    153142 and 170837 cycles, already ingested by entities_190215).
  - Raw MD5 checksums of the *_194028.md / *_205755.md files differ from *_182751.md, but this is
    feed-rotation noise (gnews reordering / embedded timestamps), NOT new article content. The
    normalized title set-difference above is the authoritative delta measure and is ~0.

CONCLUSION: ZERO genuinely new entities in the 194028 + 205755 cycles. All entity data is carried
forward unchanged from entities_190215.json. This build's value = audit trail + overnight-stability
confirmation (PIR-06 escalated-watch unchanged; no CRITICAL threshold crossing; no Tier-4 candidate
withdrawals; candidate list (103) unchanged) + one new corroborating source note.

Classification: TLP:AMBER
"""
import json, os, copy, datetime

BASE = "/home/p62operator/.openclaw/workspace-ns/04-DATA-AND-SOURCES/processed-entities/20260718"
PREV = os.path.join(BASE, "entities_190215.json")

with open(PREV, "r", encoding="utf-8") as f:
    prev = json.load(f)

# ---- Carry ALL entity data forward unchanged (zero-delta confirmation cycle) ----
out = copy.deepcopy(prev)

# ---- PIR seat sets (unchanged) ----
PIR06_TIER4 = ["N04","N05","N13","N14","N23","N25","N31","N34"]
PIR07_WATCH = ["N04","N05","N10","N13","N14","N15","N28","N32","N33"]
BERSATU_CAND_SEATS = ["N02","N03","N04","N05","N06","N07","N09","N10","N12","N13","N14",
                      "N15","N16","N17","N20","N22","N23","N24","N25","N28","N31","N32","N33","N34"]
INDEPENDENTS = {
    "Omar Mohd Isa":"N10 Nilai",
    "Teo Seng Lee":"N30 Lukut",
    "Datuk A Saravanan":"N33 Sri Tanjung",
    "Islah Wahyudi Zainudin":"N33 Sri Tanjung",
}

# ---- Timestamps (this run) ----
now_utc = datetime.datetime(2026,7,18,21,11,55)
file_id = "entities_211155"

out["processing_timestamp_utc"] = now_utc.isoformat()+"+00:00"
out["processing_timestamp_myt"] = (now_utc+datetime.timedelta(hours=8)).isoformat()+"+08:00"
out["file_id"] = file_id
out["cycle"] = ("nomination-day-surge + overnight confirmation (170837 escalation + 182751/194028/"
               "205755 three consecutive zero-delta confirmation passes; entities_190215 baseline carried)")
out["source_count_total"] = prev["source_count_total"]

# ---- Append the two new confirmation-cycle files to the PIR-relevant source list ----
sfiles = list(prev.get("source_files_pir_relevant", []))
for fn in [
    "_scrape_results_194028.json (194028 cycle — 2nd zero-delta overnight confirmation pass, 0 new titles)",
    "_scrape_results_205755.json (205755 cycle — 3rd zero-delta overnight confirmation pass, 0 new titles)",
    "nstcommy_20260718_194028.md (NST gnews — surfaced English '103 candidates confirmed for 36-seat NS election', corroborating the already-counted 103/36 figure)",
    "collection_metadata.json (205755 cycle — 3rd-pass stability + PIR-06 escalated-watch unchanged audit)",
]:
    if fn not in sfiles:
        sfiles.append(fn)
out["source_files_pir_relevant"] = sfiles

# ---- Document the delta vs the prior build (entities_190215) ----
out["delta_vs_prior_build_190215"] = {
    "prior_build": "entities_190215.json (19:02 UTC / 03:02 MYT 19 Jul)",
    "this_build": f"{file_id}.json (21:11 UTC / 05:11 MYT 19 Jul)",
    "cycle_window_ingested": [
        "194028 (19:40 UTC / 03:40 MYT 19 Jul — 2nd zero-delta overnight confirmation pass)",
        "205755 (20:57 UTC / 04:57 MYT 19 Jul — 3rd zero-delta overnight confirmation pass)",
    ],
    "delta_verification_method": ("Programmatic normalized title set-difference on _scrape_results "
        "priority_titles across 182751 / 194028 / 205755 (this agent). 194028->205755 delta = 0 titles. "
        "182751->194028/205755 delta = +1 / -1 (NST English '103 candidates confirmed' corroborating "
        "an already-counted fact; Samsuri title rotated off gnews top-60 but already captured at 170837)."),
    "genuinely_new_findings": [],
    "corroborating_reconfirmations": [
        "NST (English): '103 candidates confirmed for 36-seat Negri Sembilan election' — English-language "
        "confirmation of the already-captured Kosmo Malay '103 calon sah bertanding rebut 36 kerusi DUN – SPR'. "
        "The 103-candidate / 36-seat figures are already in entities_190215 counts (candidate_persons_unique=103, "
        "seats_parsed=36). No new entity; logged as a corroborating source.",
    ],
    "no_change": [
        "CRITICAL PIR-06 threshold (formal PN-MT removal notice) still NOT crossed — 3rd consecutive overnight pass.",
        "PIR-06 escalated-watch assessment (two-sided: PN-MT-may-remove-Bersatu via Kiandee AND Bersatu-may-exit-PN "
        "via Muhyiddin) UNCHANGED. No new Muhyiddin/Kiandee/Hadi/Annuar Musa/Samsuri/Hamzah statements this window.",
        "No Bersatu candidate withdrawals in the 8 Tier-4 seats (N04,N05,N13,N14,N23,N25,N31,N34).",
        "Candidate list unchanged: 103 candidates, 36 seats, breakdown {PH:36, BN:25, Bersatu:24, PN:11, "
        "independents:4, Berjasa:1, Asli:1, PSM:1}.",
        "PIR-09 N.14 Ampangan Day-1 messaging war unchanged (no Day-2 campaign content — overnight window).",
        "Gerakan pecat of Tang Jay Son reconfirmed (no new PN-component candidate expulsion).",
        "PIR-07 BN manifesto launch date (24 Jul) and candidate breakdown unchanged.",
        "All monitor channels quiet (deep-overnight MYT ~03:40–04:57; Day-2 campaign events begin daytime MYT 19 Jul).",
    ],
    "entity_set_delta": {"added": 0, "removed": 0, "modified": 0, "net": 0},
}

# ---- counts unchanged (zero-delta) ----
counts = prev["counts"]
out["counts"] = counts
out["counts"]["confirmation_passes_since_170837"] = 3   # 182751, 194028, 205755

# Add a corroborating-source note into the PIR-07 index (103/36 already counted; NST English corroboration)
pir_index = out["pir_priority_index"]
pir_index["PIR-07"]["candidate_count_corroboration"] = {
    "fact": "103 candidates confirmed for 36-seat Negri Sembilan election",
    "english_source": "New Straits Times (nstcommy gnews, 194028/205755 cycles)",
    "malay_source_already_counted": "Kosmo '103 calon sah bertanding rebut 36 kerusi DUN – SPR'",
    "status": "Reconfirmation of an already-counted figure (entities_190215 counts); not a new entity.",
}

# ---- Write the entities file ----
with open(os.path.join(BASE, f"{file_id}.json"), "w", encoding="utf-8") as f:
    json.dump(out, f, ensure_ascii=False, indent=2)

# ---- entity_metadata.json (update) ----
meta = {
    "date": "20260718",
    "last_updated_utc": out["processing_timestamp_utc"],
    "last_updated_myt": out["processing_timestamp_myt"],
    "classification": "TLP:AMBER",
    "extractor": "prn_ns_entity_extraction_agent (scheduled cron)",
    "latest_entities_file": f"{file_id}.json",
    "prior_entities_file": "entities_190215.json",
    "director_priority_approved": "2026-07-18 15:00 MYT",
    "cycle": ("nomination-day-surge + overnight confirmation (170837 escalation + 182751/194028/205755 "
              "three consecutive zero-delta confirmation passes; no new entities)"),
    "source_count_total": out["source_count_total"],
    "build_character": "CONFIRMATION / STABILITY BUILD — zero new entities; entities_190215 baseline carried forward unchanged.",
    "delta_vs_prior_build": {
        "prior_build": "entities_190215.json",
        "this_build": f"{file_id}.json",
        "cycles_ingested": ["194028", "205755"],
        "genuinely_new_entities": 0,
        "corroborating_reconfirmations": 1,
        "verification": "Programmatic normalized title set-difference: 194028->205755 = 0 new titles.",
    },
    "counts": counts,
    "pir_priority_tags": {
        "PIR-06": {
            "title": "PN-Removal-of-Bersatu Watch (HIGHEST)",
            "status": ("ESCALATED WATCH — UNCHANGED across 3 overnight passes. NO formal PN-MT removal notice; "
                "TWO-SIDED trajectory ACTIVE (PN-MT-may-remove-Bersatu via Kiandee AND Bersatu-may-exit-PN via "
                "Muhyiddin). Bersatu PRESIDENT publicly hinting at exit; mainstream framing 'imminent?'. "
                "No new PIR-06 statements in the 194028/205755 overnight window."),
            "formal_removal_notice_detected": False,
            "escalation_detected": True,
            "tier4_seats": PIR06_TIER4,
            "entity_count": len(pir_index["PIR-06"]["entities"]),
            "key_entities": pir_index["PIR-06"]["entities"],
        },
        "PIR-09": {
            "title": "Candidate Credibility (SECOND)",
            "bersatu_candidate_seats": BERSATU_CAND_SEATS,
            "independents": list(INDEPENDENTS.keys()),
            "entity_count": len(pir_index["PIR-09"]["entities"]),
            "key_entities": pir_index["PIR-09"]["entities"],
        },
        "PIR-07": {
            "title": "Battleground Assessment (THIRD)",
            "watch_seats": PIR07_WATCH,
            "entity_count": len(pir_index["PIR-07"]["entities"]),
            "key_entities": pir_index["PIR-07"]["entities"],
        },
    },
    "seat_pir_tag_map": prev["constituencies"],
    "files_in_folder": [
        f"{file_id}.json (THIS run — confirmation/stability build; 194028+205755 zero-delta passes; no new entities; NST English 103/36 corroboration logged)",
        "entities_190215.json (prior run 19:02 UTC — 170837 PIR-06 escalation ingested, Samsuri corrected, new PIR-09 entities)",
        "entities_165723.json (prior run 16:57 UTC — nomination-day-surge baseline w/ PIR tags)",
        "entities_consolidated.json (prior 14:00 UTC run — candidate-list baseline)",
        "entities_politicians.json / entities_parties.json / entities_constituencies.json / entities_events.json / entities_issues.json / entities_organizations.json / entities_locations.json (prior 14:00 UTC sub-sets)",
        "entity_metadata.json (this file)",
        "_build_entities.py / _build_entities_190215.py (prior build scripts)",
        f"_build_entities_{file_id.split('_')[1]}.py (this run's build script)",
    ],
    "total_entities": (counts["candidate_persons_unique"] + counts["national_figures_and_pir_actors"] +
        counts["pir06_watch_figures"] + counts["parties"] + counts["coalitions"] + counts["organizations"] +
        counts["constituencies"] + counts["events"] + counts["issues_and_signals"] + counts["locations"]),
}
with open(os.path.join(BASE, "entity_metadata.json"), "w", encoding="utf-8") as f:
    json.dump(meta, f, ensure_ascii=False, indent=2)

print("OK", file_id + ".json + entity_metadata.json written")
print("counts:", json.dumps(counts, ensure_ascii=False))
print("total_entities:", meta["total_entities"])
print("build_character:", meta["build_character"])
print("delta_vs_prior:", json.dumps(meta["delta_vs_prior_build"], ensure_ascii=False))
print("PIR-06 entity_count:", len(pir_index["PIR-06"]["entities"]))
print("PIR-09 entity_count:", len(pir_index["PIR-09"]["entities"]))
print("PIR-07 entity_count:", len(pir_index["PIR-07"]["entities"]))
