# Entity Extraction Log — 20260713

**Classification:** TLP:AMBER
**Workspace:** `/home/p62operator/.openclaw/workspace-ns/`
**Collection:** `intelligence/raw/20260713` (7 source files, 53.8% collection success rate)
**Script:** `scripts/ns-entity-extraction.sh`

---

## 1. Script Execution

- **Exit code:** 0 (success)
- **Sources processed:** 7
- **Output directory:** `intelligence/processed/20260713/`
- All 7 category files generated: politicians, parties, constituencies, issues, events, organizations, locations
- Consolidated file generated: `entities_consolidated.json`

## 2. Script Raw Output — Entity Counts

| Category | Script Count |
|---|---|
| Politicians | 0 |
| Parties | 12 |
| Constituencies | 1 |
| Issues | 0 |
| Events | 0 |
| Organizations | 0 |
| Locations | 0 |
| **Total** | **13** |

## 3. CVS Standard Compliance Audit — FAIL

The CVS standard requires: *All extracted entities must be source-attributed. No pattern-inferred entities.*

### 3.1 Pattern-Inferred False Positives (2 of 13 entities)

| Entity (script) | Actual Match | Verdict |
|---|---|---|
| `bersatu` | "kita semua **bersatu** untuk menikmati hidangan KFC" (ohbulan line 93) | Malay verb "to unite" — NOT Bersatu party. **FALSE POSITIVE** (3rd consecutive day) |
| `DUN bukan` | "BN Johor perlu buktikan kuasai 48 **DUN bukan** 'cek kosong'" (bharian line 27) | Malformed regex grab — "DUN bukan" is not a constituency. **FALSE POSITIVE** |

### 3.2 Case-Variant Duplication

12 raw party entries are case-variant duplicates of 4 unique strings + 1 false positive:
- `umno` / `UMNO` / `Umno` → UMNO (legitimate)
- `bn` / `BN` / `Barisan Nasional` → BN (legitimate)
- `PAS` / `Pas` / `pas` → PAS (legitimate)
- `pn` / `PN` → PN (legitimate but non-NS, from kosmo 404 headline about Johor)
- `bersatu` → false positive (see above)

### 3.3 Missing Source Attribution

No entity in any script output file carries a source reference. Entities are bare strings.

### 3.4 Categories With No Extraction Logic (5 of 7)

The script contains extraction regex ONLY for `parties` and `constituencies`. Politicians, issues, events, organizations, and locations have **zero extraction logic** and will always return 0 regardless of content.

**Verdict:** Script output is NON-COMPLIANT with CVS standard.

## 4. Corrected CVS-Compliant Extraction (Manual, Source-Attributed)

A verified, source-attributed extraction was performed by reading the actual collected content. Saved to:
`intelligence/processed/20260713/entities_verified_cvs_compliant.json`

| Category | Verified Count | NS-Relevant | NS-Election-Relevant |
|---|---|---|---|
| Politicians | 5 | 2 | 2 |
| Parties | 4 | 3 | 3 |
| Constituencies | 1 | 0 | 0 |
| Issues | 21 | 6 | 5 |
| Events | 11 | 2 | 1 |
| Organizations | 20 | 1 | 0 |
| Locations | 21 | 5 | 1 |
| **Total** | **83** | **19** | **12** |

Every entity includes: name, source file, context snippet, and NS-relevance flag. No pattern inference.

## 5. BREAKTHROUGH — First NS PRN 2026 Election Content Found

After **two consecutive days** (20260711, 20260712) with **zero** NS PRN election content, the 20260713 collection contains **significant** Negeri Sembilan PRN 2026 election intelligence.

### Key NS PRN Articles Found (3 sources, 5 articles)

1. **thestar** — "Negri polls: PAS in talks with Umno for political cooperation, claims Abdul Hadi"
   - SEREMBAN dateline; Tan Sri Abdul Hadi Awang claims PAS-Umno talks for Aug 1 NS polls
2. **thestar** — "Hard work won't stop at Johor"
   - SEREMBAN dateline; Datuk Seri Jalaluddin Alias says BN Johor victory boosts morale for NS
3. **thestar** — "Analysts: Johor sweep no guarantee of domino effect"
   - Analysts caution Johor results won't predict NS PRN or GE16 outcomes
4. **astroawani** — "PRN Negeri Sembilan: Pas akui berunding dengan BN"
   - PAS admits negotiating with BN for NS PRN; 1 Ogos (Aug 1)
5. **bharian** — "PAS buka ruang UMNO teraju Negeri Sembilan jika menang PRN"
   - PAS offers UMNO to lead Negeri Sembilan if coalition wins PRN

