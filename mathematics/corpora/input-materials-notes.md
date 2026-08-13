# 输入材料与主张锚点

本文件只记录当前精确化阶段真正改变研究决策的来源关系；完整逐条矩阵见 `mathematics/worker/source-consistency-review.md`。

| 材料 | 决定性锚点 | 本项目中的作用 |
| --- | --- | --- |
| `Research Plan.pdf` | p.1 定义 5-rank 与 `N^-_{5,2}`；p.2 给出改进下界及 `1/3+δ-o(1)` 目标 | 固定非形式研究目标；其 `o(1)` 量词仍需保守解释 |
| `29_noncyclic_class57.pdf` | p.2 Theorem 1.1；p.7 以次数 8 二元型结束证明 | 支持虚二次域 `X^(1/4)` 下界 |
| `Counting imaginary quadratic fields with an ideal class group of 5-rank at least 2.pdf` | p.2 Theorem 1.3；p.3 Theorem 1.4；p.7 显式曲线应用 | 支持 `X^(1/3)/(log X)^2` 下界并定位 genus/专门化机制 |

计划书在正式复用前应修订四点：把 “of order” 改成单侧下界；对 Cohen–Lenstra 预测注明固定秩阈值；给 “current benchmark” 加时间戳与检索范围；把 `X^(1/3+δ-o(1))` 改成显式量词。两次定向检索只支持论文身份和有限时点观察，不能证明不存在后续结果。

BLT 的曲线搜索是存在性层；不同二次域的计数、局部条件、thin-set 排除和重数控制属于 Kulkarni–Levin 输入层。21,088 个参数、548 条曲线和 85 个同构类不能直接相加为二次域计数。
