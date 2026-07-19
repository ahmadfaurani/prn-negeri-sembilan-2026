#!/usr/bin/env python3
"""Update collection_metadata.json for cycle 20260718_231029 (5th overnight/dawn pass)."""
import json, os, datetime

BASE = "/home/p62operator/.openclaw/workspace-ns/04-DATA-AND-SOURCES/raw-scrapes/20260718"
META = os.path.join(BASE, "collection_metadata.json")
RESULTS = os.path.join(BASE, "_scrape_results_231029.json")

m = json.load(open(META, encoding="utf-8"))
R = json.load(open(RESULTS, encoding="utf-8"))

TS = "20260718_231029"
NOW_ISO = "2026-07-18 23:10:29 UTC (07:10 MYT 19 Jul 2026)"

# ---- top-level scalars ----
m["timestamp"] = TS
m["collected_utc"] = NOW_ISO
m["cycle_phase"] = ("Day-2 dawn MYT — 5th overnight/pre-dawn pass (07:10 MYT 19 Jul); FIRST cycle with genuinely new content after 4 consecutive zero-delta overnight passes. "
                    "Utusan published 2 brand-new PIR-07 articles at 06:40 & 06:45 MYT 19 Jul (22:40 & 22:45 UTC 18 Jul). Malaysiakini homepage rotated, surfacing 23 'new' priority titles "
                    "(mostly 10-22h-old nomination-day articles re-entering the top feed). Daytime MYT Day-2 campaign window opening.")

# ---- cycle_summary ----
res_sources = R["sources"]  # 16 per-source entries
scrape_md_files = [s["file"] for s in res_sources if "file" in s]
# universal gn files
gn_files = [f"google_news_{ukey.replace('_','')}_html_{TS}.md" for ukey in
            ["_universal_prn_bersatu","_universal_pn_pecat","_universal_nomination"]]
priority_files = [
    ("priority_pir-07_5-hot-seats-utusan_20260718_231029.md","PIR-07","Utusan: 5 hot/battleground DUN seats named with full candidate matchups (Linggi, Sikamat, Ampangan/N.14, Paroi, Labu). Brand-new 06:40 MYT 19 Jul. FULL TEXT."),
    ("priority_pir-07_3-coalitions-clash-utusan_20260718_231029.md","PIR-07+PIR-06","Utusan: 3 coalitions' strategies; Bersatu contests 24 DUN under own logo & CLASHES WITH PN IN 7 SEATS (first time own symbol); PH all 36, BN 25+PN 11, 103 candidates, seat structure 11/21/2/2-cornered. Brand-new 06:45 MYT 19 Jul. FULL TEXT."),
    ("priority_pir-07_aminuddin-linggi-mstar_20260718_231029.md","PIR-07","mStar: Aminuddin (MB/PH NS chief) confident stepping to Linggi adds PH wins. FULL TEXT."),
    ("priority_pir-09_wee-bnpn-not-merger-mkini_20260718_231029.md","PIR-09","mkini: MCA president Wee Ka Siong — BN-PN pact NOT a merger, each party retains ideology/stance. Intro (paywalled)."),
    ("priority_pir-09_tamim-independent-mkini_20260718_231029.md","PIR-09","mkini: Tamim surrenders to police, hopes to campaign for NS independent candidate. Intro (paywalled)."),
    ("priority_pir-07_kiniguide-shifting-alliances-mkini_20260718_231029.md","PIR-07","mkini KiniGuide: shifting alliances as battle royale for NS begins. Intro (paywalled)."),
    ("priority_pir-07_nominations-full-force-mkini_20260718_231029.md","PIR-07","mkini: coalition leaders/supporters in full force for NS nomination day. Intro (paywalled)."),
    ("priority_pir-07_dap-revives-anti-bn-mkini_20260718_231029.md","PIR-07","mkini: DAP revives anti-BN campaign (1MDB, ruler crisis) ahead of NS polls. Intro (paywalled)."),
    ("priority_pir-06_bersatu-crossroads-nst_20260718_231029.md","PIR-06","NST: 'Bersatu at a crossroads amid BN-PN cooperation' (pubDate 23:00 GMT 18 Jul = 07:00 MYT 19 Jul). HEADLINE ONLY — full text DEFERRED (gnews URL encrypted; NST JS-rendered; Bing/DDG search yielded no direct URL). Corroborates Muhyiddin exit thesis."),
    ("priority_pir-07_36-seats-contest-astro_20260718_231029.md","PIR-07","Astro Awani: contest for 36 DUN seats begins tomorrow (SPR Ramlan presser). HEADLINE ONLY — REDUNDANT with Utusan 3-coalitions (same SPR press conference, fully captured)."),
]
all_written = scrape_md_files + gn_files + [pf[0] for pf in priority_files] + [f"_scrape_results_{TS}.json"]
bytes_written = sum(os.path.getsize(os.path.join(BASE,f)) for f in all_written if os.path.exists(os.path.join(BASE,f)))

