#!/usr/bin/env python3
"""
Figure 2: Evidence Level Distribution — WITHDRAWN (2026-06-14 fabrications audit)

The original chart asserted an aggregate "79% Evidence Level A (exceeds 73%
target)" distribution. The 2026-06-14 audit found the initial pass overstated
Level A and removed several source entries, so the entire aggregate distribution
is withdrawn: no aggregate Level-A percentage is claimed pending re-verification,
and per-source evidence levels are provisional. See FIGURES-AND-TABLES.md
(Figure 2 strike note) and analysis-bundles/cost-reality-reference.md.

This script now renders a withdrawal notice in place of the chart so the rendered
PNG/PDF no longer circulate the withdrawn number. The original bar-chart code is
preserved in git history (pre-2026-06-15); do not re-add it without a re-verified
per-source tally.
"""

import os
import matplotlib.pyplot as plt

# Set publication-quality defaults
plt.rcParams['font.family'] = 'serif'
plt.rcParams['font.serif'] = ['Times New Roman', 'DejaVu Serif']
plt.rcParams['font.size'] = 11
plt.rcParams['axes.linewidth'] = 0.8
plt.rcParams['figure.dpi'] = 300


def create_evidence_distribution():
    """Render the Figure 2 withdrawal notice (the distribution is withdrawn)."""

    fig, ax = plt.subplots(figsize=(14, 6))
    ax.axis('off')

    notice = (
        "2026-06-14 fabrications audit: the aggregate Evidence-Level-A\n"
        "distribution self-grade (and its exceeds-target comparison) is withdrawn.\n\n"
        "The initial pass overstated Level A and several source entries were removed\n"
        "in the audit, so no aggregate Level-A percentage is claimed pending\n"
        "re-verification. Per-source evidence levels are provisional.\n\n"
        "See FIGURES-AND-TABLES.md (Figure 2 strike note) and\n"
        "analysis-bundles/cost-reality-reference.md. The original draft chart is\n"
        "preserved in git history (pre-2026-06-15)."
    )

    ax.text(0.5, 0.74, "WITHDRAWN", ha='center', va='center',
            fontsize=44, fontweight='bold', color='#B71C1C', alpha=0.9)
    ax.text(0.5, 0.34, notice, ha='center', va='center', fontsize=12.5,
            color='#212121', linespacing=1.6,
            bbox=dict(boxstyle='round,pad=1.0', facecolor='#FFF3E0',
                      edgecolor='#B71C1C', linewidth=1.5))

    fig.suptitle('Figure 2: Evidence Level Distribution — WITHDRAWN (2026-06-14 audit)',
                 fontsize=15, fontweight='bold', y=0.97, color='#B71C1C')
    plt.tight_layout(rect=[0, 0, 1, 0.95])

    output_dir = os.path.expanduser('~/security-data-literature-review/publication-graphics')
    plt.savefig(f'{output_dir}/figure2_evidence_distribution.png',
                dpi=300, bbox_inches='tight', facecolor='white')
    plt.savefig(f'{output_dir}/figure2_evidence_distribution.pdf',
                bbox_inches='tight', facecolor='white')

    print("Figure 2 withdrawal notice rendered (PNG + PDF).")
    plt.close()


if __name__ == '__main__':
    create_evidence_distribution()
