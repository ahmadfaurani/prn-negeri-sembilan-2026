#!/usr/bin/env python3
"""
PRN Negeri Sembilan 2026 — Entity Extraction Agent (cron build script, run 190215 UTC).
Inherits the 36-seat candidate structure + prior PIR baseline from entities_165723.json,
then ingests the NEW content that arrived in the 170837 collection cycle (after the
16:57 UTC build) and the 182751 stability-confirmation cycle:

  NEW (PIR-06 ESCALATION):
    - Muhyiddin publicly hinting at Bersatu exit from PN ("wishing PN all the best",
      rapping PN chairperson Ahmad Samsuri Mokhtar for unilaterally entering BN pact
      and sidelining Bersatu from seat negotiations) — qualitative escalation
      (Bersatu-leadership signal, not just suspended VP Kiandee).
    - Muhyiddin signals Bersatu to form NEW coalition/bloc AFTER Negri polls.
    - Mainstream framing shifted to "Bersatu exit from PN imminent?" (mkini SNAPSHOT).
    - Hadi denies PAS made PN "toxic", blames Bersatu instead (blame-shifting).
    - "PN rift widens as PAS sends clearest signal yet of sidelining Bersatu".
    - Annuar Musa: Bersatu's own-logo use shows it wants to part ways with PN
      (collection_metadata labels speaker "Bersatu sec-gen" — caveat flagged;
      prominent Annuar Musa is the BN/UMNO veteran; Bersatu sec-gen is Hamzah Zainudin).

  CORRECTION:
    - Prior "Dr Samsuri Anuar" (role "Bersatu leader / Terengganu MB") was an error.
      Correct entity: "Datuk Seri Dr. Ahmad Samsuri Mokhtar" — PN CHAIRPERSON,
      Terengganu MB. Rapped by Muhyiddin; signals PN may continue BN cooperation
      if NS results positive.

  NEW (PIR-09):
    - Albert Tei — businessperson / PN supporter — "barking dogs" rhetoric targeting
      Harapan supporters at Dewan Besar Kuala Klawang (Jelebu) nomination centre.
    - Saw Yee Fung — MCA Youth secretary-general — told to stay out of NS polls
      campaign over BN-PN criticism (via MCA sec-gen Chong Sin Woon WhatsApp).
    - Chong Sin Woon — MCA secretary-general — issued the "you don't have to come" directive.
    - Tamim Dahri — activist — surrendered at Port Dickson (FB threat case); seeks to
      campaign for an independent candidate (independent support-network signal).

  NEW (PIR-07):
    - Asyraf Wajdi (Datuk Dr Asyraf Wajdi Dusuki) — "BN-PN understanding aimed at
      ensuring NS political stability" (NST).
    - Tunku Ismail Sultan Ibrahim — Johor Regent — peripheral, mkini SNAPSHOT framing.
    - DAP revives anti-BN campaign (1MDB scandal, ruler crisis) — PH-component tension.
    - "New political alignments needed to ensure stability" (Zahid) — jajaran politik baharu.
    - Chuah, Lukut, Bagan Pinang contests take shape (NST).

The 182751 cycle itself produced 0 new articles (deep-overnight MYT confirmation pass,
10/10 sources, 0 errors) — its value is coverage-integrity + PIR-06 escalated-watch
stability confirmation (no CRITICAL threshold crossing, no regression).

Classification: TLP:AMBER
"""
import json, os, copy, datetime

BASE = "/home/p62operator/.openclaw/workspace-ns/04-DATA-AND-SOURCES/processed-entities/20260718"
PREV = os.path.join(BASE, "entities_165723.json")

with open(PREV, "r", encoding="utf-8") as f:
    prev = json.load(f)

# ---- PIR seat sets (unchanged; candidate list (103) confirmed unchanged) ----
PIR06_TIER4 = ["N04","N05","N13","N14","N23","N25","N31","N34"]
PIR07_WATCH = ["N04","N05","N10","N13","N14","N15","N28","N32","N33"]
BERSATU_CAND_SEATS = ["N02","N03","N04","N05","N06","N07","N09","N10","N12","N13","N14",
                      "N15","N16","N17","N20","N22","N23","N24","N25","N28","N31","N32","N33","N34"]
