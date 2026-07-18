#!/usr/bin/env python3
"""
PRN Negeri Sembilan 2026 — Entity Extraction Agent (cron build script)
Builds entities_165723.json + entity_metadata.json from raw-scrapes/20260718.
Inherits the clean 36-seat candidate structure from the prior consolidated extraction,
then layers in national figures / PIR actors / signals captured from the 15:31+ surge
news cycle (NST, Utusan, BHarian, AstroAwani, The Star, priority PIR files).
Classification: TLP:AMBER
"""
import json, os, re, datetime

BASE = "/home/p62operator/.openclaw/workspace-ns/04-DATA-AND-SOURCES/processed-entities/20260718"
CONS = os.path.join(BASE, "entities_consolidated.json")

with open(CONS, "r", encoding="utf-8") as f:
    cons = json.load(f)

seats = cons["seats"]  # 36 seats, canonical candidate names

# ---- PIR seat sets (per mission + priority files) ----
PIR06_TIER4 = ["N04","N05","N13","N14","N23","N25","N31","N34"]   # Bersatu vs PN component (8)
PIR07_WATCH = ["N04","N05","N10","N13","N14","N15","N28","N32","N33"]  # battleground (9, incl N05 per mission)

# PIR-06 component-match detail per seat (from collection_metadata)
tier4_detail = {
 "N04": {"bersatu":"Muhammad Adib Musa","pn_component":"Danni Rais (Wawasan)","type":"vs Wawasan"},
 "N05": {"bersatu":"Muhammad Noraffendy Mohd Salleh","pn_component":"Mohd Fairuz Mohd Isa (PAS, 2023 incumbent)","type":"vs PAS"},
 "N13": {"bersatu":"Datuk Tun Faisal Ismail Aziz","pn_component":"Datuk Razali Abu Samah (Wawasan)","type":"vs Wawasan"},
 "N14": {"bersatu":"Noor'azah Harun","pn_component":"Datuk Dr Mohamad Rafie Ab Malek (PAS)","type":"vs PAS"},
 "N23": {"bersatu":"N Sarawanan","pn_component":"Erik Michael (Wawasan)","type":"vs Wawasan"},
 "N25": {"bersatu":"Mohd Nazree Mohd Yunos","pn_component":"Kamarol Ridzuan Mohd Zain (PAS, 2023 incumbent)","type":"vs PAS"},
 "N31": {"bersatu":"Sheikh Junaidy Jamaludin","pn_component":"Abdul Fatah Zakaria (PAS, 2023 incumbent)","type":"vs PAS"},
 "N34": {"bersatu":"Azman Abdullah","pn_component":"Ridzuan Ahmad (Wawasan, 2023 incumbent as Bersatu)","type":"vs Wawasan"},
}

# 24 BERSATU candidates (PIR-09 set)
BERSATU_CAND_SEATS = ["N02","N03","N04","N05","N06","N07","N09","N10","N12","N13","N14",
                      "N15","N16","N17","N20","N22","N23","N24","N25","N28","N31","N32","N33","N34"]

# Independents (PIR-09 set): name -> seat
INDEPENDENTS = {
 "Omar Mohd Isa":"N10 Nilai",
 "Teo Seng Lee":"N30 Lukut",
 "Datuk A Saravanan":"N33 Sri Tanjung",
 "Islah Wahyudi Zainudin":"N33 Sri Tanjung",
}

# ---- Annotate seats with PIR tags ----
def seat_tags(code):
    t = []
    if code in PIR06_TIER4: t.append("PIR-06")
    if code in PIR07_WATCH: t.append("PIR-07")
    # PIR-09 candidate-credibility seats
    if code in BERSATU_CAND_SEATS: t.append("PIR-09")
    if code in ["N10","N30","N33"]: t.append("PIR-09")  # independents
    if code == "N14": t.append("PIR-09")  # Rafie defector angle
    if code == "N22": t.append("PIR-09")  # Tang Jay Son expulsion
    # dedupe preserve order
    seen=set(); out=[]
    for x in t:
        if x not in seen: seen.add(x); out.append(x)
    return out

