---
type: plan
title: "Security Data Literature Review: Project Brief"
created: 2025-10-19
updated: 2026-11-17
tags: [project-brief, literature-review, scope, decisions-log, assumptions]
---

# Project Brief: Security Data Literature Review

This repository is a living literature review of the evidence on running security data (logs, events, detections) on modern data platforms: open table formats such as Apache Iceberg, columnar engines such as ClickHouse and DuckDB, streaming systems such as Kafka and Flink, and the schemas and catalogs that sit between them. It serves as the evidence companion to the handbook *Modular Open Architecture (MOAR) for Cybersecurity Data*, which means the handbook's footnotes resolve to entries here and each entry carries an evidence tier and a verification record, so a reader can check a claim against its source rather than taking the handbook's word for it. The same corpus feeds a journal manuscript (`PUBLICATION-MANUSCRIPT.md`) that is being prepared for submission.

This brief states what is true about the project now, what it covers, what is still assumed rather than known, and which decisions are on record. Counts that appear on more than one page are derived from the bibliography and checked by `scripts/count_reconcile.py`, so the figures below are the gated values and will fail the gate if they drift.

---

## Part 1: Canonical facts

### Fact 1: The corpus

`MASTER-BIBLIOGRAPHY.md` is the corpus. Each entry is a `#### ` block that is meant to carry an evidence tier, a URL or identifier, the findings it is cited for and a validation record; two are documented no-primary stubs without a tier, and entries still missing a primary are listed by the bibliography sweep.
- Level-A share: 22.5% live-computed 2026-11-17 (61/271 tiered). This is a description of the corpus rather than a grade, since the Level-A target was retired (Fact 4).
- Full tier mix, stub count and source-type breakdown: run `python3 scripts/count_reconcile.py`, which derives them from the bibliography and checks every page that states them.
- **Source**: `MASTER-BIBLIOGRAPHY.md`, `scripts/count_reconcile.py`, `scripts/automation_dashboard.py`

### Fact 2: 9 Hypotheses Assessed with Rubric Scores
There are 9 hypotheses assessed so far. The scores are the 2026-07-13 rubric rescore (`methods/RESCORE-2026-07-13.md`, adopted as canonical 2026-07-16) and match `PUBLICATION-MANUSCRIPT.md` §3.7, which is the canonical source; the gate checks each line below against it.
- **H-ARCH-01** (Iceberg Dominance): STRONGLY VALIDATED, 23/25 - industry consensus as de facto standard; the bare "76% adoption" figure is unsourced and is not used
- **H3-PERFORMANCE-01** (ClickHouse): HIGH CONFIDENCE, 19/25 - Cloudflare 6M requests/second in production
- **H-STREAM-01** (Stateful Streaming): MODERATE, 15/25 - Samza (VLDB 2017) plus Azure production scale; two legs cap the source count
- **H-LOGCOMP-01** (Machine-Data Compression; added 2026-07-10): HIGH CONFIDENCE, 17/25 - three peer-reviewed anchors
- **H-SOC-BASELINE-01** (SOC Alert Base Rates; added 2026-07-10): MODERATE, 13/25 - Yang et al. (USENIX Security 2024), single-source cap
- **H-COST-09** (Tiered Storage): PRELIMINARY, 9/25 - savings band withdrawn; a first-party S3 tier-price derivation bounds the saving
- **H-IMPL-02** (Staffing Scarcity): PRELIMINARY, 5/25 - quantitative legs withdrawn; directional pending re-sourcing
- **H-IMPL-03** (Timeline Premium): PRELIMINARY, 5/25 - quantitative legs withdrawn; directional pending re-sourcing
- **H-IMPL-01** (Streaming TCO): PRELIMINARY, 5/25 - quantitative legs withdrawn; directional pending re-sourcing

The three implementation hypotheses sit at the rubric floor because the staffing, timeline and cost multipliers they once carried were withdrawn in the 2026-06/07 audits as unsourced, and nothing citable has replaced them yet. The scores were computed against the tier labels in force on 2026-07-13, before the 2026-08-19 tier audit, so a rescore under the corrected tiers, which moves only the evidence-quality dimension, is pending (`PUBLICATION-MANUSCRIPT.md` §2.5). **Source**: `PUBLICATION-MANUSCRIPT.md` §3.7, `methods/scoring-rubric.md`, `LITERATURE-HYPOTHESIS-GAP-ANALYSIS.md`.

### Fact 3: A two-arm method under PRISMA 2020

Identification runs on two arms. The curation arm built the corpus from October 2025 onward, starting from the footnotes of an earlier best-practices document and continuing through ongoing channels (practitioner publications, handbook research, reader corrections); PRISMA 2020 classes this as identification via other methods. The database arm is a systematic search of OpenAlex and dblp, run retrospectively on 2026-07-13 against the corpus that already existed, to measure what curation had missed. It identified 400 records, screened 395 after deduplication and included 40, and none of the 40 was already in the corpus, so the curated corpus's measured recall against a systematic search of its own subject was zero. A critical appraisal then refused 14 of the 40, eight of them for predatory, hijacked or delisted venues, and the remaining 26 were incorporated; a second screen of the exclusions admitted one more on 2026-07-16. The search has a disclosed blind spot, since its conjunctive query cannot reach the storage-side database papers the review leans on most, and the screening was done by a single LLM screener against pre-specified criteria with every decision written to disk.
- **Source**: `METHODOLOGY.md` §2.4, `methods/PRISMA-SEARCH-PROTOCOL-2026-07-13.md`, `methods/PRISMA-RETRO-RUN-2026-07-13.md`, `methods/prisma-results/reconciliation.json`, `methods/prisma-appraisal-2026-07-13.json`

