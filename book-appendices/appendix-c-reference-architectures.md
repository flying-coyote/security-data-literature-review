---
type: design
title: "Appendix C: MOAR Reference Architectures — L-I-G-E-R Component Model and Five Patterns"
created: 2025-10-15
tags: [moar, liger, iceberg, architecture-design, multi-engine, security-data]
---

# Appendix C: MOAR Reference Architectures

**Purpose**: Visual diagrams and detailed implementation patterns for validated security data architectures based on Modular Open Architecture (MOAR) principles. Each pattern includes: architecture diagram, technology stack, deployment considerations, cost profile, and when to use.

**How to use**: Find the pattern that matches YOUR organizational constraints (from Worksheet A.2). Use as starting template, adapt for your specific requirements.

---

## The MOAR Framework

Modular Open Architecture (MOAR) is a composable, vendor-neutral approach to security data infrastructure. Rather than selecting a monolithic SIEM that bundles storage, query, visualization, and pipeline into a single vendor's stack, MOAR separates these concerns into interchangeable layers so an organization can pick the strongest component for each one.

![The MOAR reference architecture: security data flows from Source through Ingest, Store, and Analysis to security Tasks, built on open standards—Apache Arrow and Apache Iceberg for data, OCSF for schema, and Sigma for portable detection logic—with every layer independently swappable.](figures/moar-architecture.png){ width=95% }

### Five MOAR Design Principles

Every reference architecture in this appendix (except Pattern 4: Traditional SIEM) applies these principles to varying degrees:

1. **Vendor-Neutral Data Layer** — Use open table formats (Apache Iceberg, Delta Lake) with vendor-neutral catalogs. *Validation test*: Can you swap Trino for Dremio without rewriting queries or migrating data?

2. **Separation of Storage and Compute** — Store data in object storage (~$0.023/GB/month S3) while scaling compute independently based on workload demands. *Validation test*: Can you turn off all compute and still access your data via different tools?

3. **Compression-First Design** — Security logs achieve 8.5× (Iceberg Parquet, pyiceberg zstd defaults) to 9.7× (tuned cold Parquet zstd-19) compression with proper encoding (Parquet + ZSTD/SNAPPY for Iceberg, optimized codecs for ClickHouse; first-party lab measurement on OCSF-normalized Zeek and EDR corpora, per cost-to-serve-retention/results/RESULTS.md). *Validation test*: 1 TB/day of raw logs should cost ~$1,000/month for S3 storage with 365-day retention.

4. **Schema Evolution Without Breaking Changes** — Use Iceberg schema evolution and OCSF normalization (OCSF v1.x, current release v1.8.0) to onboard new log sources without system downtime. *Validation test*: Adding a new log source doesn't require downtime or data migration.

5. **Query Engine Specialization** — No single engine is optimal for real-time alerting, ad-hoc investigations, and scheduled reporting. Deploy the right engine for each workload. *Validation test*: You can choose the right tool for each workload without creating data silos.

### MOAR Component Model (L-I-G-E-R)

The reference implementation organizes components into five interchangeable layers:

| Component | Role | Options |
|-----------|------|---------|
| **L**akehouse | Storage layer and table format | Apache Iceberg, DuckLake, Delta Lake, Hudi (object store: MinIO, SeaweedFS) |
| **I**ndex | Metadata catalog and governance | Iceberg REST, Polaris, Unity Catalog, Nessie, Lakekeeper, Gravitino |
| **G**raph | Visualization and query interface (usually a passthrough) | Grafana, Superset, custom hunt UI, incumbent SOC consoles |
| **E**ngine | Query engines matched to workloads | DuckDB, Trino, ClickHouse, StarRocks, Dremio |
| **R**oute | Data pipelines and transformation | Vector, Cribl Stream, Tenzir, Fluent Bit, Kafka, Flink |

The Graph layer is usually a passthrough rather than a build decision, because the shop almost always already has somewhere its analysts work — Grafana, Superset, a custom hunt UI, or the incumbent SOC consoles (Splunk, Elastic, Sentinel) kept for federated read during a transition — and you can go many directions from here, including the AI tooling that increasingly sits above or beside the analytics. I don't try to be exhaustive about that overlying analytic layer, because it isn't where the trust problem lives and it changes faster than anything underneath it. The intent of this book runs the other way, to be exhaustive about the optional infrastructures underneath the analytic (storage, table format, catalog, engine, routing) that decide whether the analytic they feed is trustworthy, well-connected, and performant in the first place, and whatever interface sits on top inherits those properties rather than creating them.

One honest caveat on where the catalog/Index layer earns its place: at the single-node SOC scale I test, it pulls its weight less from query performance — the engines answer sub-second whether or not a separate catalog is brokering metadata — and more from governance, lineage, and letting several engines read the same tables without stepping on each other, so its weight in the decision rises with scale and with the number of engines sharing the lake, which makes the catalog a scale-and-governance bet rather than a layer every deployment needs on day one.

Each pattern below represents a different combination of these components, optimized for specific organizational constraints. The five patterns form a spectrum from fully monolithic (Pattern 4: Traditional SIEM) to fully composable (Pattern 5: MOAR Multi-Engine).

One caveat keeps the interchangeability honest: it holds only when encryption stays *outside* the open file format. Parquet's own modular encryption (PME) ties an encrypted file to the library that wrote it; in lab testing, a PME-encrypted file produced by one reader was unreadable by DuckDB, Polars, DataFusion, and ClickHouse, so encrypting inside the file silently revokes the swap-any-engine property the layer model depends on (Principle 1's "swap Trino for Dremio" test fails outright). For regulated data that must be encrypted at rest, encrypt at the volume or object-store layer (SSE-S3/SSE-KMS, dm-crypt, LUKS) so the bytes the engines read stay portable, rather than inside the Parquet file — or accept that the encrypting engine becomes the only one that can read the data.

### Production Validation

These principles are validated at scale:
- **Netflix**: 5 PB/day ClickHouse + Apache Iceberg (Daniel Muino, ClickHouse meetup presentation, late 2024; Tier C (vendor-ecosystem event, self-reported)) (Principle 2, 5)
- **Okta**: 100K QPS DuckDB, 7.5 trillion records (Okta, Jake Thomas personal account; Tier B) (Principle 5)
- **Apple**: Petabyte-scale Apache Iceberg (Baris Aydın, "Apple's Journey with Apache Iceberg," Subsurface Live 2023; Tier B) (Principle 1, 2)
- **CISA**: Zeek-OCSF mapping, ~95% mapping accuracy as reported by the project itself, an illustrative figure rather than an independently published rate (CISA Zeek-OCSF project; Tier B) (Principle 4)

Those are external deployments that validate the principles at scale; the interchangeability claim itself I verified first-party in a runnable reference stack, because "the layers are swappable" is the kind of assertion that deserves a measurement rather than a diagram. What follows is the one place in this book where I state the swap-clean claim in full and say exactly how much of it is measured.

### The swap-clean claim, stated once

The promise underneath MOAR is that each layer can be replaced with an alternative and the data — and the answers you get back from it — survive the change. That is the whole reversibility argument: if a layer choice turns out wrong, you swap the part and the data stays, which is a sentence a monolith vendor cannot say, and it is why the architecture can defend itself even where any single component choice is debatable. The L-I-G-E-R reference composition (the table above) is *one* instantiation of MOAR at a stated scale, not MOAR itself; the durable claim is that maintained open-standard parts compose over open formats, and the specific parts I name below are the composition I happen to defend on a single host, each of them falsifiable on its own. The reference stack ships a swap verb per layer that writes or reads the same OCSF data through the alternative component and checks that the answer doesn't move:

