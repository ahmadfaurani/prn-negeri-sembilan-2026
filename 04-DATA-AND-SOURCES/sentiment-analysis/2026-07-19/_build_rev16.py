#!/usr/bin/env python3
"""Build rev16 sentiment analysis from rev15 baseline + 2225 entity build.

rev16 (5th carry-forward, 212300 cycle) ingests the 230-entity 2225 build
(finalized ~22:25 UTC 19 Jul = 06:25 MYT 20 Jul, Day-2 dawn) which adds
+2 new PIR-06 [PRIORITY] cooperation-vector entities over the 228-entity
1954 build used by rev15:

  1. Zambry (Zambry Abd Kadir) — Umno Sec-Gen met Samsuri (PN chairman) in
     Port Dickson (N.05, Tier-4 seat). Leadership-level BN-PN pact
     confirmation on NS soil. Newswav gnews headline-intel (18 Jul 09:22 MYT).
  2. BN-PN pact Port Dickson meeting (Zambry-Samsuri) — narrative entity.
     Precursor to the 19 Jul 4-stage BN-PN formalization trajectory.

Both are COUNTER-vector (cooperation-hardening) signals, NOT fracture signals.
All 13 [CRITICAL] PIR-06 entities UNCHANGED (14th consecutive cycle, no
new threshold crossed). The Bersatu sharp-negative internal-fracture signal
remains CONFIRMED and STABLE (not escalating) this cycle.
"""
import json
import copy
import os
from datetime import datetime

BASE_DIR = "/home/p62operator/.openclaw/workspace-ns/04-DATA-AND-SOURCES/sentiment-analysis/2026-07-19"
REV15_FILE = os.path.join(BASE_DIR, "sentiment-20260720-0550.json")
REV16_FILE = os.path.join(BASE_DIR, "sentiment-20260720-0625.json")

with open(REV15_FILE, "r", encoding="utf-8") as f:
    rev15 = json.load(f)

rev16 = copy.deepcopy(rev15)

# --- Update metadata ---
gen_utc = "2026-07-19T22:25:00Z"
gen_myt = "2026-07-20T06:25:00+08:00"
rev16["metadata"]["version"] = "revision-16"
rev16["metadata"]["generated"] = gen_myt
rev16["metadata"]["generated_utc"] = gen_utc
rev16["metadata"]["prior_revision_file"] = "sentiment-analysis/2026-07-19/sentiment-20260720-0550.json"
rev16["metadata"]["prior_revision"] = "revision-15 (2026-07-20T05:50:00+08:00, 237 entities, 13 critical/51 priority/173 none), built on the 228-entity 1954 build"
rev16["metadata"]["entity_build"] = (
    "processed-entities/2026-07-19/entities-20260719-2225.json (230 entities, 15+ cycles, 14 critical/107 priority/109 normal). "
    "Finalized 22:25 UTC 19 Jul (06:25 MYT 20 Jul). 5th carry-forward, 212300 cycle. Supersedes the 228-entity 1954 build used by rev15 "
    "(finalized 01:54 MYT 20 Jul). +2 new entities (both PIR-06 [PRIORITY] cooperation-vector) from the 200000 + 212300 cycles (Day-2 dawn, post-midnight MYT). "
    "CYCLE CLASSIFICATION: QUIET / LOW-YIELD corroboration window. NEW ENTITIES: (1) 'Zambry (Zambry Abd Kadir)' PIR-06 [PRIORITY] — Umno Sec-Gen met "
    "Samsuri (PN chairman) in Port Dickson (N.05 Tier-4 seat); leadership-level BN-PN pact confirmation on NS soil (Newswav gnews headline-intel 18 Jul 09:22 MYT, "
    "full text not curl-recoverable); (2) 'BN-PN pact Port Dickson meeting (Zambry-Samsuri)' PIR-06 [PRIORITY] — narrative entity; precursor to the 19 Jul 4-stage "
    "BN-PN formalization trajectory (seat-swap -> gabung jentera -> manifesto bersepadu -> kongsi pentas). Both are COUNTER-vector (cooperation-hardening) signals, "
    "NOT fracture signals. No new [CRITICAL] threshold crossed (14th consecutive cycle). All 13 [CRITICAL] PIR-06 entities UNCHANGED."
)
rev16["metadata"]["director_cycle"] = "19 Jul 17:25 MYT (4th carry-forward) — 5th entity carry-forward (212300 cycle)"
rev16["metadata"]["entity_count"] = 239
rev16["metadata"]["critical_count"] = 13
rev16["metadata"]["priority_count"] = 53
rev16["metadata"]["none_count"] = 173