m["cycle_summary"] = {
    "sources_attempted": 10,
    "sources_successful": 10,
    "errors": 0,
    "strategies_deployed": ["wp-rest-api (utusan,kosmo,ohbulan)","html-extraction (malaysiakini,astroawani,thestar,tmi,mstar)","google-news-rss-per-source (nst,bharian,mstar,thestar,astroawani,malaysiakini)","google-news-rss-universal (PRN+Bersatu / PN+pecat+keluar / nomination)","priority-full-text-fetch (utusan-elementor, mstar, mkini-intro) + gnews-redirect-attempt (nst/astro-blocked)"],
    "files_written_this_cycle": len(all_written),
    "md_files_written_this_cycle": len(scrape_md_files)+len(gn_files)+len(priority_files),
    "priority_files_written_this_cycle": len(priority_files),
    "google_news_feed_files": len(gn_files),
    "results_json": f"_scrape_results_{TS}.json",
    "bytes_written_this_cycle": bytes_written,
    "cycle_character": ("FIRST NEW-CONTENT CYCLE after 4 consecutive zero-delta overnight passes (182751/194028/205755/220325). At 07:10 MYT 19 Jul (Day-2 dawn), Utusan published 2 genuinely brand-new PIR-07 articles at 06:40 & 06:45 MYT 19 Jul (22:40 & 22:45 UTC 18 Jul): 'Lima kerusi panas jadi tumpuan' (5 hot/battleground seats with FULL candidate matchups) and 'Tiga gabungan bertembung' (3 coalitions' strategies; confirms Bersatu contests 24 DUN seats under its OWN name/logo for the first time and CLASHES WITH PN CANDIDATES IN 7 SEATS; PH all 36, BN 25+PN 11; 103 total candidates; seat structure 11 two-cornered / 21 three-cornered / 2 four-cornered / 2 five-cornered; youngest 23 Leevineshwaraan Bersatu, oldest 70 Abd.Latif PH; campaign to 11:59pm 31 Jul). Malaysiakini homepage rotated, surfacing 23 'new' priority titles — mostly 10-22h-old nomination-day content re-entering the top feed; PIR-06 substance (Goodbye PN / Bersatu exit imminent / Muhyiddin raps Samsuri) already fully captured at 170837 and reconfirmed, but PIR-07 battleground + PIR-09 component-party items (Wee 'not a merger', Tamim/independent, KiniGuide, nominations full-force, DAP anti-BN) freshly captured this cycle. NST 'Bersatu at a crossroads amid BN-PN cooperation' (pubDate 23:00 GMT 18 Jul) is NEW corroborative PIR-06 — headline captured, full text deferred (gnews encrypted). PIR-06 CRITICAL threshold NOT crossed (formal_removal_notice_detected=false, precursor items 0); escalated-watch carries forward. Net: PIR-07 BATTLEGROUN ASSESSMENT substantially enriched (5 named hot seats + candidate fields + 7 Bersatu-vs-PN clash seats + 103-candidate/seat-structure confirmation). 10/10 sources, 0 errors, all 16 streams HTTP 200."),
    "key_obstacle_resolved": "Utusan article-body extraction fixed: selector upgraded to 'div.elementor-widget-theme-post-content' (Utusan uses Elementor) — both brand-new Utusan PIR-07 articles now extracted in FULL (2455 + 3891 chars). Prior pass only got a related-link heading (32 chars).",
    "key_obstacle_partial": "NST 'Bersatu at a crossroads' full text NOT retrievable this cycle: gnews article URL post-2024 is protobuf-encrypted (base64 decode yields no clean http URL); the gnews article-page (600KB) does not expose the publisher URL in extractable data-attributes/JS via curl; NST /news/nation is JS-rendered (0 article cards in static HTML); Bing + DuckDuckGo title-search returned no direct nst.com.my URL (article too new / results JS-rendered). Headline+publisher+pubDate+PIR-06 tag captured in raw scrape; full body DEFERRED to a daytime-MYT targeted fetch (consistent with prior cycles' documented NST/Star deferral). Astro Awani '36 kerusi bermula esok' headline-only — REDUNDANT with Utusan 3-coalitions (same SPR Ramlan press conference, fully captured). Malaysiakini bodies remain paywalled (lead paragraph captured for 5 priority articles).",
    "methodology_improvement_this_cycle": "Added priority full-text fetcher (_fetch_priority_231029.py) with Utusan Elementor-aware body extraction and gnews-redirect + Bing/DDG fallback attempts for encrypted-URL publishers. Delta-detection now distinguishes 'genuinely brand-new' (WP-API MYT-zoned timestamps within the cycle window — the 2 Utusan articles) from 'homepage-rotation resurfacing' (mkini 'Xh-ago' titles re-entering the top feed). This resolves over-counting: 34 globally-new priority titles reduce to ~2 genuinely brand-new articles + ~32 rotation resurfacings."
}

