#!/usr/bin/env python3
"""PRN Negeri Sembilan 2026 — News Collection Agent
Cycle: 20260719 (UTC) / Day-2 daytime MYT 19 Jul 2026
Nomination-Day Surge Mode — Director priority-approved PIR-06/09/07.

Multi-strategy scraper:
  1. wp-rest-api  : utusan, kosmo, ohbulan
  2. html-extract : malaysiakini(home), astroawani(home), thestar(/news/nation),
                    themalaysianinsight(home), mstar(home), kosmo(home), utusan(/nasional)
  3. gnews-rss-per-source : nst, bharian, mstar, thestar, astroawani, malaysiakini
  4. gnews-rss-universal  : 3 feeds (prn+bersatu, pn+pecat+keluar, nomination)

Outputs per-source .md files (with [PRIORITY] prefix on PIR-matching titles),
universal gnews .md files, _scrape_results_TS.json, and a CRITICAL PIR-06 scan.
Then runs a priority full-text fetcher for genuinely-new high-value articles.

TLP:AMBER. All content carries source URL.
"""
import subprocess, re, json, os, sys, datetime, html, time
from bs4 import BeautifulSoup
from urllib.parse import urljoin

# -------------------------------------------------------------------- config
BASE = "/home/p62operator/.openclaw/workspace-ns/04-DATA-AND-SOURCES/raw-scrapes/20260719"
os.makedirs(BASE, exist_ok=True)
NOW = datetime.datetime.utcnow()
TODAY = NOW.strftime("%Y%m%d")
TS = NOW.strftime("%Y%m%d_%H%M%S")
TS_TIME = NOW.strftime("%H%M%S")  # for filenames (prior convention: key_DATE_HHMMSS.md)
NOW_ISO = NOW.strftime("%Y-%m-%d %H:%M:%S UTC")
# MYT = UTC+8
NOW_MYT = (NOW + datetime.timedelta(hours=8))
NOW_MYT_STR = NOW_MYT.strftime("%H:%M MYT %d %b %Y")
NOW_MYT_ISO = NOW_MYT.strftime("%Y-%m-%dT%H:%M")
print(f"=== CYCLE {TS} | {NOW_ISO} | {NOW_MYT_STR} ===")

UA = ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36")

# ---- PIR keyword sets (case-insensitive substring OR regex) ----
PRN_KW = re.compile(r"(negeri\s*sembilan|n\s*sembilan|n9\s*poll|ns\s*poll|prn\s*ns|prn\s*negeri|"
                    r"rembau|rantau|jempol|seremban|port\s*dickson|linggi|sikamat|ampangan|"
                    r"paroi|labu|dut\b|lenggeng|jelebu|kerusi\s*dun|dun\s*n\.?sembilan|"
                    r"negri\s*sembilan|n\s*9\b)", re.I)

PIR06_KW = re.compile(r"(pecat|termination|remove|keluar|withdraw|tarik\s*diri|"
                      r"majlis\s*tertinggi|asas\s*kukuh|muhyiddin|samsuri|hadi\s*awang|"
                      r"kiandee|hamzah\s*zainudin|bersatu|goodbye\s*pn|buang\s*bersatu|"
                      r"expell?ed|expulsion|sack|exit\s*pn|part\s*ways|true\s*opposition|"
                      r"new\s*coali(tion|bloc)|new\s*bloc|crossroad|merger|pembangkang\s*tunggal|"
                      r"tidak\s*lagi\s*mahu\s*bersama|ronald|annuar\s*ariffin)", re.I)

PIR09_KW = re.compile(r"(pecat|disiplin|lompat|pengkhianat|defector|hopper|kredibiliti|"
                      r"eligibility|bankrup|kes\s*mahkamah|independent\s*candidate|calon\s*bebas|"
                      r"tamim|gerakan|tang\s*jay\s*son|wee\s*ka\s*siong|mca|rafie|nazri\s*kassim|"
                      r"noor.azah|saw\s*yee\s*fung|chong\s*sin\s*woon|credibility|disciplinary|"
                      r"three\s*cornered|tiga\s*penjuru|albert\s*barking|saravanan)", re.I)

