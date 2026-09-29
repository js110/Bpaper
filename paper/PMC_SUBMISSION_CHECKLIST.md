# Pervasive and Mobile Computing submission preparation

Current canonical branch: **main**.

## Template and package

- The manuscript uses Elsevier elsarticle with \documentclass[review,11pt,times]{elsarticle}.
- The target journal field is Pervasive and Mobile Computing.
- The main manuscript has six numbered sections: Introduction; Related Work; Proposed Branch-Safe Participation Framework; Privacy Guarantees and Robustness Analysis; Experimental Evaluation; Conclusion.
- Data and Code Availability and Funding are unnumbered.
- The flat Editorial Manager source archive contains no subfolders.
- highlights.txt is the editable source for highlights.docx.

## Current technical state

- Main manuscript: 28 pages.
- Flat source rebuild: 28 pages and text-equivalent to the development build.
- Supplement: 11 pages.
- References: 21 cited entries.
- Automated tests: 28.
- No final unresolved references, undefined control sequences, oversized floats, or overfull boxes.
- Robustness is explicitly limited to the declared finite model set.
- The GeoLife ambiguity-set/disclosure-floor extension is explicitly post-hoc.
- DF-BSP/RDF-BSP use a report-side threshold; the original BSP local cap remains the reference strict contract and silence is not relaxed.

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