INDEPENDENTS = {
    "Omar Mohd Isa":"N10 Nilai",
    "Teo Seng Lee":"N30 Lukut",
    "Datuk A Saravanan":"N33 Sri Tanjung",
    "Islah Wahyudi Zainudin":"N33 Sri Tanjung",
}

# ---- Inherit seats / candidate person records from previous build (unchanged) ----
seat_records = prev["seats"]
cand_person_records = prev["politicians"]["candidate_records_with_pir_tags"]
cand_names = prev["politicians"]["candidate_persons_unique"]

# ---- National figures / PIR actors (carry prior + update + add new) ----
national_figures = copy.deepcopy(prev["politicians"]["national_figures_and_pir_actors"])

# Update Annuar Musa entry: add PIR-06 tag + new statement + caveat about "Bersatu sec-gen" label
for nf in national_figures:
    if nf["name"] == "Tan Sri Annuar Musa":
        if "PIR-06" not in nf["pir_tags"]:
            nf["pir_tags"].append("PIR-06")
        nf["pir06_role"] = ("The Star reports 'Bersatu's use of own logo shows it wants to part "
            "ways with PN, says Annuar Musa' — publicly states Bersatu wants to part ways with PN "
            "(own-logo signal). CAVEAT: collection_metadata.json labels the speaker 'Bersatu "
            "sec-gen Annuar Musa'; however the known Bersatu Secretary-General is Datuk Seri "
            "Hamzah Zainudin, and the prominent 'Tan Sri Annuar Musa' is the BN/UMNO veteran. "
            "Naming ambiguity flagged — statement retained under this entry; do not conflate "
            "with Hamzah Zainudin.")
        nf["sources"].extend(["The Star (gnews)", "collection_metadata (170837 cycle)"])
        # dedupe sources
        nf["sources"] = list(dict.fromkeys(nf["sources"]))

# NEW national figures
new_figures = [
    {"name":"Albert Tei","aliases":["Albert Tei (businessperson)"],
     "role":"Businessperson; PN supporter (not a candidate)","party":"PN (supporter, not member-confirmed)",
     "pir_tags":["PIR-09"],
     "pir09_role":"Day-1 PN-camp messaging tone incident: admitted targeting PH/Harapan supporters "
       "gathered outside Dewan Besar Kuala Klawang (Jelebu) nomination centre, labelling them "
       "'barking dogs' (25-sec video clip, dressed in PN shirt). Abrasive rhetoric — character/"
       "credibility signal on a PN-side figure. Malaysiakini news/780042.",
     "sources":["Malaysiakini (priority_pir09_pn-camp-albert-barking-dogs_170837)"]},
    {"name":"Saw Yee Fung","role":"MCA Youth Secretary-General","party":"MCA (BN component)",
     "pir_tags":["PIR-09","PIR-07"],
     "pir09_role":"Allegedly instructed by MCA to skip the NS state election campaign after she "
       "openly criticised BN's decision to cooperate with PN. Revealed via lengthy Facebook post "
       "with screenshot of a WhatsApp message from MCA Sec-Gen Chong Sin Woon ('you don't have to "
       "come'). Internal BN-component disciplinary silencing of a dissenting Youth leader over the "
       "BN-PN pact — campaign-exclusion (not a candidate expulsion). Adds to the PN-component "
       "disciplinary-actions pattern (cf. Gerakan pecat of Tang Jay Son).",
     "sources":["Malaysiakini (priority_pir09_mca-youth-stay-out-ns-polls_170837)"]},
    {"name":"Chong Sin Woon","role":"MCA Secretary-General","party":"MCA (BN component)",
     "pir_tags":["PIR-09","PIR-07"],
     "pir09_role":"Issued the WhatsApp directive 'you don't have to come' to MCA Youth sec-gen "
       "Saw Yee Fung, excluding her from the NS campaign over her public criticism of the BN-PN "
       "cooperation. MCA disciplinary/credibility dynamic — PIR-09 party-discipline signal.",
     "sources":["Malaysiakini (priority_pir09_mca-youth-stay-out-ns-polls_170837)"]},
    {"name":"Tamim Dahri","aliases":["Tamim"],"role":"Activist (surrendered to police)","party":"(independent-aligned)",
     "pir_tags":["PIR-09"],
     "pir09_role":"Surrendered to police at Port Dickson over a Facebook threat case; publicly "
       "stated he hopes to campaign for an N Sembilan independent candidate. Independent-candidate "
       "support-network signal (which independent not specified in captured text).",
     "sources":["Malaysiakini (mkini homepage + mkini gnews, 170837/182751 cycles)"]},
    {"name":"Datuk Dr Asyraf Wajdi Dusuki","aliases":["Asyraf Wajdi"],
     "role":"UMNO figure (former Minister); quoted re: BN-PN understanding","party":"BN/UMNO",
     "pir_tags":["PIR-07"],
     "pir07_role":"Stated the BN-PN understanding is aimed at ensuring Negri Sembilan political "
       "stability (NST). BN-PN electoral-understanding cluster corroboration.",
     "sources":["NST (nstcommy gnews, 170837/182751 cycles)"]},
]
national_figures.extend(new_figures)

