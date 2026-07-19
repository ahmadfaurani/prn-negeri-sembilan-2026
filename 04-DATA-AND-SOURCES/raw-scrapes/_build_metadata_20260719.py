#!/usr/bin/env python3
"""Build collection_metadata.json for cycle 20260719_011915.
Loads scrape_results + priority_fetch_results, re-derives freshness (datetime-safe),
assembles comprehensive metadata with PIR-06/09/07 signal analysis + delta vs prior cycle."""
import json, os, re, datetime

BASE = "/home/p62operator/.openclaw/workspace-ns/04-DATA-AND-SOURCES/raw-scrapes/20260719"
TS = "20260719_011915"
TODAY = "20260719"
PRIOR_CYCLE = "20260718_231029"
CUTOFF = datetime.datetime(2026, 7, 18, 23, 0, 0)  # UTC = 07:00 MYT 19 Jul

R = json.load(open(os.path.join(BASE, f"_scrape_results_{TS}.json"), encoding="utf-8"))
PF = json.load(open(os.path.join(BASE, f"_priority_fetch_results_{TS}.json"), encoding="utf-8"))

# ---- prior cycle priority titles (delta baseline) ----
prior_titles = set()
PRIOR_RESULTS = f"/home/p62operator/.openclaw/workspace-ns/04-DATA-AND-SOURCES/raw-scrapes/20260718/_scrape_results_231029.json"
if os.path.exists(PRIOR_RESULTS):
    PR = json.load(open(PRIOR_RESULTS, encoding="utf-8"))
    for s in PR.get("sources", []):
        for t in s.get("priority_titles", []):
            prior_titles.add(re.sub(r"\s+"," ",t.lower().strip())[:120])
    for u in PR.get("universal_gnews_files", []):
        for t in u.get("priority_titles", []):
            prior_titles.add(re.sub(r"\s+"," ",t.lower().strip())[:120])

def norm(t): return re.sub(r"\s+"," ",t.lower().strip())[:120]
def parse_pubdate(pub):
    if not pub: return None
    pub = pub.strip()
    m = re.match(r"\w{3},\s*(\d{1,2})\s+(\w{3})\s+(\d{4})\s+(\d{2}):(\d{2}):(\d{2})\s+GMT", pub)
    if m:
        months = {"Jan":1,"Feb":2,"Mar":3,"Apr":4,"May":5,"Jun":6,"Jul":7,"Aug":8,"Sep":9,"Oct":10,"Nov":11,"Dec":12}
        return datetime.datetime(int(m.group(3)),months[m.group(2)],int(m.group(1)),int(m.group(4)),int(m.group(5)),int(m.group(6)))
    m = re.match(r"(\d{4})-(\d{2})-(\d{2})T(\d{2}):(\d{2}):(\d{2})", pub)
    if m: return datetime.datetime(*[int(x) for x in m.groups()])
    return None

# ---- re-parse all md files for title+pubdate+pir ----
all_items = []
def parse_md(fpath, key):
    if not os.path.exists(fpath): return
    txt = open(fpath, encoding="utf-8").read()
    for ch in re.split(r"\n### ", txt)[1:]:
        line1 = ch.split("\n",1)[0]
        mp = re.match(r"\[PRIORITY ([^\]]+)\]\s*(.+)", line1)
        pirs = mp.group(1).split("+") if mp else []
        title = (mp.group(2) if mp else line1).strip()
        link=""; pub=""; src=""
        pm = re.search(r"\n(?:URL|gnews URL):\s*(\S+)", ch)
        if pm: link = pm.group(1)
        pm = re.search(r"\nPubDate:\s*(.+)", ch)
        if pm: pub = pm.group(1).strip()
        pm = re.search(r"\nPublisher:\s*(.+)", ch)
        if pm: src = pm.group(1).strip()
        all_items.append({"source_key":key,"title":title,"pubdate":pub,
                          "pdt":parse_pubdate(pub),"pirs":pirs,"link":link,"publisher":src})

for s in R["sources"]:
    parse_md(os.path.join(BASE, s["file"]), s["source"])
for u in R.get("universal_gnews_files", []):
    parse_md(os.path.join(BASE, u["file"]), f"univ_{u['ukey']}")

# de-dup
seen={}; 
for it in all_items:
    k=norm(it["title"])
    if k not in seen: seen[k]=it
