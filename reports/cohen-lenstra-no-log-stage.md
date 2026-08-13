# NO-LOG 阶段报告：来源支持的证明候选

## 结论与范围

当前成果的准确状态是 **Candidate**：对
\[
N^-_{5,2}(X)\gg X^{1/3}
\]
已经形成一条来源支持、可重放且经独立冻结来源审阅通过的人工证明链。其
statementHash 为
`234b34d918c1ce566f2aac5b9ad9f78e9c8abdb89918d4d97fecac8078a806b0`。

这比 Bartz–Levin–Thamminana 的
\(X^{1/3}/(\log X)^2\) 下界去掉了对数损失，但没有给出
`EXP-EPS` 所要求的任何正指数增益。当前已有一个匹配冻结提交的 Lean 内核
回执，认证显式条件接口
`AnalyticBridge N → CubicLowerBound N`；它不构造 `AnalyticBridge`，也不绑定
无条件 NO-LOG 的 statementHash，因此 NO-LOG 总命题仍不得称为 `Verified`。

本阶段又得到更贴近来源的接口：平台回执
`lean-b450b5f91e03836f8ae94187` 认证
`FixedC0RationalSource N → CubicLowerBound N`。该定理用正整数 `p,q` 表示
来源正有理主项常数，内核完成清分母、源高度 `qH` 重索引、判别式常数乘
`q^6`、离散最大六次根选择器与最终三次不等式。它仍把 Stewart–Top/
Kulkarni–Levin 的来源计数与域注入作为显式外部输入。

## 论证依赖图

1. BLT 的显式 genus-2 曲线 \(C_0\) 提供 Jacobian 5-rank 2 的几何输入。
2. 相应六次二元型的射影因子次数为 \(1+1+4\)，可分且满足
   Stewart–Top 强 Theorem 1 的次数门槛。
3. Kulkarni–Levin Lemma 3.1 的自由充分大参数可有限避开两个分支端点；
   正确顺序为
   \(s=(\psi\circ\phi)(P)=a/b\)、\(\phi(P)=\tau(a/b)\)。
4. 对最终固定同余类使用其**类内** maximal fixed square \(w^2\)；
   不能把全局有限证书的 \(w=2\) 偷换到该类。
5. Stewart–Top pp.952–953 在同一正盒中给出 \(\gg H^2\) 个不同的
   squarefree \(t=F(a,b)/w^2\)，且每个 \(t\) 有盒内有界 witness。
6. Kulkarni–Levin 的 thin set 在高度 \(O(H)\) 内只有 \(O(H)\) 个参数；
   signed squarefree 类的单射使删除仍保留 \(\gg H^2\) 主项。
7. 六次高度界给 \(|\operatorname{Disc}K_t|=O(H^6)\)，从而得到
   \(\gg X^{1/3}\) 个互异虚二次域。

## 证据矩阵

| 步骤 | 可检查结论 | 证据 | 状态 |
| --- | --- | --- | --- |
| S0 | NO-LOG 定义、量词和 hash 固定 | `formalization-intake.json` | formalized |
| S1 | \(C_0\) 因子展开、可分性、次数模式 | `verify-route-audit.py`、PARI 重放 | reproduced |
| S2 | 固定平方边界与局部可行类 | `no-log-local-certificate.md`、`no-log-obstruction-audit.md` | reproduced/bounded |
| S3 | 强 KL/ST 人工证明链闭合 | `strong-kl-no-log-lemma.md` | source-supported candidate |
| S4 | 两个决定性量词接口 | `strong-kl-no-log-local-independent-review.md` | independent review passed |
| S5 | 三条可分离代数小引理 | `NoLogAlgebra.lean`、`verification-trace.json` | 3/3 kernel_verified |
| S6 | 显式解析假设到立方下界的完整推理 | `NoLogInference.lean` | conditional inference kernel_verified |
| S7 | S6 的常数、注入、单调性和选择器方向 | `no-log-inference-local-independent-review.md` | semantic review passed；回执字段缺口已由权威 manifest 修复 |
| S8 | 正有理常数清分母、固定缩放与六次选择器 | `NoLogNormalization.lean`、4 个平台收据 | 4/4 kernel_verified |
| S9 | 固定 C0 有理来源接口到三次下界 | `NoLogSourceBridge.lean`、`lean-b450b5f…` | conditional kernel_verified；来源实例化待独立审阅 |
| SF | NO-LOG 总命题 | S0–S9，但 ST/KL 到 `FixedC0RationalSource` 的最终来源对齐尚在审阅 | Candidate；非 Verified |

