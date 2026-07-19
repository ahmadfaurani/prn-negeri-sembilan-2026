#!/usr/bin/env python3
"""Build/update collection_metadata.json for cycle 20260719_024042 (10:40 MYT 19 Jul).
Loads NEW scrape_results + priority_fetch_results for 024042 cycle, re-derives
freshness/PIR signals/critical scan, and MERGES with the prior 011915 cycle's
hand-curated metadata so accumulated PIR assessments are preserved.

PRIOR_CYCLE = 20260719_011915 (09:19 MYT 19 Jul) — the immediately preceding cycle.
CUTOFF = 2026-07-19 01:19:00 UTC (09:19 MYT) — freshness threshold vs prior cycle.
"""
import json, os, re, datetime

BASE = "/home/p62operator/.openclaw/workspace-ns/04-DATA-AND-SOURCES/raw-scrapes/20260719"
TS = "20260719_024042"
TODAY = "20260719"
PRIOR_CYCLE = "20260719_011915"
CUTOFF = datetime.datetime(2026, 7, 19, 1, 19, 0)  # UTC = 09:19 MYT 19 Jul

R = json.load(open(os.path.join(BASE, f"_scrape_results_{TS}.json"), encoding="utf-8"))
PF = json.load(open(os.path.join(BASE, f"_priority_fetch_results_{TS}.json"), encoding="utf-8"))

# ---- prior cycle priority titles (delta baseline) ----
prior_titles = set()
PRIOR_RESULTS = os.path.join(BASE, f"_scrape_results_{PRIOR_CYCLE}.json")
if os.path.exists(PRIOR_RESULTS):
    PR = json.load(open(PRIOR_RESULTS, encoding="utf-8"))
    for s in PR.get("sources", []):
        for t in s.get("priority_titles", []):
            prior_titles.add(re.sub(r"\s+"," ",t.lower().strip())[:140])
    for u in PR.get("universal_gnews_files", []):
        for t in u.get("priority_titles", []):
            prior_titles.add(re.sub(r"\s+"," ",t.lower().strip())[:140])

# ---- load prior hand-curated metadata to preserve PIR assessments ----
PRIOR_META_PATH = os.path.join(BASE, "collection_metadata.json")
prior_meta = {}
if os.path.exists(PRIOR_META_PATH):
    try:
        prior_meta = json.load(open(PRIOR_META_PATH, encoding="utf-8"))
    except Exception:
        prior_meta = {}

def norm(t): return re.sub(r"\s+"," ",t.lower().strip())[:140]
def parse_pubdate(pub):
    if not pub: return None
    pub = pub.strip()
    m = re.match(r"\w{3},\s*(\d{1,2})\s+(\w{3})\s+(\d{4})\s+(\d{2}):(\d{2}):(\d{2})\s+GMT", pub)
    if m:
        months = {"Jan":1,"Feb":2,"Mar":3,"Apr":4,"May":5,"Jun":6,"Jul":7,"Aug":8,"Sep":9,"Oct":10,"Nov":11,"Dec":12}
        return datetime.datetime(int(m.group(3)),months[m.group(2)],int(m.group(1)),int(m.group(4)),int(m.group(5)),int(m.group(6)))
    m = re.match(r"(\d{4})-(\d{2})-(\d{2})T?(\d{2}):(\d{2}):(\d{2})", pub)
    if m: return datetime.datetime(*[int(x) for x in m.groups()])
    m = re.match(r"(\d{4})-(\d{2})-(\d{2}) (\d{2}):(\d{2}):(\d{2})", pub)
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
                         r"pn.*sack.*bersatu|bersatu.*expell|dikeluarkan daripada pn|"
                         r"pn secara rasmi.*keluarkan.*bersatu)", re.I)
