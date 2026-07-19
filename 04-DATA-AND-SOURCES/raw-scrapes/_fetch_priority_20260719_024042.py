#!/usr/bin/env python3
"""Priority full-text fetcher for cycle 20260719_024042 (10:40 MYT 19 Jul).
Fetches genuinely-fresh / high-value Day-1 articles published after the prior
011915 cycle (09:19 MYT 19 Jul), plus recovery of Day-1 campaign-ops items.

Targets (real URLs only; gnews-protobuf items captured as headline intelligence):
  - mkini Zan Azlee commentary (fresh ~09:56 MYT, PIR-07)
  - astroawani 'Polis lulus 19 permit ceramah kempen' (Day-1 campaign ops, PIR-07)

Outputs priority_pirXX_*.md with Elementor-aware + generic extraction.
TLP:AMBER. All content carries source URL.
"""
import subprocess, re, datetime, json, os
from bs4 import BeautifulSoup

BASE = "/home/p62operator/.openclaw/workspace-ns/04-DATA-AND-SOURCES/raw-scrapes/20260719"
TS = "20260719_024042"
TODAY = "20260719"
TS_TIME = "024042"
NOW_ISO = datetime.datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S UTC")
NOW_MYT = (datetime.datetime.utcnow()+datetime.timedelta(hours=8)).strftime("%H:%M MYT %d %b %Y")
UA = ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36")

# (pir, slug, url, note)
TARGETS = [
    ("PIR-07","mkini-zan-azlee-indicator-commentary",
     "https://www.malaysiakini.com/columns/780063",
     "mkini COMMENT | 'Oh, so the state elections are an indicator?' by Zan Azlee (~09:56 MYT 19 Jul, ~44m before scrape). Fresh PIR-07 commentary on whether NS polls are a national indicator."),
    ("PIR-07","awani-polis-lulus-19-permit-ceramah",
     "https://www.astroawani.com/berita-politik/prn-negeri-sembilan-polis-lulus-19-permit-ceramah-kempen",
     "Astro Awani: Police approve 19 ceramah (campaign talk) permits for PRN NS — Day-1 campaign-ops signal (PIR-07). Homepage-extracted headline; fetching full body to confirm date/detail."),
]

def fetch(url, timeout=35):
    cmd = ["curl","-sS","-L","-m",str(timeout),"-A",UA,"--compressed",
           "-H","Accept-Language: en-US,en;q=0.9,ms;q=0.8",
           "-w","\n__HTTPCODE__:%{http_code}\n__FINALURL__:%{url_effective}",
           url]
    p = subprocess.run(cmd, capture_output=True, timeout=timeout+10)
    out = p.stdout
    m = re.search(rb"__HTTPCODE__:(\d+)", out)
    code = m.group(1).decode() if m else "ERR"
    mu = re.search(rb"__FINALURL__:(\S+)", out)
    final = mu.group(1).decode("utf-8","replace") if mu else url
    body = out[:m.start()] if m else out
    return code, body, final

def extract_article(url, body):
    try:
        soup = BeautifulSoup(body.decode("utf-8","replace"), "html.parser")
    except Exception:
        return "","",""
    title = ""
    if soup.title and soup.title.string:
        title = soup.title.string.strip()
    og = soup.find("meta", property="og:title")
    if og and og.get("content"): title = og["content"].strip()
    desc = ""
    md = soup.find("meta", attrs={"name":"description"}) or soup.find("meta", property="og:description")
    if md and md.get("content"): desc = md["content"].strip()
    # pubdate meta
    pub = ""
    for sel in ['meta[property="article:published_time"]','meta[name="pubdate"]','meta[name="date"]','meta[itemprop="datePublished"]','time[datetime]']:
        n = soup.select_one(sel)
        if n and (n.get("content") or n.get("datetime")):
            pub = n.get("content") or n.get("datetime")
            break
    text_parts = []
    selectors = ["div.elementor-widget-theme-post-content",
                 "div.elementor-widget-container div.elementor-element",
                 "article","div.article-content","div.article-body","div.entry-content",
                 "div.post-content","div.content__body","div.field-body","div.story-body",
                 "div#article-body","div.article","main","div.td-post-content",
                 "div.almbe-article-body","div.posts","section.article"]
    for sel in selectors:
        nodes = soup.select(sel)
        for node in nodes:
            for p in node.find_all(["p","li","h2","h3","blockquote"]):
                t = p.get_text(" ", strip=True)
                if t and len(t) > 25:
                    text_parts.append(t)
            if text_parts:
                break
        if text_parts:
            break
    if not text_parts:
        for p in soup.find_all("p"):
            t = p.get_text(" ", strip=True)
            if t and len(t) > 40:
                text_parts.append(t)
    body_text = "\n\n".join(text_parts[:120])
    return title[:300], body_text[:25000], (desc or "")[:600], pub

results = []
for pir, slug, url, note in TARGETS:
    print(f"\n[{pir}] {slug} -> {url[:75]}")
    code, body, final = fetch(url)
    fname = f"priority_{pir.lower()}_{slug}_{TODAY}_{TS_TIME}.md"
    lines = []
    lines.append(f"# [PRIORITY {pir}] {slug}")
    lines.append(f"Source URL: {url}")
    lines.append(f"Final/redirected URL: {final}")
    lines.append(f"Collected: {TODAY} {TS_TIME} UTC ({NOW_ISO}) | MYT: {NOW_MYT}")
    lines.append(f"Classification: TLP:AMBER")
    lines.append(f"HTTP: {code} | note: {note}")
    ok = False
    title = ""; body_text = ""; desc = ""; pub = ""; body_len = 0
    if str(code) == "200":
        title, body_text, desc, pub = extract_article(url, body)
        body_len = len(body_text)
        if body_len > 200:
            ok = True
    lines.append(f"Title: {title}")
    if pub: lines.append(f"ArticlePubDate: {pub}")
    if desc: lines.append(f"Description: {desc}")
    lines.append(f"Body chars: {body_len}")
    lines.append("")
    lines.append("## Full text")
    lines.append("="*78)
    lines.append(body_text if body_text else "(no body extracted)")
    lines.append("="*78)
    with open(os.path.join(BASE, fname),"w",encoding="utf-8") as f:
        f.write("\n".join(lines))
    status = "ok" if ok else "thin/no-body"
    print(f"    HTTP {code} | {status} | body={body_len} | pub={pub} | {fname}")
    results.append({"pir":pir,"slug":slug,"file":fname,"http":code,"ok":ok,
                     "body_len":body_len,"title":title,"final":final,
                     "pub":pub,"mode":"direct","note":note})

with open(os.path.join(BASE, f"_priority_fetch_results_{TS}.json"),"w",encoding="utf-8") as f:
    json.dump(results, f, ensure_ascii=False, indent=2)
print(f"\nWrote _priority_fetch_results_{TS}.json  ({len(results)} targets, {sum(1 for r in results if r['ok'])} ok)")
