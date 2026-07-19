#!/usr/bin/env python3
"""Recover real publisher URLs for 2 high-value gnews-only headlines:
  - 'Anwar urges Melaka DAP to postpone decision to quit state govt' (PIR-16 Melaka)
  - 'Negeri Sembilan race begins as nomination day kicks off' (PIR-07, Newswav)
Approach: Google News RSS search by exact headline -> extract publisher URLs from RSS items.
Then fetch the resolved real URL for full text.
"""
import subprocess, re, datetime, json, os
from bs4 import BeautifulSoup

BASE = "/home/p62operator/.openclaw/workspace-ns/04-DATA-AND-SOURCES/raw-scrapes/20260719"
TS = "20260719_034922"
TODAY = "20260719"
TS_TIME = "034922"
NOW_MYT = (datetime.datetime.utcnow()+datetime.timedelta(hours=8)).strftime("%H:%M MYT %d %b %Y")
NOW_ISO = datetime.datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S UTC")
UA = ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36")

QUERIES = [
    ("PIR-16","star-anwar-melaka-dap-postpone", "Anwar urges Melaka DAP to postpone decision to quit state govt",
     "PIR-16 Melaka-withdrawal narrative. Anwar (PM) urges Melaka DAP to postpone quit-state-govt decision."),
    ("PIR-07","newswav-ns-race-begins-nomination-day", "Negeri Sembilan race begins as nomination day kicks off",
     "PIR-07 Day-1 nomination narrative (Newswav aggregator)."),
]

def curl(url, timeout=30):
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

def gnews_rss_search(query):
    """Return list of (title, link, pubdate, source_url) from gnews RSS for a query."""
    q = re.sub(r"\s+", "+", query)
    url = f"https://news.google.com/rss/search?q=%22{q}%22&hl=en-MY&gl=MY&ceid=MY:en"
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
            pub = n.get("content") or n.get("datetime")
            break
    text_parts = []
    selectors = ["article","div.article-content","div.article-body","div.entry-content","div.story-body",
                 "div#article-body","main","div.td-post-content","div.elementor-widget-theme-post-content",
                 "div.elementor-widget-container","div.body-content","div.news-detail","div.single-content"]
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
for pir, slug, headline, note in QUERIES:
    print(f"\n[{pir}] gnews-RSS-search: {headline[:60]}")
    items = gnews_rss_search(headline)
    print(f"    gnews returned {len(items)} items")
    real_url = None
    for it in items[:8]:
        # gnews link is protobuf; the <source url=...> attribute gives the publisher domain
        pub_domain = it.get("source_url","")
        # Title often has " - Publisher" suffix; match headline
        t = re.sub(r"\s+-\s+[^-]+$","",it["title"]).strip()
        sim = sum(1 for w in headline.lower().split() if w in it["title"].lower())
        print(f"    [{pub_domain}] sim={sim}/len={len(headline.split())} | {it['title'][:90]} | pub={it['pubdate']}")
        if sim >= max(4, len(headline.split())*0.6) and pub_domain:
            real_url = pub_domain
            # Try to construct direct article URL? Just use the domain for now; better to follow source
            break
    # If we have a publisher domain, try to find the actual article via site search on publisher
    fetched_url = None; fetched_body = b""; fetched_code = "ERR"; fetched_final = ""
    if real_url:
        # Try fetching publisher homepage to find the article link, OR just record the publisher
        print(f"    publisher domain: {real_url}")
    # Also try: the gnews item link itself, following redirect (sometimes works for non-JS)
    if items:
        # Try following the first matching gnews link directly with curl -L
        for it in items[:5]:
            code, body, final = curl(it["link"], 20)
            # If final URL is a real publisher article (not news.google.com)
            if final and "news.google.com" not in final:
                fetched_url = final; fetched_body = body; fetched_code = code; fetched_final = final
                print(f"    RESOLVED via redirect -> {final}")
                break
    fname = f"priority_{pir.lower()}_gnews_{slug}_{TODAY}_{TS_TIME}.md"
    lines = []
    lines.append(f"# [PRIORITY {pir}] {slug} (gnews-recovery)")
    lines.append(f"Original headline: {headline}")
    lines.append(f"Note: {note}")
    lines.append(f"Collected: {TODAY} {TS} UTC ({NOW_ISO}) | MYT: {NOW_MYT}")
    lines.append(f"Classification: TLP:AMBER")
    if fetched_url:
        lines.append(f"Resolved URL: {fetched_url}")
        title = ""; body_text = ""; desc = ""; pub = ""
        if str(fetched_code) == "200":
            title, body_text, desc, pub = extract_article(fetched_url, fetched_body)
        lines.append(f"HTTP: {fetched_code} | Title: {title}")
        if pub: lines.append(f"ArticlePubDate: {pub}")
        if desc: lines.append(f"Description: {desc}")
        lines.append(f"Body chars: {len(body_text)}")
        lines.append("")
        lines.append("## Full text")
        lines.append("="*78)
        lines.append(body_text if body_text else "(no body extracted)")
        lines.append("="*78)
    else:
        lines.append(f"gnews resolution FAILED. Publisher domain hint: {real_url or 'none'}")
        lines.append(f"gnews items returned: {len(items)}")
        lines.append("")
        lines.append("## gnews RSS items (headline intelligence only)")
        lines.append("="*78)
        for it in items[:10]:
            lines.append(f"- {it['title']}  | pub={it['pubdate']} | source={it.get('source_url','')} | gnews={it['link']}")
        lines.append("="*78)
    with open(os.path.join(BASE, fname),"w",encoding="utf-8") as f:
        f.write("\n".join(lines))
    print(f"    saved {fname} (resolved={bool(fetched_url)})")
    results.append({"pir":pir,"slug":slug,"file":fname,"resolved":bool(fetched_url),
                    "resolved_url":fetched_url,"items_found":len(items)})

with open(os.path.join(BASE, f"_gnews_recovery_{TS}.json"),"w",encoding="utf-8") as f:
    json.dump(results, f, ensure_ascii=False, indent=2)
print(f"\n=== gnews recovery done: {len(results)} queries ===")
