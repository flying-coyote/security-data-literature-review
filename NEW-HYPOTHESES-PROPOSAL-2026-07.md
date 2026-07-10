---
type: proposal
title: "New Tier-A-anchored hypotheses from the DR-3 intake — wording staged for owner sign-off (2026-07-10)"
created: 2026-07-10
status: STAGED — owner ruled "keep 7 + add new Tier-A anchored" (2026-07-10); wording below awaits sign-off + gate pass (karen-evaluator, hypothesis-validator, contradiction-detector) before manuscript integration
tags: [hypotheses, dr-3, tier-a, proposal, manuscript]
---

# New hypothesis candidates from the six DR-3 Tier-A primaries

**Why**: the 2026-07-10 owner ruling on the manuscript's hypothesis set was to keep the existing 7 with the post-audit honest split AND promote new hypotheses anchored on the six peer-reviewed primaries the DR-3 intake catalogued (`GEMINI-DR3-INTAKE-2026-07-10.md`, bibliography section "Peer-Reviewed Primaries — Gemini DR-3 intake"). This doc stages the candidate wording; nothing is integrated until the owner signs off on the statements and the hypothesis gates run.

**Anchor discipline**: every quantitative leg below was verified verbatim at its primary during the 2026-07-10 25-agent intake pass, so these launch with clean Tier-A legs — no inherited debt from the withdrawn-claims era.

## Candidate 1 — H-SOC-BASELINE-01: production SOC alert base rates

**Statement**: In production enterprise SOCs, alert volume runs orders of magnitude above true-attack incidence (tens of thousands to low hundreds of thousands of alerts per day against a true-attack fraction on the order of 0.01%), so the economics of any security data architecture are dominated by the cost of storing, moving, and triaging events that will never be incidents.

**Anchors** (all Tier A, one paper — flag the single-source dimension honestly):
- Yang et al., USENIX Security 2024: 24K–134K alerts/day across studied production SOCs (verbatim), ~0.01% true attacks (verbatim), alert composition 27%/49% (verbatim).

**Proposed initial score**: 14/25 ⭐⭐⭐ — evidence quality and quantitative precision max out (peer-reviewed, production-measured, verbatim-verified), but source count and organizational diversity are a single paper; the rubric caps it there until a second independent production study lands.

**Where it lands**: manuscript §3.7 (new row), Theme "Operational Reality"; project1 tracker mirror as a new entry. It also gives H-IMPL-01/02 the empirical backdrop their directional claims lacked — the connection is worth one sentence in §3.7, no more, since Yang measures alert economics rather than streaming staffing.

## Candidate 2 — H-LOGCOMP-01: log-specialized formats beat general-purpose

**Statement**: Compression and query formats designed around log structure deliver measured multiples over general-purpose equivalents on security-relevant workloads — a peer-reviewed cluster, not vendor claims — which supports the architectural claim that security telemetry deserves purpose-chosen storage formats rather than whatever the general data platform defaults to.

**Anchors** (four independent peer-reviewed papers, all verified verbatim 2026-07-10):
- LogLite (PVLDB 18(11)): 67.8% compression-ratio result, 2.7× (throughput leg).
- Blitzcrank (PVLDB 17(10):2528-2540): 85% / 19× (re-attributed at intake from the DeepSqueeze mislink — cite Blitzcrank, not DeepSqueeze).
- Pebbles (IEEE TPDS): ~8× / ~27× (title corrected at intake; publication year carries a to-confirm flag — resolve before integration).
- PBC (SIGMOD/PACMMOD 2024): 2×.

**Proposed initial score**: 18/25 ⭐⭐⭐⭐ — four independent peer-reviewed sources with verbatim-verified figures; loses points on organizational diversity (all academic prototypes, no production deployment leg yet) and on the Pebbles year flag until resolved.

**Where it lands**: manuscript §3.7 (new row), Theme "Foundational/Performance"; complements H3-PERFORMANCE-01 (general columnar engines) with the format-level result. Contradiction check required against H-ARCH-01's open-format standardization claim — specialized formats vs standard formats is a real tension the paper should name rather than paper over.

## Explicitly NOT promoted

- **Delta Lake (PVLDB 13(12))**: foundational lakehouse-ACID citation; strengthens H-ARCH-01's evidence base as a leg, doesn't need its own hypothesis.
- **The two C-tier catches** (Panther/Cockroach, layline.io): already catalogued against H-IMPL-01/02 as leads; below hypothesis-grade.

## Before integration (the gate list)

1. Owner signs off on the two statements (or edits them here).
2. Resolve the Pebbles publication-year flag at the primary.
3. Run karen-evaluator + hypothesis-validator on both; contradiction-detector across H-LOGCOMP-01 × H-ARCH-01 specifically.
4. Integrate: §2.5/§3.7/Tables 1-2/Figure 4 additions in one commit with a CHANGELOG entry; mirror to the project1 tracker.
