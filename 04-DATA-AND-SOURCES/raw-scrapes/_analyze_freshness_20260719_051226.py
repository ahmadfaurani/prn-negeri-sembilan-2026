#!/usr/bin/env python3
"""Freshness analysis for cycle 20260719_051226 (13:12 MYT 19 Jul).
Compare this cycle's titles vs prior 20260719_034922 cycle (11:49 MYT).
Identify genuinely-new priority titles (absent from prior cycle) and
candidate full-text fetch targets published after the prior cutoff
(2026-07-19T03:49:22 UTC = 11:49 MYT).
"""
import json, re, datetime, os, glob

BASE = "/home/p62operator/.openclaw/workspace-ns/04-DATA-AND-SOURCES/raw-scrapes/20260719"
THIS_TS = "20260719_051226"
PRIOR_TS = "20260719_034922"
CUTOFF_UTC = "2026-07-19T03:49:22"   # prior cycle timestamp UTC
CUTOFF_MYT = "2026-07-19 11:49 MYT"

def parse_md_for_articles(md_path):
    out = []
    try:
        with open(md_path, encoding="utf-8") as f:
            txt = f.read()
    except Exception:
        return out
    blocks = re.split(r"\n### ", txt)
    for b in blocks[1:]:
        lines = b.splitlines()
        head = lines[0].strip() if lines else ""
        if not head: continue
        prefix = ""
        m = re.match(r"(\[PRIORITY[^\]]*\])\s*(.*)", head)
        if m:
            prefix = m.group(1)
            title = m.group(2).strip()
        else:
            title = head
        url = ""; pub = ""
        for ln in lines[1:8]:
            if ln.startswith("URL:"): url = ln[4:].strip()
            elif ln.startswith("PubDate:"): pub = ln[8:].strip()
            elif ln.startswith("gnews URL:"): url = ln[10:].strip()
        out.append({"title":title, "url":url, "pubdate":pub, "prefix":prefix})
    return out

# Collect this-cycle articles from all freshly-written md files
this_articles = []
for md in sorted(glob.glob(os.path.join(BASE, f"*_{THIS_TS}.md"))):
    arts = parse_md_for_articles(md)
    src_key = os.path.basename(md).replace(f"_{THIS_TS}.md","")
    for a in arts:
        a["source_key"] = src_key
        this_articles.append(a)

# Prior-cycle titles (normalized)
prior_titles_norm = set()
prior_path_json = os.path.join(BASE, f"_scrape_results_{PRIOR_TS}.json")
if os.path.exists(prior_path_json):
    with open(prior_path_json, encoding="utf-8") as f:
        pj = json.load(f)
    for s in pj.get("sources", []):
        for t in s.get("priority_titles", []):
            prior_titles_norm.add(re.sub(r"\s+"," ",t.lower()).strip())
for md in sorted(glob.glob(os.path.join(BASE, f"*_{PRIOR_TS}.md"))):
    arts = parse_md_for_articles(md)
    for a in arts:
        prior_titles_norm.add(re.sub(r"\s+"," ",a["title"].lower()).strip())

# Genuinely-new
genuinely_new = []
for a in this_articles:
    n = re.sub(r"\s+"," ",a["title"].lower()).strip()
    if n not in prior_titles_norm:
        a["norm"] = n
        genuinely_new.append(a)

new_priority = [a for a in genuinely_new if a["prefix"]]

def parse_pub_utc(pub):
    if not pub: return None
    for fmt in ("%a, %d %b %Y %H:%M:%S %Z", "%Y-%m-%dT%H:%M:%S%z",
                "%Y-%m-%dT%H:%M:%S", "%Y-%m-%d %H:%M:%S"):
        try:
            dt = datetime.datetime.strptime(pub, fmt)
            if dt.tzinfo is None:
                dt = dt.replace(tzinfo=datetime.timezone.utc)
            return dt
        except Exception:
            pass
    return None

