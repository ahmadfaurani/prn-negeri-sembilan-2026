#!/usr/bin/env python3
"""
NS PRN 2026 Sentiment Analysis — Delta Merge (Revision 3).

Merges the 19:19 MYT collection delta (raw-scrape batch _111951 +
nomination-day-summary-1919) into the existing sentiment_analysis.json
(revision 2 finalized 2026-07-18T19:50 MYT / 11:50 UTC, built on the
_010044 + _070937 + _083302 batches + summaries-1509/1633).

Standing method: agent-manual source-attributed review (CVS-compliant).
Author runtime: GLM-5.2 (custom) — manual review fallback (ESC-002, Day 8).

CVS standard: sentiment based on verified source content only; all entities
source-attributed (verbatim surface match); SPR candidate list as ground truth.
Intelligence summaries (nomination-day-summary-1919.md) used only to LOCATE
items; underlying media source files cited as attribution per CVS standard.

DELTA RATIONALE:
  entities_consolidated.json was regenerated at 11:52 UTC (2 minutes AFTER the
  revision-2 sentiment pass at 11:50). The 11:52 extraction spans 41 source
  files (vs 31 at revision-2's 08:46 baseline): +10 new files = the _111951
  scrape batch (9 files) + nomination-day-summary-1919.md (1 intelligence asset).
  politicians 34 -> 38 (+4, notably R. Ramanan at 20 mentions). This delta was
  not sentiment-analyzed by revision 2. Revision 3 closes that gap.

KEY NEW SIGNAL (Cycle 3, 19:19 MYT, per summary-1919):
  1. "PN has grounds to remove Bersatu, says Kiandee" (NST) — the Bersatu-PN
     termination threat moves from "could face termination" (15:09) /
     "info chief floats termination" (16:33) to a concrete assertion that PN
     HAS GROUNDS to remove Bersatu. Strongest signal yet that ESC-010/ESC-011
     may formalize into an actual expulsion during the campaign window
     (escalation trigger #2 adjacent). Single highest-priority watch item.
  2. Zahid Hamidi deploys to JEMPOL + introduces explicit realignment/
     bellwether framing — Star (Jempol): "New political alignments needed to
     ensure stability"; Astro Awani: "PRN NS: Prestasi BN-PN mungkin jadi
     penentu jajaran baharu PRN Melaka, PRU16 — Ahmad Zahid." Elevates NS
     strategic stakes to a determinant of future national coalition
     restructuring.
  3. R. Ramanan (PKR VP, Sungai Buloh MP) at Wisma MBS nomination centre
     backing 6 PH candidates — first concrete PH machinery mobilisation datum.
  4. Hadi (Jempol) confirms the split is now 3-way: Bersatu vs (PN+PAS).
  5. NST independently corroborates EC's 21 three-cornered + 2 five-way figure
     (N.10 Nilai, N.33 Sri Tanjung) — PIR-04 lifted to CONFIRMED.
"""
import json, os
from datetime import datetime, timezone, timedelta

MYT = timezone(timedelta(hours=8))
BASE = "/home/p62operator/.openclaw/workspace-ns/04-DATA-AND-SOURCES/processed-entities/20260718"
PATH = os.path.join(BASE, "sentiment_analysis.json")

with open(PATH, "r", encoding="utf-8") as f:
    d = json.load(f)

# ---------------------------------------------------------------------------
# 1. Revision history
# ---------------------------------------------------------------------------
rev_now = datetime.now(MYT).strftime("%Y-%m-%dT%H:%M:%S+08:00")
d.setdefault("revision_history", [])
d["revision_history"].append({
    "revision": 3,
    "timestamp": rev_now,
    "scope": "delta merge of the 19:19 MYT collection cycle (raw-scrape _111951 batch + nomination-day-summary-1919) into the revision-2 baseline (which covered _010044 + _070937 + _083302 + summaries-1509/1633)",
    "rationale": "entities_consolidated.json was regenerated at 11:52 UTC (2 min after the 11:50 revision-2 pass). The 11:52 extraction spans 41 source files (+10 vs the revision-2 08:46 baseline of 31): the _111951 scrape batch (9 files) + nomination-day-summary-1919.md. politicians 34->38 (+4, incl. R. Ramanan 20x). This delta was not sentiment-analyzed by revision 2.",
    "method": "agent-manual source-attributed review (CVS-compliant) + SPR candidate-list cross-reference; intelligence summary used only to locate items, media files cited as attribution",
    "runtime": "GLM-5.2 (custom) — manual review fallback (ESC-002, Day 8)",
    "delta_sources_new": 10,
    "delta_politicians_new": 4,
    "delta_scored_new": 1,
})

