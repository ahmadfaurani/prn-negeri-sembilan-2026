#!/usr/bin/env python3
"""Freshness probe for late-afternoon cycle 20260720 (~15:20 MYT / 07:20 UTC).
Cutoff = 05:55 UTC (13:55 MYT) = midafternoon cycle end.
Quick probe: FMT RSS + Awani RSS + a few high-value gnews queries (PH manifesto, PDM Klawang).
"""
import subprocess, re, datetime, json
import xml.etree.ElementTree as ET
from urllib.parse import quote as url_quote

UA = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0 Safari/537.36"
CUTOFF_UTC = datetime.datetime(2026, 7, 20, 5, 55, 0, tzinfo=datetime.timezone.utc)
NOW_UTC = datetime.datetime.now(datetime.timezone.utc)
print(f"NOW UTC: {NOW_UTC.isoformat()} | cutoff: {CUTOFF_UTC.isoformat()}")

def fetch(url, timeout=20):
    try:
        r = subprocess.run(['curl','-sS','-L','-m',str(timeout),'-A',UA,'--compressed', url], capture_output=True, timeout=timeout+5)
        return r.returncode, r.stdout.decode('utf-8','replace')
    except Exception as e:
        return -1, str(e)

def parse_date(s):
    if not s: return None
    for fmt in ['%a, %d %b %Y %H:%M:%S %z','%Y-%m-%dT%H:%M:%S%z','%Y-%m-%dT%H:%M:%SZ']:
        try: return datetime.datetime.strptime(s.strip(), fmt)
        except: pass
    try:
        import email.utils
        d = email.utils.parsedate_to_datetime(s)
        if d: return d
    except: pass
    return None

# FMT + Awani RSS
FEEDS = [
    ('FMT', 'https://www.freemalaysiatoday.com/feed/'),
    ('Awani', 'https://www.astroawani.com/rss.xml'),
    ('Awani-Politik', 'https://www.astroawani.com/rss/berita-politik.xml'),
]
PRN_KW = ['negeri sembilan','prn','bersatu','loke','tok mat','aminuddin','sikamat','klawang','linggi','rantau','manifesto','mca','muhyiddin','hamzah','hadi','jalaluddin','pertang','wawasan','kacau daun','makmal','wee','chennah','chembong','palong','johol','gemencheh','repah','khaled','khairy','noh omar','arul kumar','ridzuan','kiandee','quorum','kuorum','pecat','tarik diri','lebih hebat','ros','sole opposition','melaka','wan saiful','zahid','amirudin','sufian']

fresh_prn = []
total_items = 0
for src, furl in FEEDS:
    rc, txt = fetch(furl, 20)
    if rc != 0 or not txt or '<item>' not in txt:
        print(f"{src}: rc={rc}, no items")
        continue
    try:
        root = ET.fromstring(txt.encode('utf-8'))
    except Exception as e:
        root = ET.fromstring(re.sub(r'[\x00-\x08\x0b\x0c\x0e-\x1f]','',txt).encode('utf-8'))
    cnt = 0
    fresh_cnt = 0
    for it in root.iter('item'):
        cnt += 1; total_items += 1
        t = (it.findtext('title') or '')
        l = (it.findtext('link') or '')
        d = parse_date(it.findtext('pubDate') or '')
        fresh = (d is None) or (d.tzinfo is None) or (d >= CUTOFF_UTC)
        tl = t.lower()
        isprn = any(k in tl for k in PRN_KW)
        if fresh and isprn:
            fresh_cnt += 1
            fresh_prn.append({'src':src,'title':t,'url':l,'date':d.isoformat() if d else '','fresh':True})
        elif isprn and not fresh:
            # show the latest non-fresh PRN too for context
            pass
    print(f"{src}: {cnt} items, {fresh_cnt} fresh PRN")

# Google News probe - a few high-value queries
GQ = [
    'PH manifesto launch Negeri Sembilan Amirudin 20 Jul',
    'PDM Klawang buka semula Negeri Sembilan',
    'Negeri Sembilan PRN 2026 manifesto',
    'Bersatu kuorum PN Negeri Sembilan',
    'Negeri Sembilan ceramah malam 20 Jul',
]
print("\n--- gnews probe ---")
gnews_fresh = []
for q in GQ:
    url = "https://news.google.com/rss/search?q=" + url_quote(q) + "&hl=en-MY&gl=MY&ceid=MY:en"
    rc, txt = fetch(url, 20)
    if rc != 0 or '<item>' not in txt:
        print(f"gnews [{q[:40]}]: rc={rc}, no items")
        continue
    try:
        root = ET.fromstring(txt.encode('utf-8'))
    except:
        continue
    items = list(root.iter('item'))
    fresh_items = []
    for it in items[:5]:
        t = it.findtext('title') or ''
        d = parse_date(it.findtext('pubDate') or '')
        fresh = (d is None) or (d.tzinfo is None) or (d >= CUTOFF_UTC)
        if fresh:
            fresh_items.append((t, d.isoformat() if d else ''))
    print(f"gnews [{q[:45]}]: {len(items)} items, {len(fresh_items)} fresh")
    for ft, fd in fresh_items[:3]:
        gnews_fresh.append((q, ft, fd))
        print(f"   FRESH: {ft} ({fd})")

print("\n=== SUMMARY ===")
print(f"Total RSS items scanned: {total_items}")
print(f"Fresh PRN items in RSS: {len(fresh_prn)}")
for a in fresh_prn:
    print(f"  - [{a['src']}] {a['title']} ({a['date']})")
print(f"Fresh gnews items: {len(gnews_fresh)}")
