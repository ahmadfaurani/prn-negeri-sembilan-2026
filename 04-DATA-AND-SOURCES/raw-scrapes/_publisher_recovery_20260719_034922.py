#!/usr/bin/env python3
"""Fetch publisher homepages directly, find real article URLs, then fetch full text.
Targets Malay Mail + The Star high-value headlines whose gnews links are JS-rendered.
"""
import subprocess, re, datetime, json, os
from bs4 import BeautifulSoup
import warnings
try:
    from bs4 import XMLParsedAsHTMLWarning
    warnings.filterwarnings("ignore", category=XMLParsedAsHTMLWarning)
except Exception:
    pass

BASE = "/home/p62operator/.openclaw/workspace-ns/04-DATA-AND-SOURCES/raw-scrapes/20260719"
TS = "20260719_034922"
TODAY = "20260719"
TS_TIME = "034922"
NOW_MYT = (datetime.datetime.utcnow()+datetime.timedelta(hours=8)).strftime("%H:%M MYT %d %b %Y")
NOW_ISO = datetime.datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S UTC")
UA = ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36")

# (pir, slug, publisher_homepage, headline_keywords_for_matching)
TARGETS = [
    ("PIR-16","star-anwar-melaka-dap-postpone","https://www.thestar.com.my/news/nation",
     ["anwar","melaka","dap","postpone"]),
    ("PIR-07","malaymail-ns-race-begins-nomination-day","https://www.malaymail.com/news/malaysia",
     ["negeri","sembilan","race","begins","nomination"]),
    ("PIR-07","malaymail-fahmi-tokmin-track-record","https://www.malaymail.com/news/malaysia",
     ["fahmi","tok","min","track","record","negeri"]),
]

def curl(url, timeout=30):
    cmd = ["curl","-sS","-L","-m",str(timeout),"-A",UA,"--compressed",
           "-H","Accept-Language: en-US,en;q=0.9,ms;q=0.8",
           "-w","\n__HTTPCODE__:%{http_code}\n__FINALURL__:%{url_effective}", url]
    p = subprocess.run(cmd, capture_output=True, timeout=timeout+10)
    out = p.stdout
    m = re.search(rb"__HTTPCODE__:(\d+)", out)
    code = m.group(1).decode() if m else "ERR"
    mu = re.search(rb"__FINALURL__:(\S+)", out)
    final = mu.group(1).decode("utf-8","replace") if mu else url
    body = out[:m.start()] if m else out
    return code, body, final

def find_article_url(homepage_url, keywords):
    """Fetch homepage, find <a href> whose anchor text matches >=60% of keywords."""
    code, body, final = curl(homepage_url, 30)
    if code != "200":
        return None, code
    soup = BeautifulSoup(body.decode("utf-8","replace"), "html.parser")
    candidates = []
    for a in soup.find_all("a", href=True):
        txt = a.get_text(" ", strip=True)
        if len(txt) < 15: continue
        href = a["href"]
        if not href.startswith("http"): continue
        lc = txt.lower()
        hits = sum(1 for k in keywords if k in lc)
        if hits >= max(3, len(keywords)*0.5):
            candidates.append((hits, txt, href))
    candidates.sort(key=lambda x:-x[0])
    for hits, txt, href in candidates[:3]:
        print(f"    candidate hits={hits}: {txt[:80]} -> {href[:80]}")
    return (candidates[0][2] if candidates else None), code

def extract_article(url, body):
    try:
        soup = BeautifulSoup(body.decode("utf-8","replace"), "html.parser")
    except Exception:
        return "","","",""
    title = soup.title.string.strip() if soup.title and soup.title.string else ""
    og = soup.find("meta", property="og:title")
    if og and og.get("content"): title = og["content"].strip()
    desc = ""
    md = soup.find("meta", attrs={"name":"description"}) or soup.find("meta", property="og:description")
    if md and md.get("content"): desc = md["content"].strip()
    pub = ""
    for sel in ['meta[property="article:published_time"]','meta[name="pubdate"]','meta[name="date"]','meta[itemprop="datePublished"]','time[datetime]']:
        n = soup.select_one(sel)
        if n and (n.get("content") or n.get("datetime")):
            pub = n.get("content") or n.get("datetime"); break
    text_parts = []
    selectors = ["article","div.article-content","div.article-body","div.entry-content","div.story-body",
                 "div#article-body","main","div.td-post-content","div.elementor-widget-theme-post-content",
                 "div.elementor-widget-container","div.body-content","div.news-detail","div.single-content",
                 "div.field-body","div.content__body","div.post-content","div.article-text"]
    for sel in selectors:
        for node in soup.select(sel):
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
for pir, slug, homepage, keywords in TARGETS:
    print(f"\n[{pir}] {slug} -> {homepage}")
    real_url, code = find_article_url(homepage, keywords)
    fname = f"priority_{pir.lower()}_{slug}_{TODAY}_{TS_TIME}.md"
    lines = [f"# [PRIORITY {pir}] {slug}", f"Publisher homepage: {homepage}",
             f"Collected: {TODAY} {TS} UTC ({NOW_ISO}) | MYT: {NOW_MYT}",
             f"Classification: TLP:AMBER"]
    title=""; body_text=""; desc=""; pub=""; body_len=0; ok=False
    if real_url:
        lines.append(f"Resolved article URL: {real_url}")
        c2, b2, f2 = curl(real_url, 30)
        if str(c2)=="200":
            title, body_text, desc, pub = extract_article(real_url, b2)
            body_len = len(body_text)
            ok = body_len > 150
        lines.append(f"HTTP: {c2} | Title: {title}")
        if pub: lines.append(f"ArticlePubDate: {pub}")
        if desc: lines.append(f"Description: {desc}")
        lines.append(f"Body chars: {body_len}")
        lines.append("")
        lines.append("## Full text")
        lines.append("="*78)
        lines.append(body_text if body_text else "(no body extracted)")
        lines.append("="*78)
    else:
        lines.append(f"article URL NOT found on homepage (HTTP {code})")
    with open(os.path.join(BASE, fname),"w",encoding="utf-8") as f:
        f.write("\n".join(lines))
    print(f"    saved {fname} ok={ok} body={body_len} url={real_url}")
    results.append({"pir":pir,"slug":slug,"file":fname,"resolved":bool(real_url),"ok":ok,
                    "body_len":body_len,"title":title,"pub":pub,"url":real_url})

with open(os.path.join(BASE, f"_publisher_recovery_{TS}.json"),"w",encoding="utf-8") as f:
    json.dump(results, f, ensure_ascii=False, indent=2)
print(f"\n=== publisher recovery done ({len(results)} targets) ===")
