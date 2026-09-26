# Manuscript source bundle

This is a complete research draft, not an approved submission.
Build with a TeX Live installation containing common LaTeX mathematics, graphics, font, and bibliography packages:

    latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex

The included elsarticle class and bibliography style originate from Elsevier's official template. The generated figures and tables correspond to the saved project results. Full code, experiment logs, provenance, source audit, and reproduction instructions are in the parent crowdsensing_task_privacy project. Author, affiliation, and funding text was supplied for this draft and still requires author verification; other declarations and final venue checks remain pending.

Updated 2026-09-26 after the finite-model R-BSP extension: the PMC review-layout manuscript compiles to 47 pages with 11 references, eight figures and seven tables. The complete unit-test suite now has 23 tests. A post-hoc 40-condition / 3,200-trajectory synthetic stress test is stored under `results/robust_informed/`; it was motivated by previously observed model-mismatch failures and is explicitly not described as confirmatory. The nine-model R-BSP set contains the informed attacker's generating model in that stress, eliminating observed local-cap violations at the cost of lower opportunity retention and roughly an order-of-magnitude larger Python gate time. The two PNG schematics remain image-model-generated conceptual figures; quantitative plots and tables derive from archived experiment logs. The closest 2026 task-allocation paper remains a model-level comparison, not a numerical reproduction or independent novelty certification.

Working repository: https://github.com/js110/Bpaper . The latest factual audit corrects implementation-validation wording, PML bound attainment, KL gate approximation, tie handling, and official PMLR author metadata without changing saved experimental results.
