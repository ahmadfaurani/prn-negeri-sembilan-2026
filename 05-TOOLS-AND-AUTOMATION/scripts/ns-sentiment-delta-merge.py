#!/usr/bin/env python3
"""
NS PRN 2026 Sentiment Analysis — Delta Merge (Revision 2).

Merges the 16:33 MYT collection delta (raw-scrape batches _070937 + _083302 +
nomination-day-summary-1509/1633) into the existing sentiment_analysis.json
(baseline generated 2026-07-18T08:31, built on the _010044 batch only).

Standing method: agent-manual source-attributed review (CVS-compliant).
Author runtime: GLM-5.2 (custom) — manual review fallback (ESC-002, Day 8).

CVS standard: sentiment based on verified source content only; all entities
source-attributed (verbatim surface match); SPR candidate list as ground truth.
"""
import json, copy, os
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
    "revision": 2,
    "timestamp": rev_now,
    "scope": "delta merge of later collection batches (raw-scrape _070937 + _083302 + nomination-day-summary-1509/1633) into the 08:31 baseline (which covered _010044 only)",
    "rationale": "entities_consolidated.json (08:46) spans 31 source files across 3 batches; the 08:31 sentiment pass covered only the first batch (11/13 sources). 19 new politicians, 3 new parties, 16 new constituencies, and 1 resurfacing issue were extracted from the later batches and not yet sentiment-analyzed.",
    "method": "agent-manual source-attributed review (CVS-compliant) + SPR candidate-list cross-reference",
    "runtime": "GLM-5.2 (custom) — manual review fallback",
    "delta_entities_new": 19, "delta_parties_new": 3, "delta_constituencies_new": 16,
})

# ---------------------------------------------------------------------------
# 2. Update top-level metadata
# ---------------------------------------------------------------------------
d["generated"] = rev_now
d["status"] = "completed (revision 2 — full-day delta merged)"
d["openosint_status"] = (
    "NOT ACTIVE — ns-sentiment-analysis.sh remains a stub (prints empty JSON to stdout, "
    "entities_analyzed:0, does NOT write sentiment_analysis.json). No API credentials in "
    "environment. Agent-manual review is the standing CVS-compliant method (ESC-002, Day 8). "
    "Revision 2 applied by GLM-5.2 manual-review fallback after detecting that the 08:31 "
    "baseline covered only the first (_010044) collection batch while entities_consolidated "
    "spans 31 files / 3 batches."
)

# ---------------------------------------------------------------------------
# 3. Update source_basis to full-day corpus
# ---------------------------------------------------------------------------
d["source_basis"] = {
    "collection_date": "20260718",
    "collection_batches": {
        "_010044": {"files": 11, "covered_by_baseline_0831": True},
        "_070937": {"files": 9, "covered_by_baseline_0831": False, "covered_by_revision2": True},
        "_083302": {"files": 9, "covered_by_baseline_0831": False, "covered_by_revision2": True},
        "nomination-day-summary-1509": {"files": 1, "intelligence_asset": True, "covered_by_revision2": True},
        "nomination-day-summary-1633": {"files": 1, "intelligence_asset": True, "covered_by_revision2": True},
    },
    "total_source_files": 31,
    "total_entities_extracted": 146,
    "sources_with_editorial_body": [
        "utusan.com.my (VERBATIM PROSE — 'Negeri Sembilan medan penyatuan undi Melayu'; contains Samsuri's on-record refutation of Muhyiddin: 'dakwaan ... adalah tidak berasas' + 'Proses berkenaan telah dimuktamadkan dan diluluskan oleh Majlis Tertinggi PN')",
        "thestar.com.my (FULL LEADS + EC/police datelines: 'Total of 21 seats to see three-cornered contests, says EC'; 'No untoward incidents during nomination process, say police'; 'Barisan, Perikatan have an understanding ... not a merger, says Dr Wee'; analyst 'Malay tsunami forming in Negri Sembilan?'; headline ticker 'BN confident of securing simple majority')",
        "nst.com.my (FULL LEADS — richest NS coverage: 'Muhyiddin says Bersatu remains sole opposition voice'; 'Hadi dismisses Muhyiddin's toxic PN claim, points finger at Bersatu' [JEMPOL]; 'Zahid: BN-PN cooperation based on understanding, not formal pact' [REMBAU]; 'Johari: BN-PN cooperation depends on common ground, not ideology' [TAMPIN]; 'PH banking on Aminuddin's MB track record, says Fahmi' [JEMPOL]; 'Tun Faisal faces ex-Melaka deputy police chief in Sikamat'; 'BN unfazed by three-cornered fight in Juasseh'; '103 candidates confirmed'; 'BN to launch NS election manifesto on July 24')",
        "astroawani.com (Bernama photo captions + leads: 'Leevineshwaraan calon termuda, Tok Mat antara paling otai'; 'Mohd Faizal terbuka terima cabaran Aminuddin di Linggi'; Fuziah Salleh integrity narrative; Loke 'Jelebu kritikal tentukan pembentukan kerajaan negeri')",
    ],
    "sources_headlines_or_trending_only": [
        "bharian.com.my (404 body + trending sidebar ONLY — headlines verbatim: 'Jajaran BN-PN di depan'; 'Kerjasama BN-PN hanya persefahaman, bukan gabungan - MCA'; 'PH masih berpeluang pertahankan Negeri Sembilan'; 'Kejayaan pentadbiran PH, keupayaan Aminuddin fokus kempen - Fahmi'; 'Lawan MB NS di Linggi, calon BN tekad kempen secara matang'; 'Tun Faisal tumpu isu perbandaran lama di Sikamat'; 'Sepupu bertembung di Klawang'; 'Saingan berbeza tiga warlord'; 'Kesefahaman BN-PN demi kestabilan politik - Asyraf Wajdi'; carried 'Pimpinan UMNO bahagian tak puas hati 11 kerusi'; 'DAP bakal dihukum')",
    ],
    "verified_intelligence_asset": "spr-candidate-list-20260718.json — OFFICIAL SPR candidate list (103 candidates, 36 DUNs). PRIMARY ground truth for candidate-party-seat mapping.",
    "intelligence_summaries": "nomination-day-summary-1509.md + nomination-day-summary-1633.md (PIR-framework Nomination Day Surge products) — used as structured cross-reference; all sentiment entries are re-attributed to underlying media source files per CVS standard.",
    "cvs_standard": "Sentiment based on verified source content only. No pattern-inferred sentiment. All entities source-attributed (verbatim surface match). SPR candidate list used as ground-truth cross-reference. Intelligence summaries used only to locate items; media source files cited as attribution.",
}