critical_hits = [t for t in pir06_titles if CRITICAL_RE.search(t)]
# Also fold in the scrape's own critical scan (run across all titles incl. non-priority)
scrape_crit = R.get("pir06_critical_alert", {})
if scrape_crit.get("formal_removal_notice_detected"):
    for c in scrape_crit.get("critical_evidence", []):
        t = c.get("title","")
        if t and t not in critical_hits:
            critical_hits.append(t)

# precursor (call-for-removal, not formal)
PRECURSOR_RE = re.compile(r"(asas kukuh|grounds to remove|calls? for.*sack|bidas.*pecat|"
                          r"may (leave|be expelled)|sepatutnya.*pecat|keluarkan bersatu|"
                          r"remove bersatu from pn|pecat bersatu|ouster|push.*out.*perikatan)", re.I)
precursor_hits = [t for t in pir06_titles if PRECURSOR_RE.search(t) and t not in critical_hits]

# ---- false-positive filter for PIR-06 (keyword noise) ----
FP_RE = re.compile(r"(keluar.*rm|keluar.*wang|keluar.*duit|baiki lif|cr7|ronaldo|sepanyol|"
                   r"piala dunia|air mata|sukan|bomba|runtuhan|kenderaan|covid|suhu|jerebu)", re.I)
pir06_real = [t for t in pir06_titles if not FP_RE.search(t)]

# ---- carry-over prior hand-curated PIR assessments (key_signals etc.) ----
prior_pir = prior_meta.get("pir_signal_summary", {}) if prior_meta else {}

# ---- new genuinely-fresh signals this cycle (confirmed by pubdate >= cutoff) ----
new_fresh_confirmed = [ser(it) for it in fresh_pri]

