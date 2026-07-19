#!/usr/bin/env python3
"""Priority full-text fetcher for cycle 20260719_034922 (11:49 MYT 19 Jul).
Fetches genuinely-new high-value articles published/surfaced since prior 024042
cycle (10:40 MYT), plus recovery of high-value PIR-06/07/16 narrative items.

Targets (real URLs only; gnews-protobuf items resolved where feasible):
  - kosmo 'Polis terima satu laporan gaduh mulut' (fresh 10:54 MYT, PIR-07)
  - utusan 'Berkempen jangan langgar peraturan jalan raya - Anthony Loke' (fresh 11:32 MYT, PIR-07+16)
  - mkini 'Wee: BN-PN pact not a merger, MCA principles intact' (PIR-06+16, coalition arrangement)
  - mkini 'SNAPSHOT ... Bersatu exit from PN imminent?' (PIR-06+16, disarray)
  - mkini 'SNAPSHOT BN-PN ties based on friendship, brotherhood - Hadi; Tok Mat keep adat out' (PIR-16 adat)
  - mkini 'Coalition leaders, supporters in full force for NS nominations' (PIR-07)
  - mkini 'MCA Youth sec-gen told to stay out of NS polls' (PIR-07+16)
  - mkini 'Tamim surrenders to police, hopes to campaign for independent' (PIR-09, independent narrative)
  - Resolve 2 gnews-only high-value headlines: 'Anwar urges Melaka DAP postpone quit' (PIR-16 Melaka), Newswav 'NS race begins as nomination day kicks off'

Elementor-aware + generic extraction. TLP:AMBER. All content carries source URL.
"""
import subprocess, re, datetime, json, os
from bs4 import BeautifulSoup

BASE = "/home/p62operator/.openclaw/workspace-ns/04-DATA-AND-SOURCES/raw-scrapes/20260719"
TS = "20260719_034922"
TODAY = "20260719"
TS_TIME = "034922"
NOW_ISO = datetime.datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S UTC")
NOW_MYT = (datetime.datetime.utcnow()+datetime.timedelta(hours=8)).strftime("%H:%M MYT %d %b %Y")
UA = ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36")

# (pir, slug, url, note, is_gnews_resolve)
TARGETS = [
    ("PIR-07","kosmo-polis-gaduh-mulut",
     "https://www.kosmo.com.my/2026/07/19/prn-negeri-sembilan-polis-terima-satu-laporan-gaduh-mulut/",
     "Kosmo: PRN NS — police received one 'verbal dispute' report (fresh ~10:54 MYT 19 Jul). Day-1 campaign-ops PIR-07 signal.", False),
    ("PIR-07+PIR-16","utusan-loke-berkempen-jalan-raya",
     "https://www.utusan.com.my/nasional/2026/07/berkempen-jangan-langgar-peraturan-jalan-raya-anthony-loke/",
     "Utusan: Anthony Loke urges compliance with traffic rules during campaign (fresh ~11:32 MYT 19 Jul). PIR-07 campaign + PIR-16 Loke narrative.", False),
    ("PIR-06+PIR-16","mkini-wee-bn-pn-not-merger",
     "https://www.malaysiakini.com/news/780035",
     "mkini: Wee Ka Siong — BN-PN pact in NS is NOT a merger, MCA principles intact. HIGH-VALUE PIR-06 coalition arrangement + PIR-16 narrative. May be paywalled (capture preview+meta).", False),
    ("PIR-06+PIR-16","mkini-snapshot-bersatu-exit-pn-imminent",
     "https://www.malaysiakini.com/news/780047",
     "mkini SNAPSHOT: 'Bersatu exit from PN imminent?' — rhetorical-question headline is a strong PIR-06+16 disarray signal. Capture SNAPSHOT body/preview.", False),
    ("PIR-16+PIR-07","mkini-snapshot-hadi-tokmat-adat",
     "https://www.malaysiakini.com/news/780030",
     "mkini SNAPSHOT: 'BN-PN ties based on friendship, brotherhood - Hadi; Tok Mat says keep adat out of polls campaign'. PIR-16 'adat' narrative + PIR-07.", False),
    ("PIR-07","mkini-coalition-leaders-full-force-nominations",
     "https://www.malaysiakini.com/news/780023",
     "mkini: 'Coalition leaders, supporters in full force for N Sembilan polls nominations' — Day-1 nomination narrative, PIR-07.", False),
    ("PIR-07+PIR-16","mkini-mca-youth-stay-out",
     "https://www.malaysiakini.com/news/780017",
     "mkini: 'MCA Youth sec-gen told to stay out of NS polls over PN ally disagreement' — PIR-07 + PIR-16 (BN-PN tension narrative).", False),
    ("PIR-09+PIR-16","mkini-tamim-surrenders-independent",
     "https://www.malaysiakini.com/news/780055",
     "mkini: 'Tamim surrenders to police, hopes to campaign for N Sembilan independent candidate' — PIR-09 (Tamim, independent) + PIR-16 (independent/sole-opposition narrative).", False),
]

