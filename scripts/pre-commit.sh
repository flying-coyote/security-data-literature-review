#!/usr/bin/env bash
# Repo pre-commit gate — the checked-in entry point the local git hook should exec.
#
# Install once per clone (the .git/hooks file itself is not version-controlled):
#   printf '#!/usr/bin/env bash\nexec bash "$(git rev-parse --show-toplevel)/scripts/pre-commit.sh"\n' \
#     > .git/hooks/pre-commit && chmod +x .git/hooks/pre-commit
#
# Order: secret-scan first (cheaper, security-relevant), count-reconcile second,
# then the moved-path and relative-link check on staged files, then the
# personal-communication attribution check. A non-zero exit
# from any of them blocks the commit. count_reconcile.py runs in
# --staged mode so only a staged file whose stated count disagrees with the live
# derivation blocks; stale counts in untouched files are reported, not blocking.
set -u
root="$(git rev-parse --show-toplevel)"
bash "$root/scripts/secret-scan.sh" || exit 1
python3 "$root/scripts/count_reconcile.py" --staged || exit 1
# Vendor rollup gate: only when the vendor database itself is staged (cheap otherwise-skip)
if git diff --cached --name-only | grep -q '^vendor-landscape/vendor-database.json$'; then
  python3 "$root/scripts/derive_vendor_rollups.py" --check || exit 1
fi
# Moved-path mentions and relative links: only the staged text files are checked,
# so an untouched file elsewhere cannot block an unrelated commit (CI runs the
# repo-wide check).
# Portable fill (no mapfile), so the hook also runs under macOS's stock bash 3.2.
staged=()
while IFS= read -r f; do staged+=("$f"); done < <(git diff --cached --name-only --diff-filter=ACMR \
  | grep -E '\.(md|py|sh|ya?ml|json|cff|txt|tex)$' || true)
if [ "${#staged[@]}" -gt 0 ]; then
  python3 "$root/scripts/repoint_moved_paths.py" --check --paths "${staged[@]}" >/dev/null \
    || { python3 "$root/scripts/repoint_moved_paths.py" --paths "${staged[@]}"; exit 1; }
fi
# Personal-communication gate (added 2026-11-17). A personal communication is not
# an eligible source (MASTER-BIBLIOGRAPHY.md Boundary rule), and fabricated ones
# naming people who were never spoken to survived in the appendices after the
# 2026-08-12 bibliography fix. Any ADDED line in the bibliography or a book
# appendix that carries "personal communication", "personal account" or
# "pers. comm" blocks the commit unless it also matches an allowlisted phrase:
# the anonymized form of the one practitioner conversation actually held, and the
# bibliography's own policy and correction wording. Only added lines are checked,
# so an untouched legacy line cannot block an unrelated edit.
pc_files=()
while IFS= read -r f; do pc_files+=("$f"); done < <(git diff --cached --name-only --diff-filter=ACMR \
  | grep -E '^(MASTER-BIBLIOGRAPHY\.md|book-appendices/.+\.md)$' || true)
if [ "${#pc_files[@]}" -gt 0 ]; then
  # Allowlist: the anonymized practitioner forms, then the bibliography's own Boundary
  # rule and correction wording (MASTER-BIBLIOGRAPHY.md lines 22, 1108, 1110, 2877, 2880
  # as of 2026-11-17), kept specific so a generic phrase cannot wave a name through.
  pc_allow='data-platform practitioner|anonymized practitioner|a personal communication is not eligible as a source|with URL "Personal communication \(expert validation\)"|so the personal-communication citation was|anonymized per the Boundary rule|Do not cite \(2026-11-17\)|^\+\*Corrected [0-9]{4}-[0-9]{2}-[0-9]{2}'
  pc_hits="$(git diff --cached --no-color --no-ext-diff -U0 -- "${pc_files[@]}" | grep -v '^+++' | grep '^+' \
    | grep -Ei 'personal[ -](communication|correspondence|account)|pers\. ?comm|practitioner validation|interview with' \
    | grep -Eiv "$pc_allow" || true)"
  if [ -n "$pc_hits" ]; then
    echo "pre-commit: personal-communication attribution added outside the allowlist:" >&2
    printf '%s\n' "$pc_hits" >&2
    echo "Cite a published source, or remove the attribution and mark the claim unverified." >&2
    echo "(Allowlist lives in scripts/pre-commit.sh; extend it only for a conversation that actually took place.)" >&2
    exit 1
  fi
fi
exit 0
