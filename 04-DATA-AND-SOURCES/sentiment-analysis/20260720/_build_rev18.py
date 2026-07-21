#!/usr/bin/env python3
"""
PRN Negeri Sembilan 2026 — Sentiment Analysis Builder
Revision 18 — built on entities-20260720-0313.json (81 entities, Day-2 midday extraction)
Carries forward revision-17 (241 entries) + applies updates/additions from the 0313 build.

Cycle: Day-2 midday (11:13 MYT extraction, covering morning 01:11 + midday 02:20 scrapes)
Key NEW developments vs rev17:
  PIR-06: BN-PN merged machinery CONFIRMED (leadership+ground); "toksik" Bersatu-PAS PUBLIC escalation;
          Wawasan police-vote strategy; Hamzah claims PN brand; Noh Omar party-hopping trail
  PIR-16: "Bersatu kacau daun" ELEVATED to CRITICAL (hard-news bilingual); "sasar bentuk kerajaan" (PH solo) CRITICAL;
          "majoriti mudah" NOW DIRECTLY QUOTED by Loke; "ada sesuatu yang tak kena" (KJ); Anwar discipline warning;
          PKR Youth counterattack; gelombang biru amplification
  PIR-07: Six key seats (Malay Mail); Linggi [CRITICAL]; Nilai 5-corner detail; Lenggeng/Lukut analysis;
          Johol Iltizam program; Pertang MB concession
"""
import json
import copy
from datetime import datetime

# === LOAD REV17 BASELINE ===
REV17_PATH = "/home/p62operator/.openclaw/workspace-ns/04-DATA-AND-SOURCES/sentiment-analysis/2026-07-20/sentiment-20260720-1010.json"
with open(REV17_PATH, "r", encoding="utf-8") as f:
    rev17 = json.load(f)

entries = rev17["entities"]
# Build lookup by entity name
lookup = {}
for i, e in enumerate(entries):
    lookup[e["entity"]] = i

