#!/usr/bin/env python3
"""Nomination-Day Surge cycle 20260721_predawn (collecting ~19:16 UTC / 03:16 MYT 21 Jul 2026).
Campaign Day 3 (MYT 21 Jul). Director-approved PIR-06/07/16 priority collection.
Cutoff: post-18:01 UTC 20 Jul 2026 (post-02:01 MYT 21 Jul) = earlyam cycle end.

FOCUS: Pre-dawn (~03:16 MYT) scan, ~1hr15m after earlyam cycle. Check for:
  - Any fresh Day-3 (21 Jul) campaign ground content posted after 02:01 MYT
    (midnight newsroom quiet hours; expect low yield, but international wires /
     pre-scheduled publications may surface)
  - PIR-06 [CRITICAL] watch (32nd cycle): formal PN-MT expulsion, Bersatu withdrawal,
    Kiandee quorum, RoS action, "lebih hebat" formalization
  - PIR-16 [CRITICAL] watch: hard-news corroboration of "Bersatu exit imminent" /
    "sasar bentuk kerajaan negeri"
  - Manifesto reception / BN-PN counter-response pickup (continuation)
  - Anwar Wed 22 Jul campaign schedule confirmation
  - MCMC 3R enforcement updates
  - The Vibes backlog enrichment (continue: 125290-125330)
  - Sinar ID scan (789120-789200 — next range after dawn's exhausted 789040-789120)

Sources: Google News RSS (PIR-targeted) + RSS feeds (Awani/FMT/HarianMetro/NST/
  MalayMail/Sinar/Utusan) + homepage extraction (Awani/NST/MalayMail/Utusan/
  HarianMetro/Sinar/Star/Kosmo) + The Vibes scan (125290-125330) + Sinar ID scan
  (789120-789200).
All content carries source URL. TLP:AMBER.
"""
import subprocess, re, datetime, json, os, html, time, sys
import xml.etree.ElementTree as ET
from urllib.parse import urljoin, quote as url_quote

try:
    from bs4 import BeautifulSoup
    HAVE_BS4 = True
except Exception:
    BeautifulSoup = None
    HAVE_BS4 = False

BASE = "/home/p62operator/.openclaw/workspace-ns/04-DATA-AND-SOURCES/raw-scrapes/20260721"
os.makedirs(BASE, exist_ok=True)
THIS_TS = "20260721_predawn"
TODAY = "20260721"
# Cutoff = earlyam cycle end (18:01 UTC 20 Jul = 02:01 MYT 21 Jul)
CUTOFF_UTC = datetime.datetime(2026, 7, 20, 18, 1, 0, tzinfo=datetime.timezone.utc)
NOW_UTC = datetime.datetime.now(datetime.timezone.utc)

UA = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0 Safari/537.36"

# ---- Keyword sets (PIR-06 / 07 / 16) ----
PIR06 = ['pn','bersatu','pecat','keluar','buang','tarik diri','toxic pn','termination','pn-mt',
         'supreme council','quorum','kuorum','kiandee','muhyiddin','hadi','hamzah','ridzuan ahmad',
         'new coalition','lebih hebat','wawasan','bn-pn','machinery sharing','joint ceramah',
         'gabung jentera','bersepadu','sole opposition','lone opposition','only true opposition',
         'ros',' registrar of societies','voluntary split','new alliance','looks beyond pn']
PIR16 = ['narrative','dap acceptance','loke','mca biggest loser','mca rebuttal','wee','mah hang soon',
         'adat','melaka withdrawal','melaka ph-bn','bersatu exit','bersatu in disarray','kacau daun',
         'wan saiful','barking dogs','albert tei','graft trial','muhyiddin corruption',
         'majoriti mudah','mb after prn','sole opposition','sasar bentuk kerajaan','malay unity',
         'penyatuan undi melayu','makmal politik','not briefed','resign to attack',
         'bersatu sasar bentuk kerjaan negeri','punching bag','bogeyman','traitors',
         'islamophobia','poster boy','biggest loser','menebuk','dapan','kesinambungan',
         'unity government','kerajaan perpaduan','dap congress','dap convention']
