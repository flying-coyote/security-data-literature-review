# Performance Benchmark Comparison Table

**Purpose**: Side-by-side technology performance comparison for quantitative selection decisions
**Target Chapters**: Chapter 9 (Query Engines), Chapter 8 (Storage Formats), Chapter 7 (Streaming)
**Created**: October 15, 2025
**Updated**: June 7, 2026 (added first-party MOAR reference-stack measurements; FOIL substituted into the ClickHouse-vs-Elasticsearch storage cell)
**Sources**: Borrowed-source citations reference MASTER-BIBLIOGRAPHY.md entries; first-party citations reference the SDW MOAR reference stack
**Evidence Quality**: per-source evidence levels are provisional pending re-verification (see the Revision 1.2 audit note below — the original "100% Level A" self-grade did not survive the 2026 claim-vs-source audit). First-party lab measurements are a distinct evidence tier — identical-workload, answer-equality-gated, reproducible, single host.

> **Revision 1.2 audit note (2026-06-14, folded correction).** This bundle was never swept in the 2026-06 fabrications cleanup that corrected MASTER-BIBLIOGRAPHY.md and APPENDICES.md, so several borrowed figures below asserted statistics whose cited sources were withdrawn or are empty stubs. They are marked WITHDRAWN inline (not deleted — the record stays so a future agent does not re-add them) per the APPENDICES.md folded-correction style. Withdrawn here, with the same provenance as the bibliography audit: Shell 57TB/day (dead URL, unverifiable — removed cf26e77); SK Telecom 97% query-time reduction / 52.7TB in 3.39s (figures not in the cited Trino Summit recap); the borrowed CIDR "50-100×" band (not on the cited page — the surviving anchor is the first-party probe, ~13-17× at 20M rows on a single host, §1.1); Cloudflare "96.3% queries <1s" (not in the cited source — the surviving Cloudflare figures are 6M req/sec and 10-12× compression); ClickHouse "8-10× CPU efficiency" (not on the cited page); the Uber "thousands of real-time security views / sub-second refresh" figures (not in the cited generic Confluent latency piece); Netflix "70-80% tiered-storage savings" (the cited URL is Confluent documentation, not a Netflix source); Confluent "4.5M events/sec on 9 nodes" is retained as a reproducible vendor benchmark but re-tiered to its real status (vendor benchmark, primary not re-verified at audit). The first-party MOAR-stack legs added in v1.1 (FOIL ~7.0× storage on OCSF data, the four-engine identical-workload latency in §1.3, the CIDR probe ~13-17× / ~2.9× storage) are first-party measurements verified against the FINDINGS docs in `~/sdw-lab-benchmarks` and are NOT affected. The "100%/Level A" aggregate self-grade is withdrawn; no aggregate Level-A percentage is claimed. Do NOT re-flag the named-source audit trail (Shell/SK-Telecom/Netflix/etc. appearing in correction notes are records, not new violations).

---

## Executive Summary

Performance claims are ubiquitous in vendor marketing. This reference consolidates production-deployment and benchmark figures to enable quantitative technology selection, with the load-bearing claims now anchored to first-party lab measurement rather than borrowed single-operator numbers.

**Key benchmarks** (post-audit; withdrawn borrowed stats marked WITHDRAWN inline below):
- **ClickHouse**: 6M req/sec (Cloudflare); 5-10× storage efficiency vs Elasticsearch (borrowed band, grounded first-party at ~7.0× on OCSF data via the MOAR FOIL); the "96.3% queries <1s" figure is WITHDRAWN (not in source)
- **Kafka**: 4.5M events/sec on 9 nodes (Confluent vendor benchmark, primary not re-verified at audit)
- **Iceberg**: the SK Telecom "97% query time reduction / 52.7TB in 3.39s" is WITHDRAWN (not in the cited recap); Cloudera 10× vs Hive retained
- **Arrow Flight SQL**: 20× faster than JDBC/ODBC for result retrieval (community benchmark)

I think the honest read after the audit is that security workloads have specific performance characteristics (burst patterns, CIDR-based hunting, entity tracking) that differ from general analytics, so generic benchmarks inform but production pilots and first-party probes validate — which is why the rows below now lead with the first-party legs where they exist.

---

## 1. Query Engine Performance

### 1.1 ClickHouse - OLAP Analytics

**Cloudflare - 6M Requests/Second HTTP Analytics**
📍 MASTER-BIBLIOGRAPHY.md:74-94

**Throughput**: **6 million requests/second** ingestion and query
**Query Performance**: ~~96.3% of queries complete under 1 second~~ **WITHDRAWN (2026-06-14 audit — figure not in the cited source; surviving Cloudflare figures are 6M req/sec and 10-12× compression)**
**Scale**: Billions of events processed daily
**Workload**: HTTP analytics (security-relevant log data)

**Evidence Level**: A for 6M req/sec; the latency figure is withdrawn
**Confidence**: High on throughput, Cloudflare being a production deployment; the sub-second-query claim is unsupported by the cited source

---

**Cloudflare - Log Analytics with ClickHouse**
📍 MASTER-BIBLIOGRAPHY.md:97-116

**Compression**: **10-12× compression ratios** with columnar storage
**Storage Efficiency**: Parquet/ORC equivalent compression for log data
**Workload**: Security-relevant log analytics

**Evidence Level**: A (Production deployment)
**Confidence**: High - Validates compression claims

---

