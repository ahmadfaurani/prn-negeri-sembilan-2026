#!/usr/bin/env python3
"""Evening-cycle fetch for 20260719_091800 (17:18 MYT 19 Jul — Nomination-Day+1, Campaign Day 1).
4th carry-forward of 14:50 Director-approved cycle. Re-poll proven sources for fresh post-15:50 MYT content:
  - FMT RSS (content:encoded, curl-friendly)
  - NST WordPress feed (content:encoded)
  - Awani berita-politik direct (curl-friendly static HTML)
  - mkini direct (paywalled, previews) — scan IDs 780110-780140
  - Google News universal queries incl. "kuorum" (PIR-06 NEW requirement)
  - NEW: BH (Berita Harian) RSS, mStar RSS, Sinar Harian RSS — prior cycle marked "untested"
  - gnews headline intelligence for unreachable items
TLP:AMBER. All content carries source URL.
"""
import subprocess, re, datetime, json, os, html, glob
from urllib.parse import urljoin

BASE = "/home/p62operator/.openclaw/workspace-ns/04-DATA-AND-SOURCES/raw-scrapes/20260719"
THIS_TS = "20260719_091800"
PRIOR_TS_LIST = ["20260719_075200","20260719_064654","20260719_051226","20260719_034922","20260719_024042","20260719_011915"]
TODAY = "20260719"
TS_TIME = "091800"
CUTOFF_UTC = "2026-07-19T07:50:00+00:00"   # prior cycle cutoff (15:50 MYT)
NOW_ISO = datetime.datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S UTC")
NOW_MYT = (datetime.datetime.utcnow()+datetime.timedelta(hours=8)).strftime("%H:%M MYT %d %b %Y")
UA = ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36")

def curl(url, timeout=35, extra_headers=None):
    cmd = ["curl","-sS","-L","-m",str(timeout),"-A",UA,"--compressed",
           "-H","Accept-Language: en-US,en;q=0.9,ms;q=0.8",
           "-H","Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
           "-w","\n__HTTPCODE__:%{http_code}\n__FINALURL__:%{url_effective}",
           url]
    if extra_headers:
        for h in extra_headers:
            cmd = cmd[:8] + ["-H", h] + cmd[8:]
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

# ============================================================
# Build prior-titles set from ALL prior cycles (avoid re-fetching)
# ============================================================
def parse_md_titles(md_path):
    out = []
    try:
        with open(md_path, encoding="utf-8") as f:
            txt = f.read()
    except Exception:
        return out
    blocks = re.split(r"\n### ", txt)
    for b in blocks[1:]:
        lines = b.splitlines()
        head = lines[0].strip() if lines else ""
        if not head: continue
        prefix = ""
        m = re.match(r"(\[[^\]]*\])\s*(.*)", head)
        if m:
            prefix = m.group(1)
            title = m.group(2).strip()
        else:
            title = head
        url = ""
        for ln in lines[1:8]:
            if ln.startswith("URL:"): url = ln[4:].strip()
            elif ln.startswith("Source URL:"): url = ln[11:].strip()
            elif ln.startswith("gnews URL:"): url = ln[10:].strip()
        out.append({"title":title,"url":url,"prefix":prefix})
    return out

prior_titles_norm = set()
for ts in PRIOR_TS_LIST:
    for md in glob.glob(os.path.join(BASE, f"*{ts}.md")):
        for a in parse_md_titles(md):
            prior_titles_norm.add(re.sub(r"\s+"," ",a["title"].lower()).strip())
    for pf in glob.glob(os.path.join(BASE, f"priority_*{ts}.md")):
        base = os.path.basename(pf)
        m = re.search(r"_(.*?)_20260719_", base)
        if m: prior_titles_norm.add(m.group(1).lower().replace("-"," "))
print(f"Prior titles set (all {len(PRIOR_TS_LIST)} prior cycles): {len(prior_titles_norm)}")

results = []
gn_intel = []

