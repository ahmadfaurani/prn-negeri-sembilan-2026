#!/usr/bin/env python3
"""Analyze the 51 saved files from 20260720_morning cycle:
- Extract date, title, PIR tags, [CRITICAL] status
- Cross-reference against 20260719 collection (filenames) to find genuinely-new
- Classify false positives (World Cup / geopolitics / sports / non-NS)
- Output a clean classification table."""
import os, re, glob, json

D20 = "/home/p62operator/.openclaw/workspace-ns/04-DATA-AND-SOURCES/raw-scrapes/20260720"
D19 = "/home/p62operator/.openclaw/workspace-ns/04-DATA-AND-SOURCES/raw-scrapes/20260719"

# Build set of prior titles/slugs from 20260719
prior_titles = set()
prior_slugs = set()
for fn in os.listdir(D19):
    if not fn.endswith('.md'): continue
    prior_titles.add(fn)
    # extract slug portion (between priority tags / source and timestamp)
    m = re.search(r'_(.*?)_\d{8}_', fn)
    if m: prior_slugs.add(m.group(1).lower())

# False-positive classifier
FP_PATTERNS = [
    'world cup','piala dunia','sepanyol','argentina','messi','torres','scaloni','mbappe',
    'iran','israel','gaza','lebanon','rubio','trump','russian','nadezhdin','ukraine',
    'ohtani','mcgregor','hamilton','mercedes','russell','shakira','madonna','bieber',
    'salad','cirit-birit','wabak','parasit','zizie','mahkamah','rasuah',
    'immigration','body cam','belgian gp','f1','racing',
    'banjir kilat','new york','new jersey','jalan','hujan lebat',
    'gold falls','dollar firmer','brent','rate-hike','productivity tools',
    'cyber','siber','digital','regulatory conference',
    'felda','jana wibawa'  # jana wibawa is real (Muhyiddin) - remove from FP
]
FP_PATTERNS.remove('jana wibawa')  # it's real

# Hard real-NS indicators (title/url contains these = real PRN)
REAL_NS = ['negeri sembilan','n-sembilan','negeri-sembilan','prn','pilihan raya negeri',
           'loke','aminuddin','tok mat','tok-mat','jalaluddin','pertang','klawang',
           'sikamat','linggi','rantau','chennah','khaled','muhyiddin','bersatu',
           'wawasan','mca','wee','hadi','jana wibawa','kerjasama bn pn','bn-pn',
           'perikatan','ph sasar','ph-targets','manifesto','kerusi','kempen',
           'undang-undang','mb','menteri besar','derhaka','kacau daun','johor wipeout',
           'blue wave','selangor','pru16','johol','polis','undi']

rows = []
for path in sorted(glob.glob(f"{D20}/*.md")):
    fn = os.path.basename(path)
    txt = open(path).read()
    # extract fields
    title_m = re.search(r'^# (.+)$', txt, re.M)
    title = title_m.group(1).strip() if title_m else fn
    date_m = re.search(r'\*\*Date:\*\*\s*(.*?)$', txt, re.M)
    date = date_m.group(1).strip() if date_m else ''
    tag_m = re.search(r'\*\*PIR tags:\*\*\s*(.+?)( \[CRITICAL\])?$', txt, re.M)
    tags_raw = tag_m.group(1).strip() if tag_m else 'none'
    crit = '[CRITICAL]' in (tag_m.group(0) if tag_m else '')
    url_m = re.search(r'\*\*URL:\*\*\s*(\S+)', txt)
    url = url_m.group(1) if url_m else ''
    src_m = re.search(r'\*\*Source:\*\*\s*(\S+)', txt)
    src = src_m.group(1) if src_m else ''
    body = txt.split('---',2)[-1] if '---' in txt else txt

    tl = title.lower(); bl = body.lower(); ul = url.lower(); allc = tl+' '+ul+' '+bl[:1500]

    # classify
    is_real = any(k in allc for k in REAL_NS)
    is_fp = (not is_real) and any(k in allc for k in FP_PATTERNS)
    # refine: world cup even if some real words
    wc = any(k in allc for k in ['piala dunia','world cup','messi','torres','scaloni','mbappe',
                                 'sepanyol','argentina','shakira','madonna','bieber','ohtani',
                                 'mcgregor','hamilton','belgian gp'])
    geo = any(k in allc for k in ['iran','israel','gaza','lebanon','rubio','russian','ukraine',
                                  'dollar firmer','gold falls','brent','rate-hike'])
    if wc or geo: is_fp = True; is_real = False

    # duplicate check vs prior
    # build a comparable slug
    base_slug = re.sub(r'_\d{8}.*$','',fn).lower()
    dup_in_prior = False
    for ps in prior_slugs:
        if base_slug in ps or ps in base_slug or base_slug.replace('-','') == ps.replace('-',''):
            dup_in_prior = True; break
    # also title-based dup
    if not dup_in_prior:
        for pt in prior_titles:
            ptl = pt.lower()
            # share a long token run
            toks = [t for t in re.split(r'[^a-z0-9]+', tl) if len(t)>4]
            if sum(1 for t in toks if t in ptl) >= 3:
                dup_in_prior = True; break

    cls = 'FALSE-POSITIVE' if is_fp else ('REAL-NS' if is_real else 'UNCLEAR')
    if dup_in_prior and cls=='REAL-NS': cls = 'REAL-DUP'
    rows.append({'fn':fn,'date':date,'src':src,'title':title[:70],'tags':tags_raw,
                 'crit':crit,'cls':cls,'url':url})

# sort: fresh first
def freshkey(r):
    d=r['date']
    return (d[:10] if d else '0', d[11:19] if d else '0')
rows.sort(key=freshkey, reverse=True)

print(f"{'CLASS':<13} {'CRIT':<5} {'DATE':<26} {'SRC':<11} TITLE")
print('-'*120)
counts = {'REAL-NS':0,'REAL-DUP':0,'FALSE-POSITIVE':0,'UNCLEAR':0}
for r in rows:
    counts[r['cls']] = counts.get(r['cls'],0)+1
    print(f"{r['cls']:<13} {'C' if r['crit'] else '':<5} {r['date'][:26]:<26} {r['src']:<11} {r['title']}")
print('-'*120)
print('COUNTS:', counts)
print('TOTAL:', len(rows))

# Save classification json
json.dump(rows, open(f"{D20}/_classification_20260720_morning.json",'w'), indent=2)
