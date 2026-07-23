# PRN Negeri Sembilan 2026 — Entity Extraction Summary
## Date: 2026-07-23 (Campaign Day 5) — MORNING Cycle
**Extraction generated:** 2026-07-23 08:24 +08 (MYT)
**Brief ID:** PRN-NS-2026-ENT-20260723-0824
**Agent:** PRN Negeri Sembilan 2026 Entity Extraction Agent (Stage 2 of intelligence pipeline)
**Model:** zai-org/GLM-5.2
**Source:** `04-DATA-AND-SOURCES/raw-scrapes/20260723/` (morning collection, 06:00 MYT 23 Jul)
**Output:** `04-DATA-AND-SOURCES/processed-entities/20260723/entities-20260723-0824.json`
**Scratch:** `04-DATA-AND-SOURCES/scratch/_metadata_20260723_entities.json`

---

## Pipeline Position
- **Upstream:** Collection (06:00 MYT 23 Jul) — 7 files delivered (5 full-content articles + 1 headlines summary with 14 entries + 1 index). All NS-relevant; 0 non-NS skipped.
- **This stage:** Entity Extraction (08:00 MYT) — 42 entities extracted from 7 files.
- **Downstream:** Sentiment Analysis (10:00 MYT) — clean JSON provided; parse-ready.

---

## Headline Numbers
| Metric | Value |
|---|---|
| Articles in raw scrape | 7 (5 full + 1 headlines-14 + 1 index) |
| Articles processed | 7 |
| Non-NS skipped | 0 |
| **Total entities extracted** | **42** |
| — Persons | 12 |
| — Parties | 7 |
| — Seats | 7 |
| — Narratives | 16 |
| Priority: critical | 4 |
| Priority: priority | 33 |
| Priority: normal | 5 |
| PIR-06 entities | 9 |
| PIR-07 entities | 14 |
| PIR-16 entities | 19 |
| **PIR-06 [CRITICAL] threshold crossed** | **NO** |

---

## ⚠️ CRITICAL Threshold Monitoring — PIR-06
**STATUS: CLEAR — no Bersatu candidate withdrawal in NS Tier-4 seats.**

- Bersatu's solo-logo candidates remain STABLE — no `pecat`/`keluar`/`tarik diri` event reported at any Tier-4 seat this cycle.
- **DUN Labu (Tier-4):** PH candidate Ahmad Faez active (100 families/day target). Bersatu's Mohamad Hanifah 'foreigner' allegation from yesterday — still a sidebar, NOT a withdrawal.
- No PN-MT expulsion notice, no Kiandee quorum escalation, no RoS action against PN/Bersatu this cycle.
- The 4 CRITICAL entities this cycle are **narrative/operational** (Bersatu solo+MB-undecided, 'sokong BN' directive distance, Muhyiddin as Bersatu president), NOT candidate-withdrawal events.

---

## Key Entities by PIR

### PIR-06 — Coalition Operational Arrangement [CRITICAL — Consequence Monitoring]
**Persons:** Muhyiddin Yassin (CRITICAL — Bersatu president, MB undecided, distances from 'sokong BN'), Mohamed Khaled Nordin (dismissed Bersatu), Radzi Jidin (manifesto committee chair).
**Parties:** Bersatu (CRITICAL — solo, MB undecided), PN (denies weekend-change 'fitnah', 'ditinggalkan'), BN ('sokong BN' directive context).
**Key narratives:**
1. **Bersatu solo campaign / MB undecided** [CRITICAL] — first time under own name in NS; MB not decided; focus on winning seats first. [Utusan + Sinar x2]
2. **'Sokong BN' directive distance** [CRITICAL] — Muhyiddin: 'Saya tidak terlibat'; PN 'ditinggalkan begitu sahaja'; situation 'agak janggal'. Signals Bersatu-PN operational fracture. [Sinar + Utusan]
3. **Bersatu manifesto pending** — Radzi Jidin committee drafting; focus: ekonomi, infrastruktur, kesihatan, pendidikan, kebajikan. Launch in coming days. [Utusan + Sinar]
4. **PN denies weekend holiday change** — categorised 'fitnah'. [BHarian headline]

