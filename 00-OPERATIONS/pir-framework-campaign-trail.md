# Negeri Sembilan PRN 2026 — Campaign Trail PIR Framework

**Classification:** TLP:AMBER  
**State:** Negeri Sembilan  
**Total DUN:** 36 constituencies (103 candidates)  
**Election Date:** 1 August 2026  
**Framework Version:** 1.0 (Campaign Trail Tracker)  
**Created:** 2026-07-23  
**Parent Framework:** pir-framework.md (NS-01 to NS-18)  
**Supporting Cronjob:** `10d9c6242b4e` — Campaign Trail Tracker (09:00/17:00/01:00 MYT)

---

## 1. Purpose

This framework defines the Priority Intelligence Requirements for candidate-level campaign trail monitoring during the PRN Negeri Sembilan 2026 campaign period (Phase 3: 18–31 July 2026). It complements the main PIR framework (NS-01 to NS-18) with granular, per-candidate tracking of campaign events, statements, incidents, and momentum across all 36 DUN constituencies.

**Scope:** All 103 confirmed candidates across 36 DUNs, plus national coalition leaders campaigning in NS.

**Relationship to existing PIRs:**
- **NS-10** (Candidate Acceptance) → CT PIRs provide the field evidence for candidate assessment
- **NS-11** (Opposition Strategy) → CT PIRs capture opposition campaign events and resource deployment
- **NS-18** (Campaign-Phase Readiness) → CT PIRs feed Phase 3 daily DUN movement reporting

---

## 2. Candidate Campaign Contest Configuration

| Contest Type | DUN Count | DUN Codes | Monitoring Priority |
|-------------|-----------|-----------|-------------------|
| Straight fight (2 candidates) | 11 | N.01, N.08, N.11, N.18, N.19, N.21, N.26, N.27, N.29, N.35, N.36 | Standard |
| Three-cornered (3 candidates) | 21 | N.02, N.03, N.04, N.05, N.06, N.09, N.12, N.13, N.14, N.15, N.16, N.17, N.20, N.23, N.24, N.25, N.28, N.30, N.31, N.32, N.34 | **High** |
| Four-cornered (4 candidates) | 2 | N.07, N.22 | **Critical** |
| Five-cornered (5 candidates) | 2 | N.10, N.33 | **Critical** |

**High-Profile Candidates (mandatory tracking every cycle):**
- Aminuddin Harun (PH) — Incumbent MB, N.13 Sikamat
- Mohamad Hasan / Tok Mat (BN) — Former MB, high-profile campaigner
- Loke Siew Fook (PH) — Federal minister, N.01 Chennah
- Jalaluddin Alias (BN) — Former state EXCO, N.02 Pertang
- Danni Rais (PN) — N.04 Klawang
- All incumbents across 36 DUNs

**Party Distribution:** PH 36 | BN 25 | BERSATU 24 | PN 11 | BEBAS 4 | ASLI 1 | BERJASA 1 | PSM 1

---

## 3. Campaign Trail PIR Register (CT-01 to CT-08)

| PIR ID | Priority Requirement | Primary Decision | Reporting Cadence | Escalation Owner |
|--------|----------------------|-------------------|-------------------|-----------------|
| **CT-01** | Candidate campaign event tracking | Event-targeting and counter-scheduling | 3x daily | Field Operations Lead |
| **CT-02** | Coalition leader visit tracking | Leadership deployment response | 3x daily | State Intelligence Director |
| **CT-03** | Campaign trail incidents & election offences | Legal response and public statements | Event-driven (immediate) | Legal & Political Secretariat |
| **CT-04** | Candidate messaging & statement tracking | Communications response and narrative counter | 3x daily | Narrative Intelligence Lead |
| **CT-05** | Campaign trail momentum assessment | Resource reallocation | Daily (evening cycle) | Electoral Intelligence Lead |
| **CT-06** | Social media campaign activity | Digital response and content strategy | 3x daily | Information Integrity Cell |
| **CT-07** | Multi-cornered fight dynamics | Vote-splitting risk and counter-strategy | Daily (evening cycle) | Opposition Analysis Cell |
| **CT-08** | Campaign resource & machinery deployment | Ground operations reinforcement | Daily | State Operations Director |

