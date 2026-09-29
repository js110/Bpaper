# 第二轮内部审稿：面向 Pervasive and Mobile Computing 的录用风险评估

日期：2026-09-26  
目标稿：`paper/main.tex`  
目标期刊：Pervasive and Mobile Computing (PMC)

## 总体判断

当前稿件已经具备完整问题定义、数学推导、可复现实验、负结果披露和近期强基线，但尚不建议以现有科学贡献直接投稿。主要风险不是排版，也不是“没有真车/手机实验”，而是方法增量容易被审稿人概括为：在一个已知的任务输出推断问题上，对指定二元观察信道求一个一步标量 gate 的闭式最优解；其绝对隐私解释又高度依赖正确先验、正确可用率和正确移动模型。

论文已经诚实报告了这一局限，但“诚实报告局限”本身不会自动转化为创新。最有效的增强方向是把现有最强负结果——模型失配下攻击者超过客户端后验 cap——升级为方法问题，并设计一个对模型不确定性显式鲁棒的新版本。

## 最可能导致拒稿的四个问题

### 1. 核心保证依赖共享正确模型，且论文自己给出了失败例

当前 BSP 的顺序 cap 是 model-conditional。更知情攻击者使用不同的可用概率或移动模型时可超过客户端的阈值。这不是边角问题，而是直接击中“privacy filter”最核心的保证。

审稿人可能会问：如果平台恰恰是更强的攻击者，为什么由客户端自建错误模型计算出的 cap 仍有安全意义？

**建议：把模型不确定性从 limitation 变成新方法。**

### 2. 闭式 gate 的数学结构偏简单，新颖性容易被压缩

现有 Proposition 1 本质是二元输出、标量 q 下的线性约束交。推导是正确的，但顶刊/强二区审稿人可能认为“技术难度和普适性不足”。

**建议：引入模型集合、状态相关可用率或多分支观察后，形成真正的新优化问题。**

### 3. 实证比较存在探索性 test-set envelope selection

近期 PML-T / PRIVIC-T 比较已经透明说明：部分 gamma 网格和 lower-hull envelope 是看到测试结果后扩展或选择的。透明是优点，但确认性结论仍弱。

**建议：冻结新的 robust 方法和参数后，用 validation 选配置，再只在现有 67 个 test 用户上做一次最终评价；如果不想重拆数据，可至少新增一组完全未用于选择的随机种子/时间窗口作为 confirmatory set。**

### 4. 约 50% opportunity retention 的实际服务含义较弱

现有诊断显示 BSP 完成主要来自大区域任务，小区域任务可被系统性拒绝。这意味着当前 utility 指标容易被质疑为“保住了容易保的任务”。

**建议：把任务价值改为 size-aware utility，并增加 region-size-stratified frontier。不要只报告机会保留率。**

## 最推荐的创新升级：Robust Branch-Safe Participation (R-BSP)

### 核心思想

客户端不再假设只有一个精确模型 `M`，而是维护一个公开模型集合 / ambiguity set：

- 多个移动转移矩阵；
- 可用率 `alpha` 的区间；
- 可选的状态相关完成概率；
- 多个开发人群先验或平滑强度。

对每个候选 gate `q`，要求报告分支和沉默分支在所有允许模型下都满足风险约束：

[
q^* = \max_{q\in[0,1]} q
]

subject to

[
\sup_{M\in\mathcal M}\|b_{t,M}^{+}(q)\|_\infty \le c_t,
\qquad
\sup_{M\in\mathcal M}\|b_{t,M}^{-}(q)\|_\infty \le c_t.
]

这会把论文从“正确模型下的贝叶斯 gate”推进到“攻击者模型不确定性下的鲁棒参与过滤”。

### 为什么它比继续堆基线更重要

1. 直接修复当前论文最强负结果；
2. 形成与现有闭式 BSP 明确不同的新理论问题；
3. 不需要真实硬件，现有仿真代码和 GeoLife 都能支持；
4. 可以保留现有 BSP 作为 nominal special case；
5. 与 distributionally robust optimization / robust Bayesian inference 有自然理论联系，但研究对象仍是 MCS 输出信道。

