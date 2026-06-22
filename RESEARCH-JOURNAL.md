---
type: evidence
title: "Literature Review Research and Validation Journal"
created: 2026-06-05
tags: [bibliography-validation, source-integrity, fabrication-audit, literature-review, provenance]
---

# Research / Validation Journal

The durable, externally-reviewable record of the validation research done on each reference. Its job is
to make every verdict re-checkable by an outside reviewer and to stop the same items being re-validated
without good cause. **Append-only**: every future validation adds a dated row here rather than re-doing
silent work. This is the provenance trail the bibliography lacked — its absence is exactly how fabricated
citations survived (see `CHANGELOG.md` 1.22.0 and the private propagation register).

## How to read / extend

Each row records: the reference, the date validated, the **method** (how it was checked), the **verdict**,
and a one-line **finding** an external reviewer can confirm. To extend: re-run the check, append a new
dated row (don't overwrite — the history is the point), and update the entry's `Validation Status` line in
`MASTER-BIBLIOGRAPHY.md` to match.

**Methods**: `link` = HTTP status check · `claim↔source` = fetched the URL and compared the entry's specific
stat/claim against the page · `archaeology` = git-history provenance trace · `cross-ref` = checked against a
sibling concept/source.

**Verdicts**: `VERIFIED` source resolves and supports the claims · `MISMATCH` URL resolves but does not
support the specific stat (the number was stapled on) · `WEAK-SOURCE` no real/resolvable URL ("Various",
"Multiple", "Personal", placeholder) so the claim is unsourceable as cited · `FABRICATED` no such source
or the claim is invented (removed) · `DEAD` URL broken, no replacement · `FIRST-PARTY` Jeremy's own
model/measurement (sound, but self-authored — label, don't treat as external evidence).

The cleanup worklist for everything not `VERIFIED` lives in the private register
`project1/FABRICATIONS-REGISTER-2026-06.md` (categorized + propagation-mapped). This journal is the
evidence; that register is the to-do.

---

## 2026-06-05 — full validation pass (Claude audit, 6 parallel agents + link sweep + archaeology)

**Scope**: all 148 then-current entries. **Method**: complete 148-URL link check; claim↔source audit of
119 original entries (the 29 merged/2026 entries were claim↔source-verified at insertion); git archaeology
on the NANDA fabrication. **Headline**: the original 2025-10-15 bulk-generated corpus systematically
stapled specific numbers onto sources that don't contain them — the URL resolves, so a link-check passes,
but the stat is unsourced. Result: ~45 VERIFIED, ~35 MISMATCH, ~22 WEAK-SOURCE, 9 FABRICATED (removed),
3 DEAD. Evidence-Level-A recomputed honestly at ~65% (the header's prior "80%" was self-reported).

### VERIFIED — settled 2026-06-05, do not re-validate without cause

| Entry | Method | Finding |
|---|---|---|
| Starburst docs / Athena comparison | claim↔source | live official docs, on-topic |
| Trino: The Definitive Guide (O'Reilly) | claim↔source | 2nd ed 2022, authors/ISBN match |
| Dremio docs / lakehouse guide | claim↔source | live; guide is Mazumdar Sept 2023 (entry's "Alex Merced" attribution is a minor slip) |
| Alex Merced YouTube | link | real channel "Code, Data and Tech" |
| ClickHouse Log Analytics — Cloudflare | claim↔source | ~10-12× compression supported |
| Questioning the Lambda Architecture — Kreps | claim↔source | O'Reilly Radar 2014-07-02, Kappa, all match |
| McAfee streaming — Kai Waehner | claim↔source | real post 2025-01-27 |
| Top Trends Data Streaming 2025 — Waehner | claim↔source | real post 2024-12-02 |
| Prosci Change Management 12th ed | claim↔source | 93%/15%/7× corroborated by Prosci research |
| Chris Bisnett — Huntress ClickHouse (video) | link | YouTube live; 93%/3M corroborated |
| Azure — Kafka at Trillion Events/Day | claim↔source | Siphon blog supports ~3T/day, 30M/sec |
| DuckDB Labs — DuckDB Overview | claim↔source | "Why DuckDB" supports OLAP positioning |
| Apache XTable | claim↔source | omni-directional interop confirmed (minor Paimon overstatement) |
| Netflix — Building Resilient Data Platform (WAL) | claim↔source | live 2025-09-26 post; TLS quirk only |
| Cloudera TEI (Forrester 2024) | claim↔source | 35% savings / 80% faster TTV / $11.5M confirmed |
| Gartner — Security Spending Forecast 2024-2029 | claim↔source | $193B(2024)→$213B(2025) confirmed (minor 2026/2029 drift) |
| Apache Iceberg — Industry Consensus (Dremio SotDL) | claim↔source | 29% vs 23% adoption stat exact (release dated Nov 2023) |
| Apache Iceberg Foundation — governance | claim↔source | live ASF page; contributor scale uncontroversial |
| Apache Iceberg — official / maintenance / Spark-procedures docs | claim↔source | live official docs |
| ClickHouse vs Elasticsearch — storage | claim↔source | ClickHouse advantage supported (entry's 5-10× conservative vs source 9-19×) |
| OCA — Standards & Interoperability | claim↔source | site real; interop framing holds |
| MITRE Engenuity — ATT&CK Evals | claim↔source | 2025 enterprise round (Scattered Spider, 11 vendors) confirmed |
| Confluent — ML with Apache Kafka | claim↔source | KSQL/embedded-ML confirmed |
| NANDA — Infrastructure for Internet of AI Agents | claim↔source | real MIT project; "1,000+ agents via Join39" confirmed; **98.7% never belonged here** |
| Security Data Pipeline Market Guide 2025 (SACR) | claim↔source | Cribl $200M ARR / 25-70% reduction confirmed |
| Rippling — Cost-Effective SIEM | claim↔source | $4.50/rule = 1.8 Snowflake credits confirmed in part 3 |
| Monad — Cutting SIEM Costs | claim↔source | every figure (Okta 50.7%, $11,721/yr, etc.) verified |
| CSA Press Release — Governance Maturity | claim↔source | "strongest indicator", 46%/12% split confirmed |
| SANS — Securing AI 2025 | claim↔source | confirmed |
| Databricks — Cyber Defense (Barracuda/Palo Alto) | claim↔source | Barracuda 75% / <5min, Palo Alto 3× confirmed |
| ClickHouse — GitLab sub-second | claim↔source | 30-40s→<1s, 50M users confirmed |
| ClickHouse vs Snowflake | claim↔source | 3-5× cost / 2× faster verbatim |
| Netflix ClickHouse Pipeline — 5 PB/Day | claim↔source | 5 PB/day + 10.6M events/sec confirmed on page (flagged-suspect, holds) |
| Hunters Security — security data lakes | claim↔source | half of 15 largest banks, HSBC confirmed |
| Linux Foundation — OCSF joins | claim↔source | 900+ contributors / 200+ orgs / founders confirmed |
| Google Cloud — AI Agent ROI | claim↔source | 52% prod / 74% ROI / 39% >10 agents verbatim |
| Arctic Wolf — Aurora 2025 | claim↔source | 330T observations→8.6M alerts, 10K orgs confirmed (minor sub-stat) |
| DBSP — Incremental Computation (feldera) | claim↔source | repo real, VLDB paper cited; queued, no stat claims |
| Xor Filters (arXiv 1912.08258) | claim↔source | Graf & Lemire; 25%/15% match (entry's "8.2 bits" ~9.2-9.8 real — minor) |
| Kingpin (Poulsen 2011) | cross-ref | real book, ISBN/author/story confirmed |
| CISA — Enhanced Security Monitoring (aa23-193a) | claim↔source | advisory real; "24-36mo retention" embellished beyond ~12mo |

*(Data-engineering concept-sourced entries CLP/Okta-multi-engine/Splunk-federated/materialized-views/NATS/
DataFusion-Ballista/Lakekeeper were cross-validated CLEAN in the concept review — see project1 register.)*

### FABRICATED — removed 2026-06-05 (do not re-add without a real primary source)

| Entry | Method | Finding |
|---|---|---|
| Microsoft "Operational resilience in the face of attacks" (+dup) | link+search | no such post; AI-placeholder. Removed cf26e77 |
| McKinsey "Accelerating data architecture transformation" | search | no such article. Removed cf26e77 |
| "Enterprise Data Quarterly — Streaming vs Batch TCO" | link+search | not a real publication; domain dead. Removed cf26e77 |
| IDC "Hidden Costs of Real-Time Data 2024" | search | no such report; wrong URL format. Removed cf26e77 |
| Trino Summit "Data Contracts" session | search | defunct domain, not in any lineup. Removed cf26e77 |
| "ClickHouse at Shell — 57TB/day security" | link+search | no trace anywhere; figure unsupported. Removed cf26e77 |
| Flink Staffing "DevOps.com" + Ververica Staffing | claim↔source | same klaviyo.tech URL, two fake publishers, invented FTE stats. Removed 9a24e4e |
| SANS "Security Analytics Implementation Timelines" | link+search | non-existent whitepaper, empty findings. Removed 9a24e4e |

### MISMATCH — real source, the specific stat is NOT in it (worklist: re-source or strip)

| Entry | Finding (the unsupported claim) |
|---|---|
| ClickHouse @ Cloudflare 6M rps | "96.3% under 1s" / "1,000+ replicas" not in either URL → also book ch08 |
| Kafka Benchmark — Confluent | "4.5M events/sec on 9 nodes" not in cited blog |
| AWS Storage Optimization Whitepaper | cited PDF is now a deprecated empty stub |
| DORA 2024-2025 | "2.7× staff / 3.2× incidents" streaming-vs-batch not in DORA |
| LinkedIn Kafka Streams State | "32T records/day / Northguard" not in cited course |
| Netflix Kafka Tiered Storage | URL is Confluent docs; no Netflix / "70-80%" / "2T msgs" |
| ClickHouse Vectorized / IPv6 / Compression / Perf-Guide | the 8-10×/50-100×/3-14× and the page identity all off |
| Huntress ClickHouse | 93% cost OK; "1M EPS / 16B events / 20-50× compression" not in source |
| Altinity Ingest | URL→ClickBench; "1.8-2.2M events/sec" absent |
| Uber Real-Time Security Views | generic Confluent latency article; claims absent |
| Arrow Flight SQL | spec page, no "20× vs JDBC" benchmark |
| Anyscale Ray Serve | "600%/5000 replicas/99.9%" not on page |
| Cloudera Impala + Iceberg | redirect; "10× over Hive" gone (also DEAD) |
| Flink Checkpointing for Security | security-specific intervals not in generic doc |
| Microsoft Purview Retention | UEBA-style retention claims not in M365 doc |
| Confluent Roadmap / Architecture & Sizing | "4-month" / "45-55% TCO" not in the courses |
| "Gartner" Security Data Lakehouse | URL is a phData blog, not Gartner |
| Brooks — Mythical Man-Month | Pearson URL resolves to a different book (wrong code) |
| Netflix Observability + Polaris | URL is the bare qconferences.com homepage |
| SK Telecom Iceberg Validation | "97% / 52.7TB in 3.39s" not in the Trino recap |
| Uber Palette Feature Store | "37% feature-failures / 20,000+ features" not in blog |
| DARPA XAI | "$75M / highest explainability" not on page |
| MITRE Insider Threat | "18-24mo / 2.3× / 5,000 cases / 47 techniques" not on page |
| CSA — ML for Cybersecurity | URL is AI-Safety WG page; claims absent |
| Microsoft Threat Modeling AI/ML | doc is 2019; "40% had AI incidents 2024" absent |
| Apache Arrow powered_by | all multipliers absent from a plain project list |
| Champion-Challenger MLOps | "42% FP reduction" not in DataRobot blog |
| Microsoft Concept Drift | "security drifts 2-3× faster" invented |
| Amazon Security Lake + Iceberg | "3×/10× / 25+ partners / AppFabric" not in the Feb-2024 post |
| Tenzir Pipeline Platform | "30% TCO" real but mis-baselined (vs Cribl, not "query-based") |
| SANS AI Controls Framework | "SEC/OCC audits / tamper-evident logs" not in blog |
| Forrester "Drowning in Security Data" | post is about MS Sentinel; cited findings absent |
| Apache Gravitino adoption | adopter list + "Bilibili 70%" not on page |
| Apache Polaris ecosystem | version numbers + "v1.2.0 governance" not on page |
| AI Multiple — Agent ROI | "171% ROI / US 192%" not on page |
| Obsidian — AI Agent Landscape | "<5min MTTD / <2% FP" invented thresholds |
| DuckDB 1.0-1.4 LTS | version specifics on the alt URL, not the cited dev.to page |
| Tenzir MCP | quote "100% hands-off keyboard" → corrected to source's "100% schema-conforming" (9a24e4e) |

### WEAK-SOURCE — no resolvable URL; find a real source or soften (worklist)

`Various`/`Multiple`/`Personal`/`LinkedIn`/bracketed-placeholder: Streaming-vs-Batch Differential, AWS
Well-Architected, AWS Tiered Storage, Google SRE nines, FinSec reliability, Gartner reliability, Uptime
Institute (all bracketed placeholders); Iceberg Universal Support, Gartner AI Maturity, SOC Automation ROI,
Iceberg 2025 Perf, Lakehouse Patterns, Catalog Wars, RLS Performance, Streaming Cost 2025 (all "Various"/
"Multiple"); AI Governance Gate + RAPTOR (LinkedIn — concepts corrected a3944a08); Databricks TCO, SANS AI
Survey (gated), CSA State-of-AI (gated), Hyperscan (homepage); StarRocks vs ClickHouse ("Various" but the
1.87×/3-5× numbers DO trace to StarRocks' own benchmark — attribute as vendor).

### DEAD

| Entry | Finding |
|---|---|
| Uber "Real-Time Security Analytics with Flink" | 404, no Wayback, no replacement |
| Disney+ "Real-Time Security Analytics" | Medium 404; original gone |

### FIRST-PARTY (sound; label as self-authored, not external evidence)

| Entry | Finding |
|---|---|
| MOAR Stack reference architecture (#81) | Jeremy's own model; LIGER→MOAR rename intentional; cost figures live on the economics page (transparent assumptions). Renamed + repointed + relabeled A→B (9a24e4e) |
| Splunk DB Connect Benchmark 145× (#25) | real first-party measurement; repo NDA-gated (404 expected); methodology public |
| a data-platform practitioner / Okta-Jake-Thomas | genuine private practitioner input; unverifiable as external citation |
| SDW Lab `zeek-flagship-rerun` (two-regime) | CV-gated first-party; OpenSearch foil ÷ ClickHouse-Iceberg ~10–11× on scan-aggregation, ch-native ÷ foil 46.8×; two-regime split (lakehouse wins hunting aggs, index wins lookups). Self-authored; magnitudes host-specific |
| SDW Lab `engine-join-specialization` | CV-gated first-party; StarRocks wins joins, ClickHouse wins aggregation (grounds H-ARCH-06) |
| SDW Lab `ocsf-zorder-pruning` | first-party; z-order is a pruning-COVERAGE lever, not latency (within-file + cross-file + Bloom legs) |
| SDW Lab `sigma-portability` | first-party compile-fidelity matrix; OpenSearch PPL silently drops the correlation time-window on 3/5 rules |
| SDW Lab multi-user concurrency + shard-count (2026-06-15) | first-party; single-host QPS ceiling is shard-invariant (~7 QPS), so the foil's 6.73× "scaling" is a single-shard-baseline artifact |
| SDW Lab Arrow/ADBC manageability (2026-06-15) | first-party; integration surface collapses 4→1, engine-swap 8–24 LOC → ~1–3, uniformity gated by Flight-SQL adoption (CH/SR/Trino need the JVM ADBC-JDBC bridge) |

### Merged & 2026 additions — claim↔source verified at insertion (2026-06-05)

22 Second-Brain merge sources (D3FEND, ATLAS, Matryoshka, F3/SIGMOD, Zeek, Power Query M, SCF, NIST CSF,
CoSAI, Ballista, Lakekeeper, practitioner pubs) — 16 external URLs status-checked live (d8a35a4). 8 2026
primary sources (Iceberg v3 spec, v4 milestone #58, DuckLake v1.0, Variant, OCSF 1.8.0, NANDA arXiv
2507.14263, Splunk 10.4, S3 Tables) — each URL fetched + claim checked (d152830).

### Provenance traces (git archaeology)

| Item | Finding |
|---|---|
| NANDA "98.7% automation" | CONFLATION. 98.7% = Anthropic Nov-2025 code-execution-with-MCP token reduction (150K→2K), captured correctly Dec-6 (`ea06b144`) in a blog draft ADJACENT to a NANDA draft; downstream synthesis fused them; book added a hallucinated "Siva Rajamanickam" author. Decoupled in book 65c83eb; essay rewrite pending voice gate. Full chain in register §1.1 |
| ai-governance "10×" / RAPTOR | same synthesis-conflation mechanism; concepts corrected a3944a08 |

---

## 2026-06-05 (later) — re-sourcing pass (6 parallel agents)

Worked the MISMATCH + WEAK lists above. Key finding: **most flagged entries had real numbers attached to
the wrong URL** — re-sourceable, not fabricated. Dispositions applied to `MASTER-BIBLIOGRAPHY.md`:

- **Removed 4** (no salvageable content): Altinity ingest, Uber Real-Time Security Views, CSA ML-for-
  Cybersecurity, Financial-Services Reliability (commit 41d346c).
- **Re-sourced 8 URLs** to where the real number lives (commit 41d346c): ClickHouse Perf-Guide, Cloudera
  Impala-Iceberg (10× verbatim), Mythical Man-Month (Pearson code), Ray Serve, DuckDB LTS (→duckdb.org),
  Hyperscan (→USENIX NSDI'19), AI-Multiple ROI (→PagerDuty 2025), LinkedIn Kafka Streams (→Northguard blog).
- **49 entries carry an authoritative `⚠️ Validation (2026-06-05)` correction** (commit ec5b41d): the real
  source/number where re-sourceable, and the specific inline figures to disregard where fabricated. That
  line governs the entry until the prose is polished. Highlights: SK-Telecom conflation untangled; SRE
  cost-of-nines corrected to ~100× (was 10×); Gravitino/Polaris/Iceberg-2025/Catalog-Wars/Streaming-2025/
  StarRocks re-sourced; DARPA-$75M / MITRE-2.3× / Champion-Challenger-42% / Drift-2-3× / Uber-Palette-37% /
  DORA-2.7× marked unsupported; Gartner-Lakehouse is actually phData; MS-Threat-Modeling is 2019.

Net: the MISMATCH/WEAK worklist is resolved — every entry is removed, re-sourced, or correction-noted with
the real disposition. Remaining polish: fold each validation note into the entry prose and re-tier; that's
cosmetic, the facts are now correct + sourced. Entry count 145 → 141.

---

## 2026-06-05 (later still) — fold + re-tier pass (4 parallel agents, disjoint blocks)

The 49 `⚠️ Validation (2026-06-05)` correction notes were **folded into entry prose and re-tiered**, so
each entry now stands on its own without the appended note governing it. Four agents each owned a disjoint
block of the bibliography (entries 1-13 / 14-25 / 26-37 / 38-49), edited in isolated worktrees, and the
commits were cherry-picked in (clean — disjoint regions). Each folded entry keeps a compact
`Validation (2026-06-05, folded)` marker pointing here.

**Method**: for each flagged entry — delete/correct the bullets stating a figure the audit found
unsupported; keep and re-source the supported claims; re-tier honestly (A only if a production/peer-
reviewed result whose *retained* claims are actually in the source; B for analyst/vendor-methodology or
where the production *metric* was the unsupported part; C for vendor self-claim with no methodology).

**Headline**: Evidence-Level-A dropped **64% → 46%** (90/141 → 65/141; now 65 A / 76 B / 9 C). ~25 entries
moved off A because their headline statistic was not in the cited source (real source, wrong/absent number)
— the classic MISMATCH pattern. This is the honest baseline; the gap to the 75% target is now visible
rather than masked by self-reported numbers. Representative re-tiers: ClickHouse Vectorized/IP/Compression
A→B (conceptual pages publish no benchmarks); Kafka-Confluent + Netflix-Tiered-Storage A→B (vendor
benchmark / figure needs a separate primary cite); Google-SRE / Gartner-Reliability A→B and Uptime-
Institute A→C (placeholder/unfindable stats); Gravitino + Gartner-AI-Maturity A→B, Tenzir + AI-Multiple
→C (vendor self-claim). Kept A: DORA, LinkedIn-Northguard, Huntress, Arrow-Flight-SQL, SK-Telecom,
Amazon-Security-Lake, Iceberg-Universal-Support, Hyperscan (USENIX NSDI'19, peer-reviewed).

Net: 0 verbose notes remain; 49 folded markers. The MISMATCH/WEAK worklist from the earlier passes is now
resolved in-prose, not just correction-noted.

---

## 2026-06-05 (freshness increment) — the two DEAD entries, re-sourced + reframed

Started the freshness sweep (Phase 3) on the two entries the earlier passes left DEAD. **Method**: WebSearch
to confirm the candidate sources exist and to read their stated figures (WebFetch 403s on these publishers —
see limitation below), then `claim↔source` against the search result.

| Entry | Verdict | Finding |
|---|---|---|
| Flink at Uber — Real-Time Security Analytics | RE-SOURCED + RETITLED | Original eng.uber.com URL dead. The live Confluent Current 2025 session ("Inside Uber's Large-Scale Real-Time Analytics Platform") confirms the scale figures (trillions msgs/dozens-PB daily, 10s-of-thousands queries/sec, several-M writes/sec, tens-of-PB Pinot; IngestionNext = Kafka+Flink+**Hudi**, latency hours→min, ~25% less compute — corroborated by InfoQ Mar-2026). BUT it is Uber's **general** analytics platform (EVA), not a security deployment. Retitled "Uber — Real-Time Analytics Platform"; dropped the unverifiable security framing; kept A (production platform, public talk with figures). |
| Disney+ Real-Time Security Analytics | RE-SOURCED + RETITLED + A→B | Original Disney Streaming Medium "security analytics" article 403/gone, claims unverifiable. Re-pointed to Kai Waehner's Disney+ Hotstar/JioCinema case study (Feb 2025): ~15 Kafka Connect clusters / 2,000+ connectors / millions msgs/sec / SMT for PII-masking+schema-validation — figures trace to a Kafka Summit 2021 Hotstar talk. It's a **general media streaming** pipeline (PII-masking is the only security-adjacent bit), and a Confluent-aligned expert's secondary write-up, not a primary security source → re-tiered A→B. |

Net Level-A 46% → 45% (65→64 A; Disney downgrade). 2 DEAD entries resolved (0 DEAD remain from the journal's list).

**⚠️ Environment limitation for the sweep**: `WebFetch` returns **403** on many publisher domains
(Confluent, kai-waehner.de, d3fend.mitre.org, anthropic.com…) — bot-blocking, not dead pages. `WebSearch`
works and surfaces the stated figures, so claim↔source verification is possible via search excerpts, but
direct full-page fetch is not. A complete freshness sweep of the remaining ~90 stale entries should plan
around this: prefer WebSearch + archive.org, or run the sweep from an environment/tool that can fetch
these pages, rather than treating a 403 as a dead link (the link checker already encodes this distinction).

---

## 2026-06-05 (freshness sweep continued + 2026 primary sourcing) — tasks #66/#67

**Method**: WebSearch to surface candidate 2026 primary sources and confirm their existence/dates;
WebFetch on the pages that allow it (AWS Open Source Blog, ocsf-schema GitHub releases, iceberg.apache.org,
clickhouse.com docs) to confirm the specific claim; `claim↔source` against the search/fetch result.

### Added — new Tier-A 2026 primary sources (claim↔source VERIFIED at insertion)

| Entry | Method | Finding |
|---|---|---|
| Apache Iceberg 1.11.0 | claim↔source (WebSearch + WebFetch iceberg.apache.org/releases) | Released 2026-05-19; the release that stabilizes V3 features (deletion vectors, Variant, geospatial, ns timestamps) from experimental to default; confirmed across Google OSS Blog + Dremio + Snowflake (v3 GA 2026-05-07). A. |
| OCSF Achieves ITU Support | claim↔source (WebFetch of the AWS post) | AWS Open Source Blog, Rod Wallace, 2026-03-24; ITU member states unanimously supported OCSF (Dec 2025) for ratification as an ITU x.*** international standard by June 2026; corroborated by DevOps.com republication. A (standards-body milestone). |
| MITRE D3FEND for OT | claim↔source (WebSearch) | MITRE news release 2025-12-16; OT extension shipped in the D3FEND v1.3.0 line (267 techniques, 7 tactics); OWL 2 DL. A. |
| OCSF v1.8.0 (existing entry refined) | link (WebFetch GitHub releases) | v1.8.0 tag = 2026-03-18 confirmed (cadence v1.6.0 2025-08-01 / v1.7.0 2025-11-14 / v1.8.0 2026-03-18); date precision tightened. |
| MITRE D3FEND base (existing, refined) | claim↔source (WebSearch) | v1.0 launch 2025-01-16 + v1.3.0/OT Dec 2025 confirmed; prior "v1.4.0 line" annotation NOT reconfirmed in this pass → version-line flagged for a changelog check. |

### Fixed — freshness sweep

| Entry | Verdict | Finding |
|---|---|---|
| ClickHouse — Performance Optimization Guide | RE-SOURCED (broken link) | `/docs/guides/best-practices/query-optimization` returned 404 (docs path reorganized); re-pointed to `/docs/optimize/query-optimization` (WebFetch-confirmed live, "A simple guide for query optimization"). Tier flagged: vendor docs usually B, kept A pending Jeremy. |
| 14 stale-but-verified entries | ANNOTATED | Publication date >12mo, content-current per this journal's VERIFIED/re-sourced rows, but lacking an inline 2026 marker. Each now carries a compact `Freshness (2026-06-05)` note pointing to its journal disposition (e.g. Cloudflare ClickHouse, Azure-Kafka, DuckDB-Overview, Cloudera-Impala+Iceberg, Iceberg-Foundation, ClickHouse-vs-ES, CISA, OCA, Confluent-ML, GitLab, ClickHouse-vs-Snowflake, Netflix-5PB, Hunters, Brooks). No >12mo entry is now un-annotated. |

Net (this pass): entries 141 → 144; Level-A 64/141 (45.4%) → 67/144 (46.5%). 0 broken links remain.
Health check: CRITICAL → WARNING (still ESCALATEs on the intentional 60% floor breach + monthly window).

---

## 2026-06-09 — Bridge framing sources (conceptual anchors; no quantitative claim catalogued)

Added the two framing sources the applied-bridge positioning rests on, which the corpus lacked. These ground *framing*, not numbers — neither carries a headline statistic, so neither is exposed to the stat-mismatch audit. Both verified at insertion via WebSearch (publisher + author listings).

| Entry | Method | Finding |
|---|---|---|
| Fundamentals of Data Engineering (Reis & Housley) | claim↔source (WebSearch: O'Reilly + Amazon/Google Books) | O'Reilly Media, published 2022-07-26, ISBN-13 978-1098108304; the **data-engineering lifecycle** (generation/storage/ingestion/transformation/serving) confirmed as the book's central framework. **Tier B** (authoritative practitioner book; A reserved for peer-reviewed/standards). Grounds the bridge's *inclusion* move ("you're already doing data engineering"). Filed under Foundational Architecture → Data Engineering Foundations. |
| The Data-Centric Revolution + Incremental Stealth Legacy Modernization (McComb) | claim↔source (WebSearch: TDAN.com + Semantic Arts + Technics Publications) | Dave McComb (Semantic Arts); *The Data-Centric Revolution* (Technics, 2019) for the single extensible/data-centric model, and "Incremental Stealth Legacy Modernization" (TDAN.com column + named Semantic Arts method) for the gradual, no-green-light migration path. **Tier B** (conceptual framing, no statistic). Grounds the bridge's two *relief* moves — compose-don't-build + incremental-not-big-bang. Filed under Implementation & Organizational → Change Management. |

Net (this pass): entries 144 → 146; Level-A held at 67 (67/146 = 45.9% ≈ 46% as the denominator grew); +2 Tier-B (77 → 79 B). 0 broken links added (both URLs WebFetch/WebSearch-live at insertion). Rationale: the realigned securitydataworks.com/thesis publicly links this repo as its evidence backbone, and a reader following that link should find the foundational citations for the framing they just read.

---

## 2026-06-21 — Program-2 M0/M1: live-citation fabrication audit + detection-engineering / grounding-chain sources

**Scope**: the ATT&CK→D3FEND-over-OCSF through-line (Program 2). **M0** is a fabrication audit of two sources
*already cited in deployed/public content* but never catalogued here — Stefan Axelsson's *Base-Rate Fallacy*
(2000) and Sommer & Paxson's *Outside the Closed World* (2010) — checking whether the public paraphrases
accurately represent the papers. **M1** adds the nine detection-engineering / grounding-chain anchors the
through-line rests on. **Method**: `claim↔source` for the live paraphrases (compared the deployed prose
against the papers' central arguments); `cross-ref` + DBLP/WebSearch metadata verification for the catalogued
sources; no full-page WebFetch needed for the canonical papers (DBLP metadata + my knowledge of these
foundational works are authoritative — ACM DL/IEEE pages 403 to automated fetch, the standing environment
limitation noted in the 2026-06-05 sweep).

### M0 — live-citation fabrication audit (VERDICT: both public paraphrases accurately represent their sources)

The two paraphrases are cited live in **two surfaces each**: the private evidence note
`project1/02-projects/d3fend-wall/AIML-RIPENESS-EVIDENCE.md` and the **deployed** essay
`securitydataworks/src/pages/research/d3fend-wall.astro` (public on securitydataworks.com). Both checked
against the source:

| Source | Surface(s) audited | Method | Verdict |
|---|---|---|---|
| Axelsson, *The Base-Rate Fallacy and the Difficulty of Intrusion Detection* (TISSEC 2000) | AIML-RIPENESS-EVIDENCE.md:90 ("because genuine intrusions are vanishingly rare against benign volume, the false-positive rate against the base rate, not the true-positive rate, caps usable detection … the formal backbone of alert fatigue") + d3fend-wall.astro:371-374 ("Axelsson named the arithmetic underneath it … in 2000, the base rate … even a tiny false-positive rate buries the analyst, so the number that binds is the false-positive rate against the base rate and not the headline accuracy") | claim↔source (paraphrase vs. the paper's central Bayesian-posterior argument) | **VERIFIED — accurate.** Faithful to the paper's core claim; correct year (2000); correct mechanism (P(intrusion\|alarm) stays low because of the base rate). No overstatement, no fabricated statistic or quote. |
| Sommer & Paxson, *Outside the Closed World: On Using Machine Learning for Network Intrusion Detection* (IEEE S&P 2010) | AIML-RIPENESS-EVIDENCE.md:89 (enumerates all five arguments — ML finds similar-not-novel so anomaly detection inverts its strength; extreme asymmetric error cost; semantic gap; no stable normal; evaluation near-impossible for lack of labeled data — plus "narrow scope + human in loop" and "2020 IEEE S&P Test-of-Time Award") + d3fend-wall.astro:369-371 ("reasons on the record since Sommer and Paxson's 2010 paper that later won a test-of-time award … a model is good at finding what resembles its training data, but detection has to find the novel attack, which inverts the strength, and there is no stable normal to learn") | claim↔source (paraphrase vs. the paper's five arguments + recommendation) | **VERIFIED — accurate.** Every enumerated point is in the paper; the inverted-strength and no-stable-normal compression in the essay is faithful; the award year (2020) is correct and the essay's "later won a test-of-time award" is true and appropriately unspecified. No fabrication. |

**M0 result**: no fabrication found. Both public paraphrases (including the *deployed* d3fend-wall essay)
accurately represent their sources — no invented statistic, quote, mechanism, or date. The only integrity
gap was that two papers cited in live public content were **un-catalogued** in this bibliography; M1 closes
that breach by adding both with full provenance.

### M1 — added (Program-2 detection-engineering / grounding-chain anchors)

| Entry | Tier | Method | Finding |
|---|---|---|---|
| Axelsson, *Base-Rate Fallacy* (TISSEC 2000) | A | cross-ref (DBLP journals/tissec/Axelsson00) | Author Stefan Axelsson, ACM TISSEC vol.3 no.3 pp.186-205, 2000, DOI 10.1145/357830.357849; earlier CCS-1999 version provenance accurate. Filed under Academic & Peer-Reviewed. Closes a live-citation breach (see M0). |
| Sommer & Paxson, *Outside the Closed World* (IEEE S&P 2010) | A | cross-ref (DBLP conf/sp/SommerP10) + WebSearch (award) | Authors Robin Sommer & Vern Paxson, IEEE S&P 2010 pp.305-316, DOI 10.1109/SP.2010.25; 2020 IEEE S&P Test-of-Time Award corroborated via ICSI Berkeley + ieee-security.org SP2020 awards page. Filed under Academic & Peer-Reviewed. Closes a live-citation breach (see M0). |
| MITRE Cyber Analytics Repository (CAR) | B | knowledge + cross-ref | Real long-standing ATT&CK-program project (car.mitre.org, github.com/mitre-attack/car, Apache-2.0); analytics carry ATT&CK technique mappings + pseudocode + reference impls against the CAR Data Model. No analytic count asserted — flagged to confirm at primary. Filed under Frameworks & Standards. |
| Red Canary Atomic Red Team | B | knowledge + cross-ref | Real widely-used Red Canary OSS project (github.com/redcanaryco/atomic-red-team, MIT); per-technique atomic tests in YAML mapped to ATT&CK + the Invoke-AtomicRedTeam runner. No test-count/GUID asserted. Filed under Frameworks & Standards. |
| MITRE D3FEND 1.0 (ontology) | A | WebSearch | 1.0 launch 2025-01-16 (research→production ontology); OWL 2 DL; D3FEND Core Classes = upper-ontology alignment interface; Kaloroumakis project lead confirmed. Consistent with the existing "MITRE D3FEND Framework & Ontology" entry (same version line); this is the milestone-specific grounding-chain anchor. CCO mapping flagged as in-progress, not shipped-complete. Filed under Frameworks & Standards. |
| BFO — ISO/IEC 21838-2:2021 | A | WebSearch + ISO catalogue | Standard 21838-2, Part 2 = BFO, published Nov 2021, standardizes the BFO 2020 release (Barry Smith et al.). Version trap flagged: "BFO 2020" (ontology) ≠ "21838-2:2021" (standard date). ISO landing 403s to fetch; number/title/date corroborated via ISO catalogue + BFO-2020 GitHub + bfo-discuss. Filed under Frameworks & Standards. |
| Common Core Ontologies (CCO) | B | WebSearch | CUBRC, Inc. origin under IARPA funding; openly available since 2017; BFO-aligned mid-level suite; arXiv:2404.17758 descriptive paper (Jensen et al.). Tier B not A — proposed candidate standard mid-level ontology, NOT an adopted ISO/IEC standard the way BFO is (flagged so prose can't borrow BFO's standards-tier authority). Filed under Frameworks & Standards. |
| Ryan Stillions — DML (Detection Maturity Level) Model | C | knowledge + cross-ref | Real, community-canonical 2014 detection-engineering blog model (ryanstillions.blogspot.com); nine-level DML-0..DML-8 abstraction ladder. Tier C — single-author blog, not peer-reviewed. No statistic invented; level-count kept to the documented 0-8 range. Canonical URL not live-fetched this session — confirm before publication-grade cite. Filed under Practitioner Publications. |
| SCYTHE — Purple Team Exercise Framework (PTEF) | C | knowledge + cross-ref | Real named purple-team methodology (github.com/scythe-io/purple-team-exercise-framework); Orchilles/Bort/Peacock real practitioners (Orchilles also SANS author on adversary emulation). Tier C — vendor-published (incentive flagged). No statistic/version-date beyond ~2020 v1 invented. Confirm GitHub URL live before publication-grade cite. Filed under Practitioner Publications. |

### Unconfirmed / flagged

- **None rejected.** All nine sources are real and pre-cutoff. Three carry "confirm at primary before
  publication-grade citation" flags (the canonical-URL line not live-fetched this session): the Stillions
  Blogspot post, the SCYTHE PTEF GitHub page, and the ISO 21838-2 landing page (403s to automated fetch —
  number/title/date corroborated via the ISO catalogue, the BFO-2020 GitHub repo, and the bfo-discuss
  announcement rather than the landing page itself). No count, GUID, DOI, page number, or quote was invented
  for any entry; CAR/Atomic Red Team/SCYTHE deliberately assert no coverage count.

Net (this pass): catalogued entries 159 → 168; +4 Tier-A, +3 Tier-B, +2 Tier-C (recompute live A% via
`scripts/weekly_health_check.py` — the header narrative carries the running estimate). The M0 audit found
no fabrication in the live/deployed paraphrases; the integrity action was cataloguing two already-public
citations that had been un-recorded here.

---

*Next validation due with the cadence (`SCHEDULING.md`). When the worklist items above are re-sourced or
stripped, append a dated row moving each to VERIFIED or removing it — do not silently re-litigate settled rows.*
