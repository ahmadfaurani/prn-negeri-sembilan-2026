#!/usr/bin/env python3
"""
PRN Negeri Sembilan 2026 - News Collection v2 (Nomination Day Surge cycle).
Multi-strategy: WP REST API + HTML extraction + Google News RSS fallback.
Decodes Google News article URLs to originals. PIR keyword tagging.
PIR-06 CRITICAL detection for formal PN Supreme Council removal notice.
"""
import subprocess, json, os, re, base64, datetime
from urllib.parse import urljoin, urlparse
from bs4 import BeautifulSoup
import xml.etree.ElementTree as ET

BASE = "/home/p62operator/.openclaw/workspace-ns/04-DATA-AND-SOURCES/raw-scrapes"
TODAY = datetime.datetime.utcnow().strftime("%Y%m%d")
TS = datetime.datetime.utcnow().strftime("%H%M%S")
OUTDIR = os.path.join(BASE, TODAY)
os.makedirs(OUTDIR, exist_ok=True)

UA = ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36")
NOW_ISO = datetime.datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S UTC")

PIR = {
    "PIR-06": ["pecat", "terminate", "remove", "keluar", "withdraw", "tarik diri",
               "majlis tertinggi", "asas kukuh", "bersatu", "kiandee", "muhyiddin",
               "hamzah zainudin", "samsuri", "hadi", "supreme council", "dibuang",
               "diberhentikan", "keluar pn", "bubarkan", "pecat bersatu",
               "buang bersatu", "dikeluarkan", "perikatan nasional"],
    "PIR-09": ["disiplin", "lompat", "pengkhianat", "defector", "hopper",
               "kredibiliti", "eligibility", "bankrup", "kes mahkamah", "calon",
               "independent", "bebas", "gerakan", "tang jay", "ampangan",
               "nazri kassim", "rafie", "tamim", "kalah kerusi", "tatang"],
    "PIR-07": ["kerusi tumpuan", "battleground", "pertembungan", "marquee", "pinggir",
               "manifesto", "kempen", "operasi", "hari penamaan", "nomination",
               "penamaan", "tumpuan", "pertandingan", "calonkan", "negeri sembilan",
               "negri sembilan", "n9 polls", "prn", "state election",
               "pilihanraya negeri", "ogos 1", "aug 1", "polling day"],
}
# PIR-06 CRITICAL: formal PN Supreme Council removal notice for Bersatu
PIR06_CRITICAL_PATTERNS = [
    r"majlis\s+tertinggi\s*(pn|perikatan\s+nasional).{0,60}(buang|pecat|keluarkan|dikeluarkan|remove|terminate|bubarkan).{0,40}bersatu",
    r"(pn|perikatan\s+nasional).{0,40}(buang|pecat|keluarkan|dikeluarkan|remove|terminate).{0,40}bersatu",
    r"bersatu.{0,40}(dikeluarkan|dibuang|diberhentikan|dipecat).{0,40}(daripada|dari|oleh).{0,30}(pn|perikatan)",
    r"(remov|terminat|expel|kick).{0,30}bersatu.{0,40}(from|out of).{0,20}(pn|perikatan)",
    r"notice.{0,30}remov.{0,40}bersatu",
]
PIR06_CRITICAL_RE = re.compile("|".join(PIR06_CRITICAL_PATTERNS), re.IGNORECASE)
# Negative-discriminator: Kiandee's "grounds to remove" is a PRECURSOR opinion, not a formal notice.
PIR06_PRECURSOR_RE = re.compile(r"(asas\s+kukuh|grounds\s+to\s+remove|has\s+grounds|kiandee)", re.IGNORECASE)

