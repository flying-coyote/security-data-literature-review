# Performance Benchmark Comparison Table

**Purpose**: Side-by-side technology performance comparison for quantitative selection decisions
**Target Chapters**: Chapter 9 (Query Engines), Chapter 8 (Storage Formats), Chapter 7 (Streaming)
**Created**: October 15, 2025
**Updated**: June 7, 2026 (added first-party MOAR reference-stack measurements; FOIL substituted into the ClickHouse-vs-Elasticsearch storage cell)
**Sources**: Borrowed-source citations reference MASTER-BIBLIOGRAPHY.md entries; first-party citations reference the SDW MOAR reference stack
**Evidence Quality**: 12 of 12 borrowed sources = Level A (100%), plus first-party lab measurements (distinct evidence tier — identical-workload, answer-equality-gated, reproducible, single host)

---

## Executive Summary

Performance claims are ubiquitous in vendor marketing. This reference consolidates **production-validated benchmarks** from 12 Level A sources to enable **quantitative technology selection**.

**Key Benchmarks**:
- **ClickHouse**: 6M req/sec, 96% queries <1s, 5-10× storage efficiency vs Elasticsearch
- **Kafka**: 4.5M events/sec on 9 nodes, trillions/day at Microsoft scale
- **Iceberg**: 97% query time reduction, 52.7TB scanned in 3.39s
- **Arrow Flight SQL**: 20× faster than JDBC/ODBC for result retrieval

**Critical Insight**: Security workloads have **specific performance characteristics** (burst patterns, CIDR-based hunting, entity tracking) that differ from general analytics. **Generic benchmarks mislead** - prioritize security-specific validation.

---

## 1. Query Engine Performance

### 1.1 ClickHouse - OLAP Analytics

**Cloudflare - 6M Requests/Second HTTP Analytics**
📍 MASTER-BIBLIOGRAPHY.md:74-94

**Throughput**: **6 million requests/second** ingestion and query
**Query Performance**: **96.3% of queries complete under 1 second**
**Scale**: Billions of events processed daily
**Workload**: HTTP analytics (security-relevant log data)

**Evidence Level**: A (Production deployment at massive scale)
**Confidence**: High - Cloudflare = authoritative production validation

---

**Cloudflare - Log Analytics with ClickHouse**
📍 MASTER-BIBLIOGRAPHY.md:97-116

**Compression**: **10-12× compression ratios** with columnar storage
**Storage Efficiency**: Parquet/ORC equivalent compression for log data
**Workload**: Security-relevant log analytics

**Evidence Level**: A (Production deployment)
**Confidence**: High - Validates compression claims

---

**Shell - 57TB/day Security Telemetry**
📍 MASTER-BIBLIOGRAPHY.md:119-141

**Data Volume**: **57 TB/day** security telemetry processed
**Query Performance**: **Sub-second query performance** at this scale
**Workload**: Enterprise security use case (SIEM alternative)

**Evidence Level**: A (Enterprise production deployment)
**Confidence**: High - **CRITICAL SOURCE** for security-specific validation

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

**CPU Efficiency**: **8-10× better** vs row-based databases
**Architecture**: Vectorized execution model (SIMD)
**Rationale**: Columnar storage + vectorization = massive CPU efficiency gains

**Evidence Level**: A (Vendor technical documentation)
**Confidence**: High - Architecture explanation for performance claims

---

**ClickHouse - IP Address Types Performance**
📍 MASTER-BIBLIOGRAPHY.md:616-634

**Security-Specific**: **50-100× faster CIDR-based threat hunting** vs string-based IP storage
**Feature**: Native IPv4/IPv6 data types
**Use Case**: Security threat hunting with IP/CIDR queries

**Evidence Level**: A (Vendor documentation, security-specific)
**Confidence**: High - **CRITICAL** security-specific performance advantage

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
| **Query Latency (P95)** | <1 second (96% of queries) | Cloudflare | A |
| **Compression Ratio** | 10-12× (columnar storage) | Cloudflare | A |
| **Storage Efficiency** | 5-10× vs Elasticsearch (borrowed); **~7.0× measured first-party** on OCSF data (FOIL) † | ClickHouse benchmark + MOAR FOIL (2026-06-07) | A + **first-party** |
| **CIDR Threat Hunting** | 50-100× faster (native IP types) | ClickHouse docs | A |
| **CPU Efficiency** | 8-10× vs row-based DB | ClickHouse architecture | A |
| **Production Scale** | 57 TB/day (Shell), 6M req/sec (Cloudflare) | Production cases | A |

**Security Use Case Validation**: ✅ **Exceptional** - Multiple production security deployments (Shell, Cloudflare)

† **First-party note**: the storage-efficiency row now carries a first-party measurement (~7.0× on OCSF data, MOAR FOIL, 2026-06-07, single host) inside the borrowed 5-10× band. See §1.1 and the four-engine first-party subsection (§1.3) below.

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

**Evidence Level**: A (Vendor benchmark, reproducible)
**Confidence**: High - Widely accepted industry benchmark

---

**Microsoft Azure - Kafka at Trillion Events/Day**
📍 MASTER-BIBLIOGRAPHY.md:660-678