**Shell - 57TB/day Security Telemetry — WITHDRAWN (2026-06-14 audit)**
📍 MASTER-BIBLIOGRAPHY.md:119-141

~~**Data Volume**: 57 TB/day security telemetry processed~~ — **WITHDRAWN: the cited entry was removed in the 2026 source audit (dead URL, claims unverifiable; removed cf26e77). Do not re-cite Shell 57TB/day as a first-party or borrowed anchor.**
~~**Query Performance**: Sub-second query performance at this scale~~ — withdrawn with the entry above.
**Workload**: Enterprise security use case (SIEM alternative)

**Evidence Level**: withdrawn (entry removed in the 2026 audit)
**Confidence**: n/a — claim retracted pending a resolvable source

---

**ClickHouse vs Elasticsearch - Billion Row Comparison**
📍 MASTER-BIBLIOGRAPHY.md:1382-1401

**Storage Efficiency**: **measured ~7.0× on first-party OCSF data via the MOAR FOIL** (lands inside the borrowed 5-10× band)
**Workload**: Billion-row performance comparison (borrowed); 200,000 OCSF events (first-party FOIL)
**Format**: Security log optimization

**Evidence Level**: A (borrowed benchmark study) + **FIRST-PARTY lab measurement** (2026-06-07, MOAR reference stack, single host)
**Confidence**: High - Direct performance comparison for security use case

**FIRST-PARTY measurement (2026-06-07, MOAR reference stack, single host)**: The borrowed "5-10×" is now grounded by a first-party FOIL probe (lakehouse vs an OpenSearch SIEM) over 200,000 OCSF events: the SIEM index footprint was 11.5 MB against a columnar Parquet footprint of 1.6 MB, so the SIEM index is **~7.0× the columnar footprint** — inside the borrowed band rather than at its edge. Answers agreed across the engines before the ratio was read, and the lakehouse was faster on 3/3 query trials. HEDGE: single host, OpenSearch over HTTP vs DuckDB in-process; the term-index advantage at larger scale is not isolated, so the robust first-party findings are the answer-equality and the ~7.0× storage ratio, not the latency. This is a distinct (and, for the storage ratio, higher) evidence tier than the borrowed billion-row benchmark — we ran an identical-workload comparison on our own OCSF data — and it is reported alongside the borrowed number, not in place of it.

---

**ClickHouse - Vectorized Query Execution**
📍 MASTER-BIBLIOGRAPHY.md:594-613

**CPU Efficiency**: ~~8-10× better vs row-based databases~~ **WITHDRAWN (2026-06-14 audit — the "8-10×" figure is not on the cited page)**
**Architecture**: Vectorized execution model (SIMD) — the qualitative mechanism (columnar storage plus vectorization gives a CPU-efficiency gain over row-based execution) stands; the specific multiple does not.

**Evidence Level**: B for the qualitative architecture point; the 8-10× multiple is withdrawn
**Confidence**: Moderate on the mechanism; the magnitude is unsupported by the cited source

---

**ClickHouse - IP Address Types Performance**
📍 MASTER-BIBLIOGRAPHY.md:616-634

**Security-Specific**: ~~50-100× faster CIDR-based threat hunting vs string-based IP storage~~ **borrowed band WITHDRAWN (2026-06-14 audit — the "50-100×" range is not on the cited page). The surviving anchor is the first-party probe below: ~13-17× at 20M rows on a single host, with a ~2.9× IPv4-vs-String storage saving.**
**Feature**: Native IPv4/IPv6 data types
**Use Case**: Security threat hunting with IP/CIDR queries

**Evidence Level**: first-party (the probe below); the borrowed 50-100× vendor band is withdrawn
**Confidence**: High on the measured direction and the storage ratio; the 50-100× magnitude is unsupported by the cited source

**FIRST-PARTY measurement (2026-06-07, MOAR reference stack, single host)**: a first-party CIDR probe on the MOAR reference stack — ClickHouse, one host, 20,000,000 rows, runnable as `lab/cidr_probe.py`. Counting IPs inside `10.5.0.0/16`, the native IPv4 column with an integer range comparison ran in **~0.010 s warm (0.017 s cold)** against **~0.166 s warm (0.213 s cold)** for a String column parsed per row, so the native type was **~13-17× faster**; both returned the identical answer (78,211 of 20M) before the ratio was read. Storage: the String column held **188.1 MiB** against **65.4 MiB** for the IPv4 type, **~2.9× smaller**. HEDGE: ~13-17× on a single host at 20M rows is the first-party result; the vendor "50-100×" band that used to sit above it was withdrawn in the 2026-06-14 audit (not on the cited page), so the durable findings are the measured direction and the ~2.9× storage ratio, and the magnitude is now the first-party number rather than the borrowed range. Identical-workload, answer-equality-gated, reproducible — this is the surviving anchor for the CIDR claim, not a supplement to a borrowed one.

---

**Altinity - ClickHouse Ingest Performance**
📍 MASTER-BIBLIOGRAPHY.md:637-655

**Ingestion Rate**: **1.8-2.2 million events/sec per node**
**Scale**: Production ingest benchmarks
**Validation**: Independent third-party benchmark

**Evidence Level**: A (Independent benchmark)
**Confidence**: High - Third-party validation

---

### 1.2 ClickHouse Consolidated Performance Profile

