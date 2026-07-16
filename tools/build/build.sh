#!/usr/bin/env bash
# Build a Security Data Works–branded PDF of the systematic literature review.
# Assembles the PDF entirely from PUBLICATION-MANUSCRIPT.md's own embedded
# sections (ABSTRACT … APPENDICES), normalizing heading levels and dropping
# only the internal MANUSCRIPT METADATA block. The former companion stitches
# (REFERENCES.md, APPENDICES.md) are retired: those files are superseded by
# the manuscript's embedded REFERENCES [1]–[38] and Appendices A–D.
set -euo pipefail

# Repo root derived from this script's location, so the build works from any
# checkout path (no hardcoded $HOME).
ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)"
cd "$ROOT"
mkdir -p build
SRC_M="PUBLICATION-MANUSCRIPT.md"
OUT="build/litreview.md"

# header.tex is a template: fontspec needs an absolute Path= to the brand TTFs
# (pandoc runs the TeX engine from a temp dir, so relative paths don't resolve).
# Substitute the checkout's real font dir into a generated copy.
HDR="build/header.gen.tex"
sed "s|@@FONTDIR@@|$ROOT/tools/build/fonts|g" tools/build/header.tex > "$HDR"

# Decrement every markdown heading by one level (## -> #, ### -> ##), guarding H1.
decr() { awk '{ if ($0 ~ /^##+ /) sub(/^#/,""); print }'; }
pagebreak() { printf '\n```{=latex}\n\\newpage\n```\n\n'; }

{
  # Body + back-matter statements: ABSTRACT through CODE AVAILABILITY
  # (drop only the title/metadata header above ABSTRACT).
  sed -n '/^## ABSTRACT/,/^## REFERENCES/p' "$SRC_M" | sed '/^## REFERENCES/d' | decr
  pagebreak
  # The manuscript's own embedded REFERENCES ([1]–[38]).
  awk '/^## REFERENCES/{f=1} /^## FIGURES/{f=0} f' "$SRC_M" | decr
  pagebreak
  # Figures (real images embedded in the manuscript FIGURES section).
  awk '/^## FIGURES/{f=1} /^## TABLES/{f=0} f' "$SRC_M" | decr
  pagebreak
  # Tables (real GFM tables embedded in the manuscript).
  awk '/^## TABLES/{f=1} /^## APPENDICES/{f=0} f' "$SRC_M" | decr
  pagebreak
  # The manuscript's own embedded Appendices A–D; stop before the internal
  # MANUSCRIPT METADATA block, which is repo bookkeeping, not publication content.
  awk '/^## APPENDICES/{f=1} /^## MANUSCRIPT METADATA/{f=0} f' "$SRC_M" | decr
} > "$OUT"

pandoc tools/build/metadata.yaml "$OUT" \
  -f markdown-tex_math_dollars-tex_math_single_backslash+lists_without_preceding_blankline \
  --toc --toc-depth=2 \
  --pdf-engine=xelatex \
  -H "$HDR" \
  -o build/litreview.pdf

echo "Built build/litreview.pdf"
