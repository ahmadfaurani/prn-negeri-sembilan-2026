#!/usr/bin/env python3
"""
Entity extraction build script — Run 20260720-0106 (6th carry-forward of the
Director-approved 19 Jul 17:25 MYT cycle; mission brief labels it 4th carry-forward).

Incorporates the two fetch cycles NOT yet ingested by the entity-extraction agent
after the 2225 run:
  - 20260719_222800 (06:30 MYT 20 Jul): 3 files — ALL FALSE POSITIVES
      (Iraq-Iran-US diplomacy + 2x World Cup football). 0 NS-PRN entities.
  - 20260719_233400 (07:36 MYT 20 Jul): 16 files — 13 RSS false positives
      (World Cup football x9 + South-China-Sea defence + World-Cup-hosting +
       national-flag/AI + Johor-investment) + 3 gnews genuinely-new-to-collection.

Genuine NS-PRN analytical delta from 233400:
  1. FMT EN "Khaled urges voters to ensure repeat of Bersatu's Johor wipeout in NS"
     (07:12 MYT 20 Jul, FRESH) — 5th-outlet corroboration of Khaled's "KO habis"
     statement; NEW "Johor wipeout repeat" framing (explicitly names Johor
     precedent). -> 2 context updates + 1 new narrative entity.
  2. Malay Mail "Police approve 19 permits..." (19 Jul 11:00 MYT, pre-cutoff, new
     outlet) — same event, new outlet. -> 1 context update.
  3. Newswav "Anthony Loke Coming Baptism of Fire in NS Polls" (18 Jul 16:30 MYT,
     pre-cutoff, new framing) — analytical framing of Loke's Chennah battle. ->
     1 new narrative entity.

Net: 3 context updates + 2 new entities = 232 total (230 base + 2 new).
"""
import json, os, copy

BASE = "/home/p62operator/.openclaw/workspace-ns/04-DATA-AND-SOURCES/processed-entities/2026-07-19/entities-20260719-2225.json"
OUTDIR = "/home/p62operator/.openclaw/workspace-ns/04-DATA-AND-SOURCES/processed-entities/2026-07-20"
OUTFILE = os.path.join(OUTDIR, "entities-20260720-0106.json")

os.makedirs(OUTDIR, exist_ok=True)
entities = json.load(open(BASE))
assert len(entities) == 230, f"unexpected base count {len(entities)}"

UPD_KHALED = (" 233400 UPDATE (5th outlet): FMT EN 'Khaled urges voters to ensure "
    "repeat of Bersatu's Johor wipeout in NS' (07:12 MYT 20 Jul, gnews headline-intel; "
    "FMT direct-URL recovery failed 404 across 10 guesses) — 5th-outlet corroboration "
    "of 'KO habis' statement (prior 4: NST EN + Utusan BM + BH BM + Awani BM, 171500). "
    "NEW framing detail: explicitly names the JOHOR precedent — frames the NS Bersatu "
    "wipeout as a REPEAT of the Johor state-election result (where Bersatu was wiped "
    "out). PIR-06 [PRIORITY] — rhetorical corroboration, NOT [CRITICAL].")

UPD_KOHABIS = (" 233400 UPDATE (5th outlet + Johor-precedent framing): FMT EN 'Khaled "
    "urges voters to ensure repeat of Bersatu's Johor wipeout in NS' (07:12 MYT 20 Jul, "
    "gnews headline-intel) — 5th-outlet corroboration (NST EN + Utusan BM + BH BM + Awani "
    "BM + now FMT EN). NEW: explicitly frames the NS wipeout as a REPEAT of Bersatu's "
    "Johor state-election wipeout (Johor-as-precedent). Still [PRIORITY] not [CRITICAL] "
    "(BN-leader electoral-elimination rhetoric, not formal PN-MT expulsion/withdrawal).")

UPD_PERMITS = (" 233400 UPDATE (new outlet): Malay Mail 'Police approve 19 permits as "
    "Negeri Sembilan campaigns get under way' (19 Jul 11:00 MYT, gnews headline-intel; "
    "Malay Mail full-text URL not curl-recoverable) — Malay Mail version of the same "
    "'19 campaign permits approved' story (prior outlets: NST 12:26 + Kosmo 10:54 + "
    "Awani). New outlet, same event; no new intelligence.")

