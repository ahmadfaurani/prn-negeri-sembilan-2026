#!/usr/bin/env python3
"""
PRN Negeri Sembilan 2026 — Entity Extraction Agent (scheduled cron build)
Build: entities_233104.json  (2026-07-18T23:31:04+00:00 UTC / 07:31 MYT 19 Jul)

Cycle ingested: 231029 (5th overnight/dawn pass; FIRST genuinely-new-content cycle
after 4 consecutive zero-delta passes). Two brand-new Utusan PIR-07 articles
(06:40 & 06:45 MYT 19 Jul) + freshly-captured PIR-09 component-party items.

Build character: ENRICHMENT / CORROBORATION BUILD.
  - 1 genuinely NEW named figure: Datuk Alzafny Ahmad (NS Police Chief)
  - Confirmed full names: Wee Ka Siong (MCA president), Tamim Dahri Abd Razak
  - Formal "5 hot seats" battleground designation (full candidate matchups + role
    affiliations) from Utusan full-text
  - 7 Bersatu-vs-PN clash seats confirmed (empirical ballot-level schism)
  - Operational/electoral-configuration detail (94M/9W, campaign to 31 Jul,
    36 PP-KPR, 8 centres, 2373 PDRM, no papers rejected)
  - NST PIR-06 corroboration (Bersatu at a crossroads) — NOT a removal notice
  - NO new candidates discovered (103-candidate roster UNCHANGED)
  - CRITICAL PIR-06 threshold (formal PN-MT removal notice) STILL NOT crossed

Classification: TLP:AMBER
"""
import json
import copy
from pathlib import Path
from datetime import datetime, timezone, timedelta

BASE_DIR = Path("/home/p62operator/.openclaw/workspace-ns/04-DATA-AND-SOURCES/processed-entities/20260718")
PRIOR_FILE = BASE_DIR / "entities_211155.json"
THIS_FILE_ID = "entities_233104"
THIS_FILE = BASE_DIR / f"{THIS_FILE_ID}.json"
META_FILE = BASE_DIR / "entity_metadata.json"

# --- load baseline ---
with open(PRIOR_FILE, "r", encoding="utf-8") as f:
    data = json.load(f)

# snapshot for delta accounting
prior_total_entities = data.get("pir_priority_index", {}).get("PIR-07", {}).get("total_candidates", 103)

# ===========================================================================
# 1. Top-level metadata fields
# ===========================================================================
MYT = timezone(timedelta(hours=8))
now_utc = datetime(2026, 7, 18, 23, 31, 4, tzinfo=timezone.utc)
now_myt = now_utc.astimezone(MYT)

data["processing_timestamp_utc"] = "2026-07-18T23:31:04+00:00"
data["processing_timestamp_myt"] = "2026-07-19T07:31:04+08:00"
data["file_id"] = THIS_FILE_ID
data["cycle"] = (
    "nomination-day-surge + Day-2 dawn enrichment (231029 cycle: FIRST genuinely-"
    "new-content cycle after 4 zero-delta passes; 2 brand-new Utusan PIR-07 "
    "articles 06:40/06:45 MYT 19 Jul + PIR-09 component-party items; entities_211155 "
    "baseline + 231029 enrichment)"
)
data["prior_entities_file"] = "entities_211155.json"

# extend source_files_pir_relevant with the new 231029 priority files
new_priority_files = [
    "priority_pir-07_5-hot-seats-utusan_20260718_231029.md (NEW — 5 hot seats FULL candidate matchups + role affiliations; Utusan Elementor full-text 06:40 MYT 19 Jul)",
    "priority_pir-07_3-coalitions-clash-utusan_20260718_231029.md (NEW — 3 coalitions strategy; Bersatu 24 own-logo seats + 7 Bersatu-vs-PN clash seats; 103 candidates/seat-structure from SPR Ramlan; Alzafny police; Utusan full-text 06:45 MYT 19 Jul)",
    "priority_pir-06_bersatu-crossroads-nst_20260718_231029.md (NEW — NST 'Bersatu at a crossroads amid BN-PN cooperation'; headline-only, full text deferred gnews-encrypted; PIR-06 corroboration NOT a removal notice)",
    "priority_pir-07_aminuddin-linggi-mstar_20260718_231029.md (NEW full-text — Aminuddin confident on Linggi move; 4-term Sikamat -> Linggi; mStar)",
    "priority_pir-07_dap-revives-anti-bn-mkini_20260718_231029.md (NEW intro — DAP anti-BN fundraising dinner Bandar Utama 11; 1MDB, ruler crisis; paywalled)",
    "priority_pir-07_nominations-full-force-mkini_20260718_231029.md (NEW intro — coalition leaders full force; Aminuddin at PD District Admin Complex 8:30am; Bernama)",
    "priority_pir-07_kiniguide-shifting-alliances-mkini_20260718_231029.md (NEW intro — KiniGuide: BN post-Johor-landslide, 2023 BN+PH pact vs PN; paywalled)",
    "priority_pir-09_tamim-independent-mkini_20260718_231029.md (NEW intro — Tamim Dahri Abd Razak, 33, surrenders at PD IPD 12:45pm -> Seremban court remand; NST quotes Alzafny; paywalled)",
    "priority_pir-09_wee-bnpn-not-merger-mkini_20260718_231029.md (NEW intro — MCA president Wee Ka Siong: BN-PN pact not a merger, each party retains ideology; CONFIRMS full name; paywalled)",
    "priority_pir-07_36-seats-contest-astro_20260718_231029.md (NEW headline-only — Astro Awani via gnews; redundant w/ Utusan 3-coalitions; body not extracted)",
    "collection_metadata.json (231029 cycle — FIRST new-content cycle; 2 brand-new Utusan PIR-07 articles + PIR-09 component items; PIR-06 escalated-watch unchanged)"
]
data.setdefault("source_files_pir_relevant", [])
data["source_files_pir_relevant"] = data["source_files_pir_relevant"] + new_priority_files

