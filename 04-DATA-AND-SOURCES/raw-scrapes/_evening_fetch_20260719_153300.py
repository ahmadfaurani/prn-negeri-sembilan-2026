#!/usr/bin/env python3
"""Late-night fetch cycle 20260719_153300 (23:33 MYT 19 Jul 2026).
9th carry-forward of 14:50 Director-approved cycle (mission: 4th carry-forward per brief).
Nomination-Day +1 late-night surge. Campaign Day 1 closing window.
Sources: FMT RSS + NST WP feed + BH WP feed + Utusan WP feed
       + Awani direct berita-politik (URL-path dedup fix maintained)
       + mkini direct 780271-780310
       + NEW source tests: Bernama RSS (bernama.com/rss, rss.bernama.com)
                          + The Rakyat Post (therakyatpost.com/feed)
                          + Sinar Harian (sinarharian.com.my/feed) + mStar (mstar.com.my/feed) retry
       + gnews 18 queries incl. mandatory kuorum + lebih-hebat
         + NEW: "PH manifesto 20 Jul", "BN manifesto 24 Jul", "Anwar response Tok Mat",
                "Nga resign Akmal", "PDM Klawang reopen"
gnews-overwrite-RSS FIX maintained (checks file existence, uses _gnews/_rss suffix).
Cutoff: post-22:28 MYT 19 Jul (post-14:28 UTC). TLP:AMBER. All content carries source URL.
"""
import subprocess, re, datetime, json, os, html, glob
from urllib.parse import urljoin
try:
    from bs4 import BeautifulSoup
    HAVE_BS4 = True
except Exception:
    HAVE_BS4 = False

BASE = "/home/p62operator/.openclaw/workspace-ns/04-DATA-AND-SOURCES/raw-scrapes/20260719"
THIS_TS = "20260719_153300"
PRIOR_TS = "20260719_142800"
TODAY = "20260719"
TS_TIME = "153300"
CUTOFF_UTC = datetime.datetime(2026, 7, 19, 14, 28, 0, tzinfo=datetime.timezone.utc)
CUTOFF_MYT = "22:28"
NOW_ISO = datetime.datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S UTC")
NOW_MYT = (datetime.datetime.utcnow()+datetime.timedelta(hours=8)).strftime("%H:%M MYT %d %b %Y")
UA = ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36")

results = []
fresh_items_log = []

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

def strip_html(s):
    if HAVE_BS4:
        try:
            return BeautifulSoup(s, "html.parser").get_text(" ", strip=True)
        except Exception:
            pass
    s = re.sub(r"<script.*?</script>", " ", s, flags=re.S|re.I)
    s = re.sub(r"<style.*?</style>", " ", s, flags=re.S|re.I)
    s = re.sub(r"<[^>]+>", " ", s)
    return html.unescape(re.sub(r"\s+", " ", s)).strip()

def extract_article(body_bytes):
    txt = body_bytes.decode("utf-8", "replace")
    title = ""; desc = ""; pub = ""
    tm = re.search(r"<title[^>]*>(.*?)</title>", txt, re.S|re.I)
    if tm: title = strip_html(tm.group(1))[:300]
    dm = re.search(r'<meta[^>]+name=["\']description["\'][^>]+content=["\'](.*?)["\']', txt, re.S|re.I)
    if dm: desc = strip_html(dm.group(1))[:800]
    pm = re.search(r'<meta[^>]+property=["\']article:published_time["\'][^>]+content=["\'](.*?)["\']', txt, re.S|re.I)
    if pm: pub = pm.group(1).strip()
    if not pub:
        pm2 = re.search(r'<meta[^>]+name=["\']pubdate["\'][^>]+content=["\'](.*?)["\']', txt, re.S|re.I)
        if pm2: pub = pm2.group(1).strip()
    if not pub:
        pt = re.search(r'<time[^>]+datetime=["\'](.*?)["\']', txt, re.S|re.I)
        if pt: pub = pt.group(1).strip()
    text_parts = []
    if HAVE_BS4:
        soup = BeautifulSoup(txt, "html.parser")
        selectors = ["div.entry-content","div.article-content","div.post-content",
                     "div.elementor-widget-container","article","div.article-body",
                     "div.story-body","div#article-body","main","div.td-post-content",
                     "div.single-content","div.news-detail","div.kcontent",
                     "div.body-content","div.almReadContent","div#content"]
        for sel in selectors:
            nodes = soup.select(sel)
            for node in nodes:
                for p in node.find_all(["p","li","h2","h3","blockquote"]):
                    t = p.get_text(" ", strip=True)
                    if t and len(t) > 25: text_parts.append(t)
                if text_parts: break
            if text_parts: break
    if not text_parts:
        for p in re.finditer(r"<p[^>]*>(.*?)</p>", txt, re.S|re.I):
            t = strip_html(p.group(1))
            if t and len(t) > 40: text_parts.append(t)
    return title[:300], "\n\n".join(text_parts[:160])[:28000], (desc or "")[:800], pub