def strip_html(s):
    return re.sub(r"<[^>]+>","", html.unescape(s or ""))

def extract_article(body_bytes):
    try:
        from bs4 import BeautifulSoup
        soup = BeautifulSoup(body_bytes.decode("utf-8","replace"), "html.parser")
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
    selectors = ["div.elementor-widget-theme-post-content",
                 "div.elementor-widget-container div.elementor-element",
                 "article","div.article-content","div.article-body","div.entry-content",
                 "div.post-content","div.content__body","div.field-body","div.story-body",
                 "div#article-body","div.article","main","div.td-post-content",
                 "div.almbe-article-body","div.posts","section.article","div.content-post",
                 "div.single-content","div.news-detail","div.kcontent","div.body-content",
                 "div.almReadContent","div#content","div.body-text","div.berta-entry-content",
                 "div.post-content-wrapper","div.entry-content","div.article-text"]
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
    return title[:300], "\n\n".join(text_parts[:160])[:28000], (desc or "")[:800], pub

def save_article(pir, slug, url, final, code, body_bytes, note, mode, override_title="", override_pub="", override_desc=""):
    title, body_text, desc, pub = "","","",""
    body_len = 0; ok = False
    if str(code) == "200":
        title, body_text, desc, pub = extract_article(body_bytes)
        if override_title: title = override_title
        if override_pub: pub = override_pub
        if override_desc and not desc: desc = override_desc
        body_len = len(body_text)
        if body_len > 150: ok = True
    fname = f"priority_{pir.lower().replace('+','-')}_{slug}_{TODAY}_{TS_TIME}.md"
    lines = [f"# [PRIORITY {pir}] {slug}",
             f"Source URL: {url}", f"Final/redirected URL: {final}",
             f"Collected: {TODAY} {THIS_TS} UTC ({NOW_ISO}) | MYT: {NOW_MYT}",
             f"Classification: TLP:AMBER", f"HTTP: {code} | mode: {mode}",
             f"Note: {note}", f"Title: {title}"]
    if pub: lines.append(f"ArticlePubDate: {pub}")
    if desc: lines.append(f"Description: {desc}")
    lines += [f"Body chars: {body_len}", "", "## Full text", "="*78,
              (body_text if body_text else "(no body extracted — possibly paywalled or JS-rendered)"),
              "="*78]
    with open(os.path.join(BASE, fname),"w",encoding="utf-8") as f:
        f.write("\n".join(lines))
    print(f"  [{pir}] {slug[:55]:55} | HTTP {code} | {'ok' if ok else 'thin/no-body'} | body={body_len} | {fname}")
    results.append({"pir":pir,"slug":slug,"file":fname,"http":code,"ok":ok,
                    "body_len":body_len,"title":title,"final":final,"pub":pub,"mode":mode})
    return fname

# ============================================================
# NS/PRN relevance regex (broad to catch evening campaign dispatches)
# ============================================================
NS_RE = re.compile(r"(negeri\s*sembilan|negri\s*sembilan|prn|bersatu|perikatan|loke|tok\s*mat|"
                   r"hadi|muhyiddin|aminuddin|zahid|anwar|mca|dap|melaka|linggi|sikamat|ampangan|"
                   r"rantau|nilai|sri\s*tanjung|chennah|chembong|klawang|labu|juasseh|bembang|"
                   r"kerusi|calon|nomination|polls|umb|malay\s*unity|green\s*wave|kuorum|quorum|"
                   r"campaign|ceramah|walkabout|ops\s*centre|manifesto|johari|wee|hang\s*soon|"
                   r"siow|bakri|nor\s*azman|tun\s*faisal|azizul|arul|kumar|fahmi|saarani|"
                   r"penyatuan|jalur|bn\s*pn|pn\s*bn|tampin|jelebu|port\s*dickson|seremban|gemas|"
                   r"jelai|palong|serting|jempol|bahau|repah|paroi|lobak|kubu|ranggal|temiang|"
                   r"pertang|jalaluddin|sawir|danni|adib|ridzuan|tamim|wee\s*ka|sanjeevan|"
                   r"radzi|kiandee|hamzah|supreme\s*council|mpt|ro\s*s|registrar)", re.I)

