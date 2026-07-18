#!/usr/bin/env python3
"""
PRN Negeri Sembilan 2026 — News Collection Scraper (Nomination Day Surge cycle).
Fetches Malaysian news sources, extracts article listings, tags PIR keywords,
saves timestamped .md files. Updates collection_metadata.json.
"""
import subprocess, json, os, re, sys, datetime, hashlib
from urllib.parse import urljoin, urlparse
from bs4 import BeautifulSoup

BASE = "/home/p62operator/.openclaw/workspace-ns/04-DATA-AND-SOURCES/raw-scrapes"
TODAY = datetime.datetime.utcnow().strftime("%Y%m%d")
TS = datetime.datetime.utcnow().strftime("%H%M%S")
OUTDIR = os.path.join(BASE, TODAY)
os.makedirs(OUTDIR, exist_ok=True)

UA = ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36")

# (key, label, homepage, section_url_to_scrape)
SOURCES = [
    ("malaysiakinicom", "Malaysiakini", "https://www.malaysiakini.com", "https://www.malaysiakini.com/news/my"),
    ("thmalaysianinsightcom", "The Malaysian Insight", "https://www.themalaysianinsight.com", "https://www.themalaysianinsight.com/"),
    ("nstcommy", "New Straits Times", "https://www.nst.com.my", "https://www.nst.com.my/news/nation"),
    ("thestarcommy", "The Star", "https://www.thestar.com.my", "https://www.thestar.com.my/news/nation"),
    ("utusancommy", "Utusan Malaysia", "https://www.utusan.com.my", "https://www.utusan.com.my/nasional/"),
    ("bhariancommy", "BHarian", "https://www.bharian.com.my", "https://www.bharian.com.my/berita/nasional"),
    ("kosmocommy", "Kosmo", "https://www.kosmo.com.my", "https://www.kosmo.com.my/berita/nasional/"),
    ("astroawanicom", "Astro Awani", "https://www.astroawani.com", "https://www.astroawani.com/berita-nasional"),
    ("mstarcommy", "mStar", "https://www.mstar.com.my", "https://www.mstar.com.my/lokal/sembilan"),
    ("ohbulancom", "OhBulan", "https://www.ohbulan.com", "https://www.ohbulan.com/tag/negeri-sembilan/"),
]

# PIR keyword sets (lowercased). Match on title+snippet text.
PIR = {
    "PIR-06": ["pecat", "terminate", "remove", "keluar", "withdraw", "tarik diri",
               "majlis tertinggi", "asas kukuh", "bersatu", "kiandee", "muhyiddin",
               "hamzah zainudin", "samsuri", "hadi", "supreme council", "dibuang",
               "diberhentikan", "pecat bersatu", "keluar pn", "bubarkan"],
    "PIR-09": ["disiplin", "lompat", "pengkhianat", "defector", "hopper",
               "kredibiliti", "eligibility", "bankrup", "kes mahkamah", "calon",
               "independent", "bebas", "kalah kerusi", "dibuang", "tatang",
               "gerakan", "tang jay", "ampangan", "nazri kassim", "rafie"],
    "PIR-07": ["kerusi tumpuan", "battleground", "pertembungan", "marquee", "pinggir",
               "manifesto", "kempen", "operasi", "hari penamaan", "nomination",
               "calon", "penamaan", "tumpuan", "pertandingan", "calonkan",
               "negeri sembilan", "prn", "prn ns", "hilir selangor"],
}

PRN_PATS = re.compile(r"(negeri sembilan|negri sembilan|n9 polls?|prn\s*(negeri|ns|sembilan)|"
                      r"sembilan polls?|state election|pilihanraya negeri|"
                      r"august 1|1 ogos|ogos 1|polling day|hari pengundian|"
                      r"bersatu|pn\s|perikatan|pakatan|ph\s|barisan nasional|\bbn\b)",
                      re.IGNORECASE)