- **L — store**: MinIO ↔ SeaweedFS, both speaking S3, same OCSF batch, identical answer (`./moar swap-store`).
- **I — catalog**: the Iceberg REST reference fixture ↔ Nessie ↔ Lakekeeper, three independent codebases (Java reference, Java/Quarkus, Rust/Postgres) implementing the same Iceberg REST contract, identical answer across all three (`./moar swap-catalog`).
- **I — table format**: Iceberg ↔ DuckLake, the same logical OCSF batch on the same object store, identical answer (`./moar swap-format`).
- **E — engine**: DuckDB, Trino, ClickHouse, StarRocks, and Dremio over one Iceberg table, run through a cross-engine answer-equality gate (`./moar verify`).
- **R — router**: Vector/VRL ↔ Tenzir/TQL ↔ Fluent Bit/Lua, the same raw Okta event normalized to the same OCSF Authentication record (`./moar swap-router`).

The Graph layer carries no swap verb here, and that absence is by design rather than an omission, because it's a passthrough to whatever interface the shop already runs rather than a component the lab swaps and answer-equality-checks, so there's nothing for `./moar` to hold constant across an alternative.

```text
$ ./moar verify        # E — engine: cross-engine answer-equality over one Iceberg table
  duckdb  total,rdp = 1000 125    trino   1000 125    clickhouse 1000 125
  starrocks 1000 125              dremio  1000 125     ✓ all running engines agree

$ ./moar swap-store    # L — store: same OCSF batch through two object stores
  minio (s3:9000):     1000 rows; dst_port=3389 -> 125 (truth 125)
  seaweedfs (s3:8333): 1000 rows; dst_port=3389 -> 125 (truth 125)   ✓ identical

$ ./moar swap-router   # R — router: one raw Okta event → three normalizers
  vector / tenzir / fluent-bit → identical OCSF Authentication (class_uid 3002)   ✓ identical
```

*Figure C-1 — the swap verbs run live on the reference stack (single-host, Tier B): the answer does not move when the store, the router, or the engine is swapped. This is the reversibility claim measured, not asserted.*

The honest part is how unevenly that claim is backed, and the layers are not equal. The **engine layer is the one I have actually pressure-tested for answer-equivalence** rather than asserted it, and it's the one where the gate earns its keep: a broader run across twelve publishable Parquet readers on byte-identical data found ten correct and two silently wrong (engines selected by distinct reader, because the divergence lives in the Parquet reader rather than the engine wrapped around it): a version-scoped chDB Bloom-filter undercount that reproduced only at 100M scale and was fixed in the next point release (wrong on chDB 4.1.8, correct on 4.1.9), and a fastparquet `PLAIN_DICTIONARY` decode bug still live on the latest version (2026.5.0), so on the engine layer answer-equivalence is a measured, mechanism-isolated finding (SDW Lab, `clickhouse-vs-duckdb/results/MULTI-ENGINE-CORRECTNESS.md`, first-party Tier B; see Appendix I.1.5 and `H-ENGINE-ANSWER-EQUIVALENCE-01`), and the lesson is that a fast engine can return a wrong answer with no error, so the cross-engine check is a standing control, not optional ceremony. The other four layers, store and catalog and table format and router, I verify with a swap-and-confirm demonstration (one batch through each alternative, answer held constant) and otherwise rest on the open-format contract: the same Parquet bytes flow through, so a different store or catalog or router is reading or writing the same data, and the answer should not move. I have not run those layers through the same characterized at-scale, multi-implementation divergence probe that found the engine bugs, so the accurate statement is *answer-equivalence verified for the engine layer; the store, catalog, format, and router swaps are confirmed on a single batch and otherwise asserted from the open-format contract.* The reason the engine layer needed more than the contract is that an open table format guarantees every engine can *read* the bytes, not that two engines compute the *same answer* over them — the divergence lives in the read path, not the file — which is exactly where a swap can pass the "it runs" test and still be wrong.

One file-format facet to track sits a layer below the table format: Vortex (now a Linux Foundation project, installable as `vortex-data`) claims large read speedups over Parquet. Measured against zstd-Parquet on an OCSF corpus, the gain was real but single-digit (roughly 1.7–2.6× on a full decode, 3.3–4× on a needle) rather than the headline 10–100×, with a scale-dependent footprint and identical answers. It is not yet an Iceberg data file format — Iceberg 1.11.0 shipped the pluggable File Format API but the Vortex plugin is still open — so for now it is a standalone datapoint, a candidate third answer to the read-speed question alongside the V4 metadata work and DuckLake if that plugin lands.

---

## Architecture Pattern Index

The budget and cost figures throughout this appendix are outputs of the TCO model in Worksheet A.6 (cloud and vendor rates as of Q4 2025), not measured invoices from a specific deployment, so treat them as illustrative sizing for the stated volumes and re-run A.6 against your own numbers before procurement.

| Pattern | Use case | Team | Budget/yr |
|---|---|---|---|
| 1. Healthcare Hybrid (on-prem + cloud) | HIPAA, PHI residency, hybrid cloud | 1-2 data engineers; 15-person security team | $774K-1M (platform $300-500K) |
| 2. Cloud-Native AWS-First | AWS-committed, cloud-first, cost optimization | 3-5 data engineers; 50+ analysts | $500K-2M |
| 3. Multi-Cloud Federated (Denodo) | Multi-national, data sovereignty, M&A | 5+ data engineers; distributed teams | $2M+ (complexity premium) |
| 4. Traditional SIEM (Splunk ES) | Real-time mandate, zero data engineers, simplicity | 0 data engineers (SOC analysts) | $2M-12M (volume-dependent) |
| 5. MOAR Multi-Engine | Workload optimization, 50-75% cost savings | 3-5 data engineers; hybrid-tolerant | $400K-800K |

Patterns 1-4 map to the variants chapter's architect journeys (Jennifer, Marcus Path A, Priya, Marcus Path B) — the "what good looks like" material, Chapter 6 of the handbook; Pattern 5 to Appendix I. Full detail for each follows below.

---

## Pattern 1: Healthcare Hybrid (On-Prem + Cloud)

### Architecture Overview

**Problem Statement**:
- HIPAA compliance requires PHI data on-premises
- 80% of security data (cloud logs, SaaS) has no PHI constraint
- Team has 1-2 data engineers (limited capacity for self-hosted complexity)
- Budget: Under $1M annually (cannot afford $1.6M+ Splunk expansion)

**Solution**: Hybrid Iceberg lakehouse with Dremio Cloud query engine

---

### Architecture Diagram (Text-Based)

