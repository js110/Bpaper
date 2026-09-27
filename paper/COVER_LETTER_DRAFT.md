# Cover Letter Draft — Pervasive and Mobile Computing

Dear Editor,

Please consider our manuscript, **“Robust Branch-Safe Participation for Sequential Mobile Crowdsensing: Model Uncertainty and Disclosure Floors,”** for publication in *Pervasive and Mobile Computing*.

The manuscript studies a location-privacy problem that arises even when precise coordinates remain on a participant’s device: a linkable sequence of successful region-constrained sensing reports and silences can itself reveal location. We formalize this report/silence channel and develop Branch-Safe Participation (BSP), which computes the maximal scalar participation gate satisfying a posterior-concentration constraint on both observable branches under a declared Bayesian model.

The paper extends this mechanism in three directions. First, Robust BSP intersects the feasible gates of a finite ambiguity set and provides a maximal common scalar gate under model uncertainty. Second, a development/validation procedure constructs a replay ambiguity set from mobility and prior evidence rather than relying only on a hand-selected stress grid. Third, we identify an unavoidable disclosure floor for truthful positive reports: scalar thinning changes how often a successful report occurs but not its conditional location information. The resulting disclosure-floor-aware mechanisms expose a separate positive-report ceiling while keeping the silence branch at the original BSP cap, making the fine-region privacy–service trade-off explicit rather than hidden.

The evaluation includes synthetic mobility and a disjoint development/validation/test split of Microsoft GeoLife trajectories, informed-attacker and model-boundary stress tests, region-size-aware utility, and task-channel adaptations of recent optimization-based privacy mechanisms. The manuscript reports negative and boundary results alongside favorable ones; in particular, strict robust filtering can be highly conservative, and guarantees are explicitly limited to the declared observation channel and finite model set.

The topic falls directly within the journal’s scope in urban sensing and mobile crowdsensing, location-based services, and security and privacy in pervasive and mobile systems. We believe the work will be relevant to readers interested in privacy-aware mobile sensing, inference from repeated task interactions, and deployable privacy–utility controls.

A reproducible research repository contains the configurations, implementation, tests, event-level simulation records, analysis scripts, and manuscript sources used for the reported results.

Sincerely,

Lili He  
Sheng Jiang  
Linghui Lyu  
Lei Zhang (corresponding author)  
College of Information and Electronic Technology  
Jiamusi University

---

## Author checks before upload

The responsible authors should add or confirm any journal-required statements concerning originality/exclusive submission, conflicts of interest, author approval, ethics/data use, funding roles, and other declarations. This draft intentionally does not invent those statements.
