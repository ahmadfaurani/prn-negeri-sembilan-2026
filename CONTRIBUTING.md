# Contributing Guidelines — PRN Negeri Sembilan 2026 Intelligence Workspace

**Classification:** TLP:AMBER  
**Repository:** HCR-095  
**Last Updated:** 2026-07-18

---

## 1. Purpose

This workspace collects, processes, and produces political intelligence for the PRN Negeri Sembilan 2026 state election. All contributions must follow the established taxonomy, verification framework, and classification standards.

---

## 2. Directory Taxonomy

| Directory | Purpose | Content Type |
|-----------|---------|--------------|
| `00-OPERATIONS/` | Frameworks, PIRs, master lists, escalation register | Markdown |
| `01-DAILY-INTELLIGENCE/` | Daily briefs, sitreps | Markdown |
| `02-CONSTITUENCY-INTELLIGENCE/` | 36 DUN constituency profiles | Markdown |
| `03-VERIFICATION/` | CVS framework, source register, verification log | Markdown |
| `04-DATA-AND-SOURCES/` | Raw scrapes, processed entities, SPR data | JSON, Markdown, CSV |
| `05-TOOLS-AND-AUTOMATION/` | Scripts, templates | Python, Bash, Markdown |
| `06-INFRASTRUCTURE/` | Collection/processing logs | Log files (gitignored) |
| `07-AUDIT/` | Deployment summaries, audit trails | Markdown |

---

## 3. File Naming Conventions

### Daily Briefs
```
01-DAILY-INTELLIGENCE/daily-briefs/PRN-NS-DAILY-YYYY-MM-DD.md
```

### Nomination Day Hourly Briefs
```
01-DAILY-INTELLIGENCE/daily-briefs/PRN-NS-NOMINATION-YYYYMMDD-HHMM.md
```

### Sitreps
```
01-DAILY-INTELLIGENCE/sitreps/pir-ns-XX-description-YYYYMMDD.md
```

### Constituency Profiles
```
02-CONSTITUENCY-INTELLIGENCE/constituency-profiles/NXX-NAME-analysis.md
```

### Raw Scrapes
```
04-DATA-AND-SOURCES/raw-scrapes/YYYYMMDD/source-name_YYYYMMDD_HHMMSS.md
```

### Processed Entities
```
04-DATA-AND-SOURCES/processed-entities/YYYYMMDD/entities_category.json
```

---

## 4. Verification Requirements

- **Every claim** must have a source URL
- **T1 (CONFIRMED):** Multiple sources or official — stated as fact
- **T2 (UNVERIFIED):** Single source — tag `[UNVERIFIED]`, await corroboration
- **T3 (EXCLUDED):** Rumour/unverified — log only, never include in products
- **Assessments** must be tagged `[ASSESSMENT]`
- See `03-VERIFICATION/cvs-framework.md` for full methodology

---

## 5. Git Commit Conventions

### Commit Message Format
```
<type>: <description>
```

### Types
- `intel:` — New intelligence product (brief, sitrep, analysis)
- `data:` — New raw data or processed entities
- `ops:` — Operational changes (PIR framework, escalation register)
- `fix:` — Bug fix or correction
- `auto:` — Automated cronjob sync
- `docs:` — Documentation (README, CONTRIBUTING, templates)

### Examples
```
intel: Nomination Day PIR-01 verified — SPR candidate list processed
ops: Add ESC-011, reopen ESC-006, upgrade ESC-010
data: 18 Jul collection cycle — 13 sources scraped
auto: Git sync 18 Jul 08:09 — entity extraction + sentiment
```

---

## 6. Classification

- All products are **TLP:AMBER**
- No PII (IC numbers, phone numbers, home addresses) in committed files
- SPR data: IC numbers masked in committed JSON
- Source URLs are required but do not constitute PII

---

## 7. PIR Framework Compliance

All intelligence products must reference the relevant PIR:
- **Standard framework:** NS-01 to NS-18 (see `00-OPERATIONS/pir-framework.md`)
- **Nomination Day:** PIR-01 to PIR-25 (see `00-OPERATIONS/pir-framework-nomination-day.md`)

Each brief must state which PIRs are addressed in the product.

---

## 8. Automation Pipeline

The workspace is maintained by 5 automated cronjobs:

| Job | Purpose | Output |
|-----|---------|--------|
| News Collection | Scrape 13 Malaysian news sources | `04-DATA-AND-SOURCES/raw-scrapes/` |
| Entity Extraction | Extract political entities | `04-DATA-AND-SOURCES/processed-entities/` |
| Sentiment Analysis | Analyze sentiment trends | `04-DATA-AND-SOURCES/processed-entities/` |
| Intelligence Brief | Generate and deliver brief | `01-DAILY-INTELLIGENCE/daily-briefs/` + Telegram |
| Git Sync | Commit and push changes | GitHub repository |

Manual contributions should not conflict with automated outputs. When editing a file that cronjobs modify, coordinate timing to avoid merge conflicts.

---

## 9. Quality Standards

- **Fact/inference separation:** Facts tagged with source; inferences tagged `[ASSESSMENT]`
- **Source URL tracking:** Every claim must include `**Source:** [Name], [URL], [Date]`
- **Escalation flags:** All flags tracked in `00-OPERATIONS/escalation-register.md`
- **Verification log:** T2/T3 claims logged in `03-VERIFICATION/verification-status.md`
- **No fabrication:** If information is unavailable, state so explicitly

---

**Workspace:** `/home/p62operator/.openclaw/workspace-ns/`  
**Classification:** TLP:AMBER