```
┌─────────────────────────────────────────────────────────────────────┐
│                     DATA SOURCES (2.5 TB/day)                       │
├─────────────────────────────────────────────────────────────────────┤
│ PHI-Touching (500 GB/day)          │ Non-PHI (2 TB/day)             │
│ • Clinical system logs             │ • AWS CloudTrail               │
│ • Medical device telemetry         │ • SaaS apps (Okta, O365)       │
│ • EHR access logs                  │ • Network flows (non-clinical) │
└─────────────────────────────────────────────────────────────────────┘
                    ↓                              ↓
┌─────────────────────────────────┐  ┌────────────────────────────────┐
│   ON-PREMISES (PHI Zone)        │  │   CLOUD (AWS us-east-1)        │
├─────────────────────────────────┤  ├────────────────────────────────┤
│ Ingestion:                      │  │ Ingestion:                     │
│ • Filebeat → Kafka (3 brokers) │  │ • Fivetran (managed)           │
│ • Spark Streaming → Iceberg    │  │ • AWS Kinesis → Spark → Iceberg│
│                                 │  │                                │
│ Storage:                        │  │ Storage:                       │
│ • MinIO Object Storage (500TB) │  │ • AWS S3 (1.5 PB, tiered)      │
│ • Apache Iceberg tables         │  │ • Apache Iceberg tables        │
│ • 3-year hot retention          │  │ • 90-day S3 Standard (hot)     │
│ • S3-compatible API             │  │ • 3-year S3 Glacier (cold)     │
│                                 │  │                                │
│ Catalog:                        │  │ Catalog:                       │
│ • Polaris (self-hosted)         │  │ • Polaris Cloud (managed)      │
└─────────────────────────────────┘  └────────────────────────────────┘
                    ↓                              ↓
                    └──────────────┬───────────────┘
                                   ↓
                    ┌──────────────────────────────┐
                    │   UNIFIED QUERY LAYER        │
                    ├──────────────────────────────┤
                    │ Dremio Cloud (Managed)       │
                    │ • Federated query            │
                    │ • On-prem + Cloud Iceberg    │
                    │ • Reflections (dashboards)   │
                    │ • Row/column security        │
                    └──────────────────────────────┘
                                   ↓
┌─────────────────────────────────────────────────────────────────────┐
│                           CONSUMERS                                 │
├─────────────────────────────────────────────────────────────────────┤
│ • SOC analysts (SQL via Dremio)                                     │
│ • Tableau dashboards (via Dremio BI connector)                      │
│ • SOAR (API access to Dremio for automated queries)                │
│ • Compliance reports (query both on-prem + cloud unified)           │
└─────────────────────────────────────────────────────────────────────┘
```

---

### Technology Stack

| Component | Technology | Deployment | Rationale |
|-----------|------------|------------|-----------|
| **Ingestion (PHI)** | Filebeat → Kafka → Spark Streaming | On-prem | Real-time streaming for clinical systems |
| **Ingestion (Non-PHI)** | Fivetran, AWS Kinesis | Cloud (managed) | Reduce operational burden, SaaS connectors |
| **Storage (PHI)** | MinIO (S3-compatible) | On-prem | HIPAA data residency requirement |
| **Storage (Non-PHI)** | AWS S3 (Standard + Glacier) | Cloud | Cost-optimized tiered storage |
| **Table Format** | Apache Iceberg | Both | Unified format, query across on-prem + cloud |
| **Catalog** | Polaris (self-hosted + Cloud) | Hybrid | Federate on-prem + cloud tables |
| **Query Engine** | Dremio Cloud | Cloud (managed) | 0-1 data engineer constraint, BI acceleration |
| **Table Maintenance** | Apache Spark | On-prem (scheduled) | Iceberg compaction, snapshot expiration |
| **Orchestration** | Apache Airflow | On-prem | DAG scheduling for batch jobs |

---

### Deployment Considerations

**On-Premises Infrastructure**:
- **Compute**: 3-5 bare metal servers (Kafka brokers, Spark workers, Airflow)
- **Storage**: MinIO cluster (500 TB usable, 3× replication = 1.5 PB raw)
- **Network**: VPN/DirectConnect to AWS (query federation requires low-latency link)

**Cloud Infrastructure** (AWS, pricing as of Q4 2025):
- **S3**: 1.5 PB (90-day Standard $34K/month, 3-year Glacier $1.5K/month)
- **Kinesis**: 10 shards × $15/month = $150/month
- **EMR (Spark)**: Auto-scaling 3-10 nodes, $2K-$5K/month (batch jobs)

**Managed Services**:
- **Dremio Cloud**: $15K-$25K/month (based on compute units, query volume)
- **Fivetran**: $5K-$10K/month (SaaS connector subscriptions)
- **Polaris Cloud**: $2K-$5K/month (catalog metadata management)

---

### Cost Profile (Annual)

| Cost Category | Amount | Notes |
|---------------|--------|-------|
| **On-Prem Hardware** (amortized) | $60K/year | 3-year depreciation, $180K CapEx |
| **Cloud Storage** (S3) | $420K/year | Hot + cold tiers, 1.5 PB |
| **Dremio Cloud** | $180K-$300K/year | Primary query engine |
| **Fivetran** | $60K-$120K/year | Managed ingestion |
| **Polaris Cloud** | $24K-$60K/year | Catalog management |
| **AWS Compute** (EMR, Kinesis) | $30K-$60K/year | Batch processing |
| **Personnel** (1-2 data engineers) | N/A | Existing headcount |
| **TOTAL** | **$774K-$1,020K/year** | A.6-modeled; vs. Splunk $1.6M+ (~50% savings) |

**ROI**: 18-24 month payback, illustrative (A.6 model, vs. Splunk expansion cost avoided)

---

### When to Use This Pattern

✓ **Use If**:
- HIPAA, PCI-DSS, or other data residency compliance requirements
- Hybrid cloud strategy (some data on-prem, some cloud acceptable)
- 1-2 data engineers (limited capacity for self-hosted complexity)
- Budget: $300K-$1M annually
- 80/20 split: 20% data has compliance constraint, 80% cloud-compatible

✗ **Don't Use If**:
- Cloud-first mandate (no on-premises infrastructure acceptable)
- 0 data engineers (cannot maintain Kafka, Spark, MinIO cluster)
- All data has compliance constraint requiring on-prem (Pattern 4: traditional SIEM may be simpler)

---

### Migration Path

**Phase 1: Pilot (Months 1-3)**
- Deploy Dremio Cloud + AWS S3 Iceberg (non-PHI data only)
- Ingest 3-5 cloud data sources (CloudTrail, Okta, O365)
- 5-10 early adopter analysts test threat hunting workflows
- Prove value before touching PHI data (regulatory risk mitigation)

**Phase 2: On-Prem Deployment (Months 4-6)**
- Deploy MinIO cluster + Polaris self-hosted (PHI zone)
- Ingest 2-3 PHI-touching sources (clinical systems, EHR access logs)
- Federate on-prem + cloud via Dremio (unified query experience)
- SOC analysts query both zones through a single Dremio endpoint (row-level security enforced per zone)

**Phase 3: Full Migration (Months 7-12)**
- Migrate remaining data sources (15-20 additional sources)
- Decommission legacy SIEM (Splunk or equivalent)
- Optimize costs (S3 lifecycle policies, Dremio Reflection tuning)
- Training completion (all 15 security team members proficient)

---

## Pattern 2: Cloud-Native AWS-First

### Architecture Overview

**Problem Statement**:
- AWS-committed organization ($18M annual AWS spend)
- CTO mandate: use AWS-native services, avoid third-party where possible
- 3-5 data engineers available (can manage moderate complexity)
- Budget: $500K-$2M annually (cost optimization important but not sole driver)
- No on-premises constraint (cloud-first strategy)

**Solution**: AWS Athena + EMR + Glue with Iceberg on S3

---

### Architecture Diagram (Text-Based)