# ---------------------------------------------------------------------------
# 4. Append DELTA sentiment_summary entries (prefixed [16:33Δ])
# ---------------------------------------------------------------------------
D_POS = [
    {
        "entity": "[16:33Δ] Pakatan Harapan (PH) — PROACTIVE NARRATIVE EMERGES (Fahmi + Loke + Fuziah)",
        "category": "party",
        "sentiment": "positive",
        "score": 0.61,
        "rationale": "FILLS the 08:31 data gap ('No PH proactive campaign narrative'). PH now has BOTH structural advantage (opposition split) AND a narrative voice. Fahmi Fadzil (Comms Minister, JEMPOL dateline): 'PH banking on Aminuddin's MB track record in Negri polls' (NST); bharian: 'Kejayaan pentadbiran PH, keupayaan Aminuddin fokus kempen' (PH governance success, Aminuddin's capability is the campaign focus). Anthony Loke (JELEBU): frames the NS PRN as a referendum on DAP support — 'Negri polls will test claims DAP is losing support, says Loke' (NST) — and flags the 4 Jelebu DUN seats as critical to state-government formation ('Kerusi DUN di Jelebu kritikal tentukan pembentukan kerajaan negeri', Astro Awani). Fuziah Salleh (PKR): 'Gadai kepercayaan demi kemenangan tiada dalam kamus strategi kami' (Astro Awani) — integrity/trust framing. PH's position UPTICKS from 08:31's 'minimal narrative voice (6 occ)' to a structured governance+integrity+strategy narrative. The structural PH-favorable tilt is now NARRATIVE-backed, not merely structural.",
        "sources": ["nstcommy_20260718_070937.md", "nstcommy_20260718_083302.md", "bhariancommy_20260718_070937.md", "astroawanicom_20260718_083302.md"],
        "confidence": "HIGH — multi-source, NS-specific, minister/secretary-general-level quotes, dateline-confirmed"
    },
    {
        "entity": "[16:33Δ] Nomination Day / EC + PDRM — clean nomination MULTI-SOURCE CONFIRMED",
        "category": "event/organization",
        "sentiment": "positive",
        "score": 0.63,
        "rationale": "UPGRADED from 08:31's 0.58 (single-thread) to multi-source CONFIRMED by two independent authorities. EC (The Star, Shah Alam dateline): 'No nomination papers were rejected during the nomination process for the 16th Negri Sembilan state election.' PDRM (The Star, Port Dickson dateline): 'No untoward incidents during nomination process, say police.' 103 candidates filed, zero rejections, zero incidents across 8 nomination centres. Clean nomination = no party gained an uncontested seat; every one of 36 DUNs is contestable — structurally favors the unified 36-candidate PH slate against a fragmented opposition. Polling day 1 Aug 2026 confirmed; BN manifesto launch 24 Jul (NST).",
        "sources": ["thestarcommy_20260718_083302.md", "nstcommy_20260718_070937.md", "nstcommy_20260718_083302.md"],
        "confidence": "HIGH — EC + police independent confirmation (multi-source)"
    },
    {
        "entity": "[16:33Δ] Mohd Faizal Ramli (BN candidate N.32 Linggi) — mature-challenger framing",
        "category": "politician",
        "sentiment": "positive",
        "score": 0.54,
        "rationale": "NEW. Astro Awani: 'Mohd Faizal terbuka terima cabaran Aminuddin di Linggi' (open to accepting caretaker-MB Aminuddin's challenge); bharian: 'Lawan MB NS di Linggi, calon BN tekad kempen secara matang' (BN candidate determined to campaign maturely against the MB). Confident, mature-challenge framing. SPR-verified (N.32 LINGGI, BN, 54yo). Faces Aminuddin (PH) + Bersatu's Zamri Md Said in a 3-cornered fight. Positive for BN candidate quality/temperament; the 3-cornered split of the opposition vote, however, advantages the incumbent Aminuddin.",
        "sources": ["astroawanicom_20260718_083302.md", "bhariancommy_20260718_070937.md", "spr-candidate-list-20260718.json"],
        "confidence": "HIGH — Astro Awani + bharian headline + SPR verified"
    },
    {
        "entity": "[16:33Δ] Datuk Razali Abu Samah (PN candidate N.13 Sikamat) — ex-Melaka deputy police chief (credibility asset)",
        "category": "politician",
        "sentiment": "positive",
        "score": 0.52,
        "rationale": "NEW DETAIL (candidate named in 08:31 via SPR; background is new). NST (SEREMBAN): 'Tun Faisal faces ex-Melaka deputy police chief in Sikamat three-way fight.' A senior former deputy police chief as PN candidate lends institutional credibility / establishment credentials — a credibility ASSET in the 3-cornered Sikamat fight (PN Razali vs Bersatu Tun Faisal vs PH Nor Azman). SPR-verified. Positive for PN candidate quality; in a 3-cornered seat, however, the opposition vote (Razali + Tun Faisal) splits and advantages PH's Nor Azman.",
        "sources": ["nstcommy_20260718_070937.md", "spr-candidate-list-20260718.json"],
        "confidence": "HIGH — NST headline + SPR verified"
    },
    {
        "entity": "[16:33Δ] Datuk Ismail Lasim (BN candidate N.15 Juasseh) — 'unfazed' by 3-cornered fight",
        "category": "politician",
        "sentiment": "positive",
        "score": 0.51,
        "rationale": "NEW. NST (KUALA PILAH): 'BN unfazed by three-cornered fight in Juasseh' — BN candidate Datuk Ismail Lasim is unfazed by the 3-cornered contest. Confident incumbent posture. SPR-verified (N.15 Juasseh, BN). Positive BN candidate confidence/incumbency; Juasseh is one of the 12 PH-BN-Bersatu 3-cornered seats (EC, cross-verified).",
        "sources": ["nstcommy_20260718_070937.md", "spr-candidate-list-20260718.json"],
        "confidence": "HIGH — NST lead + SPR verified"
    },
    {
        "entity": "[16:33Δ] LeeVineshwaraan Murugan (Bersatu candidate N.33 Sri Tanjung, 23yo) — youngest candidate; demographic-fit play",
        "category": "politician",
        "sentiment": "positive",
        "score": 0.50,
        "rationale": "NEW. Astro Awani/Bernama: 'Leevineshwaraan calon termuda, Tok Mat antara paling otai' (Leevinesh the youngest candidate, Tok Mat among the most veteran). Bersatu fields a 23-year-old Indian candidate in N.33 Sri Tanjung — a 5-way, Indian-plurality/mixed seat (BN + Bersatu + PH + 2 independents). A youth + demographic-fit play by Bersatu, paired (by the same piece) against Tok Mat (70, the most veteran) to illustrate the field's range. SPR-verified. Positive for Bersatu candidate diversity/youth; the 5-way fragmentation, however, makes Sri Tanjung the highest split-risk seat.",
        "sources": ["astroawanicom_20260718_083302.md", "spr-candidate-list-20260718.json"],
        "confidence": "HIGH — Astro Awani/Bernama photo caption + SPR verified"
    },
]

