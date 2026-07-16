#!/usr/bin/env python3
"""
Figure 3: Source-type taxonomy of the corpus.

DERIVED, NOT DRAWN. This chart used to hold five hand-maintained buckets whose counts summed
to 74 and described the "75+ sources" corpus of October 2025. The corpus is now derived live (229 catalogued blocks as of 2026-07-16)
entries. Nothing derived the figure, so nothing caught the drift, and a chart of a corpus that
no longer existed sat in a manuscript bound for peer review. It now reads its numbers from
methods/source-taxonomy.json, which scripts/derive_source_taxonomy.py composes from the
retro-run classification plus the incorporation pass and reconciles against
MASTER-BIBLIOGRAPHY.md — so a source added without being classified fails the build instead of
quietly falling out of the chart.

The ordering is deliberate. Peer-reviewed work sits at the top because the review's own argument
turns on how thin it is: the largest single category in a systematic review of security data
architecture is still vendor engineering blogs and product documentation.

Regenerate:  python3 scripts/derive_source_taxonomy.py && python3 publication-graphics/figure3_source_taxonomy.py
"""

import json
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402
import numpy as np  # noqa: E402

REPO = Path(__file__).resolve().parent.parent
TAXONOMY = REPO / "methods" / "source-taxonomy.json"
OUT = REPO / "publication-graphics" / "figure3_source_taxonomy.png"
OUT_PDF = REPO / "publication-graphics" / "figure3_source_taxonomy.pdf"

plt.rcParams["font.family"] = "serif"
plt.rcParams["font.serif"] = ["Times New Roman", "DejaVu Serif"]
plt.rcParams["font.size"] = 11
plt.rcParams["axes.linewidth"] = 0.8
plt.rcParams["figure.dpi"] = 300

# Peer-reviewed is the one category the review's argument hangs on, so it is the only
# one that carries a distinct, saturated colour; everything else is a graded neutral.
PEER_REVIEWED = "#1565C0"
GREY_LITERATURE = "#90A4AE"
VENDOR = "#EF6C00"


def colour_for(category):
    if category == "academic_peer_reviewed":
        return PEER_REVIEWED
    if category in ("vendor_engineering_blog_or_product_docs", "big_tech_engineering_blog"):
        return VENDOR
    return GREY_LITERATURE


def main():
    tax = json.loads(TAXONOMY.read_text(encoding="utf-8"))
    rows = tax["categories"]
    total = tax["total_entries"]

    labels = [r["label"] for r in rows]
    counts = [r["count"] for r in rows]
    pcts = [r["percent"] for r in rows]
    colours = [colour_for(r["category"]) for r in rows]

    fig, ax = plt.subplots(figsize=(11, 7))
    y = np.arange(len(rows))[::-1]  # largest at top

    bars = ax.barh(y, pcts, color=colours, alpha=0.92, edgecolor="black", linewidth=0.7, height=0.68)

    for bar, count, pct in zip(bars, counts, pcts):
        w = bar.get_width()
        ax.text(
            w + 0.4,
            bar.get_y() + bar.get_height() / 2,
            f"n={count}  ({pct:.1f}%)",
            ha="left",
            va="center",
            fontsize=10.5,
            fontweight="bold",
        )

    ax.set_yticks(y)
    ax.set_yticklabels(labels, fontsize=10)
    ax.set_xlabel("Share of the catalogued corpus (%)", fontsize=11.5, fontweight="bold")
    ax.set_xlim(0, max(pcts) + 9)
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.grid(axis="x", linestyle=":", alpha=0.4)
    ax.set_axisbelow(True)

    peer = tax["peer_reviewed"]
    peer_pct = tax["peer_reviewed_percent"]
    vendor_like = sum(
        r["count"]
        for r in rows
        if r["category"] in ("vendor_engineering_blog_or_product_docs", "big_tech_engineering_blog")
    )

    ax.set_title(
        f"Figure 3: Source-type taxonomy of the {total}-entry corpus\n"
        f"Peer-reviewed: {peer} of {total} ({peer_pct}%) — vendor-authored: {vendor_like} of {total} "
        f"({100 * vendor_like / total:.1f}%)",
        fontsize=13,
        fontweight="bold",
        pad=16,
    )

    fig.text(
        0.5,
        0.015,
        f"Derived from MASTER-BIBLIOGRAPHY.md via scripts/derive_source_taxonomy.py "
        f"({tax['added_by_incorporation_pass']} entries added by the 2026-07-13 systematic-search "
        f"incorporation). Percentages are of all {total} catalogued blocks.",
        ha="center",
        fontsize=8.5,
        style="italic",
        color="#455A64",
    )

    plt.tight_layout(rect=[0, 0.04, 1, 1])
    plt.savefig(OUT, dpi=300, bbox_inches="tight", facecolor="white")
    plt.savefig(OUT_PDF, bbox_inches="tight", facecolor="white")
    print(f"Figure 3 rendered from {TAXONOMY.name}: {total} entries, {peer} peer-reviewed ({peer_pct}%).")


if __name__ == "__main__":
    main()
