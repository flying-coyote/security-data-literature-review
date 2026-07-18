---
type: proposal
title: "July re-tier + catalog proposal — STAGED 2026-07-18, owner approve/strike per row"
created: 2026-07-18
tags: [monthly-update, re-tier, catalog, adjudication, staged]
---

# July re-tier + catalog proposal — STAGED (nothing applied)

**Status: STAGED 2026-07-18.** Every row below awaits an owner verdict — mark APPROVE or STRIKE
per row; I execute only approved rows, each through the standard instrument (claim verified at
the primary before any bibliography edit), then run the full count ripple and gates. Sources:
the July research packet remainder (`MONTHLY-2026-07-RESEARCH-PACKET.md` §2-§4, primary-verified
2026-07-09) plus the vendor-docs tier class the 2026-Q3-c vendor regeneration surfaced
(`vendor-landscape/quarterly-updates/2026-Q3-regen-2026-07-18.md`). Current baseline: 230 blocks
/ 228 tiered / 95 A (41.7%).

## A. Freshness re-tiers held from the packet (§2)

| # | Entry | Change proposed | Evidence | My call |
|---|---|---|---|---|
| A1 | Cloudera Impala + Iceberg Performance (bib L1238) | **A→B** | The "10×" is a vendor-relayed single unnamed-customer anecdote on a technical-preview announcement page, not a Cloudera-run reproducible benchmark — "A (Production benchmarks)" overstates it. The entry's own date field already carries the flag. Also: annotate the stale `RESEARCH-JOURNAL.md` ~L126 line ("10x over Hive gone (also DEAD)") as superseded by the 2026-06-05 re-source. | **APPLY** — Level A drops to 94 until B1 lands |
| A2 | ClickHouse vs Snowflake Benchmarks (bib L3369) | **B→C** | All three posts are ClickHouse-run benchmarks of a competitor, and Snowflake has publicly contested the 2026 CostBench/write-side numbers. B was defensible only with the caveat stated; contested-by-the-benchmarked-party pushes it over the line. If kept at B, the newer CostBench anchors (2026-06-23 / 2026-05-06) should replace the 2023 post either way. | **APPLY** |
| A3 | Top Trends for Data Streaming 2025 — Kai Waehner (bib L445) | **Repoint to the 2026 edition** (same author, same annual series, 2025-12-10), stays B | The 2026 edition is live: consolidation, diskless Kafka + Iceberg storage, RPO=0 SLAs, agentic AI with real-time context. Alternative: keep 2025 as a superseded prior-year anchor and add 2026 alongside. | **APPLY** (repoint, not duplicate) |
| A4 | Cloudera TEI citation split | none — **ALREADY DONE** | The bibliography already carries two entries (Public Cloud 2021-10 at L1431, Private Cloud 2024-05 at L1450, "formerly conflated" noted). Recorded here so the packet's remainder list closes clean. | NO ACTION |

## B. Catalog-ready candidates (§3 remainder + the near-A lead)

All primary-verified by the packet's adversarial pass on 2026-07-09; each add is +1 block / +1
tiered. My calls lean toward the measured/practitioner rows and away from vendor-channel
concentration (the corpus already carries several ClickHouse-published case studies).

| # | Candidate | Tier | Hypothesis/RQ | My call |
|---|---|---|---|---|
| B1 | **Bilot et al., "Sometimes Simpler is Better: SOTA Provenance-Based IDS"** — USENIX Security 2025 | **A** (peer-reviewed, top venue) | detection-architecture evidence | **ADD first** — the packet's only clean A; flagged lead-not-ready solely on claim phrasing, so execution = read the paper, write the anchor claim to what it shows |
| B2 | Bono (Microsoft), RCT for a Phishing Triage Agent — arXiv:2511.13860 | B (rigorous RCT design, vendor-authored on own product, preprint) | RQ12 | **ADD** with bias flag |
| B3 | CORTEX: Collaborative LLM Agents for Alert Triage — GMU + Fluency, arXiv:2510.00311 | B (real traces, released dataset, vendor co-author) | RQ12 | **ADD** |
| B4 | Red Canary, "Go jump in a lake" — SIEM bill decomposition (105 TB OpenSearch ≈ $24,688/mo, 65% compute) | B (practitioner, illustrative figures) | H-COST-09 / RQ13 | **ADD** — rare compute-vs-storage split |
| B5 | RiverSafe/Cribl case study — 750→450 GB/day (~40% ingest cut), £120-150K/yr avoided | B (SI-published, measured before/after) | H-COST-09 / RQ13 | **ADD** — pairs with B4 as the measured RQ13 economics |
| B6 | Naglieri, "Icebergs in the Data Lake" — Detection at Scale, Jan 2025 | B (named practitioner essay) | H-ARCH-01 / RQ11 | **ADD** — the mechanism behind the Iceberg-dominance claim |
| B7 | Artemis Security / ClickHouse — 69× faster coalesced detection queries, Jul 2026 | B (vendor-published + bias flag) | H3-PERFORMANCE-01 / RQ11 | **HOLD** — genuinely interesting query-coalescing evidence, but a fourth-plus ClickHouse-channel case study concentrates the vendor channel; coin-flip, take it if RQ11 needs the depth |
| B8 | Databricks Lakewatch announcement — lakehouse vendor entering SIEM (private preview) | C (marketing numbers hedged) | RQ11 landscape | **ADD** with explicit bias flag — the market-structure fact (a major lakehouse vendor now sells a SIEM) is the evidence, not the "up to 80%" |
| B9 | Realm.Security / Vensure "83% SIEM cost cut" | C (self-published, single self-reported metric, no methodology) | RQ13 | **STRIKE** — weakest of the set; Dark Reading coverage doesn't add methodology |