# --- Append 2 new entities (both PIR-06 PRIORITY cooperation-vector) ---
new_entities = [
    {
        "entity": "Zambry (Zambry Abd Kadir)",
        "pir_tag": "PIR-06",
        "sentiment": "positive",
        "score": 0.22,
        "trend": "stable",
        "alert": "priority",
        "source_count": 1,
        "rationale": (
            "NEW rev16 (5th carry-forward, 212300 cycle). Umno Secretary-General (Zambry Abd Kadir, former Perak MB). "
            "Newswav gnews headline-intel (18 Jul 09:22 MYT): 'BN-PN pact comes alive in Port Dickson as Zambry, Samsuri meet' "
            "(full text not curl-recoverable). Cross-surfaced via the mandatory 'Bersatu sole opposition Muhyiddin' gnews query. "
            "Zambry (BN/Umno Sec-Gen) met Samsuri (PN chairman / Terengganu MB) in PORT DICKSON — an NS constituency (N.05, "
            "Director PIR-06 Tier-4 seat). FIRST explicit Tier-4-seat (N.05) leadership-meeting intel: a PIR-06 cooperation "
            "signal on Tier-4 turf. Pre-dates the 19 Jul Hamzah 'gabung jentera' machinery merger (18:29 MYT) — this is the "
            "POLITICAL-LEADERSHIP-LEVEL BN-PN pact confirmation (Zambry=BN sec-gen <-> Samsuri=PN chairman), distinct from the "
            "operational/grassroots machinery merger. Score +0.22 (marginal positive; single-source headline-intel, "
            "cooperation-vector). [PRIORITY] (not [CRITICAL]) — cooperation-hardening signal, NOT a fracture signal. "
            "Reinforces BN-PN pact; does NOT cross the [CRITICAL] threshold (which requires 'pecat/keluar/tarik diri/toxic PN/"
            "kuorum/lebih hebat' entity). Adds N.05 to the active Tier-4 watch set."
        )
    },
    {
        "entity": "BN-PN pact Port Dickson meeting (Zambry-Samsuri)",
        "pir_tag": "PIR-06",
        "sentiment": "positive",
        "score": 0.30,
        "trend": "improving",
        "alert": "priority",
        "source_count": 1,
        "rationale": (
            "NEW rev16 (5th carry-forward, 212300 cycle). Newswav gnews headline-intel (18 Jul 09:22 MYT): 'BN-PN pact comes "
            "alive in Port Dickson as Zambry, Samsuri meet.' Leadership-level BN-PN pact confirmation on NS soil — Zambry "
            "(Umno Sec-Gen / BN) <-> Samsuri (PN chairman / Terengganu MB) meeting in PORT DICKSON (N.05, Director PIR-06 "
            "Tier-4 seat). First explicit Tier-4-seat (N.05) leadership-meeting intel: a PIR-06 cooperation signal on Tier-4 "
            "turf. Pre-dates and pre-figures the 19 Jul 4-stage BN-PN formalization trajectory (seat-swap -> gabung jentera "
            "machinery merger -> manifesto bersepadu -> kongsi pentas joint ceramah). The Zambry-Samsuri PD meeting is the "
            "POLITICAL-LEADERSHIP tier of that trajectory — the precursor that enabled the operational tiers that followed. "
            "Adds a 5th Tier-4 seat (N.05) to the active-watch set (N.04/05/13/14/23/25/31/34). Score +0.30 (positive, "
            "cooperation-hardening narrative, single-source headline-intel; improving trend as it pre-figures the "
            "formalization trajectory). [PRIORITY] (not [CRITICAL]) — cooperation-hardening, NOT a coalition-fracture "
            "signal. The [CRITICAL] flag (Kiandee quorum escalation) remains MAINTAINED on the FRACTURE vector; this is "
            "the COUNTER-vector (BN-PN pact strengthening)."
        )
    }
]
rev16["entities"].extend(new_entities)