## 支持线与反驳线

支持线包括原始来源逐页锚点、明确的强 KL 引理、独立审阅、三条 Lean
小引理收据，以及完整条件推理的命名定理收据。独立审阅主动测试了复合顺序、端点修正是否破坏正锥、类内 \(w\)
偷换、无界表示反推、只沿 subsequence 计数，以及 thin 参数的非单射风险；
没有出现决定性失败信号。

反驳线发现原始六次型所有整数值具有固定平方因子 4，这阻止直接声称
\(F\) 本身平方自由，但 Stewart–Top 的类内 maximal \(w^2\) 正是吸收该问题的
接口。归一化后的局部检查覆盖坏素数以及 \(p\le43\)，有界碰撞实验覆盖
\(H\le200\) 的 24,463 个参数；这些有限结果只说明没有发现即时障碍，不能替代
渐近证明。

## Lean 验证边界

平台 Lean 4.33 认证了三条局部代数命名定理：

- `NoLogAlgebra.c0_explicit_factor_expansion`；
- `NoLogAlgebra.exists_large_nat_avoiding_finite_endpoints`；
- `NoLogAlgebra.degree_six_homogeneous_scaling_is_nonzero_square_multiple`。

三条检查均有 0 个开放目标、0 个 `sorry`、0 个 `admit` 和 0 个项目自设
axiom。它们不认证 Stewart–Top 或 Kulkarni–Levin 的解析定理，也不认证
NO-LOG 总命题。

此外，平台回执 `lean-deb15db5d3c3746d573dba4f` 认证了
`NoLogInference.no_log_of_strong_kl_interface`：在固定正锥同余类、类内
maximal \(w^2\)、二次强计数、线性 thin-set、good-to-field 注入、单调性及
六次高度选择器全部显式给出的前提下，推出

\[
\exists X_0,A,B>0\ \forall X\ge X_0,\quad B X\le A N(X)^3.
\]

回执四元组冻结在 `no-log-inference-receipt.json`：条件 statementHash 为
`796fae5b…384`，声明 hash 为 `869535f2…0fe`，proof hash 为
`f4d7c0ec…564`，target commit 为 `4371fcb4…1b3`。独立审阅确认全部机械语义
方向正确；其发现的唯一证据缺口是通用 trace 未保存三个身份字段，现已由
权威 verifier manifest 补齐。这个修复不构成 `AnalyticBridge` 的存在证明。

平台回执 `lean-b450b5f91e03836f8ae94187` 进一步认证了
`NoLogSourceBridge.no_log_of_fixed_c0_rational_source`。其冻结 statementHash 为
`cb1ee74c…e4c4`，proof hash 为 `0f31dee1…5009`，target commit 为
`4c2bea33…b056`，且 0 goals/sorry/admit/axioms。该收据覆盖清分母与选择器的
构造，但不认证来源的具体 `goodCount` 集合或 ST/KL 定理。

## 重放

```bash
python3 mathematics/worker/verify-route-audit.py
python3 mathematics/worker/check_no_log_local_certificate.py \
  | diff -u mathematics/worker/no-log-local-certificate-output.txt -
python3 mathematics/worker/search_no_log_obstructions.py \
  > /tmp/no-log-obstruction-output.txt
cmp /tmp/no-log-obstruction-output.txt \
  mathematics/worker/no-log-obstruction-output.txt
lean -q -t 0 mathematics/formal/NoLogAlgebra.lean
lean -q -t 0 mathematics/formal/NoLogInference.lean
lean -q -t 0 mathematics/formal/NoLogNormalization.lean
lean -q -t 0 mathematics/formal/NoLogSourceBridge.lean
python3 -m json.tool \
  mathematics/formal/no-log-inference-receipt.json >/dev/null
python3 -m json.tool mathematics/verification-trace.json >/dev/null
```

## 下一步

常数归一化和高度选择器已经不再是接口阻塞。最高信息增益的下一步是完成正在
运行的冻结独立审阅：逐字段确认 strong-KL 中的 post-deletion 集合
`T_H` 在选定固定 `p,q,D,H0` 后就是 `FixedC0RationalSource.goodCount`，并且域
注入与同一高度界一致。只有该来源实例化门也通过，才可能把条件回执与无条件
NO-LOG statementHash 连接起来；在此之前结论保持 Candidate。
