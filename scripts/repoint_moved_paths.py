#!/usr/bin/env python3
"""Repoint path mentions and relative links after files move, from working/MOVE-MAP.json.

Why this exists: on 2026-11-17 the dated audit, intake, proposal and interview files
left the repository root for working/. Prose across the repo names those files by
their old root paths (``RESCORE-PROPOSAL-2026-07.md``), and a relative Markdown link
breaks silently when its target moves, so a move needs one rule that rewrites every
live mention from the same map and a check that fails while any mention is stale.

What it rewrites, in every text file it scans:

* a bare path mention of an old path (``RESCORE-PROPOSAL-2026-07.md`` in prose, a
  Python string or a shell comment) becomes the new repo-root path
  (``working/proposals/RESCORE-PROPOSAL-2026-07.md``). A mention already preceded by
  a path character (``/``, ``.``, a word character or ``-``) is left alone, which keeps
  the rewrite idempotent and leaves other repos' paths (``~/project1/.../X.md``) untouched;
* a relative Markdown link (``[t](../X.md)``, ``![a](X.png)``, ``[t]: X.md``) whose
  target resolves to an old path is rewritten relative to the file that holds it;
* inside a moved file, a relative link that resolved from the file's old folder is
  rewritten so it resolves from the new one. The body of a moved file is otherwise
  never edited, because those files are dated records.

What it never touches: ``published/`` and ``archive/`` (immutable snapshots and history)
and ``CHANGELOG.md`` (its entries record what the paths were at the time) are not
scanned at all. The move map, ``working/README.md`` (both name the old paths on
purpose), the moved files' own prose and ``working/*-quality-pass/`` unit notes (dated
working records) keep their path mentions as written, but their relative links are
still checked and repaired.

Modes:
  (default)     dry run: print every pending rewrite, change nothing
  --apply       write the rewrites
  --check       exit 1 if any mention is stale, any link needs a rewrite, or any
                relative link in a scanned Markdown file points at nothing
  --links-only  with --check: only the broken-relative-link test (no map needed)
  --paths P...  limit the scan to these repo-relative files or folders
  --report F    also write the dry-run listing to F (Markdown)

Standard library only.
"""

import argparse
import json
import os
import re
import sys
from pathlib import Path, PurePosixPath

REPO_ROOT = Path(__file__).resolve().parent.parent
MAP_PATH = REPO_ROOT / "working" / "MOVE-MAP.json"

TEXT_EXT = {".md", ".py", ".sh", ".yml", ".yaml", ".json", ".cff", ".txt", ".tex", ".toml", ".cfg"}
# Never scanned at any depth (tooling and caches), and never scanned at the top level
# (immutable snapshots, history, and build output).
SKIP_ANY_DEPTH = {".git", "node_modules", "venv", ".venv", "__pycache__", "worktrees"}
SKIP_TOP_LEVEL = {"published", "archive", "paper", "dist", "build"}
# Files whose text records history or the map itself: mentions are never rewritten
# or reported as stale there. CHANGELOG.md is skipped entirely, links included.
NO_REWRITE = {"working/MOVE-MAP.json", "working/README.md", "scripts/repoint_moved_paths.py"}
SKIP_ENTIRELY = {"CHANGELOG.md"}
NO_REWRITE_DIR_RE = re.compile(r"^working/[^/]*quality-pass/")

LINK_RE = re.compile(r"(\]\()([^)\s]+)((?:\s+\"[^\"]*\")?\))")
REFDEF_RE = re.compile(r"(?m)^([ ]{0,3}\[[^\]^][^\]]*\]:[ \t]*)(\S+)()")  # not [^footnote]:
EXTERNAL_RE = re.compile(r"^(?:[a-zA-Z][a-zA-Z0-9+.-]*:|#|/|~|<)")
# Links shown as examples inside code are not links: fenced blocks and inline spans.
CODE_RE = re.compile(r"(?ms)^ {0,3}(```|~~~).*?^ {0,3}\1[^\n]*$|`[^`\n]+`")


def code_ranges(text):
    return [(m.start(), m.end()) for m in CODE_RE.finditer(text)]


def in_ranges(pos, ranges):
    return any(a <= pos < b for a, b in ranges)


def load_moves():
    data = json.loads(MAP_PATH.read_text(encoding="utf-8"))
    return {m["from"]: m["to"] for m in data["moves"]}


def rel(path: Path) -> str:
    return path.relative_to(REPO_ROOT).as_posix()


def iter_files(scopes):
    roots = [REPO_ROOT / s for s in scopes] if scopes else [REPO_ROOT]
    seen = set()
    for r in roots:
        if r.is_file():
            cands = [r]
        elif r.is_dir():
            cands = []
            for dirpath, dirnames, filenames in os.walk(r):
                d = Path(dirpath)
                dirnames[:] = [n for n in dirnames if n not in SKIP_ANY_DEPTH
                               and not (d == REPO_ROOT and n in SKIP_TOP_LEVEL)]
                cands.extend(d / f for f in filenames)
        else:
            continue
        for p in cands:
            rp = rel(p)
            if rp.split("/", 1)[0] in SKIP_TOP_LEVEL or rp in SKIP_ENTIRELY:
                continue
            if p.suffix.lower() not in TEXT_EXT or p in seen:
                continue
            seen.add(p)
            yield p