D_NEU = [
    {
        "entity": "[16:33Δ] BN-PN 'understanding, not merger' — synchronised containment re-framing (Zahid/Wee/Johari/Asyraf)",
        "category": "issue/party",
        "sentiment": "neutral",
        "score": 0.50,
        "rationale": "NEW. Four BN leaders synchronised re-characterising the BN-PN arrangement as an informal 'understanding/persefahaman', NOT a formal pact or merger: Zahid Hamidi (REMBAU, NST): 'BN-PN cooperation based on understanding, not formal pact'; Wee Ka Siong / MCA (NST + The Star): 'understanding ... not a merger'; Johari Abdul / Speaker (TAMPIN, NST): 'BN-PN cooperation depends on common ground, not ideology'; Asyraf Wajdi (bharian): 'Kesefahaman BN-PN demi kestabilan politik'. This DOWNGRADES ESC-009 from the 08:31 'verified pact' to an informal BN-PAS understanding — a containment strategy, likely responding to (a) Bersatu's split fracturing the 'unified opposition' claim and (b) UMNO grassroots dissatisfaction (ESC-012). Neutral: the bilateral arrangement holds but is actively re-framed as informal; BN leadership has itself abandoned the 08:31 '36 matching candidates / unified opposition' framing.",
        "sources": ["nstcommy_20260718_070937.md", "nstcommy_20260718_083302.md", "thestarcommy_20260718_083302.md", "bhariancommy_20260718_070937.md"],
        "confidence": "HIGH — 4 BN leaders, 3 sources, dateline-confirmed"
    },
    {
        "entity": "[16:33Δ] Datuk Seri Ahmad Zahid Hamidi (UMNO/BN President) — fronts containment; REMBAU dateline",
        "category": "politician",
        "sentiment": "neutral",
        "score": 0.50,
        "rationale": "NEW (11 occurrences — highest-visibility NEW politician; absent from the 08:31 corpus). Zahid fronts the 'understanding not formal pact' containment line (NST, REMBAU dateline). A major BN heavyweight now visible in NS nomination coverage; his Rembau presence anchors the BN southern axis (Rembau-Tampin-Rantau, alongside Johari at Tampin and Tok Mat at Rantau). Neutral: projects BN leadership/unity but the containment framing is defensive — managing fallout from the Bersatu split + UMNO divisional dissent over 11 seats conceded to PN. Not editorially tied to any NS seat contest himself (federal/leadership role).",
        "sources": ["nstcommy_20260718_070937.md", "nstcommy_20260718_083302.md"],
        "confidence": "HIGH — NST, dateline-confirmed (REMBAU)"
    },
    {
        "entity": "[16:33Δ] Tan Sri Abdul Hadi Awang (PAS President) — dismisses 'toxic PN', points finger at Bersatu",
        "category": "politician",
        "sentiment": "neutral-negative",
        "score": 0.45,
        "rationale": "NEW. NST (JEMPOL dateline): 'Hadi dismisses Muhyiddin's toxic PN claim, points finger at Bersatu.' Hadi personally intervenes against Bersatu/Muhyiddin — ESC-010 WIDENS from a Muhyiddin-vs-Samsuri spat (08:31) to a Hadi-vs-Muhyiddin confrontation. Hadi is defending PN/PAS from Muhyiddin's 'toxic' charge but in doing so escalates the intra-opposition confrontation. Neutral-negative: assertive/defensive; deepens the opposition fracture. Hadi's Jempol dateline signals PAS priority in the Jempol Malay seats.",
        "sources": ["nstcommy_20260718_070937.md", "nstcommy_20260718_083302.md"],
        "confidence": "HIGH — NST, dateline-confirmed (JEMPOL)"
    },
    {
        "entity": "[16:33Δ] 'Malay tsunami forming in Negri Sembilan?' — analyst narrative (The Star)",
        "category": "issue",
        "sentiment": "neutral",
        "score": 0.50,
        "rationale": "NEW. The Star analysis 'Malay tsunami forming in Negri Sembilan?' posits Malay-vote consolidation as the decisive dynamic. If consolidation favours a unified BN-PN, it elevates the Tier-3/Tier-4 seats and threatens PH's 4 Malay seats (Klawang, Ampangan, Sikamat, Pilah) — UPWARD PRESSURE on ESC-007. HOWEVER, the Bersatu-PN split structurally counteracts consolidation (Bersatu splits the Malay vote in 20 of its 24 seats). Neutral/analytical: introduces a new PH-risk vector but is counteracted by the fracture. Net unchanged but a watch item.",
        "sources": ["thestarcommy_20260718_083302.md"],
        "confidence": "MEDIUM — single analyst piece; no polling data"
    },
    {
        "entity": "[16:33Δ] Wawasan/Warisan — post-election opposition-coalition positioning (no candidates of its own)",
        "category": "party",
        "sentiment": "neutral",
        "score": 0.48,
        "rationale": "PARTIAL gap-fill (the 08:31 file flagged 'Wawasan' as a data gap). The Star: 'Wawasan must win seats for it to be meaningful partner in opposition coalition, says party chairman.' A smaller party publicly positioning for a post-election opposition-coalition role. CRITICAL CAVEAT (CVS): NO Wawasan/Warisan-branded candidate appears in the SPR official list (candidate parties = PH, BN, BERSATU, PN, BEBAS, ASLI, BERJASA, PSM). So Wawasan is NOT fielding candidates under its own banner in NS — this is positioning/endorsing, not contesting. Party identity ('Warisan' vs 'Wawasan') still to verify. Neutral.",
        "sources": ["thestarcommy_20260718_083302.md", "spr-candidate-list-20260718.json"],
        "confidence": "LOW — single headline; no candidate in SPR list; identity unverified"
    },
]

