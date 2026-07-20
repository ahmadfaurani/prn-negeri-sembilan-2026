#!/usr/bin/env python3
"""Dusk-cycle supplemental fetch: fresh Utusan articles discovered via sidebar links
referenced in the PH manifesto article (15:51-15:59 MYT 20 Jul)."""
import subprocess, re, datetime, json, os, html, time
from urllib.parse import urljoin

try:
    from bs4 import BeautifulSoup
    HAVE_BS4 = True
except Exception:
    BeautifulSoup = None
    HAVE_BS4 = False

BASE = "/home/p62operator/.openclaw/workspace-ns/04-DATA-AND-SOURCES/raw-scrapes/20260720"
THIS_TS = "20260720_dusk"
NOW_UTC = datetime.datetime.now(datetime.timezone.utc)
UA = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0 Safari/537.36"

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

def hit(title, body=''):
    t = (title or '').lower(); b = (body or '').lower()
    tag = []
    if any(k in t or k in b for k in PIR06): tag.append('PIR-06')
    if any(k in t or k in b for k in PIR07): tag.append('PIR-07')
    if any(k in t or k in b for k in PIR16): tag.append('PIR-16')
    return tag

def slugify(s):
    s = re.sub(r'[^a-z0-9]+','-', s.lower()).strip('-')
    return s[:80] or 'untitled'

def fetch(url, timeout=25):
    try:
        r = subprocess.run(['curl','-sS','-L','-m',str(timeout),'-A',UA,'--compressed', url],
                           capture_output=True, timeout=timeout+5)
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

# load existing URLs
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

# Fresh Utusan sidebar articles discovered
TARGET_URLS = [
    ('https://www.utusan.com.my/nasional/2026/07/tarik-sokongan-kepada-mb-bukan-derhaka/', 'Utusan'),
    ('https://www.utusan.com.my/nasional/2026/07/ph-selangor-yakin-hadapi-gelombang-kerjasama-bn-pn/', 'Utusan'),
    ('https://www.utusan.com.my/nasional/2026/07/kerjasama-bn-pn-umno-terengganu-tunggu-dan-lihat/', 'Utusan'),
    ('https://www.utusan.com.my/nasional/2026/07/tidak-mustahil-kerjasama-bn-pn-diteruskan-di-perlis/', 'Utusan'),
    ('https://www.utusan.com.my/nasional/politik/2026/07/kerjasama-bn-pn-mampu-rampas-selangor/', 'Utusan'),
    ('https://www.utusan.com.my/nasional/politik/2026/07/ada-sesuatu-yang-tak-kena-dalam-kerjasama-bn-ph/', 'Utusan'),
    ('https://www.utusan.com.my/nasional/2026/07/negeri-sembilan-penentu-kerjasama-pru16/', 'Utusan'),
]

saved = []
for url, src in TARGET_URLS:
    if url in existing_urls:
        print(f"SKIP (already have): {url}")
        continue
    rc, htmltxt = fetch(url, timeout=25)
    if rc != 0 or not htmltxt or len(htmltxt) < 1000:
        print(f"FAIL rc={rc}: {url}")
        continue
    # title
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
    if not t:
        print(f"NO TITLE: {url}"); continue
    body = clean_html(htmltxt)
    if len(body) < 200:
        print(f"SHORT BODY: {url}"); continue
    tags = hit(t, body)
    # date heuristics
    datestr = ''
    m = re.search(r'(\d{4}-\d{2}-\d{2}[ T]\d{2}:\d{2})', htmltxt)
    if m: datestr = m.group(1)
    if not datestr:
        m = re.search(r'(\d{1,2}\s+(?:Januari|Februari|Mac|April|Mei|Jun|Julai|Ogos|September|Oktober|November|Disember)\s+2026)', htmltxt)
        if m: datestr = m.group(1)
    sl = slugify(t)
    tagprefix = ('priority_' + '-'.join(tags) + '_') if tags else ''
    fn = f"{BASE}/{tagprefix}{src}_{sl}_{THIS_TS}_sidebar.md"
    n=1
    while os.path.exists(fn):
        fn = f"{BASE}/{tagprefix}{src}_{sl}_{THIS_TS}_sidebar_{n}.md"; n+=1
    # CRITICAL check
    crit = ''
    bc = body.lower()
    is_critical = False
    if 'PIR-06' in tags:
        if any(k in bc for k in ['pecat','expulsion','tarik diri','withdraw','keluar dari pn',
                                'kuorum','quorum to vote','lebih hebat','new coalition',
                                'remove bersatu','sack bersatu','dissolve pn','bubarkan pn']):
            if any(k in bc for k in ['pn','bersatu','perikatan','muhyiddin','kiandee','klawang']):
                crit = ' [CRITICAL]'; is_critical = True
    if 'PIR-16' in tags and not is_critical:
        if ('bersatu' in bc and 'sasar bentuk kerajaan negeri' in bc):
            crit = ' [CRITICAL]'; is_critical = True
        elif 'bersatu exit imminent' in bc:
            crit = ' [CRITICAL]'; is_critical = True
    md = [f"# {t}", "", f"**Source:** {src} | **URL:** {url}",
          f"**Date:** {datestr}", f"**Collected:** {NOW_UTC.isoformat()} (cycle {THIS_TS})",
          f"**PIR tags:** {', '.join(tags) if tags else 'none'}{crit}", "", "---", "", body]
    with open(fn,'w') as f:
        f.write('\n'.join(md))
    saved.append((os.path.basename(fn), t, tags, is_critical))
    existing_urls.add(url)
    print(f"SAVED: {t[:80]} | tags={tags}{crit}")
    time.sleep(0.3)

print(f"\nTotal saved: {len(saved)}")
for fn, t, tags, crit in saved:
    print(f"  - {fn}")
