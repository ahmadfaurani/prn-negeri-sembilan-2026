# PRN Negeri Sembilan 2026 — Sentiment Analysis Summary
## Date: 20260719 (Campaign Period Day 1 Afternoon, 17:28 MYT) — Revision 11
## Generated: 2026-07-19T17:28:00+08:00 (09:28 UTC) | TLP:AMBER
## Agent: PRN Negeri Sembilan 2026 Sentiment Analysis Agent (cron)

**Latest sentiment file:** `sentiment-analysis/20260719/sentiment-20260719-1728.json`
**Prior revision:** `sentiment-analysis/20260719/sentiment-20260719-0710.json` (revision-10, 15:10 MYT 19 Jul)
**Entity build (NEW, FULL-TEXT consolidation):** `processed-entities/20260719/entities-20260719-0714.json` (223 entities, 114,922 bytes, lint-passed) — rev10 used `entities-20260719-0507.json` (167 entities) + 064654 enrichment; rev11 ingests the full 223-entity build (56 new entities + 23 context upgrades). The 0714 build adds **FMT RSS full text (19 articles), NST WordPress feed full text (7), Astro Awani direct full text (3)** — substantially closing the prior JS-render/paywalled blocker gap.
**Election milestone:** Campaign Period Day 1 (Nomination Day 18 Jul 2026 closed; Day-1 afternoon 14:00-18:00 MYT window — this pass at 17:28 MYT). Polling 1 Aug 2026; early voting 28 Jul; BN manifesto launch 24 Jul (DUN Linggi). Electorate 889,490.
**Score convention:** SIGNED per mission directive — negative = -1.0 to -0.1; neutral = -0.1 to +0.1; positive = +0.1 to +1.0.

---

## VERDICT

**CAMPAIGN DAY-1 AFTERNOON — FULL-TEXT ESCALATION (17:28 MYT 19 Jul)** — rev11 ingests the consolidated 223-entity full-text build (0714). One headline escalation vs rev10:

### [CRITICAL — ESCALATION TIER] PIR-16 — HARD-NEWS CORROBORATION OF "BERSATU EXIT IMMINENT?"

The PIR-16 CRITICAL escalation rule **FIRES** this revision. rev10 had the "Bersatu exit from PN imminent?" narrative at the **viral-amplification** CRITICAL tier (mkini SNAPSHOT + 3 new attack vectors, >50% volume). rev11's FMT **full text** (19 Jul 09:00 MYT) now confirms the hard-news corroboration the director rule requires:

> *"Muhyiddin said the party will form a new coalition after the state election, **hinting at a PN exit**."* — FMT, 19 Jul 09:00 MYT (full text)

FMT is a hard-news outlet. This full-text confirmation **escalates the "Bersatu exit imminent?" narrative from viral-amplification CRITICAL (-0.60) to hard-news-corroborated CRITICAL escalation-tier (-0.72)** — the highest PIR-16 alert the directive defines. It is simultaneously the **strongest pre-threshold PIR-06 signal** (Muhyiddin new-coalition-post-NS hint). **Formal PN-MT removal notice STILL NOT DETECTED** (9th consecutive pass since 170837) — the threshold (formal pecat/termination or formal Bersatu withdrawal) is NOT crossed, but the trajectory has moved one tier closer.

This is the most significant sentiment shift of the cycle: a narrative that was, 2 hours ago (rev10), a viral-amplification concern is now **a hard-news-corroborated exit-hint on the record**.

---

## KEY NUMERIC FINDINGS

