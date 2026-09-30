# IEEE TMC submission upload guide

Target journal: **IEEE Transactions on Mobile Computing**

This guide applies only to the tmc branch. The frozen Elsevier/PMC version is preserved on the pmc branch.

## Expected submission items

- Main manuscript PDF generated from main.tex.
- LaTeX source files for the main manuscript, including generated table/macro inputs and the system figure.
- supplement.pdf as a separate supplemental file.
- Source files for supplemental material if requested by the submission system.
- Author-reviewed cover letter text from COVER_LETTER_DRAFT.md.

Elsevier-specific Highlights and the PMC Editorial Manager ZIP are not TMC submission items.

## Before upload

Verify that:

- the manuscript is compiled with \\documentclass[10pt,journal,compsoc]{IEEEtran};
- the main manuscript does not exceed 18 formatted pages;
- the 12-page regular-paper baseline and possible overlength charges are understood if the paper remains longer than 12 pages;
- all references and figures resolve without LaTeX warnings;
- supplemental material is uploaded separately rather than appended to the main PDF;
- the author list and corresponding-author details are correct;
- the responsible authors have completed the declarations in AUTHOR_CONFIRMATION.md.

The tmc-build GitHub Actions workflow is the technical acceptance gate for this branch.
