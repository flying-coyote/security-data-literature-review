# Modern Data Architecture for Cybersecurity Operations: a living systematic literature review

This repository is an evidence-tiered review of the literature on running security operations on modern data architecture: open table formats such as Apache Iceberg, columnar query engines such as ClickHouse and DuckDB, stateful streaming, schema standards such as OCSF, and the cost, staffing and timeline questions that decide whether any of it works in a real security team. Security research tends to study detection algorithms and data engineering tends to study general analytics, so the infrastructure questions a security architect actually faces sit between two literatures, and this review reads both and grades each source it tiers. It is the evidence companion to the *Modular Open Architecture (MOAR) for Cybersecurity Data* handbook and to the essays at securitydataworks.com, and it is maintained as a living review, so new sources are added as they are verified, with a monthly review cadence ([scripts/SCHEDULING.md](scripts/SCHEDULING.md)), and the corpus and hypothesis counts on these pages are derived from the bibliography and manuscript by committed scripts rather than typed by hand.

**Version** 1.23.0 plus unreleased changes through 2026-11-22 (see [CHANGELOG.md](CHANGELOG.md)) · **Database search** current to 2026-07-13 (OpenAlex, dblp) · **Curation** monthly review cadence, most recent additions 2026-11-08 · **README reviewed** 2026-11-17

## What the review covers

The bibliography is organized by topic first (foundational architecture, security-specific data, implementation and organizational evidence, streaming and storage, performance benchmarks, emerging technologies, AI-native infrastructure, formats, catalogs, governance and cost) and then by intake batch, so each later section records when and why its sources arrived. Seventeen research questions frame it: RQ1 to RQ4 are stated in the manuscript's introduction ([PUBLICATION-MANUSCRIPT.md](PUBLICATION-MANUSCRIPT.md) §1), RQ7 to RQ10 in [METHODOLOGY.md](METHODOLOGY.md) §5.4, RQ11 to RQ14 in Gap 11 of [LITERATURE-HYPOTHESIS-GAP-ANALYSIS.md](LITERATURE-HYPOTHESIS-GAP-ANALYSIS.md), and RQ15 to RQ17 in its Gap 12, where two of the three are still unvalidated, and the isolation-first questions RQ7 to RQ10 are also open ([isolation-first-security-tracking.md](isolation-first-security-tracking.md)). RQ5 and RQ6 have no current definition in this repository; that gap is recorded for an owner ruling (noted 2026-11-22). The questions run from table-format adoption, total cost of ownership and staffing through query performance and streaming economics to isolation-first security architecture, detection-pipeline economics and the governance of AI agents in the SOC.

## How the review was built

[![Flow of the two routes into the corpus: 400 database records narrowed to 40, of which an appraisal gate refused 14 and admitted 26, plus one more admitted from a second screen of the exclusions, while the curation arm built most of the corpus by reading; both then pass through tiering before entering the bibliography.](docs/figures/review-method.png)](docs/figures/review-method.svg)

*Figure: how a source reaches the corpus. Numbers are from the July 2026 search run (`methods/PRISMA-RETRO-RUN-2026-07-13.md`) and its appraisal record (`methods/prisma-appraisal-2026-07-13.json`); live corpus counts are in "Corpus at a glance", derived by `scripts/count_reconcile.py`.*

Sources reach the corpus by two routes. The curation arm began in October 2025 from the footnotes of a practitioner manuscript and has grown since through monthly reading, reader corrections and the handbook's own citations, which is how most of the vendor engineering writing, conference talks and production case studies arrived. The database arm is a retrospective PRISMA 2020 search of OpenAlex and dblp run on 2026-07-13 ([methods/PRISMA-RETRO-RUN-2026-07-13.md](methods/PRISMA-RETRO-RUN-2026-07-13.md)): 400 records identified, 395 screened after duplicates, 40 included, and none of the 40 already in the corpus, which says the two arms cover nearly disjoint literatures. Each of the 40 then went through a full-text appraisal that refused 14, eight of them for predatory or compromised venues ([methods/prisma-appraisal-2026-07-13.json](methods/prisma-appraisal-2026-07-13.json)), and a second screen of the exclusions admitted one more on 2026-07-16.

