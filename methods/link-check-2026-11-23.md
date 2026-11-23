# Bibliography Link Check

**Date**: 2026-11-23
**Source**: `MASTER-BIBLIOGRAPHY.md` (350 unique URLs extracted)
**Script**: `scripts/link_check.py`

---

## Summary

| Class | Count | Meaning |
|---|---|---|
| OK | 282 | 2xx/3xx — reachable |
| PAYWALL_OR_BLOCKED | 64 | 401/403/429 — expected for Gartner/IDC/Forrester-class sources, not a failure |
| DEAD | 2 | 404/410 — confirmed gone |
| ERROR | 2 | timeout/DNS/other, or a status code outside the three classes above |
| **Total** | **350** | |

---

## Non-OK URLs

| URL | Class | Status | Note |
|---|---|---|---|
| https://www.anvilogic.com/case-studies/navan | DEAD | 404 |  |
| https://www.dataversity.net/the-data-centric-revolution-incremental-stealth-legacy-modernization/29181 | DEAD | 404 |  |
| https://techcommunity.microsoft.com/blog/fasttrackforazureblog/identifying-drift-in-ml-models-best-practices-for-generating-consistent-reliable/4040531 | ERROR | 400 | unclassified HTTP status 400 |
| https://www.uber.com/blog/palette-meta-store-journey/ | ERROR | 406 | unclassified HTTP status 406 |
| https://dl.acm.org/doi/10.1109/SP.2010.25 | PAYWALL_OR_BLOCKED | 403 | expected for paywalled/anti-bot sources |
| https://dl.acm.org/doi/10.1145/357830.357849 | PAYWALL_OR_BLOCKED | 403 | expected for paywalled/anti-bot sources |
| https://dl.acm.org/doi/10.14778/3749646.3749718 | PAYWALL_OR_BLOCKED | 403 | expected for paywalled/anti-bot sources |
| https://dl.acm.org/doi/abs/10.1145/3035918.3064049 | PAYWALL_OR_BLOCKED | 403 | expected for paywalled/anti-bot sources |
| https://doi.org/10.1002/cpe.5344 | PAYWALL_OR_BLOCKED | 403 | expected for paywalled/anti-bot sources |
| https://doi.org/10.1007/S10586-023-04201-9 | PAYWALL_OR_BLOCKED | 403 | expected for paywalled/anti-bot sources |
| https://doi.org/10.1007/s10664-024-10533-w | PAYWALL_OR_BLOCKED | 403 | expected for paywalled/anti-bot sources |
| https://doi.org/10.1016/j.diin.2007.06.004 | PAYWALL_OR_BLOCKED | 403 | expected for paywalled/anti-bot sources |
| https://doi.org/10.1016/j.fsidi.2024.301759 | PAYWALL_OR_BLOCKED | 403 | expected for paywalled/anti-bot sources |
| https://doi.org/10.1051/epjconf/202429501032 | PAYWALL_OR_BLOCKED | 403 | expected for paywalled/anti-bot sources |
| https://doi.org/10.1108/ijwis-03-2021-0023 | PAYWALL_OR_BLOCKED | 403 | expected for paywalled/anti-bot sources |
| https://doi.org/10.1109/ICDE55515.2023.00302 | PAYWALL_OR_BLOCKED | 403 | expected for paywalled/anti-bot sources |
| https://doi.org/10.1109/ICSE-SEIP.2019.00021 | PAYWALL_OR_BLOCKED | 403 | expected for paywalled/anti-bot sources |
| https://doi.org/10.1109/ISSRE59848.2023.00019 | PAYWALL_OR_BLOCKED | 403 | expected for paywalled/anti-bot sources |
| https://doi.org/10.1109/SP46215.2023.10179405 | PAYWALL_OR_BLOCKED | 403 | expected for paywalled/anti-bot sources |
| https://doi.org/10.1109/SPW53761.2021.00009 | PAYWALL_OR_BLOCKED | 403 | expected for paywalled/anti-bot sources |
| https://doi.org/10.1109/TDSC.2004.21 | PAYWALL_OR_BLOCKED | 403 | expected for paywalled/anti-bot sources |
| https://doi.org/10.1109/aitc.2019.8920960 | PAYWALL_OR_BLOCKED | 403 | expected for paywalled/anti-bot sources |
| https://doi.org/10.1109/bigdata62323.2024.10825247 | PAYWALL_OR_BLOCKED | 403 | expected for paywalled/anti-bot sources |
| https://doi.org/10.1109/compsac61105.2024.00355 | PAYWALL_OR_BLOCKED | 403 | expected for paywalled/anti-bot sources |
| https://doi.org/10.1109/cyberc.2018.00045 | PAYWALL_OR_BLOCKED | 403 | expected for paywalled/anti-bot sources |
| https://doi.org/10.1109/escience.2019.00028 | PAYWALL_OR_BLOCKED | 403 | expected for paywalled/anti-bot sources |
| https://doi.org/10.1109/glocom.2018.8647489 | PAYWALL_OR_BLOCKED | 403 | expected for paywalled/anti-bot sources |
| https://doi.org/10.1109/iceta51985.2020.9379260 | PAYWALL_OR_BLOCKED | 403 | expected for paywalled/anti-bot sources |
| https://doi.org/10.1109/icin69025.2026.11481838 | PAYWALL_OR_BLOCKED | 403 | expected for paywalled/anti-bot sources |
| https://doi.org/10.1109/mobisecserv.2018.8311440 | PAYWALL_OR_BLOCKED | 403 | expected for paywalled/anti-bot sources |
| https://doi.org/10.1109/snpdwinter52325.2021.00019 | PAYWALL_OR_BLOCKED | 403 | expected for paywalled/anti-bot sources |
| https://doi.org/10.1145/2568225.2568318 | PAYWALL_OR_BLOCKED | 403 | expected for paywalled/anti-bot sources |
| https://doi.org/10.1145/3158348 | PAYWALL_OR_BLOCKED | 403 | expected for paywalled/anti-bot sources |
| https://doi.org/10.1145/3319535.3354239 | PAYWALL_OR_BLOCKED | 403 | expected for paywalled/anti-bot sources |
| https://doi.org/10.1145/3339252.3340513 | PAYWALL_OR_BLOCKED | 403 | expected for paywalled/anti-bot sources |
| https://doi.org/10.1145/3411764.3445518 | PAYWALL_OR_BLOCKED | 403 | expected for paywalled/anti-bot sources |
| https://doi.org/10.1145/3427228.3427272 | PAYWALL_OR_BLOCKED | 403 | expected for paywalled/anti-bot sources |
| https://doi.org/10.1145/3428279 | PAYWALL_OR_BLOCKED | 403 | expected for paywalled/anti-bot sources |
| https://doi.org/10.1145/3484202 | PAYWALL_OR_BLOCKED | 403 | expected for paywalled/anti-bot sources |
| https://doi.org/10.1145/3552326.3567484 | PAYWALL_OR_BLOCKED | 403 | expected for paywalled/anti-bot sources |
| https://doi.org/10.1145/3589263 | PAYWALL_OR_BLOCKED | 403 | expected for paywalled/anti-bot sources |
| https://doi.org/10.1177/1461444810365313 | PAYWALL_OR_BLOCKED | 403 | expected for paywalled/anti-bot sources |
| https://doi.org/10.14569/ijacsa.2026.0170474 | PAYWALL_OR_BLOCKED | 403 | expected for paywalled/anti-bot sources |
| https://doi.org/10.1515/JISYS-2024-0109 | PAYWALL_OR_BLOCKED | 403 | expected for paywalled/anti-bot sources |
| https://doi.org/10.22323/1.327.0014 | PAYWALL_OR_BLOCKED | 403 | expected for paywalled/anti-bot sources |
| https://doi.org/10.2307/3250957 | PAYWALL_OR_BLOCKED | 403 | expected for paywalled/anti-bot sources |
| https://doi.org/10.24425/123532 | PAYWALL_OR_BLOCKED | 403 | expected for paywalled/anti-bot sources |
| https://doi.org/10.28925/2663-4023.2026.33.1144 | PAYWALL_OR_BLOCKED | 403 | expected for paywalled/anti-bot sources |
| https://doi.org/10.3390/bdcc6010019 | PAYWALL_OR_BLOCKED | 403 | expected for paywalled/anti-bot sources |
| https://doi.org/10.3390/computers15030200 | PAYWALL_OR_BLOCKED | 403 | expected for paywalled/anti-bot sources |
| https://doi.org/10.37936/ecti-cit.2026202.264216 | PAYWALL_OR_BLOCKED | 403 | expected for paywalled/anti-bot sources |
| https://doi.org/10.52436/1.jutif.2023.4.4.649 | PAYWALL_OR_BLOCKED | 403 | expected for paywalled/anti-bot sources |
| https://github.com/flying-coyote/sdw-lab-benchmarks/blob/master/cost-to-serve-retention/results/measured_footprints.json | PAYWALL_OR_BLOCKED | 429 | expected for paywalled/anti-bot sources |
| https://insiderthreat.mitre.org/ | PAYWALL_OR_BLOCKED | 403 | expected for paywalled/anti-bot sources |
| https://medium.com/@office_9948/apache-gravitino-production-ready-unified-metadata-for-enterprise-data-9ba0eb38268b | PAYWALL_OR_BLOCKED | 403 | expected for paywalled/anti-bot sources |
| https://netflixtechblog.com/building-a-resilient-data-platform-with-write-ahead-log-at-netflix-127b6712359a | PAYWALL_OR_BLOCKED | 403 | expected for paywalled/anti-bot sources |
| https://people.eecs.berkeley.edu/~julien.piet/matryoshka.pdf | PAYWALL_OR_BLOCKED | 403 | expected for paywalled/anti-bot sources |
| https://stratos.seas.harvard.edu/publications/access-path-selection-main-memory-optimized-data-systems-should-i-scan-or | PAYWALL_OR_BLOCKED | 403 | expected for paywalled/anti-bot sources |
| https://web.archive.org/web/20250119164347/https://netflixtechblog.com/kafka-inside-keystone-pipeline-dd5aeabaf6bb | PAYWALL_OR_BLOCKED | 429 | expected for paywalled/anti-bot sources; redirected -> https://web.archive.org/web/20250119164346/https://netflixtechblog.com/kafka-inside-keystone-pipeline-dd5aeabaf6bb |
| https://www.anaconda.com/resources/whitepaper/state-of-data-science-2020 | PAYWALL_OR_BLOCKED | 403 | expected for paywalled/anti-bot sources |
| https://www.forbes.com/sites/gilpress/2016/03/23/data-preparation-most-time-consuming-least-enjoyable-data-science-task-survey-says/ | PAYWALL_OR_BLOCKED | 403 | expected for paywalled/anti-bot sources |
| https://www.gartner.com/en/newsroom/press-releases/2024-07-29-gartner-predicts-30-percent-of-generative-ai-projects-will-be-abandoned-after-proof-of-concept-by-end-of-2025 | PAYWALL_OR_BLOCKED | 403 | expected for paywalled/anti-bot sources |
| https://www.gartner.com/en/newsroom/press-releases/2024-08-28-gartner-forecasts-global-information-security-spending-to-grow-15-percent-in-2025 | PAYWALL_OR_BLOCKED | 403 | expected for paywalled/anti-bot sources |
| https://www.gartner.com/en/newsroom/press-releases/2025-07-29-gartner-forecasts-worldwide-end-user-spending-on-information-security-to-total-213-billion-us-dollars-in-2025 | PAYWALL_OR_BLOCKED | 403 | expected for paywalled/anti-bot sources |
| https://www.globenewswire.com/news-release/2025/12/16/3206276/0/en/Fortinet-Delivers-Isolated-Infrastructure-Acceleration-for-the-AI-Factory-with-NVIDIA.html | PAYWALL_OR_BLOCKED | 403 | expected for paywalled/anti-bot sources |
| https://www.iso.org/standard/74572.html | PAYWALL_OR_BLOCKED | 403 | expected for paywalled/anti-bot sources |
| https://www.mitre.org/news-insights/news-release/mitre-extends-d3fend-ontology-operational-technology-cybersecurity | PAYWALL_OR_BLOCKED | 403 | expected for paywalled/anti-bot sources |
| https://www.mitre.org/news-insights/news-release/mitre-launches-d3fend-10-milestone-cybersecurity-ontology | PAYWALL_OR_BLOCKED | 403 | expected for paywalled/anti-bot sources |

---

_This pass is report-only: no bibliography file was edited by this script. Any fixes (re-pointing a dead URL, dropping a stale citation) are owner-adjudicated by hand._