| Metric | Value |
|---|---|
| **Cumulative entities scored** | 68 |
| **Delta NEW entities (rev11)** | 14 (+ 6 analyst/opinion figures) |
| **Delta revised entities (rev11)** | 17 |
| **Sentiment distribution (signed)** | 23 positive / 15 neutral / 30 negative |
| **PIR-06 >30% numeric shift (rev10→rev11)** | NO (Muhyiddin +2.4%, Bersatu +2.5%, thread +1.2%) — CRITICAL fires via qualitative internal-fracture rule (full-text-reinforced) |
| **PIR-06 >30% numeric shift (vs 20260718 baseline, 48h)** | APPROACHING — Bersatu -0.68 (unsigned-mag) → -0.82 (signed) ≈ sharp directional deepening with escalation tiers added |
| **PIR-07 incumbent >20% drop** | NOT DETECTED (Aminuddin +0.62, Bakri Sawir +0.45, Tok Mat +0.58) |
| **PIR-16 >50% viral amplification** | CARRIED ("Bersatu in disarray", subsumed under escalation tier) |
| **PIR-16 hard-news corroboration** | **FIRED (rev11 NEW)** — FMT full text corroborates "Bersatu exit imminent?" |
| **Direction flips** | NONE (Hadi improving slightly toward neutral; no flips) |
| **formal_removal_notice_detected** | false across 9 consecutive passes since 170837 |
| **Bersatu candidate withdrawals** | NONE this cycle (24 solo candidates stable) |
| **Alerts** | 7 CRITICAL / 12 PRIORITY / 49 none |

---

## PRIORITY ALERTS — DIRECTOR APPROVED (19 Jul 14:50 Cycle, 3rd carry-forward)

### [CRITICAL] PIR-06 — Coalition Operational Arrangement
**Status: CARRIED + ESCALATED (full-text reinforcement); formal threshold NOT crossed**

- **PN-removal-of-Bersatu thread (ESC-014)** — -0.86, CARRIED + ESCALATED. Formal notice still 0 hits (9 passes).
- **Muhyiddin new-coalition-post-NS hint (NEW, FMT full text)** — -0.78, **CRITICAL**. Director-flagged NEW PIR-06 signal. "Will form a new coalition after the state election, hinting at a PN exit." Strongest pre-threshold signal; approaches formal withdrawal without crossing.
- **Kiandee quorum question (NEW, NST)** — -0.75, **CRITICAL**. Director-flagged NEW. Escalation from "asas kukuh to remove" → questioning whether Bersatu Supreme Council even has quorum. Internal-legitimacy attack; termination-adjacent.
- **Bersatu** — -0.82, **ESCALATED**. Internal-fracture signal sharp-negative → [CRITICAL] per directive rule. Full-text-reinforced (Lau/Azeem/Azmil analyst consensus + Muhyiddin PN-exit hint + Ridzuan quit + PAS severed ties June 8).
- **Muhyiddin Yassin** — -0.86, **ESCALATED**. FMT full text "new coalition PN exit hint" + "charade to deceive the Malays". Internal-fracture signal applies to president.
- **Bersatu-PN fracture (ESC-011, three-sided)** — -0.85, CARRIED + ESCALATED (full-text three-sided reinforcement).
- **"toxic PN" / Hadi-blames-Bersatu (full text)** — -0.70, CARRIED. FMT full text (18 Jul 12:48): Hadi "rift caused by Bersatu misconduct"; Muhyiddin "PAS made PN toxic, baseless." Claim/counter-claim both on the record.
- **Hadi Awang** — -0.35, IMPROVING (inclusive coalition-building offsets blame-shift).
- **PN** — +0.30 neutral, stable (grassroots thumbs-up + 11-no-clashes + machinery-sharing).
- **Hamzah Zainudin** — not quoted; carryover watch figure.
- **Ridzuan Ahmad** — confirmed Bersatu-quit; Bersatu-cohesion negative (scored under Bersatu).
- **"toxic PN"/"pecat"/"kuorum" trajectory** — stable/deepening; "kuorum" is the NEW tier (internal-legitimacy attack); no formal pecat.

