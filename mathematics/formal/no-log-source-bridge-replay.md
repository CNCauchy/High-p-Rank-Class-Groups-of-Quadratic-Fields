# `NoLogSourceBridge` 重放与边界记录

## 命名定理

`NoLogSourceBridge.no_log_of_rational_counting_bridge` 是一个纯数值的
清分母接口：对某些正整数 `p,q,D`，在每个充分大自然高度
`T` 给出

```text
p * T^2 <= q * goodCount(T),
goodCount(T) <= N(D * T^6).
```

并给出目标域计数单调性。Lean 内部取源高度 `T=qH`，把自然主常数变为
`p*q`、判别式常数变为
`D*q^6`，用递归构造的最大适配高度产生双边六次界，最后推出

```text
∃ X0 A B : Nat, 0 < A ∧ 0 < B ∧
  ∀ X >= X0, B * X <= A * (N X)^3.
```

## 稳定 statementHash

规范化文本（UTF-8，无末尾换行）：

```text
FOR EVERY N : Nat -> Nat, IF POSITIVE NATURALS p, q, AND D AND A THRESHOLD H0 GIVE, FOR EVERY NATURAL T >= H0, p*T^2 <= q*goodCount(T) AND goodCount(T) <= N(D*T^6), AND IF N IS MONOTONE, THEN THERE EXIST POSITIVE NATURALS A AND B AND X0 SUCH THAT FOR EVERY X >= X0, B*X <= A*(N X)^3.
```

`statementHash = a191d05bf703dfe1d019f7d1467d67552cdb01c2c1decb88b02a75277c14a20f`。

## 平台认证状态

新定理正在等待冻结提交后的平台认证。历史收据
`lean-b450b5f91e03836f8ae94187` 只认证已被独立审阅否定为过宽对齐的旧声明
`NoLogSourceBridge.no_log_of_fixed_c0_rational_source`，不得用于当前命名定理。

`no-log-source-bridge-receipt.json` 和内容寻址 trace 将在新收据取得后更新；在此之前
当前状态仅为本地 Lean 重放通过，不称平台 `kernel_verified`。

## 精确重放

```bash
lean -q -t 0 mathematics/formal/NoLogSourceBridge.lean
rg -n -i '\b(sorry|admit|axiom)\b' mathematics/formal/NoLogSourceBridge.lean
```

预期：Lean 退出码 `0` 且无输出；禁止 token 扫描无匹配。

## 已认证与未认证边界

本定理真实构造自然数六次根选择器并认证整个**纯数值推理**，不再把选择器
存在性留作外部假设。它也认证正有理常数 `p/q` 的清分母与固定高度缩放。

它仍不证明：

- Stewart--Top/Kulkarni--Levin 来源定理本身；
- 来源的正实 Vinogradov 常数存在，或从该常数选择正有理 `p/q` 的实数稠密性；
- 固定 `C0` 的来源对象定义、正锥、类内 maximal `w`、bounded witness、
  thin/rank 结论与 `goodCount` 有限基数构造；
- 无条件 NO-LOG 或 EXP-EPS。

因此收据只绑定这条显式条件蕴含，不能绑定无条件 NO-LOG hash
`234b34d918c1ce566f2aac5b9ad9f78e9c8abdb89918d4d97fecac8078a806b0`。
