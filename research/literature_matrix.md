# 定向文献核查与差异表（2026-09-15）

本表为本地原文/出版方页面的代理核查，不等同作者人工确认，也不是系统综述。DOI 通过保存的 Crossref JSON 与题名核对；摘要只支持摘要中出现的内容。所有 human_verified 保持 false。检索词包括 AnonySense、task acceptance inference、TMarkov、bilateral task matching、posterior privacy task crowdsensing、adaptive privacy filters；公开原文与出版方页面优先。未声称检索穷尽。

|来源、定位|攻击者/可见输出|移动与防御|保证或证据|与本文关系及核查边界|
|---|---|---|---|---|
|AnonySense, DOI 10.1145/1378600.1378624；本地 PDF，§3.1 task verification 与通信/匿名设计|系统中的任务、匿名报告；原系统有具体信任边界|任务可接受性检查、匿名通信与时序处理|架构与原型；用户匿名条件不能当作位置单元概率保证|本文固定账户可关联，研究另一个输出信道；不声称复现或击破原系统|
|Qiu 等 TMarkov, DOI 10.3390/s21072474；本地 PDF §2.2/Fig.2 及方法章节|连续任务接受/拒绝能够缩小位置范围|移动关联、语义信息、代理轨迹|原文分析与实验|直接已有任务输出推断；不能把发现这一问题写成首次。本文采用真实完成/概率沉默与双分支阈值|
|Shu 等双边匹配, DOI 10.1016/j.jnca.2018.09.007；作者机构 SMU 页面摘要，出版方介绍|任务位置和匹配输出可带来推断风险|加密匹配，分段树|仅核对元数据和公开摘要；原文下载 403|不能断言该方案不处理所有历史泄漏；不做不公平的耗时排名|
|Boukoros 等 USENIX Security 2019；本地 PDF 摘要、引言，出版方 BibTeX|众包地理测量记录|评估既有位置隐私机制|实际众包数据中的位置隐私与测量效用冲突|现实背景有证据，但不是本文任务事件的实地日志|
|Andrés 等 Geo-indistinguishability, DOI 10.1145/2508859.2516735；原论文公开版本/元数据|位置发布机制的输出|距离相关的差分隐私机制|位置隐私定义|本文真实区域完成信道不提供该保证；不把坐标噪声强行用于真实完成报告|
|Rogers 等 2016；本地 PDF 摘要、§1.1|自适应选择分析及隐私参数|DP filters 与 odometers|组合隐私界|历史状态过滤思想已有；本文不同的后验约束不继承其 DP 组合定理|
|Whitehouse 等 ICML 2023；本地 PDF 摘要、引言；PMLR 官方 BibTeX|自适应算法/参数序列|改进的 DP filters/odometers|理论结果|仅用于界定不同保证，不作为同信道性能基线|
|Eilat 等 Bayesian privacy, DOI 10.3982/TE4390；本地 PDF 摘要与引言/模型|由信号引起的后验信念改变|KL 先验/后验代价，经济学模型|Bayesian 隐私形式化及分析|实现 KL(post||prior) 双分支上限的信道适配基线；不是原文整体机制的复现|
|Wang 等 LFPM/TSTA, DOI 10.1186/s42400-025-00539-2；Springer 正文 Introduction 和 Abstract|任务与用户的匹配信息|位置指纹与两阶段候选/分配|出版方正文与实验描述|与分配输入/输出相关，不是本实验的标量参与过滤器；不主张性能超过该系统|
|Duan 等 2026, DOI 10.1109/TMC.2026.3721057；用户提供18页接受稿全文|半诚实各方、SP/NCAP不串谋；§IV pp.3–5|SP看见参与者关联的真假混合任务集合；TR收到去参与者标识数据；§V-B pp.6–8|加密掩码、dummy padding、零和奖励扰动；§VI pp.8–10给定协议输出的模拟安全|全文比较已完成；其真实任务识别 hit 与本稿位置 MAP 不同，未作数值复现。七项页码证据见 revisions/review1/duan_fulltext_comparison.md|
|GeoLife 官方 Microsoft 数据集页面、本地压缩包 manifest|公开位置轨迹；不是任务日志|本项目仅离线回放采样位置|182 用户的原始档案；本项目筛选规则、哈希、排除原因均保存|任务、送达、参与和完成全部模拟；不证明真实平台已经发生本文攻击|

## 当前贡献判断
可支撑的定位是：针对真实区域任务完成/沉默信道，给出可计算的双分支后验峰值约束及其条件，提供公平的攻击—效用仿真和失配诊断。闭式公式是简单线性约束求解；不包装成通用新隐私定义。任务推断、隐私过滤器及贝叶斯隐私都不是新概念。

不能支撑：首次发现任务输出泄漏、普遍超过已有 MCS 系统、在任意先验下保护、差分隐私、实际部署安全、精确住宅定位、实测手机能耗。HECTA 全文已读，支持观测接口和研究目标的区别；不代表全面新颖性已得到独立认证。

## 纠错记录
最初候选 AnonySense DOI 10.1145/1378600.1378607 对应另一论文，已剔除并保留 rejected_wrong_doi_crossref.json。正文与参考文献采用核对后的 10.1145/1378600.1378624。

## 2026-09-17 更新：近期原文与引用清理

- PRIVIC，PoPETs 2024(1):582–596，DOI 10.56553/popets-2024-0033。出版方全文 `literature/recent/privic_2024.pdf`，作者算法 `privic_functions.py`，MIT 许可证和固定 commit 证据已保存；Algorithm 1–3/Definition 2.6 已核对。任务适配及限制见 recent_baselines_protocol.md。
- Extremal Mechanisms for Pointwise Maximal Leakage，TIFS 19 (2024):7952–7967，DOI 10.1109/TIFS.2024.3449556。作者 2024-08-27 v3 全文保存为 pml_2024.pdf；Eq.2 与 Lemma 1 的约束已核对。
- FedSense，正式 TDSC 22(3) (2025):1877–1894，DOI 10.1109/TDSC.2024.3398994。作者版本 fedsense.pdf 的 Abstract、§4.1、§5 已阅读；本地任务选择和异步 FL 描述有原文支持。其多任务学习系统尚未复现，正文不把任意局部 gate 冒称 FedSense。
- 6 个非必要旧引用已从文献表删除/更新（其中数据网页移为脚注），原下载文件保留作研究历史；当前正式引用及旧文必要性见 reference_policy.md。

## 2026-09-18 内部审稿修订

Duan 等全文再次通过 IEEE 原记录、Crossref 与开放获取发现路径核查，仍未获得可读原文。逐维度待核查表及实际访问记录见 `revisions/review1/novelty_followup.md` 和 `literature/recent/duan_review1/`。正文进一步将贡献定位标为暂定；此项不能由题名或第三方摘要关闭。

## 用户补充全文后的当前状态

前述2026-09-18访问失败记录已由用户提供的18页 accepted author version 补足。完整比较见 `revisions/review1/duan_fulltext_comparison.md`；不把原文的分配比例/任务识别比例与本稿完成比例/位置准确率混用。
