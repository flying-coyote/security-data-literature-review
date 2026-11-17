# Reader figures

Two figures for the repository's front pages, each drawn as an SVG source with a PNG render beside it. Each one carries only numbers from frozen records rather than live counts, which keeps the images from drifting as the bibliography grows, and the live corpus counts stay in the text, where `scripts/count_reconcile.py` gates them.

| Figure | Files | What it shows |
|---|---|---|
| Review method | `review-method.svg`, `review-method.png` | The curation arm and the July 2026 database arm, the appraisal gate the 40 database finds went through (with the one record a second screen of the exclusions added), then tiering, the number-checking rule and the bibliography |
| Evidence tiers | `evidence-tiers.svg`, `evidence-tiers.png` | Levels A to D as METHODOLOGY.md section 3.1 defines them, with the A/B boundary highlighted and no corpus percentages |

The repository map lives as a linked table in the root `README.md` ("Repository map"), which updates in the same commit as the files it names, so it has no image here.

## Where every number and label comes from

Paths are relative to the repository root, and line numbers were re-read on 2026-11-17 against the tree with the README, manuscript and methodology rewrites of that date in place. `build_figures.py` points here rather than repeating line numbers, so this table is the one place to update when a cited file moves.

### Review method

| Figure text | Value | Source |
|---|---|---|
| Records identified | 400 | `methods/PRISMA-RETRO-RUN-2026-07-13.md:31` |
| OpenAlex, dblp | 354, 46 | `methods/PRISMA-RETRO-RUN-2026-07-13.md:29-30`; `methods/prisma-results/search-log.json:33-34` (`raw_counts`) |
| Run date | 2026-07-13 | `methods/PRISMA-RETRO-RUN-2026-07-13.md:4` (`run_timestamp_utc: 2026-07-13T02:36:26Z`) |
| Duplicates removed | 5 | `methods/PRISMA-RETRO-RUN-2026-07-13.md:34` |
| Screened | 395 | `methods/PRISMA-RETRO-RUN-2026-07-13.md:35`; `methods/prisma-results/reconciliation.json:14` |
| Excluded | 355 | `methods/PRISMA-RETRO-RUN-2026-07-13.md:36`; `methods/prisma-results/reconciliation.json:16` |
| Included | 40 | `methods/PRISMA-RETRO-RUN-2026-07-13.md:37`; `methods/prisma-results/reconciliation.json:15` |
| Already in the corpus | 0 of 40 | `methods/prisma-results/reconciliation.json:18` (`overlap_A`) and `:22` (recall 0/40) |
| Second screen of the exclusions, flagged | 355 reviewed, 11 flagged | `methods/second-screen-2026-07-16.json:5`, `:7` (`excluded_reviewed` 355, `disagreements` 11) |
| Second screen, admitted through the gate | 1 | `methods/second-screen-adjudication-2026-07-16.json:34` (`count` 1); `methods/second-screen-adjudication-2026-07-18.json:69` (`count` 0) |
| Refused at appraisal | 14 of 40 | `methods/prisma-appraisal-2026-07-13.json:6`, `:8` (`appraised` 40, `dropped` 14) |
| Predatory or compromised venue | 8 | `methods/prisma-appraisal-2026-07-13.json:9` |
| Not peer-reviewed | 3 | `methods/prisma-appraisal-2026-07-13.json:10`; records rank 15, 19, 33 (`:562`, `:713`, `:1243`) |
| Unreadable | 1 | record rank 16, `methods/prisma-appraisal-2026-07-13.json:602` |
| Refuted by an independent verification pass | 2 | records rank 5 (duplicate publication) and rank 31 (numbers not found at the source), `methods/prisma-appraisal-2026-07-13.json:186`, `:1171`; the pass was a second LLM agent, separate from the one proposing the citation (`methods/prisma-appraisal-2026-07-13.json:4`; `PUBLICATION-MANUSCRIPT.md:184`) |
| Admitted at the gate | 26 | `methods/prisma-appraisal-2026-07-13.json:7` (`citable` 26); `methods/incorporated-2026-07-13.json:5` |
| Refusal breakdown, cross-check | 8 + 3 + 1 + 2 = 14 | `METHODOLOGY.md:96`; `PUBLICATION-MANUSCRIPT.md:184` |
| Built by reading, 2025 to 2026 | label | `methods/PRISMA-RETRO-RUN-2026-07-13.md:13` |
| 283 footnotes in a 2024 practitioner manuscript | 283; 2024-04-15 | `METHODOLOGY.md:56`, `:73` |
| Then vendor and project docs, standards, analyst reports, talks | label | `METHODOLOGY.md:65-69` |
| Mostly grey literature a database cannot index | label (171 grey of 195 blocks at run time, plus 24 indexable academic entries) | `methods/PRISMA-RETRO-RUN-2026-07-13.md:67-68` |
| Each source tiered A to D; Level A is peer review and official standards only | label | `METHODOLOGY.md:104`, `:107` |
| Rule: carried numbers checked at the primary | label (a standing rule, drawn dashed, not a completion claim) | `PUBLICATION-MANUSCRIPT.md:444`, `:1052` |
| Verdict per number in the ledger; paywalled numbers marked unverifiable | label | `methods/verification-2026-11/ledger.json` (`verdict_vocabulary` includes `unverifiable-paywall`) |
| Live counts derived by `scripts/count_reconcile.py` | label | `README.md`, section "Corpus at a glance" |