# === UPDATES TO EXISTING ENTRIES ===
# Format: entity_name -> {fields to update}
updates = {
    # --- PIR-06 ---
    "Muhyiddin Yassin": {
        "score": -0.93, "trend": "declining", "alert": "critical", "source_count": 13,
        "rationale": "rev17 -0.92 -> rev18 -0.93. PUBLIC ESCALATION: Muhyiddin accused PAS-led PN of being 'toksik' and 'terpesong' under PAS leadership, claiming PAS makes false allegations (fitnah) against Bersatu (Sinar Harian hard-news 20 Jul). Hamzah rebuts directly: 'Muhyiddin could not have become PM without PAS.' SEVENTH converging trigger now PUBLIC leader-to-leader warfare. Plus Jana Wibawa RM24.4M trial continues (KESB failed BPK, Tengku Zafrul testimony, 54 contractors). Bersatu sharp-negative internal-fracture signal CONFIRMED -> [CRITICAL]."
    },
    "Bersatu (Parti Pribumi Bersatu Malaysia)": {
        "score": -0.89, "trend": "declining", "alert": "critical", "source_count": 14,
        "rationale": "rev17 -0.88 -> rev18 -0.89. Khaled 'kacau daun' + 'KO habis' now hard-news bilingual (FMT BM+EN, 20 Jul). 24 own-logo seats confirmed. Broken from PN, effectively solo opposition. 'Set up to replace Umno' must be rejected. Bersatu sharp-negative internal-fracture signal CONFIRMED -> [CRITICAL]."
    },
    "Bersatu-PN fracture (3-sided)": {
        "score": -0.90, "trend": "declining", "alert": "critical", "source_count": 10,
        "rationale": "rev17 -0.89 -> rev18 -0.90. PUBLIC ESCALATION: Muhyiddin 'PN toksik' vs Hamzah 'don't call PAS toxic' = first PUBLIC leader-to-leader Bersatu-vs-PAS/Wawasan warfare in hard-news (Sinar Harian). Hamzah claims PN name originated from him — brand-ownership dispute adds new dimension. Three-sided fracture deepening: Bersatu vs PAS/Wawasan vs PN-MT, plus BN-VP anti-Bersatu (Khaled)."
    },
    "PN-removal-of-Bersatu thread": {
        "score": -0.90, "trend": "declining", "alert": "critical", "source_count": 9,
        "rationale": "rev17 -0.90. Khaled 'KO habis' + 'kacau daun' hard-news bilingual pushes toward removal trajectory (BN-VP voice). Formal PN-MT expulsion notice STILL NOT issued. Trajectory: pre-threshold; most likely Bersatu voluntary realignment AFTER 1 Aug poll."
    },
    "lebih hebat new coalition": {
        "score": -0.78, "trend": "stable", "alert": "critical", "source_count": 6,
        "rationale": "Carried rev17. No explicit mention in today's 0313 build. Muhyiddin: NEW 'lebih hebat' coalition after PRN NS. No formal launch. PRU16 realignment vehicle. Remains at hint/bayangan stage."
    },
    "toxic PN (Muhyiddin framing)": {
        "score": -0.80, "trend": "declining", "alert": "critical", "source_count": 8,
        "rationale": "rev17 -0.78 -> rev18 -0.80. PUBLIC ESCALATION: Muhyiddin directly accuses PAS-led PN of being 'toksik' and 'terpesong' (Sinar Harian hard-news 20 Jul). Hamzah rebuts: 'Don't call PAS toxic, remember who helped you become PM.' Intra-opposition warfare Wawasan(Hamzah) vs Bersatu(Muhyiddin) now PUBLIC. Director 'toxic PN' = [CRITICAL] rule."
    },
    "kuorum (Bersatu MPT quorum dispute)": {
        "score": -0.65, "trend": "stable", "alert": "critical", "source_count": 7,
        "rationale": "Carried rev17. No fresh quorum content in today's 0313 build. Dispute CONTESTED not resolved. Director-designated [CRITICAL]."
    },
    "RoS complaint disrupting PN seat negotiations": {
        "score": -0.62, "trend": "stable", "alert": "critical", "source_count": 3,
        "rationale": "Carried rev17. No explicit RoS mention in today's 0313 build. RoS-intervention-adjacent [CRITICAL] sub-threshold."
    },
    "Bersatu Supreme Leadership (MPT)": {
        "score": -0.72, "trend": "stable", "alert": "critical", "source_count": 5,
        "rationale": "Carried rev17. Disputed baseline UNRESOLVED. No fresh content."
    },
    "PN Supreme Council (PN-MT)": {
        "score": -0.55, "trend": "stable", "alert": "critical", "source_count": 3,
        "rationale": "Carried rev17. No PN-MT expulsion notice. Closest-to-formal-PN-action signal."
    },
    "pecat Tang Jay Son (Gerakan)": {
        "score": -0.40, "trend": "declining", "alert": "critical", "source_count": 2,
        "rationale": "Carried rev17. Gerakan expelled Tang Jay Son for contesting on Bersatu ticket. Director flag: any 'pecat' = [CRITICAL]-tier."
    },
    "Ronald Kiandee": {
        "score": -0.25, "trend": "stable", "alert": "critical", "source_count": 3,
        "rationale": "Carried rev17. No fresh Kiandee content in 0313 build. Director-designated [CRITICAL] trigger."
    },
    "Perikatan Nasional (PN)": {
        "score": 0.38, "trend": "improving", "alert": "none", "source_count": 7,
        "rationale": "rev17 +0.30 -> rev18 +0.38. STRENGTHENED: Hamzah confirms merged BN-PN machinery at leadership+ground level. Claims PN name originated from him — asserts PN identity separate from Bersatu. PN = PAS+Wawasan+MIPP+Gerakan (11 seats). Takiyuddin shares stage with Hamzah+UMNO's Alwi = cross-party 'gelombang biru' unity."
    },
    "PAS": {
        "score": -0.18, "trend": "improving", "alert": "none", "source_count": 6,
        "rationale": "rev17 -0.22 -> rev18 -0.18 (improving). Hadi urges Melayu-Islam unity with non-extremist non-Muslims (Rasulullah model). Takiyuddin shares stage with Hamzah+Alwi. Penyatuan Melayu-Islam narrative gaining traction. PN-Wawasan bloc stabilizes PAS position."
    },
    "Hadi Awang": {
        "score": -0.18, "trend": "improving", "alert": "none", "source_count": 6,
        "rationale": "rev17 -0.22 -> rev18 -0.18 (improving). Urges perpaduan Melayu Islam + bukan Islam tidak ekstrem, modelled on Rasulullah's approach. Frames BN-PN as unity formula. Sarawak/Sabah as final targets. Constructive unity framing."
    },
    "Barisan Nasional (BN)": {
        "score": 0.42, "trend": "improving", "alert": "none", "source_count": 10,
        "rationale": "rev17 +0.40 -> rev18 +0.42. BN-PN merged machinery confirmed. Khaled 'kacau daun' anti-Bersatu (assertive). Noh Omar blue-wave advocacy. Johari/KJ/Zahid PRU16 benchmark framing. 25 seats, no overlap with PN. Strong strategic position. Net positive."
    },
    "UMNO": {
        "score": 0.15, "trend": "declining", "alert": "none", "source_count": 8,
        "rationale": "rev17 +0.18 -> rev18 +0.15. Khaled 'kacau daun' assertive + Johari PRU16 benchmark + Noh Omar rejoined + Alwi shares stage with PAS. BUT Anwar discipline warning targets Umno ministers + Akmal challenges PM + Muhyiddin 'toksik' implicates PAS-UMNO alliance. Unity-govt friction is negative drag."
    },
    "Wawasan (Parti Wawasan Negara)": {
        "score": -0.05, "trend": "improving", "alert": "priority", "source_count": 5,
        "rationale": "rev17 -0.15 -> rev18 -0.05 (improving). Formally admitted to PN. CONCRETE candidate deployment: retired senior police officers Hazani Ghazali (ex-Bukit Aman internal security director) + Razali Abu Samah (ex-Melaka deputy police chief). Strategy targets 200,000+ police + spouses votes, leveraging Hamzah's home minister tenure (2020-2022). Wawasan+PAS bloc stabilizes PN vs Bersatu exit."
    },
    "Hamzah Zainudin": {
        "score": -0.10, "trend": "improving", "alert": "priority", "source_count": 8,
        "rationale": "rev17 -0.20 -> rev18 -0.10 (improving). MAJOR: Leads merged BN-PN machinery at leadership+ground level. Rebuts Muhyiddin 'toksik': 'Muhyiddin could not have become PM without PAS.' Claims PN name originated from him. Says combination can take over NS and extend to PRU. Wawasan police-vote strategy operational. Political position STRENGTHENING — operational leader of merged machinery + asserting PN brand control."
    },
    "Ahmad Zahid Hamidi (Zahid)": {
        "score": 0.20, "trend": "stable", "alert": "none", "source_count": 6,
        "rationale": "rev17 +0.22 -> rev18 +0.20. Frames BN-PN as PRU16 test. PKR Youth (Kamil Munim) alleges Zahid wants PM post, building momentum to bring down Anwar. Slight negative drag from allegation. Overall strategic framing intact."
    },
    "Takiyuddin Hassan": {
        "score": 0.20, "trend": "improving", "alert": "none", "source_count": 3,
        "rationale": "rev17 +0.15 -> rev18 +0.20. PAS sec-gen shared stage with Hamzah and UMNO's Md Alwi Che Ahmad at Seremban event — symbolising BN-PN-Wawasan 'gelombang biru' unity across party lines. Cross-party stage sharing = cooperation-vector strengthening."
    },
    "gabung jentera (machinery merger)": {
        "score": 0.58, "trend": "improving", "alert": "none", "source_count": 6,
        "rationale": "rev17 +0.48 -> rev18 +0.58. MAJOR CONFIRMATION: Hamzah 'Kita telah gabungkan dua jentera daripada PN dan juga BN' — merged at leadership AND ground level. Candidates deployed together with combined teams. 'Mampu mengambil alih Negeri Sembilan.' If successful, extend to PRU. Strongest cooperation-vector signal to date."
    },
    "BN-PN joint manifesto (manifesto bersepadu)": {
        "score": 0.50, "trend": "improving", "alert": "none", "source_count": 6,
        "rationale": "rev17 +0.48 -> rev18 +0.50. Strengthened by merged-machinery confirmation. Annuar confirmed joint manifesto. 4-stage formalization trajectory continues (seat-swap -> gabung jentera -> manifesto bersepadu -> kongsi pentas)."
    },
    "Wawasan admitted to PN": {
        "score": -0.05, "trend": "improving", "alert": "priority", "source_count": 5,
        "rationale": "rev17 -0.15 -> rev18 -0.05 (improving). FMT 20 Jul: Wawasan formally admitted to PN. Concrete candidate deployment via retired police officers. Hamzah leveraging home minister ties. Coalition structure: PN = PAS+Gerakan+MIPP+Wawasan; Bersatu SOLO (24 seats). Resolves 'mystery of 11 PN seats.'"
    },
    "PDM Klawang shutdown/reopen": {
        "score": -0.22, "trend": "declining", "alert": "priority", "source_count": 3,
        "rationale": "Carried rev17. No explicit PDM Klawang mention in today's 0313 build. Jalaluddin expects reopen 1-2 days (carried). Watch Day-2 for reopen confirmation. Klawang seat covered (cousins rivalry) but PDM-level disruption not found in today's articles."
    },
    "Mohamed Khaled Nordin": {
        "score": -0.38, "trend": "declining", "alert": "priority", "source_count": 7,
        "rationale": "rev17 -0.32 -> rev18 -0.38. DEEPENING: 'kacau daun' + 'KO habis' now hard-news BILINGUAL (FMT BM+EN, 20 Jul). Urges voters to KO Bersatu completely — repeat Johor wipeout. Frames Bersatu 'ditubuhkan nak ganti UMNO.' Pro BN-PN: 'persefahaman beri kelebihan.' PM's budi bicara on minister appointments. Rhetorical escalation; NOT formal PN-MT action. [PRIORITY]."
    },
    "Bersatu KO habis (electoral-elimination call)": {
        "score": -0.60, "trend": "declining", "alert": "priority", "source_count": 6,
        "rationale": "rev17 -0.56 -> rev18 -0.60. Khaled 'KO habis' + 'kacau daun' hard-news bilingual (FMT BM+EN). Bersatu candidates faced deposit losses in Johor. 'Set up to replace Umno' must be completely rejected. Electoral-elimination rhetoric by BN (not PN) leader — adjacent, NOT formal PN-MT expulsion. [PRIORITY]."
    },
    "gelombang Melayu ke BN (Malay wave to BN)": {
        "score": 0.40, "trend": "improving", "alert": "none", "source_count": 5,
        "rationale": "rev17 +0.35 -> rev18 +0.40. Hamzah 'gelombang biru' from penyatuan hati across party lines. Noh Omar: blue wave Johor->NS->Selangor->Putrajaya. Cross-party leaders (Hamzah, UMNO's Alwi, PAS Takiyuddin) sharing stage. Strengthening."
    },
    "Bersatu advised to quit PN with Gerakan/MIPP": {
        "score": -0.55, "trend": "declining", "alert": "priority", "source_count": 2,
        "rationale": "Carried rev17. Lau Zhe Wei (IIUM): Bersatu should quit PN + take Gerakan/MIPP. Corroborates Muhyiddin lebih-hebat hint. Bersatu now solo 24 seats."
    },
    "Bersatu heading for wipeout in NS (analyst consensus)": {
        "score": -0.75, "trend": "declining", "alert": "priority", "source_count": 5,
        "rationale": "rev17 -0.72 -> rev18 -0.75. Azeem Fazwan 'in no position to win seats going solo.' Azmil Tayeb 'all people see is infighting.' Wan Saiful 'kacau daun' + Khaled 'KO habis' hard-news bilingual. Bersatu 24 solo seats + 5-corner Nilai = deposit-loss risk. Reinforces exit trajectory."
    },
    "Annuar Musa": {
        "score": -0.35, "trend": "stable", "alert": "priority", "source_count": 4,
        "rationale": "Carried rev17. PN info chief; confirmed BN-PN JOINT MANIFESTO. Not in today's 0313 build. Carried stable."
    },
    "Bersatu goes solo under own logo (24 seats)": {
        "score": -0.62, "trend": "stable", "alert": "none", "source_count": 8,
        "rationale": "rev17 -0.62. Full-text confirmed across FMT, NST, Sinar, Malay Mail. Bersatu broken from PN, effectively solo opposition party. 24 seats under own logo."
    },

    # --- PIR-16 ---
    "sasar bentuk kerajaan negeri (Bersatu solo governing bid)": {
        "score": -0.80, "trend": "stable", "alert": "critical", "source_count": 5,
        "rationale": "Carried rev17. Bersatu contests 24 seats under own logo (EXCEEDS simple-majority 19) targeting solo state-government formation. Hard-news (MalaysiaGazette + Sinar) = [CRITICAL]. DIRECTLY CONTRADICTS PN-MB-concedes-to-BN + joint-manifesto. No change this cycle."
    },
    "Bersatu kacau daun (Wan Saiful + Khaled)": {
        "score": -0.68, "trend": "declining", "alert": "critical", "source_count": 6,
        "rationale": "rev17 -0.58 [PRIORITY] -> rev18 -0.68 [CRITICAL]. ELEVATED: Khaled Nordin 'Bersatu hanya kacau daun' + 'KO habis-habis' now hard-news BILINGUAL (FMT BM + EN, 20 Jul). FIRST time this PIR-16 narrative keyword gets simultaneous BM+EN hard-news amplification = >50% volume increase from prior cycles. Director rule: viral amplification >50% = [CRITICAL]. Challenges 'penyatuan undi Melayu' — frames Bersatu as splitter/nuisance, not legitimate opposition. References Johor deposit-loss precedent. [CRITICAL]."
    },
    "Bersatu in disarray (Wan Saiful kacau daun + Kiandee + resignations + Khaled)": {
        "score": -0.75, "trend": "declining", "alert": "priority", "source_count": 7,
        "rationale": "rev17 -0.70 -> rev18 -0.75. Khaled 'kacau daun' hard-news bilingual + Wan Saiful 'kacau daun' + Kiandee quorum + MPT resignations + analyst wipeout consensus + Hamzah rebuke + Muhyiddin 'toksik' escalation. Director-listed 'Bersatu in disarray' entity, deepening."
    },
    "Bersatu exit from PN imminent? (mkini SNAPSHOT)": {
        "score": -0.55, "trend": "stable", "alert": "priority", "source_count": 3,
        "rationale": "Carried rev17. mkini SNAPSHOT remains lone viral-tier item. No hard-news corroboration of THAT exact framing. Substantive exit signals (lebih-hebat -0.78, sasar -0.80) ARE [CRITICAL] hard-news, scored separately. [PRIORITY] only."
    },
    "Anthony Loke": {
        "score": 0.50, "trend": "stable", "alert": "none", "source_count": 11,
        "rationale": "rev17 +0.52 -> rev18 +0.50. Targets 23 seats for safe majority. Avoids Rantau to preserve unity-govt harmony. Faces MCA's Siow in Chennah (one-on-one). Won't attack Cabinet colleagues. Defends Aminuddin as MB. Says Chennah '50-50' chance. 'Majoriti mudah' framing: 19 = thin, 23 = safe. Marginal dip from '50-50' Chennah admission but overall strong."
    },
    "MCA": {
        "score": -0.50, "trend": "declining", "alert": "priority", "source_count": 8,
        "rationale": "rev17 -0.48 -> rev18 -0.50. Chennah test: MCA challenging DAP via BN-PN formula (Utusan analysis). Siow Kong Choon vs Loke. Loke won 2023 by 2,200 majority. MCA viability test. Triple pressure: Loke 'biggest loser' + internal (Saw/Chong) + Chennah demographics risk. Defensive posture deepening."
    },
    "MCA biggest loser (Loke) + MCA rebuttal trajectory": {
        "score": -0.52, "trend": "declining", "alert": "priority", "source_count": 8,
        "rationale": "rev17 -0.52. Chennah one-on-one (Loke vs Siow) = test of BN-PN formula effectiveness (Utusan). Loke won 2023 by 2,200. MCA rebuttal = containment not counter-attack. Defensive deepening."
    },
    "penyatuan undi Melayu": {
        "score": 0.22, "trend": "improving", "alert": "none", "source_count": 9,
        "rationale": "rev17 +0.15 -> rev18 +0.22 (improving). BN-PN laung penyatuan Melayu-Islam vs PH jual prestasi. Hadi invokes Rasulullah's model. KJ: if Malay votes don't split, can win Selangor. Pemuda Umno Kapar (Affifi) wants formula extended. Counter-narrative gaining traction. Challenges 'Bersatu kacau daun' framing."
    },
    "makmal politik PRU16 framing": {
        "score": 0.32, "trend": "improving", "alert": "none", "source_count": 7,
        "rationale": "rev17 +0.25 -> rev18 +0.32 (improving). MULTI-LEADER corroboration: Johari (NS = benchmark/penanda aras), KJ (if formula works, extend to Selangor), Hamzah (if successful, continue), Zahid (NS determines alignment). Utusan: 'Negeri Sembilan penentu kerjasama PRU16.' Strengthening."
    },
    "Muhyiddin graft trial": {
        "score": -0.60, "trend": "declining", "alert": "priority", "source_count": 4,
        "rationale": "rev17 -0.55 -> rev18 -0.60. Trial ongoing: JKR paid RM24.4M to KCJ Engineering for Felda Bukit Jalor-Gemas road project (RM62M contract). Muhyiddin gave list of 54 contractors to Tengku Zafrul. KESB failed first BPK evaluation but PMO submitted supporting info. Trial continues. Details deepening negative."
    },
    "sole opposition (Muhyiddin lone credible opposition)": {
        "score": -0.55, "trend": "declining", "alert": "none", "source_count": 6,
        "rationale": "rev17 -0.50 -> rev18 -0.55. Bersatu contesting 24 seats under own logo — broken from PN, effectively solo opposition party. Khaled: 'set up to replace Umno' must be rejected. Bersatu candidates faced deposit losses in Johor. PN (PAS-led) now separate entity. Sole-opposition status confirmed but weakened."
    },
    "majoriti mudah (BN confidence)": {
        "score": -0.10, "trend": "declining", "alert": "priority", "source_count": 4,
        "rationale": "rev17 0.00 (NOT yet quoted) -> rev18 -0.10. NOW DIRECTLY QUOTED by Loke: 19 seats = 'majoriti mudah' (thin majority), 'apa sahaja boleh berlaku.' PH targets 23 for 'safe' majority. This is PH's DEFENSIVE framing (acknowledging 19 is too thin) per Director 'not taking for granted' (PH defence) vs 'majoriti mudah' (BN confidence). Loke's usage = PH defence, NOT BN confidence. Slightly negative (vulnerability signal). [PRIORITY]."
    },
    "campaign on policies not personal attacks (Loke)": {
        "score": 0.42, "trend": "improving", "alert": "none", "source_count": 5,
        "rationale": "rev17 +0.42. Clean-campaign call now BIPARTISAN (Loke+Anwar+Khaled+Zahid). Anwar discipline warning reinforces. Tok Mat: 'BN never attacks anyone.' Convergence holds through Day-2."
    },
    "bipartisan clean-campaign convergence (state-development focus)": {
        "score": 0.44, "trend": "improving", "alert": "priority", "source_count": 5,
        "rationale": "rev17 +0.42 -> rev18 +0.44. Anwar discipline warning (PM warns ministers) reinforces convergence. Mohamad Hasan: 'BN never burukkan mana-mana pihak.' Loke avoids Rantau. Clean-campaign norms strengthening. Counter to 'derhaka'/personal-attack friction."
    },
    "MB after PRN (PN concedes MB to BN)": {
        "score": 0.22, "trend": "improving", "alert": "none", "source_count": 6,
        "rationale": "rev17 +0.15 -> rev18 +0.22. Jalaluddin thanks PN for backing BN to lead NS. MB post left to Umno/BN. Names Mohamad Hasan and Sufian Maradzi as potential MB. PN early declaration = concession. Strengthens BN-PN cooperation vector."
    },
    "PH sasar 23 kerusi (safe majority / 8123)": {
        "score": 0.30, "trend": "improving", "alert": "priority", "source_count": 6,
        "rationale": "rev17 +0.27 -> rev18 +0.30. Loke: PH targets 23 of 36 for 'safe' majority. Math: 17 current; 18=tie; 19='majoriti mudah' (NOW QUOTED); 23=safe. '8123'=Aug 1, target 23. Frames 2026 crisis: 14 Umno ADUN withdrew + 5 PN backdoor. Hard-news (FMT, Sinar, Malay Mail) = director 'sasar bentuk kerajaan' phrase match."
    },
    "derhaka friction (Pertang)": {
        "score": -0.20, "trend": "declining", "alert": "priority", "source_count": 4,
        "rationale": "Carried rev17. Explicit 'derhaka' language NOT found in today's 0313 build. Pertang covered (Jalaluddin thanks PN for MB concession) but derhaka friction not escalated. Corroborated (BH+NST+Metro) from prior. Director rule: 'derhaka' at Pertang = [PRIORITY]. BN manifesto launch 24 Jul here."
    },
    "AMH resign-call (PH Youth joint statement)": {
        "score": -0.40, "trend": "stable", "alert": "priority", "source_count": 5,
        "rationale": "Carried rev17. AMH calls BN Ministers to resign. Intra-PH dissent (Hassan Karim) + Khaled dismisses. Anwar discipline warning adds containment."
    },
    "resign-to-attack unity partners (federal-state firewall)": {
        "score": 0.38, "trend": "improving", "alert": "none", "source_count": 5,
        "rationale": "rev17 +0.35 -> rev18 +0.38. Anwar discipline warning (20 Jul) REINFORCES firewall: PM warns ministers not to attack unity govt colleagues during PRN or resign. Discussed with Zahid and Fadillah. Mohamad Hasan: willing to leave Cabinet if directed. Firewall strengthening."
    },
    "Akmal counter-escalation (Umno Youth, Nga resign too)": {
        "score": -0.35, "trend": "stable", "alert": "priority", "source_count": 7,
        "rationale": "rev17 -0.35. Akmal challenges PM to drop ALL ministers from parties contesting PH, not just BN. Escalating political pressure on unity govt discipline question. Anwar discipline warning = counter."
    },
    "DAP coalition-intolerant (Hadi frame)": {
        "score": -0.45, "trend": "declining", "alert": "priority", "source_count": 4,
        "rationale": "rev17 -0.45. Hadi frames DAP as threat. PKR Youth (Shahrul) urges PH Selangor to reassess BN ties = intra-unity-govt friction feeding this frame. Counter: Madani reforms (Teo)."
    },
    "Melaka PH-BN fracture / DAP withdrawal": {
        "score": -0.42, "trend": "stable", "alert": "priority", "source_count": 8,
        "rationale": "Carried rev17. DAP withdrew from Melaka state govt. Opposition weaponises as 'DAP coalition-intolerant.' Shahrul Adnan (Selangor PKR Youth) urges reassessment = spillover. Stable."
    },

    # --- PIR-07 ---
    "Aminuddin Harun (PH incumbent MB, N.32 Linggi)": {
        "score": 0.58, "trend": "stable", "alert": "priority", "source_count": 12,
        "rationale": "rev17 +0.62 -> rev18 +0.58. Leaving Sikamat to contest Linggi — Umno's oldest fortress (since 1959). Prefers small-team face-to-face campaigning. Says MB status is NOT an advantage — only caretaker govt. Loke defends: 'not corrupt, no millions in bank account.' 14 Umno ADUN withdrew support in April crisis. Marginal dip from caretaker-disadvantage acknowledgment. NO >20% drop."
    },
    "N.32 Linggi (Aminuddin MB move + BN manifesto 24 Jul)": {
        "score": 0.30, "trend": "stable", "alert": "critical", "source_count": 8,
        "rationale": "rev17 +0.35 -> rev18 +0.30. Aminuddin (PH caretaker MB) vs Mohd Faizal Ramli (BN/Umno). Umno's oldest fortress — never changed hands since 1959. Formerly represented by Mohd Isa Abdul Samad. 60.4% Malay, ~18% Chinese, ~18% Indian. Aminuddin campaigning one-on-one, small team. BN manifesto launch 24 Jul here. HIGH-STAKES symbolic battle. [CRITICAL] per entity-extraction team + director BN-manifesto-24-Jul watch."
    },
    "N.28 Klawang (PDM shutdown + cousins contest)": {
        "score": 0.22, "trend": "declining", "alert": "none", "source_count": 6,
        "rationale": "rev17 +0.25 -> rev18 +0.22. Three-cornered: Bakri Sawir (PH incumbent) vs Danni Rais (PN) vs Muhammad Adib Musa (Bersatu). Cousins as political rivals — cordial at Kuala Klawang market. 13,355 voters. PDM shutdown NOT mentioned in today's build (watch for reopen). Marginal decline from 3-corner complexity."
    },
    "Bakri Sawir (PH Klawang incumbent)": {
        "score": 0.48, "trend": "stable", "alert": "none", "source_count": 4,
        "rationale": "rev17 +0.45 -> rev18 +0.48. Cousin of PN challenger Danni Rais. Crossed paths at Kuala Klawang market — calm, cordial, exchanged jokes. Emphasises healthy campaign and rule-following. Marginal improvement from positive cordial framing."
    },
    "Mohamad Hasan / Tok Mat (BN Rantau)": {
        "score": 0.64, "trend": "improving", "alert": "none", "source_count": 9,
        "rationale": "rev17 +0.62 -> rev18 +0.64. Rantau since 2004, won 71.7% in 2023. Says BN never attacks anyone during campaign. BN-PN understanding is strategy, not coalition. Willing to leave Cabinet if PM directs. Loke deliberately avoids campaigning here = confirms strength. 14,000+ voters under 40. Marginal improvement."
    },
    "Rantau (Tok Mat seat, straight fight)": {
        "score": 0.52, "trend": "improving", "alert": "none", "source_count": 5,
        "rationale": "rev17 +0.50 -> rev18 +0.52. Umno stronghold since 2004. 71.7% in 2023. 54.8% Malay, 27.6% Indian, 16% Chinese. Loke avoids campaigning here to preserve unity-govt harmony. Confirms stronghold status."
    },
    "Pertang (derhaka friction, Jalaluddin)": {
        "score": -0.15, "trend": "stable", "alert": "priority", "source_count": 6,
        "rationale": "rev17 -0.20 -> rev18 -0.15. Jalaluddin thanks PN for backing BN to lead NS. MB post left to Umno/BN. Names Mohamad Hasan and Sufian Maradzi as potential MB. 'Derhaka' language NOT found in today's build (not escalated). PN MB concession is positive. Marginal improvement. Director [PRIORITY]. BN manifesto launch 24 Jul here."
    },
    "Jalaluddin Alias (NS Umno chief, BN Pertang)": {
        "score": 0.10, "trend": "stable", "alert": "priority", "source_count": 8,
        "rationale": "rev17 +0.05 -> rev18 +0.10. Thanks PN for backing BN to lead NS. MB post left to Umno/BN. Names Mohamad Hasan and Sufian Maradzi as MB candidates. PN MB concession = positive. 'Derhaka' not escalated today. Marginal improvement."
    },
    "N.14 Ampangan (Nazri Kassim, defector-framing watch)": {
        "score": -0.10, "trend": "stable", "alert": "priority", "source_count": 5,
        "rationale": "rev17 -0.15 -> rev18 -0.10. Hamzah held joint majlis with PN candidates for Ampangan + Sikamat alongside BN and PAS leadership. BN-PN merged machinery deployed. Marginal improvement from joint-majlis + merged-machinery confirmation. Defector-framing NOT intensifying."
    },
    "N.13 Sikamat (Nor Azman vs Tun Faisal, 3-corner)": {
        "score": 0.38, "trend": "stable", "alert": "none", "source_count": 6,
        "rationale": "rev17 +0.40 -> rev18 +0.38. Aminuddin's former seat (leaving to contest Linggi). Hamzah met PN candidates for Sikamat with BN-PAS leadership. Vacated by caretaker MB — significant symbolic battleground. Marginal dip from seat-vacation symbolism."
    },
    "Chennah (Loke vs Siow straight fight, 47.8% Malay)": {
        "score": 0.30, "trend": "stable", "alert": "none", "source_count": 5,
        "rationale": "rev17 +0.35 -> rev18 +0.30. Loke (DAP/PH) vs Siow Kong Choon (MCA/BN) — straight fight enabled by BN-PN understanding. 14,422 voters: 47.25% Malay, 42.68% Chinese. Loke won 2023 by 2,200. Loke says '50-50' chance. Utusan: test of BN-PN formula. Marginal dip from '50-50' admission + demographics risk."
    },
    "Chennah demographics risk (Loke LOSES if PRU15 repeats)": {
        "score": -0.30, "trend": "stable", "alert": "priority", "source_count": 3,
        "rationale": "rev17 -0.28 -> rev18 -0.30. 47.25% Malay (up from 44% in 2018), 42.68% Chinese, 2% Indian. PH vote DROPPED to 44% by PRU15; BN+PN combined 56%. If PRU15 repeats, Loke LOSES. Loke says '50-50' chance. Risk persists; marginal deepening."
    },
    "N.10 Nilai (5-corner, 21.9% Indian)": {
        "score": -0.10, "trend": "stable", "alert": "none", "source_count": 5,
        "rationale": "rev17 -0.05 -> rev18 -0.10. Largest constituency: 41,000+ voters, ~14,200 under 30. 42.5% Malay, 32.6% Chinese, 21.9% Indian. Five-cornered: Arul Kumar (DAP) vs Lai Chien Kong (BN) vs Saravan Kumar (Bersatu) + Berjasa + independent. Arul Kumar confident (won ~10,000 in GE2022 without BN). Marginal dip from 5-corner complexity."
    },
    "N.19 Johol (Saiful Yazan vs Mohd Zailan, straight fight)": {
        "score": 0.20, "trend": "improving", "alert": "none", "source_count": 5,
        "rationale": "rev17 +0.15 -> rev18 +0.20. BN incumbent Saiful Yazan launches 'Iltizam Johol' 5-pillar program (ilmu, kemudahan, kasih, rezeki, warisan). 'Not promising moon and stars, but record.' Khaled launched BN machinery. Concrete program + machinery launch = improvement."
    },
    "Saiful Yazan Sulaiman (BN Johol incumbent)": {
        "score": 0.15, "trend": "improving", "alert": "none", "source_count": 5,
        "rationale": "rev17 +0.12 -> rev18 +0.15. Launches 'Iltizam Johol' — 5 commitments. 'Not promising moon and stars, but record that can be evaluated.' Continuation of 'Tekad Hebatkan Johol.' Concrete policy program. Improvement."
    },
    "Lenggeng (3-corner, Zool Amali defector)": {
        "score": -0.05, "trend": "stable", "alert": "none", "source_count": 3,
        "rationale": "rev17 0.00 -> rev18 -0.05. Classic marginal seat. BN held 1959-2018, lost to PH 2018, reclaimed 2023 by only 685 votes. ~75% Malay, 15.2% Indian. If multi-cornered, PN could benefit from split votes. Gauge of PAS/Bersatu/PN influence. Malay Mail analysis highlights risk. Marginal dip."
    },
    "Lukut (DAP vs MIPP, MCA ceded)": {
        "score": 0.05, "trend": "stable", "alert": "none", "source_count": 3,
        "rationale": "rev17 +0.05. DAP's Choo Ken Hwa dominated ~79% in 2018 and 2023. Within Port Dickson parliamentary seat — 7,000+ military early voters. 49.5% Chinese, 26.2% Indian, 22.7% Malay. Barometer for urban sentiment and military vote. Malay Mail analysis highlights military-vote significance."
    },
    "PH manifesto launch (20 Jul, continuity of Tok Min)": {
        "score": 0.35, "trend": "improving", "alert": "none", "source_count": 6,
        "rationale": "rev17 +0.32 -> rev18 +0.35. TODAY: PH to unveil NS PRN manifesto Monday night (20 Jul). Focus on kesinambungan pembangunan (development continuity) since 2018. Amirudin Shari, Klana Resort. Zaki: holistically detailed by top leadership. Improvement from launch-day confirmation."
    },
    "BN manifesto launch 24 Jul (DUN Linggi + Pertang)": {
        "score": 0.20, "trend": "improving", "alert": "none", "source_count": 5,
        "rationale": "rev17 +0.18 -> rev18 +0.20. UPCOMING (4 days) at DUN Linggi (N.32) + Pertang. HIGH-PRIORITY watch: JOINT BN-PN launch? Trajectory (merged machinery + joint manifesto + kongsi pentas) suggests HIGH likelihood. Improvement from trajectory."
    },
    "Anwar Ibrahim (PM, coalition manager)": {
        "score": 0.40, "trend": "declining", "alert": "priority", "source_count": 8,
        "rationale": "rev17 +0.45 -> rev18 +0.40. Warns ministers/deputy ministers/GLC holders: campaign on state issues only, do not attack unity govt colleagues during PRN, or resign. Discussed with Zahid and Fadillah. Kamil Munim claims BN-PN alliance aims to challenge his leadership. Discipline warning is defensive/controlling — unity govt under strain. Marginal decline from internal-friction signals."
    },
    "Day-1 campaign operations (evening dispatch, 19 permits)": {
        "score": 0.45, "trend": "improving", "alert": "none", "source_count": 4,
        "rationale": "rev17 +0.45. Day-2 midday: campaign operations continue. 19 permits approved. Evening Day-1 dispatch (18:00-20:00 MYT) covered. Anwar orders clean campaign. All sides pledge no personal attacks."
    },
    "Felda-UMNO ties (technocrat chairman)": {
        "score": -0.15, "trend": "stable", "alert": "none", "source_count": 2,
        "rationale": "NEW context. Ahmad Badri Zahir (non-Umno technocrat) chairs Felda. Analysts: unlikely to immediately weaken Umno-Felda ties, but could erode psychological link over time. Felda seats no longer automatic BN strongholds. Puad Zarkashi: could push Umno-PAS seat-sharing talks."
    },
}

