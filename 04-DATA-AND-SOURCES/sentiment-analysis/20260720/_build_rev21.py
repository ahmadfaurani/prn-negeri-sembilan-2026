#!/usr/bin/env python3
"""
PRN Negeri Sembilan 2026 Sentiment Analysis — Revision-21 build.
Delta over rev20 (sentiment-20260720-1724.json) incorporating the
night (18:30 MYT) + latenight (19:42 MYT) raw-scrape cycles which are
NOT yet present in any processed-entities JSON (latest entity build =
entities-20260720-0734.json, 15:38 MYT). Entities derived from direct
raw-scrape article analysis.
"""
import json, copy, os

BASE = "sentiment-analysis/2026-07-20/sentiment-20260720-1724.json"
OUT  = "sentiment-analysis/2026-07-20/sentiment-20260720-1945.json"
GEN  = "2026-07-20T19:45:00+08:00"

def classify(score):
    if score < -0.20: return "negative"
    if score > 0.20:  return "positive"
    return "neutral"

with open(BASE) as f:
    d = json.load(f)
ents = d["entities"]
by_name = {e["entity"]: e for e in ents}

# ---- UPDATES to existing entities (rev20 -> rev21) ----
# value: dict with optional keys: score, trend, alert, source_count(+delta), rationale
UPD = {
 "Anwar Ibrahim (PMX)": dict(
     score=0.25, trend="declining", alert="priority", _sc=+1,
     rat="rev20 +0.30 -> rev21 +0.25. night build: KWAP eFishery RM163.4m loss defense in Dewan Negara — defends investment process ('no political interference'), frames against RM12.9b profit, MACC investigating. MCA urges PAC probe (adds opposition pressure). Competency question handled but persists. Slight further decline. [PRIORITY]."),
 "Anwar Ibrahim (PM, coalition manager)": dict(
     score=0.25, trend="declining", alert="priority", _sc=+1,
     rat="rev20 +0.30 -> rev21 +0.25. night build: KWAP eFishery defense (federal, competency). Coalition-manager posture intact but asset-misuse/fund-loss pressure adds drag. [PRIORITY]."),
 "Aminuddin Harun (PH incumbent MB, N.32 Linggi)": dict(
     score=0.52, trend="stable", alert="priority", _sc=+3,
     rat="rev20 +0.52 declining -> rev21 +0.52 stable. night/latenight build: urges integrity + condemns vandalism (MalayMail 17:05, statesman posture while campaigning in Linggi); 'Aminuddin disenangi ramai, masih harap beliau kekal di Sikamat' (Sinar — popularity acknowledged); PH manifesto launch 'kesinambungan usaha Kerajaan Perpaduan' (HarianMetro). These balance the rev20 analyst 'strategic error if fails' concern -> trend STABILIZES (was declining). Score holds. [PRIORITY]."),
 "N.32 Linggi (Aminuddin MB move + BN manifesto 24 Jul)": dict(
     score=0.26, trend="stable", alert="critical", _sc=+2,
     rat="rev20 +0.26 declining -> rev21 +0.26 stable. night build: PH manifesto launch TONIGHT at Linggi (Amirudin Shari, Klana Resort) + Aminuddin statesmanship + popularity evidence stabilizes the high-stakes battle. 'Strategic error' analyst concern persists but is now balanced. Trend stabilizes. Still [CRITICAL] (high-stakes symbolic battle; BN manifesto 24 Jul at DUN Linggi incoming)."),
 "Nor Azman Mohamad (PH N.13 Sikamat)": dict(
     score=0.15, trend="stable", alert="none", _sc=+1,
     rat="rev20 +0.10 -> rev21 +0.15. night build (Sinar): positive day-1 feedback, 'not a shock' as he often substituted Aminuddin at Sikamat, local & known ('penduduk di Sikamat dan dikenali masyarakat'), 'tidak memandang rendah lawan'. Credible PH substitute. Slight improvement."),
 "N.28 Klawang (PDM shutdown + cousins contest)": dict(
     score=0.10, trend="stable", alert="priority", _sc=+0,
     rat="rev20 +0.10 declining -> rev21 +0.10 stable. night build: PDM resolved (rev20); no fresh Klawang-specific negative. Sabotage at Klawang already captured. Trend stabilizes. [PRIORITY]."),
 "Pertang (derhaka friction, Jalaluddin)": dict(
     score=-0.15, trend="stable", alert="priority", _sc=+2,
     rat="rev20 -0.15 stable -> rev21 -0.15 stable. night build: Jalaluddin active courteous ground campaign in Jelebu/Pertang + FIRST vote-buying allegation rebuttal (button badge, not money) at Kampung Bemban. Derhaka NOT escalated; Jalaluddin conciliatory. New election-offense thread (vote-buying) offsets courtesy gain -> holds stable. [PRIORITY]."),
 "Jalaluddin Alias (NS Umno chief, BN Pertang)": dict(
     score=0.20, trend="improving", alert="priority", _sc=+2,
     rat="rev20 +0.15 -> rev21 +0.20. night build: 'BN tidak bazir masa kempen serang mana-mana pihak' + 'calon BN tidak menyentuh perkara Kerajaan Perpaduan dalam kempen' (disciplined courteous posture, Kampung Jerang) + vote-buying rebuttal (button badge). Active disciplined ground leadership + federal-state firewall reinforcement. Slight improvement. [PRIORITY]."),
 "Jalaluddin Alias (Datuk Seri) — Pertang candidate profile": dict(
     score=0.20, trend="improving", alert="priority", _sc=+2,
     rat="rev20 +0.10 -> rev21 +0.20. night build: courteous campaign + Unity-Govt-criticism-avoidance directive + vote-buying rebuttal. Disciplined leadership. (mirror of NS Umno chief entity.)"),
 "PH (Pakatan Harapan)": dict(
     score=0.38, trend="stable", alert="priority", _sc=+2,
     rat="rev20 +0.38 declining -> rev21 +0.38 stable. night build: manifesto launch 'kesinambungan usaha Kerajaan Perpaduan' (incumbency/continuity pitch) + 'Tiada perpecahan dalaman di DUN Chuah' (pushback on machinery-disunity narrative, Kenny Chiew gives full support). Stabilizes (was declining). [PRIORITY]."),
 "MCA": dict(
     score=-0.40, trend="improving", alert="priority", _sc=+1,
     rat="rev20 -0.45 -> rev21 -0.40. night build: MCA urges PAC to investigate KWAP eFishery RM163.4m loss (Sinar sidebar). Reinforces 'semak dan imbang' check-and-balance positioning on PH-govt fund loss. Defensive posture continues softening. [PRIORITY]."),
 "blue wave Johor→NS→Selangor→Putrajaya GE16 narrative (Noh Omar)": dict(
     score=0.25, trend="improving", alert="none", _sc=+2,
     rat="rev20 +0.30 -> rev21 +0.25. latenight build: Utusan commentary 'Bolehkah status quo dipertahankan?' explicitly states 'NS ≠ Johor' — pushes back on Johor-spillover assumption; Sanjeevan (Bersatu) 'gelombang Johor tidak akan sampai ke NS,' 'pengundi NS akan sekat gelombang biru.' Blue-wave narrative now ACTIVELY CONTESTED -> improving trend SLOWS. [none]."),
 "gelombang biru (blue wave) narrative": dict(
     score=0.35, trend="improving", alert="none", _sc=+2,
     rat="rev20 +0.42 -> rev21 +0.35. latenight build: Utusan 'status quo' commentary + Sanjeevan rebuttal challenge Johor→NS spillover. Narrative contested, not unopposed. Slows. [none]."),
 "Bersatu kacau daun narrative (Khaled)": dict(
     score=-0.65, trend="declining", alert="critical", _sc=+1,
     rat="rev20 -0.70 -> rev21 -0.65. night build: Sanjeevan (Bersatu Jeram Padang candidate) directly rebutts Khaled's 'kacau daun' — 'Khaled angkuh,' 'Johor ≠ NS,' 'Bersatu won't be buried despite PN conflict.' FIRST active Bersatu counter-narrative. Slight moderation of decline (narrative now contested, not unopposed). Still [CRITICAL] per director 'kacau daun' rule."),
 "Bersatu": dict(
     score=-0.90, trend="stable", alert="critical", _sc=+1,
     rat="rev20 -0.92 declining -> rev21 -0.90 stable. night build: Sanjeevan rebuttal ('Apa juga yang berlaku kepada Bersatu dalam PN, ia tidak akan menyebabkan parti ini terkubur') = first active Bersatu defense. Decline MODERATES + STABILIZES. Still deep-negative [CRITICAL] per director Bersatu sharp-negative internal-fracture rule."),
 "Bersatu in disarray / Bersatu exit imminent (characterisation)": dict(
     score=-0.75, trend="declining", alert="priority", _sc=+1,
     rat="rev20 -0.78 -> rev21 -0.75. night build: Sanjeevan rebuttal moderates 'in disarray' characterisation slightly. Still declining (no hard-news 'exit imminent' corroboration). [PRIORITY]."),
 "Bersatu heading for wipeout in NS (analyst consensus)": dict(
     score=-0.75, trend="stable", alert="priority", _sc=+1,
     rat="rev20 -0.78 -> rev21 -0.75. night build: Sanjeevan 'Bersatu won't be buried.' Moderates wipeout framing slightly. [PRIORITY]."),
 "PDM Klawang reopen": dict(
     score=-0.10, trend="improving", alert="priority", _sc=+0,
     rat="rev20 -0.15 -> rev21 -0.10. night build: resolved (rev20); no escalation; further drift toward neutral. [PRIORITY]."),
 "PH manifesto launch (20 Jul, continuity of Tok Min)": dict(
     score=0.40, trend="improving", alert="none", _sc=+1,
     rat="rev20 +0.35 -> rev21 +0.40. night build (HarianMetro): PH manifesto launch tonight (Amirudin Shari, Klana Resort) 'kesinambungan usaha Kerajaan Perpaduan, beri manfaat semua lapisan.' Aminuddin: 'bukan harapan untuk dengar tapi harapan untuk laksanakan.' Incumbency/continuity pitch strengthens. [none]."),
 "DUN Chuah candidacy controversy RESOLVED": dict(
     score=0.20, trend="improving", alert="none", _sc=+1,
     rat="rev20 +0.05 -> rev21 +0.20. night build (Utusan): 'Tiada perpecahan dalaman di DUN Chuah' — Aminuddin confirms issue resolved, Kenny Chiew gives full support to PH candidates across Chuah/Lukut/Seri Tanjung/Bagan Pinang/Linggi. Stronger resolution; pushback on machinery-disunity narrative. Improving."),
 "Alzafny Ahmad (Datuk)": dict(
     score=0.10, trend="stable", alert="none", _sc=+2,
     rat="rev20 +0.05 -> rev21 +0.10. night build: confirms vandalism investigations (Jempol/Palong + Chembong ongoing) + royal-institution arrest (Sedition/ Penal/CMA). Active effective policing across campaign-safety + royal-institution fronts. Slight improvement."),
 "Akmal Saleh (Dr Akmal Saleh)": dict(
     score=-0.30, trend="declining", alert="priority", _sc=+1,
     rat="rev20 -0.30 stable -> rev21 -0.30 declining. night build (Sinar): 'menggelupur sangat bila kita nak bersatu' bidas AMK + 'DAP ketandusan idea bawa penipuan baharu PRN NS.' Escalates intra-unity-govt friction (UMNO Youth vs PKR Youth). Trend -> declining (escalating). [PRIORITY]."),
 "Jeram Padang (4-corner, Sri Sanjeevan quorum-critic)": dict(
     score=-0.05, trend="stable", alert="none", _sc=+1,
     rat="rev20 -0.05 -> rev21 -0.05. night build: Sanjeevan (Bersatu candidate here) launches 'kacau daun' rebuttal + blue-wave pushback from this seat. Seat sentiment unchanged; rebuttal captured in PIR-16 narrative entity."),
 "derhaka friction (Pertang)": dict(
     score=-0.15, trend="improving", alert="priority", _sc=+1,
     rat="rev20 -0.15 improving -> rev21 -0.15 improving (carry). latenight build: royal-institution arrest (PRN-adjacent) connects to 'derhaka' concept (menentang raja/Undang Yang Empat) but is NOT defector-framing intensification at Pertang. Derhaka NOT escalated; Jalaluddin conciliatory. Holds improving. [PRIORITY]."),
}

