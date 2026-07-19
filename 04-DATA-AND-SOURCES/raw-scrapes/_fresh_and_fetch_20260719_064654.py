#!/usr/bin/env python3
"""Freshness analysis + priority full-text fetch for cycle 20260719_064654 (14:46 MYT 19 Jul).
Compare this cycle's titles vs prior 20260719_051226 cycle (13:12 MYT).
Identify genuinely-new priority titles and fetch full text via proven methods:
  - FMT RSS (curl-friendly, full text via WordPress)
  - NST WordPress feed (nst.com.my/feed, content:encoded)
  - mkini + Utusan direct URLs (may be paywalled)
  - gnews headline intelligence (title+pubdate+source) for unreachable items
TLP:AMBER. All content carries source URL.
"""
import subprocess, re, datetime, json, os, html, glob
from urllib.parse import urljoin

BASE = "/home/p62operator/.openclaw/workspace-ns/04-DATA-AND-SOURCES/raw-scrapes/20260719"
THIS_TS = "20260719_064654"
PRIOR_TS = "20260719_051226"
TODAY = "20260719"
TS_TIME = "064654"
CUTOFF_UTC = "2026-07-19T05:12:26"
CUTOFF_MYT = "2026-07-19 13:12 MYT"
NOW_ISO = datetime.datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S UTC")
NOW_MYT = (datetime.datetime.utcnow()+datetime.timedelta(hours=8)).strftime("%H:%M MYT %d %b %Y")
UA = ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36")

def curl(url, timeout=35):
    cmd = ["curl","-sS","-L","-m",str(timeout),"-A",UA,"--compressed",
           "-H","Accept-Language: en-US,en;q=0.9,ms;q=0.8",
           "-H","Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
           "-w","\n__HTTPCODE__:%{http_code}\n__FINALURL__:%{url_effective}",
           url]
    try:
        p = subprocess.run(cmd, capture_output=True, timeout=timeout+10)
    except subprocess.TimeoutExpired:
        return "TIMEOUT", b"", url
    out = p.stdout
    m = re.search(rb"__HTTPCODE__:(\d+)", out)
    code = m.group(1).decode() if m else "ERR"
    mu = re.search(rb"__FINALURL__:(\S+)", out)
    final = mu.group(1).decode("utf-8","replace").strip() if mu else url
    body = out[:m.start()] if m else out
    return code, body, final

# ============================================================
# PART A: FRESHNESS ANALYSIS
# ============================================================
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
        out.append({"title":title,"url":url,"pubdate":pub,"prefix":prefix})
    return out

this_articles = []
for md in sorted(glob.glob(os.path.join(BASE, f"_{THIS_TS}.md"))) + \
             sorted(glob.glob(os.path.join(BASE, f"*{THIS_TS}.md"))):
    arts = parse_md_for_articles(md)
    src_key = os.path.basename(md).replace(f"_{THIS_TS}.md","")
    for a in arts:
        a["source_key"] = src_key
        this_articles.append(a)

prior_titles_norm = set()
prior_path_json = os.path.join(BASE, f"_scrape_results_{PRIOR_TS}.json")
if os.path.exists(prior_path_json):
    with open(prior_path_json, encoding="utf-8") as f:
        pj = json.load(f)
    for s in pj.get("sources", []):
        for t in s.get("priority_titles", []):
            prior_titles_norm.add(re.sub(r"\s+"," ",t.lower()).strip())
for md in sorted(glob.glob(os.path.join(BASE, f"*{PRIOR_TS}.md"))):
    arts = parse_md_for_articles(md)
    for a in arts:
        prior_titles_norm.add(re.sub(r"\s+"," ",a["title"].lower()).strip())
# Also include all prior-cycle priority file slugs to avoid re-fetching
for pf in glob.glob(os.path.join(BASE, f"priority_*{PRIOR_TS}.md")):
    base = os.path.basename(pf)
    # extract slug between pir-XX_ and _20260719
    m = re.search(r"_(.*?)_20260719_", base)
    if m: prior_titles_norm.add(m.group(1).lower().replace("-"," "))