PIR07_KW = re.compile(r"(kerusi\s*tumpuan|battleground|pertembungan|marquee|pinggir|"
                      r"manifesto|kempen|operasi|pusat\s*penamaan|nomination|calon|"
                      r"kerusi\s*panas|panas\s*jadi\s*tumpuan|seat|elect|poll|prn|"
                      r"aminuddin|tok\s*mat|loke|zahid|anwar|hadi|asyraf\s*wajdi|"
                      r"5\s*hot\s*seats|tiga\s*gabungan|gabungan\s*bertembung|103\s*calon|"
                      r"36\s*kerusi|36-seat|36\s*seat)", re.I)

# CRITICAL PIR-06 formal-removal-notice patterns (must be MT/PN-issued, not a call)
CRIT_PIR06 = re.compile(
    r"(majlis\s*tertinggi\s*(pn|perikatan\s*nasional)\s*(keluarkan|pecat|buang|remove|"
    r"sack|expell?)\s*bersatu"
    r"|pn\s*(secara\s*rasmi\s*)?(keluarkan|pecat|buang|remove|sack|expell?)\s*bersatu"
    r"|bersatu\s*dikeluarkan\s*daripada\s*pn"
    r"|bersatu\s*(removed|expelled|sacked)\s*from\s*pn"
    r"|removal\s*notice|formal\s*removal"
    r"|perikatan\s*nasional\s*(keluarkan|pecat|buang)\s*bersatu)", re.I)
# Precursor (call for removal, not yet a notice)
PREC_PIR06 = re.compile(r"(asas\s*kukuh|kiandee|mengeluarkan\s*bersatu|keluarkan\s*bersatu|"
                        r"remove\s*bersatu\s*from\s*pn|pecat\s*bersatu)", re.I)

# -------------------------------------------------------------------- helpers
def curl(url, timeout=35, raw=False):
    cmd = ["curl","-sS","-L","-m",str(timeout),"-A",UA,"--compressed",
           "-H","Accept-Language: en-US,en;q=0.9,ms;q=0.8",
           "-H","Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
           "-w","\n__HTTPCODE__:%{http_code}\n__FINALURL__:%{url_effective}\n__TIME__:%{time_total}",
           url]
    try:
        p = subprocess.run(cmd, capture_output=True, timeout=timeout+15)
    except subprocess.TimeoutExpired:
        return "TIMEOUT", b"", url, 0.0
    out = p.stdout
    m = re.search(rb"__HTTPCODE__:(\d+)", out)
    code = m.group(1).decode() if m else "ERR"
    mu = re.search(rb"__FINALURL__:(\S+)", out)
    final = mu.group(1).decode("utf-8","replace").strip() if mu else url
    mt = re.search(rb"__TIME__:([\d.]+)", out)
    elapsed = float(mt.group(1)) if mt else 0.0
    body = out[:m.start()] if m else out
    return code, body, final, elapsed

def clean(t):
    if t is None: return ""
    t = html.unescape(str(t))
    t = re.sub(r"\s+", " ", t).strip()
    return t

def tag_pir(title):
    """Return (pirs_list, is_prn, priority_flag). pirs = list of PIR-XX matched."""
    t = clean(title)
    pirs = []
    is_prn = bool(PRN_KW.search(t))
    if PIR06_KW.search(t): pirs.append("PIR-06")
    if PIR09_KW.search(t): pirs.append("PIR-09")
    if PIR07_KW.search(t): pirs.append("PIR-07")
    # PIR-07 also triggers if explicitly PRN-context + any campaign term
    if is_prn and not pirs and re.search(r"(calon|kempen|kerusi|seat|poll|nomination|prn)", t, re.I):
        pirs.append("PIR-07")
    return pirs, is_prn, bool(pirs)

