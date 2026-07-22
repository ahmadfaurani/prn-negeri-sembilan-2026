# PRN Negeri Sembilan 2026 — Entity Extraction Summary
## Date: 2026-07-22 (Campaign Day 4) — DAWN Cycle
**Extraction generated:** 2026-07-22 08:22 +08 (MYT)
**Brief ID:** PRN-NS-2026-ENT-20260722-0822
**Agent:** PRN Negeri Sembilan 2026 Entity Extraction Agent (Stage 2 of intelligence pipeline)
**Model:** zai-org/GLM-5.2
**Source:** `04-DATA-AND-SOURCES/raw-scrapes/20260722/` (dawn collection, 06:00 MYT 22 Jul)
**Output:** `04-DATA-AND-SOURCES/processed-entities/20260722/entities-20260722-0822.json`
**Scratch:** `04-DATA-AND-SOURCES/scratch/extract-entities-20260722-0822.py`

---

## Pipeline Position
- **Upstream:** Collection (06:00 MYT) — 26 NS-relevant articles kept (69 false positives quarantined).
- **This stage:** Entity Extraction (08:00 MYT) — 72 entities extracted from 26 articles.
- **Downstream:** Sentiment Analysis (10:00 MYT) — clean JSON provided; parse-ready.

---

## Headline Numbers
| Metric | Value |
|---|---|
| Articles in raw scrape | 26 |
| Articles processed | 26 |
| Non-NS skipped | 0 (collector pre-filtered 69 false positives) |
| **Total entities extracted** | **72** |
| — Persons | 30 |
| — Parties | 13 |
| — Seats | 14 |
| — Narratives | 15 |
| Priority: critical | 2 |
| Priority: priority | 46 |
| Priority: normal | 24 |
| PIR-06 entities | 30 |
| PIR-07 entities | 25 |
| PIR-16 entities | 17 |
| **PIR-06 [CRITICAL] threshold crossed** | **NO** |

---

## ⚠️ CRITICAL Threshold Monitoring — PIR-06
**STATUS: CLEAR — no Bersatu candidate withdrawal in NS Tier-4 seats.**

- Bersatu's **24 solo-logo candidates remain STABLE** — no `pecat`/`keluar`/`tarik diri` event at any Tier-4 seat.
- **DUN Labu (Tier-4):** Bersatu candidate **Mohamad Hanifah** faces only a "Saya bukan warga asing" (foreigner) allegation — **sidebar only** (standalone fetch failed per collector index). NOT a withdrawal.
- The **"pecat menteri BN"** exchange (Zahid ↔ Anwar ↔ Aminuddin) concerns **federal ministers / unity-government ties** — correctly tagged **PIR-16**, NOT a PIR-06 Tier-4 candidate-withdrawal event.
- The **"tarik balik sokongan"** reference (FMT) is the **HISTORICAL** event — 14 Umno ADUN withdrew support for MB Aminuddin over the royal dispute, which triggered DUN dissolution. Not a new withdrawal.
- No PN-MT expulsion notice, no Kiandee quorum escalation, no RoS action against PN/Bersatu this cycle.

---

## Key Entities by PIR

### PIR-06 — Coalition Operational Arrangement [CRITICAL — Consequence Monitoring]
**Persons:** Ahmad Maslan (BN-PN 25-seat target), Abdul Hadi Awang (PAS two-mode strategy), Mohd Yussof Latiff (Bersatu-disband call), Muhyiddin Yassin (marginalized Bersatu leader), Mohd Isam Mohd Isa (BN Tampin → Wawasan Gemas), Hamzah Zainudin (Wawasan president / PN sec-gen at BN-PN ceramah), Takiyuddin Hassan (PAS sec-gen), Rafizi Ramli (Bersama, skipping NS), Abbas Azmi (Amanah, "kacau undi PH"), Tony Pua.
**Parties:** BN (25 DUN), PN (11 DUN), Bersatu (24 solo — CRITICAL entity), PAS (attacker NS), UMNO (rapprochement), Wawasan, Bersama, Amanah, DAP, MCA, Gerakan, MIPP.
**Seats:** DUN Labu (Tier-4 — monitoring), Tampin (BN-PN ceramah).
**Key narratives:**
1. **BN-PN 25-seat target** (Ahmad Maslan) — BN-PN understanding delivers 25/36 + state govt; strategic/tactical to avoid Malay vote split. [FMT EN+BM, HarianMetro]
2. **PAS two-mode strategy** (Hadi) — goalkeeper in Johor, attacker in NS; PH rule + "extreme DAP" + "drifting Malays"; BN-PN without Bersatu, zero clashes. [Utusan, FMT]
3. **Bersatu-disband call** (Mohd Yussof) — dissolve Bersatu, return to UMNO; 0 Johor seats; solo NS harder. [HarianMetro, Utusan]
4. **Bersatu solo = PAS-UMNO rapprochement consequence** — Bersatu marginalized, "traitor" splinter, no future solo. [HarianMetro, Utusan]
5. **Parti Bersama skipping NS** (focus Melaka) — removes a PH-vote-split variable. [Sinar]

