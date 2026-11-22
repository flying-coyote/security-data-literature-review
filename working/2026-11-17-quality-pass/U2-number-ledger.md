---
type: review
title: "U2 number ledger: PUBLICATION-MANUSCRIPT.md main text, Tables 1-5 and figure captions"
created: 2026-11-17
status: complete
tags: [quality-pass, number-fidelity, manuscript]
---

# U2 number ledger (2026-11-17)

One row per stated number in the manuscript's main text (abstract through Conclusion), Tables 1-5 and the figure captions and alt text. Locations are by section because line numbers moved during the pass.

Verdict vocabulary:

- **verified-at-primary**: re-read at the primary on 2026-11-17 (URL or file:line given).
- **verified-at-record**: matches a committed verbatim verification record made at the primary (record named); not re-fetched this pass.
- **derived-gated**: derived from the bibliography or `methods/source-taxonomy.json` and checked by `scripts/count_reconcile.py` (79 surfaces, all agree on 2026-11-17).
- **arithmetic**: follows from other verified numbers; the arithmetic is shown.
- **historical-record**: an October-2025 or dated past figure, now labelled as such in the text; the October source documents sit outside the repository and are not re-verifiable here.
- **author-modelled**: illustrative planning figure, labelled as such in the text, carries no hypothesis.
- **corrected** / **relabelled** / **removed**: changed this pass; the change is described.

## Abstract and §1

| Location | Value | Source locator | Verdict |
|---|---|---|---|
| Abstract | 271 tiered sources (was 228) | count_reconcile Counter 2 | corrected, derived-gated |
| Abstract | zero of 40 recall | methods/prisma-results/reconciliation.json `corpus_recall_against_search: 0/40` | verified-at-record |
| Abstract | 14 of 40 refused, eight predatory/compromised | methods/prisma-appraisal-2026-07-13.json; Appendix E.3 rows (8 "Predatory or compromised venue") | verified-at-record |
| Abstract | 26 survivors, one more admitted | methods/incorporated-2026-07-13.json (26 entries); methods/second-screen-adjudication-2026-07-16.json | verified-at-record |
| Abstract, §1.4, §3.7 | nine hypotheses, seven original + two | manuscript §3.7 (canonical) | derived-gated |
| Abstract, §1.1, §1.4, §3.2.2, §3.5, §3.8, §4.1, §4.4, §5, Table 4 | 6M requests/second (Cloudflare) | https://blog.cloudflare.com/http-analytics-for-6m-requests-per-second-using-clickhouse/ ("On average we process 6M HTTP requests per second, with peaks of upto 8M") | verified-at-primary |
| Abstract, §3.2.2, §3.5, §3.6, §4.1-§4.3, §5 | ~13-17× CIDR speedup, 20M rows | security-data-that-works docker/README.md:228 (2026-06-07: ~0.010 s vs ~0.166 s, ~13-17×); docker/MOAR-EVIDENCE-RUN-2026-06-15.md:62-72 (canonical re-run: median ~0.007 s vs ~0.120 s, ~17×, conservative 14.5×) | verified-at-primary |
| Abstract, §4.1, §5 | 6-12 month proficiency ramp | none (labelled practitioner estimate; Gartner attribution withdrawn 2026-07) | author-modelled, labelled |
| Abstract, §3.7, §4.1 | 24,000-134,000 alerts/day; ~0.01% true attacks | Yang et al. USENIX Security 2024; MASTER-BIBLIOGRAPHY.md:4556 entry, verbatim-verified 2026-07-10 | verified-at-record; *2026-11-22: the figures hold, but the study covers one SOC ("a real-world SOC", 2018-2022, USENIX abstract), and the manuscript said "SOCs"; corrected to the singular* |
| §1.1, §3.2.3, §3.5, Table 4 | Azure "trillions of events daily" | https://azure.microsoft.com/en-us/blog/processing-trillions-of-events-per-day-with-apache-kafka-on-azure/ ("ingest and process 3 trillion events per day") | verified-at-primary |
| §1.1, §1.4 | "2-3 months" commonly assumed timeline | none located | unverifiable-no-primary; framed as an assumption the text argues against, left as is (staged) |
| §1.4 | 271 tiered (was 227) | Counter 2 | corrected, derived-gated |
| §1.4 | 6 evidence gaps | §3.8 enumerates six | arithmetic |

## §2 Methodology