# -------------------------------------------------------------------- source defs
# Each source: key, label, strategy, url, optional section
SOURCES = [
    # ---- WordPress REST API ----
    {"key":"utusancommy","label":"Utusan Malaysia","strategy":"wpapi",
     "url":"https://www.utusan.com.my/wp-json/wp/v2/posts?per_page=60&_embed=0"},
    {"key":"kosmocommy","label":"Kosmo","strategy":"wpapi",
     "url":"https://www.kosmo.com.my/wp-json/wp/v2/posts?per_page=60&_embed=0"},
    {"key":"ohbulancom","label":"OhBulan","strategy":"wpapi",
     "url":"https://www.ohbulan.com/wp-json/wp/v2/posts?per_page=60&_embed=0"},
    # ---- HTML extraction ----
    {"key":"malaysiakinicom","label":"Malaysiakini","strategy":"html",
     "url":"https://www.malaysiakini.com"},
    {"key":"astroawanicom","label":"Astro Awani","strategy":"html",
     "url":"https://www.astroawani.com"},
    {"key":"thestarcommy","label":"The Star","strategy":"html",
     "url":"https://www.thestar.com.my/news/nation"},
    {"key":"thmalaysianinsightcom","label":"The Malaysian Insight","strategy":"html",
     "url":"https://www.themalaysianinsight.com"},
    {"key":"mstarcommy","label":"mStar","strategy":"html",
     "url":"https://www.mstar.com.my"},
    {"key":"kosmocommy_html","label":"Kosmo (homepage)","strategy":"html",
     "url":"https://www.kosmo.com.my"},
    {"key":"utusancommy_html","label":"Utusan (nasional section)","strategy":"html",
     "url":"https://www.utusan.com.my/nasional/"},
    # ---- Google News RSS per-source ----
    {"key":"nstcommy","label":"New Straits Times (via Google News)","strategy":"gnews",
     "url":"https://news.google.com/rss/search?q=site:nst.com.my+Negeri+Sembilan&hl=en-MY&gl=MY&ceid=MY:en"},
    {"key":"bhariancommy","label":"BHarian (via Google News)","strategy":"gnews",
     "url":"https://news.google.com/rss/search?q=site:bharian.com.my+Negeri+Sembilan&hl=en-MY&gl=MY&ceid=MY:en"},
    {"key":"mstarcommy_gn","label":"mStar (via Google News)","strategy":"gnews",
     "url":"https://news.google.com/rss/search?q=site:mstar.com.my+Negeri+Sembilan&hl=en-MY&gl=MY&ceid=MY:en"},
    {"key":"thestarcommy_gn","label":"The Star (via Google News)","strategy":"gnews",
     "url":"https://news.google.com/rss/search?q=site:thestar.com.my+Negeri+Sembilan&hl=en-MY&gl=MY&ceid=MY:en"},
    {"key":"astroawanicom_gn","label":"Astro Awani (via Google News)","strategy":"gnews",
     "url":"https://news.google.com/rss/search?q=site:astroawani.com+Negeri+Sembilan&hl=en-MY&gl=MY&ceid=MY:en"},
    {"key":"malaysiakinicom_gn","label":"Malaysiakini (via Google News)","strategy":"gnews",
     "url":"https://news.google.com/rss/search?q=site:malaysiakini.com+Negeri+Sembilan&hl=en-MY&gl=MY&ceid=MY:en"},
]

UNIVERSAL_GNEWS = [
    {"ukey":"universalprnbersatu","label":"Google News universal: PRN Negeri Sembilan + Bersatu",
     "url":"https://news.google.com/rss/search?q=(%22PRN+Negeri+Sembilan%22+OR+%22Negeri+Sembilan+polls%22)+AND+bersatu&hl=en-MY&gl=MY&ceid=MY:en"},
    {"ukey":"universalpnpecat","label":"Google News universal: PN + (pecat OR keluar OR buang) + Bersatu",
     "url":"https://news.google.com/rss/search?q=(PN+OR+%22Perikatan+Nasional%22)+AND+(pecat+OR+keluar+OR+buang+OR+remove+OR+expel)+AND+bersatu&hl=en-MY&gl=MY&ceid=MY:en"},
    {"ukey":"universalnomination","label":"Google News universal: nomination day Negeri Sembilan",
     "url":"https://news.google.com/rss/search?q=(%22nomination+day%22+OR+%22penamaan+calon%22)+AND+%22Negeri+Sembilan%22&hl=en-MY&gl=MY&ceid=MY:en"},
]

