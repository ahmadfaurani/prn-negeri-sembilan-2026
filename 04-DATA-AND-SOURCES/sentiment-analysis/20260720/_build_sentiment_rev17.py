#!/usr/bin/env python3
"""
Build revision-17 sentiment analysis for 2026-07-20.
Carries forward rev-16 (239 entries, built on 230-entity 2225 build) and applies
deltas from the 232-entity 0106 build (6th carry-forward, cycles 222800 + 233400).

Deltas:
  NEW entities (2):
    - "Bersatu Johor-wipeout-repeat framing (Khaled, FMT)" [PIR-06 PRIORITY]
    - "Loke baptism of fire (Chennah battle, Newswav)" [PIR-07 normal]
  UPDATED entities (3 context updates):
    - Mohamed Khaled Nordin: 5th outlet (FMT EN Johor-precedent), marginal deepening
    - Bersatu KO habis: 5th outlet (FMT EN Johor-precedent), marginal deepening
    - 19 campaign permits approved: Malay Mail outlet added, no sentiment shift

All 13 [CRITICAL] PIR-06 entities UNCHANGED (18th consecutive cycle, no new threshold).
"""
import json, copy, os

SRC = "/home/p62operator/.openclaw/workspace-ns/04-DATA-AND-SOURCES/sentiment-analysis/2026-07-19/sentiment-20260720-0625.json"
OUTDIR = "/home/p62operator/.openclaw/workspace-ns/04-DATA-AND-SOURCES/sentiment-analysis/2026-07-20"
OUT = os.path.join(OUTDIR, "sentiment-20260720-1010.json")

os.makedirs(OUTDIR, exist_ok=True)

with open(SRC, "r", encoding="utf-8") as f:
    data = json.load(f)

entries = data["entities"]

