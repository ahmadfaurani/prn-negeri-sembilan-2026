#!/usr/bin/env python3
"""Resolve real article URLs via site-restricted Google News RSS, then fetch full text."""
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

# (pir, slug, publisher_domain, site_query) — use site: search to get the real article URL
TARGETS = [
    ("PIR-16","star-anwar-melaka-dap-postpone","thestar.com.my",
     "Anwar urges Melaka DAP to postpone decision to quit state govt"),
    ("PIR-07","malaymail-ns-race-begins-nomination-day","malaymail.com",
     "Negeri Sembilan race begins as nomination day kicks off"),
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

def gnews_site_search(domain, query):
    """site:restricted gnews RSS — return list of (title, link, pubdate, source_url)."""
    q = f"site:{domain} " + query
    q_enc = q.replace(" ","+")
    url = f"https://news.google.com/rss/search?q={q_enc}&hl=en-MY&gl=MY&ceid=MY:en"
    code, body, final = curl(url, 25)
    if code != "200": return []
    soup = BeautifulSoup(body.decode("utf-8","replace"), "html.parser")
    out = []
    for item in soup.find_all("item"):
        title = item.title.get_text().strip() if item.title else ""
        link = ""
        for L in item.find_all("link"):
            link = L.get_text() or L.string or ""
            if link: break
        pub = item.pubDate.get_text().strip() if item.pubDate else ""
        src = ""
        se = item.find("source")
        if se and se.get("url"): src = se.get("url")
        out.append({"title":title,"link":link,"pubdate":pub,"source_url":src})
    return out

def resolve_gnews_to_real(glink):
    """Follow gnews link; if it redirects to a real publisher URL, return it."""
    code, body, final = curl(glink, 20)
    if final and "news.google.com" not in final:
        return final, code, body
    # Try extracting canonical link from the JS page
    m = re.search(rb'(?:canonical|og:url)["\'\s=]+(https?://[^"\'<\s]+)', body, re.I)
    if m:
        u = m.group(1).decode("utf-8","replace")
        if domain in u:
            return u, code, body
    return None, code, body

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
                 "div.field-body","div.content__body","div.post-content"]
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
for pir, slug, domain, headline in TARGETS:
    print(f"\n[{pir}] site-search {domain}: {headline[:55]}")
    items = gnews_site_search(domain, headline)
    print(f"    {len(items)} site-restricted items")
    real_url = None; best = None
    for it in items[:6]:
        sim = sum(1 for w in headline.lower().split() if w in it["title"].lower())
        print(f"    sim={sim} | {it['title'][:90]} | pub={it['pubdate']}")
        if sim >= max(5, len(headline.split())*0.6) and (best is None or sim > best[0]):
            best = (sim, it)
    if best:
        # try to follow the gnews link to get real URL
        glink = best[1]["link"]
        ru, code, body = resolve_gnews_to_real(glink)
        if ru:
            real_url = ru
            print(f"    RESOLVED -> {real_url}")
    if not real_url and best:
        # last resort: try fetching publisher homepage and grep for article slug words
        pass
    fname = f"priority_{pir.lower()}_{slug}_{TODAY}_{TS_TIME}.md"
    lines = []
    lines.append(f"# [PRIORITY {pir}] {slug}")
    lines.append(f"Original headline: {headline}")
    lines.append(f"Publisher: {domain}")
    lines.append(f"Collected: {TODAY} {TS} UTC ({NOW_ISO}) | MYT: {NOW_MYT}")
    lines.append(f"Classification: TLP:AMBER")
    title=""; body_text=""; desc=""; pub=""; body_len=0
    if real_url:
        lines.append(f"Resolved URL: {real_url}")
        code, body, final = curl(real_url, 30)
        if str(code)=="200":
            title, body_text, desc, pub = extract_article(real_url, body)
            body_len = len(body_text)
        lines.append(f"HTTP: {code} | Title: {title}")
        if pub: lines.append(f"ArticlePubDate: {pub}")
        if desc: lines.append(f"Description: {desc}")
        lines.append(f"Body chars: {body_len}")
        lines.append("")
        lines.append("## Full text")
        lines.append("="*78)
        lines.append(body_text if body_text else "(no body extracted)")
        lines.append("="*78)
    else:
        lines.append(f"resolution FAILED; gnews items below as headline intelligence")
        lines.append("")
        lines.append("## gnews site-restricted RSS items")
        lines.append("="*78)
        for it in items[:10]:
            lines.append(f"- [{it['pubdate']}] {it['title']}")
            lines.append(f"  gnews: {it['link']}")
        lines.append("="*78)
    with open(os.path.join(BASE, fname),"w",encoding="utf-8") as f:
        f.write("\n".join(lines))
    ok = body_len > 150
    print(f"    saved {fname} ok={ok} body={body_len}")
    results.append({"pir":pir,"slug":slug,"file":fname,"resolved":bool(real_url),"ok":ok,"body_len":body_len,"title":title,"pub":pub})

with open(os.path.join(BASE, f"_gnews_recovery_v2_{TS}.json"),"w",encoding="utf-8") as f:
    json.dump(results, f, ensure_ascii=False, indent=2)
print(f"\n=== gnews recovery v2 done ({len(results)} queries) ===")
