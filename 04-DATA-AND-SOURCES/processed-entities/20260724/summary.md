# PRN Negeri Sembilan 2026 — Entity Extraction Summary
## Date: 2026-07-24 (Campaign Day 7) — MORNING Cycle
**Extraction generated:** 2026-07-24 08:29 +08 (MYT)
**Brief ID:** PRN-NS-2026-ENT-20260724-0829
**Agent:** PRN Negeri Sembilan 2026 Entity Extraction Agent (Stage 2 of intelligence pipeline)
**Model:** zai-org/GLM-5.2
**Source:** `04-DATA-AND-SOURCES/raw-scrapes/20260724/` (morning collection, 06:00 MYT 24 Jul)
**Output:** `04-DATA-AND-SOURCES/processed-entities/20260724/entities-20260724-0829.json`
**Scratch:** `04-DATA-AND-SOURCES/scratch/_build_entities_20260724_0829.py`

---

## Pipeline Position
- **Upstream:** Collection (06:00 MYT 24 Jul) — 16 files delivered (14 full-content articles + 1 headlines summary with 7 entries + 1 index). All NS-relevant; 0 non-NS skipped.
- **This stage:** Entity Extraction (08:00 MYT) — 76 entities extracted from 15 files.
- **Downstream:** Sentiment Analysis (10:00 MYT) — clean JSON provided; parse-ready.

---

## Headline Numbers
| Metric | Value |
|---|---|
| Articles in raw scrape | 16 (14 full + 1 headlines-7 + 1 index) |
| Articles processed | 15 |
| Non-NS skipped | 0 |
| **Total entities extracted** | **76** |
| — Persons | 26 |
| — Parties | 10 |
| — Seats | 13 |
| — Narratives | 27 |
| Priority: critical | 1 |
| Priority: priority | 57 |
| Priority: normal | 18 |
| PIR-06 entities | 25 |
| PIR-07 entities | 21 |
| PIR-16 entities | 30 |
| **PIR-06 [CRITICAL] threshold crossed** | **NO** |

---

## ⚠️ CRITICAL Threshold Monitoring — PIR-06
**STATUS: CLEAR — no Bersatu candidate withdrawal in NS Tier-4 seats.**

- Bersatu's solo-logo candidates remain STABLE — no `pecat`/`keluar`/`tarik diri` event reported at any Tier-4 seat this cycle.
- No PN-MT expulsion notice, no Kiandee quorum escalation, no RoS action against PN/Bersatu this cycle.
- The 1 critical-priority entity this cycle is the **BN-PN merged-manifesto operational escalation** (consequence-monitoring milestone — highest-level cooperation confirmation yet), NOT a candidate-withdrawal event.
- **Notable PIR-06 shift:** the prior cycle's "'sokong BN' directive distance" fracture (Muhyiddin: 'saya tidak terlibat') has been **partially RESOLVED** — cross-voting is now formally EMBRACED by both BN and PN. The fracture now isolates **Bersatu** (excluded from the merged manifesto, running solo 24 seats).

---

## Key Entities by PIR

### PIR-06 — Coalition Operational Arrangement [CRITICAL — Consequence Monitoring]
**Persons:** Annuar Musa (merged-manifesto confirmation, shared-ceramah blueprint), Mohamad Hasan (BN manifesto launch, MB deferral), Muhyiddin Yassin (Bersatu solo, excluded), Radzi Jidin (Bersatu manifesto pending), Idris Ahmad (PAS VP, PN lampiran), Mahdzir Khalid (BN Kedah, cross-state machinery), Muhammad Saifullah Ali (UMNO Youth dissent), Wan Saiful Wan Jan (Wawasan bridge), Mazalan Maarop (UMNO Seremban).
**Parties:** BN (25 seats, merged manifesto), PN (11 seats, lampiran), Bersatu (24 solo, EXCLUDED), PAS (PN lead, policy alignment), Wawasan (4 seats, Bersatu splinter).
**Seats:** Bagan Pinang, Lukut (joint nomination), Mambau, Gemas (Wawasan).
**Key narratives:**
1. **BN-PN merged manifesto (ONE document)** [CRITICAL] — highest-level cooperation; cross-voting directive; Bersatu excluded. Resolves prior 'sokong BN' tension. [FMT + Harian Metro + Utusan]
2. **BN-PN shared campaign machinery** — shared ceramah stages, markas, simultaneous intros, grand finale joint address. [Utusan]
3. **Cross-voting directive (BN↔PN)** — both sides direct supporters to vote each other's candidates. Now EMBRACED (was distanced prior cycle). [FMT + Utusan]
4. **PN 'lampiran' manifesto** — PN supplements BN manifesto; PAS VP reviews & aligns. [Harian Metro]
5. **Bersatu solo / excluded** — NOT part of merged manifesto; manifesto pending; first time own name; projected 2 of 24 seats. [Kosmo + Malay Mail]
6. **Internal UMNO dissent** — Youth exco: 'sokongannya masih samar-samar'; 'gelombang hari ini adalah gelombang BN'. [Kosmo]
7. **Wawasan as 'bridge'** — 4 seats, Bersatu splinter vs parent party. [TRP]