# --- Apply context updates to existing entries ---
updated_count = 0
for e in entries:
    name = e["entity"]

    if name == "Mohamed Khaled Nordin":
        # 5th outlet corroboration (FMT EN "Johor wipeout repeat" 07:12 MYT 20 Jul)
        # adds Johor-as-precedent framing; marginal deepening -0.31 -> -0.32
        e["score"] = round(-0.32, 2)
        e["source_count"] = 5  # already 5 (Awani added in rev15); FMT EN is 5th outlet but source_count already 5
        # Actually rev16 rationale says source_count=5; the FMT EN is the SAME 5th outlet.
        # Per entity summary: "5th-outlet corroboration" means NST EN + Utusan BM + BH BM + Awani BM + FMT EN = 5 outlets
        e["trend"] = "declining"
        e["alert"] = "priority"
        e["rationale"] = (
            "rev16 -0.31 -> rev17 -0.32. Umno VP / Defence Minister. 5-outlet corroboration "
            "(NST EN + Utusan BM + BH BM + Awani BM + FMT EN, 23:49-07:12 MYT 19-20 Jul). "
            "Anti-Bersatu electoral-elimination: 'Pastikan Bersatu di NS KO habis-habis' / "
            "'make sure Bersatu gets knocked out'. FMT EN (07:12 MYT 20 Jul) adds Johor-as-precedent "
            "framing — explicitly names the Johor state-election wipeout as the model to repeat. "
            "Frames Bersatu 'ditubuhkan nak ganti UMNO' + 'kacau daun'. Pro BN-PN: 'persefahaman BN-PN "
            "beri kelebihan vs Johor'; 'gelombang Melayu ke BN'. Dismisses AMK resign-call ('dia cakap "
            "sajalah dengan Ketua Parti dia'). 'PM hak mutlak' framing (4-outlet). Spoke at Johol BN "
            "machinery launch. Rhetorical escalation; NOT formal PN-MT action. [PRIORITY] not [CRITICAL]."
        )
        updated_count += 1

    elif name == "Bersatu KO habis (electoral-elimination call)":
        # 5th outlet (FMT EN Johor-precedent), marginal deepening -0.55 -> -0.56
        e["score"] = round(-0.56, 2)
        e["source_count"] = 5  # NST EN + Utusan BM + BH BM + Awani BM + FMT EN
        e["trend"] = "declining"
        e["alert"] = "priority"
        e["rationale"] = (
            "rev16 -0.55 -> rev17 -0.56. Khaled Nordin 5-publisher (NST EN + Utusan BM + BH BM + "
            "Awani BM + FMT EN, 23:49-07:12 MYT 19-20 Jul). 'Pastikan BERSATU di NS KO habis' — "
            "urges voters reject Bersatu so all 24 lose deposits, paving way for BN straight fights "
            "next PRU. FMT EN (07:12 MYT 20 Jul) is FIRST to explicitly frame the NS wipeout as a "
            "REPEAT of Bersatu's Johor state-election wipeout (Johor-as-precedent). Director PIR-06 "
            "keywords 'keluar/pecat/tarik diri' = coalition-membership actions; THIS is electoral-"
            "elimination rhetoric by a BN (not PN) leader — adjacent but NOT formal PN-MT expulsion/"
            "withdrawal. [PRIORITY] not [CRITICAL]."
        )
        updated_count += 1

    elif name == "19 campaign permits approved":
        # Malay Mail outlet added (19 Jul 11:00 MYT); same event, no sentiment shift
        e["source_count"] = 3  # NST 12:26 + Kosmo 10:54 + Malay Mail 11:00
        e["score"] = 0.30
        e["trend"] = "stable"
        e["alert"] = "none"
        e["rationale"] = (
            "rev16 carried. 233400 UPDATE: Malay Mail 'Police approve 19 permits as Negeri Sembilan "
            "campaigns get under way' (19 Jul 11:00 MYT, gnews headline-intel; Malay Mail full-text "
            "URL not curl-recoverable) — 3rd-outlet version of the same '19 campaign permits approved' "
            "story (prior: NST 12:26 + Kosmo 10:54 + Awani). New outlet, same event; no new "
            "intelligence. source_count 2->3; score 0.30 STABLE."
        )
        updated_count += 1

    elif name == "Bersatu Johor-wipeout-repeat framing (Khaled, FMT)":
        # This entity already exists in rev16? Check — it was added as a NEW entity in the 0106 build
        # but rev16 was built on the 2225 build (230 entities) which did NOT have it.
        # Actually, looking at the entity file, this IS a new entity in the 0106 build.
        # But rev16 might not have it. Let me check — rev16 was built on 2225 (230 entities).
        # The 0106 build (232 entities) added it. So rev16 does NOT have this entity.
        # We'll add it below. But if it somehow exists, update it.
        pass

# --- Add NEW entities ---
new_entities = [
    {
        "entity": "Bersatu Johor-wipeout-repeat framing (Khaled, FMT)",
        "pir_tag": "PIR-06",
        "sentiment": "negative",
        "score": -0.50,
        "trend": "declining",
        "alert": "priority",
        "source_count": 1,
        "rationale": (
            "NEW rev17 (6th carry-forward, 0106 build, 233400 cycle). FMT EN (07:12 MYT 20 Jul, "
            "gnews headline-intel; FMT direct URL not curl-recoverable — 404 across 10 category/day "
            "guesses; gnews protobuf still curl-unresolvable, 18th cycle). Khaled Nordin frames the "
            "targeted NS Bersatu wipeout as a REPEAT of Bersatu's Johor state-election result (where "
            "Bersatu was wiped out). Prior 'KO habis' captures (NST EN + Utusan BM + BH BM + Awani BM, "
            "171500) used 'KO habis'/'knocked out' but did NOT explicitly name the Johor precedent — "
            "FMT is the first to make the Johor-as-precedent framing explicit. Reinforces the PIR-06 "
            "electoral-elimination vector (BN VP publicly urging Bersatu's electoral destruction while "
            "BN operationally cooperates with Bersatu's coalition partners via PN). Director PIR-06 "
            "keywords 'keluar'/'pecat'/'tarik diri'/'kuorum'/'lebih hebat' are about coalition-membership "
            "actions; this is electoral-elimination rhetoric by a BN (not PN) leader — adjacent, NOT "
            "[CRITICAL]. [PRIORITY PIR-06]."
        ),
    },
    {
        "entity": "Loke baptism of fire (Chennah battle, Newswav)",
        "pir_tag": "PIR-07",
        "sentiment": "neutral",
        "score": -0.10,
        "trend": "stable",
        "alert": "none",
        "source_count": 1,
        "rationale": (
            "NEW rev17 (6th carry-forward, 0106 build). Newswav (18 Jul 16:30 MYT, gnews headline-intel; "
            "pre-cutoff / nomination-day). Newswav frames Anthony Loke's Chennah defense as a 'baptism "
            "of fire' in the NS polls. Chennah = the only MCA-DAP straight fight (Loke PH/DAP sec-gen "
            "vs Siow Kong Choon MCA/BN); 47.8% Malay (up from 44% in 2018), 6.3% Orang Asli, 42.6% "
            "Chinese; PH vote dropped to 44% by PRU15 vs BN+PN combined 56% -> if PRU15 pattern repeats "
            "Loke LOSES (mkini 780075 full text). The 'baptism of fire' framing reinforces the PIR-16 "
            "'MCA biggest loser' / Loke-under-pressure narrative and the PIR-07 marquee-battleground "
            "status of Chennah. [normal PIR-07] — analytical framing, not a hard-news development."
        ),
    },
]

