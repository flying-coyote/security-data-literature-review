# Claude skills for the literature review

**Last updated**: 2026-11-17

This repository ships one project skill. Any other skills a session uses come from the user's own `~/.claude/skills/` and are not part of this repository, so a fresh clone works with whatever personal skills its user has (see the [Claude Code skills documentation](https://docs.claude.com/en/docs/claude-code/skills)).

## evidence-tier-classifier

**Purpose**: give each new or reviewed source the Evidence Level that METHODOLOGY §3.1 defines (A peer-reviewed research and official standards; B practitioner and production evidence; C vendor material without production measurement, bias flagged; D excluded), with the rationale written into the entry.
**Triggers**: "source", "paper", "add citation", "evidence level", "tier", "bibliography".
**What it does not do**: aim for a Level-A share. The share targets were retired by owner ruling 2026-08-19 (METHODOLOGY §8.1a), and the live counts come from `python3 scripts/count_reconcile.py`, never from this file.

## Workflow

1. Find the source and read the claim at its primary.
2. Classify it with `evidence-tier-classifier` (or `/add-source`, which walks the same rules).
3. Add the `#### ` entry to MASTER-BIBLIOGRAPHY.md and a dated taxonomy record under `methods/`.
4. Link it to the hypotheses it bears on; confidence itself is scored with `methods/scoring-rubric.md`.
5. Run `python3 scripts/count_reconcile.py` and `python3 scripts/derive_source_taxonomy.py --check`, then add a CHANGELOG.md entry.