# ===========================================================================
# 2. national_figures_and_pir_actors — enrichments + new figure
# (figures live under data["politicians"]["national_figures_and_pir_actors"];
#  total_unique_persons is a sibling int under data["politicians"])
# ===========================================================================
nfa = data["politicians"]["national_figures_and_pir_actors"]

# 2a. NEW figure: Datuk Alzafny Ahmad (NS Police Chief)
alzafny = {
    "name": "Datuk Alzafny Ahmad",
    "aliases": ["Alzafny Ahmad"],
    "role": "Ketua Polis Negeri Sembilan (Negeri Sembilan Police Chief)",
    "party": "(official / PDRM)",
    "pir_tags": ["PIR-07", "PIR-09"],
    "pir07_role": (
        "Held a press conference at Kompleks Pentadbiran Daerah Port Dickson on "
        "Nomination Day: confirmed 2,373 PDRM officers deployed for nomination "
        "security; 8 nomination centres ran smoothly with no untoward incidents / "
        "no police reports; each centre drew 1,000-2,500 supporters (Jempol most, "
        "Kuala Pilah least); reminded candidates to campaign ethically and avoid 3R "
        "(religion, rulers, race) provocations. (Utusan 3-coalitions, full text.)"
    ),
    "pir09_role": (
        "Quoted (via NST) in Malaysiakini: activist Tamim Dahri Abd Razak (33) "
        "surrendered himself at the Port Dickson district police HQ at ~12:45pm; "
        "to be brought to Seremban court for remand application (religious-"
        "provocation charges). PIR-09 independent-support-network context."
    ),
    "sources": [
        "Utusan (priority_pir-07_3-coalitions-clash-utusan_20260718_231029)",
        "Malaysiakini (priority_pir-09_tamim-independent-mkini_20260718_231029)"
    ],
    "first_captured_cycle": "231029"
}
# insert near Ramlan Harun (SPR chairman) for grouping; append if not found
inserted = False
for i, e in enumerate(nfa):
    if e.get("name") == "Datuk Seri Ramlan Harun":
        nfa.insert(i + 1, alzafny)
        inserted = True
        break
if not inserted:
    nfa.append(alzafny)

# 2b. Update Dr Wee -> confirm full name Wee Ka Siong (rm inference caveat)
for e in nfa:
    if e.get("name") == "Dr Wee":
        e["name"] = "Datuk Dr Wee Ka Siong"
        e["aliases"] = ["Dr Wee", "Wee Ka Siong", "Wee"]
        e["role"] = "MCA President; BN component leader"
        e.setdefault("pir_tags", [])
        if "PIR-09" not in e["pir_tags"]:
            e["pir_tags"].append("PIR-09")
        e["pir09_role"] = (
            "MCA president. Publicly clarified (press conference, mkini 780035) that "
            "the BN-PN electoral pact for NS is NOT a merger — each party retains its "
            "own ideology and stance; aimed at ensuring continued development under a "
            "strong, stable state government. Followed backlash over the BN-PN "
            "cooperation decision. Full name now CONFIRMED in source text (was "
            "previously inferred)."
        )
        e["pir07_role"] = (
            "Stated BN-Perikatan have an 'understanding' for NS polls, NOT a merger "
            "(The Star); framed as determinant for Melaka & PRU16. Reconfirmed this "
            "cycle (mkini 780035) with full name confirmed."
        )
        e["sources"] = [
            "The Star",
            "Malaysiakini (priority_pir-09_wee-bnpn-not-merger-mkini_20260718_231029)"
        ]
        e.pop("inference_note", None)
        e["name_confirmation_note"] = (
            "Full name 'Wee Ka Siong' now explicitly stated in mkini 780035 "
            "(231029 cycle) — prior build carried this as an inference; inference "
            "caveat removed."
        )
        break

# 2c. Update Tamim Dahri -> full name + age + surrender detail
for e in nfa:
    if e.get("name") == "Tamim Dahri":
        e["name"] = "Tamim Dahri Abd Razak"
        e["aliases"] = ["Tamim", "Tamim Dahri"]
        e["role"] = "Activist (surrendered to police); self-proclaimed land activist; age 33"
        e["pir09_role"] = (
            "Self-proclaimed land activist Tamim Dahri Abd Razak (33), on the run "
            "from court charges linked to religious provocation, surrendered to "
            "police at the Port Dickson district police HQ at ~12:45pm on "
            "Nomination Day (NST quoted NS police chief Datuk Alzafny Ahmad). To be "
            "brought to Seremban court for a remand application. Has publicly stated "
            "he hopes to campaign for an Negeri Sembilan independent candidate "
            "(which independent not specified in captured text). Independent-"
            "candidate support-network signal."
        )
        e["sources"] = [
            "Malaysiakini (priority_pir-09_tamim-independent-mkini_20260718_231029)",
            "Malaysiakini (mkini homepage + mkini gnews, 170837/182751 cycles)",
            "New Straits Times (quoted via mkini)"
        ]
        break

# update total_unique_persons counter (+1 for Alzafny Ahmad; renames of
# Wee/Tamim are modifications, not additions)
def bump_count(d, key, delta):
    if isinstance(d, dict):
        for k, v in d.items():
            if k == key and isinstance(v, int):
                d[k] = v + delta
                return True
            if isinstance(v, (dict, list)):
                if bump_count(v, key, delta):
                    return True
    elif isinstance(d, list):
        for it in d:
            if bump_count(it, key, delta):
                return True
    return False

# national_figures_and_pir_actors is a list; total_unique_persons is a sibling? No —
# it lives at data["national_figures_and_pir_actors"] as a LIST, and
bump_count(data, "total_unique_persons", 1)  # +1 for Alzafny Ahmad (in data["politicians"])

# ===========================================================================
# 3. SEATS — add hot-seat matchup detail + role affiliations + PIR-07 tags
# ===========================================================================
seats = data["seats"]

# helper to find a seat by code
def find_seat(code):
    for s in seats:
        if s["code"] == code:
            return s
    return None