PIR07 = ['ampangan','juasseh','klawang','sikamat','linggi','chembong','bembang','labu','nilai',
         'sri tanjung','rantau','tok mat','pertang','jalaluddin','derhaka','battleground',
         'kerusi tumpuan','hot seat','ceramah','walkabout','ops-centre','manifesto launch',
         'chennah','lenggeng','bahau','lobak','bukit kepayang','paroi','lukut',
         'bagan pinang','gemas','repah','jeram padang','rahang','pilihan raya negeri',
         'negeri sembilan','prn','johol','jempol','palong','chuah','gemencheh','tampin',
         'nomination','three-cornered','seat swap','candidate','menti besar','menteri besar',
         'kekal harapan','amirudin','sufian','razali','arul kumar','danni rais','bakri sawir']

def hit(title, body=''):
    t = (title or '').lower()
    b = (body or '').lower()
    tag = []
    if any(k in t or k in b for k in PIR06): tag.append('PIR-06')
    if any(k in t or k in b for k in PIR07): tag.append('PIR-07')
    if any(k in t or k in b for k in PIR16): tag.append('PIR-16')
    return tag

def is_prn(title, body=''):
    t = (title or '').lower(); b = (body or '').lower()
    kw = ['negeri sembilan','prn negeri','pilihan raya negeri','tok mat','aminuddin',
          'anthony loke','wee ka siong','hadi awang','muhyiddin','hamzah zainudin',
          'khaled nordin','khairy jamaluddin','kj ','jalaluddin alias','manifesto',
          'amirudin','asas','kesinambungan','prnns','ns prn','ns polls','negeri polls',
          'kekal harapan']
    return any(k in t or k in b for k in kw) or bool(hit(title, body))

def parse_date(s):
    if not s: return None
    for fmt in ['%a, %d %b %Y %H:%M:%S %z','%Y-%m-%dT%H:%M:%S%z','%Y-%m-%dT%H:%M:%SZ','%Y-%m-%d %H:%M:%S']:
        try: return datetime.datetime.strptime(s.strip(), fmt)
        except: pass
    try:
        import email.utils
        d = email.utils.parsedate_to_datetime(s)
        if d: return d
    except: pass
    return None

def slugify(s):
    s = re.sub(r'[^a-z0-9]+','-', s.lower()).strip('-')
    return s[:80] or 'untitled'

def fetch(url, timeout=20):
    try:
        r = subprocess.run(['curl','-sS','-L','-m',str(timeout),'-A',UA,
                           '--compressed', url], capture_output=True, timeout=timeout+5)
        return r.returncode, r.stdout.decode('utf-8','replace')
    except Exception:
        return -1, ''

def clean_html(htmltxt):
    if HAVE_BS4 and BeautifulSoup is not None:
        try:
            soup = BeautifulSoup(htmltxt, 'html.parser')
            for tag in soup(['script','style','noscript','iframe','svg','header','footer','nav']):
                tag.decompose()
            for sel in ['article','main','div.post-content','div.article-content',
                        'div.entry-content','div.content','div.body-content','div#article-body',
                        'div.story-content','div.field-body','div.article-body',
                        'div.detail-content','div.news-content','div.isi-berita','div.kandungan',
                        'div.page-content','div.article-detail','div.cms-content']:
                c = soup.select_one(sel)
                if c and len(c.get_text(strip=True)) > 300:
                    return c.get_text('\n', strip=True)
            return soup.get_text('\n', strip=True)
        except Exception:
            pass
    txt = re.sub(r'<script[^>]*>.*?</script>',' ',htmltxt,flags=re.S|re.I)
    txt = re.sub(r'<style[^>]*>.*?</style>',' ',txt,flags=re.S|re.I)
    txt = re.sub(r'<[^>]+>',' ',txt)
    return re.sub(r'\s+',' ',txt).strip()

