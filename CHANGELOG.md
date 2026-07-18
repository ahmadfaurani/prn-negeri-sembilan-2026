# Changelog — PRN Negeri Sembilan 2026

**Classification:** TLP:AMBER  
**Repository:** HCR-095

All notable changes to this intelligence workspace are documented here.  
Format: `[YYYY-MM-DD] [type] Description — commit <hash>`

---

## [2026-07-18] — Nomination Day

### intel
- **PIR-01 Verified Candidate Roll:** Processed SPR official candidate list — 103 candidates across 36 DUNs. **CRITICAL FINDING:** BERSATU running 24 candidates independently of PN. 4-way opposition split confirmed. — commit `2d21595`
- **Nomination Day Hourly Brief 07:16:** First hourly brief of Nomination Day surge mode. — commit pending

### ops
- **Nomination Day Surge Framework:** 25 PIRs (PIR-01 to PIR-25) with 8 command-centre outputs and 8 escalation triggers. — commit `718ca83`
- **Cronjob surge mode:** Collection + Brief to every 60m; Entity + Sentiment + Git Sync to every 120m. — commit `718ca83`
- **Escalation Register:** ESC-011 (NEW — BERSATU independent), ESC-006 (REOPENED), ESC-010 (UPGRADED), ESC-007/009 (DOWNGRADED)

### docs
- **Workspace optimization:** Comprehensive README, CONTRIBUTING, election calendar, escalation register, candidate tracker, CVS framework, source register, verification status, templates (brief, sitrep, nomination-day). .gitignore expanded.
- **Pycache cleanup:** Removed committed `__pycache__` artifacts, updated .gitignore.

### data
- **SPR 2026 Candidate List:** `spr-candidate-list-20260718.json` — 103 candidates, structured JSON
- **Collection cycle 070937:** 13 sources scraped in second daily cycle (surge mode)
- **Entity extraction 20260718:** 8 entity categories extracted

---

## [2026-07-17]

### intel
- **Daily Brief Day 7:** 8 escalation flags active. BN-PN pact confirmed (later invalidated 18 Jul). PN internal friction flagged.
- **Entity extraction:** 8 entity categories + sentiment analysis

### data
- **Collection cycle 010024:** 9 sources scraped

---

## [2026-07-16]

### intel
- **Daily Brief Day 6:** PH Malay seats quantified. Opposition "jual mahal" narrative tracked.
- **Entity extraction:** Enhanced sourced entity extraction with URLs

### data
- **Collection cycle 010506:** 12 sources scraped

---

## [2026-07-15]

### intel
- **Daily Brief Day 5:** PH campaign launch. First-mover advantage flagged (ESC-008).
- **SITREP NS-01:** Statewide position sitrep

### data
- **Collection cycle 010003:** 11 sources scraped including Sinar Harian

---

## [2026-07-14]

### intel
- **Daily Brief Day 4:** Enhanced entity extraction deployed with source URLs
- **Entity extraction:** Sourced entities (entities_* → sourced_entities_*) upgrade

### data
- **Collection cycle 010109:** 10 sources scraped, NST added

---

## [2026-07-13]

### intel
- **Daily Brief Day 3:** Baseline assessment consolidating
- **Entity extraction:** Standard 8-category extraction

### data
- **Collection cycle 010102:** 8 sources scraped

---

## [2026-07-12]

### ops
- **Enhanced entity extraction:** `ns-entity-extraction-enhanced.py` deployed
- **Sourced entity extraction:** `ns_entity_extraction_sourced.py` deployed

### data
- **Collection cycle 053155:** 10 sources scraped
- **Audit:** Collection status and entity extraction logs

---

## [2026-07-11]

### data
- **Collection cycle 010320:** 10 sources scraped — first full multi-source collection
- **Entity extraction:** First entity extraction run

---

## [2026-07-10]

### ops
- **Workspace deployment:** 8-directory taxonomy, PIR framework (18 PIRs), DUN master list, collection/extraction/sentiment/brief scripts
- **GitHub repo created:** `ahmadfaurani/prn-negeri-sembilan-2026` (private, HCR-095)
- **Cronjobs deployed:** 5 cronjobs (collection, extraction, sentiment, brief, git sync)

### data
- **First collection:** Sinar Harian scrape

---

**Workspace:** `/home/p62operator/.openclaw/workspace-ns/`  
**Classification:** TLP:AMBER
