# R-BSP 实施状态与后续计划（不伪造结果）

## 目标

把现有 BSP 对单一声明模型的条件后验 cap，扩展到有限模型集合下的鲁棒 cap，并以更知情攻击者的 violation rate 作为主要安全终点。

## Phase 1: finite-model robust gate

对候选模型集合 `M_1,...,M_K`：

1. 每个模型独立预测 `b_t^{(k)}`；
2. 对当前任务计算 nominal BSP 的 `q_k^*`；
3. 取 `q_R^*=min_k q_k^*`；
4. 用同一公开 `q_R^*` 产生输出；
5. 客户端保存每个模型的后验状态；
6. 攻击者使用独立的 informed model 评估真实 violation。

需要新增：
- `RobustBSPPolicy`;
- model ensemble state；
- per-model posterior audit；
- robust gate unit tests。

## Phase 2: model construction

全部从 development 数据构建，test 不参与：

- uniform + random-walk；
- population prior + random-walk；
- smoothed transition；
- alpha low / nominal / high；
- optional commute model。

Validation 用于选择 ensemble 大小和任何 uncertainty radius。

## Phase 3: confirmatory evaluation

重新冻结实验协议后：

- synthetic static / walk / commute；
- GeoLife test users；
- nominal attacker；
- informed attacker；
- misspecified attacker；
- region-size weighted utility。

主要报告：
- MAP；
- max posterior；
- cap violation rate；
- raw completion；
- opportunity retention；
- size-aware utility；
- calibration；
- runtime。

## Phase 4: theoretical extension

有限模型集合时可先给出：

**Proposition.** 若每个候选模型 `M_k` 的 nominal BSP gate 为 `q_k^*`，则 `q_R^*=min_k q_k^*` 是在“同一标量 gate 且必须同时满足全部模型 branch constraints”的机制类中的最大可行 gate。

证明直接来自可行区间交集。

这条命题虽然简单，但与实验中对 informed attacker 的鲁棒性直接对应，且比当前单模型 Proposition 更能支持论文主问题。

后续若需要更强创新，再把有限集合扩为 polyhedral / divergence ambiguity set。


## 2026-09-26 已完成

- Phase 1 finite-model gate 已完成：`src/model.py`、`src/experiment.py` 已接入；真实位置不进入模型集合状态。
- 理论命题已写入 `paper/main.tex`：有限模型每个 feasible set 均为 `[0,q_k^*]`，公共最大 gate 为 `min_k q_k^*`。
- 新增 2 项 R-BSP 测试，完整 23 项测试在 GitHub Actions 上通过。
- 完成第一轮 post-hoc synthetic stress：40 conditions / 3,200 trajectories。rho=0.1 下，旧 BSP 在四类失配产生 2.6%--14.6% attacker local-cap violations；包含 attacker 精确模型的 9-model R-BSP 为 0，但 retention 降至约 39.7%。
- 该结果只验证 finite-set 机制和代价。由于模型网格是看到旧失败后确定的，不能称 confirmatory。

## 尚未完成、也是下一轮真正能继续抬高论文质量的部分

1. 用 development/validation 数据给 ambiguity set 一个数据驱动的构造规则，而不是永久使用手工 3×3 网格。
2. 预先冻结模型集合选择规则后，再做未参与选模的验证；现有 GeoLife test 已被其他探索分析使用，不能重新包装成 pristine confirmatory set。
3. 增加 ambiguity set 外攻击者 / 插值模型测试，明确 finite-grid 保证的失效边界。
4. 研究更紧的 structured/polyhedral ambiguity set，降低当前 9-model intersection 的保守性。
5. 将 task-size-aware utility 正式纳入 robust 选模目标，而不仅报告等值 opportunity retention。
