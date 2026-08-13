# 非循环 5-类群的证明路线审计

## 结论先行

本审计的最重要发现是一条相当具体、且成本远低于“重新构造曲线”的候选改进：把 Stewart–Top 的**强平方自由值定理**直接用于 Bartz–Levin–Thamminana（下称 BLT）给出的属 2 曲线 \(C_0\)，看起来可把

\[
N^-(5^2;X)\gg \frac{X^{1/3}}{(\log X)^2}
\]

加强为

\[
N^-(5^2;X)\gg X^{1/3}.
\]

关键不是新曲线，而是该曲线的判别式参数型恰为一个次数 6 二元型，且显式分解成 \(1+1+4\) 次因子，正落在 Stewart–Top 强定理的适用范围。当前审计已核对该分解，并用模 \(7\) 多项式 gcd 给出无重根证书；尚需把 BLT/Kulkarni–Levin 的局部同余条件、thin set 剔除和强定理的固定平方因子记号逐项写成正式证明。因此本结论是“高可信候选引理”，不是已发表定理，也不是 `kernel_verified` 结果。

若目标是改进指数 \(1/3\)，固定一条属 2 双覆盖的单参数方法存在清楚的几何障碍：自然判别式高度是参数高度的六次方，而可产生的不同参数/平方类至多是二次量级。要越过 \(1/3\)，必须降低判别式高度、增加真正独立的参数，或转向按共同二次预解式计数 \(D_5\) 扩张的路线。

本文使用以下标签避免混淆：

- **[原文]**：供应 PDF 或其明确引用定理中的陈述；
- **[直接推论]**：从原文陈述立即得到、没有新筛法输入；
- **[Worker 推导]**：本审计给出的论证或计算，尚待独立审阅；
- **[研究假设]**：建议攻击的命题，不作为已证事实。

## 1. 文献身份、记号与范围

供应文件 `29_noncyclic_class57.pdf` 是 2008 年 4 月生成的预印本；BLT 的参考文献将正式版本列为 Dongho Byeon, *Quadratic fields with noncyclic 5- or 7-class groups*, Ramanujan J. 19 (2009), 71–77。下文页码均指供应 PDF 的 PDF/印刷页（两者在正文中一致）。

令

\[
N^-(5^2;X)=\#\{K/\mathbf Q:\ K\text{ 虚二次},\ |d_K|\le X,\
\operatorname{rk}_5\operatorname{Cl}(K)\ge2\}.
\]

对有限阿贝尔群，包含 \((\mathbf Z/5\mathbf Z)^2\) 与 5-rank 至少 2 等价；但 Byeon 原文的精确措辞是“类群含有一个同构于 \((\mathbf Z/g\mathbf Z)^2\) 的子群”。

### 1.1 Byeon 的主定理（准确范围）

**[原文] Theorem 1.1（p. 2）**：对 \(g=5\) 或 \(7\)，绝对判别式不超过 \(x\) 且理想类群含有
\((\mathbf Z/g\mathbf Z)^2\) 的虚二次域数目，以及实二次域数目，均满足

\[
\gg x^{1/4}.
\]

这一定理：

1. 同时覆盖实、虚二次域；
2. 只覆盖 (g=5,7)，不是所有奇素数；
3. 是无条件下界且没有 (x^{-\varepsilon}) 或对数损失；
4. 不声称正比例、渐近公式或 Cohen–Lenstra 预期数量级。

摘要（p. 1）也明确说该 (x^{1/4}) 攭进了先前 (g=5) 的 (x^{1/5-\varepsilon}) 与 (g=7) 的 (x^{1/7-\varepsilon})。

### 1.2 2025 基准

**[原文] BLT Theorem 1.3（供应 2025 PDF, p. 2）**：

\[
N^-(5^2;X)\gg \frac{X^{1/3}}{(\log X)^2}.
\]

**[原文] BLT Theorem 1.4（p. 3，引自 Kulkarni–Levin）**：若 \(C/\mathbf Q\) 是有 \(\mathbf Q\)-有理 Weierstrass 点的光滑射影超椭圆曲线，属为 \(g\)，且

\[
r=\operatorname{rk}_m \operatorname{Jac}(C)(\mathbf Q)_{\rm tors},
\]

则

\[
N^-(m^r;X)\gg \frac{X^{1/(g+1)}}{(\log X)^2}.
\]

BLT 随后只需构造 (g=2)、(r=2) 的一条曲线。供应计划书 p. 1–2 对已知界和研究目标的概述与这两个定理一致，但计划书本身不是证明来源。

## 2. Byeon 证明链的逐步拆解

