---
type: verification-report
title: "Gemini DR-3 intake — Tier-A primary hunt, verified 2026-07-10 (6 catalogued, 3 misattributions caught, 1 self-cite fabrication)"
created: 2026-07-10
tags: [gemini-dr, intake, tier-a, verification, misattribution]
---

# Gemini DR-3 intake — Tier-A primary hunt

**Run**: DR-3 from `~/project1/02-projects/GEMINI-DR-QUEUE-2026-07-10.md` (fired 2026-07-10; output Google Doc `1aFA0kimwxEnrX8RvDTLvSwTONiioO3ZrfsNy1-JRJII`). Every candidate fetched and quote-verified locally (workflow `wf_54e835a8-776`, 9 verification agents incl. four full-effort misattribution checks) before cataloguing.

**Net result**: **six Tier-A entries catalogued** (MASTER-BIBLIOGRAPHY "Peer-Reviewed Primaries — Gemini DR-3 intake" section) — Yang et al. USENIX Security '24 (the star: production-SOC alert base rates), LogLite (PVLDB 18), PBC (SIGMOD '24), Pebbles (IEEE TPDS), Blitzcrank (PVLDB 17, re-attributed), Delta Lake (PVLDB 13). Tier-A share moved 41.6% → **43.0%** (83/193, dashboard-derived).

## Dispositions

