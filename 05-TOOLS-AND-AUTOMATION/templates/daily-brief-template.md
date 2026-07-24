# PRN Negeri Sembilan 2026 — Intelligence Brief Template
## STANDARD FORMAT (all phases)

**Effective:** 2026-07-24  
**Applies to:** All Daily Intelligence Briefs (Pre-Campaign, Nomination Day, Campaign Period)  
**Cronjob:** `b8f69d6f990d` — PRN Negeri Sembilan 2026 - Daily Intelligence Brief

---

## FILENAME CONVENTION

```
PRN-NS-{PHASE}-YYYYMMDD{-HHMM}.md
```

| Phase | Pattern | Example | Schedule |
|-------|---------|---------|----------|
| Pre-Campaign | `PRN-NS-PRE-YYYYMMDD.md` | `PRN-NS-PRE-20260710.md` | Daily 09:00 MYT |
| Nomination Day | `PRN-NS-NOMINATION-YYYYMMDD-HHMM.md` | `PRN-NS-NOMINATION-20260718-1518.md` | Hourly surge |
| Campaign Period | `PRN-NS-CAMPAIGN-YYYYMMDD-HHMM.md` | `PRN-NS-CAMPAIGN-20260724-1211.md` | 2x daily 12:00/21:00 MYT |

---

## STANDARD HEADER BLOCK (mandatory)

Every brief MUST begin with this exact header structure:

```markdown
# PRN Negeri Sembilan 2026 — Intelligence Brief
## {Phase} | {Day Label} | TLP:AMBER

**Brief ID:** {FILENAME without .md}
**Generated:** YYYY-MM-DD HH:MM +08
**Classification:** TLP:AMBER — For official use only, distribution controlled
**Phase:** {Pre-Campaign | Nomination Day Surge | Campaign Period}
**Election Date:** 1 August 2026
**Nomination Day:** 18 July 2026
**Polling Day:** 1 August 2026
**Distribution:** State Campaign Leadership, DUN War Rooms

---
```

### Day Label by Phase

| Phase | Day Label Format | Example |
|-------|-----------------|---------|
| Pre-Campaign | `Day {N} of Pre-Campaign` | `Day 1 of Pre-Campaign` |
| Nomination Day | `Day {N} of 14` | `Day 1 of 14` |
| Campaign Period | `Day {N} of 14` | `Day 7 of 14` |

**Campaign Day Calculation:** Day 1 = 18 July 2026 (Nomination Day). Campaign period = 14 days (18–31 Jul).

---

## STANDARD SECTION STRUCTURE

### Campaign Period (current, most evolved)

```markdown
## 1. EXECUTIVE FLASH
  (3–5 numbered key developments, 2–3 sentences each, with source attribution)

## 2. PIR-06 UPDATE — Coalition Operational Arrangement [CRITICAL]
  (BN-PN cooperation, Bersatu rupture, seat allocation, joint machinery)

## 3. PIR-07 UPDATE — Highest-Priority NS Battlegrounds
  (T1 seat dynamics, ceramah coverage, candidate messaging, momentum shifts)
  (Incorporate Campaign Trail CT-01 events, CT-05 momentum, CT-07 multi-cornered)

## 4. PIR-16 UPDATE — Campaign Narrative Evolution [ELEVATED]
  (Amplifying vs fading narratives, manifesto messaging, media framing)

## 5. CANDIDATE ALERTS
  (Candidate-level developments, statements, incidents — from Campaign Trail reports)

## 6. COALITION OPS — Machinery Status and Posture
  (Ground operations, markas activity, resource deployment)

## 7. ESCALATION — Triggered Flags This Cycle
  (ESC-XXX status changes, new escalations, resolution of existing flags)

## 8. SENTIMENT ALERTS — Sharp Shifts
  (Entity-level sentiment changes, media tone analysis)

## 9. NEXT CYCLE PRIORITIES
  (Collection requirements, intelligence gaps, focus areas for next cycle)

## 10. 🔴 TOP 3 HIGH-IMPACT PIR — FOR APPROVAL (REQUIRED)
  (3 PIR items requiring director decision, each with recommended action)

## Sources
  (Numbered source list with URLs)
```

### Nomination Day Surge

Same header + sections 1–4, plus:
- `## 2. 36-DUN CANDIDATE ROLL (PIR-01)`
- `## 3. CONTEST CONFIGURATION MAP (PIR-04)`
- `## 4. COALITION OPERATIONAL ARRANGEMENTS (PIR-06)`
- `## 5. BATTLEGROUND ASSESSMENT (PIR-07)`
- `## 6. CANDIDATE ALERTS`
- `## 7. GRASSROOTS ACCEPTANCE MATRIX (PIR-12)`
- `## 8. NARRATIVE & SENTIMENT DASHBOARD (PIR-16/17)`
- `## 9. SECURITY, MISINFORMATION & LEGAL REGISTER (PIR-18/20/21)`
- `## 10. ESCALATION TRIGGERS — STATUS CHECK`
- `## 11. NEXT-HOUR COLLECTION PRIORITIES`
- `## 12. 🔴 TOP 3 HIGH-IMPACT PIR — FOR APPROVAL (REQUIRED)`

### Pre-Campaign

Same header + sections 1–4, plus:
- `## 1. Executive Summary`
- `## 2. Statewide Seat Position`
- `## 3. Critical DUN Updates`
- `## 4. Top Voter Issues & Narratives`
- `## 5. Opposition Movements`
- `## 6. Machinery Readiness Gaps`
- `## 7. Escalation Triggers`
- `## 8. Recommended Decisions`
- `## Appendix: Data Confidence`

---

## FORMATTING RULES

1. **Source attribution:** Every factual claim must have `[Source Name]` or `[Source Name, URL]` in-line
2. **Classification:** All briefs are TLP:AMBER — no exceptions
3. **Em dashes (—):** Use em dashes in section titles and subtitles, not hyphens
4. **Section numbering:** Numbered sequentially starting at 1, no gaps
5. **PIR references:** Use `PIR-XX` format (e.g., PIR-06, PIR-07, not PIR6 or PIR-6)
6. **DUN references:** Use `N.XX` format (e.g., N.14 Ampangan, not N14 or N14 Ampangan)
7. **Escalation flags:** Use `ESC-XXX` format with status indicator (🟢 🟡 🔴)
8. **Confidence markers:** Use `[CONFIRMED]`, `[UNVERIFIED]`, `[ASSESSMENT]` tags
9. **Campaign Trail integration:** Briefs MUST reference Campaign Trail reports when available
10. **Sources section:** All URLs listed at the bottom, numbered

---

## CAMPAIGN TRAIL INTEGRATION

Before generating a Campaign Period brief, the agent MUST:
1. Read the latest Campaign Trail report from `02-CONSTITUENCY-INTELLIGENCE/campaign-trails/YYYYMMDD/`
2. Incorporate CT-01 events into PIR-07 Battleground Matrix
3. Incorporate CT-04 statements into Candidate Alerts
4. Incorporate CT-05 momentum shifts into PIR-07 (flag as momentum change)
5. Incorporate CT-07 multi-cornered dynamics into PIR-06 coalition analysis
6. Incorporate CT-03 incidents into Escalation section

---

*Template version: 2.0 | Updated: 2026-07-24 | TLP:AMBER*