def save_article(src, url, title, datestr, body, tags, suffix=''):
    if not body or len(body) < 80:
        return None
    sl = slugify(title)
    tagprefix = ('priority_' + '-'.join(tags) + '_') if tags else ''
    fn = f"{BASE}/{tagprefix}{src}_{sl}_{THIS_TS}{suffix}.md"
    n=1
    while os.path.exists(fn):
        fn = f"{BASE}/{tagprefix}{src}_{sl}_{THIS_TS}{suffix}_{n}.md"; n+=1
    crit = ''
    bc = body.lower()
    is_critical = False
    if 'PIR-06' in tags:
        formal_terms = ['pecat','expulsion','tarik diri','withdraw','keluar dari pn',
                        'kuorum','quorum to vote','lebih hebat','remove bersatu',
                        'sack bersatu','dissolve pn','bubarkan pn','formal expulsion',
                        'expulsion notice','candidate withdrawal','bersatu withdrawal',
                        'ros revokes','registrar of societies',
                        'pdm klawang buka semula','pdm klawang reopen']
        if any(k in bc for k in formal_terms):
            if any(k in bc for k in ['pn','bersatu','perikatan','muhyiddin','kiandee','klawang']):
                crit = ' [CRITICAL]'; is_critical = True
    if 'PIR-16' in tags and not is_critical:
        if ('bersatu' in bc and 'sasar bentuk kerajaan negeri' in bc):
            crit = ' [CRITICAL]'; is_critical = True
        elif 'bersatu exit imminent' in bc:
            crit = ' [CRITICAL]'; is_critical = True
    md = []
    md.append(f"# {title}")
    md.append("")
    md.append(f"**Source:** {src} | **URL:** {url}")
    md.append(f"**Date:** {datestr}")
    md.append(f"**Collected:** {NOW_UTC.isoformat()} (cycle {THIS_TS})")
    md.append(f"**PIR tags:** {', '.join(tags) if tags else 'none'}{crit}")
    md.append("")
    md.append("---")
    md.append("")
    md.append(body)
    with open(fn,'w') as f:
        f.write('\n'.join(md))
    return fn, is_critical

results = {'scanned':0,'prn_hits':0,'saved':0,'critical':0,'saved_files':[],
           'gnews_queries':0,'feed_items':0,'fresh_after_cutoff':0,
           'duplicates':0,'gnews_headlines':[], 'rss_articles':[],
           'thevibes_collected':0,'thevibes_skipped':0, 'thevibes_new':[],
           'gnews_fresh_priority':[]}

# existing slugs/URLs to dedup (check 20260721 + 20260720 + 20260719 dirs for cross-day dedup)
existing_titles = set()
existing_basenames = set()
existing_urls = set()
for d in ['20260721','20260720','20260719']:
    p = f"/home/p62operator/.openclaw/workspace-ns/04-DATA-AND-SOURCES/raw-scrapes/{d}"
    if os.path.isdir(p):
        for fn in os.listdir(p):
            if fn.endswith('.md'):
                existing_titles.add(fn)
                core = re.sub(r'_(20260721_[^_]*|20260720_(?:morning|midday|afternoon|evening|midafternoon|lateafternoon|dusk|night|latenight|postmanifesto|night2|night3)|20260719_[^_]*)(?:_rss|_home|_targeted|_thevibes|_thevibesfresh|_gnews)?\.md','.md', fn)
                existing_basenames.add(core)
for d in ['20260721','20260720','20260719']:
    p = f"/home/p62operator/.openclaw/workspace-ns/04-DATA-AND-SOURCES/raw-scrapes/{d}"
    if os.path.isdir(p):
        for fn in os.listdir(p):
            if fn.endswith('.md'):
                try:
                    with open(os.path.join(p,fn)) as f:
                        txt = f.read()
                    for m in re.findall(r'\*\*URL:\*\*\s*(\S+)', txt):
                        existing_urls.add(m.strip())
                except: pass

print(f"[0] cutoff: {CUTOFF_UTC.isoformat()} (02:01 MYT 21 Jul) | now: {NOW_UTC.isoformat()}")
print(f"[0] existing URLs in dedup: {len(existing_urls)} | existing titles: {len(existing_titles)}")