# ---- critical_pir06_alert ----
ca = m["critical_pir06_alert"]
ca["status"] = ("ESCALATED WATCH — UNCHANGED. NO formal PN Supreme Council (Majlis Tertinggi) removal notice for Bersatu has been issued. CRITICAL threshold NOT crossed (formal_removal_notice_detected=false, precursor items 0). "
                "This cycle (07:10 MYT 19 Jul, 5th overnight/dawn pass) added CORROBORATIVE PIR-06 content only: (a) NST 'Negri Sembilan polls: Bersatu at a crossroads amid BN-PN cooperation' (pubDate 23:00 GMT 18 Jul = 07:00 MYT 19 Jul) — headline-level capture, full text deferred (gnews encrypted); corroborates the Muhyiddin exit-positioning thesis captured at 170837. "
                "(b) Utusan 'Tiga gabungan bertembung' empirically confirms Bersatu contests 24 DUN seats under its OWN logo (first time) and CLASHES WITH PN CANDIDATES IN 7 SEATS — a tangible PIR-06 schism signal but NOT a formal MT removal notice. "
                "Trajectory remains two-sided: PN-MT-may-remove-Bersatu (Kiandee 'asas kukuh' call, captured 153251) AND Bersatu-may-exit-PN (Muhyiddin 'Goodbye PN' hint, captured 170837). Automated CRITICAL-pattern regex matched 0 titles across all 29 files this cycle; precursor-pattern (asas kukuh / kiandee) returned 0.")
ca["formal_removal_notice_detected"] = False
ca["escalation_detected"] = True
ca["this_cycle_new_pir06_content"] = True
ca["negative_confirmation"] = ("Automated CRITICAL-pattern regex (formal PN-MT removal-notice phrasing) matched 0 titles across all 29 collected files this cycle. Precursor-pattern (asas kukuh / kiandee) items returned 0. "
                               "The two PIR-06-relevant items this cycle are NON-triggering: (1) NST 'Bersatu at a crossroads' is ANALYSIS/corroboration of the exit thesis, not an MT-issued notice; (2) Utusan '7 Bersatu-vs-PN clash seats' is an empirical campaign-configuration fact, not a removal notice. "
                               "Universal Google News 'PN Bersatu (pecat OR keluar OR buang)' feed re-fetched; no formal MT-issued removal notice surfaced (Hadi-denial 'PAS cannot unilaterally kick out Bersatu' still the dominant hit — a 12 Jun NEGATIVE statement, not a notice).")