The 26 admitted at the gate and the one admitted from the second screen make 27 database-arm admissions in all. The figure prints 26 at the gate's exit because that is the gate's own count, and the dashed side note carries the extra record into the same gate so that the 26 + 1 stays visible.

### Evidence tiers

Every label paraphrases `METHODOLOGY.md` section 3.1 (lines 102-132).

| Figure text | Source |
|---|---|
| Title: Level A is peer review and standards; production evidence, however good, is B | `METHODOLOGY.md:104` |
| A: peer-reviewed work at a named venue | `METHODOLOGY.md:107`, `:109` |
| A: NIST, ISO/IEC, IETF RFC, W3C, OASIS | `METHODOLOGY.md:110` |
| A: formal specs (Iceberg table spec, OCSF schema) | `METHODOLOGY.md:111` |
| A: MITRE D3FEND, ATLAS, structure not efficacy | `METHODOLOGY.md:112` |
| The line: no production evidence above it | `METHODOLOGY.md:104`, `:113` |
| B: deployments and case studies, vendor engineering blogs, talks, trade books, analyst reports, expert interviews, advisories, official project docs | `METHODOLOGY.md:113`, `:118` |
| B: preprints with no named venue | `METHODOLOGY.md:109` (not Level A); `README.md` tier table, row B |
| C: vendor posts, product docs and talks with no production measurement; kept with bias flagged, never carries a hypothesis on its own | `METHODOLOGY.md:127-128` |
| D: unverified claims, marketing, speculation; excluded | `METHODOLOGY.md:131-132` |

The figure carries no corpus percentages by design.

## Rebuilding

The SVGs come from `build_figures.py`, which holds every number as a named constant, so a change to a figure starts there:

```bash
python3 docs/figures/build_figures.py
```

The PNGs were rendered from the SVGs with sharp at 1080 px wide on a white background (`sharp(svg, {density: 144}).resize({width: 1080}).flatten({background: "#ffffff"}).png()`). The SVGs name DM Sans first and fall back to Arial or Liberation Sans, and the committed PNGs were rendered with Liberation Sans because DM Sans was not installed on the build machine.

## Glance checks

`glance/<figure>/` holds the visual-gestalt glance-check output for each PNG: the script's text report (`glance-check.txt`) and its 375 px phone, blur, grayscale and deuteranopia views, plus the three centre crops. Each figure was reviewed on those views for a single focal element, legibility at phone width, overlaps and palette conformance (only Harbor Haze colours and the azure focal highlight appear). In the method figure the refusal breakdown sits on a light inset in dark ink inside the azure gate, so the focal box keeps body-text contrast at phone scale. The review-method figure is taller than the 4:5 LinkedIn limit, which its report flags, because it is a page figure and is not meant to travel as a feed image; the evidence-tiers figure (1080 x 1309) sits inside the single-photo range.
