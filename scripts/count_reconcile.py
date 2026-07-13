#!/usr/bin/env python3
"""
count_reconcile.py — one counting rule for every stated count on this repo's surfaces.

Derive-don't-state: this script derives the repo's two live count families from the
repo's own structure, then checks every surface that states one of those numbers
against the derivation, exiting non-zero on any mismatch. It exists because the same
fact hand-typed on seven-plus surfaces drifted (9 vs 7 hypotheses; 43.0% vs a stale
42.9%/76-of-177 block inside the same README) and a gate is the only durable fix.

Counter 1 — hypotheses assessed.
  Canonical source: PUBLICATION-MANUSCRIPT.md, section "### 3.7 Hypothesis Validation
  Summary" (heading to next "### "). Each scored hypothesis is a line beginning
  "*H-...-NN (Name)*:". The count is cross-validated three ways before it is trusted:
  distinct IDs == "Confidence: N/25 points" occurrences == the sum of the section's
  own band headers ("**Band (stars) - N hypothesis/es**"). A malformed 3.7 exits 2 —
  a broken canonical source must never silently under- or over-report.

Counter 2 — bibliography tiers.
  Imported, not reimplemented: automation_dashboard.parse_master_bibliography()
  (per-#### -block first Evidence Level match over MASTER-BIBLIOGRAPHY.md, tiered
  denominator excludes documented stubs).

Deliberately NOT counted: the "Total Hypotheses: 32/34/36" population metric. Its
book-manuscript leg is enumerated nowhere in this repo, so nothing here can verify
it; per the 2026-07-12 ratification that line is being retired from live surfaces
rather than gated. Surfaces that keep a pointer to it must say the count is tracked
externally, not state a number this gate would then appear to vouch for.

Usage:
  python3 scripts/count_reconcile.py            # check all surfaces, exit 1 on mismatch
  python3 scripts/count_reconcile.py --staged   # pre-commit mode: full table printed,
                                                # but only mismatches in files staged
                                                # for commit block (exit 1)

The ALLOWLIST below is the enforcement surface: adding a new file that states a
count means adding one entry here, not writing another parser. Removing or
rephrasing a surface means updating its entry — a MISSING pattern fails the run so
that a silent rephrase cannot slip a hand-typed number past the gate. Dated audit
snapshots, archive/, published/, and sections labeled historical are intentionally
not listed (never-retro-edit convention).
"""

import os
import re
import subprocess
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
os.chdir(REPO_ROOT)
sys.path.insert(0, str(REPO_ROOT / "scripts"))

from automation_dashboard import parse_master_bibliography  # noqa: E402

MANUSCRIPT = "PUBLICATION-MANUSCRIPT.md"

WORD_NUMS = {
    "one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6,
    "seven": 7, "eight": 8, "nine": 9, "ten": 10, "eleven": 11, "twelve": 12,
}


def parse_num(token):
    """Parse a stated count that may be a digit string or a number word."""
    if token is None:
        return None
    t = token.strip().lower()
    if t in WORD_NUMS:
        return WORD_NUMS[t]
    try:
        return float(t) if "." in t else int(t)
    except ValueError:
        return None


def derive_hypothesis_counter():
    """Counter 1: assessed-hypothesis count from manuscript section 3.7, triple-checked."""
    text = (REPO_ROOT / MANUSCRIPT).read_text(encoding="utf-8")
    m = re.search(
        r"(?ms)^### 3\.7 Hypothesis Validation Summary\s*$(.*?)(?=^### )", text
    )
    if not m:
        print(f"FATAL: section 3.7 not found in {MANUSCRIPT} — canonical source broken.")
        sys.exit(2)
    span = m.group(1)

    ids = sorted(set(re.findall(r"(?m)^\*(H\d?(?:-[A-Z]+)+-\d+)", span)))
    conf = re.findall(r"Confidence:\s*\d+/25 points", span)
    bands = [
        (label.strip(), int(n))
        for label, n in re.findall(
            r"(?m)^\*\*([A-Za-z ]+)\([^)]*\)\s*-\s*(\d+)\s*hypothes", span
        )
    ]
    band_sum = sum(n for _, n in bands)

    if not (len(ids) == len(conf) == band_sum):
        print(
            "FATAL: manuscript section 3.7 is internally inconsistent — "
            f"{len(ids)} distinct IDs, {len(conf)} Confidence lines, "
            f"band headers sum to {band_sum}. Fix 3.7 before trusting any count."
        )
        sys.exit(2)

    return {"total_assessed": len(ids), "ids": ids, "bands": bands}