ca["key_new_evidence_this_cycle"] = [
    {"rank":"CORROBORATING (PIR-06, not a notice)","headline":"Negri Sembilan polls: Bersatu at a crossroads amid BN-PN cooperation","source":"New Straits Times","pubdate_gmt":"Sat, 18 Jul 2026 23:00:40 GMT (07:00 MYT 19 Jul)","url":"gnews-encrypted; direct URL not recovered","pir_significance":"NST analysis piece framing Bersatu's position post BN-PN pact. Corroborates Muhyiddin exit-positioning. Full text deferred (gnews encrypted / NST JS-rendered). Headline captured.","file":"priority_pir-06_bersatu-crossroads-nst_20260718_231029.md"},
    {"rank":"EMPIRICAL-SCHISM-SIGNAL (PIR-06, not a notice)","headline":"Tiga gabungan bertembung / Bersatu clashes with PN in 7 seats","source":"Utusan Malaysia","pubdate_myt":"2026-07-19T06:45:12 (22:45 UTC 18 Jul)","url":"https://www.utusan.com.my/berita/2026/07/tiga-gabungan-bertembung/","pir_significance":"First empirical confirmation that Bersatu (still a PN component) contests 24 DUN seats under its OWN logo and directly clashes with PN candidates in 7 seats — a tangible manifestation of the PN-Bersatu schism on the ballot. NOT a formal MT removal notice.","file":"priority_pir-07_3-coalitions-clash-utusan_20260718_231029.md"}
]
# preserve carryover_primary_evidence, trajectory_assessment, tier4_candidate_withdrawal_trigger as-is

# ---- tier4_seats_bersatu_vs_pn_component (UPDATE with 7-seat confirmation) ----
m["tier4_seats_bersatu_vs_pn_component"] = {
    "confirmed_count": 7,
    "match_to_pir06_list": ("Utusan 'Tiga gabungan bertembung' (06:45 MYT 19 Jul) confirms Bersatu clashes with PN in 7 DUN seats. The 5-hot-seats article names Bersatu-vs-PN-both-running clashes in at least: Sikamat (Tun Faisal Bersatu vs Razali PN), Ampangan/N.14 (Noor'azah Bersatu vs Rafie PN), Paroi (Nazree Bersatu vs Kamarol PN), Labu (Hanifah Bersatu incumbent vs PN/BN). Full 7-seat enumeration pending the complete candidate list cross-check (manual_senarai-calon captured 130328). Note: Bersatu contests 24 seats total; the 7 are the subset with a direct PN opponent."),
    "seats": ["Sikamat","Ampangan (N.14)","Paroi","Labu","(3 further seats pending full cross-check vs 36-seat list)"],
    "component_split": "Bersatu 24 seats (own logo) vs PN (PAS-led) filling 11 seats under BN-PN understanding; PH 36; BN 25.",
    "source": "priority_pir-07_3-coalitions-clash-utusan_20260718_231029.md + priority_pir-07_5-hot-seats-utusan_20260718_231029.md",
    "pir06_significance": "Empirical ballot-level schism: a PN component (Bersatu) running against its own coalition (PN) in 7 seats under a separate logo is the strongest on-the-ground evidence to date of the PN-Bersatu fracture — but is NOT a formal MT removal notice. No candidate tarik diri in the 8 Tier-4 seats (N.04/05/13/14/23/25/31/34) detected this cycle.",
    "tier4_candidate_withdrawal_detected": False
}