entries.extend(new_entities)

# --- Update trend_summary ---
ts = data["trend_summary"]
ts["revision"] = (
    "revision-17 (built on entities-20260720-0106.json, 232 entities, 6th carry-forward, "
    "cycles 222800 + 233400, finalized ~02:10 UTC 20 Jul / 10:10 MYT 20 Jul = Day-2 morning)"
)
ts["cycle_classification"] = (
    "QUIET / LOW-YIELD (Day-2 morning, post-midnight MYT, World Cup final dominated overnight coverage). "
    "The 222800 + 233400 cycles (6th carry-forward) added +2 new entities over the 230-entity 2225 build "
    "used by rev16: (1) 'Bersatu Johor-wipeout-repeat framing' [PIR-06 PRIORITY] — FMT EN Johor-as-"
    "precedent framing of Khaled's 'KO habis' call; (2) 'Loke baptism of fire' [PIR-07 normal] — Newswav "
    "analytical framing of Loke's Chennah defense. 3 context updates: Khaled (5th outlet + Johor-"
    "precedent), Bersatu KO habis (5th outlet + Johor-precedent), 19 permits (Malay Mail 3rd outlet). "
    "22 of 25 'fresh' items across 222800+233400 = FALSE POSITIVES (World Cup ×9, South-China-Sea "
    "defence, Iraq-Iran-US diplomacy, etc.). Genuinely-fresh post-cutoff NS PRN content = 1 article "
    "(FMT EN Khaled 'Johor wipeout repeat'). All 8 mandatory PIR-06 [CRITICAL]-watch gnews queries "
    "returned 0 fresh hard-news escalations. NO new [CRITICAL] threshold crossed (18th consecutive "
    "cycle). rev17 carries rev16 forward with 2 additions + 3 context updates; all 13 [CRITICAL] "
    "entities UNCHANGED."
)

# PIR-06
p06 = ts["pir_06"]
p06["verdict"] = (
    "[CRITICAL CARRIED - 18th consecutive cycle; no new threshold]. Bersatu sharp-negative internal-"
    "fracture signal CONFIRMED and STABLE across the SEVEN converging triggers (quorum+RoS two-pronged; "
    "'lebih hebat' new-coalition; 'sasar bentuk kerajaan' solo-24-seat; 'PN toksik'; Hamzah rebuke; "
    "Khaled 'KO habis' elimination call; Khaled 'kacau daun'). Muhyiddin -0.92 and Bersatu -0.88 "
    "UNCHANGED this cycle (no >30% shift). The 233400 cycle added ONE new PIR-06 [PRIORITY] entity: "
    "'Bersatu Johor-wipeout-repeat framing' (FMT EN, Khaled Johor-as-precedent) — rhetorical corroboration "
    "of the 'KO habis' elimination call, NOT a fracture signal. All 13 [CRITICAL] entities UNCHANGED."
)
p06["numeric_shift_check"] = (
    "rev16 -> rev17 deltas: ALL 13 [CRITICAL] entities UNCHANGED (0% shift): Muhyiddin -0.92, Bersatu "
    "-0.88, Bersatu-PN fracture -0.89, PN-removal -0.90, toxic PN -0.78, kuorum -0.65, RoS -0.62, lebih "
    "hebat -0.78, sasar bentuk kerajaan -0.80, pecat Tang Jay Son -0.40, Kiandee -0.25, PN Supreme "
    "Council -0.55, Bersatu MPT -0.72. NO PIR-06 entity crossed the >30% sharp-shift threshold (18th "
    "consecutive cycle). UPDATED: Mohamed Khaled Nordin -0.31->-0.32 (marginal, 5th outlet Johor-"
    "precedent); Bersatu KO habis -0.55->-0.56 (marginal, 5th outlet Johor-precedent). NEW: Bersatu "
    "Johor-wipeout-repeat framing -0.50 [PRIORITY]."
)