```
┌─────────────────────────────────────────────────────────────────────┐
│                     DATA SOURCES (2-4 TB/day)                       │
├─────────────────────────────────────────────────────────────────────┤
│ • AWS CloudTrail (multi-account)    • CrowdStrike EDR (API)        │
│ • VPC Flow Logs                     • Okta (SAML, API logs)        │
│ • AWS GuardDuty findings            • Office 365 (Audit logs)      │
│ • S3 Access Logs                    • Zeek network sensors         │
└─────────────────────────────────────────────────────────────────────┘
                                   ↓
                    ┌──────────────────────────────┐
                    │   INGESTION LAYER            │
                    ├──────────────────────────────┤
                    │ Real-time:                   │
                    │ • Kinesis Data Streams       │
                    │ • Lambda (transform)         │
                    │ • Kinesis Firehose → S3      │
                    │                              │
                    │ Batch:                       │
                    │ • AWS Glue ETL jobs          │
                    │ • Lambda (S3 event trigger)  │
                    └──────────────────────────────┘
                                   ↓
                    ┌──────────────────────────────┐
                    │   STORAGE LAYER              │
                    ├──────────────────────────────┤
                    │ AWS S3 (Multi-account)       │
                    │ • Raw bucket (bronze)        │
                    │ • Transformed (silver)       │
                    │ • OCSF-normalized (gold)     │
                    │                              │
                    │ Apache Iceberg Tables        │
                    │ • 90-day S3 Standard (hot)   │
                    │ • 3-year S3 Glacier (cold)   │
                    │ • Lifecycle policies         │
                    │                              │
                    │ AWS Glue Data Catalog        │
                    │ • Iceberg metadata           │
                    │ • Schema registry            │
                    └──────────────────────────────┘
                                   ↓
                    ┌──────────────────────────────┐
                    │   QUERY & PROCESSING         │
                    ├──────────────────────────────┤
                    │ Ad-hoc Queries:              │
                    │ • AWS Athena (Trino-based)   │
                    │ • Pay-per-query pricing      │
                    │ • Federated queries          │
                    │                              │
                    │ Batch Processing:            │
                    │ • AWS EMR (Spark)            │
                    │ • Iceberg maintenance        │
                    │ • OCSF transformations       │
                    │                              │
                    │ Orchestration:               │
                    │ • AWS Step Functions         │
                    │ • EventBridge (scheduling)   │
                    └──────────────────────────────┘
                                   ↓
┌─────────────────────────────────────────────────────────────────────┐
│                           CONSUMERS                                 │
├─────────────────────────────────────────────────────────────────────┤
│ • SOC analysts (Athena via AWS Console, SQL Workbench)             │
│ • QuickSight dashboards (Athena data source)                        │
│ • Security Hub (custom insights via Athena queries)                 │
│ • Lambda functions (automated threat hunting, response)             │
└─────────────────────────────────────────────────────────────────────┘
```

---

### Technology Stack

| Component | AWS Service | Open-Source Alternative | Rationale |
|-----------|-------------|------------------------|-----------|
| **Streaming Ingestion** | Kinesis Data Streams → Firehose | Apache Kafka | AWS-native, serverless, integrates with CloudWatch |
| **Batch Ingestion** | AWS Glue ETL | Apache Spark self-hosted | Managed Spark, no cluster management |
| **Storage** | S3 (Standard + Glacier) | MinIO (self-hosted) | AWS-native, lifecycle policies, 99.999999999% durability |
| **Table Format** | Apache Iceberg | Delta Lake, Hudi | Multi-engine (Athena, EMR, Redshift Spectrum) |
| **Catalog** | AWS Glue Data Catalog | Hive Metastore, Polaris | AWS-native, integrates with Athena, EMR, Redshift |
| **Query Engine** | AWS Athena (Iceberg; reads V2 spec, V3 features landing engine-by-engine) | Trino/Dremio self-hosted | Serverless (no cluster), pay-per-query ($5/TB scanned) |
| **Batch Processing** | AWS EMR (Spark) | Spark self-hosted | Iceberg compaction, OCSF transforms, auto-scaling |
| **Orchestration** | Step Functions + EventBridge | Apache Airflow | AWS-native, serverless, visual workflow |
| **Dashboards** | Amazon QuickSight | Tableau, Grafana | AWS-native, Athena integration, SPICE in-memory |

---

### Deployment Considerations

**AWS Account Structure**:
- **Security account**: Central security data lake (S3 buckets, Glue catalog)
- **Log producer accounts**: 50+ AWS accounts send logs to central security account
- **Cross-account access**: IAM roles, S3 bucket policies (least privilege)

**Cost Optimization**:
- **Athena query optimization**: Partition pruning (date-based queries), columnar Parquet format, Iceberg metadata filtering
- **S3 lifecycle policies**: Transition to Glacier Deep Archive after 90 days (reduce storage cost ~23× vs S3 Standard; AWS pricing, Q4 2025)
- **EMR auto-scaling**: Scale down to 0 nodes when idle (batch jobs run 2-4 hours daily)

**Security Considerations**:
- **IAM least privilege**: SOC analysts query via Athena (SELECT only, no DELETE/UPDATE)
- **S3 bucket encryption**: SSE-S3 or SSE-KMS (compliance requirement)
- **VPC endpoints**: Private connectivity (Athena, S3, Glue—no internet traffic)
- **CloudTrail logging**: Audit all Athena queries (who queried what data when)

---

### Cost Profile (Annual)

| Cost Category | Amount | Notes |
|---------------|--------|-------|
| **S3 Storage** | $180K-$300K/year | ~2.4-4.7 PB at 2-4 TB/day (90-day hot ~$4K-$8K/month, 3-year cold ~$8K-$16K/month; A.6 Step 3 rates) |
| **Athena Queries** | $120K-$240K/year | 2-4 TB scanned daily × $5/TB × 365 days |
| **EMR (Spark)** | $60K-$120K/year | Auto-scaling, 2-4 hours daily batch jobs |
| **Kinesis Streams** | $36K-$72K/year | 20 shards (~$3.6K) + PUT-payload units at 2-4 TB/day ingest (dominant cost) + extended retention |
| **Glue ETL** | $24K-$48K/year | DPU-hours for transformations |
| **Data Transfer** | $12K-$24K/year | Cross-region (if multi-region), VPC endpoints |
| **QuickSight** | $12K-$24K/year | 50 users × $24/user/month |
| **Personnel** (3-5 data engineers) | N/A | Existing headcount |
| **TOTAL** | **$444K-$828K/year** | A.6-modeled; vs. schema-on-read SIEM $1.5M-$4.4M/year at 2 TB/day (Worksheet A.6, Step 2) — the $12M Splunk figure belongs to Pattern 4's 10-12 TB/day Marcus case (Ch.6), a different volume tier, not this pattern's |

**ROI**: 12-18 month payback, illustrative (A.6 model, vs. Splunk expansion cost avoided)

---

### When to Use This Pattern

✓ **Use If**:
- AWS-committed organization (AWS Enterprise Support, heavy AWS investment)
- Cloud-first strategy (no on-premises constraint)
- 3-5 data engineers available (can manage AWS-native services)
- Budget: $400K-$1M annually
- Comfortable with pay-per-query pricing model (vs. always-on cluster cost)