| Location | Value | Source locator | Verdict |
|---|---|---|---|
| §2.1, §2.2, §2.4, §2.8, §4.4 | 283 footnotes; 74 archive files | LITERATURE-EXTRACTION-PLAN.md:8 (banner: "reference an archive external to this repo and have not been re-verified") | historical-record, now labelled in §2.2 |
| §2.1 | Planning Sept 2024-Oct 2025; execution Oct 2025, 4 weeks | LITERATURE-EXTRACTION-PLAN.md | historical-record |
| §2.2 | 16 of 22 URLs (73%) | LITERATURE-EXTRACTION-PLAN.md:30 | historical-record; "100% hypothesis-critical" relabelled withdrawn (Table 1) |
| §2.2 | 273 catalogued / 271 tiered (was 229/227) | Counter 2 | corrected, derived-gated |
| §2.2, Fig 1, App E | 400 records (354 OpenAlex, 46 dblp), 5 duplicates, 395 screened, 355 excluded, 40 included | methods/PRISMA-RETRO-RUN-2026-07-13.md:29-47; reconciliation.json counts | verified-at-record |
| §2.2 | 19 full text, 7 abstract-only, 0 unretrievable | methods/fulltext-retrieval-2026-07-16.json `totals` | verified-at-record |
| §2.2 | Clarivate March-2023 Hindawi cull | Appendix E.3 rank 39; prisma-appraisal record | verified-at-record |
| §2.3 | Level A 22.5% (61/271) | Counter 2 | derived-gated |
| §2.3 | Level B 62.7% (170/271) (was 47.6%, 108/227) | Counter 2 | corrected, derived-gated |
| §2.3 | Level C 14.8% (40/271) (was 10.6%, 24/227, twice) | Counter 2 | corrected, derived-gated |
| §2.3 | 57 entries moved off A on 2026-08-19 | METHODOLOGY.md §8.1a ("the 2026-08-19 audit moved 57 entries down and the share went from 41.9% to 17.0%") | verified-at-record |
| §2.3 | 97% metadata completeness | October-2025 self-assessment | historical-record, now labelled |
| §2.3 | 8.2× retired; 5.5× default, 9.0× tuned (Zeek, 10M rows) | sdw-lab-benchmarks NUMBER-VERIFICATION-2026-07-02.md:15-17 (8.2× "unsourced drift", ZSTD(22) 9.03×); zeek-flagship-rerun/results/RESULTS.md:76 (MergeTree LZ4 5.5×) | corrected: "vendor-derived 8.2×" became "an 8.2× ratio that traced to no reproducible measurement", codecs named, [21] cited |
| §2.3 App E | 14 refused, 8 predatory, 3 not peer-reviewed, 1 unreadable, 2 verification refusals | Appendix E.3 table rows | verified-at-record |
| §2.4 | Oct-2025 category tallies 18/12/15/18/12 with sub-counts | October-2025 catalogue | historical-record; first category's sub-counts sum to 20 not 18, now stated in the label |
| §2.4 | Paywalls 3, placeholders 3 | October-2025 record | historical-record, labelled |
| §2.5 | band thresholds 21/16/11; 5-25 range | methods/scoring-rubric.md | verified-at-record |
| §2.5 | "29 hypotheses" from the book | not enumerated in this repo (count_reconcile.py docstring) | removed |
| §2.5 | 3 gap-analysis hypotheses; 2 post-audit | §2.6 lists three; H-LOGCOMP-01, H-SOC-BASELINE-01 | arithmetic |
| §2.5 | "thirty-fold throughput spread"; "9× compression ratio" | Kajiura & Nakamura 22,972 / 723 = 31.8×; Zeek ZSTD(22) 9.03× | arithmetic, verified-at-record |
| §2.5 | GRADE four levels; 2026 tertiary study [47] | [42] Cochrane Handbook ch. 14; [47] Crossref 10.1007/s10664-025-10728-9 | verified-at-primary (bibliographic) |
| §2.7 | count gate surface count ("43", stale) | scripts/count_reconcile.py now 79 surfaces | removed the number ("gates every surface that states a corpus or hypothesis count") |
| §2.7 | living-review cadence (monthly / quarterly) | commitment, not a measurement | n/a |
| §2.8 | 26 surviving, 27 after second screen | as above | verified-at-record |
| §2.8 | vendor bloc 68 + 14 = 82 of 273 (30.0%) | methods/source-taxonomy.json | derived-gated |
| §2.8 | "a fifth" of search results unusable | 14 of 40 = 35% unusable; 8 of 40 = 20% predatory | corrected to "more than a third ... and a fifth sit in predatory or compromised venues" |
| §2.8 | 27 studies resolve to 24 independent author groups; CATRACA three studies | MASTER-BIBLIOGRAPHY.md:4713 | verified-at-record |
| §2.8 | IJACSA removed from DOAJ in 2017 | reference [30] note; prisma-appraisal record | *2026-11-22: record says unverified (the appraisal record took the 2017 date from a search summary it could not re-verify); the DOAJ API returned 0 results for ISSNs 2158-107X and 2156-5570 on 2026-11-22, so the text now says "not listed in DOAJ" and "ESCI rather than SCIE"* |
| §2.8 | 24 peer-reviewed entries unreachable by the conjunctive query | reconciliation.json `corpus_academic_indexable: 24` | verified-at-record |
| §2.8 | 3 analyst sources (Gartner, IDC, Forrester) | October-2025 record | historical-record; IDC entry withdrawal now noted |
| §2.8 | single-screener misses 13%, dual ~3% [39] | Gartlehner et al. 2020, J Clin Epidemiol 121:20-28, title "Single-reviewer abstract screening missed 13 percent of relevant studies" (Crossref) | verified-at-primary (title); 3% figure verified-at-record |
| §2.8 | second screen 355 → 344 confirmed, 11 flagged (3.1%); 5 then 6 adjudicated, 1 admitted | methods/second-screen-2026-07-16.json; second-screen-adjudication-2026-07-16/18.json; 11/355 = 3.10% | verified-at-record, arithmetic |
| §2.9 | 395 records, ten batches | methods/prisma-results/screen-batch-0..9.json | verified-at-record |