# Load prior titles baseline (all prior cycles across the day)
prior_titles_norm = set()
for md in glob.glob(os.path.join(BASE, f"*_20260719_*.md")):
    try:
        with open(md, encoding="utf-8") as f:
            txt = f.read()
        for m in re.finditer(r"^Title:\s*(.+)$", txt, re.M):
            prior_titles_norm.add(re.sub(r"\s+"," ",m.group(1).lower()).strip())
        for m in re.finditer(r"^#\s*(?:\[PRIORITY[^\]]*\]\s*)?(.+)$", txt, re.M):
            prior_titles_norm.add(re.sub(r"\s+"," ",m.group(1).lower()).strip())
    except Exception: pass
# Also load prior cycle priority slugs to avoid re-fetching
for pf in glob.glob(os.path.join(BASE, "priority_*_20260719_*.md")):
    base = os.path.basename(pf)
    m = re.search(r"_(.*?)_20260719_", base)
    if m: prior_titles_norm.add(m.group(1).lower().replace("-"," "))

# Build prior Awani URL-path set to maintain the dedup fix
prior_awani_paths = set()
for pf in glob.glob(os.path.join(BASE, "priority_*_20260719_*.md")):
    try:
        with open(pf, encoding="utf-8") as f:
            txt = f.read()
        m = re.search(r"Source URL:\s*(\S+astroawani\S+)", txt)
        if m:
            path = re.sub(r"^https?://[^/]+", "", m.group(1))
            prior_awani_paths.add(path)
    except Exception: pass

NS_RE = re.compile(r"(negeri\s*sembilan|negri\s*sembilan|prn|bersatu|perikatan|loke|tok\s*mat|"
                   r"hadi|muhyiddin|aminuddin|zahid|anwar|mca|dap|melaka|linggi|sikamat|ampangan|"
                   r"rantau|nilai|sri\s*tanjung|chennah|chembong|klawang|labu|juasseh|bembang|"
                   r"kerusi|calon|nomination|polls|umb|malay\s*unity|green\s*wave|kuorum|quorum|"
                   r"campaign|ceramah|walkabout|ops\s*centre|manifesto|johori|wee|hang\s*soon|"
                   r"siow|bakri|nor\s*azman|tun\s*faisal|azizul|arul|kumar|fahmi|saarani|"
                   r"penyatuan|jalur|bn\s*pn|pn\s*bn|tampin|jelebu|port\s*dickson|seremban|gemas|"
                   r"jelai|palong|serting|jempol|bahau|repah|paroi|lobak|kubu|ranggal|temiang|"
                   r"pertang|jalaluddin|sawir|danni|adib|ridzuan|tamim|wee\s*ka|sanjeevan|"
                   r"radzi|kiandee|hamzah|supreme\s*council|mpt|ro\s*s|registrar|lebih\s*hebat|"
                   r"wawasan|pejuang|new\s*coalition|gabungan\s*baharu|annuar|samsuri|faisal|"
                   r"toksik|toxic|bersepadu|joint\s*manifesto|merge\s*machinery|ahmad\s*faez|"
                   r"rakyat\s*orang\s*asli|orang\s*asli|amirudin|johari|on\s*hafiz|letak\s*jawatan|"
                   r"quit\s*cabinet|step\s*down|resign|akmal|nga|amh|gobind|teo\s*nie|cha\s*kee)",
                   re.I)

