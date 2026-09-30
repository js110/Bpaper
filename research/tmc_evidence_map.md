# TMC evidence-to-manuscript map

This file records the source-of-truth path from frozen experiment evidence to the quantitative material used in the TMC manuscript. It is intended to prevent manual number drift; it is not an additional statistical analysis.

| Manuscript item | Generated/source file | Evidence / configuration | Provenance / integrity record |
|---|---|---|---|
| GeoLife effective split counts and prior-only diagnostic macros | `paper/review_numbers.tex` | `data/geolife_development.npz`, `data/geolife_validation.npz`, `data/geolife_test.npz`; `results/review1_diagnostics/` | `results/review1_diagnostics/provenance.json` records SHA-256 hashes for all three NPZ inputs and the main replay inputs. |
| Data-driven ambiguity-set model count, selection mass, movement estimates | `paper/current_numbers.tex`; `results/data_driven_ambiguity/models.json` | effective GeoLife development/validation groups; model selection target 0.95 | `models.json` is the canonical selected-model record; selected mass is 0.9695 with two selected population-prior models. |
| GeoLife strict robustness table | `paper/data_driven_table.tex` | `results/data_driven_extension/rows.csv`, config snapshot `results/data_driven_extension/config.json` | generated analysis files live in `results/data_driven_extension/analysis/`; repository blob SHAs bind the config, rows, table and summary at the submitted commit. |
| DF-BSP / RDF-BSP frontier | `paper/dfbsp_table.tex` | `results/data_driven_extension/rows.csv` | `results/data_driven_extension/analysis/summary.csv` and `report.json` are the numerical source. |
| Hand-grid R-BSP stress | `paper/robust_table.tex` | `results/robust_informed/` | `results/robust_informed/analysis/provenance.json`: 1000 bootstrap replicates, synthetic-seed clusters, explicit 3x3 move/availability ambiguity grid. |
| Outside-set boundary stress | `paper/robust_boundary_table.tex` | `results/robust_boundary/` | `results/robust_boundary/analysis/provenance.json`: same clustering/bootstrap convention; primary endpoint is attacker local-cap violation rate. |
| Grid / mobility / availability sensitivity quoted in text | `results/sensitivity/analysis/summary.csv` | `configs/sensitivity.json`, `results/sensitivity/rows.csv` | `results/sensitivity/analysis/provenance.json` records input SHA-256 `b2b59173d8a81b93e77e53f3665858f6e580fc1fe2f6f454d6b71a809837c07b`. |
| Reset-period sensitivity after reset-prior fix | `results/reset_sensitivity_postfix/rows.csv` | `configs/reset_sensitivity_postfix.json`; 9 reset conditions, 360 trajectories | `results/reset_sensitivity_postfix/legacy_comparison.json` records source SHA, config/rows SHA-256, equal key sets, and zero differences across retained metrics versus the legacy equal-prior reset rows. The manuscript does not use the legacy reset rows for a distinct-prior claim. |
| Recent PML-T / PRIVIC-T exploratory comparisons | `results/recent_comparison/summary.csv` and matched-utility records | `results/recent_baselines/rows.csv`, `results/recent_privic_thinning/rows.csv`, `results/final/rows.csv` | `results/recent_comparison/provenance.json` records input SHA-256 hashes and the exploratory lower-convex-envelope interpolation rule. |
| Post-review spatial-availability, nonstationary-mobility, and two-step probe stress | `paper/reviewer_stress_table.tex` | `configs/tmc_reviewer_stress.json`, `results/tmc_reviewer_stress/rows.csv` | `results/tmc_reviewer_stress/analysis/provenance.json`: config SHA-256 `a4a654ac02f3283be33fdedcffc447eb0a08afef8332ba0c97844cad8be58477`; rows SHA-256 `de830c98456b5dd945e49a2cc11043d96fc4f100e9a7382388e0a306992cfb9e`; 1000 seed-cluster bootstrap replicates. |

## Regeneration path

The quantitative TMC material is regenerated with the repository analysis entry points rather than edited by hand:

- `python -m src.analyze --run results/combined`
- `python -m src.analyze_stress`
- `python -m src.analyze_recent --paper-assets`
- `python -m src.review_diagnostics --paper-assets`
- `python -m src.analyze_extensions --run results/data_driven_extension --paper-assets`
- `python -m src.analyze_reviewer_stress`
- `python -m src.paper_assets`

The TMC reviewer-stress workflow additionally reruns the full test suite before refreshing its evidence. Historical `latency_slots` values in older frozen CSV files were protocol sentinels rather than measurements and are excluded from the current analysis metric list.
