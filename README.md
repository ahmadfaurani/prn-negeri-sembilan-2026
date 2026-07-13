# PRN Negeri Sembilan 2026 - Operational Workspace

**Classification:** TLP:AMBER  
**State:** Negeri Sembilan  
**Total DUN:** 36 constituencies  
**Election Date:** 1 August 2026  
**Workspace:** `/home/p62operator/.openclaw/workspace-ns/`

---

## Mission

Establish and operate a comprehensive political intelligence collection and analysis system for the Negeri Sembilan 2026 state election, parallel to the existing PRN Johor 2026 workstream.

**Operating Principle:** Every PIR must be decision-linked, geographically specific, evidence-based, assigned to an owner, supported by measurable indicators, tied to an escalation threshold, and translated into a lawful operational action.

---

## Infrastructure Stack

| Service | Port | Status | Purpose |
|---------|------|--------|---------|
| DeerFlow Gateway | 2026 | ✓ Active | Intelligence collection orchestration |
| Firecrawl API | 3002 | ✓ Active | Web scraping (markdown extraction) |
| SearXNG | 8080 | ✓ Active | Meta-search engine |
| OpenOSINT v2.23.0 | - | ✓ Active | Entity extraction, sentiment analysis (Qwen3.5-397B-A17B) |

**CVS Standard:** 100% "absolute truth" verification mandatory. No single-source claims in operational briefs.

---

## Workspace Structure

```
/home/p62operator/.openclaw/workspace-ns/
├── PIR_FRAMEWORK.md              # Priority Intelligence Requirements (12 PIRs)
├── README.md                     # This file
├── scripts/
│   ├── ns-daily-collection.sh    # Daily news collection (13 sources)
│   ├── ns-entity-extraction.sh   # Entity extraction (7 categories)
│   ├── ns-sentiment-analysis.sh  # Sentiment analysis (OpenOSINT)
│   └── ns-daily-brief.sh         # Daily Intelligence Brief generator
├── intelligence/
│   ├── raw/                      # Collected raw news content
│   │   └── YYYYMMDD/             # Date-stamped collection directories
│   ├── processed/                # Processed intelligence
│   │   └── YYYYMMDD/             # Entities, sentiment, narratives
│   └── briefs/                   # Daily/weekly intelligence briefs
├── constituencies/
│   ├── DUN_MASTER_LIST.md        # All 36 DUN with baseline data
│   ├── defend/                   # Secure seats (baseline: TBD)
│   ├── favourable/               # Leading seats (baseline: TBD)
│   ├── competitive/              # Uncertain outcome (baseline: TBD)
│   ├── vulnerable/               # Weakening position (baseline: TBD)
│   ├── critical/                 # Immediate intervention (baseline: TBD)
│   └── gap/                      # Insufficient intelligence (baseline: 36)
├── stakeholders/                 # Stakeholder mapping (Undangs, leaders)
├── narratives/                   # Narrative tracking
├── opposition/                   # BN/PN activity monitoring
└── reports/                      # Campaign Operations Manuals
```

---

## Cronjob Pipeline

| Job ID | Name | Schedule | Delivery | Status |
|--------|------|----------|----------|--------|
| `bf8a4c1fb881` | PRN NS - Daily News Collection | 01:00 daily | local | ✓ Scheduled |
| `3c9e6756876a` | PRN NS - Entity Extraction | 06:00 daily | local | ✓ Scheduled |
| `02e588724145` | PRN NS - Sentiment Analysis | 08:00 daily | local | ✓ Scheduled |
| `b8f69d6f990d` | PRN NS - Daily Intelligence Brief | 09:00 daily | Telegram | ✓ Scheduled |

**Collection Timeline:**
- **01:00 UTC:** Collect news from 13 Negeri Sembilan sources
- **06:00 UTC:** Extract entities (politicians, parties, DUN, issues, events, orgs, locations)
- **08:00 UTC:** Analyze sentiment (Qwen3.5-397B-A17B via OpenOSINT)
- **09:00 UTC:** Generate and deliver Daily Intelligence Brief

---

## Priority Intelligence Requirements (12 PIRs)

| PIR ID | Question | Decision Supported |
|--------|----------|-------------------|
| PIR-01 | Current electoral position across all 36 DUNs? | Seat strategy, resource allocation |
| PIR-02 | Which DUNs most likely to change control? | Defensive/offensive deployment |
| PIR-03 | Which localities offer persuasion/turnout opportunity? | Field and candidate deployment |
| PIR-04 | Which issues increasing/reducing support? | Policy and communications response |
| PIR-05 | Which voter groups likely weak turnout? | Mobilisation and election-day planning |
| PIR-06 | Which candidates strengthen/weaken competitiveness? | Candidate positioning and support |
| PIR-07 | Where are opponents concentrating resources? | Counter-positioning and resource response |
| PIR-08 | Which stakeholders supportive/neutral/opposed? | Leadership engagement |
| PIR-09 | Which narratives shaping voter perception? | Strategic communications |
| PIR-10 | Which DUN/Daerah operations ready/non-operational? | Operational reinforcement |
| PIR-11 | Is electoral intelligence accurate/complete/current? | Intelligence reliability |
| PIR-12 | What emerging event could affect multiple constituencies? | Crisis escalation and response |

