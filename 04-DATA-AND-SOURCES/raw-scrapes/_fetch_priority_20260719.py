#!/usr/bin/env python3
"""Priority full-text fetcher for cycle 20260719_011915.
Fetches genuinely-new Day-2 morning MYT articles (published 08:28-09:18 MYT 19 Jul)
+ attempts recovery of the deferred NST 'Bersatu at a crossroads' PIR-06 piece.
Saves as priority_pirXX_*.md with Elementor-aware + generic extraction."""
import subprocess, re, datetime, json, os
from bs4 import BeautifulSoup

BASE = "/home/p62operator/.openclaw/workspace-ns/04-DATA-AND-SOURCES/raw-scrapes/20260719"
TS = "20260719_011915"
TODAY = "20260719"
NOW_ISO = datetime.datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S UTC")
NOW_MYT = (datetime.datetime.utcnow()+datetime.timedelta(hours=8)).strftime("%H:%M MYT %d %b %Y")
UA = ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36")

# (pir, slug, url, note)
TARGETS = [
    ("PIR-07","prn-ns-penentu-hala-tuju-dap-utusan",
     "https://www.utusan.com.my/rencana/2026/07/prn-negeri-sembilan-penentu-hala-tuju-dap/",
     "Utusan: PRN NS determines DAP's direction (brand-new 09:18 MYT 19 Jul / 01:18 UTC). Rencana/opinion."),
    ("PIR-06","percaturan-bn-ph-bersatu-kosmo",
     "https://www.kosmo.com.my/2026/07/19/percaturan-bn-ph-bersatu/",
     "Kosmo: The BN-PH-Bersatu configuration/maneuvering (brand-new 09:05 MYT 19 Jul / 01:05 UTC). PIR-06-tagged."),
    ("PIR-07","felda-martabat-peneroka-anwar-utusan",
     "https://www.utusan.com.my/nasional/2026/07/felda-mesti-terus-angkat-martabat-peneroka-anwar/",
     "Utusan: PM Anwar - Felda must continue uplifting settlers (brand-new 08:28 MYT 19 Jul / 00:28 UTC). PIR-07 campaign-adjacent."),
    # ---- deferred PIR-06 recovery attempts (NST 'Bersatu at a crossroads') ----
    ("PIR-06","bersatu-crossroads-nst-retry",
     "https://www.nst.com.my/wp-json/wp/v2/posts?search=bersatu+crossroads&per_page=5",
     "NST WP-API search for 'Bersatu at a crossroads' (deferred PIR-06 recovery). Returns JSON if WP-API exposed."),
    ("PIR-06","nst-ns-recent-wpapi",
     "https://www.nst.com.my/wp-json/wp/v2/posts?search=negeri+sembilan+bersatu&per_page=10",
     "NST WP-API search for recent NS+Bersatu articles (best-effort new-content probe)."),
]

def fetch(url, timeout=35):
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

def extract_article(url, body):
    """Full-text extraction. Elementor-aware for Utusan; generic for others."""
    try:
        soup = BeautifulSoup(body.decode("utf-8","replace"), "html.parser")
    except Exception:
        return "","",""
    title = ""
    if soup.title and soup.title.string:
        title = soup.title.string.strip()
    og = soup.find("meta", property="og:title")
    if og and og.get("content"): title = og["content"].strip()
    desc = ""
    md = soup.find("meta", attrs={"name":"description"}) or soup.find("meta", property="og:description")
    if md and md.get("content"): desc = md["content"].strip()
    # body — try Elementor first (Utusan), then common selectors
    text_parts = []
    selectors = ["div.elementor-widget-theme-post-content",
                 "div.elementor-widget-theme-post-content.elementor-element",
                 "div.elementor-widget-container div.elementor-element",
                 "article","div.article-content","div.article-body","div.entry-content",
                 "div.post-content","div.content__body","div.field-body","div.story-body",
                 "div#article-body","div.article","main","div.td-post-content"]
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
    body_text = "\n\n".join(text_parts[:100])
    return title[:300], body_text[:25000], desc[:600]

