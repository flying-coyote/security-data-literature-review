#!/usr/bin/env bash
# Assemble the curated paper/ export that IS the Zenodo deposit — the ratified
# Phase-2B "paper/ is an export of the living review" ruling
# (.claude/review-protocol.md, lit-review section; deposit-scope ruling
# 2026-07-16). A Zenodo release ZIP is DOI-frozen and permanent, so the
# deposit is assembled by WHITELIST: nothing enters the archive unless named
# below, which means a newly added repo file stays OUT of the deposit until
# someone adds it here deliberately.
#
# EXCLUDED — the classes whose presence killed the full-repo-freeze route:
#   EXPERT-INTERVIEW-GUIDE-*.md   profile named third parties with outreach
#                                 strategy; must never be DOI-frozen
#   GEMINI-*-INTAKE-*.md          internal research intake; DR2 line 10 carries
#                                 a private Google Doc ID
#   *-cowork.md                   internal cowork/audit session documents
#                                 (MIESSLER-REPO-AUDIT, VERIFICATION-SWEEP 1-3)
#   .claude/                      agent config incl. tracked settings.local.json
#                                 (fleet enumeration + auto-approve patterns)
#   archive/                      superseded working snapshots
#   published/                    superseded 2025-10-22 draft + the repudiated
#                                 verification certificate (kept in-repo as a
#                                 record, wrong thing to freeze as the paper)
#   vendor-landscape/             quarterly vendor DB, separate product from
#                                 the paper record (KNOWN-STALE 2025-Q4)
#
# EXCLUDED — superseded companions (2026-07-16 review §5/§7: they contradict
# the manuscript's embedded sections; two numbering systems in one deposit is
# a desk-reject risk):
#   REFERENCES.md  APPENDICES.md  FIGURES-AND-TABLES.md
#
# EXCLUDED — internal working/ops surfaces, not the paper record:
#   README.md, PROJECT-BRIEF.md, PUBLICATION-VENUE-RECOMMENDATIONS.md (venue
#   strategy incl. APC-waiver tactics), RESEARCH-JOURNAL.md,
#   monthly-update-tracker.md, MONTHLY-2026-07-RESEARCH-PACKET.md,
#   LITERATURE-EXTRACTION-PLAN.md, NEW-HYPOTHESES-PROPOSAL-2026-07.md,
#   RESCORE-PROPOSAL-2026-07.md, isolation-first-security-tracking.md,
#   AUDIT-REPORT-BEST-PRACTICES.md, D-AUDIT-ADJUDICATION-2026-07-09.md,
#   SELF-AUDIT-2026-06.md, REVIEW-AND-PLAN-2026-06.md,
#   REVIEW-AND-RECOMMENDATIONS-2026-07-16.md, docs/, .github/, .gitignore,
#   scripts/ repo automation (weekly_* health checks, pre-commit.sh,
#   secret-scan.sh, SCHEDULING.md — ops, not instruments)
#
# EXCLUDED conservatively (not sensitive, but not in the ruled include set —
# owner may pull these into a later version):
#   LITERATURE-HYPOTHESIS-GAP-ANALYSIS.md, analysis-bundles/,
#   book-appendices/ (MOAR book material, belongs to the book's own release)
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)"
EXPORT="$ROOT/paper"
DIST="$ROOT/dist"
MANIFEST="paper-export-manifest.txt"

rm -rf "$EXPORT"
mkdir -p "$EXPORT"

# The deposit carries a freshly built manuscript PDF, never a stale build/.
bash "$ROOT/tools/build/build.sh"

copy() { # repo-relative path in, same layout inside the export
  local rel="$1"
  mkdir -p "$EXPORT/$(dirname "$rel")"
  cp "$ROOT/$rel" "$EXPORT/$rel"
}

# The paper, its bibliography/method record, licensing, and deposit metadata.
# CHANGELOG.md ships because citation stability depends on the revision record;
# .zenodo.json/CITATION.cff ship so the deposit documents its intended metadata
# even though a MANUAL Zenodo upload never parses them (only the GitHub
# webhook route reads .zenodo.json).
for f in \
  PUBLICATION-MANUSCRIPT.md \
  MASTER-BIBLIOGRAPHY.md \
  METHODOLOGY.md \
  CHANGELOG.md \
  LICENSE \
  LICENSE-CODE \
  .zenodo.json \
  CITATION.cff \
; do copy "$f"; done

cp "$ROOT/build/litreview.pdf" "$EXPORT/litreview.pdf"