Whichever route a source takes, it gets an Evidence Level under the rules below, and the numbers it is cited for are checked at the primary before they carry a claim, with the verdict logged in [RESEARCH-JOURNAL.md](RESEARCH-JOURNAL.md) and, per number, in [methods/verification-2026-11/](methods/verification-2026-11/README.md); a number that could not be read at its primary is labelled unverified in its entry. That rule exists because a 2026-06 claim-versus-source audit found the October 2025 corpus had been graded too generously and carried figures that were not in the sources they cited; those entries were removed or re-tiered, and the audit trail is in the CHANGELOG under versions 1.22.0 and 1.23.0.

## Corpus at a glance (quality metrics)

These lines are checked in CI on every push and, when this file is staged, by the pre-commit gate, using `scripts/count_reconcile.py`, which derives them from [MASTER-BIBLIOGRAPHY.md](MASTER-BIBLIOGRAPHY.md) and fails if any surface disagrees.

- **279 sources catalogued** (277 tiered + 2 documented stubs; 22.7% Evidence Level A, live 2026-11-23 — 63/277)
- **Evidence Level A: 22.7%** (63 of 277 tiered sources)
- Evidence Level B: 174 of 277 · Evidence Level C: 40 of 277 (across 279 `#### ` blocks incl. 2 documented stubs)

The Level-A share describes where the evidence in this field lives, and it is not a target. Much of what is known about running security data platforms at scale is in production writeups and practitioner talks rather than peer-reviewed papers, so an honest corpus sits mostly at Level B, and the earlier share targets were retired for that reason (METHODOLOGY §8.1a).

## How evidence is tiered

[![Evidence levels A to D: Level A is peer review and official standards only, a highlighted line marks that no production evidence sits above it, Level B is practice and production evidence, Level C is unmeasured vendor material kept with its bias flagged, and Level D is excluded.](docs/figures/evidence-tiers.png)](docs/figures/evidence-tiers.svg)

*Figure: the four evidence levels as METHODOLOGY.md section 3.1 defines them. The share of the corpus at each level changes as entries are added, so it stays in the text.*

METHODOLOGY §3.1 is the canonical definition, and the figure above shows what qualifies at each level; the table says how each level is used:

| Level | How it is used |
|-------|----------------|
| A | Primary evidence |
| B | Real evidence, not peer-reviewed |
| C | Kept with its bias flagged; never carries a hypothesis on its own |
| D | Excluded |

Authorship decides the vendor-channel cases: a practitioner writing in the first person on a vendor blog is Level B with a curation caveat, and a vendor-authored piece quoting a practitioner is Level C.

## What the review finds

Nine hypotheses are scored with the five-dimension instrument in [methods/scoring-rubric.md](methods/scoring-rubric.md), and only legs that survived primary-source verification, or have not yet been challenged, count (methods/scoring-rubric.md §1); the scores below are the 2026-07-13 rescore ([methods/RESCORE-2026-07-13.md](methods/RESCORE-2026-07-13.md)) as printed in §3.7 of the manuscript; they were computed before the 2026-08-19 tier audit, and a rescore of the evidence-quality dimension under the corrected tiers is pending.

**Hypothesis Validation Results** (9 assessed: 7 from the original extraction, 2 formulated after the 2026 audit):
- H-ARCH-01 (Iceberg as the de facto open table format): strongly validated, 23/25. Industry consensus, with all four legs surviving primary verification; the bare 76% adoption figure once quoted for it is unsourced and is not used.
- H3-PERFORMANCE-01 (ClickHouse for security analytics): high confidence, 19/25. Anchored on Cloudflare's production deployment at 6M requests per second; the sub-second query-share figure was withdrawn in the 2026-06 audit.
- H-LOGCOMP-01 (compression specialized to machine data): high confidence, 17/25. Three peer-reviewed anchors (LogLite, PBC, Pebbles), each verified verbatim at its primary.
- H-STREAM-01 (stateful streaming at security scale): moderate, 15/25. LinkedIn's Samza (VLDB 2017) and Azure production scale; two legs cap the source count, which demoted it from the earlier High Confidence.
- H-SOC-BASELINE-01 (production SOC alert base rates): moderate, 13/25. Yang et al., USENIX Security 2024, a single-source production measurement.
- H-COST-09 (tiered storage for long retention): preliminary, 9/25. The mechanism is documented and a first-party S3 tier-price derivation bounds the saving, but the original savings band was withdrawn.
- H-IMPL-01 (streaming total cost of ownership): preliminary, 5/25. Quantitative legs withdrawn in the 2026 audits; the claim is directional pending new sources.
- H-IMPL-02 (staffing scarcity for streaming): preliminary, 5/25. Quantitative legs withdrawn in the 2026 audits; directional pending new sources.
- H-IMPL-03 (timeline premium for security lakehouses): preliminary, 5/25. Quantitative legs withdrawn in the 2026 audits; directional pending new sources.