# ---- pir09_candidate_credibility ----
m["pir09_candidate_credibility"] = {
    "cycle_status": "PIR-09 enriched this cycle. N.14 Ampangan Day-1 messaging war now fully baseline-candidate-confirmed: Nazri Kassim (PH, new, PKR NS dep chief) vs Datuk Dr. Mohamad Rafie Ab. Malek (PN, former ADUN) vs Noor'azah Harun (Bersatu) — a THREE-cornered fight (2023 margin 329). MCA president Wee Ka Siong publicly clarifies BN-PN pact is NOT a merger (component-party messaging). Independent-candidate angle: Tamim (surrendered to police) hopes to campaign for an NS independent candidate. Gerakan pecat Tang Jay Son (carryover) unchanged. No new Bersatu-candidate disciplinary action or pecat this cycle.",
    "new_this_cycle": [
        "Wee Ka Siong (MCA president): BN-PN pact not a merger, each party retains ideology/stance — priority_pir-09_wee-bnpn-not-merger-mkini (intro, paywalled).",
        "Tamim surrenders to police, to campaign for NS independent candidate — priority_pir-09_tamim-independent-mkini (intro, paywalled).",
        "N.14 Ampangan 3-cornered fight confirmed (Nazri Kassim PH vs Rafie PN vs Noor'azah Bersatu) — priority_pir-07_5-hot-seats-utusan."
    ],
    "reconfirmed_this_cycle": ["Gerakan expulsion of Tang Jay Son (carryover, unchanged)","MCA Youth sec-gen 'stay out of NS polls' (carryover, re-surfaced in mkini rotation)","Albert (PN camp) 'barking dogs' (carryover, re-surfaced)"],
    "carryover_from_prior_cycle": ["4 independents' backgrounds still partially pending (Datuk A Saravanan N.33 title/establishment background pending)"]
}

# ---- pir07_battleground (MAJOR update) ----
m["pir07_battleground"] = {
    "nomination_day_confirmed": True,
    "total_candidates": 103,
    "candidate_breakdown": "PH 36 seats (all 36) | BN 25 | PN 11 (under BN-PN understanding) | Bersatu 24 (own logo, first time) | Berjasa 1 | Asli (Parti Orang Asli) 1 | PSM 1 | Independents 4. 94 men / 9 women. Youngest 23 (M. Leevineshwaraan, Bersatu); oldest 70 (Abd. Latif A. Tambi, PH).",
    "seat_contest_structure": "11 two-cornered | 21 three-cornered | 2 four-cornered | 2 five-cornered (of 36 DUN).",
    "five_hot_seats_named": ["Linggi (Aminuddin/PH-MB vs Faizal/BN-incumbent vs Zamri/Bersatu; 2023 Faizal beat Zamri-PN by 1461)","Sikamat (Nor Azman/PH vs Tun Faisal/Bersatu vs Razali/PN; Aminuddin's old seat 2008-)","Ampangan N.14 (Nazri Kassim/PH-new vs Rafie/PN-former-ADUN vs Noor'azah/Bersatu; 2023 margin 329)","Paroi (Kamarol/PN-incumbent-largest-electorate vs Ahmad Shahir/PH vs Nazree/Bersatu)","Labu (Hanifah/Bersatu-incumbent vs Ahmad Faez/PH vs Siti Umaira/BN)"],
    "bersatu_vs_pn_clash_seats": 7,
    "cycle_status": "PIR-07 SUBSTANTIALLY ENRICHED this cycle (the cycle's main yield). 5 hot/battleground seats named with full candidate matchups; 7 Bersatu-vs-PN clash seats confirmed; 103-candidate/seat-structure confirmed from SPR chairman Ramlan Harun. Day-1 campaign activity reconfirmed (coalition leaders/supporters in full force at nominations; Aminuddin to Linggi; DAP revives anti-BN messaging; Loke 'campaign of hope'). No poll/forecast publication detected.",
    "new_this_cycle": [
        "5 hot seats named + candidate fields (Utusan 5-hot-seats, full text) — priority_pir-07_5-hot-seats-utusan",
        "3-coalition strategy + 7 Bersatu-vs-PN clashes + 103 candidates + seat structure (Utusan 3-coalitions, full text) — priority_pir-07_3-coalitions-clash-utusan",
        "Aminuddin confident on Linggi move (mStar, full text) — priority_pir-07_aminuddin-linggi-mstar",
        "KiniGuide shifting alliances battle royale (mkini intro) — priority_pir-07_kiniguide-shifting-alliances-mkini",
        "Coalition leaders/supporters full force at nominations (mkini intro) — priority_pir-07_nominations-full-force-mkini",
        "DAP revives anti-BN campaign (1MDB, ruler crisis) (mkini intro) — priority_pir-07_dap-revives-anti-bn-mkini",
        "Astro Awani: 36-seat contest begins (redundant w/ Utusan) — priority_pir-07_36-seats-contest-astro"
    ],
    "reconfirmed_this_cycle": ["BN manifesto launch 24 Jul (carryover)","Tok Mat 'keep adat out of polls' (mkini rotation)","Loke 'campaign of hope' (mkini rotation)"],
    "manifesto_and_messaging": "BN manifesto launch 24 Jul (carryover). DAP revives anti-BN rhetoric (1MDB, ruler crisis) — tension within PH-BN cooperation. MCA Wee: BN-PN not a merger.",
    "marquee_day1_events": "Nomination day full-force turnout by coalition leaders/supporters (mkini). Aminuddin (MB) moved from Sikamat to Linggi (marquee contest vs BN incumbent + Bersatu).",
    "adjacent_election_distractor_note": "PRN Johor ke-16 (concurrent) items continue to surface in feeds (Johor exco lineup, Johor regent on excos) — kept excluded from NS PIR accounting."
}