✗ **Don't Use If**:
- Multi-cloud requirement (Azure + GCP alongside AWS)
- Real-time detection <30 seconds required (Athena's batch ingestion path adds roughly a minute or more of latency — illustrative, pipeline-dependent — so it misses a sub-30-second target)
- On-premises data residency required (HIPAA PHI, air-gapped)
- 0-1 data engineers (even AWS-managed requires some operational support)

---

### Migration Path

**Phase 1: Pilot (Months 1-3)**
- Deploy S3 + Glue Catalog + Athena in single AWS account
- Ingest 3-5 AWS-native sources (CloudTrail, VPC Flow, GuardDuty)
- 10-15 early adopter analysts test Athena SQL queries
- Baseline cost (query spend, storage cost)

**Phase 2: Multi-Account Federation (Months 4-6)**
- Expand to 10-20 AWS accounts (centralized security data lake)
- Deploy Kinesis streams for real-time ingestion
- EMR for Iceberg compaction (small file optimization)
- QuickSight dashboards for SOC (top 10 high-value use cases)

**Phase 3: Full Production (Months 7-12)**
- Integrate non-AWS sources (EDR, SaaS) via Glue ETL or Fivetran
- OCSF normalization (EMR Spark jobs transform raw → OCSF)
- Decommission legacy SIEM (if applicable)
- Cost optimization (query pattern analysis, partition tuning)

---

## Pattern 3: Multi-Cloud Federated (Denodo Virtualization)

### Architecture Overview

**Problem Statement**:
- Multi-national organization (EU, US, China operations)
- Data sovereignty requirements: EU data stays in EU, China data stays in China
- Cannot consolidate to single cloud region (violates GDPR, Chinese data localization laws)
- M&A complexity: Acquired companies bring legacy systems, different cloud providers
- Budget: $2M+ annually (premium acceptable for compliance + complexity)

**Solution**: Denodo data virtualization with regional Iceberg deployments

---

### Architecture Diagram (Text-Based)

```
┌─────────────────────────────────────────────────────────────────────┐
│                     REGIONAL DATA SOURCES                           │
├─────────────────────────────────────────────────────────────────────┤
│ EU Region (GDPR)         │ US Region              │ China Region    │
│ • EU CloudTrail          │ • US CloudTrail        │ • Alibaba Cloud │
│ • EU Office 365          │ • US Office 365        │ • WeChat logs   │
│ • EU employee data       │ • US financial systems │ • China ERP     │
└─────────────────────────────────────────────────────────────────────┘
           ↓                          ↓                       ↓
┌──────────────────────┐  ┌──────────────────────┐  ┌──────────────────────┐
│ EU Data Lake         │  │ US Data Lake         │  │ China Data Lake      │
│ (AWS eu-west-1)      │  │ (AWS us-east-1)      │  │ (Alibaba cn-north-1) │
├──────────────────────┤  ├──────────────────────┤  ├──────────────────────┤
│ • S3 (EU region)     │  │ • S3 (US region)     │  │ • OSS (Alibaba)      │
│ • Iceberg tables     │  │ • Iceberg tables     │  │ • Iceberg tables     │
│ • 90-day retention   │  │ • 90-day retention   │  │ • 90-day retention   │
│ • Trino (query)      │  │ • Trino (query)      │  │ • Trino (query)      │
└──────────────────────┘  └──────────────────────┘  └──────────────────────┘
           ↓                          ↓                       ↓
           └──────────────────────────┼───────────────────────┘
                                      ↓
                       ┌──────────────────────────────┐
                       │   DENODO VIRTUALIZATION      │
                       │   (US + EU deployment)       │
                       ├──────────────────────────────┤
                       │ Federated Query Layer:       │
                       │ • Query routing by region    │
                       │ • No data movement           │
                       │ • Join EU + US (not China)   │
                       │ • Row-level security         │
                       │ • Query caching              │
                       └──────────────────────────────┘
                                      ↓
┌─────────────────────────────────────────────────────────────────────┐
│                           CONSUMERS                                 │
├─────────────────────────────────────────────────────────────────────┤
│ Global SOC (EU):                                                    │
│ • Query EU + US (federated, compliant with GDPR)                    │
│ • Cannot query China (data sovereignty isolation)                   │
│                                                                     │
│ China SOC (Beijing):                                                │
│ • Query China region only (local Trino, no federation)             │
│ • Isolated network (Great Firewall compliance)                     │
└─────────────────────────────────────────────────────────────────────┘
```

---

### Technology Stack

| Component | Technology | Region | Rationale |
|-----------|------------|--------|-----------|
| **Storage (EU)** | AWS S3 (eu-west-1) + Iceberg | EU | GDPR data residency |
| **Storage (US)** | AWS S3 (us-east-1) + Iceberg | US | US operations |
| **Storage (China)** | Alibaba OSS + Iceberg | China | Chinese data localization laws |
| **Query (Regional)** | Trino self-hosted | All regions | Local query processing |
| **Virtualization** | Denodo Platform | US + EU | Federated query without data movement |
| **Catalog** | Polaris (regional instances) | All regions | Metadata management |
| **Orchestration** | Apache Airflow (regional) | All regions | Region-specific batch jobs |

---

### Deployment Considerations

**Data Sovereignty Compliance**:
- **EU → US query**: Allowed via Denodo federation (no data leaves EU, query executes in EU, results aggregated)
- **US → EU query**: Allowed (EU GDPR allows data export with proper controls)
- **China isolation**: NO federation with EU/US (Chinese data localization law prohibits cross-border data transfer)

**Network Architecture**:
- **VPN/DirectConnect**: EU ↔ US (low-latency for federated queries)
- **China isolated**: Separate network, local Trino only (no Denodo federation)
- **Latency**: EU-US federated queries carry a few seconds of cross-region overhead on top of a local query (illustrative, not a lab-measured figure; depends on link latency and result size)

**Query Performance**:
- **Federated query overhead**: typically several times slower than a local query from network latency and coordination (order-of-magnitude expectation, not a measured constant)
- **Use cases**: Cross-region correlation (rare: 5-10% of queries), most queries regional (90-95%)
- **Optimization**: Denodo query caching (repeated federated queries served from cache)

---

### Cost Profile (Annual)

| Cost Category | Amount | Notes |
|---------------|--------|-------|
| **Storage (EU)** | $150K-$250K/year | S3 + Glacier, 1 PB |
| **Storage (US)** | $150K-$250K/year | S3 + Glacier, 1 PB |
| **Storage (China)** | $100K-$200K/year | Alibaba OSS, 500 TB |
| **Trino (3 regions)** | $180K-$360K/year | Self-hosted clusters ($60K-$120K per region) |
| **Denodo Platform** | $400K-$800K/year | Enterprise license + professional services; large multi-region/many-connector deployments (e.g. Appendix K.3) run higher, ~$1.2M/year |
| **Network (VPN/DX)** | $60K-$120K/year | Cross-region connectivity |
| **Personnel** (5+ data engineers) | N/A | Distributed team (1-2 per region) |
| **TOTAL** | **$1.04M-$1.98M/year** | A.6-modeled; premium for multi-region complexity |

**vs. Regional SIEM**: ~$4M-$8M/year on the A.6 model (Splunk EU + Splunk US + Splunk China ≈ 3× licensing, illustrative)

**ROI**: 24-36 month payback, illustrative (A.6 model; longer due to Denodo licensing cost, justified by compliance)

---

### When to Use This Pattern

✓ **Use If**:
- Multi-national operations with data sovereignty requirements (GDPR EU, China localization)
- M&A complexity (multiple cloud providers, legacy systems to federate)
- Cross-region correlation requirement (5-10% of queries span regions)
- Budget: $1M-$3M annually (premium for virtualization licensing)
- 5+ data engineers (distributed team, can manage regional complexity)

✗ **Don't Use If**:
- Single-region operations (Pattern 1 or 2 simpler and cheaper)
- Budget <$1M annually (Denodo licensing expensive for small orgs)
- High query volume requiring sub-second latency (federated queries add overhead)

---

### Migration Path

**Phase 1: Regional Deployments (Months 1-6)**
- Deploy Iceberg + Trino in each region independently (EU, US, China)
- Ingest regional data sources (no federation yet)
- Establish baseline: regional queries work correctly, analysts comfortable

**Phase 2: EU-US Federation (Months 7-9)**
- Deploy Denodo in US + EU (not China—isolated by design)
- Configure federated queries (EU analysts query EU + US)
- Test cross-region correlation use cases (lateral movement spanning regions)

**Phase 3: Optimization (Months 10-12)**
- Denodo query caching (reduce federated query overhead)
- Cost optimization (minimize cross-region data transfer)
- China remains isolated (compliance audit validation)

---

## Pattern 4: Traditional SIEM (Splunk Enterprise Security)

### Architecture Overview

**Problem Statement**:
- Real-time detection regulatory requirement (<30 seconds alert latency)
- 0 data engineers (SOC analysts only, no platform engineering team)
- Operational simplicity valued over cost optimization
- SEC fraud detection mandate (financial services) or equivalent regulatory driver

**Solution**: Splunk Enterprise Security (turnkey platform)

---

### Architecture Diagram (Text-Based)

```
┌─────────────────────────────────────────────────────────────────────┐
│                     DATA SOURCES                                    │
├─────────────────────────────────────────────────────────────────────┤
│ • EDR (CrowdStrike)              • Cloud (AWS, Azure, GCP)          │
│ • Network (Zeek, Palo Alto)      • SaaS (Okta, O365, Salesforce)   │
│ • Endpoints (Sysmon, Windows)    • Applications (Web servers, DBs)  │
└─────────────────────────────────────────────────────────────────────┘
                                   ↓
                    ┌──────────────────────────────┐
                    │   INGESTION LAYER            │
                    ├──────────────────────────────┤
                    │ Splunk Universal Forwarders  │
                    │ • Agent-based collection     │
                    │ • Real-time forwarding       │
                    │ • TLS encryption             │
                    │                              │
                    │ Splunk Heavy Forwarders      │
                    │ • Pre-processing (parsing)   │
                    │ • Routing, filtering         │
                    │ • Load balancing             │
                    └──────────────────────────────┘
                                   ↓
                    ┌──────────────────────────────┐
                    │   INDEXING LAYER             │
                    ├──────────────────────────────┤
                    │ Splunk Indexers (Clustered)  │
                    │ • tsidx (proprietary format) │
                    │ • 30-90 day hot retention    │
                    │ • Replication factor: 3      │
                    │ • Search factor: 2           │
                    └──────────────────────────────┘
                                   ↓
                    ┌──────────────────────────────┐
                    │   SEARCH & ANALYTICS         │
                    ├──────────────────────────────┤
                    │ Splunk Search Heads          │
                    │ • SPL (Search Processing)    │
                    │ • Distributed search         │
                    │ • Dashboards, alerts         │
                    │                              │
                    │ Enterprise Security (ES)     │
                    │ • ~1,700 correlation rules   │
                    │ • Risk-based alerting        │
                    │ • Threat intelligence        │
                    │ • Incident review            │
                    └──────────────────────────────┘
                                   ↓
┌─────────────────────────────────────────────────────────────────────┐
│                           CONSUMERS                                 │
├─────────────────────────────────────────────────────────────────────┤
│ • SOC analysts (SPL queries, ES dashboards)                         │
│ • Incident responders (investigation workflows)                     │
│ • SOAR integration (Splunk Phantom playbooks)                       │
│ • Executive dashboards (pre-built security posture views)           │
└─────────────────────────────────────────────────────────────────────┘
```

---

### Technology Stack

| Component | Technology | Alternative | Why Splunk Wins |
|-----------|------------|-------------|-----------------|
| **Ingestion** | Universal/Heavy Forwarders | Filebeat, Logstash | Real-time (<5 sec), agent-based, mature connectors |
| **Storage** | Splunk tsidx | Iceberg, Parquet | Indexed (not columnar) optimized for SPL queries |
| **Query Language** | SPL | SQL, KQL | Purpose-built for security (streamstats, transaction, tstats) |
| **Detection** | ES Correlation Searches | Custom rules | ~1,700 pre-built rules, tuned for low false positives |
| **SOAR** | Splunk Phantom | Third-party | Native integration, single-vendor support |
| **ML** | MLTK (Machine Learning Toolkit) | Separate ML platform | Built-in, no integration required |

---

### When to Use This Pattern

✓ **Use If**:
- **Real-time detection <30 seconds** (regulatory requirement: SEC fraud, PCI-DSS, SWIFT)
- **0 data engineers** (SOC analysts only, no platform engineering team)
- **Operational simplicity** valued over cost optimization
- **Budget: $2M-$12M annually** (enterprise scale, 1-10 TB/day)
- **Risk-averse culture** ("nobody got fired for buying Splunk")

✗ **Don't Use If**:
- **Cost optimization priority** (on the A.6 model, schema-on-read SIEM runs several times more expensive than a lakehouse stack of Iceberg on S3 + Athena or Trino — the 3-10× figure tracks the savings tiers in this appendix's cost tables)
- **Multi-year queryable retention** (Splunk archives to offline, not queryable)
- **3+ data engineers available** (lakehouse stack viable with team capacity)
- **Budget <$2M annually** at volume (10+ TB/day unsustainable on Splunk pricing)

---

### Cost Profile (Annual)

The tiers below are A.6-model outputs: the SIEM column derives from schema-on-read list pricing (the same G-Cloud-reconciled Splunk curve A.6 uses, with an enterprise discount applied), and the modern-stack column from the AWS-on-Iceberg sizing in that worksheet. Treat them as illustrative for the stated volumes, not quoted invoices.

| Ingestion Volume | Schema-on-Read SIEM Cost (Enterprise) | Modern Stack Alternative | Savings |
|------------------|---------------------------------------|--------------------------|---------|
| **1 TB/day** | $1.2M-$2M/year | $300K-$600K/year | 50-75% |
| **5 TB/day** | $6M-$10M/year | $800K-$1.5M/year | 75-85% |
| **10 TB/day** | $12M-$20M/year | $1.2M-$2.5M/year | 85-90% |

**Variants-chapter case study** (Marcus Financial Services, from the "what good looks like" material — Chapter 6 of the handbook):
- Volume: 10 TB/day (Path A: full lakehouse migration to Iceberg on S3 + Athena)
- Schema-on-read SIEM renewal: $12M/year
- Modern stack (Athena): $2.9M/year
- **Savings: $9.1M/year (76%)**

> **Note on volume differences**: The cost comparison table above uses standard volume tiers (1/5/10 TB/day) as reference points. The variants chapter's Marcus scenario uses 10-12 TB/day specific to his financial services organization. Cost estimates scale roughly linearly for ingestion/storage but benefit from volume discounts at higher tiers — actual savings percentages at 12 TB/day may exceed the 85-90% shown for 10 TB/day due to better S3 and compute pricing tiers.

**When Splunk Still Wins** (Marcus Path B):
- SEC real-time fraud detection mandate (<30 seconds)
- Team capacity dropped from 3 → 1 engineer
- **Decision**: Accept $9.1M/year premium for operational simplicity + real-time compliance

---

## Pattern 5: MOAR Multi-Engine Architecture

### Architecture Overview

**Problem Statement**:
- Diverse workload types with conflicting optimization requirements
- 3-5 data engineers (can manage hybrid complexity)
- Cost optimization important (50-75% savings target)
- No single-engine solution optimal for all workloads

**Solution**: Workload-routed multi-engine architecture

---

### Architecture Diagram

```
┌─────────────────────────────────────────────────────────────────────┐
│                     DATA SOURCES (5 TB/day)                         │
└─────────────────────────────────────────────────────────────────────┘
                                   ↓
                    ┌──────────────────────────────┐
                    │   UNIFIED STORAGE            │
                    ├──────────────────────────────┤
                    │ Apache Iceberg on S3/MinIO   │
                    │ • Single table format        │
                    │ • Multi-engine read/write    │
                    │ • 90-day S3 Standard (hot)   │
                    │ • 3-year Glacier (cold)      │
                    └──────────────────────────────┘
                                   ↓
                    ┌──────────────────────────────┐
                    │   QUERY ROUTING              │
                    │   (Workload-aware)           │
                    └──────────────────────────────┘
               ↓               ↓               ↓               ↓
┌─────────────┐  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐
│ DREMIO      │  │ TRINO       │  │ SPARK       │  │ DUCKDB      │
│ (Dashboards)│  │ (Hunting)   │  │ (Maintenance│  │ (Edge)      │
├─────────────┤  ├─────────────┤  ├─────────────┤  ├─────────────┤
│ Reflections │  │ MPP queries │  │ Compaction  │  │ Lambda      │
│ <1 sec      │  │ <60 sec     │  │ Snapshots   │  │ 50-80% ↓    │
│ BI tools    │  │ Ad-hoc SQL  │  │ Schema evo  │  │ volume      │
└─────────────┘  └─────────────┘  └─────────────┘  └─────────────┘
       ↓                ↓                ↓                ↓
┌─────────────────────────────────────────────────────────────────────┐
│ WORKLOAD ROUTING LOGIC                                              │
├─────────────────────────────────────────────────────────────────────┤
│ IF frequency = 'high' AND source = 'dashboard' → Dremio            │
│ ELSE IF workload = 'iceberg_maintenance' → Spark                   │
│ ELSE IF query_type = 'ad_hoc_investigation' → Trino                │
│ ELSE IF location = 'edge' → DuckDB                                 │
└─────────────────────────────────────────────────────────────────────┘
```

---

### Workload Routing Decision Tree

```
┌─────────────────────┐
│ Query Request       │
└──────────┬──────────┘
           ↓
    ┌──────────────┐
    │ Dashboard?   │ YES → ┌────────────┐
    │ (High freq)  │────→  │ DREMIO     │
    └──────┬───────┘       │ Reflections│
           │ NO            │ <1 sec     │
           ↓               └────────────┘
    ┌──────────────┐
    │ Iceberg      │ YES → ┌────────────┐
    │ Maintenance? │────→  │ SPARK      │
    └──────┬───────┘       │ Compaction │
           │ NO            │ Native ops │
           ↓               └────────────┘
    ┌──────────────┐
    │ Ad-hoc       │ YES → ┌────────────┐
    │ Hunting?     │────→  │ TRINO      │
    └──────┬───────┘       │ MPP        │
           │ NO            │ Interactive│
           ↓               └────────────┘
    ┌──────────────┐
    │ Edge         │ YES → ┌────────────┐
    │ Processing?  │────→  │ DUCKDB     │
    └──────────────┘       │ 50-80% ↓   │
                           │ volume     │
                           └────────────┘
```

---

### Technology Stack

| Workload | Engine | Why This Engine | Alternative |
|----------|--------|----------------|-------------|
| **Real-time Dashboards** | Dremio Cloud | Reflections (<1 sec), BI acceleration | ClickHouse (won the most aggregation-shaped query in my single-host Tier-B join bench; more infrastructure to operate) |
| **Ad-hoc Threat Hunting** | Trino | MPP interactive, federation, no cache overhead | Athena (serverless but slower) |
| **Table Maintenance** | Apache Spark | Most mature for Iceberg compaction (Trino/Flink/Dremio also support it) | Trino / Flink / Dremio |
| **Edge Preprocessing** | DuckDB | volume reduction at the edge (the 50-80% figure is illustrative and filter-dependent, not a measured constant), Lambda-compatible | Flink (overkill for simple filtering) |

---

### Cost Profile (Annual)

| Cost Category | Amount | Notes |
|---------------|--------|-------|
| **Dremio Cloud** | $60K-$120K/year | Dashboards only (10-20% of queries) |
| **Trino (self-hosted)** | $48K-$96K/year | 5-10 node cluster, threat hunting |
| **Spark (EMR/Databricks)** | $36K-$72K/year | Batch jobs (compaction), 2-4 hours daily |
| **DuckDB** | $0/year | Open-source, Lambda execution cost only |
| **S3 Storage** | $180K-$300K/year | 3 PB (hot + cold) |
| **Personnel** (3-5 engineers) | N/A | Existing headcount |
| **TOTAL** | **$324K-$588K/year** | A.6-modeled; vs. single engine $800K-$1.2M (~50-75% savings, illustrative) |

---

### When to Use This Pattern

✓ **Use If**:
- Diverse workloads (dashboards, hunting, forensics, maintenance)
- 3-5 data engineers (can manage multi-engine complexity)
- Cost optimization important (50-75% savings vs. single platform)
- Comfortable with "best tool for the job" philosophy

✗ **Don't Use If**:
- 0-2 data engineers (operational complexity too high)
- Organizational preference for vendor consolidation (single-platform simplicity)
- Real-time detection <30 seconds required (need Flink, not batch-oriented stack)

---

## Materialized Views Strategy for MOAR Architectures

**Applies to**: Pattern 1 (Healthcare Hybrid), Pattern 2 (AWS-First), Pattern 5 (Multi-Engine)

Appendix I.4B works through the trade-off in detail, and the short version is that materialized views buy 78× to 9,000× query speedups in the vendor literature — though the SDW Lab's own first-party measurement (CV-gated, single host, Tier B) lands far more modestly, at 45–77× on three SOC rollups (76.8× class-rollup, 53.6× time-series, 45.3× failed-auth), at the low end of that vendor range and nowhere near 9,000×, which is the honest independently-reproduced anchor for the claim — but security data's own characteristics (high data change rates, schema volatility, complex correlation requirements) create failure modes that make selective deployment the right default rather than turning views on everywhere.

### When to Add Materialized Views to Your Architecture

**Deploy materialized views when ALL criteria met**:

1. **Query frequency >> Data change rate** (12:1 ratio minimum)
   - Example: Dashboard refreshing every 5 minutes, data updating every hour

2. **Refresh cost < Query cost savings** (10× benefit minimum)
   - Example: $50/day refresh cost, $500/day query savings

3. **Schema stability** (source schema changes <1×/month)
   - Example: OCSF-normalized logs with stable schema

4. **IVM-compatible query patterns** (simple aggregations, single-table or append-only multi-table)
   - Example: `SELECT user_id, COUNT(*) FROM auth_logs WHERE result='failed' GROUP BY user_id`

5. **Measured benefit** (pilot 3-5 views, validate before expanding)
   - Example: Pilot compliance dashboard views, measure actual query savings

**Avoid materialized views when ANY of following true**:

- Schema volatility (new log sources weekly, vendor format changes monthly)
- Complex correlation requirements (5-table joins with window functions, MEDIAN/PERCENTILE aggregates)
- Unpredictable query patterns (threat hunting workloads where queries written during investigations)
- High data change rates (all source tables updating continuously)
- Insufficient operational expertise (team lacks experience debugging MV refresh failures)

### Four-Tier Materialization Strategy

**Pattern 1, 2, or 5 can incorporate this layered approach**:

**1. Streaming Layer** (sub-second latency)
- **Platform**: Kafka + Flink or Materialize for complex correlations
- **Use case**: Real-time detection rules requiring immediate alerting
- **Example**: Count failed authentications per user in 5-minute windows, alert when >10
- **Deployment**: Run alongside Pattern 5 Trino/Dremio (separate streaming infrastructure)

**2. Micro-batch Layer** (5-15 minute refresh)
- **Platform**: Dremio Reflections (Pattern 1, 5), AWS Athena + Lambda (Pattern 2)
- **Use case**: Behavioral baselines and correlation rules within IVM capability boundaries
- **Example**: Median processes created per user per day (simple aggregation, append-only)
- **Deployment**: Enable Dremio Reflections selectively for 3-5 high-value dashboards

**3. Batch Layer** (daily/weekly full refresh)
- **Platform**: Scheduled Spark jobs (Pattern 1, 2, 5), dbt models with full refresh
- **Use case**: Complex analytics, historical baselines, compliance reporting
- **Example**: 95th percentile authentication time per user (30-day rolling window)
- **Deployment**: Airflow DAG triggering Spark job nightly at 2 AM

**4. Data Lake Layer** (schema-on-read, no materialization)
- **Platform**: Iceberg tables with Trino/Dremio (Pattern 1, 5), Athena (Pattern 2)
- **Use case**: Ad-hoc threat hunting, unpredictable query patterns
- **Example**: "Show me all DNS queries to domains registered in the last 48 hours"
- **Deployment**: Default—most queries go here (90-95%), materialized views selective (5-10%)

### Implementation Guidance by Pattern

The per-month cost and ROI figures in this section are A.6-model projections for the example workloads, illustrative rather than measured; the independently-reproduced speedup anchor is the 45-77× SDW Lab range stated at the top of this section, and the per-pattern multipliers below should be re-derived against your own query frequency and refresh cost.

**Pattern 1 (Healthcare Hybrid with Dremio)**:
- Enable Dremio Reflections for 3-5 compliance dashboards (HIPAA audit queries)
- Example: Daily authentication statistics, failed access attempts per user
- Cost: $5K-$10K/month additional Dremio DCU for reflection storage (A.6-modeled)
- ROI: ~10-30× query cost savings for high-frequency dashboards (illustrative, workload-dependent)

**Pattern 2 (AWS-First with Athena)**:
- Create AWS Glue scheduled crawlers for incremental materialized view refresh
- Example: Athena CTAS (CREATE TABLE AS SELECT) job running nightly
- Cost: $1K-$3K/month Glue ETL + S3 storage for materialized tables (A.6-modeled)
- ROI: ~5-20× query cost savings, reducing Athena query scan volume (illustrative, workload-dependent)

**Pattern 5 (Multi-Engine Modern Stack)**:
- Use Dremio Reflections for dashboards (Tier 2)
- Use Spark for batch materialized views (Tier 3)
- Keep Trino for ad-hoc hunting (Tier 4—no materialization)
- Cost: Already included in Dremio Cloud + Spark costs
- ROI: Incremental, since it enables <1 second dashboards without additional infrastructure

**Pattern 4 (Traditional SIEM)**: N/A
- Schema-on-read SIEM Data Model Acceleration = built-in materialized views (51-270× speedups documented; Splunk Data Model Acceleration docs, docs.splunk.com — vendor docs, Tier C)
- Enable for high-value use cases (CIM-compliant dashboards)
- Cost: Included in Splunk licensing
- ROI: Performance improvement only (no separate cost)

### Operational Patterns for Success

**Pattern: Staging View Layer** (Absorb schema volatility)

```sql
-- Staging view handles vendor field name variations
CREATE VIEW auth_logs_stable AS
SELECT
    COALESCE(user_id, user_name) as user_id,
    COALESCE(src_ip, source_ip) as source_ip,
    timestamp,
    auth_result
FROM auth_logs_raw;

-- Materialized view references stable schema
CREATE MATERIALIZED VIEW auth_failures AS
SELECT user_id, source_ip, DATE_TRUNC('hour', timestamp) as hour,
       COUNT(*) as failed_count
FROM auth_logs_stable
WHERE auth_result = 'failed'
GROUP BY user_id, source_ip, DATE_TRUNC('hour', timestamp);
```

Schema changes in `auth_logs_raw` only require updating the staging view logic, and the materialized view is unaffected unless you add entirely new columns.

**Pattern: Monitor View Economics** (Track ROI)

Track per-view metrics:
- Query frequency (actual, not estimated)
- Query cost savings = (baseline query cost - materialized query cost) × frequency
- Refresh cost (compute + storage)
- Schema change frequency (manual intervention triggers)
- Net benefit = Savings - Refresh cost - Operational overhead

**Alert when**: Net benefit < 0 (refresh costs exceed query savings) → disable view

### Cost Impact Examples

Both examples below are illustrative arithmetic on A.6-model assumptions (assumed per-query cost, scan volume, and refresh cost), not measured bills; the dollar figures carry only as much precision as those inputs.

**Example 1: Compliance Dashboard (Pattern 1 Healthcare Hybrid)**

**Before materialized view**:
- Query: "Failed HIPAA access attempts, last 24 hours"
- Data scanned: 50 GB/day
- Query frequency: 288 queries/day (every 5 minutes)
- Query cost: $0.50 per query × 288 = **$144/day**

**After Dremio Reflection**:
- Refresh cost: $1.50/day (incremental, process new hour's data)
- Query cost: $0.05 per query × 288 = $14.40/day
- **Total cost**: $15.90/day
- **Savings**: $128/day = **$46,720/year** for single dashboard tile

**ROI**: Reflection storage cost ($200/month) vs savings ($46K/year) = **23× annual ROI**

**Example 2: Threat Hunting (Pattern 5 Multi-Engine)**

**Use case**: Ad-hoc lateral movement investigation
- Query pattern: Unique every investigation (5-table joins, window functions)
- Query frequency: 30 queries/week (unpredictable timing)
- Materialized view benefit: **ZERO** (queries never repeat, complex patterns unsupported)

**Recommendation**: Route to Trino (Tier 4 data lake layer), no materialization. Trino query cost acceptable for low-frequency unpredictable patterns.

### When materialization earns its keep

The Netflix 5 PB/day deployment (Appendix I.4A) is a useful reminder that running the query layer without leaning on materialized views can be a valid and durable choice — the public Netflix material reaches sub-second queries through base-table and ingest-path engineering rather than materialization, and operational simplicity and schema flexibility can outweigh query performance optimization, particularly when the data changes fast enough that refresh cost exceeds the query savings. The 78× to 9,000× speedups in the literature only translate to real cost reduction when query frequency materially exceeds the data change rate, so the right entry point is a pilot of 3-5 high-value, stable use cases (compliance dashboards, scheduled reports) with measured ROI before any broader rollout. Security data creates failure modes that general BI analytics don't face, the high change rates and schema volatility and multi-table correlation patterns that IVM implementations don't handle, which is why the four-tier model above (streaming → micro-batch → batch → data lake) distributes work across the right tool for each tier rather than applying materialization as a universal pattern.

**For detailed platform comparisons** (Dremio Reflections vs Snowflake Dynamic Tables vs Databricks MVs vs Materialize vs ksqlDB vs Flink), see ["Materialized Views for Security Data: What Actually Works at Petabyte Scale"](https://securitydataworks.com/writing/engines/materialized-views) on securitydataworks.com.

**For materialized views decision framework**, see Appendix I.4B.

**For OCSF normalization at ingestion** (the schema stability foundation for successful materialized views), see Appendix H.

---

## Quick Reference: Pattern Selection Matrix

The estimated-cost column repeats the A.6-modeled figures from each pattern above (Q4 2025 rates, illustrative for the stated volumes), not quoted prices.

| Your Constraint | Recommended Pattern | Estimated Cost | Timeline |
|-----------------|-------------------|----------------|----------|
| **HIPAA/PCI on-prem + cloud** | Pattern 1: Healthcare Hybrid | $774K-$1,020K | 9-12 months |
| **AWS-committed, cloud-first** | Pattern 2: Cloud-Native AWS | $444K-$828K | 9-12 months |
| **Multi-region sovereignty (EU/US/China)** | Pattern 3: Multi-Cloud Federated | $1.04M-$1.98M | 12-18 months |
| **0 engineers, real-time <30 sec** | Pattern 4: Traditional SIEM | $2M-$12M | 3-6 months |
| **3-5 engineers, cost optimization** | Pattern 5: Multi-Engine Modern | $324K-$588K | 9-15 months |

---

These reference architectures provide:
- **Visual diagrams** (text-based, adaptable to your diagramming tool)
- **Technology stacks** with alternatives and rationale
- **Cost profiles** with annual TCO estimates
- **When to use** (and when NOT to use) each pattern
- **Migration paths** (phased rollout timelines)

**Next**: Appendix D (Glossary Translation Guide) provides security ↔ data engineering terminology translations.
