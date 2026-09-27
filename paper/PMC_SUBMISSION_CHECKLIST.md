# Pervasive and Mobile Computing submission preparation

Prepared on 2026-09-26 for branch `submission/pmc-2026-09-26`.

## Template and file format

- The manuscript uses Elsevier's official `elsarticle` class.
- The review branch uses `\documentclass[review,12pt]{elsarticle}`.
- The journal field is set to `Pervasive and Mobile Computing`.
- The author-facing "Draft status" paragraph was removed from the submission copy.
- Keep all LaTeX submission files at one folder level when packaging for Editorial Manager; Elsevier's current LaTeX instructions state that subfolders are not supported by its processing workflow.
- A separate `highlights.txt` file has been added. Elsevier's general highlights guidance specifies 3--5 bullets, no more than 85 characters each. Journal-specific requirements still need a final check in the live Guide for Authors.

## Items that must be author-confirmed before submission

Do not invent any of the following. The responsible authors must confirm them:

1. final author order and spelling;
2. affiliation and corresponding-author details;
3. all grant names and numbers;
4. declaration of competing interests;
5. CRediT author contributions, if requested;
6. funders' roles;
7. data-use / ethics determination for the secondary GeoLife data;
8. final generative-AI disclosure wording under Elsevier's current policy; substantive AI use requires a separate declaration immediately before the references, and AI-generated/AI-altered figures require tool disclosure in the relevant captions;
9. whether the repository will remain a working GitHub repository or be archived in an immutable release.

## Scientific items that remain more important than formatting

- Robustness to attacker/model mismatch: finite-set R-BSP, outside-set boundary tests, and a development/validation-derived replay ambiguity-set construction are implemented. The extension remains post-hoc because the test users had been inspected in earlier analyses; the manuscript states this limitation explicitly.
- Fine-region service: strict BSP/R-BSP still has a structural truthful-report floor. DF-BSP/RDF-BSP now exposes a separate report ceiling while retaining the strict BSP silence cap, and reports inverse-area-weighted and 1--8-cell retention.
- Test-selected recent-baseline envelopes remain exploratory and are labeled as such; no confirmatory claim is made from them.
- Novelty claims remain bounded to the visible truthful report/silence channel, finite-model robustness, and explicit disclosure-floor service trade-off.

Scientific issues above are now either implemented or explicitly bounded in the claims. The remaining submission blockers are author-owned declarations/approvals and a final compiled-file check.

## Current validation workflow

- `code-tests.yml`: automatic, source/config/test changes only; superseded runs are cancelled.
- `rbsp-validation.yml`: manual checkpoint for the full robust stress; no LaTeX work.
- `rbsp-boundary.yml`: explicit sentinel/manual boundary experiment only.
- `paper-build.yml`: manual or `paper/.build-request` checkpoint only; ordinary manuscript edits do not launch TeX installation.

## Final author-owned blockers

- Approve the factual AI disclosure draft in `paper/AI_DECLARATION_DRAFT.md` and insert the approved statement before the references.
- Confirm competing interests, CRediT contributions, funder roles, author names/order/affiliation/corresponding details, and the GeoLife ethics/data-use determination.
- Decide whether to cite a versioned GitHub release or an immutable archive/DOI rather than only the moving repository URL.