# 3a. N32 Linggi — hot seat #1
s = find_seat("N32")
if s:
    s["pir07_hot_seat"] = {
        "rank": 1,
        "designation": "Kerusi panas (hot seat) #1 — Utusan 5-hot-seats (06:40 MYT 19 Jul)",
        "character": "MB Aminuddin's marquee seat-move (Sikamat -> Linggi); BN fortress; 3-cornered",
        "matchup": {
            "ph": "Datuk Seri Aminuddin Harun — Pengerusi PH NS / Menteri Besar / Ahli Parlimen Port Dickson (moved from Sikamat after 4 terms)",
            "bn": "Datuk Mohd Faizal Ramli — BN incumbent (2023 winner); BN fortress seat",
            "bersatu": "Datuk Zamri Md. Yunus — Bersatu (aliases: 'Datuk Zamri Md Said' [mStar spelling]; Utusan spells 'Md. Yunus')"
        },
        "result_2023": "Mohd Faizal (BN) beat Zamri (then PN) by 1,461 majority",
        "note": "Aminuddin taking a 'big risk' entering a long-time BN stronghold though he is PD MP."
    }

# 3b. N13 Sikamat — hot seat #2
s = find_seat("N13")
if s:
    s["pir07_hot_seat"] = {
        "rank": 2,
        "designation": "Kerusi panas (hot seat) #2 — Utusan 5-hot-seats",
        "character": "Aminuddin's old seat (held since 2008); now defended by his political secretary; 3-cornered; PIR-06 Tier-4 (Bersatu vs Wawasan)",
        "matchup": {
            "ph": "Nor Azman Mohamad — Setiausaha Politik kepada MB Aminuddin (defending Aminuddin's former seat)",
            "bersatu": "Datuk Tun Faisal Ismail Aziz — Ketua Penerangan Bersatu (Bersatu Information Chief)",
            "pn": "Datuk Razali Abu Samah — PN (Wawasan)"
        }
    }

# 3c. N14 Ampangan — hot seat #3
s = find_seat("N14")
if s:
    s["pir07_hot_seat"] = {
        "rank": 3,
        "designation": "Kerusi panas (hot seat) #3 — Utusan 5-hot-seats",
        "character": "Thinnest 2023 margin (329); 3-cornered; PIR-06 Tier-4 (Bersatu vs PAS); PIR-09 Day-1 messaging war",
        "matchup": {
            "ph": "Datuk (Muhammad) Nazri Kassim — Timbalan Pengerusi Majlis Pimpinan Negeri Keadilan NS (new candidate; aliases: 'Datuk Nazri Kassim')",
            "pn": "Datuk Dr. Mohamad Rafie Ab. Malek — PN-PAS, bekas ADUN Ampangan (former ADUN; 2018 PH winner, defector/hopper angle)",
            "bersatu": "Noor'azah Harun — Bersatu"
        },
        "result_2023_margin": "329 votes (Tengku Zamrah PH-PKR won 2023)",
        "note": "PH working hard to retain; new candidate vs former ADUN (PN) vs Bersatu."
    }

# 3d. N25 Paroi — hot seat #4  (ADD PIR-07 tag via Utusan designation)
s = find_seat("N25")
if s:
    if "PIR-07" not in s["pir_tags"]:
        s["pir_tags"].append("PIR-07")
    s["pir07_hot_seat"] = {
        "rank": 4,
        "designation": "Kerusi panas (hot seat) #4 — Utusan 5-hot-seats (PIR-07 tag ADDED this cycle via designation)",
        "character": "Largest electorate in NS; 3-cornered; PIR-06 Tier-4 (Bersatu vs PAS incumbent)",
        "matchup": {
            "pn": "Kamarol Ridzuan Mohd Zin — PN-PAS incumbent (largest-electorate seat; aliases: 'Kamarol Ridzuan Mohd Zain')",
            "ph": "Ahmad Shahir Mohd. Shah — Setiausaha Akhbar kepada MB NS / Setiausaha Pemuda Amanah Nasional",
            "bersatu": "Mohd. Nazree Mohd. Yunus — Ketua Penerangan Bersatu NS (aliases: 'Mohd Nazree Mohd Yunos')"
        }
    }

# 3e. N20 Labu — hot seat #5  (ADD PIR-07 tag via Utusan designation)
s = find_seat("N20")
if s:
    if "PIR-07" not in s["pir_tags"]:
        s["pir_tags"].append("PIR-07")
    s["pir07_hot_seat"] = {
        "rank": 5,
        "designation": "Kerusi panas (hot seat) #5 — Utusan 5-hot-seats (PIR-07 tag ADDED this cycle via designation)",
        "character": "Bersatu incumbent defending; 3-cornered; PIR-06 Tier-4-adjacent (Bersatu incumbent vs PH vs BN)",
        "matchup": {
            "bersatu": "Mohamad Hanifah Abu Baker — Bersatu incumbent / Ketua Badan Pimpinan Bersatu NS",
            "ph": "Datuk Ahmad Faez Abdul Razak — Penyelaras DUN Labu (PH-PKR)",
            "bn": "Siti Umaira Hasim — BN (aliases: 'Siti Nur Umaira Hasim')"
        }
    }

# ===========================================================================
# 4. constituencies list — mirror PIR-07 tag additions for N20/N25
# ===========================================================================
for c in data["constituencies"]:
    if c["code"] in ("N20", "N25"):
        if "PIR-07" not in c["pir_tags"]:
            c["pir_tags"].append("PIR-07")

# ===========================================================================
# 5. organizations — add PP-KPR
# ===========================================================================
orgs = data["organizations"]
if not any("PP-KPR" in o for o in orgs):
    # insert after PDRM
    for i, o in enumerate(orgs):
        if "PDRM" in o:
            orgs.insert(i + 1, "Pasukan Penguat Kuasa Kempen Pilihan Raya (PP-KPR) — SPR campaign-enforcement teams (36 stood up for PRN NS)")
            break

