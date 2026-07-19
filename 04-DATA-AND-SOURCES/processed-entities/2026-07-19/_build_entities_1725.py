#!/usr/bin/env python3
"""
PRN NS 2026 Entity Extraction — 17:25 cycle (4th carry-forward).
Builds entities-20260719-1725.json by carrying forward the 1435 run (205 entities)
and appending/updating entities from cycles 153300 (15:33) + 171500 (17:15).

Director-approved PIR set, 19 Jul 17:25 MYT cycle.
Source: 04-DATA-AND-SOURCES/raw-scrapes/20260719/ (12 cycles: 075200..171500)
"""
import json
import os
from collections import Counter

BASE = os.path.dirname(os.path.abspath(__file__))
PRIOR = os.path.join(BASE, "entities-20260719-1435.json")
OUT   = os.path.join(BASE, "entities-20260719-1725.json")

with open(PRIOR) as f:
    entities = json.load(f)

print(f"Loaded prior entities: {len(entities)}")


def find(name):
    for i, e in enumerate(entities):
        if e["entity"].lower() == name.lower():
            return i
    return -1


# ---------- CONTEXT UPDATES (cycle 153300 + 171500 corroboration) ----------

# Perikatan Nasional (#1) — add Khaled "KO Bersatu" + 5th-outlet Tok Mat + Loke "23 seats"
i = find("Perikatan Nasional")
entities[i]["context"] += (
    " | 153300+171500: Khaled Nordin (Umno VP) 'Pastikan Bersatu di NS KO habis' 4-publisher (NST+BH+Metro+FMT); "
    "Annuar manifesto bersepadu (Metro 20:22); PN-BN kongsi pentas (Utusan); Sanusi 'gelombang biru mendahului merah'; "
    "Bersatu sole opposition (Muhyiddin, The Vibes 18 Jul)."
)

# Bersatu (#3) — Khaled "KO habis" + "kacau daun" hard-news
i = find("Bersatu")
entities[i]["context"] += (
    " | 153300+171500: Khaled Nordin 'Bersatu KO habis, kacau daun, ditubuhkan nak ganti UMNO' 4-publisher (NST+BH+Metro+FMT 23:49-00:16 MYT); "
    "Bersatu 24 seats under own logo (reconfirmed); sole opposition framing (Muhyiddin The Vibes)."
)

# Muhyiddin (#17) — sole opposition corroboration
i = find("Muhyiddin Yassin")
entities[i]["context"] += (
    " | 153300: 'Bersatu now sole opposition party' (The Vibes 18 Jul gnews) — Muhyiddin self-positions Bersatu as lone credible Malay opposition."
)

# "Bersatu kacau daun" (#53) — UPGRADE: now Khaled-attributed in hard-news (FMT)
i = find("Bersatu kacau daun")
entities[i]["context"] = (
    "Director PIR-16 NEW entity. First attribution: Wan Saiful Wan Jan (Harian Metro 19 Jul 16:31 MYT) — Bersatu fragmenting Malay vote via overlapping seats. "
    "UPGRADED 171500 cycle: Khaled Nordin (Umno VP/Defence Minister) attributes 'Bersatu kacau daun' to Bersatu in hard-news 4-publisher "
    "(FMT BM 'Bersatu hanya kacau daun' + BH BM + Metro BM + NST EN 'make sure Bersatu gets knocked out', 23:49-00:16 MYT 19-20 Jul) — "
    "FIRST hard-news corroboration of this PIR-16 narrative keyword. BN-VP-level voice now amplifying the narrative. "
    "Challenges 'penyatuan undi Melayu'. Classified [PRIORITY PIR-16] not [CRITICAL] (CRITICAL trigger is 'Bersatu exit imminent?' or "
    "'Bersatu sasar bentuk kerajaan negeri' hard-news — neither crossed)."
)

# "sole opposition" (#45) — Muhyiddin The Vibes corroboration
i = find("sole opposition")
entities[i]["context"] += (
    " | 153300: corroborated by Muhyiddin 'Bersatu now sole opposition party' (The Vibes 18 Jul 08:22 GMT gnews)."
)

# "MB after PRN" (#59) — Tok Mat 5th-outlet
i = find("MB after PRN")
entities[i]["context"] += (
    " | 171500: Tok Mat 'Saya sedia letak jawatan jika ada arahan PM' (Metro BM 19:42 MYT) — 5th outlet joining NST+FMT EN+NST EN+BH+FMT BM (5-publisher total)."
)