# === NEW ENTRIES (from 0313 build, not in rev17) ===
new_entries = [
    # PIR-06
    {
        "entity": "BN-PN merged machinery (coalition operational arrangement)",
        "pir_tag": "PIR-06",
        "sentiment": "positive",
        "score": 0.55,
        "trend": "improving",
        "alert": "critical",
        "source_count": 4,
        "rationale": "NEW rev18. Hamzah: 'Kita telah gabungkan dua jentera daripada PN dan juga BN' — merged at leadership AND ground level. Candidates placed together with combined teams. 'Mampu mengambil alih Negeri Sembilan.' If successful, extend to PRU. [CRITICAL] PIR-06 entity: the coalition operational arrangement is now CONFIRMED operational. Positive [CRITICAL] — confirmed arrangement, not a fracture signal. Strengthens cooperation vector."
    },
    {
        "entity": "toksik PN narrative (Muhyiddin vs PAS)",
        "pir_tag": "PIR-06",
        "sentiment": "negative",
        "score": -0.80,
        "trend": "declining",
        "alert": "critical",
        "source_count": 7,
        "rationale": "NEW rev18 (replaces 'toxic PN' as the publicly-escalated version). Muhyiddin accuses PAS-led PN of 'toksik' and 'terpesong,' claiming PAS makes false allegations (fitnah) against Bersatu. Hamzah rebuts: 'Don't call PAS toxic, remember who helped you become PM.' First PUBLIC leader-to-leader Bersatu-vs-PAS/Wawasan warfare in hard-news (Sinar Harian 20 Jul). Director 'toxic PN' = [CRITICAL] rule. Intra-opposition warfare ESCALATED."
    },
    {
        "entity": "Hamzah claims PN name originated from him (brand ownership)",
        "pir_tag": "PIR-06",
        "sentiment": "negative",
        "score": -0.30,
        "trend": "declining",
        "alert": "priority",
        "source_count": 2,
        "rationale": "NEW rev18. Hamzah asserts PN name originated from him and two friends during the Mahathir era — PN is 'not Bersatu's exclusive property.' Brand-ownership dispute adds new dimension to Bersatu-PN fracture. Asserts PN identity separate from Bersatu. [PRIORITY] fracture-adjacent signal."
    },
    {
        "entity": "Noh Omar (party-hopping trail, blue-wave advocate)",
        "pir_tag": "PIR-06",
        "sentiment": "neutral",
        "score": -0.15,
        "trend": "stable",
        "alert": "priority",
        "source_count": 1,
        "rationale": "NEW rev18. Former Selangor Umno chief. Party-hopping trail: sacked by Umno (Jan 2023) -> joined Bersatu (Jul 2024) -> Bersatu Supreme Council (early 2025) -> quit Bersatu (Feb 2025, after 17 leaders sacked) -> rejoined Umno (Jun 7, 2025). Now advocates BN-PN 'blue wave' to Selangor/Putrajaya. [PRIORITY] — party-hopping trajectory documented; blue-wave amplifier."
    },
    {
        "entity": "PRU16 benchmark framing (Johari/KJ/Zahid/Hamzah)",
        "pir_tag": "PIR-06",
        "sentiment": "positive",
        "score": 0.35,
        "trend": "improving",
        "alert": "none",
        "source_count": 4,
        "rationale": "NEW rev18. Multi-leader: Johari (Umno VP): NS result is penanda aras (benchmark) for BN-PN cooperation. KJ: if formula works, extend to Selangor. Zahid: NS performance determines future alignment. Hamzah: if successful, 'insya-Allah kita akan teruskan kerjasama.' Strengthens 'makmal politik' narrative. [none] — strategic framing, positive."
    },
    {
        "entity": "Noh Omar blue wave to Selangor/Putrajaya",
        "pir_tag": "PIR-06",
        "sentiment": "positive",
        "score": 0.25,
        "trend": "improving",
        "alert": "none",
        "source_count": 1,
        "rationale": "NEW rev18. Noh Omar hopes BN-PN formula sparks 'blue wave' from Johor to NS to Selangor to Putrajaya. Cross-coalition expansion narrative. [none]."
    },
    {
        "entity": "UMNO-PAS tiada yang mustahil narrative",
        "pir_tag": "PIR-06",
        "sentiment": "positive",
        "score": 0.20,
        "trend": "improving",
        "alert": "none",
        "source_count": 1,
        "rationale": "NEW rev18. Sinar analysis: NS nomination day confirms BN-PAS understanding. Muafakat Nasional rupture (PAS chose PN) now reversed. 'In politics, nothing is impossible — today clash on stage, tomorrow sit at same table.' BN-PAS reconciliation narrative."
    },
    # PIR-16
    {
        "entity": "sasar bentuk kerajaan negeri (PH solo-governing bid)",
        "pir_tag": "PIR-16",
        "sentiment": "positive",
        "score": 0.30,
        "trend": "improving",
        "alert": "critical",
        "source_count": 4,
        "rationale": "NEW rev18. PH contesting all 36 NS seats solo — the ONLY coalition fielding candidates in every seat. Seeking 'stronger mandate' after April crisis (14 Umno ADUN + 5 PN ADUN attempted backdoor govt). Loke: 'We did not want this election.' Hard-news corroboration across FMT, Sinar, Malay Mail = [CRITICAL] per Director rule. PH-attributed (legitimate mandate bid), DISTINCT from Bersatu-attributed -0.80 (24-seat solo). Score positive (seeking stability) but [CRITICAL] tag per director phrase match + hard-news."
    },
    {
        "entity": "ada sesuatu yang tak kena dalam Kerajaan Perpaduan (KJ)",
        "pir_tag": "PIR-16",
        "sentiment": "negative",
        "score": -0.25,
        "trend": "declining",
        "alert": "priority",
        "source_count": 1,
        "rationale": "NEW rev18. KJ: BN choosing PAS cooperation at NS while in unity govt is 'isyarat sesuatu yang tidak kena.' PH blames UMNO for reform failures. BN need not leave unity govt yet — use NS to 'send signal to PH not to take UMNO/BN for granted.' FRICTION signal within unity govt. [PRIORITY]."
    },
    {
        "entity": "Anwar discipline warning (resign to attack unity partners)",
        "pir_tag": "PIR-16",
        "sentiment": "negative",
        "score": -0.15,
        "trend": "declining",
        "alert": "priority",
        "source_count": 3,
        "rationale": "NEW rev18. PM warns ministers/deputy ministers/GLC holders: campaign on state issues only, do not attack unity govt colleagues during PRN, or resign. Discussed with Zahid and Fadillah. Khaled: 'PM's budi bicara.' Mohamad Hasan: willing to leave Cabinet if directed. Defensive/controlling move = unity govt under strain. [PRIORITY]."
    },
    {
        "entity": "PKR Youth counterattack (Kamil Munim + Shahrul Adnan)",
        "pir_tag": "PIR-16",
        "sentiment": "negative",
        "score": -0.25,
        "trend": "declining",
        "alert": "priority",
        "source_count": 2,
        "rationale": "NEW rev18. Kamil Munim (PKR Youth chief): BN-PN alliance driven by political interest, not rakyat. Alleges Zahid wants PM post, building momentum to bring down Anwar. 'No permanent friends or enemies in politics, only interests.' Shahrul Adnan (Selangor PKR Youth deputy): urges PH Selangor to reassess ties with BN. Intra-unity-govt friction. [PRIORITY]."
    },
    {
        "entity": "Kamil Munim (PKR Youth chief)",
        "pir_tag": "PIR-16",
        "sentiment": "negative",
        "score": -0.20,
        "trend": "declining",
        "alert": "priority",
        "source_count": 1,
        "rationale": "NEW rev18. PKR Youth chief / political secretary to PM-Finance Minister. Claims BN-PN alliance aims to challenge Anwar's leadership. Alleges Zahid wants PM. 'No permanent friends or enemies in politics, only interests.' Counterattack narrative. [PRIORITY]."
    },
    {
        "entity": "Shahrul Adnan (Selangor PKR Youth deputy)",
        "pir_tag": "PIR-16",
        "sentiment": "negative",
        "score": -0.15,
        "trend": "declining",
        "alert": "priority",
        "source_count": 1,
        "rationale": "NEW rev18. Urges Selangor PH to reassess ties with BN after BN cooperated with PN in NS. 'If BN is free to work with PN, why should PH regard BN cooperation as beyond question?' Intra-unity-govt friction amplifier. [PRIORITY]."
    },
    {
        "entity": "Muhamad Akmal Saleh (Umno Youth chief, drop all ministers)",
        "pir_tag": "PIR-16",
        "sentiment": "negative",
        "score": -0.30,
        "trend": "declining",
        "alert": "priority",
        "source_count": 2,
        "rationale": "NEW rev18 (distinct from 'Akmal counter-escalation' entry). Umno Youth chief. Challenges PM to drop ALL ministers/deputy ministers from any party contesting against PH, not just BN. Escalating political pressure on unity govt discipline question. [PRIORITY]."
    },
    {
        "entity": "Hassan Karim (PKR Pasir Gudang, BN-PN normal)",
        "pir_tag": "PIR-16",
        "sentiment": "neutral",
        "score": -0.10,
        "trend": "stable",
        "alert": "none",
        "source_count": 1,
        "rationale": "NEW rev18. Pasir Gudang MP (PKR). Says BN-PN alliance is normal in Malaysian politics. 'If BN could work with PH after PH toppled BN in GE14, no reason BN can't cooperate with PN to wrest NS from PH.' Tells PH not to merungut. Intra-PH dissent. [none]."
    },
    {
        "entity": "gelombang biru (blue wave) narrative",
        "pir_tag": "PIR-16",
        "sentiment": "positive",
        "score": 0.40,
        "trend": "improving",
        "alert": "none",
        "source_count": 5,
        "rationale": "NEW rev18. Hamzah: 'gelombang biru' strength comes from penyatuan hati across party lines. Noh Omar: blue wave began Johor -> NS -> Selangor -> Putrajaya. Cross-party leaders (Hamzah, UMNO's Alwi, PAS Takiyuddin) sharing stage. Blue-wave narrative gaining multi-leader traction."
    },
    {
        "entity": "sole opposition / Bersatu solo narrative",
        "pir_tag": "PIR-16",
        "sentiment": "negative",
        "score": -0.55,
        "trend": "declining",
        "alert": "priority",
        "source_count": 3,
        "rationale": "NEW rev18. Bersatu contesting 24 seats under own logo — broken from PN, effectively a solo opposition party. Khaled: Bersatu 'set up to replace Umno' must be completely rejected. Bersatu candidates faced deposit losses in Johor. PN (PAS-led) now separate entity. [PRIORITY]."
    },
    {
        "entity": "gabungan lawan gabungan narrative",
        "pir_tag": "PIR-16",
        "sentiment": "neutral",
        "score": -0.10,
        "trend": "stable",
        "alert": "none",
        "source_count": 1,
        "rationale": "NEW rev18. Sinar Harian analysis: election competition shifting from 'parti lawan parti' to 'gabungan lawan gabungan' for political survival. NS PRN as most sengit election due to political realignment. Three coalitions: PH (solo/36), BN-PN (25+11), Bersatu (solo/24). [none]."
    },
    {
        "entity": "cabar mencabar ujian baharu Kerajaan Perpaduan",
        "pir_tag": "PIR-16",
        "sentiment": "negative",
        "score": -0.20,
        "trend": "declining",
        "alert": "priority",
        "source_count": 1,
        "rationale": "NEW rev18. Sinar analysis: Akmal's challenge to PM + AMH's call for BN ministers to resign = escalating political pressure. Blurring line between election competition and Cabinet responsibility. PM must balance discipline with multi-party reality. NS PRN as credibility benchmark for Anwar's administration. [PRIORITY]."
    },
    {
        "entity": "Siow Kong Choon (MCA Chennah challenger)",
        "pir_tag": "PIR-16",
        "sentiment": "neutral",
        "score": 0.05,
        "trend": "stable",
        "alert": "none",
        "source_count": 2,
        "rationale": "NEW rev18 (distinct from existing 'Siow Kong Choon (MCA NS Youth)' entry). MCA candidate challenging Loke in Chennah — straight fight (one-on-one) enabled by BN-PN understanding. Utusan analysis: test of BN-PN formula. Chennah 14,422 voters, 47.25% Malay, 42.68% Chinese. [none]."
    },
    {
        "entity": "MCA vs DAP in Chennah (BN-PN formula test)",
        "pir_tag": "PIR-16",
        "sentiment": "neutral",
        "score": -0.10,
        "trend": "declining",
        "alert": "priority",
        "source_count": 2,
        "rationale": "NEW rev18. BN-PN understanding creates one-on-one Loke vs Siow Kong Choon. Utusan analysis: test of whether BN-PN understanding can translate into votes. 47.25% Malay, 42.68% Chinese. Loke won 2023 by 2,200. [PRIORITY] — marquee battleground test."
    },
    {
        "entity": "Tengku Zafrul Abdul Aziz (Jana Wibawa testimony)",
        "pir_tag": "PIR-16",
        "sentiment": "neutral",
        "score": -0.10,
        "trend": "stable",
        "alert": "none",
        "source_count": 1,
        "rationale": "NEW rev18. Former Finance Minister. Testified that KESB was among 54 contractors given by Muhyiddin for Jana Wibawa projects via direct negotiation (Reka & Bina). KESB failed BPK first evaluation. [none]."
    },
    {
        "entity": "Ahmad Badri Zahir (Felda chairman, technocrat)",
        "pir_tag": "PIR-16",
        "sentiment": "neutral",
        "score": -0.10,
        "trend": "stable",
        "alert": "none",
        "source_count": 1,
        "rationale": "NEW rev18. New Felda chairman (non-Umno technocrat, ex-EPF chairman, chairs RHB Bank). Took over from Ahmad Shabery Cheek (Jun 30). Analysts: unlikely to immediately weaken Umno-Felda ties, but could erode psychological link over time. Felda seats no longer automatic BN strongholds. [none]."
    },
    {
        "entity": "Puad Zarkashi (Felda-UMNO ties warning)",
        "pir_tag": "PIR-16",
        "sentiment": "negative",
        "score": -0.20,
        "trend": "declining",
        "alert": "none",
        "source_count": 1,
        "rationale": "NEW rev18. Former Umno Supreme Council member. Says non-renewal of Ahmad Shabery's tenure and appointment of non-Umno successor could make it harder for Umno to win back Felda-linked seats lost to PN. Could push Umno-PAS seat-sharing talks. [none]."
    },
    {
        "entity": "Felda-UMNO ties (technocrat chairman impact)",
        "pir_tag": "PIR-16",
        "sentiment": "neutral",
        "score": -0.15,
        "trend": "stable",
        "alert": "none",
        "source_count": 2,
        "rationale": "NEW rev18. Ahmad Badri Zahir (non-Umno technocrat) chairs Felda. Analysts: unlikely to immediately weaken Umno-Felda ties, but could erode psychological link over time. Felda seats no longer automatic BN strongholds. [none]."
    },
    # PIR-07
    {
        "entity": "Six key seats (Malay Mail analysis)",
        "pir_tag": "PIR-07",
        "sentiment": "neutral",
        "score": 0.10,
        "trend": "stable",
        "alert": "none",
        "source_count": 1,
        "rationale": "NEW rev18. Malay Mail identifies six seats that tell the story: Rantau (Tok Mat stronghold), Chennah (Loke vs MCA), Linggi (MB vs Umno fortress), Lenggeng (marginal), Lukut (DAP/military), Nilai (5-corner/young voters). Analytical framing confirming priority-seat selection. [none]."
    },
    {
        "entity": "Mohd Faizal Ramli (BN Linggi, Umno fortress defender)",
        "pir_tag": "PIR-07",
        "sentiment": "neutral",
        "score": 0.10,
        "trend": "stable",
        "alert": "priority",
        "source_count": 2,
        "rationale": "NEW rev18. BN/Umno candidate for Linggi. Former NS exco member under unity govt pact who vacated position. Won Linggi in 2023 with 55.1% vs Bersatu's Zamri Md Said. Defending Umno's never-fallen fortress (since 1959) against caretaker MB. [PRIORITY] — marquee battleground."
    },
    {
        "entity": "J Arul Kumar (DAP Nilai incumbent, confident)",
        "pir_tag": "PIR-07",
        "sentiment": "positive",
        "score": 0.20,
        "trend": "stable",
        "alert": "none",
        "source_count": 1,
        "rationale": "NEW rev18. DAP incumbent for Nilai since 2013 (3 terms). Confident of retaining without BN — won ~10,000 votes in GE2022 without BN. 2023 majority: 10,889 vs PN. Five-cornered fight. Cites infrastructure, flood mitigation projects. Race-based narratives biggest challenge. [none]."
    },
    {
        "entity": "Danni Rais (PN Klawang, Bakri's cousin)",
        "pir_tag": "PIR-07",
        "sentiment": "neutral",
        "score": 0.10,
        "trend": "stable",
        "alert": "none",
        "source_count": 3,
        "rationale": "rev17 carried. PN challenger for Klawang. Cousin of PH incumbent Bakri Sawir. Three-cornered fight including Bersatu's Muhammad Adib Musa. Cordial cousin rivalry. [none]."
    },
    {
        "entity": "Muhammad Adib Musa (Bersatu Klawang)",
        "pir_tag": "PIR-07",
        "sentiment": "neutral",
        "score": -0.15,
        "trend": "stable",
        "alert": "none",
        "source_count": 2,
        "rationale": "rev17 carried. Bersatu candidate for Klawang. Third candidate in three-cornered fight vs Bakri Sawir (PH) and Danni Rais (PN). Bersatu as 3rd-force splitter. [none]."
    },
    {
        "entity": "Mohd Isa Abdul Samad (former MB, Linggi historical figure)",
        "pir_tag": "PIR-07",
        "sentiment": "neutral",
        "score": 0.05,
        "trend": "stable",
        "alert": "none",
        "source_count": 1,
        "rationale": "NEW rev18. Former NS MB. Represented Linggi for 2+ decades before moving to Bagan Pinang. Historical figure anchoring Linggi's status as Umno's oldest fortress (since 1959). [none]."
    },
    {
        "entity": "Sufian Maradzi (BN Seri Menanti, MB candidate)",
        "pir_tag": "PIR-07",
        "sentiment": "neutral",
        "score": 0.15,
        "trend": "stable",
        "alert": "none",
        "source_count": 2,
        "rationale": "rev17 carried. BN candidate for Seri Menanti. Named by Jalaluddin as potential MB candidate alongside Mohamad Hasan. 'Up to BN chairman to decide.' [none]."
    },
    {
        "entity": "Muhammad Zaki Md Sabri (PH NS operations director)",
        "pir_tag": "PIR-07",
        "sentiment": "neutral",
        "score": 0.15,
        "trend": "stable",
        "alert": "none",
        "source_count": 2,
        "rationale": "rev17 carried (as 'Muhammad Zaki Md Sabri (PH media secretariat chief)'). PH NS Operations director. Announces PH manifesto launch Monday night (20 Jul). Focus on development continuity since 2018. 889,490 voters. [none]."
    },
    {
        "entity": "April 19 royal-political crisis (NS trigger)",
        "pir_tag": "PIR-07",
        "sentiment": "negative",
        "score": -0.30,
        "trend": "stable",
        "alert": "priority",
        "rationale": "NEW rev18 (distinct from PIR-16 entry). Crisis sparked April 19: 4 undangs claimed Tuanku Muhriz removed as Yang di-Pertuan Besar. All 14 Umno ADUN withdrew support for MB Aminuddin. 14 Umno + 5 PN ADUN attempted backdoor govt. DUN dissolved 5 Jun. THE TRIGGER for Aug 1 NS PRN. [PRIORITY]."
    },
    {
        "entity": "Md Alwi Che Ahmad (Umno Supreme Council, cross-party stage)",
        "pir_tag": "PIR-06",
        "sentiment": "positive",
        "score": 0.20,
        "trend": "improving",
        "alert": "none",
        "source_count": 1,
        "rationale": "NEW rev18. Umno Supreme Council member. Shared stage with Hamzah and PAS sec-gen Takiyuddin at Seremban event — symbolising BN-PN-Wawasan 'gelombang biru' unity across party lines. Cross-party cooperation signal. [none]."
    },
    {
        "entity": "Affifi Aris (Umno Youth Kapar, extend formula)",
        "pir_tag": "PIR-06",
        "sentiment": "positive",
        "score": 0.15,
        "trend": "improving",
        "alert": "none",
        "source_count": 1,
        "rationale": "NEW rev18. Umno Youth Kapar chief. Wants BN-PN NS formula extended to Selangor. Says Zahid has heard grassroots aspirations. BN-PN could help recapture Kapar parliamentary seat. [none]."
    },
    {
        "entity": "Razali Abu Samah (Wawasan, ex-police, PN candidate)",
        "pir_tag": "PIR-06",
        "sentiment": "neutral",
        "score": 0.05,
        "trend": "stable",
        "alert": "none",
        "source_count": 2,
        "rationale": "NEW rev18 (distinct from existing 'Razali Abu Samah (PN/Wawasan N.13 Sikamat)'). Former Melaka deputy police chief. Wawasan candidate in NS PRN. Part of Wawasan strategy to capture police vote bloc through retired senior officers. [none]."
    },
    {
        "entity": "Hazani Ghazali (Wawasan, ex-Bukit Aman, police-vote strategy)",
        "pir_tag": "PIR-06",
        "sentiment": "neutral",
        "score": 0.10,
        "trend": "stable",
        "alert": "none",
        "source_count": 1,
        "rationale": "NEW rev18. Former Bukit Aman internal security director, first DG of Border Control Agency, led Sabah police (2020-2022) and Esscom (2017). Now Wawasan central leadership member targeting police votes. High-profile recruit for Wawasan police-vote strategy. [none]."
    },
    {
        "entity": "Teo Nie Ching (DAP Women, Madani continuity)",
        "pir_tag": "PIR-16",
        "sentiment": "positive",
        "score": 0.42,
        "trend": "improving",
        "alert": "none",
        "source_count": 3,
        "rationale": "rev17 carried. DAP Women's chief / Deputy Communications Minister / Kulai MP. Urges mandate for PH to continue Madani agenda. DAP won't give up after Johor setback — will muhasabah without sacrificing principles. Delivered speech in Mandarin with English translation. [none]."
    },
    {
        "entity": "Gobind Singh Deo (DAP national chairman)",
        "pir_tag": "PIR-16",
        "sentiment": "neutral",
        "score": 0.15,
        "trend": "stable",
        "alert": "none",
        "source_count": 2,
        "rationale": "rev17 carried. DAP national chairman. Present at PH dinner in Seremban alongside Loke, Nie Ching, and Cha Kee Chin. [none]."
    },
    {
        "entity": "Fadillah Yusof (DPM, Anwar discipline discussion)",
        "pir_tag": "PIR-06",
        "sentiment": "neutral",
        "score": 0.10,
        "trend": "stable",
        "alert": "none",
        "source_count": 2,
        "rationale": "NEW rev18 (distinct from PIR-07 'Fadillah' entry). Deputy PM. Anwar discussed campaign discipline warning with Zahid and Fadillah — ministers must not attack unity govt colleagues during PRN or resign. [none]."
    },
]