seat_records = []
for s in seats:
    code = s["code"]
    rec = {
        "code": code,
        "name": s["name"],
        "voters": s.get("voters",""),
        "candidate_count": s["candidate_count"],
        "candidates": s["candidates"],
        "winner_2023": s.get("winner_2023",""),
        "winner_2023_ticket": s.get("winner_2023_ticket",""),
        "pir_tags": seat_tags(code),
    }
    if code in tier4_detail:
        rec["pir06_tier4_detail"] = tier4_detail[code]
    if code == "N14":
        rec["pir09_note"] = "Day-1 messaging war: PH Nazri '50/50' vs PAS Rafie (former 2018 PH winner, defector angle) vs Bersatu Noor'azah (splits anti-PH vote)."
    if code == "N22":
        rec["pir09_note"] = "4-cornered: Tang Jay Son (Bersatu, ex-Gerakan expelled) vs Siau Meow Kong (PH inc) vs Yap Siok Moy (BN) vs S Tinagaran (PSM)."
    if code == "N13":
        rec["pir09_note"] = "Indep Bujang Abu (75) withdrew (tarik diri) — incomplete SPR docs; NOT a Bersatu/party withdrawal."
    if code == "N33":
        rec["pir09_note"] = "5-cornered; 2 independents incl Datuk A Saravanan ('Datuk' title — likely former establishment/MIC figure)."
    if code == "N10":
        rec["pir09_note"] = "5-cornered; indep Omar Mohd Isa + Berjasa present."
    seat_records.append(rec)

# ---- Candidate persons (deduplicated, canonical from seats) ----
cand_names = []
seen = set()
for s in seat_records:
    for c in s["candidates"]:
        n = c["name"]
        if n not in seen:
            seen.add(n); cand_names.append(n)

# ---- National figures / officials / PIR actors (NOT in candidate list) ----
national_figures = [
  {"name":"Datuk Seri Dr. Ronald Kiandee","aliases":["Ronald Kiandee","Datuk Seri Ronald Kiandee"],
   "role":"Former/suspended Bersatu Vice-President; MP Beluran","party":"Bersatu",
   "pir_tags":["PIR-06"],
   "pir06_role":"PRIMARY PIR-06 actor — issued Facebook statement (Nomination Day) that PN Supreme Council (Majlis Tertinggi) has 'asas kukuh' (strong grounds) to remove Bersatu, after Bersatu fielded candidates vs PN partners in 8 seats. PRECURSOR signal (no formal removal notice yet).",
   "sources":["NST","Utusan","BERNAMA wire"]},
  {"name":"Wong Chia Zhen","role":"Gerakan Secretary-General","party":"Gerakan (PN component)",
   "pir_tags":["PIR-09"],
   "pir09_role":"Issued immediate-effect expulsion (pecat) of Tang Jay Son for contesting on Bersatu ticket — 'serious breach of party discipline / contrary to principle of loyalty'.",
   "sources":["NST/BERNAMA","BHarian","AstroAwani","The Star"]},
  {"name":"Datuk Seri Anwar Ibrahim","aliases":["Anwar Ibrahim"],"role":"Prime Minister; PH Chairman","party":"PH/PKR",
   "pir_tags":["PIR-07"],
   "pir07_role":"Asked NS voters to give PH a stronger mandate for clean/stable administration under MB Aminuddin.",
   "sources":["NST","BHarian","AstroAwani","The Star"]},
  {"name":"Datuk Seri Dr. Ahmad Zahid Hamidi","aliases":["Zahid Hamidi","Ahmad Zahid Hamidi"],"role":"Deputy Prime Minister; BN Chairman","party":"BN/UMNO",
   "pir_tags":["PIR-07"],
   "pir07_role":"Escorted BN candidates (Tok Mat-Rantau, Zaifulbahri-Chembong, Suhaimi Aini-Kota) with lion-dance procession to Dewan Seri Rembau; also GEMA@KKDW program at Felda Palong 8, Jempol.",
   "sources":["Utusan"]},
  {"name":"Datuk Seri Johari Abdul Ghani","aliases":["Johari Abdul Ghani"],"role":"UMNO Vice-President","party":"BN/UMNO",
   "pir_tags":["PIR-07"],
   "pir07_role":"Escorted BN candidate Suhaimizan Bizar (Gemencheh) to Dewan Perdana Tampin on Nomination Day.",
   "sources":["Utusan"]},
  {"name":"Tan Sri Muhyiddin Yassin","aliases":["Muhyiddin"],"role":"Bersatu President; former PM","party":"Bersatu",
   "pir_tags":["PIR-06"],
   "pir06_role":"Positioned Bersatu as sole opposition voice; key figure to watch for response to Kiandee 'asas kukuh' statement (PIR-06 next-cycle watch).",
   "sources":["NST","Utusan"]},
  {"name":"Datuk Seri Hamzah Zainudin","aliases":["Hamzah Zainudin"],"role":"Founder of Parti Wawasan Negara; PN Secretary-General","party":"Wawasan/PN",
   "pir_tags":["PIR-06"],
   "pir06_role":"Wawasan contests Bersatu in 4 of the 8 Tier-4 seats (Klawang, Sikamat, Mambau, Gemas). PIR-06 watch figure.",
   "sources":["NST (priority_pir06 file)","collection_metadata"]},
  {"name":"Datuk Seri Ramlan Harun","role":"Chairman, Suruhanjaya Pilihan Raya (SPR)","party":"(official/independent)",
   "pir_tags":["PIR-07"],
   "pir07_role":"Confirmed 103 candidates for PRN NS 2026 (PH 36, BN 25, Bersatu 24, PN 11, 4 independents, Berjasa/Asli/PSM 1 each).",
   "sources":["Utusan"]},
  {"name":"Bujang Abu","role":"Independent candidate (withdrew); 75-yr-old street musician / ex-govt servant","party":"Independent (Bebas)",
   "pir_tags":["PIR-09"],
   "pir09_role":"Tarik diri (withdrew) at nomination for N13 Sikamat — failed to submit 2023 election expense report (SPR requirement). Paperwork-related; NOT a Bersatu/party withdrawal. Minor PIR-09 note.",
   "sources":["Utusan","collection_metadata"]},
  {"name":"Fuziah","role":"PKR / PH spokesperson (quoted re: parties' right to set own strategy)","party":"PKR/PH",
   "pir_tags":["PIR-07"],
   "pir07_role":"Quoted: 'PKR, PH respect parties' right to set own strategy for N9 polls'. (Full identity not expanded in source.)",
   "sources":["NST"]},
  {"name":"Tan Sri Annuar Musa","aliases":["Annuar Musa"],"role":"Senior BN/UMNO figure","party":"BN/UMNO",
   "pir_tags":["PIR-07"],
   "pir07_role":"At Port Dickson on Nomination Day; stated BN-PN will campaign together / share ceramah stage ('BN-PN akan kempen bersama, kongsi pentas ceramah').",
   "sources":["Utusan"]},
  {"name":"Dr Wee","aliases":["Dr Wee Ka Siong (inferred)"],"role":"MCA President; BN","party":"BN/MCA",
   "pir_tags":["PIR-07"],
   "pir07_role":"Stated BN-Perikatan have an 'understanding' for NS polls, NOT a merger — framed as determinant for Melaka & PRU16.",
   "sources":["The Star"],"inference_note":"Headline reads 'Dr Wee'; full name Wee Ka Siong (MCA president) inferred from context — not spelled out in source text."},
]