# ---- PIR-06 watch figures (correct Samsuri name; carry others) ----
pir06_watch_figures = copy.deepcopy(prev["politicians"]["pir06_watch_figures"])
for wf in pir06_watch_figures:
    if wf["name"] == "Dr Samsuri Anuar":
        wf["name"] = "Datuk Seri Dr. Ahmad Samsuri Mokhtar"
        wf["aliases"] = ["Ahmad Samsuri Mokhtar","Samsuri","Samsuri Mokhtar","Dr Samsuri Anuar (prior misreading)"]
        wf["role"] = "PN Chairperson; Menteri Besar of Terengganu"
        wf["party"] = "PAS/PN"
        wf["pir06_role"] = ("PN chairperson named by Muhyiddin as having UNILATERALLY entered an "
            "electoral pact with BN and sidelined Bersatu from seat negotiations — the trigger for "
            "Muhyiddin's exit hint. Samsuri separately signals PN may CONTINUE BN cooperation if "
            "NS results prove positive (NST, 17 Jul). HIGHEST-WEIGHT PIR-06 actor on the PN/PAS side. "
            "CORRECTION: prior build listed 'Dr Samsuri Anuar' as a 'Bersatu leader' — that was an "
            "error; the Terengganu MB / PN chairperson is Ahmad Samsuri Mokhtar (PAS/PN, not Bersatu).")
        wf["sources"] = ["Malaysiakini (priority_pir06_goodbye-pn-muhyiddin-raps-samsuri_170837)",
                         "NST (PN may continue BN cooperation, says Samsuri)",
                         "collection_metadata (170837/182751 cycles)"]
        wf["name_correction_note"] = "Corrected from 'Dr Samsuri Anuar' (prior build misreading) to 'Datuk Seri Dr. Ahmad Samsuri Mokhtar'."

# ---- Peripheral referenced figures (carry + add Tunku Ismail) ----
peripheral_figures = copy.deepcopy(prev["politicians"].get("peripheral_referenced_figures", []))
peripheral_figures.append(
    {"name":"Tunku Ismail Sultan Ibrahim","role":"Johor Regent (TMJ)",
     "pir_tags":["PIR-06"],
     "pir06_role":"Referenced in Malaysiakini SNAPSHOT framing 'Bersatu exit from PN imminent?' — "
       "mainstream outlet now framing exit as imminent (narrative-stage signal, not an action by "
       "TMJ). Peripheral; included for PIR-06 narrative-frame monitoring.",
     "note":"Referenced in a KINI SNAPSHOT headline; not a 2026 NS candidate and not an active PIR-06 actor.",
     "sources":["Malaysiakini (priority_pir06_bersatu-exit-pn-imminent-snapshot_170837)"]}
)

# ---- Parties / coalitions / organizations (carry prior) ----
parties = prev["parties"]
coalitions = prev["coalitions"]
organizations = prev["organizations"]

