---
title: PRISMA Search Protocol
date: 2026-07-13
status: pre-specified protocol, executed 2026-07-13
script: scripts/prisma_search.py
outputs: methods/prisma-results/
---

# PRISMA Search Protocol (2026-07-13)

This is the search protocol for the systematic-search arm of the security data architecture literature review. It is written so that a reviewer can re-run it: every database, every query string, the date window, the eligibility criteria, the screening procedure, and the deduplication rule are specified here, and the machine outputs the run produced are on disk under `methods/prisma-results/`. Where the protocol has limits — and it has several that matter — they are stated at the end rather than left for a reviewer to discover.

One thing belongs up front, because it changes how the rest of this document should be read. The corpus this search was run against was built by curation between 2025 and 2026, and the search was executed afterward, on 2026-07-13, to test that corpus's coverage. The protocol below is pre-specified in the sense that the criteria and queries were fixed before any record was screened and no criterion was revised after seeing the results, but it is not a prospective protocol registered before the review began. The companion document, `PRISMA-RETRO-RUN-2026-07-13.md`, gives the honest account of what that means and what the search found.

## 1. Research questions the search serves

The search is scoped to the four research questions the review already carries (`PUBLICATION-MANUSCRIPT.md` §1.3):

- RQ1: what architectural patterns are validated in production security data platforms — which table formats, which query engines, and what streaming-versus-batch patterns for security telemetry ingestion, at what evidence level;
- RQ2: what are the quantified operational costs of security data architectures — total cost of ownership for streaming versus batch, staffing multipliers, implementation timelines, and the conditions under which tiered storage pays;
- RQ3: what performance benchmarks exist for security-specific workloads — query latency and throughput at TB–PB scale, achievable ingestion rates for streaming security telemetry, and validated storage-efficiency gains;
- RQ4: what implementation patterns are validated for security operations — change management out of a SIEM, skills gaps and staffing models, deployment patterns under compliance constraints, and operational reliability.

Each question asks about the data architecture underneath security work, which is why the eligibility criteria in §4 exclude detection-model papers that merely run on top of a streaming platform. That exclusion is the whole discriminating move of this search, so it is specified strictly and applied strictly.

## 2. Databases searched, and the ones that were not

Two databases were searched, both free and open:

- **OpenAlex** (`https://api.openalex.org/works`), a full-text-and-abstract index with cursor paging;
- **dblp** (`https://dblp.org/search/publ/api`), the computer-science bibliography, which searches titles only.

No subscription database was searched. There is no Scopus, no Web of Science, no IEEE Xplore, and no ACM Digital Library in this protocol, because the review is run without institutional library access and the protocol will not claim coverage it did not buy. That is a real limitation on recall and it is disclosed rather than softened; §7 says what it plausibly costs.

arXiv preprints enter the search through OpenAlex, which indexes them, rather than through a separate call to the arXiv Atom API. Nine of the 395 identified records carry arXiv as their host venue (five of them under a `10.48550/arXiv` DOI), twenty are typed `preprint` by OpenAlex across all servers, and two of the forty included studies are arXiv preprints. A reviewer who wants to argue that a dedicated arXiv query would have found more is arguing about recall at the margin, not about whether preprints were eligible — they were, under criterion I1.

## 3. Exact query strings and date window

**Date window: 2018-01-01 onward.** The floor is 2018 because the table-format and lakehouse literature the review is about is a post-2018 literature; earlier work enters the corpus by citation, not by search.

**OpenAlex.** One strict boolean filter over title and abstract, cursor-paged at 200 records per page, with the date floor pushed into the query:

```
title_and_abstract.search:(cybersecurity OR "security analytics" OR SIEM OR "intrusion detection"
  OR "threat detection" OR "security operations" OR "security monitoring" OR "log analysis")
AND (lakehouse OR "data lake" OR "Apache Iceberg" OR "Delta Lake" OR "query engine" OR Trino
  OR ClickHouse OR DuckDB OR "stream processing" OR "Apache Kafka" OR "Apache Flink"
  OR "columnar storage" OR Parquet OR "data warehouse"),
from_publication_date:2018-01-01
```

The query is conjunctive by construction: a record must carry a security term *and* a storage-or-engine term in its title or abstract. That conjunction is what makes the search targeted, and it is also the source of one of its known blind spots (§7).

**dblp.** Eight title-level queries, each issued with at least 3.5 seconds between calls to respect the service, with retry-and-backoff on transient HTTP 5xx:

1. `security data lake`
2. `SIEM data lake`
3. `security analytics lakehouse`
4. `security log stream processing`
5. `intrusion detection stream processing`
6. `security data warehouse`
7. `threat detection Kafka`
8. `security telemetry pipeline`

dblp's publication API searches titles with AND semantics and takes no date parameter, so the 2018 floor **cannot** be pushed into the dblp query. It is enforced at screening instead, as criterion I1. This asymmetry — date filter applied at the database for OpenAlex, at screening for dblp — is deliberate and is disclosed because it changes what the PRISMA identified-count means: pre-2018 dblp records are identified and then excluded on I1, rather than never being identified at all.

