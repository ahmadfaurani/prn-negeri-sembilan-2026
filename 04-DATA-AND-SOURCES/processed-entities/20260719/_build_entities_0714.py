#!/usr/bin/env python3
"""
PRN NS 2026 Entity Extraction Agent — Cycle 0714 build script.
Merges NEW entities from collection cycles 20260719_051226 and 20260719_064654
into the prior extraction (entities-20260719-0507.json, 167 entities covering
cycles 011915/024042/034922) and writes entities-20260719-0714.json.

New full-text sources ingested this build:
  - FMT RSS (content:encoded) — 19 full-text articles (NEW SOURCE, largest gain)
  - NST WordPress feed (content:encoded) — 7 full-text articles
  - Astro Awani direct (berita-politik slug) — 3 full-text articles
  - mkini direct — 1 paywalled preview (Zan Azlee indicator v2)
  - gnews headline-intel — 10 items
"""
import json
from pathlib import Path
from datetime import datetime, timezone, timedelta

BASE = Path(__file__).parent
PRIOR = BASE / "entities-20260719-0507.json"
OUT = BASE / "entities-20260719-0714.json"

MYT = timezone(timedelta(hours=8))
now_utc = datetime.now(timezone.utc)
now_myt = now_utc.astimezone(MYT)
ts_utc = now_utc.strftime("%Y-%m-%dT%H:%M:%S+00:00")
ts_myt = now_myt.strftime("%Y-%m-%dT%H:%M")
file_id = f"entities-20260719-{now_utc.strftime('%H%M')}"

with PRIOR.open("r", encoding="utf-8") as f:
    data = json.load(f)

prior_entities = data["entities"]
# Index by entity name for upsert
by_name = {e["entity"]: e for e in prior_entities}

