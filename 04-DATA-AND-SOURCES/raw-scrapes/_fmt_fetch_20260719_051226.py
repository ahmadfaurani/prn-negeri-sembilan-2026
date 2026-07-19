#!/usr/bin/env python3
"""FMT (Free Malaysia Today) priority article fetcher for cycle 20260719_051226.
FMT is curl-friendly. Fetch all 20 NS-relevant articles, extract body, save as priority files.
TLP:AMBER.
"""
import subprocess, re, html, os, datetime, time

BASE = "/home/p62operator/.openclaw/workspace-ns/04-DATA-AND-SOURCES/raw-scrapes/20260719"
TS = "20260719_051226"; TODAY = "20260719"; TS_TIME = "051226"
NOW_ISO = datetime.datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S UTC")
NOW_MYT = (datetime.datetime.utcnow()+datetime.timedelta(hours=8)).strftime("%H:%M MYT %d %b %Y")
UA = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36"

def curl(url, timeout=30):
    cmd = ["curl","-sS","-L","-m",str(timeout),"-A",UA,"--compressed",
           "-H","Accept-Language: en-US,en;q=0.9,ms;q=0.8", url]
    try:
        p = subprocess.run(cmd, capture_output=True, timeout=timeout+10)
        return "200", p.stdout
    except Exception as e:
        return "ERR", str(e).encode()

def extract(body):
    from bs4 import BeautifulSoup
    try:
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
                'meta[itemprop="datePublished"]','time[datetime]','meta[property="og:updated_time"]']:
        n = soup.select_one(sel)
        if n and (n.get("content") or n.get("datetime")):
            pub = n.get("content") or n.get("datetime"); break
    text_parts = []
    # FMT article body selectors
    for sel in ["div.article-content","div.entry-content","article","div.post-content",
                "div.elementor-widget-theme-post-content","div.td-post-content","main","div.content__body",
                "div.article-body","div.single-content","div#article-body"]:
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
    return title[:300], "\n\n".join(text_parts[:160])[:30000], (desc or "")[:800], pub

