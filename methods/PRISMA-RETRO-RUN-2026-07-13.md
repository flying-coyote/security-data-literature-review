---
title: PRISMA Retro-Run — what the systematic search found
date: 2026-07-13
run_timestamp_utc: 2026-07-13T02:36:26Z
protocol: methods/PRISMA-SEARCH-PROTOCOL-2026-07-13.md
outputs: methods/prisma-results/
---

# PRISMA Retro-Run (2026-07-13): what the search found and what it costs the manuscript

## 1. What this review actually is

The corpus underneath this review was built by curation between 2025 and 2026 — reading, following citations, tracking vendor engineering blogs and open-source project docs, interviewing practitioners, and running first-party lab measurements. There was no systematic database search at the front of it. The systematic search described in `PRISMA-SEARCH-PROTOCOL-2026-07-13.md` was designed and executed afterward, on 2026-07-13, for one purpose: to test what that curated corpus had missed.

So the review discloses itself as a **retrospectively-verified curated review**, not a prospective systematic review. It did not run a search and then build a corpus from the results; it built a corpus and then ran a search against it to measure the gap. That distinction is the difference between a claim the manuscript can defend and one a reviewer would break, and the honest version is worth more than the flattering one — particularly given what §2 says about the figure this work replaces.

## 2. The finding that motivated this work

The review previously carried `publication-graphics/figure1_prisma_flowchart.tex`, titled and captioned as a "PRISMA-aligned systematic literature review flowchart". It is not one. Read the boxes: identification lists "Best Practices Document: 283 footnotes" and "Archive Manuscripts: 74 files assessed"; screening reports "Citations Extracted: 283" by "automated URL extraction from markdown footnotes" and concludes "No independent citations found beyond 283 footnotes"; and the included box reports "Total Unique Sources: 75+" against a bibliography that now holds 195 entry blocks. There is no database in that flow, no query string, no date window, and no eligibility criteria beyond a two-line quality note. What the figure describes is a citation harvest of the author's own prior best-practices document plus the archive manuscripts that reference it, drawn in the shape of a PRISMA diagram and captioned with PRISMA's authority.

Calling that a systematic literature review flowchart was wrong. It is the kind of thing a reviewer finds, and finding it first is the point of this exercise. The figure is being replaced with a PRISMA 2020 two-arm flow diagram built from the run recorded below — a database arm carrying the real search, and an "other methods" arm carrying the curated grey literature, which is where that material honestly belongs.

## 3. The search: identification through inclusion

Run 2026-07-13T02:36:26Z. Script `scripts/prisma_search.py`; log at `methods/prisma-results/search-log.json`; records at `methods/prisma-results/records.json`; screening decisions at `methods/prisma-results/screen-batch-0.json` … `screen-batch-9.json`.

| stage | n |
|---|---|
| Records identified — OpenAlex | 354 |
| Records identified — dblp | 46 |
| Total raw records identified | 400 |
| Duplicates removed (DOI) | 1 |
| Duplicates removed (normalized title) | 4 |
| Duplicates removed (total) | 5 |
| Unique records screened | 395 |
| Excluded at title/abstract screening | 355 |
| **Included** | **40** |

OpenAlex reported `meta.count` = 354 and cursor paging retrieved all 354 across two pages, so retrieval was complete rather than truncated. dblp returned 46 records across eight title queries: `security data warehouse` 33, `security data lake` 8, `intrusion detection stream processing` 5, and five queries returning zero (`SIEM data lake`, `security analytics lakehouse`, `security log stream processing`, `threat detection Kafka`, `security telemetry pipeline`). Those zeros are genuine `@total=0` responses rather than failures — dblp matches titles only, with AND semantics, so those exact phrase combinations have no title hits. No query was silently dropped: the failed-query list in `search-log.json` is empty, which is the checkable claim. Several dblp calls did return a transient HTTP 500 or 503 and succeeded on retry, but that was observed in the run's console output and the first version of the script did not record it, so a reviewer could not verify it from the artifacts. The script now writes a per-query `retries` count into `search-log.json`, so on any re-run the retry behaviour is checkable rather than asserted.

**Exclusions by governing criterion** (355 records, one criterion each, from the ten screening batches):