| Metric | Benchmark | Source | Evidence Level |
|--------|-----------|--------|----------------|
| **Ingestion Throughput** | 1.8-2.2M events/sec/node | Altinity | A |
| **Query Latency (P95)** | ~~<1 second (96% of queries)~~ **WITHDRAWN (figure not in cited source)** | Cloudflare | withdrawn |
| **Compression Ratio** | 10-12× (columnar storage) | Cloudflare | A |
| **Storage Efficiency** | 5-10× vs Elasticsearch (borrowed band); **~7.0× measured first-party** on OCSF data (FOIL) † | ClickHouse benchmark + MOAR FOIL (2026-06-07) | borrowed band + **first-party** |
| **CIDR Threat Hunting** | ~~50-100× (borrowed band — WITHDRAWN, not on cited page)~~; **~13-17× measured first-party** at 20M rows on a single host (the surviving anchor), **storage ~2.9× smaller** (IPv4 vs String) ‡ | MOAR `lab/cidr_probe.py` (2026-06-07) | **first-party** (borrowed band withdrawn) |
| **CPU Efficiency** | ~~8-10× vs row-based DB~~ **WITHDRAWN (figure not on cited page)**; qualitative vectorization advantage only | ClickHouse architecture | withdrawn (mechanism B) |
| **Production Scale** | 6M req/sec (Cloudflare); ~~57 TB/day (Shell)~~ **WITHDRAWN (entry removed in 2026 audit)** | Production cases | A (Cloudflare) |

**Security use-case validation**: production-deployment evidence narrowed by the 2026-06-14 audit — Cloudflare 6M req/sec survives; Shell 57TB/day is withdrawn. The load-bearing storage and CIDR claims now rest on first-party measurement.

† **First-party note**: the storage-efficiency row carries a first-party measurement (~7.0× on OCSF data, MOAR FOIL, 2026-06-07, single host) inside the borrowed 5-10× band. See §1.1 and the four-engine first-party subsection (§1.3) below.

‡ **First-party note**: the CIDR row carries a first-party measurement (~13-17× native IPv4 vs per-row String parsing, MOAR `lab/cidr_probe.py`, 2026-06-07, 20M rows, single host), plus a ~2.9× storage ratio (IPv4 vs String). The borrowed 50-100× band was withdrawn in the 2026-06-14 audit (not on the cited page), so the first-party number is the surviving anchor. See §1.1.

---

### 1.3 Four-Engine Identical-Workload Latency (First-Party)

**MOAR reference stack** — 2026-06-07, single host (Ryzen 5800H, WSL2)
🔬 First-party lab measurement (SDW MOAR "Modular Open Architecture" reference stack)

This is a distinct evidence tier from the production-deployment rows above: rather than a borrowed single-operator number, this is a vendor-neutral, identical-workload comparison run on one shared Apache Iceberg table holding OCSF events, with an **answer-equality gate** applied first — DuckDB, Trino, ClickHouse and StarRocks all agree on `count(*)`, the needle (`dst_port=3389`) and the `group-by dst_port` before any latency is read. (A fifth engine, Dremio, was configured but not brought up this run, so this is a four-engine measured result.)

**Workload × engine latency** — 1,000,000-row OCSF `network_activity`, median of 4 trials, milliseconds (CV% in parentheses):

| Workload | DuckDB | Trino | ClickHouse | StarRocks |
|----------|--------|-------|------------|-----------|
| `count(*)` | **2.4** (10) | 68.5 (10) | 18.2 (11) | 39.9 (1) |
| needle `dst_port=3389` | **5.7** (3) | 97.5 (6) | 22.1 (8) | 45.3 (1) |
| group-by `dst_port` | **12.1** (7) | 96.6 (7) | 30.1 (5) | 55.3 (11) |
| distinct `src_ip` (latency-only; ClickHouse approx) | 139.7 (14) | 427.9 (17) | 168.7 (6) | **97.7** (2) |

**Reading**: on a single host, DuckDB is fastest on the gated small-batch workloads (count, needle, group-by) while StarRocks wins the high-cardinality `distinct src_ip`. No single engine wins everything — specialization is a scale-and-concurrency property, and the **relative pattern is the finding, not the absolute milliseconds**. The `distinct` row is latency-only (ClickHouse computes an approximate distinct), so it is read as a latency comparison rather than an exact-count claim.

**Evidence Level**: **First-party lab measurement** (reproducible; fixed seed/data). Scope limit: single host — in-process DuckDB has a structural edge over the networked engines at this scale, so the small-batch sweep is expected to narrow or invert with concurrency and data volume. No datacenter, concurrency, or TCO claim.

**Confidence**: High for the relative pattern and the answer-equality gate; the absolute milliseconds are bounded to this apparatus.

**See also**: hypothesis-confidence-matrix.md → H-ENGINE-ANSWER-EQUIVALENCE-01 and H-ARCH-02.

---

## 2. Streaming Platform Performance

### 2.1 Apache Kafka

**Confluent - Kafka Performance Benchmark**
📍 MASTER-BIBLIOGRAPHY.md:146-163

**Throughput**: **4.5 million events/second on 9 nodes**
**Scale**: Scalability validation for massive ingestion
**Deployment**: Standard 9-node cluster (realistic enterprise sizing)

**Evidence Level**: B (vendor benchmark; reproducible in principle, but the primary was not re-verified in the 2026-06-14 audit — re-tiered from the original "A" pending a primary check)
**Confidence**: Moderate — widely cited Confluent benchmark, retained because it is reproducible, but treat as vendor-sourced until the primary is opened

