# IEEE Transactions on Mobile Computing submission checklist

Canonical working branch: **tmc**  
Frozen prior target: **pmc**

## Journal fit

- The title and abstract foreground a mobile-computing privacy problem rather than a generic Bayesian mechanism.
- The system model makes the mobile client, task region, public history, and linkable platform observation boundary explicit.
- Evaluation reports mobile-sensing service loss, model mismatch, adaptive probing, and deployment limitations.
- Claims remain limited to the declared report/silence channel and finite model set.

## Format

- Main class: \\documentclass[10pt,journal,compsoc]{IEEEtran}.
- IEEE Computer Society title/abstract/index-term structure is used.
- IEEE numeric reference style: IEEEtran.bst.
- Main paper target: 12 formatted pages where practical; submission ceiling: 18 pages.
- References and author biographies count toward the main-paper limit.
- Supplemental material is a separate file.
- Wide system figure and result tables use two-column floats when necessary.

## Technical acceptance

- Full automated test suite passes.
- main.tex compiles without unresolved references, undefined controls, overfull boxes, or oversized floats.
- supplement.tex compiles under the same quality gate.
- Main manuscript is <=18 formatted pages.
- Generated numeric macros and tables match the frozen evidence.
- GeoLife point estimates use effective-window weighting with complete state-path-group cluster bootstrap.
- Effective GeoLife split remains 23 development / 12 validation / 53 test windows after model-input-group isolation.
- Data-driven ambiguity set remains 2 selected models with 96.95% cumulative validation selection mass.
- Robustness is not generalized beyond the declared finite model set.
- DF-BSP/RDF-BSP relax only the report-side ceiling; silence retains the strict BSP constraint.

## Author-owned items

Before submission, the responsible authors must confirm:

1. all-author approval of the TMC manuscript;
2. originality/exclusive-submission statement;
3. conflicts of interest;
4. author order, affiliation, and corresponding-author details;
5. funding roles and acknowledgments;
6. any required GeoLife secondary-data/ethics wording;
7. CRediT or other contribution metadata if requested;
8. ORCID identifiers for all authors, as required by IEEE journals for peer-review submission;\n9. any IEEE disclosure requirements that are not technical manuscript content.
