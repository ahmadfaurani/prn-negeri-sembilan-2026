# PRN Negeri Sembilan 2026 — Entity Extraction Summary

**Date:** 2026-07-19 (Sunday)
**Current build timestamp (UTC):** 2026-07-19T07:19:00+00:00  |  **MYT:** 2026-07-19 15:19
**Agent:** PRN NS 2026 Entity Extraction Agent (scheduled cron)
**Director-approved cycle:** 19 Jul 2026 (PIR-06, PIR-07, PIR-16)
**Classification:** TLP:AMBER
**Current output file:** `processed-entities/20260719/entities-20260719-0714.json` (223 entities, valid JSON, lint-passed, 114,922 bytes)
**Prior output file (superseded, retained):** `processed-entities/20260719/entities-20260719-0507.json` (167 entities)

---

## 0. Build history (this folder)

| Build | File | Entities | Cycles ingested | Notes |
|---|---|---|---|---|
| 02:12 UTC | `entities_021231.json` | (delta, prior) | 011915 | pre-existing, untouched |
| 03:49 UTC | `entities_034922_delta.json` | (delta, prior) | 024042/034922 | pre-existing, untouched |
| 05:07 UTC | `entities-20260719-0507.json` | 167 | 011915/024042/034922 | consolidated first pass |
| **07:14 UTC** | **`entities-20260719-0714.json`** | **223** | **+ 051226 / 064654** | **CURRENT — this build** |

This build adds **56 new entities** and applies **23 context upgrades** to existing entities, driven by the largest single-day full-text gain to date: **FMT RSS (19 full-text articles)**, **NST WordPress feed (7 full-text)**, and **Astro Awani direct (3 full-text)**.

---

## 1. Scope & ingestion (current build)

Ingested **all content** in `04-DATA-AND-SOURCES/raw-scrapes/20260719/` across **5 scrape cycles** (011915, 024042, 034922, 051226, 064654 UTC), spanning **9+ source outlets** (FMT, NST, Astro Awani, Malaysiakini, Malay Mail, Kosmo, Utusan, The Star, Newswav/GNews mirrors) plus the collection `index.md`. **~30 priority-tagged articles read in full** in the current build; aggregate source scrapes scanned title-by-title for entity mentions.

**New full-text sources unlocked this build (this substantially closes the prior "JS-render blocker" gap):**
- **FMT (freemalaysiatoday.com)** — curl-friendly RSS (`content:encoded`) + direct article pages. 19 full-text articles recovered, the largest single-day full-text gain. Both EN and BM streams.
- **NST (nst.com.my)** — WordPress RSS feed (`content:encoded`, latest 50). 7 full-text articles.
- **Astro Awani (astroawani.com)** — direct-fetch via `berita-politik` slug. 3 full-text articles.

---

## 2. Headline numbers (current build)

| Metric | Count |
|---|---|
| **Total entities extracted** | **223** (167 prior + 56 new) |
| CRITICAL (PIR-06 termination-adjacent) | 10 |
| PRIORITY (PIR-07 battleground / PIR-16 viral-amplifier) | 45 |
| Normal | 168 |
| By type — person | 114 |
| By type — narrative | 50 |
| By type — seat | 36 |
| By type — party | 23 |
| By PIR — PIR-06 (Coalition Operational Arrangement) | 51 |
| By PIR — PIR-07 (Highest-Priority Battlegrounds) | 113 |
| By PIR — PIR-16 (First Dominant Campaign Narratives) | 59 |

---

## 3. CRITICAL entities — PIR-06 (Coalition Operational Arrangement)

**Threshold status: NOT CROSSED.** No formal PN-MT (Majlis Tertinggi) removal notice for Bersatu was detected across the 5 cycles (~5,513 titles scanned). Bersatu's operational split is **FULL TEXT confirmed** (24 own-logo seats; PAS severed political ties June 8). The formal "pecat" threshold has **not** been crossed, but the **CRITICAL precursor cluster is now 5 signals strong** (was 3 in the prior build):