cutoff_dt = datetime.datetime.fromisoformat("2026-07-19T03:49:22+00:00")
fresh_after_cutoff = []
for a in new_priority:
    pdt = parse_pub_utc(a["pubdate"])
    a["pub_utc"] = pdt
    if pdt and pdt >= cutoff_dt:
        fresh_after_cutoff.append(a)

# False-positive filter
FP_RE = re.compile(r"(keluar\s*(rm|wang|\$|rm\d|duit|baiki|untuk)|exit\s*poll|withdraws?\s+(from\s+)?(race|sikamat|documents)|sacked\s+(for|over))", re.I)
real_new_priority = [a for a in new_priority if not FP_RE.search(a["title"])]

def is_real_url(u):
    if not u: return False
    if u.startswith("https://news.google.com/rss/articles/"): return False
    if u.startswith("https://news.google.com/"): return False
    return True

fetch_candidates = [a for a in real_new_priority if is_real_url(a["url"])]
fetch_candidates.sort(key=lambda a: (a["pub_utc"] or datetime.datetime.min.replace(tzinfo=datetime.timezone.utc)), reverse=True)

result = {
    "cycle": THIS_TS, "prior_cycle": PRIOR_TS,
    "cutoff_utc": CUTOFF_UTC, "cutoff_myt": CUTOFF_MYT,
    "this_cycle_total_articles": len(this_articles),
    "prior_cycle_unique_titles": len(prior_titles_norm),
    "genuinely_new_titles_count": len(genuinely_new),
    "genuinely_new_priority_titles_count": len(new_priority),
    "real_new_priority_after_falsepos_filter": len(real_new_priority),
    "fresh_priority_items_after_cutoff_count": len(fresh_after_cutoff),
    "fetch_candidates_count": len(fetch_candidates),
    "fresh_priority_items_after_cutoff": [
        {"title":a["title"],"source":a["source_key"],"url":a["url"],"pubdate":a["pubdate"],"prefix":a["prefix"]}
        for a in fresh_after_cutoff[:40]
    ],
    "genuinely_new_priority_items_top25": [
        {"title":a["title"],"source":a["source_key"],"url":a["url"],"pubdate":a["pubdate"],"prefix":a["prefix"]}
        for a in real_new_priority[:25]
    ],
    "fetch_candidates_top20": [
        {"title":a["title"],"source":a["source_key"],"url":a["url"],"pubdate":a["pubdate"],"prefix":a["prefix"]}
        for a in fetch_candidates[:20]
    ],
}
out_path = os.path.join(BASE, f"_freshness_analysis_{THIS_TS}.json")
with open(out_path, "w", encoding="utf-8") as f:
    json.dump(result, f, ensure_ascii=False, indent=2)

print(f"=== FRESHNESS ANALYSIS {THIS_TS} (vs {PRIOR_TS}) ===")
print(f"cutoff: {CUTOFF_UTC} UTC / {CUTOFF_MYT}")
print(f"this_cycle_articles: {len(this_articles)}")
print(f"prior_unique_titles: {len(prior_titles_norm)}")
print(f"genuinely_new_titles: {len(genuinely_new)}")
print(f"genuinely_new_PRIORITY_titles: {len(new_priority)}")
print(f"after false-positive filter: {len(real_new_priority)}")
print(f"FRESH priority items pub AFTER cutoff: {len(fresh_after_cutoff)}")
print(f"fetch_candidates (real URL): {len(fetch_candidates)}")
print()
print("=== FRESH PRIORITY ITEMS (pubdate >= cutoff 11:49 MYT) ===")
for a in fresh_after_cutoff[:25]:
    print(f"  [{a['source_key']}] {a['pubdate']}")
    print(f"     {a['prefix']} {a['title']}")
    print(f"     {a['url']}")
print()
print("=== GENUINELY-NEW PRIORITY (top 25, any pubdate) ===")
for a in real_new_priority[:25]:
    print(f"  [{a['source_key']}] {a['pubdate'] or '(no pubdate)'} {a['prefix']} {a['title'][:100]}")
    print(f"     {a['url']}")
print()
print(f"Wrote {out_path}")
