---
type: proposal
title: "Hypothesis confidence re-score proposal — post-audit (2026-07-09)"
created: 2026-07-09
status: ADOPTED (owner "Apply", 2026-07-09) — applied to §2.5/§3.7/Tables 1-2/Figures 2+4 same day
tags: [hypotheses, confidence-scoring, audit, rescore]
---

# Confidence re-score proposal — the 7 manuscript hypotheses, post-audit

**Why**: every confidence score in PUBLICATION-MANUSCRIPT.md (§2.5, §3.7, Table 2, Figure 4) is still labeled "pre-audit," and §3.7's own note promises re-scoring. The 2026-06 audit and the 2026-07 verification sweep (33-item fix pass, applied at 397d00a/1e14b4b/c11d775) changed the evidence under four of the seven, so the pre-audit stars now overstate them. This proposal walks the rubric (source count / evidence quality / source diversity / quantitative precision / geographic-organizational diversity, 5 points each) against the post-fix evidence state.

**Rule applied**: a hypothesis scores on evidence that has survived primary-source verification or has not yet been challenged; withdrawn legs score zero; suspect-flagged legs (named in the 2026-06 audit as fabricated-or-dead in this repo's own copies) score zero until re-verified.

| Hypothesis | Pre-audit | Proposed | Stars | What changed |
|---|---|---|---|---|
| H-ARCH-01 (Iceberg dominance) | 23/25 ⭐⭐⭐⭐⭐ | **23/25 CONFIRM** | ⭐⭐⭐⭐⭐ | All four legs survived; two strengthened (contributor count now GitHub-derived with as-of date; SK Telecom figures verified verbatim in the Trino Summit slides PDF) |
| H3-PERFORMANCE-01 (ClickHouse) | 21/25 ⭐⭐⭐⭐ | **20/25** | ⭐⭐⭐⭐ | Cloudflare figures verbatim-verified; CH-vs-ES corrected *upward* to 12-19×; losses are the Shell entry (2026-06) and the withdrawn query-perf multiplier — source count −1, precision better-anchored |
| H-STREAM-01 (stateful streaming) | 17/25 ⭐⭐⭐⭐ | **17/25 HOLD** | ⭐⭐⭐⭐ | Composition improved, total unchanged: peer-reviewed Samza VLDB 2017 leg (verified verbatim) replaces the orphaned Kafka-Streams claim; Azure figures verbatim-verified; Uber figures remain withdrawn from this hypothesis (2026-06) |
| H-IMPL-01 (streaming TCO premium) | 22/25 ⭐⭐⭐⭐ | **6/25** | ⭐⭐ PRELIMINARY | DORA fabricated (0 matches in report PDF); TEI 39/32/29 in neither TEI document; IDC leg flagged fabricated-or-dead by the 2026-06 audit. Zero quantitative support survives; direction supported by practitioner experience only |
| H-IMPL-02 (staffing/skills scarcity) | 23/25 ⭐⭐⭐⭐⭐ | **7/25** | ⭐⭐ PRELIMINARY | The DORA bundle (2.7×, Level-4 taxonomy, 3.2× incidents) is fabricated attribution; no quantified leg survives *in this corpus*. Restoration path: verify + catalogue the Gartner Market Guide "<15% streaming expertise" (currently cited only in the project1 hypothesis file, unverified) — would lift toward ⭐⭐⭐ |
| H-IMPL-03 (timeline premium) | 13/25 ⭐⭐⭐ | **7/25** | ⭐⭐ PRELIMINARY | Already the weakest pre-audit; average-timeline figure withdrawn 2026-06, Gartner proficiency attribution withdrawn 2026-07. The security-specific-constraints reasoning (compliance gates, tool integrations, rule migration) stands but is unquantified |
| H-COST-09 (tiered-storage savings) | 19/25 ⭐⭐⭐⭐⭐ | **8/25** | ⭐⭐ PRELIMINARY | Savings band withdrawn 2026-06; the 70%/<5% access split now labeled illustrative (2026-07). Mechanism is well-documented (Confluent tiered-storage docs, Level B) but no quantified savings source survives. Restoration path: derive tier-price bounds from public S3 Standard/IA/Glacier pricing, labeled first-party. **Restoration executed 2026-07-09**: live US-East-1 list prices fetched and derived — IA 45.7% / Glacier Instant 82.6% / Flexible 84.3% / Deep Archive 95.7% cheaper than Standard per GB-month (price-floor bounds, pre-retrieval-fees; now in §3.3.2 and the bibliography). Quantitative-precision dimension recovers on the next re-score pass |

## Knock-on effects if adopted (all in the manuscript)

- §3.7 tier headings change shape: **1 strongly validated** (H-ARCH-01), **2 high confidence** (H3-PERFORMANCE-01, H-STREAM-01), **4 preliminary** (H-IMPL-01/02/03, H-COST-09). The current "3/3/1" split dissolves.
- §2.5 Phase-1 results list, Table 2, and Figure 4 need the same re-grouping; Figures 1-2 evidence-level percentages regenerate from the dashboard's live Level-A computation (42.9% at 2026-07-09 — honest figure, below the 75% target, already flagged in the repo).
- The abstract's "Seven hypotheses were assessed" framing survives unchanged — it already states the withdrawn findings directionally.
- Honest framing for the paper: the review's *architecture and performance* findings are validated at high confidence on primary-verified production evidence; its *organizational-cost* findings are directional practitioner claims awaiting real sources. That split is the paper's true post-audit contribution shape, and arguably a cleaner story than the pre-audit uniform strength.

## What this proposal does NOT do

Nothing is applied. Owner adjudicates the seven proposed scores (especially the four PRELIMINARY downgrades); on sign-off the apply pass edits §2.5/§3.7/Table 2/Figure 4 in one commit with a CHANGELOG entry, and the project1 tracker mirrors (H-IMPL-01/02 already downgraded there at 5dcac5f6; H-IMPL-03 and H-COST-09 mirrors would follow).
