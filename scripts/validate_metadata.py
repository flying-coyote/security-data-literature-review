#!/usr/bin/env python3
"""validate_metadata.py — pre-tag validation of the two Zenodo-facing metadata files.

A structurally invalid .zenodo.json or CITATION.cff makes the GitHub-release
archiving fail with nothing published, and the failure is only visible in
Zenodo's sync log (Zenodo FAQ; verified 2026-07-16). This script is the cheap
insurance the release checklist invokes before every tag:

  - .zenodo.json must parse as JSON and carry the keys a deposit needs
    (title, upload_type, creators[].name, description, license), and must NOT
    carry the keys that misbehave at release time (a static 'version' repeats
    across releases; 'doi' is a no-op).
  - CITATION.cff must parse as YAML with cff-version, message, title, authors,
    and a type in the CFF-legal set {software, dataset}. If cffconvert is
    installed, its validator runs too (schema-level, stricter).
  - The fields the two files share (title, license, author family name) must
    agree, because Zenodo reads only .zenodo.json while GitHub's citation
    widget reads only CITATION.cff, and nothing else reconciles them.

Exit 0 = both valid and consistent; exit 1 = any failure, with reasons printed.
"""

import json
import shutil
import subprocess
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
errors = []


def check_zenodo():
    p = REPO / ".zenodo.json"
    try:
        d = json.loads(p.read_text(encoding="utf-8"))
    except Exception as e:
        errors.append(f".zenodo.json does not parse: {e}")
        return None
    for key in ("title", "upload_type", "creators", "description", "license"):
        if key not in d:
            errors.append(f".zenodo.json missing required key: {key}")
    for c in d.get("creators", []):
        if "name" not in c:
            errors.append(f".zenodo.json creator missing 'name': {c}")
    for bad in ("version", "doi"):
        if bad in d:
            errors.append(
                f".zenodo.json carries '{bad}' — remove it (a static version repeats "
                "across releases; the doi field is a no-op at deposit time)"
            )
    if d.get("upload_type") == "publication" and "publication_type" not in d:
        errors.append(".zenodo.json upload_type=publication requires publication_type")
    return d


def check_cff():
    p = REPO / "CITATION.cff"
    try:
        import yaml
        d = yaml.safe_load(p.read_text(encoding="utf-8"))
    except ImportError:
        d = None
        errors.append("PyYAML not installed — CFF checked only via cffconvert (if present)")
    except Exception as e:
        errors.append(f"CITATION.cff does not parse as YAML: {e}")
        return None
    if d is not None:
        for key in ("cff-version", "message", "title", "authors"):
            if key not in d:
                errors.append(f"CITATION.cff missing required key: {key}")
        if d.get("type") not in ("software", "dataset"):
            errors.append(
                f"CITATION.cff type '{d.get('type')}' is not CFF-legal (software|dataset)"
            )
    if shutil.which("cffconvert"):
        r = subprocess.run(
            ["cffconvert", "--validate", "-i", str(p)], capture_output=True, text=True
        )
        if r.returncode != 0:
            errors.append(f"cffconvert --validate failed: {(r.stderr or r.stdout).strip()}")
        else:
            print("cffconvert: CITATION.cff schema-valid")
    else:
        print("cffconvert not installed (pip install cffconvert) — schema check skipped")
    return d


def main():
    z = check_zenodo()
    c = check_cff()
    if z and isinstance(c, dict):
        if z.get("title") != c.get("title"):
            errors.append("title differs between .zenodo.json and CITATION.cff")
        zl = (z.get("license") or "").replace("-", "").lower()
        cl = str(c.get("license") or "").replace("-", "").lower()
        if zl != cl:
            errors.append(
                f"license id differs: .zenodo.json '{z.get('license')}' vs CITATION.cff '{c.get('license')}'"
            )
        zn = {cr.get("name", "").split(",")[0].strip() for cr in z.get("creators", [])}
        cn = {a.get("family-names", "") for a in c.get("authors", []) if isinstance(a, dict)}
        if zn != cn:
            errors.append(f"author family names differ: {zn} vs {cn}")
    if errors:
        print("validate-metadata: FAIL")
        for e in errors:
            print(f"  - {e}")
        return 1
    print("validate-metadata: both files valid and consistent.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