# ---- Events (carry prior + add new) ----
events = list(prev["events"])
new_events = [
    "Kenyataan Muhyiddin 'Goodbye PN?' — Bersatu president hinting at exit, wishing PN 'all the best', rapping PN chairperson Ahmad Samsuri Mokhtar over unilateral BN pact (captured 170837) [PIR-06]",
    "Isyarat Muhyiddin: Bersatu akan bentuk gabungan/blok baharu SELEPAS PRN Negeri Sembilan [PIR-06]",
    "SNAPSHOT Malaysiakini 'Bersatu exit from PN imminent?' — mainstream narrative entered imminent-departure framing [PIR-06]",
    "Hadi nafi PAS jadikan PN 'toxic', salahkan Bersatu pula (Free Malaysia Today) — blame-shifting (PAS side) [PIR-06]",
    "Arahan MCA kekaluar Saw Yee Fung (Youth sec-gen) daripada kempen PRN NS — WhatsApp Chong Sin Woon 'you don't have to come' [PIR-09]",
    "Insiden Albert Tei 'barking dogs' di Dewan Besar Kuala Klawang (Jelebu) — retorik kasar penyokong PN terhadap penyokong Harapan pada Hari Penamaan Calon [PIR-09]",
    "Penyerahan Tamim Dahri di Port Dickson (kes ugutan FB) + niat kempen calon bebas [PIR-09]",
    "DAP hidupkan semula kempen anti-BN (skandal 1MDB, krisis ruler) — ketegangan komponen PH dengan persefahaman BN-PN [PIR-07]",
    "BN-PN understanding aimed at ensuring NS political stability — Asyraf Wajdi (NST) [PIR-07]",
    "Chuah, Lukut, Bagan Pinang contests take shape (NST) — crystallizing battleground seats [PIR-07]",
]
events.extend(new_events)

# ---- Issues / signals (carry prior + add new) ----
issues = list(prev["issues_and_signals"])
new_issues = [
    {"issue":"Muhyiddin (Bersatu president) secara terbuka menggambarkan kemungkinan Bersatu keluar PN ('wishing PN all the best', raps Samsuri) — ESCALATION kualitatif (signal kepimpinan Bersatu, bukan VP digantung)","pir_tags":["PIR-06"]},
    {"issue":"Trajektori PIR-06 kini dua sisi: PN-MT-mungkin-buang-Bersatu (Kiandee) DAN Bersatu-mungkin-keluar-PN (Muhyiddin)","pir_tags":["PIR-06"]},
    {"issue":"Bersatu akan bentuk gabungan/bloc baharu selepas PRN NS (Muhyiddin) — pelan konkrit pasca-keluar","pir_tags":["PIR-06"]},
    {"issue":"Framing media arus perdana beralih ke 'Bersatu exit from PN imminent?' (mkini SNAPSHOT) — naratif peringkat pemergian imminent","pir_tags":["PIR-06"]},
    {"issue":"Hadi nafi PAS jadikan PN 'toxic', salahkan Bersatu — blame-shifting (sisi PAS dalam retak PN)","pir_tags":["PIR-06"]},
    {"issue":"PN rift widens — PAS hantar isyarat paling jelas untuk menyingkirkan Bersatu (mkini)","pir_tags":["PIR-06"]},
    {"issue":"Annuar Musa: penggunaan logo sendiri Bersatu tunjuk ia mahu berpisah dengan PN (caveat: pelabelan 'Bersatu sec-gen' oleh collector berkonflik dengan Hamzah Zainudin; nama prominent ialah veteran BN/UMNO)","pir_tags":["PIR-06"]},
    {"issue":"Disiplin dalaman komponen BN: MCA kaluar Youth sec-gen Saw Yee Fung dari kempen NS atas kritik BN-PN (Arahan Chong Sin Woon)","pir_tags":["PIR-09","PIR-07"]},
    {"issue":"Retorik kasar kempen Day-1 pihak PN — Albert Tei 'barking dogs' (Jelebu) — isyarat karakter/kredibiliti penyokong PN","pir_tags":["PIR-09","PIR-07"]},
    {"issue":"Rangkaian sokongan calon bebas — aktivis Tamim Dahri niat kempen calon bebas (calon tidak dinyatakan dalam teks tertangkap)","pir_tags":["PIR-09"]},
    {"issue":"DAP hidupkan semula kempen anti-BN (1MDB, krisis ruler) — ketegangan komponen PH dengan persefahaman BN-PN","pir_tags":["PIR-07"]},
    {"issue":"Jajaran politik baharu perlu pasti kestabilan (Zahid) — framing 'new political alignments'","pir_tags":["PIR-07"]},
]
issues.extend(new_issues)

