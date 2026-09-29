# Release checklist: Backbrief (base)

Adapted from the predecessor's checklist (media-system-stack, 2026-08-18). Every step names its check. Tooling never tags, pushes, uploads or deploys; the steps marked OWNER stop for Charles (escalation rule).

Run from the repo root `C:\business\vault\backbrief-base`. `python` is `C:\Users\cashe\AppData\Local\Programs\Python\Python312\python.exe`.

## 1. Preconditions

| # | Check | How to tell |
|---|---|---|
| 1 | License adopted and present | `LICENSE.md` exists at the repo root and Charles named it (the license is his to name). `build_zip.py` gate `license`. |
| 2 | Buyer docs present | `docs/README.md` exists (the buyer README); every other buyer document is in `docs/`. Gate `docs`. |
| 3 | Version stamps agree | Root `VERSION` and `payload/.claude/VERSION` ("Backbrief <VERSION>"). Gate `version`. Also re-read any count or list that a bumped number heads. |
| 4 | CHANGELOG has an entry for this version | Read `CHANGELOG.md`; the version is not still under "Unreleased". |
| 5 | Manifest in sync | `python tools/manifest_build.py` exits 0. If it does not, run `--fix`, then re-read the diff. Gate `manifest`. |
| 6 | Third-party license files kept | Every skill in the table of `payload/.claude/skills/THIRD-PARTY-LICENSES.md` carries its LICENSE. Gate `thirdparty`. |
| 7 | Verifier pass on anything changed since the last release | Fresh-context verifier gets the changed files plus acceptance criteria only (verify-before-delivery rule). Confirmed findings are fixed; "no confirmed issues" is a valid result. |
| 8 | Working tree clean and level with origin | `git status` shows nothing to commit; `git fetch` then `git status` shows neither ahead nor behind. |

The standing question at every step: not "did I change it" but "what else describes this, and did that change too?" (site version strings, the buyer README, the changelog).

## 2. Build

1. `python tools/build_zip.py --check` prints PASS on every gate.
2. `python tools/build_zip.py` writes `dist/backbrief-<VERSION>.zip` and prints the entry count, byte size, zip sha256 and content digest. `dist/` is gitignored.
3. Note both hashes. The zip sha256 identifies the exact bytes you will upload. The content digest is the one a rebuild from the same commit must reproduce (the zip itself is not byte-reproducible, because zip entries carry file mtimes).

## 3. Install check

`python tools/install_check.py dist/backbrief-<VERSION>.zip` prints the zip sha256 and content digest, then PASS on every line, and exits 0. It unpacks the zip, installs it into a scratch project as the install guide says, and checks names, SKILL.md frontmatter, every manifest hash and the scaffold. Any FAIL blocks the release; fix the repo and rebuild, never patch the zip by hand.

Then a fresh-context verifier pass on the built zip's contents (item 7 again, now on the artifact that ships).

## 4. Record and tag

1. Add to the `CHANGELOG.md` entry for this version: the zip sha256, the content digest, and the commit hash the zip was built from. Commit that (the changelog inside the zip predates its own hashes; that is expected, the repo copy is the record).
2. OWNER: tag `v<VERSION>` on that commit, or say "tag it" and it is done on that GO. Tooling never creates the tag.

## 5. Publish (each stops for the owner)

| Step | OWNER decision |
|---|---|
| Make the repo public | A release; every push after it is a release too. |
| Upload the zip to the site's downloads location | Upload the new file before removing the old one, then re-read the file list. |
| Deploy the site page and any version strings | Publishing is outward. |
| Commerce surfaces, if this release changes anything they describe | Price and refund wording are Charles's. |

## 6. After publish, before calling it shipped

1. Download the zip from the live URL, run `python tools/install_check.py <downloaded zip>`, and confirm the zip sha256 it prints equals the one recorded in `CHANGELOG.md`. A watcher's report is a claim, not verification.
2. Confirm the repo (if public) shows the same version stamp as the zip.
3. Repo ends clean and level with origin.

## 7. Rollback: a shipped zip is bad

`dist/` is gitignored, so old zips are not kept in version control. What is kept: every released zip's sha256, content digest and source commit, recorded in `CHANGELOG.md` (step 4).

1. Find the last good release in `CHANGELOG.md`; note its commit, zip sha256 and content digest.
2. `git checkout <that commit>` in a clean clone or worktree (not this working tree if it holds uncommitted work).
3. `python tools/build_zip.py`, then `python tools/install_check.py dist/backbrief-<VERSION>.zip`.
4. Compare the content digest to the recorded one; it must match. (The zip sha256 will not match a rebuild, because of mtimes. It matches only if you still hold the exact original file, in which case prefer re-uploading that file.)
5. OWNER: re-upload the rebuilt zip over the bad one, verify by downloading it (step 6.1; compare the content digest it prints), then record the rollback in `CHANGELOG.md` and the decision log.
6. If a tag pointed at the bad release, retagging or deleting it is the owner's call; do not force-move a published tag.