### PIR-07 — Highest-Priority NS Battlegrounds
**Persons:** Anwar Ibrahim (first NS tour), Aminuddin Harun (PH chairman/MB, DUN Linggi), Mohd Fairuz Mohd Isa (PN incumbent DUN Serting), Ridzuan Ahmad (Wawasan DUN Gemas), Islah Wahyudi Zainudin (independent DUN Sri Tanjung, charged), G. Manivannan (PH DUN Jeram Padang), Dr G Rajasekaran (PH incumbent DUN Sri Tanjung), A Achuthan (BN), M Leevineshwaraan (Bersatu), A Saravanan (independent), Zabidi Ariffin (PN 2023), Mohamad Hanifah (Bersatu DUN Labu), Koh Kim Swee (MCA DUN Repah).
**T1 seats with campaign events:** DUN Ampangan (N.14), DUN Paroi, DUN Sikamat (N.13), DUN Sri Tanjung (N.33), DUN Linggi (N.32) — all flagged PRIORITY.
**Other seats:** DUN Jeram Padang, DUN Serting (Jempol), DUN Gemas (Tampin), DUN Repah, Port Dickson, Tampin, Seremban, Senawang.
**Key narrative:** Anwar's first NS campaign tour (Wed 22 Jul) across 4 locations; election timeline confirmed (advance 28 Jul, polling 1 Aug).

### PIR-16 — Campaign Narrative Evolution [ELEVATED]
**Persons:** Ahmad Zahid Hamidi (pecat challenge, govt-assets rebuttal, underdog, 50k jobs), Steven Sim (PH manifesto), Hisommudin Bakar (Ilham — royal issue fading), Mujibu Abd Muis (UiTM — voter pragmatism), Syaza Shukri (IIUM — Umno-punished counter-narrative), Mubarak Dohak (royal crisis trigger), Tuanku Muhriz (YDPB).
**Key narratives:**
1. **Govt-assets controversy** — PH/Aminuddin (sparked by Manivannan, DUN Jeram Padang) accuses BN → Zahid "others also use, I have records" → Aminuddin "tak wajar". Multi-day PH↔BN tension within unity govt. [FMT×4, Utusan×2]
2. **Zahid "pecat menteri BN" challenge** — dared Anwar to sack 8 BN ministers; Aminuddin "uncalled for". [Utusan, FMT×2]
3. **PH Manifesto (10 commitments)** — achievement-based, not "janji kosong"; 30k jobs, 20k homes, PD International Port, Senawang-Port Klang Bypass, Seremban Sentral, TUB. [Utusan]
4. **BN Manifesto (pending)** — 50k NS jobs, halal hub, "better than PH"; final stages. [Utusan, FMT]
5. **BN "underdog" narrative** — 14 DUN pre-dissolution; machinery sharpening. [HarianMetro, Utusan]
6. **Royal/Undang issue FADING** — voters NOT linking royal crisis with polls; 3R avoided. [FMT×2, HarianMetro]
7. **Voter pragmatism** — Mujibu/UiTM: candidate credibility > party brand; Johor momentum not guarantee. [HarianMetro]

---

## Notes for Downstream (Sentiment Analysis — 10:00 MYT)
1. **Watch PH↔BN unity-govt tension** — the govt-assets + pecat-menteri exchange is escalating (multi-day, multi-outlet). Aminuddin's "tak wajar" + "isu dalaman BN-PN" framing is the sharpest PH critique of BN this cycle.
2. **Bersatu-solo narrative increasingly negative** — "bubar Bersatu", "traitor splinter", "0 Johor seats", "may lose all + deposits". Sentiment toward Bersatu should read strongly negative.
3. **BN-PN cooperation sentiment strongly positive (BN/PAS side)** — Hadi's "attacker" framing, Mohd Fairuz "alhamdulillah", Mohd Isam "BN akan tetap mendukung PN di Gemas". Joint-machinery optimism.
4. **Royal-issue narrative fading** — Hisommudin (detachment) vs Syaza (punishment) tension; sentiment should reflect voter detachment, not active anger.
5. **Sri Tanjung independent (Islah) — legal jeopardy** — Section 233 charge; sentiment neutral-to-negative around the candidate, distinct from the 5-cornered electoral contest.
6. **Labu (Tier-4) data gap** — "foreigner" allegation is sidebar-only (fetch failed). Flag as incomplete for sentiment; do not over-weight.

## Notes for Brief (12:00 MYT)
- No CRITICAL (no Tier-4 withdrawal). Bersatu 24 solo candidates stable.
- Key development: **Anwar's first NS campaign tour (Wed 22 Jul)** across Ampangan/Paroi/Sikamat (T1) + **BN-PN 25-seat claim** + **PH & BN manifestos launching**.
- Election dates confirmed: advance voting 28 Jul, polling 1 Aug.
- Escalating PH↔BN unity-govt friction (govt-assets + pecat-menteri) is the dominant PIR-16 narrative thread to watch through polling day.

---

## Entity Type & Priority Breakdown
```
Type:       person=30  party=13  seat=14  narrative=15  (TOTAL 72)
Priority:   critical=2  priority=46  normal=24
PIR tag:    PIR-06=30  PIR-07=25  PIR-16=17
```
**Critical-priority entities (2):**
1. `DUN Labu (Tier-4)` — PIR-06 monitoring seat (Bersatu candidate "foreigner" allegation, sidebar-only, no withdrawal).
2. `PIR-06 [CRITICAL] threshold — STILL CLEAR (no Tier-4 withdrawal)` — threshold-monitoring narrative.

## Source Outlets (corroboration map)
- **FMT** (EN+BM) — 10 articles (several are EN/BM pairs of same story)
- **HarianMetro** — 6 articles
- **Utusan** — 6 articles
- **Sinar** — 4 articles (refetched)
- **Awani** — 1 article (Anwar tour, corroborated by HarianMetro)
- Multi-outlet corroboration: Ahmad Maslan 25-seat claim (FMT×3); pecat-menteri (FMT×3 + Utusan); govt-assets (FMT×2 + Utusan×2); Sri Tanjung charge (FMT×3 + HarianMetro + Sinar).

---

*End of summary — PRN Negeri Sembilan 2026 Entity Extraction, dawn cycle Day 4, 2026-07-22 08:22 MYT.*
