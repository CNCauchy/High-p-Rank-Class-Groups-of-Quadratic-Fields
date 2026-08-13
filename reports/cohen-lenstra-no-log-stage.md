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
`EXP-EPS` 所要求的任何正指数增益。NO-LOG 总命题尚无匹配 statementHash 的
Lean 内核回执，因此不得称为 `Verified`。

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
| SF | NO-LOG 总命题 | 上述组合，但解析输入未整体形式化 | Candidate；非 Verified |

## 支持线与反驳线

支持线包括原始来源逐页锚点、明确的强 KL 引理、独立审阅，以及三条 Lean
小引理收据。独立审阅主动测试了复合顺序、端点修正是否破坏正锥、类内 \(w\)
偷换、无界表示反推、只沿 subsequence 计数，以及 thin 参数的非单射风险；
没有出现决定性失败信号。

反驳线发现原始六次型所有整数值具有固定平方因子 4，这阻止直接声称
\(F\) 本身平方自由，但 Stewart–Top 的类内 maximal \(w^2\) 正是吸收该问题的
接口。归一化后的局部检查覆盖坏素数以及 \(p\le43\)，有界碰撞实验覆盖
\(H\le200\) 的 24,463 个参数；这些有限结果只说明没有发现即时障碍，不能替代
渐近证明。

## Lean 验证边界

平台 Lean 4.33 认证了三条命名定理：

- `NoLogAlgebra.c0_explicit_factor_expansion`；
- `NoLogAlgebra.exists_large_nat_avoiding_finite_endpoints`；
- `NoLogAlgebra.degree_six_homogeneous_scaling_is_nonzero_square_multiple`。

三条检查均有 0 个开放目标、0 个 `sorry`、0 个 `admit` 和 0 个项目自设
axiom。它们不认证 Stewart–Top 或 Kulkarni–Levin 的解析定理，也不认证
NO-LOG 总命题。

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
python3 -m json.tool mathematics/verification-trace.json >/dev/null
```

## 下一步

最高信息增益的后续不是继续搜索曲线，而是建立 NO-LOG 的 Lean 接口蓝图：
把 Stewart–Top 和 Kulkarni–Levin 当作明确声明的解析输入，先认证从这些输入到
最终 \(X^{1/3}\) 计数结论的形式推导；随后再逐步形式化或外部复核这些解析输入。
在取得匹配 NO-LOG statementHash 的内核回执和完整独立审查之前，结论保持
Candidate。