**Throughput**: **Trillions of events/day** (~11.57 million events/sec sustained)
**Scale**: Cloud-scale validation (Microsoft production)
**Deployment**: Azure Event Hubs (Kafka-compatible)

**Evidence Level**: A (Microsoft production deployment)
**Confidence**: High - Validates massive scale Kafka deployments

---

**Netflix - Kafka Tiered Storage**
📍 MASTER-BIBLIOGRAPHY.md:523-542

**Storage Optimization**: 70-80% cost reduction for multi-year retention
**Architecture**: Hot (Kafka brokers) + Cold (S3 object storage)
**Scale**: Netflix-scale streaming infrastructure

**Evidence Level**: A (Production deployment)
**Confidence**: High - Netflix = authoritative streaming source

---

**Uber - Kafka Streams Latency**
📍 MASTER-BIBLIOGRAPHY.md:681-699

**Latency**: **Sub-second refresh rates** for real-time security views
**Stateful Processing**: Thousands of real-time materialized views
**Use Case**: Security entity tracking at scale

**Evidence Level**: A (Production security deployment)
**Confidence**: High - **CRITICAL** security streaming validation

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
| **Real-Time Latency** | Sub-second refresh | Uber | A |
| **Storage Optimization** | 70-80% tiered storage savings | Netflix | A |

**Security Use Case Validation**: ✅ **Strong** - Production security deployments (Uber, LinkedIn)

---

## 3. Table Format Performance

### 3.1 Apache Iceberg

**SK Telecom - 52.7TB in 3.39 Seconds**
📍 MASTER-BIBLIOGRAPHY.md:49-69

**Query Performance**: **97% query time reduction** with Iceberg optimizations
**Scale**: **52.7 TB scanned in 3.39 seconds**
**Optimization**: Partition evolution + predicate pushdown

**Evidence Level**: A (Production deployment, quantitative benchmarks)
**Confidence**: High - Production validation at massive scale

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
| **Query Speedup** | 97% time reduction (10-30× faster) | SK Telecom | A |
| **Scan Performance** | 52.7 TB in 3.39 seconds | SK Telecom | A |
| **vs Hive Tables** | 10× improvement | Cloudera | A |
| **Optimization Features** | Partition evolution, predicate pushdown, metadata filtering | SK Telecom | A |

**Security Use Case Validation**: ⚠️ **Moderate** - General analytics, not security-specific (but applicable)

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
| **ClickHouse** | 1.8-2.2M/node | <1s (96%) | 10-12× | 5-10× vs Elasticsearch (**~7.0× measured first-party** on OCSF data, FOIL) | Native IP types (50-100× CIDR hunting) |
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
| **Kafka** | 4.5M events/sec (9 nodes) | Sub-second | Yes (Kafka Streams) | Tiered (70-80% savings) | Security event streaming |
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
| **Iceberg** | 10-30× (SK Telecom) | Yes | Yes | Universal (AWS, Snowflake, Databricks, Google) | 52.7 TB in 3.39s |
| **Delta Lake** | ~10× (Databricks claims) | Limited (UniForm helps) | Yes | Databricks + growing ecosystem | Production at Databricks customers |
| **Hudi** | ~5-10× (CDC optimized) | Yes | Yes | AWS, specialized use cases | Production at Uber, others |

**Notes**:
- Iceberg benchmarks from SK Telecom, Cloudera (MASTER-BIBLIOGRAPHY.md)
- Delta/Hudi: Limited independent benchmarks in this literature review (gap identified)

---

## 7. Security-Specific Performance Considerations

### 7.1 Performance Characteristics Unique to Security

**Microsoft MSRC - Incident Traffic Surges**
📍 MASTER-BIBLIOGRAPHY.md:425-443, 1404-1424

**Burst Capacity**: **350% traffic surge** during security incidents
- Normal operations: Baseline throughput
- Active incident response: 3.5× data volume spike
- Duration: Hours to days

**Performance Requirement**: Platform must handle **4× baseline capacity** or accept degraded performance during critical incidents

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
| **Threat Hunting** | CIDR-based IP queries, billion-row scans | ClickHouse IP types (50-100× speedup) | ClickHouse |
| **Incident Investigation** | Multi-year retention, fast historical queries | Iceberg (52.7 TB in 3.39s) | Iceberg + Trino/ClickHouse |
| **Compliance Queries** | Multi-year queryable retention | Tiered storage (70-80% cost savings) | Iceberg + S3 tiered storage |
| **Log Aggregation** | High ingestion throughput, compression | ClickHouse (1.8-2.2M/sec/node, 10-12× compression) | ClickHouse |
| **Entity Behavior Analytics** | Stateful entity tracking, long windows | Kafka Streams (terabytes of state, ms access) | Kafka Streams |

---

## 8. Performance vs Cost Trade-offs

### 8.1 Cost of Performance