# PIR-16
p16 = ts["pir_16"]
p16["verdict"] = (
    "[CRITICAL CARRIED - 'sasar bentuk kerajaan' + 'lebih hebat' persist at CRITICAL; STABLE, 18th "
    "consecutive cycle]. The 233400 cycle added NO new PIR-16 entities. The 'bipartisan clean-campaign "
    "convergence' [PRIORITY] (+0.42) from rev15 is carried forward. NO viral amplification >50% this "
    "cycle (quiet morning window, World Cup dominated)."
)

# PIR-07
p07 = ts["pir_07"]
p07["verdict"] = (
    "NO critical flag. No seat shows incumbent/leading-candidate sentiment drop >20% (Aminuddin +0.62 "
    "stable; Bakri Sawir +0.45 stable; Tok Mat +0.62 stable). The 233400 cycle added ONE new PIR-07 "
    "[normal] entity: 'Loke baptism of fire' (Newswav analytical framing of Chennah battle). Director-"
    "flagged seats carried, NOT intensifying."
)

# Delta section
ts["delta_vs_rev16"] = {
    "new_entities_rev17": [
        "Bersatu Johor-wipeout-repeat framing (Khaled, FMT) - [NEW PIR-06, PRIORITY, -0.50, declining; FMT EN Johor-as-precedent framing of 'KO habis' call]",
        "Loke baptism of fire (Chennah battle, Newswav) - [NEW PIR-07, normal, -0.10, stable; analytical framing of Loke's Chennah defense]",
    ],
    "revised_entities_rev17": [
        "Mohamed Khaled Nordin: score -0.31 -> -0.32 (marginal deepening, 5th outlet Johor-precedent); source_count 5; trend declining",
        "Bersatu KO habis (electoral-elimination call): score -0.55 -> -0.56 (marginal, 5th outlet Johor-precedent); source_count 4->5; trend declining",
        "19 campaign permits approved: source_count 2->3 (Malay Mail 3rd outlet added); score 0.30 STABLE",
    ],
    "unchanged_critical_entities": [
        "ALL 13 [CRITICAL] PIR-06 entities UNCHANGED (18th consecutive cycle, no new threshold): Muhyiddin -0.92, Bersatu -0.88, Bersatu-PN fracture -0.89, PN-removal -0.90, lebih hebat -0.78, sasar bentuk kerajaan -0.80, toxic PN -0.78, kuorum -0.65, RoS -0.62, pecat Tang Jay Son -0.40, Kiandee -0.25, PN Supreme Council -0.55, Bersatu MPT -0.72.",
    ],
    "alert_count_change": "priority 53 -> 54 (+1 new PIR-06 PRIORITY entity 'Bersatu Johor-wipeout-repeat framing'). Critical 13 unchanged. None 173 -> 174 (+1 new PIR-07 normal entity 'Loke baptism of fire'). Total entries 239 -> 241.",
}

