#!/usr/bin/env python3
"""Build revision-20 sentiment analysis from rev19 baseline + 0734 entity delta."""
import json
import os

PRIOR_FILE = "/home/p62operator/.openclaw/workspace-ns/04-DATA-AND-SOURCES/sentiment-analysis/2026-07-20/sentiment-20260720-1455.json"
NEW_ENTITIES_FILE = "/home/p62operator/.openclaw/workspace-ns/04-DATA-AND-SOURCES/processed-entities/2026-07-20/entities-20260720-0734.json"
OUTPUT_FILE = "/home/p62operator/.openclaw/workspace-ns/04-DATA-AND-SOURCES/sentiment-analysis/2026-07-20/sentiment-20260720-1724.json"

with open(PRIOR_FILE, "r", encoding="utf-8") as f:
    prior = json.load(f)

with open(NEW_ENTITIES_FILE, "r", encoding="utf-8") as f:
    new_entities = json.load(f)

# Build a lookup of prior entities by name (normalized)
prior_lookup = {}
for e in prior["entities"]:
    prior_lookup[e["entity"].lower().strip()] = e

# --- SCORE UPDATES (rev19 -> rev20) based on 0734 build ---
# Format: entity_name_lower -> (new_score, trend, alert, source_count_delta, rationale)
updates = {
    # PIR-06 — Coalition Operational Arrangement
    "muhyiddin yassin": (-0.95, "declining", "critical", 1,
        "rev19 -0.93 -> rev20 -0.95. 0734 build: Marzuki (ex-Muhyiddin confidential secretary) COUNTER-ATTACKS Hamzah — reveals Hamzah LED movement to topple Muhyiddin as PN chairman/Bersatu president after Muhyiddin resigned as PM, with PAS support. 'Dari saat itulah bermulanya PN menjadi toksik.' Historical root of Bersatu-PN conflict exposed. Bersatu sharp-negative internal-fracture signal CONFIRMED and PUBLICLY ESCALATED. 24 solo Bersatu-logo candidates STABLE — no withdrawals. [CRITICAL]."),
    "bersatu (parti pribumi bersatu malaysia)": (-0.92, "declining", "critical", 1,
        "rev19 -0.89 -> rev20 -0.92. 0734 build: 'Bersatu kian tidak relevan, hadapi krisis identiti' Sinar opinion piece (dedicated analysis) — 'Bersatu in disarray' signal gaining hard-news traction. Marzuki 'PN became toxic from that moment' (Hamzah-led anti-Muhyiddin movement). Khaled 'kacau daun' + 'KO habis' hard-news bilingual. Bersatu sharp-negative internal-fracture signal CONFIRMED -> [CRITICAL]."),
    "bersatu-pn fracture (3-sided)": (-0.92, "declining", "critical", 1,
        "rev19 -0.90 -> rev20 -0.92. 0734 build: Three-sided fracture DEEPENS — Marzuki exposes Hamzah LED anti-Muhyiddin movement (historical root). Bersatu vs PAS/Wawasan vs PN-MT, plus BN-VP anti-Bersatu (Khaled). Gerakan-Bersatu Rahang candidate-lending dispute (intra-PN component friction). 103-calon confirms stable seat allocation. [CRITICAL]."),
    "toxic pn (muhyiddin framing)": (-0.85, "declining", "critical", 2,
        "rev19 -0.80 -> rev20 -0.85. 0734 build: ESCALATED — Marzuki counter-attacks Hamzah: reveals Hamzah LED movement to topple Muhyiddin as PN chairman/Bersatu president. 'Dari saat itulah bermulanya PN menjadi toksik.' Narrative volley active (Hamzah midday 'don't call PAS toxic' <-> Marzuki midafternoon 'Hamzah led anti-Muhyiddin movement'). PN-MT expulsion STILL NOT issued. [CRITICAL] per director 'toxic PN' rule."),
    "hamzah zainudin": (-0.15, "declining", "priority", 2,
        "rev19 -0.05 -> rev20 -0.15 (declining). 0734 build: COUNTER-ATTACKED by Marzuki — reveals Hamzah LED movement to topple Muhyiddin as PN chairman/Bersatu president after PM resignation, with PAS support. 'PN became toxic from that moment.' Despite BN-PN machinery merged + Wawasan police-vote strategy, Marzuki revelation exposes historical conflict root. Slight decline from intra-coalition counter-attack. [PRIORITY]."),
    "wawasan (parti wawasan negara)": (0.05, "improving", "priority", 2,
        "rev19 0.00 -> rev20 +0.05 (improving). 0734 build: Wawasan candidates CONFIRMED running under PN banner — Razali Abu Samah labeled 'PN-Wawasan' at Sikamat. Police-vote strategy operational (Hazani Ghazali + Razali ex-cop). 4 Wawasan candidates confirmed. Wawasan+PAS bloc stabilizes PN vs Bersatu exit. Reaches positive band. [PRIORITY]."),
    "wawasan admitted to pn": (0.05, "improving", "priority", 1,
        "rev19 0.00 -> rev20 +0.05. 0734 build: CONFIRMED — article labels Razali 'PN-Wawasan' candidate at Sikamat. Wawasan runs under PN banner while Bersatu runs separately under own logo. Confirms PN coalition fracture (Wawasan != Bersatu). [PRIORITY]."),
    "perikatan nasional (pn)": (0.42, "improving", "none", 1,
        "rev19 +0.40 -> rev20 +0.42. 0734 build: Wawasan confirmed running under PN banner (Sikamat 'PN-Wawasan' label). PN = PAS 5 + Wawasan 4 + Gerakan 1 + MIPP 1 = 11 seats. Merged machinery confirmed. Slight improvement. 5% <30% threshold."),
    "barisan nasional (bn)": (0.46, "improving", "none", 1,
        "rev19 +0.44 -> rev20 +0.46. 0734 build: BN-PN cooperation CONFIRMED NS-specific (no Terengganu talks — Rozi Mamat). Onn Hafiz Johor machinery transfer CONFIRMED. PN MB concession. Fathi Aris 'PH has no right to feel cheated' reinforces BN-PN normalization. Strong strategic position. [none]."),
    "anwar ibrahim (pmx)": (0.30, "declining", "priority", 1,
        "rev19 +0.35 -> rev20 +0.30. 0734 build: Kamil Munim jet-misuse denial (counter-attack on PKR Youth chief suggests rival faction). Fathi Aris: 'expelling UMNO from Cabinet won't give PMX stability.' Mohd Syahir 'PMX menghitung hari' persists. KJ 'sensitiviti orang Melayu.' Decline from persistent intra-unity-govt friction. [PRIORITY]."),
    "anwar ibrahim (pm, coalition manager)": (0.30, "declining", "priority", 1,
        "rev19 +0.35 -> rev20 +0.30. 0734 build: Kamil Munim jet-misuse counter-attack. Fathi Aris 'expelling UMNO won't give PMX stability.' Mohd Syahir 'PMX menghitung hari.' Decline from persistent friction. [PRIORITY]."),
    "pecat tang jay son (gerakan)": (-0.35, "stable", "priority", 1,
        "rev19 -0.40 -> rev20 -0.35. 0734 build: Gerakan-Bersatu Rahang dispute — Gerakan sacked Tang Jay Son for contesting on Bersatu ticket. Candidate STAYING (not withdrawing). Intra-PN component friction (not PN-MT expelling Bersatu). [PRIORITY] — director 'pecat' = [CRITICAL]-tier but FALSE POSITIVE corrected (Gerakan sacking, not PN expulsion)."),
    "roli complaint disrupting pn seat negotiations": (-0.62, "stable", "critical", 0,
        "Carried rev19. NOT DETECTED in 0734 build. Seat allocation stable per 103-calon list. No RoS intervention."),
    "pdm klawang reopen": (-0.15, "improving", "priority", 1,
        "rev19 -0.25 -> rev20 -0.15 (improving). 0734 build: RESOLVED — NS Police Chief Alzafny Ahmad confirms 2 investigation papers opened under Section 427 Penal Code, both from Kuala Klawang Jelebu (DUN Klawang N.28). PDM NOT closed — investigation active. Answers prior 'UNRESOLVED hour 20+' carry-forward. Improving from resolution. [PRIORITY]."),
    "lebih hebat new coalition": (-0.78, "stable", "critical", 0,
        "Carried rev19. NOT DETECTED — 23rd cycle with no formalization. No 'lebih hebat' entity emerged. [CRITICAL]-watch maintained."),
    "pn-removal-of-bersatu thread": (-0.90, "stable", "critical", 1,
        "rev19 -0.90 -> rev20 -0.90. 0734 build: Formal PN-MT expulsion STILL NOT issued. Marzuki exposes Hamzah-led anti-Muhyiddin movement (historical root) but NOT formal PN-MT action. Trajectory: pre-threshold; Bersatu voluntary realignment AFTER 1 Aug poll. [CRITICAL]."),
    "bersatu supreme leadership (mpt)": (-0.72, "stable", "critical", 0,
        "Carried rev19. Disputed baseline UNRESOLVED. No fresh content in 0734 build."),
    "pn supreme council (pn-mt)": (-0.55, "stable", "critical", 0,
        "Carried rev19. No PN-MT expulsion notice. Closest-to-formal-PN-action signal."),
    "ronald kiandee": (-0.25, "stable", "critical", 0,
        "Carried rev19. No fresh Kiandee content. Director-designated [CRITICAL] trigger."),
    "kuorum (bersatu mpt quorum dispute)": (-0.65, "stable", "critical", 0,
        "Carried rev19. No fresh quorum content. Dispute CONTESTED not resolved. Director-designated [CRITICAL]."),

    # PIR-16 — First Dominant Campaign Narratives
    "bersatu kacau daun narrative (khaled)": (-0.70, "declining", "critical", 1,
        "rev19 -0.68 -> rev20 -0.70. 0734 build: 'Bersatu kian tidak relevan, hadapi krisis identiti' Sinar opinion piece — dedicated analysis gaining traction. Khaled 'kacau daun' + 'KO habis' hard-news bilingual. References Johor deposit-loss precedent. [CRITICAL] maintained from prior viral-amplification threshold crossing."),
    "bersatu in disarray / bersatu exit imminent (characterisation)": (-0.78, "declining", "priority", 1,
        "rev19 -0.75 -> rev20 -0.78. 0734 build: 'Bersatu kian tidak relevan, hadapi krisis identiti' Sinar opinion piece (dedicated analysis, paywalled) — 'Bersatu in disarray' signal gaining hard-news outlet traction. Khaled 'kacau daun' + Muhyiddin 'toxic PN' + Marzuki historical root. 24 solo Bersatu candidates STABLE. [PRIORITY]."),
    "bersatu heading for wipeout in ns (analyst consensus)": (-0.78, "stable", "priority", 1,
        "rev19 -0.75 -> rev20 -0.78. 0734 build: 'Bersatu kian tidak relevan' Sinar analysis + analyst Muhammad Afifi warns 6 PKR candidates lost internal elections (machinery disunity). Bersatu deposit-loss risk in 5-corner Nilai. [PRIORITY]."),
    "bersatu exit imminent": (-0.55, "stable", "priority", 0,
        "Carried rev19. NOT CORROBORATED — 23rd cycle. 'kacau daun'/'toxic PN' = characterisations, NOT events. [CRITICAL] NOT crossed. [PRIORITY]."),
    "sasar bentuk kerajaan negeri (bersatu solo governing bid)": (-0.80, "stable", "critical", 1,
        "rev19 -0.80. 0734 build: Structural evidence (Bersatu separate from PN/Wawasan at Sikamat — Tun Faisal Bersatu vs Razali PN-Wawasan; Pertang — Faizal Fadli 'calon Bersatu' not 'calon PN'). NOT [CRITICAL] — no hard-news headline. [CRITICAL] NOT crossed (23rd cycle)."),
    "sasar bentuk kerajaan negeri (ph solo-governing bid)": (0.30, "stable", "critical", 0,
        "Carried rev19. PH contesting all 36 seats solo — only coalition fielding candidates in every seat. [CRITICAL] per director phrase match + hard-news."),
    "muhyiddin graft trial (jana wibawa rm24.4m gemas road)": (-0.62, "stable", "priority", 0,
        "Carried rev19. NS-specific: Felda Bukit Jalor->Gemas road, N.34 Gemas link. [PRIORITY]."),
    "mca biggest loser narrative (loke) → wee conciliatory rebuttal": (-0.45, "improving", "priority", 0,
        "rev19 -0.48 -> rev20 -0.45 (improving). LOOP CLOSED. Wee conciliatory. Mah Hang Soon still silent. [PRIORITY]."),
    "ph (pakatan harapan)": (0.38, "declining", "priority", 1,
        "rev19 +0.42 -> rev20 +0.38. 0734 build: 6 PKR PRN NS candidates lost 2025 party elections — analyst Muhammad Afifi warns machinery disunity (supporters may boycott/minimally campaign). Aminuddin Sikamat->Linggi swap = 'strategic error if fails.' Decline from machinery-disunity warning. [PRIORITY]."),
    "aminuddin harun (ph incumbent mb, n.32 linggi)": (0.52, "declining", "priority", 1,
        "rev19 +0.58 -> rev20 +0.52 (declining). 0734 build: Analyst Muhammad Afifi CRITICAL analysis: 'Why give up a proven-safe seat (Sikamat) for a BN-held seat (Linggi) with more uncertain prospects? If Aminuddin loses Linggi -> signals voters rejecting his leadership -> weakens PH admin-achievement narrative. Strategic error if fails.' 6 PKR candidates lost internal elections. Decline from analyst strategic-risk warning. 10% decline, <20% threshold. [PRIORITY]."),
    "aminuddin sikamat→linggi swap strategic risk": (-0.40, "declining", "critical", 1,
        "NEW rev20 (0734 build). Analyst Muhammad Afifi critical analysis: 'Why would PKR give up a proven-safe seat (Sikamat) for the MB to contest a BN-held seat (Linggi) with more uncertain prospects? If PKR fails to hold Sikamat and loses marginal seats due to disunited machinery, this swap will be remembered as a strategic error, not a bold move.' First detailed critical analysis from analytical perspective. [CRITICAL] — strategic-risk assessment of MB's seat swap."),
    # PIR-07 — Battlegrounds
    "n.28 klawang (pdm shutdown + cousins contest)": (0.10, "declining", "priority", 1,
        "rev19 +0.18 -> rev20 +0.10 (declining). 0734 build: PDM Klawang RESOLVED (police actively investigating, 2 papers Section 427). BUT campaign sabotage ESCALATION — 3 seats affected (Klawang + Palong + Chembong). PH flags burned/damaged at Palong (Sunday) + Chembong (Monday). Decline from sabotage escalation. [PRIORITY]."),
    "n.32 linggi (aminuddin mb move + bn manifesto 24 jul)": (0.26, "declining", "critical", 0,
        "rev19 +0.30 -> rev20 +0.26 (declining). 0734 build: Analyst warns Aminuddin's Sikamat->Linggi swap = 'strategic error if fails.' Umno's oldest fortress (since 1959). BN manifesto launch 24 Jul CONFIRMED. HIGH-STAKES. Slight decline from analyst risk assessment. [CRITICAL]."),
    "n.13 sikamat (nor azman vs tun faisal, 3-corner)": (0.35, "stable", "none", 1,
        "rev19 +0.38 -> rev20 +0.35. 0734 build: 3-cornered CONFIRMED: Nor Azman (PH/PKR) vs Tun Faisal (Bersatu Info Chief) vs Razali (PN-Wawasan, ex-cop). 'PN-Wawasan' label confirms Wawasan under PN. Bersatu and PN/Wawasan competing AGAINST each other = PN coalition fracture. Voters still hope Aminuddin stays. Stable."),
    "pertang (derhaka friction, jalaluddin)": (-0.15, "stable", "priority", 1,
        "rev19 -0.12 -> rev20 -0.15. 0734 build: Analyst warns Sikamat->Linggi swap strategic risk. Jalaluddin conciliatory toward PN (thanks PN for MB concession). 'Derhaka' language NOT found. BN manifesto launch 24 Jul. Director [PRIORITY]."),
    "mohamad hasan / tok mat (bn rantau)": (0.55, "stable", "priority", 1,
        "rev19 +0.58 -> rev20 +0.55. 0734 build: FIRST election-related fatality near Rantau (man killed installing flags, hit-and-run). Tok Mat absent for Asean Manila. Named as primary MB candidate. Slight decline from fatality proximity. [PRIORITY]."),
    "rantau (tok mat seat, straight fight)": (0.44, "declining", "priority", 1,
        "rev19 +0.48 -> rev20 +0.44 (declining). 0734 build: FIRST election-related fatality near Rantau — 23-year-old man killed in hit-and-run while installing party flags on Jalan Kuala Sawah-Rantau. Tok Mat absent for Asean Manila. Campaign safety concern. [PRIORITY]."),
    "n.34 gemas (pkr woman candidate, felda gugusan jelai)": (0.05, "declining", "critical", 1,
        "rev19 +0.10 (approx) -> rev20 +0.05. 0734 build: PKR candidate Siti Aishah lost internal election (41.52%) — machinery disunity risk per analyst. Felda Gugusan Jelai (replanting oil palm, no income). Jana Wibawa RM24.4m road link. 5-cornered. Slight decline. [CRITICAL] per Tier-4."),
}