# ---- sources (refresh from results JSON) ----
m["sources"] = res_sources

# ---- google_news_universal_feeds ----
m["google_news_universal_feeds"] = [
    {"file": f"google_news_universalprnbersatu_html_{TS}.md","query":"PRN Negeri Sembilan Bersatu","note":"Cross-outlet PRN+Bersatu feed."},
    {"file": f"google_news_universalpnpecat_html_{TS}.md","query":"PN Bersatu (pecat OR keluar OR buang)","note":"PIR-06 negative-confirmation feed: no formal PN-MT removal-notice article; Hadi-denial ('cannot unilaterally kick out Bersatu', 12 Jun) remains dominant NEGATIVE hit."},
    {"file": f"google_news_universalnomination_html_{TS}.md","query":"(nomination OR penamaan) Negeri Sembilan","note":"Nomination-day cross-outlet feed."}
]

# ---- priority_files_created_this_cycle ----
m["priority_files_created_this_cycle"] = [
    {"file":pf[0],"pir":pf[1],"note":pf[2]} for pf in priority_files
]

# ---- monitor_channels_active ----
m["monitor_channels_active"] = {
    "kiandee_social": "ACTIVE (carryover) — Utusan confirms Kiandee 'asas kukuh / mengeluarkan Bersatu' Facebook statement (Malay original). Still a CALL on PN-MT, not an MT notice. No new Kiandee output this cycle.",
    "muhyiddin_channel": "ACTIVE (carryover/reconfirmed) — Muhyiddin exit-positioning reconfirmed via mkini 'Goodbye PN' (779941) + 'Bersatu kini pembangkang tunggal' + NST 'Bersatu at a crossroads' (NEW this cycle, corroborative). HIGHEST-WEIGHT PIR-06 channel. No qualitatively new Muhyiddin statement this cycle.",
    "annuar_musa_channel": "ACTIVE (carryover) — Bersatu sec-gen states Bersatu wants to part ways (own-logo signal). Now EMPIRICALLY CONFIRMED on the ballot: Bersatu contests 24 seats under own logo (Utusan 3-coalitions).",
    "hadi_channel": "ACTIVE (carryover) — Hadi framing BN-PN as 'friendship, brotherhood'; Hadi denies PAS made PN 'toxic', blames Bersatu. Re-surfaced in mkini snapshot rotation. No new Hadi output this cycle.",
    "samsuri_channel": "ACTIVE (carryover/reconfirm) — Samsuri signals PN may continue BN cooperation if NS results positive. Reconfirmed.",
    "bernama_wire": "ACTIVE — BERNAMA/Mediacorp carries NS polls coverage; Astro Awani '36 kerusi bermula esok' (BERNAMA-sourced SPR presser) reconfirmed.",
    "pn_component_parties": "ACTIVE (ENRICHED) — Gerakan pecat Tang Jay Son (reconfirmed); MCA president Wee publicly clarifies BN-PN not a merger (NEW this cycle); MCA Youth sec-gen 'stay out' (re-surfaced). No new PAS/Bersatu disciplinary action this cycle."
}

