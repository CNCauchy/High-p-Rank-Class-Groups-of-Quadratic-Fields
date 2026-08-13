# 强 KL 引理的本地冻结来源独立审阅

## 裁决

**passed（限于本次两个闭合点；非 Lean Verified）。** 对冻结提交
`bab963ed21c9dcab7483bbca74f8273ab2cf4297` 的
`mathematics/worker/strong-kl-no-log-lemma.md`，本地冻结材料足以支持：

1. KL Lemma 3.1 中的自由参数 `N1` 可在固定原来的全部有限/实局部邻域之后，再避开两个射影端点命中分支除子的有限异常集；正确的复合顺序是先以 `phi` 表示原局部参数，再对其施加 `psi`，即新参数为 `psi∘phi`，因此原参数满足 `phi(P)=tau(a/b)`，其中 `tau=psi^{-1}`。这保留同一个正锥和固定同余类，并使变换后的六次型首尾系数非零，不必调用 ST p.951 的后置坐标修正。
2. ST printed p.952 的正盒集合 `T` 与 p.953 的 (10)–(15) 确实从同一批 `1≤a,b≤u` 的表示对计数**不同的** `t=F(a,b)/w²`；每个被计 `t` 因而带有该盒中的 witness。结论对每个充分大整数 `u` 成立；以 `u=floor(H)` 并缩小常数，即得到冻结稿所写“每个充分大实数 `H`”的全称量词。于是每个 `t` 可选高度 `O(H)` 的参数，KL Lemma 3.2 的 thin set `O(H)` 删除方向合法。

本裁决只绑定
`NO-LOG statementHash = 234b34d918c1ce566f2aac5b9ad9f78e9c8abdb89918d4d97fecac8078a806b0`。
它不外推 `EXP-EPS`，也没有解析定理的 Lean kernel receipt。

## 冻结边界、实际本地路径与哈希

本轮没有 web 搜索、远程下载或大范围历史扫描。worktree 起点和待审提交均为
`bab963ed21c9dcab7483bbca74f8273ab2cf4297`；起始树干净。以下是实际读取且改变裁决的本地冻结文件：

| 本地路径 | SHA-256 / Git blob | 作用 |
| --- | --- | --- |
| `mathematics/worker/strong-kl-no-log-lemma.md` | `3fe2e8f755594821bababae2763049037beee0033b0d6c817a1b8e86c65f58c6` / `9e2e99c99a33f0f122f08d47ab2f69a45b3e0634` | 被审对象；KL/ST 两个新闭合点的精确声称 |
| `mathematics/worker/strong-kl-no-log-source-matrix.json` | `7469dccb986c07644516465881664932deb1710c8a0effe5aeb38ee669957acb` / `258b0f96644893595802b9dc010c2b2ece42c721` | 冻结来源版本、页码锚点、A7/A9/A10/A12 账本 |
| `mathematics/worker/no-log-independent-replay.txt` | `fd0877f1635d6c3681b3b13b467d4b71f3ab1665ffcfffd5bfc837d2b7b0e3a0` / `75e27917bcd9e259f0f0e6f67f2c5fc490bf0fef` | 已冻结的 KL p.6 与 ST pp.948–954 来源摘录/重放记录 |
| `mathematics/worker/no-log-independent-applicability-review.md` | `3a201841da10c05912ee2ea84bb3daa90445ea6300d5f111fa456c7136086036` / `35e01d3974de20b587be730b60b616684485329a` | 先前审阅中的 O2/O4/O5/O6/O7 锚点，作为待独立挑战材料 |
| `mathematics/worker/no-log-obstruction-audit.md` | `688ee6523a3ff55f530300ec02c7f38ec76b1e3fde7e83e26bb9fd805cef4529` / `b4d6d7c8f1335e58820b0b654f1797c6f138b822` | 固定平方、零首项和正锥的反驳材料 |
| `mathematics/worker/no-log-obstruction-output.txt` | `25629a4921ab85bc07f5348a85a596322ee19c9325c397bad4a7a943ca2641c5` / `337b8f787c7ed6ef1622742bc3a0606fdc5f2490` | `w=2` 全局边界及端点值的确定性输出 |
| `mathematics/worker/verify-route-audit.py` | `f689861c7bd94243837dbebf7b28edd258c832095309e38ebc850f7ac5ba9d9e` / `45992bfb8780cf8cd3138816676ffd94d86cbb91` | 主分支 C0 分解/无重根脚本 |
| `mathematics/worker/formalization-intake.json` | `89c4a79392f0de335f790f7b003fc34338fd9ab37dc91f2a1ce39eef73fb215f` / `a5d2508379d4417c62c24e0a399d90d7afcee202` | NO-LOG 规范文本与 hash |

