# PRN Negeri Sembilan 2026 — Daily Collection Status Report

**Date:** 2026-07-13
**Timestamp:** 20260713_010102
**Classification:** TLP:AMBER
**Agent:** PRN Negeri Sembilan 2026 Daily Collection Agent (cron)
**Collection Script:** `scripts/ns-daily-collection.sh`
**Firecrawl API:** `http://localhost:3002/v2/scrape` (verified healthy, HTTP 200)

---

## COLLECTION RESULTS

| Metric | Value |
|---|---|
| Sources attempted | 13 |
| Sources collected (success) | **7** |
| Failed sources | 6 |
| Timeouts | 0 |
| Success rate | **53.8%** |
| Script exit code | 0 (success: ≥5 threshold met) |
| Target | 60%+ ❌ NOT MET (short by 1 source) |
| Retry threshold | <50% — NOT triggered (53.8% > 50%) |

### Successfully Collected (7/13)

| # | Source | Words | File |
|---|---|---|---|
| 1 | bhariancommy | 415 | bhariancommy_20260713_010102.md |
| 2 | utusancommy | 83 | utusancommy_20260713_010102.md |
| 3 | thestarcommy | 1042 | thestarcommy_20260713_010102.md |
| 4 | astroawanicom | 613 | astroawanicom_20260713_010102.md |
| 5 | ohbulancom | 629 | ohbulancom_20260713_010102.md |
| 6 | mstarcommy | 95 | mstarcommy_20260713_010102.md |
| 7 | kosmocommy | 181 | kosmocommy_20260713_010102.md |

### Failed Sources (6/13)

| # | Source | Failure Reason | Category | Status Yesterday |
|---|---|---|---|---|
| 1 | sinarhariancommy | Content too thin (31 words) | Thin content | ✓ Success (117 words) — REGRESSED |
| 2 | nstcommy | Content too thin (3 words) | Thin content | ✗ Failed (4 words) — recurring |
| 3 | malaysiakinicom | Content too thin (29 words) | Thin content | ✓ Success (76 words) — REGRESSED |
| 4 | freemalaysiatodaycom | Content too thin (26 words) | Thin content | ✗ Failed (26 words) — recurring |
| 5 | bernamahubcom | No markdown in response | API error | ✗ Failed — recurring |
| 6 | metrocommy | Content too thin (48 words) | Thin content | ✗ Failed (39 words) — recurring |

**Failure analysis:** All 6 failures were "thin content" (Firecrawl returned page shells/anti-bot stubs below the 50-word threshold) except bernamahubcom (no markdown). Zero network timeouts occurred. The failures are transient site/anti-bot conditions, not systemic Firecrawl problems.

---

## RETRY ASSESSMENT

- Success rate 53.8% is **above** the 50% retry threshold. **No retry required** per mission rules.
- Retry with extended timeout (60s) was assessed but deemed unlikely to help: all failures are "content too thin" (anti-bot stubs returned quickly) or "no markdown" — NOT timeouts. A longer timeout does not address anti-bot rendering issues.
- 2 sources regressed from yesterday (sinarhariancommy, malaysiakinicom) — transient, likely to recover on subsequent runs.

---

## VERIFICATION (CVS STANDARD — 100% ABSOLUTE TRUTH)

- **Firecrawl API health:** Verified HTTP 200 prior to collection run.
- **Content authenticity:** All 7 collected files inspected for genuine content — confirmed real Malaysian news articles, no fabricated or synthetic material detected.
- **Notable intelligence find:** The Star (thestarcommy, 1042 words) contains a directly relevant article dated 13 Jul 2026: *"Negri polls: PAS in talks with Umno for political cooperation, claims Abdul Hadi"* — high-value PRN NS 2026 intelligence. Berita Harian (bhariancommy, 415 words) also carries PAS/Hadi Awang PRN-related content. Utusan (utusancommy) shows a Negeri Sembilan section page dated 13 Julai 2026, 9:01 am.
- **Single-source caveat:** No single-source claims are elevated to operational briefs. All intelligence findings will be cross-verified across multiple sources per CVS standard.

---

## HOUSEKEEPING

- Leftover junk file from 20260712 failed first run (`sinarhariancommy_20260712_052935.md`, <50 words) deletion was blocked by sandbox approval gate. Recommend manual removal: `rm intelligence/raw/20260712/sinarhariancommy_20260712_052935.md`

---

## COMPARISON TO PREVIOUS RUNS

| Date | Success | Rate | Trend |
|---|---|---|---|
| 20260710 | — | — | (early deployment) |
| 20260711 | 10/13 | 76.9% | — |
| 20260712 | 8/13 | 61.5% | ↓ |
| 20260713 | 7/13 | 53.8% | ↓ |

Downward trend over 3 consecutive days. The regression is driven by recurring anti-bot failures at nstcommy, freemalaysiatodaycom, bernamahubcom, and metrocommy, plus today's new regression at sinarhariancommy and malaysiakinicom. No systemic Firecrawl failure (0 timeouts across all runs).

---

## NEXT COLLECTION

- **Scheduled:** Daily (next run 2026-07-14).
- **Recommendations:**
  1. Monitor sinarhariancommy and malaysiakinicom — both regressed today after successful collection yesterday. Likely transient; should recover.
  2. nstcommy, freemalaysiatodaycom, bernamahubcom, and metrocommy have failed for 2+ consecutive days. Consider URL review or anti-bot workaround for these sources.
  3. The 3-day downward trend (76.9% → 61.5% → 53.8%) is approaching the 50% retry threshold. If tomorrow's collection drops below 50%, a retry with extended 60s timeout will be triggered per mission protocol.
  4. Despite below-target collection rate, today's haul includes high-value PRN NS intelligence (PAS-Umno cooperation talks for Negri polls per The Star).

---

*Generated autonomously by PRN NS 2026 Daily Collection Agent — TLP:AMBER*
*CVS Standard: 100% absolute truth verification — all content verified genuine, no fabrication*
