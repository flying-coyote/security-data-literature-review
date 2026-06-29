---
type: reference
title: "Appendix G: Security Data Stack Vendor Landscape"
created: 2026-01-09
tags: [vendor-landscape, siem, query-engine, iceberg, security-data, cost-comparison]
---

# Appendix G: Vendor Landscape

**Purpose**: A reference of vendors across the modern security data stack. Each entry carries a category, a short description, deployment options, a cost profile, and an evidence-quality rating.

**How to use**: Reference this appendix when evaluating vendors for your architecture. Use the Decision Worksheets (Appendix A) to score vendors against your requirements. The evidence ratings (A-D) tell you how well each vendor's claims are validated, so for production work I'd start from the Tier A/B entries and treat C/D as needing your own due diligence first.

**Data Source**: This appendix is synchronized with the [Security Architect MCP Server](https://github.com/flying-coyote/security-architect-mcp-server) vendor database, ensuring consistency between book content and tooling.

**Last Updated**: February 28, 2026
**Pricing Currency**: All cost ranges are in USD, based on publicly available pricing and practitioner-reported costs as of Q4 2025. Volume baselines are specified per vendor (e.g., "for 5TB/day"). Actual costs vary by contract terms, volume commitments, and negotiation.

**Sourcing note (read this first)**: This is a vendor *landscape*, so most rows describe what each vendor says it does. Treat the capability and performance language in the Description column as vendor-stated (Tier C) unless an entry carries an explicit independent source. Pricing figures fall into two buckets: rows tagged **G-Cloud 14** are anchored to the UK Government Digital Marketplace G-Cloud 14 pricelist (2024, the same source used in Appendix A.6), and everything else is vendor-published list pricing or practitioner-reported and should be read as Tier C — a starting point for your own due diligence, not an independently verified quote. The per-row Evidence rating (A-D, defined at the foot of this appendix) is the formal version of this same caution.

---

## Quick Navigation

- [SIEM](#siem) (23 vendors)
- [Detection & Response](#detection--response) (3 vendors)
- [Query Engine](#query-engine) (11 vendors)
- [Streaming Platform](#streaming-platform) (10 vendors)
- [Data Lakehouse](#data-lakehouse) (8 vendors)
- [Data Catalog & Governance](#data-catalog-and-governance) (8 vendors)
- [ETL/ELT Platform](#etlelt-platform) (10 vendors)
- [Observability Platform](#observability-platform) (7 vendors)
- [Object Storage](#object-storage) (5 vendors)
- [Data Virtualization](#data-virtualization) (4 vendors)
- [Other](#other) (1 vendor)

---

## SIEM

| Vendor | Description | Deployment | Cost Range | Evidence |
|--------|-------------|------------|------------|----------|
| [Anvilogic](https://www.anvilogic.com) | AI-powered multi-data-platform SIEM enabling detection-as-code across Snowflake, Databricks, Splunk, and Sentinel without moving data; decouples detection from log storage | cloud, on-prem, hybrid | $80K-575K/yr by employee tier (2k-100k employees); +$3K/seat/yr (per-employee, not per-volume) | B |
| [Chronicle Security (Google SecOps)](https://chronicle.security) | Cloud-native SIEM on Google infrastructure; petabyte-scale threat detection with Mandiant-enriched threat intelligence. | cloud | £2,000/TB/yr volumetric (G-Cloud 14, 12-mo hot retention); or ~$60-95/employee/yr headcount (Enterprise tier) | A |
| [CrowdStrike Falcon LogScale](https://www.crowdstrike.com/platform/next-gen-siem/falcon-logscale) | Index-free streaming log management (formerly Humio); C++ query engine and decoupled storage for real-time threat hunting. | cloud, on-prem, hybrid | Next-Gen SIEM £200/daily-GB/yr ingest + £615 retention; standalone LogScale Cloud £1,370/daily-GB/yr (G-Cloud 14, 2024); AWS PAYG since late 2025 | A |
| [Devo Platform](https://www.devo.com) | Cloud-native security data platform (SIEM, SOAR, UEBA); vendor-stated high-throughput indexing with 400-day hot retention for large enterprises. | cloud, on-prem, hybrid | $90K/yr for 100GB/day to $675K/yr for 1TB/day (400-day retention), practitioner-reported | A |
| [Elastic Security (SIEM)](https://www.elastic.co/security) | Security analytics built on Elastic Stack. | cloud, on-prem | $1M-5M for 5TB/day (practitioner-reported range) | A |
| [Exabeam Fusion SIEM](https://www.exabeam.com) | SIEM + UEBA on the New-Scale platform (2024 Exabeam-LogRhythm merger); behavioral analytics and vendor-stated unlimited storage, with self-hosted LogRhythm retained for on-prem compliance | cloud, on-prem, hybrid | $200K-1.5M for 500GB/day (practitioner-reported range) | A |
| [Grafana Loki](https://grafana.com/oss/loki) | Open-source index-free log aggregation optimized for Prometheus; compresses metadata and scales horizontally, a low-cost SIEM alternative. | cloud, on-prem, hybrid | OSS free (AGPLv3); Grafana Cloud $0.30-0.40/GB ingested after 100GB/mo free | A |
| [Graylog](https://www.graylog.org) | Open-source log management and SIEM; guided ingestion and schema mapping for mid-market compliance, low TCO, rapid deployment. | cloud, on-prem, hybrid | OSS free (SSPL); Enterprise from $15K/yr by volume | A |
| [Gurucul Next-Gen SIEM](https://gurucul.com) | Analytics-driven SIEM combining UEBA, identity profiling, and automated response across clouds; Open XDR architecture. | cloud, on-prem, hybrid | contact-sales (no public list; via Optiv/SHI GSA, custom private offers) | B |
| [IBM QRadar SIEM](https://www.ibm.com/qradar) | Enterprise SIEM with a long install base in regulated industries; IBM sold the QRadar SaaS assets to Palo Alto Networks (2024) and cloud QRadar reaches end-of-life 14 Apr 2026 (on-prem continues; Cortex XSIAM is the migration path) | cloud, on-prem, hybrid | $1M-5M for 5TB/day (practitioner-reported range) | A |
| [Microsoft Sentinel](https://azure.microsoft.com/en-us/products/microsoft-sentinel) | Cloud-native SIEM (formerly Azure Sentinel); SOAR-style automated response and Microsoft 365/Azure integration. | cloud | $144K-420K for 500GB/day (derived from Azure published per-GB tiers; varies by commitment) | A |
| [Palo Alto Networks Cortex XSIAM](https://www.paloaltonetworks.com/cortex/xsiam) | AI-driven platform unifying SIEM, SOAR, and endpoint security natively; the QRadar SaaS migration path. | cloud | $70/endpoint/yr or $100/employee/yr (3 endpoints/user); non-endpoint ingest $360/daily-GB/yr hot (G-Cloud 14, 2024) | A |
| [Panther](https://panther.com) | Cloud-native, serverless SIEM pairing Snowflake storage with Python detection-as-code; vendor-stated petabyte-scale security telemetry. | cloud | $8.1K-80K/yr base platform (practitioner-reported), plus separate cloud warehouse compute | B |
| [Query.ai](https://www.query.ai) | Federated search platform translating queries across 150+ distributed, un-ingested security sources without replicating data. | cloud | contact-sales (flat fee per integrated connector, unlimited search; community-reported) | C |
| [Rapid7 InsightIDR](https://www.rapid7.com/products/insightidr) | SaaS SIEM combining cloud log management, UEBA, and native deception technology; asset-based pricing, rapid deployment. | cloud | from $2,156/mo, 500-asset minimum, billed annually | A |
| [Securonix Unified Defense SIEM](https://www.securonix.com) | AI-driven SIEM on decoupled storage with native UEBA and SOAR; unified threat detection and response. | cloud, on-prem, hybrid | $67K-100K/yr per 1,000 monitored identities (Basic→UDS Advanced); MSSP $150K (AWS Marketplace; identity-based, not volume) | A |
| [SentinelOne Singularity AI SIEM](https://www.sentinelone.com/platform/singularity-ai-siem) | Cloud-native SIEM on the Singularity Data Lake; vendor-stated OCSF normalization, AI threat hunting, automated response. | cloud | $179.99-229.99/device/yr vendor-published list (Complete/Commercial); cloud security separate | A |
| [Splunk Enterprise Security](https://www.splunk.com) | Schema-on-read SIEM (Cisco subsidiary since the 2024 $28B acquisition) with one of the market's largest detection-content libraries; ingest-volume licensing drives the high cost at scale. | cloud, on-prem | G-Cloud 14 = $1,196/GB/day/yr; at 5TB/day this implies ~$6M list (~$3-6M discounted, practitioner-reported) for platform+ES | A |
| [Stellar Cyber Open XDR](https://stellarcyber.ai) | Open XDR platform unifying NG-SIEM, NDR, UEBA, SOAR, and TIP; orchestrates alerts across multi-vendor environments with ML. | cloud, on-prem, hybrid | contact-sales (unified "one-price" platform license; via Carahsoft/Oracle Gov Cloud) | B |
| [Sumo Logic Cloud SIEM](https://www.sumologic.com/solutions/cloud-siem) | Cloud-native SIEM with ML-assisted detection and MITRE ATT&CK mapping. | cloud | $200K-1M for 5TB/day (practitioner-reported range) | A |
| [Sysdig Secure](https://sysdig.com/products/secure) | Kubernetes-native CNAPP on the Falco engine; eBPF runtime container threat detection and cloud security posture. | cloud, on-prem, hybrid | $72/unit/mo CNAPP Enterprise (20-unit min), plus event overages | D |
| [Torq AI SOC Platform](https://torq.io) | AI-native security hyperautomation (formerly HyperSOC); agentic multi-agent system (HyperAgents/Socrates) that triages, investigates, and remediates SOC alerts across 300+ integrations | cloud, hybrid | $60K-378K/yr (Vendr median ~$179K), contact-sales | B |
| [Wazuh](https://wazuh.com) | Free open-source XDR and SIEM on Elastic Stack; file-integrity monitoring, vulnerability detection, MITRE ATT&CK, active response. | cloud, on-prem, hybrid | OSS free (GPLv2); Wazuh Cloud from $571/mo for 100 agents; support $16,234/yr | A |

## Detection & Response

| Vendor | Description | Deployment | Cost Range | Evidence |
|--------|-------------|------------|------------|----------|
| [FunnyWolf agentic-soc-platform](https://github.com/FunnyWolf/agentic-soc-platform) | Open-source on-prem agentic SOC platform; alert aggregation over a unified ELK/Splunk search abstraction, MCP-integrated. Noise-reduction claims vendor-stated and unmeasured. | on-prem | OSS free (MIT); self-hosted infra/maintenance only | C |
| [LimaCharlie](https://limacharlie.io) | SecOps Cloud Platform — API-first, infrastructure-as-code security building blocks (EDR, telemetry, detection/response, multi-tenant) with agentic AI operators, MSSP-focused | cloud, hybrid | $3/endpoint/mo + $0.20/GB ingested/stored, pay-as-you-go | B |
| [Tracecat](https://github.com/TracecatHQ/tracecat) | Open-source security-automation/SOAR platform for teams and AI agents; case management, Git-synced Python actions, nsjail-sandboxed execution orchestrated on Temporal. | cloud, on-prem, hybrid | OSS free (AGPL-3.0; enterprise add-ons) | B |
| [Velociraptor](https://www.velocidex.com/) | Open-source endpoint visibility and DFIR platform; VQL-driven threat hunting, triage, and raw endpoint-state collection at scale. | on-prem, hybrid, cloud | OSS free (AGPLv3); self-hosted infra/maintenance only | A |
| [Vigil (DeepTempo)](https://github.com/Vigil-SOC/vigil) | Open-source AI-SOC platform; MCP-based agent orchestration with confidence-gated auto-approval, marketed as own-not-rent. Self-hostable; capability claims vendor-stated and unmeasured. | cloud, on-prem, hybrid | OSS free (Apache 2.0); self-hosted infra/maintenance only | C |
| [Wazuh (agentic AI)](https://wazuh.com) | Open-source XDR/SIEM with an agentic-AI integration; a local model (e.g. Qwen3 via Ollama) reads telemetry read-only and drafts/tests decoders. Air-gappable. | cloud, on-prem, hybrid | OSS free (GPLv2); self-hosted infra/maintenance only | B |
| [Zeek](https://zeek.org/) | Open-source network security monitoring and IDS framework; turns packet streams into 50+ structured transaction log types. | on-prem, cloud, hybrid | OSS free (BSD 3-Clause); Corelight commercial support contact-sales | A |

## Query Engine

| Vendor | Description | Deployment | Cost Range | Evidence |
|--------|-------------|------------|------------|----------|
| [Amazon Athena](https://aws.amazon.com/athena) | Serverless interactive SQL query engine over S3 data lakes; pay-per-TB-scanned, optimized for partitioned columnar formats. | cloud | $5.00/TB scanned (on-demand), 10MB/query min; Capacity $0.30/DPU-hour | A |
| [Apache Drill](https://drill.apache.org) | Open-source schema-free distributed SQL query engine; explores large structured and unstructured datasets in place across stores. | cloud, on-prem, hybrid | OSS free (Apache 2.0); self-managed hosting/support only | A |
| [Apache Impala](https://impala.apache.org) | Open-source MPP SQL query engine for low-latency ad-hoc analysis on HDFS or object storage. | cloud, on-prem, hybrid | OSS free (Apache 2.0); self-managed hosting/support only | A |
| [Apache Pinot](https://pinot.apache.org) | Open-source real-time distributed OLAP datastore; sub-second, high-concurrency analytics on high-throughput security log streams. | cloud, on-prem, hybrid | OSS free (Apache 2.0); self-managed hosting/support only | A |
| [ClickHouse](https://clickhouse.com) | Open-source columnar OLAP database for high-performance real-time analytics on compressed security logs. | cloud, on-prem, hybrid | OSS free (Apache 2.0); Cloud Basic from $66.52/mo, Scale from $499.38/mo | A |
| [Google BigQuery](https://cloud.google.com/bigquery) | Serverless enterprise data warehouse with built-in ML capabilities. | cloud | $100K-500K for 5TB/day (modeled from GCP published on-demand/capacity rates; varies by query pattern) | A |
| [Hydrolix](https://hydrolix.io) | Cloud-native columnar log database with decoupled architecture; vendor-stated high-density storage and real-time S3 query performance. | cloud, on-prem, hybrid | from $0.20/GB (ingest+storage+query), vendor-published; managed AWS ~$12,160/mo for 2TB/day (community-reported estimate) | C |
| [PrestoDB](https://prestodb.io) | Open-source distributed SQL query engine (Meta origin); fast federated analytic queries over heterogeneous, un-ingested data. | cloud, on-prem, hybrid | OSS free (Apache 2.0); self-managed hosting/support only | A |
| [StarRocks](https://www.starrocks.io) | Open-source MPP vectorized database for sub-second real-time analytics and high-volume structured log analysis. | cloud, on-prem, hybrid | OSS free (Apache 2.0); self-managed hosting/support only | A |
| [Trino](https://trino.io) | Open-source distributed SQL query engine for fast ad-hoc federated analytics across heterogeneous, decoupled data lakes. | cloud, on-prem, hybrid | OSS free (Apache 2.0); self-managed hosting/support only | A |

## Streaming Platform

| Vendor | Description | Deployment | Cost Range | Evidence |
|--------|-------------|------------|------------|----------|
| [Amazon Kinesis Data Streams](https://aws.amazon.com/kinesis) | Serverless AWS streaming service for real-time ingestion and buffering of high-velocity security event logs. | cloud | On-Demand $0.08/GB written, $0.04/GB read, $0.04/stream-hour | A |
| [Apache Flink](https://flink.apache.org) | Open-source stateful stream processing with exactly-once semantics; low-latency computation over bounded and unbounded log streams. | cloud, on-prem, hybrid | OSS free (Apache 2.0); self-managed infra/routing only | A |
| [Apache Kafka](https://kafka.apache.org) | Open-source distributed event streaming platform; the industry standard for high-throughput log ingestion pipelines. | cloud, on-prem, hybrid | OSS free (Apache 2.0); self-managed infra/routing only | A |
| [Apache Pulsar](https://pulsar.apache.org) | Open-source distributed messaging and streaming with decoupled storage, multi-tenancy, geo-replication, and tiered storage. | cloud, on-prem, hybrid | OSS free (Apache 2.0); self-managed infra/routing only | A |
| [Apache Storm](https://storm.apache.org) | Open-source distributed real-time computation system; fault-tolerant, guaranteed processing of unbounded security data streams. | cloud, on-prem, hybrid | OSS free (Apache 2.0); self-managed infra/routing only | A |
| [Azure Event Hubs](https://azure.microsoft.com/services/event-hubs) | Managed event streaming service with Kafka-compatible APIs; autoscaling, billed by throughput or capacity units. | cloud | Standard $0.03/TU/hr + $0.028/M ingress events; Dedicated from $4K/mo | A |
| [Confluent Platform](https://www.confluent.io) | Enterprise Kafka distribution with managed cloud; serverless autoscaling, managed connectors, Schema Registry, stream governance. | cloud, on-prem, hybrid | Standard Cloud ~$1K-3K/mo; Dedicated from $10K/mo; storage $0.08/GB-mo | A |
| [Google Cloud Pub/Sub](https://cloud.google.com/pubsub) | Serverless GCP messaging service; global scale, at-least-once delivery, message replication, native Dataflow integration. | cloud | $40/TB ($0.04/GB) ingestion after 10GB/mo free | A |
| [RabbitMQ](https://www.rabbitmq.com) | Open-source multi-protocol message broker; AMQP, flexible routing, clustering, easy deployment across hybrid networks. | cloud, on-prem, hybrid | OSS free (MPL); self-managed infra/routing only | A |
| [Redpanda](https://redpanda.com) | Kafka-compatible streaming platform; C++ rewrite with no JVM or Zookeeper for high throughput and low overhead. | cloud, on-prem, hybrid | Serverless $0.045/GB written, $0.04/GB read, $0.09/GB-mo retention | B |

## Data Lakehouse

| Vendor | Description | Deployment | Cost Range | Evidence |
|--------|-------------|------------|------------|----------|
| [Apache Druid](https://druid.apache.org) | Open-source distributed column-oriented real-time analytics database; rapid ingestion and sub-second slice-and-dice queries. | cloud, on-prem | OSS free (Apache 2.0); self-managed infra/compute only | A |
| [Apache Hudi](https://hudi.apache.org) | Open-source transactional data lake table format (Uber origin); incremental processing and record-level updates. | cloud, on-prem, hybrid | OSS free (Apache 2.0); self-managed infra/compute only | A |
| [Apache Iceberg](https://iceberg.apache.org) | Open-source high-performance table format for analytical datasets; ACID transactions and metadata-driven schema evolution. | cloud, on-prem, hybrid | OSS free (Apache 2.0); self-managed infra/compute only | A |
| [Apache Paimon](https://paimon.apache.org) | Apache streaming lakehouse table format with LSM-tree storage; high-throughput ingestion and real-time analytics. | cloud, on-prem, hybrid | OSS free (Apache 2.0); self-managed infra/compute only | A |
| [Databricks Lakebase](https://databricks.com/lakebase) | Transactional serverless Postgres inside the Databricks lakehouse; serves ML features and real-time application state. Foundation of the LTAP architecture announced June 2026 (one governed copy for OLTP+OLAP, no ETL; LTAP itself coming-soon, not GA). | cloud | $0.092/Capacity-Unit-hour (50% promo to 2027-01-31); storage $0.345/GB-mo | D |
| [Databricks Lakehouse Platform](https://www.databricks.com) | Unified analytics platform on Apache Spark with Delta Lake and Unity Catalog; open formats, governed serverless compute. | cloud | $0.07 (Standard) to $0.40 per DBU by workload/tier | A |
| [Delta Lake](https://delta.io) | Open-source storage framework adding ACID transactions and metadata management over existing object storage (Databricks origin). | cloud, on-prem, hybrid | OSS free (Apache 2.0); self-managed infra/compute only | A |
| [Snowflake Data Cloud](https://www.snowflake.com) | Cloud-native data warehouse with lakehouse capabilities; decoupled compute and storage, multi-cloud, credit-based billing. | cloud | $2-4/credit (Standard/Enterprise/Business Critical); storage $23/TB-mo on AWS | A |

## Data Catalog & Governance

| Vendor | Description | Deployment | Cost Range | Evidence |
|--------|-------------|------------|------------|----------|
| [AWS Glue Data Catalog](https://aws.amazon.com/glue) | Serverless AWS metadata catalog; schema discovery, partition management, lineage; first million objects free, Lake Formation. | cloud | first 1M objects free; then $1.00 per 100K objects/mo | D |
| [Alation Data Intelligence Platform](https://www.alation.com) | Enterprise data catalog with 120+ connectors; automated curation, business glossaries, and behavioral usage analytics. | cloud, on-prem, hybrid | from ~$60K/yr; practitioner-reported deployments from $198K/yr for 25 Creator users | A |
| [Apache Atlas](https://atlas.apache.org) | Open-source metadata management for Hadoop and beyond; data lineage, classification, and business glossary. | cloud, on-prem, hybrid | OSS free (Apache 2.0); self-hosted infra/maintenance only | A |
| [Atlan](https://atlan.com) | Active-metadata platform for data and AI governance; automated cataloging and end-to-end lineage, named a Leader in Gartner's 2025 catalog Magic Quadrant. | cloud, hybrid | contact-sales; estimated $40K-120K+/yr by user seats (no public list; estimate, Tier C) | A |
| [Collibra Data Intelligence](https://www.collibra.com) | Data catalog plus governance, quality, and AI-governance modules; placed in the Leaders quadrant of Gartner's 2025 governance Magic Quadrant. | cloud, on-prem, hybrid | $170K-510K for 10K tables (vendor-quoted, no public list; D-tier) | D |
| [DataHub](https://datahubproject.io) | Open-source, API-first metadata platform (LinkedIn origin); search, discovery, observability, and column-level lineage. | cloud, on-prem, hybrid | OSS free (Apache 2.0); self-managed infra/maintenance only | B |
| [Microsoft Purview Data Governance](https://azure.microsoft.com/services/purview) | Unified data governance; Jan 2025 pay-as-you-go model charges per governed asset with free background Data Map scanning | cloud | $0.50/governed asset/month (Jan 2025 PAYG); ~$6K/yr per 1,000 assets | A |
| [Select Star](https://www.selectstar.com) | Modern data governance platform; automated column-level lineage and business glossary indexing. | cloud | Growth $9,720/yr (20 users, 1K tables); Enterprise $73,765/yr (100 users, 5K tables) — vendor-published list | B |

## ETL/ELT Platform

| Vendor | Description | Deployment | Cost Range | Evidence |
|--------|-------------|------------|------------|----------|
| [Airbyte](https://airbyte.com) | Open-source ELT platform with 600+ connectors; capacity- or credit-based pricing with a free self-hosted tier. | cloud, on-prem, hybrid | OSS free; Cloud Standard $10/mo + $2.50/credit; Cloud Plus from $25K/yr | A |
| [Apache NiFi](https://nifi.apache.org) | Open-source real-time dataflow automation with drag-and-drop UI; low-code routing and integration with provenance tracking. | cloud, on-prem, hybrid | OSS free (Apache 2.0); self-managed hosting/support only | A |
| [Cribl Stream](https://cribl.io/stream) | Telemetry pipeline routing, filtering, and transforming security and observability data in-flight before downstream ingestion. | cloud, on-prem, hybrid, edge | $0.32/GB Enterprise Cloud ($0.26/GB hybrid workers); first 1TB/day free | B |
| [DataBee](https://www.databee.ai) | Security data fabric (from Comcast) normalizing and enriching raw log telemetry into Apache Iceberg tables; OCSF output. | cloud | contact-sales (custom private offers via AWS Marketplace / Carahsoft) | C |
| [Databahn.ai](https://www.databahn.ai) | AI-powered security-native data pipeline; vendor-stated collection from 500+ sources with volume compression and automated routing. | cloud, hybrid | $0.01/GB ingested+committed (12-mo contract); overage $0.08/GB — vendor-published, Tier C | C |
| [Estuary](https://estuary.dev) | Real-time data pipeline with CDC and streaming; sub-second schema evolution, automated replication, millisecond routing. | cloud | free to 10GB/mo; $0.50/GB moved + $0.14/hr per paid connector | D |
| [Fivetran](https://www.fivetran.com) | Automated ELT with 700+ connectors; Monthly Active Row billing moved per-connector in 2024 (vendor change widely reported to raise multi-connector cost, commonly cited ~40-70%) | cloud | $25K-200K for 100GB-1TB/day (per-connector MAR, practitioner-reported) | A |
| [Matillion Data Productivity Cloud](https://www.matillion.com) | Cloud-native ELT for Snowflake, Redshift, and BigQuery; visual orchestration with push-down execution and Maia AI agents. | cloud | $2.00-2.30/credit (1 credit = 1 vCore-hr); edition minimums $12K-£27.6K/yr (G-Cloud 14, 2024) | A |
| [Qlik Talend Cloud](https://www.talend.com) | Enterprise data integration suite with 1000+ connectors; batch ETL, real-time replication, quality, and governance. | cloud, on-prem, hybrid | contact-sales; estimated ~$12K-50K+/yr enterprise (no public list; estimate, Tier C) | A |
| [Tenzir](https://tenzir.com) | Open-source security data pipeline with MCP-enabled AI parser generation; vendor-stated automatic source-to-OCSF mapping, normalization, and SIEM-routing cost reduction (Tier D, not independently validated) | cloud, on-prem, hybrid | OSS/Community free ≤1TB/day; Professional/Enterprise/Sovereign contact-sales | D |

## Observability Platform

| Vendor | Description | Deployment | Cost Range | Evidence |
|--------|-------------|------------|------------|----------|
| [Axiom](https://axiom.co) | Serverless event platform storing high-volume logs, metrics, and traces cheaply via index-free APL query pipelines. | cloud | free to 500GB/mo; Axiom Cloud from $25/mo (1,000GB ingest); overage $0.030/GB | D |
| [Datadog](https://www.datadoghq.com) | Cloud-scale monitoring, security, and analytics platform; 600+ integrations correlating metrics, traces, and logs with anomaly detection. | cloud | Infra $15/host/mo; log ingest $0.10/GB + $2.55/M events indexed/mo | A |
| [Dynatrace](https://www.dynatrace.com) | AI-powered full-stack observability; Davis causal-graph reasoning and automatic indexing for root-cause analysis. | cloud, on-prem, hybrid | flat $0.08/hr per 8 GiB host (infrastructure monitoring) | A |
| [Grafana Cloud](https://grafana.com/products/cloud/) | Managed full-stack observability with Loki (logs), Tempo (traces), and Mimir (metrics) across cloud environments. | cloud, on-prem, hybrid | free to 3 users/10K metrics; Pro from $29/mo + usage-based | A |
| [Honeycomb](https://www.honeycomb.io) | High-cardinality observability for distributed systems; BubbleUp anomaly detection and interactive trace debugging. | cloud | Free ≤20M events/mo; Pro from $130/mo (100M events, unlimited seats) + $0.10/GB telemetry; Enterprise custom | A |
| [New Relic One](https://newrelic.com) | Unified observability platform with AI-powered insights; full-stack APM and log correlation, 100GB/month free tier. | cloud | free to 100GB/mo; overage $0.30/GB ingest; Core users $49/mo | A |
| [Splunk Observability Cloud](https://www.splunk.com/en_us/products/observability.html) | Full-stack observability with APM, infrastructure monitoring, and RUM; real-time metrics, tracing, AI-driven incident correlation. | cloud | $25/$95/$125 per host/mo (Infra / App+Infra / End-to-End suites; 100-200 host min); G-Cloud 14 | A |

## Object Storage

| Vendor | Description | Deployment | Cost Range | Evidence |
|--------|-------------|------------|------------|----------|
| [Amazon S3](https://aws.amazon.com/s3) | Cloud object storage with 11-nines durability; the default data-lake foundation, lifecycle policies, versioning, cold tiers. | cloud | $0.023/GB/mo Standard (US East); retrieval + API requests separate | D |
| [Azure Blob Storage](https://azure.microsoft.com/services/storage/blobs) | Object storage with 11-nines durability; Hot, Cool, and Archive tiers and SFTP for Microsoft-centric workloads. | cloud | Hot $0.021, Cool $0.015, Archive $0.00099 per GB/mo (US East list) | D |
| [Ceph Object Storage (RGW)](https://ceph.io) | Open-source distributed storage with S3-compatible API; customizable redundancy on commodity hardware nodes. | cloud, on-prem, hybrid | OSS free (LGPL 2.1); self-hosted infra/hardware only | A |
| [Google Cloud Storage](https://cloud.google.com/storage) | Scalable GCP object storage with multi-class tiers; unified API, geo-replication, lifecycle transitions, BigQuery integration. | cloud | $0.020/GB/mo Standard; internet egress $0.04-0.12/GB | D |
| [MinIO](https://min.io) | S3-compatible object storage for AI/ML; vendor-stated multi-gigabit throughput, Kubernetes-native. OSS core free, but the web console moved behind an enterprise license in late 2025 (community-reported ~$96K/yr) | cloud, on-prem, hybrid, edge | $30K-300K for 100TB+ (practitioner-reported); console requires Enterprise license | A |

## Data Virtualization

| Vendor | Description | Deployment | Cost Range | Evidence |
|--------|-------------|------------|------------|----------|
| [Apache Calcite](https://calcite.apache.org) | Open-source query planning and optimization framework; SQL parser and adapters across heterogeneous data engines. | cloud, on-prem, hybrid | OSS free (Apache 2.0); self-managed hosting/support only | A |
| [Denodo Platform](https://www.denodo.com) | Logical data warehouse with real-time data virtualization; query federation across cloud and on-prem sources. | cloud, on-prem, hybrid | Professional from $6.27/hr on Azure Marketplace (30-day free trial) | A |
| [Dremio](https://www.dremio.com) | Data lakehouse platform with semantic layer and query acceleration. | cloud, on-prem | $200K-800K for 10TB/day (practitioner-reported range) | A |
| [Starburst Enterprise](https://www.starburst.io) | Commercial Trino distribution; high-concurrency federated SQL across heterogeneous, decentralized cloud data sources. | cloud, on-prem, hybrid | $0.50 (Pro), $0.75 (Enterprise), $1.00 (Mission-Critical) per credit-hour | A | *(Also serves as Query Engine)* |

## Other

| Vendor | Description | Deployment | Cost Range | Evidence |
|--------|-------------|------------|------------|----------|
| [Knostic](https://knostic.com) | Need-to-know access control for LLMs, MCP servers, and coding agents; prevents unauthorized sensitive-data disclosure. | cloud, on-prem | contact-sales (value-based pricing tied to AI-tool adoption; early-stage, founded 2023) | D |

---

## Evidence Quality Ratings

Evidence quality ratings indicate the validation level for each vendor's capabilities and cost information:

| Rating | Description | Validation Source |
|--------|-------------|-------------------|
| **A** | Production-validated | Direct production experience, expert interviews, verified case studies |
| **B** | Expert-validated | Thought leader endorsement, published benchmarks, analyst reports |
| **C** | Community-validated | Blog posts, conference talks, GitHub adoption metrics |
| **D** | Vendor-claimed | Marketing materials or documentation only; requires independent validation |

**Recommendation**: For production deployments, prioritize vendors with A or B evidence ratings. Vendors rated C or D may still be excellent choices but require additional due diligence.

---

## Methodology

This vendor landscape is maintained using the following methodology:

1. **Initial Population**: Vendors identified through literature review, expert interviews, and industry analysis
2. **Capability Mapping**: Each vendor assessed against 40+ capability dimensions (see MCP Server schema)
3. **Evidence Collection**: Cost and capability claims are checked against available sources and tiered A-D by how well they are corroborated; many capability and list-price claims are vendor-published (Tier C/D) and carry that caveat rather than an independent validation
4. **Continuous Updates**: Weekly synchronization between book appendix and MCP Server database
5. **Expert Review**: Quarterly review with industry practitioners for accuracy

**Contributing**: If you identify missing vendors or inaccurate information, please submit corrections via the [Security Architect MCP Server](https://github.com/flying-coyote/security-architect-mcp-server) repository.

---

*This appendix is synchronized with the Security Architect MCP Server vendor database to ensure consistency across book and tooling.*

