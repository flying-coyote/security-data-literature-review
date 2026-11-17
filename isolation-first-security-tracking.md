---
type: tracker
title: "Isolation-First Security Architecture: Evidence Tracker (RQ7–RQ10)"
created: 2025-11-14
updated: 2026-11-17
tags: [isolation-first-security, rq7-rq10, evidence-tracking, catalog-selection, compliance]
---

# Isolation-First Security Architecture: Evidence Tracker (RQ7–RQ10)

*Isolation-first* is the architectural idea that security telemetry can live on its own infrastructure (a dedicated account, VPC or VNet, separate from the corporate data platform that holds customer PII and financial data), so that network isolation and coarse IAM, granted per table, do the access-control work that a shared platform has to do with row-level security, column masking and fine-grained catalog policy. If that holds, an isolated security platform could skip a layer of policy machinery, pick its catalog on other grounds (vendor neutrality, versioning) and avoid the query overhead fine-grained controls add. This tracker follows the evidence on four research questions about that idea, which `METHODOLOGY.md` §5.4 formalizes.

The short version of where the evidence stands is that the idea is still a hypothesis. The production case studies first logged as support for it turned out, on checking, not to describe isolation-first designs at all, and the one measured number the review now has, a first-party engine-side benchmark, shows that the cost of row-level security depends on query shape rather than being a fixed penalty that isolation removes.

---

## Status by research question (as of 2026-11-17)

| RQ | Question | Evidence the corpus holds | Standing |
|---|---|---|---|
| RQ7 | How do isolation patterns affect query performance? | One first-party engine-side measurement of RLS cost (below); no third-party benchmark of catalog-layer RLS, masking or metadata-encryption overhead | Open; the 15-50% figure first stated here was a hypothesis with no source and has been withdrawn as a claim |
| RQ8 | Does isolation as the primary control satisfy SOC 2, ISO 27001 and NIST CSF? | None yet; no control mapping has been done | Open |
| RQ9 | Where is the threshold between multi-tenant MSSP designs that need RLS and single-tenant SOCs that can isolate? | No MSSP architecture source; no single-tenant source that documents an isolation decision | Open |
| RQ10 | Does isolation change catalog selection toward Polaris or Nessie? | Catalog documentation only; no deployment that ties catalog choice to isolation | Open |

### The measured evidence: engine-side RLS cost

The review's first-party benchmark (`ocsf-rls-overhead` in the public lab repository, https://github.com/flying-coyote/sdw-lab-benchmarks/blob/master/ocsf-rls-overhead/results/RESULTS.md, run 2026-06-08 on DuckDB 1.5.3 over a 1,000,000-row, 100-tenant OCSF corpus, seven trials after two warm-ups) enforces tenant isolation two ways, as an appended `WHERE tenant_id` predicate and as a secured view, and both return identical answers on every query. At 1% selectivity a full-scan `count_all` goes from a 0.7 ms median to 1.3 ms, 81% slower under the predicate and 94% slower under the view though the difference is well under a millisecond, while a high-cardinality `top_talkers` aggregation goes from 33.0 ms to 4.8 ms, 86% faster under either, because the tenant filter discards about 99% of the rows before the expensive grouping. So whether RLS costs or saves time depends on whether the predicate adds work to the plan or removes it, and a single "RLS adds N%" figure is the wrong shape of answer. The measurement is a lower bound on the RLS side, since catalogs such as Apache Polaris, Unity Catalog and AWS Lake Formation enforce policy before the engine plans and add token validation and policy evaluation that DuckDB's predicate does not, and it is cited at Tier B as a single-host result (bibliography entry "OCSF RLS Overhead, SDW Lab First-Party Measurement").

### What the earlier case studies do and do not show

Three production deployments were logged as isolation-first case studies in November 2025, and on checking none of them documents the pattern.

