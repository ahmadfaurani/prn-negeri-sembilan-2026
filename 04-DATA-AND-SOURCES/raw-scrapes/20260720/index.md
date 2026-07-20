# PRN Negeri Sembilan 2026 — Raw Scrapes Index
## Date: 2026-07-20 (Mon) | Campaign Day 2 | Nomination Day +2 | TLP:AMBER

**Workspace:** `04-DATA-AND-SOURCES/raw-scrapes/20260720/`
**Collection mode:** Nomination-Day Surge Mode (Director priority-approved PIR-06/07/16)
**Cycle:** `20260720_morning` — collected 01:09–01:12 UTC 20 Jul (09:09–09:12 MYT 20 Jul)
**Prior cycle:** `20260719_233400` (ended 23:34 UTC 19 Jul = 07:34 MYT 20 Jul) — used as freshness cutoff
**Polling day:** 2026-08-01 (Sat) | **Early voting:** 2026-07-28 | **Nomination day:** 2026-07-18 (Sat)
**Fetcher:** `_surge_fetch_20260720_morning.py` (Awani RSS full + FMT RSS full content:encoded + Google News RSS ×30 PIR-targeted queries + NST/Star/MalayMail/Utusan/HarianMetro/BH/Sinar homepage slug-hint extraction)

---

## CYCLE SUMMARY

| Metric | Value |
|---|---|
| Google News queries run | 30 (incl. 8 mandatory PIR-06 [CRITICAL]-watch: kuorum, lebih hebat, pecat, tarik diri, PN Supreme Council, machinery sharing, Wawasan Ridzuan, sole opposition) |
| gnews items returned | 487 (331 PRN/priority headline hits) |
| gnews **fresh** post-cutoff (≥23:34 UTC 19 Jul) | **0** (gnews RSS surfaces historical matches; latest dated 19 Jul) |
| RSS feed items scanned | Awani 10 / FMT 50 / (NST+MalayMail feeds returned 0 items — JS/403) |
| Homepage candidate links found | NST 8 / Star 8 / MalayMail 41 / Utusan 61 / Sinar 19 (HarianMetro/BH 0) |
| **Articles saved (total)** | **51** |
| Genuine PIR-06 [CRITICAL] threshold crossings | **0** (18th cycle — confirmed) |
| Auto-flagged [CRITICAL] in saved files | 1 → **FALSE POSITIVE (corrected)** — see §CRITICAL |
| Genuinely-NEW analytically-material articles | **11** (5 fresh post-cutoff + 6 new-to-collection) |
| Full-text recoveries of prior headline-intel (enrichments) | 3 |
| Duplicates (re-saved, already captured prior cycles) | ~8 |
| False positives (World Cup / geopolitics / sports / court) | 25 |
| gnews critical-keyword scan (kuorum/lebih hebat/pecat/tarik diri/bersatu exit/sasar bentuk kerajaan) | **0 hits** |

---

## 🔴 PIR-06 — COALITION OPERATIONAL ARRANGEMENT — [CRITICAL] NOT CROSSED (18th cycle)

**[CRITICAL] status: MAINTAINED from prior 075200 cycle (Kiandee quorum escalation, originated 11 Jul). NO NEW THRESHOLD CROSSING this cycle.**

This cycle did NOT detect (18th cycle confirmation): any formal PN-MT expulsion notice for Bersatu; any Bersatu candidate withdrawal (24 solo Bersatu-logo candidates stable); any Kiandee/PN quorum escalation; any PN/Bersatu Supreme Council statement; any RoS intervention; any "lebih hebat new coalition" formalization; any PDM Klawang reopening (now ~hour 16+ of Jalaluddin "1–2 days" window — 20 Jul MYT business hours underway). All 8 mandatory gnews [CRITICAL]-watch queries returned 0. gnews critical-keyword scan across 331 priority headlines = **0 hits**.

**NEW PIR-06 intelligence this cycle (cooperation-friction + operational strategy, NOT formal-threshold):**