# ---- Locations (carry prior) ----
locations = prev["locations"]

# ---- PIR priority index (update PIR-06 to ESCALATED; extend PIR-09/PIR-07) ----
pir_index = copy.deepcopy(prev["pir_priority_index"])

pir_index["PIR-06"].update({
    "status": ("ESCALATED WATCH — NO formal PN-MT removal notice; TWO-SIDED trajectory now ACTIVE. "
        "PN-MT-may-remove-Bersatu (Kiandee 'asas kukuh' call) AND Bersatu-may-exit-PN (Muhyiddin "
        "public exit hint + new post-poll bloc signal). Bersatu PRESIDENT (not a suspended VP) now "
        "signaling departure — qualitative escalation. Mainstream framing moved to 'imminent?'. "
        "Most likely near-term outcome: Bersatu voluntary realignment/exit AFTER Aug 1 poll rather "
        "than formal PN-MT expulsion beforehand; reactive PN-MT removal remains possible if Bersatu "
        "candidates damage PN partners in the 8 Tier-4 seats."),
    "escalation_detected": True,
    "formal_removal_notice_detected": False,
    "trajectory": "TWO-SIDED (PN-MT-may-remove-Bersatu AND Bersatu-may-exit-PN)",
    "muhyiddin_exit_hint": {
        "headline":"Goodbye PN?: Muhyiddin raps Samsuri over BN talks, Bersatu to move on",
        "source":"Malaysiakini","url":"https://www.malaysiakini.com/news/779941",
        "first_captured_cycle":"170837","reconfirmed_182751":True,
        "significance":"Bersatu-leadership exit signal (qualitative escalation vs Kiandee precursor)"
    },
    "new_bloc_after_polls": {
        "headline":"Bersatu to form new coalition/bloc after Negri polls, says Muhyiddin",
        "source":"The Star","first_captured_cycle":"170837","reconfirmed_182751":True,
        "significance":"Concrete post-exit plan, pre-nomination-day statement"
    },
    "imminent_framing": {
        "headline":"SNAPSHOT | Bersatu exit from PN imminent?","source":"Malaysiakini",
        "url":"https://www.malaysiakini.com/news/780047","first_captured_cycle":"170837",
        "significance":"Mainstream narrative entered imminent-departure framing"
    },
    "hadi_blame_shift": {
        "headline":"Hadi denies PAS made PN 'toxic', blames Bersatu instead","source":"Free Malaysia Today",
        "first_captured_cycle":"170837","reconfirmed_182751":True,
        "significance":"PAS-side blame-shifting (PAS sidelining Bersatu)"
    },
    "pas_sidelining_signal": {
        "headline":"PN rift widens as PAS sends clearest signal yet of sidelining Bersatu",
        "source":"Malaysiakini","first_captured_cycle":"170837",
        "significance":"PAS openly sidelining Bersatu"
    },
    "samsuri_entity_correction": "Prior 'Dr Samsuri Anuar' (Bersatu leader) corrected to 'Datuk Seri Dr. Ahmad Samsuri Mokhtar' (PN chairperson / Terengganu MB).",
    "watch_figures_next_cycle":["Tan Sri Muhyiddin Yassin","Datuk Seri Hamzah Zainudin",
        "Tan Sri Abdul Hadi Awang","Datuk Seri Dr. Ahmad Samsuri Mokhtar"],
    "entities": list(dict.fromkeys(pir_index["PIR-06"]["entities"] +
        ["Datuk Seri Dr. Ahmad Samsuri Mokhtar"])),
})

