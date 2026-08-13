# NO-LOG 完整推理接口：Lean 重放清单

## 结论与认证边界

`NoLogInference.no_log_of_strong_kl_interface` 形式化的是一条**条件蕴含**：若
`AnalyticBridge` 中逐项列出的 Stewart–Top/Kulkarni–Levin 计数、局部化、
thin-set 删除、互异域注入与六次高度选择假设成立，则计数函数满足

```text
∃ X0 A B : Nat, 0 < A ∧ 0 < B ∧
  ∀ X ≥ X0, B * X ≤ A * (N X)^3.
```

当 `A,B>0` 时，这是 `N(X) ≫ X^(1/3)` 的无除法、无开根号版本。本文件和
Lean 源码不认证 ST/KL 的解析输入本身，也不认证 EXP-EPS。

## 稳定自然语言 statementHash

规范化文本（逐字）：

```text
FOR ALL N : Nat -> Nat AND h : AnalyticBridge N, CubicLowerBound N, where AnalyticBridge explicitly supplies fixed positive-cone congruence data A,B,M; class-wise maximal fixed square w^2; a quadratic strong squarefree-value count; a linear thin-set bound and deletion partition; injection of good values into rank-at-least-two imaginary quadratic fields; monotonic field counts; and a sixth-degree height selector.
```

SHA-256：

```text
796fae5b00f462089dce3a91b859d00069a1dd85374bc3325be27c92f19bb384
```

这不是 NO-LOG 非条件命题的 hash `234b34d9…806b0`。只有在进一步形式化并认证
`AnalyticBridge` 的构造后，才可能把后者提升为 `kernel_verified`。

权威命名定理 receipt 四元组已冻结在
`mathematics/formal/no-log-inference-receipt.json`：

- `statementHash = 796fae5b…384`；
- `theoremDeclarationHash = 869535f2…60fe`；
- `proofHash = f4d7c0ec…d564`；
- `targetCommit = 4371fcb4…41b3`。

该 manifest 来自 `lean_workspace(action="certify")` 的权威返回；通用 proof-trace
只保存事件投影，不能替代这四个身份字段。

## 精确重放

工具链：Lean `4.33.0`，导入仅 `Std.Tactic`。

```bash
lean -q -t 0 mathematics/formal/NoLogInference.lean
rg -n -i '\b(sorry|admit|axiom)\b' mathematics/formal/NoLogInference.lean
lean --deps mathematics/formal/NoLogInference.lean
```

期望：第一条退出码 `0` 且无输出；第二条无匹配；第三条只出现 Lean/Std 依赖。

## 独立审阅重点

1. `CubicLowerBound` 是否与自然语言 `N(X) ≫ X^(1/3)` 在自然数计数语境下等价；
2. `mainConstant^3 * X ≤ comparisonConstant * N(X)^3` 的常数方向是否正确；
3. `deletePartition`、`thinCountBound`、`thinIsDominated` 是否足以推出二次规模的
   `goodCount`；
4. `selectorFits` 与 `selectorCompares` 的方向是否共同编码六次判别式高度转换；
5. 接口是否清楚把解析输入作为假设，而没有把条件定理冒充 NO-LOG 非条件证明。
