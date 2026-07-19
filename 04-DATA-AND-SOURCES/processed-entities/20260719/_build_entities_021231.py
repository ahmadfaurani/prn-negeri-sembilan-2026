#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
PRN Negeri Sembilan 2026 — Entity Extraction Agent
Build: entities_021231.json  (cycle 20260719_011915 — Day-2 morning MYT enrichment)

Baseline: 20260718/entities_233104.json (231029 cycle — FIRST new-content cycle)
This cycle (011915, collected 09:19 MYT 19 Jul) ingest delta vs 231029:
  - 3 new fulltext priority articles:
      (1) Kosmo "Percaturan BN-PH-Bersatu"          09:05 MYT 19 Jul  [PIR-06]
      (2) Utusan "PRN NS penentu hala tuju DAP"      09:18 MYT 19 Jul  [PIR-07 rencana]
      (3) Utusan "Felda mesti terus angkat martabat" 08:28 MYT 19 Jul  [PIR-07 campaign-adjacent]
  - 2 PIR-06 WP-API probes (NST) returned HTTP 404 — no usable text
  - gnews headline-level corroboration (Tamim red notice, adat/royal crisis, Melaka fracture)

PIR-06 threshold (formal PN-MT removal notice): STILL NOT crossed.
103-candidate roster: UNCHANGED (no new candidates, no withdrawals, no Tier-4 withdrawals).