- **Netflix** (ClickHouse + Iceberg logging platform): the source is a ClickHouse blog post dated 2025-10-23, based on a July 2025 talk, describing roughly 5 PB/day of logs. It names Polaris only as one of several pluggable Iceberg catalogs and says nothing about an isolated security platform, compliance or table-level RBAC. The isolation framing was withdrawn on 2026-07-09 as a mis-attribution, and the entry is now Tier B.
- **Huntress** (Elasticsearch to ClickHouse migration): the primary (https://clickhouse.com/blog/how-huntress-improved-performance-and-slashed-costs-with-clickHouse, 2024-11-19) reports cutting costs "by more than 90%", from "upwards of $70,000 per month" to "around $5,000 per month", across "more than 3 million endpoints" at "up to 200,000 records per second". It does not mention Iceberg, VPC isolation or table-level RBAC (checked 2026-11-17), so it is evidence for ClickHouse cost at security scale, not for isolation-first.
- **Okta** (DuckDB at production volume): the public Data Council 2024 talk supports DuckDB processing at production volume, the subject of H-EDGE-01. The isolation claims were attributed to a 2025 expert validation that never took place, and were withdrawn on 2026-08-12.

---

## What would move each question

**RQ7, performance.** A catalog-layer measurement on the same corpus (Polaris principal roles, Unity Catalog row filters, Lake Formation cell-level permissions) to set against the engine-side floor above, and vendor documentation that states masking or row-filter overhead with a method. Databricks documents row filters and column masks; whether it publishes overhead figures with a method has not been checked. Iceberg metadata encryption is a second measurement target, since its query-latency cost has no source in the corpus yet.

**RQ8, compliance.** A mapping of isolation-as-primary-control against current control sets. The original plan named ISO 27001 Annex A.13.1 and NIST CSF PR.AC-5, and both have since been renumbered:
- ISO/IEC 27001:2022 restructured Annex A into four themes; segregation of networks is now control 8.22 (it was A.13.1.3 in the 2013 edition), with network security at 8.20 and information access restriction at 8.3
- NIST CSF 2.0 (February 2024) removed the PR.AC category; NIST's CSF FAQ says its content moved to PR.AA and was re-sequenced, and network protection now sits under PR.IR-01 ("networks and environments are protected from unauthorized logical access and usage"). The PR.AC-5 to PR.IR-01 correspondence here is by subject; confirm it against NIST's official CSF 2.0 informative references before relying on it
- NIST CSF 1.1 PR.DS-5 (protections against data leaks), which the original plan also cited, was renumbered as well; a third-party listing of NIST's informative references maps it to PR.DS-10 (data in use), and whether the data-at-rest and data-in-transit outcomes at PR.DS-01 and PR.DS-02 also take it over is unconfirmed. Confirm against NIST's official crosswalk before relying on it
- SOC 2 CC6.1 (logical access) and NIST SP 800-207 (Zero Trust Architecture, 2020) and CISA's Zero Trust Maturity Model (version 2.0, 2023) remain the current references for the access-control and segmentation arguments

**RQ9, multi-tenancy.** A published architecture from a multi-tenant security service provider describing how it separates tenant data (per-tenant accounts or clusters versus shared tables with RLS), and AWS's SaaS tenant-isolation guidance as the vendor-neutral baseline. The candidates first named for this were Arctic Wolf, Expel and Red Canary, whose published architectures, if they describe tenant separation, would be the place to start. None is catalogued yet.

**RQ10, catalog choice.** A deployment write-up in which the choice of Polaris, Nessie or Unity Catalog is explained by the isolation decision. The leads first noted were Nessie production deployments, where Git-style versioning of tables would be the selection reason, and Apache Gravitino as a federating meta-catalog over several of these. Feature comparison alone cannot answer this, since it says what each catalog offers rather than why a team chose one.

### Search terms in use

- Isolation: "dedicated security data lake", "isolated security account", "network isolation as security boundary", "separation of duties security data"
- Performance: "row-level security overhead", "column masking performance", "row filter performance", "catalog access overhead", "Iceberg encryption overhead"
- Compliance: "ISO 27001 8.22 data lake", "SOC 2 CC6.1 data lake", "CSF 2.0 PR.IR segmentation", "zero trust security data"
- Architecture: "multi-tenant MSSP architecture", "tenant isolation data lake", "catalog selection criteria", "Polaris catalog adoption", "Nessie catalog production", "Gravitino meta-catalog"

---

## History

This tracker was created on 2025-11-14 alongside RQ7-RQ10, during the November 2025 monthly update. As first written it stated two headline figures, "15-50% query latency savings by avoiding catalog overhead" and "79% savings (500TB security data lake) by eliminating Unity Catalog licensing + compute overhead", neither of which had a source; they were planning targets written as findings and are withdrawn as claims (re-checked 2026-11-17: no bibliography entry, research-journal row or primary carries either). It also listed Netflix, Huntress and Okta as validating case studies, a Huntress scale figure of 1M EPS that the cited blog does not support (removed from the bibliography in the 2026-06 audit), and a Q1 2026 plan that depended on expert interviews which did not take place. The planned blog posts, the MCP-server recommendation logic and the mid-2026 journal target it referred to were overtaken by the retirement of the Substack (2026-05-24), the archiving of the MCP server repository (2026-07-01) and the choice of the Journal of Cybersecurity as the venue (2026-07-10). The November 2025 text is in the repository's git history; the change record is in `CHANGELOG.md`.

---
**Last updated**: 2026-11-17 (rewritten to current evidence; case studies re-checked at their primaries)
