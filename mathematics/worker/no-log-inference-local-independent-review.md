# NO-LOG Lean 条件接口的本地冻结独立审阅

## 裁决

**changes_requested。** `NoLogInference.lean` 的机械语义审阅本身全部通过：

- `CubicLowerBound` 的常数方向正确，确实编码自然数计数语境下的立方根下界；
- `good_count_lower_bound` 的四个不等式足以推出二次规模的 `goodCount`；
- `selectorFits`、单调性、`goodInjectsIntoFields` 与 `selectorCompares` 的方向正确；
- 证明结论严格是 `AnalyticBridge N → CubicLowerBound N` 的条件蕴含，没有构造 `AnalyticBridge`，因而没有认证无条件 NO-LOG。

但 acceptance 要求的 receipt 身份四元组无法从获准的冻结三文件完全核验。receipt
`lean-deb15db5d3c3746d573dba4f` 所在 trace 记录了 whole-file
`proofHash=f4d7c0ec…d564`、`bytes=6552`、theoremName、kernel 状态和 exit code；文件字节与它精确匹配。replay 的规范文本也独立重算得到
`statementHash=796fae5b…384`。然而该 receipt session 没有持久化
`statementHash`、`theoremDeclarationHash` 或 `targetCommit` 字段。因此目前只能确认“冻结证明文件经过 kernel check”和“replay 声称的条件命题 hash 可重算”，不能确认 receipt 本身绑定了要求的 statement/declaration/commit 身份。

这是 receipt manifest 的可修复证据缺口，不是 Lean 算术证明的反例。修复后若三个字段与冻结源一致，语义裁决可升级为 `passed`；在此之前不应把该 receipt 用作完整命题身份认证。

## 冻结范围

只读取以下 Git 冻结材料，未联网、未读 PDF、未重审 Stewart–Top/Kulkarni–Levin 来源：

| 路径 | Git blob | SHA-256 | 用途 |
| --- | --- | --- | --- |
| `mathematics/formal/NoLogInference.lean` | `ba15cf14beff584fca7559d8869b9fa043d78c32` | `f4d7c0ecdac058a7b351eecea2ddb1513707d9584be954fbf6c20af974d6d564` | 被审定理、接口与 proof bytes |
| `mathematics/formal/no-log-inference-replay.md` | `e66282c99e2deb094a85a3a132a7b960763cb5ed` | `587ef94cd3c8bba020de784a2df59c0257ce44f5bdab5e8c9da2b45b341db5f2` | 规范 statement 文本、预期 hash 与认证边界 |
| `mathematics/verification-trace.json` | `97028c757fa797e39666a8dab844487ebd3a501c` | `b4e3dba3ae390775b624295fd0b5dbbe43c427f65a0e52f42f8c0d955c74c503` | canonical receipt trace |
| `mathematics/report-traces/verification-b4e3dba3ae390775b624.json` | `97028c757fa797e39666a8dab844487ebd3a501c` | `b4e3dba3ae390775b624295fd0b5dbbe43c427f65a0e52f42f8c0d955c74c503` | replay manifest；与 canonical trace 逐字相同 |

worktree 起点为
`06b4b50872de896a27d5c7a1ed0a4c37dd0fbc8c`；proof source 来自其父提交
`4371fcb4ede90c2e981b634d847b8b04c3cd41b3`，且从该提交到 base 的
`NoLogInference.lean` 与 replay 无 diff。冻结 checkpoint 的提交文字声称 receipt 认证目标为
`4371fcb4…41b3`，但这不是 trace 内 `targetCommit` 字段，不能替代 receipt 绑定。

## 1. `CubicLowerBound` 与常数方向

源码 `:21–25` 定义

\[
\exists X_0,A,B\in\mathbf N,quad A,B>0,quad
\forall X\ge X_0,quad B X\le A N(X)^3.
\]

对正实数解释，取立方根得到

\[
N(X)\ge (B/A)^{1/3}X^{1/3}.
\]

