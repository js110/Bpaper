# TMC-style major-revision response record — 2026-09-30

Review target: tmc branch commit 5997f5b952a3eb8fb2a9319d342cba71bdc089fa

## 1. Novelty and related-work positioning

Actions:
- Corrected the TMarkov description: it predicts a mobility-aware surrogate trajectory for crowdsourcing participation; it is not categorized as acceptance/refusal inference.
- Added privacy-preserving task-allocation/matching context, including anonymous task matching, and a mechanism-level comparison across TMarkov, iTAM/task matching, HECTA, Bayesian privacy, PRIVIC, and BSP/R-BSP.
- The comparison distinguishes visible transcript, truthful-report semantics, trust assumptions, model dependence, privacy object, service semantics, and online control.
- Reframed novelty as closed-form online control of a visible, truthful, linkable report/silence channel rather than a new generic Bayesian privacy metric or a replacement for private task allocation.
- PML-T, PRIVIC-T, and the KL adaptation are explicitly treated as exploratory task-channel diagnostics; their source-method guarantees are not transferred to the adapted channel.

## 2. Scope of claims and stronger stresses

Actions:
- Abstract, evaluation, and conclusion now state the independent Bernoulli baseline task-process assumption, finite-model-set scope, finite task library, and one-step greedy main probe.
- “Utility/service rate” language is narrowed to simulated eligible-and-available opportunity retention under the declared protocol.
- Retained the outside-set alpha=0.98 boundary failure (6.93% local-cap violations) to make the finite-model boundary explicit.
- Added grid-resolution sensitivity for 4x4 and 16x16 settings and explicitly state that the 8x8 operating point is not resolution invariant.
- Added a spatially varying availability stress: the true/attacker availability is 0.35 on one half of the grid and 0.85 on the other while the client remains calibrated to scalar alpha=0.648.
- Added a nonstationary mobility stress alternating movement probability 0.05 and 0.8 every eight slots while the client remains calibrated to stationary 0.3.
- Added an all-probe two-step beam look-ahead heuristic and compare it with the one-step mutual-information greedy rule. This broadens planning sensitivity but is not claimed to be an optimal long-horizon adversary.
- The text explicitly states that coordinated accounts, personalized auxiliary priors, arbitrary distribution shift, and optimal long-horizon probing remain outside the evidence.

## 3. Exploratory baseline comparisons

Actions:
- Abstract, evaluation, and conclusion label the recent-comparator envelope results and GeoLife data-driven/disclosure-floor extensions as exploratory rather than confirmatory superiority tests.
- The manuscript states that evaluation-set policy-envelope selection is post-hoc and does not constitute an independently tuned comparison.
- GeoLife is described as a source of mobility traces, not task-delivery, willingness, deadline, energy, latency, or production service logs.

## 4. Mobile-device/deployment claims

Actions:
- Deployment language is limited to protocol/design placement between local eligibility and upload.
- The manuscript explicitly states that production-platform compatibility has not been demonstrated.
- Smartphone CPU/RAM/energy, end-to-end latency, network/deadline behavior, and production completion rates are not claimed as measured evidence.
- Python gate timing remains implementation profiling only and is not presented as a portable mobile benchmark.

## 5. Code semantics and reproducibility

Actions:
- Removed the synthetic latency_slots=1.0 result field from current experiment outputs/analysis.
- Fixed reset_every so client and attacker beliefs restore their own background priors; regression tests cover distinct priors.
- Extended the simulator to support state-dependent attacker/true availability for the reviewer stress and scheduled nonstationary movement.
- Added deterministic two-step probe-planning stress code and tests.
- Added a dedicated reviewer-stress configuration, frozen outputs, analysis summary, and provenance record.
- TMC package generation emits TMC_evidence_traceability.json with the source-head SHA and SHA-256 hashes for key configs, frozen summaries, and manuscript number/table inputs.
- research/tmc_evidence_map.md maps manuscript evidence to frozen result directories and provenance.

## Remaining evidence boundary

The revised manuscript still does not claim protection against arbitrary out-of-set models, an optimal long-horizon adversary, coordinated multi-account probing, personalized auxiliary information, or unmodeled observation channels. It also does not claim smartphone energy/latency measurements, production MCS task logs, or confirmatory superiority over recent baselines.
