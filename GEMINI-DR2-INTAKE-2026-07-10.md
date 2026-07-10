---
type: verification-report
title: "Gemini DR-2 intake — vendor-landscape delta scan Q2-Q3 2026, verified 2026-07-10 (staged for the next appendix-g pass)"
created: 2026-07-10
tags: [gemini-dr, intake, vendor-landscape, appendix-g, verification]
---

# Gemini DR-2 intake — vendor-landscape delta scan (late Q1 – July 2026)

**Run**: DR-2 from `~/project1/02-projects/GEMINI-DR-QUEUE-2026-07-10.md` (fired 2026-07-10; output Google Doc `1ELZp1JDPxVKhlXtmGi9e8cdwVNzq2gvGLmrZNVl0LSA`). All 28 grouped ledger checks verified at vendor primaries (workflow `wf_54e835a8-776`, 10 agents). **Disposition: STAGED for the next appendix-g / vendor-database.json quarterly pass** — appendix-g's July-10 review stamp is fresh, so these land as the input queue for the next touch rather than same-day edits.

## Verified firsthand at the vendor's own page (apply-ready)

| Vendor | Change | Date | Primary |
|---|---|---|---|
| Cisco/Splunk | Intent to acquire WideField Security (identity lifecycle → Agentic SOC) | 2026-06-18 | splunk.com acquisitions + blogs.cisco.com |
| Cisco | Intent to acquire Astrix Security (non-human identity) | 2026-05-04 | blogs.cisco.com (June 29 update noted) |
| Cisco | Intent to acquire Galileo Technologies (AI-agent observability) | 2026-04-09 | cisco.com acquisitions list (curl; WebFetch 403) |
| Google SecOps | Legacy Data Export API deprecated (shutdown 6/18) + v1→v2 CS-connector auto-migration (4/10) + legacy-forwarder restriction for new customers (4/1) | 2026-05-18 / 04-10 / 04-01 | docs.cloud.google.com/chronicle/docs/deprecations (all three rows verbatim) |
| Elastic | Per-endpoint pricing ELIMINATED for Elastic Security XDR | 2026-03-23 | ir.elastic.co press release |
| Securonix | Toby Weiss appointed CEO | 2026-06-29 | securonix.com press release |
| PANW (QRadar) | QRadar SaaS (QROC/SIEM/SOAR/Log Insights) EOL 2026-04-14; remaining suite (EDR/XDR/X-Force TI/Advisor) EOL 2026-08-31 | as stated | paloaltonetworks.com EOL summary (both rows verbatim) |
| SentinelOne | Prompt AI Agent Security unveiled + Purple AI one-click Auto Investigation GA (RSAC dateline) | 2026-03-23 | sentinelone.com press (note: Prompt AI announced, not stated GA) |
| PANW | Idira identity platform launched, absorbing/extending CyberArk PAM (migration paths for CyberArk SaaS customers) | 2026-05-12 | investors.paloaltonetworks.com |
| PANW | CSSP program EOS 2026-04-01 (shutdown 2026-10-01); Prisma Access Panorama plugin <5.2 EOL 2026-04-30; Panorama multi-tenancy phased out for greenfield 2026-04-15 | as stated | paloaltonetworks.com EOL announcements (all three verbatim) |
| PANW | Intent to acquire Koi (agentic endpoint) | 2026-02-17 | paloaltonetworks.com press (child URL; year-index paginated past it) |
| Graylog | 7.1 released (anomaly detectors, impossible travel, case-based triage) | 2026-05-04 | graylog.org blog |
| Torq | Acquired Jit (AI Context Graphs → Torq AI SOC Platform) | 2026-05-19 (page byline 5/18) | torq.io/news |
| ClickHouse | $250M ARR / 4,000 customers; ClickHouse Agents (Claude-powered) + CostBench launched; House Mates partner program (Fivetran, dbt Labs) | 2026-05-27 (JSON-LD) / Q2 | clickhouse.com blog (both posts) |
| IBM | COMPLETED Confluent acquisition, ~$11B EV, $31/share cash | 2026-03-17 | newsroom.ibm.com |
| Databricks | Genie products → PAYG DBU pricing + 150 free DBUs/mo (7/8); Okta automatic identity GA (7/3); Lakehouse Real-Time Beta + Claude Sonnet 5 hosted (6/30) | as stated | docs.databricks.com release notes (July + June) |
| Snowflake | ALTER ACCOUNT SET EDITION GA (5/6); redesigned Snowsight Cost Management w/ CoCo (7/7, announced GA at Summit) | as stated | docs.snowflake.com + snowflake.com blog |
| Fivetran | 2026 pricing updates: $5/mo connection minimum (1–1M MAR), deletes billed as MAR, history-mode repeats billed, Activations (ex-Census) separately billed from Feb | 2026-01-01 / Feb | fivetran.com docs (all four verbatim) |
| Cribl | Cribl Search dual-engine (Federated + new Lakehouse Engine, Cloud Credits) | 2026-03-11 | cribl.io blog |
| Estuary | $0.50/GB volume + Task Hours $0.14→$0.07/hr beyond 6 connectors | figures exact; page undated (Q2 unprovable) | docs.estuary.dev |