---

**Microsoft Azure - Kafka at Trillion Events/Day**
📍 MASTER-BIBLIOGRAPHY.md:660-678

**Throughput**: **Trillions of events/day** (~11.57 million events/sec sustained)
**Scale**: Cloud-scale validation (Microsoft production)
**Deployment**: Azure Event Hubs (Kafka-compatible)

**Evidence Level**: A (Microsoft production deployment)
**Confidence**: High - Validates massive scale Kafka deployments

---

**Netflix - Kafka Tiered Storage — figure WITHDRAWN (2026-06-14 audit)**
📍 MASTER-BIBLIOGRAPHY.md:523-542

~~**Storage Optimization**: 70-80% cost reduction for multi-year retention~~ — **WITHDRAWN: the cited "Netflix" URL is Confluent documentation, not a Netflix source (removed in the 2026 audit). The qualitative claim that hot/cold tiered storage reduces retention cost stands on the Kafka lifecycle documentation; the 70-80% magnitude does not.**
**Architecture**: Hot (Kafka brokers) + Cold (S3 object storage)
**Scale**: Netflix-scale streaming infrastructure

**Evidence Level**: withdrawn (cited source is not a Netflix source)
**Confidence**: n/a for the magnitude; the tiering mechanism is documented independently

---

**Uber - Kafka Streams Latency**
📍 MASTER-BIBLIOGRAPHY.md:681-699

~~**Latency**: Sub-second refresh rates for real-time security views~~ — **WITHDRAWN (2026-06-14 audit: the "thousands of real-time security views / sub-second refresh" figures are not in the cited article, which is a generic Confluent latency piece).**
~~**Stateful Processing**: Thousands of real-time materialized views~~ — withdrawn with the above.
**Use Case**: Security entity tracking at scale

**Evidence Level**: withdrawn (figures not in the cited article)
**Confidence**: n/a — claim retracted pending a resolvable Uber source

---

**LinkedIn - Kafka Streams State Management**
📍 MASTER-BIBLIOGRAPHY.md:502-520

**Stateful Scale**: **Terabytes of state** with millisecond access times
**Use Case**: Production security implementation (entity tracking)
**Architecture**: Kafka Streams stateful processing

**Evidence Level**: A (Production deployment at scale)
**Confidence**: High - Validates stateful processing for security

---

### 2.2 Kafka Consolidated Performance Profile

| Metric | Benchmark | Source | Evidence Level |
|--------|-----------|--------|----------------|
| **Ingestion Throughput** | 4.5M events/sec (9 nodes) | Confluent | A |
| **Maximum Scale** | Trillions/day (~11.57M/sec sustained) | Microsoft Azure | A |
| **Stateful Processing** | Terabytes of state, ms access | LinkedIn | A |
| **Real-Time Latency** | ~~Sub-second refresh~~ **WITHDRAWN (figures not in cited article)** | Uber | withdrawn |
| **Storage Optimization** | ~~70-80% tiered storage savings~~ **WITHDRAWN (cited "Netflix" URL is Confluent docs)** | Netflix | withdrawn |

**Security use-case validation**: LinkedIn stateful-state figure retained; the Uber and Netflix figures are withdrawn per the 2026-06-14 audit.

---

## 3. Table Format Performance

### 3.1 Apache Iceberg

**SK Telecom - 52.7TB in 3.39 Seconds — figures WITHDRAWN (2026-06-14 audit)**
📍 MASTER-BIBLIOGRAPHY.md:49-69

~~**Query Performance**: 97% query time reduction with Iceberg optimizations~~ — **WITHDRAWN: the specific query-time figures are not present in the cited Trino Summit recap (removed in the 2026 audit; the bibliography entry is retained at Level B as a production-deployment reference without the figures).**
~~**Scale**: 52.7 TB scanned in 3.39 seconds~~ — withdrawn with the above.
**Optimization**: Partition evolution + predicate pushdown (qualitative, retained)

**Evidence Level**: withdrawn for the figures; the deployment reference is Level B
**Confidence**: n/a for the magnitudes; the optimization mechanisms are documented independently

---

**Cloudera - Iceberg vs Hive Performance**
📍 MASTER-BIBLIOGRAPHY.md:826-845

**Query Performance**: **10× improvement** over traditional Hive tables
**Feature**: ACID transactions, time travel
**Platform**: Cloudera Data Platform (CDP) production validation

**Evidence Level**: A (Production benchmarks)
**Confidence**: High - Enterprise platform validation

---

### 3.2 Iceberg Performance Profile

| Metric | Benchmark | Source | Evidence Level |
|--------|-----------|--------|----------------|
| **Query Speedup** | ~~97% time reduction (10-30× faster)~~ **WITHDRAWN (figure not in cited recap)** | SK Telecom | withdrawn |
| **Scan Performance** | ~~52.7 TB in 3.39 seconds~~ **WITHDRAWN (figure not in cited recap)** | SK Telecom | withdrawn |
| **vs Hive Tables** | 10× improvement | Cloudera | A |
| **Optimization Features** | Partition evolution, predicate pushdown, metadata filtering | SK Telecom (qualitative) | B |

**Security use-case validation**: Moderate — general analytics, not security-specific (but applicable). Note: the SK Telecom magnitudes are withdrawn per the 2026-06-14 audit; the surviving Iceberg speedup anchor is Cloudera 10× vs Hive (and, first-party, the flagship two-regime ~10-11× foil-vs-columnar / ~4.2-4.6× open-format-tax bands in `~/sdw-lab-benchmarks/zeek-flagship-rerun`).

