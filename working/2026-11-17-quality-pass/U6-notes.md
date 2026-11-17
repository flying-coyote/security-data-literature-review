# U6-diagrams: notes (2026-11-17)

## Prose-or-visual judgement

The visual-necessity ladder was run on each candidate before anything was drawn.

- **Review method.** Rung 2 found an existing visual, `publication-graphics/figure1_prisma_flowchart.tex`, which is the full PRISMA 2020 two-arm diagram for the paper. It stays the figure of record for the manuscript, but it is a dense TikZ page at print size, it is embedded nowhere in the Markdown front pages, and its closing box carries a corpus count that has drifted (below). Rung 3 fires for the front pages, because the method is a sequence with numbers a reader compares (400 to 395 to 40 to 26), and METHODOLOGY.md section 2 currently spends three dense paragraphs on it. Verdict: a simpler overview figure for README.md and METHODOLOGY.md, with the PRISMA figure left as the paper's version.
- **Evidence tiers.** Rung 3 fires: an ordered ladder with one boundary that matters (production evidence stops at B), and the prose in METHODOLOGY.md section 3.1 buries that boundary under status notes. Verdict: figure, with no corpus percentages so it does not go stale.
- **Repository map.** Rung 3 is weaker here, because the content is a lookup list (question to file), and in a GitHub README a linked Markdown table does that job better: clickable, searchable and updated in the same commit as the files it names. Verdict, revised in the recovery pass: no image. `README.md` section "Repository map" already carries the fuller linked table, and no off-GitHub use for an image was named, so the map figure was dropped.

## Design decisions

- One focal element per figure, in the Diagram standard's azure (`#1f8fe0`): the appraisal gate and the A/B boundary. The gate's refusal breakdown sits on a light inset in dark ink so it keeps body-text contrast at phone scale. Everything else stays in the slate-blue tints and neutrals.
- The method figure prints only frozen-record numbers from the July 2026 run and its appraisal files, and names `scripts/count_reconcile.py` for live counts instead of drawing a corpus total, so a future admission does not make the image wrong.
- The step "carried numbers checked at the primary" is drawn dashed and titled "Rule:", with its subtitle pointing at the per-number verdicts in `methods/verification-2026-11/ledger.json` (PUBLICATION-MANUSCRIPT.md:444, :1052). It is a standing rule, not a completion claim: U1's ledger records 43 unverifiable-paywall, 30 not-in-source and 5 unverifiable-no-primary number verdicts (`U1-notes.md:17`).
- Labels sit at 24 to 42 px on a 1080 px canvas. The glance-check floor for a 1080 px image is about 32 px, which the titles, stage names and focal text meet; the 26 to 29 px detail lines sit under it, and on the 375 px phone view they are small but readable, and the message of each figure survives without them.

## Found in passing, for other units (not edited)

1. *Resolved by U2/U4.* The stale Level A examples ("Peer-reviewed academic publications", "Government/standards body publications (CISA, MITRE, ...)") are gone; `METHODOLOGY.md:109-113` now carries the corrected list.
2. *Resolved by U2.* `PUBLICATION-MANUSCRIPT.md:211-212` now lists peer review and standards under Level A, with B and C at the live 170 and 40 of 271.
3. `publication-graphics/figure1_prisma_flowchart.tex:178`, "n = 228": this is the as-of-run convergence that U2 kept on purpose (`U2-changelog.md:7`, "convergence box arithmetic fixed (201 + 27 = 228)", caption and alt text bridged to 273/271), so it should not be regenerated from the live count. The only open question is whether `scripts/count_reconcile.py` should gate the caption bridge so the live figure in the caption cannot drift.
4. Still open: `METHODOLOGY.md:96` says the two remaining refusals were "refused on other appraisal grounds", while `PUBLICATION-MANUSCRIPT.md:184` says they went to "an independent verification pass ... a second LLM agent". The appraisal records (ranks 5 and 31, `methods/prisma-appraisal-2026-07-13.json:186`, `:1171`) support the manuscript, and the figure uses the manuscript's wording ("refuted by an independent verification pass").
5. `README.md:13` and `:31` (U5 markers) and `U5-notes.md:9` name `docs/figures/EMBED.md`, which moved to `working/2026-11-17-quality-pass/U6-embed.md` in the recovery pass. The markers are replaced at integration, so nothing needs editing if the main session pastes from the new path.

## Staged for the owner

1. Embedding the two figures in `METHODOLOGY.md` (after the opening paragraph of section 2, and after the line-104 paragraph in section 3.1). METHODOLOGY.md ships in the deposit (`tools/build/export_paper.sh:69-78`) and `docs/` does not (`:36`), under the 2026-07-16 deposit-scope ruling, so the embed needs a whitelist addition of `docs/figures/review-method.png` and `docs/figures/evidence-tiers.png`. Default: add the two PNGs, since they carry only frozen-record numbers and no live count. Until ruled, the figures go in README.md only.

## Left undone

- The snippets in `working/2026-11-17-quality-pass/U6-embed.md` are not inserted; the main session pastes them at the two README markers at integration.
- No DM Sans on the build machine, so the committed PNGs render in Liberation Sans. If the figures should match the site's typeface, re-render on a machine with DM Sans installed.
