# PRN Negeri Sembilan 2026 — Entity Extraction Summary

**Date:** 2026-07-19 (Sunday)
**Processing timestamp (UTC):** 2026-07-19T05:07:00+00:00  |  **MYT:** 2026-07-19 13:07
**Agent:** PRN NS 2026 Entity Extraction Agent (scheduled cron)
**Director-approved cycle:** 19 Jul 2026 (PIR-06, PIR-07, PIR-16)
**Classification:** TLP:AMBER
**Output file:** `processed-entities/20260719/entities-20260719-0507.json`

---

## 1. Scope & ingestion

Ingested **all content** in `04-DATA-AND-SOURCES/raw-scrapes/20260719/` across **3 scrape cycles** (011915, 024042, 034922 UTC), spanning **7+ source outlets** (Malaysiakini, Malay Mail, NST via gnews, Astro Awani, Kosmo, Utusan, The Star gnews, Newswav/GNews mirrors) plus the collection `index.md`. 17 priority-tagged articles read in full; aggregate source scrapes (mkini, mkini-gnews, nst-gnews, astroawani, kosmo, utusan) scanned title-by-title for entity mentions.

## 2. Headline numbers

| Metric | Count |
|---|---|
| **Total entities extracted** | **167** |
| CRITICAL (PIR-06 termination-adjacent) | 7 |
| PRIORITY (PIR-07 battleground / PIR-16 viral-amplifier) | 33 |
| Normal | 127 |
| By type — person | 89 |
| By type — narrative | 22 |
| By type — seat | 33 |
| By type — party | 23 |
| By PIR — PIR-06 (Coalition Operational Arrangement) | 34 |
| By PIR — PIR-07 (Highest-Priority Battlegrounds) | 98 |
| By PIR — PIR-16 (First Dominant Campaign Narratives) | 35 |

---

## 3. CRITICAL entities — PIR-06 (Coalition Operational Arrangement)

**Threshold status: NOT CROSSED.** No formal PN-MT (Majlis Tertinggi) removal notice for Bersatu was detected across the 3 cycles. Bersatu's operational split is **confirmed** (24 own-logo seats), but the formal "pecat" threshold has **not** been crossed. **Three CRITICAL precursor signals** are now live, however:

| Entity | Type | Signal |
|---|---|---|
| **"toxic PN" claim** | narrative | Muhyiddin attributed claim; Hadi dismisses it and points finger back at Bersatu — claim/counter-claim exchange is the strongest internal-rupture discourse signal to date |
| **"PN has grounds to remove Bersatu" (Kiandee)** | narrative | Bersatu VP Ronald Kiandee's call ("asas kukuh") — a CALL for removal, not a formal notice, but director-flagged "pecat"-type precursor |
| **Ridzuan Ahmad quits Bersatu** | narrative | CONFIRMED "keluar" signal — former Gemas incumbent resigned as Bersatu division chief and quit the party; now contesting Gemas under Wawasan. Corroborated across The Edge, Malay Mail lineup, and NST headline |

**CRITICAL persons (carriers of above):**
- **Muhyiddin Yassin** (Bersatu president / PN chairman) — "toxic PN" claim attribution; "Bersatu to use own logo" announcement
- **Hadi Awang** (PAS president) — dismisses "toxic PN" claim, points finger at Bersatu; also carrier of "BN-PN ties based on friendship, brotherhood"
- **Ronald Kiandee** (Bersatu VP) — "PN has grounds to remove Bersatu"
- **Ridzuan Ahmad** — quit Bersatu, now Wawasan candidate in Gemas

**Watch entities carried per director list (no new direct quotes this cycle):** Hamzah Zainudin, Annuar Musa, PN-MT, PAS Supreme Council, Bersatu Supreme Leadership.

**PIR-06 Tier-4 seats (director list)** — no candidate withdrawals detected this cycle across N.04, N.05, N.13, N.14, N.23, N.25, N.31, N.34. N.13 Sikamat and N.14 Ampangan carry the highest messaging-war load.

---

## 4. PRIORITY entities — PIR-07 (Highest-Priority Battlegrounds)

### Defector-framing & complacency narratives (director-flagged)
- **Aminuddin Harun (outgoing MB)** — moved from long-held Sikamat to Linggi (BN stronghold); **denies "fleeing Sikamat"**, frames as strategic choice. Also PIR-16 "MB after PRN" referendum figure.
- **"fleeing Sikamat" narrative** — director-flagged defector-framing entity, active.
- **"Linggi stronghold cannot be taken for granted"** — director-flagged "not taking for granted" entity, carried by BN's Faizal Ramli camp.