# -------------------------------------------------------------------- extractors
def extract_wpapi(body):
    """WordPress REST: list of {title.rendered, link, date_gmt, excerpt.rendered}"""
    try:
        data = json.loads(body.decode("utf-8","replace"))
    except Exception:
        return []
    out = []
    if isinstance(data, list):
        for p in data:
            if not isinstance(p, dict): continue
            title = clean(p.get("title",{}).get("rendered",""))
            link = p.get("link","")
            date_gmt = p.get("date_gmt","") or p.get("date","")
            excerpt = clean(p.get("excerpt",{}).get("rendered",""))
            if title:
                out.append({"title":title,"link":link,"date_gmt":date_gmt,"excerpt":excerpt[:300]})
    return out

def extract_html_generic(body, base_url):
    """Parse homepage/section HTML; collect candidate article titles + links."""
    try:
        soup = BeautifulSoup(body.decode("utf-8","replace"), "html.parser")
    except Exception:
        return []
    out = []
    seen = set()
    # strategy: find <a> tags whose visible text looks like an article headline
    for a in soup.find_all("a", href=True):
        href = a.get("href","")
        if not href or href.startswith("#") or href.startswith("javascript:"): continue
        # skip nav/social/section boilerplate
        if re.search(r"(facebook\.com|twitter\.com|x\.com|instagram|youtube|whatsapp|mailto:|tel:|/#|"
                     r"/tag/|/category/|/author/|/page/|/about|/contact|/subscribe|/login|/search)",
                     href, re.I): continue
        # text from this anchor OR its nearest heading/img-alt
        txt = clean(a.get_text(" "))
        if not txt:
            # try img alt
            img = a.find("img")
            if img and img.get("alt"):
                txt = clean(img["alt"])
        if len(txt) < 25: continue
        # filter obvious nav/copyright
        if re.match(r"^(home|about|contact|subscribe|log\s*in|sign\s*in|menu|search|"
                    r"next|previous|read more|load more|view all|see all|all rights reserved|"
                    r"privacy|terms|advertise|copyright)\b", txt, re.I): continue
        full = urljoin(base_url, href)
        key = (txt.lower(), full)
        if key in seen: continue
        seen.add(key)
        out.append({"title":txt,"link":full,"date_gmt":"","excerpt":""})
    # de-dup by title (keep first link)
    ded = {}
    for a in out:
        k = a["title"].lower()
        if k not in ded:
            ded[k] = a
    return list(ded.values())[:120]

def extract_gnews(body):
    """Google News RSS: list of {title, link(gnews), pubDate, source}"""
    try:
        # html.parser (not "xml" — lxml not installed; prior cycles used html.parser successfully)
        soup = BeautifulSoup(body.decode("utf-8","replace"), "html.parser")
    except Exception:
        return []
    out = []
    for item in soup.find_all("item"):
        title = clean(item.title.get_text() if item.title else "")
        link = ""
        for L in item.find_all("link"):
            link = L.get_text() or L.string or ""
            if link: break
        pub = ""
        if item.pubDate: pub = clean(item.pubDate.get_text())
        src = ""
        se = item.find("source")
        if se: src = clean(se.get_text())
        if title:
            out.append({"title":title,"link":link,"date_gmt":pub,"excerpt":"","source":src})
    return out

# -------------------------------------------------------------------- main scrape
results = {"timestamp":TS, "collected_utc":NOW_ISO, "collected_myt":NOW_MYT_STR,
           "pir06_critical_alert":{"formal_removal_notice_detected":False,
                                   "critical_evidence":[],
                                   "precursor_items_count":0,
                                   "precursor_items_sample":[]},
           "sources":[]}