**Script.** `scripts/prisma_search.py`, standard library only (urllib, json, time, re, argparse, pathlib), no third-party imports and no XML parsing. It writes `methods/prisma-results/records.json` (the unique record set, each record tagged with the source or sources that returned it) and `methods/prisma-results/search-log.json` (run timestamp, the exact query strings above, per-database and per-query counts, the failed-query list, and the deduplication breakdown). A reviewer can re-run the script and diff the log.

## 4. Eligibility criteria (pre-specified, applied as written)

INCLUDE a record only if ALL hold:

- **I1.** Published 2018-01-01 or later (peer-reviewed venue, or a preprint).
- **I2.** Its subject is the DATA ARCHITECTURE handling security telemetry — table formats, lakehouse/data-lake design, columnar storage, query engines, stream-processing platforms, or the storage/query/ingest pipeline itself — applied to security data (SIEM, detection, log analysis, security analytics, security operations).
- **I3.** It reports EVIDENCE about that architecture: a measurement, a benchmark, a production deployment, or a substantive design evaluation.

EXCLUDE a record if ANY hold:

- **E1.** It is a machine-learning or deep-learning INTRUSION-DETECTION MODEL paper that merely runs on top of a big-data or streaming platform without evaluating the data architecture itself. (This is the dominant false positive in the result set — a paper whose contribution is a classifier's accuracy on NSL-KDD/CICIDS, mentioning Kafka or Spark only as plumbing, is EXCLUDED. Be strict here.)
- **E2.** It is a data-engineering paper with no security application.
- **E3.** It is a survey with no architecture-level content of its own.
- **E4.** It is an abstract, poster, editorial, or under ~4 pages.
- **E5.** It is not in English.
- **E6.** It is a duplicate of a record already included.

For every record, the screening step returns the decision, the single governing criterion (e.g. "E1"), and a one-line reason quoting the specific thing in the title or abstract that decided it.

## 5. Screening procedure

Title-and-abstract screening was performed by an LLM (Claude) against the pre-specified criteria in §4, in ten batches covering the full unique record set, with every decision written to disk. There was no human second screener and no inter-rater reliability statistic, and the protocol does not pretend otherwise.

What makes the procedure auditable rather than a black box is that each decision is recorded as a row a reviewer can check: `methods/prisma-results/screen-batch-0.json` through `screen-batch-9.json` carry, for each of the 395 unique records, its OpenAlex or dblp identifier, its DOI, its title, its year, the include/exclude decision, the single governing criterion, and a one-line reason quoting the deciding phrase from the title or abstract. A reviewer who disagrees with a call can find it, read the reason, and overturn it against the same criteria the screener was given. A reviewer who wants to re-screen the whole set from scratch has the record set on disk to do it with.

Two constraints on screening are worth naming here rather than in the limitations section, because they are procedural rather than conceptual. 318 of the 395 unique records carry an abstract and 367 carry a DOI; dblp supplies no abstracts at all, so the 45 dblp-only records were screened on title, venue, and year, which is weaker evidence than an abstract and is flagged as such in the per-record reasons. Records screened on title alone that were nevertheless included are marked in the gap list with an instruction to read the full text before citing.

## 6. Deduplication rule

Deduplication runs at identification, before screening, in two passes:

1. **DOI**, exact string match after case normalization;
2. **normalized title**, lowercased with punctuation and parentheticals stripped.

A record surviving both passes is unique. Where a record was returned by both databases, its `sources` list in `records.json` carries both, so cross-database overlap is measurable from the file rather than asserted. Duplicates that survive this rule — a preprint and its published version under different DOIs and slightly different titles — are caught at screening under E6, and thirteen records were in fact excluded under E6 in this run, which is a reminder that DOI-and-title deduplication at identification catches the easy cases and not the hard ones.

## 7. Limitations this protocol carries

- **Subscription databases were not searched.** No Scopus, no Web of Science, no IEEE Xplore, no ACM Digital Library. OpenAlex indexes a great deal of what those hold, including DOI-registered IEEE and ACM work, but the coverage is not equivalent and the recall claim this protocol can support is correspondingly weaker.
- **The conjunctive query cannot reach single-half literature.** A record must carry both a security term and a storage/engine term. The database-systems papers that carry only the storage half — Delta Lake, LHBench, FastLanes, DBSP and the rest — are unreachable by this query even though the review depends on them, and in this run 24 peer-reviewed corpus entries were missed for exactly that reason. This is a property of the search strategy, not a defect in the databases.
- **dblp searches titles only, with AND semantics and no date parameter.** Five of the eight dblp queries returned zero records, which is a genuine statement about title matches and not a failure; and the date floor had to be enforced at screening for dblp records.
- **Screening was single-screener and LLM-performed.** No second human screener, no kappa. The mitigation is full decision-level auditability (§5), not a claim of reliability.
- **45 records were screened without abstracts** (dblp-only), on title, venue, and year.
- **The protocol is retrospective.** It was specified and run after the corpus was built, to test that corpus, and it is reported as such. It is not a registered prospective protocol and the review does not claim to be one.