def fetch(url, timeout=30, accept_html=False):
    try:
        cmd = ["curl","-sS","-L","-m",str(timeout),"-A",UA,"--compressed",
               "-H","Accept-Language: en-US,en;q=0.9,ms;q=0.8"]
        if not accept_html:
            cmd += ["-H","Accept: application/json, text/xml, application/xml, */*"]
        cmd += ["-w","\n__HTTPCODE__:%{http_code}", url]
        p = subprocess.run(cmd, capture_output=True, timeout=timeout+10)
        out = p.stdout
        m = re.search(rb"__HTTPCODE__:(\d+)", out)
        code = m.group(1).decode() if m else "ERR"
        body = out[:m.start()] if m else out
        return code, body
    except Exception:
        return "ERR", b""

def decode_gnews_url(google_url):
    m = re.search(r"/articles/([A-Za-z0-9_\-]+)", google_url)
    if not m: return None
    token = m.group(1)
    token += "=" * (-len(token) % 4)
    try:
        raw = base64.urlsafe_b64decode(token)
    except Exception:
        return None
    m2 = re.search(rb"https?://[A-Za-z0-9.\-]+/[^\x00-\x1f\x22<> ]+", raw)
    return m2.group(0).decode("utf-8","replace") if m2 else None

def gnews(query, label, max_items=60):
    """Fetch Google News RSS; return list of article dicts."""
    url = f"https://news.google.com/rss/search?q={query}&hl=en-MY&gl=MY&ceid=MY:en"
    code, body = fetch(url)
    items = []
    if code != "200" or not body:
        return code, items
    try:
        root = ET.fromstring(body)
    except Exception:
        return code, items
    for it in root.iter("item"):
        title = (it.findtext("title") or "").strip()
        link = (it.findtext("link") or "").strip()
        pub = (it.findtext("pubDate") or "").strip()
        src_el = it.find("source")
        publisher = src_el.text.strip() if src_el is not None and src_el.text else ""
        orig = decode_gnews_url(link) or ""
        # strip trailing " - Publisher" from title
        clean_title = title
        if publisher and title.endswith(" - " + publisher):
            clean_title = title[:-(len(publisher)+3)].strip()
        else:
            mm = re.match(r"^(.*?)(?:\s+-\s+[^-]+)$", title)
            if mm: clean_title = mm.group(1).strip()
        items.append({
            "title": clean_title[:220], "gnews_link": link, "orig_url": orig,
            "publisher": publisher, "pubDate": pub, "source_query": label,
        })
        if len(items) >= max_items: break
    return code, items

def wpapi(base, per_page=50, search=None):
    q = f"{base}/wp-json/wp/v2/posts?per_page={per_page}&_embed=1"
    if search: q += f"&search={search}"
    code, body = fetch(q)
    if code != "200" or not body:
        return code, []
    try:
        arr = json.loads(body)
    except Exception:
        return code, []
    items = []
    for p in arr:
        t = re.sub(r"<[^>]+>","", p.get("title",{}).get("rendered","")).strip()
        ex = re.sub(r"<[^>]+>","", p.get("excerpt",{}).get("rendered","")).strip()
        items.append({
            "title": t[:220], "orig_url": p.get("link",""), "pubDate": p.get("date",""),
            "snippet": ex[:300], "gnews_link": "",
        })
    return code, items

TIME_RE = re.compile(r"(\b\d+\s*(min|mins|minute|minutes|hr|hrs|hour|hours|day|days|week|weeks)\s*ago\b|"
                     r"\bjust now\b|\bbaru\s+sahaja\b|\b\d{1,2}[:.]\d{2}\s*(am|pm)?\b|"
                     r"\bhari\s+ini\b|\bsemalam\b|\d{1,2}\s+(jam|minit|hari)\s+yang\s+lepas)", re.IGNORECASE)

def is_article(href, host):
    if not href: return False
    p = urlparse(href)
    if p.netloc and p.netloc != host: return False
    path = p.path.lower()
    if re.search(r"\.(jpg|jpeg|png|gif|css|js|svg|ico|webp|pdf|mp4)$", path): return False
    if re.search(r"/(news|berita|nasional|lokal|nation|article|sembilan|sem|columns|feed)/", path): return True
    if re.search(r"/20\d{2}/", path): return True
    if re.search(r"/\d{4,}", path): return True
    return False

