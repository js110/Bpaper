# Target journal decision (2026-09-25)

## Primary target: Pervasive and Mobile Computing (PMC)

Primary target selected: **Pervasive and Mobile Computing** (Elsevier, ISSN 1574-1192).

Reason for selection: the journal's current official scope explicitly includes **Urban Sensing and Mobile Crowdsensing**, **Positioning, Localization and Tracking Technologies**, **Location-based Services and Applications**, and **Trust, Reliability, Security, and Privacy in Pervasive and Mobile Computing Systems**. This manuscript studies sequential location inference from linkable mobile-crowdsensing task outcomes and a client-side participation mechanism, so the topic is directly aligned with the journal's stated scope.

Official scope:
https://shop.elsevier.com/journals/pervasive-and-mobile-computing/1574-1192

Recent topical evidence includes privacy-preserving mobile-crowdsensing articles published by PMC, e.g.:
- Montori and Bedogni, "Privacy preservation for spatio-temporal data in Mobile Crowdsensing scenarios", Pervasive and Mobile Computing 90 (2023), 101755.
- Andola and Yadav, "A blockchain-assisted privacy-preserving framework for Mobile CrowdSensing", Pervasive and Mobile Computing 115 (2026), 102125.

This is a scope decision, not a claim about acceptance probability.

## Backup venues

1. **Journal of Information Security and Applications (JISA)** — strong privacy/security fit and has published mobile-crowdsensing privacy work, but the manuscript would need to foreground the threat model, security guarantee, and robustness more strongly.
   Official scope: https://shop.elsevier.com/journals/journal-of-information-security-and-applications/2214-2126

2. **Computer Communications** — acceptable backup if the manuscript is repositioned toward mobile/ubiquitous network services and system simulation; current contribution is less communication-protocol-centric.
   Official scope: https://shop.elsevier.com/journals/computer-communications/0140-3664

## LaTeX and submission format

Elsevier's current LaTeX instructions recommend the official `elsarticle` class. The working manuscript already uses `elsarticle`; the submission-preparation branch changes the journal declaration to `Pervasive and Mobile Computing` and restores the standard Elsevier first-page behavior.

Official LaTeX instructions:
https://www.elsevier.com/researcher/author/policies-and-guidelines/latex-instructions

Elsevier states that Editorial Manager does not process LaTeX source bundles with subfolders. The repository build helper `src/package_paper.py` therefore creates a **flat** `manuscript_source.zip` and rewrites the two conceptual figure paths inside the archived `main.tex`. AI-generation provenance is packaged separately so it does not break the manuscript-source layout.

The journal-specific ScienceDirect Guide for Authors returned HTTP 403 during this check, so journal-specific details that are not visible from the official public pages must still be verified manually in the submission portal before final submission.

## Current submission status

The manuscript is **not yet scientifically submission-ready** solely because the template is correct. The main unresolved items are:

- the robustness gap exposed by the better-informed attacker;
- weak/approximate prior assumptions in the replay attack;
- test-selected exploratory policy envelopes;
- utility dominated by large-region tasks;
- only 11 references for a 20+ page paper;
- final author verification of declarations and the exact generative-AI disclosure.

See `research/reviews/reviewer_report_2026-09-25.md` and `paper/PMC_SUBMISSION_CHECKLIST.md`.
