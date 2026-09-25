# 内部审稿意见（目标期刊：Pervasive and Mobile Computing）

日期：2026-09-25  
稿件：*Truthful Reports and Informative Silence: A Bayesian Participation Filter for Sequential Mobile Crowdsensing*

## 总体判断

这篇稿件已经不是“缺少基本实验或复现材料”的早期草稿。现有代码、实验日志、GeoLife 回放、近期基线、负结果和复现记录比较完整。当前最主要的录用风险不在工程完整性，而在 **创新性是否足够、隐私保证对攻击者知识的脆弱性、以及效用评价是否真正代表移动群智感知任务价值**。

以当前版本直接投稿，最可能遭遇的核心审稿意见是：BSP 的闭式标量 gate 虽然推导清楚，但属于一个较窄的、模型条件化的 Bayesian posterior filter；而“任务接受/拒绝或任务输出会泄露位置”本身已有直接前例。稿件自己又通过 informed-attacker 实验表明，一旦攻击者比客户端掌握更准确的模型，客户端的 posterior cap 就不再约束该攻击者。因此，这个问题不能只放在 Limitations 中，需要反过来成为方法扩展的核心。

建议在投稿前完成一次实质性 Major Revision，而不是只改版式。

---

## Major concerns

### M1. 当前创新边界仍然偏窄

论文已经正确承认：任务接受/拒绝序列与移动相关性可用于位置推断并非新问题；Bayesian privacy、后验约束、位置扰动机制也不是新概念。当前最有辨识度的技术点是：

1. 把“真实完成”和“概率性沉默”写成一个明确的二元可观测信道；
2. 同时检查正、负两个 posterior branch；
3. 在“公共历史决定的标量 gate”这一受限策略族内推导最大可行参与概率。

问题是，审稿人可能把第 3 点看成一个较简单的一维约束求交，而不是足够支撑 20+ 页期刊论文的核心方法创新。

**建议：不要把创新重点放在“发现任务输出泄漏”或“第一次考虑 silence”。应把主线升级为“在不确定攻击者知识下，对 truthful task-output channel 的鲁棒参与控制”。**

### M2. informed-attacker 结果实际上击中了当前方法的核心保证

稿件现有 stress test 已经显示：当客户端和攻击者对 availability 或 mobility 的认知不同，更知情攻击者的 posterior peak 可以明显超过客户端设定的 0.1 cap。现有结果中，在特定失配条件下约 30.0% 或 41.4% 的评估时隙超过阈值，最大 posterior peak 可达到约 0.246 或 0.263。

这不是一般意义上的“小局限”，而是直接说明当前保证只对单一声明模型成立。对于隐私论文，审稿人很容易追问：

- 客户端凭什么知道攻击者的 prior？
- 攻击者是否可以利用人口统计、home/work 规律、历史网络记录或更准确的 mobility model？
- 如果真实攻击者不在声明模型中，ρ 到底还能解释为什么？

**这应当成为下一版方法扩展的第一优先级。**

### M3. replay 场景中的 uniform prior 太弱

稿件已经做了一个重要诊断：仅使用 development 数据拟合的无输出 modal-cell predictor，在 test users 上达到约 25.75% 命中率，而原始 uniform-prior BSP attack 的命中率只有约 2%–3%。

这意味着当前 replay 主攻击模型严重低估了“什么都没看到之前”攻击者已经知道的信息。审稿人可能据此质疑主结果中的绝对 hit rate。

建议至少新增：

- development-fitted population prior；
- 若数据允许，再加入 user-history-derived prior 或 time-of-day prior；
- 在这些 prior 下重新运行 fixed/adaptive attack，而不是只把 25.75% 当作旁路诊断。

最终应报告 **incremental leakage over a realistic prior**，而不是只报告 uniform-prior 下的绝对 accuracy。

### M4. 当前 utility 指标对大区域任务明显有利

在 BSP (ho=0.1) 的代表性结果中，绝大多数完成任务来自覆盖至少 32/64 cells 的大区域任务，1–8-cell 任务完全没有被完成；同时 raw completion 对全部 normal tasks 只有约 5% 左右。

这会让审稿人提出一个很合理的问题：所谓“保留约一半机会”是否主要因为 denominator 已经筛掉了用户不在区域/不可用的任务，并且保留下来的又主要是大区域任务？

建议补至少两类 utility：