## §3 Findings

| Location | Value | Source locator | Verdict |
|---|---|---|---|
| §3.1 | 273 / 271 / 2 stubs; A 22.5% (61), B 62.7% (170), C 14.8% (40) | Counter 2 | derived-gated (date stamp corrected to 2026-11-17: 273 was reached 2026-11-08, so "recounted 2026-11-07" was wrong) |
| §3.1 | taxonomy 75 / 68 / 38 / 26 / 18 / 17 / 14 / 9 / 2 each, with shares | methods/source-taxonomy.json | derived-gated (75, 82 bloc gated; the rest match the JSON) |
| §3.1 | peer-reviewed 24/203 (11.8%) → 50/229 (21.8%) → 75/273 (27.5%) | 24/203 = 11.82%; 50/229 = 21.83%; 75/273 = 27.47% | arithmetic, verified-at-record |
| §3.2.1 | Dremio 29% Iceberg vs 23% Delta; n=500; Nov 28, 2023 | https://www.dremio.com/press-releases/state-of-the-data-lakehouse-2024-... ("29% adopting an open table format in the next three years plan to choose Iceberg, compared to 23% for Delta Lake") | verified-at-primary |
| §3.2.1, §3.7 | 407 contributors (2026-07-09) | GitHub apache/iceberg, dated count | verified-at-record (dated; not re-counted) |
| §3.2.1 | Databricks Iceberg support Public Preview 2025-06-12 | MASTER-BIBLIOGRAPHY.md H-ARCH-01 vendor-support entry | verified-at-record |
| §3.2.1 | withdrawn "76%" | named as withdrawn | n/a |
| §3.2.2, §3.5, §3.7 | Cloudflare 600 → 60 bytes per row (~10×) | https://blog.cloudflare.com/log-analytics-using-clickhouse/ ("Each Elasticsearch document which used 600 bytes, came down to 60 bytes per row in ClickHouse") | verified-at-primary |
| §3.2.2, §3.5, §3.7, Table 4 | 12-19× less storage than Elasticsearch; 9-12× with `_source` disabled | https://clickhouse.com/blog/clickhouse_vs_elasticsearch_the_billion_row_matchup ("12 to 19 times less storage space"; "9 to 12 times less storage space") | verified-at-primary |
| §3.2.2 | 0.010 s vs 0.166 s; 65.4 vs 188.1 MiB (~2.9×) | security-data-that-works docker/README.md:228 (2026-06-07 run) | verified-at-primary |
| §3.2.2 (added) | canonical re-run ~17×, 69.2 vs 188.1 MiB (~2.7×) | docker/MOAR-EVIDENCE-RUN-2026-06-15.md:62-75 (188.10 / 69.21 = 2.72) | verified-at-primary |
| §3.5, §3.6, §4.1-§4.3, §5 | "~2.9× IPv4-vs-String storage savings" (six places) | both runs | corrected to "~2.7-2.9×" |
| §3.2.3, §3.5, §3.6, §3.7, §4.2, §5 | Samza: hundreds of TB of state per application; millions of requests/s from local state | Noghabi et al., PVLDB 10(12) PDF lines "sizes (hundreds of TB) per application" and "When using local state we perform millions of requests/s" | verified-at-primary |
| §3.2.3 | Andreoni Lopez >95% accuracy, >85% under drift | fulltext-retrieval / prisma-appraisal records | verified-at-record |
| §3.2.3 | Loganathan >2.5 million events/s | same records | verified-at-record |
| §3.2.3 | Saputra 650,000 msg/s, 172 MB/s | same records | verified-at-record |
| §3.3.2 | S3 $0.023 / $0.0125 / $0.004 / $0.0036 / $0.00099; 45.7% / 82.6% / 84.3% / 95.7% | MASTER-BIBLIOGRAPHY.md:668 (verbatim list prices fetched 2026-07-09); arithmetic re-done: 45.65, 82.61, 84.35, 95.70 | verified-at-record, arithmetic; live re-check failed (pricing table is script-rendered), stays dated 2026-07-09 |
| §3.3.2 | hot <100 ms, warm <1 s; cold 12-48 h retrieval | https://docs.aws.amazon.com/AmazonS3/latest/userguide/restoring-objects-retrieval-options.html (Deep Archive: standard within 12 h, bulk within 48 h) | verified-at-primary for 12-48 h; tier corrected from "S3 Glacier" to "S3 Glacier Deep Archive" (Flexible Retrieval is 3-5 h / 5-12 h) |
| §3.3.2 | compliance retention 1-7 years; ~30 days query concentration | none named | unverifiable-no-primary; *2026-11-22: the illustrative label covered only the 30-day clause, not the stated retention mandate, which is now replaced by OMB M-21-31 [15] plus a labelled practitioner estimate* |
| §3.3.3 | 99.9% = 8.76 hours/year | 0.001 × 8,760 h | arithmetic |
| §3.4.1 | 6-12 months proficiency | practitioner estimate | author-modelled, labelled |
| §3.4.1 | 20-30% salary premium; 15-20% on-call | none | relabelled as author-modelled (§3.4.3) |
| §3.4.2 | 20% / 50% / 75% / 90% productivity curve | none (Gartner withdrawn) | author-modelled, labelled illustrative |
| §3.4.3 | 2-4, 3-4, 6-9, 9-12 months; $15K-$50K; 200-400 hours; $150K; 20-30%; 12-18 months | author's planning model, labelled at the head of §3.4.3 | author-modelled |
| §3.5 | Kajiura & Nakamura 22,972 / 22,736 / 19,869 / 8,413 / 723 sessions/s; F1 0.964-0.972 | fulltext-retrieval record ("throughputs 22,972/22,736/19,869/8,413"); prisma-appraisal (RF 0.972, DT 0.967, NB 0.964) | verified-at-record |
| §3.5 | Abbasi 4,450 events/s, 12 ms, 40 MB, 93-98%, 95% to 3,500, degrades past 2,500, 96.2 vs 96.8, p=0.318, p<0.001, d>0.8 | prisma-appraisal-2026-07-13.json (verbatim abstract quotes) | verified-at-record |
| §3.5 | Gentz MsgPack 0.68 ms, JSON 6.47 ms, Protobuf 47.02 ms (Python); C++ all < 1 ms | fulltext-retrieval record (Table I: 0.6806 / 6.4709 / 47.0197; C++ 0.795 / 0.473 / 0.185) | verified-at-record |
| §3.5 | "two orders of magnitude" | 47.02 / 0.68 = 69× | corrected to "a nearly seventyfold spread" |
| §3.5 | Chalaemwongwan 79% / 70%; 45% / 80% / 98%; 3M+ records | prisma-appraisal and fulltext records; PRISMA-RETRO-RUN:136 | verified-at-record |
| §3.6 | M-21-31: 12 months active + 18 months cold | M-21-31 PDF (Aug. 27, 2021), retention table "12 Months Active Storage / 18 Months Cold Data Storage"; AA23-193A quotes it (https://www.cisa.gov/news-events/cybersecurity-advisories/aa23-193a) | verified-at-primary |
| §3.6, §4.2 | "4× capacity provisioning" | none | removed ("well above steady-state capacity" / "heavy over-provisioning") |
| §3.6, §4.2 | 10-20 vs 3-5 pivots; 30-60 s | practitioner estimate | author-modelled, labelled |
| §3.6 | CERN ~1 TB/day, goal 5 TB/day | fulltext-retrieval record | verified-at-record |
| §3.7, Table 2, Fig 4 | all nine scores and splits | manuscript §3.7, methods/RESCORE-2026-07-13.md | verified-at-record as the 2026-07-13 computation; see U2-notes staged item 1 (tier labels have since moved) |
| §3.7 | LogLite up to 67.8% ratio improvement, up to 2.7× speed | PVLDB 18(11) PDF ("average improvement of up to 67.8% in compression ratio and up to 2.7× in compression speed") | verified-at-primary |
| §3.7 | PBC ~2× ratio | arXiv 2311.13947 ("compression ratio twice as high as the state-of-the-art") | verified-at-primary |
| §3.7 | Pebbles ~8× transfer, ~27× throughput | par.nsf.gov PDF ("up to a ∼8× reduction ... ∼27× improvement in throughput") | verified-at-primary |
| §3.7 | Blitzcrank 85% memory, 19% throughput cost | MASTER-BIBLIOGRAPHY entry, verbatim 2026-07-10 | verified-at-record |
| §3.7 | Yang 27% / 49% composition | MASTER-BIBLIOGRAPHY.md:4556 | verified-at-record |
| §3.8 | 50-200 TB mid-market | framing of a gap, not a finding | n/a |
| §3.8 | engine reading: "DuckDB leads gated small-batch, StarRocks leads high-cardinality distinct" | analysis-bundles/hypothesis-confidence-matrix.md:640-645 (1M table: distinct `src_ip` StarRocks 97.7 ms vs DuckDB 139.7, latency-only, ClickHouse approximate) and :629-637 (100M: ClickHouse 10.5 ms full-scan count vs DuckDB 12.4); archive/analysis-bundles/performance-benchmarks-table.md:158-166 (same 1M table and reading) | verified-at-record (recovery pass 2026-11-17; the first-pass "not-in-source" verdict searched only security-data-that-works, which does not hold the per-workload table). §3.8 now carries both the DuckDB gated sweep and the StarRocks distinct lead, plus the 100M ClickHouse count crossover |
| §3.8 (replacement) | concurrency 1→16 clients: DuckDB 1.52×, servers 3.7-5.4× | docker/MOAR-EVIDENCE-RUN-2026-06-15.md:77-89 (ClickHouse 3.71×, Trino 4.00×, StarRocks 5.35×) | verified-at-primary |
| §3.8, §4.4 | "~7.0×" SIEM index footprint | docker/README.md:136 and :221 (1.6 MB Parquet vs 11.5 MB OpenSearch at 200,000 events; 7.19×; "~7×") | corrected to "~7×" with the two sizes; run record not located beyond README prose; *2026-11-22: "measured" dropped and the text now says the figure is from the stack's documentation with no captured run record* |
| §3.8 | Ryzen 5800H, WSL2, single host | docker/README.md:228 | verified-at-primary |

## §4 Discussion and §5 Conclusion

| Location | Value | Source locator | Verdict |
|---|---|---|---|
| §4.1 | 5-10% streaming / 90-95% batch split, cited to [19] Uber "and Netflix" | https://current.confluent.io/... session page gives no split (only "10s of thousands of queries/sec", "several million writes/sec"); [19] is not a Netflix source | relabelled as an illustrative practitioner estimate; Netflix attribution removed |
| §4.1 | $25K-$50K training; 30-50% managed premium | author-modelled (§3.4.3) | author-modelled, labelled |
| §4.2 | three nines vs four nines; 3-6 month analytics retention | framing | unverifiable-no-primary (general framing; staged) |
| §4.3 | nine hypotheses scored | §3.7 | derived-gated |
| §5 | 271 tiered (was 228) | Counter 2 | corrected, derived-gated |

## Tables

| Location | Value | Source locator | Verdict |
|---|---|---|---|
| Table 1 | 273 catalogued, 271 tiered | Counter 2 | derived-gated; date stamp corrected to 2026-11-17 |
| Table 1 | peer-reviewed 27.5% (75/273), was 11.8% | taxonomy JSON | derived-gated |
| Table 1 | Level A 22.5% (61/271), target ">70%" / "Below target" | Counter 2; METHODOLOGY §8.1a (target retired) | corrected: target column now "retired 2026-08-19", status "Measured, not targeted"; gate pattern updated |
| Table 1 | 3 regions; 5 organization types | §3.1 diversity list | verified-at-record (understated since the search arm; left) |
| Table 2 | scores, splits, pre-audit values | methods/RESCORE-2026-07-13.md | verified-at-record (see staged rescore) |
| Table 3 | 1.0× baseline | definitional | n/a |
| Table 4 | 12-19× (9-12×); 6M req/s; trillions/day | as above | verified-at-primary |
| Table 5 | 4 engines, one Iceberg/OCSF table (2026-06-07) | docker/README.md, workload_matrix.py:4-8 | verified-at-primary |

## Figure captions and alt text

| Location | Value | Source locator | Verdict |
|---|---|---|---|
| Fig 1 caption and alt | 400 / 354 / 46 / 5 (1 DOI, 4 title) / 395 / 355 / 137 E2 / 103 E1 / 36 date floor / 40 / 14 / 26 / 27 | PRISMA-RETRO-RUN:29-47; reconciliation.json; appraisal record | verified-at-record |
| Fig 1 caption and alt | 203 curated, 179 grey (67/35/18/17/14/14/8 + 6), 24 academic; 228 tiered | figure1_prisma_flowchart.tex right arm (sums: 179 + 24 = 203; 201 + 27 = 228) | verified-at-record as the 2026-07-16 edition; bridge to 273/271 added (43 entries added since, = sum of methods/added-2026-07-23 ... -2026-11-08 JSON entries: 1+9+2+8+2+9+9+1+2) and gated |
| Fig 1 .tex | convergence box said "+ 26 via the database arm" against a total of 228 = 201 + 27 | tex left arm says 27 | corrected to 27; PDF recompiled |
| Fig 2 caption, alt, shows | 22.5 / 62.7 / 14.8 of 271 | Counter 2 | derived-gated; the "shows" line (20.8 / 64.9 / 14.3 of 259) corrected and gated |
| Fig 2 shows | 11 Level-A of 26 search-arm admissions | Fig 1 tex (11 A, 12 B, 3 C) | verified-at-record |
| Fig 3 caption, alt, shows | taxonomy counts and shares; 82 of 273; 75 of 273 | taxonomy JSON | derived-gated |
| Fig 4 caption, alt, shows | nine scores, thresholds 21/16/11 | §3.7; rubric | verified-at-record |
| Figures note | "Figure 2 carries the live evidence tally (2026-07-09)" | Fig 2 PNG shows 61/170/40 of 271 | corrected to "(271 tiered)" |

## Second-opinion additions (2026-11-22)

| Location | Value | Source locator | Verdict |
|---|---|---|---|
| §3.2.2 | "Azure Event Hubs ... trillions of events daily" [12] | https://azure.microsoft.com/en-us/blog/processing-trillions-of-events-per-day-with-apache-kafka-on-azure/ ("Siphon" about 5 times, "HDInsight" about 6, "Event Hubs" 0; "ingest and process 3 trillion events per day") | corrected: the post describes Siphon, Microsoft's internal ingestion service on Apache Kafka on Azure HDInsight |
| Reference [13] | page date Jul. 14, 2026 | MASTER-BIBLIOGRAPHY.md Netflix petabyte-scale logging entry ("ClickHouse blog dated Oct 23, 2025") | corrected to Oct. 23, 2025, with the 2026 re-dating noted |
| §3.5 | Gentz et al. C++ "ordering inverts" | MASTER-BIBLIOGRAPHY.md Gentz entry (C++: Protobuf 0.795 ms, MsgPack 0.473 ms, JSON 0.185 ms) | corrected: Protobuf is slowest in both runtimes and only JSON moves, to fastest |
| §3.6 | training break-even "6 months" | $150K/yr is $12.5K a month against $25K per engineer | arithmetic corrected: about two months for one engineer, six for three |

The remaining record-tier rows (Loganathan, Saputra, Abbasi, CERN) were not re-read at a primary in either pass and are flagged for a primary re-read before submission.
