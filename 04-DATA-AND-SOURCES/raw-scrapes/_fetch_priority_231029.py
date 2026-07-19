#!/usr/bin/env python3
"""Priority full-text fetcher for cycle 20260718_231029.
Fetches genuinely net-new high-value PIR articles, saves as priority_pirXX_*.md."""
import subprocess, re, datetime
from bs4 import BeautifulSoup
from urllib.parse import urljoin

BASE = "/home/p62operator/.openclaw/workspace-ns/04-DATA-AND-SOURCES/raw-scrapes/20260718"
TS = "231029"
TODAY = "20260718"
NOW_ISO = datetime.datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S UTC")
UA = ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36")

# (pir, slug, url, note)
TARGETS = [
    ("PIR-07","5-hot-seats-utusan","https://www.utusan.com.my/berita/2026/07/lima-kerusi-panas-jadi-tumpuan/","Utusan: 5 hot seats in focus (brand-new 06:40 MYT 19 Jul)"),
    ("PIR-07","3-coalitions-clash-utusan","https://www.utusan.com.my/berita/2026/07/tiga-gabungan-bertembung/","Utusan: 3 coalitions clash (brand-new 06:45 MYT 19 Jul)"),
    ("PIR-07","aminuddin-linggi-mstar","https://www.mstar.com.my/lokal/semasa/2026/07/18/aminuddin-yakin-langkah-ke-linggi-mampu-tambah-kemenangan-ph","mStar: Aminuddin confident stepping to Linggi adds PH wins"),
    ("PIR-09","wee-bnpn-not-merger-mkini","https://www.malaysiakini.com/news/780035","mkini: Wee BN-PN pact not a merger, MCA principles intact (16h ago)"),
    ("PIR-09","tamim-independent-mkini","https://www.malaysiakini.com/news/780055","mkini: Tamim surrenders, to campaign for NS independent candidate (10h ago)"),
    ("PIR-07","kiniguide-shifting-alliances-mkini","https://www.malaysiakini.com/news/780052","mkini KiniGuide: shifting alliances, battle royale NS (10h ago)"),
    ("PIR-07","nominations-full-force-mkini","https://www.malaysiakini.com/news/780023","mkini: coalition leaders/supporters full force for NS nominations (19h ago)"),
    ("PIR-07","dap-revives-anti-bn-mkini","https://www.malaysiakini.com/news/780010","mkini: DAP revives anti-BN campaign ahead of NS polls (22h ago)"),
    ("PIR-06","bersatu-crossroads-nst","https://news.google.com/rss/articles/CBMiswFBVV95cUxNamFSdDhwU2Y2bVY0UDRMQVhaYVE4OW5kZ192WmlHTlM3THFIU1Yya2FlZ1JDYjVNcDc4S2xDTHc2REFpRnAybDBaNkZvbDB2dXJyWHNYQ0hjdWRBRDdvZ1o3NGszYTRuVUw5cHVxUjFFMFRES3d2eDgyUWJzRVUtcVlGVW91dUpVa1Ftdm96LU8ydGJVMGhpa29BOUVXNUJNaXhsakRHUmlkZWdLWU1rQWNxRdIBuAFBVV95cUxQLXJNRVJ1a1ppcHF6akpOWkpNczFuNG9PRTBKRndtcXc4UFhtNFAxT2NsNGJxeGdLaldOOTdrUjNNcy1YeklhenZ6elpFVG0tRF9ReFFFdkQzR3RRcVRsLVJwend6eUZma0FIOU11REZuUlRUQ0dSSHZNNENmOTFjbU9fdXBzOTRsa0kzVUJibHpmNDRfQ2szMklaSUJFdDY2cHdvY0tFbXJicFJGTHdJbEJIUHc4S3lV?oc=5","NST via gnews: Bersatu at a crossroads amid BN-PN cooperation (pubDate 23:00 GMT 18 Jul)"),
    ("PIR-07","36-seats-contest-astro","https://news.google.com/rss/articles/CBMitwFBVV95cUxPdnNEellKanZROXpfYlp6ZHREVE1uVTBxTUlJUFFZS2VwZ3RYd2tmaEYyYWwweWF6cUkyQTdGZmJ1Vlh1WDRVOHpjcFJHYmlXY1NrX0tOY05COTc0eC1SdGNpVHhJbTNrR0pGbFNTVjZUZlpGY0lhR3loWklVem1sai1IX0lPcGM4R25XRFJaZ0RDWDZmSXpGUkg0ZUpBcUFYVlNTTnhLbjZHckVhYXc4blc4ZlYxd1U?oc=5","Astro Awani via gnews: contest for 36 DUN seats begins tomorrow"),
]