| criterion | n | what it caught |
|---|---|---|
| E2 | 137 | data-engineering paper with no security application |
| E1 | 103 | ML/DL intrusion-detection model riding on a streaming platform without evaluating the architecture |
| I1 | 36 | published before 2018-01-01 (all 36 are dblp records; the dblp API takes no date parameter, so the floor is enforced here) |
| E3 | 35 | survey with no architecture-level content of its own |
| E6 | 13 | duplicate of an already-included record |
| E4 | 11 | abstract, poster, editorial, or under ~4 pages |
| I2 (failed) | 10 | not about the data architecture handling security telemetry |
| I3 (failed) | 8 | no measurement, benchmark, deployment, or substantive design evaluation |
| E5 | 2 | not in English |

E1 alone accounts for 103 of the 355 exclusions, which confirms the criterion was written for the right false positive: the dominant thing this query returns is a classifier's accuracy on NSL-KDD or CICIDS with Kafka mentioned as plumbing.

**Two coverage findings from identification**, both of which are properties of the search worth reporting rather than smoothing over. First, cross-database overlap is one record, not five: the by-source breakdown is OpenAlex 349, dblp+OpenAlex 1, dblp 45, so exactly one paper was found by both databases (the single DOI-matched duplicate), and the four title-matched duplicates were all *within* OpenAlex. dblp contributed 45 records that OpenAlex's boolean filter never returned. Near-zero overlap between two databases searching the same field is a statement about how differently they index, and it argues that a third database would likely add records again rather than confirm these. Second, 318 of the 395 unique records carry an abstract and 367 carry a DOI; dblp supplies no abstracts, which is the whole of the abstract gap and means the 45 dblp-only records were screened on title, venue, and year.

## 4. Reconciliation against the curated corpus

`methods/prisma-results/reconciliation.json`. The corpus is `MASTER-BIBLIOGRAPHY.md`, 195 `#### ` entry blocks, of which 193 carry an evidence level and 2 are documented no-primary stubs. Matching was attempted three ways: DOI (exact, case-normalized), normalized title (lowercased, punctuation and parentheticals stripped; exact, substring, and difflib fuzzy), and author surname plus year co-occurring inside a single bibliography block.

| set | n |
|---|---|
| A — overlap (search-included ∧ already in the corpus) | **0** |
| B — search-only (the gap list) | **40** |
| C — corpus-only grey literature (a database search could not have returned these) | **171** |
| corpus entries peer-reviewed and indexable in principle, yet not returned by this search | 24 |
| **measured recall of the curated corpus against this search** | **0 / 40 = 0.0** |

Set A is empty, and it is empty honestly. Only 8 of the 195 bibliography blocks carry a DOI at all and none of those 8 is among the 40. Normalized-title matching fails at every level — the best fuzzy ratio across the full 40 × 195 grid is 0.54, between "Machine learning based network intrusion detection for data streaming IoT applications" and "Outside the Closed World", which is a coincidence of vocabulary and not a match. Author-plus-year produced five surname collisions, all on "Zhang", all rejected because the titles are unrelated.

So the curated corpus's measured recall against its own systematic search is zero. That number needs its context to be read correctly rather than to be softened: the corpus was built out of the grey literature this field actually runs on, and the search reaches only the journal-and-conference literature, and the two sets turn out to be nearly disjoint. Zero recall is not a claim that the corpus is bad — it is a claim that the corpus and the search cover different literatures, which is exactly the thing a retrospective search is for finding out.

### C — corpus-only grey literature, by kind (171)

These are the entries a database search could not have returned, because they are not journal or conference literature and are not indexed in OpenAlex or dblp. Under PRISMA 2020 they belong in the "identification of studies via other methods" arm of the flow diagram, which is where the replacement figure puts them:

| category | n |
|---|---|
| vendor engineering blogs / product docs (ClickHouse ×15, Databricks, Dremio, Confluent, AWS, Cribl, Tenzir, Panther, Splunk, …) | 63 |
| open-source project docs / specs / repos (Iceberg, Arrow, Trino, DuckDB, Polaris, DataFusion, Zeek, GitHub) | 33 |
| practitioner talks / personal blogs / LinkedIn / Substack | 18 |
| standards, frameworks, government (NIST, ISO, CISA, MITRE D3FEND/ATLAS/CAR, OCA, CSA, DARPA) | 17 |
| big-tech engineering blogs (Netflix, Uber, Cloudflare, Google, Microsoft, Anthropic) | 14 |
| analyst / industry reports (Gartner, Forrester, KPMG, Uptime Institute, DORA, Prosci) | 12 |
| books (O'Reilly ×3, No Starch, Manning, Pearson, Technics, one trade title) | 8 |
| expert interviews / personal communications | 2 |
| first-party SDW lab measurements | 2 |
| documented no-primary stubs (retired / declined) | 2 |
| **total** | **171** |

### The 24 academic corpus entries the search did not return

Counted apart from C because they are indexable in principle. Two — Axelsson 2000 and Sommer & Paxson 2010 — fall outside the 2018 date floor and could not have been returned. Most of the rest are database-systems papers in PVLDB, CIDR, and SIGMOD (Delta Lake, LHBench, FastLanes, F3, LogLite, Blitzcrank, DBSP, Ursa) whose titles and abstracts carry the storage half of the conjunctive query but not the security half, so the query as written could not reach them. That asymmetry is a property of the search strategy and it is recorded rather than patched over: a search built to find security-and-storage papers will not return the storage papers this review leans on hardest.

## 5. B — the search-only gap list (40, untruncated)

Every record the search included and the corpus does not hold. Each entry carries what it would add, so the manuscript work in §6 is scoped rather than gestured at. Records screened on title alone (no abstract retrieved) are flagged; read the full text before citing those.

1. **Performance Evaluation of Intrusion Detection Streaming Transactions Using Apache Kafka and Spark Streaming** — 2019, venue not recorded in OpenAlex, `10.1109/aitc.2019.8920960` (OpenAlex). First-party throughput and fault-tolerance measurement of a Kafka+Spark security ingest path on UNSW-NB15 — a peer-reviewed measurement of the pipeline itself, where the corpus has only vendor blogs.
2. **Toward a monitoring and threat detection system based on stream processing as a virtual network function for big data** — 2019, Concurrency and Computation: Practice and Experience, `10.1002/cpe.5344` (OpenAlex). CATRACA, a Spark-based VNF evaluated as a deployed threat-detection pipeline with concept-drift handling — a refereed instance of the detection-in-the-pipeline pattern.
3. **An evaluation of a virtual network function for real-time threat detection using stream processing** — 2018, preprint (MobiSecServ), `10.1109/mobisecserv.2018.8311440` (OpenAlex). Reports >5M messages/sec and sensor-migration latency — an academic throughput anchor for the streaming chapter, where the corpus leans on Confluent and Tenzir numbers.
4. **Machine learning based network intrusion detection for data streaming IoT applications** — 2021, `10.1109/snpdwinter52325.2021.00019` (OpenAlex). Head-to-head Flink vs Spark Streaming throughput on an IoT NIDS workload — a direct engine comparison with no academic counterpart in the corpus.
5. **Real-Time Intrusion Detection in Network Traffic Using Adaptive and Auto-Scaling Stream Processor** — 2018, GLOBECOM, `10.1109/glocom.2018.8647489` (OpenAlex). The "Wisdom" auto-scaling CEP processor at >2.5M events/sec with lower resource use than a monolithic deployment — evidence for the elastic-vs-monolith argument.
6. **A Monitoring and Threat Detection System Using Stream Processing as a Virtual Function for Big Data** — 2019, theses.fr / SBRC, `10.5753/sbrc_estendido.2019.7789` (OpenAlex). Sensor-placement heuristic and greedy VNF allocation — design evidence on where detection compute sits, which the corpus treats only qualitatively.
7. **DATA WAREHOUSE MODELLING INFORMATION SECURITY LOG MANAGEMENT IN BUILDING A SECURITY OPERATION CENTER IN CENTRAL GOVERNMENT AGENCIES WITH KIMBALL METHOD** — 2023, Jurnal Teknik Informatika (Jutif), `10.52436/1.jutif.2023.4.4.649` (OpenAlex). Kimball dimensional modelling applied to SOC log management — the only peer-reviewed dimensional-modelling treatment of security data in the search.
8. **Transforming Cybersecurity with AI-driven Dashboards: A Cloud-Native Implementation Framework for Real-Time Threat Detection and Automated Response** — 2022, Int. J. of Future Innovative Science and Technology, `10.15662/ijfist.2022.0505004` (OpenAlex). Four-layer cloud-native architecture with simulated MTTR/MTTD reductions; weak venue, tier it C.
9. **A study on time models in graph databases for security log analysis** — 2021, International Journal of Web Information Systems, `10.1108/ijwis-03-2021-0023` (OpenAlex). Three timestamp-storage models compared for query performance — the corpus has no graph-database anchor.
10. **Building a large scale Intrusion Detection System using Big Data technologies** — 2018, PoS, `10.22323/1.327.0014` (OpenAlex). CERN's production IDS processing ~1 TB/day — a named, non-vendor production-scale deployment.
11. **Efficient Host Intrusion Detection using Hyperdimensional Computing** — 2024, IEEE BigData, `10.1109/bigdata62323.2024.10825247` (OpenAlex). Provenance-graph query latencies argued to be impractical for modern detection — an academic statement of the query-latency problem the cost-to-serve argument rests on.
12. **High-performance FPGA Architecture for Data Streams Processing on Example of IPsec Gateway** — 2018, Int. J. of Electronics and Telecommunications, `10.24425/123532` (OpenAlex). Hardware acceleration at the ingest tier, a topic the corpus does not cover at all.
13. **Workload-Aware Storage Reduction for Multi-Tenant SIEM on ClickHouse** — 2026, IJACSA, `10.14569/ijacsa.2026.0170474` (OpenAlex). 79% uncompressed / 70% compressed storage reduction at sub-second latency — the closest peer-reviewed analogue to the SDW lab's ClickHouse results and a direct check on the corpus's ClickHouse claims.
14. **AIDA Framework** — 2019, ACM (ARES), `10.1145/3339252.3340513` (OpenAlex). A CEP framework deployed inside an alert-sharing platform, with a deployment evaluation.
15. **The Next-Generation NIDS Platform: Cloud-Based Snort NIDS Using Containers and Big Data** — 2022, Big Data and Cognitive Computing, `10.3390/bdcc6010019` (OpenAlex). Containerized Snort on a lambda-architecture backend with measured aggregation and delivery performance.
16. **Federated Stream-Processing and Latency-Gated Response for Cross-Sector Threat Detection and Collaborative Containment** — 2026, arXiv, `10.48550/arxiv.2605.17325` (OpenAlex). Federated stream processing reconciled inside a version-keyed columnar engine at 500K events/sec — the only record touching columnar storage and federation together, closest to the MOAR lakehouse thesis, but an unrefereed preprint.
17. **Towards Low-Latency Big Data Infrastructure at Sangfor** — 2022, Communications in Computer and Information Science (book chapter), `10.1007/978-3-031-23098-1_3` (OpenAlex). A security vendor's production infrastructure inside a peer-reviewed venue; **screened on title, no abstract — read the full text before citing.**
18. **Enhancing Cybersecurity Through the Unification of Data Analytics, Artificial Intelligence, and Machine Learning in Big Data Cloud Environments: A Databricks Lakehouse Approach** — 2023, IJCTT, `10.14445/22312803/ijctt-v71i6p104` (OpenAlex). The search's only lakehouse-for-security paper; weak venue, but the academic counterpart to the corpus's Databricks vendor material.
19. **Securing Big Data Pipelines in Healthcare: A Framework for Real-Time Threat Detection in Population Health Systems** — 2025, Research Corridor Journal of Engineering Science, `10.66320/aen33a42` (OpenAlex). Kafka + Splunk layered pipeline, 2.5M events/sec and 500 ms detection latency in simulation — a domain the corpus never covers.
20. **Architecting Petabyte-Scale Stream Processing Systems for Cybersecurity: A Sharded Data and Compute Processing Strategy for Minimizing Incident Response Time in Real-Time Enterprise Defense** — 2026, Open MIND (Zenodo), `10.5281/zenodo.18817603` (OpenAlex). Compute-sharded petabyte-scale design with multi-region topology and schema-agnostic ingestion; Zenodo/Open MIND venue, tier it C.
21. **A Cloud-Native Framework for Real-Time Topology Analysis and Security Monitoring in SDN Environments** — 2026, Advances in Science and Technology (book chapter), `10.1201/9781003774679-27` (OpenAlex). Kafka + OrientDB monitoring with measured topology-discovery accuracy — extends the review into SDN telemetry.
22. **A Data Middle Platform-Based Power Grid Data Security Monitoring System** — 2025, IEEE AIBDF, `10.1109/aibdf67964.2025.11440698` (OpenAlex). A MaxCompute warehouse for grid security monitoring, compared experimentally against mainstream SIEM tooling — relevant to the OT sections.
23. **Hybrid Stream Processing for Runtime Protection in Remote and Infrastructure-Supported Driving** — 2026, IEEE ICIN, `10.1109/icin69025.2026.11481838` (OpenAlex). Distributed stream processing (a GALOIS extension) where the online operator beats the offline detector — an automotive-OT case for streaming-vs-batch.
24. **Performance Comparison of Python-Based Complex Event Processing Engines for IoT Intrusion Detection: Faust Versus Streamz** — 2026, Computers (MDPI), `10.3390/computers15030200` (OpenAlex **and** dblp — the single record hit by both databases). A like-for-like CEP engine benchmark of exactly the kind the lab builds itself, peer-reviewed.
25. **SPARCS: Stream-Processing Architecture Applied in Real-Time Cyber-Physical Security** — 2019, IEEE eScience, `10.1109/escience.2019.00028` (OpenAlex). An end-to-end fault-tolerant collection / transport / storage / processing reference design.
26. **General purpose data streaming platform for log analysis, anomaly detection and security protection** — 2024, EPJ Web of Conferences, `10.1051/epjconf/202429501032` (OpenAlex). The INFN-CNAF WLCG Tier-1 production platform — a second named non-vendor large-scale deployment alongside CERN.
27. **Practical Performance of a Distributed Processing Framework for Machine-Learning-based NIDS** — 2024, IEEE COMPSAC, `10.1109/compsac61105.2024.00355` (OpenAlex). Measures the framework's own throughput and bottlenecks with five NIDS classifiers as workload — the cleanest separation of pipeline performance from model accuracy in the set, which is this review's methodological stance.
28. **Corporate Security is a Big Data Problem** — 2018, ACM Ubiquity, `10.1145/3158348` (OpenAlex). A security-data-lake-to-"security cockpit" architecture — a 2018 academic statement of a thesis the corpus dates to vendor writing.
29. **Aprendizado de Máquina em Plataformas de Processamento Distribuído de Fluxo: Análise e Detecção de Ameaças em Tempo Real** — 2018, book chapter, **no DOI** (OpenAlex). Portuguese-language comparison of Storm, Spark Streaming, and Flink including lambda-architecture proposals; outside the English-language corpus, and acquisition needs checking since there is no DOI.
30. **ARCHITECTURAL AND ANALYTICAL ASPECTS OF BIG DATA APPLICATION FOR ENSURING IOT SYSTEM SECURITY** — 2026, Cybersecurity Education Science Technique, `10.28925/2663-4023.2026.33.1144` (OpenAlex). Multi-layer big-data architecture with a data-lake storage tier and simulated DDoS results.
31. **BUILDING A DYNAMIC SCALABLE PARALLEL CLOUD-BASED SNORT NIDS USING CONTAINERS AND BIG DATA** — 2021, Journal of Southwest Jiaotong University, `10.35741/issn.0258-2724.56.5.27` (OpenAlex). A companion measurement to #15, from the same line of work.
32. **МЕХАНИЗМЫ ВЗАИМОДЕЙСВИЯ МЕЖДУ РАСПРЕДЕЛЕННЫМИ IDPS И SOC В ИНФРАСТРУКТУРАХ УМНЫХ ГОРОДОВ НА ОСНОВЕ IoT** — 2025, Int. J. of Information and Communication Technologies, `10.54309/ijict.2025.24.4.002` (OpenAlex). Kafka bus + STIX/TAXII normalization + Elastic SIEM, reporting ~28% correlation-latency and ~30% false-positive reductions — the only record in the search that treats schema normalization end-to-end, which is the OCSF question the corpus cares most about.
33. **Analysis of Logs in the Environment of Email Services** — 2020, IEEE ICETA, `10.1109/iceta51985.2020.9379260` (OpenAlex). Compares Elasticsearch, Kafka, Redis, Splunk, and MongoDB as log stores for email-service audit records — a store-selection comparison for the query-engine chapter.
34. **Practical Performance of a Distributed Processing Framework for Machine-Learning-based NIDS** — 2024, arXiv, `10.48550/arxiv.2405.13066` (OpenAlex). The arXiv version of #27, same title under a distinct DOI; kept in the flow because it shows the preprint/version duplication that DOI-level deduplication cannot merge.
35. **A Binary Feature Extraction Based Data Provenance System Implemented on Flink Platform** — 2018, CyberC, `10.1109/cyberc.2018.00045` (OpenAlex). Data-provenance and information-flow-control implemented on Flink — provenance-as-security-telemetry, a pattern the corpus does not carry.
36. **Comparative Evaluation of Log Reduction Techniques Using Vector on Public Security Datasets** — 2026, ECTI Transactions on Computer and Information Technology, `10.37936/ecti-cit.2026202.264216` (OpenAlex). Benchmarks five Vector-based log-reduction methods against a Filebeat baseline over 3M+ SOC records, reporting throughput, bandwidth, and attack coverage — a peer-reviewed check on the pipeline-reduction economics the corpus sources from vendors.
37. **Engineering a Cloud Security Incident Detection and Response Pipeline for Large-Scale and Operationally Resilient Environments** — 2025, International Journal of Research Publication and Reviews, `10.55248/gengpi.06.1225.4219` (OpenAlex). A pipeline evaluated on detection accuracy, response time, availability, and operational overhead; low-tier venue, tier it C.
38. **A data lake-based security transmission and storage scheme for streaming big data** — 2024, Cluster Computing, `10.1007/S10586-023-04201-9` (dblp). A peer-reviewed security-data-lake design; **screened on title, no abstract — read the full text before citing.**
39. **Digital forensics architecture for real-time automated evidence collection and centralization: Leveraging security lake and modern data architecture** — 2024, Journal of Intelligent Systems, `10.1515/JISYS-2024-0109` (dblp). The closest peer-reviewed match to the security-data-lake thesis in the whole search; **screened on title, no abstract — read the full text before citing.**
40. **International Network Performance and Security Testing Based on Distributed Abyss Storage Cluster and Draft of Data Lake Framework** — 2018, Security and Communication Networks, `10.1155/2018/1746809` (dblp). An early (2018) data-lake-for-security design; **screened on title, no abstract — read the full text before citing.**

## 6. What the author owes the manuscript

- **Replace figure 1.** `figure1_prisma_flowchart.tex` goes, and a PRISMA 2020 two-arm flow diagram replaces it, built from §3 and §4: a database arm (400 identified → 5 duplicates removed → 395 screened → 355 excluded with the criterion breakdown → 40 included) and an "identification via other methods" arm carrying the 171 grey-literature entries plus the 24 academic entries the query could not reach. No box in the new figure may carry a number that is not in `methods/prisma-results/`.
- **Retire "75+ sources."** The bibliography holds 195 entry blocks, 193 with an evidence level and 2 documented no-primary stubs. Every surface still claiming 75+ — the manuscript's contribution section says it — gets the real count.
- **Rewrite the methods section as a retrospectively-verified curated review.** State the curation-then-search order, state that screening was LLM-performed against pre-specified criteria with every decision on disk, state the single-screener limitation, and state that no subscription database was searched.
- **Triage the 40.** Read them, tier them, and admit the ones that survive. Several are direct checks on claims the corpus currently sources from vendors — #13 on ClickHouse storage reduction, #36 on pipeline log-reduction economics, #24 on CEP engine comparison — and those are the ones a reviewer would go looking for. Four (#17, #38, #39, #40) were screened on title alone and need a full-text read before they can be cited at all.
- **Report the zero recall rather than bury it.** The measured recall of 0/40 is the headline result of this run, and the manuscript is stronger for stating it with its explanation (the corpus and the search cover nearly disjoint literatures) than for leaving a reviewer to compute it.
- **Disclose the search's own blind spot.** The conjunctive query cannot reach the storage-only literature that the review leans on hardest — 24 peer-reviewed corpus entries, most of them PVLDB/CIDR/SIGMOD papers, were unreachable by construction. A future run needs a second query arm on the storage side, and until it exists, this limitation belongs in the limitations section.

---

## Addendum (2026-07-16): eight entries were invisible to this run's corpus counter

This run counted the curated corpus at 195 entry blocks (193 tiered + 2 stubs) everywhere above. On 2026-07-16 a counter audit found eight full bibliography entries headed `### ` instead of `#### ` since their November-2025 addition — invisible to the `(?m)^####\s+` split that `parse_master_bibliography()` and this run's reconciliation both use. The corpus at run time was therefore 203 blocks (201 tiered: 179 grey + 24 academic), and the headings were promoted the same day, with a conformance lint added to `scripts/count_reconcile.py` so a mis-leveled heading now fails the gate.

The run's results are unaffected in substance: all eight are grey vendor/OSS items (Confluent and Databricks survey reports, Tenzir, Cribl, Vortex, Databricks MCP Catalog, Apache Polaris docs, Unity Catalog RLS), none resembling any of the 40 database-arm academic records, so the 0/40 overlap and the zero-recall finding stand. Their taxonomy classifications live in `methods/heading-fix-2026-07-16.json` (a third dated input to `derive_source_taxonomy.py`); `reconciliation.json` and `incorporated-2026-07-13.json` are left unedited as frozen records per the never-retro-edit convention. The body of this document above retains its as-run 195/193 numbers as the historical record.
