# PRN Negeri Sembilan 2026 — Unified Workspace Guide

**Classification:** TLP:AMBER  
**Repository:** [github.com/ahmadfaurani/prn-negeri-sembilan-2026](https://github.com/ahmadfaurani/prn-negeri-sembilan-2026)  
**Workspace:** `/home/p62operator/.openclaw/workspace-ns/`  
**HCR:** HCR-095  
**Updated:** 2026-07-24  

---

## 1. Purpose

This document defines the unified workspace structure for PRN Negeri Sembilan 2026 intelligence operations. It maps the Priority Intelligence Requirements (PIR) framework → Operational Use Cases (UC) → directory structure → cronjob pipeline, ensuring all 6 automated cronjobs produce outputs that flow through a single consolidated workspace optimized for Political Intelligence Applied Operational Use Case.

---

## 2. Intelligence Pipeline — 6 Cronjobs

| Stage | Cronjob | ID | Schedule (MYT) | Output Directory | Deliver |
|-------|---------|-----|----------------|-------------------|--------|
| 1 | News Collection | `bf8a4c1fb881` | 06:00 / 18:00 | `04-DATA-AND-SOURCES/raw-scrapes/YYYYMMDD/` | local |
| 2 | Campaign Trail Tracker | `10d9c6242b4e` | 09:00 / 15:00 / 23:00 | `02-CONSTITUENCY-INTELLIGENCE/campaign-trails/YYYYMMDD/` | Telegram |
| 3 | Entity Extraction | `3c9e6756876a` | 08:00 | `04-DATA-AND-SOURCES/processed-entities/YYYYMMDD/` | local |
| 4 | Sentiment Analysis | `02e588724145` | 10:00 | `04-DATA-AND-SOURCES/sentiment-analysis/YYYYMMDD/` | local |
| 5 | Daily Intelligence Brief | `b8f69d6f990d` | 12:00 / 21:00 | `01-DAILY-INTELLIGENCE/daily-briefs/` | Telegram |
| 6 | Git Sync | `2df980e8e094` | 00:00 | Commits all outputs to GitHub | local |

### Data Flow

```
06:00/18:00  News Collection ──────────────────────► raw-scrapes/YYYYMMDD/
                    │
09:00/15:00/23:00  Campaign Trail Tracker ────────► campaign-trails/YYYYMMDD/
                    │                                    │
08:00  Entity Extraction ◄──── raw-scrapes ──────► processed-entities/YYYYMMDD/
                    │
10:00  Sentiment Analysis ◄── processed-entities ► sentiment-analysis/YYYYMMDD/
                    │                                    │
12:00/21:00  Daily Brief ◄── ALL ABOVE ──────────► daily-briefs/PRN-NS-CAMPAIGN-*.md
                    │                                       │
00:00  Git Sync ─── commits everything ──────────► GitHub remote
```

**Key Integration Point:** The Daily Brief (Stage 5) reads Campaign Trail reports (Stage 2) as input, incorporating candidate-level event tracking (CT-01 to CT-08) into the PIR-07 Battleground Matrix and Candidate Alerts sections.

---

## 3. PIR Framework Structure

### 3.1 Statewide PIRs (NS-01 to NS-18)

**Document:** `00-OPERATIONS/pir-framework.md`

| PIR | Priority Intelligence Requirement | Key Focus |
|-----|----------------------------------|-----------|
| NS-01 | Statewide electoral position | Overall PH vs BN vs PN positioning |
| NS-02 | Coalition configuration | PH-BN-UMNO seat allocation |
| NS-03 | Campaign resource deployment | Funding, machinery, volunteers |
| NS-04 | DUN-level risk assessment | 36 DUN classification (Secure→Critical) |
| NS-05 | Demographic targeting | Malay, Chinese, Indian, Orang Asli |
| NS-06 | Coalition operational arrangement | Bersatu-PN rupture consequences |
| NS-07 | Voter sentiment | STR/SARA, welfare, cost of living |
| NS-09 | Youth vote | Apathy, AI-assisted voting, mobilisation |
| NS-10 | Candidate acceptance | PKR machinery friction, candidate quality |
| NS-11 | Opposition strategy | BN-PN cooperation, FELDA credit attribution |
| NS-14 | Dominant narratives | "DAP kontrol gov", racial narrative ecosystem |
| NS-16 | Campaign narrative evolution | Amplifying vs fading narratives |
| NS-17 | T1 seat audit coverage | 19/36 DUNs without audit data |

### 3.2 Campaign Trail PIRs (CT-01 to CT-08)

**Document:** `00-OPERATIONS/pir-framework-campaign-trail.md`

| PIR | Priority Intelligence Requirement | Cadence | Owner |
|-----|----------------------------------|---------|-------|
| CT-01 | Candidate campaign event tracking | 3x daily | Field Operations Lead |
| CT-02 | Coalition leader visit tracking | 3x daily | State Intelligence Director |
| CT-03 | Campaign trail incidents & offences | Event-driven | Legal & Political Secretariat |
| CT-04 | Candidate messaging & statement tracking | 3x daily | Narrative Intelligence Lead |
| CT-05 | Campaign trail momentum assessment | Daily | Electoral Intelligence Lead |
| CT-06 | Social media campaign activity | 3x daily | Information Integrity Cell |
| CT-07 | Multi-cornered fight dynamics | Daily | Opposition Analysis Cell |
| CT-08 | Resource & machinery deployment | Daily | State Operations Director |

---

## 4. Operational Use Cases (UC-01 to UC-12)

**Document:** `00-OPERATIONS/pir-operational-use-cases-20260723.md`

These 12 use cases translate validated PIR findings into actionable campaign operations. Each use case has a 4-phase cycle (Collection → Analysis → Deployment → Verification) with defined decision owners, deadlines, and escalation paths.

| UC# | Title | PIR | Owner | Priority | Deadline |
|-----|-------|-----|-------|----------|----------|
| UC-01 | STR/SARA Ground Verification | NS-07, NS-14 | Insights Lead | CRITICAL | 25 Jul |
| UC-02 | Racial Narrative Counter-Deployment | NS-07, NS-11, NS-14 | Narrative Intel Lead | CRITICAL | 27 Jul |
| UC-03 | FELDA Credit Reattribution | NS-05, NS-07, NS-11, NS-14 | Field Ops Lead | CRITICAL | 30 Jul |
| UC-04 | PKR Candidate-Machinery Reconciliation | NS-10, NS-16 | Candidate Mgmt Lead | CRITICAL | 25 Jul |
| UC-05 | Emergency Campaign Material Deployment | NS-05, NS-16 | State Ops Director | CRITICAL | 26 Jul |
| UC-06 | Youth Mobilisation & AI Info Audit | NS-09, NS-14, NS-15 | Youth Ops Lead | HIGH | 28 Jul |
| UC-07 | Orang Asli Community Access | NS-05 | Field Ops Lead | HIGH | 27 Jul |
| UC-08 | BN Ketua Kampung Network Mapping | NS-05, NS-11 | Opposition Analysis | HIGH | 25 Jul |
| UC-09 | DAP Communications Discipline | NS-14 | Narrative Intel Lead | HIGH | 24 Jul |
| UC-10 | Angkat State Coordination Protocol | NS-10, NS-16 | State Ops Director | HIGH | 26 Jul |
| UC-11 | BN Manifesto Counter-Messaging | NS-11, NS-14 | Opposition Analysis | CRITICAL | 25 Jul |
| UC-12 | Emergency T1 Seat Audit Deployment | NS-04, NS-17 | Electoral Intel Lead | CRITICAL | 26 Jul |

---

## 5. Directory Structure

```
prn-negeri-sembilan-2026/
│
├── 00-OPERATIONS/                         # PIR frameworks, operational use cases, escalation
│   ├── pir-framework.md                   # NS-01 to NS-18 (statewide PIRs)
│   ├── pir-framework-campaign-trail.md    # CT-01 to CT-08 (candidate-level PIRs)
│   ├── pir-operational-use-cases-20260723.md  # UC-01 to UC-12 (actionable use cases)
│   ├── pir-approval-record.md             # Director-approved PIR priorities
│   ├── pir-quick-reference.md             # Quick-ref card for field operators
│   ├── pir-non-core-candidates.md         # Non-core candidate tracking
│   ├── candidate-tracker.md               # 103 candidates across 36 DUNs
│   ├── dun-master-list.md                  # 36 DUN master list
│   ├── election-calendar.md               # Campaign calendar (18 Jul – 1 Aug)
│   ├── escalation-register.md             # Triggered escalation flags
│   └── sanitize-filter-triggers.sh         # Content filter false-positive mitigation
│
├── 01-DAILY-INTELLIGENCE/                  # Daily briefs and situational reports
│   ├── daily-briefs/                       # PRN-NS-CAMPAIGN-YYYYMMDD-HHMM.md
│   │   ├── (Daily_Brief_20260710.md … 20260717.md)    # Pre-campaign period
│   │   ├── (PRN-NS-NOMINATION-20260718-*.md)           # Nomination day series
│   │   └── (PRN-NS-CAMPAIGN-20260721-*.md … current)   # Campaign period
│   └── sitreps/                            # Special situational reports
│       ├── pir-field-audit-integration-20260723.md     # 84 audit records → 8 PIRs
│       └── pir-ns-01-statewide-position-20260710.md   # Statewide position sitrep
│
├── 02-CONSTITUENCY-INTELLIGENCE/           # DUN-level intelligence
│   ├── campaign-trails/                    # Campaign Trail Tracker outputs (Stage 2)
│   │   └── YYYYMMDD/
│   │       └── PRN-NS-CAMPAIGN-TRAIL-YYYYMMDD-HHMM.md
│   └── constituency-profiles/              # DUN intelligence profiles (36 DUNs)
│
├── 03-VERIFICATION/                        # Verification & ground-truth tracking
│
├── 04-DATA-AND-SOURCES/                   # Raw data and processed intelligence
│   ├── raw-scrapes/                        # News collection outputs (Stage 1)
│   │   └── YYYYMMDD/
│   ├── processed-entities/                 # Entity extraction outputs (Stage 3)
│   │   └── YYYYMMDD/
│   ├── sentiment-analysis/                 # Sentiment analysis outputs (Stage 4)
│   │   └── YYYYMMDD/
│   ├── field-audit/                        # Field audit PDF + extracted text
│   │   ├── LAPORAN-TERPERINCI-ISU-DUN-N9.pdf
│   │   └── LAPORAN-TERPERINCI-ISU-DUN-N9.txt
│   └── spr-data/                           # SPR official election data
│
├── 05-TOOLS-AND-AUTOMATION/                # Scripts, configs, templates
│   ├── cronjob-configs.json                # All 6 NS cronjob configurations (auto-exported)
│   ├── scripts/                             # Processing scripts
│   └── templates/                           # Output templates
│
├── 06-INFRASTRUCTURE/                      # Infrastructure documentation
│
├── 07-AUDIT/                               # Audit trails and quality checks
│
├── WORKSPACE-GUIDE.md                      # THIS FILE — unified workspace map
├── README.md                               # Repository overview
├── CHANGELOG.md                            # Change log
├── CONTRIBUTING.md                         # Contribution guidelines
└── .github/                                # Issue templates, PR templates
    ├── ISSUE_TEMPLATE/
    │   ├── intelligence-product.md
    │   └── operational-change.md
    └── PULL_REQUEST_TEMPLATE.md
```

---

## 6. PIR → Directory → Cronjob Cross-Reference

| PIR Framework | Operational Use Case | Output Directory | Producing Cronjob |
|---------------|---------------------|-------------------|-------------------|
| NS-01 to NS-18 | — | `01-DAILY-INTELLIGENCE/daily-briefs/` | Daily Brief (Stage 5) |
| NS-04, NS-17 | UC-12 | `02-CONSTITUENCY-INTELLIGENCE/constituency-profiles/` | Manual + Campaign Trail |
| NS-05, NS-07, NS-11, NS-14 | UC-01, UC-02, UC-03, UC-08, UC-11 | `01-DAILY-INTELLIGENCE/sitreps/` | Daily Brief + manual |
| NS-07, NS-14 | UC-01 | `04-DATA-AND-SOURCES/field-audit/` | Manual (field audit) |
| NS-09, NS-14, NS-15 | UC-06 | `02-CONSTITUENCY-INTELLIGENCE/campaign-trails/` | Campaign Trail (Stage 2) |
| NS-10, NS-16 | UC-04, UC-10 | `02-CONSTITUENCY-INTELLIGENCE/campaign-trails/` | Campaign Trail (Stage 2) |
| CT-01 to CT-08 | All UCs | `02-CONSTITUENCY-INTELLIGENCE/campaign-trails/` | Campaign Trail (Stage 2) |
| All NS PIRs | All UCs | `04-DATA-AND-SOURCES/raw-scrapes/` | News Collection (Stage 1) |
| All NS PIRs | All UCs | `04-DATA-AND-SOURCES/processed-entities/` | Entity Extraction (Stage 3) |
| All NS PIRs | All UCs | `04-DATA-AND-SOURCES/sentiment-analysis/` | Sentiment Analysis (Stage 4) |

---

## 7. Cronjob Cross-Integration

### 7.1 Campaign Trail → Daily Brief (Critical Integration)

The Campaign Trail Tracker (Stage 2) produces candidate-level intelligence that the Daily Brief (Stage 5) must ingest before generating each brief.

**What flows:**
- CT-01 events → Brief's PIR-07 Battleground Matrix (candidate event coverage)
- CT-04 statements → Brief's Candidate Alerts section
- CT-05 momentum shifts → Brief's PIR-07 update (momentum change flags)
- CT-07 multi-cornered dynamics → Brief's PIR-06 coalition analysis
- CT-03 incidents → Brief's Escalation section

**How:**
The Daily Brief prompt instructs the agent to read the latest Campaign Trail report from `02-CONSTITUENCY-INTELLIGENCE/campaign-trails/YYYYMMDD/` before generating the brief.

### 7.2 News Collection → Campaign Trail (Complementary)

The News Collection (Stage 1) provides issue-level news coverage. The Campaign Trail Tracker (Stage 2) provides candidate-level event tracking. They run at different times and use different search strategies:

- News Collection: 06:00/18:00 MYT — broad news scrape, issue-focused
- Campaign Trail: 09:00/15:00/23:00 MYT — targeted candidate searches, event-focused

### 7.3 Campaign Trail → PIR Operational Use Cases

The Campaign Trail Tracker references the PIR Operational Use Cases document (`00-OPERATIONS/pir-operational-use-cases-20260723.md`). When campaign trail findings are relevant to an active use case, the tracker notes "UC-XX RELEVANT" in the relevant section, creating a real-time feedback loop between field intelligence and operational planning.

---

## 8. Configuration Export

The Git Sync cronjob (`2df980e8e094`) automatically exports all 6 NS cronjob configurations to `05-TOOLS-AND-AUTOMATION/cronjob-configs.json` on each run. This file contains:
- Cronjob IDs, names, schedules, delivery targets
- Model and provider configurations
- Full prompts (for audit and version control)
- Enabled toolsets
- Workspace paths

---

## 9. Election Calendar Reference

| Date | Event | Operational Significance |
|------|-------|------------------------|
| 18 Jul | Nomination Day | Candidate confirmation, 103 candidates across 36 DUNs |
| 18–31 Jul | Campaign Period (14 days) | All 6 cronjobs active in Campaign Period Mode |
| 24 Jul | BN manifesto launch | DUN Linggi + Pertang — UC-11 activated |
| 28 Jul | Early Voting Day | Police/military voters |
| 31 Jul 23:59 | Campaigning prohibited | All deployment phases must complete |
| 1 Aug | Polling Day | All use case success criteria verified |

---

## 10. Maintenance

- **Git Sync** runs daily at 00:00 MYT — all untracked files are committed and pushed
- **Cronjob configs** are auto-exported on each Git Sync run
- **Workspace Guide** (this file) should be updated when:
  - New PIRs are added or approved
  - New operational use cases are created
  - Directory structure changes
  - New cronjobs are added to the pipeline

---

*TLP:AMBER — For official use only. Distribution controlled.*