# ---- NEW entities (rev21) ----
NEW = [
 dict(entity="Asyraf Wajdi Dusuki (UMNO Sec-Gen)", pir_tag="PIR-06", score=0.35,
   rat="NEW rev21 (latenight build, HarianMetro+Buletin TV3). UMNO Sec-Gen Datuk Dr Asyraf Wajdi Dusuki: 'UMNO tidak akan sesekali menebuk atap Kerajaan Perpaduan' until dissolved for GE. STRONGEST formal UMNO statement on Unity Govt stability during NS campaign. Carries formal party weight (Sec-Gen, #2 admin). References 'Perjanjian Kerajaan Perpaduan.' Cooperation-STABILIZING -> reduces critical-risk on unity-govt-fracture axis (alert none, not critical). Pairs with KJ 'isyarat' + Jalaluddin ground directive. [none]."),
 dict(entity="menebuk atap reassurance (UMNO unity-govt stability)", pir_tag="PIR-06", score=0.35,
   rat="NEW rev21. Narrative entity: UMNO's coordinated message that state-level BN-PN cooperation ≠ federal Unity Govt destabilization. Asyraf Wajdi (formal, latenight) + Jalaluddin 'calon BN tidak menyentuh Kerjaan Perpaduan dalam kempen' (ground, night) + KJ 'isyarat kepada PH' (dusk). Federal-state firewall reinforcement. Positive/stabilizing."),
 dict(entity="Akmal Saleh bidas AMK (menggelupur sangat bila kita nak bersatu)", pir_tag="PIR-06", score=-0.20,
   rat="NEW rev21 (night build, Sinar). Akmal (UMNO Youth chief) counter-attacks AMK (PKR Youth): 'menggelupur sangat bila kita nak bersatu,' 'cium tapak kaki' retort (if UMNO-PAS = cium tapak kaki, then PKR-DAP = cium tapak kaki DAP), 'DAP ketandusan idea bawa penipuan baharu PRN NS.' Intra-unity-govt friction (UMNO Youth vs PKR Youth). Escalates penyatuan Melayu push vs PH-Youth resistance. [PRIORITY]."),
 dict(entity="AMK (Angkatan Muda Keadilan / PKR Youth)", pir_tag="PIR-06", score=-0.25,
   rat="NEW rev21 (night build, Sinar). PKR Youth (AMK), Selangor Sec Ghafurullah Ismail: claims UMNO now 'bergantung kepada parti lawan demi meraih kuasa,' no longer able to stand on own strength, 'cium tapak kaki' of PAS. Target of Akmal's rebuttal. Intra-unity-govt friction. DISTINCT from AMH (PH Youth wing coalition). [PRIORITY]."),
 dict(entity="Sanjeevan bidas Khaled 'kacau daun' (Bersatu rebuttal)", pir_tag="PIR-16", score=-0.25,
   rat="NEW rev21 (night build, FMT). R Sri Sanjeevan (Bersatu Ketua Bersekutu, Jeram Padang candidate): 'Khaled angkuh,' 'Johor ≠ NS,' 'gelombang Johor tidak akan sampai ke NS,' 'pengundi NS akan sekat gelombang biru dan kebangkitan Umno-BN di bawah Zahid,' 'Bersatu won't be buried despite PN conflict.' FIRST active Bersatu counter-narrative to 'kacau daun.' Moderates dominant 'Bersatu in disarray/wipeout' framing. [PRIORITY]."),
 dict(entity="Utusan commentary: status quo dipertahankan?", pir_tag="PIR-16", score=0.05,
   rat="NEW rev21 (latenight build, Utusan commentary). Hard-news analytical commentary framing the CENTRAL question: 'Bolehkah status quo dipertahankan?' NS ≠ Johor (counters blue-wave spillover); stable moderate electorate prioritizes 'prestasi pentadbiran'; Aminuddin track record 'tidak boleh dinafikan.' Frames dominant narrative contestation: PH (performance+continuity) vs BN-PN (penyatuan Melayu + blue wave). Counters blue-wave spillover assumption. [PRIORITY]."),
 dict(entity="Utusan commentary: gelanggang PRN NS mula dibuka", pir_tag="PIR-16", score=0.00,
   rat="NEW rev21 (latenight build, Utusan commentary). 'No coalition has advantage' open-contest framing. 889,490 voters / 36 DUN / ~3 years since 2023 election (unexpectedly early dissolution). Pairs with status-quo commentary. Neutral analytical baseline."),
 dict(entity="Jalaluddin nafi beri wang (button badge vote-buying rebuttal)", pir_tag="PIR-07", score=-0.20,
   rat="NEW rev21 (latenight build, HarianMetro). FIRST explicit vote-buying allegation/rebuttal of the campaign. Jalaluddin (BN Pertang) denies giving money at Kampung Bemban, Jelebu — items were 'button badges,' not cash. Election-offense thread (SPRM-relevant monitoring). [PRIORITY]."),
 dict(entity="BN courteous campaign posture (Jalaluddin — no Unity Govt criticism)", pir_tag="PIR-06", score=0.30,
   rat="NEW rev21 (night build, Utusan). Jalaluddin (NS UMNO chief) at Kampung Jerang: 'BN tidak bazir masa kempen serang mana-mana pihak' + 'calon BN tidak menyentuh perkara Kerjaan Perpaduan dalam kempen.' Disciplined ground-level message reinforcing federal-state firewall. Pairs with Asyraf Wajdi formal assurance. Cooperation-stabilizing."),
 dict(entity="13,263 postal votes issued today (EC)", pir_tag="PIR-07", score=0.00,
   rat="NEW rev21 (night build, Utusan). EC operational milestone: 12,669 Cat 1A (petugas/police/military/media) + 343 Cat 1B (overseas) + 251 Cat 1C (security/health). Issued in presence of all candidate reps. Early voting 28 Jul; polling 1 Aug. Neutral logistical baseline."),
 dict(entity="Lelaki ditahan hina institusi Diraja NS (royal institution)", pir_tag="PIR-07", score=-0.30,
   rat="NEW rev21 (latenight build, Utusan). 52-year-old arrested for insulting NS royal institution (Undang Yang Empat) on social media. Sedition Act S4 + Penal Code S505 + CMA S233. Content uploaded 17 Jul (nomination day). PRN-adjacent; connects to 'derhaka' concept (menentang raja/Undang Yang Empat) per BN Palong candidate's framing. [PRIORITY] (PRN-adjacent, campaign-safety/legality)."),
 dict(entity="Anwar defends KWAP eFishery (RM163.4m loss)", pir_tag="PIR-06", score=-0.05,
   rat="NEW rev21 (night build, MalayMail). PM/finance minister defends KWAP investment process in Dewan Negara: 'no political interference,' RM12.9b profit puts RM160m setback in perspective, MACC investigating, 'even world-renowned auditors approve something, no guarantee of success.' Competency question handled competently. Federal (separate from PRN) -> keeps Anwar roughly stable. [none]."),
 dict(entity="MCA urges PAC probe KWAP eFishery", pir_tag="PIR-16", score=0.10,
   rat="NEW rev21 (night build, Sinar sidebar). MCA urges PAC to investigate KWAP RM163.4m eFishery loss. MCA acting as check-and-balance on PH-govt fund loss — reinforces 'semak dan imbang' positioning (distinct from MCA entity which tracks overall posture)."),
 dict(entity="Bersama (Rafizi) dimalukan Melaka (analyst)", pir_tag="PIR-16", score=-0.50,
   rat="NEW rev21 (night build, Awani/Sinar). UUM analyst Prof Mohamad Faisol Keling: after losing all 15 Johor DUN (lost deposits), Bersama (Rafizi's party) expected to be humiliated again in Melaka PRN. 'Parti pengacau' (disruptor) — Tony Pua's label, broke PH votes at 2 Johor seats. Bersama confirms skipping PRN16 to focus on Melaka. Reinforces spoiler/pecah-undi narrative. Melaka PH-BN fracture context. [PRIORITY]."),
]