所以 `B` 位于 `X` 一侧、`A` 位于 `N³` 一侧是正确方向；交换两者仍会是某个正常数下界，但必须与构造所给实例一致。定理 `:133–134` 选择

\[
A=\texttt{comparisonConstant},qquad
B=\texttt{mainConstant}^3.
\]

在 `:150–166` 中，`selectorCompares` 给

\[
X\le C H^6,
\]

而计数链给 `mH²≤N(X)`，所以

\[
m^3X\le m^3 C H^6=C(mH^2)^3\le C N(X)^3.
\]

这正是 `B X≤A N³`，其中 `B=m³`、`A=C`。`mainConstantPositive` 与
`comparisonConstantPositive` 确保两者正；自然数乘方不会引入除法或取根语义漏洞。

**义务 1：passed。** 这是自然数上的 root-free 渐近编码；源码没有声称已经给出实分析版本的显式根常数。

## 2. `good_count_lower_bound` 的四个不等式

令 `m=mainConstant`。源码 `:81–94` 的四项是：

1. `2(mH²) ≤ raw`；
2. `thin ≤ thinConstant·H`；
3. `thinConstant·H ≤ mH²`；
4. `raw ≤ good+thin`。

链式相加得

\[
2mH^2\le raw\le good+thin\le good+mH^2,
\]

从而 `mH²≤good`。`deletePartition` 方向尤其正确：若 raw objects 被分成 good 与被删 thin 的覆盖，则需要 `raw≤good+thin`；反向 `good+thin≤raw` 单独不足以给下界。由于三项均为自然数，`omega` 对该线性组合有效，乘方 `H²` 在局部被视为固定自然数项，不需要非线性推理。

**义务 2：passed。** 四项恰好足够；`thinCountBound` 和
`thinIsDominated` 缺一都会使结论无从推出。

## 3. 选择器、单调性与 good-to-field 注入方向

源码 `:97–112` 与证明 `:136–151` 的方向如下：

- `goodCount H ≤ N(D·H⁶)`：不同 good values 注入所需域，故域数至少为 good 数；方向正确。
- `D·H⁶ ≤ X` (`selectorFits`) 与 `N` 单调，推出 `N(D·H⁶)≤N(X)`；方向正确。
- `X≤C·H⁶` (`selectorCompares`) 防止 selected height 过小，和 `mH²≤N(X)` 合成立方关系；方向正确。
- `H0≤selectedHeight X` 保证所有渐近盒假设可调用。

`selectorFits` 与 `selectorCompares` 共同把 `H⁶` 夹在 `X` 的固定常数尺度内。只保留前者会给场落入高度 `X`，却不能从 `H²` 推出 `X^{1/3}`；只保留后者则无法保证已计场的判别式不超过 `X`。

接口中四个 source-level Prop 都配有证明字段，但这只使 `AnalyticBridge` 的实例携带它们；Lean 文件没有构造该实例，也没有从这些抽象 Prop 推出数值字段。数值字段本身仍是明确的条件假设。

**义务 3：passed。** good-to-field、monotonicity 和两个 selector 不等式没有反向。

## 4. receipt、hash 与冻结字节对齐

确定性重放得到：

| 项 | 观察 | 裁决 |
| --- | --- | --- |
| receipt ID | `lean-deb15db5d3c3746d573dba4f` | trace 中存在 |
| theorem | `NoLogInference.no_log_of_strong_kl_interface` | 与源码命名一致 |
| status / exit | `kernel_verified` / `0` | trace 中存在 |
| proof bytes | `6552` | 当前文件与 trace 一致 |
| proofHash | `f4d7c0ec…d564` | 当前 SHA-256 与 trace 一致 |
| statementHash | 规范文本重算 `796fae5b00f462089dce3a91b859d00069a1dd85374bc3325be27c92f19bb384` | replay 一致；receipt session **无字段** |
| theoremDeclarationHash | reviewer 对 `theorem …` 至 `end namespace` 前的冻结切片计算 `b9fa1458…832` | 仅为审阅者定义的切片 hash；receipt session **无权威字段/规范**，不可宣称对齐 |
| targetCommit | checkpoint/replay 上下文指向 `4371fcb4…41b3` | receipt session **无字段**，不可宣称绑定 |