| # | Entity | Type | Signal & what's new this build |
|---|---|---|---|
| 1 | **"toxic PN" claim** | narrative | FULL TEXT confirmed via FMT (18 Jul 12:48 MYT). Muhyiddin attributes "PAS made PN toxic"; Hadi DENIES and BLAMES Bersatu ("rift caused by Bersatu's misconduct"). Claim/counter-claim = strongest internal-rupture discourse. |
| 2 | **"PN has grounds to remove Bersatu" (Kiandee)** | narrative | Bersatu VP Kiandee's "asas kukuh" call (precursor, prior build). |
| 3 | **Ridzuan Ahmad quits Bersatu** | narrative | CONFIRMED "keluar" signal — former Gemas incumbent resigned as Bersatu division chief and quit the party; now contesting Gemas under Wawasan (PN). |
| 4 | **Kiandee quorum question** ⭐NEW | narrative | NEW ESCALATION (NST headline-intel, 19 Jul): Kiandee asks Muhyiddin if Bersatu Supreme Council still has quorum — from "grounds to remove" to "is the decision-making body even functional?" Director-flagged "termination"-adjacent. |
| 5 | **Muhyiddin new coalition after state election** ⭐NEW | narrative | FULL TEXT via FMT (19 Jul 09:00 MYT): "Muhyiddin said the party will form a new coalition after the state election, hinting at a PN exit." **Strongest pre-threshold signal.** |
| 6 | **Hadi denies PAS made PN toxic, blames Bersatu** ⭐NEW | narrative | FULL TEXT FMT (18 Jul 12:48 MYT) — the Hadi side of the claim/counter-claim, made distinct. |

**CRITICAL persons (carriers):**
- **Muhyiddin Yassin** (Bersatu president / PN chairman) — now FULL TEXT: "Bersatu must survive as lone opposition" (FMT 18 Jul 16:52) + "new coalition after state election, hinting at PN exit" (FMT 19 Jul 09:00) + "charade to deceive the Malays" counter to Malay-unity framing.
- **Hadi Awang** (PAS president) — now FULL TEXT: denies PAS made PN toxic, blames Bersatu (FMT 18 Jul 12:48); "more than marriage" (FMT BM 19 Jul); "Malay-Muslim unity with non-extreme partners incl MCA, MIC" (NST 19 Jul 14:03). Jempol nomination (Serting, Palong, Jeram Padang, Bahau).
- **Ronald Kiandee** (Bersatu VP) — "asas kukuh" removal call + NEW quorum-question escalation.
- **Ridzuan Ahmad** — quit Bersatu, now Wawasan/PN candidate in Gemas.

**Watch entities carried per director list:** Hamzah Zainudin, Annuar Musa, PN-MT, PAS Supreme Council, Bersatu Supreme Leadership — no new direct quotes this build; the Bersatu Supreme Council is now the subject of Kiandee's quorum question (watch for formal response).

**PIR-06 Tier-4 seats (director list):** no candidate withdrawals detected across N.04, N.05, N.13, N.14, N.23, N.25, N.31, N.34. **N.14 Ampangan candidate CONFIRMED** via Awani teka-teki (16 Jul): PN = Mohamad Rafie Ab Malek (director-flagged "Rafie"). N.13 Sikamat and N.14 Ampangan carry the highest messaging-war load.

---

## 4. PRIORITY entities — PIR-07 (Highest-Priority Battlegrounds)

### Defector-framing & complacency narratives (director-flagged)
- **Aminuddin Harun (outgoing MB)** — moved from long-held Sikamat to Linggi (BN stronghold); denies "fleeing Sikamat", frames as strategic choice. Also PIR-16 "MB after PRN" referendum figure.
- **"fleeing Sikamat" narrative** — director-flagged defector-framing entity, active.
- **"Linggi stronghold cannot be taken for granted"** — director-flagged "not taking for granted" entity, carried by BN's Faizal Ramli camp. (NST headline-intel this build: "Linggi move is risky for PH, says analyst" — adds analyst-layer confirmation.)

### Director-listed highest-priority battleground seats (10 seats)
N.13 Sikamat, N.14 Ampangan, N.15 Juasseh, N.28 Klawang, N.32 Linggi, N.27 Chembong, N.20 Bembang, N.25 Labu, N.10 Nilai, N.33 Sri Tanjung — all tagged PRIORITY.

