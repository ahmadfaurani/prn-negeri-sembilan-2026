#!/usr/bin/env python3
"""Fetch genuinely-new high-value Astro Awani articles for cycle 20260719_064654.
These are PIR-07/16 articles surfacing in gnews but not yet full-text captured.
Awani is curl-friendly (static HTML)."""
import subprocess, re, os, html, datetime

BASE = "/home/p62operator/.openclaw/workspace-ns/04-DATA-AND-SOURCES/raw-scrapes/20260719"
THIS_TS = "20260719_064654"; TODAY = "20260719"; TS_TIME = "064654"
NOW_ISO = datetime.datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S UTC")
NOW_MYT = (datetime.datetime.utcnow()+datetime.timedelta(hours=8)).strftime("%H:%M MYT %d %b %Y")
UA = ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36")

def curl(url, timeout=35):
    cmd = ["curl","-sS","-L","-m",str(timeout),"-A",UA,"--compressed",
           "-H","Accept-Language: en-US,en;q=0.9,ms;q=0.8",
           "-w","\n__HTTPCODE__:%{http_code}\n__FINALURL__:%{url_effective}", url]
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

def extract_article(body):
    try:
        from bs4 import BeautifulSoup
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
    selectors = ["div.detail-article","div.article-body","div.entry-content","div.post-content",
                 "article","div.content__body","div.story-body","div#article-body","div.article",
                 "main","div.news-detail","div.kcontent","div.body-content","div#content"]
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

TARGETS = [
    ("PIR-07","awani-dua-sepupu-klawang",
     "https://www.astroawani.com/berita-politik/prn-negeri-sembilan-dua-sepupu-bertembung-raih-sokongan-pengundi-di-pasar-minggu-kuala-klawang",
     "Awani: Two cousins face off at Pasar Minggu Kuala Klawang — PH incumbent Bakri Sawir vs PN's Danni Rais. N.28 Klawang = T1 seat. FRESH 19 Jul (Day-1 campaign, Jelebu)."),
    ("PIR-16+PIR-07","awani-pengundi-kempen-matang",
     "https://www.astroawani.com/berita-politik/prn-negeri-sembilan-pengundi-mahu-kempen-matang-calon-fokus-kehendak-rakyat",
     "Awani: Voters want mature campaign, candidates focus on people's needs. PIR-16 narrative (mature campaign framing). FRESH 19 Jul."),
    ("PIR-06+PIR-07","awani-teka-teki-11-kerusi-bn-pn-cal",
     "https://www.astroawani.com/berita-politik/prn-negeri-sembilan-teka-teki-11-kerusi-bn-terjawab-pn-umum-baki-calon",
     "Awani: Mystery of 11 BN seats answered, PN announces remaining candidates. PIR-06/07 coalition configuration. FRESH 19 Jul. (constructed URL — may 404 if slug differs)."),
]

for pir, slug, url, note in TARGETS:
    print(f"fetch -> {url}")
    code, body, final = curl(url, timeout=30)
    title, body_text, desc, pub = ("","","","")
    body_len = 0; ok = False
    if str(code) == "200":
        title, body_text, desc, pub = extract_article(body)
        body_len = len(body_text)
        if body_len > 150: ok = True
    fname = f"priority_{pir.lower().replace('+','-')}_{slug}_{TODAY}_{TS_TIME}.md"
    lines = [f"# [PRIORITY {pir}] {slug}", f"Source URL: {url}", f"Final/redirected URL: {final}",
             f"Collected: {TODAY} {THIS_TS} UTC ({NOW_ISO}) | MYT: {NOW_MYT}",
             f"Classification: TLP:AMBER", f"HTTP: {code} | mode: awani-direct",
             f"Note: {note}", f"Title: {title}"]
    if pub: lines.append(f"ArticlePubDate: {pub}")
    if desc: lines.append(f"Description: {desc}")
    lines += [f"Body chars: {body_len}", "", "## Full text", "="*78,
              (body_text if body_text else "(no body extracted)"), "="*78]
    with open(os.path.join(BASE, fname),"w",encoding="utf-8") as f:
        f.write("\n".join(lines))
    print(f"  [{pir}] {slug} | HTTP {code} | {'ok' if ok else 'thin/no-body'} | body={body_len} | pub={pub} | {fname}")
print("DONE.")