# ===========================================================================
# 6. events — add new events
# ===========================================================================
new_events = [
    "Sidang Akhbar SPR (Pengerusa SPR Datuk Seri Ramlan Harun) — pengesahan 103 calon / 36 kerusi / struktur pertandingan 11-21-2-2 / 94L-9P / termuda 23-tertua 70 / kempen hingga 11.59pm 31 Jul [PIR-07]",
    "Sidang Akhbar Polis (Ketua Polis NS Datuk Alzafny Ahmad) di Kompleks Pentadbiran Daerah Port Dickson — 2,373 PDRM, 8 pusat penamaan lancar tanpa insiden, tiada laporan polis [PIR-07]",
    "Majlis makan malam penggalang dana DAP (Bandar Utama 11 community hall, malam sebelum kempen) — DAP hidupkan semula kempen anti-BN (1MDB, krisis ruler) [PIR-07]",
    "Kehadiran penuh pemimpin/penyokong gabungan Hari Penamaan Calon — Aminuddin tiba di Auditorium Kompleks Pentadbiran Daerah Port Dickson ~8:30pag (Bernama) [PIR-07]",
    "Penyerahan Tamim Dahri Abd Razak (33) di IPD Port Dickson ~12:45tgh -> bawa ke mahkamah Seremban untuk permohonan reman [PIR-09]",
    "Sidang akhbar Wee Ka Siong (presiden MCA) — pact BN-PN bukan penggabungan, setiap parti kekal ideologi [PIR-09, PIR-07]",
    "KiniGuide Malaysiakini 'Shifting alliances as battle royale for Negeri Sembilan begins' — BN masuk selepas kemenangan besar Johor; lanskap politik berubah [PIR-07]"
]
data["events"] = data["events"] + new_events

# ===========================================================================
# 7. issues_and_signals — add new signals
# ===========================================================================
new_issues = [
    {"issue": "Bersatu bertanding 24 kerusi bawah NAMA & LAMBANG sendiri KALI PERTAMA dalam pilihan raya — isyarat schism empirik peringkat undi (masih komponen PN)", "pir_tags": ["PIR-06", "PIR-07"]},
    {"issue": "Bersatu bertembung de­ngan calon PN di 7 kawasan DUN — schism empirik peringkat undi (Sikamat N13, Ampangan N14, Paroi N25, Labu N20 + 3 lagi pending senarai penuh)", "pir_tags": ["PIR-06", "PIR-07"]},
    {"issue": "5 kerusi panas diwartakan Utusan (Linggi N32, Sikamat N13, Ampangan N14, Paroi N25, Labu N20) dengan padanan calon penuh + afiliasi peranan", "pir_tags": ["PIR-07"]},
    {"issue": "NST analysis 'Bersatu at a crossroads amid BN-PN cooperation' — PIR-06 corroborative (BUKAN notis MT; teks penuh tertangguh gnews-encrypted)", "pir_tags": ["PIR-06"]},
    {"issue": "Konfigurasi calon: 94 lelaki / 9 wanita; calon termuda 23 (M. Leevineshwaraan, Bersatu N33), tertua 70 (Abd. Latif A. Tambi, PH N35)", "pir_tags": ["PIR-07", "PIR-09"]},
    {"issue": "Tempoh kempen sehingga 11.59 malam 31 Julai 2026; SPR tubuhkan 36 PP-KPR untuk pantau kempen; amaran jauhi hasutan/perkauman/agama (3R)", "pir_tags": ["PIR-07"]},
    {"issue": "Tiada kertas penamaan calon ditolak; 8 pusat penamaan lancar tanpa insiden; 2,373 PDRM digerakkan; penyokong 1,000-2,500 pusat (Jempol paling ramai, Kuala Pilah paling sedikit)", "pir_tags": ["PIR-07"]},
    {"issue": "MCA president Wee Ka Siong (nama penuh disahkan) — pact BN-PN bukan penggabungan; setiap parti kekal ideologi/pendirian (mkini 780035)", "pir_tags": ["PIR-09", "PIR-07"]}
]
data["issues_and_signals"] = data["issues_and_signals"] + new_issues

# ===========================================================================
# 8. locations — add new venues
# ===========================================================================
ncav = data["locations"]["nomination_centres_and_venues"]
new_venues = [
    "Auditorium Kompleks Pentadbiran Daerah Port Dickson — nomination centre (Aminuddin arrival ~8:30am, Bernama) [PIR-07]",
    "Kompleks Pentadbiran Daerah Port Dickson — venue for NS Police Chief (Alzafny Ahmad) nomination-day press conference [PIR-07]",
    "Bandar Utama 11 community hall (Petaling Jaya) — DAP fundraising dinner venue, eve of campaign (anti-BN messaging) [PIR-07] — peripheral_non_prn"
]
for v in new_venues:
    if v not in ncav:
        ncav.append(v)
# IPD Port Dickson district police HQ (Tamim surrender) — peripheral? it's PRN-adjacent (Port Dickson), add to nomination_centres_and_venues
ipd_pd = "IPD Port Dickson (district police HQ) — Tamim Dahri Abd Razak surrender ~12:45pm (Nomination Day) [PIR-09]"
if ipd_pd not in ncav:
    ncav.append(ipd_pd)

# ===========================================================================
# 9. pir_priority_index — PIR-06 / PIR-09 / PIR-07 enrichment
# ===========================================================================
ppi = data["pir_priority_index"]