## Corrections and caveats found during verification (the run's errors)

- **Airbyte capacity-based Data Workers pricing: introduced 2025-02-11, NOT "mid-2026"** (Airbyte's own firsthand blog; the DR's secondhand integrate.io source is undated). MISMATCH — carry the corrected date.
- **CrowdStrike Falcon AIDR GA: 2025-12-15** per CrowdStrike's own press release (Austin dateline), NOT "March 2026" (CRN's July roundup gives no date). MISMATCH — carry the corrected date.
- **CrowdStream decommission**: EOL confirmed at Cribl's docs+blog, but the specific 2026-04-20 date does not appear on either primary ("March 2026" announcement per docs; the 4/20 regional date traces only to a Reddit post quoting the CrowdStrike notice). PARTIAL — treat the date as secondhand.
- **Snowflake × Select Star: this is an ACQUISITION with firsthand sources on both sides** (snowflake.com "definitive agreement to acquire the Select Star team and platform technology" + selectstar.com) — the DR ledger under-labeled it as a secondhand Summit-integration story. Upgrade on landing; exact announcement date needs one more look at the Snowflake post.
- **Collibra**: PostgreSQL-14 EOL row exact (support ends 2026-11-12, announced with release 2026.03); the lastSyncDate/continueOnError row only half-matched (the deprecation announcement is under release 2026.05 external-mappings changes, not April) — re-check the row detail when applying.
- **Third-party-sourced rows** (siemcostcalculator.com for Google Data Benefit Program 2/1, Exabeam Nova modular pricing, Sumo credit tiers; solutionsreview for DataBee RiskFlow; integrate.io for Airbyte): all confirmed as stated at those third-party pages, but none is a vendor primary — label SECONDHAND if carried into appendix-g.

## Not carried

"No change found" list from the DR (Microsoft Sentinel, Rapid7, Devo, Gurucul, Stellar Cyber, Panther, Anvilogic, Hunters, Grafana Loki, Wazuh, Query.ai, Hydrolix, LimaCharlie, Velociraptor, Zeek, Tracecat, StarRocks, Trino, Starburst, Presto, Pinot, Drill, Impala, Athena, BigQuery, Redpanda, Kinesis, Kafka, Flink, Pulsar, RabbitMQ, Event Hubs, Pub/Sub, Delta Lake, Iceberg, Hudi, Paimon, Druid, Dremio, Denodo, Calcite, Glue, Atlas, Atlan, DataHub, Purview, Matillion, Qlik Talend, Tenzir, Databahn.ai, NiFi, Datadog, Dynatrace, New Relic, Honeycomb, Grafana Cloud, Axiom, MinIO, Ceph, S3, Azure Blob, GCS, Knostic) — accepted as absence-of-evidence only; the next quarterly pass should not treat it as verified-no-change.
