# Zenodo release checklist (owner-held mint)

Prepared 2026-07-12 as part of the 2B wave (ratified fork 2B-F2: mint a Zenodo DOI on a tagged release; the mint itself stays with the owner). The DOI is not a journal requirement — the DR-5 verification killed the "reviewers reject a bare GitHub link" claim — but one deposit is cheap and serves both the data- and code-availability statements in the DataCite `[dataset]` citation form, so the recommendation stands as mint. The metadata files this checklist depends on are already in the repo: `.zenodo.json` (Zenodo reads it from the release tarball and uses it instead of guessing metadata) and `CITATION.cff` (GitHub's cite-this-repository box).

## Step 0 — pre-mint prerequisites

> **Deposit scope (ruled 2026-07-16).** The v1 deposit is the curated paper export, not the full-repo release ZIP. Run `tools/build/export_paper.sh`, which builds the PDF, assembles `paper/` by whitelist, writes `paper/paper-export-manifest.txt`, and cuts a `dist/` tarball; review the manifest, then upload the tarball through Zenodo's manual upload form. The full-repo route was rejected because the release archive would freeze the expert-interview guides profiling named third parties and the internal cowork/audit docs into a DOI-permanent record, so the GitHub webhook toggle in Step 1 stays OFF for v1 and Steps 2-3 run against the manual deposit rather than a release archive (note a manual deposit never parses `.zenodo.json` — that file only drives webhook deposits — so the record metadata is entered in the Zenodo form, with `.zenodo.json` in the tarball as the reference copy). The mint itself remains owner-held.

- [x] **Add a LICENSE file.** ✅ Done 2026-07-13 (owner ruling H2: prep now, mint stays yours). `LICENSE` at the repo root carries the canonical Creative Commons Attribution 4.0 International legal code, fetched verbatim from `creativecommons.org/licenses/by/4.0/legalcode.txt` rather than retyped, so GitHub's license detection recognizes it. The matching keys are set in both metadata files: `"license": "cc-by-4.0"` in `.zenodo.json` (Zenodo's lowercased convention) and `license: CC-BY-4.0` in `CITATION.cff` (SPDX id). CC-BY-4.0 is the usual choice for a text review and matches OUP Gold-OA norms; if you want a different license the swap is three lines — replace `LICENSE` and edit the one key in each metadata file — and it must happen **before** the first deposit, because the license is fixed into the Zenodo record at mint.
- [x] **Confirm the availability statements exist in the manuscript.** ✅ Done — commit fea2e05 (2026-07-12, the 2B wave) added DATA AVAILABILITY and CODE AVAILABILITY sections to `PUBLICATION-MANUSCRIPT.md` (lines ~796/~802), each carrying a `10.5281/zenodo.PLACEHOLDER` for step 4 to replace. (This box's earlier "no such sections exist" text described the pre-fea2e05 state; verified closed 2026-07-16.)
- [x] **Dual-license the repo before the ZIP freezes.** ✅ Done 2026-07-16: code in `scripts/`, `tools/`, and `publication-graphics/` is MIT per `LICENSE-CODE` (Creative Commons recommends against CC licenses on software; The Turing Way's split is the model), the redistributed DM Sans / JetBrains Mono fonts carry their SIL OFL-1.1 texts at `tools/build/fonts/OFL-*.txt`, README gained a License section scoping all three, and `.zenodo.json` keeps `cc-by-4.0` as the single-valued record license with the carve-out stated in `notes`. Note: Zenodo record *metadata* (incl. license field) stays editable post-mint, but the release ZIP freezes — which is why this landed pre-tag.
- [ ] **Register an ORCID iD (owner).** Journal of Cybersecurity requires one at submission, and it should be in the Zenodo creator record from version 1: add `"orcid": "0000-...."` to `.zenodo.json` creators and `orcid: https://orcid.org/0000-....` to the CITATION.cff author before tagging.
- [ ] **Pick the Zenodo community entry (owner, optional).** Communities requests are only auto-submitted when declared in `.zenodo.json` at release time (format `"communities": [{"identifier": "<id>"}]`). Browse zenodo.org/communities for a fit (e.g. an open-science or security-research community) or skip — it can also be requested later from the record page.
- [ ] **Settle the tag scheme (owner — blocks step 2).** ~~The checklist below says `v2026.07` (CalVer) but the repo's citation convention is `YYYY-QX-v1.0`, and tag `2026-Q3-v1.0` already exists on the remote — pushed 2026-07-12, BEFORE any Zenodo webhook toggle, so it will never mint, and it now sits well behind HEAD. Pick one convention, mint from a fresh tag at current HEAD or later, and record the choice in CHANGELOG.md; two names for divergent snapshots would be a citation-stability failure.~~ **RULED 2026-07-16**: the convention stays `YYYY-QX-v1.0` (it is already the citation identity across CHANGELOG and the published snapshots; CalVer would introduce a second scheme mid-life). Execution stays with the owner because it needs push authority: delete the stale never-minted remote tag while nothing cites it and no DOI exists (`git push origin :2026-Q3-v1.0`, then `git tag -d 2026-Q3-v1.0` locally), re-tag `2026-Q3-v1.0` at the release-ready HEAD, and record both acts in CHANGELOG.md. Fallback if deleting a pushed tag is unacceptable on principle: leave it and mint from `2026-Q3-v1.1`, recording why. Box stays unchecked until the tag act happens.
- [ ] **Run the metadata validator before every tag**: `python3 scripts/validate_metadata.py` (parses both files, checks required keys, flags the fields that misbehave at release time, cross-checks the shared fields; runs `cffconvert --validate` when installed — CITATION.cff was schema-validated clean 2026-07-16). A structurally invalid file makes the whole release archiving fail silently on Zenodo's side.

## Step 1 — link the GitHub repo at Zenodo

- [ ] Log in at https://zenodo.org using the GitHub login (account owning `flying-coyote/security-data-literature-review`).
- [ ] Open https://zenodo.org/account/settings/github/, hit Sync if the repo list is stale, and flip the toggle ON for `flying-coyote/security-data-literature-review`. Nothing is deposited yet at this point; the toggle just subscribes Zenodo to future releases.

## Step 2 — tag and publish a release

- [ ] Pick a version tag that fits the living-review identity (G-R1), e.g. `v2026.07` for the quarterly snapshot. Either create the release in the GitHub Releases UI, or tag locally and push:

```bash
git tag -a v2026.07 -m "Living review snapshot 2026-07"
git push origin v2026.07
```

then create a GitHub Release from that tag (Zenodo triggers on the *release* webhook, not on the bare tag). Zenodo archives the release tarball within a few minutes and reads `.zenodo.json` for the deposit metadata.

## Step 3 — record the two DOIs

- [ ] The deposit lands with a **version DOI** (this snapshot) and a **concept DOI** (resolves to the latest version, shown on the record page as "Cite all versions"). For a living review the concept DOI is the citation target in the availability statements, with the version DOI available where a reviewer wants the exact snapshot pinned.

## Step 4 — replace the manuscript's DOI placeholders

- [ ] Locate the placeholders in the two availability statements (added by the 2B wave per Step 0) and substitute the real DOIs:

```bash
grep -n -i "data availability\|code availability\|10\.5281\|DOI" PUBLICATION-MANUSCRIPT.md
```

As of 2026-07-12 these sections do not exist yet, so exact line numbers cannot be named here; once the 2B statement sections are in, the grep above finds them directly (Zenodo DOIs carry the `10.5281/zenodo.` prefix). Both statements point at the same deposit, cited in the DataCite `[dataset]` form the DR-5 intake verified.

## Step 5 — back-fill the repo metadata

- [ ] Add the concept DOI to `CITATION.cff` under `identifiers:` (type `doi`), plus `version:` and `date-released:` matching the tag.
- [ ] Verify the Zenodo record page rendered the `.zenodo.json` metadata correctly (title, creator, description, keywords, license); fix in the repo and re-release if anything is off, since record metadata for GitHub deposits is also editable in the Zenodo UI.

## Step 6 — subsequent quarterly releases

- [ ] Nothing to re-link: each new tagged GitHub Release mints a new version DOI under the same concept DOI automatically. Keep `.zenodo.json` and `CITATION.cff` current before tagging, since the deposit metadata is read at release time.