genuinely_new = []
for a in this_articles:
    n = re.sub(r"\s+"," ",a["title"].lower()).strip()
    if n not in prior_titles_norm:
        a["norm"] = n
        genuinely_new.append(a)

new_priority = [a for a in genuinely_new if a["prefix"]]

def parse_pub_utc(pub):
    if not pub: return None
    for fmt in ("%a, %d %b %Y %H:%M:%S %Z","%Y-%m-%dT%H:%M:%S%z","%Y-%m-%dT%H:%M:%S","%Y-%m-%d %H:%M:%S"):
        try:
            dt = datetime.datetime.strptime(pub, fmt)
            if dt.tzinfo is None:
                dt = dt.replace(tzinfo=datetime.timezone.utc)
            return dt
        except Exception:
            pass
    return None

cutoff_dt = datetime.datetime.fromisoformat("2026-07-19T05:12:26+00:00")
fresh_after_cutoff = []
for a in new_priority:
    pd = parse_pub_utc(a["pubdate"])
    if pd and pd >= cutoff_dt:
        fresh_after_cutoff.append(a)

print(f"=== FRESHNESS: {THIS_TS} vs {PRIOR_TS} ===")
print(f"This-cycle articles (all): {len(this_articles)}")
print(f"Prior-cycle titles set: {len(prior_titles_norm)}")
print(f"Genuinely-new (not in prior): {len(genuinely_new)}")
print(f"Genuinely-new PRIORITY: {len(new_priority)}")
print(f"Fresh (pubdate >= 13:12 MYT cutoff): {len(fresh_after_cutoff)}")
print()
print("--- Genuinely-new PRIORITY titles (top 80) ---")
for a in new_priority[:80]:
    src = a.get("source_key","")[:22]
    pub = a.get("pubdate","")[:25]
    print(f"  [{a['prefix'][:18]:18}] {src:22} | {pub:25} | {a['title'][:90]}")
print()

# Save freshness JSON
fj = {
    "this_ts": THIS_TS, "prior_ts": PRIOR_TS,
    "this_articles": len(this_articles),
    "genuinely_new": len(genuinely_new),
    "new_priority": len(new_priority),
    "fresh_after_cutoff": len(fresh_after_cutoff),
    "new_priority_titles": [a["title"] for a in new_priority],
    "fresh_titles": [a["title"] for a in fresh_after_cutoff],
}
with open(os.path.join(BASE, f"_freshness_analysis_{THIS_TS}.json"),"w") as f:
    json.dump(fj, f, indent=2, ensure_ascii=False)

# ============================================================
# PART B: ARTICLE BODY EXTRACTOR (full text)
# ============================================================
def extract_article(body):
    try:
        from bs4 import BeautifulSoup
    except Exception:
        return "","","",""
    try:
        soup = BeautifulSoup(body.decode("utf-8","replace"), "html.parser")
    except Exception:
        return "","","",""
    title = ""
    if soup.title and soup.title.string: title = soup.title.string.strip()
    og = soup.find("meta", property="og:title")
    if og and og.get("content"): title = og["content"].strip()
    desc = ""
    md = soup.find("meta", attrs={"name":"description"}) or soup.find("meta", property="og:description")
    if md and md.get("content"): desc = md["content"].strip()
    pub = ""
    for sel in ['meta[property="article:published_time"]','meta[name="pubdate"]','meta[name="date"]',
                'meta[itemprop="datePublished"]','time[datetime]']:
        n = soup.select_one(sel)
        if n and (n.get("content") or n.get("datetime")):
            pub = n.get("content") or n.get("datetime"); break
    text_parts = []
    selectors = ["div.elementor-widget-theme-post-content",
                 "div.elementor-widget-container div.elementor-element",
                 "article","div.article-content","div.article-body","div.entry-content",
                 "div.post-content","div.content__body","div.field-body","div.story-body",
                 "div#article-body","div.article","main","div.td-post-content",
                 "div.almbe-article-body","div.posts","section.article","div.content-post",
                 "div.single-content","div.news-detail","div.kcontent","div.body-content","div#content"]
    for sel in selectors:
        nodes = soup.select(sel)
        for node in nodes:
            for p in node.find_all(["p","li","h2","h3","blockquote"]):
                t = p.get_text(" ", strip=True)
                if t and len(t) > 25: text_parts.append(t)
            if text_parts: break
        if text_parts: break
    if not text_parts:
        for p in soup.find_all("p"):
            t = p.get_text(" ", strip=True)
            if t and len(t) > 40: text_parts.append(t)
    return title[:300], "\n\n".join(text_parts[:140])[:28000], (desc or "")[:800], pub