---

## 4. CT-01: Candidate Campaign Event Tracking

**Priority Intelligence Question:**
What ceramah, rallies, walkabouts, and public events is each candidate conducting across all 36 DUNs, and what is the attendance and reception at each?

**Decisions Supported:**
- Event scheduling and counter-programming
- Candidate deployment priorities
- Resource allocation to high-activity DUNs
- Identification of campaign dead zones (DUNs with no activity)

**Collection Requirements:**

For each candidate event, collect:
- **Event type:** Ceramah | Mega ceramah | Walkabout | Meet-and-greet | Market visit | Community program | Religious event | Door-to-door | Roadshow
- **Location:** Specific venue, polling district, DUN, parliamentary constituency
- **Date & time:** Scheduled and actual start/end
- **Speakers:** Candidate + guest speakers (coalition leaders, local figures)
- **Attendance estimate:** With source attribution ("police estimate", "organiser claim", "eyewitness", "journalist report")
- **Crowd reception:** Enthusiasm level, notable moments, audience composition (demographic visible signs)
- **Content highlights:** Key announcements, promises, attacks
- **Source URL:** Required for every event

**Coverage Standard:**
- All 36 DUNs must be checked every cycle
- For DUNs with no reported activity: explicitly state "No campaign trail activity reported this cycle"
- Priority focus on 25 High/Critical DUNs (3-cornered and above)
- Minimum 8-10 web searches per cycle

**Escalation Triggers:**
- A candidate cancels multiple scheduled events without explanation
- A DUN records zero campaign activity across two consecutive cycles
- Attendance at a major ceramah falls below 50% of organizer's claimed expectation
- A candidate is absent from their own DUN for 48+ hours during campaign period

---

## 5. CT-02: Coalition Leader Visit Tracking

**Priority Intelligence Question:**
Which national and coalition leaders are campaigning in Negeri Sembilan, which constituencies are they visiting, and what is the strategic purpose and impact of each visit?

**Tracked Leaders:**
- **PH/Pakatan:** Anwar Ibrahim (PM), Zahid Hamidi (DPM), Rafizi Ramli, Anthony Loke, other cabinet ministers
- **BN/UMNO:** Zahid Hamidi (UMNO President), Mohamad Hasan (if campaigning for others), Khairy Jamaluddin, other UMNO supreme council members
- **PN/BERSATU:** Muhyiddin Yassin, Hamzah Zainudin, Azmin Ali, Ahmad Faizal Azumu
- **PAS:** Abdul Hadi Awang, Takiyuddin Hassan, PAS central committee
- **State leaders:** MB Aminuddin Harun (campaigning outside his own DUN), state EXCO members

**Collection Requirements:**

For each leader visit, record:
- **Leader name & title** (federal position, party position)
- **DUN(s) visited** — which constituencies, which specific locations
- **Event type** — ceramah, walkabout, officiating ceremony, press conference
- **Purpose** — fundraising, candidate support, voter engagement, symbolic show of force
- **Strategic significance** — why this DUN? Is it marginal? Is the candidate struggling?
- **Local response** — crowd size, media coverage, social media reaction
- **Follow-on events** — did the visit generate additional local activity?
- **Source URL**

**Impact Assessment Framework:**

| Impact Level | Indicators |
|-------------|-----------|
| **High Impact** | Visit generates sustained media coverage (2+ days), crowd >1,000, visible social media amplification, candidate's visibility materially improved |
| **Moderate Impact** | Single-day media coverage, crowd 300–1,000, some social media discussion |
| **Low Impact** | Minimal coverage, crowd <300, limited social media trace |
| **Counterproductive** | Visit generates negative coverage, low turnout despite VIP presence, local backlash reported |

**Escalation Triggers:**
- PM or DPM visits a seat currently classified as Competitive or Vulnerable
- Multiple coalition leaders visit the same DUN within 48 hours (surge indicator)
- A leader visit is met with notable protest or low turnout
- A leader cancels or skips a planned NS visit (signals withdrawal of support?)

---

## 6. CT-03: Campaign Trail Incidents & Election Offences