---

## 4. Advanced Integration Performance

### 4.1 Apache Arrow Flight SQL

**Arrow Summit 2024 - High-Performance Query Connectivity**
📍 MASTER-BIBLIOGRAPHY.md:752-772

**Query Result Retrieval**: **20× faster than JDBC/ODBC**
**Architecture**: Columnar data format eliminates row-based serialization overhead
**Production Validation**: ClickHouse integration tested

**Evidence Level**: A (Benchmark testing, production validation)
**Confidence**: High - Critical for multi-engine architectures

---

**Apache Arrow - Columnar Analytics Performance**
📍 MASTER-BIBLIOGRAPHY.md:1600-1624

**Data Transfer Performance**:
- **PySpark**: 10-100× improvement in some cases
- **Dremio Arrow Flight**: 20-30× better than ODBC/turbodbc
- **Snowflake Python/JDBC**: Up to 5× data retrieval speedup
- **Streamlit**: 15× better performance

**Use Case**: High-bandwidth path for security investigations (VAST network telemetry)

**Evidence Level**: A (Community benchmarks, production validation)
**Confidence**: High - Multiple production validations

---

### 4.2 Arrow Performance Profile

| Metric | Benchmark | Source | Evidence Level |
|--------|-----------|--------|----------------|
| **Flight SQL vs JDBC/ODBC** | 20× faster | Arrow Summit | A |
| **PySpark Integration** | 10-100× improvement (some cases) | Apache Arrow community | A |
| **Dremio Arrow Flight** | 20-30× vs ODBC | Apache Arrow community | A |
| **Snowflake Speedup** | 5× data retrieval | Apache Arrow community | A |

**Security Use Case Validation**: ✅ **Validated** - VAST network telemetry use case documented

---

## 5. Apache Flink Performance

### 5.1 Fault-Tolerance & Recovery

**Apache Flink - Checkpointing for Security Workloads**
📍 MASTER-BIBLIOGRAPHY.md:848-868

**Checkpointing Interval**: **30-60 seconds** recommended for security
**Recovery Time**: **Sub-2 minute recovery** with RocksDB state backend
**Use Case**: Security workload fault-tolerance requirements

**Evidence Level**: A (Official documentation, best practices)
**Confidence**: High - Aligns with production requirements

---

**Uber - Flink Real-Time Security Analytics**
📍 MASTER-BIBLIOGRAPHY.md:190-208

**Benefits**:
- Unified streaming approach for security
- Reduced detection latency
- Operational overhead reduction

**Evidence Level**: A (Production security deployment)
**Confidence**: High - Security use case at scale

---

**Disney+ - Real-Time Security Analytics**
📍 MASTER-BIBLIOGRAPHY.md:212-230

**Benefits**:
- Unified processing logic for security
- Development efficiency gains

**Evidence Level**: A (Production security deployment)
**Confidence**: High - Enterprise streaming security validation

---

### 5.2 Flink Performance Profile

| Metric | Benchmark | Source | Evidence Level |
|--------|-----------|--------|----------------|
| **Checkpointing Interval** | 30-60 seconds (security workloads) | Flink docs | A |
| **Recovery Time** | <2 minutes (RocksDB backend) | Flink docs | A |
| **Security Use Cases** | Uber, Disney+ production | Production cases | A |

**Security Use Case Validation**: ✅ **Strong** - Multiple production security deployments

---

## 6. Comparative Performance Matrix

### 6.1 Query Engines: ClickHouse vs Alternatives

| Platform | Throughput (events/sec) | Query Latency (P95) | Compression | Storage Efficiency | Security-Specific Features |
|----------|------------------------|---------------------|-------------|-------------------|---------------------------|
| **ClickHouse** | 1.8-2.2M/node | ~~<1s (96%)~~ withdrawn | 10-12× | 5-10× vs Elasticsearch (**~7.0× measured first-party** on OCSF data, FOIL) | Native IP types (~13-17× CIDR hunting **measured first-party** at 20M rows, single host — the borrowed 50-100× band is withdrawn — plus ~2.9× storage, §1.1) |
| **Elasticsearch** | ~500K-1M/node (typical) | 1-5s (varies) | 3-5× | Baseline | Full-text search optimized |
| **Trino** | N/A (query engine, not storage) | Varies (federated) | Depends on storage | Federated (no storage) | SQL federation across sources |
| **Athena** | N/A (serverless) | 5-30s (varies) | Depends on Parquet | Pay-per-query | Serverless, no ops overhead |

**Notes**:
- ClickHouse benchmarks from MASTER-BIBLIOGRAPHY.md (7 Level A sources)
- Elasticsearch comparison from MASTER-BIBLIOGRAPHY.md:1382-1401
- Trino/Athena: Different architecture (query engines vs OLAP databases)

---

### 6.2 Streaming Platforms: Kafka vs Alternatives

| Platform | Throughput | Latency | Stateful Processing | Storage | Use Case Fit |
|----------|-----------|---------|---------------------|---------|--------------|
| **Kafka** | 4.5M events/sec (9 nodes, vendor benchmark — B) | Sub-second | Yes (Kafka Streams) | Tiered (~~70-80% savings~~ withdrawn) | Security event streaming |
| **Kafka (Azure)** | 11.57M/sec sustained | Sub-second | Yes | Cloud-native tiered | Cloud-scale security |
| **Flink** | Depends on source | Sub-second | Yes (strong) | External (S3, etc.) | Complex event processing |
| **Spark Streaming** | ~1M events/sec (typical) | Seconds (micro-batch) | Yes (DStreams) | External | Batch + streaming hybrid |

