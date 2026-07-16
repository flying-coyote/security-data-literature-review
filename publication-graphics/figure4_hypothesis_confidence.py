#!/usr/bin/env python3
"""
Figure 4: Hypothesis Validation Confidence Levels — rubric rescore (2026-07-13)

Scores are the mechanical application of methods/scoring-rubric.md (the explicit
instrument of record, ruling G-R4) to the nine hypotheses, computed in
methods/RESCORE-2026-07-13.md. They supersede the 2026-07-09 adopted values from
RESCORE-PROPOSAL-2026-07.md where the two differ: those totals were directionally
right but contained interpolated dimension values with no anchor a reviewer could
re-derive them from.

What moved: H3-PERFORMANCE-01 20 -> 19, H-STREAM-01 17 -> 15 (High -> Moderate;
the section cites two legs after the Uber withdrawal, and the source-count anchor
prices 1-2 sources at 1 point), H-SOC-BASELINE-01 14 -> 13, H-COST-09 8 -> 9 (the
first-party S3 tier-delta derivation lands), and the three H-IMPL hypotheses
collapse to the instrument's 5/25 floor, retiring their 6/7/7 gradation. Band
thresholds are drawn at the rubric's boundaries (21/16/11), not the 19/15/10 this
script previously used. Labels carry no withdrawn figures.
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

# Rescored under methods/scoring-rubric.md (methods/RESCORE-2026-07-13.md).
# Ordered by descending total, ties alphabetical by hypothesis ID (rubric section 3).
# 'dims' = source count / evidence quality / source diversity / quantitative
# precision / geographic-organizational diversity; each sums to 'score'.
HYPOTHESES = {
    'H-ARCH-01\nIceberg Dominance': {
        'score': 23, 'level': 'strong', 'dims': [5, 5, 5, 3, 5],
        'label': 'Broad vendor support; 407 GitHub contributors; SK Telecom slides-verified'},
    'H3-PERF-01\nClickHouse': {
        'score': 19, 'level': 'high', 'dims': [5, 3, 3, 5, 3],
        'label': 'Cloudflare 6M req/sec verbatim-verified; 4 legs, 3 at Level A; first-party CIDR probe'},
    'H-LOGCOMP-01 \u2020\nMachine-Data Compression': {
        'score': 17, 'level': 'high', 'dims': [3, 5, 1, 5, 3],
        'label': 'LogLite + PBC + Pebbles (peer-reviewed, verbatim-verified); two independent author groups'},
    'H-STREAM-01\nStateful Streaming': {
        'score': 15, 'level': 'moderate', 'dims': [1, 5, 3, 3, 3],
        'label': 'Samza VLDB 2017 + Azure verbatim-verified; two legs cap the source count'},
    'H-SOC-BASELINE-01 \u2020\nSOC Alert Base Rates': {
        'score': 13, 'level': 'moderate', 'dims': [1, 5, 1, 5, 1],
        'label': 'Yang USENIX Sec 24: 24K-134K alerts/day, ~0.01% true attacks; single-source cap'},
    'H-COST-09\nTiered Storage': {
        'score': 9, 'level': 'preliminary', 'dims': [1, 1, 1, 3, 3],
        'label': 'Mechanism documented; savings band withdrawn 2026-06; S3 tier-delta bounds the saving'},
    'H-IMPL-01\nStreaming TCO': {
        'score': 5, 'level': 'preliminary', 'dims': [1, 1, 1, 1, 1],
        'label': 'DORA fabricated + TEI breakdown in neither doc; no scoreable leg, instrument floor'},
    'H-IMPL-02\nStaffing Scarcity': {
        'score': 5, 'level': 'preliminary', 'dims': [1, 1, 1, 1, 1],
        'label': 'DORA attribution fabricated (withdrawn 2026-07); no scoreable leg, instrument floor'},
    'H-IMPL-03\nTimeline Premium': {
        'score': 5, 'level': 'preliminary', 'dims': [1, 1, 1, 1, 1],
        'label': 'Timeline figures withdrawn 2026-06/07; no scoreable leg, instrument floor'},
}

# Guard: every stated total must equal the sum of its five anchor dimensions.
for _name, _h in HYPOTHESES.items():
    assert sum(_h['dims']) == _h['score'], f"{_name}: dims do not sum to score"


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

    # Band boundaries per methods/scoring-rubric.md section 3 (21-25 / 16-20 /
    # 11-15 / 5-10). The 19/15/10 lines this script drew before contradicted the
    # rubric they were meant to illustrate.
    ax1.axvline(x=21, color=COLORS['strong'], linestyle=':', linewidth=1.5,
                alpha=0.5, label='Strongly Validated (21+)')
    ax1.axvline(x=16, color=COLORS['high'], linestyle=':', linewidth=1.5,
                alpha=0.5, label='High Confidence (16+)')
    ax1.axvline(x=11, color=COLORS['moderate'], linestyle=':', linewidth=1.5,
                alpha=0.5, label='Moderate (11+)')

    ax1.set_yticks(y_pos)
    ax1.set_yticklabels(labels, fontsize=11, fontweight='bold')
    ax1.set_xlabel('Confidence Score (out of 25 points)', fontsize=12,
                   fontweight='bold')
    ax1.set_title('Hypothesis Validation Confidence Levels — rubric rescore, '
                  '2026-07-13 (9 hypotheses; \u2020 = added post-audit 2026-07-10)',
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
        'Moderate\n***': (2, 'moderate'),
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
    ax2.set_title('Distribution by Confidence Level (2026-07-13 rescore)',
                  fontsize=13, fontweight='bold')
    ax2.set_ylim(0, 5)
    ax2.grid(axis='y', alpha=0.3, linestyle=':', linewidth=0.5)

    # ========== Subplot 3: Rubric example — H-ARCH-01 (strongest) ==========
    ax3 = fig.add_subplot(gs[1, 1])

    dimensions = ['Source Count', 'Evidence Quality', 'Source Diversity',
                  'Quantitative Precision', 'Geographic Diversity']
    # Read the worked example straight from the scored data so the panel cannot
    # drift from the bars above it (rubric section 4: H-ARCH-01, 5/5/5/3/5 = 23/25).
    example_scores = HYPOTHESES['H-ARCH-01\nIceberg Dominance']['dims']

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
    ax3.set_title('Example: H-ARCH-01 Scoring (strongest; rubric section 4)',
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
    Confidence rescore, 2026-07-13 (methods/scoring-rubric.md; applied in methods/RESCORE-2026-07-13.md):
    - Every score is the sum of five anchor-valued dimensions, so a reviewer holding the rubric and the
      bibliography re-derives it. Bands: 21-25 Strongly Validated, 16-20 High, 11-15 Moderate, 5-10 Preliminary.
    - 1 strongly validated (H-ARCH-01), 2 high confidence (H3-PERFORMANCE-01, H-LOGCOMP-01),
      2 moderate (H-STREAM-01, H-SOC-BASELINE-01), 4 preliminary (H-COST-09, H-IMPL-01/02/03).
    - H-STREAM-01 moves High -> Moderate: after the Uber withdrawal the section cites two legs, and the
      source-count anchor prices 1-2 sources at 1 point. One further verified leg restores it to 17/25.
    - H-IMPL-01/02/03 sit at the instrument's 5/25 floor: no scoreable leg survives the audits, and their
      former 6/7/7 gradation was judgment the rubric cannot express.
    - Every score reflects only evidence that survived primary-source verification.
    """

    ax4.text(0.5, 0.5, summary.strip(), ha='center', va='center', fontsize=10,
             transform=ax4.transAxes,
             bbox=dict(boxstyle='round,pad=1', facecolor='#F5F5F5',
                       edgecolor='black', linewidth=1.5),
             family='monospace')

    fig.suptitle('Figure 4: Hypothesis Validation Confidence Levels — '
                 'rubric rescore (2026-07-13)',
                 fontsize=16, fontweight='bold', y=0.98)

    output_dir = os.path.dirname(os.path.abspath(__file__))
    plt.savefig(f'{output_dir}/figure4_hypothesis_confidence.png',
                dpi=300, bbox_inches='tight', facecolor='white')
    plt.savefig(f'{output_dir}/figure4_hypothesis_confidence.pdf',
                bbox_inches='tight', facecolor='white')

    print("Figure 4 rendered with the 2026-07-13 rubric rescore.")
    plt.close()


if __name__ == '__main__':
    create_hypothesis_confidence()
