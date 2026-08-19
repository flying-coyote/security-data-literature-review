#!/usr/bin/env python3
"""Rewrite the gated surfaces that count_reconcile.py reports as MISMATCH.

WHY THIS EXISTS. count_reconcile.py enumerates every live surface that states a gated
count and checks it against the value derived from the corpus. It reports; it does not
fix. When a re-tiering pass moves the Level-A share, nineteen surfaces go stale at once
and hand-editing them is how a number drifts back out of sync.

HOW IT STAYS HONEST. It imports build_allowlist() from count_reconcile rather than
restating the patterns, so the fixer and the validator share one definition and cannot
disagree. Run count_reconcile.py afterwards; it is the acceptance test, and this script
deliberately has no opinion of its own about what the numbers should be.

SAFETY. Dry-run by default: --apply is required to write. It only touches surfaces that
currently MISMATCH, and only when every group it would change is numeric, because some
surfaces spell their counts as words ("Nine hypotheses") and rewriting those correctly
needs a judgement this script should not be making unsupervised. Anything it declines is
printed so it can be fixed by hand.

Usage:
  python3 scripts/count_reconcile_fix.py            # dry run, show what would change
  python3 scripts/count_reconcile_fix.py --apply    # write the changes
"""
import re
import sys
import pathlib

sys.path.insert(0, str(pathlib.Path(__file__).parent))
import count_reconcile as cr  # noqa: E402

ROOT = pathlib.Path(__file__).parent.parent


def rebuild(match, expected):
    """Return the matched text with each capture group replaced by its expected value.

    Walks the group spans in order and splices, so literal text between groups (units,
    punctuation, prose) survives untouched. Returns None if the rewrite is not safe.
    """
    text = match.group(0)
    base = match.start()
    pieces = []
    cursor = 0
    for i, want in enumerate(expected, start=1):
        if want is None:
            continue
        gs, ge = match.start(i) - base, match.end(i) - base
        if gs < 0:
            return None  # optional group that did not participate
        have = text[gs:ge]
        if have == str(want):
            continue
        if not re.fullmatch(r"[\d.]+", have):
            return None  # word-form or non-numeric: leave it for a human
        pieces.append((gs, ge, str(want)))
    if not pieces:
        return text
    pieces.sort()
    out = []
    for gs, ge, val in pieces:
        out.append(text[cursor:gs])
        out.append(val)
        cursor = ge
    out.append(text[cursor:])
    return "".join(out)


def main():
    apply = "--apply" in sys.argv
    T = cr.derive_hypothesis_counter()["total_assessed"]
    bib = cr.parse_master_bibliography()

    print(f"derived: A={bib['level_a_count']} B={bib['level_b_count']} C={bib['level_c_count']} "
          f"tiered={bib['tiered_total']} Level-A {bib['evidence_quality']}%\n")

    changed, skipped, missing = 0, [], []
    edits = {}
    for name, fname, pat, expected, _sum in cr.build_allowlist(T, bib):
        path = ROOT / fname
        if not path.exists():
            missing.append((name, fname))
            continue
        text = edits.get(fname, path.read_text())
        m = re.search(pat, text)
        if not m:
            missing.append((name, fname))
            continue
        new = rebuild(m, expected)
        if new is None:
            skipped.append((name, fname, m.group(0)[:70]))
            continue
        if new == m.group(0):
            continue
        print(f"  {name}  ({fname})")
        print(f"    - {m.group(0)[:120]}")
        print(f"    + {new[:120]}")
        edits[fname] = text[:m.start()] + new + text[m.end():]
        changed += 1

    if skipped:
        print("\nDECLINED (non-numeric group, fix by hand):")
        for name, fname, snip in skipped:
            print(f"  {name} ({fname}): {snip}")
    if missing:
        print("\nPATTERN NOT FOUND (surface moved or reworded):")
        for name, fname in missing:
            print(f"  {name} ({fname})")

    if not changed:
        print("\nnothing to change.")
        return
    if apply:
        for fname, text in edits.items():
            (ROOT / fname).write_text(text)
        print(f"\napplied {changed} surface update(s) across {len(edits)} file(s).")
        print("now run: python3 scripts/count_reconcile.py")
    else:
        print(f"\n{changed} surface update(s) would be applied. Re-run with --apply to write.")


if __name__ == "__main__":
    main()
