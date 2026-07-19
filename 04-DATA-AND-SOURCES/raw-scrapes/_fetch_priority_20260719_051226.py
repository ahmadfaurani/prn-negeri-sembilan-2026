#!/usr/bin/env python3
"""Gnews URL resolver + priority fetcher for cycle 20260719_051226 (13:12 MYT 19 Jul).
Uses REGEX-based gnews RSS parsing (html.parser mangles <link/> self-closing tags).
Resolves gnews protobuf URLs to real publisher URLs via redirect-follow, then fetches.
Also directly fetches known real URLs for genuinely-new high-value articles.
TLP:AMBER. All content carries source URL.
"""
import subprocess, re, datetime, json, os, html

BASE = "/home/p62operator/.openclaw/workspace-ns/04-DATA-AND-SOURCES/raw-scrapes/20260719"
TS = "20260719_051226"
TODAY = "20260719"
TS_TIME = "051226"
NOW_ISO = datetime.datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S UTC")
NOW_MYT = (datetime.datetime.utcnow()+datetime.timedelta(hours=8)).strftime("%H:%M MYT %d %b %Y")
UA = ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36")

def curl(url, timeout=35):
    cmd = ["curl","-sS","-L","-m",str(timeout),"-A",UA,"--compressed",
           "-H","Accept-Language: en-US,en;q=0.9,ms;q=0.8",
           "-H","Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
           "-w","\n__HTTPCODE__:%{http_code}\n__FINALURL__:%{url_effective}",
           url]
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

def parse_gnews_regex(raw_bytes):
    """Regex parse gnews RSS to get {title, link, pubdate, source, source_url}."""
    txt = raw_bytes.decode("utf-8","replace")
    items = []
    for m in re.finditer(r"<item>(.*?)</item>", txt, re.S):
        block = m.group(1)
        tm = re.search(r"<title>(.*?)</title>", block, re.S)
        lm = re.search(r"<link>(.*?)</link>", block, re.S)
        pm = re.search(r"<pubDate>(.*?)</pubDate>", block, re.S)
        sm = re.search(r'<source\s+url="([^"]*)"[^>]*>(.*?)</source>', block, re.S)
        title = html.unescape(re.sub(r"\s+"," ",tm.group(1))).strip() if tm else ""
        link = lm.group(1).strip() if lm else ""
        pub = pm.group(1).strip() if pm else ""
        src = sm.group(2).strip() if sm else ""
        src_url = sm.group(1).strip() if sm else ""
        if title:
            items.append({"title":title,"link":link,"pubdate":pub,"source":src,"source_url":src_url})
    return items

def find_gnews_url_for_title(feed_url, title_needles):
    """Fetch gnews feed, return list of (title, gnews_url, pubdate, source_url) matching any needle."""
    code, body, _ = curl(feed_url, timeout=30)
    if code != "200": return []
    items = parse_gnews_regex(body)
    out = []
    tl = [n.lower() for n in title_needles]
    for it in items:
        for n in tl:
            if n in it["title"].lower():
                out.append(it); break
    return out

# ---- ARTICLE BODY EXTRACTOR ----
def extract_article(body):
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
                'meta[itemprop="datePublished"]','time[datetime]']:
        n = soup.select_one(sel)
        if n and (n.get("content") or n.get("datetime")):
            pub = n.get("content") or n.get("datetime"); break
    text_parts = []
    selectors = ["div.elementor-widget-theme-post-content",
                 "div.elementor-widget-container div.elementor-element",
                 "article","div.article-content","div.article-body","div.entry-content",
                 "div.post-content","div.content__body","div.field-body","div.story-body",
                 "div#article-body","div.article","main","div.td-post-content",
                 "div.almbe-article-body","div.posts","section.article","div.content-post",
                 "div.single-content","div.news-detail","div.kcontent","div.body-content","div#content"]
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

