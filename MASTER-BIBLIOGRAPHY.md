---
type: reference
title: "Master Bibliography: Security Data Works Living Literature Review"
created: 2025-10-15
tags: [bibliography, literature-review, security-data, lakehouse, clickhouse, ocsf]
---

# Master Bibliography - Living Literature Review

**Purpose**: The citation record for the Security Data Works evidence program, which covers the handbook *Modular Open Architecture (MOAR) for Cybersecurity Data*, the securitydataworks.com essays and research pages, and this review's own manuscript. Each `#### ` block below is one source, with its evidence level, what it is cited for, what it actually says, and how it was checked.
**Last Updated**: November 23, 2026 (monthly refresh: six sources added under "Monthly Refresh Additions (2026-11-23)", eight older entries re-read at their primaries with dated refresh notes, two dead links moved to archived copies). November 17, 2026: verification sweep of every entry, recorded in `methods/verification-2026-11/`; the retired December 2025 benchmark entry rewritten to cite the public SDW Lab re-run; the October 2025 extraction log moved to `archive/bibliography-extraction-log-2025-10.md`). Earlier changes are in [CHANGELOG.md](CHANGELOG.md).
**Total Sources**: 279 catalogued `#### ` blocks (277 tiered sources + 2 documented stubs — the "Declined — EITT Academy" no-primary record and the retired phantom "Streaming vs Batch Cost Differential" CloudZero placeholder). The counts on this page are derived from the blocks by `scripts/count_reconcile.py`, which fails the build when any gated surface disagrees with them.
**Evidence Quality**: 23.1% Evidence Level A (live-derived 2026-11-23: 64 of 277 tiered entries; 173 B, 40 C, across 279 `#### ` blocks incl. 2 documented stubs). The share is reported descriptively and has no target attached. It sits where it does because Level A is reserved for peer-reviewed research and official standards, so vendor engineering blogs, trade books, conference talks and production case studies tier at B however good their evidence is, and much of what a practitioner needs to know about security data platforms is published mainly in those forms.

**How to read an entry.**
- **Evidence Level** follows [METHODOLOGY.md §3.1](METHODOLOGY.md). A is peer-reviewed research, an official standard, or a normative framework from a neutral non-commercial body (MITRE D3FEND and ATLAS, which are primary for taxonomy and silent on efficacy). B is "practitioners and production evidence — production deployments and case studies with real numbers, vendor engineering blogs, industry-conference talks, trade books, analyst reports, expert interviews, government advisories, and official project documentation", which is real evidence but not independently reviewed (expert interviews appear in that definition, but this file catalogues only published works, per the Boundary rule below). C is "vendor blog posts, product documentation, and conference talks not backed by production measurement", catalogued with its bias flagged and never carrying a hypothesis on its own, and D (marketing material, unverified claims, speculation) is excluded from the corpus.
- **Key Findings** state what the source says. A number in Key Findings should trace to the cited primary, and where the 2026-11-17 sweep could not confirm one at its primary, the number is either removed with a dated note or labelled *unverified* with the reason. Numbers stated outside Key Findings and Notes, such as a figure in a Relevance list, were not swept, so treat them as provisional until an entry marks them verified.
- **Validation Status** and the dated notes beneath it record each check. Where the 2026-11-17 sweep left figures in an entry unconfirmed, the Validation Status line ends with a count of them and each figure carries its own label, so a green mark should be read together with that count, and the ledger below has the per-number verdict.

**Verification record.** The 2026-11-17 sweep wrote one row per entry to [`methods/verification-2026-11/ledger.json`](methods/verification-2026-11/ledger.json), with the identifier checked (DOI, arXiv ID or URL), whether the work exists, and a verdict for each quoted number, and [`methods/verification-2026-11/README.md`](methods/verification-2026-11/README.md) summarizes the verdict counts. Earlier per-reference checks are in [RESEARCH-JOURNAL.md](RESEARCH-JOURNAL.md), which is append-only.

**Boundary**: Public repo. Only published works are catalogued here, and a personal communication is not eligible as a source. One entry's citation of a 2025 personal communication was removed on 2026-08-12 because no such communication had taken place; the entry now cites the person's public Data Council 2024 talk, and the claims that talk does not support were withdrawn rather than re-sourced (see the "Okta Security Analytics — Isolation-First Architecture" entry and CHANGELOG.md). Outreach and relationship tracking is kept outside this repository.

---

## Organization

The corpus was assembled from these routes, each recorded in its own section below:
1. The October 2025 extraction of the 283 footnotes in the 2024-04-15 best-practices document (extraction log archived at `archive/bibliography-extraction-log-2025-10.md`).
2. Curated additions from 2025-2026 research, including the January 2026 research update and the June 2026 merge from the author's research notes.
3. The PRISMA database search arm of 2026-07-13 and its second-screen admission (see [METHODOLOGY.md](METHODOLOGY.md)).
4. The November 2026 citation-graph snowball admissions and the handbook footnote passes.

Sources from practitioner conversations are not eligible; the earlier entries attributed to expert interviews were re-sourced to public material or withdrawn, except that three entries without a citable primary (the anonymized practitioner entry, the AI Governance Maturity Gate entry and the Security Data Lakehouse Implementation Patterns composite) remain catalogued and counted, each with a note against citing it, pending an owner ruling on their withdrawal (noted 2026-11-22).

**Format**: Organized by intake section, with standardized entries including evidence level, relevance to book chapters/hypotheses, and validation status.

---

## Table of Contents

- [Foundational Architecture](#foundational-architecture)
  - [Table Formats (Iceberg, Delta, Hudi)](#table-formats)
  - [Query Engines (Trino, Dremio, ClickHouse)](#query-engines)
  - [Streaming Architectures (Kafka, Flink)](#streaming-architectures)
- [Security-Specific Data](#security-specific-data)
  - [Data Volume & Characteristics](#data-volume--characteristics)
  - [Cost Comparisons](#cost-comparisons)
  - [OCSF & Schema Standards](#ocsf--schema-standards)
- [Vendor Landscape](#vendor-landscape)
  - [Platform Capabilities](#platform-capabilities)
  - [Performance Benchmarks](#performance-benchmarks)
- [Implementation & Organizational](#implementation--organizational)
  - [Change Management](#change-management)
  - [Skills & Staffing](#skills--staffing)
  - [Deployment Patterns](#deployment-patterns)
- [Emerging Technologies](#emerging-technologies)
- [AI-Native Infrastructure & Emerging Architectures](#ai-native-infrastructure--emerging-architectures)
  - [AI Governance & Agent Architectures](#ai-governance--agent-architectures)

---

## Foundational Architecture

### Data Engineering Foundations

#### Fundamentals of Data Engineering (O'Reilly Book)

**Authors**: Joe Reis, Matt Housley
**Date**: June 2022 (O'Reilly platform date, fetch-verified in the part-2 sweep; print edition 2022-07-26 explains the former "July 2022")
**URL**: https://www.oreilly.com/library/view/fundamentals-of-data/9781098108298/
**Alt URL**: https://www.amazon.com/Fundamentals-Data-Engineering-Robust-Systems/dp/1098108302 (ISBN-13 978-1098108304)
**Evidence Level**: B (Authoritative practitioner reference; conceptual framing, not a quantitative source)
**Relevance**:
- Book Chapters 1–2 (the applied-bridge thesis: security's platform problem is largely a data-engineering problem)
- Grounds the bridge's *inclusion* move — the data-engineering lifecycle is what security analysts, threat hunters, and especially detection engineers already perform ad hoc when they pull data out of the SIEM and wrangle it in tools they understand
- The modern-data-stack framing the bridge uses to place security roughly a decade behind the data-engineering field

**Key Findings**:
- The **data engineering lifecycle** — generation, storage, ingestion, transformation, serving — as the durable spine that has "remained essentially unchanged despite the rise and fall of specific technologies and vendor products"
- Treats the lifecycle as independent of any specific tool or vendor — the principle the bridge carries into security: open formats and modular engines outlast the monolith
- Defines data engineering as a discipline in its own right, which is the practice the bridge argues security teams are already doing without naming it

**Citations**: Applied-bridge framing (the relabel + inclusion moves); the modern-data-stack maturation narrative; Joe Reis is the "modern data stack" voice in the origin narrative's cold open (securitydataworks.com/thesis/origin)
**Notes**: Framing/conceptual anchor for the applied-bridge positioning (securitydataworks.com/thesis). Carries no headline statistic — catalogued for the lifecycle framework, not a number, so it is not exposed to the 2026 stat-mismatch audit. Tier B under the strict tiers in METHODOLOGY.md §3.1 (authoritative practitioner book; A is reserved for peer-reviewed research / official standards).

**Validation Status**: ✅ Verified 2026-06-09 (WebSearch: O'Reilly Media, published 2022-07-26, ISBN-13 978-1098108304, Joe Reis & Matt Housley; the data-engineering-lifecycle framework confirmed against the publisher and author listings). · Refresh (2026-11-23): still the only edition. Reis's retrospective, 'The Data Engineering Lifecycle and Undercurrents, 4 Years Later' (joereis.substack.com/p/the-data-engineering-lifecycle-and, 2026-07-27, Tier B, same author), restates the same five stages, says he would write the book the same way 'mostly yes. With some caveats', names more data-modeling depth and FinOps as a possible seventh undercurrent as what he would add, and says of a second edition 'I'm not ruling it out'. The quoted 'remained essentially unchanged...' sentence in Key Findings could not be confirmed verbatim on 2026-11-23 (O'Reilly blocks automated fetch), so treat it as a paraphrase until it is checked against a licensed copy.

---

#### Data Engineering for Cybersecurity (No Starch Press Book)

**Author**: James Bonifield
**Date**: 2025 (No Starch Press, © 2025, first printing)
**ISBN-13**: 978-1-7185-0402-8 (print); 978-1-7185-0403-5 (ebook)
**Subtitle**: Build Secure Data Pipelines with Free and Open Source Tools
**Companion repo**: github.com/bonifield/data-engineering-for-cybersecurity
**URL**: https://nostarch.com/data-engineering-cybersecurity (publisher page, checked 2026-11-17: July 2025, 344 pp, ISBN-13 9781718504028)
**Evidence Level**: B (practitioner reference book; conceptual/tooling, not a quantitative source)
**Relevance**:
- The closest named companion (and competitor) to the MOAR book: "Build Secure Data Pipelines with Free and Open Source Tools." Frames the same underlying problem — security teams are already doing data engineering — from a build-the-pipelines-with-FOSS angle rather than the architecture-decision angle MOAR takes.
- Read for positioning before the next MOAR chapter pass: where it overlaps (FOSS pipelines, parsing and normalization) versus where MOAR is differentiated (open table formats, the trustworthy / well-connected / performant decision frame, the Capability Matrix, the independent-measurement lab).
**Notes**: Title, author, and publisher verified 2026-06-30 from the book cover (PDF/EPUB held in the research inbox). Catalogued as a positioning anchor; carries no headline statistic, so it is not exposed to the stat-mismatch audit.
**Validation Status**: ✅ Title/author/publisher verified 2026-06-30 (book cover); © 2025 and both ISBN-13s verified 2026-11-07 from the book's own copyright page (PDF held in the research inbox). Handbook footnotes in ch01/ch02/ch04 now carry Tier B to match this entry.

---

### Table Formats

#### Apache Iceberg Performance Tuning - SK Telecom

**Authors**: SK Telecom Tech Blog (Jaechang Song, Jennifer Oh)
**Date**: 2022-12-19 (Trino Summit 2022 talk and recap; the former '2022-2024' range had no 2024 primary behind it, corrected 2026-11-23)
**URL**: https://trino.io/blog/2022/12/19/trino-summit-2022-sk-telecom-recap.html
**Alt URL**: https://trino.io/assets/blog/trino-summit-2022/Trino@SK-Telecom.pdf (presentation slides)
**Evidence Level**: B (Production deployment, quantitative benchmarks) — re-tiered from A 2026-08-19: neither peer-reviewed research nor an official standard
**Relevance**:
- Hypothesis H-ARCH-01 (Iceberg dominance)
- Book ch05 §5.1 (table format) [was: Chapter 8] (Storage Formats)
- Best Practices Doc footnote [^3]

**Key Findings**:
- Case 1: −97% read data size (209 GB → 6.11 GB) and −96.5% elapsed time (97.2 s → 3.39 s) with Iceberg optimizations (slides)
- Case-1 table: 52.7 TB Iceberg logical size, 109,765 partitions (was Hive 52.1 TB) — the 3.39 s query reads 6.11 GB after pruning, not the full table (the earlier "processed 52.7TB in 3.39 seconds" framing conflated table size with data read; corrected 2026-07-09)
- Production validation at scale; headline improvement across cases ~−80% (slides)
- Recap-page approximations: input data reduced "on the order of hundreds, down to under ten gigabytes"; query planning ~70 ms
- Metadata indexing and snapshot isolation key to performance gains

**Citations**: ch05 §5.1 (table format) [was: Chapter 8] performance benchmarks
**Notes**: High-credibility source, production deployment, quantitative data; Medium URL returns 403, replaced with Trino Summit recap. **Source split (2026-07-09)**: the precise figures (209 GB, 6.11 GB, 97.2 s, 3.39 s, 52.7 TB, −80%) are in the Trino Summit slides PDF (Alt URL) — verified against the PDF 2026-07-09; the recap page carries only the approximations. Cite the slides for the precise numbers.

**Validation Status**: ✅ Figures re-verified against slides PDF (Alt URL) 2026-07-09; recap URL live (Medium link blocked, replaced January 2026) · Refresh (2026-11-23): both URLs live. The precise figures were re-verified verbatim against the slides PDF and the two approximations against the recap page. SK Telecom's follow-up talk, 'Efficient Kappa Architecture with Trino' (Sanghyun Lee, Trino Summit 2023, https://trino.io/assets/blog/trino-summit-2023/efficient-kappa-architecture-sk-telecom.pdf, HTTP 200), is a candidate companion source that has not been read for figures yet.

---

### Query Engines

#### Starburst - Official Documentation

**Authors**: Starburst Data
**Date**: 2024-2026 (continuously updated)
**URL**: https://docs.starburst.io
**Evidence Level**: B (Vendor documentation, technical authority)
**Relevance**:
- Blog post: "Starburst vs Dremio vs AWS Athena: Core Differences"
- Book ch05 §5.3 + Appendix I [was: Chapter 9] (Query Engines - federated query)
- Trino-based enterprise platform

**Key Findings**:
- Trino (formerly PrestoSQL) enterprise distribution
- Federated query across multiple data sources
- Security features (RBAC, data masking, audit logging)
- Query optimization and performance tuning

**Citations**: Blog query engine comparison, ch05 §5.3 + Appendix I [was: Chapter 9] Starburst capabilities
**Notes**: Commercial Trino distribution with enterprise security features

**Validation Status**: ✅ Active (verified Feb 2026)

---

#### Starburst - AWS Athena Comparison

**Authors**: Starburst Data
**Date**: 2024-2026 (updated)
**URL**: https://www.starburst.io/aws-athena/
**Evidence Level**: B (Vendor comparison documentation)
**Relevance**:
- Blog post: "Starburst vs Dremio vs AWS Athena"
- Book ch05 §5.3 + Appendix I [was: Chapter 9] (Query Engines - hybrid deployment)
- AWS ecosystem integration

**Key Findings**:
- Starburst Galaxy vs AWS Athena capabilities
- Trino-based federation patterns
- Hybrid query engine architectures

**Note**: URL updated 2026-01-03 (original enterprise integration page restructured)
- Cost optimization strategies

**Citations**: Blog query engine comparison, ch05 §5.3 + Appendix I [was: Chapter 9] hybrid architectures
**Notes**: Practical guide for AWS security data architectures

**Validation Status**: ✅ Active (verified Feb 2026)

---

#### Trino: The Definitive Guide (O'Reilly Book)

**Authors**: Matt Fuller, Manfred Moser, Martin Traverso
**Date**: October 2022 (2nd Edition)
**URL**: https://www.oreilly.com/library/view/trino-the-definitive/9781098137229/
**Alt URL**: https://trino.io/trino-the-definitive-guide.html
**Evidence Level**: B (Authoritative technical book, O'Reilly publication) — re-tiered from A 2026-08-19: not peer-reviewed research and not an official standard
**Relevance**:
- Blog post: "Starburst vs Dremio vs AWS Athena"
- Book ch05 §5.3 + Appendix I [was: Chapter 9] (Query Engines - Trino architecture)
- Foundational federated query engine understanding

**Key Findings**:
- Trino architecture and internals
- Query optimization techniques
- Federation patterns for security data
- Production deployment best practices
- 2nd Edition (October 2022) is updated to Trino release 392 and adds Java 17 usage, the Iceberg and Delta Lake connectors, the lakehouse architecture, dbt and Metabase (trino.io announcement, 2022-10-03). A Helm chart for Kubernetes deployment is listed in the table of contents per library catalog records seen only as search summaries. Fault-tolerant execution could not be confirmed for the English edition on 2026-11-23.

**Citations**: Blog query engine deep-dive, ch05 §5.3 + Appendix I [was: Chapter 9] Trino fundamentals
**Notes**: **CRITICAL** - Authoritative Trino reference, Matt Fuller = Starburst co-founder; ISBN 978-1-098-13723-6 (print/paperback, confirmed via ISBN registry 2026-07-10; the cited O'Reilly platform URL carries the digital-edition identifier 978-1-098-13722-9 — both valid, label whichever you cite)

**Validation Status**: ✅ Updated January 2026 - Corrected to 2nd Edition URL · Refresh (2026-11-23): still the latest edition, with no third edition found. The book is pinned to Trino 392 (2022), so version-specific configuration may lag current releases.

---

#### Dremio - Official Documentation

**Authors**: Dremio Corporation
**Date**: 2024-2026 (continuously updated)
**URL**: https://docs.dremio.com
**Evidence Level**: B (Vendor documentation, technical authority)
**Relevance**:
- Blog post: "Starburst vs Dremio vs AWS Athena"
- Book ch05 §5.3 + Appendix I [was: Chapter 9] (Query Engines - semantic layer)
- Data lakehouse query acceleration

**Key Findings**:
- Reflections (materialized views) for query acceleration
- Apache Arrow-based columnar execution
- Self-service data catalog
- Iceberg table format integration

**Citations**: Blog query engine comparison, ch05 §5.3 + Appendix I [was: Chapter 9] Dremio capabilities
**Notes**: Semantic layer approach to data lakehouse architecture

**Validation Status**: ✅ Active (verified Feb 2026)

---

#### Dremio - Data Lakehouse Architecture Guide

**Authors**: Dremio Corporation (Dipankar Mazumdar, Developer Advocate — byline verified 2026-07-10; the former Merced credit was wrong for this URL)
**Date**: 2023-09-06
**URL**: https://www.dremio.com/blog/what-is-a-data-lakehouse/
**Evidence Level**: B (Vendor thought leadership, educational)
**Relevance**:
- Blog post: "Starburst vs Dremio vs AWS Athena"
- Book ch05 §5.1 (table format) [was: Chapter 2] (Data Engineering Foundation - lakehouse architecture)
- Foundational architecture understanding

**Key Findings**:
- Data lakehouse architecture principles
- Separation of storage and compute
- Open file formats (Apache Parquet) on cloud object storage. The article body does not name Iceberg, Delta Lake or Hudi (checked 2026-11-23 against the live page, where Iceberg appears only in site navigation and promo cards), so cite another entry for table formats.
- A data management layer and a data processing layer serving SQL analytics and machine learning, with no named query-engine layer.

**Citations**: Blog query engine context, ch05 §5.1 (table format) [was: Chapter 2] lakehouse fundamentals
**Notes**: Educational resource from Dremio, vendor perspective Page title is 'What Is a Data Lakehouse? Merging Data Lakes and Warehouses' (2023-09-06). Dremio has been part of SAP since 2026-07-06 (news.sap.com/2026/07/sap-completes-dremio-acquisition/), which is ownership context only. The Wayback Machine holds no capture of this URL later than 2023-06-02, so there is no archived copy of the current article.

**Validation Status**: ✅ Active (verified Feb 2026) · Refresh (2026-11-23): live page read, and the table-format and query-engine findings narrowed to what the body says.

---

#### Alex Merced - Dremio YouTube Channel

**Authors**: Alex Merced (Head of DevRel, Dremio, per Dremio's author page 2026-11-23)
**Date**: 2023-2024 (ongoing series; channel page live 2026-11-23, upload recency not confirmed in the check pass)
**URL**: https://www.youtube.com/@alexmercedcoder
**Evidence Level**: B (Vendor educational content, practitioner tutorials)
**Relevance**:
- Blog post: "Starburst vs Dremio vs AWS Athena"
- Book ch05 §5.3 + Appendix I [was: Chapter 9] (Query Engines - practical tutorials)
- Hands-on query engine learning

**Key Findings**:
- Data lakehouse architecture tutorials
- Apache Iceberg hands-on guides
- Dremio query optimization
- No security-data examples found (a channel search for 'security' on 2026-11-23 returns web-auth, JWT and SSH tutorials; finding removed 2026-11-23)

**Citations**: Blog query engine resources, ch05 §5.3 + Appendix I [was: Chapter 9] learning resources
**Notes**: Educational YouTube channel, personal and not an official Dremio channel ('Code, Data and Tech with Alex Merced'). Dremio has been part of SAP since 2026-07-06. A second channel, @alexmerceddata ('Understanding Data with Alex Merced'), is the handle cited in appendix-e. For a citable Iceberg reference, prefer the existing entry 'Architecting an Apache Iceberg Lakehouse' (Manning) in this bibliography, or Apache Iceberg: The Definitive Guide (Shiran, Hughes and Merced, O'Reilly, May 2024), which has no entry yet and was not opened in this pass.

**Validation Status**: ✅ Active (verified Feb 2026) · Refresh (2026-11-23): both channel URLs live, and the security-examples finding removed.

---

#### ClickHouse at Cloudflare - 6M Requests/Second

**Authors**: Alex Bocharov (Cloudflare Engineering Blog)
**Date**: 2018-03-06 (verified at primary 2026-07-09; entry formerly said "2024-2025, updated February 2026" — a bulk-stamp artifact. the Alt-URL post is dated 18 February 2026, corrected 2026-11-17 from "Oct 2025")
**URL**: https://blog.cloudflare.com/http-analytics-for-6m-requests-per-second-using-clickhouse/
**Alt URL**: https://clickhouse.com/blog/cloudflare
**Evidence Level**: B (Production deployment at massive scale) — re-tiered from A 2026-08-19: not peer-reviewed research and not an official standard
**Relevance**:
- Hypothesis H3-PERFORMANCE-01 (ClickHouse OLAP performance)
- Book ch05 §5.3 + Appendix I [was: Chapter 9] (Query Engines)
- Best Practices Doc footnote [^7]

**Key Findings**:
- 6M req/sec sustained (peak 8M req/sec) on the Cloudflare HTTP analytics pipeline
- ~3× replication across 36 nodes for high availability
- −50% query latency achieved via index tuning
- **February 2026 (Alt URL — ClickHouse blog post of 18 February 2026, describing an August 2025 meetup demo)**: a single query scanned 96 trillion events in an hour and returned in under two seconds, with a stated margin of error under one percent
- *Removed 2026-11-17: an "exceeded 1,000 active replicas, hundreds of millions of inserted rows/sec" line, which appears in neither the Alt URL post nor the 2018 primary.*
- Nearly 10 years running on open-source ClickHouse (one of earliest large-scale adopters)
- System withstands large-scale outages without collapsing

**Citations**: ch05 §5.3 + Appendix I [was: Chapter 9] ClickHouse deep-dive, H3-PERFORMANCE-01 validation
**Notes**: Primary Cloudflare post supports throughput/replication/latency figures; the 96-trillion-event query figure is from the ClickHouse blog post of 18 February 2026 (Alt URL). The "96.3% under 1s" figure that appeared in earlier versions is not in either cited source and has been removed.

**Validation Status**: ✅ Refreshed February 2026 against the quadrillion-row ClickHouse blog post, which is dated 18 February 2026 rather than October 2025 as earlier versions of this entry said (date corrected 2026-11-17)

**Validation (2026-06-05, folded)**: corrections applied to findings/tier above; provenance in RESEARCH-JOURNAL.md.
---

#### ClickHouse Log Analytics - Cloudflare

**Authors**: Cloudflare Engineering Blog
**Date**: 2022-09-02 (ClickHouse-hosted Cloudflare blog byline; catalogued "2024" was wrong — corrected 2026-07-09, verified at primary)
**URL**: https://blog.cloudflare.com/log-analytics-using-clickhouse/
**Evidence Level**: B (Production deployment) — re-tiered from A 2026-08-19: not peer-reviewed research and not an official standard
**Relevance**:
- Hypothesis H3-PERFORMANCE-01
- Book ch05 §5.3 + Appendix I [was: Chapter 9] (Query Engines)
- Best Practices Doc footnote [^8]

**Key Findings**:
- ~10× storage reduction migrating Elasticsearch → ClickHouse (600 → 60 bytes/row, LZ4 default compression) — an ES→CH migration figure (columnar + schema change), not a pure columnar-compression ratio; there is no 12× figure on the page (the earlier "10-12×" was corrected 2026-07-09, verified at primary)
- 8× reduction in inserter CPU and memory in the same migration (verified at primary 2026-07-09)
- Error/troubleshooting request-log analytics (security-adjacent, not a security-specific workload)

**Citations**: ch05 §5.3 + Appendix I [was: Chapter 9] compression discussion
**Notes**: Validates compression claims

**Validation Status**: ✅ Active URL · Claim re-verified at primary 2026-07-09 — ~10× ES→ClickHouse storage reduction confirmed on the page; the earlier "10-12×" was corrected (no 12× figure present). Publication date 2022-09-02 (was mis-catalogued as 2024).

---

### Streaming Architectures

#### Kafka Performance Benchmark - Confluent

**Authors**: Alok Nikhil and Vinoth Chandar (Confluent)
**Date**: 2020-08-21 (single benchmark post; the entry's former "2023-2026 continuously updated" framing was wrong — corrected 2026-07-10)
**URL**: https://www.confluent.io/blog/kafka-fastest-messaging-system/
**Alt URL**: https://developer.confluent.io/learn/kafka-performance/
**Evidence Level**: B (Vendor benchmark, methodology disclosed but self-published)
**Relevance**:
- Book ch02 §2.2 (components: collection and pipeline) [was: Chapter 7] (Ingestion)
- Best Practices Doc footnote [^4]

**Key Findings**:
- 605 MB/s peak throughput across 3 brokers (page verbatim)
- "Writing 15x faster than RabbitMQ and 2x faster than Pulsar" (page verbatim) under the benchmark conditions

**Citations**: ch02 §2.2 (components: collection and pipeline) [was: Chapter 7] Kafka performance
**Notes**: Vendor-published benchmark; 605 MB/s, 15× RabbitMQ, 2× Pulsar figures are from the cited blog. Widely referenced but self-published — and a 2020 result on then-current versions; cite the method and ordering, not the absolute numbers, as current. Correction (2026-07-10, part-2 sweep fix 6): the Kora 12×, "10 MBps→1.4 GBps ingress", Kafkorama 1M msg/s fanout, and 2-3 ms latency-delta bullets were removed — none appear on the cited page (exhaustive term search); the Kora figure likely traces to Confluent's separate Kora engine material — re-source there if needed.

**Validation Status**: ✅ Verified at primary 2026-07-10; re-dated to the actual 2020-08-21 post

**Validation (2026-06-05, folded)**: corrections applied to findings/tier above; provenance in RESEARCH-JOURNAL.md.
---

#### Questioning the Lambda Architecture - Jay Kreps

**Authors**: Jay Kreps (Kafka co-creator, with Neha Narkhede and Jun Rao; the article itself says only 'We built Kafka')
**Date**: 2014-07-02
**URL**: https://www.oreilly.com/radar/questioning-the-lambda-architecture/
**Evidence Level**: B (Foundational thought leadership) — re-tiered from A 2026-08-19: not peer-reviewed research and not an official standard
**Relevance**:
- Book ch02 §2.2 + Appendix D [was: Chapter 2] (Data Engineering Foundation)
- Book ch02 §2.2 (components: collection and pipeline) [was: Chapter 7] (Ingestion patterns)
- Best Practices Doc footnotes [^17], [^22]

**Key Findings**:
- Kappa architecture proposal (stream-only)
- Lambda complexity criticism
- Unified processing advantages

**Citations**: ch02 §2.2 + Appendix D [was: Chapter 2] Lambda vs Kappa, ch02 §2.2 (components: collection and pipeline) [was: Chapter 7] architecture patterns
**Notes**: **FOUNDATIONAL SOURCE** - Widely cited, shaped industry thinking

**Validation Status**: ✅ Active URL, O'Reilly publication · Refresh (2026-11-23): re-read at the primary. The Kappa proposal and the two-code-paths critique are as stated.

---

#### Uber - Real-Time Analytics Platform (Kafka/Flink/Pinot)

**Authors**: Uber Engineering (Confluent Current 2025 session)
**Date**: 2025 (Confluent Current 2025; re-verified 2026-06-05)
**URL**: https://current.confluent.io/post-conference-videos-2025/inside-ubers-large-scale-real-time-analytics-platform-bng25
**Evidence Level**: B (Production platform, public conference talk with specific scale figures) — re-tiered from A 2026-08-19: not peer-reviewed research and not an official standard
**Relevance**:
- Book ch02 §2.2 (components: collection and pipeline) [was: Chapter 7] (Ingestion) — streaming-at-scale example (general analytics, not security-specific)
- Best Practices Doc footnote [^19]

**Key Findings**:
- Serves "up to 10s of thousands of queries/sec, several million writes/sec and host up to tens of Petabytes of Pinot datasets" (page verbatim)
- Processes trillions of messages and dozens of PB daily via Kafka + Flink (NOT on the cited page — sourced to InfoQ's Mar 2026 IngestionNext coverage; cite InfoQ for this figure)
- **IngestionNext**: streaming-first data-lake ingestion on Kafka + Flink + Apache Hudi; latency hours→minutes, ~25% less compute (corroborated by InfoQ, Mar 2026)
- **AthenaX**: Uber's SQL-based transformation layer on Flink (page verbatim: "AthenaX(SQL based transformation on Flink)" — the entry formerly said "FlinkSQL", corrected 2026-07-10)
- Data Streaming Award: not shown on the cited session page (the site's award section is elsewhere); treat as unverified at this URL

**Citations**: ch02 §2.2 (components: collection and pipeline) [was: Chapter 7] streaming architecture at extreme scale
**Notes**: The original eng.uber.com "real-time security analytics with Flink" URL is dead (not carried in the eng.uber.com→uber.com/blog migration, no Wayback snapshot 2026-06-05), and its security-specific framing was never independently verifiable. Re-pointed to the live Confluent Current 2025 session, which supports the scale figures but describes Uber's **general** real-time analytics platform (EVA), not a security deployment. Cite as a streaming-at-scale example, not a security case study. Correction (2026-07-10, part-2 sweep fix 7): qps/writes/PB figures verified verbatim at the page; trillions/dozens-PB re-attributed to InfoQ; AthenaX naming fixed; award claim de-anchored from this URL.

**Validation Status**: ✅ Verified at primary 2026-07-10 (page no longer 403s automated fetch — stale note dropped)
**Validation (2026-06-05, folded)**: dead security URL retired, re-pointed to verified general-analytics source, security framing removed; provenance in RESEARCH-JOURNAL.md.

---

#### Disney+ Hotstar - Kafka/Flink Streaming at Scale

**Authors**: Kai Waehner (citing Disney+ Hotstar, Kafka Summit 2021)
**Date**: 2025 (Kai Waehner blog, Feb 2025; underlying figures from Kafka Summit 2021; re-verified 2026-06-05)
**URL**: https://www.kai-waehner.de/blog/2025/02/28/data-streaming-with-apache-kafka-and-flink-in-the-media-industry-disney-hotstar-and-jiocinema/
**Evidence Level**: B (Vendor-aligned expert secondary source citing a Kafka Summit production talk)
**Relevance**:
- Book ch02 §2.2 (components: collection and pipeline) [was: Chapter 7] (Ingestion) — streaming-at-scale example (general media pipeline; PII handling is the security-adjacent angle)
- Best Practices Doc footnote [^20]

**Key Findings**:
- Disney+ Hotstar: ~15 Kafka Connect clusters, 2,000+ connectors, auto-scaling on traffic
- Handles millions of messages/sec; scaled to tens of millions of concurrent viewers (IPL seasons)
- Single Message Transforms (SMT) used for PII masking/filtering, sampling, and schema validation/enforcement

**Citations**: ch02 §2.2 (components: collection and pipeline) [was: Chapter 7] streaming ingestion + PII-handling patterns
**Notes**: The original Disney Streaming "scalable real-time security analytics" Medium article 403s and its security-analytics claims were never independently verifiable — retired. Re-pointed to Kai Waehner's Disney+ Hotstar/JioCinema case study (Feb 2025), which is a **general media streaming** pipeline, not a security deployment; the PII-masking-via-SMT detail is the only security-adjacent element. Re-tiered A→B: this is a Confluent-aligned expert's secondary write-up of a 2021 conference talk, not a primary production-security source.

**Validation Status**: ✅ Re-verified 2026-06-05 — live source confirms the Hotstar figures (WebSearch; page 403s automated fetch)
**Validation (2026-06-05, folded)**: dead security URL retired, re-pointed + reframed to the verified general-streaming source, re-tiered A→B; provenance in RESEARCH-JOURNAL.md.

---

#### McAfee Cybersecurity Streaming Evolution - Kai Waehner

**Authors**: Kai Waehner
**Date**: January 2025
**URL**: https://www.kai-waehner.de/blog/2025/01/27/the-role-of-data-streaming-in-mcafees-cybersecurity-evolution/
**Evidence Level**: C (Vendor architecture, industry expert) — re-tiered from A 2026-08-19: not peer-reviewed research and not an official standard
**Relevance**:
- Book ch02 §2.2 (components: collection and pipeline) [was: Chapter 7] (Ingestion)
- Best Practices Doc footnote [^1]

**Key Findings**:
- Real-time processing essential for threat neutralization
- Industry shift toward streaming security analytics

**Citations**: ch02 §2.2 (components: collection and pipeline) [was: Chapter 7] introduction - industry trends
**Notes**: Kai Waehner = authoritative voice in streaming

**Validation Status**: ✅ Active URL, recent (2025)

---

#### Top Trends for Data Streaming 2025 - Kai Waehner

**Authors**: Kai Waehner
**Date**: December 2024
**URL**: https://www.kai-waehner.de/blog/2024/12/02/top-trends-for-data-streaming-with-apache-kafka-and-flink-in-2025/
**Evidence Level**: B (Expert analysis, trends)
**Relevance**:
- Book ch02 §2.2 (components: collection and pipeline) [was: Chapter 7] (Emerging patterns)
- Best Practices Doc footnote [^16]

**Key Findings**:
- 2025 streaming trends
- Kafka and Flink evolution

**Citations**: ch02 §2.2 (components: collection and pipeline) [was: Chapter 7] trends section
**Notes**: Forward-looking, expert perspective

**Validation Status**: ✅ Active URL
**Refresh (2026-11-23)**: superseded by the 2026 edition, *Top Trends for Data Streaming with Apache Kafka and Flink in 2026* (Waehner, 2025-12-10, https://www.kai-waehner.de/blog/2025/12/10/top-trends-for-data-streaming-with-apache-kafka-and-flink-in-2026/), which gives "the six most important trends shaping the streaming space in 2026", among them "Diskless Kafka and Apache Iceberg Create a New Storage Foundation" and "Real-Time Analytics Becomes Part of the Streaming Layer". Cite the 2026 post for current trends and this one as the 2025 snapshot.

---

## Security-Specific Data

### Data Volume & Characteristics

### Cost Comparisons

#### AWS Storage Optimization Whitepaper

**Authors**: AWS
**Date**: 2024
**URL**: https://docs.aws.amazon.com/whitepapers/latest/cost-optimization-storage-optimization/cost-optimization-storage-optimization.pdf (serves an official "DEPRECATED" stub as of 2026-07-10)
**Alt URL**: https://aws.amazon.com/whitepapers (current Whitepapers & Guides index, per the stub's own redirect notice); tier figures live at https://aws.amazon.com/s3/storage-classes/intelligent-tiering/ (see the standalone "AWS Storage Optimization - Tiered Storage" entry)
**Evidence Level**: B for what the tiers do; C with vendor bias flagged for the savings percentages, per the 2026-11-03 vendor-documentation ruling (cited PDF deprecated, tier figures sourced from the S3 Intelligent-Tiering page)
**Relevance**:
- Hypothesis H1-COST-08 (SIEM vs storage costs)
- Book ch02 §2.3 (economics) [was: Chapter 1] (Cost comparisons)
- Best Practices Doc footnote [^15]

**Key Findings**:
- S3 tiered storage cost savings (from AWS S3 Intelligent-Tiering documentation): up to 40% with Infrequent Access tier, up to 68% with Archive Instant Access tier, up to 95% with Deep Archive tier (the page gives 71% for the opt-in Archive Access tier; added 2026-11-23)
- Storage cost optimization patterns depend on access frequency and tier selection

**Citations**: ch02 §2.3 (economics) [was: Chapter 1] cost section, H1-COST-08 validation
**Notes**: Original PDF (cited URL) is a deprecated stub; tier-specific savings figures are from the AWS S3 Intelligent-Tiering product page. Cite individual tiers with "up to" language rather than a single average.

**Validation Status**: ⚠️ Cited PDF is a deprecated 4-page stub (re-checked 2026-11-23; it now redirects to the docs.aws.amazon.com/pdfs/ path). Tier figures were re-verified verbatim on the S3 Intelligent-Tiering page on 2026-11-23. This entry duplicates 'AWS Storage Optimization - Tiered Storage' and is a candidate to merge into it.

**Validation (2026-06-05, folded)**: corrections applied to findings/tier above; provenance in RESEARCH-JOURNAL.md.
---

## Implementation & Organizational

### Change Management

#### The Data-Centric Revolution + Incremental Stealth Legacy Modernization (Dave McComb)

**Authors**: Dave McComb (President / co-founder, Semantic Arts)
**Date**: 2019 (*The Data-Centric Revolution*, Technics Publications); "Incremental Stealth Legacy Modernization" (TDAN.com column, published 2022-03-02 / Semantic Arts method)
**URL**: https://technicspub.com/software_wasteland/ (Technics Publications page for *Software Wasteland* + *The Data-Centric Revolution*)
**Alt URL**: https://web.archive.org/web/20240301150721/https://tdan.com/the-data-centric-revolution-incremental-stealth-legacy-modernization/29181 [Archived] (the original TDAN.com column, "The Data-Centric Revolution: Incremental Stealth Legacy Modernization" by Dave McComb, published March 2, 2022, read at the Wayback Machine's 2024-03-01 snapshot on 2026-11-23, where the "no one is going to get the green light to take this on directly" sentence quoted below appears verbatim; re-pointed 2026-11-23). *Correction, 2026-11-23: the dataversity.net address this line carried from 2026-07-16 still returns HTTP 404, and the 2026-11-17 finding that the Wayback Machine holds no snapshot is true for that address only, because the original tdan.com address has snapshots from 2022 through 2024.*
**Evidence Level**: B (Authoritative practitioner; conceptual framing, not a quantitative source)
**Relevance**:
- Book ch07 §7.2-7.3 + Appendix K [was: Chapter 4] (Implementation journeys — migrating off a legacy SIEM one workload at a time)
- Grounds the bridge's two *relief* moves: **compose, don't build** (the single canonical, extensible, data-centric model — data as the durable, reusable, interoperable asset rather than application-centric silos) and **incremental, not big-bang** (the stealth-modernization method: fix the broken pieces, no rip-and-replace, no green-light megaproject)

**Key Findings**:
- **Single extensible data model / data-centric architecture**: data as the durable asset the applications come and go around — the principle behind composing maintained open-standard parts (Iceberg, Arrow, OCSF) instead of building a stack from scratch or buying one vendor's monolith
- **Incremental Stealth Legacy Modernization**: a deliberately safe, gradual path — move some data first, prove it, then move more data and functionality — created precisely because "no one is going to get the green light to take this on directly"; the SIEM parallel is that the legacy keeps running while the lakehouse takes the workloads it wins
- Application-centric sprawl (*Software Wasteland*, 2018) as the failure mode the data-centric model is meant to avoid

**Citations**: The bridge relief moves (compose-don't-build, incremental-not-big-bang); the migration-as-a-sequence framing in the origin narrative and the Subsurface talk
**Notes**: Framing/conceptual anchor for the applied-bridge positioning (securitydataworks.com/thesis). Carries no headline statistic — catalogued for the method and the data-centric model, not a number, so it is not exposed to the stat-mismatch audit. McComb has authored *The Data-Centric Revolution*, *Software Wasteland*, and *Semantics in Business Systems*; Semantic Arts has been Data-Centric-focused since 2000.

**Validation Status**: ✅ Verified 2026-06-09 (WebSearch: McComb authorship of the three books confirmed; "Incremental Stealth Legacy Modernization" confirmed as a TDAN.com column and a named Semantic Arts method). · Re-verified 2026-11-23: the TDAN column (Dave McComb, March 2, 2022) was read at the Wayback 2024-03-01 snapshot with the 'green light' sentence verbatim, and the Technics Publications page is live selling the McComb duology.

---

#### Prosci Change Management Best Practices (12th Edition)

**Authors**: Prosci
**Date**: 2023 (12th Edition; executive summary '© 2023', and Prosci's own 2026 materials cite it as 'Prosci, 2023'; corrected 2026-11-23)
**URL**: https://www.prosci.com/blog/change-management-best-practices
**Alt URL**: https://prosci.com/hubfs/Website_English/2.downloads/webinars/EN-EUR%20Webinar/Best-Practices-in-Change-Management-12th-Edition-Executive-Summary.pdf (12th Edition executive summary, © 2023); https://www.prosci.com/hubfs/Website_English/2.downloads/webinars/Prosci-BPCM-12th-Edition-Highlights-and-Insights-slides-2023.pdf (Highlights slides)
**Evidence Level**: C (Industry standard framework, research-based) — re-tiered from A 2026-08-19: not peer-reviewed research and not an official standard
**Relevance**:
- Book ch07 §7.2-7.3 + Appendix K [was: Chapter 4] (Implementation journeys)
- Best Practices Doc footnote [^13]

**Key Findings**:
- **Effectiveness**: Prosci's Feb 2026 PDF, Can You Afford for Your Change to Fail?, says projects with poor change management 'meet success targets only 15% of the time' and those with excellent change management 'achieve success 93% of the time', citing the 12th Edition. The 12th Edition executive summary's own chart of respondents who met or exceeded project objectives gives 88% (excellent), 73% (good), 39% (fair) and 13% (poor). The two pairs come from Prosci documents citing the same edition and were not reconciled on 2026-11-23, so cite whichever document you quote and prefer the executive summary. *(Re-sourced 2026-11-23; neither pair is on the cited blog page.)*
- 7× more likely to meet objectives with excellent versus poor change management (12th Edition executive summary, 'Excellent Change Management Drives 7X Success'; U.S. subset 8X)
- **2024 Trends**: AI technology, digital transformation, regulatory compliance, talent retention *(Not found 2026-11-23 on the cited page, in the 12th Edition executive summary or in the Highlights slides.)*
- ~~183% increase in pace of change over last four years~~ *(Withdrawn 2026-11-23: not found in the cited page, the 12th Edition executive summary, the Highlights slides or Prosci's Feb 2026 PDF; the figure appears verbatim in Accenture's Pulse of Change 2024 Index release, 2024-01-12, https://newsroom.accenture.com/news/2024/businesses-anticipate-unprecedented-rate-of-change-in-2024-new-accenture-pulse-of-change-index-shows.)*
- **Sponsorship**: Active and visible sponsorship is top contributor to success
- **Notable shift**: Change management office now most commonly located in PMO (vs HR previously) *(Verified 2026-11-23 in Prosci's 12th Edition Highlights and Insights slides, 2023: 'The PMO replaced HR as the most common location of the Change Management Office'.)*
- The "30/60/80% adoption pattern" formerly listed here does not match Prosci's published figures (their correlation data runs 13/39/73/88% meeting objectives by change-management effectiveness) — removed 2026-07-09

**Citations**: ch07 §7.2-7.3 + Appendix K [was: Chapter 4] organizational readiness, implementation best practices
**Notes**: Industry-standard change management source, 12th edition reflects latest research

**Validation Status**: ✅ Active (page updated 2026-11-04) · Refresh (2026-11-23): edition year corrected to 2023, 93%/15% re-sourced to Prosci's Feb 2026 PDF alongside the executive summary's 88%/13%, 7× and the PMO shift verified, 183% withdrawn and traced to Accenture, and the 2024 Trends bullet labelled not found.

---

#### 2024-2025 State of DevOps Report - DORA

**Authors**: DevOps Research and Assessment (DORA) / Google Cloud
**Date**: 2024-2025 (10th anniversary 2024 + inaugural AI report 2025)
**URL**: https://dora.dev/research/2024/dora-report/
**Evidence Level**: B (Industry research, 39,000+ professionals surveyed) — re-tiered from A 2026-08-19: not peer-reviewed research and not an official standard
**Relevance**:
- Book ch07 §7.2-7.3 + Appendix K [was: Chapter 4] (Implementation challenges)
- Best Practices Doc footnotes [^31], [^33], [^43]

**Key Findings**:
- **2024 Report** (39,000+ professionals): *(Unverified 2026-11-17: the report's landing page carries no report text, and the report PDF, which gives the respondent count, was not read.)*
  - AI significantly impacting software development
  - Platform engineering promises and challenges
  - Transformational leadership linked to high-performance teams
- **2025 Report** (State of AI-Assisted Software Development):
  - AI boosts individual productivity but slightly reduces overall software delivery performance
  - AI adoption linked to higher throughput but increased instability
  - Seven team archetypes replace traditional performance rankings
  - Value stream management critical for AI-driven productivity gains

**Citations**: ch07 §7.2-7.3 + Appendix K [was: Chapter 4] organizational readiness, ch02 §2.2 (components: collection and pipeline) [was: Chapter 7] operational realities, AI/ML integration patterns
**Notes**: **CRITICAL SOURCE** - Annual large-scale practitioner survey; DORA does not study streaming-vs-batch operational ratios; do not use this source for staffing or incident-rate comparisons between architecture types.

**Validation Status**: ✅ Active (verified Feb 2026), annual authoritative report · ⚠️ 1 figure unverified 2026-11-17, see the dated label

**Validation (2026-06-05, folded)**: corrections applied to findings/tier above; provenance in RESEARCH-JOURNAL.md.
---

## Survey & Industry Reports

#### Confluent Data Streaming Report (2025)

**Authors**: Confluent (with Freeform Dynamics, Radma Research)
**Date**: 2025 (May 2025 report, updated February 2026)
**URL**: https://www.confluent.io/resources/report/2025-data-streaming-report/
**Alt URL**: https://report.confluent.io/
**Evidence Level**: B (Vendor survey, 4,175 IT leaders, 12 countries)
**Relevance**:
- Book ch02 §2.2 (components: collection and pipeline) [was: Chapter 7] (Industry trends)
- RQ13: Pipeline vs query detection economics
- Best Practices Doc footnotes [^18], [^23]

**Key Findings**:
- 86% of IT leaders prioritize data streaming investments (2025)
- 89% see DSPs easing AI adoption via data access/quality/governance
- 90% plan to increase DSP investments in 2025
- **44% report 5× returns** on data streaming investments
- **93%** cite 4+ benefits of shift-left approach (detect/enrich earlier in pipeline) *(Unverified 2026-11-17: not on the report's landing pages; the full report sits behind a registration form and was not read.)*
- **25%** now at Level 1 maturity (up from 8% in 2024 — 3× growth)
- Real-time data essential for competitive edge

**Citations**: ch02 §2.3 (economics) [was: Chapter 7] industry validation, RQ13 pipeline economics
**Notes**: Vendor survey but comprehensive scope; 44% reporting 5× ROI strengthens pipeline-first economics; shift-left aligns with RQ13 pipeline detection hypothesis

**Validation Status**: ✅ Refreshed February 2026 - 2025 report · ⚠️ 2 figures unverified 2026-11-17 (the 93% and its 4+, corrected 2026-11-22), see the dated label

---

#### Databricks State of Data + AI 2024

**Authors**: Databricks
**Date**: 2024
**URL**: https://web.archive.org/web/20250122143448/https://www.databricks.com/resources/ebook/state-of-data-ai (archived snapshot of the 2024 report page — the live URL now serves Databricks' 2026 "State of AI Agents" report instead)
**Alt URL**: https://www.databricks.com/sites/default/files/2024-06/state-of-data-ai-report.pdf (full 2024 report, ungated, 36 pp, verified 2026-11-23)
**Evidence Level**: B (vendor first-party platform usage data from 10,000+ Databricks customers, Feb 2023 to Mar 2024, not a survey; vendor bias flagged for any generalisation beyond Databricks customers)
**Relevance**:
- Book ch02 §2.2 (components: collection and pipeline) [was: Chapter 7] (AI/ML adoption context; the report carries no Flink or streaming data, checked 2026-11-23)
- Best Practices Doc footnote [^24]

**Key Findings**:
- AI models in production: 11x growth year-over-year — archive-verified verbatim ("Why 11x more AI models were put into production year over year")
- RAG direction confirmed; the 377% figure is year-over-year growth in the number of customers using vector databases (printed pp. 21 and 23 of the report), not RAG adoption itself (narrowed 2026-11-23)
- 76% of companies using LLMs choose open source models, often alongside proprietary ones; Financial Services has the highest GPU growth, 88% over six months (both verified in the full report 2026-11-23)
- Customer base (usage data, not survey respondents): "more than 10,000 companies — now including over 300 of the Fortune 500" (archived page verbatim)

**Citations**: ch02 §2.2 (components: collection and pipeline) [was: Chapter 7] technology adoption trends, AI/ML integration patterns
**Notes**: Correction (2026-07-10, part-2 sweep fix 3): the live URL was silently repurposed for the 2026 State of AI Agents report (published 2026-01-09), orphaning all four cited figures; re-sourced to the Jan-2025 archive.org snapshot of the 2024 page rather than retiring the entry. Only 11x and the survey base verify verbatim at the snapshot; the other three figures live inside the gated ebook. Refresh (2026-11-23): the full report PDF is public at the Alt URL, so all four figures now verify at the primary.

**Validation Status**: ✅ All four figures verified 2026-11-23 against the full 2024 report PDF; 377% narrowed to vector-database growth; the live landing URL still serves the 2026 State of AI Agents report

---

## Streaming and Storage Sources (Additional)

*The October 2025 extraction summary that used to open this section is archived verbatim at [archive/bibliography-extraction-log-2025-10.md](archive/bibliography-extraction-log-2025-10.md).*


#### LinkedIn Security - Kafka Streams State Management

**Authors**: LinkedIn Engineering / Confluent
**Date**: 2023 (updated February 2026)
**URL**: https://www.linkedin.com/blog/engineering/infrastructure/introducing-northguard-and-xinfra
**Evidence Level**: B (Production deployment at scale) — re-tiered from A 2026-08-19: not peer-reviewed research and not an official standard
**Relevance**:
- Book ch02 §2.2 (components: collection and pipeline) [was: Chapter 7] (Ingestion - streaming)
- Best Practices Doc footnote [^68]

**Key Findings**:
- **2025 update (Northguard blog)**: LinkedIn processes 32 trillion records/day, 17 PB/day across 400K topics, 10K+ machines, 150 clusters
- Northguard replaces Kafka at hyper-scale: sharded data/metadata, log striping, self-balancing clusters
- Original Kafka Streams state management patterns remain valid for typical enterprise scale

**Citations**: ch02 §2.2 (components: collection and pipeline) [was: Chapter 7] Kafka Streams for security
**Notes**: **CRITICAL** - URL re-sourced to LinkedIn Northguard blog; Northguard is general infrastructure (not a security-specific deployment). Scale figures (32T records/day, 17 PB/day) are verbatim from the Northguard post. The former "terabytes of state with millisecond access" key finding is not in the post and was removed 2026-07-09 — for LinkedIn stateful-processing scale, cite the Samza VLDB 2017 entry instead. For Kafka-Streams stateful mechanics, use Confluent course as secondary cite only.

**Validation Status**: ✅ Refreshed February 2026

**Validation (2026-06-05, folded)**: corrections applied to findings/tier above; provenance in RESEARCH-JOURNAL.md.
---

#### AWS S3 Storage-Class Pricing — First-Party Tier-Delta Derivation (2026-07-09)

**Authors**: AWS (list prices) / Jeremy Wiley (derivation) — FIRST-PARTY derivation from public vendor pricing
**Date**: 2026-07-09 (prices fetched live from the page's US East (N. Virginia) tab)
**URL**: https://aws.amazon.com/s3/pricing/
**Evidence Level**: B (public list prices, verbatim-quoted; the derivation is arithmetic on them)
**Relevance**:
- Hypothesis H-COST-09 (tiered-storage economics — restoration-path evidence per working/proposals/RESCORE-PROPOSAL-2026-07.md)
- Manuscript §3.3.2

**Key Findings** (list prices verified verbatim 2026-07-09; per GB-month, US-East-1):
- S3 Standard (first 50 TB): $0.023 · Standard-IA: $0.0125 (−45.7% vs Standard) · Glacier Instant Retrieval: $0.004 (−82.6%) · Glacier Flexible Retrieval: $0.0036 (−84.3%) · Glacier Deep Archive: $0.00099 (−95.7%)
- Bounds, not TCO: IA/Glacier tiers carry retrieval fees, minimum-storage-duration, and minimum-object-size charges (footnoted on the page) that reduce effective savings; Standard also steps down at volume ($0.022 next 450 TB, $0.021 over 500 TB)

**Citations**: §3.3.2 Storage Tier Economics; H-COST-09 restoration evidence
**Notes**: Added 2026-07-09 executing the re-score's restoration path — replaces nothing; it is the first quantified, verifiable leg under the tiered-storage savings claim since the 2026-06 withdrawal. Prices drift; re-fetch before citing in a submission.

**Validation Status**: ✅ Prices fetched live and quoted verbatim 2026-07-09
**Refresh (2026-11-23)**: re-read from the AWS Price List API, because the pricing page renders its table in the browser and a text fetch returns no values: offer `AmazonS3`, region us-east-1, publicationDate 2026-11-21T17:29:19Z (https://pricing.us-east-1.amazonaws.com/offers/v1.0/aws/AmazonS3/current/us-east-1/index.json), and offer `AmazonS3GlacierDeepArchive`, publicationDate 2026-11-20T17:41:33Z, for the Deep Archive storage line. Every price above is unchanged (Standard $0.023, $0.022 and $0.021 per GB-month across the three volume steps; Standard-IA $0.0125; Glacier Instant Retrieval $0.004; Glacier Flexible Retrieval $0.0036; Glacier Deep Archive $0.00099), and the deltas recompute to the same -45.7%, -82.6%, -84.3% and -95.7%.

---

#### Samza - Stateful Scalable Stream Processing at LinkedIn (VLDB 2017)

**Authors**: Shadi A. Noghabi, Kartik Paramasivam, Yi Pan, Navina Ramesh, Jon Bringhurst, Indranil Gupta, Roy H. Campbell (UIUC + LinkedIn)
**Date**: 2017 (PVLDB Vol. 10, No. 12, pp. 1634-1645)
**URL**: https://www.vldb.org/pvldb/vol10/p1634-noghabi.pdf
**Evidence Level**: A (Peer-reviewed VLDB paper with LinkedIn production data)
**Relevance**:
- Hypothesis H-STREAM-01 (stateful stream processing at scale)
- Book ch02 §2.2 (components: collection and pipeline) [was: Chapter 7] (Ingestion - streaming)

**Key Findings**:
- Partitioned local state + low-overhead changelog "allowing it to scale to massive state sizes (hundreds of TB) per application" (abstract, verified verbatim 2026-07-09)
- "When using local state we perform millions of requests/s" (§6 evaluation, verified verbatim 2026-07-09)
- Host Affinity makes recovery time near-constant independent of state size
- LinkedIn production deployment: "100s of TB total data" across "more than 200 applications on over 10,000 containers processing Trillions of events per day" (§1, verified verbatim 2026-11-23; the former "200+ machines" misread applications as machines)

**Citations**: H-STREAM-01 validation; manuscript §3.2.3/3.5/3.6/4.2
**Notes**: Added 2026-07-09 to replace the orphaned "LinkedIn Kafka Streams: terabytes of state with millisecond access" claim — LinkedIn's stream processor is Samza (Kafka-backed changelog + local RocksDB state, same design family as Kafka Streams), and these are the verified figures. Do not cite a millisecond latency number to this paper; its stated local-state figure is throughput (millions of requests/s).
**Refresh (2026-11-23)**: PDF re-read (HTTP 200); the scale, throughput and Host Affinity findings are unchanged and verbatim, and the deployment bullet is corrected to the paper wording. No superseding paper from the same authors was found. Apache Samza 1.8.0 (announced 2023-01-17 on samza.apache.org) is the latest release listed on the project site and the project is not in the Apache Attic, so the paper stays the reference for the changelog-plus-local-state design rather than for current LinkedIn practice.

**Validation Status**: ✅ Added + verified against the PDF 2026-07-09

---

#### Netflix - Kafka Tiered Storage

**Authors**: Netflix Technology Blog
**Date**: 2023 (updated February 2026)
**URL**: https://docs.confluent.io/platform/current/kafka/tiered-storage.html
**Evidence Level**: B (Confluent vendor docs for tiered-storage; Netflix scale figure requires Netflix Keystone blog as primary cite)
**Relevance**:
- Hypothesis H1-COST-08 (cost optimization)
- Book ch02 §2.2 (components: collection and pipeline) [was: Chapter 7] (Ingestion)
- Best Practices Doc footnote [^70]

**Key Findings**:
- Netflix Keystone: "More than 700 billion messages are ingested on an average day" (Keystone post, 2016, netflixtechblog.com/kafka-inside-keystone-pipeline-dd5aeabaf6bb, read 2026-11-23 at the archived copy https://web.archive.org/web/20250119164347/https://netflixtechblog.com/kafka-inside-keystone-pipeline-dd5aeabaf6bb) *(Corrected 2026-11-23: this line formerly gave 2 trillion messages/day, a figure that is not in the Keystone post, where the word "trillion" does not appear.)*
- Security data retention optimization via tiered storage
- **2025 update**: Kafka tiered storage marked production-ready in Apache Kafka 3.9.0 (cite Apache release notes, not Confluent docs)
- Tiered storage enables indefinite retention at minimal cost for compliance use cases

**Citations**: ch02 §2.3 (economics) [was: Chapter 1] cost comparisons, ch02 §2.3 (economics) [was: Chapter 7] tiered storage
**Notes**: **CRITICAL** - Validates scale and retention feasibility. Cost-reduction percentages (70-80%, 90%+) are not Netflix-published and should not be cited. Use Apache Kafka 3.9.0 release notes for GA tiered-storage claim.

**Validation Status**: ✅ Refreshed February 2026 - Kafka 3.9.0 production-ready · the former 2 trillion figure, labelled unverified on 2026-11-22, was replaced on 2026-11-23 by the Keystone post's own figure, see the dated note
**Currency (2026-11-17)**: Apache Kafka has moved to the 4.x line (the newest release tag in apache/kafka is 4.4.0); the tiered-storage GA statement for 3.9.0 still stands as history, and current behaviour should be cited from the 4.x documentation at https://kafka.apache.org/documentation/.

**Validation (2026-06-05, folded)**: corrections applied to findings/tier above; provenance in RESEARCH-JOURNAL.md.
---

## Performance Benchmarks (Additional)

### ClickHouse Performance (Additional Sources)

#### ClickHouse - Vectorized Query Execution

**Authors**: ClickHouse Engineering Blog
**Date**: 2023-2026 (continuously updated documentation)
**URL**: https://clickhouse.com/docs/concepts/why-clickhouse-is-so-fast
**Evidence Level**: B (Vendor technical documentation — conceptual page, no throughput benchmarks disclosed)
**Relevance**:
- Hypothesis H3-PERFORMANCE-01
- Book ch05 §5.3 + Appendix I [was: Chapter 9] (Query Engines - ClickHouse)
- Best Practices Doc footnote [^99]

**Key Findings**:
- Vectorized execution model processes data in CPU cache-sized batches
- SIMD-level parallelism for columnar data processing
- Automatic SIMD instruction set selection based on hardware capabilities

**Citations**: ch05 §5.3 + Appendix I [was: Chapter 9] ClickHouse architecture
**Notes**: Conceptual architecture explanation; cited page does not publish throughput numbers or comparative multipliers. Do not cite specific CPU-efficiency multipliers, rows/sec, or PostgreSQL comparison figures from this source.

**Validation Status**: ✅ Active URL (refreshed January 2026)

**Validation (2026-06-05, folded)**: corrections applied to findings/tier above; provenance in RESEARCH-JOURNAL.md.
---

#### ClickHouse - IP Address Types Performance

**Authors**: ClickHouse documentation
**Date**: 2024-2026 (continuously updated)
**URL**: https://clickhouse.com/docs/reference/data-types/ipv6
**Evidence Level**: B (Vendor documentation; qualitative storage-efficiency claim only — no benchmarked multiplier in source)
**Relevance**:
- Book ch05 §5.3 + Appendix I [was: Chapter 9] (ClickHouse security use cases)
- Best Practices Doc footnote [^101]

**Key Findings**:
- Native IPv4/IPv6 fixed-width types (16-byte UInt128 for IPv6) are storage-efficient vs string representations (qualitative advantage for CIDR-based threat hunting)

**Citations**: ch05 §5.3 + Appendix I [was: Chapter 9] security-specific optimizations
**Notes**: Documentation confirms native IP type support; no throughput or speed multiplier is published on this page. Do not cite a specific CIDR-query speedup factor from this source.
**Refresh (2026-11-23)**: the docs moved from /docs/sql-reference/ to /docs/reference/ (the old path redirects here, HTTP 308); the page still reads "Stored in 16 bytes as UInt128 big-endian" and still publishes no performance figure. Evidence Level stays B for what the type does, per the 2026-11-03 vendor-documentation ruling.

**Validation Status**: ✅ Active URL

**Validation (2026-06-05, folded)**: corrections applied to findings/tier above; provenance in RESEARCH-JOURNAL.md.
---

#### Retired December 2025 multi-engine benchmark (superseded by SDW Lab zeek-flagship-rerun)

**Authors**: Jeremy Wiley
**Date**: December 2025
**URL**: https://github.com/flying-coyote/sdw-lab-benchmarks/tree/master/zeek-flagship-rerun (the public successor)
**Note (2026-11-17)**: the December 2025 benchmark ran from a private repository that was never published, so the URL above points at the public re-run that supersedes it, and the entry was retitled without the retired benchmark's name.
**Evidence Level**: B (retired first-party lab benchmark; cite the successor) — re-tiered from A 2026-08-19: not peer-reviewed research and not an official standard
**Relevance**:
- Hypothesis H3-PERFORMANCE-01 (ClickHouse OLAP performance; its framing after the 2026-06-14 supersession is under review)
- Hypothesis H3-PERFORMANCE-02 (StarRocks vs Dremio comparison)
- Hypothesis H3-PERFORMANCE-03 (compression optimization; see the compression line in Key Findings)
- Hypothesis H-ARCH-02 (Multi-engine Iceberg validation)
- Book ch05 §5.3 + Appendix I [was: Chapter 8] (Query Engine Selection)

**Key Findings** (rewritten 2026-11-17; the December 2025 timings are retired and are not reproduced here):
- This is a retired December 2025 benchmark, kept as a dated record. Its named-vendor timings and the multiples derived from them were withdrawn from the handbook appendix on 2026-07-11 and from this entry on 2026-11-17 under the vendor's licence terms that bar publishing benchmark results (often called a DeWitt clause), and the private repository they came from cannot be re-derived from public material, so no figure from it should be quoted.
- Its successor is the public SDW Lab re-run on a sha256-pinned 10M-row Zeek conn corpus, which splits into two regimes by query shape rather than producing a single multiple. Across three independent draws the OpenSearch baseline runs 10.1×, 10.6× and 11.3× slower than ClickHouse over Iceberg on scan aggregation (about 10–11×), and reading Iceberg costs ClickHouse 4.6×, 4.3× and 4.2× over its native store (about 4.2–4.6×), while the absolute single-host milliseconds drift about 5–10% between draws, so the multiples are what transfer. The three draws span two OpenSearch versions, 2.18.0 for the first two and probably 3.7.0 for the third, per the lab's own 2026-11-17 correction to the band file, and the same-day 3.7.0 comparison (2.5524 s against ClickHouse over Iceberg at 0.2438 s) gives about 10.5× ([FLAGSHIP-TRIPLE-BAND-2026-06-14.md](https://github.com/flying-coyote/sdw-lab-benchmarks/blob/master/zeek-flagship-rerun/FLAGSHIP-TRIPLE-BAND-2026-06-14.md), two-regime table; Tier B, single host). The front-engine arm's results are withheld in that public repository under the vendor's benchmark-publication terms, and they are withheld here too.
- The baseline was moved from OpenSearch 2.18.0 to 3.7.0 and the clean same-draw comparison came out 1.1% faster on 3.7.0, so the multiples held on what was the current release in June 2026; OpenSearch had reached 3.9.0 by 2026-11-17 (released 2026-09-29), which has not been measured ([VERSION-CURRENCY-2026-06-14.md](https://github.com/flying-coyote/sdw-lab-benchmarks/blob/master/VERSION-CURRENCY-2026-06-14.md), "Flagship foil" section).
- Compression: the December 2025 4.6× (LZ4) and 8.2× (ZSTD-22) figures are superseded. The lab re-measured compression on its own sha256-pinned 10M-row Zeek conn corpus at 5.5× for ClickHouse MergeTree with default LZ4 (684,777,971 bytes, about 685 MB) and 9.0× for blanket ZSTD(22) (414,722,162 bytes, about 415 MB) against 374.3 raw bytes per event, and the old 8.2× traced to no lab measurement ([measured_footprints.json](https://github.com/flying-coyote/sdw-lab-benchmarks/blob/master/cost-to-serve-retention/results/measured_footprints.json), keys `ch_native_lz4` and `ch_zstd22`; [RESULTS.md](https://github.com/flying-coyote/sdw-lab-benchmarks/blob/master/cost-to-serve-retention/results/RESULTS.md), Layer 1 table; Tier B, measured 2026-06-10).

**Citations**: All 4 hypotheses, Book ch05 §5.1 (table format) [was: Ch 8]
**Notes**: A first-party multi-engine benchmark on identical OCSF data, now retired. Cite the public SDW Lab re-run above for any performance or compression figure, and quote the two-regime split with its ~10–11× baseline-to-columnar multiple and ~4.2–4.6× open-format tax rather than a single headline multiple. This entry does not change the confidence wording of H3-PERFORMANCE-01, which is under review, so read that wording alongside this entry rather than on its own.

**Validation Status**: ⚠️ Retired December 2025 benchmark; the figures above were re-read at the public SDW Lab repository on 2026-11-17 (each linked file returned 200 and carries the quoted values).

---

#### Access Path Selection in Main-Memory Optimized Data Systems: Should I Scan or Should I Probe? (Kester et al., SIGMOD 2017)

**Authors**: Michael S. Kester, Manos Athanassoulis, Stratos Idreos (Harvard DASLab)
**Date**: 2017 (ACM SIGMOD International Conference on Management of Data)
**URL**: https://stratos.seas.harvard.edu/publications/access-path-selection-main-memory-optimized-data-systems-should-i-scan-or
**Alt URL**: https://dl.acm.org/doi/abs/10.1145/3035918.3064049 (DOI 10.1145/3035918.3064049)
**Alt URL 2**: https://cs-people.bu.edu/mathan/publications/sigmod17-kester.pdf (author-hosted PDF; fetches when the Harvard and ACM pages bot-block)
**Evidence Level**: A (peer-reviewed, SIGMOD)
**Relevance**:
- The academic "why" behind the lab's two-regime / Needle result (`zeek-flagship-rerun/results/NEEDLE-FINDINGS-2026-06-14.md`): a point lookup wins on a secondary index over an unsorted store but ties a sorted columnar store, so the lakehouse point-lookup weakness is a layout choice, not a hard limit. Kester et al. is the formal version of that argument — in a main-memory column store, modern vectorized/SIMD/multi-core sequential scans have become competitive across a much wider selectivity range than the textbook assumes, yet access-path selection is still required because both paths remain useful under varying workloads.
- Book ch05 §5.3 + Appendix I [was: Chapter 9] (query engines, index-vs-scan), Appendix I (two-regime symmetry); grounds the SPEC/Matrix "where the index wins" framing.

**Key Findings**: Sequential scans in main-memory-optimized columnar systems benefit from column-group storage, vectorized execution, shared scans, operating directly over compressed data, and SIMD + multi-core execution, which together make scans the better access path in more cases than older cost models assumed; secondary-index probes still win in a region, so the optimizer must still choose between scan and probe rather than defaulting to one. **FLAG CLOSED (2026-07-10, part-2 sweep fix 40)**: the previously 403-blocked PDF now fetches, and the paper's scoped crossover reads verbatim: "the index is preferable when selectivity drops below 0.5−1%" (single-query, column-at-a-time baseline; the threshold rises to ~8% for 10-column groups and falls toward 0.4% under concurrency). The relayed "~1%" claim was directionally right but unscoped — cite the scoped figure, never a bare "~1%". Authorship/venue confirmed earlier (Harvard DASLab + dblp SIGMOD 2017 + ACM DOI); the ACM page itself was also browser-confirmed live 2026-07-10 for the Axelsson-style bot-block reason.
**Citations**: Kester, M. S., Athanassoulis, M., & Idreos, S. (2017). *Access Path Selection in Main-Memory Optimized Data Systems: Should I Scan or Should I Probe?* SIGMOD '17, 715–730. DOI 10.1145/3035918.3064049.
**Validation Status**: ✅ Authorship/title/venue/DOI verified 2026-06-14; ✅ scoped selectivity crossover (0.5–1%, ~8% for 10-column groups, ~0.4% under concurrency) verified at the now-fetchable PDF 2026-07-10 — FLAG closed.
**Refresh (2026-11-23)**: re-read at the BU-hosted PDF because the Harvard and ACM pages returned 403 to automated fetch; the scoped crossover figures (0.5 to 1%, 8% for ten-column groups, toward 0.4% under concurrency) are unchanged and verbatim. Foundational result, still accurate.

---

#### Analyzing and Comparing Lakehouse Storage Systems (LHBench, CIDR 2023)

**Authors**: Paras Jain, Peter Kraft, Conor Power, Tathagata Das, Ion Stoica, Matei Zaharia (UC Berkeley / Stanford / Databricks — full roster verified at the PDF title page 2026-07-10)
**Date**: 2023 (Conference on Innovative Data Systems Research — CIDR 2023)
**URL**: https://www.cidrdb.org/cidr2023/papers/p92-jain.pdf
**Alt URL**: https://github.com/lhbench/lhbench (benchmark code)
**Evidence Level**: A (peer-reviewed, CIDR)
**Relevance**:
- The independent academic benchmark of the three lakehouse table formats the book tracks (Iceberg / Hudi / Delta Lake), and the external grounding for "metadata processing is where the table formats actually differ" — the lab's compaction/file-count results sit inside the same regime LHBench measures.
- Book ch05 §5.1 (table format) [was: Chapter 8] (table formats), ch05 §5.1 (table format) [was: Chapter 9]; contextualizes the SDW lab's own first-party benchmarks against a published cross-format baseline.

**Key Findings**: Adapts TPC-DS to the lakehouse setting on AWS EMR across Iceberg, Hudi, and Delta Lake. Headline: Delta Lake ran ~1.4× faster than Hudi and ~1.7× faster than Iceberg on end-to-end TPC-DS queries (vendor-affiliated authorship — Databricks ships Delta, so read the cross-format ordering with that incentive in mind). The large-file-count test (the `store_sales` table split into 10MB files, 1,000→200,000 files) is the more durable contribution: it isolates metadata-processing strategy, with the paper's exact figure: Delta Lake's distributed planning "improves performance by 7–12× for a 200K file table" (p.5 §3.4 verbatim — the entry's former "~7×–20×" appears nowhere in the paper; corrected 2026-07-10). Note this is a 2023 result on the then-current format versions; Iceberg V3/1.11.0 and Hudi have moved since, so cite the *method and the metadata-is-the-differentiator finding*, not the 2023 cross-format ranking as current.
**Citations**: Jain, P., et al. (2023). *Analyzing and Comparing Lakehouse Storage Systems*. CIDR 2023. cidrdb.org/cidr2023/papers/p92-jain.pdf.
**Validation Status**: ✅ Verified at the PDF 2026-07-10 (part-2 sweep fix 8): full author roster + Stanford affiliation added; 7–12× metadata figure corrected to paper verbatim; Delta 1.4×/1.7× headline re-confirmed.
**Refresh (2026-11-23)**: PDF re-read (HTTP 200); the 1.4×, 1.7× and 7 to 12× figures are unchanged. Pin the versions when citing: Spark on AWS EMR 6.9.0 with Delta Lake 2.2.0, Hudi 0.12.0 and Iceberg 1.1.0 (Iceberg 0.14.0 for merge-on-read after S3 timeouts). No LHBench follow-up paper was found. Newer cross-format numbers measure different workloads and point different ways: the Apache Hudi blog (Narayanan, 2026-08-13, Tier C, Hudi maintainer) reports that on an upsert-heavy fact-table workload "Hudi averaged ~4x lower incremental write latency than Iceberg and ~6x lower than Delta Lake" on Hudi 1.1.1, Iceberg 1.10.0 and Delta Lake 3.3.2 with LakeLoader, so the format ordering depends on read versus write workload and on version.

---

#### LST-Bench: Benchmarking Log-Structured Tables in the Cloud (SIGMOD 2024)

**Authors**: Jesús Camacho-Rodríguez, Ashvin Agrawal, Anja Gruenheid, Ashit Gosalia, Cristian Petculescu, Josep Aguilar-Saborit, Avrilia Floratou, Carlo Curino, Raghu Ramakrishnan (Microsoft)
**Date**: 2024 (SIGMOD 2024 / Proc. ACM Manag. Data, Vol. 2, No. 1)
**URL**: https://github.com/microsoft/lst-bench
**Alt URL**: https://arxiv.org/abs/2305.01120 (technical report, v3 2024-01-19); DOI 10.1145/3639314
**Evidence Level**: A (peer-reviewed, SIGMOD; framework is Microsoft OSS)
**Relevance**:
- The complement to LHBench: a Microsoft framework + paper for benchmarking log-structured tables (Delta Lake, Apache Hudi, Apache Iceberg) with workloads that stress longevity/maintenance behavior (compaction, time-travel, concurrent writes) rather than only point-in-time TPC-DS reads — the dimension the SDW compaction-recovery and interference benches probe.
- Book ch05 §5.1 (table format) [was: Chapter 8] (table formats), ch05 §5.1 (table format) [was: Chapter 9]; second external anchor for the "the table-format choice shows up under maintenance and concurrency, not just on a cold read" argument.

**Key Findings**: A configurable framework for evaluating log-structured tables (LSTs — Delta/Hudi/Iceberg) under cloud workloads, designed to capture longevity and operational behavior (degradation over many write/compaction cycles) that single-shot benchmarks miss. Cite for the methodology and the operational-dimension framing; specific per-format numbers were not extracted at primary, so do not quote LST-Bench multipliers without reading the paper.
**Citations**: Camacho-Rodríguez, J., Agrawal, A., Gruenheid, A., Gosalia, A., Petculescu, C., Aguilar-Saborit, J., Floratou, A., Curino, C., & Ramakrishnan, R. (2024). *LST-Bench: Benchmarking Log-Structured Tables in the Cloud*. SIGMOD 2024 / Proc. ACM Manag. Data 2(1). DOI 10.1145/3639314.
**Validation Status**: ✅ Verified 2026-06-14 (microsoft/lst-bench GitHub: title/author roster/SIGMOD-2024 venue/three-format scope confirmed via fetch); specific result figures not extracted at primary.
**Refresh (2026-11-23)**: repo README (HTTP 200) and arXiv v3 re-read; venue Proc. ACM Manag. Data 2(1), DOI 10.1145/3639314, confirmed from the README BibTeX. The same team presented a follow-up at the DBTest 2024 workshop (June 2024, slides linked from the README, not read). Per-format figures are still not extracted.

---

#### ClickBench — A Benchmark for Analytical Databases (ClickHouse)

**Authors**: ClickHouse, Inc. (open community submissions)
**Date**: 2022–2026 (continuously updated)
**URL**: https://github.com/ClickHouse/ClickBench
**Evidence Level**: C (vendor-authored benchmark — ClickHouse maintains it; flag the author-incentive when citing cross-engine rankings)
**Relevance**:
- The most-cited public analytical-database benchmark and a useful methodology reference for the lab's own cold/hot discipline — but it is authored by a vendor whose engine it benchmarks, so it is a Tier-C landscape reference, not an A-tier neutral arbiter.
- Book ch05 §5.3 + Appendix I [was: Chapter 9] (query engines); contextualizes the SDW lab's choice to run its own first-party benchmark rather than rely on a vendor leaderboard.

**Key Findings**: A single-table analytical benchmark (web-analytics workload) run across many engines. Documented methodology: a cold run with OS page-cache (and, for "true cold," database caches) cleared and the database restarted before the first run of each query; a hot run taking the smaller of the 2nd/3rd run times; a "Combined" score as a weighted geometric mean (load time 10%, data size 10%, cold runtime 20%, hot runtime 60%). Cite for the cold/hot methodology and as the public-leaderboard landscape; treat the cross-engine ordering as vendor-incented (Tier C) given ClickHouse maintains the harness.
**Citations**: ClickHouse, Inc. *ClickBench: A Benchmark for Analytical Databases*. github.com/ClickHouse/ClickBench.
**Validation Status**: ✅ Verified 2026-06-14 (ClickHouse/ClickBench GitHub README: cold/hot/Combined methodology and weights confirmed).

---

#### ClickHouse - Compression Codecs Documentation

**Authors**: ClickHouse Documentation Team
**Date**: 2024-2026 (continuously updated)
**URL**: https://clickhouse.com/docs/en/sql-reference/statements/create/table#compression-codecs
**Evidence Level**: B (Vendor technical documentation; codec list confirmed, ratio figures require separate engineering-blog cite)
**Relevance**:
- Blog post: "ClickHouse Compression Reality: Vendor Claims vs Production Testing"
- Book ch05 §5.3 + Appendix I [was: Chapter 9] (Query Engines - ClickHouse)
- Compression optimization for security data

**Key Findings**:
- Supported compression codecs: LZ4, ZSTD, Delta, DoubleDelta, T64, Gorilla
- Codec selection guidance for security telemetry optimization
- For per-codec ratio ranges, cite ClickHouse's "Database compression: encodings, codecs and ratios" engineering page (LZ4 ~2-4×, ZSTD ~3-6×) — not this reference page

**Citations**: Blog compression deep-dive, ch05 §5.1 (table format) [was: Chapter 9] storage optimization
**Notes**: This page documents available codecs and syntax; it does not publish compression ratio benchmarks. Do not cite the "3-14×" range from this source.

**Validation Status**: ✅ Active (verified Feb 2026)

**Validation (2026-06-05, folded)**: corrections applied to findings/tier above; provenance in RESEARCH-JOURNAL.md.
---

#### ClickHouse - Performance Optimization Guide

**Authors**: ClickHouse Documentation Team
**Date**: 2024-2026 (continuously updated)
**URL**: https://clickhouse.com/docs/optimize/query-optimization
**Evidence Level**: B (Vendor technical documentation) — *tier note (2026-06-05): vendor product docs usually score B under the re-tier discipline (no independent benchmark on the page); flag resolved by the 2026-08-19 re-tier to B.* — re-tiered from A 2026-08-19: not peer-reviewed research and not an official standard
**Relevance**:
- Blog post: "ClickHouse Compression Reality"
- Book ch05 §5.3 + Appendix I [was: Chapter 9] (Query Engines)
- Security data performance tuning

**Key Findings**:
- Query optimization techniques (ORDER BY / primary-key selection as the highest-leverage lever)
- Index strategies for security workloads
- Partitioning and clustering best practices

**Citations**: Blog compression testing methodology, ch05 §5.3 + Appendix I [was: Chapter 9] performance tuning
**Notes**: Comprehensive performance optimization reference

**Validation Status**: ✅ Active URL · Freshness (2026-06-05): the prior URL `/docs/guides/best-practices/query-optimization` returned 404 (docs path reorganized); re-pointed to the current `/docs/optimize/query-optimization` (WebFetch-confirmed live, "A simple guide for query optimization").

---

#### How Exabeam uses ClickHouse for scalable, searchable security analytics (ClickHouse case study, 2025)

**Authors**: ClickHouse (case study of Exabeam, SIEM/UEBA vendor)
**Date**: 2025 (published Sep 11, 2025)
**URL**: https://clickhouse.com/blog/exabeam-clickhouse-security-analytics
**Evidence Level**: B (Production deployment with quantitative operational metrics; ClickHouse-published — vendor bias flagged) — re-tiered from A 2026-08-19: not peer-reviewed research and not an official standard
**Relevance**:
- Hypothesis H3-PERFORMANCE-01 (ClickHouse for security analytics)
- Research Question RQ11 (LIGER stack vs traditional SIEM — from the incumbent-SIEM side)
- Book ch05 §5.3 + Appendix I [was: Chapter 9] (Query engines — ClickHouse as SIEM backend)

**Key Findings** (verified verbatim at the primary, 2026-07-09):
- Exabeam runs its SIEM/UEBA analytics backend on ClickHouse Cloud across 10 global regions
- Peak ingest 1.2M events/sec per region; 80B+ events daily; 1T+ events retained
- 3.5 PB raw → 200 TiB after compression (about 16×; corrected 2026-11-17 from "~17.5×", which divided petabytes by tebibytes as if they were the same unit); schema reduced from 1,150+ fields to ~250 columns
- Query latency cut from 8s+ (scanning 180+ columns) to under 1s
- Ingest scaled 100K→250K events/sec on a three-node cluster; ingestor optimization cut per-pod memory 7 GB → 4 GB (the page's own "45%" caption is a slight arithmetic slip — 7→4 GB is ~43%; both figures appear on the page)

**Citations**: H3-PERFORMANCE-01 / RQ11 — an incumbent SIEM vendor running its own analytics backend on a columnar store is evidence for the columnar-store-as-SIEM-backend thesis
**Notes**: First-party ClickHouse case study (ClickHouse marketing its own product via a customer) — figures self-reported, not independently audited. All numbers verified verbatim at the primary; kept at A on production-quantitative grounds with the vendor-bias caveat stated (a strict independent-verification bar would place it at B), and re-tiered to B on 2026-08-19.

**Validation Status**: ✅ Verified 2026-07-09 (ClickHouse blog primary fetched; every figure confirmed verbatim or near-verbatim) · *Correction 2026-11-17: the derived "~17.5×" compression ratio passed that check but divided petabytes by tebibytes, and is about 16× (see Key Findings).*

---

#### Huntress - ClickHouse Migration Case Study

**Authors**: Huntress / ClickHouse
**Date**: 2024-11-19
**URL**: https://clickhouse.com/blog/how-huntress-improved-performance-and-slashed-costs-with-clickHouse
**Evidence Level**: B (Production deployment, validated metrics) — re-tiered from A 2026-08-19: not peer-reviewed research and not an official standard
**Relevance**:
- ~~Research Question RQ7 (Isolation patterns and performance)~~ *(withdrawn 2026-11-22; the post describes no isolation pattern)*
- ~~Research Question RQ8 (Compliance trade-offs)~~ *(withdrawn 2026-11-22, same reason)*
- Blog post: "Sparking an Architecture: RSA Conversations"
- Blog post: "LIGER Stack Reference Architecture"
- Book ch05 §5.3 + Appendix I [was: Chapter 9] (Query Engines - ClickHouse)
- Hypothesis H-IMPL-01 (TCO Reality)

**Key Findings**:
- Cost cut by "more than 90%" (the post's words): upwards of $70,000 a month on Elasticsearch to around $5,000 a month on ClickHouse Cloud for a comparable workload, about 93% by arithmetic (Elastic → ClickHouse migration)
- *Withdrawn 2026-11-22: the former "Iceberg data lake on isolated AWS infrastructure", "table-level RBAC" and "network isolation as primary control" findings. Re-read at the cited post on 2026-11-22, it mentions none of Iceberg, isolation, RBAC or RSA.*
- 3 million+ endpoints monitored; >1 million M365 identities managed
- Up to 200K records/sec ingest throughput
- **16 billion events/day** processed (figure from the description on the ClickHouse Huntress video page, clickhouse.com/videos/lessons-learned-building-siem-with-clickhouse, not the blog post; read there 2026-11-22)

**Citations**: Blog RSA conversations, H-IMPL-01 TCO validation
**Notes**: Production security deployment. The cited post does not describe an isolation-first design, table-level-only permissions or an RSA 2025 validation, so those claims, and the RQ7 isolation-first relevance, are withdrawn (2026-11-22). "1M EPS / 3×16-core servers" and "20-50× compression" figures are not supported by the cited blog and have been removed.

**Validation Status**: ✅ Active (verified Feb 2026); the 16 billion figure, labelled unverified on 2026-11-17, was read at the video page on 2026-11-22
**Refresh (2026-11-23)**: post re-read (HTTP 200, datePublished 2024-11-19); the cost, endpoint, identity and 200,000 records per second figures are unchanged and verbatim, and the video page still carries the 16 billion events a day. A later Huntress engineering post (Coyne, 2025-04-01, https://www.huntress.com/blog/scalable-edr-advanced-agent-analytics-with-clickhouse, Tier B, read at the 2026-07-16 Wayback snapshot because the live page returns 403 to automated fetch) confirms continued ClickHouse use at "millions of endpoints generating billions of data points per day" and says ClickHouse "can automatically take terabytes of data and compress it down to a couple of dozen gigabytes" for its EDR agent analytics data; it gives no ratio for the SIEM workload, so it does not restore the removed 20 to 50× figure.

**Validation (2026-06-05, folded)**: corrections applied to findings/tier above; provenance in RESEARCH-JOURNAL.md.
---

#### Chris Bisnett - Huntress ClickHouse Migration (Video)

**Authors**: Chris Bisnett (Huntress CTO)
**Date**: 2024
**URL**: https://www.youtube.com/watch?v=lhsWNofOcdk
**Evidence Level**: B (Production deployment presentation) — re-tiered from A 2026-08-19: not peer-reviewed research and not an official standard
**Relevance**:
- Blog post: "Sparking an Architecture: RSA Conversations"
- Hypothesis H-IMPL-01 (TCO Reality)
- Production ClickHouse validation

**Key Findings**:
- First-hand account of Elastic → ClickHouse migration
- 93% cost reduction, derived from the $70K to $5K a month the talk's description gives (92.9%), read 2026-11-22 on the ClickHouse video page that embeds this video (https://clickhouse.com/videos/lessons-learned-building-siem-with-clickhouse)
- 3M endpoint scale ("over 3 million endpoints", same page)
- Compression and performance discussion: unconfirmed (the video description gives no compression figure, and the talk was not watched or transcribed as of 2026-11-23; do not cite a compression ratio to this talk until it is)

**Citations**: Blog RSA conversations, practitioner validation
**Notes**: Video of a ClickHouse New York meetup talk by the Huntress CTO (uploaded 2024-10-02, per the ClickHouse video page) *(Corrected 2026-11-23: the former "RSA 2025 field validation" is withdrawn, because the video page describes a NY meetup talk and gives no RSA connection.)*

**Validation Status**: ✅ Active (verified Feb 2026); both figures, labelled unverified on 2026-11-17, were read at the ClickHouse video page on 2026-11-22
**Refresh (2026-11-23)**: video (HTTP 200, uploaded 2024-10-02) and the ClickHouse video page re-read; the 93% and 3 million endpoint figures are unchanged. The auto-caption track returned an empty body to automated fetch, so the compression item, and the pending Huntress 50:1 check at appendix-i line 529, still need a human viewing.

---

#### RunReveal - SIEM Built on ClickHouse + sigmalite (RunReveal evaluates Sigma at ingest)

**Authors**: RunReveal / ClickHouse
**Date**: 2024 (verified live 2026-07-08)
**URL**: https://clickhouse.com/blog/clickhouse-cloud-runreveal (ClickHouse's security team as customer); https://github.com/runreveal/sigmalite (Apache-2.0 Sigma execution engine); https://runreveal.com/case-studies/clickhouse
**Evidence Level**: B (named-practitioner engineering blog + first-party OSS repo)
**Relevance**:
- Book ch05 §5.3 footnote `[^bakeoff]` (production corroboration of engine-for-the-workload; added 2026-07-08, WT-2)
- Hypothesis H-SIGMA-01 (sigmalite is a non-pySigma Sigma-evaluator implementation; RunReveal deploys it at ingest time)
- securitydataworks.com ProductionValidatorGrid row (RunReveal, Tier A first-party)

**Key Findings**:
- RunReveal is a security data platform / modern SIEM built on ClickHouse
- sigmalite: Go parser + execution engine for Sigma detection rules, Apache 2.0; RunReveal evaluates it at ingest time, though where in the pipeline sigmalite runs is the integrator's choice rather than a property of the library
- ClickHouse's own security team migrated its in-house security logging program to RunReveal, using their own ClickHouse Cloud service via the Destinations feature

**Citations**: Book ch05 `[^bakeoff]` corroboration sentence
**Notes**: The "RunReveal's team includes ex-ClickHouse security people" phrasing that circulated in internal planning docs did NOT verify and must not be used; the verified relationship is the inverse (ClickHouse's security team is a RunReveal customer).

**Validation Status**: ✅ verified 2026-07-08 (sigmalite repo fetched; ClickHouse blog + RunReveal case study confirmed via search primaries)

---

#### DNB - Cyber Defense Center on Ibis (Multi-Engine Lakehouse)

**Authors**: marimo (vendor-hosted case study; subject is DNB's Cyber Defense Center)
**Date**: 2025-10-14 (post date verified 2026-07-10; site last checked live 2026-07-08)
**URL**: https://marimo.io/blog/case-study-dnb
**Evidence Level**: B (named org + named security workload; vendor-hosted — marimo is the notebook vendor in the stack, bias flagged)
**Relevance**:
- Book ch06 §6.3 footnote `[^dnb]` (named external instance of the multi-engine variant; added 2026-07-08, WT-2)
- securitydataworks.com ProductionValidatorGrid row (DNB Bank, Tier B)

**Key Findings**:
- DNB (Norway's largest financial services group) Cyber Defense Center moved off Azure Databricks (Delta tables) to a composable stack
- Ibis as the query layer: analysts write once, execute across DuckDB, Spark, and Snowflake
- Iceberg table format for object-storage compatibility; DuckDB for single-node investigation performance; Neo4j for lateral-movement graph investigations; marimo notebooks as the unified interface (also connecting Splunk, Databricks, Snowflake)
- Stated motivation: investigation workloads wanted single-node performance but were tied to Databricks' distributed architecture and pricing model

**Citations**: Book ch06 `[^dnb]`
**Notes**: The site grid abbreviates to "Norway's largest bank"; the case study's own phrasing is "Norway's largest financial services group" — the book footnote uses the latter.

**Validation Status**: ✅ verified 2026-07-08 (WebFetch of the case study)

---

### Kafka Performance (Additional)

#### Azure - Kafka at Trillion Events/Day

**Authors**: Microsoft Azure Blog
**Date**: 2019-02-05 (verified at primary 2026-07-09; entry formerly said 2024)
**URL**: https://azure.microsoft.com/en-us/blog/processing-trillions-of-events-per-day-with-apache-kafka-on-azure/
**Evidence Level**: B (Microsoft production deployment) — re-tiered from A 2026-08-19: not peer-reviewed research and not an official standard
**Relevance**:
- Book ch02 §2.2 (components: collection and pipeline) [was: Chapter 7] (Kafka scalability)
- Best Practices Doc footnote [^72]

**Key Findings**:
- "3 trillion events per day" ingested and processed via Kafka on Azure; "up to 30 million events per second" (both verified verbatim at primary 2026-07-09 — supersedes the 2026-06-22 caution, which predated a full-page re-fetch and correctly removed a derived ~11.57M/sec figure)
- Cloud-scale validation

**Citations**: ch02 §2.2 (components: collection and pipeline) [was: Chapter 7] Kafka scale claims
**Notes**: Validates massive scale Kafka deployments

**Validation Status**: ✅ Active URL · Re-verified at primary 2026-07-09: 3T events/day and up-to-30M events/sec are on the page verbatim; publication date corrected to 2019-02-05.

---

## Emerging Technologies

### DuckDB Edge Processing

#### DuckDB Labs - DuckDB Overview

**Authors**: DuckDB Labs
**Date**: 2024-2026 (continuously updated)
**URL**: https://duckdb.org/why_duckdb
**Evidence Level**: B (official project documentation, cited for what DuckDB is; METHODOLOGY §3.1 and the 2026-11-03 vendor-documentation ruling; re-tiered from A 2026-08-19)
**Relevance**:
- Hypothesis (DuckDB edge processing - to be formalized)
- Book Chapter (emerging patterns)
- Public production report: Jake Thomas, Data Council 2024 (no interview held)
- Best Practices Doc footnote [^144]

**Key Findings**:
- Embedded analytics capabilities
- SQLite alternative for analytical workloads

**Citations**: Chapter on emerging patterns
**Notes**: no interview has happened; cite the Data Council 2024 talk entry instead

**Validation Status**: ✅ Active URL · Freshness (2026-06-05): publication date pre-2025 (>12mo) but freshness-triaged (date-stale; content NOT re-verified against source) in RESEARCH-JOURNAL.md ("Why DuckDB" supports the OLAP positioning). Stale-by-date, not by content.
**Refresh (2026-11-23)**: content re-verified, closing the 2026-06-05 date-only triage. The page still says DuckDB "does not run as a separate process but is completely embedded within a host process" by default and is "designed to support analytical query workloads", so both findings hold.

---

#### Okta Security Analytics with DuckDB — Data Council 2024 talk

> **Corrected 2026-08-12.** This entry previously cited "Jake Thomas (Okta, expert
> validation)", dated 2025, with URL "Personal communication (expert validation)"
> and Evidence Level B. **No such communication ever took place.** Outreach to Jake
> Thomas was drafted and never sent, so the personal-communication citation was
> fabricated, and downstream documents chained to it as though it were a source of
> record (appendix B's Okta figures trace here). What is real is his PUBLIC
> conference talk, which needs no permission and can be cited by anyone. The entry
> below is what the evidence actually supports. Claims this entry previously
> carried that the talk does NOT support have been removed rather than re-sourced.

**Authors**: Jake Thomas (then at Okta; now Blue Water Autonomy)
**Date**: 2024
**Source**: Data Council 2024, public conference talk
**URL**: https://duckdb.org/library/processing-trillions-of-records-at-okta-with-mini-serverless-databases/ (talk abstract, dated 2024-04-18)
**Alt URL**: https://www.aicouncil.com/talks/processing-trillions-of-records-at-okta-with-mini-serverless-databases (the old datacouncil.ai path redirects here)
**Evidence Level**: B (practitioner reporting a production deployment, publicly)
**Relevance**:
- ~~Research Question RQ7 (Isolation patterns and performance)~~ *(withdrawn 2026-11-23; the talk carries no isolation claim, per the Not-supported block below)*
- Hypothesis H-EDGE-01 (DuckDB edge processing)
- Book ch05 §5.3 + Appendix I [was: Chapter 9] (Query engines - DuckDB)

**Key Findings** (as reported in the talk):
- 7.5 trillion records across 130 million files processed in six months using thousands
  of concurrent DuckDB instances, with daily volume spiking from 1.5 TB to 50 TB without
  infrastructure changes (talk abstract, verified 2026-11-17). The abstract says only "serverless"; the runtime,
  AWS Lambda, is named in Julien Hurault's 2024-05-01 write-up of the talk (see the
  "Okta's Multi-Engine Data Stack" entry; re-sourced 2026-11-22)
- DuckDB viable for security analytics at genuine production volume

**Not supported by this source** (previously asserted here, now withdrawn): the
table-level-permissions-only detail, the "performance-first, avoids fine-grained
access control overhead" characterisation, and the isolation-first pattern
validation. Those came from the invented interview, not from the talk. Do not cite
them to Jake Thomas. RQ7 and RQ10 need another source.

**Citations**: H-EDGE-01 DuckDB production-volume evidence
**Notes**: A public talk is citable without permission. There has been no interview,
and nothing may be attributed to one.

**Refresh (2026-11-23)**: abstract re-read (HTTP 200); all four figures unchanged and verbatim. The same speaker gave a follow-up, "Embedding OLAP, Everywhere: Lessons from Okta" (Data Council 2025, 2025-05-29, https://duckdb.org/library/embedding-olap-everywhere-lessons-from-okta/, Tier B), whose abstract describes how Okta "shifted from traditional data processing systems to embedded database systems across multiple workloads" and gives no new figures, so it corroborates continued production use without replacing the 2024 numbers.

**Validation Status**: ✅ Public source, no permission required

---

### Table Format Interoperability

#### Apache XTable - Format Interoperability

**Authors**: Apache Software Foundation (Incubating)
**Date**: 2023-2025 (updated February 2026)
**URL**: https://xtable.apache.org/
**Alt URL**: https://github.com/apache/incubator-xtable
**Evidence Level**: B (Apache Incubator project, active development)
**Relevance**:
- Book ch05 §5.1 (table format) [was: Chapter 8] (Table formats)
- Best Practices Doc footnotes [^140], [^146]

**Key Findings**:
- Table format interoperability layer (renamed from OneTable)
- Omni-directional metadata translation: Iceberg ↔ Delta ↔ Hudi ↔ Paimon
- Not a new format - reads existing metadata, writes metadata for other formats
- **2025 updates**: CatalogSyncClient/CatalogSync interfaces added
- Glue and HMS catalog sync for all three formats
- Continuous sync via RunSync for real-time interop
- Restore/rollback sync during conversion
- Active development with Iceberg version support in pull requests

**Citations**: ch05 §5.1 (table format) [was: Chapter 8] format portability, catalog interoperability
**Notes**: Maturing beyond "emerging" - catalog sync and continuous sync features show production readiness trajectory; reduces vendor lock-in for security data lake implementations

**Validation Status**: ✅ Refreshed February 2026 - Active Apache Incubator project

---

#### Apache Arrow Flight SQL - High-Performance Query Connectivity

**Authors**: Apache Arrow Community
**Date**: 2022-2025 (ongoing development)
**URL**: https://arrow.apache.org/docs/format/Flight.html
**Alt URL**: https://arrow.apache.org/blog/2022/02/16/introducing-arrow-flight-sql/
**Evidence Level**: B (Official project documentation and project blog; not peer-reviewed research or a standard, so Level B under METHODOLOGY §3.1)
**Relevance**:
- Emerging Technologies section
- Book ch05 §5.2 (Arrow wire) [was: Chapter 10] (Integration patterns)
- Best Practices Doc footnotes [^150], [^151]

**Key Findings**:
- **As much as 20× faster than PyODBC** for query result retrieval — the blog's stated comparison target is PyODBC specifically (per a Dremio Subsurface talk it cites), not a generic JDBC/ODBC benchmark; scoped 2026-07-09 (from Alt URL: arrow.apache.org/blog/2022/02/16/introducing-arrow-flight-sql/ — not the spec page)
- Columnar data format eliminates row-based serialization overhead (qualitative advantage; no transfer-time percentage from this source)
- Production validation with ClickHouse, DuckDB, Dremio, StarRocks integrations
- Zero-copy transmission with Arrow in-memory columnar format
- ADBC libraries v17 released March 2025 (18 resolved issues, 13 contributors)

**Citations**: ch05 §5.2 (Arrow wire) [was: Chapter 10] federated query performance
**Notes**: Critical for multi-engine security architectures; original Summit 2024 link archived, replaced with official docs. The 20× benchmark is from the Feb 2022 Arrow blog post (Alt URL), not the spec page; cite accordingly. "60-90% transfer time saved" is not in either source and should not be cited.

**Validation Status**: ✅ Updated January 2026 - Official Apache Arrow documentation

**Validation (2026-06-05, folded)**: corrections applied to findings/tier above; provenance in RESEARCH-JOURNAL.md.
**Re-tiered (2026-11-07)**: A → B. Project documentation and a project blog post meet the §3.1 Level B definition, not Level A (peer-reviewed research and official standards only); this entry survived the 2026-08-19 downward audit and was caught by the 2026-11-07 upgrade-plan review. Key Findings unchanged.
---

#### Anyscale Ray Serve - Production AI Deployment Platform

**Authors**: Anyscale (Akshay Malik, Edward Oakes, Phi Nguyen)
**Date**: 2023-09-25 (byline verified 2026-07-10; entry formerly said 2024)
**URL**: https://www.anyscale.com/blog/tackling-the-cost-and-complexity-of-serving-ai-in-production-ray-serve
**Evidence Level**: B (Vendor platform with production validation)
**Relevance**:
- Emerging Technologies section
- ML model deployment and serving
- Best Practices Doc footnote [^152]

**Key Findings**:
- Ray Serve + Anyscale Services generally available (2024)
- 600% usage growth since Jan 2023
- 99.9% availability, 5000+ replicas scale demonstrated
- Private/public networking for security compliance
- Multi-AZ support, head node fault tolerance
- **Replica Compaction**: 56% faster performance (Ray Summit 2024 press release — not the cited blog post; cite separately)

**Citations**: Advanced analytics, ML deployment patterns
**Notes**: General AI/ML serving platform, applicable to security analytics use cases. The 600% growth, 99.9% availability, and 5000+ replicas figures are from the cited "tackling-the-cost-and-complexity" blog post. The 56% Replica Compaction figure is from the Ray Summit 2024 press release. The "60% elastic-training cost reduction" figure is not in any findable source and has been removed.

**Validation Status**: ✅ Active URL (verified Anyscale blog, 2024)

**Validation (2026-06-05, folded)**: corrections applied to findings/tier above; provenance in RESEARCH-JOURNAL.md.
---

#### Cloudera Impala + Iceberg Performance

**Authors**: Cloudera Engineering Blog
**Date**: 2022-02-22 (cited page dated Feb 22, 2022; catalogued "2024" corrected 2026-07-09 — A→B re-tier flagged in review packet: the "10x" is a vendor-relayed single-customer anecdote)
**URL**: https://www.cloudera.com/blog/technical/introducing-apache-iceberg-in-cloudera-data-platform.html
**Evidence Level**: B (Production benchmarks) — re-tiered from A 2026-08-19: not peer-reviewed research and not an official standard
**Relevance**:
- Hypothesis H-ARCH-01 (Iceberg dominance)
- Book ch05 §5.1 (table format) [was: Chapter 8] (Storage formats)
- Best Practices Doc footnote [^159]

**Key Findings**:
- 10× performance improvement over traditional Hive tables
- Private technical-preview release of Iceberg for CDP Data Services (2022) — the page announces a TP, not GA; the 10× figure is a single customer's anecdote ("one of our customers found that Iceberg tables perform 10x times better") (re-scoped 2026-07-10)
- Iceberg ACID transactions

**Citations**: ch05 §5.1 (table format) [was: Chapter 8] Iceberg performance validation
**Notes**: Enterprise platform validation

**Validation Status**: ✅ Active URL · Freshness (2026-06-05): publication date pre-2025 (>12mo) but content-current — re-sourced 2026-06-05 (10× over Hive verbatim on the live page); see RESEARCH-JOURNAL.md. Stale-by-date, not by content.

---

#### Apache Flink Checkpointing - Fault Tolerance Patterns

**Authors**: Apache Flink Documentation
**Date**: 2024-2026 (continuously updated; v2.3.0 docs read 2026-11-23)
**URL**: https://nightlies.apache.org/flink/flink-docs-stable/docs/dev/datastream/fault-tolerance/checkpointing/
**Evidence Level**: B (Official documentation; prescribes mechanism, not security-specific intervals or recovery SLAs)
**Relevance**:
- Hypothesis H-IMPL-02 (Streaming expertise)
- Book ch02 §2.2 (components: collection and pipeline) [was: Chapter 7] (Streaming architectures)
- Best Practices Doc footnotes [^166], [^169]

**Key Findings**:
- Checkpoint-interval configuration: frequency-vs-overhead tradeoff must be tuned per workload (generic doc does not prescribe specific intervals)
- RocksDB state backend supported for large state; recovery time depends on state size and checkpoint frequency
- Checkpointing is a fundamental fault-tolerance mechanism for stateful streaming jobs

**Citations**: ch02 §2.2 (components: collection and pipeline) [was: Chapter 7] streaming reliability patterns
**Notes**: The Flink documentation describes checkpointing mechanics and configuration options without prescribing specific intervals. Do not cite "30-60s for security" or "sub-2min recovery" — these figures are not in this source.
**Refresh (2026-11-23)**: the `flink-docs-stable` alias now serves the v2.3.0 documentation, so the cited URL moves with each release; the pinned copy is https://nightlies.apache.org/flink/flink-docs-release-2.3/docs/dev/datastream/fault-tolerance/checkpointing/ (HTTP 200). The page still treats the interval as a parameter ("call enableCheckpointing(n) on the StreamExecutionEnvironment, where n is the checkpoint interval in milliseconds") and prescribes no security-specific value. One precision for the second finding: on this page, large state is handled through checkpoint storage ("For proper persistence of large state, Flink supports various approaches for checkpointing state in other locations"), and RocksDB appears only as `EmbeddedRocksDBStateBackend` in the configuration options, so cite Flink's state-backends page for the RocksDB recommendation.

**Validation Status**: ✅ Active URL

**Validation (2026-06-05, folded)**: corrections applied to findings/tier above; provenance in RESEARCH-JOURNAL.md.
---

#### Microsoft Purview - Retention Policies and Labels

**Authors**: Microsoft Learn
**Date**: 2024-2026 (continuously updated; page ms.date 2026-07-22)
**URL**: https://learn.microsoft.com/en-us/purview/retention
**Evidence Level**: B (vendor documentation cited for what the feature does, per the 2026-11-03 ruling; general retention-policy/label reference only)
**Relevance**:
- Compliance retention requirements
- Book ch06 §6.1 (sovereignty) + Appendix J [AMBIGUOUS] [was: Chapter 11] (Governance)
- Best Practices Doc footnote [^168]

**Key Findings**:
- Microsoft Purview provides retention policies and labels for governing data lifecycle across M365 services
- Supports configuring retention periods and disposal actions at the policy and per-label level
- Reference for understanding retention-framework mechanics, not security-specific UEBA thresholds

**Citations**: ch06 §6.1 (sovereignty) + Appendix J [AMBIGUOUS] [was: Chapter 11] compliance patterns
**Notes**: Generic retention-policy/label reference. Security-specific figures (session durations, entity-profile windows, NIST alignment) are not present in this source and have been removed.
**Refresh (2026-11-23)**: page re-read (HTTP 200, last updated 2026-07-22). It still sets policies at "a site or mailbox level" and labels "at an item level (folder, document, email)", with retain-only, delete-only and retain-then-delete outcomes, so the findings hold; it also lists "Microsoft Copilot experiences" among the locations retention covers.

**Validation Status**: ✅ Active URL

**Validation (2026-06-05, folded)**: corrections applied to findings/tier above; provenance in RESEARCH-JOURNAL.md.
---

#### Confluent Customer Success - Implementation Roadmap

**Authors**: Confluent Developer Resources
**Date**: 2024
**URL**: https://developer.confluent.io/courses/apache-kafka/
**Evidence Level**: C (Vendor learning-path resource — no deployment-timeline data disclosed)
**Relevance**:
- Hypothesis H-IMPL-03 (Implementation timelines)
- Book ch07 §7.2-7.3 + Appendix K [was: Chapter 4] (Journey timelines)
- Best Practices Doc footnotes [^170], [^171]

**Key Findings**:
- Confluent publishes Apache Kafka 101, an introductory developer course of 16 lessons, 11 topic lessons and 5 hands-on exercises (topics, partitions, brokers, replication, producers, consumers, Schema Registry, Kafka Connect, stream processing with a Flink SQL exercise, Confluent's offerings)
- The course is ordered from concepts to client code to integration, but it is a learning sequence for developers, with no adoption or implementation roadmap and nothing about maturity stages; its operations content is limited to the Brokers and Replication lessons
- No specific deployment-timeline figures are disclosed in this source; specific month estimates have been removed

**Citations**: ch02 §2.2 (components: collection and pipeline) [was: Chapter 4] streaming implementation journey
**Notes**: Supports the qualitative point that vendor-structured learning paths exist; not a source for quantitative timeline claims.

**Validation Status**: ✅ Active URL
**Refresh (2026-11-23)**: URL redirects to the course's first lesson (/courses/apache-kafka/events/), status 200. The course is Apache Kafka 101 with 16 lessons (5 of them hands-on exercises), and it now links Kafka 4.0 material, so it was revised after 2024. The heading's "Implementation Roadmap" framing goes beyond the source: the page is an introductory course with no adoption stages or timelines, and the findings were narrowed to match.

**Validation (2026-06-05, folded)**: corrections applied to findings/tier above; provenance in RESEARCH-JOURNAL.md.
---

#### phData - Data Platform Implementation (Iterative Delivery)

**Authors**: phData (Nick Hauschild)
**Date**: 2021-11-12 (byline verified 2026-07-10; entry formerly said 2024)
**URL**: https://www.phdata.io/blog/how-to-implement-a-data-platform/
**Evidence Level**: C (Vendor opinion blog — iterative/use-case-first delivery argument, no quantitative timeline data)
**Relevance**:
- **Hypothesis H-IMPL-03** (Security timeline premium)
- Book ch07 §7.2-7.3 + Appendix K [was: Chapter 4] (Implementation timelines)
- Best Practices Doc footnotes [^172], [^173]

**Key Findings**:
- phData argues for iterative, use-case-first delivery over big-bang data platform implementations
- Recommends phased rollout to reduce risk and accelerate time-to-value
- No Gartner attribution; no specific month-based timeline figures appear in the source

**Citations**: H-IMPL-03 qualitative support, ch07 §7.2-7.3 + Appendix K [was: Chapter 4] implementation approach
**Notes**: Previously mislabeled as Gartner research. Specific numeric timelines (5.5 months, 6-12 months) are not present in this source and have been removed. Cite with vendor-blog bias caveat.

**Validation Status**: ✅ Active URL

**Validation (2026-06-05, folded)**: corrections applied to findings/tier above; provenance in RESEARCH-JOURNAL.md.
---

#### Brooks - The Mythical Man-Month (Throwaway Prototype)

**Authors**: Frederick P. Brooks Jr.
**Date**: 1995 (Anniversary Edition)
**URL**: https://www.pearson.com/en-us/subject-catalog/p/mythical-man-month-essays-on-software-engineering-anniversary-edition-the/P200000000149
**Evidence Level**: B (Seminal work, widely cited) — re-tiered from A 2026-08-19: not peer-reviewed research and not an official standard
**Relevance**:
- Implementation patterns
- Book ch07 §7.2-7.3 + Appendix K [was: Chapter 4] (Pilot-first approach)
- Best Practices Doc footnote [^183]

**Key Findings**:
- "Plan to throw one away" principle (1975 essay, ch. 11). In the 1995 Anniversary Edition's added ch. 19, "The Mythical Man-Month after 20 Years", Brooks is reported to revise it as "too simplistic" because it assumes a waterfall sequence, and to favour incremental build *(Unverified at the primary 2026-11-23: wording via a Tier C secondary source, a 2008 blog comment quoting p. 265 of ISBN 0-201-83595-9; confirm against the book before quoting)*
- Complex systems require experiential learning
- Pilot architecture reduces risk

**Citations**: ch07 §7.2-7.3 + Appendix K [was: Chapter 4] implementation methodology
**Notes**: Classic reference, data architecture applicability Cite the pilot-first point to ch. 11 and state the 1995 revision wherever the throwaway principle is used, because the edition cited here is reported to contain Brooks's own revision of it.

**Validation Status**: ✅ Active URL (book available) · Freshness (2026-06-05): publication date pre-2025 (>12mo) but content-current — re-sourced 2026-06-05 (Pearson product code corrected — the prior URL resolved to a different book); see RESEARCH-JOURNAL.md. Stale-by-date, not by content.
**Refresh (2026-11-23)**: Pearson page live (200), 1995 Anniversary Edition confirmed (paperback ISBN 9780201835953). The ch. 19 revision of the throwaway advice is corroborated by a secondary source only and was added to Key Findings with an unverified label.

---

#### Netflix - Building Resilient Data Platform with WAL

**Authors**: Netflix Technology Blog
**Date**: 2025
**URL**: https://netflixtechblog.com/building-a-resilient-data-platform-with-write-ahead-log-at-netflix-127b6712359a
**Evidence Level**: B (Production implementation at scale) — re-tiered from A 2026-08-19: not peer-reviewed research and not an official standard
**Relevance**:
- Resilient data platform patterns
- Book ch02 §2.2 (components: collection and pipeline) [was: Chapter 7] (Migration patterns)
- Best Practices Doc footnote [^185]

**Key Findings**:
- Write-Ahead Log (WAL) for data reliability
- Keystone central nervous system
- Shadow infrastructure validation approach
- Chaos engineering for resilience

**Citations**: ch07 §7.2-7.3 + Appendix K [was: Chapter 7] migration best practices, resilience patterns
**Notes**: Netflix = authoritative streaming source, WAL provides durability guarantees

**Validation Status**: ✅ Active URL (verified 2025)

---

#### Netflix Petabyte-Scale Logging — ClickHouse + Iceberg (Muino, 2025)

**Authors**: Daniel Muino (Netflix)
**Date**: 2025 (ClickHouse blog dated Oct 23, 2025; underlying talk Daniel Muino, ClickHouse meetup, July 2025; catalogued "2024" corrected 2026-07-09)
**URL**: https://clickhouse.com/blog/netflix-petabyte-scale-logging
**Evidence Level**: B (ClickHouse-published case study of a Netflix production deployment; vendor-relayed, no first-party Netflix primary found)
**Relevance**:
- **Research Question RQ7** (Isolation patterns and performance)
- ~~**Research Question RQ10** (Catalog governance decisions)~~ *(2026-11-23: the blog body says nothing about catalogs, so this entry carries no catalog-governance evidence)*
- Book ch05 §5.1 (table format) [was: Chapter 8] (Storage formats - ~~catalog selection~~ Iceberg cold tier only, per the 2026-11-23 note under Key Findings)
- Book ch05 §5.3 + Appendix I [was: Chapter 9] (Query engines - ClickHouse architecture)

**Key Findings** (figures verified at the ClickHouse blog primary, 2026-07-09):
- ClickHouse hot tier + Apache Iceberg cold tier, handling ~5 PB/day of logs
- 10.6M events/sec average (12.5M peak), ~5 KB/event; 40,000+ microservices
- 500–1,000 queries/sec; logs usually searchable within ~20 seconds vs a 5-minute SLA
- ~~Iceberg metadata catalog is pluggable — the blog names Apache Polaris, Unity Catalog OSS, Nessie, and Hive Metastore as options; "Polaris" is one catalog choice, not the platform name~~ *(Not in page, 2026-11-23: the blog body, live and in Wayback copies of 2025-10-31 and 2026-07-18, contains none of "Polaris", "Nessie", "Hive Metastore", "Unity Catalog", "pluggable" or "catalog"; whether the underlying July 2025 talk named these catalogs is unconfirmed, so cite nothing about catalogs from this entry without a talk-level source.)*
- The blog does not use "isolation-first"; the earlier security/isolation framing was a mis-attribution and has been removed (entry retitled 2026-07-09)

**Citations**: RQ7/RQ10 qualitative architecture reference, ch05 §5.3 + Appendix I [was: Chapter 8/9] ClickHouse + Iceberg pattern
**Notes**: Retitled + de-misattributed 2026-07-09 (was "Netflix Security Observability - Isolation-First Architecture with Polaris"). Still likely overlaps "Netflix ClickHouse Pipeline - 5 PB/Day" — consider merging in a future pass. Cite as a ClickHouse + Iceberg production-scale case study; ClickHouse-published, so vendor-relayed (Tier B).

**Validation Status**: ⚐ Re-sourced to ClickHouse blog post; original QCon claims not substantiated

**Validation (2026-06-05, folded)**: corrections applied to findings/tier above; provenance in RESEARCH-JOURNAL.md.
---

#### Cloudera Total Economic Impact — Public Cloud (Forrester TEI, October 2021)

**Authors**: Forrester Consulting (commissioned by Cloudera)
**Date**: 2021-10 (PDF date verified 2026-07-09; formerly conflated into a single "2024" entry)
**URL**: https://www.cloudera.com/content/dam/www/marketing/resources/analyst-reports/total-economic-impact-cdp-public-cloud.pdf (gated landing page; 194% ROI confirmed on the landing page 2026-11-17; $35.54M and the October 2021 cover date carried from the 2026-07-09 PDF check)
**Evidence Level**: C (Commissioned research, quantitative — flag vendor-commissioned bias where cited) — re-tiered from A 2026-08-19: not peer-reviewed research and not an official standard
**Relevance**:
- Book ch02 §2.3 (economics) [was: Chapter 1] (Cost comparisons)

**Key Findings**:
- 194% ROI and $35.54M benefits over 3 years (verified in the PDF 2026-07-09)

**Citations**: ch02 §2.3 (economics) [was: Chapter 1] cost modeling
**Notes**: **Split 2026-07-09** from a conflated Public+Private entry. The "39% licensing / 32% hardware / 29% operational" TCO breakdown formerly credited to this study appears in NEITHER TEI document (grep-negative in both) and was withdrawn — H-IMPL-01 must not cite a TCO distribution from Forrester TEI.

**Validation Status**: ✅ Figures verified in PDF 2026-07-09; PDF is dated October 2021, not 2024

---

#### Cloudera Total Economic Impact — Private Cloud (Forrester TEI, May 2024)

**Authors**: Forrester Consulting (commissioned by Cloudera)
**Date**: 2024-05
**URL**: https://tei.forrester.com/go/cloudera/onPremises/
**Evidence Level**: C (Commissioned research, quantitative, six representatives of five organizations interviewed, results modelled on a composite organization; flag vendor-commissioned bias where cited) — re-tiered from A 2026-08-19: not peer-reviewed research and not an official standard
**Relevance**:
- **Hypothesis H-IMPL-01** (Hidden costs)
- Book ch02 §2.3 (economics) [was: Chapter 1] (Cost comparisons)
- Best Practices Doc footnote [^187]

**Key Findings**:
- 35% cost savings with modern architecture
- 80% faster time to value worth $11.5M over 3 years
- 20% enhanced data team productivity, $1.6M over 3 years
- Headline: 254% ROI and $12.77M NPV over three years for the composite; the 35% saving is against a $6M annual storage-and-compute baseline and is valued at $4.7M over three years (risk-adjusted present value; verified 2026-11-23)

**Citations**: H-IMPL-01 (directional only — see note), ch02 §2.3 (economics) [was: Chapter 1] cost modeling
**Notes**: **Split 2026-07-09** from a conflated entry that mixed this study with the October 2021 Public Cloud PDF. The TCO-distribution claim was withdrawn (see the Public Cloud entry); the remaining figures are savings/velocity claims, not a cost-share breakdown.

**Validation Status**: ✅ Active URL; all figures verified on the TEI page 2026-11-23
**Refresh (2026-11-23)**: page live (200), May 2024 date confirmed; no newer Cloudera TEI found; interviewee count corrected to six representatives of five organizations. A financial-services spotlight of the same study exists at tei.forrester.com/go/cloudera/financialspotlight/ and repeats the 254% and $12.77M figures; it is the same May 2024 study, not new evidence.

---

#### Confluent - Kafka Architecture & Sizing

**Authors**: Confluent Developer Resources
**Date**: 2024
**URL**: https://developer.confluent.io/courses/architecture/get-started/
**Evidence Level**: B (Vendor best practices)
**Relevance**:
- ~~**Hypothesis H-IMPL-01** (Streaming TCO)~~ *(2026-11-23: the page carries no TCO content, so it supports no H-IMPL-01 leg)*
- Book ch02 §2.3 (economics) [was: Chapter 7] (Kafka sizing)
- Best Practices Doc footnote [^188]

**Key Findings**:
- Operational complexity and specialized talent dominate self-managed Kafka TCO (qualitative consensus; specific 45-55% figure is not in this source) *(Withdrawn 2026-11-23, not in source: the course page contains none of "TCO", "total cost", "talent", "operational complexity" or "sizing", and its two mentions of cost concern choosing a Confluent Cloud cluster type for the exercises.)*
- Sizing methodology covering partition counts, replication, and broker capacity *(Narrowed 2026-11-23: the page explains topics, partitions and what sits inside a broker, and notes that a partition can exceed "the capacity of a single broker" in Confluent's implementation, but it gives no sizing method; read it as architecture background.)*

**Citations**: ~~H-IMPL-01 TCO validation~~ *(withdrawn 2026-11-23)*, ch02 §2.3 (economics) [was: Chapter 7] capacity planning
**Notes**: ~~**CRITICAL** - Streaming operational cost driver.~~ *(Withdrawn 2026-11-23 with the driver finding above; the course page is architecture background only.)* The "45-55% of TCO" figure has been removed as unsupported by this source. For a quantified reduction claim, Confluent's TCO page cites "up to 40-60% TCO reduction" with managed Kafka. Correction (2026-07-10, part-2 sweep fix 9): the "infrastructure cost benchmarks for capacity planning" finding was dropped — the cited course covers Kafka internals/architecture only and carries no cost or capacity-cost content at all. *(Unverified 2026-11-17: the TCO page this figure is attributed to is not named by URL, and Confluent's cost-effectiveness page, confluent.io/project-metamorphosis/cost-effective/, says "up to 60%" and gives no 40-60% range. Re-read 2026-11-23: the cost-effective page still says "Reduce TCO of Kafka by up to 60% using Confluent" and gives no 40-60% range; cite it as "up to 60%", vendor claim, Tier C.)*

**Validation Status**: ✅ Verified at primary 2026-07-10; cost-benchmark finding removed as unsupported · ⚠️ 1 figure unverified 2026-11-17, see the dated label

**Validation (2026-06-05, folded)**: corrections applied to findings/tier above; provenance in RESEARCH-JOURNAL.md.
---

#### Databricks TCO - Lakehouse vs Traditional Platforms

**Authors**: Databricks / Lovelytics + 2025 Industry Analysis
**Date**: 2022-2026 (updated January 2026)
**URL**: https://www.databricks.com/databricks-vs-snowflake
**Alt URL**: https://dateonic.com/databricks-vs-snowflake-a-ctos-guide-to-total-cost-of-ownership-tco/
**Evidence Level**: C (Vendor analysis + independent benchmarks, quantitative data) — re-tiered from A 2026-08-19: not peer-reviewed research and not an official standard
**Relevance**:
- Cost comparisons
- Book ch02 §2.3 (economics) [was: Chapter 1] (Platform economics)
- Best Practices Doc footnote [^189]

**Key Findings**:
- **2025 TCO formula**: TCO = Direct Costs + Engineering/Operational Costs – ROI from AI/ML
- **Up to 9× lower ETL costs** vs Snowflake — Alt URL (dateonic) verbatim "up to 9x lower ETL costs compared to Snowflake"; attribute to dateonic, NOT the Databricks page
- Databricks page's own current claims (2026-07-10 fetch): "Unity Catalog managed tables accelerate queries up to 20x and cut cost by more than 50%"; "Databricks ran 2.8x faster, at about 3.4x better price/performance"; Snowflake Gen2 "increases cost by up to 35% for I/O bound workloads" — vendor self-claims, cite as such
- Platform consolidation reduces admin overhead
- **Security note**: Databricks lacks storage layer (relies on S3/Azure Blob/GCS); Snowflake has always-on encryption

**Note**: URL updated January 2026 to current comparison pages; TCO varies significantly by workload type

**Citations**: ch02 §2.3 (economics) [was: Chapter 1] lakehouse economics
**Notes**: Lakehouse cost structure validation. Correction (2026-07-10, part-2 sweep fix 5): the former 30-50% TCO, 15-40%-in-3-6-months, 57%-vs-27% YoY revenue, and AMN Healthcare 93% counterpoint findings were removed — none appear on the cited Databricks page or the dateonic Alt URL (fetched both); the 9× figure was the only one that verified, at dateonic. If the AMN counterpoint matters for balance, re-source it to its own primary before re-adding.

**Validation Status**: ✅ Both URLs fetched 2026-07-10; figures re-attributed to their actual sources

---

#### Gartner - Security Data Growth Rates & Spending Forecast 2024-2029

**Authors**: Gartner Security & Risk Management
**Date**: 2024-2026 (updated February 2026)
**URL**: https://www.gartner.com/en/newsroom/press-releases/2025-07-29-gartner-forecasts-worldwide-end-user-spending-on-information-security-to-total-213-billion-us-dollars-in-2025
**Alt URL**: https://www.gartner.com/en/newsroom/press-releases/2024-08-28-gartner-forecasts-global-information-security-spending-to-grow-15-percent-in-2025
**Evidence Level**: B (Authoritative industry research) — re-tiered from A 2026-08-19: not peer-reviewed research and not an official standard
**Relevance**:
- Hypothesis H1-VOLUME-07 (Data volume claims)
- Book ch01 (background) + ch02 §2.3 [was: Chapter 2] (Volume trends)
- Best Practices Doc footnote [^190]

**Key Findings**:
- **Updated 2025 Forecast** (July 2025 revision):
  - $193B (2024) → $213B (2025) → $244B (2026) → $323B (2029)
  - 13.3% growth rate 2025-2026
  - AI and GenAI driving both internal adoption and attacker capabilities
- **AI-Amplified Security Market**: $49B (2025) → $160B (2029)
- **Security Software**: $95B (2024) → $106B (2025) → $121B (2026)
- **Previous Forecast Segments 2024-2028**:
  - Cloud security: 25.9% CAGR ($9.0B → $22.6B)
  - Managed security services: 15.0% CAGR ($24.1B → $42.1B)
  - Enterprise security software: 14.1% CAGR ($78.8B → $132.4B)
  - Infrastructure protection: 13.1% CAGR ($31.3B → $51.2B)
- 25-35% annual volume growth typical; multi-year volume planning requirements

*Unverified 2026-11-17: none of the figures above, nor the $212B in the Notes, could be re-read, because gartner.com blocks automated readers.*

**Citations**: H1-VOLUME-07 validation, ch01 (background) + ch02 §2.3 [was: Chapter 2] volume projections, market trends
**Notes**: July 2025 update raised 2025 forecast from $212B to $213B; extended to 2029 ($323B); AI-amplified security segment ($49B→$160B) is entirely new category

**Validation Status**: ✅ Refreshed February 2026 - July 2025 forecast update · ⚠️ 24 figures unverified 2026-11-17, see the dated labels

---

#### Retired (no primary) — "Streaming vs Batch Cost Differential" (phantom CloudZero citation)

**Status**: RETIRED 2026-07-09. This entry never resolved to a real primary — the URL was a placeholder, no CloudZero (or other) source supports a fixed streaming-over-batch cost premium, and every specific multiplier once attached to it (2.8-3.6×, IDC 2.5-3×, "Enterprise Data Quarterly" 1.5-2×) has since been withdrawn. `APPENDICES.md` D.3 already dropped the CloudZero line. Kept as a transparency record rather than silently deleted, following the "Declined — EITT Academy" precedent — so it is now an untiered stub (no Evidence Level), excluded from the tiered denominator.
**Disposition**: the qualitative "streaming carries a cost premium" point, if used at all, now anchors only to the Cloudera/Forrester TEI entry (Level A), with the caveat that 2025-2026 sources argue the premium is conditional on utilization/scale, not a fixed differential.
**Former tier**: B (industry-consensus placeholder) — retired as unsourced.
---

#### AWS Well-Architected - Compute Optimization

**Authors**: Amazon Web Services
**Date**: 2026-11-16 (Framework 'Last updated', per the Framework welcome page; the standalone Cost Optimization Pillar whitepaper is marked historical and slated for deprecation)
**URL**: https://docs.aws.amazon.com/wellarchitected/latest/framework/cost-optimization.html
**Evidence Level**: B (Cloud provider framework guidance — prescriptive methodology without a specific quantified savings figure)
**Relevance**:
- Cost optimization patterns
- Book ch02 §2.3 (economics) [was: Chapter 1] (Cost reduction strategies)
- Best Practices Doc footnotes [^194], [^198]

**Key Findings**:
- The AWS Well-Architected Framework's cost optimization pillar prescribes right-sizing compute to workload demand as a primary cost-reduction mechanism
- No savings figure appears in the Well-Architected cost-optimization guidance for right-sizing. AWS's own Compute Optimizer marketing claims recommendations can "reduce costs by up to 25%" (amazonaws.cn/en/compute-optimizer, read 2026-11-23; vendor ceiling, Tier C, bias flagged); the unsourced 15-25% range and the CloudZero 22% are not citable from this entry
- Pricing-model selection ("Select the best pricing model", COST07) is a separate practice in the same area; COST07-BP01 names Savings Plans, Reserved Instances and Spot Instances as the models to match to usage patterns. Graviton is not named on the pages read 2026-11-23

**Citations**: ch02 §2.3 (economics) [was: Chapter 1] cost optimization tactics
**Notes**: Cloud cost optimization baseline. The 22% figure has been removed; do not cite a right-sizing percentage from this entry; cite CloudZero separately for its 22%, or the Compute Optimizer 'up to 25%' as a vendor ceiling.

**Validation Status**: ✅ URL available (AWS docs) · the 2026-11-17 unverified range was removed 2026-11-23, see the Refresh note
**Refresh (2026-11-23)**: cited URL redirects to the Framework's cost-optimization page (Framework last updated 2026-11-16), which regroups the pillar into four areas; the standalone pillar whitepaper is now historical. Right-sizing guidance unchanged in substance.

**Validation (2026-06-05, folded)**: corrections applied to findings/tier above; provenance in RESEARCH-JOURNAL.md.
---

#### AWS Storage Optimization - Tiered Storage

**Authors**: Amazon Web Services
**Date**: 2024
**URL**: https://aws.amazon.com/s3/storage-classes/intelligent-tiering/
**Evidence Level**: B (Cloud provider quantitative claim from vendor product page; methodology not independently audited)
**Relevance**:
- **Hypothesis H-COST-09** (Tiered storage economics)
- Book ch02 §2.3 (economics) [was: Chapter 8] (Storage lifecycle)
- Best Practices Doc footnotes [^196], [^200]

**Key Findings**:
- Page verbatim tier savings: "The Infrequent Access tier saves up to 40% on storage costs"; "The Archive Instant Access tier saves up to 68% on storage costs"; Archive and Deep Archive tiers "save up to 95% for rarely accessed objects"
- Named customer outcomes on the page: Stripe ~30%, Zalando 37%, GRAIL 40%, Shutterstock and Illumina up to 60% — vendor-curated examples, cite as such
- Hot/warm/cold tiering mechanics covered; cold/archive tiers offer steeper savings for infrequently accessed data

**Citations**: H-COST-09 validation, ch02 §2.3 (economics) [was: Chapter 8] tiered storage economics
**Notes**: **CRITICAL** - Validates tiered storage hypothesis directionally. Correction (2026-07-10, part-2 sweep fix 10): the former "~35% average savings for non-optimized buckets" and "30-40% range" findings appear nowhere on the page — replaced with the page's actual up-to-40%/68%/95% tier figures and its named customer percentages. H-COST-09's independent grounding remains the S3 storage-class price-delta derivation (see the "AWS S3 Storage-Class Pricing" entry).

**Validation Status**: ✅ Verified at primary 2026-07-10; savings figures restated page-verbatim
**Refresh (2026-11-23)**: page re-read; the three tier figures are unchanged and verbatim. The 95% figure is stated for the Archive Access and Deep Archive Access tiers together ("save up to 95% for rarely accessed objects") and again for Deep Archive Access after 180 days, and the same passage gives "savings of 71%" for objects moved directly to Archive Access at 90 days. The page now names more customers than the five above: Torc Robotics "24% per month", Electronic Arts "30%", Amazon Photos "over 10%", Teespring "more than 30 percent", SimilarWeb "20%" and AppsFlyer "18% per GB stored". All are vendor-curated.

**Validation (2026-06-05, folded)**: corrections applied to findings/tier above; provenance in RESEARCH-JOURNAL.md.
---

#### Google SRE - Reliability Economics (Exponential Cost of Nines)

**Authors**: Marc Alvidrez (ed. Kavita Guliani), in Beyer et al., Site Reliability Engineering, O'Reilly/Google
**Date**: 2017 (book copyright, per the page footer — entry formerly said 2024)
**URL**: https://sre.google/sre-book/embracing-risk/
**Evidence Level**: B (Authoritative public text; bracketed placeholder URL corrected — cite as expert-consensus reference, not a quantified production study)
**Relevance**:
- Cost modeling for security infrastructure
- Book ch02 §2.3 (economics) [was: Chapter 1] (Cost comparisons - reliability tradeoffs)
- Best Practices Doc footnote [^222]

**Key Findings**:
- Cost does not rise linearly with reliability: an incremental improvement in reliability "may cost 100x more than the previous increment" (Embracing Risk). This is a hedged illustration and the chapter gives no per-nine multiplier; its nines sentence ("Each additional nine corresponds to an order of magnitude improvement toward 100% availability") is about availability and says nothing about cost
- The chapter names two cost dimensions, redundant machine/compute resources and the opportunity cost of engineering time spent on reliability in place of features; it calls the risk continuum nonlinear and never uses the word exponential
- Match the reliability target to business need: "We strive to make a service reliable enough, but no more reliable than it needs to be."

**Citations**: ch02 §2.3 (economics) [was: Chapter 1] reliability economics, cost optimization
**Notes**: URL updated to sre.google/sre-book/embracing-risk/. The original "10×" multiplier was incorrect; the SRE book says an increment "may cost 100x more" and gives no ~100× per nine figure. Security-specific reliability guidance is not in this source; remove that framing.

**Validation Status**: ✅ SRE book available
**Refresh (2026-11-23)**: page live (200), © 2017 confirmed. The ~100×-per-nine wording and 'exponential' were narrowed to the chapter's 'may cost 100x' and 'nonlinear'. The heading's 'Exponential' is kept as an anchor only.

**Validation (2026-06-05, folded)**: corrections applied to findings/tier above; provenance in RESEARCH-JOURNAL.md.
---

#### Gartner - Reliability Overinvestment Analysis

**Authors**: Gartner Research
**Date**: 2024 *(Unconfirmed 2026-11-23: the document page could not be read; an earlier pass reported a Wayback capture of the page dated 2022-12-24, which would put the document before 2024, but that capture was not re-read)*
**URL**: https://www.gartner.com/en/documents/3906266 (paywalled; returns 403 to automated fetch; title and existence of the document not confirmed 2026-11-23)
**Evidence Level**: B (Analyst advisory; specific "70% overspend" statistic is not findable in any Gartner source — entry retained as paywalled-analyst-consensus reference only)
**Relevance**:
- Infrastructure investment optimization
- Book ch02 §2.3 (economics) [was: Chapter 1] (Cost optimization patterns)
- Best Practices Doc footnote [^237]

**Key Findings**:
- Gartner advises aligning resilience investment to actual business need to avoid overspend on reliability that exceeds genuine requirements *(Unverified 2026-11-23: the document's title and content could not be read; paraphrase only.)*
- Resources committed to excess reliability headroom are unavailable for higher-value security initiatives *(Unverified 2026-11-23: the document's title and content could not be read; paraphrase only.)*
- Tiered reliability targets, matched to workload criticality, are the recommended approach (topic anchor: Gartner doc 3906266) *(Unverified 2026-11-23: the document's title and content could not be read; paraphrase only.)*

**Citations**: ch02 §2.3 (economics) [was: Chapter 1] optimization recommendations
**Notes**: The specific "70% of orgs overspend" figure is not verifiably sourced in any Gartner publication and has been removed. Cite this entry as paywalled-analyst guidance only.

**Validation Status**: ⚠️ Paywall (Gartner research)
**Refresh (2026-11-23)**: document page returns 403 to automated fetch; no public title or abstract found by search. Owner decision needed on whether a paraphrase of an unread paywalled document stays in the bibliography; the Google SRE entry carries the same 'reliable enough, no more' point verbatim and can stand in for it.

**Validation (2026-06-05, folded)**: corrections applied to findings/tier above; provenance in RESEARCH-JOURNAL.md.
---

#### Uptime Institute - Reliability Tier Economics

**Authors**: Uptime Institute
**Date**: 2024
**URL**: https://uptimeinstitute.com/tiers
**Evidence Level**: C (Industry standards body — specific "98% cannot justify beyond four nines" statistic is not findable; URL updated to tier-classification page; cite with methodology-disclosure caveat)
**Relevance**:
- Reliability tier cost analysis
- Book ch02 §2.3 (economics) [was: Chapter 1] (Reliability economics)
- Best Practices Doc footnote [^232]

**Key Findings**:
- Uptime Institute's Tier I-IV classification rates data-center facility infrastructure (power, cooling, maintenance, fault tolerance) and is presented as a way of "aligning infrastructure investments to business goals"; the page says a higher tier is not better in itself ("This progression does not mean that a Tier IV data center is better than a Tier II") and that "It is ultimately up to the owner to determine which Tier is best for their business needs."
- *(Narrowed 2026-11-23: the tiers page states no cost figures or cost comparison between tiers and does not discuss over-engineering; the cost gradient is an inference and has no cited source here.)*
- *(Inference, absent from the page 2026-11-23: applying facility tiers to workload criticality is this bibliography's extrapolation.)*

**Citations**: ch02 §2.3 (economics) [was: Chapter 1] reliability guidance
**Notes**: The specific "98% of orgs cannot economically justify beyond four nines" figure is not findable and has been removed. Cite this entry as the Uptime Institute tier-classification framework only (uptimeinstitute.com/tiers). The heading's 'Reliability Tier Economics' is not a document title; the cited source is the Tier Classification System page, which is open and not paywalled.

**Validation Status**: ⚠️ URL updated to uptimeinstitute.com/tiers; original specific statistic not sourced
**Refresh (2026-11-23)**: page live (200); claims narrowed to the page's 'aligning infrastructure investments to business goals' and 'Tier IV is not better than Tier II' wording; the tiers concern facility infrastructure and say nothing about software reliability.

**Validation (2026-06-05, folded)**: corrections applied to findings/tier above; provenance in RESEARCH-JOURNAL.md.
---

#### Apache Iceberg - Industry Consensus & Market Momentum

**Authors**: Dremio (State of the Data Lakehouse 2024) + Industry Analysis + 2025 Year in Review
**Date**: 2024-2026 (updated January 2026)
**URL**: https://www.dremio.com/press-releases/state-of-the-data-lakehouse-2024-businesses-are-leaving-cloud-data-warehouses-for-data-lakehouses/
**Alt URL**: https://amdatalakehouse.substack.com/p/2025-year-in-review-apache-iceberg
**Evidence Level**: C (Industry survey + vendor support validation) — re-tiered from A 2026-08-19: neither peer-reviewed research nor an official standard
**Relevance**:
- **Hypothesis H-ARCH-01** (Iceberg dominance)
- Book ch05 §5.1 (table format) [was: Chapter 8] (Storage formats)
- Best Practices Doc footnotes [^243], [^244]

**Key Findings**:
- **Industry consensus as de facto standard**: Iceberg confirmed as dominant open table format
- **Dremio 2024 survey**: 29% of organizations planning to adopt open table format chose Iceberg vs 23% for Delta Lake
- **Universal vendor support**: AWS, Google, Snowflake, Databricks, Microsoft all announced Iceberg compatibility
- **2025 maturity milestone**: "The open lakehouse is no longer a concept. In 2025, key Apache projects matured, making data warehouse performance on object storage a practical reality."
- **Gartner upgrade (2025)**: Lakehouse upgraded from "high-benefit" to "transformational" based on open table format adoption
- **V3 specification finalized (2025)**: Row-level deletes, row lineage, semi-structured data handling, native encryption
- **2026 outlook**: "Streaming-first lakehouses" with Iceberg as foundation; default starting point for cloud/warehouse modernization

**Citations**: H-ARCH-01 dominance validation, ch05 §5.1 (table format) [was: Chapter 8] format selection
**Notes**: **CRITICAL** - 2025 Year in Review confirms Iceberg's position. Confidence remains Strong (⭐⭐⭐⭐⭐) with Gartner "transformational" upgrade + V3 maturity + universal vendor support.

**Validation Status**: ✅ Refreshed January 2026 - V3 maturity, Gartner upgrade, 2026 streaming-first outlook confirmed

---

#### Apache Iceberg - Universal Vendor Support

**Authors**: Apache Software Foundation + Vendor Announcements
**Date**: 2025 (universal support confirmed; announcements began 2024, Databricks gap closed 2025)
**URL**: https://www.theregister.com/2024/10/14/apache_iceberg_feature_announcements/
**Alt URL 2**: https://www.databricks.com/blog/announcing-full-apache-iceberg-support-databricks
**Evidence Level**: C (Vendor public commitments — date corrected to 2025 when full cross-vendor support was achieved) — re-tiered from A 2026-08-19: neither peer-reviewed research nor an official standard
**Relevance**:
- Hypothesis H-ARCH-01 (Iceberg dominance)
- Book ch05 §5.1 (table format) [was: Chapter 8] (Format ecosystem)
- Best Practices Doc footnote [^245]

**Key Findings**:
- Snowflake, AWS, Google, and Cloudera support Apache Iceberg per The Register's Oct 2024 roundup; Databricks added Iceberg support (Managed/Foreign tables via Unity Catalog) in **Public Preview** June 12, 2025 — not GA at announcement
- Microsoft is the named holdout, not a supporter: the cited Register piece's subheading is "Market rivals settle on open table format, while Microsoft and Databricks go their own way", and its body says "Although Microsoft Fabric provides some support for Iceberg and Hudi by default, Fabric favors Delta and Apache Parquet"
- Reduces vendor lock-in risk — open standard with cross-platform read/write compatibility, though vendor coverage is broad rather than universal

**Citations**: H-ARCH-01 validation, ch05 §5.1 (table format) [was: Chapter 8] vendor support
**Notes**: Correction (2026-07-10, part-2 sweep fix 2): the prior "Databricks, Snowflake, AWS, Google, and Microsoft all support" finding contradicted its own cited source — the Register piece explicitly separates Microsoft (Delta-first, partial Iceberg in Fabric) from the settlers, and its settler list is AWS/Cloudera/Google/Snowflake. Databricks support re-scoped to Public-Preview-as-of-2025-06 per the Alt URL 2 announcement. The entry title's "Universal" overstates; kept for cross-reference stability with the overstatement documented here. H-ARCH-01 reads on this: dominance-as-direction holds, universality does not.

**Validation Status**: ✅ Verified at both Alt URLs 2026-07-10 (part-2 sweep); Microsoft leg corrected

**Validation (2026-06-05, folded)**: corrections applied to findings/tier above; provenance in RESEARCH-JOURNAL.md.
---

#### Apache Iceberg Foundation - Governance & Contributors

**Authors**: Apache Software Foundation
**Date**: 2024
**URL**: https://iceberg.apache.org/community/
**Evidence Level**: B (Official ASF project metrics) — re-tiered from A 2026-08-19: neither peer-reviewed research nor an official standard
**Relevance**:
- Hypothesis H-ARCH-01 (Open governance advantage)
- Book ch05 §5.1 (table format) [was: Chapter 8] (Format selection criteria)
- Best Practices Doc footnotes [^246], [^247], [^249]

**Key Findings**:
- 407 contributors on apache/iceberg (GitHub deduplicated count, as of 2026-07-09) — re-sourced 2026-07-09: the cited community page carries no contributor or organization counts, so the earlier "300+ contributors across 100+ organizations" was replaced with the GitHub-derived figure and the organization count dropped as underivable *(Superseded 2026-11-23: the count was a floor set by the API limit and the "deduplicated" reading was mistaken; see the next bullet.)*
- Refreshed 2026-11-23: the GitHub contributors endpoint for apache/iceberg (read through `gh api`) now lists 406 linked accounts, 405 users and 1 bot, and with `anon=1` it lists 946 entries, 540 of them anonymous. GitHub's documentation for the endpoint says "only the first 500 author email addresses in the repository link to GitHub users" and that "The rest will appear as anonymous contributors without associated GitHub user information" (https://docs.github.com/en/rest/repos/repos#list-repository-contributors). The repository has more than 500 author email addresses, so the linked-account count is a floor set by that limit, and the 2026-07-09 reading that 407 was uncapped because it sat under 500 was mistaken. The distinct contributor count lies somewhere between 406 and 946, because anonymous entries are per email address and can repeat a person, and the API cannot narrow it further. Cite it as "more than 400 contributors with linked GitHub accounts (2026-11-23)" with the limit stated, and drop the bare "407".
- Open governance under the Apache Software Foundation: the community page describes the path from contributor to committer, with committers nominated and discussed by the PMC (the page does not use the word 'governance')
- ~~Iceberg Foundation for dedicated advancement~~ *(Withdrawn 2026-11-23: no 'Iceberg Foundation' appears on the community page or in a web search; the project is governed by the Apache Iceberg PMC under the Apache Software Foundation.)*

**Citations**: H-ARCH-01 sustainability validation
**Notes**: Community strength = long-term viability. For the contributor count, cite GitHub (https://github.com/apache/iceberg) with an as-of date, not the community page. The heading's 'Apache Iceberg Foundation' is a misnomer kept as an anchor; read it as 'Apache Iceberg (ASF project)'.

**Validation Status**: ✅ Re-verified 2026-07-09: community page live but count-free; contributor figure re-sourced to GitHub API (407, under the API's 500-entry cap, so uncapped). *(Corrected 2026-11-23: the 500 limit applies to author email addresses, which exceed 500 here, so the figure was capped.)*
**Refresh (2026-11-23)**: contributor count re-derived and the cap reading corrected (see Key Findings); the community page text was read and still gives no contributor or organization count. The governance findings were re-read the same day: no 'Iceberg Foundation' appears on the community page or in a web search, and the Iceberg Summit 2026 announcement (2026-01-10) says the summit is sanctioned by the Apache Software Foundation with oversight from the Apache Iceberg PMC, so the foundation finding is withdrawn and the open-governance finding is narrowed to what the page says. Latest release apache-iceberg-1.12.0, published 2026-09-30 (GitHub releases API, 2026-11-23).

---

#### Apache Iceberg - Official Documentation

**Authors**: Apache Iceberg Community
**Date**: 2024-2026 (continuously updated)
**URL**: https://iceberg.apache.org/
**Evidence Level**: B (Official open-source project documentation) — re-tiered from A 2026-08-19: neither peer-reviewed research nor an official standard
**Relevance**:
- Blog post: "Apache Iceberg - Yes, It's Important to Security"
- Book ch05 §5.1 (table format) [was: Chapter 8] (Storage Formats)
- Hypothesis H-ARCH-01 (Iceberg dominance)

**Key Findings**:
- Table format specification and architecture
- Schema evolution, time travel, ACID transactions
- Multi-engine query support (Spark, Trino, Dremio, Flink, etc.)
- Hidden partitioning for security analyst accessibility

**Citations**: Blog Iceberg deep-dive, ch05 §5.1 (table format) [was: Chapter 8] table format fundamentals
**Notes**: Authoritative technical reference for Iceberg architecture

**Validation Status**: ✅ Active (verified Feb 2026)

---

#### Apache Iceberg - Maintenance Documentation

**Authors**: Apache Iceberg Community
**Date**: 2024-2026 (continuously updated)
**URL**: https://iceberg.apache.org/docs/latest/maintenance/
**Evidence Level**: B (Official documentation) — re-tiered from A 2026-08-19: neither peer-reviewed research nor an official standard
**Relevance**:
- Blog post: "Spark Persistence Reality: Hybrid Architectures"
- Book ch05 §5.1 (table format) [was: Chapter 8] (Storage Formats - operational considerations)
- Table maintenance procedures

**Key Findings**:
- Expire snapshots procedure
- Rewrite data files optimization
- Remove orphan files cleanup
- Compact data files for query performance

**Citations**: Blog Spark hybrid architectures, ch05 §5.1 (table format) [was: Chapter 8] operational maintenance
**Notes**: Critical for production security data lake operations

**Validation Status**: ✅ Active (verified Feb 2026)

---

#### Apache Iceberg - Spark Procedures Documentation

**Authors**: Apache Iceberg Community
**Date**: 2024-2026 (continuously updated)
**URL**: https://iceberg.apache.org/docs/latest/spark-procedures/
**Evidence Level**: B (Official documentation) — re-tiered from A 2026-08-19: neither peer-reviewed research nor an official standard
**Relevance**:
- Blog post: "Spark Persistence Reality: Hybrid Architectures"
- Book ch05 §5.1 (table format) [was: Chapter 8] (Storage Formats - Spark integration)
- Production maintenance workflows

**Key Findings**:
- Spark SQL procedure syntax for maintenance
- Snapshot management procedures
- Metadata operations
- Table optimization commands

**Citations**: Blog Spark procedures, ch05 §5.1 (table format) [was: Chapter 8] Spark + Iceberg integration
**Notes**: Practical reference for security data engineers using Spark

**Validation Status**: ✅ Active (verified Feb 2026)

---

#### SK Telecom - Iceberg Performance Validation

**Authors**: SK Telecom (duplicate entry for cross-reference)
**Date**: 2022-12 (Trino Summit 2022)
**URL**: https://trino.io/blog/2022/12/19/trino-summit-2022-sk-telecom-recap.html
**Alt URL**: https://trino.io/assets/blog/trino-summit-2022/Trino@SK-Telecom.pdf (presentation slides — the precise figures below are in the slides, verified 2026-07-09; the recap page carries only approximations)
**Evidence Level**: B (Production deployment) — re-tiered from A 2026-08-19: not peer-reviewed research and not an official standard
**Relevance**:
- Hypothesis H-ARCH-01 (Performance advantage)
- Book ch05 §5.1 (table format) [was: Chapter 8] (Iceberg performance)
- Best Practices Doc footnote [^248]

**Key Findings**:
- Case 1: −97% read data size (209 GB → 6.11 GB) on a 52.7 TB Iceberg table; elapsed time 97.2 s → 3.39 s (−96.5%)
- The slides credit a partition redesign for partition pruning (33,942 Hive partitions to 109,765 Iceberg partitions, with hidden partitioning on days(event_time)) and column sorting for predicate pushdown, kept in order by a daily rewrite_data_files compaction; partition evolution is not mentioned. The before and after therefore compares a Hive table with a redesigned, sorted and compacted Iceberg table, so the gain cannot be assigned to the format alone
- Headline: "Reduced query elapsed time by 80%" (slides; the accompanying chart shows −82% total drivers, −91% read data size and −76% elapsed time); the same slides report storage reduced 75% and cores and memory reduced 60%

**Citations**: H-ARCH-01 performance validation
**Notes**: Quantitative production validation

**Validation Status**: ✅ Active URL
**Refresh (2026-11-23)**: recap and slides live (200); Case 1 figures re-verified verbatim; mechanism narrowed (predicate pushdown and partition pruning are in the slides, partition evolution is not). A separate SK Telecom Trino Summit 2023 deck (efficient Kappa architecture) exists but was not read and does not update these figures.

**Validation (2026-06-05, folded)**: corrections applied to findings/tier above; provenance in RESEARCH-JOURNAL.md.
---

#### ClickHouse vs Elasticsearch - Storage Efficiency

**Authors**: Tom Schreiber (ClickHouse)
**Date**: 2024
**URL**: https://clickhouse.com/blog/clickhouse_vs_elasticsearch_the_billion_row_matchup
**Evidence Level**: B (Benchmark study) — re-tiered from A 2026-08-19: not peer-reviewed research and not an official standard
**Relevance**:
- Hypothesis H3-PERFORMANCE-01 (ClickHouse advantages)
- Book ch05 §5.3 + Appendix I [was: Chapter 9] (Query engines)
- Best Practices Doc footnote [^208]

**Key Findings**:
- 12-19× less storage than Elasticsearch on the 10-billion-row data set and 9-12× on the 1-billion-row data set, both at functionally equivalent configuration (Elasticsearch `_source` kept, same compression level); with `_source` disabled the gap is about 7× (LZ4) to 10× (ZSTD) at 1 billion rows and 9× to over 14× at 10 billion (re-read 2026-11-23; the earlier "9-12× with `_source` disabled" reading was wrong, and the earlier "5-10×" matched only query-speed multipliers)
- Billion-row performance comparison
- Security log format optimization *(Not on the cited page, 2026-11-23: the benchmark uses PyPI download events and has no security content.)*

**Citations**: H3-PERFORMANCE-01 extension, ch05 §5.3 + Appendix I [was: Chapter 9] ELK migration
**Notes**: Vendor benchmark on PyPI download-event data (analytics and observability workload, count(*) aggregations); not a security-log test, label as such where cited

**Validation Status**: ✅ Re-verified at primary 2026-07-09: page (dated 2024-05-07 at fetch) states 12-19× / 9-12× storage reduction. The earlier freshness note's "2026-03-03 update / 5x realistic-OTel / 9-19×" claims are not on this page (the ~5×/OTel figures belong to a different 2026 ClickHouse post) and were removed.
**Refresh (2026-11-23)**: storage figures re-read verbatim ("12 to 19 times less storage space" at 10 billion rows; "9 to 12 times less storage space" at 1 billion rows, both with `_source` kept), the same as on 2026-07-09. The byline is Tom Schreiber (ClickHouse), May 7, 2024, so cite him as author. The page's structured data also carries `dateModified` 2026-03-03T12:30:30Z, which is probably where the removed "2026-03-03 update" note came from. The figures read the same as at the 2026-07-09 check. The `_source`-disabled attribution carried since 2026-07-09 is corrected in this pass.

---

#### Uber - Palette Feature Store for ML

**Authors**: Uber Engineering (Michelangelo Platform)
**Date**: 2024-01-18 (post date verified 2026-07-10; entry formerly said 2022-2024)
**URL**: https://www.uber.com/blog/palette-meta-store-journey/
**Evidence Level**: B (Production case study with unsupported headline stat; retained claims are qualitative/process)
**Relevance**:
- ML for security analytics
- Book Chapter (Advanced analytics patterns)
- Best Practices Doc footnote [^255]

**Key Findings**:
- Onboarding deployment time reduced by more than 95% after the metadata migration ("Palette Onboarding Deployment time has reduced drastically by more than 95%", read at the post 2026-11-22)
- Feature store solution for training/production consistency — eliminates training/serving skew
- Support for batch and near-real-time feature computation

**Citations**: Advanced analytics chapter, ML patterns
**Notes**: Production ML feature store at scale, presented at Feature Store Summit 2023

**Validation Status**: ✅ Active URL (verified 2024); the 95% figure, labelled unverified on 2026-11-17, was read at the post on 2026-11-22

**Validation (2026-06-05, folded)**: corrections applied to findings/tier above; provenance in RESEARCH-JOURNAL.md.
---

#### DARPA XAI - Explainable Artificial Intelligence Program

**Authors**: DARPA (program page); David Gunning and David W. Aha (AI Magazine 2019); David Gunning, Eric Vorm, Jennifer Yunyan Wang and Matt Turek (Applied AI Letters 2021 retrospective)
**Date**: 2017-2021 (program), published 2019
**URL**: https://www.darpa.mil/research/programs/explainable-artificial-intelligence
**Evidence Level**: B (Government research program; headline budget/ranking claims unsupported — retained claims are program-scope facts)
**Relevance**:
- ML explainability requirements
- Book Chapter (Advanced analytics)
- Best Practices Doc footnote [^270]

**Key Findings**:
- Development of XAI toolkit for future systems — program page verbatim: "the final delivery will be a toolkit library consisting of machine learning and human-computer interface software modules that could be used to develop future explainable AI systems"
- Defense and national security focus areas; false positives/negatives have high operational consequences
- 4-year program (2017-2021), ~11 research teams, David Gunning as program manager — attribute these to the retrospective (Gunning, Vorm, Wang & Turek 2021, *Applied AI Letters* 2(4), doi 10.1002/ail2.61), NOT the program page, which carries neither the team count, nor Gunning's name, nor the 2017-2021 span (verified 2026-07-10)

**Citations**: Advanced analytics, ML governance, regulatory compliance
**Notes**: Definitive government source on explainability requirements for security AI. Correction (2026-07-10, part-2 sweep fix 11): program-metadata claims re-attributed from the DARPA page to the retrospective the entry already lists.

**Validation Status**: ✅ Verified at primary 2026-07-10; toolkit claim page-verbatim, metadata re-attributed
**Refresh (2026-11-23)**: program page 200 and the toolkit sentence re-read verbatim. The retrospective at doi 10.1002/ail2.61 is by Gunning, Vorm, Wang and Turek per Crossref, not Gunning and Aha, whose paper is AI Magazine 40(2), 2019, doi 10.1609/aimag.v40i2.2850, so the author credit is corrected. The ~11 teams, the 2017-2021 span and the program-manager credit could not be re-read at the retrospective, which blocks automated readers, so they stay as attributed and unconfirmed this pass. For a standards anchor on explainability, see NIST IR 8312 (Four Principles of Explainable Artificial Intelligence, 2021-09-29, Tier A).

**Validation (2026-06-05, folded)**: corrections applied to findings/tier above; provenance in RESEARCH-JOURNAL.md.
---

#### SANS Institute - AI Survey & SOC Automation Research

**Authors**: 2024 AI Survey — Matt Edmondson, Matt Bromiley; 2025 SOC Survey — Christopher Crowley (SANS Institute; bylines verified at the landing pages 2026-07-10 — the former combined credit was wrong)
**Date**: 2024-2025 (updated February 2026)
**URL**: https://www.sans.org/white-papers/sans-2024-ai-survey-ai-growing-role-cybersecurity-lessons-learned-path-forward
**Alt URL**: https://www.sans.org/white-papers/sans-2025-soc-survey
**Evidence Level**: B (Security research authority, industry survey) — re-tiered from A 2026-08-19: neither peer-reviewed research nor an official standard
**Relevance**:
- Security ML operations and automation
- Book Chapter (Advanced analytics)
- Best Practices Doc footnote [^276]

**Key Findings**:
- AI reshaping cybersecurity landscape (2024 survey)
- SOC automation and detection/response capabilities
- **2025 AI Survey**: 100% of organizations plan GenAI adoption within 1 year
- 50% currently use AI for cybersecurity tasks, but autonomous SOC deployment lagging
- **2025 SOC Survey**: 79% operate 24/7 but 69% still rely on manual reporting
- 62% say organizations aren't doing enough to retain talent
- 40% use AI/ML tools but satisfaction ranks dead last among SOC capabilities
- Staff shortages and overwhelming data volumes persist as top challenges

*Unverified 2026-11-17, widened 2026-11-22: the 100%, 50%, 79%, 69%, 62% and 40% figures are not on the two survey landing pages, and the reports themselves sit behind registration and were not read.*

**Citations**: Advanced analytics, MLOps, SOC operations
**Notes**: 2025 surveys show paradox: universal AI intent (100% plan GenAI) vs. low satisfaction with existing AI tools (ranked last); staff retention crisis (62%) validates H-IMPL-02 streaming expertise scarcity

**Validation Status**: ✅ Refreshed February 2026 - 2025 AI + SOC surveys · ⚠️ 6 figures unverified 2026-11-17 (widened from 3 on 2026-11-22), see the dated labels

---

#### CISA - Enhanced Security Monitoring Best Practices

**Authors**: CISA (Cybersecurity and Infrastructure Security Agency)
**Date**: 2023-07-12 (updated 2023-07-14)
**URL**: https://www.cisa.gov/news-events/alerts/2023/07/12/cisa-and-fbi-release-cybersecurity-advisory-enhanced-monitoring-detect-apt-activity-targeting
**Alt URL**: https://www.cisa.gov/news-events/cybersecurity-advisories/aa23-193a (advisory, source of the findings)
**Evidence Level**: B (Government security authority) — re-tiered from A 2026-08-19: neither peer-reviewed research nor an official standard
**Relevance**:
- Enhanced monitoring and logging requirements
- Book Chapter (Advanced analytics)
- Best Practices Doc footnote [^260]

**Key Findings**:
- Enhanced audit logging for APT detection
- Baseline establishment for outlier detection
- MailItemsAccessed events monitoring (Microsoft 365)
- Continuous monitoring of cloud environments
- Quotes OMB M-21-31: Microsoft audit logs retained for at least twelve months in active storage plus eighteen months in cold storage (a federal civilian requirement, not a baseline-specific figure; read at advisory aa23-193a 2026-11-23)

**Citations**: Advanced analytics chapter, data retention, threat detection
**Notes**: Government authority on security monitoring practices, joint CISA/FBI guidance

**Validation Status**: ✅ Active URL (verified CISA advisory, July 2023) · Freshness (2026-06-05): publication date pre-2025 (>12mo), freshness-triaged (date-stale). Content correction 2026-06-22: the earlier "24-36 month retention" figure was an embellishment beyond the ~12mo the source supports — corrected to ~12mo.
**Refresh (2026-11-23)**: advisory aa23-193a read (it blocks curl, a reader tool got through); MailItemsAccessed, Purview Audit (Premium), baseline/outlier and the M-21-31 12+18-month retention lines all read. The retention figure is the federal log-retention rule the advisory quotes, so it is no longer framed as a baseline window. The alert URL in this entry is only the announcement and carries none of these lines. Follow-up: CISA Microsoft Expanded Cloud Logs Implementation Playbook (released 2025-01-15, page revised 2026-05-01) covers the same logs, now in Purview Audit (Standard) for E3/G3 and above.

---

#### MITRE Corporation - Insider Threat Research & Framework

**Authors**: MITRE Insider Threat Research & Solutions
**Date**: 2024
**URL**: https://insiderthreat.mitre.org/
**Evidence Level**: B (Research authority, over 20 years of program work per its homepage; headline detection-rate stats were invented — retained claims are framework-scope facts)
**Relevance**:
- Security ML training requirements
- Book Chapter (Advanced analytics - insider threat)
- Best Practices Doc footnote [^261]

**Key Findings**:
- Over 20 years of insider threat research and program stand-up work, multi-disciplinary team (homepage, read via Wayback snapshot 2026-10-05)
- 47 ATT&CK techniques, 29 sub-techniques for insider threats — source is the MITRE Engenuity Insider Threat Knowledge Base 2.0 announcement (medium.com/mitre-engenuity/insider-threat-knowledge-base-2-0-more-techniques-new-mitigations-and-the-human-touch-d246f5ef1135, verbatim "47 ATT&CK techniques and 29 sub-techniques"), a distinct property from the cited insiderthreat.mitre.org page, which carries no technique counts (repointed 2026-07-10)
- Bi-Directional Loyalty (BDL) defined by MITRE as a more practical risk measure than organizational commitment; measurement methods and the BDL-to-insider-threat link are still being developed and validated, and the homepage lists it under work seeking funding

**Citations**: Advanced analytics, insider threat detection, behavioral analytics
**Notes**: MITRE = definitive authority on insider threat research, multi-disciplinary team

**Validation Status**: ✅ Active URL (verified MITRE official site, 2024 data)
**Refresh (2026-11-23)**: live page blocks automated readers; read via Wayback 2026-10-05. Tenure is now stated as over 20 years; the InT Lab name is not on the homepage; BDL narrowed to in-development. The 47/29 technique counts belong to the CTID Insider Threat TTP Knowledge Base v2.0.0 (center-for-threat-informed-defense.github.io/insider-threat-ttp-kb) and its announcement post, which could not be re-read this pass.

**Validation (2026-06-05, folded)**: corrections applied to findings/tier above; provenance in RESEARCH-JOURNAL.md.
---

#### Microsoft Security - Threat Modeling & Data Security for AI/ML

**Authors**: Andrew Marshall, Jugal Parikh, Emre Kiciman, Ram Shankar Siva Kumar (Microsoft, with the AETHER Security Engineering Workstream)
**Date**: November 2019 (page ms.date 2025-03-12)
**URL**: https://learn.microsoft.com/en-us/security/engineering/threat-modeling-aiml
**Evidence Level**: B (Vendor engineering guidance; incident-rate stat removed — retained claims are the documented threat taxonomy)
**Relevance**:
- Security ML data requirements and security
- Book Chapter (Advanced analytics)
- Best Practices Doc footnote [^264]

**Key Findings**:
- 11-category AI/ML threat taxonomy: adversarial perturbation, data poisoning, model inversion, membership inference, model stealing, neural net reprogramming, physical-domain adversarial examples, malicious ML providers recovering training data, ML supply-chain attacks, backdoor ML, and exploited software dependencies
- Training data from public datasets poses supply chain risks
- Inference queries require input validation
- Training-data documentation (Datasheets for Datasets) and provenance tracking

**Citations**: Advanced analytics, data management, AI security
**Notes**: Microsoft = authoritative source on enterprise AI/ML security practices

**Validation Status**: ✅ Active URL (verified Microsoft Learn documentation)
**Refresh (2026-11-23)**: page 200, ms.date 2025-03-12; all 11 headings read, and the fourth is membership inference, not model inference. For a current Tier A taxonomy, see NIST AI 100-2 E2025 (Adversarial Machine Learning: A Taxonomy and Terminology of Attacks and Mitigations, March 2025).

**Validation (2026-06-05, folded)**: corrections applied to findings/tier above; provenance in RESEARCH-JOURNAL.md.
---

#### Apache Arrow - Columnar Analytics Performance

**Authors**: Apache Arrow Community & Users
**Date**: 2023-2024
**URL**: https://arrow.apache.org/powered_by/
**Evidence Level**: B (Adoption reference; cited page is a community powered-by list, not a benchmark — performance multipliers not substantiated there)
**Relevance**:
- ML training performance and data transfer
- Book Chapter (Advanced analytics)
- Best Practices Doc footnote [^266]

**Key Findings**:
- Broad production adoption across major platforms (Apache Spark, Dremio, VAST, ClickHouse, pandas, Polars, and others per powered_by list — Snowflake and Streamlit are no longer on the current list, verified 2026-07-10)
- Shared columnar in-memory format avoids the serialization and deserialization cost of moving data between systems (arrow.apache.org/overview/)
- VAST network telemetry: high-bandwidth path for security investigations (VAST is now Tenzir; the powered_by list still uses the old name)
- High-cardinality features (IP addresses, domains) optimized by columnar layout *(Not on the cited page or the Arrow overview, 2026-11-23; needs its own source.)*

**Citations**: Advanced analytics, data formats, security telemetry
**Notes**: Reference for adoption breadth; specific performance figures require per-platform benchmarks, not the powered_by page

**Validation Status**: ✅ Active URL (verified Apache Arrow official site)
**Refresh (2026-11-23)**: powered_by 200, adoption names re-read; current release apache-arrow-26.0.1 (2026-11-03).

**Validation (2026-06-05, folded)**: corrections applied to findings/tier above; provenance in RESEARCH-JOURNAL.md.
---

#### Champion-Challenger Model Pattern (MLOps Industry Standard)

**Authors**: MLOps Industry Practice (DataRobot, Dataiku, Capital One reference)
**Date**: 2020-06-19 (the cited DataRobot post's date, verified 2026-07-10; entry formerly said 2022-2024)
**URL**: https://www.datarobot.com/blog/introducing-mlops-champion-challenger-models/
**Evidence Level**: B (Industry methodology, widely adopted)
**Relevance**:
- ML model deployment patterns
- Book Chapter (Advanced analytics)
- Best Practices Doc footnote [^268]

**Key Findings**:
- Champion/challenger = A/B testing for ML models in production
- Parallel model comparison reduces deployment risk
- Standard MLOps pattern across financial services and security
- Enables safe model transitions without production disruption

**Citations**: Advanced analytics, deployment patterns, MLOps
**Notes**: Industry-standard pattern, methodology validated via DataRobot MLOps documentation

**Validation Status**: ✅ Active URL (verified DataRobot MLOps pattern documentation)

**Validation (2026-06-05, folded)**: corrections applied to findings/tier above; provenance in RESEARCH-JOURNAL.md.
---

#### Open Cybersecurity Alliance - Standards & Interoperability

**Authors**: Open Cybersecurity Alliance (OASIS Open Project to 2026-03-31; now an OASIS-governed community initiative)
**Date**: 2019-2026
**URL**: https://github.com/opencybersecurityalliance (re-pointed 2026-07-16 — opencybersecurityalliance.org is gone at the root per the 2026-07-16 link check; OCA was an OASIS Open Project until 2026-03-31 and its GitHub organization is the live canonical presence, 200 again on 2026-11-23)
**Evidence Level**: B (Industry standards consortium) — re-tiered from A 2026-08-19: neither peer-reviewed research nor an official standard
**Relevance**:
- Cybersecurity tool interoperability
- Book Chapter (Advanced analytics, integration)
- Best Practices Doc footnote [^269]

**Key Findings**:
- Standardized data interfaces for security tool interoperability
- Open ecosystem without custom integrations
- Builds tooling aligned with OASIS standards such as STIX: STIX Shifter, Kestrel, CACAO Roaster, IoB STIX extensions; the OpenDXL Ontology repos are archived
- Threat management lifecycle coverage
- Federated data operations

**Citations**: Advanced analytics, deployment standards, tool integration
**Notes**: OCA = community-led interoperability effort under OASIS governance; the OASIS Open Project model was sunset on 2026-03-31

**Validation Status**: ✅ Active URL (verified OCA official site) · Freshness (2026-06-05): publication date pre-2025 (>12mo) but freshness-triaged (date-stale; content NOT re-verified against source) in RESEARCH-JOURNAL.md (site real; interop framing holds). Stale-by-date, not by content.
**Refresh (2026-11-23)**: GitHub org 200, 28 repos, IoB and STIX Shifter pushed in Oct-Nov 2026. The OASIS Open Project was sunset 2026-03-31 per the archived oasis-open-project README, and OCA continues as an OASIS-governed community initiative without guaranteed staff support or funding. opencybersecurityalliance.org still does not answer.

---

#### MITRE Engenuity - ATT&CK Evaluations Framework

**Authors**: MITRE Engenuity
**Date**: 2019-2025 (ongoing program, updated February 2026)
**URL**: https://evals.mitre.org/
**Alt URL**: https://evals.mitre.org/enterprise/er7
**Evidence Level**: B (Framework authority, rigorous methodology) — re-tiered from A 2026-08-19: neither peer-reviewed research nor an official standard
**Relevance**:
- ML model evaluation standards and threat coverage
- Book Chapter (Advanced analytics)
- Best Practices Doc footnote [^272]

**Key Findings**:
- Rigorous, transparent methodology using threat-informed purple-teaming
- Assesses security product effectiveness against real-world threats
- ML capabilities tested (memory attacks, behavioral detection)
- Freely published results and emulation plans
- The "76% of enterprises use ATT&CK" figure formerly listed here is not on the evals site and was replaced 2026-07-09 — the verifiable adoption figure in this family is 81% general enterprise ATT&CK adoption (UC Berkeley CLTC/McAfee, 2020; Level B, dated)
- **2025 Enterprise Evaluation**: 11 vendors tested against Scattered Spider and Mustang Panda scenarios
- **Cloud/hybrid** environments added alongside traditional endpoints (identity abuse, cloud service misuse)
- Multiple vendors achieved 100% detection rates (CrowdStrike, Sophos, Cybereason) *(Unverified 2026-11-17: the cited page blocks automated readers, so this could not be re-read.)*

**Citations**: Advanced analytics, evaluation frameworks, threat coverage validation
**Notes**: Gold standard for security product evaluations; 2025 round added cloud/hybrid and identity-centric attack scenarios — reflects modern SOC requirements

**Validation Status**: ✅ Refreshed February 2026 - Enterprise 2025 results published · ⚠️ 1 figure unverified 2026-11-17, see the dated label

---

#### Microsoft - Concept Drift Detection & Monitoring

**Authors**: James Croft (Microsoft, FastTrack for Azure blog; page handle james_croft); security framing from Kuppa & Le-Khac 2022
**Date**: 2024-01-26 (updated 2024-02-22); arXiv paper 2022-06-15
**URL**: https://techcommunity.microsoft.com/blog/fasttrackforazureblog/identifying-drift-in-ml-models-best-practices-for-generating-consistent-reliable/4040531
**Evidence Level**: B (Vendor platform guidance + academic citation; quantified rate-of-drift claim removed)
**Relevance**:
- ML model maintenance and monitoring
- Book Chapter (Advanced analytics)
- Best Practices Doc footnote [^275]

**Key Findings**:
- Ever-evolving threat landscape creates non-stationary data — security ML requires active drift monitoring (from Kuppa & Le-Khac, arXiv 2206.07581; not stated in the Microsoft post)
- Azure Machine Learning provides tools for monitoring and managing model drift
- Four drift varieties: sudden, gradual, incremental, reoccurring
- Separate academic source: Kuppa & Le-Khac, "Learn to Adapt: Robust Drift Detection in Security Domain" (arXiv 2206.07581, 2022)

**Citations**: Advanced analytics, model maintenance, MLOps
**Notes**: Generic drift taxonomy from the Microsoft post; security-specific drift characteristics from arXiv 2206.07581 only

**Validation Status**: ✅ Updated February 2026 - URL format corrected to /blog/ path
**Refresh (2026-11-23)**: post 200; four-variety taxonomy read verbatim; the post has no security content, so the security claims are re-attributed to the arXiv paper, whose abstract carries them. Current Azure ML model-monitoring doc (ms.date 2026-01-27) lists data drift, prediction drift, data quality, feature attribution drift and model performance signals.

**Validation (2026-06-05, folded)**: corrections applied to findings/tier above; provenance in RESEARCH-JOURNAL.md.
---

#### Confluent - Machine Learning with Apache Kafka

**Authors**: Kai Waehner (Confluent)
**Date**: 2018-11-19 (page modified 2025-06-17)
**URL**: https://www.confluent.io/blog/using-apache-kafka-drive-cutting-edge-machine-learning/
**Evidence Level**: B (Vendor best practices, production patterns)
**Relevance**:
- Streaming feature computation
- Book ch02 §2.2 (components: collection and pipeline) [was: Chapter 7] (Streaming) + Advanced analytics
- Best Practices Doc footnote [^280]

**Key Findings**:
- KSQL (now ksqlDB) for feature engineering (filtering, enrichment, transformation)
- Kafka Streams embeds ML into microservices
- Kafka Streams or KSQL preprocessing in one pipeline that feeds both model training and in-stream inference (architecture described, parity not measured)
- ~~Current 2023: Building real-time ML apps on generative AI with Kafka Streams~~ (removed 2026-07-10 — the cited page is a single 2018-11-19 Kai Waehner post with no generative-AI content; the other findings verify against it)
- Vendor-described scalable ML architecture; names Uber, Netflix and PayPal platforms as examples but reports no measured results

**Citations**: ch02 §2.2 (components: collection and pipeline) [was: Chapter 7] + Advanced analytics integration, streaming ML architecture
**Notes**: Single 2018 post on Kafka + ML integration, links streaming to ML workflows

**Validation Status**: ✅ Active URL (single 2018 post)
**Refresh (2026-11-23)**: post 200; KSQL feature-engineering and Kafka Streams model-embedding lines read verbatim. Confluent's current documented path for in-stream inference is Flink SQL ML_PREDICT in Confluent Cloud (docs page 200), so the 2018 KSQL framing is historical.

---

## AI-Native Infrastructure & Emerging Architectures

### Reference Architectures & Implementation Patterns

#### Amazon Security Lake with Apache Iceberg

**Authors**: AWS Security Team
**Date**: February 2024 (updated February 2026)
**URL**: https://aws.amazon.com/about-aws/whats-new/2024/02/amazon-security-lake-analytics-ocsf-iceberg/
**Alt URL**: https://aws.amazon.com/security-lake/features/
**Evidence Level**: B (AWS production service, enterprise deployment) — re-tiered from A 2026-08-19: neither peer-reviewed research nor an official standard
**Relevance**:
- OCSF v1.1.0 integration with Apache Iceberg
- Production validation at scale
- Enterprise security data lake architecture

**Key Findings**:
- Native support for Apache Iceberg tables in Security Lake (February 2024)
- Automatic centralization from AWS environments, SaaS providers, on-premises
- Direct query support from Athena, Redshift, and third-party services — source is the Security Lake user guide (docs.aws.amazon.com/security-lake/latest/userguide/what-is-security-lake.html, verbatim "You can also query data by using Amazon Athena, Amazon Redshift…"), NOT the cited announcement or the features page, neither of which mentions the query engines (repointed 2026-07-10; the part-2 sweep's own features-page suggestion was checked and refuted)
- **OCSF v1.1.0 Observables** for threat intel matching and identity search across environments
- Note: 3× query / 10× TPS figures are from Amazon S3 Tables (December 2024 announcement), not Security Lake itself

**Citations**: OCSF integration, Iceberg performance, security data lake
**Notes**: Major cloud provider validation of Iceberg + OCSF for security; AppFabric and partner-count claims require separate sourcing

**Validation Status**: ✅ Refreshed February 2026 - Active production service with expanding partner ecosystem
**Currency (2026-11-17)**: the OCSF v1.1.0 mention describes the schema version Security Lake was built on; the current OCSF schema release is v1.9.0 (https://github.com/ocsf/ocsf-schema/releases, published 2026-08-03), so check Security Lake's documentation for the version it supports today before citing.
**Refresh (2026-11-23)**: the current OCSF release is now v1.10.0 (2026-11-20, https://github.com/ocsf/ocsf-schema/releases/tag/1.10).

**Validation (2026-06-05, folded)**: corrections applied to findings/tier above; provenance in RESEARCH-JOURNAL.md.
---

#### StarRocks vs ClickHouse Production Benchmarks

**Authors**: Multiple vendors and practitioners
**Date**: 2024-2025
**URL**: https://docs.starrocks.io/docs/benchmarking/SSB_Benchmarking/ (vendor-run SSB flat-table benchmark)
**Alt URL**: https://www.tinybird.co/blog/clickhouse-vs-starrocks (vendor comparison, architecture and workload trade-offs)
**Evidence Level**: B (Vendor-run benchmarks with disclosed methodology; interpret with vendor-bias caveat)
**Relevance**:
- Query engine selection for security analytics
- Performance under high concurrency
- Real-time update capabilities

**Key Findings**:
- StarRocks reports overall query performance 1.87× that of ClickHouse across the 13 queries of the 100 GB SSB flat-table benchmark (StarRocks' own benchmark page, vendor-run, flag bias; re-read 2026-11-17)
- StarRocks shows multi-engine advantages on TPC-H (benchmarked vs Trino/Spark, not ClickHouse directly — ClickHouse comparison weaker)
- *Removed 2026-11-17: a "sub-second P95 latency with 100× more concurrent sessions" claim, which names no primary and was not found at either source above.*
- ClickHouse excels at single-table queries on flat schemas
- StarRocks better for high-concurrency production (hundreds of users)
- *Removed 2026-11-17: a "~30K pull requests in 2025" count, which names no primary.*

**Citations**: Query engine benchmarks, production deployment patterns
**Notes**: Critical for LIGER Stack "E" (Engine) component selection

**Validation Status**: ⚠️ Vendor-run benchmarks; the 1.87× figure verified at the StarRocks page 2026-11-17, two unsourced numbers removed the same day

**Validation (2026-06-05, folded)**: corrections applied to findings/tier above; provenance in RESEARCH-JOURNAL.md.
---

#### MOAR Stack - Security Data Lakehouse Reference Architecture

**Authors**: Jeremy Wiley (FIRST-PARTY — the author's own reference architecture + cost model, not third-party evidence)
**Date**: October 2025 (renamed from "LIGER" → "MOAR", an intentional rebrand)
**URL**: https://securitydataworks.com/thesis/moar
**Cost-model source**: https://securitydataworks.com/engagements/moar-architecture-design/economics — the transparent $3,560/mo-at-500GB/day cost model with its assumptions stated (the cost figures below live HERE, not on /thesis/moar)
**Evidence Level**: B (first-party model with disclosed assumptions; relabeled from A — self-authored, not external validation)
**⚠️ Update needed (2026-06-05)**: the L-I-G-E-R 5-letter component breakdown below is the retired naming; reconcile to the current MOAR component model on /thesis/moar.
**Relevance**:
- Complete reference architecture for security data lakehouse
- Alternative to traditional SIEM platforms
- Cost reduction strategies

**Key Findings**:
- **L**akehouse (Iceberg) + **I**ndex (Polaris) + **G**raph (Grafana) + **E**ngine (StarRocks) + **R**oute (Cribl/Tenzir)
- 70-90% cost reduction vs traditional SIEMs ($3,560/month vs $31-100K/month for 500GB/day) *(Unverified 2026-11-17: 70-90% and $31-100K are not on the cited securitydataworks.com pages.)*
- 10-12× compression with Parquet/ZSTD reducing 1TB/day to <$700/month storage *(Unverified 2026-11-17: not on the cited securitydataworks.com pages.)*
- Separation of storage ($0.023/GB/month S3) and compute (scale independently)
- Vendor-neutral architecture (20+ query engines supported via Iceberg) *(Unverified 2026-11-22: not on the cited securitydataworks.com pages.)*
- Fixed compute costs regardless of query volume (vs per-query SIEM charges)
- Supports both pipeline-based detection (real-time, 10-50× cost reduction) and query-based (retroactive analysis) *(Unverified 2026-11-17: not on the cited securitydataworks.com pages.)*

**Design Principles**:
1. Vendor-neutral data layer (open table formats)
2. Separation of storage and compute
3. Compression-first design (10-12× typical)
4. Schema evolution without breaking changes
5. Query engine specialization (right tool for workload)

**Implementation Timeline**: 12 months across 4 phases *(Unverified 2026-11-17: not on the cited securitydataworks.com pages.)*
- Phase 1 (Months 1-3): Lakehouse foundation
- Phase 2 (Months 4-6): Real-time engine
- Phase 3 (Months 7-9): Transformation pipeline
- Phase 4 (Months 10-12): Semantic layer (optional)

**Citations**: Reference architecture, cost optimization, SIEM replacement
**Notes**: **CRITICAL** - First complete, production-validated security data lakehouse architecture with detailed cost modeling

**Validation Status**: ✅ Production deployments referenced · ⚠️ 7 figures unverified 2026-11-17 (the 20+ and 1TB figures added 2026-11-22), see the dated labels

---

### AI Governance & Agent Architectures

#### Evaluating Goal Drift in Language Model Agents (arXiv 2505.02709)

**Authors**: Rauno Arike, Elizabeth Donoway, Henning Bartsch, Marius Hobbhahn (MATS; Apollo Research)
**Date**: May 2025 (arXiv:2505.02709v1, 5 May 2025)
**URL**: https://arxiv.org/abs/2505.02709
**Evidence Level**: B (technical report; empirical, not a peer-reviewed venue)
**Relevance**:
- Agentic security (H-AGENT-SECURITY-01): even initially well-specified goals can shift as an LM agent accumulates context and meets competing objectives over a long horizon.
- Finding: a scaffolded Claude 3.5 Sonnet maintained nearly perfect goal adherence for more than 100,000 tokens in the hardest setting, while all evaluated models showed some goal drift, and drift correlated with rising susceptibility to pattern-matching as context length grew.
- Supports the constrained-inference / deterministic-verifiability positioning: long-horizon autonomy degrades, which is an argument for verifiable checks around any agent acting on security data.
**Notes**: Verified 2026-06-30 from the paper PDF (title, authors, abstract). The 100k-token figure is the paper's own reported result, not independently reproduced.
**Validation Status**: ✅ Verified 2026-06-30 (PDF title/authors/abstract).

---

#### Security Challenges in AI Agent Deployment: Insights from a Large Scale Public Competition (arXiv 2507.20526)

**Authors**: Andy Zou, Maxwell Lin, Eliot Jones, Micha Nowak, Mateusz Dziemian, Nick Winter, Alexander Grattan, Valent Nathanael, Ayla Croft, Xander Davies, Jai Patel, Robert Kirk, Nate Burnikell, Yarin Gal, Dan Hendrycks, J. Zico Kolter, Matt Fredrikson
**Date**: July 2025 (arXiv:2507.20526v1, 28 Jul 2025; no later version listed as of 2026-11-07)
**URL**: https://arxiv.org/abs/2507.20526
**Evidence Level**: B (preprint; large-scale empirical red-teaming competition, not a peer-reviewed venue)
**Relevance**:
- Agentic security (H-AGENT-SECURITY-01) and the "capability isn't safety" argument: participants "submitted 1.8 million prompt-injection attacks, with over 60,000 successfully eliciting policy violations", "targeting 22 frontier AI agents across 44 realistic deployment scenarios", and the authors "find limited correlation between agent robustness and model size, capability, or inference-time compute".
- "Nearly all agents exhibit policy violations for most behaviors within 10-100 queries", which is the scale-of-attempts argument for deterministic gates around agents rather than reliance on model robustness; it pairs with AgentDojo, which the site already cites.
- Found via the [un]prompted March 2026 Stripe deck (Bullen, p3), which shows only the paper title; the arXiv ID and figures were read at arxiv.org, not taken from the slide.
**Notes**: Verified 2026-11-07 from the arXiv abstract page (title, 17 authors, v1 date, the quoted abstract sentences). Full paper not read; the robustness-vs-capability finding is the authors' own result.
**Validation Status**: ✅ Verified 2026-11-07 (arXiv abstract page).

---

#### Adaptive Monitoring and Real-World Evaluation of Agentic AI Systems (arXiv 2509.00115)

**Author**: Manish A. Shukla (Independent Researcher, Plano, TX)
**Date**: August 2025 (arXiv:2509.00115v3, 13 Sep 2025)
**URL**: https://arxiv.org/abs/2509.00115
**Evidence Level**: B (independent technical report; simulations plus experiments, not a peer-reviewed venue)
**Relevance**:
- The measurement-imbalance finding grounds the "capability isn't safety" argument: a systematic review of 84 papers (2023–2025) found about 83% report capability metrics while only about 30% consider human-centred or economic axes.
- Proposes AMDM (Adaptive Multi-Dimensional Monitoring): per-axis exponentially-weighted thresholds with joint anomaly detection via Mahalanobis distance; reported to cut anomaly-detection latency from 12.3 s to 5.6 s and the false-positive rate from 4.5% to 0.9% versus static thresholds.
- Relevant to monitoring agentic AI in security operations and to the AI-maturity / safety-half framing.
**Notes**: Verified 2026-06-30 from the paper PDF. The latency and false-positive numbers are the paper's own simulated results, not independently reproduced.
**Validation Status**: ✅ Verified 2026-06-30 (PDF title/author/abstract).

---

#### Governing Evolving Memory in LLM Agents — SSGM Framework (arXiv 2603.11768)

**Authors**: Chingkwun Lam, Jiaxin Li, Lingfei Zhang, Kuo Zhao (Jinan University, College of Intelligent Science and Engineering)
**Date**: May 2026 (arXiv:2603.11768v2, 19 May 2026)
**URL**: https://arxiv.org/abs/2603.11768
**Evidence Level**: C (conceptual governance framework, no empirical evaluation; post-cutoff publication — verify before relying on it)
**Relevance**:
- Agentic security (H-AGENT-SECURITY-01): mutable agent memory introduces a stability-plasticity dilemma, where facts distort through iterative summarization (semantic drift), workflows degrade (procedural drift), and hallucinations or injections get internalized as valid knowledge, with errors that are cumulative and persistent rather than isolated to one retrieval step.
- Proposes SSGM (Stability and Safety-Governed Memory): decouples memory evolution from execution by enforcing consistency verification, temporal decay modeling, and dynamic access control before any memory consolidation.
- A framing source for the agentic-security angle: governing what an agent is permitted to remember about security telemetry.
**Notes**: Verified 2026-06-30 from the paper PDF (title, authors, abstract). Conceptual, with no empirical results; post-cutoff publication, so confirm at arXiv before relying on it in a publication.
**Validation Status**: ✅ PDF verified 2026-06-30; conceptual framework, no empirical evaluation.

---

#### OpenSec: Measuring Incident Response Agent Calibration Under Adversarial Evidence (arXiv 2601.21083)

**Authors**: Jarrod Barnes (independent)
**Date**: 2026 (arXiv:2601.21083; v1 2026-01-28, v3 2026-02-06)
**URL**: https://arxiv.org/abs/2601.21083
**Evidence Level**: B (Independent-authored arXiv preprint with open code + datasets; execution-based benchmark, not peer-reviewed or a standard)
**Relevance**:
- Research Question RQ14 (Agentic security automation — restraint/calibration under adversarial evidence)
- Research Question RQ12 (AI/agent governance maturity)
- Book chapter on agentic SOC / AI governance

**Key Findings** (verbatim from the arXiv primary, 2026-07-09):
- Four frontier models, 40 standard-tier episodes each; consistent over-triggering (agents act before gathering sufficient evidence)
- GPT-5.2: executes containment in 100% of episodes at 82.5% false-positive rate, acting at step 4
- Claude Sonnet 4.5: partial calibration (62.5% containment, 45% FP, time-to-first-containment 10.6)
- All models correctly identify the ground-truth threat when they act — the calibration gap is in restraint, not detection
- Open-source env (github.com/jbarnes850/opensec-env) + public datasets (huggingface.co/datasets/Jarrodbarnes/opensec-seeds)

**Citations**: RQ14 measured counter-evidence to "autonomous SOC" hype — quantifies premature action when agents are given authority to act
**Notes**: Independent single-author preprint with reproducible code/data. The skeptical, measured framing is the counterweight RQ14 needs against vendor ROI claims; Tier B (not peer-reviewed, not production).

**Validation Status**: ✅ Verified 2026-07-09 (arXiv abstract + figures confirmed at primary)

---

#### Gartner AI Maturity and Success Metrics

**Authors**: Gartner Research
**Date**: 2024-2025
**URL**: https://www.gartner.com/en/newsroom/press-releases/2024-07-29-gartner-predicts-30-percent-of-generative-ai-projects-will-be-abandoned-after-proof-of-concept-by-end-of-2025 (press release, 2024-07-29; the page blocks automated fetches, and the 30% prediction is its headline)
**Evidence Level**: B (Analyst prediction; headline maturity-correlation and abandonment figures not traceable to any Gartner publication)
**Relevance**:
- AI maturity correlation with success rates
- Organizational readiness metrics
- Long-term sustainability patterns

**Key Findings**:
- Gartner (July 2024) predicted ~30% of GenAI projects would be abandoned after PoC by end-2025, citing poor data quality and unclear business value as primary drivers
- Note: Previously cited maturity-tier percentages (45%/20%/60% sustainability, 42% abandoned, 81%/45% agent figures) are not traceable to any Gartner publication and have been removed; the "42% abandoned" figure is a 2025 S&P Global statistic, not Gartner

**Citations**: AI maturity models, governance requirements, failure rates
**Notes**: Retain for the ~30% PoC-abandonment prediction only; re-source or remove maturity-tier quantification

**Validation Status**: ⚠️ The 30% figure appears in the press release's URL; the page blocks automated readers and its text was not re-read on 2026-11-17 or 2026-11-22, so the "~30%" wording and the drivers clause should be re-read in a browser before they are relied on · 1 figure unverified

**Validation (2026-06-05, folded)**: corrections applied to findings/tier above; provenance in RESEARCH-JOURNAL.md.
---

#### AI Governance Maturity Gate - Prerequisites for AI Success

**Authors**: Benjamin Rogojan (Seattle Data Guy), John Wernfeldt
**Date**: December 2025
**URL**: LinkedIn professional discourse
**Evidence Level**: B (Practitioner consensus, multiple independent sources)
**Relevance**:
- AI initiative failure patterns
- Data governance prerequisites
- Organizational readiness assessment

**Key Findings**:
- AI initiatives fail at organizations already struggling with data governance
- *Removed 2026-11-17: the "10× amplification", "<5% success at Level 1" and "70-85% success at Level 4" figures and a quoted "6 months" line. The entry's only source is unnamed LinkedIn discussion, which this review does not fetch, so none of them has a primary.*

**Citations**: AI implementation reality, governance prerequisites
**Notes**: Practitioner opinion with no citable primary, so do not cite this entry for any claim.

**Validation Status**: ⚠️ No primary (LinkedIn discussion, not fetched); numbers removed 2026-11-17

---

#### RAPTOR Security Automation Framework - Production AI Patching

**Authors**: Gadi Evron, Daniel Cuthbert, Thomas Dullien, Michael Bargury, John Cartwright (author list per the repository README, checked 2026-11-17)
**Date**: December 2025
**URL**: https://github.com/gadievron/raptor (originally announced on LinkedIn)
**Evidence Level**: B (Production demonstration, "duct tape MVP")
**Relevance**:
- Agentic security automation
- Vulnerability remediation
- Practical AI deployment

**Key Findings**:
- Chains static analysis, binary analysis, LLM-assisted vulnerability validation, exploit generation and patch writing into one workflow (README)
- *Unverified 2026-11-17: the FFmpeg patch result came from the LinkedIn announcement and is not in the repository README.*
- Openly acknowledges "duct tape MVP" architecture
- Demonstrates practical AI agent implementation for security
- "Embarrassingly simple" infrastructure that actually works
- Represents "Perl/CGI era" of AI security automation

**Citations**: Agentic security patterns, practical AI deployment
**Notes**: The README describes itself as "held together with enthusiasm and duct tape". The earlier "first public example of AI successfully patching vulnerabilities" claim had no primary and was dropped 2026-11-17.

**Validation Status**: ⚐ Public demonstration (December 2025) · ⚠️ 1 claim unverified 2026-11-17, see the dated label

---

#### NANDA - Infrastructure for Internet of AI Agents

**Authors**: Ramesh Raskar (MIT Media Lab)
**Date**: 2024-2025
**URL**: https://nanda.media.mit.edu/, https://arxiv.org/pdf/2507.14263
**Evidence Level**: B (MIT research, 10 years development, arXiv paper) — re-tiered from A 2026-08-19: not peer-reviewed research and not an official standard
**Relevance**:
- Agent infrastructure for security operations
- Decentralized agent registry ("DNS for agents")
- Agent authentication and discovery

**Key Findings**:
- Provides foundational infrastructure for trillions of AI agents
- Decentralized registry solving identity, discovery, coordination at scale
- Builds on Anthropic's Model Context Protocol (MCP) — supported by the companion arXiv paper (see the "NANDA Index in Practice" entry, verified 2026-07-10)
- Open governance model with modular stack

**Citations**: Agent infrastructure, security architecture for AI systems
**Notes**: **CRITICAL** - Security operations will require agent-to-agent coordination. NANDA provides infrastructure layer. Correction (2026-07-10, part-2 sweep fix 16): the "1,000+ agents via Join39", "MLflow + NANDA integration (Databricks validation)", and Google-A2A bullets were removed — none appear on the MIT overview page (browser-checked 2026-07-10; the page is a light group overview) or in the arXiv abstract; the site still advertises the April 2025 summit, so treat its content as stale. Re-add individually if primaries surface.

**Validation Status**: ✅ MIT page live (browser-verified 2026-07-10; redirects to media.mit.edu/groups/nanda/overview); arXiv leg live

---

#### AI-Generated Security Parsers - Tenzir MCP Implementation

**Authors**: Jannis Köhl (Tenzir) — byline browser-verified 2026-07-10; entry formerly credited Vallentin
**Date**: 2025-08-21 (v0.1 announcement; entry formerly said November-December 2025)
**URL**: https://tenzir.com/blog/announcing-the-tenzir-mcp-server-ai-generated-ocsf-mappings
**Alt URL**: https://tenzir.com/blog/ai-generated-integrations-the-end-of-vendor-lock-in (Tenzir MCP Server v0.4.0, 2025-11-10)
**Evidence Level**: B (Production demonstration, vendor implementation)
**Relevance**:
- Automated parser generation
- OCSF normalization automation
- Vendor independence

**Key Findings**:
- AI generates security data parsers / OCSF mappings from log samples
- v0.1 announcement (cited URL) describes the generated mappings as "100% schema-conforming"
- v0.4.0 post (Alt URL, 2025-11-10): "turns a single log sample into a complete, tested, production-ready Tenzir package with both parsing and OCSF mapping—100% hands-off-keyboard" — the "hands-off-keyboard" and "tested, production-ready packages" claims removed 2026-06-05 as unsourced were in THIS later post, not the v0.1 announcement; restored 2026-07-10 with the correct source
- Shifts power dynamic from vendors to customers ("The integration power dynamic between vendors and security teams just flipped" — v0.4.0 post verbatim)
- Commoditizes parser development

**Citations**: AI automation, OCSF integration, parser generation
**Notes**: Correction (2026-07-10, part-2 sweep fix 17): re-dated and re-attributed — the cited URL is the v0.1 announcement (2025-08-21, Jannis Köhl), and the former "Production deployment validated (December 2025)" claim was dropped as absent from it. The two-post split resolves the 2026-06-05 correction's puzzle: the strong claims belong to the v0.4.0 post, now cited as Alt URL. Eliminates vendor roadmap dependency for integrations.

**Validation Status**: ✅ Both posts browser-verified at primary 2026-07-10

---

### Pipeline Detection vs Query-Based Analytics

#### Tenzir Security Data Pipeline Platform

**Authors**: Tenzir Team
**Date**: 2024 (live page read 2026-11-23; 30% figure and the two phrases below archived 2026-06-17)
**URL**: https://tenzir.com/product/comparisons/cribl/
**Evidence Level**: C (Vendor self-claim on comparison page; no independent methodology disclosed)
**Relevance**:
- Pipeline-based detection architecture
- Cost reduction strategies
- Unified platform vs fragmented tools

**Key Findings**:
- Tenzir's comparison page claimed 30% lower TCO vs Cribl's pipeline-plus-separate-SIEM model as of the 2026-06-17 Wayback snapshot and claims 50% lower TCO, 75% fewer tools and 2x faster threat detection on the live page (2026-11-23); vendor self-claims, no methodology, baseline is Cribl's combined stack and not query-based architectures generally
- In-stream detection in the pipeline, which Tenzir says Cribl Stream lacks (live wording; the "shifting detection left" phrase is on the 2026-06-17 snapshot and gone from the live page)
- Single platform eliminates separate SIEM layer costs (wording from the 2026-06-17 snapshot; the live page folds this into its 50% TCO line)
- Open-source engine (tenzir/tenzir, C++, BSD-3-Clause) with a commercial platform
- Deploys in minutes with single lightweight binary
- Unified detection workflow vs Cribl's fragmented suite (Stream, Search, Lake on the live page; the 2026-06-17 snapshot also listed Edge)

**Citations**: Pipeline detection economics, TCO reduction, architecture simplification
**Notes**: Validates RQ13 pipeline vs query detection economics hypothesis; cite with vendor-bias caveat

**Validation Status**: ⚠️ Vendor comparison page whose claims changed between 2026-06-17 and 2026-11-23; no documented deployments on the page
**Refresh (2026-11-23)**: live page re-read; the TCO claim moved from 30% to 50%, and the 30% line, the shift-left phrase and the separate-SIEM line are confirmed in the 2026-06-17 Wayback snapshot. Single-binary deploy claim verbatim. Engine language and license checked on GitHub.

**Validation (2026-06-05, folded)**: corrections applied to findings/tier above; provenance in RESEARCH-JOURNAL.md.
---

#### Security Data Pipeline Market Guide 2025

**Authors**: Software Analyst Cyber Research (SACR)
**Date**: 2025-04-21 (byline verified at primary 2026-07-10; entry formerly said February 2025)
**URL**: https://softwareanalyst.substack.com/p/market-guide-2025-the-rise-of-security
**Evidence Level**: B (Industry analyst report with vendor data)
**Relevance**:
- RQ13: Pipeline vs query detection economics
- Security data pipeline market sizing
- SIEM cost pressure quantification

**Key Findings**:
- Cribl crossed $200M ARR in Feb 2025 (one of fastest to $100M ARR behind only Wiz, HashiCorp, Snowflake)
- Log reduction "often uses rules or machine learning to identify redundant events and reduce volume by 80% or more" (page verbatim, general claim); Axoflow-specific "reported log volume reductions of 25–70%, especially for verbose logs like Windows" — the entry's former blended "50-70%" figure appears nowhere on the page (corrected 2026-07-10)
- SIEM ingestion volume reducible by 80%+ with pipeline processing
- Security telemetry doubling every ~18 months; organizations use 40-50+ security tools
- SIEMs evolving from monolithic to modular "query layer" with separate storage
- Pipelines becoming "control plane" of modern SOC architecture
- Traditional volume-based SIEM pricing "economically unsustainable"

**Citations**: Pipeline detection economics, SIEM cost reduction, market evolution
**Notes**: Validates RQ13 hypothesis - quantifies why pipeline-first approach wins economically; Cribl's $200M ARR validates market demand; Tier B because analyst report (not peer-reviewed) but well-sourced with vendor data

**Validation Status**: ✅ Added February 2026

---

#### Rippling - Engineering a Cost-Effective SIEM (3-Part Series)

**Authors**: Rippling Security Engineering Team
**Date**: 2025
**URL**: https://www.rippling.com/blog/engineering-siem-part-3
**Alt URLs**: https://www.rippling.com/blog/engineering-siem-part-1, https://www.rippling.com/blog/engineering-siem-part-2
**Evidence Level**: B (Production deployment with quantitative cost data) — re-tiered from A 2026-08-19: not peer-reviewed research and not an official standard
**Relevance**:
- RQ13: Pipeline vs query detection economics
- Security data lakehouse architecture
- Cost-per-detection quantification

**Key Findings**:
- CloudTrail detection cost: $4.50/month (1.8 Snowflake credits) per detection rule
- Detection scans 50-70 MB every 5 minutes via log clustering optimization
- 75GB/month log ingestion: $31-34/month (Snowpipe + AWS combined)
- Ingestion latency <1 minute via Snowpipe near-real-time delivery
- Serverless detection eliminates pre-provisioned warehouse overhead
- Adding a new detection = "nominal expense increase" via serverless architecture
- Search optimization reduces query time by "several dozen times" on VARIANT columns
- Security data lakehouse on Snowflake + S3 for extended retention

*Unverified 2026-11-17: the 50-70 MB, 5-minute, 75 GB and under-1-minute figures could not be re-read, because rippling.com blocks automated readers.*

**Citations**: Detection cost modeling, serverless SIEM architecture, pipeline economics
**Notes**: First quantitative cost-per-detection data found for RQ13; validates query-based approach with Snowflake serverless can be cost-effective at $4.50/month/rule; counterpoint to pipeline-first hypothesis

**Validation Status**: ✅ Added February 2026 · ⚠️ 4 figures unverified 2026-11-17, see the dated labels

---

#### Monad - Detection Engineering Guide to Cutting SIEM Costs

**Authors**: Monad Security Team
**Date**: 2025
**URL**: https://www.monad.com/blog/a-detection-engineers-guide-to-cutting-siem-costs
**Evidence Level**: B (Quantitative cost analysis with production data) — re-tiered from A 2026-08-19: not peer-reviewed research and not an official standard
**Relevance**:
- RQ13: Pipeline vs query detection economics
- SIEM cost optimization
- Data pipeline filtering economics

**Key Findings**:
- Okta case study: 50.7% cost reduction ($1,929→$952/month) via pipeline filtering
- Annual savings of $11,721 per 1M daily Okta events
- Event size reduction: 2,570→1,545 bytes (40% field reduction)
- 180,000 low-value events/day filtered from SIEM (18% of 1M total)
- SIEM ingestion licensing: ~$25/GB/day; S3 archival storage: $0.023/GB/month (an ingest-licensing rate and a storage rate respectively, so the two are not commensurable and no cost multiple is derived from them; the previously stated 1,087× mixed the units and was struck 2026-07-12)
- 3-year savings: $35,181 per log source optimized
- Pipeline filtering preserves investigation capability via S3 archival

**Citations**: Detection engineering cost optimization, pipeline filtering ROI
**Notes**: Validates RQ13 hybrid approach - pipeline filtering + tiered storage achieves 50%+ cost reduction per log source while maintaining compliance; quantitative production data strengthens evidence

**Validation Status**: ✅ Added February 2026

---

#### Contentsquare - Elasticsearch to ClickHouse Migration

**Authors**: Ryad Zenine (Contentsquare engineer; guest post on the ClickHouse blog)
**Date**: 2022-10-11
**URL**: https://clickhouse.com/blog/contentsquare-migration-from-elasticsearch-to-clickhouse
**Evidence Level**: B (first-person practitioner authorship on a vendor channel — B-with-curation-caveat per the 2026-07-10 vendor-channel tier rule; ClickHouse selected and hosts the piece)
**Relevance**:
- Book ch02 cost-corroboration footnote (general log/product-analytics migration, held apart from the security-workload set)

**Key Findings**:
- "ClickHouse turned out to be 11 times cheaper (in infrastructure cost) and allowed us to have a 10x performance improvement in our p99 for queries" (page verbatim)

**Citations**: ch02 [^cost-corroboration-ch2]
**Validation Status**: ✅ Verified at primary 2026-07-10 (part-2 follow-up, 5-agent cite hunt); author affiliation cross-checked
**Refresh (2026-11-23)**: page 200; the 11x cost and 10x p99 sentence re-read verbatim, byline Ryad Zenine, published 2022-10-11 (page modified 2026-03-03, figures unchanged).

---

#### Didi - Elasticsearch to ClickHouse Log Storage Migration

**Authors**: Yuankai Zhong (Didi engineer; translated from Didi Tech, republished on the ClickHouse blog)
**Date**: 2024-04-19
**URL**: https://clickhouse.com/blog/didi-migrates-from-elasticsearch-to-clickHouse-for-a-new-generation-log-storage-system
**Evidence Level**: B (named practitioner authorship, vendor-hosted translation — B-with-curation-caveat per the 2026-07-10 vendor-channel tier rule)
**Relevance**:
- Book ch02 cost-corroboration footnote (general log-analytics migration, held apart from the security-workload set)

**Key Findings**:
- "Compared to Elasticsearch, the machine cost of ClickHouse has decreased by 30%" (page verbatim); query speed "improved by about 4 times"

**Citations**: ch02 [^cost-corroboration-ch2]
**Validation Status**: ✅ Verified at primary 2026-07-10
**Refresh (2026-11-23)**: re-fetched at the same URL (HTTP 200), and both quoted figures are still on the page verbatim ("the machine cost of ClickHouse has decreased by 30%", query speed "improved by about 4 times"). The post is still dated 19 April 2024. A search for a 2025 or 2026 follow-up by Didi found none. The figure is a hardware-cost reduction for a general logging workload, not a security one, which matches how ch02 holds it apart.

---

#### Cloudflare - Log Analytics using ClickHouse

**Authors**: Monika Singh and Pradeep Chhetri (Cloudflare engineers; adapted from their Monitorama PDX 2022 talk)
**Date**: 2022-09-02
**URL**: https://blog.cloudflare.com/log-analytics-using-clickhouse/
**Evidence Level**: B (named practitioners describing their own org's internal system on their own engineering blog)
**Relevance**:
- Book ch02 cost-corroboration footnote (general log-analytics migration, held apart from the security-workload set)

**Key Findings**:
- "Each Elasticsearch document which used 600 bytes, came down to 60 bytes per row in ClickHouse" (page verbatim — a 90% per-document storage reduction)
- "CPU and memory consumption on the inserter side were reduced by eight times" (page verbatim)
- **The page carries NO cost-reduction percentage and no dollar figures** — the "Cloudflare 85-90% cost reduction" sometimes attributed to this migration is a phantom (traced 2026-07-10 to a third-party dev.to post about an unnamed crypto-derivatives platform that cited Cloudflare in passing); cite the storage/compute figures only, framed as storage/compute

**Citations**: ch02 [^cost-corroboration-ch2] (which correctly frames it as 8x compute / 10x per-document storage)
**Validation Status**: ✅ Verified at primary 2026-07-10 (fetched twice, second pass scanning specifically for cost/percentage/dollar language — none found)
**Refresh (2026-11-23)**: re-fetched (HTTP 200), and the 600-bytes-to-60-bytes and eight-times inserter figures are verbatim on the page. A third scan for cost language found percentages only in operational contexts (0.1%, 1%, 10%, 99%, 100%) and no dollar figures, so the phantom "85-90% cost reduction" note still holds. A search found no 2025 or 2026 Cloudflare follow-up on this logging pipeline. The nearest newer Cloudflare data-pipeline posts (Jetflow, July 2025) describe a different system and are not substitutes.

---

#### Navan - SIEM-less Detection Engineering (Anvilogic Case Study)

**Authors**: Anvilogic (vendor case study quoting Prabhath Karanth, Global Head of Security & Trust, Navan)
**Date**: Undated page (likely 2023-2024; the related Snowflake Ventures post on the same partnership is 2024-05-21)
**URL**: https://web.archive.org/web/20260720190353/https://www.anvilogic.com/case-studies/navan [Archived] (Wayback Machine snapshot of the case-study page, which returns HTTP 404 at its original address, www.anvilogic.com/case-studies/navan, as of 2026-11-23)
**Evidence Level**: C (vendor-authored case study quoting a practitioner — C per the 2026-07-10 vendor-channel tier rule; flag marketing bias)
**Relevance**:
- Book ch02 cost-corroboration footnote (security-workload outcome)

**Key Findings**:
- "By using a detection engineering platform on top of our data lake, we are able to achieve some significant efficiencies in our overall SOC and IR operations, which can equate to cost savings of close to 70–80%" (Karanth, page verbatim) — a SOC/IR operating-cost figure, not a SIEM-bill figure; baseline and ingest volume unnamed

**Citations**: ch02 [^cost-corroboration-ch2]
**Validation Status**: ✅ Verified at the case-study page 2026-07-10; no publication date on page, not in Wayback. On 2026-11-17 the page returned 404 to an automated fetch but is still indexed by search engines with the same 70–80% wording, so it is recorded as live-but-unconfirmed rather than dead
**Refresh (2026-11-23)**: the page returned HTTP 404 again on 2026-11-23, this time to a browser-header request as well as to the link checker, so the entry is marked Archived. The Wayback Machine does hold a copy (snapshot 2026-07-20), and that copy carries the Karanth quote above verbatim, including "cost savings of close to 70–80%", so the 2026-07-10 note that the page was not in Wayback no longer holds. The snapshot is now the URL above. The same snapshot's headline and body restate the figure more firmly than Karanth does ("Navan saved 70-80% in cost", "Navan has achieved 70-80% cost savings and saved over 15K hours"); those are Anvilogic's words, not his, and are not cited.

---

#### Rivian - SIEM Cost Reduction on Databricks

**Authors**: Taylor Kain, Dave Herrald, Omar Khawaja (Databricks; vendor blog quoting Chris Mandich, Director of Cybersecurity Operations, Rivian)
**Date**: 2025-09-30
**URL**: https://www.databricks.com/blog/transforming-cybersecurity-data-intelligence
**Evidence Level**: C (vendor-authored post quoting a practitioner — C per the 2026-07-10 vendor-channel tier rule; flag testimonial selection bias)
**Relevance**:
- Book ch02 cost-corroboration footnote (security-workload outcome; read against the A.6 model's 92-96% projection at Rivian's scale, it undershoots)

**Key Findings**:
- "Lowering our SIEM costs by 60% while migrating 7–10TB of daily data from over 100 sources in under four months was only possible because Databricks gave us full control, scalability, and real-time detection" (Mandich, page verbatim)

**Citations**: ch02 [^cost-corroboration-ch2]
**Validation Status**: ✅ Verified at primary 2026-07-10 (quote and attribution re-confirmed twice)

---

#### SOC Automation ROI and AI Implementation

**Authors**: KPMG, Fortinet, Prophet Security
**Date**: 2024-2025
**URL**: https://www.securityinfowatch.com/ai/article/55315748/prophet-security-report-highlights-urgent-need-for-ai-in-socs (trade-press report of a Prophet Security vendor survey of nearly 300 security leaders)
**Evidence Level**: B (Partial industry-survey support; two headline stats unverifiable)
**Relevance**:
- SOC automation return on investment
- AI implementation challenges
- Level 1 analyst task automation

**Key Findings**:
- 40% of alerts go uninvestigated without automation (Prophet Security, via securityinfowatch.com)
- *Removed 2026-11-17: a "SOAR market reaching $2.3 billion by 2025 (16.3% CAGR)" figure, which names no primary.*
- AI triage can boost effectiveness in mature SOC deployments
- *Unverified 2026-11-17: an "autonomous SOC standard within 1-2 years" expectation, which names no primary.*

**Citations**: SOC automation metrics, AI implementation challenges, ROI data
**Notes**: Validates RQ14 agent automation ROI hypothesis. Fortinet "11 min" and KPMG "24%" claims could not be verified in primary sources and have been removed.

**Validation Status**: ⚠️ The 40% figure verified at the securityinfowatch report 2026-11-17 (vendor survey, flag bias); market-size figure removed · ⚠️ 1 claim unverified 2026-11-17, see the dated label

**Validation (2026-06-05, folded)**: corrections applied to findings/tier above; provenance in RESEARCH-JOURNAL.md.
---

#### Tenzir Streaming Fabric - Policy vs. Pipe Layer Framework

**Authors**: Matthias Vallentin (Tenzir Founder)
**Date**: November 2025
**URL**: LinkedIn post (professional network analysis)
**Evidence Level**: B (Vendor framework, emerging architecture)
**Relevance**:
- Emerging streaming architectures for security data
- OCSF normalization at ingest
- Ingest-throughput claims (unverified, see below)

**Key Findings**:
- "Policy layer" (business logic) vs. "Pipe layer" (infrastructure) separation
- Infrastructure handles transport, storage, transformation
- Policy focuses on security-specific logic
- *Unverified 2026-11-17: a "100+ Gbps ingest" claim from the LinkedIn post, which this review does not fetch and which names no benchmark.*
- OCSF normalization built-in

**Citations**: Emerging architectures, streaming innovation
**Notes**: Novel framework for security data pipeline architecture. Needs production validation.

**Validation Status**: ⚐ Emerging concept (November 2025) · ⚠️ 1 figure unverified 2026-11-17, see the dated label

---

#### Cribl Pipeline Economics - Route, Reshape, Reduce Pattern

**Authors**: Clint Sharp (Cribl CEO)
**Date**: October 2025
**URL**: CriblCon25 announcement
**Evidence Level**: B (CEO perspective, vendor strategy)
**Relevance**:
- Pipeline economics for security data
- Cost optimization patterns
- Agentic telemetry architecture

**Key Findings**:
- "Route, reshape, reduce" data pipeline pattern
- *Unverified 2026-11-17: an "88-98% cost savings" claim, which names no primary and was not found in Cribl's CriblCon 2025 press material.*
- Intelligent routing based on data value
- *Unverified 2026-11-17: a "10x queries at half the cost" line, not found in Cribl's published CriblCon 2025 material.*
- AI agents issuing thousands of queries/minute vs. dozens/hour for humans

**Citations**: Cost optimization, pipeline architecture, AI-native infrastructure
**Notes**: Vendor CEO perspective. Needs production validation, and a primary for any number before one is cited.

**Validation Status**: ⚐ CriblCon25 announcement, awaiting case studies · ⚠️ 2 figures unverified 2026-11-17, see the dated labels

---

#### Vortex File Format - Emerging Columnar Format

**Authors**: Will Manning et al.
**Date**: November 2025
**URL**: https://github.com/vortex-data/vortex
**Evidence Level**: C (Emerging technology, unvalidated claims)
**Relevance**:
- Next-generation columnar file format
- Potential Parquet successor

**Key Findings**:
- The project README claims 100× faster random-access reads, 10-20× faster scans and 5× faster writes than modern Apache Parquet at similar compression ratios (README, re-read 2026-11-17; project-authored claims, not independently measured)
- Different compression and encoding strategies
- Early stage development
- Limited production adoption

**Citations**: Emerging technologies, file formats
**Notes**: **NEEDS VALIDATION** - Performance claims unverified. Monitor for production adoption.

**Validation Status**: ⚠️ Unvalidated performance claims

---

#### Databricks MCP Catalog - Unity Catalog for AI Agents

**Authors**: Databricks
**Date**: June 18, 2025 (corrected 2026-11-17 from "October 2025" to the blog's publication date)
**URL**: https://www.databricks.com/blog/announcing-managed-mcp-servers-unity-catalog-and-mosaic-ai-integration
**Evidence Level**: B (Vendor announcement, beta release)
**Relevance**:
- AI agent governance for data access
- Unity Catalog integration
- MCP (Model Context Protocol) standardization

**Key Findings**:
- Unity Catalog exposed via MCP servers
- AI agents can discover and access governed data
- Fine-grained access control for LLM applications
- Managed MCP servers for Unity Catalog functions, Genie spaces and AI Search indexes that respect each user's Unity Catalog permissions (blog)
- *Unverified 2026-11-17: a named-assistant integration list (Claude, ChatGPT), not in the blog.*

**Citations**: AI governance, catalog integration, emerging standards
**Notes**: Early adoption phase. Part of broader AI-native infrastructure trend.

**Validation Status**: ✅ Blog re-read 2026-11-17 (Beta at announcement) · ⚠️ 1 claim unverified 2026-11-17, see the dated label

---

#### Apache Polaris Catalog - Security Architecture & Isolation

**Authors**: Snowflake / Apache Software Foundation
**Date**: 2024
**URL**: https://polaris.apache.org/
**Evidence Level**: B (Official documentation, production-ready catalog) — re-tiered from A 2026-08-19: neither peer-reviewed research nor an official standard
**Relevance**:
- **Research Question RQ7** (Isolation patterns and performance)
- **Research Question RQ10** (Catalog governance decisions)
- Book ch05 §5.1 (table format) [was: Chapter 8] (Storage formats - catalog selection)
- Isolation-first security architecture pattern

**Key Findings**:
- Table-level RBAC with credential vending
- Internal/external catalog isolation patterns
- Vendor-neutral open-source catalog for isolated platforms
- Production deployments at Netflix (security observability) and other enterprises *(Withdrawn 2026-11-23: no Netflix deployment appears on polaris.apache.org, its community page or its 1.9.0 access-control page, and the Netflix entry this traced to was de-attributed from Polaris on 2026-07-09; see the "Netflix Petabyte-Scale Logging" entry's Notes)*
- No row-level security or column masking overhead - table-level permissions only

**Citations**: **CRITICAL** - RQ7 and RQ10 isolation-first catalog validation
**Notes**: ~~Production validation of vendor-neutral catalog choice for isolated security platforms.~~ *(Withdrawn 2026-11-23 with the Netflix production-deployment finding above, which was the only production claim behind it.)* *(Withdrawn 2026-11-23: the former "Complements Netflix and Huntress isolation-first architecture patterns" sentence, because neither source describes an isolation-first design; see the Netflix Petabyte-Scale Logging entry ("The blog does not use 'isolation-first'") and the Huntress entry's 2026-11-22 note.)*

**Validation Status**: ✅ Active (verified Feb 2026, Apache project)
**Refresh (2026-11-23)**: checked against the Polaris 1.9.0 documentation (release published 2026-11-14), https://polaris.apache.org/releases/1.9.0/managing-security/access-control/. Its RBAC model grants privileges on catalogs, namespaces, tables, views, policies (as of 1.9.0 the predefined types are maintenance only: compaction, snapshot expiry, orphan-file removal; custom policy types are described as in progress) and semantic models, and the page names no row-level security or column masking, so the table-level reading above holds for 1.9.0. One addition since the February check: "Polaris supports integration with external Policy Decision Points (PDPs) such as Open Policy Agent (OPA)", which is where a deployment that needs finer-grained decisions would put them.

---

#### Unity Catalog - Row-Level Security Performance Analysis

**Authors**: Unity Catalog Community / Databricks Documentation
**Date**: 2024 (as catalogued; the "performance analysis published September 2024" could not be located on 2026-11-23; the ABAC performance page now cited was last updated 2026-10-08 and the filters-and-masks page 2026-11-06)
**URL**: https://docs.databricks.com/aws/en/data-governance/unity-catalog/abac/performance
**Alt URL**: https://docs.databricks.com/aws/en/data-governance/unity-catalog/filters-and-masks/
**Evidence Level**: C for the performance claims (vendor documentation on how a feature performs, per the 2026-11-03 ruling in METHODOLOGY.md §3.1); B for what row filters and column masks do
**Relevance**:
- **Research Question RQ7** (Isolation patterns and performance)
- Book ch05 §5.1 (table format) [was: Chapter 8] (Storage formats - catalog selection)
- Fine-grained access control performance trade-offs

**Key Findings**:
- Column masking introduces computational overhead for query execution
- Two separate documented costs. Caching depends on how the filter or mask UDF is written: "Non-deterministic functions and expressions that can throw errors reduce the optimizer's ability to cache results and reorder operations". Pruning depends on the policy being present at all: row filters and column masks put a SecureView barrier on the table that stops predicates with side effects from being pushed down, which "can also block partition pruning and liquid clustering optimizations, which can force full table scans", and "This applies even when the policy UDF resolves to a constant true" (narrowed 2026-11-23 from "Row-level security can prevent effective query result caching", which the docs do not state as a general rule)
- Performance impact varies with UDF complexity, the number of distinct masks and lookup-table size (ABAC performance page), and with the number of UDF arguments and AND conjuncts in a row filter (filters-and-masks page). This is Databricks guidance; neither page publishes an overhead figure or a method, and neither names cardinality
- Table-level permissions (isolation-first approach) avoids fine-grained overhead
- Multi-tenant architectures may require Unity Catalog features, but isolation-first SOCs can avoid complexity

**Citations**: RQ7 isolation-first performance validation
**Notes**: Supports isolation-first architecture pattern - network isolation with table-level permissions avoids Unity Catalog overhead. *(Withdrawn 2026-11-23: the former "Relevant for Huntress, Okta, Netflix patterns", because the Huntress and Netflix sources describe no isolation-first design (Huntress entry's 2026-11-22 note; Netflix Petabyte-Scale Logging entry); the Okta leg was not re-checked in this pass and is not carried without a source.)*

**Validation Status**: ✅ Active (verified Feb 2026, official Databricks docs)
**Refresh (2026-11-23)**: the catalogued URL now redirects to the Unity Catalog overview, which carries none of these claims, so the entry points at the ABAC performance-considerations page and the filters-and-masks page instead. Databricks gives tuning guidance and no measured overhead, so the review's own engine-side RLS measurement (isolation-first-security-tracking.md, ocsf-rls-overhead, DuckDB, single host) is still the only measured figure in the corpus. Bullets 4 and 5 are the review's inference and are not Databricks statements; the SecureView point above cuts partly in their favour, because the docs say a policy's presence alone can cost pruning for some query shapes.

---

### Practitioner Validation

#### Anonymized practitioner - Security Data Platform Practitioner Validation

**Authors**: Anonymized practitioner
**Date**: October 2025
**URL**: Personal communication (Practitioner validation), anonymized per the Boundary rule
**Evidence Level**: B (Practitioner validation, production security implementations) — re-tiered from A 2026-08-19: not peer-reviewed research and not an official standard

> **Do not cite (2026-11-17).** This entry's only source is a personal communication, which the
> Boundary rule in this file's header excludes, and it carries no number.
**Relevance**:
- Query engine viability for security operations at scale
- Book ch07 §7.2-7.3 + Appendix K [was: Chapter 4] (Three Architect Journeys)
- Validates Starburst/Athena architectural patterns

**Key Findings**:
- Starburst and Athena proven at security data scale
- Query engine approach viable for security operations
- Production deployments validate book architectural recommendations
- Federated query engines handle security workload requirements

**Citations**: ch07 §7.2-7.3 + Appendix K [was: Chapter 4] (Three Architect Journeys - practitioner validation)
**Notes**: Practitioner feedback validates query engine architectures for security use cases

**Validation Status**: ⚠️ No citable primary (an unpublished conversation, ineligible under the Boundary rule); do not cite

---

## Additional Sources: Formats, Catalogs, Governance and Cost

*The October 2025 extraction progress log and completion summary that used to sit here are archived verbatim at [archive/bibliography-extraction-log-2025-10.md](archive/bibliography-extraction-log-2025-10.md).*


#### Apache Iceberg 2025 Performance Analysis
**Authors**: Multiple vendors and analysts
**Date**: 2025
**URL**: Various (ProCogia, Streamkap, AutoMQ, Starburst); primary: https://iceberg.apache.org/docs/latest/performance/
**Evidence Level**: B (Multiple vendor analyses with disclosed methodology; primary Iceberg docs support core claim)
**Relevance**:
- RQ11: LIGER Stack validation (Lakehouse component)
- Apache Iceberg production readiness
- Performance vs Delta/Hudi comparison

**Key Findings**:
- Iceberg's performance docs say clustered data lets the planner eliminate splits without running tasks, which "in some cases" is a 10x performance improvement (corrected 2026-11-17: the docs do not frame this as a comparison with Hive)
- Metadata pruning skips large fractions of scanned files, substantially reducing scan costs for large datasets
- Nanosecond-precision timestamps support for finance/telco (2025 feature)
- Sub-second latency with CDC and streaming (Kafka, Flink)
- Industry-wide adoption as de facto standard (AWS, Google, Microsoft, Databricks)
- Performance considerations: Delta/Hudi faster for write-heavy workloads

**Citations**: Iceberg performance, production deployment, streaming integration
**Notes**: Industry consensus on Iceberg leadership despite write performance gaps. "50% scan reduction" figure was vendor-soft and replaced with qualitative framing.
**Validation Status**: ✅ Multiple independent sources (2025)

**Validation (2026-06-05, folded)**: corrections applied to findings/tier above; provenance in RESEARCH-JOURNAL.md.
---

#### SANS AI Security Controls Framework
**Authors**: SANS Institute (Rob T. Lee)
**Date**: 2025-03-31
**URL**: https://www.sans.org/blog/securing-ai-in-2025-a-risk-based-approach-to-ai-controls-and-governance
**Evidence Level**: B (Expert-consensus practitioner framework; regulatory-audit and logging-requirement claims not in source)
**Cross-reference**: same source URL as "SANS Institute - Securing AI in 2025: Risk-Based Approach" below — deliberate topic split (this entry: the controls framework; that entry: implementation practices), tiers reconciled to B 2026-07-10 (part-2 sweep fix 39)
**Relevance**:
- RQ12: AI governance maturity
- Security controls for AI agents
- Production deployment guidelines

**Key Findings**:
- Critical AI Security Guidelines v1.1 framework
- Three bedrock principles: security controls, governance/compliance, risk-based approach
- Six key control categories including access controls, audit logging, continuous monitoring
- Phased implementation approach for production

**Citations**: AI governance framework, security controls, audit requirements
**Notes**: Industry standard emerging for AI agent governance. Regulatory-audit (SEC/OCC) and tamper-evident-log-requirement bullets were not present in the source and have been removed.
**Validation Status**: ✅ Active framework (2025)

**Validation (2026-06-05, folded)**: corrections applied to findings/tier above; provenance in RESEARCH-JOURNAL.md.
---

#### Security Data Lakehouse Implementation Patterns
**Authors**: Multiple industry practitioners
**Date**: 2025
**URL**: Various (Snowflake, Ryft.io, Query.ai, Dremio)
**Evidence Level**: B (Industry analysis and implementation guides)
**Relevance**:
- RQ11: LIGER Stack validation
- Security lakehouse architecture patterns
- OCSF integration challenges

**Key Findings**:
- *Removed 2026-11-17: an "OCSF normalization requires 6+ months for 700+ mappings" claim, which names no primary among the four vendors listed.*
- Iceberg snapshot-based queries enable "time travel" for incident investigation
- Schema evolution critical for security data (new sources, fields, vendors)
- Multi-engine architecture validated (ClickHouse for alerting, Trino for ad-hoc, Spark for batch)
- *Removed 2026-11-17: a "70-90% cost reduction" range attributed to unnamed vendor claims.*

**Citations**: Security lakehouse patterns, OCSF implementation, multi-engine architecture
**Notes**: A composite entry with no named primary per claim, so cite the vendors' own published material for any of these points rather than this entry.
**Validation Status**: ⚠️ No primary named; numbers removed 2026-11-17

---

#### Data Catalog Wars 2025 - Polaris vs Unity vs Nessie vs Gravitino
**Authors**: E6Data, Dremio, Medium contributors; RBAC comparison via onehouse.ai/blog/comprehensive-data-catalog-comparison
**Date**: 2025
**URL**: https://www.onehouse.ai/blog/comprehensive-data-catalog-comparison (the access-control comparison quoted below, re-read 2026-11-17)
**Alt URL**: https://projectnessie.org/
**Evidence Level**: B (Vendor analyses and community reviews)
**Relevance**:
- RQ10: Catalog governance decisions
- Isolation-first security implementation
- Enterprise deployment patterns

**Key Findings**:
- Nessie: Most mature open-source option with Git-like versioning; does not provide access-control features
- Unity Catalog: Now fully open-source, strong within Databricks ecosystem; offers granular RBAC
- Polaris: REST-based interoperability, backed by Snowflake and Dremio; offers granular RBAC
- Gravitino: Emerging with AI/unstructured data features; offers granular RBAC
- Unity, Polaris, and Gravitino provide fine-grained access control (source: onehouse.ai comparison — verbatim "the only catalogs that offer this are Unity, Polaris, and Gravitino"; its evaluated set is Unity/Polaris/DataHub/Glue/Gravitino/Atlan). Nessie's versioning-only focus re-attributed 2026-07-10 to Nessie's own documentation (projectnessie.org — Git-like data versioning is its stated design center); Nessie sits outside the onehouse.ai comparison's evaluated scope (one passing mention as an Iceberg catalog integration)
- "Catalog wars" intensifying in 2025 with vendor competition

**Citations**: Catalog comparison, governance features, production adoption
**Notes**: Critical for catalog selection in isolation-first architectures
**Validation Status**: ✅ Active competition and adoption (2025)

**Validation (2026-06-05, folded)**: corrections applied to findings/tier above; provenance in RESEARCH-JOURNAL.md.
---

#### Row-Level Security Performance Impact Studies
**Authors**: PostgreSQL community, SQL Server team, various practitioners
**Date**: 2024-2025
**URL**: https://www.postgresql.org/docs/current/ddl-rowsecurity.html (supports the per-row evaluation bullet only)
**Evidence Level**: B (Technical documentation and benchmarks)
**Relevance**:
- RQ7: Isolation-first security validation
- Performance overhead quantification
- Table vs row/column security tradeoffs

**Key Findings**:
- PostgreSQL evaluates a row-security policy expression "for each row prior to any conditions or functions coming from the user's query" (PostgreSQL docs, re-read 2026-11-17; the docs do not quantify the overhead)
- Column-level ACLs perform better than row-level but worse than table-level
- *Removed 2026-11-17: a "SQL Server 2025 RLS optimizations with hardware acceleration" claim, which names no primary.*
- Complex policies recommended at application layer (OPA) not database
- Simple tenant_id RLS efficient for basic isolation
- GIN indexes help maintain performance on ACL arrays

**Citations**: RLS performance overhead, isolation patterns, security optimization
**Notes**: Only the per-row evaluation bullet has a named primary; the others are unsourced practitioner guidance. For a measured engine-side number, cite the SDW Lab entry that follows.
**Validation Status**: ⚠️ One bullet verified at the PostgreSQL docs 2026-11-17; the rest have no named primary

---

#### OCSF RLS Overhead, SDW Lab First-Party Measurement (engine-side, DuckDB)
**Authors**: SDW Lab (sdw-lab-benchmarks/ocsf-rls-overhead)
**Date**: 2026-06-08
**URL**: https://github.com/flying-coyote/sdw-lab-benchmarks/blob/master/ocsf-rls-overhead/results/RESULTS.md (reproduce: `python ocsf-rls-overhead/run.py`; +81%, +94% and -86% re-read in the results table 2026-11-17)
**Evidence Level**: B (single machine; latencies are medians with reported coefficient of variation over 7 trials after 2 warmups; the corpus and the answers are deterministic; engine-side overhead only)
**Relevance**:
- RQ7: isolation-first security validation, the first-party number for the RLS-overhead gap the 2026-06 audit opened when it removed the unsupported figures carried above
- Advances H-SECURITY-02 (federated catalog RBAC)

**Key Findings**:
The third-party studies above describe RLS overhead qualitatively ("significant overhead", "evaluated for every row"), so I put a measured number on the engine-side cost. The bench enforces row-level security two ways over a 1,000,000-row, 100-tenant OCSF corpus on DuckDB 1.5.3: a `tenant_id` WHERE predicate appended to the query, and a secured VIEW the query hits directly. The two mechanisms return identical answers across every query and every selectivity tier (the correctness gate reads True), which is the precondition for comparing their cost at all. The overhead is not a single percentage, it tracks query shape and selectivity: at 1% selectivity a full-scan `count_all` runs about 81% slower under the predicate and about 94% slower under the view, while a high-cardinality `top_talkers` runs about 86% *faster* under either mechanism, because the tenant filter reads roughly 99% fewer rows and the saving on scan cost outweighs the filter. So whether RLS costs or saves depends on whether the predicate adds work or removes it from the plan, and a blanket "RLS adds N%" figure of the kind the audit removed is the wrong shape for the answer.

The reading that matters for the architecture argument is the lower-bound caveat. This is engine-side enforcement only: DuckDB evaluates the RLS predicate as an ordinary WHERE clause after parsing, so the numbers above are the floor. A real multi-tenant catalog (Apache Polaris principal roles, Unity Catalog row filters, AWS Lake Formation cell-level permissions) enforces policy at the catalog protocol layer before the engine plans, adding token validation, policy evaluation, and protocol round-trips on top of the engine cost measured here. The catalog-layer component is the subject of the separate q3-catalog-benchmark; cite this entry only for the engine-side floor.

**Citations**: RQ7 isolation-first performance, first-party RLS-overhead measurement replacing removed third-party figures
**Notes**: Tier B, single host (14 vCPU, WSL2), DuckDB 1.5.3 engine-side only. Pairs with the Unity Catalog RLS analysis above (which is documentation, not measurement) and fills the figure gap noted in the Netflix/ClickHouse entry where RLS overhead claims were removed in the 2026-06-05 audit.
**Validation Status**: ✅ Reproducible from corpus fingerprint and seed; answers deterministic, latencies are medians with CV
**Currency (2026-11-17)**: measured on DuckDB 1.5.3; DuckDB v2.0.0 was released 2026-10-21 (https://github.com/duckdb/duckdb/releases), so the percentages are version-bound to 1.5.3.

---

#### Streaming vs Batch Cost Analysis 2025
**Authors**: Confluent, Redpanda, AWS, industry analysts
**Date**: 2025
**URL**: https://www.confluent.io/press-release/data-streaming-report-2025/ (Confluent's release of its 2025 Data Streaming Report, 4,175 IT leaders across 12 countries)
**Evidence Level**: B (Primary survey data from Confluent report confirmed; several cost-ratio bullets lack primary-source backing)
**Relevance**:
- RQ13: Pipeline vs query detection economics
- Streaming infrastructure costs
- TCO comparison methodology

**Key Findings**:
- 86% rank data streaming as an important strategic priority (Confluent 2025 Data Streaming Report, 4,175 respondents; wording corrected 2026-11-17 from "top strategic investment")
- 44% report 5× return on investment for data streaming, against 41% in 2024 (Confluent 2025 Data Streaming Report; vendor-commissioned survey, flag bias)
- Flink emerging as standard for stream processing
- Hybrid streaming/batch approach optimal for cost
- Note: managed-Kafka TCO reduction, Kinesis processing-time reduction, and batch idle-executor waste figures cited in earlier versions are not from the Confluent report and require separate sourcing before use

**Citations**: Streaming TCO, ROI metrics, infrastructure costs
**Notes**: Strong validation for pipeline-based detection economics. Retain only Confluent-report-sourced figures until supplementary cost bullets are individually re-sourced.
**Validation Status**: ✅ 86%, 44% and the 4,175 sample re-read at Confluent's release 2026-11-17

**Validation (2026-06-05, folded)**: corrections applied to findings/tier above; provenance in RESEARCH-JOURNAL.md.
---

## January 2026 Research Update

### AI Governance & Security Maturity (RQ12)

#### CSA/Google Cloud - The State of AI Security and Governance

**Authors**: Cloud Security Alliance, Google Cloud
**Date**: December 2025
**URL**: https://cloudsecurityalliance.org/artifacts/the-state-of-ai-security-and-governance
**Evidence Level**: B (Industry survey, independent research, major vendors) — re-tiered from A 2026-08-19: not peer-reviewed research and not an official standard
**Relevance**:
- RQ12: AI Governance Maturity Gates
- Governance prerequisites for AI success
- Agentic AI adoption rates

**Key Findings**:
- Only 26% of organizations have comprehensive AI security governance
- 54% use public frontier LLMs, 60% plan agentic AI within 12 months
- Governance maturity is strongest predictor of AI readiness
- Organizations with comprehensive policies: 46% early agentic AI adoption
- Organizations with policies in development: only 12% adoption
- Sensitive data exposure ranks as leading AI security concern
- Top concerns: compliance, regulatory issues, model-level risks (lower priority)

*Unverified 2026-11-17: the 26%, 54%, 60%, 12-month, 46% and 12% figures are not on the report's landing page, and the report itself sits behind registration and was not read.*

**Citations**: AI governance prerequisites, maturity assessment, agentic AI adoption
**Notes**: **CRITICAL** - Primary validation for RQ12. Use in Lisa Cao and Jake Thomas interviews.

**Validation Status**: ✅ Survey published December 2025 · ⚠️ 6 figures unverified 2026-11-17, see the dated labels

---

#### CSA Press Release - Governance Maturity as AI Predictor

**Authors**: Cloud Security Alliance
**Date**: December 18, 2025
**URL**: https://cloudsecurityalliance.org/press-releases/2025/12/18/csa-and-google-cloud-study-finds-governance-maturity-is-strongest-predictor-of-ai-readiness
**Evidence Level**: B (Industry consortium, Google Cloud partnership) — re-tiered from A 2026-08-19: not peer-reviewed research and not an official standard
**Relevance**:
- RQ12: AI Governance Maturity Gates
- Quantitative validation of governance-success correlation

**Key Findings**:
- "Governance maturity stands out as the strongest indicator of readiness"
- Organizations with comprehensive AI governance policies are nearly twice as likely to report early adoption of agentic AI (46%) vs those with only partial guidelines (25%) or policies still in development (12%) — the entry's former "about 25% have comprehensive governance" mis-scoped the page's 25%, which is the agentic-adoption rate among partial-guideline orgs (corrected 2026-07-10)
- Survey base: 300 IT and security professionals, conducted online by CSA in Summer 2025
- Gap between AI adoption pace and governance structure

**Citations**: Governance-readiness correlation, industry benchmarks
**Notes**: Supplements main CSA report with additional context

**Validation Status**: ✅ December 2025 publication

---

#### SANS Institute - Securing AI in 2025: Risk-Based Approach

**Authors**: SANS Institute (Rob T. Lee)
**Date**: 2025-03-31
**URL**: https://www.sans.org/blog/securing-ai-in-2025-a-risk-based-approach-to-ai-controls-and-governance
**Evidence Level**: B (re-tiered from A 2026-07-10, part-2 sweep fix 39 — a SANS blog post is practitioner-tier under the strict A=peer-reviewed/standards definition, and the same URL was catalogued at B in the "SANS AI Security Controls Framework" entry above; deliberate topic split retained, tiers reconciled)
**Relevance**:
- RQ12: AI Governance Maturity Gates
- Implementation best practices

**Key Findings**:
- Data integrity critical for preventing model bias/corruption
- Separate sensitive data from training data unless necessary
- Protect AI prompts from business intelligence exposure
- Implement AI incrementally in non-critical systems first
- Adopt enterprise AI policies with centralized governance boards
- Develop AI incident response plans

**Citations**: AI implementation best practices, governance frameworks
**Notes**: Practical implementation guidance from security authority

**Validation Status**: ✅ Active URL (2025)

---

### Security Data Lakehouse Production Evidence (RQ11)

#### Databricks Data Intelligence for Cyber Defense - Barracuda & Palo Alto

**Authors**: HyperFRAME Research
**Date**: October 2025
**URL**: https://hyperframeresearch.com/2025/10/07/databricks-releases-data-intelligence-for-cyber-defense/
**Evidence Level**: B (Production deployment, quantitative results) — re-tiered from A 2026-08-19: not peer-reviewed research and not an official standard
**Relevance**:
- RQ11: LIGER Stack TCO validation
- Security lakehouse cost reduction

**Key Findings**:
- **Barracuda Networks**: 75% reduction in daily processing and storage costs
- Real-time alerting delivered in under 5 minutes
- **Palo Alto Networks**: 3× faster AI-powered threat detection
- Signals major SIEM disruption from lakehouse platforms

*Unverified 2026-11-17: the figures above, and the 70-90% in the Notes, could not be re-read, because the HyperFRAME page blocks automated readers.*

**Citations**: Security lakehouse cost reduction, production deployments
**Notes**: **CRITICAL** - First major vendor validation of 70-90% cost reduction claims

**Validation Status**: ✅ Production customer results (October 2025) · ⚠️ 4 figures unverified 2026-11-17, see the dated labels

---

#### ClickHouse - GitLab Sub-Second Analytics Case Study

**Authors**: ClickHouse
**Date**: 2025 (page byline Oct 21, 2025; catalogued "2024" corrected 2026-07-09, verified at primary)
**URL**: https://clickhouse.com/blog/how-gitlab-uses-clickhouse-to-scale-analytical-workloads
**Evidence Level**: B (Production deployment, quantitative benchmarks) — re-tiered from A 2026-08-19: not peer-reviewed research and not an official standard
**Relevance**:
- RQ11: LIGER Stack "E" (Engine) component
- Query performance for security analytics

**Key Findings**:
- Queries over 100M rows: reduced from 30-40 seconds to <1 second
- GitLab serves sub-second analytics to 50 million users
- Built and maintained own ClickHouse operator (now open source)
- Migrated to ClickHouse Cloud to reduce operational overhead

**Citations**: ClickHouse performance, production deployment patterns
**Notes**: Strong validation for ClickHouse in high-scale analytics

**Validation Status**: ✅ Production case study — re-verified at primary 2026-07-10 ("queries over 100M rows that once took 30–40 seconds now return in under a second" page-verbatim, byline 2025-10-21); the former "pre-2025" freshness remnant no longer applied after the 2026-07-09 date correction and was removed (part-2 sweep).

---

#### ClickHouse vs Snowflake Benchmarks and Cost Analysis

**Authors**: ClickHouse
**Date**: 2023 (published Sept 6, 2023; catalogued "2024" corrected 2026-07-09 — newer 2026 CostBench posts exist + Snowflake contests them, see review packet)
**URL**: https://clickhouse.com/blog/clickhouse-vs-snowflake-for-real-time-analytics-benchmarks-cost-analysis
**Evidence Level**: B (Vendor benchmark, methodology disclosed)
**Relevance**:
- RQ11: Query engine cost comparison
- Real-time analytics economics

**Key Findings**:
- ClickHouse Cloud 3-5× more cost-effective than Snowflake
- ClickHouse querying speeds 2× faster than Snowflake
- Advantages in real-time analytics workloads

**Citations**: Query engine TCO, performance comparison
**Notes**: Vendor benchmark but methodology disclosed; cross-validate with independent sources

**Validation Status**: ✅ Published benchmark (2023-09-06) — re-verified at primary 2026-07-10 ("ClickHouse Cloud is 3-5x more cost-effective than Snowflake" and "over 2x faster" both page-verbatim); the former "(2024)" internal remnant corrected (part-2 sweep).

---

#### Netflix ClickHouse Pipeline - 5 PB/Day Ingestion

**Authors**: Tom Schreiber (ClickHouse)
**Date**: 2025-12-22 (page byline; metadata 2025-12-17; catalogued "2024" corrected 2026-11-23)
**URL**: https://clickhouse.com/blog/what-really-matters-for-performance-lessons-from-a-year-of-benchmarks
**Evidence Level**: B (ClickHouse benchmark retrospective reporting Netflix's described result — secondhand, not a Netflix primary source)
**Relevance**:
- RQ11: LIGER Stack scale validation
- High-volume log ingestion patterns

**Key Findings**:
- Netflix ingests ~5 PB of logs per day into ClickHouse (per ClickHouse's blog reporting Netflix's described result; verified on the page 2026-06-22)
- Reverse-engineered Go client for native-protocol encoding with LZ4
- Implemented in Java pipeline for lower CPU usage and better memory efficiency
- FastFormats benchmark drove optimization decisions

**Citations**: High-volume ingestion, ClickHouse production patterns
**Notes**: Shows ClickHouse ingesting general application logs at ~5 PB/day; the page does not describe a security workload (narrowed 2026-11-23). The cited page is a ClickHouse benchmarking retrospective that uses Netflix as a case study, not a Netflix-authored source.

**Validation Status**: ✅ Active URL (ClickHouse blog citing Netflix) · Freshness (2026-06-05): publication date pre-2025 (>12mo), freshness-triaged (date-stale). Content correction 2026-06-22 (WebFetch-verified): ~5 PB/day IS stated on the page (secondhand report of Netflix's result); the "10.6M events/sec" figure is NOT on the page — removed; Evidence Level corrected A→B (ClickHouse retrospective, not a Netflix primary).
**Refresh (2026-11-23)**: re-fetched (HTTP 200). The ~5 PB/day, Go-client reverse-engineering, LZ4 native-protocol and FastFormats points are verbatim on the page, and 10.6M events/sec is still absent from it. The page is a December 2025 retrospective by Tom Schreiber, so the entry is no longer date-stale. Its Netflix passage links to the ClickHouse post catalogued here as "Netflix Petabyte-Scale Logging, ClickHouse + Iceberg (Muino, 2025)" (byline 23 October 2025), which carries the 10.6M and 12.5M events/sec figures; cite that entry for the figures and this one only for the FastFormats-to-native-protocol link. The two entries overlap, as that entry's Notes already say.

---

#### Forrester - Drowning In Security Data Costs

**Authors**: Forrester Research (Allie Mellen)
**Date**: 2025-07-22
**URL**: https://www.forrester.com/blogs/drowning-in-security-data-costs-you-get-a-data-lake/
**Evidence Level**: B (Analyst blog post; actual content differs from previous summary)
**Relevance**:
- RQ11: LIGER Stack business case
- Security data lake adoption trends

**Key Findings**:
- Advocates a store-vs-access two-tier data strategy for security log economics
- Microsoft Sentinel lake tier priced at less than 15% of analytics-tier log costs

**Citations**: Security data lake adoption, CISO priorities
**Notes**: Independent analyst validation of security lakehouse trend. Prior bullets ("CISOs voting with budget", "immediate ROI", "SIEM unsustainable") were not in the post and have been replaced with the actual content.

**Validation Status**: ✅ Forrester blog (2025)

**Validation (2026-06-05, folded)**: corrections applied to findings/tier above; provenance in RESEARCH-JOURNAL.md.
---

#### Hunters Security - Why Companies Are Adopting Security Data Lakes

**Authors**: Hunters Security (vendor blog reporting remarks by Omar Khawaja, Field CISO, Databricks, at Hunters Con)
**Date**: 2023-11-27 (page metadata, and the earliest Wayback capture, 2024-03-05, shows the same date; catalogued "2024" corrected 2026-11-23)
**URL**: https://www.hunters.security/en/blog/why-companies-are-adopting-security-data-lakes
**Evidence Level**: C (vendor blog relaying a second vendor's executive; flag bias: both Hunters and Databricks sell security data lake products)
**Relevance**:
- RQ11: Security data lake adoption
- Enterprise case studies

**Key Findings**:
- Khawaja (Databricks) said that "of the world's 15 largest banks, he's aware that half of them are using a security data lake" (one vendor executive's awareness, not a survey; narrowed 2026-11-23)
- **HSBC**: "3x more hunts while lowering the total cost of ownership", relayed from a 2023 Databricks blog; an earlier Databricks post (2021) gives "2-3x more threat hunts per analyst" and describes a Lakehouse-alongside-SIEM setup. Both figures are Databricks' wording and no HSBC-authored source was found (narrowed 2026-11-23)
- Security data lakes emerged to address SIEM limitations and high costs
- ~~Skills shortage affects security data lake projects~~ (removed 2026-07-10 — absent from the cited page; the bank and HSBC figures above verify verbatim)

**Citations**: Enterprise adoption, banking sector case studies
**Notes**: HSBC is a named production deployment, but every figure reaches us through Databricks. The two Databricks posts give different figures (3x in 2023, 2-3x per analyst in 2021), so cite the lower, per-analyst wording (https://www.databricks.com/blog/2021/07/23/augment-your-siem-for-cybersecurity-at-cloud-scale.html) and treat the deployment as SIEM augmentation, since that post frames it as Lakehouse plus SIEM.

**Validation Status**: ✅ Re-verified at the page 2026-11-23 (both figures present as relayed remarks; see narrowed bullets)
**Refresh (2026-11-23)**: dated 2023-11-27, not 2024. The bank figure is Khawaja's stated awareness at a vendor conference. The HSBC figure is relayed from a 2023 Databricks post that says 3x, and Databricks' 2021 post says 2-3x per analyst, so both findings are narrowed and the entry is re-tiered B to C.

---

### OCSF Schema Adoption (RQ11)

#### Linux Foundation - OCSF Joins Linux Foundation

**Authors**: Linux Foundation
**Date**: November 19, 2024 (updated February 2026)
**URL**: https://www.linuxfoundation.org/press/open-cybersecurity-schema-framework-ocsf-joins-the-linux-foundation-to-optimize-critical-security-data
**Alt URL**: https://ocsf.io/
**Evidence Level**: B (Linux Foundation official, consortium milestone) — re-tiered from A 2026-08-19: neither peer-reviewed research nor an official standard
**Relevance**:
- RQ11: LIGER Stack schema standardization
- OCSF adoption trajectory

**Key Findings**:
- OCSF now a Linux Foundation Project (November 2024)
- 900+ contributors
- 200+ participating organizations
- Founded by AWS, Cisco, IBM, Splunk, Broadcom (Symantec)
- Latest version at press-release time: v1.3.0 (August 2024) — "The latest version, 1.3.0, released in August 2024" (page verbatim)
- **Schema velocity** (re-sourced 2026-07-10 to github.com/ocsf/ocsf-schema releases — the press release carries nothing past v1.3.0): 3 releases in 2025 (v1.5.0 Apr, v1.6.0 Aug, v1.7.0 Nov) plus v1.8.0 in March 2026; release dates verified at GitHub 2026-07-09 (see the "OCSF Schema v1.8.0" entry); per-release feature contents live in the GitHub release notes, not re-verified here

**Citations**: OCSF adoption, industry consortium, schema evolution velocity
**Notes**: Correction (2026-07-10, part-2 sweep fix 1): the "80%+ security professionals" stat, the SentinelOne/AWS-Security-Lake adoption claims, and the "15+ additional organizations" vendor list were removed — none appear on the cited press release or the ocsf.io Alt URL, and no primary was located this pass; re-add individually if a primary turns up. What the press release does verify verbatim: v1.3.0 latest (Aug 2024), "over 900 contributors and 200 participating organizations", and the founder list.

**Validation Status**: ✅ Verified at primary 2026-07-10 (part-2 sweep); velocity claims re-sourced to GitHub releases
**Currency (2026-11-17)**: the current OCSF schema release is v1.9.0 (https://github.com/ocsf/ocsf-schema/releases, published 2026-08-03), with v1.10.0 in development per schema.ocsf.io.
**Refresh (2026-11-23)**: v1.10.0 was released on 2026-11-20 and is now the current release (https://github.com/ocsf/ocsf-schema/releases/tag/1.10).

---

### Catalog Governance & Multi-Catalog Management (RQ10)

#### Apache Gravitino - Production Adoption

**Authors**: Medium account "Office" (summarizes Jerry Shao's talk; entry formerly credited "Datastrato, Apache Foundation")
**Date**: 2025-08-26
**URL**: https://medium.com/@office_9948/apache-gravitino-production-ready-unified-metadata-for-enterprise-data-9ba0eb38268b
**Evidence Level**: B (Community/vendor blog; adopter list partially confirmed via separate sources)
**Relevance**:
- RQ10: Catalog governance influence
- Multi-catalog management patterns

**Key Findings**:
- Pinterest confirmed adopter (per cited Medium article)
- ChatSlide: Scaled from 100K to 150K+ users with sub-second query performance (per chatslide.ai/pages/apache-gravitino-data-catalog) *(Unverified 2026-11-17: the cited page blocks automated readers, so this could not be re-read.)*
- **Bilibili**: ~70% reduction in metadata query API response times (per Gravitino "OneMeta" writeup; treat as vendor case study) *(Unverified 2026-11-17: the cited page blocks automated readers, so this could not be re-read.)*
- Supports OAuth2 and HTTPS security ("OAuth2: Modern web-based authentication for applications and users" — article verbatim)

**Citations**: Multi-catalog management, enterprise adoption
**Notes**: The Medium source names Pinterest; broader adopter list (Uber, Apple, Intel, eBay, Xiaomi, Cloudflare, AWS, Tencent, Yahoo, Roku TV) requires verification against gravitino.apache.org/blog/gravitino-top-level-project/ before citing. Correction (2026-07-10, part-2 sweep fix 22): the geo-distributed-architecture and Apache-Ranger-integration bullets were removed — neither appears in the cited Medium article; re-source to gravitino.apache.org docs if needed. Article re-attributed: Medium account "Office", 2025-08-26, summarizing Jerry Shao's talk "Scaling Iceberg Adoption at Pinterest with Gravitino".

**Validation Status**: ✅ Production deployments documented · ⚠️ 3 figures unverified 2026-11-17, see the dated labels

**Validation (2026-06-05, folded)**: corrections applied to findings/tier above; provenance in RESEARCH-JOURNAL.md.
---

#### Apache Polaris - Growing Ecosystem

**Authors**: Dremio
**Date**: 2025
**URL**: https://www.dremio.com/blog/the-growing-apache-polaris-ecosystem-the-growing-apache-iceberg-catalog-standard/
**Alt URL**: https://www.dremio.com/blog/whats-new-in-apache-polaris-1-2-0/ (version release details)
**Evidence Level**: B (Vendor analysis, ecosystem overview)
**Relevance**:
- RQ10: Catalog governance influence
- Polaris adoption patterns

**Key Findings**:
- Polaris production-ready for Iceberg — "Commercial offerings from Dremio and Snowflake have already proven its production readiness" (page verbatim)
- Upcoming integrations from ingestion vendors, catalog platforms, storage providers
- Version 1.2.0 (Oct 2025) focused on governance: fine-grained authorization, event persistence, expanded RBAC (per dremio.com/blog/whats-new-in-apache-polaris-1-2-0/)

**Citations**: Polaris ecosystem, production readiness
**Notes**: Validates Polaris for isolation-first architectures. Correction (2026-07-10, part-2 sweep fix 23): the "time travel, commit retries, STS credential vending" parenthetical and the 1.0.0 (Jul 2025) / 1.1.0 (Sep 2025) release dates were removed — none appear on either cited Dremio page; re-source to Polaris release notes (polaris.apache.org) if the version history is needed. Both Dremio pages now carry a "Dremio is now part of SAP" banner (ownership context, live 2026-07-10).

**Validation Status**: ✅ Active development (2025)

**Validation (2026-06-05, folded)**: corrections applied to findings/tier above; provenance in RESEARCH-JOURNAL.md.
---

### Agent Automation & ROI (RQ14)

#### Google Cloud - AI Agent ROI Report

**Authors**: Google Cloud
**Date**: September 2025
**URL**: https://cloud.google.com/transform/roi-of-ai-how-agents-help-business
**Evidence Level**: C (Major vendor, survey data) — re-tiered from A 2026-08-19: not peer-reviewed research and not an official standard
**Relevance**:
- RQ14: Agentic Security Automation ROI
- Agent deployment rates

**Key Findings**:
- 52% of executives deploying AI agents in production
- 74% achieve ROI within first year
- 39% have deployed more than 10 agents across enterprise
- AI agents unlocking new wave of business value

**Citations**: Agent ROI, deployment rates
**Notes**: **CRITICAL** - Primary validation for RQ14 agent automation ROI

**Validation Status**: ✅ September 2025 report

---

#### AI Multiple - AI Agent Performance: Success Rates & ROI

**Authors**: PagerDuty (survey research; originally attributed to AI Multiple Research)
**Date**: 2025
**URL**: https://www.pagerduty.com/resources/ai/learn/companies-expecting-agentic-ai-roi-2025/
**Evidence Level**: C (Vendor survey, n=1,000; self-reported ROI projections; cite bias)
**Relevance**:
- RQ14: Agent automation ROI metrics
- Performance benchmarks

**Key Findings**:
- Average ROI projection: 171% (PagerDuty 2025 Agentic-AI ROI Survey, n=1,000; vendor-commissioned)
- 62% of respondents expect >100% returns
- U.S. enterprises project ~192% ROI

**Citations**: Agent ROI metrics, performance benchmarks
**Notes**: Source is a PagerDuty vendor survey, not a neutral research aggregator. Self-reported projections (not measured outcomes). Cite with vendor-bias caveat. "Up to 70% cost reduction" figure has no support in the survey and has been removed.

**Validation Status**: ✅ Research compilation (2025)

**Validation (2026-06-05, folded)**: corrections applied to findings/tier above; provenance in RESEARCH-JOURNAL.md.
---

#### Obsidian Security - 2025 AI Agent Security Landscape

**Authors**: Obsidian Security
**Date**: 2025-10-23 (published; page rewritten 2026-06-30)
**URL**: https://www.obsidiansecurity.com/blog/ai-agent-market-landscape
**Evidence Level**: B (Security vendor analysis; qualitative guidance, no disclosed benchmarks)
**Relevance**:
- RQ14: Agent automation metrics
- Security-specific agent considerations

**Key Findings**:
- Real-time monitoring and anomaly detection essential (present on the rewritten page)

**Citations**: Agent security metrics, operational guidance
**Notes**: Correction (2026-07-10, part-2 sweep fix 24): the page was rewritten 2026-06-30 — after this entry's 2026-06-05 validation — and the MTTD/MTTR/false-positive-rate metric recommendations and the SIEM/SOAR-integration guidance no longer appear anywhere on it; those bullets were removed rather than left asserting content the live source no longer carries. If the metric guidance matters, cite an archive.org snapshot of the pre-rewrite page instead.

**Validation Status**: ⚠️ Page rewritten 2026-06-30; re-verified against current text 2026-07-10 — most former findings no longer on live page

**Validation (2026-06-05, folded)**: corrections applied to findings/tier above; provenance in RESEARCH-JOURNAL.md.
---

### MSSP Multi-Tenant Architecture (RQ9)

#### Arctic Wolf Aurora Platform - Multi-Tenant Security Operations

**Authors**: Arctic Wolf
**Date**: 2025
**URL**: https://arcticwolf.com/resources/press-releases/arctic-wolf-2025-security-operations-report-reveals-threat-landscape-acceleration-majority-of-security-alerts-now-occur-outside-working-hours/
**Alt URL**: https://arcticwolf.com/resources/blog/2025-year-in-review/
**Evidence Level**: C (Production platform, quantitative metrics) — re-tiered from A 2026-08-19: not peer-reviewed research and not an official standard
**Relevance**:
- RQ9: Multi-tenant MSSP architecture
- OCSF integration patterns

**Key Findings**:
- Analyzed 330 trillion security observations from 10,000+ organizations
- "Reduced 330 trillion raw observations down to 8.6 million alerts — a noise reduction rate of more than 99.99999%" (page verbatim, seven nines — the entry's prior 99.999% understated Arctic Wolf's own figure; corrected 2026-07-10)
- UpSight Security acquired (Alt URL verbatim: "Arctic Wolf acquired UpSight Security, accelerating our roadmap with predictive, on-device AI capabilities")

**Citations**: MSSP architecture, multi-tenant patterns
**Notes**: Original product page URL (403) replaced with 2025 Security Operations Report; validates multi-tenant at massive scale. Correction (2026-07-10, part-2 sweep fix 4): the "116T→20T (Aug-Oct 2025)", OCSF-normalization, and multi-tenant-portal bullets were removed — none appear on the primary or Alt URL; and the former "Sevco Security acquired Feb 2026" claim was replaced with UpSight (the Alt URL names UpSight, not Sevco — re-add Sevco only with its own primary).

**Validation Status**: ✅ Verified at primary + Alt URL 2026-07-10; noise-reduction figure restated page-verbatim

---

### DuckDB & Edge Processing (Supporting RQ7)

#### DuckDB 1.0-1.4 Production Readiness & LTS

**Authors**: DEV Community, DuckDB Labs
**Date**: 2024-2025 (updated February 2026)
**URL**: https://duckdb.org/2025/09/16/announcing-duckdb-140
**Alt URL**: https://duckdb.org/2024/06/03/announcing-duckdb-100 (v1.0.0 announcement — source for the v1.0 facts below)
**Evidence Level**: B (Community analysis, official release notes)
**Relevance**:
- RQ7: Isolation-first performance
- Edge/embedded analytics

**Key Findings**:
- Version 1.0.0 released June 3, 2024, "codename 'Snow Duck' (anas nivis)" (v1.0.0 announcement verbatim; the v1.4.0 page's release table lists the same 1.0.x line under the Latin "Nivis")
- Stable on-disk storage format: "DuckDB files created with DuckDB 1.0.0 will be compatible with future DuckDB versions" (v1.0.0 announcement verbatim)
- "Download counts are in the millions each month, and download traffic just for extensions is upwards of four terabytes each day" (v1.0.0 announcement verbatim)
- **v1.4.0 LTS** (September 16, 2025): First Long-Term Support release, 1-year support window
- **Iceberg write support** added in v1.4.0 (copy data from DuckDB to Iceberg)
- In-memory checkpointing enables 5-10× performance improvements for some queries
- Rewritten k-way merge sort reduces data movement in sorting/window functions
- 3,500+ commits by 90+ contributors since v1.3.2
- **DuckLake**: ACID-compliant lakehouse format planned for v1.0 in 2026

**Citations**: DuckDB production readiness, adoption metrics, Iceberg integration
**Notes**: v1.4.0 LTS + Iceberg write support validates DuckDB as serious lakehouse component; DuckLake may create new architecture options for isolated SOC deployments. Correction (2026-07-10, part-2 sweep fix 25): the composite was split — v1.0 facts re-sourced to the v1.0.0 announcement (added as Alt URL, verified 2026-07-10) rather than the v1.4.0 page that doesn't carry them; the "Used at Facebook, Google, Airbnb" claim was removed (on neither announcement; no primary located).

**Validation Status**: ✅ Refreshed February 2026 - v1.4.0 LTS current
**Currency (2026-11-17)**: DuckDB v2.0.0 was released 2026-10-21 and the 1.5 line reached v1.5.6 on 2026-09-28 (https://github.com/duckdb/duckdb/releases), so the "v1.4.0 LTS current" status above is history; check the DuckDB release calendar for which line is now LTS before citing.

**Validation (2026-06-05, folded)**: corrections applied to findings/tier above; provenance in RESEARCH-JOURNAL.md.
---

## Reading Queue (Pending Analysis)

The following papers have been identified for future analysis:

#### Hyperscan: A Fast Multi-pattern Regex Matcher for Modern CPUs

**Authors**: Xiang Wang, Yang Hong, Harry Chang, KyoungSoo Park, Geoff Langdale, Jiayu Hu, Heqing Zhu (Intel / KAIST / branchfree.org — roster corrected 2026-07-10 from a garbled name-order list; verified vs NSDI '19 listing, pp. 631-648)
**Date**: 2019
**URL**: https://www.usenix.org/conference/nsdi19/presentation/wang-xiang
**Evidence Level**: A (Peer-reviewed, USENIX NSDI '19)
**Relevance**:
- Query engine performance
- Pattern matching for log analytics
- Security detection engine optimization
- Book ch05 §5.3 + Appendix I [was: Chapter 10] (Query Engines)

**Key Findings**: (Pending full reading)
- High-performance multi-pattern regex matching
- Multi-pattern simultaneous matching
- Relevance to log search/SIEM performance

**Source**: Identified via "Humio Clone" reference collection (December 2025)
**Status**: 📚 QUEUED - Not yet read
**Added**: 2026-01-02
**Refresh (2026-11-23)**: the NSDI '19 page is live (HTTP 200) and its abstract supports the generic findings above, with one figure, an 8.7x Snort speed-up on a real traffic trace. The implementation's status has changed since publication. The intel/hyperscan GitHub repository's last tagged release is v5.4.2 (2023-04-19). The Vectorscan README quotes an Intel document saying "The latest open-source version (BSD-3 license) of Hyperscan on Github is 5.4" and that Intel delivers later releases under an Intel Proprietary License from 5.5; that Intel document was not opened here. The open-source line continues as VectorCamp's Vectorscan (BSD, release 5.4.14 on 2026-11-09), which "aims to be ABI and API compatible with the last open source version of Intel Hyperscan 5.4". A stack built on open components would use Vectorscan, and the paper's design description still applies to the 5.4 code it forked from.

**Validation (2026-06-05, folded)**: corrections applied to findings/tier above; provenance in RESEARCH-JOURNAL.md.
---

#### DBSP: Automatic Incremental View Maintenance for Rich Query Languages

**Authors**: Mihai Budiu, Tej Chajed, Frank McSherry, Leonid Ryzhyk, Val Tannen (verified at the PVLDB PDF 2026-07-10; entry formerly said "Academic paper"/"TBD")
**Date**: 2023 (PVLDB 16(7): 1601-1614; VLDB 2023, Vancouver, August 2023)
**URL**: https://www.vldb.org/pvldb/vol16/p1601-budiu.pdf
**Alt URL**: https://github.com/feldera/feldera (implementation)
**Extended edition**: Budiu, M., Ryzhyk, L., Zellweger, G., Pfaff, B., Suresh, L., Kassing, S., Gyawali, A., Budiu, M., Chajed, T., McSherry, F., Tannen, V. (2025). DBSP: automatic incremental view maintenance for rich query languages. The VLDB Journal 34(4), article 39. https://doi.org/10.1007/s00778-025-00922-y (published online 2025-05-08)
**Evidence Level**: A (Peer-reviewed, PVLDB)
**Relevance**:
- Streaming database patterns
- Incremental computation
- Real-time analytics foundations
- Validates RisingWave, Materialize patterns
- Book ch02 §2.2 (components: collection and pipeline) [was: Chapter 7] (Streaming Architectures)

**Key Findings**: (Pending reading)
- Database operations as streaming primitives
- Incremental view maintenance
- Mathematical foundations for stream processing

**Source**: Identified via "Humio Clone" reference collection (December 2025)
**Status**: 📚 QUEUED - Not yet read
**Added**: 2026-01-02
**Refresh (2026-11-23)**: the PVLDB 2023 paper is still the original and is still live. An extended journal edition appeared in The VLDB Journal in 2025 (Crossref, DOI above). Per the author's manuscript at mihaibudiu.github.io/work/budiu-vldb25.pdf, it adds new incremental-program examples, standard-SQL semantics, a longer implementation section and a preliminary evaluation, and it says the proofs are formalized in Lean in a separate cited work. Read the journal edition first when this entry moves out of the queue. Both editions are Level A.

---

#### Xor Filters: Faster and Smaller Than Bloom and Cuckoo Filters

**Authors**: Thomas Mueller Graf, Daniel Lemire (verified at the arXiv record 2026-08-19; entry formerly said "Academic paper"/"TBD", the same placeholder defect the 2026-07 sweep fixed on the DBSP entry and missed here)
**Date**: 2020 (Journal of Experimental Algorithmics 25(1), 2020; arXiv v3 27 Jan 2020, submitted 17 Dec 2019)
**URL**: https://arxiv.org/abs/1912.08258
**Evidence Level**: A (peer-reviewed — ACM Journal of Experimental Algorithmics; the arXiv record names the journal in its Journal-reference field, so this is not a venue-less preprint)
**Relevance**:
- Indexing optimization
- Log analytics performance
- Probabilistic data structures
- Alternative to Bloom filters for membership testing
- Book ch05 §5.1 (table format) [was: Chapter 8] (Storage Optimization)

**Key Findings**: (Pending reading)
- Faster lookup than Bloom filters
- Smaller memory footprint
- Immutable filter construction
- Relevance to log indexing optimization

**Source**: Identified via "Humio Clone" reference collection (December 2025)
**Status**: 📚 QUEUED - Not yet read
**Added**: 2026-01-02

**Citations**: Graf, T. M., & Lemire, D. (2020). *Xor Filters: Faster and Smaller Than Bloom and Cuckoo Filters*. Journal of Experimental Algorithmics, 25(1). arXiv:1912.08258.
**Validation Status**: ✅ Authors, title, date and venue verified at the arXiv record 2026-08-19. Claim-vs-source was already checked in the 2026-07 sweep (RESEARCH-JOURNAL.md: Graf & Lemire; the entry's "8.2 bits" reads ~9.2-9.8 in the paper, logged as a minor mismatch) — that verification was never written back into this entry, which is why it still carried a placeholder byline.
**Refresh (2026-11-23)**: arXiv record live; the venue (ACM JEA 25, 2020, DOI 10.1145/3376122) is confirmed at Crossref. The same authors published a follow-up, Graf, T. M., & Lemire, D. (2022). *Binary Fuse Filters: Fast and Smaller Than Xor Filters*. ACM Journal of Experimental Algorithmics 27. https://doi.org/10.1145/3510449. By its title it claims a faster and smaller filter for the same membership-testing job, so a reader choosing a filter today should read it alongside this paper; its text was not read in this pass. This paper is still accurate and is not superseded as a citation for xor filters.

---

## Sources Merged from the Author's Research Notes (June 2026)

Academic, framework, standards and practitioner publications merged in June 2026 from the author's
private research notes, which held published works this book-focused bibliography lacked. Only
published works are merged here; nothing about outreach or relationships is reproduced. URLs marked
*verified 2026-06-05* were status-checked at merge time, and the 2026-11-17 verification ledger
(`methods/verification-2026-11/ledger.json`) records the current existence check for every entry.

### Academic & Peer-Reviewed

#### Matryoshka — Semantic-Aware Parsing for Security Logs

**Authors**: Julien Piet, Vivian Fang, Rishi Khare, Scott Coull, Vern Paxson, Raluca Ada Popa, David Wagner (UC Berkeley + Google — full roster verified at arXiv 2026-07-10; entry formerly credited Piet alone with the informal "Log Parsing" title)
**Date**: 2025 (arXiv 2506.17512; entry formerly said 2024)
**URL**: https://people.eecs.berkeley.edu/~julien.piet/matryoshka.pdf
**Alt URL**: https://arxiv.org/abs/2506.17512
**Evidence Level**: B (peer-reviewed academic research) — re-tiered from A 2026-08-19: not peer-reviewed research and not an official standard
**Relevance**:
- Semantic-aware parsing methodology directly applicable to Zeek → OCSF transformation
- Book ch04 §4.2 (OCSF) + Appendix H [was: Chapter 8] (OCSF mapping), Appendix F (mapping implementation)
- Grounds the parsing-fidelity argument that field mapping is a semantic problem, not a syntactic one

**Citations**: Piet, J., Fang, V., Khare, R., Coull, S., Paxson, V., Popa, R.A., Wagner, D. (2025). *Semantic-Aware Parsing for Security Logs*. arXiv:2506.17512.
**Validation Status**: ✅ Verified at arXiv 2026-07-10 (part-2 sweep fix 29): title, seven-author roster, and affiliations corrected

---

#### Mining Temporal Attack Patterns from Cyberthreat Intelligence Reports

**Authors**: Md Rayhanur Rahman, Brandon Wroblewski, Quinn Matthews, Brantley Morgan, Tim Menzies, Laurie Williams (author list verified at the arXiv record 2026-11-07)
**Date**: 2025 (Knowledge and Information Systems 67(10), published online 2025-07-22; arXiv v1 2024-01-03)
**URL**: https://doi.org/10.1007/s10115-025-02491-6
**Alt URL**: https://arxiv.org/abs/2401.01883 (preprint v1)
**Evidence Level**: A (peer-reviewed journal, Knowledge and Information Systems, 2025; re-tiered B to A 2026-11-23 once the published venue was found)
**Relevance**:
- Temporal attack-pattern detection from CTI narrative reports
- Threat-modeling and detection-engineering research foundation

**Citations**: Rahman, M.R., Wroblewski, B., Matthews, Q., Morgan, B., Menzies, T., Williams, L. (2025). Mining temporal attack patterns from cyberthreat intelligence reports. *Knowledge and Information Systems*, 67(10), 8941-8981. https://doi.org/10.1007/s10115-025-02491-6. Preprint arXiv:2401.01883.
**Validation Status**: ✅ Active URL (verified 2026-06-05)
**Re-tiered (2026-11-07)**: A → B. The entry was tiered A as "academic research, preprint" with no author list and no venue, which §3.1 says does not qualify; authors filled from the arXiv record, description unchanged.
**Refresh (2026-11-23)**: the paper was published in Knowledge and Information Systems (Crossref record, same six authors, online 2025-07-22), so the entry returns to Level A on the journal version. The 2026-11-07 re-tier was right about the entry as it then stood, an arXiv record with no venue, but it missed the journal version, which was already online and which the arXiv record still does not link. The journal abstract at Crossref keeps the preprint's figures (713 reports, 124 patterns, nine categories) and adds that ChronoCTI "demonstrates higher precision but lower recall performance on a real-world dataset of 94 CTI reports". The journal full text was not read.

---

#### F3: The Open-Source Data File Format for the Future

**Authors**: Xinyu Zeng, Ruijun Meng, Martin Prammer, Wes McKinney, Jignesh M. Patel, Andrew Pavlo, Huanchen Zhang (CMU Database Group + Wisconsin-Madison + Apache Arrow)
**Date**: September 2025 (SIGMOD)
**URL**: https://db.cs.cmu.edu/papers/2025/zeng-sigmod2025.pdf
**Alt URL**: https://github.com/future-file-format/f3
**Evidence Level**: A (peer-reviewed, SIGMOD 2025)
**Relevance**:
- WebAssembly-embedded decoders for self-describing, platform-independent columnar files
- Addresses Parquet row-group layout limitations; next-generation columnar format research
- Book ch05 §5.1 (table format) [was: Chapter 9] (format war), long-term forensic data preservation
- Research prototype, not production-ready (label accordingly)

**Citations**: Zeng, X., Meng, R., Prammer, M., McKinney, W., Patel, J. M., Pavlo, A., & Zhang, H. (2025). *F3: The Open-Source Data File Format for the Future*. Proc. ACM Manag. Data, 3(4). **DOI: 10.1145/3749163** (verified resolves to F3 at ACM DL, 2026-06-13).
**Validation Status**: ✅ Active URL (verified 2026-06-05); DOI added + venue/author list re-confirmed 2026-06-13. Correction (2026-07-10, part-2 sweep fix 30 — the 2026-06-13 note above had it inverted): the paper itself fixes the decoder size verbatim — "Wasm binary size for the two custom encodings is approximately 150 KB—negligible compared to the achieved size reduction" (verified at the SIGMOD 2025 PDF; full-text grep finds no "0.001%" anywhere in the paper). Cite ~150 KB as paper-primary; the "~0.001% overhead" phrasing is what has no paper support.

---

#### The Base-Rate Fallacy and the Difficulty of Intrusion Detection

**Authors**: Stefan Axelsson
**Date**: 2000 (ACM TISSEC 3(3):186-205; earlier version ACM CCS 1999)
**URL**: https://dl.acm.org/doi/10.1145/357830.357849
**Evidence Level**: A (Peer-reviewed journal, ACM Transactions on Information and System Security)
**Relevance**:
- D3FEND Wall AIML-ripeness evidence: the formal limit on the statistical-anomaly detector tier (PHDURA, UGLPA, anomaly-mode CSPP/PMAD)
- /research/d3fend-wall essay (securitydataworks.com): "Axelsson named the arithmetic underneath" the anomaly-detection difficulty
- Foundational anchor for the alert-fatigue / false-positive-scaling argument

**Key Findings**:
- Because the base rate of genuine intrusions is extremely low against benign volume, the false-positive rate — not the detection rate — caps the usable accuracy of an intrusion-detection system (Bayesian posterior P(intrusion|alarm) stays low even at small false-alarm rates)
- The number that binds is the false-positive rate against the base rate, not the headline true-positive rate or accuracy
- Formal backbone of what operators experience as alert fatigue

**Citations**: AIML-RIPENESS-EVIDENCE.md (statistical-anomaly tier limit); /research/d3fend-wall essay (the base-rate arithmetic under anomaly detection)
**Notes**: Cited inline in already-public content (the d3fend-wall essay) — catalogued here 2026-06-21 to close that citation breach. Tier A under the strict tiers in METHODOLOGY.md §3.1 (peer-reviewed ACM journal). Refresh (2026-11-23): Erbacher, 'Base-Rate Fallacy Redux and a Deep Dive Review in Cybersecurity' (arXiv:2203.08801, 2022, single version, no journal reference on arXiv) re-examines Axelsson's argument and argues that false positives deserve the same depth of analysis as true positives; abstract read only, so cite it for direction.

**Validation Status**: ✅ Verified 2026-06-21 (DBLP rec journals/tissec/Axelsson00: ACM TISSEC vol 3, issue 3, pp.186-205, 2000, DOI 10.1145/357830.357849). · Re-verified 2026-11-23: abstract read at a hosted copy of the TISSEC PDF (profsandhu.com/cs6393_s20/p186-axelsson.pdf); 'the false alarm rate is the limiting factor for the performance of an intrusion detection system' is verbatim, and the paper's worked scenario requires a detection rate of 0.7 at a false alarm rate of 1/100,000 per event. The ACM DOI page returns 403 to automated fetch, so Crossref (TISSEC 3(3):186-205) stands in for the landing page.

---

#### Outside the Closed World: On Using Machine Learning for Network Intrusion Detection

**Authors**: Robin Sommer, Vern Paxson
**Date**: 2010 (IEEE Symposium on Security and Privacy / Oakland, pp.305-316)
**URL**: https://dl.acm.org/doi/10.1109/SP.2010.25
**Alt URL**: https://www.icir.org/robin/papers/oakland10-ml.pdf (author-hosted PDF)
**Evidence Level**: A (Peer-reviewed, IEEE S&P; 2020 IEEE S&P Test-of-Time Award)
**Relevance**:
- D3FEND Wall AIML-ripeness evidence: why anomaly detection is the hardest place to make ML work, against the structural-optimist 'models belong in the broad base' reading
- /research/d3fend-wall essay (securitydataworks.com): 'reasons on the record since Sommer and Paxson's 2010 paper' for why ML struggles at network anomaly detection
- Anchor for the ripe-is-not-solved caveat

**Key Findings**:
- ML is good at finding what resembles its training data, but detection must find the novel attack — anomaly detection inverts ML's natural strength
- Error costs in NIDS are extreme and asymmetric
- A wide semantic gap separates 'an anomaly' from 'an attack'
- Network traffic has no stable notion of 'normal' to learn
- Training data is scarce, and sound evaluation is fundamentally difficult, with the lack of appropriate public datasets named as the biggest evaluation obstacle (the authors list training data and evaluation as two separate challenges)
- Recommendations (Section IV): understand the threat model, keep the scope narrow, reduce the cost of errors (including giving the analyst more context to speed manual inspection), and evaluate soundly; the authors 'do not consider machine-learning an inappropriate tool for intrusion detection'

**Citations**: AIML-RIPENESS-EVIDENCE.md (anomaly-detection difficulty); /research/d3fend-wall essay (the on-the-record reasons ML is hardest at anomaly detection)
**Notes**: Cited inline in already-public content (the d3fend-wall essay) — catalogued here 2026-06-21 to close that citation breach. Tier A (peer-reviewed IEEE S&P; 2020 Test-of-Time Award). Authors are the Corelight/Zeek co-founders.

**Validation Status**: ✅ Verified 2026-06-21 (DBLP rec conf/sp/SommerP10: IEEE S&P 2010, pp.305-316, DOI 10.1109/SP.2010.25; 2020 Test-of-Time Award confirmed via ICSI Berkeley and the IEEE-Security SP2020 awards page). · Re-verified 2026-11-23 at the author-hosted PDF: the five challenges and the 'not an inappropriate tool' sentence are verbatim; 'keep a human in the loop' is not a stated recommendation in the paper and was replaced with the Section IV recommendation headings.

---

#### Ursa: A Lakehouse-Native Data Streaming Engine for Kafka (StreamNative, PVLDB 2025)

**Authors**: Matteo Merli, Sijie Guo, Penghui Li, Hang Chen, Neng Lu (StreamNative — roster verified at the PVLDB PDF 2026-07-10; entry formerly said "Guo et al.")
**Date**: 2025 (PVLDB Vol. 18(12):5184-5196; VLDB 2025 Industry Track — Best Industry Paper)
**URL**: https://www.vldb.org/pvldb/vol18/p5184-guo.pdf
**DOI**: 10.14778/3750601.3750636
**Evidence Level**: A (Peer-reviewed, VLDB 2025 Best Industry Paper; also carries production-quantitative field measurements)
**Relevance**:
- Hypothesis H-ARCH-01 (Iceberg/lakehouse convergence) + streaming↔storage convergence
- Research Question RQ11 (LIGER stack vs traditional SIEM — ingest layer)
- Book ch02 §2.2 (components: collection and pipeline) [was: Chapter 7] (Streaming) / ch05 §5.1 (table format) [was: Chapter 8] (Storage formats)

**Key Findings** (all verified verbatim at the VLDB PDF primary, 2026-07-09):
- Kafka-compatible engine that writes topics directly to open lakehouse tables (Apache Iceberg or Delta Lake) on object storage — leaderless, no disk-based broker storage, no external connectors
- ~5 GB/s sustained publish and consume throughput across tested configurations (§7.1)
- Production field measurement: infrastructure spend ≈ 5% of a comparably sized Kafka stack (§7.5, two years continuous production on StreamNative Cloud across AWS/GCP/Azure)
- Benchmark headline: up to 10× infrastructure-cost reduction; Figure 10 reports 92% reduction vs Kafka-Disk (~8% of cost) and 78% vs Kafka-TS (~22%) (figure reference corrected from Table 1, 2026-07-10). The ~5% production figure and the 10× benchmark headline are distinct numbers, catalogued separately
- Object storage's internal replication removes Ursa's need to replicate across zones (vs Kafka keeping three replicas)

**Citations**: H-ARCH streaming↔lakehouse convergence; RQ11 ingest-layer evidence — the "topics ARE Iceberg tables" pattern removes the connector hop between the detection pipeline and the security data lake
**Notes**: Peer-reviewed primary (clean Tier A). Vendor-authored (StreamNative) but venue-refereed; production figures are self-reported field measurements corroborated by the paper's benchmarks.

**Validation Status**: ✅ Verified 2026-07-09 (VLDB proceedings PDF fetched; all six sub-claims + venue/award confirmed at primary)

---

#### Log Parsing Evaluation in the Era of Modern Software Systems (Petrescu et al., ISSRE 2023)

**Authors**: Stefan Petrescu, Floris Den Hengst, Alexandru Uta, Jan S. Rellermeyer (Leibniz University Hannover; ING Analytics; DFINITY; affiliations from the arXiv title page)
**Date**: 2023 (2023 IEEE 34th International Symposium on Software Reliability Engineering, ISSRE; published 2023-10-09)
**URL**: https://doi.org/10.1109/ISSRE59848.2023.00019
**Alt URL**: https://arxiv.org/abs/2308.09003 (preprint)
**DOI**: 10.1109/ISSRE59848.2023.00019
**Evidence Level**: A (peer-reviewed, IEEE ISSRE 2023)
**Relevance**:
- Book ch03 ("bad parsing logic" in the four-defect list): the strongest outside anchor for parsers that fail silently, because the usual evaluation metric reports success while the extracted templates are mostly wrong.
- Scope limit: these are operational application logs from a large bank plus public LogHub-style benchmarks, and a template-level metric. It does not measure the share of unusable production *security* data, so it supports the mechanism and never the chapter's first-hand ~30% figure.

**Key Findings** (read at the arXiv preprint text, Finding 1 and the Finding 3 discussion; Tables II and III): 14 widely used log parsers were assessed. "Previous studies obtained parsing accuracy average results of 0.73 [10]; however, under the considered metric, an average log template accuracy of 0.2 is obtained" (about 400 of 2,000 templates matched rather than the 1,460 the grouping metric implies). On the bank's industry dataset "the highest log template accuracy is roughly 0.05", about 100 of 2,000 messages parsed correctly. The 0.73 is the earlier literature's reported grouping accuracy that the paper re-evaluates, not a new measurement by these authors.
**Citations**: Petrescu, S., Den Hengst, F., Uta, A., & Rellermeyer, J. S. (2023). *Log Parsing Evaluation in the Era of Modern Software Systems*. 2023 IEEE 34th International Symposium on Software Reliability Engineering (ISSRE), 379-390. DOI 10.1109/ISSRE59848.2023.00019.
**Notes**: Found via the 2026-11-07 Jenova academic citation check (row 9, verdict V). Figures were read at the arXiv preprint (2308.09003); the IEEE version of record was not fetched, so the wording of the quoted sentences may differ slightly in the published text. Refresh (2026-11-23): no follow-up by the same authors found. Two later studies sit beside it: Jiang et al., 'A Large-Scale Evaluation for Log Parsing Techniques: How Far Are We?' (ISSTA 2024, DOI 10.1145/3650212.3652123, which introduces Loghub-2.0), and Beck, Landauer, Wurzenberger, Skopik and Rauber, 'System Log Parsing with Large Language Models: A Review' (arXiv:2504.04877, 2025), which reviews 29 LLM-based parsers, benchmarks seven, and critically assesses the comparability and reproducibility of reported results. Neither was read for figures, so cite them for direction only.
**Validation Status**: ✅ Verified 2026-11-07 (Crossref API record for title, four authors, venue, pages 379-390 and DOI; figures at the arXiv preprint text). · Figures re-read at the arXiv PDF and DOI confirmed to redirect to IEEE Xplore document 10301279 (2026-11-23).

---

#### From Attack Scenario to Measurable Detection Improvement: A Knowledge-Driven ATT&CK/D3FEND Framework for Instrumented Purple Teaming (Madani et al., C&ESAR 2026)

**Authors**: Tristan Madani (CEDRIC Lab, CNAM), Yulliwas Ameur, Samia Bouzefrane
**Date**: November 2026 (C&ESAR 2026, Computer & Electronics Security Applications Rendez-vous, European Cyber Week, Rennes)
**URL**: https://hal.science/hal-05743354v1
**Alt URL**: https://2026.cesar-conference.org/accepted-papers/ (listed on the accepted-papers page)
**Evidence Level**: B (accepted conference paper; venue confirmed, but the C&ESAR site describes selection by relevance, clarity and pedagogical value without describing peer review, and the CEUR-WS proceedings volume is not yet published; eligible for re-tier to A once the proceedings index)
**Relevance**:
- Book ch04 (the ATT&CK/D3FEND join and "a coverage count rather than a measured detection rate"): the one study found that tests a technique-to-data-source-to-rule knowledge graph against adversary-emulation ground truth.
- Scope limit, in the authors' own abstract: "CTI knowledge graphs map threats to countermeasures without ever testing whether those countermeasures fire on real telemetry." The paper validates the detection chain; it is not evidence that D3FEND's artifact-mediated countermeasure edges are validated.

**Key Findings** (abstract only): evaluated on four CTID adversary-emulation profiles (APT29, FIN6, Sandworm, Wizard Spider), a four-step detection maturity ladder "raises strict coverage from C0 = 23.1% (out-of-the-box SIEM) to C3 = 71.6% (with KG-generated rules)", with the KG-guided rule-engineering step alone contributing +30.3 percentage points on average; the pre-set decision rule (ΔC3 > 0.10 in at least 3 of 4 scenarios) held in all four.
**Citations**: Madani, T., Ameur, Y., & Bouzefrane, S. (2026). *From Attack Scenario to Measurable Detection Improvement: A Knowledge-Driven ATT&CK/D3FEND Framework for Instrumented Purple Teaming*. C&ESAR 2026, Rennes. HAL hal-05743354.
**Notes**: Found via the 2026-11-07 Jenova academic citation check (row 12, verdict M: Jenova's "WACCO/ANUBIS" venue was wrong). No Crossref DOI exists yet. Only the abstract figures are verified; the full-text figures circulated in the ensemble report (+33.1 pp effective coverage, 2,396 community Sigma rules, 0 pp strict gain from those rules) are unconfirmed and must not be cited from this entry.
**Validation Status**: ✅ Verified 2026-11-07 (HAL API record for title, authors, venue, date and abstract; C&ESAR 2026 accepted-papers page lists the paper). Abstract figures only.

---

### Frameworks & Standards

#### MITRE D3FEND Framework & Ontology

**Authors**: MITRE (funded by NSA and OUSD)
**Date**: 2024-2026 (ongoing). Milestones: v1.0 launched 2025-01-16 (research-project → production ontology); OT extension + v1.3.0 line 2025-12 (267 techniques, 7 tactical categories). See the dedicated "MITRE D3FEND for OT" entry in the 2026 Format & Standards section.
**URL**: https://d3fend.mitre.org/
**Alt URL**: https://d3fend.mitre.org/changelog/ (release history) · https://www.mitre.org/news-insights/news-release/mitre-launches-d3fend-10-milestone-cybersecurity-ontology (v1.0 launch)
**Evidence Level**: A (framework authority, formal ontology — OWL 2 DL) — HELD AT A 2026-08-19 (owner ruling): a normative reference document from a neutral, non-commercial body, published as a versioned formal specification, which is the same evidentiary position as a NIST or ISO document. SCOPE: primary for taxonomy and structure, and silent on efficacy — it is authoritative about what the framework says, never evidence that following it works.
**Relevance**:
- Defensive-technique ontology; the defensive counterpart to ATT&CK
- The OCSF ↔ D3FEND grounding chain (D3FEND → CCO → BFO) central to the grounding work — ch04 §4.1 (D3FEND) [was: Chapter 3], ch04 §4.2 (OCSF) + Appendix H [was: Chapter 8], Appendix F
- Digital-artifact / offense-defense inferred matrix; semantic compliance mapping

**Citations**: MITRE. *D3FEND: A Knowledge Graph of Cybersecurity Countermeasures*. https://d3fend.mitre.org/
**Notes**: A glaring prior gap — absent from this bibliography despite being central to the current grounding research. *Version-line note (2026-06-05, FLAG closed 2026-07-10): the live d3fend.mitre.org version badge reads **v1.4.0** (fetch-confirmed in the part-2 sweep), reconciling the prior tension — v1.3.0 (Dec 2025) carried the OT extension, and v1.4.0 is now current. Quote v1.4.0 as current.* (Superseded 2026-11-17 by the Currency line below: 1.6.0 is now current.)
**Validation Status**: ✅ Active URL (verified 2026-06-05); v1.0/OT milestones verified via WebSearch
**Currency (2026-11-17)**: the live d3fend.mitre.org version badge reads 1.6.0 (release date 2026-08-31 in the site's version record); quote 1.6.0 as current (line added 2026-11-22, moved from a note in another entry).

---

#### MITRE ATLAS (Adversarial Threat Landscape for AI Systems)

**Authors**: MITRE
**Date**: 2024-2025 (AI-agent techniques added Oct 2024)
**URL**: https://atlas.mitre.org/
**Evidence Level**: A (framework authority) — HELD AT A 2026-08-19 (owner ruling): a normative reference document from a neutral, non-commercial body, published as a versioned formal specification, which is the same evidentiary position as a NIST or ISO document. SCOPE: primary for taxonomy and structure, and silent on efficacy — it is authoritative about what the framework says, never evidence that following it works.
**Relevance**:
- AI/ML version of ATT&CK; threat taxonomy for AI-powered tools and agents
- New AI-agent techniques: AML.T0080 (context poisoning), AML.T0082 (RAG credential harvesting), AML.T0084, AML.T0086
- Detection engineering for AI-security

**Citations**: MITRE. *ATLAS: Adversarial Threat Landscape for Artificial-Intelligence Systems*. https://atlas.mitre.org/
**Validation Status**: ✅ Active URL (verified 2026-06-05)

---

#### Secure Controls Framework (SCF)

**Authors**: Secure Controls Framework Council
**Date**: 2024-2026 (continuously updated)
**URL**: https://www.securecontrolsframework.com/
**Evidence Level**: C (framework; independent validation advised)
**Relevance**:
- "1,500+ Controls across 34 domains" mapped to "200+ Laws, regulations & frameworks" (site verbatim, SCF v2026.2 — refreshed 2026-07-10 from the stale 1,200+/150+ figures)
- D3FEND ↔ SCF control mapping; compliance-control reconciliation

**Citations**: Secure Controls Framework Council. *Secure Controls Framework*. https://www.securecontrolsframework.com/
**Validation Status**: ✅ Verified at primary 2026-07-10 (counts refreshed to v2026.2)

---

#### NIST Cybersecurity Framework (CSF 2.0)

**Authors**: NIST
**Date**: 2024 (CSF 2.0)
**URL**: https://www.nist.gov/cyberframework
**Evidence Level**: A (official government standard)
**Relevance**:
- Compliance-framework baseline; control-mapping reference
- Vendor-filtering and capability-mapping (NIST CSF 2.0 functions)

**Citations**: NIST. *Cybersecurity Framework 2.0* (2024). https://www.nist.gov/cyberframework
**Notes**: Refresh (2026-11-23): CSF 2.0 (2024) is still the current version. NIST's Cyber AI Profile, NIST IR 8596 (initial preliminary draft dated 2025-12-16, comment period closed 2026-01-30, https://csrc.nist.gov/pubs/ir/8596/iprd), is a CSF 2.0 Community Profile with three focus areas: securing AI system components, conducting AI-enabled cyber defense, and thwarting AI-enabled cyber attacks. It was still a preliminary draft on 2026-11-23, so cite it as in-progress guidance and never as a standard.
**Validation Status**: ✅ Active URL (verified 2026-06-05; re-verified 2026-11-23, still the CSF 2.0 Resource Center, no successor version)

---

#### CISA / ICS-CERT Industrial Control Systems Guidance

**Authors**: CISA (Cybersecurity and Infrastructure Security Agency)
**Date**: ongoing
**URL**: https://www.cisa.gov/topics/industrial-control-systems
**Evidence Level**: B (government guidance)
**Relevance**:
- OT/ICS security; OT-IT convergence
- Critical-infrastructure security framing for the OT chapters/sections

**Citations**: CISA. *Industrial Control Systems*. https://www.cisa.gov/topics/industrial-control-systems
**Validation Status**: ⏳ Carried from the June 2026 merge; existence re-checked 2026-11-17 (see `methods/verification-2026-11/ledger.json`)

---

#### CoSAI — Coalition for Secure AI (OASIS)

**Authors**: OASIS / CoSAI
**Date**: 2024-2025
**URL**: https://github.com/cosai-oasis/ws2-defenders
**Evidence Level**: B (industry consortium)
**Relevance**:
- WS2 — preparing defenders for a changing cybersecurity landscape
- AI-security best practices and defender readiness

**Citations**: OASIS CoSAI. *WS2: Preparing Defenders*. https://github.com/cosai-oasis/ws2-defenders
**Validation Status**: ✅ Active URL (verified 2026-06-05)

---

#### MITRE Cyber Analytics Repository (CAR) — Analytics Mapped to ATT&CK

**Authors**: MITRE Corporation (MITRE ATT&CK team)
**Date**: 2015 onward; newest analytic CAR-2022-03-001 (merged 2022-04), analytics last edited 2023-08, repository last changed 2025-05 (checked 2026-11-23)
**URL**: https://car.mitre.org/
**Alt URL**: https://github.com/mitre-attack/car (analytics + data model, Apache-2.0)
**Evidence Level**: B (official MITRE practitioner/operational catalogue; not peer-reviewed research)
**Relevance**:
- Detection-coverage measurement: each CAR analytic carries an explicit mapping to one or more ATT&CK technique IDs, so a detection corpus can be scored by which techniques its analytics cover. This is the analytic-to-technique side of a coverage corpus (the rules), complementary to a malicious-test catalogue (the needles).
- Supports the ATT&CK-coverage / detection-engineering threads and the D3FEND-coverage work (analytics expressed against a CAR-style abstract data model travel across telemetry schemas).

**Key Findings**: CAR is a knowledge base of analytics organized around the ATT&CK adversary model. Each analytic includes a description, the ATT&CK technique(s)/tactic(s) it addresses, pseudocode, and — where available — reference implementations (e.g., Splunk SPL, EQL) plus a unit/coverage note. Analytics are written against the **CAR Data Model (CARDM)**, an abstraction of host/network telemetry (objects like process, flow, file) that decouples the analytic logic from any one product's field names. A coverage view maps the analytic set onto the ATT&CK matrix. Treat CAR as a curated reference set, not an exhaustive one — it covers a subset of ATT&CK techniques, so "covered by CAR" is a floor, not the universe. Refresh (2026-11-23): the repository holds 102 analytics and has added none since April 2022, so treat CAR as a stable reference set and not a growing one. ATT&CK v18 (October 2025) replaced in-technique detections with Detection Strategies and Analytics objects and deprecated Data Sources; Enterprise ATT&CK carried 691 Detection Strategies, 1,739 Analytics and 106 Data Components at v18 and 703, 1,770 and 106 at v20 (October 2026, current on the check date), per MITRE's update notes, which makes ATT&CK's own analytics the larger MITRE analytic-to-technique corpus.
**Citations**: ATT&CK-coverage / detection-engineering framing; the analytic↔technique mapping that anchors detection-coverage scoring.
**Notes**: Tier B under the strict tiers — authoritative operational catalogue from MITRE, but a curated analytics repository rather than peer-reviewed research or a ratified standard. Cite the analytic's ATT&CK technique ID(s) and the CAR analytic ID (e.g., CAR-2013-xx-xxx); confirm an analytic's current implementations at the repo before citing one, since CAR is updated over time.
**Validation Status**: ✅ Verified at primary 2026-11-23 (GitHub API: 102 analytics, newest CAR-2022-03-001 merged 2022-04-18, last repository commit 2025-05-16; ATT&CK counts from the attack.mitre.org October 2025 and October 2026 update pages). Confirm per-analytic implementations at the primary before citing one.

---

#### Atomic Red Team — Per-Technique Atomic Tests Mapped to ATT&CK

**Authors**: Red Canary (community-maintained, open source)
**Date**: 2017–present (continuously updated)
**URL**: https://github.com/redcanaryco/atomic-red-team
**Alt URL**: https://atomicredteam.io/ (project site / docs)
**Evidence Level**: B (operational open-source testing library; MIT License; not peer-reviewed)
**Relevance**:
- Detection-coverage measurement: provides small, portable "atomic" tests, each mapped to a specific ATT&CK technique/sub-technique, that execute real (benign-by-design) attacker behaviors. These are the malicious needles a coverage corpus plants — you run the atomic for a technique, then check whether your detection set fired, which makes per-technique catch rate measurable rather than asserted.
- Pairs with an analytic catalogue (e.g., MITRE CAR) and with the D3FEND-coverage work: CAR/Sigma supplies the rules keyed to ATT&CK, Atomic Red Team supplies the activity keyed to the same techniques, so coverage is testable end-to-end against one technique vocabulary.

**Key Findings**: A library of executable tests organized by ATT&CK technique ID. Each test is "atomic" — small, self-contained, dependency-light, and meant to exercise a single technique (often via command-line / scripted execution across Windows, macOS, Linux). Tests are defined in a structured YAML format and can be driven by the companion **Invoke-AtomicRedTeam** (PowerShell) execution framework. MIT-licensed and community-maintained under Red Canary. Coverage is broad but not total across the ATT&CK matrix, and a passing atomic exercises one variant of a technique, so "the atomic fired a detection" measures that variant, not the whole technique — frame catch rate as injected-and-tested, not field-validated.
**Citations**: Detection-coverage / detection-engineering threads; the technique-keyed adversary-activity side that complements CAR/Sigma analytics in a coverage corpus.
**Notes**: Tier B under the strict tiers — widely-used operational testing library from a credible vendor, but an open-source test catalogue rather than peer-reviewed research or a standard. Cite the atomic's ATT&CK technique ID and the test name/GUID; confirm a given test's current definition at the repo before citing specifics, since the library changes. Synthetic/benign-by-design execution only — do not pipe raw execution telemetry into context.
**Validation Status**: ✅ Verified at primary 2026-11-23 (GitHub README and API: MIT, active maintenance, README badge read 1,950 atomics that day; Invoke-Atomic runner repository last pushed 2025-09-08). Confirm any technique-coverage count or specific test GUID at the primary before quoting one.

---

#### MITRE D3FEND 1.0 (Cybersecurity Countermeasures Ontology)

**Authors**: MITRE (D3FEND project led by Peter Kaloroumakis, Principal Applied Ontologist; funded by NSA / OUSD)
**Date**: D3FEND 1.0 launched 2025-01-16 (research project → production ontology). The v1.3.0 line (Dec 2025) adds the OT extension — see the dedicated "MITRE D3FEND for OT" entry.
**URL**: https://d3fend.mitre.org/
**Alt URL**: https://www.mitre.org/news-insights/news-release/mitre-launches-d3fend-10-milestone-cybersecurity-ontology (1.0 launch) · https://github.com/d3fend/d3fend-ontology (ontology distribution source)
**Evidence Level**: A (framework authority + formal ontology — OWL 2 DL; the 1.0 milestone is the official MITRE production release framing) — HELD AT A 2026-08-19 (owner ruling): a normative reference document from a neutral, non-commercial body, published as a versioned formal specification, which is the same evidentiary position as a NIST or ISO document. SCOPE: primary for taxonomy and structure, and silent on efficacy — it is authoritative about what the framework says, never evidence that following it works.
**Relevance**:
- The defensive-technique ontology cross-referenced in the book appendix's D3FEND cross-ref; the grounding chain D3FEND → CCO → BFO
- D3FEND 1.0 ships D3FEND Core Classes, an interface enabling alignment to major upper ontologies — the design hook that lets the grounding chain reach BFO
- 400+ digital artifacts; offense (ATT&CK) ↔ defense inferred relationships *(Unverified 2026-11-17: not on the D3FEND site or repository pages read that day.)*

**Citations**: MITRE. *D3FEND: A Knowledge Graph of Cybersecurity Countermeasures*. https://d3fend.mitre.org/ ; MITRE (2025, Jan 16). *MITRE Launches D3FEND 1.0 — A Milestone in Cybersecurity Ontology*.
**Notes**: "1.0" is the official MITRE release framing (production ontology), confirmed via the MITRE news release. Built on OWL 2 DL; Core Classes provide the upper-ontology alignment interface. CCO mapping is in-progress work, not a shipped 1.0 mapping — do not cite it as complete. Cross-reference: the existing "MITRE D3FEND Framework & Ontology" entry above catalogues the broader framework and the same v1.0/OT version line; this entry is the milestone-specific 1.0-ontology anchor for the grounding-chain work.
**Validation Status**: ✅ Verified 2026-06-21 (WebSearch: 1.0 launch 2025-01-16 + OWL 2 DL + Core Classes upper-ontology interface confirmed via mitre.org release; Kaloroumakis as project lead confirmed). · ⚠️ 1 figure unverified 2026-11-17, see the dated label
**Currency (2026-11-17)**: the live d3fend.mitre.org version badge reads 1.6.0 (release date 2026-08-31 in the site's version record); quote 1.6.0 as current.

---

#### Basic Formal Ontology (BFO) — ISO/IEC 21838-2:2021

**Authors**: ISO/IEC JTC 1 (joint ISO + IEC committee); BFO authored by Barry Smith et al. (BFO 2020 release standardized by the document)
**Date**: Published November 2021 (ISO/IEC 21838-2:2021). Note the version distinction: the ontology release is named "BFO 2020"; the ISO/IEC standard document is dated 2021 — cite the standard as 21838-2:2021.
**URL**: https://www.iso.org/standard/74572.html
**Alt URL**: https://github.com/BFO-ontology/BFO-2020 (artifacts specified in ISO 21838-2:2020/2021) · https://en.wikipedia.org/wiki/Basic_Formal_Ontology · https://webstore.iec.ch/en/publication/72703 (IEC catalogue record, fetchable)
**Evidence Level**: A (official ISO/IEC international standard)
**Relevance**:
- The top-level (upper) ontology at the base of the grounding chain D3FEND → CCO → BFO referenced in the book appendix
- 21838 is the "Top-level ontologies (TLO)" family; Part 2 is BFO — establishes BFO as a conformant top-level ontology for interchange across heterogeneous information systems
- Anchors the formal-ontology rigor the grounding work imports into the OCSF ↔ D3FEND mapping

**Citations**: ISO/IEC 21838-2:2021. *Information technology — Top-level ontologies (TLO) — Part 2: Basic Formal Ontology (BFO)*.
**Notes**: BFO is used as the top-level ontology by a large number of ontology projects in biomedicine, defense and intelligence, and industry: the official users list at basic-formal-ontology.org/users.html named 731 ontologies and about 100 institutions and groups when counted on 2026-11-23. The page states no total, and the earlier '650+' figure could not be traced to a primary, so quote the dated count. The "BFO 2020" name (ontology release) and "21838-2:2021" (standard publication date) are distinct — do not write "ISO/IEC 21838-2:2020". Part 1 of the 21838 family specifies the requirements for top-level ontologies; Part 2 is BFO specifically.
**Validation Status**: ✅ Verified 2026-06-21 (WebSearch + ISO catalogue: standard number 21838-2, Part 2 = BFO, published Nov 2021, standardizes BFO 2020). ISO landing page returns HTTP 403 to automated fetch; number/title/date corroborated via ISO catalogue listing, the BFO-2020 GitHub repo, and the bfo-discuss announcement. · Re-verified 2026-11-23: IEC webstore lists ISO/IEC 21838-2 Edition 1.0, published 2021-11-30, with no edition listed as under development; users-list count taken from basic-formal-ontology.org/users.html the same day.

---

#### Common Core Ontologies (CCO) — BFO-aligned mid-level ontology

**Authors**: CUBRC, Inc. (Buffalo, NY); created under IARPA funding; maintained by the CCO team (e.g., Ron Rudnicki) and a CCO Governance Board (incl. John Beverley)
**Date**: Created 2010; made openly available 2017; actively maintained (governance board formed 2024)
**URL**: https://github.com/CommonCoreOntology/CommonCoreOntologies
**Alt URL**: https://ncor-network.org/wiki/ontologies/common-core-ontologies · https://arxiv.org/pdf/2404.17758 (Jensen et al., *The Common Core Ontologies*)
**Evidence Level**: B (widely-adopted community/defense ontology suite with an arXiv descriptive paper; not itself an ISO/IEC standard — proposed as a candidate standard mid-level ontology, so A is not yet warranted)
**Relevance**:
- The mid-level link in the grounding chain D3FEND → CCO → BFO referenced in the book appendix
- BFO-aligned suite of exactly eleven ontologies (page verbatim "a widely-used suite of eleven ontologies"; latest release v2.2, 2026-08-14 (refreshed 2026-11-23; v2.1 was April 2026)); used across defense/intelligence for interoperability and automated reasoning
- The reusable middle layer the D3FEND-to-BFO grounding routes through rather than mapping D3FEND straight to a top-level ontology

**Citations**: Jensen, M., et al. *The Common Core Ontologies* (arXiv:2404.17758). CUBRC, Inc. CCO open-source distribution.
**Notes**: CCO is explicitly designed to extend BFO (the top-level ontology) — confirming the BFO-alignment the grounding chain depends on. Owner/maintainer is CUBRC (Buffalo-based R&D company), not the University at Buffalo philosophy department, though the two are closely connected (Barry Smith/NCOR). "Mid-level" is the correct register — CCO sits between BFO (top-level) and mission/domain ontologies. Tier B not A: CCO is *proposed* as a standard mid-level ontology but is not an adopted ISO/IEC standard the way BFO is. Refresh (2026-11-23): the CCO README states CCO is under evaluation as a mid-level ontology standard by IEEE SA under PAR P3195.1 (an active PAR approved 2022-09-21, not an approved standard), so the Tier B rating holds until that standard is approved. The Governance Board expects structural release 3.0 by 2026-12-31 and 4.0 by 2027-06-30 and recommends users wait for 4.0 before updating, so any class-level citation should name the CCO version.
**Validation Status**: ✅ Verified 2026-06-21 (WebSearch: CUBRC origin + IARPA funding + 2017 open release + BFO-extension/mid-level framing confirmed via NCOR, CUBRC, and the arXiv CCO paper). · Re-verified 2026-11-23 (GitHub releases: v2.2 2026-08-14; README on the develop branch: eleven ontologies, IEEE P3195.1; IEEE SA page: Active PAR).

---

### Technical Documentation

#### Zeek Network Security Monitor — Documentation

**Authors**: The Zeek Project
**Date**: 2024-2026 (continuously updated)
**URL**: https://docs.zeek.org/
**Evidence Level**: B (official open-source documentation)
**Relevance**:
- Network-log transformation and OCSF mapping; the open-source NSM whose logs anchor much of the book's parsing/mapping discussion
- ch04 §4.2 (OCSF) + Appendix H [was: Chapter 8] (OCSF mapping), Appendix F

**Citations**: The Zeek Project. *Zeek Documentation*. https://docs.zeek.org/
**Validation Status**: ✅ Active URL (verified 2026-06-05)

---

#### Microsoft Power Query M — Language Reference

**Authors**: Microsoft
**Date**: continuously updated
**URL**: https://learn.microsoft.com/en-us/powerquery-m/
**Evidence Level**: B (official vendor documentation)
**Relevance**:
- The transformation language behind the CISA Zeek-OCSF M-code mapping referenced in the manuscript
- Reference for the validated transformation-pattern library

**Citations**: Microsoft. *Power Query M Formula Language Reference*. https://learn.microsoft.com/en-us/powerquery-m/
**Validation Status**: ✅ Active URL (verified 2026-06-05)

---

### Emerging Projects

#### Apache DataFusion Ballista

**Authors**: Apache DataFusion project
**Date**: 2024-2026 (active development)
**URL**: https://datafusion.apache.org/ballista/
**Evidence Level**: B (Apache open-source project; limited production case studies)
**Relevance**:
- Rust + Arrow distributed query execution; emerging alternative to Spark/Trino
- ch05 §5.3 + Appendix I [was: Chapter 9] (query-engine comparison) as an emerging option; not yet production-proven for security data lakes (label accordingly)

**Citations**: Apache DataFusion Project. *Ballista Documentation*. https://datafusion.apache.org/ballista/
**Validation Status**: ✅ Active URL (verified 2026-06-05)

---

#### Lakekeeper — Apache Iceberg REST Catalog (Rust)

**Authors**: Lakekeeper project
**Date**: 2024-2026 (pre-1.0, active development)
**URL**: https://docs.lakekeeper.io/
**Evidence Level**: B (open-source project; limited production case studies)
**Relevance**:
- Stateless, single-binary Iceberg REST catalog; lightweight alternative to Polaris (Java) and Nessie (Git-like versioning)
- ch05 §5.1 (table format) [was: Chapter 6] (catalog selection); prototype/POC-appropriate, await 1.0 for production (label accordingly)

**Citations**: Lakekeeper Project. *Lakekeeper Documentation*. https://docs.lakekeeper.io/
**Validation Status**: ✅ Active URL (verified 2026-06-05)

---

### Practitioner Publications

*(Published works cited as literature; any relationship/communication status from the source entry is intentionally omitted.)*

#### Architecting an Apache Iceberg Lakehouse — Alex Merced

**Authors**: Alex Merced (Dremio)
**Date**: 2025 (MEAP v1)
**URL**: https://www.manning.com/books/architecting-an-apache-iceberg-lakehouse
**Evidence Level**: B (practitioner book; Manning MEAP)
**Relevance**:
- 5-layer lakehouse architecture (Storage → Ingestion → Catalog → Federation → Consumption); modular, vendor-neutral design
- Production cost-optimization patterns (Insider: 90% S3 cost reduction with Iceberg) *(Unverified 2026-11-17: the book text is not openly accessible, and Manning's product page does not carry the figure.)*
- Chapters 2, 6, 9 (Iceberg fundamentals, decision framework, cost)

**Citations**: Merced, A. (2025). *Architecting an Apache Iceberg Lakehouse* (MEAP v1). Manning.
**Validation Status**: ⏳ Carried from the June 2026 merge; existence re-checked 2026-11-17 (see `methods/verification-2026-11/ledger.json`) · ⚠️ 1 figure unverified 2026-11-17, see the dated label

---

#### The 9 Ways to Move Data Kafka -> Iceberg — Tom Scott (Streambased)

**Authors**: Tom Scott (Streambased)
**Date**: 2025-10-20 (actual publication date; catalogued "October 2024" corrected 2026-07-09, verified at primary)
**URL**: https://blog.streambased.io/p/the-9-ways-to-move-data-kafka-iceberg
**Evidence Level**: B (practitioner analysis)
**Relevance**:
- Streaming-lakehouse architecture; zero-copy vs copy-based trade-offs. The article's actual 9: Kafka Connect, Redpanda Iceberg Topics, Confluent TableFlow, WarpStream TableFlow, AutoMQ Table Topics, Bufstream, Aiven Iceberg Topics, StreamNative Ursa, Streambased (verified at the article 2026-07-10 — the entry's former list wrongly included Apache Fluss and omitted Kafka Connect and WarpStream)
- ch05 §5.1 (table format) [was: Chapter 9] (Kafka → Iceberg integration patterns)

**Citations**: Scott, T. (2025). *The 9 Ways to Move Data Kafka -> Iceberg*. Streambased blog.
**Validation Status**: ✅ Verified at the article 2026-07-10 (part-2 sweep fix 31): URL repointed from blog root to the article; title and solution list corrected

---

#### Okta's Multi-Engine Data Stack — Julien Hurault

**Authors**: Julien Hurault (Ju Data Engineering Newsletter)
**Date**: May 1, 2024
**URL**: https://juhache.substack.com/p/oktas-multi-engine-data-stack (repointed 2026-11-22 from the newsletter root)
**Evidence Level**: B (Tier-1 production validation, named deployment with metrics) — re-tiered from A 2026-08-19: not peer-reviewed research and not an official standard
**Relevance**:
- Okta serverless DuckDB: "1 million DuckDB invocations per day in average" and "peaks of up to 250GB of data processed per minute"; AWS Lambda + DuckDB + Snowflake + S3 (read at the post 2026-11-22)
- Upstream preprocessing to cut warehouse compute; ch02 §2.3 (economics) [was: Chapter 10] (cost), ch05 §5.3 + Appendix I [was: Chapter 9] (serverless patterns)

**Citations**: Hurault, J. (2024, May 1). *Okta's Multi-Engine Data Stack*. Ju Data Engineering Newsletter.
**Notes**: Refresh (2026-11-23): both figures re-read verbatim at the post. Hurault relays them from a Data Council 2024 talk by Jake Thomas of Okta, 'Processing Trillions of Records at Okta with Mini Serverless Databases' (2024-04-18). The post names the speaker only as 'Jake' and its link to the talk page now returns 404; the speaker and event are confirmed at https://duckdb.org/library/processing-trillions-of-records-at-okta-with-mini-serverless-databases/. That talk is the primary for the figures and is worth citing beside this post, though the recording was not watched.
**Validation Status**: ✅ Active URL (verified 2026-06-05); both figures, labelled unverified on 2026-11-17, were read at the post on 2026-11-22 · re-read 2026-11-23

---

#### SOC Modernization & AI — Anton Chuvakin

**Authors**: Anton Chuvakin (Google Cloud Security)
**Date**: 2024-2025
**URL**: https://cloud.withgoogle.com/cloudsecurity/podcast/
**Evidence Level**: B (industry thought-leadership, published)
**Relevance**:
- "Accelerated SIEM Journey: A SOC Leader's Playbook for Modernization and AI" (Cloud Security Podcast ep. 236); "How Google Does It: Building AI agents for cybersecurity"
- SOC evolution, SIEM modernization, AI-in-SOC readiness

**Citations**: Chuvakin, A. (2024-2025). *Accelerated SIEM Journey* and related, Google Cloud Security Podcast.
**Validation Status**: ⏳ Carried from the June 2026 merge; existence re-checked 2026-11-17 (see `methods/verification-2026-11/ledger.json`)

---

#### Building AI for Cyber Defenders + Claude-Assisted Intrusion Report — Anthropic

**Authors**: Anthropic
**Date**: 2025 (intrusion report published Nov 13, 2025 — the entry's former "November 2024" was wrong; corrected 2026-07-10)
**URL**: https://www.anthropic.com/research
**Alt URL**: https://www.anthropic.com/news/disrupting-AI-espionage (the GTG-1002 intrusion report)
**Evidence Level**: B (vendor research, named publications)
**Relevance**:
- "Building AI for Cyber Defenders"; the November 13, 2025 report on a state-sponsored actor using Claude for a largely-autonomous intrusion — page verbatim: "human intervention required only sporadically (perhaps 4-6 critical decision points per hacking campaign)"
- Validates "AI amplification, not replacement"; AI threat-intelligence reference

**Citations**: Anthropic (2025). *Building AI for Cyber Defenders*; *Disrupting AI-orchestrated cyber operations*. anthropic.com/news/disrupting-AI-espionage
**Validation Status**: ✅ Verified at primary 2026-07-10 (part-2 sweep fix 32): date corrected, report URL added

---

#### Business AI Is the Automation of Intelligence Tasks / ITEM Framework — Daniel Miessler

**Authors**: Daniel Miessler
**Date**: 2024-07-29 (the post was retitled and is dated 2024-07-29 at the live page, verified 2026-07-10; entry formerly said 2025)
**URL**: https://danielmiessler.com/blog/weve-been-thinking-about-ai-all-wrong
**Evidence Level**: C (practitioner blog; anti-hype perspective)
**Relevance**:
- ITEM Framework (Knowledge, Intelligence, Speed, Accuracy, Cost) for intelligence-task automation
- Realistic AI-adoption expectations for security operations; AI-maturity hypothesis input

**Citations**: Miessler, D. (2024). *Business AI Is the Automation of Intelligence Tasks* (formerly *We've Been Thinking About AI All Wrong*); ITEM Framework. danielmiessler.com.
**Validation Status**: ⏳ Carried from the June 2026 merge; existence re-checked 2026-11-17 (see `methods/verification-2026-11/ledger.json`)

---

#### How We Hijacked a Claude Skill with an Invisible Sentence — Josh Devon

**Authors**: Josh Devon (Secure Trajectories, publication now at Sondera)
**Date**: October 20, 2025 (the entry's former "October 2024" was implausible — it predates Claude Skills; corrected 2026-07-10)
**URL**: https://blog.sondera.ai/p/claude-skill-hijack-invisible-sentence
**Evidence Level**: B (independent security research, published)
**Relevance**:
- PDF-based prompt injection against AI agents (Claude Skills) via invisible/white-on-white text; maps to MITRE ATLAS AML.T0080 (context poisoning)
- AI-agent security vulnerabilities and defenses

**Citations**: Devon, J. (2025). *How We Hijacked a Claude Skill with an Invisible Sentence*. Secure Trajectories / Sondera.
**Validation Status**: ✅ Located at the moved publication 2026-07-10 (part-2 sweep fix 33): securetrajectories.substack.com 301s to blog.sondera.ai; article URL, live title, and date corrected

---

#### AI Engineering — Chip Huyen

**Authors**: Chip Huyen
**Date**: 2025
**URL**: https://github.com/chiphuyen/aie-book
**Evidence Level**: B (practitioner book)
**Relevance**:
- AI-engineering best practices applicable to security AI/ML systems
- Reference for AI/ML implementation guidance

**Citations**: Huyen, C. (2025). *AI Engineering*. O'Reilly.
**Validation Status**: ✅ Active URL (verified 2026-06-05)

---

#### Ryan Stillions — The DML (Detection Maturity Level) Model

**Authors**: Ryan Stillions
**Date**: 2014-04-21 (confirmed via the Blogger post feed, 2026-11-23)
**URL**: https://ryanstillions.blogspot.com/2014/04/the-dml-model_21.html
**Evidence Level**: C (practitioner blog-published conceptual model; widely cited in the detection-engineering community but not peer-reviewed or a standards document — cite as a framing model, not as an empirical result)
**Relevance**:
- Anchors the "detection maturity is about *abstraction level*, not coverage count" framing used in the D3FEND-coverage / detection-engineering line of argument — a control's value depends on *what altitude* of adversary behavior it observes (goals/strategy/TTPs vs. atomic indicators), not merely on how many techniques it nominally touches.
- Conceptual complement to MITRE ATT&CK (which enumerates techniques) and to the ATT&CK↔D3FEND coverage work: the DML levels give a vocabulary for *why* a high-abstraction detection (DML-5 Techniques, DML-6 Tactics, and the largely subjective DML-7 Strategy and DML-8 Goals) is more durable than a low-abstraction one (DML-1 Atomic IOCs, DML-2 Host & Network Artifacts).

**Key Findings**:
- A nine-level model, DML-0 to DML-8, with the lowest levels the most technically specific: DML-8 Goals, DML-7 Strategy, DML-6 Tactics, DML-5 Techniques, DML-4 Procedures, DML-3 Tools, DML-2 Host & Network Artifacts, DML-1 Atomic IOCs, DML-0 None or Unknown.
- Core claim: an organization's detection maturity is measured by the *highest abstraction level at which it can reliably detect adversary activity*, not by the raw number of indicators or signatures it maintains. Detecting at the Tactics/Techniques level survives an adversary changing tools or infrastructure; detecting only at the Atomic-Indicator level does not.
- Frequently paraphrased alongside David Bianco's "Pyramid of Pain" (the two are complementary: Pyramid of Pain frames adversary cost, DML frames defender abstraction level).

**Citations**: Detection-engineering / coverage-quality framing; supports the argument that D3FEND/ATT&CK coverage must be read by abstraction level, not technique count.
**Notes**: Tier C under the strict tiers in METHODOLOGY.md §3.1 — a single-author practitioner blog post, durable and community-canonical but not peer-reviewed. Cite Stillions by name + 2014 for the model; do not attribute specific empirical detection-rate numbers to it (it publishes none).

**Validation Status**: ✅ Verified at primary 2026-11-23 (full post text via the Blogger JSON feed: nine levels 0-8 as listed, published 2014-04-21). Corrected that day: an 'Identity' level the post does not contain was removed, and the Relevance level numbers were fixed.

---

#### SCYTHE — Purple Team Exercise Framework (PTEF)

**Authors**: SCYTHE. Per the PTEFv4 Contributors section: v1 names no author and credits reviewers and contributors including Jorge Orchilles and Bryson Bort; v2 authored by Christopher Peacock, Jorge Orchilles, Tim Schulz and Shawn Edwards; v3 authored by Jorge Orchilles; v4 contributors Trey Bilbrey, Tyler Casey and Jarrad Pemberton
**Date**: 2020 (v1); current PTEFv4, dated January 2026 in the document and merged to the repository 2026-04-09
**URL**: https://github.com/scythe-io/purple-team-exercise-framework
**Evidence Level**: C (vendor-published operational practice framework — SCYTHE is an adversary-emulation vendor, so flag the author-incentive; the *methodology* is community-adopted and credible, but it is not peer-reviewed or a neutral standard)
**Relevance**:
- Anchors the "purple-teaming = the operational loop that measures detection by adversary emulation" claim used in the detection-validation / D3FEND-coverage line: detection quality is established by *emulating* known adversary TTPs (ATT&CK-mapped) and observing whether the blue team detects them, then iterating — not by counting deployed controls.
- Complements the DML/abstraction-level framing (Stillions 2014) and the ATT&CK↔D3FEND coverage work: purple-teaming is how an org *empirically* tests whether claimed coverage actually fires, closing the gap between nominal control inventory and measured detection.

**Key Findings**:
- Defines a repeatable cycle: select adversary TTPs (typically ATT&CK techniques) → red executes the emulation → blue observes telemetry and detection → measure detect/alert/respond → tune detections → repeat. The loop is the unit of measurement, with red and blue working *together* (the "purple" collaboration) rather than adversarially.
- Frames detection effectiveness as something *measured by emulation*, against known TTPs, rather than assumed from control coverage — the operational counterpart to ATT&CK Evaluations' threat-informed purple-teaming (see the MITRE Engenuity ATT&CK Evaluations entry, which uses the same purple-team methodology at vendor-evaluation scale).

**Citations**: Detection-validation / measured-coverage framing; supports the claim that coverage must be tested by adversary emulation, not asserted.
**Notes**: Tier C — credible, named, community-adopted operational framework, but vendor-published (SCYTHE) so flag the incentive when citing. The named-practitioner anchor (Orchilles, Bort, Peacock) keeps this above Tier-D speculation; Orchilles is also a SANS author on purple teaming / adversary emulation, which corroborates the practitioner authority. Do not attach empirical detection-rate statistics to this source. Refresh (2026-11-23): cite PTEFv4 (PTEFv4.md in the repository) for current wording. v4 adopts ATT&CK v18 Detection Strategies and Analytics terminology, classifies each missed detection into one of five gap types (visibility, detection logic, alert suppression, process, timeliness), adds metrics such as Detection Coverage Growth, and covers AI/ML targets with reference to MITRE ATLAS and the OWASP Top 10 for LLM Applications. Bryson Bort appears only as a v1 reviewer and contributor, so the practitioner anchor is better stated as Orchilles and Peacock. The repository README calls PTEF 'the industry standard for Purple Team Exercises'; treat that as vendor self-description.

**Validation Status**: ✅ Verified at primary 2026-11-23 (GitHub repo, README and PTEFv4.md read; MIT license; v1 to v3 archived under Archive/; contributor list per version).

---

### Books

#### Kingpin: How One Hacker Took Over the Billion-Dollar Cybercrime Underground

**Authors**: Kevin Poulsen
**Date**: 2011
**URL**: https://openlibrary.org/books/OL24438892M (catalog record; print ISBN 978-0307588685, Crown, 2011)
**Alt URL**: https://www.penguinrandomhouse.com/books/197890/kingpin-by-kevin-poulsen/ (publisher title page)
**Evidence Level**: B (non-fiction, investigative)
**Relevance**:
- Attack-surface economics; attackers optimize for ROI, not capability (Max Butler abandoned exploitable bank-network access for faster carding monetization)
- Threat-actor behavior and monetization patterns

**Citations**: Poulsen, K. (2011). *Kingpin*. Crown.
**Validation Status**: ✅ Open Library record found 2026-11-17 (Crown, first edition, ISBN 978-0307588685). The record's publish_date is 2010 and its LCCN is 2010027952, which probably reflects the cataloging-in-publication year, and its LC call numbers carry both 2010 and 2011. Refresh (2026-11-23): the Penguin Random House title page lists the Crown ebook (ISBN 978-0307588708) as published Feb 22, 2011 and the paperback (ISBN 978-0307588692) as Feb 7, 2012, which supports a 2011 first release; that page does not list the hardcover ISBN 978-0307588685, so the hardcover date itself is inferred. The Open Library HTML page now sits behind a bot-check interstitial, so the record was read through its .json endpoint. The Butler ROI anecdote was not re-checked against the book text in this pass.

---

## 2026 Format & Standards Developments (added June 2026)

Primary sources for the developments that postdate the book's March-2026 snapshot. Each URL was
fetched and confirmed live, and each claim checked against the primary page (2026-06-05).

#### Apache Iceberg v3 — Table Format Specification

**Authors**: Apache Iceberg project (Apache Software Foundation)
**Date**: v3 complete and adopted (spec current on the 1.11.0 release line)
**URL**: https://iceberg.apache.org/spec/
**Alt URL**: https://raw.githubusercontent.com/apache/iceberg/main/format/spec.md
**Evidence Level**: A (official standard)
**Relevance**:
- The V3 shift the book is mostly pre-: binary deletion vectors, the Variant type, row-lineage tracking, default-value support, nanosecond timestamps, geometry/geography types
- ch05 §5.1 (table format) [was: Chapter 9] (format war), ch05 §5.1 (table format) [was: Chapter 2] (table-format fundamentals); closes the H-SEC-CATALOG row-lineage audit-trail gap

**Key Findings**: spec states "Versions 1, 2 and 3 ... are complete and adopted." V3 additions include deletion vectors, Variant, row lineage, default values, multi-argument transforms, table encryption keys. (V3 stabilizes in the 1.11.0 release — see the dedicated Iceberg 1.11.0 entry below.)
**Citations**: Apache Iceberg. *Table Format Specification* (v3). https://iceberg.apache.org/spec/
**Validation Status**: ✅ Active (verified 2026-06-05; cite the raw spec.md as the fetchable primary)

---

#### Apache Iceberg v4 — Spec Effort (Milestone #58)

**Authors**: Apache Iceberg project (GitHub)
**Date**: Open / proposal-stage as of 2026-06-05
**URL**: https://github.com/apache/iceberg/milestone/58
**Evidence Level**: B (official project tracker) — re-tiered from A 2026-08-19: neither peer-reviewed research nor an official standard
**Relevance**:
- The V4 format effort the book tracks as a milestone; proposal-stage, NOT adopted
- ch05 §5.1 (table format) [was: Chapter 9]; user's top format-war tracking priority

**Key Findings**: Milestone Open, 2 tracked proposals — #13153 Column Stats Improvements, #13141 Relative Path Support. The wider V4 wishlist (single-file commits, Parquet-not-Avro metadata) circulates in secondary blogs only — do not cite as settled.
**Citations**: Apache Iceberg. *V4 Spec — Milestone #58*. https://github.com/apache/iceberg/milestone/58
**Validation Status**: ✅ Active (verified 2026-06-05)
**Currency (2026-11-17)**: the Iceberg spec page still says "Version 4 is under active development and has not been formally adopted" (https://iceberg.apache.org/spec/), so v3 remains the newest adopted format version; the newest library release is 1.12.0 (2026-09-30).

---

#### DuckLake v1.0: The Lakehouse Format Built on SQL

**Authors**: The DuckDB team
**Date**: April 13, 2026
**URL**: https://duckdb.org/2026/04/13/ducklake-10
**Alt URL**: https://ducklake.select/2026/04/13/ducklake-10/
**Evidence Level**: B (project/vendor authoritative)
**Relevance**:
- The DuckLake-vs-Iceberg comparison the book and Lab track; v1.0 is production-ready (stable spec, shipped with DuckDB v1.5.2)
- ch05 §5.1 (table format) [was: Chapter 9], ch05 §5.1 (table format) [was: Chapter 12]; the SQL-as-catalog-metadata alternative to Iceberg's file-based metadata

**Key Findings**: all table metadata in a SQL catalog (SQLite/PostgreSQL/DuckDB); v1.0 adds data inlining (small DML in the catalog, no new files), sorted tables, murmur3 bucket partitioning (Iceberg-compatible), GEOMETRY + Variant, and experimental Iceberg-v3-compatible deletion vectors via Puffin.

**First-party catalog failure-mode observations (BENCH-E, 2026-06-14)** — [SDW Lab `ducklake-catalog-failuremodes/FINDINGS-2026-06-14.md`](https://github.com/flying-coyote/sdw-lab-benchmarks/blob/master/ducklake-catalog-failuremodes/FINDINGS-2026-06-14.md) (Tier B), pinned to **DuckDB 1.5.3 + DuckLake spec e6a3bd0a**. The SQL catalog buys the flat ~3ms planning the design promises (measured first-party in R6 `ocsf-format-planning`, where the DuckLake catalog planning column of [RESULTS.md](https://github.com/flying-coyote/sdw-lab-benchmarks/blob/master/ocsf-format-planning/results/RESULTS.md) reads 2.94, 3.57 and 3.56 ms at 10, 50 and 200 commits — the ~3ms is R6's number, not BENCH-E's) and pays for it in catalog-layer surface, so the trade is real on both sides rather than free:
- **#1215 cross-store delete-conflict PERSISTS** — 29 rows survive a delete that should leave 0 (silent row resurrection). This is the worst class of failure for GDPR erasure, retention expiry, and tombstoned false-positives, where a "deleted" record reappearing is a correctness and compliance problem, not a performance one.
- **#1184 >1600-column Postgres CREATE wall PERSISTS** — wide tables fail to create against a PostgreSQL catalog (identical with data-inlining off); security schemas go wide (flattened OCSF, EDR), so this is the constraint that bites the security workloads first.
- **#1031 catalog-pool timeout FIXED 1.5.2→1.5.3** — 60s→0.036s, the version-currency story (the same shape as the chDB bloom-undercount fix on the ClickHouse-vs-DuckDB bench): a real bug that the next release closed, which is why each verdict is version-bound rather than a durable indictment.
- Version-bound and peer-level by design: #1215/#1184 are OPEN as of this stack and may close the way #1031 did, so re-check on the next DuckLake release before treating either as a standing verdict. The **105×/923×/189× streaming numbers are deliberately NOT reproduced here** (unequal-workload vendor benchmark — see the DuckLake data-inlining entry below for why the relayed "105×/926×" pairs two different baselines).

**Citations**: DuckDB team (2026, Apr 13). *DuckLake v1.0*. https://duckdb.org/2026/04/13/ducklake-10. First-party failure-mode findings: `sdw-lab-benchmarks/ducklake-catalog-failuremodes/FINDINGS-2026-06-14.md` (ab4e4d6).
**Validation Status**: ✅ Active (verified 2026-06-05); first-party BENCH-E observations added 2026-06-14 (version-bound to DuckDB 1.5.3 + DuckLake e6a3bd0a; #1215/#1184 OPEN, re-check next release)
**Currency (2026-11-17)**: DuckLake 1.0 is still the current release per https://ducklake.select/; the first-party observations above are pinned to DuckDB 1.5.3, while DuckDB itself is now at v2.0.0 (released 2026-10-21), so they need a re-run before being quoted against a current DuckDB.

---

#### Introducing Variant — Open Standard for Semi-Structured Data

**Authors**: Databricks — Gene Pang, David Cashman, Ryan Blue, Aniruth Narayanan
**Date**: October 10, 2025
**URL**: https://www.databricks.com/blog/introducing-variant-new-open-standard-semi-structured-data-apache-parquettm-delta-lake
**Evidence Level**: B (vendor authoritative; co-authored by Iceberg co-creator Ryan Blue)
**Relevance**:
- The open Variant type now in Parquet (2.12.0 / Parquet-Java 1.16.0), Iceberg v3, Delta, Spark — the semi-structured path for CloudTrail/JSON security logs (the MFA absence-as-NULL flattening problem)
- ch04 §4.2 (OCSF) + Appendix H [was: Chapter 8] (OCSF/flattening), Appendix B

**Key Findings**: Variant "ratified in the Apache Parquet community" with Delta/Iceberg/Spark support. Shredding (columnarizing common fields) improves read 8× vs regular Variant / 30× vs string; writes 20-50% slower — *vendor's own benchmark, treat the multiples as Tier C*.
**Citations**: Pang, G., Cashman, D., Blue, R., Narayanan, A. (2025, Oct 10). *Introducing Variant*. Databricks.
**Validation Status**: ✅ Active (verified 2026-06-05)

---

#### OCSF Schema v1.8.0

**Authors**: Open Cybersecurity Schema Framework (Linux Foundation)
**Date**: March 18, 2026 (v1.8.0 release tag — confirmed; cadence: v1.6.0 2025-08-01, v1.7.0 2025-11-14, v1.8.0 2026-03-18)
**URL**: https://github.com/ocsf/ocsf-schema/releases
**Alt URL**: https://schema.ocsf.io/
**Evidence Level**: A (official schema standard)
**Relevance**:
- Current OCSF schema version (the book's OCSF analysis predates it); the six-schemas crosswalk corpus targets 1.8.0
- ch04 §4.2 (OCSF) + Appendix H [was: Chapter 8], Appendix F

**Key Findings**: v1.8.0 is the latest release (cadence: v1.5.0 Apr 2025, v1.6.0 Aug 2025, v1.7.0 Nov 2025, v1.8.0 Mar 2026). 1.8.0 adds an `ai_operation` profile (`ai_model`/`message_context`), privilege-analysis objects with MITRE ATT&CK mapping, and a macOS process extension.
**Citations**: OCSF (2026). *OCSF Schema v1.8.0*. https://github.com/ocsf/ocsf-schema/releases
**Validation Status**: ✅ Active (verified 2026-06-05; day-of-month unconfirmed)
**Currency (2026-11-17)**: superseded as the current release by OCSF v1.9.0 (https://github.com/ocsf/ocsf-schema/releases, published 2026-08-03; v1.10.0-dev listed at https://schema.ocsf.io/). Findings above describe v1.8.0 and stay version-bound to it.
**Refresh (2026-11-23)**: OCSF v1.10.0 was released on 2026-11-20 (tag `1.10`, https://github.com/ocsf/ocsf-schema/releases/tag/1.10), so it is now the current release and the "v1.10.0-dev" above is out of date. Its changelog adds a `dns_zone_transfer_activity` event class, an optional `ai_capability` attribute and object for the `ai_operation` profile that v1.8.0 introduced, an `ai_status` object, a `physical_site` profile and a `firewall_rule_evaluation` object.

---

#### Using the NANDA Index Architecture in Practice: An Enterprise Perspective

**Authors**: Sichao Wang, Ramesh Raskar (MIT Media Lab), Mahesh Lambe, Pradyumna Chari, Rekha Singhal, Shailja Gupta, Rajesh Ranjan, Ken Huang
**Date**: August 5, 2025
**URL**: https://arxiv.org/abs/2508.03101
**Evidence Level**: B (preprint, not peer-reviewed; MIT-affiliated)
**Relevance**:
- The actual NANDA primary source: agent discovery, authentication, capability attestation (AgentFacts — spelling per the paper), cross-protocol interoperability (MCP/A2A/NLWeb) for an "Internet of Agents"
- no current chapter home [AMBIGUOUS] [was: Chapter 12] (agent-native architecture) — as infrastructure, not a SOC-automation benchmark

**⚠️ VERIFICATION (2026-06-05)**: the "≈98.7% SOC automation" figure attached to NANDA across the book (ch12) and the website essay ("The 98.7% Solution") is **NOT in this paper** and no primary source for it could be found — NANDA is agent-internet infrastructure, not a SOC system, and the abstract reports no percentage metrics. Cite this paper for the architecture only; the 98.7% figure has no primary and must not be cited to it.
**Citations**: Wang, S., Raskar, R., et al. (2025, Aug 5). *Using the NANDA Index Architecture in Practice: An Enterprise Perspective*. arXiv:2508.03101.
**Validation Status**: ✅ Active (verified 2026-06-05); ⚠️ the 98.7% claim is unsupported

---

#### Splunk Platform 10.4 + Cisco Data Fabric — Federated Search

**Authors**: Splunk (Cisco) — Aqib Kazi, Michelle Corpora
**Date**: May 18, 2026
**URL**: https://www.splunk.com/en_us/blog/platform/splunk-cloud-platform-10-4-and-splunk-enterprise-10-4.html
**Evidence Level**: B (vendor product announcement)
**Relevance**:
- The current Splunk picture (the book's Splunk analysis is on the 2024 product): Federated Search GA, "core pillar of the Cisco Data Fabric," SPL2, BYO catalogs
- ch06 §6.5 (keep the SIEM) [was: Chapter 6] (when Splunk wins / federation)

**Key Findings**: Splunk Cloud Platform 10.4 + Enterprise 10.4 ship Federated Search — "a core pillar of the Cisco Data Fabric powered by the Splunk Platform" (page verbatim) — with SPL2 and BYO-catalog support; bundles Splunk AI Assistant 2.0. (The former "Federated Search for Snowflake GA July 2026" clause was removed 2026-07-10 — Snowflake is unmentioned on the cited post; re-source separately if a Snowflake-specific citation is wanted.)
**Citations**: Kazi, A., Corpora, M. (2026, May 18). *Splunk Cloud Platform 10.4 and Enterprise 10.4: Federated Search*. Splunk.
**Validation Status**: ✅ Active (verified 2026-06-05)

---

#### Amazon S3 Tables — Native Apache Iceberg in Object Storage

**Authors**: Amazon Web Services
**Date**: December 3, 2024 (GA; REST Catalog APIs March 2025; auto-replication December 2025)
**URL**: https://aws.amazon.com/about-aws/whats-new/2024/12/amazon-s3-tables-apache-iceberg-tables-analytics-workloads/
**Evidence Level**: B (vendor GA announcement)
**Relevance**:
- The strongest single "Iceberg is the standard" anchor — a hyperscaler building Iceberg natively into object storage; ch05 §5.1 (table format) [was: Chapter 1], ch05 §5.1 (table format) [was: Chapter 9]
- Iceberg adoption / vendor-convergence evidence

**Key Findings**: "first cloud object store with built-in Apache Iceberg support"; AWS claims up to 3× query throughput / 10× transactions vs self-managed Iceberg (*vendor benchmark, Tier C*); Iceberg REST Catalog APIs added March 2025.
**Citations**: AWS (2024, Dec 3). *Amazon S3 Tables — fully managed Apache Iceberg tables*. aws.amazon.com.
**Validation Status**: ✅ Active (verified 2026-06-05)

---

#### Apache Iceberg 1.11.0 — Release

**Authors**: Alex Stephen & Talat Uyarer (Google, Lakehouse team — bylines verified at the post 2026-07-10)
**Date**: May 27, 2026 (post date verified at primary; entry formerly said May 19)
**URL**: https://opensource.googleblog.com/2026/05/announcing-apache-iceberg-1110.html
**Alt URL**: https://iceberg.apache.org/releases/ (official releases index; 1.11.0 is latest)
**Evidence Level**: B (official ASF release) — re-tiered from A 2026-08-19: neither peer-reviewed research nor an official standard
**Relevance**:
- The latest Iceberg release. Pairs with the Iceberg-v3-spec entry above; ch05 §5.1 (table format) [was: Chapter 9] (format war); user's top format-war tracking priority.

**Key Findings**: What the cited Google post actually covers (verified 2026-07-10): support for Apache Spark 4.1 and Apache Flink 2.1; "the REST catalog learns to plan scans server-side, shifting metadata work off the query engine"; built-in table encryption (envelope encryption, KMS integration); a new File Format API; and an SQL UDF specification. Separately sourced context, NOT from this post: predecessor 1.10.0 (2025-09-11) was the first release to "close" the V3 table spec, and Snowflake reached Iceberg-v3 GA 2026-05-07 (catalog-side adoption).
**Citations**: Stephen, A., Uyarer, T. (2026, May 27). *Announcing Apache Iceberg 1.11.0*. Google Open Source Blog / iceberg.apache.org/releases.
**Validation Status**: ✅ Verified at the post 2026-07-10 (part-2 sweep fix 35): the entry's former "V3 stabilization / features now require format-version-3" framing appears nowhere in the cited post and was replaced with the post's actual contents; date and bylines corrected
**Currency (2026-11-17)**: superseded by Apache Iceberg 1.12.0 (https://github.com/apache/iceberg/releases, published 2026-09-30); Apache Flink's latest stable release is 2.3.0 (https://flink.apache.org/downloads/), newer than the Flink 2.1 support described above.

---

#### OCSF Achieves ITU Support — Toward an International Standard

**Authors**: Rod Wallace (Director of Security Services, AWS); reporting an ITU / OCSF (Linux Foundation) development
**Date**: March 24, 2026 (article); ITU member-state support December 2025; ratification slated by June 2026
**URL**: https://aws.amazon.com/blogs/opensource/ocsf-achieves-itu-support-powering-ai-ready-security-operations/
**Evidence Level**: B (official standards-body milestone — ITU is the UN's telecommunication standards body; report is from the AWS Open Source team, an OCSF founding contributor) — re-tiered from A 2026-08-19: neither peer-reviewed research nor an official standard
**Relevance**:
- The standards-tier step-change for OCSF: in December 2025 ITU member states unanimously supported OCSF for ratification as an ITU X-series ("x.***") international standard, slated for June 2026. This moves OCSF from an industry-consortium schema (its Linux Foundation status, already catalogued) toward a formally ratified international standard that governments fold into national cyber policy.
- ch04 §4.2 (OCSF) + Appendix H [was: Chapter 8] (OCSF / schema standards); strengthens the "OCSF as lingua franca" thread the book and the crosswalk corpus track (cite alongside the bearish-on-lingua-franca caveat — ITU ratification is governance momentum, not field-level adoption).

**Key Findings**: ITU member states unanimously supported OCSF for ratification as an international standard (Dec 2025); ratification as an ITU x.*** standard slated by June 2026; the article frames standardization as "a global necessity" governments will incorporate into national cybersecurity policy. The supporting standardization claim is corroborated by DevOps.com's republication ("Future Proofing the Foundation for AI-Ready Security Operations"). Cross-source date note (2026-07-10): this post states v1.8.0 "released March 16th, 2026" — two days off the authoritative GitHub release timestamp (2026-03-18, per github.com/ocsf/ocsf-schema/releases); keep the bibliography's v1.8.0 entry date (March 18) and treat this post's date as the outlier.
**Citations**: Wallace, R. (2026, Mar 24). *OCSF Achieves ITU Support: Powering AI-Ready Security Operations*. AWS Open Source Blog.
**Validation Status**: ✅ Active (verified 2026-06-05 via WebFetch of the AWS post — date, author, Dec-2025 ITU member-state support, and June-2026 ratification timeline all confirmed on the page)

---

#### MITRE D3FEND for OT — Operational Technology Extension (v1.3.0)

**Authors**: MITRE (D3FEND project; funded by NSA and the Office of the Under Secretary of War for Acquisition & Sustainment — the Alt URL's verbatim funder title post-rename, verified 2026-07-10; formerly "OUSD")
**Date**: December 16, 2025 (OT extension; shipped in the D3FEND v1.3.0 release line, December 2025)
**URL**: https://www.mitre.org/news-insights/news-release/mitre-extends-d3fend-ontology-operational-technology-cybersecurity
**Alt URL**: https://d3fend.mitre.org/domain/ot/
**Evidence Level**: A (official MITRE release; formal OWL 2 DL ontology extension)
**Relevance**:
- Extends the D3FEND defensive ontology (already catalogued for the OCSF↔D3FEND grounding work) to cyber-physical / industrial-control-system defense — relevant to the OT-estate anecdotes and the isolation-first / OT thread. The OT domain is a distinct, separately-citable artifact from the base ATT&CK-mapped enterprise ontology.
- ch04 §4.1 (D3FEND) [was: Chapter 8]/grounding work; complements the existing "MITRE D3FEND Framework & Ontology" entry, which now reflects the v1.0 (2025-01-16) → v1.3.0 (Dec 2025) line.

**Key Findings**: MITRE extended D3FEND to OT on 2025-12-16, building a structured knowledge base for defending cyber-physical systems, with additional ICS artifacts and implementation guidance expected through 2026. The "267 defensive techniques across seven tactical categories", "v1.3.0", and OWL-2-DL details are secondary-coverage figures (Industrial Cyber et al.), NOT on the cited MITRE news release or the d3fend.mitre.org/domain/ot Alt URL — cite them to the secondary coverage explicitly or not at all (labeled 2026-07-10). Version update: the live d3fend.mitre.org badge read **v1.4.0** on 2026-07-10, superseding the v1.3.0 line this entry tracks.
**Citations**: MITRE (2025, Dec 16). *MITRE Extends D3FEND Ontology to Operational Technology Cybersecurity*. mitre.org news release.
**Validation Status**: ✅ Alt URL verified 2026-07-10 (funder title confirmed verbatim; mitre.org news release 403s automated fetch — technique-count figures labeled secondary pending a rendered check)
**Currency (2026-11-17)**: D3FEND's current release is 1.6.0 (d3fend.mitre.org version badge, release date 2026-08-31); the OT extension described here arrived in v1.3.0.

---

#### Cohasset Associates — Amazon S3 Object Lock Compliance Assessment (SEC 17a-4(f) / 18a-6(e), FINRA 4511(c), CFTC 1.31(c))

**Authors**: Cohasset Associates, Inc. (independent records-management and compliance assessor); commissioned by AWS
**Date**: 2025 assessment
**URL**: https://d1.awsstatic.com/onedam/marketing-channels/website/aws/en_US/whitepapers/compliance/Amazon-S3-Compliance-Assessment-2025.pdf
**Alt URL**: https://aws.amazon.com/compliance/secrule17a-4f/
**Evidence Level**: B (independent third-party compliance attestation against named SEC/FINRA/CFTC rules) — re-tiered from A 2026-08-19: not peer-reviewed research and not an official standard
**Relevance**:
- The strongest compliance anchor for the lakehouse-on-object-storage thesis in regulated financial services: an independent assessor's WORM attestation that object storage can satisfy the same broker-dealer record-retention rules historically used to justify a proprietary archival SIEM/archive tier. Supports the FSI/compliance and retention hypotheses (immutability without vendor lock-in).
- Chapter on compliance/retention; pairs with the Amazon S3 Tables and Iceberg-on-S3 entries.

**Key Findings**: Cohasset's opinion is that Amazon S3 with Object Lock — Compliance mode for the strict case, Governance mode for less-restrictive needs — meets the non-rewriteable, non-erasable (WORM) record-retention requirements of SEC 17a-4(f), SEC 18a-6(e), FINRA 4511(c), and CFTC 1.31(c) for time-based retention periods and legal holds. In Compliance mode a locked object version cannot be overwritten or deleted by any user including the root account, and the retention period cannot be shortened. The report is downloadable for presentation to regulators when notifying them of the decision to store regulated records on S3.
**Citations**: Cohasset Associates (2025). *Amazon S3 — SEC 17a-4(f), SEC 18a-6(e), FINRA 4511(c), and CFTC 1.31(c) Compliance Assessment*. AWS.
**Validation Status**: ✅ Active (verified 2026-06-13 via WebSearch — AWS compliance page + the 2025 assessment PDF confirm Cohasset's WORM attestation for S3 Object Lock under the named rules; exact assessment-report day within 2025 not pinned)

---

#### pySigma-pipeline-ocsf — Sigma → OCSF Detection-as-Code Pipeline

**Authors**: SigmaHQ (maintainer: Hendrik Baecker)
**Date**: pre-release (as of 2026-06-13)
**URL**: https://github.com/SigmaHQ/pySigma-pipeline-ocsf
**Evidence Level**: B (official SigmaHQ open-source project; pre-release)
**Relevance**:
- Detection-as-code portability across OCSF: converts Sigma rules to OCSF field/event-type names so a single detection corpus can target OCSF-normalized telemetry. Supports the Sigma-portability and OCSF-crosswalk threads, and the "contribute to pySigma-pipeline-ocsf rather than own a competing repo" engagement move.
- Chapter on detection portability / OCSF; complements the OCSF v1.8.0 and crosswalk entries.

**Key Findings**: provides the `sigma.pipeline.ocsf` package with an `ocsf_pipeline()` that returns a pySigma `ProcessingPipeline`; the README lists **25** Sigma logsource-category → OCSF event-type mappings as of 2026-07-10 (grown from 23 at the 2026-06-13 check — counts move; restate with an as-of date whenever cited). MIT license; badge marks it pre-release. The 2026-06-13 correction's other half still holds: the README does **not** mention a "Detection Finding" output class — cite the logsource→OCSF mapping only, and confirm the targeted OCSF version at the repo before citing one (the README pins none).
**Citations**: SigmaHQ; Baecker, H. *pySigma-pipeline-ocsf*. GitHub.
**Validation Status**: ✅ Active (verified 2026-06-13 via WebFetch of the GitHub README — project, maintainer, MIT license, pre-release status, and 23 logsource mappings confirmed; Gemini's 25-categories / Detection-Finding-class claim corrected)

---

#### Declined (no primary) — EITT Academy "90-second triage / 340% ROI / 8 FTE saved"

The 2026-06-13 Gemini-DR lit-review intake surfaced an EITT Academy vendor-guide relay citing a "90-second triage, 340% ROI, 8 FTE saved" outcome. **Not added.** The precise-but-unsourced trio is a vendor-guide relay with no locatable primary (no named customer, methodology, or independent measurement), and it fits the fabricated-precise pattern the 2026-06-05 audit was built to catch. Recorded here as a deliberate refusal so it is not re-proposed; admit only if a named primary with methodology appears.

---

#### Cribl "Finality" Customer Case Study — In-Stream Windows-Event Reduction

**Authors**: Cribl (vendor case study); customer Finality, Inc. (CEO Eric Jeanmaire quoted)
**Date**: April 22, 2024
**URL**: https://cribl.io/resources/cs/finality/
**Alt URL**: https://docs.cribl.io/stream/usecase-win-xml/
**Evidence Level**: C (vendor-published, single-customer self-reported)
**Relevance**:
- Pipeline pre-ingest volume reduction (RQ13 detection economics / pipeline-vs-query) — dropping repetitive Windows-event fields in Cribl Stream before the SIEM. Concrete practitioner data point for the "filter at the pipeline" thesis.
- ch02 §2.2 (components: collection and pipeline) [was: Chapter 6] (stream processing) / ch04 §4.3-4.5 (Sigma, coverage) + Appendix M [was: Chapter 13] (detection engineering).

**Key Findings**: Finality — an IT and security consulting firm helping US Federal agencies meet log-management/M-21-31 obligations — is a Cribl Stream customer. CEO Eric Jeanmaire, verbatim: "Being able to get a 47% reduction on average in our Windows Events by dropping repetitive fields is huge." Also documented: "10x faster" data extractions / Splunk CIM compliance, and a 250% month-over-month increase in SIEM detection-content (new-rule) delivery; CPU-intensive work (CMDB, threat enrichment) shifted off SIEM indexers onto Cribl Stream. No dollar-savings figure published. Cribl's own docs give a broader 34–70% range for Windows XML event reduction generally. **Correction to the Gemini-DR intake**: "Finality" is a Cribl *customer* (a consulting firm), not a Cribl product/feature; the 47% is a single-customer self-report qualified "on average … by dropping repetitive fields," not an independent benchmark.
**Citations**: Cribl (2024, Apr 22). *Finality customer case study*. cribl.io.
**Validation Status**: ✅ Active (verified 2026-06-13 via WebFetch — 47% CEO quote, 10× and 250% figures, and the customer-not-product correction confirmed) Refresh (2026-11-23): old /customers/ path now redirects to /resources/cs/finality/; 47%, 10x, 250% and the 34-70% docs range re-read verbatim; the page title and section headings frame the 250% as faster threat detection or faster content delivery while the body gives it as a month-over-month increase in new detection rules, and the entry follows the body.

---

#### Fortinet + NVIDIA — FortiGate-VM on the BlueField-3 DPU (Isolated Infrastructure)

**Authors**: Fortinet, Inc. and NVIDIA (joint press release)
**Date**: December 16, 2025
**URL**: https://www.fortinet.com/corporate/about-us/newsroom/press-releases/2025/fortinet-delivers-isolated-infrastructure-acceleration-for-the-ai-factory-with-nvidia
**Alt URL**: https://www.globenewswire.com/news-release/2025/12/16/3206276/0/en/Fortinet-Delivers-Isolated-Infrastructure-Acceleration-for-the-AI-Factory-with-NVIDIA.html
**Evidence Level**: B (vendor-official joint announcement; no independent benchmark)
**Relevance**:
- Isolation-first security architecture at the hardware layer (RQ7–RQ10): FortiGate-VM runs directly on the DPU, isolating the security plane from compute workloads. Relevant to the OT/AI-factory and multi-tenant isolation thread.
- Chapter on isolation patterns; complements the isolation-first tracking work.

**Key Findings**: FortiGate-VM "running on BlueField executes on the DPU, bypassing the host CPU." Verbatim isolation language: BlueField "offloads networking and security functions in an isolated trust domain, purpose-built for isolating the security plane from compute workloads"; "Security is implemented at the hardware level, yet software defined"; the integration improves "multitenant isolation, throughput, and inspection accuracy for AI workloads." Requires FortiOS 7.6.3+ with OVS bridges. **No quantified throughput/latency** appears in the release. **Correction to the intake**: "hardware-level multi-tenant isolation" is a synthesis of adjacent vendor phrases, not a single coined term; this is a vendor marketing announcement (Tier B by provenance), not an independent test.
**Citations**: Fortinet & NVIDIA (2025, Dec 16). *Fortinet Delivers Isolated Infrastructure Acceleration for the AI Factory with NVIDIA*.
**Validation Status**: ✅ Active (verified 2026-06-13 via WebFetch — product, date, and isolation language confirmed at the Fortinet primary; no perf figures to cite)

---

#### Databricks — Cross-Engine ABAC via the Iceberg REST Catalog Scan APIs (Beta)

**Authors**: Alex Jiang, Alex Reid, Michelle Leon (Databricks)
**Date**: June 2, 2026
**URL**: https://www.databricks.com/blog/introducing-cross-engine-abac
**Alt URL**: https://docs.databricks.com/aws/en/data-governance/unity-catalog/filters-and-masks/
**Evidence Level**: C (vendor blog; includes a vendor self-claim)
**Relevance**:
- Catalog-as-control-plane governance (RQ10 catalog governance; the catalog leg of the open-lakehouse security story): row filters and column masks enforced at the catalog layer, before data reaches the engine, across engines via an open API.
- Chapter on catalog/governance; pairs with the Polaris and Iceberg-REST entries.

**Key Findings**: Beta (announced 2026-06-02, **not GA**). "Cross-engine ABAC is built on the Iceberg REST Catalog scan APIs … to delegate policy enforcement to the catalog"; "Enforcement happens at the catalog layer, before data reaches the engine." Mechanism is **server-side scan planning** — Unity Catalog evaluates entitlements during scan planning and returns "a filtered scan plan scoped to the data the user is authorized to access" (row filters, column masks, tag-based rules, SQL UDFs). **Correction to the intake**: this is distinct from credential vending (standard Iceberg REST credential vending does *not* support row-filter/column-mask tables); the relay conflated the two. Engine support at Beta: Apache Spark today; Starburst and DuckDB "coming soon." "First and only catalog to deliver cross-engine ABAC" is a vendor self-claim (flag bias). No metrics.
**Citations**: Jiang, A., Reid, A., Leon, M. (2026, Jun 2). *Introducing Cross-Engine ABAC*. Databricks.
**Validation Status**: ✅ Active (verified 2026-06-13 via WebFetch — Iceberg-REST-scan mechanism, Beta status, and the scan-planning-vs-credential-vending distinction confirmed)

---

#### Apache Polaris — Top-Level Project Graduation + Credential Vending

**Authors**: Apache Polaris project (Apache Software Foundation)
**Date**: Graduated to ASF Top-Level Project, February 2026 (official Polaris blog Feb 19, 2026; IPMC graduation-recommendation vote passed Feb 16, 2026; Dremio press-release dateline Feb 18, 2026)
**URL**: https://polaris.apache.org/blog/2026/02/19/apache-polaris-graduates-to-top-level-project/
**Alt URL**: https://polaris.apache.org/releases/1.0.0/
**Evidence Level**: B for the graduation fact (ASF-official); B for the credential-vending feature docs — re-tiered from A 2026-08-19: neither peer-reviewed research nor an official standard
**Relevance**:
- Zero-trust catalog / credential vending (RQ10 catalog governance): the vendor-neutral Iceberg REST catalog is now an ASF Top-Level Project, and vends temporary, scoped storage credentials so engines need no standing cloud-storage access.
- Chapter on catalogs; complements the Snowflake-Polaris and Databricks-ABAC entries.

**Key Findings**: Official Polaris blog (Feb 19, 2026): "Apache Polaris has officially graduated from the Apache Incubator to become a Top Level Project." The ASF incubator IPMC RESULT vote recommending graduation passed Feb 16, 2026 (10 binding +1); Polaris had incubated since Aug 2024. Polaris 1.0.0 docs: "Polaris vends temporary storage credentials to the query engine during query execution," using scoped tokens, so engines run queries without direct cloud-storage access. **Correction to the intake**: the precise "Feb 18" date is from the Dremio vendor press release (Tier C), not an ASF-official page (the official blog byline is Feb 19); "zero-trust catalog" is the relay's label, not the docs' term ("credential vending").
**Citations**: Apache Polaris (2026, Feb 19). *Apache Polaris Graduates to Top-Level Project*; Apache Polaris 1.0.0 docs (Security and access control).
**Validation Status**: ✅ Active (verified 2026-06-13 via WebFetch — graduation at the ASF-official blog + IPMC vote, and credential vending in the 1.0.0 docs)
**Currency (2026-11-17)**: Apache Polaris has released up to 1.9.0 (https://github.com/apache/polaris/releases, published 2026-11-14), so the Polaris 1.0 statements above are version-bound history.

---

#### KPMG — AI Quarterly Pulse Survey, Q3 2025

**Authors**: KPMG US (KPMG LLP)
**Date**: September 18, 2025
**URL**: https://kpmg.com/us/en/media/news/q3-ai-pulse.html
**Alt URL**: https://kpmg.com/kpmg-us/content/dam/kpmg/pdf/2025/ai-quarterly-pulse-survey-q3-2025.pdf
**Evidence Level**: C (vendor/marketing survey; small executive panel; flag bias)
**Relevance**:
- Agentic-AI adoption pace and ROI expectation (RQ14 agent ROI / RQ12 governance) — executive sentiment, a demand-signal data point rather than field measurement. Distinct from the existing KPMG/Fortinet/Prophet RQ14 entry.
- no current chapter home [AMBIGUOUS] [was: Chapter 17] (future predictions) / no current chapter home [AMBIGUOUS] [was: Chapter 13].

**Key Findings**: n = 130 U.S. C-suite/business leaders at $1B+ revenue organizations. Verbatim: "42% of organizations now having deployed at least some agents, up from 11% two quarters ago," and "the majority (57%) expect measurable ROI within 12 months." **Correction to the intake**: the relay's "42% run AI agents in production" overstates KPMG's wording — "deployed at least some agents" is weaker than production-grade running. Small self-selected executive panel; KPMG professional-services marketing survey (vendor-incented toward agentic momentum), Tier C.
**Citations**: KPMG US (2025, Sep 18). *AI Quarterly Pulse Survey: Q3 2025*.
**Validation Status**: ✅ Active (verified 2026-06-13 via WebFetch — 42% "deployed at least some agents" / 57% ROI-<12mo confirmed verbatim; "in production" overstatement corrected)

---

#### The FastLanes File Format

**Authors**: Azim Afroozeh and Peter A. Boncz (Centrum Wiskunde & Informatica / CWI Amsterdam)
**Date**: 2025 (VLDB 2025, London)
**URL**: https://www.vldb.org/pvldb/vol18/p4629-afroozeh.pdf
**Alt URL**: https://ir.cwi.nl/pub/35881 — DOI https://dl.acm.org/doi/10.14778/3749646.3749718
**Evidence Level**: A (peer-reviewed, PVLDB)
**Relevance**:
- The columnar-format-war thread (ch05 §5.1 (table format) [was: Chapter 9]): a fully data-parallel (SIMD/GPU) lightweight-encoding format that, like Vortex and CMU F3, the Iceberg File Format API (1.11.0) opens the ecosystem to. The CWI/academic anchor for "the next Parquet" discussion.
- Pairs with the Apache Iceberg v3/1.11.0, DuckLake, and Variant entries.

**Key Findings**: PVLDB 18(11):4629–4643 (2025), DOI 10.14778/3749646.3749718. Avoids generic compression (e.g. Snappy) in favor of fully data-parallel lightweight encodings; cascades them via a flexible expression-encoding mechanism enabling multi-column compression (MCC); supports partial decompression. Evaluation on a real-world corpus: on average **~43× faster decode/scan** than Parquet+Snappy (44× vs +ZSTD, 7× vs BtrBlocks, 29× vs DuckDB) and **~315× faster first-value (random-access) retrieval** than Parquet+Snappy, while improving compression ratio over Parquet. **Corrections to the intake**: "GPU-saturation encodings" overstates the abstract ("designed for SIMD or GPU"); and the often-quoted ">100 billion integers/sec scalar decode" headline belongs to the *separate* 2023 paper "The FastLanes Compression Layout" (PVLDB 16(9):2132–2144, DOI 10.14778/3598581.3598587), not this File Format paper.
**Citations**: Afroozeh, A. & Boncz, P. (2025). *The FastLanes File Format*. PVLDB 18(11):4629–4643. **Complementary** (added 2026-06-13): Afroozeh, A. (2026). *FastLanes: A Next-Gen File Format* (PhD thesis, Vrije Universiteit Amsterdam), **DOI 10.5463/thesis.1348** — the consolidated thesis behind the FastLanes line of work (DOI verified to resolve at the VU research portal, 2026-06-13). The encoding it defines is leveraged by Vortex and CMU F3 rather than shipping as a standalone format (the "integrated, not standalone" reading holds for the *encoding*; the 2026 thesis separately frames a "FastLanes File Format"). The often-quoted ">100 billion ints/sec" SIMD headline traces to the earlier 2023 *FastLanes Compression Layout* paper (PVLDB 16(9), DOI 10.14778/3598581.3598587) — keep the attribution above; a web-search "confirmation" that the figure sits in the 2025 File Format paper is not authoritative on which paper owns it.
**Validation Status**: ✅ Active (verified 2026-06-13 — title/authors/venue/DOI confirmed at CWI + PVLDB; the 43×/315× multipliers are evaluation-body figures corroborated via search indexing of the primary PDF, which blocked direct text extraction)

---

#### DuckLake — Data Inlining for Streaming

**Authors**: Pedro Holanda (DuckLake / DuckDB Labs)
**Date**: April 2, 2026
**URL**: https://ducklake.select/2026/04/02/data-inlining-in-ducklake/
**Alt URL**: https://duckdb.org/2026/04/02/data-inlining-in-ducklake
**Evidence Level**: C (project's own benchmark; not independent)
**Relevance**:
- The small-files / streaming-into-the-lakehouse problem (RQ13; ch05 §5.1 (table format) [was: Chapter 9]): inlining stages small DML directly in the SQL catalog (e.g. PostgreSQL) instead of writing many small Parquet files, the streaming weakness the book tracks for Iceberg. Extends the existing DuckLake v1.0 entry with the specific inlining benchmark.
- Pairs with the DuckLake v1.0 and Iceberg entries.

**Key Findings**: Benchmark is a **single DuckDB process** inserting 100 rows/second (10 batches × 10 rows) into a 23-column table — **not a 100-stream simulation**. Two distinct baselines: (1) DuckLake-with-inlining vs **Apache Iceberg + Polaris** (100-second run via pyiceberg) = **105× insert / 923× aggregation / 189× checkpoint** (the Iceberg run generated 1,000+ small Parquet files vs zero inlined); (2) DuckLake with- vs without-inlining (50-minute run) = **5.2× insert / 925.9× (≈926×) aggregation / 14.5× checkpoint**. **Correction to the intake**: the relayed "105× / 926×" pairs figures from *two different baselines* and mislabels the workload as "100-stream"; the consistent vs-Iceberg pair is 105× / 923×, and the inlining mechanism alone yields only ~5.2× on insert (most of the 105× is DuckLake vs Iceberg+Polaris overhead).
**Cross-reference (2026-06-14)**: the inlining mechanism this entry describes is the same catalog-layer machinery the BENCH-E failure-mode bench exercises — see the DuckLake v1.0 entry above for the first-party catalog-correctness observations on DuckDB 1.5.3 (#1215 delete-resurrection PERSISTS, #1184 wide-schema CREATE wall PERSISTS, #1031 pool-timeout FIXED). The streaming multipliers here (105×/923× vs Iceberg+Polaris) are the vendor's own benchmark and are deliberately not reproduced as first-party in the SDW lab; what the lab measures is the catalog-correctness surface, not the streaming throughput.
**Citations**: Holanda, P. (2026, Apr 2). *Data Inlining in DuckLake: Unlocking Streaming for Data Lakes*. DuckLake / DuckDB Labs.
**Validation Status**: ✅ Active (verified 2026-06-13 via WebFetch — both baselines, the single-process workload, and the cross-baseline pairing error confirmed)
**Currency (2026-11-17)**: DuckDB v2.0.0 was released 2026-10-21 (https://github.com/duckdb/duckdb/releases); any DuckDB 1.5.x-pinned figure above is version-bound.

---

#### Apache Ossie (incubating) — Open Semantic Interchange Enters the ASF Incubator

**Authors**: Apache Ossie project (Apache Software Foundation Incubator); Open Semantic Interchange coalition (Snowflake-convened, Salesforce and dbt Labs co-founders)
**Date**: ASF incubation June 2026 (proposal thread June 19–22); OSI initiative announced 2025-09-23; spec v0.1.1 released 2025-12-11; ontology layer added 2026-05-29 (0.2.0.dev0 draft)
**URL**: https://incubator.apache.org/clutch/ossie.html
**Alt URL**: https://github.com/apache/ossie
**Evidence Level**: B (official ASF incubation record + the project's own spec repository) — re-tiered from A 2026-08-19: neither peer-reviewed research nor an official standard
**Relevance**:
- The candidate interchange standard for the semantic data layer — governed metric definitions bound to tables — which the MOAR architecture names as deliberately open (book Ch2 §2.2 forward pointer, 2026-07-23; MATRIX.md standards catalog row)
- Security-greenfield finding (2026-07-23): zero security presence across the project's issues, discussions, dev list, and 60+ member coalition, and no open machine-readable security metrics layer exists in any semantic-layer format
- Pairs with the OCSF Schema v1.8.0 and pySigma-pipeline-ocsf entries: the schema and detection-portability standards this layer would sit above

**Key Findings**: Vendor-neutral YAML/JSON spec for semantic models: datasets bound to physical tables, foreign-key relationships, model-level metrics in multi-dialect SQL (dialect enum ANSI_SQL / Snowflake / MDX / Tableau / Databricks / MAQL / BigQuery — no ClickHouse, DuckDB, or Trino), and `ai_context` fields for agent grounding. Draft 0.2.0.dev0 on main with an explicit schema-may-change banner; the only git tag is osi-0.1.1-rc1 and there are zero ASF-blessed releases as of 2026-07-23. Reference converters (dbt/MetricFlow, GoodData, Salesforce, Polaris) are CLI proof-of-concept grade per every source that graded them. The ontology layer (2026-05-29) is ORM-style conceptual modeling with dataset mappings, not OWL. First vertical working group (financial services, FIBO-aligned) held its first formal meeting July 2026; security absent.
**Citations**: Apache Software Foundation. *Ossie (incubating)*. https://incubator.apache.org/clutch/ossie.html; Apache Ossie. *Core Metadata Specification* (0.2.0.dev0). https://github.com/apache/ossie
**Notes**: Coalition-size claims (17 → 50+/60+ organizations) trace to Snowflake's own blog — vendor-reported, Tier C within an otherwise Tier-A entry. Named critiques on record: MetricFlow-as-reference-implementation neutrality (Mullins), Microsoft MDX/DAX absence (Jayatillake), convener-asymmetry (Coginiti). Practitioner posture: align metric definitions to the format, no runtime dependency before a 1.0.
**Validation Status**: ✅ Active (verified 2026-07-23 — spec files, JSON Schema, and validator fetched and run first-party; incubation record and roadmap read at primary)

---

## Peer-Reviewed Primaries — Gemini DR-3 intake (2026-07-10, all verified at primary locally)

Six Tier-A additions from the DR-3 hunt (external Gemini Deep Research run; every entry below was fetched and quote-verified locally before cataloguing — three of the run's other candidates were rejected for misattribution or unreachability, see `working/intake/GEMINI-DR3-INTAKE-2026-07-10.md`).

#### Yang et al. - True Attacks, Attack Attempts, or Benign Triggers? An Empirical Measurement of Network Alerts in a Security Operations Center

**Authors**: Limin Yang, Zhi Chen, Chenkai Wang, Zhenning Zhang, Sushruth Booma, Phuong Cao, Constantin Adam, Alexander Withers, Zbigniew Kalbarczyk, Ravishankar K. Iyer, Gang Wang (UIUC / NCSA / IBM Research)
**Date**: 2024 (USENIX Security '24)
**URL**: https://www.usenix.org/conference/usenixsecurity24/presentation/yang-limin
**PDF**: https://www.usenix.org/system/files/usenixsecurity24-yang-limin.pdf
**Evidence Level**: A (USENIX Security, top-tier peer-reviewed; production SOC data)
**Relevance**:
- The empirical-SOC base-rate grounding the corpus lacked: alert volumes, true-attack rates, and alert composition measured in a production SOC rather than surveyed
- Feeds alert-fatigue and detection-pipeline-economics claims; the strongest single source for "most alerts are not attacks" with a measured denominator

**Key Findings**:
- "SOC analysts are facing excessive alerts (24K–134K per day), but only a small percentage of the alerts (0.01%) are associated with true attacks" (verbatim)
- "a significant portion of the alerts are related to 'attack attempts' (attacks that did not lead to true compromises, 27%), and 'benign triggers' (correctly matched security events but had business-justified explanations, 49%)" (verbatim)
- 4 of 11 investigated true compromises went undetected by network-level alerts — network telemetry alone misses initial endpoint compromise and stealthy lateral movement

**Validation Status**: ✅ Verified at primary 2026-07-10 (abstract page + PDF; full author list from citation metadata) Refresh (2026-11-23): both URLs live; 24K–134K/day, 0.01%, 27% and 49%, and 4 of 11 re-read verbatim in the USENIX PDF. The body states the attack-attempt share as "at least 27%" (27.37%, about 3.9 million alerts, per Section 6.2), and the data comes from a single SOC at NCSA.

---

#### LogLite: Lightweight Plug-and-Play Streaming Log Compression

**Authors**: Benzhao Tang, Shiyu Yang, Zhitao Shen, Wenjie Zhang, Xuemin Lin, Zhihong Tian (Guangzhou University / Ant Group / UNSW / Shanghai Jiao Tong)
**Date**: September 2025, PVLDB 18(11):3757-3770
**URL**: https://www.vldb.org/pvldb/vol18/p3757-yang.pdf
**Alt URL**: https://arxiv.org/abs/2507.10337
**Evidence Level**: A (PVLDB, peer-reviewed)
**Relevance**:
- Streaming log compression without pre-trained templates (XOR + byte-aligned RLE in a sliding window) — the edge-compression leg of the columnar-vs-row / log-storage cost story

**Key Findings**:
- "compared to state-of-the-art baselines, LogLite achieves Pareto optimality in most scenarios, delivering an average improvement of up to 67.8% in compression ratio and up to 2.7× in compression speed" (verbatim)

**Validation Status**: ✅ Verified at primary 2026-07-10 (vldb.org PDF + arXiv)

---

#### PBC: High-Ratio Compression for Machine-Generated Data

**Authors**: Jiujing Zhang, Zhitao Shen, Shiyu Yang, Lingkai Meng, Chuan Xiao, Wei Jia, Yue Li, Qinhui Sun, Wenjie Zhang, Xuemin Lin (Ant Group / Guangzhou University / UNSW)
**Date**: December 2023 (PACMMOD 1(4), DOI 10.1145/3626732; the issue presented at ACM SIGMOD 2024)
**URL**: https://arxiv.org/pdf/2311.13947
**Code**: https://github.com/antgroup/pbc
**DOI**: https://doi.org/10.1145/3626732
**Evidence Level**: A (SIGMOD/PACMMOD, top-tier peer-reviewed)
**Relevance**:
- Pattern-based per-record log compression enabling random point-lookups without full block decompression — machine-generated-log structure exploited beyond generic Zstd/Snappy

**Key Findings**:
- "PBC, on average, achieves a compression ratio twice as high as the state-of-the-art techniques while maintaining competitive compression and decompression speeds" (verbatim)

**Validation Status**: ✅ Verified at primary 2026-07-10 (arXiv PDF; venue + author list confirmed) Refresh (2026-11-23): arXiv and code links live; "twice as high" re-read verbatim; DOI and PACMMOD issue (vol. 1, no. 4, published 2023-12-08) resolved at Crossref. The published title is "High-Ratio Compression for Machine-Generated Data" without the "PBC:" prefix, and the SIGMOD 2024 pairing follows the PACMMOD issue convention and was not read at a primary in this pass.

---

#### Pebbles: Leveraging Sketches for Processing Voluminous, High Velocity Data Streams

**Authors**: Thilina Buddhika, Sangmi Lee Pallickara, Shrideep Pallickara (Colorado State University)
**Date**: August 2021, IEEE Transactions on Parallel and Distributed Systems 32(8):2005-2020, DOI 10.1109/TPDS.2021.3055265 (year resolved at the dblp structured record, 2026-07-10)
**URL**: https://par.nsf.gov/servlets/purl/10284573
**Evidence Level**: A (IEEE TPDS, peer-reviewed; the DR run's "Sketch-Aware Streaming Telemetry, NSF 2023" title/label was wrong — corrected at intake)
**Relevance**:
- Sketch-based telemetry-stream reduction — quantified upstream volume reduction for detection pipelines (pre-ingest filtering effectiveness family)

**Key Findings**:
- "up to a ~8× reduction in data volumes transferred and a ~27× improvement in throughput" (verbatim, abstract)

**Validation Status**: ✅ Verified at primary 2026-07-10 (PDF fetched; title/authors corrected from the DR run's invented label)

---

#### Blitzcrank: Fast Semantic Compression for In-Memory Online Transaction Processing

**Authors**: Yiming Qiao, Yihan Gao, Huanchen Zhang (Tsinghua University)
**Date**: 2024, PVLDB 17(10):2528-2540
**URL**: https://www.vldb.org/pvldb/vol17/p2528-zhang.pdf
**Alt URL**: https://www.vldb.org/pvldb/volumes/17/paper/Blitzcrank%3A%20Fast%20Semantic%20Compression%20for%20In-Memory%20Online%20Transaction%20Processing (landing page, script-rendered)
**DOI**: https://doi.org/10.14778/3675034.3675044
**Evidence Level**: A (PVLDB, peer-reviewed)
**Relevance**:
- The row-oriented/OLTP counterpoint in the columnar-vs-row storage story: semantic compression with random-tuple access — what row stores can do that block-compressed columnar can't
- ⚠ Intake note: the DR run attributed this paper's quote to a DIFFERENT paper (DeepSqueeze, ResearchGate 341750834) — re-attributed at intake after fetching both

**Key Findings**:
- "BLITZCRANK achieves a sub-microsecond latency for decompressing a random tuple while obtaining high compression factors. This leads to an 85% memory reduction in the TPC-C evaluation with a moderate (19%) throughput degradation" (verbatim)

**Validation Status**: ✅ Verified at primary 2026-07-10 (correct paper located and fetched; misattribution documented in the intake doc) Refresh (2026-11-23): quote re-read verbatim in the PVLDB PDF; the volume-page URL returns only the site shell to a plain fetch (the abstract is script-rendered), so the PDF is the primary link.

---

#### Delta Lake: High-Performance ACID Table Storage over Cloud Object Stores

**Authors**: Michael Armbrust, Tathagata Das, Liwen Sun, Burak Yavuz, Shixiong Zhu, Mukul Murthy, Joseph Torres, Herman van Hovell, Adrian Ionescu, Alicja Łuszczak, Michał Świtakowski, et al. (21 authors, Databricks / CWI / UC Berkeley / Stanford)
**Date**: 2020, PVLDB 13(12):3411-3424
**URL**: https://www.vldb.org/pvldb/vol13/p3411-armbrust.pdf
**DOI**: https://doi.org/10.14778/3415478.3415560
**Evidence Level**: A (PVLDB, peer-reviewed; industry-authored)
**Relevance**:
- The foundational peer-reviewed description of the transaction-log-over-object-store design (log compacted into Parquet checkpoints, ACID + time travel) that the book's table-format chapters describe — a citable primary underneath vendor documentation

**Key Findings**:
- The transaction log is compacted into Apache Parquet checkpoint files, providing ACID properties, time travel, and faster metadata operations for large tabular datasets on cloud object stores (paraphrase; the abstract's own words are "uses a transaction log that is compacted into Apache Parquet format to provide ACID properties, time travel, and significantly faster metadata operations for large tabular datasets"; the paper is the definitional source rather than a benchmark)

**Validation Status**: ✅ Verified at primary 2026-07-10 (PDF fetched, title + full author list confirmed) Refresh (2026-11-23): PDF live, abstract re-read; affiliations corrected and DOI added; a foundational design paper that still describes the log-over-object-store design accurately, while current protocol features live in the delta-io PROTOCOL.md, not this paper.

---

### Vendor case studies — Gemini DR-1 intake (2026-07-10, verified at primary locally)

Two C-tier catches from the DR-1 streaming-economics hunt (the run's other candidates were rejected: two predatory-adjacent journals, an anonymous Medium blog, an unreachable ResearchGate venue — see `working/intake/GEMINI-DR1-INTAKE-2026-07-10.md`).

#### Panther - How Cockroach Labs Ingests 5x More Logs and Cut SecOps Costs Over $200K

**Authors**: Panther Labs (vendor case study; named customer sources quoted: Munir Jaber, Security Engineer, and Adam Brennick, Director of Security, Risk, and Compliance, Cockroach Labs)
**Date**: 2026 (fetched 2026-07-10)
**URL**: https://panther.com/case-studies/how-cockroach-labs-ingests-5x-more-logs-and-cut-secops-costs-over-200k-with-panther
**Evidence Level**: C (vendor-authored case study quoting the customer — C per the 2026-07-10 vendor-channel tier rule; the 5×/$200K figures are Panther's own framing, the 365-day-retention quote is Brennick's directly)
**Relevance**:
- Migration-outcome family (legacy SIEM → security data lake): direction contradicts the streaming-costs-more premise for the SIEM-replacement case specifically
- H-IMPL-01/H-IMPL-02 context: a modern-lake counter-datapoint, not a streaming-vs-batch measurement

**Key Findings**:
- "Gained visibility into 5x more log data while maintaining budget and eliminating $200K+ in tooling overhead" (page verbatim); hot retention expanded from 90/30-day limits to 365 days queryable

**Validation Status**: ✅ Verified at primary 2026-07-10

---

#### layline.io - The Hidden Costs of Switching from Batch to Streaming

**Authors**: Andrew Tan (on layline.io, a streaming-platform vendor's blog)
**Date**: 2026-04-27
**URL**: https://layline.io/resources/blog/2026-04-27-the-hidden-costs-of-switching-from-batch-to-streaming
**Evidence Level**: C (vendor-channel authorship; treat the figures as directional practitioner observation, not measured data — no methodology disclosed)
**Relevance**:
- H-IMPL-02 (staffing scarcity) directional support: salary bands, hiring timelines, retraining and dual-running costs for the batch→streaming transition — the only 2026 source found that puts numbers on the transition costs, at C tier

**Key Findings**:
- "A senior stream processing engineer in London or New York costs between $160,000 and $220,000 base salary right now, plus the four-month average time-to-hire for that specialty" (verbatim)
- Retraining "typically three to six months"; "Budget for six months of dual operation minimum" (verbatim); an 8-month e-commerce dual-run example and a 5-week stored-procedure migration anecdote

**Validation Status**: ✅ Verified at primary 2026-07-10 (raw HTML fetch; all five checked figures verbatim)

---

## Systematic Search Arm — PRISMA Database Search (2026-07-13)

Everything above this line reached the corpus by curation: footnote extraction, expert interviews, vendor and standards material, and ongoing practitioner reading. That is the "identification via other methods" arm of a PRISMA 2020 flow, and it is a legitimate arm, but on its own it cannot answer the question a reviewer will ask — what does the indexed literature contain, and did this review find it?

The retro-run search (OpenAlex + dblp, 2018 onward, protocol in `methods/PRISMA-SEARCH-PROTOCOL-2026-07-13.md`) answered that question, and the answer was uncomfortable: of 40 studies the search included, **not one was already in this corpus**. Measured recall of the curated corpus against a systematic search of its own subject was zero. The entries below are the repair.

They are not, however, simply 40 new citations. Every included study went through a critical-appraisal stage the topical screening had skipped — venue identity resolved at the DOI, publisher and indexing established from primaries (DOAJ, Scopus, Web of Science), predatory-list and delisting checks run, then an independent LLM verification pass (a second LLM agent, separately prompted to refute each proposed citation; see the manuscript's §2.9). **Fourteen of the 40 did not survive it.** Eight were in predatory or compromised venues — including one paper in a *hijacked* journal whose DOI prefix is documented in Abalkina's 2024 work on journal hijacking, and one in a Hindawi title Clarivate delisted in its March-2023 cull after Wiley admitted paper-mill compromise. Three were not peer-reviewed at all, among them an arXiv preprint typeset with a counterfeit IEEE Access masthead and a placeholder DOI line. One could not be read at any price and was dropped rather than cited unread.

That leaves the 26 below. The appraisal record for all 40, including every drop and its reason, is `methods/prisma-appraisal-2026-07-13.json`.

Two cautions travel with these entries. First, the arm's 27 records resolve to only **24 independent author groups** — and the two papers that were supposed to put peer-reviewed footing under the corpus's weakest, vendor-sourced claims (ClickHouse storage reduction; pipeline log-reduction economics) turn out to share a single author, one of them publishing in a journal that is not listed in DOAJ (a 2017 removal is reported but not confirmed at DOAJ). They corroborate each other, not the claim. Second, several entries carry figures that are real but not usable as evidence here — speedups measured against unrelated hardware baselines, a percentage that is malformed as written, numbers a paper quotes from someone else. Each such entry says in the open what is carried and what is left behind.

### Streaming Architectures & Engine Comparisons (search arm)

#### Stream-Based IP Flow Analysis (IFIP/IEEE IM 2021, Dissertation Digest)

**Authors**: Milan Čermák, Pavel Čeleda (Masaryk University, CSIRT-MU)
**Date**: 2021 (17th IFIP/IEEE International Symposium on Integrated Network Management (IM 2021), Dissertation Digest track, Bordeaux (virtual), May 2021, pp. 736-741; IFIP ISBN 978-3-903176-32-4; no DOI — IEEE Xplore 9464011, dblp conf/im/CermakC21)
**URL**: https://dl.ifip.org/db/conf/im/im2021diss/212545.pdf (open full text)
**Evidence Level**: B (flagship IFIP/IEEE symposium series, Xplore- and dblp-indexed, no integrity flags — but this is the five-paper PhD Dissertation Digest track summarizing the author's 2020 thesis, whose primary benchmark was published at NOMS 2016, so it carries architecture-level findings and the deployment's existence rather than current performance numbers)
**Relevance**:
- Hypothesis H-STREAM-01 — an early peer-reviewed statement of the stream-plus-retention pattern: the authors conclude stream-based flow analysis cannot fully replace batch analysis because retrospective queries are impossible on streams, and recommend pairing the streaming pipeline with a primary data-retention store

**Key Findings**:
- A cybersecurity-derived benchmark (Identity/Filter/Count/Aggregation/Top-N/SYN-DoS operations, Kafka-fed CAIDA-derived flows, 7-node cluster) found Apache Samza, Storm, and Spark each processed ≥500k IP flows/second on 4 nodes/16 vCPUs against the authors' 300k flows/s requirement, with Samza fastest but constrained by its partition-per-core requirement — 2016-era measurements of framework versions since superseded, cite as historical suitability, not current guidance
- The resulting Stream4Flow stack (IPFIXcol → Kafka → Spark → Elastic Stack, open-sourced) ran experimentally on the Masaryk University campus network: 24,000 active IPs, 12,000 flows/s average
- PatternFinder attributed the attacking tool for roughly a third of detected SSH dictionary attacks (31% pattern match: Ncrack-1 26%, Ncrack-2 4%, Hydra 1%, Medusa 0.4%)

**Provenance**: PRISMA database-arm search, 2026-07-13 (originally excluded E2 at title/abstract screening; the 2026-07-16 independent second screen flagged the exclusion as a misread, and the owner-ruled adjudication admitted it through the same critical-appraisal + adversarial-verification gate as the original 40 — see `methods/second-screen-adjudication-2026-07-16.json`). All cited numbers verified at the IFIP DL full text, including a page-render check of the Fig. 3 percentages. Refresh (2026-11-23): IFIP PDF live; 500k/300k flows/s, Samza caveat, 24,000 IPs / 12,000 flows/s and the cannot-fully-replace-batch conclusion re-read verbatim; the Fig. 3 PatternFinder percentages were not re-extracted in this pass.

#### Intrusion Detection Streaming Transactions Using Apache Kafka and Spark Streaming (IEEE ICAIT, 2019)

**Authors**: May Thet Tun, Dim En Nyaung, Myat Pwint Phyu
**Full title**: Performance Evaluation of Intrusion Detection Streaming Transactions Using Apache Kafka and Spark Streaming
**Date**: 2019 (2019 International Conference on Advanced Information Technologies (ICAIT) — 3rd edition, Univ. of Information Technology, Yangon, Myanmar, 6-7 Nov 2019), pp. 25-30
**URL**: https://doi.org/10.1109/aitc.2019.8920960
**Evidence Level**: B (Legitimate IEEE-published conference proceedings from a real, ongoing university-run series with no predatory or integrity flags found — so this is not a DROP-on-venue case)
**Relevance**:
- Hypothesis H-STREAM-01 — recorded as an instance of first-party Kafka/Spark pipeline measurement on UNSW-NB15

**Key Findings**:
- Carried for the existence of the measurement only. No number may be quoted from it: the readable abstract contains no figures, and its one directional statement (that Kafka partitions *increase* processing time) contradicts the paper's own stated aim, which the full text — IEEE-paywalled and unread — would have to resolve. A metadata trap worth recording: Semantic Scholar mis-assigns this paper to the unrelated IEEE International Conference on Advanced Infocomm Technology; the venue here is the Yangon ICAIT series, per Crossref.

**Provenance**: PRISMA database-arm search, 2026-07-13 (search record 0 of 40). Appraised for venue integrity and content, then independently verified by a second LLM agent's verification pass; number check: no numbers to check. Refresh (2026-11-23): DOI resolves to IEEE Xplore 8920960; full title and pages from Crossref; abstract re-read at OpenAlex, still no figures.

#### CATRACA — Stream-Processing Threat Detection as a Virtual Network Function (Concurrency and Computation, 2019)

**Authors**: Martin Andreoni Lopez, Diogo M. F. Mattos, Otto Carlos M. B. Duarte, Guy Pujolle
**Full title**: Toward a monitoring and threat detection system based on stream processing as a virtual network function for big data (vol. 31, no. 20, e5344)
**Date**: 2019 (Concurrency and Computation: Practice and Experience)
**URL**: https://doi.org/10.1002/cpe.5344
**Evidence Level**: A (Established, currently Scopus/WoS-SCIE-indexed Wiley journal with no integrity flags found; a prototype deployed on OPNFV and evaluated on three datasets, with concrete accuracy figures in the abstract)
**Relevance**:
- Hypothesis H-STREAM-01 (stateful stream processing at scale) — a peer-reviewed instance of detection embedded in the streaming pipeline rather than bolted on after it
- Book ch02 §2.2 (components: collection and pipeline) [was: Chapter 7] (Ingestion — streaming)

**Key Findings**:
- over 95% accuracy distinguishing normal traffic from DoS attacks and vulnerability probes, across three different datasets
- more than 85% accuracy handling streaming data under concept-drift detection
- A working prototype deployed on OPNFV and evaluated against three datasets, with concept-drift handling — the pattern the rest of the corpus sources from vendor material.

**Provenance**: PRISMA database-arm search, 2026-07-13 (search record 1 of 40). Appraised for venue integrity and content, then independently verified by a second LLM agent's verification pass; number check: numbers confirmed in source. Refresh (2026-11-23): 95% and 85% re-read verbatim in the Crossref abstract; the abstract calls the system a prototype and says "we propose", so the deployed-system wording was narrowed to match, which also applies the method-basis correction recorded in methods/prisma-appraisal-2026-07-13.json. The figures are bare accuracy at abstract level; the full text was not read.

#### Virtual Network Function for Real-Time Threat Detection Using Stream Processing (MobiSecServ, 2018)

**Authors**: Martin Andreoni Lopez, Antonio Gonzalez Pastana Lobato, Otto Carlos M. B. Duarte, Guy Pujolle
**Full title**: An evaluation of a virtual network function for real-time threat detection using stream processing
**Date**: 2018 (2018 Fourth International Conference on Mobile and Secure Services (MobiSecServ), Miami Beach, FL, 24-25 Feb 2018), pp. 1-5
**URL**: https://doi.org/10.1109/mobisecserv.2018.8311440
**Evidence Level**: B (Legitimate, multi-year IEEE conference with no predatory or integrity flags — and I actively disconfirmed the one apparent red flag in the record set (the OpenAlex 'preprint' type tag), so this is not an unreviewed preprint)
**Relevance**:
- Hypothesis H-STREAM-01 (streaming throughput at scale)
- Book ch02 §2.2 (components: collection and pipeline) [was: Chapter 7] (Ingestion — streaming)

**Key Findings**:
- more than five million messages per second (scaling test, hardware/test conditions not stated in the abstract)
- Earlier conference statement of the CATRACA line of work; shares authors with the 2019 journal paper above and with the SBRC short-course chapter below, so the three are one research group and not three independent confirmations.

**Provenance**: PRISMA database-arm search, 2026-07-13 (search record 2 of 40). Appraised for venue integrity and content, then independently verified by a second LLM agent's verification pass; number check: numbers confirmed in source. Refresh (2026-11-23): DOI resolves to IEEE Xplore 8311440; "more than five million messages per second" re-read in the OpenAlex abstract; OpenAlex now types the record as a conference paper, so the preprint tag noted in the Evidence Level is gone.

#### Flink vs Spark Streaming for Machine-Learning NIDS on Data Streams (ACIS SNPD Winter, 2021)

**Authors**: Aymen Yahyaoui, Haithem Lakhdhar, Takoua Abdellatif, Rabah Attia
**Full title**: Machine learning based network intrusion detection for data streaming IoT applications
**Date**: 2021 (2021 21st ACIS International Winter Conference on Software Engineering, Artificial Intelligence, Networking and Parallel/Distributed Computing (SNPD-Winter), Ho Chi Minh City, Vietnam, 28-30 Jan 2021), pp. 51-56
**URL**: https://doi.org/10.1109/snpdwinter52325.2021.00019
**Evidence Level**: B (Long-running (21-edition), IEEE/ACIS-published conference series with no predatory or integrity flags — a defensible venue)
**Relevance**:
- Hypothesis H-STREAM-01 (engine selection)
- Answers, in part, the head-to-head engine comparison this review names as open work (Section 4.4, Future Direction 4)

**Key Findings**:
- A direct peer-reviewed Flink-versus-Spark-Streaming comparison on an IoT intrusion-detection workload (two public datasets), whose abstract leans toward Flink ("considerable throughputs and high detection accuracy especially for Apache Flink"). The abstract's headline claim is qualitative, so the paper is carried for the existence and direction of the comparison, not for a throughput number.

**Provenance**: PRISMA database-arm search, 2026-07-13 (search record 3 of 40). Appraised for venue integrity and content, then independently verified by a second LLM agent's verification pass; number check: no numbers to check. Refresh (2026-11-23): full title, pages and abstract direction confirmed at Crossref and OpenAlex; full text paywalled and unread.

#### Adaptive and Auto-Scaling Stream Processing for Real-Time Intrusion Detection (IEEE GLOBECOM, 2018)

**Authors**: G. V. Loganathan, Jagath Samarabandu, Xianbin Wang
**Date**: 2018 (2018 IEEE Global Communications Conference (GLOBECOM))
**URL**: https://doi.org/10.1109/glocom.2018.8647489
**Evidence Level**: A (Genuinely peer-reviewed IEEE flagship conference paper (documented multi-reviewer process, IEEE Xplore/Scopus/WoS pedigree); the precision/recall numbers are measured against the real, published CICIDS2017 intrusion-detection dataset (not a network simulator), and throughput was measured on the actual system)
**Relevance**:
- Hypothesis H-STREAM-01 (elastic vs monolithic stream processing)
- Book ch02 §2.2 (components: collection and pipeline) [was: Chapter 7] (Ingestion) — the elastic-scaling argument

**Key Findings**:
- average precision of 99.98%
- average recall of 93.42%
- processing over 2.5 million events per second
- Uses the Wisdom CEP engine; the auto-scaling deployment is reported to use fewer resources than a monolithic one at the same load, which is the architectural claim the review makes from vendor sources elsewhere.

**Provenance**: PRISMA database-arm search, 2026-07-13 (search record 4 of 40). Appraised for venue integrity and content, then independently verified by a second LLM agent's verification pass; number check: numbers confirmed in source.
**Refresh (2026-11-23)**: DOI resolves to IEEE Xplore 8647489 (paywalled, so this pass checked the abstract only, not the full text). The three figures are verbatim in the abstract ('an average precision of 99.98% and an average recall of 93.42% while processing over 2.5 million events per second'), and so is the resource claim ('consumes significantly fewer system resources than the monolithic deployment of CEP rules'). The qualifier 'at the same load' was not re-checked against the full text. The published title is 'Real-Time Intrusion Detection in Network Traffic Using Adaptive and Auto-Scaling Stream Processor'. No journal follow-up was found. A longer treatment of the same Wisdom work is Gobinath Loganathan's University of Western Ontario thesis, 'Real-time Intrusion Detection using Multidimensional Sequence-to-Sequence Machine Learning and Adaptive Stream Processing' (https://ir.lib.uwo.ca/etd/5523), and the Wisdom code (https://github.com/slgobinath/wisdom) was last pushed 2022-12-14.

#### AIDA Framework — Real-Time Correlation and Prediction of Intrusion Detection Alerts (ARES, 2019)

**Authors**: Martin Husák, Jaroslav Kašpar
**Date**: 2019 (14th International Conference on Availability, Reliability and Security (ARES 2019 / CyberTIM workshop), Canterbury, UK)
**URL**: https://doi.org/10.1145/3339252.3340513
**Evidence Level**: A (Genuinely peer-reviewed ACM conference paper from an identifiable, durable academic group (Husak/Kaspar, Masaryk University CSIRT-MU) with a multi-year publication trail on the same real production system (SABU/Warden), evaluated on real alert data from a live platform rather than simulation)
**Relevance**:
- Hypothesis H-STREAM-01 (stream processing for alert correlation)
- Book ch04 §4.3-4.5 (Sigma, coverage) + Appendix M [was: Chapter 9] (Detection) — pipeline-side correlation

**Key Findings**:
- Deployed as an analytical component of SABU, an alert-sharing platform in which a community of peer organizations exchange alerts from intrusion detection systems and honeypots, on a live feed of around 1.7 million alerts per day (first half of 2019). The authors call it an experimental deployment, run on one commodity server (Xeon E5520, 16 GB RAM) with Kafka 2.2.0, Spark 2.2.0 and Esper 8.0.0. The paper does not itself use the word 'production' for SABU.

**Provenance**: PRISMA database-arm search, 2026-07-13 (search record 13 of 40). Appraised for venue integrity and content, then independently verified by a second LLM agent's verification pass; number check: numbers confirmed in source.
**Refresh (2026-11-23)**: re-read in the authors' version (Wayback copy of https://is.muni.cz/publication/1540256/2019-CyberTIM-AIDA-Framework-paper.pdf), which describes 'the experimental deployment' receiving 'around 1.7 million alerts per day'. A follow-up from the same group, Husák, Bajtoš, Kašpar, Bou-Harb and Čeleda, 'Predictive Cyber Situational Awareness and Personalized Blacklisting', ACM TMIS 11(4), 2020 (https://doi.org/10.1145/3386250), processes '12 million alerts from 34 intrusion detection systems in 3 organizations gathered in an alert sharing platform' with what its abstract calls 'our analytical framework' (the abstract does not name AIDA or SABU), and reports a predictive blacklist 'the size of only 3% of the raw data' with 'more than 60% of its entries' predicting accurately 'in operational, real-world settings'. Code: https://github.com/CSIRT-MU/AIDA-Framework (last pushed 2021-11-11).

#### Cloud-Based Snort NIDS Using Containers and Big Data (Big Data and Cognitive Computing, 2022)

**Authors**: Ferry Astika Saputra, Muhammad Salman, Jauari Akhmad Nur Hasim, Isbat Uzzin Nadhori, Kalamullah Ramli
**Date**: 2022 (Big Data and Cognitive Computing (BDCC), Vol. 6, Issue 1, Article 19 (2022))
**URL**: https://doi.org/10.3390/bdcc6010019
**Evidence Level**: B (Legitimately peer-reviewed and properly indexed (Scopus Q1, ESCI, Ei Compendex) with no documented integrity problem specific to this journal; real measured Kafka/big-data testbed numbers, not simulation)
**Venue appraisal (2026-07-13)**: MDPI — class `mdpi_or_similar_apc_but_indexed`. No integrity flags found.
**Relevance**:
- Hypothesis H-STREAM-01 (Kafka ingest throughput)
- Book ch02 §2.2 (components: collection and pipeline) [was: Chapter 7] (Ingestion) — the containerized-sensor pattern

**Key Findings**:
- Apache Kafka achieved a maximum message rate of 650,000 messages/sec
- Maximum throughput of 172 MBps streaming data into Spark and Hadoop
- Kafka message-rate and throughput figures measured on a single Kafka broker feeding a lambda-architecture (Spark and Hadoop) backend.

**Provenance**: PRISMA database-arm search, 2026-07-13 (search record 14 of 40). Appraised for venue integrity and content, then independently verified by a second LLM agent's verification pass; number check: numbers confirmed in source.
**Refresh (2026-11-23)**: re-read at the MDPI article page. Both figures are verbatim, and the results section scopes them to one broker ('a single broker can process about 100 million messages, with a maximum message rate of 650,000 messages/s, and the maximum throughput was 172 MBps'). The published title is 'The Next-Generation NIDS Platform: Cloud-Based Snort NIDS Using Containers and Big Data'. No newer edition or same-group follow-up on this platform was found.

#### Faust vs Streamz — Complex Event Processing Engines for IoT Intrusion Detection (Computers, MDPI, 2026)

**Authors**: Maryam Abbasi, Filipe Cardoso, Paulo Váz, José Silva, Filipe Sá, Pedro Martins
**Date**: 2026 (Computers (MDPI), ISSN 2073-431X)
**URL**: https://doi.org/10.3390/computers15030200
**Evidence Level**: A (Confirmed DOAJ-listed, Scopus/ESCI/DBLP/Ei Compendex-indexed journal from an identifiable, non-predatory publisher, with a full, detailed, methodologically transparent abstract reporting controlled experiments with explicit statistics on two real datasets rather than a simulation or an unevaluated proposal)
**Venue appraisal (2026-07-13)**: MDPI AG — class `mdpi_or_similar_apc_but_indexed`. No integrity flags found.
**Relevance**:
- Hypothesis H-STREAM-01 (engine selection under a security workload)
- Directly answers Future Direction 4 (Section 4.4): a like-for-like engine benchmark on an identical security workload, with significance testing

**Key Findings**:
- Streamz: 4450 events/sec throughput, 89% efficiency, 40 MB memory, 12 ms median latency
- Faust: 93-98% intrusion-detection accuracy, 1.4% CPU utilization standard deviation
- Faust vs Kafka Streams detection quality: 96.2% vs 96.8% (0.6 pp difference, not statistically significant, p=0.318)
- Statistically significant performance differences across all metrics (p<0.001, Cohen's d>0.8)
- Streamz maintains >95% efficiency up to 3500 events/sec; Faust degrades beyond 2500 events/sec
- The closest published analogue to this program's own engine benchmarks: same workload across engines, effect sizes and p-values reported rather than a single headline multiple.

**Provenance**: PRISMA database-arm search, 2026-07-13 (search record 23 of 40). Appraised for venue integrity and content, then independently verified by a second LLM agent's verification pass; number check: numbers confirmed in source.

#### SPARCS — Stream-Processing Architecture for Real-Time Cyber-Physical Security (IEEE eScience, 2019)

**Authors**: Reinhard Gentz, Sean Peisert, Joshua Boverhof, Dan Gunter
**Date**: 2019 (2019 IEEE 15th International Conference on eScience (eScience 2019))
**URL**: https://doi.org/10.1109/escience.2019.00028
**Evidence Level**: A (Real, established, peer-reviewed IEEE conference (CORE A eScience series); no integrity flags of any kind; full text confirms genuine LBNL deployment work with at least one directly measured hardware benchmark (Protobuf/MsgPack/JSON serialization timing on a BeagleBone Black minicomputer, Python and C++))
**Relevance**:
- Book ch06 (variants) + Appendix C [was: Chapter 6] (Architecture) — an end-to-end collection/transport/storage/processing reference design
- Serialization-format selection (ch05 §5.1 (table format) [was: Chapter 8]): the measured Protobuf/MsgPack/JSON spread is directly comparable to the format decisions this review discusses

**Key Findings**:
- Protobuf serialization (Python): 47.0197 ms; deserialization: 48.6306 ms
- MsgPack serialization (Python): 0.6806 ms; deserialization: 0.3453 ms
- JSON serialization (Python): 6.4709 ms; deserialization: 2.0404 ms
- Protobuf serialization (C++): 0.79528 ms; deserialization: 0.66304 ms
- MsgPack serialization (C++): 0.47313 ms; deserialization: 0.29642 ms
- JSON serialization (C++): 0.18463 ms; deserialization: 0.29469 ms
- Authored at Lawrence Berkeley National Laboratory. The only record in the search set to receive a clean CITE with no venue caveat.

**Provenance**: PRISMA database-arm search, 2026-07-13 (search record 24 of 40). Appraised for venue integrity and content, then independently verified by a second LLM agent's verification pass; number check: numbers confirmed in source.
**Refresh (2026-11-23)**: all twelve Table I timings re-checked verbatim in the open-access copy (https://escholarship.org/content/qt3pj19498/qt3pj19498.pdf). The table times one second of PMU data (6,304 bytes raw) on a BeagleBone Black. The published title is 'SPARCS: Stream-Processing Architecture Applied in Real-Time Cyber-Physical Security' (pp. 199-202, a short paper). No newer edition or follow-up was found.

#### Practical Performance of a Distributed Processing Framework for ML-Based NIDS (IEEE COMPSAC, 2024)

**Authors**: M. Kajiura, Junya Nakamura
**Date**: 2024 (2024 IEEE 48th Annual Computers, Software, and Applications Conference (COMPSAC 2024))
**URL**: https://doi.org/10.1109/compsac61105.2024.00355
**Evidence Level**: A (Established, rigorous, peer-reviewed IEEE flagship conference (48th edition, <25% acceptance, 3+ reviews/paper); no integrity flags; full text confirms real measured throughput/latency on named real hardware (9-node Kubernetes cluster), directly on point for the review's pipeline-vs-accuracy methodological stance)
**Relevance**:
- Hypothesis H3-PERFORMANCE-01 (pipeline throughput is distinct from model accuracy)
- Supports this review's core methodological stance: the pipeline, not the classifier, is where the throughput goes

**Key Findings**:
- Decision Tree: 22,972 sessions/sec (~9.0 Gbps), ~340-350 ms latency
- Naive Bayes: 22,736 sessions/sec (~9.0 Gbps), ~340-350 ms latency
- Random Forest: 19,869 sessions/sec (~7.5 Gbps), ~340-350 ms latency
- SVM: 8,413 sessions/sec (~3.0 Gbps), ~530 ms latency
- kNN: 723 sessions/sec (~250 Mbps), ~1.5 s latency
- Baseline (no classifier): 23,596 sessions/sec
- F1 scores of 0.967 / 0.964 / 0.974 for the Decision Tree / Naive Bayes / Random Forest configurations actually benchmarked (Table VI; §V-B runs each algorithm's highest-F1 classifier, which is the tuned one for NB, up from 0.599 at default, the default one for RF because the parameter search lowered it to 0.972, and either one for DT, which the search left at 0.967) despite large throughput gaps
- Bottlenecks identified in Zeek, Logstash, and Elasticsearch processes
- Separates framework performance from model accuracy and locates the bottlenecks in Zeek, Logstash and Elasticsearch — the three fastest classifiers, in the configurations benchmarked, land within about 0.010 of each other on F1 (0.964 to 0.974). The arXiv deposit of this paper (record 33) is the same work and was removed as a duplicate.

**Provenance**: PRISMA database-arm search, 2026-07-13 (search record 26 of 40). Appraised for venue integrity and content, then independently verified by a second LLM agent's verification pass; number check: numbers confirmed in source.
**Refresh (2026-11-23)**: throughputs, latencies and bottlenecks re-checked verbatim in arXiv 2405.13066v1 (the IEEE version of record is paywalled and was not re-read). The F1 spread is corrected because §V-B benchmarks each algorithm's highest-F1 classifier, which for RF is the default setting (0.974). No 2025-2026 follow-up by the same authors was found.

---

### Non-Vendor Production Deployments (search arm)

#### CERN — Large-Scale Intrusion Detection on Big Data Technologies (PoS, ISGC 2018)

**Authors**: Pablo Panero, Liviu Vâlsan, Vincent Brillault, Ioan Cristian Schuszter
**Date**: 2018 (PoS(ISGC2018)014 -- Proceedings of the International Symposium on Grids and Clouds 2018 in conjunction with Frontiers in Computational Drug Discovery (ISGC 2018 & FCDD), Vol. 327)
**URL**: https://doi.org/10.22323/1.327.0014
**Evidence Level**: B (Genuine, non-predatory, indexed proceedings venue (DOAJ + Scopus), but the review process is proceedings-level (organizer/convener review under an editorial committee), not full journal double-blind peer review -- so this doesn't clear the bar for tier A under the program's rule)
**Relevance**:
- Hypothesis H1-VOLUME-07 (production security-telemetry volumes)
- Book ch06 §6.3 (multi-engine variant, named deployments) [AMBIGUOUS] [was: Chapter 3] — a named, non-vendor production deployment at scale

**Key Findings**:
- processing in real time approximately one TB of data per day
- final goal of coping with at least 5 TB / day
- Valuable for what it is rather than what it measures: the corpus's production-scale evidence is otherwise almost entirely big-tech engineering blogs, and this is a named public-research deployment with no product to sell.

**Provenance**: PRISMA database-arm search, 2026-07-13 (search record 9 of 40). Appraised for venue integrity and content, then independently verified by a second LLM agent's verification pass; number check: numbers confirmed in source.
**Refresh (2026-11-23)**: 1 TB/day and the 5 TB/day goal re-checked verbatim in the PoS PDF (published title 'Building a large scale Intrusion Detection System using Big Data technologies'). Newer context from the same team (Tier B, conference slides): Vâlsan, 'Zeek and the Balance between Academic Freedom, Industrial Operations & Security', Zeek Workshop CERN, 2026-03-25 (https://zeek.org/wp-content/uploads/2026/04/Zeek-and-the-Balance-between-Academic-Freedom-Industrial-Operations-Security.pdf). It reports a Zeek 'cluster of 16 nodes (12 production, 4 QA)', '~2.5 billion daily connections' and '~1.2 TB of daily Zeek logs', on a stack of Apache Flume and Fluent Bit, Kafka, Spark and Go, Hadoop HDFS and OpenSearch. The 1.2 TB is Zeek logs only, while the 2018 figure covers the whole pipeline, so the two are not a like-for-like progress measure against the 5 TB goal. A 2020 CERN computing seminar gives the Kafka layer as '6 Kafka brokers, 3 Zookeeper nodes' at '~100,000 messages / sec on average' with a '72 hours retention period' (https://indico.cern.ch/event/927793/attachments/2073576/3485397/2020-07-08__Computing_Seminar__CERN_SOC.pdf).

#### INFN-CNAF — General-Purpose Data-Streaming Platform for Log Analysis and Security Protection (EPJ Web of Conferences, CHEP 2023)

**Authors**: Francesco Amori, Stefano Antonelli, Vincenzo Ciaschini, Antonio Falabella, Enrico Fattibene, F. Fornari, Daniele Lattanzio, Diego Michelotto, Lucia Morganti
**Date**: 2024 (EPJ Web of Conferences, Vol. 295, Art. 01032 — Proceedings of CHEP 2023 (26th International Conference on Computing in High Energy and Nuclear Physics))
**URL**: https://doi.org/10.1051/epjconf/202429501032
**Evidence Level**: B (Legitimate peer-reviewed proceedings at a DOAJ-sealed, Scopus-indexed venue with no integrity flags — the venue itself would support Tier A)
**Relevance**:
- Book ch06 §6.3 (multi-engine variant, named deployments) [AMBIGUOUS] [was: Chapter 3] — a second named non-vendor production deployment (WLCG Tier-1), alongside CERN above

**Key Findings**:
- A platform description rather than an evaluation: it reports the architecture in production but publishes no throughput or latency measurement, so it supports the deployment claim and not a performance claim.

**Provenance**: PRISMA database-arm search, 2026-07-13 (search record 25 of 40). Appraised for venue integrity and content, then independently verified by a second LLM agent's verification pass; number check: no numbers to check.
**Refresh (2026-11-23)**: full text re-read by the refresh pass (the independent check reached only the abstract page, so the quote below is single-checked). Production status is quoted from the Conclusions ('in production since Spring 2023 and receives log data from tens of servers running at INFN-CNAF data centre'), on a three-node Kafka cluster with OpenSearch and Wazuh. A search of the text found no platform throughput or latency figure, so the deployment claim stands and no performance claim is supported. The scale described is tens of servers, which is worth keeping in mind where this entry is grouped with 'production-scale' deployments. The published title is 'General purpose data streaming platform for log analysis, anomaly detection and security protection' (published online 2024-05-06). No CHEP 2024 or later follow-up by the same group was found.

---

### Storage Reduction, Compression & Query (search arm)

#### Time Models in Graph Databases for Security Log Analysis (International Journal of Web Information Systems, 2021)

**Authors**: Daniel Hofer, Markus Jäger, Aya Mohamed, Josef Küng
**Date**: 2021 (International Journal of Web Information Systems, Vol. 17, No. 5, pp. 427-448 (2021))
**URL**: https://doi.org/10.1108/ijwis-03-2021-0023
**Evidence Level**: A (Legitimate, Scopus/ESCI-indexed Emerald journal with no integrity flags found anywhere I checked; real query-performance measurement against real log data (not simulation or an unevaluated proposal))
**Relevance**:
- Book ch04 §4.2 (OCSF) + Appendix H [was: Chapter 8] (Schema and modelling) — temporal modelling of security logs
- The corpus carries no graph-database anchor; this is the only one the search returned

**Key Findings**:
- Compares three timestamp-storage models for query performance. The finding is comparative and qualitative — the simplest model also yields the simplest queries — so no figure is carried.

**Provenance**: PRISMA database-arm search, 2026-07-13 (search record 8 of 40). Appraised for venue integrity and content, then independently verified by a second LLM agent's verification pass; number check: no numbers to check.
**Refresh (2026-11-23)**: re-checked at abstract level only (the publisher's full text is bot-blocked this session). The abstract concludes that the simplest model 'is also the one yielding the simplest and fastest queries', and names its own limit: 'only one graph database was studied'. The same four authors published an earlier conference paper on the topic, 'On Applying Graph Database Time Models for Security Log Analysis' (FDSE 2020, Springer LNCS, https://doi.org/10.1007/978-3-030-63924-2_5), which this journal article appears to extend. The published title is 'A study on time models in graph databases for security log analysis'. No later follow-up on time models was found.

#### Efficient Host Intrusion Detection Using Hyperdimensional Computing (IEEE BigData, 2024)

**Authors**: Yujin Nam, Rachel King, Quinn Burke, Minxuan Zhou, Patrick McDaniel, Tajana Rosing
**Date**: 2024 (2024 IEEE International Conference on Big Data (IEEE BigData 2024), Washington DC, pp. 2645-2652)
**URL**: https://doi.org/10.1109/bigdata62323.2024.10825247
**Evidence Level**: A (Real-world-dataset evaluation (not simulation), from a rigorously and competitively peer-reviewed IEEE conference (18.4% acceptance for the 2024 edition per the 2026-07-13 appraisal record), with no integrity concerns found; the verification note in the same record disputes this basis, finding a CyberHunt workshop paper at IEEE BigData 2024 to which the 18.4% regular-paper rate does not apply and recommending Tier B, which is left for an owner ruling)
**Relevance**:
- Book ch04 §4.3-4.5 (Sigma, coverage) + Appendix M [was: Chapter 9] (Detection) — cited for its statement of the provenance-graph query-latency problem, which the review's cost-to-serve argument depends on

**Key Findings**:
- >90% detection accuracy
- The paper's headline speedups (up to 4,242x on CPU, up to 18,000x on a hardware accelerator, and power figures quoted in orders of magnitude) are measured against different baselines and different hardware than anything this review compares, and are deliberately NOT carried. What is carried is the framing: state-of-the-art provenance-graph query latencies are described as impractical for modern threat detection, from an authorship group including Patrick McDaniel and Tajana Rosing.

**Provenance**: PRISMA database-arm search, 2026-07-13 (search record 10 of 40). Appraised for venue integrity and content, then independently verified by a second LLM agent's verification pass; number check: numbers confirmed in source.
**Refresh (2026-11-23)**: '>90% detection accuracy', 'up to 4,242× speedups' and the carried sentence on 'query latencies that are impractical for modern threat detection' are verbatim in the abstract (IEEE Xplore 10825247, paywalled, so the full text was not re-read). The uncarried hardware-accelerator and power figures were not re-checked. No newer version by the same authors was found.

#### Workload-Aware Storage Reduction for Multi-Tenant SIEM on ClickHouse (IJACSA, 2026)

**Authors**: Nutthakorn Chalaemwongwan
**Date**: 2026 (International Journal of Advanced Computer Science and Applications (IJACSA), Vol. 17, No. 4, 2026)
**URL**: https://doi.org/10.14569/ijacsa.2026.0170474
**Evidence Level**: C (Read the full paper directly)
**Venue appraisal (2026-07-13)**: The Science and Information (SAI) Organization (thesai.org) — class `low_tier_legitimate`. Removed from DOAJ in 2017, per search-derived DOAJ-blog records (could not re-verify by a direct live DOAJ query this session). Publisher (SAI / thesai.org) has a documented history of appearing on Beall's list of potential predatory publishers, though Beall's-list criteria are contested and some sources describe SAI's more recent output as improved. Web of Science coverage is ESCI (Emerging Sources Citation Index) only, not the more selective SCIE — ranks 32.2 percentile (bottom third) of its WoS category with Journal Impact Factor 1.1. Sweeping, all-encompassing journal title ("International Journal of Advanced Computer Science and Applications") matching the APC-mill naming pattern this review was told to watch for. Single-author paper from a Thai vocational/technical college (KOSEN-KMITL), no co-authors or external institutional cross-check, with an explicit generative-AI-writing-assistance declaration on the manuscript itself.
**Relevance**:
- Hypothesis H3-PERFORMANCE-01 (ClickHouse for security analytics) and H-LOGCOMP-01 (machine-data compression)
- The closest published analogue to this program's own ClickHouse storage-reduction measurements

**Key Findings**:
- 79% uncompressed storage reduction (331.43 MiB to 68.67 MiB)
- 70% compressed storage reduction (35.10 MiB to 10.57 MiB)
- 56% column-count reduction (27 to 12 columns)
- compression ratio 9.4:1 baseline vs. 6.5:1 optimized
- query latency 144-170ms across RULE/INVESTIGATE/IOC/AGGREGATE query classes, all under 200ms ('sub-second')
- 100% Sigma detection-rule coverage preserved at optimal threshold tau*=0.23
- 74% uncompressed reduction under a uniform-distribution robustness check, vs. 79% under the primary Zipf-distributed workload
- READ THE VENUE APPRAISAL BEFORE CITING THIS. The figures were located in the source and are reported here faithfully, but the venue cannot carry a Level-A claim, so this paper does not corroborate the storage-reduction claim in the way a peer-reviewed source normally would — it records that the only indexed paper on the exact question sits in a weak venue. The ~$30,000/year saving is the paper's own back-of-envelope projection for a hypothetical 100 GB/day SOC, not a measured result, and is not carried. Note also that this author's other 2026 paper (ECTI-CIT, below) is the review's other peer-reviewed check on a vendor-sourced claim: the two are the same author and are not independent of each other.

**Provenance**: PRISMA database-arm search, 2026-07-13 (search record 12 of 40). Appraised for venue integrity and content, then independently verified by a second LLM agent's verification pass; number check: numbers confirmed in source.

#### Comparative Evaluation of Log-Reduction Techniques Using Vector on Public Security Datasets (ECTI-CIT, 2026)

**Authors**: Nutthakorn Chalaemwongwan
**Date**: 2026 (ECTI Transactions on Computer and Information Technology (ECTI-CIT), Vol. 20 No. 2 (April 2026))
**URL**: https://doi.org/10.37936/ecti-cit.2026202.264216
**Evidence Level**: A (Passes venue integrity: DOAJ-listed, Scopus-indexed, Diamond OA (no APC motive), double-blind reviewed, published by an established engineering-society journal with continuous history since 2005 — no predatory or delisting signal found)
**Venue appraisal (2026-07-13)**: ECTI Association (Electrical Engineering/Electronics, Computer, Telecommunications and Information Technology Association, Thailand); hosted on the TCI-Thaijo (Thailand Citation Index) platform — class `low_tier_legitimate`. No integrity flags found.
**Relevance**:
- Hypothesis H-COST-09 (pipeline reduction economics) — a dataset-based check on the Cribl/Vector-class reduction claims the corpus otherwise takes from vendor material
- Book ch02 §2.2 (components: collection and pipeline) [was: Chapter 7] (Ingestion) — the route/reshape/reduce pattern

**Key Findings**:
- Throughput improved by 45%
- Outbound traffic reduced by 80%
- Attack coverage maintained at 98%
- 3,000,000+ SOC log records evaluated
- Benchmarks five Vector-based reduction methods against a Filebeat baseline over 3M+ SOC records, reporting attack-coverage retention alongside the reduction — which is the honest way to state a reduction claim, since throwing away data always reduces volume and the question is what detection you lose. Same single author as the IJACSA ClickHouse paper above; the two are not independent.

**Provenance**: PRISMA database-arm search, 2026-07-13 (search record 35 of 40). Appraised for venue integrity and content, then independently verified by a second LLM agent's verification pass; number check: numbers confirmed in source.

---

### Security Data Lake & Forensics Architecture (search arm)

#### Data-Lake-Based Security Transmission and Storage Scheme for Streaming Big Data (Cluster Computing, 2024)

**Authors**: Xiaoyan Zhao, Conghui Zhang, Shaopeng Guan
**Date**: 2024 (Cluster Computing (Springer), Vol. 27, Issue 4, pp. 4741-4755; published online 2023-12-09)
**URL**: https://doi.org/10.1007/S10586-023-04201-9
**Evidence Level**: B (Venue is legitimate and currently indexed (Scopus/WoS, IF 7.31, not delisted), and no evidence ties this specific article to the journal's known special-issue paper-mill problem, so it is not disqualified on integrity grounds; the 2026-07-13 appraisal downgraded it from A because the full text could not be read)
**Venue appraisal (2026-07-13)**: Springer Science and Business Media LLC (Springer Nature) — class `established_journal`. Context only, not disqualifying for this article: Cluster Computing has a documented history of paper-mill infiltration via guest-edited special issues; Springer Nature's Research Integrity department has been retracting affected articles, and the journal appointed a dedicated Editor-in-Chief for Special Issues and capped concurrent guest-edited collections in response. I found no evidence this specific article (Vol 27, Issue 4, pp. 4741-4755; online 2023-12-09, issue July 2024; a 75-article issue with no special-issue label on the article page or the issue contents page) came from a flagged special issue, and the journal remains actively Scopus/WoS-indexed with a 2024 IF of 7.31 — it was never delisted.
**Relevance**:
- Hypothesis H-ARCH-01 (lakehouse/data-lake architecture for security data)
- Book ch06 (variants) + Appendix C [was: Chapter 6] (Architecture) — secure ingestion and storage of streaming security data

**Key Findings**:
- An ECC lightweight-encryption interceptor at the data source, an SSL-secured Flume/Kafka transport, and an LZO-compressed Hadoop data-lake storage layer. The published abstract reports roughly an 18% reduction in memory load attributed to the encryption interceptor; the figure was confirmed in the publisher's abstract by an independent check, but no full text was read, so it is recorded and not built upon. Cluster Computing has a documented paper-mill problem confined to guest-edited special issues; this is a regular-issue article, which is why it survives appraisal.

**Provenance**: PRISMA database-arm search, 2026-07-13 (search record 37 of 40). Appraised for venue integrity and content, then independently verified by a second LLM agent's verification pass; number check: numbers confirmed in source.
**Refresh (2026-11-23)**: the 18% figure re-checked verbatim in the Springer abstract ('reduces memory load by 18%'). The issue number is corrected to 4 per Crossref and OpenAlex. Neither the article page nor the Issue 4 contents page (75 articles) shows a special-issue label, which is consistent with the regular-issue reading but is not a publisher statement of it. The IF figure was not re-checked. The full text is still unread, and an SSRN preprint (https://doi.org/10.2139/ssrn.4134117) is the open route if the figure is ever built on, though that preprint was not opened and is not confirmed to be the same paper.

#### Digital-Forensics Architecture on a Security Lake for Automated Evidence Collection (Journal of Intelligent Systems, 2024)

**Authors**: Wasan Saad Ahmed, Ziyad Tariq Mustafa AL-Ta'I, Tamirat Abegaz, Ghassan Sabeeh Mahmood
**Date**: 2024 (Journal of Intelligent Systems, Vol. 33, Issue 1, art. 20240109; published 2024-12-09)
**URL**: https://doi.org/10.1515/JISYS-2024-0109
**Evidence Level**: B (Legitimate, DOAJ/Scopus/ESCI-indexed venue with documented double-anonymous peer review — no integrity flags found)
**Relevance**:
- Hypothesis H-ARCH-01 (security data lake) — the closest published statement of the security-lake thesis this review argues
- Book ch06 (variants) + Appendix C [was: Chapter 6] (Architecture)

**Key Findings**:
- A security-lake plus data-lake architecture for real-time forensic evidence collection across multiple cloud accounts and regions, stated to be validated on an actual AWS deployment. The full text (open access, read 2026-11-23) reports lake counts and creation times for the test deployment but no throughput, latency or cost measurement, so no quantitative result is carried. Venue verified at primaries: DOAJ-listed, Scopus Q2, double-anonymous review, not retracted.

**Provenance**: PRISMA database-arm search, 2026-07-13 (search record 38 of 40). Appraised for venue integrity and content, then independently verified by a second LLM agent's verification pass; number check: no numbers to check.
**Refresh (2026-11-23)**: full text read at De Gruyter Brill. The architecture is built on Amazon Security Lake (OCSF and Parquet) plus AWS modern data architecture, queried with Athena and Lake Formation and integrated with Wazuh, and validated on a university AWS organization, where it created eight regional lakes and one roll-up lake centralized in a forensics account. It is best read as an AWS-native instance of the security-lake pattern, which matters where the Relevance line calls it the closest published statement of the thesis.

---

### Framing & Position Sources (search arm)

#### Corporate Security Is a Big Data Problem (ACM Ubiquity, 2018)

**Authors**: Louisa Saunier, Kemal A. Delic
**Date**: 2018 (Ubiquity (ACM's web-based magazine), Vol. 2018, July, subtitled 'Big Data (Ubiquity symposium)')
**URL**: https://doi.org/10.1145/3158348
**Evidence Level**: B (Legitimate ACM in-house venue, no integrity flags found, but the peer review Ubiquity applies to commentaries is lighter than a full journal's (ACM's own materials distinguish 'peer-reviewed commentaries' from unreviewed 'blogs' within the same magazine, and I could not directly confirm on the ACM DL page — 403'd — which track this ran under))
**Relevance**:
- Section 1.2 (Literature gap) — a 2018 statement, in an ACM venue, of the thesis this review otherwise dates to vendor writing

**Key Findings**:
- Argues corporate security is a big-data problem and sketches a security-data-lake-to-'security cockpit' architecture. Ubiquity is ACM's editor-led web magazine, not a peer-reviewed journal — the review it applies to commentary is lighter than a journal's, so this is a framing source and not evidence.

**Provenance**: PRISMA database-arm search, 2026-07-13 (search record 27 of 40). Appraised for venue integrity and content, then independently verified by a second LLM agent's verification pass; number check: no numbers to check.
**Refresh (2026-11-23)**: DOI still resolves to the ACM DL, which returns 403 to automated fetch (bot-gating, not a paywall, since Ubiquity is free to read). The abstract was re-read at the OpenAlex record and still supports the architectural framing. The Wayback capture used for the July full-text read was rate-limited today. OpenAlex lists no citing work since 2025, so the entry stands as a 2018 framing source.

#### Machine Learning on Distributed Stream-Processing Platforms — Storm, Spark Streaming and Flink (SBRC Short Courses, 2018, in Portuguese)

**Authors**: Martin Andreoni Lopez, Igor Jochem Sanz, Antonio Gonzalez Pastana Lobato, Diogo M. F. Mattos, Otto Carlos M. B. Duarte (author list corrected 2026-11-17 to the chapter's title page)
**Date**: 2018 (Minicursos do XXXVI Simpósio Brasileiro de Redes de Computadores e Sistemas Distribuídos (SBRC 2018) — book chapter, SBC OpenLib (SOL))
**URL**: https://www.gta.ufrj.br/ftp/gta/TechReports/ASL18.pdf (author-hosted copy of the chapter, "Capítulo 3"; no DOI registered)
**Evidence Level**: B (Legitimate, non-predatory venue — SBC is Brazil's primary computer-science professional society, no integrity flags found — but this is a reviewed-proposal tutorial/survey chapter, not a blind-peer-reviewed original-research paper, and its numbers are not carried: the introduction's headline numbers are third-party citations, and the section 3.3 platform benchmark is the authors' own earlier work, matching their GLOBECOM 2016 platform comparison (10.1109/GLOCOM.2016.7841533) although the chapter's in-text citation points to their MobiSecServ 2018 paper; whether any of the chapter's other results are new to it was not established)
**Venue appraisal (2026-07-13)**: Sociedade Brasileira de Computação (SBC) — class `low_tier_legitimate`. No integrity flags found.
**Relevance**:
- Background for the engine-comparison discussion (Storm vs Spark Streaming vs Flink), including lambda-architecture treatment

**Key Findings**:
- A short-course/tutorial chapter, not a primary study. The introduction's figures are third-party citations, and the section 3.3 throughput and node-failure benchmark (Storm 0.9.4, Flink 0.10.2, Spark Streaming 1.6.1 on eight VMs on one host) is the group's own earlier work: its versions, hardware and loss figures match the authors' GLOBECOM 2016 paper (10.1109/GLOCOM.2016.7841533, not catalogued here), though the chapter cites their MobiSecServ 2018 paper for it. The detection-accuracy results in section 3.4 are also the group's own. No number is carried here. Shares authors with records 1 and 2 above (the CATRACA group).

**Provenance**: PRISMA database-arm search, 2026-07-13 (search record 28 of 40). Appraised for venue integrity and content, then independently verified by a second LLM agent's verification pass; number check: numbers confirmed in source.
**Refresh (2026-11-23)**: author-hosted PDF re-read (HTTP 200, 56 pages). The earlier 'every figure is third-party' wording was corrected, because section 3.3 presents the authors' own Storm / Flink / Spark Streaming benchmark. The chapter cites the group's MobiSecServ 2018 paper for it, but that paper tests Spark Streaming 1.3.1 only, and the versions, test host and message-loss figures match the group's GLOBECOM 2016 comparison (10.1109/GLOCOM.2016.7841533). The engine versions tested are several major lines old (Flink's stable documentation now serves 2.3, per the checkpointing entry), so the comparison reads as history, not as guidance on current engines.

---

### Recorded from the Search, Not Supporting a Claim in This Edition (search arm)

#### Data-Warehouse Modelling for Security-Log Management in a Government SOC (Jurnal Teknik Informatika, 2023)

**Authors**: Maya Asmita, Henny Henny, Samidi Samidi
**Date**: 2023 (Jurnal Teknik Informatika (JUTIF))
**URL**: https://doi.org/10.52436/1.jutif.2023.4.4.649
**Evidence Level**: C (Not predatory, but not internationally indexed either — a real university-run journal at national (SINTA 2) accreditation tier only, so its peer-review rigor cannot be externally corroborated the way DOAJ/Scopus indexing would provide)
**Venue appraisal (2026-07-13)**: Informatics Department, Universitas Jenderal Soedirman (UNSOED), Indonesia — class `low_tier_legitimate`. Not found in DOAJ (direct ISSN searches for 2723-3863 returned no match). Not on the journal's own claimed indexing list, which conspicuously omits DOAJ, Scopus, and Web of Science despite listing 17 other indexers. One entry on that self-reported indexing list, 'ISI Indexing,' is a separate low-value indexing service unrelated to Clarivate's Web of Science despite the deceptively similar name — a soft red flag common at this journal tier, though not itself proof of predatory intent.
**Relevance**:
- No hypothesis in this edition. Recorded as the only treatment the search returned of Kimball-style dimensional modelling applied to SOC log data

**Key Findings**:
- A modelling proposal with no evaluation, in a journal not listed in DOAJ, Scopus or Web of Science. Recorded for completeness of the search record; it supports nothing.

**Provenance**: PRISMA database-arm search, 2026-07-13 (search record 6 of 40). Appraised for venue integrity and content, then independently verified by a second LLM agent's verification pass; number check: no numbers to check.
**Refresh (2026-11-23)**: DOI and the publisher PDF both resolve (HTTP 200). Crossref gives Vol. 4, No. 4, pp. 987-994. The abstract says testing was done with Pentaho. The July full-text read found that this testing was an ETL build check with no performance or analyst-outcome evaluation, so the 'no evaluation' description stands. DOAJ still returns no match for ISSN 2723-3863. OpenAlex lists no citing work since 2025.

#### High-Performance FPGA Architecture for Data-Stream Processing — IPsec Gateway (International Journal of Electronics and Telecommunications, 2018)

**Authors**: Mateusz Korona, Krzysztof Skowron, Mateusz Trzepiński, Mariusz Rawski
**Date**: 2018 (International Journal of Electronics and Telecommunications, 2018, Vol. 64, No. 3, pp. 351-356)
**URL**: https://doi.org/10.24425/123532
**Alt URL**: http://journals.pan.pl/Content/107747/PDF/48_1444.pdf (publisher PDF; the DOI landing page served a bot-check interstitial on 2026-11-23)
**Evidence Level**: A (Legitimate, national-academy-backed, Scopus+DOAJ-indexed journal with no integrity flags found)
**Relevance**:
- No hypothesis in this edition. Recorded from the systematic search: hardware acceleration of the ingest tier is outside the scope this review sets (software architecture on commodity infrastructure), and is noted as adjacent work rather than folded into a finding

**Key Findings**:
- Gateway 2.0 best DES config (8/8/8/16): 10,227.44 Mbit/s for 1500-byte packets at a 128-packet stream (computed by the paper's formula 1 from cycles per packet and the synthesis Fmax; the paper reports no on-the-wire throughput measurement for this design)
- Gateway 2.0 best AES-CBC config (8/8/12/8): 5,518.80 Mbit/s for 1500-byte packets at a 128-packet stream (computed by the paper's formula 1 from cycles per packet and the synthesis Fmax; the paper reports no on-the-wire throughput measurement for this design)
- Peer-reviewed and sound; simply not on any claim this review makes.

**Provenance**: PRISMA database-arm search, 2026-07-13 (search record 11 of 40). Appraised for venue integrity and content, then independently verified by a second LLM agent's verification pass; number check: numbers confirmed in source.
**Refresh (2026-11-23)**: re-read at the publisher PDF. Both throughput figures are verbatim in Tables V and IX, and section V states they were computed by the prototype's estimation formula from cycle counts and the synthesis clock rate, so they are design-estimate throughputs. OpenAlex lists no citing work since 2025.

#### Hybrid Stream Processing for Runtime Protection in Remote Driving (IEEE ICIN, 2026)

**Authors**: Tarek Stolz, Aliza Katharina Reif, O. H. Ramírez-Agudelo, Michael Karl
**Date**: 2026 (2026 29th Conference on Innovation in Clouds, Internet and Networks (ICIN), Athens, Greece, 30 Mar - 2 Apr 2026)
**URL**: https://doi.org/10.1109/icin69025.2026.11481838
**Evidence Level**: A (Venue integrity is solid: ICIN is a genuinely established, continuously-run, IEEE-published conference (29th edition, DLR-funded, real institutional authors, no publisher instability or indexing red flags of any kind) — nothing here resembles the mill pattern found in rank 21)
**Relevance**:
- No hypothesis in this edition. Recorded from the systematic search as an automotive/OT instance of the online-vs-offline detection split

**Key Findings**:
- Its headline figure — an online operator beating an offline detector 'by 584.3% in latency time' — is malformed as written (a percentage improvement in latency is not interpretable without the direction and the base), so no number is carried.

**Provenance**: PRISMA database-arm search, 2026-07-13 (search record 22 of 40). Appraised for venue integrity and content, then independently verified by a second LLM agent's verification pass; number check: numbers confirmed in source.

#### Architectural and Analytical Aspects of Big Data for IoT System Security (Cybersecurity: Education, Science, Technique, 2026)

**Authors**: U. P. Panovyk, Rostyslav Tkachuk, Valeriia Balatska, V. A. Yashchuk
**Date**: 2026 (Кібербезпека: освіта, наука, техніка (Cybersecurity: Education, Science, Technique))
**URL**: https://doi.org/10.28925/2663-4023.2026.33.1144
**Evidence Level**: B (Real, DOAJ-verified, double-blind peer-reviewed journal with no integrity red flags found — legitimate though niche and not Scopus/WoS-indexed)
**Venue appraisal (2026-07-13)**: Borys Grinchenko Kyiv University — class `low_tier_legitimate`. No integrity flags found.
**Relevance**:
- No hypothesis in this edition. Recorded from the systematic search

**Key Findings**:
- Simulated evaluation, qualitative claims only, no figures with units in the abstract.

**Provenance**: PRISMA database-arm search, 2026-07-13 (search record 29 of 40). Appraised for venue integrity and content, then independently verified by a second LLM agent's verification pass; number check: no numbers to check.

#### Analysis of Logs in the Environment of Email Services (IEEE ICETA, 2020)

**Authors**: Martin Chovanec, Martin Havrilla, Eva Chovancová
**Date**: 2020 (2020 18th International Conference on Emerging eLearning Technologies and Applications (ICETA), Technical University of Košice, Slovakia)
**URL**: https://doi.org/10.1109/iceta51985.2020.9379260
**Evidence Level**: B (Venue integrity is clean: a real, long-running IEEE-co-sponsored conference with standard peer review, no predatory or delisting signal found)
**Relevance**:
- No hypothesis in this edition. Recorded from the systematic search as a store-selection comparison (Elasticsearch, Kafka, Redis, Splunk, MongoDB) for audit records

**Key Findings**:
- The comparison method could not be established from the available text, so it is recorded and not relied on.

**Provenance**: PRISMA database-arm search, 2026-07-13 (search record 32 of 40). Appraised for venue integrity and content, then independently verified by a second LLM agent's verification pass; number check: no numbers to check.
**Refresh (2026-11-23)**: DOI resolves to IEEE Xplore (paywalled, bot-gated to automated fetch). The abstract was re-read and still names the five stores without stating how they were compared, so the entry's caution stands. Pages 74-79 per Crossref. OpenAlex lists one citing work since 2025, a 2026 Research Square preprint (10.21203/rs.3.rs-10592797/v1) that was not read.

#### Binary-Feature-Extraction Data-Provenance System on Flink (IEEE CyberC, 2018)

**Authors**: Yangyizhou Wang, Lan Li, Lei Fan
**Date**: 2018 (2018 International Conference on Cyber-Enabled Distributed Computing and Knowledge Discovery (CyberC), 10th edition, Zhengzhou, China)
**URL**: https://doi.org/10.1109/cyberc.2018.00045
**Evidence Level**: C (Venue integrity is clean (legitimate long-running IEEE conference, no predatory or delisting signal))
**Relevance**:
- No hypothesis in this edition. Recorded from the systematic search as provenance-as-security-telemetry implemented on a stream processor

**Key Findings**:
- A pattern the corpus does not otherwise carry; noted for a future edition rather than cited here.

**Provenance**: PRISMA database-arm search, 2026-07-13 (search record 34 of 40). Appraised for venue integrity and content, then independently verified by a second LLM agent's verification pass; number check: no numbers to check.
**Refresh (2026-11-23)**: DOI resolves to IEEE Xplore (paywalled, bot-gated). The abstract was re-read and still supports the architectural description, with no figures to carry. OpenAlex shows no citing work since 2025.

---


## Citation-Graph Snowball Admissions (2026-11-07)

Admitted from the 2026-11-07 snowball pass (`methods/snowball-candidates-2026-11.md`): one hop backward through Crossref reference lists and forward through OpenCitations from 35 DOI-resolved peer-reviewed seeds, deduplicated against this bibliography and the July PRISMA records, then ranked against the thin claims in `methods/claim-evidence-matrix-2026-11.md`. Three rows were identified by targeted known-item lookup against a named thin claim rather than by the graph walk, and are marked so. Each one-line description below was checked against the abstract at the source named in its Validation Status line; none carries a figure beyond what that abstract or the first page states.

---

#### Matched and Mismatched SOCs: A Qualitative Study on Security Operations Center Issues (Kokulu et al., ACM CCS 2019)

**Authors**: Faris Bugra Kokulu, Ananta Soneji, Tiffany Bao, Yan Shoshitaishvili, Ziming Zhao, Adam Doupé, Gail-Joon Ahn
**Date**: 2019 (Proceedings of the 2019 ACM SIGSAC Conference on Computer and Communications Security, pp. 1955-1970)
**URL**: https://doi.org/10.1145/3319535.3354239
**DOI**: 10.1145/3319535.3354239
**Evidence Level**: A (peer-reviewed, ACM CCS 2019)
**Relevance**:
- Book ch01 §1.5 (the claim that SOC problems are people, process and organizational problems, today carried only by a LinkedIn quotation of Chuvakin) and ch07 §7.4 (organizational barriers): an interview study that finds non-technical issues alongside technical ones.
- Scope limit: 18 interviews, qualitative; it supports the existence and kind of organizational issues, not a share of them, so it does not back ch07's "well over half" figure.

**Key Findings** (abstract): 18 semi-structured interviews with SOC analysts and managers across industry sectors identified technical and non-technical issues in SOCs, and inherent disagreements between SOC managers and their analysts that the authors say risk SOC efficiency and effectiveness.
**Citations**: Kokulu, F.B., Soneji, A., Bao, T., Shoshitaishvili, Y., Zhao, Z., Doupé, A., Ahn, G.-J. (2019). *Matched and Mismatched SOCs: A Qualitative Study on Security Operations Center Issues*. ACM CCS 2019, 1955-1970.
**Notes**: Identified by targeted known-item lookup for the ch01/ch07 organizational claim, not by the graph walk. ACM DL returned 403 to automated fetch.
**Validation Status**: ✅ Verified 2026-11-07 (Crossref record for title, seven authors, venue, pages and DOI; abstract read at the Semantic Scholar record and matched word for word against the OpenAlex copy; the ACM landing page itself was not reachable).
**Refresh (2026-11-23)**: abstract re-read; Crossref metadata unchanged. OpenAlex counts 96 citing works since 2025, among them Tariq, Chhetri, Nepal and Paris, 'Alert Fatigue in Security Operations Centres: Research Challenges and Opportunities' (ACM Computing Surveys 57(9), 2025, 10.1145/3723158). That is a candidate peer-reviewed review for the organizational-issues thread, not yet admitted or appraised.

---

#### Finding Bugs in Database Systems via Query Partitioning (Rigger & Su, OOPSLA 2020)

**Authors**: Manuel Rigger, Zhendong Su
**Date**: 2020 (Proceedings of the ACM on Programming Languages 4, OOPSLA, pp. 1-30)
**URL**: https://doi.org/10.1145/3428279
**DOI**: 10.1145/3428279
**Evidence Level**: A (peer-reviewed, PACMPL / OOPSLA 2020)
**Relevance**:
- Book ch03 §3.4 (the silent wrong answer): the peer-reviewed anchor for the claim that a mature query engine can return an incorrect result with no error, which the chapter today carries only on the SDW Lab cross-engine scorecard.
- Also ch05 §5.4 and ch06 §6.3, which point back to the ch03 scorecard.

**Key Findings** (abstract): defines logic bugs as bugs that make a DBMS return an incorrect result, for example by omitting a row, and notes they are likely to go unnoticed; Ternary Logic Partitioning splits a query on p, NOT p and p IS NULL and compares the recombined result to the original; the campaign found 175 bugs in MySQL, TiDB, SQLite and CockroachDB, 125 fixed, of which 77 were logic bugs.
**Citations**: Rigger, M., Su, Z. (2020). *Finding Bugs in Database Systems via Query Partitioning*. Proc. ACM Program. Lang. 4(OOPSLA), 1-30.
**Notes**: Identified by targeted known-item lookup for the ch03 silent-engine claim, not by the graph walk. Its NULL-partition mechanism is the same three-valued-logic hazard the ch03 allowlist case shows. ACM DL returned 403 to automated fetch.
**Validation Status**: ✅ Verified 2026-11-07 (Crossref record for title, authors, venue, volume and DOI; full abstract read at the Semantic Scholar record, including the 175 / 125 / 77 counts, and matched against the OpenAlex copy).
**Refresh (2026-11-23)**: abstract re-read and the 175 / 125 / 77 counts confirmed verbatim. The mechanism is current: Rigger's group continues the line, most recently with SQLancer++ (Zhong and Rigger, 'Scaling Automated Database System Testing', ASPLOS 2026, 10.1145/3779212.3790215), whose abstract reports 196 previously unknown bugs across 18 DBMSs, 180 of them fixed. That abstract does not split logic bugs from crash bugs, so only the qualitative point carries.

---

#### Don't Hold My Data Hostage: A Case for Client Protocol Redesign (Raasveldt & Mühleisen, PVLDB 2017)

**Authors**: Mark Raasveldt, Hannes Mühleisen (Centrum Wiskunde & Informatica)
**Date**: 2017 (Proceedings of the VLDB Endowment 10(10), pp. 1022-1033)
**URL**: https://www.vldb.org/pvldb/vol10/p1022-muehleisen.pdf
**DOI**: 10.14778/3115404.3115408
**Evidence Level**: A (peer-reviewed, PVLDB)
**Relevance**:
- Book ch05 §5.2 (Arrow as the wire): the peer-reviewed anchor for the row-protocol serialization tax, which the chapter carries today on a lab figure and on the Arrow Flight SQL project blog (re-tiered B on 2026-11-07).

**Key Findings** (abstract and introduction, read at the VLDB PDF): transferring a large result set from a database to a client is expensive and can dominate query execution time; the authors measure result-set serialization across a large part of the database market, show the inefficiencies, and propose a columnar serialization method that improves transmission performance by an order of magnitude.
**Citations**: Raasveldt, M., Mühleisen, H. (2017). *Don't Hold My Data Hostage: A Case for Client Protocol Redesign*. PVLDB 10(10), 1022-1033.
**Notes**: Identified by targeted known-item lookup for the ch05 §5.2 claim, not by the graph walk. The paper predates Arrow Flight and does not evaluate it; it supports the mechanism, not any Arrow-specific number.
**Validation Status**: ✅ Verified 2026-11-07 (VLDB proceedings PDF fetched; title, authors and abstract read on page 1; Crossref record for DOI and pages).
**Refresh (2026-11-23)**: VLDB PDF re-fetched (HTTP 200) and the abstract sentences confirmed verbatim. The transfer-cost problem is still an active research topic: Gavriilidis, Beedkar, Böhm and Markl, 'Fast and Scalable Data Transfer Across Data Systems' (XDBC, PACMMOD 3(3), 2025, 10.1145/3725294), cites this paper and reports that its transfer framework outperforms state-of-the-art generic transfer tools by up to 5x. That is a different comparison and supports the mechanism only.

---

#### Tools and Benchmarks for Automated Log Parsing (Zhu et al., ICSE-SEIP 2019)

**Authors**: Jieming Zhu, Shilin He, Jinyang Liu, Pinjia He, Qi Xie, Zibin Zheng, Michael R. Lyu
**Date**: 2019 (2019 IEEE/ACM 41st International Conference on Software Engineering: Software Engineering in Practice, pp. 121-130)
**URL**: https://doi.org/10.1109/ICSE-SEIP.2019.00021
**Alt URL**: https://arxiv.org/abs/1811.03509
**DOI**: 10.1109/ICSE-SEIP.2019.00021
**Evidence Level**: A (peer-reviewed, ICSE-SEIP 2019)
**Relevance**:
- Book ch03 (bad parsing logic): the widely used parser benchmark line that Petrescu et al. (ISSRE 2023, above) argue overstates parser quality under a grouping metric, so the two are best read together, this one for what parsers were reported to achieve and Petrescu for the template-level correction. The 0.73 average that Petrescu quotes does not appear in this paper: Petrescu's reference for it is He et al., A Survey on Automated Log Analysis for Reliability Engineering (ACM Computing Surveys 54(6), 2021, 10.1145/3460345), by an overlapping group, while this paper's Table IV reports per-parser average accuracy from 0.482 (LogSig) to 0.865 (Drain) on 2,000-message samples; how the survey arrived at 0.73, and whether it derives from these results, was not checked.

**Key Findings** (abstract, read at the arXiv abstract page): evaluates 13 automated log parsers on 16 log datasets spanning distributed systems, supercomputers, operating systems, mobile systems, server applications and standalone software, reports accuracy, robustness and efficiency, and releases the tools and benchmarks for reuse.
**Citations**: Zhu, J., He, S., Liu, J., He, P., Xie, Q., Zheng, Z., Lyu, M.R. (2019). *Tools and Benchmarks for Automated Log Parsing*. ICSE-SEIP 2019, 121-130.
**Notes**: Snowball, backward from Petrescu et al. (ISSRE 2023). Table IV was read at the arXiv full text on 2026-11-23; the per-parser averages are recorded in Relevance for provenance and are not carried as a claim.
**Validation Status**: ✅ Verified 2026-11-07 (arXiv abstract page for title and abstract; Crossref record for venue, seven authors, pages and DOI).
**Refresh (2026-11-23)**: arXiv full text read. The same group's successor benchmark is Loghub-2.0 (Jiang, Liu, Huang, Li, Huo, Gu, Chen, Zhu and Lyu, 'A Large-Scale Evaluation for Log Parsing Techniques: How Far Are We?', ISSTA 2024, 10.1145/3650212.3652123). Its abstract says the original Loghub 'suffers from limited scale and representativeness', and it re-evaluates 15 parsers on 14 datasets averaging 3.6 million lines each with a metric less sensitive to imbalanced data. That is a scale and representativeness limitation acknowledged by the benchmark's own authors, separate from the template-level metric correction Petrescu makes.

---

#### An Empirical Evaluation of Columnar Storage Formats (Zeng et al., PVLDB 2023)

**Authors**: Xinyu Zeng, Yulong Hui, Jiahong Shen, Andrew Pavlo, Wes McKinney, Huanchen Zhang (Tsinghua University; Carnegie Mellon University; Voltron Data)
**Date**: 2023 (Proceedings of the VLDB Endowment 17(2), pp. 148-161)
**URL**: https://www.vldb.org/pvldb/vol17/p148-zeng.pdf
**Alt URL**: https://arxiv.org/abs/2304.05028
**DOI**: 10.14778/3626292.3626298
**Evidence Level**: A (peer-reviewed, PVLDB)
**Relevance**:
- Book ch05 §5.1 (the writer is the lever): the peer-reviewed counterpart to the lab's writer-as-read-lever arm; it attributes Parquet and ORC performance and size to encoding and layout decisions inside the format, including dictionary encoding.

**Key Findings** (abstract, read at the VLDB PDF): benchmarks the internals of Parquet and ORC under different workload configurations and identifies design decisions that suit modern hardware and real-world data, including using dictionary encoding by default, favouring decoding speed over compression ratio for integer encodings, making block compression optional, and embedding finer-grained auxiliary structures.
**Citations**: Zeng, X., Hui, Y., Shen, J., Pavlo, A., McKinney, W., Zhang, H. (2023). *An Empirical Evaluation of Columnar Storage Formats*. PVLDB 17(2), 148-161.
**Notes**: Snowball, backward from F3 (SIGMOD 2025) and FastLanes, and forward from Delta Lake (PVLDB 2020). Same lead author as the F3 entry; a different paper.
**Validation Status**: ✅ Verified 2026-11-07 (VLDB proceedings PDF fetched; title, six authors and the abstract's design-decision sentence read in the text; Crossref record for DOI and pages).
**Refresh (2026-11-23)**: VLDB PDF re-fetched (HTTP 200) and the design-decision sentence confirmed verbatim. A follow-up sharing four of these authors, F3, is already catalogued. A further 2025 peer-reviewed comparison, Liu, Pavlenko, Interlandi and Haynes, 'Data formats in analytical DBMSs: performance trade-offs and future directions' (The VLDB Journal 34(3), 2025, 10.1007/s00778-025-00911-1), evaluates Arrow, Parquet and ORC as formats inside an analytical DBMS and finds that each has trade-offs. That is consistent with this entry and not yet admitted.

---

#### Exploiting Cloud Object Storage for High-Performance Analytics (Durner, Leis & Neumann, PVLDB 2023)

**Authors**: Dominik Durner, Viktor Leis, Thomas Neumann (Technische Universität München)
**Date**: 2023 (Proceedings of the VLDB Endowment 16(11), pp. 2769-2782)
**URL**: https://www.vldb.org/pvldb/vol16/p2769-durner.pdf
**DOI**: 10.14778/3611479.3611486
**Evidence Level**: A (peer-reviewed, PVLDB)
**Relevance**:
- Book ch05 §5.1 and §5.3 (open files on object storage read by a columnar engine) and ch02 §2.3 (the warm-tier economics): peer-reviewed evidence that analytics can run directly on cloud object storage without a local cache at warehouse-like performance.
- Scope limit: general analytics (no security workload) and a research engine (Umbra), and it derives retrieval cost configurations rather than a SIEM-versus-object-storage price ratio.

**Key Findings** (abstract, read at the VLDB PDF): presents the first in-depth study of cloud object stores for analytical query processing, derives cost- and performance-optimal retrieval configurations, introduces the AnyBlob download manager, and reports that Umbra with AnyBlob, without caching, achieves performance similar to cloud data warehouses that cache data on local SSDs.
**Citations**: Durner, D., Leis, V., Neumann, T. (2023). *Exploiting Cloud Object Storage for High-Performance Analytics*. PVLDB 16(11), 2769-2782.
**Notes**: Snowball, backward from F3 (SIGMOD 2025) and forward from Delta Lake (PVLDB 2020).
**Validation Status**: ✅ Verified 2026-11-07 (VLDB proceedings PDF fetched; title, authors and abstract read in the text; Crossref record for DOI and pages).
**Refresh (2026-11-23)**: VLDB PDF re-read (HTTP 200); abstract unchanged and every Key Findings clause is verbatim in it, including "even without caching, Umbra with integrated AnyBlob achieves similar performance to state-of-the-art cloud data warehouses that cache data on local SSDs". No newer edition or same-author follow-up paper found in a targeted search; the AnyBlob repository at https://github.com/durner/AnyBlob is not archived and was last pushed 2026-10-28. F3 (SIGMOD 2025, entry above) is later work from a different group (CMU and others) that cites this paper. Foundational and still accurate.

---

#### NoDoze: Combatting Threat Alert Fatigue with Automated Provenance Triage (Hassan et al., NDSS 2019)

**Authors**: Wajih Ul Hassan, Shengjian Guo, Ding Li, Zhengzhang Chen, Kangkook Jee, Zhichun Li, Adam Bates (NEC Laboratories America; University of Illinois at Urbana-Champaign; Virginia Tech)
**Date**: 2019 (Network and Distributed System Security Symposium 2019)
**URL**: https://www.ndss-symposium.org/ndss-paper/nodoze-combatting-threat-alert-fatigue-with-automated-provenance-triage/
**DOI**: 10.14722/ndss.2019.23349
**Evidence Level**: A (peer-reviewed, NDSS 2019)
**Relevance**:
- Book ch07 §7.3 (the dead-tail rules and the alert noise their deletion removed) and ch04 §4.5: a peer-reviewed statement that analysts receive more alerts than they can investigate and miss true attacks in the noise.
- Scope limit: one enterprise deployment (NEC Labs America) and an estimated, not a field-measured, reduction.

**Key Findings** (abstract, read at the NDSS paper page): names "threat alert fatigue" as more alerts than analysts can investigate, so true attack alerts are missed among false alarms; NoDoze builds a causal dependency graph per alert and scores it against the enterprise's event history; on a dataset of 364 threat alerts it ranked true alerts above false ones, and with a cutoff threshold the authors estimate an 84% reduction in false-alarm volume.
**Citations**: Hassan, W.U., Guo, S., Li, D., Chen, Z., Jee, K., Li, Z., Bates, A. (2019). *NoDoze: Combatting Threat Alert Fatigue with Automated Provenance Triage*. NDSS 2019.
**Notes**: Snowball, backward from the hyperdimensional-computing host intrusion detection entry (IEEE BigData 2024).
**Validation Status**: ✅ Verified 2026-11-07 (NDSS paper page for title, seven authors with affiliations and abstract; Crossref record for DOI).
**Refresh (2026-11-23)**: DOI now resolves straight to the NDSS PDF (HTTP 200); abstract re-read and the 364 alerts, the ranking result and the estimated 84% false-alarm reduction are verbatim ("we estimate that our system decreases the volume of false alarms by 84%"). The paper body restates the 84% without the hedge, so keep the abstract's 'estimate' wording. Newer work on the same alert-fatigue problem: Uetz et al. (arXiv 2026, entry below) evaluate risk-based alert prioritization on eight datasets, a preprint that agrees in direction but measures ranking quality (AUROC), not a false-alarm count. Foundational and still accurate.

---

#### A Comprehensive Approach to Intrusion Detection Alert Correlation (Valeur et al., IEEE TDSC 2004)

**Authors**: Fredrik Valeur, Giovanni Vigna, Christopher Kruegel, Richard A. Kemmerer
**Date**: 2004 (IEEE Transactions on Dependable and Secure Computing 1(3), pp. 146-169)
**URL**: https://doi.org/10.1109/TDSC.2004.21
**Alt URL**: https://sites.cs.ucsb.edu/~vigna/publications/2004_valeur_vigna_kruegel_kemmerer_TDSC_Correlation.pdf (author copy)
**DOI**: 10.1109/TDSC.2004.21
**Evidence Level**: A (peer-reviewed, IEEE TDSC)
**Relevance**:
- Book ch04 §4.2-4.5 (cross-source correlation): the canonical decomposition of alert correlation into components, and an early peer-reviewed finding that correlation effectiveness depends heavily on the data it is fed, which is the chapter's verify-the-values argument in older form.

**Key Findings** (abstract, read at the author copy): presents a general correlation model with a comprehensive set of components and a framework built on it, applied to several well-known intrusion detection datasets; the components were effective at alert reduction and abstraction, and the effectiveness of each component depended heavily on the nature of the dataset analysed.
**Citations**: Valeur, F., Vigna, G., Kruegel, C., Kemmerer, R.A. (2004). *A Comprehensive Approach to Intrusion Detection Alert Correlation*. IEEE TDSC 1(3), 146-169.
**Notes**: Snowball, backward from the AIDA alert-correlation entry (ARES 2019).
**Validation Status**: ✅ Verified 2026-11-07 (author-hosted PDF of the TDSC article, page 1 title, authors and abstract; Crossref record for volume, pages and DOI).
**Refresh (2026-11-23)**: author copy re-read (HTTP 200) and the DOI still resolves to IEEE Xplore document 1366134; the abstract sentence the chapter leans on is verbatim ("the effectiveness of a component depends heavily on the nature of the data set analyzed"). A journal article has no newer edition; later surveys were not searched beyond the AIDA (ARES 2019) entry already held. Foundational and still accurate.

---

#### BtrBlocks: Efficient Columnar Compression for Data Lakes (Kuschewski et al., SIGMOD 2023)

**Authors**: Maximilian Kuschewski, David Sauerwein, Adnan Alhomssi, Viktor Leis (Technische Universität München; Friedrich-Alexander-Universität Erlangen-Nürnberg)
**Date**: 2023 (Proceedings of the ACM on Management of Data 1(2), Article 118, SIGMOD 2023)
**URL**: https://doi.org/10.1145/3589263
**Alt URL**: https://www.cs.cit.tum.de/fileadmin/w00cfj/dis/papers/btrblocks.pdf (author version)
**DOI**: 10.1145/3589263
**Evidence Level**: A (peer-reviewed, PACMMOD / SIGMOD 2023)
**Relevance**:
- Book ch05 §5.1 (encoding choices decide size and scan cost): a second peer-reviewed source, alongside Zeng et al., that encoding rather than the general-purpose codec decides decompression cost and therefore scan time and dollars on object storage.

**Key Findings** (abstract, read at the author version): argues that open formats such as Parquet are not optimized for remotely accessed data lakes and high-throughput networks, that inefficient decompression makes scans CPU-bound and raises query time and cost, and presents BtrBlocks, an open columnar format built on lightweight encoding schemes for fast decompression and high compression ratios.
**Citations**: Kuschewski, M., Sauerwein, D., Alhomssi, A., Leis, V. (2023). *BtrBlocks: Efficient Columnar Compression for Data Lakes*. Proc. ACM Manag. Data 1(2), Article 118.
**Notes**: Snowball, backward from F3 (SIGMOD 2025); the FastLanes entry already mentions BtrBlocks in passing, and this is its first standalone entry.
**Validation Status**: ✅ Verified 2026-11-07 (author-hosted author version PDF, page 1 title, authors and abstract; Crossref record for DOI).
**Refresh (2026-11-23)**: TUM author version re-read (HTTP 200); the abstract sentences on Parquet, CPU-bound decompression and lightweight encodings are verbatim, and the PDF labels itself the author's version, not the version of record. Later format work held in this bibliography: the FastLanes file format (PVLDB 2025), which also prefers lightweight cascaded encodings over generic codecs and reports decoding about 7x faster than BtrBlocks on its corpus, and F3 (SIGMOD 2025), from which this entry was snowballed. Foundational and still accurate for the ch05 use.

---
## Handbook Footnote Companions (2026-11-07)

Added 2026-11-07 so that every source the handbook (`moar-cybersecurity-data`) now footnotes has a verified companion entry for the style handbook's JIT check: the Reis modeling book behind the *Mixed Model Arts* integration, six [un]prompted talks (March 2026 and October 2026) cited in ch03 and ch04, the Humio post cited in ch05, and the social-media paper that is the standard reference for "context collapse." Each was checked at the primary page named in its Validation Status line. Talks are Tier B practitioner evidence: the presenters' own builds and experiments, not independently replicated.

---

#### Mixed Model Arts: The Building Blocks of Cross-Disciplinary Data Modeling (Reis, Practical Data Media 2026)

**Author**: Joe Reis (foreword by Bill Inmon)
**Date**: 2026 (First Edition, first printing 2026; publisher site gives September 27, 2026)
**Publisher**: Practical Data Media, Salt Lake City, Utah (Book 1 in the Mixed Model Arts series)
**ISBN**: 979-8-952478-00-8 (paperback); 979-8-952478-01-5 (ebook), as printed on the copyright page
**URL**: https://mixedmodelarts.com
**Alt URL**: https://practicaldata.media
**Evidence Level**: B (authoritative practitioner book; conceptual modeling reference, not a quantitative source)
**Relevance**:
- Handbook ch04 §4.2: the four kinds of time (event, ingestion, processing, valid; Ch 10) and the term "context collapse" as data modelers use it (Ch 13).
- Handbook ch03 §3.6: the grain audit checklist, `COUNT(*)` against `COUNT(DISTINCT grain key)` and per-join grain effect (Ch 8).
- Handbook front matter ("About this book"): the recommended companion for modeling fundamentals.

**Key Findings**: a general data-modeling book with no security material; distinguishes event, ingestion, processing and valid time and recommends naming columns for the time they hold; describes context collapse as a failure mode "often described as" such, usually "a byproduct of optimizing for speed or storage efficiency"; gives a grain audit checklist for hidden duplicates and join fan-out.
**Citations**: Reis, J. (2026). *Mixed Model Arts: The Building Blocks of Cross-Disciplinary Data Modeling*. Practical Data Media.
**Notes**: Every application to security telemetry in the handbook is the handbook author's transfer, and the footnotes say so. Reis does not claim the term "context collapse"; see the Marwick & boyd entry below for its standard reference. The publisher site hyphenates the ISBNs as 979-8-95247-800-8 / 979-8-95247-801-5 (same digits); the copyright page is treated as primary. Carries no headline statistic.
**Validation Status**: ✅ Verified 2026-11-07 (copyright and title pages of the book text: title, subtitle, author, publisher, city, edition, both ISBNs; mixedmodelarts.com fetched for subtitle, foreword, 2026-09-27 date, 474-page paperback; practicaldata.media lists it as the publisher's first release).

---

#### Exploring the AI Automation Boundary for Threat Hunting at Datadog (Nagarajan, [un]prompted March 2026)

**Speaker**: Arthi Nagarajan (Software Engineer for Internal Threat Detection, Datadog)
**Date**: March 4, 2026 ([un]prompted, San Francisco, Day 2, Stage 1, 15:05-15:30)
**URL**: https://unpromptedcon.org/day-2/
**Alt URL**: https://citation.thinkst.com/talk/101336
**Evidence Level**: B (practitioner conference talk; the team's own build and evaluation)
**Relevance**:
- Handbook ch03 §3.4: an LLM hunting copilot that writes syntactically valid queries against the wrong fields, the gap between query syntax accuracy and semantic accuracy, and schema discovery as the fix.

**Key Findings** (deck pp. 6, 7, 17, 20): Datadog's Hunting Copilot evolved from a single agent with basic tooling into an orchestrator-subagent system centered on field discovery and dynamic log-schema exploration; the deck reports 92% syntax accuracy against 72% semantic accuracy for generated queries.
**Citations**: Nagarajan, A. (2026, March 4). *Exploring the AI Automation Boundary for Threat Hunting at Datadog*. [un]prompted, San Francisco.
**Notes**: The deck's title page drops "at Datadog" ("Exploring the AI Automation Boundary for Threat Hunting"); the handbook footnote uses the deck title. Tier B for what the team built and measured; Datadog's claims about its own MCP server are Tier C for how well it works (vendor, bias flagged). The twenty-point gap in the handbook is the handbook author's subtraction; the deck does not report how the two failure sets overlap.
**Validation Status**: ✅ Verified 2026-11-07 (official Day 2 agenda page fetched: title, speaker, affiliation, date, slot; Thinkst Citation listing for title and speaker; deck text read for the title page and the cited pages).

---

#### The Hard Part Isn't Building the Agent: On Measuring Agent Effectiveness to Improve It (Saxe, [un]prompted March 2026)

**Speaker**: Joshua Saxe (listed as AI Security Technical Lead, Meta; the deck says he had left Meta to co-found a startup days before the talk)
**Date**: March 3, 2026 ([un]prompted, San Francisco, Day 1, Stage 1, 09:35-10:00)
**URL**: https://unpromptedcon.org/day-1/
**Evidence Level**: B (practitioner conference talk; argument and the speaker's own evaluation experience)
**Relevance**:
- Handbook ch03 §3.6: ground truth in security is noisy, so evaluation sets a noise ceiling; seed known answers and score the misses rather than trusting labels.

**Key Findings** (deck): argues that rigorous evaluation, not building, is the bottleneck for deploying autonomous cyber defenses; deck p. 12 states that "every supposed source of truth has a significant error rate, including human sources," which is the noisy-ground-truth point the handbook cites.
**Citations**: Saxe, J. (2026, March 3). *The Hard Part Isn't Building the Agent: On Measuring Agent Effectiveness to Improve It*. [un]prompted, San Francisco.
**Notes**: The deck's title page reads "Evaluation is the hard part (in building the autonomous cyber defenses we need)", which is the title the handbook footnote cites; both refer to this one talk. The handbook's "formerly Meta" follows the deck's speaker slide.
**Validation Status**: ✅ Verified 2026-11-07 (official Day 1 agenda page fetched: title, speaker, affiliation, date, slot; deck text read for the title page, speaker slide and p. 12).

---

#### The Model Is NOT a Security Control: Prompt Injection Dies at the Token Sampler (Ovando, [un]prompted II October 2026)

**Speaker**: Vince Ovando (AI Security Researcher & Engineer, IOActive per the deck; the agenda lists no organization)
**Date**: October 2026 ([un]prompted II, San Francisco, October 27-29, 2026; main agenda, Stage 2, 13:55-14:20)
**URL**: https://unpromptedcon.org/agenda-10-2026/
**Evidence Level**: B (practitioner conference talk; self-run experiment)
**Relevance**:
- Handbook ch03 §3.5: constrain the output space before generation (grammar-constrained decoding at the sampler) instead of relying on the model or a classifier gate as the control.

**Key Findings** (deck and transcript): per-control attack success rates for a secret-exfiltration objective, a Qwen3-1.7B comparison of a classifier gate against grammar-constrained decoding (282,000 attacks each), and valid-tool-call rates under constraint; run size stated on the deck as "~6M inference calls" and "2.46M attack trials" on the presenter's own hardware.
**Citations**: Ovando, V. (2026, October). *The Model Is NOT a Security Control: Prompt Injection Dies at the Token Sampler*. [un]prompted II, San Francisco.
**Notes**: One attack objective, one author's hardware, not independently replicated; the handbook footnote carries the same scope limit.
**Validation Status**: ✅ Verified 2026-11-07 (official October 2026 agenda page fetched: title verbatim, speaker, slot, conference dates; deck text read for the IOActive affiliation and run-size figures; transcript held locally).

---

#### We Don't Need an LLM for That (Mountrouidou & Wilson, [un]prompted II October 2026)

**Speakers**: Xenia Mountrouidou (Principal Applied AI Scientist, AppGate); Casey Wilson (Principal Software Engineer, BusinessLoans.com)
**Date**: October 2026 ([un]prompted II, San Francisco, October 27-29, 2026; Villages programme, Stage 2, 12:00-12:25)
**URL**: https://unpromptedcon.org/agenda-10-2026/
**Evidence Level**: B (practitioner conference talk; the presenters' own experiment)
**Relevance**:
- Handbook ch03 §3.5: the right-sized model; language models win on text-heavy tasks such as phishing, while gradient-boosted trees and tabular models win on structured network data.

**Key Findings** (transcript): compared zero-shot LLMs, fine-tuned small models, XGBoost and tabular transformers on phishing and network-intrusion datasets, with class-prior baselines; language models led on phishing text and tree-based models on tabular network data.
**Citations**: Mountrouidou, X., & Wilson, C. (2026, October). *We Don't Need an LLM for That*. [un]prompted II, San Francisco.
**Notes**: The agenda capitalizes the title "We don't need an LLM for That"; the handbook uses that form. Per-dataset scores appear on slides; the transcript gives the phishing percentages and baselines in words, without the network-data figures.
**Validation Status**: ✅ Verified 2026-11-07 (official October 2026 agenda page fetched: title, both speakers with affiliations, slot; transcript held locally).

---

#### Your AI Analyst Is Confidently Wrong: Adversarial QC for Agentic Security Analysis (Kovalsky & Arshad, [un]prompted II October 2026)

**Speakers**: Maxim Kovalsky (Managing Director, AI Security CoE, Consortium Networks); Ali Arshad (Senior Security Consultant, Consortium Networks)
**Date**: October 2026 ([un]prompted II, San Francisco, October 27-29, 2026; Villages programme, Stage 2, 14:20-14:45)
**URL**: https://unpromptedcon.org/agenda-10-2026/
**Evidence Level**: B (practitioner conference talk; one team's experiments)
**Relevance**:
- Handbook ch03 §3.6: as analytic workload grows, model errors are dominated by missed findings (recall loss) rather than hallucination, so QC should seed known answers and score misses.

**Key Findings** (transcript): tested several models on increasingly heavy security-analysis tasks; accuracy degraded mainly through recall loss, with models missing details in the documents they were given, and compared error-correction strategies including adversarial review.
**Citations**: Kovalsky, M., & Arshad, A. (2026, October). *Your AI Analyst Is Confidently Wrong: Adversarial QC for Agentic Security Analysis*. [un]prompted II, San Francisco.
**Notes**: The talk itself does not name the employer; the agenda does (Consortium Networks).
**Validation Status**: ✅ Verified 2026-11-07 (official October 2026 agenda page fetched: title verbatim, both speakers with affiliations, slot; transcript held locally).

---

#### What Designing a Cyber Ontology for Agents Taught Us About Governance (Chismon, [un]prompted II October 2026)

**Speaker**: David Chismon (Chief Security Architect, UK National Cyber Security Centre)
**Date**: October 2026 ([un]prompted II, San Francisco, October 27-29, 2026; Villages programme, Stage 1, 13:55-14:20)
**URL**: https://unpromptedcon.org/agenda-10-2026/
**Evidence Level**: B (practitioner conference talk by a government security architect; experience report, not official NCSC guidance)
**Relevance**:
- Handbook ch04 §4.1: orders of controls for agent access (privileged access workstations as the analogy) and ablation as the way to learn which control is doing the work.

**Key Findings** (transcript and slides): NCSC's experience designing a cyber ontology for agent use, and the governance lessons it produced about which controls agents need and in what order.
**Citations**: Chismon, D. (2026, October). *What Designing a Cyber Ontology for Agents Taught Us About Governance*. [un]prompted II, San Francisco.
**Notes**: Tier B rather than A because it is a conference talk, not a published NCSC standard or guidance document. The transcript renders "PAWs" as "pause"; the handbook footnote records the fix.
**Validation Status**: ✅ Verified 2026-11-07 (official October 2026 agenda page fetched: title verbatim, speaker, affiliation, slot; slides and transcript held locally).

---

#### How Humio Leverages Kafka and Brute-Force Search to Get Blazing-Fast Search Results (Humio Staff, CrowdStrike blog 2021)

**Author**: Humio Staff
**Date**: September 28, 2021 (CrowdStrike blog; originally published on humio.com January 6, 2020)
**URL**: https://www.crowdstrike.com/en-us/blog/how-humio-leverages-kafka-and-brute-force-search-to-get-blazing-fast-search-results/
**Evidence Level**: C (vendor blog; bias flagged: CrowdStrike sells Falcon LogScale, formerly Humio, so every speed figure is the vendor's own and unmeasured. Per the 2026-11-03 vendor-documentation ruling the description of the index-free design is B-grade, and the speed claims are C; the entry is tiered C because the handbook cites its figures.)
**Relevance**:
- Handbook ch05 §5.3a: the named counter-example to index-first SIEM design, a needle hunt served by time-scoped brute-force scan over compressed data instead of an index lookup.

**Key Findings**: "While we consider Humio to be index-free, we do index time series information so all ingested data can be found based on its time"; streaming querying gives "no time to apply complex indexes that could make searching faster"; worked example of a 1 GB search taking 1.1 seconds that "now takes 0.7 seconds" once the data is compressed 10x.
**Citations**: Humio Staff (2021, September 28). *How Humio Leverages Kafka and Brute-Force Search to Get Blazing-Fast Search Results*. CrowdStrike blog. (Originally humio.com, 2020-01-06.)
**Notes**: The post's "30-40x the speed of a regular search" claim is unanchored and is not cited by the handbook.
**Validation Status**: ✅ Verified 2026-11-07 (CrowdStrike URL fetched: byline, 2021-09-28 date, the "originally published Jan. 6, 2020 on humio.com" note, and the three quoted sentences).
**Refresh (2026-11-23)**: CrowdStrike URL re-read (HTTP 200); byline, both dates and the three quoted sentences unchanged. The current product documentation still describes the design: the LogScale page *Index-Free Data Storage* (https://library.humio.com/logscale-architecture/training-arch-op-indexfree.html, HTTP 200) says "LogScale stores the start and end time every segment and will only search the specified time interval" (sic), which is B-grade for what the feature does under the 2026-11-03 ruling; the speed figures stay C.

---

#### I Tweet Honestly, I Tweet Passionately: Twitter Users, Context Collapse, and the Imagined Audience (Marwick & boyd, New Media & Society 2011)

**Authors**: Alice E. Marwick, danah boyd
**Date**: 2011 (New Media & Society 13(1), pp. 114-133; online first 2010-07-07)
**URL**: https://doi.org/10.1177/1461444810365313
**DOI**: 10.1177/1461444810365313
**Evidence Level**: A (peer-reviewed journal article)
**Relevance**:
- Handbook ch04 §4.2: the standard reference for the term "context collapse," which Reis borrows into data modeling and the handbook applies to field coarsening in security telemetry. Cited as the term's standard reference only, not as its origin.

**Key Findings**: describes context collapse as the flattening of multiple audiences into one on social media, and how users manage an imagined audience in response.
**Citations**: Marwick, A.E., & boyd, d. (2011). I tweet honestly, I tweet passionately: Twitter users, context collapse, and the imagined audience. *New Media & Society*, 13(1), 114-133.
**Notes**: Social-media research, not security; carries no claim the handbook relies on beyond the term's standard reference. boyd styles her name in lower case.
**Validation Status**: ✅ Verified 2026-11-07 (Crossref record: title, both authors, journal, volume 13, issue 1, pages 114-133, DOI; Crossref's issued date 2010-07-07 is the online-first date).
**Refresh (2026-11-23)**: metadata unchanged at Crossref. Origin claim narrowed: boyd's own account (zephoria.org, 2013-12-08) says this paper is "the first time that I used 'context collapse' instead of 'collapsed contexts' in published writing", traces the idea to her 2002 MIT thesis on "collapsed contexts", and notes that Michael Wesch published an article with 'context collapse' in its title in 2009 (*Explorations in Media Ecology* 8(2), doi:10.1386/eme.8.2.99_1; Crossref gives pp. 99-114), before this paper appeared. By her account the two were building on common roots in Goffman and Meyrowitz, so the coinage is shared and uncertain; cite this paper as the standard reference, which the handbook footnote already does.

---
## Thin-Claim Legs and Handbook Companions, Second Pass (2026-11-07)

Added 2026-11-07 after a thin-claims scouting pass (Gemini Flash) and the owner's approval of the resulting handbook edits. Six peer-reviewed papers now carry handbook footnotes as the outside leg for a mechanism the book previously stated on first-hand or lab evidence alone; one practitioner blog carries the softened data-preparation range in ch01; and two sources the handbook already footnoted, Conway (1968) and the Sigma specification, get the companion entries they lacked. Flash's raw answers are Tier C and were not used: each one-line finding below was re-read at the abstract or primary page named in its Validation Status line, and venue identity was confirmed at the Crossref record (container title and event) plus the publisher or conference page, because DBLP returned HTTP 429 during this pass. Several Flash numbers for these papers (CLP "1.75:1 vs 32:1", LogGrep "5% of Elasticsearch / 20×") are body-level or invented and are not carried.

---

#### CLP: Efficient and Scalable Search on Compressed Text Logs (Rodrigues, Luo & Yuan, USENIX OSDI 2021)

**Authors**: Kirk Rodrigues, Yu Luo, Ding Yuan (University of Toronto and YScope Inc.)
**Date**: July 2021 (15th USENIX Symposium on Operating Systems Design and Implementation, OSDI '21, pp. 183-198)
**URL**: https://www.usenix.org/conference/osdi21/presentation/rodrigues
**DOI**: none (USENIX open-access proceedings)
**Evidence Level**: A (peer-reviewed, USENIX OSDI 2021)
**Relevance**:
- Handbook ch02 §2.3: the peer-reviewed leg for the index-size half of the storage floor, that a search index carries bytes on the order of the raw logs while a compressed structured layout carries far fewer.
- Scope limit: no SIEM-versus-object-storage price ratio; the multiple stays the author's desk calculation (C) and lab floor (B).

**Key Findings** (abstract): Elasticsearch and Splunk Enterprise index logs for fast search, "yet the size of the index is within the same order of magnitude as the raw log size"; CLP compresses losslessly at a significantly higher ratio than common compressors while searching comparably to or faster than both, ingests over 13x faster than them, and is shown scaling to petabytes.
**Citations**: Rodrigues, K., Luo, Y., & Yuan, D. (2021). CLP: Efficient and Scalable Search on Compressed Text Logs. *15th USENIX Symposium on Operating Systems Design and Implementation (OSDI 21)*, 183-198.
**Notes**: Bias flag: the authors list YScope Inc., the company that builds on CLP, so the comparison against Elasticsearch and Splunk is by an interested party, though peer-reviewed. The handbook cites only the abstract-level index-size statement.
**Validation Status**: ✅ Verified 2026-11-07 (USENIX presentation page fetched: title, authors, affiliation, abstract text, pp. 183-198 in the BibTeX).
**Refresh (2026-11-23)**: USENIX page re-read (HTTP 200); the index-size sentence, the 13x ingest figure and the YScope affiliation are verbatim. Same-group follow-up: Wang et al., "μSlope: High Compression and Fast Search on Semi-Structured Logs," OSDI '24, pp. 529-544 (https://www.usenix.org/conference/osdi24/presentation/wang-rui; YScope, Uber and University of Toronto, so the same interest flag applies), extends the approach to JSON logs and reports "21.9:1 to 186.8:1 compression ratio" against unnamed semi-structured data management systems; it does not restate the index-size claim, so this entry stays the citation for that sentence.

---

#### LogGrep: Fast and Cheap Cloud Log Storage by Exploiting both Static and Runtime Patterns (Wei et al., EuroSys 2023)

**Authors**: Junyu Wei, Guangyan Zhang, Junchao Chen, Yang Wang, Weimin Zheng, Tingtao Sun, Jiesheng Wu, Jiangwei Jiang (Tsinghua University, The Ohio State University, Alibaba Group)
**Date**: May 2023 (Proceedings of the Eighteenth European Conference on Computer Systems, EuroSys '23, pp. 452-468)
**URL**: https://doi.org/10.1145/3552326.3567484
**DOI**: 10.1145/3552326.3567484
**Alt URL**: https://yangwang83.github.io/papers/eurosys23-final39.pdf (author camera-ready)
**Evidence Level**: A (peer-reviewed, ACM EuroSys 2023)
**Relevance**:
- Handbook ch02 §2.3: second peer-reviewed leg for the storage mechanism; the abstract reports that structured, compressed log storage cut query latency and overall cost by an order of magnitude against the state-of-the-art works it was compared with, evaluated on production log types from Alibaba Cloud (near-line debugging logs) and not in a reported deployment. The paper body splits that result: overall cost is 36% of CLP, 34% of gzip+grep and 7% of ElasticSearch on the Alibaba logs, so the order-of-magnitude cost gap is against the Elasticsearch index and the gap against the compression baselines is about 3x.

**Key Findings** (abstract): parses logs into variable vectors by static patterns, extracts runtime patterns within each vector, and splits them into stamped "Capsules" that queries can skip without decompressing; on 21 production log types from Alibaba Cloud and 16 public log types, it reduces query latency and overall cost (storage plus compression and query compute) by an order of magnitude compared to state-of-the-art works.
**Citations**: Wei, J., Zhang, G., Chen, J., Wang, Y., Zheng, W., Sun, T., Wu, J., & Jiang, J. (2023). LogGrep: Fast and Cheap Cloud Log Storage by Exploiting both Static and Runtime Patterns. *EuroSys '23*, 452-468.
**Notes**: The abstract's comparators are "state-of-the-art works" in log compression, not named SIEMs or Elasticsearch; Flash's "5% of Elasticsearch / 20x" is not in the abstract and is not carried as a headline; the paper body does name its comparators (CLP, ElasticSearch, gzip+grep) and gives overall cost at 7% of ElasticSearch on the Alibaba logs and 5% on the public logs (§6.2). Three co-authors are Alibaba Group employees.
**Validation Status**: ✅ Verified 2026-11-07 (Crossref record: title, eight authors, EuroSys '23 event, pages, DOI; abstract read on page 1 of the author-hosted camera-ready PDF at yangwang83.github.io; ACM DL returned a bot challenge).
**Refresh (2026-11-23)**: abstract and §6.2 re-read in the author camera-ready PDF (HTTP 200), now added as Alt URL; the 21 production and 16 public log types and the abstract's order-of-magnitude sentence are verbatim, the paper reports an evaluation and no deployment, and the body puts overall cost at 36% of CLP, 34% of gzip+grep and 7% of ElasticSearch, so the Relevance line was narrowed to match. Same-group follow-ups: the journal extension "Exploiting Data-pattern-aware Vertical Partitioning to Achieve Fast and Low-cost Cloud Log Storage" (Wei, Zhang, Chen, Wang et al., ACM Transactions on Storage 20(2), 2024, doi:10.1145/3643641), and LogCloud (Wang, Wei, Aiken, Zhang et al., PVLDB 18(8):2362-2370, 2025, doi:10.14778/3742728.3742733), which searches compressed logs on object storage, uses LogGrep inside its indexing step and takes LogGrep and OpenSearch UltraWarm as its baselines.

---

#### Threat Intelligence Quality Dimensions for Research and Practice (Zibak, Sauerwein & Simpson, ACM DTRAP 2022)

**Authors**: Adam Zibak, Clemens Sauerwein, Andrew C. Simpson
**Date**: 2022 (Digital Threats: Research and Practice 3(4), pp. 1-22; published March 10, 2022)
**URL**: https://doi.org/10.1145/3484202
**DOI**: 10.1145/3484202
**Evidence Level**: A (peer-reviewed journal, ACM DTRAP)
**Relevance**:
- Handbook ch03 §3.1: the closest peer-reviewed application of data-quality dimensions to security data, beside the DAMA-DMBOK2 framework (B) the chapter leans on.
- Scope limit: threat intelligence, not telemetry; the handbook does not claim their dimension list matches its six.

**Key Findings** (abstract): data quality is one of the most common barriers to effective threat-intelligence sharing and research and practice lack a common understanding of expected quality; a systematic literature review followed by a modified Delphi study with 30 threat-intelligence experts in Europe produced a set of threat-intelligence quality dimensions and revised definitions of threat data, information and intelligence.
**Citations**: Zibak, A., Sauerwein, C., & Simpson, A.C. (2022). Threat Intelligence Quality Dimensions for Research and Practice. *Digital Threats: Research and Practice*, 3(4), 1-22.
**Notes**: Flash gave the year as 2021; Crossref gives 2022.
**Validation Status**: ✅ Verified 2026-11-07 (Crossref record: title, three authors, journal, volume 3, issue 4, pages 1-22, 2022-03-10, and the abstract text).
**Refresh (2026-11-23)**: Crossref record and abstract re-read; journal, volume 3(4), pages and the 30-expert Delphi finding are unchanged. A Crossref author query found no later quality-dimension paper by the same authors (their adjacent 2021 work is a success model for CTI management platforms, *Computers & Security*, doi:10.1016/j.cose.2021.102466). Still the closest peer-reviewed source held for the ch03 use.

---

#### SoK: History is a Vast Early Warning System: Auditing the Provenance of System Intrusions (Inam et al., IEEE S&P 2023)

**Authors**: Muhammad Adil Inam, Yinfang Chen, Akul Goyal, Jason Liu, Jaron Mink, Noor Michael, Sneha Gaur, Adam Bates, Wajih Ul Hassan
**Date**: May 2023 (2023 IEEE Symposium on Security and Privacy, pp. 2620-2638)
**URL**: https://doi.org/10.1109/SP46215.2023.10179405
**DOI**: 10.1109/SP46215.2023.10179405
**Evidence Level**: A (peer-reviewed, IEEE S&P 2023)
**Relevance**:
- Handbook ch04 §4.2 (context collapse under field coarsening): an independent, peer-reviewed measurement that lossy reduction of security telemetry costs detection, in provenance audit logs rather than OCSF.

**Key Findings** (abstract): surveys provenance-based system auditing in a layered taxonomy, then independently evaluates 8 exemplar log-reduction techniques against the DARPA Transparent Computing datasets; past approaches frequently prune an overlapping set of activities, there is "an inverse relation between storage efficiency and anomaly detection performance", and reduction combined with compression could cut log retention costs by multiple orders of magnitude.
**Citations**: Inam, M.A., Chen, Y., Goyal, A., Liu, J., Mink, J., Michael, N., Gaur, S., Bates, A., & Hassan, W.U. (2023). SoK: History is a Vast Early Warning System: Auditing the Provenance of System Intrusions. *2023 IEEE Symposium on Security and Privacy (SP)*, 2620-2638.
**Notes**: Flash described this paper as showing detection invariant to reduction, which reverses the abstract; the abstract supports the handbook's direction. The retention-cost finding is carried in the handbook footnote as the other side of the trade.
**Validation Status**: ✅ Verified 2026-11-07 (Crossref record: title, nine authors, IEEE S&P 2023 event, pages, DOI; full abstract read at the OpenAlex record).
**Refresh (2026-11-23)**: Crossref and OpenAlex records re-read; the eight-technique evaluation, the "inverse relation between storage efficiency and anomaly detection performance" and the retention-cost finding are verbatim. This SoK has no newer edition and no successor SoK was found; Hassan's group continues the audit-logging line (for example "Rethinking Tamper-Evident Logging" at ACM CCS 2025, doi:10.1145/3719027.3765024), and those later papers were checked at the metadata level only. Still accurate.

---

#### On the Forensic Validity of Approximated Audit Logs (Michael et al., ACSAC 2020)

**Authors**: Noor Michael, Jaron Mink, Jason Liu, Sneha Gaur, Wajih Ul Hassan, Adam Bates (University of Illinois Urbana-Champaign)
**Date**: December 2020 (Annual Computer Security Applications Conference, ACSAC '20, pp. 189-202)
**URL**: https://doi.org/10.1145/3427228.3427272
**Alt URL**: https://www.acsac.org/2020/program/final/s238.html
**DOI**: 10.1145/3427228.3427272
**Evidence Level**: A (peer-reviewed, ACSAC 2020)
**Relevance**:
- Handbook ch04 §4.2: supports and bounds the context-collapse claim; how much forensic evidence survives a reduction depends on what the reduction keeps.

**Key Findings** (abstract): formalizes metrics for the forensic validity of approximated audit logs; LogApprox aggressively approximates benign file I/O while preserving anomalous events losslessly, and retains 100% of attack-associated log events at reduction rates comparable to prior techniques, which "retain as little as 7.3% of forensic evidence in certain attack scenarios".
**Citations**: Michael, N., Mink, J., Liu, J., Gaur, S., Hassan, W.U., & Bates, A. (2020). On the Forensic Validity of Approximated Audit Logs. *Annual Computer Security Applications Conference (ACSAC '20)*, 189-202.
**Notes**: Flash read this as "80-90% can be discarded harmlessly", which reverses the abstract.
**Validation Status**: ✅ Verified 2026-11-07 (Crossref record: title, six authors, ACSAC '20 event, pages, DOI; full abstract and affiliations read on the ACSAC 2020 program page).
**Refresh (2026-11-23)**: ACSAC program page re-read (the bare acsac.org host now redirects to www.acsac.org, Alt URL updated); the 100% attack-event retention and the "as little as 7.3% of forensic evidence" finding are verbatim. The 2023 SoK (Inam et al., entry above), which shares all six of this paper's authors, re-evaluates eight reduction techniques and reports an inverse relation between storage efficiency and anomaly detection, so it agrees in direction but is same-group corroboration, not an independent replication. Still accurate.

---

#### SPA: Economical and Workload-Driven Indexing for Data Analytics in the Cloud (Boncz et al., IEEE ICDE 2023)

**Authors**: Peter Boncz, Yannis Chronis, Jan Finis, Stefan Halfpap, Viktor Leis, Thomas Neumann, Anisoara Nica, Caetano Sauer, Knut Stolze, Marcin Żukowski (publisher order, alphabetical)
**Date**: April 2023 (2023 IEEE 39th International Conference on Data Engineering, pp. 3740-3746)
**URL**: https://doi.org/10.1109/ICDE55515.2023.00302
**DOI**: 10.1109/ICDE55515.2023.00302
**Evidence Level**: A (peer-reviewed, IEEE ICDE 2023; short vision paper)
**Relevance**:
- Handbook ch05 §5.3a: a peer-reviewed statement of the point-lookup weakness of lakes, cited alongside the Kumar LinkedIn post (C) the section already carried.

**Key Findings** (abstract): because of their size, expensive maintenance and difficulty to tune and automate, secondary indexes "are typically not used in modern cloud data warehouses or data lakes", which rely on full scans and min/max filtering whose effectiveness depends on data layout and value distributions; proposes SPA as the vision for adaptive, workload-driven partial indexing of immutable copy-on-write formats, usable as an accelerator over cloud data lakes.
**Citations**: Boncz, P., Chronis, Y., Finis, J., Halfpap, S., Leis, V., Neumann, T., Nica, A., Sauer, C., Stolze, K., & Żukowski, M. (2023). SPA: Economical and Workload-Driven Indexing for Data Analytics in the Cloud. *2023 IEEE 39th International Conference on Data Engineering (ICDE)*, 3740-3746.
**Notes**: A vision paper: the problem statement is the evidence the handbook uses; the proposed design carries no benchmark in the abstract. The scout file listed the authors as "Chronis, Finis, Halfpap, Boncz et al."; Crossref and OpenAlex both give the alphabetical order above.
**Validation Status**: ✅ Verified 2026-11-07 (Crossref record: title, ten authors, ICDE 2023 event, pages, DOI; full abstract and author order read at the OpenAlex record). Refresh (2026-11-23): DOI still resolves to IEEE Xplore document 10184818; abstract re-read at OpenAlex, the quoted sentence unchanged, no retraction. A narrow OpenAlex search found no follow-up by the same authors, which does not show that none exists.

---

#### Do Data Scientists Spend 80% of Their Time Cleaning Data? Turns Out, No? (Dodds, blog 2020)

**Author**: Leigh Dodds
**Date**: January 31, 2020 (updated September 29, 2020)
**URL**: https://blog.ldodds.com/2020/01/31/do-data-scientists-spend-80-of-their-time-cleaning-data-turns-out-no/
**Evidence Level**: C (personal blog; a secondary tally of vendor and platform surveys, each self-reported)
**Relevance**:
- Handbook ch01 §1.1: the low end (about 26%) of the softened data-preparation range that replaces the bare "80%" figure; the high end is Anaconda's 2020 survey (45%), already cited in the same footnote.

**Key Findings**: traces the 80% figure to CrowdFlower 2016 (cleaning and organizing 60%, collecting data sets 19%); CrowdFlower 2017 reports 51% for collecting, labelling, cleaning and organizing combined; Kaggle 2018 reports about 11% gathering and 15% cleaning.
**Citations**: Dodds, L. (2020, January 31; updated 2020, September 29). *Do data scientists spend 80% of their time cleaning data? Turns out, no?* Blog post.
**Notes**: The Kaggle 2018 figures are read through this tally, not at Kaggle, and the handbook footnote says so.
**Validation Status**: ✅ Verified 2026-11-07 (post fetched: title, author, dates and the three survey figures quoted above). Refresh (2026-11-23): post re-fetched live; the three survey figures and the September 29, 2020 update date unchanged.

---

#### How Do Committees Invent? (Conway, Datamation 1968)

**Author**: Melvin E. Conway
**Date**: April 1968 (*Datamation* 14(4), pp. 28-31)
**URL**: https://www.melconway.com/Home/Committees_Paper.html
**Evidence Level**: C (computer-industry trade magazine article, not peer-reviewed; widely cited, but below the Level-A bar by venue)
**Relevance**:
- Handbook ch07 (story time): the origin of Conway's law, applied to a parallel-SIEM build that copied its two owning teams; also the point Stojkovski applies to SIEM deployments, cited in ch01 via Chuvakin.

**Key Findings**: the paper's conclusion states that "organizations which design systems (in the broad sense used here) are constrained to produce designs which are copies of the communication structures of these organizations."
**Citations**: Conway, M.E. (1968). How Do Committees Invent? *Datamation*, 14(4), 28-31.
**Notes**: The author's reprint opens with a note written 42 years after publication restating the thesis informally. The handbook footnote labels it Tier C, matching this entry (the claim-evidence matrix had flagged an earlier Tier A label).
**Validation Status**: ✅ Verified 2026-11-07 (author's reprint fetched: title, author's note, the conclusion sentence quoted above, and the reprint notice "Copyright 1968, F. D. Thompson Publications, Inc. Reprinted by permission of Datamation magazine, where it appeared April, 1968"; volume, issue and pages confirmed later the same day at the scanned April 1968 issue on bitsavers.org (`magazines/Datamation/196804.pdf`): the masthead reads "april 1968, volume 14, number 4", the contents list the article at page 28 with the next article at page 32, and the article's printed folios run 28 to 31. The Crossref reference lists of Nagappan et al. (ICSE 2008, doi:10.1145/1368088.1368160) give 14(4), pp. 28-31, while MacCormack et al. (Research Policy 2012, doi:10.1016/j.respol.2012.04.011) give issue 5, which the scan contradicts). Refresh (2026-11-23): author reprint re-fetched live, the conclusion sentence unchanged; tier stays C by venue.

---

#### Sigma Rules Specification (SigmaHQ, sigma-specification v2.1.0)

**Author**: SigmaHQ project (Sigma originated with Florian Roth and Thomas Patzke)
**Date**: Sigma Rules Specification version 2.1.0, release date 2025-08-02 (repository release v2.1.0 published 2025-09-12)
**URL**: https://github.com/SigmaHQ/sigma-specification
**Evidence Level**: B (community specification maintained by an open-source project, not a formal standards body)
**Relevance**:
- Handbook ch04 §4.3 and the `sigma` footnote: Sigma as an open YAML detection format that compiles through pySigma to many backends, and the SigmaHQ public ruleset the lab's context-collapse benchmark ran unmodified.

**Key Findings**: the repository publishes the Sigma Rules, Correlation Rules and Filters specifications, appendices for modifiers, tags and taxonomy, and JSON schemas for each rule type; the SigmaHQ rule and filename conventions in the same repository are marked as not part of the specification. The specification is released into the public domain per the repository LICENSE.
**Citations**: SigmaHQ. (2025). *Sigma Rules Specification* (Version 2.1.0). https://github.com/SigmaHQ/sigma-specification
**Notes**: Tier B on the specification as a definition of the format; it carries no claim about detection efficacy. The Roth and Patzke attribution is carried from the handbook footnote and was not re-checked against a SigmaHQ page this pass. The handbook's backend count ("roughly thirty other backends") is a pySigma plugin count, not a specification claim.
**Validation Status**: ✅ Verified 2026-11-07 (GitHub API: repository description, README, `specification/` listing, sigma-rules-specification.md header for version and release date, latest release tag v2.1.0, LICENSE).

---

## Handbook Chapter 1 Survey Companions (2026-11-07)

Added 2026-11-07 because the handbook's ch01 `[^wrangle]` footnote already cited both of these surveys for the softened data-preparation range and neither had a bibliography entry. Both are vendor-run, self-reported practitioner surveys, so both sit at Tier C with the bias flagged, and both were re-read at the primary named in their Validation Status lines rather than carried from the footnote.

---

#### The State of Data Science 2020: Moving from Hype Toward Maturity (Anaconda, vendor survey 2020)

**Author**: Anaconda, Inc.
**Date**: 2020 (survey fielded February 12 to April 20, 2020; the landing page states no release date; the report PDF's metadata gives a creation date of July 23, 2020, and a GlobeNewswire release URL is dated June 30, 2020, though that page returned HTTP 403 and was not read)
**URL**: https://www.anaconda.com/resources/whitepaper/state-of-data-science-2020
**Alt URL**: https://know.anaconda.com/rs/387-XNW-688/images/Anaconda-SODS-Report-2020-Final.pdf
**Evidence Level**: C (vendor-run online survey; self-reported time shares)
**Relevance**:
- Handbook ch01 §1.1 (`[^wrangle]`): the high end (45%) of the softened data-preparation range that replaces the bare "80%" figure; the low end is the Dodds tally (about 26%), cited in the same footnote.

**Key Findings**: 2,360 people from more than 100 countries took the online survey; respondents "reported that almost half of their time is spent on the combined tasks of data loading and cleansing", which the landing page states as "on average 45% of their time is spent getting data ready (loading and cleansing)". The time-allocation question that produces the figure has n=1,099 in the report's chart, which gives the two tasks as 19% and 26%, with data visualization about 21% and the three modeling tasks 11–12% each.
**Citations**: Anaconda. (2020). *The State of Data Science 2020: Moving from Hype Toward Maturity*. Anaconda, Inc.
**Notes**: Bias flag: Anaconda sells data-science tooling, and respondents were recruited via social media and Anaconda's own email database, so the sample leans toward its user base. The 45% comes from the 1,099 respondents who answered the time-allocation question, not all 2,360; the handbook footnote attributed it to the full sample until the 2026-11-07 fix, and now names the 1,099 and the 19% plus 26% split. Later editions exist (2022, 3,493 respondents from 133 countries and regions; 2024, described by Anaconda as its 7th annual report); neither landing page states a data-preparation time share, so no later figure is carried.
**Validation Status**: ✅ Verified 2026-11-07 (landing page fetched: title, 2,360 responses, 45% loading and cleansing; report PDF fetched: field dates, recruitment, the time-allocation chart with n=1,099, and the "almost half" sentence quoted above). Refresh (2026-11-23): landing page and report PDF both return 200; the 45% sentence and the 2,360 count re-read on the landing page, and the almost-half sentence and the n=1,099 chart with the 19% and 26% split re-read in the PDF, all unchanged.

---

#### Cleaning Big Data: Most Time-Consuming, Least Enjoyable Data Science Task, Survey Says (Press, Forbes 2016, reporting CrowdFlower)

**Author**: Gil Press (Forbes contributor)
**Date**: March 23, 2016
**URL**: https://www.forbes.com/sites/gilpress/2016/03/23/data-preparation-most-time-consuming-least-enjoyable-data-science-task-survey-says/
**Alt URL**: http://web.archive.org/web/20160406121440/http://www.forbes.com:80/sites/gilpress/2016/03/23/data-preparation-most-time-consuming-least-enjoyable-data-science-task-survey-says/
**Evidence Level**: C (press report of a vendor-run survey)
**Relevance**:
- Handbook ch01 §1.1 (`[^wrangle]`): the most direct trace of the folk "80%" figure to the CrowdFlower 2016 Data Science Report.

**Key Findings**: reports CrowdFlower's survey of "about 80 data scientists", conducted for the second year in a row: "Data scientists spend 60% of their time on cleaning and organizing data. Collecting data sets comes second at 19% of their time, meaning data scientists spend around 80% of their time on preparing and managing data for analysis." The same piece reports that 76% of respondents view data preparation as the least enjoyable part of the work.
**Citations**: Press, G. (2016, March 23). Cleaning Big Data: Most Time-Consuming, Least Enjoyable Data Science Task, Survey Says. *Forbes*.
**Notes**: Bias flag: CrowdFlower sold a "data enrichment" platform for data scientists, so the vendor running the survey benefits from the finding, and the sample is small (about 80). The page title is "Cleaning Big Data: …" while the URL slug reads "data-preparation-…". Until the 2026-11-07 fix the handbook footnote used the slug wording as the title and described the figures as shares of respondents naming a task; it now carries the page title and gives them as shares of time from about 80 data scientists.
**Validation Status**: ✅ Verified 2026-11-07 (live forbes.com returned HTTP 403; the Wayback snapshot of 2016-04-06 was read: og:title, author meta "Gil Press", publication timestamp 2016-03-23T13:17:00-04:00, and the passage quoted above). Refresh (2026-11-23): forbes.com returned 403 again; the Wayback snapshot of 2016-04-06 re-read, with the title, the 60/19/80 passage, the about-80 sample and the 76% unchanged.

---

---
## Handbook Footnote Legs, Third Pass (2026-11-07)

Added 2026-11-07 when the owner approved a second set of handbook footnotes drawn from a thin-claims scouting pass (Gemini Flash). Seven peer-reviewed papers carry the outside leg for a mechanism or kind of claim the book previously stated on first-hand evidence, and none of them supplies the book's own percentages, which the footnotes say. One vendor release carries a bound on ch07's dead-rule tail. Flash's raw answers are Tier C and were not carried; every entry below was re-read at Crossref and its abstract (OpenAlex) or the vendor's own release, and Flash's sample sizes were replaced with the abstracts' (Wixom & Watson 111 organizations, not 454; Khadka 26 interviews plus 198 survey respondents, not 310).

---

#### "Everyone wants to do the model work, not the data work": Data Cascades in High-Stakes AI (Sambasivan et al., CHI 2021)

**Authors**: Nithya Sambasivan, Shivani Kapania, Hannah Highfill, Diana Akrong, Praveen Paritosh, Lora M Aroyo
**Date**: May 2021 (Proceedings of the 2021 CHI Conference on Human Factors in Computing Systems, pp. 1-15)
**URL**: https://doi.org/10.1145/3411764.3445518
**DOI**: 10.1145/3411764.3445518
**Evidence Level**: A (peer-reviewed, ACM CHI 2021)
**Relevance**:
- Handbook ch01 §1.1 (`[^sambasivan-ch1]`): supports the claim that data work decides AI outcomes, beside the softened data-preparation range in `[^wrangle]`.
- Scope limit: gives no time share; the handbook footnote says so.

**Key Findings** (abstract): interviews with 53 AI practitioners in India, East and West African countries, and the USA; defines data cascades as compounding events causing negative downstream effects from data issues, triggered by practices that undervalue data quality, and finds them pervasive (92% prevalence), invisible, delayed, but often avoidable; describes data as "the most under-valued and de-glamorised aspect of AI."
**Citations**: Sambasivan, N., Kapania, S., Highfill, H., Akrong, D., Paritosh, P., & Aroyo, L.M. (2021). "Everyone wants to do the model work, not the data work": Data Cascades in High-Stakes AI. *Proceedings of the 2021 CHI Conference on Human Factors in Computing Systems*, 1-15.
**Notes**: High-stakes AI domains (health, conservation, lending), not security; the transfer to security AI is the handbook author's.
**Validation Status**: ✅ Verified 2026-11-07 (Crossref record: title, six authors, CHI 2021 proceedings, pages, DOI; full abstract read at the OpenAlex record). Refresh (2026-11-23): DOI resolves to the ACM Digital Library (bot-blocked to curl); abstract re-read at OpenAlex, 53 interviews and 92% prevalence unchanged, no retraction.

---

#### An Empirical Investigation of the Factors Affecting Data Warehousing Success (Wixom & Watson, MIS Quarterly 2001)

**Authors**: Barbara H. Wixom, Hugh J. Watson
**Date**: March 2001 (MIS Quarterly 25(1), pp. 17-42)
**URL**: https://doi.org/10.2307/3250957
**DOI**: 10.2307/3250957
**Evidence Level**: A (peer-reviewed journal, MIS Quarterly)
**Relevance**:
- Handbook ch07 (`[^orgwork-ch7]`): supports the kind of claim that much of a data-platform effort is organizational, in the closest information-systems analogue to a SIEM migration.
- Scope limit: no split of effort between organizational and technical work; the body's more-than-half figure stays the author's estimate.

**Key Findings** (abstract): a cross-sectional survey of data-warehousing managers and data suppliers from 111 organizations (paired mail questionnaires), analysed with Partial Least Squares; management support and resources help address organizational issues during warehouse implementations; resources, user participation, and highly skilled project team members raise the likelihood of on-time, on-budget delivery; diverse, unstandardized source systems and poor development technology increase technical issues; success with organizational and project issues in turn influences system quality.
**Citations**: Wixom, B.H., & Watson, H.J. (2001). An Empirical Investigation of the Factors Affecting Data Warehousing Success. *MIS Quarterly*, 25(1), 17-42.
**Notes**: Flash gave the sample as 454 projects; the abstract gives 111 organizations. Crossref appends a footnote marker ("Success1") to the title, dropped here.
**Validation Status**: ✅ Verified 2026-11-07 (Crossref record: title, two authors, journal, volume 25, issue 1, pages 17-42, DOI; full abstract read at the OpenAlex record). Refresh (2026-11-23): DOI resolves to the article page at misq.umn.edu (bot-blocked to curl, not read); abstract re-read at OpenAlex, 111 organizations unchanged.

---

#### How Do Professionals Perceive Legacy Systems and Software Modernization? (Khadka et al., ICSE 2014)

**Authors**: Ravi Khadka, Belfrit V. Batlajery, Amir M. Saeidi, Slinger Jansen, Jurriaan Hage
**Date**: May 2014 (Proceedings of the 36th International Conference on Software Engineering, pp. 36-47)
**URL**: https://doi.org/10.1145/2568225.2568318
**DOI**: 10.1145/2568225.2568318
**Evidence Level**: A (peer-reviewed, ICSE 2014)
**Relevance**:
- Handbook ch07 (`[^orgwork-ch7]`): second leg, with Wixom & Watson, for the kind of claim that modernization difficulty is organizational as well as technical.
- Scope limit: no effort share.

**Key Findings** (abstract): an exploratory study interviewing 26 industrial practitioners on what makes a system legacy, what drives modernization, and what challenges arise, validated by a survey with 198 respondents; practitioners value their legacy systems highly, and the challenges "are not just technical, but also include business and organizational aspects."
**Citations**: Khadka, R., Batlajery, B.V., Saeidi, A.M., Jansen, S., & Hage, J. (2014). How do professionals perceive legacy systems and software modernization? *Proceedings of the 36th International Conference on Software Engineering (ICSE 2014)*, 36-47.
**Notes**: Flash gave a wrong DOI (it resolves to an unrelated ICSE 2014 paper), a sample of 310, and read the paper as contradicting the claim; the abstract supports it.
**Validation Status**: ✅ Verified 2026-11-07 (Crossref record: title, five authors, ICSE 2014 proceedings, pages, DOI; full abstract read at the OpenAlex record). Refresh (2026-11-23): DOI resolves to the ACM Digital Library (bot-blocked to curl); abstract re-read at OpenAlex, the 26 interviews, the 198 respondents and the quoted sentence unchanged.

---

#### A Brief Study of Time (Buchholz & Tjaden, Digital Investigation 2007)

**Authors**: Florian Buchholz, Brett Tjaden
**Date**: September 2007 (Digital Investigation 4, Supplement, pp. 31-42; DFRWS 2007)
**URL**: https://doi.org/10.1016/j.diin.2007.06.004
**DOI**: 10.1016/j.diin.2007.06.004
**Evidence Level**: A (peer-reviewed journal, Digital Investigation)
**Relevance**:
- Handbook ch04 §4.2 (`[^clock-ch4]`): measured evidence that host clocks are often wrong, the second way a stored time lies beside a dropped offset.
- Scope limit: clock correctness, not offset loss; supports the mechanism, not the lab's recall figures.

**Key Findings** (abstract): the first large-scale, long-term study of how Internet hosts manage their clocks, motivated by forensic correlation of events from disparate sources; over 8,000 web servers sampled regularly for more than six months; only about 74% were within 10 seconds of UTC, and the rest showed a wide variety of clock behaviours.
**Citations**: Buchholz, F., & Tjaden, B. (2007). A brief study of time. *Digital Investigation*, 4, 31-42.
**Notes**: A 2007 sample of web servers, so the 74% is historical; the handbook uses it for the mechanism only.
**Validation Status**: ✅ Verified 2026-11-07 (Crossref record: title, two authors, journal, volume 4, pages 31-42, DOI; full abstract read at the OpenAlex record). Refresh (2026-11-23): DOI resolves; abstract re-read at OpenAlex, the 74% within 10 s unchanged. A limited search found no newer large-scale prevalence study, so the figure stays historical and mechanism-only.

---

#### Was the Clock Correct? Exploring Timestamp Interpretation through Time Anchors for Digital Forensic Event Reconstruction (Vanini et al., FSI: Digital Investigation 2024)

**Authors**: Céline Vanini, Christopher J. Hargreaves, Harm van Beek, Frank Breitinger
**Date**: July 2024 (Forensic Science International: Digital Investigation 49, article 301759)
**URL**: https://doi.org/10.1016/j.fsidi.2024.301759
**DOI**: 10.1016/j.fsidi.2024.301759
**Evidence Level**: A (peer-reviewed journal, FSI: Digital Investigation)
**Relevance**:
- Handbook ch04 §4.2 (`[^clock-ch4]`): when system time is skewed, recorded timestamps do not reflect when events happened, which is the reconstruction problem the chapter's correlation argument rests on.

**Key Findings** (abstract): timestamps derive from a system clock, so skew from tampering, natural drift, or malfunction makes recorded times diverge from when events occurred; defines time anchors, anchoring and non-anchoring events, and time anomalies to test whether the system time was correct, illustrated with a Google search and a file creation in correct and skewed versions.
**Citations**: Vanini, C., Hargreaves, C.J., van Beek, H., & Breitinger, F. (2024). Was the clock correct? Exploring timestamp interpretation through time anchors for digital forensic event reconstruction. *Forensic Science International: Digital Investigation*, 49, 301759.
**Notes**: Worked examples, no prevalence or recall figure. Follow-ups by the same group, neither read in full: Breitinger, Studiawan and Hargreaves, SoK: Timeline based event reconstruction for digital forensics (Forensic Science International: Digital Investigation 53, 301932, July 2025, doi:10.1016/j.fsidi.2025.301932; preprint arXiv 2504.18131), and Vanini, Gruber, Hargreaves, Benenson, Freiling and Breitinger, Understanding Strategies and Challenges of Timestamp Tampering for Improved Digital Forensic Event Reconstruction (Digital Forensics Doctoral Symposium, April 2025, doi:10.1145/3712716.3712727).
**Validation Status**: ✅ Verified 2026-11-07 (Crossref record: title, four authors, journal, volume 49, article 301759, DOI; full abstract read at the OpenAlex record). Refresh (2026-11-23): DOI resolves; abstract re-read at OpenAlex, unchanged; the two follow-up records confirmed at Crossref.

---

#### Troubleshooting an Intrusion Detection Dataset: the CICIDS2017 Case Study (Engelen, Rimmer & Joosen, IEEE SPW 2021)

**Authors**: Gints Engelen, Vera Rimmer, Wouter Joosen
**Date**: May 2021 (2021 IEEE Security and Privacy Workshops, SPW, pp. 7-12)
**URL**: https://doi.org/10.1109/SPW53761.2021.00009
**DOI**: 10.1109/SPW53761.2021.00009
**Evidence Level**: A (peer-reviewed workshop, IEEE S&P Workshops)
**Relevance**:
- Handbook ch03 (`[^dqbound-ch3]`): the closest peer-reviewed analogue to a "share silently wrong" figure, beside the author's first-hand roughly 30%.
- Scope limit: a research dataset, not a production pipeline.

**Key Findings** (abstract): revisits CICIDS2017 and its data collection pipeline and finds problems with traffic generation, flow construction, feature extraction and labelling that severely affect correctness, validity and utility; an improved processing methodology reconstructs or relabels more than 20 percent of the original traffic traces, and ML benchmarks on the corrected dataset improve significantly.
**Citations**: Engelen, G., Rimmer, V., & Joosen, W. (2021). Troubleshooting an Intrusion Detection Dataset: the CICIDS2017 Case Study. *2021 IEEE Security and Privacy Workshops (SPW)*, 7-12.
**Notes**: Workshop paper (WTMC at IEEE S&P); tiered A as refereed. A separate group reports further flaws in the same dataset: Lanvin et al., Errors in the CICIDS2017 Dataset and the Significant Differences in Detection Performances It Makes (CRiSIS 2022, LNCS 13857, 2023, pp. 18-33, doi:10.1007/978-3-031-31108-6_2), whose abstract names packet misorder, packet duplication and attacks performed but not correctly labelled; read at abstract level only, and a candidate for its own entry.
**Validation Status**: ✅ Verified 2026-11-07 (Crossref record: title, three authors, SPW 2021 proceedings, pages 7-12, DOI; full abstract read at the OpenAlex record). Refresh (2026-11-23): DOI resolves to IEEE Xplore document 9474286; abstract re-read at OpenAlex, the more-than-20-percent figure unchanged.

---

#### Impact of Log Parsing on Deep Learning-Based Anomaly Detection (Khan, Shin, Bianculli & Briand, Empirical Software Engineering 2024)

**Authors**: Zanis Ali Khan, Donghwan Shin, Domenico Bianculli, Lionel C. Briand
**Date**: August 2024 (Empirical Software Engineering 29(6), article 139)
**URL**: https://doi.org/10.1007/s10664-024-10533-w
**DOI**: 10.1007/s10664-024-10533-w
**Evidence Level**: A (peer-reviewed journal, Empirical Software Engineering)
**Relevance**:
- Handbook ch03 (`[^dqbound-ch3]`): bounds "unusable"; badly parsed data is not always fatal to a given downstream task.
- Scope limit: software-system logs, not security telemetry.

**Key Findings** (abstract): an empirical study of 13 log parsing techniques and seven anomaly detection techniques (five deep-learning, two traditional machine learning) on three public log datasets; "there is no strong correlation between log parsing accuracy and anomaly detection accuracy, regardless of the metric used for measuring log parsing accuracy," and a property the authors call distinguishability in parsing results, rather than their accuracy, plays the essential role.
**Citations**: Khan, Z.A., Shin, D., Bianculli, D., & Briand, L.C. (2024). Impact of log parsing on deep learning-based anomaly detection. *Empirical Software Engineering*, 29(6), 139.
**Notes**: The scout file described the detectors as "7 detectors"; the abstract's five plus two split is carried here and in the handbook.
**Validation Status**: ✅ Verified 2026-11-07 (Crossref record: title, four authors, journal, volume 29, issue 6, article 139, DOI; full abstract read at the OpenAlex record).
**Refresh (2026-11-23)**: DOI re-resolved (HTTP 200 at link.springer.com); the article is open access under CC BY 4.0 per its Crossref licence record, and the arXiv preprint 2305.15897 (v4, 2024-08-19) carries the journal reference "Empir Software Eng 29, 139 (2024)". The OpenAlex abstract was re-read and the 13-parser, five-plus-two-detector, three-dataset design and the no-strong-correlation sentence are unchanged. No newer edition or follow-up by the same authors was found in this pass. The LLM-based log parsing work since 2024, for example Beck et al., "System Log Parsing with Large Language Models: A Review" (arXiv 2504.04877, v2 of 2025-05-15, first posted as "SoK: LLM-based Log Parsing"), reviews 29 parsers and benchmarks seven of them on public datasets per its abstract, which does not mention a downstream anomaly-detection measurement, so on the abstract alone it neither corroborates nor contradicts this finding.

---

#### Fourth Annual Report on the State of SIEM Detection Risk (CardinalOps, press release 2024)

**Author**: CardinalOps
**Date**: June 13, 2024
**URL**: https://prnewswire.com/news-releases/enterprise-siems-cover-only-19-of-mitre-attck-techniques-used-by-adversaries-302171478.html
**Evidence Level**: C (vendor report announced by the vendor's own release; bias flagged: CardinalOps sells detection-posture tooling, so a high broken-rule share suits its pitch)
**Relevance**:
- Handbook ch07 §7.3 (`[^cardinalops-ch7]`): a production measurement of the broken slice of a SIEM rule set, used as a bound on the body's "often around half" dead tail rather than as confirmation.

**Key Findings**: across "more than 3,000 detection rules, 1.2 million log sources and hundreds of unique log source types" in customer SIEMs, "18% of SIEM rules will never fire due to a common issue like misconfigured data sources and missing fields."
**Citations**: CardinalOps. (2024, June 13). *Fourth Annual Report on the State of SIEM Detection Risk* [Press release]. PR Newswire.
**Notes**: The release, not the gated report PDF, was read. Other editions (about 15% in 2022, about 12% in 2023) appear in press coverage and were not read at a CardinalOps primary; the 2022 report PDF mirror returned HTTP 403. The 2025 edition was read at its primaries on 2026-11-23 (see the refresh line). "Never fire" is narrower than the handbook's dead tail, which also counts noisy rules analysts ignore. The scout file's note that cardinalops.com redirects to cribl.io was checked on 2026-11-23 and holds (see the refresh line).
**Validation Status**: ✅ Verified 2026-11-07 (PR Newswire release fetched: date, "Fourth Annual" title line, dataset sentence and the 18% sentence quoted above).
**Refresh (2026-11-23)**: The cardinalops.com home page and its blog both redirect to cribl.io. Cribl announced on 2026-07-14 that it "is acquiring CardinalOps, an Agentic Detection Engineering solution" (https://cribl.io/news/cribl-acquires-cardinalops-to-expand-its-ai-platform-into-security-operations/), so the publisher of this series now sits inside a telemetry-pipeline vendor, which the bias flag above should be read to include. The fifth edition (2025) was read at two CardinalOps primaries, and they give different figures for the year. The release of 2025-06-05 (https://www.prnewswire.com/news-releases/enterprise-siems-miss-79-of-mitre-attck-techniques-used-by-adversaries-according-to-cardinalops-5th-annual-report-302473779.html) gives "13% on average" of rules as "non-functional and will never trigger" and coverage of "just 21% of adversary techniques", and compares both with 2024 as year-on-year changes ("a five percent decrease from 2024"). The report itself, now off cardinalops.com and read from a Wayback copy (https://web.archive.org/web/20250714230723/https://cardinalops.com/wp-content/uploads/2025/06/25-CardinalOps-2025-State-of-SIEM-Report.pdf), shows 21% and 13% on a summary page headed "Based on aggregate analysis of all five years of our sample data", and gives this year's figures in the body as 22% coverage and "This year's 10% finding" for broken rules, over "Over 13,000 unique detection rules" and "Nearly 2.5 million total log sources", while noting that "year to year variations could be attributed to sampling differences". How far that summary-page heading reaches is unclear, because the same page carries the 259 log types that the body treats as a 2025 value and the body puts the historical coverage benchmark at 20%, so the safest reading is that the release's 13% and 21% are the summary-page figures and the body's 10% and 22% are the single-year ones. The same report confirms the 2024 value cited here ("a slight regression back to 18% last year"), so the 18% stands, and across the two latest editions the vendor's own never-fire share sits between 10% and 18%. The report's retrospective ("steady improvements from 25% to 15% across the first few years") does not mention the roughly 12% that press coverage gives for 2023, which stays unread at a primary. Help Net Security's write-up (2025-06-09, https://www.helpnetsecurity.com/2025/06/09/siem-detection-coverage/) repeats the release's 13% and 79%.

## Agent Harness Benchmarking (2026-11-08)

Added 2026-11-08 at the owner's request, as outside method references for the lab's own benchmark methodology ([BENCHMARKING-METHODOLOGY.md](https://github.com/flying-coyote/sdw-lab-benchmarks/blob/master/BENCHMARKING-METHODOLOGY.md)) and for the agent trust-boundary material. Both are live Hugging Face Spaces that change between versions, so each entry pins the version, commit and date read. The headline numbers were re-read from the board's own JSON (`/api/index`, generated 2026-11-08T17:39:25Z, board v0.1.1), not from the LinkedIn post that announced it.

---

#### Harness Leaderboard: Which coding-agent harness should you run your open model in? (Niklaus, Hugging Face Space, v0.1.1, 2026)

**Authors**: Joel Niklaus (Space owner, `joelniklaus`)
**Date**: v0.1.0 released 2026-11-05; v0.1.1 2026-11-06; read 2026-11-08 (Space commit fb3c971)
**URL**: https://huggingface.co/spaces/joelniklaus/harness-leaderboard
**Evidence Level**: B (independent practitioner measurement with a published method, a public lab notebook, and every scored trajectory in a public bucket; not peer-reviewed, and the owner's affiliation was not checked)
**Relevance**:
- Lab methodology: a worked example of controlled-variable benchmarking where only one factor changes (the harness), with model, provider and reasoning effort pinned and enforced by a metering proxy, three attempts per task, 95% confidence intervals, a paired bootstrap test that marks harnesses tied with the leader, and a re-run flip rate that separates harness effect from run-to-run noise.
- Reliability reporting: per harness, the share of tasks solved on all three attempts beside the share solved on at least one, which is the unattended-operation question rather than the best-case one.
- Benchmark integrity: cheating (looking up published solutions, fetching the upstream code a task was cut from, special-casing the grader) is scored as a fail by the board's own rule, enforced with atif-scan plus a human read of every flagged pass; the lab notebook records 414 proposed confirmed answer-key lookups and the corrections that followed.
- Agent trust boundary: agents could read the meter's record and write `/etc/hosts` but did not get past Landlock; offline DeepSWE runs held network isolation in every trial read.

**Key Findings** (board JSON, all models at all efforts, 28,849 board trials, $4,746 of router inference): mini-swe-agent (bash only) 51.4% macro resolve rate (95% CI 48.5-54.2), with Kimi Code 50.5%, Hermes Agent 50.3%, Pi 49.4% and Claude Code 49.2% statistically tied with it; Qwen Code 44.7%, Codex 44.5%, OpenCode 35.5%, OpenClaw 27.3%. Cost per solved task: Pi $0.29, Claude Code $0.52, mini-swe-agent $0.53, OpenCode $3.35. Models: GLM-5.3-Flash and DeepSeek-V4.1-Flash at low and high effort, Flint at default; benchmarks Terminal-Bench 2.1 and DeepSWE v1.1 via Harbor.
**Citations**: Niklaus, J. (2026). *Harness Leaderboard* (v0.1.1) [Hugging Face Space]. https://huggingface.co/spaces/joelniklaus/harness-leaderboard
**Notes**: The board's own changelog qualifies several headline results. Pi, Claude Code, Qwen Code, Codex and OpenCode ran with their own defaults for models they did not know (Pi assumed a 128,000-token window and summarized at about 112,000 against models holding 262,144 to 1,048,576), and the changelog attributes most of Pi's lower cost per call to that early summarizing, so the cost-per-solve comparison is configuration-bound. Claude Code did not see the model's reasoning on the two router models until a proxy fix on 2026-11-07, after the board's runs. Codex and OpenCode first ran without their own system prompts and were re-run (2026-10-29). DeepSWE mixes online-era and offline trials. Scope is open "Flash"-class models on coding benchmarks only. Edition-bound in the sense of the lab's own rule: results hold for the pinned harness versions and default configurations, not the harnesses in general.
**Validation Status**: ✅ Verified 2026-11-08 (README, CHANGELOG.md and LAB_NOTEBOOK.md read at Space commit fb3c971; every number above re-read from the live board JSON; the LinkedIn post's figures match it).

---

#### Harness Lens: an interactive comparison of coding-agent harnesses (harness-hub, Hugging Face Space, 2026)

**Authors**: harness-hub (Hugging Face organization)
**Date**: created 2026-10-20; read 2026-11-08 (Space commit d1ad16b, last modified 2026-11-07)
**URL**: https://huggingface.co/spaces/harness-hub/harness-lens
**Evidence Level**: B (source-linked documentation of what each harness does: every claim links to exact source lines at a pinned commit, and a checker verifies the links; it makes no performance claims)
**Relevance**:
- Companion to the Harness Leaderboard: explains what differs between the harnesses it measures (system prompts, tools, edit formats, context compaction, subagents, permissions, project instructions, extensibility, model providers).
- Agent security: verbatim system and compaction prompts and the model-visible tool inventory per harness, which is the attack surface a prompt-injection or tool-abuse review starts from.

**Key Findings**: a matrix, per-harness pages, side-by-side compare with prompt diffs and tool overlap, verbatim prompts with token counts, a compaction calculator (when each harness auto-compacts for any window size), and tools grouped by canonical category. Search runs in the browser with a quantized MiniLM embedding model; no generative model runs in the Space.
**Citations**: harness-hub. (2026). *Harness Lens* [Hugging Face Space]. https://huggingface.co/spaces/harness-hub/harness-lens
**Notes**: The harness count differs by surface: the README says 17, the announcing post says 34, and the Space's `harnesses/` folder held 37 entries on 2026-11-08 (including Claude Code, Codex, Gemini CLI, OpenHands, Aider and SWE-agent). Cite the folder count with its date.
**Validation Status**: ✅ Verified 2026-11-08 (README and `harnesses/` listing read through the Hugging Face API at commit d1ad16b).

---

## Monthly Refresh Additions (2026-11-23)

Added in the November 2026 monthly refresh. Each source was published or first committed in or after July 2026, was read at its primary on 2026-11-23, and bears on one of the hypotheses in manuscript §3.7. None of them moves a hypothesis score here; where one could, the question is staged for the owner and the entry says what it can and cannot carry.

---

#### Interoperable ACID Transactions for Open Table Formats (Götz, Ritter, El-Hindi & Giceva, PVLDB 2026)

**Authors**: Tobias Götz, Muhammad El-Hindi, Jana Giceva (Technical University of Munich); Daniel Ritter (SAP)
**Date**: July 2026 (PVLDB Vol. 19, No. 11, pp. 3216-3230); read 2026-11-23
**URL**: https://www.vldb.org/pvldb/vol19/p3216-goetz.pdf
**DOI**: 10.14778/3836663.3836684
**Evidence Level**: A (peer-reviewed; the venue is confirmed in the PVLDB Vol. 19 No. 11 front matter on vldb.org, dated July 2026, and in the paper's own PVLDB Reference Format block)
**Relevance**:
- H-ARCH-01 (context): the paper treats Delta Lake, Apache Iceberg and Apache Hudi together as the open table formats "widely used in modern cloud analytics" and measures a limit they share. It says nothing about Iceberg's share against the other two, so it adds to what the formats can and cannot do and leaves the dominance claim where it was.
- Lakehouse design for security data: a detection or enrichment job that has to update two tables atomically, such as an alert table and the evidence table behind it, runs into exactly the limit this paper addresses.

**Key Findings**: The abstract states that "existing OTFs provide transactional guarantees only for single-table transactions. Supporting transactions that access multiple tables typically requires external coordination services, which compromise interoperability and deployment independence." The authors present "OTF-native mechanisms for multi-table atomicity, consistency, and isolation that rely solely on object-store primitives", build them into a prototype called LakeVilla, and evaluate it with "formal verification, extensive benchmarks, and an interoperability case study with Trino". Table 1 is captioned "Properties of OTF solutions. Current solutions trade off interoperability to support cross-table transactions", and its rows include DuckLake and Project Nessie.
**Citations**: Götz, T., Ritter, D., El-Hindi, M., & Giceva, J. (2026). Interoperable ACID Transactions for Open Table Formats. *Proceedings of the VLDB Endowment*, 19(11), 3216-3230. https://doi.org/10.14778/3836663.3836684
**Notes**: LakeVilla is a research prototype, and the abstract's "low overhead" is the authors' own evaluation, which was not re-derived here. One author is at SAP. The DOI resolves to dl.acm.org, which refused a scripted request (HTTP 403), so the PDF at vldb.org is the copy read.
**Validation Status**: ✅ Verified 2026-11-23 (PDF read at vldb.org; abstract, Table 1 caption and the PVLDB reference block quoted from it; issue and month confirmed in the Vol. 19 No. 11 front matter)

---

#### Fugue: Online Elasticity for Distributed Stateful Stream Processing (Zhang, Mao & Jacobsen, PVLDB 2026)

**Authors**: Yuqiu Zhang (Confluent Inc.; the paper's footnote reads "Work done while at the University of Toronto"), Yunhao Mao and Hans-Arno Jacobsen (University of Toronto)
**Date**: July 2026 (PVLDB Vol. 19, No. 11, pp. 3288-3301); read 2026-11-23
**URL**: https://www.vldb.org/pvldb/vol19/p3288-zhang.pdf
**DOI**: 10.14778/3836663.3836689
**Evidence Level**: A (peer-reviewed; venue confirmed in the PVLDB Vol. 19 No. 11 front matter and in the paper's PVLDB Reference Format block)
**Relevance**:
- H-STREAM-01 (context): a peer-reviewed measurement of what it costs to change parallelism in a stateful stream engine, which is operational evidence about stateful streaming at scale. It is a benchmark study on Apache Flink with NEXMark queries, with no production deployment and no security workload. The manuscript's restoration path reads "one additional verified, catalogued production or peer-reviewed leg returns the hypothesis to 17/25 and the High band" (`PUBLICATION-MANUSCRIPT.md` §3.7, H-STREAM-01), and on that wording this paper qualifies as a peer-reviewed leg, so the open question is whether a peer-reviewed benchmark with no security workload should count for a hypothesis about stateful security processing. That call is staged for the owner as a two-sided one, and no score moves here.
- H-IMPL-02 (context): describes Flink's rescaling model as one that "requires halting applications globally for a long time", which is one concrete source of the operational burden the staffing hypothesis is about. It carries no staffing figure.

**Key Findings**: The abstract reports that Fugue, implemented in Apache Flink, "reduces tail reconfiguration latency by up to 98.6% relative to native Flink while maintaining over 90% of peak throughput", and that "Compared to reactive pull-based baselines, Fugue reduces end-to-end migration latency by up to 93.7%." The evaluation uses "the NEXMark benchmarking suite" (Section 5.1, Workloads paragraph). The testbed runs "Apache Flink version 1.18" with "RocksDB as the state backend", "Apache Kafka 3.8.1" as the message broker and a checkpointing interval of 60 seconds (Section 5.1, Testbed Setup paragraph).
**Citations**: Zhang, Y., Mao, Y., & Jacobsen, H.-A. (2026). Fugue: Online Elasticity for Distributed Stateful Stream Processing. *Proceedings of the VLDB Endowment*, 19(11), 3288-3301. https://doi.org/10.14778/3836663.3836689
**Notes**: Both percentages are "up to" figures from the authors' own runs of their extension against stock Flink, so they are best cases across those runs. Fugue is a research extension, and whether any of it has reached an Apache Flink release was not checked. The baseline is Flink 1.18, an older line than the Flink 2.2.1 the SDW Lab stream-complexity entry below runs, so the comparison is against Flink 1.18's native rescaling. The first author is at Confluent Inc., and the paper's footnote places the work at the University of Toronto.
**Validation Status**: ✅ Verified 2026-11-23 (PDF read at vldb.org; abstract, testbed and workload sentences and the author affiliations taken from it; venue confirmed in the front matter)

---

#### Splunk Cloud Platform 10.7: Federated Search over Amazon S3 datasets backed by an Apache Iceberg REST catalog (Splunk documentation, 2026)

**Authors**: Splunk (Cisco), product documentation
**Date**: 10.7 page last updated 2026-10-23; 10.7 release notes last updated 2026-10-17; the 10.6 version of the page, last updated 2026-09-16, gives the minimum version; read 2026-11-23
**URL**: https://help.splunk.com/en/splunk-cloud-platform/search/federated-search/10.7/run-federated-searches-over-amazon-s3-datasets/define-an-amazon-s3-dataset/create-an-amazon-s3-dataset-for-federated-search-that-is-backed-by-an-iceberg-rest-catalog
**Alt URL**: https://help.splunk.com/en/splunk-cloud-platform/release-notes/10.7/splunk-cloud-platform-release-notes/whats-new (10.7 release notes)
**Evidence Level**: B (vendor technical documentation, cited only for what the feature does, under the 2026-11-03 owner ruling recorded in METHODOLOGY §3.1, which places vendor documentation at B for what a feature does and at C, bias flagged, for how well it works, how fast it is or how it compares; nothing here is cited for speed, cost or reliability)
**Relevance**:
- H-ARCH-01: the incumbent SIEM vendor whose product runs on its own index format now reads Iceberg tables in place through a customer-run REST catalog, which extends the vendor-support leg from the lakehouse and cloud vendors to the SIEM side of the market. It shows Splunk reading Iceberg in place and leaves open whether Splunk stores any of its own indexes in Iceberg.
- ch06 §6.5 (keep the SIEM, federation): the operating documentation behind the Splunk Platform 10.4 and Cisco Data Fabric federated-search announcement catalogued above.

**Key Findings**: The 10.7 page: "The dataset must have an Amazon S3 connection definition that includes the Catalog URL of your Apache Iceberg REST catalog", and at the Configure dataset step the user selects "Apache Iceberg REST as the type of catalog". The 10.6 page: "Your Splunk Cloud Platform deployment must be on version 10.4.2604 or higher." The 10.7 release notes: "You can continuously promote selected Machine Data Lake data into an analytics table for recurring analysis, summary workloads, scheduled alerting, and long-term queryable retention."
**Citations**: Splunk. (2026). *Create an Amazon S3 dataset for federated search that is backed by an Iceberg REST catalog* (Splunk Cloud Platform 10.7 documentation). help.splunk.com.
**Notes**: These pages document configuration only, and the cost and speed of a federated search against Iceberg are not on them. The 10.7 release notes do not contain the word "Iceberg", so the Machine Data Lake "analytics table" quote is context on what the release ships and is no evidence about Iceberg. The page's version switcher already lists 10.8, so 10.7 was not the newest documentation on 2026-11-23; the 10.7 pages are cited because they are the ones read. The Machine Data Lake limits pages were not read for this entry, so nothing about promotion limits is catalogued here.
**Validation Status**: ✅ Verified 2026-11-23 (all three pages fetched at help.splunk.com; quotes taken from the fetched text; "last updated" stamps read from each page title)

---

#### Arroyo 0.16.0: stateful stream processing with transactional Iceberg ingestion (Wylde, arroyo.dev, 2026)

**Authors**: Micah Wylde (byline: "Creator of Arroyo")
**Date**: November 17, 2026 (post date; GitHub release v0.16.0 published 2026-11-17T00:48:50Z); read 2026-11-23
**URL**: https://www.arroyo.dev/blog/arroyo-0-16-0
**Alt URL**: https://github.com/ArroyoSystems/arroyo/releases/tag/v0.16.0
**Evidence Level**: B (official release notes of an Apache-2.0 open-source project, for what the release ships, which METHODOLOGY §3.1 places at B with vendor engineering blogs and project documentation; bias flagged: the post names Basin Pipelines as Cloudflare's managed Arroyo service, announces its general availability in this release and recruits for Cloudflare's Pipelines team, so the author's team sells the managed product, and the operating-scale statement is the maintainer's own and carries no figure)
**Relevance**:
- H-ARCH-01: a stateful stream engine that treats Iceberg as a first-class sink and maintains its commit handling in the main release line, which is ecosystem evidence for Iceberg as the landing format for streamed data.
- H-STREAM-01 (context only): the post reports operating the engine "at scale across thousands of concurrent pipelines and many GB/s of traffic" in Basin Pipelines, which it calls Cloudflare's managed Arroyo service. With no measured figure and no security workload, that statement cannot be scored as a leg.

**Key Findings**: The release "encompasses almost a year of work and over 140 PRs merged" and marks the general-availability release of Basin Pipelines. The rewritten FileSystem sink is "the sink used for writing files to object storage and performing transactional ingestion into data lake formats, including Delta and Apache Iceberg", designed so that "each incoming event should appear exactly once in the output, even if we crash in the middle". The changelog lists "Populate snapshot summary stats in Iceberg commits", "Add timeouts to Iceberg commit to prevent unbounded checkpoint stalls" and "Classify Iceberg rate limits as external failures". For JSON sources, "With bad_data = 'fail' (the default), the pipeline fails with that error", which matters for security telemetry, where malformed records are routine. The post names 0.17 as the expected "last before 1.0".
**Citations**: Wylde, M. (2026, November 17). *Announcing Arroyo 0.16.0*. Arroyo blog. https://www.arroyo.dev/blog/arroyo-0-16-0
**Notes**: No benchmark, latency figure, catalog list or Iceberg format-version detail is in the post, and Arroyo is pre-1.0 software.
**Validation Status**: ✅ Verified 2026-11-23 (post fetched at arroyo.dev and every quote above taken from it; release tag and Apache-2.0 licence confirmed through the GitHub API)

---

#### Can Risk-Based Alerting Mitigate Cybersecurity Alert Fatigue? (Uetz, Bönninghausen, Hackländer-Jansen & Henze, arXiv preprint, 2026)

**Authors**: Rafael Uetz, Philipp Bönninghausen, Louis Hackländer-Jansen, Martin Henze
**Date**: 2026-09-02 (arXiv v1); read 2026-11-23
**URL**: https://arxiv.org/abs/2609.02465
**Evidence Level**: B (preprint; the arXiv comment reads "Submitted to USENIX Security '27", so no venue is confirmed and the entry sits in the preprint category under METHODOLOGY §3.1)
**Relevance**:
- H-SOC-BASELINE-01 (adjacent): the hypothesis rests on one production measurement of alert base rates, and its promotion path is a second independent production study. This paper evaluates alert prioritization on "eight diverse alert datasets, six of which we created or extended" and does not measure a production SOC's base rate, so it does not lift the single-source cap. It bears on the §4.1 inference about where alert volume goes, because it tests whether risk-based scoring can move true attacks to the top of the review queue.

**Key Findings**: The abstract calls the work "the first systematic evaluation of RBA", reformulated as "a continuous alert prioritization problem rather than a binary decision problem", with "five fundamental risk hypotheses" implemented in an experimentation suite named CATS. The best combinations reach "AUROC μ=0.92, σ=0.09 across the eight datasets", against prioritization by severity level at "AUROC μ=0.72, σ=0.21".
**Citations**: Uetz, R., Bönninghausen, P., Hackländer-Jansen, L., & Henze, M. (2026). *Can Risk-Based Alerting Mitigate Cybersecurity Alert Fatigue?* arXiv:2609.02465.
**Notes**: Only the arXiv record and abstract were read; the dataset list and method were not. Most of the datasets were built or extended by the authors, so the scores describe those datasets. AUROC measures ranking quality, so it says how well true alerts were ordered and gives no count of false alerts removed. Recheck the venue if the paper is accepted.
**Validation Status**: ✅ Verified 2026-11-23 (arXiv API record: title, authors, v1 date, comment line and abstract)

---

#### Batch vs Streaming Operational Complexity for One Detection, SDW Lab First-Party Measurement (stream-complexity, 2026)

**Authors**: Jeremy Wiley (SDW Lab), FIRST-PARTY
**Date**: 2026-07-19 (July run; pre-registration committed before the scored results), extended by the v2 run of 2026-11-03, the freshness sweep of 2026-11-06 and the RisingWave run of 2026-11-07; read 2026-11-23 at lab commit 08f1044 (the URLs below are pinned to it; master has since moved to ba58d65, which changes the README and leaves both results files unchanged)
**URL**: https://github.com/flying-coyote/sdw-lab-benchmarks/blob/08f10448eced4ba02d591c7aca4a3ddbf7892296/stream-complexity/results/RESULTS.md
**Alt URL**: https://github.com/flying-coyote/sdw-lab-benchmarks/blob/08f10448eced4ba02d591c7aca4a3ddbf7892296/stream-complexity/results/RESULTS-v2-2026-11-03.md (v2, which supersedes the July freshness framing and reports the falsifier as a knife-edge)
**Evidence Level**: B (first-party lab measurement under a frozen pre-registration: single host, synthetic seeded corpus, one detection shape, and complexity proxies that are not dollars, headcount or on-call hours)
**Relevance**:
- H-IMPL-01 (Streaming TCO): the only measured evidence on the hypothesis's direction since its literature legs were withdrawn. The results file names H-IMPL-01 as its target and states that the run "does not deliver a clean magnitude", so it does not meet the pre-registered bar to move the score.
- H-IMPL-02 (Staffing premium, context): the fault battery measures operator steps and time to restore, which is the kind of work the staffing claim is about, though the bench carries no staffing figure.

**Key Findings** (July run, `results/RESULTS.md`, with line numbers at lab commit 08f1044): one detection (five or more failed logins per user and source IP inside a 60-second event-time window) over a seeded 500,000-event corpus, batch on DuckDB against Kafka 4.3.1 with Flink 2.2.1 (lines 6-8). Moving parts: "stream 3 containers + 1 host process" with images "totaling ~913 MB", against "batch 0 containers + 1 host process" (line 18). Configuration: "stream 197 LOC vs batch 131 LOC = 1.5×", which fails the pre-registered 3× threshold (line 19). Fault recovery: a Kafka broker kill took 2 steps and 18.1 s and a Flink taskmanager kill 2 steps and 21.5 s to restore infrastructure, against 1 step and 0.02 s for the batch job (lines 27-29); recovery correctness was not cleanly measured (line 31). The v2 run puts the real-clock freshness gap at "about 3.0 s at the median (2.18 vs 5.20 s, roughly 2.4×)" and says July's 8-9× figure came from an accelerated clock (`RESULTS-v2-2026-11-03.md` line 124).
**Citations**: SDW Lab (2026). *stream-complexity: batch vs streaming operational complexity* [benchmark results]. https://github.com/flying-coyote/sdw-lab-benchmarks/tree/master/stream-complexity
**Notes**: Self-authored, so it is labelled first-party and cannot stand as independent evidence. The v2 falsifier "sits on a knife-edge that depends on rounding 1.50×" and is "reported rather than resolved" (lab README line 31 at 08f1044), and the confidence move it would trigger is already staged for the owner on the lab side. Quote the complexity proxies with the honesty boundary at line 3 of the July results file attached.
**Validation Status**: ✅ Verified 2026-11-23 (July and v2 results files read in the public repository at commit 08f1044; every figure above quoted from the line cited; both pinned commit URLs return HTTP 200, and 08f1044 is an ancestor of master)