### Key Political Dynamics Emerging

- **PAS-BN/UMNO electoral cooperation** for NS PRN (Aug 1, 2026) — confirmed by multiple sources
- **PAS offering UMNO the NS state government** if coalition wins — major strategic concession
- **BN Johor victory as momentum narrative** for NS — Jalaluddin Alias optimistic
- **Analyst caution** — Johor sweep won't guarantee domino effect in NS or GE16
- The Star maintains dedicated **"Negri Crisis"** and **"State Polls 2026"** topic tags

### NS-Election-Relevant Entities (12)

| # | Entity | Category | Source |
|---|---|---|---|
| 1 | Tan Sri Abdul Hadi Awang | Politicians | thestar |
| 2 | Datuk Seri Jalaluddin Alias | Politicians | thestar |
| 3 | PAS | Parties | thestar, astroawani, bharian |
| 4 | UMNO | Parties | thestar, bharian |
| 5 | Barisan Nasional (BN) | Parties | thestar, astroawani, bharian |
| 6 | PAS-Umno cooperation for NS PRN | Issues | thestar, astroawani |
| 7 | PAS offers UMNO NS leadership | Issues | bharian |
| 8 | BN Johor momentum for NS | Issues | thestar |
| 9 | Johor domino effect on NS/GE16 | Issues | thestar |
| 10 | Negri Crisis (topic tag) | Issues | thestar |
| 11 | PRN Negeri Sembilan 2026 (Aug 1) | Events | thestar, astroawani, bharian |
| 12 | Seremban (dateline) | Locations | thestar, astroawani |

### Non-Political Persons Found (20, excluded from politicians)

Gianni Infantino (FIFA), Lindsey Graham (US Senator), Conor McGregor, Max Holloway (UFC), Bella Astillah (celebrity), Pavithra Charles (health story), Waris, Suki Low, Nabil Ahmad, Aeril Zafrel, Wawa Zainal (entertainers), Rooney, Mbappe, Messi, Bellingham, Tuchel, Haaland, Sorloth (football), Mark Wahlberg (actor), Rahim Maarof (singer).

## 6. Sentiment Analysis Readiness — READY ✓

| Criterion | Status |
|---|---|
| Entities extracted | Yes (83 verified, 12 NS-election-relevant) |
| Source attribution | Yes (in verified file) |
| NS PRN 2026 content present | **YES** (first day) |
| Ready for NS sentiment analysis | **YES** |

### Recommended Sentiment Analysis Targets

1. PAS-BN/UMNO cooperation narrative (positive/negative framing across sources)
2. BN Johor victory momentum transfer to NS (optimism vs caution)
3. PAS offering UMNO NS leadership (strategic concession vs weakness)
4. Analysts' domino effect caution (skepticism toward Johor predicting NS)
5. Abdul Hadi Awang statements (credibility and reception)
6. Jalaluddin Alias BN momentum claims (confidence vs overconfidence)

## 7. Source Quality

| Metric | Value |
|---|---|
| Total files | 7 |
| Substantive content | 2 (thestar, astroawani) |
| Partial content (headlines only) | 1 (bharian — trending headlines incl. NS-relevant) |
| 404/minimal pages | 4 (kosmo, mstar, ohbulan, utusan) |
| NS-specific files | 3 (thestar, astroawani, bharian) |
| Collection success rate | 53.8% (7/13 attempted) |
| Dominant topic | NS PRN 2026 (PAS-BN cooperation) + Johor PRN aftermath |

### Improvement vs Previous Days

| Date | Total Files | NS-Election Entities | Sentiment Ready |
|---|---|---|---|
| 20260711 | 10 | 0 | NO |
| 20260712 | 9 | 0 | NO |
| **20260713** | **7** | **12** | **YES** |

The Star has emerged as the primary NS PRN source (4 articles with full prose), with Astro Awani and Berita Harian providing complementary coverage.

## 8. Output Files

```
intelligence/processed/20260713/
├── entities_politicians.json           (5 entities, source-attributed)
├── entities_parties.json                (4 entities, source-attributed)
├── entities_constituencies.json         (1 entity, source-attributed)
├── entities_issues.json                 (21 entities, source-attributed)
├── entities_events.json                 (11 entities, source-attributed)
├── entities_organizations.json          (20 entities, source-attributed)
├── entities_locations.json              (21 entities, source-attributed)
├── entities_consolidated.json           (CVS-compliant summary)
└── entities_verified_cvs_compliant.json (MASTER: full audit + all entities)
```

---

*Log generated: 2026-07-13 by NS Entity Extraction Agent (cron).*
*TLP:AMBER — All extracted entities source-attributed. No pattern-inferred entities.*
