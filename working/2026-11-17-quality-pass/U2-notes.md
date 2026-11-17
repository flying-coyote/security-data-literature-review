---
type: review
title: "U2 notes: manuscript, methodology and superseded companions (2026-11-17 quality pass)"
created: 2026-11-17
status: complete
tags: [quality-pass, manuscript, references, staged]
---

# U2 notes (2026-11-17)

Scope: PUBLICATION-MANUSCRIPT.md, METHODOLOGY.md, REFERENCES.md, APPENDICES.md, FIGURES-AND-TABLES.md, publication-graphics/, scripts/count_reconcile.py. No hypothesis score or confidence label was changed. The per-number record is `U2-number-ledger.md`; the paste-ready changelog entry is `U2-changelog.md`.

## Checks at the end of the pass

- `python3 scripts/count_reconcile.py`: all 79 surfaces agree (was 54). Counts unchanged: 273 blocks, 271 tiered, A 61 (22.5%), B 170, C 40.
- `python3 scripts/count_reconcile_fix.py`: nothing to change.
- Main-text word count by the documented command (`sed -n '/^## ABSTRACT/,/^## ACKNOWLEDGMENTS/p' PUBLICATION-MANUSCRIPT.md | wc -w`): 14,957 at the end of the first pass (was 14,904 on disk at the start of the pass, 14,859 as last recorded); 14,954 after the recovery pass. Abstract: 350 words, unchanged. The pass added tier definitions and corrections and paid for them by cutting duplicated October-2025 process text (the §2.5 audit-note repeat of §3.7, the §2.6 thematic list, the stale quarterly-plan block, the extraction-phase list, one duplicated sentence in §2.2).
- `bash tools/build/build.sh` completes (pandoc and xelatex present), run in a scratch copy of the tree so no `build/` directory was created in the worktree: `Built build/litreview.pdf`.
- Figure 1 recompiled with pdflatex and inspected as a rendered PNG; the left-arm boxes overlapped in the committed PDF (appraisal, eligibility and inclusion boxes stacked into each other, and the duplicates box's last line was hidden), and they no longer do.

## Reference verification, [1]-[49]

| Ref | Check | Result | Change |
|---|---|---|---|
| [1] Arrow Flight SQL | URL 200 | exists, Feb 16 2022 | none |
| [2] Iceberg | URLs 200 | exists; 407 contributors is a dated count | none |
| [3] Cloudflare 6M | URL 200, quote read | page names no author in metadata; "6M HTTP requests per second" verified | none (author A. Bocharov kept from the bibliography record) |
| [4] CISA AA23-193A | old alert URL returns 403 to scripted clients | advisory page verified, quotes M-21-31 retention | URL repointed to the advisory page `cybersecurity-advisories/aa23-193a` |
| [5] ClickHouse vs ES | URL 200 | author Tom Schreiber, May 7 2024, 12-19× / 9-12× verified | author added |
| [6] ClickHouse IPv6 type | redirects | live at `/docs/reference/data-types/ipv6` | URL updated |
| [7] Confluent tiered storage | redirects | live at `/platform/current/clusters/tiered-storage.html` | URL updated |
| [8] DORA 2024 | URL 200 | exists; cited only in audit notes | none |
| [9] Dremio | URL 200 | Nov 28 2023, n=500, Propeller Insights, 29% vs 23% verified | day added |
| [10] Forrester TEI CDP Public Cloud | no locator before | Cloudera-hosted PDF exists ("October 2021, A Forrester Total Economic Impact Study Commissioned by Cloudera", 28 pages); the withdrawn 39/32/29 split is absent from it | landing-page locator added |
| [11] Forrester TEI Private Cloud | URL 200 | May 2024 | none |
| [12] Azure Kafka | URL 200 | Feb 5 2019; authors Noor Abani and Negin Raoof; "3 trillion events per day" | authors added |
| [13] Netflix logging | URL 200 | ClickHouse-authored post about a July 2025 meetup talk by Daniel Muino (the page carries a 2026 publication date) | attribution corrected to ClickHouse as author, talk named |
| [14] Samza | Crossref 10.14778/3137765.3137770 | authors, vol 10(12), pp. 1634-1645, 2017 match | DOI added |
| [15] OMB M-21-31 | URL 200, PDF downloaded | official URL is live (not dead as the survey expected); dated Aug 27 2021; retention table reads "12 Months Active Storage / 18 Months Cold Data Storage" | day added; URL kept |
| [16] PRISMA 2020 | Crossref | BMJ 372:n71, 2021 | none; still the current statement |
| [17] Cloudflare log analytics | URL 200 | authors Monika Singh and Pradeep Chhetri, Sep 2 2022; 600→60 bytes verified | co-author added |
| [18] SK Telecom | URLs 200 | speakers JaeChang Song and Jennifer Oh, Dec 19 2022 | none |
| [19] Uber | URL 200 | speakers Rohit Yadav and Satish Duggana, Current Bengaluru 2025; no streaming/batch split on the page | speakers and event added; §4.1 split relabelled |
| [20] MOAR | URL 200 (redirects to trailing slash) | exists | none |
| [21] SDW lab | URL 200 | the CIDR probe, engine bench, concurrency sweep and SIEM-baseline probe are in `flying-coyote/security-data-that-works` (docker/lab/), not in `sdw-lab-benchmarks`, which holds the Zeek compression runs | locator rewritten to name both repositories and the run-record files |
| [20], [21] | Zenodo placeholders | owner-held | untouched |
| [22] Pebbles | Crossref | matches | none |
| [23] Blitzcrank | Crossref 10.14778/3675034.3675044 | matches | DOI added |
| [24] LogLite | Crossref 10.14778/3749646.3749652 | author order Tang, Yang, Shen, Zhang, Lin, Tian matches (the PDF filename uses "yang") | DOI added |
| [25] Yang et al. | USENIX page | eleven authors in the listed order | none |
| [26] PBC | Crossref 10.1145/3626732 | PACMMOD vol 1 no 4, 2023 (SIGMOD 2024) | volume, issue, DOI added; year corrected 2024 → 2023 issue year |
| [27]-[31], [33], [36], [37] | Crossref | authors, venue, volume match | [31] pages 383-395 added |
| [32] SPARCS | Crossref | pages are 199-202, not 91-100 | corrected |
| [34] Kajiura | Crossref | pages 2215-2221 | added |
| [35] Loganathan | Crossref | pages 1-6 | added |
| [38] Yahyaoui | Crossref | pages 51-56 | added |
| [39], [41], [43]-[48] | Crossref | match | none |
| [40] Flemyng et al. | Crossref | Cochrane Database Syst Rev, ED000178, 2025 (Crossref misspells the second author; the manuscript spelling Noel-Storr is right) | none |
| [42] Cochrane Handbook ch. 14 | cochrane.org current page and versions page | current version 6.5 (2024), minor 6.5.1 updates in 2025 (Figure 14.1.a corrected) and 2026 (no ch. 14 change; adds Chapter 21 on living systematic reviews); ch. 14 last updated Aug 2023 | chapter URL added; recovery pass replaced the version note with Cochrane's own cite form |
| [49] PRISMA-LSR (new) | Crossref 10.1136/bmj-2024-079183 | Akl et al., BMJ 387:e079183, Nov 2024 | added as the current reporting extension for living reviews, cited once in §2.7 |
| Format line | — | "alphabetical by author" was false past [21], and the first rewrite still claimed it for [1]-[21] | recovery pass: no ordering claim for [1]-[21] |

## Staged for the owner (not applied)

1. **Rescore under the corrected tiers (hypothesis confidence, ask class).** The §3.7 scores were computed 2026-07-13 against tier labels the 2026-08-19 audit has since changed. Re-deriving only the evidence-quality dimension (rubric Dimension 2, share of legs at Level A, methods/scoring-rubric.md:39-47) from the current bibliography labels gives:
   - H-ARCH-01: legs SK Telecom (B, MASTER-BIBLIOGRAPHY.md:116), vendor support (C, :1710), ASF governance (B, :1734), Dremio/industry consensus (C, :1681): 0 of 4 at A, quality 5 → 1, total 23 → 19 (High, leaves Strongly Validated, which would leave no hypothesis in that band).
   - H3-PERFORMANCE-01: Cloudflare 6M (B, :286 block), Cloudflare log migration (B), ClickHouse-vs-ES benchmark (B, :1849 block), first-party CIDR probe (A by the rubric's "measured A" rule): 1 of 4 = 25%, quality 3 → 1, total 19 → 17 (stays High).
   - H-STREAM-01: Samza (A, :694), Azure (B, :1055 block): 50%, quality 5 → 2, total 15 → 12 (stays Moderate).
   - H-LOGCOMP-01, H-SOC-BASELINE-01: all legs still A, unchanged. H-COST-09 and the three H-IMPL rows already score 1 on quality, unchanged.
   Default I would take: run the rescore through the evidence gate and apply it, since the rubric says to score from the current label. Until then the manuscript states (§2.5, Appendix A, metadata item 7) that the scores are the dated 2026-07-13 computation. That qualifier is the only §3.7-adjacent wording this pass added; no score, band or confidence label moved.
2. **A named practitioner in METHODOLOGY.md §2.2.** It named the one practitioner actually interviewed (with employer), while the manuscript's acknowledgments say that practitioner is "anonymized by request", and it gave the outreach status of three other named people. The pass anonymized it to match the manuscript. Please confirm, and decide whether the manuscript should keep naming the two prepared-but-not-held interviewees in §3.8, §4.4, Appendix C and the acknowledgments (outreach-adjacent).
3. **§3.8 engine finding (closed in the recovery pass).** The first pass marked "StarRocks leads high-cardinality distinct" as not-in-source because it searched only `security-data-that-works`. The per-workload table is in this repository at `analysis-bundles/hypothesis-confidence-matrix.md:640-645` (StarRocks 97.7 ms vs DuckDB 139.7 on the latency-only distinct) and `archive/analysis-bundles/performance-benchmarks-table.md:158-166`, and the 100M crossover (ClickHouse takes the full-scan count) is at `hypothesis-confidence-matrix.md:629-637`. §3.8 now states all three readings, and [21] points at the matrix for the per-workload tables. Ledger row 123 is now verified-at-record.
4. **Unsourced framing numbers left in place**, each labelled where the text already treats it as an estimate: "2-3 months" commonly assumed timeline (§1.1, §1.4), 1-7 year retention and the ~30-day query concentration (§3.3.2), three-nines/four-nines tiering (§3.3.3, §4.2), 3-6 month analytics retention (§4.2). A primary for any of these would let the label come off.
5. **PRISMA-LSR conformance.** [49] is now cited as the reporting standard for living reviews, but the manuscript has not been checked against its four living-specific items (L1 living-mode parameters, L2 changes to methods, L3 changes to results, L4 authors and roles per version). Worth a pass before submission. The 2026 Cochrane Handbook 6.5.1 update also added a Chapter 21 on living systematic reviews, a candidate methods reference.
6. **Figure 1 is the 2026-07-16 edition.** Its other-methods arm counts 203 curated entries; the corpus has grown by 43 entries since, all through that arm. The caption, alt text and convergence box now bridge to 273/271 and the bridge is gated, but a full regeneration would need the per-entry source type of the current other-methods arm (the taxonomy JSON gives the whole corpus, not the arm split).

## Out of scope, for other units or the main session

- `tools/build/build.sh` comments still say "[1]–[38]" and "Appendices A–D" (U5 scope; the manuscript now has [1]–[49] and Appendices A–E).
- `analysis-bundles/cost-reality-reference.md` still points at FIGURES-AND-TABLES.md (U3 scope); FIGURES-AND-TABLES.md stays at its path.
- The manuscript cites `NEW-HYPOTHESES-PROPOSAL-2026-07.md`, `RESCORE-PROPOSAL-2026-07.md` and `GEMINI-DR1-INTAKE-2026-07-10.md` by bare filename, which U5's move map will relocate; `scripts/repoint_moved_paths.py --apply` should be run over PUBLICATION-MANUSCRIPT.md and METHODOLOGY.md at integration.
- METHODOLOGY.md §5.4 was left in place because PROJECT-BRIEF.md:53 and isolation-first-security-tracking.md:11 cite it by number; the new §1 roadmap points readers to it instead of moving it.

## Recovery pass additions (2026-11-17)

- **Two concurrency sweeps disagree, and the manuscript cites one.** §3.8 now says its concurrency figures come from the 2026-06-15 1M-row sweep (`security-data-that-works/docker/MOAR-EVIDENCE-RUN-2026-06-15.md:77-89`: DuckDB 1.52×, ClickHouse 3.71×, Trino 4.00×, StarRocks 5.35× from 1 to 16 clients). `analysis-bundles/hypothesis-confidence-matrix.md:648-657` reports a different sweep over a 10M-row table (DuckDB flat at ~46 q/s, ClickHouse 20 → 58, StarRocks 16 → 42, Trino 9 → 13). The workloads and table sizes differ, so the two do not refute each other, but the repo should name one sweep as canonical. Left for the owner or U3 (the matrix is U3 scope); the manuscript is qualified so a reader can tell which sweep it cites.
- **Ledger verdict split, stated.** The ledger holds 35 verified-at-record rows and 20 verified-at-primary rows (counted on the verdict column after the row-123 change), plus derived-gated, corrected, author-modelled and historical-record rows. Record-tier rows lean on the 2026-06/07 audit records and the 2026-07-10 verbatim checks instead of a fresh fetch, because those records quote the primary verbatim and re-fetching every one was beyond this unit's budget. Plan goal 2 asked for re-reads at the primary, so this is a stated deviation. The review pass spot-read the CIDR, SIEM-index, Zeek, Uber and Crossref rows at their primaries and agreed with each. The record-tier rows that carry headline numbers (Yang 24K-134K / 0.01%, LogLite, Abbasi) are the ones to re-read first if the gap matters before submission.
- **Expert-interview pair in the taxonomy.** The two `expert_interview_or_personal_communication` entries in `methods/prisma-results/reconciliation.json` are the anonymized practitioner (MASTER-BIBLIOGRAPHY.md:2866) and the Okta / DuckDB entry, which the bibliography re-sourced on 2026-08-12 to a public Data Council 2024 talk (MASTER-BIBLIOGRAPHY.md:1104-1110). The frozen classification still types the second as an interview. The manuscript §3.1 line now says so. Re-typing it would change `source-taxonomy.json`, Figure 3 and the gated counts, so it is left for a deliberate regeneration.
- **Anonymization of the METHODOLOGY interviewee (staged item 2, continued).** The edit stays applied. Whether the repository's history matters is with the owner (see the hub unit log). METHODOLOGY.md RQ8's data sources named an OCSF contact who has no bibliography entry and was never interviewed; the name is replaced with "OCSF deployment case studies".
- **Cochrane [42].** The 6.5.1 update detail (2025 and 2026 minor updates, Figure 14.1.a corrected in 2025, Chapter 21 on living reviews added in 2026) now lives only here. The reference uses Cochrane's own cite form, because the versions page could not be re-fetched to confirm the detail.
- **Word count after the recovery pass:** 14,954 main text by the documented command (was 14,957), abstract 350. 46 words of headroom remain under 15,000.
