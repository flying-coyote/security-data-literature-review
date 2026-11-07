# Chapter remap: retired outline numbering → current seven-chapter book (2026-11-07)

The bibliography's Relevance and Citations fields were written against the book's earlier outlines, and they still said "Chapter 7 (Ingestion)", "Chapter 8 (Storage Formats)", "Chapter 9 (Query Engines)" and so on months after the book became seven chapters in two parts (`~/modern-data-stack-for-cybersecurity-book`, `part-1-so-what/` ch01–ch02, `part-2-what-now/` ch03–ch07; the old navigation chapters became appendices H–L in this repo's `book-appendices/`). Any per-chapter measure, including the claim-to-evidence matrix, needs these labels in the current numbering first.

## Why this is keyed on topic, not on the archived renumber table

The book repo carries a renumber table (`archive/docs/planning/RESTRUCTURE-EXECUTION-2026-06.md`), but it cannot be applied mechanically, for two reasons. The bibliography's labels are not all from the 11-chapter layout that table describes: they include "Chapter 13" and "Chapter 17", which never existed in an 11-chapter book, and "Chapter 7 (Ingestion)", where the 11-chapter layout's ch07 was decision-framework material, so the numbers behave as topical tags from older outlines. And the table targets an intermediate six-chapter Part 2 (Decision Framework / Three Journeys / From Decision to Deployment) that was itself restructured again into the current trustworthy / well-connected / performant / variants / modularity shape. So each label was mapped by its topic text against the current chapter headings, with the old number used only when the label carries no topic.

## Current chapter homes used

| Current home | Heading |
|---|---|
| ch01 | You're doing data engineering *without* the tools for it (cost and volume as background) |
| ch02 §2.2 / §2.3 | MOAR explained: the components (collection, pipeline, storage, engine) / the economics |
| ch03 | Trustworthy security data (source, flow, content; silent wrong answers) |
| ch04 §4.1 / §4.2 / §4.3–4.5 | D3FEND / OCSF / Sigma, verification and source coverage |
| ch05 §5.1 / §5.2 / §5.3 | Table format is read-neutral / Arrow as the wire / match the engine to the workload |
| ch06 | MOAR variants (sovereignty, cloud-commitment, multi-engine, mid-size, keep-the-SIEM) |
| ch07 | Modularity: incremental, reversible migration, one source and workload at a time |
| Appendices C, D, H, I, J, K, L, M | Reference architectures, glossary and DE foundations, OCSF strategy, query-engine selection, resources and community, journey walkthroughs, ops detail, detection coverage |

## Applied map (181 label mentions on 168 lines)

Each rewritten mention keeps its old label inline as `[was: Chapter N]`, so the join to the old text stays auditable, and a home marked AMBIGUOUS is a best fit a reader should check rather than trust. A rule id with no topic match (FALLBACK) was mapped by its old number.

| Old label | Rule | Current home | Mentions | Rationale |
|---|---|---|---|---|
| Chapter 1 | R05 | ch02 §2.3 (economics) | 17 | cost and storage economics are ch02 §2.3; ch01 keeps cost only as background |
| Chapter 1 | R08 | ch05 §5.1 (table format) | 1 | table formats and catalogs are ch05 §5.1 |
| Chapter 2 | R06 | ch01 (background) + ch02 §2.3 | 2 | volume trends are ch01 background feeding the ch02 economics |
| Chapter 2 | R08 | ch05 §5.1 (table format) | 3 | table formats and catalogs are ch05 §5.1 |
| Chapter 2 | R14 | ch02 §2.2 + Appendix D | 2 | DE foundations moved to Appendix D; components in ch02 §2.2 |
| Chapter 3 | R01 | ch04 §4.1 (D3FEND) | 1 | D3FEND/grounding chain is ch04 §4.1 |
| Chapter 3 | R16 | ch06 §6.3 (multi-engine variant, named deployments) [AMBIGUOUS] | 2 | named production deployments best fit the variants chapter; old-outline intent unclear |
| Chapter 4 | R09 | ch07 §7.2-7.3 + Appendix K | 12 | incremental migration and sequencing are ch07; the journey walkthroughs are Appendix K |
| Chapter 4 | R13a | ch02 §2.2 (components: collection and pipeline) | 1 | ingestion/streaming is a component in ch02 §2.2; no current chapter is ingestion-only |
| Chapter 6 | R08 | ch05 §5.1 (table format) | 1 | table formats and catalogs are ch05 §5.1 |
| Chapter 6 | R10 | ch06 §6.5 (keep the SIEM) | 1 | the keep-the-SIEM case is ch06 §6.5 |
| Chapter 6 | R12a | ch06 (variants) + Appendix C | 3 | reference designs map to the variants chapter and Appendix C (reference architectures) |
| Chapter 6 | R13a | ch02 §2.2 (components: collection and pipeline) | 1 | ingestion/streaming is a component in ch02 §2.2; no current chapter is ingestion-only |
| Chapter 7 | R05 | ch02 §2.3 (economics) | 4 | cost and storage economics are ch02 §2.3; ch01 keeps cost only as background |
| Chapter 7 | R09 | ch07 §7.2-7.3 + Appendix K | 1 | incremental migration and sequencing are ch07; the journey walkthroughs are Appendix K |
| Chapter 7 | R13 | ch02 §2.2 (components: collection and pipeline) | 10 | ingestion/streaming is a component in ch02 §2.2; no current chapter is ingestion-only |
| Chapter 7 | R13a | ch02 §2.2 (components: collection and pipeline) | 24 | ingestion/streaming is a component in ch02 §2.2; no current chapter is ingestion-only |
| Chapter 8 | FALLBACK | ch05 §5.1 (table format) | 2 | no topic keyword; mapped by old number to the nearest current home |
| Ch 8 | FALLBACK | ch05 §5.1 (table format) | 1 | no topic keyword; mapped by old number to the nearest current home |
| Chapter 8 | R01 | ch04 §4.1 (D3FEND) | 1 | D3FEND/grounding chain is ch04 §4.1 |
| Chapter 8 | R02 | ch04 §4.2 (OCSF) + Appendix H | 7 | OCSF/schema material is ch04 §4.2; full OCSF strategy is Appendix H (old ch08) |
| Chapter 8 | R05 | ch02 §2.3 (economics) | 2 | cost and storage economics are ch02 §2.3; ch01 keeps cost only as background |
| Chapter 8 | R07 | ch05 §5.3 + Appendix I | 2 | engine selection is ch05 §5.3/5.3a; the full query-engine guide is Appendix I (old ch09) |
| Chapter 8/9 | R07 | ch05 §5.3 + Appendix I | 1 | engine selection is ch05 §5.3/5.3a; the full query-engine guide is Appendix I (old ch09) |
| Chapter 8 | R08 | ch05 §5.1 (table format) | 23 | table formats and catalogs are ch05 §5.1 |
| Chapter 9 | R03 | ch04 §4.3-4.5 (Sigma, coverage) + Appendix M | 2 | detection logic and coverage live in ch04 §4.3-4.5 and Appendix M |
| Chapter 9 | R07 | ch05 §5.3 + Appendix I | 31 | engine selection is ch05 §5.3/5.3a; the full query-engine guide is Appendix I (old ch09) |
| Chapter 9 | R08 | ch05 §5.1 (table format) | 12 | table formats and catalogs are ch05 §5.1 |
| Chapter 10 | R04 | ch05 §5.2 (Arrow wire) | 2 | Arrow Flight connectivity is ch05 §5.2 |
| Chapter 10 | R05 | ch02 §2.3 (economics) | 1 | cost and storage economics are ch02 §2.3; ch01 keeps cost only as background |
| Chapter 10 | R07 | ch05 §5.3 + Appendix I | 1 | engine selection is ch05 §5.3/5.3a; the full query-engine guide is Appendix I (old ch09) |
| Chapter 11 | R11 | ch06 §6.1 (sovereignty) + Appendix J [AMBIGUOUS] | 2 | no chapter owns governance; nearest is the sovereignty variant |
| Chapter 12 | R08 | ch05 §5.1 (table format) | 1 | table formats and catalogs are ch05 §5.1 |
| Chapter 12 | R15 | no current chapter home [AMBIGUOUS] | 1 | agent-native and futures material has no chapter in the 7-chapter book |
| Chapter 13 | R03 | ch04 §4.3-4.5 (Sigma, coverage) + Appendix M | 1 | detection logic and coverage live in ch04 §4.3-4.5 and Appendix M |
| Chapter 13 | R15 | no current chapter home [AMBIGUOUS] | 1 | agent-native and futures material has no chapter in the 7-chapter book |
| Chapter 17 | R15 | no current chapter home [AMBIGUOUS] | 1 | agent-native and futures material has no chapter in the 7-chapter book |

## Left as written

- The two entries added 2026-11-07 (Petrescu, ch03; Madani, ch04) were already written in the current numbering; their labels were normalised to `ch03` / `ch04`.
- The Apache Ossie entry's "Ch2 §2.2" pointer (2026-07-23) is already current.
- The "Chapter Coverage" summary block under Book Integration Readiness is a historical snapshot; it now carries a note that its numbers are the retired outline's, and its lines were not rewritten.

## Flagged for a human read

- Governance and compliance (old Chapter 11) have no chapter in the seven-chapter book; mapped to the sovereignty variant (ch06 §6.1) plus Appendix J.
- Agent-native architecture and future-predictions labels (old Chapters 12, 13, 17) have no current chapter home.
- The CERN and INFN-CNAF production-deployment entries said "Book Chapter 3"; whether that meant the trustworthy chapter or an older outline's chapter is unclear, so they are mapped to ch06 §6.3 (named deployments of the multi-engine variant).
- "Book Ch 8" on the query-engine-selection entry, "Chapter 8 vendor support" and "Chapter 8 performance benchmarks" carry no topic and fell back to ch05 §5.1 by number; one line ("Chapter 8 operational maintenance" on a Spark-plus-Iceberg entry) was hand-corrected from the engine section to ch05 §5.1 after the run.

Derived by a one-off script over `MASTER-BIBLIOGRAPHY.md` on 2026-11-07; rerunning it is idempotent because rewritten lines carry `[was: ...]` and are skipped.
