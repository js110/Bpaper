# Pervasive and Mobile Computing submission preparation

Prepared on 2026-09-26 for branch `submission/pmc-2026-09-26`.

## Template and file format

- The manuscript uses Elsevier's official `elsarticle` class.
- The review branch uses `\documentclass[review,12pt]{elsarticle}`.
- The journal field is set to `Pervasive and Mobile Computing`.
- The author-facing "Draft status" paragraph was removed from the submission copy.
- Keep all LaTeX submission files at one folder level when packaging for Editorial Manager; Elsevier's current LaTeX instructions state that subfolders are not supported by its processing workflow.
- A separate `highlights.txt` file has been added. Elsevier's general highlights guidance specifies 3--5 bullets, no more than 85 characters each. Journal-specific requirements still need a final check in the live Guide for Authors.

## Items that must be author-confirmed before submission

Do not invent any of the following. The responsible authors must confirm them:

1. final author order and spelling;
2. affiliation and corresponding-author details;
3. all grant names and numbers;
4. declaration of competing interests;
5. CRediT author contributions, if requested;
6. funders' roles;
7. data-use / ethics determination for the secondary GeoLife data;
8. final generative-AI disclosure wording under the journal's current policy;
9. whether the repository will remain a working GitHub repository or be archived in an immutable release.

## Scientific items that remain more important than formatting

- Robustness to attacker/model mismatch;
- independent parameter selection instead of test-set policy-envelope selection;
- practical utility for small-region tasks;
- a stronger novelty statement relative to inference-resistant MCS task-allocation work.

The paper should not be marked submission-ready until these points are resolved or explicitly bounded in the claims.