def fetch(url, timeout=30):
    """Fetch with curl; return (http_code, body_text_or_empty, raw_bytes)."""
    try:
        proc = subprocess.run(
            ["curl", "-sS", "-L", "-m", str(timeout), "-A", UA,
             "--compressed", "-H", "Accept-Language: en-US,en;q=0.9,ms;q=0.8",
             "-w", "\n__HTTPCODE__:%{http_code}", url],
            capture_output=True, timeout=timeout+10)
        out = proc.stdout
        m = re.search(rb"__HTTPCODE__:(\d+)", out)
        code = m.group(1).decode() if m else "ERR"
        body = out[:m.start()] if m else out
        return code, body
    except Exception as e:
        return "ERR", b""

def is_article(href, host):
    """Heuristic: does href look like a news article (not nav/category/static)?"""
    if not href:
        return False
    p = urlparse(href)
    if p.netloc and p.netloc not in host and not host.endswith(p.netloc) and p.netloc not in host:
        # external link
        return False
    path = p.path.lower()
    if any(path.endswith(ext) for ext in [".jpg",".jpeg",".png",".gif",".css",".js",".svg",".ico",".webp",".pdf"]):
        return False
    # article-like paths: contain a year or /news/ /berita/ /article/ etc., and have some depth
    if re.search(r"/(news|berita|nasional|lokal|nation|article|sem|sembilan)/", path):
        return True
    if re.search(r"/20\d{2}/", path):
        return True
    if re.search(r"/\d{4,}", path):  # numeric id
        return True
    return False

TIME_RE = re.compile(r"(\b\d+\s*(min|mins|minute|minutes|hr|hrs|hour|hours|day|days|week|weeks)\s*(ago)\b|"
                     r"\bjust now\b|\bbaru\s+sahaja\b|\bjam\s+lepas\b|\bminit\s+lepas\b|"
                     r"\b\d{1,2}[:.]\d{2}\s*(am|pm)?\b|\bhari\s+ini\b|\bsemalam\b|"
                     r"\d{1,2}\s+(jam|minit|hari)\s+yang\s+lepas)", re.IGNORECASE)

def extract_articles(soup, base_url, host):
    """Return list of dicts: {title, url, time, snippet}."""
    arts = []
    seen = set()
    # Strategy 1: <article> containers
    for art in soup.find_all(["article"]):
        a = art.find("a", href=True)
        if not a:
            continue
        href = urljoin(base_url, a["href"])
        if not is_article(href, host):
            continue
        title = a.get_text(" ", strip=True)
        if len(title) < 8:
            # try heading inside
            h = art.find(["h1","h2","h3","h4"])
            if h: title = h.get_text(" ", strip=True)
        if len(title) < 8:
            continue
        if href in seen:
            continue
        seen.add(href)
        # time
        t = art.find("time")
        time_txt = t.get_text(" ", strip=True) if t else ""
        if not time_txt:
            txt = art.get_text(" ", strip=True)
            mt = TIME_RE.search(txt)
            time_txt = mt.group(0) if mt else ""
        # snippet: text excluding the title
        snippet = art.get_text(" ", strip=True)
        snippet = snippet.replace(title, "", 1).strip()
        arts.append({"title": title[:200], "url": href, "time": time_txt[:40], "snippet": snippet[:300]})
    # Strategy 2: standalone <a> with article-like href + decent text
    for a in soup.find_all("a", href=True):
        href = urljoin(base_url, a["href"])
        if href in seen:
            continue
        if not is_article(href, host):
            continue
        title = a.get_text(" ", strip=True)
        if len(title) < 12:
            continue
        # skip nav/category labels
        if title.lower() in ("news","nation","nasional","berita","more","read more","selanjutnya","lokal","sembilan"):
            continue
        seen.add(href)
        # look for time near this anchor
        parent = a.parent
        time_txt = ""
        for _ in range(3):
            if parent is None:
                break
            ptxt = parent.get_text(" ", strip=True) if hasattr(parent, "get_text") else ""
            mt = TIME_RE.search(ptxt)
            if mt:
                time_txt = mt.group(0)
                break
            parent = parent.parent
        arts.append({"title": title[:200], "url": href, "time": time_txt[:40], "snippet": ""})
    return arts