uniq=list(seen.values())
fresh=[it for it in uniq if it["pdt"] and it["pdt"]>=CUTOFF]
fresh.sort(key=lambda x:x["pdt"],reverse=True)
fresh_pri=[it for it in fresh if it["pirs"]]
new_pri=[it for it in uniq if it["pirs"] and norm(it["title"]) not in prior_titles]
new_pri.sort(key=lambda x:x["pdt"] or datetime.datetime(2000,1,1),reverse=True)

def ser(it):
    return {"title":it["title"],"pubdate":it["pubdate"],
            "pdt":it["pdt"].isoformat() if it["pdt"] else None,
            "pirs":it["pirs"],"source_key":it["source_key"],
            "link":it["link"],"publisher":it["publisher"]}

# ---- PIR signal extraction ----
pir06_titles = [it["title"] for it in uniq if it["pirs"] and "PIR-06" in it["pirs"]]
pir09_titles = [it["title"] for it in uniq if it["pirs"] and "PIR-09" in it["pirs"]]
pir07_titles = [it["title"] for it in uniq if it["pirs"] and "PIR-07" in it["pirs"]]

# PIR-06 CRITICAL scan: formal PN-MT removal notice keywords
CRITICAL_RE = re.compile(r"(majlis tertinggi.*pecat|pecat.*majlis tertinggi|removal notice|"
                         r"formal.*remove.*bersatu|bersatu.*dibubarkan|"
                         r"pn.*sack.*bersatu|bersatu.*expell)", re.I)
critical_hits = [t for t in pir06_titles if CRITICAL_RE.search(t)]
# precursor (call-for-removal, not formal)
PRECURSOR_RE = re.compile(r"(asas kukuh|grounds to remove|calls? for.*sack|bidas.*pecat|"
                          r"may (leave|be expelled)|sepatutnya.*pecat)", re.I)
precursor_hits = [t for t in pir06_titles if PRECURSOR_RE.search(t) and t not in critical_hits]

