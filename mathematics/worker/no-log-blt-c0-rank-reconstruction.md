# BLT `C0` 的最小 5-rank 输入：显式重构

## 裁决

**通过。** Bartz--Levin--Thamminana（BLT）Theorem 2.1 对

\[
(t,u,z)=\left(\frac23,-\frac13,25\right)
\]

给出的偶六次模型，与 BLT p.7 展示的

\[
C_0:y^2=(5x+7)(128x^4+549x^3+1007x^2+936x+368)
\]

在 \(\mathbf Q\) 上显式同构。因此 Theorem 2.1 已经证明

\[
\operatorname{rk}_5 \operatorname{Jac}(C_0)(\mathbf Q)_{\rm tors}=2.
\]

NO-LOG 证明只需这个结论；不需要另外信任 p.7 的 Magma 断言
`Jac(C0)(Q)_tors = Z/5Z x Z/10Z`。

## 原始来源边界

- BLT PDF pp.4--5：Theorem 2.1 的系数 \(a,a_0,a_2,a_4,a_6\)，以及结论
  \(\operatorname{Jac}(C)\) 与 \(E_t\times E_u\) 作 \((2,2)\)-同源、5-rank 为 2。
- BLT PDF p.6：该定理的直接证明；同源次数为 4，与 5 互素。
- BLT PDF pp.6--7：样本 \((2/3,-1/3,25)\)，以及“简化并改为奇模型”后得到的 `C0`。
- 作者公开的 `Section3Computations.magma` 第 54--98 行与论文使用同一系数公式并将样本代入偶六次模型；第 125--128 行是额外的 Magma 搜索/挠群核验，不是本证书所依赖的秩来源。

## 样本代入

精确有理数运算给出 BLT (2.3) 两边均为 \(-3125/2187\)，并且

\[
\begin{aligned}
a&=2048/243, &a_0&=-10240/531441,\\
a_2&=20480/59049, &a_4&=182272/177147,\\
a_6&=31129600/531441.
\end{aligned}
\]

此外 \(a\ne0\)，且 \(t,u\notin\{0,1/2,1\}\)，所以 Theorem 2.1 的全部显式
样本假设成立。令

\[
C_{\rm even}:y^2=P(x)=a(a_6x^6+a_4x^4+a_2x^2+a_0).
\]

由 \(zx^2-1\mid P(x)\)，\(x=1/5\) 是一个有理分支点。

## 显式奇模型和 `C0`

先令

\[
X=\frac1{x-1/5},\qquad Y=yX^3.
\]

则

\[
Y^2=\frac{4194304}{16142520375},
\bigl(1900000+2280000X+1173375X^2+330700X^3+64860X^4+9216X^5\bigr).
\]

再令 \(X=25x_0/6+10/3\)。逐项比较系数得到

\[
\frac{108}{1953125},p(25x_0/6+10/3)
=640x_0^5+3641x_0^4+8878x_0^3+11729x_0^2+8392x_0+2576,
\]

而

\[
\frac{4194304/16142520375}{108/1953125}
=\left(\frac{128000}{59049}\right)^2.
\]

合并变量代换可写成简洁的显式同构

\[
x_0=\frac{2(1-2x)}{5x-1},\qquad
y_0=\frac{59049y}{1024(5x-1)^3},
\]

其逆变换为

\[
x=\frac{x_0+2}{5x_0+4},\qquad
y=\frac{8192y_0}{2187(5x_0+4)^3}.
\]

令

\[
f_0(x_0)=640x_0^5+3641x_0^4+8878x_0^3
+11729x_0^2+8392x_0+2576.
\]

重放脚本不是只抽样点，而是逐项断言清分母后的精确恒等式

\[
1024^2(5x-1)^6
f_0\!\left(\frac{2(1-2x)}{5x-1}\right)=59049^2P(x).
\]

此外，由 `5x_0+4=6/(5x-1)`，脚本分别断言

\[
\frac{x_0+2}{5x_0+4}=x,
\qquad
\frac{8192}{2187(5x_0+4)^3}
\frac{59049}{1024(5x-1)^3}=1.
\]

旧的 inverse-`y` 分子 `1024` 会使后一复合因子恰为 `1/8`，因而已被拒绝。
所以 `C_even` 与 BLT p.7 的 `C0` 在 \(\mathbf Q\) 上同构。

## 强度账本

| 命题 | 状态 | 依据 |
|---|---|---|
| 样本满足 BLT (2.3) 与 Theorem 2.1 假设 | proved | 精确分数重放 |
| 样本偶六次模型与 p.7 的 `C0` 同构 | proved | 上述显式双向变换与系数恒等式 |
| `Jac(C0)` 与两个带有理 5-挠的椭圆曲线之积作次数 4 同源 | source-supported theorem | BLT Theorem 2.1 及 p.6 proof |
| `rk_5 Jac(C0)(Q)_tors = 2` | source-supported theorem + proved model identification | BLT Theorem 2.1；次数 4 与 5 互素 |
| 完整挠群恰为 `Z/5 x Z/10` | computational/source-reported, unnecessary | BLT p.7 Magma 输出 |

## 主动失败测试

作者仓库的 `verification.magma` 中另有六次型
`1025*x^6+24334*x^4+3025*x^2-160`。它不是论文 pp.6--7 用来识别样本 `C0`
的公式，不能拿来替代上述样本代入。本证书完全从 Theorem 2.1 的系数重新生成模型，
所以避开了这个错误文件匹配风险。

## 重放

```sh
python3 mathematics/worker/no-log-blt-c0-rank-replay.py
```

预期末行：`PASS`。脚本只使用 Python 标准库 `fractions` 和整数运算。