**Recovery status (UPDATED this build — two more seats recovered):**
- **Full candidate roster recovered** for N.13 Sikamat (3-cornered), N.14 Ampangan (Rafie CONFIRMED via Awani teka-teki), N.32 Linggi (3-cornered MB battle: Aminuddin vs Faizal Ramli vs Zamri), N.10 Nilai (5-cornered), N.33 Sri Tanjung (5-cornered), N.15 Juasseh (BN "unfazed" by 3-cornered).
- ⭐ **N.28 Klawang NOW RECOVERED** (Awani full text, 19 Jul 12:11 MYT) — 3-cornered: PH incumbent **Datuk Bakri Sawir** vs PN's **Danni Rais** (Bakri's COUSIN) vs Bersatu's **Muhammad Adib Musa**. 13,355 voters. Day-1 "two cousins face off" marquee storyline at Pasar Minggu Kuala Klawang (Jelebu) — met peacefully, mature-campaign framing. **Highest PIR-07 value this build.**
- ⭐ **N.27 Chembong NOW RECOVERED** (FMT Tok Mat article, 18 Jul) — straight fight: BN's **Zaifulbahri Idris** (since 2008; 2023 maj 4,335) vs PH's **Danish Nazran Murad**.
- **Candidate detail NOT recovered** for N.20 Bembang, N.25 Labu — kept verbatim per director list. Honest limitation: the full Malay Mail nomination-lineup text recovered named "Bahau" (DAP Teo Kok Seong vs MCA Chong Fui Ming) — whether director-list "N.20 Bembang" maps to "Bahau" is **unconfirmed**. Both tags retained.

### Director-flagged candidates
- **Nazri Kassim** (PH, N.14 Ampangan) and **Datuk Dr Mohamad Rafie Ab Malek** "Rafie" (PN, N.14 Ampangan) — Day-1 messaging war: PH "defector" vs PN "experienced rep".
- **Datuk Mohd Faizal Ramli** (BN, N.32 Linggi) — director-flagged "Faizal Ramli" entity; carrier of "not taking for granted" framing vs MB Aminuddin.
- ⭐ **Danni Rais** (PN, N.28 Klawang) + **Datuk Bakri Sawir** (PH, N.28 Klawang) + **Muhammad Adib Musa** (Bersatu, N.28 Klawang) — NEW director-listed-seat candidates recovered this build.
- ⭐ **Zaifulbahri Idris** (BN, N.27 Chembong) + **Danish Nazran Murad** (PH, N.27 Chembong) — NEW director-listed-seat candidates recovered this build.

### Seat-profile data recovered this build (demographics, majorities)
- **Rantau** (FMT): Tok Mat vs Dr Azizul Hakim; 2023 maj 10,280; Malay 54.8% / Indian 27.6% / Chinese 16%.
- **Kota** (FMT): BN Suhaimi Aini vs PH Allif Ibrahim vs Bersatu Akmal Noradzmi; **2023 maj 135** (razor margin; never left Umno since 1959).
- **N.10 Nilai** (FMT): DAP J. Arul Kumar (4th term, 2023 maj 10,889) + 4 others; Malay 42.5% / Chinese 32.6% / Indian 21.9%.
- **N.33 Sri Tanjung** (FMT): PH Dr G. Rajasekaran (2nd term, 2023 maj 3,996) + 4 others; Malay 37.2% / Chinese 31.5% / Indian 28.35%.
- **Paroi** (FMT, correction): 3-cornered — PAS/PN Kamarul Ridzuan (incumbent, 2023 maj 5,539) vs PH Ahmad Shahir vs Bersatu Nazree Yunus. (Malay Mail had described straight fight — discrepancy; FMT more detailed.)
- **Pertang** (FMT): 3-way — BN Jalaluddin Alias (potential MB) vs PH Umry Abdul Khois vs Bersatu Faizal Fadli Idrus.

---

## 5. PRIORITY entities — PIR-16 (First Dominant Campaign Narratives)