# ----------------------------------------------------------------------------
# CONTEXT UPDATES for existing entities (new full-text evidence strengthens)
# ----------------------------------------------------------------------------
context_updates = {
    "Muhyiddin Yassin": (
        "Bersatu president; PN chairman. PIR-06 CRITICAL figure — now FULL TEXT via FMT "
        "('Bersatu must survive as lone opposition', 18 Jul 16:52 MYT): frames Bersatu as 'country's "
        "only credible opposition'; PN's BN arrangement means PN 'indirectly supports government.' "
        "FMT 19 Jul 09:00 MYT: 'Muhyiddin said the party will form a new coalition after the state "
        "election, hinting at a PN exit' — STRONGEST pre-threshold PIR-06 signal. Also accuses "
        "Umno/BN of 'charade to deceive the Malays' re ummah/Malay unity; claims Bersatu 'free of "
        "all this charade' + committed to anti-kleptocracy/1MDB founding struggle. Original: subject "
        "of 'toxic PN' claim (dismissed by Hadi); 'Bersatu to use own logo for NS polls' (24 seats)."
    ),
    "Hadi Awang": (
        "PAS president. PIR-06 CRITICAL — now FULL TEXT via FMT ('Hadi denies PAS made PN toxic, "
        "blames Bersatu instead', 18 Jul 12:48 MYT): 'rift caused by Bersatu's misconduct within PN'; "
        "says Bersatu new-coalition plan 'up to his former ally'; wants to EXPAND BN-PN cooperation "
        "NATIONWIDE. NST full text (19 Jul 14:03 MYT): calls for Malay-Muslim unity with 'non-extreme' "
        "partners incl MCA, MIC, DHPP; reject 'unnatural Malay groups with DAP.' FMT BM (19 Jul 09:30): "
        "'Bukan retorik' — PN-BN ties 'lebih daripada berkahwin' (more than marriage). Jempol nomination "
        "(Serting, Palong, Jeram Padang, Bahau). PAS severed political ties with Bersatu June 8."
    ),
    "Ronald Kiandee": (
        "Bersatu VP. PIR-06 CRITICAL precursor. ORIGINAL: 'PN has grounds (asas kukuh) to remove "
        "Bersatu' (call, not formal notice). NEW THIS CYCLE (NST headline-intel, 19 Jul): ESCALATION — "
        "'Kiandee asks Muhyiddin if Bersatu Supreme Council still has quorum' — from 'grounds to "
        "remove' to 'is the decision-making body even functional?' (implying mass exits hollowed it out). "
        "Director-flagged 'pecat'-type signal; threshold still NOT crossed."
    ),
    "toxic PN claim": (
        "CRITICAL director-flagged 'toxic PN' entity — now FULL TEXT confirmed via FMT (18 Jul 12:48 MYT). "
        "Attributed to Muhyiddin (PAS making PN toxic), DENIED by Hadi who counter-accuses Bersatu "
        "('rift caused by Bersatu's misconduct within PN'). Claim/counter-claim exchange is the "
        "strongest internal-rupture discourse signal. Muhyiddin had accused PAS of 'baseless allegations "
        "and defamatory claims'; cited Perlis political crisis (MB post PAS→Bersatu)."
    ),
    "PN has grounds to remove Bersatu": (
        "CRITICAL director-flagged 'pecat'-type signal. Kiandee's 'asas kukuh' call (precursor). "
        "NEW THIS CYCLE: Kiandee ESCALATED to questioning whether Bersatu Supreme Council still has "
        "quorum (NST headline-intel, 19 Jul) — implies mass exits hollowed out the decision body. "
        "Threshold for formal PN-MT removal still NOT crossed."
    ),
    "sole opposition": (
        "PRIORITY director-flagged PIR-16 narrative — now FULL TEXT via FMT Muhyiddin (18 Jul 16:52 MYT): "
        "'Bersatu must survive as lone opposition'; 'no longer a credible party to check and balance "
        "government policies'; PN's BN arrangement means PN 'indirectly supports the government.' "
        "Bersatu exit-from-PN question (mkini SNAPSHOT 18 Jul 18:00) + 24 own-logo seats reframe "
        "opposition bloc identity. Muhyiddin says Bersatu 'must survive' to fill the 'huge vacuum.'"
    ),
    "Bersatu goes solo under own logo": (
        "PIR-06 dominant operational-split narrative — now FULL TEXT confirmed across FMT (x4), NST, "
        "Awani. Muhyiddin: Bersatu to use own logo for NS polls. 24 own-logo seats. Breaks PN state "
        "consensus. PAS severed political ties with Bersatu June 8 (FMT); both remain in PN. PN says "
        "move 'expected.' Strongest operational-split confirmation; NOT a formal expulsion."
    ),
    "Bersatu": (
        "Parti Pribumi Bersatu Malaysia. Operational split FULL TEXT confirmed: 24 own-logo seats, "
        "broke PN state consensus. PAS severed political ties June 8 (FMT) — both remain in PN. "
        "Subject of Kiandee removal call + quorum question + 'toxic PN' claim-counterclaim. Ridzuan "
        "Ahmad quit. Analysts (FMT full text): Lau Zhe Wei (IIUM) advises quit PN + take Gerakan/MIPP; "
        "Azeem Fazwan (USM) expects wipeout; Azmil Tayeb (USM) — 'all people see is infighting.'"
    ),
    "PN-BN understanding NOT merger": (
        "PIR-16 DOMINANT official-framing narrative — now FULL TEXT corroborated across 3 sources. "
        "Wee Ka Siong (MCA, FMT 18 Jul): 'cooperation does not amount to an alliance... each party "
        "upholds ideological principles... checks and balances.' Mohd Isam Mohd Isa (Tampin Umno, NST "
        "19 Jul 11:59): 'merely an understanding to face the election, not a political merger'; BN-MCA/MIC "
        "relationships 'remain intact.' Zahid: 'merely an understanding, no agreements.' Hadi: 'lebih "
        "daripada berkahwin' but formal ties 'dinilai dari semasa ke semasa.'"
    ),
    "MCA biggest loser": (
        "PIR-16 PRIORITY viral-amplifier narrative — now FULL TEXT via FMT EN+BM (12:26 MYT EN, 13:30 MYT BM). "
        "Loke (after Pasar Besar Seremban walkabout): MCA 'biggest loser' — surrendered Lobak, Mambau, "
        "Lukut to PN. MCA contesting 7 seats (mostly straight fights, except Nilai/Temiang/Rahang where "
        "Bersatu also contests). Loke mocks: 'I want to thank Wee Ka Siong for being so generous.' "
        "BN-PN pact = biggest PH challenge (avoids Malay vote-split, allows vote transfers). Viral-risk: "
        "MCA rebuttal watch (Wee/Mah response)."
    ),
    "MB after PRN": (
        "PRIORITY director-flagged PIR-16 narrative — now FULL TEXT confirmed via FMT (Jalaluddin Alias, "
        "18 Jul): 'BN to decide NS MB candidate only if it wins polls'; 'several leaders capable of "
        "helming the incoming administration'; final decision rests with coalition leadership. "
        "Jalaluddin among those touted as potential MB. Aminuddin (outgoing MB) moved to Linggi; if PH "
        "loses, MB question opens. Utusan rencana frames Aminuddin seat-move + adat-crisis as MB-credibility referendum."
    ),
    "penyatuan undi Melayu": (
        "PRIORITY director-flagged PIR-16 narrative — now FULL TEXT corroborated. Kosmo: 'memaksimumkan "
        "pengundian Melayu.' NEW: Hadi (NST 14:03 MYT) 'Malay-Muslim unity with non-extreme partners' + "
        "reject 'unnatural Malay groups with DAP.' FMT akar umbi (19 Jul): grassroots 'penyatuan ummah' "
        "framing — 'Penyatuan ummah inilah yang diharapkan oleh akar umbi Umno.' Muhyiddin counters: "
        "'charade to deceive the Malays.' Tok Mat: 'safeguard the future of race and religion.'"
    ),
    "N.28 Klawang": (
        "PIR-07 highest-priority battleground (director list) — candidate detail NOW RECOVERED via Awani "
        "full text (Day-1 campaign, 19 Jul 12:11 MYT). 3-cornered: PH incumbent Datuk Bakri Sawir vs "
        "PN's Danni Rais (Bakri's COUSIN) vs Bersatu's Muhammad Adib Musa. 13,355 registered voters. "
        "Day-1: both cousins campaigned at Pasar Minggu Kuala Klawang (Jelebu) simultaneously — met "
        "peacefully, joked, no provocation. Bakri took down flags after Majlis Daerah Jelebu warning. "
        "Mature-campaign framing. HIGHEST PIR-07 value this cycle."
    ),
    "N.27 Chembong": (
        "PIR-07 highest-priority battleground (director list) — candidate detail NOW RECOVERED via FMT "
        "Tok Mat article (18 Jul). Straight fight: BN's Zaifulbahri Idris (since 2008; 2023 maj 4,335) "
        "vs PH's Danish Nazran Murad. (Prior cycle: candidate detail not recovered — now resolved.)"
    ),
    "Paroi": (
        "Urban seat. CORRECTION/CLARIFICATION: FMT Tok Mat article (18 Jul) reports 3-CORNERED: PAS/PN "
        "Kamarul Ridzuan Mohd Zain (incumbent, 2023 maj 5,539) vs PH Ahmad Shahir Mohd Shah vs Bersatu's "
        "Nazree Yunus. (Malay Mail nomination lineup described Paroi as straight fight Amanah vs PAS — "
        "discrepancy; FMT is more detailed/recent. 3-cornered retained as lead.)"
    ),
    "Pertang": (
        "BN bigwig Jalaluddin Alias retains seat. CLARIFICATION via FMT (18 Jul): 3-WAY contest — "
        "Jalaluddin (BN, seeking 3rd term, touted as potential MB) vs PH's Umry Abdul Khois vs Bersatu's "
        "Faizal Fadli Idrus. Falls under Jelebu parliamentary constituency (Jalaluddin MP since 2018)."
    ),
    "Kota": (
        "3-cornered BN stronghold. FMT confirms: BN Suhaimi Aini (incumbent; 2023 maj 135 votes — RAZOR "
        "MARGIN, highest-risk marginal; never left Umno since 1959) vs PH Allif Ibrahim vs Bersatu Akmal "
        "Noradzmi Abd Rahim."
    ),
    "Rantau": (
        "Marquee straight fight. FMT full text (18 Jul): Tok Mat (Mohamad Hasan, Umno dep president / FM / "
        "ex-MB 2004-2018 / 5 terms since 2004; 2023 maj 10,280) vs PH Dr Azizul Hakim Mahdi. Mixed seat, "
        "Rembau parliamentary. Demographics: Malay 54.8%, Indian 27.6%, Chinese 16%. Zahid accompanied "
        "nomination. Day-1: Tok Mat 'act now or lose chance forever' at Sendayan Air Base Family Day."
    ),
    "N.10 Nilai": (
        "PIR-07 highest-priority battleground (director list) + 5-cornered vote-split test. FMT full text "
        "(18 Jul): DAP J. Arul Kumar (Loke's aide, 4th term since 2013; 2023 maj 10,889) vs BN Lai Chien "
        "Kong vs Bersatu V. Saravan Kumar vs Berjasa Zamani Ibrahim vs Indep Omar Isa. Demographics: "
        "Malay 42.5%, Chinese 32.6%, Indian 21.9%. Seremban parliamentary (Loke's)."
    ),
    "N.33 Sri Tanjung": (
        "PIR-07 highest-priority battleground (director list) + 5-cornered vote-split test. FMT full text "
        "(18 Jul): PH Dr G. Rajasekaran (2nd term; 2023 maj 3,996) vs BN A. Achutan vs Bersatu M. "
        "Leevineshwaran (note FMT spelling variant) vs Indep A. Saravanan vs Indep Islah Wahyudi Zainudin. "
        "Demographics: Malay 37.2%, Chinese 31.5%, Indian 28.35%. Port Dickson constituency."
    ),
    "N.14 Ampangan": (
        "PIR-06 Tier-4 seat AND PIR-07 highest-priority battleground. CANDIDATE CONFIRMED via Awani teka-teki "
        "(16 Jul 23:12): PN candidate = Mohamad Rafie Ab Malek (director-flagged 'Rafie'). Director-flagged "
        "PH candidate Nazri Kassim. Day-1 messaging war: PH 'defector' vs PN 'experienced rep' (carryover)."
    ),
    "Datuk Dr Mohamad Rafie Ab Malek": (
        "Director-flagged N.14 Ampangan candidate 'Rafie' — CONFIRMED via Awani teka-teki (16 Jul 23:12): "
        "PN candidate Mohamad Rafie Ab Malek for Ampangan. PN 'experienced rep' framing vs PH's Nazri Kassim. "
        "Active Day-1 messaging war."
    ),
    "N.20 Bembang": (
        "PIR-07 highest-priority battleground (director list, named 'N.20 Bembang'). NOTE: lineup full-text "
        "recovered 'Bahau' seat (DAP Teo Kok Seong vs MCA Chong Fui Ming); whether 'N.20 Bembang' maps to "
        "'Bahau' is unconfirmed from this cycle's full text — kept per director list verbatim. (No further "
        "clarification this cycle.)"
    ),
}

for name, new_ctx in context_updates.items():
    if name in by_name:
        by_name[name]["context"] = new_ctx
        # Upgrade priority where director-flagged full-text evidence strengthens
        if name in ("sole opposition", "MCA biggest loser", "MB after PRN", "penyatuan undi Melayu"):
            by_name[name]["priority"] = "priority"
        if name in ("N.28 Klawang", "N.27 Chembong"):
            by_name[name]["priority"] = "priority"
    else:
        # Should not happen, but create if missing
        by_name[name] = {"entity": name, "type": "narrative", "pir_tag": "PIR-16",
                        "priority": "priority", "source_url": "context-update", "context": new_ctx}