results = []
def save_article(pir, slug, url, final, code, body_bytes, note, mode):
    title, body_text, desc, pub = ("","","","")
    body_len = 0; ok = False
    if str(code) == "200":
        title, body_text, desc, pub = extract_article(body_bytes)
        body_len = len(body_text)
        if body_len > 150: ok = True
    fname = f"priority_{pir.lower().replace('+','-')}_{slug}_{TODAY}_{TS_TIME}.md"
    lines = [f"# [PRIORITY {pir}] {slug}",
             f"Source URL: {url}", f"Final/redirected URL: {final}",
             f"Collected: {TODAY} {THIS_TS} UTC ({NOW_ISO}) | MYT: {NOW_MYT}",
             f"Classification: TLP:AMBER", f"HTTP: {code} | mode: {mode}",
             f"Note: {note}", f"Title: {title}"]
    if pub: lines.append(f"ArticlePubDate: {pub}")
    if desc: lines.append(f"Description: {desc}")
    lines += [f"Body chars: {body_len}", "", "## Full text", "="*78,
              (body_text if body_text else "(no body extracted — possibly paywalled or JS-rendered)"),
              "="*78]
    with open(os.path.join(BASE, fname),"w",encoding="utf-8") as f:
        f.write("\n".join(lines))
    print(f"  [{pir}] {slug[:55]:55} | HTTP {code} | {'ok' if ok else 'thin/no-body'} | body={body_len} | {fname}")
    results.append({"pir":pir,"slug":slug,"file":fname,"http":code,"ok":ok,
                    "body_len":body_len,"title":title,"final":final,"pub":pub,"mode":mode})

# ============================================================
# PART C: FMT RSS FULL-TEXT FETCH (proven curl-friendly)
# ============================================================
print("\n=== PART C: FMT RSS fetch ===")
FMT_FEED = "https://www.freemalaysiatoday.com/feed/"
code, body, final = curl(FMT_FEED, timeout=35)
fmt_items = []
if str(code) == "200":
    txt = body.decode("utf-8","replace")
    for m in re.finditer(r"<item>(.*?)</item>", txt, re.S):
        block = m.group(1)
        tm = re.search(r"<title>(?:<!\[CDATA\[)?(.*?)(?:\]\]>)?</title>", block, re.S)
        lm = re.search(r"<link>(.*?)</link>", block, re.S)
        pm = re.search(r"<pubDate>(.*?)</pubDate>", block, re.S)
        cm = re.search(r"<content:encoded>(?:<!\[CDATA\[)?(.*?)(?:\]\]>)?</content:encoded>", block, re.S)
        title = html.unescape(re.sub(r"\s+"," ",tm.group(1))).strip() if tm else ""
        link = lm.group(1).strip() if lm else ""
        pub = pm.group(1).strip() if pm else ""
        content = cm.group(1) if cm else ""
        if title: fmt_items.append({"title":title,"link":link,"pubdate":pub,"content":content})

# NS/PRN/Bersatu/PN-relevant FMT articles
NS_RE = re.compile(r"(negeri\s*sembilan|negri\s*sembilan|prn|bersatu|perikatan|loke|tok\s*mat|hadi|muhyiddin|aminuddin|zahid|anwar|mca|dap|melaka|linggi|sikamat|ampangan|rantau|nilai|sri\s*tanjung|chennah|kerusi|calon|nomination|polls|umb|malay\s*unity|green\s*wave)", re.I)
fmt_ns = [it for it in fmt_items if NS_RE.search(it["title"])]
print(f"FMT RSS items: {len(fmt_items)} total | NS/PRN-relevant: {len(fmt_ns)}")

# Determine which FMT NS titles are genuinely new vs prior cycle
prior_slugs_norm = set()
for a in genuinely_new:
    prior_slugs_norm.add(a["norm"])  # actually these are new