# Update collection_limitations
ts["collection_limitations"] = [
    "rev17 ingests the 232-entity 0106 build (6th carry-forward, cycles 222800 + 233400, finalized ~01:06 MYT 20 Jul = Day-2 dawn). QUIET / LOW-YIELD cycle: +2 new entities, 3 context updates. 22 of 25 'fresh' items = FALSE POSITIVES (World Cup final Argentina-Spain dominated overnight; Spain won via Torres). Genuinely-fresh post-cutoff NS PRN content = 1 article (FMT EN Khaled 'Johor wipeout repeat').",
    "gnews protobuf URLs remain curl-unresolvable (18th consecutive cycle). FMT direct URL for Khaled 'Johor wipeout repeat' article returned 404 across 10 category/day guesses.",
    "rev17 inherits all rev16 collection limitations (Kiandee NST headline-intelligence only; mkini 'Bersatu exit imminent?' body paywalled; 'barking dogs' Albert Tei paywalled; N.20 Bembang candidate detail unrecovered; Mah Hang Soon response to Loke 'biggest loser' not surfaced; Zambry-Samsuri PD meeting full text not curl-recoverable).",
    "Day-2 morning is a low-activity window; ceramah/ground coverage resumes Day-2 daytime. Watch for PDM Klawang reopen confirmation, PH manifesto 20 Jul coverage (Amirudin Shari, Klana Resort), BN manifesto 24 Jul (DUN Linggi + Pertang, potential JOINT BN-PN), and any Bersatu Supreme Council response to the quorum+RoS pressure.",
    "Score convention SIGNED per mission directive (rev1-9 unsigned; rev10+ converted). PIR weights PIR-06=2.0, PIR-16=1.8, PIR-07=1.3.",
    "Alert-count change rev16->rev17: priority 53 -> 54 (+1 new PIR-06 PRIORITY). Critical 13 unchanged. None 173 -> 174 (+1 new PIR-07 normal). Total 239 -> 241.",
]

ts["next_actions"] = [
    "PIR-06 (HIGHEST): Watch Bersatu Supreme Council formal response to Kiandee quorum + RoS two-pronged pressure (18 cycles, no formal action). Monitor Muhyiddin 'lebih hebat'/'sasar' for FORMAL launch/withdrawal (would cross next tier). Watch 24 Jul BN manifesto launch - JOINT BN-PN event? (Trajectory with leadership-tier Zambry-Samsuri precursor suggests HIGH likelihood.) Monitor PDM Klawang reopen (Day-2). Track Khaled 'Johor-wipeout-repeat' framing - does it gain Day-2 traction?",
    "PIR-16 (HIGHEST): Track 'bipartisan clean-campaign convergence' - does it hold through Day-2 ceramah or fracture under 'derhaka'/resign pressure? Watch MCA rebuttal (Wee/Mah Hang Soon counter to Loke 'biggest loser'). Track Khaled 'PM discretion' framing - does it draw PH/AMH response? Watch 'majoriti mudah' at BN manifesto 24 Jul.",
    "PIR-07: Capture Day-2 ceramah for T1 seats - Klawang (cousins + PDM reopen), Linggi (Aminuddin + BN manifesto 24 Jul JOINT?), Chennah (Loke vs Siow, demographics risk + 'baptism of fire' framing + transport-minister rebuttal), Rantau (Tok Mat), Pertang (derhaka), Johol (Khaled machinery), Port Dickson N.05 (Zambry-Samsuri leadership meeting turf). Monitor razor-margin Kota + 5-corner Nilai/Sri Tanjung. Watch Nga response.",
    "Backfill the 20260716 sentiment-analysis 1-day gap. Reconcile folder migration (hyphenated 2026-07-19/20 vs non-hyphenated 20260719).",
]

# Write output
data["entities"] = entries
data["trend_summary"] = ts
data["generated_at"] = "2026-07-20T10:10:00+08:00"
data["source_entity_file"] = "entities-20260720-0106.json"
data["prior_revision"] = "revision-16 (sentiment-20260720-0625.json)"

with open(OUT, "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

# Count alerts
critical = sum(1 for e in entries if e["alert"] == "critical")
priority = sum(1 for e in entries if e["alert"] == "priority")
none_alert = sum(1 for e in entries if e["alert"] == "none")
print(f"Written: {OUT}")
print(f"Total entries: {len(entries)}")
print(f"Critical: {critical}, Priority: {priority}, None: {none_alert}")
print(f"Context updates applied: {updated_count}")
print(f"New entities added: {len(new_entities)}")
