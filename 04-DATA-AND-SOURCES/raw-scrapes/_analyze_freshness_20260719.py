#!/usr/bin/env python3
"""Analyze cycle 20260719_011915 freshness + identify genuinely-new PIR articles for full-text fetch.
Prior cycle cutoff: 20260718_231029 UTC = 07:10 MYT 19 Jul. We look for content published
after 23:00 UTC 18 Jul 2026 (07:00 MYT 19 Jul) — i.e., Day-2 morning MYT content.
Also delta against prior cycle's priority_titles set."""
import json, os, re, datetime
from bs4 import BeautifulSoup

BASE = "/home/p62operator/.openclaw/workspace-ns/04-DATA-AND-SOURCES/raw-scrapes/20260719"
TS = "20260719_011915"
PRIOR_TS = "20260718_231029"
CUTOFF = datetime.datetime(2026, 7, 18, 23, 0, 0)  # UTC

R = json.load(open(os.path.join(BASE, f"_scrape_results_{TS}.json"), encoding="utf-8"))

# ---- prior cycle priority titles (for delta) — load from prior results json ----
PRIOR_PATH = f"/home/p62operator/.openclaw/workspace-ns/04-DATA-AND-SOURCES/raw-scrapes/20260718/_scrape_results_{PRIOR_TS}.json"
prior_titles = set()
if os.path.exists(PRIOR_PATH):
    PR = json.load(open(PRIOR_PATH, encoding="utf-8"))
    for s in PR.get("sources", []):
        for t in s.get("priority_titles", []):
            prior_titles.add(re.sub(r"\s+"," ",t.lower().strip())[:120])
print(f"Prior cycle priority_titles loaded: {len(prior_titles)}")

def norm(t):
    return re.sub(r"\s+"," ",t.lower().strip())[:120]

def parse_pubdate(pub):
    """Parse RFC822 (gnews) or ISO (wpapi) pubDate to UTC datetime."""
    if not pub: return None
    pub = pub.strip()
    # RFC822: "Sat, 18 Jul 2026 12:51:31 GMT"
    m = re.match(r"\w{3},\s*(\d{1,2})\s+(\w{3})\s+(\d{4})\s+(\d{2}):(\d{2}):(\d{2})\s+GMT", pub)
    if m:
        months = {"Jan":1,"Feb":2,"Mar":3,"Apr":4,"May":5,"Jun":6,"Jul":7,"Aug":8,"Sep":9,"Oct":10,"Nov":11,"Dec":12}
        d,mo,y,H,M,S = int(m.group(1)), months[m.group(2)], int(m.group(3)), int(m.group(4)), int(m.group(5)), int(m.group(6))
        return datetime.datetime(y,mo,d,H,M,S)
    # ISO: "2026-07-19T06:45:12" or with Z
    m = re.match(r"(\d{4})-(\d{2})-(\d{2})T(\d{2}):(\d{2}):(\d{2})", pub)
    if m:
        return datetime.datetime(*[int(x) for x in m.groups()])
    return None

# ---- re-parse all md files to get title+pubdate+pir per article ----
all_items = []  # (source_key, title, pubdate_str, pubdate_dt, pirs, link, prn)
for s in R["sources"]:
    key = s["source"]
    fname = s["file"]
    fpath = os.path.join(BASE, fname)
    if not os.path.exists(fpath): continue
    txt = open(fpath, encoding="utf-8").read()
    # split on "### " headers
    chunks = re.split(r"\n### ", txt)
    for ch in chunks[1:]:
        # first line = "[PRIORITY PIR-XX] Title" or "Title"
        line1 = ch.split("\n",1)[0]
        mp = re.match(r"\[PRIORITY ([^\]]+)\]\s*(.+)", line1)
        if mp:
            pirs = mp.group(1).split("+")
            title = mp.group(2).strip()
        else:
            pirs = []
            title = line1.strip()
        # extract URL / PubDate / Publisher
        link = ""
        pub = ""
        src = ""
        pm = re.search(r"\nURL:\s*(\S+)", ch)
        if pm: link = pm.group(1)
        pm = re.search(r"\nPubDate:\s*(.+)", ch)
        if pm: pub = pm.group(1).strip()
        pm = re.search(r"\nPublisher:\s*(.+)", ch)
        if pm: src = pm.group(1).strip()
        pdt = parse_pubdate(pub)
        all_items.append({"source_key":key,"title":title,"pubdate":pub,"pdt":pdt,
                          "pirs":pirs,"link":link,"publisher":src})