**Escalation progression:** rev3 (precursor) → rev4 (senior-figure advocacy) → rev5 (two-sided principal-level) → rev6 (consolidation) → rev7 (corroboration) → rev8 (operational-split reinforcement) → rev9 (viral-amplification: "imminent?" SNAPSHOT) → rev10 (internal-legitimacy attack: quorum + analyst wipeout consensus) → **rev11 (full-text reinforcement of all three sides + Muhyiddin PN-exit hint hard-news-corroborated)**. NO new escalation TIER beyond "hard-news-corroborated exit-hint"; NO formal notice.

**Trigger #2 (coalition restructuring): UNCHANGED — reachable via EITHER path (PN-MT removal OR Bersatu exit), NOT fired.** Most likely near-term outcome unchanged: Bersatu voluntary realignment AFTER Aug 1 poll. The Muhyiddin full-text hint strengthens the "Bersatu voluntary exit" path's plausibility.

### [CRITICAL — ESCALATION TIER] PIR-16 — "Bersatu exit imminent?" HARD-NEWS CORROBORATION
**Status: ESC-017 ESCALATED / ACTIVE — HARD-NEWS CORROBORATION DETECTED**

rev10 → rev11: the "Bersatu exit from PN imminent?" narrative escalates from viral-amplification CRITICAL to **hard-news-corroborated CRITICAL escalation-tier**:
- rev10: viral-amplification (>50% volume) — mkini SNAPSHOT + 3 attack vectors (quorum + PAS-expel + quit-advice)
- **rev11: FMT FULL TEXT (19 Jul 09:00)** — Muhyiddin "will form a new coalition after the state election, hinting at a PN exit." = hard-news corroboration.

This is the PIR-16 CRITICAL escalation rule: *"If hard-news outlet corroborates 'Bersatu exit imminent?' = [CRITICAL] (escalation tier)."* FMT is a hard-news outlet. Narrative -0.60 → -0.72. **PIR-06+16 overlap** — this is simultaneously the strongest pre-threshold PIR-06 signal.

### [PRIORITY — NEW] PIR-16 — Other narrative alerts

- **"Umno's dangerous dance with PAS" (ESC-020 NEW)** — FMT FULL-TEXT opinion (19 Jul, 7009c). Highest-risk viral-amplifier opinion piece this cycle: "By quietly opening the side door for PAS in NS, Umno is validating the very force designed to replace it." Cites Amanat Hadi (1981, Umno supporters as "infidels"). "The tiger is always hungry, and it does not care for understandings." Warns urban non-Malay alienation (Seremban, Rasah, Nilai). -0.60. Viral-amplification watch.
- **"DAP coalition-intolerant" frame (ESC-021 NEW)** — Director-flagged NEW monitor. Hadi (NST full text 14:03): reject "unnatural Malay groups with DAP, namely fanatical secular and extreme chauvinist groups that threaten Islam and the Malay community." Targets the 13 non-Malay DUNs DAP defends. Frame -0.45. **Counter-narrative emerging:** Lim Lip Eng (FMT full text) rejects Hadi's Islamophobia claim, cites green-wave provenance (Hadi coined "gelombang hijau" 2018) + Tuan Ibrahim "PAS never claimed sole embodiment of Islam." +0.35. Net contested.
- **"MCA biggest loser" + MCA rebuttal trajectory (ESC-018)** — Loke quote (FMT full text) -0.50. MCA rebuttal = Wee "not a merger" containment + Saw Yee Fung internal dissent = **CONTAINMENT not counter-attack** → MCA on the defensive. Trajectory: declining (MCA).
- **AMH "BN ministers quit" (ESC-019)** — PM Anwar responded ("resign to attack unity partners", NST full text). Amplification signal held. -0.40.
- **"barking dogs" (Albert Tei)** — carried PRIORITY. Paywalled, high viral-potential.
- **Melaka PH-BN fracture (DAP withdrawal, ESC-016)** — carried PRIORITY. 7 NST headline-intel + mkini preview. Stable/declining visibility as cycle shifts to NS Day-1. Still dominant PIR-16 frame for DAP acceptance in NS Malay seats.
- **Muhyiddin graft-trial frame** — carried PRIORITY. "Company gave Bersatu RM1m for unknown reasons." mkini paywalled.