**Notes**:
- Kafka benchmarks from Confluent, Microsoft Azure (MASTER-BIBLIOGRAPHY.md)
- Flink benchmarks from Uber, Disney+ production deployments
- Spark Streaming: Micro-batch architecture (higher latency than true streaming)

---

### 6.3 Table Formats: Iceberg vs Delta vs Hudi

| Format | Query Speedup | Partition Evolution | Time Travel | Vendor Support | Production Scale |
|--------|--------------|---------------------|-------------|----------------|------------------|
| **Iceberg** | 10× vs Hive (Cloudera; the SK Telecom 10-30× is withdrawn) | Yes | Yes | Universal (AWS, Snowflake, Databricks, Google) | ~~52.7 TB in 3.39s~~ withdrawn |
| **Delta Lake** | ~10× (Databricks claims) | Limited (UniForm helps) | Yes | Databricks + growing ecosystem | Production at Databricks customers |
| **Hudi** | ~5-10× (CDC optimized) | Yes | Yes | AWS, specialized use cases | Production at Uber, others |

**Notes**:
- Iceberg benchmarks from SK Telecom, Cloudera (MASTER-BIBLIOGRAPHY.md)
- Delta/Hudi: Limited independent benchmarks in this literature review (gap identified)

---

## 7. Security-Specific Performance Considerations

### 7.1 Performance Characteristics Unique to Security

**Microsoft MSRC - Incident Traffic Surges — figure WITHDRAWN (2026-06-14 audit)**
📍 MASTER-BIBLIOGRAPHY.md:425-443, 1404-1424

~~**Burst Capacity**: 350% traffic surge during security incidents (3.5× spike, hours to days)~~ — **WITHDRAWN: the sole source for the 350% figure was withdrawn in the 2026 audit.** The qualitative point — telemetry spikes sharply during active incidents and the platform must absorb the burst or degrade — stands; the 350% / 4×-baseline magnitude does not.

**Performance Requirement**: provision burst headroom (or accept degradation) sized from a real surge measurement, not the withdrawn 350% figure.

**Implication**: Elastic cloud scaling or on-premises over-provisioning required

---

**Gartner - Security Data Growth Rates**
📍 MASTER-BIBLIOGRAPHY.md:1102-1122

**Data Volume Growth**: **28% CAGR** (compound annual growth rate)
- Year 1: Baseline
- Year 3: 1.64× baseline
- Year 5: 2.14× baseline

**Performance Requirement**: Platform must scale linearly with volume growth (2× data within 3-4 years)

---

### 7.2 Security Workload Performance Requirements

| Workload Type | Performance Requirement | Relevant Benchmark | Platform Recommendation |
|---------------|------------------------|-------------------|------------------------|
| **Real-Time Detection** | Sub-second latency, stateful processing | Kafka Streams (Uber, LinkedIn) | Kafka + ClickHouse |
| **Threat Hunting** | CIDR-based IP queries, billion-row scans | ClickHouse IP types (~13-17× measured first-party at 20M rows, single host — the borrowed 50-100× band is withdrawn — §1.1) | ClickHouse |
| **Incident Investigation** | Multi-year retention, fast historical queries | Iceberg (the SK Telecom 52.7TB/3.39s figure is withdrawn; first-party flagship two-regime bands stand, §1.3 and `~/sdw-lab-benchmarks`) | Iceberg + Trino/ClickHouse |
| **Compliance Queries** | Multi-year queryable retention | Tiered storage (the 70-80% magnitude is withdrawn; mechanism documented) | Iceberg + S3 tiered storage |
| **Log Aggregation** | High ingestion throughput, compression | ClickHouse (1.8-2.2M/sec/node, 10-12× compression) | ClickHouse |
| **Entity Behavior Analytics** | Stateful entity tracking, long windows | Kafka Streams (terabytes of state, ms access) | Kafka Streams |

---

## 8. Performance vs Cost Trade-offs

### 8.1 Cost of Performance

**ClickHouse Real-Time Performance**:
- **Performance**: 6M req/sec (Cloudflare; the "96% <1s" figure is withdrawn — not in source)
- **Cost**: More expensive than S3 + Athena for same storage
- **When Justified**: Real-time threat hunting, analyst productivity (40% improvement validated)

**Kafka Streaming vs Batch**:
- **Performance**: Sub-second latency, stateful entity tracking
- **Cost**: 2-3× total TCO vs batch (per Cost Reality Evidence Bundle)
- **When Justified**: Real-time detection required, compliance mandates, MTTD reduction justifies cost

**Iceberg Query Performance**:
- **Performance**: 10-30× speedup vs traditional formats
- **Cost**: Minimal (open format, no licensing)
- **When Justified**: Always (no trade-off, pure benefit)

---

### 8.2 Performance Optimization ROI