**ClickHouse Real-Time Performance**:
- **Performance**: 6M req/sec, 96% <1s queries
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
| **Native IP Types (ClickHouse)** | 50-100× CIDR hunting speedup | Free (feature, not add-on) | Immediate |
| **Iceberg Table Format** | 10-30× query speedup | Free (open format) | Immediate |
| **Tiered Storage (Kafka)** | Minimal perf impact (cold data) | 70-80% storage savings | Immediate |
| **Arrow Flight SQL** | 20× result retrieval speedup | Free (open protocol) | Immediate |
| **Streaming (Kafka + Flink)** | Sub-second latency | 2-3× TCO premium | 6-12 months (if MTTD reduction justifies) |

**High-ROI Quick Wins**:
1. Iceberg table format (10-30× query speedup, no cost)
2. ClickHouse native IP types (50-100× CIDR hunting, no cost)
3. Arrow Flight SQL (20× result retrieval, no cost)
4. Tiered storage (70-80% savings, minimal perf impact)

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
→ **ClickHouse** (6M req/sec, 96% <1s, validated at Shell 57TB/day)

**Need Real-Time Streaming with Stateful Processing?**
→ **Kafka + Kafka Streams** (4.5M events/sec, terabytes of state, Uber/LinkedIn validated)

**Need Fast Historical Queries (Multi-Year Retention)?**
→ **Iceberg + Trino/ClickHouse** (52.7 TB in 3.39s, 10-30× speedup)

**Need IP/CIDR-Based Threat Hunting?**
→ **ClickHouse with Native IP Types** (50-100× faster than string-based)

**Need Multi-Engine Federation?**
→ **Arrow Flight SQL** (20× faster than JDBC/ODBC)

---

### 10.2 Chapter 9 Book Writing Quick Reference

**Key Performance Messages**:

1. **"ClickHouse processes 6 million requests/second with 96% of queries completing under 1 second (Cloudflare production), validated at enterprise security scale processing 57 TB/day (Shell)"**
   - Citations: MASTER-BIBLIOGRAPHY.md:74-94 (Cloudflare), MASTER-BIBLIOGRAPHY.md:119-141 (Shell)

2. **"Apache Iceberg delivers 10-30× query performance improvement vs traditional formats, with SK Telecom scanning 52.7 TB in 3.39 seconds (97% time reduction)"**
   - Citation: MASTER-BIBLIOGRAPHY.md:49-69

3. **"Kafka achieves 4.5 million events/second on 9-node clusters (Confluent), validated at trillion events/day scale in Microsoft Azure production"**
   - Citations: MASTER-BIBLIOGRAPHY.md:146-163 (Confluent), MASTER-BIBLIOGRAPHY.md:660-678 (Azure)

4. **"ClickHouse native IP types provide 50-100× performance improvement for CIDR-based threat hunting vs string-based implementations"**
   - Citation: MASTER-BIBLIOGRAPHY.md:616-634 (security-specific optimization)

5. **"Kafka Streams enables stateful entity tracking at scale: LinkedIn maintains terabytes of state with millisecond access times, Uber operates thousands of real-time security views with sub-second refresh rates"**
   - Citations: MASTER-BIBLIOGRAPHY.md:502-520 (LinkedIn), MASTER-BIBLIOGRAPHY.md:681-699 (Uber)

---

## 11. Evidence Quality Assessment

### Source Distribution

**Evidence Level A (12 sources, 100%)**:
- Cloudflare (2 sources): HTTP analytics, log analytics
- Shell: 57TB/day security telemetry
- ClickHouse: Elasticsearch comparison, vectorized execution, IP types, ingest performance
- Confluent: Kafka benchmark
- Microsoft Azure: Trillion events/day
- Netflix: Tiered storage
- Uber: Kafka Streams latency
- LinkedIn: State management
- SK Telecom: Iceberg performance
- Cloudera: Iceberg vs Hive
- Apache Arrow: Flight SQL, columnar analytics
- Apache Flink: Checkpointing
- Disney+: Real-time security

**Overall Quality**: **100% Evidence Level A** - Exceptional

---

### Confidence Levels by Technology

| Technology | Benchmark Confidence | Production Validation | Security-Specific Validation |
|-----------|---------------------|----------------------|----------------------------|
| **ClickHouse** | High | ✅ Strong (Shell, Cloudflare) | ✅ Strong (IP types, 57TB/day) |
| **Kafka** | High | ✅ Strong (Uber, LinkedIn, Azure) | ✅ Strong (Uber, LinkedIn security) |
| **Iceberg** | High | ✅ Strong (SK Telecom, Cloudera) | ⚠️ Moderate (general analytics) |
| **Arrow** | High | ✅ Strong (multiple platforms) | ✅ Moderate (VAST network telemetry) |
| **Flink** | Moderate-High | ✅ Strong (Uber, Disney+) | ✅ Strong (security deployments) |

---

## Revision History

| Version | Date | Changes | Sources Updated |
|---------|------|---------|-----------------|
| 1.0 | 2025-10-15 | Initial synthesis | 12 sources consolidated |

---

**Maintained By**: Jeremy Wiley
**Repository**: security-data-literature-review
**Purpose**: Provide quantitative performance comparison for technology selection
**Source Truth**: MASTER-BIBLIOGRAPHY.md (all citations reference line numbers)
