# Literature review: state-of-the-repo review + update/integration plan (2026-06-05)

This is the periodically-updated literature review that's meant to be the evidence source of truth under
the book, the website's claims, and the hypothesis tracker. It was last updated 2026-02-28 (v1.21.0), so
the cadence has been dark for ~96 days, and the review below is what I found when I came back to it. The
plan at the end is phased, and the three decisions it needs from Jeremy are called out explicitly.

## What I found

### The update mechanism works as a script but nothing drives it
The monthly update is a manual checklist (`.claude/commands/monthly-update.md`) that a person runs in a
session — there is no scheduler behind it, so when nobody ran it, it simply stopped. The workflow's own
verification doc set a "February 2026 decision point" to choose monthly / bi-monthly / quarterly, and the
last update is February, so it lapsed at exactly the point where the experiment was supposed to be
re-decided. The two automation scripts still run clean (`weekly_health_check.py` and
`automation_dashboard.py`, both exit 0).

### The content has gone stale, and the freshness collapse is the real problem
The health check on 2026-06-05 reports 109 sources, **5 of 10 sampled links broken** (Uber 404, a Netflix
post, two Confluent/Ververica 404s), and **92 of 109 sources older than 12 months**. Evidence Level A is
still ~80% (above the 75% target), so the *quality tier* held, but the *freshness* did not — link rot at a
50% sample rate and 84% of sources over a year old is the headline.

### The dashboard reports fiction, which is how the lapse stayed invisible
`automation_dashboard.py` printed `Broken Links: 0 | Outdated Sources: 0` and
`Blog (security-data-commons-blog): ✅ ACTIVE` in the same run where the health check found 5/10 broken and
where the Substack has been retired since 2026-05-24. The dashboard is echoing hardcoded/cached numbers from
the tracker docs rather than computing live, so it always looks green — that's a big part of why a 96-day
lapse didn't surface. This is a mechanism bug, not just stale data.

