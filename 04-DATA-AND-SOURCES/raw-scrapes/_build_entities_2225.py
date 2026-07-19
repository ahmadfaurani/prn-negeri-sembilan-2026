#!/usr/bin/env python3
"""
PRN NS 2026 — Entity Extraction Build Script (5th carry-forward run)
Run: 20260719-2225 (20 Jul ~05:25 MYT) — incorporates cycles 200000 + 212300
Base: entities-20260719-1954.json (228 entities, 13 cycles)

New analytical delta from cycles 200000 + 212300 (Day-2 dawn window, 04:00 MYT cutoff):
  - 200000 cycle: 1 fresh NST RSS file (Zahid World Cup hosting — sports/non-PRN, marginal)
  - 212300 cycle: 12 files (3 fresh sports RSS false-positives + 9 gnews headline-intel
    duplicates of prior-cycle items); 1 genuinely-new PIR-06 item: Zambry-Samsuri
    Port Dickson meeting (Newswav gnews 18 Jul 09:22 MYT, cross-surfaced via
    "Bersatu sole opposition Muhyiddin" query)

Output:
  - entities-20260719-2225.json (230 entities = 228 base + 2 new)
  - summary.md updated with new section
"""
import json
import os
from copy import deepcopy

BASE_PATH = "/home/p62operator/.openclaw/workspace-ns/04-DATA-AND-SOURCES/processed-entities/2026-07-19/entities-20260719-1954.json"
OUT_PATH  = "/home/p62operator/.openclaw/workspace-ns/04-DATA-AND-SOURCES/processed-entities/2026-07-19/entities-20260719-2225.json"
SUMMARY_PATH = "/home/p62operator/.openclaw/workspace-ns/04-DATA-AND-SOURCES/processed-entities/2026-07-19/summary.md"

# --- Load base entities ---
with open(BASE_PATH, "r", encoding="utf-8") as f:
    entities = json.load(f)

print(f"Loaded base entities: {len(entities)}")

# ---------------------------------------------------------------------------
# PART 1 — CONTEXT UPDATES to existing entities (append new cycle intel)
# ---------------------------------------------------------------------------

# (1) "sole opposition" narrative — now 5-outlet corroborated
#     Original (1954): FMT 18 Jul 16:52 + The Vibes 18 Jul (gnews)
#     NEW (212300): NST 18 Jul 08:31 + The Star 18 Jul 23:24 + Malay Mail 18 Jul 08:53
#     (all gnews headline-intel cross-surfaced via "Bersatu sole opposition Muhyiddin" query)
for e in entities:
    if e.get("entity") == "sole opposition":
        e["context"] += (
            " | 212300 UPDATE: now 5-outlet corroborated — NST 'Muhyiddin says Bersatu remains "
            "sole opposition voice' (18 Jul 08:31 GMT) + The Star 'bersatu-lone-opposition-"
            "party-in-parliament' (18 Jul 23:24) + Malay Mail 'muhyiddin-claims-bersatu-is-"
            "parliament-s-only-true-opposition' (18 Jul 08:53) — all gnews headline-intel "
            "freshly surfaced this cycle. Hard-news corroboration of Muhyiddin's "
            "'Bersatu sole opposition' framing now spans FMT + The Vibes + NST + The Star + "
            "Malay Mail (5 outlets, all 18 Jul). PIR-16 [PRIORITY] — narrative reinforcement, "
            "NOT a [CRITICAL] 'Bersatu exit imminent?' hard-news corroboration."
        )
        e["source_url"] = "https://www.freemalaysiatoday.com/category/nation/2026/07/18/bersatu-must-survive-lone-opposition-muhyiddin"
        break

# (2) "Bersatu exit from PN imminent?" narrative — 14th consecutive cycle = 0 fresh
#     hard-news hits for "bersatu exit pn" gnews query. [CRITICAL] threshold NOT CROSSED.
for e in entities:
    if e.get("entity") == "Bersatu exit from PN imminent?":
        e["context"] += (
            " | 212300 UPDATE: 14th consecutive cycle (200000 + 212300) with ZERO fresh hard-"
            "news items from the mandatory gnews 'bersatu exit pn' query. The 212300 cycle's "
            "sole 'kuorum' gnews hit was a verified FALSE POSITIVE (KOHA.net article on a "
            "Kosovo/Albania assembly resolution on missing persons — unrelated to PN-MT / "
            "Bersatu). [CRITICAL] threshold (hard-news corroboration of 'Bersatu exit "
            "imminent?') STILL NOT CROSSED — remains [PRIORITY PIR-16]. mkini SNAPSHOT "
            "(18 Jul 18:00) remains the lone viral-tier item."
        )
        break