| # | Candidate | Verdict at primary | Disposition |
|---|---|---|---|
| 3.15 | Yang et al., USENIX Security 2024 (24K-134K alerts/day; 0.01% true attacks; 27%/49% composition) | VERIFIED verbatim (abstract + PDF; 11 authors UIUC/NCSA/IBM) | **CATALOGUED A** |
| 3.10 | LogLite, PVLDB 18(11) (67.8% ratio, 2.7× speed) | VERIFIED verbatim at vldb.org + arXiv | **CATALOGUED A** |
| 3.09 | PBC, SIGMOD/PACMMOD 2024 (2× compression vs SOTA) | VERIFIED verbatim; 10 authors, Ant Group lineage; antgroup/pbc exists | **CATALOGUED A** |
| 3.08 | "Sketch-Aware Streaming Telemetry, NSF 2023" | Quote VERIFIED (~8× / ~27×) but the DR's title/label was INVENTED — real paper is **Pebbles** (Buddhika/Pallickara/Pallickara, IEEE TPDS) | **CATALOGUED A** (corrected citation) |
| 3.11 | "Blitzcrank" quote linked to DeepSqueeze (ResearchGate 341750834) | MISATTRIBUTION CONFIRMED — quote is real and verbatim in **Blitzcrank, PVLDB 17(10):2528-2540, 2024 (Qiao/Gao/Zhang, Tsinghua)**; DeepSqueeze is a different paper and does not contain it | **CATALOGUED A** (re-attributed) |
| 3.14 | Delta Lake, PVLDB 13(12), Armbrust et al. 2020 | VERIFIED (PDF; 21 authors; the DR "quote" was a paraphrase — entry records the abstract's actual claim) | **CATALOGUED A** |
| 3.12 | "Magnus" PVLDB 18 p4964 with "thousand-fold speedups" quote | Paper identity VERIFIED (Magnus is real: PVLDB 18(12):4964-4977, ByteDance+Zhejiang, ML-workload data management) but the QUOTE is misattributed — it is not verbatim anywhere in Magnus; the DR's own citation trail points at "Big Metadata" (VLDB 2021, Google BigQuery). The DR's prose description of Magnus (Iceberg metadata/manifest-sorting/MOR upserts) also doesn't match the actual paper's focus | STAGED — Magnus + Big Metadata are both real Tier-A candidates for the table-format-maintenance topic, but neither has a locally verified quantitative quote yet; needs a real read before cataloguing |
| 3.13 | "Lakestream Metadata Manifest Coordination, ByteDance Systems Research Group" (arXiv 2605.09994) | Real paper is **BatchWeave** ("Lakestream" appears ZERO times — DR fabricated the title and author group); 2.68-7.73× quote verified; domain is foundation-model TRAINING data planes, not security lakehouses — the DR's filing under security table-format maintenance is a stretch | REJECTED for this corpus (relevance; preprint-only) |
| 3.01 | "SecurityDataWorks Research Group, Security Data Works Platform Analysis, Q1 2026" citing securitydataworks.com | **SELF-CITE SYNTHESIS-CONFLATION**: the three figures (Photon 17s→5s, Sentinel $2.30/GB, BigQuery $0.02/GB/mo) DO each appear on the live homepage — but as three SEPARATE teardown reference cards about three DIFFERENT platforms (rendered from `src/data/references.ts`); the DR stitched them into one fabricated sentence and invented a "SecurityDataWorks Research Group." Textbook synthesis-conflation + circular self-citation | REJECTED (recorded as the run's cautionary exhibit) |
| 3.03 | Matryoshka (arXiv 2506.17512; UDM P/R 0.60/0.60 vs 0.50/0.48; F1 0.95) | Figures VERIFIED; arXiv-preprint ONLY (no venue); DR's author list omitted Scott Coull; affiliations mixed Berkeley+other | STAGED B/C — directly relevant to the OCSF-fidelity work (interoperability-vs-fidelity trade-off) but preprint-only; catalogue if it lands at a venue or if cited with the preprint caveat |
| 3.04 | Beyond Collection (arXiv 2605.05531; 50 RCE vulns, logging-standard detection efficacy) | VERIFIED (authors exact: Holeman/Hastings/Vaidyan); preprint-only, single version | STAGED B/C (same preprint caveat; relevant to logging-standard efficacy claims) |
| 3.07 | Alert-screening survey (arXiv 2605.08316; FNR <2% budget framing) | VERIFIED; real authors are **Ndichu/Ban/Ozawa/Takahashi/Inoue** (DR credited "Aminanto et al." — that is a cited-within source) | STAGED C (survey preprint; useful framing, not primary data) |
| 3.05 | Deterministic forensic preprocessing (100% consistency, UNSW-NB15/IoT-23/TON_IoT) | Located at arXiv 2606.11565 (ResearchGate blocked); DR's author line ("M. J. Scholar, J. Forensic") was garbled/invented | STAGED C (preprint; real authors recorded in workflow journal) |
| 3.06 | Mohale federated stream-processing (arXiv 2605.17325; PFDS 99.8%, 500K eps) | VERIFIED verbatim; sole author is an independent researcher, no affiliation, preprint-only | STAGED C/D (verify any onward use carefully) |
| 3.02 | Cisco/AWS Security Lake blog (partition-optimization quote) | VERIFIED verbatim; author Jessica (Bair) Oppenheimer, Cisco | REJECTED (C-tier vendor blog, no quantitative finding worth an entry) |
| 3.16 | "Ex-SOC" XAI framework (ResearchGate 404704611) | UNREACHABLE (Cloudflare 1020 hard block on every route); "Ex-SOC Human Systems Research" author line is DR-invented | REJECTED |
| 3.17 | Al-Kindi JCSTS (8%/15% incident-resolution rates) | Quote VERIFIED verbatim in the PDF — but the stat is itself the article's secondhand cite, and Al-Kindi profiles as a low-quality/predatory publisher | REJECTED (venue + secondhand) |

## Pattern notes (for the DR queue doc's next revision)

Four fabrication-class defects in one run, all caught by verify-at-primary: an invented title+author-group (BatchWeave→"Lakestream"), a quote attached to the wrong paper (Blitzcrank→DeepSqueeze link), an invented author line ("M. J. Scholar, J. Forensic"; "Ex-SOC Human Systems Research"), and the self-cite conflation (three unrelated reference cards from our own site stitched into one fake finding under an invented research group). The quotes themselves were almost always verbatim-real — DR's failure mode is ATTRIBUTION, not quotation, which is exactly the failure the intake discipline (fetch the primary, confirm authors/venue, then catalogue) is built to catch.