### Fact 4: Evidence tiers, and why there is no Level-A target

Level A is peer-reviewed research and official standards (including normative frameworks such as MITRE D3FEND and ATLAS), and nothing else. Production case studies, vendor engineering blogs, conference talks, analyst reports and project documentation are Level B, however good they are; vendor material that is the only support for a claim about how well a product works is Level C, catalogued with its bias stated; Level D (marketing, speculation) is excluded. The review once targeted a Level-A share above 70%, but that target was set against looser criteria that counted production deployments as Level A, and under the corrected definition it was never reachable because peer-reviewed research on security data engineering is thin. The target was retired on 2026-08-19 and replaced with accuracy measures (tier accuracy, claim-to-source integrity, ineligible sources, outstanding fabrications), so the Level-A share is now reported as a fact about the field rather than as a score to push up.
- **Source**: `METHODOLOGY.md` §3.1 and §8.1a

### Fact 5: Research questions

Alongside the scored hypotheses the review tracks 17 research questions (RQ1-RQ17). `METHODOLOGY.md` formalizes RQ1-RQ10, RQ11-RQ14 live in `LITERATURE-HYPOTHESIS-GAP-ANALYSIS.md` Gap 11 and RQ15-RQ17 in Gap 12; RQ15 and RQ17 have no validating evidence yet. The isolation-first questions RQ7-RQ10 have their own working tracker, `isolation-first-security-tracking.md`.
- **Source**: `README.md`, `METHODOLOGY.md` §5.4, `LITERATURE-HYPOTHESIS-GAP-ANALYSIS.md`

### Fact 6: How the review is maintained

A weekly health check (`scripts/weekly_scheduled_check.py`) checks links and source age and escalates to a supervised refresh when something is red or once a month; it decides and reports but never edits the bibliography. The last recorded health-check run is 2026-07-18, so the weekly routine should be treated as lapsed until a new run appears in `scripts/automation_dashboard.py`. Refreshes are logged in `monthly-update-tracker.md` and every change lands in `CHANGELOG.md`, which also serves as the review's amendments record. The vendor database in `vendor-landscape/` is on a quarterly regeneration cadence and gated by `scripts/derive_vendor_rollups.py`, though its last regeneration was 2026-07-18 (version 2026-Q3-c) and the October 2026 regeneration is overdue.
- **Source**: `scripts/SCHEDULING.md`, `monthly-update-tracker.md`, `vendor-landscape/README.md`

### Fact 7: Publication path

The submission target is the *Journal of Cybersecurity* (Oxford University Press, open access), chosen on 2026-07-10 over ACM Computing Surveys and IEEE Security & Privacy. A versioned deposit on Zenodo, assembled by whitelist from this repository by `tools/build/export_paper.sh`, is prepared but its first tagged release and DOI have not been minted. The essays that draw on the review are published at securitydataworks.com/writing; the Substack where the review was first released on 2025-10-22 was retired on 2026-05-24.
- **Source**: `PUBLICATION-VENUE-RECOMMENDATIONS.md`, `docs/ZENODO-RELEASE-CHECKLIST.md`, `tools/build/export_paper.sh`

### Status at a glance
- ✅ 22.5% Evidence Level A (live-derived 2026-11-17: 61 of 271 tiered; reported as a description, the target having been retired 2026-08-19)
- ✅ 9 hypotheses assessed (7 original + 2 added post-audit 2026-07-10), scored under `methods/scoring-rubric.md`
- Database arm run and incorporated (2026-07-13, second screen 2026-07-16)
- The count and vendor-rollup gates run in pre-commit, and those two plus the source-taxonomy and metadata checks run in CI (`.github/workflows/gates.yml`)
- Not yet done: retrospective OSF registration, first Zenodo release, journal submission, independent expert review of the manuscript

---

## Part 2: Scope and boundaries

**In scope**:
- Evidence on modern data platforms applied to security operations: table formats, query engines, streaming, schemas (OCSF), catalogs and the economics of storing and searching security telemetry
- Hypothesis validation (9 assessed under the rubric, drawn from handbook claims, the gap analysis and post-audit peer-reviewed additions); the handbook's own larger hypothesis population is tracked in the handbook project and is not restated here, since nothing in this repository can verify it
- Production deployments and peer-reviewed measurements with numbers, and the vendor landscape as structured data
- First-party benchmark results from the public lab repository, cited at Tier B as single-environment measurements

**Out of scope**:
- A census of all cybersecurity literature; detection-logic research without a data-platform angle
- General data engineering with no security workload
- Operational tooling, except where a tool's measured behaviour is the evidence
- Vendor marketing claims with no production measurement behind them