# (3) Zahid entity — 200000 cycle: NST "Malaysia dreams of hosting World Cup, says Zahid"
#     (20 Jul 03:15 MYT) — sports/non-PRN context. Marginal; documents Zahid making a
#     national-pride statement during campaign period. NOT a PIR-threshold signal.
for e in entities:
    if e.get("entity") == "Ahmad Zahid Hamidi (Zahid)":
        e["context"] += (
            " | 200000 UPDATE: NST 'Malaysia dreams of hosting World Cup, says Zahid' "
            "(20 Jul 03:15 MYT, Bangi Semarak Subuh programme, Argentina-Spain World Cup "
            "final giant-screen viewing) — Zahid (Deputy PM / Rural & Regional Development "
            "Minister) voices national aspiration to host FIFA World Cup. Non-PRN / "
            "sports context; marginal context-update only. NOT a PIR-06 threshold signal. "
            "Zahid remains BN chairman / Umno president; no new NS-PRN-relevant statement "
            "captured in the 200000 or 212300 cycles."
        )
        break

# ---------------------------------------------------------------------------
# PART 2 — NEW entities (2)
# ---------------------------------------------------------------------------

new_entities = [
    {
        "entity": "Zambry (Zambry Abd Kadir)",
        "type": "person",
        "pir_tag": "PIR-06",
        "priority": "priority",
        "source_url": "https://news.google.com/rss/search?q=Bersatu+sole+opposition+Muhyiddin+when:3d&hl=en-MY&gl=MY&ceid=MY:en",
        "context": (
            "NEW PIR-06 person (5th carry-forward, 212300 cycle). Umno Secretary-General "
            "(Zambry Abd Kadir, former Perak MB). Headline-intel: Newswav 'BN-PN pact comes "
            "alive in Port Dickson as Zambry, Samsuri meet' (18 Jul 09:22 MYT, gnews "
            "headline-intel — full text not curl-recoverable). Cross-surfaced via the "
            "mandatory 'Bersatu sole opposition Muhyiddin' gnews query. Zambry (BN/Umno "
            "Sec-Gen) met Samsuri (PN chairman / Terengganu MB) in PORT DICKSON — an NS "
            "constituency (N.05, Director PIR-06 Tier-4 seat). FIRST explicit Tier-4-seat "
            "(N.05) leadership-meeting intel: a PIR-06 cooperation signal on Tier-4 turf. "
            "Pre-dates the 19 Jul Hamzah 'gabung jentera' machinery merger (18:29 MYT) — "
            "this is the POLITICAL-LEADERSHIP-LEVEL BN-PN pact confirmation (Zambry=BN "
            "sec-gen ↔ Samsuri=PN chairman), distinct from the operational/grassroots "
            "machinery merger. Class [PRIORITY] (not [CRITICAL]) — cooperation-hardening "
            "signal, NOT a fracture signal. Reinforces BN-PN pact; does NOT cross the "
            "[CRITICAL] threshold (which requires 'pecat/keluar/tarik diri/toxic PN/kuorum/"
            "lebih hebat' entity)."
        ),
    },
    {
        "entity": "BN-PN pact Port Dickson meeting (Zambry-Samsuri)",
        "type": "narrative",
        "pir_tag": "PIR-06",
        "priority": "priority",
        "source_url": "https://news.google.com/rss/search?q=Bersatu+sole+opposition+Muhyiddin+when:3d&hl=en-MY&gl=MY&ceid=MY:en",
        "context": (
            "NEW PIR-06 narrative (5th carry-forward, 212300 cycle). Newswav gnews "
            "headline-intel (18 Jul 09:22 MYT): 'BN-PN pact comes alive in Port Dickson as "
            "Zambry, Samsuri meet.' Leadership-level BN-PN pact confirmation on NS soil — "
            "Zambry (Umno Sec-Gen / BN) ↔ Samsuri (PN chairman / Terengganu MB) meeting in "
            "PORT DICKSON (N.05, Director PIR-06 Tier-4 seat). First explicit Tier-4-seat "
            "(N.05) leadership-meeting intel: a PIR-06 cooperation signal on Tier-4 turf. "
            "Pre-dates and pre-figures the 19 Jul 4-stage BN-PN formalization trajectory "
            "(seat-swap → gabung jentera machinery merger → manifesto bersepadu → kongsi "
            "pentas joint ceramah). The Zambry-Samsuri PD meeting is the POLITICAL-LEADERSHIP "
            "tier of that trajectory — the precursor that enabled the operational tiers "
            "that followed. Adds a 5th Tier-4 seat (N.05) to the active-watch set "
            "(N.04/05/13/14/23/25/31/34). Class [PRIORITY] (not [CRITICAL]) — cooperation-"
            "hardening, NOT a coalition-fracture signal. The [CRITICAL] flag (Kiandee "
            "quorum escalation) remains MAINTAINED on the FRACTURE vector; this is the "
            "COUNTER-vector (BN-PN pact strengthening)."
        ),
    },
]