# --- Update "sole opposition" entity: gnews cross-surfacing corroborated to 5-outlet ---
for e in rev16["entities"]:
    if e["entity"] == "sole opposition (Muhyiddin lone credible opposition)":
        e["source_count"] = 5
        e["rationale"] = (
            "rev13 -0.50 stable. 153300 corroborated (The Vibes 18 Jul 'Bersatu now sole opposition party'). "
            "rev16 (212300 cycle): gnews 'Bersatu sole opposition Muhyiddin' query cross-surfaced the Zambry-Samsuri "
            "Port Dickson meeting (Newswav 18 Jul 09:22) and corroborating outlets (NST, The Star, Malay Mail) — "
            "5-outlet corroboration. Muhyiddin self-positioning as sole credible opposition persists; "
            "source_count 4->5; score -0.50 STABLE (corroboration, not escalation)."
        )
        # score stays -0.50, trend stays declining, alert stays none
        break

# --- Update trend_summary ---
ts = rev16["trend_summary"]
ts["revision"] = "revision-16 (built on entities-20260719-2225.json, 230 entities, 15+ cycles, finalized 22:25 UTC 19 Jul / 06:25 MYT 20 Jul)"
ts["cycle_classification"] = (
    "QUIET / LOW-YIELD corroboration (Day-2 dawn continuing, post-midnight MYT). The 200000 + 212300 cycles (5th carry-forward) "
    "added +2 new PIR-06 [PRIORITY] cooperation-vector entities (Zambry + BN-PN pact Port Dickson meeting) over the 228-entity "
    "1954 build used by rev15. Both are COUNTER-vector (BN-PN pact strengthening) signals, NOT fracture signals. All 8 mandatory "
    "PIR-06 [CRITICAL]-watch gnews queries returned 0 fresh hard-news escalations. NO new [CRITICAL] threshold crossed (14th "
    "consecutive cycle). rev16 carries rev15 forward with 2 cooperation-vector additions; all 13 [CRITICAL] entities UNCHANGED."
)