def fetch(url, timeout=35):
    cmd = ["curl","-sS","-L","-m",str(timeout),"-A",UA,"--compressed",
           "-H","Accept-Language: en-US,en;q=0.9,ms;q=0.8",
           "-w","\n__HTTPCODE__:%{http_code}\n__FINALURL__:%{url_effective}",
           url]
    p = subprocess.run(cmd, capture_output=True, timeout=timeout+10)
    out = p.stdout
    m = re.search(rb"__HTTPCODE__:(\d+)", out)
    code = m.group(1).decode() if m else "ERR"
    mu = re.search(rb"__FINALURL__:(\S+)", out)
    final = mu.group(1).decode("utf-8","replace") if mu else url
    body = out[:m.start()] if m else out
    return code, body, final

def extract(url, body):
    try:
        soup = BeautifulSoup(body.decode("utf-8","replace"), "html.parser")
    except Exception:
        return "", "", ""
    # title
    title = ""
    if soup.title and soup.title.string:
        title = soup.title.string.strip()
    og = soup.find("meta", property="og:title")
    if og and og.get("content"): title = og["content"].strip()
    # body text: prefer article tags, then <p> aggregation
    text_parts = []
    for sel in ["article","div.article-content","div.article-body","div.entry-content",
                "div.post-content","div.content__body","div.field-body","div.story-body",
                "div#article-body","div.article","main"]:
        node = soup.select_one(sel)
        if node:
            for p in node.find_all(["p","li","h2","h3"]):
                t = p.get_text(" ", strip=True)
                if t and len(t) > 25:
                    text_parts.append(t)
            if text_parts:
                break
    if not text_parts:
        for p in soup.find_all("p"):
            t = p.get_text(" ", strip=True)
            if t and len(t) > 40:
                text_parts.append(t)
    body_text = "\n\n".join(text_parts[:80])
    # meta description
    desc = ""
    md = soup.find("meta", attrs={"name":"description"}) or soup.find("meta", property="og:description")
    if md and md.get("content"): desc = md["content"].strip()
    return title[:300], body_text[:20000], desc[:500]

results = []
for pir, slug, url, note in TARGETS:
    code, body, final = fetch(url)
    title, text, desc = extract(url, body) if body else ("","","")
    ok = bool(text) and code == "200"
    fname = f"priority_{pir.lower()}_{slug}_{TODAY}_{TS}.md"
    lines = []
    lines.append(f"# [PRIORITY {pir}] {slug}")
    lines.append(f"Source URL: {url}")
    lines.append(f"Final/redirected URL: {final}")
    lines.append(f"Collected: {TODAY} {TS} UTC ({NOW_ISO}) | Classification: TLP:AMBER")
    lines.append(f"HTTP: {code} | fetch_ok: {ok} | note: {note}")
    lines.append(f"Page title: {title}")
    if desc: lines.append(f"Meta desc: {desc}")
    lines.append("")
    lines.append("## Article Body (extracted)")
    lines.append("="*70)
    if text:
        lines.append(text)
    else:
        lines.append(f"[NO BODY EXTRACTED — code={code}, bytes={len(body)}. Likely paywalled (mkini) or gnews-redirect blocked (NST/Astro). Headline + publisher + pubDate already captured in raw scrape .md.]")
    lines.append("="*70)
    with open(f"{BASE}/{fname}","w",encoding="utf-8") as f:
        f.write("\n".join(lines))
    results.append({"pir":pir,"slug":slug,"file":fname,"http":code,"ok":ok,"body_len":len(text),"final":final})

print("=== PRIORITY FETCH RESULTS ===")
for r in results:
    print(f"  [{r['http']}] ok={r['ok']} body={r['body_len']:6d}  {r['pir']} {r['slug']}  -> {r['file']}")
    if r['ok'] and len(r['final']) < 120: print(f"        final: {r['final']}")
