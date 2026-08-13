# 反例与边界审计：5-rank 至少 2 的虚二次域计数

## 结论先行

本审计**没有反驳** Bartz–Levin–Thamminana（BLT）2025 年论文的定理，也没有找到可支持研究计划书所拟指数改进的证据。准确的已知结论是渐近下界

\[
N^-_{5,2}(X)=\#\{K/\mathbf Q\text{ 虚二次}:|\Delta_K|\le X,
\operatorname{rk}_5\mathrm{Cl}(K)\ge2\}
\gg \frac{X^{1/3}}{(\log X)^2}.
\]

它不是渐近公式、上界或正密度结论；BLT 也未显式给出隐含常数和起始阈值。BLT 第 2 页定理 1.3 给出此下界；第 3 页定理 1.4 表明幂指数来自固定 genus $g$ 的模板 $1/(g+1)$，本例 $g=2$。

核心审计结论如下：

1. BLT 的有限计算只需提供一条合格 genus-2 曲线作为**存在性证书**。21,088 个参数三元组、548 条产出曲线和 85 个 $\mathbf Q$-同构类均不是二次域的计数，不能相加为更强的阶。
2. 互异二次域计数、薄集排除、局部条件和重数控制位于所引用的 Kulkarni–Levin（KL）定理中。若要改进指数或对数，应审计 KL 的二次 Hilbert 不可约性和二元型取值模平方部分，而非继续增加 BLT 候选曲线数。
3. 本地精确有限搜索覆盖所有 $-50,000\le D<0$ 的负基本判别式（15,195 个），找到 9 个 5-rank 至少 2 的例子；首个为 $D=-11199$。这仅是 `not_refuted_within_scope`。
4. 明确边界反例为 $D=-479$：$h(-479)=25$，但 $|\mathrm{Cl}(-479)[5]|=5$，所以 5-rank 仅为 1。“$25\mid h(D)$”并不等价于“5-rank 至少 2”。

## 1. 输入与证据边界

输入及本次读取哈希：

- `Counting imaginary quadratic fields with an ideal class group of 5-rank at least 2.pdf`，8 页，SHA-256 `1b63f04fa1daad0c16a76474bfdd91f7b8ffab01bfd1c55a550b2db75b82539b`。
- `Research Plan.pdf`，3 页，SHA-256 `af39b83d353d68de98f6db718313c5dea2c03b28cdc6be593119b111f716cb46`。
- BLT 第 6 页脚注 2 指向的公开作者代码 `Magma_Code/Section3Computations.magma`；本次只读网页，不把浮动 `main` 当作正式重现边界。
- KL 原论文 *Hilbert’s Irreducibility Theorem and Ideal Class Groups of Quadratic Fields*，尤其定理 1.2、1.3、2.1 及第 7–8 页对定理 1.3 的证明。

BLT 将 $\operatorname{rk}_m A$ 定义为使 $A$ 含有 $(\mathbf Z/m\mathbf Z)^r$ 的最大 $r$（第 1–2 页）。计划书以 $\dim_{\mathbf F_p}(\mathrm{Cl}(K)/p\mathrm{Cl}(K))$ 定义 $p$-rank；对有限阿贝尔群和 $p=5$，两者一致。有限搜索计算 $\ker([5]:\mathrm{Cl}(D)\to\mathrm{Cl}(D))$ 的大小：若为 $5^r$，5-rank 即为 $r$。

本轮 Lean、Magma、Sage、PARI/GP 不可用，故无 `kernel_verified` 主张。Python 结果是精确整数/有理数的有界证据；文末给出 PARI/GP 独立复验设计。

## 2. BLT 主结果的关键限制

### 2.1 计数命题

BLT 第 2 页定义 $N^-(m^r;X)$ 为满足 $|d_k|\le X$ 且 $\operatorname{rk}_m\mathrm{Cl}(k)\ge r$ 的**虚二次数域个数**。同页定理 1.3 断言

