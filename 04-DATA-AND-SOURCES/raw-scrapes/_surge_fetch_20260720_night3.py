#!/usr/bin/env python3
"""Nomination-Day Surge cycle 20260720_night3 (collecting ~15:09 UTC / 23:09 MYT 20 Jul 2026).
Campaign Day 2-3 (MYT 20 Jul). Director-approved PIR-06/07/16 priority collection.
Cutoff: post-14:00 UTC 20 Jul 2026 (post-22:00 MYT 20 Jul) = prior night2 cycle end.

KEY INSIGHT (from night2): The Vibes (thevibes.com) sitemap has 585 PRN-relevant articles;
  prior cycles only collected 2. The Vibes is a high-quality English outlet with unique
  analytical angles (Bersatu "voluntary split from PN", Muhyiddin "signals new alliance",
  Wan Saiful "messing things up", Loke "punching bag/bogeyman", sole-opposition framing)
  NOT found in the BM outlets (Awani/FMT/HarianMetro/Utusan) that dominated collection.
  This cycle = The Vibes backlog ENRICHMENT + standard fresh-content scan.

PRIORITY 1: The Vibes — collect highest-value NS-PRN-specific articles (125046-125257 range)
  that are genuinely NEW to the collection. Focus on PIR-06 (Bersatu/PN coalition ops),
  PIR-16 (dominant narratives), PIR-07 (battlegrounds). Tag [PRIORITY]/[CRITICAL] per rules.
PRIORITY 2: Check for any genuinely-fresh post-22:00 MYT content (manifesto launch coverage
  still pending 4 cycles; Loke DAP-congress pickup tracking).
PRIORITY 3: Standard gnews + RSS + homepage + Sinar ID scan.

Sources: The Vibes (sitemap + article fetch) + Google News RSS (PIR-targeted) + RSS feeds
  (Awani/FMT/HarianMetro) + homepage extraction + Sinar ID scan (788960-789040).
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
THIS_TS = "20260720_night3"
TODAY = "20260720"
# Cutoff = prior night2 cycle end (14:00 UTC 20 Jul = 22:00 MYT 20 Jul)
CUTOFF_UTC = datetime.datetime(2026, 7, 20, 14, 0, 0, tzinfo=datetime.timezone.utc)
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
         'islamophobia','poster boy','biggest loser']
PIR07 = ['ampangan','juasseh','klawang','sikamat','linggi','chembong','bembang','labu','nilai',
         'sri tanjung','rantau','tok mat','pertang','jalaluddin','derhaka','battleground',
         'kerusi tumpuan','hot seat','ceramah','walkabout','ops-centre','manifesto launch',
         'chennah','lenggeng','bahau','lobak','bukit kepayang','paroi','lukut',
         'bagan pinang','gemas','repah','jeram padang','rahang','pilihan raya negeri',
         'negeri sembilan','prn','johol','jempol','palong','chuah','gemencheh','tampin',
         'nomination','three-cornered','seat swap','candidate','menti besar','menteri besar']

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
          'amirudin','asas','kesinambungan','prnns','ns prn','ns polls','negeri polls']
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
        if any(k in bc for k in ['pecat','expulsion','tarik diri','withdraw','keluar dari pn',
                                'kuorum','quorum to vote','lebih hebat','new coalition',
                                'remove bersatu','sack bersatu','dissolve pn','bubarkan pn',
                                'formal expulsion','expulsion notice','candidate withdrawal',
                                'bersatu withdrawal','ros revokes','registrar of societies',
                                'pdm klawang buka semula','pdm klawang reopen',
                                'voluntary split','signals new alliance','looks beyond pn']):
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
           'duplicates':0,'gnews_headlines':[], 'rss_articles':[], 'thevibes_collected':0,
           'thevibes_skipped':0, 'thevibes_new':[]}

# existing slugs/URLs to dedup (check 20260720 + 20260719 dir for cross-day dedup)
existing_titles = set()
existing_basenames = set()
existing_urls = set()
for d in ['20260720','20260719']:
    p = f"/home/p62operator/.openclaw/workspace-ns/04-DATA-AND-SOURCES/raw-scrapes/{d}"
    if os.path.isdir(p):
        for fn in os.listdir(p):
            if fn.endswith('.md'):
                existing_titles.add(fn)
                core = re.sub(r'_(20260720_(?:morning|midday|afternoon|evening|midafternoon|lateafternoon|dusk|night|latenight|postmanifesto|night2|night3)|20260719_[^_]*)(?:_rss|_home|_targeted|_thevibes)?\.md','.md', fn)
                existing_basenames.add(core)
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

print(f"[0] dedup baseline: {len(existing_titles)} existing md files, {len(existing_urls)} URLs")
print(f"[0] cutoff: {CUTOFF_UTC.isoformat()} (22:00 MYT 20 Jul) | now: {NOW_UTC.isoformat()}")

# ============================================================
# 1. THE VIBES — sitemap-driven backlog enrichment (HIGHEST PRIORITY this cycle)
# ============================================================
print("\n=== [1] THE VIBES SITEMAP ENRICHMENT ===")
rc, txt = fetch("https://www.thevibes.com/sitemap.xml", timeout=30)
tv_locs = re.findall(r'<loc>([^<]+)</loc>', txt) if rc==0 else []
print(f"[1] The Vibes sitemap: {len(tv_locs)} locs")

# Curated list of highest-value NS-PRN article IDs (from sitemap analysis)
# Focus on NS PRN campaign period (125046-125257) + key Johor/Melaka context
TV_PRIORITY_IDS = [
    # PIR-06 CRITICAL-relevant: Bersatu/PN coalition ops, new alliance, sole opposition
    125155,  # bersatu-looks-beyond-pn-as-muhyiddin-signals-new-alliance-after-negeri-polls
    125101,  # bersatus-decision-to-use-own-logo-signals-voluntary-split-from-pn-in-ns-polls-annuar-musa
    125088,  # bersatu-to-contest-negeri-polls-under-own-logo-as-muhyiddin-blasts-pas-bn-tie-up
    125190,  # bersatu-now-sole-opposition-party-muhyiddin
    125123,  # pn-predicts-new-political-alignment-with-bn-to-continue
    125168,  # bn-pn-pact-in-negeri-sembilan-polls-centred-on-stability-and-full-36-seat-victory-target
    125183,  # prnns-bn-collaboration-with-pn-merely-an-understanding-no-agreements-zahid
    125189,  # unity-government-unlikely-to-return-for-second-term-as-bn-pn-cooperation-gains-momentum
    125223,  # bn-pn-understanding-puts-barisan-in-strong-position-for-ns-polls
    125211,  # bersatu-messing-things-up-for-bn-pn-candidates-claims-wan-saiful
    125210,  # ph-youth-wing-calls-on-bn-ministers-to-quit-cabinet-over-pn-electoral-alliance
    125099,  # bn-pn-cooperation-talks-revive-questions-over-political-loyalty-as-pas-shifts-closer-to-umno
    125074,  # bersama-pulls-out-of-negeri-sembilan-election-targets-medaka-battle
    125121,  # bns-11-unnamed-seats-fuel-speculation-of-pn-pact-in-negeri-sembilan-polls
    125122,  # negeri-prn-pn-to-contest-11-seats-completes-bns-puzzle-in-36-duns
    124997,  # zahid-no-final-umno-pas-deal-as-seat-talks-claims-surface-ahead-of-ns-polls
    # PIR-16 narratives
    125130,  # we-are-the-punching-bag-and-the-bogeyman-as-ph-eyes-20-seat-victory-loke
    125065,  # there-are-traitors-among-us-waiting-topple-aminuddin-loke
    125111,  # pas-president-alleges-dap-led-ph-turning-to-islamophobia-narratives
    125046,  # dap-secretary-general-backs-aminuddin-harun-as-pakatan-harapan-ns-state-election-poster-boy
    125222,  # prnns-loke-we-must-win-all-11-seats-to-help-ph-form-state-government
    125198,  # negeri-sembilan-voters-called-on-to-back-ph-for-continuity-of-stable-and-integrity-based-govt
    125182,  # ns-prn-ph-administrations-success-aminuddins-ability-will-be-campaign-focus-fahmi
    # Melaka DAP withdrawal (PIR-16 context)
    125058,  # dap-melaka-moves-into-opposition-benches-after-withdrawing-from-state-government
    125040,  # anwar-urges-dap-melaka-to-delay-withdrawal-from-state-government
    125039,  # ab-rauf-says-melaka-government-will-remain-stable-despite-dap-pullout
    125030,  # dap-withdraws-support-for-melaka-govt-after-assembly-approves-seven-appointed-seats
    125028,  # melaka-passes-appointed-assembly-members-bill-as-dap-moves-to-pull-out-of-state-govt
    # Muhyiddin graft trial (PIR-16)
    125144,  # jana-wibawa-graft-trial-rm1-million-cheque-to-bersatu-at-centre-of-proceedings
    125104,  # jana-wibawa-trial-kcj-finance-manager-says-she-was-directed-to-prepare-rm800000-cheques-for-bersatu
    # PIR-07 battlegrounds + nomination + candidates
    125163,  # prn-negeri-sembilan-jalaluddin-anthony-loke-arrive-a-nomination-centre
    125166,  # dragon-dance-drums-welcome-tok-mats-at-nomination-centre
    125169,  # prn-negeri-sembilan-handshake-between-hadi-awang-and-asyraf-wajdi-centre-of-attention
    125170,  # prn-negeri-sembilan-straight-fight-in-rantau-chembong-three-cornered-in-paroi-kota
    125177,  # negeri-sembilan-polls-the-battlegrounds-big-names-and-three-cornered-fights-to-watch
    125179,  # 103-candidates-confirmed-for-negeri-sembilan-polls-as-two-week-campaign-begins
    125157,  # negeri-sembilan-poll-race-begins-today-as-nomination-day-to-open-across-8-centres
    125136,  # negeri-sembilan-polls-enter-race-mode-as-36-seat-battle-begins
    125173,  # prn-negeri-sembilan-four-seats-in-focus-battle-expected-to-be-tougher-than-johor
    125202,  # bn-cannot-rely-solely-on-johor-victory-formula-for-negeri-sembilan-johari
    125181,  # negeri-sembilan-prn-bn-to-launch-manifesto-on-july-24-focus-on-development-well-being-stability
    125201,  # negeri-sembilan-prn-police-record-one-report-over-supporters-verbal-dispute
    125049,  # an-electoral-gamble-aminuddin-contests-in-bn-stronghold-linggi-after-4-terms-in-sikamat
    125103,  # aminuddin-denies-abandoning-sikamat
    125091,  # prn-negeri-sembilan-hopes-of-kj-becoming-menteri-besar-dashed-as-name-left-off-candidate-list
    125086,  # bn-pledges-stable-leadership-as-zahid-unveils-first-25-candidates-for-negeri-sembilan-polls
    125047,  # anwar-urges-political-parties-to-keep-negeri-sembilan-royal-institution-out-of-election-campaign
    124991,  # anwar-to-unveil-ph-candidates-for-negeri-sembilan-polls-tomorrow
    124987,  # dap-retains-eight-incumbents-unveils-three-new-candidates-for-ns-polls
    124911,  # dap-aims-to-defend-all-11-negeri-sembilan-seats-sets-sights-on-opposition-strongholds
    124686,  # bn-mulls-seat-swaps-in-negeri-sembilan-as-tok-mat-pushes-for-election-reset
    125057,  # rumours-rife-over-kj-contesting-in-negeri-polls-possibly-in-rembau
    124592,  # want-to-contest-in-negeri-no-problem-update-your-address-first-loke-tells-albert-tei
    124579,  # albert-tei-mulls-negeri-sembilan-election-bid-eyes-showdown-with-anthony-loke
]

# Build URL->ID map from sitemap for resolution
tv_url_by_id = {}
for l in tv_locs:
    m = re.search(r'/articles/(\w+)/(\d+)', l)
    if m:
        tv_url_by_id[int(m.group(2))] = l

tv_saved = 0
tv_skipped = 0
tv_new_list = []
for aid in TV_PRIORITY_IDS:
    url = tv_url_by_id.get(aid)
    if not url:
        # try news category fallback
        url = f"https://www.thevibes.com/articles/news/{aid}"
    if url in existing_urls:
        tv_skipped += 1
        continue
    rc, htmltxt = fetch(url, timeout=20)
    if rc != 0 or len(htmltxt) < 2000:
        # try alternate categories
        for cat in ['news','opinion','business','education']:
            alt = f"https://www.thevibes.com/articles/{cat}/{aid}"
            if alt == url: continue
            rc, htmltxt = fetch(alt, timeout=15)
            if rc==0 and len(htmltxt) > 2000 and 'Not Found' not in htmltxt[:800]:
                url = alt; break
    if rc != 0 or len(htmltxt) < 2000:
        tv_skipped += 1
        continue
    low = htmltxt[:1500].lower()
    if 'not found' in low or '404' in low[:200]:
        tv_skipped += 1; continue
    # title
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
    if not soup_title: tv_skipped += 1; continue
    soup_title = soup_title.replace(' | The Vibes','').replace(' | Malaysia | The Vibes','').strip()
    body = clean_html(htmltxt)
    if len(body) < 200: tv_skipped += 1; continue
    tags = hit(soup_title, body)
    if not tags:
        tags = ['PIR-07'] if is_prn(soup_title, body) else []
    if not tags: tv_skipped += 1; continue
    # date heuristic
    datestr = ''
    m = re.search(r'(\d{4}-\d{2}-\d{2}[ T]\d{2}:\d{2})', htmltxt)
    if m: datestr = m.group(1)
    if not datestr:
        # try The Vibes date format in JSON-LD
        m2 = re.search(r'"datePublished"\s*:\s*"([^"]+)"', htmltxt)
        if m2: datestr = m2.group(1)[:16]
    fn_info = save_article('TheVibes', url, soup_title, datestr, body, tags, suffix='_thevibes')
    if fn_info:
        fn, crit = fn_info
        if fn:
            results['saved'] += 1
            results['saved_files'].append(os.path.basename(fn))
            existing_urls.add(url)
            tv_saved += 1
            results['thevibes_collected'] += 1
            tv_new_list.append({'id':aid,'title':soup_title[:90],'url':url,'tags':tags,'critical':crit})
            if crit: results['critical'] += 1
    else:
        tv_skipped += 1
    time.sleep(0.3)

results['thevibes_new'] = tv_new_list
print(f"[1] The Vibes: {tv_saved} collected, {tv_skipped} skipped/not-PRN, {len(TV_PRIORITY_IDS)} targeted")

# ============================================================
# 2. Check for genuinely-NEW The Vibes articles beyond sitemap (125258-125270)
# ============================================================
print("\n=== [2] THE VIBES NEW-ARTICLE SCAN (125258-125270) ===")
tv_new_fresh = 0
for aid in range(125258, 125271):
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
                tv_new_list.append({'id':aid,'title':soup_title[:90],'url':url,'tags':tags,'critical':fn_info[1],'fresh':True})
                if fn_info[1]: results['critical'] += 1
            break
    time.sleep(0.2)
print(f"[2] The Vibes fresh scan 125258-125270: {tv_new_fresh} found")

# ============================================================
# 3. GOOGLE NEWS RSS — focused queries (manifesto launch + Loke pickup + night campaign)
# ============================================================
print("\n=== [3] GOOGLE NEWS RSS ===")
GNEWS_QUERIES = [
    # PIR-06 [CRITICAL] watch (mandatory)
    'Bersatu pecat PN Negeri Sembilan',
    'Bersatu tarik diri PN kuorum Negeri Sembilan',
    'lebih hebat coalition PN Bersatu Negeri Sembilan',
    'Bersatu sole opposition parliament Negeri Sembilan',
    'Kiandee quorum Bersatu Negeri Sembilan',
    'Bersatu looks beyond PN Muhyiddin new alliance',
    'Bersatu voluntary split PN Negeri Sembilan',
    # PIR-16 narratives
    'Bersatu kacau daun Negeri Sembilan',
    'Loke DAP congress Unity Government Negeri Sembilan',
    'Loke abide DAP congress decision kerajaan perpaduan',
    'DAP keluar kerajaan perpaduan PRN Negeri Sembilan',
    'Wan Saiful bersatu messing things up Negeri Sembilan',
    'makmal politik PRU16 Anwar Negeri Sembilan',
    'penyatuan undi Melayu Negeri Sembilan',
    # PIR-07 MANIFESTO LAUNCH (top priority — 5th cycle flagging)
    'PH manifesto launch Negeri Sembilan 20 Jul',
    'manifesto PH Negeri Sembilan dilancarkan malam',
    'manifesto Pakatan Harapan Negeri Sembilan 2026',
    'Amirudin Shari lancar manifesto PH Negeri Sembilan',
    'Aminuddin Harun manifesto kesinambungan Negeri Sembilan',
    'manifesto PH Negeri Sembilan B40 M50 perlindungan',
    'PH manifesto Negeri Sembilan promise pledges',
    'Amirudin manifesto PH Negeri Sembilan speech',
    'manifesto PH Negeri Sembilan 36 kerusi menang',
    'BN manifesto Negeri Sembilan 24 Jul',
    # PIR-07 battlegrounds
    'Negeri Sembilan PRN 2026',
    'PRN Negeri Sembilan pilihan raya',
    'Bersatu PN Negeri Sembilan 2026',
    'Jalaluddin button badge wang pengundi Negeri Sembilan',
    'Tok Mat Rantau Negeri Sembilan ceramah',
    'Anthony Loke Chennah Negeri Sembilan',
    'Pertang Jalaluddin derhaka Negeri Sembilan',
    'Negeri Sembilan calon kempen malam 21 Jul',
    'PRN Negeri Sembilan ceramah malam 20 Jul',
    'lelaki ditahan hina institusi diraja Negeri Sembilan',
    # night3 fresh-content watch
    'Negeri Sembilan PRN 21 Jul',
    'PRN N9 21 Jul calon kempen',
    'Negeri Sembilan pilihan raya malam 20 Jul',
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
print(f"[3] gnews: {results['gnews_queries']} queries -> {len(gnews_all)} items, "
      f"{len(results['gnews_headlines'])} PRN/priority hits, {results['fresh_after_cutoff']} fresh")

# ============================================================
# 4. RSS FEEDS — Awani + FMT + HarianMetro (the working feeds)
# ============================================================
print("\n=== [4] RSS FEEDS ===")
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
        print(f"[4] {src} feed: HTTP rc={rc}, no items")
        continue
    try:
        root = ET.fromstring(txt.encode('utf-8'))
    except Exception:
        try: root = ET.fromstring(re.sub(r'[\x00-\x08\x0b\x0c\x0e-\x1f]','',txt).encode('utf-8'))
        except Exception:
            print(f"[4] {src} feed: parse fail"); continue
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
    print(f"[4] {src} feed: {cnt} items scanned, "
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
print(f"[4] RSS full-text saved: {rss_saved}")

# ============================================================
# 5. For gnews FRESH priority hits + RSS no-full items: extract article from URL
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
print(f"[5] URLs to extract full text: {len(to_extract)} (fresh gnews: {fresh_gnews})")
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
print(f"[5] Extracted full-text from URLs: {extracted}")

# ============================================================
# 6. Homepage headline scan
# ============================================================
print("\n=== [6] HOMEPAGE SCAN ===")
HOME_PAGES = [
    ('Awani', 'https://www.astroawani.com.my/berita'),
    ('Awani', 'https://www.astroawani.com.my/berita-politik'),
    ('NST', 'https://www.nst.com.my/news/politics'),
    ('MalayMail', 'https://www.malaymail.com/news/politics'),
    ('Utusan', 'https://www.utusan.com.my/politik'),
    ('HarianMetro', 'https://www.hmetro.com.my/terkini'),
    ('Sinar', 'https://www.sinarharian.com.my/politik'),
]
home_links = set()
for src, hurl in HOME_PAGES:
    rc, htmltxt = fetch(hurl, timeout=20)
    if rc != 0 or not htmltxt:
        print(f"[6] {src} {hurl}: rc={rc}")
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
    print(f"[6] {src} {hurl}: {cnt} candidate links")

url_prn_kw = ['negeri-sembilan','prn','bersatu','loke','tok-mat','aminuddin','sikamat','ampangan',
              'klawang','linggi','rantau','manifesto','ceramah','mca','kiandee','muhyiddin',
              'hamzah','hadi','jalaluddin','pertang','wawasan','kacau-daun','makmal-politik',
              'melaka','wan-saiful','albert-tei','wee','chennah','lenggeng','lukut','nilai',
              'gemas','chembong','bembang','labu','juasseh','johol','jempol','palong','khaled',
              'khairy','kj','noh-omar','sri-tanjung','5-penjuru','chennah','derhaka','status-quo',
              'gelanggang','amirudin','sufian','ridzuan','kamil','derhaka','kwap','efishery',
              'fathi-aris','rafizi','bersama','asas','kesinambungan','asyraf','menebuk',
              'button-badge','diraja','bendera','maut','sole-opposition','lone-opposition',
              'dapan','dap-','pn-','-pn','/bn','umno','poster-boy','punching','bogeyman',
              'traitors','islamophobia','jana-wibawa','sole-opposition','new-alliance']
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
              ('NST' if 'nst' in full else ('HarianMetro' if 'hmetro' in full else 'Homepage'))))))
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
print(f"[6] Homepage extracted: {home_extracted}")

# ============================================================
# 7. Targeted Sinar article-ID scan (788960-789040) for fresh content
# ============================================================
print("\n=== [7] SINAR ID SCAN 788960-789040 ===")
sinar_saved = 0
sinar_new = []
for aid in range(788960, 789041):
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
print(f"[7] Sinar 788960-789040: {sinar_saved} saved, {len(sinar_new)} PRN hits")
results['sinar_targeted_hits'] = sinar_new

# ============================================================
# SAVE summaries
# ============================================================
with open(f"{BASE}/_gnews_headlines_20260720_night3.json","w") as f:
    json.dump(results['gnews_headlines'], f, ensure_ascii=False, indent=1)
with open(f"{BASE}/_night3_summary_20260720.json","w") as f:
    json.dump(results, f, ensure_ascii=False, indent=1, default=str)

print("\n" + "=" * 60)
print(f"NIGHT3 CYCLE SUMMARY ({THIS_TS})")
print(f"  The Vibes collected: {results['thevibes_collected']} (backlog enrichment)")
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
print("THE VIBES NEW (this cycle):")
for t in results['thevibes_new']:
    print(f"  - [{t['id']}] {t['title']} | tags={t['tags']}{t.get('critical','')}")
print("SINAR TARGETED HITS (788960-789040):")
for s in sinar_new:
    print(f"  - [{s['id']}] {s['title'][:90]} | tags={s['tags']}")
print("=" * 60)