def classify_pir(title):
    pirs = []
    if re.search(r"(pecat|keluar|buang|tarik\s*diri|muhyiddin|hadi|bersatu|pn|perikatan|merger|new\s*coali|"
                 r"expell|sack|machinery|joint|ceramah|stage|kuorum|quorum|supreme\s*council|"
                 r"understanding|pact|exit|imminent|ro\s*s|registrar|mpt|lebih\s*hebat|wawasan|"
                 r"gabungan\s*baharu|new\s*coalition|toksik|toxic|bersepadu|annuar|samsuri|"
                 r"merge\s*elec|joint\s*manifesto|hamzah|pecat)", title, re.I): pirs.append("PIR-06")
    if re.search(r"(battleground|kerusi\s*tumpuan|marquee|marginal|majority\s*tipis|defector|5\s*corner|"
                 r"tiga\s*penjuru|linggi|sikamat|ampangan|nilai|sri\s*tanjung|chennah|rantau|chembong|"
                 r"klawang|labu|juasseh|bembang|calon|nomination|seat|polls|police|permit|"
                 r"campaign|walkabout|ops\s*centre|manifesto|ceramah|pertang|jalaluddin|sawir|"
                 r"pdm|pusat\s*daerah\s*mengundi|ahmad\s*faez|orang\s*asli|tok\s*mat|letak\s*jawatan|"
                 r"ready\s*to\s*step\s*down|quit\s*cabinet|aminuddin|amirudin|tebok)", title, re.I): pirs.append("PIR-07")
    if re.search(r"(narrative|loke|adat|melaka|fled|aminuddin|barking|albert|graft|corruption|"
                 r"majoriti|mb\s*after|sole\s*opposition|malay\s*unity|penyatuan|mca|dap\s*acceptance|"
                 r"green\s*wave|islamophobia|traitor|exit\s*imminent|in\s*disarray|toxic|derhaka|"
                 r"biggest\s*loser|rebuttal|wee\s*ka|hang\s*soon|kacau\s*daun|sasar\s*bentuk|"
                 r"kerajaan\s*negeri|makmal\s*politik|not\s*briefed|barking\s*dogs|continuity|"
                 r"toksik|toxic|resign|letak\s*jawatan|step\s*down|akmal|nga|amh|gobind|teo\s*nie)",
                 title, re.I): pirs.append("PIR-16")
    if not pirs: pirs = ["PIR-07"]
    return "+".join(pirs)

def is_fresh(pubdate_str):
    """Check if pubdate >= 22:28 MYT 19 Jul 2026 (14:28 UTC). Handle MYT-as-GMT bug."""
    if not pubdate_str: return False
    s = pubdate_str.strip()
    for fmt in ["%a, %d %b %Y %H:%M:%S %Z","%Y-%m-%dT%H:%M:%S%z","%Y-%m-%d %H:%M:%S %Z",
                "%a, %d %b %Y %H:%M:%S %z","%Y-%m-%dT%H:%M:%S"]:
        try:
            dt = datetime.datetime.strptime(s, fmt)
            if dt.tzinfo is None:
                if "GMT" in s or "UTC" in s:
                    dt_utc = dt - datetime.timedelta(hours=8)
                else:
                    dt_utc = dt.replace(tzinfo=datetime.timezone.utc)
            else:
                dt_utc = dt.astimezone(datetime.timezone.utc)
            return dt_utc >= CUTOFF_UTC
        except Exception: continue
    return False

