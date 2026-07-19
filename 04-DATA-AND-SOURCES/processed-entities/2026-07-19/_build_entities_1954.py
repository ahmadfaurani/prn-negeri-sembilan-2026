#!/usr/bin/env python3
"""
PRN Negeri Sembilan 2026 — Entity Extraction Agent
Cycle 20260719_182000 (02:20 MYT 20 Jul, Campaign Day 2 dawn window)
Builds cumulative entities JSON from prior 1725 run (226 entities) + 182000 cycle new content.

182000 cycle fetch (per _priority_fetch_results_20260719_182000.json + index.md 182000 section):
  5 files (4 full-text RSS + 1 gnews headline-intel duplicate). 1 genuinely-fresh post-cutoff:
   - BH BM "Kalau orang dah tak suka, buat apa nak tunggu - Khaled Nordin" (23:45:19 MYT, FRESH, 1698c)
   - NST EN "PM alone decides ministers' fate, says Khaled" (23:44 MYT, 1450c)
   - FMT BM "Tak payah desak, kuasa PM tentu jawatan menteri, kata Khaled" (16:04 MYT, 1872c)
   - FMT BM "PH sasar menang 23 kerusi untuk 'selamat' di N Sembilan, kata Loke" (16:01 MYT, 3550c)
   - gnews NST "PM alone decides ministers' fate" (headline-intel duplicate of NST RSS)

All 8 mandatory PIR-06 [CRITICAL]-watch gnews queries returned 0. PIR-06 [CRITICAL] MAINTAINED
(Kiandee quorum, prior 075200). No new threshold crossing (13th cycle). PIR-16 NOT [CRITICAL].
PIR-07 no new content.

The 1725 run already captured the Khaled Johol content (Awani BM 23:36) + Loke 23-seats (5-publisher).
The 182000 cycle adds 3 more outlet/language versions → 4-outlet corroboration of Khaled's
"PM hak mutlak / kalau orang dah tak suka" Johol statement + 5th outlet (FMT BM) for Loke 23-seats.
This is a QUIET corroboration cycle; 2 genuinely new narrative entities + 7 context updates.
"""
import json, copy, os

BASE = '04-DATA-AND-SOURCES/processed-entities/2026-07-19'
PRIOR = os.path.join(BASE, 'entities-20260719-1725.json')
OUT = os.path.join(BASE, 'entities-20260719-1954.json')

prior = json.load(open(PRIOR))
ents = copy.deepcopy(prior)
print(f'Loaded prior: {len(ents)} entities')

# --- Source URLs for the 182000 cycle new content ---
URL_NST_KHALED = 'https://www.nst.com.my/news/nation/2026/07/1492740/pm-alone-decides-ministers-fate-says-khaled'
URL_BH_KHALED = 'https://www.bharian.com.my/berita/nasional/2026/07/1590568/kalau-orang-dah-tak-suka-buat-apa-nak-tunggu-khaled-nordin'
URL_FMT_KHALED = 'https://www.freemalaysiatoday.com/category/bahasa/tempatan/2026/07/20/tak-payah-desak-kuasa-pm-tentu-jawatan-kata-khaled'
URL_FMT_LOKE = 'https://www.freemalaysiatoday.com/category/bahasa/tempatan/2026/07/20/ph-sasar-menang-23-kerusi-di-n-sembilan-bentuk-kerajaan-negeri-lebih-stabil'

# ============================================================
# NEW ENTITIES (2) — genuinely new analytical angles from 182000 full-text recovery
# ============================================================

new_entities = [
    {
        "entity": "PM discretion on minister appointments (hak mutlak PM / budi bicara PM)",
        "type": "narrative",
        "pir_tag": "PIR-06",
        "priority": "priority",
        "source_url": URL_NST_KHALED,
        "context": ("NEW PIR-06 narrative (Khaled Nordin, Umno VP/Defence Minister, 182000 cycle full-text recovery, "
                    "now 4-outlet: Awani BM 23:36 + NST EN 23:44 + BH BM 23:45 + FMT BM 16:04 MYT 19-20 Jul). "
                    "At Majlis Pengenalan Calon & Pelancaran Jentera BN DUN Johol. 'PM alone decides ministers' fate' / "
                    "'urusan lantikan serta kedudukan seorang menteri... hak mutlak Perdana Menteri' / 'budi bicara PM' / "
                    "'kalau orang dah tak suka, buat apa nak tunggu' (if people don't want you, why wait — implicit jab at Tok Mat resign-ready). "
                    "BN counter-line to AMH resign-call + Tok Mat 'ready to resign' + Anwarn 'resign to attack unity partners' warning. "
                    "Khaled: 'tak payahlah (Pemuda PH) nak suruh mana-mana menteri (letak jawatan)... dia cakaplah dengan ketua parti dia.' "
                    "Classified [PRIORITY] — rhetorical reinforcement of 'PM discretion' line, NOT [CRITICAL] (not a formal PN-MT expulsion/withdrawal/quorum signal).")
    },
    {
        "entity": "bipartisan clean-campaign convergence (state-development focus)",
        "type": "narrative",
        "pir_tag": "PIR-16",
        "priority": "priority",
        "source_url": URL_BH_KHALED,
        "context": ("NEW PIR-16 narrative (182000 cycle). Khaled Nordin (BN/Umno VP) adds BN VOICE to the clean-campaign call — "
                    "'PRN NS seharusnya memberi tumpuan kepada isu berkaitan pembangunan negeri dan bukannya dijadikan medan serangan antara parti' / "
                    "'tak perlu guna pendekatan yang boleh menyakitkan hati ataupun saling memburuk-burukkan' (NST EN + BH BM + FMT BM, 23:44-23:45/16:04 MYT). "
                    "References Zahid (Umno president/BN chairman): 'Seperti ditekankan Presiden UMNO... kempen perlu dijalankan secara berhemah.' "
                    "Clean-campaign / state-development-focus call is now BIPARTISAN: Loke (PH, 3-publisher NST+BH+Metro) + Anwar (PM, NST 14:47) + "
                    "Khaled (BN) + Zahid (BN). Converges with Loke 'campaign on policies not personal attacks' [211] and counters the "
                    "'derhaka'/personal-attack + resign-narrative friction. [PRIORITY PIR-16] — multi-leader convergence signal.")
    },
]