1. **task-size-stratified utility**：分别报告 1–8、9–31、32–64 cells 的服务率；
2. **value-weighted utility**：对精细区域任务赋予更高信息价值，或者使用 coverage / reconstruction quality，而不是所有 completion 都按 1 计数。

如果 R-BSP 会进一步降低 retention，更需要这组分析说明它牺牲了什么。

### M5. PML-T 和 PRIVIC-T 是“适配后的 comparator”，不是直接 SOTA 系统对比

当前写法已经比较谨慎，但投稿时仍要避免任何“全面优于最新方法”的措辞。PML-T 和 PRIVIC-T 都改变了原论文接口或效用语义，尤其 PRIVIC-T 的 true-eligibility check 使原始 geo-indistinguishability 保证不能直接迁移。

HECTA 又采用了 dummy tasks、加密和非串通辅助方，观测边界不同。

因此建议把近期方法对比定位为：

- **constraint/objective comparators on the same truthful-output channel**；
- 而不是“系统级 SOTA head-to-head”。

这样更科学，也更不容易被原作者型审稿人抓住。

### M6. test-selected envelope 会削弱统计结论

当前后续 thinning grid 和 lower-envelope 选择使用过 test results，稿件也如实说明这是 exploratory analysis。问题在于，如果表格里仍给出 confidence interval，审稿人会质疑这是“在测试集上调参以后再对同一测试集做推断”。

建议修复为：

- validation set 负责参数/候选策略选择；
- test set 只运行最终冻结策略一次；
- 或者采用 nested resampling / cross-fitting，明确把 selection uncertainty 纳入。

这是投稿前应该修掉的实验设计问题，不建议继续只靠文字 disclaimer。

### M7. 实际场景的抽象仍较强

当前实验是约 4 km cell、每用户 48 分钟、GeoLife 历史轨迹、模拟 task/delivery/willingness/deadline；没有 measurement content、network metadata、真实 payment/ack、真实任务日志，也没有手机功耗/延迟实验。

如果论文继续定位为 **analytical privacy mechanism paper**，这些并非致命问题，但相应地理论贡献必须更强。若方法仍只是单模型 scalar gate，审稿人就会同时觉得“理论不够强 + 系统又不够真实”。

因此最经济的路线不是硬凑一个手机 demo，而是增强模型与鲁棒性理论，并把实验升级为强攻击模型下的验证。

### M8. 11 条参考文献对于当前稿件明显偏少

20+ 页期刊论文只有 11 条参考文献，会给人一种相关工作覆盖不足的直接印象，尤其主题横跨：

- mobile crowdsensing privacy；
- task acceptance / task-allocation inference；
- Bayesian / posterior privacy；
- geo-indistinguishability；
- Pufferfish / prior-robust privacy；
- sequential/adaptive privacy；
- trajectory privacy；
- uncertainty / robust optimization。

建议补到约 25–40 条真正相关的一手文献，而不是填充引用。优先补近五年直接工作，同时保留少量必要的基础文献。

### M9. sequential guarantee 需要从“正确单模型”提升到“模型集合”

当前 corollary 的解释对 transition/model correctness 依赖很强。建议把下一版 theorem 写成：

> 对一个公开定义的候选模型集合 𝓜，只要真实攻击者模型属于 𝓜，且每个候选模型的 transition 满足相应预测条件，则同一个公开 gate 对集合内所有模型的两个输出分支同时满足 posterior concentration constraint。

这比把 model mismatch 作为 limitation 更能形成方法学贡献。

### M10. 投稿声明仍需要作者最终人工确认

Elsevier 当前政策要求对实质性 generative-AI manuscript preparation 做明确声明；AI 生成/编辑的图像还需要在图注和声明中按要求披露。仓库已经保存 prompt/provenance，这很好，但不能由自动化流程臆造工具版本、作者贡献、利益冲突、伦理适用性或 funder role。

这些必须在投稿前由作者确认后再写入最终稿件。

---

# 建议的核心新方法：Model-Set Robust BSP（R-BSP）

这是当前最值得做的扩展，因为它正面解决论文已经发现的 informed-attacker failure。

设候选攻击者模型集合为 𝓜 = {M₁, …, M_K}。模型 M_k 在当前任务前给出 belief b^(k)，并允许具有不同的 availability / completion likelihood h_i^(k)。定义：

- m_k = Σ_i b_i^(k) h_i^(k)
- c_k = max{ρ, ||b^(k)||∞}