# ---------------------------------------------------------------------------
# 2. Update top-level metadata
# ---------------------------------------------------------------------------
d["generated"] = rev_now
d["status"] = "completed (revision 3 — Cycle 3 / 19:19 MYT delta merged)"
d["sentiment_model_runtime"] = (
    "GLM-5.2 (custom) — manual review fallback. Revision 3 applied after detecting "
    "that entities_consolidated.json was regenerated at 11:52 UTC (41 sources / 150 "
    "entities), 2 minutes after the 11:50 revision-2 pass (31 sources). The 10 new "
    "source files (raw-scrape _111951 batch + nomination-day-summary-1919) were not "
    "covered by revision 2."
)
d["openosint_status"] = (
    "NOT ACTIVE — ns-sentiment-analysis.sh remains a stub (prints empty JSON to "
    "stdout, entities_analyzed:0, does NOT write sentiment_analysis.json, does NOT "
    "call OpenOSINT/Aras API). No credentials in environment. Agent-manual review is "
    "the standing CVS-compliant method (ESC-002, Day 8). Revision 3 applied by "
    "GLM-5.2 manual-review fallback."
)

# ---------------------------------------------------------------------------
# 3. Update source_basis to include the Cycle-3 corpus (41 sources)
# ---------------------------------------------------------------------------
sb = d["source_basis"]
sb["collection_batches"]["_111951"] = {
    "files": 9,
    "covered_by_revision2": False,
    "covered_by_revision3": True,
    "window": "19:19 MYT (11:19 UTC) — Cycle 3 of Nomination Day",
    "note": "raw-scrape batch: bharian, freemalaysiatoday, kosmo, malaysiakini, mstar, nst, ohbulan, thestar, utusan",
}
sb["collection_batches"]["nomination-day-summary-1919"] = {
    "files": 1,
    "intelligence_asset": True,
    "covered_by_revision3": True,
    "supersedes": "nomination-day-summary-1633.md for escalation-flag currency",
    "note": "PIR-framework Nomination Day Surge product, Cycle 3 (19:19 MYT). Used to LOCATE items only; media source files cited as attribution per CVS.",
}
sb["total_source_files"] = 41
sb["total_entities_extracted"] = 150
sb["intelligence_summaries"] = (
    "nomination-day-summary-1509.md + -1633.md + -1919.md (PIR-framework Nomination "
    "Day Surge products) — used as structured cross-reference; all sentiment entries "
    "are re-attributed to underlying media source files per CVS standard."
)
sb["cvs_standard"] = (
    "Sentiment based on verified source content only. No pattern-inferred sentiment. "
    "All entities source-attributed (verbatim surface match). SPR candidate list used "
    "as ground-truth cross-reference. Intelligence summaries used only to locate "
    "items; media source files cited as attribution."
)

