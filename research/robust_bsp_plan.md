# R-BSP 实施计划（不伪造结果）

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