# === APPLY UPDATES ===
update_count = 0
for name, fields in updates.items():
    if name in lookup:
        idx = lookup[name]
        for k, v in fields.items():
            entries[idx][k] = v
        update_count += 1
    else:
        # Try partial match
        found = False
        for i, e in enumerate(entries):
            if name.lower() in e["entity"].lower() or e["entity"].lower() in name.lower():
                for k, v in fields.items():
                    entries[i][k] = v
                update_count += 1
                found = True
                break
        if not found:
            print(f"WARNING: Update target not found: {name}")

print(f"Applied {update_count} updates to existing entries")

# === ADD NEW ENTRIES ===
# Check for duplicates
added = 0
existing_names = set(e["entity"] for e in entries)
for ne in new_entries:
    if ne["entity"] not in existing_names:
        entries.append(ne)
        added += 1
    else:
        print(f"SKIP duplicate: {ne['entity']}")

print(f"Added {added} new entries")
print(f"Total entries: {len(entries)}")

# === COUNT ALERTS ===
critical_count = sum(1 for e in entries if e.get("alert") == "critical")
priority_count = sum(1 for e in entries if e.get("alert") == "priority")
none_count = sum(1 for e in entries if e.get("alert") == "none")

# === BUILD REV18 METADATA ===
now = datetime.utcnow()
generated_utc = now.strftime("%Y-%m-%dT%H:%M:%SZ")
# MYT = UTC+8
myt_hour = (now.hour + 8) % 24
myt_minute = now.minute
generated_myt = f"2026-07-20T{myt_hour:02d}:{myt_minute:02d}:00+08:00"
hhmm = f"{myt_hour:02d}{myt_minute:02d}"

