#!/usr/bin/env python3
"""Derive per-vendor evidence_summary rollups for vendor-landscape/vendor-database.json.

Derive-don't-state, applied to the vendor database: every evidence_summary block is a
DERIVED artifact of the vendor's actual source objects, never hand-stated. The 2026-07-18
regen exists because the Oct-2025 hand-stated rollups drifted (10 vendors claimed a
Tier-A analyst source whose object the I-1 pass had removed; the 7 capability-scored
vendors undercounted their unions), so this script is the permanent gate.

Counting rules (the mirror rule matters):
- A vendor's logical sources = capability-level evidence.sources + cost_modeling
  evidence.sources + vendor-level evidence_sources, deduplicated.
- MIRROR RULE: the Oct-2025 MCP integration denormalized capability sources into
  vendor-level entries with id "<vendor>-<capability_context>-<original-id>". Such an
  entry is the SAME logical source as the capability-level original and counts once.
  (The mirrors are kept in the file as dated records; only the counting collapses them.)
- Sources whose evidence_status starts with "dropped" are not counted.
- overall_evidence_quality = majority tier among logical sources; ties break to the
  lower-quality tier (conservative). Zero sources => "unevidenced".
- analyst_reports = count of logical sources with type "analyst_report" (key written
  only when >0 or already present).

Schema compliance (--check also enforces the schema's Evidence Tier Requirements table,
vendor-database-schema.md): score 5 needs tier A + 3+ sources on that capability;
4 needs A/B + 2+; 3 needs >=C + 1; 2 needs any + 1; 1 needs 1 source. A capability
whose sources all dropped carries score null with an evidence_status note and is exempt.
Confidence must sit in the schema band for the score (5: 4-5, 4: 3-4, 3: 2-3, 2: 1-2).

Modes:
  --check   recompute and diff against stored values; exit 1 on any drift (CI/pre-commit)
  --stats   print aggregate figures for prose surfaces (totals, tier counts, coverage)
  --apply   rewrite evidence_summary blocks in place (stamps last_validated with --date)
"""

import argparse
import json
import sys
from collections import Counter
from pathlib import Path

DB = Path(__file__).resolve().parent.parent / "vendor-landscape" / "vendor-database.json"

TIER_ORDER = {"A": 0, "B": 1, "C": 2, "D": 3}
# score -> (allowed tiers for the capability's evidence.tier, min distinct sources, confidence band)
SCORE_REQUIREMENTS = {
    5: ({"A"}, 3, (4, 5)),
    4: ({"A", "B"}, 2, (3, 4)),
    3: ({"A", "B", "C"}, 1, (2, 3)),
    2: ({"A", "B", "C", "D"}, 1, (1, 2)),
    1: ({"A", "B", "C", "D"}, 1, (1, 5)),
}


def is_dropped(src):
    return str(src.get("evidence_status", "")).startswith("dropped")


def logical_sources(vendor):
    """Return {logical_id: source_dict} after mirror collapse, plus per-capability id sets."""
    vid = vendor["id"]
    logical = {}
    cap_ids = {}  # capability name -> set of logical ids evidencing it

    def add(src, capability=None):
        sid = src.get("id", "")
        if not sid or is_dropped(src):
            return
        logical.setdefault(sid, src)
        if capability:
            cap_ids.setdefault(capability, set()).add(sid)

    for cname, cval in (vendor.get("capabilities") or {}).items():
        if isinstance(cval, dict) and "score" in cval:
            for src in ((cval.get("evidence") or {}).get("sources") or []):
                add(src, capability=cname)
    for src in (((vendor.get("cost_modeling") or {}).get("evidence") or {}).get("sources") or []):
        add(src)
    for src in (vendor.get("evidence_sources") or []):
        sid = src.get("id", "")
        ctx = src.get("capability_context")
        if ctx and sid.startswith(f"{vid}-{ctx}-"):
            origin = sid[len(f"{vid}-{ctx}-"):]
            if origin in logical:  # mirror of a capability-level source
                if not is_dropped(src):
                    cap_ids.setdefault(ctx, set()).add(origin)
                continue
            # mirror whose original was dropped/absent: count under the origin id
            # so a future re-add of the original cannot double-count
            if not is_dropped(src):
                logical.setdefault(origin, src)
                cap_ids.setdefault(ctx, set()).add(origin)
            continue
        add(src, capability=ctx)
    return logical, cap_ids


def derive_summary(vendor, existing):
    logical, _ = logical_sources(vendor)
    tiers = Counter(s.get("evidence_tier", "D") for s in logical.values())
    total = len(logical)
    if total == 0:
        quality = "unevidenced"
    else:
        best = max(tiers.values())
        quality = sorted((t for t, n in tiers.items() if n == best),
                         key=lambda t: TIER_ORDER.get(t, 9))[-1]
    out = {
        "total_sources": total,
        "tier_a_sources": tiers.get("A", 0),
        "tier_b_sources": tiers.get("B", 0),
        "tier_c_sources": tiers.get("C", 0),
        "tier_d_sources": tiers.get("D", 0),
        "overall_evidence_quality": quality,
    }
    analyst = sum(1 for s in logical.values() if s.get("type") == "analyst_report")
    if analyst or "analyst_reports" in (existing or {}):
        out["analyst_reports"] = analyst
    return out