# ============================================================
# 1. GOOGLE NEWS RSS — PIR-targeted queries
# ============================================================
print("\n=== [1] GOOGLE NEWS RSS ===")
GNEWS_QUERIES = [
    # PIR-06 [CRITICAL] watch (mandatory — 32nd cycle)
    'Bersatu pecat PN Negeri Sembilan',
    'Bersatu tarik diri PN kuorum Negeri Sembilan',
    'lebih hebat coalition PN Bersatu Negeri Sembilan',
    'Bersatu sole opposition parliament Negeri Sembilan',
    'Kiandee quorum Bersatu Negeri Sembilan',
    'PDM Klawang buka semula Negeri Sembilan',
    'RoS registrar societies PN Bersatu Negeri Sembilan',
    'Bersatu candidate withdrawal Negeri Sembilan PRN',
    # PIR-16 narratives — manifesto reception + Loke DAP-congress + Asyraf counter
    'manifesto PH Kekal Harapan Negeri Sembilan response',
    'BN PN response manifesto PH Negeri Sembilan',
    'Loke DAP congress Unity Government Negeri Sembilan',
    'Asyraf Wajdi kerajaan perpaduan kekal Negeri Sembilan',
    'DAP keluar kerajaan perpaduan PRN Negeri Sembilan',
    'Bersatu kacau daun Negeri Sembilan',
    'Wan Saiful bersatu messing things up Negeri Sembilan',
    'makmal politik PRU16 Anwar Negeri Sembilan',
    'penyatuan undi Melayu Negeri Sembilan',
    'MCA Wee Ka Siong Loke Negeri Sembilan',
    'Melaka DAP withdrawal PH BN Negeri Sembilan',
    # PIR-07 battlegrounds — Day-3 campaign
    'Negeri Sembilan PRN 2026',
    'PRN Negeri Sembilan pilihan raya',
    'Bersatu PN Negeri Sembilan 2026',
    'PRN Negeri Sembilan calon kempen 21 Jul',
    'Negeri Sembilan PRN ceramah 21 Jul',
    'Tok Mat Rantau Negeri Sembilan ceramah',
    'Anthony Loke Chennah Negeri Sembilan',
    'Aminuddin Harun Linggi Negeri Sembilan kempen',
    'Pertang Jalaluddin derhaka Negeri Sembilan',
    'Sikamat Razali Wawasan Negeri Sembilan',
    'Klawang cousins Negeri Sembilan three-cornered',
    'Nilai Arul Kumar DAP Negeri Sembilan',
    'BN manifesto Negeri Sembilan 24 Jul',
    'Johol Khaled Negeri Sembilan machinery',
    # fresh Day-3 pre-dawn content watch
    'PRN N9 21 Jul calon kempen',
    'Negeri Sembilan pilihan raya 21 Jul',
    'pilihan raya negeri Sembilan hari ini',
    'Anwar berkempen Sikamat Paroi Negeri Sembilan',
    'MCMC 3R Tuanku Muhriz Negeri Sembilan',
]
seen_urls = set()
gnews_all = []
for q in GNEWS_QUERIES:
    url = "https://news.google.com/rss/search?q=" + url_quote(q) + "&hl=en-MY&gl=MY&ceid=MY:en"
    rc, txt = fetch(url, timeout=20)
    results['gnews_queries'] += 1
    if rc != 0 or not txt or '<item>' not in txt:
        continue
    try:
        root = ET.fromstring(txt.encode('utf-8'))
        for it in root.iter('item'):
            title_el = it.find('title'); link_el = it.find('link')
            pub_el = it.find('pubDate'); src_el = it.find('source')
            t = (title_el.text or '') if title_el is not None else ''
            mt = re.match(r'^(.*?)\s+-\s+([^-]+)$', t)
            if mt: headline=mt.group(1).strip(); srcname=mt.group(2).strip()
            else: headline=t; srcname=(src_el.text if src_el is not None else 'gnews')
            l = (link_el.text or '') if link_el is not None else ''
            d = parse_date(pub_el.text if pub_el is not None else '')
            if l in seen_urls: continue
            seen_urls.add(l)
            gnews_all.append({'q':q,'title':headline,'src':srcname,'url':l,'date':d})
    except Exception:
        pass
    time.sleep(0.25)

