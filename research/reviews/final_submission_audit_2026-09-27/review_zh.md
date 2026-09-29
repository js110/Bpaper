# 投稿前最终内部审稿（PMC）

日期：2026-09-27  
目标期刊：Pervasive and Mobile Computing  
分支：submission/pmc-2026-09-26

## 结论

从方法、实验、可复现性和论文叙事四个层面看，当前稿件已经达到“可以送外审”的技术标准。这里的“达到投稿标准”不等于“保证录用”。仍存在真实的审稿风险，但主要风险已经从“方法缺口/实验缺口”转化为论文明确承认的外部有效性限制，而不是未处理的问题。

在作者声明、利益冲突、CRediT、基金角色、数据伦理/使用说明以及作者自行处理的 AI 相关投稿要求完成之前，不应在仓库状态中标记 submission_ready=true。

## 已解决的主要拒稿风险

### 1. 单一模型假设过强
原始 BSP 在攻击者知道更准确的可用性或移动模型时会违反客户端声明的 posterior cap。现在增加：
- finite-model R-BSP；
- 模型集合内严格分支约束；
- ambiguity-set 外边界实验；
- development/validation 数据驱动模型集合构造；
- validation-best single-model control，用于区分“更好的单模型”与“鲁棒集合”的作用。

因此论文不再依赖一个未经检验的 nominal attacker 假设。

### 2. ambiguity set 拍脑袋
旧 3x3 hand grid 仍保留为 post-hoc mechanism stress，但主 replay 扩展现在采用：
- 23 名 development 用户生成 mobility/prior candidates；
- user-level bootstrap；
- 17 名 validation 用户的 bootstrap predictive-likelihood winner frequency；
- 95% support selection；
- 67 名 test 用户不参与集合构造。

alpha=0.648 没有伪装成数据驱动参数，因为 GeoLife 不含真实任务 delivery/willingness/deadline 日志。

### 3. 小区域效用接近零
论文现在给出结构性解释，而不是继续调参：
- truthful positive report 的 conditional posterior 与 scalar thinning probability q 无关；
- uniform prior 下 m-cell region 的成功报告 posterior floor 为 1/m；
- rho=0.1 时，少于 10 cells 的 truthful success 无法满足严格 cap。

新增 asymmetric DF-BSP/RDF-BSP：
- positive report 使用显式 ceiling tau；
- silence 继续使用原 BSP cap max(rho, prior peak)；
- tau=rho 时严格退化为 BSP；
- robust 版本对 finite model set 取 member-wise maximal gate 的交集。

这使“隐私放宽”只发生在不可避免的成功报告分支，不再无理由放宽 silence。

### 4. 细粒度 service 没有指标
新增：
- 1--8 / 9--31 / 32--64 cell retention；
- inverse-area-weighted utility；
- original-rho exceedance；
- branch-specific cap violation；
- synthetic 与 GeoLife 分别报告。

最终 illustrative tau=0.5：
- synthetic walk：small-region retention 56.4%，weighted retention 43.1%，branch-cap violation 0；
- GeoLife data-driven RDF-BSP：small-region retention 14.3%，weighted retention 20.8%，branch-cap violation 0.16%，original-rho exceedance 14.3%。

这些结果支持“显式 privacy-service frontier”，不支持“免费提升效用”的表述。

### 5. 近期相关工作覆盖不足
Related Work 已覆盖：
- task-output / acceptance inference；
- Bayesian privacy；
- geo-indistinguishability / PRIVIC；
- pointwise maximal leakage；
- iTAM bilateral assignment；
- task-location privacy；
- differential-obfuscation task assignment；
- secret-sharing recruitment；
- encrypted location/reward assignment；
- 2025--2026 mobility-prediction、regional-heat、fingerprint、blockchain/ZKP、HECTA 等方案。

论文明确区分这些方法保护的 coordinate / assignment / recruitment / transaction interface 与本文 visible truthful report/silence channel，避免不公平地把不同安全定义做数值排名。

## 当前证据链

- 28 个自动化测试；
- BSP、R-BSP、DF-BSP、RDF-BSP 的 branch feasibility/reduction/maximality 检查；
- informed-attacker stress；
- ambiguity-set boundary stress；
- development/validation 数据驱动模型选择；
- validation-best single-model control；
- 新 synthetic seeds；
- GeoLife development/validation/test 用户隔离；
- 近年 PML-T 与 PRIVIC-T channel adaptations；
- HECTA 全文模型差异核对；
- raw event logs、配置、bootstrap analysis 与 provenance 文件保留。

## 仍然存在、但已正确限定的审稿风险

1. **扩展仍是 post-hoc。** GeoLife test users 在更早的分析中已经被查看，因此 data-driven extension 不能称为完全独立的 confirmatory study。
2. **没有真实 MCS task logs。** GeoLife 提供轨迹而不是 delivery/willingness/deadline 行为，因此 alpha 与任务过程仍是模拟设定。
3. **空间分辨率粗。** 8x8 Beijing grid 约为公里级 cell，不能解释成地址级隐私。
4. **攻击是 greedy finite-library probing。** 不是最优长期攻击的证明。
5. **RDF-BSP 不是任意 auxiliary information 的保证。** finite-set 外仍可能出现 branch violation，当前实验直接报告这一点。
6. **没有手机端能耗/部署测量。** 当前 runtime 是 Python microbenchmark，不应声称真实移动端低开销。
7. **recent-baseline envelope selection 使用 evaluation results。** 已明确标为 exploratory，不能写成独立验证的 superiority claim。

这些限制不建议再通过堆叠新模块来“修补”。继续添加区块链、联邦学习、ZKP 或更多无关 baseline 会降低论文聚焦度。

## 投稿前技术门槛

技术侧应满足以下条件后冻结：
- 全部 28 tests 通过；
- final LaTeX 编译无 Overfull / Float-too-large / undefined references / undefined control sequence；
- flat Editorial Manager source 独立编译成功；
- flat source 与开发版 PDF 文本一致；
- Highlights 3--5 条且每条 <=85 characters；
- abstract 保持约 250 words；
- 所有 cite keys 有 BibTeX entry，所有 BibTeX entries 在正文被引用；
- 最终 PDF 对首页、公式、核心结果表、讨论、参考文献做视觉检查。

## 作者本人必须完成

- 作者姓名、顺序、单位、通讯信息最终确认；
- 全体作者批准最终稿；
- competing interests；
- CRediT（如投稿系统要求）；
- funder roles；
- GeoLife 二次数据使用/伦理措辞；
- 作者自行处理的 AI 相关投稿要求；
- 决定是否对代码建立 versioned release / immutable DOI。

在上述作者项完成前：technical_ready=true，submission_ready=false。