**Priority Intelligence Question:**
What incidents, disruptions, heckling, or election offences are occurring on the campaign trail, and what is the legal and reputational exposure?

**Incident Categories:**

| Category | Examples | Reporting Priority |
|----------|---------|-------------------|
| **Election Offence** | Treating, intimidation, poster vandalism, campaigning on polling day, corruption | IMMEDIATE |
| **Disruption** | Heckling, walkout, ceramah interrupted, verbal altercation | Same cycle |
| **Security Incident** | Physical altercation, crowd control failure, threat to candidate, police called | IMMEDIATE |
| **EC/SPR Complaint** | Formal complaint lodged, investigation opened, show-cause issued | Same cycle |
| **Police Report** | Police report filed re: campaign conduct, sedition, defamation | IMMEDIATE |
| **Coalition Friction** | Seat dispute, running mate disagreement, public disagreement between allies | Same cycle |
| **Misinformation** | False claims about candidate, fake event announcements, doctored images | Same cycle |
| **Access Denial** | Candidate denied entry to a venue, community, or event | Same cycle |

**Collection Requirements:**

For each incident, record:
- **Incident type** (from above categories)
- **DUN & location** — where did it occur
- **Parties involved** — which candidates/coalitions
- **Description** — factual account (2-3 sentences)
- **Legal status** — police report filed? EC complaint? Investigation status?
- **Reputational impact** — media coverage, social media reaction
- **Source URL** + [UNVERIFIED] tag if not independently confirmed

**Evidence Standard:**
- IMMEDIATE incidents → deliver to Telegram the same cycle, do not wait for file write
- Flag all unverified reports clearly with [UNVERIFIED]
- Use [ASSESSMENT] for analytical judgments about impact
- Distinguish between alleged and confirmed offences

**Escalation Triggers:**
- Any election offence reported — immediate escalation to Legal & Political Secretariat
- A candidate's safety is threatened — immediate security escalation
- EC issues show-cause to any NS candidate — immediate legal escalation
- Three or more incidents in a single DUN within 24 hours — pattern flag
- A coalition friction incident suggests seat negotiation breakdown — strategic escalation

---

## 7. CT-04: Candidate Messaging & Statement Tracking

**Priority Intelligence Question:**
What are candidates saying at campaign events, and which statements are defining the narrative battle in each DUN?

**Statement Categories:**

| Category | Definition | Collection Priority |
|----------|-----------|-------------------|
| **Policy Promise** | Specific commitment to a project, program, or policy | High — track for accountability |
| **Attack on Opponent** | Direct criticism or accusation against another candidate/party | High — track for counter-narrative |
| **Achievement Claim** | Claim about own or party's record/performance | Medium — verify for accuracy |
| **Defensive Statement** | Response to criticism, explanation of controversy | Medium — track for damage control |
| **Coalition Signal** | Statement about coalition unity, seat deals, post-election plans | High — strategic indicator |
| **Emotional Appeal** | Cultural, religious, or identity-based appeal | Medium — narrative tracking |
| **Call to Action** | Mobilisation, GOTV, volunteer recruitment | Low — operational |

**Collection Requirements:**

For each notable statement, record:
- **Candidate name, DUN, party**
- **Statement summary** (verbatim quote if available, otherwise paraphrase with attribution)
- **Category** (from above table)
- **Context** — at what event, in response to what
- **Target** — who/what is the statement about?
- **Theme** — cost of living, governance, race/religion, development, integrity, etc.
- **Reception** — crowd response, social media reaction, media coverage
- **Source URL**

**Notable Quote Threshold:**
- A statement is "notable" if it: (a) generates media coverage, (b) goes viral on social media, (c) contradicts party line, (d) makes a specific quantifiable promise, (e) attacks a named individual, or (f) signals a coalition shift
- Do not record routine campaign talking points unless they are novel to that candidate

**Escalation Triggers:**
- A candidate makes a statement contradicting coalition leadership's official position
- A statement generates a formal complaint (police, EC, defamation)
- A promise is made that exceeds the state's fiscal capacity (flag for verification)
- An attack on an opponent is demonstrably false (trigger NS-15 misinformation protocol)

---

## 8. CT-05: Campaign Trail Momentum Assessment