# We want FMT items whose titles are NOT in prior cycle. Compare to prior_titles_norm
fmt_new = []
for it in fmt_ns:
    n = re.sub(r"\s+"," ",it["title"].lower()).strip()
    if n not in prior_titles_norm:
        fmt_new.append(it)
print(f"FMT NS-relevant & genuinely-new: {len(fmt_new)}")
for it in fmt_new[:40]:
    print(f"  FMT | {it['pubdate'][:25]:25} | {it['title'][:95]}")

def strip_html(s):
    return re.sub(r"<[^>]+>","", html.unescape(s or ""))

for it in fmt_new:
    title = it["title"]
    link = it["link"]
    # PIR classification
    pirs = []
    if re.search(r"(pecat|keluar|buang|tarik\s*diri|muhyiddin|hadi|bersatu|pn|perikatan|merger|new\s*coali|expell|sack|machinery|joint|ceramah|stage)", title, re.I): pirs.append("PIR-06")
    if re.search(r"(battleground|kerusi\s*tumpuan|marquee|marginal|majority\s*tipis|defector|5\s*corner|tiga\s*penjuru|linggi|sikamat|ampangan|nilai|sri\s*tanjung|chennah|rantau|chembong|klawang|labu|juasseh|calon|nomination|seat|polls)", title, re.I): pirs.append("PIR-07")
    if re.search(r"(narrative|loke|adat|melaka|fled|aminuddin|barking|albert|graft|corruption|majoriti|mb\s*after|sole\s*opposition|malay\s*unity|penyatuan|mca|dap\s*acceptance|green\s*wave|islamophobia)", title, re.I): pirs.append("PIR-16")
    if not pirs: pirs = ["PIR-07"]
    pir = "+".join(pirs)
    slug = re.sub(r"[^a-z0-9]+","-",title.lower()).strip("-")[:80]
    # Use content:encoded if present (full text), else fetch
    if it["content"] and len(it["content"]) > 300:
        body_text = strip_html(it["content"])[:28000]
        body_len = len(body_text)
        ok = body_len > 150
        fname = f"priority_{pir.lower().replace('+','-')}_{slug}_{TODAY}_{TS_TIME}.md"
        lines = [f"# [PRIORITY {pir}] {slug}",
                 f"Source URL: {link}", f"Final/redirected URL: {link}",
                 f"Collected: {TODAY} {THIS_TS} UTC ({NOW_ISO}) | MYT: {NOW_MYT}",
                 f"Classification: TLP:AMBER", f"HTTP: 200 | mode: fmt-rss-content",
                 f"Note: Full text from FMT RSS content:encoded (no curl fetch needed)",
                 f"Title: {title}", f"ArticlePubDate: {it['pubdate']}",
                 f"Body chars: {body_len}", "", "## Full text", "="*78, body_text, "="*78]
        with open(os.path.join(BASE, fname),"w",encoding="utf-8") as f:
            f.write("\n".join(lines))
        print(f"  [{pir}] {slug[:55]:55} | RSS-OK | {'ok' if ok else 'thin'} | body={body_len} | {fname}")
        results.append({"pir":pir,"slug":slug,"file":fname,"http":"200","ok":ok,
                        "body_len":body_len,"title":title,"final":link,"pub":it['pubdate'],"mode":"fmt-rss"})
    else:
        # Direct fetch
        code, body, final = curl(link, timeout=30)
        save_article(pir, slug, link, final, code, body, "FMT direct (RSS content thin)", mode="fmt-direct")

