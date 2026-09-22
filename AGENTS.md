# Repository instructions

## Manuscript and integrity

- The canonical source is `mathieu_second_conjecture_spherical_pairs.tex`; its PDF is tracked.
- Preserve mathematical statements, hypotheses, proof content, authorship, notation, and stable labels unless explicitly instructed to change them.
- The manuscript has one author: Christopher D. Long. Do not add coauthors without explicit instruction.
- Flag suspected mathematical errors; do not silently repair, weaken, or broaden claims.
- Keep mathematical changes separate from migration and editorial changes.
- Compile with `latexmk -pdf -interaction=nonstopmode -halt-on-error mathieu_second_conjecture_spherical_pairs.tex`.
  Check undefined citations/references and layout warnings before committing a new PDF.
- Do not commit LaTeX auxiliary files or build caches.

## Exact verification

- Auxiliary verification scripts and checked outputs belong in `scripts/`.
- Install `scripts/requirements.txt` and run `python scripts/check_verification.py`.
- Do not silently regenerate `scripts/verification_output.txt` to make checks pass.
- Finite computational checks are diagnostics, not proofs of the manuscript's all-exponent identities or branching statements.
- The classification proof cites external theorems, including Duistermaat--van der Kallen, affine Hilbert--Mumford, branching rules, and the radial-transfer theorem from arXiv:2609.16178. Preserve those dependencies explicitly.

## Formalization

- No Lean project is currently part of this repository. Do not add Lean scaffolding merely for symmetry with other repositories.
- If formalization work is explicitly started, use a root Lake project, a named module directory, a root umbrella module, `FORMALIZATION_STATUS.md`, and explicit axiom/dependency audits, following the current `long-mathematics` conventions.
- Never claim formal verification before statement correspondence and transitive dependency audits are complete.

## Git workflow

Use a feature branch, pull request, successful applicable CI, and squash merge.
Never bypass protections, force-push `main`, or overwrite unique source material.

## Documentation

Keep this tree a current paper companion, not a development archive. The README should cover the abstract, manuscript links, theorem status, reproducible checks, related work, citation, and license. Do not add local source paths, obsolete drafts, redundant build logs, or migration narratives.
