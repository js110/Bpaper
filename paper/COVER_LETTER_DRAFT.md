# Cover Letter Draft — IEEE Transactions on Mobile Computing

Dear Editor-in-Chief,

Please consider our manuscript, **“Branch-Safe Participation for Location Privacy in Sequential Mobile Crowdsensing,”** for publication in *IEEE Transactions on Mobile Computing*.

The manuscript studies a mobile-computing privacy problem that remains even when precise coordinates never leave a participant’s device. In region-constrained mobile crowdsensing, a linkable successful report certifies that the participant was eligible in the task region, while silence can also update the platform’s belief once delivery, willingness, timely completion, and privacy filtering are taken into account. Repeated task outcomes therefore create a sequential inference channel at the mobile sensing interface.

We develop Branch-Safe Participation (BSP), a client-side online gate that maximizes participation while bounding posterior location concentration after every observable report or silence branch under an explicit mobility and completion model. We then extend the mechanism to finite model sets through Robust BSP, characterize an unavoidable disclosure floor for truthful positive reports, and introduce disclosure-floor-aware variants that separate the report-side floor from the strict silence constraint.

The evaluation combines synthetic mobility with a model-input-group-isolated Microsoft GeoLife replay, informed model-mismatch attacks, outside-set boundary cases, adaptive probes, region-size-aware service metrics, and task-channel adaptations of recent privacy mechanisms. The results show both the benefit and the cost of robust filtering: strict finite-model protection substantially reduces model-mismatch violations but can sharply reduce service for fine-grained tasks, while an explicit report-side ceiling restores service only by making that relaxation visible.

The work is aligned with TMC’s focus on mobile environments, security, online algorithm/protocol design, and location-dependent mobile applications. Its central contribution is not a generic privacy metric but an online participation mechanism for a concrete mobile sensing interaction: the report/silence sequence observed by a linkable platform.

The repository contains the implementation, deterministic preprocessing, frozen configurations, tests, analysis scripts, and processed evidence supporting the reported results.

Sincerely,

Lili He  
Sheng Jiang  
Linghui Lyu  
Lei Zhang (corresponding author)  
College of Information and Electronic Technology  
Jiamusi University

---

## Author checks before upload

The responsible authors should confirm the final author list and approval, originality/exclusive submission, conflicts of interest, funding roles, any required GeoLife secondary-data wording, and any other IEEE/TMC declarations requested by the submission system. This draft intentionally does not invent author-owned declarations.
