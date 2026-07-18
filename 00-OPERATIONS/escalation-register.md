# PRN Negeri Sembilan 2026 — Escalation Register

**Classification:** TLP:AMBER  
**Created:** 2026-07-10  
**Last Updated:** 2026-07-18 (Nomination Day)  
**Live Document:** Updated with each intelligence cycle

---

## Active Escalation Flags

| ESC ID | Description | Status | Severity | First Raised | Last Updated | Source |
|--------|-------------|--------|----------|--------------|--------------|--------|
| ESC-002 | Sentiment pipeline non-operational (Aras API not wired) | Active | HIGH | 10 Jul | 17 Jul (Day 7) | Daily brief — ongoing |
| ESC-003 | Royal issue sensitivity — indirectly confirmed | Active | MEDIUM | 15 Jul | 17 Jul | Daily brief |
| ESC-006 | Opposition unity disruption | **REOPENED** | **CRITICAL** | 15 Jul | 18 Jul | SPR candidate list — BERSATU 24 independent candidates |
| ESC-007 | PH Malay seats quantified and threatened | Downgraded | MEDIUM | 16 Jul | 18 Jul | SPR data shows opposition fragmented, not consolidated |
| ESC-009 | BN-PN electoral pact | Downgraded | MEDIUM | 17 Jul | 18 Jul | Pact is BN-PAS only, not BN-PN(Bersatu) |
| ESC-010 | PN internal friction (Muhyiddin vs Samsuri) | **UPGRADED** | **CRITICAL** | 17 Jul | 18 Jul | Materialised into formal electoral split — BERSATU vs PN in 8 DUNs |
| ESC-011 | BERSATU 24-candidate independent deployment | **NEW** | **CRITICAL** | 18 Jul | 18 Jul | SPR official candidate list |

---

## Resolved Flags

| ESC ID | Description | Resolved | Resolution |
|--------|-------------|---------|------------|
| ESC-006 | Opposition unity disruption | Was RESOLVED on 17 Jul → **REOPENED on 18 Jul** | 17 Jul: BN-PN pact reported as unity. 18 Jul: SPR data shows BERSATU excluded, 4-way split. |
| ESC-008 | PH first-mover advantage | 17 Jul | Neutralised by opposition matching 36-candidate slate in 48h. (Note: now further complicated by 4-way split.) |

---

## Escalation Trigger Checklist (Nomination Day PIR Framework)

Immediately escalate if ANY of the following are detected:

- [x] Candidate rejection or unexpected withdrawal in priority DUN — **CONFIRMED: BERSATU excluded from PN pact, running independently**
- [x] Unannounced alliance, seat concession or reciprocal-support arrangement — **CONFIRMED: BN-PAS pact (not BN-PN as reported)**
- [ ] Grassroots boycott involving divisional or branch leadership
- [ ] Security incident involving candidates or senior political leaders
- [ ] Viral allegation capable of materially damaging candidate credibility
- [ ] Confirmed coordinated misinformation targeting election administration
- [x] Independent candidate capable of splitting the decisive voter segment — **4 independents in N.10 and N.33**
- [x] Candidate deployment that fundamentally changes the projected state majority — **4-way opposition split changes all projections**

---

## Flag History

### ESC-011 (NEW — CRITICAL)
- **18 Jul:** BERSATU confirmed running 24 candidates independently. SPR data shows BERSATU separate from PN (11). In 8 DUNs, BERSATU and PN directly compete. Opposition is 4-way split: PH (36) vs BN (25) vs BERSATU (24) vs PN (11). This invalidates the 17 Jul "opposition unity" assessment.

### ESC-010 (UPGRADED to CRITICAL)
- **17 Jul (MEDIUM):** PN Chairman Ahmad Samsuri (PAS) publicly rebutted Bersatu President Muhyiddin's claim as "tidak berasas" (baseless). PAS-Bersatu tension within PN.
- **18 Jul (CRITICAL):** Friction has materialised into a formal electoral split. BERSATU running independently. 8 DUNs have direct BERSATU vs PN competition.

### ESC-009 (DOWNGRADED to MEDIUM)
- **17 Jul (HIGH):** BN-PN electoral pact confirmed. Opposition full mobilisation. 25 BN + 11 PN = 36 candidates matching PH.
- **18 Jul (MEDIUM):** Pact is BN-PAS only, not BN-PN(Bersatu). Smaller scope than assessed. Bersatu's 24 independent candidates create a 3-way opposition split in 21 DUNs.

### ESC-007 (DOWNGRADED to MEDIUM)
- **16 Jul (HIGH):** PH Malay seats quantified — 4 of 23 Malay-majority seats. Directly threatened by BN-PN consolidation.
- **18 Jul (MEDIUM):** PH Malay seat vulnerability is REDUCED by BERSATU-PN split. The opposition vote is fragmented, not consolidated. PH may actually benefit from the split.

### ESC-006 (REOPENED — CRITICAL)
- **15 Jul (raised):** Opposition unity disruption — "jual mahal" narrative.
- **17 Jul (RESOLVED):** BN-PN pact overcomes disruption. Opposition unity achieved.
- **18 Jul (REOPENED):** SPR data shows BERSATU excluded from pact. 4-way split confirmed. Opposition is NOT unified.

### ESC-008 (RESOLVED)
- **15 Jul (raised):** PH first-mover advantage — campaign launch on 15 Jul.
- **17 Jul (resolved):** Neutralised — opposition matched 36-candidate slate in 48h.

### ESC-003 (MEDIUM — Active)
- **15 Jul (raised):** Royal issue sensitivity — indirectly confirmed through campaign messaging. No direct royal intervention reported.

### ESC-002 (HIGH — Active)
- **10 Jul (raised):** OpenOSINT/Aras sentiment API not wired. Day 7 of non-operation. Manual sentiment analysis used as fallback in daily briefs.

---

## Escalation Severity Definitions

| Severity | Definition | Action |
|----------|------------|--------|
| **CRITICAL** | Fundamental change to electoral calculus or security threat | Immediate Telegram notification + war room activation |
| **HIGH** | Material threat to electoral position or operational gap | Priority briefing + remediation plan |
| **MEDIUM** | Monitored development requiring tracking | Daily brief inclusion + watch |
| **LOW** | Minor development, no immediate action | Log for trend analysis |

---

**Workspace:** `/home/p62operator/.openclaw/workspace-ns/`  
**Classification:** TLP:AMBER  
**Authority:** State Intelligence Director
