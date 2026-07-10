---
type: verification-report
title: "Gemini DR-1 intake — streaming-vs-batch economics (H-IMPL rebuild hunt), verified 2026-07-10"
created: 2026-07-10
tags: [gemini-dr, intake, streaming-vs-batch, h-impl, verification]
---

# Gemini DR-1 intake — streaming-vs-batch cost and staffing

**Run**: DR-1 from `~/project1/02-projects/GEMINI-DR-QUEUE-2026-07-10.md` (fired by owner 2026-07-10; output Google Doc `13ZN9-9Lc9xz06uIbcA_DGN4NxH-LFL61H72-XCkDYS0`). Every candidate fetched and quote-verified locally (workflow `wf_54e835a8-776`, 3 verification agents) before any disposition.

**Headline for the rescore adjudication**: the hunt found **zero Tier-A or Tier-B material** on streaming-vs-batch operational economics. Quotes mostly verify verbatim, but the venues are anonymous-Medium, vendor channels, and two predatory-adjacent journals. **The H-IMPL-01 (1/5) and H-IMPL-02 (2/5) post-overturn scores survive this hunt unchallenged** — no withdrawn leg is restored, and the RESCORE-PROPOSAL can proceed on the existing evidence. Note the Google-Docs export also silently dropped many inline figures from the DR prose (empty gaps where numbers were), so the verbatim table was the only usable layer.

| # | Source | Verdict at primary | Tier | Disposition |
|---|---|---|---|---|
| 1 | Medium "Reliable Data Engineering" ($7,600 vs $700/mo; "Streaming is 11x more expensive") | VERIFIED verbatim (via WebFetch; curl bot-blocked) | C/D — anonymous/pseudonymous account, unsourced illustrative numbers | REJECTED (no author identity, no methodology) |
| 2 | layline.io, Andrew Tan, 2026-04-27 ($160-220K salary, 4-mo hire, 3-6 mo retrain, 6-mo dual-run) | VERIFIED verbatim (all five figures) | C — vendor-channel authorship, no methodology | **CATALOGUED** (C; H-IMPL-02 directional) |
| 3 | JAIGS / Sikarwar 2024 (batch near-zero idle cost) | VERIFIED verbatim at the journal galley (RePEc is only an index) | D — JAIGS flagged as likely predatory/pay-to-publish | REJECTED (venue) |
| 4 | IRJMETS / Kodakandla 2023 (Kafka-Spark-BigQuery 30-day cost sim) | PARTIAL (primary 403-blocked; search-snippet corroboration only) | D — IRJMETS lacks genuine peer review (near-instant turnaround) | REJECTED (venue + unverified primary) |
| 5 | Panther / Cockroach Labs case study (5× logs, $200K+ cut, 365-day retention) | VERIFIED verbatim; named customer sources (Jaber, Brennick) | C — vendor case study quoting customer (tier rule) | **CATALOGUED** (C; migration-outcome family, contradicts premise) |
| 6 | Snowflake blog 2024-04-18 (Navan "over 70%", "15K+ hours in 8 months") | VERIFIED verbatim; unattributed vendor copy | C | ALREADY CATALOGUED (part-2 Navan entry, C 70-80%); the 15K-hours + 4× MITRE-coverage details noted here for a future touch of that entry |
| 7 | Sarcouncil / Velichala 2025 (28% ops reduction, 41% CSAT — attributed to Achanta 2024) | VERIFIED verbatim in the PDF — but the load-bearing stats are the paper's own SECONDHAND cites of untraceable primaries | D — SARC flagged predatory-adjacent (20+ journals, pay-to-publish profile) | REJECTED (venue + secondhand-of-secondhand) |
| 8 | SiliconANGLE / Estuary CEO (40-60% savings claim) | VERIFIED; funding figure is $17M in the article body (the URL slug "14m" is stale) | C — CEO self-claim in funding coverage | REJECTED (marginal relevance: data-integration TCO, not security streaming-vs-batch) |
| 9 | Fuentes/Mathews/Anderson (Flink energy efficiency, Apr 2026) | UNREACHABLE (ResearchGate 403 through every route incl. proxies) — venue unidentifiable; leans on untraced "Souames et al. 2025" | unassignable | STAGED (re-try if it surfaces at a real venue; do not cite) |

**DR-quality notes for the queue doc**: (1) the run respected the known-dead-ends list — none of the withdrawn legs (IDC/DORA/Ververica/MIT-TR/DOES) reappeared; (2) it labeled two predatory venues "peer-reviewed"; (3) it mislabeled the Estuary funding amount internally ($14M vs $17M); (4) its "unresolved references" section honestly listed five untraceable secondhand cites — those stay untraceable after local checks too.