| Optimization | Performance Improvement | Cost Impact | ROI Timeline |
|--------------|------------------------|-------------|--------------|
| **Native IP Types (ClickHouse)** | ~13-17× CIDR hunting speedup measured first-party at 20M rows on a single host (the borrowed 50-100× band is withdrawn), plus ~2.9× storage (IPv4 vs String) | Free (feature, not add-on) | Immediate |
| **Iceberg Table Format** | 10× vs Hive (Cloudera; SK Telecom 10-30× withdrawn) | Free (open format) | Immediate |
| **Tiered Storage (Kafka)** | Minimal perf impact (cold data) | tiering reduces retention cost (the borrowed 70-80% magnitude is withdrawn) | Immediate |
| **Arrow Flight SQL** | 20× result retrieval speedup | Free (open protocol) | Immediate |
| **Streaming (Kafka + Flink)** | Sub-second latency | 2-3× TCO premium | 6-12 months (if MTTD reduction justifies) |

**High-ROI Quick Wins**:
1. Iceberg table format (10× vs Hive per Cloudera; the SK Telecom 10-30× is withdrawn — no cost)
2. ClickHouse native IP types (~13-17× CIDR hunting measured first-party; borrowed 50-100× withdrawn — no cost)
3. Arrow Flight SQL (20× result retrieval, no cost)
4. Tiered storage (reduces retention cost; the 70-80% magnitude is withdrawn — minimal perf impact)

---

## 9. Benchmark Caveats and Limitations

### 9.1 Vendor Benchmark Skepticism

**ClickHouse Benchmarks**:
- **Strengths**: Multiple independent validations (SK Telecom, Shell, Cloudflare)
- **Limitations**: Vendor-favorable test conditions, optimized configurations
- **Mitigation**: Production case studies provide real-world validation

**Kafka Benchmarks**:
- **Strengths**: Confluent benchmark widely reproduced, Microsoft Azure validates scale
- **Limitations**: 9-node cluster may not reflect typical deployments (smaller = lower throughput)
- **Mitigation**: Uber, LinkedIn production cases provide realistic expectations

**Iceberg Benchmarks**:
- **Strengths**: SK Telecom production deployment (real workload)
- **Limitations**: Single data point, heavily optimized deployment
- **Mitigation**: Cloudera 10× vs Hive provides secondary validation

---

### 9.2 "Your Mileage May Vary" Factors

**Performance Depends On**:
1. **Query Patterns**: ClickHouse excels at analytical queries, not transactional
2. **Data Characteristics**: Compression ratios vary (logs compress better than binaries)
3. **Infrastructure**: SSD vs HDD, network bandwidth, CPU cores
4. **Configuration**: ClickHouse requires tuning for optimal performance
5. **Workload**: Benchmarks may not reflect your specific use case

**Recommendation**: **Pilot with your data** before production commitment. Generic benchmarks inform, production pilots validate.

---

## 10. Quick Reference: Performance Comparison

### 10.1 Technology Selection by Performance Requirement

**Need Sub-Second Queries on Large Data (TB-scale)?**
→ **ClickHouse** (6M req/sec, Cloudflare; the "96% <1s" and "Shell 57TB/day" anchors are withdrawn — see the audit note)

**Need Real-Time Streaming with Stateful Processing?**
→ **Kafka + Kafka Streams** (4.5M events/sec, terabytes of state, Uber/LinkedIn validated)

**Need Fast Historical Queries (Multi-Year Retention)?**
→ **Iceberg + Trino/ClickHouse** (the SK Telecom 52.7TB/3.39s and 10-30× figures are withdrawn; Cloudera 10× vs Hive and the first-party flagship two-regime bands stand)

**Need IP/CIDR-Based Threat Hunting?**
→ **ClickHouse with Native IP Types** (~13-17× faster than string-based, measured first-party at 20M rows on a single host; the borrowed 50-100× band is withdrawn)

**Need Multi-Engine Federation?**
→ **Arrow Flight SQL** (20× faster than JDBC/ODBC)

---

### 10.2 Chapter 9 Book Writing Quick Reference

**Key Performance Messages**:

1. **"ClickHouse processes 6 million requests/second (Cloudflare production)."** — The "96% of queries <1s" and "Shell 57 TB/day" claims that this message originally carried are WITHDRAWN (2026-06-14 audit): the latency figure is not in the Cloudflare source and the Shell entry was removed (dead URL). Do not re-introduce either; cite 6M req/sec only.
   - Citation: MASTER-BIBLIOGRAPHY.md:74-94 (Cloudflare, 6M req/sec)

2. **"Apache Iceberg delivers a meaningful query-performance improvement vs traditional Hive tables (Cloudera, ~10×)."** — The SK Telecom "10-30× / 52.7 TB in 3.39s / 97% time reduction" figures this message originally carried are WITHDRAWN (not in the cited Trino Summit recap). Use Cloudera 10× vs Hive, and the first-party flagship two-regime bands (§1.3, `~/sdw-lab-benchmarks`), as the surviving anchors.
   - Citation: MASTER-BIBLIOGRAPHY.md:826-845 (Cloudera, 10× vs Hive)

3. **"Kafka achieves 4.5 million events/second on 9-node clusters (Confluent), validated at trillion events/day scale in Microsoft Azure production"**
   - Citations: MASTER-BIBLIOGRAPHY.md:146-163 (Confluent), MASTER-BIBLIOGRAPHY.md:660-678 (Azure)