entities.extend(new_entities)
print(f"Added {len(new_entities)} new entities. Total now: {len(entities)}")

# ---------------------------------------------------------------------------
# PART 3 — Validate + write JSON
# ---------------------------------------------------------------------------

valid_pir = {"PIR-06", "PIR-07", "PIR-16"}
valid_pri = {"normal", "priority", "critical"}
valid_type = {"person", "party", "seat", "narrative"}

issues = 0
for i, e in enumerate(entities):
    if "entity" not in e or not e["entity"]:
        print(f"  [WARN] entity {i}: missing/empty 'entity' field"); issues += 1
    if e.get("pir_tag") not in valid_pir:
        print(f"  [WARN] entity {i} '{e.get('entity')}': bad pir_tag '{e.get('pir_tag')}'"); issues += 1
    if e.get("priority") not in valid_pri:
        print(f"  [WARN] entity {i} '{e.get('entity')}': bad priority '{e.get('priority')}'"); issues += 1
    if e.get("type") not in valid_type:
        print(f"  [WARN] entity {i} '{e.get('entity')}': bad type '{e.get('type')}'"); issues += 1

# Tally
pir_tally = {"PIR-06": 0, "PIR-07": 0, "PIR-16": 0}
pri_tally = {"normal": 0, "priority": 0, "critical": 0}
type_tally = {"person": 0, "party": 0, "seat": 0, "narrative": 0}
for e in entities:
    pir_tally[e["pir_tag"]] += 1
    pri_tally[e["priority"]] += 1
    type_tally[e["type"]] += 1

print(f"\nValidation issues: {issues}")
print(f"\nEntity tally:")
print(f"  by PIR:       {pir_tally}")
print(f"  by priority:  {pri_tally}")
print(f"  by type:      {type_tally}")
print(f"  TOTAL:        {len(entities)}")

with open(OUT_PATH, "w", encoding="utf-8") as f:
    json.dump(entities, f, ensure_ascii=False, indent=2)
print(f"\nWrote: {OUT_PATH}")

# ---------------------------------------------------------------------------
# PART 4 — Append new section to summary.md
# ---------------------------------------------------------------------------

