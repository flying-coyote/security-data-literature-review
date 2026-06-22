---
repo: security-data-literature-review
date: 2026-06-21
source: WF-C intent self-audit
evidence-tier: B
method: intent-alignment-audit.md (9-question portable bank) + AUDIT-CONTEXT.md signal routing
---

# Intent self-audit — security-data-literature-review (2026-06-21)

This is the "why" pass, not a presence/absence audit. For each load-bearing mechanism I asked
whether it still matches the reason it was added, and re-derived the actual state from the current
tree rather than recalling what the docs claim. The repo is in genuinely good health on the thing
that matters most — provenance integrity after a fabrication scare — so most of what follows is
drift between the working corpus and the documents that describe it, plus one real loop-without-rethink.

## What this repo is FOR (Q1 — Goal)

One sentence: it is the public, evidence-tiered literature review that is the **source of truth**
for the citations under the book (*Modular Open Architecture for Cybersecurity Data*),
securitydataworks.com's `/writing` + `/research` claims, and the hypothesis tracker — every external
claim the program makes is supposed to trace back here. That intent is stated consistently in the
README executive summary (`README.md:3`, `:12`), `.claude/CLAUDE.md:1-13`, and
`REPOSITORY-STATUS.md` purpose line. The goal is written down and stable; this is not an
`intent-undocumented` repo.

The sharper version of the goal, learned the hard way in June 2026: the review's value is *provenance*,
not volume. The 2026-06-05 validation pass found the original 2025-10-15 bulk-generated corpus had
"systematically stapled specific numbers onto sources that don't contain them" (`RESEARCH-JOURNAL.md:43-46`)
— 9 FABRICATED entries removed, ~35 MISMATCH, ~22 WEAK-SOURCE. So the real job now is *defending the
chain of custody on every claim*, and the repo has built the right instrument for that:
`RESEARCH-JOURNAL.md` is an append-only, externally-re-checkable validation ledger with a defined
method/verdict vocabulary (`:24-31`), and the cleanup worklist lives in the private
`project1/FABRICATIONS-REGISTER-2026-06.md`. That is the strongest part of this repo and it should
not be touched except to extend it.

## Self-model accuracy (Q2) — the biggest live gap

The repo's description of itself has drifted from the corpus on disk, and the README is the worst offender.

- **Live count vs claimed count.** `grep -c "^#### " MASTER-BIBLIOGRAPHY.md` returns **160** entries
  today; `grep -c '**Evidence Level**: A'` returns **73**, i.e. **45.6% Level A**.
  - `README.md:15,39` claims **146 sources / ~46% A (67/146)**.
  - `.claude/CLAUDE.md:12` claims **144 sources / ~47% A (67/144)**.
  - `README.md:190-198` ("Quality Metrics, Updated November 2025") still asserts **78% Level A (65/83)**
    and **"Evidence Level C/D: 0%"** — a self-reported figure the 2026-06-05 audit explicitly retired.
  - The live SessionStart hook already computes the count correctly (`.claude/hooks/SessionStart.sh:27`
    greps `^#### `), and the weekly check recomputes Level-A live, so the *mechanisms* are honest — it's
    the *prose* that lags. This is the `generated-vs-hand-maintained` drift the intent doc's Q2
    promotion rule names: point the prose at the live number instead of restating a count.
- **README still describes the retired world.** `README.md` repeatedly frames Substack / "Security Data
  Commons (3x/week)" as the PRIMARY driver and live integration (`:141`, `:151-155`, `:219`), and lists
  "Q1 2026 Deep Dive active (January)" as the current priority (`:18-27`) — six months stale. The
  Substack was retired 2026-05-24; the `REVIEW-AND-PLAN-2026-06.md` and `.claude/CLAUDE.md` already know
  this, but the README never got the rewrite. A first-time reader of the public README is told a
  materially false story about how the review is maintained and how fresh it is.
- **Two self-describing docs disagree on hypotheses.** `.claude/CLAUDE.md:12` flags it directly:
  "7 (needs review)", and notes "3 strongly validated / 6 proposed" in the Oct-2025 gap analysis vs
  "31 validated" cited in `REVIEW-AND-PLAN-2026-06.md:112`. The validated-hypothesis count is
  unreconciled across surfaces and is honestly labelled as such — good — but unresolved.