def html_extract(url, host):
    code, body = fetch(url, accept_html=True)
    if code != "200" or not body: return code, []
    soup = BeautifulSoup(body.decode("utf-8","replace"), "html.parser")
    items = []; seen = set()
    for a in soup.find_all("a", href=True):
        href = urljoin(url, a["href"])
        if href in seen: continue
        if not is_article(href, host): continue
        txt = a.get_text(" ", strip=True)
        alt = ""
        img = a.find("img")
        if img and img.get("alt"): alt = img["alt"]
        title = txt or alt or a.get("title","") or ""
        title = re.sub(r"\s+"," ", title).strip()
        if len(title) < 10: continue
        low = title.lower()
        if low in ("news","nation","nasional","berita","more","read more","selanjutnya",
                   "lokal","sembilan","log out","latest","world","focus","home"): continue
        # skip pure category labels
        if re.fullmatch(r"[A-Za-z ]{1,30}", title) and not re.search(r"\d", title) and len(title.split())<=3:
            # could be a category; keep only if URL has an article slug depth
            if urlparse(href).path.count("/") < 5: continue
        seen.add(href)
        # time
        time_txt=""; par=a.parent
        for _ in range(3):
            if par is None: break
            pt = par.get_text(" ",strip=True) if hasattr(par,"get_text") else ""
            mt = TIME_RE.search(pt)
            if mt: time_txt=mt.group(0); break
            par = par.parent
        snip=""
        if par is not None and hasattr(par,"get_text"):
            snip = par.get_text(" ",strip=True)
            snip = snip.replace(title,"",1).strip()
        items.append({"title":title[:220],"orig_url":href,"pubDate":time_txt[:40],"snippet":snip[:300]})
    return code, items

def tag_pir(text):
    tl = text.lower(); tags=[]; hits_map={}
    for pir,kws in PIR.items():
        hits=[k for k in kws if k in tl]
        if hits: tags.append(pir); hits_map[pir]=hits
    return tags, hits_map

def prn_relevant(text):
    return bool(re.search(r"(negeri sembilan|negri sembilan|n9 poll|prn\s*(neg|ns|semb)|sembilan poll|state election|pilihanraya negeri|hari penamaan|nomination|bersatu|perikatan|pakatan|\bph\b|\bbn\b|barisan nasional|august 1|1 ogos|ogos 1|polling day)", text, re.IGNORECASE))

def render_md(label, source_url, items, code, strategy):
    lines = []
    lines.append(f"# {label} - PRN Negeri Sembilan 2026 News Collection")
    lines.append(f"Source URL: {source_url}")
    lines.append(f"Collected: {TODAY} {TS} UTC ({NOW_ISO}) | Classification: TLP:AMBER")
    lines.append(f"Strategy: {strategy} | HTTP: {code} | articles: {len(items)}")
    lines.append("")
    lines.append("## Article Listing")
    lines.append("="*70)
    for it in items:
        combined = it["title"] + " " + it.get("snippet","") + " " + it.get("publisher","")
        tags, hits = tag_pir(combined)
        prn = prn_relevant(combined)
        prefix = ""
        if tags: prefix = f"[PRIORITY {' '.join(tags)}] "
        elif prn: prefix = "[PRN-NS] "
        line = f"{prefix}{it['title']}"
        meta=[]
        if it.get("pubDate"): meta.append(it["pubDate"])
        if it.get("publisher"): meta.append(it["publisher"])
        if meta: line += f"  | {' | '.join(meta)}"
        lines.append(line)
        url = it.get("orig_url") or it.get("gnews_link") or ""
        if url: lines.append(f"   {url}")
        if it.get("snippet"): lines.append(f"   > {it['snippet']}")
        lines.append("")
    lines.append("="*70)
    return "\n".join(lines)