# PIR-06 summary update
p6 = ts["pir_06"]
p6["verdict"] = (
    "[CRITICAL CARRIED - 14th consecutive cycle; no new threshold]. Bersatu sharp-negative internal-fracture signal CONFIRMED "
    "and STABLE across the SEVEN converging triggers (quorum+RoS two-pronged; 'lebih hebat' new-coalition; 'sasar bentuk "
    "kerajaan' solo-24-seat; 'PN toksik'; Hamzah rebuke; Khaled 'KO habis' elimination call; Khaled 'kacau daun'). Muhyiddin "
    "-0.92 and Bersatu -0.88 UNCHANGED this cycle (no >30% shift; no shift at all). The 212300 cycle added TWO COUNTER-vector "
    "cooperation-hardening entities: (1) Zambry (Umno Sec-Gen) + Samsuri (PN chairman) met in Port Dickson (N.05 Tier-4 seat) — "
    "leadership-level BN-PN pact confirmation on NS soil (Newswav 18 Jul 09:22); (2) 'BN-PN pact Port Dickson meeting' narrative — "
    "precursor to the 19 Jul 4-stage formalization trajectory. Both [PRIORITY] cooperation-vector, NOT fracture signals. "
    "The [CRITICAL] fracture-vector scores remain UNCHANGED; the cooperation-vector scores nudge upward."
)
p6["numeric_shift_check"] = (
    "rev15 -> rev16 deltas: ALL 13 [CRITICAL] entities UNCHANGED (0% shift): Muhyiddin -0.92, Bersatu -0.88, Bersatu-PN fracture "
    "-0.89, PN-removal -0.90, toxic PN -0.78, kuorum -0.65, RoS -0.62, lebih hebat -0.78, sasar bentuk kerajaan -0.80, pecat Tang "
    "Jay Son -0.40, Kiandee -0.25, PN Supreme Council -0.55, Bersatu MPT -0.72. NO PIR-06 entity crossed the >30% sharp-shift "
    "threshold (14th consecutive cycle). NEW cooperation-vector entities: Zambry +0.22 (PRIORITY), BN-PN pact PD meeting +0.30 "
    "(PRIORITY improving). 'sole opposition' source_count 4->5 (corroboration), score -0.50 stable."
)
p6["zambry_samsuri_pd_meeting_new"] = (
    "NEW [PRIORITY PIR-06] cooperation-vector. Zambry (Umno Sec-Gen/BN) met Samsuri (PN chairman/Terengganu MB) in Port Dickson "
    "(N.05 Tier-4 seat) on 18 Jul 09:22 MYT (Newswav gnews headline-intel). POLITICAL-LEADERSHIP-LEVEL BN-PN pact confirmation "
    "on NS soil — the precursor that enabled the 19 Jul 4-stage formalization (seat-swap -> gabung jentera -> manifesto bersepadu "
    "-> kongsi pentas). Adds N.05 to the active Tier-4 watch set. [PRIORITY] not [CRITICAL] — cooperation-hardening, NOT fracture."
)
p6["bn_pn_cooperation_stages"] = (
    "4-stage BN-PN cooperation formalization UNCHANGED this cycle, now with a CONFIRMED political-leadership precursor: "
    "(0) Zambry-Samsuri PD meeting 18 Jul [NEW rev16, leadership-tier precursor], (1) seat-swap, (2) gabung-jentera machinery "
    "merger +0.48, (3) manifesto bersepadu joint manifesto +0.48, (4) kongsi pentas joint ceramah +0.40, plus MB-concession-to-BN "
    "+0.15. WATCH: does 24 Jul BN manifesto launch become a JOINT BN-PN event? Trajectory (now with leadership-tier precursor) "
    "suggests HIGH likelihood."
)
p6["threshold_status"] = (
    "Formal pecat/termination NOT crossed (14th consecutive cycle). 7 converging [CRITICAL] triggers; formal PN-MT expulsion "
    "notice absent. The 212300 cycle added COUNTER-vector cooperation signals (Zambry-Samsuri PD meeting) — the cooperation "
    "trajectory is strengthening while the fracture trajectory remains FLAT/stable (not escalating)."
)
p6["offsetting_signals"] = (
    "Cooperation signals carried + STRENGTHENED this cycle: gabung-jentera +0.48, joint-manifesto +0.48, kongsi-pentas +0.40, "
    "MB-concession +0.15, BN +0.40, PAS/Hadi -0.22, Zahid +0.22, gelombang Melayu ke BN +0.30 (all carried). NEW: Zambry +0.22 "
    "(PRIORITY), BN-PN pact PD meeting +0.30 (PRIORITY improving). The political-leadership tier (Zambry-Samsuri) is now "
    "confirmed as the precursor to the operational 4-stage formalization."
)
# keep existing keys that are still valid; update lebih_hebat/sasar/etc to note "carried 14th cycle"
for k in ["lebih_hebat_new_coalition_sentiment", "sasar_bentuk_kerajaan_sentiment",
          "wawasan_admission_sentiment", "ros_complaint_disruption_sentiment",
          "pdm_klawang_reopen_sentiment", "toxic_termination_pecat_kuorum_lebih_hebat_trajectory",
          "bersatu_sharp_negative", "pm_discretion_new_entity"]:
    if k in p6:
        p6[k] = p6[k].replace("13th consecutive cycle", "14th consecutive cycle").replace(
            "13 cycles", "14 cycles").replace("Carried -0.78 CRITICAL. No escalation 13th cycle.",
            "Carried -0.78 CRITICAL. No escalation 14th consecutive cycle.")

