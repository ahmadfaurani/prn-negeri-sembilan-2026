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

---
---

# CYCLE: `20260720_lateafternoon` — Campaign Day 2-3 (late afternoon surge)

**Cycle:** `20260720_lateafternoon` — collected ~15:21 MYT 20 Jul (07:21 UTC) | cutoff = 05:55 UTC / **13:55 MYT** (midafternoon cycle end)
**Fetcher:** `_surge_fetch_20260720_lateafternoon.py` (67 gnews queries + 10 RSS feeds incl. **Harian Metro RSS — NEW working source** + homepage extraction + Sinar article-ID scan 788590-788660 + Harian Metro alt-path recovery)
**Purpose:** Capture fresh Day-2 content since 13:55 MYT + recover midafternoon sidebar-referenced targets (DUN Pilah two-women, 21 DUN three-cornered, etc.) + monitor PH manifesto launch timing + PDM Klawang reopen status + [CRITICAL] watch continuation.
**Polling day:** 2026-08-01 (Sat) | **Early voting:** 2026-07-28 | **Nomination day:** 2026-07-18

## CYCLE SUMMARY

| Metric | Value |
|---|---|
| Google News queries run | 67 (incl. 12 mandatory PIR-06 [CRITICAL]-watch: kuorum, lebih hebat, pecat, tarik diri, PDM Klawang reopen, RoS, sole opposition, new coalition) |
| gnews items returned | 676 (420 PRN/priority headline hits) |
| gnews **fresh** post-cutoff (≥13:55 MYT) | **1** (Pertang Mandarin PKR — gnews fresh hit) |
| RSS feed items scanned | **787** total (Awani 10 + **HarianMetro 51 — NEW** + FMT 50; NST/MalayMail/Sinar/Utusan/BH feeds = 0) |
| **Articles saved (total)** | **91** (after 13 favicon false positives deleted; pre-delete 104) |
| RSS full-text saved | 53 (FMT 18 + HarianMetro 31 + Awani 1 + Sinar home 3) |
| URL-extracted (gnews fresh) | 1 (Awani Chuah) |
| Homepage-extracted | 7 |
| Sinar targeted article-ID scan | 30 (788590-788660) |
| HarianMetro alt-path recovery | 13 (but 13 were favicon PNG false positives → deleted) |
| Genuine PIR-06 [CRITICAL] threshold crossings | **0** (23rd cycle — confirmed) |
| Auto-flagged [CRITICAL] | 1 → **FALSE POSITIVE (corrected)** — see §CRITICAL |
| Genuinely-new analytically-material articles | **~14** (Pertang, Chuah, Pilah, Gemas, Gemencheh, Bahau, Sikamat, flags-sabotage, death, permits, 6-PKR-loss, Fathi Aris, Terengganu BN-PN, BM Pertang) |
| Duplicates skipped | 21 |
| False positives (non-PRN) | ~40 (World Cup, crime, weather, international, federal parliament, favicon PNGs) |

---

## 🔴 PIR-06 — COALITION OPERATIONAL ARRANGEMENT — [CRITICAL] NOT CROSSED (23rd cycle)

**[CRITICAL] status: MAINTAINED. NO NEW THRESHOLD CROSSING this cycle.** One auto-flag (Nur Jazlan Senate article, sidebar "dipecat Bersatu") = FALSE POSITIVE (corrected — see §CRITICAL). No formal PN-MT expulsion, no Bersatu candidate withdrawal, no Kiandee quorum escalation, no "lebih hebat new coalition," no RoS intervention. All 12 mandatory gnews [CRITICAL]-watch queries returned 0 fresh critical hits.

**[CRITICAL] FALSE POSITIVE CORRECTION:**
- `priority_PIR-06-PIR-07_sinarharian_nur-jazlan-dilantik-semula-timbalan-speaker-dewan-negara...` — auto-flag fired on sidebar text "Timbalan Speaker DUN Kelantan kekal walaupun dipecat Bersatu" (Kelantan DUN Deputy Speaker remains despite being sacked FROM Bersatu). This is an INDIVIDUAL expelled BY Bersatu (not Bersatu expelled from PN), and it's a sidebar/related-article link, not the article's main content. Opposite direction of PIR-06 [CRITICAL] threshold. Article itself = Nur Jazlan Senate reappointment (routine parliamentary, non-PRN). Corrected in-file.

### 1. No BN-PN cooperation in Terengganu — confirms NS-specific arrangement [NEW]
→ `priority_PIR-06-PIR-07_sinarharian_tiada-perbincangan-kerjasama-bn-pn-di-terengganu-sinar-harian_20260720_lateafternoon_targeted.md` (Sinar 788618)
- **UMNO Terengganu chairman Datuk Rozi Mamat:** "setakat ini tidak ada perbincangan lagi dengan mana-mana pihak" — no formal BN-PN cooperation talks in Terengganu for PRU16.
- "Pola politik sekarang kita tidak boleh jangka. Kadang-kadang di Terengganu lain, di Sarawak lain, di Sabah lain, di Negeri Sembilan lain dan di Johor pula lain." — political patterns differ by state.
- Open to cooperation if it benefits rakyat, citing Sarawak model (state-level ≠ federal-level).
- Also addressed KWAP/eFishery RM200m scandal — won't comment without official reports.
- **Significance:** PIR-06 — confirms BN-PN cooperation is **NS-specific** (and Johor), NOT a national formula. Contrasts with "blue wave to Selangor/Putrajaya" framing (KJ/Noh Omar from morning/midday cycles). Each state has its own "acuan politik."

### 2. Fathi Aris: "PH has no right to feel cheated by UMNO/BN" [NEW — PIR-16 narrative]
→ `priority_PIR-06-PIR-07_sinarharian_ph-tak-punya-hak-untuk-berasa-tertipu-dengan-umno-bn-fathi-aris-sinar-harian_20260720_lateafternoon_targeted.md` (Sinar 788616)
- **Political observer Fathi Aris Omar** (former editor): PH misread the Unity Government basis — UMNO only supported PH after PRU15 because no coalition had majority. PH should be grateful, not complaining.
- "UMNO kini lebih selesa dengan Pas dan PN tidak boleh disalahkan pada Ahmad Zahid atau Mohamad Hasan (Tok Mat)" — UMNO more comfortable with PAS/PN; can't blame Zahid/Tok Mat.
- **Rebuts AMH (Angkatan Muda Harapan)** call for all BN ministers to resign from Cabinet — calls it "terlajak" (over the top). Notes parties in government also contested each other in Sabah PRN.
- "PRN Johor dan NS adalah bagi penggal DUN ke-16" — new PRU16 term, so BN free to find new partners (PAS, Wawasan).
- "Expelling UMNO from Cabinet won't give PMX/Madani stability" — warns against destabilizing the federal government.
- **Significance:** PIR-06/16 — major narrative analysis reinforcing "BN free to partner PN" normalization. Direct rebuttal to AMH "resign to attack" call (morning cycle Kamil Munim thread). Fathi cites Melaka PRN late 2021 (BN vs PN vs PH three-way) as precedent. Sidebar references: "Bersatu kian tidak relevan, hadapi krisis identiti" — narrative continues surfacing.

### 3. Bersatu running SEPARATELY from PN/Wawasan — additional confirmation [CARRY-FORWARD + NEW data point]
- **Pertang (T1):** 3-cornered = Umry (PH) vs Jalaluddin (BN) vs **Faizal Fadli Idrus (calon Bersatu)** — article labels Faizal as "calon Bersatu" (not "calon PN"), confirming Bersatu runs under its own logo.
- **Sikamat (N.13 Tier-4):** 3-cornered = Razali (PN/Wawasan) vs Tun Faisal (Bersatu) vs Nor Azman (PH) — PN/Wawasan and Bersatu competing AGAINST each other.
- **Bahau:** BN/MCA candidate Ah Chong notes "kerjasama berpasukan membabitkan parti komponen BN dan... membantu persefahaman dengan Perikatan Nasional (PN)" — BN-PN ground cooperation confirmed.
- **Significance:** Bersatu candidates appear as separate Bersatu-logo entries, not under PN/Wawasan. In Sikamat, Bersatu and PN/Wawasan field SEPARATE candidates against each other — confirming the PN coalition fracture in NS (Wawasan ≠ Bersatu). Connects to midafternoon "Bersatu sasar bentuk kerajaan negeri" narrative. NOT [CRITICAL] — no formal expulsion/withdrawal, but structural evidence of Bersatu operating independently.

---

## 🟢 PIR-07 — HIGHEST-PRIORITY BATTLEGROUNDS — late afternoon surge (HIGH YIELD)

