# PRN Negeri Sembilan 2026 — Political Intelligence Operational Workspace (WS1)

**Classification:** TLP:AMBER  
**Repository:** [prn-negeri-sembilan-2026](https://github.com/ahmadfaurani/prn-negeri-sembilan-2026) (HCR-095, Private)  
**Coverage:** 36 DUN constituencies across 8 Parliamentary seats, Negeri Sembilan State Election 2026  
**Election Date:** 1 August 2026  
**Nomination Day:** 18 July 2026  
**Operational Period:** Pre-Campaign → Polling Day → Post-Election  

---

## Workspace Architecture

This workspace follows the **Intelligence Lifecycle** taxonomy — each directory represents a phase in the collection, processing, analysis, and dissemination cycle. The structure mirrors the proven PRN Johor 2026 operational workspace.

```
prn-negeri-sembilan-2026/
│
├── 00-OPERATIONS/                    Framework, PIR, methodology, DUN master list
├── 01-DAILY-INTELLIGENCE/             Time-series intelligence products
├── 02-CONSTITUENCY-INTELLIGENCE/      Seat-level intelligence & candidate dossiers
├── 03-VERIFICATION/                   Fact-checking & source integrity
├── 04-DATA-AND-SOURCES/               Raw data, SPR results, processed entities
├── 05-TOOLS-AND-AUTOMATION/           Scripts, templates
├── 06-INFRASTRUCTURE/                 Logs, deployment config
└── 07-AUDIT/                          Reports, QA tracking
```

---

## Directory Breakdown

### 00-OPERATIONS/ (3 files)
Operational framework documents governing intelligence collection and analysis.

- `pir-framework.md` — 12 Priority Intelligence Requirements (PIR) with sub-questions
- `pir-quick-reference.md` — Quick-reference card for PIR framework
- `dun-master-list.md` — 36 DUN seats across 8 Parliaments with baseline classification

### 01-DAILY-INTELLIGENCE/ (6 files)
Time-series intelligence products from automated cronjob pipeline.

- **`daily-briefs/`** (5) — Consolidated daily intelligence briefs (10 Jul – 14 Jul 2026)
- **`sitreps/`** (1) — PIR NS-01 Statewide Position assessment (10 Jul 2026)

### 02-CONSTITUENCY-INTELLIGENCE/ (36 files)
Seat-level intelligence for all 36 DUN constituencies.

- **`constituency-profiles/`** (36) — Full DUN seat profiles (N01–N36) with 2023 SPR baseline results, classification, and intelligence gap tracking
- **`candidate-dossiers/`** — Individual candidate deep-dives (to be populated post-nomination)
- **`war-room-reports/`** — Rapid-response seat analysis (to be activated for critical seats)

### 03-VERIFICATION/ (0 files — framework ready)
Source integrity and fact-checking products.

### 04-DATA-AND-SOURCES/ (130+ files)
Raw data, processed entities, and reference sources.

- **`spr-data/`** (3) — SPR 2023 election results (CSV, JSON, README) — complete for all 36 DUN
- **`raw-scrapes/`** (~40) — Raw news scrape outputs by date (10 Jul – 14 Jul 2026)
- **`processed-entities/`** (~90) — Entity extraction outputs by date (politicians, parties, constituencies, organizations, events, issues, locations)

### 05-TOOLS-AND-AUTOMATION/ (6 files)
Collection, analysis, and processing scripts.

- `ns-daily-collection.sh` — Daily news collection from 10 Malaysian sources
- `ns-daily-brief.sh` — Daily intelligence brief generator
- `ns-entity-extraction.sh` — Entity extraction pipeline
- `ns-sentiment-analysis.sh` — Sentiment analysis pipeline
- `ns_cvs_extraction_20260712.py` — CVS-compliant entity extraction
- `ns_entity_extraction_sourced.py` — Source-attributed entity extraction

### 06-INFRASTRUCTURE/ (4 files)
Operational logs and deployment tracking.

- `collection_20260712_052935.log` — Collection log
- `collection_20260713_010102.log` — Collection log
- `collection_20260714_010109.log` — Collection log
- `extraction_20260714.log` — Entity extraction log

### 07-AUDIT/ (6 files)
Quality assurance and deployment tracking.

- `DEPLOYMENT_SUMMARY_20260710.md` — Initial deployment summary
- `COLLECTION_STATUS_20260712.md` — Collection status report
- `COLLECTION_STATUS_20260713.md` — Collection status report
- `ENTITY_EXTRACTION_LOG_20260711.md` — Entity extraction QA
- `ENTITY_EXTRACTION_LOG_20260713.md` — Entity extraction QA
- `GITHUB_UPLOAD_SUMMARY_20260710.md` — GitHub sync summary

---

## Automated Pipeline (5 Cronjobs)

| Cronjob | Schedule | Job ID | Output Directory |
|---------|----------|---------|------------------|
| Daily News Collection | 01:00 UTC | `bf8a4c1fb881` | `04-DATA-AND-SOURCES/raw-scrapes/` |
| Entity Extraction | 06:00 UTC | `3c9e6756876a` | `04-DATA-AND-SOURCES/processed-entities/` |
| Sentiment Analysis | 08:00 UTC | `02e588724145` | `04-DATA-AND-SOURCES/processed-entities/` |
| Daily Intelligence Brief | 09:00 UTC | `b8f69d6f990d` | `01-DAILY-INTELLIGENCE/daily-briefs/` |
| Git Sync Automation | 10:00 UTC | `2df980e8e094` | Pushes to GitHub |

---

## 2023 Baseline Results

| Coalition | Seats Won | Key Strongholds |
|-----------|-----------|-----------------|
| **PH** | 17 | Seremban urban (DAP), Sikamat (MB seat), Port Dickson |
| **BN** | 14 | Rural Malay heartland (Jelebu, Kuala Pilah, Rembau, Tampin) |
| **PN** | 5 | Serting, Labu, Paroi, Bagan Pinang, Gemas |

**Total registered voters:** 864,425  
**Average turnout:** 68.35%  
**Closest margin:** N15 Juasseh (78 votes, 0.86%)

---

## Seat Priority Classification

### T1: Critical (7 seats, <5% margin)
- N03 Sungai Lui (4.0%) — BN vs PN
- N05 Serting (4.3%) — PN vs BN
- N06 Palong (3.7%) — BN vs PN
- N09 Lenggeng (3.5%) — BN vs PN
- N14 Ampangan (2.2%) — PH vs PN
- N15 Juasseh (0.9%) — BN vs PN
- N28 Kota (1.2%) — BN vs PN

### T2: Vulnerable (6 seats, <10% margin)
- N04 Klawang (6.4%) — PH vs PN
- N07 Jeram Padang (6.8%) — BN vs PN
- N16 Seri Menanti (5.2%) — BN vs PN
- N17 Senaling (9.8%) — BN vs PN
- N18 Pilah (9.5%) — PH vs PN
- N20 Labu (7.6%) — PN vs PH

---

## Intelligence Lifecycle

```
  PLAN          COLLECT           PROCESS          ANALYZE          VERIFY          DISSEMINATE
   │               │                 │                 │                │                │
   ▼               ▼                 ▼                 ▼                ▼                ▼
00-OPERATIONS  04-DATA-AND-     05-TOOLS-AND-     01-DAILY-       03-VERIFICATION  01-DAILY-
  PIR           SOURCES          AUTOMATION        INTELLIGENCE                       BRIEFS
  DUN Master    Raw scrapes      Scripts          Daily briefs
  Framework     SPR data         Templates        Sitreps
                                                  │
                                                  ▼
                                        02-CONSTITUENCY-INTELLIGENCE
                                          36 DUN profiles
                                          Candidate dossiers
                                          War-room reports
                                                  │
                                                  ▼
                                            07-AUDIT
                                        Reports, QA tracking
```

---

## Key Context: Royal Crisis (April 2026)

- Removal of Datuk Mubarak Dohak as Undang of Sungei Ujong
- Counter-declaration by 4 Undangs naming Tunku Nadzaruddin as YDP
- 14 UMNO assemblymen withdrawing support (later reversed by Zahid)
- PAS cutting ties with Bersatu (9 June 2026)
- Intelligence questions: impact on Malay voter sentiment, UMNO grassroots machinery, Undang campaigning

---

## Related Workstreams

| Workstream | Repo | HCR |
|-----------|------|-----|
| **PRN Negeri Sembilan 2026** (this) | prn-negeri-sembilan-2026 | HCR-095 |
| PRN Johor 2026 | PRN-Johor-2026-H | HCR-062 |
| Intelligence Pipeline Ops | hoi-intelligence-ops | HCR-003 |
| Journalist Registry | malaysia-journalist-registry | HCR-011 |

---

## File Inventory

**Total tracked files:** 160+ (124 migrated + 36 constituency profiles + SPR data)  
**Last sync:** 2026-07-14  
**Git remote:** `https://github.com/ahmadfaurani/prn-negeri-sembilan-2026.git` (private)