for g in gnews_all:
    results['feed_items'] += 1
    d = g['date']
    fresh = (d is None) or (d.tzinfo is None) or (d >= CUTOFF_UTC)
    if fresh: results['fresh_after_cutoff'] += 1
    tags = hit(g['title'])
    isprn = is_prn(g['title'])
    if tags or isprn:
        results['gnews_headlines'].append({
            'q':g['q'],'title':g['title'],'src':g['src'],'url':g['url'],
            'date': d.isoformat() if d else '', 'fresh': fresh, 'tags': tags
        })
        if fresh and tags:
            results['gnews_fresh_priority'].append(g)
print(f"[1] gnews: {results['gnews_queries']} queries -> {len(gnews_all)} items, "
      f"{len(results['gnews_headlines'])} PRN/priority hits, {results['fresh_after_cutoff']} fresh")

# ============================================================
# 2. RSS FEEDS — Awani + FMT + HarianMetro + NST + MalayMail + Sinar + Utusan
# ============================================================
print("\n=== [2] RSS FEEDS ===")
RSS_FEEDS = [
    ('Awani', 'https://www.astroawani.com/rss.xml'),
    ('Awani-Politik', 'https://www.astroawani.com/rss/berita-politik.xml'),
    ('FMT', 'https://www.freemalaysiatoday.com/feed/'),
    ('HarianMetro', 'https://www.hmetro.com.my/feed'),
    ('NST', 'https://www.nst.com.my/feed/rss/nation'),
    ('MalayMail', 'https://www.malaymail.com/rss'),
    ('Sinar', 'https://www.sinarharian.com.my/rss'),
    ('Utusan', 'https://www.utusan.com.my/rss.xml'),
]
feed_articles = []
for src, furl in RSS_FEEDS:
    rc, txt = fetch(furl, timeout=20)
    if rc != 0 or not txt or '<item>' not in txt:
        print(f"[2] {src} feed: HTTP rc={rc}, no items")
        continue
    try:
        root = ET.fromstring(txt.encode('utf-8'))
    except Exception:
        try: root = ET.fromstring(re.sub(r'[\x00-\x08\x0b\x0c\x0e-\x1f]','',txt).encode('utf-8'))
        except Exception:
            print(f"[2] {src} feed: parse fail"); continue
    cnt = 0
    for it in root.iter('item'):
        title_el = it.find('title'); link_el = it.find('link')
        pub_el = it.find('pubDate'); desc_el = it.find('description')
        cont_el = it.find('{http://purl.org/rss/1.0/modules/content/}encoded')
        t = (title_el.text or '') if title_el is not None else ''
        l = (link_el.text or '') if link_el is not None else ''
        d = parse_date(pub_el.text if pub_el is not None else '')
        desc = (desc_el.text or '') if desc_el is not None else ''
        cont = (cont_el.text or '') if cont_el is not None else ''
        body_avail = clean_html(cont) if cont else clean_html(desc)
        cnt += 1
        results['feed_items'] += 1
        tags = hit(t, body_avail)
        isprn = is_prn(t, body_avail)
        if not (tags or isprn):
            continue
        results['prn_hits'] += 1
        fresh = (d is None) or (d.tzinfo is None) or (d >= CUTOFF_UTC)
        feed_articles.append({'src':src,'title':t,'url':l,'date':d,
                              'body':body_avail,'tags':tags,'fresh':fresh,
                              'has_full': bool(cont)})
    print(f"[2] {src} feed: {cnt} items scanned, "
          f"{sum(1 for a in feed_articles if a['src']==src)} PRN/priority hits")

rss_saved = 0
for a in feed_articles:
    if not a['has_full']:
        continue
    if a['url'] in existing_urls:
        results['duplicates'] += 1
        continue
    sl = slugify(a['title'])
    already = False
    for ex in existing_titles:
        if sl in ex and a['src'].lower() in ex.lower():
            already = True; break
    if already and not a['fresh']:
        results['duplicates'] += 1
        continue
    fn_info = save_article(a['src'], a['url'], a['title'],
                           a['date'].isoformat() if a['date'] else '',
                           a['body'], a['tags'], suffix='_rss')
    if fn_info:
        fn, crit = fn_info
        if fn:
            results['saved'] += 1
            results['saved_files'].append(os.path.basename(fn))
            existing_urls.add(a['url'])
            rss_saved += 1
            if crit: results['critical'] += 1