def classify_pir(title):
    pirs = []
    if re.search(r"(pecat|keluar|buang|tarik\s*diri|muhyiddin|hadi|bersatu|pn|perikatan|merger|new\s*coali|"
                 r"expell|sack|machinery|joint|ceramah|stage|kuorum|quorum|supreme\s*council|"
                 r"understanding|pact|exit|imminent|ro\s*s|registrar|mpt)", title, re.I): pirs.append("PIR-06")
    if re.search(r"(battleground|kerusi\s*tumpuan|marquee|marginal|majority\s*tipis|defector|5\s*corner|"
                 r"tiga\s*penjuru|linggi|sikamat|ampangan|nilai|sri\s*tanjung|chennah|rantau|chembong|"
                 r"klawang|labu|juasseh|bembang|calon|nomination|seat|polls|police|permit|"
                 r"campaign|walkabout|ops\s*centre|manifesto|ceramah|pertang|jalaluddin|sawir)", title, re.I): pirs.append("PIR-07")
    if re.search(r"(narrative|loke|adat|melaka|fled|aminuddin|barking|albert|graft|corruption|"
                 r"majoriti|mb\s*after|sole\s*opposition|malay\s*unity|penyatuan|mca|dap\s*acceptance|"
                 r"green\s*wave|islamophobia|traitor|exit\s*imminent|in\s*disarray|toxic|derhaka|"
                 r"biggest\s*loser|rebuttal|wee\s*ka|hang\s*soon)", title, re.I): pirs.append("PIR-16")
    if not pirs: pirs = ["PIR-07"]
    return "+".join(pirs)

# ============================================================
# PART A: FMT RSS (full text via content:encoded)
# ============================================================
print("\n" + "="*70)
print("=== PART A: FMT RSS fetch ===")
code, body, final = curl("https://www.freemalaysiatoday.com/feed/", timeout=35)
fmt_items = []
if str(code) == "200":
    txt = body.decode("utf-8","replace")
    for m in re.finditer(r"<item>(.*?)</item>", txt, re.S):
        block = m.group(1)
        tm = re.search(r"<title>(?:<!\[CDATA\[)?(.*?)(?:\]\]>)?</title>", block, re.S)
        lm = re.search(r"<link>(.*?)</link>", block, re.S)
        pm = re.search(r"<pubDate>(.*?)</pubDate>", block, re.S)
        cm = re.search(r"<content:encoded>(?:<!\[CDATA\[)?(.*?)(?:\]\]>)?</content:encoded>", block, re.S)
        title = html.unescape(re.sub(r"\s+"," ",tm.group(1))).strip() if tm else ""
        link = lm.group(1).strip() if lm else ""
        pub = pm.group(1).strip() if pm else ""
        content = cm.group(1) if cm else ""
        if title: fmt_items.append({"title":title,"link":link,"pubdate":pub,"content":content})
fmt_ns = [it for it in fmt_items if NS_RE.search(it["title"])]
print(f"FMT RSS: {len(fmt_items)} total | NS-relevant: {len(fmt_ns)}")
fmt_new = [it for it in fmt_ns if re.sub(r"\s+"," ",it["title"].lower()).strip() not in prior_titles_norm]
print(f"FMT NS-relevant & genuinely-new (vs all prior cycles): {len(fmt_new)}")
for it in fmt_new[:40]:
    print(f"  FMT | {it['pubdate'][:25]:25} | {it['title'][:95]}")