## C. Leads (§4 remainder)

| # | Lead | Finding | My call |
|---|---|---|---|
| C1 | Matryoshka arXiv:2506.17512 | **Duplicate confirmed** — the bibliography already holds "Matryoshka — Semantic-Aware Parsing for Security Logs" (L3753, Berkeley PDF primary) | **SKIP** (no action; arXiv id could be added to the existing entry's metadata if wanted) |
| C2 | CSTS — Canonical Security Telemetry Substrate, arXiv:2603.23459 | On-topic (RQ16-adjacent) but post-cutoff framing, partial claim confirmation | **HOLD** for a future month |
| C3 | OWASP State of Agentic AI Security 2.0 | The figure as phrased is contradicted at the primary on a falsifiable numeric detail | **HOLD** — usable only after re-phrasing to the real number; not worth the add this month |

## D. Vendor-docs tier class (surfaced by the 2026-Q3-c regen — vendor DB legs, not bibliography entries)

The regen re-tiered the Sentinel pricing leg B→C under the vendor-channel rule (vendor-authored
docs; authorship is the line), which leaves eight same-class legs at B in
`vendor-landscape/vendor-database.json`. Sweeping them is a one-rule decision, so it's staged as
one row with the single genuine nuance separated:

| # | Legs | Change proposed | My call |
|---|---|---|---|
| D1 | aws-athena-docs-serverless, aws-athena-pricing-5tb, snowflake-multi-cloud-docs, snowflake-governance-features, unity-catalog-docs, databricks-ml-platform, sentinel-ai-threat-detection | **B→C sweep** (vendor-authored docs/pricing pages, same class as the ruled Sentinel pricing leg) | **APPLY** — scores already re-derived at the regen won't move further except athena serverless_simplicity/cost_predictability and the snowflake/databricks 3s, whose tier ceilings at C still support score 3; I re-run the rollup gate after |
| D2 | trino-connectors-docs | owner rule needed | **HOLD for your ruling** — ASF-project community docs, not vendor marketing; the vendor-channel rule's authorship line doesn't map cleanly onto a foundation project. My lean: keep B (community-authored reference, no commercial author) and record the distinction as a rule extension |

## E. Observed during staging (mine, not the packet's)

| # | Entry | Observation | My call |
|---|---|---|---|
| E1 | ClickHouse vs Elasticsearch — Storage Efficiency (bib L1858, currently **A**) | Same class as A2: a ClickHouse-run benchmark of a competitor, at A ("Benchmark study"). The 12-19× figures were verbatim-verified 2026-07-09, so the numbers are honest, but the tier sits above the class the packet re-tiers elsewhere. | **Re-tier A→B** for class consistency (vendor benchmark, methodology disclosed, uncontested — one notch above A2's contested C) |

## Net impact if my calls are applied as-is

Derived at execution, not promised, but roughly: re-tiers move A 95→93 (Impala, CH-vs-ES) then
Bilot restores one → 94; adds B2-B6+B8 bring tiered 228→235; Level A ≈ 94/235 = 40.0%. The share
dips because this wave adds measured B/C evidence faster than A — the honest direction given the
packet found exactly one clean A, and the 75% target remains a multi-quarter climb, not a
this-wave outcome.