# "resign to attack unity partners" (#67) — Khaled joins + Akmal-Nga conditional
i = find("resign to attack unity partners (Anwar discipline firewall)")
entities[i]["context"] += (
    " | 153300+171500: Khaled Nordin 'kalau orang dah tak suka, buat apa nak tunggu' + 'menteri hak mutlak PM' (Awani 23:36 + Metro 23:55) adds Khaled's voice to resign-narrative. "
    "Akmal 'I'll resign as exco if Nga quits Cabinet' (NST 23:59 MYT) — conditional escalation. Teng Chang Khim (DAP) had challenged Akmal; Ab Rauf Yusoh (Melaka CM) earlier rejected Akmal's resignation. "
    "Khaled dismisses AMK resign-call: 'dia cakap sajalah dengan Ketua Parti dia' (Awani 23:36)."
)

# "Madani reforms continuity" (#72) — BH BM 22:35 corroboration
i = find("Madani reforms continuity (Teo Nie Ching)")
entities[i]["context"] += (
    " | 153300: corroborated by BH BM 'PH perlu terus diberi mandat laksana agenda MADANI di NS - Nie Ching' (22:35 MYT, full text 2477c). Now 2-publisher (NST EN 22:07 + BH BM 22:35). "
    "Teo (Deputy Communications Minister, MP Kulai) cited Madani economic record + 10A-SPM matriculation guarantee. Day-1 evening PH dinner in Seremban (Loke + Gobind + Cha Kee Chin)."
)

# "AMH resign-call" (#68) — Hassan Karim PKR dissent + Khaled dismissal
i = find("AMH resign-call (PH Youth joint statement)")
entities[i]["context"] += (
    " | 153300+171500: Hassan Karim (PKR MP Pasir Gudang) pushes back against AMH: 'Tak pelik... PH juga selepas PRU 2008 mengatur strategi jatuhkan BN' (FMT 15:00 MYT). "
    "Khaled Nordin dismisses AMK challenge to Akmal: 'dia cakap sajalah dengan Ketua Parti dia' (Awani 23:36). Intra-PH dissent added."
)

# "Akmal counter-escalation" (#69) — NST full text + Nga resignation pledge context
i = find("Akmal counter-escalation (Umno Youth)")
entities[i]["context"] += (
    " | 153300+171500: NST full text 'Akmal: I'll resign as exco if Nga quits Cabinet' (23:59 MYT) — conditional: 'the day Nga submits his, I will submit mine.' "
    "Context: Nga allegedly pledged to resign if BN won Johor (Newswav 17 Jul + MSN 17 Jul gnews) — Akmal is calling out a pre-existing pledge, not just deflecting. "
    "Teng Chang Khim (DAP) had challenged Akmal; Ab Rauf Yusoh (Melaka CM) rejected Akmal's Jan resignation."
)

# Ab Rauf (#95) — expand context
i = find("Ab Rauf")
entities[i]["context"] = (
    "Melaka Chief Minister Datuk Seri Ab Rauf Yusoh. PIR-16: Melaka PH-BN fracture (DAP withdrawal over appointed assemblymen). "
    "153300+171500: rejected Akmal Saleh's January resignation as Melaka exco, allowing Akmal to remain — context for Akmal's conditional 'I'll resign if Nga quits' (NST 23:59 MYT)."
)

# "PH manifesto launch 20 Jul" (#102) — now 5-source + Amirudin to officiate
i = find("PH manifesto launch 20 Jul")
entities[i]["context"] = (
    "PH to launch NS PRN manifesto Mon 20 Jul evening (night). 5-source corroborated: Metro 'PH lancar manifesto malam esok' (18:00 MYT) + Malay Mail gnews "
    "'Pakatan to reveal game plan...Monday night' (20:17 MYT) + Newswav gnews 'PH urged to keep NS for Madani reforms' (22:42) + BH BM Teo 22:35 + NST EN. "
    "Officiated by Amirudin Shari (Selangor MB, PH presidential council member, PRN NS co-election director). Muhammad Zaki Md Sabri: 'Aminuddin (Tok Min) administration record is the manifesto's basis.' "
    "Held at Klana Resort, Seremban. [PRIORITY PIR-07] — major upcoming event to capture next cycle."
)