# ----------------------------------------------------------------------------
# NEW entities (not in prior 167)
# ----------------------------------------------------------------------------
new_entities = [
    # --- PIR-06 CRITICAL (new precursor escalations) ---
    {"entity": "Kiandee quorum question", "type": "narrative", "pir_tag": "PIR-06", "priority": "critical",
     "source_url": "https://www.nst.com.my (gnews: Kiandee asks Muhyiddin if Bersatu Supreme Council still has quorum - NST Online)",
     "context": "CRITICAL NEW precursor escalation (NST headline-intel, 19 Jul, cycle 064654). Kiandee escalated from 'PN has grounds (asas kukuh) to remove Bersatu' to questioning whether Bersatu's Supreme Council even has quorum — implies mass exits have hollowed out the decision-making body. Director-flagged 'termination'-adjacent signal (questions organisational functionality). Threshold for formal PN-MT removal still NOT crossed; this is the strongest pre-threshold signal this cycle. Watch for Bersatu Supreme Council formal response."},
    {"entity": "Muhyiddin new coalition after state election", "type": "narrative", "pir_tag": "PIR-06", "priority": "critical",
     "source_url": "https://www.freemalaysiatoday.com/category/nation/2026/07/19/quit-pn-with-gerakan-mipp-in-tow-bersatu-advised",
     "context": "CRITICAL PIR-06 PN-exit signal — FULL TEXT via FMT (19 Jul 09:00 MYT): 'Muhyiddin said the party will form a new coalition after the state election, hinting at a PN exit.' Strongest pre-threshold signal — escalate monitoring for post-NS-PRN formal announcement. Corroborates 'Bersatu exit from PN imminent?' (mkini SNAPSHOT 18 Jul 18:00). Not yet a formal expulsion/withdrawal → threshold NOT crossed, but approaches it."},
    {"entity": "Hadi denies PAS made PN toxic, blames Bersatu", "type": "narrative", "pir_tag": "PIR-06", "priority": "critical",
     "source_url": "https://www.freemalaysiatoday.com/category/nation/2026/07/18/hadi-denies-pas-made-pn-toxic-blames-bersatu-instead",
     "context": "CRITICAL director-flagged 'toxic PN' entity — FULL TEXT via FMT (18 Jul 12:48 MYT). Hadi BLAMES Bersatu: 'rift caused by Bersatu's misconduct within PN.' Counter to Muhyiddin's accusation that PAS made 'baseless allegations and defamatory claims' to sideline Bersatu. Muhyiddin cited Perlis crisis (MB post PAS→Bersatu). Rift stated at Jempol nomination (Serting, Palong, Jeram Padang, Bahau). PAS severed political ties with Bersatu June 8; both remain in PN. Claim/counter-claim = strongest internal-rupture discourse signal."},

    # --- PIR-06 normal (operational arrangement, analysts) ---
    {"entity": "PN-BN ties more than marriage", "type": "narrative", "pir_tag": "PIR-06", "priority": "normal",
     "source_url": "https://www.freemalaysiatoday.com/category/bahasa/tempatan/2026/07/19/bukan-retorik-hadi-beri-isyarat-uji-model-kerjasama-pn-bn-menjelang-pru16",
     "context": "PIR-06+PIR-16 narrative. Hadi (18 Jul): PN-BN ties 'lebih daripada berkahwin' (more than marriage); coalitions will assist each other in NS campaign. Formal ties 'dimuktamadkan dan dinilai dari semasa ke semasa' (finalised and evaluated from time to time). Analyst Zaharuddin Sani: 'bukan sekadar retorik' — frames as market test for a new coalition."},
    {"entity": "PAS severed political ties with Bersatu (June 8)", "type": "narrative", "pir_tag": "PIR-06", "priority": "normal",
     "source_url": "https://www.freemalaysiatoday.com/category/nation/2026/07/18/hadi-denies-pas-made-pn-toxic-blames-bersatu-instead",
     "context": "PIR-06 operational fact — FULL TEXT via FMT. PAS severed political ties with Bersatu on June 8; both parties remain in PN and used same logo for Johor polls. Underpins the operational-split narrative."},
    {"entity": "Bersatu advised to quit PN with Gerakan, MIPP", "type": "narrative", "pir_tag": "PIR-06", "priority": "normal",
     "source_url": "https://www.freemalaysiatoday.com/category/nation/2026/07/19/quit-pn-with-gerakan-mipp-in-tow-bersatu-advised",
     "context": "PIR-06 analyst recommendation — FULL TEXT via FMT (19 Jul 09:00 MYT). IIUM's Lau Zhe Wei advises Bersatu to leave PN now (no longer gains from staying, PAS fallout worsening) and take Gerakan + MIPP — would strip PN of multiethnic image. 'Bersatu should at least drag Gerakan with them.' Corroborates Muhyiddin new-coalition hint."},
    {"entity": "Bersatu heading for wipeout in NS", "type": "narrative", "pir_tag": "PIR-06", "priority": "normal",
     "source_url": "https://www.freemalaysiatoday.com/category/nation/2026/07/19/quit-pn-with-gerakan-mipp-in-tow-bersatu-advised",
     "context": "PIR-06 analyst consensus — FULL TEXT via FMT. USM's Azeem Fazwan Ahmad Farouk expects Bersatu wiped out in NS: 'Bersatu is in no position to win seats going solo.' Azmil Tayeb (USM): Bersatu hasn't distinguished itself from Umno/PAS; 'all that people see coming out of Bersatu is the infighting.' PN fragmented image deals blow to PAS too."},
    {"entity": "Teka-teki 11 kerusi BN terjawab", "type": "narrative", "pir_tag": "PIR-06", "priority": "normal",
     "source_url": "https://www.astroawani.com/berita-politik/prn-negeri-sembilan-teka-teki-11-kerusi-bn-terjawab-pn-umum-baki-calon",
     "context": "PIR-06 coalition configuration confirmation — Awani full text (16 Jul 23:12 MYT). PN chairman Ahmad Samsuri Mokhtar announced remaining PN candidates at Kompleks PAS NS. Resolves 'mystery of 11 BN seats.' Confirms BN 25 / PN 11, no clashes. PN candidates: Danni Rais (Klawang), Mohamad Rafie Ab Malek (Ampangan), Kumar Paramasevam (Lobak), Razali Abu Samah (Sikamat), Erik Michael (Mambau), Lee Boon Shian (Bukit Kepayang), Sathes Kumar Nilameham (Lukut); 4 incumbents retained: Mohd Fairuz Mohd Isa (Serting), Kamarol Ridzuan Mohd Zain (Paroi), Abdul Fatah Zakaria (Bagan Pinang), Ridzuan Ahmad (Gemas)."},
    {"entity": "BN ops rooms open to assist PN (Gemas machinery-sharing)", "type": "narrative", "pir_tag": "PIR-06", "priority": "normal",
     "source_url": "https://www.nst.com.my/news/nation/2026/07/1492233/bn-pn-electoral-understanding-strictly-avoid-multi-cornered-clashes",
     "context": "PIR-06 machinery-sharing CONFIRMED at seat level — NST full text (19 Jul 11:59 MYT). Tampin Umno chief Mohd Isam Mohd Isa: ALL BN operations rooms in Gemas will remain open to assist PN (Wawasan) candidate's campaign. 'We do not want any sabotage.' Aim: win all 3 state seats in Tampin parliamentary. Explicit: 'merely an understanding to face the election, not a political merger.' BN-MCA/MIC relationships 'remain intact.'"},
    {"entity": "Zahid: NS performance determines future alliance", "type": "narrative", "pir_tag": "PIR-06", "priority": "normal",
     "source_url": "https://www.freemalaysiatoday.com/category/nation/2026/07/18/bn-pn-performance-in-negeri-sembilan-to-determine-future-alliance-says-zahid",
     "context": "PIR-06+PIR-16 narrative — FULL TEXT via FMT (18 Jul). Zahid: BN will assess NS performance before deciding wider PN cooperation; results decide whether 'understanding' extends to Melaka polls and GE16. 'Politics is very dynamic.' Learned from Johor geopolitics. NS = test for PRU16 alliance."},
    {"entity": "Datuk Mohd Isam Mohd Isa", "type": "person", "pir_tag": "PIR-06", "priority": "normal",
     "source_url": "https://www.nst.com.my/news/nation/2026/07/1492233/bn-pn-electoral-understanding-strictly-avoid-multi-cornered-clashes",
     "context": "Tampin Umno division chief / Tampin MP. Carrier of seat-level machinery-sharing confirmation: all BN ops rooms in Gemas open to assist PN (Wawasan) candidate. 'Not a political merger'; BN-MCA/MIC relationships intact. Urged no racial/religious sentiment exploitation in Tampin."},
    {"entity": "PN-BN grassroots thumbs up", "type": "narrative", "pir_tag": "PIR-06", "priority": "normal",
     "source_url": "https://www.freemalaysiatoday.com/category/bahasa/tempatan/2026/07/19/akar-umbi-tiada-masalah-undi-calon-bn-pn-harap-noktah-perpecahan",
     "context": "PIR-06+PIR-16 grassroots-acceptance narrative — FMT BM full text (19 Jul). BN/PN grassroots in Jempol welcome cooperation, expect cross-voting in non-contested seats, hope it ends 'perpecahan' (division). Supporters: Mohamad Yusof Abdullah (PN, 78), Noorizan Karim (BN, 49), Jefri Baharom (PN, 60), Mohd Zuki (BN, 61), Abu Ubaidah (PN, 38). 'Penyatuan ummah inilah yang diharapkan oleh akar umbi Umno.'"},

    # --- PIR-06 analysts ---
    {"entity": "Lau Zhe Wei", "type": "person", "pir_tag": "PIR-06", "priority": "normal",
     "source_url": "https://www.freemalaysiatoday.com/category/nation/2026/07/19/quit-pn-with-gerakan-mipp-in-tow-bersatu-advised + https://www.freemalaysiatoday.com/category/nation/2026/07/19/bn-pas-tie-up-will-force-mca-to-make-difficult-choice",
     "context": "IIUM (International Islamic University Malaysia) analyst. PIR-06: advises Bersatu to quit PN with Gerakan+MIPP (strip PN of multiethnic image). PIR-16: MCA benefits from BN-PAS alliance (PAS vote transfer to MCA); MCA faces choice — chase scarce Chinese votes or opt for BN-PAS cooperation and win seats. 'Second option may be better for MCA.' Johor MCA doubled seats to 8 with PAS votes."},
    {"entity": "Azeem Fazwan Ahmad Farouk", "type": "person", "pir_tag": "PIR-06", "priority": "normal",
     "source_url": "https://www.freemalaysiatoday.com/category/nation/2026/07/19/quit-pn-with-gerakan-mipp-in-tow-bersatu-advised",
     "context": "Universiti Sains Malaysia (USM) analyst. Expects Bersatu wiped out in NS: 'Bersatu is in no position to win seats going solo.' Bersatu lacks strong political base, unlikely to recover while internal tensions unresolved."},
    {"entity": "Azmil Tayeb", "type": "person", "pir_tag": "PIR-06", "priority": "normal",
     "source_url": "https://www.freemalaysiatoday.com/category/nation/2026/07/19/quit-pn-with-gerakan-mipp-in-tow-bersatu-advised",
     "context": "Universiti Sains Malaysia (USM) analyst. Bersatu problems run deeper than PAS issues; hasn't distinguished itself from Umno/PAS despite competing for same Malay electorate. 'All that people see coming out of Bersatu is the infighting.' PN fragmented image deals blow to PAS too."},
    {"entity": "Ahmad Zaharuddin Sani Ahmad Sabri", "type": "person", "pir_tag": "PIR-16", "priority": "priority",
     "source_url": "https://www.freemalaysiatoday.com/category/bahasa/tempatan/2026/07/19/bukan-retorik-hadi-beri-isyarat-uji-model-kerjasama-pn-bn-menjelang-pru16",
     "context": "Analyst, Global Asia Consulting. PRIORITY PIR-16 carrier of 'NS = makmal politik (political laboratory)' framing. Hadi 'more than marriage' = 'bukan sekadar retorik' — forms perception that PN-BN cooperation already exists though not formally sealed. 'The most important question is not whether the bride and groom agree, but whether the children accept the new marriage' (children = grassroots). Political marriage without family blessing is fragile."},
    {"entity": "Azmi Hassan", "type": "person", "pir_tag": "PIR-16", "priority": "normal",
     "source_url": "https://www.freemalaysiatoday.com/category/bahasa/tempatan/2026/07/19/bukan-retorik-hadi-beri-isyarat-uji-model-kerjasama-pn-bn-menjelang-pru16",
     "context": "Felo Majlis Profesor Negara (National Professorial Council Fellow). PIR-16 'Johor formula' carrier. Hadi's statement reflects increased cooperation tested unofficially in Johor. Johor PAS-Umno success motivates clearer NS understanding. BN not contesting all 36 + PAS only contesting BN-uncontested seats = 'persefahaman begitu nyata.' Model not necessarily applicable to all states — Johor/NS/Melaka landscapes differ."},
    {"entity": "Wong Chin Huat", "type": "person", "pir_tag": "PIR-16", "priority": "normal",
     "source_url": "https://www.freemalaysiatoday.com/category/nation/2026/07/19/bn-pas-tie-up-will-force-mca-to-make-difficult-choice",
     "context": "Sunway University analyst. PIR-16: PH weakness incentivised BN-PAS pact. 'If PH collapses in Negeri Sembilan, BN and PN would collaborate further in GE16.' MCA weaker in NS than Johor. Non-Malays unwilling to stake future on MCA if perceive risk of PH defeated by BN-PAS alliance. DAP/supporters concerned about BN-PAS ramifications."},

    # --- PIR-07 NEW candidates (director-list seats now recovered) ---
    {"entity": "Datuk Bakri Sawir", "type": "person", "pir_tag": "PIR-07", "priority": "priority",
     "source_url": "https://www.astroawani.com/berita-politik/prn-negeri-sembilan-dua-sepupu-bertembung-raih-sokongan-pengundi-di-pasar-minggu-kuala-klawang",
     "context": "PRIORITY PIR-07 — PH incumbent in N.28 Klawang (director-listed seat). Day-1 campaign (Awani full text, 19 Jul 12:11 MYT): campaigned at Pasar Minggu Kuala Klawang (Jelebu) same time as cousin/PN rival Danni Rais — met peacefully, joked, no provocation. Took down flags after Majlis Daerah Jelebu warning. 'No special challenge… campaign healthily, follow rules.' Mature-campaign framing carrier."},
    {"entity": "Danni Rais", "type": "person", "pir_tag": "PIR-07", "priority": "priority",
     "source_url": "https://www.astroawani.com/berita-politik/prn-negeri-sembilan-dua-sepupu-bertembung-raih-sokongan-pengundi-di-pasar-minggu-kuala-klawang + https://www.astroawani.com/berita-politik/prn-negeri-sembilan-teka-teki-11-kerusi-bn-terjawab-pn-umum-baki-calon",
     "context": "PRIORITY PIR-07 — PN candidate in N.28 Klawang (director-listed seat). Confirmed via Awani teka-teki (16 Jul 23:12) and Day-1 campaign article (19 Jul 12:11 MYT). Cousin of PH incumbent Bakri Sawir — 'two cousins face off' marquee Day-1 storyline. (Spelling variant 'Danii Rais' in teka-teki article.)"},
    {"entity": "Muhammad Adib Musa", "type": "person", "pir_tag": "PIR-07", "priority": "priority",
     "source_url": "https://www.astroawani.com/berita-politik/prn-negeri-sembilan-dua-sepupu-bertembung-raih-sokongan-pengundi-di-pasar-minggu-kuala-klawang",
     "context": "PRIORITY PIR-07 — Bersatu candidate in N.28 Klawang (director-listed seat), 3-cornered vs Bakri Sawir (PH) + Danni Rais (PN). Awani full text (19 Jul 12:11 MYT)."},
    {"entity": "Zaifulbahri Idris", "type": "person", "pir_tag": "PIR-07", "priority": "priority",
     "source_url": "https://www.freemalaysiatoday.com/category/nation/2026/07/18/tok-mat-in-straight-fight-with-ph-in-rantau",
     "context": "PRIORITY PIR-07 — BN candidate in N.27 Chembong (director-listed seat), NOW RECOVERED via FMT Tok Mat article (18 Jul). Has represented Chembong since 2008; retained seat with 4,335-vote majority in 2023. Straight fight vs PH's Danish Nazran Murad."},
    {"entity": "Danish Nazran Murad", "type": "person", "pir_tag": "PIR-07", "priority": "priority",
     "source_url": "https://www.freemalaysiatoday.com/category/nation/2026/07/18/tok-mat-in-straight-fight-with-ph-in-rantau",
     "context": "PRIORITY PIR-07 — PH candidate in N.27 Chembong (director-listed seat), NOW RECOVERED via FMT (18 Jul). Straight fight vs BN's Zaifulbahri Idris."},
    {"entity": "Kumar Paramasevam", "type": "person", "pir_tag": "PIR-07", "priority": "normal",
     "source_url": "https://www.astroawani.com/berita-politik/prn-negeri-sembilan-teka-teki-11-kerusi-bn-terjawab-pn-umum-baki-calon",
     "context": "PN (PAS) candidate in Lobak. Awani teka-teki (16 Jul 23:12) names 'Kumar Paramasevam' for Lobak — likely the full name of the 'Dr P. Kumar' listed in Malay Mail nomination lineup (PAS candidate in Lobak urban straight fight vs DAP's Chew Seh Yong). Name-clarification entity."},
    {"entity": "Erik Michael", "type": "person", "pir_tag": "PIR-07", "priority": "normal",
     "source_url": "https://www.astroawani.com/berita-politik/prn-negeri-sembilan-teka-teki-11-kerusi-bn-terjawab-pn-umum-baki-calon",
     "context": "PN candidate in Mambau. Awani teka-teki (16 Jul 23:12). Mambau = one of the 3 seats (Lobak, Mambau, Lukut) Loke said MCA 'surrendered' to PN ('MCA biggest loser')."},
    {"entity": "Mohd Fairuz Mohd Isa", "type": "person", "pir_tag": "PIR-06", "priority": "normal",
     "source_url": "https://www.astroawani.com/berita-politik/prn-negeri-sembilan-teka-teki-11-kerusi-bn-terjawab-pn-umum-baki-calon",
     "context": "PN incumbent in Serting (retained). Awani teka-teki (16 Jul 23:12). One of 4 PN incumbents retained (others: Kamarol Ridzuan Paroi, Abdul Fatah Zakaria Bagan Pinang, Ridzuan Ahmad Gemas). Serting = one of the Jempol-district seats Hadi nomination covered."},
    {"entity": "Nazree Yunus", "type": "person", "pir_tag": "PIR-07", "priority": "normal",
     "source_url": "https://www.freemalaysiatoday.com/category/nation/2026/07/18/tok-mat-in-straight-fight-with-ph-in-rantau",
     "context": "Bersatu candidate in Paroi. FMT Tok Mat article (18 Jul) reports Paroi as 3-CORNERED: PAS/PN Kamarul Ridzuan Mohd Zain (incumbent, 2023 maj 5,539) vs PH Ahmad Shahir Shah vs Bersatu Nazree Yunus. (Malay Mail had described Paroi as straight fight — discrepancy; FMT more detailed.)"},
    {"entity": "Umry Abdul Khois", "type": "person", "pir_tag": "PIR-07", "priority": "normal",
     "source_url": "https://www.freemalaysiatoday.com/category/nation/2026/07/18/bn-to-decide-negeri-sembilan-mb-candidate-only-if-it-wins-polls",
     "context": "PH candidate in Pertang (3-way vs BN's Jalaluddin Alias + Bersatu's Faizal Fadli Idrus). FMT full text (18 Jul)."},
    {"entity": "Faizal Fadli Idrus", "type": "person", "pir_tag": "PIR-07", "priority": "normal",
     "source_url": "https://www.freemalaysiatoday.com/category/nation/2026/07/18/bn-to-decide-negeri-sembilan-mb-candidate-only-if-it-wins-polls",
     "context": "Bersatu candidate in Pertang (3-way vs BN's Jalaluddin Alias + PH's Umry Abdul Khois). FMT full text (18 Jul)."},
    {"entity": "Mambau", "type": "seat", "pir_tag": "PIR-07", "priority": "normal",
     "source_url": "https://www.freemalaysiatoday.com/category/nation/2026/07/19/mca-biggest-loser-in-bn-pn-negeri-sembilan-pact-says-loke + https://www.astroawani.com/berita-politik/prn-negeri-sembilan-teka-teki-11-kerusi-bn-terjawab-pn-umum-baki-calon",
     "context": "Seat ceded to PN (Loke: MCA 'surrendered' Mambau to PN). Previously held by senior MCA figures. PN candidate Erik Michael (Awani teka-teki). Part of the 'MCA biggest loser' narrative cluster (Lobak, Mambau, Lukut)."},
    {"entity": "Serting", "type": "seat", "pir_tag": "PIR-06", "priority": "normal",
     "source_url": "https://www.astroawani.com/berita-politik/prn-negeri-sembilan-teka-teki-11-kerusi-bn-terjawab-pn-umum-baki-calon + https://www.freemalaysiatoday.com/category/nation/2026/07/18/hadi-denies-pas-made-pn-toxic-blames-bersatu-instead",
     "context": "PN incumbent seat (Mohd Fairuz Mohd Isa, retained). One of the Jempol-district seats (Serting, Palong, Jeram Padang, Bahau) where Hadi spoke at nomination and stated the PAS-Bersatu rift."},
    {"entity": "Tampin", "type": "seat", "pir_tag": "PIR-07", "priority": "normal",
     "source_url": "https://www.nst.com.my/news/nation/2026/07/1492233/bn-pn-electoral-understanding-strictly-avoid-multi-cornered-clashes",
     "context": "Parliamentary constituency (3 state seats). BN aiming to win all 3 via BN-PN understanding. Tampin Umno chief Mohd Isam Mohd Isa confirmed machinery-sharing: BN ops rooms in Gemas open to assist PN candidate. Johari met Tampin BN election machinery (NST Johor-formula article)."},
    {"entity": "Fadillah Yusof", "type": "person", "pir_tag": "PIR-07", "priority": "normal",
     "source_url": "https://www.nst.com.my/news/nation/2026/07/1492353/resign-if-you-want-attack-unity-partners-anwar-tells-ministers",
     "context": "Deputy Prime Minister. Anwar conveyed the 'resign if you want to attack unity partners' reminder in discussions yesterday with DPMs Zahid + Fadillah, following NS election campaign."},
    {"entity": "Fahmi Fadzil", "type": "person", "pir_tag": "PIR-07", "priority": "normal",
     "source_url": "https://www.nst.com.my/news/nation/2026/07/1492251/anwar-invokes-ali-baba-bujang-lapok-urge-unity-reject-plunder",
     "context": "Communications Minister. Present at Anwar's Ali Baba Bujang Lapok unity speech at National Month launch (Ipoh, Sultan Azlan Shah Health Ministry Training Institute, 19 Jul 12:21 MYT)."},
    {"entity": "Saarani Mohamad", "type": "person", "pir_tag": "PIR-07", "priority": "normal",
     "source_url": "https://www.nst.com.my/news/nation/2026/07/1492251/anwar-invokes-ali-baba-bujang-lapok-urge-unity-reject-plunder",
     "context": "Perak Menteri Besar. Present at Anwar's Ali Baba Bujang Lapok unity speech (Ipoh, 19 Jul). Perak unity govt ties unaffected by Melaka DAP pullout (per prior-cycle Star headline)."},

    # --- PIR-16 NEW narratives (priority viral-amplifier) ---
    {"entity": "NS = makmal politik (political laboratory for PRU16)", "type": "narrative", "pir_tag": "PIR-16", "priority": "priority",
     "source_url": "https://www.freemalaysiatoday.com/category/bahasa/tempatan/2026/07/19/bukan-retorik-hadi-beri-isyarat-uji-model-kerjasama-pn-bn-menjelang-pru16",
     "context": "PRIORITY PIR-16 framing — NEW this cycle. Zaharuddin Sani (Global Asia Consulting): NS 'sedang dijadikan makmal politik' (being made a political laboratory). 'Jika eksperimen ini meningkatkan sokongan, ia boleh berkembang menjadi model kerjasama menjelang PRU16. Jika gagal, kedua-dua pihak masih mempunyai ruang untuk berkata bahawa mereka tidak pernah benar-benar berkahwin.' Frames every NS seat as a PRU16 indicator. Azmi Hassan: Johor PAS-Umno success is the motivator. Corroborates Zahid 'NS performance determines future alliance' + Johari 'Johor formula' + Utusan Johari 'PRN NS penentu kerjasama BN-PN PRU16.'"},
    {"entity": "Johor formula", "type": "narrative", "pir_tag": "PIR-16", "priority": "normal",
     "source_url": "https://www.nst.com.my/news/nation/2026/07/1492212/johari-adapt-successful-johor-election-formula-ns-polls + https://www.freemalaysiatoday.com/category/bahasa/tempatan/2026/07/19/bukan-retorik-hadi-beri-isyarat-uji-model-kerjasama-pn-bn-menjelang-pru16",
     "context": "PIR-16 narrative. Johari Abdul Ghani (Umno VP): adapt BN's successful Johor election formula to NS — 3 core elements: party strength, strategic candidate selection, election machinery capability. 'We cannot assume the same formula will apply automatically.' Spoke at Tampin BN machinery meeting. Azmi Hassan: Johor PAS-Umno success motivates NS understanding; 'pengorbanan PAS mungkin dikatakan berbaloi.'"},
    {"entity": "Act now or lose chance forever (Tok Mat)", "type": "narrative", "pir_tag": "PIR-16", "priority": "priority",
     "source_url": "https://www.nst.com.my/news/nation/2026/07/1492349/n9-polls-act-now-or-lose-chance-forever-says-tok-mat",
     "context": "PRIORITY PIR-16 existential Malay-future framing — FULL TEXT via NST (19 Jul 14:46 MYT, FRESH). Tok Mat at Sendayan Air Base Family Day Carnival: BN-PN understanding 'important to safeguard the future of race and religion.' First mooted 2018 but 'fell through halfway.' 'If we don't do it this time, we will miss the boat… our children and grandchildren will become mere traders in their own country.' Frames BN-PN as EXISTENTIAL for Malay future. Directly counters DAP/Madani multi-ethnic narrative."},
    {"entity": "Malay-Muslim unity with non-extreme partners (Hadi)", "type": "narrative", "pir_tag": "PIR-16", "priority": "priority",
     "source_url": "https://www.nst.com.my/news/nation/2026/07/1492319/hadi-calls-malay-muslim-unity-non-extreme-partners-including-mca-mic",
     "context": "PRIORITY PIR-16 narrative — FULL TEXT via NST (19 Jul 14:03 MYT, FRESH). Hadi (FB post): support PAS+Umno+MCA+MIC+DHPP 'non-extreme' formula; extend to Sabah/Sarawak to 'save Malaysia.' Reject 'unnatural Malay groups with DAP' (secular/chauvinist). 'Malay Muslims must lead because they dominate the Muslim population.' NS: BN 25 / PN 11 / PAS 5 under PN. Frames NS as PRU16 realignment test. Expanded 'penyatuan undi Melayu' with conditional multiracial extension."},
    {"entity": "Reject unnatural Malay groups with DAP", "type": "narrative", "pir_tag": "PIR-16", "priority": "normal",
     "source_url": "https://www.nst.com.my/news/nation/2026/07/1492319/hadi-calls-malay-muslim-unity-non-extreme-partners-including-mca-mic",
     "context": "PIR-16 narrative (Hadi, NST 19 Jul 14:03 MYT). Reject 'unnatural Malay groups that are with DAP, namely fanatical secular and extreme chauvinist groups that threaten Islam and the Malay community.' Implicit attack on PH/Umno-DAP federal unity cooperation. Frames DAP as existential threat to Malay/Islamic interests."},
    {"entity": "Ali Baba Bujang Lapok / 40 thieves were also united (Anwar)", "type": "narrative", "pir_tag": "PIR-16", "priority": "priority",
     "source_url": "https://www.nst.com.my/news/nation/2026/07/1492251/anwar-invokes-ali-baba-bujang-lapok-urge-unity-reject-plunder",
     "context": "PRIORITY PIR-16 COUNTER-NARRATIVE — FULL TEXT via NST (19 Jul 12:21 MYT). Anwar at National Month launch (Ipoh): 'Unity alone is not enough… the 40 thieves were also united.' 'Unite for what? We must unite to improve the quality of life of the people. Not unite to steal or plunder timber and wealth.' Multi-ethnic independence narrative; implicit counter to BN-PN 'Malay unity' framing + Tok Mat existential framing. Fahmi + Perak MB Saarani present."},
    {"entity": "Resign to attack unity partners (Anwar)", "type": "narrative", "pir_tag": "PIR-16", "priority": "priority",
     "source_url": "https://www.nst.com.my/news/nation/2026/07/1492353/resign-if-you-want-attack-unity-partners-anwar-tells-ministers",
     "context": "PRIORITY PIR-16 DISCIPLINE narrative — FULL TEXT via NST (19 Jul 14:47 MYT, FRESH). Anwar warns ministers/deputy ministers/agency heads to RESIGN if they intend to use federal positions to attack unity-govt partners during state campaigns. Federal-aligned parties free to contest each other in state polls, but office-holders must keep discipline. Conveyed in discussions with DPMs Zahid + Fadillah. (Article marked 'MORE TO COME'.) Federal-state firewall."},
    {"entity": "BN to decide NS MB candidate only if it wins (Jalaluddin)", "type": "narrative", "pir_tag": "PIR-16", "priority": "normal",
     "source_url": "https://www.freemalaysiatoday.com/category/nation/2026/07/18/bn-to-decide-negeri-sembilan-mb-candidate-only-if-wins-polls",
     "context": "PIR-16 'MB after PRN' confirmation — FULL TEXT via FMT (18 Jul). Jalaluddin Alias (state Umno chief, touted as potential MB): 'Once we achieve victory, BN's leadership will decide who is best suited to be appointed the menteri besar.' 'Several leaders capable.' Jalaluddin seeking 3rd term in Pertang (3-way vs PH Umry + Bersatu Faizal Fadli)."},
    {"entity": "BN-PN cooperation only to avoid vote splits, not alliance (Wee)", "type": "narrative", "pir_tag": "PIR-16", "priority": "normal",
     "source_url": "https://www.freemalaysiatoday.com/category/nation/2026/07/18/bn-pn-cooperation-only-to-avoid-vote-splits-says-wee",
     "context": "PIR-16 narrative — FULL TEXT via FMT (18 Jul). Wee Ka Siong (MCA president): cooperation 'does not amount to an alliance'; each party upholds ideological principles + checks and balances. 'Not an alliance and it will not lead to the formation of a new party or coalition.' Decision finalised early hours of July 15. MCA involvement = ensure Chinese community/multiracial/vernacular education/religious freedom representation. Hadi: PAS agreed in principle to let BN defend 14 prior seats + PAS contest 3 it won."},
    {"entity": "BN-PAS tie-up will force MCA difficult choice", "type": "narrative", "pir_tag": "PIR-16", "priority": "normal",
     "source_url": "https://www.freemalaysiatoday.com/category/nation/2026/07/19/bn-pas-tie-up-will-force-mca-to-make-difficult-choice",
     "context": "PIR-16 narrative — FULL TEXT via FMT (19 Jul). MCA must choose between winning elections and losing core supporters. Lau Zhe Wei: MCA benefits from BN-PAS alliance (PAS vote transfer — Johor MCA doubled to 8 seats) but may discourage MCA supporters. 'Second option (BN-PAS cooperation) may be better for MCA.' Wong Chin Huat: MCA weaker in NS than Johor; non-Malays won't stake future on MCA if perceive PH defeat risk."},
    {"entity": "Umno's dangerous dance with PAS", "type": "narrative", "pir_tag": "PIR-16", "priority": "priority",
     "source_url": "https://www.freemalaysiatoday.com/category/opinion/2026/07/19/umnos-dangerous-dance-with-pas",
     "context": "PRIORITY PIR-16 viral-amplifier opinion — FULL TEXT via FMT (19 Jul, 7009c). 'By quietly opening the side door for PAS in NS, Umno is committing the oldest form of political miscalculation: validating the very force designed to replace it.' Frames BN-PN as 'friends with benefits'; PAS transfers ideological brand to BN candidates. Cites Amanat Hadi (1981, Umno supporters as 'infidels'). 'Religious populism does not seek to share power; they seek to replace the decadent old order entirely.' Warns urban non-Malay alienation (Seremban, Rasah, Nilai). 'The tiger is always hungry, and it does not care for understandings.'"},
    {"entity": "Lim rejects Islamophobia claim, Hadi coined green wave", "type": "narrative", "pir_tag": "PIR-16", "priority": "normal",
     "source_url": "https://www.freemalaysiatoday.com/category/nation/2026/07/18/lim-rejects-islamophobia-claim-says-hadi-coined-green-wave-term",
     "context": "PIR-16 counter-narrative — FULL TEXT via FMT (18 Jul). Lim Lip Eng (Kepong MP, DAP): Hadi himself coined 'gelombang hijau' (green wave) in 2018 (Harakah) re PAS gains in Perak + Terengganu in GE14 — 4 years before GE15. 'PAS cannot use religion as an armour against political criticism.' Cites PAS deputy president Tuan Ibrahim Tuan Man: 'PAS never claimed to be sole embodiment of Islam.' Counters Hadi's Islamophobia claim."},
    {"entity": "gelombang hijau / green wave", "type": "narrative", "pir_tag": "PIR-16", "priority": "normal",
     "source_url": "https://www.freemalaysiatoday.com/category/nation/2026/07/18/lim-rejects-islamophobia-claim-says-hadi-coined-green-wave-term",
     "context": "PIR-16 narrative. Term 'green wave' (gelombang hijau) — Hadi coined 2018 (PAS mouthpiece Harakah) re GE14 PAS gains in Perak + Terengganu. Hadi now says DAP used term after GE15 to stigmatise PAS/Muslims (Islamophobia claim). Lim Lip Eng counters with 2018 provenance. Active framing contest."},
    {"entity": "Amanat Hadi (1981)", "type": "narrative", "pir_tag": "PIR-16", "priority": "normal",
     "source_url": "https://www.freemalaysiatoday.com/category/opinion/2026/07/19/umnos-dangerous-dance-with-pas",
     "context": "PIR-16 historical reference. 1981 Amanat Hadi labelled Umno supporters as 'infidels' — cited in FMT 'Umno's dangerous dance with PAS' opinion as the historical frame for why Umno-PAS cooperation is risky (Umno spent half a century framing PAS as extremist). Now Umno 'inviting back the very force it spent half a century containing.'"},
    {"entity": "charade to deceive the Malays (Muhyiddin)", "type": "narrative", "pir_tag": "PIR-16", "priority": "normal",
     "source_url": "https://www.freemalaysiatoday.com/category/nation/2026/07/18/bersatu-must-survive-as-lone-opposition-says-muhyiddin",
     "context": "PIR-16 counter-narrative — FULL TEXT via FMT Muhyiddin (18 Jul 16:52 MYT). Accuses Umno/BN of deflecting blame while in government + using 'ummah unity'/'Malay unity' calls to win Malay voters. 'This is just a charade to deceive the eyes of the Malays and the people in order to gain power.' Claims Bersatu 'free of all this charade' + committed to anti-kleptocracy/1MDB founding struggle. Direct counter to Tok Mat/Hadi 'Malay unity' framing."},
    {"entity": "Pengundi mahu kempen matang (mature campaign)", "type": "narrative", "pir_tag": "PIR-16", "priority": "normal",
     "source_url": "https://www.astroawani.com/berita-politik/prn-negeri-sembilan-pengundi-mahu-kempen-matang-calon-fokus-kehendak-rakyat",
     "context": "PIR-16 PROCESS narrative — Awani full text (19 Jul 13:58 MYT). Rembau voters want mature, courteous campaign focused on people's needs/economy, not provocation. Voters quoted: Malek Ibrahim (77, retiree), Mohd Firdaus Nordin (35, Imam Masjid Kampung Pedas Tengah), Siti Hawa Yahya (56, trader — cost of living). 'Rakyat sekarang sudah cerdik.' Bakri Sawir (Klawang) embodies it. 103 candidates / 36 seats confirmed."},
    {"entity": "Johari: adapt Johor formula for NS", "type": "narrative", "pir_tag": "PIR-16", "priority": "normal",
     "source_url": "https://www.nst.com.my/news/nation/2026/07/1492212/johari-adapt-successful-johor-election-formula-ns-polls",
     "context": "PIR-16 narrative — NST full text (19 Jul 11:34 MYT). Johari Abdul Ghani (Umno VP) at Tampin BN machinery meeting: adapt Johor election formula (party strength + candidate selection + machinery) to NS local realities. 'Cannot assume same formula will apply automatically.' BN victory in NS = part of broader state-level rebuild. (See also 'Johor formula' entity.)"},

    # --- PIR-16 NEW persons ---
    {"entity": "Lim Lip Eng", "type": "person", "pir_tag": "PIR-16", "priority": "normal",
     "source_url": "https://www.freemalaysiatoday.com/category/nation/2026/07/18/lim-rejects-islamophobia-claim-says-hadi-coined-green-wave-term",
     "context": "Kepong MP (DAP), four-term. Rejects Hadi's Islamophobia claim; says Hadi coined 'green wave' term in 2018 (Harakah). 'PAS cannot use religion as an armour against political criticism.' Cites Tuan Ibrahim Tuan Man contradicting Hadi."},
    {"entity": "Tuan Ibrahim Tuan Man", "type": "person", "pir_tag": "PIR-16", "priority": "normal",
     "source_url": "https://www.freemalaysiatoday.com/category/nation/2026/07/18/lim-rejects-islamophobia-claim-says-hadi-coined-green-wave-term",
     "context": "PAS deputy president. Cited by Lim Lip Eng: 'PAS had never claimed to be the sole embodiment of Islam' — used to counter Hadi's Islamophobia claim / framing of PAS criticism as attack on Islam."},
    {"entity": "Ab Rauf", "type": "person", "pir_tag": "PIR-16", "priority": "normal",
     "source_url": "https://www.nst.com.my (gnews: Ab Rauf says PH only mirrored federal unity in Melaka - NST Online)",
     "context": "Melaka Chief Minister. PIR-16 Melaka DAP withdrawal narrative peripheral figure. Headline-intel (NST, 14 Jul 10:08 GMT): 'Ab Rauf says PH only mirrored federal unity in Melaka' — frames Melaka state govt arrangement as mirroring federal unity govt. Full text not recovered (gnews JS-render). Context for Melaka DAP quit-state-govt narrative."},
    {"entity": "Adly", "type": "person", "pir_tag": "PIR-16", "priority": "normal",
     "source_url": "https://www.malaymail.com (gnews: Melaka assembly: Four DAP assemblymen moved to opposition but Amanah's Adly still seated with govt)",
     "context": "Amanah's Melaka leader. In Melaka DAP withdrawal: 4 DAP assemblymen moved to opposition bloc but Adly still seated with govt — Amanah did not follow DAP out. Highlights PH-component divergence in Melaka. Frames DAP isolation vs Amanah compliance. (Per prior-cycle Melaka DAP narrative; now added as distinct entity.)"},
]