Four of the nine sit at or near the instrument's floor, which is the honest state of the cost, staffing and timeline evidence after the audits rather than a statement that those effects are absent; the gap analysis records what new sources would move them.

## Where to start

- **To read the findings**, start with [PUBLICATION-MANUSCRIPT.md](PUBLICATION-MANUSCRIPT.md): sections 3 and 4 carry the evidence and the discussion, and its embedded references and appendices are the current ones.
- **To check a claim**, find the source in [MASTER-BIBLIOGRAPHY.md](MASTER-BIBLIOGRAPHY.md), where each entry carries its Evidence Level, the numbers it is cited for and a validation status, then look up its verdict in [RESEARCH-JOURNAL.md](RESEARCH-JOURNAL.md).
- **To judge the method**, read [METHODOLOGY.md](METHODOLOGY.md) and the search, appraisal and rescore records in [methods/](methods/).
- **For the journal version**, the manuscript is being prepared for the Journal of Cybersecurity (Oxford), and [PUBLICATION-VENUE-RECOMMENDATIONS.md](PUBLICATION-VENUE-RECOMMENDATIONS.md) records why that venue was chosen.
- **For practitioner depth**, the handbook appendices in [book-appendices/](book-appendices/) cover the vendor landscape, cost models and walkthroughs at more length than the paper can.

## How to cite

[CITATION.cff](CITATION.cff) carries the citation metadata, and GitHub's "Cite this repository" box reads it. A Zenodo DOI is planned for the first curated release of the paper export, and the deposit itself is held by the owner ([docs/ZENODO-RELEASE-CHECKLIST.md](docs/ZENODO-RELEASE-CHECKLIST.md)); until then, cite the title and repository URL, and because this is a living review, name the commit or tag you read so a reader can see the same snapshot:

> Wiley, J. (2026). *Modern Data Architecture for Cybersecurity Operations: A Systematic Literature Review* [Data set]. Security Data Works. https://github.com/flying-coyote/security-data-literature-review (commit or tag).

## Reproducing the counts

Every gated count is derived, and these commands re-derive and check them from a clean checkout with Python 3.12 (`pip install pyyaml cffconvert` for the metadata check):

```bash
python3 scripts/count_reconcile.py                 # corpus and hypothesis counts on every gated surface
python3 scripts/derive_source_taxonomy.py --check  # source-type taxonomy behind Figure 3
python3 scripts/derive_vendor_rollups.py --check   # vendor-landscape evidence rollups
python3 scripts/validate_metadata.py               # CITATION.cff and .zenodo.json
python3 scripts/repoint_moved_paths.py --check     # no stale moved-file paths or broken relative links outside archive/, published/ and CHANGELOG.md
bash tools/build/build.sh                          # manuscript PDF (needs pandoc and a TeX engine)
```

CI runs the count, taxonomy, vendor-rollup, metadata and moved-path checks on every push and pull request ([.github/workflows/gates.yml](.github/workflows/gates.yml)); the secret scan reads only staged changes, so it does its work in the local hook rather than in CI. Locally, `scripts/pre-commit.sh` runs the secret scan, the staged-file count check, the moved-path check and a check that blocks new personal-communication attributions in the bibliography and book appendices before each commit; the git hook itself is not version-controlled, so install it once per clone:

```bash
printf '#!/usr/bin/env bash\nexec bash "$(git rev-parse --show-toplevel)/scripts/pre-commit.sh"\n' \
  > .git/hooks/pre-commit && chmod +x .git/hooks/pre-commit
```

A new surface that states a gated count needs one entry in the ALLOWLIST in `scripts/count_reconcile.py`, and rephrasing a gated line means updating its pattern there, because a pattern that no longer matches fails the run on purpose.

## Repository map