Classification: TLP:AMBER
"""
import json, copy, os
from datetime import datetime, timezone, timedelta

BASE_PATH = "/home/p62operator/.openclaw/workspace-ns/04-DATA-AND-SOURCES/processed-entities/20260718/entities_233104.json"
OUT_DIR   = "/home/p62operator/.openclaw/workspace-ns/04-DATA-AND-SOURCES/processed-entities/20260719"
OUT_FILE  = os.path.join(OUT_DIR, "entities_021231.json")
META_FILE = os.path.join(OUT_DIR, "entity_metadata.json")
FILE_ID   = "entities_021231"
PRIOR     = "entities_233104"

MYT = timezone(timedelta(hours=8))
now_utc = datetime.now(timezone.utc)
now_myt = now_utc.astimezone(MYT)
ts_utc = now_utc.strftime("%Y-%m-%dT%H:%M:%S+00:00")
ts_myt = now_myt.strftime("%Y-%m-%dT%H:%M:%S+08:00")

os.makedirs(OUT_DIR, exist_ok=True)

with open(BASE_PATH, encoding="utf-8") as f:
    d = json.load(f)

# ---------------------------------------------------------------------------
# 1. Core header fields — this is an enrichment build ON TOP of the 231029 baseline
# ---------------------------------------------------------------------------
d["date"] = "20260719"
d["collection_date"] = "20260719"
d["processing_timestamp_utc"] = ts_utc
d["processing_timestamp_myt"] = ts_myt
d["file_id"] = FILE_ID
d["cycle"] = (
    "nomination-day-surge + Day-2 morning enrichment (011915 cycle: 3 brand-new fulltext "
    "priority articles 08:28-09:18 MYT 19 Jul — Kosmo PIR-06 'Percaturan BN-PH-Bersatu', "
    "Utusan PIR-07 'PRN NS penentu hala tuju DAP' rencana, Utusan PIR-07 'Felda martabat "
    "peneroka' campaign-adjacent; entities_233104 baseline + 011915 enrichment; "
    "103-candidate roster UNCHANGED; PIR-06 threshold still NOT crossed)"
)
d["source_count_total"] = 89  # 86 prior + 3 new fulltext
d["prior_entities_file"] = PRIOR

# Append the new fulltext sources to the PIR-relevant file list
new_sources = [
    "priority_pir-06_percaturan-bn-ph-bersatu-kosmo_20260719_011915.md (NEW fulltext — Kosmo nomination recap 09:05 MYT 19 Jul; Bersatu 'keluar konsensus PN negeri' + 24 own-logo seats + 'memecah undi kawasan kritikal'; MIPP explicitly named in BN-PN components; Aminuddin Linggi 3-cornered vs Faizal/Zamri; 103/36 structure; operational-split STRONGEST confirmation to date)",
    "priority_pir-07_prn-ns-penentu-hala-tuju-dap-utusan_20260719_011915.md (NEW fulltext rencana — Utusan 09:18 MYT 19 Jul; DAP leadership referendum on Loke; NS adat/istana crisis as PRN issue; Aminuddin seat-move linked to adat crisis; Loke 'penyaluran dana' controversy with Balai Undang Luak Sungai Ujong; Melaka PH-BN fracture (4 DAP+1 Amanah ADUN withdrew); 41 kampung baru Cina / 13 DUN majority non-Malay; UEC; MCA 4->8 Johor)",
    "priority_pir-07_felda-martabat-peneroka-anwar-utusan_20260719_011915.md (NEW fulltext — Utusan 08:28 MYT 19 Jul; PM Anwar on Felda; NEW figures: Tan Sri Ahmad Badri Mohd. Zahir (new Felda Chairman) + Datuk Seri Ahmad Shabery Cheek (former, ended 30 Jun); campaign-adjacent/peripheral to NS PRN)",
    "priority_pir-06_bersatu-crossroads-nst-retry_20260719_011915.md (WP-API 404 — no text; NST not WP-backed)",
    "priority_pir-06_nst-ns-recent-wpapi_20260719_011915.md (WP-API 404 — no text)",
    "malaysiakinicom_gn_20260719_011915.md (gnews headlines — corroborating: 'Anwar: Don't campaign on NS ruler crisis; red notice applied for Tamim' [PIR-09 NEW legal-status], 'Loke vows fight against Umno leader who withdrew support, betrayed royal system', 'Can the derhaka card defeat BN?', 'High Court allows contempt bid against NS nobles', 'chieftains order Friday sermons to pray for Tunku Nadzaruddin')",
    "google_news_universalprnbersatu_html_20260719_011915.md (gnews 54 items P06=29/P07=42 — corroborating Bersatu own-logo + new-coalition-after-PRN framing)",
    "google_news_universalpnpecat_html_20260719_011915.md (gnews 45 items P06=35 — PIR-06 precursor corroborative, NO formal removal notice)",
    "google_news_universalnomination_html_20260719_011915.md (gnews 42 items P07=37 — 'Bersama sits out NS polls', 'MCA 7 seats MIC 4 — Zahid', '22,000 PDRM/ATM early vote')",
    "collection_metadata.json (011915 cycle — 3 new fulltext priority fetches; PIR-06 UNCHANGED; cycle_delta_vs_prior_231029 logged)"
]
d["source_files_pir_relevant"] = d.get("source_files_pir_relevant", []) + new_sources

# ---------------------------------------------------------------------------
# 2. Delta vs prior build (233104)
# ---------------------------------------------------------------------------
d["delta_vs_prior_build_" + PRIOR] = {
    "prior_build": PRIOR + ".json (23:31 UTC 18 Jul / 07:31 MYT 19 Jul — 231029 cycle)",
    "this_build": FILE_ID + ".json (" + now_utc.strftime("%H:%M") + " UTC 19 Jul / " + now_myt.strftime("%H:%M") + " MYT 19 Jul — 011915 cycle)",
    "cycle_window_ingested": ["011915 (Day-2 morning MYT; +2.15h vs 231029; 3 brand-new fulltext priority articles 08:28-09:18 MYT 19 Jul)"],
    "genuinely_new_findings": [
        "PIR-06: Kosmo nomination recap (fulltext) gives STRONGEST operational-split confirmation to date — Bersatu explicitly 'keluar daripada konsensus PN negeri' and contests 24 DUN seats under own logo, 'memecah undi di kawasan-kawasan kritikal'. Corroborative, NOT a formal PN-MT removal notice.",
        "PIR-06: BN-PN pact components explicitly enumerated — PAS, Gerakan, Wawasan, dan MIPP (MIPP first time named inside the BN-PN election pact); BN 25 calon + PN 11 kerusi to avoid friendly fights & maximise Malay vote.",
        "PIR-07 NEW ISSUE: NS adat/istana crisis ('kemelut membabitkan institusi adat dan pihak istana') surfaces as an explicit PRN campaign issue (Utusan rencana fulltext). Aminuddin criticised for failing to handle it; his Sikamat->Linggi move LINKED to the adat crisis (new framing vs baseline 'caretaker MB seat move').",
        "PIR-07 NEW ORG: Balai Undang Luak Sungai Ujong (NS adat institution) named in rencana re: Loke 'penyaluran dana' (fund-disbursement) controversy. Loke denies DAP interfering in adat/royal institution.",
        "PIR-07 NEW EVENT: Melaka PH-BN fracture — 4 DAP ADUN + 1 Amanah ADUN withdrew support from BN-led state govt; Melaka now effectively BN-only govt, 5 PH ADUN in opposition. Direct blow to 'Kerajaan Perpaduan' unity-govt narrative heading into NS PRN.",
        "PIR-07 NEW DATA: 41 kampung baru Cina in NS, concentrated in 13 DUN with non-Malay majority — DAP defence terrain. UEC (Sijil Peperiksaan Bersepadu) recognition an active Chinese-voter issue. MCA rose 4->8 seats in PRN Johor (pressure metric on DAP).",
        "PIR-07 NEW SIGNAL: Anthony Loke leadership referendum — PRN NS is a test of Loke's DAP Sec-Gen leadership (his home state); DAP defending all 11 seats won in PRU-14 (2018) & PRN 2023; Melaka PH-BN fracture adds 'party-of-principle vs hard-to-coalition' dual narrative.",
        "PIR-07 PERIPHERAL NEW FIGURES: Tan Sri Ahmad Badri Mohd. Zahir (new Felda Chairman, replacing Datuk Seri Ahmad Shabery Cheek who ended 30 Jun) — national news, campaign-adjacent only; Ahmad Badri ex-Ketua Setiausaha Perbendaharaan 2018-2020, boards BNM/PNB/TNB/Sime Darby, Chairman RHB Bank/LGM.",
        "PIR-09 NEW (headline-level): Tamim Dahri — red notice applied (Anwar statement via mkini gnews); Anwar also says 'Don't campaign on NS ruler crisis'. Escalation of Tamim independent-candidate legal status beyond baseline surrender+remand.",
        "CORROBORATION: 103 candidates / 36 DUN / PH36-BN25-Bersatu24-PN11-4ind / 94M-9W / youngest 23 (Leevineshwaraan Murugan, Bersatu N33) / oldest 70 (Abd Latif A Tambi, PH N35) / campaign to 11:59pm 31 Jul — all reconfirmed in Kosmo fulltext; no roster change."
    ],
    "corrections": [
        "M. Leevineshwaraan (Bersatu N33) full name confirmed as 'Leevineshwaraan Murugan' (Kosmo spells 'Leevineshwaraan Murugan, 23'); baseline 'M. Leevineshwaraan' enriched."
    ],
    "no_change": [
        "CRITICAL PIR-06 threshold (formal PN-MT removal notice) still NOT crossed.",
        "No Bersatu candidate withdrawals in the 8 Tier-4 seats (N04,N05,N13,N14,N23,N25,N31,N34).",
        "Candidate list (103 candidates) UNCHANGED — no new candidates, no withdrawals, no substitutions.",
        "PIR-09 N.14 Ampangan Day-1 messaging war unchanged (PH-defector vs experienced-rep).",
        "PIR-07 5 hot seats (Linggi N32, Sikamat N13, Ampangan N14, Paroi N25, Labu N20) unchanged; 7 Bersatu-vs-PN clash seats unchanged.",
        "Bersatu 24 own-logo seats list unchanged; BN 25 / PN 11 split unchanged."
    ]
}

# ---------------------------------------------------------------------------
# 3. Seats — enrich N32 Linggi (adat-crisis link), N33 (full name), N35 (already had oldest)
# ---------------------------------------------------------------------------
for s in d["seats"]:
    if s["code"] == "N32":
        # add adat-crisis link to the hot-seat character
        hs = s.setdefault("pir07_hot_seat", {})
        hs["adat_crisis_link_011915"] = (
            "Utusan rencana (09:18 MYT 19 Jul) links Aminuddin's Sikamat->Linggi move to the "
            "NS adat/istana crisis ('kemelut institusi adat'); MB criticised for failing to "
            "handle the adat issue effectively."
        )
    if s["code"] == "N33":
        # confirm full name of Bersatu candidate
        for c in s["candidates"]:
            if c["ticket"] == "BERSATU" and "Leevinesh" in c["name"]:
                c["full_name_confirmed_011915"] = "Leevineshwaraan Murugan (Kosmo, age 23 — youngest candidate of PRN NS 2026)"
        s.setdefault("pir07_note", {})
        if not isinstance(s.get("pir07_note"), dict):
            s["pir07_note"] = {"prior_note": s.get("pir07_note")}
        s["pir07_note"]["youngest_candidate_011915"] = "Leevineshwaraan Murugan (Bersatu), 23 — confirmed youngest of 103 candidates (Kosmo fulltext 09:05 MYT 19 Jul)."

# ---------------------------------------------------------------------------
# 4. Parties — add Bersama (sitting out) and Urimai (MACC report, not contesting)
# ---------------------------------------------------------------------------
# Avoid duplicates
party_names = set(p if isinstance(p, str) else p.get("name","") for p in d["parties"])
new_parties = [
    "Bersama (Parti Bersama Malaysia) — NOT contesting NS; sat out citing 'tougher terrain', focusing on Melaka (gnews The Malaysian Reserve / Newswav)",
    "Urimai (Parti Urimai) — NOT contesting NS; filed MACC report alleging RM3.06m allocated to Harapan reps before NS polls (mkini gnews) [PIR-07/09-adjacent]"
]
for np in new_parties:
    key = np.split(" ")[0]
    if not any(key in (p if isinstance(p,str) else p.get("name","")) for p in d["parties"]):
        d["parties"].append(np)

# ---------------------------------------------------------------------------
# 5. Coalitions — enrich BN-PN pact with MIPP-explicit enumeration
# ---------------------------------------------------------------------------
# Add an enrichment note to the PN coalition entry if present as string; else add standalone note
bn_pn_note = "BN-PN election pact (011915 Kosmo fulltext): components explicitly PAS, Gerakan, Wawasan, MIPP; BN contests 25 seats, PN fills 11 — designed to avoid friendly fights & maximise Malay vote. Distinct from formal coalition; Wee Ka Siong: 'not a merger'."
# store as a structured enrichment field rather than mutating coalition strings
d["coalition_pact_bn_pn_011915"] = bn_pn_note

# ---------------------------------------------------------------------------
# 6. Organizations — add Balai Undang Luak Sungai Ujong + Felda
# ---------------------------------------------------------------------------
new_orgs = [
    "Balai Undang Luak Sungai Ujong — NS adat/customary institution (Luak Sungai Ujong = Seremban/PD region); referenced re: Loke 'penyaluran dana' controversy & NS adat/istana crisis [PIR-07]",
    "Felda (Lembaga Kemajuan Tanah Persekutuan) — federal land-development authority; new chairman appointment campaign-adjacent to PRN [PIR-07 peripheral]",
    "Bank Negara Malaysia (BNM) — central bank (Ahmad Badri board background)",
    "Permodalan Nasional Bhd. (PNB) — GLC fund manager (Ahmad Badri board background)",
    "Tenaga Nasional Bhd. (TNB) — utility GLC (Ahmad Badri board background)",
    "RHB Bank Bhd. — Ahmad Badri former chairman",
    "Lembaga Getah Malaysia (LGM) — rubber board; Ahmad Badri former chairman",
    "Sime Darby Bhd. — conglomerate GLC; Ahmad Badri board member",
    "Kementerian Kewangan (Treasury) — Ahmad Badri entered civil service 1989; KSU Perbendaharaan 2018-2020",
    "Majlis Pemuda UMNO Malaysia (UMNO Youth) — referenced re: Akmal 'backdoor govt' (gnews)",
    "Urimai (party/org — see parties; filed MACC report)"
]
existing_orgs_blob = json.dumps(d["organizations"], ensure_ascii=False).lower()
for no in new_orgs:
    key = no.split(" —")[0].split("(")[0].strip().lower()
    if key not in existing_orgs_blob:
        d["organizations"].append(no)
        existing_orgs_blob += " " + key

# ---------------------------------------------------------------------------
# 7. Events — add Melaka PH-BN fracture + adat/royal crisis PRN-campaign surfacing
# ---------------------------------------------------------------------------
new_events = [
    "Perpecahan PH-BN Melaka (Melaka PH-BN fracture) — 4 ADUN DAP + 1 ADUN Amanah menarik sokongan daripada kerajaan negeri pimpinan BN; Melaka kini kerajaan BN sepenuhnya, 5 ADUN PH di blok pembangkang. Tamparan hebat kepada naratif Kerajaan Perpaduan menjelang PRN NS [PIR-07]",
    "Kemelut institusi adat & istana NS menjadi ISU KEMPEN PRN (Utusan rencana 09:18 MYT 19 Jul) — Aminuddin dikritik gagal tangani isu adat; perpindahan kerusi Sikamat->Linggi dikaitkan dengan kemelut adat; Loke 'penyaluran dana' dikaitkan dengan Balai Undang Luak Sungai Ujong [PIR-07]",
    "Lantikan Pengerusi Felda baharu — Tan Sri Ahmad Badri Mohd. Zahir menggantikan Datuk Seri Ahmad Shabery Cheek (tamat 30 Jun); kenyataan Anwar (Utusan 08:28 MYT 19 Jul); campaign-adjacent/peripheral [PIR-07]",
    "Amaran Anwar 'jangan kempen atas krisis ruler NS' (mkini gnews) + red notice dimohon untuk Tamim Dahri — eskalasi status perundangan calon-bebas Tamim melebihi penyerahan+reman baseline [PIR-09, PIR-07]",
    "Kempen 'derhaka card' vs BN (mkini COMMENT + Loke 'betrayed royal system') — naratif kesetiaan/adat sebagai modal kempen [PIR-07]",
    "High Court benarkan permohonan contempt terhadap pembesar NS (nobles) atas pertikaian pelantikan (mkini gnews) — eskalasi perundangan krisis adat [PIR-07]",
    "Pembesar NS (chieftains) arahkan khutbah Jumaat mendoakan Tunku Nadzaruddin (mkini gnews) — Tunku Nadzaruddin tokoh diraja NS [PIR-07]",
    "Bersama (parti) umum tidak bertanding PRN NS — fokus Melaka (gnews) [PIR-07]",
    "Urimai lapor MACC: RM3.06m diagihkan kepada wakil Harapan sebelum PRN NS (mkini gnews) [PIR-07, PIR-09-adjacent]",
    "Zahid: MCA bertanding 7 kerusi, MIC 4 kerusi PRN NS (gnews The Malaysian Reserve / KLSE) — pecahan komponen BN [PIR-07]",
    "22,000 personel PDRM/ATM mengundi awal PRN NS (gnews The Edge) [PIR-07]"
]
# dedupe by leading phrase
existing_events_blob = json.dumps(d["events"], ensure_ascii=False).lower()
for ne in new_events:
    head = ne.split(" —")[0][:40].lower()
    if head not in existing_events_blob:
        d["events"].append(ne)
        existing_events_blob += " " + head

# ---------------------------------------------------------------------------
# 8. Issues & signals — add new issues
# ---------------------------------------------------------------------------
new_issues = [
    {"issue": "Kemelut institusi adat & istana NS menjadi modal/isyarat kempen PRN — Aminuddin dikritik gagal tangani; perpindahan kerusi dikaitkan dengan kemelut adat (Utusan rencana 09:18 MYT 19 Jul)", "pir_tags": ["PIR-07"]},
    {"issue": "Loke 'penyaluran dana' & Balai Undang Luak Sungai Ujong — dakwaan dana ke entiti yang dipertikaan oleh balai adat; Loke nafi DAP campuri urusan adat/istana (Utusan rencana)", "pir_tags": ["PIR-07"]},
    {"issue": "Perpecahan PH-BN Melaka (4 DAP+1 Amanah ADUN tarik sokongan) — tamparan kepada naratif Kerajaan Perpaduan menjelang PRN NS", "pir_tags": ["PIR-07"]},
    {"issue": "Referendum kepimpinan Loke — PRN NS ujian kuat kepemimpinan Loke sebagai Setiausaha Agung DAP (negeri kelahirannya); pertahan 11 kerusi PRU-14 & PRN 2023", "pir_tags": ["PIR-07"]},
    {"issue": "Demografi pengundi Cina NS — 41 kampung baru Cina, 13 DUN majoriti bukan Melayu; UEC (Sijil Peperiksaan Bersepadu) pengiktirafan separuh sebagai isu aktif", "pir_tags": ["PIR-07"]},
    {"issue": "Tekanan MCA ke atas DAP — MCA 4->8 kerusi PRN Johor; potensi tekanan undi Cina di NS", "pir_tags": ["PIR-07"]},
    {"issue": "Red notice dimohon untuk Tamim Dahri (calon bebas NS) + amaran Anwar jangan kempen atas krisis ruler — eskalasi status perundangan calon bebas (mkini gnews)", "pir_tags": ["PIR-09", "PIR-07"]},
    {"issue": "PIR-06 operational-split TERKUAT setakat ini — Kosmo (fulltext 09:05 MYT 19 Jul): Bersatu 'keluar daripada konsensus PN negeri', 24 kerusi bawah logo sendiri, 'memecah undi di kawasan-kawasan kritikal' (BUKAN notis MT formal)", "pir_tags": ["PIR-06", "PIR-07"]},
    {"issue": "BN-PN pact komponen eksplisit — PAS, Gerakan, Wawasan, MIPP; BN 25 calon + PN 11 kerusi (elak pertembungan sesama sendiri, maksimum undi Melayu); MIPP pertama kali dinamakan dalam pact (Kosmo fulltext)", "pir_tags": ["PIR-06", "PIR-07"]},
    {"issue": "Naratif 'derhaka card' / 'betrayed royal system' sebagai modal kempen (mkini COMMENT + Loke) — sentimen kesetiaan-adat di kalangan pengundi Melayu", "pir_tags": ["PIR-07"]},
    {"issue": "Eskalasi perundangan krisis adat NS — High Court benarkan contempt bid vs pembesar NS; chieftains arahkan khutbah Jumaat mendoakan Tunku Nadzaruddin (mkini gnews)", "pir_tags": ["PIR-07"]},
    {"issue": "Pecahan komponen BN NS — MCA 7 kerusi, MIC 4 kerusi (Zahid); jumlah 25 calon BN (gnews)", "pir_tags": ["PIR-07"]}
]
existing_issues_blob = json.dumps(d["issues_and_signals"], ensure_ascii=False).lower()
for ni in new_issues:
    head = ni["issue"][:50].lower()
    if head not in existing_issues_blob:
        d["issues_and_signals"].append(ni)
        existing_issues_blob += " " + head

# ---------------------------------------------------------------------------
# 9. Peripheral / national figures — add Ahmad Badri, Shabery, Tunku Nadzaruddin
# ---------------------------------------------------------------------------
# Baseline peripheral is a dict with media_bylines/note; add structured figures
if not isinstance(d.get("peripheral"), dict):
    d["peripheral"] = {"prior": d.get("peripheral")}
d["peripheral"]["figures_new_011915"] = [
    {
        "name": "Tan Sri Ahmad Badri Mohd. Zahir",
        "role": "Pengerusi Felda (baharu)",
        "context": "Dilantik Pengerusi Felda menggantikan Ahmad Shabery Cheek (tamat 30 Jun); kenyataan Anwar (Utusan 08:28 MYT 19 Jul). Bekas Ketua Setiausaha Perbendaharaan 2018-2020; Ahli Lembaga BNM/PNB/TNB/Sime Darby; Pengerusi RHB Bank & LGM.",
        "pir_relevance": "PIR-07 campaign-adjacent (PM/Felda, national) — NOT an NS candidate",
        "source": "priority_pir-07_felda-martabat-peneroka-anwar-utusan_20260719_011915.md (fulltext)"
    },
    {
        "name": "Datuk Seri Ahmad Shabery Cheek",
        "role": "bekas Pengerusi Felda (tamat 30 Jun 2026)",
        "context": "Diganti oleh Ahmad Badri Mohd. Zahir.",
        "pir_relevance": "peripheral (national Felda leadership)",
        "source": "priority_pir-07_felda-martabat-peneroka-anwar-utusan_20260719_011915.md (fulltext)"
    },
    {
        "name": "Tunku Nadzaruddin",
        "role": "tokoh diraja Negeri Sembilan (ruler/royal figure)",
        "context": "Pembesar NS (chieftains) arahkan khutbah Jumaat mendoakan Tunku Nadzaruddin (mkini gnews); konteks krisis adat/istana NS yang menjadi isu kempen PRN.",
        "pir_relevance": "PIR-07 (adat/royal crisis context) — headline-level only",
        "source": "malaysiakinicom_gn_20260719_011915.md (gnews headline)"
    }
]

# ---------------------------------------------------------------------------
# 10. PIR priority index — update with this-cycle deltas
# ---------------------------------------------------------------------------
d["pir_priority_index"] = d.get("pir_priority_index", {})
d["pir_priority_index"]["PIR-06"] = {
    "title": "PN-Removal-of-Bersatu Watch (HIGHEST)",
    "status": "ESCALATED WATCH — UNCHANGED this cycle (011915). NO formal PN-MT removal notice. TWO-SIDED trajectory still ACTIVE. 011915 added STRONGEST operational-split confirmation to date: Kosmo fulltext states Bersatu 'keluar daripada konsensus PN negeri', 24 own-logo seats, 'memecah undi di kawasan-kawasan kritikal'. BN-PN pact components explicitly PAS/Gerakan/Wawasan/MIPP (BN25+PN11). Still NOT a formal MT removal notice. Trajectory unchanged: Bersatu voluntary realignment/exit AFTER Aug 1 poll most likely; reactive PN-MT removal remains possible if Bersatu candidates damage PN partners in Tier-4 seats.",
    "formal_removal_notice_detected": False,
    "escalation_detected": True,
    "this_cycle_new_pir06_content": True,
    "new_this_cycle": [
        "Kosmo fulltext (09:05 MYT 19 Jul): Bersatu 'keluar daripada konsensus PN negeri' + 24 own-logo seats + 'memecah undi di kawasan-kawasan kritikal' — strongest operational-split confirmation (corroborative, NOT a removal notice)",
        "Kosmo: BN-PN pact components explicitly PAS/Gerakan/Wawasan/MIPP; BN25+PN11 to avoid friendly fights & maximise Malay vote",
        "NST WP-API probes (2x) returned HTTP 404 — no usable text; no escalation there"
    ],
    "tier4_seats": ["N04","N05","N13","N14","N23","N25","N31","N34"],
    "key_entities": [
        "Tan Sri Muhyiddin Yassin","Datuk Seri Dr. Ronald Kiandee","Datuk Seri Hamzah Zainudin",
        "Majlis Tertinggi PN","Bersatu","PN","PAS","Gerakan","Wawasan","MIPP",
        "Datuk Seri Dr. Ahmad Samsuri Mokhtar"
    ]
}
d["pir_priority_index"]["PIR-09"] = {
    "title": "Candidate Credibility (SECOND)",
    "status": "ACTIVE. 103-candidate roster UNCHANGED (no new candidates, no withdrawals, no Tier-4 withdrawals). New headline-level legal-status development: red notice applied for Tamim Dahri (Anwar statement, mkini gnews) — escalation beyond baseline surrender+remand. N.14 Ampangan Day-1 messaging war unchanged. No new Bersatu-candidate bankruptcy/court-eligibility findings this cycle.",
    "bersatu_candidate_seats": d["pir_priority_index"].get("PIR-09",{}).get("bersatu_candidate_seats", [
        "N02","N03","N04","N05","N06","N07","N09","N10","N12","N13","N14","N15","N16","N17",
        "N20","N22","N23","N24","N25","N28","N31","N32","N33","N34"]),
    "independents": ["Omar Mohd Isa","Teo Seng Lee","Datuk A Saravanan","Islah Wahyudi Zainudin"],
    "key_entities": [
        "Tang Jay Son","Wong Chia Zhen","Bujang Abu","Datuk Dr Mohamad Rafie Ab Malek",
        "Omar Mohd Isa","Teo Seng Lee","Datuk A Saravanan","Islah Wahyudi Zainudin",
        "Gerakan","Bersatu","Albert Tei","Saw Yee Fung","Chong Sin Woon",
        "Tamim Dahri Abd Razak","Datuk Alzafny Ahmad","Datuk Dr Wee Ka Siong",
        "Leevineshwaraan Murugan (full name confirmed 011915)"
    ],
    "new_this_cycle": [
        "Red notice applied for Tamim Dahri (Anwar statement, mkini gnews) — escalation of independent-candidate legal status",
        "Anwar: 'Don't campaign on NS ruler crisis' (mkini gnews) — links Tamim legal status to adat/royal crisis",
        "Leevineshwaraan Murugan full name confirmed (Bersatu N33, age 23, youngest) — Kosmo fulltext"
    ]
}
d["pir_priority_index"]["PIR-07"] = {
    "title": "Battleground Assessment (THIRD)",
    "status": "ENRICHED. 011915 added the NS adat/istana crisis as an explicit PRN campaign issue (Utusan rencana fulltext) — Aminuddin seat-move linked to adat crisis; Loke 'penyaluran dana' controversy with Balai Undang Luak Sungai Ujong; Melaka PH-BN fracture (4 DAP+1 Amanah ADUN withdrew) blows to Kerajaan Perpaduan narrative; Loke leadership-referendum framing; 41 kampung baru Cina / 13 DUN non-Malay-majority / UEC; MCA 4->8 Johor pressure. 5 hot seats & 7 Bersatu-vs-PN clash seats UNCHANGED.",
    "watch_seats": ["N04","N05","N10","N13","N14","N15","N28","N32","N33"],
    "key_entities": [
        "Datuk Seri Anwar Ibrahim","Datuk Seri Dr. Ahmad Zahid Hamidi","Datuk Seri Johari Abdul Ghani",
        "Datuk Seri Jalaluddin Alias","Datuk Seri Aminuddin Harun","Anthony Loke Siew Fook",
        "Datuk Seri Mohamad Hasan","Tan Sri Annuar Musa","Datuk Dr Wee Ka Siong",
        "Datuk Seri Ramlan Harun","Datuk Dr Asyraf Wajdi Dusuki","Datuk Alzafny Ahmad",
        "Balai Undang Luak Sungai Ujong (NEW org)","Tunku Nadzaruddin (NEW royal figure)",
        "Tan Sri Ahmad Badri Mohd. Zahir (peripheral)","Datuk Seri Ahmad Shabery Cheek (peripheral)"
    ],
    "new_this_cycle": [
        "NS adat/istana crisis surfaces as PRN campaign issue (Utusan rencana 09:18 MYT 19 Jul) — Aminuddin criticised; seat-move linked to adat crisis",
        "Loke 'penyaluran dana' + Balai Undang Luak Sungai Ujong controversy — Loke denies DAP interfering in adat/royal institution",
        "Melaka PH-BN fracture (4 DAP+1 Amanah ADUN withdrew support) — blow to Kerajaan Perpaduan narrative",
        "Loke leadership-referendum framing; DAP defending all 11 seats (PRU-14 2018 & PRN 2023)",
        "41 kampung baru Cina / 13 DUN non-Malay majority; UEC recognition active issue; MCA 4->8 Johor",
        "Peripheral: Ahmad Badri Mohd. Zahir new Felda Chairman (campaign-adjacent)"
    ]
}

# ---------------------------------------------------------------------------
# 11. Counts
# ---------------------------------------------------------------------------
d["counts"] = d.get("counts", {})
d["counts"].update({
    "seats_parsed": 36,
    "candidate_persons_unique": 103,
    "national_figures_and_pir_actors": 18,
    "pir06_watch_figures": 4,
    "parties": len(d["parties"]),
    "coalitions": len(d["coalitions"]),
    "organizations": len(d["organizations"]),
    "constituencies": 36,
    "events": len(d["events"]),
    "issues_and_signals": len(d["issues_and_signals"]),
    "locations": d["counts"].get("locations", 53),
    "pir06_tier4_seats": 8,
    "pir07_watch_seats": 9,
    "pir09_bersatu_candidates": 24,
    "pir09_independents": 4,
    "confirmation_passes_since_170837": 0,
    "pir07_battleground_seats_tagged": d["counts"].get("pir07_battleground_seats_tagged", 11),
    "genuinely_new_entities_this_build": 7,
    "enriched_existing_entities_this_build": 6,
    "new_named_figures": ["Tan Sri Ahmad Badri Mohd. Zahir", "Datuk Seri Ahmad Shabery Cheek", "Tunku Nadzaruddin"],
    "new_organizations": ["Balai Undang Luak Sungai Ujong", "Felda (campaign-adjacent)"],
    "new_parties_referenced": ["Bersama (sat out NS)", "Urimai (filed MACC report, not contesting)"],
    "confirmed_full_names": ["Leevineshwaraan Murugan (Bersatu N33, age 23)"],
    "new_events_this_build": 11,
    "new_issues_this_build": 12,
    "candidate_roster_changed": False,
    "pir06_threshold_crossed": False
})

# ---------------------------------------------------------------------------
# 12. Write the entities file
# ---------------------------------------------------------------------------
d["total_entities"] = (
    len(d.get("seats",[])) + len(d.get("parties",[])) + len(d.get("coalitions",[])) +
    len(d.get("organizations",[])) + len(d.get("events",[])) + len(d.get("issues_and_signals",[])) +
    103 + 18 + 4 + 9 + 8 + 36 + len(d.get("peripheral",{}).get("figures_new_011915",[]))
)
with open(OUT_FILE, "w", encoding="utf-8") as f:
    json.dump(d, f, ensure_ascii=False, indent=2)
print("WROTE:", OUT_FILE, f"{os.path.getsize(OUT_FILE)} bytes")

# ---------------------------------------------------------------------------
# 13. Write entity_metadata.json
# ---------------------------------------------------------------------------
meta = {
    "date": "20260719",
    "last_updated_utc": ts_utc,
    "last_updated_myt": ts_myt,
    "classification": "TLP:AMBER",
    "extractor": "prn_ns_entity_extraction_agent (scheduled cron)",
    "latest_entities_file": FILE_ID + ".json",
    "prior_entities_file": PRIOR + ".json",
    "director_priority_approved": "2026-07-18 15:00 MYT",
    "cycle": "nomination-day-surge + Day-2 morning enrichment (011915: 3 brand-new fulltext priority articles 08:28-09:18 MYT 19 Jul — Kosmo PIR-06, Utusan PIR-07 DAP-direction rencana, Utusan PIR-07 Felda; 103-candidate roster UNCHANGED; PIR-06 threshold still NOT crossed)",
    "source_count_total": 89,
    "build_character": "ENRICHMENT / CORROBORATION BUILD — 3 new fulltext articles; 3 new peripheral figures (Ahmad Badri, Shabery, Tunku Nadzaruddin); 1 new NS org (Balai Undang Luak Sungai Ujong); 2 new non-contesting party refs (Bersama, Urimai); NS adat/istana crisis surfaces as PRN campaign issue (Aminuddin seat-move + Loke dana controversy); Melaka PH-BN fracture; Tamim red-notice escalation; Leevineshwaraan full name; PIR-06 strongest operational-split confirmation ('keluar konsensus PN negeri'); 103-candidate roster UNCHANGED; CRITICAL PIR-06 threshold still NOT crossed.",
    "delta_vs_prior_build": {
        "prior_build": PRIOR + ".json",
        "this_build": FILE_ID + ".json",
        "cycles_ingested": ["011915"],
        "genuinely_new_entities": 7,
        "enriched_existing_entities": 6,
        "corroborating_reconfirmations": 12,
        "verification": "collection_metadata.json (011915) + this agent's reconciliation of 3 priority fulltext articles + gnews headlines vs entities_233104 baseline (231029 cycle)."
    },
    "counts": d["counts"],
    "pir_priority_tags": {
        "PIR-06": d["pir_priority_index"]["PIR-06"],
        "PIR-09": d["pir_priority_index"]["PIR-09"],
        "PIR-07": d["pir_priority_index"]["PIR-07"]
    },
    "seat_pir_tag_map": d.get("seat_pir_tag_map", []),
    "files_in_folder": [
        FILE_ID + ".json (THIS run — Day-2 morning ENRICHMENT build; 011915 cycle: 3 new fulltext articles; adat/istana crisis + Melaka fracture + Tamim red notice + Ahmad Badri/Shabery/Tunku Nadzaruddin + Balai Undang Luak Sungai Ujong; 103-candidate roster unchanged; PIR-06 threshold still NOT crossed)",
        PRIOR + ".json (prior run — 231029 cycle Day-2 dawn enrichment; 20260718 folder)"
    ],
    "total_entities": d["total_entities"]
}
with open(META_FILE, "w", encoding="utf-8") as f:
    json.dump(meta, f, ensure_ascii=False, indent=2)
print("WROTE:", META_FILE, f"{os.path.getsize(META_FILE)} bytes")
print("PARTIES:", d["counts"]["parties"], "| ORGS:", d["counts"]["organizations"], "| EVENTS:", d["counts"]["events"], "| ISSUES:", d["counts"]["issues_and_signals"], "| TOTAL_ENTITIES:", d["total_entities"])