# ---------------------------------------------------------------------------
# 4. Append DELTA sentiment_summary entries (prefixed [19:19Δ])
# ---------------------------------------------------------------------------
D_POS = [
    {
        "entity": "[19:19Δ] Datuk Seri R. Ramanan (PKR VP / Sungai Buloh MP — federal surrogate) — first concrete PH nomination-centre mobilisation",
        "category": "politician (federal surrogate / machinery)",
        "sentiment": "positive",
        "score": 0.55,
        "rationale": (
            "NEW (20 occurrences — highest-visibility NEW politician in the 11:52 extraction; absent from the revision-2 corpus). "
            "The Star (SEREMBAN, Wisma MBS / Seremban City Council Building nomination centre, 18 Jul): PKR vice-president and Sungai "
            "Buloh MP Datuk Seri R. Ramanan was at the nomination centre to show support for six Pakatan Harapan (PH) candidates. Per "
            "nomination-day-summary-1919 (PIR-13/PIR-22): 'the first concrete nomination-centre mobilisation datum of the day, "
            "indicating coordinated PH machinery concentration at the Seremban nomination centre.' Positive for PH: a named federal-level "
            "surrogate (PKR VP + MP) physically deployed to back 6 PH candidates signals coordinated PH machinery — extending the "
            "revision-2 finding that PH's edge shifted from STRUCTURAL to STRUCTURAL+NARRATIVE now adds a MACHINERY/mobilisation dimension. "
            "CAVEAT (CVS): R. Ramanan is a federal MP (Sungai Buloh, Selangor), NOT an NS candidate; he is a surrogate/mobiliser. No "
            "candidate of his appears under a Ramanan name in the SPR NS list. Scored for the mobilisation signal, not as a contesting candidate."
        ),
        "sources": ["thestarcommy_20260718_111951.md", "nomination-day-summary-1919.md", "entities_politicians.json"],
        "confidence": "HIGH — The Star dateline-confirmed (SEREMBAN/Wisma MBS) + cross-referenced to intelligence summary; federal-surrogate role verified",
    },
]
# No new neutral or negative sentiment_summary entries: the Bersatu-PN
# formalization escalation is captured as a revision3_update to the existing
# ESC-011 negative entry + a NEW escalation FLAG (ESC-014) + a NEW narrative
# indicator (NAR-18), avoiding duplication of the existing fracture entry.
D_NEU = []
D_NEG = []

d["sentiment_summary"]["positive"].extend(D_POS)
d["sentiment_summary"]["neutral"].extend(D_NEU)
d["sentiment_summary"]["negative"].extend(D_NEG)

# ---------------------------------------------------------------------------
# 5. Update sentiment_distribution (revision-3 merged)
# ---------------------------------------------------------------------------
d["sentiment_distribution_baseline_0831"] = d.get("sentiment_distribution_baseline_0831") or {
    "positive": 4, "neutral": 4, "negative": 4, "total": 12
}
prev = d.get("sentiment_distribution", {})
d["sentiment_distribution"] = {
    "positive": len(d["sentiment_summary"]["positive"]),
    "neutral": len(d["sentiment_summary"]["neutral"]),
    "negative": len(d["sentiment_summary"]["negative"]),
    "total_scored": len(d["sentiment_summary"]["positive"]) + len(d["sentiment_summary"]["neutral"]) + len(d["sentiment_summary"]["negative"]),
    "baseline_0831": {"positive": 4, "neutral": 4, "negative": 4, "total": 12},
    "delta_1633": prev.get("delta_1633", {"positive": 6, "neutral": 5, "negative": 2}),
    "delta_1919": {"positive": len(D_POS), "neutral": len(D_NEU), "negative": len(D_NEG)},
    "note": (
        "Revision-3 merged distribution. Baseline (08:31) 4/4/4; revision-2 delta (16:33) +6 pos/+5 neu/+2 neg -> 10/9/6; "
        "revision-3 delta (19:19) +1 pos (R. Ramanan PH machinery mobilisation) -> 11/9/6. NET: the PH-favorable tilt "
        "STRENGTHENS further with the first concrete PH machinery/mobilisation datum (a named federal surrogate deployed "
        "to back 6 PH candidates at the Seremban nomination centre). The dominant development of Cycle 3 is the "
        "ESCALATION of the Bersatu-PN split TOWARD FORMALIZATION — 'PN has grounds to remove Bersatu, says Kiandee' "
        "(NST) — captured as ESC-014 (CRITICAL, NEW) and as updates to ESC-010/ESC-011, not as a new sentiment_summary "
        "entry (it deepens the existing fracture entry rather than introducing a new sentiment dimension)."
    ),
}