**Priority Intelligence Question:**
Based on campaign trail activity, which candidates are gaining or losing momentum, and where is the energy shifting?

**Momentum Indicators:**

| Indicator | Direction | Weight |
|-----------|----------|--------|
| Event frequency | More events = positive momentum | High |
| Attendance trend | Increasing attendance = positive | High |
| Coalition leader visits | VIP visits = confidence in seat | High |
| Social media buzz | Increasing engagement = positive | Medium |
| Media coverage volume | More coverage = visibility | Medium |
| Volunteer mobilisation | More volunteers = ground strength | Medium |
| Crowd enthusiasm | Visible enthusiasm = positive | Medium |
| Opponent's avoidance | Opponent skipping DUN = weakness signal | Low |

**Momentum Assessment Rating:**

| Rating | Definition |
|--------|-----------|
| **Surging** | Multiple positive indicators, clear upward trajectory |
| **Building** | Two or more positive indicators, gradual improvement |
| **Steady** | No significant change from baseline |
| **Fading** | Two or more negative indicators, declining activity |
| **Stalled** | Minimal campaign activity, candidate appears disengaged |
| **Insufficient Data** | Not enough trail activity to assess |

**Reporting Requirement:**
- Every evening cycle (17:00 MYT), produce a momentum snapshot for all 36 DUNs
- Highlight any DUN where momentum has shifted category since the previous assessment
- Identify the top 3 momentum gainers and top 3 momentum losers statewide

**Escalation Triggers:**
- A candidate in a Competitive seat moves to Fading or Stalled
- An opposition candidate is Surging in a seat currently classified as Favourable
- A candidate's event frequency drops by >50% between cycles
- No campaign activity recorded in a DUN for 24+ hours

---

## 9. CT-06: Social Media Campaign Activity

**Priority Intelligence Question:**
What candidate and coalition social media content is generating engagement in NS, and which posts are going viral or shaping the digital campaign?

**Platforms Monitored:**
- **Facebook** — primary platform for Malaysian political content
- **TikTok** — growing influence, especially among youth voters
- **X (Twitter)** — journalist and political commentator discourse
- **Instagram** — candidate lifestyle and community engagement content
- **WhatsApp** — viral forwards (tracked via news reports of WhatsApp circulation)

**Collection Requirements:**

For each notable social media item:
- **Candidate/coalition** — who posted
- **Platform** — which platform
- **Content type** — video, image, live stream, text post, story
- **Content summary** — 1-2 sentence description
- **Engagement metrics** — views, likes, shares, comments (if available)
- **Viral status** — Is it being shared beyond the candidate's own audience?
- **Sentiment** — positive/negative/mixed reception
- **Cross-platform spread** — did it migrate from one platform to another?
- **Source URL** (direct link if available, otherwise platform search reference)

**Viral Threshold:**
- Facebook: >10,000 interactions (likes + shares + comments)
- TikTok: >50,000 views
- X: >1,000 retweets or >500 quote tweets
- WhatsApp: reported as circulating by news sources

**Escalation Triggers:**
- A candidate's post goes viral with negative sentiment (damage control)
- An opposition candidate's positive content goes viral in a Competitive DUN
- Coordinated inauthentic behaviour detected (same content posted across multiple accounts)
- A doctored or manipulated media item is gaining traction (trigger NS-15 protocol)

---

## 10. CT-07: Multi-Cornered Fight Dynamics

**Priority Intelligence Question:**
In the 25 multi-cornered DUNs, how are candidates distributing their attacks, and what is the vote-splitting risk for each coalition?

**Contest Breakdown:**
- 21 three-cornered fights (PH vs BN vs BERSATU/PN)
- 2 four-cornered fights (N.07 Jeram Padang, N.22 Rahang)
- 2 five-cornered fights (N.10 Nilai, N.33 Sri Tanjung)

**Collection Requirements:**

For each multi-cornered DUN, track:
- **Attack direction matrix** — which candidate is attacking which?
  - PH → BN? PH → BERSATU? BN → PH? BN → BERSATU? BERSATU → PH? BERSATU → BN?