**Boundaries**:
- **Time window**: published 2018 onward, matching the database arm's date floor, with named pre-2018 foundational exceptions; as a living review there is no fixed end date
- **Eligibility**: only published, publicly citable works; a personal communication is not an eligible source (enforced since 2026-08-12, when one such citation was found and removed)
- **Public repository**: current outreach and relationship tracking are kept outside this repository; older planning notes that name contacts remain in the dated records

---

## Part 3: Open assumptions and known risks

These are the places where the review rests on something not yet verified, or where its own method has a known weakness. Each is stated so a reader can discount accordingly.

1. **No independent expert review yet.** The manuscript has not been reviewed by an outside domain expert, and no interview has taken place; nothing in the corpus may be attributed to a person who has not published it. Expert review is planned before submission, and until then the review's quality controls are its own audits and gates.
2. **The implementation hypotheses are directional.** H-IMPL-01, H-IMPL-02 and H-IMPL-03 sit at 5/25 because their quantitative legs were withdrawn. They will move only if citable staffing, timeline or cost evidence is found, and the review says so rather than restating the withdrawn multipliers.
3. **Single-screener search arm.** LLM screening without a second human screener tends to miss relevant studies (the manuscript cites roughly 13% missed for single screening against about 3% for dual screening), and the database arm's query cannot reach storage-side database venues. Both are disclosed in the manuscript's limitations.
4. **Vendor-relayed evidence is a large share of the corpus.** Roughly three in ten entries are vendor-authored or vendor-relayed (the gated figure is in `PUBLICATION-MANUSCRIPT.md` §3.1), which is why Level B and C entries never carry a hypothesis on their own.
5. **Maintenance has lapsed once already.** The monthly cadence went 96 days without a run in 2026 before the weekly check was added, and the weekly routine's last recorded run is 2026-07-18 (Fact 6). The vendor database has the same problem, since its October 2026 regeneration did not happen and the last one is 2026-07-18.

---

## Part 4: Decisions on record

| Date | Decision | Where it is recorded |
|---|---|---|
| 2025-10-15 | PRISMA-aligned extraction method for the curated corpus | `LITERATURE-EXTRACTION-PLAN.md`, `METHODOLOGY.md` §2 |
| 2026-05-24 | Substack retired; essays move to securitydataworks.com/writing | `CHANGELOG.md` |
| 2026-06-05 | Weekly health check with monthly escalation replaces the lapsed manual cadence | `scripts/SCHEDULING.md` |
| 2026-07-10 | Journal of Cybersecurity chosen as the submission target | `PUBLICATION-VENUE-RECOMMENDATIONS.md` |
| 2026-07-13 | Database arm run and appraised; survivors incorporated | `methods/PRISMA-RETRO-RUN-2026-07-13.md` |
| 2026-07-16 | 2026-07-13 rubric rescore adopted as the canonical hypothesis scores | `methods/RESCORE-2026-07-13.md` |
| 2026-07-16 | Zenodo deposit assembled by whitelist from this repository | `tools/build/export_paper.sh` |
| 2026-07-18 | Vendor database regenerated; rollups derived and gated | `vendor-landscape/quarterly-updates/2026-Q3-regen-2026-07-18.md` |
| 2026-08-12 | Personal communications ruled ineligible as sources | `MASTER-BIBLIOGRAPHY.md` header, `CHANGELOG.md` |
| 2026-08-19 | Level-A target retired; tier criteria corrected and every tiered entry re-audited | `METHODOLOGY.md` §8.1a |

Every stated count is derived rather than typed, which is the rule behind `scripts/count_reconcile.py`: a number that appears on more than one page drifted on seven-plus pages before the gate existed, so the gate now fails a commit that states a count the bibliography does not support.

---

## Part 5: Where things live

| Question | File |
|---|---|
| What does the evidence say? | `PUBLICATION-MANUSCRIPT.md` |
| What is the source for a claim, and has it been checked? | `MASTER-BIBLIOGRAPHY.md`, `RESEARCH-JOURNAL.md` |
| How was the corpus built and tiered? | `METHODOLOGY.md`, `methods/` |
| Which hypotheses lack evidence? | `LITERATURE-HYPOTHESIS-GAP-ANALYSIS.md` |
| What changed, and when? | `CHANGELOG.md` |
| Vendor capabilities and evidence | `vendor-landscape/` |
| Deep evidence behind the handbook chapters | `book-appendices/` |

---

## History

This brief was first compiled on 2025-10-19, when the review had about 76 sources, a self-graded 79% Level-A share, a Substack as its venue and an analyst-data partnership in prospect for the vendor work. Most of that picture changed in 2026: the fabrication audits of June and July withdrew the Level-A self-grade and several hypothesis legs, the Substack was retired, the partnership did not go ahead before the integration it was meant to feed was archived, and the method gained a systematic database arm. Earlier versions of this brief, including the October 2025 assumption log and its risk estimates, are in the repository's git history, and the dated record of each change is in `CHANGELOG.md`.

---
**Updated**: 2026-11-17 (rewritten to current scope; previous stamp 2026-07-16)