results = []
def save_article(pir, slug, url, final, code, body_bytes, note, mode):
    title, body_text, desc, pub = ("","","","")
    body_len = 0; ok = False
    if str(code) == "200":
        title, body_text, desc, pub = extract_article(body_bytes)
        body_len = len(body_text)
        if body_len > 150: ok = True
    fname = f"priority_{pir.lower().replace('+','-')}_{slug}_{TODAY}_{TS_TIME}.md"
    lines = [f"# [PRIORITY {pir}] {slug}",
             f"Source URL: {url}", f"Final/redirected URL: {final}",
             f"Collected: {TODAY} {TS} UTC ({NOW_ISO}) | MYT: {NOW_MYT}",
             f"Classification: TLP:AMBER", f"HTTP: {code} | mode: {mode}",
             f"Note: {note}", f"Title: {title}"]
    if pub: lines.append(f"ArticlePubDate: {pub}")
    if desc: lines.append(f"Description: {desc}")
    lines += [f"Body chars: {body_len}", "", "## Full text", "="*78,
              (body_text if body_text else "(no body extracted — possibly paywalled or JS-rendered)"),
              "="*78]
    with open(os.path.join(BASE, fname),"w",encoding="utf-8") as f:
        f.write("\n".join(lines))
    print(f"  [{pir}] {slug} | HTTP {code} | {'ok' if ok else 'thin/no-body'} | body={body_len} | pub={pub} | {fname}")
    results.append({"pir":pir,"slug":slug,"file":fname,"http":code,"ok":ok,
                    "body_len":body_len,"title":title,"final":final,"pub":pub,"mode":mode})

# ============================================================
# PART 1: DIRECT REAL-URL FETCHES (known mkini + Utusan URLs)
# ============================================================
print("=== PART 1: Direct real-URL fetches (genuinely-new high-value) ===")
DIRECT = [
    ("PIR-16+PIR-09+PIR-07","mkini-loke-malay-votes-mca-biggest-loser",
     "https://www.malaysiakini.com/news/780073",
     "mkini TOP STORY: 'Loke vows to win Malay votes, calls MCA biggest loser in BN-PN pact'. HIGH-VALUE PIR-16 (Loke narrative, DAP Malay-vote acceptance) + PIR-07 + PIR-09 (MCA). Genuinely-new this cycle. May be paywalled."),
    ("PIR-16+PIR-07","mkini-zan-azlee-indicator-commentary-v2",
     "https://www.malaysiakini.com/columns/780063",
     "mkini COMMENTARY: 'Oh, so the state elections are an indicator? Zan Azlee' — PIR-16 indicator narrative. Genuinely-new this cycle (distinct from prior 780023-era Zan Azlee piece)."),
    ("PIR-07","utusan-prn-ns-penentu-kerjasama-bn-pn",
     "https://www.utusan.com.my/nasional/2026/07/prn-negeri-sembilan-penentu-kerjasama-bn-dan-pn/",
     "Utusan: 'PRN Negeri Sembilan penentu kerjasama BN dan PN' — FRESH 12:11 MYT 19 Jul. PIR-07 coalition-arrangement narrative: NS PRN as determinant of BN-PN cooperation. HIGH-VALUE."),
    ("PIR-07+PIR-16","mkini-snapshot-anwar-ai-chatbot",
     "https://www.malaysiakini.com/news/780066",
     "mkini SNAPSHOT: 'Anwar AI chatbot is live, susceptible to manipulation' — PIR-07. New this cycle; campaign-tech narrative (lower core-PIR value but new signal)."),
    ("PIR-07","mkini-johor-exco-lineup",
     "https://www.malaysiakini.com/news/780048",
     "mkini: 'New Johor exco lineup to deliver manifesto pledges' — PIR-07 (Johor parallel-election context). New this cycle."),
]
for pir, slug, url, note in DIRECT:
    print(f"  fetch -> {url[:75]}")
    code, body, final = curl(url, timeout=35)
    save_article(pir, slug, url, final, code, body, note, mode="direct")

