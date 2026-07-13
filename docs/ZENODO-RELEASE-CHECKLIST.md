# Zenodo release checklist (owner-held mint)

Prepared 2026-07-12 as part of the 2B wave (ratified fork 2B-F2: mint a Zenodo DOI on a tagged release; the mint itself stays with the owner). The DOI is not a journal requirement — the DR-5 verification killed the "reviewers reject a bare GitHub link" claim — but one deposit is cheap and serves both the data- and code-availability statements in the DataCite `[dataset]` citation form, so the recommendation stands as mint. The metadata files this checklist depends on are already in the repo: `.zenodo.json` (Zenodo reads it from the release tarball and uses it instead of guessing metadata) and `CITATION.cff` (GitHub's cite-this-repository box).

## Step 0 — pre-mint prerequisites

- [x] **Add a LICENSE file.** ✅ Done 2026-07-13 (owner ruling H2: prep now, mint stays yours). `LICENSE` at the repo root carries the canonical Creative Commons Attribution 4.0 International legal code, fetched verbatim from `creativecommons.org/licenses/by/4.0/legalcode.txt` rather than retyped, so GitHub's license detection recognizes it. The matching keys are set in both metadata files: `"license": "cc-by-4.0"` in `.zenodo.json` (Zenodo's lowercased convention) and `license: CC-BY-4.0` in `CITATION.cff` (SPDX id). CC-BY-4.0 is the usual choice for a text review and matches OUP Gold-OA norms; if you want a different license the swap is three lines — replace `LICENSE` and edit the one key in each metadata file — and it must happen **before** the first deposit, because the license is fixed into the Zenodo record at mint.
- [ ] **Confirm the availability statements exist in the manuscript.** As of this writing `PUBLICATION-MANUSCRIPT.md` carries no Data-availability or Code-availability section and no DOI placeholder (verified by grep 2026-07-12; the only DOI strings in the file are reference-list DOIs of cited papers). The placeholders this checklist later replaces are the ones in the data/code availability statements added by the 2B wave (fix-list item 1 in `STAGED-2B-litreview-findings-2026-07-12.md`), so if that agent has not yet run, run it first or add the two sections by hand.

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
