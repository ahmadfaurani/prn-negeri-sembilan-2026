#!/usr/bin/env python3
"""Fetch full text of key NEW priority articles, save priority_*.md files."""
import subprocess, re, os, datetime
from bs4 import BeautifulSoup

OUTDIR = "/home/p62operator/.openclaw/workspace-ns/04-DATA-AND-SOURCES/raw-scrapes/20260718"
TS = "170837"
NOW = "2026-07-18 17:08 UTC"
UA = ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36")

# (filename_key, pir_tag, title, url, publisher)
ARTICLES = [
    ("pir06_goodbye-pn-muhyiddin-raps-samsuri","PIR-06 CRITICAL-ESCALATION",
     "Goodbye PN?: Muhyiddin raps Samsuri over BN talks, Bersatu to move on",
     "https://www.malaysiakini.com/news/779941","Malaysiakini"),
    ("pir06_bersatu-contest-own-flag","PIR-06",
     "N Sembilan polls: Bersatu to contest under own flag, avoids BN, Harapan strongholds",
     "https://www.malaysiakini.com/news/779996","Malaysiakini"),
    ("pir06_bersatu-exit-pn-imminent-snapshot","PIR-06 CRITICAL-WATCH",
     "SNAPSHOT | Johor regent: Excos must be dedicated in their work; Bersatu exit from PN imminent?",
     "https://www.malaysiakini.com/news/780047","Malaysiakini"),
    ("pir09_mca-youth-stay-out-ns-polls","PIR-09 PIR-07",
     "MCA Youth sec-gen told to 'stay out of N Sembilan polls' over PN ally disagreement",
     "https://www.malaysiakini.com/news/780017","Malaysiakini"),
    ("pir09_pn-camp-albert-barking-dogs","PIR-09",
     "From PN camp, Albert calls Harapan supporters 'barking dogs'",
     "https://www.malaysiakini.com/news/780042","Malaysiakini"),
    ("pir06_bersatu-tidak-lagi-mahu-bersama-pn-ronald","PIR-06",
     "Bersatu tidak lagi mahu bersama PN - Ronald",
     "https://www.utusan.com.my/nasional/2026/07/bersatu-tidak-lagi-mahu-bersama-pn-ronald/","Utusan Malaysia"),
]

def fetch(url, timeout=30):
    try:
        p=subprocess.run(["curl","-sS","-L","-m",str(timeout),"-A",UA,"--compressed",
                         "-H","Accept-Language: en-US,en;q=0.9,ms;q=0.8",
                         "-w","\n__HTTP__:%{http_code}",url],
                        capture_output=True,timeout=timeout+10)
        o=p.stdout; m=re.search(rb"__HTTP__:(\d+)",o)
        code=m.group(1).decode() if m else "ERR"
        body=o[:m.start()] if m else o
        return code, body
    except Exception:
        return "ERR", b""

def extract_mkini(soup):
    # Malaysiakini article body
    for sel in ["div.article-body","div.articleBody","article","div.entry-content","div.post-content"]:
        el=soup.select_one(sel)
        if el and len(el.get_text(strip=True))>200:
            return el.get_text("\n",strip=True)
    # fallback: collect <p>
    ps=[p.get_text(" ",strip=True) for p in soup.find_all("p") if len(p.get_text(strip=True))>40]
    return "\n\n".join(ps)

def extract_utusan(soup):
    for sel in ["article","div.entry-content","div.post-content","div.article-content","div.elementor-widget-theme-post-content"]:
        el=soup.select_one(sel)
        if el and len(el.get_text(strip=True))>200:
            return el.get_text("\n",strip=True)
    ps=[p.get_text(" ",strip=True) for p in soup.find_all("p") if len(p.get_text(strip=True))>40]
    return "\n\n".join(ps)

def extract_generic(soup):
    ps=[p.get_text(" ",strip=True) for p in soup.find_all("p") if len(p.get_text(strip=True))>40]
    return "\n\n".join(ps)

summary=[]
for key,pir,title,url,pub in ARTICLES:
    code,body=fetch(url)
    text=""
    if body:
        soup=BeautifulSoup(body.decode("utf-8","replace"),"html.parser")
        if "malaysiakini" in url: text=extract_mkini(soup)
        elif "utusan" in url: text=extract_utusan(soup)
        else: text=extract_generic(soup)
        if not text or len(text)<150:
            text=extract_generic(soup)
    wc=len(text.split())
    fname=f"priority_{key}_{TS}.md"
    md=[]
    md.append(f"[PRIORITY {pir}] {title}")
    md.append("="*(len(title)+10))
    md.append(f"Source: {pub}")
    md.append(f"URL: {url}")
    md.append(f"Collected: {NOW} | Classification: TLP:AMBER")
    md.append(f"HTTP: {code} | word_count: {wc}")
    md.append("")
    md.append("--- ARTICLE BODY ---")
    md.append(text[:8000] + ("\n...[truncated]..." if len(text)>8000 else ""))
    with open(os.path.join(OUTDIR,fname),"w",encoding="utf-8") as f:
        f.write("\n".join(md))
    summary.append((key,code,wc,title))
    print(f"[{code}] {key}: {wc} words -> {fname}")

print("\n--- SAVED ---")
for k,c,w,t in summary: print(f"  {k:45} HTTP{c} {w:5}w | {t[:60]}")
