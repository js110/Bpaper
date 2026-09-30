# Bpaper：Sequential Mobile Crowdsensing Location Privacy

This repository contains the current manuscript and reproducibility record for the BSP/R-BSP/DF-BSP study. The canonical branch is **main**. The canonical machine-readable submission state is `research/manuscript_status.json`; checked-in PDFs and ZIP artifacts should be treated as current only when that file reports `technical_ready=true` for the validated source SHA.

## Current manuscript

- Target journal: *Pervasive and Mobile Computing*.
- Main manuscript: 28 pages, 6 numbered sections, 1 main figure, 2 main tables.
- Supplementary material: 5 pages.
- References: 21 cited entries.
- Automated tests: 31.
- Recorded experiment executions: 28,973 trajectories and 1,390,704 audited slot events.
- Technical package status: see `research/manuscript_status.json`. Any evidence or manuscript-source change requires a fresh final-package validation before upload.
- Journal submission status: not submitted; author-owned declarations and approvals remain outstanding.

Primary files:

- paper/main.pdf — current review manuscript.
- paper/main.tex — current LaTeX source.
- paper/supplement.pdf and paper/supplement.tex — focused technical supplement.
- paper/PMC_submission_source.zip — flat Editorial Manager source archive.
- paper/highlights.docx — Highlights upload file.
- paper/SUBMISSION_UPLOAD_GUIDE.md — upload map.
- research/manuscript_status.json — canonical machine-readable status.

Historical drafts, failed/interrupted runs, preview screenshots, and superseded package artifacts were removed from main after finalization. They remain recoverable from Git history.

## Scientific scope

The paper studies a linkable truthful report/silence channel for ordinary mobile crowdsensing. It contains:

- BSP: a maximal scalar participation gate for report and silence posterior branches.
- R-BSP: finite-model robust intersection of BSP gates.
- DF-BSP/RDF-BSP: an explicit report-side threshold for the truthful-report disclosure floor while silence keeps the original BSP local cap.
- Synthetic and GeoLife evaluation, stronger-model replay attacks, ambiguity-set boundary tests, and PML-T/PRIVIC-T task-channel comparisons.

The guarantees are Bayesian, channel-specific, and model-set-specific. They are not differential privacy, geo-indistinguishability, or a guarantee against arbitrary auxiliary information.

## Environment and tests

~~~bash
python3 -m venv .venv
source .venv/bin/activate
python3 -m pip install -r requirements-lock.txt
python3 -m unittest discover -s tests -v
python3 -m src.audit
~~~

Python 3.10+ is supported. LaTeX builds use TeX Live/latexmk and the tracked elsarticle class/BST.

## Data

The raw Microsoft GeoLife archive is not tracked. data/manifest.json records the source URL, SHA-256, preprocessing rule, user split, and selected windows. With data/geolife.zip present locally:

~~~bash
python3 -m src.prepare_data
~~~

The raw deterministic user-ID split contains 23 development, 17 validation, and 67 test candidates. Effective analyses additionally isolate complete 48-slot 8×8 state-path groups across development/validation/test; current effective counts are recorded in `results/geolife_decontamination.json`. Tasks and participation/report events are simulated; only the mobility traces are observational data.

## Reproducing experiments

Current evidence retained in main includes results/final, kl_baseline, sensitivity, informed, recent_baselines, recent_privic_thinning, recent_comparison, robust_informed, robust_boundary, data_driven_ambiguity, data_driven_extension, review1_diagnostics, and their analysis/provenance files.

A fresh run should use a new output directory rather than overwrite frozen evidence:

~~~bash
python3 -m src.reproduce --output results/reproduction_01
~~~

The checked-in result directories are frozen evidence. Do not run a frozen config directly into its checked-in output directory. For the robust and data-driven extensions, either clone the config and change its output path, or use the manual rbsp-validation, rbsp-boundary, and data-driven-extension GitHub Actions workflows to intentionally refresh the tracked evidence.

## Regenerating manuscript assets

~~~bash
python3 -m src.analyze --run results/combined
python3 -m src.analyze_stress
python3 -m src.analyze_recent --paper-assets
python3 -m src.review_diagnostics --paper-assets
python3 -m src.analyze_extensions --run results/data_driven_extension --paper-assets
python3 -m src.paper_assets
cd paper
latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex
latexmk -pdf -interaction=nonstopmode -halt-on-error supplement.tex
~~~

src.paper_assets only synchronizes assets used by the current manuscript; it does not rewrite references, templates, or manuscript text.

## Submission package

The pmc-final-package GitHub Actions workflow runs on main manuscript-source changes and can also be started manually. It runs the unit tests, compiles the development manuscript and supplement, builds and independently compiles the flat Editorial Manager source, verifies PDF text equivalence, and refreshes the final upload artifacts.

Before submission, complete the author-owned items in paper/AUTHOR_CONFIRMATION.md and paper/PMC_SUBMISSION_CHECKLIST.md.
