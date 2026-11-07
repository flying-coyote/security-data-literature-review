#!/usr/bin/env python3
"""
derive_source_taxonomy.py — the source-type mix of the corpus, derived rather than drawn.

Figure 3 used to be a hand-maintained chart: five buckets whose counts (17 production,
33 vendor, 10 analyst, 8 government, 6 academic) summed to 74 and described the
"75+ sources" corpus of October 2025. The corpus is now 195 entries. Nothing derived
the figure, so nothing caught the drift, and a chart of a corpus that no longer exists
sat in a manuscript bound for peer review. This script is the fix: it composes the
taxonomy from two committed, dated inputs and writes a single artifact that the figure
script and the count gate both read.

Inputs (both frozen records, neither edited by this script):
  methods/prisma-results/reconciliation.json   the retro-run's classification of all
                                               195 then-catalogued entries — 171 grey
                                               literature across ten categories, plus
                                               24 peer-reviewed entries held separately
  methods/incorporated-2026-07-13.json         the studies added by the incorporation
                                               pass, each with its appraised category

The composition is checked against MASTER-BIBLIOGRAPHY.md: the taxonomy must account
for every catalogued block, no more and no less. A mismatch exits non-zero rather than
emitting a chart that quietly drops or double-counts entries.

Usage:
  python3 scripts/derive_source_taxonomy.py            # write methods/source-taxonomy.json
  python3 scripts/derive_source_taxonomy.py --check    # verify only, write nothing
"""

import json
import os
import sys
from collections import Counter
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
os.chdir(REPO_ROOT)
sys.path.insert(0, str(REPO_ROOT / "scripts"))

from automation_dashboard import parse_master_bibliography  # noqa: E402

RECON = REPO_ROOT / "methods" / "prisma-results" / "reconciliation.json"
ADDED = REPO_ROOT / "methods" / "incorporated-2026-07-13.json"
# Fourth dated input (2026-07-16, later the same day): the second-screen flag
# adjudication admitted one study through the same appraisal gate as the
# original 40, so it enters the taxonomy through its own dated record.
ADJUD = REPO_ROOT / "methods" / "second-screen-adjudication-2026-07-16.json"
# Third dated input (2026-07-16): eight entries were headed '### ' instead of
# '#### ' from November 2025 until the heading fix, so they are in neither frozen
# record above; their classifications live in this file rather than in a retro-edit.
HEADFIX = REPO_ROOT / "methods" / "heading-fix-2026-07-16.json"
# Fifth dated input (2026-07-23): the Apache Ossie entry added by the
# semantic-data-layer standards pass, classified in its own dated record.
ADDED_0723 = REPO_ROOT / "methods" / "added-2026-07-23.json"
# Sixth dated input (2026-11-07): Zou et al. arXiv 2507.20526, classified in its
# own dated record (arXiv preprint, bucketed with the academic entries per the
# reconciliation record's precedent for arXiv research papers).
ADDED_1107 = REPO_ROOT / "methods" / "added-2026-11-07.json"
# Seventh dated input (2026-11-07, later the same day): Petrescu (ISSRE 2023) and
# Madani (C&ESAR 2026) from the Jenova citation-check harvest, in their own dated
# record so the earlier same-day file stays frozen.
ADDED_1107_JENOVA = REPO_ROOT / "methods" / "added-2026-11-07-jenova.json"
# Ninth dated input (2026-11-07, snowball pass): nine peer-reviewed admissions.
ADDED_1107_SNOWBALL = REPO_ROOT / "methods" / "added-2026-11-07-snowball.json"
# Eighth dated input (2026-11-07): the first record that MOVES entries between
# categories instead of adding them. It introduces the 'preprint' category and moves
# Shukla (arXiv 2509.00115) and Zou (arXiv 2507.20526) out of the peer-reviewed bucket.
RETIER_PREPRINT_1107 = REPO_ROOT / "methods" / "retier-preprint-2026-11-07.json"
# Tenth dated input (2026-11-07, handbook footnote companions): Reis (book), six
# [un]prompted talks, the Humio post (vendor blog) and Marwick & boyd 2011 (peer-reviewed).
ADDED_1107_BOOKFN = REPO_ROOT / "methods" / "added-2026-11-07-book-footnotes.json"
# Eleventh dated input (2026-11-07, thin-claim legs second pass): six peer-reviewed
# papers (CLP, LogGrep, Zibak, Inam, Michael, SPA), the Dodds blog, Conway 1968 and the
# SigmaHQ specification.
ADDED_1107_THIN = REPO_ROOT / "methods" / "added-2026-11-07-thin-claims.json"
# Twelfth dated input (2026-11-07, ch01 survey companions): Anaconda's 2020 State of
# Data Science survey and the 2016 Forbes report of the CrowdFlower survey, both
# analyst_or_industry_report.
ADDED_1107_CH01 = REPO_ROOT / "methods" / "added-2026-11-07-ch01-surveys.json"
# Thirteenth dated input (2026-11-07, handbook footnote legs third pass): seven
# peer-reviewed papers and CardinalOps's 2024 SIEM detection-risk release.
ADDED_1107_LEGS3 = REPO_ROOT / "methods" / "added-2026-11-07-footnote-legs-3.json"
# Records whose 'moves' list is applied after every additive record above.
MOVE_RECORDS = [RETIER_PREPRINT_1107]
OUT = REPO_ROOT / "methods" / "source-taxonomy.json"

ACADEMIC = "academic_peer_reviewed"