# ---- apply updates ----
for name, u in UPD.items():
    if name not in by_name:
        print("WARN update target not found:", name); continue
    e = by_name[name]
    e["score"] = u.get("score", e["score"])
    e["trend"] = u.get("trend", e["trend"])
    e["alert"] = u.get("alert", e["alert"])
    if "_sc" in u: e["source_count"] = e.get("source_count", 0) + u["_sc"]
    e["rationale"] = u["rat"]
    e["sentiment"] = classify(e["score"])

# ---- append new entities ----
for n in NEW:
    ne = dict(entity=n["entity"], pir_tag=n["pir_tag"], score=n["score"],
              sentiment=classify(n["score"]),
              trend="stable", alert="none", source_count=1, rationale=n["rat"])
    # set alert/trend where implied by rationale keywords
    r = str(n["rat"])
    if "[CRITICAL]" in r: ne["alert"]="critical"
    elif "[PRIORITY]" in r: ne["alert"]="priority"
    if "declining" in r[:60] or "Escalates" in r or "escalat" in r.lower()[:80]:
        ne["trend"]="declining"
    elif "improving" in r[:60] or "strengthen" in r.lower()[:80] or "Improving" in r[:80]:
        ne["trend"]="improving"
    ents.append(ne)

# ---- recompute metadata counts ----
crit = sum(1 for e in ents if e["alert"]=="critical")
prio = sum(1 for e in ents if e["alert"]=="priority")
none = sum(1 for e in ents if e["alert"]=="none")