def build_allowlist(T, bib):
    """Every live surface that states a gated count: (id, file, regex, expected).

    expected is a tuple aligned to the regex's capture groups; None skips a group.
    'sum_check' additionally requires groups 2..n to sum to group 1 (composition
    claims like "9 assessed (7 original + 2 added)" must stay internally true).
    """
    A, B, C = bib["level_a_count"], bib["level_b_count"], bib["level_c_count"]
    TIER, N, S = bib["tiered_total"], bib["total_entries"], bib["untiered_stubs"]
    PCT = bib["evidence_quality"]
    # Level-B and Level-C shares are derived the same way the dashboard derives
    # the Level-A share (automation_dashboard.py:88), so Figure 2's three-bar mix
    # is gated against the bibliography rather than hand-maintained.
    PCT_B = round(B / TIER * 100, 1) if TIER else None
    PCT_C = round(C / TIER * 100, 1) if TIER else None

    return [
        # ---- Counter 1: hypotheses assessed (canonical = manuscript 3.7) ----
        ("manuscript abstract", MANUSCRIPT,
         r"(\w+) hypotheses were assessed, (\w+) from the original extraction and (\w+) added",
         (T, None, None), True),
        ("manuscript 1.4 contributions", MANUSCRIPT,
         r"validation of (\w+) operational hypotheses",
         (T,), False),
        ("manuscript 2.4 phase-4", MANUSCRIPT,
         r"Identified (\w+) hypotheses requiring quantitative validation",
         (T,), False),
        ("manuscript 2.5 framework", MANUSCRIPT,
         r"(\w+) Hypotheses assessed \((\w+) original; (\w+) added",
         (T, None, None), True),
        ("manuscript 3.7 intro", MANUSCRIPT,
         r"(\w+) hypotheses received quantitative validation \((\w+) assessed in the original extraction; (\w+) formulated post-audit",
         (T, None, None), True),
        ("manuscript 4.3 contributions", MANUSCRIPT,
         r"(\w+) hypotheses were scored under this framework",
         (T,), False),
        ("manuscript Figure 4 caption", MANUSCRIPT,
         r"Figure 4: Hypothesis validation confidence levels for all (\w+) hypotheses",
         (T,), False),
        ("manuscript Figure 4 spec", MANUSCRIPT,
         r"Bar chart of (\w+) hypotheses with rescored confidence scores",
         (T,), False),
        ("README roster header", "README.md",
         r"\*\*Hypothesis Validation Results\*\* \((\w+) assessed",
         (T,), False),
        ("README gap-analysis line", "README.md",
         r"Gap analysis[^\n]*\((\w+) assessed",
         (T,), False),
        ("PROJECT-BRIEF Fact 2", "PROJECT-BRIEF.md",
         r"### Fact 2: (\w+) Hypotheses Assessed",
         (T,), False),
        ("PROJECT-BRIEF scope", "PROJECT-BRIEF.md",
         r"Hypothesis validation \((\w+) assessed",
         (T,), False),
        ("PROJECT-BRIEF phase-1 metrics", "PROJECT-BRIEF.md",
         r"✅ (\w+) hypotheses assessed \((\w+) original \+ (\w+) added",
         (T, None, None), True),
        ("PROJECT-BRIEF methodology", "PROJECT-BRIEF.md",
         r"(\w+) hypotheses assessed so far",
         (T,), False),
        ("METHODOLOGY quantitative-evidence", "METHODOLOGY.md",
         r"Quantitative evidence in all (\w+) hypotheses",
         (T,), False),
        ("METHODOLOGY section-10 validation", "METHODOLOGY.md",
         r"\*\*Quantitative Validation\*\*: (\w+) hypotheses validated",
         (T,), False),
        ("METHODOLOGY phase-1 success", "METHODOLOGY.md",
         r"\*\*Phase 1 Success\*\*:[^\n]*?(\w+) hypotheses validated",
         (T,), False),
        ("FIGURES-AND-TABLES total", "FIGURES-AND-TABLES.md",
         r"\*\*Total hypotheses validated\*\*: (\w+)",
         (T,), False),
        # ---- Counter 2: bibliography tiers (canonical = MASTER-BIBLIOGRAPHY.md) ----
        ("README top status block", "README.md",
         r"\*\*(\d+) sources catalogued\*\* \((\d+) tiered \+ (\d+) documented stubs; ([\d.]+)% Evidence Level A, live [0-9-]+ — (\d+)/(\d+)",
         (N, TIER, S, PCT, A, TIER), False),
        ("README contents bibliography line", "README.md",
         r"(\d+) catalogued sources \((\d+) tiered\), ([\d.]+)% Evidence Level A \(live, (\d+)/(\d+)\)",
         (N, TIER, PCT, A, TIER), False),
        ("README quality metrics A", "README.md",
         r"\*\*Evidence Level A: ([\d.]+)%\*\* \((\d+) of (\d+) tiered sources\)",
         (PCT, A, TIER), False),
        ("README quality metrics B/C", "README.md",
         r"Evidence Level B: (\d+) of (\d+) · Evidence Level C: (\d+) of (\d+) \(across (\d+) `#### ` blocks incl\. (\d+) documented stubs\)",
         (B, TIER, C, TIER, N, S), False),
        ("monthly-tracker live status", "monthly-update-tracker.md",
         r"([\d.]+)% live \((\d+)/(\d+) tiered",
         (PCT, A, TIER), False),
        ("PROJECT-BRIEF Fact 1 Level-A share", "PROJECT-BRIEF.md",
         r"Level-A share: ([\d.]+)% live-computed [0-9-]+ \((\d+)/(\d+) tiered\)",
         (PCT, A, TIER), False),
        ("PROJECT-BRIEF phase-1 Level-A", "PROJECT-BRIEF.md",
         r"✅ ([\d.]+)% Evidence Level A \(live-derived [0-9-]+: (\d+) of (\d+) tiered",
         (PCT, A, TIER), False),
        # Figure 2 states the tier mix in three places (the chart's own constants,
        # the manuscript caption, and the alt text). All three drifted to a stale
        # 76/177 @ 42.9% while the README was being reconciled to the live tally,
        # which is exactly the failure this gate exists to catch — so they are
        # gated now rather than trusted.
        ("figure2 script tally", "publication-graphics/figure2_evidence_distribution.py",
         r"TIERED_TOTAL = (\d+)\nTALLY = \{'A': (\d+), 'B': (\d+), 'C': (\d+)\}",
         (TIER, A, B, C), False),
        ("manuscript Figure 2 caption", MANUSCRIPT,
         r"Figure 2: Evidence level distribution[^\n]*?([\d.]+)% Level A \((\d+)/(\d+) tiered\), ([\d.]+)% Level B \((\d+)/(\d+)\), ([\d.]+)% Level C \((\d+)/(\d+)\)",
         (PCT, A, TIER, PCT_B, B, TIER, PCT_C, C, TIER), False),
        ("manuscript Figure 2 alt text", MANUSCRIPT,
         r"Bar chart of the evidence-level distribution across the (\d+) tiered sources[^\n]*?Level A ([\d.]+)% \((\d+) sources\), Level B ([\d.]+)% \((\d+) sources\), Level C ([\d.]+)% \((\d+) sources\)",
         (TIER, PCT, A, PCT_B, B, PCT_C, C), False),
        ("manuscript corpus note", MANUSCRIPT,
         r"The full living-review corpus \((\d+) entries, (\d+) of them carrying evidence-tier classifications",
         (N, TIER), False),
        # The 2026-07-13 incorporation found a second cohort of stale surfaces sitting
        # OUTSIDE this allowlist — including MASTER-BIBLIOGRAPHY.md's own header, which
        # had been describing a 179-block corpus for months while being the very file the
        # counts derive FROM, and a "73% Evidence Level A" claim in the venue memo that was
        # wrong by thirty points. A gate that watches only some of the surfaces teaches you
        # that the watched ones are fine; it says nothing about the rest. These are the rest.
        ("bibliography header total", "MASTER-BIBLIOGRAPHY.md",
         r"\*\*Total Sources\*\*: (\d+) catalogued `#### ` blocks \((\d+) tiered sources \+ (\d+) documented stubs",
         (N, TIER, S), False),
        ("bibliography header tiers", "MASTER-BIBLIOGRAPHY.md",
         r"\*\*Evidence Quality\*\*: ([\d.]+)% Evidence Level A \(live-derived [0-9-]+: (\d+) of (\d+) tiered entries; (\d+) B,\s*\n?\s*(\d+) C, across (\d+) `#### ` blocks incl\. (\d+) documented stubs",
         (PCT, A, TIER, B, C, N, S), False),
        ("manuscript Table 1 total sources", MANUSCRIPT,
         r"\| Total Sources \| 100\+ \| (\d+) catalogued \((\d+) tiered; live-derived [0-9-]+\) \|",
         (N, TIER), False),
        ("manuscript Table 1 Level-A", MANUSCRIPT,
         r"\| Evidence Level A \| >70% \| ([\d.]+)% \((\d+)/(\d+) tiered; live-derived [0-9-]+\) \|",
         (PCT, A, TIER), False),
        ("manuscript tier-mix prose", MANUSCRIPT,
         r"The live, derived tally as of [0-9-]+ is (\d+) of (\d+) tiered entries at Level A \(([\d.]+) percent\), (\d+) at Level B \(([\d.]+) percent\), and (\d+) at Level C \(([\d.]+) percent\)",
         (A, TIER, PCT, B, PCT_B, C, PCT_C), False),
        ("manuscript 2.3 tier shares", MANUSCRIPT,
         r"\*\*Evidence Level A\*\* \(target >70%; live ([\d.]+)%, (\d+) of (\d+) tiered\)",
         (PCT, A, TIER), False),
        ("manuscript 3.1 source statistics", MANUSCRIPT,
         r"\*\*Evidence levels\*\*: Level A ([\d.]+)% \((\d+)/(\d+)\), Level B ([\d.]+)% \((\d+)/(\d+)\), Level C ([\d.]+)% \((\d+)/(\d+)\)",
         (PCT, A, TIER, PCT_B, B, TIER, PCT_C, C, TIER), False),
        ("METHODOLOGY Level-A achievement", "METHODOLOGY.md",
         r"\*\*Current Achievement\*\*: (\d+) of (\d+) tiered entries \(([\d.]+)%\), live-derived",
         (A, TIER, PCT), False),
        ("METHODOLOGY target table", "METHODOLOGY.md",
         r"\| Evidence Level A \| >70% \| ([\d.]+)% \((\d+)/(\d+) tiered; live-derived [0-9-]+\) \|",
         (PCT, A, TIER), False),
        ("publication-graphics README fig2", "publication-graphics/README.md",
         r"live per-source tier tally \(([\d.]+)% Level A, (\d+)/(\d+) tiered, derived",
         (PCT, A, TIER), False),
        ("PUBLICATION-VENUE-RECOMMENDATIONS header", "PUBLICATION-VENUE-RECOMMENDATIONS.md",
         r"MASTER-BIBLIOGRAPHY\.md \((\d+) catalogued sources, (\d+) tiered; ([\d.]+)% Evidence Level A live-derived",
         (N, TIER, PCT), False),
    ]


