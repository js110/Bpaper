# Independent mobile crowdsensing research
All work for this paper stays in this repository. No vehicular setting, infrastructure, or claims.
English manuscript; Chinese research notes. No hardware, paid compute, or automatic journal submission.
Never invent results, references, authorship, or declarations. Preserve null results and claim boundaries.
Attacks consume only public observations; private ground truth is evaluator-only.
Separate development/validation/test users or seeds. Re-run adaptive attacks for each defense.
Use real numerical algorithms and measured runtime; do not simulate cryptographic performance.
Read research/protocol.md and research/progress.md before continuing.

Core checks:
MPLCONFIGDIR=.cache/matplotlib python3 -m unittest discover -s tests -v
python3 -m src.audit
cd paper && latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex

For a fresh experiment run, use src.reproduce with a new output directory; do not overwrite frozen evidence in results/.

Reference policy: prefer recent work where appropriate, retain necessary original-method and dataset citations, and never alter publication metadata to satisfy an age window.

## CI / validation policy
- main is the canonical branch.
- code-tests.yml is the automatic source/config/test validation workflow on main.
- data-driven-extension.yml, rbsp-validation.yml, and rbsp-boundary.yml are manual experiment checkpoints.
- pmc-final-package.yml is the manual manuscript/package checkpoint and may refresh tracked final upload artifacts.
- Generated evidence or package commits must not recursively trigger the workflow that produced them.