pir_index["PIR-09"].update({
    "mca_youth_exclusion": {
        "subject":"Saw Yee Fung (MCA Youth sec-gen)","directed_by":"Chong Sin Woon (MCA sec-gen)",
        "action":"Excluded from NS campaign (WhatsApp: 'you don't have to come') over BN-PN criticism",
        "type":"Campaign-exclusion (internal BN-component discipline, NOT candidate expulsion)",
        "first_captured_cycle":"170837","reconfirmed_182751":True
    },
    "albert_tei_rhetoric": {
        "actor":"Albert Tei (businessperson, PN supporter)","venue":"Dewan Besar Kuala Klawang (Jelebu) nomination centre",
        "action":"Labelled Harapan supporters 'barking dogs' (25-sec video, PN shirt)",
        "type":"Day-1 abrasive rhetoric — character/credibility signal on PN-side figure",
        "first_captured_cycle":"170837"
    },
    "tamim_independent_support": {
        "actor":"Tamim Dahri (activist)","context":"Surrendered at Port Dickson (FB threat case); intends to campaign for an independent",
        "type":"Independent-candidate support-network signal","first_captured_cycle":"170837"
    },
    "entities": list(dict.fromkeys(pir_index["PIR-09"]["entities"] +
        ["Albert Tei","Saw Yee Fung","Chong Sin Woon","Tamim Dahri"])),
})

pir_index["PIR-07"].update({
    "asyraf_wajdi_statement": "BN-PN understanding aimed at ensuring NS political stability (Asyraf Wajdi, NST)",
    "dap_anti_bn_revival": "DAP revives anti-BN campaign (1MDB scandal, ruler crisis) — PH-component tension with BN-PN pact (mkini)",
    "zahid_new_alignments": "New political alignments needed to ensure stability (Zahid) — jajaran politik baharu framing",
    "crystallizing_seats": ["N29 Chuah","N30 Lukut","N31 Bagan Pinang"],
    "entities": list(dict.fromkeys(pir_index["PIR-07"]["entities"] +
        ["Datuk Dr Asyraf Wajdi Dusuki"])),
})

# ---- Timestamps ----
now_utc = datetime.datetime(2026,7,18,19,2,15)
file_id = "entities_190215"

source_files_pir_relevant = list(prev["source_files_pir_relevant"]) + [
    "priority_pir06_bersatu-tidak-lagi-mahu-bersama-pn-ronald_170837.md",
    "priority_pir06_bersatu-exit-pn-imminent-snapshot_170837.md",
    "priority_pir06_bersatu-contest-own-flag_170837.md",
    "priority_pir06_goodbye-pn-muhyiddin-raps-samsuri_170837.md",
    "priority_pir09_mca-youth-stay-out-ns-polls_170837.md",
    "priority_pir09_pn-camp-albert-barking-dogs_170837.md",
    "malaysiakinicom_20260718_182751.md",
    "nstcommy_20260718_182751.md",
    "utusancommy_20260718_182751.md",
    "thestarcommy_gn_20260718_182751.md",
    "google_news_universalpnpecat_html_20260718_182751.md",
    "collection_metadata.json (182751 cycle — stability/confirmation + 170837 escalation audit)",
]

# ---- Counts ----
counts = {
    "seats_parsed": len(seat_records),
    "candidate_persons_unique": len(cand_names),
    "national_figures_and_pir_actors": len(national_figures),
    "pir06_watch_figures": len(pir06_watch_figures),
    "parties": len(parties),
    "coalitions": len(coalitions),
    "organizations": len(organizations),
    "constituencies": len(seat_records),
    "events": len(events),
    "issues_and_signals": len(issues),
    "locations": (len(locations["constituency_and_district_locations"]) +
                  len(locations["nomination_centres_and_venues"])),  # = 49; matches prior-build formula (peripheral_non_prn reported separately)
    "pir06_tier4_seats": len(PIR06_TIER4),
    "pir07_watch_seats": len(PIR07_WATCH),
    "pir09_bersatu_candidates": len(BERSATU_CAND_SEATS),
    "pir09_independents": len(INDEPENDENTS),
    "peripheral_referenced_figures": len(peripheral_figures),
}

total_unique_persons = len(set(cand_names +
    [f["name"] for f in national_figures] +
    [f["name"] for f in pir06_watch_figures] +
    [f["name"] for f in peripheral_figures]))