# ============================================================
# PART D: NST WORDPRESS FEED (nst.com.my/feed, content:encoded)
# ============================================================
print("\n=== PART D: NST WordPress feed fetch ===")
NST_FEED = "https://www.nst.com.my/feed"
code, body, final = curl(NST_FEED, timeout=35)
nst_items = []
if str(code) == "200":
    txt = body.decode("utf-8","replace")
    for m in re.finditer(r"<item>(.*?)</item>", txt, re.S):
        block = m.group(1)
        tm = re.search(r"<title>(?:<!\[CDATA\[)?(.*?)(?:\]\]>)?</title>", block, re.S)
        lm = re.search(r"<link>(.*?)</link>", block, re.S)
        pm = re.search(r"<pubDate>(.*?)</pubDate>", block, re.S)
        cm = re.search(r"<content:encoded>(?:<!\[CDATA\[)?(.*?)(?:\]\]>)?</content:encoded>", block, re.S)
        title = html.unescape(re.sub(r"\s+"," ",tm.group(1))).strip() if tm else ""
        link = lm.group(1).strip() if lm else ""
        pub = pm.group(1).strip() if pm else ""
        content = cm.group(1) if cm else ""
        if title: nst_items.append({"title":title,"link":link,"pubdate":pub,"content":content})

nst_ns = [it for it in nst_items if NS_RE.search(it["title"])]
print(f"NST feed items: {len(nst_items)} total | NS-relevant: {len(nst_ns)}")
nst_new = []
for it in nst_ns:
    n = re.sub(r"\s+"," ",it["title"].lower()).strip()
    if n not in prior_titles_norm:
        nst_new.append(it)
print(f"NST NS-relevant & genuinely-new: {len(nst_new)}")
for it in nst_new[:30]:
    print(f"  NST | {it['pubdate'][:25]:25} | {it['title'][:95]}")

for it in nst_new:
    title = it["title"]; link = it["link"]
    pirs = []
    if re.search(r"(pecat|keluar|buang|tarik\s*diri|muhyiddin|hadi|bersatu|pn|perikatan|merger|new\s*coali|expell|sack|machinery|joint|ceramah|stage|understanding|pact)", title, re.I): pirs.append("PIR-06")
    if re.search(r"(battleground|kerusi\s*tumpuan|marquee|marginal|majority\s*tipis|defector|5\s*corner|tiga\s*penjuru|linggi|sikamat|ampangan|nilai|sri\s*tanjung|chennah|rantau|chembong|klawang|labu|juasseh|calon|nomination|seat|polls|police|permit)", title, re.I): pirs.append("PIR-07")
    if re.search(r"(narrative|loke|adat|melaka|fled|aminuddin|barking|albert|graft|corruption|majoriti|mb\s*after|sole\s*opposition|malay\s*unity|mca|dap\s*acceptance|green\s*wave|islamophobia|traitor)", title, re.I): pirs.append("PIR-16")
    if not pirs: pirs = ["PIR-07"]
    pir = "+".join(pirs)
    slug = re.sub(r"[^a-z0-9]+","-",title.lower()).strip("-")[:80]
    if it["content"] and len(it["content"]) > 300:
        body_text = strip_html(it["content"])[:28000]
        body_len = len(body_text)
        ok = body_len > 150
        fname = f"priority_{pir.lower().replace('+','-')}_{slug}_{TODAY}_{TS_TIME}.md"
        lines = [f"# [PRIORITY {pir}] {slug}",
                 f"Source URL: {link}", f"Final/redirected URL: {link}",
                 f"Collected: {TODAY} {THIS_TS} UTC ({NOW_ISO}) | MYT: {NOW_MYT}",
                 f"Classification: TLP:AMBER", f"HTTP: 200 | mode: nst-feed-content",
                 f"Note: Full text from NST WordPress feed content:encoded",
                 f"Title: {title}", f"ArticlePubDate: {it['pubdate']}",
                 f"Body chars: {body_len}", "", "## Full text", "="*78, body_text, "="*78]
        with open(os.path.join(BASE, fname),"w",encoding="utf-8") as f:
            f.write("\n".join(lines))
        print(f"  [{pir}] {slug[:55]:55} | FEED-OK | {'ok' if ok else 'thin'} | body={body_len} | {fname}")
        results.append({"pir":pir,"slug":slug,"file":fname,"http":"200","ok":ok,
                        "body_len":body_len,"title":title,"final":link,"pub":it['pubdate'],"mode":"nst-feed"})
    else:
        code, body, final = curl(link, timeout=30)
        save_article(pir, slug, link, final, code, body, "NST direct (feed content thin)", mode="nst-direct")

