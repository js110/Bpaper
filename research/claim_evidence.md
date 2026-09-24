# 正文论断—证据定位

所有条目均为代理核对，human_verified=false；作者需要独立确认。具体源文权限和全文状态见 literature_matrix.md。

|论断 ID|正文位置与内容|证据/定位|适用范围|
|---|---|---|---|
|C01|§1–2：任务输出推断已有研究|literature/tmarkov.pdf §2.2/Fig.2|不声称本研究首次发现|
|C02|§1–2：本地任务选择与近期隐私任务分配|literature/recent/fedsense.pdf Abstract/§4.1；fingerprint 出版方全文|接口不同，不伪造整个系统的复现|
|C03|§2：Bayesian 与 DP filters 的先例|bayesian.pdf 引言；adaptive2023.pdf 引言|本方法不继承 DP 保证|
|C04|§3–4：信道、gate、条件上界|src/model.py；正文 Eqs.1–5 的代数推导；tests/test_model.py|声明模型正确，全部可见输出入模；不适用于任意知识|
|C05|§5：数据来源与拆分|data/manifest.json；src/prepare_data.py；微软官方数据集页及所要求引用|轨迹真实、任务模拟；一个窗口/用户|
|C06|§5：配置、样本、固定/自适应攻击|configs/*.json；results/*/config.json；src/experiment.py|独立统计单位为 seed 或用户，不是所有时隙|
|C07|§6：旧基线匹配效用差值|results/combined/analysis/matched_utility.json target_utility=0.5 comparator=random/kl|内插、逐点 95% CI；无外推或普遍胜出；摘要的近期比较见 C14|
|C08|§6 表1及宏数字|results/combined/analysis/summary.csv；research/numeric_registry.json|指定参数的执行结果，与内插估计分开|
|C09|§6：模型校准及消融|同 summary 的 covered95/hit/utility；calibration.pdf|弱模型后验不等于真实不确定性|
|C10|§6：更知情攻击者超阈值|results/informed/analysis/cap_audit.json，逐条件 gz 原始事件|客户端错参数、攻击者知道真实生成概率；不偷看实际位置|
|C11|§6：耗时|summary.csv gate_us_p50/gate_us_p95；environment.json|先轨迹内分位数后跨用户平均；本机 Python，不含其他流水线|
|C12|§8：测试和审计|results/tests.txt；results/audit.json；src/audit.py|同实现审计非独立科学验证|
|C13|§2/§7：HECTA与BSP的观测接口、信任和目标区别|literature/recent/duan_fulltext/duan2026.pdf，§IV–VIII pp.3–16；revisions/review1/duan_fulltext_comparison.md|已读全文，不宣称数值复现、安全优势或首次发现任务输出推断|

图1/2 ← 内置 image_gen + research/imagegen/；图3/4/6 ← src/analyze.py + results/combined/rows.csv；图5 ← src/analyze_recent.py；图7 ← src/analyze_stress.py；图 A.1 ← src/review_diagnostics.py（保存的 Commute 点和原下凸包）。
修订后的表1（先验）、表2（代表条件，增加 pooled raw completion）、表 A.1（任务尺寸）← src/review_diagnostics.py；表3/5与旧数字宏 ← src/paper_assets.py；表4 ← src/analyze_recent.py。results/combined/inputs.json 记录组成两份源 CSV 哈希，各 analysis/provenance.json 记录统计规则。

C14：近期基线比较 → results/recent_comparison/matched_utility.json；research/recent_numeric_registry.json。下凸包与原相邻点内插属于不同估计对象。
C15：基线强度/一致性 → tests/test_recent_baselines.py；PML 通用 LP；作者 BA/IBU；results/privic_training/*audit*.json。最终 BA 全部到容差，GIBU 7 个限次。
C16：参考文献时效性 → reference_policy.md；citation_validation.json；新来源原文与 Crossref。

C17：摘要/§5.1/§6.1/表1 的先验诊断及粗网格描述 → results/review1_diagnostics/diagnostics.json、prior_users.csv、provenance.json。开发众数固定后评价测试；区间条件于固定开发预测器，不是新自适应攻击。
C18：§6.2/表2/表 A.1 的区域尺寸和原始完成率 → task_area.csv、area_events.csv、diagnostics.json；分母为全部正常任务或明确的可完成机会。仅执行 rho=0.1 的分层，不代表策略混合。
C19：§5.1/§5.4/表4 的探索性选择与训练条件 → recent_baselines_protocol.md、src/analyze_recent.py、PRIVIC 训练 manifest；测试集用于网格追加和 envelope，未用于训练信道。
C20：§1–2/结论 的创新性暂定 → revisions/review1/novelty_followup.md 逐项未解决比较；renewed Crossref 及访问记录不能支撑非重叠论断。