# Display order and labels for the figure. Peer-reviewed sits first because the
# review's own argument turns on how little of it there is.
DISPLAY = [
    (ACADEMIC, "Peer-reviewed\nacademic"),
    ("vendor_engineering_blog_or_product_docs", "Vendor blogs /\nproduct docs"),
    ("open_source_project_docs_or_repo", "Open-source\nproject docs"),
    ("practitioner_talk_or_personal_blog", "Practitioner talks /\npersonal blogs"),
    ("standards_frameworks_government", "Standards /\ngovernment"),
    ("big_tech_engineering_blog", "Big-tech\nengineering blogs"),
    ("analyst_or_industry_report", "Analyst /\nindustry reports"),
    ("book", "Books"),
    ("expert_interview_or_personal_communication", "Expert interviews"),
    ("first_party_lab_measurement", "First-party lab\nmeasurement"),
    ("preprint", "Preprints\n(arXiv, no venue)"),
    ("no_primary_retired_or_declined", "Retired / declined\n(no primary)"),
]


def load_counts():
    recon = json.loads(RECON.read_text(encoding="utf-8"))
    counts = Counter(recon["C_corpus_only_grey_literature"]["by_category"])
    counts[ACADEMIC] = len(recon["corpus_academic_entries"])

    added = []
    if ADDED.exists():
        added = json.loads(ADDED.read_text(encoding="utf-8"))["entries"]
        for entry in added:
            counts[entry.get("category", ACADEMIC)] += 1

    if HEADFIX.exists():
        for entry in json.loads(HEADFIX.read_text(encoding="utf-8"))["entries"]:
            counts[entry["category"]] += 1

    if ADJUD.exists():
        for entry in json.loads(ADJUD.read_text(encoding="utf-8"))["entries"]:
            counts[entry["category"]] += 1

    if ADDED_0723.exists():
        for entry in json.loads(ADDED_0723.read_text(encoding="utf-8"))["entries"]:
            counts[entry["category"]] += 1

    if ADDED_1107.exists():
        for entry in json.loads(ADDED_1107.read_text(encoding="utf-8"))["entries"]:
            counts[entry["category"]] += 1

    if ADDED_1107_JENOVA.exists():
        for entry in json.loads(ADDED_1107_JENOVA.read_text(encoding="utf-8"))["entries"]:
            counts[entry["category"]] += 1

    if ADDED_1107_SNOWBALL.exists():
        for entry in json.loads(ADDED_1107_SNOWBALL.read_text(encoding="utf-8"))["entries"]:
            counts[entry["category"]] += 1

    if ADDED_1107_BOOKFN.exists():
        for entry in json.loads(ADDED_1107_BOOKFN.read_text(encoding="utf-8"))["entries"]:
            counts[entry["category"]] += 1

    if ADDED_1107_THIN.exists():
        for entry in json.loads(ADDED_1107_THIN.read_text(encoding="utf-8"))["entries"]:
            counts[entry["category"]] += 1

    if ADDED_1107_CH01.exists():
        for entry in json.loads(ADDED_1107_CH01.read_text(encoding="utf-8"))["entries"]:
            counts[entry["category"]] += 1

    if ADDED_1107_LEGS3.exists():
        for entry in json.loads(ADDED_1107_LEGS3.read_text(encoding="utf-8"))["entries"]:
            counts[entry["category"]] += 1

    # Dated reclassifications: each move takes one entry out of 'from' and into 'to'.
    # A move whose source bucket is already empty means the record and the frozen
    # inputs disagree, which is a reconciliation failure, not something to clamp.
    for path in MOVE_RECORDS:
        if not path.exists():
            continue
        for move in json.loads(path.read_text(encoding="utf-8"))["moves"]:
            if counts[move["from"]] < 1:
                raise SystemExit(f"FATAL: move of {move['title']!r} from empty bucket {move['from']}")
            counts[move["from"]] -= 1
            counts[move["to"]] += 1

    return counts, len(added)


def main():
    counts, n_added = load_counts()
    bib = parse_master_bibliography()
    if bib is None:
        print("FATAL: MASTER-BIBLIOGRAPHY.md not found — canonical source broken.")
        return 2

    total = sum(counts.values())
    n_blocks = bib["total_entries"]
    if total != n_blocks:
        print(
            f"FATAL: taxonomy accounts for {total} entries but MASTER-BIBLIOGRAPHY.md "
            f"has {n_blocks} catalogued blocks. The classification is stale — a source "
            "was added or removed without being classified. Reconcile before charting."
        )
        return 1

    unknown = set(counts) - {k for k, _ in DISPLAY}
    if unknown:
        print(f"FATAL: unclassified category/categories: {sorted(unknown)}")
        return 1

    ordered = [
        {
            "category": key,
            "label": label,
            "count": counts[key],
            "percent": round(counts[key] / total * 100, 1),
        }
        for key, label in DISPLAY
        if counts[key]
    ]

    payload = {
        "derived_by": "scripts/derive_source_taxonomy.py",
        "total_entries": total,
        "peer_reviewed": counts[ACADEMIC],
        "peer_reviewed_percent": round(counts[ACADEMIC] / total * 100, 1),
        "added_by_incorporation_pass": n_added,
        "categories": ordered,
        "note": (
            "Composed from the retro-run classification of the pre-existing corpus plus "
            "the studies added by the incorporation pass. Percentages are of all "
            f"{total} catalogued blocks, which includes the two documented stubs the "
            "tier counts exclude, so this denominator is the block count and not the "
            "tiered count."
        ),
    }

    if "--check" in sys.argv:
        print(f"source-taxonomy: {total} entries reconcile with MASTER-BIBLIOGRAPHY.md.")
        return 0

    OUT.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    print(f"wrote {OUT.relative_to(REPO_ROOT)} — {total} entries across {len(ordered)} categories")
    for row in ordered:
        print(f"  {row['count']:>4}  {row['percent']:>5.1f}%  {row['category']}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
