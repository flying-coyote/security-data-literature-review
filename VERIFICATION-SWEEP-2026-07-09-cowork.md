---
type: verification-report
title: "Per-Citation Verification Sweep — 2026-07-09 (Cowork session)"
created: 2026-07-09
tags: [verification, citations, url-sweep, evidence-tier, audit]
---

# Verification Sweep — 2026-07-09 (Cowork)

**What this is**: a just-in-time, per-citation verification sweep run in a Cowork cloud session (no owner memory loaded). Every verdict below rests on a live fetch performed 2026-07-09; nothing was marked VERIFIED without fetching the cited primary. Web content was treated strictly as data. This report makes verification status explicit — it changes nothing; the fix pass is local and should carry a CHANGELOG entry when applied.

**Method**: repo-side claims were inventoried from PUBLICATION-MANUSCRIPT.md, APPENDICES.md, book-appendices/, MASTER-BIBLIOGRAPHY.md, and REFERENCES.md, then each cited URL was fetched (raw fetch preferred; a text-rendering proxy was used only where a page serves a JS shell, always against the exact cited URL) and each specific attributed number/quote was checked against the fetched text. web.archive.org is on this environment's fetch blocklist, so dead-link archive recovery was not possible here — UNREACHABLE means "could not render," never "assumed bad."

---

## 1. Verdict counts (49 URL/claim checks)

