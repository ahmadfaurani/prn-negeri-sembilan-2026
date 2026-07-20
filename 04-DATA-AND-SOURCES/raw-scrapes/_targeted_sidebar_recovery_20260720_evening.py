#!/usr/bin/env python3
"""Targeted Sinar sidebar-article recovery for 20260720_evening cycle.
Fetches articles referenced in the Wee Ka Siong (788589) sidebar that are
PRN-NS relevant and not yet captured: Onn Hafiz, Mohd Syahir, Ka Siong BN-PN,
Senarai calon, Loke 'biggest loser' originals from new outlets.
"""
import subprocess, re, os, sys
from urllib.parse import quote as url_quote

BASE = "/home/p62operator/.openclaw/workspace-ns/04-DATA-AND-SOURCES/raw-scrapes/20260720"
THIS_TS = "20260720_evening"
UA = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0 Safari/537.36"

try:
    from bs4 import BeautifulSoup
except Exception:
    BeautifulSoup = None

def fetch(url, timeout=20):
    try:
        r = subprocess.run(['curl','-sS','-L','-m',str(timeout),'-A',UA,'--compressed', url],
                           capture_output=True, timeout=timeout+5)
        return r.returncode, r.stdout.decode('utf-8','replace')
    except Exception:
        return -1, ''

def clean_html(htmltxt):
    if BeautifulSoup is not None:
        try:
            soup = BeautifulSoup(htmltxt, 'html.parser')
            for tag in soup(['script','style','noscript','iframe','svg','header','footer','nav']):
                tag.decompose()
            for sel in ['article','main','div.post-content','div.article-content',
                        'div.entry-content','div.content','div.body-content','div#article-body',
                        'div.story-content','div.field-body','div.article-body',
                        'div.detail-content','div.news-content','div.isi-berita','div.kandungan']:
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

def slugify(s):
    return re.sub(r'[^a-z0-9]+','-', s.lower()).strip('-')[:80] or 'untitled'

# Load existing URLs to dedup
existing_urls = set()
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

print(f"existing URLs: {len(existing_urls)}")

# Step 1: Get the Wee article (788589) raw HTML to extract related-article hrefs
wee_url = "https://www.sinarharian.com.my/article/788589/berita/politik/terima-kasih-anthony-loke-ingatkan-mca---ka-siong"
rc, htmltxt = fetch(wee_url, timeout=20)
related_hrefs = []
if rc == 0 and htmltxt:
    # find all article hrefs
    hrefs = re.findall(r'href="(https://www\.sinarharian\.com\.my/article/\d+/[^"]+)"', htmltxt)
    seen = set()
    for h in hrefs:
        if h == wee_url or h in seen: continue
        seen.add(h)
        related_hrefs.append(h)
print(f"related-article hrefs found in Wee article: {len(related_hrefs)}")
for h in related_hrefs[:25]:
    print("  ", h)

# Step 2: Google News RSS searches for specific sidebar-referenced articles
GNEWS_QUERIES = [
    'Onn Hafiz bawa formula kemenangan BN Johor Negeri Sembilan',
    'Mohd Syahir Pemuda PH Exco Perak Pahang letak jawatan',
    'Kerjasama BN-PN elak pecah undi Ka Siong',
    'Senarai penuh 103 calon PRN Negeri Sembilan 2026',
    'Onn Hafiz Negeri Sembilan BN Johor formula',
    'Loke vows win Malay votes MCA biggest loser',
    'MCA bars youth sec-general Negeri Sembilan election',
    'Hadi Awang Asyraf Wajdi handshake Negeri Sembilan',
]
import xml.etree.ElementTree as ET
gnews_urls = []
for q in GNEWS_QUERIES:
    url = "https://news.google.com/rss/search?q=" + url_quote(q) + "&hl=en-MY&gl=MY&ceid=MY:en"
    rc, txt = fetch(url, timeout=20)
    if rc != 0 or not txt or '<item>' not in txt:
        continue
    try:
        root = ET.fromstring(txt.encode('utf-8'))
        for it in root.iter('item'):
            title_el = it.find('title'); link_el = it.find('link')
            t = (title_el.text or '') if title_el is not None else ''
            l = (link_el.text or '') if link_el is not None else ''
            if l and l not in existing_urls:
                gnews_urls.append((t, l, q))
    except Exception: pass
    import time; time.sleep(0.3)

print(f"\ngnews candidate URLs (not in existing): {len(gnews_urls)}")
for t, l, q in gnews_urls[:20]:
    print(f"  [{q[:30]}] {t[:90]}")

# Step 3: Candidate URLs to fetch = Sinar related hrefs + gnews candidates
# Filter to PRN-NS-relevant
prn_kw = ['negeri-sembilan','negeri sembilan','prn','bersatu','loke','tok-mat','aminuddin',
          'sikamat','ampangan','klawang','linggi','rantau','manifesto','mca','kiandee',
          'muhyiddin','hamzah','hadi','jalaluddin','pertang','wawasan','kacau-daun',
          'makmal-politik','melaka','wan-saiful','wee','chennah','lenggeng','lukut','nilai',
          'gemas','chembong','bembang','labu','juasseh','johol','jempol','palong','khaled',
          'khairy','kj','noh-omar','arul-kumar','on-hafiz','onn-hafiz','syahir','ka-siong',
          'calon','103-calon','hadi-awang','asyraf-wajdi','handshake']

candidates = []
for h in related_hrefs:
    slug_hint = h.lower()
    if any(k in slug_hint for k in prn_kw):
        candidates.append(('sinar-related', h))
