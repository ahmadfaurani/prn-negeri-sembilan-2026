#!/usr/bin/env python3
"""NST WordPress feed full-content extractor for cycle 20260719_051226.
The NST /feed is a WordPress RSS with content:encoded (full article body).
Extract NS-relevant articles and save as priority files. Also fetch FMT homepage articles.
TLP:AMBER.
"""
import re, html, os, datetime, subprocess

BASE = "/home/p62operator/.openclaw/workspace-ns/04-DATA-AND-SOURCES/raw-scrapes/20260719"
TS = "20260719_051226"; TODAY = "20260719"; TS_TIME = "051226"
NOW_ISO = datetime.datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S UTC")
NOW_MYT = (datetime.datetime.utcnow()+datetime.timedelta(hours=8)).strftime("%H:%M MYT %d %b %Y")
UA = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) Chrome/126.0.0.0 Safari/537.36"

def clean(s):
    s = re.sub(r'<!\[CDATA\[','',s); s=re.sub(r'\]\]>','',s)
    s = html.unescape(s)
    s = re.sub(r'\s+',' ',s).strip()
    return s

def clean_html(s):
    s = re.sub(r'<!\[CDATA\[','',s); s=re.sub(r'\]\]>','',s)
    s = html.unescape(s)
    # convert <p> and <br> to newlines, strip other tags
    s = re.sub(r'</p>', '\n\n', s, flags=re.I)
    s = re.sub(r'<br\s*/?>', '\n', s, flags=re.I)
    s = re.sub(r'<[^>]+>', '', s)
    s = re.sub(r'\n{3,}', '\n\n', s)
    return s.strip()

with open('/home/p62operator/.openclaw/workspace-ns/04-DATA-AND-SOURCES/raw-scrapes/tmp_work/nst_feed.xml',encoding='utf-8',errors='replace') as f:
    txt = f.read()
items = re.findall(r'<item>(.*?)</item>', txt, re.S)
print(f"NST feed items: {len(items)}")

NS_RE = re.compile(r'(negeri sembilan|negri sembilan|n\.?\s?9\s|prn|loke|hadi|bersatu|bn.pn|pn.bn|election|polls|umno|dap|aminuddin|tok mat|chennah|rantau|linggi|sikamat|melaka|perikatan|barisan|johari| coalition|understanding)', re.I)

saved = 0
for it in items:
    tm = re.search(r'<title>(.*?)</title>', it, re.S)
    lm = re.search(r'<link>(.*?)</link>', it, re.S)
    pm = re.search(r'<pubDate>(.*?)</pubDate>', it, re.S)
    cm = re.search(r'<content:encoded>(.*?)</content:encoded>', it, re.S)
    dm = re.search(r'<description>(.*?)</description>', it, re.S)
    if not tm: continue
    title = clean(tm.group(1))
    link = clean(lm.group(1)) if lm else ''
    pub = clean(pm.group(1)) if pm else ''
    if not NS_RE.search(title): continue
    body = clean_html(cm.group(1)) if cm else (clean_html(dm.group(1)) if dm else "")
    body = body[:20000]
    # PIR tag
    t = title.lower()
    pir = "PIR-07"
    if re.search(r'(melaka|dap quits|appointed assemblymen)', t): pir = "PIR-16+PIR-07"
    if re.search(r'(bersatu|pecat|hadi|perikatan|pn.bn|bn.pn|coalition|understanding)', t): pir = "PIR-06+PIR-07"
    if re.search(r'(loke|mca|dap)', t) and 'melaka' not in t: pir = "PIR-16+PIR-07"
    slug = re.sub(r'[^a-z0-9]+','-', title[:55].lower()).strip('-')
    fname = f"priority_{pir.lower().replace('+','-')}_nst-{slug}_{TODAY}_{TS_TIME}.md"
    lines = [f"# [PRIORITY {pir}] nst-{slug}",
             f"Source URL: {link}",
             f"Collected: {TODAY} {TS} UTC ({NOW_ISO}) | MYT: {NOW_MYT}",
             f"Classification: TLP:AMBER",
             f"Source: New Straits Times (nst.com.my WordPress feed)",
             f"HTTP: 200 | mode: nst-wp-feed",
             f"Title: {title}", f"PubDate: {pub}", f"Body chars: {len(body)}",
             "", "## Full text (from NST WordPress RSS content:encoded)", "="*78,
             body if body else "(no content:encoded)", "="*78]
    with open(os.path.join(BASE, fname),"w",encoding="utf-8") as f:
        f.write("\n".join(lines))
    print(f"  [{pir}] {title[:90]}")
    print(f"    body={len(body)} | pub={pub} | {fname}")
    saved += 1
print(f"\nNST feed articles saved: {saved}")