### Viral-content amplifier narratives (director-flagged)
- **Albert Tei** — PN-camp businessperson who called Harapan supporters "barking dogs" (mkini /news/780042). Full body still NOT fetched (paywalled); entity from mkini homepage headline+description. Watch.
- **"barking dogs"** — the insult narrative itself, high viral-potential.
- **Muhyiddin graft trial** — "Company gave Bersatu RM1m for unknown reasons, witness tells court in Muhyiddin's graft trial" (mkini /news/779968). Active trial narrative.
- **Melaka DAP withdrawal** — DAP quit Melaka state govt (4 DAP reps moved to opposition; Amanah's Adly still seated with govt) over bill allowing appointed/nominated assemblymen. Dominant PIR-16 narrative directly framing DAP's acceptability in NS Malay seats. Per prior build: Anwar urged postpone; Melaka CM said abrupt exit shuts door on negotiations. This build adds headline-intel: Ab Rauf "PH only mirrored federal unity in Melaka" + "Melaka clears path to appoint seven unelected assemblymen".
- **"adat dispute"** — NS adat/istana (royal) crisis. Tok Mat: "keep adat out of polls campaign." Loke "penyaluran dana" controversy with Balai Undang Luak Sungai Ujong. Anwar: "Don't campaign on NS ruler crisis."
- **DAP revives anti-BN campaign** (mkini /news/780010) — 1MDB, ruler crisis, political manoeuvres.
- **Harapan Youth (AMH) demands BN ministers quit Cabinet** over PN alliance.

### ⭐ NEW PRIORITY PIR-16 narratives this build (FULL TEXT)
- **NS = makmal politik (political laboratory for PRU16)** — Zaharuddin Sani (Global Asia Consulting): "NS sedang dijadikan makmal politik." Every NS seat as a PRU16 indicator. Corroborates Zahid "NS performance determines future alliance" + Johari "Johor formula" + Utusan "PRN NS penentu kerjasama BN-PN PRU16".
- **Act now or lose chance forever (Tok Mat)** — NST 19 Jul 14:46 MYT, FRESH: "If we don't do it this time, we will miss the boat… our children and grandchildren will become mere traders in their own country." Existential Malay-future framing.
- **Malay-Muslim unity with non-extreme partners (Hadi)** — NST 19 Jul 14:03 MYT, FRESH: PAS+Umno+MCA+MIC+DHPP "non-extreme" formula; reject "unnatural Malay groups with DAP".
- **Ali Baba Bujang Lapok / 40 thieves were also united (Anwar)** — NST 19 Jul 12:21 MYT: "Unity alone is not enough… the 40 thieves were also united." Multi-ethnic counter-narrative to BN-PN Malay-unity framing.
- **Resign to attack unity partners (Anwar)** — NST 19 Jul 14:47 MYT, FRESH: ministers/deputy ministers must resign if they intend to use federal positions to attack unity-govt partners in state campaigns. Conveyed to DPMs Zahid + Fadillah. Federal-state firewall.
- **Umno's dangerous dance with PAS** — FMT opinion (19 Jul, 7009c): "By quietly opening the side door for PAS in NS, Umno is committing the oldest form of political miscalculation: validating the very force designed to replace it." Cites Amanat Hadi (1981). Viral-amplifier opinion piece.
- **Ahmad Zaharuddin Sani Ahmad Sabri** (analyst, Global Asia Consulting) — carrier of "makmal politik" framing. "The most important question is not whether the bride and groom agree, but whether the children accept the new marriage."

### Director-listed PIR-16 narrative figures
- **Anthony Loke Siew Fook (DAP)** — PIR-16 key figure. Defends Chennah. This build: FMT FULL TEXT "MCA biggest loser in BN-PN NS pact" — Loke mocks MCA "surrendered" Lobak, Mambau, Lukut to PN; "I want to thank Wee Ka Siong for being so generous." BN-PN pact = biggest PH challenge. Day-1 urged traffic-rule compliance at Pasar Besar Seremban.
- ⭐ **Lim Lip Eng** (Kepong MP, DAP) — NEW this build (FMT 18 Jul): rejects Hadi's Islamophobia claim; says Hadi himself coined "green wave" (gelombang hijau) in 2018. Cites Tuan Ibrahim Tuan Man.
- ⭐ **Tuan Ibrahim Tuan Man** (PAS deputy president) — NEW this build: "PAS never claimed to be sole embodiment of Islam" (cited by Lim to counter Hadi's Islamophobia framing).
- ⭐ **Wong Chin Huat** (Sunway University analyst) — NEW: MCA weaker in NS than Johor; non-Malays won't stake future on MCA if perceive PH-defeat risk.
- ⭐ **Lau Zhe Wei** (IIUM analyst) — NEW: advises Bersatu quit PN + take Gerakan/MIPP; MCA benefits from BN-PAS alliance (PAS vote transfer).
- ⭐ **Azeem Fazwan Ahmad Farouk** (USM analyst) — NEW: expects Bersatu wiped out in NS.
- ⭐ **Azmil Tayeb** (USM analyst) — NEW: "All people see coming out of Bersatu is the infighting."
- ⭐ **Azmi Hassan** (Felo Majlis Profesor Negara) — NEW: Johor PAS-Umno success motivates NS understanding.

### Director-listed PIR-16 narratives (watch-list — status updated)
- **"penyatuan undi Melayu"** — CONFIRMED active + EXPANDED this build: Kosmo "memaksimumkan pengundian Melayu"; Hadi "Malay-Muslim unity with non-extreme partners"; FMT akar umbi grassroots "penyatuan ummah"; Muhyiddin counter "charade to deceive the Malays"; Tok Mat "safeguard future of race and religion".
- **"MB after PRN"** — CONFIRMED active + FULL TEXT this build (FMT Jalaluddin): "BN to decide NS MB candidate only if it wins"; Jalaluddin among those touted.
- **"sole opposition"** — CONFIRMED active + FULL TEXT this build (FMT Muhyiddin): "Bersatu must survive as lone opposition".
- **"majoriti mudah"** — listed per director PIR-16 list; **still not directly quoted** in recovered full text. Watch.
- **Melaka DAP withdrawal** — now corroborated by 7 NST headline-intel items (Ab Rauf, Anwar postpone, Melaka clears path, DAP quits, DAP backs reps) + 1 mkini preview (Zan Azlee indicator v2).
- **adat dispute** — unchanged from prior build (still active).

### Coalition operational picture (PIR-06, FULL TEXT confirmed via Kosmo + FMT + NST + Awani this build)
- **BN: 25 seats** under BN-PN understanding; **PAS, Gerakan, Wawasan, MIPP fill the remaining 11** to avoid friendly fights.
- **PH: 36 seats** (all 36 contested); Amanah 5, DAP 11 (defending all), PKR 20.
- **Bersatu: 24 own-logo seats** — broke PN consensus, splits the vote in critical constituencies.
- **Teka-teki 11 kerusi terjawab** (Awani 16 Jul 23:12) — PN chairman Ahmad Samsuri Mokhtar announced remaining PN candidates; resolves the "mystery of 11 BN seats." PN candidates incl: Danni Rais (Klawang), Mohamad Rafie Ab Malek (Ampangan), Kumar Paramasevam (Lobak), Razali Abu Samah (Sikamat), Erik Michael (Mambau), Lee Boon Shian (Bukit Kepayang), Sathes Kumar Nilameham (Lukut); 4 incumbents retained: Mohd Fairuz (Serting), Kamarol Ridzuan (Paroi), Abdul Fatah Zakaria (Bagan Pinang), Ridzuan Ahmad (Gemas).
- **Machinery-sharing CONFIRMED at seat level** (NST 19 Jul 11:59 MYT): Tampin Umno chief Mohd Isam Mohd Isa — all BN ops rooms in Gemas open to assist PN (Wawasan) candidate. "Not a political merger."
- **PN-BN understanding NOT merger** — FULL TEXT corroborated across Wee (FMT), Isam (NST), Zahid, Hadi. DOMINANT official-framing narrative.

**SPR confirmation (Kosmo full text):** 103 candidates / 36 seats; 11 straight fights, 21 three-cornered, 2 four-cornered, 2 five-cornered; 94 men / 9 women; oldest Abd Latif A Tambi (70, Gemencheh), youngest M. Leevineshwaraan Murugan (23, Sri Tanjung).

---

## 6. Day-1 (19 Jul) campaign operations
- **NS Police (Datuk Alzafny Ahmad):** 1 election-offense report — verbal dispute ("gaduh mulut") from nomination day; no investigation paper opened. **19 ceramah permits ALL APPROVED.** No significant incidents. (FULL TEXT NST this build.)
- **Loke campaign Day-1** at Pasar Besar Seremban — candidates met visitors; Loke urged traffic-rule compliance; FMT "MCA biggest loser" statement.
- **Klawang Day-1 marquee** (Awani 19 Jul 12:11 MYT) — two cousins (PH Bakri Sawir vs PN Danni Rais) campaigned simultaneously at Pasar Minggu Kuala Klawang, met peacefully, joked — mature-campaign framing.
- **Tok Mat Day-1** (NST 19 Jul 14:46 MYT) — "act now or lose chance forever" at Sendayan Air Base Family Day Carnival.
- **Anwar Day-1** (NST 19 Jul 12:21 + 14:47 MYT) — Ali Baba Bujang Lapok unity speech (Ipoh) + resign-to-attack warning.
- **Melaka DAP quit-state-govt** decision landed on Day -1/Day 0 (18-19 Jul) — Anwar urged postpone but decision proceeded.

---

## 7. Honest collection limitations

1. **Malaysiakini paywall:** mkini articles (Loke Malay votes, Zan Azlee indicator v2, AI chatbot, Johor exco, Albert "barking dogs", Muhyiddin graft trial) captured as previews (91-600c) only; full body paywalled. Entity extraction is headline+description-derived for these high-signal pieces.
2. **gnews protobuf resolution via curl: CONFIRMED INFEASIBLE** across 4 cycles — intermediate is 588KB JS SPA, protobuf base64 decodes to encrypted tokens only. 10 items this build saved as headline-intelligence (title+pubdate+source). The Kiandee-quorum NST article is headline-intel only — full text requires NST feed (rotated past top-50) or JS-render.
3. **NST WordPress feed: only latest 50 items** — older high-value NST articles (Asyraf Wajdi BN-PN stability, Hadi PN-assist-BN, Bersatu goes solo, Loke slams traitors, Linggi risky) fell outside the top-50 window → headline-intelligence only.
4. **The Star + Malay Mail listing pages: JS-rendered**; Melaka DAP + Fahmi "Tok Min track record" articles captured as headline intelligence only.
5. **SOLVED this build:** FMT (curl-friendly RSS+direct) + NST WordPress feed + Awani direct-fetch (berita-politik slug) now provide reliable full-text paths — substantially closes the prior "JS-render blocker" gap for three major sources.
6. Director-list seats **N.20 Bembang, N.25 Labu** — candidate-level detail still NOT recovered; tagged per director list verbatim. "N.20 Bembang"↔"Bahau" mapping unconfirmed.

---

## 8. Key judgments

- **PIR-06 threshold (formal PN-MT removal of Bersatu): NOT CROSSED.** The CRITICAL precursor cluster is now **5 signals strong** (was 3): (1) Kiandee "asas kukuh" removal call, (2) ⭐NEW Kiandee quorum-question escalation, (3) "toxic PN" claim-counterclaim (FULL TEXT FMT), (4) Ridzuan Ahmad quits Bersatu, (5) ⭐NEW Muhyiddin "new coalition after state election" PN-exit hint (FULL TEXT FMT — strongest pre-threshold signal). The Bersatu operational split is real but is an operational/strategic divergence, not yet an organisational expulsion. **Watch next cycle for:** (a) Bersatu Supreme Council formal response to the quorum question, (b) post-NS-PRN formalisation of Muhyiddin's "new coalition", (c) further Bersatu quits beyond Ridzuan.
- **PIR-07:** The "fleeing Sikamat" + "Linggi not for granted" narrative pair remains the most active defector-framing cluster. **This build recovered N.28 Klawang (two-cousins marquee) and N.27 Chembong candidates** — the Day-1 "two cousins face off" Klawang storyline is the single highest-value new PIR-07 thread. Candidate recovery is now complete for 8 of 10 director-listed seats (only N.20 Bembang + N.25 Labu outstanding).
- **PIR-16:** The narrative field has **expanded and sharpened** this build. The dominant new thread is **"NS = makmal politik (political laboratory for PRU16)"** — Zaharuddin Sani + Azmi Hassan + Zahid + Johari converge on framing every NS seat as a PRU16 indicator. The **Anwar counter-narrative pair** (Ali Baba "40 thieves were also united" + "resign to attack unity partners") directly contests the Tok Mat/Hadi Malay-unity framing. **Melaka DAP withdrawal** remains the dominant directly-DAP-implicating narrative. The **FMT "Umno's dangerous dance with PAS" opinion** (7009c) is the highest-risk viral-amplifier opinion piece this build.

---

## 9. Files produced

- `processed-entities/20260719/entities-20260719-0714.json` — **223 entities** (114,922 bytes), valid JSON, lint-passed. CURRENT.
- `processed-entities/20260719/summary.md` — this summary.
- `processed-entities/20260719/_build_entities_0714.py` — merge/build script (reproducible).

*(Pre-existing/superseded, retained untouched: `entities-20260719-0507.json` (167 entities), `entities_021231.json` (02:12 UTC), `entities_034922_delta.json` (03:49 UTC), `entity_metadata.json`.)*

---

**End of summary.**
