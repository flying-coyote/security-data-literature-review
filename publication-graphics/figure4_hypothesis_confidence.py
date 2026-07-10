#!/usr/bin/env python3
"""
Figure 4: Hypothesis Validation Confidence Levels — post-audit re-score (2026-07-09)

Scores are the ADOPTED post-audit values from RESCORE-PROPOSAL-2026-07.md
(owner-ratified 2026-07-09), applied after the 2026-06 fabrications audit and
the 2026-07 per-citation verification sweep. Four hypotheses drop to
PRELIMINARY: their quantitative legs were withdrawn (fabricated attribution or
figures absent from cited sources) and no quantified support survives pending
re-sourcing. Labels carry no withdrawn figures.
"""

import os
import matplotlib.pyplot as plt
import numpy as np

# Set publication-quality defaults
plt.rcParams['font.family'] = 'serif'
plt.rcParams['font.serif'] = ['Times New Roman', 'DejaVu Serif']
plt.rcParams['font.size'] = 11
plt.rcParams['axes.linewidth'] = 0.8
plt.rcParams['figure.dpi'] = 300

COLORS = {
    'strong': '#1B5E20',       # ⭐⭐⭐⭐⭐
    'high': '#388E3C',         # ⭐⭐⭐⭐
    'moderate': '#F57C00',     # ⭐⭐⭐
    'preliminary': '#B71C1C',  # ⭐⭐ (quantitative legs withdrawn)
    'dimension': '#1976D2',
}
HATCHES = {'strong': '///', 'high': '//', 'moderate': 'xx', 'preliminary': '..'}
STARS = {'strong': '*****', 'high': '****', 'moderate': '***',
         'preliminary': '**'}

# Post-audit scores (RESCORE-PROPOSAL-2026-07.md, adopted 2026-07-09)
HYPOTHESES = {
    'H-ARCH-01\nIceberg Dominance': {
        'score': 23, 'level': 'strong',
        'label': 'Universal vendor support; 407 GitHub contributors; SK Telecom slides-verified'},
    'H3-PERF-01\nClickHouse': {
        'score': 20, 'level': 'high',
        'label': 'Cloudflare 6M req/sec verbatim-verified; 12-19x vs ES (vendor benchmark)'},
    'H-STREAM-01\nStateful Streaming': {
        'score': 17, 'level': 'high',
        'label': 'Samza VLDB 2017 (peer-reviewed); Azure 3T events/day verbatim-verified'},
    'H-COST-09\nTiered Storage': {
        'score': 8, 'level': 'preliminary',
        'label': 'Mechanism documented; savings band withdrawn 2026-06'},
    'H-IMPL-02\nStaffing Scarcity': {
        'score': 7, 'level': 'preliminary',
        'label': 'DORA attribution fabricated (withdrawn 2026-07); directional only'},
    'H-IMPL-03\nTimeline Premium': {
        'score': 7, 'level': 'preliminary',
        'label': 'Timeline figures withdrawn 2026-06/07; directional only'},
    'H-IMPL-01\nStreaming TCO': {
        'score': 6, 'level': 'preliminary',
        'label': 'DORA fabricated + TEI breakdown in neither doc; directional only'},
}


