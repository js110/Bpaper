# PMC submission upload guide

Target journal: **Pervasive and Mobile Computing**

Use only the files produced for the source SHA recorded in `../research/manuscript_status.json`; do not reconstruct the package from historical commits or mix artifacts from different runs.

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

Before upload, verify that `../research/manuscript_status.json` reports `technical_ready=true`, `data_status.refresh_required=false`, and a `final_package_source_sha` matching the manuscript source being submitted. The same record must report successful development/flat/supplement compilation, flat-source text equivalence, and ZIP-manifest verification. Page counts are taken from that validated build rather than copied from an older package.

`submission_ready` remains false until the responsible authors complete the declarations and approvals in `AUTHOR_CONFIRMATION.md`.
