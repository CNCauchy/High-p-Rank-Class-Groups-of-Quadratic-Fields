# Cohen–Lenstra 子问题：精确研究基线

## 当前结论

本项目研究虚二次域中 5-rank 至少 2 的理想类群计数。当前阶段已经固定研究对象、量词、已知下界、有限边界反例与后续路线；**尚未证明计划书要求的指数改进，也没有可绑定该开放命题的 Lean 内核回执**。

计划书中的 `X^(1/3+δ-o(1))` 没有给出 `o(1)` 的量词顺序。本项目采用下述 `EXP-EPS` 作为保守、可复现的主候选；它与计划书字面陈述的关系记为 `unknown`，在标准“任意 ε 指数损失”解释下条件等价。

## 对象与计数函数

对实数 `X>0`，令

\[
N^-_{5,2}(X)=\#\{[K]_{\mathbf Q}: [K:\mathbf Q]=2,\ K\text{ 无实嵌入},\
|\operatorname{Disc}(K)|\le X,\
\dim_{\mathbf F_5}(\operatorname{Cl}(K)/5\operatorname{Cl}(K))\ge2\}.
\]

这里按 `Q`-同构类计数。对于有限阿贝尔群，条件等价于 5-primary Sylow 子群含有 `(Z/5Z)^2`；它不等价于“类数被 25 整除”。

## 主候选 `EXP-EPS`

存在固定 `δ∈Q_{>0}`，使得对每个 `ε∈R_{>0}`，存在 `c_ε>0` 与 `X_ε>1`，并且对所有 `X≥X_ε`，

\[
N^-_{5,2}(X)\ge c_\varepsilon X^{1/3+\delta-\varepsilon}.
\]

- `statementHash`: `6c6e7cf3f3128a0423dd33cc64e4bd57bbcd622caf92d96776f76158edf02d49`
- 状态：`candidate / open`
- 与计划书原意：`unknown`；若采用标准 ε-损失语义，则为 `equivalent`
- 与 Cohen–Lenstra 启发式：该启发式预测固定秩阈值具有正频率，因而远强于这里的次线性下界；本项目没有把启发式当作证明输入。

## 已知基线与较弱目标

| ID | 结论 | statementHash | 证据状态 |
| --- | --- | --- | --- |
| `BYEON-BASELINE` | `N^-_{5,2}(X) ≫ X^(1/4)` | `0a31f4b4a375e338f944fe1eab68561d79a5a3d424113d55d375a11b17123bec` | Byeon Theorem 1.1 支持 |
| `BLT-BASELINE` | `N^-_{5,2}(X) ≫ X^(1/3)/(log X)^2` | `824e395028a3a2df3d655ab1e8a32203acbc582c5458e6bfe69332f62e5f3aad` | BLT Theorem 1.3 支持 |
| `NO-LOG` | `N^-_{5,2}(X) ≫ X^(1/3)` | `234b34d918c1ce566f2aac5b9ad9f78e9c8abdb89918d4d97fecac8078a806b0` | source-supported 人工证明候选；独立审阅通过；总命题非 Lean Verified |
| `EXP-EPS` | 固定正 `δ` 的指数增益 | `6c6e7cf3f3128a0423dd33cc64e4bd57bbcd622caf92d96776f76158edf02d49` | 候选；未证明 |

逻辑关系为 `EXP-EPS ⇒ NO-LOG ⇒ BLT-BASELINE`。BLT 的 `1/3` 与 `(log X)^-2` 已在其引用的 Kulkarni–Levin 定量专门化定理中出现；不能把 BLT 搜索得到的参数、曲线或同构类数量相加成不同二次域的计数。

## 支持线与反驳线

支持线：三份 PDF 的哈希、页码与关键定理锚点已核对；七个规范化命题的 SHA-256 均可重算；Byeon 与 BLT 的两个单侧下界陈述一致。独立审阅要求修订计划书中的 “of order”、Cohen–Lenstra 固定秩限定、“current benchmark” 时间边界和 `o(1)` 量词。

反驳线：标准库精确搜索穷举所有 `-50000≤D<0` 的 15,195 个负基本判别式，找到 9 个 5-rank 至少 2 的例子；范围内首例是 `D=-11199`，其类群不变量由 PARI/GP 复算为 `[20,5]`。`D=-479` 的类群不变量为 `[25]`，因此反驳“`25|h(D)` 当且仅当 5-rank 至少 2”。有限搜索只提供声明范围内证据，不证明任何渐近结论或无界最小性。

## NO-LOG 阶段性结果

对 BLT 的显式 genus-2 曲线 `C0`，已形成 Stewart–Top 强 Theorem 1 与
Kulkarni–Levin 局部化相结合的完整人工证明候选。KL 端点有限避让与 ST
正盒 bounded-witness/thin-set 删除两个决定性接口已经过独立冻结来源审阅，
裁决为 `passed`。审阅要求显式补出的 `ψ∘φ` 复合顺序和
`u=floor(H)` 量词推导已写回主稿。

三条可分离代数小引理已取得 Lean 4.33 平台内核回执，但解析计数输入与
NO-LOG 总命题尚未整体形式化。因此本结果是 **Candidate**，不得称为
`Verified`；它也不支持 `EXP-EPS`。

## 下一条最高信息增益路线

对 BLT 的显式 genus-2 曲线 `C0`，相关次数 6 二元型已核对为 `1+1+4` 次因子，并取得模 7 无重根证书。这使 Stewart–Top 强平方自由值定理成为去掉 `(log X)^2` 的具体候选入口。

下一阶段继续绑定 `NO-LOG` 的 statementHash，将已审阅人工证明拆成 Lean
接口定理：明确哪些解析输入作为假设，认证从这些输入到最终 `X^(1/3)` 计数的
形式推导，并逐步缩小未形式化的 Stewart–Top/Kulkarni–Levin 部分。完成该门后
才回到多参数或 `D5` 扩张等 `EXP-EPS` 路线。即使 `NO-LOG` 最终成立，它也不
提供 `EXP-EPS` 的正指数增益。

## 可复现入口

- 形式命题与哈希：`mathematics/worker/formalization-intake.json`
- 独立来源审阅：`mathematics/worker/source-consistency-review.md`
- 有限反例审计：`mathematics/worker/counterexample-boundary-audit.md`
- 有限搜索重放：`python3 mathematics/worker/counterexample_finite_search.py --bound 50000`
- 路线代数检查：`python3 mathematics/worker/verify-route-audit.py`
- NO-LOG 人工证明：`mathematics/worker/strong-kl-no-log-lemma.md`
- 独立审阅：`mathematics/worker/strong-kl-no-log-local-independent-review.md`
- Lean 收据：`mathematics/verification-trace.json`
- 阶段报告：`reports/cohen-lenstra-no-log-stage.md`