for t, l, q in gnews_urls:
    slug_hint = (t + ' ' + l).lower()
    if any(k in slug_hint for k in prn_kw):
        candidates.append((q, l, t))

# dedup candidates by URL
seen_cand = set()
uniq_cands = []
for c in candidates:
    key = c[1] if len(c) > 1 else c[0]
    if key in seen_cand or key in existing_urls: continue
    seen_cand.add(key)
    uniq_cands.append(c)

print(f"\n=== {len(uniq_cands)} unique candidate URLs to fetch ===")
saved = 0
for c in uniq_cands[:25]:
    if len(c) == 2:
        src_label, url = c
        title_hint = url
    else:
        src_label, url, title_hint = c
    if url in existing_urls:
        continue
    rc, htxt = fetch(url, timeout=20)
    if rc != 0 or not htxt or len(htxt) < 500:
        print(f"  SKIP (fetch fail): {url[:80]}")
        continue
    # extract title
    title = ''
    if BeautifulSoup is not None:
        try:
            s = BeautifulSoup(htxt,'html.parser')
            tt = s.find('title')
            title = tt.get_text(strip=True) if tt else ''
        except: pass
    if not title:
        m = re.search(r'<title[^>]*>([^<]+)</title>', htxt, re.I)
        title = m.group(1).strip() if m else title_hint
    body = clean_html(htxt)
    if len(body) < 200:
        print(f"  SKIP (body too short): {title[:70]}")
        continue
    # PRN relevance check
    bc = (title + ' ' + body).lower()
    if not any(k in bc for k in ['negeri sembilan','prn','bersatu','loke','tok mat','aminuddin',
                                 'mca','kiandee','muhyiddin','hamzah','hadi','jalaluddin',
                                 'pertang','wawasan','chennah','linggi','klawang','sikamat',
                                 'rantau','nilai','johol','khaled','khairy','noh omar',
                                 'wee ka siong','ka siong','on hafiz','onn hafiz','syahir',
                                 'calon','manifesto','johor','selangor']):
        print(f"  SKIP (not PRN-relevant): {title[:70]}")
        continue
    # Determine tags
    tags = []
    PIR06 = ['pn','bersatu','pecat','kuorum','kiandee','muhyiddin','hadi','hamzah','wawasan',
             'bn-pn','machinery','sole opposition','lebih hebat','ros','jalaluddin','pertang',
             'ka siong','wee','mca','noh omar','khairy','kj','khaled','on hafiz','onn hafiz',
             'syahir','hadi awang','asyraf wajdi']
    PIR16 = ['loke','mca','wee','kacau daun','makmal politik','sasar bentuk','penyatuan undi melayu',
             'muhyiddin corruption','majoriti mudah','melaka','wan saiful','calon','manifesto',
             'sole opposition']
    PIR07 = ['ampangan','juasseh','klawang','sikamat','linggi','chembong','bembang','labu','nilai',
             'sri tanjung','rantau','tok mat','pertang','jalaluddin','chennah','lenggeng','johol',
             'jempol','palong','gemas','ceramah','walkabout','manifesto','calon']
    bl = (title + ' ' + body).lower()
    if any(k in bl for k in PIR06): tags.append('PIR-06')
    if any(k in bl for k in PIR07): tags.append('PIR-07')
    if any(k in bl for k in PIR16): tags.append('PIR-16')
    if not tags:
        tags = ['PIR-07']
    # Determine source
    if 'sinarharian' in url.lower(): src = 'sinarharian'
    elif 'malaymail' in url.lower(): src = 'malaymail'
    elif 'nst.com' in url.lower(): src = 'nst'
    elif 'thestar' in url.lower(): src = 'star'
    elif 'utusan' in url.lower(): src = 'utusan'
    elif 'freemalaysiatoday' in url.lower(): src = 'FMT'
    elif 'astroawani' in url.lower(): src = 'Awani'
    elif 'kosmo' in url.lower(): src = 'kosmo'
    elif 'malaysiakini' in url.lower(): src = 'malaysiakini'
    elif 'thevibes' in url.lower(): src = 'thevibes'
    elif 'focusmalaysia' in url.lower(): src = 'focusmalaysia'
    elif 'edgemy' in url.lower() or 'theedge' in url.lower(): src = 'theedge'
    elif 'thesun' in url.lower(): src = 'thesun'
    elif 'newswav' in url.lower(): src = 'newswav'
    else:
        try: src = url.split('/')[2].replace('www.','').split('.')[0]
        except: src = 'web'
    tagprefix = 'priority_' + '-'.join(tags) + '_'
    sl = slugify(title)
    fn = f"{BASE}/{tagprefix}{src}_{sl}_{THIS_TS}_targeted.md"
    n = 1
    while os.path.exists(fn):
        fn = f"{BASE}/{tagprefix}{src}_{sl}_{THIS_TS}_targeted_{n}.md"; n += 1
    md = [f"# {title}", "",
          f"**Source:** {src} | **URL:** {url}",
          f"**Date:** ",
          f"**Collected:** (cycle {THIS_TS} targeted sidebar-recovery)",
          f"**PIR tags:** {', '.join(tags)}",
          "", "---", "", body]
    with open(fn,'w') as f:
        f.write('\n'.join(md))
    saved += 1
    existing_urls.add(url)
    print(f"  SAVED: {src} | {title[:80]}")

print(f"\n=== Targeted recovery saved: {saved} articles ===")