# ---- next_cycle_watch ----
m["next_cycle_watch"] = [
    "PIR-06 CRITICAL trigger: ANY formal PN Supreme Council (Majlis Tertinggi) removal notice for Bersatu — keyword watch on 'mengeluarkan Bersatu daripada PN' issued BY the MT (not Kiandee's call ON the MT). The 7 Bersatu-vs-PN ballot clashes are an empirical schism signal but NOT the trigger.",
    "PIR-06: Muhyiddin follow-through on 'new bloc/coalition after Negri polls' — any concrete announcement of Bersatu's new alliance partners.",
    "PIR-06: Any Bersatu candidate tarik diri in the 8 Tier-4 seats (N.04/05/13/14/23/25/31/34) — would signal internal Bersatu collapse. None detected this cycle.",
    "PIR-06: Full text of NST 'Bersatu at a crossroads amid BN-PN cooperation' — recover via direct NST URL at the next daytime-MYT cycle (gnews encrypted; try NST sitemap/section pagination or a later Bing re-index).",
    "PIR-09: N.14 Ampangan Day-2 messaging evolution (Day-2 = 19 Jul MYT daytime) — PH 'defector' attack vs PN 'experienced rep' counter; Noor'azah (Bersatu) third-candidate impact. Candidate field now CONFIRMED: Nazri Kassim (PH) vs Rafie (PN) vs Noor'azah (Bersatu).",
    "PIR-09: MCA president Wee 'not a merger' clarification fallout + MCA Youth sec-gen Saw Yee Fung — whether further BN-component cracks over the BN-PN pact widen.",
    "PIR-09: Independent background vetting — Datuk A Saravanan (N.33) title/establishment background still pending; Tamim's independent-candidate link to follow.",
    "PIR-07: Full 7-seat enumeration of Bersatu-vs-PN clashes (cross-check Utusan 3-coalitions '7 seats' vs the 36-seat candidate list captured 130328).",
    "PIR-07: BN manifesto launch 24 Jul; Day-2 daytime MYT campaign events at T1/T2 seats; any poll/forecast publications. Daytime MYT window (~09:00-12:00 MYT 19 Jul) is NOW OPENING — next cycle expected to capture Day-2 campaign events.",
    "Distractor guard: PRN Johor ke-16 (concurrent) items (Johor exco, regent) surface in NS feeds — keep excluded from NS PIR accounting."
]

# ---- delta_vs_prior_cycle_220325 (NEW) ----
m["delta_vs_prior_cycle_220325"] = {
    "prior_cycle_time": "20260718_220325 (22:03 UTC 18 Jul / 06:03 MYT 19 Jul)",
    "this_cycle_time": f"{TS} (23:10 UTC 18 Jul / 07:10 MYT 19 Jul)",
    "wall_clock_window_note": "~67 min after the 220325 pass; 5th overnight/dawn pass; Day-2 MYT dawn. This is the FIRST cycle to break the 4-pass zero-delta streak.",
    "genuinely_new_findings": [
        "Utusan 'Lima kerusi panas jadi tumpuan' — brand-new 06:40 MYT 19 Jul (22:40 UTC 18 Jul). 5 hot seats + full candidate matchups. FULL TEXT captured.",
        "Utusan 'Tiga gabungan bertembung' — brand-new 06:45 MYT 19 Jul (22:45 UTC 18 Jul). 3-coalition strategy + 7 Bersatu-vs-PN clashes + 103 candidates + seat structure. FULL TEXT captured.",
        "NST 'Bersatu at a crossroads amid BN-PN cooperation' — pubDate 23:00 GMT 18 Jul (07:00 MYT 19 Jul). NEW corroborative PIR-06. Headline only (full text deferred).",
        "Malaysiakini homepage rotation surfaced 23 'new' priority titles (10-22h-old nomination-day articles re-entering top feed) — substance of PIR-06 items already captured 170837; PIR-07/09 items freshly captured as priority intros this cycle."
    ],
    "delta_scan_result": "Set-difference on normalized priority_titles: 34 globally-new titles vs the 220325 baseline. Of these, 2 are genuinely brand-new (Utusan, MYT-zoned WP-API timestamps within the cycle window) and ~32 are mkini/mstar homepage-rotation resurfacings of already-published content (verified via 'Xh ago' relative-timestamp markers). PIR-06 CRITICAL regex: 0. Precursor items: 0.",
    "newly_surfaced_in_per_source_delta": {"utusancommy":4,"utusancommy_html":3,"malaysiakinicom":23,"mstarcommy":2,"nstcommy":1,"astroawanicom_gn":1},
    "no_change": ["PIR-06 CRITICAL threshold (not crossed)","precursor items (0)","PIR-06 escalated-watch status","Gerakan pecat Tang Jay Son","Muhyiddin/Samsuri/Hadi statements (substance unchanged)"],
    "source_coverage_this_cycle": "10/10 sources, 0 errors, all 16 streams HTTP 200. Utusan body extraction methodology fixed (Elementor selector) — recovers 2 brand-new articles in full."
}