### Director-listed highest-priority battleground seats (10 seats)
N.13 Sikamat, N.14 Ampangan, N.15 Juasseh, N.28 Klawang, N.32 Linggi, N.27 Chembong, N.20 Bembang, N.25 Labu, N.10 Nilai, N.33 Sri Tanjung — all tagged PRIORITY.

**Recovery status:**
- **Full candidate roster recovered** for N.13 Sikamat (3-cornered), N.14 Ampangan (per director list — Nazri Kassim vs Rafie), N.32 Linggi (3-cornered MB battle: Aminuddin vs Faizal Ramli vs Zamri), N.10 Nilai (5-cornered), N.33 Sri Tanjung (5-cornered), N.15 Juasseh (BN "unfazed" by 3-cornered).
- **Candidate detail NOT recovered** for N.28 Klawang, N.27 Chembong, N.20 Bembang, N.25 Labu — kept verbatim per director list. **Honest limitation:** the full Malay Mail nomination-lineup text recovered named "Bahau" (DAP Teo Kok Seong vs MCA Chong Fui Ming) — whether director-list "N.20 Bembang" maps to "Bahau" is **unconfirmed** from this cycle's full text. Both tags retained.

### Director-flagged candidates
- **Nazri Kassim** (PH, N.14 Ampangan) and **Datuk Dr Mohamad Rafie Ab Malek** "Rafie" (PN, N.14 Ampangan) — Day-1 messaging war: PH "defector" vs PN "experienced rep".
- **Datuk Mohd Faizal Ramli** (BN, N.32 Linggi) — director-flagged "Faizal Ramli" entity; carrier of "not taking for granted" framing vs MB Aminuddin.

---

## 5. PRIORITY entities — PIR-16 (First Dominant Campaign Narratives)