### 可落地的三档实现

#### A. 最小可行版：有限模型集合 R-BSP

从开发数据构造 K 个候选模型，例如：

- population prior；
- per-user smoothed prior；
- random-walk transition；
- commute transition；
- `alpha` 的低/中/高三档。

每个时隙对 K 个模型同时检查后验峰值，取所有模型允许 q 的最小值。

优点：实现简单、完全可复现、可直接验证“更知情攻击者”是否仍突破。

#### B. 论文增强版：区间不确定性

令 `alpha_i \in [\underline{\alpha}_i, \overline{\alpha}_i]`，或者对转移概率给出置信区间。将 worst-case branch constraint 转成一维线性分式约束，再通过端点/LP 求解。

如果能给出“最坏情况一定出现在 ambiguity polytope 的极点”之类的命题，理论贡献会明显加强。

#### C. 更强版：数据驱动 ambiguity set

用开发用户 bootstrap 或 divergence ball 构造模型集合，研究 ambiguity 半径与 utility 的权衡，并给出 finite-sample coverage 或 calibration 解释。

这一步理论工作较大，不是首选的最低成本方案。

## 第二个增强点：任务尺度感知效用

当前正报告要求支持集合足够大，小区域任务天然困难。建议把 utility 从简单 opportunity retention 扩为：

[
U = \sum_t v(S_t)\,Y_t,
]

其中 `v(S_t)` 可以取：

- 等值；
- 与区域面积反比；
- 小区域更高价值；
- 按任务类型分层。

必须同时报告 1--8、9--31、32--64 单元的风险--效用曲线。这样可以直接回答“方法是不是只保住大区域任务”。

## 第三个增强点：确认性实验设计

建议冻结：

1. nominal BSP；
2. R-BSP；
3. PML-T；
4. PRIVIC-T；
5. random / periodic baselines。

使用 development 构造模型和 ambiguity set，validation 选 R-BSP 半径及所有混合参数，test 只跑一次。不要再用 test lower hull 选择主要结论。

主要终点建议：

- attacker MAP hit rate；
- worst-case posterior peak violation rate；
- region-weighted utility；
- log loss / calibration；
- online gate runtime。

其中“violation rate under informed attacker”应成为新方法的核心安全终点。

## 第四个增强点：论文叙事重构

建议标题从当前偏现象式标题，收敛到机制与鲁棒性，例如：

**Robust Participation Filtering against Sequential Location Inference in Mobile Crowdsensing**

若只完成有限模型集合版本，也可使用：

**Branch-Safe Participation under Model Uncertainty for Sequential Mobile Crowdsensing**

摘要贡献顺序应变为：

1. 明确真实完成/沉默输出信道；
2. nominal BSP closed-form；
3. R-BSP 对多模型攻击者的鲁棒约束；
4. GeoLife + synthetic confirmatory evaluation；
5. 明确大/小区域效用边界。

## 不建议做的“伪创新”

- 不要把 BSP 改名后声称新的隐私定义；
- 不要把模型条件后验 cap 写成 differential privacy；
- 不要仅增加区块链、联邦学习、零知识证明等不相关模块；
- 不要把 HECTA 的 dummy-task 机制简化成一个弱基线；
- 不要只增加更多普通算法而不修复模型失配；
- 不要用更多图或更多 seed 替代方法层创新。

## 投稿顺序建议

首投目标：Pervasive and Mobile Computing。其 scope 直接覆盖 mobile crowdsensing、location-based services 和 privacy/security。

备选：
- Journal of Information Security and Applications：若进一步强化“攻击者模型、鲁棒隐私约束、安全分析”；
- Computer Communications：若强化移动网络/任务通信模型和网络可用性；
- Internet of Things：若扩展为更一般 IoT sensing / cyber-physical-human framework。

当前版本如果不做 R-BSP 或等价的实质方法升级，建议至少完成确认性测试拆分和任务尺度效用，否则 PMC 审稿中“novelty + practical utility”两项仍有明显风险。