def create_hypothesis_confidence():
    """Create Figure 4 with adopted post-audit confidence scores."""

    fig = plt.figure(figsize=(16, 12))
    gs = fig.add_gridspec(3, 2, height_ratios=[2, 1.5, 1], hspace=0.4,
                          wspace=0.3)

    # ========== Subplot 1: Confidence Scores (Horizontal Bar) ==========
    ax1 = fig.add_subplot(gs[0, :])

    labels = list(HYPOTHESES.keys())
    scores = [HYPOTHESES[h]['score'] for h in labels]
    levels = [HYPOTHESES[h]['level'] for h in labels]
    colors = [COLORS[lv] for lv in levels]

    y_pos = np.arange(len(labels))
    bars = ax1.barh(y_pos, scores, color=colors, alpha=0.9,
                    edgecolor='black', linewidth=0.8, height=0.6)
    for bar, level in zip(bars, levels):
        bar.set_hatch(HATCHES[level])

    for i, (bar, hyp) in enumerate(zip(bars, labels)):
        width = bar.get_width()
        ax1.text(max(width - 1, 1.2), bar.get_y() + bar.get_height() / 2,
                 f'{scores[i]}/25', ha='right', va='center', fontsize=12,
                 fontweight='bold', color='white')
        ax1.text(width + 0.5, bar.get_y() + bar.get_height() / 2,
                 STARS[levels[i]], ha='left', va='center', fontsize=11)
        ax1.text(27, i, HYPOTHESES[hyp]['label'], ha='left', va='center',
                 fontsize=8, style='italic', color='#424242')

    ax1.axvline(x=19, color=COLORS['strong'], linestyle=':', linewidth=1.5,
                alpha=0.5, label='Strong threshold (19+)')
    ax1.axvline(x=15, color=COLORS['high'], linestyle=':', linewidth=1.5,
                alpha=0.5, label='High threshold (15+)')
    ax1.axvline(x=10, color=COLORS['moderate'], linestyle=':', linewidth=1.5,
                alpha=0.5, label='Moderate threshold (10+)')

    ax1.set_yticks(y_pos)
    ax1.set_yticklabels(labels, fontsize=11, fontweight='bold')
    ax1.set_xlabel('Confidence Score (out of 25 points)', fontsize=12,
                   fontweight='bold')
    ax1.set_title('Hypothesis Validation Confidence Levels — post-audit '
                  're-score, 2026-07-09 (7 hypotheses)',
                  fontsize=14, fontweight='bold', pad=15)
    ax1.set_xlim(0, 30)
    ax1.invert_yaxis()
    ax1.grid(axis='x', alpha=0.3, linestyle=':', linewidth=0.5)
    ax1.legend(loc='upper right', bbox_to_anchor=(1.0, -0.10), ncol=3, fontsize=9, frameon=False)

    # ========== Subplot 2: Distribution by Confidence Level ==========
    ax2 = fig.add_subplot(gs[1, 0])

    level_counts = {
        'Strongly\nValidated\n*****': (1, 'strong'),
        'High\nConfidence\n****': (2, 'high'),
        'Moderate\n***': (0, 'moderate'),
        'Preliminary\n**\n(withdrawn legs)': (4, 'preliminary'),
    }
    lv_labels = list(level_counts.keys())
    lv_values = [v[0] for v in level_counts.values()]
    lv_colors = [COLORS[v[1]] for v in level_counts.values()]

    bars2 = ax2.bar(range(len(lv_labels)), lv_values, color=lv_colors,
                    alpha=0.9, edgecolor='black', linewidth=0.8)
    for bar, (_, lv) in zip(bars2, level_counts.values()):
        bar.set_hatch(HATCHES[lv])
    for bar in bars2:
        h = bar.get_height()
        ax2.text(bar.get_x() + bar.get_width() / 2, h + 0.1,
                 f'{int(h)}', ha='center', va='bottom', fontsize=11,
                 fontweight='bold')

    ax2.set_xticks(range(len(lv_labels)))
    ax2.set_xticklabels(lv_labels, fontsize=9, fontweight='bold')
    ax2.set_ylabel('Number of Hypotheses', fontsize=11, fontweight='bold')
    ax2.set_title('Distribution by Confidence Level (post-audit)',
                  fontsize=13, fontweight='bold')
    ax2.set_ylim(0, 5)
    ax2.grid(axis='y', alpha=0.3, linestyle=':', linewidth=0.5)

    # ========== Subplot 3: Rubric example — H-ARCH-01 (strongest) ==========
    ax3 = fig.add_subplot(gs[1, 1])

    dimensions = ['Source Count', 'Evidence Quality', 'Source Diversity',
                  'Quantitative Precision', 'Geographic Diversity']
    example_scores = [5, 5, 4, 5, 4]  # H-ARCH-01 = 23/25

    x_pos = np.arange(len(dimensions))
    bars3 = ax3.barh(x_pos, example_scores, color=COLORS['dimension'],
                     alpha=0.9, edgecolor='black', linewidth=0.8)
    for bar, score in zip(bars3, example_scores):
        ax3.text(bar.get_width() + 0.1, bar.get_y() + bar.get_height() / 2,
                 f'{score}/5', ha='left', va='center', fontsize=10,
                 fontweight='bold')

    ax3.set_yticks(x_pos)
    ax3.set_yticklabels(dimensions, fontsize=10)
    ax3.set_xlabel('Score (out of 5 points)', fontsize=11, fontweight='bold')
    ax3.set_title('Example: H-ARCH-01 Scoring (strongest post-audit)',
                  fontsize=13, fontweight='bold', pad=10)
    ax3.set_xlim(0, 6)
    ax3.invert_yaxis()
    ax3.grid(axis='x', alpha=0.3, linestyle=':', linewidth=0.5)

    ax3.text(0.98, 0.05,
             f'Total: {sum(example_scores)}/25 points\n***** Strongly Validated',
             transform=ax3.transAxes, ha='right', va='bottom', fontsize=10,
             fontweight='bold',
             bbox=dict(boxstyle='round,pad=0.5', facecolor='#E8F5E9',
                       edgecolor=COLORS['strong'], linewidth=1.5))

    # ========== Subplot 4: Quality Summary ==========
    ax4 = fig.add_subplot(gs[2, :])
    ax4.axis('off')

    summary = """
    Post-audit validation summary (re-scored 2026-07-09; RESCORE-PROPOSAL-2026-07.md):
    - Architecture & performance findings VALIDATED on primary-verified production evidence:
      1 strongly validated (H-ARCH-01), 2 high confidence (H3-PERFORMANCE-01, H-STREAM-01).
    - Organizational-cost findings PRELIMINARY: 4 hypotheses (H-IMPL-01/02/03, H-COST-09) lost their
      quantitative legs to the 2026-06 audit and 2026-07 verification sweep (fabricated attribution or
      figures absent from cited sources); each is stated directionally pending re-sourcing.
    - Every score reflects only evidence that survived primary-source verification.
    """

    ax4.text(0.5, 0.5, summary.strip(), ha='center', va='center', fontsize=10,
             transform=ax4.transAxes,
             bbox=dict(boxstyle='round,pad=1', facecolor='#F5F5F5',
                       edgecolor='black', linewidth=1.5),
             family='monospace')

    fig.suptitle('Figure 4: Hypothesis Validation Confidence Levels — '
                 'post-audit re-score (2026-07-09)',
                 fontsize=16, fontweight='bold', y=0.98)

    output_dir = os.path.expanduser(
        '~/security-data-literature-review/publication-graphics')
    plt.savefig(f'{output_dir}/figure4_hypothesis_confidence.png',
                dpi=300, bbox_inches='tight', facecolor='white')
    plt.savefig(f'{output_dir}/figure4_hypothesis_confidence.pdf',
                bbox_inches='tight', facecolor='white')

    print("Figure 4 rendered with adopted post-audit scores.")
    plt.close()


if __name__ == '__main__':
    create_hypothesis_confidence()