for it in fmt_new:
    title = it["title"]; link = it["link"]
    pir = classify_pir(title)
    slug = re.sub(r"[^a-z0-9]+","-",title.lower()).strip("-")[:80]
    if it["content"] and len(it["content"]) > 300:
        body_text = strip_html(it["content"])[:28000]
        body_len = len(body_text)
        ok = body_len > 150
        fname = f"priority_{pir.lower().replace('+','-')}_{slug}_{TODAY}_{TS_TIME}.md"
        lines = [f"# [PRIORITY {pir}] {slug}",
                 f"Source URL: {link}", f"Final/redirected URL: {link}",
                 f"Collected: {TODAY} {THIS_TS} UTC ({NOW_ISO}) | MYT: {NOW_MYT}",
                 f"Classification: TLP:AMBER", f"HTTP: 200 | mode: fmt-rss-content",
                 f"Note: Full text from FMT RSS content:encoded (no curl fetch needed)",
                 f"Title: {title}", f"ArticlePubDate: {it['pubdate']}",
                 f"Body chars: {body_len}", "", "## Full text", "="*78, body_text, "="*78]
        with open(os.path.join(BASE, fname),"w",encoding="utf-8") as f:
            f.write("\n".join(lines))
        print(f"  [{pir}] {slug[:55]:55} | RSS-OK | {'ok' if ok else 'thin'} | body={body_len} | {fname}")
        results.append({"pir":pir,"slug":slug,"file":fname,"http":"200","ok":ok,
                        "body_len":body_len,"title":title,"final":link,"pub":it['pubdate'],"mode":"fmt-rss"})
    else:
        code, body, final = curl(link, timeout=30)
        save_article(pir, slug, link, final, code, body, "FMT direct (RSS content thin)", mode="fmt-direct")

# ============================================================
# PART B: NST WordPress feed (content:encoded)
# ============================================================
print("\n" + "="*70)
print("=== PART B: NST WordPress feed fetch ===")
code, body, final = curl("https://www.nst.com.my/feed", timeout=35)
nst_items = []
if str(code) == "200":
    txt = body.decode("utf-8","replace")
    for m in re.finditer(r"<item>(.*?)</item>", txt, re.S):
        block = m.group(1)
        tm = re.search(r"<title>(?:<!\[CDATA\[)?(.*?)(?:\]\]>)?</title>", block, re.S)
        lm = re.search(r"<link>(.*?)</link>", block, re.S)
        pm = re.search(r"<pubDate>(.*?)</pubDate>", block, re.S)
        cm = re.search(r"<content:encoded>(?:<!\[CDATA\[)?(.*?)(?:\]\]>)?</content:encoded>", block, re.S)
        title = html.unescape(re.sub(r"\s+"," ",tm.group(1))).strip() if tm else ""
        link = lm.group(1).strip() if lm else ""
        pub = pm.group(1).strip() if pm else ""
        content = cm.group(1) if cm else ""
        if title: nst_items.append({"title":title,"link":link,"pubdate":pub,"content":content})
nst_ns = [it for it in nst_items if NS_RE.search(it["title"])]
print(f"NST feed: {len(nst_items)} total | NS-relevant: {len(nst_ns)}")
nst_new = [it for it in nst_ns if re.sub(r"\s+"," ",it["title"].lower()).strip() not in prior_titles_norm]
print(f"NST NS-relevant & genuinely-new: {len(nst_new)}")
for it in nst_new[:30]:
    print(f"  NST | {it['pubdate'][:25]:25} | {it['title'][:95]}")