# ---------------------------------------------------------------------------
# 6. Update party_sentiment_matrix (revision-3 delta notes)
# ---------------------------------------------------------------------------
psm = d["party_sentiment_matrix"]
psm["PH"]["revision3_delta"] = (
    "MACHINERY/MOBILISATION dimension added. R. Ramanan (PKR VP, Sungai Buloh MP) deployed "
    "to the Wisma MBS (Seremban City Council) nomination centre to back 6 PH candidates (The "
    "Star, SEREMBAN) — the first concrete nomination-centre mobilisation datum of the day. "
    "PH's edge is now STRUCTURAL + NARRATIVE (rev 2) + MACHINERY (rev 3). PH's proactive posture "
    "continues to strengthen."
)
psm["PN"]["revision3_delta"] = (
    "TOWARD FORMALIZATION of the Bersatu split. NST (Kiandee): 'PN has grounds to remove Bersatu' "
    "— the termination threat acquires concrete 'grounds' (progression: 15:09 'could face' -> "
    "16:33 'info chief floats' -> 19:19 'has grounds'). The highest-priority watch item: if PN "
    "executes the removal, the opposition restructures mid-campaign (trigger #2). PN now openly "
    "contemplating procedural expulsion of its largest former Malay component."
)
psm["Bersatu"]["revision3_delta"] = (
    "Faces formalization of the split. PN 'has grounds to remove Bersatu' (Kiandee, NST) — "
    "Bersatu's independent posture (24 seats, fighting allies in 20/24) now risks an actual "
    "procedural expulsion from PN during the campaign window. Muhyiddin's 'sole opposition' / "
    "'PN supports government' posture (rev 2) continues. Bersatu's defiance is unchanged but "
    "now carries an expulsion risk."
)
psm["BN"]["revision3_delta"] = (
    "Zahid ELEVATES the NS strategic stakes to a bellwether/realignment determinant. The Star "
    "(JEMPOL): 'New political alignments needed to ensure stability, says Ahmad Zahid'; Astro "
    "Awani: 'PRN Negeri Sembilan: Prestasi BN-PN mungkin jadi penentu jajaran baharu PRN Melaka, "
    "PRU16 — Ahmad Zahid.' The BN/UMNO president publicly frames the NS result as a determinant "
    "of future national coalition restructuring (Melaka PRN + PRU16 lineups) — rhetorically "
    "adjacent to trigger #2. BN's 'understanding, not merger' containment (rev 2) is reinforced; "
    "BN confident of simple majority (Star ticker, carried)."
)
psm["PAS"] = psm.get("PAS", {
    "status": "PRESENT (8 occ, rev 2) — NEUTRAL-POSITIVE (confident, now dominant in diminished PN)",
    "surrogates_detected": ["Kamarol Ridzuan Mohd Zain (PAS NS Deputy Comm, PN candidate Paroi)"],
    "assessment": "PAS is now the dominant component of a diminished PN (Bersatu split away).",
    "cvs_status": "VERIFIED — NST + SPR",
})
psm["PAS"]["revision3_delta"] = (
    "Hadi (JEMPOL, NST) confirms PAS is now the THIRD PARTY in the Bersatu-vs-PN confrontation — "
    "the split is Bersatu vs (PN+PAS), three-way. PAS 'ready to face Bersatu' (NST) and Hadi "
    "personally dismisses Muhyiddin's 'toxic PN' claim (rev 2). PAS now openly at war with Bersatu; "
    "the PN-removal-of-Bersatu threat (Kiandee) advances PAS's position as the surviving Malay core of PN."
)