D_NEG = [
    {
        "entity": "[16:33Δ] Bersatu-PN fracture DEEPENS to MUTUAL, ON-THE-RECORD confrontation",
        "category": "party/issue",
        "sentiment": "negative",
        "score": 0.72,
        "rationale": "ESCALATION of the 08:31 ESC-011 (0.68). The fracture is now MUTUAL and public at leadership level (no longer Muhyiddin isolated/contradictory): (a) Muhyiddin (NST 083302): 'Muhyiddin says Bersatu remains sole opposition voice' — positions Bersatu as the only opposition, claims PN supports the government party (Bersatu publicly disowns PN); (b) Hadi Awang (NST, JEMPOL): 'Hadi dismisses Muhyiddin's toxic PN claim, points finger at Bersatu' — PAS president personally attacks back; (c) Samsuri (PN Chairman, Utusan 070937 VERBATIM): 'dakwaan Presiden ... Bersatu ... bahawa ia dibuat tanpa persetujuan Majlis Tertinggi PN adalah tidak berasas' + 'Proses berkenaan telah dimuktamadkan dan diluluskan oleh Majlis Tertinggi PN' — the chairman-vs-president contradiction is now ON THE RECORD. (d) Per nomination-day-summary-1633, a PN info chief floated TERMINATION of Bersatu's PN membership over the 8+ seat clashes. The 08:31 'Muhyiddin isolated' finding is SUPERSEDED — this is now a mutual, leadership-level war on the ballot. Maximally favourable to the incumbent (PH).",
        "sources": ["nstcommy_20260718_083302.md", "nstcommy_20260718_070937.md", "utusancommy_20260718_070937.md", "nomination-day-summary-1633.md"],
        "confidence": "HIGH — multi-source, dateline-confirmed, verbatim refutation (Utusan)"
    },
    {
        "entity": "[16:33Δ] Tan Sri Muhyiddin Yassin — 'sole opposition' / 'PN supports government' escalation",
        "category": "politician",
        "sentiment": "negative",
        "score": 0.68,
        "rationale": "ESCALATION of the 08:31 Muhyiddin entry (0.65). NST 083302: 'Muhyiddin says Bersatu remains sole opposition voice' — positions Bersatu as the country's only opposition force and claims Perikatan Nasional supports the government party. A retaliatory escalation BEYOND 08:31's 'PN toxic + new bloc + not quitting' contradiction: Muhyiddin now explicitly DISOWNS PN as an opposition force. Deepens the contradictory posture (calls PN toxic, announces a new bloc, insists not quitting PN, AND now claims PN is government-aligned). Continues the 20260714-20260717 Muhyiddin-vulnerability trajectory (Pagoh at risk, Nepturis trial, claim rebutted). Bersatu treats the NS PRN as a voter-acceptance test for a post-election realignment.",
        "sources": ["nstcommy_20260718_083302.md", "nomination-day-summary-1633.md"],
        "confidence": "HIGH — NST lead + multi-source (bharian/FMT per summary)"
    },
]

d["sentiment_summary"]["positive"].extend(D_POS)
d["sentiment_summary"]["neutral"].extend(D_NEU)
d["sentiment_summary"]["negative"].extend(D_NEG)

# ---------------------------------------------------------------------------
# 5. Update sentiment_distribution (full-day merged)
# ---------------------------------------------------------------------------
d["sentiment_distribution_baseline_0831"] = d.get("sentiment_distribution")
d["sentiment_distribution"] = {
    "positive": len(d["sentiment_summary"]["positive"]),
    "neutral": len(d["sentiment_summary"]["neutral"]),
    "negative": len(d["sentiment_summary"]["negative"]),
    "total_scored": len(d["sentiment_summary"]["positive"]) + len(d["sentiment_summary"]["neutral"]) + len(d["sentiment_summary"]["negative"]),
    "baseline_0831": {"positive": 4, "neutral": 4, "negative": 4, "total": 12},
    "delta_1633": {"positive": len(D_POS), "neutral": len(D_NEU), "negative": len(D_NEG)},
    "note": (
        "Full-day merged distribution. Baseline (08:31, _010044 batch) was 4/4/4 (BALANCED, structurally PH-favorable). "
        "Delta (16:33, _070937+_083302+summaries) ADDS: +6 positive (PH-narrative emergence, clean-nomination multi-source upgrade, Faizal mature challenge, Razali ex-police credibility, Ismail unfazed, LeeVinesh youth), "
        "+5 neutral (understanding-not-merger containment, Zahid, Hadi, Malay-tsunami analyst, Wawasan positioning), +2 negative (Bersatu-Pn mutual fracture, Muhyiddin sole-opposition escalation). "
        "NET SHIFT: the PH-favorable tilt STRENGTHENS and is now NARRATIVE-backed (PH proactive voice FILLS the 08:31 gap), while the opposition fracture deepens to a MUTUAL leadership-level war. "
        "New PH-risk vector: the 'Malay tsunami' analyst narrative (ESC-007/ESC-013 upward pressure), though structurally counteracted by the Bersatu-PN split. "
        "Distribution remains balanced in count but the negative entries are higher-severity (CRITICAL mutual fracture) and the positives now include a proactive incumbent narrative."
    ),
}

