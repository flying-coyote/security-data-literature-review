---
type: operating-doc
title: "Quarterly Literature Review Deep-Dive Workflow"
created: 2026-01-02
updated: 2026-11-17
tags: [literature-review, quarterly-cadence, hypothesis-validation, evidence-synthesis]
---

# Quarterly deep dive

Run once a quarter (January, April, July, October), roughly 24 hours across the quarter. Counts are never typed into this checklist or into a tag message by hand; they come from `python3 scripts/count_reconcile.py` at the time of the run.

## Phase 1: expert input (owner-run)

Expert interviews involve contacting named people, so the owner decides whether any happen this quarter and runs them. The prepared guides are records in `working/expert-interviews/` (index: `working/README.md`), and each carries a refresh-before-scheduling banner naming figures that must not be quoted. A session can prepare a refreshed context section from the current bibliography for the owner to review; it does not schedule or send anything.

## Phase 2: hypothesis review (6-8 hours)

1. Run `python3 scripts/count_reconcile.py` and `python3 scripts/automation_dashboard.py`.
2. For each hypothesis in PUBLICATION-MANUSCRIPT.md §3.7, list what changed in its legs this quarter: new primaries catalogued, legs withdrawn, numbers re-verified.
3. Re-run the scoring instrument (`methods/scoring-rubric.md`) for any hypothesis whose evidentiary basis changed. A score change is staged for the owner with the rubric arithmetic shown, not applied.
4. Record research-question coverage against the roster (RQ1-RQ4 in PUBLICATION-MANUSCRIPT.md §1; RQ7-RQ10 in METHODOLOGY.md §5.4; RQ11-RQ17 in LITERATURE-HYPOTHESIS-GAP-ANALYSIS.md Gaps 11 and 12; RQ5 and RQ6 have no current definition, pending an owner ruling), noting which remain unvalidated.

## Phase 3: evidence synthesis and quality (4-6 hours)

- Review the quarter's CHANGELOG.md [Unreleased] entries and the RESEARCH-JOURNAL.md verdicts they produced.
- Run `python3 scripts/weekly_health_check.py` and `python3 scripts/link_check.py`; fix or mark broken links (dated note, archive URL where one exists).
- Refresh the sources the health check flags (older than 12 months) that still carry a cited claim.
- Re-check each tier against METHODOLOGY §3.1 where a source's status changed (a preprint reaching a venue, a page moving behind a paywall). Tier changes are staged, not applied.
- Regenerate the vendor landscape and run `python3 scripts/derive_vendor_rollups.py --check`.

## Phase 4: versioned snapshot (2-3 hours)

1. Gates green: `count_reconcile.py`, `derive_source_taxonomy.py --check`, `derive_vendor_rollups.py --check`, `validate_metadata.py`, `repoint_moved_paths.py --check`.
2. Fold [Unreleased] into a numbered CHANGELOG.md release.
3. Tag `YYYY-QX-v1.0` (the ruled convention, docs/ZENODO-RELEASE-CHECKLIST.md Step 0; for the first deposit, Step 0 re-tags `2026-Q3-v1.0` at the release-ready HEAD, or falls back to `2026-Q3-v1.1`). Write the tag message from the gate output rather than from memory:

```bash
f="$(mktemp)"
python3 scripts/count_reconcile.py | sed -n '1,2p' > "$f"
git tag -a YYYY-QX-v1.0 -F "$f"   # owner creates and pushes the tag
```

Tagging and any Zenodo deposit stay with the owner.

## Phase 5: quarterly synthesis (optional, owner decides)

A short synthesis for securitydataworks.com/writing, drafted for the owner's review: what entered the corpus, which hypotheses moved and why, and what the next quarter will look for. Drafts go through the publish gate before anything is posted (the Security Data Commons Substack was retired 2026-05-24).

## Done when

- [ ] Gates green
- [ ] Hypothesis changes staged with rubric arithmetic, or "no change" recorded
- [ ] CHANGELOG.md release written
- [ ] Tag prepared for the owner
- [ ] Next quarter's evidence gaps listed in monthly-update-tracker.md
