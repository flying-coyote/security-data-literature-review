#!/usr/bin/env python3
"""
Figure 2: Evidence Level Distribution — live re-verified tally (2026-07-09)

History: the original chart asserted "79% Evidence Level A (exceeds 73% target)".
The 2026-06-14 audit withdrew that self-grade (Level A overstated, entries
removed) and this script rendered a withdrawal notice, with the condition that
the chart not return without a re-verified per-source tally.

That condition is now met: the 2026-07 monthly update reconciled the corpus to
179 blocks / 177 tiered and the dashboard live-computes the tier mix from
per-entry Evidence-Level markers (automation_dashboard.py, fixed 2026-07-09).
This chart states the honest figure — 42.9% Level A, BELOW the 70% target —
rather than a self-grade. Update the TALLY constants from the dashboard before
regenerating; do not hand-edit percentages.
"""

import os
import matplotlib.pyplot as plt

# Set publication-quality defaults
plt.rcParams['font.family'] = 'serif'
plt.rcParams['font.serif'] = ['Times New Roman', 'DejaVu Serif']
plt.rcParams['font.size'] = 11
plt.rcParams['axes.linewidth'] = 0.8
plt.rcParams['figure.dpi'] = 300

# Live tally — source: automation_dashboard.py live computation, 2026-07-09
TALLY_DATE = '2026-07-09'
TIERED_TOTAL = 177
TALLY = {'A': 76, 'B': 85, 'C': 16}
TARGET_A_PCT = 70  # manuscript Table 1 target (>70% Level A)

COLORS = {'A': '#1B5E20', 'B': '#388E3C', 'C': '#F57C00'}
DESCRIPTIONS = {
    'A': 'Production deployments,\npeer-reviewed research,\ngovernment standards',
    'B': 'Industry analysts,\nexpert validation,\nvendor technical docs',
    'C': 'Blog posts / vendor content\n(held provisionally,\nbias flagged)',
}


def create_evidence_distribution():
    """Render the live evidence-level distribution with the honest target gap."""

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

    ax.axhline(y=TARGET_A_PCT, color='#B71C1C', linestyle='--', linewidth=1.5,
               alpha=0.8)
    ax.text(2.35, TARGET_A_PCT + 1.5, f'Level-A target (>{TARGET_A_PCT}%)',
            ha='right', va='bottom', fontsize=10, color='#B71C1C',
            fontweight='bold')

    gap = TARGET_A_PCT - pcts[0]
    ax.annotate('', xy=(0, TARGET_A_PCT), xytext=(0, pcts[0]),
                arrowprops=dict(arrowstyle='<->', color='#B71C1C', lw=1.2))
    ax.text(0.12, (TARGET_A_PCT + pcts[0]) / 2,
            f'−{gap:.1f} pts\nbelow target',
            ha='left', va='center', fontsize=9.5, color='#B71C1C',
            fontweight='bold')

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

    fig.suptitle('Figure 2: Evidence Level Distribution — 42.9% Level A '
                 '(below the 70% target; honest live tally)',
                 fontsize=14, fontweight='bold', y=0.97)
    plt.tight_layout(rect=[0, 0, 1, 0.93])

    output_dir = os.path.expanduser(
        '~/security-data-literature-review/publication-graphics')
    plt.savefig(f'{output_dir}/figure2_evidence_distribution.png',
                dpi=300, bbox_inches='tight', facecolor='white')
    plt.savefig(f'{output_dir}/figure2_evidence_distribution.pdf',
                bbox_inches='tight', facecolor='white')

    print(f"Figure 2 rendered from live tally {TALLY} / {TIERED_TOTAL} "
          f"({TALLY_DATE}).")
    plt.close()


if __name__ == '__main__':
    create_evidence_distribution()