None of these is a wrong *mechanism*; each is a self-description that the corpus outgrew. The fix is a
single README rewrite pass that (a) deletes the Nov-2025 "78%/0% C-D" quality block, (b) replaces every
hardcoded count with a pointer to the live SessionStart number, and (c) rewrites the integration section
to securitydataworks.com `/writing` + `/research` + the Lab, dropping Substack-as-primary.

## Does it run loops / automation, and where is its RETHINK? (Q3/Q4 — the real finding)

**Yes — and this is the one place the repo has a strong-Act / stale-Orient problem.**

A live cloud routine runs the weekly health check: `trig_01XkVDZSc4nyMiUT5p7Ft2zr`, cron `33 12 * * 1`
(Mondays ~08:33 EDT), read-only tools, against `main`, first run 2026-06-08 (`scripts/SCHEDULING.md:55-59`).
The autonomy boundary is set correctly (Q4): the routine is **read-only and NOTIFY-only** — it
"only DECIDES and NOTIFIES; it never edits the bibliography" (`weekly_scheduled_check.py:13-15`), and a
real refresh is the supervised `/monthly-update`. For a source-of-truth artifact that is exactly the
right rung — unattended web-research edits to the SoT are correctly forbidden. No complaint there.

The problem is the **escalation gate has no RETHINK step and is wired to fire RED every single week,
permanently, by design**. `weekly_scheduled_check.py:31-38` documents that `TIER_A_FLOOR = 60%` is
"BREACHED on purpose" because real Level-A is ~46%, "so the floor is currently BREACHED on purpose:
46% < 60% correctly escalates every run until the freshness sweep ... restore[s] genuine Tier-A quality."
The comment is honest and the reasoning was sound at the time, but the consequence is that the loop
emits `VERDICT: ESCALATE` on **every** run with the same reason, indefinitely. That is precisely the
failure mode the intent-alignment doc warns about: a strong Act leg (the routine fires weekly, forever)
driving on a stale Orient — an escalation signal that means "refresh due" every week stops carrying
information, and "🔧 ESCALATE — run /monthly-update" becomes wallpaper a human learns to ignore. An
alert that is always on is an alert nobody reads, which is the same dynamic that let the *previous*
96-day lapse stay invisible behind a dashboard that "couldn't go red" (`REVIEW-AND-PLAN-2026-06.md:31-36`).

There is **no instrument that re-asks whether the weekly cadence is still the right cadence**, or
whether a permanently-RED floor is still the right gate. The loop verifies "is the corpus below the
floor" (always yes); nothing verifies "is firing this identical escalation every week still useful, or
should the gate be re-derived now that the sweep has partly landed." That is the `loop-without-rethink`
signal: looping primitive present (`harness-scheduled-agent` analogue via the cloud routine), no
goal-re-check instrument behind it.

The fix is small and matches the loop-engineering RETHINK pattern: make the escalation gate
**state-aware instead of level-only** — escalate on a *delta* (Level-A fell since last run, a new broken
link appeared, freshness regressed) plus the genuine monthly window, and treat "still below the 60%
floor but recovering on trend" as a tracked-but-not-re-alerted condition rather than a fresh RED every
Monday. Equivalently: add a quarterly re-derive step that re-decides the floor and the cadence against
the current corpus, so "permanently breached on purpose" can't quietly outlive the sweep that justified it.

## Where this repo is most likely WRONG (Q5)

The most load-bearing belief is that **the freshness sweep was completed**. `REVIEW-AND-PLAN-2026-06.md:108`
marks task #66 done — "Every >12mo entry now carries a 2026-06-05 validation or freshness marker" — but
the same line concedes "deeper per-source content re-verification of the remaining stale corpus is the
multi-session continuation." So a freshness *marker* was applied broadly, but the *content* re-verification
that the marker implies was not finished. The risk: a reader (or a downstream book/website claim) treats
a 2026-06-05 freshness stamp as "this source was re-read and still supports the claim" when in many cases
it means "this entry was touched during the sweep." After a fabrication scare, the gap between "stamped"
and "re-verified" is exactly the gap that let stapled-on numbers survive the first time. The falsifier:
sample 10 stale-but-stamped entries and claim↔source-check them; if more than one or two are MISMATCH,
the marker is over-claiming and should be downgraded to "touched, not re-verified."

## The one constraint (Q6)

Integration, not internal quality. The corpus is now provenance-clean and the loop fires; what it does
*not* yet do is reach the surfaces it exists to serve. `REVIEW-AND-PLAN-2026-06.md:112` records two
still-open propagation gaps: (1) securitydataworks.com `/research/methodology.astro:85` has **zero links
to this public repo** despite being the natural anchor for the evidence base, and (2) project1's own
`01-knowledge-base/MASTER-BIBLIOGRAPHY.md` is still a divergent ~8-month-stale second bibliography rather
than a pointer to this SoT. A source of truth that nothing links to isn't yet functioning as a source of
truth. Every doc-count fix is downstream of this — the count only matters once a reader can reach it.

