# PMC submission upload guide

Use this file to avoid uploading stale or development-only artifacts.

## Primary manuscript
- `main.pdf` — final review PDF generated from the validated main LaTeX source.
- `PMC_submission_source.zip` — flat one-level LaTeX source package for Editorial Manager. This is the source archive to use; the older `manuscript_source.zip` has been removed.
- `PMC_submission_manifest.json` — internal manifest listing every file contained in the flat source archive.

## Supplementary material
- `supplement.pdf` — extended methods, comparator details, diagnostic figures/tables, model-mismatch/boundary results, task-size analysis, and reproducibility information.
- `supplement.tex` — editable supplementary source retained in the repository. Upload the PDF unless the submission system explicitly requests supplementary source files.

## Other submission files
- `highlights.docx` — five Highlights bullets generated from `highlights.txt`.
- `COVER_LETTER_DRAFT.md` — cover-letter text; responsible authors must confirm any originality, conflict, ethics, funding-role, or approval statements before use.
- `AUTHOR_CONFIRMATION.md` — internal author checklist; do not upload this file.

## Do not upload as the manuscript source
- `full_research_record.tex` — archived pre-condensation research record.
- development-only figures/tables not listed in `PMC_submission_manifest.json`.
- raw GeoLife archives, third-party article full texts, result logs, or internal review files.

## Technical validation
- final main manuscript: 27 pages;
- flat source independently compiles and is text-equivalent to the development build;
- 28 automated tests pass;
- no final unresolved references, undefined control sequences, oversized floats, or overfull boxes;
- final source package has no subfolders.

Repository state remains `technical_ready=true`, `submission_ready=false` until the responsible authors complete `AUTHOR_CONFIRMATION.md`.