所有模型共享同一个公开 gate probability q。要求对于每一个 M_k，report 和 silence 两个正概率分支的 posterior peak 都不超过 c_k。

如果任意候选模型的正报告 posterior 已满足

max_i [ b_i^(k) h_i^(k) / m_k ] > c_k,

那么只要 q > 0，正报告分支就无法满足该模型的约束，因此 robust gate 必须取 q* = 0。

否则，对每个候选模型和状态定义

d_(k,i) = c_k m_k - b_i^(k) h_i^(k).

同一个 gate 的最大鲁棒可行值为

q*_R = min { 1, min_k min_(i : d_(k,i) > 0) [ (c_k - b_i^(k)) / d_(k,i) ] }.

也就是说，R-BSP 是所有候选模型可行 gate 区间的交集。计算复杂度从单模型 O(N) 增加到 O(KN)，对目前 64-cell 规模仍然很轻。

需要谨慎定位：**多 prior / 多攻击者知识的保护思想本身并不是首次出现**，Pufferfish privacy 及 robust local-privacy 文献已经研究过 attacker belief uncertainty。这里可以主张的创新应当是：

> 针对 linkable truthful-completion / probabilistic-silence 的 mobile-crowdsensing channel，给出一个可计算的多模型双分支 robust participation gate、相应 sequential condition，以及对 privacy–utility–robustness 成本的系统实验。

这比宣称“首次提出 prior-robust privacy”稳妥得多。

## 建议新增的 R-BSP 实验

- **Model-set sweep**：让客户端同时防守多个 α、move probability、population prior 组合，画出 K 或 uncertainty radius 增大时的 retention–worst-case posterior frontier。
- **Informed attacker rerun**：用现有 informed.json 中的真实攻击者设置，比较 BSP 与 R-BSP 的 cap violation rate、maximum posterior peak、MAP hit rate、retention。
- **Nonuniform prior adaptive attack**：把 development-fitted prior 放进候选集合，重新跑 adaptive probes。
- **Validation-correct selection**：所有 uncertainty set / threshold / baseline 参数只用 development+validation 选择，然后冻结，在 test users 上一次性评估。
- **Fine-task utility**：同时报告区域大小分层的 utility，避免 robust 版本只通过拒绝小任务获得“隐私”。

如果这组实验成立，论文叙事会从：

> “单一已知模型下，一个简单 gate 可以降低位置推断”

升级为：

> “攻击者模型不确定时，单模型 Bayesian filter 会失效；我们给出对多个 plausible attacker models 同时成立的闭式双分支参与机制，并量化鲁棒性带来的任务效用代价。”

后一个故事更接近期刊论文所需要的完整问题闭环。

---

# 第二层创新方向

如果 R-BSP 完成后还要继续增强，可以考虑两个方向，但优先级低于 R-BSP。

## A. Horizon-aware / non-myopic participation

当前 BSP 最大化的是“当前任务”的 completion probability，没有考虑今天放行一个任务会不会导致后续很多任务无法参与。

可以把状态定义为候选 beliefs / privacy slack，优化未来 (H) 个任务的 expected reward，在每一步仍满足 robust branch constraints。可用有限时域 dynamic programming、MPC 或近似 value function。

这个扩展能回答一个很自然的问题：**maximal current gate 是否等于最佳长期 crowdsensing utility？答案一般不是。**

## B. Window-aware observation channel

现实任务往往不是“某一个瞬时点是否在区域”，而是“在一个采集时间窗内是否进入过区域/完成采样”。

可以把隐状态扩展为：
- current location；
- whether region has been visited；
- acquisition time bucket。

然后重新推导 report/silence likelihood。这样可以把目前“timely completion probability sweep”升级成真正的 spatio-temporal sensing model。

---

# 推荐投稿策略

**优先目标：Pervasive and Mobile Computing。**

原因不是“容易中”，而是主题边界高度吻合：移动群智感知、位置/轨迹推断、移动系统 privacy、算法与 simulation evaluation 都属于该刊明确范围。

但不建议把当前稿件仅换 PMC 模板后立即提交。建议至少完成：

1. R-BSP 或等价的实质 robust extension；
2. 非均匀 prior 下的 adaptive attack；
3. validation/test 重新分工，消除 test-selected envelope；
4. 小区域 / value-aware utility；
5. 扩充直接相关文献。

如果这些完成，稿件的创新主线、威胁模型和实验闭环都会明显更完整。