# ============================================================
# CONTEXT UPDATES (7) — append 182000 corroboration notes to existing entities
# ============================================================

updates = {
    "Mohamed Khaled Nordin": (
        " | 182000 UPDATE: 'PM hak mutlak / kalau orang dah tak suka' Johol machinery-launch statement now 4-outlet corroborated "
        "(Awani BM 23:36 + NST EN 23:44 + BH BM 23:45 + FMT BM 16:04); reinforces 'PM discretion' counter-line to AMH resign-call + Tok Mat resign-ready; "
        "adds BN voice to clean-campaign/state-development-focus call (references Zahid 'berhemah')."
    ),
    "Khaled dismisses AMK resign-call": (
        " | 182000 UPDATE: now 4-outlet (Awani BM 23:36 + NST EN 'PM alone decides ministers' fate' 23:44 + BH BM 23:45 + FMT BM 16:04). "
        "Full-text recovery confirms 'PM's absolute right/discretion' framing: 'tak payahlah (Pemuda PH) nak suruh mana-mana menteri letak jawatan... dia cakaplah dengan ketua parti dia.'"
    ),
    "campaign on policies not personal attacks (Loke)": (
        " | 182000 UPDATE: clean-campaign call now BIPARTISAN — Khaled (BN/Umno VP) echoes 'tumpu isu pembangunan negeri, bukan serang peribadi' + "
        "references Zahid 'berhemah' (NST EN + BH BM + FMT BM, 23:44-23:45/16:04 MYT). Now spans Loke (PH) + Anwar (PM) + Khaled (BN) + Zahid (BN)."
    ),
    "Ahmad Zahid Hamidi (Zahid)": (
        " | 182000 UPDATE: 'kempen berhemah' (prudent campaign) emphasis referenced by Khaled Nordin at Johol BN machinery launch "
        "(NST EN + BH BM + FMT BM, 23:44-23:45/16:04 MYT) — 'Seperti ditekankan Presiden UMNO yang juga Pengerusi BN, kempen perlu dijalankan secara berhemah.'"
    ),
    "PH sasar 23 kerusi (safe majority / 8123)": (
        " | 182000 UPDATE: FMT BM 5th-outlet version recovered — 'PH sasar menang 23 kerusi untuk selamat di N Sembilan, kata Loke' (16:01 MYT, 3550c). "
        "Confirms 5-publisher corroboration (NST EN + FMT EN + FMT BM + BH BM + Metro BM). Math reconfirmed: 17 (current) insufficient, 18=tie, 19=simple 'apa sahaja boleh berlaku', 23=safe."
    ),
    "N.19 Johol": (
        " | 182000 UPDATE: Khaled's BN machinery launch at Johol now 4-outlet corroborated (Awani BM + NST EN + BH BM + FMT BM, 23:36-23:45/16:04 MYT). "
        "Saiful Yazan Sulaiman (BN incumbent) introduction confirmed across 4 outlets."
    ),
    "Saiful Yazan Sulaiman": (
        " | 182000 UPDATE: introduction at BN Johol machinery launch corroborated NST EN + BH BM + FMT BM (23:44-23:45/16:04 MYT). "
        "NST EN: 'launching the Barisan Nasional (BN) Johol election machinery and introducing candidate Datuk Saiful Yazan Sulaiman.'"
    ),
}

applied_updates = 0
for e in ents:
    if e['entity'] in updates:
        e['context'] = e['context'] + updates[e['entity']]
        applied_updates += 1

print(f'Context updates applied: {applied_updates} / {len(updates)} expected')

# Append new entities
ents.extend(new_entities)
print(f'New entities added: {len(new_entities)}')
print(f'TOTAL entities: {len(ents)}')

# Priority/PIR counts
from collections import Counter
print('Priority:', Counter(e['priority'] for e in ents))
print('PIR:', Counter(e['pir_tag'] for e in ents))

# Write output
json.dump(ents, open(OUT, 'w'), ensure_ascii=False, indent=2)
print(f'WROTE: {OUT} ({os.path.getsize(OUT)} bytes)')