def extract_wpapi_search(body):
    """Parse WP-API search JSON; return list of {title, link, date, excerpt}."""
    try:
        data = json.loads(body.decode("utf-8","replace"))
    except Exception:
        return None
    out = []
    if isinstance(data, list):
        for p in data:
            if isinstance(p, dict):
                out.append({"title":p.get("title",{}).get("rendered",""),
                            "link":p.get("link",""),
                            "date":p.get("date_gmt","") or p.get("date",""),
                            "excerpt":p.get("excerpt",{}).get("rendered","")[:300]})
    return out

results = []
for pir, slug, url, note in TARGETS:
    print(f"\n[{pir}] {slug} -> {url[:75]}")
    code, body, final = fetch(url)
    is_wpapi = "wp-json/wp/v2" in url
    fname = f"priority_{pir.lower()}_{slug}_{TODAY}_{TS.split('_')[1]}.md"
    lines = []
    lines.append(f"# [PRIORITY {pir}] {slug}")
    lines.append(f"Source URL: {url}")
    lines.append(f"Final/redirected URL: {final}")
    lines.append(f"Collected: {TODAY} {TS} UTC ({NOW_ISO}) | MYT: {NOW_MYT}")
    lines.append(f"Classification: TLP:AMBER")
    lines.append(f"HTTP: {code} | note: {note}")
    lines.append("")
    lines.append("## Article Body (extracted)")
    lines.append("="*70)

    if is_wpapi:
        arts = extract_wpapi_search(body)
        if arts is None:
            lines.append(f"[WP-API NOT AVAILABLE — HTTP {code}, {len(body)} bytes. NST likely not WP-backed or endpoint blocked.]")
            print(f"  HTTP {code} | WP-API not JSON ({len(body)} bytes)")
            results.append({"pir":pir,"slug":slug,"file":fname,"http":code,"ok":False,
                            "body_len":0,"mode":"wpapi","final":final})
        elif len(arts) == 0:
            lines.append(f"[WP-API returned 0 posts for this search — HTTP {code}.]")
            print(f"  HTTP {code} | WP-API 0 results")
            results.append({"pir":pir,"slug":slug,"file":fname,"http":code,"ok":False,
                            "body_len":0,"mode":"wpapi","n":0,"final":final})
        else:
            lines.append(f"[WP-API search returned {len(arts)} post(s). Capturing all as structured metadata.]")
            print(f"  HTTP {code} | WP-API returned {len(arts)} posts")
            for i, a in enumerate(arts):
                lines.append("")
                lines.append(f"### [{i+1}] {a['title']}")
                lines.append(f"URL: {a['link']}")
                lines.append(f"Date: {a['date']}")
                lines.append(f"Excerpt: {a['excerpt']}")
            results.append({"pir":pir,"slug":slug,"file":fname,"http":code,"ok":True,
                            "body_len":sum(len(a['excerpt']) for a in arts),"mode":"wpapi",
                            "n":len(arts),"final":final,"posts":arts})
    else:
        title, text, desc = extract_article(url, body) if body else ("","","")
        ok = bool(text) and code == "200"
        lines.append(f"Page title: {title}")
        if desc: lines.append(f"Meta desc: {desc}")
        lines.append("")
        if text:
            lines.append(text)
        else:
            lines.append(f"[NO BODY EXTRACTED — code={code}, bytes={len(body)}. "
                         f"Headline + URL captured in raw scrape .md.]")
        print(f"  HTTP {code} | title={title[:50]!r} body={len(text)} chars | ok={ok}")
        results.append({"pir":pir,"slug":slug,"file":fname,"http":code,"ok":ok,
                        "body_len":len(text),"title":title,"final":final})
    lines.append("="*70)
    with open(os.path.join(BASE, fname),"w",encoding="utf-8") as f:
        f.write("\n".join(lines))

print("\n=== PRIORITY FETCH RESULTS ===")
for r in results:
    print(f"  [{r['http']}] ok={r['ok']} body={r.get('body_len',0):6d}  {r['pir']} {r['slug']}  -> {r['file']}")

# save fetcher results
with open(os.path.join(BASE, f"_priority_fetch_results_{TS}.json"),"w",encoding="utf-8") as f:
    json.dump(results, f, ensure_ascii=False, indent=2)
print(f"\nWrote _priority_fetch_results_{TS}.json")
