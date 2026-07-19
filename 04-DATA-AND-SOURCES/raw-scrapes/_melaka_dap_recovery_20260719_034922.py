#!/usr/bin/env python3
"""Fetch Malay Mail 'Melaka DAP quits state government over nominated assemblymen Bill' (PIR-16 Melaka withdrawal).
Also grab a couple more high-value fresh items if findable on Malay Mail."""
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
              "div.field-body","div.content__body","div.post-content","div.article-text"]
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

# Search Malay Mail for Melaka DAP quits state government article
print("=== Malay Mail search for Melaka DAP quits state govt ===")
# Try the malaysia section + search endpoint
candidates = []
for u in ["https://www.malaymail.com/news/malaysia",
          "https://www.malaymail.com/search?q=melaka+dap+quits+state+government"]:
    code, body, final = curl(u, 30)
    print(f"  {u[:55]} -> HTTP {code} {len(body)} bytes")
    if str(code)!="200": continue
    soup = BeautifulSoup(body.decode("utf-8","replace"),"html.parser")
    for a in soup.find_all("a", href=True):
        href=a["href"]; txt=a.get_text(" ",strip=True)
        if len(txt)<20: continue
        if not href.startswith("http"): href="https://www.malaymail.com"+href
        if "malaymail.com" not in href: continue
        if re.search(r"(melaka|malacca).*(dap).*(quit|withdraw|pullout|exit|resign)", txt, re.I) or \
           re.search(r"dap.*(quits|quit|withdraw).*(melaka|malacca|state)", txt, re.I):
            candidates.append((txt, href))
            print(f"    candidate: {txt[:85]} -> {href[:85]}")

# Dedup
seen=set(); best=None
for txt, href in candidates:
    if href in seen: continue
    seen.add(href)
    if re.search(r"melaka.*dap.*(quit|withdraw|exit)|dap.*(quit|withdraw).*melaka", txt, re.I):
        best=href; break

fname=f"priority_pir-16_malaymail-melaka-dap-quits-state-govt_{TODAY}_{TS_TIME}.md"
lines=[f"# [PRIORITY PIR-16] malaymail-melaka-dap-quits-state-govt",
       f"Collected: {TODAY} {TS} UTC ({NOW_ISO}) | MYT: {NOW_MYT}",
       f"Classification: TLP:AMBER",
       f"PIR-16 relevance: Melaka DAP withdrawal from state govt — major narrative affecting DAP acceptance in NS PRN."]
title=""; body_text=""; desc=""; pub=""; body_len=0; ok=False; resolved_url=best
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
else:
    lines.append("article URL NOT found on Malay Mail; captured as headline intelligence from gnews.")
    lines.append(""); lines.append("## Headline intelligence (from gnews, this cycle)")
    lines.append("="*78)
    headlines = [
        "DAP quits Melaka govt in protest of newly passed bill that allows for unelected assemblymen",
        "Melaka DAP quits state government over nominated assemblymen Bill - Malay Mail",
        "DAP quits Melaka govt after appointed reps bill passed - Free Malaysia Today",
        "Melaka assembly: Four DAP assemblymen moved to opposition but Amanah's Adly still seated with govt",
        "Anwar says not briefed on DAP reps who quit Melaka state govt - KLSE Screener",
        "PM Anwar Yet To Be Briefed On Four Melaka DAP Reps Who Quit State Govt - bernama",
        "Anwar urges Melaka DAP to postpone decision to quit state govt - The Star",
        "Melaka CM: DAP reps' abrupt exit shuts door on negotiations - The Star",
        "DAP reps' pullout in Melaka won't affect Perak unity govt ties, says Saarani - The Star",
    ]
    for h in headlines: lines.append(f"- {h}")
    lines.append("="*78)
with open(os.path.join(BASE,fname),"w",encoding="utf-8") as f:
    f.write("\n".join(lines))
print(f"\nsaved {fname} ok={ok} body={body_len} url={resolved_url}")
print(f"TITLE: {title}")
print(f"PUB: {pub}")