print(f"[2] RSS full-text saved: {rss_saved}")

# ============================================================
# 3. For gnews FRESH priority hits + RSS no-full items: extract article from URL
# ============================================================
to_extract = []
fresh_gnews = 0
for g in results['gnews_headlines']:
    if g['url'] in existing_urls:
        continue
    if g['fresh'] and g['tags']:
        to_extract.append(('gnews', g['src'], g['title'], g['url'], g.get('date',''), g['tags']))
        fresh_gnews += 1
for a in feed_articles:
    if not a['has_full'] and a['fresh'] and a['url'] not in existing_urls:
        to_extract.append((a['src'], a['src'], a['title'], a['url'],
                           a['date'].isoformat() if a['date'] else '', a['tags']))
print(f"[3] URLs to extract full text: {len(to_extract)} (fresh gnews: {fresh_gnews})")
extracted = 0
for kind, src, title, url, datestr, tags in to_extract:
    if not url: continue
    rc, htmltxt = fetch(url, timeout=20)
    if rc != 0 or not htmltxt or len(htmltxt) < 500:
        continue
    body = clean_html(htmltxt)
    if len(body) < 150:
        continue
    tags2 = hit(title, body)
    if tags2: tags = tags2
    fn_info = save_article(src, url, title, datestr, body, tags, suffix='')
    if fn_info:
        fn, crit = fn_info
        if fn:
            results['saved'] += 1
            results['saved_files'].append(os.path.basename(fn))
            existing_urls.add(url)
            if crit: results['critical'] += 1
            extracted += 1
    time.sleep(0.4)
print(f"[3] Extracted full-text from URLs: {extracted}")

# ============================================================
# 4. Homepage headline scan
# ============================================================
print("\n=== [4] HOMEPAGE SCAN ===")
HOME_PAGES = [
    ('Awani', 'https://www.astroawani.com.my/berita'),
    ('Awani', 'https://www.astroawani.com.my/berita-politik'),
    ('NST', 'https://www.nst.com.my/news/politics'),
    ('MalayMail', 'https://www.malaymail.com/news/politics'),
    ('Utusan', 'https://www.utusan.com.my/politik'),
    ('HarianMetro', 'https://www.hmetro.com.my/terkini'),
    ('Sinar', 'https://www.sinarharian.com.my/politik'),
    ('Star', 'https://www.thestar.com.my/news/nation'),
    ('Kosmo', 'https://www.kosmo.com.my/terkini'),
]
home_links = set()
for src, hurl in HOME_PAGES:
    rc, htmltxt = fetch(hurl, timeout=20)
    if rc != 0 or not htmltxt:
        print(f"[4] {src} {hurl}: rc={rc}")
        continue
    links = re.findall(r'href=["\']([^"\']+)["\']', htmltxt)
    cnt = 0
    for lk in links:
        full = urljoin(hurl, lk)
        if full in seen_urls or full in home_links or full in existing_urls:
            continue
        if not re.search(r'/(news|berita|article|nasional|politik|nation|terkini)[/\-]', full, re.I):
            continue
        if re.search(r'\.(css|js|jpg|png|svg|ico)(\?|$)', full, re.I): continue
        home_links.add(full)
        cnt += 1
    print(f"[4] {src} {hurl}: {cnt} candidate links")

url_prn_kw = ['negeri-sembilan','prn','bersatu','loke','tok-mat','aminuddin','sikamat','ampangan',
              'klawang','linggi','rantau','manifesto','ceramah','mca','kiandee','muhyiddin',
              'hamzah','hadi','jalaluddin','pertang','wawasan','kacau-daun','makmal-politik',
              'melaka','wan-saiful','albert-tei','wee','chennah','lenggeng','lukut','nilai',
              'gemas','chembong','bembang','labu','juasseh','johol','jempol','palong','khaled',
              'khairy','kj','noh-omar','sri-tanjung','derhaka','status-quo',
              'gelanggang','amirudin','sufian','ridzuan','kamil','derhaka','kwap','efishery',
              'fathi-aris','rafizi','bersama','asas','kesinambungan','asyraf','menebuk',
              'button-badge','diraja','bendera','sole-opposition','lone-opposition',
              'dapan','dap-','pn-','-pn','/bn','umno','poster-boy','punching','bogeyman',
              'traitors','islamophobia','jana-wibawa','new-alliance','kekal-harapan',
              'razali','arul-kumar','danni-rais','bakri','siow','zamri','faizal',
              'fahmi','anwar','sri-menanti','kamarul','muhriz','mcmc','3r']
