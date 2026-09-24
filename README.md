# 连续群智感知任务输出与位置隐私

项目已形成英文全文、模型推导、无硬件实验和可重生成的图表。范围是普通移动群智感知；不使用车联网。当前是供作者审阅的研究稿，未投稿，最近邻 HECTA 全文比较已完成，作者人工核查和进一步科学验证仍待完成。

仓库：[js110/Bpaper](https://github.com/js110/Bpaper)。同步范围、外部原文/原包获取及日常 Git 操作见 [仓库管理说明](research/repository_management.md)。

## 阅读入口

- `paper/main.pdf`：英文完整稿。
- `research/revisions/factual_audit/report_zh.md`：本轮事实、公式、代码和数据一致性核查。
- `paper/main.tex`：LaTeX 正文；`numbers.tex` 和表格由结果自动生成。
- `research/summary_zh.md`：中文研究结论与限制。
- `research/protocol.md`、`amendments.md`：研究协议和修订。
- `research/literature_matrix.md`：原文证据、DOI、更近论文的未解决重叠风险。
- `research/self_review.md`：本地自查，区别于外部同行评审。
- `research/revisions/review1/response_zh.md`：内部审稿逐条回应及未解决项。
- `results/review1_diagnostics/`：开发先验诊断、任务尺寸分层、原始完成率及放大图的来源与结果。
- `results/combined/analysis/summary.csv`：120 个主条件加 16 个 KL 扩展条件。
- `results/sensitivity/analysis/summary.csv`、`results/informed/analysis/summary.csv`：稳健性与更知情攻击者实验。

## 环境

在本项目根目录执行命令。实际主实验环境为 macOS arm64、Python 3.14.5、NumPy 2.4.1；具体版本和源码哈希保存在各运行的 `environment.json`。依赖为 Python 3.10+、NumPy、Matplotlib、SciPy（独立 LP 核对）；LaTeX 需要 TeX Live、latexmk、elsarticle 及常见字体/数学包。`requirements-lock.txt` 保存生成交付时的安装版本。没有硬件、GPU、SUMO、密钥或付费 API 要求。

```bash
cd /Users/jiangsheng/Desktop/crowdsensing_task_privacy
python3 -m venv --system-site-packages .venv
source .venv/bin/activate
python3 -m pip install -r requirements-lock.txt
export MPLCONFIGDIR="$PWD/.cache/matplotlib"
python3 -m unittest discover -s tests -v
python3 -m src.audit
```

## 数据

`data/manifest.json` 保存官方下载 URL、SHA-256、选样、排除理由、拆分与文件定位；`data/geolife.zip` 是本地已下载的 Microsoft 原包。该原包不是本项目新采集数据，不另赋许可证。任务及所有参与/报告事件为模拟。公开来源：
https://www.microsoft.com/en-us/download/details.aspx?id=52367

若原包已存在，可按保存的规则重新生成开发、验证、测试 NPZ：

```bash
python3 -m src.prepare_data
```

不跨缺失分钟插值；一个用户一个 48 分钟窗口。开发 23、验证 17、测试 67，另排除 75 人。拆分按用户进行。开发估计移动参数，验证为小规模检查，最终配置与全部参数网格保留。

## 重生成分析、图表和 PDF

已有原始结果时不必重跑仿真：

```bash
python3 -m src.analyze --run results/combined
python3 -m src.analyze_stress
python3 -m src.paper_assets
python3 -m src.analyze_recent --paper-assets
cd paper
latex -interaction=nonstopmode elsarticle.ins
latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex
```

`paper_assets` 生成数字宏、表格、参考文献和图表副本；不覆盖正文。`results/combined/inputs.json` 记录拼接的两个原始 CSV 哈希。`src/analyze.py` 中的 cluster bootstrap 使用固定种子，置信区间是逐点而非同时区间。分析耗时可能高于仿真，因为包含多组 bootstrap 内插。

## 从头重复实验

不要覆盖现有证据目录。运行脚本自动拒绝覆盖已完成的原始结果。以下命令使用同一冻结配置，输出到一个新的目录：

```bash
python3 -m src.reproduce --output results/reproduction_01
```

这会重复 final、kl_baseline、sensitivity、informed、recent_baselines、recent_privic_thinning；重新用开发数据训练 PRIVIC，再分析原主实验/KL 合集及近期基线比较。也可以用 `--runs final` 只复现一组。若目录已存在，请改名，不要删除原始证据。硬件计时应重新测量，不能要求与存档逐位一致；概率与事件结果应可复现。`tests/test_pipeline.py` 已对一个自适应 BSP 条件进行逐事件数值回放检查。

## 文件和实验语义

`model.py`：公开任务、观测、贝叶斯更新与 gate；`experiment.py`：轨迹、任务、用户响应、攻击和评估；`prepare_data.py`：轨迹输入；`analyze*.py`：统计与绘图。真实位置只传入用户响应与评估，攻击不接收未来轨迹。审计日志包含 truth 字段用于查证，不能把整份审计日志当作攻击 API。

共有 23,929 次主/扩展/敏感性轨迹执行，含重复使用的轨迹，不是独立受试者数。每次 48 槽。Pilot、validation 和中断运行不计入正文主结论。固定截止释放使延迟恒为一槽；没有把仿真延迟、Python 时间或零密码实现描述成手机实测。

## 投稿前仍需解决

剩余作者声明与确认；更广泛的创新性与实际效用验证；独立审查假设和实现；现实任务或更丰富窗口模型；目标期刊当前专属要求。当前使用 Elsevier 官方 elsarticle 模板，PMC 为暂定匹配方向，未认证投稿格式全部合规。详见 `research/venue.md` 和中文总结。

## 新增近期基线和生图示意图

- `research/recent_baselines_protocol.md`：2024 年原论文来源、强基线选择依据、完整算法与任务接口适配的区别、参数冻结与后续扩展记录。
- `research/recent_comparison_zh.md`：近期对比结果和限制。
- `src/recent_baselines.py`：PRIVIC BA/IBU/GIBU 训练、PML-T 精确求解及独立 LP。作者代码和 MIT 许可证在 `literature/recent/`。
- `results/recent_baselines/`、`results/recent_privic_thinning/`：新增 132 条件、10,131 次轨迹执行；攻击对每种设置独立重跑。
- `results/privic_training/`：24 个训练信道、扰动计数、迭代残差；7 个最终 GIBU 达到迭代上限，不冒称全部收敛。
- `results/recent_comparison/`：全参数汇总、原始点、下凸包混合比较和配对区间。下凸包是探索性的测试集边界选择，不等于独立调参后部署。
- `paper/figures/system_architecture.png`、`bsp_workflow.png`：用内置生图模型生成并核对的系统架构、方法与沉默反例图。提示词和核查记录在 `research/imagegen/`。数据曲线由 Matplotlib 从原始结果生成。

现有结果的额外核查：

```bash
python3 -m src.audit_recent
python3 -m src.audit_recent --run results/recent_privic_thinning
python3 -m unittest discover -s tests -v
```

单独重跑近期方法并重新训练（输出目录必须是新的）：

```bash
python3 -m src.reproduce --output results/recent_reproduction_01 --runs recent_baselines recent_privic_thinning
python3 -m src.analyze_recent --recent-run results/recent_reproduction_01/recent_baselines --extra-run results/recent_reproduction_01/recent_privic_thinning --reference-run results/final --output results/recent_reproduction_01/comparison
```

上述复现分析默认不会改论文图；只有显式 `--paper-assets` 才复制新图表到 `paper/`。PRIVIC 的任务适配不继承原位置输出的 geo-ind 保证；PML-T 是原约束在本信道下的精确特化。不能将结果写成全面超越两个已发表系统。

参考文献遵循近五年优先；逐项旧文保留理由见 `research/reference_policy.md`，当前正文与文献表 11 项一一对应。

## 审稿后诊断与图表复现

2026-09-18 修订增加开发先验无输出诊断、任务尺寸分层和所有正常任务的原始完成率；没有新模拟条件。新表和附录图均从已有数据自动生成：

```bash
.venv/bin/python -m src.review_diagnostics --output results/review1_diagnostics --paper-assets
cd paper
latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex
```

默认不加 `--paper-assets` 时只生成指定结果目录，不修改论文。当前主表采用 `main_table_revision.tex`，附加数字在 `review_numbers.tex`；旧 `main_table.tex` 保留但不再被正文引用。新 raw completion 为 pooled ratio，与旧汇总的逐轨迹比率平均不混用。预测先验仅用开发用户拟合，新增区间条件于该固定预测器；任务尺寸计数是描述性结果。逐条回应见 `research/revisions/review1/response_zh.md`，最近邻全文比较已在 `research/revisions/review1/duan_fulltext_comparison.md` 补齐。