# ---- Assemble final document ----
out = {
    "date": "20260718",
    "collection_date": "20260718",
    "processing_timestamp_utc": now_utc.isoformat()+"+00:00",
    "processing_timestamp_myt": (now_utc+datetime.timedelta(hours=8)).isoformat()+"+08:00",
    "file_id": file_id,
    "cycle": ("nomination-day-surge + overnight confirmation (170837 escalation ingested: "
              "Muhyiddin exit hint; 182751 stability-confirmation pass, 0 new articles, 10/10 sources)"),
    "classification": "TLP:AMBER",
    "extractor": "prn_ns_entity_extraction_agent (scheduled cron)",
    "director_priority_approved": "2026-07-18 15:00 MYT",
    "source_count_total": 86,
    "source_files_pir_relevant": source_files_pir_relevant,
    "pir_priorities": {
        "PIR-06": "PN-Removal-of-Bersatu Watch (HIGHEST) — STATUS: ESCALATED (two-sided trajectory)",
        "PIR-09": "Candidate Credibility (SECOND)",
        "PIR-07": "Battleground Assessment (THIRD)",
    },
    "delta_vs_prior_build_165723": {
        "prior_build": "entities_165723.json (16:57 UTC / 00:57 MYT 19 Jul)",
        "this_build": f"{file_id}.json (19:02 UTC / 03:02 MYT 19 Jul)",
        "cycle_window_ingested": ["170837 (source-gap fill + PIR-06 ESCALATION: Muhyiddin exit hint)",
                                  "182751 (stability/confirmation pass — 0 new articles, deep-overnight MYT)"],
        "genuinely_new_findings": [
            "PIR-06 ESCALATION: Muhyiddin publicly hinting at Bersatu exit from PN ('wishing PN all the best', rapping PN chairperson Ahmad Samsuri Mokhtar) — qualitative escalation (Bersatu-leadership signal).",
            "PIR-06: Muhyiddin signals Bersatu to form new coalition/bloc AFTER Negri polls (concrete post-exit plan).",
            "PIR-06: Mainstream framing shifted to 'Bersatu exit from PN imminent?' (mkini SNAPSHOT).",
            "PIR-06: Hadi denies PAS made PN 'toxic', blames Bersatu (blame-shifting); PAS openly sidelining Bersatu (PN rift widens).",
            "PIR-06: Annuar Musa states Bersatu wants to part ways with PN (own-logo signal) — speaker-label caveat flagged.",
            "PIR-09 NEW: MCA Youth sec-gen Saw Yee Fung excluded from NS campaign over BN-PN criticism (directive by MCA sec-gen Chong Sin Woon).",
            "PIR-09 NEW: Albert Tei 'barking dogs' rhetoric at Jelebu nomination centre — PN-side abrasive Day-1 tone.",
            "PIR-09 NEW: Activist Tamim Dahri to campaign for an independent candidate (support-network signal).",
            "PIR-07 NEW: Asyraf Wajdi on BN-PN stability; DAP revives anti-BN campaign; Zahid 'new alignments'; Chuah/Lukut/Bagan Pinang crystallizing.",
        ],
        "corrections": [
            "'Dr Samsuri Anuar' (role 'Bersatu leader / Terengganu MB') corrected to 'Datuk Seri Dr. Ahmad Samsuri Mokhtar' (PN Chairperson / Terengganu MB, PAS/PN — NOT Bersatu).",
        ],
        "no_change": [
            "CRITICAL PIR-06 threshold (formal PN-MT removal notice) still NOT crossed.",
            "No Bersatu candidate withdrawals in the 8 Tier-4 seats.",
            "Candidate list (103 candidates) unchanged.",
            "Gerakan pecat of Tang Jay Son reconfirmed (no new PN-component candidate expulsion).",
            "PIR-09 N.14 Ampangan Day-1 messaging war unchanged.",
            "PIR-07 BN manifesto launch date (24 Jul) and candidate breakdown unchanged.",
        ],
    },
    "counts": counts,
    "seats": seat_records,
    "politicians": {
        "candidate_persons_unique": cand_names,
        "candidate_records_with_pir_tags": cand_person_records,
        "national_figures_and_pir_actors": national_figures,
        "pir06_watch_figures": pir06_watch_figures,
        "peripheral_referenced_figures": peripheral_figures,
        "total_unique_persons": total_unique_persons,
    },
    "parties": parties,
    "coalitions": coalitions,
    "organizations": organizations,
    "constituencies": prev["constituencies"],
    "events": events,
    "issues_and_signals": issues,
    "locations": locations,
    "pir_priority_index": pir_index,
    "peripheral": prev["peripheral"],
}

