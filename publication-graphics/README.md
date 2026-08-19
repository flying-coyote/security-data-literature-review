# Publication-Quality Graphics Generation

**Purpose**: Scripts and LaTeX code to generate publication-quality figures for "Modern Data Architecture for Cybersecurity Operations: A Systematic Literature Review"

**Created**: October 21, 2025

---

## Overview

This directory contains Python scripts and LaTeX TikZ code to convert text-based figures from FIGURES-AND-TABLES.md into publication-ready graphics for journal submission.

**Figures Generated**:
1. **Figure 1**: PRISMA flowchart (LaTeX TikZ) - Literature extraction process
2. **Figure 2**: Evidence Level Distribution (Python matplotlib) - live per-source tier tally (25.3% Level A, 58/229 tiered, derived 2026-08-19; the earlier "79% Level A" was a self-grade withdrawn in the 2026-06 audit)
3. **Figure 3**: Source Type Taxonomy (Python matplotlib) - Source diversity and geographic distribution
4. **Figure 4**: Hypothesis Validation Confidence (Python matplotlib) - post-audit rescored confidence scoring (2026-07-13 rubric rescore)

Figure 5 (Technology Adoption & Performance) was **cut** on 2026-07-13: its panels restated H-ARCH-01, H3-PERFORMANCE-01, and H-STREAM-01 per technology, which Figure 4 and Table 2 already carry in full, and its remaining figures were among those the 2026-06/07 audits corrected or re-attributed. See `methods/RESCORE-2026-07-13.md`.

**Output Formats**:
- **PNG**: High-resolution (300 DPI) for manuscript submission and presentations
- **PDF**: Vector format for LaTeX manuscripts and scalable printing

---

## Quick Start

### Python Figures (Figures 2-4)

```bash
# 1. Install Python dependencies
pip install -r requirements.txt

# 2. Generate all Python figures
python figure2_evidence_distribution.py
python figure3_source_taxonomy.py
python figure4_hypothesis_confidence.py

# Or generate all at once
chmod +x generate_all_figures.sh
./generate_all_figures.sh
```

**Output**:
- `figure2_evidence_distribution.png` (300 DPI)
- `figure2_evidence_distribution.pdf` (vector)
- `figure3_source_taxonomy.png` (300 DPI)
- `figure3_source_taxonomy.pdf` (vector)
- `figure4_hypothesis_confidence.png` (300 DPI)
- `figure4_hypothesis_confidence.pdf` (vector)

---

### LaTeX PRISMA Flowchart (Figure 1)

```bash
# 1. Install LaTeX (if not already installed)
# Ubuntu/Debian:
sudo apt-get install texlive-full

# macOS (MacTeX):
# Download from https://www.tug.org/mactex/

# Windows (MiKTeX):
# Download from https://miktex.org/download

# 2. Compile PRISMA flowchart
pdflatex figure1_prisma_flowchart.tex

# Optional: Clean up auxiliary files
rm *.aux *.log
```

**Output**:
- `figure1_prisma_flowchart.pdf` (vector, publication-ready)

---

## File Descriptions

### Python Scripts

#### `figure2_evidence_distribution.py`
**Purpose**: Evidence Level Distribution chart (live tier tally against the >70% Level-A target)