\[
N^-(5^2;X)\gg X^{1/3}/(\log X)^2.
\]

必须保留以下限定：

- 只计虚二次域，按绝对域判别式截断，每个域计一次。
- 是无条件渐近下界，不是精确渐近、上界或正密度。
- 只保证 5-rank **至少** 2；不分类完整 5-primary 结构，也不计“恰好 2”。
- 它改进 Byeon 的 $X^{1/4}$ 下界，但不说明新下界接近真实数量级。

### 2.2 计数引擎、局部条件与互异性

BLT 第 3 页定理 1.4（引用 KL）要求 $C/\mathbf Q$ 为光滑射影超椭圆曲线、有一个 $\mathbf Q$-有理 Weierstrass 点、genus 为 $g$，且 $m>1$；令

\[
r=\operatorname{rk}_m\operatorname{Jac}(C)(\mathbf Q)_{\rm tors},
\]

则 $N^-(m^r;X)\gg X^{1/(g+1)}/(\log X)^2$。BLT 取 $(g,m,r)=(2,5,2)$，故指数为 $1/3$。在这个固定曲线/固定模板内，“找到更多 genus-2 曲线”本身没有改变 $1/3$ 的机制。

KL 第 2 页定理 1.2 计数次数 2 映射的专门化：给定有限地方集合 $S$、局部邻域和薄集 $\mho$，高度 $H(\phi(P))\le B$ 的点产生 $\gg B^2/(\log B)^2$ 个**互异**二次域。KL 第 7–8 页将 $C$ 写成奇次数首一模型 $y^2=f(x)$，取坏约化素数集合 $S$，以 $p$-进邻域强制这些素数分歧，以实处邻域控制实/虚符号，并排除薄集；同时

\[
|d_{\mathbf Q(P)}|\le c'B^{2g+2}.
\]