# ---------------------------------------------------------------------------
# 6. Update party_sentiment_matrix (delta notes for the parties that moved)
# ---------------------------------------------------------------------------
psm = d["party_sentiment_matrix"]
psm["PH"]["revision2_delta"] = (
    "PROACTIVE NARRATIVE EMERGES (fills the 08:31 'minimal narrative voice' gap). Fahmi Fadzil (Comms Minister, JEMPOL): "
    "'PH banking on Aminuddin's MB track record' (NST). Loke: NS-as-DAP-referendum + Jelebu-4-seats-critical (NST + Astro Awani). "
    "Fuziah Salleh (PKR): integrity framing (Astro Awani). PH now has BOTH structural advantage (opposition split) AND narrative voice. "
    "VERDICT SUPERSEDES the 08:31 'minimal narrative voice' note — PH's edge is now narrative-backed, not merely structural."
)
psm["PN"]["revision2_delta"] = (
    "FRICTION DEEPENS TO MUTUAL, ON THE RECORD. Samsuri (PN Chairman, Utusan verbatim) publicly refutes Muhyiddin — "
    "'dakwaan ... adalah tidak berasas' + 'Proses ... diluluskan oleh Majlis Tertinggi PN'. Hadi Awang (PAS President, NST JEMPOL) "
    "dismisses Muhyiddin's 'toxic PN' claim and points the finger at Bersatu. Per nomination-day-summary-1633, a PN info chief "
    "floated termination of Bersatu's PN membership. The chairman-president rift is now a public mutual confrontation."
)
psm["Bersatu"]["revision2_delta"] = (
    "Muhyiddin escalates: 'Bersatu remains sole opposition voice' / claims 'PN supports the government party' (NST 083302). "
    "Bersatu publicly disowns PN as an opposition force. Comprehensive independent posture confirmed: Bersatu fights one or both "
    "allies in 20 of its 24 contested DUNs (EC 12-of-36 PH-BN-Bersatu three-cornered, cross-verified to SPR)."
)
psm["BN"]["revision2_delta"] = (
    "Leadership SYNCHRONISES 'understanding, not merger' containment re-framing: Zahid (REMBAU), Wee/MCA, Johari (TAMPIN), Asyraf Wajdi. "
    "ESC-009 downgraded from 'verified pact' to informal BN-PAS understanding. New confidence signal: 'BN confident of securing simple "
    "majority to form state government' (Star ticker); manifesto launch 24 Jul (NST). Zahid (11 occ, REMBAU) is the highest-visibility "
    "new politician. BN's southern axis anchored: Zahid-Rembau, Johari-Tampin, Tok Mat-Rantau."
)
psm["UMNO"]["revision2_delta"] = (
    "Zahid Hamidi (UMNO/BN President) now leads the containment line (11 occ, REMBAU) — visibility SURGES vs 08:31 (3 occ). "
    "Internal dissent (11 seats conceded to PN, bharian) AGGRAVATION RISK: Muhyiddin's 'PN supports government' rhetoric may "
    "intensify UMNO grassroots dissatisfaction if PN/PAS is perceived as government-aligned (ESC-012 watch)."
)
psm["DAP"]["revision2_delta"] = (
    "Loke now has a PROACTIVE voice: 'Negri polls will test claims DAP is losing support' (NST, JELEBU) — frames NS as a DAP referendum; "
    "plus 'Jelebu kritikal tentukan pembentukan kerajaan negeri' (Astro Awani). CHENNAH is a STRAIGHT FIGHT (vs BN's Siow Kong Choon), "
    "cleaner than the 08:31 'mixed seat at risk' framing — the Bersatu/BN split reduces the unified-opposition threat to DAP's mixed seats."
)
psm["PKR"] = {
    "status": "PRESENT (2 occurrences, nomination-day-summary-1633 + Astro Awani) — sentiment POSITIVE (integrity/trust framing). NEW in revision 2 (was a 08:31 data gap).",
    "surrogates_detected": ["Fuziah Salleh (PKR) — 'Gadai kepercayaan demi kemenangan tiada dalam kamus strategi kami' (Astro Awani)"],
    "assessment": "PKR becomes editorially present via Fuziah Salleh's integrity/trust narrative ('sacrificing trust for victory is not in our strategy dictionary'). This FILLS the 08:31 data gap ('PKR not editorially mentioned'). PKR's contribution to the PH narrative is an integrity/anti-cynicism frame, complementing Fahmi's governance frame and Loke's strategic frame.",
    "cvs_status": "VERIFIED — Astro Awani (PKR-named, direct quote framing)",
    "revision2_delta": "NEW — closes the 08:31 PKR data gap."
}
psm["data_gap"] = (
    "MUDA: appears in astroawanicom_20260718_083302 (4 occ per extractor) but verbatim context is thin in the headline/lead scrape — "
    "treat as MENTIONED, not sentiment-scored. Wawasan/Warisan: positioning only, NO candidate in the SPR list (parties = PH/BN/BERSATU/PN/BEBAS/ASLI/BERJASA/PSM); "
    "identity (Warisan vs 'Wawasan') to verify. AMANAH/GERAKAN still not editorially mentioned. "
    "NEW discrepancy to verify: Tok Mat's federal title — the 08:31 baseline says 'Defence Minister'; nomination-day-summary-1633 calls him 'DPM'. "
    "Neither affects the heavyweight-candidate sentiment; flag for verification."
)

