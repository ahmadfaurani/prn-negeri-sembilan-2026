#!/usr/bin/env python3
"""Retry The Star Melaka DAP article via thestar.com.my search endpoint."""
import subprocess, re, datetime, json, os
from bs4 import BeautifulSoup
import warnings
try:
    from bs4 import XMLParsedAsHTMLWarning
    warnings.filterwarnings("ignore", category=XMLParsedAsHTMLWarning)
except Exception:
    pass

BASE = "/home/p62operator/.openclaw/workspace-ns/04-DATA-AND-SOURCES/raw-scrapes/20260719"
TS = "20260719_034922"; TODAY="20260719"; TS_TIME="034922"
NOW_MYT = (datetime.datetime.utcnow()+datetime.timedelta(hours=8)).strftime("%H:%M MYT %d %b %Y")
NOW_ISO = datetime.datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S UTC")
UA = ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36")

def curl(url, timeout=30):
    cmd=["curl","-sS","-L","-m",str(timeout),"-A",UA,"--compressed",
         "-H","Accept-Language: en-US,en;q=0.9,ms;q=0.8",
         "-w","\n__HTTPCODE__:%{http_code}\n__FINALURL__:%{url_effective}", url]
    p=subprocess.run(cmd, capture_output=True, timeout=timeout+10)
    out=p.stdout
    m=re.search(rb"__HTTPCODE__:(\d+)", out)
    code=m.group(1).decode() if m else "ERR"
    mu=re.search(rb"__FINALURL__:(\S+)", out)
    final=mu.group(1).decode("utf-8","replace") if mu else url
    body=out[:m.start()] if m else out
    return code, body, final

def extract_article(url, body):
    try:
        soup=BeautifulSoup(body.decode("utf-8","replace"),"html.parser")
    except Exception:
        return "","","",""
    title = soup.title.string.strip() if soup.title and soup.title.string else ""
    og=soup.find("meta",property="og:title")
    if og and og.get("content"): title=og["content"].strip()
    desc=""
    md=soup.find("meta",attrs={"name":"description"}) or soup.find("meta",property="og:description")
    if md and md.get("content"): desc=md["content"].strip()
    pub=""
    for sel in ['meta[property="article:published_time"]','meta[name="pubdate"]','meta[name="date"]','meta[itemprop="datePublished"]','time[datetime]']:
        n=soup.select_one(sel)
        if n and (n.get("content") or n.get("datetime")):
            pub=n.get("content") or n.get("datetime"); break
    text_parts=[]
    selectors=["article","div.article-content","div.article-body","div.entry-content","div.story-body",
              "div#article-body","main","div.td-post-content","div.elementor-widget-theme-post-content",
              "div.elementor-widget-container","div.body-content","div.news-detail","div.single-content",
              "div.field-body","div.content__body","div.post-content","div.article-text","div.story"]
    for sel in selectors:
        for node in soup.select(sel):
            for p in node.find_all(["p","li","h2","h3","blockquote"]):
                t=p.get_text(" ",strip=True)
                if t and len(t)>25: text_parts.append(t)
            if text_parts: break
        if text_parts: break
    if not text_parts:
        for p in soup.find_all("p"):
            t=p.get_text(" ",strip=True)
            if t and len(t)>40: text_parts.append(t)
    return title[:300], "\n\n".join(text_parts[:140])[:28000], (desc or "")[:800], pub

# Try The Star search API / search page
SEARCH_URLS = [
    "https://www.thestar.com.my/search?searchtext=Anwar+melaka+DAP+postpone&q=Anwar+melaka+DAP",
    "https://www.thestar.com.my/search?searchtext=melaka+DAP+quit+state+govt",
]
print("=== The Star search attempts ===")
found_urls = []
for surl in SEARCH_URLS:
    code, body, final = curl(surl, 30)
    print(f"  {surl[:70]} -> HTTP {code}, {len(body)} bytes")
    if str(code)!="200": continue
    soup = BeautifulSoup(body.decode("utf-8","replace"),"html.parser")
    for a in soup.find_all("a", href=True):
        href=a["href"]
        txt=a.get_text(" ",strip=True)
        if (re.search(r"(melaka|dap).*(postpone|quit|withdraw)", txt, re.I) or
            re.search(r"(postpone|quit).*(melaka|dap)", txt, re.I)) and "thestar.com.my" in href:
            found_urls.append((txt, href))
            print(f"    candidate: {txt[:80]} -> {href[:80]}")

# Also try fetching The Star's nation news listing for Anwar/Melaka
print("\n=== The Star news/nation listing for melaka/anwar ===")
code, body, final = curl("https://www.thestar.com.my/news/nation", 30)
soup = BeautifulSoup(body.decode("utf-8","replace"),"html.parser")
for a in soup.find_all("a", href=True):
    href=a["href"]; txt=a.get_text(" ",strip=True)
    if re.search(r"(melaka|anwar).*(dap|postpone|quit|govt)", txt, re.I) and len(txt)>20:
        if href not in [u for _,u in found_urls]:
            found_urls.append((txt, href))
        print(f"    candidate: {txt[:80]} -> {href[:80]}")

# Dedup and try fetching the best candidate
seen=set(); best=None
for txt, href in found_urls:
    if href in seen: continue
    seen.add(href)
    if re.search(r"melaka", txt, re.I) and re.search(r"(dap|postpone|quit)", txt, re.I):
        if not href.startswith("http"): href="https://www.thestar.com.my"+href
        best=href; break

fname=f"priority_pir-16_star-anwar-melaka-dap-postpone_{TODAY}_{TS_TIME}.md"
lines=[f"# [PRIORITY PIR-16] star-anwar-melaka-dap-postpone (recovery)",
       f"Collected: {TODAY} {TS} UTC ({NOW_ISO}) | MYT: {NOW_MYT}",
       f"Classification: TLP:AMBER"]
title=""; body_text=""; desc=""; pub=""; body_len=0; ok=False
if best:
    lines.append(f"Resolved URL: {best}")
    c2,b2,f2 = curl(best, 30)
    if str(c2)=="200":
        title, body_text, desc, pub = extract_article(best, b2)
        body_len=len(body_text); ok=body_len>150
    lines.append(f"HTTP: {c2} | Title: {title}")
    if pub: lines.append(f"ArticlePubDate: {pub}")
    if desc: lines.append(f"Description: {desc}")
    lines.append(f"Body chars: {body_len}")
    lines.append(""); lines.append("## Full text"); lines.append("="*78)
    lines.append(body_text if body_text else "(no body extracted)")
    lines.append("="*78)
    print(f"\nFETCHED: {best} ok={ok} body={body_len} title={title}")
else:
    lines.append("article URL NOT found on The Star search/listing")
    lines.append(""); lines.append("## Search candidates found"); lines.append("="*78)
    for txt,href in found_urls[:15]:
        lines.append(f"- {txt[:100]} -> {href}")
    lines.append("="*78)
    print("\nNo matching article URL found on The Star.")

with open(os.path.join(BASE,fname),"w",encoding="utf-8") as f:
    f.write("\n".join(lines))
print(f"saved {fname}")