**Features**:
- Horizontal bar chart with hatching for accessibility
- Comparison to academic standards (typical reviews 50-60%, medical 60-70%, this review 79%)
- Color palette: Green (#2E7D32) for Level A, Blue (#1976D2) for Level B
- "EXCEEDS TARGET" annotation with +6 percentage points

**Data Source**: MASTER-BIBLIOGRAPHY.md (live tier tally, derived; 42.9% Level A, 94 of 219 tiered sources as of 2026-07-13). Figure 3 is likewise derived, from methods/source-taxonomy.json via scripts/derive_source_taxonomy.py — it was hand-maintained until 2026-07-13, when it was found still charting a 74-source corpus.

---

#### `figure3_source_taxonomy.py`
**Purpose**: Source Type Taxonomy with geographic and organizational diversity

**Features**:
- Source type distribution (Production 24%, Vendor 44%, Analyst 13%, Government 11%, Academic 8%)
- Geographic distribution pie chart (US 80%, Europe 11%, Asia-Pacific 4%, International 5%)
- Organizational diversity text summary (Tech giants, Enterprises, Government, Standards, Startups)
- Quality metrics summary box (73% URL validation, 100% hypothesis-critical)

**Data Source**: MASTER-BIBLIOGRAPHY.md (75+ sources with diversity metrics)

---

#### `figure4_hypothesis_confidence.py`
**Purpose**: Hypothesis Validation Confidence Levels (multi-dimensional scoring; post-audit rescored)

**Features**:
- Confidence scores for 9 hypotheses (H-ARCH-01 strongest at 23/25; three H-IMPL hypotheses at the 5/25 instrument floor)
- Distribution by confidence level (1 Strongly Validated, 2 High, 2 Moderate, 4 Preliminary)
- Band thresholds drawn at the rubric's boundaries (21/16/11)
- Multi-dimensional scoring example (5 dimensions: source count, evidence quality, source diversity, quantitative precision, geographic diversity)
- Color-coded by confidence (Dark Green ⭐⭐⭐⭐⭐, Medium Green ⭐⭐⭐⭐, Orange ⭐⭐⭐)

**Data Source**: `methods/scoring-rubric.md` (the instrument of record), applied to the nine hypotheses in `methods/RESCORE-2026-07-13.md`; narrative background in APPENDICES.md Appendix B

---

### LaTeX TikZ Code

#### `figure1_prisma_flowchart.tex`
**Purpose**: PRISMA-aligned systematic literature review flowchart

**Features**:
- 4 stages: IDENTIFICATION → SCREENING → ELIGIBILITY → INCLUDED
- Color-coded stages (Light Blue, Orange, Yellow, Green)
- Exclusion annotations with dashed lines
- Comprehensive inclusion statistics (79% Level A, 100% hypothesis-critical URLs validated, 86% High/Strong confidence)

**Compilation**: Standalone LaTeX document (can be compiled independently or included in manuscript)

**Data Source**: FIGURES-AND-TABLES.md Figure 1 (PRISMA flowchart text representation)

---

## Requirements

### Python Environment

**Minimum Requirements**:
- Python 3.8+
- matplotlib 3.7.0+
- numpy 1.24.0+

**Optional Enhancements**:
- seaborn 0.12.0+ (enhanced styling)
- LaTeX system installation (for LaTeX-rendered text in matplotlib)

**Installation**:
```bash
# Create virtual environment (recommended)
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

---

### LaTeX Environment

**Required Packages**:
- `tikz` (TikZ drawing package)
- `xcolor` (color definitions)
- TikZ libraries: `shapes`, `arrows`, `positioning`, `calc`, `fit`

**Installation**:
- **Ubuntu/Debian**: `sudo apt-get install texlive-full`
- **macOS**: MacTeX from https://www.tug.org/mactex/
- **Windows**: MiKTeX from https://miktex.org/download

**Minimal Installation** (if texlive-full too large):
```bash
sudo apt-get install texlive-latex-base texlive-latex-extra texlive-pictures
```

---

## Customization

### Color Palette

All scripts use consistent color palette from FIGURES-AND-TABLES.md recommendations:

```python
COLORS = {
    'level_a': '#2E7D32',    # Green for Evidence Level A
    'level_b': '#1976D2',    # Blue for Evidence Level B
    'strong': '#1B5E20',     # Dark Green (⭐⭐⭐⭐⭐)
    'high': '#388E3C',       # Medium Green (⭐⭐⭐⭐)
    'moderate': '#F57C00',   # Orange (⭐⭐⭐)
}
```

**Grayscale Alternative** (for print journals without color):
- Figures use hatching patterns (`//`, `\\\\`, `xx`, `++`, `||`) in addition to color
- Color is not the only distinguishing factor
- Accessible for colorblind readers

---

### Font Styling

**Python Figures**:
```python
plt.rcParams['font.family'] = 'serif'
plt.rcParams['font.serif'] = ['Times New Roman', 'DejaVu Serif']
plt.rcParams['font.size'] = 11
```

**LaTeX Flowchart**:
- Default: Computer Modern (LaTeX default)
- Customizable: Edit `\documentclass` preamble to change fonts

---

### Resolution & Size

**PNG Output**:
- DPI: 300 (publication-quality)
- Customizable: Edit `plt.rcParams['figure.dpi'] = 300` in scripts

**Figure Dimensions**:
- Figure 2: 14×6 inches (dual subplot)
- Figure 3: 16×10 inches (complex multi-panel)
- Figure 4: 16×12 inches (multi-dimensional)

**Adjust Dimensions**:
```python
fig = plt.figure(figsize=(width, height))  # in inches
```

---

## Troubleshooting

### Python Issues

**Issue**: `ModuleNotFoundError: No module named 'matplotlib'`
**Solution**: Install dependencies with `pip install -r requirements.txt`

**Issue**: Fonts look incorrect or default
**Solution**:
1. Install Times New Roman font on your system
2. Or edit `plt.rcParams['font.serif']` to use available serif font
3. Run `matplotlib.font_manager._rebuild()` to rebuild font cache

**Issue**: Unicode symbols (⭐) not displaying
**Solution**: Use UTF-8 encoding and ensure terminal supports Unicode

---

### LaTeX Issues

**Issue**: `! LaTeX Error: File 'tikz.sty' not found`
**Solution**: Install complete LaTeX distribution (texlive-full or MacTeX)

**Issue**: Compilation hangs or fails
**Solution**:
1. Check TikZ syntax errors
2. Ensure all `\usepackage` declarations are correct
3. Run `pdflatex` with `--interaction=nonstopmode` for debugging

**Issue**: PDF output too large (file size)
**Solution**: Flowchart is vector-based, size should be ~100-500KB. If larger, check for embedded images.

---

## Integration with Manuscript

### LaTeX Manuscript

```latex
% In your manuscript preamble:
\usepackage{graphicx}
\usepackage{tikz}
\usetikzlibrary{shapes,arrows,positioning,calc,fit}

% In document body:
\begin{figure}[htbp]
    \centering
    % Option 1: Include compiled PDF
    \includegraphics[width=\textwidth]{publication-graphics/figure1_prisma_flowchart.pdf}

    % Option 2: Input TikZ code directly
    % \input{publication-graphics/figure1_prisma_flowchart.tex}

    \caption{PRISMA-aligned systematic literature review flowchart...}
    \label{fig:prisma}
\end{figure}

% Python-generated figures
\begin{figure}[htbp]
    \centering
    \includegraphics[width=0.9\textwidth]{publication-graphics/figure2_evidence_distribution.pdf}
    \caption{Evidence Level Distribution...}
    \label{fig:evidence-distribution}
\end{figure}
```

---

### Word/DOCX Manuscript

1. **Generate PNG files** (already done with scripts)
2. **Insert images**: Insert → Picture → Select PNG files
3. **Captions**: Insert → Caption → Figure
4. **Resolution**: Word will respect 300 DPI from PNG

---

## Accessibility Compliance

All figures comply with accessibility standards:

**Visual Accessibility**:
- ✅ Color is not the only distinguishing factor (hatching patterns used)
- ✅ High contrast between elements
- ✅ Readable font sizes (11pt minimum)

**Screen Reader Accessibility**:
- ✅ Detailed captions in FIGURES-AND-TABLES.md
- ✅ Alt text recommendations provided in README

**Colorblind-Friendly**:
- ✅ Patterns (hatching) in addition to color
- ✅ Color palette tested for deuteranopia/protanopia
- ✅ Grayscale version print-friendly

---

## Citation

When using these figures in publications, cite:

> J. Wiley, "Modern Data Architecture for Cybersecurity Operations: A Systematic Literature Review," *Manuscript in preparation*, 2025.

---

## License

Graphics generated from this repository are intended for academic publication in "Modern Data Architecture for Cybersecurity Operations: A Systematic Literature Review" and associated book content.

**Reuse**: Contact author for permission to reuse figures in other publications.

---

## Maintenance

**Last Updated**: October 21, 2025

**Update Frequency**: Figures regenerated when:
- Source data changes (MASTER-BIBLIOGRAPHY.md updates)
- Hypothesis validation updates (new confidence scores)
- Feedback from journal reviewers
- Expert interview results incorporated

**Regeneration**: Simply re-run Python scripts and recompile LaTeX to update figures with latest data.

---

## Contact

**Author**: Jeremy Wiley
**Project**: Modern Data Stack for Cybersecurity (Book + Literature Review)
**Repository**: security-data-literature-review

For questions about figure generation or customization, refer to FIGURES-AND-TABLES.md for source data.
