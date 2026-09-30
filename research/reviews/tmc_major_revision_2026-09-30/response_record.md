# TMC-style major-revision response record — 2026-09-30

Review target: tmc branch commit 5997f5b952a3eb8fb2a9319d342cba71bdc089fa

## 1. Novelty and related-work positioning

Actions:
- Corrected the TMarkov description: it predicts a surrogate mobility trajectory for crowdsourcing participation; it is not categorized as acceptance/refusal inference.
- Added Anonymous Privacy-Preserving Task Matching in Crowdsourcing (IEEE IoT Journal 2018, DOI 10.1109/JIOT.2018.2830784).
- Added a mechanism-level comparison across TMarkov, privacy-preserving task matching/iTAM, HECTA, Bayesian privacy, and BSP/R-BSP. The table distinguishes visible transcript, truthful-report semantics, trust assumptions, prior/model dependence, privacy objective, and online cost.
- Reframed novelty as online control of a visible, truthful, linkable report/silence channel rather than a new generic privacy metric.
- Reclassified PML-T/PRIVIC-T and the KL adaptation as exploratory task-channel diagnostics whose adapters do not inherit the original application guarantees.

## 2. Scope of claims and attack model

Actions:
- Abstract and conclusion now state the independent Bernoulli task-process assumption, finite model-set scope, finite task library, one-step greedy probe, and exploratory status of the GeoLife/post-hoc comparator analyses.
- “Utility/service rate” language is narrowed to simulated completable-opportunity retention under the declared task-process model.
- Added grid-resolution sensitivity evidence from the frozen synthetic sensitivity suite (4x4 and 16x16 endpoints) and explicitly state that the nominal 8x8 result is not grid invariant.
- Retained and foregrounded the outside-set alpha=0.98 failure (6.93% local-cap violation).
- Explicitly state that location-dependent availability, non-stationary task processes, long-horizon task design, coordinated accounts, and personalized priors remain untested.

## 3. Exploratory baseline comparisons

Actions:
- Abstract, evaluation, and conclusion now label recent-comparator envelope results and GeoLife disclosure-floor/data-driven extensions as exploratory, not confirmatory superiority tests.
- Main text explicitly states that PML-T and PRIVIC-T alter output semantics and therefore support only channel diagnostics.

## 4. Mobile-device/deployment claims

Actions:
- Deployment language is changed from compatibility claims to design-level placement in the eligibility-to-upload path.
- Smartphone energy, end-to-end latency, network behavior, and production task completion are explicitly excluded from evidence.
- Complexity claims remain analytical only.

## 5. Code semantics and reproducibility

Actions:
- Removed the synthetic `latency_slots=1.0` result field from new runs and from analysis metrics.
- Fixed `reset_every` so client and attacker beliefs reset to their own configured background priors; added a regression test for distinct priors.
- TMC package generation now emits `TMC_evidence_traceability.json` with the source SHA and SHA-256 hashes for key configs, decontamination metadata, frozen analysis summaries, and manuscript number/table inputs.

## Remaining evidence boundary

No new claim is made for location-dependent availability, non-stationary adversaries, optimal long-horizon probing, smartphone energy/latency, production MCS logs, or confirmatory recent-baseline superiority. Those remain explicit limitations rather than being inferred from the existing simulation record.
