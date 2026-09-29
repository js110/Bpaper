# PMC submission upload guide

Target journal: **Pervasive and Mobile Computing**

Use the current files on main; do not reconstruct the package from historical commits.

## Upload files

- main.pdf — 28-page final review manuscript.
- PMC_submission_source.zip — flat one-level LaTeX source for Editorial Manager.
- supplement.pdf — 5-page supplementary technical material.
- highlights.docx — five Elsevier Highlights bullets.
- COVER_LETTER_DRAFT.md — author-reviewed text source for the cover letter.

PMC_submission_manifest.json is an internal package manifest and normally does not need to be uploaded.

## Internal files that are not submission items

- AUTHOR_CONFIRMATION.md
- PMC_SUBMISSION_CHECKLIST.md
- SOURCE_README.md
- raw results/, research/, literature/, workflows, and test files

Do not upload the raw GeoLife archive or third-party article full texts.

## Technical status

The validated main and flat-source builds are both 28 pages and text-equivalent. The supplement is 5 pages. All 31 automated tests pass, and the final LaTeX quality gate has no unresolved references, undefined control sequences, oversized floats, or overfull boxes.

The repository remains technical_ready=true and submission_ready=false until the responsible authors complete the remaining declarations and approvals listed in AUTHOR_CONFIRMATION.md.