### PIR-07 — Highest-Priority NS Battlegrounds
**Persons:** Anwar Ibrahim (Sikamat dinner + Paroi ceramah), Aminuddin Harun (MB confirmed, service record), Bakri Sawir (PH Klawang — R&R + university Jelebu), Jalaluddin Alias (BN Pertang — 'hab intelek'), Ahmad Faez (PH Labu — 100 families/day), Fahmi Fadzil (campaign sabotage action).
**T1 seats with campaign events:**
- **Sikamat (N.13)** — Anwar unity dinner + Muhyiddin BGU ceramah (direct PH-vs-Bersatu clash venue)
- **Paroi (N.25)** — Anwar Ceramah Perdana PH, SARA announcement
- **Senawang** — Jelajah Kekal Harapan venue (Paroi area), SARA + Mat Sabu speeches
- **Ampangan (N.14)** — named by Anwar at Sikamat (evaluate Aminuddin's record)
- **Klawang (N.28)** — PH candidate Bakri Sawir (R&R + university pledge) [NEW]
- **Pertang (N.02)** — BN candidate Jalaluddin Alias ('hab intelek') [NEW]
- **Labu (N.20)** — PH candidate Ahmad Faez (100 families/day) [NEW]

### PIR-16 — Campaign Narrative Evolution [ELEVATED]
**Persons:** Anwar Ibrahim (multiple narratives), Aminuddin Harun (MB confirmed, manifesto implementation), Mohamad Sabu/Mat Sabu (anti-kahwin-cerai, anti-DAP-labeling), Muhammad Faiz Fadzil (anti-PAS), Johan Mahmood Merican (SARA/Treasury background).
**Parties:** PH (MB confirmed, manifesto implementation, stability), PAS (penyatuan Melayu tactic), DAP (labeling narrative + 'boneka DAP'), Amanah (Mat Sabu + Faiz Fadzil).
**Key narratives:**
1. **'We have a candidate AND a record'** — Anwar: 'Kita ada calon, kita ada rekod' vs opposition 'berebut, belum mampu umum'. Deliberate pairing with Bersatu's undecided MB. [Utusan]
2. **SARA increase / federal-state alignment** — SARA to be raised + aligned ('digabungkan') with NS. Economic welfare as campaign pillar. Aminuddin credited with public-servant bonus. [Utusan + Sinar]
3. **Bersatu 'here to win' counter-narrative** — Muhyiddin counters Khaled: 'Bukan nak kacau daun, kita masuk untuk menang.' [Sinar]
4. **Anti-corruption / anti-'sakau'** — Anwar integrity messaging at Paroi. [Utusan]
5. **'Tebuk atap' accusation** — opposition tried to topple NS govt early; not policy-driven but power-grab. [Utusan]
6. **Anti-party-hopping ('kahwin-cerai')** — Mat Sabu at Senawang. [Sinar headline]
7. **DAP labeling for votes** — Mat Sabu: 'Labelkan DAP jahat untuk dapat undi'. [Sinar 788993]
8. **'Boneka DAP' defense** — Anwar defends Aminuddin vs DAP-puppet accusation. [Awani headline]
9. **PAS 'penyatuan Melayu' tactic** — Faiz Fadzil: PAS uses Malay unity for power. [Sinar headline]
10. **MB bukan rebutan** — Anwar at Sikamat: MB position not a contest. [Sinar headline]
11. **Government stability** — 'Kerajaan Perpaduan kekal stabil' (Anwar, Senawang). [Sinar headline]

---

## Notable Developments vs Previous Cycle (22 Jul)

| Dimension | 22 Jul (dawn) | 23 Jul (morning) | Delta |
|---|---|---|---|
| Articles processed | 26 | 7 | ↓ (smaller batch — post-ceramah coverage) |
| Entities extracted | 72 | 42 | ↓ |
| Bersatu MB candidate | Undecided | **Still undecided** | No change [PIR-06 CRITICAL persists] |
| 'Sokong BN' directive | First reported (Hamzah) | **Muhyiddin distances: 'Saya tidak terlibat'** | ↑ Escalation — Bersatu president disavows |
| Aminuddin as MB | Implied/Anwar tour preview | **Explicitly confirmed by Anwar** | ↑ Crystallised |
| SARA increase | Not mentioned | **Announced, NS-aligned** | NEW |
| New T1 candidate pledges | — | Bakri Sawir (Klawang), Jalaluddin (Pertang), Ahmad Faez (Labu) | NEW x3 |
| Bersatu manifesto | Pending | **Still pending** (Radzi Jidin drafting) | No change — narrative FADING |
| Tier-4 withdrawal | CLEAR | **CLEAR** | No change |

---

## Downstream Guidance for Sentiment Analysis (10:00 MYT)
1. **PH confidence axis:** Anwar/Aminuddin — 'confirmed MB + record + federal-state benefits (SARA)'. Expect positive/assured sentiment.
2. **Bersatu vulnerability axis:** Muhyiddin — 'undecided MB + distances from PN + solo first-timer'. Expect defensive/assertive-but-exposed sentiment.
3. **PH↔BN tension:** Khaled Nordin's dismissal of Bersatu + 'sokong BN' directive — intra-unity-government friction persisting but not escalating to candidate level.
4. **Anti-racial-politics cluster:** Mat Sabu (DAP labeling) + Faiz Fadzil (PAS Malay unity) + Anwar (boneka DAP defense) — coordinated PH counter-narrative to racial framing.
5. **Headline-only entities** (14 entries): Full content blocked by antibot — sentiment should use headline-level signals only and flag lower confidence.

---

## Files
- `entities-20260723-0824.json` — 42 entities, parse-ready JSON
- `summary.md` — this file
- Scratch: `04-DATA-AND-SOURCES/scratch/_metadata_20260723_entities.json`