def check_source_taxonomy(bib):
    """Special surface: the derived source taxonomy must account for every catalogued block.

    Figure 3 charts this file. It used to chart five hardcoded buckets summing to 74 — a corpus
    that stopped existing in October 2025 — and nothing noticed for nine months because nothing
    derived it. Now a source added without a classification fails here rather than silently
    dropping out of a published figure.
    """
    path = REPO_ROOT / "methods" / "source-taxonomy.json"
    if not path.exists():
        return None, bib["total_entries"]
    import json

    tax = json.loads(path.read_text(encoding="utf-8"))
    return tax.get("total_entries"), bib["total_entries"]


def check_readme_roster_ids(T):
    """Special surface: the README roster must list exactly T distinct hypothesis IDs."""
    lines = (REPO_ROOT / "README.md").read_text(encoding="utf-8").splitlines()
    ids, in_block = set(), False
    for line in lines:
        if re.search(r"\*\*Hypothesis Validation Results\*\*", line):
            in_block = True
            continue
        if in_block:
            m = re.match(r"^- (H\d?(?:-[A-Z]+)+-\d+)", line)
            if m:
                ids.add(m.group(1))
            elif line.strip() and not line.startswith("- "):
                break
    return len(ids), T


def check_figure4_dict(T):
    """Special surface: the Figure 4 script's hardcoded roster dict must have T entries."""
    path = REPO_ROOT / "publication-graphics" / "figure4_hypothesis_confidence.py"
    if not path.exists():
        return None, T
    keys = re.findall(r"(?m)^\s+'H[^']*':\s*\{", path.read_text(encoding="utf-8"))
    return len(keys), T