# Add new entities (skip if name already exists to avoid dup; new_entities are genuinely new)
added = 0
for ne in new_entities:
    if ne["entity"] not in by_name:
        prior_entities.append(ne)
        by_name[ne["entity"]] = ne
        added += 1
    else:
        # merge: append new context note
        existing = by_name[ne["entity"]]
        if ne["context"] not in existing["context"]:
            existing["context"] = existing["context"] + " || ADDL: " + ne["context"]

# ----------------------------------------------------------------------------
# Recompute metadata + counts
# ----------------------------------------------------------------------------
def counts(entities):
    by_type = {}
    by_pir = {}
    by_pri = {}
    for e in entities:
        by_type[e["type"]] = by_type.get(e["type"], 0) + 1
        by_pir[e["pir_tag"]] = by_pir.get(e["pir_tag"], 0) + 1
        by_pri[e["priority"]] = by_pri.get(e["priority"], 0) + 1
    return by_type, by_pir, by_pri

by_type, by_pir, by_pri = counts(prior_entities)

data["extraction_metadata"].update({
    "processing_timestamp_utc": ts_utc,
    "processing_timestamp_myt": ts_myt,
    "file_id": file_id,
    "cycles_ingested": ["20260719_011915", "20260719_024042", "20260719_034922",
                       "20260719_051226", "20260719_064654"],
    "cycles_new_this_build": ["20260719_051226", "20260719_064654"],
    "entities_added_this_build": added,
    "context_updates_this_build": len(context_updates),
    "new_full_text_sources_this_build": [
        "FMT RSS (content:encoded) — 19 full-text articles (NEW SOURCE, largest single-day gain)",
        "NST WordPress feed (content:encoded) — 7 full-text articles (Tok Mat, Anwar resign, Hadi unity, Anwar Ali Baba, Johari Johor-formula, NS police, Melaka shophouse)",
        "Astro Awani direct (berita-politik slug) — 3 full-text (Klawang cousins N.28 T1, Pengundi kempen matang, Teka-teki 11 kerusi PN candidate list)",
        "mkini direct — 1 paywalled preview (Zan Azlee indicator v2, 513c)",
        "gnews headline-intel — 10 items (Kiandee quorum, PAS-may-leave analysts, Anthony-Loké-Awani-Intl, PH-lineup-tomorrow, Newswav x3, Star x1, Malay Mail dup)"
    ],
    "entity_counts": {
        "total_entities": len(prior_entities),
        "critical": by_pri.get("critical", 0),
        "priority": by_pri.get("priority", 0),
        "normal": by_pri.get("normal", 0),
        "by_type": by_type,
        "by_pir": by_pir
    },
    "pir06_threshold_status": (
        "NOT CROSSED — no formal PN-MT removal notice for Bersatu detected across 5 cycles "
        "(5,513 titles scanned: 1151+1174+1164+1151+1160). Bersatu operational split FULL TEXT confirmed "
        "(24 own-logo seats; PAS severed ties June 8). CRITICAL precursor cluster now 5: (1) Kiandee 'asas "
        "kukuh' removal call, (2) Kiandee quorum-question ESCALATION (NEW this build), (3) 'toxic PN' "
        "claim-counterclaim (FULL TEXT FMT), (4) Ridzuan Ahmad quits Bersatu, (5) Muhyiddin 'new coalition "
        "after state election' PN-exit hint (FULL TEXT FMT — strongest pre-threshold signal). Watch next "
        "cycle for Bersatu Supreme Council response to quorum question + post-NS-PRN formalisation."
    ),
    "collection_limitations_honest": [
        "Malaysiakini paywall: mkini articles (Loke Malay votes 780073, Zan Azlee 780063, AI chatbot 780066, Johor exco 780048) captured as previews (91-600c) only; full body paywalled",
        "gnews protobuf resolution via curl: CONFIRMED INFEASIBLE across 4 cycles — intermediate is 588KB JS SPA, protobuf base64 decodes to encrypted tokens only. 10 items this build saved as headline-intelligence (title+pubdate+source). Kiandee-quorum NST article is headline-intel only — full text requires NST feed (rotated past top-50) or JS-render",
        "NST WordPress feed: only latest 50 items — older high-value NST articles (Asyraf Wajdi BN-PN stability, Hadi PN-assist-BN, Bersatu goes solo, Loke slams traitors, Linggi risky) fell outside top-50 window → headline-intelligence only",
        "The Star + Malay Mail search/listing: JS-rendered; Melaka DAP + Fahmi articles captured as headline intelligence only",
        "SOLVED this build: FMT (curl-friendly RSS+direct) + NST WordPress feed + Awani direct-fetch (berita-politik slug) now provide reliable full-text paths — substantially closes prior 'JS-render blocker' gap for three major sources"
    ]
})