# --- PIR-06 ---
pir06 = ppi["PIR-06"]
pir06["status"] = (
    "ESCALATED WATCH — UNCHANGED this cycle. NO formal PN-MT removal notice; "
    "TWO-SIDED trajectory ACTIVE (PN-MT-may-remove-Bersatu via Kiandee AND "
    "Bersatu-may-exit-PN via Muhyiddin). 231029 cycle added CORROBORATIVE PIR-06 "
    "content only: (a) NST 'Bersatu at a crossroads amid BN-PN cooperation' "
    "(headline, full text deferred); (b) Utusan empirically confirms Bersatu "
    "contests 24 DUN seats under OWN logo (first time) and CLASHES WITH PN "
    "CANDIDATES IN 7 SEATS — tangible ballot-level schism, NOT a formal MT "
    "removal notice. Trajectory unchanged: Bersatu voluntary realignment/exit "
    "AFTER Aug 1 poll most likely; reactive PN-MT removal remains possible if "
    "Bersatu candidates damage PN partners in Tier-4 seats."
)
pir06["nst_crossroads_corroboration"] = {
    "headline": "Negri Sembilan polls: Bersatu at a crossroads amid BN-PN cooperation",
    "source": "New Straits Times",
    "pubdate_gmt": "Sat, 18 Jul 2026 23:00:40 GMT (07:00 MYT 19 Jul)",
    "url": "gnews-encrypted; direct URL not recovered",
    "first_captured_cycle": "231029",
    "significance": "NST analysis piece corroborating the Muhyiddin exit-positioning thesis. NOT a formal MT removal notice. Full text deferred (gnews encrypted / NST JS-rendered).",
    "file": "priority_pir-06_bersatu-crossroads-nst_20260718_231029.md"
}
pir06["bersatu_own_logo_empirical_schism"] = {
    "fact": "Bersatu contests 24 DUN seats under its OWN name/logo (first time) and clashes with PN candidates in 7 seats",
    "source": "Utusan (priority_pir-07_3-coalitions-clash-utusan_20260718_231029, full text)",
    "first_captured_cycle": "231029",
    "significance": "Strongest on-the-ground evidence to date of the PN-Bersatu fracture — a PN component running against its own coalition under a separate logo. NOT a formal MT removal notice.",
    "clash_seats_named": ["N13 Sikamat", "N14 Ampangan", "N25 Paroi", "N20 Labu", "(3 further pending full cross-check)"],
    "clash_seats_confirmed_count": 7
}
# add Alzafny is not a PIR-06 actor; leave watch_figures unchanged.

# --- PIR-09 ---
pir09 = ppi["PIR-09"]
# add Wee Ka Siong full-name confirmation + Tamim detail
pir09["wee_ka_siong_clarification"] = {
    "actor": "Datuk Dr Wee Ka Siong (MCA president — full name CONFIRMED this cycle)",
    "statement": "BN-PN electoral pact in NS is NOT a merger; each party retains its own ideology and stance; aimed at strong/stable state government for continued development.",
    "source": "Malaysiakini (priority_pir-09_wee-bnpn-not-merger-mkini_20260718_231029, intro)",
    "first_captured_cycle": "231029",
    "type": "Component-party messaging (BN side) — follows backlash over BN-PN cooperation"
}
# update tamim_independent_support with full name/age
if "tamim_independent_support" in pir09:
    pir09["tamim_independent_support"] = {
        "actor": "Tamim Dahri Abd Razak (activist, 33, self-proclaimed land activist)",
        "context": "Surrendered at Port Dickson district police HQ ~12:45pm (Nomination Day); to be brought to Seremban court for remand (religious-provocation charges); intends to campaign for an NS independent candidate (which one not specified).",
        "police_source": "NST quoted NS police chief Datuk Alzafny Ahmad",
        "type": "Independent-candidate support-network signal",
        "first_captured_cycle": "170837",
        "enriched_cycle": "231029 (full name + age + surrender timing + remand)"
    }
# add full name to entities list
if "Datuk Dr Wee Ka Siong" not in pir09["entities"] and "Dr Wee" in pir09["entities"]:
    pir09["entities"] = ["Datuk Dr Wee Ka Siong" if x == "Dr Wee" else x for x in pir09["entities"]]
if "Tamim Dahri" in pir09["entities"]:
    pir09["entities"] = ["Tamim Dahri Abd Razak" if x == "Tamim Dahri" else x for x in pir09["entities"]]
# Tamim already not in PIR-09 entities list (it's in the list actually); ensure
# Alzafny is NOT a PIR-09 entity (he's official). Leave.

# --- PIR-07 ---
pir07 = ppi["PIR-07"]
pir07["journalist_designated_hot_seats"] = {
    "source": "Utusan 'Lima kerusi panas jadi tumpuan' (priority_pir-07_5-hot-seats-utusan_20260718_231029, full text, 06:40 MYT 19 Jul)",
    "seats": [
        {"code": "N32", "name": "Linggi", "rank": 1, "matchup": "Aminuddin (PH/MB) vs Datuk Mohd Faizal Ramli (BN inc) vs Datuk Zamri Md Yunus (Bersatu); 2023 Faizal beat Zamri-PN by 1,461"},
        {"code": "N13", "name": "Sikamat", "rank": 2, "matchup": "Nor Azman (PH, Aminuddin's pol-sec) vs Datuk Tun Faisal (Bersatu, info chief) vs Datuk Razali (PN-Wawasan); Aminuddin's old seat 2008-"},
        {"code": "N14", "name": "Ampangan", "rank": 3, "matchup": "Datuk Nazri Kassim (PH new) vs Datuk Dr Mohamad Rafie (PN, ex-ADUN) vs Noor'azah (Bersatu); 2023 margin 329"},
        {"code": "N25", "name": "Paroi", "rank": 4, "matchup": "Kamarol Ridzuan (PN-PAS inc, largest electorate) vs Ahmad Shahir (PH, MB press-sec/Amanah Youth sec) vs Mohd Nazree (Bersatu, NS info chief)"},
        {"code": "N20", "name": "Labu", "rank": 5, "matchup": "Mohamad Hanifah (Bersatu inc, NS chief) vs Datuk Ahmad Faez (PH, Labu coord) vs Siti Umaira (BN)"}
    ],
    "note": "Utusan journalist designation; overlaps director-approved PIR-07 watch seats at N13/N14/N32; N25 Paroi & N20 Labu ADDED as PIR-07-relevant this cycle via this designation (both already PIR-06 Tier-4 / PIR-09 Bersatu seats)."
}
pir07["bersatu_vs_pn_clash_seats"] = {
    "confirmed_count": 7,
    "named": ["N13 Sikamat", "N14 Ampangan", "N25 Paroi", "N20 Labu"],
    "pending_full_cross_check": 3,
    "source": "Utusan (priority_pir-07_3-coalitions-clash-utusan_20260718_231029, full text)",
    "significance": "Empirical ballot-level schism: a PN component (Bersatu) running against its own coalition (PN) under a separate logo — strongest on-the-ground PN-Bersatu fracture evidence (PIR-06 + PIR-07)."
}
pir07["operational_detail_231029"] = {
    "gender_split": "94 men / 9 women",
    "youngest": "M. Leevineshwaraan (Bersatu, N33), 23",
    "oldest": "Abd. Latif A. Tambi (PH, N35 Gemencheh), 70",
    "campaign_window": "until 11:59pm 31 July 2026",
    "pp_kpr_teams": 36,
    "nomination_centres": 8,
    "papers_rejected": 0,
    "pdrm_deployed": 2373,
    "supporters_per_centre": "1,000-2,500 (Jempol most, Kuala Pilah least)",
    "incidents": "none / no police reports",
    "source": "Utusan 3-coalitions (Ramlan Harun SPR + Alzafny Ahmad PDRM press conferences)"
}
# candidate-count corroboration: upgrade to Utusan full-text Malay confirmation
pir07["candidate_count_corroboration"] = {
    "fact": "103 candidates for 36-seat PRN NS ke-16",
    "malay_full_text_source": "Utusan 'Tiga gabungan bertembung' (priority_pir-07_3-coalitions-clash-utusan_20260718_231029, full text, SPR Ramlan Harun press conference)",
    "english_source": "New Straits Times (nstcommy gnews, 194028/205755 cycles)",
    "prior_malay_source": "Kosmo '103 calon sah bertanding rebut 36 kerusi DUN – SPR'",
    "status": "Reconfirmation of the already-counted figure; Utusan full-text now the primary Malay source. No new entity."
}
# add Alzafny to PIR-07 entities
if "Datuk Alzafny Ahmad" not in pir07["entities"]:
    pir07["entities"].append("Datuk Alzafny Ahmad")