### PIR-07 — Highest-Priority NS Battlegrounds
**Persons:** Nor Azman Mohamad (PH Sikamat), Razali Abu Samah (PN/Wawasan Sikamat), Tun Faisal Ismail Aziz (Bersatu Sikamat), Zaifulbahri Idris (BN Chembong), Abu Ubaidah Redza (former ADUN Ampangan), Dr Kelvin Goh (Vodus).
**T1 seats with campaign events:**
- **Sikamat (N.13)** — full 3-cornered fight confirmed (PH vs PN/Wawasan vs Bersatu); 34,103 voters; Aminuddin's legacy seat; BGU Bersatu venue [MOST WATCHED]
- **Linggi (N.32)** — Aminuddin's new constituency; PH manifesto context; voter cost-of-living voice
- **Paroi (N.25)** — first-time voter on employment; prior Anwar ceramah venue
- **Ampangan (N.14)** — former ADUN at PN lampiran event
- **Nilai (N.10)** — Nilai AI City project (Aminuddin vision)
- **Klawang (N.28)** — Wawasan seat; prior PH candidate pledge (Bakri Sawir)
- **Rantau** — Mohamad Hasan's base
- **Chembong** — Zaifulbahri (BN incumbent), campaign trail
- **Mambau, Gemas** — Wawasan seats
- **Bagan Pinang, Lukut** — joint BN-PN nomination
**Key narrative:** Vodus projection (hung assembly possible), 22,339 PDRM/ATM early voters (28 Jul).

### PIR-16 — Campaign Narrative Evolution [ELEVATED]
**Persons:** Aminuddin Harun (economic corridor vision, anti-retorik), Khalid Abdul Samad (perpaduan ummah counter), Fahmi Fadzil, Cha Kee Chin, Onn Hafiz Ghazi (favourability benchmark), Zahid Hamidi (Unity Govt defense), voter voices (Nurulainee, Najmi Aiman, Kamarulzaman, Lim Kian, M. Manisha).
**Parties:** PH (Kekal Harapan, anti-retorik), Amanah (Khalid Samad), DAP (perpaduan ummah concern), Calon Bebas (7-point manifesto).
**Key narratives:**
1. **'Sambung Yang Tergendala'** — BN nostalgia for pre-2018 governance; denies Sabah plagiarism. [UMNO Online]
2. **'Kekal Harapan' / 10 commitments** — PH anti-retorik, realistic & implementable, 8-year record. [Utusan]
3. **'Bukan lagi negeri laluan'** — Aminuddin 4-wilayah economic corridor, 6 strategic projects. [Awani]
4. **Anwar-Aminuddin partnership** — federal-state alignment delivers development. [Awani + Utusan]
5. **'Perpaduan ummah' PH counter** — framed as threat to multiracial harmony (Khalid Samad). [Kosmo]
6. **'Perpaduan ummah / penyatuan bangsa' BN-PN** — inclusive Malay-Muslim unity (Mahdzir). [Harian Metro]
7. **'Kuasa untuk laksanakan kebaikan'** — Annuar reframes power as virtue. [FMT]
8. **BN trust advantage (45% vs 19%)** — strategic asset despite vote deficit. [Malay Mail + Sinar]
9. **Aminuddin low favourability (31.7%)** — vs Johor MB 58.1%; leadership perception challenge. [Malay Mail]
10. **Voter volatility: 30% movable / 51% very likely to vote** — turnout risk. [Malay Mail]
11. **Voters want 'leaders who can get things done'** — competence over rhetoric; aligns with PH. [Malay Mail]
12. **Mohamad Hasan MB deferral** — 'Let we pass the post first'. [UMNO Online]
13. **Bersatu manifesto pending (isu rakyat)** — economy, infrastructure, health, education; FADING. [Kosmo]
14. **Zahid-Anwar pantun exchange** — Unity Govt defense. [headline-only]