DERIVED_KEYS = ["total_sources", "tier_a_sources", "tier_b_sources", "tier_c_sources",
                "tier_d_sources", "overall_evidence_quality", "analyst_reports"]


def check_schema(vendor):
    """Yield (capability, problem) rows for score/evidence mismatches."""
    _, cap_ids = logical_sources(vendor)
    logical, _ = logical_sources(vendor)
    for cname, cval in (vendor.get("capabilities") or {}).items():
        if not (isinstance(cval, dict) and "score" in cval):
            continue
        score = cval.get("score")
        if score is None:
            if not str(cval.get("evidence_status", "")).startswith("unevidenced"):
                yield cname, "score null without an unevidenced_* evidence_status note"
            continue
        if score == 0:
            continue
        req = SCORE_REQUIREMENTS.get(score)
        if req is None:
            yield cname, f"score {score} outside 0-5"
            continue
        allowed_tiers, min_sources, band = req
        ev = cval.get("evidence") or {}
        tier = ev.get("tier")
        conf = ev.get("confidence")
        n = len(cap_ids.get(cname, set()))
        if tier not in allowed_tiers:
            yield cname, f"score {score} requires tier in {sorted(allowed_tiers)}, evidence.tier is {tier}"
        if n < min_sources:
            yield cname, f"score {score} requires {min_sources}+ distinct sources, capability has {n}"
        if conf is not None and not (band[0] <= conf <= band[1]):
            yield cname, f"score {score} confidence band is {band[0]}-{band[1]}, stored {conf}"


def main():
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    mode = ap.add_mutually_exclusive_group(required=True)
    mode.add_argument("--check", action="store_true")
    mode.add_argument("--stats", action="store_true")
    mode.add_argument("--apply", action="store_true")
    ap.add_argument("--date", default=None, help="last_validated stamp for --apply (YYYY-MM-DD)")
    args = ap.parse_args()

    data = json.loads(DB.read_text())
    vendors = data["vendors"]
    problems = []

    if data["meta"].get("vendor_count") != len(vendors):
        problems.append(("meta", "vendor_count", data["meta"].get("vendor_count"), len(vendors)))

    changed = 0
    agg = Counter()
    for v in vendors:
        existing = v.get("evidence_summary") or {}
        derived = derive_summary(v, existing)
        for k in DERIVED_KEYS:
            if k == "analyst_reports" and k not in derived and k not in existing:
                continue
            if existing.get(k) != derived.get(k):
                problems.append((v["id"], k, existing.get(k), derived.get(k)))
        for cname, msg in check_schema(v):
            problems.append((v["id"], f"schema:{cname}", msg, ""))
        agg["total"] += derived["total_sources"]
        for t in "abcd":
            agg[t.upper()] += derived[f"tier_{t}_sources"]
        if derived.get("analyst_reports"):
            agg["vendors_with_analyst"] += 1
        logical, _ = logical_sources(v)
        if any(s.get("type") == "production_deployment" for s in logical.values()):
            agg["vendors_with_production"] += 1
        if derived["total_sources"] == 0:
            agg["vendors_unevidenced"] += 1
        if args.apply:
            new_summary = dict(existing)
            before = {k: new_summary.get(k) for k in DERIVED_KEYS}
            new_summary.update(derived)
            if "analyst_reports" in new_summary and not new_summary["analyst_reports"] \
               and "analyst_reports" not in derived:
                del new_summary["analyst_reports"]
            if {k: new_summary.get(k) for k in DERIVED_KEYS} != before:
                changed += 1
                if args.date:
                    new_summary["last_validated"] = args.date
            v["evidence_summary"] = new_summary

    if args.stats:
        n = len(vendors)
        print(f"vendors: {n}")
        print(f"logical sources: {agg['total']} (A {agg['A']}, B {agg['B']}, C {agg['C']}, D {agg['D']})")
        pct = 100 * agg['A'] / agg['total'] if agg['total'] else 0
        print(f"tier A share: {pct:.1f}%")
        print(f"vendors with analyst report: {agg['vendors_with_analyst']} ({100*agg['vendors_with_analyst']/n:.1f}%)")
        print(f"vendors with production deployment: {agg['vendors_with_production']} ({100*agg['vendors_with_production']/n:.1f}%)")
        print(f"vendors with zero sources: {agg['vendors_unevidenced']} ({100*agg['vendors_unevidenced']/n:.1f}%)")
        return 0

    if args.apply:
        DB.write_text(json.dumps(data, indent=2, ensure_ascii=True) + "\n")
        print(f"applied: {changed} vendor evidence_summary blocks rewritten")
        schema_problems = [p for p in problems if str(p[1]).startswith("schema:")]
        for vid, key, msg, _ in schema_problems:
            print(f"  SCHEMA {vid} {key[7:]}: {msg}")
        return 0

    if problems:
        print(f"vendor rollup drift: {len(problems)} problem(s)")
        for vid, key, stored, derived_v in problems:
            if str(key).startswith("schema:"):
                print(f"  SCHEMA {vid} [{key[7:]}]: {stored}")
            else:
                print(f"  DRIFT  {vid}.{key}: stored={stored} derived={derived_v}")
        return 1
    print("vendor rollups: all derived values match stored values; schema compliant")
    return 0


if __name__ == "__main__":
    sys.exit(main())