canonical trace 与 report trace 逐字相同，因此缺失不是两个副本不一致。冻结 trace 的
`file.opened` event 绑定 whole-file proof bytes；`receipt.published` event 只给 receiptId、checkId、proofPath、theoremName 与 status。全 session 搜索确认
`statementHash=false`、`theoremDeclarationHash=false`、`targetCommit=false`、
`proofHash=true`。

**义务 4：changes_requested。** 需从 verifier 导出并冻结含
`statementHash=796f…384`、权威 `theoremDeclarationHash`、
`proofHash=f4d7…d564` 与 `targetCommit=4371fcb4…41b3`（若这确为认证目标）的 receipt manifest。不得用 commit message 或审阅者自定切片 hash 冒充 receipt 字段。

## 5. 条件/非条件认证边界

定理类型是

```lean
{N : Nat → Nat} → AnalyticBridge N → CubicLowerBound N
```

所以 kernel receipt 最多认证：“给定一个包含所有列出假设的 `AnalyticBridge N` 实例，算术/计数推理得到 cubic lower bound。”它不认证：

- 存在任何 `AnalyticBridge N` 实例；
- ST/KL 解析计数、thin-set 删除、局部秩或六次 height selector；
- 无条件 NO-LOG statementHash `234b34d9…806b0`；
- `EXP-EPS`；
- 先前三条小代数引理之外的解析 theorem。

因此 `statementHash=796f…384` 与无条件 NO-LOG hash 必须隔离。即便 receipt manifest 补全，此定理也只能标为**conditional inference kernel verified**，不能把 `AnalyticBridge` 构造或无条件 NO-LOG 标为 kernel verified。

**义务 5：passed，边界明确。** replay `:5–15,31–32` 与源码注释 `:6–8,125–128` 都准确说明了这一区别。

## issue list 与证伪结局

| ID | 严重性 | issue | 所需修复 |
| --- | --- | --- | --- |
| R1 | blocking for receipt identity acceptance | receipt session 缺 `statementHash` | 冻结 verifier 权威字段 `796f…384` |
| R2 | blocking for receipt identity acceptance | receipt session 缺 `theoremDeclarationHash` | 用 verifier 的声明规范化规则导出并冻结，不采用审阅者切片 hash |
| R3 | blocking for receipt identity acceptance | receipt session 缺 `targetCommit` | 冻结实际认证 commit，预期需核对 `4371fcb4…41b3` |
| S1 | passed | `CubicLowerBound` 常数方向 | 无修改 |
| S2 | passed | good count 四不等式 | 无修改 |
| S3 | passed | selector/单调/注入方向 | 无修改 |
| S4 | scope guard | receipt 只能认证条件蕴含 | 报告中始终保留 conditional 标签 |

**falsification outcome: refuted（针对完整 acceptance 假设）。** “冻结三文件足以核对 receipt 的 statement/declaration/proof/commit 四元组”被 R1–R3 精确反驳。相反，“Lean 条件蕴含的机械语义正确”在全部方向与边界测试中 survived。

修复后的最便宜复核：读取新增的权威 receipt manifest，核对四字段，并确认
`NoLogInference.lean` blob/bytes 未变；不需要修改或重跑数学证明。

## 重放

完整确定性输出保存于
`mathematics/worker/no-log-inference-local-independent-replay.txt`。关键命令：

```bash
lean -q -t 0 mathematics/formal/NoLogInference.lean
python3 -m json.tool mathematics/verification-trace.json >/dev/null
cmp mathematics/verification-trace.json \
  mathematics/report-traces/verification-b4e3dba3ae390775b624.json
git diff --check
```