### 1. Pertang (T1) — 3-cornered with candidate names + demographics [FRESH 14:13 MYT, NEW]
→ `priority_PIR-06-PIR-07_FMT_pkr-man-hopes-mandarin-fluency-will-help-wrest-pertang-from-bn_20260720_lateafternoon_rss.md` (EN) + `..._fasih-mandarin-senjata-calon-ph-lawan-ketua-umno-di-pertang..._rss.md` (BM)
- **3-cornered:** Umry Abdul Khois (PH/PKR, SJKC Pertang alumnus, Mandarin fluent) vs **Jalaluddin Alias** (BN, state BN chief, MP Jelebu, former deputy minister, seeking 3rd term) vs **Faizal Fadli Idrus** (Bersatu).
- **Demographics:** Malay 65.5%, Chinese ~20-30% (EN says 20.1%; BM says "hampir 30%").
- Pertang held by UMNO since 1964. Jalaluddin won 2023 with **2,790 majority** (straight fight vs PN when PH-BN were allies).
- Umry's strategy: Mandarin fluency to court Chinese voters + PH admin record (Aminuddin since 2018) + PM Anwar's aura. Focus on education and youth development.
- "BN-PN cooperation doesn't affect my focus" — PH going solo in all 36 seats.
- **Significance:** T1 seat candidate names confirmed. Bersatu candidate = Faizal Fadli Idrus (NEW name). Jalaluddin "derhaka" angle (Tok Mat's ally contesting under BN-PN pact against former PH ally) — not mentioned in article itself but contextually relevant.

### 2. Chuah — Candidacy controversy RESOLVED, 2-cornered confirmed [FRESH 14:20 MYT, NEW]
→ `priority_PIR-06-PIR-07_Awani_prn-negeri-sembilan-polemik-pencalonan-dun-chuah-sudah-selesai-aminuddin_20260720_lateafternoon.md`
→ `priority_PIR-06-PIR-07_sinarharian_ph-nafi-dakwaan-tak-puas-hati-pemilihan-calon-dun-chuah-sinar-harian_20260720_lateafternoon_home.md` (Sinar 788617, PH denial)
- **Aminuddin Harun** (PH NS chairman): DUN Chuah candidacy controversy resolved. Press conference at Port Dickson with Boon Lai, Kenny, and Sri Tanjung incumbent Dr Rajasekaran Gunnasekaran.
- Issue: incumbent **Datuk Yew Boon Lai** (PH) vs **Datuk Kenny Chiew Chi Kin** (PD PKR deputy chief) over PH candidate selection. Kenny now gives full support to PH candidates in Chuah, Lukut, Sri Tanjung, Bagan Pinang, Linggi.
- **2026 PRN16 Chuah = 2-cornered:** Boon Lai (PH incumbent) vs **Pau Jeou Ching** (BN). [NEW BN candidate name]
- 2023 PRN: Boon Lai won Chuah 2-cornered (8,172 votes vs PN's Tang Jay Son, majority 6,298). Tang Jay Son now contesting Rahang under Bersatu (see midafternoon cycle).
- **Significance:** Resolves the Chuah internal friction (Boon Lai vs Kenny). Five PD-area DUN seats (Chuah, Lukut, Sri Tanjung, Bagan Pinang, Linggi) confirmed as PH sweep target.

### 3. DUN Pilah — Two-women contest RECOVERED [NEW — sidebar target from evening cycle]
→ `priority_PIR-06-PIR-07-PIR-16_sinarharian_calon-dun-pilah-fokus-kebajikan-warga-emas-peluang-kerja-untuk-anak-muda-sinar-h_20260720_lateafternoon_home.md` (Sinar 788617)
- **2-women contest:** **Datuk Noorzunita Begum Mohd Ibrahim** (PH incumbent, also lost Ketua Wanita Cabang 2025) vs **S Leza Md Yasin** (BN). [NEW BN candidate name]
- Noorzunita's 5-year plan: attract investment to Kuala Pilah for youth jobs (prevent outmigration), elderly welfare (those without pension).
- Kuala Pilah development under Aminuddin since 2018: Dataran Melang, Pilah Gateway, LED screen, HTAN hospital.
- **Significance:** RECOVERS the "DUN Pilah dua calon wanita" target from evening cycle's next-cycle recommendations. Also confirmed in the "6 PKR candidates lost" analyst article (Noorzunita lost Ketua Wanita Cabang with 37.05% — internal election loser fielded as candidate).

### 4. DUN Gemas (N34) — PKR woman candidate profiled [NEW]
→ `priority_PIR-06-PIR-07_sinarharian_calon-wanita-pkr-mahu-bawa-perubahan-di-gemas-sinar-harian_20260720_lateafternoon_home.md` (Sinar 788627)
- **PKR candidate Siti Aishah Seman @ Othman**, DUN Gemas (N34) — one of only **TWO women PKR fielded in NS** (the other: Noorzunita in Pilah).
- BA Syariah from UM, active in politics since 2000, joined PKR 2018. Former DUN Gemas coordinating officer (2021-2023). Timbalan Ketua Wanita PKR NS (2022-2025).
- 4 children (22-28), lived in Gemas 29 years. First-time election candidate.
- Key issue: **Felda settlers in Gugusan Jelai** (replanting oil palm, no income yet — need cost-of-living assistance).
- Campaign: house-to-house approach.
- Also lost Ketua Cabang Tampin (41.52%) in 2025 party elections — one of the 6 PKR candidates who lost internal elections.
- **Significance:** N34 Gemas candidate profile. Felda Gugusan Jelai as key demographic. Confirms 5-cornered seat (N34). Two PKR women confirmed (Siti Aishah Gemas + Noorzunita Pilah).

### 5. DUN Gemencheh — PH's oldest candidate (70, AMANAH) [FRESH 13:24 MYT, NEW]
→ `priority_PIR-07_HarianMetro_prn-n9-usia-hanya-angka-calon-ph-dun-gemencheh_20260720_lateafternoon_rss.md` (Harian Metro — NEW working source)
- **PH candidate Datuk Abd Latif A Thambi**, 70, DUN Gemencheh — **oldest candidate in PRN NS**. AMANAH NS vice chairman.
- **1-on-1 vs BN's Suhaimizan Bizar** (straight fight). [NEW BN candidate name]
- Platform: Gemencheh as sports hub (cricket, hockey, volleyball, golf), recreation center, internet, jobs.
- Met at PDM Bukit Rokan.
- **Significance:** DUN Gemencheh = AMANAH (PH) vs BN straight fight. Confirms polling day 1 August 2026. AMANAH vice chairman as candidate.

### 6. DUN Bahau — MCA challenges DAP 20-year stronghold [FRESH 12:52 MYT, NEW]
→ `priority_PIR-06-PIR-07_HarianMetro_prn-n9-bn-kena-kerja-keras-dap-sudah-lebih-20-tahun-di-sini-ah-chong_20260720_lateafternoon_rss.md`
- **BN/MCA candidate Chong Fui Ming** ("Ah Chong"), MCA Jempol deputy chairman, DUN Bahau.
- DAP has held Bahau since 2004 (20+ years) — difficult to break dominance.
- 4 pledges: agriculture, tourism, welfare, health.
- **BN-PN ground cooperation confirmed:** "kerjasama berpasukan membabitkan parti komponen BN dan... membantu persefahaman dengan Perikatan Nasional (PN) diharap dapat membantu kemenangan MCA di Bahau."
- Urban + traditional kampung voters "want change." Polling day: 1 August.
- **Significance:** DUN Bahau = MCA (BN) vs DAP (PH) straight fight. BN-PN cooperation on the ground confirmed for MCA seats.

### 7. Sikamat (N.13 Tier-4) — PN/Wawasan candidate profiled [FRESH 13:02 MYT, NEW]
→ `priority_PIR-06-PIR-07_HarianMetro_prn-n9-polis-atau-wakil-rakyat-sama-sama-jaga-masyarakat_20260720_lateafternoon_rss.md`
- **PN/Wawasan candidate Datuk Razali Abu Samah**, 63, DUN Sikamat — retired PDRM (16 Jun 2023), former acting Melaka Police Chief. From Jelebu.
- 3-cornered: Razali (PN/Wawasan) vs **Datuk Tun Faisal Ismail Aziz** (Bersatu info chief) vs **Nor Azman Mohamad** (PH). [MB Aminuddin moved to Linggi]
- Razali: PDRM service spirit drives political service. Sikamat = "kerusi panas" (hot seat) against "figura besar."
- Won't make empty promises; will identify problems and find solutions.
- **Significance:** Full candidate profiles for all 3 corners at Sikamat Tier-4 seat. Razali's police background connects to morning-cycle Wawasan-police-vote strategy. Confirms Bersatu running separately from PN/Wawasan in this seat.

### 8. Campaign material sabotage — Palong + Chembong + PDM Klawang RESOLVED [FRESH 14:28 MYT, NEW]
→ `priority_PIR-06-PIR-07_HarianMetro_prn-n9-bahan-kempen-dirosakkan-dipercayai-angkara-khianat_20260720_lateafternoon_rss.md`
→ `priority_PIR-06-PIR-07_utusan_prn-negeri-sembilan-polis-lulus-107-permit-ceramah-kempen_20260720_lateafternoon_home.md` (Utusan, police permits + investigation papers)
- **PH Bilik Gerakan Utama** reports:
  - **DUN Palong** — flags **burned** (night 19 Jul)
  - **DUN Chembong** (N.27/N31 Tier-4) — flag posts **damaged (khianat)** (morning 20 Jul)
- PH threatens legal action: **Section 4A Election Offences Act 1954** + **Section 427 Penal Code**
- **NS Police Chief Datuk Alzafny Ahmad:** 2 investigation papers opened under Section 427 Penal Code, both reports from **Kuala Klawang, Jelebu**:
  - 19 Jul: man found PH flags + banners thrown into drain at Kuala Klawang
  - Another man found scratch marks on car bumper after flag installation
  - Total: **3 police reports, 2 investigation papers** for 18-19 Jul
- **PDM Klawang STATUS RESOLVED:** Police investigations ARE ACTIVE at Kuala Klawang (DUN Klawang N.28 T1 area). The PDM is NOT closed — investigation papers opened, not resolved. This answers the midafternoon cycle's "PDM Klawang reopening UNRESOLVED (hour 21+)" — the PDM activity is active with police investigating election sabotage.
- **Significance:** Campaign sabotage escalation: 3 seats affected (Klawang + Palong + Chembong Tier-4). PDM Klawang question resolved — police actively investigating. NS police chief Alzafny Ahmad is the common authority (also handles ceramah permits).

### 9. Election-related death — man killed installing party flags near Rantau [NEW]
→ `priority_PIR-06-PIR-07_sinarharian_lelaki-maut-dilanggar-lari-ketika-pasang-bendera-parti-sinar-harian_20260720_lateafternoon_targeted.md` (Sinar 788630)
- 23-year-old man killed in **hit-and-run** while installing party flags on Jalan Kuala Sawah-Rantau near Kampung Belangkan (Sunday 6:40pm).
- A lorry hit a signpost and the man on the road shoulder. Driver fled.
- Seremban OCPD Asst Comm **Mohd Yatim Osman**: investigated under **Section 41(1) Road Transport Act 1987**.
- Witness hotline: Inspektor Nor Fadzilah Mohd Zainuddin (019-4611794), Bilik Gerakan IPD (06-6033222).
- **Significance:** FIRST election-related fatality in PRN NS 2026. Occurred near Rantau (Tok Mat's seat area). Campaign activity (flag installation) turned deadly — significant PIR-07 escalation.

### 10. Police approve 107 ceramah permits [FRESH 14:55 MYT, NEW]
→ `priority_PIR-06-PIR-07_utusan_prn-negeri-sembilan-polis-lulus-107-permit-ceramah-kempen_20260720_lateafternoon_home.md` (Utusan, by Nor Shafiqah Mohd Ghazali)
- **NS police chief Datuk Alzafny Ahmad:** 107 permits approved (out of 109 received, 18-19 Jul).
- 19 Jul alone: 90 received, 88 approved (2 rejected for non-compliance).
- Security situation "baik dan terkawal" (good and controlled).
- 2 investigation papers opened for election sabotage (Section 427 Penal Code — see #8 above).
- **Significance:** Campaign operational data — 107 active permits. Police monitoring all political programs.

### 11. Six PKR candidates lost party elections — analyst warns of machinery disunity [NEW]
→ `priority_PIR-06-PIR-07_sinarharian_enam-calon-pkr-kalah-pemilihan-parti-penganalisis-sinar-harian_20260720_lateafternoon_targeted.md` (Sinar 788622)
- **Analyst Muhammad Afifi Abdul Razak** (senior lecturer): at least 6 PKR PRN NS candidates lost 2025 party elections at branch level:
  1. **DUN Gemas:** Siti Aishah Seman — lost Ketua Cabang Tampin (41.52%)
  2. **DUN Ampangan:** Datuk Muhammad Nazri Kassim — lost Ketua Cabang Seremban (47.91%)
  3. **DUN Labu:** Datuk Ahmad Faez Abdul Razak — lost Ketua Cabang Rasah (35.10%)
  4. **Kuala Pilah:** Mohd Aidil Abdullah — lost Ketua Cabang (46.04%)
  5. **Kuala Pilah:** Mohd Kamarul Arifin Mohd Wafa — lost Timbalan Ketua Cabang (36.49%)
  6. **DUN Pilah:** Datuk Nur Zunita Begum Mohd Ibrahim — lost Ketua Wanita Cabang (37.05%)
- Warning: supporters may become passive, silently boycott, or campaign minimally. "Elections are won through voter acceptance, machinery unity, and member confidence."
- **Critical analysis of Aminuddin's seat swap:** "Why would PKR give up a proven-safe seat (Sikamat) for the MB to contest a BN-held seat (Linggi) with more uncertain prospects?" If Aminuddin loses Linggi → signals voters rejecting his leadership → weakens PH's admin-achievement narrative. "If PKR fails to hold Sikamat and loses marginal seats due to disunited machinery, this swap will be remembered as a strategic error, not a bold move."
- Sidebar references: "Leevineshwaraan calon termuda, Tok Mat antara paling otai", "Calon tertua 70 tahun, termuda 23 tahun", "Tiada kertas penamaan calon ditolak, 103 sah bertanding"
- **Significance:** VERY high-value PIR-07 intel. Names all 6 PKR candidates who lost internal elections (cross-references with Pilah, Gemas, Ampangan, Labu findings). First detailed critical analysis of Aminuddin's Sikamat→Linggi swap from an analytical perspective. Confirms 103 candidates total, youngest 23, oldest 70.

---

## 🟡 PIR-16 — FIRST DOMINANT CAMPAIGN NARRATIVES — late afternoon updates

### 1. Fathi Aris: "PH has no right to feel cheated" — major narrative analysis [NEW]
- See PIR-06 #2 above for full details. Key PIR-16 angles:
  - Reinforces "BN free to partner PN" normalization (PRN Johor + NS = new PRU16 term)
  - Rebuts AMH "resign to attack" call (Kamil Munim thread from morning)
  - Cites Melaka PRN late 2021 (BN vs PN vs PH three-way) as precedent for parties in government contesting each other
  - "PH salah membaca asas kerjasama" — PH misread the Unity Government basis
  - Sidebar "Bersatu kian tidak relevan, hadapi krisis identiti" continues surfacing (paywalled, midafternoon cycle)

### 2. 6 PKR candidates lost party elections — internal friction narrative [NEW]
- See PIR-07 #11 above. PIR-16 angle: analyst frames PKR's candidate selection as potentially undermining internal democracy → "meninggalkan terlalu banyak persoalan" (leaves too many questions). This is a narrative challenge for PKR's campaign — if supporters feel their branch-level winners were bypassed, machinery motivation drops.

### 3. "Bersatu sasar bentuk kerajaan negeri" — structural evidence [CARRY-FORWARD]
- Pertang: Faizal Fadli Idrus as "calon Bersatu" (not "calon PN")
- Sikamat: Bersatu (Tun Faisal) vs PN/Wawasan (Razali) — competing against each other
- Bersatu running independently from PN/Wawasan = the "sasar bentuk kerajaan negeri" narrative manifesting in candidate selection
- NOT [CRITICAL] — no hard-news outlet has explicitly stated "Bersatu exit imminent" or "Bersatu sasar bentuk kerajaan negeri" as a headline. The structural evidence (separate candidates) is clear but the explicit narrative hasn't been published as hard news.

---

## ⚠️ COLLECTION LIMITATIONS (late afternoon cycle)

- **gnews freshness (23rd cycle):** 67 queries → 676 items, 420 PRN/priority hits, **1 fresh** (Pertang Mandarin PKR via FMT). gnews continues to surface mostly historical matches. The 1 fresh hit was successfully extracted via Awani URL.
- **Harian Metro RSS — NEW working source:** `https://www.hmetro.com.my/feed` returned 51 items (37 PRN/priority hits) — a breakthrough after 22 cycles of HTTP 000/404. Harian Metro now provides full-text RSS content. However, the alt-path homepage recovery phase captured 13 favicon PNG files as false positives (deleted).
- **RSS feeds:** FMT 50 items (18 PRN saved), HarianMetro 51 items (31 saved), Awani 10 items (8 PRN hits, 1 fresh saved). NST/MalayMail/Sinar/Utusan/BH RSS feeds still return 0 (JS/403).
- **Sinar article-ID scan:** 788590-788660 yielded 30 articles (many non-PRN but several genuinely-new PRN articles including Pilah, Gemas, Fathi Aris, 6-PKR-loss, Terengganu, death). 0 paywalled (unlike midafternoon's 4 paywalled — the targeted range shifted to news articles, not opinion/premium).
- **Homepage extraction:** 7 articles saved (Utusan, Sinar, MalayMail). NST/Star/Kosmo/BH/mStar returned few candidate links.
- **[CRITICAL] auto-flag:** 1 false positive (Nur Jazlan Senate, sidebar "dipecat Bersatu" = Kelantan individual expelled by party, not PN expelling Bersatu). Corrected in-file. Detector needs semantic refinement for sidebar text (related-article links shouldn't trigger [CRITICAL]).
- **False positives (~40):** favicon PNGs (13, deleted), World Cup/football, crime stories, international (Nicaragua, Iran, Singapore minister, Orang Asli), federal parliament (KWAP/eFishery, Vivy Yusof, Nur Jazlan Senate, MV Berkat Tuah, imigresen), weather alerts, missing persons. Many triggered on substring matches ("negeri" in non-NS context, "anwar" in federal news, "pn" as common abbreviation).

---

## 📈 CYCLE DELTA: midafternoon → late afternoon (13:55 → 15:21 MYT 20 Jul, ~1h26m)

- **Articles saved:** 91 (after 13 favicon deletions; 53 RSS + 1 URL-extract + 7 homepage + 30 Sinar targeted)
- **Genuinely-new FULL-TEXT:** **~14** (Pertang EN+BM, Chuah Awani+Sinar, Pilah, Gemas, Gemencheh, Bahau, Sikamat PN/Wawasan, flags-sabotage HarianMetro, death Sinar, permits Utusan, 6-PKR-loss Sinar, Fathi Aris Sinar, Terengganu Sinar)
- **Genuinely-fresh post-cutoff (≥13:55 MYT):** **2** (Pertang 14:13 MYT via FMT RSS, Chuah 14:20 MYT via Awani)
- **PIR-06 status:** [CRITICAL] MAINTAINED (23rd cycle). 1 auto-flag FALSE POSITIVE corrected. NEW intel: (a) No BN-PN talks in Terengganu = NS-specific cooperation confirmed; (b) Fathi Aris major narrative analysis; (c) Bersatu-separate-from-PN/Wawasan additional data point (Pertang).
- **PIR-07 status:** **HIGHEST YIELD this cycle** — 11 major new intelligence items: Pertang 3-corner, Chuah resolved, Pilah two-women RECOVERED, Gemas candidate, Gemencheh oldest candidate, Bahau MCA, Sikamat PN/Wawasan profile, flags-sabotage + PDM Klawang RESOLVED, election death, 107 permits, 6-PKR-loss analyst.
- **PIR-16 status:** NOT [CRITICAL]. Fathi Aris narrative analysis + 6-PKR-loss internal friction + "Bersatu sasar bentuk" structural evidence (no explicit hard-news headline yet).
- **Source breakthrough:** Harian Metro RSS now working (51 items, 31 saved) — first time in 23 cycles. Major addition to source coverage.
- **PDM Klawang:** RESOLVED — police actively investigating at Kuala Klawang, Jelebu (2 investigation papers, Section 427 Penal Code). Not closed, not reopened — active investigation.

---

## 🎯 NEXT-CYCLE RECOMMENDATIONS (16:00–20:00 MYT window → PH manifesto launch tonight)

1. **PIR-07 (PRIORITY):** **PH MANIFESTO LAUNCH tonight ~18:00-20:00 MYT** — expected to be the biggest campaign event of Day 2-3. Capture ALL coverage when published (Awani, FMT, NST, Star, Sinar, Utusan, HarianMetro). Look for: manifesto content/pledges, Amirudin Shari officiation, Aminuddin Harun's role, PH's 36-seat strategy, MB-after-PRN narrative.
2. **PIR-07 (continued):** **BN MANIFESTO 24 Jul at DUN Linggi + Pertang** — monitor for advance coverage/announcements. Track Jalaluddin's Pertang campaign ground intel. Monitor Chembong (N31) + Palong sabotage follow-up (police investigation outcomes). Track the election-death hit-and-run investigation (Rantau area).
3. **PIR-06 ([CRITICAL] watch):** 23rd cycle with no threshold crossing. Maintain formal-removal watch: Bersatu Supreme Council quorum, RoS, "lebih hebat new coalition," Bersatu candidate withdrawal. Monitor whether Bersatu-separate-from-PN/Wawasan arrangement escalates to formal coalition statement. Monitor Gerakan-Bersatu Rahang dispute follow-up.
4. **PIR-16:** Track "Bersatu kian tidak relevan / krisis identiti" — does any hard-news outlet explicitly publish "Bersatu exit imminent?" or "Bersatu sasar bentuk kerajaan negeri" as headline? If yes → [CRITICAL]. Track Fathi Aris narrative pickup. Track AMH/Kamil Munim response to Fathi's rebuttal. Monitor "toxic PN" volley (Hamzah ↔ Marzuki).
5. **Source maintenance:** **Harian Metro RSS now working** — add to regular RSS polling cycle. Sinar homepage extraction = proven yield. Re-poll FMT/Awani/HarianMetro RSS for post-15:21 MYT fresh content. Sinar Premium paywall still blocks opinion pieces (if credentials available: Bersatu identity crisis, coalition-vs-coalition, PKR strategy). gnews URL resolution remains curl-infeasible (23rd cycle).

---

*Late afternoon cycle index appended 2026-07-20 ~15:25 MYT (07:25 UTC) by PRN Negeri Sembilan 2026 News Collection Agent — Nomination-Day Surge Mode. TLP:AMBER. 91 articles saved (53 RSS + 1 URL + 7 homepage + 30 Sinar targeted; 13 favicon false positives deleted). [CRITICAL] NOT crossed (23rd cycle; 1 auto-flag FALSE POSITIVE corrected — Nur Jazlan Senate sidebar "dipecat Bersatu" = Kelantan individual, not PN expelling Bersatu). Source breakthrough: Harian Metro RSS working for first time (51 items, 31 saved). Key late afternoon developments: (1) Pertang T1 3-corner confirmed — Umry (PH) vs Jalaluddin (BN) vs Faizal Fadli Idrus (Bersatu); Mandarin fluency strategy; (2) Chuah controversy RESOLVED — Boon Lai (PH) vs Pau Jeou Ching (BN) 2-cornered; Kenny Chiew gives full support; (3) DUN Pilah two-women contest RECOVERED — Noorzunita (PH) vs S Leza (BN); (4) DUN Gemas N34 PKR woman candidate Siti Aishah profiled; Felda Gugusan Jelai issue; (5) DUN Gemencheh PH oldest candidate Abd Latif (70, AMANAH) vs Suhaimizan (BN); (6) DUN Bahau MCA Ah Chong challenges DAP 20-year stronghold; BN-PN ground cooperation confirmed; (7) Sikamat PN/Wawasan candidate Razali (ex-police) profiled; Bersatu vs PN/Wawasan split confirmed; (8) Campaign sabotage escalation — Palong flags burned + Chembong Tier-4 damaged + PDM Klawang RESOLVED (police 2 investigation papers at Kuala Klawang); (9) First election-related death — man killed installing flags near Rantau; (10) 107 ceramah permits approved; (11) 6 PKR candidates lost party elections — analyst warns machinery disunity + questions Aminuddin Sikamat→Linggi swap; (12) Fathi Aris: "PH has no right to feel cheated" — major PIR-16 narrative; (13) No BN-PN talks in Terengganu — NS-specific cooperation confirmed. PH manifesto launch tonight 18:00-20:00 MYT — next major collection window.*

---

# DUSK CYCLE — 20260720_dusk (15:25 → 16:37 MYT 20 Jul, ~1h12m)

**Cutoff:** post-07:25 UTC 20 Jul (post-15:25 MYT 20 Jul) = prior lateafternoon cycle end
**Fetcher:** `_surge_fetch_20260720_dusk.py` (gnews ×82 queries + Awani/FMT/HarianMetro RSS full + homepage extraction NST/Star/MalayMail/Utusan/Sinar/Kosmo) + `_dusk_sidebar_fetch_20260720.py` (6 fresh Utusan sidebar articles referenced in PH manifesto piece)
**Articles saved:** **39** (26 RSS + 1 gnews URL-extract + 6 homepage + 6 Utusan sidebar targeted)
**Genuinely-fresh post-cutoff (≥15:25 MYT):** **8** (Aminuddin jaga adab 15:56, PH manifesto 15:51, derhaka rebuttal 15:59, PH Selangor BN-PN 15:56, Akmal DAP ketandusan 15:35, Kamil Munim rebuttal 15:32, Rafizi Melaka 15:28, MCA KWAP eFishery 15:42)
**Enrichments (Utusan republications of prior Sinar content):** 3 (KJ "ada sesuatu tak kena" 07:58, Noh Omar "rampas Selangor" 08:10, NS penentu PRU16)
**[CRITICAL] status: MAINTAINED (24th cycle). NO NEW THRESHOLD CROSSING.** 1 auto-flag FALSE POSITIVE corrected (Fashion Valet CBT trial — PNB matched "pn"; "withdraw"/"advances" matched fund-withdrawal not candidate withdrawal). gnews 82 queries → 694 items, 425 PRN/priority hits, 1 fresh; critical-keyword scan = **0 hits**.

---

## 🔴 PIR-06 — COALITION OPERATIONAL ARRANGEMENT — [CRITICAL] NOT CROSSED (24th cycle)

**[CRITICAL] status: MAINTAINED. 24th cycle with no formal PN-MT expulsion notice, no Bersatu candidate withdrawal (24 solo Bersatu-logo candidates stable), no Kiandee/PN quorum escalation, no PN/Bersatu Supreme Council statement, no RoS intervention, no "lebih hebat new coalition" formalization. All 8 mandatory gnews [CRITICAL]-watch queries returned 0. gnews critical-keyword scan across 425 priority headlines = 0 hits.**

**NEW PIR-06 intelligence this dusk cycle (cooperation-friction + spread, NOT formal-threshold):**

### 1. BN-PN cooperation "will spread to all states" — PH Selangor Amanah [FRESH 15:56 MYT, NEW]
→ `priority_PIR-06-PIR-07_Utusan_ph-selangor-yakin-hadapi-gelombang-kerjasama-bn-pn_20260720_dusk_sidebar.md`
- **Amanah Selangor communications director Abbas Azmi** (ADUN Sri Serdang): PH Selangor NOT afraid of BN-PN cooperation trend, but EXPECTS it to spread from Johor+NS to all states including Melaka and Selangor.
- "It (BN-PN cooperation) will continue. We see the pattern is already there and eventually it will go to all states."
- **Intra-unity-government friction escalation:** Calls for BN political appointees in Selangor who criticize the state government to RESIGN. "Those unable to be disciplined in the organization and continue criticizing the government they represent should consider resigning." Says BN ADUNs contribute "minimum" to the state government.
- "Api dalam sekam" (smoldering fire) warning — risk to state government stability if BN-PN cooperation not reviewed.
- If BN leaves Selangor state gov, PH still has enough majority to govern.
- **Significance:** NEW escalation of intra-unity-government friction in Selangor. Confirms BN-PN cooperation is read as a multi-state trend by PH itself. Not [CRITICAL].

### 2. Noh Omar: BN-PN can capture 6 parliament + 34 DUN Selangor seats [Utusan republication, 08:10 MYT]
→ `priority_PIR-06-PIR-07_Utusan_kerjasama-bn-pn-mampu-rampas-selangor_20260720_dusk_sidebar.md`
- **Noh Omar** (ex-UMNO Selangor chief): if NS BN-PN formula succeeds → 6 parliamentary + 34 DUN Selangor seats capturable. Named: **Kuala Selangor, Shah Alam, Sepang, Hulu Langat, Gombak, Sungai Buloh**.
- Three-cornered Umno/PAS/PH only benefits PH (cites KJ's Sungai Buloh GE15 defeat).
- **KJ** at same event (Subang UMNO youth/wanita/puteri): BN-PN cooperation = "a good experiment," "anjalan dan pejal" (flexible vs rigid). "We can give our votes to PAS and Wawasan candidates, and vice versa." → confirms **Wawasan as a PN-coalition vote-recipient partner** (NS operational arrangement: votes flow BN↔PAS↔Wawasan).
- **Significance:** Utusan enrichment of prior Sinar content. Confirms Wawasan's role in the BN-PN vote-sharing arrangement. PIR-06 cooperation-arrangement + PIR-16 "makmal politik PRU16."

### 3. Terengganu "tunggu dan lihat" — NS-specific cooperation reconfirmed [14:10 MYT]
→ `priority_PIR-06-PIR-07_Utusan_kerjasama-bn-pn-umno-terengganu-tunggu-dan-lihat_20260720_dusk_sidebar.md`
- **UMNO Terengganu chief Datuk Rozi Mamat** (UMNO Supreme Council): "wait and see" on BN-PN cooperation. NO discussions yet in Terengganu — "landscape differs by state." References Sarawak as precedent for state/federal cooperation differences.
- "We need to be smart in adapting to strengthen our own party without thinking too much about others."
- **Significance:** Confirms (3rd corroboration: prior Sinar + lateafternoon Utusan + this Utusan) that BN-PN cooperation is NS-specific, not a national mandate. Terengganu, Perlis = "wait and see / not impossible" posture.

### 4. Perlis: "not impossible" BN-PN cooperation continues [Utusan, dated 20 Jul]
→ `priority_PIR-06-PIR-07_Utusan_tidak-mustahil-kerjasama-bn-pn-diteruskan-di-perlis-utusan-malaysia_20260720_dusk_sidebar.md`
- **Significance:** Perlis joins Terengganu as "wait-and-see" state. NS cooperation model = potential template but not yet adopted elsewhere.

**Tier-4 seat watch (N.04, N.05, N.13, N.14, N.23, N.25, N.31, N.34):**
- **N.31 Palong** — NEW intel: BN candidate **Datuk Mustapha Nagoor** actively campaigning at Pasar Tani Keluarga Malaysia Palong (Jempol) — pushes back against "derhaka" narrative (see PIR-07 #1). Ground campaign confirmed at Tier-4 seat.
- No Bersatu candidate withdrawals. No other new Tier-4 intel.

---

## 🟠 PIR-07 — HIGHEST-PRIORITY BATTLEGROUNDS — DUSK UPDATES

### 1. DERHAKA COUNTER-NARRATIVE — BN Palong (N.31) candidate pushes back [FRESH 15:59 MYT, NEW — HIGH VALUE]
→ `priority_PIR-06-PIR-07_Utusan_tarik-sokongan-kepada-mb-bukan-derhaka_20260720_dusk_sidebar.md`
- **BN Palong (N.31 Tier-4) candidate Datuk Mustapha Nagoor:** "Withdrawing support from the MB is NOT derhaka. Derhaka is opposing the Ruler, the Undang Yang Empat."
- "Menarik sokongan daripada Menteri Besar tak boleh istilah derhaka. Derhaka ini adalah kita menentang raja, menentang Undang Yang Empat."
- **References DAP Melaka as precedent:** "DAP Melaka withdrew support from the Melaka state government. Are they derhaka? No."
- Campaigning at Pasar Tani Keluarga Malaysia, Palong, Jempol.
- **Significance:** FIRST direct BN rebuttal of the "derhaka" narrative that PH has used to frame BN-PN cooperation as betrayal. Originates from a Tier-4 (N.31 Palong) candidate on the ground. The DAP Melaka precedent is notable — frames withdrawal-of-support as normal democratic politics, not treason. PIR-07 (derhaka narrative at Palong Tier-4) + PIR-16 (narrative contestation).

### 2. Aminuddin: "jaga adab, integriti" — call for decorous campaigning [FRESH 15:56 MYT, NEW]
→ `priority_PIR-07-PIR-16_Awani_prn-negeri-sembilan-aminuddin-ingatkan-ahli-politik-jaga-adab-integriti-sepanjan_20260720_dusk.md`
- Aminuddin (caretaker MB) urges ALL parties to campaign with integrity + mature politics. "We are in a state that is beradat dan beradab (has customs and manners) — I hope all political parties follow the rules."
- Spoke at PH candidate press conference for DUN Chuah and Sri Tanjung, Port Dickson.
- References the **2 police investigation papers** on election sabotage (from lateafternoon cycle: Palong flags burned, Chembong damaged, Klawang drain).
- **Significance:** Aminuddin's "adat dan adab" framing connects to the "adat" PIR-16 keyword (Tok Mat's "adat politik" narrative from prior cycles). Positions PH as the decorous/civilized campaigner vs the sabotage incidents. FRESH post-cutoff.

### 3. PH MANIFESTO TONIGHT — CONFIRMED + content preview [FRESH 15:51 MYT, NEW — KEY EVENT]
→ `priority_PIR-06-PIR-07_Utusan_ph-tawar-manifesto-lebih-menyeluruh-manfaat-semua-golongan_20260720_dusk_home.md`
- **Aminuddin confirms PH NS manifesto launches TONIGHT (20 Jul evening)**, attended by key PH leaders.
- **Manifesto content preview:** expands benefits beyond B40 → **M40** ("we want more rakyat to benefit"). Continuity of prior state-government initiatives retained + new additions.
- "Banyak yang kami teruskan, kami mendapat maklumat inisiatif sebelum ini telah memberi manfaat yang besar kepada penduduk di Negeri Sembilan."
- Aminuddin met traders at Medan Selera Dataran Tanjung Agas, Linggi, Port Dickson (Linggi campaign ground intel).
- **Significance:** CONFIRMS the PH manifesto launch event flagged as the next major collection window in the lateafternoon index. B40→M50 expansion = notable manifesto strategy. This is a pre-launch preview — the full manifesto content + launch coverage (expected 18:00-20:00 MYT) = next cycle priority. PIR-07 + PIR-16.

---

## 🟡 PIR-16 — FIRST DOMINANT CAMPAIGN NARRATIVES — [CRITICAL] NOT CROSSED (24th cycle)

**PIR-16 [CRITICAL] threshold NOT CROSSED.** No hard-news outlet corroboration of "Bersatu exit imminent?" or "Bersatu sasar bentuk kerajaan negeri" as explicit headline (gnews 0 hits; no RSS/homepage match). The "Bersatu kian tidak relevan / krisis identiti" narrative continues to surface in sidebar text but no hard-news headline yet.

### NEW PIR-16 intelligence this dusk cycle:

### 1. Akmal Saleh: DAP "ketandusan idea" bringing "new lies" to NS PRN [FRESH 15:35 MYT, NEW]
→ `priority_PIR-06-PIR-07-PIR-16_Sinar_dap-ketandusan-idea-bawa-penipuan-baharu-pada-prn-negeri-sembilan-akmal-saleh-si_20260720_dusk_home.md`
- **Umno Youth chief Datuk Dr Muhamad Akmal Saleh** (ADUN Merlimau): DAP "running out of ideas," continuing to use misleading narratives in NS PRN.
- "Previously DAP lied to the rakyat with 'undi BN, Najib dibebaskan' in Johor. This time in NS they come with a new lie."
- References **Tony Pua's PRU16 claim**: Pua urged voters to keep supporting PH, warning that **Zahid would become PM** if otherwise. Voting for "pengacau" (spoiler) parties or not voting = advantages BN.
- **Significance:** NEW PIR-16 narrative volley from Akmal (Umno's most aggressive campaigning voice). Frames DAP as deceitful; the Tony Pua/Zahid-PM angle connects to the intra-unity-government tension. PIR-16 "DAP acceptance" + "MCA biggest loser" narrative cluster.

### 2. Kamil Munim JET REBUTTAL — denies asset misuse [FRESH 15:32 MYT, NEW]
→ `priority_PIR-06-PIR-07_Sinar_dakwaan-salah-guna-aset-kerajaan-tidak-benar-kamil-munim-sinar-harian_20260720_dusk_home.md`
- **AMK chief Kamil Munim** (PM's political secretary): DENIES misusing government assets/jet during Kelantan visit. Explains he accompanied PM Anwar on official duties (Terminal Lapangan Terbang Sultan Ismail Petra, mosque ramah mesra, PKR convention).
- "I was assigned to accompany the PM. I only followed in my capacity as political secretary — not using government facilities for personal interest."
- References **Tengku Zafrul** (PM's senior advisor) also implicated in the jet-misuse allegation.
- Warns netizens/TikTokers about fitnah (slander) "especially now in election season."
- **Significance:** This is the REBUTTAL to the "jet rasmi" allegation that surfaced in the morning cycle (where Kamil was the PKR Youth chief framing BN-PN as a plot to topple Anwar). The jet-misuse attack was a counter-offensive against Kamil's anti-BN-PN rhetoric. PIR-16 Kamil Munim narrative thread + intra-PKR tension.

### 3. Rafizi's "Bersama" party will be "humiliated again in Melaka" — analyst [FRESH 15:28 MYT, NEW]
→ `priority_PIR-06-PIR-07_Sinar_selepas-johor-parti-rafizi-akan-dimalukan-lagi-di-melaka-penganalisis-sinar-hari_20260720_dusk_home.md` + `priority_..._Utusan_..._20260720_dusk_home.md`
- **Analyst Prof Madya Dr Mohamad Faisol Keling** (UUM): after losing ALL 15 DUN seats in Johor (lost deposits), Rafizi's "Bersama" party will face the same fate in Melaka PRN.
- Reasons: high Malay rejection of Rafizi's ministerial performance + Chinese voters returning to PH after PAS-BN cooperation.
- **Tony Pua** calls Bersama "parti pengacau" (spoiler party) — broke PH votes causing 2-seat loss in Johor.
- Bersama confirmed NOT contesting NS PRN16, focusing on Melaka.
- **Significance:** PIR-16 "Melaka PH-BN fracture" + "Melaka withdrawal" narrative. Bersama = the new spoiler-party variable. Confirms Melaka PRN as the next domino after NS.

### 4. MCA asserts accountability voice — KWAP/eFishery PAC probe call [FRESH 15:42 MYT, NEW]
→ `priority_PIR-06-PIR-07_Sinar_mca-gesa-pac-siasat-kerugian-pelaburan-kwap-dalam-efishery-sinar-harian_20260720_dusk_home.md`
- **MCA information chief Chan Quin Er** urges PAC to investigate KWAP's loss in eFishery (Indonesian aquaculture tech startup). RM200m (PM's figure) vs RM163.4m (KWAP's figure) discrepancy.
- Targets **Anwar as both PM and Finance Minister** — "cannot confirm the process was correct while simultaneously denying responsibility when KWAP was defrauded."
- Demands: KWAP board, investment panel, top management explain approval process + control mechanisms. SPRM investigation if negligence/breach found.
- eFishery ex-CEO sentenced to 9 years in Indonesia for financial manipulation.
- **Significance:** PIR-16 "MCA rebuttal / MCA biggest loser" — MCA is actively asserting itself as an accountability/fiscal-watchdog voice DURING the NS campaign period (KWAP = federal issue, not NS-specific). This is MCA's positioning counter to the "MCA biggest loser" narrative. Chan Quin Er = emerging MCA spokesperson.

### 5. KJ: "ada sesuatu yang tak kena dalam kerjasama BN-PH" [Utusan republication, 07:58 MYT]
→ `priority_PIR-06-PIR-07_Utusan_ada-sesuatu-yang-tak-kena-dalam-kerjasama-bn-ph_20260720_dusk_sidebar.md`
- **KJ** (ex-UMNO youth chief, Rembau): "Something is wrong with BN-PH cooperation in the Federal Government." Johor = first warning, NS = next, Melaka = second warning, PRU16 = third ("we thrash them completely").
- Warns DAP/Nga Kor Ming: "jangan cakap macam itu" — PH partners keep crossing lines.
- UMNO must sell dreams to urban Malays (80% of Malays live in cities) — AI engineers, millionaires.
- **Significance:** Utusan enrichment of prior Sinar "ada sesuatu yang tak kena dalam kerajaan perpaduan" piece. Full KJ "makmal politik PRU16" framing: Johor→NS→Melaka→PRU16 escalation ladder. PIR-16 "makmal politik" + "penyatuan undi Melayu."

### 6. "Bersatu sasar bentuk kerajaan negeri" — structural evidence [CARRY-FORWARD, NOT CRITICAL]
- Bersatu running independently from PN/Wawasan (separate candidates at Pertang, Sikamat, Rahang) = the structural manifestation. No hard-news headline yet explicitly stating "Bersatu sasar bentuk kerajaan negeri" or "Bersatu exit imminent." Maintained.

---

## ⚠️ COLLECTION LIMITATIONS (dusk cycle)

- **gnews freshness (24th cycle):** 82 queries → 694 items, 425 PRN/priority hits, **1 fresh** (Aminuddin jaga adab via Awani 15:56 MYT). gnews continues to surface mostly historical matches; the 1 fresh hit was successfully extracted.
- **RSS feeds:** FMT 50 (18 PRN saved), HarianMetro 51 (11 PRN saved), Awani 10 (1 fresh saved). NST/MalayMail/Sinar/Utusan/BH RSS still return 0 (JS/403).
- **Homepage extraction:** 6 articles saved (Utusan, Sinar). NST/Star/Kosmo/BH/mStar returned few/no PRN candidate links.
- **Sinar targeted scan (788660-788720):** 0 PRN hits — range exhausted (no new articles in that ID window). The fresh Sinar content (788631-788636) was recovered via homepage extraction, not ID scan.
- **Utusan sidebar recovery:** 6 fresh articles recovered by following sidebar links from the PH manifesto piece — high-yield technique. Discovered: derhaka rebuttal, PH Selangor BN-PN, Terengganu, Perlis, rampas Selangor, KJ ada sesuatu tak kena.
- **[CRITICAL] auto-flag:** 1 FALSE POSITIVE corrected (Fashion Valet CBT trial — PNB = Permodalan Nasional Bhd matched "pn"; "withdraw"/"advances" matched fund-withdrawal, not candidate withdrawal). Detector needs PNB-surname exclusion + context-aware "withdraw" disambiguation.
- **False positives (~15):** World Cup (Bangi Square, Johor footbrawl, Dataran Merdeka sampah), crime (rape, mechanic, police chief), federal (Fashion Valet, data centres, CIMB, Airborneo, Ryanair, Cyprus, Hormuz vessel, Sabah diesel), bowling, TFC recruit.

---

## 📈 CYCLE DELTA: late afternoon → dusk (15:25 → 16:37 MYT 20 Jul, ~1h12m)

- **Articles saved:** 39 (26 RSS + 1 gnews URL + 6 homepage + 6 Utusan sidebar)
- **Genuinely-fresh post-cutoff (≥15:25 MYT):** **8** (Aminuddin jaga adab 15:56, PH manifesto preview 15:51, derhaka rebuttal 15:59, PH Selangor BN-PN 15:56, Akmal DAP ketandusan 15:35, Kamil Munim rebuttal 15:32, Rafizi Melaka 15:28, MCA KWAP eFishery 15:42)
- **Enrichments:** 3 (KJ, Noh Omar, NS-penentu-PRU16 — Utusan republications of prior Sinar content)
- **PIR-06 status:** [CRITICAL] MAINTAINED (24th cycle). 1 auto-flag FALSE POSITIVE corrected. NEW intel: (a) BN-PN cooperation "will spread to all states" (Amanah Selangor); (b) Wawasan confirmed as PN vote-sharing partner (KJ); (c) Terengganu + Perlis "wait-and-see" reconfirms NS-specific cooperation; (d) N.31 Palong ground campaign (Mustapha Nagoor).
- **PIR-07 status:** 3 major new items — (1) derhaka COUNTER-narrative from BN Palong candidate (N.31 Tier-4); (2) Aminuddin "jaga adab" call; (3) PH manifesto TONIGHT confirmed + B40→M50 preview.
- **PIR-16 status:** NOT [CRITICAL]. 4 new narrative items — (a) Akmal "DAP ketandusan idea" + Tony Pua/Zahid-PM angle; (b) Kamil Munim jet rebuttal; (c) Rafizi "Bersama" Melaka humiliation forecast; (d) MCA KWAP/eFishery accountability voice (Chan Quin Er).
- **Key narrative contestation this cycle:** the "derhaka" frame (PH) vs "bukan derhaka, ini demokrasi" (BN Palong) — first direct BN rebuttal. Plus MCA asserting fiscal-watchdog role (KWAP) counter to "MCA biggest loser" framing.

---

## 🎯 NEXT-CYCLE RECOMMENDATIONS (17:00–22:00 MYT window → PH MANIFESTO LAUNCH tonight)

1. **PIR-07 (HIGHEST PRIORITY):** **PH MANIFESTO LAUNCH TONIGHT ~18:00-20:00 MYT** — now CONFIRMED by Aminuddin (Utusan 15:51). Capture ALL coverage when published (Awani, FMT, NST, Star, Sinar, Utusan, HarianMetro). Look for: full manifesto pledges/content, Amirudin Shari officiation, B40→M50 details, MB-after-PRN narrative, PH's 36-seat strategy.
2. **PIR-07 (continued):** Monitor derhaka narrative evolution — does PH respond to BN Palong candidate's "bukan derhaka" rebuttal? Track Chembong (N.27/N.31) + Palong sabotage follow-up. Track election-death hit-and-run investigation (Rantau area). BN manifesto 24 Jul at DUN Linggi + Pertang — monitor advance coverage.
3. **PIR-06 ([CRITICAL] watch):** 24th cycle with no threshold crossing. Maintain formal-removal watch: Bersatu Supreme Council quorum, RoS, "lebih hebat new coalition," Bersatu candidate withdrawal. Monitor Wawasan vote-sharing arrangement (now confirmed by KJ). Monitor Gerakan-Bersatu Rahang dispute follow-up.
4. **PIR-16:** Track whether any hard-news outlet explicitly publishes "Bersatu exit imminent?" or "Bersatu sasar bentuk kerajaan negeri" as headline → if yes = [CRITICAL]. Track Akmal's "DAP ketandusan idea" narrative pickup. Track MCA KWAP/eFishery story (does it escalate to a major campaign issue?). Track Kamil Munim jet rebuttal response. Monitor "toxic PN" volley.
5. **Source maintenance:** Utusan sidebar-link following = proven high-yield technique (6 fresh articles). Re-poll FMT/Awani/HarianMetro RSS for post-16:37 MYT fresh content. Sinar homepage extraction = proven yield. gnews URL resolution = 1 fresh hit this cycle (Awani Aminuddin piece).

---

*Dusk cycle index appended 2026-07-20 ~16:37 MYT (08:37 UTC) by PRN Negeri Sembilan 2026 News Collection Agent — Nomination-Day Surge Mode. TLP:AMBER. 39 articles saved (26 RSS + 1 gnews URL + 6 homepage + 6 Utusan sidebar). [CRITICAL] NOT crossed (24th cycle; 1 auto-flag FALSE POSITIVE corrected — Fashion Valet CBT trial: PNB matched "pn", "withdraw"/"advances" matched fund-withdrawal not candidate withdrawal). Key dusk developments: (1) PH MANIFESTO TONIGHT CONFIRMED — Aminuddin confirms launch 20 Jul evening, B40→M50 expansion, continuity of prior initiatives; (2) DERHAKA COUNTER-NARRATIVE — BN Palong (N.31 Tier-4) candidate Mustapha Nagoor: "withdrawing support from MB is NOT derhaka, derhaka = opposing Ruler/Undang Yang Empat"; references DAP Melaka precedent; (3) Aminuddin "jaga adab, integriti" call — references 2 police investigation papers on sabotage; (4) Kamil Munim JET REBUTTAL — denies asset misuse during Kelantan visit, explains PM political secretary role; references Tengku Zafrul; (5) Akmal Saleh: DAP "ketandusan idea" bringing "new lies" to NS PRN, references Tony Pua/Zahid-PM PRU16 claim; (6) Analyst: Rafizi's "Bersama" party will be "humiliated again in Melaka" after Johor wipeout; Tony Pua calls Bersama "parti pengacau"; (7) MCA Chan Quin Er urges PAC probe into KWAP RM200m eFishery loss, targets Anwar as PM+Finance Minister; (8) BN-PN cooperation "will spread to all states" — Amanah Selangor's Abbas Azmi; calls BN Selangor political appointees to resign; "api dalam sekam" warning; (9) Noh Omar: 6 parliament + 34 DUN Selangor seats capturable; KJ: Wawasan confirmed as PN vote-sharing partner; (10) Terengganu + Perlis "wait-and-see" reconfirms NS-specific cooperation. PH manifesto launch tonight 18:00-20:00 MYT — next major collection window.*

---

# 🌙 NIGHT CYCLE — 20260720_night (collected 18:26 MYT / 10:28 UTC, 20 Jul 2026)

**Cycle window:** 16:37 → 18:26 MYT 20 Jul 2026 (~1h49m since dusk cycle)
**Script:** `_surge_fetch_20260720_night.py` (88 gnews queries, 10 RSS feeds, 17 homepage pages, Sinar ID scan 788720-788800)
**Cutoff:** post-08:37 UTC 20 Jul (post-16:37 MYT 20 Jul) = prior dusk cycle end

## Collection Metrics

| Metric | Value |
|---|---|
| gnews queries | 88 |
| gnews items returned | 754 |
| gnews PRN/priority hits | 448 |
| gnews fresh post-cutoff | 1 |
| RSS feed items scanned | 865 (Awani 10, FMT 50, HarianMetro 51; NST/MalayMail/Sinar/Utusan/BH RSS = 0) |
| RSS PRN hits | 87 |
| RSS full-text saved | 30 |
| URL-extracted (gnews + RSS no-full) | 7 |
| Homepage extracted | 10 |
| Sinar ID scan (788720-788800) | 0 PRN hits |
| **Total articles saved** | **47 (script) + 1 manual (BN bazir) = 48** |
| Duplicates skipped | 48 |
| [CRITICAL] auto-flagged | **0** |
| False positives | ~20 (World Cup, crime, federal non-PRN, elephant transfer DAK) |

## Key New Articles (genuinely fresh post-16:37 MYT or new to collection)

### 1. PH MANIFESTO PREVIEW — launches TONIGHT [FRESH 18:05 MYT, HIGHEST PRIORITY] ⭐
→ `priority_PIR-07_HarianMetro_prn-n9-manifesto-ph-kesinambungan-usaha-kerajaan-perpaduan-beri-manfaat-semua-la_20260720_night_rss.md`
- **Aminuddin Harun** (MB, PH Linggi candidate) confirms PH manifesto launches tonight (20 Jul evening).
- Manifesto = **continuity of Unity Government's prior work** ("kesinambungan pengisian diusahakan kerajaan PH sebelum ini"). Covers all layers of society.
- Key quote: "Bukan harapan untuk mereka tunggu dan dengar tapi harapan untuk kita laksanakan" — emphasis on delivery, not promises.
- **Amirudin Shari** (Selangor MB, PH Presidential Council member, Co-Director of NS PRN) to officiate the launch.
- **Muhammad Zaki Md Sabri** (media centre sec-gen): manifesto will detail future plans as continuation of Aminuddin's administration.
- **PIR-07 Significance:** This is the PRE-LAUNCH preview. The actual launch event coverage (expected ~19:00-20:00 MYT) = NEXT collection target. Confirms Amirudin Shari's elevated campaign role.

### 2. Sanjeevan REBUTS Khaled "kacau daun" — Bersatu candidate fires back [FRESH 17:49 MYT, NEW] ⭐
→ `priority_PIR-06-PIR-07-PIR-16_FMT_sanjeevan-bidas-khaled-angkuh-gelar-bersatu-kacau-daun-di-n-sembilan_20260720_night_rss.md`
- **R Sri Sanjeevan** (Bersatu Associated Chief, DUN Jeram Padang candidate) rebuts Khaled Nordin's "Bersatu kacau daun" dismissal.
- Calls Khaled **"angkuh" (arrogant)** — Johor victory made Umno overconfident. "Mereka mula menunjukkan keangkuhan dan menganggap gelombang itu boleh dibawa ke Negeri Sembilan."
- **Johor ≠ NS:** "Keadaan politik di Johor dan Negeri Sembilan amat berbeza. Saya percaya gelombang yang berlaku di Johor tidak akan sampai ke Negeri Sembilan."
- Confident NS voters will **"block the blue wave"** ("menyekat gelombang biru") and Umno-BN resurgence under Zahid Hamidi.
- **Rejects "Bersatu will be buried" narrative:** "Apa juga yang berlaku kepada Bersatu dalam PN, ia tidak akan menyebabkan parti ini terkubur."
- **PIR-06/16 Significance:** Bersatu's own candidate directly pushing back against the "kacau daun / disarray" narrative (PIR-16). New narrative contestation vector: Bersatu's survival defense vs Umno's "kacau daun" dismissal. Not [CRITICAL] — no formal exit/expulsion/quorum trigger, but important PIR-16 rebuttal.

### 3. Akmal Saleh REBUTS AMK — "menggelupur sangat bila kita nak bersatu" [FRESH 18:14 MYT, NEW]
→ `priority_PIR-06-PIR-07_Sinar_menggelupur-sangat-bila-kita-nak-bersatu-akmal-saleh-bidas-amk-sinar-harian_20260720_night_home.md`
- **Akmal Saleh** (UMNO Youth chief) rebuts AMK (PKR Youth) criticism of Malay party unity efforts.
- AMK's **Ghafurullah Ismail** (Selangor AMK Sec-Gen) claimed UMNO is "willing to depend on opponents for power" and called the unity effort **"cium tapak kaki" (kissing feet)**.
- Akmal fires back: "By AMK's logic, their cooperation with DAP means they're 'kissing DAP's feet' too."
- Also references AMK's dismissal of **Afifi Aris** (UMNO Kapar Youth chief) who claimed BN-PAS cooperation could help UMNO recapture Kapar.
- Akmal: "Menggelupur sangat bila kita nak bersatu" (squirming too much when we try to unite).
- **Related analysis:** "Jangan baru dicuit sedikit, sudah menggelupur dan melenting" (Sinar, 17:07 MYT, by Norhaspida Yatim) — commentary arguing excessive reactions show some leaders' inability to handle differences maturely. (URL returned 404; captured via sidebar reference only.)
- **PIR-06/16 Significance:** UMNO Youth vs PKR Youth exchange ESCALATES. AMK's "cium tapak kaki" = a NEW PIR-16 narrative volley (ridiculing Malay unity/penyatuan undi Melayu). Akmal's counter = "you're kissing DAP's feet" — reverses the frame. Connects to PIR-16 "penyatuan undi Melayu" and "makmal politik" threads.

### 4. Aminuddin: campaign with integrity, condemns vandalism [FRESH 17:05 MYT EN / 18:18 MYT BM]
→ `priority_PIR-07_MalayMail_aminuddin-urges-integrity-in-negeri-sembilan-polls-condemns-vandalism-of-campaig_20260720_night_home.md` (EN, 17:05 MYT)
→ `priority_PIR-06-PIR-07_HarianMetro_prn-n9-kempenlah-secara-beradab-matang-aminuddin_20260720_night_rss.md` (BM, 18:18 MYT)
- Aminuddin calls on ALL parties to campaign with integrity, obey election laws. Vandalism = "no place in mature democracy."
- **Vandalism incidents (Day 2 of campaign):** flags BURNED in **Palong (N.31)**; flagpoles DAMAGED in **Chembong (N.27)**.
- **NS Police Chief Datuk Alzafny Ahmad** confirms: report received on Jempol (Palong) vandalism; Chembong investigation ONGOING.
- EN version (Bernama): DUN dissolved June 5, early voting July 28, polling August 1.
- BM version adds: Aminuddin also addresses Chuah candidacy issue (resolved before nomination day, "tidak sepatutnya dijadikan isu").
- **PIR-07 Significance:** Continuation of PIR-07 vandalism/sabotage thread from dusk cycle. Confirms Chembong (N.27) investigation still open. Palong (N.31) = same seat where derhaka counter-narrative emerged (dusk cycle). Both = Tier-4 seats.

### 5. Chuah NO internal split — Aminuddin + Kenny Chiew joint presser [FRESH 17:00 MYT, NEW]
→ `priority_PIR-07_Utusan_tiada-perpecahan-dalaman-di-dun-chuah_20260720_night_home.md`
- **Aminuddin Harun** + **Yew Boon Lye** (PH Chuah incumbent candidate) + **Kenny Chiew** (PKR Port Dickson deputy chief) joint press conference at Port Dickson.
- Chuah candidacy issue **RESOLVED before nomination day** — Kenny was passed over despite "giving service and working hard." Social media tried to frame it as a split.
- Kenny gives **full support** to PH candidates in Chuah, Lukut, Sri Tanjung, Bagan Pinang, Linggi.
- Aminuddin: "Bukan perpecahan tetapi dimainkan isu ini di media sosial." Thanks Kenny for clarifying to machinery.
- Kenny: accepts decision, "party interest > personal interest."
- **PIR-07 Significance:** Resolves the Chuah (N.33) internal tension narrative. Five PD-area DUN seats (Chuah, Lukut, Sri Tanjung, Bagan Pinang, Linggi) = PH's PD bastion. Unified front presented.

### 6. BN won't waste campaign time attacking — Jalaluddin at Kampung Jerang [FRESH 17:56 MYT, NEW]
→ `priority_PIR-06-PIR-07_Utusan_bn-tidak-akan-bazir-masa-kempen-untuk-serang-mana-mana-pihak_20260720_night_home.md`
- **Jalaluddin Alias** (NS UMNO chairman, BN Pertang candidate) at walkabout in Kampung Jerang, Jelebu.
- BN won't waste short campaign time attacking: "Gunakan masa berkempen sebaiknya, jangan sia-siakan 20 atau 30 minit hanya untuk mencaci."
- Will respond if continuously insulted but won't degrade opponents.
- **KEY SIGNAL:** "Calon-calon BN juga tidak menyentuh perkara berkaitan Kerajaan Perpaduan dalam kempen kerana masing-masing memahami perkara yang wajar dan tidak wajar untuk dibangkitkan" — **BN candidates deliberately AVOID Unity Government criticism in NS campaign.**
- **PIR-06/07 Significance:** PIR-06 signal — BN's careful navigation of federal-state tension. BN is in coalition with PH federally but opposing PH in NS — the "don't mention Unity Government" directive reflects internal discipline to avoid alienating federal partners while campaigning against them locally. PIR-07 — Jalaluddin walkabout in Jelebu (near Pertang DUN).

### 7. 13,263 postal ballots issued — electoral operational data [FRESH 17:26 MYT, NEW]
→ `priority_PIR-06-PIR-07_Utusan_prn-n-sembilan-13-263-kertas-undi-pos-dikeluarkan-hari-ini_20260720_night_home.md`
- **EC Secretary Datuk Khairul Shahril Idrus** confirms 13,263 postal ballots issued today (20 Jul).
- Breakdown: 12,669 Cat-1A (election workers, SPR, police, military, media); 343 Cat-1B (Malaysians abroad); 251 Cat-1C (11 security/health agencies).
- Process witnessed by candidate reps from all parties.
- Postal voters reminded: mark ballot, fill Form 2, return before 5pm polling day (Aug 1). Don't photograph/share ballot on social media.
- **PIR-07 Significance:** Electoral operational baseline. 13,263 postal ballots = ~1.1% of total electorate. Early voting July 28, polling Aug 1.

### 8. Anwar defends KWAP/eFishery — federal context [NEW to collection, 11:12-17:04 MYT]
→ `priority_PIR-07_MalayMail_anwar-defends-kwap-over-efishery-loss-says-rm12-9b-profit-puts-setback-in-perspe_20260720_night_home.md`
- **Anwar Ibrahim** (PM + Finance Minister) defends KWAP's RM163.4m eFishery investment in Dewan Negara.
- Investment went through rigorous process, no political interference. Individual decisions made independently by professionals.
- KWAP not alone — Temasek, SoftBank, Sequoia, Aqua-Spark, 42XFund, Northstar also invested.
- RM160m loss should be viewed against KWAP's **RM12.9b net profit in 2024**, RM15.8b fund size increase, 9.3% annual growth.
- Supports MACC investigation: "If there are elements of wrongdoing, the MACC must investigate."
- Draws parallel to 1MDB: "Even world-renowned auditors approve something, it is no guarantee of success."
- eFishery ex-CEO Gibran Huzaifah sentenced to 9 years (Bandung District Court, April 29) for embezzlement + money laundering.
- **PIR-16 Significance:** This is the FEDERAL-LEVEL response to MCA's Chan Quin Er PAC probe call (dusk cycle). MCA's accountability-voice positioning now has a direct Anwar rebuttal. KWAP/eFishery narrative thread connects federal fiscal governance to NS campaign discourse. Pre-cutoff (11:12 MYT) but new to collection — provides the Anwar-side context for the ongoing KWAP exchange.

## PIR Status Assessment

### PIR-06 — Coalition Operational Arrangement [CRITICAL — NOT CROSSED, 25th cycle]
- **No formal PN-MT expulsion notice, Bersatu candidate withdrawal, Kiandee quorum escalation, or "lebih hebat new coalition" formalization detected.**
- NEW: Bersatu's own candidate (Sanjeevan, Jeram Padang) rejects "Bersatu will be buried" narrative — defensive posture, not exit signal.
- NEW: BN candidates deliberately AVOID Unity Government criticism in campaign (Jalaluddin directive) — reflects BN's careful federal-state coalition management.
- NEW: Akmal vs AMK "cium tapak kaki" exchange = UMNO-PKR Youth tension over Malay unity, but not a coalition fracture signal.
- Maintain [CRITICAL] watch.

### PIR-16 — First Dominant Campaign Narratives [NOT CRITICAL, 25th cycle]
- **No hard-news outlet has explicitly published "Bersatu exit imminent?" or "Bersatu sasar bentuk kerajaan negeri" as a headline.** Threshold NOT crossed.
- NEW narrative volleys:
  - (a) Sanjeevan's "Bersatu won't be buried" rebuttal of Khaled's "kacau daun" — Bersatu's survival defense.
  - (b) Akmal's "menggelupur sangat" + "cium tapak kaki" reversal — UMNO Youth vs PKR Youth escalation over penyatuan undi Melayu.
  - (c) "Jangan baru dicuit sedikit, sudah menggelupur dan melenting" — Sinar analysis (17:07 MYT) framing excessive reactions as immaturity.
  - (d) Anwar's KWAP defense — federal response to MCA's PAC probe call. The KWAP/eFishery thread continues as a MCA accountability-voice vs Anwar governance thread.

### PIR-07 — Highest-Priority Battlegrounds
- **PH Manifesto launch TONIGHT** — confirmed by Aminuddin, Amirudin Shari to officiate. Pre-launch preview captured (18:05 MYT). Actual launch coverage = next collection target.
- **Palong (N.31):** flags burned (vandalism confirmed by police chief). Same seat as derhaka counter-narrative (dusk).
- **Chembong (N.27):** flagpoles damaged, investigation ONGOING.
- **Chuah (N.33):** internal split narrative RESOLVED — Aminuddin + Kenny Chiew joint presser.
- **Pertang (N.28):** Jalaluddin walkabout at Kampung Jerang, Jelebu — "BN won't waste time attacking" + avoid Unity Govt criticism.
- **Linggi (N.32):** Aminuddin campaigning — manifesto preview + integrity call delivered here.

## ⚠️ COLLECTION LIMITATIONS (night cycle)

- **gnews freshness:** 88 queries → 754 items, 448 PRN/priority hits, **1 fresh** post-cutoff. gnews continues to surface mostly historical matches.
- **RSS feeds:** Awani 10 (9 PRN, 0 fresh), FMT 50 (42 PRN, several fresh), HarianMetro 51 (36 PRN, several fresh). NST/MalayMail/Sinar/Utusan/BH RSS = 0 (JS/403).
- **Homepage extraction:** 10 articles saved (Utusan 3, Sinar 3, MalayMail 3, NST 1). Star/Kosmo/BH/mStar = 0 PRN links.
- **Sinar ID scan (788720-788800):** 0 PRN hits — range exhausted. Fresh Sinar content (788655, 788659) was recovered via homepage/sidebar, not ID scan.
- **Sinar "jangan dicuit" article (788659):** URL returned 404; captured via sidebar reference only (title + description: "Reaksi politik yang berlebihan menunjukkan ketidaksediaan segelintir kepimpinan dalam menguruskan perbezaan pandangan secara matang").
- **False positives (~20):** World Cup (Parades, Paredes), crime (rape, Durian Tunggal shooting inquest), federal non-PRN (KWAP/eFishery is PRN-adjacent via MCA thread but article itself is federal), elephant transfer DAK (MCW/SPRM — NOT PRN), foreign news (China, Morocco, Mexico, Thames Water, Ryanair, Mideast, Kremlin).
- **Utusan sidebar technique:** Recovered "BN tidak akan bazir masa" (Jalaluddin, 17:56 MYT) by following sidebar link from the postal-ballots article — proven high-yield again.

---

## 📈 CYCLE DELTA: dusk → night (16:37 → 18:26 MYT 20 Jul, ~1h49m)

- **Articles saved:** 48 (30 RSS + 7 URL-extract + 10 homepage + 1 manual Utusan sidebar)
- **Genuinely-fresh post-cutoff (≥16:37 MYT):** **9** (PH manifesto preview 18:05, Sanjeevan rebuttal 17:49, Akmal AMK rebuttal 18:14, Aminuddin adab BM 18:18, Aminuddin integrity EN 17:05, Chuah no split 17:00, postal ballots 17:26, BN bazir masa 17:56, jangan dicuit analysis 17:07)
- **New to collection (pre-cutoff):** 1 (Anwar KWAP defense 11:12-17:04 MYT — federal context)
- **PIR-06 status:** [CRITICAL] MAINTAINED (25th cycle). No threshold crossing. NEW: Sanjeevan's "Bersatu won't be buried" rebuttal + BN avoids Unity Govt criticism directive.
- **PIR-16 status:** NOT [CRITICAL]. 4 new narrative volleys — Sanjeevan "kacau daun" rebuttal, Akmal "menggelupur/cium tapak kaki," "jangan dicuit" analysis, Anwar KWAP defense vs MCA PAC call.
- **PIR-07 status:** PH MANIFESTO PREVIEW captured (pre-launch). Actual launch tonight = next target. Palong/Chembong vandalism confirmed. Chuah split resolved. Pertang Jalaluddin walkabout.
- **Key narrative contestation this cycle:** Bersatu's survival defense (Sanjeevan "won't be buried") vs Umno's "kacau daun" dismissal (Khaled). Plus UMNO Youth vs PKR Youth "cium tapak kaki" escalation (Akmal vs AMK) over Malay unity.

---

## 🎯 NEXT-CYCLE RECOMMENDATIONS (19:00–23:00 MYT window → PH MANIFESTO LAUNCH COVERAGE)

1. **PIR-07 (HIGHEST PRIORITY):** **PH MANIFESTO LAUNCH COVERAGE** — the actual launch event is tonight ~19:00-20:00 MYT. Capture ALL coverage when published: full manifesto pledges/content, Amirudin Shari's speech, B40→M50 details, specific initiatives, MB-after-PRN framing. Re-poll Awani/FMT/HarianMetro/NST/Sinar RSS + homepages for post-19:00 content.
2. **PIR-07 (continued):** Monitor vandalism/sabotage follow-up — Palong (N.31) + Chembong (N.27) investigations. Monitor election-death hit-and-run (Rantau area, from lateafternoon). BN manifesto 24 Jul at DUN Linggi — monitor advance coverage.
3. **PIR-06 ([CRITICAL] watch):** 25th cycle with no threshold crossing. Maintain formal-removal watch. Monitor BN's "avoid Unity Govt criticism" directive — does it hold or crack? Monitor Sanjeevan's "Bersatu won't be buried" narrative pickup — does it signal Bersatu digging in or preparing exit?
4. **PIR-16:** Track whether "Bersatu exit imminent?" or "Bersatu sasar bentuk kerajaan negeri" appears as a hard-news headline → if yes = [CRITICAL]. Track Akmal-AMK "cium tapak kaki" escalation. Track KWAP/eFishery: does Anwar's defense escalate or defuse the MCA PAC probe call?
5. **Source maintenance:** Utusan sidebar-link following = proven (recovered BN bazir masa). Re-poll FMT/Awani/HarianMetro RSS for post-18:26 fresh content. Sinar homepage extraction working (788655 Akmal piece). gnews freshness = 1 hit — low yield but still produces some.

---

*Night cycle index appended 2026-07-20 ~18:26 MYT (10:28 UTC) by PRN Negeri Sembilan 2026 News Collection Agent — Nomination-Day Surge Mode. TLP:AMBER. 48 articles saved (30 RSS + 7 URL-extract + 10 homepage + 1 manual). [CRITICAL] NOT crossed (25th cycle). Key night developments: (1) PH MANIFESTO PREVIEW — Aminuddin confirms launch tonight, Amirudin Shari to officiate, continuity of Unity Govt work, all-layers coverage; (2) SANJEEVAN REBUTS KHALED — Bersatu Jeram Padang candidate calls Khaled "angkuh," Johor≠NS, "Bersatu won't be buried" regardless of PN internal conflicts; (3) AKMAL REBUTS AMK — "menggelupur sangat bila kita nak bersatu," reverses "cium tapak kaki" frame onto AMK-DAP cooperation; (4) AMINUDDIN INTEGRITY/VANDALISM — flags burned Palong (N.31), flagpoles damaged Chembong (N.27), police investigation ongoing; (5) CHUAH NO SPLIT — Aminuddin + Kenny Chiew + Yew Boon Lye joint presser, issue resolved before nomination day; (6) BN WON'T WASTE TIME ATTACKING — Jalaluddin at Kampung Jerang, BN candidates deliberately avoid Unity Govt criticism; (7) 13,263 POSTAL BALLOTS issued — EC operational data; (8) ANWAR DEFENDS KWAP/eFishery — RM163.4m loss vs RM12.9b profit, supports MACC probe, federal response to MCA's PAC call. PH manifesto launch tonight — next major collection window.*

---

# 🌃 LATENIGHT CYCLE — 20260720_latenight (collected 19:36 MYT / 11:36 UTC, 20 Jul 2026)

**Cycle window:** 18:26 → 19:36 MYT 20 Jul 2026 (~1h10m since night cycle)
**Script:** manual collection (HarianMetro RSS + Utusan homepage + Buletin TV3 gnews + gnews scan)
**Cutoff:** post-10:28 UTC 20 Jul (post-18:26 MYT 20 Jul) = prior night cycle end

## Collection Metrics

|| Metric | Value |
||---|---|
|| RSS feeds polled | 4 (FMT, FMT_BM, Awani, HarianMetro) |
|| RSS PRN hits | 11 (HarianMetro 6, FMT_BM 9, Awani 0, FMT 2) |
|| RSS fresh post-cutoff | 3 (HarianMetro: Jalaluddin 18:58, Asyraf Wajdi 18:41; FMT_BM: 2 non-PRN) |
|| Homepage extracted | 5 (Utusan 3 commentary/nasional, Sinar 0, MalayMail 403, NST 0, Awani 2 non-fresh) |
|| gnews queries | 29 (14 targeted + 5 quick-scan + 10 manifesto-specific) |
|| gnews fresh post-cutoff | 0 (PH manifesto launch coverage NOT yet published) |
|| **Total articles saved** | **5** |
| [CRITICAL] auto-flagged | 0 |
| False positives | ~5 (World Cup, weather, Starmer PM resignation, Saudi visa, India police) |

## Key New Articles (genuinely fresh post-18:26 MYT or new to collection)

### 1. ASYRAF WAJDI: UMNO won't 'menebuk atap' Unity Government [FRESH 18:41 MYT, HIGHEST PRIORITY] ⭐
→ `priority_PIR-06-PIR-07_HarianMetro_umno-tidak-menebuk-atap-kerajaan-perpaduan-asyraf-wajdi_20260720_latenight_rss.md`
→ Buletin TV3 version: "BN tidak akan sesekali 'tebuk atap', kekal dukung Perjanjian Kerajaan Perpaduan" (18:14 MYT, gnews)
- **UMNO Secretary-General Datuk Dr Asyraf Wajdi Dusuki** gives explicit assurance UMNO will NOT undermine the Unity Government until it's dissolved for the next GE.
- **COOPERATION-STABILIZING signal.** Directly addresses the BN-PN cooperation vs Unity Government tension. References the formal "Perjanjian Kerajaan Perpaduan" (Unity Government Agreement).
- **Significance:** Strongest formal UMNO statement on federal coalition stability during NS campaign. Pairs with Jalaluddin's "BN candidates avoid Unity Govt criticism" directive (night cycle) — message discipline from top (SG) to ground (candidates). REDUCES PIR-06 [CRITICAL] risk.

### 2. JALALUDDIN denies vote-buying — "button badge, not money" [FRESH 18:58 MYT, NEW] ⭐
→ `priority_PIR-07_HarianMetro_prn-n9-button-badge-jalaluddin-nafi-beri-wang_20260720_latenight_rss.md`
- **Jalaluddin Alias** (BN Pertang N.28 candidate) denies giving money to voters during walkabout at Kampung Bemban, Jelebu. Says items were "button badges" not cash.
- **Significance:** FIRST explicit vote-buying allegation/rebuttal of the campaign. At Pertang (N.28) Tier-4 seat. Same candidate who said "BN won't waste time attacking" (night cycle) + "avoid Unity Govt criticism" directive. Active ground campaign in Jelebu/Pertang area.

### 3. Royal institution insult — man arrested [FRESH 19:16 MYT, PRN-ADJACENT]
→ `PIR-07_Utusan_lelaki-ditahan-hina-institusi-diraja-negeri-sembilan_20260720_latenight_home.md`
- **52-year-old Malay man** arrested for uploading offensive content about NS royal institution (Undang Yang Empat) on social media. Uploaded 17 Jul (nomination day), arrested 20 Jul at IPD Seremban.
- **NS Police Chief Datuk Alzafny Ahmad** confirms. Charges: Sedition Act S4, Penal Code S505, CMA S233.
- **Significance:** Connects to "derhaka" narrative — BN Palong candidate defined "derhaka = menentang raja, menentang Undang Yang Empat" (dusk cycle). This arrest is about someone doing exactly that. Same police chief handling Palong/Chembong vandalism investigations.

### 4. Utusan Commentary: "Gelanggang PRN NS mula dibuka" [NEW to collection]
→ `priority_PIR-07-PIR-16_Utusan_commentary-gelanggang-prn-negeri-sembilan-mula-dibuka_20260720_latenight_home.md`
- Campaign arena opens. 889,490 voters, 36 DUN seats. PRN held almost exactly 3 years after last (12 Aug 2023).
- **Key framing:** Unlike Johor and Melaka, NS begins with NO coalition able to claim advantage in forming government. "Open contest" framing.

### 5. Utusan Commentary: "Bolehkah status quo dipertahankan?" [NEW to collection]
→ `priority_PIR-07-PIR-16_Utusan_commentary-prn-n-sembilan-status-quo-dipertahankan_20260720_latenight_home.md`
- Can PH maintain the status quo? NS ≠ Johor — different political maps. NS characterized as stable, moderate, performance-oriented electorate.
- Aminuddin Harun's administrative track record "cannot be denied" — PH's incumbent advantage acknowledged.
- **PIR-16 significance:** Frames the central narrative contestation: PH's "prestasi pentadbiran" (performance) vs BN-PN's "penyatuan undi Melayu" (Malay unity). Pushes back on "Johor spillover" assumption.

## PIR Status Assessment

### PIR-06 — Coalition Operational Arrangement [CRITICAL — NOT CROSSED, 26th cycle]
- **No formal PN-MT expulsion notice, Bersatu candidate withdrawal, Kiandee quorum escalation, or "lebih hebat new coalition" formalization detected.**
- **NEW: Asyraf Wajdi's "menebuk atap" assurance** = COOPERATION-STABILIZING signal. UMNO SG formally commits to Unity Government stability. This is the STRONGEST counter-signal to PIR-06 [CRITICAL] risk to date — it directly addresses the federal-state tension.
- **Cross-cycle pattern:** Asyraf Wajdi (SG, formal) + Jalaluddin (ground, directive) = consistent message discipline: BN-PN cooperation at state level ≠ federal destabilization. BN is carefully managing the dual-track position.
- **MalaysiaGazette "Bersatu sasar bentuk kerajaan negeri" article:** Confirmed as already tracked (ESC-022, ACTIVE/CRITICAL since 19 Jul 17:25 cycle). Muhyiddin's 24-seat governing bid = ambition statement, NOT hard-news corroboration of formalized coalition split. 24 seats requires winning ALL 24 to form government (exceeds 19-seat majority but would need near-sweep). Maintained as pre-[CRITICAL] signal.
- Maintain [CRITICAL] watch.

### PIR-16 — First Dominant Campaign Narratives [NOT CRITICAL, 26th cycle]
- **No hard-news outlet has explicitly published "Bersatu exit imminent?" or "Bersatu sasar bentuk kerajaan negeri" as a headline reporting a FORMALIZED event (vs reporting Muhyiddin's ambition statement).** Threshold NOT crossed.
- **NEW this cycle:**
  - (a) Utusan commentary "Bolehkah status quo dipertahankan?" — frames the central question of the PRN. NS's moderate/performance electorate vs Johor spillover assumption.
  - (b) Utusan commentary "Gelanggang PRN mula dibuka" — "no coalition advantage" framing.
  - (c) Vote-buying narrative emerging (Jalaluddin rebuttal) — first election-offense thread.
  - (d) Royal institution insult arrest — "derhaka" narrative's real-world manifestation.

### PIR-07 — Highest-Priority Battlegrounds
- **PH Manifesto Launch:** Event expected ~19:00-20:00 MYT tonight. Pre-launch preview captured (night cycle, 18:05 MYT). Actual launch coverage NOT YET available in RSS/gnews as of 19:36 MYT — event likely ongoing. **NEXT CYCLE PRIORITY.**
- **N.28 Pertang:** Jalaluddin active — vote-buying rebuttal (18:58 MYT, Kampung Bemban) + "avoid Unity Govt criticism" directive (night cycle, Kampung Jerang). Two walkabouts in Jelebu area in ~2 hours = intensive ground campaign.
- **Royal institution arrest:** 52yo man arrested for insulting NS Undang Yang Empat. Connects to "derhaka" narrative at Palong (N.31). Same police chief (Alzafny) handling all PRN-related incidents.

## ⚠️ COLLECTION LIMITATIONS (latenight cycle)

- **gnews freshness:** 29 queries → 0 fresh post-cutoff hits. PH manifesto launch coverage not yet indexed by gnews (event still ongoing).
- **RSS feeds:** HarianMetro = sole source of fresh PRN content (2 fresh articles: Jalaluddin 18:58, Asyraf Wajdi 18:41). FMT/FMT_BM = 0 fresh PRN. Awani = 0 PRN. NST/MalayMail/Sinar/Utusan/BH RSS = 0 (JS/403).
- **Homepage extraction:** Utusan = 3 articles (2 commentary + 1 nasional). Sinar = 0 PRN links. MalayMail = 403. NST = 0. Awani = 2 (non-fresh).
- **PH manifesto launch:** Event confirmed for tonight ~19:00-20:00 MYT (Aminuddin, night cycle). Coverage expected within 1-2 hours. NOT available at collection time (19:36 MYT).
- **Article body extraction:** HarianMetro articles JS-rendered (0 body chars from page fetch); RSS description (intro paragraph) used as primary content. Utusan articles partially extracted via `<p>` tag parsing (enough for commentary analysis).
- **False positives (~5):** World Cup (Madrid, Spain), weather warning (7 states), Starmer PM resignation (UK), Saudi umrah visa, India police gas.

---

## 📈 CYCLE DELTA: night → latenight (18:26 → 19:36 MYT 20 Jul, ~1h10m)

- **Articles saved:** 5 (2 HarianMetro RSS + 2 Utusan homepage commentary + 1 Utusan homepage nasional)
- **Genuinely-fresh post-cutoff (≥18:26 MYT):** **3** (Asyraf Wajdi 18:41, Jalaluddin 18:58, hina diraja 19:16)
- **New to collection (pre-cutoff):** 2 (Utusan commentary pieces — dates uncertain, new to collection)
- **PIR-06 status:** [CRITICAL] MAINTAINED (26th cycle). NEW: Asyraf Wajdi's "menebuk atap" assurance = COOPERATION-STABILIZING signal (strongest counter to [CRITICAL] risk). BN message discipline confirmed (SG + ground candidates aligned).
- **PIR-16 status:** NOT [CRITICAL]. 2 Utusan commentary pieces framing the central "status quo" question + vote-buying narrative emerging.
- **PIR-07 status:** PH MANIFESTO LAUNCH still pending (event ongoing, coverage expected next cycle). Pertang (N.28) = active ground campaign (Jalaluddin 2 walkabouts). Royal institution arrest (derhaka connection).
- **Key narrative contestation this cycle:** Asyraf Wajdi's "won't undermine Unity Govt" vs the BN-PN cooperation tension. Utusan's "can status quo be maintained?" frames the entire PRN as a referendum on PH's performance vs BN-PN's Malay unity pitch.

---

## 🎯 NEXT-CYCLE RECOMMENDATIONS (20:00–23:00 MYT window → PH MANIFESTO LAUNCH COVERAGE)

1. **PIR-07 (HIGHEST PRIORITY):** **PH MANIFESTO LAUNCH COVERAGE** — event expected to complete ~20:00 MYT. Capture ALL coverage when published: full manifesto pledges, Amirudin Shari's speech, B40→M50 expansion details, specific initiatives, MB-after-PRN framing, PH's 36-seat strategy. Re-poll Awani/FMT/HarianMetro/NST/Sinar RSS + homepages for post-20:00 content. gnews should index within 30-60 min of publication.
2. **PIR-07 (continued):** Monitor Jalaluddin vote-buying allegation follow-up — does the accuser go public? Does SPRM/EC respond? Track Pertang (N.28) ground campaign. Monitor royal institution arrest follow-up (remand hearing tomorrow). BN manifesto 24 Jul at DUN Linggi + Pertang.
3. **PIR-06 ([CRITICAL] watch):** 26th cycle with no threshold crossing. Asyraf Wajdi's "menebuk atap" assurance = stabilizing. Monitor whether it holds or if BN-PN cooperation triggers further intra-Unity-Govt friction. Maintain formal-removal watch.
4. **PIR-16:** Track Utusan commentary pickup — does "Bolehkah status quo dipertahankan?" framing spread to other outlets? Track vote-buying narrative escalation. Track "derhaka" narrative evolution (royal institution arrest = real-world manifestation).
5. **Source maintenance:** HarianMetro RSS = most reliable fresh PRN source this cycle. Utusan homepage = good for commentary (JS-rendered but `<p>` extraction works). Re-poll all feeds post-20:00 MYT for manifesto coverage.

---

*Latentight cycle index appended 2026-07-20 ~19:36 MYT (11:36 UTC) by PRN Negeri Sembilan 2026 News Collection Agent — Nomination-Day Surge Mode. TLP:AMBER. 5 articles saved (2 HarianMetro RSS + 2 Utusan homepage commentary + 1 Utusan homepage nasional). [CRITICAL] NOT crossed (26th cycle). Key latenight developments: (1) ASYRAF WAJDI "menebuk atap" assurance — UMNO SG formally commits to Unity Govt stability, references Perjanjian Kerajaan Perpaduan, COOPERATION-STABILIZING signal (strongest counter to PIR-06 [CRITICAL] risk); (2) JALALUDDIN vote-buying rebuttal — "button badge, not money" at Kampung Bemban, Jelebu (Pertang N.28), first election-offense allegation/rebuttal of campaign; (3) Royal institution insult arrest — 52yo man arrested for insulting NS Undang Yang Empat, uploaded 17 Jul (nomination day), connects to "derhaka" narrative; (4) Utusan commentary "Gelanggang PRN mula dibuka" — 889,490 voters, no coalition advantage, open contest; (5) Utusan commentary "Bolehkah status quo dipertahankan?" — NS ≠ Johor, moderate/performance electorate, Aminuddin track record acknowledged. PH manifesto launch event still ongoing — coverage expected next cycle (20:00+ MYT).*

---

# 📋 POSTMANIFESTO CYCLE — 20260720_postmanifesto (collected 20:46 MYT / 12:46 UTC, 20 Jul 2026)

**Cycle window:** 19:36 → 20:46 MYT 20 Jul 2026 (~1h10m since latenight cycle)
**Script:** `_surge_fetch_20260720_postmanifesto.py` (100 gnews queries, 10 RSS feeds, 17 homepage pages, Sinar ID scan 788800-788880)
**Cutoff:** post-11:36 UTC 20 Jul (post-19:36 MYT 20 Jul) = prior latenight cycle end
**Purpose:** Capture PH Manifesto Launch coverage (event completed ~20:00 MYT) + continuation of PIR-06 [CRITICAL] watch + Jalaluddin vote-buying denial cross-outlet corroboration + royal arrest cross-outlet

## Collection Metrics

|| Metric | Value ||
||---|---|
|| gnews queries | 100 (incl. 12 mandatory PIR-06 [CRITICAL]-watch + 12 manifesto-specific + 15 evening-ceramah/battleground) |
|| gnews items returned | 748 |
|| gnews PRN/priority hits | 436 |
|| gnews **fresh** post-cutoff (≥19:36 MYT) | **2** (Jalaluddin cash denial EN 19:38 MYT, royal arrest EN 20:10 MYT — both FMT) |
|| RSS feed items scanned | **859** (Awani 10 + FMT 50 + HarianMetro 51; NST/MalayMail/Sinar/Utusan/BH RSS = 0) |
|| RSS PRN hits | 90 |
|| RSS full-text saved | 29 |
|| URL-extracted (gnews fresh) | 1 |
|| Homepage extracted | 8 |
|| Sinar ID scan (788800-788880) | 0 PRN hits — range exhausted |
|| **Total articles saved (raw)** | **38** |
|| False positives deleted | **27** (World Cup ×3, international news ×6, crime/drugs ×5, federal non-PRN ×5, elephant-DAK ×1, influencer event ×1, homeless ×1, fitness ×1, non-NS deaths ×4) |
|| **Total articles saved (cleaned)** | **11** |
|| Duplicates skipped | 54 |
|| [CRITICAL] auto-flagged | **0** (27th cycle — confirmed) |
|| Genuine [CRITICAL] threshold crossings | **0** |

---

## 🔑 KEY NEW ARTICLES (genuinely new to collection, analytically material)

### 1. ⭐⭐⭐ ANTHONONY LOKE: "I will abide by DAP congress decision on whether to stay in govt" — HIGHEST VALUE [FRESH 19:07 MYT EN / 19:29 MYT BM, NEW TO COLLECTION]
→ `priority_PIR-07-PIR-16_FMT_i-will-abide-by-dap-congress-decision-on-whether-to-stay-in-govt-says-loke_20260720_postmanifesto_rss.md` (EN)
→ `priority_PIR-07-PIR-16_FMT_saya-patuh-keputusan-kongres-dap-mengenai-kedudukan-dalam-kerajaan-kata-loke_20260720_postmanifesto_rss.md` (BM)
- **Anthony Loke** (DAP Sec-Gen, Transport Minister) in BFM 89.9 interview with Sharaad Kuttan: wants DAP to remain in federal government BUT will accept whatever 3,000-4,000 delegates decide at **DAP congress Aug 16** (secret ballot).
- **"I want to defend this government. I want to defend the party's role in the government. But I need the mandate of the members to continue this journey."**
- DAP members unhappy with the party's role in government must be prepared for DAP to **return to the backbench/opposition**: "In the government, our duty is to govern, deliver, and ensure that we can keep this country moving forward."
- **"Negeri Sembilan polls' outcome will influence delegates"** — Loke explicitly ties the NS PRN result to DAP's future in the Unity Government.
- Defended dissolving the NS assembly: PH controlled only 17 of 36 seats; "If we had waited for another couple of months, we would have been defeated during the budget vote."
- DAP's decision to work with BN after GE15 was collective by all MPs — to prevent PN from taking Putrajaya.
- **PIR-16/07 Significance:** MAJOR narrative development. Loke is the first Unity Government component leader to openly float DAP's potential return to opposition, explicitly linking it to the NS PRN outcome. This connects to: (a) AMH/Kamil Munim "resign to attack" calls (morning/dusk cycles); (b) Amanah Selangor's Abbas Azmi "api dalam sekam" warning + call for BN appointees to resign (dusk); (c) Fathi Aris "PH has no right to feel cheated" (lateafternoon); (d) the intra-unity-government friction thread. Loke positions the NS PRN as a **referendum on DAP's continued participation in the Unity Government** — escalating the stakes of the state election beyond state-level governance. Pre-cutoff (19:07/19:29 MYT, cutoff 19:36 MYT) but NEW to collection — FMT article not captured in latenight cycle (which focused on HarianMetro + Utusan).
- **NOT PIR-16 [CRITICAL]:** The [CRITICAL] threshold requires corroboration of "Bersatu exit imminent?" or "Bersatu sasar bentuk kerjaan negeri." This is about DAP's position, not Bersatu's. But it is the **highest-value PIR-16 narrative signal of the day** — a Unity Government component leader publicly conditioning continued participation on a state election outcome.

### 2. JALALUDDIN vote-buying denial — FMT EN+BM [FRESH 19:38 MYT EN / 20:00 MYT BM, CROSS-OUTLET]
→ `priority_PIR-06-PIR-07_FMT_jalaluddin-denies-handing-cash-to-voters-during-walkabout_20260720_postmanifesto_rss.md` (EN, 19:38 MYT)
→ `priority_PIR-06-PIR-07_FMT_jalaluddin-nafi-tuduhan-agih-wang-kepada-pengundi_20260720_postmanifesto_rss.md` (BM)
- **Jalaluddin Alias** (BN Pertang N.28 candidate) denies giving cash to voters during walkabout. Says items were button badges, not money.
- FMT version provides the English-language corroboration of the HarianMetro BM article captured in the latenight cycle (18:58 MYT).
- Genuinely FRESH post-cutoff (19:38 MYT EN > 19:36 MYT cutoff).
- **PIR-07 Significance:** Cross-outlet corroboration of the first vote-buying allegation/rebuttal of the campaign at Pertang (N.28) Tier-4 seat. FMT (hard news) now confirms the HarianMetro report. The allegation is gaining traction across outlets.

### 3. Royal institution insult arrest — FMT EN [FRESH 20:10 MYT, CROSS-OUTLET]
→ `priority_PIR-07_FMT_man-arrested-over-post-allegedly-insulting-negeri-sembilan-royalty_20260720_postmanifesto_rss.md`
- 52-year-old man arrested for social media post allegedly insulting NS royal institution (Undang Yang Empat).
- FMT English version of the Utusan BM article captured in latenight cycle (19:16 MYT).
- Genuinely FRESH post-cutoff (20:10 MYT).
- **PIR-07 Significance:** Cross-outlet corroboration. Connects to "derhaka" narrative — BN Palong candidate defined "derhaka = menentang raja, menentang Undang Yang Empat" (dusk cycle). Same police chief (Alzafny) handling all PRN-related incidents.

### 4. SANJEEVAN: Khaled's "spoiler" jab shows Umno's arrogance — FMT EN [18:21 MYT, CROSS-LANGUAGE]
→ `priority_PIR-06-PIR-07_FMT_khaled-s-spoiler-jab-shows-umno-s-arrogance-says-sanjeevan_20260720_postmanifesto_rss.md`
- English version of the FMT BM article captured in the night cycle (17:49 MYT "Sanjeevan bidas Khaled angkuh").
- Bersatu Jeram Padang candidate Sanjeevan: Khaled's "spoiler" label = Umno arrogance post-Johor. Johor ≠ NS. NS voters will "stop the blue wave." "Whatever happens to Bersatu within PN, it will not spell the end of the party."
- **PIR-06/16 Significance:** Cross-language version of the Bersatu survival-defense rebuttal. Same content, English delivery for broader audience.

### 5. EC dispatches 13,263 postal ballots — MalayMail EN + Sinar BM [CROSS-OUTLET CORROBORATION]
→ `priority_PIR-07_MalayMail_ec-dispatches-13-263-postal-ballots-for-negeri-sembilan-state-polls-malay-mail_20260720_postmanifesto_home.md` (EN)
→ `priority_PIR-06-PIR-07_Sinar_spr-keluar-13-263-kertas-undi-pos-bagi-prn-negeri-sembilan-sinar-harian_20260720_postmanifesto_home.md` (BM)
- EC Secretary Datuk Khairul Shahril Idrus confirms 13,263 postal ballots issued 20 Jul.
- Cross-outlet corroboration of the Utusan article captured in the night cycle (17:26 MYT). MalayMail (EN) + Sinar (BM) versions now captured.
- Breakdown: 12,669 Cat-1A (election workers/police/military/media), 343 Cat-1B (Malaysians abroad), 251 Cat-1C (security/health agencies).
- Early voting July 28, polling Aug 1.

### 6. Election-related death — Utusan version [CROSS-OUTLET]
→ `priority_PIR-07_Utusan_lelaki-maut-dilanggar-lari-ketika-pasang-bendera-parti_20260720_postmanifesto_home.md`
- Utusan version of the Sinar article captured in the lateafternoon cycle (man killed in hit-and-run while installing party flags near Rantau).
- Cross-outlet corroboration. 23-year-old man killed on Jalan Kuala Sawah-Rantau near Kampung Belangkan (Sunday 6:40pm).

### 7. Awani: Rumah Warisan Uwan Robah — NS cultural heritage [PRN-ADJACENT, NEW]
→ `priority_PIR-07-PIR-16_Awani_rumah-warisan-uwan-robah-ruwur-khazanah-yang-diselamatkan_20260720_postmanifesto.md`
- Heritage house restoration in **Kuala Pilah, Negeri Sembilan** — 100+ year old traditional NS house (Adat Perpatih architecture, no nails). Awani tags with **#prn Negeri Sembilan**.
- Mentions **Adat Perpatih** (NS's matrilineal customary system) — connects to PIR-16 "adat" keyword (Tok Mat's "adat politik" narrative).
- **PIR-07/16 Significance:** Soft PRN-adjacent content — cultural heritage framing of NS identity during election period. Awani explicitly tags it with #prn NS. Provides cultural context for the "adat" narrative thread.

### 8. Asyraf Wajdi "menebuk atap" — HarianMetro [DUPLICATE from latenight, cross-cycle confirmation]
→ `priority_PIR-06-PIR-07_HarianMetro_umno-beri-jaminan-tidak-akan-menebuk-atap-kerajaan-perpaduan-asyraf-wajdi_20260720_postmanifesto_rss.md`
- HarianMetro version of the Asyraf Wajdi Unity Government stability assurance captured in latenight cycle (18:41 MYT).
- True duplicate (same content, same URL source). Kept for cross-cycle confirmation but not a new story.

---

## 🔴 PIR-06 — COALITION OPERATIONAL ARRANGEMENT — [CRITICAL] NOT CROSSED (27th cycle)

**[CRITICAL] status: MAINTAINED. 27th cycle with no formal PN-MT expulsion notice, no Bersatu candidate withdrawal (24 solo Bersatu-logo candidates stable), no Kiandee/PN quorum escalation, no PN/Bersatu Supreme Council statement, no RoS intervention, no "lebih hebat new coalition" formalization. All 12 mandatory gnews [CRITICAL]-watch queries returned 0 fresh critical hits. gnews critical-keyword scan across 436 priority headlines = 0 hits.**

**No NEW PIR-06 intelligence this cycle.** The cross-cycle pattern holds:
- Asyraf Wajdi's "menebuk atap" assurance (latenight) = COOPERATION-STABILIZING signal (strongest counter to [CRITICAL] risk)
- BN message discipline confirmed (SG + ground candidates aligned)
- Bersatu candidates running under own logo (24 seats) = structural independence, NOT formal exit
- No Bersatu candidate withdrawals; no quorum escalation; no RoS action

**Tier-4 seat watch (N.04, N.05, N.13, N.14, N.23, N.25, N.31, N.34):** No new Tier-4 intel this cycle. Pertang (N.28, technically T1 but listed for derhaka/vote-buying watch) = active ground campaign (Jalaluddin vote-buying denial now cross-outlet corroborated by FMT).

---

## 🟠 PIR-07 — HIGHEST-PRIORITY BATTLEGROUNDS

### PH MANIFESTO LAUNCH — COVERAGE STILL PENDING ⏳
- **Event confirmed:** Aminuddin confirmed launch tonight (20 Jul evening), Amirudin Shari (Selangor MB, PH Presidential Council) to officiate (night cycle, 18:05 MYT).
- **Pre-launch preview captured:** HarianMetro 18:05 MYT (night cycle) — manifesto = "kesinambungan usaha Kerajaan Perpaduan," B40→M50 expansion, all-layers coverage.
- **Actual launch coverage NOT YET available:** As of 20:46 MYT collection time, no RSS/gnews article describing the launch event itself (Amirudin's speech, full pledge list, launch ceremony). The event likely completed ~20:00 MYT but coverage has not propagated to RSS feeds or Google News indexing yet (typically 30-60 min lag).
- **NEXT CYCLE: TOP PRIORITY.** Re-poll all feeds + gnews post-21:00 MYT for manifesto launch coverage.

### Battleground developments (cross-outlet corroboration):
- **N.28 Pertang (T1/derhaka-watch):** Jalaluddin vote-buying denial now cross-outlet (FMT EN+BM + HarianMetro BM). First election-offense allegation of campaign gaining multi-outlet traction.
- **Royal institution (NS-wide):** Arrest cross-outlet corroborated (FMT EN + Utusan BM). Same police chief Alzafny handling all PRN incidents (Palong vandalism, Chembong damage, Klawang investigation, royal insult).
- **EC operations:** 13,263 postal ballots — now 3-outlet corroborated (Utusan + MalayMail EN + Sinar BM). Early voting July 28, polling Aug 1.

---

## 🟡 PIR-16 — FIRST DOMINANT CAMPAIGN NARRATIVES — [CRITICAL] NOT CROSSED (27th cycle)

**PIR-16 [CRITICAL] threshold NOT CROSSED.** No hard-news outlet corroboration of "Bersatu exit imminent?" or "Bersatu sasar bentuk kerjaan negeri" as explicit headline. The structural evidence (Bersatu running under own logo in 24 seats, separate from PN/Wawasan) continues but no hard-news formalization headline.

### NEW PIR-16 intelligence this cycle — ANTHONY LOKE = HIGHEST-VALUE NARRATIVE SIGNAL:

**Loke's DAP-congress/Unity-Government statement (19:07/19:29 MYT):**
- First Unity Government component leader to openly condition DAP's continued participation on a state election outcome
- "Negeri Sembilan polls' outcome will influence delegates" — explicitly ties NS PRN to DAP congress (Aug 16) decision on whether DAP stays in federal government
- Floats DAP returning to "backbench" if members reject leadership's preferred position
- This ESCALATES the intra-unity-government friction narrative to a new level — it's no longer just AMK (PKR Youth) or Amanah Selangor making "resign to attack" calls; now it's DAP's own Sec-Gen openly discussing the possibility
- Connects to the full PIR-16 narrative chain: AMH/Kamil Munim "resign to attack" → Amanah Selangor "api dalam sekam" → Fathi Aris "PH has no right to feel cheated" → **Loke "I'll abide by congress decision"**
- The DAP congress on Aug 16 (15 days after NS polling day Aug 1) = the next institutional checkpoint. If NS PRN goes badly for PH, DAP delegates may vote to leave the Unity Government.
- **NOT [CRITICAL]:** Does not meet the "Bersatu exit imminent?" or "sasar bentuk kerajaan negeri" threshold. But it is a **pre-[CRITICAL] narrative escalation** — the first time a federal coalition partner has publicly linked a state election outcome to federal coalition continuity.

### PIR-16 narrative status summary (cumulative):
1. **"Bersatu kacau daun / disarray" narrative** — Khaled's "spoiler" label (night cycle) vs Sanjeevan's "Bersatu won't be buried" rebuttal (night cycle + this cycle EN). Structural evidence (own-logo candidates) but no hard-news "exit imminent" headline.
2. **"DAP acceptance / Unity Government stability" narrative** — Loke's DAP-congress statement (THIS CYCLE, highest value) + AMH "resign to attack" + Amanah Selangor "api dalam sekam" + Fathi Aris "PH has no right to feel cheated." Escalating.
3. **"Derhaka" narrative** — BN Palong candidate's "bukan derhaka" rebuttal (dusk) + royal institution arrest (latenight + this cycle cross-outlet). Real-world manifestation.
4. **"MCA accountability voice" narrative** — MCA Chan Quin Er's KWAP/eFishery PAC probe call (dusk) + Anwar's KWAP defense (night). Ongoing.
5. **"Penyatuan undi Melayu" narrative** — Akmal vs AMK "cium tapak kaki" exchange (night) + KJ "makmal politik PRU16" framing (dusk). Ongoing.
6. **"Status quo" narrative** — Utusan "Bolehkah status quo dipertahankan?" (latenight) — frames the PRN as a referendum on PH's performance vs BN-PN's Malay unity pitch.

---

## ⚠️ COLLECTION LIMITATIONS (postmanifesto cycle)

- **gnews freshness (27th cycle):** 100 queries → 748 items, 436 PRN/priority hits, **2 fresh** post-cutoff (Jalaluddin cash denial EN 19:38 MYT, royal arrest EN 20:10 MYT — both FMT). gnews continues to surface mostly historical matches.
- **RSS feeds:** FMT 50 (41 PRN/priority hits, several fresh), HarianMetro 51 (42 PRN/priority hits), Awani 10 (7 PRN/priority hits). NST/MalayMail/Sinar/Utusan/BH RSS = 0 (JS/403). Awani-Politik feed broken (rc=0, no items).
- **PH Manifesto Launch coverage:** NOT available in any RSS feed or gnews as of 20:46 MYT. Event completed ~20:00 MYT; coverage propagation lag = 30-60 min typical. NEXT CYCLE TOP PRIORITY.
- **Loke article (KEY FINDING):** Pre-cutoff (19:07/19:29 MYT, cutoff 19:36 MYT) but NEW to collection — FMT RSS item not polled in latenight cycle (which used HarianMetro + Utusan + manual gnews). Discovered via FMT RSS this cycle.
- **Homepage extraction:** 8 articles saved (MalayMail 1, Sinar 1, Utusan 5, Awani 1). Star/Kosmo/BH/mStar/HarianMetro homepage = 0 PRN links.
- **Sinar ID scan (788800-788880):** 0 PRN hits — range exhausted (no new articles in that ID window). Fresh Sinar content was recovered via homepage extraction.
- **False positives (27 deleted):** World Cup ×3 (Spain, Madrid, Yamal-Trump), international ×6 (UK PM Burnham, Thailand rail, AliExpress EU, Ukraine drone, HK Patrick Tse, Bahrain-Kuwait-Iran), crime/drugs ×5 (child neglect, Sabah drug smuggling, Sri Lanka cocaine, Selangor AADK, stabbing death), federal non-PRN ×5 (Ringgit, Sabah diesel, elephant-DAK MACC, influencer PIM event, homeless woman), non-NS deaths ×4 (trailer accident, motorcycle convoy, drunk driver, stabbing), fitness/leadership ×1, activist arrest ×1 (Tamim Dahri, KL). Many triggered on substring matches ("pn" in PNB/Spain/Palestine, "loke" in Burnham, "negeri" in non-NS context).
- **[CRITICAL] auto-flag:** 0 this cycle (27th cycle confirmed). No false positives. Detector performed cleanly.
- **HarianMetro RSS dedup issue:** Asyraf Wajdi "menebuk atap" article saved again (true duplicate from latenight cycle). Dedup by URL should have caught it but didn't — likely because the HarianMetro URL was not in the existing_urls set loaded from latenight cycle (latenight used manual collection, not the script's URL-tracking). Minor; no analytical impact.

---

## 📈 CYCLE DELTA: latenight → postmanifesto (19:36 → 20:46 MYT 20 Jul, ~1h10m)

- **Articles saved (cleaned):** 11 (29 RSS + 1 URL-extract + 8 homepage = 38 raw; 27 false positives deleted)
- **Genuinely-fresh post-cutoff (≥19:36 MYT):** **2** (Jalaluddin cash denial EN 19:38 MYT, royal arrest EN 20:10 MYT — both FMT EN versions of latenight's BM stories)
- **New to collection (pre-cutoff but not previously captured):** **1** (Loke DAP-congress article 19:07/19:29 MYT — HIGHEST VALUE)
- **Cross-outlet/cross-language corroboration:** **5** (Jalaluddin EN+BM, royal arrest EN, EC postal ballots EN+BM, Sanjeevan EN, election death Utusan)
- **PIR-06 status:** [CRITICAL] MAINTAINED (27th cycle). No new intel. No threshold crossing. Asyraf Wajdi stabilizing signal holds.
- **PIR-16 status:** NOT [CRITICAL]. **NEW HIGHEST-VALUE NARRATIVE SIGNAL: Loke's DAP-congress/Unity-Government statement** — first federal coalition partner to condition participation on a state election outcome. Pre-[CRITICAL] escalation.
- **PIR-07 status:** PH MANIFESTO LAUNCH COVERAGE STILL PENDING. Jalaluddin vote-buying denial + royal arrest cross-outlet corroborated. EC postal ballots 3-outlet confirmed.
- **Key narrative development this cycle:** Loke's "I will abide by DAP congress decision" — the NS PRN is now explicitly framed by a federal coalition partner as a referendum on federal coalition continuity. This is the most significant PIR-16 narrative escalation of the day.

---

## 🎯 NEXT-CYCLE RECOMMENDATIONS (21:00–23:00 MYT window → PH MANIFESTO LAUNCH COVERAGE)

1. **PIR-07 (HIGHEST PRIORITY):** **PH MANIFESTO LAUNCH COVERAGE** — event completed ~20:00 MYT. Coverage should now be propagating to RSS/gnews (30-60 min lag). Re-poll Awani/FMT/HarianMetro/NST/Sinar RSS + homepages for post-20:00 content. Look for: full manifesto pledges/content, Amirudin Shari's speech, B40→M50 expansion details, specific initiatives, MB-after-PRN framing, PH's 36-seat strategy. **This is the 3rd consecutive cycle flagging the manifesto launch as priority — coverage should finally be available.**
2. **PIR-16 (HIGH PRIORITY):** **Track Loke's DAP-congress statement pickup** — does any other outlet (NST, Star, Awani, Sinar) report Loke's "I will abide by DAP congress decision" interview? Does it trigger responses from AMK, Amanah, UMNO, or Bersatu? This is the most significant intra-unity-government friction signal to date. Monitor whether the "DAP may leave Unity Government" narrative spreads.
3. **PIR-07 (continued):** Monitor Jalaluddin vote-buying allegation follow-up — does the accuser go public? Does SPRM/EC respond? Track Pertang (N.28) ground campaign. Monitor royal institution arrest follow-up (remand hearing). BN manifesto 24 Jul at DUN Linggi + Pertang — monitor advance coverage.
4. **PIR-06 ([CRITICAL] watch):** 27th cycle with no threshold crossing. Asyraf Wajdi's "menebuk atap" assurance = stabilizing. Maintain formal-removal watch. Monitor whether Loke's DAP-congress statement triggers any PN/Bersatu response that could escalate the coalition-fracture narrative.
5. **Source maintenance:** FMT RSS = best source for fresh PRN content this cycle (2 fresh hits). HarianMetro RSS = steady (42 PRN/priority hits). Re-poll all feeds post-21:00 MYT for manifesto coverage. Sinar ID scan 788800-788880 exhausted — next range should be 788880+. gnews freshness = 2 hits (low but non-zero).

---

*Postmanifesto cycle index appended 2026-07-20 ~20:51 MYT (12:51 UTC) by PRN Negeri Sembilan 2026 News Collection Agent — Nomination-Day Surge Mode. TLP:AMBER. 38 raw articles saved → 27 false positives deleted → **11 PRN-relevant articles retained** (29 RSS + 1 URL-extract + 8 homepage; after cleanup: 6 FMT + 1 HarianMetro + 1 Awani + 1 Sinar + 1 MalayMail + 1 Utusan). [CRITICAL] NOT crossed (27th cycle; 0 auto-flags, 0 false positives). Key postmanifesto developments: (1) ⭐⭐⭐ ANTHONY LOKE — DAP Sec-Gen says he will abide by DAP congress (Aug 16) decision on whether DAP stays in Unity Government; explicitly ties NS PRN outcome to delegates' direction; first federal coalition partner to condition participation on a state election result; HIGHEST-VALUE PIR-16 narrative escalation of the day; (2) JALALUDDIN vote-buying denial — FMT EN+BM cross-outlet corroboration of latenight's HarianMetro BM report (19:38 MYT, genuinely fresh); (3) ROYAL ARREST — FMT EN version of latenight's Utusan BM report (20:10 MYT, genuinely fresh); (4) SANJEEVAN — FMT EN version of night cycle's BM "kacau daun" rebuttal; (5) EC 13,263 postal ballots — 3-outlet corroborated (Utusan + MalayMail + Sinar); (6) Awani NS heritage house (Kuala Pilah, Adat Perpatih, #prn NS tag) — PRN-adjacent cultural content. PH MANIFESTO LAUNCH COVERAGE STILL PENDING (event completed ~20:00 MYT, coverage not yet in RSS/gnews as of 20:46 MYT) — NEXT CYCLE TOP PRIORITY (3rd consecutive cycle flagging). PIR-06 [CRITICAL] maintained 27th cycle; Asyraf Wajdi stabilizing signal holds; no formal expulsion/withdrawal/quorum/RoS action.*

---

## 🔹 CYCLE 28 — NIGHT2 (20:46 → 22:00 MYT 20 Jul, ~1h14m)

**Generated:** 2026-07-20 22:00 MYT (14:00 UTC)
**Cycle:** 20260720_night2 (28th cycle, Campaign Day 2-3)
**Cutoff:** 20:46 MYT 20 Jul (prior postmanifesto cycle end)

### COLLECTION YIELD

| Source | Items | PRN/priority hits | Fresh post-cutoff | Saved | After cleanup |
|--------|-------|-------------------|-------------------|-------|---------------|
| Google News (132 queries) | 879 | 518 | **0** | 0 | 0 |
| RSS feeds (10) | 990 | 87 | **0** | 33 | 0 |
| Homepage extraction (19 pages) | — | — | — | 6 | 0 |
| Sinar ID scan (788880-788960) | 81 | 0 | 0 | 0 | 0 |
| **Targeted The Vibes search** | — | — | — | **2** | **2** |
| **TOTAL** | — | — | **0** | 41 | **2** |

### ARTICLES RETAINED (2 genuinely new — recovered via targeted The Vibes search, NOT in gnews/RSS/homepage)

1. ⭐⭐ **[PIR-07] TheVibes — "PH offers more comprehensive manifesto, benefits all groups"** (16:13 MYT 20 Jul, PRE-LAUNCH ANALYSIS)
   - URL: https://www.thevibes.com/articles/news/125248/ph-offers-more-comprehensive-manifesto-benefits-all-groups
   - Aminuddin Harun: manifesto to benefit all groups, not just B40 but also M40. "God willing, it will not only be for the B40 group, but we will also cater to the M50 [sic, means M40]." Many previous initiatives maintained ("kesinambungan" continuity theme). Manifesto launch scheduled "tonight" (20 Jul). Holistically detailed by coalition's top leadership for sustainable economic + social impact.
   - **Significance:** Pre-launch framing — confirms B40→M40 expansion narrative + "kesinambungan" (continuity) messaging as core manifesto themes. 4h before actual launch.

2. ⭐⭐ **[PIR-07] TheVibes — "PH banks on Negeri Sembilan development record as campaign heats up"** (18:03 MYT 20 Jul, CAMPAIGN NARRATIVE)
   - URL: https://www.thevibes.com/articles/news/125254/ph-banks-on-negeri-sembilans-development-record-as-campaign-heats-up
   - **Sri Tanjung (N.33) incumbent Datuk Dr Rajasekaran Gunnasekaran** campaigning on investment record: AI-powered Midport Pasir Panjang + Google RM1B data centre Port Dickson. "Under Tok Min's [Aminuddin] leadership, NS has secured record investments."
   - **Seri Menanti candidate Mohd Kamarul Arifin Mohd Wafa**: voters judging on performance not promises; STR/SARA federal aid resonating; local issues = housing repairs, drainage, infrastructure.
   - **Investment data:** approvals RM1.14B (2017) → RM54.3B (2025); revenue RM413M → RM610M; reserves RM725.96M → RM1.04B; unemployment 3.8% (2020) → 3.1% (2025).
   - **Aug 1 election date confirmed.** Campaign = economic growth + investment + welfare delivery vs election pledges.
   - **Significance:** First detailed PIR-07 campaign-ground intelligence for Sri Tanjung (N.33) + Seri Menanti seats. Quantified development-record narrative = PH's dominant campaign framing. New candidate names (Rajasekaran, Kamarul) added to entity inventory.

### ⚠️ KEY FINDING: PH MANIFESTO LAUNCH COVERAGE — 4th CONSECUTIVE CYCLE, STILL NOT FOUND

- **Event completed ~20:00 MYT 20 Jul.** Now 22:00 MYT — **2+ hours post-event.**
- **gnews "after:2026-07-20" targeted search: 0 items.** 132 standard queries → 879 items, 518 PRN hits, **0 fresh post-20:46 MYT.**
- **RSS feeds (Awani/FMT/HarianMetro/NST/MalayMail/Sinar/Utusan/BH): 0 manifesto titles.** Manual grep of Awani + HarianMetro RSS for "manifesto/kesinambungan/amirudin/aminuddin" = empty.
- **Homepage extraction (19 pages incl. Awani berita/politik): 0 manifesto content.**
- **Sinar ID scan 788880-788960: 0 PRN hits** (range exhausted, consecutive failure).
- **Assessment:** Coverage propagation lag now exceeds 2 hours — abnormal. Possible explanations: (a) outlets delaying publication to morning cycle (21 Jul); (b) Awani/FMT/HarianMetro RSS caches stale (Awani-Politik feed confirmed broken in prior cycles); (c) event coverage published but not yet indexed by gnews/RSS aggregators. **The Vibes pre-launch analysis (16:13 MYT) is the most recent manifesto content found — it previews B40/M50 + continuity themes but does NOT cover the actual launch.** NEXT CYCLE: maintain top priority; also check The Vibes directly (it has faster indexing than RSS-dependent outlets — this cycle's 2 recoveries came from direct The Vibes search, not gnews/RSS).

### PIR STATUS UPDATE

- **PIR-06 [CRITICAL]: MAINTAINED (28th cycle).** 0 threshold crossing. 102 Bersatu/PN gnews hits — ALL pre-cutoff (Jul 11-17), no new intel. No formal expulsion, withdrawal, quorum escalation, RoS action, or "lebih hebat" formalization. Asyraf Wajdi stabilizing signal holds. **No change from 27th cycle.**
- **PIR-16: NOT [CRITICAL].** Loke DAP-congress statement (postmanifesto cycle's HIGHEST-VALUE find) has **NOT been picked up by any other outlet** — gnews has 74 Loke hits, all pre-cutoff, none from NST/Star/Awani/Sinar covering the DAP-congress statement. No AMK/Amanah/UMNO/Bersatu response detected. The "DAP may leave Unity Government" narrative has not spread beyond the original FMT article (19:07/19:29 MYT). Pre-[CRITICAL] escalation status unchanged.
- **PIR-07:** 2 new articles (The Vibes) add campaign-ground intelligence (Sri Tanjung N.33, Seri Menanti). Manifesto launch coverage still pending. BN manifesto 24 Jul at DUN Linggi + Pertang — no advance coverage found this cycle. Jalaluddin vote-buying denial — no follow-up. EC postal ballots — no new coverage.

### ⚠️ COLLECTION LIMITATIONS (night2 cycle)

- **gnews freshness (28th cycle):** 132 queries → 879 items, 518 PRN/priority hits, **0 fresh** post-cutoff. gnews has plateaued — no new PRN content indexed since postmanifesto cycle. gnews continues to surface only historical matches (Jul 11-19).
- **RSS feeds:** FMT 50 (47 PRN/priority hits, 0 fresh — same items as postmanifesto), HarianMetro 51 (38 PRN/priority hits, 0 fresh), Awani 10 (0 fresh), NST/MalayMail/Sinar/Utusan/BH RSS = 0 (JS/403, persistent). Awani-Politik feed still broken.
- **Homepage extraction:** 6 articles saved, ALL false positives (Utusan ×4, Sinar ×2 — deaths, crime, fitness, non-NS). Star/Kosmo/BH/mStar/HarianMetro homepage = 0 PRN links.
- **Sinar ID scan (788880-788960):** 0 PRN hits — 2nd consecutive range exhausted. No new Sinar content in this ID window.
- **False positives (33 deleted):** World Cup ×5 (Spain, Madrid, Yamal-Trump, Paredes-Argentina, Superb Spain), international ×6 (UK PM Burnham, Thailand rail, AliExpress EU, Ukraine drone, HK Patrick Tse, Bahrain-Kuwait-Iran), crime/drugs ×6 (Tamim Dahri Langkawi, Sri Lanka drug, AADK Selangor, Kuching drug, dedah dadah, 2 ditahan seludup), non-NS deaths ×6 (Kajang stabbing, lorry crash, runcit death, motorcycle convoy, drunk driver, stabbing death), federal non-PRN ×6 (Ringgit, Sabah diesel, Pahang orang asli, Ironman Desaru, PIM influencers, Sabah renewable), other ×4 (robot AI, SKMM NADI, Philippine-China, Morocco hotels, Johor land, Kremlin-Rubio). All triggered on substring matches ("pn" in Spain/Palestine/PNB, "negeri" in non-NS context, "loke" in Burnham, etc.).
- **[CRITICAL] auto-flag:** 0 this cycle (28th cycle confirmed). Detector performed cleanly.
- **KEY METHODOLOGY NOTE:** This cycle's 2 genuine recoveries came from **direct The Vibes website search** — NOT from gnews, RSS, or homepage extraction. The Vibes has faster web indexing than RSS-dependent outlets and was not in the standard homepage scan. **Recommend adding The Vibes (thevibes.com/search) to the standard source rotation.** Both recovered articles pre-date the cutoff (16:13 + 18:03 MYT < 20:46 MYT) but were new to collection.

---

## 📈 CYCLE DELTA: postmanifesto → night2 (20:46 → 22:00 MYT 20 Jul, ~1h14m)

- **Articles saved (cleaned):** 2 (33 script-generated false positives deleted + 2 The Vibes manual recoveries = 35 raw; 33 false positives/duplicates deleted)
- **Genuinely-fresh post-cutoff (≥20:46 MYT):** **0** — no new PRN content published after 20:46 MYT detected in any source
- **New to collection (pre-cutoff but not previously captured):** **2** (The Vibes manifesto preview 16:13 MYT + development-record campaign piece 18:03 MYT — both recovered via targeted The Vibes search)
- **Cross-outlet/cross-language corroboration:** **0** this cycle
- **PIR-06 status:** [CRITICAL] MAINTAINED (28th cycle). No new intel. No threshold crossing. Asyraf Wajdi stabilizing signal holds.
- **PIR-16 status:** NOT [CRITICAL]. Loke DAP-congress statement NOT picked up by other outlets. Pre-[CRITICAL] escalation status unchanged.
- **PIR-07 status:** PH MANIFESTO LAUNCH COVERAGE STILL PENDING (4th consecutive cycle, 2+ hours post-event). 2 new campaign-ground articles (Sri Tanjung N.33 + Seri Menanti) recovered. Development-record = dominant PH campaign narrative.
- **Key development this cycle:** The Vibes pre-launch manifesto analysis + campaign-record piece provide the FIRST detailed campaign-ground intelligence for Sri Tanjung (N.33) and Seri Menanti, plus confirmation of B40→M40 expansion and "kesinambungan" continuity as core manifesto themes. However, the actual manifesto launch event coverage remains absent from all monitored sources 2+ hours post-event.

---

## 🎯 NEXT-CYCLE RECOMMENDATIONS (22:00–24:00 MYT window → PH MANIFESTO LAUNCH COVERAGE)

1. **PIR-07 (HIGHEST PRIORITY):** **PH MANIFESTO LAUNCH COVERAGE** — event completed ~20:00 MYT, now 2+ hours post-event with ZERO coverage in gnews/RSS/homepage. **4th consecutive cycle flagging.** Re-poll all sources + add direct The Vibes search (proven effective this cycle). Check if outlets delayed to morning 21 Jul cycle. Look for: full manifesto pledges, Amirudin Shari speech, Aminuddin framing, B40/M50 details, 36-seat strategy, "kesinambungan" continuity messaging. **If still absent by 23:00 MYT, assess whether coverage has shifted to 21 Jul morning print/digital cycle.**
2. **PIR-16 (HIGH PRIORITY):** **Track Loke DAP-congress statement pickup** — still only FMT (19:07/19:29 MYT). Does NST/Star/Awani/Sinar pick it up? Does it trigger AMK/Amanah/UMNO/Bersatu responses? Monitor whether the "DAP may leave Unity Government" narrative spreads. Check The Vibes + Malaysiakini directly (both have faster indexing).
3. **PIR-07 (continued):** Monitor Jalaluddin vote-buying follow-up (accuser going public? SPRM/EC response?). BN manifesto 24 Jul at DUN Linggi + Pertang — monitor advance coverage. Track Sri Tanjung (N.33) + Seri Menanti campaign (new candidates: Rajasekaran, Kamarul — from this cycle's The Vibes recovery).
4. **PIR-06 ([CRITICAL] watch):** 28th cycle with no threshold crossing. Maintain formal-removal watch. Monitor whether Loke's DAP-congress statement triggers any PN/Bersatu response.
5. **Source maintenance:** **ADD THE VIBES to standard source rotation** — this cycle's only genuine recoveries came from direct The Vibes search. FMT RSS = 0 fresh (plateaued). HarianMetro RSS = 0 fresh. gnews = 0 fresh (plateaued). Sinar ID scan 788880-788960 exhausted (2nd consecutive range failure) — next range 788960+. Awani-Politik feed still broken. Consider direct outlet homepage/search checks for FMT, NST, MalayMail, Sinar as RSS alternatives.

---

*Night2 cycle index appended 2026-07-20 ~22:00 MYT (14:00 UTC) by PRN Negeri Sembilan 2026 News Collection Agent — Nomination-Day Surge Mode. TLP:AMBER. 35 raw articles saved → 33 false positives/duplicates deleted → **2 PRN-relevant articles retained** (both The Vibes, recovered via targeted direct search — NOT from gnews/RSS/homepage). [CRITICAL] NOT crossed (28th cycle; 0 auto-flags, 0 false positives). Key night2 developments: (1) ⭐⭐ THE VIBES pre-launch manifesto analysis (16:13 MYT) — Aminuddin confirms B40→M40 expansion + "kesinambungan" continuity as core manifesto themes, 4h before actual launch; (2) ⭐⭐ THE VIBES development-record campaign piece (18:03 MYT) — Sri Tanjung N.33 incumbent Rajasekaran + Seri Menanti candidate Kamarul campaign on investment record (RM1.14B→RM54.3B), "Tok Min" leadership, STR/SARA aid; first detailed PIR-07 campaign-ground intel for these seats; (3) PH MANIFESTO LAUNCH COVERAGE STILL NOT FOUND — 4th consecutive cycle, 2+ hours post-event, 0 items in gnews "after:2026-07-20" search, 0 in all RSS/homepage; (4) Loke DAP-congress statement NOT picked up by other outlets; (5) gnews/RSS freshness plateaued at 0. PIR-06 [CRITICAL] maintained 28th cycle; no formal expulsion/withdrawal/quorum/RoS action. METHODOLOGY NOTE: The Vibes direct search proved decisive — recommend adding to standard source rotation.*