# "BN manifesto launch 24 Jul" (#103) — additional NST gnews source
i = find("BN manifesto launch 24 Jul")
entities[i]["context"] += (
    " | 153300: additional source NST Online gnews 'BN to launch NS election manifesto on July 24' (18 Jul 07:10 GMT) — now 4-source (Kosmo + The Vibes + prior intel + NST gnews). At DUN Linggi + Pertang."
)

# "gabung jentera" (#38) — Metro full text recovered (17:29 MYT cycle 171500)
i = find("gabung jentera (machinery merger)")
entities[i]["context"] += (
    " | 171500: Metro BM FULL TEXT recovered 'PRN N9: BN-PN gabung jentera, tekad rampas NS' (18:29 MYT, Hamzah Zainudin). Attendees: Takiyuddin Hassan (PN Sec-Gen), Ronald Kiandee (suspended Bersatu VP — attended despite suspension), Mazalan Maarop (Umno Seremban chief); candidates Razali Abu Samah (PN Sikamat), Mohd Asna Amin (BN Lenggeng), Dr Rafie (PN Ampangan). Hamzah deflects seat-criticism: '11 of 36 is fine, don't quarrel.'"
)

# "BN-PN joint manifesto" (#39) — Metro full text
i = find("BN-PN joint manifesto (manifesto bersepadu)")
entities[i]["context"] += (
    " | 171500: Metro BM FULL TEXT 'PRN N9: PN-BN bakal tampil manifesto bersepadu - Annuar' (20:22 MYT, KOMPAS meeting). Attendees: Samsuri (PN chair), Takiyuddin (Sec-Gen), Sanusi (election director), Wan Saiful (Wawasan VP). Annuar: PN-Jawatankuasa-Induk forms working committee; two manifestos (joint + local candidate ikrar). Sanusi: 'gelombang biru mendahului gelombang merah.'"
)

# "penyatuan undi Melayu" (#60) — Khaled "gelombang Melayu"
i = find("penyatuan undi Melayu")
entities[i]["context"] += (
    " | 171500: Khaled Nordin 'gelombang Melayu ke BN' (BH + Metro 00:13-00:56 MYT) — Johor PRN result will trigger Malay wave to BN in NS. 'Orang Melayu dah ada kesedaran mahu sokong BN.' Adds Khaled-voice to Malay-unity narrative."
)

# "Bersatu exit from PN imminent?" (#42) — confirm NOT crossed (12th cycle)
i = find("Bersatu exit from PN imminent?")
entities[i]["context"] += (
    " | 153300+171500: gnews 'bersatu exit pn'=0 + 'sasar kerajaan negeri'=0 (12th consecutive cycle). No hard-news corroboration. mkini SNAPSHOT (18 Jul 18:00) remains lone viral-tier item. [CRITICAL] threshold NOT CROSSED — classified [PRIORITY] only."
)

# "sasar bentuk kerajaan negeri" (#44) — confirm PH/Loke version ≠ Bersatu CRITICAL trigger
i = find("sasar bentuk kerajaan negeri (Bersatu solo governing bid)")
entities[i]["context"] += (
    " | 171500: NOTE — Loke 'PH sasar menang 23 kerusi untuk bentuk kerajaan negeri lebih stabil' (NST+FMT+BH+Metro) contains the phrase 'sasar bentuk kerajaan negeri' BUT is PH/Loke-attributed (23-seat safe-majority target), NOT Bersatu. The Director [CRITICAL] trigger is specifically the Bersatu-attributed 'Bersatu sasar bentuk kerajaan negeri' (24 seats solo) — that Bersatu version was corroborated prior 091800 (MalaysiaGazette + Sinar 19 Jul 15:37-15:53) and remains [CRITICAL]. The PH/Loke version is a different framing, classified [PRIORITY PIR-16]."
)

# "fleeing Sikamat" (#204) — unchanged but note Aminuddin Linggi move context
i = find("fleeing Sikamat (Aminuddin move)")
entities[i]["context"] += (
    " | 171500: Aminuddin 'lebih selesa berkempen dalam kumpulan kecil' at Linggi (Metro 16:47) — acknowledges caretaker MB status gives no advantage; Linggi traditionally BN stronghold; meets voters 2-3 at a time."
)

