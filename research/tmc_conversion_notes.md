# IEEE TMC conversion notes (2026-09-30)

Target: IEEE Transactions on Mobile Computing (TMC).

## Current official constraints checked before editing

- Scope: mobile-computing architectures, support services, algorithm/protocol design and analysis, mobile environments (including security), and location-dependent/pervasive/sensor-network applications.
- TMC's current scope guidance emphasizes a clear mobile-computing problem, system-level implications, deployability/overhead/robustness analysis, and an explicit mobile-systems take-home message.
- IEEE Computer Society journal submissions must use an IEEE article template.
- Computer Society Transactions use a 12-formatted-page regular-paper baseline; TMC author guidance permits regular-paper submissions up to 18 double-column pages, with overlength charges applying beyond the regular limit after final layout.
- References and author biographies count toward the main-paper page limit.
- Supplemental material is uploaded separately and is not included in the main-paper page count.
- Computer Society double-anonymous review is optional by request rather than the default; this branch therefore retains the author byline unless the authors explicitly choose the double-anonymous option at submission.
- IEEE journal supplementary material should be submitted as separate files.

Official/reference pages checked:
- https://www.computer.org/digital-library/journals/tm/cfp-ieee-transactions-mobile-computing
- https://www.computer.org/publications/author-resources
- https://journals.ieeeauthorcenter.ieee.org/create-your-ieee-journal-article/authoring-tools-and-templates/tools-for-ieee-authors/ieee-article-templates/
- https://journals.ieeeauthorcenter.ieee.org/create-your-ieee-journal-article/prepare-supplementary-materials/

## Style observations from recent TMC work

Recent TMC mobile-crowdsensing/mobile-privacy papers generally make the mobile-computing problem explicit in the title and first paragraphs, then move through system/problem formulation, mechanism/algorithm design, theoretical properties, and evaluation. Real mobility/sensing data, system implications, robustness/overhead, and limitations are made visible rather than left as supplementary narrative.

Examples inspected:
- C-PRISM: TMC 2026, DOI 10.1109/TMC.2026.3665505.
- Marginal Effect-Driven Participant Selection With Local Differential Privacy for Mobile Crowdsensing: TMC 2026, DOI 10.1109/TMC.2026.3676248.
- Crowdsensing From a Distance: A Contract Mechanism Design: TMC Early Access 2026, DOI 10.1109/TMC.2026.3725722.
- Rethinking the Effect of Sparse Data Completion on Sparse Mobile Crowdsensing Tasks: TMC 2025, DOI 10.1109/TMC.2025.3531362.

## Conversion decisions for this branch

- Use the IEEE Computer Society journal class: `\\documentclass[10pt,journal,compsoc]{IEEEtran}`.
- Keep six top-level scientific sections, but retitle them for TMC:
  1. Introduction
  2. Related Work
  3. System Model and Branch-Safe Participation
  4. Robustness and Disclosure-Floor Analysis
  5. Evaluation
  6. Conclusion
- Make the system/observation model and mobile-computing implications more prominent.
- Keep theorem statements and core proofs in the main paper initially; move nonessential derivations/validation details to the separate supplement only if the IEEE-formatted manuscript exceeds the 18-page submission ceiling.
- Use a two-column-wide system figure and two-column-wide result tables where needed.
- Use IEEE numeric references via `IEEEtran.bst`.
- Remove Elsevier-only front matter, highlights, and PMC package language from the TMC submission materials.