def save_rss_article(pir, slug, title, link, pub, content, source_label):
    body_text = strip_html(content)[:28000] if content else ""
    body_len = len(body_text)
    ok = body_len > 150
    fname = f"priority_{pir.lower().replace('+','-')}_{slug}_{TODAY}_{TS_TIME}.md"
    if os.path.exists(os.path.join(BASE, fname)):
        fname = f"priority_{pir.lower().replace('+','-')}_{slug}_{TODAY}_{TS_TIME}_rss.md"
    lines = [f"# [PRIORITY {pir}] {slug}",
             f"Source URL: {link}", f"Final/redirected URL: {link}",
             f"Collected: {TODAY} {THIS_TS} UTC ({NOW_ISO}) | MYT: {NOW_MYT}",
             f"Classification: TLP:AMBER", f"HTTP: 200 | mode: {source_label}-rss-content",
             f"Note: Full text from {source_label} RSS content:encoded (no curl fetch needed)",
             f"Title: {title}", f"ArticlePubDate: {pub}",
             f"Body chars: {body_len}", "", "## Full text", "="*78,
             (body_text if body_text else "(no body extracted)"), "="*78]
    with open(os.path.join(BASE, fname), "w", encoding="utf-8") as f:
        f.write("\n".join(lines))
    fresh = is_fresh(pub)
    print(f"  [{pir}] {slug[:55]:55} | RSS-OK | fresh={fresh} | body={body_len} | {fname}")
    results.append({"pir":pir,"slug":slug,"file":fname,"http":"200","ok":ok,
                    "body_len":body_len,"title":title,"final":link,"pub":pub,
                    "mode":f"{source_label}-rss","fresh":fresh})
    if fresh:
        fresh_items_log.append({"source":source_label,"title":title,"pub":pub,"url":link,"pir":pir})
    return fname

def save_direct_article(pir, slug, url, final, code, body_bytes, note, mode, override_title="", override_pub=""):
    title, body_text, desc, pub = "","","",""
    body_len = 0; ok = False
    if str(code) == "200":
        title, body_text, desc, pub = extract_article(body_bytes)
        if override_title: title = override_title
        if override_pub: pub = override_pub
        body_len = len(body_text)
        if body_len > 150: ok = True
    fname = f"priority_{pir.lower().replace('+','-')}_{slug}_{TODAY}_{TS_TIME}.md"
    if os.path.exists(os.path.join(BASE, fname)):
        fname = f"priority_{pir.lower().replace('+','-')}_{slug}_{TODAY}_{TS_TIME}_direct.md"
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
    with open(os.path.join(BASE, fname), "w", encoding="utf-8") as f:
        f.write("\n".join(lines))
    print(f"  [{pir}] {slug[:55]:55} | HTTP {code} | {'ok' if ok else 'thin'} | body={body_len} | {fname}")
    results.append({"pir":pir,"slug":slug,"file":fname,"http":code,"ok":ok,
                    "body_len":body_len,"title":title,"final":final,"pub":pub,"mode":mode})
    return fname

def save_gnews_headline(query, title, source, pub, gnews_url):
    pir = classify_pir(title)
    slug = re.sub(r"[^a-z0-9]+","-",title.lower()).strip("-")[:80]
    fname = f"priority_{pir.lower().replace('+','-')}_{slug}_{TODAY}_{TS_TIME}.md"
    if os.path.exists(os.path.join(BASE, fname)):
        fname = f"priority_{pir.lower().replace('+','-')}_{slug}_{TODAY}_{TS_TIME}_gnews.md"
    fresh = is_fresh(pub)
    lines = [f"# [PRIORITY {pir}] {slug}",
             f"gnews query: {query}",
             f"Source (publisher): {source}",
             f"gnews URL: {gnews_url}",
             f"Collected: {TODAY} {THIS_TS} UTC ({NOW_ISO}) | MYT: {NOW_MYT}",
             f"Classification: TLP:AMBER | mode: gnews-headline-intel",
             f"Note: gnews protobuf URL not curl-resolvable (JS SPA); title+pubdate+source captured as headline intelligence",
             f"Title: {title}"]
    if pub: lines.append(f"ArticlePubDate: {pub}")
    lines += [f"Publisher: {source}", f"Fresh (post-{CUTOFF_MYT} MYT): {fresh}", "",
              "## Headline intelligence (full text not curl-recoverable)", "="*78,
              f"Title: {title}", f"Source: {source}", f"PubDate: {pub}", "="*78]
    with open(os.path.join(BASE, fname), "w", encoding="utf-8") as f:
        f.write("\n".join(lines))
    results.append({"pir":pir,"slug":slug,"file":fname,"http":"gnews","ok":False,
                    "body_len":0,"title":title,"final":gnews_url,"pub":pub,
                    "mode":"gnews-headline","source":source,"fresh":fresh})
    if fresh:
        fresh_items_log.append({"source":f"gnews:{source}","title":title,"pub":pub,"url":gnews_url,"pir":pir})