# PIR-06 watch figures (named in collection_metadata next_cycle_watch, not directly quoted in articles)
pir06_watch_figures = [
  {"name":"Tan Sri Muhyiddin Yassin","note":"Already listed above — PIR-06 response watch."},
  {"name":"Datuk Seri Hamzah Zainudin","note":"Already listed above — PIR-06 response watch."},
  {"name":"Tan Sri Abdul Hadi Awang","aliases":["Hadi Awang"],"role":"PAS President","party":"PAS/PN",
   "pir_tags":["PIR-06"],"pir06_role":"Watch for response to Kiandee 'asas kukuh' statement (collection_metadata next_cycle_watch).","sources":["collection_metadata"]},
  {"name":"Dr Samsuri Anuar","aliases":["Samsuri"],"role":"Bersatu leader / Terengganu MB","party":"Bersatu",
   "pir_tags":["PIR-06"],"pir06_role":"Watch for response to Kiandee statement (collection_metadata next_cycle_watch).","sources":["collection_metadata"]},
]

# National-role annotations for candidates who are also national figures
candidate_national_roles = {
 "Anthony Loke Siew Fook": ("PH Secretary-General / Transport Minister","PIR-07"),
 "Datuk Seri Mohamad Hasan": ("Deputy Finance Minister / 'Tok Mat'","PIR-07"),
 "Datuk Seri Aminuddin Harun": ("Caretaker Menteri Besar (moved N13->N32)","PIR-07"),
 "Datuk Seri Jalaluddin Alias": ("UMNO NS Liaison Chief / MP Jelebu","PIR-07"),
 "Datuk Dr Mohamad Rafie Ab Malek": ("Former 2018 PH winner (defected to PAS) — PIR-09 defector angle","PIR-09"),
 "Tang Jay Son": ("Ex-Gerakan, expelled for contesting on Bersatu ticket — PIR-09","PIR-09"),
 "Danni Rais": ("PN-Wawasan N04; son of veteran politician Rais Yatim (collector note)","PIR-07"),
}