# ============================================================
# PART 2: GNEWS RESOLUTION for high-value NST/Star headlines
# (regex-parse gnews RSS to get protobuf links, follow redirect)
# ============================================================
print("\n=== PART 2: gnews resolution for high-value NST/Star/Melaka headlines ===")

# NST gnews feed — high-value titles to resolve
NST_FEED = "https://news.google.com/rss/search?q=site:nst.com.my+Negeri+Sembilan&hl=en-MY&gl=MY&ceid=MY:en"
NST_NEEDLES = [
    "BN-PN understanding aimed at ensuring Negri Sembilan political stability",
    "BN-PN electoral understanding strictly to avoid multi-cornered clashes",
    "PN to assist BN during Negri Sembilan polls campaign, says Hadi",
    "Bersatu goes solo in Negri Sembilan polls, PN says move expected",
    "Linggi move is risky for PH, says analyst",
    "Negri Sembilan polls: DAP faces battle against negative perception created by rivals",
    "Loke slams 'traitors' for plot to topple Negri Sembilan govt",
    "Negri Sembilan polls: Lion dance kicks off Tok Mat's bid to retain Rantau",
    "Negri Sembilan election: Supporters flood Seremban nomination centre",
    "Negri Sembilan polls: Chuah, Lukut and Bagan Pinang contests take shape",
]
# NST Melaka feed — Melaka DAP narrative
NST_MELAKA_FEED = "https://news.google.com/rss/search?q=site:nst.com.my+Melaka+DAP+appointed+assemblymen&hl=en-MY&gl=MY&ceid=MY:en"
NST_MELAKA_NEEDLES = [
    "Melaka clears path to appoint seven unelected assemblymen",
    "Melaka DAP quits state govt over appointed assemblymen amendment",
    "Anwar tells Melaka DAP to put state exit on hold",
    "Ab Rauf says PH only mirrored federal unity in Melaka",
    "DAP backs Melaka reps' decision to oppose appointed assemblymen",
]
# The Star gnews feed
STAR_FEED = "https://news.google.com/rss/search?q=site:thestar.com.my+Negeri+Sembilan&hl=en-MY&gl=MY&ceid=MY:en"
STAR_NEEDLES = [
    "Negri polls: Nomination opens for four state seats in Jelebu",
    "Negri polls: All eight nomination centres closed at 10am",
    "Polls shine light on PH-BN alliance",
    "Police to monitor social media during polls",
]
# Universal nomination — The Vibes / Newswav / CNA / Edge
VIBES_FEED = "https://news.google.com/rss/search?q=(%22nomination+day%22+OR+%22penamaan+calon%22)+AND+%22Negeri+Sembilan%22&hl=en-MY&gl=MY&ceid=MY:en"
VIBES_NEEDLES = [
    "Battle for Negeri Sembilan: Heavyweight clashes",
    "Negeri Sembilan poll race begins as nomination day kicks off",  # The Vibes
    "Negeri Sembilan race begins as nomination day kicks off",  # Newswav
    "Malaysia politics: Parties unveil candidates ahead of nomination day",  # CNA
    "Over 22,000 PDRM, ARM personnel to vote early",
    "Negeri Sembilan state polls: Loke says ready to face all comers in Chennah",
    "Hadi says Perikatan and BN will campaign for each other in Negeri Sembilan polls",
    "Umno sec-gen says BN-Perikatan understanding puts stability first in Negeri Sembilan polls",
    "MCA to contest seven seats, MIC four in Negeri Sembilan polls",
    "Pakatan's Negeri Sembilan team enters race with strong show of support",
]

# Map source-key to (feed, needles, slug-prefix)
FEED_MAP = [
    ("nst", NST_FEED, NST_NEEDLES, "nst"),
    ("nst-melaka", NST_MELAKA_FEED, NST_MELAKA_NEEDLES, "nst-melaka"),
    ("star", STAR_FEED, STAR_NEEDLES, "star"),
    ("vibes", VIBES_FEED, VIBES_NEEDLES, "vibes"),
]