# gnews-protobuf URLs to attempt to resolve (decode redirect)
GNEWS_RESOLVE = [
    ("PIR-16","star-anwar-melaka-dap-postpone",
     "https://news.google.com/rss/articles/CBMiuwFBVV95cUxPRUg3cklyc3BQNFV2TjBfMmZ3OE91Um1PZUc1bkNfUjRzc19mUVBJQmluM2oxUl9kYjE0Y2l4ZWh0bUJjbEtfY3lpaXB0VGlfSTdRSDlfZjV6VFlLdmRwajJ4QXNxQmZ5VGRDUjJrZkFfTnZCSG15b2x2c2J5aGxCaFZKaFNYSW12NVJjdW5qRERZeWN4YlZjZ3AxNkxkMW5tVnFfYUNrdzBOUmRXaF9mejBtRzBrcWZqX1BOdXc?oc=5",
     "gnews-redirect: The Star — 'Anwar urges Melaka DAP to postpone decision to quit state govt'. PIR-16 Melaka-withdrawal narrative. Attempt to resolve to real URL + fetch."),
    ("PIR-07","newswav-ns-race-begins-nomination-day",
     "https://news.google.com/rss/articles/CBMixAFBVV95cUxOdlBpdzNfVlhKc0w5OHl6VFl0azJVRUZ6Y3l1bVlBZ0NfX0NUaW9QNjNkQjZKdzJveWx5OVQwRE1vUUR4ZjBNZ3hfbGxjMm1kVlB4X3Q1WjhYZVJXSDdZc2pVR2pTeDl3WGZFbm5IdXdJOHdjcjNqRG5TYjZuNmhOQzJwUWNoSDJ5MjZUd2Y3SExYVWF1NGo1UE9SUGMwT1BmdzBfYzR3Zlc4Rk5KX2x4cTFuSTBpNXNSQXJ2NlFYalFkbWtJZ2JlRXBEYUl6UWx1UHFfNFF6b0g4aHF2SjlZbXVZdGFScTVKZGs?oc=5",
     "gnews-redirect: Newswav — 'Negeri Sembilan race begins as nomination day kicks off'. PIR-07 Day-1 narrative. Attempt resolve."),
]