# PIR-16 summary update
p16 = ts["pir_16"]
p16["verdict"] = (
    "[CRITICAL CARRIED - 'sasar bentuk kerajaan' + 'lebih hebat' persist at CRITICAL; STABLE, 14th consecutive cycle]. "
    "The 212300 cycle added NO new PIR-16 entities. The 'bipartisan clean-campaign convergence' [PRIORITY] (+0.42) from rev15 "
    "is carried forward. NO viral amplification >50% this cycle (quiet dawn window). The Zambry-Samsuri PD meeting (PIR-06) "
    "reinforces the BN-PN cooperation trajectory that underpins the 'makmal politik' PRU16 framing."
)
p16["viral_amplification_gt50"] = "NOT FIRED this cycle (quiet dawn; no narrative showed >50% volume increase). 14th consecutive cycle without re-trigger."
p16["hard_news_corroboration_bersatu_exit_or_sasar"] = (
    "FIRED (carried) - 'sasar bentuk kerajaan' (Bersatu-attributed, MalaysiaGazette + Sinar) = [CRITICAL] and 'lebih hebat' "
    "(multi-publisher) = [CRITICAL] both persist UNCHANGED. The specific 'Bersatu exit imminent?' mkini framing remains "
    "PRIORITY (viral-tier) because hard-news corroboration of THAT exact framing is absent across 14 cycles."
)
for k in ["bersatu_kacau_daun_sentiment", "sasar_vs_mb_after_prn_vs_joint_manifesto_vs_kongsi_pentas",
          "makmal_politik_sentiment", "bipartisan_clean_campaign_convergence_new",
          "mca_biggest_loser_and_rebuttal_trajectory", "dap_coalition_intolerant_frame_13_duns",
          "majoriti_mudah_vs_not_taking_for_granted", "resign_narrative_chain",
          "madani_reforms_continuity_ph_counter"]:
    if k in p16:
        p16[k] = p16[k].replace("13th consecutive cycle", "14th consecutive cycle").replace(
            "13 cycles", "14 cycles")

# PIR-07 summary update
p7 = ts["pir_07"]
p7["verdict"] = (
    "NO critical flag. No seat shows incumbent/leading-candidate sentiment drop >20% (Aminuddin +0.62 stable; Bakri Sawir "
    "+0.45 stable; Tok Mat +0.62 stable). The 212300 cycle added NO new PIR-07 entities. Director-flagged seats carried, "
    "NOT intensifying. The Zambry-Samsuri PD meeting (PIR-06) adds N.05 Port Dickson to the active Tier-4 watch set — "
    "a cooperation-vector signal on Tier-4 turf, not a seat-level sentiment shift."
)
for k in ["pertang_derhaka_friction", "pdm_klawang_shutdown_reopen_impact",
          "n14_defector_intensification", "bn_manifesto_launch_24_jul",
          "ph_manifesto_launch_20_jul", "evening_day1_to_day2_dawn_dispatch",
          "n19_johol_corroboration", "incumbent_drop_gt20"]:
    if k in p7:
        p7[k] = p7[k].replace("13th consecutive cycle", "14th consecutive cycle").replace(
            "13 cycles", "14 cycles")
