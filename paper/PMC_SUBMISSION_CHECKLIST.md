# Pervasive and Mobile Computing 投稿前检查表

更新：2026-09-25

## A. 已处理的格式项

- [x] 目标期刊确定为 **Pervasive and Mobile Computing**
- [x] 使用 Elsevier 官方 `elsarticle` 文档类
- [x] `main.tex` 中期刊名改为 `Pervasive and Mobile Computing`
- [x] 删除研究草稿专用的首页 footer override
- [x] 删除正文中的 `Draft status` 段落
- [x] 保持 Elsevier numeric bibliography style
- [x] 提交打包脚本改为生成 **flat LaTeX source archive**
- [x] AI schematic provenance 改为单独 archive，不放入主 LaTeX source bundle 的子目录

## B. 必须在最终投稿前验证的版式/系统要求

- [ ] 在 Editorial Manager/ScienceDirect 的实时 Guide for Authors 中再次核对 journal-specific 要求；2026-09-25 自动访问该页面返回 403，因此不能声称所有专属要求已经核实
- [ ] 运行 `python -m src.package_paper`
- [ ] 解压 `paper/manuscript_source.zip` 到空目录
- [ ] 在空目录运行：
  `latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex`
- [ ] 检查 0 undefined reference/citation
- [ ] 检查 0 overfull box（或逐项人工确认）
- [ ] 逐页视觉检查最终 PDF
- [ ] 确认所有图的分辨率、字体、legend、caption 满足期刊要求
- [ ] 确认 submission system 是否允许/要求 Highlights、Graphical Abstract、Declaration of Interest 等单独文件

## C. 科学内容阻塞项

- [ ] 将 informed-attacker 的 model mismatch 从 limitation 升级成实质方法扩展；首选 R-BSP / model-set robust filter
- [ ] 在 development-fitted nonuniform prior 下重新运行 adaptive attack
- [ ] 不再使用 test set 选择 thinning grid / final policy envelope；改用 validation 或 nested procedure
- [ ] 新增 task-size-stratified utility
- [ ] 新增 value-aware / fine-region utility，避免只靠大区域任务维持 retention
- [ ] 对最终 robust 机制重新跑主要 synthetic + GeoLife comparison
- [ ] 明确最近方法属于 task-channel adaptations，避免宣称原系统级 guarantee 的直接比较
- [ ] 扩充直接相关文献；当前 11 条不足以支撑 20+ 页期刊稿的 novelty positioning

## D. 作者必须人工确认的声明

- [ ] 作者姓名拼写
- [ ] 作者顺序
- [ ] 通讯作者
- [ ] 单位及邮编
- [ ] 通讯邮箱
- [ ] 四项基金名称和 grant number
- [ ] funder role
- [ ] CRediT author contributions
- [ ] Declaration of competing interest
- [ ] 数据使用/伦理声明是否适用
- [ ] 所有作者最终批准投稿版本

## E. Generative AI disclosure

当前仓库记录显示，AI assistance 用于研究组织、代码、分析、写作，以及两幅 conceptual schematics。Elsevier 当前政策要求据实披露。

投稿前必须：

- [ ] 人工确认实际使用的 AI 工具/产品名称及用途，不从仓库缺失信息中猜测版本
- [ ] 按 Elsevier 要求，在 references 前加入最终 generative-AI declaration（如果当时政策仍要求该位置/形式）
- [ ] 对两幅 AI-generated conceptual figures 在 caption 中按当时政策写明工具信息
- [ ] 如果 AI 参与代码/数据分析属于研究方法的一部分，在 Methods / reproducibility 中准确说明
- [ ] 作者对所有 AI-assisted 内容完成最终科学核查并承担责任

## F. 投稿前最后一次“拒稿风险”检查

- [ ] Abstract 不把 exploratory/test-selected 结果写成 confirmatory conclusion
- [ ] Introduction 的贡献不声称 task-output leakage / Bayesian privacy 为首次提出
- [ ] Related Work 对 HECTA、TMarkov、PML、PRIVIC、prior-robust privacy 的边界写清楚
- [ ] Theorem 的条件与现实解释一致，不把 model-conditional cap 写成 attacker-independent privacy
- [ ] Results 保留不利/不显著结果
- [ ] Discussion 明确 coarse grid、48-min windows、simulated tasks、large-region bias
- [ ] Conclusion 与最终新增 robust mechanism 和实际证据一致
