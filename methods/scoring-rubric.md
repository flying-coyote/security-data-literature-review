---
type: reference
title: "Hypothesis confidence scoring rubric — the re-derivable instrument (G-R4)"
created: 2026-07-12
tags: [hypotheses, confidence-scoring, rubric, methods, oxford-jcs]
---

# Hypothesis confidence scoring rubric

**Why this file exists.** Ruling G-R4 (`STAGED-litreview-oxford-readiness-2026-07-12.md`, ratified 2026-07-12) requires that every confidence score in Figure 4 and Table 2 of PUBLICATION-MANUSCRIPT.md be re-derivable by a reviewer from a documented instrument. The instrument already existed in three partial forms — the anchor tables in `analysis-bundles/hypothesis-confidence-matrix.md` (October 2025), the manuscript's Appendix B narrative, and the survived-verification rule formalized in `RESCORE-PROPOSAL-2026-07.md` — but the arbitration rules that decide edge cases lived nowhere, which is how off-anchor values (a 4 on a dimension whose scale defines only 1, 3, and 5) and band-threshold contradictions (Figure 4's legend drew thresholds at 19/15/10 while the source bundle defines 21/16/11) entered the published surfaces. This file consolidates the instrument and makes the implicit rules explicit. Nothing here invents a new criterion; where practice was internally inconsistent, the rule below records which existing practice wins and why.

**Scope.** The nine manuscript hypotheses scored in §2.5, §3.7, Table 2, and Figure 4. The instrument re-runs whenever an audit changes a hypothesis's evidentiary basis (Appendix B's re-computation rule): a citation withdrawn, a figure re-verified, or a new primary catalogued.

## 1. What counts as a scoreable leg

A hypothesis scores only on evidence that has survived primary-source verification or has not yet been challenged (the RESCORE-PROPOSAL-2026-07 rule, adopted 2026-07-09). Specifically:

- a leg withdrawn by an audit scores zero and does not count as a source on any dimension;
- a leg flagged fabricated-or-dead by a prior audit scores zero until independently re-verified;
- a scoreable leg must be a catalogued source: a `#### ` block in MASTER-BIBLIOGRAPHY.md carrying an Evidence Level, or a first-party measurement cited in the manuscript with full provenance (script path, run date, host) — first-party legs should also be catalogued as bibliography blocks, following the AWS S3 tier-delta derivation precedent;
- the legs scored for a hypothesis are the sources its manuscript evidence section (§3.2–§3.6) actually cites for that claim. The reviewer reads the paper, so the paper's cited evidence is the scoring input; if the canonical bundle carries a leg the manuscript does not cite, that leg does not score until the manuscript cites it.