def fetch(url, timeout=35):
    cmd = ["curl","-sS","-L","-m",str(timeout),"-A",UA,"--compressed",
           "-H","Accept-Language: en-US,en;q=0.9,ms;q=0.8",
           "-H","Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
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

def extract_article(url, body):
    try:
        soup = BeautifulSoup(body.decode("utf-8","replace"), "html.parser")
    except Exception:
        return "","","",""
    title = ""
    if soup.title and soup.title.string:
        title = soup.title.string.strip()
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
    selectors = ["div.elementor-widget-theme-post-content",
                 "div.elementor-widget-container div.elementor-element",
                 "article","div.article-content","div.article-body","div.entry-content",
                 "div.post-content","div.content__body","div.field-body","div.story-body",
                 "div#article-body","div.article","main","div.td-post-content",
                 "div.almbe-article-body","div.posts","section.article",
                 "div.content-post","div.single-content","div.news-detail","div.kcontent",
                 "div.body-content","div#content"]
    for sel in selectors:
        nodes = soup.select(sel)
        for node in nodes:
            for p in node.find_all(["p","li","h2","h3","blockquote"]):
                t = p.get_text(" ", strip=True)
                if t and len(t) > 25:
                    text_parts.append(t)
            if text_parts:
                break
        if text_parts:
            break
    if not text_parts:
        for p in soup.find_all("p"):
            t = p.get_text(" ", strip=True)
            if t and len(t) > 40:
                text_parts.append(t)
    body_text = "\n\n".join(text_parts[:140])
    return title[:300], body_text[:28000], (desc or "")[:800], pub

results = []
def do_fetch(pir, slug, url, note, mode="direct"):
    print(f"\n[{pir}] {slug} -> {url[:80]}")
    code, body, final = fetch(url)
    fname = f"priority_{pir.lower().replace('+','-')}_{slug}_{TODAY}_{TS_TIME}.md"
    lines = []
    lines.append(f"# [PRIORITY {pir}] {slug}")
    lines.append(f"Source URL: {url}")
    lines.append(f"Final/redirected URL: {final}")
    lines.append(f"Collected: {TODAY} {TS} UTC ({NOW_ISO}) | MYT: {NOW_MYT}")
    lines.append(f"Classification: TLP:AMBER")
    lines.append(f"HTTP: {code} | mode: {mode} | note: {note}")
    ok = False
    title = ""; body_text = ""; desc = ""; pub = ""; body_len = 0
    if str(code) == "200":
        title, body_text, desc, pub = extract_article(url, body)
        body_len = len(body_text)
        if body_len > 150:
            ok = True
    lines.append(f"Title: {title}")
    if pub: lines.append(f"ArticlePubDate: {pub}")
    if desc: lines.append(f"Description: {desc}")
    lines.append(f"Body chars: {body_len}")
    lines.append("")
    lines.append("## Full text")
    lines.append("="*78)
    lines.append(body_text if body_text else "(no body extracted — possibly paywalled or JS-rendered)")
    lines.append("="*78)
    with open(os.path.join(BASE, fname),"w",encoding="utf-8") as f:
        f.write("\n".join(lines))
    status = "ok" if ok else "thin/no-body"
    print(f"    HTTP {code} | {status} | body={body_len} | pub={pub} | {fname}")
    results.append({"pir":pir,"slug":slug,"file":fname,"http":code,"ok":ok,
                     "body_len":body_len,"title":title,"final":final,
                     "pub":pub,"mode":mode,"note":note})
    return code, body, final

# 1) Direct real-URL fetches
for pir, slug, url, note, _ in TARGETS:
    do_fetch(pir, slug, url, note, mode="direct")

# 2) gnews-protobuf resolution attempts (decode redirect to get real publisher URL)
for pir, slug, gurl, note in GNEWS_RESOLVE:
    print(f"\n[{pir}] gnews-resolve {slug} -> {gurl[:70]}...")
    # First follow the gnews redirect to get the real publisher URL
    code, body, final = fetch(gurl, timeout=30)
    # gnews typically redirects to the real article; check final URL
    real_url = final
    if real_url and not real_url.startswith("https://news.google.com"):
        print(f"    resolved -> {real_url[:80]}")
        do_fetch(pir, slug, real_url, note + f" [resolved from gnews to {real_url}]", mode="gnews-resolve")
    else:
        # Try to extract the real URL from the gnews intermediate page
        m = re.search(rb'(https?://[^"\'<\s]+(?:nst|thestar|star|newswav|malaysiakini|astroawani|bharian|mstar|kosmo|utusan|freemalaysiatoday|thevibes|malaysianreserve|edgedailymalaysia|themalaysianinsight|malaymail)\.[^"\'<\s]+)', body, re.I)
        if m:
            real_url = m.group(1).decode("utf-8","replace")
            print(f"    extracted -> {real_url[:80]}")
            do_fetch(pir, slug, real_url, note + f" [extracted from gnews body]", mode="gnews-extract")
        else:
            # Save the gnews intermediate body as intelligence
            fname = f"priority_{pir.lower().replace('+','-')}_{slug}_{TODAY}_{TS_TIME}.md"
            with open(os.path.join(BASE, fname),"w",encoding="utf-8") as f:
                f.write(f"# [PRIORITY {pir}] {slug} (gnews-resolve FAILED — raw intermediate)\n"
                        f"Source gnews URL: {gurl}\nFinal URL: {final}\n"
                        f"Collected: {TODAY} {TS} UTC | MYT: {NOW_MYT}\n"
                        f"Classification: TLP:AMBER\nHTTP: {code}\n"
                        f"Note: {note}\n\n## Raw gnews intermediate body (first 4000 chars)\n{'='*78}\n"
                        f"{body.decode('utf-8','replace')[:4000]}\n{'='*78}\n")
            print(f"    !! could not resolve gnews -> saved intermediate ({len(body)} bytes)")
            results.append({"pir":pir,"slug":slug,"file":fname,"http":code,"ok":False,
                            "body_len":len(body),"title":"","final":final,"pub":"",
                            "mode":"gnews-unresolved","note":note+" [resolution failed]"})

with open(os.path.join(BASE, f"_priority_fetch_results_{TS}.json"),"w",encoding="utf-8") as f:
    json.dump(results, f, ensure_ascii=False, indent=2)
print(f"\n=== Wrote _priority_fetch_results_{TS}.json ({len(results)} targets, {sum(1 for r in results if r['ok'])} ok) ===")