meta = copy.deepcopy(d["metadata"])
meta.update(dict(
    version="revision-21",
    generated=GEN,
    generated_utc="2026-07-20T11:45:00Z",
    prior_revision_file="sentiment-analysis/2026-07-20/sentiment-20260720-1724.json",
    prior_revision="revision-20 (2026-07-20T17:24:00+08:00, 336 entities, 25 critical/109 priority/202 none), built on entities-20260720-0734.json (72-entity delta)",
    entity_build="DELTA over rev20 incorporating night (18:30 MYT) + latenight (19:42 MYT) raw-scrape cycles NOT yet present in any processed-entities JSON (latest entity build = entities-20260720-0734.json @ 15:38 MYT). Entities derived from direct raw-scrape article analysis: Asyraf Wajdi 'menebuk atap' unity-govt assurance (HarianMetro+Buletin TV3), Akmal bidas AMK 'menggelupur sangat bila kita nak bersatu' + 'DAP ketandusan idea' (Sinar), Sanjeevan bidas Khaled 'kacau daun' Bersatu rebuttal (FMT), Aminuddin urges integrity/condemns vandalism (MalayMail), 'Aminuddin disenangi ramai harap kekal di Sikamat' Nor Azman (Sinar), Utusan commentary 'status quo dipertahankan?' + 'gelanggang mula dibuka' (NS≠Johor pushback), PH manifesto launch 'kesinambungan' (HarianMetro), 'Tiada perpecahan dalaman DUN Chuah' (Utusan), 13,263 postal votes issued (Utusan/EC), Jalaluddin nafi beri wang button badge + courteous campaign (HarianMetro/Utusan), lelaki ditahan hina institusi Diraja NS (Utusan), Anwar defends KWAP eFishery RM163.4m (MalayMail), MCA urges PAC probe KWAP (Sinar), Bersama/Rafizi dimalukan Melaka (Awani/Sinar).",
    director_cycle="19 Jul 17:25 MYT (4th carry-forward) - 10th sentiment build (night+latenight delta, Day-2 evening)",
    entity_count=len(ents), critical_count=crit, priority_count=prio, none_count=none,
))

out = dict(metadata=meta, entities=ents)
os.makedirs("sentiment-analysis/2026-07-20", exist_ok=True)
with open(OUT, "w") as f:
    json.dump(out, f, ensure_ascii=False, indent=2)
print("WROTE", OUT)
print("entity_count:", len(ents), "| critical:", crit, "| priority:", prio, "| none:", none)
print("new entities added:", len(NEW))
print("updates applied:", len(UPD))
