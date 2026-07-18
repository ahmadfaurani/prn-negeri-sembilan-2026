#!/usr/bin/env python3
"""Debug: inspect link structure of sources to fix extractor."""
import subprocess, re
from urllib.parse import urljoin, urlparse
from bs4 import BeautifulSoup

UA = ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36")

def fetch(url):
    p = subprocess.run(["curl","-sS","-L","-m","30","-A",UA,"--compressed",url],
                       capture_output=True, timeout=40)
    return p.stdout

sources = {
    "nst": "https://www.nst.com.my/news/nation",
    "thestar": "https://www.thestar.com.my/news/nation",
    "astroawani": "https://www.astroawani.com",
    "kosmo": "https://www.kosmo.com.my",
    "mstar": "https://www.mstar.com.my",
    "ohbulan": "https://www.ohbulan.com",
    "malaysiakini": "https://www.malaysiakini.com",
    "bharian": "https://www.bharian.com.my",
    "tmi": "https://www.themalaysianinsight.com",
}

for name, url in sources.items():
    print(f"\n===== {name} :: {url} =====")
    body = fetch(url)
    if not body:
        print("  EMPTY response"); continue
    soup = BeautifulSoup(body.decode("utf-8","replace"), "html.parser")
    base = url
    host = urlparse(url).netloc
    # collect article-like links
    links = []
    for a in soup.find_all("a", href=True):
        href = urljoin(base, a["href"])
        p = urlparse(href)
        if p.netloc and p.netloc != host:
            continue
        path = p.path.lower()
        if re.search(r"\.(jpg|png|gif|css|js|svg|ico|webp|pdf)$", path):
            continue
        txt = a.get_text(" ", strip=True)
        alt = ""
        img = a.find("img")
        if img and img.get("alt"):
            alt = img.get("alt")
        title_attr = a.get("title","")
        links.append((href, txt[:80], alt[:80], title_attr[:80]))
    # show first 15 distinct hrefs
    seen=set()
    c=0
    for href, txt, alt, ta in links:
        if href in seen: continue
        seen.add(href)
        # only show ones that look like articles
        if re.search(r"/(news|berita|nasional|nation|lokal|article|sembilan|sem)/|/20\d{2}/|/\d{4,}", href.lower()):
            label = (txt or alt or ta or "(no text)")
            print(f"  {href[:90]}")
            print(f"      txt='{txt[:60]}' alt='{alt[:40]}' title='{ta[:40]}' label='{label[:70]}'")
            c+=1
        if c>=12: break