### Integration is the weakest link: two bibliographies, and counts that don't agree
- There are **two** `MASTER-BIBLIOGRAPHY.md` files: this repo's (140 KB, ~109 sources, Feb-stale) and
  `~/project1/01-knowledge-base/MASTER-BIBLIOGRAPHY.md`, which the project1 doc-coherence triage already
  flagged as last updated 2025-10-15 (~8 months stale, "likely missing all citations from the 2025-12
  validation marathon and 2026 research passes"). They've diverged and neither is marked canonical.
- The **source count disagrees with itself** across every surface that cites it: 75+ (book about-the-author),
  83 (Nov verification), 109 (live link-parse), 115+ (project1 training docs), 124 (dashboard "entries").
- The **website has zero links to the lit review**, even though `/research/methodology` exists and is
  exactly where the SLR/methodology should be anchored. The book's about-the-author still says
  "75+ sources, 73% Evidence Level A" — both numbers wrong now.
- Two checklist **inputs are dead**: step 3 ("Review External Inputs") tells the updater to read Substack
  comments and blog feedback from Security Data Commons, which no longer exists.

## The plan

### Phase 1 — make the mechanism honest and schedulable (bounded; one decision)
- Fix the dead Substack inputs in `monthly-update.md` step 3 → securitydataworks.com (/writing feedback,
  LinkedIn, the Lab benchmarks as a new internal input).
- Fix `automation_dashboard.py` so it computes broken-link and outdated-source counts live (or calls the
  health check) instead of echoing zeros, and drop the "Blog ACTIVE / Security Data Commons" integration
  line. A dashboard that can't go red is worse than no dashboard.
- Pick one canonical source count and reconcile every surface to it (see Phase 2).
- **DECISION 1 (Jeremy, 2026-06-05) = weekly + scheduled agent.** Wire a recurring scheduled agent
  (`/schedule`) that runs `weekly_health_check.py` weekly and opens the update so a lapse becomes a
  notification instead of silence. Weekly is aggressive — the agent should do the light weekly pass (link
  health + flag new sources) and escalate to a fuller refresh when the health check goes red, rather than a
  full ~7h update every week. (task #64)

### Phase 2 — fix integration / pick a source of truth (DECIDED: merge-first, repo = SoT)
- **DECISION 2 (Jeremy, 2026-06-05) = merge first, then this repo is SoT.** ✅ project1 → repo literature
  merge DONE (commit d8a35a4): 22 published works folded in (D3FEND + ontology, MITRE ATLAS, Matryoshka,
  F3/SIGMOD, Zeek, Power Query M, SCF, NIST CSF, CoSAI, Ballista, Lakekeeper, + practitioner pubs).
- **Public/private boundary (Jeremy, 2026-06-05).** This repo is PUBLIC. There's a difference between a
  *literature review* (the published work — paper/book/framework/post — which belongs here) and
  *relationship / communication-status tracking* (outreach state, availability, partnership posture, the
  "expert contact identified / active monitoring / $N investment" notes — which stays PRIVATE in project1).
  Port the literature; never the relationship status. A person's publication is fine; their comms status isn't.
- **Third merge source: the website.** securitydataworks.com `/writing` + `/research` cite **159 distinct
  external URLs**; many are tool homepages already covered, but a real citable set is not yet catalogued
  (ACM/arXiv/USENIX papers, Ryan Stillions detection-maturity blog, the CrowdStrike/SentinelOne investor
  filings behind the FSI hypothesis, NIST CSRC). Triage these 159 against the 146-entry bibliography and fold
  in the genuine sources. Sized as its own pass (see task #70).
- Reconcile the count + Level-A % to the canonical number and propagate to: book about-the-author (75+/73%
  → current ~146), project1 training docs (115+), the dashboard, the README. Make project1's bibliography a
  pointer to this repo for *literature*, while it keeps its private relationship tracking.
- Add the lit-review/methodology linkage to the website `/research/methodology` so the evidence base the
  site's claims rest on is actually reachable (the book Tier-1 re-home already points readers there).

### Phase 3 — the extensive content update (DECIDED: full freshness sweep; the big one)
- **DECISION 3 (Jeremy, 2026-06-05) = full freshness sweep of all 92 stale sources + broad new sourcing.**
  Multi-session by design.
- Fix/replace the broken links the health check found (5/10 sampled).
- Refresh all 92 stale sources, hypothesis-critical first (31 hypotheses are validated against this corpus).
- Add the March–June 2026 sources the rest of the estate already moved on without: Iceberg V3/V4 + Variant +
  DuckLake, the OCSF↔D3FEND grounding work, the economics trilogy, the agentic/NANDA/Kimball thread, Splunk
  Platform 10.4 + Cisco Data Fabric. Each classified through the evidence-tier rubric.

### Phase 4 — re-verify and prove the cadence fires
Run the health check, confirm freshness recovered and Level A held, commit in clean units, and confirm the
scheduled agent actually fires once so "periodic" is demonstrated, not assumed.

## Status (2026-06-05)
Decisions 1–3 made by Jeremy. Done so far, on branch `lit-review-revival-2026-06` (main untouched):
- ✅ Phase 1: dashboard honesty fix + dead-input fix + this plan (commit eb4c720)
- ✅ Recovered the stranded Feb-2026 bibliography refresh (commit b4d227d)
- ✅ Phase 2 merge: project1 → repo literature merge, repo is now SoT, public/private boundary held (d8a35a4)

Remaining (in order):
1. Weekly scheduled agent (task #64) — Decision 1.
2. Fix 5 broken links (task #65).
3. Full freshness sweep of all 92 stale sources (task #66) — Decision 3; multi-session.
4. Add March–June 2026 sources (task #67).
5. Website-citation merge — triage 159 external URLs, fold in the genuine sources (task #70).
6. Propagate canonical count + website /research linkage + make project1's a literature-pointer (task #68).
7. Re-verify health check, confirm freshness recovered + schedule fires, commit (task #69).
