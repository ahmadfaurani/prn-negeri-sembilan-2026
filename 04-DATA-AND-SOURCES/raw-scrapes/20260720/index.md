# PRN Negeri Sembilan 2026 — Raw Scrapes Index
## Date: 2026-07-20 (Mon) | Campaign Day 2 | Nomination Day +2 | TLP:AMBER

**Workspace:** `04-DATA-AND-SOURCES/raw-scrapes/20260720/`
**Collection mode:** Nomination-Day Surge Mode (Director priority-approved PIR-06/07/16)
**Cycle:** `20260720_morning` — collected 01:09–09:12 MYT 20 Jul (09:09–09:12 MYT 20 Jul)
**Prior cycle:** `20260719_233400` (ended 07:34 MYT 19 Jul = 07:34 MYT 20 Jul) — used as freshness cutoff
**Polling day:** 2026-08-01 (Sat) | **Early voting:** 2026-07-28 | **Nomination day:** 2026-07-18 (Sat)
**Fetcher:** `_surge_fetch_20260720_morning.py` (Awani RSS full + FMT RSS full content:encoded + Google News RSS ×30 PIR-targeted queries + NST/Star/MalayMail/Utusan/HarianMetro/BH/Sinar homepage slug-hint extraction)

---

## CYCLE SUMMARY

| Metric | Value |
|---|---|
| Google News queries run | 30 (incl. 8 mandatory PIR-06 [CRITICAL]-watch: kuorum, lebih hebat, pecat, tarik diri, PN Supreme Council, machinery sharing, Wawasan Ridzuan, sole opposition) |
| gnews items returned | 487 (331 PRN/priority headline hits) |
| gnews **fresh** post-cutoff (≥07:34 MYT 19 Jul) | **0** (gnews RSS surfaces historical matches; latest dated 19 Jul) |
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

*Index generated 2026-07-20 09:12 MYT (09:12 MYT) by PRN Negeri Sembilan 2026 News Collection Agent — Nomination-Day Surge Mode. TLP:AMBER. All content carries source URL. [CRITICAL] flag on Kiandee quorum escalation MAINTAINED from prior 075200 cycle (no formal-threshold crossing this cycle; 18th cycle with no [CRITICAL] threshold crossing). One auto-flagged [CRITICAL] corrected to FALSE POSITIVE (PH 23-seat target misfire). 11 genuinely-new analytically-material articles collected (5 fresh post-cutoff + 6 new-to-collection). Malay Mail homepage extraction = largest new-content gain. gnews critical-keyword scan = 0 hits.*

---

# CYCLE: `20260720_midday` — collected 02:19–10:26 MYT 20 Jul (10:19–10:26 MYT 20 Jul)

**Fetcher:** `_surge_fetch_20260720_midday.py` (FMT RSS full content:encoded + Awani RSS + homepage slug-hint extraction NST/Star/MalayMail/Utusan/Sinar) + targeted Sinar article-ID scan + `_targeted_sinar_extract_20260720_midday.py`
**Prior cycle:** `20260720_morning` (ended 09:12 MYT / 09:12 MYT 20 Jul) — used as freshness cutoff
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

*Midday cycle index appended 2026-07-20 10:30 MYT (10:30 MYT) by PRN Negeri Sembilan 2026 News Collection Agent — Nomination-Day Surge Mode. TLP:AMBER. 42 articles saved (36 script + 6 targeted Sinar extract). ~15 genuinely-new analytically-material articles. [CRITICAL] NOT crossed (19th cycle; auto-flag = FALSE POSITIVE on Madagascar "pecat" in sidebar). Dominant narrative crystallised: "PH jual prestasi, BN-PN laung penyatuan Melayu-Islam." PH manifesto launch confirmed 20 Jul evening. DUN dissolution date resolved (June 5). Methodology addition: Sinar article-ID scan for sidebar-referenced headlines.*

---

# ▓▓▓ AFTERNOON CYCLE — 20260720_afternoon ▓▓▓

**Fetcher:** `_surge_fetch_20260720_afternoon.py` (Awani RSS + FMT RSS + Google News RSS ×30 PIR queries + NST/Star/MalayMail/Utusan/Sinar homepage extraction + PIR-07 evening ceramah queries)
**Collection window:** ~11:34 MYT 20 Jul (script execution)

## AFTERNOON CYCLE SUMMARY

| Metric | Value |
|---|---|
| Articles saved (afternoon script) | 23 |
| Duplicates skipped | 35 (URL dedup vs morning + midday) |
| Fresh gnews items post-cutoff | 1 |
| Genuine [CRITICAL] threshold crossings | **0** (20th cycle — confirmed) |
| Genuinely-NEW analytically-material articles | **6** (5 articles + 1 gnews-only Tok Mat intel) |
| Content duplicates (same Sinar article ID, different URL) | 3 (788573 KJ, 788529 Khaled, 788575 Johol — already captured midday) |
| False positives (non-PRN) | 12 (World Cup, court, tourism, cyber, Gobind Network School) |

---

## 🔴 PIR-06 — AFTERNOON UPDATES — [CRITICAL] NOT CROSSED (20th cycle)

**[CRITICAL] status: MAINTAINED. No formal PN-MT expulsion, no Bersatu candidate withdrawal, no Kiandee quorum escalation, no "lebih hebat new coalition" formalization. PDM Klawang reopening status UNRESOLVED — ~hour 18+ of Jalaluddin "1–2 days" window.**

### 1. PN concedes MB post to BN — Utusan BM corroboration [NEW outlet]
→ `priority_PIR-06-PIR-07_utusan_pn-beri-laluan-bn-jadi-mb-jika-menang-prn-negeri-sembilan_20260720_afternoon_home.md`
- Jalaluddin Alias (UMNO NS chairman) confirms PN made "deklarasi awal" to yield MB post to BN
- MB candidates named: **Tok Mat (Mohamad Hasan), Jalaluddin Alias, Sufian Maradzi (Seri Menanti candidate)** — final decision up to BN chairman
- BN-PN priority: win first, then discuss MB/Exco positions
- Events: Majlis Sepetang Bersama Masyarakat Orang Asli Kampung Putra, Jelebu + Program Hari Kemahiran Kemas Bahagian Jelebu at Felda Pasoh 4
- **Utusan BM corroborates morning MalayMail EN capture of same Jalaluddin statement — new outlet added.**

### 2. KJ: Malay vote unity could help BN-PN reclaim Selangor [NEW outlet — MalayMail EN via Kosmo!]
→ `priority_PIR-06-PIR-07-PIR-16_malaymail_khairy-malay-vote-unity-could-help-bn-perikatan-reclaim-selangor_20260720_afternoon_home.md`
- KJ: Selangor demographics similar to NS → NS results as "reference/test" for future strategies
- "If there is sincerity and commitment from both sides, we want to see whether BN supporters can vote for PAS candidates"
- "Something wrong with unity-govt cooperation, four years" — BUT BN should not leave govt (stability until GE16)
- **MalayMail EN corroboration of midday Sinar KJ article (788573) — new outlet. Adds "former Rembau MP" and "four years" framing.**

### 3. Noh Omar: UMNO-PAS cooperation could win 34/56 Selangor DUN + 6 parliament seats [GENUINELY NEW — detailed projections]
→ `priority_PIR-06-PIR-07-PIR-16_sinarharian_kerjasama-umno-pas-mampu-bentuk-kerajaan-selangor-noh-omar_20260720_afternoon_home.md`
- **NEW detailed seat projections:** ~34 of 56 DUN seats + 6 parliament (Kuala Selangor, Shah Alam, Sepang, Hulu Langat, Gombak, Sungai Buloh) winnable via straight fights
- NS formula = "pencetus gelombang politik" → Selangor → **PRU16**
- Related article referenced: "Noh Omar pertahan pendirian UMNO Johor, jawab kenyataan Anthony Loke" — **Noh-Loke exchange escalation**
- More detailed than morning FMT "blue wave" capture; specific seat numbers are NEW intel

---

## 🟠 PIR-16 — AFTERNOON UPDATES — ESCALATION (no [CRITICAL] corroboration)

**[CRITICAL] check: No hard-news outlet corroborated "Bersatu exit imminent?" or "sasar bentuk kerjaan negeri" as fact. "Makmal politik" and "penyatuan undi Melayu" narratives continue to escalate (KJ + Noh Omar) but remain characterisations, not formalised events. PIR-16 [CRITICAL] = NOT crossed.**