# Referenced peripheral political figure (collector note only)
peripheral_figures = [
  {"name":"Tan Sri Rais Yatim","role":"Veteran politician (father of Danni Rais, PN-Wawasan N04)","pir_tags":["PIR-07"],
   "note":"Referenced in collector analysis only; not a 2026 candidate.","sources":["priority_pir07 file (collector note)"]},
]

# ---- Parties & coalitions ----
parties = [
  "UMNO","MCA","MIC","PAS","Bersatu (Parti Pribumi Bersatu Malaysia)","Gerakan",
  "DAP","PKR","Amanah (AMANAH)","Wawasan (Parti Wawasan Negara)","MIPP",
  "Berjasa (Barisan Jamaah Islamiah Semalaysia)","Asli (Parti Orang Asli Malaysia)",
  "PSM (Parti Sosialis Malaysia)","Bebas (Independent)"
]
coalitions = [
  "PH (Pakatan Harapan)","BN (Barisan Nasional)","PN (Perikatan Nasional)",
  "Pakatan Rakyat (PR) — historical coalition (pre-PH, referenced re: 2008 Ampangan)",
  "Kerajaan Perpaduan (Unity Government) — federal, referenced re: BN role"
]

# ---- Organizations ----
organizations = [
  "Suruhanjaya Pilihan Raya (SPR) — Election Commission",
  "Majlis Tertinggi PN (PN Supreme Council) — PIR-06 critical body (grounds to remove Bersatu)",
  "Dewan Undangan Negeri (DUN) Negeri Sembilan",
  "EXCO Negeri Sembilan",
  "Majlis Bandaraya Seremban (MBS)",
  "Badan Perhubungan UMNO Negeri Sembilan",
  "Polis Diraja Malaysia (PDRM)",
  "BERNAMA (national news wire)",
  "NSTP (New Straits Times Press)",
  "IPD Port Dickson"
]

# ---- Events ----
events = [
  "PRN Negeri Sembilan 2026 (Pilihan Raya Negeri ke-16)",
  "Hari Penamaan Calon (Nomination Day, 18 Julai 2026)",
  "Hari Pengundian (Polling Day, 1 Ogos 2026)",
  "Pengundian Awal (Early Voting, 28 Julai 2026)",
  "Kempen PRN Negeri Sembilan (campaign period ~2 weeks)",
  "Pelancaran Manifesto BN (24 Julai 2026, DUN Linggi) [PIR-07]",
  "Perarakan tarian singa Rantau — Zahid escorts Tok Mat/Zaifulbahri/Suhaimi Aini to Dewan Seri Rembau (Nom Day) [PIR-07]",
  "Ops Penamaan Calon BN Jelebu — Chennah/Pertang/Sungai Lui/Klawang to Dewan Besar Kuala Klawang (Nom Day) [PIR-07]",
  "Ops Penamaan Calon BN Gemencheh — Johari Abdul Ghani escorts Suhaimizan Bizar to Dewan Perdana Tampin (Nom Day) [PIR-07]",
  "Kempen Bersama BN-PN / Kongsi Pentas Ceramah — Annuar Musa statement (Port Dickson) [PIR-07]",
  "Pecatan Tang Jay Son oleh GERAKAN (immediate-effect, Nomination Day) [PIR-09]",
  "Kenyataan Ronald Kiandee 'asas kukuh' (Facebook post, Nomination Day) — PIR-06 PRECURSOR signal [PIR-06]",
  "Penarikan diri Bujang Abu (N13 Sikamat) — dokumen SPR tidak lengkap [PIR-09]",
]

