# PRN Negeri Sembilan 2026 — Election Calendar

**Classification:** TLP:AMBER  
**Election:** 16th Negeri Sembilan State Legislative Assembly  
**Total DUN:** 36 (19 for majority)  
**Created:** 2026-07-10  
**Last Updated:** 2026-07-18

---

## Election Phases

| Phase | Period | Description | Intelligence Cadence |
|-------|--------|-------------|---------------------|
| Phase 1 | 5 Jun – 17 Jul | Pre-Nomination | Daily |
| Phase 2 | 18 Jul | Nomination Day | Hourly |
| Phase 3 | 18–31 Jul | Campaign Period | Daily + event-driven |
| Phase 4 | 28 Jul | Early Voting | Every 4 hours |
| Phase 5 | 1 Aug | Polling Day | Hourly |
| Phase 6 | 1 Aug+ | Post-Poll | Daily → Weekly |

---

## Key Dates

| Date | Event | Impact | Intelligence Priority |
|------|-------|--------|----------------------|
| 5 Jun 2026 | State Assembly dissolved | Election called | HIGH — initial baseline |
| 10 Jul 2026 | Intelligence workspace deployed | Operations begin | — |
| 10–17 Jul | Pre-nomination collection | Baseline establishment | Daily briefs |
| **18 Jul 2026** | **Nomination Day** | Candidates confirmed | **HOURLY — all 25 Nomination Day PIRs activated** |
| 18–31 Jul | Campaign period | Active campaigning | Daily briefs + event-driven sitreps |
| 28 Jul 2026 | Early Voting | Security forces, EC officers vote | Every 4 hours |
| **1 Aug 2026** | **Polling Day** | Voting 08:00–18:00 MYT | **HOURLY — all PIRs at maximum cadence** |
| 1 Aug evening | Unofficial results | Result counting | Real-time tracking |
| 2 Aug 2026 | Official results | SPR confirmation | Final assessment |

---

## Parliamentary Constituencies (8)

| Code | Name | DUNs Included |
|------|------|---------------|
| P.126 | Jelebu | N.01 Chennah, N.02 Pertang, N.03 Sungai Lui, N.04 Klawang |
| P.127 | Jempol | N.05 Serting, N.06 Palong, N.07 Jeram Padang, N.08 Bahau |
| P.128 | Seremban | N.09 Lenggeng, N.10 Nilai, N.11 Lobak, N.12 Temiang, N.13 Sikamat, N.14 Ampangan |
| P.129 | Kuala Pilah | N.15 Juasseh, N.16 Seri Menanti, N.17 Senaling, N.18 Pilah, N.19 Johol, N.20 Labu |
| P.130 | Rembau | N.21 Bukit Kepayang, N.22 Rahang, N.23 Mambau, N.24 Seremban Jaya, N.25 Paroi, N.26 Chembong |
| P.131 | Tampin | N.27 Rantau, N.28 Kota, N.29 Chuah |
| P.132 | Port Dickson | N.30 Lukut, N.31 Bagan Pinang, N.32 Linggi, N.33 Sri Tanjung, N.34 Gemas, N.35 Gemenceh, N.36 Repah |

---

## 2023 Baseline Results

| Coalition | Seats | Key DUNs |
|-----------|-------|----------|
| PH (Pakatan Harapan) | 17 | Seremban urban, mixed-race seats |
| BN (Barisan Nasional) | 14 | Rural Malay, Jelebu/Jempol |
| PN (Perikatan Nasional) | 5 | Tampin, rural Malay |

**T1 Critical Seats (2023 margins <5%):** N.03, N.05, N.06, N.09, N.14, N.15, N.28

---

## Cronjob Schedule by Phase (MYT — Asia/Kuala_Lumpur)

| Job | Phase 1 (Daily) | Phase 2 (Surge) | Phase 3 (Campaign) | Phase 4 (Early Vote) | Phase 5 (Polling) |
|-----|-----------------|------------------|---------------------|----------------------|-------------------|
| Collection | 01:00 | Every 60m | **06:00 + 18:00** | Every 4h | Every 60m |
| Entity Extraction | 08:00 | Every 120m | **08:00** | Every 4h | Every 120m |
| Sentiment Analysis | 10:00 | Every 120m | **10:00** | Every 4h | Every 120m |
| Intelligence Brief | 09:00 | Every 60m | **12:00 + 21:00** | Every 4h | Every 60m |
| Campaign Trail Tracker | — | — | **09:00 + 17:00 + 01:00** | Every 4h | Every 60m |
| Git Sync | 10:00 | Every 120m | **00:00** (daily) | Every 4h | Every 120m |

**Phase 3 pipeline:** Collection (06:00) → Entity (08:00) → Sentiment (10:00) → Brief (12:00) → Campaign Trail (17:00) → Evening Collection (18:00) → Evening Brief (21:00) → Campaign Trail (01:00) → Git Sync (00:00). The Campaign Trail Tracker runs 3x daily, filling gaps between general collection and brief cycles with candidate-level ceramah/rally/event tracking across all 36 DUNs.

**Phase transitions require manual schedule update** — update cronjob schedules at each phase boundary.

---

**Workspace:** `/home/p62operator/.openclaw/workspace-ns/`  
**Classification:** TLP:AMBER