home_extracted = 0
for full in list(home_links):
    slug_hint = full.lower()
    if not any(k in slug_hint for k in url_prn_kw):
        continue
    rc, htmltxt = fetch(full, timeout=18)
    if rc != 0 or not htmltxt: continue
    soup_title = ''
    if HAVE_BS4:
        try:
            soup = BeautifulSoup(htmltxt, 'html.parser')
            t = soup.find('title')
            if t: soup_title = t.get_text(strip=True)
        except: pass
    if not soup_title:
        m = re.search(r'<title[^>]*>(.*?)</title>', htmltxt, re.S|re.I)
        if m: soup_title = re.sub(r'\s+',' ', html.unescape(m.group(1))).strip()
    if not soup_title: continue
    body = clean_html(htmltxt)
    if len(body) < 200: continue
    tags = hit(soup_title, body)
    isprn = is_prn(soup_title, body)
    if not (tags or isprn): continue
    datestr = ''
    m = re.search(r'(\d{4}-\d{2}-\d{2}[ T]\d{2}:\d{2})', htmltxt)
    if m: datestr = m.group(1)
    srcname = ('Awani' if 'awani' in full else ('Utusan' if 'utusan' in full else
              ('Sinar' if 'sinar' in full else ('MalayMail' if 'malaymail' in full else
              ('NST' if 'nst' in full else ('HarianMetro' if 'hmetro' in full else
              ('Star' if 'thestar' in full else ('Kosmo' if 'kosmo' in full else 'Homepage'))))))))
    fn_info = save_article(srcname, full, soup_title, datestr, body, tags, suffix='_home')
    if fn_info:
        fn, crit = fn_info
        if fn:
            results['saved'] += 1
            results['saved_files'].append(os.path.basename(fn))
            existing_urls.add(full)
            home_extracted += 1
            if crit: results['critical'] += 1
    time.sleep(0.3)
print(f"[4] Homepage extracted: {home_extracted}")

# ============================================================
# 5. The Vibes — new-article scan (125290-125330) for fresh content
# ============================================================
print("\n=== [5] THE VIBES NEW-ARTICLE SCAN (125290-125330) ===")
tv_new_fresh = 0
for aid in range(125290, 125331):
    for cat in ['news','opinion','business']:
        url = f"https://www.thevibes.com/articles/{cat}/{aid}"
        if url in existing_urls: continue
        rc, htmltxt = fetch(url, timeout=12)
        if rc==0 and len(htmltxt) > 3000 and 'Not Found' not in htmltxt[:800]:
            soup_title = ''
            m = re.search(r'<title[^>]*>(.*?)</title>', htmltxt, re.S|re.I)
            if m: soup_title = re.sub(r'\s+',' ', html.unescape(m.group(1))).strip().replace(' | The Vibes','').replace(' | Malaysia','')
            if not soup_title: continue
            body = clean_html(htmltxt)
            if len(body) < 200: continue
            tags = hit(soup_title, body)
            if not (tags or is_prn(soup_title, body)): continue
            datestr = ''
            m2 = re.search(r'(\d{4}-\d{2}-\d{2}[ T]\d{2}:\d{2})', htmltxt)
            if m2: datestr = m2.group(1)
            fn_info = save_article('TheVibes', url, soup_title, datestr, body, tags or ['PIR-07'], suffix='_thevibesfresh')
            if fn_info and fn_info[0]:
                results['saved'] += 1
                results['saved_files'].append(os.path.basename(fn_info[0]))
                existing_urls.add(url)
                tv_new_fresh += 1
                results['thevibes_new'].append({'id':aid,'title':soup_title[:90],'url':url,'tags':tags,'critical':fn_info[1],'fresh':True})
                if fn_info[1]: results['critical'] += 1
            break
    time.sleep(0.2)
