# `NoLogSourceBridge` 重放与边界记录

## 命名定理

`NoLogSourceBridge.no_log_of_fixed_c0_rational_source` 把固定 `C0` 来源链压缩为
一个精确的清分母接口：对某些正整数 `p,q,D`，来源在每个充分大自然高度
`T` 给出

```text
p * T^2 <= q * goodCount(T),
goodCount(T) <= N(D * T^6).
```

并给出目标域计数单调性。四个来源级局部/几何命题仍作为显式 Prop+proof 字段
保留。Lean 内部取源高度 `T=qH`，把自然主常数变为 `p*q`、判别式常数变为
`D*q^6`，用递归构造的最大适配高度产生双边六次界，最后推出

```text
∃ X0 A B : Nat, 0 < A ∧ 0 < B ∧
  ∀ X >= X0, B * X <= A * (N X)^3.
```

## 稳定 statementHash

规范化文本（UTF-8，无末尾换行）：

```text
FOR EVERY N : Nat -> Nat, IF POSITIVE NATURALS p, q, AND D AND A THRESHOLD H0 GIVE, FOR EVERY NATURAL T >= H0, p*T^2 <= q*goodCount(T) <= q*N(D*T^6), WITH THE GOOD VALUES ARISING FROM THE EXPLICIT FIXED-C0 POSITIVE-CONE, CLASS-WISE MAXIMAL-SQUARE, BOUNDED-WITNESS, THIN-INJECTION, AND LOCAL-RANK SOURCE OBLIGATIONS, AND IF N IS MONOTONE, THEN THERE EXIST POSITIVE NATURALS A AND B AND X0 SUCH THAT FOR EVERY X >= X0, B*X <= A*(N X)^3.
```

`statementHash = cb1ee74c7c99eb77ea1b0ece80d485c4eb089bc8820675220b738e662463e4c4`。

## 平台认证

- `receiptId = lean-b450b5f91e03836f8ae94187`
- `targetCommit = 4c2bea33640112c6cb8756ee1aa243126124b056`
- `proofHash = 0f31dee1984c9d575e1ec7f9e550fb13ef25c427538e75640e88cdcf878e5009`
- `theoremDeclarationHash = 6ae30555b15cd10c8065d08f25dcaaee8c271ba4752d58c9b90451a242f2bc99`
- `status = kernel_verified`
- `goalsRemaining/sorry/admit = 0`, `axioms = []`

完整身份字段见 `no-log-source-bridge-receipt.json`；内容寻址 trace 为
`mathematics/report-traces/verification-8015df0b7d1021d26913.json`。

## 精确重放

```bash
lean -q -t 0 mathematics/formal/NoLogSourceBridge.lean
rg -n -i '\b(sorry|admit|axiom)\b' mathematics/formal/NoLogSourceBridge.lean
```

预期：Lean 退出码 `0` 且无输出；禁止 token 扫描无匹配。

## 已认证与未认证边界

本定理真实构造自然数六次根选择器并认证整个推理，不再把选择器存在性留作
外部假设。它也认证正有理常数 `p/q` 的清分母与固定高度缩放。

它仍不证明：

- Stewart--Top/Kulkarni--Levin 来源定理本身；
- 来源的正实 Vinogradov 常数存在，或从该常数选择正有理 `p/q` 的实数稠密性；
- 固定 `C0` 的来源对象定义与 `goodCount` 有限基数构造；
- 无条件 NO-LOG 或 EXP-EPS。

因此收据只绑定这条显式条件蕴含，不能绑定无条件 NO-LOG hash
`234b34d918c1ce566f2aac5b9ad9f78e9c8abdb89918d4d97fecac8078a806b0`。