for it in nst_new:
    title = it["title"]; link = it["link"]
    pir = classify_pir(title)
    slug = re.sub(r"[^a-z0-9]+","-",title.lower()).strip("-")[:80]
    if it["content"] and len(it["content"]) > 300:
        body_text = strip_html(it["content"])[:28000]
        body_len = len(body_text)
        ok = body_len > 150
        fname = f"priority_{pir.lower().replace('+','-')}_{slug}_{TODAY}_{TS_TIME}.md"
        lines = [f"# [PRIORITY {pir}] {slug}",
                 f"Source URL: {link}", f"Final/redirected URL: {link}",
                 f"Collected: {TODAY} {THIS_TS} UTC ({NOW_ISO}) | MYT: {NOW_MYT}",
                 f"Classification: TLP:AMBER", f"HTTP: 200 | mode: nst-feed-content",
                 f"Note: Full text from NST WordPress feed content:encoded",
                 f"Title: {title}", f"ArticlePubDate: {it['pubdate']}",
                 f"Body chars: {body_len}", "", "## Full text", "="*78, body_text, "="*78]
        with open(os.path.join(BASE, fname),"w",encoding="utf-8") as f:
            f.write("\n".join(lines))
        print(f"  [{pir}] {slug[:55]:55} | FEED-OK | {'ok' if ok else 'thin'} | body={body_len} | {fname}")
        results.append({"pir":pir,"slug":slug,"file":fname,"http":"200","ok":ok,
                        "body_len":body_len,"title":title,"final":link,"pub":it['pubdate'],"mode":"nst-feed"})
    else:
        code, body, final = curl(link, timeout=30)
        save_article(pir, slug, link, final, code, body, "NST direct (feed content thin)", mode="nst-direct")

# ============================================================
# PART C: AWANI direct (berita-politik category, paginated)
# ============================================================
print("\n" + "="*70)
print("=== PART C: Awani direct fetch (berita-politik) ===")
AWANI_URLS = [
    "https://www.astroawani.com/berita-politik",
    "https://www.astroawani.com/berita-politik?page=1",
    "https://www.astroawani.com/berita-politik?page=2",
]
awani_links = set()
for au in AWANI_URLS:
    code, body, final = curl(au, timeout=30)
    if str(code) != "200":
        print(f"  Awani {au} HTTP {code}")
        continue
    txt = body.decode("utf-8","replace")
    for m in re.finditer(r'href="(/berita-politik/[^"]+)"', txt):
        awani_links.add(m.group(1))
print(f"Awani berita-politik links found: {len(awani_links)}")
awani_ns_links = [l for l in awani_links if NS_RE.search(l)]
print(f"Awani NS-relevant links: {len(awani_ns_links)}")
for l in sorted(awani_ns_links)[:30]:
    print(f"  AWANI | https://www.astroawani.com{l}")

awani_fetched = 0
for l in sorted(awani_ns_links)[:30]:
    url = "https://www.astroawani.com" + l
    n = re.sub(r"\s+"," ",l.lower()).strip()
    if n in prior_titles_norm: continue
    code, body, final = curl(url, timeout=30)
    slug = re.sub(r"[^a-z0-9]+","-",l.lower()).strip("-")[:80]
    tparts = l.strip("/").split("/")
    title_guess = tparts[2] if len(tparts) > 2 else slug
    save_article("PIR-07", slug, url, final, code, body, "Awani direct berita-politik", mode="awani-direct",
                  override_title=title_guess.replace("-"," ").title())
    awani_fetched += 1
print(f"Awani fresh articles fetched: {awani_fetched}")

# ============================================================
# PART D: mkini direct — try newer article IDs beyond 780110
# ============================================================
print("\n" + "="*70)
print("=== PART D: mkini direct (try newer article IDs 780110-780140) ===")
mkini_fetched = 0
for aid in range(780110, 780141):
    url = f"https://www.malaysiakini.com/news/{aid}"
    code, body, final = curl(url, timeout=20)
    if str(code) == "200":
        title, body_text, desc, pub = extract_article(body)
        if title and NS_RE.search(title + " " + desc):
            slug = re.sub(r"[^a-z0-9]+","-",title.lower()).strip("-")[:80]
            n = re.sub(r"\s+"," ",title.lower()).strip()
            if n in prior_titles_norm: continue
            pir = classify_pir(title)
            save_article(pir, slug, url, final, code, body, f"mkini direct news/{aid}", mode="mkini-direct")
            mkini_fetched += 1
print(f"mkini new NS-relevant articles found: {mkini_fetched}")