- **Alliance signals** — are any candidates implicitly aligned? (e.g., BN and PAS not attacking each other)
- **Vote-splitting risk** — which coalition's vote is most likely to split?
- **Second-preference indicators** — if a voter's first choice is unviable, where does the vote go?
- **Strategic voting messaging** — is anyone telling voters to "vote strategically"?
- **Independent/minor party impact** — are BEBAS, ASLI, BERJASA, PSM candidates drawing from one coalition more than others?

**Attack Direction Matrix Format:**
```
         PH    BN    BERSATU  PN    Others
PH       —     ↗↗    ↗       ↗     ·
BN       ↗↗    —     ↗       ·     ·
BERSATU  ↗↗    ↗↗    —       ↗     ·
PN       ↗     ·     ↗       —     ·
```
(↗ = attacking, ↗↗ = heavily attacking, · = not attacking, ↓ = defending against)

**Assessment Output:**
For each multi-cornered DUN, produce:
1. Which coalition is most at risk of vote-splitting
2. Which candidate is the primary target of attacks (under pressure)
3. Whether any implicit alliance is visible
4. Net beneficiary of the multi-cornered configuration
5. Confidence rating (High/Moderate/Low)

**Escalation Triggers:**
- A four or five-cornered fight shows signs of consolidation (one candidate surging at others' expense)
- An implicit alliance becomes explicit (public statements of support)
- Vote-splitting risk for the governing coalition exceeds 50% probability
- A minor party candidate begins outperforming a major coalition candidate

---

## 11. CT-08: Campaign Resource & Machinery Deployment

**Priority Intelligence Question:**
What campaign resources, volunteers, and machinery is each candidate deploying on the ground, and where are operations strongest or weakest?

**Resource Categories:**

| Category | Indicators | Collection Method |
|----------|-----------|-------------------|
| **Volunteer mobilisation** | Number of volunteers visible at events, t-shirt distribution, door-to-door teams | Event observation, social media |
| **Material deployment** | Banners, posters, flyers, buntings, flags — density and freshness | Drive-through reports, social media photos |
| **Ground operations** | Operations room (pusat kempen) status, staffing, activity level | Local reports |
| **Transportation** | Vehicles deployed, shuttle services for voters, campaign convoys | Event observation |
| **Digital operations** | Social media posting frequency, paid advertising, influencer engagement | Platform monitoring |
| **Financial indicators** | Scale of events, production quality of materials, paid ads (indirect proxy) | Observation |

**Deployment Rating:**

| Rating | Indicators |
|--------|-----------|
| **Heavy** | Multiple visible teams, frequent events, dense signage, active digital operations |
| **Moderate** | Regular events, some signage, periodic digital activity |
| **Light** | Minimal events, sparse signage, limited digital presence |
| **Minimal/None** | No visible campaign activity |
| **Insufficient Data** | Cannot assess from available sources |

**Reporting:**
- Daily evening cycle: deployment rating for each DUN
- Flag any DUN where deployment rating has changed since previous assessment
- Cross-reference with NS-16 (Machinery Readiness) for discrepancies

**Escalation Triggers:**
- A Competitive DUN shows Light or Minimal deployment by the governing coalition
- An opposition candidate shows Heavy deployment in a seat classified as Secure
- Deployment suddenly increases in the final 72 hours of campaign (surge indicator)
- A candidate's operations room is reported as closed or inactive during campaign period

---

## 12. Reporting Integration

### Feed to Existing PIRs

| Campaign Trail PIR | Feeds Into | How |
|-------------------|-----------|-----|
| CT-01 (Events) | NS-10 (Candidate Acceptance) | Event frequency and attendance as acceptance proxy |
| CT-02 (Leader Visits) | NS-01 (Statewide Position) | VIP deployment patterns as confidence indicator |
| CT-03 (Incidents) | NS-15 (Misinformation) + NS-13 (Sensitivities) | Incident triggers for legal/cultural escalation |
| CT-04 (Messaging) | NS-14 (Narratives) | Candidate statements feed narrative tracking |
| CT-05 (Momentum) | NS-04 (DUN Risk) | Momentum shift triggers DUN reclassification |
| CT-06 (Social Media) | NS-14 (Narratives) + NS-15 (Misinformation) | Viral content as narrative velocity indicator |
| CT-07 (Multi-cornered) | NS-11 (Opposition Strategy) | Vote-splitting risk feeds opposition analysis |
| CT-08 (Resources) | NS-16 (Machinery Readiness) | Ground deployment validates/contradicts machinery reports |

### Daily Intelligence Brief Integration

Campaign Trail PIR outputs feed the evening Intelligence Brief (21:00 MYT) via:
1. **Executive Summary** — top 3-5 campaign trail developments
2. **Critical DUN Updates** — momentum changes, incidents, resource shifts
3. **Narrative Environment** — notable candidate statements, viral content
4. **Early-Warning Register** — incidents, election offences, coalition friction
5. **Command Decisions** — recommended responses to campaign trail developments

### Output Location
- Full reports: `02-CONSTITUENCY-INTELLIGENCE/campaign-trails/YYYYMMDD/PRN-NS-CAMPAIGN-TRAIL-YYYYMMDD-HHMM.md`
- Telegram delivery: concise summary (top developments, incidents, upcoming events)
- Source data: `04-DATA-AND-SOURCES/raw-scrapes/YYYYMMDD/` (from Collection job)

---

## 13. Analytical Standards

### Evidence Classification (Campaign Trail Specific)

| Type | Definition | Example |
|------|-----------|---------|
| **Confirmed Event** | Reported by 2+ independent news sources | "Aminuddin Harun held ceramah at Taman Sri sendayan — confirmed by Sinar Harian + BH" |
| **Single-Source Event** | Reported by one news source only | "Danni Rais walkabout reported only by FMT" |
| **Social Media Reported** | Posted by candidate or attendees on social media | "Candidate's Facebook live stream of ceramah" |
| **Organiser Claimed** | Stated by organisers without independent verification | "Organiser claims 2,000 attendance" |
| **Unverified Report** | Circulating but not confirmed | "WhatsApp forward about cancelled event [UNVERIFIED]" |

### Attendance Assessment Rules
- Always attribute source: "police estimate", "organiser claim", "journalist report", "eyewitness estimate"
- When organiser and independent estimates differ significantly, report both
- Never state attendance as fact without source attribution
- Flag inflated estimates: "Organiser claims 5,000; journalist estimates 1,500 [ASSESSMENT: likely inflated]"

### Momentum Assessment Rules
- Momentum is assessed relative to the candidate's own baseline, not absolute
- A "Surging" rating requires at least 2 positive indicators from different categories
- Momentum shifts require evidence from the current cycle, not carry-over from previous
- "Insufficient Data" is a valid assessment — do not infer momentum from absence of reporting

---

## 14. Legal and Ethical Controls

**All campaign trail monitoring must comply with:**
- Malaysian Elections Act 1958 and Election Offences Act 1954
- Communications and Multimedia Act 1998
- Personal Data Protection Act 2010
- Only public, lawful information is collected
- No private surveillance, interception, or covert gathering
- No use of personal data to profile or target individual voters
- All sources must be attributed in reporting
- Unverified claims must be tagged [UNVERIFIED]
- Analytical judgments must be tagged [ASSESSMENT]

---

## 15. Phase Applicability

| Phase | CT PIR Status | Cadence |
|-------|--------------|--------|
| Phase 1 (Pre-Nomination) | Not active | — |
| Phase 2 (Nomination Day) | Standby | — |
| **Phase 3 (Campaign Period)** | **ACTIVE — All 8 PIRs** | **3x daily (09:00/17:00/01:00 MYT)** |
| Phase 4 (Early Voting) | Active — reduced focus | Every 4h |
| Phase 5 (Polling Day) | Suspended (campaigning prohibited) | — |
| Phase 6 (Post-Poll) | Closed | — |

**Campaigning is prohibited on polling day (1 August 2026). CT PIRs suspend at 00:00 MYT 1 August.**

---

**Framework Version:** 1.0 (Campaign Trail Tracker)  
**Total CT PIRs:** 8  
**Parent Framework:** pir-framework.md (NS-01 to NS-18)  
**Next Review:** 25 July 2026 (mid-campaign review)  
**Classification:** TLP:AMBER