# All 20 FMT NS-relevant articles from the RSS feed
ARTICLES = [
    ("https://www.freemalaysiatoday.com/category/nation/2026/07/18/bns-support-for-pn-in-11-negeri-sembilan-seats-part-of-political-reality-says-zahid", "PIR-06+PIR-07", "fmt-zahid-bn-support-pn-11-seats-political-reality"),
    ("https://www.freemalaysiatoday.com/category/nation/2026/07/19/bn-pn-cooperation-gets-thumbs-up-from-grassroots-members", "PIR-06+PIR-07", "fmt-bn-pn-cooperation-thumbs-up-grassroots"),
    ("https://www.freemalaysiatoday.com/category/nation/2026/07/19/quit-pn-with-gerakan-mipp-in-tow-bersatu-advised", "PIR-06", "fmt-quit-pn-gerakan-mipp-bersatu-advised"),
    ("https://www.freemalaysiatoday.com/category/opinion/2026/07/19/umnos-dangerous-dance-with-pas", "PIR-16+PIR-06", "fmt-umno-dangerous-dance-pas-opinion"),
    ("https://www.freemalaysiatoday.com/category/nation/2026/07/19/bn-pas-tie-up-will-force-mca-to-make-difficult-choice", "PIR-16+PIR-06", "fmt-bn-pas-tie-up-mca-difficult-choice"),
    ("https://www.freemalaysiatoday.com/category/nation/2026/07/18/give-ph-stronger-mandate-anwar-tells-negeri-sembilan-voters", "PIR-07+PIR-16", "fmt-anwar-give-ph-stronger-mandate-ns-voters"),
    ("https://www.freemalaysiatoday.com/category/nation/2026/07/18/bersatu-must-survive-as-lone-opposition-says-muhyiddin", "PIR-06", "fmt-bersatu-must-survive-lone-opposition-muhyiddin"),
    ("https://www.freemalaysiatoday.com/category/nation/2026/07/18/bn-pn-performance-in-negeri-sembilan-to-determine-future-alliance-says-zahid", "PIR-06+PIR-07", "fmt-zahid-bn-pn-performance-ns-determine-future-alliance"),
    ("https://www.freemalaysiatoday.com/category/nation/2026/07/18/103-candidates-vying-for-36-seats-in-negeri-sembilan-polls", "PIR-07", "fmt-103-candidates-36-seats-ns-polls"),
    ("https://www.freemalaysiatoday.com/category/nation/2026/07/18/hadi-denies-pas-made-pn-toxic-blames-bersatu-instead", "PIR-06", "fmt-hadi-denies-pas-made-pn-toxic-blames-bersatu"),
    ("https://www.freemalaysiatoday.com/category/nation/2026/07/18/bn-to-decide-negeri-sembilan-mb-candidate-only-if-it-wins-polls", "PIR-16+PIR-07", "fmt-bn-decide-ns-mb-candidate-only-if-wins"),
    ("https://www.freemalaysiatoday.com/category/nation/2026/07/18/bn-pn-cooperation-only-to-avoid-vote-splits-says-wee", "PIR-06+PIR-16", "fmt-bn-pn-cooperation-avoid-vote-splits-wee"),
    ("https://www.freemalaysiatoday.com/category/nation/2026/07/18/mca-youth-sec-gen-told-to-skip-negeri-sembilan-campaign", "PIR-16+PIR-06", "fmt-mca-youth-sec-gen-skip-ns-campaign"),
    ("https://www.freemalaysiatoday.com/category/nation/2026/07/18/tok-mat-in-straight-fight-with-ph-in-rantau", "PIR-07", "fmt-tok-mat-straight-fight-ph-rantau"),
    ("https://www.freemalaysiatoday.com/category/nation/2026/07/18/full-list-of-candidates-contesting-in-negeri-sembilan", "PIR-07", "fmt-full-list-candidates-ns"),
    ("https://www.freemalaysiatoday.com/category/nation/2026/07/18/loke-faces-mca-challenger-in-chennah-straight-fight", "PIR-07+PIR-16", "fmt-loke-mca-challenger-chennah-straight-fight"),
    ("https://www.freemalaysiatoday.com/category/nation/2026/07/18/lim-rejects-islamophobia-claim-says-hadi-coined-green-wave-term", "PIR-16", "fmt-lim-rejects-islamophobia-hadi-green-wave"),
    ("https://www.freemalaysiatoday.com/category/nation/2026/07/18/lokes-aide-in-5-cornered-fight-for-4th-term-in-nilai", "PIR-07", "fmt-loke-aide-5-cornered-fight-nilai"),
    ("https://www.freemalaysiatoday.com/category/nation/2026/07/18/pn-bn-ties-in-negeri-sembilan-more-than-a-marriage-says-hadi", "PIR-06", "fmt-pn-bn-ties-ns-more-than-marriage-hadi"),
    ("https://www.freemalaysiatoday.com/category/nation/2026/07/19/firefighters-suspend-search-at-collapsed-melaka-shophouse", "PIR-16+PIR-07", "fmt-melaka-shophouse-collapse-search-suspended"),
]

saved = 0; ok_count = 0
for url, pir, slug in ARTICLES:
    code, body = curl(url, timeout=30)
    title, body_text, desc, pub = ("","","","")
    if str(code) == "200":
        title, body_text, desc, pub = extract(body)
    blen = len(body_text)
    ok = blen > 150
    if ok: ok_count += 1
    fname = f"priority_{pir.lower().replace('+','-')}_{slug}_{TODAY}_{TS_TIME}.md"
    lines = [f"# [PRIORITY {pir}] {slug}",
             f"Source URL: {url}", f"Collected: {TODAY} {TS} UTC ({NOW_ISO}) | MYT: {NOW_MYT}",
             f"Classification: TLP:AMBER", f"Source: Free Malaysia Today (freemalaysiatoday.com)",
             f"HTTP: {code} | mode: fmt-direct", f"Title: {title}"]
    if pub: lines.append(f"ArticlePubDate: {pub}")
    if desc: lines.append(f"Description: {desc}")
    lines += [f"Body chars: {blen}", "", "## Full text", "="*78,
              (body_text if body_text else "(no body extracted)"), "="*78]
    with open(os.path.join(BASE, fname),"w",encoding="utf-8") as f:
        f.write("\n".join(lines))
    print(f"  [{pir}] {slug[:60]} | HTTP {code} | {'ok' if ok else 'thin'} | body={blen} | pub={pub}")
    saved += 1
    time.sleep(0.4)

print(f"\nFMT articles saved: {saved} | with body: {ok_count}")