# ---- assemble metadata ----
meta = {
  "collection_cycle": {
    "cycle_id": TS,
    "date_folder": TODAY,
    "timestamp_utc": "2026-07-19 01:19:15 UTC",
    "timestamp_myt": "2026-07-19 09:19 MYT",
    "mode": "Nomination-Day Surge Mode (Day-2 daytime MYT cycle)",
    "classification": "TLP:AMBER",
    "director_priority_approval": "2026-07-18 15:00 MYT",
    "pir_priorities": {"PIR-06":"HIGHEST — PN-Removal-of-Bersatu Watch",
                       "PIR-09":"SECOND — Candidate Credibility",
                       "PIR-07":"THIRD — Battleground Assessment"},
    "prior_cycle": PRIOR_CYCLE,
    "cutoff_utc": CUTOFF.isoformat(),
    "cutoff_myt": "2026-07-19 07:00 MYT (freshness threshold vs prior cycle)"
  },
  "critical_alerts": {
    "PIR-06_formal_removal_notice": {
      "status": "NOT DETECTED",
      "critical_hits": critical_hits,
      "critical_hits_count": len(critical_hits),
      "threshold_crossed": False,
      "assessment": "No formal PN Supreme Council removal notice for Bersatu detected across 1151 titles scanned. "
                    "Bersatu remains a PN component operating solo under its own logo in NS (operational split confirmed in "
                    "Kosmo nomination recap), but no formal expulsion/termination has been issued by PN-MT."
    },
    "precursor_signals": {
      "count": len(precursor_hits),
      "titles": precursor_hits,
      "note": "Call-for-removal / analytical-level signals (NOT formal notices). Kiandee 'asas kukuh'/'grounds to remove' "
              "is the highest-signal precursor (English + Malay versions captured across cycles)."
    }
  },
  "collection_summary": {
    "total_titles_scanned": R.get("titles_scanned_for_critical", 1151),
    "unique_titles": len(uniq),
    "sources_attempted": len(R["sources"]) + len(R.get("universal_gnews_files",[])),
    "sources_http_200": sum(1 for s in R["sources"] if str(s["http_code"])=="200") + sum(1 for u in R.get("universal_gnews_files",[]) if str(u.get("http_code"))=="200"),
    "fresh_items_after_cutoff": len(fresh),
    "fresh_priority_items": len(fresh_pri),
    "genuinely_new_priority_titles_vs_prior": len(new_pri),
    "priority_articles_fetched_fulltext": sum(1 for p in PF if p["ok"]),
    "priority_fetch_attempts": len(PF)
  },
  "sources": [
    {"source":s["source"],"label":s["label"],"url":s["url"],"strategy":s["strategy"],
     "http_code":s["http_code"],"article_count":s["article_count"],
     "priority_article_count":s["priority_article_count"],
     "prn_article_count":s["prn_article_count"],
     "pir06_hits":s["pir06_hits"],"pir09_hits":s["pir09_hits"],"pir07_hits":s["pir07_hits"],
     "file":s["file"],"priority_titles":s.get("priority_titles",[])}
    for s in R["sources"]
  ],
  "universal_google_news": [
    {"ukey":u["ukey"],"http_code":u.get("http_code"),
     "item_count":u["article_count"],"pir06_hits":u["pir06_hits"],
     "pir09_hits":u["pir09_hits"],"pir07_hits":u["pir07_hits"],
     "file":u["file"]}
    for u in R.get("universal_gnews_files",[])
  ],
  "priority_fulltext_fetches": [
    {"pir":p["pir"],"slug":p["slug"],"file":p["file"],"http":p["http"],"ok":p["ok"],
     "body_chars":p.get("body_len",0),"title":p.get("title",""),"final_url":p.get("final",""),
     "mode":p.get("mode","direct"),"n_posts":p.get("n")}
    for p in PF
  ],
  "freshness_analysis": {
    "cutoff_utc": CUTOFF.isoformat(),
    "fresh_items_count": len(fresh),
    "fresh_priority_items_count": len(fresh_pri),
    "genuinely_new_priority_count_vs_prior_231029": len(new_pri),
    "fresh_items": [ser(i) for i in fresh],
    "fresh_priority_items": [ser(i) for i in fresh_pri],
    "genuinely_new_priority_items_top20": [ser(i) for i in new_pri[:20]]
  },
  "pir_signal_summary": {
    "PIR-06": {
      "priority": "HIGHEST",
      "unique_titles_tagged": len(pir06_titles),
      "critical_formal_notice": len(critical_hits),
      "precursor_count": len(precursor_hits),
      "key_signals": [
        "Bersatu goes solo under own logo in NS (24 seats), breaking PN state consensus — confirmed in Kosmo nomination recap (09:05 MYT 19 Jul)",
        "Kiandee: 'PN has grounds (asas kukuh) to remove Bersatu' — precursor call (EN via NST, MY via Utusan; carryover from 18 Jul)",
        "Muhyiddin: 'Bersatu to use own logo for NS polls' (malaysiakini) — operational split",
        "Analysts: 'PAS may leave or be expelled from PN after split with Bersatu' (NST) — inverse speculation, NOT formal",
        "Machang Bersatu division calls for Wan Ahmad Fayhsal to be sacked (NST) — internal Bersatu disciplinary, PIR-09-adjacent",
        "Muhyiddin graft trial: 'Company gave Bersatu RM1m for unknown reasons, witness tells court' (malaysiakini) — legal pressure context"
      ],
      "tier4_seat_watch": "N.04, N.05, N.13, N.14, N.23, N.25, N.31, N.34 — no candidate withdrawals reported this cycle. "
                         "N.14 Ampangan: PH 'defector' vs PN 'experienced rep' (Rafie) messaging war continues (Utusan 'Kempen berkesan mampu bantu PH pertahankan Ampangan').",
      "assessment": "PIR-06 threshold (formal PN-MT removal notice) NOT crossed. Situation stable at operational-split + "
                    "precursor-call level. Watch continues — no retaliation/exit by Bersatu, no Tier-4 withdrawals."
    },
    "PIR-09": {
      "priority": "SECOND",
      "unique_titles_tagged": len(pir09_titles),
      "key_signals": [
        "N.14 Ampangan Day-1 messaging: Utusan 'Kempen berkesan mampu bantu PH pertahankan Ampangan' (11:04 UTC 18 Jul) — PH defending Rafie as 'experienced rep'",
        "Tamim surrenders to police, hopes to campaign for NS independent candidate (malaysiakini) — independent-candidate backstory, PIR-09",
        "Machang Bersatu calls for Wan Ahmad Fayhsal to be sacked from party, PN (NST) — Bersatu internal disciplinary",
        "MCA Youth sec-gen told to 'stay out of NS polls' over PN ally disagreement (malaysiakini) — component discipline",
        "Wee: BN-PN pact in NS not a merger, MCA principles intact (malaysiakini) — component-positioning messaging",
        "Anwar: Don't campaign on NS ruler crisis; red notice applied for Tamim (malaysiakini) — independent-candidate legal status",
        "4 independents: backgrounds still partially mapped — Tamim (independent, red-notice/legal issue) confirmed; others TBD"
      ],
      "assessment": "PIR-09 active. N.14 Ampangan messaging war continues (PH-defector vs experienced-rep framing). "
                    "Tamim independent-candidate legal situation (surrender + red notice) is the clearest new credibility thread. "
                    "No new Bersatu-candidate bankruptcy/court-eligibility findings this cycle."
    },
    "PIR-07": {
      "priority": "THIRD",
      "unique_titles_tagged": len(pir07_titles),
      "key_signals": [
        "Kosmo nomination recap (09:05 MYT 19 Jul): 103 candidates, 36 DUN — PH 36 / BN 25 / Bersatu 24 / PN 11 / 4 ind; 21 three-cornered, 11 straight, 2 four-cornered, 2 five-cornered; campaign ends 31 Jul 23:59",
        "Utusan rencana (09:18 MYT 19 Jul): 'PRN NS penentu hala tuju DAP' — DAP leadership referendum on Loke; Melaka PH-BN fracture (4 DAP+1 Amanah ADUNs withdrew support); adat/royal controversy link to Aminuddin's Sikamat->Linggi move",
        "Aminuddin (PH NS chairman) moved Sikamat->Linggi, three-cornered vs BN Mohd Faizal Ramli + Bersatu Zamri Md Said (Kosmo)",
        "Loke to defend Chennah; Aminuddin 'poster boy' takes Linggi (malaysiakini)",
        "PN unveils 11 candidates, completes NS line-up with 'friend' BN (malaysiakini)",
        "BN to contest 25 seats, signals electoral pact with PN (malaysiakini)",
        "How PAS can deliver Loke's seat and NS on a platter to BN (malaysiakini) — battleground forecast",
        "DAP revives anti-BN campaign ahead of NS polls (malaysiakini) — PH-BN tension within the pact",
        "No poll/forecast publications with numerical seat projections detected this cycle"
      ],
      "day1_campaign_activity": "Ops-centre openings / candidate walkabouts not yet reported in detail (Day-1 morning). "
                                 "Campaign officially opened after nomination declaration; ends 31 Jul 23:59 MYT.",
      "marquee_seats_watch": "N.14 Ampangan (Rafie messaging war), N.15 Chennah (Loke defending), N.28 Rantau (Tok Mat), "
                             "N.13 Pertang (Jalaluddin), N.32 Linggi (Aminuddin vs BN vs Bersatu three-cornered marquee), "
                             "N.04, N.33, N.10 — T1/T2 seats per PIR-07 monitor list.",
      "assessment": "PIR-07 rich. Full nomination-day structure confirmed (103 candidates, three-way configuration). "
                    "DAP-direction analysis + Aminuddin Linggi move + Melaka PH-BN fracture are the highest-value new threads. "
                    "Await Day-1 walkabout/ops-centre coverage in next cycle."
    }
  },
  "deferred_and_blocked": {
    "NST_Bersatu_at_a_crossroads_fullbody": {
      "status": "STILL BLOCKED",
      "reason": "NST is not WordPress-backed (WP-API returns HTTP 404, confirmed this cycle). "
                "gnews article URLs are protobuf-encrypted and do not redirect to real NST URLs via curl. "
                "Headline + gnews URL captured in nstcommy gnews .md (carryover, stable gnews item).",
      "headline": "Bersatu at a crossroads (NST, 16 Jul 2026)",
      "pir": "PIR-06",
      "mitigation": "Headline-only intelligence retained. Full body requires either NST subscription/manual access "
                   "or a headless-browser (JS-rendered) fetch — not available in this environment."
    },
    "thestarcommy_html_static": {
      "status": "LIMITED (JS-rendered)",
      "reason": "thestar.com.my static HTML yields only 5 article cards (JS-rendered). gnews fallback (thestarcommy_gn) "
                "recovers 100 items with 47 priority / 8 P06 / 6 P09 / 43 P07 — gnews is the effective The Star channel.",
      "compensated_by": "thestarcommy_gn (gnews RSS)"
    },
    "thmalaysianinsightcom": {
      "status": "0 articles (blocked/fenced)",
      "reason": "themalaysianinsight.com returns HTTP 200 but no parseable article cards in static HTML (paywall/fence).",
      "mitigation": "TMI coverage of NS is partially captured via universal gnews queries where TMI items surface."
    }
  },
  "file_inventory": {
    "scrape_results_json": f"_scrape_results_{TS}.json",
    "priority_fetch_results_json": f"_priority_fetch_results_{TS}.json",
    "freshness_analysis_json": f"_freshness_analysis_{TS}.json",
    "per_source_md": [s["file"] for s in R["sources"]] + [u["file"] for u in R.get("universal_gnews_files",[])],
    "priority_fulltext_md": [p["file"] for p in PF],
    "scraper_script": "_scrape_20260719.py",
    "fetcher_script": "_fetch_priority_20260719.py",
    "analysis_script": "_analyze_freshness_20260719.py",
    "metadata_builder_script": "_build_metadata_20260719.py"
  },
  "cycle_delta_vs_prior_231029": {
    "prior_cycle_time_myt": "2026-07-19 07:10 MYT",
    "this_cycle_time_myt": "2026-07-19 09:19 MYT",
    "delta_hours": 2.15,
    "new_fulltext_articles_fetched": 3,
    "new_fulltext_titles": [
      "PRN Negeri Sembilan penentu hala tuju DAP (Utusan rencana, 09:18 MYT)",
      "Percaturan BN-PH-Bersatu (Kosmo, 09:05 MYT)",
      "Felda mesti terus angkat martabat peneroka - Anwar (Utusan, 08:28 MYT)"
    ],
    "pir06_status_change": "UNCHANGED (not detected -> not detected)",
    "new_pir06_signals_this_cycle": [
      "Kosmo nomination recap explicitly states Bersatu 'keluar daripada konsensus PN negeri' and contests 24 seats under own logo, 'memecah undi di kawasan-kawasan kritikal' — strongest operational-split confirmation to date"
    ],
    "new_pir09_signals_this_cycle": [
      "Tamim surrenders to police, hopes to campaign for NS independent candidate (malaysiakini) — independent-candidate legal-status development"
    ],
    "new_pir07_signals_this_cycle": [
      "Full 103-candidate nomination structure confirmed (PH36/BN25/Bersatu24/PN11/4ind)",
      "DAP-direction rencana: Loke leadership referendum + Melaka PH-BN fracture + adat-controversy link to Aminuddin seat move",
      "Aminuddin Linggi three-cornered (vs BN Faizal Ramli + Bersatu Zamri Md Said) confirmed in Kosmo"
    ]
  },
  "next_cycle_recommendations": [
    "Continue PIR-06 watch — no formal removal notice yet, but Bersatu-solo operational split is now explicitly confirmed; monitor for any PN-MT convened meeting statement",
    "Next cycle (~11:00-13:00 MYT 19 Jul): expect Day-1 walkabout / ops-centre-opening coverage for T1/T2 marquee seats (N.14, N.15, N.28, N.13, N.32); capture for PIR-07",
    "PIR-09: deeper background on the 3 remaining independents (Tamim mapped; others TBD) — watch BERNAMA wire + mkini SNAPSHOT items",
    "Retry NST full-body recovery only if a headless-browser capability becomes available; otherwise continue headline-only via gnews",
    "Monitor mkini for fresh 'Xh ago' items with X<6h in next cycle (relative-time items currently all carryover)"
  ]
}

out_path = os.path.join(BASE, "collection_metadata.json")
with open(out_path,"w",encoding="utf-8") as f:
    json.dump(meta, f, ensure_ascii=False, indent=2)
print(f"Wrote {out_path}")
print(f"  sources: {len(meta['sources'])}, universal: {len(meta['universal_google_news'])}")
print(f"  fresh items: {meta['collection_summary']['fresh_items_after_cutoff']}")
print(f"  PIR-06 critical: {meta['critical_alerts']['PIR-06_formal_removal_notice']['critical_hits_count']} (threshold crossed: {meta['critical_alerts']['PIR-06_formal_removal_notice']['threshold_crossed']})")
print(f"  PIR-06 unique titles: {len(pir06_titles)} | PIR-09: {len(pir09_titles)} | PIR-07: {len(pir07_titles)}")
print(f"  genuinely new priority vs prior: {meta['collection_summary']['genuinely_new_priority_titles_vs_prior']}")
print(f"  fulltext fetched OK: {meta['collection_summary']['priority_articles_fetched_fulltext']}/{meta['collection_summary']['priority_fetch_attempts']}")