本地 BLT PDF
`Counting imaginary quadratic fields with an ideal class group of 5-rank at least 2.pdf`
的 SHA-256 为
`1b63f04fa1daad0c16a76474bfdd91f7b8ffab01bfd1c55a550b2db75b82539b`；本任务的两个新闭合点并不依赖重读其余页面。KL 与 ST 的冻结来源哈希分别为
`26a9e645b55d70a253be2017cc8d656be188ed9c02350c21884286c60b015aae`
和
`96fb376bf0d8a4d3b70338a89b630a5e26c3cb0354be90da8cf2224d2603ba97`；当前 Git 树不含这两个 PDF 文件，本轮实际依据是上述已提交、带哈希与逐页锚点的本地冻结摘录/重放文件，没有声称重新直接读取缺席的 PDF。

## 闭合点一：KL p.6 的 `N1`、复合顺序与端点避让

### 冻结文字/公式锚点

- `strong-kl-no-log-lemma.md:116–124` 将 KL Lemma 3.1 p.6 的自由度记录为：取任意充分大的整数 `N1>1`，
  \[
  \psi(q)=\frac{1-N_1q}{1+N_1q},\qquad
  \tau(s)=\frac{1-s}{N_1(1+s)}=\psi^{-1}(s),
  \]
  再取 `A=B=1`，以及被所有有限地方的充分高 prime powers 整除的固定 `M`；正整数 `a,b` 且 `a≡A, b≡B (mod M)` 落入全部指定局部邻域。
- 同文件 `:126–135` 明确删除端点异常：
  \[
  g(-N_0/M_0+1/N_1)g(-N_0/M_0-1/N_1)\ne0.
  \]
  这里 `tau(0)=1/N1`、`tau(∞)=-1/N1`，故这正是两个射影端点不落到原分支除子的条件。
- 本地冻结 replay `no-log-independent-replay.txt:95–103` 把 KL p.6 Lemmas 3.1–3.2 的接口记录为：一个 `PGL2(Q)` 变换把全部固定局部邻域编码为正同余类，并在选择 bounded witnesses 后删除高度受控的 thin 参数。

### 独立核对

复合顺序必须写清。原来的局部函数是 `phi=u+N0/M0`；Lemma 3.1 对其值施加 `psi`，所以送入正同余参数的是

\[
s=(\psi\circ\phi)(P)=a/b,
\quad\text{从而}\quad
\phi(P)=\tau(a/b),
\quad
u(P)=\tau(a/b)-N_0/M_0.
\]

这与冻结稿 `:137–146` 的型恒等式

\[
g(\tau(X/Y)-N_0/M_0)=F(X,Y)R(X,Y)^2
\]

一致。若把复合误写为 `phi∘psi` 或令 `tau` 后再接 `phi`，则端点公式与局部邻域都不再对应；冻结稿的**公式**顺序正确，只是 prose 应以上式消除歧义。

局部量词为：先固定有限地方集合、邻域与误差阈值；存在阈值 `N*`，所有充分大的整数 `N1` 均可用于 Lemma 3.1。对固定可分五次 `g`，每个方程