令 $B=(X/c')^{1/(2g+2)}$，即得到 $X^{1/(g+1)}/(\log X)^2$。因此：

- **互异性/重数控制**来自 KL 对平方自由部分 $t$ 的计数，二次域写为 $\mathbf Q(\sqrt t)$；它不来自 BLT 候选曲线列表。
- **局部条件**是类群秩结论和“虚二次”符号控制的一部分，不能任意删除。
- **对数损失**继承自 KL 第 4 页定理 2.1 所用 Stewart–Top 型平方自由值计数 $\gg x^{2/r}/(\log x)^2$；BLT 没有证明此损失最优。

### 2.3 几何构造与排除参数

BLT 第 3–4 页使用带有有理 10-挠点的椭圆曲线 $E_t,E_u$，令

\[
\Delta_{10}(v)=(2v-1)(4v^2-2v-1).
\]

两个 2-挠 Galois 模相同的条件等价于第 4 页方程

\[
(2t-1)^5(4t^2-2t-1)z^2=(2u-1)^5(4u^2-2u-1). \tag{2.3}
\]

第 5 页定理 2.1 另要求：

- $t,u\notin\{0,1/2,1\}$；
- 系数 $a\ne0$，即排除正文给出的一个 $z$ 的有理函数值；
- $a_6\ne0$ 且六次多项式可分，从而确为光滑 genus-2 曲线。

第 6 页证明还核对六次判别式的因子只来自 $a,a_6,t,t-1,2t-1,t^2-3t+1,4t^2-2t-1$ 等。所得 $(2,2)$-isogeny 次数为 4，与 5 互素，才可传递两个独立 5-挠方向。第 3 页的 Weil-pairing 上界给出在 $\mathbf Q$ 上 5-rank 不超过 genus 2，故这里恰为 2。

### 2.4 有限计算筛选到底证明了什么

BLT 第 6 页第 3 节对分子、分母绝对值均不超过 100 的既约有理数 $t,u$ 搜索，报告：

- 21,088 个合格 $(t,u,z)\in\mathbf Q^3$；
- 548 条有有理 Weierstrass 点的 genus-2 曲线；
- 85 个 $\mathbf Q$-同构类。

作者的 `Section3Computations.magma` 显示：先按 $\Delta_{10}$ 的平方类配对参数，加入 $(t,u,\pm z)$ 和 $(u,t,\pm z^{-1})$，并排除令 $a=0$ 的根；随后用 `#Roots(g) gt 1` 检测有理根，以 `IsIsomorphic` 去曲线同构，再用 `HasOddDegreeModel` 和 Jacobian torsion invariants 复核 85 个代表。$21088\to548\to85$ 本身即显示参数交换、$z$ 符号和同构导致的大量重数。

第 6–7 页给出样本

\[
(t,u,z)=(2/3,-1/3,25)
\]

及奇次数模型

\[
C_0:y^2=(5x+7)(128x^4+549x^3+1007x^2+936x+368).
\]

第 7 页称 Magma 验证 $\operatorname{Jac}(C_0)(\mathbf Q)_{\rm tors}\cong\mathbf Z/5\mathbf Z\times\mathbf Z/10\mathbf Z$。定理 1.3 只需 $C_0$（或另外 84 条中的任一条）存在。上述三个搜索数字不是二次域数，也不能用于改善下界的阶。

## 3. 与研究计划书的证据对照

| 计划书主张/目标 | 支持证据线 | 反驳或边界证据线 |
|---|---|---|
| 当前基准为 $X^{1/3}/(\log X)^2$ | 计划书第 1 页定理 1；BLT 第 2 页定理 1.3 | 必须表述为充分大 $X$ 的 `\gg` 下界；不能据此预测小 $X$。 |
| 几何 torsion 与定量专门化构造所需域 | 计划书第 2 页；BLT 第 3 页定理 1.4 和第 3–7 页构造 | “很多曲线”不是“更多互异域”；域计数与去重由 KL 完成。 |
| 查明 $1/3$ 与 $(\log X)^{-2}$ 的来源 | KL 的判别式界给 $2g+2=6$，与 $B^2/(\log B)^2$ 合成为目标下界 | 固定 genus-2/KL 模板内，扩大 BLT 参数搜索不能改变损失。 |
| 寻找 $\delta>0$ 使指数 $>1/3$ | Cohen–Lenstra 启发式给研究动机 | 启发式不是无条件下界；有限数据不能证明任何 $\delta$。 |
| 长期研究“频率/分布” | $N^-_{5,2}(X)$ 是合法计数函数 | BLT 没有渐近常数、匹配上界、密度或误差项。把下界外推成分布结论是逻辑跃迁。 |

建议计划书在“Known Results”后补明：benchmark 只是一侧下界；所谓更强行为属于启发式目标，并非 BLT 已支持的经验分布结论。

## 4. 高风险边界案例与隐藏假设测试

### T1. 类数可除性偷换为 5-rank

**风险：** 用 $25\mid h(D)$ 作为 $\operatorname{rk}_5\mathrm{Cl}(D)\ge2$ 的判据；循环群 $\mathbf Z/25\mathbf Z$ 的 5-rank 只有 1。

**失败信号：** $25\mid h(D)$ 但 $|\mathrm{Cl}(D)[5]|=5$。

**结果：** $D=-479$ 满足 $h=25$，但 5-挠核大小为 5，5-rank 为 1；简化判据已被反例击破。

### T2. 参数/曲线重数偷换为互异域数

**风险：** 将不同 $(t,u,z)$、模型或曲线的 KL 下界直接相加。参数存在 $t\leftrightarrow u$、$z\leftrightarrow-z$、模型变换和曲线同构重数；不同曲线产生的域集合也可能重叠。

**失败信号：** 没有将域判别式平方自由化和全局去重，就声称常数倍 85 或更高指数。

**结果：** BLT 的 $21088\to548\to85$ 已显示参数层重数；论文未给 85 个专门化域集合的交集上界，故跨曲线求和不成立。

### T3. 退化/坏参数未排除

**风险：** 只检查 (2.3)，却未检查 $t,u\notin\{0,1/2,1\}$、$a\ne0$、六次式可分、椭圆曲线非奇异和拼接非退化。

**失败信号：** $a=0$、$a_6=0$、六次判别式为 0、genus 下降，或不再得到所需光滑 genus-2 曲线。

**结果：** 对样本 $(2/3,-1/3,25)$，本地精确计算得 (2.3) 两边均为 $-3125/2187$，且 $a=2048/243\ne0$。这只复核两个必要条件；完整可分性与 Jacobian torsion 仍需 Magma/Sage 独立重放。

### T4. 有理 5-挠与独立 5-rank 2 混淆

**风险：** 两个 5-挠点可能相关，或经过次数被 5 整除的 isogeny 后丢失。

**失败信号：** 生成子群只有 5 个元素、isogeny kernel 含 5-primary 部分，或 torsion invariants 不含两个 5 因子。

**边界控制：** BLT 的两个 degree-2 映射产生 degree-4 的 $(2,2)$-isogeny，4 与 5 互素；对 $C_0$ 又报告 $\mathbf Z/5\times\mathbf Z/10$。任何新构造都必须重新核验。

### T5. 省略局部条件、薄集或符号控制

**风险：** 从“很多有理参数”直接断言每个参数产生虚二次域且类群秩不降。

**失败信号：** $f(x_0)$ 成平方、得到实二次域、坏约化使 pullback 论证失效，或落入 KL 薄集使 torsion 类不独立。

**边界控制：** KL 第 7–8 页显式选择坏约化集合 $S$、互素 $M,N$、$p$-进邻域、实处符号邻域和薄集排除。新参数化必须重建这些条件。

### T6. 从下界外推分布/正密度

**风险：** 把 $\gg X^{1/3}/(\log X)^2$ 读成 $N(X)\asymp X^{1/3}/(\log X)^2$，或把 Cohen–Lenstra 动机当成已证明正密度的一部分。

**失败信号：** 无匹配上界或渐近公式却报告比例、典型概率或渐近常数。

**边界控制：** 始终分开标记已证明下界、启发式预测和有限实验频率。

## 5. 可复现有限搜索与边界记录

脚本：`mathematics/worker/counterexample_finite_search.py`

输出：`mathematics/worker/counterexample-finite-search-output.txt`

```bash
python3 mathematics/worker/counterexample_finite_search.py --bound 50000
```

算法对每个负基本判别式 $D$：

1. 枚举全部本原约化正定二元二次型 $[a,b,c]$，其数目为类数；
2. 通过对应二次序理想乘法实现 Gauss composition；
3. 计算满足 $[f]^5=1$ 的类的个数 $|\mathrm{Cl}(D)[5]|$；
4. 若该数至少 25，则 5-rank 至少 2；另记录 $25\mid h(D)$ 但 rank 小于 2 的边界。

内部护栏核对 $h(-3)=h(-4)=1$ 与 $\mathrm{Cl}(-23)$ 的 3 阶群结构，并精确复核 BLT 样本的 (2.3) 与 $a\ne0$。脚本 SHA-256 为 `220f4a952477d95132ced43eafc1bf4a36d1bd04731497f58b643164eb1b4f37`；输出 SHA-256 为 `12cc6a5216fb4f00f899345c988af064aefbc5b23becd75fc0ee1918e01d8115`。

运行摘要：

- 搜索 15,195 个负基本判别式；
- 5-rank 至少 2 的记录有 9 个：$-11199,-12451,-17944,-30263,-33531,-37363,-38047,-39947,-42871$；
- $D=-11199$ 有 $h=100$、$|\mathrm{Cl}[5]|=25$；
- 有 445 个 $25\mid h(D)$ 但 5-rank 小于 2 的记录，第一个是 $D=-479$。

输出与公开文献表中 $D=-11199$ 为最小 5-rank 2 虚二次基本判别式的记录相容，但仍只应视为可重放的有限证据。

### PARI/GP 独立复验设计

```gp
qpoly(D) = if(D % 4 == 1, x^2-x+(1-D)/4, x^2-D/4);
forstep(D=-3, -50000, -1,
  if(isfundamental(D),
    my(B=bnfinit(qpoly(D)), r=sum(i=1,#B.cyc,B.cyc[i]%5==0));
    if(r>=2, print(D," ",B.cyc))
  )
)
```

另打印 `bnfinit(qpoly(-479)).cyc` 与 `bnfinit(qpoly(-11199)).cyc`。若安装版本无 `isfundamental`，应使用等价的平方自由判别式判断。决定性失败信号为：

- `D=-11199` 的 `cyc` 中少于两个不变量被 5 整除；
- `D=-479` 的 `cyc` 中至少两个不变量被 5 整除；
- 脚本列出的任一 $D$ 不是基本判别式。

完整验证 $C_0$ 仍需 Magma/Sage 的 genus-2 Jacobian torsion、曲线同构、奇次数模型和可分性能力；PARI/GP 类群检查不能替代几何验证。

## 6. 证据平衡与证伪结局

**支持线：** BLT 定理 1.3、1.4 给出下界及曲线归约；BLT 第 4–7 页给出显式 $C_0$；本地检查通过样本的 (2.3) 与 $a\ne0$；有限搜索在声明范围内找到 9 个 5-rank 至少 2 的域。

**反驳/边界线：** $D=-479$ 反驳类数可除性简化；参数、模型、曲线、域是不同对象；KL 的局部/薄集条件和平方自由去重不能省略；当前材料没有上界或分布定理；本轮没有 Lean/Magma/Sage/PARI 的独立重放。

**任务层证伪：** 假设“本任务可产出有用审计与可复现有限检查”经产物和输出而 `survived`；失败标准未触发。

**数学层结局：** 在 $-50,000\le D<0$ 的全部负基本判别式内，脚本找到 9 个正例，首个为 $D=-11199$。结论为 **`not_refuted_within_scope`**，不是范围外的普遍最小性证明，更不是 BLT 渐近下界的证明。替代命题“$25\mid h(D)$ 当且仅当 5-rank 至少 2”则由 $D=-479$ **`refuted_within_scope`**。

## 7. 下一步最便宜的决定性检查

1. 在固定版本 PARI/GP 上独立核对全部 454 个 $25\mid h(D)$ 的记录（9 个 rank 至少 2，445 个 rank 小于 2），保存 `bnf.cyc` 和版本。
2. 冻结作者 Git 提交而非浮动 `main`，在 Magma 重放 `Section3Computations.magma`；若只关心定理，优先核验 $C_0$ 的可分性、genus 和 Jacobian torsion。
3. 若目标是改善 $(\log X)^{-2}$，审计 KL 定理 2.1 的 Stewart–Top 输入；若目标是指数 $>1/3$，需提出高度—判别式次数更优或参数维数更高且重数可控的新机制。扩大 BLT 的 $t,u$ 搜索范围不是决定性检验。

## 资料锚点

- BLT：第 2 页定理 1.3；第 3 页定理 1.4 与 Weil-pairing 限制；第 4 页 (2.3)；第 5 页定理 2.1；第 6 页光滑性证明、Remark 2.2、搜索范围和脚注代码；第 7 页 $C_0$ 与 torsion。
- Research Plan：第 1 页定义、启发式、已知下界；第 2 页对数/指数改进目标；第 3 页长期分布视角。
- KL：第 2 页定理 1.2–1.3；第 4 页定理 2.1；第 7–8 页局部条件、判别式界和实/虚分支。
- 作者计算：`https://github.com/amantham20/Rank5Quadratics-Research/blob/main/Magma_Code/Section3Computations.magma`（读取于 2026-08-13；重放前须冻结 commit）。
