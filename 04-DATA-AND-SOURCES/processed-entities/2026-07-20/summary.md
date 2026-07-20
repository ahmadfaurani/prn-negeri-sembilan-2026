# PRN Negeri Sembilan 2026 — Entity Extraction Summary
**Date:** 2026-07-20 (Campaign Day 2, morning) — processing run 01:06 UTC = 09:06 MYT
**Extraction run:** 20260720-0106 (6th carry-forward of the Director-approved 19 Jul 17:25 MYT cycle; mission brief labels it the 4th carry-forward)
**Source:** `04-DATA-AND-SOURCES/raw-scrapes/20260719/` — the two fetch cycles NOT yet ingested by the entity-extraction agent after the prior 2225 run: **20260719_222800** (06:30 MYT 20 Jul) + **20260719_233400** (07:36 MYT 20 Jul)
**Output:** `entities-20260720-0106.json` — **232 entities** (230 base from 2225 run + 2 new; PIR-06=57, PIR-07=108, PIR-16=67; critical=14, priority=108, normal=110)
**Build script:** `raw-scrapes/_build_entities_0106.py`
**Prior runs (in `2026-07-19/`):** 1217 (133) → 1435 (205) → 1725 (226) → 1954 (228) → 2225 (230) → **this run (232)**
**Base reference:** the comprehensive 12→15-cycle analysis lives in `2026-07-19/summary.md` (this run appends only the genuinely-new delta; it does not repeat the full corpus).

---

## Headline Finding — QUIET / World-Cup-dominated corroboration cycle

Both newly-ingested cycles are **low-yield** by the nature of the Day-2 pre-dawn/early-morning MYT window, which is dominated by overnight coverage of the **19 Jul 2026 World Cup final (Argentina–Spain; Spain won via Torres)**. The collection agent's own index confirms this explicitly:

- **222800 cycle:** 3 files created — **ALL FALSE POSITIVES** (Iraq-Iran-US diplomacy + 2× World Cup football). Matched the NS regex on incidental substrings. **0 NS-PRN entities.**
- **233400 cycle:** 16 files created — **13 RSS items = ALL FALSE POSITIVES** (World Cup football ×9 + South-China-Sea defence [Khaled as Defence Minister, not NS PRN] + World-Cup-hosting [Zahid] + national-flag/AI [Fahmi] + Johor-investment). Only **3 gnews items are genuinely-new-to-collection**, of which **1 is genuinely-fresh** post-cutoff.