# --- NEW ENTITIES from 0734 build ---
new_entity_entries = [
    {
        "entity": "Marzuki Mohamad (Datuk Dr)",
        "pir_tag": "PIR-06",
        "sentiment": "negative",
        "score": -0.55,
        "trend": "stable",
        "alert": "critical",
        "source_count": 1,
        "rationale": "NEW rev20 (0734 build). Ex-Confidential Secretary to Muhyiddin. COUNTER-ATTACKS Hamzah: reveals HAMZAH LED MOVEMENT TO TOPPLE MUHYIDDIN as PN chairman/Bersatu president after PM resignation, with PAS support. 'Dari saat itulah bermulanya PN menjadi toksik.' Historical root of Bersatu-PN conflict exposed. [CRITICAL] — exposes intra-coalition fracture historical root."
    },
    {
        "entity": "Hamzah Zainudin led anti-Muhyiddin movement",
        "pir_tag": "PIR-06",
        "sentiment": "negative",
        "score": -0.75,
        "trend": "stable",
        "alert": "critical",
        "source_count": 1,
        "rationale": "NEW rev20 (0734 build). Marzuki's revelation: after Muhyiddin resigned as PM, a movement to topple him as PN chairman AND Bersatu president began — LED BY HAMZAH with PAS leaders' support. 'PN became toxic from that moment.' Muhyiddin-camp response to Hamzah's midday 'don't call PAS toxic' statement. [CRITICAL] — 'toxic PN' entity per PIR-06 flag."
    },
    {
        "entity": "PN menjadi toksik (PN became toxic)",
        "pir_tag": "PIR-06",
        "sentiment": "negative",
        "score": -0.80,
        "trend": "declining",
        "alert": "critical",
        "source_count": 1,
        "rationale": "NEW rev20 (0734 build). Marzuki's framing: 'Dari saat itulah bermulanya PN menjadi toksik' — PN became toxic from the moment Hamzah moved against Muhyiddin. Direct 'toxic PN' entity per PIR-06 [CRITICAL] flag. Paired with Hamzah's midday rebuttal. Narrative volley active. [CRITICAL]."
    },
    {
        "entity": "Annuar Musa (Tan Sri)",
        "pir_tag": "PIR-06",
        "sentiment": "negative",
        "score": -0.35,
        "trend": "stable",
        "alert": "priority",
        "source_count": 1,
        "rationale": "NEW rev20 (0734 build). Referenced by Marzuki as source for 15 UMNO MPs withdrawing support from Muhyiddin, leading to PN government collapse 2021. Historical context for BN-PN friction."
    },
    {
        "entity": "Gerakan-Bersatu candidate-lending dispute (Rahang)",
        "pir_tag": "PIR-06",
        "sentiment": "negative",
        "score": -0.40,
        "trend": "stable",
        "alert": "priority",
        "source_count": 1,
        "rationale": "NEW rev20 (0734 build). Intra-PN component-party friction at Tier-4 seat Rahang. Gerakan sacks Bersatu-lent candidate Tang Jay Son for contesting under Bersatu logo. Candidate-lending arrangement broke down. NOT PN-MT expelling Bersatu — candidate staying. [PRIORITY] — cooperation-arrangement friction signal."
    },
    {
        "entity": "Tang Jay Son",
        "pir_tag": "PIR-06",
        "sentiment": "neutral",
        "score": -0.10,
        "trend": "stable",
        "alert": "none",
        "source_count": 1,
        "rationale": "NEW rev20 (0734 build). Bersatu DUN Rahang candidate. Gerakan sacked him for contesting under Bersatu ticket. Clarifies 'dipinjamkan' (lent) to Gerakan in 2023. Candidate STAYING. Intra-PN component friction."
    },
    {
        "entity": "Wong Chia Zhen",
        "pir_tag": "PIR-06",
        "sentiment": "negative",
        "score": -0.25,
        "trend": "stable",
        "alert": "none",
        "source_count": 1,
        "rationale": "NEW rev20 (0734 build). Gerakan Sec-Gen. Sacked Tang Jay Son for Bersatu ticket breach — 'serious disciplinary violation/breach of loyalty.' Reveals intra-PN component friction."
    },
    {
        "entity": "BN-PN cooperation is NS-specific (not national)",
        "pir_tag": "PIR-06",
        "sentiment": "neutral",
        "score": -0.10,
        "trend": "stable",
        "alert": "priority",
        "source_count": 1,
        "rationale": "NEW rev20 (0734 build). UMNO Terengganu chairman Rozi Mamat: no BN-PN talks in Terengganu. 'Each state has own acuan politik.' Contrasts with KJ/Noh 'blue wave to Selangor/Putrajaya' framing. BN-PN = NS+Johor only. [PRIORITY] — scope-limitation signal."
    },
    {
        "entity": "Rozi Mamat (Datuk) — no BN-PN in Terengganu",
        "pir_tag": "PIR-06",
        "sentiment": "neutral",
        "score": 0.05,
        "trend": "stable",
        "alert": "none",
        "source_count": 1,
        "rationale": "NEW rev20 (0734 build). UMNO Terengganu chairman. Confirms no BN-PN cooperation talks in Terengganu for PRU16. Political patterns differ by state. Open to cooperation if benefits rakyat."
    },
    {
        "entity": "Bersatu kian tidak relevan, hadapi krisis identiti",
        "pir_tag": "PIR-16",
        "sentiment": "negative",
        "score": -0.70,
        "trend": "declining",
        "alert": "priority",
        "source_count": 1,
        "rationale": "NEW rev20 (0734 build). Sinar Harian opinion/analysis piece (dedicated section): 'Bersatu increasingly irrelevant, facing identity crisis.' Strong PIR-16 'Bersatu in disarray' narrative signal gaining traction (Sinar publishing dedicated analysis). [PRIORITY] — hard-news outlet amplification of 'Bersatu in disarray.'"
    },
    {
        "entity": "Fathi Aris Omar",
        "pir_tag": "PIR-16",
        "sentiment": "neutral",
        "score": 0.10,
        "trend": "stable",
        "alert": "none",
        "source_count": 1,
        "rationale": "NEW rev20 (0734 build). Political observer, former editor. Major narrative analysis: 'PH has no right to feel cheated by UMNO/BN.' PH misread Unity Government basis. UMNO more comfortable with PAS/PN. Rebuts AMH 'resign to attack' call. Cites Melaka PRN precedent. Reinforces 'BN free to partner PN' normalization."
    },
    {
        "entity": "PH has no right to feel cheated (Fathi Aris narrative)",
        "pir_tag": "PIR-16",
        "sentiment": "neutral",
        "score": 0.05,
        "trend": "stable",
        "alert": "priority",
        "source_count": 1,
        "rationale": "NEW rev20 (0734 build). Major PIR-16 narrative analysis reinforcing 'BN free to partner PN' normalization. Direct rebuttal to AMH 'resign to attack' call. 'PH salah membaca asas kerjasama.' Reinforces 'makmal politik PRU16' framing. [PRIORITY] — narrative normalization signal."
    },
    {
        "entity": "6 PKR candidates lost party elections (machinery disunity)",
        "pir_tag": "PIR-16",
        "sentiment": "negative",
        "score": -0.40,
        "trend": "declining",
        "alert": "priority",
        "source_count": 1,
        "rationale": "NEW rev20 (0734 build). Analyst Muhammad Afifi warns: 6 PKR PRN NS candidates lost 2025 party elections at branch level — supporters may become passive, silently boycott, or campaign minimally. 'Elections are won through voter acceptance, machinery unity, and member confidence.' [PRIORITY] — PH machinery disunity warning."
    },
    {
        "entity": "Muhammad Afifi Abdul Razak",
        "pir_tag": "PIR-07",
        "sentiment": "neutral",
        "score": -0.10,
        "trend": "stable",
        "alert": "priority",
        "source_count": 1,
        "rationale": "NEW rev20 (0734 build). Analyst, senior lecturer. Warns of PKR machinery disunity (6 candidates lost internal elections). Critical analysis of Aminuddin's Sikamat->Linggi swap: 'strategic error if fails.' [PRIORITY] — analytical risk assessment."
    },
    {
        "entity": "Election-related death near Rantau (flag installation)",
        "pir_tag": "PIR-07",
        "sentiment": "negative",
        "score": -0.50,
        "trend": "stable",
        "alert": "critical",
        "source_count": 1,
        "rationale": "NEW rev20 (0734 build). FIRST election-related fatality in PRN NS 2026. 23-year-old man killed in hit-and-run while installing party flags near Rantau. Lorry hit signpost. Driver fled. Section 41(1) Road Transport Act. Near Tok Mat's seat area. [CRITICAL] — campaign safety escalation, first fatality."
    },
    {
        "entity": "DUN Palong (PH flags burned)",
        "pir_tag": "PIR-07",
        "sentiment": "negative",
        "score": -0.45,
        "trend": "stable",
        "alert": "priority",
        "source_count": 1,
        "rationale": "NEW rev20 (0734 build). Campaign-material sabotage: PH flags BURNED Sunday night (19 Jul) at DUN Palong (Felda seat). Legal action threatened under Section 4A Election Offences Act + Section 427 Penal Code. Escalation from Klawang-only to 3 seats. [PRIORITY]."
    },
    {
        "entity": "N.31 Chembong (flag damage incident)",
        "pir_tag": "PIR-07",
        "sentiment": "negative",
        "score": -0.40,
        "trend": "stable",
        "alert": "priority",
        "source_count": 1,
        "rationale": "NEW rev20 (0734 build). Campaign-material sabotage: flag posts DAMAGED Monday morning (20 Jul) at N31 DUN Chembong — T1 priority + Tier-4 seat. Escalation from 1 to 3 seats. [PRIORITY]."
    },
    {
        "entity": "PDM Klawang police investigation RESOLVED",
        "pir_tag": "PIR-07",
        "sentiment": "neutral",
        "score": -0.10,
        "trend": "improving",
        "alert": "priority",
        "source_count": 1,
        "rationale": "NEW rev20 (0734 build). NS Police Chief Alzafny Ahmad confirms 2 investigation papers opened under Section 427, both from Kuala Klawang. 19 Jul: PH flags/banners thrown into drain; car bumper scratched. PDM NOT closed — active investigation. [PRIORITY]."
    },
    {
        "entity": "Alzafny Ahmad (Datuk)",
        "pir_tag": "PIR-07",
        "sentiment": "neutral",
        "score": 0.05,
        "trend": "stable",
        "alert": "none",
        "source_count": 1,
        "rationale": "NEW rev20 (0734 build). NS Police Chief. Confirms 2 investigation papers for election sabotage at Kuala Klawang. 107 ceramah permits approved out of 109. Security 'baik dan terkawal.'"
    },
    {
        "entity": "N.13 Sikamat 3-cornered CONFIRMED (PN-Wawasan vs Bersatu vs PH)",
        "pir_tag": "PIR-07",
        "sentiment": "neutral",
        "score": 0.05,
        "trend": "stable",
        "alert": "critical",
        "source_count": 1,
        "rationale": "NEW rev20 (0734 build). CONFIRMED: Nor Azman (PH/PKR) vs Tun Faisal (Bersatu Info Chief) vs Razali (PN-Wawasan). 'PN-Wawasan' label confirms Wawasan runs under PN banner. Bersatu and PN/Wawasan competing AGAINST each other = PN coalition fracture. [CRITICAL] per Tier-4 + coalition fracture."
    },
    {
        "entity": "N.02 Pertang (3-cornered, demographics confirmed)",
        "pir_tag": "PIR-07",
        "sentiment": "neutral",
        "score": -0.10,
        "trend": "stable",
        "alert": "critical",
        "source_count": 1,
        "rationale": "NEW rev20 (0734 build). T1 priority seat. 3-cornered: Umry (PH/PKR, Mandarin fluent) vs Jalaluddin (BN, 2023 majority 2,790) vs Faizal Fadli (Bersatu). Malay 65.5%, Chinese 20.1%. Held by UMNO since 1964. BN manifesto launch 24 Jul. [CRITICAL] per T1 + derhaka friction."
    },
    {
        "entity": "Jalaluddin Alias (Datuk Seri) — Pertang candidate profile",
        "pir_tag": "PIR-07",
        "sentiment": "neutral",
        "score": 0.10,
        "trend": "stable",
        "alert": "priority",
        "source_count": 2,
        "rationale": "NEW rev20 (0734 build). NS Umno chief, BN candidate N.02 Pertang, seeking 3rd term. Thanks PN for backing BN. 'Derhaka' friction context. BN manifesto launch 24 Jul. Names Tok Mat + Sufian as potential MB. [PRIORITY]."
    },
    {
        "entity": "Umry Abdul Khois",
        "pir_tag": "PIR-07",
        "sentiment": "neutral",
        "score": 0.10,
        "trend": "stable",
        "alert": "none",
        "source_count": 1,
        "rationale": "NEW rev20 (0734 build). PH/PKR Pertang candidate. SJKC Pertang alumnus, Mandarin fluent — strategy to court Chinese voters (20.1%). Focus on PH admin record + PM Anwar's aura. [none]."
    },
    {
        "entity": "Faizal Fadli Idrus",
        "pir_tag": "PIR-07",
        "sentiment": "neutral",
        "score": -0.10,
        "trend": "stable",
        "alert": "none",
        "source_count": 1,
        "rationale": "NEW rev20 (0734 build). Bersatu Pertang candidate. Article labels him 'calon Bersatu' (not 'calon PN') — confirms Bersatu runs under own logo, separate from PN/Wawasan. [none]."
    },
    {
        "entity": "Bersatu sasar bentuk kerajaan negeri (structural evidence)",
        "pir_tag": "PIR-16",
        "sentiment": "negative",
        "score": -0.70,
        "trend": "stable",
        "alert": "priority",
        "source_count": 1,
        "rationale": "NEW rev20 (0734 build). Structural evidence: (1) Pertang — Faizal Fadli 'calon Bersatu' not 'calon PN'; (2) Sikamat — Bersatu (Tun Faisal) vs PN/Wawasan (Razali) competing AGAINST each other. Bersatu separate from PN/Wawasan confirmed. NOT [CRITICAL] — no hard-news headline. [PRIORITY]."
    },
    {
        "entity": "Wawasan guns for police vote (retired senior officers)",
        "pir_tag": "PIR-06",
        "sentiment": "neutral",
        "score": 0.10,
        "trend": "improving",
        "alert": "priority",
        "source_count": 1,
        "rationale": "NEW rev20 (0734 build). Wawasan formally part of PN. Fielding candidates via retired senior police officers — Hazani Ghazali, Razali Abu Samah. Strategy targets 200,000+ police + spouses votes. [PRIORITY]."
    },
    {
        "entity": "Mohd Syahir Che Sulaiman — resign-narrative expands to Perak + Pahang",
        "pir_tag": "PIR-16",
        "sentiment": "negative",
        "score": -0.22,
        "trend": "declining",
        "alert": "priority",
        "source_count": 1,
        "rationale": "NEW rev20 (0734 build). PAS MP Mohd Syahir. Expands resign-narrative to Perak + Pahang PH Exco. Invokes DAP Melaka as model. 'PMX and PH sedang menghitung hari.' Unity-govt-end escalation. [PRIORITY]."
    },
    {
        "entity": "DAP Melaka model (resign-narrative)",
        "pir_tag": "PIR-16",
        "sentiment": "negative",
        "score": -0.42,
        "trend": "stable",
        "alert": "priority",
        "source_count": 1,
        "rationale": "NEW rev20 (0734 build). Mohd Syahir directly invokes 'Tindakan DAP Melaka wajar dijadikan contoh' (PIR-16 'Melaka withdrawal' keyword). Resign-narrative expands beyond NS to Perak + Pahang using Melaka as precedent. [PRIORITY]."
    },
    {
        "entity": "PMX menghitung hari (PMX and PH counting days)",
        "pir_tag": "PIR-16",
        "sentiment": "negative",
        "score": -0.28,
        "trend": "declining",
        "alert": "priority",
        "source_count": 1,
        "rationale": "NEW rev20 (0734 build). Mohd Syahir escalation: 'PMX and PH sedang menghitung hari.' Unity-govt-end framing. 'MCA's reaction shows doubt.' [PRIORITY]."
    },
    {
        "entity": "KJ sensitiviti orang Melayu (Malay sensitivities)",
        "pir_tag": "PIR-16",
        "sentiment": "negative",
        "score": -0.22,
        "trend": "declining",
        "alert": "priority",
        "source_count": 1,
        "rationale": "NEW rev20 (0734 build). KJ sharper framing: 'sebahagian ahli Umno merasakan kerajaan persekutuan kurang memberi perhatian terhadap sensitiviti orang Melayu.' FMT BM+EN (3rd outlet). Reinforces 'penyatuan undi Melayu' + 'isyarat kepada PH.' [PRIORITY]."
    },
    {
        "entity": "Noh Omar — UMNO-PAS to Selangor (blue wave)",
        "pir_tag": "PIR-06",
        "sentiment": "positive",
        "score": 0.30,
        "trend": "stable",
        "alert": "none",
        "source_count": 1,
        "rationale": "NEW rev20 (0734 build). UMNO-PAS cooperation could form Selangor govt. NS formula as precursor. Blue wave Johor->NS->Selangor->PRU16. [none]."
    },
    {
        "entity": "Tok Mat — BN tidak pernah burukkan (clean campaign)",
        "pir_tag": "PIR-06",
        "sentiment": "positive",
        "score": 0.40,
        "trend": "stable",
        "alert": "none",
        "source_count": 1,
        "rationale": "NEW rev20 (0734 build). Mohamad Hasan frames BN-PN as 'electoral strategy not political coalition.' 'BN tidak pernah burukkan mana-mana pihak.' Willing to leave Cabinet if PM directs. In Manila for Asean FM meeting. [none]."
    },
    {
        "entity": "Khaled Nordin — Bersatu kacau daun",
        "pir_tag": "PIR-16",
        "sentiment": "negative",
        "score": -0.38,
        "trend": "stable",
        "alert": "priority",
        "source_count": 1,
        "rationale": "NEW rev20 (0734 build). Umno VP / Defence Minister. Labels Bersatu 'kacau daun' in NS. Urges voters 'KO habis-habis.' FMT BM corroboration. References Johor deposit-loss. [PRIORITY]."
    },
    {
        "entity": "KJ — makmal politik PRU16 framing (Sinar)",
        "pir_tag": "PIR-16",
        "sentiment": "positive",
        "score": 0.35,
        "trend": "stable",
        "alert": "none",
        "source_count": 1,
        "rationale": "NEW rev20 (0734 build). KJ frames NS as 'makmal politik' for PRU16. 'Formula BN, PN di NS mungkin ke Selangor.' If works, extend. [none]."
    },
    {
        "entity": "Kamil Munim jet-misuse denial",
        "pir_tag": "PIR-16",
        "sentiment": "negative",
        "score": -0.30,
        "trend": "declining",
        "alert": "priority",
        "source_count": 1,
        "rationale": "NEW rev20 (0734 build). AMK Kelantan denies viral claim that Tengku Zafrul and Kamil Munim misused government jet/asset. Counter-attack on PKR Youth chief suggests rival faction surfacing asset-misuse claims. PKR internal friction. [PRIORITY]."
    },
    {
        "entity": "Wee Ka Siong — BN-PN elak pecah undi (vote-split avoidance)",
        "pir_tag": "PIR-06",
        "sentiment": "neutral",
        "score": 0.05,
        "trend": "stable",
        "alert": "none",
        "source_count": 1,
        "rationale": "NEW rev20 (0734 build). Wee frames BN-PN as 'elak pecah undi' (vote-split avoidance), not merger. MCA = 'semak dan imbang.' Unity govt = 'perpaduan yang hipokrit' if just power-sharing. [none]."
    },
    {
        "entity": "DUN Chuah candidacy controversy RESOLVED",
        "pir_tag": "PIR-07",
        "sentiment": "neutral",
        "score": 0.05,
        "trend": "improving",
        "alert": "none",
        "source_count": 1,
        "rationale": "NEW rev20 (0734 build). Aminuddin confirms Chuah candidacy resolved. 2026 = 2-cornered: Boon Lai (PH) vs Pau Jeou Ching (BN). Kenny Chiew gives full support. [none]."
    },
    {
        "entity": "DUN Pilah two-women contest",
        "pir_tag": "PIR-07",
        "sentiment": "neutral",
        "score": 0.00,
        "trend": "stable",
        "alert": "none",
        "source_count": 1,
        "rationale": "NEW rev20 (0734 build). 2-women contest: Noorzunita (PH incumbent, lost internal election 37.05%) vs S Leza (BN). RECOVERED sidebar target. [none]."
    },
    {
        "entity": "N.34 Gemas (PKR woman candidate, Felda Gugusan Jelai)",
        "pir_tag": "PIR-07",
        "sentiment": "negative",
        "score": -0.15,
        "trend": "declining",
        "alert": "critical",
        "source_count": 1,
        "rationale": "NEW rev20 (0734 build). Tier-4. PKR candidate Siti Aishah lost internal election (41.52%) — machinery disunity. Felda Gugusan Jelai (replanting, no income). Jana Wibawa road link. 5-cornered. [CRITICAL] per Tier-4."
    },
    {
        "entity": "DUN Gemencheh (AMANAH vs BN straight fight)",
        "pir_tag": "PIR-07",
        "sentiment": "neutral",
        "score": 0.05,
        "trend": "stable",
        "alert": "none",
        "source_count": 1,
        "rationale": "NEW rev20 (0734 build). Straight fight: Abd Latif (PH/AMANAH, 70, oldest) vs Suhaimizan (BN). No Bersatu/PN. [none]."
    },
    {
        "entity": "DUN Bahau (MCA challenges DAP 20-year stronghold)",
        "pir_tag": "PIR-07",
        "sentiment": "neutral",
        "score": -0.10,
        "trend": "stable",
        "alert": "none",
        "source_count": 1,
        "rationale": "NEW rev20 (0734 build). MCA (BN) vs DAP (PH) straight fight. DAP held since 2004 (20+ years). BN-PN ground cooperation confirmed. [none]."
    },
    {
        "entity": "107 ceramah permits approved",
        "pir_tag": "PIR-07",
        "sentiment": "positive",
        "score": 0.25,
        "trend": "stable",
        "alert": "none",
        "source_count": 1,
        "rationale": "NEW rev20 (0734 build). 107 permits approved out of 109 received. Security 'baik dan terkawal.' Campaign operational data. [none]."
    },
    {
        "entity": "Six NS seats that tell the story (Malay Mail analysis)",
        "pir_tag": "PIR-07",
        "sentiment": "neutral",
        "score": 0.05,
        "trend": "stable",
        "alert": "none",
        "source_count": 1,
        "rationale": "NEW rev20 (0734 build). Malay Mail identifies 6 key seats: Rantau, Chennah, Linggi, Lenggeng, Lukut, Nilai. [none]."
    },
    {
        "entity": "Klawang cousins rivalry (Bakri vs Danni)",
        "pir_tag": "PIR-07",
        "sentiment": "neutral",
        "score": 0.10,
        "trend": "stable",
        "alert": "none",
        "source_count": 1,
        "rationale": "NEW rev20 (0734 build). N.28 Klawang 3-cornered: Bakri (PH) vs Danni (PN, cousin) vs Adib (Bersatu). Cordial cousin rivalry at market. [none]."
    },
    {
        "entity": "Jalaluddin thanks PN for backing BN to lead NS",
        "pir_tag": "PIR-06",
        "sentiment": "positive",
        "score": 0.30,
        "trend": "stable",
        "alert": "none",
        "source_count": 1,
        "rationale": "NEW rev20 (0734 build). Jalaluddin thanks PN for 'deklarasi awal' — PN leaves MB post to BN. MB candidates: Tok Mat, Jalaluddin, Sufian. [none]."
    },
    {
        "entity": "Arul Kumar — DAP Nilai defense",
        "pir_tag": "PIR-07",
        "sentiment": "neutral",
        "score": 0.10,
        "trend": "stable",
        "alert": "none",
        "source_count": 1,
        "rationale": "NEW rev20 (0734 build). DAP candidate DUN Nilai (N.10 Tier-4). Confident defending Nilai without BN. 5-cornered. [none]."
    },
    {
        "entity": "Senarai penuh 103 calon PRN NS 2026 (full candidate list)",
        "pir_tag": "PIR-07",
        "sentiment": "neutral",
        "score": 0.05,
        "trend": "stable",
        "alert": "none",
        "source_count": 1,
        "rationale": "NEW rev20 (0734 build). Complete candidate list. PH 36 solo / BN 25 / PN 11 / Bersatu 24. 0 nomination papers rejected. [none]."
    },
    {
        "entity": "Siti Aishah Seman @ Othman",
        "pir_tag": "PIR-07",
        "sentiment": "negative",
        "score": -0.15,
        "trend": "stable",
        "alert": "priority",
        "source_count": 1,
        "rationale": "NEW rev20 (0734 build). PKR DUN Gemas (N34 Tier-4). One of 2 women PKR fielded. Lost Ketua Cabang Tampin (41.52%) — machinery disunity risk. Felda Gugusan Jelai. [PRIORITY]."
    },
    {
        "entity": "Abd Latif A Thambi (Datuk)",
        "pir_tag": "PIR-07",
        "sentiment": "neutral",
        "score": 0.05,
        "trend": "stable",
        "alert": "none",
        "source_count": 1,
        "rationale": "NEW rev20 (0734 build). PH/AMANAH DUN Gemencheh, 70 — oldest candidate. Straight fight vs BN. Platform: sports hub. [none]."
    },
    {
        "entity": "Chong Fui Ming (Ah Chong)",
        "pir_tag": "PIR-07",
        "sentiment": "neutral",
        "score": 0.05,
        "trend": "stable",
        "alert": "none",
        "source_count": 1,
        "rationale": "NEW rev20 (0734 build). BN/MCA DUN Bahau. Challenges DAP 20-year stronghold. BN-PN ground cooperation confirmed. [none]."
    },
    {
        "entity": "Noorzunita Begum Mohd Ibrahim (Datuk)",
        "pir_tag": "PIR-07",
        "sentiment": "negative",
        "score": -0.10,
        "trend": "stable",
        "alert": "priority",
        "source_count": 1,
        "rationale": "NEW rev20 (0734 build). PH incumbent DUN Pilah. Lost Ketua Wanita Cabang (37.05%) — one of 6 PKR candidates who lost internal elections. Machinery disunity risk. [PRIORITY]."
    },
    {
        "entity": "Pau Jeou Ching",
        "pir_tag": "PIR-07",
        "sentiment": "neutral",
        "score": 0.05,
        "trend": "stable",
        "alert": "none",
        "source_count": 1,
        "rationale": "NEW rev20 (0734 build). BN candidate DUN Chuah. 2-cornered vs Yew Boon Lai (PH). [none]."
    },
    {
        "entity": "Tun Faisal Ismail Aziz (Datuk)",
        "pir_tag": "PIR-07",
        "sentiment": "neutral",
        "score": -0.10,
        "trend": "stable",
        "alert": "none",
        "source_count": 1,
        "rationale": "NEW rev20 (0734 build). Bersatu Info Chief. DUN Sikamat (N.13) candidate under Bersatu logo — competing AGAINST PN/Wawasan's Razali. [none]."
    },
    {
        "entity": "Razali Abu Samah (Datuk)",
        "pir_tag": "PIR-07",
        "sentiment": "neutral",
        "score": 0.05,
        "trend": "stable",
        "alert": "none",
        "source_count": 1,
        "rationale": "NEW rev20 (0734 build). PN/Wawasan DUN Sikamat candidate, 63. Retired PDRM, former acting Melaka Police Chief. 'PN-Wawasan' confirms Wawasan under PN. [none]."
    },
    {
        "entity": "Nor Azman Mohamad",
        "pir_tag": "PIR-07",
        "sentiment": "neutral",
        "score": 0.10,
        "trend": "stable",
        "alert": "none",
        "source_count": 1,
        "rationale": "NEW rev20 (0734 build). PH/PKR Sikamat candidate, PKR Info Chief. Acknowledges voters still hope Aminuddin stays. Promises to continue 'Tok Min's' work. [none]."
    },
    {
        "entity": "Yew Boon Lai (Datuk)",
        "pir_tag": "PIR-07",
        "sentiment": "positive",
        "score": 0.35,
        "trend": "stable",
        "alert": "none",
        "source_count": 1,
        "rationale": "NEW rev20 (0734 build). PH incumbent DUN Chuah. Chuah controversy RESOLVED. 2026 = 2-cornered vs Pau Jeou Ching (BN). [none]."
    },
    {
        "entity": "S Leza Md Yasin",
        "pir_tag": "PIR-07",
        "sentiment": "neutral",
        "score": 0.05,
        "trend": "stable",
        "alert": "none",
        "source_count": 1,
        "rationale": "NEW rev20 (0734 build). BN candidate DUN Pilah. 2-women contest vs Noorzunita (PH). [none]."
    },
    {
        "entity": "Muhammad Nazri Kassim (Datuk)",
        "pir_tag": "PIR-07",
        "sentiment": "negative",
        "score": -0.10,
        "trend": "stable",
        "alert": "priority",
        "source_count": 1,
        "rationale": "NEW rev20 (0734 build). PKR DUN Ampangan (N.14 Tier-4). Lost Ketua Cabang Seremban (47.91%) — machinery disunity risk. [PRIORITY]."
    },
    {
        "entity": "Ahmad Faez Abdul Razak (Datuk)",
        "pir_tag": "PIR-07",
        "sentiment": "negative",
        "score": -0.10,
        "trend": "stable",
        "alert": "priority",
        "source_count": 1,
        "rationale": "NEW rev20 (0734 build). PKR DUN Labu (N.25 Tier-4). Lost Ketua Cabang Rasah (35.10%) — machinery disunity risk. [PRIORITY]."
    },
    {
        "entity": "Gabungan lawan gabungan (coalition vs coalition)",
        "pir_tag": "PIR-16",
        "sentiment": "neutral",
        "score": -0.10,
        "trend": "stable",
        "alert": "none",
        "source_count": 1,
        "rationale": "NEW rev20 (0734 build). Sinar analysis: competition shifting from 'parti lawan parti' to 'gabungan lawan gabungan.' Three coalitions: PH (solo/36), BN-PN (25+11), Bersatu (solo/24). [none]."
    },
    {
        "entity": "Percaturan yang bakal mengundang padah kepada PKR",
        "pir_tag": "PIR-16",
        "sentiment": "negative",
        "score": -0.20,
        "trend": "stable",
        "alert": "none",
        "source_count": 1,
        "rationale": "NEW rev20 (0734 build). Sinar analysis of PKR strategy risks. Connects to Aminuddin swap + 6 PKR candidates who lost internal elections. [none]."
    },
    {
        "entity": "Mohd Yatim Osman (Asst Comm)",
        "pir_tag": "PIR-07",
        "sentiment": "neutral",
        "score": 0.00,
        "trend": "stable",
        "alert": "none",
        "source_count": 1,
        "rationale": "NEW rev20 (0734 build). Seremban OCPD. Investigating election-related hit-and-run death near Rantau. [none]."
    },
]

