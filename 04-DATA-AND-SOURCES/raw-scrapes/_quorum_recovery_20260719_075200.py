#!/usr/bin/env python3
"""Focused recovery: FMT Kiandee-quorum full text (PIR-06 NEW req) + current Sinar/bernama items.
Cycle 20260719_075200. TLP:AMBER."""
import subprocess, re, html, os, datetime
from bs4 import BeautifulSoup

BASE = "/home/p62operator/.openclaw/workspace-ns/04-DATA-AND-SOURCES/raw-scrapes/20260719"
TS = "20260719_075200"; TODAY = "20260719"; TS_TIME = "075200"
NOW_ISO = datetime.datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S UTC")
NOW_MYT = (datetime.datetime.utcnow()+datetime.timedelta(hours=8)).strftime("%H:%M MYT %d %b %Y")
UA = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/126.0.0.0 Safari/537.36"

def curl(url, timeout=30):
    cmd = ["curl","-sS","-L","-m",str(timeout),"-A",UA,"--compressed",
           "-H","Accept-Language: en-US,en;q=0.9,ms;q=0.8", url]
    try:
        p = subprocess.run(cmd, capture_output=True, timeout=timeout+10)
        return "200", p.stdout
    except Exception as e:
        return "ERR", str(e).encode()

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
                'meta[itemprop="datePublished"]','time[datetime]']:
        n = soup.select_one(sel)
        if n and (n.get("content") or n.get("datetime")):
            pub = n.get("content") or n.get("datetime"); break
    text_parts = []
    for sel in ["div.elementor-widget-theme-post-content","div.article-content","div.entry-content",
                "article","div.post-content","div.single-content","div.news-detail","div.body-text",
                "div#article-body","main","div.content__body","div.kandungan","div.story-body",
                "div.elementor-widget-container"]:
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
    return title[:300], "\n\n".join(text_parts[:160])[:28000], (desc or "")[:800], pub

def save(pir, slug, url, body_bytes, note, mode):
    title, body_text, desc, pub = extract(body_bytes) if body_bytes else ("","","","")
    blen = len(body_text); ok = blen > 150
    fname = f"priority_{pir.lower().replace('+','-')}_{slug}_{TODAY}_{TS_TIME}.md"
    lines = [f"# [PRIORITY {pir}] {slug}", f"Source URL: {url}",
             f"Collected: {TODAY} {TS} UTC ({NOW_ISO}) | MYT: {NOW_MYT}",
             f"Classification: TLP:AMBER", f"HTTP: 200 | mode: {mode}", f"Note: {note}",
             f"Title: {title}"]
    if pub: lines.append(f"ArticlePubDate: {pub}")
    if desc: lines.append(f"Description: {desc}")
    lines += [f"Body chars: {blen}", "", "## Full text", "="*78,
              (body_text if body_text else "(no body extracted)"), "="*78]
    with open(os.path.join(BASE, fname),"w",encoding="utf-8") as f:
        f.write("\n".join(lines))
    print(f"  [{pir}] {slug[:55]:55} | {'ok' if ok else 'thin'} | body={blen} | {fname}")
    return ok

# 1. FMT search for kiandee quorum articles
print("=== FMT search: kiandee quorum ===")
code, body = curl("https://www.freemalaysiatoday.com/?s=kiandee+quorum+bersatu", timeout=30)
fmt_links = set()
if str(code) == "200":
    for m in re.finditer(r'href="(https://www\.freemalaysiatoday\.com/category/[^"]+)"', body.decode("utf-8","replace")):
        u = m.group(1)
        if re.search(r"(quorum|kiandee|bersatu)", u, re.I):
            fmt_links.add(u)
print(f"FMT search candidate links: {len(fmt_links)}")
for u in sorted(fmt_links)[:10]:
    print(f"  {u}")
for u in sorted(fmt_links)[:6]:
    code, body = curl(u, timeout=30)
    slug = re.sub(r"[^a-z0-9]+","-",u.lower()).strip("-")[-80:]
    save("PIR-06", slug, u, body, "FMT Kiandee-quorum full-text recovery via FMT search", "fmt-quorum-recovery")

# 2. FMT search: bersatu exit pn (for current PIR-16 corroboration)
print("\n=== FMT search: bersatu keluar PN ===")
code, body = curl("https://www.freemalaysiatoday.com/?s=bersatu+keluar+PN", timeout=30)
fmt_links2 = set()
if str(code) == "200":
    for m in re.finditer(r'href="(https://www\.freemalaysiatoday\.com/category/[^"]+)"', body.decode("utf-8","replace")):
        u = m.group(1)
        if re.search(r"(bersatu|keluar|exit|pn|perikatan|reput|pecat)", u, re.I):
            fmt_links2.add(u)
print(f"FMT search 'bersatu keluar PN' candidate links: {len(fmt_links2)}")
for u in sorted(fmt_links2)[:8]:
    print(f"  {u}")
for u in sorted(fmt_links2)[:5]:
    code, body = curl(u, timeout=30)
    slug = re.sub(r"[^a-z0-9]+","-",u.lower()).strip("-")[-80:]
    save("PIR-06", slug, u, body, "FMT bersatu-exit full-text recovery via FMT search", "fmt-exit-recovery")

# 3. Sinar Harian: Muhyiddin Bersatu utamakan kebajikan (19 Jul) - try Sinar search
print("\n=== Sinar Harian search: PRN Negeri Sembilan Muhyiddin ===")
code, body = curl("https://www.sinarharian.com.my/search?q=PRN+Negeri+Sembilan+Muhyiddin", timeout=30)
sinar_links = set()
if str(code) == "200":
    txt = body.decode("utf-8","replace")
    for m in re.finditer(r'href="(/[^"]*PRN[^"]*)"', txt, re.I):
        sinar_links.add("https://www.sinarharian.com.my" + m.group(1))
    for m in re.finditer(r'href="(https://www\.sinarharian\.com\.my/[^"]+)"', txt):
        if re.search(r"(prn|negeri|bersatu|muhyiddin|hadi|loke)", m.group(1), re.I):
            sinar_links.add(m.group(1))
print(f"Sinar candidate links: {len(sinar_links)}")
for u in sorted(sinar_links)[:5]:
    print(f"  {u}")

# 4. bernama search PRN Negeri Sembilan (curl-friendly static)
print("\n=== bernama search: PRN Negeri Sembilan ===")
code, body = curl("https://www.bernama.com/bm/am/index.php?tag=PRN+Negeri+Sembilan", timeout=30)
bernama_links = set()
if str(code) == "200":
    txt = body.decode("utf-8","replace")
    for m in re.finditer(r'news\.php\?id=(\d+)', txt):
        bernama_links.add("https://www.bernama.com/bm/am/news.php?id=" + m.group(1))
print(f"bernama candidate links: {len(bernama_links)}")
for u in sorted(bernama_links)[:8]:
    print(f"  {u}")
for u in sorted(bernama_links)[:5]:
    code, body = curl(u, timeout=30)
    slug = re.sub(r"[^a-z0-9]+","-",u.lower()).strip("-")[-80:]
    save("PIR-07", slug, u, body, "bernama PRN NS recovery", "bernama-recovery")

print("\nDONE.")