meta = {
  "collection_cycle": {
    "cycle_id": TS,
    "date_folder": TODAY,
    "timestamp_utc": "2026-07-19 02:40:42 UTC",
    "timestamp_myt": "2026-07-19 10:40 MYT",
    "mode": "Nomination-Day Surge Mode (Day-1 morning MYT cycle, 2nd cycle of 19 Jul)",
    "classification": "TLP:AMBER",
    "director_priority_approval": "2026-07-18 15:00 MYT",
    "pir_priorities": {"PIR-06":"HIGHEST — PN-Removal-of-Bersatu Watch",
                       "PIR-09":"SECOND — Candidate Credibility",
                       "PIR-07":"THIRD — Battleground Assessment"},
    "prior_cycle": PRIOR_CYCLE,
    "cutoff_utc": CUTOFF.isoformat(),
    "cutoff_myt": "2026-07-19 09:19 MYT (freshness threshold vs prior 011915 cycle)"
  },
  "critical_alerts": {
    "PIR-06_formal_removal_notice": {
      "status": "NOT DETECTED" if not critical_hits else "CRITICAL — DETECTED",
      "critical_hits": critical_hits,
      "critical_hits_count": len(critical_hits),
      "threshold_crossed": len(critical_hits) > 0,
      "assessment": (f"No formal PN Supreme Council removal notice for Bersatu detected across "
                     f"{R.get('titles_scanned_for_critical', len(uniq))} titles scanned this cycle. "
                     "Bersatu remains a PN component operating solo under its own logo in NS (operational split "
                     "confirmed in prior Kosmo nomination recap), but no formal expulsion/termination has been "
                     "issued by PN-MT. Status UNCHANGED vs prior 011915 cycle.")
                    if not critical_hits else
                    ("CRITICAL: formal PN-MT removal notice for Bersatu DETECTED this cycle. "
                     "See critical_hits list for evidence titles + URLs. Flag for immediate analyst escalation.")
    },
    "precursor_signals": {
      "count": len(precursor_hits),
      "titles": precursor_hits[:12],
      "note": "Call-for-removal / analytical-level signals (NOT formal notices). Kiandee 'asas kukuh'/'grounds "
              "to remove' remains the highest-signal precursor (carryover, stable across cycles). No new "
              "precursor escalated to a formal notice this cycle."
    }
  },
  "collection_summary": {
    "total_titles_scanned": R.get("titles_scanned_for_critical", len(uniq)),
    "unique_titles": len(uniq),
    "sources_attempted": len(R["sources"]) + len(R.get("universal_gnews_files",[])),
    "sources_http_200": sum(1 for s in R["sources"] if str(s["http_code"])=="200") + sum(1 for u in R.get("universal_gnews_files",[]) if str(u.get("http_code"))=="200"),
    "fresh_items_after_cutoff": len(fresh),
    "fresh_priority_items": len(fresh_pri),
    "genuinely_new_priority_titles_vs_prior": len(new_pri),
    "priority_articles_fetched_fulltext": sum(1 for p in PF if p["ok"]),
    "priority_fetch_attempts": len(PF),
    "note": "Thin genuinely-new content this cycle: only 1 absolutely-timed fresh item (a Kosmo lift-repair "
            "article that is a PIR-06 FALSE POSITIVE — 'keluar' = 'took out' money, not 'exit PN'). Confirmed-fresh "
            "PRN-relevant items are the awani campaign-permit piece (10:07 MYT, full text fetched) and the mkini "
            "Zan Azlee commentary (09:49 MYT, paywalled preview). Remainder of the 136 'genuinely-new vs prior' "
            "priority titles are older articles re-surfaced by the universal Google News feeds (freshness by "
            "publication date is pre-cutoff)."
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
     "pub":p.get("pub",""),"mode":p.get("mode","direct"),"note":p.get("note","")}
    for p in PF
  ],
  "freshness_analysis": {
    "cutoff_utc": CUTOFF.isoformat(),
    "cutoff_myt": "2026-07-19 09:19 MYT",
    "fresh_items_count": len(fresh),
    "fresh_priority_items_count": len(fresh_pri),
    "genuinely_new_priority_count_vs_prior_011915": len(new_pri),
    "fresh_items": [ser(i) for i in fresh],
    "fresh_priority_items": [ser(i) for i in fresh_pri],
    "genuinely_new_priority_items_top25": [ser(i) for i in new_pri[:25]]
  },
  "pir_signal_summary": {
    "PIR-06": {
      "priority": "HIGHEST",
      "unique_titles_tagged": len(pir06_titles),
      "unique_titles_after_false_positive_filter": len(pir06_real),
      "critical_formal_notice": len(critical_hits),
      "precursor_count": len(precursor_hits),
      "key_signals": (prior_pir.get("PIR-06", {}).get("key_signals", []) or []) + [
        "[THIS CYCLE 024042] No formal PN-MT removal notice detected (0 critical hits across 1174 titles). Status UNCHANGED vs 011915.",
        "[THIS CYCLE 024042] Kiandee 'PN has grounds (asas kukuh) to remove Bersatu' precursor persists (carryover, via NST gnews + universal pnpecat feed) — still a CALL, not a notice.",
        "[THIS CYCLE 024042] FALSE POSITIVE flagged: Kosmo 'Penghuni Seri Perantau keluar RM26,000 baiki lif sendiri' (10:00 MYT) — 'keluar' = 'took out' money for lift repair, NOT a Bersatu/PN exit. Keyword noise; excluded from real PIR-06 signal count.",
        "[THIS CYCLE 024042] Headline-only (gnews, freshness-unconfirmed): 'Incumbent Gemas rep resigns as division chief, quits Bersatu ahead of NS polls' (The Edge, universal feed) — a Bersatu quit/resignation signal to verify next cycle if it surfaces with a real URL/pubdate."
      ],
      "tier4_seat_watch": "N.04, N.05, N.13, N.14, N.23, N.25, N.31, N.34 — no candidate withdrawals reported this cycle. "
                         "N.14 Ampangan: PH 'defector' vs PN 'experienced rep' (Rafie) messaging war continues (carryover). "
                         "NEW headline-only: NST gnews 'Senior citizen withdraws from Sikamat race over incomplete documents' — a non-Tier-4 Sikamat withdrawal (PIR-09 eligibility), freshness-unconfirmed.",
      "assessment": "PIR-06 threshold (formal PN-MT removal notice) NOT crossed — UNCHANGED vs prior 011915 cycle. "
                    "Situation stable at operational-split + precursor-call level. Bersatu-solo-under-own-logo confirmed; "
                    "no retaliation/exit by Bersatu, no Tier-4 withdrawals. Watch continues."
    },
    "PIR-09": {
      "priority": "SECOND",
      "unique_titles_tagged": len(pir09_titles),
      "key_signals": (prior_pir.get("PIR-09", {}).get("key_signals", []) or []) + [
        "[THIS CYCLE 024042] NST gnews headline-only: 'Senior citizen withdraws from Sikamat race over incomplete documents' — candidate credibility/eligibility (incomplete nomination docs), freshness-unconfirmed (no pubdate in per-source gnews md).",
        "[THIS CYPLE 024042] The Star gnews headline-only: 'Negri polls: Campaign with integrity, Dr Wee tells MCA candidates' — MCA candidate-conduct messaging (PIR-09+PIR-07), freshness-unconfirmed.",
        "[THIS CYCLE 024042] Tamim (independent, red-notice/legal) carryover from 011915 — no new development this cycle."
      ],
      "assessment": "PIR-09 active but no new confirmed-fresh credibility development this cycle. N.14 Ampangan messaging war "
                    "continues (carryover). 4 independents: Tamim mapped; remaining 3 still TBD. Sikamat senior-citizen "
                    "withdrawal (headline-only) is the only new PIR-09-adjacent item — needs pubdate confirmation next cycle."
    },
    "PIR-07": {
      "priority": "THIRD",
      "unique_titles_tagged": len(pir07_titles),
      "key_signals": (prior_pir.get("PIR-07", {}).get("key_signals", []) or []) + [
        "[THIS CYCLE 024042 — CONFIRMED FRESH, FULL TEXT] Astro Awani 'PRN NS: Polis lulus 19 permit ceramah kempen' (pub 10:07 MYT 19 Jul): PDRM approved 19 ceramah/campaign permits since nomination day; NS Police Chief Datuk Alzafny Ahmad says security 'good and controlled', only 1 police report, NO election-offense investigation files opened. Campaign ends 31 Jul 23:59, polling 1 Aug, early voting 28 Jul. Strongest Day-1 campaign-ops signal.",
        "[THIS CYCLE 024042 — CONFIRMED FRESH, paywalled] mkini COMMENT by Zan Azlee 'Oh, so the state elections are an indicator?' (pub 09:49 MYT): frames NS polls as national indicator; references Johor (BN 48/56). Preview only (paywalled).",
        "[THIS CYCLE 024042 — headline-only, gnews] The Star: 'Back local boy Siow against DAP sec-gen who forgot Chennah, urges Ling' (N.15 Chennah Day-1 messaging); 'Lukut to see three-cornered fight as independent joins the fray' (new independent in Lukut); 'Aminuddin to face three-cornered battle in Linggi' (N.32 marquee confirm).",
        "[THIS CYCLE 024042 — headline-only, gnews] NST: 'BN to launch Negri Sembilan election manifesto on July 24' (PIR-07 manifesto event date set); 'BN-PN understanding aimed at ensuring NS political stability, says Asyraf Wajdi'; 'PN to assist BN during NS polls campaign, says Hadi' (BN-PN mutual campaign assistance confirmed); 'Chuah, Lukut and Bagan Pinang contests take shape'.",
        "[THIS CYCLE 024042] No poll/forecast publications with numerical seat projections detected this cycle (carryover)."
      ],
      "day1_campaign_activity": "Day-1 campaign activity emerging: 19 ceramah permits approved (awani, confirmed). "
                                 "Detailed ops-centre openings / candidate walkabouts still sparse at 10:40 MYT — "
                                 "expect fuller coverage in next cycle (11:00-13:00 MYT).",
      "marquee_seats_watch": "N.14 Ampangan (Rafie messaging war), N.15 Chennah (Loke defending; Ling urges local boy Siow), "
                             "N.28 Rantau (Tok Mat), N.13 Pertang (Jalaluddin), N.32 Linggi (Aminuddin three-cornered vs BN vs Bersatu), "
                             "N.10 Sikamat (senior-citizen withdrawal headline), Lukut (independent three-cornered), "
                             "N.04, N.33 — T1/T2 seats per PIR-07 monitor list.",
      "assessment": "PIR-07 enriched this cycle with the first confirmed Day-1 campaign-ops data point (19 ceramah permits, "
                    "awani 10:07 MYT). Full nomination-day structure (103 candidates) carryover stable. BN manifesto launch "
                    "set for 24 Jul (headline-only). Await fuller walkabout/ops-centre coverage next cycle."
    }
  },
  "deferred_and_blocked": prior_meta.get("deferred_and_blocked", {
    "NST_Bersatu_at_a_crossroads_fullbody": {
      "status": "STILL BLOCKED",
      "reason": "NST is not WordPress-backed; gnews article URLs are protobuf-encrypted.",
      "mitigation": "Headline-only intelligence retained."
    }
  }),
  "file_inventory": {
    "scrape_results_json": f"_scrape_results_{TS}.json",
    "priority_fetch_results_json": f"_priority_fetch_results_{TS}.json",
    "per_source_md": [s["file"] for s in R["sources"]] + [u["file"] for u in R.get("universal_gnews_files",[])],
    "priority_fulltext_md": [p["file"] for p in PF],
    "scraper_script": "_scrape_20260719.py",
    "fetcher_script": f"_fetch_priority_{TS}.py",
    "metadata_builder_script": f"_build_metadata_{TS}.py"
  },
  "cycle_delta_vs_prior_011915": {
    "prior_cycle_time_myt": "2026-07-19 09:19 MYT",
    "this_cycle_time_myt": "2026-07-19 10:40 MYT",
    "delta_hours": 1.35,
    "titles_scanned_prior": 1151,
    "titles_scanned_this": R.get("titles_scanned_for_critical", len(uniq)),
    "new_fulltext_articles_fetched": sum(1 for p in PF if p["ok"]),
    "new_fulltext_titles": [p.get("title","") for p in PF if p["ok"]],
    "pir06_status_change": "UNCHANGED (not detected -> not detected; 0 -> 0 critical hits)",
    "pir06_precursor_change": f"{prior_meta.get('critical_alerts',{}).get('precursor_signals',{}).get('count','?')} -> {len(precursor_hits)} (stable, Kiandee carryover)",
    "new_confirmed_fresh_pir07_signals_this_cycle": [
      "Astro Awani: PDRM approved 19 ceramah permits; security good/controlled; no election-offense files (10:07 MYT) — first confirmed Day-1 campaign-ops data point",
      "mkini Zan Azlee commentary: NS polls as national-indicator frame (09:49 MYT, paywalled)"
    ],
    "headline_only_day1_signals_to_verify_next_cycle": [
      "NST: Senior citizen withdraws from Sikamat race over incomplete documents (PIR-09 eligibility)",
      "The Star: Lukut three-cornered with independent; Chennah 'local boy Siow' vs Loke; Linggi Aminuddin three-cornered",
      "NST: BN manifesto launch 24 Jul; Hadi 'PN to assist BN campaign'; Asyraf Wajdi 'BN-PN understanding for stability'",
      "The Edge (universal feed): Incumbent Gemas rep resigns/quits Bersatu ahead of NS polls (PIR-06 quit signal — verify)"
    ],
    "false_positives_filtered": [
      "Kosmo 'Penghuni Seri Perantau keluar RM26,000 baiki lif sendiri' — 'keluar'=took out money, NOT Bersatu/PN exit (PIR-06 keyword noise)",
      "mStar 'Air mata CR7... Ronaldo... Sepanyol' — sports article, PIR-06 keyword noise (ranap/tumpah match)"
    ]
  },
  "cycle_history_20260719": [
    {"cycle_id": PRIOR_CYCLE, "timestamp_myt": "2026-07-19 09:19 MYT",
     "titles_scanned": prior_meta.get("collection_summary",{}).get("total_titles_scanned",1151),
     "pir06_critical": 0, "fulltext_fetched": prior_meta.get("collection_summary",{}).get("priority_articles_fetched_fulltext",3)},
    {"cycle_id": TS, "timestamp_myt": "2026-07-19 10:40 MYT",
     "titles_scanned": R.get("titles_scanned_for_critical", len(uniq)),
     "pir06_critical": len(critical_hits), "fulltext_fetched": sum(1 for p in PF if p["ok"])}
  ],
  "next_cycle_recommendations": [
    "PIR-06 (HIGHEST): no formal removal notice — maintain watch. Next cycle (~12:00-13:00 MYT) monitor for any PN-MT convened meeting statement; verify The Edge 'Gemas rep quits Bersatu' headline with a real URL/pubdate.",
    "PIR-07 (THIRD): capture fuller Day-1 walkabout/ops-centre-opening coverage for T1/T2 marquee seats (N.14, N.15, N.28, N.13, N.32, N.10 Sikamat, Lukut) — expected to materialize 11:00-14:00 MYT.",
    "PIR-09 (SECOND): confirm pubdate of NST 'Senior citizen withdraws from Sikamat' (is it 19 Jul Day-1?) and deepen background on the 3 remaining independents (Tamim mapped).",
    "Retry NST/The Star gnews-only headline recovery: attempt gnews URL de-redirection or Firecrawl JS-render for Sikamat withdrawal, Chennah Siow, Lukut independent, BN manifesto 24 Jul.",
    "Continue to flag PIR-06 keyword false positives (keluar RM/wang, sports) in metadata to keep the real signal count clean.",
    "Watch mkini for fresh 'Xh ago' items with X<6h (relative-time) in next cycle — currently only the Zan Azlee commentary qualified."
  ]
}

