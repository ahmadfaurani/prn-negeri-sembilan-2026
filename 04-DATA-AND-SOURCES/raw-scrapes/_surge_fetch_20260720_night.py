#!/usr/bin/env python3
"""Nomination-Day Surge cycle 20260720_night (collecting ~10:26 UTC / 18:26 MYT 20 Jul 2026).
Campaign Day 2-3 (MYT 20 Jul). Director-approved PIR-06/07/16 priority collection.
Cutoff: post-08:37 UTC 20 Jul 2026 (post-16:37 MYT 20 Jul) = prior dusk cycle end.
HIGHEST PRIORITY: PH MANIFESTO LAUNCH tonight ~18:00-20:00 MYT (confirmed by Aminuddin).
Sources: Awani RSS (full) + FMT RSS (full content:encoded) + HarianMetro RSS (full)
       + Google News RSS (PIR-targeted queries incl. mandatory CRITICAL-watch
         + PH manifesto launch coverage + Day-2/3 evening ceramah/walkabout)
       + NST/Star/MalayMail/Utusan/Sinar/Kosmo/HarianMetro/BH homepage slug-hint extraction
       + targeted Sinar article-ID scan (788720-788800) to recover fresh content.
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

BASE = "/home/p62operator/.openclaw/workspace-ns/04-DATA-AND-SOURCES/raw-scrapes/20260720"
os.makedirs(BASE, exist_ok=True)
THIS_TS = "20260720_night"
TODAY = "20260720"
# Cutoff = prior dusk cycle end (08:37 UTC 20 Jul = 16:37 MYT 20 Jul)
CUTOFF_UTC = datetime.datetime(2026, 7, 20, 8, 37, 0, tzinfo=datetime.timezone.utc)
NOW_UTC = datetime.datetime.now(datetime.timezone.utc)

UA = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0 Safari/537.36"

# ---- Keyword sets (PIR-06 / 07 / 16) ----
PIR06 = ['pn','bersatu','pecat','keluar','buang','tarik diri','toxic pn','termination','pn-mt',
         'supreme council','quorum','kuorum','kiandee','muhyiddin','hadi','hamzah','ridzuan ahmad',
         'new coalition','lebih hebat','wawasan','bn-pn','machinery sharing','joint ceramah',
         'gabung jentera','bersepadu','sole opposition','lone opposition','only true opposition',
         'ros',' registrar of societies']
PIR16 = ['narrative','dap acceptance','loke','mca biggest loser','mca rebuttal','wee','mah hang soon',
         'adat','melaka withdrawal','melaka ph-bn','bersatu exit','bersatu in disarray','kacau daun',
         'wan saiful','barking dogs','albert tei','graft trial','muhyiddin corruption',
         'majoriti mudah','mb after prn','sole opposition','sasar bentuk kerajaan','malay unity',
         'penyatuan undi melayu','makmal politik','not briefed','resign to attack',
         'bersatu sasar bentuk kerajaan negeri']
PIR07 = ['ampangan','juasseh','klawang','sikamat','linggi','chembong','bembang','labu','nilai',
         'sri tanjung','rantau','tok mat','pertang','jalaluddin','derhaka','battleground',
         'kerusi tumpuan','hot seat','ceramah','walkabout','ops-centre','manifesto launch',
         'chennah','lenggeng','bahau','lobak','bukit kepayang','paroi','lukut',
         'bagan pinang','gemas','repah','jeram padang','rahang','pilihan raya negeri',
         'negeri sembilan','prn','johol','jempol','palong','chuah','gemencheh','tampin']
GENERIC_PRN = ['negeri sembilan','prn negeri','pilihan raya negeri','tok mat','aminuddin',
               'anthony loke','wee ka siong','hadi awang','muhyiddin','hamzah zainudin',
               'khaled nordin','khairy jamaluddin','kj ','jalaluddin alias','manifesto']

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
    return any(k in t or k in b for k in GENERIC_PRN) or bool(hit(title, body))

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
                        'div.page-content']:
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
        if any(k in bc for k in ['pecat','expulsion','tarik diri','withdraw','keluar dari pn',
                                'kuorum','quorum to vote','lebih hebat','new coalition',
                                'remove bersatu','sack bersatu','dissolve pn','bubarkan pn',
                                'formal expulsion','expulsion notice','candidate withdrawal',
                                'bersatu withdrawal','ros revokes','registrar of societies',
                                'pdm klawang buka semula','pdm klawang reopen']):
            # require PN/Bersatu co-occurrence to avoid false positives
            if any(k in bc for k in ['pn','bersatu','perikatan','muhyiddin','kiandee','klawang']):
                crit = ' [CRITICAL]'; is_critical = True
    if 'PIR-16' in tags and not is_critical:
        # require "bersatu" co-occurrence for "sasar bentuk kerajaan negeri"
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
           'duplicates':0,'gnews_headlines':[], 'rss_articles':[]}

# existing slugs to dedup (check 20260720 + 20260719 dir for cross-day dedup)
existing_titles = set()
existing_basenames = set()
existing_urls = set()
for d in ['20260720','20260719']:
    p = f"/home/p62operator/.openclaw/workspace-ns/04-DATA-AND-SOURCES/raw-scrapes/{d}"
    if os.path.isdir(p):
        for fn in os.listdir(p):
            if fn.endswith('.md'):
                existing_titles.add(fn)
                core = re.sub(r'_(20260720_(?:morning|midday|afternoon|evening|midafternoon|lateafternoon|dusk|night)|20260719_[^_]*)(?:_rss|_home|_targeted)?\.md$','.md', fn)
                existing_basenames.add(core)
                core2 = re.sub(r'_(20260720|20260719)[^_]*_?(?:rss|home|targeted)?\.md$','.md', fn)
                existing_basenames.add(core2)
# load existing URLs from article files
for d in ['20260720','20260719']:
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

print(f"[0] dedup baseline: {len(existing_titles)} existing md files, "
      f"{len(existing_basenames)} normalized cores, {len(existing_urls)} URLs")
print(f"[0] cutoff: {CUTOFF_UTC.isoformat()} (16:37 MYT 20 Jul) | now: {NOW_UTC.isoformat()}")

# ============================================================
# 1. GOOGLE NEWS RSS — PIR-targeted queries
# ============================================================
GNEWS_QUERIES = [
    # PIR-06 [CRITICAL] watch (mandatory)
    'Bersatu pecat PN Negeri Sembilan',
    'Bersatu tarik diri PN kuorum',
    'PN Supreme Council Bersatu Negeri Sembilan',
    'lebih hebat coalition PN Bersatu Negeri Sembilan',
    'kuorum Bersatu PN Negeri Sembilan',
    'Bersatu calon tarik diri Negeri Sembilan',
    'Bersatu sole opposition parliament Negeri Sembilan',
    'PDM Klawang buka semula Negeri Sembilan',
    'Klawang PDM reopen Negeri Sembilan',
    'RoS PN Bersatu Negeri Sembilan',
    'Kiandee quorum Bersatu Negeri Sembilan',
    'Bersatu PN new coalition formalization',
    # PIR-06 cooperation + machinery
    'BN PN machinery sharing Negeri Sembilan gabung jentera',
    'Wawasan Ridzuan Ahmad Negeri Sembilan',
    'Gerakan sacking Bersatu candidate Rahang Negeri Sembilan',
    'Tang Jay Son Bersatu Rahang Negeri Sembilan',
    # PIR-16 narratives
    'Bersatu kacau daun Negeri Sembilan',
    'Bersatu sasar bentuk kerajaan negeri',
    'makmal politik PRU16 Anwar',
    'Loke MCA biggest loser Negeri Sembilan',
    'MCA rebuttal Wee BN PN Negeri Sembilan',
    'Melaka DAP withdrawal PH BN fracture',
    'Wan Saiful barking dogs Negeri Sembilan',
    'Muhyiddin corruption graft trial Bersatu',
    'penyatuan undi Melayu Negeri Sembilan',
    'Tok Mat resign to attack unity partners',
    'Bersatu kian tidak relevan krisis identiti',
    'Kamil Munim jet rasmi PKR',
    'Marzuki Muhyiddin Hamzah toxic PN',
    # PIR-07 battlegrounds + Day-2/3 evening — MANIFESTO FOCUS
    'PH manifesto launch Negeri Sembilan 20 Jul',
    'manifesto PH Negeri Sembilan dilancarkan',
    'Amirudin Shari pelancaran manifesto PH Negeri Sembilan',
    'manifesto PH Negeri Sembilan kesinambungan',
    'Negeri Sembilan PRN 2026 manifesto BN PH',
    'PH manifesto malam Negeri Sembilan Amirudin',
    'manifesto PH Negeri Sembilan B40 M40',
    'BN manifesto launch Linggi Negeri Sembilan 24 Jul',
    'Negeri Sembilan ceramah malam walkabout',
    'Negeri Sembilan ceramah malam ops-centre 20 Jul',
    'Tok Mat Rantau Negeri Sembilan ceramah',
    'Anthony Loke Chennah Negeri Sembilan',
    'Aminuddin Harun Linggi Sikamat',
    'Pertang Jalaluddin derhaka Negeri Sembilan',
    'Khaled Nordin Bersatu Johor Negeri Sembilan',
    'Khairy Jamaluddin makmal politik Selangor',
    'Noh Omar blue wave Selangor BN PN',
    'Hamzah Zainudin Wawasan PAS toxic Negeri Sembilan',
    'DUN Chuah pencalonan Aminuddin Negeri Sembilan',
    'PKR Mandarin Pertang BN Negeri Sembilan',
    'DUN Pilah calon wanita Negeri Sembilan',
    '21 DUN tiga penjuru Negeri Sembilan',
    'pertelingkahan mulut penyokong parti Negeri Sembilan',
    'Hadi Asyraf Wajdi berjabat tangan',
    'Akmal Saleh penyatuan BN Negeri Sembilan',
    'Zahid Johor spirit BN Negeri Sembilan',
    'Tok Mat adat politik Negeri Sembilan',
    'MCA sec-gen campaign Negeri Sembilan Focus Malaysia',
    'DAP Melaka BN PN pact',
    # generic catch
    'Negeri Sembilan PRN 2026',
    'PRN Negeri Sembilan pilihan raya',
    'Bersatu PN Negeri Sembilan 2026',
    'Negeri Sembilan pilihan raya negeri calon',
    'Hadi Awang Zahid BN PN Negeri Sembilan',
    'Khalid Samad Akmal Negeri Sembilan resign',
    'Negeri Sembilan calon 5 penjuru',
    'polis kertas siasatan Kuala Klawang Jelebu',
    'Anwar amaran menteri kempen PRN Negeri Sembilan',
    'Sinar Harian PRN Negeri Sembilan 2026',
    # NEW night-cycle additions — PH manifesto launch coverage + evening events
    'manifesto PH dilancarkan Negeri Sembilan malam',
    'PH Negeri Sembilan manifesto 36 kerusi',
    'Aminuddin manifesto PH Negeri Sembilan 20 Jul malam',
    'Anthony Loke manifesto PH Negeri Sembilan',
    'Amirudin Shari manifesto PH Negeri Sembilan',
    'manifesto kesinambungan kemakmuran PH Negeri Sembilan',
    'PRN Negeri Sembilan kempen malam 20 Jul',
    'PRN Negeri Sembilan ceramah 20 Jul malam',
    'Negeri Sembilan calon kempen malam 20 Jul',
    'Tok Mat Mohamad Hasan Rantau ceramah malam',
    'Negeri Sembilan pilihan raya 20 Jul malam',
    'PRN N9 ceramah malam PH PN BN',
    'PRN Negeri Sembilan derhaka PH BN Palong',
    'derhaka Palong BN calon Negeri Sembilan',
    'Rafizi Bersama Melaka Negeri Sembilan',
    'Fathi Aris PH Bersatu Negeri Sembilan',
    'Akmal Saleh DAP ketandusan idea Negeri Sembilan',
    'MCA KWAP eFishery Chan Quin Er Negeri Sembilan',
    'Negeri Sembilan lelaki maut pasang bendera Rantau',
    'Negeri Sembilan bahan kempen rosak Palong Chembong',
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

results['gnews_total_items'] = len(gnews_all)
print(f"[1] gnews: {results['gnews_queries']} queries -> {len(gnews_all)} items, "
      f"{len(results['gnews_headlines'])} PRN/priority hits, {results['fresh_after_cutoff']} fresh")

# ============================================================
# 2. RSS FEEDS — Awani (full) + FMT (full content:encoded) + HarianMetro (full) + others
# ============================================================
RSS_FEEDS = [
    ('Awani', 'https://www.astroawani.com/rss.xml'),
    ('Awani-Politik', 'https://www.astroawani.com/rss/berita-politik.xml'),
    ('FMT', 'https://www.freemalaysiatoday.com/feed/'),
    ('NST', 'https://www.nst.com.my/feed/rss/nation'),
    ('NST-Politik', 'https://www.nst.com.my/feed/rss/politics'),
    ('MalayMail', 'https://www.malaymail.com/rss'),
    ('Sinar', 'https://www.sinarharian.com.my/rss'),
    ('Utusan', 'https://www.utusan.com.my/rss.xml'),
    ('HarianMetro', 'https://www.hmetro.com.my/feed'),
    ('BH', 'https://www.bharian.com.my/rss.xml'),
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

# ============================================================
# 3. Save RSS full-text articles (only fresh OR not already captured)
# ============================================================
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

print(f"[3] RSS full-text saved: {rss_saved}")

# ============================================================
# 4. For gnews FRESH priority hits + RSS no-full items: extract article from URL
# ============================================================
to_extract = []
fresh_gnews = 0
for g in results['gnews_headlines']:
    if g['url'] in existing_urls:
        continue
    if g['fresh'] and g['tags']:
        to_extract.append(('gnews', g['src'], g['title'], g['url'], g.get('date',''), g['tags']))
        fresh_gnews += 1
# RSS items without full text (fresh only)
for a in feed_articles:
    if not a['has_full'] and a['fresh'] and a['url'] not in existing_urls:
        to_extract.append((a['src'], a['src'], a['title'], a['url'],
                           a['date'].isoformat() if a['date'] else '', a['tags']))

print(f"[4] URLs to extract full text: {len(to_extract)} (fresh gnews: {fresh_gnews})")
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

print(f"[4] Extracted full-text from URLs: {extracted}")

# ============================================================
# 5. Homepage headline scan — NST, Star, MalayMail, Utusan, Sinar, Kosmo, HarianMetro, BH, mStar
# ============================================================
HOME_PAGES = [
    ('NST', 'https://www.nst.com.my/news/nation'),
    ('NST', 'https://www.nst.com.my/news/politics'),
    ('Star', 'https://www.thestar.com.my/news/nation'),
    ('Star', 'https://www.thestar.com.my/news/politics'),
    ('MalayMail', 'https://www.malaymail.com/news/malaysia'),
    ('MalayMail', 'https://www.malaymail.com/news/politics'),
    ('Utusan', 'https://www.utusan.com.my/terkini'),
    ('Utusan', 'https://www.utusan.com.my/nasional'),
    ('Utusan', 'https://www.utusan.com.my/politik'),
    ('HarianMetro', 'https://www.hmetro.com.my/terkini'),
    ('HarianMetro', 'https://www.hmetro.com.my/berita'),
    ('BH', 'https://www.bharian.com.my/terkini'),
    ('Sinar', 'https://www.sinarharian.com.my/'),
    ('Sinar', 'https://www.sinarharian.com.my/politik'),
    ('Kosmo', 'https://www.kosmo.com.my/'),
    ('Kosmo', 'https://www.kosmo.com.my/terkini'),
    ('mStar', 'https://www.thestar.com.my/mstar'),
]
home_links = set()
for src, hurl in HOME_PAGES:
    rc, htmltxt = fetch(hurl, timeout=20)
    if rc != 0 or not htmltxt:
        print(f"[5] {src} {hurl}: rc={rc}")
        continue
    links = re.findall(r'href=["\']([^"\']+)["\']', htmltxt)
    cnt = 0
    for lk in links:
        full = urljoin(hurl, lk)
        if full in seen_urls or full in home_links or full in existing_urls:
            continue
        if not re.search(r'/(news|berita|article|nasional|politik|nation|politik|terkini)[/\-]', full, re.I):
            continue
        if re.search(r'\.(css|js|jpg|png|svg|ico)(\?|$)', full, re.I): continue
        home_links.add(full)
        cnt += 1
    print(f"[5] {src} {hurl}: {cnt} candidate links")

url_prn_kw = ['negeri-sembilan','prn','bersatu','loke','tok-mat','aminuddin','sikamat','ampangan',
              'klawang','linggi','rantau','manifesto','ceramah','mca','kiandee','muhyiddin',
              'hamzah','hadi','jalaluddin','pertang','wawasan','gabung-jentera','bersepadu',
              'kacau-daun','makmal-politik','melaka','wan-saiful','albert-tei','wee','machang',
              'chennah','lenggeng','lukut','nilai','gemas','chembong','bembang','labu','juasseh',
              'johol','jempol','palong','khaled','khairy','kj','noh-omar','sri-tanjung',
              '5-penjuru','limpahan','suarakeadilan','arul-kumar','zamani','berjasa','chuah',
              'gemencheh','repah','tampin','rahang','paroi','bahau','lobak','pilah',
              'akmal','zahid','amirudin','sufian','ridzuan','marzuki','kamil','tang-jay-son',
              'gerakan','wong-chia-zhen','nor-azman','tun-faisal','razali','bakri-sawir',
              'danni-rais','muhammad-adib','siow-kong','faizal-ramli','zamri','derhaka',
              'kwap','efishery','fathi-aris','rafizi','bersama']
home_extracted = 0
for full in list(home_links):
    slug_hint = full.lower()
    if not any(k in slug_hint for k in url_prn_kw):
        continue
    rc, htmltxt = fetch(full, timeout=20)
    if rc != 0 or not htmltxt: continue
    soup_title = ''
    if HAVE_BS4 and BeautifulSoup is not None:
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
    # date heuristics
    datestr = ''
    m = re.search(r'(\d{4}-\d{2}-\d{2}[ T]\d{2}:\d{2})', htmltxt)
    if m: datestr = m.group(1)
    fn_info = save_article('Utusan' if 'utusan' in full else
                           ('Sinar' if 'sinar' in full else
                            ('MalayMail' if 'malaymail' in full else
                             ('NST' if 'nst' in full else
                              ('Star' if 'star' in full else
                               ('HarianMetro' if 'hmetro' in full else
                                ('BH' if 'bharian' in full else 'Homepage')))))),
                           full, soup_title, datestr, body, tags, suffix='_home')
    if fn_info:
        fn, crit = fn_info
        if fn:
            results['saved'] += 1
            results['saved_files'].append(os.path.basename(fn))
            existing_urls.add(full)
            home_extracted += 1
            if crit: results['critical'] += 1
    time.sleep(0.3)

print(f"[5] Homepage extracted: {home_extracted}")

# ============================================================
# 6. Targeted Sinar article-ID scan (788720-788800) for fresh content
# ============================================================
sinar_saved = 0
sinar_new = []
for aid in range(788720, 788801):
    url = f"https://www.sinarharian.com.my/article/{aid}"
    rc, htmltxt = fetch(url, timeout=15)
    if rc != 0 or not htmltxt or len(htmltxt) < 1500:
        continue
    # detect 404 / not found
    low = htmltxt[:2000].lower()
    if 'not found' in low or '404' in low or 'tidak dijumpai' in low or 'artikel tidak' in low:
        continue
    t = ''
    if HAVE_BS4 and BeautifulSoup is not None:
        try:
            soup = BeautifulSoup(htmltxt, 'html.parser')
            t = soup.find('title')
            if t: t = t.get_text(strip=True)
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
    # date heuristics
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
    time.sleep(0.15)

print(f"[6] Sinar targeted scan 788720-788800: {sinar_saved} saved, {len(sinar_new)} PRN hits found")

# ============================================================
# SAVE gnews headlines JSON + summary
# ============================================================
with open(f"{BASE}/_gnews_headlines_20260720_night.json","w") as f:
    json.dump(results['gnews_headlines'], f, ensure_ascii=False, indent=1)

results['sinar_targeted_hits'] = sinar_new
with open(f"{BASE}/_night_summary_20260720.json","w") as f:
    json.dump(results, f, ensure_ascii=False, indent=1, default=str)

print("=" * 60)
print(f"NIGHT CYCLE SUMMARY ({THIS_TS})")
print(f"  gnews queries: {results['gnews_queries']}")
print(f"  gnews items: {results['gnews_total_items']} (PRN hits: {len(results['gnews_headlines'])})")
print(f"  fresh post-cutoff: {results['fresh_after_cutoff']}")
print(f"  RSS feed items: {results['feed_items']} (PRN hits: {results['prn_hits']})")
print(f"  Articles saved: {results['saved']}")
print(f"  CRITICAL: {results['critical']}")
print(f"  Duplicates: {results['duplicates']}")
print("SAVED FILES:")
for sf in results['saved_files']:
    print(f"  - {sf}")
print("SINAR TARGETED HITS (788720-788800):")
for s in sinar_new:
    print(f"  - [{s['id']}] {s['title'][:90]} | tags={s['tags']}")
print("=" * 60)
