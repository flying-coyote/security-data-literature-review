---
type: review
title: "U3 notes: companions quality pass (appendices, analysis bundles, gap analysis)"
created: 2026-11-17
status: working
---

# U3 notes (2026-11-17)

Scope: `book-appendices/**`, `analysis-bundles/**`, `LITERATURE-HYPOTHESIS-GAP-ANALYSIS.md`. The change list is `U3-changelog.md`; the full per-change log with sources is in the hub at `02-projects/quality-program-2026-11-17/litreview/unit-U3-companions.md`.

## Checks at the end of the pass

- Withdrawn-leg grep (DORA 2.7x, Ververica, IDC, MIT-TR, DOES, AWS 55%, Netflix 70-80%, Shell, 76% adoption, 96%, and the retired benchmark's two headline figures): 226 hits, of which 114 are struck at the point of use and 60 sit inside a dated note. The 52 left unstruck were reviewed one by one and judged not to be live withdrawn legs, though the recovery review below found further live legs that this grep did not catch (the H-IMPL-01 convergence line, the H-IMPL-03 source-type, geography and limiter lines, the AWS Well-Architected 35% line and the Uber mentions in H-STREAM-01), and those are now struck. The 52 are the Netflix ClickHouse logging figures (5 PB/day, a different Tier C source that stands), Netflix as an Iceberg maintainer or blog, the W3Techs 96% Linux figure in Appendix H (a different, hedged claim), Appendix K's computed 2.3-2.7× SIEM ratio, the staffing calculator's own 2.7× multiplier (now labelled author-modeled at each use), the confidence rubric's illustrative "2.7× more" precision example, and lines that name a withdrawn figure in order to say it was not found (the 76% notes). The retired benchmark's two headline figures have zero hits in scope.
- Relative Markdown links in scope: 1, resolving; same-file anchors: all resolve.
- `python3 scripts/count_reconcile.py`: all 79 surfaces agree (re-run after the recovery pass) (none of the U3 files is a gated surface).
- Local paths and memory slugs: zero `~/`, `/home/`, `project1`, `01-knowledge-base` or `00-inbox` left in scope. Open decisions that used to carry an owner sign-off flag now read "pending review" in the public text, so the status stays visible without a name. "Maintained By / Author: Jeremy Wiley" lines are author bylines and were left.

## Ledger coverage, stated honestly

3,379 numeric tokens after the recovery pass, which extended the extractor to N:1 ratios (10 ratio rows, among them Appendix I's Huntress 50:1; the other 4 new rows come from the recovery edits); 87 checked at a primary (64 verified against lab result files and the re-score, 13 found not-in-source by the lab erratum and labelled, 10 S3 tier figures arithmetic-checked), plus 1 flagged not-in-source on the bibliography's Huntress note and staged for U1 (the video primary was not checked), 1,107 labelled as author-modeled in the text (line or section level), 503 withdrawn and labelled, 237 traced to a named public lab bench, 112 traced to a bibliography entry that carries the same number (U1 owns the entry check), 225 cite a URL, tier or footnote not re-fetched this pass (including Appendix I's three Netflix and 10-100× Tier C figures, which the first run had mis-filed as lab-traced, and the gap analysis's Cloudflare 10×, which it had mis-filed as withdrawn), and **1,107 state a number with no source named at the point of use**. That last group is the backlog, so plan goals 1 and 6 (every number sourced or labelled) are only partly met by this unit, and the 1,107 rows should run as an explicit follow-on unit. The backlog concentrates in Appendix I (300, mostly operational figures in the engine-selection prose and code-adjacent text), Appendix B (165), Appendix A (163, worksheet defaults and vendor price inputs), Appendix H (118) and the cost bundle (76). Many are design defaults, SLA thresholds or illustrative timings that a reader would recognize as such, but the text does not label them, so a future pass should either attach the A.6 model or a primary, or add a section-level "illustrative" label as Appendices C and K already have. I did not add blanket labels, because deciding which figures are modeled is an authorial call on each appendix.

## Staged for the owner (not applied)

1. **Appendix H §H.4.4 rewrite.** The shipped-mapping paragraph's argument ("maps to OCSF is a coverage claim, not a fidelity guarantee", illustrated by activity 17%) now carries a correction note, but the paragraph itself still argues from the withdrawn example. Default I would take: rewrite it around what the re-score shows (field 100%, value 93.24% with the `time` type-contract failure, activity 83.30% with S0 the only disagreement, and the availability gap for other sources), keeping the method claim. This is a voice and argument change, so it waits for a ruling.
2. **RQ14 re-tier wording in the gap analysis.** The OVERTURN block's "coverage is a claim, fidelity is not" re-tier rested partly on the 17% example. The availability leg stands. Default: keep the Tier-B caveat, reword its fidelity clause to the type-contract and S0 findings.
3. **Open decisions now marked "pending review" in the public text (the decision is still open):** (a) treating the de-gamed APT29 +0.188 as the confidence-matrix headline over the published +0.719, and the H-CROSS-TOOL-ASSURANCE-01 band row (matrix revision row 1.4); (b) the RQ14 asserted-A to Tier-B re-tier (gap analysis RQ14 OVERTURN and the author line). Both are hypothesis-confidence items.
4. **Grades flagged but not changed:** the gap analysis's "Netflix Security Observability Platform" source block (Evidence Level A, but its bibliography entry was retitled 2026-07-09 as a mis-attribution); the RQ12 maturity success bands (Evidence Level A with no primary for the per-level percentages); H-STREAM-01's Evidence Level A after the Uber leg's withdrawal. Each is a tier change, so it is staged.
5. **Staffing calculator break-even inputs.** The Altinity "70% MTTR reduction / 40% analyst productivity" figures still have no bibliography entry, and a 2026-11-17 web search found no Altinity page carrying them (the closest, the SenseOn case study, does not show either figure in its search excerpt). The calculator already marks them UNCONFIRMED. Default: remove both from the break-even example or replace them with an explicitly assumed input.
6. **Drifted `MASTER-BIBLIOGRAPHY.md:NNN` anchors** in the confidence matrix and cost bundle point at pre-July line numbers, and U1 is editing that file in parallel. Default: re-anchor by entry title after U1 lands, not by line.

## Currency notes

- OCSF 1.9.0 released 2026-08-03 (GitHub release and tag); 1.8.0's tag commit and release are both 2026-03-18, so the "2026-03-16" dates in Appendices H and J were corrected. In the lab's pinned 1.9.0 export, Account Change and User Access are deprecated since 1.9.0 in favour of User Management, the `d3fend` and `d3f_tactic` objects are still present, and there is still no network-anomaly class.
- D3FEND ontology 1.6.0, tag commit 2026-09-01; d3fend.mitre.org shows 1.6.0.
- Releases read from GitHub 2026-11-17: OpenSearch 3.9.0 (2026-09-29), DuckDB 2.0.0 (2026-10-21), Iceberg 1.12.0 (2026-09-30), ClickHouse v26.10 stable, Trino 484, Spark 4.3.0, Flink 2.3.0, Kafka 4.4.0, Polaris 1.9.0; DuckLake is still 1.0 per ducklake.select.
- Not checked against DuckDB 2.0.0: the Iceberg maintenance gaps in Appendix I §I.2.2 (stated as true through 1.5.3) and the DuckLake issue repros in §I.5.5.
- Appendix G's 93-row link sweep was not re-run (outside this unit's link goal, which named E and J).

## Process note

Two read-only `git log`/`git status` calls were made against `~/sdw-lab-benchmarks` (another repo) to confirm the lab erratum was committed and pushed before citing it. No git command was run in this worktree.

## Added by the recovery pass (2026-11-17)

Staged, not applied:

7. **Appendix I §I.4A.2, Huntress 50:1 (line 529).** `MASTER-BIBLIOGRAPHY.md entry "Huntress - ClickHouse Migration Case Study", Notes line (978 on 2026-11-17)` records that the Huntress "20-50× compression" figures are not supported by the cited blog and were removed, and the reviewer's 2026-11-17 fetch of the ClickHouse Huntress blog found a cost reduction of "more than 90%" and 200,000 records/s but no compression ratio. The 50:1 sentence predates this unit and stays in Appendix I until U1 resolves it against the video primary (youtube `lhsWNofOcdk`); it should not be cited until then. The copy this unit had added to the gap analysis was deleted.
8. **Gap analysis RQ16 (around line 846).** The opening clause "the normalization step itself drops detection-relevant structure" still rests on the withdrawn mechanism. The closing clause is now struck and re-pointed at the re-score, but rewriting the argument is a voice change, so it waits with item 1.
9. **Gap analysis Huntress source block (Gap 6, Source 2).** Its "Evidence Level: A" now carries a note that the bibliography re-tiered both Huntress entries to B on 2026-08-19; the letter itself was left for the tier ruling. In the cost bundle the same grade was aligned to Tier B at the reviewer's request, as factual alignment with the bibliography rather than a new tier call; reverse it if that is judged a tier change.
10. **H-STREAM-01 score text.** The matrix's record note still says "re-score pending", while `methods/RESCORE-2026-07-13.md` records 15/25 (High to Moderate). The Total Confidence line now points to both, and reconciling the note is a confidence-wording item.

Left as is, with the reason: Appendix H's JSON example at about line 830 carries `"version": "1.4.0"` inside a sample `d3fend` object, which illustrates the object shape rather than stating the current release; H3-PERFORMANCE-01's 17/25 total already carries its own recompute note and the 2026-07-16 supersession note, so it got no extra label.