# ---- Issues / signals (PIR-tagged) ----
issues = [
  {"issue":"Perpecahan Bersatu-PN (Bersatu-PN split)","pir_tags":["PIR-06"]},
  {"issue":"Isyarat pra-pembuangan Bersatu daripada PN — Kiandee 'asas kukuh' (precursor, no formal notice yet)","pir_tags":["PIR-06"]},
  {"issue":"Bersatu vs komponen PN di 8 kerusi Tier-4 (N04,N05,N13,N14,N23,N25,N31,N34)","pir_tags":["PIR-06"]},
  {"issue":"Disiplin komponen PN terhadap defector ke Bersatu (Gerakan pecat Tang Jay Son)","pir_tags":["PIR-06","PIR-09"]},
  {"issue":"Kredibiliti calon / defector-hopper (Rafie 2018 PH -> PAS/PN, N14 Ampangan)","pir_tags":["PIR-09"]},
  {"issue":"Peperangan mesej Day-1 N14 Ampangan (PH 'defector' vs PN 'experienced rep')","pir_tags":["PIR-09","PIR-07"]},
  {"issue":"Latar belakang calon bebas — Datuk A Saravanan (N33) credibility vetting","pir_tags":["PIR-09"]},
  {"issue":"Penarikan diri calon bebas (Bujang Abu, dokumen — bukan calon parti)","pir_tags":["PIR-09"]},
  {"issue":"Fragmentasi kerusi (1v1: 27->11; 3-penjuru: 7->21; 4-penjuru: 2; 5-penjuru: 2)","pir_tags":["PIR-07"]},
  {"issue":"Persefahaman BN-PN (bukan penggabungan) — penentu Melaka & PRU16 (Wee)","pir_tags":["PIR-07"]},
  {"issue":"Calon Menteri Besar diputuskan selepas PRN (BN; tidak diumum awal)","pir_tags":["PIR-07"]},
  {"issue":"Mandat kukuh PH (Anwar) — kesinambungan pentadbiran bersih/stabil di bawah MB Aminuddin","pir_tags":["PIR-07"]},
  {"issue":"Pencalonan semula MB Aminuddin N.13 -> N.32 (caretaker MB seat move)","pir_tags":["PIR-07"]},
  {"issue":"Pertembungan tokoh utama (marquee fights: N01 Loke vs Siow; N27 Tok Mat vs Dr Azizul)","pir_tags":["PIR-07"]},
  {"issue":"Calon Bebas/penyingkir undi (independents splitting votes)","pir_tags":["PIR-07","PIR-09"]},
  {"issue":"Penyandang diganti/berpindah (incumbents replaced/moved)","pir_tags":["PIR-07"]},
  {"issue":"Penyatuan undi Melayu (Malay vote consolidation)","pir_tags":["PIR-07"]},
]

# ---- Locations (incl nomination centers) ----
locations_existing = ["Ampangan","Bagan Pinang","Bahau","Bukit Kepayang","Chennah","Chuah","Gemas",
 "Gemenceh","Jelebu","Jempol","Jeram Padang","Johol","Juasseh","Klawang","Kota","Kuala Lumpur",
 "Kuala Pilah","Labu","Lenggeng","Linggi","Lobak","Lukut","Mambau","Nilai","Palong","Paroi",
 "Pertang","Pilah","Port Dickson","Putrajaya","Rahang","Rantau","Rembau","Repah","Senaling",
 "Seremban","Seremban Jaya","Seri Menanti","Serting","Sikamat","Sungai Lui","Tampin","Temiang"]
locations_new = [
  "Dewan Besar Kuala Klawang (Jelebu) — nomination centre [PIR-07]",
  "Dewan Seri Rembau (Rantau) — nomination centre [PIR-07]",
  "Dewan Perdana Tampin (Gemencheh) — nomination centre [PIR-07]",
  "Wisma Majlis Bandaraya Seremban / Wisma MBS Forest Heights — nomination centre (Sikamat, Ampangan et al.) [PIR-07]",
  "Felda Palong 8, Jempol — GEMA@KKDW program venue (Zahid) [PIR-07]",
  "Parlimen Seremban (federal constituency)",
]
# peripheral non-PRN locations seen in feeds
peripheral_locations = ["Petaling Jaya (PJ)","Klang Valley","Bagan Datuk","Kluang","Kuantan","Kangar","Kinabatangan"]

# ---- Media bylines (person names in content, non-political) ----
media_bylines = [
  "Nazarudin Shahari (Utusan photographer/reporter)","Amirul Aiman Osman (Utusan)",
  "Fatin Norizati Mat Isa (Utusan)","Iskandar Ishak (Utusan)",
  "Nor Ain Mohamed Radhi (NST)","Bernama (wire)"
]