### 1. "Makmal politik" framing escalates — KJ + Noh Omar chain
- KJ (MalayMail EN): NS as "test/reference" for BN-PN cooperation → Selangor → GE16. Unity-govt critique: "something wrong, four years." (PIR-16 "makmal politik" + "Anwar not briefed" adjacent)
- Noh Omar (Sinar): NS formula → Selangor → PRU16. Specific seat projections (34/56 DUN, 6 parliament). (PIR-16 "makmal politik" + "majoriti mudah" adjacent)
- **Combined: The "NS = makmal politik for PRU16" narrative is now corroborated by 3 named UMNO figures (KJ, Noh Omar, Khaled morning) across 3 outlets (Sinar, MalayMail/Kosmo, FMT). Escalation confirmed but NOT [CRITICAL].**

### 2. Noh-Loke exchange escalation
- Sinar sidebar reference: "Noh Omar pertahan pendirian UMNO Johor, jawab kenyataan Anthony Loke"
- Noh responding to Loke's earlier statement (possibly re: UMNO Johor position or BN-PN cooperation)
- **NEW friction vector: Noh Omar vs Loke — track for escalation**

---

## 🔵 PIR-07 — AFTERNOON UPDATES — Ground intel + Klawang incident + Tok Mat absence

### 1. Police open 2 investigation papers at Kuala Klawang, Jelebu — election mischief [FRESH 10:50 MYT 20 Jul]
→ `priority_PIR-06-PIR-07_Awani_prn-negeri-sembilan-polis-buka-dua-kertas-siasatan-melibatkan-kesalahan-pilihan-_20260720_afternoon.md`
- NS PDRM opened 2 investigation papers for election offences (mischief causing property damage/loss)
- 3 police reports received in 2-day campaign; 2 for election offences
- **Location: Kuala Klawang, Jelebu** — PH flags, banners, bumper stickers damaged, thrown into drains
- Under Section 427 Penal Code (mischief causing damage/loss)
- Police chief: Datuk Azfanny Ahmad
- 109 permit applications received, 107 approved
- **PIR-07 significance:** Klawang (N.28) is a 3-corner fight (Bakri Sawir PH vs Danni Rais PN vs Muhammad Adib Musa Bersatu). Flag vandalism at Kuala Klawang = first documented election-related incident at a T1 battleground seat.

### 2. Loke at Pekan Titi, Jelebu — PH tailors campaign to local voter demographics [FRESH 11:10-11:26 MYT 20 Jul]
→ `priority_PIR-07-PIR-16_Awani_prn-negeri-sembilan-strategi-kempen-ph-ikut-keperluan-karakter-lokaliti-pengundi_20260720_afternoon.md` + `priority_PIR-07-PIR-16_malaymail_pakatan-tailors-campaign-strategies-in-negeri-sembilan-loke-says-each-village-ne_20260720_afternoon_home.md`
- Loke at Pekan Titi walkabout (Jelebu)
- PH strategy: tailor campaign to each village's character — Malay-dominant areas use Malay reps, Chinese areas use Chinese reps, mixed areas use mixed teams
- **Chennah = straight fight vs BN's Siow Kong Choon** (NEW candidate name confirmed)
- PH manifesto launch confirmed "malam ini" (tonight 20 Jul) — consistent with midday intel
- Campaign Day 3 smooth; all PH candidates on the ground
- **PIR-07 significance:** Chennah (N.06) BN opponent named; Loke's Jelebu outreach confirmed; PH manifesto timing confirmed for tonight