# ============================================================
# PART E: Google News universal queries (incl. "kuorum" — PIR-06 NEW requirement)
# ============================================================
print("\n" + "="*70)
print("=== PART E: Google News universal queries ===")
GN_QUERIES = [
    ("kuorum", 'https://news.google.com/rss/search?q=kuorum%20Bersatu%20PN&hl=ms&gl=MY&ceid=MY:ms'),
    ("kuorum-kiandee", 'https://news.google.com/rss/search?q=kuorum%20Kiandee%20Bersatu&hl=ms&gl=MY&ceid=MY:ms'),
    ("prn-ns-bersatu", 'https://news.google.com/rss/search?q=PRN%20Negeri%20Sembilan%20Bersatu&hl=ms&gl=MY&ceid=MY:ms'),
    ("bersatu-exit-pn", 'https://news.google.com/rss/search?q=Bersatu%20keluar%20PN%20pecat&hl=ms&gl=MY&ceid=MY:ms'),
    ("ns-campaign-ceramah", 'https://news.google.com/rss/search?q=Negeri%20Sembilan%20ceramah%20kempen&hl=ms&gl=MY&ceid=MY:ms'),
    ("ns-manifesto", 'https://news.google.com/rss/search?q=Negeri%20Sembilan%20manifesto%20BN&hl=ms&gl=MY&ceid=MY:ms'),
    ("mca-loke-rebuttal", 'https://news.google.com/rss/search?q=MCA%20Loke%20biggest%20loser%20Wee&hl=en&gl=MY&ceid=MY:en'),
    ("pn-supreme-council", 'https://news.google.com/rss/search?q=PN%20Supreme%20Council%20Bersatu%20Negeri%20Sembilan&hl=en&gl=MY&ceid=MY:en'),
    ("jalaluddin-pertang", 'https://news.google.com/rss/search?q=Jalaluddin%20Pertang%20derhaka%20Negeri%20Sembilan&hl=ms&gl=MY&ceid=MY:ms'),
]
for qname, qurl in GN_QUERIES:
    code, body, final = curl(qurl, timeout=25)
    if str(code) != "200":
        print(f"  gnews [{qname}] HTTP {code}")
        continue
    txt = body.decode("utf-8","replace")
    items = re.findall(r"<item>(.*?)</item>", txt, re.S)
    q_new = 0
    for it in items:
        tm = re.search(r"<title>(?:<!\[CDATA\[)?(.*?)(?:\]\]>)?</title>", it, re.S)
        lm = re.search(r"<link>(.*?)</link>", it, re.S)
        pm = re.search(r"<pubDate>(.*?)</pubDate>", it, re.S)
        sm = re.search(r"<source[^>]*url=\"([^\"]+)\"", it)
        title = html.unescape(re.sub(r"\s+"," ",tm.group(1))).strip() if tm else ""
        link = lm.group(1).strip() if lm else ""
        pub = pm.group(1).strip() if pm else ""
        src = sm.group(1) if sm else ""
        pub_name = ""
        mt = re.search(r"\s-\s([^-]+)$", title)
        if mt: pub_name = mt.group(1).strip()
        n = re.sub(r"\s+"," ",title.lower()).strip()
        n_base = re.sub(r"\s-\s[^-]+$","",n).strip()
        if n in prior_titles_norm or n_base in prior_titles_norm: continue
        if not NS_RE.search(title): continue
        q_new += 1
        pir = classify_pir(title)
        slug = re.sub(r"[^a-z0-9]+","-",n_base).strip("-")[:80]
        fname = f"priority_{pir.lower().replace('+','-')}_{slug}_{TODAY}_{TS_TIME}.md"
        lines = [f"# [PRIORITY {pir}] {slug}",
                 f"Source URL: {link}",
                 f"Collected: {TODAY} {THIS_TS} UTC ({NOW_ISO}) | MYT: {NOW_MYT}",
                 f"Classification: TLP:AMBER", f"HTTP: n/a | mode: gnews-headline-intel [{qname}]",
                 f"Note: Headline intelligence from gnews RSS [{qname}]. gnews protobuf URL not curl-resolvable (JS SPA). Publisher: {pub_name or src}.",
                 f"Title: {title}"]
        if pub: lines.append(f"PubDate: {pub}")
        lines += [f"Publisher: {pub_name or src}", "",
                  "## Headline intelligence (no full text — gnews JS-render block)",
                  "="*78, f"TITLE: {title}", f"PUBDATE: {pub}", f"PUBLISHER: {pub_name or src}",
                  f"QUERY: {qname}", "="*78]
        with open(os.path.join(BASE, fname),"w",encoding="utf-8") as f:
            f.write("\n".join(lines))
        gn_intel.append({"pir":pir,"slug":slug,"file":fname,"title":title,"pub":pub,"publisher":pub_name or src,"query":qname})
    print(f"  gnews [{qname}]: {len(items)} items | genuinely-new NS-relevant: {q_new}")

