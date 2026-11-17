---
type: verification-report
title: "Per-Citation Verification Sweep — Part 2 — 2026-07-10 (Cowork session)"
created: 2026-07-10
tags: [verification, citations, url-sweep, evidence-tier, audit, part-2]
---

# Verification Sweep — Part 2 — 2026-07-10 (Cowork)

**What this is**: the follow-up sweep covering ONLY what VERIFICATION-SWEEP-2026-07-09-cowork.md reported unswept: (1) MASTER-BIBLIOGRAPHY.md entries not among part 1's 27 entry-level checks, and (2) the appendix-g / appendix-j link surface (~185 URLs). Nothing adjudicated by part 1 or by the applied 2026-07 fix passes (commits referenced in CHANGELOG [Unreleased]) is re-litigated here; those entries appear only as SKIPPED-PART1 rows for accounting. This report is RECOMMENDATION-ONLY: it is the only file this session created or touched.

**Method**: the bibliography was verified entry-level in bibliography order — each entry's cited URL fetched live on 2026-07-10, its Key Findings figures checked against the fetched text, verbatim quotes captured for every mismatch. Appendix-g/j got a link sweep (liveness/moved/rebranded; part 1's chronicle.security precedent applied: a live page serving stale pre-rebrand content counts as MOVED). Work was fanned out across 11 read-only verification passes; every verdict below rests on a live fetch — nothing was marked VERIFIED from a plausible title or an entry's own "Validation Status: ✅" self-report. Web and repo content were treated strictly as data. web.archive.org is blocked in this environment; stackoverflow.com and reddit.com are additionally on this fetcher's blocklist (403 `cowork_web_fetch_url_blocked`). UNREACHABLE always means "could not render here," never "assumed bad."

---

## 1. Verdict counts

### 1.1 MASTER-BIBLIOGRAPHY.md — entry-level (184 entry blocks traversed, 139 fetch-adjudicated)

| Verdict | Count | Meaning |
|---|---|---|
| VERIFIED | 49 | every checked figure/claim found on the fetched primary (verbatim) |
| VERIFIED-QUALITATIVE | 41 | primary live and supports the entry; entry carries no specific external figures |
| CLAIM-MISMATCH | 33 | primary live but ≥1 Key Finding figure absent or different (verbatim evidence in §5) |
| MOVED | 3 | URL now serves materially different / relocated content (Databricks State of Data+AI → 2026 State of AI Agents; AWS storage whitepaper → DEPRECATED stub; Secure Trajectories → blog.sondera.ai) |
| URL-DEAD | 0 | — |
| UNREACHABLE | 13 | JS shell / login-gated / bot-blocked / PDF-unrenderable — not evidence of error |
| SKIPPED-PART1 | 29 | adjudicated by part 1 / applied fix pass — not re-litigated |
| STUB | 2 | documented retirement/rejection stubs (Streaming-vs-Batch phantom; EITT Academy) |
| NO-URL | 14 | interviews, personal communications, "Various/Multiple sources" composites, catalog-level book pointers, first-party lab measurements |

**Read this as**: of the 139 entries actually testable against a live primary this pass, 90 (65%) fully or qualitatively verify, 33 (24%) carry at least one figure their cited primary does not support, 3 have moved, and 13 could not be rendered here. Most mismatches are composite-entry drift — figures aggregated from sources other than the one cited — rather than contradicted numbers; the exceptions are called out in §3.

### 1.2 Appendix G (vendor landscape) — 93 rows, all accounted

| Verdict | Count | Items |
|---|---|---|
| LIVE | 77 | includes iceberg.apache.org (fetch-size error in the g-pass; confirmed LIVE via the appendix-j pass same day) |
| MOVED / REBRANDED | 11 | Microsoft Sentinel (URL), Rapid7 InsightIDR→"Incident Command" (rename+URL), Sysdig Secure→"Sysdig Platform", Velociraptor (root page now a docs stub), Alation→"AIOS", Collibra→"Collibra Platform", DataHub→datahub.com, Microsoft Purview (URL), Matillion (fronted by "Maia"), New Relic One→"New Relic", **Knostic: knostic.com is a parked for-sale domain — vendor is live at knostic.ai** |
| URL-DEAD | 1 | databricks.com/lakebase (empty body; live page exists at databricks.com/product/lakebase) |
| UNREACHABLE | 2 | paloaltonetworks.com/cortex/xsiam, sentinelone.com/platform/singularity-ai-siem (bot-blocked; not evidence of error) |
| SKIPPED-PART1 | 2 | query.ai, hydrolix.io |

### 1.3 Appendix J (resources & community) — 92 URL occurrences, all accounted

| Verdict | Count (occurrences) | Notes |
|---|---|---|
| LIVE | 71 | incl. duplicates reused across J.17/References |
| MOVED | 5 | Kinesis Data Firehose→"Amazon Data Firehose" (aws.amazon.com/firehose); Great Expectations integration page→/docs/help/compatibility_reference; Databricks Delta page→/product/lakehouse-storage ("Lakehouse Storage", Delta+Iceberg); Starburst forum→starburst.io/community/forum; Tabular blog live but frozen at 2023 pre-acquisition posts |
| URL-DEAD | 0 | — |
| UNREACHABLE | 13 | 4 Slack workspace URLs (login walls to non-members), schema.ocsf.io (SPA shell, ×2 occurrences), GitHub /discussions (empty render), Stack Overflow + Reddit (fetcher blocklist), linuxfoundation.org/projects/ocsf (empty render), netflixtechblog.com (Medium bot-block), starburst.io/slack |
| SKIPPED-PART1 | 3 | EvidenceForge, community.dremio.com, bit.ly/dremio-slack |

---

## 2. Coverage (honest accounting — nothing silently truncated)

1. **MASTER-BIBLIOGRAPHY.md**: traversed end-to-end in nine contiguous ranges (lines 61 → EOF). 184 entry blocks were adjudicated: 182 `#### ` blocks plus 2 legacy `###`-headed survey entries embedded in the streaming section (Confluent Data Streaming Report 2025; Databricks State of Data + AI 2024) that carry full entry structure but don't match the dashboard's `#### ` counter. Every block from "Fundamentals of Data Engineering" through "DuckLake — Data Inlining for Streaming" has exactly one row in §5. One mid-sweep rate-limit stall (see §7) split one range across two passes; the seam is at "Obsidian Security" and both sides are complete — combined coverage of that range is 18 of 18.
2. **Count observation (NEEDS-LOCAL-CONFIRMATION)**: this sweep observed 182 `#### ` blocks; CLAUDE.md states 179 (dashboard-computed 2026-07-09). Plausibly real growth since the count was pinned, but recount locally with `scripts/automation_dashboard.py` before citing either number.
3. **Line-number caveat (NEEDS-LOCAL-CONFIRMATION)**: Grep-reported and Read-reported line numbers for the same headings drifted by ~20 lines through the middle of the file (likely a tooling artifact of this environment). Entries were matched by exact title, which is unambiguous; the line numbers in §5 are approximate anchors — re-grep locally before making line-targeted edits.
4. **book-appendices/appendix-g-vendor-landscape.md**: 93 vendor-row URLs — 91 fetched this pass (89 by the g-passes, axiom.co and knostic.ai directly), 2 skipped as part-1-verified. Zero rows unaccounted. One row (iceberg.apache.org) exceeded the fetcher's response-size limit in the g-pass and inherited its LIVE verdict from the j-pass fetch of the same URL.
5. **book-appendices/appendix-j-resources-and-community.md**: 92 URL occurrences — 28 fetched in J.1–J.6, 50 fetched in J.7–References (duplicate URLs fetched once, verdicts reused and marked), 3 skipped as part-1-adjudicated, and 1 first-half 429 leftover (Databricks Delta) resolved in the second pass. Zero occurrences unaccounted.
6. **Out of scope, untouched**: everything part 1 already covered (manuscript claims, APPENDICES.md, REFERENCES.md, appendix-e/f/i, the 27 part-1 bibliography entries), and all other book-appendices files (a/b/c/d/h/k/l/m) — same boundary part 1 drew.

---

## 3. Worst findings, ranked

