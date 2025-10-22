#!/bin/bash
# Generate All Publication-Quality Figures
# Usage: ./generate_all_figures.sh

set -e  # Exit on error

echo "========================================="
echo "Publication Graphics Generation"
echo "========================================="
echo ""

# Check Python installation
if ! command -v python3 &> /dev/null; then
    echo "❌ Error: python3 not found. Please install Python 3.8+"
    exit 1
fi

echo "✓ Python3 found: $(python3 --version)"
echo ""

# Check if virtual environment should be used
if [ ! -d "venv" ]; then
    echo "ℹ️  No virtual environment found. Creating one..."
    python3 -m venv venv
    echo "✓ Virtual environment created"
fi

# Activate virtual environment
echo "Activating virtual environment..."
source venv/bin/activate

# Install/upgrade dependencies
echo ""
echo "Installing Python dependencies..."
pip install --quiet --upgrade pip
pip install --quiet -r requirements.txt
echo "✓ Dependencies installed"
echo ""

# Generate Python figures
echo "========================================="
echo "Generating Python Figures"
echo "========================================="
echo ""

echo "Figure 2: Evidence Level Distribution..."
python3 figure2_evidence_distribution.py
echo ""

echo "Figure 3: Source Type Taxonomy..."
python3 figure3_source_taxonomy.py
echo ""

echo "Figure 4: Hypothesis Validation Confidence..."
python3 figure4_hypothesis_confidence.py
echo ""

# Generate LaTeX figure (if pdflatex available)
echo "========================================="
echo "Generating LaTeX Figures"
echo "========================================="
echo ""

if command -v pdflatex &> /dev/null; then
    echo "Figure 1: PRISMA Flowchart (LaTeX TikZ)..."
    pdflatex -interaction=nonstopmode figure1_prisma_flowchart.tex > /dev/null 2>&1
    # Clean up auxiliary files
    rm -f *.aux *.log
    echo "✅ Figure 1 created successfully!"
    echo "   - PDF: figure1_prisma_flowchart.pdf (vector)"
    echo ""
else
    echo "⚠️  pdflatex not found. Skipping Figure 1 (PRISMA flowchart)."
    echo "   Install LaTeX to generate Figure 1:"
    echo "   - Ubuntu/Debian: sudo apt-get install texlive-full"
    echo "   - macOS: Install MacTeX from https://www.tug.org/mactex/"
    echo "   - Windows: Install MiKTeX from https://miktex.org/download"
    echo ""
fi

# Summary
echo "========================================="
echo "Generation Complete!"
echo "========================================="
echo ""
echo "Generated files:"
ls -lh figure*.png figure*.pdf 2>/dev/null | awk '{print "  - " $9 " (" $5 ")"}'
echo ""
echo "✓ All figures generated successfully!"
echo "✓ Output directory: $(pwd)"
echo ""
echo "Next steps:"
echo "  1. Review generated figures"
echo "  2. Insert into PUBLICATION-MANUSCRIPT.md"
echo "  3. Submit to journal (ACM Computing Surveys target)"
echo ""

# Deactivate virtual environment
deactivate
