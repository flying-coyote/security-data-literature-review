---
type: operating-doc
title: "Evidence Quality Validation Checklist"
created: 2026-01-02
updated: 2026-11-17
tags: [literature-review, evidence-tiers, bibliography, quality-assurance, hypothesis-coverage]
---

# Validate evidence quality

Check that the bibliography's tiers, verification records and hypothesis coverage are honest. There is no Level-A share target to hit: the share targets were retired by owner ruling 2026-08-19 (METHODOLOGY §8.1a), and the share is reported as a description of where evidence in this field lives.

## 1. Counts and gates

```bash
python3 scripts/count_reconcile.py           # blocks, tiered entries, A/B/C split, hypothesis count; every gated surface
python3 scripts/derive_source_taxonomy.py --check
python3 scripts/automation_dashboard.py      # dashboard view, freshness, health-report summary
```

## 2. Tier accuracy

Sample entries at each level and check them against METHODOLOGY §3.1:

- Level A holds only peer-reviewed research at a confirmed venue, standards-body documents, formal open-standard specifications and the MITRE D3FEND / ATLAS frameworks.
- Production case studies, engineering blogs, talks, analyst reports, project documentation and venue-less preprints are Level B.
- Level C entries carry a bias flag and never carry a hypothesis alone.
- Proposed tier changes are staged for the owner (they change the gated counts and the taxonomy), never applied directly.

## 3. Hypothesis coverage

For each hypothesis in PUBLICATION-MANUSCRIPT.md §3.7, list its scoreable legs under `methods/scoring-rubric.md` §1 (catalogued, and either survived primary-source verification or not yet challenged) and check the manuscript cites each. A hypothesis with no scoreable leg sits at the instrument floor of 5/25; say so rather than padding it.

## 4. Verification records

Every number in a `**Key Findings**` line needs a primary named with a locator, and a `**Validation Status**` mark is only honest when that is true. Flag entries where the mark sits over a number with no named primary; log verdicts in RESEARCH-JOURNAL.md.

## 5. Freshness and links

```bash
python3 scripts/weekly_health_check.py   # samples links, flags sources older than 12 months
python3 scripts/link_check.py            # every bibliography URL, report under methods/
```

Sources the health check flags (older than 12 months) that still carry a cited claim: refresh or find a newer primary. Dead links: repoint to the archived copy with a dated note, or mark the entry.

## Report

```markdown
## Evidence validation report: [DATE]

- Gate output: [paste the first two lines of count_reconcile.py]
- Tier spot-check: [N sampled, N mis-tiered, staged changes]
- Hypotheses with no scoreable leg: [list]
- Numbers without a named primary: [list with line numbers]
- Freshness: [counts from the health check]
- Actions: [list]
```
