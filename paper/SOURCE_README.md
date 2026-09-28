# Manuscript source and submission bundle

The working manuscript targets *Pervasive and Mobile Computing* and uses Elsevier's `elsarticle` review layout.

Development build:

    latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex

The repository keeps a convenient development layout, including the `figures/` subdirectory. Elsevier Editorial Manager does not process LaTeX submissions with subfolders, so the development folder itself should not be uploaded as the final LaTeX source package.

The final checkpoint workflow `.github/workflows/pmc-final-package.yml` builds a separate flat source package:
- `PMC_submission_source.zip`: one-level LaTeX source and all referenced figures/tables;
- `PMC_submission_manifest.json`: exact packaged-file manifest;
- `highlights.docx`: Elsevier Highlights upload file generated from `highlights.txt`;
- `main.pdf`: compiled review manuscript.

The workflow independently compiles both the development source and the flat source, rejects unresolved references, undefined controls, overfull boxes, or oversized floats, and compares their extracted PDF text.

Current scientific contents include nominal BSP, finite-model R-BSP, development/validation-derived R-BSP, asymmetric DF-BSP/RDF-BSP, informed-attacker and ambiguity-boundary stress tests, region-size-aware utility, and recent PML-T/PRIVIC-T task-channel comparisons. The ambiguity and disclosure-floor extensions are explicitly post-hoc and are not presented as independent confirmatory evidence.

Final validated inventory:
- main manuscript: 27 pages, 1 figure, 2 tables;
- supplementary technical material: 58 pages;
- 21 cited references;
- 28 automated tests;
- final flat Editorial Manager source independently compiles to the same 27-page text as the development source;
- final packaging workflow: GitHub Actions run 36369413681, successful.

Full code, configurations, raw event logs, analyses, provenance, internal reviews, and reproduction notes are stored in the repository root. Third-party article full texts and the raw GeoLife archive are not part of the distributable submission source.

Author-owned declarations remain separate in `AUTHOR_CONFIRMATION.md`. The repository must not claim final author approval, competing-interest status, CRediT roles, funder roles, data-use/ethics wording, or other submission declarations until the responsible authors confirm them.

Working repository: https://github.com/js110/Bpaper