**Genuinely-fresh post-cutoff (post-06:28 MYT 20 Jul) NS PRN content = 1 article.**
**NO new PIR-06/07/16 intelligence developments** (collection agent's own 233400 assessment).

---

## What is genuinely NEW this run (2 new entities, 3 context updates)

### 🟢 NEW PIR-06 entity — "Bersatu Johor-wipeout-repeat framing" (Khaled, FMT) [PRIORITY]

**FMT EN** "Khaled urges voters to ensure repeat of Bersatu's Johor wipeout in NS" (07:12 MYT 20 Jul, gnews headline-intel; FMT direct URL not curl-recoverable — 404 across 10 category/day guesses; gnews protobuf still curl-unresolvable, 18th cycle confirmation). This is the **5th-outlet corroboration** of Khaled Nordin's "Pastikan Bersatu di NS KO habis" statement (prior 4 outlets: NST EN + Utusan BM + BH BM + Awani BM, all from the 171500 cycle).

**The genuinely-new analytical element** is the **Johor-precedent framing**: FMT is the first outlet to explicitly frame the targeted NS Bersatu wipeout as a **REPEAT of Bersatu's Johor state-election result** (where Bersatu was wiped out). Prior captures used "KO habis" / "knocked out" but did not name the Johor precedent. This reinforces the PIR-06 electoral-elimination vector — a BN VP publicly urging Bersatu's electoral destruction while BN operationally cooperates with Bersatu's coalition partners via PN.

**Classification: [PRIORITY PIR-06], NOT [CRITICAL].** Director PIR-06 [CRITICAL] keywords ("pecat"/"keluar"/"tarik diri"/"termination"/"toxic PN"/"kuorum"/"lebih hebat") are about coalition-membership actions; this is electoral-elimination *rhetoric* by a BN (not PN) leader — adjacent to but not the same as a formal PN-MT expulsion/withdrawal. No formal threshold is crossed.

### 🟢 NEW PIR-07 entity — "Loke baptism of fire" (Chennah, Newswav) [normal]

**Newswav** "Anthony Loke Coming Baptism of Fire in The Negeri Sembilan Polls" (18 Jul 16:30 MYT, gnews headline-intel; pre-cutoff / nomination-day). Newswav's analytical framing of Loke's Chennah defense as a "baptism of fire." Chennah = the only MCA-DAP straight fight (Loke PH/DAP sec-gen vs Siow Kong Choon MCA/BN); 47.8% Malay (up from 44% in 2018); PH vote dropped to 44% by PRU15 vs BN+PN combined 56% → if the PRU15 pattern repeats, Loke LOSES (per mkini 780075 full text, prior 075200 cycle). The "baptism of fire" framing reinforces the PIR-16 "MCA biggest loser" / Loke-under-pressure narrative and the PIR-07 marquee-battleground status of Chennah. **[normal PIR-07]** — analytical framing, not a hard-news development.

### 🔄 Context updates (3)

| Entity | PIR | Update |
|---|---|---|
| **Mohamed Khaled Nordin** | PIR-06 [PRIORITY] | Now **5-outlet** corroborated (NST EN + Utusan BM + BH BM + Awani BM + **FMT EN**, 233400). NEW Johor-precedent framing ("repeat of Bersatu's Johor wipeout"). |
| **Bersatu KO habis (electoral-elimination call)** | PIR-06 [PRIORITY] | 5th-outlet (FMT) + Johor-as-precedent framing now explicit. Still [PRIORITY] not [CRITICAL] (BN-leader electoral-elimination rhetoric, not formal PN-MT action). |
| **19 campaign permits approved** | PIR-07 [normal] | **Malay Mail** outlet added (19 Jul 11:00 MYT, gnews headline-intel; Malay Mail full-text URL not curl-recoverable). Same event, new outlet (prior: NST 12:26 + Kosmo 10:54 + Awani). No new intelligence. |

---

## PIR-06 [CRITICAL] status — MAINTAINED, 18th consecutive cycle with no threshold crossing

The three Director-designated [CRITICAL] PIR-06 triggers remain in play; **none newly crossed** this run:

| # | Trigger | Status |
|---|---------|--------|
| 1 | **"lebih hebat" new-coalition declaration** (Muhyiddin, Sinar 17 Jul) | [CRITICAL] MAINTAINED — no formal launch 18–20 Jul. gnews "lebih-hebat" = 0 (18th cycle). |
| 2 | **"sasar bentuk kerjaan negeri" Bersatu solo 24-seat governing bid** (MalaysiaGazette + Sinar 19 Jul) | [CRITICAL] MAINTAINED — Bersatu-attributed hard-news confirmed; 24 > 19 simple-majority threshold; no formal withdrawal of solo bid. (PH/Loke "sasar 23 kerusi" version is PH-attributed → [PRIORITY], does NOT cross this trigger.) |
| 3 | **Kiandee quorum escalation** (FMT 11 Jul, [CRITICAL] flagged 075200) | [CRITICAL] MAINTAINED — formal PN-MT expulsion notice / Bersatu candidate withdrawal / RoS intervention all STILL NOT issued across 18 cycles. Radzi Jidin rebuttal contested (49-vs-23 baseline). Kiandee attended Hamzah "gabung jentera" event (suspended VP still operating inside PN campaign). |

**[CRITICAL]-tier adjacent signals (sustained, not escalated):**
- toxic PN (Muhyiddin) — Hamzah rebuttal; no new escalation
- pecat Tang Jay Son (Gerakan) — no new intra-PN pecat events
- RoS complaint disrupting PN seat negotiations (Tun Faisal) — no formal RoS action
- gabung jentera (machinery merger) — operationalized; no fracture
- kuorum (MPT quorum dispute) — contested, not resolved; gnews "kuorum Bersatu" (tightened with false-positive filter) returned 0; no KOHA.net foreign-assembly false positive this cycle
- PDM Klawang shutdown/reopen — Jalaluddin expected "1–2 days"; now **hour 15+** of that window (20 Jul MYT business hours just beginning). **Watch for reopening confirmation next cycle.**

**All 8 mandatory PIR-06 [CRITICAL]-watch gnews queries returned 0** in the 222800 + 233400 cycles. The KUORUM false-positive filter (new in 233400) is confirmed working — no KOHA.net Kosovo-assembly false positive appeared (vs. 1 in the 212300 cycle).

---

## Tier-4 seat watch (Director PIR-06 list)

| Seat | Status this run |
|------|-----------------|
| N.04 | No new intel; no Bersatu candidate withdrawals |
| N.05 | Zambry-Samsuri Port Dickson meeting (prior 2225 run); no new intel |
| N.13 (Sikamat) | No new intel; Tun Faisal (Bersatu) vs Razali (Wawasan/PN) vs Nor Azman (PH) |
| N.14 (Ampangan) | No new intel; Dr Rafie (PN) vs Nazri Kassim (PH) |
| N.23 | No new intel; no Bersatu candidate withdrawals |
| N.25 (Labu) | No new intel; Maira (Bersatu) vs Ahmad Faez (PH) |
| N.31 | No new intel; no Bersatu candidate withdrawals |
| N.34 | No new intel; no Bersatu candidate withdrawals |

---

## Watch entities (Director PIR-16 list — retained, no new intel this run)

- **Mah Hang Soon** (MCA) — no statement/response; MCA rebuttal watch continues (only Wee's "not a merger" defense has surfaced)
- **Albert Tei** — 0 fresh items across 18 cycles
- **"barking dogs"** — 0 fresh items across 18 cycles
- **"majoriti mudah"** — not surfaced this run
- **Muhyiddin graft trial** — not surfaced in today's collection

---

## PIR-16 [CRITICAL] threshold check — NOT CROSSED (18th cycle)

- **"Bersatu exit from PN imminent?"** — gnews "bersatu-exit-pn" returned **0 fresh items** across the 222800 + 233400 cycles. The mkini SNAPSHOT (18 Jul 18:00) remains the lone viral-tier item. **Hard-news corroboration NOT detected → [CRITICAL] threshold NOT crossed → remains [PRIORITY PIR-16].**
- **"sasar bentuk kerajaan negeri"** (Bersatu-attributed) — no new hard-news this run; the MalaysiaGazette + Sinar (19 Jul) items stand as the [CRITICAL] baseline (trigger already crossed on the Bersatu-attributed version in prior runs).
- **"Bersatu kacau daun"** — no new hard-news pickup; stands at Wan Saiful (Metro 16:31) + Khaled 4-publisher (FMT+BH+Metro+NST, 171500). This run's FMT Khaled "Johor wipeout repeat" reinforces but does not newly cross the hard-news-corroboration bar.

---

## Cross-PIR synthesis (unchanged; reinforced marginally this run)

The central structural tension documented across the prior 15 cycles persists and is only marginally reinforced this run:

> **PN concedes the NS MB post to BN, merges campaign machinery (gabung jentera), prepares a joint manifesto (manifesto bersepadu), and permits joint ceramah (kongsi pentas) — while Bersatu simultaneously declares a "lebih hebat" post-PRN new coalition, contests 24 seats under its own logo targeting solo state-government formation ("sasar bentuk kerajaan negeri"), frames PN as "toksik", and faces an internal MPT quorum crisis (Kiandee). Meanwhile, BN's own Umno VP (Khaled Nordin) publicly calls for Bersatu to be "KO habis" electorally — now with explicit Johor-precedent framing (FMT, this run) — so BN gets straight fights in PRU16.**

The BN-PN operational arrangement and the Bersatu-exit-from-PN trajectory continue to run in parallel on the same ballot. This run adds only a **5th-outlet corroboration + Johor-precedent framing** to Khaled's electoral-elimination rhetoric — a marginal reinforcement, not a structural change.

---

## Methodology notes
- **Cycles covered this run:** 222800 (0 NS-PRN entities — 3 false positives) + 233400 (1 fresh NS item + 2 pre-cutoff new-outlet/new-framing items). Built on the 2225 base (230 entities, 15 cycles).
- **Source URLs** are direct article URLs where full text was fetched (NST/BH/FMT/METRO/Utusan RSS); the 3 genuinely-new 233400 items are **gnews headline-intel** (title + pubdate + publisher) because gnews protobuf URLs remain curl-unresolvable (18th cycle confirmation) and FMT direct-URL recovery failed (404 × 10). The "19 permits" Malay Mail full-text URL is also not curl-recoverable (JS-rendered). These are honest collection limitations.
- **[CRITICAL] flags** applied per Director-designated PIR-06 triggers. **No new [CRITICAL] threshold crossed this run** (18th consecutive cycle; Kiandee quorum [CRITICAL] from 11 Jul maintained).
- **[PRIORITY] flags** applied per Director rules. The 2 new entities this run are [PRIORITY] (Johor-wipeout-repeat framing) and [normal] (Loke baptism-of-fire framing) — both rhetorical/analytical, not formal PN-MT action.
- **False-positive pattern (recurring, 4th consecutive cycle):** the 19 Jul World Cup final generates overnight/morning sports content across NST/BH/Utusan/METRO that matches the NS regex on incidental substrings (`hadi`≤`hadiahkan`, `jalur`≤`Jalur Gemilang`, `fahmi`≤`Fahmi`, `zahid`≤`Ahmad Zahid`, `khaled`≤`Khaled Nordin` [Defence Minister context], `wee`≤`week`, `nga`≤`Fernandez`). 22 of 25 "fresh" items across the two cycles are false positives. Documented; not analytically material. Expected to recede as campaign content dominates the 08:00+ MYT window.
- **GMT-parsing edge case (technical, from 233400):** the FMT Khaled item (pubdate "Sun, 19 Jul 2026 23:12:42 GMT") was logged fresh=False due to Python `strptime %Z` not robustly parsing "GMT"; the item IS genuinely-fresh (23:12 UTC ≥ 22:28 UTC cutoff). Flagged for is_fresh() fix in future cycles.
- **This run (0106) supersedes the 2225 run** by incorporating the 222800 + 233400 cycles: 2 new entities + 3 context updates. The bulk of the corpus (230 of 232 entities) was established in prior runs; this run's analytical delta is deliberately small and honestly reported.
- **No fabrication:** every entity traces to a fetched article URL or a gnews-surfaced publisher+title+pubdate. The 2 new entities and 3 context updates all reference real collected content in `raw-scrapes/20260719/`.

---

## Pipeline status
- **Total cycles run 2026-07-19 → 2026-07-20:** 17+ (075200 → 233400 UTC = 15:25–07:36 MYT span)
- **Total titles scanned:** ~3,800+
- **Total entities:** 232 (PIR-06=57, PIR-07=108, PIR-16=67; critical=14, priority=108, normal=110)
- **PIR-06 [CRITICAL] flag:** MAINTAINED — formal PN Supreme Council expulsion/removal notice for Bersatu = **0 hits across ~3,800+ titles scanned** (18th consecutive cycle with no [CRITICAL] threshold crossing on the fracture vector)
- **Next significant content windows:** (a) **PH manifesto launch — Mon 20 Jul evening** (Klana Resort, Seremban; Amirudin Shari officiating; "manifesto for continuity"); (b) **BN manifesto launch — 24 Jul at DUN Linggi + Pertang** (potential JOINT BN-PN event per Annuar's "manifesto bersepadu"); (c) Day-2 morning campaign dispatches expected 08:00–10:00 MYT as the news cycle fully resumes (post-World-Cup dominance).

---
*Run 0106 complete. 232 entities saved to `entities-20260720-0106.json`. 2 new entities, 3 context updates. [CRITICAL] count unchanged at 14 (no new threshold crossed; 18th consecutive cycle). [PRIORITY] count +1 (107→108). Day-2 early-morning window World-Cup-dominated: 22 of 25 "fresh" items across 222800+233400 = false positives. Genuinely-fresh post-cutoff NS PRN = 1 article (FMT Khaled "Johor wipeout repeat", 5th-outlet corroboration of already-captured event). No new PIR-06/07/16 intelligence developments. Generated 2026-07-20 09:07 MYT (01:07 UTC) by PRN NS 2026 Entity Extraction Agent. TLP:AMBER. All entities carry source_url (direct or gnews-headline-intel).*