Counting rule: source count counts distinct *measurements*, not distinct bibliography blocks or distinct organizations. Two blocks documenting the same deployment story count once; two different measurements from the same organization (Cloudflare's 6M req/sec HTTP analytics and its separate ES-to-ClickHouse log-pipeline migration) count separately, because organizational concentration is already penalized by dimension 5, not dimension 1.

If a hypothesis has zero scoreable legs, every dimension takes its floor of 1, giving the instrument's minimum of 5/25. The gradations previously shown among such hypotheses (6/25 vs 7/25) were judgment calls the instrument cannot express and are retired.

## 2. The five dimensions

Each dimension is scored independently at its anchor values only. Four dimensions define anchors at 1, 3, and 5; intermediate values (2, 4) are not valid scores on those dimensions, because an interpolated value has no anchor a reviewer can re-derive it from. Evidence Level Quality is the exception: its scale is a five-band percentage table, so all of 1–5 are reachable there.

**Dimension 1 — Source count** (anchors 1/3/5):

| Scoreable legs | Points |
|---|---|
| 1–2 | 1 |
| 3 | 3 |
| 4 or more | 5 (no extra credit past 6; redundant sources add no independent confirmation) |

**Dimension 2 — Evidence Level Quality** (bands 1–5). Computed as the share of the hypothesis's scoreable legs whose MASTER-BIBLIOGRAPHY.md block is tiered `**Evidence Level**: A`. The bibliography tier label is the input of record; if a tier label is stale against the repo's own tier definitions (Appendix A), fix the bibliography entry first, then score. Two first-party sub-cases, split the way the bibliography already splits them: a first-party *lab measurement* on the MOAR reference stack counts as Level A (the canonical bundle's "measured A" convention — the run is ours, reproducible, answer-equality-gated), while a first-party *derivation from vendor-published inputs* keeps its bibliography tier (the AWS S3 tier-delta derivation is tiered B because the underlying list prices are vendor-published, and it scores as B).

| Share of legs at Level A | Points |
|---|---|
| 0–25% | 1 |
| 26–50% | 2 |
| 51–75% | 3 |
| 76–99% | 4 |
| 100% | 5 |

**Dimension 3 — Source diversity** (anchors 1/3/5). Each source is assigned exactly one primary type by publisher/venue: Government/Standards body, Industry Analyst/Survey, Production Deployment, Academic (peer-reviewed venue), or Vendor. A peer-reviewed paper carrying production data (Samza, VLDB 2017) types as Academic — the venue governs. First-party legs contribute **no** type: a first-party run cannot manufacture source diversity (the canonical bundle's own words), so it counts on dimensions 1 and 2 but not here.

| Distinct types | Points |
|---|---|
| 1 | 1 |
| 2 | 3 |
| 3 or more | 5 |

**Dimension 4 — Quantitative precision** (anchors 1/3/5). Precision attaches to the hypothesis's own claim variable, not to any number in the vicinity. A precise figure that quantifies an adjacent indicator scores as a range estimate: H-ARCH-01's surviving figures (29%-vs-23% planning intent, 407 contributors) are precise, but they quantify adoption momentum and community size, not the dominance share the claim asserts (the original 76% was withdrawn), so the dimension scores 3. A bound is likewise a 3, not a 5: the S3 tier-price deltas are exact arithmetic on list prices, but they bound the achievable saving rather than measure a realized one, and the claim is about realized cost reduction.

| Verified quantitative support for the claim variable | Points |
|---|---|
| Directional only ("costs more") | 1 |
| Range estimate, bound, or precise figure for an adjacent indicator | 3 |
| Precise measured quantification of the claim variable itself | 5 |

**Dimension 5 — Geographic/organizational diversity** (anchors 1/3/5). Counts independent evidence-producing organizations. A shared author collaboration counts once even across multiple papers (LogLite and PBC share the Ant Group / Guangzhou University / UNSW author cluster, so together they contribute one group; Pebbles's Colorado State group is the second). Our own lab contributes zero organizations. For a single study measuring one organization's environment, the studied organization is one org.

| Independent orgs/regions | Points |
|---|---|
| 1 | 1 |
| 2–3 | 3 |
| 4+ with international spread | 5 |

## 3. Bands and labels

Total = sum of the five dimensions, 5–25. One band table governs every surface; the labels below are the manuscript's post-audit vocabulary. Figure 4's threshold lines must be drawn at these boundaries (21/16/11), not at the 19/15/10 the current script uses.

| Total | Band label | Stars |
|---|---|---|
| 21–25 | Strongly Validated | ⭐⭐⭐⭐⭐ |
| 16–20 | High Confidence | ⭐⭐⭐⭐ |
| 11–15 | Moderate | ⭐⭐⭐ |
| 5–10 | Preliminary | ⭐⭐ |

A hypothesis whose quantitative legs were all withdrawn sits at the 5/25 floor inside the Preliminary band, carried with the withdrawn-legs note; the legacy "Unvalidated ⭐" level from §2.5's pre-audit five-level prose scale is unreachable by the point instrument (the floor is 5, which lands in Preliminary) and is retired as a scored band — it survives only as a categorical label for a claim with no supporting evidence of any kind, which no current hypothesis matches. §2.5's prose level definitions ("5+ sources with quantitative evidence…"), which conflict with the point bands and cite stale examples, are superseded by this table.

Ties order by descending total, then alphabetically by hypothesis ID.

## 4. Worked example: H-ARCH-01 (23/25, Strongly Validated)

Scoreable legs, all cited in §3.2.1 and all catalogued: SK Telecom production deployment (Iceberg with Trino; Evidence Level A — one measurement, documented in two bibliography blocks, counted once), the vendor-support roundup (broad-not-universal per the cited Register piece, Microsoft the named Delta-first holdout; A), ASF governance with the GitHub-derived 407-contributor count as of 2026-07-09 (A), and Dremio's 2024 survey, 29% planning Iceberg vs 23% Delta (A).

- Source count: 4 distinct measurements → **5**
- Evidence Level Quality: 4 of 4 legs tiered A = 100% → **5**
- Source diversity: Production Deployment (SK Telecom) + Vendor (support roundup) + Government/Standards (ASF) + Industry Analyst/Survey (Dremio) = 4 types → **5**
- Quantitative precision: the claim variable is dominance share; the withdrawn 76% was its only precise quantification, and the surviving precise figures quantify adjacent indicators → **3**
- Geographic/organizational diversity: SK Telecom (South Korea), the ASF's international contributor base, US/global vendors → 4+ orgs, international → **5**

Total 5+5+5+3+5 = **23/25**, in the 21–25 band → Strongly Validated ⭐⭐⭐⭐⭐. This reproduces the canonical bundle's decomposition, so the score is stable under the explicit rules.

## 5. Provenance and precedence

Derived from, in order of precedence where they disagreed: the anchor tables in `analysis-bundles/hypothesis-confidence-matrix.md` §Confidence Rubric (the instrument's origin, October 2025); the survived-verification rule in `RESCORE-PROPOSAL-2026-07.md` (adopted 2026-07-09); the manuscript's Appendix B narrative; and the canonical bundle's first-party evidence-tier note (2026-06-14). New in this file, made explicit rather than invented: anchor-only scoring, the distinct-measurement counting rule, the manuscript-cited-legs scope rule, the one-type-per-source assignment, the claim-variable precision rule, the collaboration-counts-once org rule, the zero-legs floor, and the single band table. The mechanical application of this instrument to the nine hypotheses is `methods/RESCORE-2026-07-13.md`.