# ---------------------------------------------------------------------------
# 7. Append DELTA narrative_indicators (NAR-18, NAR-19) + revision3_update NAR-12/16
# ---------------------------------------------------------------------------
d["narrative_indicators"].extend([
    {
        "id": "NAR-18",
        "indicator": "Bersatu-PN split TOWARD FORMALIZATION — 'PN has grounds to remove Bersatu, says Kiandee' (NST)",
        "type": "Electoral — coalition fracture (escalation toward procedural expulsion)",
        "severity": "CRITICAL",
        "trend": "DEEPENED toward formalization — 16:33 (mutual on-the-record confrontation, PN info chief floats termination) -> 19:19 (NST, Kiandee: PN 'has grounds' to remove Bersatu). The termination threat acquires concrete 'grounds'.",
        "evidence": "NST: 'PN has grounds to remove Bersatu, says Kiandee'. Per nomination-day-summary-1919: progression 15:09 'could face termination' (Star ticker) -> 16:33 'info chief floats termination' (summary-1633) -> 19:19 'has grounds to remove' (NST, Kiandee). Single highest-priority watch item; escalation trigger #2 (coalition restructuring/realignment) adjacent.",
        "significance": "If PN executes the removal, the opposition restructures MID-CAMPAIGN (trigger #2 fires). This is the closest the cycle has come to a trigger firing. ESC-010/ESC-011 progress from mutual confrontation toward a potential procedural expulsion; new ESC-014 raised. Maximally favourable to the incumbent (PH) — an expelled/contested Bersatu further fragments the opposition vote."
    },
    {
        "id": "NAR-19",
        "indicator": "Zahid bellwether/realignment framing — NS result as determinant of PRN Melaka + PRU16 lineups",
        "type": "Electoral — strategic-stakes elevation (national realignment framing)",
        "severity": "MEDIUM-HIGH",
        "trend": "NEW — BN/UMNO president publicly elevates the NS contest to a determinant of future national coalition restructuring.",
        "evidence": "The Star (JEMPOL): 'New political alignments needed to ensure stability, says Ahmad Zahid'; Astro Awani (~19:14 MYT): 'PRN Negeri Sembilan: Prestasi BN-PN mungkin jadi penentu jajaran baharu PRN Melaka, PRU16 — Ahmad Zahid.'",
        "significance": "Elevates the strategic stakes of the NS contest beyond a single state election — the BN/UMNO president publicly frames NS as a bellwether for national coalition restructuring (Melaka PRN + PRU16 lineups). Rhetorically adjacent to trigger #2 (alliance/realignment). Reinforces BN's 'understanding, not merger' containment (rev 2) while hedging toward post-election realignment. Watch for any concrete BN-PAS or BN-PH accommodation signal."
    },
])
# revision3 refinements to existing indicators
for n in d["narrative_indicators"]:
    if n.get("id") == "NAR-12":
        n["revision3_update"] = (
            "REFINED — the split is now THREE-WAY: Bersatu vs (PN+PAS). Hadi Awang (JEMPOL, NST) "
            "confirms PAS is now the third party in the confrontation (defends PN/PAS, attacks Bersatu). "
            "The 16:33 'mutual Muhyiddin-vs-Samsuri' framing is extended to a Bersatu-vs-(PN+PAS) war. "
            "Cycle 3 escalation: PN 'has grounds to remove Bersatu' (Kiandee, NST) — see NAR-18."
        )
    if n.get("id") == "NAR-16":
        n["revision3_update"] = (
            "CORROBORATED — NST independently confirms the EC's 21 three-cornered + 2 five-way figure: "
            "'N9 polls: Three-cornered contests on the rise, two seats witness five-way fights'. The two "
            "five-way fights are N.10 Nilai and N.33 Sri Tanjung. PIR-04 lifted from 'EC single-source' "
            "to CONFIRMED (EC + NST mainstream). Bersatu's independent posture verified across nearly all seats."
        )

# ---------------------------------------------------------------------------
# 8. Append / update escalation_flags
# ---------------------------------------------------------------------------
def find_flag(d, cid):
    for fl in d["escalation_flags"]:
        if fl.get("id") == cid:
            return fl
    return None

# Update ESC-011
f = find_flag(d, "ESC-011-20260718")
if f:
    f["revision3_update"] = (
        "TOWARD FORMALIZATION — 'PN has grounds to remove Bersatu, says Kiandee' (NST, Cycle 3/19:19). "
        "The mutual confrontation (rev 2) now threatens to formalize into a procedural expulsion during "
        "the campaign window. The termination threat has acquired concrete 'grounds' (progression: "
        "'could face' -> 'info chief floats' -> 'has grounds'). The split is now THREE-WAY: Bersatu vs "
        "(PN+PAS) (Hadi, JEMPOL). Severity remains CRITICAL; the fracture is escalating toward a formal "
        "coalition-restructuring event (trigger #2 adjacent). See new ESC-014."
    )

# Update ESC-010
f = find_flag(d, "ESC-010-20260718")
if f:
    f["revision3_update"] = (
        "TOWARD FORMALIZATION — PN 'has grounds to remove Bersatu' (Kiandee, NST). The chairman-vs-"
        "president rift (rev 2) now carries an actual procedural-expulsion risk. CRITICAL."
    )