all_titles_for_crit_scan = []   # (title, source, link, pubdate)

for s in SOURCES:
    key, label, strat, url = s["key"], s["label"], s["strategy"], s["url"]
    print(f"[{strat:6}] {key:24} -> {url[:70]}")
    code, body, final, elapsed = curl(url)
    if code != "200":
        print(f"    !! HTTP {code} (elapsed {elapsed:.1f}s)")
        results["sources"].append({"source":key,"label":label,"url":url,"strategy":strat,
                                   "http_code":code,"article_count":0,
                                   "priority_article_count":0,"prn_article_count":0,
                                   "pir06_hits":0,"pir09_hits":0,"pir07_hits":0,
                                   "file":f"{key}_{TODAY}_{TS}.md",
                                   "priority_titles":[],"error":f"http_{code}"})
        continue
    if strat == "wpapi":
        arts = extract_wpapi(body)
    elif strat == "gnews":
        arts = extract_gnews(body)
    else:  # html
        arts = extract_html_generic(body, url)

    # tag + assemble md
    lines = []
    lines.append(f"# {label} — raw scrape")
    lines.append(f"Source URL: {url}")
    lines.append(f"Final/redirected URL: {final}")
    lines.append(f"Collected: {TODAY} {TS} UTC ({NOW_ISO}) | MYT: {NOW_MYT_STR}")
    lines.append(f"Classification: TLP:AMBER")
    lines.append(f"Strategy: {strat} | HTTP: {code} | articles_extracted: {len(arts)} | fetch_time: {elapsed:.2f}s")
    lines.append("")
    lines.append("## Articles (priority-tagged: [PRIORITY PIR-XX] for PIR-06/09/07 keyword matches)")
    lines.append("="*78)

    prn_count = 0; pri_count = 0
    p06=0; p09=0; p07=0
    pri_titles = []
    for a in arts:
        title = a["title"]
        pirs, is_prn, is_pri = tag_pir(title)
        if is_prn: prn_count += 1
        if is_pri:
            pri_count += 1
            pri_titles.append(title)
            for p in pirs:
                if p=="PIR-06": p06+=1
                if p=="PIR-09": p09+=1
                if p=="PIR-07": p07+=1
            prefix = "[PRIORITY " + "+".join(pirs) + "] "
        else:
            prefix = ""
        lines.append("")
        lines.append(f"### {prefix}{title}")
        if a.get("link"): lines.append(f"URL: {a['link']}")
        if a.get("date_gmt"): lines.append(f"PubDate: {a['date_gmt']}")
        if a.get("source"): lines.append(f"Publisher: {a['source']}")
        if a.get("excerpt"): lines.append(f"Excerpt: {a['excerpt']}")
        all_titles_for_crit_scan.append((title, label, a.get("link",""), a.get("date_gmt","")))
    lines.append("")
    lines.append("="*78)
    lines.append(f"END — {len(arts)} articles, {pri_count} priority-tagged, {prn_count} PRN-NS-relevant")

    fname = f"{key}_{TODAY}_{TS_TIME}.md"
    with open(os.path.join(BASE, fname),"w",encoding="utf-8") as f:
        f.write("\n".join(lines))
    print(f"    ok HTTP {code} | arts={len(arts):3d} pri={pri_count:2d} prn={prn_count:2d} "
          f"P06={p06} P09={p09} P07={p07} | {fname} ({elapsed:.1f}s)")
    results["sources"].append({"source":key,"label":label,"url":url,"strategy":strat,
                               "http_code":code,"article_count":len(arts),
                               "priority_article_count":pri_count,
                               "prn_article_count":prn_count,
                               "pir06_hits":p06,"pir09_hits":p09,"pir07_hits":p07,
                               "file":fname,"priority_titles":pri_titles})