def main():
    per_source = {}  # key -> {label, url, items, code, strategy, file}
    all_items = []   # for metadata/delta

    # ---- WP API sources ----
    for key,label,base in [("utusancommy","Utusan Malaysia","https://www.utusan.com.my"),
                          ("kosmocommy","Kosmo","https://www.kosmo.com.my"),
                          ("ohbulancom","OhBulan","https://www.ohbulan.com")]:
        code, items = wpapi(base, per_page=60)
        # also try homepage HTML for these (kosmo homepage had date-based articles)
        per_source[key] = {"label":label,"url":base+"/wp-json/wp/v2/posts","items":items,"code":code,"strategy":"wpapi","hits":[]}

    # ---- HTML extraction sources ----
    html_sources = [
        ("malaysiakinicom","Malaysiakini","https://www.malaysiakini.com"),
        ("astroawanicom","Astro Awani","https://www.astroawani.com"),
        ("thestarcommy","The Star","https://www.thestar.com.my/news/nation"),
        ("thmalaysianinsightcom","The Malaysian Insight","https://www.themalaysianinsight.com"),
        ("mstarcommy","mStar","https://www.mstar.com.my"),
        ("kosmocommy_html","Kosmo (homepage)","https://www.kosmo.com.my"),
        ("utusancommy_html","Utusan (nasional section)","https://www.utusan.com.my/nasional/"),
    ]
    for key,label,url in html_sources:
        host=urlparse(url).netloc
        code, items = html_extract(url, host)
        if key in per_source and len(per_source[key]["items"]) < len(items):
            per_source[key] = {"label":label,"url":url,"items":items,"code":code,"strategy":"html","hits":[]}
        elif key not in per_source:
            per_source[key] = {"label":label,"url":url,"items":items,"code":code,"strategy":"html","hits":[]}

    # ---- Google News per-source + universal ----
    gn_queries = [
        ("nstcommy","New Straits Times (via Google News)","site:nst.com.my+Negeri+Sembilan"),
        ("bhariancommy","BHarian (via Google News)","site:bharian.com.my+Negeri+Sembilan"),
        ("mstarcommy_gn","mStar (via Google News)","site:mstar.com.my+Negeri+Sembilan"),
        ("thestarcommy_gn","The Star (via Google News)","site:thestar.com.my+Negeri+Sembilan"),
        ("astroawanicom_gn","Astro Awani (via Google News)","site:astroawani.com+Negeri+Sembilan"),
        ("malaysiakinicom_gn","Malaysiakini (via Google News)","site:malaysiakini.com+Negeri+Sembilan"),
        ("_universal_prn_bersatu","Google News Universal: PRN Negeri Sembilan Bersatu","PRN+Negeri+Sembilan+Bersatu"),
        ("_universal_pn_pecat","Google News Universal: PN pecat/keluar Bersatu","PN+Bersatu+(pecat+OR+keluar+OR+buang)"),
        ("_universal_nomination","Google News Universal: Nomination Day Negeri Sembilan","(nomination+OR+penamaan)+Negeri+Sembilan"),
    ]
    gn_all = []
    for key,label,q in gn_queries:
        code, items = gnews(q, key, max_items=60)
        for it in items: it["publisher_host"]=urlparse(it.get("orig_url") or "").netloc
        gn_all.extend(items)
        if not key.startswith("_"):
            # merge into per-source if richer
            if key in per_source:
                if len(items) > len(per_source[key]["items"]):
                    per_source[key] = {"label":label,"url":"Google News: "+q,"items":items,"code":code,"strategy":"gnews","hits":[]}
            else:
                per_source[key] = {"label":label,"url":"Google News: "+q,"items":items,"code":code,"strategy":"gnews","hits":[]}

    # Save universal google-news file
    for ukey,ulabel in [("_universal_prn_bersatu","PRN Negeri Sembilan Bersatu"),
                       ("_universal_pn_pecat","PN pecat/keluar Bersatu"),
                       ("_universal_nomination","Nomination Day Negeri Sembilan")]:
        u_items = [it for it in gn_all if it.get("source_query")==ukey]
        md = render_md(f"Google News Universal - {ulabel}", "https://news.google.com/rss/search", u_items, "200", "google-news-rss")
        fname = f"google_news_{ukey.replace('_','')}_html_{TODAY}_{TS}.md"
        with open(os.path.join(OUTDIR, fname),"w",encoding="utf-8") as f: f.write(md)
        per_source["gnfile_"+ukey] = {"label":ulabel,"file":fname,"items":u_items}

    # ---- Write per-source .md files ----
    summary = []
    pir06_critical_flag = False
    pir06_critical_evidence = []
    pir06_precursor_items = []
    for key, info in per_source.items():
        if key.startswith("gnfile_"): continue
        if "items" not in info: continue
        items = info["items"]
        md = render_md(info["label"], info.get("url",""), items, info.get("code",""), info.get("strategy",""))
        fname = f"{key}_{TODAY}_{TS}.md"
        with open(os.path.join(OUTDIR, fname),"w",encoding="utf-8") as f: f.write(md)
        # aggregate
        pri_count = 0; prn_count=0; pir06_hits=0; pir09_hits=0; pir07_hits=0
        for it in items:
            combined = it["title"]+" "+it.get("snippet","")+" "+it.get("publisher","")
            tags, hits = tag_pir(combined)
            prn = prn_relevant(combined)
            if tags: pri_count+=1
            if prn: prn_count+=1
            if "PIR-06" in tags: pir06_hits+=1
            if "PIR-09" in tags: pir09_hits+=1
            if "PIR-07" in tags: pir07_hits+=1
            full = combined
            if PIR06_CRITICAL_RE.search(full) and not PIR06_PRECURSOR_RE.search(full):
                pir06_critical_flag=True
                pir06_critical_evidence.append({"title":it["title"],"url":it.get("orig_url") or it.get("gnews_link"),"source":key})
            elif PIR06_PRECURSOR_RE.search(full) and "bersatu" in full.lower():
                pir06_precursor_items.append({"title":it["title"],"url":it.get("orig_url") or it.get("gnews_link"),"source":key})
        summary.append({
            "source":key,"label":info["label"],"url":info["url"],"strategy":info.get("strategy",""),
            "http_code":info.get("code",""),"article_count":len(items),
            "priority_article_count":pri_count,"prn_article_count":prn_count,
            "pir06_hits":pir06_hits,"pir09_hits":pir09_hits,"pir07_hits":pir07_hits,
            "file":fname,
            "priority_titles":[it["title"] for it in items if tag_pir(it["title"]+" "+it.get("snippet","")+" "+it.get("publisher",""))[0]][:25],
        })

    # ---- Save structured results + CRITICAL flag ----
    out = {
        "timestamp": f"{TODAY}_{TS}", "collected_utc": NOW_ISO,
        "pir06_critical_alert": {
            "formal_removal_notice_detected": pir06_critical_flag,
            "critical_evidence": pir06_critical_evidence,
            "precursor_items_count": len(pir06_precursor_items),
            "precursor_items_sample": pir06_precursor_items[:15],
        },
        "sources": summary,
    }
    with open(os.path.join(OUTDIR, f"_scrape_results_{TS}.json"),"w") as f:
        json.dump(out, f, indent=2, ensure_ascii=False)

    print(f"=== SCRAPE COMPLETE ts={TODAY}_{TS} ===")
    print(f"PIR-06 CRITICAL (formal removal notice): {pir06_critical_flag}")
    print(f"PIR-06 precursor items: {len(pir06_precursor_items)}")
    if pir06_critical_evidence:
        print("CRITICAL EVIDENCE:")
        for e in pir06_critical_evidence: print("  !",e["title"],e["url"])
    print(f"\nPer-source summary:")
    for s in summary:
        print(f"  [{s['http_code']}] {s['source']:24s} arts={s['article_count']:4d} pri={s['priority_article_count']:3d} prn={s['prn_article_count']:3d} P06={s['pir06_hits']} P09={s['pir09_hits']} P07={s['pir07_hits']} [{s['strategy']}]")
    print(f"\nResults JSON: {OUTDIR}/_scrape_results_{TS}.json")

if __name__ == "__main__":
    main()
