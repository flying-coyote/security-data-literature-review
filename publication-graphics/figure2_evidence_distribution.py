#!/usr/bin/env python3
"""
Figure 2: Evidence Level Distribution — live re-verified tally (2026-07-09)

History: the original chart asserted "79% Evidence Level A (exceeds 73% target)".
The 2026-06-14 audit withdrew that self-grade (Level A overstated, entries
removed) and this script rendered a withdrawal notice, with the condition that
the chart not return without a re-verified per-source tally.

That condition is now met: the corpus reconciles to 195 blocks / 193 tiered and
the tier mix is computed from per-entry Evidence-Level markers. This chart states
the honest figure rather than a self-grade. (An earlier version also drew a
">70% Level-A target" line and a "pts below target" gap; the target was retired by
owner ruling on 2026-08-19, METHODOLOGY 8.1a, so the share is plotted as a
measurement and graded against nothing.) Update the TALLY constants from the canonical counter before
regenerating; do not hand-edit percentages.

Canonical source for TIERED_TOTAL and TALLY: scripts/count_reconcile.py
("Counter 2: bibliography tiers"), which derives them from MASTER-BIBLIOGRAPHY.md.
The reconcile script also gates this figure's caption in the manuscript, so a
tally change here that is not propagated there fails the count-reconcile check.
"""

import os
import matplotlib.pyplot as plt

# Set publication-quality defaults
plt.rcParams['font.family'] = 'serif'
plt.rcParams['font.serif'] = ['Times New Roman', 'DejaVu Serif']
plt.rcParams['font.size'] = 11
plt.rcParams['axes.linewidth'] = 0.8
plt.rcParams['figure.dpi'] = 300

# Live tally — source: scripts/count_reconcile.py Counter 2, derived from
# MASTER-BIBLIOGRAPHY.md (tier audit 2026-08-19; recounted 2026-11-07 after the Zou
# arXiv 2507.20526 addition, and again later that day after the Petrescu ISSRE 2023 (A)
# and Madani C&ESAR 2026 (B) additions; then again after the 2026-11-07 phase 1 pass
# (two A→B re-tiers, nine snowball admissions at A): 243 blocks / 241 tiered / 2 stubs).
TALLY_DATE = '2026-11-07'
TIERED_TOTAL = 259
TALLY = {'A': 54, 'B': 168, 'C': 37}

COLORS = {'A': '#1B5E20', 'B': '#388E3C', 'C': '#F57C00'}
DESCRIPTIONS = {
    'A': 'Peer-reviewed research\nand official standards',
    'B': 'Practitioners, production\ndeployments, conference\ntalks, vendor docs',
    'C': 'Blog posts / vendor content\n(held provisionally,\nbias flagged)',
}


def create_evidence_distribution():
    """Render the live evidence-level distribution as a measurement."""

    fig, ax = plt.subplots(figsize=(12, 6.5))

    levels = list(TALLY.keys())
    counts = [TALLY[k] for k in levels]
    pcts = [100.0 * c / TIERED_TOTAL for c in counts]

    bars = ax.bar(range(len(levels)), pcts,
                  color=[COLORS[k] for k in levels],
                  alpha=0.9, edgecolor='black', linewidth=0.8, width=0.6)
    bars[0].set_hatch('///')
    bars[1].set_hatch('//')
    bars[2].set_hatch('xx')

    for i, (bar, k) in enumerate(zip(bars, levels)):
        h = bar.get_height()
        ax.text(bar.get_x() + bar.get_width() / 2, h + 1.2,
                f'Level {k}: {TALLY[k]}/{TIERED_TOTAL}\n({h:.1f}%)',
                ha='center', va='bottom', fontsize=12, fontweight='bold')
        ax.text(bar.get_x() + bar.get_width() / 2, h / 2, DESCRIPTIONS[k],
                ha='center', va='center', fontsize=9, color='white',
                fontweight='bold', linespacing=1.4)

    ax.set_xticks(range(len(levels)))
    ax.set_xticklabels([f'Level {k}' for k in levels], fontsize=12,
                       fontweight='bold')
    ax.set_ylabel('Share of tiered corpus (%)', fontsize=12, fontweight='bold')
    ax.set_ylim(0, 82)
    ax.grid(axis='y', alpha=0.3, linestyle=':', linewidth=0.5)

    ax.text(0.99, 0.97,
            f'Live per-source tally, {TALLY_DATE} '
            f'({TIERED_TOTAL} tiered entries; dashboard-computed, not self-graded).\n'
            'Replaces the withdrawn 79% self-grade (2026-06-14 audit).',
            transform=ax.transAxes, ha='right', va='top', fontsize=9,
            style='italic', color='#424242',
            bbox=dict(boxstyle='round,pad=0.4', facecolor='#F5F5F5',
                      edgecolor='#9E9E9E', linewidth=0.8))

    pct_a = round(TALLY['A'] / TIERED_TOTAL * 100, 1)
    fig.suptitle(f'Figure 2: Evidence Level Distribution — {pct_a}% Level A '
                 '(live per-source tally)',
                 fontsize=14, fontweight='bold', y=0.97)
    plt.tight_layout(rect=[0, 0, 1, 0.93])

    output_dir = os.path.dirname(os.path.abspath(__file__))
    plt.savefig(f'{output_dir}/figure2_evidence_distribution.png',
                dpi=300, bbox_inches='tight', facecolor='white')
    plt.savefig(f'{output_dir}/figure2_evidence_distribution.pdf',
                bbox_inches='tight', facecolor='white')

    print(f"Figure 2 rendered from live tally {TALLY} / {TIERED_TOTAL} "
          f"({TALLY_DATE}).")
    plt.close()


if __name__ == '__main__':
    create_evidence_distribution()