# methods/ ships whole: search protocol, retro-run, appraisal, retrieval,
# second-screen, link-check, scoring rubric, prisma-results/ — the
# reproducibility record PRISMA-S expects.
mkdir -p "$EXPORT/methods"
cp -R "$ROOT/methods/." "$EXPORT/methods/"

# scripts/ ships instruments only (the derive-don't-state toolchain the
# manuscript's counts depend on); enumerated so repo automation can't leak in.
for f in \
  scripts/automation_dashboard.py \
  scripts/count_reconcile.py \
  scripts/derive_source_taxonomy.py \
  scripts/emit_search_arm_entries.py \
  scripts/link_check.py \
  scripts/prisma_search.py \
  scripts/validate_metadata.py \
; do copy "$f"; done

# tools/build/ ships whole so the PDF is reproducible from the deposit alone:
# code under LICENSE-CODE (MIT), redistributed DM Sans / JetBrains Mono fonts
# under their SIL OFL-1.1 texts (OFL-*.txt travel WITH the fonts — an OFL
# redistribution constraint, not a courtesy).
mkdir -p "$EXPORT/tools/build"
cp -R "$ROOT/tools/build/." "$EXPORT/tools/build/"

# publication-graphics/ ships figure sources + rendered figures only; venv/
# (~188MB) and TeX aux never ship, so files are enumerated by type rather
# than copied as a tree.
mkdir -p "$EXPORT/publication-graphics"
for f in \
  "$ROOT"/publication-graphics/README.md \
  "$ROOT"/publication-graphics/generate_all_figures.sh \
  "$ROOT"/publication-graphics/requirements.txt \
  "$ROOT"/publication-graphics/requirements-lock.txt \
  "$ROOT"/publication-graphics/*.py \
  "$ROOT"/publication-graphics/*.tex \
  "$ROOT"/publication-graphics/*.pdf \
  "$ROOT"/publication-graphics/*.png \
; do cp "$f" "$EXPORT/publication-graphics/"; done

# Manifest: the owner's review gate before any upload. Every included file is
# listed; the header pins the source commit so the deposit is traceable to a
# repo state.
COMMIT="$(git -C "$ROOT" rev-parse --short=12 HEAD 2>/dev/null || echo unknown)"
DIRTY=""
if [ -n "$(git -C "$ROOT" status --porcelain 2>/dev/null)" ]; then
  DIRTY=" + uncommitted changes"
fi
COUNT="$(find "$EXPORT" -type f ! -name "$MANIFEST" | wc -l)"
BYTES="$(find "$EXPORT" -type f ! -name "$MANIFEST" -printf '%s\n' | awk '{s+=$1} END{print s}')"
SIZE_H="$(numfmt --to=iec --suffix=B "$BYTES")"

{
  echo "# paper/ export manifest — owner reviews this file BEFORE any Zenodo upload"
  echo "# built: $(date -u +%Y-%m-%dT%H:%M:%SZ)"
  echo "# source commit: ${COMMIT}${DIRTY}"
  echo "# files: ${COUNT}  total: ${BYTES} bytes (${SIZE_H})"
  echo "#"
  (cd "$EXPORT" && find . -type f ! -name "$MANIFEST" -printf '%10s  %P\n' | sort -k2)
} > "$EXPORT/$MANIFEST"

# DOI-frozen archives are permanent: an excluded-class name in the manifest is
# a build FAILURE, not a warning.
BLOCK='EXPERT-INTERVIEW|GEMINI|(^|/| )archive/|\.claude|-cowork|vendor-landscape|settings\.local|(^|/| )published/|book-appendices|GAP-ANALYSIS'
if grep -E -i "$BLOCK" "$EXPORT/$MANIFEST" | grep -v '^#'; then
  echo "FATAL: excluded-class file present in export (see lines above)" >&2
  exit 1
fi

mkdir -p "$DIST"
TARBALL="$DIST/paper-export-$(date +%Y%m%d).tar.gz"
tar -czf "$TARBALL" -C "$ROOT" paper

echo ""
echo "paper/ export built at $EXPORT"
echo "  files: ${COUNT}   total: ${SIZE_H}   source: ${COMMIT}${DIRTY}"
echo "  manifest: $EXPORT/$MANIFEST (owner review gate before upload)"
echo "  tarball:  $TARBALL ($(numfmt --to=iec --suffix=B "$(stat -c %s "$TARBALL")"))"