# Add new sources extracted from
sources = data["extraction_metadata"].get("sources_extracted_from", [])
new_sources = [
    "priority_pir-07_awani-dua-sepupu-klawang_20260719_064654.md (FULL TEXT, 2148c — N.28 Klawang T1 Day-1 cousins campaign, FRESH 12:11 MYT)",
    "priority_pir-07_n9-polls-act-now-or-lose-chance-forever-says-tok-mat_20260719_064654.md (FULL TEXT NST, 1946c — Tok Mat existential Malay-future framing, FRESH 14:46 MYT)",
    "priority_pir-07_resign-if-you-want-to-attack-unity-partners-anwar-tells-ministers_20260719_064654.md (FULL TEXT NST, 1001c — Anwar discipline warning, FRESH 14:47 MYT)",
    "priority_pir-06-pir-16_hadi-calls-for-malay-muslim-unity-with-non-extreme-partners-including-mca-mic_20260719_064654.md (FULL TEXT NST, 2863c — Hadi non-extreme partners formula, FRESH 14:03 MYT)",
    "priority_pir-07_anwar-invokes-ali-baba-bujang-lapok-to-urge-unity-reject-plunder_20260719_064654.md (FULL TEXT NST, 5937c — Anwar counter-narrative)",
    "priority_pir-06-pir-16_mca-biggest-loser-in-bn-pn-negeri-sembilan-pact-says-loke_20260719_064654.md (FULL TEXT FMT EN, 2350c — Loke MCA biggest loser)",
    "priority_pir-06_kiandee-asks-muhyiddin-if-bersatu-supreme-council-still-has-quorum-nst-online_20260719_064654.md (headline-intel — Kiandee quorum ESCALATION)",
    "priority_pir-06_bukan-retorik-hadi-beri-isyarat-uji-model-kerjasama-pn-bn-menjelang-pru16_20260719_064654.md (FULL TEXT FMT BM, 4019c — makmal politik framing)",
    "priority_pir-06-pir-07_akar-umbi-tiada-masalah-undi-calon-bn-pn-harap-noktah-perpecahan_20260719_064654.md (FULL TEXT FMT BM, 3248c — grassroots thumbs up)",
    "priority_pir-16-pir-07_awani-pengundi-kempen-matang_20260719_064654.md (FULL TEXT Awani, 2631c — mature campaign)",
    "priority_pir-06-pir-07_awani-teka-teki-11-kerusi-bn-pn-cal_20260719_064654.md (FULL TEXT Awani, 1305c — PN candidate list confirms N.14 Ampangan Rafie, N.28 Klawang Danni Rais)",
    "priority_pir-07_fmt-tok-mat-straight-fight-ph-rantau_20260719_051226.md (FULL TEXT FMT, 2634c — Rantau + Kota razor 135 + Chembong Zaifulbahri + Paroi 3-cornered Nazree Yunus)",
    "priority_pir-07_fmt-loke-aide-5-cornered-fight-nilai_20260719_051226.md (FULL TEXT FMT, 1951c — Nilai + Sri Tanjung 5-cornered demographics/majorities)",
    "priority_pir-06_fmt-bersatu-must-survive-lone-opposition-muhyiddin_20260719_051226.md (FULL TEXT FMT, 2276c — lone opposition + new coalition hint)",
    "priority_pir-06_fmt-hadi-denies-pas-made-pn-toxic-blames-bersatu_20260719_051226.md (FULL TEXT FMT, 2182c — toxic PN claim-counterclaim + PAS severed ties June 8)",
    "priority_pir-06_fmt-quit-pn-gerakan-mipp-bersatu-advised_20260719_051226.md (FULL TEXT FMT, 3197c — Lau Zhe Wei + Azeem Fazwan + Azmil Tayeb analyst consensus)",
    "priority_pir-06-pir-07_nst-bn-pn-electoral-understanding-strictly-to-avoid-multi-c_20260719_051226.md (FULL TEXT NST, 2588c — Mohd Isam Mohd Isa Gemas machinery-sharing)",
    "priority_pir-16-pir-07_nst-johari-adapt-successful-johor-election-formula-for-ns_20260719_051226.md (FULL TEXT NST, 1827c — Johor formula)",
    "priority_pir-07_nst-ns-polls-one-police-report-received-19-campaign-permi_20260719_051226.md (FULL TEXT NST, 2097c — Alzafny 19 permits)",
    "priority_pir-06-pir-07_fmt-zahid-bn-pn-performance-ns-determine-future-alliance_20260719_051226.md (FULL TEXT FMT, 1944c — Zahid NS=PRU16 test)",
    "priority_pir-16-pir-06_fmt-bn-pas-tie-up-mca-difficult-choice_20260719_051226.md (FULL TEXT FMT, 3032c — Lau Zhe Wei + Wong Chin Huat)",
    "priority_pir-16-pir-06_fmt-umno-dangerous-dance-pas-opinion_20260719_051226.md (FULL TEXT FMT opinion, 7009c — dangerous dance + Amanat Hadi 1981)",
    "priority_pir-16_fmt-lim-rejects-islamophobia-hadi-green-wave_20260719_051226.md (FULL TEXT FMT, 1905c — Lim Lip Eng + Tuan Ibrahim + green wave provenance)",
    "priority_pir-16-pir-07_fmt-bn-decide-ns-mb-candidate-only-if-wins_20260719_051226.md (FULL TEXT FMT, 1278c — Jalaluddin MB-after-PRN)",
    "priority_pir-06-pir-16_fmt-bn-pn-cooperation-avoid-vote-splits-wee_20260719_051226.md (FULL TEXT FMT, 3403c — Wee not-alliance)",
    "priority_pir-16-pir-07_nst-melaka-*_20260719_051226.md (7 headline-intel items — Ab Rauf, Anwar postpone, Melaka clears path, DAP quits, DAP backs reps — Melaka DAP withdrawal arc)",
    "priority_pir-07_nst-linggi-move-is-risky-for-ph-says-analyst-nst-online_20260719_051226.md (headline-intel — Linggi risky for PH analyst)",
    "index.md (collection summary — cycles 051226 + 064654 sections appended)"
]
sources.extend(new_sources)
data["extraction_metadata"]["sources_extracted_from"] = sources

data["entities"] = prior_entities

with OUT.open("w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

# Report
print(f"Prior entities: 167")
print(f"New entities added: {added}")
print(f"Context updates applied: {len(context_updates)}")
print(f"Total entities: {len(prior_entities)}")
print(f"By type: {by_type}")
print(f"By PIR: {by_pir}")
print(f"By priority: {by_pri}")
print(f"Output: {OUT}")
print(f"File size: {OUT.stat().st_size} bytes")
