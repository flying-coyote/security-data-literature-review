# Bibliography Link Check

**Date**: 2026-07-16
**Source**: `MASTER-BIBLIOGRAPHY.md` (264 unique URLs extracted)
**Script**: `scripts/link_check.py`

---

## Summary

| Class | Count | Meaning |
|---|---|---|
| OK | 243 | 2xx/3xx — reachable |
| PAYWALL_OR_BLOCKED | 16 | 401/403/429 — expected for Gartner/IDC/Forrester-class sources, not a failure |
| DEAD | 3 | 404/410 — confirmed gone |
| ERROR | 2 | timeout/DNS/other, or a status code outside the three classes above |
| **Total** | **264** | |

---

## Non-OK URLs

| URL | Class | Status | Note |
|---|---|---|---|
| https://github.com/flying-coyote/splunk-db-connect-benchmark | DEAD | 404 |  |
| https://opencybersecurityalliance.org/ | DEAD | 404 |  |
| https://tdan.com/the-data-centric-revolution-incremental-stealth-legacy-modernization/29181 | DEAD | 404 | redirected -> https://www.dataversity.net/the-data-centric-revolution-incremental-stealth-legacy-modernization/29181 |
| https://techcommunity.microsoft.com/blog/fasttrackforazureblog/identifying-drift-in-ml-models-best-practices-for-generating-consistent-reliable/4040531 | ERROR | 400 | unclassified HTTP status 400 |
| https://www.uber.com/blog/palette-meta-store-journey/ | ERROR | 406 | unclassified HTTP status 406 |
| https://dl.acm.org/doi/10.1109/SP.2010.25 | PAYWALL_OR_BLOCKED | 403 | expected for paywalled/anti-bot sources |
| https://dl.acm.org/doi/10.1145/357830.357849 | PAYWALL_OR_BLOCKED | 403 | expected for paywalled/anti-bot sources |
| https://dl.acm.org/doi/10.14778/3749646.3749718 | PAYWALL_OR_BLOCKED | 403 | expected for paywalled/anti-bot sources |
| https://dl.acm.org/doi/abs/10.1145/3035918.3064049 | PAYWALL_OR_BLOCKED | 403 | expected for paywalled/anti-bot sources |
| https://doi.org/10.1002/cpe.5344 | PAYWALL_OR_BLOCKED | 403 | expected for paywalled/anti-bot sources; redirected -> https://onlinelibrary.wiley.com/doi/10.1002/cpe.5344 |
| https://doi.org/10.1108/ijwis-03-2021-0023 | PAYWALL_OR_BLOCKED | 403 | expected for paywalled/anti-bot sources; redirected -> https://www.emerald.com/ijwis/article/17/5/427-448/375925 |
| https://doi.org/10.1145/3158348 | PAYWALL_OR_BLOCKED | 403 | expected for paywalled/anti-bot sources; redirected -> https://dl.acm.org/doi/10.1145/3158348 |
| https://doi.org/10.1145/3339252.3340513 | PAYWALL_OR_BLOCKED | 403 | expected for paywalled/anti-bot sources; redirected -> https://dl.acm.org/doi/10.1145/3339252.3340513 |
| https://doi.org/10.3390/bdcc6010019 | PAYWALL_OR_BLOCKED | 403 | expected for paywalled/anti-bot sources; redirected -> https://www.mdpi.com/2504-2289/6/1/19 |
| https://doi.org/10.3390/computers15030200 | PAYWALL_OR_BLOCKED | 403 | expected for paywalled/anti-bot sources; redirected -> https://www.mdpi.com/2073-431X/15/3/200 |
| https://people.eecs.berkeley.edu/~julien.piet/matryoshka.pdf | PAYWALL_OR_BLOCKED | 403 | expected for paywalled/anti-bot sources |
| https://stratos.seas.harvard.edu/publications/access-path-selection-main-memory-optimized-data-systems-should-i-scan-or | PAYWALL_OR_BLOCKED | 403 | expected for paywalled/anti-bot sources |
| https://www.gartner.com/en/newsroom/press-releases/2024-08-28-gartner-forecasts-global-information-security-spending-to-grow-15-percent-in-2025 | PAYWALL_OR_BLOCKED | 403 | expected for paywalled/anti-bot sources |
| https://www.gartner.com/en/newsroom/press-releases/2025-07-29-gartner-forecasts-worldwide-end-user-spending-on-information-security-to-total-213-billion-us-dollars-in-2025 | PAYWALL_OR_BLOCKED | 403 | expected for paywalled/anti-bot sources |
| https://www.mitre.org/news-insights/news-release/mitre-extends-d3fend-ontology-operational-technology-cybersecurity | PAYWALL_OR_BLOCKED | 403 | expected for paywalled/anti-bot sources |
| https://www.mitre.org/news-insights/news-release/mitre-launches-d3fend-10-milestone-cybersecurity-ontology | PAYWALL_OR_BLOCKED | 403 | expected for paywalled/anti-bot sources |

---

_This pass is report-only: no bibliography file was edited by this script. Any fixes (re-pointing a dead URL, dropping a stale citation) are owner-adjudicated by hand._