# also parse universal gnews files
for u in R.get("universal_gnews_files", []):
    fname = u["file"]
    fpath = os.path.join(BASE, fname)
    if not os.path.exists(fpath): continue
    txt = open(fpath, encoding="utf-8").read()
    chunks = re.split(r"\n### ", txt)
    for ch in chunks[1:]:
        line1 = ch.split("\n",1)[0]
        mp = re.match(r"\[PRIORITY ([^\]]+)\]\s*(.+)", line1)
        if mp:
            pirs = mp.group(1).split("+"); title = mp.group(2).strip()
        else:
            pirs = []; title = line1.strip()
        link = ""; pub = ""; src = ""
        pm = re.search(r"\ngnews URL:\s*(\S+)", ch)
        if pm: link = pm.group(1)
        pm = re.search(r"\nPubDate:\s*(.+)", ch)
        if pm: pub = pm.group(1).strip()
        pm = re.search(r"\nPublisher:\s*(.+)", ch)
        if pm: src = pm.group(1).strip()
        pdt = parse_pubdate(pub)
        all_items.append({"source_key":f"univ_{u['ukey']}","title":title,"pubdate":pub,"pdt":pdt,
                          "pirs":pirs,"link":link,"publisher":src})

print(f"Total items re-parsed from md files: {len(all_items)}")

# ---- de-dup by normalized title ----
seen = {}
for it in all_items:
    k = norm(it["title"])
    if k not in seen:
        seen[k] = it
uniq = list(seen.values())
print(f"Unique titles: {len(uniq)}")

# ---- freshness: items with pdt >= CUTOFF ----
fresh = [it for it in uniq if it["pdt"] and it["pdt"] >= CUTOFF]
fresh.sort(key=lambda x: x["pdt"], reverse=True)
print(f"\n=== FRESH items (pubDate >= {CUTOFF} UTC = 07:00 MYT 19 Jul): {len(fresh)} ===")
for it in fresh:
    pirs = ",".join(it["pirs"]) if it["pirs"] else "-"
    print(f"  {it['pdt']} | {pirs:16} | [{it['source_key']}] {it['title'][:95]}")

# ---- genuinely new (priority title not in prior cycle set) ----
new_pri = [it for it in uniq if it["pirs"] and norm(it["title"]) not in prior_titles]
print(f"\n=== GENUINELY NEW priority titles (not in prior cycle 231029): {len(new_pri)} ===")
# sort by pdt desc if available
new_pri.sort(key=lambda x: x["pdt"] or datetime.datetime(2000,1,1), reverse=True)
for it in new_pri[:60]:
    pirs = ",".join(it["pirs"])
    pd = it["pdt"].strftime("%m-%d %H:%M UTC") if it["pdt"] else "?"
    print(f"  {pd:14} | {pirs:16} | [{it['source_key']:22}] {it['title'][:90]}")

# ---- focus: fresh + priority + PIR-06/09/07 (candidates for full-text fetch) ----
fetch_candidates = [it for it in fresh if it["pirs"] and
                    ("PIR-06" in it["pirs"] or "PIR-09" in it["pirs"] or "PIR-07" in it["pirs"])]
print(f"\n=== FETCH CANDIDATES (fresh + PIR-tagged): {len(fetch_candidates)} ===")
for it in fetch_candidates:
    pirs = ",".join(it["pirs"])
    pd = it["pdt"].strftime("%m-%d %H:%M UTC") if it["pdt"] else "?"
    print(f"  {pd:14} | {pirs:16} | [{it['source_key']:22}] {it['title'][:85]}")
    print(f"        link: {it['link'][:110]}")

# ---- write candidates json for the fetcher ----
out = {
    "cycle": TS,
    "cutoff_utc": CUTOFF.isoformat(),
    "cutoff_myt": "2026-07-19 07:00 MYT",
    "total_items_reparsed": len(all_items),
    "unique_titles": len(uniq),
    "fresh_items_count": len(fresh),
    "genuinely_new_priority_count": len(new_pri),
    "fetch_candidates": fetch_candidates,
    "fresh_items": [{"title":i["title"],"pubdate":i["pubdate"],"pdt":i["pdt"].isoformat() if i["pdt"] else None,
                     "pirs":i["pirs"],"source_key":i["source_key"],"link":i["link"],"publisher":i["publisher"]} for i in fresh],
    "genuinely_new_priority": [{"title":i["title"],"pubdate":i["pubdate"],"pdt":i["pdt"].isoformat() if i["pdt"] else None,
                                "pirs":i["pirs"],"source_key":i["source_key"],"link":i["link"],"publisher":i["publisher"]} for i in new_pri],
}
with open(os.path.join(BASE, f"_freshness_analysis_{TS}.json"),"w",encoding="utf-8") as f:
    json.dump(out, f, ensure_ascii=False, indent=2)
print(f"\nWrote _freshness_analysis_{TS}.json")
