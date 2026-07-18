# Core Truth Validation (CVS) Framework

**Classification:** TLP:AMBER  
**Created:** 2026-07-10  
**Last Updated:** 2026-07-18  
**Applies to:** All intelligence products in this workspace

---

## 1. Purpose

The CVS framework ensures every intelligence claim in this workspace meets a minimum verification standard before inclusion in any brief, sitrep, or analysis product. No claim appears in a disseminated product without a confidence rating and source attribution.

---

## 2. Verification Tiers

| Tier | Label | Criteria | Usage |
|------|-------|----------|-------|
| **T1** | CONFIRMED | Multiple independent sources agree OR official source (SPR, EC, government gazette, party Sec-Gen statement) | May be stated as fact in briefs |
| **T2** | MEDIUM-CONFIDENCE | Single credible source (mainstream news, named journalist, verified social media account) | Stated with attribution; tag `[UNVERIFIED]` if not independently corroborated within 24h |
| **T3** | EXCLUDED | Rumour, anonymous source, or uncorroborated social media | Not included in briefs. Logged in verification status for tracking only. |

---

## 3. Source Reliability Ratings

| Rating | Source Type | Examples |
|--------|-------------|----------|
| **A** | Official/Government | SPR, Election Commission, Registrar of Societies, government gazettes |
| **B** | Major mainstream media | Sinar Harian, The Star, NST, Astro Awani, Bernama, Utusan, Bharian |
| **C** | Independent/alternative media | Malaysiakini, Free Malaysia Today, MalaysiaNow |
| **D** | Social media (verified accounts) | Verified Twitter/FB accounts of politicians, party official accounts |
| **E** | Social media (unverified) | Anonymous accounts, WhatsApp forwards, blog posts |
| **F** | OSINT/Aggregate | Aggregated from multiple sources, no single authoritative origin |

Source reliability is re-assessed every 7 days. Sources that demonstrate consistent accuracy are upgraded; sources with repeated errors are downgraded.

---

## 4. Claim Lifecycle

```
Collection → Raw Claim → Source Assessment → Tier Assignment → Cross-Check → Product Inclusion
    ↓                                    ↓                      ↓
  04-DATA-AND-SOURCES/          verification-status.md      01-DAILY-INTELLIGENCE/
  (raw-scrapes, entities)      (tracking log)              (briefs, sitreps)
```

1. **Collection:** Raw claims scraped from sources → `04-DATA-AND-SOURCES/raw-scrapes/`
2. **Source Assessment:** Source reliability rated A–F
3. **Tier Assignment:** Confidence tier T1/T2/T3 assigned
4. **Cross-Check:** Claim checked against existing intelligence and other sources
5. **Product Inclusion:** T1 claims stated as fact; T2 claims attributed with source; T3 claims excluded

---

## 5. Special Rules

### SPR Official Data
All SPR/EC official data (candidate lists, results, election writ) is automatically **T1 — CONFIRMED**. No cross-check required.

### Party Announcements
Official party statements from Sec-Gen or President are **T1** for the fact that the statement was made. The content of the statement is **T2** until independently verified.

### Social Media
- Verified accounts of named politicians: **T2** for statements made
- Party official accounts: **T2** for announcements
- Unverified accounts: **T3 — EXCLUDED** unless corroborated by B-tier or above

### Rumour and WhatsApp
All WhatsApp forwards, anonymous tips, and unattributed claims are **T3 — EXCLUDED**. Logged in verification status for trend tracking only. Never included in intelligence products.

---

## 6. Tagging Conventions

All intelligence products must use the following tags:

| Tag | Meaning |
|-----|---------|
| `[CONFIRMED]` | T1 — multiple sources or official |
| `[UNVERIFIED]` | T2 — single source, not yet corroborated |
| `[ASSESSMENT]` | Analytical judgment, not a fact claim |
| `[EXCLUDED]` | T3 — logged but not used in products |
| `[SOURCE: URL]` | Source URL for the claim |

---

## 7. Audit Trail

Every brief must include a **Sources** section listing all URLs referenced. Entity extraction outputs must include source URLs. The verification status log (`03-VERIFICATION/verification-status.md`) tracks all T2 claims awaiting corroboration and T3 claims logged for exclusion.

---

**Workspace:** `/home/p62operator/.openclaw/workspace-ns/`  
**Classification:** TLP:AMBER