# Update ESC-009
f = find_flag(d, "ESC-009-20260718")
if f:
    f["revision3_update"] = (
        "STRATEGIC-STAKES ELEVATION — Zahid (JEMPOL) frames the NS result as a determinant of PRN Melaka "
        "+ PRU16 coalition lineups (Star + Astro Awani). The 'understanding, not merger' containment (rev 2) "
        "is reinforced while BN hedges toward post-election realignment. Watch for concrete accommodation signals."
    )

# New flag ESC-014
d["escalation_flags"].append({
    "id": "ESC-014-20260718",
    "severity": "CRITICAL",
    "category": "PN removal-of-Bersatu threat TOWARD FORMALIZATION — 'has grounds to remove' (Kiandee, NST)",
    "status": "NEW (revision 3)",
    "description": (
        "NST: 'PN has grounds to remove Bersatu, says Kiandee.' The Bersatu-PN termination threat has "
        "progressed from 'could face termination' (15:09, Star ticker) -> 'info chief floats termination' "
        "(16:33, summary-1633) -> 'has grounds to remove' (19:19, NST, Kiandee). This is the strongest "
        "signal yet that ESC-010/ESC-011 may formalize into an actual procedural expulsion during the "
        "campaign window. Per nomination-day-summary-1919: the single highest-priority watch item; "
        "escalation trigger #2 (coalition restructuring/realignment) is adjacent — the closest the cycle "
        "has come to a trigger firing."
    ),
    "action": (
        "Track PN/Bersatu/PAS official channels for any formal removal notice, Bersatu retaliation, or "
        "candidate withdrawals. Determine whether 'has grounds' is (a) rhetorical pressure to force Bersatu "
        "to withdraw candidates or (b) a genuine procedural expulsion in motion. Track Zahid's "
        "'new political alignments' / 'NS determines PRU16' framing for concrete BN-PAS or BN-PH accommodation."
    ),
    "carries_forward": "NEW flag. Escalates ESC-010/ESC-011 toward formalization. Adjacent to trigger #2.",
})

# ---------------------------------------------------------------------------
# 9. Update data_gaps (close none; add forward-looking items)
# ---------------------------------------------------------------------------
gaps = d["data_gaps"]
gaps.append(
    "[19:19Δ FORWARD-LOOKING] A NEWER collection batch is NOT yet extracted: raw-scrape "
    "_130328 batch (7 files: bharian, kosmo, mstar, nst, ohbulan, thestar, utusan) + "
    "nomination-day-summary-2103.md (Cycle 4, 21:03 MYT, 33KB) + 5 manual_*_130328 files "
    "(kerusi-tumpuan, kualapilah, senarai-calon, tangjayson, warlord) arrived 13:04-13:12 UTC, "
    "AFTER the 11:52 entity extraction. These are in raw-scrapes/20260718/ but NOT yet in "
    "processed-entities/20260718/. They are OUT OF SCOPE for this revision-3 sentiment pass "
    "(input = extracted entities). RECOMMENDATION: run ns-entity-extraction-enhanced.py on the "
    "full corpus, then a revision-4 sentiment delta merge to cover the 130328 batch + summary-2103."
)
gaps.append(
    "[19:19Δ CARRIED] 20260716 SENTIMENT GAP DAY remains unbackfilled (1-day gap persists, Day 8)."
)
gaps.append(
    "[19:19Δ CARRIED] ESC-002 — ns-sentiment-analysis.sh remains a stub; agent-manual review is the "
    "standing CVS-compliant method."
)
d["data_gaps"] = gaps

# ---------------------------------------------------------------------------
# 10. Update entities_analyzed + entities_analyzed_by_category
# ---------------------------------------------------------------------------
delta_scored = len(D_POS) + len(D_NEU) + len(D_NEG)  # 1 new scored entry
d["entities_analyzed_delta_1633"] = d.get("entities_analyzed_delta_1633", 13)
d["entities_analyzed_delta_1919"] = delta_scored
d["entities_analyzed"] = d["entities_analyzed"] + delta_scored
d["entities_analyzed_by_category"]["politicians"] = d["entities_analyzed_by_category"].get("politicians", 0) + 1