# ============================================================
# PART E: DIRECT FETCHES for known high-value URLs (mkini/Utusan/Awani/BH)
# ============================================================
print("\n=== PART E: Direct real-URL fetches (mkini/Utusan/Awani) ===")
DIRECT = [
    # mkini — check for fresh article IDs (780073 Loke was prior cycle; try newer)
    ("PIR-16+PIR-07","mkini-loke-malay-votes-mca-biggest-loser-retry",
     "https://www.malaysiakini.com/news/780073",
     "Retry mkini 780073 Loke Malay votes MCA biggest loser (prior was paywalled preview)."),
    ("PIR-16+PIR-07","mkini-zan-azlee-indicator-retry",
     "https://www.malaysiakinicom/columns/780063",
     "Retry mkini 780063 Zan Azlee indicator."),
]
for pir, slug, url, note in DIRECT:
    print(f"  fetch -> {url[:75]}")
    code, body, final = curl(url, timeout=35)
    save_article(pir, slug, url, final, code, body, note, mode="direct")

# ============================================================
# PART F: GNEWS HEADLINE INTELLIGENCE for genuinely-new priority titles
# (capture title+pubdate+source for items we can't resolve via curl)
# ============================================================
print("\n=== PART F: gnews headline intelligence for genuinely-new priority titles ===")
gn_saved = 0
for a in new_priority:
    # Skip if already covered by FMT/NST feed fetch above
    title_lower = a["title"].lower()
    if any(r.get("title","").lower() == title_lower for r in results):
        continue
    src = a.get("source_key","")
    # Only save gnews-origin items (those whose URL is a gnews link or empty)
    url = a.get("url","")
    if "news.google.com" in url or not url:
        pir_label = a["prefix"].strip("[]").replace("PRIORITY ","")
        slug = re.sub(r"[^a-z0-9]+","-",a["title"].lower()).strip("-")[:80]
        fname = f"priority_{pir_label.lower().replace('+','-')}_{slug}_{TODAY}_{TS_TIME}.md"
        lines = [f"# [PRIORITY {pir_label}] {slug}",
                 f"Source URL: {url}",
                 f"Collected: {TODAY} {THIS_TS} UTC ({NOW_ISO}) | MYT: {NOW_MYT}",
                 f"Classification: TLP:AMBER", f"HTTP: n/a | mode: gnews-headline-intel",
                 f"Note: Headline intelligence from gnews RSS (full-text URL not curl-resolvable; JS-rendered intermediate).",
                 f"Title: {a['title']}"]
        if a.get("pubdate"): lines.append(f"PubDate: {a['pubdate']}")
        lines += [f"Source-key: {src}", "", "## Headline intelligence (no full text — gnews JS-render block)",
                  "="*78, f"TITLE: {a['title']}", f"PUBDATE: {a.get('pubdate','')}",
                  f"SOURCE: {src}", "="*78]
        with open(os.path.join(BASE, fname),"w",encoding="utf-8") as f:
            f.write("\n".join(lines))
        gn_saved += 1
print(f"gnews headline-intelligence files saved: {gn_saved}")

# ============================================================
# SUMMARY
# ============================================================
print("\n" + "="*70)
print(f"=== CYCLE {THIS_TS} SUMMARY ===")
print(f"Total priority files created: {len(results) + gn_saved}")
print(f"  Full-text (body>150c): {sum(1 for r in results if r.get('ok'))}")
print(f"  Thin/no-body: {sum(1 for r in results if not r.get('ok'))}")
print(f"  gnews headline-intel: {gn_saved}")
ok_bodies = [r for r in results if r.get("ok")]
total_chars = sum(r.get("body_len",0) for r in ok_bodies)
print(f"Total body chars (full-text): {total_chars}")

# Save results JSON
with open(os.path.join(BASE, f"_priority_fetch_results_{THIS_TS}.json"),"w") as f:
    json.dump({"results":results,"gnews_intel_count":gn_saved,
               "freshness":{"genuinely_new":len(genuinely_new),"new_priority":len(new_priority),
                            "fresh_after_cutoff":len(fresh_after_cutoff)}}, f, indent=2, ensure_ascii=False)
print(f"Saved _priority_fetch_results_{THIS_TS}.json")
print("DONE.")
