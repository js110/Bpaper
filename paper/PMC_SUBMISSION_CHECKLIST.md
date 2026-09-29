# Pervasive and Mobile Computing submission preparation

Prepared on 2026-09-28 for branch `submission/pmc-2026-09-26`.

## Template and file format

- The manuscript uses Elsevier's official `elsarticle` class.
- The final review manuscript uses `\documentclass[review,11pt,times]{elsarticle}`.
- The journal field is set to `Pervasive and Mobile Computing`.
- The author-facing "Draft status" paragraph was removed from the submission copy.
- Keep all LaTeX submission files at one folder level when packaging for Editorial Manager; Elsevier's current LaTeX instructions state that subfolders are not supported by its processing workflow.
- `highlights.txt` is the editable source; the final packaging workflow generates `highlights.docx` for upload as the Elsevier Highlights file. It contains 5 acronym-free bullets, each <=85 characters.

## Items that must be author-confirmed before submission

Do not invent any of the following. The responsible authors must confirm them:

1. all-author approval of the final manuscript;
2. declaration of competing interests;
3. CRediT author contributions, if requested;
4. funders' roles;
5. data-use / ethics determination for the secondary GeoLife data;
6. any AI-related disclosure or figure-caption wording required by the journal, to be handled by the authors before submission;
7. whether the repository will remain a working GitHub repository or be archived in an immutable release.

## Manuscript structure

- The main manuscript now has six numbered sections only: Introduction; Related Work; Proposed Branch-Safe Participation Framework; Privacy Guarantees and Robustness Analysis; Experimental Evaluation; Conclusion.
- Data and Code Availability and Funding remain unnumbered submission sections.

## Scientific items that remain more important than formatting


- Robustness to attacker/model mismatch: finite-set R-BSP, outside-set boundary tests, and a development/validation-derived replay ambiguity-set construction are implemented. The extension remains post-hoc because the test users had been inspected in earlier analyses; the manuscript states this limitation explicitly.
- Fine-region service: strict BSP/R-BSP still has a structural truthful-report floor. DF-BSP/RDF-BSP now exposes a separate report ceiling while retaining the strict BSP silence cap, and reports inverse-area-weighted and 1--8-cell retention.
- Test-selected recent-baseline envelopes remain exploratory and are labeled as such; no confirmatory claim is made from them.
- Novelty claims remain bounded to the visible truthful report/silence channel, finite-model robustness, and explicit disclosure-floor service trade-off.

Scientific issues above are now either implemented or explicitly bounded in the claims. Final technical QA is complete: the 28-page development manuscript, 28-page flat-source rebuild, and 11-page supplementary technical material compile cleanly; the flat and development PDFs are text-equivalent. The remaining blockers are author-owned declarations/approvals.

## Current validation workflow

- `code-tests.yml`: automatic, source/config/test changes only; superseded runs are cancelled.
- `rbsp-validation.yml`: manual checkpoint for the full robust stress; no LaTeX work.
- `rbsp-boundary.yml`: explicit sentinel/manual boundary experiment only.
- `paper-build.yml`: manual or `paper/.build-request` checkpoint only; ordinary manuscript edits do not launch TeX installation.
- `pmc-final-package.yml`: final checkpoint only; builds a flat Editorial Manager source zip, recompiles it independently, compiles the supplement, compares extracted PDF text with the development build, and generates `highlights.docx`. Final run 36511273191 passed all steps.

## Final author-owned blockers

- Complete any AI-related journal disclosure/caption requirements before submission; this is intentionally left for the authors to handle.
- Author names/order/affiliation/corresponding details and the four grant names/numbers have been copied from the supplied reference paper. Confirm competing interests, CRediT contributions, funder roles, and the GeoLife ethics/data-use determination.
- Decide whether to cite a versioned GitHub release or an immutable archive/DOI rather than only the moving repository URL.
