# Pervasive and Mobile Computing submission preparation

Current canonical branch: **main**.

## Template and package

- The manuscript uses Elsevier elsarticle with \documentclass[review,11pt,times]{elsarticle}.
- The target journal field is Pervasive and Mobile Computing.
- The main manuscript has six numbered sections: Introduction; Related Work; Proposed Branch-Safe Participation Framework; Privacy Guarantees and Robustness Analysis; Experimental Evaluation; Conclusion.
- Data and Code Availability and Funding are unnumbered.
- The flat Editorial Manager source archive contains no subfolders.
- highlights.txt is the editable source for highlights.docx.

## Final technical acceptance criteria

The final package is acceptable for upload only when `../research/manuscript_status.json` records all of the following for the current source SHA:

- `technical_ready=true` and `data_status.refresh_required=false`;
- all 31 automated tests pass;
- development manuscript, flat submission source, and supplement compile successfully;
- development and flat PDFs are text-equivalent and have the same recorded page count;
- the flat ZIP matches its manifest;
- no unresolved references, undefined control sequences, oversized floats, or overfull boxes are reported by the final quality gate;
- robustness remains explicitly limited to the declared finite model set;
- the GeoLife ambiguity-set/disclosure-floor extension remains explicitly post-hoc;
- DF-BSP/RDF-BSP retain the original BSP cap for silence and use a separate report-side threshold.

## Validation workflows

- code-tests.yml — automatic on main for source/test/config/dependency changes.
- data-driven-extension.yml — manual rerun of the data-driven ambiguity-set and DF/RDF extension.
- rbsp-validation.yml — manual rerun of the finite-model robust stress.
- rbsp-boundary.yml — manual rerun of the out-of-set boundary stress.
- pmc-final-package.yml — automatic on main manuscript-source changes and also manually dispatchable; performs final manuscript/package validation and artifact refresh.

## Author-owned items before submission

The responsible authors must confirm:

1. all-author approval of the final manuscript;
2. competing-interests wording;
3. CRediT roles if requested;
4. funder roles;
5. any GeoLife secondary-data ethics/data-use wording required by the journal or institution;
6. any journal disclosure requirements that are not part of the technical manuscript;
7. whether to cite a versioned GitHub release or immutable archive/DOI.

Author names/order/affiliation/corresponding details and the four grant names/numbers have already been copied from the supplied reference paper.
