#!/usr/bin/env python3
"""
Figure 2: Evidence Level Distribution
Publication-quality chart for systematic literature review

Creates horizontal bar chart showing evidence level distribution
with comparison to target and academic standards.
"""

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np

# Set publication-quality defaults
plt.rcParams['font.family'] = 'serif'
plt.rcParams['font.serif'] = ['Times New Roman', 'DejaVu Serif']
plt.rcParams['font.size'] = 11
plt.rcParams['axes.linewidth'] = 0.8
plt.rcParams['figure.dpi'] = 300

# Color palette (from FIGURES-AND-TABLES.md recommendations)
COLORS = {
    'level_a': '#2E7D32',  # Green for Evidence Level A
    'level_b': '#1976D2',  # Blue for Evidence Level B
    'target': '#757575',   # Gray for target line
    'comparison': '#FFA726'  # Orange for comparison bars
}

def create_evidence_distribution():
    """Create Figure 2: Evidence Level Distribution chart."""

    # Data
    data = {
        'Level A (Production/Academic/Government)': {
            'value': 79,
            'count': 57,
            'total': 72,
            'color': COLORS['level_a'],
            'subcategories': [
                'Production deployments: 18+ orgs',
                'Peer-reviewed research: 6 sources',
                'Government standards: 8 sources'
            ]
        },
        'Level B (Industry Analysts/Expert)': {
            'value': 21,
            'count': 15,
            'total': 72,
            'color': COLORS['level_b'],
            'subcategories': [
                'Industry analysts: 10 sources',
                'Expert validation: 3 sources',
                'Vendor docs (production): 2 sources'
            ]
        }
    }

    target_value = 73  # Target: 73% Level A

    # Create figure with two subplots
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))

    # ========== Subplot 1: Main Evidence Distribution ==========

    labels = list(data.keys())
    values = [data[label]['value'] for label in labels]
    colors = [data[label]['color'] for label in labels]

    # Create horizontal bars
    y_pos = np.arange(len(labels))
    bars = ax1.barh(y_pos, values, color=colors, alpha=0.9,
                     edgecolor='black', linewidth=0.8, height=0.6)

    # Add hatching for accessibility (not just color)
    bars[0].set_hatch('//')  # Level A with diagonal lines
    bars[1].set_hatch('\\\\')  # Level B with reverse diagonal

    # Add value labels on bars
    for i, (bar, label) in enumerate(zip(bars, labels)):
        width = bar.get_width()
        count = data[label]['count']
        total = data[label]['total']

        # Label inside bar (right side)
        ax1.text(width - 3, bar.get_y() + bar.get_height()/2,
                f'{width}%',
                ha='right', va='center', fontsize=13, fontweight='bold',
                color='white')

        # Count label outside bar
        ax1.text(width + 2, bar.get_y() + bar.get_height()/2,
                f'({count}/{total} sources)',
                ha='left', va='center', fontsize=10, style='italic')

    # Add target line for Level A
    ax1.axvline(x=target_value, color=COLORS['target'], linestyle='--',
                linewidth=2, label=f'Target: {target_value}% Level A')

    # Add "EXCEEDS TARGET" annotation
    ax1.annotate('EXCEEDS TARGET\n+6 percentage points',
                xy=(target_value, 0), xytext=(target_value + 8, 0.3),
                fontsize=10, fontweight='bold', color=COLORS['level_a'],
                bbox=dict(boxstyle='round,pad=0.5', facecolor='white',
                         edgecolor=COLORS['level_a'], linewidth=2),
                arrowprops=dict(arrowstyle='->', lw=1.5,
                              color=COLORS['level_a']))

    # Formatting
    ax1.set_yticks(y_pos)
    ax1.set_yticklabels(labels, fontsize=11)
    ax1.set_xlabel('Percentage of Sources (%)', fontsize=12, fontweight='bold')
    ax1.set_title('Evidence Level Distribution (n=72 sources)',
                 fontsize=14, fontweight='bold', pad=15)
    ax1.set_xlim(0, 100)
    ax1.grid(axis='x', alpha=0.3, linestyle=':', linewidth=0.5)
    ax1.legend(loc='lower right', fontsize=10, framealpha=0.9)

    # Add subcategory annotations
    for i, label in enumerate(labels):
        subcats = data[label]['subcategories']
        subcat_text = '\n'.join([f'  • {s}' for s in subcats])
        ax1.text(-2, i, subcat_text, ha='right', va='center',
                fontsize=8, style='italic', color='#424242')

    # ========== Subplot 2: Comparison to Academic Standards ==========

    comparison_data = {
        'Typical systematic review': 55,  # 50-60% midpoint
        'Medical systematic reviews': 65,  # 60-70% midpoint
        'This review (Level A)': 79
    }

    comp_labels = list(comparison_data.keys())
    comp_values = list(comparison_data.values())
    comp_colors = [COLORS['comparison'], COLORS['comparison'], COLORS['level_a']]

    y_pos2 = np.arange(len(comp_labels))
    bars2 = ax2.barh(y_pos2, comp_values, color=comp_colors, alpha=0.9,
                     edgecolor='black', linewidth=0.8, height=0.5)

    # Add hatching for this review
    bars2[2].set_hatch('//')

    # Add value labels
    for i, (bar, value) in enumerate(zip(bars2, comp_values)):
        width = bar.get_width()
        ax2.text(width + 1, bar.get_y() + bar.get_height()/2,
                f'{value}%',
                ha='left', va='center', fontsize=11, fontweight='bold')

    # Add "EXCEEDS" label
    ax2.text(82, 2, '✓ EXCEEDS', fontsize=11, fontweight='bold',
            color=COLORS['level_a'], va='center')

    # Formatting
    ax2.set_yticks(y_pos2)
    ax2.set_yticklabels(comp_labels, fontsize=11)
    ax2.set_xlabel('High-Quality Sources (%)', fontsize=12, fontweight='bold')
    ax2.set_title('Comparison to Academic Standards',
                 fontsize=14, fontweight='bold', pad=15)
    ax2.set_xlim(0, 100)
    ax2.grid(axis='x', alpha=0.3, linestyle=':', linewidth=0.5)

    # Overall figure title
    fig.suptitle('Figure 2: Evidence Level Distribution - 79% Level A Sources (Exceeds 73% Target)',
                fontsize=16, fontweight='bold', y=0.98)

    plt.tight_layout(rect=[0, 0, 1, 0.96])

    # Save in multiple formats
    output_dir = '/home/USER/security-data-literature-review/publication-graphics'
    plt.savefig(f'{output_dir}/figure2_evidence_distribution.png',
                dpi=300, bbox_inches='tight', facecolor='white')
    plt.savefig(f'{output_dir}/figure2_evidence_distribution.pdf',
                bbox_inches='tight', facecolor='white')

    print("✅ Figure 2 created successfully!")
    print(f"   - PNG: {output_dir}/figure2_evidence_distribution.png (300 DPI)")
    print(f"   - PDF: {output_dir}/figure2_evidence_distribution.pdf (vector)")

    # Optional: display if running interactively
    # plt.show()

    plt.close()

if __name__ == '__main__':
    create_evidence_distribution()
