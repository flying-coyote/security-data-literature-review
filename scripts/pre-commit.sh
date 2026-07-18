#!/usr/bin/env bash
# Repo pre-commit gate — the checked-in entry point the local git hook should exec.
#
# Install once per clone (the .git/hooks file itself is not version-controlled):
#   printf '#!/usr/bin/env bash\nexec bash "$(git rev-parse --show-toplevel)/scripts/pre-commit.sh"\n' \
#     > .git/hooks/pre-commit && chmod +x .git/hooks/pre-commit
#
# Order: secret-scan first (cheaper, security-relevant), count-reconcile second.
# A non-zero exit from either blocks the commit. count_reconcile.py runs in
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
exit 0