resolved_count = 0
fetch_count = 0
for fkey, feed, needles, prefix in FEED_MAP:
    print(f"  [{fkey}] resolving {len(needles)} needles...")
    matches = find_gnews_url_for_title(feed, needles)
    print(f"    found {len(matches)} matches in feed")
    for it in matches:
        gurl = it["link"]
        if not gurl or "news.google.com" not in gurl:
            continue
        resolved_count += 1
        # Follow gnews redirect to get real publisher URL
        code, body, final = curl(gurl, timeout=30)
        real_url = final
        slug_base = re.sub(r"[^a-z0-9]+","-", it["title"][:60].lower()).strip("-")
        # Determine PIR tag
        t = it["title"].lower()
        pir = "PIR-07"
        if any(k in t for k in ["melaka","dap quits","appointed assemblymen","anwar tells melaka"]):
            pir = "PIR-16+PIR-07"
        if any(k in t for k in ["bersatu","pecat","keluar","muhyiddin","hadi"]):
            pir = "PIR-06+PIR-07"
        if any(k in t for k in ["loke","mca biggest","malay vote","traitor"]):
            pir = "PIR-16+PIR-07"
        if real_url and not real_url.startswith("https://news.google.com"):
            # Real publisher URL resolved — fetch it
            fetch_count += 1
            note = f"gnews-resolve: '{it['title'][:70]}' | gnews pubdate: {it['pubdate']} | source: {it['source']} ({it['source_url']})"
            print(f"    RESOLVED -> {real_url[:80]}")
            save_article(pir, f"{prefix}-{slug_base}", real_url, real_url, "200", b"", note, mode="gnews-resolved-needs-fetch")
            # Actually fetch the real URL now
            code2, body2, final2 = curl(real_url, timeout=35)
            save_article(pir, f"{prefix}-{slug_base}", real_url, final2, code2, body2, note, mode="gnews-resolved")
        else:
            # Could not resolve — save gnews intermediate as headline intelligence
            note = f"gnews UNRESOLVED: '{it['title'][:70]}' | gnews pubdate: {it['pubdate']} | source: {it['source']} ({it['source_url']}) | gnews final: {final}"
            fname = f"priority_{pir.lower().replace('+','-')}_{prefix}-{slug_base}_{TODAY}_{TS_TIME}.md"
            with open(os.path.join(BASE, fname),"w",encoding="utf-8") as f:
                f.write(f"# [PRIORITY {pir}] {prefix}-{slug_base} (gnews-resolve FAILED — headline intelligence)\n"
                        f"Source gnews URL: {gurl}\nFinal URL: {final}\n"
                        f"Collected: {TODAY} {TS} UTC ({NOW_ISO}) | MYT: {NOW_MYT}\n"
                        f"Classification: TLP:AMBER\nHTTP: {code}\n"
                        f"Title (from gnews): {it['title']}\nPubDate: {it['pubdate']}\n"
                        f"Publisher: {it['source']} ({it['source_url']})\nNote: {note}\n")
            print(f"    !! unresolved -> saved headline intelligence: {fname}")
            results.append({"pir":pir,"slug":f"{prefix}-{slug_base}","file":fname,"http":code,"ok":False,
                            "body_len":0,"title":it["title"],"final":final,"pub":it["pubdate"],"mode":"gnews-unresolved"})

print(f"\n  gnews matches processed: {resolved_count} | real-URL fetches attempted: {fetch_count}")

with open(os.path.join(BASE, f"_priority_fetch_results_{TS}.json"),"w",encoding="utf-8") as f:
    json.dump(results, f, ensure_ascii=False, indent=2)
print(f"\n=== Wrote _priority_fetch_results_{TS}.json ({len(results)} targets, {sum(1 for r in results if r['ok'])} ok) ===")
