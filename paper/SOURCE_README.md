# Manuscript source bundle

This is a complete research draft, not an approved submission.
Build with a TeX Live installation containing common LaTeX mathematics, graphics, font, and bibliography packages:

    latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex

The included elsarticle class and bibliography style originate from Elsevier's official template. The generated figures and tables correspond to the saved project results. Full code, experiment logs, provenance, source audit, and reproduction instructions are in the parent crowdsensing_task_privacy project. Author, affiliation, and funding text was supplied for this draft and still requires author verification; other declarations and final venue checks remain pending.

Updated 2026-09-23 after internal review and author details: 21 pages, 11 references, eight figures and six tables. The two PNG schematics were created with the built-in image generation tool; their prompts and provenance are included under imagegen/. Quantitative plots and the added task-area, prior-predictor, and expanded Commute displays derive from archived experiment data. The 2024 PML and PRIVIC comparisons are explicitly task-channel adaptations. The source uses the xurl package to wrap long reference URLs. The closest 2026 task-allocation paper has now been compared using the user-supplied accepted author version. This is a model-level comparison, not a numerical reproduction or an independent novelty certification.

Working repository: https://github.com/js110/Bpaper . The latest factual audit corrects implementation-validation wording, PML bound attainment, KL gate approximation, tie handling, and official PMLR author metadata without changing saved experimental results.