# ---- universal Google News feeds ----
gn_files = []
for u in UNIVERSAL_GNEWS:
    ukey, label, url = u["ukey"], u["label"], u["url"]
    print(f"[gn-univ] {ukey:22} -> {url[:70]}")
    code, body, final, elapsed = curl(url)
    if code != "200":
        print(f"    !! HTTP {code}")
        gn_files.append({"ukey":ukey,"http_code":code,"article_count":0})
        continue
    arts = extract_gnews(body)
    lines = []
    lines.append(f"# {label} — universal Google News RSS")
    lines.append(f"Feed URL: {url}")
    lines.append(f"Collected: {TODAY} {TS} UTC ({NOW_ISO}) | MYT: {NOW_MYT_STR}")
    lines.append(f"Classification: TLP:AMBER")
    lines.append(f"HTTP: {code} | items: {len(arts)}")
    lines.append("")
    lines.append("## Items")
    lines.append("="*78)
    p06=p09=p07=0
    for a in arts:
        title = a["title"]
        pirs, is_prn, is_pri = tag_pir(title)
        prefix = "[PRIORITY " + "+".join(pirs) + "] " if is_pri else ""
        for p in pirs:
            if p=="PIR-06": p06+=1
            if p=="PIR-09": p09+=1
            if p=="PIR-07": p07+=1
        lines.append("")
        lines.append(f"### {prefix}{title}")
        if a.get("source"): lines.append(f"Publisher: {a['source']}")
        if a.get("link"): lines.append(f"gnews URL: {a['link']}")
        if a.get("date_gmt"): lines.append(f"PubDate: {a['date_gmt']}")
        all_titles_for_crit_scan.append((title, label, a.get("link",""), a.get("date_gmt","")))
    lines.append("")
    lines.append("="*78)
    lines.append(f"END — {len(arts)} items | P06={p06} P09={p09} P07={p07}")
    fname = f"google_news_{ukey}_html_{TODAY}_{TS_TIME}.md"
    with open(os.path.join(BASE, fname),"w",encoding="utf-8") as f:
        f.write("\n".join(lines))
    print(f"    ok HTTP {code} | items={len(arts):3d} P06={p06} P09={p09} P07={p07} | {fname}")
    gn_files.append({"ukey":ukey,"http_code":code,"article_count":len(arts),
                     "pir06_hits":p06,"pir09_hits":p09,"pir07_hits":p07,"file":fname})

# ---- CRITICAL PIR-06 scan across all collected titles ----
crit_hits = []
precursor_hits = []
for title, label, link, pub in all_titles_for_crit_scan:
    if CRIT_PIR06.search(title):
        crit_hits.append({"title":title,"source":label,"url":link,"pubdate":pub})
    if PREC_PIR06.search(title):
        precursor_hits.append({"title":title,"source":label,"url":link,"pubdate":pub})

results["pir06_critical_alert"]["formal_removal_notice_detected"] = len(crit_hits) > 0
results["pir06_critical_alert"]["critical_evidence"] = crit_hits
results["pir06_critical_alert"]["precursor_items_count"] = len(precursor_hits)
results["pir06_critical_alert"]["precursor_items_sample"] = precursor_hits[:10]
results["universal_gnews_files"] = gn_files
results["titles_scanned_for_critical"] = len(all_titles_for_crit_scan)

# ---- write results json ----
with open(os.path.join(BASE, f"_scrape_results_{TS}.json"),"w",encoding="utf-8") as f:
    json.dump(results, f, ensure_ascii=False, indent=2)

print("\n" + "="*70)
print(f"CRITICAL PIR-06 formal-removal-notice scan: {len(crit_hits)} hits across {len(all_titles_for_crit_scan)} titles")
if crit_hits:
    print("  !!! CRITICAL DETECTED !!!")
    for c in crit_hits: print(f"   - {c['title']}  [{c['source']}]  {c['url']}")
else:
    print("  (none — formal PN-MT removal notice NOT detected)")
print(f"Precursor (call-for-removal) items: {len(precursor_hits)}")
for p in precursor_hits[:8]:
    print(f"   - {p['title']}  [{p['source']}]")
print("="*70)
print(f"DONE. results_json = _scrape_results_{TS}.json")
print(f"TS={TS} TODAY={TODAY}")