# ---------------------------------------------------------------------------
# 11. Append delta verdict
# ---------------------------------------------------------------------------
d["verdict"] = (
    d.get("verdict", "").rstrip() + "\n\n"
    "[19:19Δ REVISION 3 — CYCLE 3 DELTA MERGED] The 19:19 MYT collection cycle (raw-scrape "
    "_111951 batch + nomination-day-summary-1919) extends the Nomination-Day verdict along "
    "three axes: (1) The Bersatu-PN split moves TOWARD FORMALIZATION — NST (Kiandee): 'PN has "
    "grounds to remove Bersatu.' The termination threat has acquired concrete 'grounds' "
    "(progression: 'could face' -> 'info chief floats' -> 'has grounds'), making this the "
    "strongest signal yet that ESC-010/ESC-011 may formalize into an actual procedural expulsion "
    "during the campaign window — the single highest-priority watch item, adjacent to trigger "
    "#2. The split is now THREE-WAY: Bersatu vs (PN+PAS) (Hadi, JEMPOL). NEW ESC-014 (CRITICAL) "
    "raised; ESC-010/ESC-011 updated to 'toward formalization'. (2) Zahid Hamidi ELEVATES the NS "
    "strategic stakes to a bellwether/realignment determinant — 'new political alignments needed' "
    "(Star, JEMPOL) + 'PRN NS prestasi BN-PN mungkin jadi penentu jajaran baharu PRN Melaka, PRU16' "
    "(Astro Awani). The NS contest is now publicly framed as a determinant of future national "
    "coalition restructuring (NEW NAR-19). (3) PH's edge gains a MACHINERY/mobilisation dimension "
    "— R. Ramanan (PKR VP, Sungai Buloh MP) deployed to the Wisma MBS nomination centre to back "
    "6 PH candidates (The Star, SEREMBAN), the first concrete nomination-centre mobilisation datum "
    "of the day. PH's edge is now STRUCTURAL + NARRATIVE (rev 2) + MACHINERY (rev 3). NST "
    "independently corroborates the EC's 21 three-cornered + 2 five-way figure (N.10 Nilai, "
    "N.33 Sri Tanjung) — PIR-04 CONFIRMED. No escalation trigger has FIRED, but trigger #2 "
    "(coalition restructuring) is elevated to WATCH (ELEVATED — HIGHEST PRIORITY), the closest "
    "it has been. NET: the PH-favorable tilt STRENGTHENS further; the opposition fracture is "
    "escalating toward a formal mid-campaign restructuring event. Distribution: 11 positive / "
    "9 neutral / 6 negative (revision-3 merged; rev-2 was 10/9/6; baseline 4/4/4). "
    "FORWARD-LOOKING: a newer unextracted batch (_130328 + summary-2103 + 5 manual files, "
    "13:04-13:12 UTC) awaits the next extraction + revision-4 pass."
)

# ---------------------------------------------------------------------------
# 12. Write back + validate
# ---------------------------------------------------------------------------
with open(PATH, "w", encoding="utf-8") as f:
    json.dump(d, f, indent=2, ensure_ascii=False)

# Re-load to confirm valid JSON + print summary
with open(PATH, "r", encoding="utf-8") as f:
    v = json.load(f)
print("JSON VALID:", True)
print("revision_history count:", len(v.get("revision_history", [])))
print("status:", v.get("status"))
print("entities_analyzed:", v.get("entities_analyzed"),
      "(baseline", v.get("entities_analyzed_baseline_0831"),
      "+ rev2 delta", v.get("entities_analyzed_delta_1633"),
      "+ rev3 delta", v.get("entities_analyzed_delta_1919"), ")")
print("sentiment_summary counts: pos", len(v["sentiment_summary"]["positive"]),
      "neu", len(v["sentiment_summary"]["neutral"]),
      "neg", len(v["sentiment_summary"]["negative"]))
print("sentiment_distribution:", v["sentiment_distribution"])
print("narrative_indicators:", len(v["narrative_indicators"]))
print("escalation_flags:", len(v["escalation_flags"]))
print("data_gaps:", len(v["data_gaps"]))
print("source_basis total_source_files:", v["source_basis"].get("total_source_files"))
print("file bytes:", os.path.getsize(PATH))
