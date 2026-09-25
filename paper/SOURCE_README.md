# Pervasive and Mobile Computing submission source

Primary target: **Pervasive and Mobile Computing (Elsevier)**.

The repository manuscript uses Elsevier's official `elsarticle` class. Build the working manuscript with:

    latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex

For Editorial Manager packaging, run from the repository root:

    python -m src.package_paper

This creates:

- `paper/manuscript_source.zip`: a flat LaTeX source bundle. The packaging script rewrites the two conceptual image paths so no subfolder is required inside the submission archive.
- `paper/ai_provenance.zip`: prompt/provenance records for the AI-generated conceptual schematics, kept separate from the manuscript source.

Elsevier's current LaTeX instructions state that LaTeX submissions containing subfolders cannot be processed by Editorial Manager, which is why the submission archive is flattened.

The manuscript contains executed experiments, reproducible analyses, and archived negative results. Formatting for PMC does not by itself make the paper submission-ready. Before submission, complete the scientific and disclosure checks in `PMC_SUBMISSION_CHECKLIST.md`, especially the robust-attacker issue, test-set tuning issue, author declarations, and exact generative-AI disclosure.

Working repository: https://github.com/js110/Bpaper