### 1. Pemuda PKR: BN-PN cooperation = plot to topple Anwar [FRESH 07:00 MYT 20 Jul, NEW]
→ `priority_PIR-06-PIR-07_FMT_pemuda-pkr-dakwa-kerjasama-bn-pn-mahu-cabar-kepimpinan-anwar_20260720_morning_rss.md` (FMT full text)
- **PKR Youth chief Kamil Munim** (also political secretary to PM/Finance Minister Anwar) claims BN-PN cooperation in NS PRN is driven by political interest, not rakyat agenda — framed as **building momentum to challenge Anwar's leadership**.
- Direct quote: "Zahid wants to be PM, partnering with opposition to build momentum to topple Anwar. Manipulating race/religion issues to gain Malay support. The reality is, this modus operandi is the same as how Dr Mahathir was removed. After that, they will fight among themselves for power."
- References **AMH (Angkatan Muda Harapan) call for all BN ministers/deputy ministers to resign from Cabinet** following BN's open cooperation with PN (carryover signal, now reinforced).
- **Dissent within PH:** Pasir Gudang MP **Hassan Karim** (PKR) calls it "normal in politics" — "PH shouldn't complain and sigh" — notes BN cooperated with PH after toppling BN in GE14, so BN-PN cooperating to seize NS from PH is analogous.
- **Significance:** NEW escalation of intra-unity-government friction. A PKR Youth leader (Anwar's own political sec) openly framing BN-PN as a leadership-toppling plot is a notable PIR-06 cooperation-friction signal. Not [CRITICAL] (no formal expulsion/withdrawal).

### 2. Wawasan guns for police vote via retired senior officers [FRESH 07:30 MYT 20 Jul, NEW]
→ `priority_PIR-06-PIR-07_FMT_wawasan-guns-for-crucial-police-vote-through-retired-senior-officers_..._rss.md` (EN) + `..._wawasan-sasar-undi-penting-polis-melalui-pegawai-kanan-bersara_..._rss.md` (BM)
- **Wawasan (Hamzah Zainudin's party) targeting the police vote** through retired senior officers joining the party.
- **Ex-Bukit Aman internal security director Hazani Ghazali** (also first DG of Border Control & Protection Agency, ex-Sabah police chief 2020-2022, ex-Esscom 2017) = Wawasan central leadership member.
- **Ex-Melaka deputy police chief Razali Abu Samah = Wawasan CANDIDATE in NS PRN** → **confirms Razali Abu Samah = the Wawasan candidate in N.13 Sikamat** (3-cornered: Nor Azman PH vs Tun Faisal Ismail Aziz Bersatu vs Wawasan's Razali Abu Samah). New Sikamat intel: Razali's police background = vote-pull strategy.
- 130,000+ policemen nationwide; 200,000+ votes incl. wives; significant in marginal seats (a few hundred votes can flip). Hamzah leveraging his home-minister tenure (Mar 2020–Nov 2022) relationships.
- Analysts Azmi Hassan (Akademi Nusantara) + Mazlan Ali (UTM): nothing wrong with ex-cops in politics; ex-IGP Khalid Abu Bakar says legal but "I don't like politics."
- **Significance:** NEW Wawasan operational strategy intel + confirms Sikamat Wawasan candidate's vote-pull rationale (police bloc).

### 3. Noh Omar: BN-PN "blue wave" Johor → NS → Selangor → Putrajaya (GE16) [00:24 MYT 20 Jul, NEW]
→ `priority_PIR-06-PIR-07-PIR-16_FMT_noh-omar-hopes-bn-pn-formula-sparks-blue-wave-in-selangor_..._rss.md`
- Former Selangor Umno chief **Noh Omar**: NS BN-PN cooperation should spark a "wave" spreading to Selangor → capture Putrajaya in **GE16**.
- "The 'blue wave' began in Johor and is now moving to Negeri Sembilan. Confident this formula will positively impact Selangor, and by GE16, BN and PN will return to power."
- Frames NS as the **test-bed / "makmal politik" for PRU16** — explicit escalation of the PRU16-framing narrative. Avoids direct Umno-PAS clashes → strengthens Malay-majority support. Three-cornered Umno/PAS/PH only benefits PH (cites Khairy's Sungai Buloh GE15 defeat).
- Met **Hadi Awang in 2018** to urge Umno-PAS not to contest each other in Selangor.
- **Noh's full timeline (NEW detail):** sacked by Umno Jan 2023 (GE15 discipline) → joined Bersatu July 2024 → Supreme Council early 2025 → resigned Feb (after sacking of 17 leaders) → quit Bersatu, rejoined Umno June 7 under special initiative. ("If Umno severs ties with DAP in the morning, I will return by noon.")
- **Significance:** Clear PIR-16 "makmal politik PRU16" / "penyatuan undi Melayu" framing. Not the PIR-16 [CRITICAL] trigger (not "Bersatu exit imminent" / "sasar bentuk kerajaan negeri").

### 4. Jalaluddin thanks Perikatan: PN concedes MB post to BN [19 Jul 5:55pm MYT, NEW]
→ `priority_PIR-06-PIR-07-PIR-16_malaymail_jalaluddin-thanks-perikatan-for-backing-bn-to-lead-negeri-sembilan-..._home.md`
- NS Umno chief **Datuk Jalaluddin Alias** (BN's **Pertang** candidate) THANKED PN for early decision to **leave the MB post to Umno/BN** should the alliance win the Aug 1 election.
- "We never discussed who should become MB. I thank the PN leadership for declaring early they would leave the MB post to Umno and BN." No exco allocation discussed — "priority is to achieve victory first."
- **MB succession named:** Jalaluddin named **Tok Mat (Mohamad Hasan)** and **Seri Menanti candidate Sufian Maradzi** as those who could be considered for MB. "Up to the BN chairman to decide."
- Connects to **Pertang "derhaka" friction** (PIR-07 brief) — Jalaluddin in conciliatory posture toward PN, deflecting MB question from himself to Tok Mat/Sufian. PIR-06 (PN concedes MB) + PIR-16 ("MB after PRN").
- **Significance:** NEW — PN's MB concession is a significant cooperation-arrangement signal. MB candidates (Tok Mat, Sufian Maradzi) now on record.

### 5. Felda-Umno ties tough to undo despite non-Umno chairman [FRESH 08:00 MYT 20 Jul, NEW]
→ `priority_PIR-06-PIR-16_FMT_felda-umno-ties-tough-to-undo-..._rss.md` (EN) + `..._hubungan-felda-umno-sukar-..._rss.md` (BM)
- Non-Umno **Felda chairman Ahmad Badri Zahir** (replacing Umno stalwart Ahmad Shabery Cheek, contract ended June 30). Analysts split: Awang Azman (UM) + Syaza Shukri (IIUM) say Umno-Felda bond built over decades won't shift overnight; Zaharuddin Sani (Global Asia) says neutral/professional Felda leadership "ends Umno's monopoly" — settlers may drift to PH/alternatives.
- **Puad Zarkashi** (ex-Umno Supreme Council): non-renewal could make it harder to win back Felda seats lost to PN in GE15 → could **push Umno-PAS seat-sharing talks** (PAS holds several Felda-linked parliamentary seats won under PN in GE15).
- **Significance:** Relevant to NS Felda seats (Serting, Palong, Jeram Padang, Bahau, Gemas, Felda Pasoh 4 — Jalaluddin's Kemas event was at Felda Pasoh 4). PIR-06 (Umno-PAS seat-sharing) + Felda-voter-bloc strategy.

**Tier-4 seat watch (N.04, N.05, N.13, N.14, N.23, N.25, N.31, N.34):** No Bersatu candidate withdrawals. **N.13 Sikamat** now has Wawasan candidate Razali Abu Samah's police-vote strategy intel (item 2 above). No other new Tier-4 intel.

---

## 🟠 PIR-07 — HIGHEST-PRIORITY BATTLEGROUNDS — DAY-2 CAMPAIGN INTEL (NEW)

### 1. Six NS seats that could tell the story of the election [FRESH 20 Jul 7:00am MYT, NEW — HIGH VALUE]
→ `priority_PIR-06-PIR-07-PIR-16_malaymail_six-negeri-sembilan-seats-that-could-tell-the-story-of-the-election-..._home.md` (Malay Mail, full analysis, 10,066 chars)
Malay Mail's marquee seat-analysis piece (6 seats to watch):
| Seat | Contest | Key detail | Demographics |
|---|---|---|---|
| **Rantau** | Straight | Tok Mat since 2004; 2023 = 71.7%, won by 10,000+ vs PAS Rozmal Malakan; 2019 by-sec 63.2%. Question = by how much (Johor momentum test) | Malay 54.8%, Indian 27.6%, Chinese 16%; 14,000+ voters under 40 |
| **Chennah** | Straight | Loke since 2013; 2023 = 61.5% vs Bersatu Rosmadi Arif; narrowest 2018 (3-cornered, just over half). "50-50" per Loke. Gauge of Chinese support for DAP post-unity-govt | Malay 46.3%, Chinese 44.3%, Indian 2%+ |
| **Linggi** | 3-corner | Aminuddin (leaving Sikamat) vs Umno's Mohd Faizal Ramli (ex-coalition exco colleague). **Never changed hands since 1959** (Umno's oldest fortress). Faizal won 2023 with 55.1% vs Bersatu Zamri. Within Port Dickson parliamentary (Aminuddin's) | Malay 60.4%, Chinese ~18%, Indian ~18% |
| **Lenggeng** | 3-corner | BN since 1959 → lost to PH 2018 → reclaimed 2023 by **only 685 votes** over PAS. Classic marginal; PN split-vote test | ~75% Malay, Indian 15.2% |
| **Lukut** | Straight | DAP Choo Ken Hwa ~79% both 2018/2023. Within PD parliamentary = **7,000+ military early voters**. Barometer for urban + military vote | Chinese 49.5%, Indian 26.2%, Malay 22.7% |
| **Nilai** | **5-corner** | DAP Arul Kumar Jambunathan since 2013, 2/3+ votes each election. **Largest of the six: 41,000+ voters, ~14,200 under 30.** Young/urban voter barometer | Malay 42.5%, Chinese 32.6%, Indian 21.9% |

### 2. Klawang cousins: 3-cornered fight, candidate names confirmed [19 Jul 1:29pm MYT, NEW]
→ `priority_PIR-06-PIR-07-PIR-16_malaymail_negeri-sembilan-polls-cousins-turn-political-rivals-in-three-way-contest-for-kla_..._home.md`
- **Klawang (N.28) = 3-cornered:** PH incumbent **Datuk Bakri Sawir** vs PN's **Danni Rais** (cousins) vs Bersatu's **Muhammad Adib Musa**. 13,355 registered voters.
- Cousins crossed paths cordially at Kuala Klawang weekend market, Jelebu (19 Jul) — exchanged jokes, no provocation. Bakri: campaign healthily, respect the law (Jelebu District Council reprimanded flag installation on stadium fence → removed).
- **Significance:** Confirms Klawang candidate names (prior index had the PDM/polling-centre-closed protest story + cousins-encounter event, but not all 3 candidate names). Note: Bersatu's Muhammad Adib Musa = third candidate.

### 3. Aminuddin one-on-one Linggi campaign [19 Jul 6:50pm MYT, NEW] + Utusan BM corroboration [FRESH 20 Jul 7:59am]
→ `priority_PIR-06-PIR-07_malaymail_forget-big-walkabouts-aminuddin-says-he-d-rather-meet-linggi-voters-one-on-one-..._home.md` + `priority_..._utusan_aminuddin-pilih-kempen-bersemuka_..._home.md`
- Aminuddin (caretaker MB, contesting Linggi) prefers small-scale/one-on-one campaign (since 2008), not big walkabouts — "voters want to meet candidates personally."
- **Crossed paths with BN incumbent Mohd Faizal Ramli** campaigning in same area (Pasir Panjang). Indian community support "very positive" despite Linggi being BN stronghold.
- **Linggi voter breakdown (NEW):** 20,677 voters = 18,420 ordinary + **2,222 military + spouses** + 35 police (early voting). The 2,222 military bloc is significant.
- Aminuddin = PKR vice-president, state PKR chairman, Port Dickson MP, 59. Linggi contest: Aminuddin (PH) vs Faizal (BN, 54) vs Zamri Md Said (Bersatu, 54).
- **Date discrepancy noted:** Malay Mail says state assembly dissolved **June 5**; prior index/cycles used **June 26**. Flag for verification.
- **PH manifesto launch 20 Jul evening** (officiated by Selangor MB Amirudin Shari; "manifesto for continuity"; 5-outlet corroborated prior) + **BN manifesto 24 Jul at DUN Linggi + Pertang** remain the next major PIR-07 events — capture all coverage when published.

---

## 🟡 PIR-16 — FIRST DOMINANT CAMPAIGN NARRATIVES — [CRITICAL] NOT CROSSED (18th cycle)

**PIR-16 [CRITICAL] threshold NOT CROSSED.** No hard-news outlet corroboration of "Bersatu exit imminent?" or "Bersatu sasar bentuk kerajaan negeri" detected (gnews 0 hits; no RSS/homepage match).

### NEW PIR-16 intelligence this cycle:

**Muhyiddin Jana Wibawa graft trial — RM24.4m paid for Felda Bukit Jalor–Gemas NS road [NEW, surfaced today]**
→ `priority_PIR-06-PIR-07-PIR-16_utusan_syarikat-dicadangkan-muhyiddin-terima-rm24-4-juta-bayaran-projek-jana-wibawa_..._home.md` (Utusan, dated 15 Jul 5:45pm, by Nur Aimi Hazirah)
- Court told **JKR paid RM24.4 million to KCJ Engineering Sdn Bhd (KESB)** for a Jana Wibawa project linked to ex-PM Muhyiddin. KESB among **54 contractors Muhyiddin gave to ex-Finance Minister Tengku Zafrul** for 54 Jana Wibawa projects (direct negotiation / Design & Build).
- **The project: building a new road connecting Felda Bukit Jalor to Gemas, Negeri Sembilan** — total contract **RM62 million**. **(NS/Gemas link — Gemas = the seat where Wawasan's Ridzuan Ahmad, the Bersatu-quit figure, is contesting.)**
- 17th prosecution witness **Wan Hasnan Wan Musa** (JKR NS director) confirmed. Contract began 22 Dec 2021, 34-month term. RM10m Wang Pendahuluan Kontrak + 9 transactions (28 Mar–15 Feb 2023); 3 more payments ~RM4.7m recommended but not paid (insufficient allocation).
- **Significance:** PIR-16 "Muhyiddin corruption/graft trial" with NS-specific project detail (Gemas road). Reinforces the Bersatu-disarray / Muhyiddin-corruption narrative during the NS campaign.

**Sinar analysis: "Cabar mencabar ujian baharu Kerajaan Perpaduan menjelang PRN NS" [NEW]**
→ `priority_PIR-06-PIR-07_sinarharian_cabar-mencabar-ujian-baharu-kerajaan-perpaduan-menjelang-prn-negeri-sembilan-..._home.md`
- Sinar Harian opinion/analysis: Akmal Saleh's challenge to Anwar (drop ministers from parties contesting PH) + AMH's call for BN ministers to resign = escalating political pressure. Anwar's discipline principle must apply uniformly across parties.
- Unity-govt component anxiety over BN's political direction; PRN sees unity-govt parties clashing due to different state landscapes; line between electoral competition and admin responsibility blurring.
- **Related-headline intel:** "PRN Negeri Sembilan: PH sasar menang **32 kerusi** untuk bentuk kerajaan lebih stabil – Anthony" — note the **32-seat** figure (vs the "8123"/23-seat "safe majority" target). Possible two-tier framing: 23 = safe majority, 32 = full ambition. Flag for verification.

**Narrative map status (unchanged/confirmed):**
- "Bersatu kacau daun" (Khaled) — full RSS text recovered this cycle (enrichment of 171500 capture). Narrative stable.
- "makmal politik PRU16" — Noh Omar's "blue wave" framing (item PIR-06 #3) is the clearest pickup this cycle.
- MCA rebuttal to Loke "biggest loser" — no new pickup; top leadership (Wee/Mah) still silent; Saw Yee Fung (MCA Youth) remains closest-to-rebuttal.
- Resign-narrative (AMH → Anwar warning → Tok Mat "ready to resign" → Akmal "Nga resign too") — stable; Sinar analysis reinforces.

---

## ⚠️ [CRITICAL] FLAG CORRECTION — FALSE POSITIVE

**File:** `priority_..._FMT_ph-targets-23-seats-for-safe-majority-in-negeri-sembilan-says-loke_..._rss.md`
- **Auto-flag fired [CRITICAL]** because the body contained "sasar" (PH sasar menang 23 kerusi = PH targets winning 23 seats) + "majoriti" (safe majority) + "sasar bentuk" — but the actual phrase is "PH sasar menang 23 kerusi untuk bentuk kerajaan lebih stabil" = PH's seat-count target, **NOT** the PIR-16 trigger "Bersatu sasar bentuk kerjaan negeri" (Bersatu targets forming the state government).
- **Corrected to non-critical** via patch. Article is a **DUPLICATE** of 171500 cycle (Negri Sembilan polls: PH targets 23 seats). Retained as full-RSS-text enrichment (the "8123" backdrop detail + Loke staying away from Rantau to preserve unity-govt harmony).
- **Net result: 0 genuine [CRITICAL] files this cycle.** PIR-06 and PIR-16 [CRITICAL] thresholds both NOT CROSSED (18th cycle).

---

## 📦 FILE INVENTORY — Cycle 20260720_morning (51 files)

### Genuinely-NEW analytically-material articles (11)
**PIR-06:**
- `priority_PIR-06-PIR-07_FMT_pemuda-pkr-dakwa-kerjasama-bn-pn-mahu-cabar-kepimpinan-anwar_..._rss.md` — **FRESH 07:00 MYT, PKR Youth: BN-PN = topple-Anwar plot**
- `priority_PIR-06-PIR-07_FMT_wawasan-guns-for-crucial-police-vote-through-retired-senior-officers_..._rss.md` — **FRESH 07:30 MYT, Wawasan police-vote strategy; Razali Abu Samah = Sikamat candidate**
- `priority_PIR-06-PIR-07_FMT_wawasan-sasar-undi-penting-polis-melalui-pegawai-kanan-bersara_..._rss.md` — BM version of above
- `priority_PIR-06-PIR-07-PIR-16_FMT_noh-omar-hopes-bn-pn-formula-sparks-blue-wave-in-selangor_..._rss.md` — **Noh Omar: blue wave Johor→NS→Selangor→Putrajaya GE16**
- `priority_PIR-06-PIR-07-PIR-16_malaymail_jalaluddin-thanks-perikatan-for-backing-bn-to-lead-negeri-sembilan-..._home.md` — **PN concedes MB to BN; MB candidates Tok Mat/Sufian Maradzi**
- `priority_PIR-06-PIR-16_FMT_felda-umno-ties-tough-to-undo-..._rss.md` + `..._hubungan-felda-umno-sukar-..._rss.md` — **FRESH 08:00 MYT, Felda voter-bloc; Umno-PAS seat-sharing**

**PIR-16:**
- `priority_PIR-06-PIR-07-PIR-16_utusan_syarikat-dicadangkan-muhyiddin-terima-rm24-4-juta-bayaran-projek-jana-wibawa_..._home.md` — **Muhyiddin graft trial; RM24.4m Felda Bukit Jalor–Gemas NS road**
- `priority_PIR-06-PIR-07_sinarharian_cabar-mencabar-ujian-baharu-kerajaan-perpaduan-menjelang-prn-negeri-sembilan-..._home.md` — **Sinar analysis: unity-govt test; Akmal/AMH resignation challenge**

**PIR-07:**
- `priority_PIR-06-PIR-07-PIR-16_malaymail_six-negeri-sembilan-seats-that-could-tell-the-story-of-the-election-..._home.md` — **FRESH 20 Jul 7am, 6-seat analysis (Rantau/Chennah/Linggi/Lenggeng/Lukut/Nilai)**
- `priority_PIR-06-PIR-07-PIR-16_malaymail_negeri-sembilan-polls-cousins-turn-political-rivals-in-three-way-contest-for-kla_..._home.md` — **Klawang 3-corner: Bakri Sawir (PH) vs Danni Rais (PN) vs Muhammad Adib Musa (Bersatu)**
- `priority_PIR-06-PIR-07_malaymail_forget-big-walkabouts-aminuddin-says-he-d-rather-meet-linggi-voters-one-on-one-..._home.md` — **Aminuddin one-on-one Linggi; 20,677 voters incl 2,222 military**
- `priority_PIR-06-PIR-07-PIR-16_utusan_aminuddin-pilih-kempen-bersemuka_..._home.md` — **FRESH 20 Jul 7:59am, Utusan BM corroboration of Aminuddin Linggi**

### Full-text recoveries of prior headline-intel (3 — enrichments, same events)
- `priority_..._FMT_khaled-urges-voters-to-ensure-repeat-of-bersatu-s-johor-wipeout-in-ns_..._rss.md` — full RSS text (prior 233400 = headline-intel)
- `priority_..._FMT_bersatu-hanya-kacau-daun-khaled-gesa-pengundi-n-sembilan-bagi-ko_..._rss.md` — full RSS text (prior 171500 capture)
- `priority_..._FMT_ph-targets-23-seats-for-safe-majority-in-negeri-sembilan-says-loke_..._rss.md` — full RSS text (prior 171500 capture) + BM `..._ph-sasar-menang-23-kerusi-..._rss.md` — **[CRITICAL] corrected to FALSE POSITIVE**

### Duplicates (re-saved, already captured in prior cycles — ~8)
- `priority_..._malaymail_pakatan-to-reveal-its-game-plan-for-negeri-sembilan-polls-with-new-manifesto-mon_..._home.md` (dup 171500 — PH manifesto Monday)
- `priority_..._malaymail_win-but-not-by-breaking-the-law-loke-urges-road-safety-..._home.md` (dup 034922 — Loke road safety, Utusan version prior)
- `priority_..._utusan_gabungan-bn-pn-tekad-rampas-negeri-sembilan_..._home.md` (BN-PN vows to seize NS — prior Utusan)
- `priority_..._utusan_negeri-sembilan-penentu-kerjasama-pru16-..._home.md` (dup — NS determines PRU16, prior)
- `priority_..._FMT_tak-payah-desak-kuasa-pm-tentu-jawatan-menteri-kata-khaled_..._rss.md` (Khaled — prior)
- `priority_..._utusan_analisis-mampukah-percaturan-bn-pn-tumbangkan-anthony-loke-..._home.md` (analysis: can BN-PN unseat Loke — prior Utusan analysis)
- `priority_..._utusan_jaga-disiplin-kempen-prn-atau-letak-jawatan-menteri-..._home.md` (campaign discipline / Anwar warning — prior)
- `priority_..._FMT_7-tahun-berdepan-perbicaraan-nasib-zizie-izette-..._rss.md` (Zizie court — incidental, not PRN)

### False positives (25 — World Cup / geopolitics / sports / court / non-NS)
World Cup football (×9): `..._Awani_piala-dunia-*`, `..._FMT_sepanyol-juara-piala-dunia-*`, `..._FMT_trump-lingers-on-stage-...world-cup-*`, `..._FMT_madonna-shakira-bieber-...halftime-*`, `..._FMT_argentina-spain-fans-flood-new-york-...world-cup-*`, `..._Awani_puluhan-ribu-gegar-dataran-merdeka-...piala-dunia-*`, `..._Awani_piala-dunia-air-mata-seorang-raja`, `..._Awani_piala-dunia-dari-dukungan-messi-*`, `..._Awani_trump-bantu-sampaikan-trofi-piala-dunia-*`.
Geopolitics (×8): `..._FMT_israel-warns-...iran-*`, `..._FMT_iraqi-pm-to-visit-iran-*`, `..._FMT_israelis-march-to-gaza-border-*`, `..._FMT_rubio-hails-lebanon-*`, `..._FMT_russian-opposition-figure-nadezhdin-*`, `..._FMT_dollar-firmer-...us-iran-*`, `..._FMT_gold-falls-...us-iran-*`, `..._FMT_israel-warns-...iran-*`.
Sports (×4): `..._FMT_hamilton-rues-...belgian-gp-*`, `..._FMT_mercedes-boss-...russell-*`, `..._FMT_mcgregor-...acl-meniscus-*`, `..._FMT_left-knee-issues-...ohtani-*`.
Other non-NS (×4): `..._Awani_sampel-salad-positif-parasit-*` (US parasite outbreak), `..._Awani_hujan-lebat-landa-new-york-*` (NY flooding), `..._FMT_us-immigration-officers-...body-cameras-*`, `..._FMT_international-regulatory-conference-*` / `..._FMT_dari-bilik-darjah-ke-makmal-...siber-*` (cyber), `..._FMT_why-work-feels-harder-...productivity-*`.

### Index/analysis JSONs (this cycle)
- `_surge_results_20260720_morning.json` — full scrape results
- `_gnews_headlines_20260720_morning.json` — 331 gnews priority headline-intel items
- `_classification_20260720_morning.json` — 51-file classification (note: crude heuristic; manual verification superseded it — see §CRITICAL + file inventory)

---

## 📈 CYCLE DELTA: 233400 → 20260720_morning (07:34 → 09:11 MYT 20 Jul, ~1h37m)
- **Prior titles baseline:** 3,806 (all 17 prior cycles 011915→233400, ~2,150+ files in 20260719)
- **Articles saved:** 51 (11 genuinely-new + 3 full-text recoveries + ~8 dups + 25 false positives + 4 incidental)
- **Genuinely-fresh post-cutoff (≥07:34 MYT 20 Jul):** **5** — Pemuda PKR (07:00 MYT, just before cutoff), Wawasan police vote (07:30), Felda-Umno (08:00), Six seats analysis (07:00), Aminuddin bersemuka Utusan (07:59). [Note: Pemuda PKR 07:00 & Wawasan 07:30 & Six-seats 07:00 are technically 0–34 min before the 07:34 cutoff but were NOT captured by the prior 233400 cycle and contain new intel — counted as new-to-collection.]
- **Genuinely-new-to-collection (pre-cutoff, newly-surfaced):** 6 — Noh Omar blue wave, Jalaluddin thanks Perikatan, Muhyiddin Jana Wibawa, Klawang cousins, Aminuddin Linggi one-on-one, Sinar analysis.
- **PIR-06 status:** [CRITICAL] MAINTAINED (Kiandee quorum, prior 075200). **18th cycle with no [CRITICAL] threshold crossing.** NEW cooperation-friction intel: PKR Youth "topple-Anwar" framing, Wawasan police-vote strategy, PN concedes MB to BN, Noh Omar GE16 blue-wave, Felda-Umno seat-sharing.
- **PIR-16 status:** NOT [CRITICAL]. **18th cycle with no "Bersatu exit imminent"/"sasar bentuk kerajaan negeri" hard-news corroboration.** NEW: Muhyiddin Jana Wibawa NS-road graft detail; "makmal politik PRU16" framing via Noh Omar; Sinar unity-govt-test analysis.
- **Source status:** Awani RSS (200, 10 items) + FMT RSS (200, 50 items, content:encoded) working. NST + MalayMail RSS feeds failed (JS/403) — compensated by homepage slug-hint extraction (MalayMail 41 links → 6 saved; Utusan 61 → 7 saved; Sinar 19 → 1 saved). Google News RSS (200) surfaces historical matches only (0 fresh). gnews protobuf resolution still curl-infeasible (18th cycle).
- **False-positive pattern (5th consecutive cycle):** World Cup final (19 Jul) content still present in Awani/FMT morning feeds (9 of 25 false positives). Receding as campaign content dominates. Substring false matches: `pn`/`wee`/`hadi`/`nga`/`loke`/`majoriti`/`sasar` incidental.

---

## 🎯 NEXT-CYCLE RECOMMENDATIONS (10:30–14:00 MYT window)
1. **PIR-06 ([CRITICAL] watch):** Maintain formal-removal watch. Re-poll gnews for Bersatu Supreme Council quorum statement, PN Supreme Council convening to "assess Bersatu's position," RoS intervention, Muhyiddin "new coalition" formalization, Bersatu candidate withdrawal, **PDM Klawang reopen** (now hour 16+ — 20 Jul MYT business hours; Jalaluddin "1–2 days" window may materialize today). Re-poll "lebih-hebat" + "pn-supreme-council" + "kuorum Bersatu" + "gabungan baharu" + "KO Bersatu".
2. **PIR-06 (NEW threads to track):** (a) PKR Youth "topple-Anwar" framing — does it draw a PH/Anwar/BN response? (b) Wawasan police-vote strategy + Razali Abu Samah Sikamat campaign — capture Sikamat ground coverage. (c) PN-MB-concession (Jalaluddin) — does PH/AMH respond to "PN concedes MB"? (d) Felda-Umno seat-sharing — does it formalize?
3. **PIR-07:** Capture midday/evening Day-2 campaign dispatches (ceramah/walkabout/ops-centre) for T1 seats: Linggi (Aminuddin vs Faizal crossed paths — capture follow-up), Sikamat (Razali police-vote), Klawang (cousins), Pertang (Jalaluddin), Rantau (Tok Mat), Chennah (Loke), Johol (Khaled's launch site). **PH MANIFESTO LAUNCH 20 JUL EVENING** (Amirudin Shari) + **BN MANIFESTO 24 JUL at DUN Linggi + Pertang** — capture all coverage when published. Verify state-assembly dissolution date (June 5 vs June 26 discrepancy).
4. **PIR-16:** MCA rebuttal watch (Wee/Mah still silent). Track Muhyiddin Jana Wibawa trial next hearing. Verify the "PH sasar 32 kerusi" vs "8123/23-seat" discrepancy (two-tier target?). Track whether Noh Omar "blue wave GE16" draws Bersatu/PN formal response.
5. **Source maintenance:** Malay Mail homepage extraction is now a **proven high-yield path** (6 new articles this cycle) — prioritize it. Sinar Harian homepage extraction also worked (1 new analysis). Re-poll FMT/Awani RSS for post-09:11 MYT items. Try mkini 780631–780690.

---

## ⚠️ COLLECTION LIMITATIONS (honest disclosure)
- **gnews freshness:** gnews RSS returns historical matches (latest 19 Jul; 0 post-cutoff). Fresh Day-2 content was captured via direct RSS feeds (FMT/Awani) and **homepage slug-hint extraction** (Malay Mail/Utusan/Sinar) — NOT via gnews. gnews protobuf URL resolution remains curl-infeasible (18th cycle).
- **NST + MalayMail RSS feeds:** NST `/feed/rss/nation` and MalayMail `/rss` returned 0 items (JS-rendered/403). Compensated by homepage link extraction (MalayMail: 41 candidate links → 6 saved; NST: 8 links → 0 saved after PRN filter). Malay Mail homepage extraction is the cycle's **single largest new-content gain** (6 of 11 genuinely-new articles).
- **[CRITICAL] auto-flag false positive:** The auto-detector misfired on "sasar"/"majoriti"/"sasar bentuk" in the Loke 23-seats article (PH's seat target, not "Bersatu sasar bentuk kerajaan negeri"). Corrected via patch. **Net genuine [CRITICAL] = 0.** The detector's PIR-16 critical-trigger substring matching needs tightening to require "Bersatu" co-occurrence with "sasar bentuk kerajaan negeri".
- **World Cup false positives (5th cycle):** 9 of 25 false positives are World Cup final content; expected to recede. Substring false-matches on `pn`/`wee`/`hadi`/`nga`/`loke` documented.
- **Date discrepancy:** Malay Mail (Aminuddin article) states state assembly dissolved **June 5**; prior index/cycles used **June 26**. Flagged for verification — does not affect collection.
- **HarianMetro / BH homepage:** 0 candidate links extracted (site structure / JS). Harian Metro /feed remains a stable full-text source per prior cycles (not re-fetched this cycle — FMT RSS + homepage extraction covered the yield).
- **mkini:** Not polled this cycle (prior 17 cycles confirmed paywall + 24h lag); NS coverage lags RSS/gnews.

---

*Index generated 2026-07-20 09:12 MYT (01:12 UTC) by PRN Negeri Sembilan 2026 News Collection Agent — Nomination-Day Surge Mode. TLP:AMBER. All content carries source URL. [CRITICAL] flag on Kiandee quorum escalation MAINTAINED from prior 075200 cycle (no formal-threshold crossing this cycle; 18th cycle with no [CRITICAL] threshold crossing). One auto-flagged [CRITICAL] corrected to FALSE POSITIVE (PH 23-seat target misfire). 11 genuinely-new analytically-material articles collected (5 fresh post-cutoff + 6 new-to-collection). Malay Mail homepage extraction = largest new-content gain. gnews critical-keyword scan = 0 hits.*

---

# CYCLE: `20260720_midday` — collected 02:19–02:26 UTC 20 Jul (10:19–10:26 MYT 20 Jul)

**Fetcher:** `_surge_fetch_20260720_midday.py` (FMT RSS full content:encoded + Awani RSS + homepage slug-hint extraction NST/Star/MalayMail/Utusan/Sinar) + targeted Sinar article-ID scan + `_targeted_sinar_extract_20260720_midday.py`
**Prior cycle:** `20260720_morning` (ended 01:12 UTC / 09:12 MYT 20 Jul) — used as freshness cutoff
**Method:** Reused morning methodology verbatim (cutoff = morning cycle end). Plus targeted Sinar article-ID iteration (788520–788588) to recover high-value PIR-16 narrative articles referenced in sidebars but not captured by homepage slug-hint extraction.

## MIDDAY CYCLE SUMMARY

| Metric | Value |
|---|---|
| Articles saved (script) | 36 |
| Articles saved (targeted Sinar extract) | 6 |
| **Articles saved (total)** | **42** |
| Genuine PIR-06 [CRITICAL] threshold crossings | **0** (19th cycle — confirmed) |
| Auto-flagged [CRITICAL] in saved files | 1 → **FALSE POSITIVE (corrected)** — see §CRITICAL-midday |
| Genuinely-NEW analytically-material articles | **~15** (8 PIR-06 + 4 PIR-16 + 5 PIR-07; some BM/EN dup pairs) |
| Duplicates (re-saved, already captured prior cycles) | ~6 (PKR Youth EN-of-BM; Aminuddin Utusan-of-MalayMail; Loke campaign Sinar+MalayMail same event; PH 23-seats Sinar+MalayMail same event; PH-Selangor PKR Youth FMT EN+BM) |
| False positives (World Cup / geopolitics / sports / court / health / markets / movie / AI) | ~14 |
| Sinar Premium paywall (intro-only) | 1 (788548 "PH jual prestasi, BN-PN laung penyatuan Melayu-Islam") |
| Date discrepancy RESOLVED | DUN dissolved **June 5** confirmed (Sinar/Bernama manifesto article) |

---

## 🔴 PIR-06 — COALITION OPERATIONAL ARRANGEMENT — [CRITICAL] NOT CROSSED (19th cycle)

**[CRITICAL] status: MAINTAINED. NO NEW THRESHOLD CROSSING this cycle.** No formal PN-MT expulsion notice; no Bersatu candidate withdrawal (24 solo Bersatu-logo candidates stable); no Kiandee/PN quorum escalation; no "lebih hebat new coalition" formalization; no RoS intervention; no PDM Klawang reopening. CRITICAL auto-flag = FALSE POSITIVE (Madagascar "pecat" in sidebar, NOT PN context — corrected).

**NEW PIR-06 intelligence this cycle (cooperation-friction + operational strategy):**

1. **Tok Mat frames BN-PN as "electoral strategy not political coalition"** (Sinar 788524, Rembau, Ahad) — `priority_PIR-06-PIR-07-PIR-16_sinarharian_prn-negeri-sembilan-bn-tidak-pernah-burukkan...moham`. BN deputy chairman Mohamad Hasan (Rantau candidate, Foreign Minister): BN never badmouths anyone during campaign; BN-PN understanding in NS is NOT a political coalition but an electoral strategy/tactical consideration; BN didn't contest some seats based on past performance (not BN strongholds). Responds to Anwar's warning not to use govt position to attack federal allies. Warns voters vs fake social media. Early voting 28 Jul, polling 1 Aug. **KEY framing — distinguishes "strategy" from "coalition" to manage unity-govt optics.**

2. **KJ: BN-PN formula "could expand to Selangor"; NS as "makmal politik" test** (Sinar 788569, Shah Alam, Ahad, pub 20 Jul 08:03 MYT) — `priority_...formula-bn-pn-di-negeri-sembilan-mungkin-ke-selangor-kj`. Khairy Jamaluddin: NS BN-PN formula could expand to Selangor if it unites Malay votes (Selangor similar demographics). "Wait for NS results first." Political experiment to test Malay vote unity. If Malay votes don't split, can win Selangor. BN-PN cooperation = signal something wrong with unity govt. **BUT BN should NOT leave federal govt now** — stability priority until GE16. Reinforces "penyatuan undi Melayu" + "makmal politik" framing (cf. Noh Omar morning, but KJ more measured).

3. **UMNO Kapar Youth reinforces: BN-PN formula "should expand to Selangor"** (Sinar 788523) — `priority_...formula-kerjasama-bn-pn-perlu-diperluas-ke-selangor-pemuda-umno-kapar`. Echoes KJ; grassroots UMNO Youth picking up the "NS as test for Selangor" frame.

4. **UMNO-PAS: "Tiada yang mustahil dalam politik"** (Sinar 788549) — `priority_...umno-pas-tiada-yang-mustahil-dalam-politik`. Reconciliation framing — "nothing is impossible in politics" re: UMNO-PAS cooperation.

5. **Selangor PKR Youth: reassess PH-BN ties** (FMT, 20 Jul 09:29 MYT; EN+BM) — `priority_...selangor-pkr-youth-urges-ph-to-reassess-ties-with-bn` + `priority_...ph-selangor-digesa-kaji-semula-kerjasama-bn`. Selangor PKR Youth deputy chief Shahrul Adnan: PH should reassess BN ties after BN-PN NS cooperation. "If BN is free to work with PN to oppose PH in NS, why should PH regard BN cooperation as beyond question?" PH-BN formed Selangor govt (34/56 in 2023); PN got 22. **EXPANDS the morning's "Pemuda PKR topple-Anwar" thread to Selangor PKR Youth** — intra-PH pressure to break with BN at state level, triggered by NS BN-PN cooperation.

6. **Hamzah defends PAS vs Muhyiddin's "toxic PN" claim** (Sinar, Ahad) — `priority_...jangan-tuduh-pas-toksik...hamzah`. Hamzah Zainudin (Wawasan president) rebuts Muhyiddin: don't call PAS "toxic," remember who helped you become PM (UMNO+PAS). Claims the "PN" name originated from him + 2 friends in Mahathir era. Wants to "return government under a stronger group" — "gabungan bukan hanya di Johor, tetapi juga di negeri-negeri lain." **Intra-opposition friction (Bersatu vs PAS/Wawasan).** NOT [CRITICAL] (no formal expulsion/withdrawal). Auto-flag = FALSE POSITIVE.

7. **Hamzah "kekuatan sebenar gelombang biru"** (Sinar, FB post Ahad) — `priority_...berucap-di-pentas-umno-hamzah-kata-inilah-kekuatan-sebenar-gelombang-biru`. Hamzah: "true strength of blue wave" = unity of hearts across parties, not just coalition. Sepentas with UMNO's Alwi Che Ahmad + PAS sec-gen Takiyuddin Hassan at UMNO Seremban permanent chairman's residence. Cross-party unity messaging (machinery sharing / joint appearance).

8. **Khaled: "Kalau orang dah tak suka, buat apa nak tunggu" + Tok Mat willing to relinquish Cabinet post** (Sinar 788529, Kuala Pilah, Ahad) — `priority_...kalau-orang-dah-tak-suka-buat-apa-nak-tunggu-khaled-nordin`. UMNO VP Khaled Nordin: appointing/sacking ministers is PM's prerogative — "if people don't like you, why wait?" Responding to Anwar's Ipoh warning. Khaled: PRN campaign should focus on state issues, not attacks. **Tok Mat separately says he doesn't mind relinquishing Cabinet post if PM orders**, asserts no BN leader badmouthed unity govt. "Resign-to-attack" / Cabinet-discipline friction thread escalating.

---

## 🟠 PIR-16 — DOMINANT CAMPAIGN NARRATIVES — ESCALATION CONFIRMED (no hard-news [CRITICAL] corroboration of "Bersatu exit imminent")

**[CRITICAL] corroboration check: NO hard-news outlet corroborated "Bersatu exit imminent?" or "sasar bentuk kerajaan negeri" as fact. The "Bersatu kacau daun" narrative (Khaled morning) continues as characterisation, not formalised event. PIR-16 [CRITICAL] = NOT crossed.**

**NEW PIR-16 intelligence this cycle:**

1. **Dominant narrative dichotomy crystallised: "PH jual prestasi, BN-PN laung penyatuan Melayu-Islam"** (Sinar 788548, pub 20 Jul 09:00 MYT) — `priority_...ph-jual-prestasi-bn-pn-laung-penyatuan-melayu-islam`. Sinar analysis: NS expected to be among fiercest contests due to political realignment; PH campaigns on performance/governance record; BN-PN chants "Malay-Islam unity" (penyatuan Melayu-Islam). **This is the dominant campaign-narrative framing for PIR-16.** (Sinar Premium paywall — intro only; full text gated. Title + intro captured.)

2. **Loke: campaign on policies not personal attacks; NOT campaigning in Rantau** (Sinar BM 788528 + MalayMail EN, same PH-dinner event, pub 20 Jul 09:15–09:24 MYT) — `priority_...kempen-patut-tumpu-tawaran-bukan-serangan-peribadi-anthony` + `priority_...anthony-loke-urges-campaign-on-what-parties-offer`. Loke won't attack Cabinet colleagues (meet weekly, share responsibilities); follows Anwar's discipline advice. **NEW: Loke NOT campaigning in Rantau (Tok Mat's seat) to preserve unity-govt harmony** — focuses on Chennah (his seat) + DAP seats + helps Aminuddin in Linggi. Transport Minister role benefits Chennah (Kampung Madani projects). Confirms morning's "Loke staying away from Rantau" intel.

3. **PH targets 23 seats** (Sinar BM 788532 titled "32 kerusi" + MalayMail EN titled "23") — `priority_...ph-sasar-menang-32-kerusi` + `priority_...pakatan-sets-23-seat-target`. PH has 17 seats, needs 19 for simple majority, targets 23 for stability. "23 is realistic." Loke + Gobind (DAP chairman) + Nie Ching + Cha Kee Chin present. Aminuddin to continue as MB (honest, humble, not corrupt). **TITLE-BODY DISCREPANCY: Sinar BM title says "32 kerusi" but body says "23" — likely title error; MalayMail EN clearly says 23.** Loke confirmed Seremban MP + Chennah assemblyman.

4. **Nie Ching: PH needs mandate for Madani agenda; DAP won't give up after Johor** (Sinar 788527, PH dinner) — `priority_...ph-perlu-terus-diberi-mandat-laksana-agenda-madani-nie-ching`. DAP Women's chief Teo Nie Ching (Deputy Comm Minister, Kulai MP): PH needs mandate to continue Madani reforms. Federal achievements: economy, pension reform, education (10A SPM matrikulasi guarantee). Spoke in Mandarin + English translation. DAP won't give up despite Johor PRN defeat — will muhasabah without sacrificing principles.

5. **KJ "Ada sesuatu yang tak kena dalam Kerajaan Perpaduan"** (Sinar 788573, pub 20 Jul 09:19 MYT) — `priority_...ada-sesuatu-yang-tak-kena-dalam-kerajaan-perpaduan-kj`. KJ: BN-PN cooperation = signal something is wrong with the unity government. (Reinforces "makmal politik" / unity-govt critique frame.)

---

## 🔵 PIR-07 — HIGHEST-PRIORITY BATTLEGROUNDS — Day-2 ground intel + manifesto confirmation

1. **PH manifesto launch confirmed: "malam esok" (Mon 20 Jul evening)** (Sinar 788505/manifesto article, Ahad press conf) — `priority_...ph-umum-manifesto-esok`. PH manifesto = continuity of development/prosperity since PH led state since 2018. PH war room director Muhammad Zaki Md Sabri. Day-2: satisfied with logistics, positive voter response. Urges healthy campaign, avoid 3R. **KEY DATA RESOLVED: DUN dissolved 5 Jun (June 5, not June 26)** — Sinar/Bernama confirms; polling 1 Aug; early voting 28 Jul; **889,490 voters = 867,151 ordinary + 16,884 military+spouses + 5,455 police**.

2. **Aminuddin small-team campaign in Linggi** (Utusan, 19 Jul 15:20, pub 20 Jul) — `priority_...aminuddin-lebih-selesa-berkempen-bersama-pasukan-kecil`. Aminuddin (Linggi candidate, caretaker MB, PD MP): prefers small-group campaign since 2008. Linggi challenge = many kampung (slower than taman perumahan). Met voters at Pasir Panjang, PD. Positive reception but uncertain if translates to votes. **MB status = NOT an advantage (caretaker govt only, can't make decisions).** Similar to morning's MalayMail "forget big walkabouts" but Utusan BM with new details (kampung vs taman challenge, caretaker clarification, Pasir Panjang location).

3. **Arul Kumar confident defending Nilai without BN** (FMT BM+EN, 20 Jul 08:30 MYT) — `priority_...calon-dap-arul-kumar-yakin-pertahan-nilai-tanpa-bn` + `priority_...dap-s-arul-kumar-bullish-on-retaining-nilai-without-bn`. **N.10 Nilai 5-corner (FRESH):** Arul Kumar (DAP/PH, Adun since 2013) vs Lai Chien Kong (BN) vs V Saravan Kumar (Bersatu) vs Zamani Ibrahim (Berjasa) vs Omar Isa (independent). Won 2023 with 10,889 majority (1v1 vs PN). GE15 won ~10,000 without BN. Demographics (FMT): Malay 46.4%, Chinese 30%, Indian 20.8% (cf. morning MalayMail: 42.5/32.6/21.9 — minor discrepancy). Race narrative may reduce majority. NS differs from Sabah/Johor DAP decline (PH is incumbent).

4. **Felda Palong ground survey** (FMT, 20 Jul 09:00 MYT) — `priority_...rumah-terbengkalai-klinik-tertangguh-tuntutan-utama-penduduk-felda-palong`. Jempol district. Voter concerns: abandoned 2nd-gen housing (>10 yrs), Felda Palong 7 clinic stalled, jobs (60%+ youths leave), infrastructure. Pure ground/voter-intel for Felda seat context.

5. **BN Johol machinery launch + candidate "Iltizam Johol"** (Sinar 788575, pub 20 Jul 08:58 MYT) — `priority_...bukan-janji-bulan-dan-bintang-tetapi-rekod-dan-iltizam-johol`. BN DUN Johol candidate: "not moon-and-stars promises, but record and Iltizam Johol." Jentera BN Johol launch (Mohamed Khaled presided).

---

## §CRITICAL-midday — AUTO-FLAG FALSE POSITIVE (corrected)

**File:** `priority_PIR-06-PIR-07_sinarharian_jangan-tuduh-pas-toksik...hamzah` — auto-flagged [CRITICAL] because the substring "pecat" appeared in the body. **Verified FALSE POSITIVE:** the word "pecat" came from an **unrelated Madagascar news headline** ("Presiden Madagascar pecat Perdana Menteri, keseluruhan Kabinet") scraped into the article's related-items sidebar — NOT in any PN/Bersatu context. The Hamzah article's actual substance (defending PAS vs Muhyiddin's "toxic" characterisation) is genuine PIR-06 intelligence but does NOT meet any [CRITICAL] threshold (no formal expulsion/withdrawal/quorum/"lebih hebat new coalition" formalization). **Net genuine [CRITICAL] this cycle = 0.** (19th cycle with no [CRITICAL] threshold crossing.)

---

## ⚠️ COLLECTION LIMITATIONS (midday cycle)

- **Sinar Premium paywall:** Article 788548 ("PH jual prestasi, BN-PN laung penyatuan Melayu-Islam") is behind Sinar Premium — only intro paragraph + title captured. Title + intro still provide the dominant-narrative framing intelligence. Full text gated behind RM7.90–71.90 subscription.
- **Sinar homepage slug-hint extraction gaps:** Several high-value Day-2 Sinar articles (penyatuan Melayu-Islam, KJ "ada sesuatu tak kena", Khaled, UMNO-PAS, UMNO Kapar, Johol) were NOT captured by the morning/midday homepage extraction (slug-hint keywords didn't match). **Recovered via targeted article-ID scan (788520–788588)** + extraction script — a new methodology addition this cycle. 6 articles recovered.
- **False positives (14):** World Cup final content (Spain/Trump/FIFA/Mbappe/Paredes), geopolitics (Senegal ECOWAS/Iran Hormuz/West Africa pipeline), health (gut bacteria), markets (ringgit/Bursa), movie (Odyssey), AI, women's autonomy, court (Zizie Izette acquitted — non-PRN). Expected to recede post-World Cup.
- **Dup pairs:** PKR Youth (FMT EN+BM), Arul Kumar Nilai (FMT EN+BM), Loke campaign (Sinar BM + MalayMail EN same event), PH 23-seats (Sinar BM + MalayMail EN same event) — both languages saved for completeness; cross-reference for nuance.
- **Date discrepancy RESOLVED:** Morning cycle flagged June 5 vs June 26 for DUN dissolution. **Midday Sinar/Bernama manifesto article confirms June 5.** Resolved.

---

*Midday cycle index appended 2026-07-20 10:30 MYT (02:30 UTC) by PRN Negeri Sembilan 2026 News Collection Agent — Nomination-Day Surge Mode. TLP:AMBER. 42 articles saved (36 script + 6 targeted Sinar extract). ~15 genuinely-new analytically-material articles. [CRITICAL] NOT crossed (19th cycle; auto-flag = FALSE POSITIVE on Madagascar "pecat" in sidebar). Dominant narrative crystallised: "PH jual prestasi, BN-PN laung penyatuan Melayu-Islam." PH manifesto launch confirmed 20 Jul evening. DUN dissolution date resolved (June 5). Methodology addition: Sinar article-ID scan for sidebar-referenced headlines.*