def tag_pir(text):
    tl = text.lower()
    tags = []
    for pir, kws in PIR.items():
        hits = [k for k in kws if k in tl]
        if hits:
            tags.append((pir, hits))
    return tags

def build_md(label, src_url, code, arts, full_text_len, host):
    lines = []
    lines.append(f"# {label} - PRN Negeri Sembilan 2026 News Collection")
    lines.append(f"Source URL: {src_url}")
    lines.append(f"Collected: {TODAY} {TS} UTC | Classification: TLP:AMBER")
    lines.append(f"HTTP: {code} | articles_extracted: {len(arts)} | page_text_bytes: {full_text_len}")
    lines.append("")
    lines.append("## Article Listing")
    lines.append("=" * 60)
    if not arts:
        lines.append("(no article listings extracted - see Page Text below)")
    prn_arts = []
    for a in arts:
        combined = a["title"] + " " + a["snippet"]
        tags = tag_pir(combined)
        is_prn = bool(PRN_PATS.search(combined))
        prefix = ""
        if tags:
            tagnames = " ".join(t for t, _ in tags)
            prefix = f"[PRIORITY {tagnames}] "
        elif is_prn:
            prefix = "[PRN-NS] "
        line = f"{prefix}{a['title']}"
        if a["time"]:
            line += f"  | {a['time']}"
        line += f"\n   {a['url']}"
        if a["snippet"]:
            line += f"\n   > {a['snippet']}"
        lines.append(line)
        lines.append("")
        prn_arts.append({**a, "tags": [t for t,_ in tags], "is_prn": is_prn})
    lines.append("=" * 60)
    lines.append("")
    return "\n".join(lines), prn_arts

def main():
    results = []
    for key, label, home, sec in SOURCES:
        host = urlparse(home).netloc
        code, body = fetch(sec)
        text = body.decode("utf-8", errors="replace") if body else ""
        soup = BeautifulSoup(text, "html.parser") if text else None
        arts = extract_articles(soup, sec, host) if soup else []
        # full page text for fallback / keyword sweep
        full_text = soup.get_text(" ", strip=True) if soup else ""
        md, prn_arts = build_md(label, sec, code, arts, len(full_text), host)
        # append full text (truncated) for keyword sweep visibility
        md += "\n## Page Text (extracted, truncated 6000 chars)\n" + "="*60 + "\n"
        md += full_text[:6000] + ("\n...[truncated]..." if len(full_text) > 6000 else "")
        md += "\n"
        fname = f"{key}_{TODAY}_{TS}.md"
        fpath = os.path.join(OUTDIR, fname)
        with open(fpath, "w", encoding="utf-8") as f:
            f.write(md)
        # also full-text keyword tags
        full_tags = tag_pir(full_text)
        results.append({
            "source": key, "label": label, "url": sec, "http_code": code,
            "article_count": len(arts),
            "priority_article_count": sum(1 for a in prn_arts if a["tags"]),
            "prn_article_count": sum(1 for a in prn_arts if a["is_prn"]),
            "priority_tags": [t for t,_ in full_tags],
            "file": fname,
            "prn_arts_titles": [a["title"] for a in prn_arts if a["tags"] or a["is_prn"]][:30],
        })
        print(f"[{code}] {key}: {len(arts)} articles, {sum(1 for a in prn_arts if a['tags'])} priority, {sum(1 for a in prn_arts if a['is_prn'])} PRN-NS -> {fname}")
    # save results summary for the metadata builder
    with open(os.path.join(OUTDIR, f"_scrape_results_{TS}.json"), "w") as f:
        json.dump({"timestamp": f"{TODAY}_{TS}", "results": results}, f, indent=2)
    print(f"\nSUMMARY saved. timestamp={TODAY}_{TS} outdir={OUTDIR}")
    return results

if __name__ == "__main__":
    main()