with open(os.path.join(BASE, f"{file_id}.json"), "w", encoding="utf-8") as f:
    json.dump(out, f, ensure_ascii=False, indent=2)

# ---- entity_metadata.json (update) ----
meta = {
    "date": "20260718",
    "last_updated_utc": out["processing_timestamp_utc"],
    "last_updated_myt": out["processing_timestamp_myt"],
    "classification": "TLP:AMBER",
    "extractor": "prn_ns_entity_extraction_agent (scheduled cron)",
    "latest_entities_file": f"{file_id}.json",
    "prior_entities_file": "entities_165723.json",
    "director_priority_approved": "2026-07-18 15:00 MYT",
    "cycle": "nomination-day-surge + overnight confirmation (170837 escalation + 182751 stability pass)",
    "source_count_total": 86,
    "counts": counts,
    "pir_priority_tags": {
        "PIR-06": {
            "title": "PN-Removal-of-Bersatu Watch (HIGHEST)",
            "status": ("ESCALATED WATCH — NO formal PN-MT removal notice; TWO-SIDED trajectory ACTIVE "
                "(PN-MT-may-remove-Bersatu via Kiandee AND Bersatu-may-exit-PN via Muhyiddin). "
                "Bersatu PRESIDENT now publicly hinting at exit; mainstream framing 'imminent?'."),
            "formal_removal_notice_detected": False,
            "escalation_detected": True,
            "tier4_seats": PIR06_TIER4,
            "entity_count": len(pir_index["PIR-06"]["entities"]),
            "key_entities": pir_index["PIR-06"]["entities"],
        },
        "PIR-09": {
            "title": "Candidate Credibility (SECOND)",
            "bersatu_candidate_seats": BERSATU_CAND_SEATS,
            "independents": list(INDEPENDENTS.keys()),
            "entity_count": len(pir_index["PIR-09"]["entities"]),
            "key_entities": pir_index["PIR-09"]["entities"],
        },
        "PIR-07": {
            "title": "Battleground Assessment (THIRD)",
            "watch_seats": PIR07_WATCH,
            "entity_count": len(pir_index["PIR-07"]["entities"]),
            "key_entities": pir_index["PIR-07"]["entities"],
        },
    },
    "seat_pir_tag_map": prev["constituencies"],
    "files_in_folder": [
        f"{file_id}.json (THIS run — escalation ingested, Samsuri corrected, new PIR-09 entities added)",
        "entities_165723.json (prior run 16:57 UTC — nomination-day-surge baseline w/ PIR tags)",
        "entities_consolidated.json (prior 14:00 UTC run — candidate-list baseline)",
        "entities_politicians.json / entities_parties.json / entities_constituencies.json / entities_events.json / entities_issues.json / entities_organizations.json / entities_locations.json (prior 14:00 UTC sub-sets)",
        "entity_metadata.json (this file)",
        "_build_entities.py (prior build script)",
        f"_build_entities_190215.py (this run's build script)",
    ],
    "total_entities": (counts["candidate_persons_unique"] + counts["national_figures_and_pir_actors"] +
        counts["pir06_watch_figures"] + counts["parties"] + counts["coalitions"] + counts["organizations"] +
        counts["constituencies"] + counts["events"] + counts["issues_and_signals"] + counts["locations"]),
}
with open(os.path.join(BASE, "entity_metadata.json"), "w", encoding="utf-8") as f:
    json.dump(meta, f, ensure_ascii=False, indent=2)

print("OK", file_id + ".json + entity_metadata.json written")
print("counts:", json.dumps(counts, ensure_ascii=False))
print("total_entities:", meta["total_entities"])
print("total_unique_persons:", total_unique_persons)
print("PIR-06 entities:", pir_index["PIR-06"]["entities"])
print("PIR-09 entities:", pir_index["PIR-09"]["entities"])