p7["n05_port_dickson_new"] = (
    "NEW rev16. N.05 Port Dickson added to active Tier-4 watch set via the Zambry-Samsuri leadership meeting (Newswav 18 Jul "
    "09:22 MYT). A PIR-06 cooperation-vector signal on Tier-4 turf — NOT a seat-level incumbent/leading-candidate sentiment "
    "shift. Watch for Day-2 Port Dickson campaign coverage."
)

# Delta vs rev15
ts["delta_vs_rev15"] = {
    "new_entities_rev16": [
        "Zambry (Zambry Abd Kadir) - [NEW PIR-06, PRIORITY, +0.22, cooperation-vector; Umno Sec-Gen met Samsuri (PN chairman) in Port Dickson N.05]",
        "BN-PN pact Port Dickson meeting (Zambry-Samsuri) - [NEW PIR-06, PRIORITY, +0.30 improving, cooperation-hardening narrative; precursor to 4-stage formalization]"
    ],
    "revised_entities_rev16": [
        "sole opposition (Muhyiddin lone credible opposition): source_count 4 -> 5 (gnews cross-surfacing corroboration); score -0.50 STABLE"
    ],
    "unchanged_critical_entities": [
        "ALL 13 [CRITICAL] PIR-06 entities UNCHANGED (14th consecutive cycle, no new threshold): "
        "Muhyiddin -0.92, Bersatu -0.88, Bersatu-PN fracture -0.89, PN-removal -0.90, lebih hebat -0.78, "
        "sasar bentuk kerajaan -0.80, toxic PN -0.78, kuorum -0.65, RoS -0.62, pecat Tang Jay Son -0.40, "
        "Kiandee -0.25, PN Supreme Council -0.55, Bersatu MPT -0.72."
    ],
    "alert_count_change": "priority 51 -> 53 (+2 new cooperation-vector entities both priority). Critical 13 unchanged. None 173 unchanged."
}

# Collection limitations update
ts["collection_limitations"] = [
    "rev16 ingests the 230-entity 2225 build (5th carry-forward, cycles 200000 + 212300, finalized ~22:25 UTC 19 Jul / 06:25 MYT 20 Jul = Day-2 dawn). "
    "It is a QUIET / LOW-YIELD cycle: +2 new PIR-06 [PRIORITY] cooperation-vector entities (Zambry + BN-PN pact PD meeting), both single-source "
    "Newswav gnews headline-intel (full text not curl-recoverable). All 8 mandatory PIR-06 [CRITICAL]-watch gnews queries returned 0 fresh escalations.",
    "rev16 inherits all rev15 collection limitations (Kiandee NST headline-intelligence only; mkini 'Bersatu exit imminent?' body paywalled; "
    "'barking dogs' Albert Tei paywalled; N.20 Bembang candidate detail unrecovered; Mah Hang Soon response to Loke 'biggest loser' not surfaced; "
    "Zambry-Samsuri PD meeting full text not curl-recoverable).",
    "Day-2 dawn is a low-activity window; ceramah/ground coverage resumes Day-2 daytime. Watch for PDM Klawang reopen confirmation, "
    "PH manifesto 20 Jul coverage (Amirudin Shari, Klana Resort), BN manifesto 24 Jul (DUN Linggi + Pertang, potential JOINT BN-PN), "
    "and any Bersatu Supreme Council response to the quorum+RoS pressure.",
    "Folder migration: rev16 writes to 2026-07-19 (hyphenated, per mission YYYY-MM-DD spec). The 20260716 sentiment-analysis 1-day gap remains unfilled.",
    "Score convention SIGNED per mission directive (rev1-9 unsigned; rev10+ converted). PIR weights PIR-06=2.0, PIR-16=1.8, PIR-07=1.3.",
    "Alert-count change rev15->rev16: priority 51 -> 53 (+2 new cooperation-vector entities both priority). Critical 13 unchanged. None 173 unchanged."
]

