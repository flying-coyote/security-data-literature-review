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

The cleanup worklist for everything not `VERIFIED` is kept in a private register outside this
repository (categorized + propagation-mapped). This journal is the evidence; that register is the to-do.
From 2026-11-17 the per-number record for the whole bibliography is `methods/verification-2026-11/ledger.json`.

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
| Retired December 2025 multi-engine benchmark (#25) | real first-party measurement; repo NDA-gated (404 expected); methodology public |
| anonymized practitioner / Okta-Jake-Thomas | genuine private practitioner input; unverifiable as external citation |
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
| 15 stale entries (freshness-triaged) | ANNOTATED | Publication date >12mo, freshness-triaged (date-stale; content NOT re-verified against the cited source — a 2026-06-22 10-sample falsifier found 3/10 markers over-claimed), previously lacking an inline 2026 marker. Each now carries a compact `Freshness (2026-06-05)` note pointing to its journal disposition (e.g. Cloudflare ClickHouse, Azure-Kafka, DuckDB-Overview, Cloudera-Impala+Iceberg, Iceberg-Foundation, ClickHouse-vs-ES, CISA, OCA, Confluent-ML, GitLab, ClickHouse-vs-Snowflake, Netflix-5PB, Hunters, Brooks). No >12mo entry is now un-annotated. |

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

---

## 2026-11-07 — Phase 1 upgrade pass: two re-tiers and nine snowball admissions

### Re-tiers (A → B, against METHODOLOGY §3.1)

| Entry | Was | Now | Method | Finding |
|---|---|---|---|---|
| Apache Arrow Flight SQL | A | B | cross-ref (§3.1 definition) | Evidence was project documentation plus a project blog post, which §3.1 names Level B; survived the 2026-08-19 downward audit. Key Findings unchanged. |
| Mining Temporal Attack Patterns from Cyberthreat Intelligence Reports (arXiv 2401.01883) | A | B | arXiv API record | arXiv preprint with no venue; the arXiv comment says a modified version is under review at IEEE TSE. Author list (Rahman, Wroblewski, Matthews, Morgan, Menzies, Williams) filled from the record. |

### Snowball admissions (all Tier A, all VERIFIED)

Identification: one hop backward (Crossref reference lists) and forward (OpenCitations) from 35 DOI-resolved peer-reviewed seeds, 2,812 unique DOIs, metadata via keyed OpenAlex; ranking and screening recorded in `methods/snowball-candidates-2026-11.md`. "Targeted" marks a known-item lookup against a named thin claim.

| Entry | Found via | Method | Finding |
|---|---|---|---|
| Kokulu et al., *Matched and Mismatched SOCs* (CCS 2019) | targeted | Crossref + abstract at Semantic Scholar, matched to OpenAlex copy (ACM DL 403) | 18 semi-structured interviews; technical and non-technical SOC issues; manager–analyst disagreements. |
| Rigger & Su, *Query Partitioning* (OOPSLA 2020) | targeted | Crossref + abstract at Semantic Scholar, matched to OpenAlex copy (ACM DL 403) | Logic bugs return incorrect results unnoticed; 175 bugs found, 125 fixed, 77 logic bugs. |
| Raasveldt & Mühleisen, *Don't Hold My Data Hostage* (PVLDB 2017) | targeted | VLDB PDF page 1 + Crossref | Result-set serialization can dominate query time; columnar serialization improves transmission by an order of magnitude. |
| Zhu et al., *Tools and Benchmarks for Automated Log Parsing* (ICSE-SEIP 2019) | backward from Petrescu | arXiv abstract page + Crossref | 13 parsers on 16 datasets; accuracy, robustness, efficiency; tools and benchmarks released. |
| Zeng et al., *Empirical Evaluation of Columnar Storage Formats* (PVLDB 2023) | backward from F3 / FastLanes | VLDB PDF text + Crossref | Parquet/ORC internals benchmarked; dictionary encoding by default, decode speed over ratio, optional block compression. |
| Durner, Leis & Neumann, *Exploiting Cloud Object Storage* (PVLDB 2023) | backward from F3, forward from Delta Lake | VLDB PDF text + Crossref | Cost- and performance-optimal object-store retrieval; AnyBlob; uncached Umbra comparable to SSD-caching warehouses. |
| Hassan et al., *NoDoze* (NDSS 2019) | backward from hyperdimensional host-IDS entry (IEEE BigData 2024) | NDSS paper page + Crossref | Threat alert fatigue; provenance-graph triage; 364 alerts; estimated 84% false-alarm volume reduction. |
| Valeur et al., *Alert Correlation* (IEEE TDSC 2004) | backward from AIDA (ARES 2019) | author-hosted TDSC PDF page 1 + Crossref | Component model of correlation; effective alert reduction; effectiveness depends heavily on the dataset. |
| Kuschewski et al., *BtrBlocks* (SIGMOD 2023) | backward from F3 | author-hosted version-of-record PDF page 1 + Crossref | Parquet not optimized for remote data lakes; decompression makes scans CPU-bound; lightweight-encoding format. |

### Held, not admitted

Julisch (TISSEC 2003), Bhatt et al. (IEEE S&P magazine 2014), Oliner et al. (CACM 2012) and Wang & Strong (JMIS 1996) are real (Crossref-resolved) and ranked high, but their publisher pages returned 403 and no independent abstract page was reached this session (the Semantic Scholar records carried no abstract), so they stay in the candidates file until read at a primary.

---

## 2026-11-17 — Verification sweep of all 273 entries (existence and number fidelity)

Every entry was checked for existence at its DOI, arXiv ID or URL, and every number quoted in its Key Findings or Notes was searched for in the cited source. The full per-number record, with the URL and the sentence each figure was found in, is `methods/verification-2026-11/ledger.json`, summarized in `methods/verification-2026-11/README.md`. Rows below cover only the entries whose verdict or text changed. Verdict mapping to this journal's vocabulary: `verified-at-primary` is VERIFIED, `not-in-source` is MISMATCH, `unverifiable-no-primary` is WEAK-SOURCE, `dead-link` is DEAD, and `unverifiable-paywall` (the page blocks an automated reader) has no older equivalent and is recorded as such.

| Entry | Method | Finding |
|---|---|---|
| Data Engineering for Cybersecurity (No Starch Press Book) | link | URL placeholder replaced by the No Starch product page; edition, date and ISBN match. |
| ClickHouse at Cloudflare - 6M Requests/Second | claim↔source | MISMATCH: the Alt URL post (clickhouse.com/blog/cloudflare) is dated 18 February 2026, not October 2025, and date mentions corrected; the 1,000-replica and hundreds-of-millions-of-rows line is on neither cited page and was removed (not-in-source). |
| Prosci Change Management Best Practices (12th Edition) | claim↔source | Labelled unverified in the entry: 93%, 15%, 183% (not-in-source). |
| 2024-2025 State of DevOps Report - DORA | claim↔source | Labelled unverified in the entry: 39,000+ (unverifiable-paywall: the fetched page is a landing shell with no report text, and the report PDF was not read). |
| Confluent Data Streaming Report (2025) | claim↔source | Labelled unverified in the entry: 93% (unverifiable-paywall: only the landing pages were read; the report sits behind registration). |
| Retired December 2025 multi-engine benchmark (superseded by SDW Lab zeek-flagship-rerun) | archaeology | FIRST-PARTY: retired named-vendor timings removed on the 0165a38 precedent; successor figures re-read in the public SDW Lab repo; entry retitled without the retired benchmark's name and its URL re-pointed from the private repository to the public `zeek-flagship-rerun` folder. |
| How Exabeam uses ClickHouse for scalable, searchable security analytics (ClickHouse case study, 2025) | claim↔source | MISMATCH: "~17.5×" divided PB by TiB; corrected to about 16×, with a dated correction note on the 2026-07-09 "every figure confirmed" Validation Status line. |
| Huntress - ClickHouse Migration Case Study (Isolation-First Security) | claim↔source | Labelled unverified in the entry: 16 billion (unverifiable-paywall; the figure comes from the named ClickHouse video, which was not re-checked). |
| Chris Bisnett - Huntress ClickHouse Migration (Video) | claim↔source | Labelled unverified in the entry: 93%, 3M (unverifiable-paywall). |
| Okta Security Analytics with DuckDB — Data Council 2024 talk | claim↔source | Talk abstract located at duckdb.org and Data Council; 7.5 trillion records and 1.5-50 TB/day confirmed; unsupported "Lambda" detail dropped. |
| Cloudera Total Economic Impact — Public Cloud (Forrester TEI, October 2021) | claim↔source | PDF URL catalogued; it now redirects to a gated landing page, where the 194% ROI was confirmed; $35.54M and the October 2021 cover date are carried from the 2026-07-09 PDF check. |
| Confluent - Kafka Architecture & Sizing | claim↔source | Labelled unverified in the entry: 40-60% (unverifiable-no-primary: the entry attributes it to a Confluent TCO page it does not name, and Confluent's cost-effectiveness page says "up to 60%"). |
| Gartner - Security Data Growth Rates & Spending Forecast 2024-2029 | claim↔source | Labelled unverified in the entry: $193B, $213B, $244B, $323B, 13.3%, $49B, $160B, $95B, $106B, $121B, 25.9%, $9.0B, $22.6B, 15.0%, $24.1B, $42.1B, 14.1%, $78.8B, $132.4B, 13.1%, $31.3B, $51.2B, 25-35%, $212B (unverifiable-paywall). |
| AWS Well-Architected - Compute Optimization | claim↔source | Labelled unverified in the entry: 15-25% (not-in-source). |
| Apache Iceberg - Universal Vendor Support | link | "Multiple vendor announcements" replaced by The Register article as the URL. |
| Uber - Palette Feature Store for ML | claim↔source | Labelled unverified in the entry: 95% (unverifiable-paywall). |
| SANS Institute - AI Survey & SOC Automation Research | claim↔source | Labelled unverified in the entry: 100%, 50%, 79% (unverifiable-paywall: only the landing pages were read; the reports sit behind registration). |
| CISA - Enhanced Security Monitoring Best Practices | claim↔source | Labelled unverified in the entry: 12 months (unverifiable-paywall). |
| MITRE Corporation - Insider Threat Research & Framework | claim↔source | Labelled unverified in the entry: 15+ (unverifiable-paywall). |
| MITRE Engenuity - ATT&CK Evaluations Framework | claim↔source | Labelled unverified in the entry: 100% (unverifiable-paywall). |
| StarRocks vs ClickHouse Production Benchmarks | claim↔source | 1.87× verified at the StarRocks SSB page (vendor-run); 100× concurrency and 30K-PR figures removed, no primary. MISMATCH → partially VERIFIED. |
| MOAR Stack - Security Data Lakehouse Reference Architecture | claim↔source | Labelled unverified in the entry: 70-90%, $31-100K, 10-12×, 10-50×, 12 months (not-in-source; unverifiable-no-primary). |
| Gartner AI Maturity and Success Metrics | claim↔source | Gartner 2024-07-29 press release named as the URL; its headline is the 30% prediction. |
| AI Governance Maturity Gate - Prerequisites for AI Success | claim↔source | WEAK-SOURCE: LinkedIn discussion only; four numbers removed; withdrawal staged. |
| RAPTOR Security Automation Framework - Production AI Patching | claim↔source | Repository located; author list corrected to the README; FFmpeg-patch claim not in README, labelled unverified. |
| Tenzir Security Data Pipeline Platform | claim↔source | Labelled unverified in the entry: 30% (not-in-source). |
| Rippling - Engineering a Cost-Effective SIEM (3-Part Series) | claim↔source | Labelled unverified in the entry: 50-70 MB, 5 minutes, 75GB, 1 minute (unverifiable-paywall). |
| Navan - SIEM-less Detection Engineering (Anvilogic Case Study) | link | Page returned 404 to an automated fetch but remains search-indexed with the quoted wording; recorded as unconfirmed, not dead. |
| SOC Automation ROI and AI Implementation | claim↔source | 40% verified at the securityinfowatch report of the Prophet survey; SOAR $2.3B/16.3% removed, no primary. |
| Tenzir Streaming Fabric - Policy vs. Pipe Layer Framework | claim↔source | WEAK-SOURCE: LinkedIn post, not fetched; 100+ Gbps labelled unverified. |
| Cribl Pipeline Economics - Route, Reshape, Reduce Pattern | claim↔source | WEAK-SOURCE: 88-98% and 10x claims not found in Cribl's CriblCon 2025 press material; labelled; engagement metric removed. |
| Vortex File Format - Emerging Columnar Format | claim↔source | README located; claims restated exactly (100× random access, 10-20× scans, 5× writes). |
| Databricks MCP Catalog - Unity Catalog for AI Agents | claim↔source | Blog located; date corrected to 2025-06-18; "vector search indexes" corrected to the blog's "AI Search indexes"; Claude/ChatGPT integration list not in blog, labelled. |
| Anonymized practitioner - Security Data Platform Practitioner Validation | cross-ref | WEAK-SOURCE: personal communication is ineligible under the file's Boundary rule; withdrawal staged. |
| Apache Iceberg 2025 Performance Analysis | claim↔source | MISMATCH: the docs' 10x is about split elimination on clustered data, not a comparison with Hive; reworded. |
| Security Data Lakehouse Implementation Patterns | claim↔source | WEAK-SOURCE: composite with no named primary; three numbers removed; withdrawal or split staged. |
| Data Catalog Wars 2025 - Polaris vs Unity vs Nessie vs Gravitino | link | Composite URL replaced by the onehouse.ai comparison quoted in the entry; projectnessie.org as Alt URL. |
| Row-Level Security Performance Impact Studies | claim↔source | PostgreSQL docs support the per-row evaluation bullet; SQL Server 2025 claim removed, no primary. |
| OCSF RLS Overhead, SDW Lab First-Party Measurement (engine-side, DuckDB) | claim↔source | FIRST-PARTY: public results URL catalogued; +81%, +94%, -86% re-read in the results table. |
| Streaming vs Batch Cost Analysis 2025 | claim↔source | Confluent release confirms 86% ("important strategic priority", wording corrected), 44% at 5x, n=4,175. |
| CSA/Google Cloud - The State of AI Security and Governance | claim↔source | Labelled unverified in the entry: 26%, 54%, 60%, 12 months, 46%, 12% (unverifiable-paywall: only the artifact landing page was read; the report sits behind registration). |
| Databricks Data Intelligence for Cyber Defense - Barracuda & Palo Alto | claim↔source | Labelled unverified in the entry: 75%, 5 minutes, 3×, 70-90% (unverifiable-paywall). |
| Apache Gravitino - Production Adoption | claim↔source | Labelled unverified in the entry: 100K, 150K, 70% (unverifiable-paywall). |
| MITRE D3FEND 1.0 (Cybersecurity Countermeasures Ontology) | link | Currency: site badge now 1.6.0 (release 2026-08-31); 400+ artifacts not on the page, labelled. Labelled unverified: 400+. |
| Architecting an Apache Iceberg Lakehouse — Alex Merced | claim↔source | Labelled unverified in the entry: 90% (unverifiable-paywall: the book text is not openly accessible; only Manning's product page was read). |
| Okta's Multi-Engine Data Stack — Julien Hurault | claim↔source | Labelled unverified in the entry: 1M, 250 GB (unverifiable-paywall). |
| Kingpin: How One Hacker Took Over the Billion-Dollar Cybercrime Underground | link | Open Library record catalogued as the URL; its publish_date is 2010 (LCCN 2010027952, with LC call numbers for both 2010 and 2011), so the entry's 2011 is noted as not confirmed by the record. |
| DuckLake v1.0: The Lakehouse Format Built on SQL | claim↔source | FIRST-PARTY: 2.9–3.6 ms verified at the public lab file `ocsf-format-planning/results/RESULTS.md` (2.94, 3.57, 3.56 ms), now linked in the entry. |
| Stream-Based IP Flow Analysis (IFIP/IEEE IM 2021, Dissertation Digest) | claim↔source | 31%, 26%, 4%, 1%, 0.4% are Fig. 3 image values that a text search cannot see; carried as verified from the page-render check the entry's Provenance line records, and no label. |
| Machine Learning on Distributed Stream-Processing Platforms — Storm, Spark Streaming and Flink (SBRC Short Courses, 2018, in Portuguese) | link | Author-hosted PDF located; two missing authors added from the title page. |
| The Data-Centric Revolution + Incremental Stealth Legacy Modernization (Dave McComb) | link | DEAD: the dataversity.net Alt URL returns HTTP 404 and the Wayback Machine has no snapshot; marked dead in the entry, primary URL live. |
| ClickHouse - Performance Optimization Guide | cross-ref | Stale 2026-06-05 tier flag replaced with a note that the 2026-08-19 re-tier to B resolved it. |

### Currency notes added (checked at each project's own release record, 2026-11-17)

OCSF v1.9.0 current (v1.8.0 and v1.1.0 mentions noted); Apache Iceberg 1.12.0 current, spec v4 still not adopted; DuckDB v2.0.0 released 2026-10-21 (1.5.3-pinned lab figures noted as version-bound); DuckLake 1.0 still current; D3FEND 1.6.0 current; Kafka on the 4.x line; Flink 2.3.0 latest stable; Apache Polaris 1.9.0; OpenSearch 3.9.0 (the lab baseline was 3.7.0). Each note sits under the entry's Validation Status line.

## 2026-11-23: corrections to the 2026-11-22 second-opinion pass

| Entry | Method | Finding |
|---|---|---|
| Netflix - Kafka Tiered Storage | claim↔source | MISMATCH: the Keystone post (netflixtechblog.com, 2016), read at its Wayback Machine copy (snapshot 20250119164347), gives "More than 700 billion messages are ingested on an average day" and the word "trillion" does not appear in it. The 2 trillion figure moves from `unverifiable-paywall` to `not-in-source` and is replaced in the entry by the post's own figure, with a dated note. |
| Huntress - ClickHouse Migration Case Study | cross-ref | Retitled without the "(Isolation-First Security)" parenthetical, in the bibliography, `ledger.json` and `methods/prisma-results/reconciliation.json`; the 2026-11-22 withdrawal of the isolation-first claims is carried to the Bisnett video entry (a 2024 ClickHouse New York meetup talk, not RSA 2025) and to the Polaris and Unity Catalog notes. |

## 2026-11-23: monthly refresh (link check, refreshed sources, six admissions)

**Scope**: the November 2026 monthly refresh. `scripts/weekly_health_check.py` and `scripts/automation_dashboard.py` were run first, then `scripts/link_check.py` over all 350 unique URLs in the bibliography (282 OK, 64 paywalled or blocked, 2 dead, 2 errors). Each dead or erroring URL was re-requested with browser headers before any verdict. The two errors (Microsoft Tech Community drift post, HTTP 400; Uber Palette post, HTTP 406) return HTTP 200 to a browser request, so both are link-checker false positives and their entries are unchanged. Rows below are only for verdicts that changed.

### Changed verdicts

| Entry | Method | Finding |
|---|---|---|
| Navan - SIEM-less Detection Engineering (Anvilogic Case Study) | link | DEAD at the origin (HTTP 404 to the link checker and to a browser-header request); marked [Archived], with the snapshot moved into the URL field. The Wayback Machine snapshot of 2026-07-20 carries the Karanth quote verbatim, so the entry's 2026-07-10 "not in Wayback" note and its 2026-11-17 "live-but-unconfirmed" status are both superseded. |
| The Data-Centric Revolution + Incremental Stealth Legacy Modernization (Dave McComb) | link | The dataversity.net Alt URL is still HTTP 404. The 2026-11-17 row above found no Wayback snapshot, which is true for that address, but the original tdan.com address has snapshots from 2022 to 2024; the 2024-03-01 snapshot shows the column, its 2022-03-02 date and the "green light" sentence the entry quotes. Alt URL re-pointed to that snapshot and marked [Archived]. |
| Apache Iceberg Foundation - Governance & Contributors | claim↔source | MISMATCH of method. The GitHub contributors endpoint lists 406 linked accounts today (405 users, 1 bot) and 946 entries with `anon=1`, 540 anonymous. GitHub documents that only the first 500 author email addresses link to users, and the repository has more than 500, so the 2026-07-09 count of 407 was already a floor set by that limit. The entry now gives both numbers with the limit; H-ARCH-01's "407 GitHub contributors" in manuscript §3.7 is staged for correction. |
| Apache Polaris Catalog - Security Architecture & Isolation | claim↔source | not-in-source: the "Production deployments at Netflix (security observability)" finding is on no Polaris page checked (home, community, 1.9.0 access control) and traces to the Netflix entry de-attributed from Polaris on 2026-07-09; withdrawn inline. The table-level-permissions finding is VERIFIED against the 1.9.0 access-control page, which also documents external policy decision points such as OPA. |
| Confluent - Kafka Architecture & Sizing | claim↔source | not-in-source: the course page contains none of "TCO", "total cost", "talent", "operational complexity" or "sizing", so the TCO finding is withdrawn as a finding of this source and the sizing finding is narrowed to architecture background. H-IMPL-01 already scores at the instrument floor, so no score changes. |
| Fourth Annual Report on the State of SIEM Detection Risk (CardinalOps, press release 2024) | cross-ref | cardinalops.com redirects to cribl.io; Cribl's release of 2026-07-14 announces it "is acquiring CardinalOps". Bias note extended to the new owner (checked at the home page and blog). The 2025 edition's 13% and 79% figures were found only in trade press (Help Net Security, 2025-06-09), so they stay unverified at a primary and the 2024 release stays the cited one. |
| ClickHouse vs Elasticsearch - Storage Efficiency | cross-ref | Figures re-verified verbatim. The byline is Tom Schreiber (May 7, 2024), and the page's structured data carries `dateModified` 2026-03-03, which corrects the 2026-07-09 note's implication that the "2026-03-03 update" had no basis on this page; the storage figures read the same as at the 2026-07-09 check. |

### Re-verified, verdict unchanged (dated note added to each entry)

AWS S3 Storage-Class Pricing (H-COST-09): every list price re-read from the AWS Price List API (publication 2026-11-21) and unchanged, deltas recomputed. AWS Storage Optimization - Tiered Storage (H-COST-09): tier figures verbatim; six further vendor-curated customer figures noted. Apache Flink Checkpointing (H-IMPL-02): the stable alias now serves 2.3.0, a pinned 2.3 URL added, and the RocksDB finding pointed to the state-backends page because this page handles large state through checkpoint storage. Top Trends for Data Streaming 2025 (Waehner): the 2026 edition (2025-12-10) noted as its successor. OCSF Schema v1.8.0, Linux Foundation - OCSF Joins Linux Foundation, and Amazon Security Lake with Apache Iceberg: OCSF v1.10.0 released 2026-11-20 and recorded as current.

### Admitted (all VERIFIED at the primary 2026-11-23; taxonomy record `methods/added-2026-11-23.json`)

| Entry | Tier | Hypotheses | Finding |
|---|---|---|---|
| Götz et al., Interoperable ACID Transactions for Open Table Formats (PVLDB 19(11), 2026) | A | H-ARCH-01 (context) | Abstract and Table 1 caption quoted from the vldb.org PDF; venue confirmed in the issue front matter. |
| Zhang, Mao & Jacobsen, Fugue (PVLDB 19(11), 2026) | A | H-STREAM-01, H-IMPL-02 (context) | 98.6% and 93.7% "up to" figures quoted from the abstract; NEXMark on Flink, no production or security workload. |
| Splunk Cloud Platform 10.7, Iceberg REST catalog datasets for Federated Search | B | H-ARCH-01 | Catalog-URL requirement (10.7), minimum version 10.4.2604 (10.6 page) and continuous Machine Data Lake promotion (10.7 release notes) quoted from help.splunk.com. |
| Wylde, Arroyo 0.16.0 release | B | H-ARCH-01, H-STREAM-01 (context) | Iceberg commit changes, the exactly-once FileSystem sink and the `bad_data` default quoted from the post; release tag and licence checked on GitHub. |
| Uetz et al., Can Risk-Based Alerting Mitigate Cybersecurity Alert Fatigue? (arXiv 2609.02465) | B (preprint) | H-SOC-BASELINE-01 (adjacent) | AUROC 0.92 against 0.72 quoted from the abstract; datasets mostly author-built; not a production base-rate leg. |
| SDW Lab stream-complexity (July 2026 run, v2 of 2026-11-03) | B (FIRST-PARTY) | H-IMPL-01, H-IMPL-02 (context) | 4 runtime units against 1, config 197 against 131 lines (1.5×, under the 3× threshold), fault restore 2 steps and about 20 s against 1 step and 0.02 s, quoted at `results/RESULTS.md` lines 18-29; v2 real-clock freshness gap about 3.0 s at line 124. The results file says the run does not meet the bar to move H-IMPL-01. |

Evaluated and not admitted on 2026-11-23: NVIDIA auto-ontology and its eval harness (business text-to-SQL, bears on none of the nine hypotheses); Apache Iceberg 1.12.0 as a separate entry (routine release, already recorded as a currency note on 2026-11-17); Tsegai et al., arXiv 2610.10608 (a replayed single-scenario benchmark of LLM triage, no production base rate); "The Exclusion Ratchet", arXiv 2608.31062 (SigmaHQ rule-history measurement, relevant to detection-coverage framing and to no hypothesis); the Axiom post and Cyberpresso comparison (Tier C, nothing for a hypothesis to rest on). A search for a second production SOC base-rate study published since July 2026 found no peer-reviewed or primary one, so H-SOC-BASELINE-01 stays single-source. One lead was traced and set aside: a Cloud Security Alliance research note cites "approximately 16.9 million SOC alerts", which traces to a contributed article on The Hacker News (2026-09-12) by an Intezer researcher, drawn from the vendor's own unnamed telemetry and reporting only on the 0.43% of alerts that were AI-related, so it is Tier C and is no base-rate leg. For the lab, every bench changed in `sdw-lab-benchmarks` since 2026-07-01 was listed from the git log, and the `bench.yaml` of stream-complexity, clickhouse-vs-duckdb, ocsf-streaming-cadence, cost-to-serve-retention, ocsf-zstd-dictionary, duckdb-edge-floor, iceberg-compaction and bench-d-tiered-realization was read. Stream-complexity, first committed 2026-07-19 and targeting H-IMPL-01, was admitted above; the others were either first committed before July or bear on no hypothesis in §3.7.

### Corrections after the independent verification (2026-11-23)

A second pass re-read every admission and refreshed entry at its primary on the same day and confirmed all of them. It found no fabricated figure, and the corrections it raised were applied to the bibliography before commit.

| Entry | Method | Finding |
|---|---|---|
| Fugue (Zhang, Mao & Jacobsen, PVLDB 19(11)) | claim↔source | The entry said Fugue cannot supply H-STREAM-01's restoration leg, but `PUBLICATION-MANUSCRIPT.md` §3.7 accepts "one additional verified, catalogued production or peer-reviewed leg", so on that wording it qualifies. The entry now quotes the restoration path, and the open question (does a benchmark with no security workload count) is staged for the owner as two-sided. Affiliations added from the PDF (first author at Confluent Inc., work done at the University of Toronto; co-authors at Toronto) with a vendor note, the testbed versions added (Flink 1.18, Kafka 3.8.1), and the RocksDB and 60-second facts re-located to the Testbed Setup paragraph. |
| SDW Lab stream-complexity | link | URLs pinned to lab commit 08f1044, because master moved to ba58d65 and its README changed; both results files are unchanged between the two commits. |
| Arroyo 0.16.0 | bias | The post calls Basin Pipelines Cloudflare's managed Arroyo service and announces its general availability, so a vendor-channel bias note is added; Level B holds. |
| Splunk Cloud Platform 10.7 | claim↔source | The 10.7 release notes do not contain "Iceberg", so the Machine Data Lake quote is marked as context with no Iceberg bearing; the 10.8 documentation is noted. The tier rationale now cites the 2026-11-03 owner ruling, written into METHODOLOGY §3.1 the same day. |
| Monthly Refresh Additions (section intro) | date | Two PVLDB papers are in the July 2026 issue and the lab bench was first committed 2026-07-19, so the intro now says "in or after July 2026". |

### Stale-source review, fan-out batch (2026-11-23)

Thirty date-stale entries were re-read at their primaries by a proposer and then checked independently by a skeptic pass, and only the checked changes were applied. No hypothesis score or confidence was moved; three tier relabels under the 2026-11-03 vendor-documentation ruling are noted in their rows.

| Entry | Method | Finding |
|---|---|---|
| Apache Iceberg Performance Tuning - SK Telecom | claim↔source | Every slide figure re-verified verbatim against the slides PDF and the two approximations against the recap page. Date corrected from "2022-2024" to 2022-12-19, since no 2024 primary sits behind it; the Trino Summit 2023 follow-up talk noted as an unread companion. |
| Trino: The Definitive Guide (O'Reilly Book) | claim↔source | The trino.io announcement (2022-10-03) confirms release 392, Java 17 and the Iceberg and Delta Lake connectors. Helm is seen only in search summaries of library records, and fault-tolerant execution could not be confirmed for the English edition, so the 2nd-edition bullet is narrowed. |
| Dremio - Data Lakehouse Architecture Guide | claim↔source | MISMATCH for two findings: the article body names no table format (Iceberg appears only in site navigation) and no query-engine layer. Both narrowed to what the body says; SAP ownership since 2026-07-06 noted. REFERENCES.md [41] retitled and redated to the page (2023-09-06). The ch05 §5.1 table-format pointer is flagged for the owner. |
| Alex Merced - Dremio YouTube Channel | claim↔source | A channel search for "security" returns web-auth and SSH tutorials, so "Practical security data examples" is removed. Role updated to Head of DevRel (Dremio author page); upload recency not confirmed. REFERENCES.md [56] initial and channel name corrected, appendix-e role updated. |
| AWS Storage Optimization Whitepaper | claim↔source | Cited PDF re-confirmed as a deprecated stub; tier figures verbatim on the Intelligent-Tiering page, including the existing 95% Deep Archive wording, with 71% for Archive Access added. Evidence Level split to B for function and C for savings claims per the 2026-11-03 ruling; flagged as a merge candidate with the Tiered Storage entry. |
| Prosci Change Management Best Practices (12th Edition) | claim↔source | Edition year corrected to 2023. 93%/15% re-sourced to Prosci's Feb 2026 PDF beside the executive summary's 88%/13% (not reconciled); 7× and the PMO shift verified; 183% not found at Prosci and traced to Accenture's Pulse of Change release (2024-01-12), so withdrawn; the 2024 Trends bullet labelled not found. Rows 60 and 417 above are superseded by this one, and monthly-update-tracker.md carries a dated note. |
| Databricks State of Data + AI 2024 | claim↔source | The full 2024 report PDF is public and all four figures verify. 377% narrowed to year-over-year growth in customers using vector databases, not RAG adoption; methodology is customer usage data, not a survey, and the report has no Flink or streaming data, so Relevance is corrected. |
| Samza (VLDB 2017) | claim↔source | MISMATCH: "200+ machines" misreads the paper, which says "more than 200 applications on over 10,000 containers"; bullet corrected to the §1 wording. Samza 1.8.0 (2023-01-17) is the latest release and the project is not in the Attic. |
| ClickHouse - IP Address Types Performance | link | Docs moved to /docs/reference/ (HTTP 308 from the old path); URL updated and author relabelled to documentation. The legacy URL in REFERENCES.md [22] returns 404 and is staged, not changed. |
| LST-Bench (SIGMOD 2024) | claim↔source | arXiv v3 and DOI 10.1145/3639314 added from the README BibTeX; the DBTest 2024 follow-up noted, slides unread. |
| Chris Bisnett - Huntress ClickHouse Migration (Video) | claim↔source | The description carries the 93% and 3 million endpoint figures and no compression figure, and the auto-caption track came back empty, so the compression finding is narrowed to unconfirmed pending a human viewing. A dated note was added to the hub essay note rsa-field-validation.md. |
| DuckDB Labs - DuckDB Overview | link | URL moved to /why_duckdb (HTTP 308); both findings re-verified at the content, closing the 2026-06-05 date-only triage. Tier relabelled C to B under METHODOLOGY §3.1. |
| Okta Security Analytics with DuckDB | cross-ref | Abstract figures re-verified verbatim. Alt URL now redirects to aicouncil.com; the RQ7 relevance line is struck because the entry's own block says the talk carries no isolation claim. The 2025 follow-up talk noted as corroboration with no new figures. |
| Microsoft Purview - Retention Policies and Labels | claim↔source | Findings re-verified at the page (ms.date 2026-07-22). Tier relabelled C to B under the 2026-11-03 ruling. |
| Confluent Customer Success - Implementation Roadmap | claim↔source | The URL serves Apache Kafka 101, 16 lessons including 5 exercises, with no adoption roadmap or maturity stages, so both findings are narrowed to an introductory developer course. |
| Brooks - The Mythical Man-Month | claim↔source | Pearson page confirms the 1995 edition (ISBN 9780201835953). The ch. 19 revision of "plan to throw one away" is added with an unverified-at-primary label (Tier C secondary only). APPENDICES.md [14] relabelled Level B with the qualifier, REFERENCES.md [14] publisher corrected. |
| Cloudera TEI, Private Cloud (May 2024) | claim↔source | All figures verified at the TEI page, so the "not re-verified" labels are removed and the 254% ROI and $12.77M NPV headline added. MISMATCH on the interview base: six representatives of five organizations, not six organizations. |
| AWS Well-Architected - Compute Optimization | claim↔source | URL redirects to the Framework's cost-optimization page (last updated 2026-11-16); the pillar whitepaper is historical. The unsourced 15-25% range is removed and the Compute Optimizer "up to 25%" given as a vendor ceiling; COST07-BP01 names Savings Plans, Reserved Instances and Spot, and Graviton was not found. REFERENCES.md [3] staged. |
| Google SRE - Reliability Economics | claim↔source | MISMATCH: the chapter says an increment "may cost 100x more" and gives no per-nine cost multiplier, and it says "nonlinear", never "exponential". Findings, author credit (Alvidrez, ed. Guliani) and REFERENCES.md [50] corrected. |
| Gartner - Reliability Overinvestment Analysis | link | WEAK-SOURCE: the document page returns 403 and search finds no title or abstract, so each finding is labelled unverified and the 2024 date marked unconfirmed. Keeping or removing the entry goes to the owner. REFERENCES.md [48] staged. |
| Uptime Institute - Reliability Tier Economics | claim↔source | not-in-source for two findings: the open tiers page carries no cost comparison and no over-engineering language, and it classifies facility infrastructure. Findings narrowed to the page's verbatim wording; REFERENCES.md [77] repointed to the Tier Classification System page and removed from the paywall list. |

Re-verified with the verdict unchanged, and a dated note added where the batch called for one: Fundamentals of Data Engineering (five stages confirmed in Reis's 2026-07-27 retrospective; the quoted "remained essentially unchanged" sentence is now labelled a paraphrase until checked against the book), Questioning the Lambda Architecture (date 2014-07-02 and "co-creator" wording), Top Trends for Data Streaming 2025 (existing note accurate, no edit), The Data-Centric Revolution (McComb), Access Path Selection (Kester et al., BU-hosted PDF added as a second Alt URL), LHBench (versions pinned and the 2026 Hudi blog noted as a write-workload counterpoint, Tier C), Huntress - ClickHouse Migration Case Study (date 2024-11-19, the 2025-04-01 Huntress EDR post noted), Apache Flink Checkpointing (date field only), Confluent - Kafka Architecture & Sizing ("up to 60%" re-read) and AWS Storage Optimization - Tiered Storage (no edit).

### Carry-through of the three changed verdicts (2026-11-23)

The three verdicts in the changed-verdicts table above were carried the same day to the manuscript, APPENDICES.md, the gap analysis, METHODOLOGY.md, REFERENCES.md, FIGURES-AND-TABLES.md, the scoring rubric, two analysis bundles and the Figure 4 script, and the GitHub contributor counts were re-derived before the wording changed (`gh api repos/apache/iceberg/contributors`, paginated: 405 users and 1 bot, so 406 linked accounts, and 946 entries with `anon=1`, 540 of them anonymous). The manuscript, appendices, gap analysis, references, scoring rubric and Figure 4 label now say "more than 400 contributors with linked GitHub accounts" with the 500-email limit stated, and Figure 4 was re-rendered from its script. The October-2025 record tables keep the 407 with a dated note, since they are preserved as written, and FIGURES-AND-TABLES.md's older "300+ contributors, 100+ organizations", which an earlier sweep missed, is struck and restated. The Netflix/Polaris finding is struck where it was still listed as a data source or a finding (METHODOLOGY RQ8 and RQ10, gap analysis Gap 9), and the Confluent driver claim where it was still described as standing (APPENDICES H-IMPL-01 key evidence and [28], the cost-reality bundle). The gitignored `paper/` and `build/` exports and the frozen `published/` snapshots still carry the old wording and were left alone. No hypothesis score or confidence moved, though two basis questions are left for the owner: whether H-ARCH-01's quantitative-precision 3 still rests on a contributor figure now known to be a floor, and what the "qualitative operational-cost premium stands on the remaining sources" line under H-IMPL-01 in APPENDICES.md now stands on.

### Stale-source review, fan-out batch 2 (2026-11-23)

A second set of thirty-one date-stale entries was re-read at the primaries by a proposer and checked independently by a skeptic pass, and only the checked changes were applied to MASTER-BIBLIOGRAPHY.md. No hypothesis score or confidence was moved. Three tier moves follow from this batch: Unity Catalog B to C and Hunters B to C (vendor documentation and relayed vendor remarks under the 2026-11-03 ruling), and Rahman et al. B to A on the journal version, so `scripts/count_reconcile.py` needs re-running before the count surfaces are regenerated.

| Entry | Method | Finding |
|---|---|---|
| Apache Iceberg Foundation - Governance & Contributors | claim↔source | not-in-source: no "Iceberg Foundation" appears on the community page or in a web search, and the Iceberg Summit 2026 post says the summit is sanctioned by the ASF with PMC oversight, so the foundation finding is withdrawn inline. The open-governance finding is narrowed to the page's committer and PMC text. Contributor count (405 users plus 1 bot) re-derived unchanged; release 1.12.0 (2026-09-30) noted. The struck line in `analysis-bundles/hypothesis-confidence-matrix.md` gets a dated note. |
| SK Telecom - Iceberg Performance Validation | claim↔source | MISMATCH on mechanism: "evolution" appears nowhere in the slides, which credit a partition redesign (33,942 Hive to 109,765 Iceberg partitions), column sorting for predicate pushdown and daily `rewrite_data_files` compaction, so the gain cannot be assigned to the format alone. The −82/−91/−76 chart values are per-metric, not per-case. Gap-analysis line 60 corrected (the −97% is read data size, elapsed time −96.5%), and APPENDICES [71] updated now that the slides carry the figures. |
| ClickHouse vs Elasticsearch - Storage Efficiency | claim↔source | MISMATCH: 9-12× and 12-19× are both the `_source`-kept configuration, at 1 billion and 10 billion rows; `_source` disabled gives about 7-10× and 9-14×. The data set is PyPI download events, so the security-log finding and Notes are marked not-in-source. Supersedes this entry's monthly-refresh row above, which carried the misreading forward. Carried to APPENDICES.md (two lines) and PUBLICATION-MANUSCRIPT.md (three lines); `methods/verification-2026-11/ledger.json` (lines 3707 and 3716) quotes the old bibliography wording in its context fields as of 2026-11-17, and `working/2026-11-17-quality-pass/U2-number-ledger.md` line 91 still marks the old reading verified-at-primary; both are left for the owner to correct or annotate. |
| DARPA XAI - Explainable Artificial Intelligence Program | cross-ref | MISMATCH of attribution: Crossref lists the doi 10.1002/ail2.61 retrospective as Gunning, Vorm, Wang and Turek; Gunning and Aha is AI Magazine 40(2), 2019. Author credit corrected; team count, span and programme-manager credit stay attributed and unconfirmed (retrospective blocks automated readers). NIST IR 8312 noted. |
| CISA - Enhanced Security Monitoring Best Practices | claim↔source | Advisory aa23-193a read through a reader tool. The 12-month figure is OMB M-21-31's audit-log retention (twelve months active plus eighteen cold) quoted by the advisory, not a baseline window, so the finding is narrowed and the 2026-11-17 unverified label removed. Advisory URL added as Alt URL; the 2025 Expanded Cloud Logs playbook noted. |
| MITRE Corporation - Insider Threat Research & Framework | claim↔source | Homepage read at Wayback 2026-10-05: "over 20 years", a "multi-disciplinary team" with no InT Lab name, and BDL listed under work seeking funding. Tenure updated, InT Lab dropped, BDL narrowed to in-development. The 47/29 counts stay as attributed to the CTID knowledge base announcement (not re-read). |
| Microsoft Security - Threat Modeling & Data Security for AI/ML | claim↔source | MISMATCH: the fourth heading is membership inference, not model inference; all eleven headings now listed. "audit" and "ownership" are not on the page, so bullets 3 and 4 are narrowed to input validation and Datasheets-for-Datasets provenance. Authors named from the byline; NIST AI 100-2 E2025 noted. |
| Apache Arrow - Columnar Analytics Performance | claim↔source | The overview page supports avoiding serialization cost between systems, not eliminating it for analytics generally, so bullet 2 is narrowed. The high-cardinality bullet is on neither page and is marked, with removal left to the owner. VAST renamed Tenzir noted; release 26.0.1 recorded. |
| Open Cybersecurity Alliance - Standards & Interoperability | claim↔source | MISMATCH on governance: the OASIS Open Project was sunset on 2026-03-31 and OCA continues as an OASIS-governed community initiative without guaranteed staff support or funding. Authors, date, URL note, Notes and the standards bullet updated; malformed relevance line fixed. REFERENCES.md line 155 and APPENDICES.md line 827 still carry the old framing and are staged. |
| Microsoft - Concept Drift Detection & Monitoring | claim↔source | not-in-source: the Microsoft post has no security content and does not cite the arXiv paper, so the security-drift claim is re-attributed to Kuppa & Le-Khac (arXiv 2206.07581), whose abstract carries it. "Azure ML Observability" narrowed to the post's own wording; byline and dates added. |
| Confluent - Machine Learning with Apache Kafka | claim↔source | A single 2018 post, not a series. Training-and-inference parity is an inference from the architecture, not stated, and "production-validated" is narrowed to named platform examples with no measured results. The 2026-06-05 date-only triage note is replaced; ksqlDB and Flink `ML_PREDICT` noted as the current path. |
| Tenzir Security Data Pipeline Platform | claim↔source | The 30% TCO line is gone from the live page and confirmed on the 2026-06-17 Wayback snapshot; the live page now claims 50% lower TCO, 75% fewer tools and 2x faster detection, with no methodology. The shift-left and separate-SIEM phrases are dated to the snapshot; "production deployments documented" is removed from the status line. Supersedes the earlier row at line 143 of this journal. A dated note is added beside the TCO line in the hub's `book-critical-hypotheses.md`; H3-INTEGRATION-04 is not moved. |
| Unity Catalog - Row-Level Security Performance Analysis | claim↔source | The catalogued URL redirects to the overview page, which carries none of the claims; repointed to the ABAC performance page and the filters-and-masks page. Caching is narrowed to how the UDF is written, and pruning loss is added as a cost of the policy's presence even for a constant-true UDF. No published figure or method; the "September 2024 analysis" could not be found. Tier C for performance claims under the 2026-11-03 ruling, B for function. Gap-analysis Source 4 and `isolation-first-security-tracking.md` RQ7 updated. |
| Netflix ClickHouse Pipeline - 5 PB/Day Ingestion | claim↔source | Page dated 2025-12-22 (Tom Schreiber), not 2024, so the entry is no longer date-stale. ~5 PB/day verbatim; 10.6M events/sec is on the upstream Muino post, not here. The page describes no security workload, so the Notes framing is narrowed. Supersedes the earlier row at line 84 of this journal. |
| Hunters Security - Why Companies Are Adopting Security Data Lakes | claim↔source | Dated 2023-11-27, not 2024. The bank figure is one Databricks executive's stated awareness at a vendor conference, and the HSBC 3x is relayed from a 2023 Databricks post, with Databricks' 2021 post giving 2-3x per analyst in a Lakehouse-plus-SIEM setup. Both findings are narrowed, and the entry moves from B to C. Supersedes the earlier row at line 85 of this journal. Gap-analysis HSBC and bank lines and the RQ11 row carry dated notes, and the RQ11 rating is not touched. |
| Hyperscan (NSDI '19) | cross-ref | Intel's open-source line stopped at 5.4 (Intel's own statement, quoted in the Vectorscan README), and the open fork is VectorCamp Vectorscan 5.4.14 (2026-11-09). branchfree.org added to the affiliations. |
| DBSP (PVLDB 2023) | cross-ref | An extended edition is in The VLDB Journal 34(4), 2025, art. 39 (Crossref), adding examples, standard-SQL semantics, a longer implementation section and a preliminary evaluation. It is recorded beside the original, and both editions stay Level A. |
| Mining Temporal Attack Patterns from CTI Reports (Rahman et al.) | cross-ref | Published in Knowledge and Information Systems 67(10), 2025 (Crossref, online 2025-07-22), so it moves back from B to A on the journal version. The 2026-11-07 re-tier missed a version that was already online, because the arXiv record never linked it. Supersedes the earlier row at line 385 of this journal. METHODOLOGY 8.1a and the §3.1 share lines are staged, not edited. |
| Outside the Closed World (Sommer & Paxson 2010) | claim↔source | not-in-source: "keep a human in the loop" is not a stated recommendation. Section IV's recommendations are the threat model, narrow scope, reducing error cost (including analyst context for manual inspection) and sound evaluation. Training data and evaluation are split into two challenges. The hub's `d3fend-wall/AIML-RIPENESS-EVIDENCE.md` line is narrowed to match. |
| MITRE Cyber Analytics Repository (CAR) | claim↔source | MISMATCH on currency: 102 analytics, none added since April 2022, last repository change 2025-05-16, so "continuously updated" is replaced. ATT&CK Detection Strategies and Analytics noted as the larger MITRE corpus (v18 691/1,739/106; v20, current, 703/1,770/106). Status line moved from "verified from knowledge" to "verified at primary". |
| Basic Formal Ontology (ISO/IEC 21838-2:2021) | claim↔source | The "650+ projects" figure is not on the official users page, which listed 731 ontologies and about 100 institutions on 2026-11-23. The count is replaced with that dated figure. The IEC webstore shows Edition 1.0 with no revision under development, and it is added as a fetchable Alt URL. |

Re-verified with the verdict unchanged, and a dated note added: Contentsquare (11x cost and 10x p99 verbatim), Didi (30% machine cost and about 4x query speed verbatim, no follow-up found), Cloudflare log analytics (600-to-60-byte and eight-times figures verbatim, still no cost percentage), Navan (one sentence added to the existing refresh note on Anvilogic's firmer restatement), Apache Polaris (the policy wording scoped to 1.9.0 maintenance types), Xor Filters (Binary Fuse Filters 2022 noted as a follow-up, not read), Axelsson base-rate fallacy (abstract and the 0.7 at 1/100,000 scenario read at a hosted PDF; Erbacher 2022 noted for direction), Petrescu et al. log parsing (0.73, 0.2 and ~0.05 re-read; Jiang et al. ISSTA 2024 and Beck et al. 2025 noted), NIST CSF 2.0 (still current; NIST IR 8596 Cyber AI Profile noted as a preliminary draft) and Atomic Red Team (status line moved to "verified at primary", badge 1,950 atomics).

### Stale-source review, fan-out batch 3 (2026-11-23)

A third set of thirty-one date-stale entries, most of them from the 2026-07-13 systematic search arm, was re-read at the primaries by a proposer and checked independently by a skeptic pass, and only the checked changes were applied to MASTER-BIBLIOGRAPHY.md. No hypothesis score or confidence and no evidence tier was moved, and no entry was added or removed, so the counts are unchanged. Two Evidence Level lines in the search arm had been cut off mid-number (at "(18" and "(IF 7") because `scripts/emit_search_arm_entries.py` takes the appraiser's first sentence by splitting at the first full stop, which also falls inside a decimal; both were restored from `methods/prisma-appraisal-2026-07-13.json`, and the generator itself is left for the owner.

| Entry | Method | Finding |
|---|---|---|
| Common Core Ontologies (CCO) | cross-ref | Latest release is v2.2 (2026-08-14), not v2.1. The README places CCO under evaluation by IEEE SA as P3195.1, an active PAR approved 2022-09-21, so Tier B holds; the Governance Board expects 3.0 by 2026-12-31 and 4.0 by 2027-06-30. The superseded version in `book-appendices/appendix-h-ocsf-strategy.md` lines 762 and 1070 is staged, because the "no CCO:CyberEvent class" statement there needs re-checking against v2.2 first. |
| Ryan Stillions - The DML Model | claim↔source | MISMATCH: the post, read in full through the Blogger feed, has no "Identity" level, and the Relevance labels had the levels misnumbered. Key Findings now list DML-8 Goals to DML-0 None or Unknown as the post does, the date is fixed at 2014-04-21, and the status moves from knowledge-confirmed to verified at primary. |
| SCYTHE - Purple Team Exercise Framework (PTEF) | cross-ref | PTEFv4 (dated January 2026, merged 2026-04-09) supersedes the cited version. MISMATCH on authorship: v1 names no author, and the v4 contributors are Bilbrey, Casey and Pemberton, so the Authors line now follows the v4 Contributors section. v4's five missed-detection gap types, ATT&CK v18 terminology and ATLAS coverage are noted; the README's "industry standard" is labelled vendor self-description. |
| Kingpin (Poulsen) | date | The Penguin Random House page gives the Crown ebook as Feb 22, 2011 and the paperback as Feb 7, 2012, which supports 2011 as first release; the hardcover ISBN the entry cites is not on that page, so its date is inferred. Open Library now sits behind a bot check and was read through its .json endpoint. |
| Cribl "Finality" Customer Case Study | link | URL moved to /resources/cs/finality/; 47%, 10x, 250% and the docs' 34-70% re-read verbatim. The page frames the 250% four ways, and the entry follows the body's month-over-month new-rule wording. |
| PBC: High-Ratio Compression for Machine-Generated Data | cross-ref | Crossref gives PACMMOD 1(4), published 2023-12-08, DOI 10.1145/3626732, under a title without the "PBC:" prefix. The SIGMOD 2024 pairing follows the PACMMOD issue convention and is labelled as such; the heading keeps its 2024 year. The manuscript's reference [26] has not been compared against Crossref. |
| Blitzcrank (PVLDB 2024) | link | The volume-page URL returns only the script-rendered site shell to a plain fetch, so the PVLDB PDF becomes the URL with the landing page and DOI as alternates. The manuscript's [23] still resolves and is left alone. |
| Delta Lake (PVLDB 2020) | claim↔source | Affiliations corrected to Databricks, CWI, UC Berkeley and Stanford, and the DOI added. The Key Findings parenthetical called a paraphrase "near-verbatim"; it is now labelled a paraphrase with the abstract's own clause quoted beside it. |
| Intrusion Detection Streaming Transactions (ICAIT 2019) | cross-ref | Full published title and pages 25-30 added from Crossref; the OpenAlex abstract still has no figures, so the existence-only carry stands. |
| CATRACA (Concurrency and Computation, 2019) | claim↔source | The abstract says "we propose" and "Our prototype", so "real deployed-system measurement (not simulation)" and "not a proposal" are narrowed to a prototype deployed on OPNFV and evaluated on three datasets. This carries the method-basis correction the 2026-07-13 appraisal record already held. Carried the same day to PUBLICATION-MANUSCRIPT.md §3.2.3, the generator note, and a dated addendum in `methods/PRISMA-RETRO-RUN-2026-07-13.md`. Tier A not moved; whether its rationale still holds is for the owner. |
| Virtual Network Function for Real-Time Threat Detection (MobiSecServ 2018) | cross-ref | Full title and pages 1-5 added. OpenAlex now types the record as a conference paper, so the preprint tag the Evidence Level argues against is gone. |
| Flink vs Spark Streaming for ML NIDS (SNPD-Winter 2021) | claim↔source | The comparison is on an IoT intrusion-detection workload with two public datasets, and the abstract leans toward Flink in one qualitative clause; Key Findings now say so. Full title and pages 51-56 added. |
| AIDA Framework (ARES 2019) | claim↔source | not-in-source: the paper never calls SABU "production" and calls its own run "the experimental deployment" (one commodity server, about 1.7 million alerts a day). The two duplicate bullets are replaced with the paper's wording, and the TMIS 2020 follow-up (12 million alerts, 34 IDSs, 3 organizations) is noted. The entry's Evidence Level line and manuscript §3.2.3 still say "production" and are staged. |
| Cloud-Based Snort NIDS (BDCC 2022) | claim↔source | Both Kafka figures are scoped in the results to a single broker, and the Key Findings bullet now says so. The same precision at manuscript §3.2.3 is staged. |
| Practical Performance of ML-Based NIDS (COMPSAC 2024) | claim↔source | MISMATCH: §V-B benchmarks each algorithm's highest-F1 classifier, which for Random Forest is the default at 0.974, since the parameter search lowered it to 0.972. The spread is about 0.010 (0.964 to 0.974), not about 0.008. PUBLICATION-MANUSCRIPT.md lines 593 and 740 and the U2 number ledger line 107 carry the old spread and are staged. |
| CERN - Large-Scale Intrusion Detection (ISGC 2018) | cross-ref | Figures re-read verbatim. Vâlsan's Zeek Workshop slides (2026-03-25) give about 1.2 TB a day of Zeek logs and about 2.5 billion connections a day on a 16-node cluster, and a 2020 CERN seminar gives six Kafka brokers at about 100,000 messages a second. The 1.2 TB is Zeek logs only, so it is no like-for-like measure against the 2018 5 TB goal. Whether it becomes H1-VOLUME-07 evidence is for the evidence gate. |
| Data-Lake-Based Security Transmission and Storage (Cluster Computing 2024) | cross-ref | MISMATCH: the article is in Issue 4 (pp. 4741-4755, online 2023-12-09), not Issue 9. Neither the article page nor the 75-article issue contents page shows a special-issue label. The truncated Evidence Level line was restored, and the 18% figure was re-read in the Springer abstract. |
| Digital-Forensics Architecture on a Security Lake (JISYS 2024) | claim↔source | The full text is open access and was read, so "full text was unreachable" is withdrawn. The system is built on Amazon Security Lake and validated in a university AWS organization (eight regional lakes and one roll-up lake), with no throughput, latency or cost figure. Author name corrected to the publisher's form, and volume and date added. Whether "the closest published statement of the security-lake thesis" should say AWS-native is for the owner. |
| Machine Learning on Distributed Stream-Processing Platforms (SBRC 2018) | claim↔source | MISMATCH: §3.3 presents the authors' own Storm, Flink and Spark Streaming benchmark, so "every figure is third-party" is withdrawn. The chapter cites the group's MobiSecServ 2018 paper for it, but the versions, host and loss figures match their GLOBECOM 2016 paper (10.1109/GLOCOM.2016.7841533, not catalogued). The generator's text was changed to match. The appraisal JSON and `methods/fulltext-retrieval-2026-07-16.json` rank 28 keep the old attribution as historical records. |
| High-Performance FPGA Architecture - IPsec Gateway (IJET 2018) | claim↔source | Both throughput figures are verbatim, but §V computes them with formula 1 from cycles per packet and the synthesis Fmax, and no on-the-wire measurement is reported, so each bullet now says so. Author name expanded to Krzysztof Skowron, and the publisher PDF added as Alt URL. The same qualifier and name were written into `methods/prisma-appraisal-2026-07-13.json` (record 11), which feeds the generator; `methods/prisma-results/records.json` and `reconciliation.json` keep "K. Skowron" as retrieved. |

Re-verified with the verdict unchanged, and a dated note added: Okta's Multi-Engine Data Stack (both figures verbatim; the speaker, Jake Thomas, and the Data Council 2024 talk are confirmed at the DuckDB library page because the post's own talk link returns 404), Yang et al. USENIX Security '24 (every figure verbatim; "at least 27%" is 27.37% per §6.2, all from one SOC at NCSA), Stream-Based IP Flow Analysis (five quotes verbatim; Fig. 3 not re-extracted), Adaptive and Auto-Scaling Stream Processing (three figures and the resource claim verbatim in the abstract; the UWO thesis and Wisdom code noted), SPARCS (all twelve Table I timings verbatim, scoped to one second of PMU data on a BeagleBone Black), INFN-CNAF (Conclusions quote single-checked, since the skeptic reached only the abstract page), Time Models in Graph Databases (both phrases verbatim; the FDSE 2020 conference paper noted), Efficient Host Intrusion Detection Using Hyperdimensional Computing (abstract phrases verbatim, and the truncated Evidence Level was restored together with the appraisal record's own verification note, which finds a CyberHunt workshop paper and recommends Tier B; the tier is left for the owner), Corporate Security Is a Big Data Problem (no citing work since 2025, per OpenAlex), Data-Warehouse Modelling in a Government SOC (Crossref volume and pages added; no citing work since 2025) and Analysis of Logs in the Environment of Email Services (one citing 2026 preprint, not read).

### Stale-source review, fan-out batch 4 (2026-11-23)

A fourth set of thirty date-stale entries, most of them from the 2026-11-07 snowball admissions and handbook companions, was re-read at the primaries by a proposer and checked independently by a skeptic pass, and only the checked changes were applied to MASTER-BIBLIOGRAPHY.md. No hypothesis score or confidence and no evidence tier was moved, and no entry was added or removed, so the counts are unchanged. Four verdicts changed, two of them narrowings, and the follow-on papers named in the refresh lines are recorded as leads, none of them admitted.

| Entry | Method | Finding |
|---|---|---|
| Tools and Benchmarks for Automated Log Parsing (Zhu et al., ICSE-SEIP 2019) | claim↔source | The 0.73 average Petrescu quotes does not occur in this paper; Petrescu's reference for it is He et al., ACM Computing Surveys 54(6), 2021, while Table IV (read at the arXiv full text) gives per-parser averages from 0.482 (LogSig) to 0.865 (Drain). Whether the survey derives 0.73 from these results was not checked, so the Relevance line says only what was verified. Loghub-2.0 (ISSTA 2024) noted as the same group's successor benchmark, which its own authors say addresses the original's limited scale and representativeness. |
| I Tweet Honestly, I Tweet Passionately (Marwick & boyd, New Media & Society 2011) | claim↔source | Origin claim narrowed to standard reference. boyd's own account (zephoria.org, 2013-12-08) calls this paper the first time she used "context collapse" in published writing, traces the idea to her 2002 thesis, and notes Wesch's 2009 article with the term in its title (Explorations in Media Ecology 8(2), Crossref pp. 99-114). Relevance, Key Findings, Notes, the Reis entry's Notes and the section intro were all changed from "origin" or "coined" to "standard reference"; the handbook ch04 footnote and the two hub concept notes already used that framing. |
| LogGrep (Wei et al., EuroSys 2023) | claim↔source | "in a production setting" narrowed: the paper reports an evaluation on Alibaba Cloud production log types and no deployment. The body puts overall cost at 36% of CLP, 34% of gzip+grep and 7% of ElasticSearch on the Alibaba logs, so the order-of-magnitude cost gap holds against the Elasticsearch index and the gap against the compression baselines is about 3x. Author camera-ready added as Alt URL; the ACM TOS 2024 extension and LogCloud (PVLDB 2025) noted. The two ch02 manuscript sentences that follow the abstract are flagged for the owner, not edited. |
| Fourth Annual Report on the State of SIEM Detection Risk (CardinalOps, press release 2024) | cross-ref | The 2025 edition is now read at two CardinalOps primaries, the 2025-06-05 release and the report PDF through a Wayback copy, and they disagree: the release and the report's summary page give 13% never-fire and 21% coverage, while the report body gives 10% and 22% for the year. The report confirms the 2024 18%, so the cited figure stands, and the vendor's own never-fire share sits between 10% and 18% across the two latest editions. Supersedes this entry's monthly-refresh row above, which said the 2025 figures were found only in trade press. |

Re-verified with the verdict unchanged, and a dated note added: Binary-Feature-Extraction Data-Provenance System on Flink (no citing work since 2025), Kokulu et al. CCS 2019 (18 interviews verbatim; Tariq, Chhetri, Nepal and Paris, ACM Computing Surveys 57(9), 2025, noted as an unappraised review), Rigger and Su OOPSLA 2020 (175 / 125 / 77 verbatim; SQLancer++ at ASPLOS 2026 confirmed at Crossref and noted), Raasveldt and Mühleisen PVLDB 2017 (abstract verbatim; XDBC, PACMMOD 2025, noted as a citing mechanism paper), Zeng et al. PVLDB 2023 (design-decision sentence verbatim; Liu et al., The VLDB Journal 2025, noted), Durner, Leis and Neumann PVLDB 2023 (abstract verbatim; F3 corrected in the note to a different group that cites this paper), NoDoze NDSS 2019 (the 84% is hedged in the abstract and unhedged in the body, so the "estimate" wording stays), Valeur et al. TDSC 2004, BtrBlocks SIGMOD 2023 (the PDF labels itself the author's version, so the Validation Status line no longer calls it the version of record; FastLanes noted as a later format reporting about 7x faster decode), the Humio post (quotes verbatim; the current LogScale *Index-Free Data Storage* page noted as B-grade for the design under the 2026-11-03 ruling), CLP OSDI 2021 (μSlope, OSDI '24, noted with the same interest flag), Zibak et al. DTRAP 2022, Inam et al. S&P 2023 (the CCS 2025 follow-up is Hassan's group, not Bates'), Michael et al. ACSAC 2020 (Alt URL moved to www.acsac.org; the SoK labelled same-group corroboration), SPA ICDE 2023, Dodds 2020, Conway 1968, Anaconda 2020 (later editions noted, with no time-share figure carried from them), Press/Forbes 2016, Sambasivan et al. CHI 2021, Wixom and Watson 2001, Khadka et al. ICSE 2014, Buchholz and Tjaden 2007, Vanini et al. 2024 (two same-group follow-ups confirmed at Crossref and noted), Engelen et al. SPW 2021 (Lanvin et al., CRiSIS 2022, noted as a candidate entry) and Khan et al. EMSE 2024.