out_path = os.path.join(BASE, "collection_metadata.json")
with open(out_path,"w",encoding="utf-8") as f:
    json.dump(meta, f, ensure_ascii=False, indent=2)
print(f"Wrote {out_path}")
print(f"  cycle: {TS} (10:40 MYT) | prior: {PRIOR_CYCLE} (09:19 MYT)")
print(f"  sources: {len(meta['sources'])}, universal: {len(meta['universal_google_news'])}")
print(f"  titles scanned: {meta['collection_summary']['total_titles_scanned']} | unique: {len(uniq)}")
print(f"  fresh items (>=09:19 MYT): {len(fresh)} | fresh priority: {len(fresh_pri)}")
print(f"  PIR-06 critical: {meta['critical_alerts']['PIR-06_formal_removal_notice']['critical_hits_count']} (threshold crossed: {meta['critical_alerts']['PIR-06_formal_removal_notice']['threshold_crossed']})")
print(f"  PIR-06 unique titles: {len(pir06_titles)} (real after FP filter: {len(pir06_real)}) | precursor: {len(precursor_hits)}")
print(f"  PIR-09 unique titles: {len(pir09_titles)} | PIR-07 unique titles: {len(pir07_titles)}")
print(f"  genuinely new priority vs prior 011915: {len(new_pri)}")
print(f"  fulltext fetched OK: {meta['collection_summary']['priority_articles_fetched_fulltext']}/{meta['collection_summary']['priority_fetch_attempts']}")