print(f"[5] The Vibes fresh scan 125290-125330: {tv_new_fresh} found")

# ============================================================
# 6. Sinar article-ID scan (789120-789200) for fresh content
# ============================================================
print("\n=== [6] SINAR ID SCAN 789120-789200 ===")
sinar_saved = 0
sinar_new = []
for aid in range(789120, 789201):
    url = f"https://www.sinarharian.com.my/article/{aid}"
    rc, htmltxt = fetch(url, timeout=12)
    if rc != 0 or not htmltxt or len(htmltxt) < 1500:
        continue
    low = htmltxt[:2000].lower()
    if 'not found' in low or '404' in low[:300] or 'tidak dijumpai' in low:
        continue
    t = ''
    if HAVE_BS4:
        try:
            soup = BeautifulSoup(htmltxt, 'html.parser')
            tt = soup.find('title')
            if tt: t = tt.get_text(strip=True)
        except: pass
    if not t:
        m = re.search(r'<title[^>]*>(.*?)</title>', htmltxt, re.S|re.I)
        if m: t = re.sub(r'\s+',' ', html.unescape(m.group(1))).strip()
    if not t: continue
    body = clean_html(htmltxt)
    if len(body) < 300: continue
    tags = hit(t, body)
    isprn = is_prn(t, body)
    if not (tags or isprn): continue
    datestr = ''
    m = re.search(r'(\d{4}-\d{2}-\d{2}[ T]\d{2}:\d{2})', htmltxt)
    if m: datestr = m.group(1)
    sinar_new.append({'id':aid,'title':t,'url':url,'tags':tags,'datestr':datestr})
    if url in existing_urls: continue
    fn_info = save_article('sinarharian', url, t, datestr, body, tags, suffix='_targeted')
    if fn_info:
        fn, crit = fn_info
        if fn:
            results['saved'] += 1
            results['saved_files'].append(os.path.basename(fn))
            existing_urls.add(url)
            sinar_saved += 1
            if crit: results['critical'] += 1
    time.sleep(0.12)
print(f"[6] Sinar 789120-789200: {sinar_saved} saved, {len(sinar_new)} PRN hits")
results['sinar_targeted_hits'] = sinar_new

# ============================================================
# SAVE summaries
# ============================================================
with open(f"{BASE}/_gnews_headlines_20260721_predawn.json","w") as f:
    json.dump(results['gnews_headlines'], f, ensure_ascii=False, indent=1)
with open(f"{BASE}/_predawn_summary_20260721.json","w") as f:
    json.dump(results, f, ensure_ascii=False, indent=1, default=str)

print("\n" + "=" * 60)
print(f"PREDAWN CYCLE SUMMARY ({THIS_TS})")
print(f"  gnews queries: {results['gnews_queries']}")
print(f"  gnews items: {len(gnews_all)} (PRN hits: {len(results['gnews_headlines'])})")
print(f"  fresh post-cutoff: {results['fresh_after_cutoff']}")
print(f"  RSS feed items: {results['feed_items']} (PRN hits: {results['prn_hits']})")
print(f"  Articles saved TOTAL: {results['saved']}")
print(f"  CRITICAL: {results['critical']}")
print(f"  Duplicates: {results['duplicates']}")
print("SAVED FILES:")
for sf in results['saved_files']:
    print(f"  - {sf}")
print("FRESH GNEWS PRIORITY HITS (post-cutoff):")
for g in results['gnews_fresh_priority']:
    dstr = g['date'].isoformat() if g['date'] else '?'
    print(f"  - [{dstr}] {g['title']} ({g['src']}) tags={hit(g['title'])}")
    print(f"    {g['url']}")
print("THE VIBES NEW (this cycle):")
for t in results['thevibes_new']:
    print(f"  - [{t['id']}] {t['title']} | tags={t['tags']}{t.get('critical','')}")
print("SINAR TARGETED HITS (789120-789200):")
for s in sinar_new:
    print(f"  - [{s['id']}] {s['title'][:90]} | tags={s['tags']}")
print("=" * 60)