\[
g(-N_0/M_0\pm1/N_1)=0
\]

对正整数 `N1` 只有有限多个解（事实上每个分支根至多给一个相应 `N1`）。因此可从仍然无限的 `N1>N*` 中避开它们；然后才固定 `psi,tau`，再选有限地方模数 `M`。该额外删除不改变已由“`N1` 充分大”保证的有限或实局部条件。

对正 `a,b`，`s=a/b>0`，而 `tau(s)` 位于 `(-1/N1,1/N1)`；因此原来的实局部邻域/目标符号保持。有限处由 `a≡b≡1 (mod M)` 保持。端点避让使变换后分支型在 `[0:1]` 与 `[1:0]` 都非零，所以首尾系数非零；无需在 ST p.951 再作可能移动正锥的 `SL2(Z)` 变换。

**闭合点一裁决：passed。** 失败信号“端点避让必须在 `N1` 固定后修改 `M` 或破坏某个地方邻域”没有出现。

## 闭合点二：ST pp.951–953 的计数对象、有界 witness 与全称量词

### 冻结文字/公式锚点

- `strong-kl-no-log-lemma.md:149–153` 依 ST printed p.948 定义**所选同余类内**最大的 `w`，并指出 Theorem 1 直接筛 `F(a,b)/w²`；不能把另一参数空间中的全局数值 `w=2` 偷换为该类内 `w`。
- 同文件 `:155–163` 记录 ST printed p.952 的 `T`：`1≤a,b≤u`、固定同余、且 `F(a,b)/w²` squarefree；p.953 的 equations (10)–(15) 从同一个 `T` 推出至少 `C21 u²` 个**不同值**，并用
  \[
  |F(a,b)|\le rH_Fu^r
  \]
  转为 `R2(x)` 的下界。
- `no-log-independent-replay.txt:107–116` 独立冻结了同一锚点：p.948 的 `w,R_k`；pp.950–951 的强 Theorem 1；pp.951–954 的证明从 `1≤a,b≤u` 的固定同余对产生不同值；p.954 才是有 `log²` 损失的 Theorem 2。

### 独立核对

ST 的 theorem statement 中 `R2(x)` 只要求某处有表示，单独引用它不足以给 bounded witness。这里需要而且确实使用 proof-level 方向：先在正盒 `T(u)` 中构造表示对，再由 (10)–(15) 除去坏对并控制同值表示的重数，最终得到至少 `C21 u²` 个不同的

\[
t=F(a,b)/w^2,
\qquad 1\le a,b\le u.
\]

所以对每个这些 `t`，至少保留一个同一盒中的 witness。这不是从 `R2(x)` 反推 witness 大小。

量词方面，冻结稿 `:161–163` 写“每个 `H≥H1`”。ST 证明直接给每个充分大整数盒参数 `u`。对实数 `H`，令 `u=floor(H)`；当 `H≥2u0` 时，`u≥H/2` 且 `T(u)⊂T(H)`，故

\[
\#\{t:\text{有 }1\le a,b\le H\text{ 的 witness}\}
\ge C_{21}u^2\ge (C_{21}/4)H^2.
\]

因此“每个充分大实数 `H`”成立，不是只有一个 subsequence，也不是仅存在任意大的盒子。

对每个不同 `t` 选一个 bounded witness 并令 `q_t=tau(a_t/b_t)`。固定 Möbius 变换给 `H(q_t)=O(H)`。若 `q_t=q_t'`，`tau` 的单射性给相同比值 `a/b=a'/b'`；六次齐次性使两型值之比是有理数的六次方，特别是平方。因 `w` 相同，两个带符号 squarefree 商落在同一 square class，只能 `t=t'`。故 `t↦q_t` 单射，KL Lemma 3.2 的 `O(H)` 个 bad rational parameters 至多删除 `O(H)` 个不同 `t`，不能吞掉 `≫H²` 主项。