### 3. Tok Mat pauses campaign for Asean FM Meeting in Manila [gnews-only intel — 18-20 Jul]
→ `priority_PIR-07_googlenews_tokmat-pauses-campaign-asean-manila-meeting_20260720_afternoon_gnews.md`
- **TheStarTV.com (18 Jul): "Negri polls: Tok Mat pauses campaign for Asean meeting"**
- **MalayMail (20 Jul): "Mohamad Hasan says Asean ministers in Manila to confront Gaza killings, West Asia turmoil and rice security"**
- Tok Mat (Foreign Minister) absent from NS campaign since at least 18 Jul — in Manila for Asean FM meeting
- **PIR-07 significance:** Rantau (N.36, Tok Mat's seat) campaign running WITHOUT candidate physically present for 2+ days during critical early campaign period. Loke not campaigning in Rantau (per midday intel). Campaign vulnerability: PH could exploit "Tok Mat prioritises Manila over Rantau voters."
- **Note:** Full article text unavailable (Star URL 404; Google News redirect JS-rendered). Intel from Google News RSS headlines + MalayMail sidebar.

### 4. Jalaluddin at Orang Asli Kampung Putra + Felda Pasoh 4 (Jelebu) [from Utusan MB article]
- Majlis Sepetang Bersama Masyarakat Orang Asli Kampung Putra, Jelebu (19 Jul afternoon)
- Program Hari Kemahiran Kemas Bahagian Jelebu at Felda Pasoh 4
- **PIR-07 ground intel:** Jalaluddin (Jelebu MP, Pertang area) conducting Orang Asli + Felda outreach in Jelebu

---

## ⚠️ COLLECTION LIMITATIONS (afternoon cycle)

- **Tok Mat Asean article:** Full text unavailable — The Star URL returned 404; Google News redirect is JS-rendered splash page. Intel derived from Google News RSS headlines + MalayMail sidebar references. The article is from TheStarTV.com (video platform) which may have different URL structure.
- **3 Sinar content duplicates:** Articles 788573 (KJ), 788529 (Khaled), 788575 (Johol) had different URLs but same article IDs as midday captures — identified and excluded from genuinely-new count.
- **12 false positives:** FMT World Cup/court/cyber/tourism (8), Awani Network School/Gobind + Dataran Merdeka litter + TVET (3), Utusan FIFA World Cup (1). These are keyword-match artifacts from "negeri" or "sembilan" appearing in non-PRN contexts.
- **No Harian Metro/BH new content:** Both remained inaccessible (HTTP 000/404) — consistent with morning/midday cycles.
- **Google News freshness:** Only 1 fresh item post-cutoff (Tok Mat Manila). gnews RSS continues to surface mostly historical matches. Malaysian news cycle may be slower on Monday afternoon.

---

*Afternoon cycle index appended 2026-07-20 ~11:45 MYT by PRN Negeri Sembilan 2026 News Collection Agent — Nomination-Day Surge Mode. TLP:AMBER. 23 articles saved (afternoon script) + 1 gnews-only intel note. 6 genuinely-new analytically-material articles. [CRITICAL] NOT crossed (20th cycle). Key afternoon developments: (1) Police investigation papers at Klawang (N.28) for election mischief; (2) Loke at Pekan Titi walkabout + Chennah BN opponent named Siow Kong Choon; (3) Tok Mat absent from campaign — in Manila for Asean FM meeting (2+ days); (4) PN concedes MB to BN (Utusan BM corroboration); (5) KJ + Noh Omar escalate "makmal politik" narrative with Selangor seat projections; (6) Noh-Loke exchange emerging. PDM Klawang reopening status UNRESOLVED.*

---

# ▓▓▓ EVENING CYCLE — 20260720_evening ▓▓▓

**Fetcher:** `_surge_fetch_20260720_evening.py` (Awani RSS + FMT RSS + Google News RSS ×50 PIR queries + NST/Star/MalayMail/Utusan/Sinar/Kosmo/HarianMetro homepage extraction + PIR-07 evening ceramah queries + PDM Klawang reopen + PH manifesto launch) + `_targeted_sidebar_recovery_20260720_evening.py` (Sinar article-ID recovery via Wee Ka Siong article 788589 sidebar hrefs + gnews candidates)
**Collection window:** ~04:42–04:48 UTC 20 Jul (12:42–12:48 MYT 20 Jul)
**Prior cycle:** `20260720_afternoon` (ended ~03:40 UTC / 11:40 MYT 20 Jul) — used as freshness cutoff
**Method:** Reused afternoon methodology (cutoff = afternoon cycle end 03:40 UTC). Plus targeted sidebar-recovery: extracted related-article hrefs from the Wee Ka Siong article (788589) + gnews RSS searches for sidebar-referenced headlines (Onn Hafiz, Mohd Syahir, Ka Siong BN-PN, 103 calon, Loke "thanks MCA"), then fetched each Sinar article URL directly. 5 genuinely-new Sinar articles recovered.

## EVENING CYCLE SUMMARY

| Metric | Value |
|---|---|
| Articles saved (main script) | 20 |
| Articles saved (targeted sidebar recovery) | 5 |
| **Articles saved (total)** | **25** |
| Duplicates skipped (URL/slug dedup) | 23 |
| Genuine PIR-06 [CRITICAL] threshold crossings | **0** (21st cycle — confirmed) |
| Auto-flagged [CRITICAL] in saved files | 0 (tightened detector: now requires PN/Bersatu co-occurrence for PIR-06; requires "bersatu" co-occurrence for "sasar bentuk kerajaan negeri" PIR-16 — no false positives this cycle) |
| Genuinely-NEW analytically-material articles | **8** (3 from main script + 5 targeted recovery) |
| Duplicates (re-saved, new outlet only) | 1 (FMT BM police investigation papers = dup of afternoon Awani, pre-cutoff) |
| False positives (non-PRN) | 16 (Zizie court ×4, World Cup ×5, geopolitics Rubio ×2, markets ×1, UAE stranded ×1, Nur Jazlan Senate ×1, eFishery/KWAP federal ×3 [not yet re-classified as false-positive in saved files; flagged here]) |
| gnews queries run | 50 (incl. mandatory kuorum/lebih hebat/pecat/tarik diri/PDM Klawang + PH manifesto launch + Onn Hafiz + Mohd Syahir) |
| gnews total items | 508 (357 PRN/priority headline hits) |
| gnews **fresh** post-cutoff (≥03:40 UTC / 11:40 MYT 20 Jul) | **0** (gnews RSS surfaces historical matches; 21st cycle confirmation) |
| RSS feed items scanned | Awani main (10) + FMT (50) — NST/MalayMail/Sinar/Utusan RSS returned 0 (JS/403, same as prior cycles) |
| Homepage candidate links found | NST 8 / Star 8 / MalayMail 40 / Utusan 69 / Sinar 27 / Kosmo 2 (HarianMetro/BH 0) |
| Sidebar-recovery candidate URLs fetched | 46 (5 saved, 21 gnews JS-splash skips, 20 non-PRN/skip) |

---

## 🔴 PIR-06 — COALITION OPERATIONAL ARRANGEMENT — [CRITICAL] NOT CROSSED (21st cycle)

**[CRITICAL] status: MAINTAINED. NO NEW THRESHOLD CROSSING this cycle.** No formal PN-MT expulsion notice; no Bersatu candidate withdrawal (24 solo Bersatu-logo candidates stable); no Kiandee/PN quorum escalation; no "lebih hebat new coalition" formalization; no RoS intervention; no PDM Klawang reopening. All mandatory gnews [CRITICAL]-watch queries (kuorum, lebih hebat, pecat, tarik diri, PDM Klawang buka semula, RoS PN Bersatu) returned 0. PDM Klawang reopening status UNRESOLVED — now ~hour 20+ of Jalaluddin "1–2 days" window (20 Jul MYT business hours progressing).

**NEW PIR-06 intelligence this cycle (cooperation-friction + machinery transfer + MCA positioning):**

### 1. Wee Ka Siong MCA rebuttal to Loke — "Terima kasih Anthony Loke ingatkan MCA" [NEW, HIGH VALUE — PIR-16 carry-forward flag RESOLVED]
→ `priority_PIR-06-PIR-07-PIR-16_sinarharian_terima-kasih-anthony-loke-ingatkan-mca-ka-siong-sinar-harian_20260720_evening_home.md` (Sinar 788589, pub ~00:00 MYT 20 Jul "tengah malam Ahad", by Nurul Hidayah Hamid, 20 Jul 11:27am Sinar Politik sidebar)
- **MCA President Wee Ka Siong has now FORMALLY RESPONDED to Loke's "MCA biggest loser" remark** — resolves the PIR-16 carry-forward flag "MCA rebuttal to Loke quote; top leadership (Wee/Mah) still silent." Wee's response is CONCILIATORY, not aggressive:
  - Frames Loke's criticism as a "peringatan" (reminder) that helps MCA stay humble ("merendah diri") and not take any election for granted.
  - "Saya benar-benar berterima kasih kepada Anthony Loke kerana sentiasa mengingatkan semua pihak tentang kelemahan MCA. Kritikan menjadikan kami lebih merendah diri." (I truly thank Anthony Loke for always reminding everyone about MCA's weakness. Criticism makes us more humble.)
  - Acknowledges reality: **MCA has not won a single NS DUN seat since 2013** (13 years without a state assemblyman).
  - On MCA not contesting 3 traditional seats: decision based on assessment that chances were "terlalu tipis" (too thin) after big losses in those seats in previous elections. "Tiada gunanya berpura-pura sebaliknya." (No point pretending otherwise.)
  - 7 seats MCA IS contesting: believes they still have a chance to compete.
  - MCA must work harder, convince voters one-by-one; "MCA pada asasnya sedang bermula semula di Negeri Sembilan" (MCA is essentially starting afresh in NS).
  - References Johor: grateful voters gave MCA 3 DUN seats back in recent Johor PRN; hopes NS voters give MCA another chance.
- **Significance:** PIR-16 "MCA rebuttal" loop CLOSED. Wee's conciliatory "thanks-for-the-reminder" framing (rather than counter-attack) is a notable strategic choice — acknowledges weakness, positions MCA as humble/underdog. Mah Hang Soon (MCA deputy) still silent. NOT [CRITICAL] (no "Bersatu exit imminent"/"sasar bentuk kerajaan negeri" corroboration).

### 2. Ka Siong (Saturday press conf): BN-PN = vote-split avoidance, NOT merger; MCA = "semak dan imbang" [NEW outlet/intel]
→ `priority_PIR-06-PIR-07-PIR-16_sinarharian_kerjasama-bn-pn-elak-pecah-undi-ideologi-parti-tetap-kekal-ka-siong-sinar-harian_20260720_evening_targeted.md` (Sinar 788363, Saturday press conf Seremban)
- Wee Ka Siong's earlier (Saturday) framing of BN-PN cooperation, recovered via sidebar:
  - BN-PN cooperation is to avoid multi-cornered fights / vote splitting ("elak pecah undi"), NOT a merger. Each party keeps ideology/pendirian/peranan.
  - MCA joins to ensure Chinese/mixed-community/vernacular education/religious freedom have representation.
  - "Persefahaman berlandaskan kepentingan rakyat, bukan sokongan tanpa syarat" — understanding based on rakyat interest, NOT unconditional support. MCA will oppose any policy harming mixed-community rights.
  - **MCA positioning = "semak dan imbang" (check and balance)** within BN-PN.
  - Critique of DAP: "politik melabel dan retorik berunsur konfrontasi" (labelling politics + confrontational rhetoric) drove social division. "BN is the only party able to unite the middle ground."
  - **Unity-govt critique:** if Unity Govt is just power-sharing but fails reform/solve rakyat problems = **"perpaduan yang hipokrit" (hypocritical unity)**.
- **Significance:** PIR-06 (BN-PN = electoral strategy, not coalition — reinforces Tok Mat's midday framing) + PIR-16 (MCA check-and-balance positioning; unity-govt critique). Sidebar references NEW articles: "PRN NS: Polis terima satu laporan pertelingkahan mulut antara penyokong parti" (verbal clash between supporters — new incident), "PRN NS: 21 DUN lawan tiga penjuru" (21 DUN three-cornered), "PRN NS: DUN Pilah saksi pertembungan dua calon wanita" (DUN Pilah two-women contest).

### 3. Onn Hafiz brings BN Johor winning formula to NS — Johor→NS machinery transfer CONFIRMED [NEW, HIGH VALUE]
→ `priority_PIR-06-PIR-07-PIR-16_sinarharian_onn-hafiz-bawa-formula-kemenangan-besar-bn-johor-ke-negeri-sembilan-sinar-harian_20260720_evening_targeted.md` (Sinar 788481, Tampin event Ahad/Sunday 19 Jul, Dataran Kampung Tengah, Gemencheh)
- **Johor MB Datuk Onn Hafiz Ghazi** at Program Perjumpaan Jentera PRN NS + Pelancaran Gerak Gempur BN Tampin (Gemencheh, Sunday):
  - Two "secrets" of BN Johor victory: (1) **gerak kerja berpasukan** (teamwork — all component parties UMNO/MCA/MIC/Friends of BN moving in one saf/row); (2) jentera mematahkan fitnah/tohmahan/janji tidak realistik (machinery countering slander/unrealistic promises).
  - "Kita menangkan BN di Negeri Sembilan, insya-ALLAH" — confident BN can win NS if machinery maintains teamwork spirit.
  - **Johor youth volunteers physically coming to Tampin (Parlimen Tampin) to help NS campaign**: "Budak-budak Johor nak sokong budak-budak Negeri Sembilan. Kita datang untuk membantu." (Johor youth supporting NS youth. We came to help.) — **direct machinery-sharing confirmation.**
  - Present: Tampin UMNO chief **Datuk Mohd Isam Mohd Isa**; BN candidates **Suhaimizan Bizar (DUN Gemencheh)** + **Koh Kim Swee (DUN Repah)** — **NEW PIR-07 candidate names.**
  - Sidebar references: "Formula BN, PN di Negeri Sembilan mungkin ke Selangor - KJ", "'Buktikan penyatuan kita mampu gegar mereka' - Akmal Saleh", "Kejayaan PRN Johor jadi pembakar semangat BN cipta kemenangan di Negeri Sembilan - Ahmad Zahid" (Zahid: Johor victory = spirit-burner for NS).
- **Significance:** PIR-06 (machinery sharing — Johor→NS transfer confirmed with physical volunteer movement) + PIR-16 (Johor momentum narrative). New PIR-07 ground intel: Gemencheh + Repah BN candidates named. Akmal Saleh + Zahid statements referenced (next-cycle targets).

### 4. KJ: BN-PN = "isyarat kepada PH"; federal govt ignoring "sensitiviti orang Melayu" [FRESH 11:48 MYT, NEW outlet — FMT BM + EN]
→ `priority_PIR-06-PIR-07_FMT_kerjasama-bn-pn-isyarat-kepada-ph-kata-khairy_20260720_evening_rss.md` (FMT BM, dated 03:48 UTC = 11:48 MYT 20 Jul, FRESH) + `priority_PIR-06-PIR-07-PIR-16_FMT_bn-working-with-pn-to-send-ph-a-signal-says-khairy_20260720_evening_rss.md` (FMT EN, dated 03:18 UTC = 11:18 MYT, new-to-collection)
- **Khairy Jamaluddin** to reporters after **Subang Umno meeting (malam tadi / last night)**:
  - **BN-PN cooperation = "isyarat" (signal) to PH** — not a permanent break from unity govt.
  - **NEW sharper framing:** "Sebahagian ahli Umno merasakan kerajaan persekutuan kurang memberi perhatian terhadap sensitiviti orang Melayu" (some Umno members feel federal govt pays insufficient attention to **Malay sensitivities**), besides failing to fulfil promises.
  - PH uses Umno's presence in unity govt as excuse for reform failures: "Seolah-olah mereka menyalahkan Umno atas kegagalan mereka sendiri."
  - **BN should NOT leave unity govt or push for early GE** — "Kita boleh tunggu sehingga pilihan raya umum. Kita hanya mengambil peluang ini untuk memberi isyarat kepada PH supaya tidak memandang mudah Umno dan BN."
  - Context: PH-BN ties soured after BN went solo in Johor PRN (11 Jul); deteriorated further with BN-PN NS alliance.
- **Significance:** FMT (BM+EN) is a NEW outlet for KJ's signal-to-PH thread (prior: midday Sinar 788573 "ada sesuatu yang tak kena" + afternoon MalayMail "khairy-malay-vote-unity"). Adds "sensitiviti orang Melayu" (Malay sensitivities) as a sharper formulation — PIR-16 "Anwar not briefed"/unity-govt critique + "penyatuan undi Melayu" adjacent. Reinforces "makmal politik" framing. NOT [CRITICAL].

**Tier-4 seat watch (N.04, N.05, N.13, N.14, N.23, N.25, N.31, N.34):** No Bersatu candidate withdrawals. No new Tier-4 intel this cycle (Sikamat Wawasan Razali Abu Samah police-vote strategy from morning remains the latest).

---

## 🟠 PIR-16 — DOMINANT CAMPAIGN NARRATIVES — ESCALATION (no [CRITICAL] corroboration)

**[CRITICAL] check: NO hard-news outlet corroborated "Bersatu exit imminent?" or "Bersatu sasar bentuk kerajaan negeri" as fact. The "Bersatu kacau daun" characterisation (Khaled) and "makmal politik PRU16" framing (KJ + Noh Omar) continue to escalate but remain characterisations, not formalised events. PIR-16 [CRITICAL] = NOT crossed (21st cycle).**

### 1. MCA rebuttal loop CLOSED — Wee Ka Siong responds to Loke [HIGH VALUE — see PIR-06 #1]
- Wee's conciliatory "thanks-for-the-reminder" framing (Sinar 788589) closes the loop on Loke's "MCA biggest loser" remark (FMT/MalayMail 19 Jul + Sinar 788446 Sunday Pasar Besar Seremban).
- **Loke's original remark (Sinar 788446, recovered this cycle):** Loke sarcastically thanked MCA for "helping DAP" by not contesting 3 traditional seats (Lobak, Lukut, Mambau). Strategy = ensure PN doesn't contest MCA seats, redirect Malay voters to BN. Only at **Chennah** did strategy succeed (no 3-cornered with Bersatu). **MCA contests 7 seats: Chennah, Bahau, Nilai, Temiang, Rahang, Chuah, Repah** (article says "lima" but lists 7 — likely "tujuh" typo). **3 MCA seats NOT contested: Lobak (most Chinese voters in NS), Lukut (ex-MCA Dr Yao Chai Thiam, ex-Exco), Mambau (ex-MCA Exco Hew Chok Tau before 2008).**
- **Net narrative status:** Loke "biggest loser" → Wee "thanks for reminder" = exchange complete. MCA positioned as humble/underdog/starting-afresh. Mah Hang Soon still silent. NOT [CRITICAL].

### 2. Mohd Syahir (PAS) expands resign-narrative to Perak + Pahang; invokes DAP Melaka model [NEW, HIGH VALUE]
→ `priority_PIR-06-PIR-07-PIR-16_sinarharian_sepatutnya-pemuda-ph-desak-exco-perak-pahang-letak-jawatan-dulu-mohd-syahir-sina_20260720_evening_targeted.md` (Sinar 788502, Ahad/Sunday statement)
- **PAS MP Mohd Syahir Che Sulaiman (Bachok)** — NEW voice in the resign-narrative escalation:
  - Rebukes AMH's call for BN ministers to resign: "Why is PH so anxious in Putrajaya when BN-PN cooperation is limited to NS PRN 'persefahaman'?"
  - **Key argument:** When BN-PH clashed in 56 seats in Johor PRN, this resignation demand didn't arise. So why now for NS?
  - **"Sepatutnya Pemuda PH mendesak Exco PH di Perak dan Pahang meletakkan jawatan terlebih dahulu. Tindakan DAP Melaka wajar dijadikan contoh"** — PH Youth should demand PH Exco in **Perak and Pahang** resign first; **DAP Melaka's action should be the example/model.** (PIR-16 "Melaka withdrawal" / "Melaka PH-BN fracture" keyword directly invoked.)
  - BN-PN NS cooperation = avoid seat overlap, strengthen ummah unity, offer alternative to PH admin failure.
  - **Post-PRN NS BN-PN cooperation still "ujian formula" (formula test)** — cautious, including grassroots views.
  - "MCA's reaction shows doubt about this cooperation still exists. Or maybe PH Youth themselves no longer confident in Madani govt strength, despite previously boasting 'Kalah atau menang PRN Johor, saya tetap Perdana Menteri.'"
  - **"PMX and PH sedang menghitung hari"** (PMX and PH are counting days) — escalation of unity-govt-end framing.
- **Significance:** PIR-16 resign-narrative EXPANDS to Perak + Pahang (new states); directly links to PIR-16 "Melaka withdrawal" / "Melaka PH-BN fracture" keyword (DAP Melaka as model); "ujian formula" = "makmal politik" adjacent; "PMX menghitung hari" = unity-govt-end escalation. NOT [CRITICAL].

### 3. KJ "sensitiviti orang Melayu" + "isyarat kepada PH" — new FMT outlet (see PIR-06 #4)
- KJ's Subang Umno meeting statement now in FMT (BM+EN). "Sensitiviti orang Melayu" (Malay sensitivities) = sharper formulation than prior Sinar/MalayMail captures. Reinforces "penyatuan undi Melayu" + "Anwar not briefed" + unity-govt critique threads.

### 4. Senarai penuh 103 calon PRN Negeri Sembilan 2026 [NEW reference data]
→ `priority_PIR-06-PIR-07-PIR-16_sinarharian_senarai-penuh-103-calon-prn-negeri-sembilan-2026-sinar-harian_20260720_evening_targeted.md` (Sinar, full candidate list)
- Complete list of 103 candidates across 36 DUN seats. Reference data for cross-checking seat allocations (PH 36 solo / BN 25 / PN 11 / Bersatu 24 solo / Berjasa + independents). PIR-07 reference.

---

## 🔵 PIR-07 — HIGHEST-PRIORITY BATTLEGROUNDS — evening updates

### 1. Onn Hafiz at Tampin (Gemencheh) — Johor machinery launch (see PIR-06 #3)
- Dataran Kampung Tengah, Gemencheh, Tampin (Sunday). Gerak Gempur BN Tampin launch.
- **NEW candidate names:** Suhaimizan Bizar (BN, DUN Gemencheh), Koh Kim Swee (BN, DUN Repah). Tampin UMNO chief Mohd Isam Mohd Isa present.
- Johor youth volunteers physically in Tampin for NS campaign.

### 2. Loke "thanks MCA" at Pasar Besar Seremban (Sunday) — 3 MCA seats not contested named (see PIR-16 #1)
- 3 MCA traditional seats NOT contested: **Lobak** (most Chinese voters in NS), **Lukut** (ex-MCA Dr Yao Chai Thiam, ex-Exco), **Mambau** (ex-MCA Exco Hew Chok Tau before 2008).
- MCA contests 7: Chennah, Bahau, Nilai, Temiang, Rahang, Chuah, Repah.
- Only Chennah = straight fight (BN-PN strategy succeeded); other MCA seats still 3-cornered with Bersatu.

### 3. Police investigation papers at Klawang — FMT BM corroboration (new outlet, pre-cutoff dup)
→ `priority_PIR-06-PIR-07_FMT_prn-n-sembilan-polis-buka-2-kertas-siasatan-babit-kesalahan-pilihan-raya_20260720_evening_rss.md` (FMT BM, dated 03:02 UTC = 11:02 MYT, pre-cutoff)
- FMT BM version of the afternoon Awani capture: 2 investigation papers, Section 427 Penal Code, Kuala Klawang Jelebu (PH flags/banners/bumper stickers damaged), police chief "Alzafny Ahmad" (Sinar/Utusan spelling; Awani spelled "Azfanny"). 109 permits, 107 approved. DUN dissolved 5 Jun, polling 1 Aug, early voting 28 Jul.
- **New outlet corroboration only; no new analytical content.** Note spelling discrepancy (Alzafny vs Azfanny).

### 4. Sidebar-referenced PIR-07 articles NOT yet captured (next-cycle targets)
- "PRN NS: Polis terima satu laporan pertelingkahan mulut antara penyokong parti" (verbal clash between supporters — new incident)
- "PRN NS: DUN Pilah saksi pertembungan dua calon wanita" (DUN Pilah two-women contest)
- "PRN NS: 21 DUN lawan tiga penjuru" (21 DUN three-cornered — seat allocation summary)
- "Jangan campur aduk adat dengan politik - Tok Mat" (Tok Mat on adat — PIR-16 "adat" keyword)
- "'Buktikan penyatuan kita mampu gegar mereka' - Akmal Saleh" (Akmal on unity)
- "Kejayaan PRN Johor jadi pembakar semangat BN cipta kemenangan di Negeri Sembilan - Ahmad Zahid" (Zahid on Johor spirit)
- "Abdul Hadi, Asyraf Wajdi berjabat tangan, curi tumpuan" (Hadi-Asyraf handshake — PIR-06 UMNO-PAS symbolism)
- "MCA bars its youth wing sec-gen to campaign in Negeri Sembilan election" (Focus Malaysia, 18 Jul — MCA internal discipline)

---

## ⚠️ COLLECTION LIMITATIONS (evening cycle)

- **gnews freshness (21st cycle):** 50 queries → 508 items, 357 PRN/priority hits, **0 fresh post-cutoff**. gnews RSS continues to surface historical matches only. Fresh Day-2 content was captured via direct RSS feeds (FMT) + **targeted sidebar-recovery** (Sinar article-ID extraction from Wee Ka Siong article related-hrefs) — NOT via gnews. gnews protobuf URL resolution remains curl-infeasible (21st cycle; all 21 gnews candidate URLs = JS-splash skips).
- **NST + MalayMail + Sinar + Utusan RSS feeds:** All returned 0 items (JS-rendered/403, same as prior 20 cycles). Compensated by FMT RSS (full content:encoded) + homepage slug-hint extraction (MalayMail 40 links → 1 saved; Utusan 69 → 1 saved; Sinar 27 → 1 saved) + **targeted sidebar-recovery** (5 saved — the cycle's largest new-content gain).
- **[CRITICAL] auto-flag:** 0 false positives this cycle. Detector tightened (now requires PN/Bersatu co-occurrence for PIR-06 critical triggers; requires "bersatu" co-occurrence for PIR-16 "sasar bentuk kerajaan negeri"). Working as intended.
- **False positives (16):** Zizie Izette court case ×4 (Awani + FMT BM + FMT EN + MalayMail EN — Bung Moktar's widow acquitted, non-PRN), World Cup ×5 (Awani prize money + FMT Rodri/Cucurella tattoo/Dataran Merdeka litter/Trump-Canada), Rubio geopolitics ×2 (Russia-China-Philippines, Iran-Hormuz), markets ×1 (Asian shares), UAE stranded Malaysians ×1, Nur Jazlan Senate deputy president ×1 (UMNO-adjacent but non-PRN), eFishery/KWAP federal Dewan Negara ×3 (Sinar + Utusan + FMT — Anwar Q&A, non-PRN). Substring false-matches on "negeri"/"sembilan"/"pn"/"wee" in sidebars.
- **No Harian Metro/BH new content:** Both remained inaccessible (HTTP 000/404) — consistent with all prior cycles.
- **PH manifesto launch 20 Jul evening:** At 12:48 MYT collection time, the manifesto launch (scheduled "malam ini"/tonight 20 Jul) had NOT yet occurred. Coverage expected in the next cycle (~18:00-20:00 MYT window).
- **Targeted sidebar-recovery methodology (NEW this cycle):** Extracting related-article hrefs from a high-value captured article's raw HTML + gnews RSS searches for sidebar-referenced headlines, then fetching each Sinar article URL directly. Yielded 5 genuinely-new articles — a high-yield methodology addition when gnews freshness is 0 and homepage extraction underperforms.

---

## 📈 CYCLE DELTA: afternoon → evening (11:40 → 12:48 MYT 20 Jul, ~1h08m)
- **Articles saved:** 25 (20 main script + 5 targeted recovery)
- **Genuinely-new analytically-material:** **8** (Wee MCA rebuttal, KJ FMT BM+EN, Onn Hafiz Johor formula, Mohd Syahir Perak/Pahang, Ka Siong BN-PN vote-split, Loke "thanks MCA" original, 103 calon list)
- **Genuinely-fresh post-cutoff (≥11:40 MYT):** **1** (FMT BM KJ "isyarat kepada PH" at 11:48 MYT). All other genuinely-new articles are pre-cutoff (Sunday 19 Jul / early Monday) but new-to-collection (not surfaced by prior cycles' homepage extraction).
- **PIR-06 status:** [CRITICAL] MAINTAINED (Kiandee quorum, prior 075200). **21st cycle with no [CRITICAL] threshold crossing.** NEW intel: Wee MCA rebuttal, Ka Siong BN-PN-vote-split-avoidance, Onn Hafiz Johor→NS machinery transfer, KJ "sensitiviti orang Melayu."
- **PIR-16 status:** NOT [CRITICAL]. **21st cycle with no "Bersatu exit imminent"/"sasar bentuk kerajaan negeri" hard-news corroboration.** NEW: MCA rebuttal loop CLOSED (Wee responded); resign-narrative expands to Perak/Pahang (Mohd Syahir) + invokes DAP Melaka model; KJ "sensitiviti orang Melayu" sharpens unity-govt critique; "PMX menghitung hari" escalation.
- **PIR-07 status:** New ground intel: Gemencheh (Suhaimizan Bizar) + Repah (Koh Kim Swee) BN candidates named; 3 MCA non-contested seats named (Lobak/Lukut/Mambau); MCA contests 7 seats named. Klawang police investigation (FMT BM new-outlet corroboration).
- **Source status:** FMT RSS (200, 50 items, content:encoded) working. Awani main RSS (200, 10 items) working. NST/MalayMail/Sinar/Utusan RSS = 0 (JS/403). Homepage extraction: MalayMail 40 links → 1 saved, Utusan 69 → 1, Sinar 27 → 1. **Targeted sidebar-recovery = largest new-content gain (5 of 8 genuinely-new articles).** gnews = 0 fresh (21st cycle).
- **Methodology addition:** Targeted sidebar-recovery (extract related-article hrefs from a high-value article's HTML + gnews searches for sidebar headlines + direct Sinar URL fetch). High-yield when gnews freshness = 0 and homepage extraction underperforms. Reusable next cycle.

---

## 🎯 NEXT-CYCLE RECOMMENDATIONS (14:00–18:00 MYT window)
1. **PIR-06 ([CRITICAL] watch):** Maintain formal-removal watch. Re-poll gnews for Bersatu Supreme Council quorum, PDM Klawang reopen (now hour 20+), RoS, Muhyiddin "new coalition," Bersatu candidate withdrawal, "lebih hebat." PDM Klawang reopening may materialize today (20 Jul business hours).
2. **PIR-06 (NEW threads):** (a) Does PH/AMH/Anwar respond to Wee's conciliatory MCA rebuttal? (b) Does Onn Hafiz's Johor-volunteers-to-Tampin draw PH response? (c) Does KJ's "sensitiviti orang Melayu" draw Anwar/PH response? (d) Track Akmal Saleh "buktikan penyatuan" + Zahid "Johor spirit" statements (sidebar-referenced, not yet captured).
3. **PIR-07:** **PH MANIFESTO LAUNCH 20 JUL EVENING** (Amirudin Shari officiating) — capture ALL coverage when published (expected ~18:00-20:00 MYT). **BN MANIFESTO 24 JUL at DUN Linggi + Pertang** — next major PIR-07 event. Capture Day-2 evening ceramah/walkabout/ops-centre for T1 seats: Linggi, Sikamat, Klawang, Pertang, Rantau, Chennah, Johol, Gemencheh, Repah. Recover sidebar-referenced articles: DUN Pilah two-women contest, 21 DUN three-cornered, verbal-clash police report, Tok Mat "adat," Hadi-Asyraf handshake.
4. **PIR-16:** Track MCA response to Wee's rebuttal (does Mah Hang Soon add?). Track Mohd Syahir "Perak/Pahang resign" — does PH Perak/Pahang Exco respond? Track "PMX menghitung hari" framing pickup. Verify DAP Melaka model reference (what did DAP Melaka do? — PIR-16 "Melaka withdrawal" keyword).
5. **Source maintenance:** **Targeted sidebar-recovery = proven high-yield** (5 of 8 genuinely-new this cycle). Repeat: extract related-article hrefs from any new high-value Sinar/FMT article + fetch directly. Re-poll FMT/Awani RSS for post-12:48 MYT items. Continue MalayMail/Sinar homepage extraction.

---

*Evening cycle index appended 2026-07-20 12:48 MYT (04:48 UTC) by PRN Negeri Sembilan 2026 News Collection Agent — Nomination-Day Surge Mode. TLP:AMBER. 25 articles saved (20 main script + 5 targeted sidebar-recovery). 8 genuinely-new analytically-material articles. [CRITICAL] NOT crossed (21st cycle; 0 auto-flag false positives — tightened detector working). Key evening developments: (1) Wee Ka Siong MCA rebuttal to Loke — PIR-16 "MCA rebuttal" carry-forward flag RESOLVED (conciliatory "thanks for reminder" framing); (2) Onn Hafiz confirms Johor→NS machinery transfer (Johor volunteers to Tampin; Gemencheh/Repah candidates named); (3) KJ "sensitiviti orang Melayu" + "isyarat kepada PH" in FMT (BM+EN, FRESH 11:48 MYT); (4) Mohd Syahir (PAS) expands resign-narrative to Perak/Pahang + invokes DAP Melaka model; (5) Ka Siong frames BN-PN as vote-split avoidance + MCA "semak dan imbang." PDM Klawang reopening UNRESOLVED (hour 20+). PH manifesto launch tonight (coverage expected next cycle). Methodology addition: targeted sidebar-recovery (5/8 new articles).*

---
---

# CYCLE: `20260720_midafternoon` — Campaign Day 2 (midafternoon recovery)

**Cycle:** `20260720_midafternoon` — collected ~13:51 MYT 20 Jul (05:51 UTC) | cutoff = 04:48 UTC / **12:48 MYT** (evening cycle end)
**Fetcher:** `_surge_fetch_20260720_midafternoon.py` (adapted from evening script: cutoff 04:48 UTC, +14 sidebar-recovery queries added)
**Purpose:** Recover evening cycle's sidebar-referenced next-cycle targets + capture any fresh content since 12:48 MYT. Freshness probe (FMT RSS + Awani RSS) confirmed 0 fresh PRN items; cycle focused on recovery via homepage slug-hint extraction + targeted sidebar-recovery.

## CYCLE SUMMARY

| Metric | Value |
|---|---|
| Google News queries run | 64+ (incl. 14 sidebar-recovery queries: pertelingkahan, Aminuddin/Sikamat, Bersatu Rahang, PH flags burned, Muhyiddin Umno toppling PN, etc.) |
| gnews items returned | 546 (368 PRN/priority headline hits) |
| gnews **fresh** post-cutoff (≥12:48 MYT) | **0** (22nd cycle — gnews surfaces historical only) |
| RSS feed items scanned | FMT 50 (0 fresh PRN) / Awani 10 (3 fresh non-PRN: weather/debt/body-found) |
| Homepage candidate links found | Sinar 27 (main yield — 4 genuinely-new articles surfaced) |
| **Articles saved (total)** | **16** (12 main script + 4 targeted sidebar-recovery) |
| Genuinely-new FULL-TEXT articles | **4** (all Sinar, published 12:46–13:46 MYT — 3 genuinely fresh post-cutoff) |
| Paywalled title-only recoveries | **4** (Sinar Premium opinion/analysis pieces) |
| Duplicates skipped | 37 |
| Auto-flagged [CRITICAL] | 1 → **FALSE POSITIVE (corrected)** — see §CRITICAL |
| False positives (non-PRN) | 8 (Awani weather/debt/body ×3, MalayMail Melaka drone, eFishery/KWAP ×3, TEKUN borderline) |
| Unrecovered but confirmed-exist (historical gnews) | 4 (Focus Malaysia MCA sec-gen, The Vibes Hadi-Asyraf handshake, FMT Tok Mat adat, FMT DAP Melaka — all JS-rendered/gnews-redirect, curl-infeasible) |

---

## 🔴 PIR-06 — COALITION OPERATIONAL ARRANGEMENT — [CRITICAL] NOT CROSSED (22nd cycle)

**[CRITICAL] status: MAINTAINED. NO NEW THRESHOLD CROSSING this cycle.** One auto-flag (Bersatu Rahang "pecat") = FALSE POSITIVE (corrected). No formal PN-MT expulsion, no Bersatu candidate withdrawal, no Kiandee quorum escalation, no "lebih hebat new coalition," no PDM Klawang reopening detected.

### 1. Bersatu Rahang candidate "dipinjamkan" + Gerakan sacking [12:46 MYT 20 Jul, NEW — auto-flag [CRITICAL] = FALSE POSITIVE]
→ `priority_PIR-06-PIR-07-PIR-16_sinarharian_saya-tak-pernah-keluar-bersatu-hanya-dipinjamkan-calon-bersatu-rahang-sinar-hari_20260720_midafternoon_home.md`
- **Tang Jay Son** (Bersatu DUN Rahang candidate) clarifies he joined **Gerakan** in 2023 because he was "dipinjamkan" (lent) to represent Gerakan in DUN Chuah (Gerakan had no candidate). He **never left Bersatu** since joining in 2021; his Bersatu membership was never cancelled.
- **Gerakan SACKED (memecat) Jay Son** effective immediately for contesting under Bersatu ticket in PRN NS — Gerakan Sec-Gen **Wong Chia Zhen** calls it serious disciplinary violation / breach of loyalty.
- Jay Son: has no objection to Gerakan sacking but feels timing (announced on nomination day) was "kurang matang" (immature); learned from media, never received notice.
- **[CRITICAL] FALSE POSITIVE correction:** The "pecat" (sacking) trigger fired because "memecat/dipecat/pemecatan" + "Bersatu/Perikatan" co-occurred. BUT this is **Gerakan's internal disciplinary action against a member who contested under Bersatu's logo** — NOT a PN-MT expulsion of Bersatu, and the candidate is **STAYING** (not withdrawing). This is intra-PN component-party friction (Gerakan vs Bersatu over candidate "lending"), NOT the PIR-06 [CRITICAL] threshold. Corrected in-file.
- **Significance:** Reveals **intra-PN component friction** (Gerakan vs Bersatu candidate-lending dispute) at a Tier-4 seat (Rahang). Not [CRITICAL] but a cooperation-arrangement friction signal.

### 2. Marzuki fires back at Hamzah: "UMNO toppled PN govt, Hamzah tried to topple Muhyiddin" [13:08 MYT 20 Jul, FRESH]
→ `priority_PIR-06-PIR-07_sinarharian_muhyiddin-tidak-lupa-jasa-tetapi-sejarah-buktikan-umno-tumbangkan-kerajaan-pn-ma_20260720_midafternoon_home.md`
- **Datuk Dr Marzuki Mohamad** (ex-Confidential Secretary to Muhyiddin) Facebook post (Monday): Muhyiddin never forgot UMNO/PAS jasa, BUT history records **UMNO toppled the PN government in 2021** — 15 UMNO MPs withdrew support (per Annuar Musa), UMNO president wrote to Agong backing Anwar as PM.
- Despite UMNO toppling him, Muhyiddin proposed a UMNO leader as PM to sustain PN govt (later "Keluarga Malaysia").
- **Direct counter to Hamzah** (Wawasan president): Hamzah told Muhyiddin not to call PAS "toksik." Marzuki fires back: Muhyiddin's "madu dibalas tuba" (kindness repaid with poison); **after Muhyiddin resigned, a movement to topple him as PN chairman AND Bersatu president began — LED BY HAMZAH with PAS leaders' support/encouragement.**
- "Dari saat itulah bermulanya PN menjadi toksik" (PN became toxic from that moment). "Yang menaikkan jugalah yang menjatuhkan" (the same who raised him also brought him down). "Plot still happening now with the same characters."
- **Significance:** PIR-06/16 friction escalation. Reveals **historical root of Bersatu-PN internal conflict**: Hamzah allegedly led the effort to topple Muhyiddin as PN chairman/Bersatu president. This is the Marzuki/Muhyiddin-camp RESPONSE to Hamzah's midday "don't call PAS toxic" statement. Not [CRITICAL] (narrative/friction exchange, no formal threshold).

### 3. Sinar Premium opinion/analysis (paywalled, title-only) [NEW this cycle]
→ `priority_PIR-06-PIR-16_sinarharian_bersatu-kian-tidak-relevan-hadapi-krisis-identiti-sinar-harian_20260720_midafternoon_targeted.md` (788600, paywalled)
→ `priority_PIR-06-PIR-16_sinarharian_gabungan-lawan-gabungan_20260720_midafternoon_targeted.md` (788546, paywalled)
→ `priority_PIR-06-PIR-16_sinarharian_percaturan-yang-bakal-mengundang-padah-kepada-pkr_20260720_midafternoon_targeted.md` (788459, paywalled)
- **"Bersatu kian tidak relevan, hadapi krisis identiti"** — Sinar opinion piece: Bersatu "increasingly irrelevant, facing identity crisis." Strong PIR-16 "Bersatu in disarray" narrative signal. Paywalled (title + paywall notice only; no body text). NOT [CRITICAL] — opinion column, not hard-news corroboration of "Bersatu exit imminent."
- **"Gabungan lawan gabungan"** — coalition-vs-coalition framing analysis (PIR-06). Paywalled.
- **"Percaturan yang bakal mengundang padah kepada PKR?"** — analysis of PKR strategy risks (PIR-06/16). Paywalled.

---

## 🟢 PIR-07 — HIGHEST-PRIORITY BATTLEGROUNDS — midafternoon updates

### 1. PH flags burned/damaged at DUN Palong + N31 Chembong [13:18 MYT 20 Jul, FRESH — NEW incidents]
→ `priority_PIR-06-PIR-07_sinarharian_prn-negeri-sembilan-ph-kesal-bendera-parti-dibakar-dirosakkan-sinar-harian_20260720_midafternoon_home.md`
- PH main ops centre received reports of campaign-material damage since Sunday night.
- **DUN Palong** — PH flags **burned** Sunday night. (Palong = Felda seat; afternoon cycle had Felda Palong ground survey.)
- **N31 DUN Chembong** — flag posts **damaged ("khianat")** Monday morning. **Chembong (N.27/N31) = T1 priority seat AND Tier-4 seat.**
- PH will take legal action under **Section 4A Election Offences Act 1954** + **Section 427 Penal Code** (mischief). DUN election directors advised to file police reports. PH won't point fingers; urges healthy campaign, no retaliation.
- **Significance:** NEW election incidents at 2 seats (escalation from afternoon Klawang N.28 single incident → now 3 seats: Klawang + Palong + Chembong). **Chembong Tier-4 seat incident** is PIR-07-relevant. Distinct from the Klawang police investigation papers (afternoon cycle).

### 2. Sikamat (N.13, Tier-4): Nor Azman replaces Aminuddin; 3-corner confirmed [13:46 MYT 20 Jul, FRESH]
→ `priority_PIR-06-PIR-07_sinarharian_aminuddin-disenangi-ramai-masih-harap-beliau-kekal-di-sikamat-sinar-harian_20260720_midafternoon_home.md`
- Day 2 campaign: PH Sikamat candidate **Nor Azman Mohamad** (PKR Information Chief) acknowledges many voters still hope **Aminuddin Harun** ("Tok Min") stays as their rep. Voters understand Aminuddin's move to Linggi; appreciate his service since ADUN 2008.
- Nor Azman: often substituted for Aminuddin in Sikamat affairs → candidacy not a shock. Promises to continue "Tok Min's" work (student aid, entrepreneur fund, Rumah Harapan Rakyat, affordable housing).
- **Sikamat = 3-cornered CONFIRMED:** Nor Azman (PH/PKR) vs **Datuk Tun Faisal Ismail Aziz** (Bersatu Information Chief) vs **Datuk Razali Abu Samah** (PN-Wawasan, ex-Deputy Melaka police chief).
- **Significance:** Confirms morning-cycle Wawasan-police-vote intel (Razali Abu Samah = Wawasan's Sikamat candidate, ex-cop vote-pull). Article labels Razali "PN-Wawasan" → confirms **Wawasan candidates run under PN banner** for this seat (key coalition-arrangement detail). Sikamat = Tier-4 seat (N.13) PIR-06/07 overlap.

### 3. Evening cycle next-cycle targets — recovery status
- "Pertelingkahan mulut antara penyokong parti" (verbal clash) — gnews query run, NOT surfaced (not yet published or gnews-delayed).
- "DUN Pilah dua calon wanita" / "21 DUN tiga penjuru" — gnews queries run, NOT surfaced.
- "Tok Mat adat" / "Hadi-Asyraf handshake" / "MCA sec-gen" / "DAP Melaka BN-PN" — surfaced as **historical gnews headlines** (Focus Malaysia / The Vibes / FMT) but **unrecoverable via curl** (gnews protobuf URL resolution curl-infeasible 22nd cycle; FMT/The Vibes/Focus Malaysia site search JS-rendered). Confirmed-exist; carry forward as next-cycle targets with gnews headline intel preserved in `_gnews_headlines_20260720_midafternoon.json`.

---

## 🟡 PIR-16 — FIRST DOMINANT CAMPAIGN NARRATIVES — midafternoon updates

### 1. "Bersatu kian tidak relevan, hadapi krisis identiti" — narrative pickup [PAYWALLED]
- Sinar opinion piece (788600, khas/pendapat) — "Bersatu increasingly irrelevant, facing identity crisis." This is a **PIR-16 "Bersatu in disarray" narrative signal** gaining traction (Sinar publishing dedicated analysis). Paywalled (title-only). NOT [CRITICAL] — opinion column, not hard-news corroboration of "Bersatu exit imminent."

### 2. Kamil Munim jet-misuse denial [PAYWALLED, connects to morning "topple-Anwar" thread]
→ `priority_PIR-06_sinarharian_tular-dakwaan-guna-jet-rasmi-amk-kelantan-nafi-tengku-zafrul-kamil-salah-guna-as_20260720_midafternoon_targeted.md` (788493)
- AMK (PKR Youth) Kelantan denies viral claim that **Tengku Zafrul and Kamil [Munim]** misused government jet/asset. Paywalled (title-only).
- **Connects to morning PIR-06 thread:** Kamil Munim (PKR Youth chief, Anwar's political sec) was the figure who framed BN-PN cooperation as a "topple-Anwar" plot (morning FMT). Now a jet-misuse denial surfaces — suggests **counter-attack on Kamil** (rival faction surfacing asset-misuse claims). PKR internal friction continues.

### 3. Marzuki/Muhyiddin-camp vs Hamzah — "toxic PN" narrative exchange (see PIR-06 #2)
- Marzuki's "PN menjadi toksik" + "Hamzah led movement to topple Muhyiddin" = direct PIR-16 "toxic PN" / "Bersatu in disarray" escalation via proxy statements. Hamzah (midday) said "don't call PAS toxic"; Marzuki (this cycle) says "PN became toxic when Hamzah moved against Muhyiddin." **Narrative volley active.**

---

## ⚠️ COLLECTION LIMITATIONS (midafternoon cycle)

- **gnews freshness (22nd cycle):** 64+ queries → 546 items, 368 PRN/priority hits, **0 fresh post-cutoff**. gnews RSS surfaces historical matches only. Fresh Day-2 content captured via **Sinar homepage slug-hint extraction** (4 genuinely-new articles surfaced from Sinar homepage updated 12:46–13:46 MYT) — NOT via gnews. gnews protobuf URL resolution remains curl-infeasible (22nd cycle; tried gnews decode + Bing + FMT/TheVibes site search — all 0 direct links).
- **RSS feeds:** FMT 50 items (0 fresh PRN). Awani 10 items (3 fresh non-PRN: weather/debt/body-found). NST/MalayMail/Sinar/Utusan RSS = 0 (JS/403, consistent).
- **Sinar Premium paywall:** 4 targeted-recovery articles (788600, 788546, 788459, 788493) all behind Sinar Premium paywall — title + paywall notice captured, no body text. Consistent with midday 788548 paywall finding. These are opinion/analysis pieces (khas/pendapat section) — title-only intel still has narrative-signal value.
- **[CRITICAL] auto-flag:** 1 false positive this cycle (Bersatu Rahang "pecat" = Gerakan sacking member, NOT PN expelling Bersatu; candidate staying). Corrected in-file. Detector fires on "pecat" + PN/Bersatu co-occurrence — semantically this is intra-component discipline, not coalition-expulsion. Working but needs semantic refinement (Gerakan-sacking-member ≠ PN-expelling-Bersatu).
- **False positives (8):** Awani weather/debt/body-found ×3 (non-PRN, "negeri"/"anwar" substring match), MalayMail Melaka drone-smuggling ×1 (Melaka, non-PRN, "melaka" PIR-16 false match), eFishery/KWAP ×3 (Sinar + Utusan + Sinar video — federal Dewan Negara, non-PRN), MalayMail TEKUN RM36m NS ×1 (borderline — NS-specific but federal agency disbursement, not core PIR).
- **Unrecovered historical gnews (4):** Focus Malaysia MCA sec-gen, The Vibes Hadi-Asyraf handshake, FMT Tok Mat adat, FMT DAP Melaka — all confirmed-exist via gnews headlines but unrecoverable (JS-rendered search / gnews-redirect). Carry forward.

---

## 📈 CYCLE DELTA: evening → midafternoon (12:48 → 13:51 MYT 20 Jul, ~1h03m)
- **Articles saved:** 16 (12 main script + 4 targeted sidebar-recovery)
- **Genuinely-new FULL-TEXT:** **4** (all Sinar: Bersatu Rahang 12:46, Muhyiddin/Marzuki 13:08, PH flags 13:18, Aminuddin/Sikamat 13:46 MYT)
- **Genuinely-fresh post-cutoff (≥12:48 MYT):** **3** (Muhyiddin/Marzuki 13:08, PH flags 13:18, Aminuddin/Sikamat 13:46 MYT). Bersatu Rahang 12:46 = borderline pre-cutoff (2 min before) but new-to-collection.
- **Paywalled title-only recoveries:** **4** (Bersatu identity-crisis, Gabungan lawan gabungan, PKR padah, Kamil jet — all Sinar Premium)
- **PIR-06 status:** [CRITICAL] MAINTAINED (22nd cycle). 1 auto-flag FALSE POSITIVE corrected. NEW intel: intra-PN component friction (Gerakan sacks Bersatu-lent candidate at Rahang Tier-4 seat); Marzuki/Muhyiddin-camp counter-attack on Hamzah (reveals Hamzah led anti-Muhyiddin movement — historical root of Bersatu-PN conflict).
- **PIR-16 status:** NOT [CRITICAL]. "Bersatu kian tidak relevan" opinion piece = narrative signal (paywalled). "Toxic PN" volley active (Hamzah midday ↔ Marzuki this cycle). Kamil jet-misuse denial = PKR internal friction counter-attack.
- **PIR-07 status:** NEW incidents at 2 seats (Palong flags burned + N31 Chembong Tier-4 flag damage — escalation from 1→3 incident seats). Sikamat (N.13 Tier-4) 3-corner confirmed; "PN-Wawasan" label confirms Wawasan runs under PN banner.
- **Source status:** Sinar homepage extraction = main yield (4 genuinely-new). FMT/Awani RSS = 0 fresh PRN. gnews = 0 fresh (22nd cycle). Targeted sidebar-recovery yielded 4 paywalled titles. gnews URL resolution + Bing + site-search all failed (22nd cycle).

---

## 🎯 NEXT-CYCLE RECOMMENDATIONS (14:00–18:00 MYT window → PH manifesto launch tonight)
1. **PIR-06 ([CRITICAL] watch):** Maintain formal-removal watch. PDM Klawang reopening UNRESOLVED (now hour 21+). Re-poll gnews for Bersatu Supreme Council quorum, RoS, "lebih hebat new coalition," Bersatu candidate withdrawal. Monitor whether Gerakan-Bersatu candidate-lending dispute (Rahang) escalates to formal PN component-friction statement.
2. **PIR-06 (NEW threads):** (a) Does Hamzah/Wawasan respond to Marzuki's "Hamzah led movement to topple Muhyiddin" accusation? (b) Does Gerakan Sec-Gen issue follow-up on Rahang sacking? (c) Track whether Tang Jay Son's clarification draws PN Supreme Council response.
3. **PIR-07:** **PH MANIFESTO LAUNCH 20 JUL EVENING** (Amirudin Shari officiating) — capture ALL coverage when published (expected ~18:00-20:00 MYT). **BN MANIFESTO 24 JUL at DUN Linggi + Pertang.** Monitor Chembong (N31 Tier-4) + Palong incident follow-up (police reports filed?). Recover: DUN Pilah two-women, 21 DUN three-cornered, verbal-clash police report, Tok Mat adat, Hadi-Asyraf handshake (all still unrecovered).
4. **PIR-16:** Track "Bersatu kian tidak relevan / krisis identiti" narrative pickup (does hard-news outlet corroborate?). Track Kamil jet-misuse denial fallout (PKR factional friction). Track "toxic PN" volley (Hamzah ↔ Marzuki/Muhyiddin-camp). Recover DAP Melaka BN-PN pact article (FMT, PIR-16 "Melaka withdrawal" keyword).
5. **Source maintenance:** Sinar homepage extraction = proven yield (4 genuinely-new this cycle). Repeat. Targeted sidebar-recovery = 4 paywalled titles (title-only value). Re-poll FMT/Awani RSS for post-13:51 MYT items. Sinar Premium paywall blocks 4 opinion pieces — if credentials available, these are high-value PIR-16 targets (Bersatu identity crisis, coalition-vs-coalition, PKR strategy).

---

*Midafternoon cycle index appended 2026-07-20 ~13:55 MYT (05:55 UTC) by PRN Negeri Sembilan 2026 News Collection Agent — Nomination-Day Surge Mode. TLP:AMBER. 16 articles saved (12 main script + 4 targeted sidebar-recovery). 4 genuinely-new full-text + 4 paywalled title-only. [CRITICAL] NOT crossed (22nd cycle; 1 auto-flag FALSE POSITIVE corrected — Bersatu Rahang "pecat" = Gerakan sacking member, not PN expelling Bersatu). Key midafternoon developments: (1) Intra-PN component friction — Gerakan sacks Bersatu-lent candidate Tang Jay Son at Rahang (Tier-4); candidate STAYING; (2) Marzuki/Muhyiddin-camp counter-attacks Hamzah — "Hamzah led movement to topple Muhyiddin as PN chairman/Bersatu president"; "PN became toxic from that moment"; (3) NEW election incidents at Palong (flags burned) + N31 Chembong (Tier-4, flag damage) — escalation from 1→3 incident seats; (4) Sikamat N.13 Tier-4 3-corner confirmed; "PN-Wawasan" label confirms Wawasan runs under PN banner; (5) "Bersatu kian tidak relevan, hadapi krisis identiti" Sinar opinion piece (paywalled) — PIR-16 "Bersatu in disarray" narrative signal. PH manifesto launch tonight 18:00-20:00 MYT — next major collection window.*
