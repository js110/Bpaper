# 稿件事实与一致性复核（2026-09-23）

对象：本项目 `paper/main.tex`，不是另一个 PCVCS 车联网项目。范围为正文、数学推导、实现接口、结果来源、基线原文、参考文献元数据、作者基金和 PDF。使用 scientific-critical-thinking、scientific-writing 和 PDF 核查流程。此次不改变仿真策略、数据或历史测量值。

## 已修正

1. **实现能力描述过度。** 原稿声称验证 observation identifiers 和 expired tasks，容易被理解为独立消息编号及真实到达时间的过期校验。`src/model.py:PublicBelief.observe` 实际检查任务/观测的 task_id 与 slot 匹配、重复 task_id、deadline 不早于采样 slot。现据实改写，并说明及时完成由 Bernoulli 变量表示，没有网络迟到消息处理。测试覆盖描述同步改为 invalid task deadlines。
2. **PML 推导用语错误。** 原文说常数似然同时达到两个上界；实际达到二者的最小值。已修正，并明确除以 alpha 的公式要求 alpha>0，alpha=0 时任意门控完成概率均为零。公式、实现和实验结果不变。
3. **KL 最大门控说法过于精确。** 实现用 30 次二分近似；零先验质量区域返回 q=0，该分支在声明先验下任意 q 都无信息。已写明近似与退化分支，避免宣称所有情况下实现都返回精确最大 q。
4. **并列概率处理说明不完整。** MAP 使用数值容差后均匀并列期望；可信集使用稳定排序、按单元编号破同概率。现明确两者规则和 MAP 容差。
5. **参考文献作者形式。** Fully-Adaptive Composition 的官方 PMLR 元数据为 Steven Wu，原稿扩写为 Zhiwei Steven Wu。按官方记录统一为 Steven Wu，并同步 `src/paper_assets.py`，避免重新生成时恢复旧形式。[官方页面](https://proceedings.mlr.press/v202/whitehouse23a.html)。
6. **发布状态同步。** 按用户本轮要求加入 Bpaper 仓库链接和工作仓库性质；不再保留“从未公开存放”的过时表述。第三方原文和原始数据单独获取。

7. **附录浮动位置。** 新增解释后出现附录表浮到附录标题之前，已在附录前清空浮动队列并分页，使标题先于其表格出现。

## 本轮验证证据

- 项目 `.venv` 中 21 项测试全部通过，含 BSP 最大性、PML 与独立 LP 对照、PRIVIC 作者代码一致性、策略包络 LP 对照。日志：`tests.log`。系统 Python 首次执行缺少 SciPy，3 项报错；失败日志完整保留为 `tests_system_python_failed.log`，随后使用已有项目环境通过，未把环境错误隐去。
- 重跑 `src.audit`：352 个条件、23,929 次轨迹执行、1,148,592 个事件，日志与汇总行一致，GeoLife 原包哈希一致，未发现问题。此检查不是对真实世界有效性的独立认证。
- 重跑两组 `src.audit_recent`：60/72 条件、221,040/265,248 个事件。只用公开历史重建近期基线门控与后验，最大后验差为 0；共同正常任务与外生可用性一致。见 `recent_channels.log` 和 `thinning_channels.log`。
- 逐项核对 64 个数值宏与 CSV、注册表；重新生成 prior/任务面积/原始完成率诊断，与之前保存输出一致，4 个稿件表格/宏文件与重生成结果一致。见 `numeric_checks.json` 和 `results/factual_audit_diagnostics/`。
- 手工复核 BSP 两分支不等式及双随机转移的归纳条件、PML 二元通道特例、KL 的后验到先验方向、PRIVIC 真实资格适配改变原始隐私语义。未发现需要改变已保存实验数字的推导问题。
- 重新检查 2026 HECTA 全文比较记录：平台可见带参与者关联的真假混合任务集合；其真实任务识别率不是定位 MAP。保留“未复现、无数值优越性结论”的界限，详见 `../review1/duan_fulltext_comparison.md`。
- 核对作者顺序、单位、通讯邮箱与四个基金编号，保留用户确认的字母 O：**D2O25O185**。本轮没有从外部验证基金授予事实，稿件明确这些信息由作者提供。

## 原始来源交叉核查

[PML IEEE 页面](https://ieeexplore.ieee.org/document/10646583/)与[PRIVIC 官方页面](https://petsymposium.org/popets/2024/popets-2024-0033.php)确认两项对比方法正式发表年份为 2024；2024 比较仍符合近三年要求。GeoLife 官网要求的三项旧数据文献保留，未将其年份改成新版网页日期。[GeoLife 下载页](https://www.microsoft.com/en-in/download/details.aspx?id=52367)的页面 Version 字段与下载文件名不同，稿件明确指压缩包 1.3。2026 location fingerprint 文献按[出版页面](https://link.springer.com/article/10.1186/s42400-025-00539-2)保留 2026 年，不误用 DOI 中的 2025 作为正式年份。

## 仍需科学验证的限制

- 两个近年强基线是任务通道适配版本，不是对原系统全部实验的复现，也没有证据支持全面优于它们。
- 主要回放攻击使用均匀先验；开发数据拟合的无输出预测器可达 25.75%，因此 BSP 下 2.4% 的均匀模型命中率不能解释成现实攻击者准确率上界。
- 匹配效用包络和追加 thinning 网格带有测试集探索性质；区间不含训练噪声变异。现有诊断不足以替代开发集选参后独立最终评估。
- 保留的任务主要为大区域任务，原始完成率低；模型保证依赖共同正确先验、观测模型及双随机转移，不覆盖任意辅助信息。
- 目标期刊最终政策、作者声明、创新性充分程度和真实部署价值尚需负责作者及外部同行审阅。本次核查不能保证不存在任何遗漏。

最终编译和页面检查见 `final_checks.json`；对应源文件修改见 `manuscript.diff`。