# ---- PIR priority index ----
pir_index = {
 "PIR-06": {
   "title":"PN-Removal-of-Bersatu Watch (HIGHEST)",
   "status":"ELEVATED WATCH — NO formal removal notice; HIGH-CONFIDENCE PRECURSOR signal detected",
   "formal_removal_notice_detected": False,
   "precursor_signal_detected": True,
   "primary_actor":"Datuk Seri Dr. Ronald Kiandee (suspended/former Bersatu VP, MP Beluran)",
   "signal_keywords":["asas kukuh","Majlis Tertinggi","keluar","remove","Bersatu","PN"],
   "critical_body":"Majlis Tertinggi PN (PN Supreme Council)",
   "tier4_seats": PIR06_TIER4,
   "tier4_component_split":{"vs_PAS":4,"vs_Wawasan":4},
   "watch_figures_next_cycle":["Muhyiddin Yassin","Hamzah Zainudin","Hadi Awang","Samsuri Anuar"],
   "entities":["Datuk Seri Dr. Ronald Kiandee","Tan Sri Muhyiddin Yassin","Datuk Seri Hamzah Zainudin",
               "Majlis Tertinggi PN","Bersatu","PN","PAS","Wawasan","Gerakan"],
   "seat_entities":[f"{c} {tier4_detail[c]['bersatu']} (Bersatu) vs {tier4_detail[c]['pn_component']}" for c in PIR06_TIER4]
 },
 "PIR-09": {
   "title":"Candidate Credibility (SECOND)",
   "bersatu_candidates_count":24,
   "bersatu_candidate_seats":BERSATU_CAND_SEATS,
   "independents":INDEPENDENTS,
   "independents_count":4,
   "rafie_n14":"Datuk Dr Mohamad Rafie Ab Malek (PN-PAS) — former 2018 PH winner, defector/hopper angle",
   "gerakan_expulsion":{"subject":"Tang Jay Son","seat":"N22 Rahang","issued_by":"Wong Chia Zhen (Gerakan Sec-Gen)","action":"Expelled (pecat) immediate effect"},
   "withdrawal":{"subject":"Bujang Abu","seat_intended":"N13 Sikamat","type":"Independent (paperwork, NOT party)","triggers_pir06_tier4_alert":False},
   "entities":["Tang Jay Son","Wong Chia Zhen","Bujang Abu","Datuk Dr Mohamad Rafie Ab Malek",
               "Omar Mohd Isa","Teo Seng Lee","Datuk A Saravanan","Islah Wahyudi Zainudin","Gerakan","Bersatu"]
 },
 "PIR-07": {
   "title":"Battleground Assessment (THIRD)",
   "nomination_day":"18 Jul 2026","polling_day":"1 Aug 2026","early_voting":"28 Jul 2026",
   "total_candidates":103,
   "candidate_breakdown":{"PH":36,"BN":25,"Bersatu":24,"PN":11,"independents":4,"Berjasa":1,"Asli":1,"PSM":1},
   "contest_structure":{"straight_1v1":11,"three_cornered":21,"four_cornered":2,"five_cornered":2},
   "fragmentation_trend":"Sharply UP vs 2023 (straight 27->11; three-cornered 7->21)",
   "watch_seats":PIR07_WATCH,
   "marquee_day1_events":[
     "N01 Chennah: Anthony Loke (PH) vs Siow Kong Choon (BN-MCA) — straight fight",
     "N27 Rantau: Mohamad Hasan (Tok Mat, BN) vs Dr Azizul Hakim (PH) — straight fight; Zahid + lion-dance",
     "N32 Linggi: MB Aminuddin (PH-incumbent) 3-corner; 'not easy to enter a fortress'",
     "N14 Ampangan: Day-1 messaging war (see PIR-09)",
     "BN ops: Gemencheh (Johari Ghani), Jelebu (Jalaluddin), Rantau/Chembong/Kota (Zahid)"
   ],
   "messaging":{"bn_manifesto_launch":"24 Jul 2026 (DUN Linggi)","mb_candidate":"decided AFTER PRN",
     "anwar_pitch":"stronger PH mandate","bn_pn_framing":"understanding not merger (Wee)"},
   "entities":["Datuk Seri Anwar Ibrahim","Datuk Seri Dr. Ahmad Zahid Hamidi","Datuk Seri Johari Abdul Ghani",
               "Datuk Seri Jalaluddin Alias","Datuk Seri Aminuddin Harun","Anthony Loke Siew Fook",
               "Datuk Seri Mohamad Hasan","Tan Sri Annuar Musa","Dr Wee","Datuk Seri Ramlan Harun"]
 }
}