def numbers_match(stated, expected):
    if expected is None:
        return True
    if stated is None:
        return False
    if isinstance(expected, float) or isinstance(stated, float):
        return round(float(stated), 1) == round(float(expected), 1)
    return int(stated) == int(expected)


def main():
    staged_mode = "--staged" in sys.argv

    hyp = derive_hypothesis_counter()
    T = hyp["total_assessed"]
    bib = parse_master_bibliography()
    if bib is None:
        print("FATAL: MASTER-BIBLIOGRAPHY.md not found — canonical source broken.")
        sys.exit(2)

    staged_files = set()
    if staged_mode:
        try:
            out = subprocess.run(
                ["git", "diff", "--cached", "--name-only"],
                capture_output=True, text=True, cwd=REPO_ROOT, check=True,
            ).stdout
            staged_files = set(out.split())
        except Exception:
            staged_mode = False  # no git available: fall back to full enforcement

    bands = ", ".join(f"{label.strip()}={n}" for label, n in hyp["bands"])
    print(f"Counter 1 (hypotheses assessed, manuscript 3.7): {T}  [{bands}]")
    print(
        "Counter 2 (bibliography tiers): "
        f"{bib['total_entries']} blocks / {bib['tiered_total']} tiered "
        f"/ {bib['untiered_stubs']} stubs; "
        f"A={bib['level_a_count']} B={bib['level_b_count']} C={bib['level_c_count']}; "
        f"Level-A {bib['evidence_quality']}%"
    )
    print()

    rows, failures, blocking = [], 0, 0
    file_cache = {}

    def file_text(fname):
        if fname not in file_cache:
            p = REPO_ROOT / fname
            file_cache[fname] = p.read_text(encoding="utf-8") if p.exists() else None
        return file_cache[fname]

    for surf_id, fname, pattern, expected, sum_check in build_allowlist(T, bib):
        text = file_text(fname)
        if text is None:
            status, stated_str = "MISS", "file not found"
        else:
            m = re.search(pattern, text)
            if not m:
                status, stated_str = "MISS", "pattern not found (rephrased? update ALLOWLIST)"
            else:
                stated = [parse_num(g) for g in m.groups()]
                ok = all(numbers_match(s, e) for s, e in zip(stated, expected))
                if sum_check and ok:
                    parts = [s for s in stated[1:] if s is not None]
                    ok = bool(parts) and sum(parts) == stated[0]
                status = "OK" if ok else "FAIL"
                stated_str = "/".join(str(g) for g in m.groups())
        exp_str = "/".join("-" if e is None else str(e) for e in expected)
        rows.append((status, surf_id, fname, stated_str, exp_str))
        if status != "OK":
            failures += 1
            if not staged_mode or fname in staged_files:
                blocking += 1

    # Special (non-regex) surfaces
    n_roster, _ = check_readme_roster_ids(T)
    status = "OK" if n_roster == T else "FAIL"
    rows.append((status, "README roster ID count", "README.md", str(n_roster), str(T)))
    if status != "OK":
        failures += 1
        if not staged_mode or "README.md" in staged_files:
            blocking += 1

    n_fig4, _ = check_figure4_dict(T)
    fig4_file = "publication-graphics/figure4_hypothesis_confidence.py"
    if n_fig4 is None:
        status, stated_str = "MISS", "file not found"
    else:
        status, stated_str = ("OK" if n_fig4 == T else "FAIL"), str(n_fig4)
    rows.append((status, "Figure 4 script dict entries", fig4_file, stated_str, str(T)))
    if status != "OK":
        failures += 1
        if not staged_mode or fig4_file in staged_files:
            blocking += 1

    n_tax, n_blocks = check_source_taxonomy(bib)
    tax_file = "methods/source-taxonomy.json"
    if n_tax is None:
        status, stated_str = "MISS", "file not found (run scripts/derive_source_taxonomy.py)"
    else:
        status, stated_str = ("OK" if n_tax == n_blocks else "FAIL"), str(n_tax)
    rows.append((status, "Figure 3 source taxonomy total", tax_file, stated_str, str(n_blocks)))
    if status != "OK":
        failures += 1
        if not staged_mode or tax_file in staged_files:
            blocking += 1

    w_id = max(len(r[1]) for r in rows)
    w_f = max(len(r[2]) for r in rows)
    print(f"{'STATUS':6}  {'SURFACE':{w_id}}  {'FILE':{w_f}}  STATED -> EXPECTED")
    for status, surf_id, fname, stated_str, exp_str in rows:
        print(f"{status:6}  {surf_id:{w_id}}  {fname:{w_f}}  {stated_str} -> {exp_str}")
    print()

    if failures == 0:
        print(f"count-reconcile: all {len(rows)} surfaces agree with the derived counts.")
        return 0
    if staged_mode and blocking == 0:
        print(
            f"count-reconcile: {failures} stale surface(s) exist but none are in this "
            "commit's staged files — not blocking. Run without --staged for the full gate."
        )
        return 0
    verb = "block this commit" if staged_mode else "mismatch the derived counts"
    print(
        f"count-reconcile: {blocking if staged_mode else failures} surface(s) {verb}. "
        "Regenerate the stated number from the counter above (or update the ALLOWLIST "
        "if a surface was deliberately rephrased or retired)."
    )
    return 1


if __name__ == "__main__":
    sys.exit(main())