**闭合点二裁决：passed。** 失败信号“ST 只给无界表示 / 只沿 subsequence 给盒计数 / 一个 thin 参数删除多个不同 squarefree `t`”均未出现。

## 主动挑战与 issue list

| ID | 主动挑战 | 结果 | 处置 |
| --- | --- | --- | --- |
| I1 | 把全局原始型的 `w=2` 代入 KL 最终同余类 | 冻结稿没有这样做；其 `:149–153` 正确重定义类内 maximal `w` | passed；正式稿应继续避免写出类内 `w=2` |
| I2 | 原齐次型首项为零，ST p.951 后置修正可能破坏正锥 | `N1` 有限端点避让同时使首尾非零，因此无需后置修正 | passed |
| I3 | `psi/phi/tau` 复合次序在 prose 中含混 | 公式实际采用正确顺序：新参数 `psi∘phi`，回代 `phi=tau(a/b)` | **minor clarification**；建议正文显式加入该等式 |
| I4 | ST 只计 `R2(x)` 的无界表示 | p.952 `T(u)` 先给盒 witness，p.953 (10)–(15) 再计不同商值 | passed |
| I5 | “每个实数 H”从整数 `u` 无依据外推 | 取 `u=floor(H)`，用单调性且 `u≥H/2`，常数缩小为 `C21/4` | **minor clarification**；建议正文显式写出 |
| I6 | 同一射影参数对应多个 signed squarefree class | 偶次数齐次性使比例为平方；固定 `w` 后 squarefree 代表唯一 | passed |
| I7 | 把 NO-LOG 人工解析论证标成 Lean Verified，或外推 EXP-EPS | 无 kernel receipt；hash 只对齐 NO-LOG，指数仍为 `1/3` | 明确禁止 |

I3、I5 是可在现有来源内立即补出的说明，不改变数学命题或 proof route，故不升级为
`changes_requested`。若稿件将来改动 `phi/psi/tau` 的公式、改用类内 `w=2`、或删去 p.952–953 的 proof-level bounded-witness 引用，本审阅随即 stale。

## 证据平衡与证伪结局

支持线：KL p.6 的冻结公式/量词允许先保留全部固定局部条件再有限避让；ST p.952–953 的冻结 `T` 与 (10)–(15) 锚点给同一正盒中的不同 `F/w²` 值及逐值 witness；射影参数到 signed squarefree class 的单射使 thin 删除严格为低阶。

反驳线：逐项测试了 `N1` 被局部条件唯一钉死、复合顺序反向、端点修正必须移动正锥、类内 `w` 偷换、只有 subsequence witness、无界 `R2` 反推、以及 thin 映射非单射。没有观察到决定性失败信号；I3/I5 仅需显式化已成立的推导。

**falsification outcome: survived。** 精确假设“两个新闭合点足以在冻结来源范围内支持强 KL 的 NO-LOG 人工证明候选”存活。本结论不是对 KL/ST 全文的重新来源认证；由于两个原 PDF 不在当前 Git 树，来源级别准确写作“本地冻结摘录/重放支持”，不是本轮直接 PDF 复读。

## 重放

确定性命令和原始输出保存在
`mathematics/worker/strong-kl-no-log-local-independent-replay.txt`。主要入口：

```bash
python3 mathematics/worker/verify-route-audit.py
python3 -m json.tool mathematics/worker/strong-kl-no-log-source-matrix.json >/dev/null
python3 - <<'PY'
import hashlib, json, pathlib
d=json.loads(pathlib.Path('mathematics/worker/formalization-intake.json').read_text())
s=next(x for x in d['statements'] if x['id']=='NO-LOG')
assert hashlib.sha256(s['normalized'].encode()).hexdigest()==s['statementHash']
print(s['statementHash'])
PY
git diff --check
```

最终验证边界：人工来源审阅 `passed`；无 Lean receipt；不得写 `kernel_verified` 或
`Verified`，不得由本结果推出 `EXP-EPS`。
