# PRN Negeri Sembilan 2026 — Political Intelligence Workstream (HCR-095)

**Classification:** TLP:AMBER  
**Repository:** [prn-negeri-sembilan-2026](https://github.com/ahmadfaurani/prn-negeri-sembilan-2026) (HCR-095, Private)  
**Coverage:** 36 DUN constituencies across 8 Parliamentary seats  
**Election:** 16th Negeri Sembilan State Legislative Assembly  
**Dissolution:** 5 June 2026 | **Nomination Day:** 18 July 2026 | **Polling Day:** 1 August 2026  
**Baseline (PRN 2023):** PH 17 / BN 14 / PN 5 (19 needed for majority)  
**Created:** 10 July 2026 | **Last Updated:** 18 July 2026

---

## 1. Mission

Produce timely, source-attributed political intelligence to support state campaign leadership, constituency war rooms, and strategic decision-making throughout the PRN Negeri Sembilan 2026 election cycle. All products classified TLP:AMBER and verified using the CVS (Core Truth Validation) framework.

---

## 2. Workspace Structure

```
prn-negeri-sembilan-2026/
├── 00-OPERATIONS/              Frameworks, PIRs, master lists, escalation register
│   ├── pir-framework.md              PRN16 standard framework (18 PIRs, NS-01 to NS-18)
│   ├── pir-framework-nomination-day.md  Nomination Day surge framework (25 PIRs, PIR-01 to PIR-25)
│   ├── pir-quick-reference.md         One-page operations reference card
│   ├── pir-non-core-candidates.md      Non-core candidate tracking
│   ├── dun-master-list.md             36 DUN master reference (N01-N36)
│   ├── election-calendar.md            Full election timeline and phases
│   ├── escalation-register.md          Live escalation flag tracker (ESC-001 to ESC-011)
│   └── candidate-tracker.md            36-DUN candidate roll (SPR-verified, continuously updated)
│
├── 01-DAILY-INTELLIGENCE/      Daily briefs, sitreps, coalition analysis
│   ├── daily-briefs/                   Daily and hourly intelligence briefs
│   └── sitreps/                        Situation reports
│
├── 02-CONSTITUENCY-INTELLIGENCE/  36 DUN constituency profiles
│   └── constituency-profiles/         N01-N36 individual analysis files
│
├── 03-VERIFICATION/            CVS compliance, source register, verification status
│   ├── cvs-framework.md               Core Truth Validation methodology
│   ├── source-register.md             All sources tracked with reliability ratings
│   └── verification-status.md         Per-claim verification status log
│
├── 04-DATA-AND-SOURCES/        Raw scrapes, processed entities, SPR official data
│   ├── raw-scrapes/                    Daily news scrapes (YYYYMMDD format)
│   ├── processed-entities/            Extracted entities per day (JSON)
│   ├── spr-data/                       SPR official 2023 results + 2026 candidate list
│   └── spr-candidate-list-20260718.json  SPR official 2026 candidate list (103 candidates)
│
├── 05-TOOLS-AND-AUTOMATION/    Scripts, templates, automation infrastructure
│   ├── scripts/                        Collection, extraction, sentiment, brief scripts
│   └── templates/                      Brief, sitrep, and nomination-day templates
│
├── 06-INFRASTRUCTURE/          Collection and processing logs
├── 07-AUDIT/                   Deployment summaries, audit logs
├── .github/                    Issue templates, PR templates
├── CONTRIBUTING.md             Operational guidelines for intelligence cell
├── CHANGELOG.md                Operational changelog
└── README.md                   This file
```

---

## 3. PIR Framework

### Standard Framework (PRN16) — 18 PIRs

| PIR | Question | Cadence |
|-----|----------|---------|
| NS-01 | Statewide electoral position | Daily |
| NS-02 | Post-dissolution realignment | Daily |
| NS-03 | Government-formation scenarios | Weekly → Daily |
| NS-04 | DUN electoral risk | Daily |
| NS-05 | Locality prioritisation | Daily |
| NS-06 | Turnout risk | Daily → Hourly (Polling Day) |
| NS-07 | Voter sentiment and issues | Daily |
| NS-08 | Undecided electorate | 2x Weekly |
| NS-09 | Youth participation | 2x Weekly |
| NS-10 | Candidate acceptance | Daily |
| NS-11 | Opposition strategy | Daily |
| NS-12 | Stakeholder alignment | Daily |
| NS-13 | Adat and institutional sensitivity | Event-driven |
| NS-14 | Dominant narratives | Continuous |
| NS-15 | Misinformation risk | Continuous |
| NS-16 | Machinery readiness | Daily |
| NS-17 | Data readiness | Daily |
| NS-18 | Campaign-phase readiness | Phase-based |

### Nomination Day Surge Framework — 25 PIRs (PIR-01 to PIR-25)

Activated 18 July 2026 for the Nomination Day window. Covers:
- **PIR-01–05:** Candidate configuration, paper rejections, no-shows, contest type, substitutions
- **PIR-06–07:** Coalition operational arrangements, battleground identification
- **PIR-08–12:** Candidate quality, demographics, independents, incumbents dropped, grassroots rejection
- **PIR-13–15:** Machinery mobilisation, ground support failure, crowd patterns
- **PIR-16–19:** Narratives, public reaction, misinformation, influence networks
- **PIR-20–22:** Security incidents, legal complaints, leader deployment
- **PIR-23–24:** Endorsements, resource disparities
- **PIR-25:** Post-nomination watch

See `00-OPERATIONS/pir-framework-nomination-day.md` for full framework with EEIs.

---

## 4. Automated Pipeline (5 Cronjobs)

| # | Job | Schedule (Normal) | Schedule (Nomination Day) | Delivery |
|---|-----|-------------------|---------------------------|----------|
| 1 | News Collection | Daily 01:00 MYT | Every 1 hour | Local |
| 2 | Entity Extraction | Daily 06:00 MYT | Every 2 hours | Local |
| 3 | Sentiment Analysis | Daily 08:00 MYT | Every 2 hours | Local |
| 4 | Intelligence Brief | Daily 09:00 MYT | Every 1 hour | Telegram |
| 5 | Git Sync | Daily 10:00 MYT | Every 2 hours | Local |

**Pipeline flow:** Collection → Entity Extraction → Sentiment Analysis → Intelligence Brief → Git Sync

**Sources scraped (13):** Sinar Harian, Bharian, Utusan, NST, The Star, Malaysiakini, Free Malaysia Today, Astro Awani, Bernama, Kosmo, mStar, OhBulan, and one additional source per cycle.

---

## 5. Election Timeline

| Date | Event | Phase |
|------|-------|-------|
| 5 Jun 2026 | Assembly dissolved | Phase 1 — Pre-Nomination |
| 10 Jul 2026 | Intelligence workspace deployed | Phase 1 |
| 18 Jul 2026 | **Nomination Day** | Phase 2 — Nomination |
| 18–31 Jul 2026 | Campaign Period | Phase 3 — Campaign |
| 28 Jul 2026 | Early Voting | Phase 4 — Early Voting |
| 1 Aug 2026 | **Polling Day** | Phase 5 — Polling |
| 1 Aug+ | Post-Poll Analysis | Phase 6 — Post-Poll |

---

## 6. Current Escalation Flags (as of 18 Jul 2026)

| Flag | Description | Status | Severity |
|------|-------------|--------|----------|
| ESC-002 | Sentiment pipeline non-operational (Aras API not wired) | Active | HIGH |
| ESC-003 | Royal issue sensitivity — indirectly confirmed | Active | MEDIUM |
| ESC-006 | Opposition unity disruption | **REOPENED** | CRITICAL |
| ESC-007 | PH Malay seats quantified and threatened | Downgraded | MEDIUM |
| ESC-009 | BN-PN electoral pact | Downgraded | MEDIUM |
| ESC-010 | PN internal friction (Muhyiddin vs Samsuri) | **UPGRADED** | CRITICAL |
| ESC-011 | **NEW:** BERSATU 24-candidate independent deployment | **NEW** | CRITICAL |

See `00-OPERATIONS/escalation-register.md` for full history.

---

## 7. SPR Verified Candidate Configuration (18 Jul 2026)

**Total:** 103 candidates across 36 DUNs  
**Confirmed by:** SPR/Returning Officer official list

| Party | Candidates | Contesting Under |
|-------|-----------|------------------|
| PH (Pakatan Harapan) | 36 | Full slate (all 36 DUNs) |
| BN (Barisan Nasional) | 25 | Own symbol |
| BERSATU | 24 | **Own symbol — independent of PN** |
| PN (Perikatan Nasional) | 11 | Own symbol (likely PAS candidates) |
| BEBAS (Independent) | 4 | Individual |
| ASLI | 1 | N.07 Jeram Padang |
| BERJASA | 1 | N.10 Nilai |
| PSM | 1 | N.22 Rahang |

**Contest types:** 11 straight fights | 21 three-cornered | 2 four-cornered | 2 five-cornered

**Critical finding:** BERSATU is contesting independently of PN, creating a 4-way split that invalidates the "opposition unity" narrative from 17 July.

See `04-DATA-AND-SOURCES/spr-candidate-list-20260718.json` for structured data.  
See `01-DAILY-INTELLIGENCE/daily-briefs/PRN-NS-NOMINATION-20260718-PIR01-CANDIDATE-ROLL.md` for full analysis.

---

## 8. Intelligence Products

### Daily Briefs (10 Jul – 18 Jul)
8 days of daily briefs covering the pre-nomination and nomination period. Briefs include:
- Executive assessment (5 points)
- Statewide seat dashboard
- Coalition dynamics
- Critical DUN updates
- Narrative and issue environment
- Machinery readiness
- Stakeholder developments
- Early-warning register
- Command decisions

### Nomination Day Hourly Briefs
Hourly briefs produced during the 18 July nomination window with 11-section structure including 36-DUN candidate roll, contest configuration map, and escalation trigger checklist.

### Constituency Profiles
All 36 DUN constituency profiles (N01–N36) covering:
- 2023 SPR results (winner, margin, contest type)
- Demographic breakdown
- T1/T2/T3 classification
- Incumbent information
- Historical trends

---

## 9. Data Collection

- **Raw scrapes:** 9 days (10 Jul – 18 Jul), 13 sources per day
- **Processed entities:** 8 days of extracted political entities (politicians, parties, constituencies, issues, events, locations, organizations)
- **SPR 2023 results:** Complete 36-DUN results in CSV and JSON format
- **SPR 2026 candidate list:** Official 103-candidate list (JSON)
- **Sentiment analysis:** Daily sentiment tracking (where available)

---

## 10. Git Configuration

```
user.name:  ahmadfaurani
user.email: p62operator@proton.me
remote:     origin → https://github.com/ahmadfaurani/prn-negeri-sembilan-2026.git
branch:     main
```

Auto-sync commits use prefix `auto:` and run every 2 hours during Nomination Day surge.

---

## 11. Classification and Compliance

- **All products:** TLP:AMBER
- **Source attribution:** Required for every claim
- **Unverified information:** Tagged `[UNVERIFIED]`
- **Assessments:** Tagged `[ASSESSMENT]`
- **CVS framework:** 3-tier verification (VERIFIED / MEDIUM / EXCLUDED)
- **No PII:** IC numbers in SPR data are masked in committed files

---

**Workspace:** `/home/p62operator/.openclaw/workspace-ns/`  
**Authority:** State Intelligence Director  
**Classification:** TLP:AMBER  
**HCR:** HCR-095