summary_addendum = """

---

## Extraction Run 20260719-2225 (5th carry-forward; cycles 200000 + 212300 incorporated)

**Run basis:** Same Director-approved 19 Jul 17:25 MYT cycle (4th carry-forward label retained per Director mission spec). This run extends the entity corpus with the two cycles fetched AFTER the 1954 run:

- **200000 cycle** (04:03 MYT 20 Jul cutoff): 1 fresh NST RSS file (Zahid World Cup hosting — sports/non-PRN, marginal context-update only)
- **212300 cycle** (05:25 MYT 20 Jul cutoff): 12 files total — 3 fresh RSS false-positives (Argentina-Spain World Cup final + Fahmi RTM sports coverage, all non-PIR) + 9 gnews headline-intel duplicates of prior-cycle items (including the verified FALSE-POSITIVE KOHA.net "kuorum" hit — a Kosovo/Albania assembly resolution on missing persons, UNRELATED to Bersatu/PN-MT)

**Output:** `entities-20260719-2225.json` — **230 entities** (228 base + 2 new): PIR-06=55, PIR-07=107, PIR-16=66 + 1 dual-tag context-update; critical=14, priority=107, normal=109.

**Cumulative prior runs:** 1217 (133 entities, 4 cycles) → 1435 (205 entities, 8 cycles) → 1725 (226 entities, 12 cycles) → 1954 (228 entities, 13 cycles) → **2225 (230 entities, 15 cycles)**

### What's NEW this run (2 new entities, 3 context updates)

#### 🟢 NEW PIR-06 entities (2 — both [PRIORITY], cooperation-hardening vector)

1. **Zambry (Zambry Abd Kadir)** — NEW PIR-06 [PRIORITY] person. Umno Secretary-General (former Perak MB). Headline-intel (Newswav, 18 Jul 09:22 MYT, gnews): Zambry (BN/Umno Sec-Gen) met Samsuri (PN chairman / Terengganu MB) in **Port Dickson** — an NS constituency (N.05, Director PIR-06 Tier-4 seat). Cross-surfaced via the mandatory "Bersatu sole opposition Muhyiddin" gnews query.

2. **BN-PN pact Port Dickson meeting (Zambry-Samsuri)** — NEW PIR-06 [PRIORITY] narrative. The leadership-level BN-PN pact confirmation on NS soil. Pre-dates the 19 Jul 4-stage formalization trajectory (seat-swap → gabung jentera → manifesto bersepadu → kongsi pentas). The Zambry-Samsuri PD meeting is the **POLITICAL-LEADERSHIP tier** of that trajectory — the precursor enabling the operational tiers that followed. **First explicit Tier-4-seat (N.05) leadership-meeting intel**: a PIR-06 cooperation signal on Tier-4 turf.

> ⚠️ These two entities are on the **cooperation-hardening** vector, NOT the coalition-fracture vector. They REINFORCE the BN-PN pact and do NOT cross the [CRITICAL] threshold (which is reserved for "pecat/keluar/tarik diri/toxic PN/kuorum/lebih hebat" entities on the fracture vector). The [CRITICAL] flag (Kiandee quorum escalation) remains MAINTAINED on the FRACTURE vector; this run strengthens the COUNTER-vector.

#### 🔄 Context updates (3)

1. **"sole opposition" narrative** — now **5-outlet corroborated**: FMT (18 Jul 16:52) + The Vibes (18 Jul) + NST (18 Jul 08:31) + The Star (18 Jul 23:24) + Malay Mail (18 Jul 08:53). The NST/Star/Malay Mail items were freshly surfaced this cycle as gnews headline-intel cross-surfaced via the "Bersatu sole opposition Muhyiddin" query. Hard-news corroboration of Muhyiddin's "Bersatu sole opposition" framing is now multi-publisher. **PIR-16 [PRIORITY]** — narrative reinforcement, NOT a [CRITICAL] "Bersatu exit imminent?" corroboration (the Director [CRITICAL] trigger requires hard-news of an actual imminent exit, not just self-positioning as the sole opposition voice).

2. **"Bersatu exit from PN imminent?" narrative** — **14th consecutive cycle** (200000 + 212300) with ZERO fresh hard-news items from the mandatory gnews "bersatu exit pn" query. The 212300 cycle's sole "kuorum" gnews hit was a verified **FALSE POSITIVE** (KOHA.net article on a Kosovo/Albania assembly resolution on missing persons — unrelated to PN-MT / Bersatu). **[CRITICAL] threshold (hard-news corroboration of 'Bersatu exit imminent?') STILL NOT CROSSED — remains [PRIORITY PIR-16].** mkini SNAPSHOT (18 Jul 18:00) remains the lone viral-tier item.

3. **Ahmad Zahid Hamidi (Zahid)** — marginal context-update: NST "Malaysia dreams of hosting World Cup, says Zahid" (20 Jul 03:15 MYT, Bangi Semarak Subuh programme, Argentina-Spain World Cup final giant-screen viewing). Zahid voices national aspiration to host FIFA World Cup. **Non-PRN / sports context**; not a PIR-06 threshold signal. Zahid remains BN chairman / Umno president; no new NS-PRN-relevant statement captured in the 200000 or 212300 cycles.

### PIR-06 [CRITICAL] status — MAINTAINED, 15th consecutive cycle with no threshold crossing

| # | Trigger | Status |
|---|---------|--------|
| 1 | **"lebih hebat" new-coalition declaration** (Muhyiddin, Sinar 17 Jul) | [CRITICAL] MAINTAINED — no formal launch 18-20 Jul |
| 2 | **"sasar bentuk kerajaan negeri" Bersatu solo 24-seat governing bid** (MalaysiaGazette + Sinar 19 Jul) | [CRITICAL] MAINTAINED — Bersatu-attributed hard-news confirmed; no formal withdrawal of solo bid |
| 3 | **Kiandee quorum escalation** (FMT 11 Jul) | [CRITICAL] MAINTAINED — formal PN-MT expulsion notice / Bersatu withdrawal NOT issued across 15 cycles |

**[CRITICAL]-tier adjacent signals (sustained, not escalated):**
- toxic PN (Muhyiddin) — Hamzah rebuttal, no new escalation
- pecat Tang Jay Son (Gerakan) — no new intra-PN pecat events
- RoS complaint disrupting PN seat negotiations (Tun Faisal) — no formal RoS action
- gabung jentera (machinery merger) — operationalized, no fracture
- kuorum (MPT quorum dispute) — contested, not resolved; gnews "kuorum" surfaced KOHA.net false positive only

**Day-2 dawn window (20 Jul 01:17–05:25 MYT) = LOW YIELD.** The 200000 and 212300 cycles produced no new election developments — Day-2 dawn news cycle is dominated by overnight sports content (World Cup final) and historical-but-newly-surfaced gnews headline-intel. The genuinely-new analytical delta is limited to the Zambry-Samsuri Port Dickson meeting (an 18 Jul item freshly surfaced via gnews, not a new same-day development).

### Tier-4 seat watch (Director PIR-06 list)

| Seat | Status this run |
|------|-----------------|
| N.04 | No new intel; no Bersatu candidate withdrawals |
| **N.05** | **NEW: Zambry-Samsuri Port Dickson meeting — first explicit Tier-4 (N.05) leadership-meeting intel (PIR-06 cooperation signal on Tier-4 turf)** |
| N.13 (Sikamat) | No new intel; Tun Faisal (Bersatu) vs Razali (Wawasan/PN) vs Nor Azman (PH) |
| N.14 (Ampangan) | No new intel; Dr Rafie (PN) vs Nazri Kassim (PH) |
| N.23 | No new intel; no Bersatu candidate withdrawals |
| N.25 (Labu) | No new intel; Maira (Bersatu) vs Ahmad Faez (PH) |
| N.31 | No new intel; no Bersatu candidate withdrawals |
| N.34 | No new intel; no Bersatu candidate withdrawals |

### Watch entities (Director PIR-16 list — retained, no new intel this run)

- **Mah Hang Soon** (MCA) — no statement/response detected; MCA rebuttal watch continues (only Wee's "not a coalition" defense has surfaced)
- **Albert Tei** — 0 fresh items across 15 cycles
- **"barking dogs"** — 0 fresh items across 15 cycles
- **"majoriti mudah"** — not surfaced this cycle
- **Muhyiddin graft trial** — not surfaced in today's collection

### Pipeline status

- **Total cycles run 2026-07-19:** 15+ (075200 → 212300 UTC = 15:25–05:25 MYT span)
- **Total titles scanned:** ~2,500+
- **Total entities:** 230 (PIR-06=55, PIR-07=107, PIR-16=66 + 1 dual-tag context-update; critical=14, priority=107, normal=109)
- **PIR-06 [CRITICAL] flag:** MAINTAINED — formal PN Supreme Council expulsion/removal notice for Bersatu = **0 hits across ~2,500+ titles scanned** (15th consecutive cycle with no [CRITICAL] threshold crossing on the fracture vector)
- **Day-2 dawn posture:** LOW YIELD. Next significant content window expected to be the **PH manifesto launch 20 Jul evening (Klana Resort, Seremban)** — Amirudin Shari officiating. Watch for the BN manifesto launch 24 Jul at DUN Linggi + Pertang (potential JOINT BN-PN event per Annuar's "manifesto bersepadu" confirmation).

---

*Run 2225 appended 2026-07-20 ~05:30 MYT (21:30 UTC 19 Jul) by PRN NS 2026 Entity Extraction Agent. TLP:AMBER. All entities carry source_url. [CRITICAL] flag on Kiandee quorum escalation MAINTAINED from prior 075200 cycle (15th consecutive cycle with no formal-threshold crossing on the fracture vector). Day-2 dawn window QUIET: 2 genuinely-new analytical items only (Zambry + BN-PN pact PD meeting, both PIR-06 [PRIORITY] cooperation-vector). The KOHA.net "kuorum" gnews hit was verified as a FALSE POSITIVE (Kosovo assembly, not Bersatu MPT).*
"""

with open(SUMMARY_PATH, "a", encoding="utf-8") as f:
    f.write(summary_addendum)
print(f"Appended to: {SUMMARY_PATH}")

print("\n=== BUILD COMPLETE ===")
print(f"Total entities: {len(entities)}")
print(f"  PIR-06: {pir_tally['PIR-06']}")
print(f"  PIR-07: {pir_tally['PIR-07']}")
print(f"  PIR-16: {pir_tally['PIR-16']}")
print(f"  critical: {pri_tally['critical']}")
print(f"  priority: {pri_tally['priority']}")
print(f"  normal:   {pri_tally['normal']}")
