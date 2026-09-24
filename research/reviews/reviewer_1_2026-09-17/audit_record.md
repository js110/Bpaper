# 内部预审核验记录

范围：作者授权的当前应用内 AI 辅助工作稿；仅本地文件工具和当前应用模型，没有额外网络/外部服务调用。工作根目录 `/Users/jiangsheng/Desktop/crowdsensing_task_privacy`。仅审查目录写入。用户最终核实并承担科学责任。

## 阅读顺序和材料

1. AGENTS.md、research/protocol.md、research/progress.md；peer-review SKILL.md、ethical_review_practice.md 及其统计/报告/常见问题参考。
2. 完整 main.tex、生成数字/4张表/references.bib；核心 model、experiment、recent_baselines、analyze_recent、analyze、prepare_data 和所有测试源码；训练与近期分析协议、修订说明。
3. 独立提出模型/先验、任务尺度、凸包选择诊断；运行 checks.py。之后才读取 self_review.md，未用其替代独立判断。
4. 读取 README、requirements-lock、环境与训练诊断；针对性检查本地 PRIVIC Algorithm 1–3、GIBU 定义和 PML Lemma 1 文本。没有重新核实全部引用原文或在线元数据。
5. 视觉查看 system_architecture.png、bsp_workflow.png、recent_tradeoff.png。用 main.aux 确認节/图/表/公式编号。未重编译或逐页验收 PDF。

核心输入哈希见 review_input_hashes.json；主线程另有审稿开始时快照 review_request_2026-09-17.json。

## 执行命令及输出

所有命令在项目根目录执行；`R=research/reviews/reviewer_1_2026-09-17` 在下列说明中为路径缩写，不是实际设置的环境变量。

- 首次 `PYTHONDONTWRITEBYTECODE=1 MPLCONFIGDIR=research/reviews/reviewer_1_2026-09-17/mpl_cache python3 research/reviews/reviewer_1_2026-09-17/checks.py`：系统 Python 缺 SciPy，在首个 PML LP 检查停止；完整错误保留 checks_console.txt。没有安装任何依赖。
- 改用同命令但解释器为 `.venv/bin/python`：成功；输出 checks_console_venv.txt、checks_output.json。300 个 BSP 随机分支/最大性检查无失败；100 个 PML LP 最大差 1.1102230246251565e-16。包含沉默反例、GeoLife prior-only 诊断、8 份日志正常任务面积分层、全方法补入共同端点的探索。固定随机种子 170926。脚本本身保存为 checks.py。
- `PYTHONDONTWRITEBYTECODE=1 MPLCONFIGDIR=research/reviews/reviewer_1_2026-09-17/mpl_cache .venv/bin/python -m unittest discover -s tests -v`：21/21 通过，0.900 秒；tests_output.txt。包括小型仿真/一条48槽存档回放，不是全套实验复现。
- `PYTHONDONTWRITEBYTECODE=1 MPLCONFIGDIR=research/reviews/reviewer_1_2026-09-17/mpl_cache .venv/bin/python -m src.analyze_recent --output research/reviews/reviewer_1_2026-09-17/reanalysis`：成功；仅输出到审查目录，没有 --paper-assets。reanalysis/ 存分析、图、表，reanalysis_console.txt 为输出；reanalysis_comparison.json 记录 matched_utility JSON 与原件结构完全相等、近期 LaTeX 表与 paper/recent_matched_table.tex 字节完全相等。
- `PYTHONDONTWRITEBYTECODE=1 .venv/bin/python research/reviews/reviewer_1_2026-09-17/prepare_audit.py`：生成审核输入、引用键转换、输入哈希及 additional_diagnostics.json 中的 raw completion。引文转换只用于11项引用的一致性，不把本地格式检查称为文献真实性核查。

`checks.py` 不重跑原实验，只读取日志/处理后数据并运行小型公式数值检查。开发人口 prior 选单元严格只用 development，随后在 test 评分；它不访问任务输出，不重跑 BSP gate 或自适应区域选择，不证明 informed-attack 最终风险或 rho 违反。

## 技能检查

技能脚本目录为 `/Users/jiangsheng/.agents/skills/peer-review/scripts`。以下各脚本实际执行，报告保留：

- validate_review_intake.py intake.json → intake_validation.json：BLOCKED，原因是无目标期刊与应用模型非本地推理不能映射技能字段；真实授权及不适用处理见 intake_context.md。作者已明确授权，未伪造期刊政策通过。没有运行要求 READY intake 的 generate_review_scaffold.py，直接按作者内部预审范围建立工作稿。
- select_reporting_guidelines.py study_profile.json → reporting_guidelines.json：VALID、NO_BUNDLED_GUIDELINE_MATCH。计算机隐私仿真不强套临床试验清单。
- validate_claim_evidence.py claim_evidence.csv → claim_evidence_validation.json：VALID_WITH_ALIGNMENT_GAPS；6项主张，C2–C5仍有范围/证据问题。
- audit_statistics_reproducibility.py statistics_checklist.json → statistics_audit.json：VALID_WITH_REVIEW_GAPS。完成性清单不等于统计质量分数。
- audit_citations.py citation_keys.md citation_references.csv → citation_audit.json：11项全部对应，无缺失/未引用条目。全部标 not_verified，表示未在本次做完整外部文献验证；两篇 GeoLife 会议文献本地 Bib 条目未列 DOI/URL，不据此认定引用不存在。
- lint_review.py review_zh.md → review_lint.json：READY_FOR_HUMAN_REVIEW，6条结构化意见，无错误/警告。这只是格式和有限词汇检查，不是科学结论认证。

## 核验边界和保留

未重跑全套实验、全部事件审计、原始 ZIP 预处理、PRIVIC 训练；未联网核查文献；未验证真实部署可用性、伦理/使用许可最终判断或手机性能。未修改论文/实现/旧结果。新审查产物由作者授权保留在此项目审查目录，不作为外部发表意见、训练材料或无关研究。没有可发送的期刊 editor-only 通道；review_zh.md 最后格式标题明确标为不适用。
