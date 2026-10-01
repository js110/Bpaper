# Bpaper: Sequential Mobile Crowdsensing Location Privacy

This branch contains the IEEE Transactions on Mobile Computing version of the BSP/R-BSP/DF-BSP study. The finalized Elsevier/PMC version is preserved on the `pmc` branch. All TMC manuscript and submission-format changes are isolated to the `tmc` branch.

## Canonical experimental artifact

The independently usable experimental code and the selected frozen numerical evidence for the TMC manuscript have been exported to [Branch-Safe (fixed artifact commit)](https://github.com/js110/Branch-Safe/tree/2dfaeeced5bb162203fa689b482d229371a17671). This `Bpaper/tmc` repository remains the manuscript and complete historical event-log archive. The export's source baseline is commit `2cc94ff6e7c4696dc364392dc19c8137d0cb7e65`; the new repository includes an evidence map and a Git blob SHA manifest so a reader can audit what was transferred without guessing from the moving branch.

## Current manuscript

- Target journal: *IEEE Transactions on Mobile Computing*.
- LaTeX format: IEEE Computer Society journal style via `\\documentclass[10pt,journal,compsoc]{IEEEtran}`.
- Main-paper policy used here: 12 formatted pages as the regular-paper baseline; submissions may be up to 18 pages.
- Supplemental material is a separate upload and is not counted toward the main-paper page limit.
- Manuscript structure: Introduction; Related Work; System Model and Branch-Safe Participation; Robustness and Disclosure-Floor Analysis; Evaluation; Conclusion.
- Scientific evidence is unchanged from the final model-input-isolated, window-weighted analysis.
- Technical TMC build status: see `research/manuscript_status.json` and the `tmc-build` workflow.
- Journal submission status: not submitted; author-owned declarations and approvals remain outstanding.

Primary files:

- `paper/main.tex` — IEEE TMC manuscript source.
- `paper/supplement.tex` — separate supplemental material.
- `paper/COVER_LETTER_DRAFT.md` — TMC cover-letter draft.
- `paper/TMC_SUBMISSION_CHECKLIST.md` — TMC technical and author checklist.
- `paper/SUBMISSION_UPLOAD_GUIDE.md` — TMC upload map.
- `research/tmc_conversion_notes.md` — format/style decisions and sources consulted.
- `research/manuscript_status.json` — machine-readable conversion status.

## Scientific scope

The paper studies a linkable truthful report/silence channel for mobile crowdsensing. It contains:

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

The validated CI path uses Python 3.12. LaTeX builds use TeX Live/latexmk with the IEEEtran publishers package.

## Data

The raw Microsoft GeoLife archive is not tracked. data/manifest.json records the source URL, SHA-256, preprocessing rule, user split, and selected windows. With data/geolife.zip present locally:

~~~bash
python3 -m src.prepare_data
~~~

The raw deterministic user-ID split contains 23 development, 17 validation, and 67 test candidates. Effective analyses additionally isolate complete 48-slot 8×8 state-path groups across development/validation/test; current effective counts are recorded in `results/geolife_decontamination.json`. Tasks and participation/report events are simulated; only the mobility traces are observational data.

## Reproducing experiments

Current evidence retained in main includes results/final, kl_baseline, sensitivity, reset_sensitivity_postfix, informed, recent_baselines, recent_privic_thinning, recent_comparison, robust_informed, robust_boundary, data_driven_ambiguity, data_driven_extension, review1_diagnostics, and their analysis/provenance files. The post-fix reset rerun supersedes the legacy `reset_every_*` rows for implementation-semantic verification; the legacy equal-prior rows remain only as historical frozen evidence.

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

## TMC build and submission preview

The `tmc-build` GitHub Actions workflow runs on pushes to the `tmc` branch. It executes the full test suite, compiles the IEEE-formatted manuscript and supplement, rejects unresolved references and layout failures, enforces the 18-page submission ceiling, and uploads a source/PDF preview artifact.

Before submission, complete the author-owned items in `paper/AUTHOR_CONFIRMATION.md` and `paper/TMC_SUBMISSION_CHECKLIST.md`.