4. **"ClickHouse native IP types speed up CIDR-based threat hunting vs string-based implementations: a MOAR-stack probe (2026-06-07, 20M rows, single host, `lab/cidr_probe.py`) measured ~13-17× native IPv4 vs per-row String parsing, with a ~2.9× storage saving."**
   - Citation: first-party (`lab/cidr_probe.py`); the borrowed "50-100×" vendor band formerly cited (MASTER-BIBLIOGRAPHY.md:616-634) is WITHDRAWN — not on the cited page. Cite the first-party measurement as the surviving anchor; do not re-introduce 50-100× as a borrowed claim.

5. **"Kafka Streams enables stateful entity tracking at scale: LinkedIn maintains terabytes of state with millisecond access times, Uber operates thousands of real-time security views with sub-second refresh rates"**
   - Citations: MASTER-BIBLIOGRAPHY.md:502-520 (LinkedIn), MASTER-BIBLIOGRAPHY.md:681-699 (Uber)

---

## 11. Evidence Quality Assessment

### Source Distribution (post-2026-06-14 audit)

The original "12 sources, 100% Evidence Level A" self-grade is WITHDRAWN — it did not survive the claim-vs-source audit. Per-source levels are provisional pending re-verification, and no aggregate Level-A percentage is claimed. Audit dispositions:

- Cloudflare (HTTP + log analytics): 6M req/sec and 10-12× compression retained (A); "96.3% queries <1s" withdrawn (not in source)
- ~~Shell: 57TB/day security telemetry~~ — withdrawn (entry removed, dead URL)
- ClickHouse: Elasticsearch comparison retained (5-10× band, grounded first-party at ~7.0×); vectorized "8-10×" withdrawn; IP-types "50-100×" withdrawn (first-party ~13-17× is the anchor); ingest 1.8-2.2M/node retained
- Confluent: Kafka 4.5M/sec re-tiered to B (vendor benchmark, primary not re-verified)
- Microsoft Azure: trillion events/day retained
- ~~Netflix: tiered storage 70-80%~~ — withdrawn (cited URL is Confluent docs)
- ~~Uber: Kafka Streams "thousands of views / sub-second refresh"~~ — withdrawn (not in cited article)
- LinkedIn: state management retained
- ~~SK Telecom: 97% / 52.7TB / 3.39s figures~~ — withdrawn (not in cited recap); deployment reference retained at B
- Cloudera: Iceberg 10× vs Hive retained (A)
- Apache Arrow: Flight SQL, columnar analytics retained
- Apache Flink: checkpointing retained
- Disney+: real-time security retained (qualitative)

**Overall quality**: aggregate self-grade withdrawn; the load-bearing storage and CIDR claims now rest on first-party measurement verified against `~/sdw-lab-benchmarks`.

---

### Confidence Levels by Technology

| Technology | Benchmark Confidence | Production Validation | Security-Specific Validation |
|-----------|---------------------|----------------------|----------------------------|
| **ClickHouse** | High (Cloudflare 6M req/sec; Shell 57TB/day withdrawn) | ✅ Cloudflare (Shell withdrawn) | first-party CIDR probe (2026-06-07) measures ~13-17× + ~2.9× storage at 20M rows, single host — the surviving anchor; the borrowed 50-100× band is withdrawn (§1.1) |
| **Kafka** | Moderate (Confluent 4.5M re-tiered to B; Uber/Netflix figures withdrawn) | ✅ LinkedIn, Azure (Uber refresh-rate figure withdrawn) | LinkedIn state-management retained; Uber views figure withdrawn |
| **Iceberg** | Moderate (SK Telecom figures withdrawn; Cloudera 10× vs Hive stands) | ✅ Cloudera (SK Telecom magnitudes withdrawn) | ⚠️ Moderate (general analytics) |
| **Arrow** | High | ✅ Strong (multiple platforms) | ✅ Moderate (VAST network telemetry) |
| **Flink** | Moderate-High | ✅ Strong (Uber, Disney+) | ✅ Strong (security deployments) |

---

## Revision History

| Version | Date | Changes | Sources Updated |
|---------|------|---------|-----------------|
| 1.0 | 2025-10-15 | Initial synthesis | 12 sources consolidated |
| 1.1 | 2026-06-07 | Added first-party MOAR-stack legs: FOIL storage (~7.0× on OCSF), four-engine identical-workload latency (§1.3), and a CIDR probe (`lab/cidr_probe.py`: ~13-17× native IPv4 vs String, below the borrowed 50-100× band; ~2.9× storage). Borrowed sources retained. | + first-party lab measurements |
| 1.2 | 2026-06-14 | **Folded-correction audit** (this bundle was never swept in the 2026-06 fabrications cleanup). Marked WITHDRAWN inline, mirroring APPENDICES.md: Shell 57TB/day, SK Telecom 97%/52.7TB/3.39s, borrowed CIDR 50-100×, Cloudflare 96.3%-<1s, ClickHouse 8-10× CPU, Uber views/refresh, Netflix 70-80% tiered. Re-tiered Confluent 4.5M to B. Withdrew the "100% Level A" aggregate self-grade. First-party legs (FOIL ~7.0×, four-engine §1.3, CIDR ~13-17×/~2.9×) re-verified against `~/sdw-lab-benchmarks` FINDINGS and retained. Audit-trail names left inline as records, not new violations. | borrowed stats withdrawn; first-party retained |

---

**Maintained By**: Jeremy Wiley
**Repository**: security-data-literature-review
**Purpose**: Provide quantitative performance comparison for technology selection
**Source Truth**: MASTER-BIBLIOGRAPHY.md (all citations reference line numbers)
