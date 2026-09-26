# 研究进度
- 2026-09-06：用户授权独立项目、完整期刊论文、英文 LaTeX/PDF、无需硬件。
- 已创建目录；原项目不修改。不创建其他任务，不自动投稿。
- 当前：英文全文与实验交付已生成；正在完成最终审计记录。创新性近邻全文核对和作者信息仍待解决。
- 本机有 NumPy、Matplotlib、LaTeX；缺少 SciPy，本项目先采用 NumPy 与标准库。
- 技能：scientific-critical-thinking、experimental-design、scientific-writing 已阅读；后续使用 scientific-visualization、venue-templates、PDF 与本地自查。
- research-lookup 的 parallel-cli 不可用；用可用 web 工具和公开论文原文完成有记录的定向检索，不声称系统综述或 60 篇文献核查完成。

- pilot-v1 已完成：32 条件，各 12 个轨迹。发现固定正常/探测时隙与周期限频存在相位混淆；正式实验改为共享随机日程。pilot 保留，不进入论文主结果。10 项正确性测试通过。

- GeoLife 按固定规则得到 {'development': 23, 'validation': 17, 'test': 67}；测试用户尚未用于调参。正式配置冻结：120 条件，20 合成 seed，每 seed 4 用户，48 时隙；GeoLife 67 测试用户。阈值与基线网格全部报告，不按测试结果选优。

- 正式主实验 120 条件 / 9210 轨迹运行，稳健性 72 条件 / 2880 轨迹运行完成。文献核对后增加 Eilat 等 Bayesian privacy 的 KL 分支约束适配基线；属于后续探索比较，参数网格全部报告，不宣称复现其经济学应用。旧运行源码已快照。

- 2026-09-15 继续：KL 基线在上次中断时未完成；已保留中断日志并重新运行。主实验/敏感性无需重跑。匹配效用的区间仅在原始曲线有重叠且至少 95% bootstrap 重抽样仍有重叠时输出。

- 2026-09-16：完整 KL 扩展、12 条件独立知情攻击者测试完成；英文 13 页/14 引用/4 图/3 表编译成功，全部页面已视觉检查；无溢出和未解析引用。15 项测试及 662,304 事件审计通过。中文总结、自查、证据映射与复现说明已写入。

- 复现入口新增实跑验证：153 条验证轨迹除计时外所有字段在 1e-12 容差内与存档一致。已打包 manuscript_source.zip；最终交付哈希见 delivery_manifest.json。

- 2026-09-16 近期基线扩展：原文核对 PoPETs 2024 PRIVIC、TIFS 2024 PML；实现 BA/IBU/GIBU 与 PML-T 精确特化。PRIVIC 更新与作者代码一致，100 组 PML LP 核对通过；后续测试合计 21 项。
- 新增 132 条件 / 10,131 轨迹 / 486,288 事件。自适应攻击按各设置重跑，逐事件重建公开信道、正常任务/外生可用性共享核对通过。完整事件总数 1,148,592。
- 首轮 PRIVIC 完成率缺乏交集，透明追加全部 beta 的 gamma=0.25/0.5/0.75；使用全参数下凸包，加强基线而非挑选劣点。保留原始点及初版分析。结果不支持普遍优越性。
- 两张科学示意图由内置 image_gen 实际生成；系统图经模型改图修正任务输入与反馈箭头。英文稿扩展为 17 页 / 16 引用 / 7 图 / 4 表，正在完成最新交付复核。

- 2026-09-17 完成最新交付：引用精简为 11 项，更新原文对应及必要旧文理由；17 页 / 7 图 / 4 表已逐页视觉核对。主稿和独立解压源码包编译通过，0 Overfull、0 未定义引用。全量 1,148,592 事件审计及 21 项测试通过。当前仍为作者待审研究稿，完整证据与哈希见 delivery_manifest.json。

- 2026-09-22 按内部审稿意见完成修订：增加开发集固定众数先验诊断、任务区域尺度与原始完成率表、Commute 放大图；区分测试集选择的探索比较与独立验证，并收窄新颖性和效用主张。报告及逐条回应见 `research/reviews/reviewer_1_2026-09-17/` 和 `research/revisions/review1/response_zh.md`。修订稿为 19 页 / 11 引用 / 8 图 / 6 表，逐页视觉检查。新增诊断以保存日志重算，数值交叉核对通过；21 项测试通过。主稿及重新打包的独立源码均编译通过，0 Overfull、0 未定义引用、0 重复超链接目标。最近邻 2026 论文全文比较仍未完成，未标记投稿就绪。

- 2026-09-22 作者补充四位作者、同一单位、Lei Zhang 通讯邮箱和四项资助。已用 elsarticle 前置作者/地址/通讯作者命令填入，Funding 独立置于结论后；未虚构作者贡献或利益冲突。PDF 更新为 20 页 / 11 引用 / 8 图 / 6 表，20 页缩略图及变动页全尺寸检查，主稿和解压源码各自编译成功，正文抽取一致，无溢出、未定义引用或重复跳转目标。期刊仅暂定 PMC，最新期刊专属指南仍无法访问；作者应核对基金号 `D2O25O185` 中 O/0。交付哈希已更新。

