# `NoLogBridge` 重放与边界记录

## 结论

`NoLogBridge.no_log_of_fixed_c0_post_deletion_bridge` 是一个自包含的
Lean 4/Std 条件定理。它证明：若固定 `C0` 路线已经给出删去 thin set
后的二次规模 good-value 计数、到目标虚二次域的注入、域计数单调性，
以及同一个六次高度选择器的双边不等式，则得到根号自由形式的三次
下界

```text
∃ X0 A B : Nat, 0 < A ∧ 0 < B ∧
  ∀ X ≥ X0, B * X ≤ A * (N X)^3.
```

文件内的 `NoLogBridge.CubicLowerBound` 与已获收据的
`NoLogInference.CubicLowerBound` 定义逐字同型；重复定义只为让本文件
不依赖未配置的项目模块路径而可独立认证。

## 稳定自然语言 statementHash

规范化文本（UTF-8，计算哈希时不附加换行）：

```text
FOR EVERY N : Nat -> Nat, IF THERE EXISTS A FIXED-C0 POST-DELETION BRIDGE WITH A POSITIVE NATURAL QUADRATIC GOOD-VALUE CONSTANT, AN INJECTION OF GOOD VALUES INTO THE DESIRED FIELD COUNT AT SIXTH-DEGREE DISCRIMINANT HEIGHT, MONOTONICITY OF THAT FIELD COUNT, AND ONE TWO-SIDED SIXTH-DEGREE HEIGHT SELECTOR, THEN THERE EXIST POSITIVE NATURAL CONSTANTS A AND B AND A THRESHOLD X0 SUCH THAT FOR EVERY X >= X0, B * X <= A * (N X)^3.
```

`statementHash = 15f96ab0d2ebb841449247742018013b767961c9cea4bdfc000e1e6b1084d99b`。
该值由上述字节串直接重算，不含代码围栏与末尾换行。

## 精确重放

```bash
lean -q -t 0 mathematics/formal/NoLogBridge.lean
rg -n -i '\b(sorry|admit|axiom)\b' mathematics/formal/NoLogBridge.lean
```

预期结果：Lean 退出码 `0` 且无输出；禁止占位符/项目自设公理扫描无匹配。

## 已证与未证边界

已由本文件内核检查的只是上述组装蕴含。以下均未由本文件证明：

- Stewart--Top 的平方自由值定理；
- Kulkarni--Levin 的局部化与 thin-set 定理；
- 任意正实主项常数到正自然数二次常数的高度缩放；
- 六次高度选择器的具体构造；
- 固定 `C0` 的整个桥接结构存在；
- 无条件 NO-LOG 命题或 EXP-EPS 命题。

特别地，来源下界 `#T_H >= c H^2` 中的 `c>0` 一般不能在同一高度
直接改写成原 `AnalyticBridge` 的 `2*m*H^2`（`m : Nat`, `m>0`）。
需要先固定缩放 `L`，在来源高度 `L*H` 计数，并同步把判别式高度常数
乘以 `L^6`。该义务记录在
`mathematics/worker/no-log-analytic-bridge-matrix.json` 的 `B-NORM-1`。
