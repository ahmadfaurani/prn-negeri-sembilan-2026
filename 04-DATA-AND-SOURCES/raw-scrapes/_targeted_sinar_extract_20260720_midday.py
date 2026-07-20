#!/usr/bin/env python3
"""Targeted extraction of 6 high-value Sinar articles found via ID scan (midday cycle)."""
import subprocess, re, os
from urllib.parse import urljoin

try:
    from bs4 import BeautifulSoup
    HAVE_BS4 = True
except Exception:
    BeautifulSoup = None; HAVE_BS4 = False

BASE = "/home/p62operator/.openclaw/workspace-ns/04-DATA-AND-SOURCES/raw-scrapes/20260720"
THIS_TS = "20260720_midday"
UA = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120 Safari/537.36"

ARTICLES = [
    (788523, "https://www.sinarharian.com.my/article/788523/berita/politik/formula-kerjasama-bn-pn-perlu-diperluas-ke-selangor-pemuda-umno-kapar"),
    (788529, "https://www.sinarharian.com.my/article/788529/berita/politik/kalau-orang-dah-tak-suka-buat-apa-nak-tunggu-khaled-nordin"),
    (788548, "https://www.sinarharian.com.my/article/788548/berita/politik/ph-jual-prestasi-bn-pn-laung-penyatuan-melayu-islam"),
    (788549, "https://www.sinarharian.com.my/article/788549/berita/politik/umno-pas-tiada-yang-mustahil-dalam-politik"),
    (788573, "https://www.sinarharian.com.my/article/788573/berita/politik/ada-sesuatu-yang-tak-kena-dalam-kerajaan-perpaduan-kj"),
    (788575, "https://www.sinarharian.com.my/article/788575/berita/politik/bukan-janji-bulan-dan-bintang-tetapi-rekod-dan-iltizam-johol-calon-bn-dun-johol"),
]

PIR06 = ['pn','bersatu','pecat','keluar','buang','tarik diri','toxic pn','termination','pn-mt',
         'supreme council','quorum','kuorum','kiandee','muhyiddin','hadi','hamzah','ridzuan ahmad',
         'new coalition','lebih hebat','wawasan','bn-pn','machinery sharing','joint ceramah',
         'gabung jentera','bersepadu','sole opposition','lone opposition','only true opposition']
PIR16 = ['narrative','dap acceptance','loke','mca biggest loser','mca rebuttal','wee','mah hang soon',
         'adat','melaka withdrawal','melaka ph-bn','bersatu exit','bersatu in disarray','kacau daun',
         'wan saiful','barking dogs','albert tei','graft trial','muhyiddin corruption',
         'majoriti mudah','mb after prn','sole opposition','sasar bentuk kerajaan','malay unity',
         'penyatuan undi melayu','makmal politik','not briefed','resign to attack']
PIR07 = ['ampangan','juasseh','klawang','sikamat','linggi','chembong','bembang','labu','nilai',
         'sri tanjung','rantau','tok mat','pertang','jalaluddin','derhaka','battleground',
         'kerusi tumpuan','hot seat','ceramah','walkabout','ops-centre','manifesto launch',
         'chennah','lenggeng','bahau','lobak','bukit kepayang','paroi','lukut',
         'bagan pinang','gemas','repah','jeram padang','rahang','pilihan raya negeri',
         'negeri sembilan','prn','johol','iltizam']

def hit(title, body=''):
    t=(title or '').lower(); b=(body or '').lower(); tag=[]
    if any(k in t or k in b for k in PIR06): tag.append('PIR-06')
    if any(k in t or k in b for k in PIR07): tag.append('PIR-07')
    if any(k in t or k in b for k in PIR16): tag.append('PIR-16')
    return tag

def slugify(s):
    s = re.sub(r'[^a-z0-9]+','-', s.lower()).strip('-')
    return s[:80] or 'untitled'

def fetch(url, timeout=20):
    r = subprocess.run(['curl','-sS','-L','-m',str(timeout),'-A',UA,'--compressed', url],
                      capture_output=True, timeout=timeout+5)
    return r.returncode, r.stdout.decode('utf-8','replace')

def clean_html(htmltxt):
    if HAVE_BS4:
        try:
            soup = BeautifulSoup(htmltxt, 'html.parser')
            for tag in soup(['script','style','noscript','iframe','svg','header','footer','nav']):
                tag.decompose()
            for sel in ['article','main','div.post-content','div.article-content',
                        'div.entry-content','div.content','div.body-content','div#article-body',
                        'div.story-content','div.field-body','div.article-body','div.detail-body']:
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

import datetime
NOW_UTC = datetime.datetime.now(datetime.timezone.utc)
existing = set(os.listdir(BASE))

saved = []
for aid, url in ARTICLES:
    # try the full URL first, fall back to bare /article/id
    rc, htmltxt = fetch(url, 18)
    if rc != 0 or len(htmltxt) < 500:
        rc, htmltxt = fetch(f"https://www.sinarharian.com.my/article/{aid}", 18)
    if rc != 0 or len(htmltxt) < 500:
        print(f"{aid}: fetch failed rc={rc}"); continue
    title = ''
    if HAVE_BS4:
        try:
            s = BeautifulSoup(htmltxt,'html.parser'); tt = s.find('title')
            title = tt.get_text(strip=True).replace(' - Sinar Harian','').strip() if tt else ''
        except: pass
    if not title:
        title = f"Sinar article {aid}"
    body = clean_html(htmltxt)
    if len(body) < 150:
        print(f"{aid}: body too short ({len(body)})"); continue
    tags = hit(title, body)
    sl = slugify(title)
    # dedup
    already = any(sl in fn for fn in existing)
    if already:
        print(f"{aid}: DUP slug already exists -> {sl}"); continue
    tagprefix = ('priority_' + '-'.join(tags) + '_') if tags else ''
    fn = f"{BASE}/{tagprefix}sinarharian_{sl}_{THIS_TS}_home.md"
    crit = ''
    if 'PIR-06' in tags:
        bc = body.lower()
        if any(k in bc for k in ['pecat','expulsion','tarik diri','withdraw','keluar dari pn',
                                'kuorum','quorum to vote','lebih hebat','new coalition',
                                'remove bersatu','sack bersatu','dissolve pn','bubarkan pn']):
            crit = ' [CRITICAL]'
    if 'PIR-16' in tags:
        bc = body.lower()
        if any(k in bc for k in ['bersatu exit imminent','sasar bentuk kerajaan negeri',
                                'bersatu kacau daun','makmal politik']):
            crit = crit or ' [CRITICAL]'
    md = [f"# {title}", "", f"**Source:** sinarharian | **URL:** {url}",
          f"**Date:** (Sinar article {aid})", f"**Collected:** {NOW_UTC.isoformat()} (cycle {THIS_TS})",
          f"**PIR tags:** {', '.join(tags) if tags else 'none'}{crit}", "", "---", "", body]
    with open(fn,'w') as f:
        f.write('\n'.join(md))
    saved.append((aid, os.path.basename(fn), tags, ('CRITICAL' in crit)))
    print(f"{aid}: SAVED -> {os.path.basename(fn)} tags={tags} crit={'CRITICAL' in crit}")

print(f"\nTotal saved: {len(saved)}")
