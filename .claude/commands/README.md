# Custom slash commands

**Project**: security-data-literature-review
**Last updated**: 2026-11-17

| Command | When | What it does |
|---------|------|--------------|
| `/monthly-update` | monthly, or when the weekly check escalates (`scripts/SCHEDULING.md`) | health check, new sources with tiers, refresh of stale sources, link repair, CHANGELOG entry |
| `/add-source` | whenever a source is added | metadata, Evidence Level under METHODOLOGY §3.1, entry format, gates |
| `/validate-evidence` | during monthly updates or when quality is in doubt | gates, tier spot-check, hypothesis coverage, verification records, freshness |
| `/quarterly-deep-dive` | January, April, July, October | hypothesis review under the scoring rubric, synthesis, vendor regeneration, versioned snapshot |

Counts never live in these files. They come from `python3 scripts/count_reconcile.py`, and the Level-A share is a description rather than a target (METHODOLOGY §8.1a). Anything that contacts a person, changes a tier or score, or pushes a tag is staged for the owner.