- 2026-09-22 用户确认基金号 `D2O25O185` 中的疑似 0 字符为字母 O；正文与源码包已使用该写法，无需重新编译。

- 用户提供 DOI 10.1109/TMC.2026.3721057 的18页接受稿后，已阅读全文并以七维比较补齐 M2。主稿更新 HECTA 的真实/混合任务观测、非串谋双服务器、模拟安全保证与任务识别指标；不再写未取得全文，也不宣称已完成其数值复现。比较记录见 research/revisions/review1/duan_fulltext_comparison.md；原文与哈希保存在 literature/recent/duan_fulltext/，不放入论文源码包。PDF仍20页，实验数字未改，投稿就绪仍为 false。

## 2026-09-23 事实核查与仓库接入

完成代码/公式/元数据/结果一致性复核；7 类修正记录在 revisions/factual_audit/report_zh.md，主结果不变。21 项测试通过、352 条件共 1,148,592 个事件审计无差异，近期方法 486,288 个事件公开后验重算一致。当前 PDF 21 页，无未定义引用、溢出或重复锚点，源码包独立编译且文本一致。依用户要求初始化 Bpaper 仓库，纳入可复现材料并保留外部全文/原始压缩包的来源清单；Git 推送结果由提交记录核验。

## 2026-09-26 R-BSP 方法升级

- 根据第二轮内部审稿，将旧 informed stress 的模型失配失败从 limitation 升级为有限模型鲁棒机制问题。实现 `robust_bsp_gates` 与 `RobustPublicBelief`：候选模型共享公开任务/输出历史，各自维护后验；同一任务的 R-BSP gate 为各模型 nominal BSP 最大 gate 的最小值。
- 新增有限模型“最大公共 scalar gate”命题并写入论文。该结论只覆盖给定 finite ambiguity set；不声称任意先验、任意辅助知识或 differential privacy。
- 新增 2 项 R-BSP 测试后完整测试套件为 23 项。GitHub Actions/Python 3.12.14 上 23 项全部通过；随机多模型交集、分支约束、最大性与包含 informed attacker 的集成条件均通过。
- 新增 `configs/robust_informed.json`：9 模型网格 `v∈{0.05,0.3,0.8}` × `alpha∈{0.3,0.648,0.9}`，20 个新 synthetic seeds、4 users/seed、40 条件、3,200 条轨迹；分析按 seed cluster bootstrap 1,000 次。
- 已真实执行该 stress。rho=0.1 时，nominal BSP 在 alpha_low/alpha_high/move_low/move_high 下 informed-attacker local-cap violation 分别约 12.6%/2.6%/2.8%/14.6%；R-BSP 五组条件均为 0，因为 attacker 的精确模型被显式包含。R-BSP retention 约 39.7%，而 BSP 为约 46.9%--55.2%，说明鲁棒性代价明显。
- 上述模型集合是在旧失配结果已知后设计，因此全部标记 post-hoc exploratory；没有把它包装成预注册或独立确认。论文标题、摘要、方法、实验、结果、讨论和结论已据此重构，保留 utility cost 和集合外无保证的边界。

## 2026-09-26 R-BSP 边界实验与 CI 拆分

- 修复之前的重型流水线：代码单测、R-BSP 实验、LaTeX 编译彻底拆开。快速代码测试和 checkpoint PDF 编译均已在 GitHub Actions 成功验证；cm-super 修复了此前 pdfTeX scalable-font 错误。
- paper-build 不再随普通论文文字改动自动触发；R-BSP 主实验也不再随每次 commit 重跑。
- 新增 post-hoc boundary characterization：固定原 9-model ambiguity set，用新 seeds 4000--4019 测 4 个不属于集合的正确 attacker/generating models，共 8 条件 / 640 trajectories。
- rho=0.1 时，R-BSP 对 unlisted interior alpha=0.50 为 0 local-cap violation；对 unlisted interior v=0.50 为 2/3840 (0.052%)；对 outside alpha=0.98 为 6.93% [5.70%, 8.31%]；对 outside v=0.95 为 1/3840 (0.026%)。结果已写入正文和新表，明确 finite-set 保证不能外推。
- Related Work 新增 3 篇 2025--2026 MCS 隐私/任务分配文献，用于区分坐标/匹配/交易隐私接口与本文 linkable report/silence channel。

## 2026-09-26 最终 checkpoint 编译

- 轻量 CI 拆分后的最终论文 checkpoint 编译成功。
- 当前 `paper/main.pdf` 为 50 页；最终 LaTeX 日志无 Overfull、无 Float-too-large、无未解析引用、无 Undefined control sequence。
- 新 R-BSP boundary 表的横向溢出已通过紧凑列标题修复；主结果表通过轻微压缩 `arraystretch` 消除了页面高度警告，未删减实验数据。
- GitHub Actions 只在显式 `paper/.build-request` checkpoint 下编译论文；普通正文修改不再触发 TeX 安装或实验。