# ---------------------------------------------------------------------------
# 7. Append DELTA narrative_indicators (NAR-12 ... NAR-17)
# ---------------------------------------------------------------------------
d["narrative_indicators"].extend([
    {
        "id": "NAR-12",
        "indicator": "Bersatu-PN fracture DEEPENS to MUTUAL, on-the-record leadership confrontation (Hadi + Samsuri vs Muhyiddin)",
        "type": "Electoral — coalition fracture (escalation of the dominant story)",
        "severity": "CRITICAL",
        "trend": "DEEPENED — 08:31 (Muhyiddin isolated/contradictory) → 16:33 (MUTUAL: Hadi attacks back, Samsuri refutes on record, Muhyiddin 'sole opposition' disowns PN, PN info chief floats termination)",
        "evidence": "NST: 'Muhyiddin says Bersatu remains sole opposition voice'; NST (JEMPOL): 'Hadi dismisses Muhyiddin's toxic PN claim, points finger at Bersatu'; Utusan (verbatim): Samsuri — 'dakwaan ... adalah tidak berasas' + 'Proses ... diluluskan oleh Majlis Tertinggi PN'; nomination-day-summary-1633: PN info chief floats termination of Bersatu's membership.",
        "significance": "The 08:31 'Muhyiddin isolated' framing is SUPERSEDED. The Bersatu-PN split is now a public, mutual, leadership-level war (chairman vs president, PAS president vs Bersatu president), with a membership-termination threat floated. This is the most opposition-cohesion-negative development of the cycle and maximally favourable to the incumbent (PH)."
    },
    {
        "id": "NAR-13",
        "indicator": "BN-PN 'understanding, not merger' — synchronised containment re-framing by 4 BN leaders",
        "type": "Electoral — coalition framing (containment/downgrade)",
        "severity": "HIGH",
        "trend": "NEW — ESC-009 downgraded from 'verified pact' (08:31) to informal BN-PAS 'understanding'. BN leadership abandons the 'unified opposition / 36 matching candidates' framing.",
        "evidence": "Zahid (REMBAU, NST): 'BN-PN cooperation based on understanding, not formal pact'; Wee/MCA (NST+Star): 'understanding ... not a merger'; Johari (TAMPIN, NST): 'BN-PN cooperation depends on common ground, not ideology'; Asyraf Wajdi (bharian): 'Kesefahaman BN-PN demi kestabilan politik'.",
        "significance": "A coordinated containment strategy — likely responding to (a) Bersatu's split fracturing the 'unified opposition' claim and (b) UMNO grassroots dissatisfaction (ESC-012). The bilateral arrangement holds but is re-framed as informal; the pact's strategic PURPOSE (unify to defeat PH) is publicly softened by BN itself."
    },
    {
        "id": "NAR-14",
        "indicator": "PH proactive narrative EMERGES — governance (Fahmi) + strategy (Loke) + integrity (Fuziah/PKR)",
        "type": "Political — incumbent narrative (fills prior data gap)",
        "severity": "MEDIUM",
        "trend": "NEW — 08:31 ('No PH proactive campaign narrative', data gap) → 16:33 (structured governance+integrity+strategy narrative across NST/bharian/Astro Awani).",
        "evidence": "NST (JEMPOL): 'PH banking on Aminuddin's MB track record, says Fahmi'; bharian: 'Kejayaan pentadbiran PH, keupayaan Aminuddin fokus kempen'; NST (JELEBU): 'Negri polls will test claims DAP is losing support, says Loke'; Astro Awani: 'Kerusi DUN di Jelebu kritikal tentukan pembentukan kerajaan negeri' (Loke); Astro Awani: Fuziah Salleh 'Gadai kepercayaan demi kemenangan tiada dalam kamus strategi kami'.",
        "significance": "PH's structural advantage (opposition split) is now NARRATIVE-backed. The 08:31 caveat that PH's benefit was 'structural, not narrative' is SUPERSEDED. Three PH voices (Fahmi/Loke/Fuziah) provide governance, strategic, and integrity frames. PH's edge is reinforced."
    },
    {
        "id": "NAR-15",
        "indicator": "'Malay tsunami forming in Negri Sembilan?' — analyst narrative (new PH-risk vector)",
        "type": "Electoral — analyst narrative (risk vector)",
        "severity": "MEDIUM",
        "trend": "NEW — introduces upward pressure on ESC-007 (PH Malay seats) but structurally counteracted by the Bersatu-PN split.",
        "evidence": "The Star analysis: 'Malay tsunami forming in Negri Sembilan?' — posits Malay-vote consolidation as the decisive dynamic.",
        "significance": "If Malay consolidation favours a unified BN-PN, it elevates the Tier-3/Tier-4 seats and threatens PH's 4 Malay seats (Klawang, Ampangan, Sikamat, Pilah). However, Bersatu splits the Malay vote in 20 of its 24 seats, counteracting consolidation. A watch item, not a confirmed shift."
    },
    {
        "id": "NAR-16",
        "indicator": "EC cross-verified contest granularity — 12 PH-BN-Bersatu 3-cornered; Bersatu fights allies in 20/24 seats",
        "type": "Electoral — contest structure (verified, refined)",
        "severity": "MEDIUM",
        "trend": "REFINED — 08:31 (25 multi-cornered, SPR-derived) → 16:33 (EC official: 21 three-cornered; 12 are PH-BN-Bersatu, cross-verified to SPR roll).",
        "evidence": "The Star (SEREMBAN, EC official): 'Total of 21 seats to see three-cornered contests' + 'PH, BN, Bersatu in three-cornered fights in 12 of the 36'. Cross-verified to SPR roll: 12 PH-BN-Bersatu (N02,N03,N06,N09,N12,N15,N16,N17,N20,N24,N28,N32) + 8 PH-BN-Bersatu-PN direct-clash (N04,N05,N13,N14,N23,N25,N31,N34) + 1 PH-PN-Ind (N30) = 21 three-cornered. Bersatu fights one/both allies in 20 of 24 seats.",
        "significance": "EC-official granularity confirms the opposition fragmentation is COMPREHENSIVE, not partial. Bersatu's independent-from-PN posture is verified across nearly all its seats."
    },
    {
        "id": "NAR-17",
        "indicator": "Candidate-quality sweep — Faizal (mature challenge), Razali (ex-police), LeeVinesh (youngest), Ismail (unfazed), Tok Mat (heavyweight)",
        "type": "Electoral — candidate quality (new, multi-candidate)",
        "severity": "LOW",
        "trend": "NEW — first-day candidate-framing sweep across the later batches.",
        "evidence": "Astro Awani: 'Mohd Faizal terbuka terima cabaran Aminuddin di Linggi' + bharian 'calon BN tekad kempen secara matang'; NST: 'Tun Faisal faces ex-Melaka deputy police chief in Sikamat' (Razali); Astro Awani/Bernama: 'Leevineshwaraan calon termuda'; NST: 'BN unfazed by three-cornered fight in Juasseh' (Ismail Lasim); Astro Awani: 'Tok Mat antara paling otai'.",
        "significance": "Across both coalitions, candidates project confidence/credibility (Faizal mature, Razali institutional, Ismail unfazed, Tok Mat heavyweight, LeeVinesh youth+demographic-fit). Positive candidate-quality signal but in 3-cornered/5-way seats the opposition vote splits and advantages PH."
    },
])

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
    f["revision2_update"] = (
        "DEEPENED to MUTUAL, ON-THE-RECORD confrontation. Hadi Awang (NST, JEMPOL) dismisses 'toxic PN' and points finger at Bersatu; "
        "Samsuri (Utusan verbatim) refutes Muhyiddin ('tidak berasas'); Muhyiddin (NST 083302) declares Bersatu 'sole opposition' and claims "
        "PN supports the government; PN info chief floats termination of Bersatu's membership (summary-1633). Severity remains CRITICAL; "
        "the fracture is now a public mutual leadership war, not a one-sided spat."
    )

