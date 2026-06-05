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

*Next validation due with the cadence (`SCHEDULING.md`). When the worklist items above are re-sourced or
stripped, append a dated row moving each to VERIFIED or removing it — do not silently re-litigate settled rows.*