| 步骤 | 精确输入/操作 | 输出 | 性质与锚点 |
|---|---|---|---|
| 1 | 有理 (p)-扭点 (P\in A(\mathbf Q))、商同源 φ 与 Néron 模型 | 从商群到 \(\operatorname{Hom}(\operatorname{Cl}_K,\mathbf Z/p\mathbf Z)\) 的注入；两个独立的未分歧 (p)-覆盖给出 (p)-rank 至少 2 | **[原文综述]** p. 2–3；具体充分条件交由 Mestre |
| 2 | (p=5) 时取带有理 5-扭点的椭圆曲线族，定义三次式 \(D(x,u,v)=4x^3+B_2x^2+2B_4x+B_6\) | 若 \(D(x_1,u,v)=D(x_2,u,v)\) 且满足若干局部不等式/同余，则 \(\operatorname{Cl}(\mathbf Q(\sqrt D))\) 含 \((\mathbf Z/5)^2\) | **[原文输入]** Mestre Proposition 2.1，p. 3 |
| 3 | 虚二次 5-rank 情形固定 \(u=0,v=1,q=5\)，并取两个显式有理函数 \(x_1(t),x_2(t)\) | \(D(x_1)=D(x_2)\) 在平方类意义下变成负的次数 8 多项式 \(m(t)\)；特定同余类的 (t) 均给出所需类群 | **[原文]** Lemma 4.2，p. 5–6 |
| 4 | 写 (t=a/b)，齐次化 \(F(U,V)=V^8m(U/V)\) | 次数 8 二元型；其 displayed factorization 为二次因子乘六次因子 | **[原文/直接推论]** Lemma 4.2 与 p. 7 的统一证明 |
| 5 | Stewart–Top：非零判别式、次数 (r\ge3)、每个不可约因子次数至多 6 的二元型，在固定同余类中产生 \(\gg X^{2/r}\) 个不同平方自由部分 | (r=8\) 给 \(\gg X^{1/4}\) 个不同平方类 (t) | **[原文输入]** Proposition 3.1，p. 4；Theorem 1.1 的证明，p. 7 |
| 6 | (m(t)<0)，且平方自由 (t) 决定唯一二次域 \(\mathbf Q(\sqrt t)\) | 虚二次域、判别式只差至多常数因子；类群含 \((\mathbf Z/5)^2\) | **[原文证明结构]** Lemma 4.2 与 p. 7“其余情形相同” |

实 5、实 7、虚 7 分别由 Lemmas 4.1、4.3、4.4（pp. 5–7）替换步骤 3，筛法部分相同。

### 2.1 参数化为何自然产生次数 8

固定 (u,v) 后，去掉平凡分支 (x_1=x_2)，等值条件分解为圆锥

\[
4(x_1^2+x_1x_2+x_2^2)+B_2(x_1+x_2)+2B_4=0.
\]

**[Worker 推导]** 其无穷远截面为

\[
x_1^2+x_1x_2+x_2^2=0,
\]

两个点定义在 ℚ(√−3) 而非 ℚ 上。圆锥若有有理点可由 ℙ¹ 参数化，但 (x_i) 在上述两个共轭无穷远点处有极点；三次函数 (D(x_i)) 通常在两点各有奇数阶极点。于是双覆盖

\[
y^2=D(x_1(t),u,v)
\]

通常有“六个有限零点 + 两个无穷远极点”共八个分歧点，即属 3，对应平方类次数 8。这解释了 Byeon 的显式 (m(t)=(t^2+t+1)\cdot(\text{sextic}))，也说明仅对 (t) 做 Möbius 变换不会自动降到次数 6。

对 Lemma 4.2 的 (m(t))，本审计把显示的二次与六次因子相乘，并检查

