# NO-LOG：Kulkarni--Levin / BLT 原文接口 Lead 审计

## 裁决边界

本审计只处理当前候选

\[
N^-_{5,2}(X)\gg X^{1/3}
\]

中 Kulkarni--Levin（KL）与 Bartz--Levin--Thamminana（BLT）的接口；
Stewart--Top（ST）的无对数平方自由值计数由另一条原文审计独立裁决。
在 ST 接口独立闭合前，总状态仍为 **CANDIDATE**。

## 冻结来源

| 来源 | 身份 | 本轮使用位置 |
| --- | --- | --- |
| KL, *Hilbert's Irreducibility Theorem and Ideal Class Groups of Quadratic Fields* | arXiv:2111.15582v1；PDF SHA-256 `26a9e645b55d70a253be2017cc8d656be188ed9c02350c21884286c60b015aae`；期刊版 Acta Arith. 205 (2022), no. 4, 371--380，DOI `10.4064/aa211224-22-9` | PDF p.2 Thms. 1.2--1.3；p.4 Thm. 2.1；p.6 Lemmas 3.1--3.2 与 Thm. 1.2 proof；p.7 (3.1)--(3.2)、计数不等式、Thm. 4.1；pp.7--8 Thm. 1.3 proof |
| BLT, *Counting imaginary quadratic fields with an ideal class group of 5-rank at least 2* | 本地开放期刊 PDF SHA-256 `1b63f04fa1daad0c16a76474bfdd91f7b8ffab01bfd1c55a550b2db75b82539b`；Ramanujan J. 68 (2025), article 26，DOI `10.1007/s11139-025-01184-6` | PDF p.2 Thms. 1.1--1.3；p.3 Thm. 1.4；p.7 显式曲线 `C0` 与 Jacobian torsion |

页码均指 PDF 物理页。技术判断来自逐页原文，不把既有 Agent 摘要当作定理来源。

## 逐项接口矩阵

### K1. thin set 的参数空间与一致性

**原文明示。** KL p.7 Thm. 4.1：对固定的 `C, m, phi` 存在一个固定 thin set
`Omega subset Q`。KL p.6 Lemma 3.2：固定 thin set 中高度 `< x` 的有理数只有
`O(x)` 个。KL p.7 Thm. 1.2 proof 明确定义

\[
\Omega(x)=\{\alpha\in\Omega:H(\alpha)<x\},\qquad |\Omega(x)|\ll x.
\]

因此 `Omega` 和隐常数在曲线、映射和局部数据固定后不依赖盒参数 `H`。

**裁决：source explicit。** 但 Lemma 3.2 只数有理参数；它自身没有陈述删除
多少平方自由值或多少二次域。

### K2. 从不同平方自由值到 thin 删除

**原文明示的证明步骤。** KL p.6 Thm. 1.2 proof 定义 `T(x)` 为不同平方自由整数
`t` 的集合，并为每个 `t` 选一个正整数 witness `(a_t,b_t)`，形成 `T'(x)`。
p.7 的 (3.1)--(3.2) 后，原文给出

\[
|R(c^{-1}x)|\ge |T'(c^{-1}x)|-2|\Omega(x)|.
\]

这里因次数二覆盖，每个坏参数至多对应两个几何点，故系数 2。

**用于强 ST 替换所需的附加初等引理。** 若强 ST 直接给不同带符号平方自由值
`t` 及一个 bounded witness，令 `q_t=tau(a_t/b_t)`。若 `q_{t_1}=q_{t_2}`，
则两个 witness 给同一射影比。六次齐次性使对应的 `F` 值之比为有理平方；两个
带符号平方自由整数属于同一 `Q*/Q*2` 类当且仅当相等。因此 `t -> q_t` 单射，
thin 删除至多删 `O(H)` 个已计 `t`。

**裁决：原路线为 source explicit；强 ST 替换为 immediate/additional elementary
lemma。** 该引理已在此写出，但不应误标为 KL Lemma 3.2 的结论。

### K3. 不同二次域与共轭点措辞

KL p.7 逐式计算

\[
Q(P)=Q(\sqrt{f(\phi(P))})=Q(\sqrt{F(a_t,b_t)})=Q(\sqrt t).
\]

不同带符号平方自由 `t` 给不同平方类，从而给不同二次域。

**需要修正的原文措辞。** `R(x)` 定义为几何点集合；同一个非分支参数通常有两个
共轭点，它们生成同一个二次域。因此 p.7 “the fields `Q(P), P in R(x), are all
distinct`” 不能逐字理解为对几何点的单射。正确陈述是：不同 `t` 产生不同域；
每个域至多由该二覆盖的两个共轭点出现。按 `t` 直接计数，或把点数除以 2，数量级
不变。