def mention_patterns(moves):
    pats = []
    for old, new in moves.items():
        pat = re.compile(r"(?<![\w./\-])" + re.escape(old) + r"(?![\w\-])")
        pats.append((old, new, pat))
    return pats


def norm(p: PurePosixPath) -> str:
    return os.path.normpath(p.as_posix()).replace(os.sep, "/")


def fix_link_target(target, file_rel, moves, inverse):
    """Return (new_target or None, broken: bool) for one relative link target."""
    if EXTERNAL_RE.match(target):
        return None, False
    path_part, sep, anchor = target.partition("#")
    if not path_part:
        return None, False
    here = PurePosixPath(file_rel).parent
    resolved = norm(here / path_part)
    new_resolved = None
    if resolved in moves:
        new_resolved = moves[resolved]
    elif file_rel in inverse and not (REPO_ROOT / resolved).exists():
        # a moved file: resolve the link from the folder it used to live in
        old_here = PurePosixPath(inverse[file_rel]).parent
        old_resolved = norm(old_here / path_part)
        old_resolved = moves.get(old_resolved, old_resolved)
        if (REPO_ROOT / old_resolved).exists():
            new_resolved = old_resolved
    if new_resolved is not None:
        new_t = os.path.relpath(new_resolved, here.as_posix() or ".").replace(os.sep, "/")
        return new_t + (sep + anchor if sep else ""), False
    return None, not (REPO_ROOT / resolved).exists()


def process(path, moves, pats, inverse, links_only):
    file_rel = rel(path)
    try:
        text = path.read_text(encoding="utf-8")
    except (UnicodeDecodeError, OSError):
        return None, [], []
    mentions_ok = (not links_only and file_rel not in NO_REWRITE
                   and file_rel not in inverse and not NO_REWRITE_DIR_RE.match(file_rel))
    changes, broken = [], []
    new_text = text

    if path.suffix.lower() == ".md":
        ranges = code_ranges(new_text)

        def sub_link(m):
            if in_ranges(m.start(), ranges):
                return m.group(0)
            target = m.group(2)
            new_t, is_broken = fix_link_target(target, file_rel, moves, inverse)
            if new_t is not None and new_t != target:
                line = text.count("\n", 0, m.start()) + 1
                changes.append((line, "link", target, new_t))
                return m.group(1) + new_t + m.group(3)
            if is_broken:
                broken.append((text.count("\n", 0, m.start()) + 1, target))
            return m.group(0)

        new_text = LINK_RE.sub(sub_link, new_text)
        ranges = code_ranges(new_text)
        new_text = REFDEF_RE.sub(sub_link, new_text)
        if links_only:
            changes, new_text = [], text  # links-only reports broken links, never rewrites

    if mentions_ok:
        for old, new, pat in pats:
            for m in pat.finditer(new_text):
                line = new_text.count("\n", 0, m.start()) + 1
                changes.append((line, "mention", old, new))
            new_text = pat.sub(new, new_text)

    return (new_text if new_text != text else None), changes, broken


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    ap.add_argument("--apply", action="store_true")
    ap.add_argument("--check", action="store_true")
    ap.add_argument("--links-only", action="store_true")
    ap.add_argument("--paths", nargs="*", default=None)
    ap.add_argument("--report")
    args = ap.parse_args()

    moves = {} if args.links_only else load_moves()
    inverse = {v: k for k, v in moves.items()}
    pats = mention_patterns(moves)

    total_changes, total_broken, report = 0, 0, []
    for path in sorted(iter_files(args.paths)):
        new_text, changes, broken = process(path, moves, pats, inverse, args.links_only)
        fr = rel(path)
        if changes or broken:
            report.append(f"\n### {fr}\n")
        for line, kind, old, new in changes:
            report.append(f"- line {line}: {kind} `{old}` -> `{new}`")
        for line, target in broken:
            report.append(f"- line {line}: BROKEN relative link `{target}`")
        total_changes += len(changes)
        total_broken += len(broken)
        if args.apply and new_text is not None:
            path.write_text(new_text, encoding="utf-8")

    verb = "applied" if args.apply else "pending"
    summary = (f"repoint_moved_paths: {total_changes} rewrite(s) {verb}, "
               f"{total_broken} broken relative link(s)"
               + (f" in scope {args.paths}" if args.paths else " repo-wide"))
    out = "\n".join(report).strip()
    if out:
        print(out)
    print(summary)
    if args.report:
        Path(args.report).write_text(
            "# repoint_moved_paths dry-run report\n\n" + summary + "\n\n" + out + "\n",
            encoding="utf-8")

    if args.check:
        pending = 0 if args.apply else total_changes
        sys.exit(1 if (pending or total_broken) else 0)


if __name__ == "__main__":
    main()