### [PRIORITY-WATCH] PIR-07 — Highest-Priority Battlegrounds
**Status: Day-1 afternoon enrichment; NO critical flag; NO incumbent >20% drop**

- **Incumbent sentiment drop >20%: NOT DETECTED.** Aminuddin (N.32) +0.62; **Bakri Sawir (N.28) +0.45 confident**; Tok Mat (Rantau) +0.58.
- **N.28 Klawang: full-text confirmed** (Awani 19 Jul 12:11). Bakri Sawir (PH incumbent) vs Danni Rais (PN, Bakri's cousin) vs Muhammad Adib Musa (Bersatu). Cousins campaigned peacefully at Pasar Minggu Kuala Klawang; "brotherly fight." HIGHEST PIR-07 value.
- **N.27 Chembong: FMT full text recovered.** BN Zaifulbahri (since 2008, 4,335 maj) vs PH Danish Nazran. Straight fight, BN incumbent edge.
- **"fleeing Sikamat" narrative: persists, NOT intensifying.** "Aminuddin fled Sikamat" frame NOT gaining negative traction (frame is "pindah kawasan").
- **N.14 defector-framing: ACTIVE, NOT intensifying.** PH "defector" vs PN "experienced rep" — priority-watch per directive.
- **Afternoon Day-1 dispatch (14:00-18:00 MYT window):** 17:28 MYT, within window. NST full text: 19 ceramah permits ALL APPROVED, 1 verbal-dispute report (no investigation). Mature-campaign framing dominant. Positive.
- **BN manifesto launch 24 Jul at DUN Linggi: UPCOMING** (5 days). Director-flagged NEW monitor. No sentiment yet; watch for narrative shifts at the launch.

**No PIR-07 critical flag triggered.** Priority-watch only.

---

## PIR TREND ANALYSIS

### PIR-06 Trajectory (CRITICAL carried + escalated; full-text reinforcement)
Across 11 revisions:
- rev3-5: precursor → senior-figure advocacy → two-sided principal-level exit signaling
- rev6-7: consolidation (KINIGUIDE) → corroboration (NST "crossroads" + 7 ballot clashes)
- rev8-9: operational-split reinforcement (Kosmo "keluar") → viral-amplification ("imminent?" SNAPSHOT)
- rev10: internal-legitimacy attack (Kiandee quorum + analyst "perebutan kuasa"/wipeout consensus)
- **rev11: full-text reinforcement of all three sides + Muhyiddin "new coalition PN exit" hint HARD-NEWS-CORROBORATED (FMT full text).** Approaches formal withdrawal without crossing.

**Three-sided fracture now viral-amplification-reinforced AND analyst-validated AND hard-news-corroborated.** Trajectory UNCHANGED: most likely Bersatu voluntary realignment AFTER Aug 1; PN-MT removal remains possible if Bersatu candidates damage PN in 8 confirmed direct-clash seats. Trigger #2 unchanged (not fired).

### PIR-16 Trajectory (CRITICAL escalation-tier + new priorities)
- rev9: Melaka DAP withdrawal (+600% source) + "imminent?" SNAPSHOT → first PIR-16 priority
- rev10: "Bersatu in disarray" rapid amplification (>50% volume, NEW CRITICAL ESC-017) + "MCA biggest loser" (NEW PRIORITY ESC-018) + AMH amplification (NEW PRIORITY ESC-019)
- **rev11: "Bersatu exit imminent?" HARD-NEWS CORROBORATION (FMT full text) → escalation tier (ESC-017-ESCALATED); NEW "Umno dangerous dance with PAS" viral-amplifier opinion (ESC-020); NEW "DAP coalition-intolerant" frame + Lim Lip Eng counter (ESC-021).**
- Counter-trends: Tok Mat "act now" existential + Anwar "Ali Baba" multi-ethnic counter + Anwar "resign to attack" discipline + Hadi inclusive MCA/MIC formula + "mature campaign" process frame + "makmal politik" analyst frame (FMT full text).
- "majoriti mudah" (BN confidence) NOT yet quoted (latent watch for 24 Jul manifesto); "not taking for granted" (PH/BN defence) active.

### PIR-07 Trajectory (Day-1 afternoon enrichment; no critical)
- rev9: FIRST Day-1 walkabout (Loke/Chennah) + Aminuddin revised UP
- rev10: N.28 Klawang gap FILLED + Tok Mat/Anwar/Johari Day-1 coverage
- **rev11: full-text confirmation (Awani Klawang cousins, NST Tok Mat/Anwar, FMT N.27 Chembong/N.10/N.33/Kota/Paroi/Pertang recovered). Afternoon Day-1 dispatch (17:28 MYT) positive. BN manifesto 24 Jul upcoming.** No incumbent drop.

---

## ESCALATION FLAGS UPDATE

| Flag ID | Severity | Status (rev11) | Description |
|---|---|---|---|
| **ESC-017-ESCALATED** | CRITICAL | NEW / ESCALATION TIER | "Bersatu exit imminent?" HARD-NEWS CORROBORATION (FMT full text Muhyiddin "new coalition PN exit hint") |
| **ESC-014** | CRITICAL | CARRIED + ESCALATED | PN-removal-of-Bersatu thread — quorum + exit hint; no formal notice |
| **ESC-011** | CRITICAL | CARRIED + ESCALATED | Bersatu-PN fracture (three-sided, full-text reinforced) |
| **PIR-06-BERSATU** | CRITICAL | ESCALATED | Bersatu internal-fracture signal sharp-negative (full-text confirmed) |
| **PIR-06-MUHYIDDIN** | CRITICAL | ESCALATED | Muhyiddin (Bersatu president) — "new coalition PN exit hint" hard-news |
| **ESC-017-PREV** | CRITICAL | CARRIED (subsumed) | "Bersatu in disarray" viral amplification (>50% volume, rev10 origin) |
| **PIR-06-TOXIC-PN** | CRITICAL | CARRIED (full text) | "toxic PN" claim/Hadi-blames-Bersatu claim-counterclaim (FMT full text) |
| **ESC-020 (NEW)** | PRIORITY | NEW / ACTIVE | "Umno dangerous dance with PAS" FMT opinion (viral-amplifier, Amanat Hadi 1981) |
| **ESC-021 (NEW)** | PRIORITY | NEW / ACTIVE | "DAP coalition-intolerant" frame (Hadi, 13 non-Malay DUNs) + Lim Lip Eng counter |
| **ESC-016** | PRIORITY | CARRIED | Melaka PH-BN fracture (DAP withdrawal) — stable/declining visibility |
| **ESC-018** | PRIORITY | CARRIED | "MCA biggest loser" (Loke) + MCA rebuttal = containment (defensive) |
| **ESC-019** | PRIORITY | CARRIED | AMH "BN ministers quit" — PM responded (amplification signal) |
| **PIR-07-FLEEING-SIKAMAT** | PRIORITY | WATCH (active, not intensifying) | "fleeing Sikamat" persists; Aminuddin no drop |
| **PIR-07-N14-DEFECTOR** | PRIORITY | WATCH (present, not intensifying) | N.14 defector-framing carryover |
| **PIR-16-BARKING-DOGS** | PRIORITY | CARRIED | Paywalled, high viral-potential, watch |
| **PIR-16-MUHYIDDIN-GRAFT** | PRIORITY | CARRIED | Active trial draining credibility |
| **PIR-07-AMINUDDIN-WATCH** | PRIORITY | WATCH (no critical) | Aminuddin stable +0.62; "fleeing" not intensifying |
| **ESC-015** | HIGH | CARRIED | PIR-09 — Tamim re-surface; no new credibility event |
| **ESC-007** | HIGH | Day-1 ENRICHMENT | PIR-07 — Klawang/Chembong full-text; no incumbent drop |

**Triggers fired: NONE.** Trigger #2 (coalition restructuring) UNCHANGED (reachable via EITHER path; the Muhyiddin full-text hint strengthens the "Bersatu voluntary exit" path's plausibility but threshold not crossed). Trigger #7 (independents in 5-cornered seats N.10/N.33) on WATCH.

---

## NEW ENTITIES SCORED (Rev11 Delta)

### Critical-tier NEW/escalated
| Entity | PIR | Score (signed) | Trend | Alert |
|---|---|---|---|---|
| "Bersatu exit imminent?" / Muhyiddin new-coalition-post-NS | PIR-06+16 | -0.72 | declining | CRITICAL (escalation tier) |
| Kiandee quorum question (is Supreme Council functional?) | PIR-06 | -0.75 | declining | CRITICAL |
| Muhyiddin new coalition after state election (PN-exit hint) | PIR-06 | -0.78 | declining | CRITICAL |

### Priority NEW
| Entity | PIR | Score | Trend | Alert |
|---|---|---|---|---|
| "Umno's dangerous dance with PAS" (FMT opinion) | PIR-16 | -0.60 | improving (viral) | PRIORITY |
| "DAP coalition-intolerant" frame (Hadi, 13 non-Malay DUNs) | PIR-16 | -0.45 | declining | PRIORITY |
| Bersatu advised to quit PN (analyst, FMT full text) | PIR-06+16 | -0.55 | declining | PRIORITY |
| "Bersatu heading for wipeout" (analyst consensus) | PIR-06+16 | -0.70 | declining | PRIORITY |
| Kota (razor 135 margin, 3-cornered) | PIR-07 | -0.15 | stable | none |

### Positive NEW (full-text-confirmed)
| Entity | PIR | Score | Trend | Alert |
|---|---|---|---|---|
| BN-PN grassroots endorsement (FMT full text BM) | PIR-06 | +0.48 | improving | none |
| Lim Lip Eng (green-wave/Islamophobia counter) | PIR-16 | +0.35 | improving | none |
| N.27 Chembong (FMT full text, BN incumbent) | PIR-07 | +0.35 | improving | none |
| Zaifulbahri Idris (N.27 BN incumbent) | PIR-07 | +0.40 | stable | none |
| Datuk Mohd Isam (Tampin machinery-sharing, NST full text) | PIR-06 | +0.35 | stable | none |

### Revised (rev10 → rev11)
| Entity | Prior (rev10) | New (rev11) | Δ | Note |
|---|---|---|---|---|
| Muhyiddin Yassin | -0.84 | -0.86 | -0.02 | FMT full text "new coalition PN exit hint" + "charade" |
| Bersatu | -0.80 | -0.82 | -0.02 | FMT full-text analyst consensus reinforcement |
| "Bersatu exit imminent?" | -0.60 | -0.72 | -0.12 | **HARD-NEWS CORROBORATION (escalation tier)** |
| N.28 Klawang | +0.35 | +0.40 | +0.05 | full-text confirmed cousins, mature |
| Bakri Sawir | +0.40 | +0.45 | +0.05 | confident Day-1 |
| N.27 Chembong | +0.30 | +0.35 | +0.05 | FMT full text recovered |
| Anthony Loke | +0.45 | +0.50 | +0.05 | FMT full text "MCA biggest loser" offense |
| "MCA biggest loser" | -0.45 | -0.50 | -0.05 | MCA rebuttal = containment, defensive |
| Hadi Awang | -0.40 | -0.35 | +0.05 | inclusive coalition-building offsets blame-shift |
| Anwar Ibrahim | +0.40 | +0.42 | +0.02 | NST full text discipline + Ali Baba |
| BN-PN grassroots | +0.45 | +0.48 | +0.03 | FMT full text BM |
| makmal politik | +0.10 | +0.15 | +0.05 | FMT full text BM |
| "sole opposition" | -0.35 | -0.50 | -0.15 | deepens with PN-exit hint |
| "Ali Baba 40 thieves" | +0.30 | +0.35 | +0.05 | NST full text |
| "Mature campaign" | +0.35 | +0.40 | +0.05 | Awani full text |

---

## COLLECTION LIMITATIONS (honest disclosure)
- **Kiandee quorum attack (NST)**: headline-intelligence only (gnews JS-rendered; NST feed rotated past top-50). Sentiment at title-level inference. Full text requires NST feed rotation or JS-render.
- **mkini "Bersatu exit from PN imminent?" SNAPSHOT**: paywalled body — preview only. The FMT full-text Muhyiddin "new coalition" article provides the hard-news corroboration independently.
- **"barking dogs" (Albert Tei)**: full body NOT fetched (paywalled) — headline+description derived.
- **Melaka DAP withdrawal article bodies**: JS-rendered (Malay Mail) / paywalled (Star) — 7+ source headline-intel cluster meets multi-source corroboration for the basic fact only.
- **Director-list seats N.20 Bembang, N.25 Labu**: candidate detail still NOT recovered; "N.20 Bembang" <-> "Bahau" mapping unconfirmed. Tagged per director list verbatim. Honest limitation.
- **Score convention**: SIGNED per mission directive (rev1-9 used unsigned magnitude; rev10+ converted); cross-revision numeric comparisons require sign-aware reading.

---

## NEXT ACTIONS
1. **PIR-06 (HIGHEST):** Watch for Bersatu Supreme Council formal response to Kiandee's quorum question — a statement confirming/denying quorum would be threshold-adjacent. Monitor Muhyiddin evening statements for "new coalition" formalization (FMT full text already hints at PN exit — the next tier is a formal withdrawal statement). Watch the 8 Bersatu-vs-PN direct-clash seats for campaign friction.
2. **PIR-16 (HIGHEST):** Track whether "Bersatu exit imminent?" escalates from hard-news-corroboration tier to FORMAL withdrawal/pecat notice (the next tier — would fire Trigger #2). MCA rebuttal watch (Wee/Mah Hang Soon counter to Loke "biggest loser" — amplification). Track "Umno dangerous dance with PAS" opinion viral spread. Track "DAP coalition-intolerant" frame vs Lim Lip Eng counter across 13 non-Malay DUNs.
3. **PIR-07:** Capture evening ceramah for T1 seats — Klawang (cousins angle, high viral-risk), Linggi (Aminuddin), Sikamat, Chennah (Loke vs Siow), Rantau (Tok Mat). Monitor BN manifesto launch 24 Jul (DUN Linggi) for narrative shifts.
4. **Backfill the 20260716 sentiment-analysis gap** (1-day gap in time series).

---

## REVISION HISTORY

| Rev | MYT | Coverage | Verdict (abbreviated) |
|---|---|---|---|
| baseline | 18 Jul 08:31 | Nomination Day opens | opposition-fractured; PN-Bersatu split dominant; PH-favorable |
| rev2 | 18 Jul 16:33 | PN-Bersatu split three-way | mutual on-the-record confrontation |
| rev3 | 18 Jul 21:56 | 41 src / 150 ent | PN "has grounds to remove Bersatu" (Kiandee) |
| rev4 | 19 Jul 00:10 | 55 src / 232 ent | senior-figure public advocacy (Kiandee Utusan body) — CRITICAL PIR-06 |
| rev5 | 19 Jul 02:35 | 86 src / 264 ent | CRITICAL escalation to two/three-sided principal-level motion |
| rev6 | 19 Jul 05:04 | 86 src + 291 ent | CRITICAL CARRIED (consolidation): KINIGUIDE + "sole true opposition" + graft-trial |
| rev7 | 19 Jul 07:21 | + 220325/231029 | CRITICAL CARRIED (corroboration): NST "crossroads" + 7 ballot clashes |
| rev8 | 19 Jul 10:02 | + 011915 | CRITICAL CARRIED (operational-split): Kosmo "keluar daripada konsensus PN negeri" |
| rev9 | 19 Jul 12:30 | + 034922 (Day-1 midday) | CRITICAL CARRIED (viral-amplification: "imminent?" SNAPSHOT); NEW PIR-16 PRIORITY (ESC-016 Melaka +600%); Aminuddin revised UP; FIRST Day-1 walkabout (Loke) |
| rev10 | 19 Jul 15:10 | + 064654 (Day-1 afternoon, 18 full-text) | CRITICAL CARRIED + ESCALATED (internal-fracture signal sharp-negative: Kiandee quorum + analyst "perebutan kuasa"/wipeout consensus); NEW CRITICAL ESC-017 "Bersatu in disarray" viral amplification (>50% volume); NEW PRIORITY ESC-018 "MCA biggest loser" + ESC-019 AMH; N.28 Klawang gap FILLED; formal PN-MT notice STILL NOT DETECTED (8 passes) |
| **rev11** | **19 Jul 17:28** | **FULL 223-entity build (0714) — FMT 19 + NST 7 + Awani 3 full text** | **[CRITICAL ESCALATION TIER] PIR-16 hard-news corroboration of "Bersatu exit imminent?" (FMT full text Muhyiddin "new coalition PN exit hint") — escalates from rev10 viral-amplification tier; NEW PRIORITY ESC-020 "Umno dangerous dance with PAS" + ESC-021 "DAP coalition-intolerant" frame; full-text reinforcement of all three PIR-06 sides; N.27 Chembong/Kota/Paroi/Pertang full-text recovered; formal PN-MT notice STILL NOT DETECTED (9 passes)** |

---

## METHODOLOGY
- **Method:** Agent-manual source-attributed review (CVS-compliant) + SPR official candidate-list cross-reference + director-approved PIR priority weighting (PIR-06/07/16, 19 Jul 14:50 cycle, 3rd carry-forward) + collection_metadata trajectory assessment + verified 0714 full-text source files (FMT RSS 19 / NST WordPress 7 / Awani 3) + multi-source headline-intel clusters + entities-20260719-0714.json (223 entities) reconciliation.
- **Weighting:** PIR-06 × 2.0, PIR-16 × 1.8, PIR-07 × 1.3, non-priority × 1.0.
- **CVS standard:** Sentiment based on verified source content only. No pattern-inferred sentiment. All entities source-attributed (verbatim surface match). PIR priority pointer files + collection_metadata trajectory assessment used only to LOCATE items; media source files cited as attribution.
- **Signed score convention:** negative = -1.0 to -0.1; neutral = -0.1 to +0.1; positive = +0.1 to +1.0 (per mission directive).
- **PIR-06 CRITICAL logic:** the >30% numeric shift rule did NOT fire for any PIR-06 entity on the rev10→rev11 delta (max +2.5% Bersatu); the CRITICAL fires via the qualitative "Bersatu internal-fracture signal sharp-negative" rule (now full-text-reinforced: quorum + analyst consensus + Muhyiddin PN-exit hint) — clearly disclosed. Against the 20260718 baseline (48h), Bersatu shows sharp directional deepening with escalation tiers added.
- **PIR-16 CRITICAL logic (rev11):** the hard-news-corroboration rule FIRED — FMT full text corroborates "Bersatu exit imminent?" via Muhyiddin "new coalition after state election, hinting at a PN exit" = escalation tier. (The >50% viral-amplification rule had fired in rev10; now escalated.)

---

*End of summary — sentiment-20260719-1728.json (revision 11) — generated 2026-07-19T17:28:00+08:00 — TLP:AMBER*