1. **Linux Foundation OCSF entry: the 2025 schema-velocity content is unsupported by both cited URLs.** The cited LF press release (dated 19 Nov 2024, Jennifer Bly) says "The latest version, 1.3.0, released in August 2024" — the entry's v1.4.0–v1.7.0 release-velocity findings, "80%+ security professionals," the SentinelOne/AWS-Security-Lake adoption claims, and the "15+ additional organizations" list appear on neither the press release nor the ocsf.io Alt URL. What DOES verify verbatim: "over 900 contributors and 200 participating organizations" + the founder list. The velocity claims need re-sourcing to github.com/ocsf/ocsf-schema releases (which part 1 already verified through v1.8.0) or removal.
2. **Apache Iceberg "Universal Vendor Support": the cited Register piece contradicts the Microsoft leg.** Entry says AWS/Google/Snowflake/Microsoft/Databricks all support Iceberg, "confirmed by The Register"; the Register article actually says "Market rivals settle on open table format, while Microsoft and Databricks go their own way" and "Microsoft went with Delta Lake" (Fabric: only "some support"). The Databricks half verifies via the Alt URL ("Announcing full Apache Iceberg™ support in Databricks", 2025-06-12 — as Public Preview, not GA).
3. **Databricks "State of Data + AI 2024" is MOVED — all four figures orphaned.** The cited URL now redirects to the 2026 "State of AI Agents" report (published 2026-01-09); none of the entry's figures (11× model growth, 76% OSS LLMs, 377% RAG, 88% GPU) appear there. Re-source to an archived/canonical 2024 copy or retire.
4. **Arctic Wolf: entry understates the page's own number and carries unsupported figures.** Cited PR says "330 trillion raw observations down to 8.6 million alerts — a noise reduction rate of more than 99.99999%" (seven nines); entry says 99.999%. Absent from both cited URLs: the "Aug–Oct 2025: 116T → 20T" figures, OCSF support, multi-tenant portal, and the Sevco Security acquisition claim (the Alt URL names UpSight, not Sevco).
5. **Databricks TCO entry (lakehouse-vs-traditional): none of its headline figures are on the cited primary.** Page offers only "market-leading TCO… holds at scale" and a GetYourGuide "about 20%" example. The 30-50% TCO reduction, "up to 9× lower ETL costs," 15-40%-in-3-6-months, 57%-vs-27% YoY, and the AMN Healthcare 93% counterpoint are all absent — they likely trace to the Alt URL, but the entry doesn't attribute them there.
6. **Confluent Kafka benchmark entry: dated "2023-2026 continuously updated," but the cited page is a single Aug 21, 2020 post** (Nikhil & Chandar). Core benchmark verifies verbatim ("writing 15x faster than RabbitMQ and 2x faster than Pulsar", 605 MB/s); the Kora 12×, "10 MBps → 1.4 GBps ingress," Kafkorama 1M msg/s, and 2-3 ms latency-delta figures are not on the page.
7. **Knostic (appendix-g) points at a parked domain.** knostic.com now serves a "for sale" page on BrandBucket; the vendor is live at **knostic.ai** ("AI Security Platform | Knostic" — verified this pass). Most material link break in either appendix.
8. **Two attribution/date errors in the AI-security cluster**: the Anthropic intrusion-report entry says "November 2024" — the report page says **Nov 13, 2025**; the Josh Devon "Hijacked a Claude Skill" entry cites securetrajectories.substack.com, which now redirects to **blog.sondera.ai**, the cited article isn't in the visible archive, and the entry's "October 2024" date is implausible (predates Claude Skills; publication launched ~mid-2025).
9. **Academic-entry metadata is the weakest surface**: Hyperscan's author list is garbled ("Hong Cheng, Chang Yang, Park Jinseon, Hu Jianbo" — actual: Xiang Wang, Yang Hong, Harry Chang, KyoungSoo Park, Geoff Langdale, Jiayu Hu, Heqing Zhu, NSDI '19); Matryoshka's real title is "Semantic-Aware Parsing for Security Logs" (7 authors, UC Berkeley + Google, not sole-authored); DBSP's Date is "TBD" (it's VLDB, August 2023); LHBench's "7×–20×" should be the paper's verbatim "7–12× for a 200K file table"; F3 needs a two-way fix (drop "~0.001% overhead" — not in the paper; but the ~150 KB figure the entry dismisses as Medium-only IS in the paper verbatim: "approximately 150 KB—negligible compared to the achieved size reduction").
10. **Iceberg 1.11.0 entry doesn't match its cited Google post.** The post (dated **May 27, 2026**, Stephen & Uyarer) covers Spark 4.1/Flink 2.1 support, server-side scan planning, table encryption, File Format API, SQL UDFs — it contains no "all V3 features stabilized / require format-version-3" framing and no deletion-vectors/Variant-stabilization content.
11. **MITRE D3FEND-for-OT entry: the "267 defensive techniques / v1.3.0 / OWL 2 DL" figures are not at the cited news release** (entry's own status already hints they came from secondary coverage). Bonus resolution: the live d3fend.mitre.org version badge now reads **1.4.0**, answering the entry's open v1.3-vs-v1.4 question; and the funder is the "Office of the Under Secretary of **War** for Acquisition and Sustainment" (post-rename), not "OUSD (Defense)".
12. **Bulk-stamp date drift continues** (same pattern part 1 and the 2026-07-09 freshness sweep flagged, in entries neither touched): Anyscale Ray Serve GA is 2023-09-25 (entry: 2024); DNB/marimo post is 2025-10-14 (entry: 2026); phData is 2021-11-12 (entry: 2024); Dremio lakehouse guide is Mazumdar 2023-09-06 (entry: Merced, 2024); Champion-Challenger is 2020-06-19 (entry: 2022-2024); Google SRE book content is ©2017 (entry: 2024); Miessler's post is retitled and dated 2024-07-29 (entry: 2025); DML model is April 21, 2014 (entry: May 2014); Tenzir MCP post is 2025-08-21 by Jannis Köhl (entry: Nov-Dec 2025, Vallentin); SACR market guide is 2025-04-21 (entry: Feb 2025); Uber Palette is 2024-01-18. One cross-source conflict to resolve at re-source time: the AWS OCSF-ITU blog dates OCSF v1.8.0 to March 16, 2026 — the bibliography's v1.8.0 entry says March 18.

**Corroborations worth recording** (fetch-confirmed this pass): the entire 2026 production-anchor cluster verifies verbatim — Ursa PVLDB figures ("92% cost reduction relative to Kafka (Disk)", 5 GB/s, ≈5% spend), FastLanes (43×/44×/7×/29×, random access 315×; the PDF now text-extracts, clearing the entry's extraction-blocked note), DuckLake data-inlining (105×/923×/189× and 5.2×/925.9×/14.5× tables exactly as decomposed — the entry's decomposition is more accurate than the blog's own TL;DR pairing), Variant (8×/30×, 20-50% slower writes, Parquet 2.12.0), S3 Tables ("first cloud object store with built-in Apache Iceberg support… 3x faster query throughput… 10x higher transactions per second"), OCSF-ITU ("ratification as an ITU x.*** international standard by June 2026"), Cohasset/S3 Object Lock (SEC 17a-4(f)(2)/18a-6(e)(2), FINRA 4511(c), CFTC 1.31(c)-(d)), Databricks cross-engine ABAC, KPMG Q3 pulse (42%/11%/57%/130 leaders), Cribl Finality (47% Windows-event reduction), Fortinet/NVIDIA BlueField-3 isolation, Google Cloud agent ROI (74%/52%/39%), PagerDuty (62%/171%/192%), Rippling ($4.50/1.8 credits; $31-34 sum verified from page components), Monad ($11,721; 50.7%; $25/GB vs $0.023/GB), GitLab sub-second analytics, ClickHouse-vs-Snowflake (3-5×, 2×), Iceberg v3 spec feature list, Iceberg v4 milestone (2 open proposals), Kester et al. — which also **closes a flagged item**: the previously 403-blocked Harvard PDF now fetches and gives the scoped crossover verbatim ("the index is preferable when selectivity drops below 0.5−1%", rising to ~8% for 10-column groups, falling with concurrency).

---

## 4. Proposed fix list (recommendation-only; nothing applied)

### Bibliography — claim/attribution fixes (verbatim evidence in §5)

1. LF-OCSF entry → re-source v1.4.0–v1.7.0 velocity, "80%+", and vendor-adoption list to github.com/ocsf/ocsf-schema releases or drop; keep the verified "900 contributors / 200 organizations".
2. Iceberg Universal Vendor Support → remove Microsoft from the "all support" list (cited Register piece: "Microsoft went with Delta Lake"); mark Databricks support Public-Preview-as-of-2025-06.
3. Databricks State of Data + AI 2024 (legacy `###` entry) → URL serves the 2026 State of AI Agents; re-source the 2024 figures or retire the entry.
4. Arctic Wolf → 99.999% → "more than 99.99999%" (page verbatim); re-source or drop 116T→20T, OCSF, portal, and Sevco claims (Alt URL names UpSight).
5. Databricks TCO → attribute 30-50%/9×/15-40%/57-vs-27/AMN figures to their actual source (Alt URL) or drop; cited page carries none of them.
6. Confluent Kafka benchmark → re-date 2020-08-21; keep 15×/2×/605 MB/s; re-source or drop Kora 12×, 1.4 GBps, Kafkorama, 2-3 ms.
7. Uber Real-Time Analytics → keep the verified qps/writes/PB figures; re-source "trillions of messages / dozens of PB daily" + Data Streaming Award (entry sources them to InfoQ — make that the citation); page says AthenaX, not "FlinkSQL"; the page no longer 403s (drop stale note).
8. LHBench → "~7×–20×" → paper's "7–12× for a 200K file table"; add Stanford to the author affiliations.
9. Confluent Architecture & Sizing → drop the "infrastructure cost benchmarks" key finding (cited course has no cost content).
10. AWS S3 Intelligent-Tiering → "~35% average savings" not on page; restate as page's "up to 40%" (IA) / "up to 68%" (Archive Instant Access) or re-source.
11. DARPA XAI → "~11 teams / 2017-2021 / Gunning" not on the cited program page; re-source or trim (toolkit claim verifies).
12. MITRE Insider Threat → 47/29 technique counts belong to the Insider Threat Knowledge Base, not the cited page; repoint or trim.
13. Apache Arrow powered_by → Snowflake and Streamlit are no longer on the list; refresh names or drop them.
14. Confluent ML-with-Kafka → "Current 2023: generative AI…" finding absent (cited page is a 2018 Waehner post); trim or re-source.
15. Amazon Security Lake → move the "direct query from Athena/Redshift/Spark/EMR" bullet to the features Alt URL it actually lives on (other three findings verify verbatim).
16. NANDA (media-lab entry) → "1,000+ agents via Join39", MLflow/Databricks validation, and Google A2A absent from both cited pages; re-source or drop; note site content is stale (still advertising the April 2025 summit).
17. Tenzir MCP → drop "Production deployment validated (December 2025)" (page is the v0.1 announcement); re-date 2025-08-21, author Jannis Köhl.
18. SACR Market Guide → "50-70% log volume reduction" → page's "80% or more" (general) or "25–70%" (Axoflow-specific); re-date 2025-04-21.
19. Data Catalog Wars → Nessie "versioning only" is mis-attributed to the onehouse.ai comparison (Nessie isn't in its evaluated scope); re-source the Nessie characterization.
20. CSA press-release entry → "≈25% have comprehensive governance" mis-scopes the page's 25% (which is agentic-adoption among partial-guideline orgs); restate as the 46%/25%/12% adoption-by-maturity split, or cite the 26% from the gated report with an explicit gated-source caveat; note n=300.
21. Hunters → drop the "skills shortage" bullet (absent from page; bank/HSBC headline figures verify verbatim).
22. Gravitino → drop/re-source Ranger-integration and geo-distributed bullets; re-attribute the article (Medium account "Office", 2025-08-26, summarizing Jerry Shao's talk).
23. Polaris ecosystem → re-source "time travel, commit retries, STS credential vending" and the 1.0.0/1.1.0 release dates to the actual release notes (neither is on the cited Dremio pages); note Dremio pages now carry the "part of SAP" banner.
24. Obsidian Security → the cited page was rewritten (updated 2026-06-30) and no longer carries the MTTD/MTTR/FP-rate/SIEM-SOAR content; re-verify against current text or trim.
25. DuckDB 1.0-1.4 LTS → split the composite: v1.4 facts verify on the cited page (LTS 1-year support, Iceberg writes, 5-10× compression-speed, 3,500 commits/90 contributors), but v1.0 "Snow Duck" (page's table: codename "Nivis"), download counts, and Facebook/Google/Airbnb usage are not on it.
26. SCF → refresh stale counts: site now says "1,500+ controls across 200+ laws, regulations, and industry frameworks" (v2026.2).
27. Hyperscan → fix garbled author list (Wang, Hong, Chang, Park, Langdale, Hu, Zhu — NSDI '19); full title appends "for Modern CPUs".
28. DBSP → Date TBD → VLDB, August 2023; actual title "DBSP: Automatic Incremental View Maintenance for Rich Query Languages".
29. Matryoshka → title "Semantic-Aware Parsing for Security Logs"; seven authors (Piet, Fang, Khare, Coull, Paxson, Popa, Wagner — UC Berkeley and Google).
30. F3 → drop "~0.001% overhead" (not in paper); reinstate ~150 KB as paper-primary (verbatim: "approximately 150 KB—negligible compared to the achieved size reduction").
31. Streambased Kafka-to-Iceberg → point URL at the article (…/p/the-9-ways-to-move-data-kafka-iceberg), not the blog root; real title "The 9 Ways to Move Data Kafka -> Iceberg"; fix the solution list (no Apache Fluss; includes Kafka Connect and WarpStream TableFlow).
32. Anthropic intrusion report → date is Nov 13, 2025 (entry says November 2024).
33. Josh Devon / Secure Trajectories → publication moved to blog.sondera.ai; locate the exact article URL and correct the implausible Oct-2024 date (Claude Skills postdate it; publication launched ~mid-2025).
34. Splunk 10.4 + Cisco Data Fabric → "Federated Search for Snowflake GA July 2026" absent from the cited post (Snowflake unmentioned); re-source or drop.
35. Iceberg 1.11.0 → replace the V3-stabilization framing with what the cited Google post says (Spark 4.1/Flink 2.1, server-side scan planning, encryption, File Format API, SQL UDFs); post date 2026-05-27, Stephen & Uyarer.
36. MITRE D3FEND for OT → keep 267/v1.3.0 only with their real (secondary) sources labeled, or drop; update: live site badge shows v1.4.0; funder title now "Under Secretary of War for Acquisition and Sustainment".
37. pySigma-pipeline-ocsf → logsource-category count on the live README is now 25 (entry asserts 23, from the 2026-06-13 check); restate with an as-of date.
38. AWS Storage Optimization whitepaper → the PDF now serves an official "DEPRECATED" stub; repoint to the current whitepapers index and give the 40/68/95% tier figures a real Alt URL (S3 Intelligent-Tiering product page) — cross-links with fix 10.
39. SANS blog double-entry → the same URL is catalogued twice at different tiers (A at "SANS AI Security Controls Framework", B at "SANS - Securing AI in 2025"); reconcile tier and merge or cross-reference.
40. Kester et al. → close the entry's FLAGGED item with the now-fetchable PDF's scoped figure: "index preferable when selectivity drops below 0.5−1%" (single-query, column-at-a-time; ~8% for 10-column groups; falls toward 0.4% with concurrency).
41. Metadata-drift batch (dates/authors/titles; each verified at the primary this pass): Anyscale GA 2023-09-25; DNB 2025-10-14; phData 2021-11-12 (Hauschild); Dremio lakehouse guide Mazumdar 2023-09-06 (and the entry's "Alex Merced, contributor" credit is wrong for this URL); Champion-Challenger 2020-06-19; SRE book ©2017; Miessler 2024-07-29 + retitle; DML 2014-04-21; Uber Palette 2024-01-18; SANS 2024 AI Survey byline Edmondson & Bromiley (Crowley authors the 2025 SOC Survey); Ursa first author is Merli (not "Guo et al.") and the 92%/78% live in Figure 10, not Table 1; NANDA-index arXiv title carries the subtitle "An Enterprise Perspective" and spells "AgentFacts"; CCO says exactly eleven ontologies (entry: "eleven+"), latest v2.1 Apr 2026; Fundamentals of Data Engineering O'Reilly page displays "June 2022" (print date July); Trino Definitive Guide page ISBN is the digital variant; Cloudera Impala+Iceberg page announces a technical preview — the entry's "Production CDP validation" overstates (10× customer quote verifies); Netflix Kafka Tiered Storage: cited Confluent doc itself notes it describes Confluent Platform tiered storage, "a different feature than" KIP-405 (entry Notes already consistent — keep); GitLab and CH-vs-Snowflake entries carry stale internal "pre-2025"/"2024" validation-note remnants contradicting their own corrected dates.

### Appendix G — link/rebrand fixes

42. Knostic row → replace knostic.com (parked/for-sale) with https://www.knostic.ai (verified live).
43. Databricks Lakebase row → URL to https://www.databricks.com/product/lakebase (cited shorthand URL serves an empty body).
44. Rapid7 row → product renamed "Incident Command" (URL redirects to /products/siem); update name + URL, keep InsightIDR as former name.
45. Microsoft Sentinel row → URL moved off the Azure catalog to microsoft.com/en-us/security/business/siem-and-xdr/microsoft-sentinel.
46. Sysdig row → /products/secure redirects to /products/platform, page titled "Sysdig Platform"; update.
47. Velociraptor row → velocidex.com root is now a stub ("Docs moved here"); point to velocidex.com/docs/.
48. New Relic One row → current branding is "New Relic" ("Intelligent Observability"); drop the "One".
49. Rebrand annotations (page live, name drifted): Alation → "Alation Intelligence Operating System (AIOS)"; Collibra → "Collibra Platform"; DataHub → datahub.com (DataHub Cloud, Acryl); Microsoft Purview URL → microsoft.com security path; Matillion → homepage fronts "Maia", Data Productivity Cloud demoted; MinIO → flagship now marketed as "AIStor" (Community Edition remains MinIO).
50. Ownership notes worth a row annotation (NEEDS-LOCAL-CONFIRMATION for anything beyond what the pages state): Panther homepage indicates acquisition by Databricks; Fivetran homepage notes the dbt Labs merger; Dremio pages carry "Dremio is now part of SAP" (consistent with part 1's SAP-close note).
51. Cortex XSIAM + SentinelOne rows → bot-blocked to this fetcher only; recommend a browser spot-check locally, no edit implied.

### Appendix J — link fixes

52. AWS Kinesis Data Firehose → renamed "Amazon Data Firehose"; canonical aws.amazon.com/firehose; update name + link.
53. Great Expectations "Validating Iceberg tables" link → redirects to /docs/help/compatibility_reference; update.
54. Databricks Delta link → /product/lakehouse-storage ("Lakehouse Storage", now covers Delta+Iceberg); update and consider rewording the row.
55. Starburst Community forum → www.starburst.io/community/forum; update.
56. Tabular blog → annotate: frozen at 2023 pre-acquisition posts; current content at databricks.com/blog (row for the latter already exists and is LIVE).
57. DetectionLab → annotate: repo unmaintained since 2023-01-01 (still live).
58. Slack workspace URLs (apache-iceberg / apache-airflow / mitreattack / ocsf .slack.com) → login walls for non-members; consider replacing with each project's public invite/community page (the Iceberg and Airflow community pages verified LIVE this pass and carry the invite links).
59. SageMaker docs → retitled "Amazon SageMaker AI Documentation" (same URL, optional name refresh).

### Process

60. CHANGELOG.md → add an entry when any of this lands (citation-stability rule); this report itself is a new root-level file and should be committed on its own branch (see §8).

---

## 5. Detail tables — MASTER-BIBLIOGRAPHY.md (entry · verdict · evidence)

Line numbers are approximate anchors (see §2.3); entries were matched by exact title. Verdict key: V = VERIFIED, VQ = VERIFIED-QUALITATIVE, CM = CLAIM-MISMATCH, MV = MOVED, UD = URL-DEAD, UR = UNREACHABLE, SKIP = SKIPPED-PART1.

### 5.1 Lines ~61–552 (20 entries)

| Entry (~line) | Verdict | Evidence / reason |
|---|---|---|
| Fundamentals of Data Engineering (61) | V | O'Reilly: "by Joe Reis, Matt Housley — June 2022"; lifecycle ToC (Generation/Storage/Ingestion/Transformation/Serving). Drift: entry "July 2022" vs page "June 2022" (print 2022-07-26 explains it) |
| Data Engineering for Cybersecurity (85) | NO-URL | Bare nostarch.com catalog pointer; entry itself says exact URL/ISBN still to confirm |
| Apache Iceberg Performance Tuning - SK Telecom (101) | SKIP | Fix-pass re-verified against slides PDF 2026-07-09 |
| Starburst - Official Documentation (129) | VQ | Live: "Starburst products are built on Trino, the fastest open source, massively parallel processing SQL query engine" |
| Starburst - AWS Athena Comparison (153) | VQ | Live comparison page, capability tables present; entry qualitative |
| Trino: The Definitive Guide (179) | V | "2nd Edition — Fuller, Moser, Traverso — October 2022". Page ISBN is the digital variant (benign) |
| Dremio - Official Documentation (205) | UR | Docusaurus JS shell — only meta tags render; site is live but unreadable to this fetcher |
| Dremio - Data Lakehouse Architecture Guide (229) | VQ | Benign redirect to /resources/guides/; "separate storage and computing…scale independently". Drift: byline Dipankar Mazumdar, 2023-09-06 — entry credits Merced, 2024 |
| Alex Merced - Dremio YouTube Channel (253) | VQ | Channel live; About page shows a personal code/data channel, no Dremio affiliation — label overstates |
| ClickHouse at Cloudflare - 6M (277) | SKIP | Part 1 |
| ClickHouse Log Analytics - Cloudflare (305) | SKIP | Part 1 |
| Kafka Performance Benchmark - Confluent (330) | CM | Verbatim: "writing 15x faster than RabbitMQ and 2x faster than Pulsar" (605 MB/s). Absent: Kora 12×, "10 MBps→1.4 GBps ingress", Kafkorama 1M msg/s, 2-3 ms latency delta. Page is 2020-08-21 (Nikhil & Chandar), not "2023-2026 continuously updated" |
| Questioning the Lambda Architecture (357) | VQ | Kreps, 2014-07-02: "Maybe we could call this the Kappa Architecture…" |
| Uber - Real-Time Analytics Platform (380) | CM | Verbatim: "serve up to 10s of thousands of queries/sec, several million writes/sec and host up to tens of Petabytes of Pinot datasets". Absent: "trillions of messages / dozens of PB daily", IngestionNext ~25%, award; page says AthenaX, not FlinkSQL. Page no longer 403s |
| Disney+ Hotstar - Kafka/Flink (406) | V | "~15 different Kafka Connect clusters with over 2000+ connectors and auto-scaling"; "millions of messages per second" |
| McAfee Streaming Evolution (429) | VQ | Live, 2025-01-27; no figures in entry |
| Top Trends for Data Streaming 2025 (450) | VQ | Live, 2024-12-02; "Flink Becomes the Standard for Stream Processing" |
| AWS Storage Optimization Whitepaper (477) | MV | PDF now serves only "DEPRECATED: AWS Storage Optimization — refer to the AWS Whitepapers & Guides page". The 40/68/95% tier figures have no fetchable Alt URL in the entry |
| McComb - Data-Centric Revolution duology (504) | VQ | technicspub.com confirms both titles + author |
| Prosci Best Practices (527) | SKIP | Part 1 (UNREACHABLE/JS-gated; correction applied) |

### 5.2 Lines ~553–1221 (27 rows: 25 `####` + 2 legacy `###` survey entries)

| Entry (~line) | Verdict | Evidence / reason |
|---|---|---|
| 2024-2025 State of DevOps - DORA (553) | SKIP | Part 1 |
| Confluent Data Streaming Report 2025 (legacy `###`, ~584) | CM | Verbatim: "44% of IT leaders reporting 5x returns—the vast majority (90%) are increasing their DSP investments"; 89% present. Absent from accessible page (report gated): 86%, 93% shift-left, 25% Level-1. Page meta already advertises the 2026 edition (4,625 leaders) while body serves 2025 (4,175) |
| Databricks State of Data + AI 2024 (legacy `###`, ~612) | MV | Redirects to databricks.com/resources/ebook/state-of-ai-agents — the 2026 "State of AI Agents" (2026-01-09). None of 11×/76%/377%/88% present |
| LinkedIn - Northguard (665) | SKIP | Part 1 |
| AWS S3 Storage-Class Pricing derivation (~688) | UR | aws.amazon.com/s3/pricing tables are JS-rendered; static HTML has footnotes but no $/GB-month values — $0.023/$0.0125/$0.004/$0.0036/$0.00099 uncheckable here |
| Samza VLDB 2017 (~709) | SKIP | Added + PDF-verified by the 2026-07-09 fix pass |
| Netflix - Kafka Tiered Storage (~732) | VQ | Confluent doc live; the doc itself notes it covers Confluent Platform tiered storage, "a different feature than" KIP-405; Netflix figures are entry-attributed elsewhere (consistent with entry Notes) |
| ClickHouse - Vectorized Query Execution (~761) | V | "apply SIMD instructions to process multiple values at once… automatically select the most recent and fastest version"; no multipliers on page (matches entry caveat) |
| ClickHouse - IP Address Types (~785) | SKIP | Part 1 |
| Splunk DB Connect Benchmark (~806) | NO-URL | NDA-gated private repo (404 expected per entry); first-party benchmark |
| Kester et al., SIGMOD 2017 (~843) | V | Abstract verbatim: "access path selection (APS) is still required". PDF now fetches (previously 403): "the index is preferable when selectivity drops below 0.5−1%" — closes the entry's FLAGGED ~1% item with a scoped figure |
| LHBench, CIDR 2023 (~860) | CM | Verbatim: "1.4× faster on Delta Lake than on Hudi and 1.7×… than on Iceberg"; paper says "improves performance by 7–12× for a 200K file table" — entry's "7×–20×" wrong. Stanford missing from author affiliations |
| LST-Bench, SIGMOD 2024 (877) | V | Scope + all 9 authors + Proc. ACM Manag. Data 2(1) 2024 confirmed in repo CITATION.bib |
| ClickBench (893) | V | "weighted geometric mean… load 10%, size 10%, cold 20%, hot 60%"; cold-vs-lukewarm discipline confirmed |
| ClickHouse - Compression Codecs (909) | V | Redirects to current docs; LZ4/LZ4HC/ZSTD/Delta/DoubleDelta/Gorilla/T64 all present; no ratio benchmarks (matches entry's "do not cite 3-14× from this source") |
| ClickHouse - Performance Optimization Guide (933) | VQ | Live at the 2026-06-05 re-pointed URL; PK-pruning claim supported |
| Exabeam (956) | SKIP | Part 1 |
| Huntress - ClickHouse Migration (981) | SKIP | Part 1 |
| Chris Bisnett - Huntress Video (1013) | UR | YouTube JS-gated, empty body; 93%/3M-endpoint content unverifiable here |
| RunReveal - SIEM on ClickHouse + sigmalite (1037) | V | "collect raw logs from SaaS and Cloud Services, ingest them into ClickHouse Cloud"; sigmalite repo: "a parser and an execution engine for the Sigma detection format" (Apache-2.0, Go) |
| DNB - Cyber Defense Center on Ibis (1060) | V | "adopt Ibis as the query layer… across DuckDB, Spark, and Snowflake"; Delta→Iceberg, Neo4j confirmed. Drift: post dated 2025-10-14, entry says 2026 |
| Azure - Kafka Trillion Events (1085) | SKIP | Part 1 |
| DuckDB Labs - Overview (1110) | VQ | "completely embedded within a host process"; OLAP positioning |
| Okta - Jake Thomas (1133) | NO-URL | Personal communication (expert validation) by design |
| Apache XTable (1161) | VQ | "NOT a new or separate format… translation of lakehouse table format metadata"; OneTable rename on page. Note: Paimon listed as future format; CatalogSync/RunSync claims live in docs, unchecked |
| Apache Arrow Flight SQL (1189) | SKIP | Part 1 |
| Anyscale Ray Serve (1216) | V | "grown over 600%"; "availability upwards of 99.9%… at least 5000 Ray Serve replicas". Drift: GA blog is 2023-09-25, entry says 2024 |

### 5.3 Lines ~1222–1845 (26 rows)

| Entry (~line) | Verdict | Evidence / reason |
|---|---|---|
| Cloudera Impala + Iceberg (1243) | V | "Iceberg tables perform 10x times better than the previously used Hive external tables using Impala queries" (2022-02-22). Nuance: page announces a technical preview — entry's "Production CDP validation" overstates a customer anecdote |
| Apache Flink Checkpointing (1266) | VQ | Docs live; interval config + EmbeddedRocksDBStateBackend; no security-specific prescriptions (as corrected entry states) |
| Microsoft Purview Retention (1290) | VQ | Live; no external figures. Page ms.date 2026-06-03 vs entry "2024" |
| Confluent Implementation Roadmap (1314) | VQ | Kafka 101 course live (16 modules); no timeline figures (matches corrected entry) |
| phData - Data Platform Implementation (1338) | VQ | "Build iteratively, delivering value to the business early"; published 2021-11-12 (Hauschild), entry says 2024 |
| Brooks - Mythical Man-Month (1362) | V | Pearson: Anniversary Ed., 2nd, Brooks, 1995-08-02; ch. 11 "Plan to Throw One Away" |
| Netflix - Resilient Data Platform with WAL (1385) | UR | netflixtechblog.com (Medium) empty body ×2 — bot-block |
| Netflix Petabyte-Scale Logging (1409) | SKIP | Part 1 |
| Cloudera TEI Public Cloud (1436) | SKIP | Part 1 / fix pass |
| Cloudera TEI Private Cloud (1455) | SKIP | Part 1 / fix pass |
| Confluent - Kafka Architecture & Sizing (1478) | CM | Page is an internals course ("storage layer and a compute layer"); Key Finding "Infrastructure cost benchmarks for capacity planning" — no cost/TCO content anywhere on cited page |
| Databricks TCO (1502) | CM | Page: "We continue to provide market-leading TCO, which holds at scale"; "ETL is typically half or more of total data spend"; GetYourGuide "about 20%". Absent: 30-50% TCO, 9× ETL, 15-40% in 3-6 months, 57%-vs-27%, AMN 93% |
| Gartner - Security Data Growth (1533) | SKIP | Part 1 |
| Retired stub — Streaming vs Batch (1566) | STUB | Documented retirement stub |
| AWS Well-Architected Compute (1573) | VQ | "A cost-optimized workload fully utilizes all resources…" — no savings figure attributed (post-correction) |
| AWS S3 Intelligent-Tiering (1597) | CM | Page: "The Infrequent Access tier saves up to 40%…"; "Archive Instant Access tier saves up to 68%". Entry's "~35% average savings for non-optimized buckets" absent |
| Google SRE - Embracing Risk (1621) | V | "an incremental improvement in reliability may cost 100x more than the previous increment". Book ©2017, entry says 2024 |
| Gartner - Reliability Overinvestment (1645) | NO-URL | Bracketed paywalled-doc placeholder; nothing fetchable |
| Uptime Institute Tiers (1669) | VQ | Tier I–IV page live; supports match-investment-to-need |
| Iceberg - Industry Consensus (1693) | SKIP | Part 1 |
| Iceberg - Universal Vendor Support (1721) | CM | Cited Register piece: "Market rivals settle on open table format, while Microsoft and Databricks go their own way"; "Microsoft went with Delta Lake". Databricks leg verified via Alt URL ("Announcing full Apache Iceberg™ support in Databricks", 2025-06-12 — Public Preview) |
| Iceberg Foundation - Governance (1747) | SKIP | Part 1 |
| Iceberg - Official Documentation (1770) | SKIP | Part 1 |
| Iceberg - Maintenance Docs (1794) | VQ | Expire Snapshots / Delete orphan files / Compact data files all present |
| Iceberg - Spark Procedures (1818) | VQ | rollback_to_snapshot, cherrypick_snapshot, expire_snapshots present |
| SK Telecom - Iceberg Validation (1842) | SKIP | Part 1 |

### 5.4 Lines ~1846–2499 (26 rows)

| Entry (~line) | Verdict | Evidence / reason |
|---|---|---|
| ClickHouse vs Elasticsearch (1867) | SKIP | Part 1 |
| Uber - Palette Feature Store (1890) | V | "Palette Onboarding Deployment time has reduced drastically by more than 95%". Page 2024-01-18 |
| DARPA XAI (1914) | CM | Toolkit claim verifies ("toolkit library consisting of machine learning and human-computer interface software modules"); "~11 research teams", "2017-2021", "David Gunning" absent from cited page |
| SANS AI Survey & SOC Automation (1939) | UR | Both landing pages login-gated ("Login to download"); figures sit in gated PDFs. Drift: 2024 AI Survey byline Edmondson & Bromiley — not the entry's author list (Crowley authors the 2025 SOC Survey) |
| CISA - Enhanced Security Monitoring (1968) | SKIP | Part 1 / fix pass |
| MITRE Insider Threat (1993) | CM | "over 15 years of scientific research" + BDL verify; "47 ATT&CK techniques, 29 sub-techniques" absent (belongs to Insider Threat Knowledge Base 2.0) |
| Microsoft - Threat Modeling AI/ML (2017) | V | Doc dated November 2019; threats #1–#11 incl. "#11 Exploit software dependencies"; untrusted-training-data supply-chain claim verbatim |
| Apache Arrow - powered_by (2042) | CM | VAST entry verifies verbatim; Snowflake and Streamlit are NOT on the current powered_by list (entry names both) |
| Champion-Challenger Pattern (2067) | VQ | "similar concept to A/B testing"; post is 2020-06-19, entry says 2022-2024 |
| Open Cybersecurity Alliance (2092) | VQ | "standardized data interfaces… interoperate without the need for custom integrations"; OASIS confirmed |
| MITRE Engenuity - ATT&CK Evals (2117) | SKIP | Part 1 / fix pass |
| Microsoft - Concept Drift (2146) | UR | Khoros community JS shell; title matches, body never renders |
| Confluent - ML with Kafka (2171) | CM | KSQL/Kafka-Streams claims verify; "Current 2023: …generative AI" absent — page is a single 2018-11-19 Waehner post |
| Amazon Security Lake + Iceberg (2200) | CM | 3 of 4 verbatim incl. "support for Open Cybersecurity Schema Framework (OCSF) v.1.1.0 and Apache Iceberg tables"; "Direct query from Athena, Redshift, Spark, EMR" is on the features Alt URL, not the cited announcement |
| StarRocks vs ClickHouse (2227) | NO-URL | URL field "Various (Tinybird, StarRocks, Medium)" |
| MOAR Stack (2254) | SKIP | Part 1 |
| Goal Drift, arXiv 2505.02709 (2298) | V | "maintains nearly perfect goal adherence for more than 100,000 tokens"; authors/date exact |
| Adaptive Monitoring, arXiv 2509.00115 (2313) | V | "83% report capability metrics while only 30%…"; 12.3s→5.6s and 4.5%→0.9% verbatim |
| SSGM, arXiv 2603.11768 (2328) | V | "consistency verification, temporal decay modeling, and dynamic access control" verbatim; conceptual (no empirical eval) as entry states |
| OpenSec, arXiv 2601.21083 (2343) | UR | abs URL served an unrenderable PDF ×2; title matches via header; 100%/82.5%/62.5%/45%/10.6 uncheckable |
| Gartner AI Maturity (2368) | NO-URL | "Multiple Gartner reports" |
| AI Governance Maturity Gate (2391) | NO-URL | "LinkedIn professional discourse" |
| RAPTOR Framework (2416) | NO-URL | "LinkedIn announcement" |
| NANDA - Internet of AI Agents (2441) | CM | "builds on Anthropic's Model Context Protocol (MCP)" verifies; Raskar arXiv verified. Absent from both cited pages: "1,000+ agents via Join39", MLflow/Databricks validation, Google A2A. Site stale (still advertising the April 2025 summit) |
| Tenzir MCP Parsers (2467) | CM | "generate validated, 100%-schema-conforming OCSF mappings" verbatim; "Production deployment validated (December 2025)" absent — page is the v0.1 announcement, 2025-08-21, Jannis Köhl (entry: Nov-Dec 2025, Vallentin) |
| Tenzir Platform (2494) | V | "Slash software licenses, infrastructure footprint, and operational overhead for a 30% lower TCO"; shift-left + C++ SDK on page |

### 5.5 Lines ~2500–3315 (19 rows)

| Entry (~line) | Verdict | Evidence / reason |
|---|---|---|
| Security Data Pipeline Market Guide 2025 (2521) | CM | Verified verbatim: "$200 million in ARR", "behind only Wiz, HashiCorp, and Snowflake", "doubling every ~18 months", "more than 40–50 security tools". Absent: "50-70% log volume reduction" — page says "reduce volume by 80% or more" (general) and "25–70%" (Axoflow-specific). Byline 2025-04-21, not Feb 2025 |
| Rippling - Cost-Effective SIEM 3-part (2548) | V | Part 3: "approximately 1.8 credits per month in Snowflake, or $4.50 USD"; Part 2: "ingestion latency is less than one minute"; $31-34 = accurate sum of page components |
| Monad - Cutting SIEM Costs (2577) | V | "Annual Savings: $11,721 per million daily Okta events"; "50.7% reduction"; "$25/GB/day" vs "$0.023/GB/month". Note: 1,087× is derived arithmetic; page 2025-09-04 |
| SOC Automation ROI (2604) | NO-URL | "Multiple industry reports" |
| Anonymized practitioner (2779) | NO-URL | Personal communication |
| Apache Iceberg 2025 Performance (3001) | UR | Page live (HTTP 200) but fetch output truncates inside the version-selector nav ×2; body never renders — "10× over Hive" uncheckable either way |
| SANS AI Security Controls (3026) | V | "three bedrock principals: robust security controls, governance and compliance, and a risk-based approach"; six categories present. Nuance: audit logging is a sub-item, not a category. 2025-03-31, Rob T. Lee |
| Security Data Lakehouse Patterns (3049) | NO-URL | "Various (Snowflake, Ryft.io, Query.ai, Dremio)" |
| Data Catalog Wars 2025 (3072) | CM | "the only catalogs that offer this are Unity, Polaris, and Gravitino" verbatim; but Nessie is NOT in the comparison's evaluated scope (one passing mention) — the entry's Nessie characterization is mis-attributed to this source |
| RLS Performance Studies (3097) | NO-URL | "Various database documentation and benchmarks" |
| OCSF RLS Overhead — SDW Lab (3121) | NO-URL | First-party measurement; repo-relative results path |
| Streaming vs Batch Cost 2025 (3141) | UR | Report form-gated; landing verifies "44% of IT leaders reporting 5x returns" + n=4,175; "86%" uncheckable. URL rolling over to the 2026 edition |
| CSA/Google - State of AI Security (3169) | UR | PDF login-gated; landing (released 2025-12-17) verifies "AI governance is the strongest predictor of AI readiness"; 46%/12% corroborated verbatim via the CSA press release; 26%/54%/60% uncheckable |
| CSA Press Release (3196) | CM | Entry's "about 25% have comprehensive AI security governance" mis-scopes the page's 25%: "early adoption of agentic AI (46%) compared to those with only partial guidelines (25%) or policies still in development (12%)". n=300, Summer 2025 |
| SANS - Securing AI in 2025 (3219) | V | "Separating Sensitive Data: Avoid training AI models with highly confidential or personal information…" + incident-response/incremental claims verbatim. Flag: same URL as row "SANS AI Security Controls" but tiered A here vs B there |
| Databricks Cyber Defense (3246) | V | "a 75% reduction in daily processing and storage costs, alongside real-time alerting delivered in under five minutes" (Barracuda); Palo Alto "factor of three" |
| ClickHouse - GitLab (3269) | V | "queries over 100M rows that once took 30–40 seconds now return in under a second"; byline 2025-10-21. Entry's internal freshness footnote ("pre-2025") is stale |
| ClickHouse vs Snowflake (3292) | V | "ClickHouse Cloud is 3-5x more cost-effective than Snowflake" + "over 2x faster"; 2023-09-06. Entry's Validation line still says "(2024)" — stale |
| Netflix ClickHouse 5 PB/Day (3314) | SKIP | Part 1 |

### 5.6 Lines ~3316–3769 (18 rows; range completed across two passes — seam at Obsidian, no gaps)

| Entry (~line) | Verdict | Evidence / reason |
|---|---|---|
| Forrester - Drowning in Security Data (3337) | V | "data retention in the data lake tier is priced at less than 15% of its traditional analytics logs" |
| Hunters - Security Data Lakes (3359) | CM (minor) | "of the world's 15 largest banks… half of them are using a security data lake"; HSBC "3x more hunts while lowering the total cost of ownership" — both verify. "Skills shortage" bullet absent |
| Linux Foundation - OCSF (3384) | CM | "over 900 contributors and 200 participating organizations" verifies. Page (2024-11-19): "The latest version, 1.3.0, released in August 2024" — entry's v1.4.0–v1.7.0 velocity, "80%+", adoption list on NEITHER cited URL |
| Apache Gravitino (3418) | CM | Pinterest talk + "OAuth2: Modern web-based authentication" verify; Ranger integration and geo-distributed bullets NOT in article. Author: Medium account "Office", 2025-08-26 |
| Apache Polaris - Ecosystem (3444) | CM (partial) | "Commercial offerings from Dremio and Snowflake have already proven its production readiness" verifies; 1.2.0 governance quote verifies. Absent: "time travel, commit retries, STS credential vending"; 1.0.0/1.1.0 dates not on cited pages. "Dremio is now part of SAP" banner |
| Google Cloud - AI Agent ROI (3472) | V | "74% of executives report achieving ROI within the first year"; 52% production; 39% >10 agents. 2025-09-04 |
| PagerDuty - Agentic AI ROI (3495) | V | "(62%) expect more than 100% ROI… 171% ROI… almost 2x (192%)"; n=1,000 (Wakefield, Feb-Mar 2025) |
| Obsidian - AI Agent Landscape (3518) | CM | Monitoring claim present; MTTD/MTTR/false-positive-rate and SIEM/SOAR content absent — page rewritten (updated 2026-06-30) after the entry's 2026-06-05 validation |
| Arctic Wolf Aurora (3545) | CM | "reduced 330 trillion raw observations down to 8.6 million alerts — a noise reduction rate of more than 99.99999%" — entry says 99.999%. Absent from both URLs: 116T→20T, OCSF, multi-tenant portal, Sevco (Alt URL names UpSight) |
| DuckDB 1.0-1.4 LTS (3573) | CM | Verified: "This is an LTS release with one year of community support", Iceberg writes, 5-10× compression speedup, "over 3,500 commits by over 90 contributors". Absent: v1.0 "Snow Duck" (page table: codename "Nivis"), download counts, Facebook/Google/Airbnb usage |
| Hyperscan (3607) | VQ | NSDI '19 page verifies scope. Entry author list garbled — actual: Xiang Wang, Yang Hong, Harry Chang, KyoungSoo Park, Geoff Langdale, Jiayu Hu, Heqing Zhu |
| DBSP (3631) | VQ | feldera repo: "The formal model that underpins our system, called DBSP". Paper is VLDB, Aug 2023, "Automatic Incremental View Maintenance for Rich Query Languages"; entry Date: TBD |
| Xor Filters (3655) | VQ | "xor filters can be faster than Bloom and cuckoo filters while using less memory" |
| Matryoshka (3692) | VQ | "directly inferring log syntax, variable naming, and normalization to common security-specific schemas (e.g., OCSF)". PDF title "Semantic-Aware Parsing for Security Logs"; 7 authors (UC Berkeley + Google) |
| ChronoCTI mining temporal patterns (3708) | VQ | "we propose ChronoCTI, an automated pipeline for mining temporal attack patterns" — title exact, 2024-01-03 |
| F3 (3723) | CM | Title/authors/venue verify. "~0.001% overhead" nowhere in paper; but "approximately 150 KB—negligible compared to the achieved size reduction" IS in the paper — entry's dismissal of 150 KB as secondary-only is inverted |
| Base-Rate Fallacy (Axelsson) (3741) | UR | dl.acm.org empty body ×2 (bot-block); no Alt URL in entry — unverifiable here |
| Outside the Closed World (3764) | VQ | Verified via entry's Alt URL (icir.org PDF): "the task of finding attacks is fundamentally different from these other applications"; semantic gap, cost of errors, traffic diversity all present. Primary ACM URL blocked |

### 5.7 Lines ~3770–4065 (17 rows)

| Entry (~line) | Verdict | Evidence / reason |
|---|---|---|
| Ursa, PVLDB 2025 (3791) | V | "Ursa delivers a 92% cost reduction relative to Kafka (Disk) and a 78% reduction compared to Kafka (TS)"; ~5 GB/s; ≈5% spend; PVLDB 18(12):5184-5196. Drift: first author Merli (entry: "Guo et al."); figures in Figure 10, not Table 1 |
| MITRE D3FEND (3819) | VQ | Live knowledge graph; NSA funding. Site badge reads **1.4.0** — resolves the entry's v1.3-vs-v1.4 open question |
| MITRE ATLAS (3837) | UR | JS shell — title only, no body |
| Secure Controls Framework (3853) | CM | Page: "The SCF maps 1,500+ controls across 200+ laws, regulations, and industry frameworks" (v2026.2) — entry's 1,200+/150+ stale |
| NIST CSF 2.0 (3868) | VQ | Live; "Celebrating Two Years of CSF 2.0" |
| CISA ICS Guidance (3883) | VQ | Live — clears entry's ⏳ re-verify flag |
| CoSAI (3898) | VQ | WS2 "Preparing Defenders…" repo live, OASIS confirmed |
| MITRE CAR (3913) | VQ | "a knowledge base of analytics developed by MITRE based on the MITRE ATT&CK adversary model" |
| Atomic Red Team (3931) | VQ | "library of tests mapped to the MITRE ATT&CK® framework"; MIT license |
| MITRE D3FEND 1.0 (3949) | V | "Built upon OWL 2 DL…"; release 2025-01-16; Kaloroumakis; ~450 artifacts supports "400+" |
| BFO ISO 21838-2 (3967) | UR | iso.org serves empty body to fetchers (entry already notes the 403); corroborated indirectly by CCO page |
| Common Core Ontologies (3985) | V | "a widely-used suite of eleven ontologies… extends from the Basic Formal Ontology (BFO)"; v2.1 Apr 2026. Entry says "eleven+" — page says exactly eleven |
| Zeek Docs (4005) | VQ | "Book of Zeek (8.2.1)" |
| Power Query M (4020) | VQ | "functional, case sensitive language similar to F#" |
| DataFusion Ballista (4037) | VQ | Official docs; changelogs through 53.0.0/54.0.0 |
| Lakekeeper (4052) | VQ | "rust native Iceberg REST Catalog"; "Single binary… no JVM"; 0.13.x = still pre-1.0 as entry states |
| Architecting an Iceberg Lakehouse - Merced (4071) | SKIP | Part 1 |

### 5.8 Lines ~4066–4325 (15 rows)

| Entry (~line) | Verdict | Evidence / reason |
|---|---|---|
| Kafka to Iceberg: 9 Solutions - Streambased (4087) | CM | Real post: "The 9 Ways to Move Data Kafka -> Iceberg" (2025-10-20). The 9 = Kafka Connect, Redpanda, Confluent TableFlow, WarpStream TableFlow, AutoMQ, Bufstream, Aiven, StreamNative Ursa, Streambased — **Apache Fluss (in entry) absent**; entry omits Kafka Connect/WarpStream. Cited URL is the blog root, not the article |
| Okta Multi-Engine Stack - Hurault (4102) | V | "1 million DuckDB invocations per day in average. Peaks of up to 250GB of data processed per minute !" (2024-05-01). Cited URL is newsletter root; figures at the /p/ article |
| SOC Modernization & AI - Chuvakin (4117) | VQ | Podcast page live (Chuvakin & Peacock); ep-236 number not shown on fetched page; no figures in entry |
| Anthropic - AI for Cyber Defenders (4132) | CM | Report page dated **Nov 13, 2025** — entry says "November 2024". Substance holds: "human intervention required only sporadically (perhaps 4-6 critical decision points per hacking campaign)" |
| Miessler - ITEM Framework (4147) | V | "the metrics concept we'll remember as ITEM (EYE-tehm)" + the five dimensions. Drift: retitled "Business AI Is the Automation of Intelligence Tasks", dated 2024-07-29 (entry: 2025) |
| Josh Devon - Hijacked Claude Skill (4162) | MV | securetrajectories.substack.com redirects to **blog.sondera.ai** ("Secure Trajectories by Sondera"); cited article not in visible archive; entry's "October 2024" implausible (pre-dates Claude Skills; publication ~mid-2025) |
| AI Engineering - Chip Huyen (4177) | V | Repo citation block: "Chip Huyen, *AI Engineering*. O'Reilly Media, 2025." |
| Stillions - DML Model (4192) | VQ | Page live; body is a JS Blogger template (ladder not textually confirmable). Permalink dates it 2014-04-21 (entry: May 2014) |
| SCYTHE PTEF (4214) | VQ | "collaborative security exercises that bring together CTI, Red Teams, and Blue Teams"; current PTEFv4 |
| Kingpin - Poulsen (4237) | NO-URL | Print ISBN only; no fetchable URL given |
| Iceberg v3 Spec (4257) | V | "Versions 1, 2 and 3 of the Iceberg spec are complete and adopted by the community"; v3 feature list verbatim (variant, geo types, ns timestamps, defaults, row lineage, deletion vectors, encryption keys) |
| Iceberg v4 Milestone #58 (4274) | V | "Iceberg V4 Spec… 0% complete", exactly 2 open proposals (#13153, #13141); spec page: "Version 4 is under active development" |
| DuckLake v1.0 (4290) | SKIP | Part 1 |
| Variant Open Standard (4314) | V | "improves read performance 8x… and 30x compared to using string"; "ratified in the Apache Parquet™ community"; 20-50% slower writes; Parquet 2.12.0; 2025-10-10 |
| OCSF Schema v1.8.0 (4330) | SKIP | Part 1 |

### 5.9 Lines ~4326–EOF (16 rows)

| Entry (~line) | Verdict | Evidence / reason |
|---|---|---|
| NANDA Index in Practice, arXiv 2508.03101 (4347) | V | "global agent discovery, cryptographically verifiable capability attestation through AgentFacts, and cross-protocol interoperability across… MCP… A2A… NLWeb"; abstract has no % metrics — consistent with the entry's own 98.7%-unsupported flag. Subtitle ": An Enterprise Perspective" omitted by entry |
| Splunk 10.4 + Cisco Data Fabric (4363) | CM | "Introducing Federated Search, a core pillar of the Cisco Data Fabric powered by the Splunk Platform" verifies (SPL2, BYO catalogs, SAIA 2.0 too). "Federated Search for Snowflake GA July 2026" absent — Snowflake unmentioned on page |
| Amazon S3 Tables (4379) | V | "first cloud object store with built-in Apache Iceberg support… up to 3x faster query throughput and up to 10x higher transactions per second". REST-Catalog-Mar-2025 addendum necessarily not on this Dec-2024 page |
| Apache Iceberg 1.11.0 (4395) | CM | Post covers "support for Apache Spark 4.1 and Apache Flink 2.1… REST catalog learns to plan scans server-side", encryption, File Format API, SQL UDFs. No V3-stabilization framing. Post 2026-05-27 (Stephen & Uyarer), entry says May 19 |
| OCSF Achieves ITU Support (4412) | V | "Slated for official ratification as an ITU x.*** international standard by June 2026"; "In December 2025, ITU member nations formally supported OCSF"; Wallace, 2026-03-24. Cross-source conflict: this page dates v1.8.0 to Mar 16, 2026 (bibliography entry: Mar 18) |
| MITRE D3FEND for OT (4428) | CM | "extended its D3FEND cybersecurity ontology to operational technology (OT)" verifies (2025-12-16, NSA). "267 defensive techniques", "v1.3.0", OWL 2 DL absent from cited release. Funder: "Office of the Under Secretary of War for Acquisition and Sustainment" |
| Cohasset - S3 Object Lock (4445) | V | Meets "SEC Rules 17a-4(f)(2) and 18a-6(e)(2) and FINRA Rule 4511(c)" + CFTC 1.31(c)-(d); Compliance mode "cannot be removed by any user, even administrators with the BypassGovernanceRetention permission" (page says "any user", not "root account") |
| pySigma-pipeline-ocsf (4462) | CM | "provides the package `sigma.pipeline.ocsf`…" verifies (MIT, pre-release, Baecker; no "Detection Finding" — that correction holds). README logsource-category list now counts **25**, not the entry's asserted 23 |
| Declined stub — EITT Academy (4478) | STUB | Documented rejection stub |
| Cribl "Finality" Case Study (4484) | V | "Being able to get a 47% reduction on average in our Windows Events by dropping repetitive fields is huge"; "10x faster data extractions"; 301s to /resources/cs/finality |
| Fortinet + NVIDIA BlueField-3 (4501) | V | "offloads networking and security functions in an isolated trust domain"; "executes on the DPU, bypassing the host CPU"; FortiOS 7.6.3. No dateline visible in render |
| Databricks Cross-Engine ABAC (4518) | V | "Unity Catalog returns a filtered scan plan scoped to the data the user is authorized to access"; "built on the Iceberg REST Catalog scan APIs"; Beta; 2026-06-02 |
| Apache Polaris TLP + Credential Vending (4535) | SKIP | Part 1 (note: entry's URL is polaris.apache.org/blog/2026/02/19/…, matched on entry name) |
| KPMG AI Pulse Q3 2025 (4552) | V | "42% of organizations now having deployed at least some agents, up from 11% two quarters ago"; 57% ROI-in-12-months; 130 leaders, $1B+ revenue; 2025-09-18 |
| FastLanes File Format (4569) | V | "43 times faster than Parquet+Snappy, 44 times faster than Parquet+ZSTD, 7 times faster than BtrBlocks, and 29 times faster than DuckDB"; random access "315 times faster". PDF now text-extracts (entry's extraction-blocked note can be cleared) |
| DuckLake - Data Inlining (4586) | V | "two orders of magnitude faster across the board, and nearly three orders of magnitude faster for aggregations"; tables match entry exactly (105×/923×/189×; 5.2×/925.9×/14.5×). The entry's cross-baseline decomposition is more accurate than the blog's own TL;DR pairing |

---

## 6. Appendix G & J detail (non-LIVE rows itemized; LIVE rows rolled up per section)

### 6.1 Appendix G — non-LIVE rows

| Section | Vendor (row) | Verdict | Detail |
|---|---|---|---|
| SIEM | Microsoft Sentinel | MOVED | Redirects to microsoft.com/en-us/security/business/siem-and-xdr/microsoft-sentinel (off the Azure catalog); product name unchanged |
| SIEM | Palo Alto Cortex XSIAM | UNREACHABLE | Empty body ×2 — JS/bot-blocked; not evidence of error |
| SIEM | Rapid7 InsightIDR | MOVED | Redirects to /products/siem; page now "Incident Command: AI Powered Next-Gen SIEM" — product renamed |
| SIEM | SentinelOne Singularity AI SIEM | UNREACHABLE | Empty body ×2 — JS/bot-blocked |
| SIEM | Sysdig Secure | MOVED | Redirects to /products/platform, titled "Sysdig Platform" |
| SIEM | Query.ai / Hydrolix (Query Engine) | SKIPPED-PART1 | Verified in part 1 |
| Detection & Response | Velociraptor | MOVED | velocidex.com root is now a stub ("Docs moved here" → /docs/); no marketing page at root |
| Data Lakehouse | Databricks Lakebase | URL-DEAD | databricks.com/lakebase serves an empty body; live page exists at databricks.com/product/lakebase |
| Data Lakehouse | Apache Iceberg | LIVE (via j-pass) | g-pass fetch exceeded the tool's response-size limit; same URL fetched LIVE in the appendix-j pass |
| Catalog & Governance | Alation | MOVED (rebrand) | Now "Alation Intelligence Operating System (AIOS)"; old product name gone from homepage |
| Catalog & Governance | Collibra Data Intelligence | MOVED (rebrand) | Now "Collibra Platform" / "Enterprise AI Control Plane" |
| Catalog & Governance | DataHub | MOVED | datahubproject.io redirects to datahub.com — "DataHub Cloud" by Acryl Data |
| Catalog & Governance | Microsoft Purview | MOVED | azure.microsoft.com/services/purview redirects to microsoft.com/en-us/security/… |
| ETL/ELT | Matillion | MOVED (rebrand) | Homepage fronted by new "Maia" AI platform; Data Productivity Cloud demoted to "Existing Customers" link |
| Observability | New Relic One | MOVED (rebrand) | Branding is now "New Relic" / "Intelligent Observability"; "New Relic One" not used |
| Object Storage | MinIO | LIVE (rebrand note) | Flagship now marketed as "AIStor"; Community Edition still MinIO |
| Data Virtualization | Dremio | LIVE (ownership note) | Banner: "Dremio is now part of SAP" |
| Other | Knostic | MOVED | knostic.com is a parked for-sale domain (BrandBucket). Vendor live at **https://www.knostic.ai** — "AI Security Platform \| Knostic" (fetched this pass) |

**LIVE roll-up** (fetched, matches row): SIEM — Anvilogic, Google SecOps (new canonical URL confirmed live: "formerly known as Chronicle"), CrowdStrike Falcon LogScale, Devo, Elastic Security, Exabeam, Grafana Loki, Graylog, Gurucul, IBM QRadar, Panther (page notes acquisition by Databricks), Securonix, Splunk ES, Stellar Cyber, Sumo Logic, Torq, Wazuh. Detection & Response — FunnyWolf agentic-soc-platform, LimaCharlie, Tracecat, Vigil, Wazuh (dup), Zeek. Query Engine — Athena, Drill, Impala, Pinot, ClickHouse, BigQuery, PrestoDB, StarRocks, Trino. Streaming — Kinesis, Flink, Kafka, Pulsar, Storm, Azure Event Hubs, Confluent, Pub/Sub, RabbitMQ, Redpanda. Data Lakehouse — Druid, Hudi, Paimon, Databricks, Delta Lake, Snowflake. Catalog — AWS Glue, Apache Atlas, Atlan, Select Star. ETL/ELT — Airbyte, NiFi, Cribl Stream, DataBee, Databahn.ai, Estuary, Fivetran (page notes dbt Labs merger), Qlik Talend, Tenzir. Observability — Axiom, Datadog, Dynatrace, Grafana Cloud, Honeycomb, Splunk Observability Cloud. Object Storage — S3, Azure Blob, Ceph, GCS, MinIO. Data Virtualization — Calcite, Denodo, Dremio, Starburst Enterprise.

### 6.2 Appendix J — non-LIVE rows

| Section | Link | Verdict | Detail |
|---|---|---|---|
| J.1.3 | AWS Kinesis Data Firehose | MOVED | Redirects to aws.amazon.com/firehose — renamed "Amazon Data Firehose" (Kinesis dropped) |
| J.2.1 | Great Expectations integration page | MOVED | Redirects to /docs/help/compatibility_reference |
| J.2.4 | EvidenceForge | SKIPPED-PART1 | Part 1 |
| J.6.2 | Databricks Delta page | MOVED | Redirects to /product/lakehouse-storage — "Lakehouse Storage", now covers Delta+Iceberg (first-half 429 leftover, resolved second pass) |
| J.9.1 | apache-iceberg.slack.com | UNREACHABLE | Slack login wall for non-members |
| J.9.1 | Iceberg GitHub /discussions | UNREACHABLE | Empty render |
| J.9.1 | stackoverflow.com/…/apache-spark | UNREACHABLE | Fetcher blocklist (403 cowork_web_fetch_url_blocked) |
| J.9.1 | apache-airflow.slack.com | UNREACHABLE | Slack login wall |
| J.9.2 | community.dremio.com / bit.ly/dremio-slack | SKIPPED-PART1 | Part 1 |
| J.9.2 | starburst.io/slack | UNREACHABLE | Empty render |
| J.9.2 | community.starburst.io | MOVED | Redirects to starburst.io/community/forum (same forum, new path) |
| J.9.3 | reddit.com/r/dataengineering | UNREACHABLE | Fetcher blocklist |
| J.10.2 | mitreattack.slack.com | UNREACHABLE | Slack login wall |
| J.11.1 | schema.ocsf.io (×2 occurrences) | UNREACHABLE | SPA shell (same as part 1; v1.8.0 corroborated via GitHub releases there) |
| J.11.1 | ocsf.slack.com | UNREACHABLE | Slack login wall |
| J.11.1 | linuxfoundation.org/projects/ocsf | UNREACHABLE | Empty render |
| J.13.2 | tabular.io/blog | MOVED | Live but frozen at 2023 pre-acquisition posts; current content at databricks.com/blog (already a LIVE row) |
| J.13.2 | netflixtechblog.com | UNREACHABLE | Medium bot-block (same behavior as the bibliography's Netflix WAL entry) |

**LIVE roll-up** (fetched, matches row — annotations in parentheses): all J.1–J.6 official docs and integrations not listed above (Flink, Iceberg-Flink, AWS Managed Flink, Spark Structured Streaming (guide reorganized in Spark 4.0+), Iceberg spark-writes, Firehose Lambda transformation, GX docs, dbt docs + Iceberg support, Soda docs + soda-core, Airflow docs, MWAA, Step Functions, Grafana docs + datasources, Jupyter, JupyterHub, SageMaker docs (retitled "Amazon SageMaker AI"), SageMaker examples, MLflow, Iceberg docs/spec/Glue integration, Delta docs); J.9–J.13 — Iceberg community page, Databricks Community, Airflow community + issues, Data Engineering Weekly, DetectionLab (repo live but unmaintained since 2023-01-01), SANS ISC, attack.mitre.org, mitre-attack GitHub, d3fend.mitre.org + GitHub, OCSF GitHub, iceberg/spark/flink/airflow project sites, CNCF, NIST CSF, CIS Controls, Iceberg/Trino/Dremio/Spark release pages, securitydataworks.com writing/lab/sigma-essay, Databricks/Dremio/Starburst blogs, Uber engineering blog, Data Engineering Podcast, ISC Stormcast; duplicate J.17/References occurrences reuse these verdicts.

---

## 7. Environment notes & limits (read before acting on any verdict)

1. **No git in this session.** The shell sandbox could not mount this repo's WSL path (UNC unsupported — same as part 1), so nothing in this report asserts git state (tracked files, branches, tags, hooks). Anything requiring git is labeled for the local session; the branch/commit context cited in §"What this is" comes from CHANGELOG.md's text only. NEEDS-LOCAL-CONFIRMATION applies to all of it.
2. **Rate limiting shaped the run.** A session-wide web_fetch quota (HTTP 429) stalled mid-sweep twice; two passes stopped cleanly at a named entry/row rather than guessing, and follow-up passes completed both remainders after the quota lifted. Final coverage is complete as accounted in §2 — no verdict below rests on an unfetched page.
3. **Fetcher blocklist / bot-gates encountered** (UNREACHABLE ≠ dead): web.archive.org (blocked, per part 1), stackoverflow.com and reddit.com (403 `cowork_web_fetch_url_blocked`), dl.acm.org, iso.org, atlas.mitre.org, YouTube, *.slack.com workspaces, netflixtechblog.com (Medium), techcommunity.microsoft.com (Khoros), docs.dremio.com (Docusaurus shell), paloaltonetworks.com, sentinelone.com, schema.ocsf.io (SPA), aws.amazon.com/s3/pricing (tables JS-rendered), plus one response-size failure (iceberg.apache.org, resolved via a second fetch in another pass). Recommend local browser spot-checks for: Bisnett video (Huntress figures), Cortex XSIAM / SentinelOne rows, ATLAS, Axelsson base-rate paper (only entry left unconfirmed at its primary with no Alt URL).
4. **Line numbers and counts.** Grep- vs Read-reported line numbers drifted ~20 lines through the file's middle; §5 line numbers are anchors, not edit targets — re-grep by title locally. This sweep traversed 182 `#### ` blocks (+2 legacy `###` entries) vs CLAUDE.md's stated 179; run `scripts/automation_dashboard.py` locally to reconcile before citing a count. NEEDS-LOCAL-CONFIRMATION.
5. **What this session touched**: exactly one file — `VERIFICATION-SWEEP-PART2-2026-07-10-cowork.md` (this report), created at the repo root. No other file was created, edited, or deleted.

---

## 8. Git handoff (for the local session — verify before committing)

```bash
cd ~/security-data-literature-review
git status                       # confirm the ONLY change is the new report file
git checkout -b litreview-verify2-2026-07-10
git add VERIFICATION-SWEEP-PART2-2026-07-10-cowork.md
git commit -m "📋 Verification sweep part 2 (cowork): 139 bibliography entries + 185 appendix links — 49 verified, 41 qualitative, 33 claim-mismatch, 3 moved, 13 unreachable; appendix G/J: 16 moved/rebranded, 1 dead, Knostic re-pointed to knostic.ai"
git push -u origin litreview-verify2-2026-07-10
```

Suggested local pre-commit checks: spot-verify two or three §5 verdicts at their primaries (e.g., LF-OCSF press release, Arctic Wolf PR, Streambased article), and run the dashboard for the count reconciliation in §7.4. Never push to main/master; no force-push or rebase needed (new branch, single new file). Per the citation-stability rule, the CHANGELOG entry belongs with whichever future commit *applies* fixes from §4 — this report itself changes no content.

---

**Sweep run**: 2026-07-10, Cowork cloud session (part 2 of 2) · 139 bibliography entries fetch-adjudicated + 29 part-1 skips, 2 stubs, 14 no-URL accounted (184 rows) · appendix-g 93 rows and appendix-j 92 URL occurrences fully accounted · web.archive.org/stackoverflow/reddit blocked in-environment (noted per item) · No repo file edited; §4 is proposals only.
