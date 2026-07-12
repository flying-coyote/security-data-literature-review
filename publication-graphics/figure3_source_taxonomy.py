#!/usr/bin/env python3
"""
Figure 3: Source Type Taxonomy
Publication-quality chart for systematic literature review

Creates stacked/grouped visualization showing source type distribution
with geographic and organizational diversity.
"""

import os
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np

# Set publication-quality defaults
plt.rcParams['font.family'] = 'serif'
plt.rcParams['font.serif'] = ['Times New Roman', 'DejaVu Serif']
plt.rcParams['font.size'] = 11
plt.rcParams['axes.linewidth'] = 0.8
plt.rcParams['figure.dpi'] = 300

# Color palette
COLORS = {
    'production': '#1976D2',      # Blue
    'government': '#2E7D32',      # Green
    'analyst': '#F57C00',         # Orange
    'academic': '#7B1FA2',        # Purple
    'vendor': '#00796B',          # Teal
    'us': '#1976D2',
    'europe': '#388E3C',
    'asia': '#F57C00',
    'international': '#7B1FA2'
}

def create_source_taxonomy():
    """Create Figure 3: Source Type Taxonomy chart."""

    # Data for source type distribution
    source_types = {
        'Production\nDeployments': {
            'count': 17,
            'percentage': 23,
            'color': COLORS['production'],
            'examples': ['Netflix', 'Uber', 'LinkedIn', 'Cloudflare', 'SK Telecom']
        },
        'Vendor\nDocumentation': {
            'count': 33,
            'percentage': 45,
            'color': COLORS['vendor'],
            'examples': ['Apache', 'Confluent', 'ClickHouse', 'AWS', 'Databricks']
        },
        'Industry\nAnalysts': {
            'count': 10,
            'percentage': 13,
            'color': COLORS['analyst'],
            'examples': ['Gartner', 'IDC', 'Forrester', 'DORA']
        },
        'Government/\nStandards': {
            'count': 8,
            'percentage': 11,
            'color': COLORS['government'],
            'examples': ['CISA', 'MITRE', 'DARPA', 'NSA', 'SANS']
        },
        'Academic/\nResearch': {
            'count': 6,
            'percentage': 8,
            'color': COLORS['academic'],
            'examples': ['DARPA XAI', 'Peer-reviewed', 'O\'Reilly books']
        }
    }

    # Geographic distribution
    geographic = {
        'United States': {'percentage': 80, 'sources': '60+'},
        'Europe': {'percentage': 11, 'sources': '8+'},
        'Asia-Pacific': {'percentage': 4, 'sources': '3+'},
        'International': {'percentage': 5, 'sources': '4+'}
    }

    # Create figure with two subplots
    fig = plt.figure(figsize=(16, 10))
    gs = fig.add_gridspec(3, 2, height_ratios=[2, 1, 1], hspace=0.4, wspace=0.3)

    # ========== Subplot 1: Source Type Distribution (Horizontal Bar) ==========
    ax1 = fig.add_subplot(gs[0, :])

    labels = list(source_types.keys())
    counts = [source_types[label]['count'] for label in labels]
    percentages = [source_types[label]['percentage'] for label in labels]
    colors = [source_types[label]['color'] for label in labels]

    y_pos = np.arange(len(labels))
    bars = ax1.barh(y_pos, percentages, color=colors, alpha=0.9,
                     edgecolor='black', linewidth=0.8, height=0.6)

    # Add hatching patterns for accessibility
    hatches = ['//', '\\\\', 'xx', '++', '||']
    for bar, hatch in zip(bars, hatches):
        bar.set_hatch(hatch)

    # Add labels
    for i, (bar, label) in enumerate(zip(bars, labels)):
        width = bar.get_width()
        count = counts[i]
        percentage = percentages[i]

        # Percentage inside bar
        ax1.text(width/2, bar.get_y() + bar.get_height()/2,
                f'{percentage}%',
                ha='center', va='center', fontsize=13, fontweight='bold',
                color='white')

        # Count outside bar
        ax1.text(width + 1, bar.get_y() + bar.get_height()/2,
                f'n={count}',
                ha='left', va='center', fontsize=11, fontweight='bold')

        # Examples on left side
        examples = source_types[label]['examples']
        example_text = ', '.join(examples[:3])
        if len(examples) > 3:
            example_text += ', etc.'
        ax1.text(-2, i, example_text, ha='right', va='center',
                fontsize=9, style='italic', color='#424242')

    # Formatting
    ax1.set_yticks(y_pos)
    ax1.set_yticklabels(labels, fontsize=12, fontweight='bold')
    ax1.set_xlabel('Percentage of Total Sources (%)', fontsize=12, fontweight='bold')
    ax1.set_title('Source Type Distribution (n=74 sources)',
                 fontsize=14, fontweight='bold', pad=15)
    ax1.set_xlim(0, 50)
    ax1.grid(axis='x', alpha=0.3, linestyle=':', linewidth=0.5)

    # ========== Subplot 2: Geographic Distribution (Pie Chart) ==========
    ax2 = fig.add_subplot(gs[1, 0])

    geo_labels = list(geographic.keys())
    geo_values = [geographic[label]['percentage'] for label in geo_labels]
    geo_colors = [COLORS['us'], COLORS['europe'], COLORS['asia'], COLORS['international']]

    wedges, texts, autotexts = ax2.pie(geo_values, labels=geo_labels,
                                        autopct='%1.0f%%',
                                        colors=geo_colors,
                                        startangle=90,
                                        explode=[0.05, 0, 0, 0],
                                        textprops={'fontsize': 10, 'fontweight': 'bold'},
                                        wedgeprops={'linewidth': 1, 'edgecolor': 'black'})

    # Add source counts as annotations
    for i, (label, autotext) in enumerate(zip(geo_labels, autotexts)):
        sources = geographic[label]['sources']
        autotext.set_color('white')
        autotext.set_fontsize(11)

    ax2.set_title('Geographic Distribution', fontsize=13, fontweight='bold', pad=10)

    # ========== Subplot 3: Organizational Diversity (Text Summary) ==========
    ax3 = fig.add_subplot(gs[1, 1])
    ax3.axis('off')

    org_diversity = [
        ('Tech Giants', 'Netflix, Uber, LinkedIn, Microsoft, Google, AWS, Cloudflare'),
        ('Enterprises', 'SK Telecom, Nordstrom, Disney+'),
        ('Government', 'CISA, MITRE, DARPA, NSA, SANS'),
        ('Standards', 'Apache SF, CSA, OCA, OASIS'),
        ('Startups', 'DataRobot, Anyscale, Huntress')
    ]

    y_start = 0.95
    y_step = 0.18

    ax3.text(0.5, y_start + 0.05, 'Organizational Diversity',
            ha='center', va='top', fontsize=13, fontweight='bold',
            transform=ax3.transAxes)

    for i, (org_type, examples) in enumerate(org_diversity):
        y = y_start - (i * y_step)

        # Type label (bold)
        ax3.text(0.05, y, f'{org_type}:',
                ha='left', va='top', fontsize=10, fontweight='bold',
                transform=ax3.transAxes)

        # Examples (italic, wrapped)
        ax3.text(0.05, y - 0.04, examples,
                ha='left', va='top', fontsize=9, style='italic',
                wrap=True, transform=ax3.transAxes, color='#424242')

    # Add border
    rect = mpatches.Rectangle((0.02, 0.02), 0.96, 0.96,
                              linewidth=1.5, edgecolor='black',
                              facecolor='none', transform=ax3.transAxes)
    ax3.add_patch(rect)

    # ========== Subplot 4: Quality Summary (Text) ==========
    ax4 = fig.add_subplot(gs[2, :])
    ax4.axis('off')

    summary_text = """
    Quality Metrics Summary:
    • Total Sources: 74 sources documented (100% extraction from 283 footnotes)
    • Evidence Level: aggregate Level-A self-grade WITHDRAWN (2026-06-14 audit) — per-source levels provisional, no aggregate % claimed pending re-verification (see FIGURES-AND-TABLES.md)
    • Evidence levels (A/B/C/D) are classified per-source; the prior aggregate Level-A distribution (exceeds-target framing) is withdrawn
    • Geographic Diversity: 3 regions (US 80%, Europe 11%, Asia-Pacific 4%)
    • Organizational Diversity: 5 types (Tech giants, Enterprises, Government, Standards bodies, Startups)
    • URL Validation: 73% overall, 100% hypothesis-critical sources validated ✓
    """

    ax4.text(0.5, 0.5, summary_text.strip(),
            ha='center', va='center', fontsize=10,
            transform=ax4.transAxes,
            bbox=dict(boxstyle='round,pad=1', facecolor='#F5F5F5',
                     edgecolor='black', linewidth=1.5),
            family='monospace')

    # Overall figure title
    fig.suptitle('Figure 3: Source Type Taxonomy — 74 Sources with Geographic & Organizational Diversity',
                fontsize=16, fontweight='bold', y=0.98)

    # Save
    output_dir = os.path.expanduser('~/security-data-literature-review/publication-graphics')
    plt.savefig(f'{output_dir}/figure3_source_taxonomy.png',
                dpi=300, bbox_inches='tight', facecolor='white')
    plt.savefig(f'{output_dir}/figure3_source_taxonomy.pdf',
                bbox_inches='tight', facecolor='white')

    print("✅ Figure 3 created successfully!")
    print(f"   - PNG: {output_dir}/figure3_source_taxonomy.png (300 DPI)")
    print(f"   - PDF: {output_dir}/figure3_source_taxonomy.pdf (vector)")

    plt.close()

if __name__ == '__main__':
    create_source_taxonomy()
