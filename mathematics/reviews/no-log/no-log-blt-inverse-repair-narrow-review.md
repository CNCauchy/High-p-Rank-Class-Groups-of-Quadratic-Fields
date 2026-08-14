# BLT `C_even ↔ C0` 逆映射修复：独立窄审阅

## 裁决

**passed（仅限修复提交）。** 本审阅从曲线方程重新推导正逆映射，不导入或调用被审
脚本。提交 `72f288cd34b341210ead2fc529641530a168433f` 把 inverse-`y` 分子从
`1024` 改为 `8192` 是必要且正确的：新映射的正反复合比例均为 `1`，旧公式的比例恰为
`1/8`。清分母后的 forward curve identity 为精确多项式恒等式，两个方向的 `x` 复合也
均为恒等。

该裁决不增强 NO-LOG 的范围。两份 Lean 文件仍只认证条件蕴含，完整 NO-LOG 结果仍是
`CANDIDATE`；本轮没有做 novelty search。

## 冻结边界

- 被审提交：`72f288cd34b341210ead2fc529641530a168433f`
- 父提交：`a39641d52ec93c56f1dfbddb9ef206196c6e6b43`
- 被审差异仅有三文件：
  - `mathematics/problems/no-log-candidate-complete-proof.md`
  - `mathematics/worker/no-log-blt-c0-rank-reconstruction.md`
  - `mathematics/worker/no-log-blt-c0-rank-replay.py`
- 本审阅只新增本文件与相邻的冻结 replay 文本；没有修改上述三文件。

三个被审文件的 SHA-256 依次为：

- `302dc3be04ecc7df3b32c4a6a437daa273afc42b88a98415ab502105d5580718`
- `263b7f65068e95c96431834ae0bffc54a0ec5a2b4d1c488493e12cf28ccd5652`
- `f936ec90429ab96ca32b0cbeafa8c8913277612b75ad0768a9316937be821446`

## 独立重导

写

\[
C_{\rm even}: y^2=P(x),\qquad C_0:y_0^2=f_0(x_0),
\]

以及

\[
x_0=\frac{N}{D}=\frac{2(1-2x)}{5x-1},
\qquad
y_0=\frac{59049}{1024D^3}y.
\]

### Forward curve identity

把 `C0` 的五次多项式直接代入 `N/D`，独立 PARI/GP 有理函数计算得到

\[
1024^2D^6 f_0(N/D)-59049^2P(x)=0.
\]

这是系数级精确恒等式，不是有限点抽样。于是 forward map 确实把
`C_even` 的曲线方程送到 `C0`。

### `x` 的正逆复合

从 `x_0(5x-1)=2(1-2x)` 直接解得

\[
x=\frac{x_0+2}{5x_0+4}.
\]

代回两边分别得到

\[
x\mapsto x_0\mapsto x=x,
\qquad
x_0\mapsto x\mapsto x_0=x_0.
\]

PARI/GP 对两个有理函数之差均返回精确的 `0`。

### `y` 的正逆复合及旧公式反例

由 inverse-`x` 立即有

\[
D=5x-1=\frac6{5x_0+4}.
\]

因此

\[
y=\frac{1024D^3}{59049}y_0
=\frac{1024\cdot6^3}{59049(5x_0+4)^3}y_0
=\frac{8192}{2187(5x_0+4)^3}y_0.
\]

新分子的复合比例为

\[
\frac{8192}{2187}\frac{59049}{1024}\frac1{6^3}=1.
\]

反向复合给出同一比例。若仍用旧分子 `1024`，比例则为

\[
\frac{1024}{2187}\frac{59049}{1024}\frac1{6^3}=\frac18,
\]

所以旧公式在任意非零 `y` 上都不是逆映射。这是精确、可重放的失败见证，而非数值误差。

## 边界案例

仿射公式在 `D=5x-1=0` 或 `5x_0+4=0` 处有极点；两者互为射影坐标的无穷远边界。
本审阅的复合等式是有理函数恒等式，先在分母非零的稠密开集上成立，并由曲线的射影
同构解释边界点。不能把极点处未定义的仿射表达式误报为映射失败，也不能用有限点抽样
代替上述有理恒等式。

## 范围与回归审计

`a39641d..72f288c` 的差异统计为 `22/2`、`27/3`、`41/7`，且 `git diff --check`
通过。语义变化限于：

1. 两处文档把 inverse-`y` 的 `1024` 修为 `8192`；
2. replay 增加 forward curve identity、精确 `x/y` 复合与旧公式 `1/8` 拒绝断言；
3. 完整证明稿仍明确标为 `CANDIDATE`，条件 Lean 源码未改。

没有改变计数指数、量词、局部条件、thin-set、重数义务或 theorem statement，故未发现
范围增强。

## 重放结果

以下命令均退出 `0`；完整 stdout 与命令保存在
`mathematics/reviews/no-log/no-log-blt-inverse-repair-narrow-replay.txt`。

```sh
python3 mathematics/worker/no-log-blt-c0-rank-replay.py
python3 mathematics/worker/verify-route-audit.py
lean -q -t 0 mathematics/formal/NoLogSourceBridge.lean
lean -q -t 0 mathematics/formal/NoLogInference.lean
git diff --check a39641d52ec93c56f1dfbddb9ef206196c6e6b43 \
  72f288cd34b341210ead2fc529641530a168433f
```

### 证据平衡

- 支持修复：独立 forward identity、双向 `x` 复合、双向 `y` 比例、全部回归命令均通过。
- 反驳旧公式：`1024` 给出精确比例 `1/8`。
- 未覆盖：本审阅不重新证明 BLT 来源定理、Stewart--Top/KL 分析桥或 NO-LOG；这些不是
  本次 inverse-map 修复的范围。

最终判定：修复提交在声明范围内 **passed**；不存在由本轮有限检查外推出的新定理。
