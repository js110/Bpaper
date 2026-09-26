# Independent mobile crowdsensing research
All work for this paper stays in this directory. No vehicular setting, infrastructure, or claims.
English manuscript; Chinese research notes. No hardware, paid compute, or automatic submission.
Never invent results, references, authorship, or declarations. Preserve null results and failures.
Attacks consume only public observations; private ground truth is evaluator-only.
Separate development and test users/seeds. Re-run adaptive attacks for each defense.
Use real numerical algorithms and measured runtime; no simulated cryptographic performance.
Read research/protocol.md and research/progress.md before continuing.
Commands: MPLCONFIGDIR=.cache/matplotlib python3 -m unittest discover -s tests -v;
python3 -m src.experiment --config configs/pilot.json;
python3 -m src.analyze --run results/final;
cd paper && latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex.

Reference policy (2026-09-17): Prefer publications from 2022--2026; comparison baselines must be published in 2024--2026. Older citations require a concrete necessity recorded in research/reference_policy.md. Do not change publication years to meet the window. Retain attribution for original methods used and citations requested by the dataset provider.


## CI / validation policy (2026-09-26)
- `.github/workflows/code-tests.yml` is the only automatic code-validation path; it is limited to source, tests, configs, and dependency files and cancels superseded runs.
- R-BSP experiment reruns are checkpoint actions, not per-commit CI. `rbsp-validation.yml` is manual; the boundary stress uses only the explicit `research/.run-rbsp-boundary` sentinel.
- Manuscript compilation is checkpoint-only. `paper-build.yml` runs manually or when `paper/.build-request` is changed; editing `paper/main.tex` alone must not install TeX or launch a build.
- Generated result/PDF commits must not recursively retrigger the workflow that produced them.
- Do not combine full experiments and LaTeX installation in one job again.