## Bus-factor (Q9)

Single maintainer (Jeremy), which is expected for a personal research repo and not itself the finding.
The fragile part is **the validation discipline lives in one person's practice, not in an enforced gate**.
The `RESEARCH-JOURNAL.md` method/verdict vocabulary and the "append a dated row, don't silently re-validate"
rule (`:18-21`) are the thing that prevents a fabrication relapse — and they are followed by hand. There
is a `PreCommit.sh` hook and an OKF type-registry discipline, but nothing mechanically checks that a new
`#### ` bibliography entry carries a `**Validation Status**` line tied to a journal row before it can be
committed. The highest-leverage bus-factor reduction is to promote that one invariant into the pre-commit
hook: block a commit that adds a bibliography entry with no validation-status field. That moves
"the maintainer remembers to log provenance" (the exact thing whose *absence* caused the 2025-10 fabrication)
to "the commit blocks," per the Q9 promotion rule.

## Dead weight (archive or kill)

- **`README.md` Nov-2025 quality block and Substack-primary integration narrative** (`:18-27`, `:74-167`,
  `:189-219`) — not just stale, actively misleading on the public face of the repo. Rewrite, don't archive.
- **`scripts/automation_dashboard.py` static integration lines** — the June-5 honesty fix corrected the
  worst line (it now notes "Security Data Commons Substack retired ... do not poll it", `:226`), but the
  surrounding block still prints hardcoded `✅ ACTIVE` / `✅ OPERATIONAL` / "~90 vendors, 84% Tier A"
  (`:207-234`) rather than computing them. The dashboard's only live numbers are the broken-link / outdated
  counts it scrapes from a health report (`:123-124,202`). It half-can't-go-red still. Either finish the
  live-compute or retire the integration section; a dashboard that prints "ACTIVE" unconditionally is the
  same fiction that hid the last lapse, just quieter.
- **`PROJECT-PLAN-2026-Q1.md` and `LITERATURE-EXTRACTION-PLAN.md`** — Q1-2026 / Nov-2025 dated planning
  docs the program has moved past; candidates for `archive/` alongside the existing `ARCHIVED-COMPLETED-PHASES.md`.
- **Dual `main` + `master` branches** — the routine runs against `main`, but the repo carries both plus
  `lit-review-revival-2026-06` and `local-wip-2026-06-05`. Worth confirming which is canonical so the
  scheduled routine and any reader are looking at the same tree. (Verify — do not touch; the main session owns git.)
- **`monthly-update-workflow-verification.md`** set a "February 2026 decision point" that has been
  superseded by the `SCHEDULING.md` weekly-routine decision; it's historical now.

## What is genuinely fine (do not re-flag)

- The provenance recovery is exemplary: append-only journal, defined verdict vocabulary, fabrications
  quarantined to a private register, public repo kept clean. This is the model other repos should copy.
- The autonomy boundary on the loop is correct: read-only, notify-only, no unattended edits to the SoT.
- The honest live-recompute in `SessionStart.sh` and `weekly_scheduled_check.py` (counting `#### ` and
  `**Evidence Level**: A` rather than trusting a header) is the right pattern; the prose just needs to
  defer to it.
- The `TIER_A_FLOOR` comment explicitly forbidding lowering the floor to silence a real breach is good
  discipline — the fix is to make the gate delta-aware, not to weaken the floor.

## Top 3 actions (ranked)

1. **Add a RETHINK / delta-aware escalation to the weekly loop** so it stops emitting an identical RED
   every Monday — escalate on regression + the monthly window, track "below-floor-but-recovering"
   without re-alerting, and add a quarterly re-derive of the floor/cadence. (Q3/Q4, `loop-without-rethink`.)
2. **Rewrite the public README** to the live self-model: delete the Nov-2025 "78%/0% C-D" quality block,
   replace hardcoded counts with the live SessionStart number, and rewrite the integration section off
   Substack onto securitydataworks.com + Lab. (Q2.)
3. **Promote the provenance invariant into the pre-commit hook** — block a new bibliography entry that
   lacks a validation-status line tied to a journal row — so a fabrication relapse can't pass through one
   person forgetting. (Q9.)