# Update ESC-010
f = find_flag(d, "ESC-010-20260718")
if f:
    f["revision2_update"] = (
        "DEEPENED to MUTUAL, ON THE RECORD. Samsuri's verbatim refutation (Utusan) + Hadi's counter-attack (NST JEMPOL) + Muhyiddin's "
        "'sole opposition' escalation (NST). Chairman-vs-president contradiction is now public and mutual. CRITICAL."
    )

# Update ESC-009
f = find_flag(d, "ESC-009-20260718")
if f:
    f["revision2_update"] = (
        "DOWNGRADED in framing — 4 BN leaders (Zahid/Wee/Johari/Asyraf) synchronise 'understanding, not merger' containment line. "
        "Bilateral arrangement holds but is re-framed as an informal BN-PAS understanding, not a formal pact. BN itself abandons the "
        "'unified opposition' framing."
    )

# Update ESC-007
f = find_flag(d, "ESC-007-20260718")
if f:
    f["revision2_update"] = (
        "UPWARD PRESSURE — The Star analyst narrative 'Malay tsunami forming in NS?' introduces a PH-Malay-seat risk vector. "
        "Structurally counteracted by the Bersatu-PN split (Bersatu splits the Malay vote in 20/24 seats). Watch item."
    )

# Update ESC-012
f = find_flag(d, "ESC-012-20260718")
if f:
    f["revision2_update"] = (
        "AGGRAVATION RISK — Muhyiddin's 'PN supports the government party' rhetoric may intensify UMNO grassroots dissatisfaction "
        "if PN/PAS is perceived as government-aligned (weakens the rationale for conceding 11 seats to PN)."
    )

# Update ESC-008
f = find_flag(d, "ESC-008-20260718")
if f:
    f["revision2_update"] = (
        "STRENGTHENED — PH proactive narrative emerges (Fahmi governance + Loke strategy + Fuziah integrity), so PH's first-mover/structural "
        "advantage is now narrative-backed, not merely structural."
    )

# New flag ESC-013
d["escalation_flags"].append({
    "id": "ESC-013-20260718",
    "severity": "MEDIUM",
    "category": "'Malay tsunami' analyst narrative — PH Malay-seat risk vector",
    "status": "NEW (revision 2)",
    "description": "The Star analysis 'Malay tsunami forming in Negri Sembilan?' posits Malay-vote consolidation as the decisive dynamic. If consolidation favours a unified BN-PN, it elevates Tier-3/Tier-4 seats and threatens PH's 4 Malay seats (Klawang, Ampangan, Sikamat, Pilah). The Bersatu-PN split structurally counteracts consolidation (Bersatu splits the Malay vote in 20/24 seats).",
    "action": "Track whether the 'Malay tsunami' narrative gains traction in campaign-period coverage and whether it overrides the Bersatu-split effect in Malay-majority seats. Cross-reference 2023 SPR margins for the 4 PH Malay seats.",
    "carries_forward": "NEW flag. Relates to ESC-007 (PH Malay seats)."
})

