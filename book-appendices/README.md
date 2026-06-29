# Book Appendices — MOAR Handbook Tier-3 Deep Evidence

These thirteen files are the MOAR handbook's Tier-3 deep-evidence appendices, and they are canonical *here* in the companion (the literature-review repository) rather than in the book repository. The handbook itself stays deliberately short — roughly a hundred pages across seven chapters that carry the decision path and the load-bearing argument — and it points *up* to these appendices wherever a reader needs the full machinery behind a chapter's summary: the complete scoring matrices, the per-vendor POC results, the OCSF mapping mechanics, the query-engine cost models, the measured detection-coverage method. Each chapter keeps the decision-relevant version and hands off the depth to the appendix that grounds it, so the appendices are where the worksheets, walkthroughs, vendor data, and lab measurements live in full. Because these are the canonical copies, the book repository should not carry a second maintained copy; edit here, and let the handbook reference up.

## The Thirteen Appendices

The "Primarily grounds" column maps each appendix to the new seven-chapter spine — Ch.1 *Why cybersecurity data is different* (manageability and the foreground-constraints decision framework), Ch.2 *MOAr explained*, Ch.3 *Trustworthy*, Ch.4 *Well-connected*, Ch.5 *Performant*, Ch.6 *Variants / what good looks like*, Ch.7 *Modularity / incremental modernization* — derived from the chapter cross-references each appendix actually carries.

| App. | Title | Filename | Primarily grounds |
|------|-------|----------|-------------------|
| A | Decision Worksheets — Security Data Platform Selection | `appendix-a-decision-worksheets.md` | Ch.1 (decision framework / TCO); Ch.6 (variant TCO examples); Ch.7 (business case) |
| B | Anti-Patterns Catalog | `appendix-b-anti-patterns.md` | Ch.1 (constraints-first decisions); Ch.7 (rollout / change management); Ch.3 (data-trust failure mode) |
| C | MOAr Reference Architectures — L-I-G-E-R Component Model and Five Patterns | `appendix-c-reference-architectures.md` | Ch.2 (MOAr framework); Ch.6 (the four architect-journey patterns) |
| D | Glossary — Security ↔ Data Engineering Translation Guide | `appendix-d-glossary-translation-guide.md` | Ch.1 (manageability framing); Ch.6/Ch.7 (decision-frameworks-in-practice) |
| E | Consolidated Resource Directory | `appendix-e-resource-directory.md` | Ch.1 (learning path entry point); cross-handbook (companion essay map) |
| F | OCSF Implementation Guide & Field Mapping Reference | `appendix-f-ocsf-implementation-guide.md` | Ch.3 (trustworthy data — tactical OCSF mapping; pairs with Appendix H) |
| G | Security Data Stack Vendor Landscape | `appendix-g-vendor-landscape.md` | Ch.1 / Ch.6 (vendor evaluation; scored via Appendix A worksheets) |
| H | OCSF as a Normalization Baseline — Strategy, Economics, and Failure Modes | `appendix-h-ocsf-strategy.md` | Ch.3 (trustworthy data — OCSF strategy and the mapping failure mode); Ch.1 (cost model) |
| I | Query Engine Selection for Security Workloads | `appendix-i-query-engine-selection.md` | Ch.5 (performant — multi-engine selection); Ch.1 (cost), Ch.6/Ch.7 (engine decisions) |
| J | Resources and Community | `appendix-j-resources-and-community.md` | Ch.5 (performant — tooling judgment); Ch.3 (trustworthy — why Iceberg); cross-handbook (community) |
| K | The Three Journeys — Full Walkthroughs | `appendix-k-three-journeys-walkthroughs.md` | Ch.6 (variants — full Jennifer/Marcus/Priya machinery behind the chapter summaries) |
| L | Implementation Operations Detail | `appendix-l-implementation-operations-detail.md` | Ch.7 (modularity — operational depth behind the incremental-modernization plan) |
| M | Detection Coverage Measurement — ATT&CK→D3FEND over OCSF | `appendix-m-detection-coverage.md` | Ch.7 (modularity — measuring migrated-detection firing; the C5 method) |

## Chapter cross-reference reconciliation

The appendices were drafted against an older six-chapter manuscript spine, and their internal chapter pointers were reconciled to the new seven-chapter spine on 2026-06-29. References that named the older structure ("the manageability chapter", "the variants chapter", "the incremental-modernization material") now resolve to the current chapters — Ch.1, Ch.6, and Ch.7 respectively — and the trustworthy-data and performant material to Ch.3 and Ch.5. If you find a stale chapter number while editing, fix it here and treat the seven-chapter spine above as the source of truth.