**裁决：additional elementary correction，非致命。** 当前 NO-LOG 路线应始终按
不同 `t` 计数，不应引用错误的逐点单射措辞。

### K4. 虚二次符号和类群 5-rank

KL pp.7--8 Thm. 1.3 proof：把有理 Weierstrass 模型写为首一奇次数
`y^2=f(x)`，固定坏素数集 `S` 和 `M=prod_{p in S}p`；为虚二次情形选择固定平移
`phi=x+N/M`，其中 `N` 足够大，使 `|phi(P)|_infty<1` 时 `f(x(P))<0`。
同一局部邻域还使每个 `p in S` 在 `Q(P)` 中分歧。KL p.7 Thm. 4.1 再给
class-rank 不等式；虚二次域的普通单位秩为 0，且每个坏素数分歧，故 S-unit 修正
恰好抵消 `#S`，得到

\[
rk_m Cl(Q(P))\ge rk_m Jac(C)(Q)_{tors}.
\]

BLT p.7 给出
`Jac(C0)(Q)_tors = Z/5Z x Z/10Z`，其 5-rank 为 2；BLT p.3 Thm. 1.4
正是把 KL Thm. 1.3 用于这种曲线。

在强 ST 替换中，KL p.6 Lemma 3.1 的正盒同余类保证所有固定有限/实局部邻域；
而恒等式 `f(tau(a/b))=F(a,b)R(a,b)^2` 使合格 `F(a,b)=t w^2` 与 `f<0`
同号，故 `t<0`。

**裁决：source explicit + immediate sign transfer。** 前提是变换端点不落在分支点，
且强 ST 的正盒确实保留同一固定同余类；后者属于 ST 原文审计。

### K5. 判别式 `O(H^6)` 的统一性

KL p.8 Thm. 1.3 proof 明示：若 `H(phi(P))<=B`，则对固定 `f,M,N` 有

\[
|d_{Q(P)}|\le c' B^{2g+2}.
\]

对 BLT 的 genus 2 曲线，指数为 6，常数只依赖固定曲线和平移。

强 ST 路线还有更直接的界：固定六次齐次型上，`1<=a,b<=H` 时
`|F(a,b)|<=C_F H^6`；若 `F(a,b)=t w^2` 且 `t` squarefree，则
`Disc(Q(sqrt t))` 为 `t` 或 `4t`，故

\[
|Disc(Q(\sqrt t))|\le 4C_F H^6/w^2.
\]

全部常数在 `F,w` 固定后独立于 `H,t,a,b`。

**裁决：source explicit；强路线另有 immediate direct proof。** 不需要额外的表示
重数估计。

### K6. BLT 的固定 `C0` 专门化

BLT p.7 显式给出奇五次模型

\[
C_0:y^2=(5x+7)(128x^4+549x^3+1007x^2+936x+368)
\]

并报告 Magma 验证的 Jacobian torsion `Z/5 x Z/10`。奇五次模型给有理无穷远
Weierstrass 点；因此满足 BLT p.3 Thm. 1.4 / KL p.2 Thm. 1.3 的几何前提。
BLT p.2 对 `N^-(m^r;X)` 和 `m`-rank 的定义显示，`m=5,r=2` 正是所需
`5`-rank 至少 2，而不是只要求 `5 | h_K`。

**裁决：source explicit，另含计算机支持的 torsion 等式。** BLT 论文将 Magma
计算作为其定理证明输入；本审计只核对其已发表使用，不把该计算提升为 Lean 认证。

## KL 弱定理替换为 ST 强分支时不能省略的义务

KL p.4 Thm. 2.1 是 Stewart--Top Thm. 2 的轻微变体，结论带 `(log x)^-2`。
NO-LOG 必须改用 ST 的更强分支；以下不是 KL 的 theorem statement：

1. 最终固定同余类中的 maximal fixed square `w^2`；
2. 强定理数的是不同 squarefree `t=F(a,b)/w^2`；
3. 每个已计 `t` 在同一正盒内有 bounded witness；
4. 正盒、首尾系数、PGL2 变换和因子次数条件可同时满足；
5. 上述固定数据和正主项常数均先于 `forall H` 选择。

这五项全部属于 ST 原文审计/附加局部化引理。KL 原文只提供之后的 local/thin/sign/
height/field 接口。

## 对抗结论

最便宜的破坏测试是把 KL Lemma 3.2 的参数计数直接当作不同域计数。该推理本身
无效；原文必须通过 p.6 为每个 `t` 选 witness、p.7 的域恒等式和至多二对一修正。
完成这些修正后，没有发现 KL/BLT 侧会吞掉 `H^2` 主项的反例。

本轮没有验证 ST 的五项替换义务，因此最终状态保持 **CANDIDATE**，不进行新颖性
检索，也不声称无条件 NO-LOG 已证。