def parse_wp_feed(url, label):
    """Generic WordPress /feed parser used for FMT, NST, BH, Utusan, Sinar, mStar, TRP, Bernama tests."""
    code, body, final = curl(url, timeout=35)
    items = []
    if str(code) != "200":
        print(f"{label}: HTTP {code} (final: {final[:80]})")
        return code, items
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
        if title: items.append({"title":title,"link":link,"pubdate":pub,"content":content})
    return code, items

# ============================================================
# PART A: FMT RSS (full text via content:encoded)
# ============================================================
print("\n" + "="*70)
print("=== PART A: FMT RSS ===")
code, fmt_items = parse_wp_feed("https://www.freemalaysiatoday.com/feed/", "FMT")
fmt_ns = [it for it in fmt_items if NS_RE.search(it["title"])]
fmt_new = [it for it in fmt_ns if re.sub(r"\s+"," ",it["title"].lower()).strip() not in prior_titles_norm]
print(f"FMT RSS: {len(fmt_items)} total | NS-relevant: {len(fmt_ns)} | genuinely-new: {len(fmt_new)}")
for it in fmt_new:
    print(f"  FMT [FRESH={is_fresh(it['pubdate'])}] | {it['pubdate'][:25]:25} | {it['title'][:90]}")
for it in fmt_new:
    title = it["title"]; link = it["link"]
    pir = classify_pir(title)
    slug = re.sub(r"[^a-z0-9]+","-",title.lower()).strip("-")[:80]
    save_rss_article(pir, slug, title, link, it["pubdate"], it["content"], "FMT")

# ============================================================
# PART B: NST WordPress feed (content:encoded)
# ============================================================
print("\n" + "="*70)
print("=== PART B: NST WordPress feed ===")
code, nst_items = parse_wp_feed("https://www.nst.com.my/feed", "NST")
nst_ns = [it for it in nst_items if NS_RE.search(it["title"])]
nst_new = [it for it in nst_ns if re.sub(r"\s+"," ",it["title"].lower()).strip() not in prior_titles_norm]
print(f"NST feed: {len(nst_items)} total | NS-relevant: {len(nst_ns)} | genuinely-new: {len(nst_new)}")
for it in nst_new:
    print(f"  NST [FRESH={is_fresh(it['pubdate'])}] | {it['pubdate'][:25]:25} | {it['title'][:90]}")
for it in nst_new:
    title = it["title"]; link = it["link"]
    pir = classify_pir(title)
    slug = re.sub(r"[^a-z0-9]+","-",title.lower()).strip("-")[:80]
    save_rss_article(pir, slug, title, link, it["pubdate"], it["content"], "NST")

# ============================================================
# PART C: BH (Berita Harian) WordPress feed (content:encoded)
# ============================================================
print("\n" + "="*70)
print("=== PART C: BH WordPress feed ===")
code, bh_items = parse_wp_feed("https://bharian.com.my/feed", "BH")
bh_ns = [it for it in bh_items if NS_RE.search(it["title"])]
bh_new = [it for it in bh_ns if re.sub(r"\s+"," ",it["title"].lower()).strip() not in prior_titles_norm]
print(f"BH feed: {len(bh_items)} total | NS-relevant: {len(bh_ns)} | genuinely-new: {len(bh_new)}")
for it in bh_new:
    print(f"  BH [FRESH={is_fresh(it['pubdate'])}] | {it['pubdate'][:25]:25} | {it['title'][:90]}")
for it in bh_new:
    title = it["title"]; link = it["link"]
    pir = classify_pir(title)
    slug = re.sub(r"[^a-z0-9]+","-",title.lower()).strip("-")[:80]
    save_rss_article(pir, slug, title, link, it["pubdate"], it["content"], "BH")

# ============================================================
# PART C2: Utusan WordPress feed
# ============================================================
print("\n" + "="*70)
print("=== PART C2: Utusan WordPress feed ===")
code, ut_items = parse_wp_feed("https://www.utusan.com.my/feed", "UTUSAN")
ut_ns = [it for it in ut_items if NS_RE.search(it["title"])]
ut_new = [it for it in ut_ns if re.sub(r"\s+"," ",it["title"].lower()).strip() not in prior_titles_norm]
print(f"Utusan feed: {len(ut_items)} total | NS-relevant: {len(ut_ns)} | genuinely-new: {len(ut_new)}")
for it in ut_new:
    print(f"  UTUSAN [FRESH={is_fresh(it['pubdate'])}] | {it['pubdate'][:25]:25} | {it['title'][:90]}")