# confirm Wee full name in PIR-07 entities
pir07["entities"] = ["Datuk Dr Wee Ka Siong" if x == "Dr Wee" else x for x in pir07["entities"]]

# ===========================================================================
# 10. counts
# ===========================================================================
counts = data["counts"]
counts["national_figures_and_pir_actors"] = counts.get("national_figures_and_pir_actors", 17) + 1  # +Alzafny
counts["organizations"] = counts.get("organizations", 10) + 1  # +PP-KPR
counts["events"] = counts.get("events", 23) + len(new_events)
counts["issues_and_signals"] = counts.get("issues_and_signals", 29) + len(new_issues)
counts["locations"] = counts.get("locations", 49) + 4  # +4 new venues (incl IPD PD)
# PIR-07 watch seats unchanged (director list preserved); but seats with PIR-07 tag grew by 2 (N20,N25)
counts["pir07_battleground_seats_tagged"] = counts.get("pir07_watch_seats", 9) + 2  # N20 Labu, N25 Paroi added
counts["confirmation_passes_since_170837"] = 0  # reset: 231029 is first NEW-content cycle
counts["genuinely_new_entities_this_build"] = 1  # Alzafny Ahmad
counts["enriched_existing_entities_this_build"] = 4  # Wee, Tamim, +2 seats PIR-07 tag
counts["new_named_figures"] = ["Datuk Alzafny Ahmad"]
counts["confirmed_full_names"] = ["Wee Ka Siong (MCA president)", "Tamim Dahri Abd Razak (activist)"]