# ---- prior_cycles_today (add this cycle, preserve prior) ----
m["prior_cycles_today"]["231029_cycle"] = ("THIS cycle — 5th overnight/dawn pass (07:10 MYT 19 Jul, Day-2 dawn). FIRST cycle with genuinely new content after 4 consecutive zero-delta overnight passes. "
    "10/10 sources, 0 errors, all 16 streams HTTP 200, 29 md files / {bytes} bytes. Brand-new Utusan PIR-07 articles at 06:40 & 06:45 MYT 19 Jul captured in FULL (5 hot seats + candidate matchups; 3-coalition strategy + 7 Bersatu-vs-PN clashes + 103 candidates + seat structure). "
    "mkini homepage rotation surfaced 23 'new' priority titles (10-22h-old, mostly re-surfaced; PIR-07/09 intros freshly captured). NST 'Bersatu at a crossroads' (NEW corroborative PIR-06, headline only, full text deferred — gnews encrypted). "
    "PIR-06 CRITICAL threshold NOT crossed (formal_removal_notice_detected=false, precursor 0); escalated-watch carries forward. PIR-07 BATTLEGROUN ASSESSMENT substantially enriched. Utusan Elementor body-extraction fixed. "
    "Value = first new content of the Day-2 window + PIR-07 baseline establishment + PIR-06 corroboration. Daytime MYT campaign window now opening — next cycle should capture Day-2 campaign events.").format(bytes=bytes_written)

# ---- tooling_artifacts ----
ta = m.get("tooling_artifacts_in_raw_scrapes_dir", [])
# add this cycle's artifacts if not present
for a in [f"_scrape_results_{TS}.json (structured cycle results + CRITICAL-flag computation — THIS cycle)",
          "_fetch_priority_231029.py (priority full-text fetcher w/ Utusan Elementor extraction + gnews-redirect/Bing/DDG fallback — THIS cycle)"]:
    # avoid duplicates
    key = a.split(" (")[0]
    if not any(key in x for x in ta):
        ta.append(a)
m["tooling_artifacts_in_raw_scrapes_dir"] = ta

# write back
with open(META,"w",encoding="utf-8") as f:
    json.dump(m,f,indent=2,ensure_ascii=False)

print("=== METADATA UPDATED ===")
print("timestamp:",m["timestamp"])
print("collected_utc:",m["collected_utc"])
print("cycle_summary.priority_files_written_this_cycle:",m["cycle_summary"]["priority_files_written_this_cycle"])
print("cycle_summary.md_files_written_this_cycle:",m["cycle_summary"]["md_files_written_this_cycle"])
print("cycle_summary.bytes_written_this_cycle:",m["cycle_summary"]["bytes_written_this_cycle"])
print("critical_pir06_alert.formal_removal_notice_detected:",m["critical_pir06_alert"]["formal_removal_notice_detected"])
print("tier4.bersatu_vs_pn_clash_seats:",m["tier4_seats_bersatu_vs_pn_component"]["confirmed_count"])
print("pir07.five_hot_seats_named:",len(m["pir07_battleground"]["five_hot_seats_named"]))
print("pir07.total_candidates:",m["pir07_battleground"]["total_candidates"])
print("prior_cycles count:",len(m["prior_cycles_today"]))
print("delta_vs_prior_cycle_220325 keys:",list(m["delta_vs_prior_cycle_220325"].keys()))
print("priority_files_created_this_cycle:",len(m["priority_files_created_this_cycle"]))
print("metadata bytes:",os.path.getsize(META))