| Verdict | Count | Items |
|---|---|---|
| VERIFIED | 31 | see §5 tables |
| CLAIM-MISMATCH | 8 | Cloudflare log-analytics "10-12×"; LinkedIn "terabytes of state"; CH-vs-ES "5-10×"; Iceberg "300+ contributors"; SK Telecom recap figures; CISA "24-36 month"; Cloudera TEI "39/32/29"; MITRE Engenuity "76%" |
| MISATTRIBUTED | 1 | DORA 2024 "Level 4 skill / top 5% of organizations" |
| URL-DEAD | 3 | Snowflake apache-polaris workload page (as annotated); Confluent "2024 State of Data Architecture Report" (no evidence this report exists); Databricks "State of Data Engineering 2024" (title belongs to lakeFS, not Databricks) |
| UNREACHABLE | 6 | Gartner 2025-07-29 PR (JS-gated; existence corroborated); Prosci best-practices article (JS-gated; claim contradicted by Prosci's own published data); ocsfcommunity.slack.com (as annotated); schema.ocsf.io (JS shell; v1.8.0 corroborated via GitHub releases); docs.dremio.com/cloud/acceleration/reflections/ (JS shell); bit.ly/dremio-slack (shortener opaque to fetcher) |

---

## 2. Coverage per file (honest accounting — nothing silently truncated)

1. **PUBLICATION-MANUSCRIPT.md** — contains no inline footnote URLs (References section reads "[TO BE GENERATED]"); all citations are by source name and resolve through MASTER-BIBLIOGRAPHY.md. I enumerated **24 distinct externally-attributed specific claims**; **20 of 24 were checked against fetched primaries** (results in §5.1). 2 were unreachable at the primary (Gartner PR, Prosci). 2 have **no citable source anywhere in the repo**: "Gartner documents 6-12 months for team proficiency" (no Gartner-proficiency entry or URL exists in the bibliography) and "70% of security queries target last 30 days / <5% access historical data" (§3.3.2 — unsourced). First-party claims (CIDR probe ~13-17×, MOAR/FOIL figures) are repo-internal measurements, out of scope for web verification, and are clearly labeled first-party in the text — no issue.
2. **APPENDICES.md** — 0 URLs in file; **14 of ~20 attributed-claim bundles checked** via their bibliography-resolved primaries (§5.2). The unchecked remainder are rubric examples without specific external numbers.
3. **book-appendices/appendix-e-resource-directory.md** (79 URL occurrences) — **all 4 July-2026 flagged items re-verified** (all annotations correct) **+ 14 spot-checks** = 18 of 79 checked. Not checked: the remaining directory-style links (books, YouTube, conference registration pages).
4. **book-appendices/ other files** — appendix-f: 4 of 5 checked (5th is an example.com placeholder); appendix-i: 4 of 7; appendix-j: 4 of 92; appendix-g: 4 of 93 (plus ~6 of its vendor homepages covered incidentally by other fetches); appendix-c: 0 of 1; appendix-d: 0 of 1; appendices a/b/h/k/l/m: not URL-swept (a has 2 pricing URLs self-verified 2026-07-06). **The g/j directories are the largest unswept surface** (~170 mostly vendor-homepage links, low claim density).
5. **MASTER-BIBLIOGRAPHY.md** — **27 of 176 entries verified at entry level**, prioritized by what the manuscript and appendices actually cite. Remaining ~149 entries not fetched this pass.
6. **REFERENCES.md** — 78 numbered entries (9 already withdrawn); ~25 of the 69 active entries share URLs with today's fetches and inherit those verdicts (mirror fixes listed in §4).

---

## 3. Worst findings, ranked

1. **DORA 2024 "Level 4 skill / top 5% of organizations" is fabricated attribution — and still live in the manuscript.** The DORA 2024 report page and full PDF contain **zero** occurrences of any Level-1/3/4 skill taxonomy, "top 5%," or even the word "fault-tolerance" (grep of extracted PDF text: 0 matches; only verifiable figure: "more than 39,000 professionals"). The bibliography's own note (MASTER-BIBLIOGRAPHY.md:575) already forbids this use, yet the claim appears in the manuscript abstract and at least 8 sections (lines 24, 114, 486, 520-526, 592, 644, 712, 716-720) and APPENDICES.md:740 still says "DORA 2024: streaming operations demand specialized 'Level 4' skills." This is the single most damaging survivor of the 2026-06 audit — it anchors H-IMPL-02 in a source that says no such thing.
2. **CISA retention "24-36 months" is wrong everywhere it still appears.** AA23-193A quotes OMB M-21-31: "Microsoft audit logs be retained for **at least twelve months in active storage and an additional eighteen months in cold storage**" — an OMB requirement for FCEB agencies quoted by CISA, not a CISA recommendation, and not 24-36 months. Manuscript lines 578, 654 and APPENDICES.md:55, 772 still carry 24-36. Note: the bibliography's 2026-06-22 correction to "~12 month" is itself incomplete (drops the +18 cold).
3. **Four APPENDICES.md stats survived the 2026-06 audit but fail verification**: Confluent "76% prioritize real-time detection" (the cited "2024 State of Data Architecture Report" does not appear to exist; Confluent's real 2024 report is the Data Streaming Report, and no such 76% stat was found); Databricks "+64% YoY Flink adoption" (Databricks has no "State of Data Engineering 2024" — that title is a lakeFS report, which also contains no 64% figure); Prosci "30/60/80% adoption pattern" (Prosci's own published pattern is 13/39/73/88% *meeting objectives*, not adoption); MITRE Engenuity "76% of enterprises use ATT&CK" (no stat on the evals site; the real adoption figure in this family is **81%**, UC Berkeley CLTC/McAfee 2020 — different number, different source).
4. **SK Telecom precise figures are not in the cited recap** — confirming the note in APPENDICES.md:284 that MASTER-BIBLIOGRAPHY.md:1788-1790 ignores. The recap actually says input data reduced "on the order of hundreds [of GB], down to under ten gigabytes" and "around six gigabytes… planning only took 70 milliseconds." 209 GB, 6.11 GB, 97.2s, 3.39s, 52.7 TB, "~80%" — none present. The manuscript's qualitative "SK Telecom operates Iceberg with Trino in production" IS supported.
5. **ClickHouse vs Elasticsearch "5-10×" matches nothing on the cited page.** The billion-row matchup (dated May 7, 2024 at fetch) states **12-19× less storage** (functionally equivalent config) and 9-12× (`_source` disabled); the 5-12× numbers on the page are *query-speed* multipliers. The bibliography's freshness note ("page updated 2026-03-03… 5x realistic-OTel figure") is also not supported by this page — no OpenTelemetry content; the ~5×/OTel figures belong to a different 2026 ClickHouse post. Repo understates a favorable number, but it's still a claim-mismatch.
6. **Cloudflare "10-12× compression" is not on the cited page** (repo's July packet suspicion confirmed). Real quotable figures: 600 bytes/doc → 60 bytes/row (≈10×, an ES→CH migration figure) and 8× inserter CPU/memory reduction. Manuscript lines 460, 562, 600 and APPENDICES.md:675 still carry 10-12×.
7. **LinkedIn "terabytes of state with millisecond access" was orphaned by the URL re-sourcing.** The now-cited Northguard post verifies 32T records/day, 17 PB/day, 400K topics, 10K+ machines, 150 clusters — but never mentions Kafka Streams state management or the terabytes/ms claim. The manuscript uses the orphaned phrasing 7 times.
8. **Iceberg "300+ contributors across 100+ organizations" is not on the cited page** (iceberg.apache.org/community/ — confirmed against the page's markdown source: no counts at all). Needs GitHub metrics or another primary.
9. **Cloudera/Forrester TEI entry is miscredited and partially unsupported**: the catalogued URL is the *Private Cloud* study (May 2024); the 194% ROI / $35.54M figures verify — but in the *Public Cloud* PDF dated **October 2021**, not 2024; and the "39% licensing / 32% hardware / 29% operational" TCO breakdown appears in **neither** document. Manuscript line 488 rests H-IMPL-01's surviving quantitative support on that breakdown.
10. **Metadata drift on verified entries**: Cloudflare 6M post is 2018-03-06 by Alex Bocharov (entry says "2024-2025, updated Feb 2026"); Azure Kafka post is 2019-02-05 (entry says 2024) and its precise figure is "3 trillion events per day" / "up to 30 million events per second." Same 2025-10-15 bulk-stamp pattern the July packet already identified.

**Corroborations worth recording** (things that checked out): Cloudflare 6M/8M/36-node/−50%-latency all verbatim; Dremio 29% vs 23% verbatim (note it's *planned* adoption; same paragraph: current usage 39% Delta vs 31% Iceberg); Huntress $70K→$5K verbatim (page says "more than 90%" — the repo's "93%" is derived arithmetic, and "16 billion events/day" is confirmed absent; page figure is 200K records/sec); Netflix ClickHouse blog: all eight numeric claims verbatim, and the negative checks confirm the packet's held corrections (no "materialized views," no "Polaris/isolation-first" anywhere in the post); Exabeam 1.2M eps/region and 3.5 PB→200 TiB verbatim (17.5× is derived, not stated); Arrow Flight "as much as 20x faster" vs **PyODBC** (not a JDBC/ODBC benchmark — soften wording); arXiv:1702.06370 exactly matches Berkholz/Keppeler/Schweikardt PODS 2017 (the appendix-e arXiv correction is right).

---

## 4. Proposed fix list (one line each; fix pass is local — none applied here)

1. PUBLICATION-MANUSCRIPT.md:24,114,486,520-526,592,644,712,716-720 → remove/re-source every "DORA 2024 / Level 4 / top 5%" attribution (not in DORA 2024; bibliography note already forbids it).
2. PUBLICATION-MANUSCRIPT.md:460,562,600 → "10-12× compression" → "~10× storage reduction (600→60 bytes/row, ES→ClickHouse migration)".
3. PUBLICATION-MANUSCRIPT.md:462,562,600,834 → "5-10× vs Elasticsearch" → "12-19× (vendor benchmark, functionally equivalent config; 9-12× with _source disabled)" or re-anchor ~5× to the 2026 OTel post.
4. PUBLICATION-MANUSCRIPT.md:578,654 → "CISA recommends 24-36 month retention" → "AA23-193A quotes OMB M-21-31: ≥12 months active + 18 months cold (FCEB requirement)".
5. PUBLICATION-MANUSCRIPT.md:654 → drop "28% CAGR per Gartner" (cited PR is a spending forecast; no data-volume CAGR exists in any repo-cited Gartner source).
6. PUBLICATION-MANUSCRIPT.md:488 → drop/re-source "39% licensing, 32% hardware, 29% operational" (in neither Forrester TEI document) — note this also un-anchors H-IMPL-01's last quantitative support.
7. PUBLICATION-MANUSCRIPT.md:472,560,576,602,658,676,714 → "LinkedIn terabytes of state with ms access" → re-source (original Kafka Streams primary) or reframe on Northguard's verified figures.
8. PUBLICATION-MANUSCRIPT.md:448,590,712 → "300+ contributors across 100+ organizations" → re-source to GitHub contributor metrics or drop the counts.
9. PUBLICATION-MANUSCRIPT.md:26,524,536,644,716 → "Gartner … 6-12 months proficiency" → no source in repo; find a primary or mark expert-estimate.
10. PUBLICATION-MANUSCRIPT.md:500 → "70% of queries target last 30 days / <5% historical" → unsourced; source or mark illustrative.
11. MASTER-BIBLIOGRAPHY.md:281 → Cloudflare 6M date → 2018-03-06, Alex Bocharov.
12. MASTER-BIBLIOGRAPHY.md:318,324 → "10-12× compression" → 10× (600→60 B/row) + 8× inserter CPU; clear the stale "content NOT re-verified" hedge (now verified).
13. MASTER-BIBLIOGRAPHY.md:676 → delete "Terabytes of state with millisecond access times" from Northguard entry key findings (not in post).
14. MASTER-BIBLIOGRAPHY.md:1020 → Azure entry: date → 2019-02-05; add exact "3 trillion events/day"/"up to 30M events/sec" figures.
15. MASTER-BIBLIOGRAPHY.md:1788-1790 → replace SK Telecom figures with recap's actual wording ("hundreds of GB → under ten GB"; "~6 GB, 70 ms planning") or re-source figures to the talk video/slides.
16. MASTER-BIBLIOGRAPHY.md:1812,1819 → "5-10×" → 12-19×/9-12×; fix freshness note (page dated 2024-05-07 at fetch; no OTel content; ~5× belongs to the 2026-04-23 post).
17. MASTER-BIBLIOGRAPHY.md:1693 → remove "300+ contributors across 100+ organizations" or re-source (not on cited page).
18. MASTER-BIBLIOGRAPHY.md:1366-1390 → split TEI entry per July packet; correct Public Cloud study date to Oct 2021; delete "39% licensing, 32% hardware" (in neither doc).
19. MASTER-BIBLIOGRAPHY.md:1134 → "20× faster than JDBC/ODBC" → "as much as 20× faster than PyODBC (per Dremio Subsurface talk cited in the Arrow blog)".
20. APPENDICES.md:43,72,681 → Huntress "93%" → "more than 90% (~$70K→~$5K/month)" (93% is derived, not stated).
21. APPENDICES.md:55,772 → CISA 24-36 → 12+18 per M-21-31 (see fix 4).
22. APPENDICES.md:111,809 → remove Confluent "76% real-time detection" (cited report not found; stat unlocatable).
23. APPENDICES.md:756 → remove Prosci "30/60/80% adoption" (Prosci's own data: 13/39/73/88% meeting objectives).
24. APPENDICES.md:767 → remove Gartner "28% CAGR for security data" (see fix 5).
25. APPENDICES.md:792 → fix MITRE "76% use ATT&CK" → 81% per UC Berkeley CLTC/McAfee 2020, cited to that study, or drop.
26. APPENDICES.md:810 → remove Databricks "+64% YoY Flink adoption" (report not Databricks'; figure not in the lakeFS report either).
27. APPENDICES.md:730 → remove "[3] AWS: 22% average compute savings" (bibliography already removed the 22% as CloudZero-origin; sync).
28. REFERENCES.md → mirror fixes 11-19 onto entries [6],[9],[15],[16],[18],[25],[26],[34],[36],[49],[65],[68] where the same URLs/claims appear.
29. book-appendices/appendix-e-resource-directory.md:427 → Polaris "Apache incubator project (October 2024)" → top-level project since 2026-02-19 (v1.5.0 released 2026-05-18).
30. book-appendices/appendix-e-resource-directory.md:429-431 → add: Snowflake Open Catalog is closed to new sign-ups (docs now steer new customers to Horizon Catalog; billing begins H1 2026) — changes the "use Open Catalog" recommendation.
31. book-appendices/appendix-e-resource-directory.md:206 → soften "several already moved off their old dremio.com/... paths" — docs/University/community all live and unredirected at 2026-07-09; keep the churn warning (SAP close completed July 2026).
32. book-appendices/appendix-g-vendor-landscape.md:44 → chronicle.security serves stale pre-rebrand content; point to the Google SecOps canonical page.
33. CHANGELOG.md → add an entry when the fix pass lands (citation-stability rule).

---

## 5. Detail tables (entry · URL · verdict · evidence)

### 5.1 PUBLICATION-MANUSCRIPT.md claims (resolved via MASTER-BIBLIOGRAPHY.md)

| Claim (manuscript) | Cited primary | Verdict | Evidence / reason |
|---|---|---|---|
| Cloudflare 6M req/sec (peak 8M; 36 nodes ×3 replication; −50% latency) | blog.cloudflare.com/http-analytics-for-6m-requests-per-second-using-clickhouse/ | VERIFIED | "On average we process 6M HTTP requests per second, with peaks of upto 8M"; "36 nodes with x3 replication factor"; "query latency decreased by 50%… index granularity 8192→32". Actual date 2018-03-06, Alex Bocharov |
| Cloudflare "10-12× compression for log data" | blog.cloudflare.com/log-analytics-using-clickhouse/ | CLAIM-MISMATCH | Figure absent. Page (2022-09-02, Monika Singh): "Each Elasticsearch document which used 600 bytes, came down to 60 bytes per row in ClickHouse" (≈10×, ES→CH migration); also 8× inserter CPU/memory |
| DORA 2024: fault-tolerance = "Level 4" skill, "top 5% of organizations" | dora.dev/research/2024/dora-report/ | MISATTRIBUTED | Full report PDF: 0 matches for Level 1/3/4, "top 5%", or "fault-toleran*". Only verifiable figure: "more than 39,000 professionals". Bibliography note (line 575) already prohibits this use |
| LinkedIn: terabytes of state, ms access (Kafka Streams) | linkedin.com/blog/engineering/infrastructure/introducing-northguard-and-xinfra | CLAIM-MISMATCH | Post verifies "over 32T records/day at 17 PB/day on 400K topics… 10K+ machines within 150 clusters" but never discusses Kafka Streams state or terabytes/ms |
| Microsoft/Azure: trillions of events/day (Kafka) | azure.microsoft.com/…/processing-trillions-of-events-per-day-with-apache-kafka-on-azure/ | VERIFIED | "ingest and process 3 trillion events per day"; "up to 30 million events per second". Date 2019-02-05 (entry says 2024) |
| ClickHouse 5-10× storage efficiency vs Elasticsearch | clickhouse.com/blog/clickhouse_vs_elasticsearch_the_billion_row_matchup | CLAIM-MISMATCH | Page states "12 to 19 times less storage space" (equivalent config); 9-12× with `_source` disabled; the page's 5-12× figures are query speed, not storage. No OTel content on page (dated 2024-05-07 at fetch) |
| ClickHouse native IP types (no vendor multiplier cited) | clickhouse.com/docs/sql-reference/data-types/ipv6 | VERIFIED | "Stored in 16 bytes as UInt128 big-endian." Negative check passed: no speed multiplier anywhere on page (entry already corrected — consistent) |
| Dremio 2024 survey: 29% Iceberg vs 23% Delta (planned) | dremio.com/press-releases/state-of-the-data-lakehouse-2024-… | VERIFIED | "29% adopting an open table format in the next three years plan to choose Iceberg, compared to 23% for Delta Lake" (Nov 28, 2023; Propeller Insights, n=500). Caveat: current usage in same paragraph = 39% Delta vs 31% Iceberg |
| Iceberg: 300+ contributors, 100+ organizations | iceberg.apache.org/community/ | CLAIM-MISMATCH | No contributor/organization counts on page (confirmed against page source markdown) |
| SK Telecom operates Iceberg+Trino in production | trino.io/blog/2022/12/19/trino-summit-2022-sk-telecom-recap.html | VERIFIED (qualitative) | Recap "Journey to Iceberg with Trino" supports production use; the *bibliography's* precise figures are absent from it (see 5.3) |
| CISA: 24-36 month retention | cisa.gov alert 2023-07-12 + AA23-193A PDF | CLAIM-MISMATCH | AA23-193A: "OMB M-21-31 requires Microsoft audit logs be retained for at least twelve months in active storage and an additional eighteen months in cold storage." No 24-36 anywhere |
| Gartner: 28% CAGR security data growth | gartner.com PR 2025-07-29 ($213B) | UNREACHABLE (claim unsupported) | PR is JS-gated here; existence + $213B spending corroborated via Gartner's own channels. It is a *spending* forecast — no data-volume CAGR; no repo-cited Gartner source contains 28% |
| Cloudera TCO: 39% licensing / 32% hardware / 29% operational | tei.forrester.com/go/cloudera/onPremises/ + Cloudera Public Cloud TEI PDF | CLAIM-MISMATCH | Breakdown in neither document (grep-negative in both). Public Cloud PDF verifies "an ROI of 194%" and $35.54M benefits — but is dated October 2021, not 2024 |
| Arrow Flight SQL faster than JDBC/ODBC | arrow.apache.org/blog/2022/02/16/introducing-arrow-flight-sql/ | VERIFIED (wording caveat) | "Compared to existing libraries like PyODBC, Arrow Flight is already as much as 20x faster" — vs PyODBC, per an external Dremio talk; manuscript's directional phrasing is fine |
| Gartner: 6-12 months team proficiency | (no URL in repo) | UNSOURCED | No Gartner-proficiency entry exists in MASTER-BIBLIOGRAPHY.md or REFERENCES.md |
| 70% of queries target last 30 days; <5% historical | (no URL in repo) | UNSOURCED | No source found in any repo surface |
| First-party: CIDR probe ~13-17×, ~2.9× storage; MOAR/FOIL figures | repo-internal (lab/cidr_probe.py etc.) | out of scope | Labeled first-party in text; not web-verifiable — correctly framed |

Manuscript coverage: 20 of 24 externally-attributed claims fetched-and-checked; 2 unreachable at primary; 2 unsourced in repo.

### 5.2 APPENDICES.md attributed claims

| Claim | Verdict | Evidence / reason |
|---|---|---|
| Huntress 93% cost reduction; $70K→$5K/mo (lines 43, 72, 681) | VERIFIED (caveat) | Page (2024-11-19): "upwards of $70,000 per month" → "around $5,000 per month"; page says "more than 90%" — 93% is derived. "16 billion events/day" confirmed absent (page: "up to 200,000 records per second") |
| CISA 24-36 month retention (lines 55, 772) | CLAIM-MISMATCH | See 5.1 — actual: ≥12 months active + 18 cold (OMB M-21-31, quoted by AA23-193A) |
| Dremio 29% vs 23% (lines 102, 291, 660) | VERIFIED | See 5.1 |
| Confluent 2024 State of Data Architecture: 76% real-time (lines 111, 809) | URL-DEAD / stat unlocatable | No such report found on confluent.io; Confluent's 2024 flagship is the Data Streaming Report; no matching 76% stat found anywhere |
| Cloudflare 6M req/sec (lines 71, 674) | VERIFIED | See 5.1 |
| Cloudflare 10-12× compression (line 675) | CLAIM-MISMATCH | See 5.1 — actual ~10× (600→60 B/row) |
| ClickHouse vs ES 5-10× (lines 387, 676) | CLAIM-MISMATCH | See 5.1 — page says 12-19× / 9-12× |
| DORA "Level 4" (lines 718, 740) | MISATTRIBUTED | See 5.1 |
| Cloudera/Forrester TEI 39/32/29 (lines 306, 311, 720) | CLAIM-MISMATCH | See 5.1 |
| Prosci 30/60/80% adoption (line 756) | UNREACHABLE (claim contradicted) | Article JS-gated; Prosci's own published correlation data: "excellent… 88% met or exceeded objectives… good… 73%… Only 13%… poor" — pattern is 13/39/73/88 meeting objectives, not 30/60/80 adoption |
| Gartner 28% CAGR (line 767) | unsupported | See 5.1 |
| MITRE Engenuity: 76% use ATT&CK (line 792) | CLAIM-MISMATCH | No statistics on attackevals.mitre-engenuity.org at all; real family stat: 81% (UC Berkeley CLTC/McAfee 2020). Site also rebranded to evals.mitre.org |
| Databricks +64% YoY Flink (line 810) | URL-DEAD / stat unlocatable | databricks.com/resources/report/state-of-data-engineering-2024 unfetchable and no such Databricks report found; lakeFS owns that title, and its report has no 64% Flink figure |
| AWS 22% right-sizing (line 730) | internal inconsistency | Bibliography already removed the 22% as CloudZero-origin (line 1520); APPENDICES not synced |

### 5.3 MASTER-BIBLIOGRAPHY.md entry-level results (27 of 176 entries)

| Entry | URL | Verdict | Note |
|---|---|---|---|
| ClickHouse at Cloudflare — 6M req/sec | blog.cloudflare.com/http-analytics-… | VERIFIED | Date wrong in entry: actual 2018-03-06 |
| ClickHouse Log Analytics — Cloudflare | blog.cloudflare.com/log-analytics-using-clickhouse/ | CLAIM-MISMATCH | "10-12×" not on page; ~10× (600→60 B/row) + 8× inserter CPU |
| 2024-2025 State of DevOps — DORA | dora.dev/research/2024/dora-report/ | VERIFIED (entry) | Entry itself is correct incl. its warning note; the *manuscript* violates it |
| LinkedIn Security — Kafka Streams State Mgmt | linkedin.com/blog/…northguard-and-xinfra | CLAIM-MISMATCH | 32T/day, 17 PB/day, 400K topics, 10K+ machines, 150 clusters verbatim; "terabytes of state, ms access" absent |
| Azure — Kafka at Trillion Events/Day | azure.microsoft.com/…kafka-on-azure/ | VERIFIED | "3 trillion events per day"; date 2019-02-05, not 2024 |
| ClickHouse vs Elasticsearch — Storage Efficiency | clickhouse.com/blog/…billion_row_matchup | CLAIM-MISMATCH | Page: 12-19× / 9-12× storage; entry's 5-10× matches only query-speed figures; freshness note's OTel/2026-03-03 claims not on page |
| ClickHouse — IP Address Types | clickhouse.com/docs/sql-reference/data-types/ipv6 | VERIFIED | No multiplier on page — entry already correctly caveated |
| Huntress — ClickHouse Migration | clickhouse.com/blog/how-huntress-… | VERIFIED (caveat) | "more than 90%", $70K→$5K; 93% derived |
| Netflix ClickHouse Pipeline — 5 PB/Day | clickhouse.com/blog/netflix-petabyte-scale-logging | VERIFIED | All 8 numeric claims verbatim (5 PB/day; 10.6M/12.5M eps; 20s; 8-10×; 31 buckets; 3s→1.3s; ~3s→<700ms). Byline is "ClickHouse"; Muino is the featured engineer |
| Netflix "Security Observability… with Polaris" | (same ClickHouse blog) | MISATTRIBUTED | Confirms July packet: no "Polaris" (beyond catalog option) and no "isolation-first" in post; retitle per packet §2 |
| Apache Iceberg — Industry Consensus (Dremio survey) | dremio.com/press-releases/state-of-the-data-lakehouse-2024-… | VERIFIED | 29%/23% verbatim; planned-adoption framing required |
| Apache Iceberg Foundation — Governance & Contributors | iceberg.apache.org/community/ | CLAIM-MISMATCH | No contributor/org counts on page |
| Apache Iceberg — Official Documentation | iceberg.apache.org | VERIFIED | Live |
| SK Telecom — Iceberg Performance Validation (+ dup entry) | trino.io/blog/2022/12/19/…sk-telecom-recap.html | CLAIM-MISMATCH | Recap: "hundreds [of GB]… down to under ten gigabytes"; "around six gigabytes… 70 milliseconds"; none of 209 GB/6.11 GB/97.2s/3.39s/52.7 TB/~80% present |
| CISA — Enhanced Security Monitoring | cisa.gov alert + AA23-193A | VERIFIED (caveat) | Entry's ~12mo correction is close but incomplete: ≥12mo active + 18mo cold (OMB M-21-31) |
| Gartner — Security Data Growth & Spending | gartner.com PR 2025-07-29 | UNREACHABLE | JS-gated; $213B corroborated; spending only — no volume CAGR |
| Cloudera TEI (Forrester 2024) | tei.forrester.com/go/cloudera/onPremises/ + Public Cloud PDF | CLAIM-MISMATCH | URL = Private Cloud May 2024; 194%/$35.54M verified in Public Cloud PDF dated Oct 2021; 39/32/29 in neither. Split per July packet |
| Apache Arrow Flight SQL | arrow.apache.org/blog/2022/02/16/… | VERIFIED (caveat) | "as much as 20x faster" vs PyODBC |
| Exabeam ClickHouse (July packet candidate) | clickhouse.com/blog/exabeam-clickhouse-security-analytics | VERIFIED (caveat) | 10 regions, 1.2M eps/region, 3.5 PB→200 TiB verbatim; 17.5× is derived |
| Apache Polaris — TLP Graduation | github.com/apache/polaris (+ Snowflake blog 2026-02-19) | VERIFIED | TLP confirmed; v1.5.0 2026-05-18 |
| OCSF Schema v1.8.0 | schema.ocsf.io (via github.com/ocsf/ocsf-schema releases) | VERIFIED (via GitHub) | "[v1.8.0] - Mar 16th, 2026" marked Latest; site itself JS-shell to fetcher |
| DuckLake v1.0 | ducklake.select/2026/04/13/ducklake-10/ | VERIFIED | Title/date match |
| Architecting an Apache Iceberg Lakehouse — Merced | manning.com/books/architecting-an-apache-iceberg-lakehouse | VERIFIED | "April 2026, ISBN 9781633435100, 408 pages" — final edition |
| MOAR Stack reference architecture | securitydataworks.com/thesis/moar | VERIFIED | Live, expected title |
| SDW Lab benchmarks (+ security-context-graph) | github.com/flying-coyote/sdw-lab-benchmarks | VERIFIED | Public; SCG subproject present |
| Streaming vs Batch Cost Differential | [Placeholder URL] | (already flagged) | Phantom entry; July packet's "retire" recommendation stands — nothing to fetch |
| MITRE Engenuity — ATT&CK Evaluations | attackevals.mitre-engenuity.org | CLAIM-MISMATCH | No 76% (or any stat) on site; rebranded to evals.mitre.org |

### 5.4 book-appendices results

| Item | Verdict | Evidence / note |
|---|---|---|
| **appendix-e flagged #1**: arXiv:1702.06370 (corrected ID) | VERIFIED | "Answering Conjunctive Queries under Updates," Berkholz/Keppeler/Schweikardt, PODS '17 — exact match; correction was right |
| **flagged #2**: Snowflake Open Catalog docs | VERIFIED (+new caveat) | Live, managed Apache Polaris; but "Customers who haven't previously created a Snowflake Open Catalog account can't sign up" → new users steered to Horizon Catalog |
| **flagged #3**: old snowflake.com apache-polaris workload URL | URL-DEAD | Empty response while sibling snowflake.com pages render; annotation correct. Replacement: polaris.apache.org |
| **flagged #4**: OCSF Slack path | VERIFIED / UNREACHABLE | ocsf.io live with "send an email to info@ocsf.io" invite path; ocsfcommunity.slack.com unusable for non-members — annotation correct |
| Dremio docs / University / community (SAP close July 2026) | VERIFIED ×3 | All live, unredirected at 2026-07-09; appendix's "several already moved" overstates — keep churn warning (SAP close confirmed via SAP newsroom July 2026) |
| Netflix ClickHouse petabyte logging (appendix-e I.4A refs) | VERIFIED | See 5.3; appendix-e's "no materialized-views claim" annotation confirmed correct |
| Polaris status line (appendix-e:427) | STALE | Says "Apache incubator (October 2024)"; Polaris is TLP since 2026-02-19 |
| iceberg.apache.org; trino.io/slack; d3fend.mitre.org; materialize.com/docs; schema.ocsf.io; github.com/apache/polaris; securitydataworks.com ×2 | VERIFIED (7) + UNREACHABLE (schema.ocsf.io JS shell, claim corroborated) | Spot-checks pass |
| appendix-i: ducklake-10; motherduck ducklake; trino iceberg connector | VERIFIED ×3 | Titles/dates match |
| appendix-i: docs.dremio.com/cloud/acceleration/reflections/ | UNREACHABLE | JS shell; archive blocked here — browser check recommended |
| appendix-j: EvidenceForge; community.dremio.com | VERIFIED ×2 | Live, expected content |
| appendix-j: bit.ly/dremio-slack | UNREACHABLE | Shortener opaque to fetcher; search suggests dremio-dev.slack.com invite — confirm and replace with direct URL |
| appendix-g: query.ai; hydrolix.io; chronicle.security | VERIFIED ×3 | chronicle.security live but serving stale pre-SecOps content — consider Google SecOps canonical |
| appendix-f: ocsf.io; schema.ocsf.io; github.com/ocsf/ocsf-schema; docs.aws.amazon.com/security-lake/ | VERIFIED ×3 + 1 via index.html | Security Lake docs render at /security-lake/index.html (bare path is JS shell) |

---

## 6. Git handoff (sandbox cannot run git against this repo)

This Cowork session's shell sandbox cannot mount the WSL repo path (UNC unsupported), so no branch was created here. **File created by this sweep (the only change): `VERIFICATION-SWEEP-2026-07-09-cowork.md`** — no existing file was edited. To land it as specified, run locally:

```bash
cd ~/security-data-literature-review
git checkout -b litreview-verify-cowork-2026-07-09
git add VERIFICATION-SWEEP-2026-07-09-cowork.md
git commit -m "📋 Verification sweep 2026-07-09 (cowork): 49 checks — 31 verified, 8 claim-mismatch, 1 misattributed, 3 dead, 6 unreachable"
git push -u origin litreview-verify-cowork-2026-07-09
```

Never push to master; no force-push or rebase needed (new branch, single new file).

---

**Sweep run**: 2026-07-09, Cowork cloud session · 49 fetch-backed checks (4 parallel verification passes) · web.archive.org blocked in-environment (noted per item) · No repo file edited; fix list in §4 is proposals only.