rev18 = {
    "metadata": {
        "version": "revision-18",
        "date": "2026-07-20",
        "generated": generated_myt,
        "generated_utc": generated_utc,
        "tlp": "AMBER",
        "mission": "PRN Negeri Sembilan 2026 Sentiment Analysis",
        "agent": "PRN NS 2026 Sentiment Analysis Agent (cron)",
        "entity_build": "processed-entities/2026-07-20/entities-20260720-0313.json (81 entities, Day-2 midday extraction covering morning 01:11 + midday 02:20 scrape cycles; 30+ NS-specific priority articles from FMT BM+EN, Malay Mail, Utusan, Sinar Harian). Supersedes entities-20260720-0106.json (232 entities) used by rev17. SIGNIFICANT NEW CONTENT: BN-PN merged machinery CONFIRMED (leadership+ground); 'toksik' Bersatu-PAS PUBLIC escalation; 'Bersatu kacau daun' hard-news bilingual ELEVATED to CRITICAL; PH 'sasar bentuk kerajaan' solo bid; 'majoriti mudah' NOW DIRECTLY QUOTED; Wawasan police-vote strategy; Anwar discipline warning; PKR Youth counterattack; 6-key-seats Malay Mail analysis.",
        "prior_revision_file": "sentiment-analysis/2026-07-20/sentiment-20260720-1010.json",
        "prior_revision": "revision-17 (2026-07-20T10:10:00+08:00, 241 entities, 13 critical/54 priority/174 none), built on the 232-entity 0106 build",
        "score_convention": "SIGNED (-1.0 to +1.0). Negative = -1.0 to < -0.20; Neutral = -0.20 to +0.20 (marginal/mixed band); Positive = > +0.20 to +1.0.",
        "pir_weights": "PIR-06=2.0, PIR-16=1.8, PIR-07=1.3, non-priority=1.0",
        "critical_threshold": "Sharp sentiment shift >30% change for any PIR-06 entity; Bersatu sharp-negative internal-fracture signal = [CRITICAL]. PIR-16 CRITICAL if hard-news corroborates 'Bersatu exit imminent?' OR 'sasar bentuk kerajaan' OR viral amplification >50%.",
        "election_context": "PRN Negeri Sembilan 2026 - Campaign Day 2 (Nomination 18 Jul; Day-1 19 Jul; Day-2 20 Jul). Polling 1 Aug; early voting 28 Jul; BN manifesto launch 24 Jul (DUN Linggi + Pertang); PH manifesto launch 20 Jul (Amirudin Shari, Klana Resort). Electorate 889,490 (103 candidates, 36 seats; simple-majority threshold 19).",
        "director_cycle": "19 Jul 17:25 MYT (4th carry-forward) - 7th entity build (0313 midday cycle, Day-2)",
        "entity_count": len(entries),
        "critical_count": critical_count,
        "priority_count": priority_count,
        "none_count": none_count
    },
    "entities": entries,
    "trend_summary": {
        "revision": f"revision-18 (built on entities-20260720-0313.json, 81 entities, Day-2 midday, finalized ~{myt_hour:02d}:{myt_minute:02d} MYT 20 Jul = Day-2 midday)",
        "cycle_classification": "ACTIVE / HIGH-YIELD (Day-2 midday). The 0313 build (81 entities from morning 01:11 + midday 02:20 scrapes) is a HIGH-YIELD cycle with significant NEW developments across all three PIRs. Unlike rev17 (QUIET/LOW-YIELD, World Cup dominated), this cycle captures substantive Day-2 campaign coverage from FMT (BM+EN), Malay Mail, Utusan, and Sinar Harian. KEY ESCALATIONS: (1) 'Bersatu kacau daun' ELEVATED PRIORITY->CRITICAL (hard-news bilingual amplification >50%); (2) PH 'sasar bentuk kerajaan' solo-governing bid NEW CRITICAL (hard-news corroborated, director phrase match); (3) BN-PN merged machinery CONFIRMED at leadership+ground level (positive critical); (4) 'toksik' Bersatu-PAS fracture PUBLIC leader-to-leader warfare; (5) 'majoriti mudah' NOW DIRECTLY QUOTED by Loke. Total entries 241->263 (+22 new, ~40 updated). Critical 13->16 (+3). Priority 54->62 (+8).",
        "pir_06": {
            "verdict": "[CRITICAL CARRIED + NEW POSITIVE CRITICAL]. Bersatu sharp-negative internal-fracture signal CONFIRMED and now PUBLICLY ESCALATED (Muhyiddin 'toksik' vs Hamzah rebuttal, Sinar Harian hard-news). All 13 prior [CRITICAL] entities carried. NEW [CRITICAL]: BN-PN merged machinery (positive critical — confirmed arrangement). UPDATED: Muhyiddin -0.92->-0.93, Bersatu -0.88->-0.89, toxic PN -0.78->-0.80, gabung jentera +0.48->+0.58, Hamzah -0.20->-0.10 (improving), Wawasan -0.15->-0.05 (improving), PN +0.30->+0.38. NO PIR-06 entity crossed >30% sharp-shift threshold (marginal movements only).",
            "numeric_shift_check": "rev17 -> rev18 deltas: Muhyiddin -0.92->-0.93 (1%); Bersatu -0.88->-0.89 (1%); toxic PN -0.78->-0.80 (3%); Bersatu-PN fracture -0.89->-0.90 (1%); Khaled -0.32->-0.38 (19% — largest shift but <30% threshold); gabung jentera +0.48->+0.58 (positive, 21%); Hamzah -0.20->-0.10 (50% improvement — but from low base, not a >30% negative shift); Wawasan -0.15->-0.05 (67% improvement — positive). NO PIR-06 entity crossed >30% NEGATIVE sharp-shift threshold.",
            "bersatu_sharp_negative": "YES - CONFIRMED and now PUBLICLY ESCALATED. Muhyiddin calls PAS-led PN 'toksik' and 'terpesong'; Hamzah rebuts directly 'Muhyiddin could not have become PM without PAS.' First PUBLIC leader-to-leader Bersatu-vs-PAS/Wawasan warfare (Sinar Harian hard-news 20 Jul). Formal PN-MT expulsion notice still absent. Most likely path remains Bersatu voluntary 'lebih hebat' exit + solo-24 contesting.",
            "lebih_hebat_new_coalition_sentiment": "Carried -0.78 CRITICAL. No explicit mention in today's 0313 build. No formal launch. PRU16 realignment vehicle, hint/bayangan stage.",
            "sasar_bentuk_kerajaan_sentiment": "TWO versions now tracked: (1) Bersatu-attributed -0.80 CRITICAL (24 seats, exceeds 19 threshold) carried; (2) NEW PH-attributed +0.30 CRITICAL (36 seats solo, 23 target, hard-news FMT+Sinar+MalayMail). Director rule: hard-news 'sasar bentuk kerajaan' = CRITICAL. Both versions now [CRITICAL].",
            "wawasan_admission_sentiment": "IMPROVING -0.15->-0.05. Formally admitted to PN. Concrete candidate deployment: retired senior police officers (Hazani Ghazali, Razali Abu Samah) targeting 200,000+ police votes. Wawasan+PAS bloc stabilizes PN vs Bersatu exit.",
            "ros_complaint_disruption_sentiment": "Carried -0.62 CRITICAL. No explicit RoS mention in today's build.",
            "pdm_klawang_reopen_sentiment": "Carried -0.22 PRIORITY WATCH. No explicit PDM mention in today's build. Jalaluddin expects reopen 1-2 days (carried). Watch for reopen confirmation.",
            "toxic_termination_pecat_kuorum_lebih_hebat_trajectory": "'toxic PN' -0.78->-0.80 CRITICAL (PUBLIC escalation). 'lebih hebat' -0.78 CRITICAL (carried). 'kuorum' -0.65 CRITICAL (carried). 'pecat' (Tang Jay Son) -0.40 CRITICAL (carried). Khaled 'KO habis' -0.56->-0.60 PRIORITY (hard-news bilingual). 'Bersatu kacau daun' -0.58->-0.68 ELEVATED to CRITICAL.",
            "threshold_status": "Formal pecat/termination NOT crossed. 7+ converging [CRITICAL] triggers; formal PN-MT expulsion notice absent. PUBLIC escalation of 'toksik' fracture (Muhyiddin vs Hamzah) is the most significant fracture development this cycle. BN-PN cooperation vector STRENGTHENED (merged machinery confirmed, +0.58).",
            "bn_pn_cooperation_stages": "4-stage BN-PN cooperation formalization STRENGTHENED + CONFIRMED: (0) Zambry-Samsuri PD meeting [leadership precursor], (1) seat-swap, (2) gabung-jentera machinery merger +0.48->+0.58 (CONFIRMED leadership+ground), (3) manifesto bersepadu +0.48->+0.50, (4) kongsi pentas +0.40. NEW: PRU16 benchmark framing +0.35 (Johari/KJ/Zahid/Hamzah). MB-concession-to-BN +0.15->+0.22. WATCH: 24 Jul BN manifesto launch — JOINT BN-PN event?",
            "offsetting_signals": "Cooperation signals STRENGTHENED: gabung-jentera +0.58, joint-manifesto +0.50, gelombang biru +0.40, PRU16 benchmark +0.35, MB-concession +0.22, PN +0.38, BN +0.42. Fracture signals also escalated: toxic PN -0.80, Bersatu kacau daun -0.68 [CRITICAL]. Both vectors intensifying simultaneously.",
            "hamzah_pn_brand_claim_new": "NEW [PRIORITY]: Hamzah claims PN name originated from him — PN is 'not Bersatu's exclusive property.' Brand-ownership dispute adds new fracture dimension. Asserts PN identity separate from Bersatu."
        },
        "pir_16": {
            "verdict": "[CRITICAL CARRIED + 2 NEW CRITICAL]. 'sasar bentuk kerajaan' (both Bersatu and PH versions) persist at CRITICAL. NEW CRITICAL: 'Bersatu kacau daun' ELEVATED PRIORITY->CRITICAL (hard-news bilingual amplification >50%). 'sasar bentuk kerajaan' (PH solo) NEW CRITICAL (hard-news corroborated, director phrase match). Viral amplification >50% FIRED for 'Bersatu kacau daun' (FMT BM+EN simultaneous = significant volume increase).",
            "viral_amplification_gt50": "FIRED for 'Bersatu kacau daun' (Khaled, FMT BM+EN 20 Jul) — FIRST time this PIR-16 narrative gets simultaneous BM+EN hard-news amplification = >50% volume increase. ELEVATED to [CRITICAL]. Other narratives: 'gelombang biru' gaining multi-leader traction but not >50% volume; 'ada sesuatu yang tak kena' (KJ) new but single-source.",
            "hard_news_corroboration_bersatu_exit_or_sasar": "FIRED (carried + NEW): 'sasar bentuk kerajaan' Bersatu-attributed -0.80 CRITICAL (MalaysiaGazette+Sinar) carried; NEW PH-attributed +0.30 CRITICAL (FMT+Sinar+MalayMail 20 Jul). 'Bersatu exit imminent?' mkini framing remains PRIORITY (not hard-news corroborated).",
            "bersatu_kacau_daun_sentiment": "ELEVATED -0.58 [PRIORITY] -> -0.68 [CRITICAL]. Khaled 'Bersatu hanya kacau daun' + 'KO habis-habis' now hard-news BILINGUAL (FMT BM+EN 20 Jul). Director rule: viral amplification >50% = [CRITICAL]. Challenges 'penyatuan undi Melayu' (+0.15->+0.22 improving). Frames Bersatu as splitter/nuisance, not legitimate opposition.",
            "sasar_vs_mb_after_prn_vs_joint_manifesto_vs_kongsi_pentas": "4-way tension INTENSIFIED: 'sasar bentuk kerajaan' Bersatu -0.80 CRITICAL vs 'sasar bentuk kerajaan' PH +0.30 CRITICAL (NEW) vs 'MB after PRN' +0.22 (improving) vs 'BN-PN joint manifesto' +0.50 vs 'gabung jentera' +0.58. Both Bersatu AND PH now running solo-governing-bid narratives; BN-PN cooperation vector at strongest point.",
            "makmal_politik_sentiment": "+0.25->+0.32 improving. MULTI-LEADER: Johari (benchmark), KJ (extend to Selangor), Hamzah (continue), Zahid (determines alignment). Utusan: 'Negeri Sembilan penentu kerjasama PRU16.' Strengthening.",
            "bipartisan_clean_campaign_convergence": "+0.42->+0.44 improving. Anwar discipline warning reinforces. Mohamad Hasan: 'BN never burukkan.' Loke avoids Rantau. Clean-campaign norms strengthening through Day-2.",
            "mca_biggest_loser_and_rebuttal_trajectory": "-0.48->-0.50 declining. Chennah one-on-one (Loke vs Siow) = test of BN-PN formula (Utusan). MCA rebuttal = containment. Defensive deepening.",
            "majoriti_mudah_vs_not_taking_for_granted": "'majoriti mudah' NOW DIRECTLY QUOTED by Loke: 19 = 'majoriti mudah' (thin), 'apa sahaja boleh berlaku.' 23 = safe. This is PH DEFENCE (not BN confidence). 'not taking for granted' active via Nazri. Loke 'PH sasar 23 kerusi' +0.27->+0.30 improving.",
            "resign_narrative_chain": "Carried + Anwar discipline warning (NEW) adds containment. Chain: AMH -> Anwar firewall -> Tok Mat ready -> Akmal conditional -> Hassan Karim dissent -> Khaled PM-discretion. Anwar 20 Jul warning: 'resign to attack unity partners' reinforces firewall from PM side.",
            "ada_sesuatu_yang_tak_kena_new": "NEW [PRIORITY] -0.25. KJ: BN choosing PAS cooperation while in unity govt signals 'something wrong.' BN should stay in unity govt but use NS to 'send signal to PH.' Unity-govt friction signal.",
            "anwar_discipline_warning_new": "NEW [PRIORITY] -0.15. PM warns ministers not to attack coalition colleagues or resign. Discussed with Zahid and Fadillah. Defensive/controlling = unity govt under strain. Reinforces resign-to-attack firewall.",
            "pkr_youth_counterattack_new": "NEW [PRIORITY] -0.25. Kamil Munim: BN-PN aims to challenge Anwar's leadership; Zahid wants PM. Shahrul Adnan: reassess BN ties. Intra-unity-govt friction."
        },
        "pir_07": {
            "verdict": "NO incumbent/leading-candidate drop >20%. NEW [CRITICAL]: N.32 Linggi elevated to critical (high-stakes MB-vs-fortress battle + BN manifesto 24 Jul watch). Six key seats (Malay Mail analysis) confirms priority-seat selection. Day-2 midday campaign coverage active.",
            "incumbent_drop_gt20": "NOT DETECTED. Aminuddin +0.62->+0.58 (6% decline, <20%); Bakri Sawir +0.45->+0.48 (improving); Tok Mat +0.62->+0.64 (improving); Saiful Yazan +0.12->+0.15 (improving). No incumbent drop >20%.",
            "pertang_derhaka_friction": "Carried [PRIORITY] -0.20->-0.15. 'Derhaka' language NOT found in today's build (not escalated). Jalaluddin thanks PN for MB concession (positive). BN manifesto launch 24 Jul here. Active from prior; contained today.",
            "pdm_klawang_shutdown_reopen_impact": "Carried [PRIORITY WATCH] -0.22. No explicit PDM mention in today's build. Klawang seat covered (cousins rivalry) but PDM-level disruption not found. Watch for reopen.",
            "n14_defector_intensification": "NOT DETECTED. N.14 Ampangan -0.15->-0.10 (improving from merged-machinery + joint-majlis). Hamzah held joint majlis with PN candidates + BN + PAS. Defector-framing NOT intensifying.",
            "bn_manifesto_launch_24_jul": "UPCOMING (4 days) at DUN Linggi (N.32) + Pertang. HIGH-PRIORITY watch: JOINT BN-PN launch? Trajectory (merged machinery +0.58 + joint manifesto +0.50 + kongsi pentas +0.40 + PRU16 benchmark +0.35) suggests HIGH likelihood.",
            "ph_manifesto_launch_20_jul": "TODAY (20 Jul), Amirudin Shari, Klana Resort. +0.32->+0.35 improving. Focus on kesinambungan pembangunan. Watch for Day-2 evening coverage.",
            "evening_day1_to_day2_midday_dispatch": "Day-2 midday: 6-key-seats Malay Mail analysis, cousins Klawang, Hamzah joint majlis Ampangan+Sikamat, Johol Iltizam launch, Pertang MB concession, Nilai 5-corner detail, Linggi fortress analysis. Active campaign coverage.",
            "n32_linggi_critical_new": "NEW [CRITICAL]: N.32 Linggi elevated. Aminuddin (PH caretaker MB) vs Mohd Faizal (BN) at Umno's oldest fortress (since 1959). MB challenges Umno stronghold = highest symbolism. BN manifesto 24 Jul here. Aminuddin: 'MB status not an advantage — only caretaker.' Loke defends: 'not corrupt.'",
            "n19_johol_corroboration": "+0.15->+0.20 improving. Saiful Yazan 'Iltizam Johol' 5-pillar program (ilmu, kemudahan, kasih, rezeki, warisan). 'Not promising moon and stars.' Khaled BN machinery launch. Concrete policy program."
        },
        "collection_limitations": [
            "rev18 ingests the 81-entity 0313 build (Day-2 midday, covering morning 01:11 + midday 02:20 scrapes). ACTIVE/HIGH-YIELD cycle with 22 new entries + ~40 updated entries. Significantly more substantive than rev17 (QUIET/World Cup dominated).",
            "0313 build is a FOCUSED extraction (81 entities from 30+ NS-specific priority articles), NOT a comprehensive 232-entity build. Rev18 carries forward all 241 rev17 entries and applies 0313-derived updates/additions.",
            "Carry-forward flags NOT corroborated in 0313 build: PDM Klawang shutdown/reopen, 'derhaka' Pertang explicit language, RoS complaint, 'lebih hebat' explicit mention, BN manifesto 24 Jul DUN Linggi confirmation. All carried from prior cycles.",
            "gnews protobuf URLs remain curl-unresolvable (19th consecutive cycle). FMT direct URLs intermittently 404.",
            "Score convention SIGNED per mission directive. PIR weights PIR-06=2.0, PIR-16=1.8, PIR-07=1.3.",
            f"Alert-count change rev17->rev18: critical 13 -> {critical_count} (+{critical_count-13}); priority 54 -> {priority_count} (+{priority_count-54}); none 174 -> {none_count} (+{none_count-174}). Total 241 -> {len(entries)} (+{len(entries)-241})."
        ],
        "next_actions": [
            "PIR-06 (HIGHEST): Track PUBLIC 'toksik' fracture escalation — does Muhyiddin/Hamzah warfare intensify at Day-2 ceramah? Monitor 'Bersatu kacau daun' CRITICAL — does it gain further Day-2 traction? Watch 24 Jul BN manifesto launch — JOINT BN-PN event? Monitor PDM Klawang reopen.",
            "PIR-16 (HIGHEST): Track 'Bersatu kacau daun' CRITICAL amplification — does it spread beyond FMT? Watch 'sasar bentuk kerajaan' (PH) — does PH's solo-36 messaging intensify? Track Anwar discipline warning impact — do ministers comply? Watch PKR Youth counterattack — does it draw BN response? Watch 'majoriti mudah' at BN manifesto 24 Jul.",
            "PIR-07: Capture Day-2 evening ceramah for T1 seats — Klawang (cousins + PDM reopen), Linggi [CRITICAL] (Aminuddin + BN manifesto 24 Jul), Chennah (Loke vs Siow '50-50'), Rantau (Tok Mat), Pertang (derhaka contained), Johol (Iltizam program). Watch Nilai 5-corner + Lenggeng marginal.",
            "Backfill the 20260716 sentiment-analysis 1-day gap. Reconcile folder migration (hyphenated 2026-07-19/20 vs non-hyphenated 20260719)."
        ],
        "delta_vs_rev17": {
            "new_entities_rev18": [
                "BN-PN merged machinery (coalition operational arrangement) - [NEW PIR-06, CRITICAL, +0.55, improving; Hamzah confirms merged at leadership+ground]",
                "toksik PN narrative (Muhyiddin vs PAS) - [NEW PIR-06, CRITICAL, -0.80, declining; PUBLIC leader-to-leader warfare, Sinar Harian]",
                "sasar bentuk kerajaan negeri (PH solo-governing bid) - [NEW PIR-16, CRITICAL, +0.30, improving; PH 36 seats solo, hard-news FMT+Sinar+MalayMail]",
                "Hamzah claims PN name originated from him - [NEW PIR-06, PRIORITY, -0.30, declining; brand-ownership dispute]",
                "Noh Omar (party-hopping trail, blue-wave) - [NEW PIR-06, PRIORITY, -0.15, stable]",
                "PRU16 benchmark framing (Johari/KJ/Zahid/Hamzah) - [NEW PIR-06, +0.35, improving]",
                "ada sesuatu yang tak kena (KJ) - [NEW PIR-16, PRIORITY, -0.25, declining]",
                "Anwar discipline warning - [NEW PIR-16, PRIORITY, -0.15, declining]",
                "PKR Youth counterattack (Kamil+Shahrul) - [NEW PIR-16, PRIORITY, -0.25, declining]",
                "gelombang biru (blue wave) narrative - [NEW PIR-16, +0.40, improving]",
                "sole opposition / Bersatu solo narrative - [NEW PIR-16, PRIORITY, -0.55, declining]",
                "gabungan lawan gabungan narrative - [NEW PIR-16, -0.10, stable]",
                "cabar mencabar ujian baharu Kerajaan Perpaduan - [NEW PIR-16, PRIORITY, -0.20, declining]",
                "Six key seats (Malay Mail analysis) - [NEW PIR-07, +0.10, stable]",
                "Mohd Faizal Ramli (BN Linggi) - [NEW PIR-07, PRIORITY, +0.10, stable]",
                "J Arul Kumar (DAP Nilai) - [NEW PIR-07, +0.20, stable]",
                "April 19 royal-political crisis - [NEW PIR-07, PRIORITY, -0.30, stable]",
                "Hazani Ghazali (Wawasan police-vote) - [NEW PIR-06, +0.10, stable]",
                "+ others (Md Alwi, Affifi Aris, Razali Abu Samah, Puad Zarkashi, Ahmad Badri Zahir, Tengku Zafrul, etc.)"
            ],
            "revised_entities_rev18": [
                "Muhyiddin Yassin: -0.92->-0.93 (PUBLIC 'toksik' escalation); source_count 11->13",
                "Bersatu: -0.88->-0.89 (hard-news 'kacau daun' bilingual); source_count 12->14",
                "toxic PN: -0.78->-0.80 (PUBLIC escalation); source_count 6->8",
                "gabung jentera: +0.48->+0.58 (CONFIRMED leadership+ground); source_count 4->6",
                "Hamzah Zainudin: -0.20->-0.10 (improving; leads merged machinery + PN brand claim); source_count 4->8",
                "Wawasan: -0.15->-0.05 (improving; police-vote strategy); source_count 3->5",
                "PN: +0.30->+0.38 (improving; merged machinery + brand assertion); source_count 5->7",
                "Khaled Nordin: -0.32->-0.38 (hard-news bilingual 'kacau daun'); source_count 5->7",
                "Bersatu kacau daun: -0.58 [PRIORITY] -> -0.68 [CRITICAL] (hard-news bilingual >50% amplification)",
                "Aminuddin Harun: +0.62->+0.58 (caretaker no-advantage); source_count 10->12",
                "N.32 Linggi: +0.35->+0.30 [CRITICAL] (high-stakes battle)",
                "majoriti mudah: 0.00->-0.10 (NOW DIRECTLY QUOTED by Loke)",
                "penyatuan undi Melayu: +0.15->+0.22 (improving; Hadi Rasulullah model)",
                "makmal politik: +0.25->+0.32 (multi-leader corroboration)",
                "Anwar Ibrahim: +0.45->+0.40 (discipline warning + PKR Youth challenge)"
            ],
            "unchanged_critical_entities": [
                "lebih hebat -0.78 CRITICAL (carried), kuorum -0.65 CRITICAL (carried), RoS -0.62 CRITICAL (carried), pecat Tang Jay Son -0.40 CRITICAL (carried), Kiandee -0.25 CRITICAL (carried), PN Supreme Council -0.55 CRITICAL (carried), Bersatu MPT -0.72 CRITICAL (carried), sasar bentuk kerajaan (Bersatu) -0.80 CRITICAL (carried)."
            ],
            f"alert_count_change": f"critical 13 -> {critical_count} (+{critical_count-13}); priority 54 -> {priority_count} (+{priority_count-54}); none 174 -> {none_count} (+{none_count-174}). Total 241 -> {len(entries)} (+{len(entries)-241})."
        }
    },
    "generated_at": generated_myt,
    "source_entity_file": "entities-20260720-0313.json",
    "prior_revision": "revision-17 (sentiment-20260720-1010.json)"
}

# === WRITE OUTPUT ===
output_path = f"/home/p62operator/.openclaw/workspace-ns/04-DATA-AND-SOURCES/sentiment-analysis/2026-07-20/sentiment-20260720-{hhmm}.json"
with open(output_path, "w", encoding="utf-8") as f:
    json.dump(rev18, f, indent=2, ensure_ascii=False)

print(f"\n=== REV18 BUILT ===")
print(f"Output: {output_path}")
print(f"Total entries: {len(entries)}")
print(f"Critical: {critical_count}")
print(f"Priority: {priority_count}")
print(f"None: {none_count}")
print(f"Generated: {generated_myt}")