# ---- Build candidate person records with PIR tags ----
cand_person_records = []
for s in seat_records:
    for c in s["candidates"]:
        tags = list(s["pir_tags"])
        # refine: PIR-09 applies specifically to Bersatu candidates, independents, Rafie, Tang
        is_bersatu = c["ticket"].upper().startswith("BERSATU")
        is_indep = c["ticket"].upper() in ("BEBAS","BEBAS (INDEPENDENT)","BEBAS")
        if not (is_bersatu or is_indep):
            tags = [t for t in tags if t != "PIR-09"]
        if c["name"] == "Datuk Dr Mohamad Rafie Ab Malek" and "PIR-09" not in tags:
            tags.append("PIR-09")
        rec = {"name":c["name"],"ticket":c["ticket"],"seat":f"{s['code']} {s['name']}","pir_tags":tags}
        if c["name"] in candidate_national_roles:
            rec["national_role"], rt = candidate_national_roles[c["name"]]
            if rt not in rec["pir_tags"]: rec["pir_tags"].append(rt)
        cand_person_records.append(rec)

# ---- Assemble final document ----
now_utc = datetime.datetime(2026,7,18,16,57,23)
out = {
 "date":"20260718",
 "collection_date":"20260718",
 "processing_timestamp_utc": now_utc.isoformat()+"+00:00",
 "processing_timestamp_myt": (now_utc+datetime.timedelta(hours=8)).isoformat()+"+08:00",
 "file_id":"entities_165723",
 "cycle":"nomination-day-surge (post-153400 MYT cycle; director-approved PIR priorities)",
 "classification":"TLP:AMBER",
 "extractor":"prn_ns_entity_extraction_agent (scheduled cron)",
 "director_priority_approved":"2026-07-18 15:00 MYT",
 "source_count_total":86,
 "source_files_pir_relevant":["priority_pir06_kiandee-grounds-remove-bersatu_20260718_153142.md",
   "priority_pir09_gerakan-expels-tang-jay-son_20260718_153142.md",
   "priority_pir09_ampangan-day1-messaging-war_20260718_153142.md",
   "priority_pir07_day1-campaign-battleground_20260718_153142.md",
   "nstcommy_20260718_153251.md","utusancommy_20260718_153251.md","bhariancommy_20260718_153400.md",
   "astroawanicom_20260718_153251.md","thestarcommy_20260718_153251.md","ohbulancom_20260718_153251.md"],
 "pir_priorities":{
   "PIR-06":"PN-Removal-of-Bersatu Watch (HIGHEST)",
   "PIR-09":"Candidate Credibility (SECOND)",
   "PIR-07":"Battleground Assessment (THIRD)"
 },
 "counts":{
   "seats_parsed":len(seat_records),
   "candidate_persons_unique":len(cand_names),
   "national_figures_and_pir_actors":len(national_figures),
   "pir06_watch_figures":len(pir06_watch_figures),
   "parties":len(parties),
   "coalitions":len(coalitions),
   "organizations":len(organizations),
   "constituencies":len(seat_records),
   "events":len(events),
   "issues_and_signals":len(issues),
   "locations":len(locations_existing)+len(locations_new),
   "pir06_tier4_seats":len(PIR06_TIER4),
   "pir07_watch_seats":len(PIR07_WATCH),
   "pir09_bersatu_candidates":len(BERSATU_CAND_SEATS),
   "pir09_independents":len(INDEPENDENTS)
 },
 "seats":seat_records,
 "politicians":{
   "candidate_persons_unique":cand_names,
   "candidate_records_with_pir_tags":cand_person_records,
   "national_figures_and_pir_actors":national_figures,
   "pir06_watch_figures":pir06_watch_figures,
   "peripheral_referenced_figures":peripheral_figures,
   "total_unique_persons":len(set(cand_names+[f["name"] for f in national_figures]+[f["name"] for f in pir06_watch_figures]+[f["name"] for f in peripheral_figures]))
 },
 "parties":parties,
 "coalitions":coalitions,
 "organizations":organizations,
 "constituencies":[{"code":s["code"],"name":s["name"],"pir_tags":s["pir_tags"]} for s in seat_records],
 "events":events,
 "issues_and_signals":issues,
 "locations":{"constituency_and_district_locations":locations_existing,
   "nomination_centres_and_venues":locations_new,
   "peripheral_non_prn":peripheral_locations},
 "pir_priority_index":pir_index,
 "peripheral":{"media_bylines":media_bylines,
   "note":"Media byline names appear in collected content but are not political entities; listed for completeness only."}
}