for it in ut_new:
    title = it["title"]; link = it["link"]
    pir = classify_pir(title)
    slug = re.sub(r"[^a-z0-9]+","-",title.lower()).strip("-")[:80]
    save_rss_article(pir, slug, title, link, it["pubdate"], it["content"], "UTUSAN")

# ============================================================
# PART C3: NEW source tests — Sinar Harian, mStar, The Rakyat Post, Bernama
# ============================================================
print("\n" + "="*70)
print("=== PART C3: NEW source tests (Sinar/mStar/TRP/Bernama) ===")
NEW_FEED_TESTS = [
    ("SINAR", "https://sinarharian.com.my/feed"),
    ("MSTAR", "https://www.mstar.com.my/feed"),
    ("TRP",   "https://therakyatpost.com/feed"),
    ("BERNAMA1", "https://www.bernama.com/rss"),
    ("BERNAMA2", "https://rss.bernama.com"),
    ("BERNAMA3", "https://www.bernama.com/feed"),
]
for label, url in NEW_FEED_TESTS:
    code, items = parse_wp_feed(url, label)
    ns_hits = [it for it in items if NS_RE.search(it["title"])]
    new_hits = [it for it in ns_hits if re.sub(r"\s+"," ",it["title"].lower()).strip() not in prior_titles_norm]
    print(f"  {label}: HTTP {code} | {len(items)} items | NS-relevant: {len(ns_hits)} | genuinely-new: {len(new_hits)}")
    for it in new_hits:
        title = it["title"]; link = it["link"]
        pir = classify_pir(title)
        slug = re.sub(r"[^a-z0-9]+","-",title.lower()).strip("-")[:80]
        save_rss_article(pir, slug, title, link, it["pubdate"], it["content"], label)

# ============================================================
# PART D: Awani direct berita-politik (with URL-path dedup fix)
# ============================================================
print("\n" + "="*70)
print("=== PART D: Awani direct berita-politik ===")
awani_new = []
for page in [1, 2]:
    url = f"https://www.astroawani.com/berita-politik?page={page}"
    code, body, final = curl(url, timeout=30)
    if str(code) != "200": continue
    txt = body.decode("utf-8","replace")
    for m in re.finditer(r'href="(/berita-politik/[^"#?]+)"', txt):
        path = m.group(1)
        if path in prior_awani_paths: continue
        ctx_start = max(0, m.start()-200)
        ctx_end = min(len(txt), m.end()+400)
        ctx = txt[ctx_start:ctx_end]
        tm = re.search(r'title="([^"]+)"', ctx)
        if not tm:
            tm = re.search(r'>([^<]{15,120})</a>', ctx)
        title = strip_html(tm.group(1)).strip() if tm else path.split("/")[-1].replace("-"," ")
        if NS_RE.search(title) or "prn" in path.lower() or "negeri-sembilan" in path.lower() or "n9" in path.lower():
            awani_new.append((path, title))

seen_paths = set()
awani_unique = []
for path, title in awani_new:
    if path not in seen_paths:
        seen_paths.add(path)
        awani_unique.append((path, title))
print(f"Awani: {len(awani_unique)} genuinely-new berita-politik links (URL-path dedup fix applied)")
for path, title in awani_unique[:25]:
    print(f"  Awani | {title[:90]} | {path}")
for path, title in awani_unique:
    url = f"https://www.astroawani.com{path}"
    pir = classify_pir(title)
    slug = path.split("/")[-1][:80]
    code, body, final = curl(url, timeout=30)
    save_direct_article(pir, slug, url, final, code, body,
                       f"Awani direct fetch (URL-path dedup fix; not in prior Awani paths)",
                       mode="awani-direct")