\[
\gcd(\bar m,\bar m')=1\quad\text{in }\mathbf F_7[t].
\]

因此该具体次数 8 模型确实无重根；这同时排除了“Byeon 的虚 5 族其实已因隐藏平方因子降为次数 6”的最便宜反驳。

## 3. (1/3) 与 ((\log X)^{-2}) 分别从哪里来

BLT 的曲线为（p. 7）

\[
C_0:y^2=f(x)=640x^5+3641x^4+8878x^3+11729x^2+8392x+2576,
\]

且

\[
f(x)=(5x+7)(128x^4+549x^3+1007x^2+936x+368).
\]

**[原文]** BLT 先由 Howe–Leprévost–Poonen 的 \(2,2\)-gluing 构造 \(\\operatorname{Jac}(C)\) 与两个带 5-扭点的椭圆曲线之积间、次数与 5 互素的同源（pp. 3–6），再在搜索中找到有有理 Weierstrass 点的 \(C_0\)；Magma 检查其有理挠子群恰为 \(\\mathbf Z/5\\mathbf Z\\times\\mathbf Z/10\\mathbf Z\)（p. 7）。代入 Theorem 1.4 即得 Theorem 1.3。

Kulkarni–Levin 的证明把参数高度 (B) 转为判别式高度 (O(B^{2g+2}))，同时其二次 Hilbert 不可约计数给 ≫ (B^2/(\log B)^2) 个域。因此

\[
B=X^{1/(2g+2)}\quad\Longrightarrow\quad
\frac{B^2}{(\log B)^2}\asymp \frac{X^{1/(g+1)}}{(\log X)^2}.
\]

所以：

- 指数 (1/3) 来自 (g=2) 与判别式六次高度；
- ((\log X)^{-2}) 来自 Kulkarni–Levin 对一般二次覆盖使用 Stewart–Top 的弱定理（其 Chebotarev 选素步骤产生该损失），不是 Jacobian 5-扭点构造本身造成的。

## 4. 路线 A（最高优先级）：对 \(C_0\) 使用 Stewart–Top 强定理，去掉对数

### 4.1 已完成的廉价核验

对 (x=a/b)，决定平方域的自然齐次型是

\[
\begin{aligned}
F(a,b)&=b^6f(a/b)\\
&=b(5a+7b)(128a^4+549a^3b+1007a^2b^2+936ab^3+368b^4).
\end{aligned}
\]

故 (F) 的次数为 6，而不可约因子的次数至多 4。直接整数展开已与 (f) 的五个系数逐项吻合。本审计还检查

\[
\gcd(\bar f,\bar f')=1\quad\text{in }\mathbf F_7[x],
\]

从而 (f)（以及加入无穷远线性因子后的 (F)）判别式非零。

Stewart–Top, Theorem 1（JAMS 8 (1995), pp. 950–951）对非零判别式的次数 (r) 二元型，在平方自由情形要求最大不可约因子次数 ≤ (2k+1=5)，并另包含 (k=2,m=6) 的边界情形；结论是固定同余类中有 ≫ (X^{2/r}) 个不同平方自由表示值。这里 (r=6,m\le4)，故形式条件明显满足。

### 4.2 最小决定性引理

**[研究假设 A / 候选引理]** 在 Kulkarni–Levin/BLT 为 \(C_0\) 选取的坏素数局部条件和 thin set \(\Omega\) 下，可选一个整系数 \(GL_2(\mathbf Q)\) 坐标变换及一个原始同余类 \((a,b)\bmod M\)，使变换后的次数 6 二元型仍有非零判别式、最大不可约因子次数至多 5，并且 Stewart–Top 强定理产生的参数满足所有局部条件。则

\[
N^-(5^2;X)\gg X^{1/3}.
\]

证明骨架只有四步：强定理给高度 (B) 内 ≫ (B^2) 个不同平方类；Ω 内高度 (B) 的有理数只有 (O(B)) 个，故剔除不改变主阶；局部条件保证虚二次与两个 5-类独立；判别式 (O(B^6))，置 (B\asymp X^{1/6})。

### 4.3 依赖、失败信号、可能产物

- 依赖：Stewart–Top Theorem 1 的固定同余类版本；Kulkarni–Levin 的局部化引理、thin-set 引理及 Gillibert–Levin 类群特化定理。
- 最便宜失败测试：逐行重写 Kulkarni–Levin Theorem 1.2/3.1 的证明，并查明其 (GL_2) 变换后的强定理常数 (w)、正象限条件或同余类是否出现不能满足的固定平方障碍。若出现某个素数 (p) 使允许同余类中 (F(a,b)/w^2) 永远不平方自由，路线失败。
- 当前 falsification：**初步存活**。因子次数和无重根条件均通过；尚未完成局部条件的逐素数审计。
- 可能产物：一篇很短的 note，主命题为 \(N^-(5^2;X)\gg X^{1/3}\)，附 \(C_0\) 的显式二元型和局部条件表。

## 5. 路线 B：在 Mestre 等值圆锥上寻找属降，改进 Byeon 的指数

固定 (u,v) 的一般族是属 3，因而产生次数 8 型和 (X^{1/4})。若能让八个分歧点中的两个合并成偶重数（同时保持剩余六个简单分歧点及 Mestre 局部独立条件），就得到属 2/次数 6 子族，并至少恢复 (X^{1/3})；若再出现合法的次数 ≤5 平方类模型，才可能在单参数框架内越过 (1/3)。

### 最小决定性引理

**[研究假设 B]** 存在有理 (u:v) 及等值圆锥的一条有理参数化，使 (D(x_1(t),u,v)) 的平方自由部分分歧度 ≤6，判别式非零、符号为负，并在一个非空同余类上满足 Mestre Proposition 2.1 的全部条件。

### 依赖、失败信号、可能产物

- 依赖：对 (D(x_1(t),u,v)) 的 numerator、denominator、resultant 和 discriminant 做符号计算；最后仍用 Stewart–Top。
- 最便宜失败测试：在有限域上消元“判别式降阶/有偶重根”条件。若其唯一分量均落在 (x_1=x_2)、椭圆曲线退化、(D=0) 或 Mestre 禁止的局部因子上，则该路线被反驳。
- 当前 falsification：**一般情形的天真降次已被否定**。无穷远共轭点给两个奇极点；Byeon 的具体虚 5 模型又经模 7 gcd 证实无重根。只有特殊 (u:v) 的退化子簇仍开放。
- 可能产物：参数退化簇的方程及分量分类；成功时给新的显式低次数族，失败时给“固定 Mestre 三次等值构造的属下界”命题。

这一路线与 A 独立：A 改筛法输入而不改曲线，B 改几何分歧度而沿用强筛。

## 6. 路线 C：保留 Howe–Leprévost–Poonen 的第二参数，冲击 (1/3+\delta)

BLT 从方程

\[
\Delta_{10}(t)z^2=\Delta_{10}(u)
\]

构造 \(\\operatorname{Jac}(C)\) 与 \(E_t\\times E_u\) 的 \(2,2\)-同源（pp. 4–6），但最终只挑一条固定曲线 \(C_0\)，再沿其超椭圆坐标做单参数特化。固定曲线最多提供高度盒中的 \(B^2\) 个有理参数对，而判别式为 \(B^6\)，自然停在 \(1/3\)。潜在的指数改进必须证明 HLP 解空间中有一族不同的 \(C_s\)，且新增参数 \(s\) 产生的二次域没有被原有参数的碰撞完全吞掉。

### 最小决定性引理

**[研究假设 C]** 构造一个正维有理子族 (C_s)，每条曲线有有理 Weierstrass 点及两个独立 5-扭特化类，并证明在一个二维/加权参数盒中：

1. 判别式高度 ≤ (X)；
2. 至少 ≫ (X^{1/3+\delta-o(1)}) 个不同平方类；
3. thin 异常集与曲线间同构/平方类碰撞为低阶。

这个“多参数平方类碰撞引理”是决定性内容；仅列出很多 (C_s) 不足以改指数。

### 依赖、失败信号、可能产物

- 依赖：HLP gluing、Weierstrass 点条件所定义子簇的几何、二元/多元平方自由筛、统一 Hilbert 不可约与高度计数。
- 最便宜失败测试：先计算“有理 Weierstrass 点”条件在 ((t,u,z))-曲面上的维数和几何亏格；若它只有零维分量，或所有正维分量均为 isotrivial/同一平方类，则路线失败。BLT 的有限搜索得到 85 个 ℚ-同构类（p. 6–7）是支持探索的证据，但不是正维性的证明。
- 当前 falsification：**未决**。供应材料没有给出 Weierstrass locus 的方程或维数。
- 可能产物：该 locus 的消元方程与分量分解；即使没有指数改进，得到一个含 ((\mathbf Z/5)^2) Jacobian torsion 的显式属 2 曲线族也有独立价值。

## 7. 路线 D（长期、通向 Cohen–Lenstra）：共同二次预解式的 \(D_5\) 对计数

类群中的一个 5-rank 方向对应一个未分歧循环五次扩张；其在 \(\mathbf Q\) 上的 Galois 闭包为典型的 \(D_5\) 扩张。5-rank 至少 2 时，二维 \(\mathbf F_5\) 空间含

\[
\frac{5^2-1}{5-1}=6

\]

条一维方向。因此不能仅靠“有很多 (D_5) 域”推出 rank ≥2：必须控制具有**同一二次预解式**的多个独立五次扩张。

### 最小决定性引理

**[研究假设 D]** 对 (|d_K|\le X) 的虚二次 (K)，设 (a_K) 为相应未分歧 (C_5) 扩张（或 (D_5) 五次域）的方向数。证明一个足以迫使 (a_K\ge6) 在 ≫ (X^{1-o(1)}) 个 (K) 上发生的截断阶乘矩下界，并同时控制少数大 (a_K) 对矩的集中贡献。

### 依赖、失败信号、可能产物

- 依赖：(D_5) 域的参数化/轨道计数、共同二次预解式条件、局部未分歧筛，以及一阶与二阶矩的上下一致控制。
- 最便宜失败测试：在可复现的小判别式数据库上按二次预解式分桶，比较一阶和二阶阶乘矩是否几乎全由极少数高重数桶贡献。若是，朴素二阶矩不能给所需下界，必须加入截断或更高矩。
- 当前 falsification：**未运行**；供应数据不含数域表，且本任务不授权外部数据库提交。
- 可能产物：共同 resolvent 的 (D_5)-对计数定理。它是四条路线中唯一结构上可能接近 Cohen–Lenstra 所预言 (X) 量级者，也是依赖最重的一条。

## 8. 优先次序与依赖说明

1. **先做 A**：已有显式次数 6 型，决定性失败测试只需文献逐行兼容审计；若通过，立即去掉 ((\log X)^2)。
2. **并行准备 B 的符号消元**：它能说明 Byeon (1/4) 是偶然参数选择还是构造内在障碍；成功也只先到 (1/3)，但会给清晰的结构结论。
3. **A 完成后再做 C**：指数改进的核心不是更多曲线样本，而是多参数的高度与碰撞定理。
4. **D 作为长期主线**：它最接近 Cohen–Lenstra，但当前不应把 moment 启发式写成定理。

关键依赖的精确位置：

- Byeon: Theorem 1.1 (p. 2), Mestre Propositions 2.1–2.2 (pp. 3–4), Stewart–Top Proposition 3.1 (p. 4), Lemma 4.2 (pp. 5–6), final homogenization/sieve (p. 7)。
- BLT 2025: Theorems 1.3–1.4 (pp. 2–3), HLP gluing and Theorem 2.1 (pp. 3–6), search and \(C_0\) (pp. 6–7)。
- Kulkarni–Levin, arXiv:2111.15582: main quadratic HIT theorem and the hyperelliptic corollary；其 proof 明写判别式高度 (B^{2g+2})。
- Stewart–Top, JAMS 8 (1995): strong Theorem 1 (pp. 950–951) 与 general/weak Theorem 2 (p. 954) 应严格区分；前者无对数但需非零判别式及因子次数条件，后者适用更广而损失 ((\log X)^2)。

公开来源：

- C. L. Stewart and J. Top, [*On Ranks of Twists of Elliptic Curves and Power-Free Values of Binary Forms*](https://uwaterloo.ca/pure-mathematics/sites/default/files/uploads/documents/s0894-0347-1995-1290234-5_0.pdf).
- K. Kulkarni and A. Levin, [*Hilbert's Irreducibility Theorem and Ideal Class Groups of Quadratic Fields*](https://arxiv.org/abs/2111.15582).

## 9. 显式 falsification 结论与验证边界

任务级假设“现有材料足以产生可用的独立证明路线审计”经测试后为 **survived**：已恢复 Byeon 的完整构造—筛法依赖链，区分 (1/3) 与对数损失的来源，并得到四条互相独立的路线及其最小失败信号。

路线 A 的核心代数前提也通过了最便宜反驳测试：

- \(C_0\) 的五次多项式确切分解为线性乘四次；
- 齐次型确切为 (b(5a+7b)Q_4(a,b))，总次数 6、最大因子次数 ≤4；
- \(\\gcd(f,f')=1\) in \(\\mathbf F_7[x]\)，故无重根。

但本审计没有完成局部同余兼容的正式证明，也没有 Lean/Magma 内核收据；因此 A 的最终状态仍是 **Candidate / 非 kernel-verified**。路线 B 的一般天真降次已被无穷远分歧分析和模 7 无重根证书否定，但特殊参数退化 locus 未被穷尽。C、D 尚属开放研究假设。

可复核命令（均在指派 worktree 根目录执行）：

```bash
gs -q -dNOPAUSE -dBATCH -sDEVICE=txtwrite -sOutputFile=- \
  '29_noncyclic_class57.pdf'
gs -q -dNOPAUSE -dBATCH -sDEVICE=txtwrite -sOutputFile=- \
  'Counting imaginary quadratic fields with an ideal class group of 5-rank at least 2.pdf'
git diff --check
```

代数证书由同目录的 `verify-route-audit.py` 复现；它只使用 Python 标准库实现有限域 Euclidean gcd。观察值为 Byeon Lemma 4.2 的 \(m\) 与 BLT 的 \(f\) 均满足 gcd \(=1\) modulo \(7\)，且 \(C_0\) 因子展开系数逐项等于
`[2576, 8392, 11729, 8878, 3641, 640]`（升幂次序）。运行：

~~~bash
python3 mathematics/worker/verify-route-audit.py
~~~