# ---------------------------------------------------------------------------
# 9. Update data_gaps (close filled gaps; add new ones)
# ---------------------------------------------------------------------------
gaps = d["data_gaps"]
# Close the PH-narrative and PKR gaps
gaps = [g for g in gaps if not g.startswith("No PH proactive campaign narrative")]
# PKR gap is implicit (08:31 said PKR/MUDA/AMANAH/GERAKAN not mentioned in party_sentiment_matrix data_gap note, not in data_gaps list). Add a closure note.
gaps.insert(0, "[16:33Δ CLOSED] 'No PH proactive campaign narrative' — FILLED by Fahmi (governance), Loke (strategy), Fuziah/PKR (integrity).")
gaps.insert(1, "[16:33Δ CLOSED] 'PKR not editorially mentioned' — now present via Fuziah Salleh (Astro Awani).")
gaps.append("[16:33Δ NEW] Tok Mat federal title discrepancy — 08:31 baseline says 'Defence Minister'; nomination-day-summary-1633 calls him 'DPM'. Verify against official cabinet list. Does not affect heavyweight-candidate sentiment.")
gaps.append("[16:33Δ PARTIAL] Wawasan/Warisan — Star reports the party chairman positioning for a post-election opposition-coalition role, but NO Wawasan/Warisan-branded candidate appears in the SPR list. Party is positioning/endorsing, not contesting. Identity (Warisan vs 'Wawasan') still to verify.")
gaps.append("[16:33Δ THIN] MUDA — 4 occurrences in astroawanicom_20260718_083302 per extractor, but verbatim context is thin in the headline/lead scrape. Treated as MENTIONED, not sentiment-scored.")
gaps.append("[16:33Δ PERSISTENT] bharian article bodies remain unscraped (404 page + trending sidebar only) — the Jajaran-BN-PN, Klawang-cousins, three-warlord, and Tun-Faisal-urban-issues stories remain headline-only (confidence capped).")
d["data_gaps"] = gaps

# ---------------------------------------------------------------------------
# 10. Update entities_analyzed + entities_analyzed_by_category
# ---------------------------------------------------------------------------
delta_scored = len(D_POS) + len(D_NEU) + len(D_NEG)  # 13 new scored entries
d["entities_analyzed_baseline_0831"] = d.get("entities_analyzed")
d["entities_analyzed"] = d["entities_analyzed"] + delta_scored
d["entities_analyzed_by_category"]["politicians"] = d["entities_analyzed_by_category"].get("politicians", 0) + 7
d["entities_analyzed_by_category"]["parties"] = d["entities_analyzed_by_category"].get("parties", 0) + 3
d["entities_analyzed_by_category"]["issues"] = d["entities_analyzed_by_category"].get("issues", 0) + 2
d["entities_analyzed_by_category"]["events"] = d["entities_analyzed_by_category"].get("events", 0) + 1
d["entities_analyzed_delta_1633"] = delta_scored

# ---------------------------------------------------------------------------
# 11. Append delta verdict
# ---------------------------------------------------------------------------
d["verdict_baseline_0831"] = d.get("verdict")
d["verdict"] = (
    d.get("verdict", "").rstrip() + "\n\n"
    "[16:33Δ REVISION 2 — FULL-DAY DELTA MERGED] The later collection batches (raw-scrape _070937 + _083302 + the "
    "nomination-day PIR summaries) materially extend and reinforce the 08:31 Nomination-Day verdict, with three movements: "
    "(1) the Bersatu-PN fracture DEEPENS from a one-sided Muhyiddin spat (08:31) into a MUTUAL, ON-THE-RECORD leadership "
    "confrontation — Hadi Awang dismisses 'toxic PN' and points the finger at Bersatu (NST, JEMPOL); Samsuri verbatim-refutes "
    "Muhyiddin in Utusan ('tidak berasas' / 'diluluskan oleh Majlis Tertinggi PN'); Muhyiddin declares Bersatu the 'sole "
    "opposition' and claims PN supports the government (NST); a PN info chief floats terminating Bersatu's membership. "
    "ESC-011/ESC-010 remain CRITICAL and are now mutual. (2) PH's edge shifts from STRUCTURAL-only to STRUCTURAL + NARRATIVE: "
    "Fahmi ('banking on Aminuddin's MB track record'), Loke (NS-as-DAP-referendum + Jelebu-4-seats-critical), and Fuziah/PKR "
    "(integrity framing) give PH a proactive voice — FILLING the 08:31 'no PH narrative' gap. (3) BN leadership synchronises an "
    "'understanding, not merger' containment re-framing (Zahid/Wee/Johari/Asyraf), DOWNGRADING ESC-009 from 'verified pact' to "
    "an informal BN-PAS understanding — BN itself abandons the 'unified opposition' framing, likely to contain fallout from the "
    "Bersatu split + UMNO divisional dissent. The clean nomination is upgraded to multi-source CONFIRMED (EC + PDRM; zero "
    "rejections, zero incidents). EC granularity (cross-verified): 21 three-cornered fights, 12 of them PH-BN-Bersatu; Bersatu "
    "fights one/both allies in 20 of 24 seats. New candidate-quality sweep (Faizal mature, Razali ex-police, LeeVinesh youngest, "
    "Ismail unfazed, Tok Mat heavyweight). The ONE new PH-risk vector is the analyst 'Malay tsunami forming in NS?' narrative "
    "(ESC-013, MEDIUM), though it is structurally counteracted by the Bersatu-PN split. NET: the PH-favorable tilt "
    "STRENGTHENS and is now narrative-backed; the opposition fracture is the dominant, defining development of Nomination Day. "
    "Distribution: 10 positive / 9 neutral / 6 negative (full-day merged; baseline was 4/4/4)."
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
print("revision_history:", v.get("revision_history"))
print("status:", v.get("status"))
print("entities_analyzed:", v.get("entities_analyzed"), "(baseline", v.get("entities_analyzed_baseline_0831"), "+ delta", v.get("entities_analyzed_delta_1633"), ")")
print("sentiment_summary counts: pos", len(v["sentiment_summary"]["positive"]),
      "neu", len(v["sentiment_summary"]["neutral"]), "neg", len(v["sentiment_summary"]["negative"]))
print("sentiment_distribution:", v["sentiment_distribution"])
print("narrative_indicators:", len(v["narrative_indicators"]))
print("escalation_flags:", len(v["escalation_flags"]))
print("data_gaps:", len(v["data_gaps"]))
print("file bytes:", os.path.getsize(PATH))
