#!/usr/bin/env bash
# Build a Security Data Works–branded PDF of the systematic literature review.
# Assembles the manuscript core + tables + references + appendices from the
# canonical markdown, normalizing heading levels and dropping draft stubs.
set -euo pipefail
ROOT="/home/USER/security-data-literature-review"
cd "$ROOT"
mkdir -p build
SRC_M="PUBLICATION-MANUSCRIPT.md"
SRC_A="APPENDICES.md"
SRC_R="REFERENCES.md"
OUT="build/litreview.md"

# Decrement every markdown heading by one level (## -> #, ### -> ##), guarding H1.
decr() { awk '{ if ($0 ~ /^##+ /) sub(/^#/,""); print }'; }
pagebreak() { printf '\n```{=latex}\n\\newpage\n```\n\n'; }

{
  # Manuscript: ABSTRACT through CONCLUSION (drop title/metadata header + the
  # ACKNOWLEDGMENTS/REFERENCES/FIGURES/APPENDICES/METADATA stub sections that
  # carry [TO BE …] placeholders — the real content lives in the other files).
  sed -n '/^## ABSTRACT/,/^## ACKNOWLEDGMENTS/p' "$SRC_M" | sed '/^## ACKNOWLEDGMENTS/d' | decr
  pagebreak
  # Figures (real images now embedded in the manuscript FIGURES section).
  awk '/^## FIGURES/{f=1} /^## TABLES/{f=0} f' "$SRC_M" | decr
  pagebreak
  # Tables (real GFM tables embedded in the manuscript).
  awk '/^## TABLES/{f=1} /^## APPENDICES/{f=0} f' "$SRC_M" | decr
  pagebreak
  # References (78 IEEE citations), drop the file's own H1 title.
  sed -n '/^## REFERENCES/,$p' "$SRC_R" | decr
  pagebreak
  # Appendices A–D, drop the file's H1 title + its local table of contents.
  sed -n '/^# APPENDIX A/,$p' "$SRC_A"
} > "$OUT"

pandoc tools/build/metadata.yaml "$OUT" \
  -f markdown-tex_math_dollars-tex_math_single_backslash+lists_without_preceding_blankline \
  --toc --toc-depth=2 \
  --pdf-engine=xelatex \
  -H tools/build/header.tex \
  -o build/litreview.pdf

echo "Built build/litreview.pdf"