| Path | What it holds |
|------|---------------|
| [PUBLICATION-MANUSCRIPT.md](PUBLICATION-MANUSCRIPT.md) | The paper, with its embedded references and appendices |
| [MASTER-BIBLIOGRAPHY.md](MASTER-BIBLIOGRAPHY.md) | 279 catalogued sources (277 tiered), 22.7% Evidence Level A (live, 63/277), each with its tier, cited numbers and validation status |
| [METHODOLOGY.md](METHODOLOGY.md) | Search strategy, appraisal, the tier definitions (§3.1) and the hypothesis method |
| [RESEARCH-JOURNAL.md](RESEARCH-JOURNAL.md) | Per-claim verification verdicts |
| [CHANGELOG.md](CHANGELOG.md) | Every revision, for citation stability |
| [LITERATURE-HYPOTHESIS-GAP-ANALYSIS.md](LITERATURE-HYPOTHESIS-GAP-ANALYSIS.md) | Gap analysis that seeded the hypothesis roster (9 assessed today), with RQ11 to RQ17 and dated overturn notes |
| [LITERATURE-EXTRACTION-PLAN.md](LITERATURE-EXTRACTION-PLAN.md) | The original PRISMA-aligned extraction plan |
| [REFERENCES.md](REFERENCES.md), [APPENDICES.md](APPENDICES.md) | Earlier companion files, superseded by the manuscript's embedded sections and bannered as such |
| [FIGURES-AND-TABLES.md](FIGURES-AND-TABLES.md) | The working record behind the manuscript's figures and tables, not a source of numbers |
| [PROJECT-BRIEF.md](PROJECT-BRIEF.md) | Scope and context for contributors |
| [PUBLICATION-VENUE-RECOMMENDATIONS.md](PUBLICATION-VENUE-RECOMMENDATIONS.md) | Venue comparison for the journal submission |
| [monthly-update-tracker.md](monthly-update-tracker.md), [isolation-first-security-tracking.md](isolation-first-security-tracking.md) | Update cadence and the RQ7 to RQ10 tracking record |
| [methods/](methods/) | Search protocol, PRISMA runs, appraisal records, the scoring rubric and rescore, dated taxonomy inputs, and the 2026-11 per-number verification ledger |
| [scripts/](scripts/) | The counting, derivation, validation and health-check tools |
| [publication-graphics/](publication-graphics/) | Figure sources and rendered figures for the manuscript |
| [book-appendices/](book-appendices/), [analysis-bundles/](analysis-bundles/), [vendor-landscape/](vendor-landscape/) | Handbook appendices, three live analysis bundles, and the quarterly vendor database |
| [docs/](docs/) | Release checklist and reader figures |
| [tools/build/](tools/build/) | PDF build and the curated Zenodo export |
| [working/](working/README.md) | Dated audits, research-intake notes, scoring proposals and interview guides, indexed with their status |
| [archive/](archive/README.md), [published/](published/) | Superseded working snapshots and session logs, and the immutable 2025-10-22 release snapshots |
| [CITATION.cff](CITATION.cff), [.zenodo.json](.zenodo.json), [LICENSE](LICENSE), [LICENSE-CODE](LICENSE-CODE) | Citation and deposit metadata, and the two licenses |

## History

The review was first released on 2025-10-22 on the Security Data Commons Substack, which was retired on 2026-05-24; the essays now live at securitydataworks.com/writing, and the original release is kept unedited in [published/](published/). The record of what changed since, including the 2026-06 fabrication audit, the July verification sweeps, the database-search arm, the hypothesis rescore and the November handbook-footnote admissions, is in [CHANGELOG.md](CHANGELOG.md), with the 2026-08-19 tier audit that moved 57 entries off Level A recorded in METHODOLOGY §8.1a, and the working files behind those passes are indexed in [working/README.md](working/README.md).

## License

The review prose, bibliography, methods records, and data files are licensed [CC-BY-4.0](LICENSE). The code in `scripts/`, `tools/` (excluding fonts), and the Python and shell files in `publication-graphics/` is licensed [MIT](LICENSE-CODE), because Creative Commons licenses are not designed for software. The redistributed DM Sans and JetBrains Mono fonts in `tools/build/fonts/` remain under their own SIL Open Font License 1.1 (`tools/build/fonts/OFL-*.txt`).

**Maintained by** Jeremy Wiley, Security Data Works · **Repository** https://github.com/flying-coyote/security-data-literature-review