# ===========================================================================
# 11. delta_vs_prior_build_211155
# ===========================================================================
data["delta_vs_prior_build_211155"] = {
    "prior_build": "entities_211155.json (21:11 UTC / 05:11 MYT 19 Jul)",
    "this_build": "entities_233104.json (23:31 UTC / 07:31 MYT 19 Jul)",
    "cycle_window_ingested": [
        "231029 (23:10 UTC / 07:10 MYT 19 Jul — 5th overnight/dawn pass; FIRST genuinely-new-content cycle after 4 consecutive zero-delta passes)"
    ],
    "delta_verification_method": (
        "collection_metadata.json (231029 cycle) documents: 2 genuinely brand-new Utusan "
        "PIR-07 articles at 06:40 & 06:45 MYT 19 Jul (22:40 & 22:45 UTC 18 Jul) with "
        "Elementor full-text extraction; plus freshly-captured PIR-09 component-party "
        "items (Wee, Tamim) and PIR-07 mkini intros (DAP anti-BN, nominations full-force, "
        "KiniGuide). PIR-06 substance already fully captured at 170837; NST 'Bersatu at a "
        "crossroads' headline captured this cycle (full text deferred, gnews encrypted). "
        "This agent read all 10 priority_*.md files from the 231029 cycle and reconciled "
        "against the entities_211155 baseline."
    ),
    "genuinely_new_findings": [
        "NEW NAMED FIGURE: Datuk Alzafny Ahmad — Ketua Polis Negeri Sembilan (NS Police Chief). Quoted in Utusan 3-coalitions (nomination security press conference, 2,373 PDRM) AND mkini Tamim article (Tamim surrender ~12:45pm PD IPD). PIR-07 + PIR-09.",
        "FORMAL '5 HOT SEATS' BATTLEGROUN DESIGNATION (Utusan full-text): Linggi N32, Sikamat N13, Ampangan N14, Paroi N25, Labu N20 — each with FULL candidate matchups + role affiliations (e.g. Aminuddin = MB/PD MP; Tun Faisal = Bersatu info chief; Nazri Kassim = PKR NS dep chief; Rafie = ex-ADUN; Hanifah = Bersatu NS chief). PIR-07 substantially enriched.",
        "7 BERSATU-vs-PN CLASH SEATS CONFIRMED (Utusan full-text): Bersatu contests 24 seats under OWN logo (first time) and clashes with PN candidates in 7 seats — empirical ballot-level schism (PIR-06 + PIR-07). 4 named (Sikamat, Ampangan, Paroi, Labu); 3 pending full cross-check.",
        "FULL NAME CONFIRMATION: 'Dr Wee' -> 'Datuk Dr Wee Ka Siong' (MCA president) explicitly named in mkini 780035 (prior build carried full name as inference; inference caveat removed).",
        "FULL NAME + DETAIL: 'Tamim Dahri' -> 'Tamim Dahri Abd Razak', age 33, self-proclaimed land activist; surrendered at PD IPD ~12:45pm -> Seremban court remand (religious-provocation charges).",
        "OPERATIONAL DETAIL (PIR-07): 94M/9W; youngest 23 (Leevineshwaraan Bersatu), oldest 70 (Abd Latif PH); campaign to 11:59pm 31 Jul; 36 PP-KPR teams; 8 centres; 0 papers rejected; 2,373 PDRM; supporters 1,000-2,500/centre (Jempol most, Kuala Pilah least); no incidents.",
        "PIR-06 CORROBORATION: NST 'Bersatu at a crossroads amid BN-PN cooperation' (pubDate 07:00 MYT 19 Jul) — analysis piece, NOT a removal notice; full text deferred (gnews encrypted).",
        "NEW EVENTS: SPR Ramlan press conference; Alzafny police press conference; DAP Bandar Utama 11 fundraising dinner; Aminuddin PD nomination ~8:30am; Tamim surrender; Wee press conference; KiniGuide.",
        "NEW ORGANIZATION: PP-KPR (Pasukan Penguat Kuasa Kempen Pilihan Raya) — 36 SPR campaign-enforcement teams.",
        "NEW LOCATIONS: Auditorium Kompleks Pentadbiran Daerah Port Dickson; Kompleks Pentadbiran Daerah Port Dickson; Bandar Utama 11 community hall (PJ); IPD Port Dickson (Tamim surrender).",
        "PIR-07 TAG ADDED to N20 Labu & N25 Paroi (via Utusan 5-hot-seats designation) — director-approved watch_seats list (9) preserved unchanged; these 2 are journalist-designated battlegrounds overlapping PIR-06 Tier-4."
    ],
    "corroborating_reconfirmations": [
        "103 candidates / 36 seats / breakdown {PH:36, BN:25, Bersatu:24, PN:11, ind:4, Berjasa:1, Asli:1, PSM:1} — reconfirmed via Utusan full-text (Ramlan Harun SPR press conference).",
        "Seat structure 11 two-cornered / 21 three-cornered / 2 four-cornered / 2 five-cornered — reconfirmed.",
        "N32 Linggi: Aminuddin (PH/MB) vs Faizal (BN) vs Zamri (Bersatu); 2023 Faizal beat Zamri-PN by 1,461 — reconfirmed by both Utusan 5-hot-seats and mStar aminuddin-linggi full-text.",
        "Aminuddin held Sikamat 4 terms (since 2008), moved to Linggi — reconfirmed.",
        "BN manifesto launch 24 Jul — reconfirmed (carryover).",
        "DAP revives anti-BN campaign (1MDB, ruler crisis) — reconfirmed (mkini intro)."
    ],
    "no_change": [
        "CRITICAL PIR-06 threshold (formal PN-MT removal notice) STILL NOT crossed.",
        "Candidate roster UNCHANGED: 103 candidates, 36 seats — NO new candidates discovered (Alzafny/Abd-Latif-age are details on already-listed figures; Abd Latif A Tambi already in N35 Gemencheh).",
        "No Bersatu candidate withdrawals in the 8 Tier-4 seats (N04,N05,N13,N14,N23,N25,N31,N34).",
        "Gerakan pecat of Tang Jay Son reconfirmed (no new PN-component candidate expulsion).",
        "PIR-09 N.14 Ampangan Day-1 messaging war core unchanged (Day-2 dawn, no new Day-2 campaign content yet).",
        "PIR-06 escalated-watch two-sided trajectory (PN-MT-may-remove-Bersatu AND Bersatu-may-exit-PN) UNCHANGED.",
        "PIR-07 director-approved watch_seats (9: N04,N05,N10,N13,N14,N15,N28,N32,N33) UNCHANGED.",
        "All PIR-06 monitor channels (Kiandee/Muhyiddin/Annuar Musa/Hadi/Samsuri/Hamzah) — no new output this cycle."
    ],
    "entity_set_delta": {
        "added": 1,
        "removed": 0,
        "modified": 7,
        "net": 1,
        "added_entities": ["Datuk Alzafny Ahmad (NS Police Chief)"],
        "modified_entities": [
            "Dr Wee -> Datuk Dr Wee Ka Siong (full name confirmed)",
            "Tamim Dahri -> Tamim Dahri Abd Razak (full name + age 33 + surrender detail)",
            "N20 Labu (+PIR-07 tag + hot-seat detail)",
            "N25 Paroi (+PIR-07 tag + hot-seat detail)",
            "N32 Linggi (+hot-seat matchup detail)",
            "N13 Sikamat (+hot-seat matchup detail)",
            "N14 Ampangan (+hot-seat matchup detail)"
        ]
    }
}

