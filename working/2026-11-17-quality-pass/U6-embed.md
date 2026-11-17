# U6 figures: embed snippets for integration (2026-11-17)

Integration notes for the main session, kept under `working/` so that `docs/figures/` holds only reader material. Paths are written for `README.md` at the repository root. Each snippet links the PNG and wraps it in a link to the SVG, which GitHub renders sharper on click. The alt text carries the message in a sentence or two; the full description sits in each SVG's `<desc>`.

## Where the figures go

- **README.md only, for now.** `METHODOLOGY.md` is in the DOI-frozen deposit whitelist (`tools/build/export_paper.sh:69-78`), and `docs/` is excluded from the deposit (`tools/build/export_paper.sh:36`) under the 2026-07-16 deposit-scope ruling, so an image link from METHODOLOGY.md into `docs/figures/` would ship broken in the Zenodo deposit. The METHODOLOGY.md embed is staged for the owner (see `U6-notes.md`, "Staged for the owner").
- **No repository-map image.** `README.md` section "Repository map" is the canonical linked table; the figure was dropped in the recovery pass.

## 1. Review method

At the first U5 marker in `README.md`, section "How the review was built" (`<!-- U6-FIGURE: review-method ... -->`, line 13 on 2026-11-17), replacing the marker.

```markdown
[![Flow of the two routes into the corpus: 400 database records narrowed to 40, of which an appraisal gate refused 14, while the curation arm built most of the corpus by reading; both then pass through tiering before entering the bibliography.](docs/figures/review-method.png)](docs/figures/review-method.svg)

*Figure: how a source reaches the corpus. Numbers are from the July 2026 search run (`methods/PRISMA-RETRO-RUN-2026-07-13.md`) and its appraisal record (`methods/prisma-appraisal-2026-07-13.json`); live corpus counts are in "Corpus at a glance", derived by `scripts/count_reconcile.py`.*
```

## 2. Evidence tiers

At the second U5 marker in `README.md`, section "How evidence is tiered" (`<!-- U6-FIGURE: evidence-tiers ... -->`, line 31 on 2026-11-17), replacing the marker.

```markdown
[![Evidence levels A to D: Level A is peer review and official standards only, a highlighted line marks that no production evidence sits above it, Level B is practice and production evidence, Level C is unmeasured vendor material kept with its bias flagged, and Level D is excluded.](docs/figures/evidence-tiers.png)](docs/figures/evidence-tiers.svg)

*Figure: the four evidence levels as METHODOLOGY.md section 3.1 defines them. The share of the corpus at each level changes as entries are added, so it stays in the text.*
```

The README already carries a tier table directly under this marker (`README.md:35-40`), and showing the figure above a table with the same "What qualifies" column puts the same content on the page twice, where the two can drift. The default here is to embed the figure and cut the table to its `Level` and `How it is used` columns, because the figure carries the qualifying rules and METHODOLOGY.md section 3.1 stays canonical. If the main session would rather keep the full table, skip the figure in README.md instead; either way only one of the two should list what qualifies.

## Before pasting

- If a U2 or U5 edit has moved the README markers, anchor on the marker comment rather than the line number.
- `count_reconcile.py` gates the README count lines; the snippets add no count, so no ALLOWLIST change is needed.
