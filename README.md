# 虚二次域 5-rank≥2 计数研究

本项目研究
\[
N^-_{5,2}(X)=\#\{[K]_{\mathbf Q}:K/\mathbf Q\text{ 为虚二次域},
|\operatorname{Disc}K|\le X,\operatorname{rk}_5\operatorname{Cl}(K)\ge2\}.
\]

## 当前结果

- 主目标 `EXP-EPS`（固定正指数增益）仍开放，statementHash 为
  `6c6e7cf3f3128a0423dd33cc64e4bd57bbcd622caf92d96776f76158edf02d49`。
- 较弱的 `NO-LOG` 命题
  \(N^-_{5,2}(X)\gg X^{1/3}\) 已形成来源支持的完整人工证明候选，
  statementHash 为
  `234b34d918c1ce566f2aac5b9ad9f78e9c8abdb89918d4d97fecac8078a806b0`。
- 两个决定性解析接口——KL 端点有限避让与 Stewart–Top 正盒
  bounded-witness/thin-set 删除——已通过独立冻结来源审阅。
- 三条可分离代数小引理，以及从显式 `AnalyticBridge` 假设到立方下界的完整
  条件推理，已有 Lean 4.33 平台 `kernel_verified` 收据。
- 独立审阅反驳了旧接口中的装饰性来源 `Prop` 对齐；修复后的纯数值定理
  `RationalCountingBridge → CubicLowerBound` 已获新平台收据
  `lean-be179a7b1c063b4bc53752a5`。来源 strong-KL 集合到三个数值义务的
  单独账本正在窄范围复审，因此总结果仍是 **Candidate**，不是 `Verified`。

## 阅读与复现

- 精确问题：[mathematics/problems/cohen-lenstra-subproblem.md](mathematics/problems/cohen-lenstra-subproblem.md)
- 阶段报告：[reports/cohen-lenstra-no-log-stage.md](reports/cohen-lenstra-no-log-stage.md)
- 人工证明候选：[mathematics/worker/strong-kl-no-log-lemma.md](mathematics/worker/strong-kl-no-log-lemma.md)
- 独立审阅：[mathematics/worker/strong-kl-no-log-local-independent-review.md](mathematics/worker/strong-kl-no-log-local-independent-review.md)
- Lean 源码：[mathematics/formal/NoLogAlgebra.lean](mathematics/formal/NoLogAlgebra.lean)
- 条件推理：[mathematics/formal/NoLogInference.lean](mathematics/formal/NoLogInference.lean)
- 条件回执：[mathematics/formal/no-log-inference-receipt.json](mathematics/formal/no-log-inference-receipt.json)
- 有理来源桥：[mathematics/formal/NoLogSourceBridge.lean](mathematics/formal/NoLogSourceBridge.lean)
- 有理来源桥回执：[mathematics/formal/no-log-source-bridge-receipt.json](mathematics/formal/no-log-source-bridge-receipt.json)
- 平台收据：[mathematics/verification-trace.json](mathematics/verification-trace.json)

最小重放命令记录在阶段报告中。当前只剩对冻结 strong-KL 集合到
`RationalCountingBridge` 三个数值义务的来源账本做独立复审；无条件 NO-LOG
statementHash 仍没有匹配内核回执。
