# IEEE TMC manuscript source

This branch targets *IEEE Transactions on Mobile Computing* and uses the IEEE Computer Society journal layout:

    \\documentclass[10pt,journal,compsoc]{IEEEtran}

Development build:

    latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex

The main manuscript is intentionally kept separate from supplement.tex. IEEE Computer Society supplemental material is submitted as a separate file and does not count toward the main-paper page limit.

## TMC length policy used by this branch

- Regular-paper baseline: 12 formatted double-column pages, including references and any author biographies.
- Maximum regular-paper submission length: 18 formatted pages.
- The branch build fails above 18 pages and emits a warning above 12 pages.
- Supplemental material is separate and not counted in the main manuscript page limit.

## Scientific organization

The TMC version keeps six top-level sections:

1. Introduction
2. Related Work
3. System Model and Branch-Safe Participation
4. Robustness and Disclosure-Floor Analysis
5. Evaluation
6. Conclusion

The mobile-computing problem and observation boundary are made explicit early in the paper. Core mechanism definitions and guarantees stay in the main paper; comparator derivations, finite-model stress details, ambiguity-set construction details, and reproducibility material remain in the supplement unless page pressure requires further movement.

## Validation

.github/workflows/tmc-build.yml runs on pushes to the tmc branch. It:

- runs the full Python test suite;
- installs the IEEE LaTeX publishers package;
- compiles the main TMC manuscript and supplemental material;
- rejects unresolved references, undefined commands, oversized/overfull layout problems, and an 18-page main-paper overflow;
- packages a preview ZIP as a workflow artifact.

The canonical scientific evidence remains the same model-input-isolated, window-weighted analysis used by the final PMC checkpoint. TMC conversion changes presentation and journal framing, not the underlying experimental record.

Working repository: https://github.com/js110/Bpaper