# ============================================================
# PART F: NEW SOURCES — Berita Harian (BH), mStar, Sinar Harian RSS
# ============================================================
print("\n" + "="*70)
print("=== PART F: NEW SOURCES — BH/mStar/Sinar RSS ===")
NEW_FEEDS = [
    ("bh", "https://www.bharian.com.my/feed/rss/category/nasional"),
    ("bh-politik", "https://www.bharian.com.my/feed/rss/category/politik"),
    ("mstar", "https://www.mstar.com.my/feed/rss/category/politik"),
    ("sinar", "https://www.sinarharian.com.my/feed"),
    ("sinar-politik", "https://www.sinarharian.com.my/rss/politik.xml"),
]
for src_name, src_url in NEW_FEEDS:
    code, body, final = curl(src_url, timeout=25)
    if str(code) != "200":
        print(f"  [{src_name}] {src_url} -> HTTP {code}")
        continue
    txt = body.decode("utf-8","replace")
    items = re.findall(r"<item>(.*?)</item>", txt, re.S)
    src_ns = 0; src_new = 0
    for it in items:
        tm = re.search(r"<title>(?:<!\[CDATA\[)?(.*?)(?:\]\]>)?</title>", it, re.S)
        lm = re.search(r"<link>(.*?)</link>", it, re.S)
        pm = re.search(r"<pubDate>(.*?)</pubDate>", it, re.S)
        cm = re.search(r"<content:encoded>(?:<!\[CDATA\[)?(.*?)(?:\]\]>)?</content:encoded>", it, re.S)
        title = html.unescape(re.sub(r"\s+"," ",tm.group(1))).strip() if tm else ""
        link = lm.group(1).strip() if lm else ""
        pub = pm.group(1).strip() if pm else ""
        content = cm.group(1) if cm else ""
        if not title: continue
        if not NS_RE.search(title): continue
        src_ns += 1
        n = re.sub(r"\s+"," ",title.lower()).strip()
        if n in prior_titles_norm: continue
        src_new += 1
        pir = classify_pir(title)
        slug = re.sub(r"[^a-z0-9]+","-",title.lower()).strip("-")[:80]
        if content and len(content) > 300:
            body_text = strip_html(content)[:28000]
            body_len = len(body_text)
            ok = body_len > 150
            fname = f"priority_{pir.lower().replace('+','-')}_{slug}_{TODAY}_{TS_TIME}.md"
            lines = [f"# [PRIORITY {pir}] {slug}",
                     f"Source URL: {link}", f"Final/redirected URL: {link}",
                     f"Collected: {TODAY} {THIS_TS} UTC ({NOW_ISO}) | MYT: {NOW_MYT}",
                     f"Classification: TLP:AMBER", f"HTTP: 200 | mode: {src_name}-rss-content",
                     f"Note: Full text from {src_name} RSS content:encoded",
                     f"Title: {title}", f"ArticlePubDate: {pub}",
                     f"Body chars: {body_len}", "", "## Full text", "="*78, body_text, "="*78]
            with open(os.path.join(BASE, fname),"w",encoding="utf-8") as f:
                f.write("\n".join(lines))
            print(f"  [{pir}] [{src_name}] {slug[:55]:55} | RSS-OK | body={body_len} | {fname}")
            results.append({"pir":pir,"slug":slug,"file":fname,"http":"200","ok":ok,
                            "body_len":body_len,"title":title,"final":link,"pub":pub,"mode":f"{src_name}-rss"})
        else:
            code2, body2, final2 = curl(link, timeout=25)
            save_article(pir, slug, link, final2, code2, body2, f"{src_name} direct (RSS thin)", mode=f"{src_name}-direct")
    print(f"  [{src_name}] {len(items)} items | NS-relevant: {src_ns} | genuinely-new: {src_new}")