### Viral-content amplifier narratives (director-flagged)
- **Albert Tei** — PN-camp businessperson who called Harapan supporters **"barking dogs"** (mkini /news/780042). Full body NOT fetched this cycle (paywalled/homepage); entity derived from mkini homepage headline+description. Full name "Albert Tei" per director PIR-16 list.
- **"barking dogs"** — the insult narrative itself, high viral-potential entering Day-1.
- **Muhyiddin graft trial** — "Company gave Bersatu RM1m for unknown reasons, witness tells court in Muhyiddin's graft trial" (mkini /news/779968). Active trial narrative framing Bersatu/Muhyiddin credibility.
- **Melaka DAP withdrawal** — DAP quit Melaka state govt (4 DAP reps + 1 Amanah's Adly moved to opposition bloc) over bill allowing appointed/nominated assemblymen. **Dominant PIR-16 narrative directly framing DAP's acceptability in NS PRN Malay seats.** Anwar urged postpone; Melaka CM said abrupt exit shuts door on negotiations; Perak unity ties unaffected.
- **"adat dispute"** — NS adat/istana (royal) crisis surfaced as PRN campaign issue. Tok Mat: "keep adat out of polls campaign." Loke's "penyaluran dana" controversy with Balai Undang Luak Sungai Ujong. Anwar: "Don't campaign on NS ruler crisis." Rembau chieftain sacked 3 nobles; court injunction.
- **DAP revives anti-BN campaign** (mkini /news/780010, Zarrah Morden) — leaders bring up 1MDB scandal, ruler crisis, and political manoeuvres.
- **Harapan Youth (AMH) demands BN ministers quit Cabinet** over PN alliance — "BN is ungrateful despite trust and positions given by PM." Day-1 amplification of BN-PN backlash (mkini top story + Astro Awani).

### Director-listed PIR-16 narrative figures
- **Anthony Loke Siew Fook (DAP)** — PIR-16 key figure. Defends Chennah. Day-1 urged traffic-rule compliance after PH candidates met visitors at Pasar Besar Seremban. Carries: leadership-referendum framing, "penyaluran dana" adat controversy, DAP-not-quitting-Harapan, "campaign of hope".

### Director-listed PIR-16 narratives (watch-list, some not yet directly quoted in recovered text)
- **"penyatuan undi Melayu"** — confirmed active (Kosmo full text: "mengelakkan pertembungan sesama sendiri dan memaksimumkan pengundian Melayu")
- **"MB after PRN"** — confirmed active (Utusan rencana)
- **"sole opposition"** — confirmed active ("Bersatu exit from PN imminent?" + Bersatu going solo reframes opposition identity)
- **"majoriti mudah"** — listed per director PIR-16 list; **not yet directly quoted** in this cycle's recovered full text. Watch for emergence in campaign coverage.

---

## 6. Coalition operational picture (PIR-06, full-text confirmed via Kosmo)

The Kosmo full-text article (`percaturan-bn-ph-bersatu`, 20260719_011915 cycle) confirms the operational arrangement as of Day -1 / Day 0:

- **BN: 25 seats** under BN-PN understanding, with **PAS, Gerakan, Wawasan, and MIPP filling the remaining 11** to avoid friendly fights.
- **PH: 36 seats** (all 36 contested); Amanah 5, DAP 11 (defending all), PKR 20.
- **Bersatu: 24 own-logo seats** — **broke PN consensus**, "memecah undi di kawasan-kawasan kritikal" (splits the vote in critical constituencies).
- **BN bigwigs retained:** Tok Mat (Rantau), Jalaluddin Alias (Pertang). Bersatu info chief Tun Faisal contests Sikamat.

**SPR confirmation (Kosmo full text):** 103 candidates / 36 seats; 11 straight fights, 21 three-cornered, 2 four-cornered, 2 five-cornered; 94 men / 9 women; oldest Abd Latif A Tambi (70, Gemencheh), youngest M. Leevineshwaraan Murugan (23, Sri Tanjung).

---

## 7. Day-1 (19 Jul) campaign operations

- **NS Police (Datuk Alzafny Ahmad):** 1 election-offense report — verbal dispute ("gaduh mulut") from nomination day; no investigation paper opened. **19 ceramah permits ALL APPROVED.** No significant incidents.
- **Loke campaign Day-1** at Pasar Besar Seremban — candidates met visitors; Loke urged traffic-rule compliance (helmet use, no standing on 4x4s).
- **Melaka DAP quit-state-govt** decision landed on Day -1/Day 0 (18-19 Jul) — Anwar urged postpone but decision proceeded.

---

## 8. Honest collection limitations

1. **Malaysiakini paywall:** 6 high-value mkini articles (Albert "barking dogs", Muhyiddin graft trial, MCA internal dissent, Wee "not a merger", Hadi-Tok Mat adat, Tamim surrender) were captured as **title + pubdate + preview (~180-513 chars) only**. Full body is paywalled. Entity extraction is therefore headline+description-derived for these high-signal pieces.
2. **The Star + Malay Mail listing pages are JS-rendered**; 2 Melaka DAP + 1 Fahmi "Tok Min track record" article captured as **headline intelligence only** (full-text URL unrecoverable via curl).
3. **The Malaysian Insight** homepage returned 0 articles — no coverage this cycle.
4. **Albert "barking dogs" article (mkini /news/780042)** full body NOT fetched this cycle — entity derived from mkini homepage scrape; full name "Albert Tei" per director PIR-16 list.
5. Director-list seats **N.28 Klawang, N.27 Chembong, N.20 Bembang, N.25 Labu** — candidate-level detail NOT recovered from this cycle's full text; tagged per director list verbatim.

---

## 9. Key judgments

- **PIR-06 threshold (formal PN-MT removal of Bersatu): NOT CROSSED.** All three CRITICAL signals are **precursors** (a removal *call*, a *quit*, a *toxic claim-counterclaim*) — none is a formal PN-MT notice. The Bersatu operational split is real (24 own-logo seats) but is an operational/strategic divergence, not yet an organisational expulsion. **Watch next cycle for:** (a) PN-MT convening, (b) further Bersatu quits beyond Ridzuan, (c) escalation of "toxic PN" claim into a formal PN-MT response.
- **PIR-07:** The "fleeing Sikamat" + "Linggi not for granted" narrative pair is the **most active PIR-07 defector-framing cluster**, centred on MB Aminuddin's seat-move. This is the single highest-value PIR-07 messaging thread to track through polling day.
- **PIR-16:** The **Melaka DAP withdrawal** is the single most dominant PIR-16 narrative entering Day-1, directly framing DAP's acceptability in NS Malay-majority seats. The **Albert "barking dogs"** story has the highest viral-amplification potential but its full body is not yet in hand. The **Muhyiddin graft trial** runs in parallel as a credibility-drain on Bersatu/PN.

---

## 10. Files produced this cycle

- `processed-entities/20260719/entities-20260719-0507.json` — 167 entities (60,393 bytes), valid JSON, lint-passed.
- `processed-entities/20260719/summary.md` — this summary.

*(Pre-existing from earlier cycles: `entities_021231.json` (02:12 UTC), `entities_034922_delta.json` (03:49 UTC), `entity_metadata.json` — left untouched.)*

---

**End of summary.**