# Apply updates to existing entities
for e in prior["entities"]:
    key = e["entity"].lower().strip()
    if key in updates:
        new_score, trend, alert, sc_delta, rationale = updates[key]
        e["score"] = new_score
        e["trend"] = trend
        e["alert"] = alert
        e["source_count"] = e.get("source_count", 0) + sc_delta
        e["rationale"] = rationale
        # Determine sentiment from score
        if new_score > 0.20:
            e["sentiment"] = "positive"
        elif new_score < -0.20:
            e["sentiment"] = "negative"
        else:
            e["sentiment"] = "neutral"

# Add new entities (avoid duplicates)
existing_names = set(e["entity"].lower().strip() for e in prior["entities"])
for ne in new_entity_entries:
    if ne["entity"].lower().strip() not in existing_names:
        prior["entities"].append(ne)

# Update metadata
prior["metadata"]["version"] = "revision-20"
prior["metadata"]["generated"] = "2026-07-20T17:24:00+08:00"
prior["metadata"]["prior_revision_file"] = "sentiment-analysis/2026-07-20/sentiment-20260720-1455.json"
prior["metadata"]["prior_revision"] = "revision-19 (2026-07-20T14:55:00+08:00, 274 entities, 19 critical/83 priority/172 none), built on the 121-entity 0520 consolidated build"
prior["metadata"]["entity_build"] = "processed-entities/2026-07-20/entities-20260720-0734.json (72 entities — MIDAFTERNOON+LATEAFTERNOON delta extraction covering scrape cycles 05:51 + 07:21 UTC; all 6 scrape cycles now processed). Supersedes entities-20260720-0520.json (121 entities). SIGNIFICANT NEW CONTENT: Marzuki reveals Hamzah LED anti-Muhyiddin movement ('PN became toxic from that moment') — 'toxic PN' volley ESCALATES; Gerakan-Bersatu Rahang candidate-lending dispute (intra-PN friction); PDM Klawang RESOLVED (police actively investigating, 2 papers Section 427); Campaign sabotage ESCALATION — 3 seats (Klawang+Palong+Chembong); FIRST election-related fatality near Rantau (hit-and-run flag installation); Sikamat 3-corner CONFIRMED (Wawasan-under-PN + Bersatu-separate); 6 PKR candidates lost internal elections (machinery disunity warning); Fathi Aris 'PH has no right to feel cheated' narrative; BN-PN NS-specific confirmed (no Terengganu talks); 'Bersatu kian tidak relevan' Sinar opinion piece; Aminuddin Sikamat->Linggi swap strategic risk analyst assessment."
prior["metadata"]["entity_count"] = len(prior["entities"])
prior["metadata"]["director_cycle"] = "19 Jul 17:25 MYT (4th carry-forward) - 9th entity build (0734 midafternoon+lateafternoon, Day-2)"

# Count alerts
critical_count = sum(1 for e in prior["entities"] if e["alert"] == "critical")
priority_count = sum(1 for e in prior["entities"] if e["alert"] == "priority")
none_count = sum(1 for e in prior["entities"] if e["alert"] == "none")
prior["metadata"]["critical_count"] = critical_count
prior["metadata"]["priority_count"] = priority_count
prior["metadata"]["none_count"] = none_count

# Write output
with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
    json.dump(prior, f, indent=2, ensure_ascii=False)

print(f"Written: {OUTPUT_FILE}")
print(f"Total entities: {len(prior['entities'])}")
print(f"Critical: {critical_count}, Priority: {priority_count}, None: {none_count}")
