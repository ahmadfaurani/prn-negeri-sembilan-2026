# Entity Extraction Log — 20260711

**Classification:** TLP:AMBER
**Workspace:** `/home/p62operator/.openclaw/workspace-ns/`
**Collection:** `intelligence/raw/20260711` (10 source files, 76.9% collection success rate)
**Script:** `scripts/ns-entity-extraction.sh`

---

## 1. Script Execution

- **Exit code:** 0 (success)
- **Sources processed:** 10
- **Output directory:** `intelligence/processed/20260711/`
- All 7 category files generated: politicians, parties, constituencies, issues, events, organizations, locations
- Consolidated file generated: `entities_consolidated.json`

## 2. Script Raw Output — Entity Counts

| Category | Script Count |
|---|---|
| Politicians | 0 |
| Parties | 3 |
| Constituencies | 1 |
| Issues | 0 |
| Events | 0 |
| Organizations | 0 |
| Locations | 0 |
| **Total** | **4** |

## 3. CVS Standard Compliance Audit — FAIL

The CVS standard requires: *All extracted entities must be source-attributed. No pattern-inferred entities.*

The script violates this standard on multiple counts:

### 3.1 Pattern-Inferred False Positives (3 of 4 entities)

| Entity (script) | Actual Match | Verdict |
|---|---|---|
| `bersatu` | "kita semua **bersatu** untuk menikmati hidangan KFC" (ohbulan) | Malay verb "to unite" — NOT Bersatu party. **FALSE POSITIVE** |
| `bersama` | "beramah mesra **bersama** atlet" (astroawani) | Malay word "together" — no party "Bersama" exists. **FALSE POSITIVE** (bug: invalid party in regex list) |
| `DUN Puteri Wangsa beratur seawal jam` | Greedy regex grab of headline (bharian) | Malformed capture; Puteri Wangsa is a **Johor** DUN, not NS. **FALSE POSITIVE** |
| `umno` | "Umno needs fresh ideas" (freemalaysiatoday) | Legitimate, but **no source attribution recorded** |

### 3.2 Missing Source Attribution
No entity in any script output file carries a source reference. Entities are bare strings.

### 3.3 Categories With No Extraction Logic (5 of 7)
The script contains extraction regex ONLY for `parties` and `constituencies`. Politicians, issues, events, organizations, and locations have **zero extraction logic** and will always return 0 regardless of content.

**Verdict:** Script output is NON-COMPLIANT with CVS standard.

## 4. Corrected CVS-Compliant Extraction (Manual, Source-Attributed)

A verified, source-attributed extraction was performed by reading the actual collected content. Saved to:
`intelligence/processed/20260711/entities_verified_cvs_compliant.json`

| Category | Verified Count |
|---|---|
| Politicians | 9 |
| Parties | 1 |
| Constituencies | 2 |
| Issues | 5 |
| Events | 4 |
| Organizations | 10 |
| Locations | 14 |
| **Total** | **45** |

Every entity includes: name, source file, context snippet, and NS-relevance flag. No pattern inference.

## 5. Critical Finding — No NS PRN 2026 Content

**ZERO entities related to the Negeri Sembilan PRN 2026 (state election) were found in the collection.**

- The collection is dominated by **PRN Johor** (Johor state election polling day, 11 Julai 2026).
- 7 of 10 source files are **404 error pages** or minimal landing pages.
- The only NS-tagged source (ohbulan) contains old (2021–2025) entertainment/lifestyle/royalty articles — no election content.
- None of NS's 36 DUN constituencies appear in any source.
- No Negeri Sembilan state politicians appear in any source.
- Only 6 of 45 verified entities are NS-relevant at all (and none are election-relevant).

### NS-Relevant Entities Found (none election-related)
1. Hari Keputeraan Ke-77 Yang Dipertuan Besar Negeri Sembilan — event, past (Jan 2025), royalty
2. McDonald's Tampin — organization, commercial
3. Negeri Sembilan — location (tag page)
4. Tampin — location, commercial
5. Port Dickson (PD) — location, celebrity gossip

## 6. Sentiment Analysis Readiness — NOT READY

| Criterion | Status |
|---|---|
| Entities extracted | Yes (45 verified, but 0 NS-election-relevant) |
| Source attribution | Yes (in verified file) |
| NS PRN 2026 content present | **NO** |
| Ready for NS sentiment analysis | **NO** |

Running sentiment analysis on the current collection would measure **Johor election** and **World Cup** sentiment, not Negeri Sembilan PRN 2026.

## 7. Root-Cause Recommendation

The collection script (`ns-daily-collection.sh`) is fetching source URLs that return 404 pages and/or Johor-focused landing pages rather than Negeri Sembilan-specific election content. **Collection targeting must be fixed upstream** before useful NS entity extraction or sentiment analysis is possible. Recommend:
1. Audit source URL list in `ns-daily-collection.sh` — many return 404.
2. Add NS-specific search terms / section URLs (e.g. `negeri-sembilan` election pages, NS DUN seat pages).
3. Fix `ns-entity-extraction.sh`: remove invalid "Bersama" party pattern; add extraction logic for the 5 empty categories; add source-attribution to every extracted entity; constrain DUN regex to NS's 36 seats only.

---

*Log generated: 2026-07-11 by NS Entity Extraction Agent (cron).*