# Chennah demographics (#196) — Loke transport-minister advantage
i = find("Chennah demographics risk (Loke LOSES if PRU15 repeats)")
entities[i]["context"] += (
    " | 171500: Loke rebuts 'neglected Chennah' charge — as transport minister he channelled MORE benefits (Kampung Madani projects); full-time team manages constituency. NST+BH+Metro."
)


# ---------- NEW ENTITIES (from cycles 153300 + 171500) ----------

new_entities = [
    # --- PIR-06 ---
    {
        "entity": "Mohamed Khaled Nordin",
        "type": "person",
        "pir_tag": "PIR-06",
        "priority": "priority",
        "source_url": "https://www.nst.com.my/news/regional/2026/07/1492742/negri-sembilan-polls-make-sure-bersatu-gets-knocked-out-khaled-tells",
        "context": "Umno Vice-President / Defence Minister / MP Kota Tinggi. NEW dominant voice this cycle (4-publisher NST+EN + BH+BM + Metro+BM + FMT+BM, 23:49-00:16 MYT 19-20 Jul). Anti-Bersatu electoral-elimination: 'Pastikan Bersatu di Negeri Sembilan KO habis-habis' / 'Make sure Bersatu gets knocked out completely' — urges voters to ensure Bersatu wins ZERO seats so it has 'no basis to contest future PRU'. Frames Bersatu as 'ditubuhkan nak ganti UMNO' and 'kacau daun'. Pro BN-PN: 'persefahaman BN-PN beri kelebihan vs Johor'; 'gelombang Melayu ke BN'. On Tok Mat resignation: 'menteri hak mutlak PM... kalau orang dah tak suka, buat apa nak tunggu'. Dismisses AMK resign-call: 'dia cakap sajalah dengan Ketua Parti dia'. Spoke at Majlis Pengenalan Calon & Pelancaran Jentera BN DUN Johol. [PRIORITY PIR-06] — rhetorical escalation, NOT formal PN-MT action."
    },
    {
        "entity": "Hassan Karim",
        "type": "person",
        "pir_tag": "PIR-06",
        "priority": "normal",
        "source_url": "https://www.freemalaysiatoday.com/category/bahasa/tempatan/2026/07/19/tak-pelik-pemimpin-pkr-beritahu-ph-jangan-merungut-kerjasama-bn-pn",
        "context": "PKR MP Pasir Gudang. NEW intra-PH dissent voice (FMT BM 15:00 MYT, full text 3287c). Says BN-PN cooperation is 'normal' in Malaysian politics; PH shouldn't complain. Recalls PH's own post-PRU2008 strategy (under Anwar) to topple the BN govt that had the people's mandate: 'Saya dah tua, saya menyaksikan itu semua walaupun saya seorang Ahli Parlimen PKR yang setia.' 'Hampir semua parti politik di Malaysia ada rekod mengkhianati antara satu sama lain.' Pushes back against AMH (PH Youth) resign-demand — counter-perspective within PH coalition (PKR old guard vs PH Youth). Adds nuance to resign-narrative."
    },
    {
        "entity": "Bersatu KO habis (electoral-elimination call)",
        "type": "narrative",
        "pir_tag": "PIR-06",
        "priority": "priority",
        "source_url": "https://www.bharian.com.my/berita/nasional/2026/07/1590574/pastikan-bersatu-di-negeri-sembilan-ko-habis-khaled-nordin",
        "context": "NEW narrative entity (Khaled Nordin, 4-publisher NST+EN + BH+BM + Metro+BM + FMT+BM, 23:49-00:16 MYT 19-20 Jul). 'Pastikan BERSATU di Negeri Sembilan KO habis' / 'Make sure Bersatu gets knocked out completely.' Urges voters to reject Bersatu outright so all 24 Bersatu candidates lose deposits — paving way for BN straight fights in next PRU and strengthening BN's federal-power bid. Bersatu 'ditubuhkan nak ganti UMNO.' Director PIR-06 keywords 'keluar'/'pecat'/'tarik diri' are about coalition membership actions; this is electoral-elimination rhetoric by a BN (not PN) leader — adjacent but NOT a formal PN-MT expulsion/withdrawal signal. Classified [PRIORITY PIR-06] not [CRITICAL]."
    },
    {
        "entity": "gelombang Melayu ke BN (Malay wave to BN)",
        "type": "narrative",
        "pir_tag": "PIR-06",
        "priority": "priority",
        "source_url": "https://www.bharian.com.my/berita/nasional/2026/07/1590578/persefahaman-bn-pn-di-negeri-sembilan-beri-kelebihan-khaled-nordin",
        "context": "NEW narrative entity (Khaled Nordin, BH+BM + Metro+BM 00:13-00:56 MYT 20 Jul). Johor PRN result will trigger 'gelombang Melayu' supporting BN in NS. 'Gelombang Melayu ke BN itu bukan sesuatu yang hanya akan berlaku di Johor... itulah perasaan orang-orang Melayu pada hari ini yang hendak kembali ke BN.' Challenges BN machinery to convert sentiment into votes. Pairs with 'persefahaman BN-PN beri kelebihan' (BN-PN understanding gives advantage vs Johor's multi-corner fight)."
    },
    {
        "entity": "PN kongsi pentas dengan BN (joint ceramah)",
        "type": "narrative",
        "pir_tag": "PIR-06",
        "priority": "normal",
        "source_url": "https://www.utusan.com.my/nasional/2026/07/pn-benarkan-pimpinan-kongsi-pentas-dengan-bn/",
        "context": "NEW cooperation-hardening signal (Utusan 12:13 MYT, headline only — RSS lacked content:encoded). 'PN benarkan pimpinan kongsi pentas dengan BN' — PN permits its leadership to share the stage with BN. Joint-ceramah confirmation. 3rd stage of BN-PN cooperation formalization trajectory: (1) seat-swap, (2) machinery merger (gabung jentera, 18:29 MYT), (3) joint manifesto (manifesto bersepadu, 20:22 MYT), (4) joint ceramah (this). Watch whether 24 Jul BN manifesto launch becomes a JOINT BN-PN event."
    },
    {
        "entity": "Khaled dismisses AMK resign-call",
        "type": "narrative",
        "pir_tag": "PIR-06",
        "priority": "priority",
        "source_url": "https://www.astroawani.com/berita-politik/prn-negeri-sembilan-kalau-orang-dah-tak-suka-buat-apa-nak-tunggu-khaled-nordin",
        "context": "NEW friction entity (Khaled Nordin, Awani 23:36 MYT, full text 2863c). Khaled dismisses AMK (Angkatan Muda Keadilan/PKR Youth) challenge to Akmal to make Umno ministers resign: 'Tak payahlah dia nak suruh mana-mana Menteri untuk lakukan letak jawatan... dia cakap sajalah dengan Ketua Parti dia.' Adds BN-VP voice counter to PH-Youth resign-demand. Reinforces 'menteri hak mutlak PM' framing. New Khaled-vs-AMK/AMH friction axis."
    },

    # --- PIR-16 ---
    {
        "entity": "campaign on policies not personal attacks (Loke)",
        "type": "narrative",
        "pir_tag": "PIR-16",
        "priority": "priority",
        "source_url": "https://www.nst.com.my/news/regional/2026/07/1492756/negri-sembilan-polls-campaign-policies-not-personal-attacks-says-loke",
        "context": "NEW PIR-16 narrative (Loke, 3-publisher NST+EN + BH+BM + Metro+BM, 23:51-00:06 MYT 19-20 Jul). Loke backs PM Anwar's clean-campaign call: 'kempen patut tumpu tawaran, bukan serang peribadi.' Takes position NOT to attack any Cabinet minister throughout NS PRN because 'they are my colleagues... we meet every week at Cabinet.' Counter to 'derhaka'/personal-attack narrative. Translates to NOT campaigning in Rantau (Tok Mat's seat) to preserve unity-govt harmony; focuses on Chennah + DAP seats + helps Aminuddin in Linggi."
    },
    {
        "entity": "Loke not campaigning in Rantau (unity-govt harmony)",
        "type": "narrative",
        "pir_tag": "PIR-16",
        "priority": "priority",
        "source_url": "https://www.nst.com.my/news/regional/2026/07/1492756/negri-sembilan-polls-campaign-policies-not-personal-attacks-says-loke",
        "context": "NEW PIR-16/PIR-07 narrative (Loke, 3-publisher NST+BH+Metro, 23:51-00:06 MYT). Loke explicitly chose NOT to campaign in Rantau (contested by BN deputy chair / Foreign Minister Mohamad Hasan) to 'menjaga keharmonian dalam Kerjaan Perpaduan.' Instead focuses on Chennah (his seat), DAP-contested seats, and helps Aminuddin in Linggi. Notable intra-unity-govt restraint signal — a PH leader voluntarily ceding a battleground to a BN partner. Director PIR-16 'MCA biggest loser'/'Wee rebuttal' watch adjacent."
    },
    {
        "entity": "PH sasar 23 kerusi (safe majority / 8123)",
        "type": "narrative",
        "pir_tag": "PIR-16",
        "priority": "priority",
        "source_url": "https://www.freemalaysiatoday.com/category/nation/2026/07/20/ph-targets-23-seats-for-safe-majority-in-negeri-sembilan-says-loke",
        "context": "NEW dominant PIR-16/PIR-07 narrative (Loke, 5-publisher NST+EN + FMT+EN + FMT+BM + BH+BM + Metro+BM, 16:01-00:21 MYT 19-20 Jul). PH targets 23 of 36 seats for 'safe' majority / stable govt. Math: current 17 (insufficient); 18 = tie; 19 = simple majority but 'apa sahaja boleh berlaku'; 23 = safe. Backdrop '8123' code = Aug 1 polling, target 23 seats. Frames 2026 crisis: 14 Umno ADUN withdrew support for MB Aminuddin + 5 PN attempted backdoor govt. Defends Aminuddin: 'done nothing wrong, friendly, not arrogant, not corrupt, no millions in bank.' Director 'majoriti mudah' adjacent — Loke implicitly says 19 'majoriti mudah' is NOT enough."
    },
    {
        "entity": "MCA told her to stay home (Saw Yee Fung vs Chong Sin Woon)",
        "type": "narrative",
        "pir_tag": "PIR-16",
        "priority": "priority",
        "source_url": "https://www.therakyatpost.com/news/malaysia/2026/07/19/she-asked-about-mcas-deal-with-pass-coalition-mca-told-her-to-stay-home/",
        "context": "NEW PIR-16 intra-MCA friction narrative (TRP, 2 articles 17-19 Jul). MCA Youth sec-gen Saw Yee Fung publicly questioned BN-PAS cooperation in NS, contradicting what she told Johor voters ('we are not cooperating with PAS'). No central committee response to her WhatsApp. MCA sec-gen Chong Sin Woon privately replied '对，森州州选妳不需要来。谢谢' (yes, NS state election — you don't need to come, thank you) at 4:58 PM; Saw screenshot and posted publicly (9,100 likes). Chong later clarified it was the party's decision in line with BN's electoral arrangement. FIRST concrete MCA-leader pushback against BN-PN/PAS. Director PIR-16 'Wee rebuttal'/'MCA biggest loser' adjacent — top leadership (Wee/Mah) still silent. Viral-content amplifier = [PRIORITY] per Director rule."
    },
    {
        "entity": "Teng Chang Khim",
        "type": "person",
        "pir_tag": "PIR-16",
        "priority": "normal",
        "source_url": "https://www.nst.com.my/news/nation/2026/07/1492751/akmal-ill-resign-exco-if-nga-quits-cabinet",
        "context": "DAP leader (Selangor Speaker / Selangor senior exco). NEW — challenged Akmal Saleh to follow through on his earlier resignation pledge (NST 23:59 MYT, via FMT). Triggered Akmal's conditional 'I'll resign as exco if Nga quits Cabinet' counter."
    },
    {
        "entity": "Nga resignation pledge (Johor precondition)",
        "type": "narrative",
        "pir_tag": "PIR-16",
        "priority": "priority",
        "source_url": "https://news.google.com/rss/search?q=Nga+resign+Akmal+when:3d&hl=en-MY&gl=MY&ceid=MY:en",
        "context": "NEW context for Akmal-Nga resign-narrative (gnews 17 Jul: Newswav 'Akmal Challenges Nga to Honour Resignation Pledge' + MSN 'Nga Kor Ming urged to honour resignation pledge after BN's Johor landslide victory'). Nga Kor Ming allegedly pledged to resign if BN won Johor — the pledge predates NS PRN. Akmal's 'Nga resign too' counter is calling out this pre-existing pledge, not just deflecting. A DAP leader says Nga's remarks were misinterpreted. Enriches the resign-narrative chain (AMH demand -> Anwar warning -> Tok Mat ready -> Akmal conditional -> Hassan Karim PKR dissent -> Nga pledge context)."
    },
    {
        "entity": "Tuanku Muhriz Tuanku Munawir",
        "type": "person",
        "pir_tag": "PIR-16",
        "priority": "normal",
        "source_url": "https://www.freemalaysiatoday.com/category/nation/2026/07/20/ph-targets-23-seats-for-safe-majority-in-negeri-sembilan-says-loke",
        "context": "Yang di-Pertuan Besar Negeri Sembilan. NEW context (Loke speech, NST+FMT 16:03 MYT). April 19 royal/political crisis: the state's four undangs (chieftains) claimed Tuanku Muhriz had been removed as Yang di-Pertuan Besar — sparking the royal and political crisis that led to 14 Umno ADUN withdrawing support for MB Aminuddin and the NS PRN. Background context for why the election is happening."
    },
    {
        "entity": "April 19 royal crisis (4 undangs claim Tuanku Muhriz removed)",
        "type": "narrative",
        "pir_tag": "PIR-16",
        "priority": "priority",
        "source_url": "https://www.freemalaysiatoday.com/category/nation/2026/07/20/ph-targets-23-seats-for-safe-majority-in-negeri-sembilan-says-loke",
        "context": "NEW PIR-16/PIR-07 narrative (Loke speech, NST+FMT 16:03 MYT). April 19 2026: NS's four undangs (traditional Malay chieftains) claimed Tuanku Muhriz Tuanku Munawir had been removed as Yang di-Pertuan Besar — sparking a royal and political crisis. Resulted in all 14 Umno ADUN withdrawing support for MB Aminuddin Harun (citing his handling of the royal dispute) + 5 PN ADUN attempting to form a 'backdoor government.' This is the trigger for the Aug 1 NS PRN. Loke uses this as the justification for PH's 'safe majority 23' target ('we did not want this election, but look what they did'). [PRIORITY] — central to understanding the election's origin."
    },
    {
        "entity": "14 Umno ADUN withdrew support + 5 PN backdoor attempt",
        "type": "narrative",
        "pir_tag": "PIR-16",
        "priority": "priority",
        "source_url": "https://www.freemalaysiatoday.com/category/nation/2026/07/20/ph-targets-23-seats-for-safe-majority-in-negeri-sembilan-says-loke",
        "context": "NEW PIR-16/PIR-07 narrative (Loke speech, NST+FMT 16:03 MYT). 'Fourteen Umno assemblymen withdrew their support (for the menteri besar) and joined forces with five PN assemblymen to attempt to form a backdoor government.' This is the political-crisis framing PH uses to justify seeking a fresh/stable mandate. Note: some of these 14 Umno ADUN are now BN candidates in this PRN — the 'backdoor' attempt collapsed, leading to the dissolution and this election. [PRIORITY] — core PH campaign narrative."
    },

    # --- PIR-07 ---
    {
        "entity": "N.19 Johol",
        "type": "seat",
        "pir_tag": "PIR-07",
        "priority": "normal",
        "source_url": "https://www.astroawani.com/berita-politik/prn-negeri-sembilan-kalau-orang-dah-tak-suka-buat-apa-nak-tunggu-khaled-nordin",
        "context": "NEW PIR-07 seat (DUN Johol, N.19). Site of Khaled Nordin's BN machinery launch (Majlis Pengenalan Calon & Pelancaran Jentera BN DUN Johol, 19 Jul). Straight fight: Saiful Yazan Sulaiman (BN incumbent, Datuk) vs Mohd Zailan Mohd Munawar (PH). Khaled: Johol is Malay-majority; 'gelombang Melayu' sentiment is felt here. Index.md notes Johol as a T1 seat."
    },
    {
        "entity": "Saiful Yazan Sulaiman",
        "type": "person",
        "pir_tag": "PIR-07",
        "priority": "normal",
        "source_url": "https://www.bharian.com.my/berita/nasional/2026/07/1590578/persefahaman-bn-pn-di-negeri-sembilan-beri-kelebihan-khaled-nordin",
        "context": "NEW PIR-07 person. BN incumbent candidate for DUN Johol (N.19), Datuk. Introduced by Khaled Nordin at BN machinery launch. Khaled frames him as the beneficiary of 'tak nak UMDAP' Malay sentiment — voters who dislike PH (which contains DAP) will choose Saiful."
    },
    {
        "entity": "Mohd Zailan Mohd Munawar",
        "type": "person",
        "pir_tag": "PIR-07",
        "priority": "normal",
        "source_url": "https://www.bharian.com.my/berita/nasional/2026/07/1590578/persefahaman-bn-pn-di-negeri-sembilan-beri-kelebihan-khaled-nordin",
        "context": "NEW PIR-07 person. PH candidate for DUN Johol (N.19). Straight fight vs BN incumbent Saiful Yazan Sulaiman."
    },
    {
        "entity": "Aminuddin small-group campaign style (caretaker no advantage)",
        "type": "narrative",
        "pir_tag": "PIR-07",
        "priority": "priority",
        "source_url": "https://www.hmetro.com.my/mutakhir/2026/07/1386583/prn-n9-aminuddin-lebih-selesa-berkempen-dalam-kumpulan-kecil",
        "context": "NEW PIR-07 narrative (Aminuddin Harun, Metro 16:47 MYT, full text 2624c). MB/caretaker Aminuddin prefers small-group campaigning (2-3 people at a time) at Linggi — 'sejak 2008 saya berkempen macam ini... yang penting saya dapat jumpa orang.' Explicitly states caretaker MB status gives NO advantage: 'MB pun sekarang dah dipanggil caretaker saja... saya tidak boleh buat apa-apa keputusan... saya lalui kempen ini macam biasa sebagai calon saja.' Acknowledges Linggi is traditionally a BN stronghold; village terrain harder than urban. Met Indian voters at Pekan Pasir Panjang, Port Dickson — 'terharu' with Indian community reception, positive sign for PH. [PRIORITY] — Director 'fleeing Sikamat' adjacent (Aminuddin moved MB seat from Sikamat to Linggi)."
    },
    {
        "entity": "Aminuddin honest-not-corrupt defense (Loke)",
        "type": "narrative",
        "pir_tag": "PIR-07",
        "priority": "priority",
        "source_url": "https://www.nst.com.my/news/regional/2026/07/1492754/negri-sembilan-polls-ph-targets-23-seats-form-stable-govt-says-loke",
        "context": "NEW PIR-07 narrative (Loke speech, NST+FMT 16:03 MYT). Loke defends MB Aminuddin Harun as the PH MB-retention candidate: 'He has done nothing wrong. He is not corrupt, he has not abused his position and he has always been a humble leader who is willing to work with everyone.' 'PH is an inclusive government — represents all races: Malays, Chinese, Indians.' Frames PH as seeking fresh mandate to retain Aminuddin as MB. Counter to BN-PN 'stability/Malay-unity' narrative — PH's pitch is incumbent-performance continuity + inclusive governance."
    },
    {
        "entity": "Loke transport-minister advantage for Chennah",
        "type": "narrative",
        "pir_tag": "PIR-07",
        "priority": "normal",
        "source_url": "https://www.nst.com.my/news/regional/2026/07/1492756/negri-sembilan-polls-campaign-policies-not-personal-attacks-says-loke",
        "context": "NEW PIR-07 narrative (Loke, NST+BH+Metro). Loke rebuts 'neglected Chennah' charge: as transport minister he channelled MORE benefits to Chennah, including Kampung Madani project allocations. 'Highly dedicated full-time team' manages the constituency. Frames ministerial status as a Chennah advantage, not a distraction. Counter to Director 'Chennah demographics risk' (Loke LOSES if PRU15 repeats) — Loke's rebuttal."
    },
]

# Deduplicate against existing entities (by exact name match, case-insensitive)
added = 0
for ne in new_entities:
    if find(ne["entity"]) == -1:
        entities.append(ne)
        added += 1
    else:
        print(f"  SKIP (already exists): {ne['entity']}")

print(f"New entities added: {added}")
print(f"Total entities: {len(entities)}")

# ---------- WRITE ----------
with open(OUT, "w") as f:
    json.dump(entities, f, ensure_ascii=False, indent=2)
print(f"Wrote: {OUT}")

# ---------- STATS ----------
print("\n=== STATS ===")
print("By PIR:", dict(Counter(d["pir_tag"] for d in entities)))
print("By priority:", dict(Counter(d["priority"] for d in entities)))
print("By type:", dict(Counter(d["type"] for d in entities)))
