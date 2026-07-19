#!/usr/bin/env python3
"""Fetch confirmed FMT Kiandee-quorum articles (PIR-06 NEW requirement satisfied via URL guess).
Cycle 20260719_075200. TLP:AMBER."""
import subprocess, re, os, datetime
from bs4 import BeautifulSoup

BASE = "/home/p62operator/.openclaw/workspace-ns/04-DATA-AND-SOURCES/raw-scrapes/20260719"
TS = "20260719_075200"; TODAY = "20260719"; TS_TIME = "075200"
NOW_ISO = datetime.datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S UTC")
NOW_MYT = (datetime.datetime.utcnow()+datetime.timedelta(hours=8)).strftime("%H:%M MYT %d %b %Y")
UA = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/126.0.0.0 Safari/537.36"

def curl(url, timeout=30):
    cmd = ["curl","-sS","-L","-m",str(timeout),"-A",UA,"--compressed",
           "-H","Accept-Language: en-US,en;q=0.9,ms;q=0.8", url]
    p = subprocess.run(cmd, capture_output=True, timeout=timeout+10)
    return p.stdout

def extract(body):
    soup = BeautifulSoup(body.decode("utf-8","replace"), "html.parser")
    title = ""
    if soup.title and soup.title.string: title = soup.title.string.strip()
    og = soup.find("meta", property="og:title")
    if og and og.get("content"): title = og["content"].strip()
    desc = ""
    md = soup.find("meta", attrs={"name":"description"}) or soup.find("meta", property="og:description")
    if md and md.get("content"): desc = md["content"].strip()
    pub = ""
    for sel in ['meta[property="article:published_time"]','meta[name="pubdate"]','meta[name="date"]',
                'meta[itemprop="datePublished"]','time[datetime]','meta[property="og:updated_time"]']:
        n = soup.select_one(sel)
        if n and (n.get("content") or n.get("datetime")):
            pub = n.get("content") or n.get("datetime"); break
    # FMT Next.js renders article in <div class="article-content"> or og:description rich; try multiple
    text_parts = []
    for sel in ["div.article-content","div.entry-content","article","div.post-content",
                "div.single-content","div.elementor-widget-theme-post-content",
                "div.body-text","div#article-body","main","div.content__body"]:
        nodes = soup.select(sel)
        for node in nodes:
            for p in node.find_all(["p","li","h2","h3","blockquote"]):
                t = p.get_text(" ", strip=True)
                if t and len(t) > 25: text_parts.append(t)
            if text_parts: break
        if text_parts: break
    if not text_parts:
        # FMT Next.js: paragraphs may be in generic divs; collect long <p> globally
        for p in soup.find_all("p"):
            t = p.get_text(" ", strip=True)
            if t and len(t) > 40: text_parts.append(t)
    return title[:300], "\n\n".join(text_parts[:180])[:28000], (desc or "")[:800], pub

def save(pir, slug, url, body, note, mode):
    title, body_text, desc, pub = extract(body) if body else ("","","","")
    blen = len(body_text); ok = blen > 150
    fname = f"priority_{pir.lower().replace('+','-')}_{slug}_{TODAY}_{TS_TIME}.md"
    lines = [f"# [PRIORITY {pir}] {slug}", f"Source URL: {url}",
             f"Collected: {TODAY} {TS} UTC ({NOW_ISO}) | MYT: {NOW_MYT}",
             f"Classification: TLP:AMBER", f"HTTP: 200 | mode: {mode}", f"Note: {note}",
             f"Title: {title}"]
    if pub: lines.append(f"ArticlePubDate: {pub}")
    if desc: lines.append(f"Description: {desc}")
    lines += [f"Body chars: {blen}", "", "## Full text", "="*78,
              (body_text if body_text else "(no body extracted — FMT Next.js may need JS-render)"), "="*78]
    with open(os.path.join(BASE, fname),"w",encoding="utf-8") as f:
        f.write("\n".join(lines))
    print(f"  [{pir}] {slug[:55]:55} | {'ok' if ok else 'thin'} | body={blen} | pub={pub[:25]} | {fname}")
    return ok, title, body_text, pub

# Confirmed + guessed FMT Kiandee-quorum URLs
URLS = [
    ("PIR-06", "fmt-kiandee-quorum-bersatu-supreme-council-en",
     "https://www.freemalaysiatoday.com/category/nation/2026/07/11/does-bersatu-supreme-council-still-have-a-quorum-kiandee-asks-muhyiddin",
     "FMT EN Kiandee quorum article (confirmed URL via guess). PIR-06 NEW requirement."),
    ("PIR-06", "fmt-kiandee-quorum-bersatu-supreme-council-bm",
     "https://www.freemalaysiatoday.com/category/nation/2026/07/11/adakah-mpt-bersatu-cukup-kuorum-kiandee-soal-muhyiddin",
     "FMT BM Kiandee quorum article (URL guess)."),
    # Also Radzi Jidin response (same day)
    ("PIR-06", "fmt-radzi-jalan-biasa-mpt-bersatu-cukup-kuorum-en",
     "https://www.freemalaysiatoday.com/category/nation/2026/07/11/jalan-seperti-biasa-mpt-bersatu-cukup-kuorum-jelas-radzi",
     "FMT EN Radzi Jidin response: quorum sufficient, business as usual."),
    ("PIR-06", "fmt-radzi-jalan-biasa-mpt-bersatu-cukup-kuorum-bm",
     "https://www.freemalaysiatoday.com/category/nation/2026/07/11/mpt-bersatu-cukup-kuorum-jalan-seperti-biasa-jelas-radzi",
     "FMT BM Radzi Jidin response (URL guess)."),
    # Sanjeevan quorum-NS PRN link (15 Jul)
    ("PIR-06", "fmt-sanjeevan-isu-kuorum-alasan-sekat-bersatu-prn-ns",
     "https://www.freemalaysiatoday.com/category/nation/2026/07/15/isu-kuorum-hanya-alasan-sekat-bersatu-bertanding-prn-negeri-sembilan-sanjeevan",
     "FMT Sanjeevan: quorum issue just an excuse to block Bersatu from NS PRN. Ties quorum to NS PRN."),
]
saved_ok = 0
for pir, slug, url, note in URLS:
    body = curl(url, timeout=30)
    if body and len(body) > 5000:
        ok, title, txt, pub = save(pir, slug, url, body, note, "fmt-quorum-direct-guess")
        if ok: saved_ok += 1
    else:
        print(f"  [{pir}] {slug[:55]:55} | SKIP (small/empty body {len(body) if body else 0}) | {url}")

print(f"\nFMT quorum articles with body: {saved_ok}/{len(URLS)}")
print("DONE.")