# ============================================================
# PART G: NST Kiandee-quorum full-text recovery retry (PIR-06 [CRITICAL] watcher)
# ============================================================
print("\n" + "="*70)
print("=== PART G: NST Kiandee-quorum full-text recovery retry ===")
# Try NST search endpoint with different slugs
NST_SEARCH_URLS = [
    "https://www.nst.com.my/?s=kiandee+quorum",
    "https://www.nst.com.my/?s=Bersatu+Supreme+Council+quorum",
    "https://www.nst.com.my/?s=PN+Supreme+Council+Bersatu",
    "https://www.nst.com.my/?s=Muhyiddin+new+coalition",
]
for su in NST_SEARCH_URLS:
    code, body, final = curl(su, timeout=30)
    if str(code) != "200":
        print(f"  NST search {su} -> HTTP {code}")
        continue
    txt = body.decode("utf-8","replace")
    nst_links = set()
    for m in re.finditer(r'href="(https?://www\.nst\.com\.my/[^"]*(?:kiandee|quorum|bersatu|muhyiddin|supreme)[^"]*)"', txt, re.I):
        nst_links.add(m.group(1))
    print(f"  NST search '{su.split('?=')[-1]}' -> {len(nst_links)} candidate links")
    for u in sorted(nst_links)[:3]:
        n = re.sub(r"\s+"," ",u.lower()).strip()
        if any(k in n for k in ["kiandee","quorum","supreme-council","muhyiddin-new"]):
            slug = re.sub(r"[^a-z0-9]+","-",u.lower()).strip("-")[-80:]
            code2, body2, final2 = curl(u, timeout=30)
            save_article("PIR-06", slug, u, final2, code2, body2,
                         "NST Kiandee-quorum/Supreme-Council full-text recovery", mode="nst-search-recovery")

# ============================================================
# SUMMARY
# ============================================================
print("\n" + "="*70)
print(f"=== CYCLE {THIS_TS} SUMMARY ({NOW_MYT}) ===")
print(f"Prior titles set: {len(prior_titles_norm)}")
print(f"Priority full-text/hard fetches: {len(results)}")
print(f"  Full-text (body>150c): {sum(1 for r in results if r.get('ok'))}")
print(f"  Thin/no-body: {sum(1 for r in results if not r.get('ok'))}")
print(f"gnews headline-intel files: {len(gn_intel)}")
ok_bodies = [r for r in results if r.get("ok")]
total_chars = sum(r.get("body_len",0) for r in ok_bodies)
print(f"Total body chars (full-text): {total_chars}")

# Save results JSON
with open(os.path.join(BASE, f"_priority_fetch_results_{THIS_TS}.json"),"w") as f:
    json.dump({"results":results,"gnews_intel":gn_intel,
               "freshness":{"prior_titles_set":len(prior_titles_norm),
                            "fmt_new":len(fmt_new),"nst_new":len(nst_new)}}, f, indent=2, ensure_ascii=False)
print(f"Saved _priority_fetch_results_{THIS_TS}.json")
print("DONE.")