---

## DUN Classification System

| Status | Meaning | Action |
|--------|---------|--------|
| **Secure** | Strong position, low risk | Maintain machinery, monitor |
| **Favourable** | Leading, needs activity | Continue engagement |
| **Competitive** | Uncertain outcome | Priority resource allocation |
| **Vulnerable** | Weakening position | Emergency intervention |
| **Critical** | Immediate intervention required | War room activation |
| **GAP** | Insufficient intelligence | Intelligence collection priority |

**Current Baseline:** All 36 DUN classified as **GAP** pending Week 1 intelligence sprint.

---

## News Collection Sources (13 Priority)

1. Sinar Harian Negeri Sembilan
2. BHarian Sembilan
3. Utusan Negeri Sembilan
4. NST Nation
5. The Star Nation
6. Malaysiakini MY
7. Free Malaysia Today Nation
8. Bernama Hub Nasional
9. Astro Awani Nasional
10. Oh Bulan Negeri Sembilan
11. MStar Lokal Sembilan
12. Metro Nasional
13. Kosmo Nasional

---

## Royal Crisis Context (April 2026)

**Key Events:**
- 17 Apr: MB Aminuddin removes Datuk Mubarak Dohak as Undang of Sungei Ujong
- 19 Apr: 4 Undangs declare removal of Tuanku Muhriz, name Tunku Nadzaruddin as YDP
- 27 Apr: 14 UMNO assemblymen withdraw support (later reversed by Zahid)
- 9 Jun: PAS cuts ties with Bersatu
- 4 Jun: Assembly dissolved (snap election)
- 1 Aug: Polling Day

**Intelligence Questions:**
1. Which 14 assemblymen withdrew support?
2. How has crisis affected Malay voter sentiment in royal constituencies?
3. Has UMNO grassroots machinery been compromised?
4. Are Undangs actively campaigning against PH?

---

## Core Truth Validation (CVS) Framework

| Tier | Status | Confidence | Deployment |
|------|--------|------------|------------|
| **VERIFIED** | Multi-source confirmed (SPR + 2+ news) | 95%+ | Deploy-ready |
| **MEDIUM** | Single-source or inferred | 60-85% | Hold for browser verification |
| **EXCLUDED** | Unverified claims, pattern-inferred | <60% | Stripped from briefs |

**Standard:** 100% "absolute truth" — no single-source claims in operational products.

---

## Escalation Triggers

**Immediate escalation required when:**
- [ ] Favourable DUN moves to competitive/vulnerable
- [ ] Critical locality shows sustained support decline
- [ ] High-influence stakeholder changes position
- [ ] Negative narrative expands across multiple constituencies
- [ ] Competitive DUN has weak machinery readiness
- [ ] Turnout falls below expected baseline
- [ ] Candidate rejection threatens electoral viability
- [ ] Intelligence/voter data materially inaccurate or compromised

---

## Week 1 Intelligence Priorities

### Tier 1: Critical Gaps
1. Complete 2023 election results (all 36 DUN: vote counts, margins, turnout)
2. Incumbent status (defending, retiring, challenging)
3. Candidate nominations (track all coalitions)
4. Demographic breakdown (voter rolls by ethnicity, age, locality)

### Tier 2: Baseline Assessment
1. Historical voting patterns (2013, 2018, 2023)
2. Current assemblymen performance (approval, controversies)
3. Opposition targeting (priority seats for PN/BN)
4. Stakeholder mapping (Undangs, community leaders, business groups)

### Tier 3: Operational Readiness
1. Machinery audit (PH/BN/PN ground operations by DUN)
2. Early voting patterns (postal, advance voting)
3. Narrative baseline (top 5 issues per constituency)

---

## Next Steps

1. [ ] Complete OpenOSINT Aras Integrasi API integration
2. [ ] Test full collection pipeline (collection → entities → sentiment → brief)
3. [ ] Scrape SPR data for 2023 election results (all 36 DUN)
4. [ ] Deploy browser automation for candidate nomination tracking (18 July)
5. [ ] Generate first Daily Command Brief (baseline assessment)
6. [ ] Identify priority DUNs for immediate profiling (Week 2)
7. [ ] Establish stakeholder database (Undangs, influencers, community leaders)

---

## Contact & Support

**Workspace:** `/home/p62operator/.openclaw/workspace-ns/`  
**Classification:** TLP:AMBER  
**GitHub:** Private repository (sensitive intelligence)  
**Infrastructure:** Self-hosted (DeerFlow, Firecrawl, SearXNG, OpenOSINT)

**Parallel Workstream:** PRN Johor 2026 (`/home/p62operator/.openclaw/workspace-hoi/`)

---

**Framework Version:** 1.0  
**Created:** 2026-07-10  
**Last Updated:** 2026-07-10