---

## Notable Developments vs Previous Cycle (23 Jul)

| Dimension | 23 Jul (morning) | 24 Jul (morning) | Delta |
|---|---|---|---|
| Articles processed | 7 | 15 | ↑ (manifesto-week batch) |
| Entities extracted | 42 | 76 | ↑ |
| BN-PN cooperation | Shared ceramah blueprint | **MERGED manifesto into ONE document** | ↑ MAJOR escalation |
| 'Sokong BN' directive | Muhyiddin distanced ('saya tidak terlibat') | **Embraced by both BN & PN** (cross-voting formalized) | ↑ Resolved (Bersatu now isolated) |
| Bersatu status | Solo, MB undecided, manifesto pending | **STILL solo, manifesto STILL pending, EXCLUDED from merged manifesto** | No change — FADING |
| Bersatu Tier-4 withdrawal | CLEAR | **CLEAR** | No change |
| PH manifesto | Launched (21 Jul) | **'Kekal Harapan' detail + anti-retorik strategy** | Crystallised |
| BN manifesto | Pending | **'Sambung Yang Tergendala' launched 24 Jul (TODAY)** | NEW |
| Survey data | — | **Vodus (437 voters): PH 17/BN 15/PN 2, hung assembly, trust gap, favourability** | NEW (quantitative) |
| Sikamat field | Anwar dinner + Muhyiddin BGU | **Full 3-cornered confirmed (Nor Azman/Razali/Tun Faisal), 34,103 voters** | Crystallised |
| Internal UMNO dissent | — | **Youth exco cautions BN-PN premature** | NEW |
| Wawasan | — | **4 seats (Klawang/Sikamat/Mambau/Gemas), bridge positioning** | NEW |
| Early voting | — | **22,339 PDRM/ATM, 28 Jul** | NEW |

---

## Downstream Guidance for Sentiment Analysis (10:00 MYT)
1. **BN-PN 'unified front' axis:** Merged manifesto + cross-voting + shared machinery = highest cooperation confidence. Expect positive/assured sentiment for BN & PN; note Bersatu EXCLUSION as tension.
2. **Bersatu vulnerability axis:** Excluded from merged manifesto + solo + manifesto pending + MB undecided + projected 2 of 24 seats. Expect defensive/isolated sentiment; underdog framing (Muhyiddin caution).
3. **PH confidence axis:** Aminuddin economic corridor vision + anti-retorik + confirmed MB + Vodus seat lead (17). But LOW favourability (31.7%) and trust deficit (19% vs BN 45%) = vulnerability to track.
4. **Narrative duel — 'perpaduan ummah':** BN-PN (inclusive 'penyatuan bangsa') vs PH (threat to multiracial harmony). Intensifying; sentiment should weight both framings.
5. **Vodus quantitative axis:** Trust gap (BN 45% vs PH 19%), favourability gap (Aminuddin 31.7% vs Johor 58.1%), 30% movable voters, 51% turnout intent = leading sentiment data points.
6. **Internal UMNO dissent:** Saifullah's 'belum sesuai' = grassroots friction signal; track for escalation vs absorption.
7. **Headline-only entities** (7 entries): Full content blocked by antibot — sentiment should use headline-level signals only and flag lower confidence.

---

## Files
- `entities-20260724-0829.json` — 76 entities, parse-ready JSON
- `summary.md` — this file
- Scratch: `04-DATA-AND-SOURCES/scratch/_build_entities_20260724_0829.py`