NEW_ENTITIES = [
    {
        "entity": "Bersatu Johor-wipeout-repeat framing (Khaled, FMT)",
        "type": "narrative",
        "pir_tag": "PIR-06",
        "priority": "priority",
        "source_url": "https://news.google.com/rss/search?q=khaled+bersatu+KO+when:3d&hl=en-MY&gl=MY&ceid=MY:en",
        "context": ("NEW framing entity (FMT EN, 07:12 MYT 20 Jul, gnews headline-intel; "
            "FMT direct URL not curl-recoverable — 404 across 10 category/day guesses; "
            "gnews protobuf still curl-unresolvable, 18th cycle). Khaled Nordin frames the "
            "targeted NS Bersatu wipeout as a REPEAT of Bersatu's Johor state-election "
            "result (where Bersatu was wiped out). Prior 'KO habis' captures (NST EN + "
            "Utusan BM + BH BM + Awani BM, 171500) used 'KO habis'/'knocked out' but did "
            "NOT explicitly name the Johor precedent — FMT is the first to make the "
            "Johor-as-precedent framing explicit. Reinforces the PIR-06 electoral-"
            "elimination vector (BN VP publicly urging Bersatu's electoral destruction "
            "while BN operationally cooperates with Bersatu's coalition partners via PN). "
            "Director PIR-06 keywords 'keluar'/'pecat'/'tarik diri'/'kuorum'/'lebih hebat' "
            "are about coalition-membership actions; this is electoral-elimination "
            "rhetoric by a BN (not PN) leader — adjacent, NOT [CRITICAL]. [PRIORITY PIR-06]."),
    },
    {
        "entity": "Loke baptism of fire (Chennah battle, Newswav)",
        "type": "narrative",
        "pir_tag": "PIR-07",
        "priority": "normal",
        "source_url": "https://news.google.com/rss/search?q=ceramah+Negeri+Sembilan+when:3d&hl=en-MY&gl=MY&ceid=MY:en",
        "context": ("NEW analytical-framing entity (Newswav, 18 Jul 16:30 MYT, gnews "
            "headline-intel; pre-cutoff / nomination-day). Newswav frames Anthony Loke's "
            "Chennah defense as a 'baptism of fire' in the NS polls. Chennah = the only "
            "MCA-DAP straight fight (Loke PH/DAP sec-gen vs Siow Kong Choon MCA/BN); "
            "47.8% Malay (up from 44% in 2018), 6.3% Orang Asli, 42.6% Chinese; PH vote "
            "dropped to 44% by PRU15 vs BN+PN combined 56% -> if PRU15 pattern repeats "
            "Loke LOSES (mkini 780075 full text, prior 075200). The 'baptism of fire' "
            "framing reinforces the PIR-16 'MCA biggest loser' / Loke-under-pressure "
            "narrative and the PIR-07 marquee-battleground status of Chennah. "
            "[normal PIR-07] — analytical framing, not a hard-news development."),
    },
]

updated = 0
for e in entities:
    if e["entity"] == "Mohamed Khaled Nordin":
        e["context"] = e["context"] + UPD_KHALED
        updated += 1
    elif e["entity"] == "Bersatu KO habis (electoral-elimination call)":
        e["context"] = e["context"] + UPD_KOHABIS
        updated += 1
    elif e["entity"] == "19 campaign permits approved":
        e["context"] = e["context"] + UPD_PERMITS
        updated += 1

assert updated == 3, f"expected 3 updates, got {updated}"
entities.extend(NEW_ENTITIES)
assert len(entities) == 232, f"unexpected final count {len(entities)}"

# sanity: every entity has required keys
for e in entities:
    for k in ("entity", "type", "pir_tag", "priority", "context"):
        assert k in e and e[k], f"missing key {k} in {e.get('entity')}"
    # new entities without source_url: add empty string for schema consistency
    e.setdefault("source_url", "")

with open(OUTFILE, "w") as f:
    json.dump(entities, f, ensure_ascii=False, indent=1)

from collections import Counter
print("WROTE:", OUTFILE)
print("TOTAL entities:", len(entities))
print("priority:", dict(Counter(e["priority"] for e in entities)))
print("pir_tag:", dict(Counter(e["pir_tag"] for e in entities)))
print("type:", dict(Counter(e["type"] for e in entities)))
print("critical count:", sum(1 for e in entities if e["priority"] == "critical"))
print("updates applied:", updated, "| new entities:", len(NEW_ENTITIES))