# ===========================================================================
# 12. write entities file
# ===========================================================================
with open(THIS_FILE, "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

# ===========================================================================
# 13. update entity_metadata.json
# ===========================================================================
with open(META_FILE, "r", encoding="utf-8") as f:
    meta = json.load(f)

# recompute total_entities by counting seat candidates + figures + parties + etc.
# (kept consistent with prior methodology: sum of count categories)
meta["last_updated_utc"] = "2026-07-18T23:31:04+00:00"
meta["last_updated_myt"] = "2026-07-19T07:31:04+08:00"
meta["latest_entities_file"] = "entities_233104.json"
meta["prior_entities_file"] = "entities_211155.json"
meta["cycle"] = (
    "nomination-day-surge + Day-2 dawn enrichment (231029: FIRST new-content cycle after "
    "4 zero-delta passes; 2 brand-new Utusan PIR-07 articles + PIR-09 component items)"
)
meta["build_character"] = (
    "ENRICHMENT / CORROBORATION BUILD — 1 new named figure (Alzafny, NS police chief); "
    "Wee Ka Siong + Tamim full names confirmed; 5 hot seats formally designated (full "
    "matchups); 7 Bersatu-vs-PN clash seats confirmed; PIR-06/07/09 enriched; "
    "103-candidate roster UNCHANGED; CRITICAL PIR-06 threshold still NOT crossed."
)

# delta_vs_prior_build
meta["delta_vs_prior_build"] = {
    "prior_build": "entities_211155.json",
    "this_build": "entities_233104.json",
    "cycles_ingested": ["231029"],
    "genuinely_new_entities": 1,
    "enriched_existing_entities": 7,
    "corroborating_reconfirmations": 6,
    "verification": "collection_metadata.json (231029) + this agent's reconciliation of 10 priority_*.md files vs entities_211155 baseline."
}

# counts
meta["counts"] = counts

# pir_priority_tags — update key entity lists
m_pir = meta["pir_priority_tags"]
# PIR-06: add NST crossroads + 7 clash seats note; keep key_entities
m_pir["PIR-06"]["status"] = pir06["status"]
m_pir["PIR-06"]["formal_removal_notice_detected"] = False
m_pir["PIR-06"]["escalation_detected"] = True
m_pir["PIR-06"]["this_cycle_new_pir06_content"] = True
m_pir["PIR-06"]["new_this_cycle"] = [
    "NST 'Bersatu at a crossroads amid BN-PN cooperation' (headline, full text deferred) — corroborative, NOT a removal notice",
    "Utusan empirically confirms Bersatu 24 own-logo seats + 7 Bersatu-vs-PN clash seats — ballot-level schism, NOT a removal notice"
]
# PIR-09
m_pir["PIR-09"]["new_this_cycle"] = [
    "Wee Ka Siong full name confirmed (MCA president) — BN-PN pact not a merger (mkini 780035)",
    "Tamim Dahri Abd Razak full name + age 33 + surrender detail (mkini 780055)"
]
m_pir["PIR-09"]["key_entities"] = list(dict.fromkeys(
    m_pir["PIR-09"]["key_entities"]
    + ["Datuk Alzafny Ahmad (context: Tamim surrender)", "Datuk Dr Wee Ka Siong", "Tamim Dahri Abd Razak"]
))
# replace old short names in key_entities
m_pir["PIR-09"]["key_entities"] = [
    "Datuk Dr Wee Ka Siong" if x == "Dr Wee" else
    ("Tamim Dahri Abd Razak" if x == "Tamim Dahri" else x)
    for x in m_pir["PIR-09"]["key_entities"]
]
# PIR-07
m_pir["PIR-07"]["key_entities"] = list(dict.fromkeys(
    [ ("Datuk Dr Wee Ka Siong" if x == "Dr Wee" else x) for x in m_pir["PIR-07"]["key_entities"] ]
    + ["Datuk Alzafny Ahmad"]
))
m_pir["PIR-07"]["new_this_cycle"] = [
    "5 hot seats formally designated (Linggi N32, Sikamat N13, Ampangan N14, Paroi N25, Labu N20) with full candidate matchups + role affiliations (Utusan full-text)",
    "7 Bersatu-vs-PN clash seats confirmed (4 named: Sikamat, Ampangan, Paroi, Labu; 3 pending)",
    "Operational detail: 94M/9W; youngest 23 (Leevineshwaraan), oldest 70 (Abd Latif); campaign to 11:59pm 31 Jul; 36 PP-KPR; 8 centres; 0 papers rejected; 2,373 PDRM",
    "PIR-07 tag added to N20 Labu & N25 Paroi (Utusan hot-seat designation; director watch list unchanged)"
]

# seat_pir_tag_map — mirror PIR-07 additions for N20/N25
for sm in meta["seat_pir_tag_map"]:
    if sm["code"] in ("N20", "N25"):
        if "PIR-07" not in sm["pir_tags"]:
            sm["pir_tags"].append("PIR-07")

# files_in_folder — prepend this run
files_note = (
    "entities_233104.json (THIS run — Day-2 dawn ENRICHMENT build; 231029 cycle: 1 new "
    "figure Alzafny + Wee/Tamim full names + 5 hot seats + 7 clash seats + operational "
    "detail; 103-candidate roster unchanged; PIR-06 threshold still NOT crossed)"
)
meta.setdefault("files_in_folder", [])
meta["files_in_folder"] = [files_note] + meta["files_in_folder"]

# total_entities: recompute as before (sum of count categories minus overlaps is hard;
# keep prior total + added). Prior was 291. +1 figure +1 org +7 events +8 issues +4 locs
# = +21, but some are signals not distinct entities. Use a principled bump: +1 figure,
# +1 org, +4 locations = +6 distinct entities; events/issues are signals. We add +6.
meta["total_entities"] = meta.get("total_entities", 291) + 6

with open(META_FILE, "w", encoding="utf-8") as f:
    json.dump(meta, f, ensure_ascii=False, indent=2)

# ===========================================================================
# 14. validate JSON round-trips
# ===========================================================================
with open(THIS_FILE, "r", encoding="utf-8") as f:
    json.load(f)
with open(META_FILE, "r", encoding="utf-8") as f:
    json.load(f)

print("OK: entities_233104.json + entity_metadata.json written and validated.")
print(f"entities file: {THIS_FILE}")
print(f"metadata file: {META_FILE}")
print(f"total_unique_persons: {data.get('total_unique_persons')}")
print(f"seats with PIR-07 tag: {sum(1 for s in data['seats'] if 'PIR-07' in s.get('pir_tags', []))}")
print(f"organizations: {len(data['organizations'])}")
print(f"events: {len(data['events'])}")
print(f"issues_and_signals: {len(data['issues_and_signals'])}")
print(f"nomination_centres_and_venues: {len(data['locations']['nomination_centres_and_venues'])}")