# Next actions update
ts["next_actions"] = [
    "PIR-06 (HIGHEST): Watch Bersatu Supreme Council formal response to Kiandee quorum + RoS two-pronged pressure (14 cycles, no formal action). "
    "Monitor Muhyiddin 'lebih hebat'/'sasar' for FORMAL launch/withdrawal (would cross next tier). Watch 24 Jul BN manifesto launch - JOINT BN-PN event? "
    "(Trajectory now with leadership-tier Zambry-Samsuri precursor suggests HIGH likelihood.) Monitor PDM Klawang reopen (Day-2). "
    "Track Zambry-Samsuri PD meeting - does it surface in Day-2 Port Dickson campaign coverage?",
    "PIR-16 (HIGHEST): Track 'bipartisan clean-campaign convergence' - does it hold through Day-2 ceramah or fracture under 'derhaka'/resign pressure? "
    "Watch MCA rebuttal (Wee/Mah Hang Soon counter to Loke 'biggest loser'). Track Khaled 'PM discretion' framing - does it draw PH/AMH response? "
    "Watch 'majoriti mudah' at BN manifesto 24 Jul.",
    "PIR-07: Capture Day-2 ceramah for T1 seats - Klawang (cousins + PDM reopen), Linggi (Aminuddin + BN manifesto 24 Jul JOINT?), "
    "Chennah (Loke vs Siow, demographics risk + transport-minister rebuttal), Rantau (Tok Mat), Pertang (derhaka), Johol (Khaled machinery), "
    "Port Dickson N.05 (NEW - Zambry-Samsuri leadership meeting turf). Monitor razor-margin Kota + 5-corner Nilai/Sri Tanjung. Watch Nga response.",
    "Backfill the 20260716 sentiment-analysis 1-day gap. Reconcile folder migration (hyphenated 2026-07-19 vs non-hyphenated 20260719)."
]

# Remove old delta_vs_rev14 key (superseded by delta_vs_rev15)
if "delta_vs_rev14" in ts:
    del ts["delta_vs_rev14"]

# --- Write rev16 ---
with open(REV16_FILE, "w", encoding="utf-8") as f:
    json.dump(rev16, f, indent=2, ensure_ascii=False)

# --- Verify ---
with open(REV16_FILE, "r", encoding="utf-8") as f:
    verify = json.load(f)

print(f"rev16 written: {REV16_FILE}")
print(f"  version: {verify['metadata']['version']}")
print(f"  entity_count: {verify['metadata']['entity_count']}")
print(f"  critical_count: {verify['metadata']['critical_count']}")
print(f"  priority_count: {verify['metadata']['priority_count']}")
print(f"  none_count: {verify['metadata']['none_count']}")
print(f"  entities in array: {len(verify['entities'])}")

# Count by alert
from collections import Counter
alert_counts = Counter(e["alert"] for e in verify["entities"])
pir_counts = Counter(e["pir_tag"] for e in verify["entities"])
print(f"  alert breakdown: {dict(alert_counts)}")
print(f"  pir_tag breakdown: {dict(pir_counts)}")

# Show the 2 new entities
new_names = {"Zambry (Zambry Abd Kadir)", "BN-PN pact Port Dickson meeting (Zambry-Samsuri)"}
for e in verify["entities"]:
    if e["entity"] in new_names:
        print(f"  NEW: {e['entity']} | {e['pir_tag']} | {e['sentiment']} {e['score']} | alert={e['alert']} | src={e['source_count']}")

# Show sole opposition update
for e in verify["entities"]:
    if e["entity"] == "sole opposition (Muhyiddin lone credible opposition)":
        print(f"  UPDATED: {e['entity']} | src_count={e['source_count']} | score={e['score']}")

# Verify all 13 critical entities unchanged
critical_entities = [e for e in verify["entities"] if e["alert"] == "critical"]
print(f"\n  [CRITICAL] entities ({len(critical_entities)}):")
for e in critical_entities:
    print(f"    {e['entity']}: {e['score']} ({e['trend']})")