# ============================================================
# PART E: mkini direct 780271-780310
# ============================================================
print("\n" + "="*70)
print("=== PART E: mkini direct 780271-780310 ===")
mkini_count = 0
for nid in range(780271, 780311):
    url = f"https://www.malaysiakini.com/news/{nid}"
    code, body, final = curl(url, timeout=20)
    if str(code) != "200": continue
    txt = body.decode("utf-8","replace")
    tm = re.search(r"<title[^>]*>(.*?)</title>", txt, re.S|re.I)
    title = strip_html(tm.group(1)).strip() if tm else ""
    if not title: continue
    if not NS_RE.search(title): continue
    if re.sub(r"\s+"," ",title.lower()).strip() in prior_titles_norm: continue
    slug = re.sub(r"[^a-z0-9]+","-",title.lower()).strip("-")[:80]
    pir = classify_pir(title)
    save_direct_article(pir, slug, url, final, code, body,
                       f"mkini direct news/{nid}", mode="mkini-direct")
    mkini_count += 1
print(f"mkini: {mkini_count} genuinely-new NS-relevant articles in 780271-780310")

# ============================================================
# PART F: gnews queries (headline intelligence)
# ============================================================
print("\n" + "="*70)
print("=== PART F: gnews queries (headline intelligence) ===")
GNEWS_QUERIES = [
    # Mandatory PIR-06
    "kuorum", "lebih hebat", "bersatu exit pn", "sasar kerajaan negeri",
    "pdm klawang", "pn supreme council", "merge machinery BN PN",
    "joint manifesto BN PN",
    # PIR-07
    "jalaluddin pertang", "tok mat letak jawatan",
    # PIR-16
    "mca loke rebuttal", "bersatu kacau daun", "makmal politik",
    # Prior-cycle carries
    "anwar tok mat resign", "AMH BN resign", "manifesto PH Negeri Sembilan",
    # NEW this cycle (20 Jul manifesto / Anwar response / PDM reopen watch)
    "PH manifesto 20 Jul", "BN manifesto 24 Jul", "Anwar response Tok Mat",
    "Nga resign Akmal", "PDM Klawang reopen",
]
for query in GNEWS_QUERIES:
    q_enc = query.replace(" ", "+")
    gnews_url = f"https://news.google.com/rss/search?q={q_enc}+when:3d&hl=en-MY&gl=MY&ceid=MY:en"
    code, body, final = curl(gnews_url, timeout=25)
    if str(code) != "200":
        print(f"  gnews [{query}]: HTTP {code}")
        continue
    txt = body.decode("utf-8","replace")
    items_count = 0
    for m in re.finditer(r"<item>(.*?)</item>", txt, re.S):
        block = m.group(1)
        tm = re.search(r"<title>(.*?)</title>", block, re.S)
        sm = re.search(r"<source[^>]*>(.*?)</source>", block, re.S)
        pm = re.search(r"<pubDate>(.*?)</pubDate>", block, re.S)
        if not tm: continue
        title = html.unescape(tm.group(1)).strip()
        title = re.sub(r"\s*-\s*[^-]+$", "", title).strip()
        source = sm.group(1).strip() if sm else "unknown"
        pub = pm.group(1).strip() if pm else ""
        if not NS_RE.search(title): continue
        if re.sub(r"\s+"," ",title.lower()).strip() in prior_titles_norm: continue
        save_gnews_headline(query, title, source, pub, gnews_url)
        items_count += 1
    print(f"  gnews [{query}]: {items_count} NS-relevant new items")

# ============================================================
# PART G: Save results JSON
# ============================================================
print("\n" + "="*70)
print("=== Save results JSON ===")
with open(os.path.join(BASE, f"_priority_fetch_results_{TODAY}_{TS_TIME}.json"), "w", encoding="utf-8") as f:
    json.dump({"cycle":THIS_TS, "cutoff_myt":CUTOFF_MYT, "now_iso":NOW_ISO, "results":results,
               "fresh_items":fresh_items_log, "results_count":len(results),
               "fresh_count":len(fresh_items_log)}, f, indent=2, ensure_ascii=False, default=str)
print(f"Total files: {len(results)} | Fresh post-{CUTOFF_MYT} MYT: {len(fresh_items_log)}")
print(f"Saved: _priority_fetch_results_{TODAY}_{TS_TIME}.json")
print("\n=== Fresh items log ===")
for fi in fresh_items_log:
    print(f"  [FRESH] [{fi['pir']}] {fi['source']} | {fi['pub'][:25]} | {fi['title'][:90]}")
print("\nDONE")