os.makedirs(BASE, exist_ok=True)
with open(os.path.join(BASE,"entities_165723.json"),"w",encoding="utf-8") as f:
    json.dump(out,f,ensure_ascii=False,indent=2)

# ---- entity_metadata.json ----
meta = {
 "date":"20260718",
 "last_updated_utc": out["processing_timestamp_utc"],
 "last_updated_myt": out["processing_timestamp_myt"],
 "classification":"TLP:AMBER",
 "extractor":"prn_ns_entity_extraction_agent (scheduled cron)",
 "latest_entities_file":"entities_165723.json",
 "director_priority_approved":"2026-07-18 15:00 MYT",
 "cycle":"nomination-day-surge (post-153400)",
 "source_count_total":86,
 "counts":out["counts"],
 "pir_priority_tags":{
   "PIR-06":{
     "title":"PN-Removal-of-Bersatu Watch (HIGHEST)",
     "status":"ELEVATED WATCH — NO formal removal notice; PRECURSOR signal detected (Kiandee 'asas kukuh')",
     "tier4_seats":PIR06_TIER4,
     "entity_count":9,
     "key_entities":["Datuk Seri Dr. Ronald Kiandee","Majlis Tertinggi PN","Tan Sri Muhyiddin Yassin","Datuk Seri Hamzah Zainudin","Hadi Awang","Samsuri Anuar","Bersatu","PN","PAS","Wawasan","Gerakan"]
   },
   "PIR-09":{
     "title":"Candidate Credibility (SECOND)",
     "bersatu_candidate_seats":BERSATU_CAND_SEATS,
     "independents":list(INDEPENDENTS.keys()),
     "entity_count":9,
     "key_entities":["Tang Jay Son","Wong Chia Zhen","Bujang Abu","Datuk Dr Mohamad Rafie Ab Malek","Omar Mohd Isa","Teo Seng Lee","Datuk A Saravanan","Islah Wahyudi Zainudin","Gerakan"]
   },
   "PIR-07":{
     "title":"Battleground Assessment (THIRD)",
     "watch_seats":PIR07_WATCH,
     "entity_count":10,
     "key_entities":["Datuk Seri Anwar Ibrahim","Datuk Seri Dr. Ahmad Zahid Hamidi","Datuk Seri Johari Abdul Ghani","Datuk Seri Jalaluddin Alias","Datuk Seri Aminuddin Harun","Anthony Loke Siew Fook","Datuk Seri Mohamad Hasan","Tan Sri Annuar Musa","Dr Wee","Datuk Seri Ramlan Harun"]
   }
 },
 "seat_pir_tag_map":[ {"code":s["code"],"name":s["name"],"pir_tags":s["pir_tags"]} for s in seat_records ],
 "files_in_folder":[
   "entities_165723.json (this run — full extraction w/ PIR tags)",
   "entities_consolidated.json (prior 14:00 UTC run — candidate-list baseline)",
   "entities_politicians.json / entities_parties.json / entities_constituencies.json / entities_events.json / entities_issues.json / entities_organizations.json / entities_locations.json (prior 14:00 UTC sub-sets)",
   "entity_metadata.json (this file)",
   "_build_entities.py (build script)"
 ],
 "total_entities": (out["counts"]["candidate_persons_unique"]+out["counts"]["national_figures_and_pir_actors"]+out["counts"]["pir06_watch_figures"]+out["counts"]["parties"]+out["counts"]["coalitions"]+out["counts"]["organizations"]+out["counts"]["constituencies"]+out["counts"]["events"]+out["counts"]["issues_and_signals"]+out["counts"]["locations"])
}
with open(os.path.join(BASE,"entity_metadata.json"),"w",encoding="utf-8") as f:
    json.dump(meta,f,ensure_ascii=False,indent=2)

print("OK entities_165723.json + entity_metadata.json written")
print("counts:", json.dumps(out["counts"], ensure_ascii=False))
print("total_entities:", meta["total_entities"])
