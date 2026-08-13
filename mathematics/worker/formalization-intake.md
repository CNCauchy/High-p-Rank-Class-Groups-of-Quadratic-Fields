# Cohen–Lenstra 子问题：形式化预检与假设台账

## 结论

计划书选择的对象是虚二次域的理想类群，当前核心计数函数是

\[
N^-_{5,2}(X)=\#\{[K]_{\mathbf Q}: [K:\mathbf Q]=2,\ K\text{ 无实嵌入},\
|\operatorname{Disc}K|\le X,\ \dim_{\mathbf F_5}(\mathrm{Cl}(K)/5\mathrm{Cl}(K))\ge2\}.
\]

这里按 `Q`-同构类计数。计划书的已知基线是

\[
N^-_{5,2}(X)\gg \frac{X^{1/3}}{(\log X)^2},
\]

主研究目标不是一条已知定理，而是寻找固定、明确的 `δ>0`，把指数提高到
`1/3+δ-o(1)`。本文给出一个保守的精确候选 `EXP-EPS`，并保留“explicit”是否还要求
可计算常数这一未消歧点。结论状态为 **formalized candidate / not proved**；Lean 在共享预检中不可用，
本文没有 Lean 文件、kernel receipt 或 `kernel_verified` 声明。

## 来源与核对方法

页码均指 PDF 物理页（括号中同时给出论文印刷页码，如有）。文本锚点是可在
Ghostscript `txtwrite` 输出中搜索的短语；公式符号另由 150 dpi 页面图像目视核对。

| 来源 | SHA-256 | 决定性位置与锚点 |
| --- | --- | --- |
| `Research Plan.pdf` | `af39b83d353d68de98f6db718313c5dea2c03b28cdc6be593119b111f716cb46` | PDF p.1: “For a prime p, define the p-rank”; “We focus on imaginary quadratic fields and define”; “Theorem 1 (Bartz–Levin–Thamminana, 2025)”. PDF p.2: “Problem 1. Improve the quantitative lower bound”; “A first possible level of progress”; “Research Goal 1. Prove that there exists an explicit δ > 0”. |
| `Counting imaginary quadratic fields with an ideal class group of 5-rank at least 2.pdf` | `1b63f04fa1daad0c16a76474bfdd91f7b8ffab01bfd1c55a550b2db75b82539b` | PDF p.1: abstract “5-rank at least 2”. PDF p.2（印刷 p.2）: definition “we let N−(m^r; X) denote”; Theorem 1.3 “We have”. PDF p.3（印刷 p.3）: Theorem 1.4 and “in order to prove Theorem 1.3”. PDF p.7（印刷 p.7）: “combined with Theorem 1.4 finishes the proof of Theorem 1.3”. |
| `29_noncyclic_class57.pdf` | `0b135b2651241d21d7b8f6bce9bf995d4f1fc4db1762bc64defb54bd014ee3cd` | PDF p.1（印刷 p.1）: abstract “noncyclic 5 or 7-class group”. PDF p.2（印刷 p.2）: Theorem 1.1 “If g = 5 or 7”; condition “subgroup isomorphic to Z/gZ × Z/gZ”. PDF p.7（印刷 p.7）: “Proof of Theorem 1.1” concludes from the degree-8 binary form and square-free-value estimate. |

可复现抽取命令（从指派工作树根运行）：

```sh
gs -q -dNOPAUSE -dBATCH -sDEVICE=txtwrite -sOutputFile=/tmp/research-plan.txt 'Research Plan.pdf'
gs -q -dNOPAUSE -dBATCH -sDEVICE=txtwrite -sOutputFile=/tmp/counting-5rank.txt 'Counting imaginary quadratic fields with an ideal class group of 5-rank at least 2.pdf'
gs -q -dNOPAUSE -dBATCH -sDEVICE=txtwrite -sOutputFile=/tmp/noncyclic-class57.txt '29_noncyclic_class57.pdf'
```

若要核对单页，可加 `-dFirstPage=2 -dLastPage=2`。本次使用 Ghostscript 10.07.0；
`txtwrite` 会丢失或错排部分 `≫`、上下标和分式，因此不能只依赖整篇纯文本。

## 定义规范化

1. `K` 是 `Q` 的二次扩张且无实嵌入，即虚二次域；等价地，域判别式
   `Disc(K)<0`。计数限制使用绝对值 `|Disc(K)|≤X`。
2. `Cl(K)` 是有限理想类群，
   `rk_5 Cl(K) := dim_{F_5}(Cl(K)/5Cl(K))`。这与 Bartz–Levin–Thamminana
   对有限阿贝尔群采用的“最大的 `r`，使其含 `(Z/5Z)^r` 子群”的定义等价。
3. `N^-_{5,2}(X)` 按域的 `Q`-同构类计数。Bartz–Levin–Thamminana 写作
   `N^-(5^2;X)`：这里 `5^2` 是其 `N^-(m^r;X)` 记号中的 `(m,r)=(5,2)`，
   不是“25-rank”。
4. `f(X)≫g(X)` 被展开为：存在 `c>0,X_0>1`，使每个实数 `X≥X_0`
   都有 `f(X)≥c g(X)`。带 `ε` 时允许 `c` 和 `X_0` 依赖 `ε`，但不依赖 `X`。
5. “5-class group noncyclic”在本文只指 `Cl(K)` 的 Sylow-5 子群非循环；对有限阿贝尔群，
   它等价于 `rk_5 Cl(K)≥2`，也等价于含 `(Z/5Z)^2` 子群。它不等价于不带
   5-primary 限定的“整个类群非循环”。

## 精确候选命题

### `EXP-EPS`：主保守候选

**任务型形式陈述。** 产生一个具体的 `δ∈Q_{>0}`，并证明

\[
\forall\varepsilon\in\mathbf R_{>0}\ \exists c_\varepsilon>0\ \exists X_\varepsilon>1\
\ \forall X\in\mathbf R,\quad
X\ge X_\varepsilon\Longrightarrow
N^-_{5,2}(X)\ge c_\varepsilon X^{1/3+\delta-\varepsilon}.
\]

其规范化文本（ASCII、单行、末尾无换行）是：

```text
EXISTS delta IN Q_{>0} SUCH THAT FOR ALL epsilon IN R_{>0} THERE EXIST c_epsilon IN R_{>0} AND X_epsilon IN R_{>1} SUCH THAT FOR ALL X IN R WITH X >= X_epsilon, N_5,2^-(X) >= c_epsilon * X^(1/3 + delta - epsilon), WHERE N_5,2^-(X) IS THE NUMBER OF Q-ISOMORPHISM CLASSES OF FIELDS K WITH [K:Q] = 2, K HAS NO REAL EMBEDDING, |Disc(K)| <= X, AND dim_F5(Cl(K)/5Cl(K)) >= 2.
```

`statementHash = 6c6e7cf3f3128a0423dd33cc64e4bd57bbcd622caf92d96776f76158edf02d49`。

与计划书原意的关系：**unknown（条件性 equivalent）**。若把计划书的
`X^{1/3+δ-o(1)}` 按解析数论常用方式解释为“对每个固定 `ε>0` 允许指数损失 `ε`”，
并把“explicit δ”解释为证明中实际给出一个固定正有理数，则本候选与 Research Goal 1
等价。计划书没有写出 `ε`、隐常数的依赖关系，也没有形式定义“explicit”，所以无条件标签保持
`unknown`，不得静默消歧。

### `EXP-EFFECTIVE`：非等价的更强交付候选

要求产生 `δ∈Q_{>0}` 以及算法 `C,T`，使每个有理 `ε>0` 上 `C(ε)>0,T(ε)>1`
均可实际计算，并对所有实数 `X≥T(ε)` 有
`N^-_{5,2}(X)≥C(ε)X^{1/3+δ-ε}`。

规范化文本哈希为
`c1af02c5316e2c00d97adb1a00d9565821c7d602d3d24737f6e9729f703a8e0a`（完整文本在
`formalization-intake.json`）。关系：**stronger**，因为计划书只明确要求 `δ` 显式，未要求
所有隐常数和阈值可计算。这是应保留而不自行采用的另一读法。

### 计划书还明确列出的较低目标

| ID | 精确化 | statementHash | 与计划书原意 |
| --- | --- | --- | --- |
| `LOG-IMPROVEMENT` | `∃α<2,c>0,X_0>1,∀X≥X_0: N^-_{5,2}(X)≥cX^{1/3}/(log X)^α` | `48c7bda4e674f2bb3a12217eda782f843a012d88b867c1fe53ce66f428c5342e` | **equivalent** 于 p.2 “for example … α<2”的标准 `≫` 展开；它是“first possible level”，不是主 Research Goal 1。 |
| `NO-LOG` | `∃c>0,X_0>1,∀X≥X_0: N^-_{5,2}(X)≥cX^{1/3}` | `234b34d918c1ce566f2aac5b9ad9f78e9c8abdb89918d4d97fecac8078a806b0` | **equivalent** 于 p.2 “or, more strongly”；比 `LOG-IMPROVEMENT` 的存在型表述更强。 |
| `CL-POSITIVE-FREQUENCY` | 若 `Q^-(X)` 计数所有 `|Disc(K)|≤X` 的虚二次域，则 `liminf_{X→∞}N^-_{5,2}(X)/Q^-(X)>0` | `80cbdf9353b77ef10b9485c1a599618f3dba344579c515bc7c8c0b9ef30ebe15` | **weaker** 于“存在正的极限密度”的常见精确化；计划书仅说 Cohen–Lenstra “predict … positive frequency”，未给常数或极限方式，故它只是保守启发式候选，不是本轮要证明的目标。 |

在 `EXP-EPS` 下，任取 `ε<δ` 就得到比 `X^{1/3}` 更大的幂次，故
`EXP-EPS ⇒ NO-LOG ⇒ LOG-IMPROVEMENT ⇒` 当前基线。正频率预测的量级约为线性，远强于这些目标，
但计划书及两篇论文都没有把它当作已证明结论。

## 已知基线与两篇论文的关系

### Byeon（2009）

Byeon 的 Theorem 1.1（PDF p.2）称：对 `g=5` 或 `7`，分别对虚二次域和实二次域，
含 `Z/gZ×Z/gZ` 子群且绝对判别式至多 `x` 的域数 `≫x^{1/4}`。限制到 `g=5`
和虚二次域后，由有限阿贝尔群等价性，这正是

\[
N^-_{5,2}(X)\gg X^{1/4}.
\]

规范化哈希为 `0a31f4b4a375e338f944fe1eab68561d79a5a3d424113d55d375a11b17123bec`。
与计划书 p.1 对 Byeon 的陈述关系：**equivalent（取上述限制后）**；Byeon 原定理本身范围更广，
还包括 `g=7` 和实二次域。论文 p.7 的证明把次数 8 的二元型与 Stewart–Top 的无平方值计数结合，
产生指数 `2/8=1/4`。

### Bartz–Levin–Thamminana（2025）

该文 PDF p.2 先定义 `N^-(m^r;X)`，随后 Theorem 1.3 给出

\[
N^-(5^2;X)\gg \frac{X^{1/3}}{(\log X)^2}.
\]

按其定义及素数 `5` 的群论等价，这与计划书的 `N^-_{5,2}` 基线
**equivalent**。规范化哈希为
`824e395028a3a2df3d655ab1e8a32203acbc582c5458e6bfe69332f62e5f3aad`。

关系链也解释了计划书要审计的两个损失：论文 p.3 的 Theorem 1.4 对 genus `g` 给出
`X^{1/(g+1)}/(log X)^2`；同页说明，为证 Theorem 1.3，只需找到 genus-2、带有理
Weierstrass 点且 Jacobian 的 5-rank 为 2 的曲线。因此 `g=2` 直接给出指数 `1/3`，而
`(log X)^{-2}` 已存在于所调用的定量专门化定理中。论文 p.7 给出具体曲线并说与 Theorem 1.4
结合即完成 Theorem 1.3。这里是来源结构说明，不是对“任何方法均不可能改进”的断言。

## 假设台账

| ID | 假设/约定 | 状态 | 若改变会怎样 | 来源 |
| --- | --- | --- | --- | --- |
| `A01` | 按 `Q`-同构类计数虚二次**域**，不是按方程或根式表示计数。 | explicit normalization | 按表示计数会重复同一域，改变计数函数。 | 三份来源均说 number fields；计划书 p.1 定义集合。 |
| `A02` | 使用域判别式，且 `|Disc(K)|≤X`；`X` 为趋于无穷的实参数。 | explicit | 改成任意次序判别式或生成多项式判别式会改变对象和高度。 | 计划书 p.1；两论文主定理页。 |
| `A03` | `rk_5 Cl(K)=dim_F5(Cl(K)/5Cl(K))`。 | explicit | 把它读成 25-rank、5-adic rank 或仅“5 整除类数”均改变条件。 | 计划书 p.1；Bartz et al. pp.1–2。 |
| `A04` | “noncyclic 5-class group”指 Sylow-5 子群非循环。 | derived/terminological | 若“noncyclic”修饰整个 `Cl(K)`，则不等价于 5-rank≥2。 | Byeon 标题、p.2 定理的 `(Z/5Z)^2` 条件。 |
| `A05` | `≫` 的常数对 `X` 一致；在 `EXP-EPS` 中可依赖 `ε`。 | conventional, made explicit | 允许常数依赖 `X` 会令下界近乎空泛。 | 所有三个 PDF 使用 `≫`，未逐字量化。 |
| `A06` | `δ` 必须在量词 `X` 之前固定，且主候选取显式有理数。 | conservative normalization | 若 `δ=δ(X)→0`，并不构成固定幂次改进。 | 计划书 p.2 “there exists an explicit δ>0”。 |
| `A07` | `-o(1)` 按“每个固定 `ε>0` 的指数损失”读。 | unresolved convention | 计划书未指明 `o(1)` 的函数、符号、均匀性或隐常数依赖；故 alignment 仅条件等价。 | 计划书 p.2 Research Goal 1。 |
| `A08` | 结果应为无条件下界。 | explicit by source context | 引入 abc、GRH 等会得到不同命题，必须生成新 statementHash。 | Bartz et al. p.2 明说相关更好结果可能 conditional on abc，而 Theorem 1.3 无条件。 |
| `A09` | `log` 取自然对数；换固定底只改变 `≫` 常数。 | harmless convention | 不影响下界等价类，但机器陈述需固定。 | 公式中的 `log X`。 |
| `A10` | Cohen–Lenstra 在此仅作启发式比较基线，不作前提。 | explicit | 把启发式当假设会把无条件研究目标改成条件命题。 | 计划书 pp.1–2。 |
| `A11` | “explicit”至少要求提交具体 `δ`；是否还要求 `c_ε,X_ε` 可计算未定。 | unresolved | 采用可计算版本得到严格更强的 `EXP-EFFECTIVE` 交付义务。 | 计划书 p.2 只修饰 `δ`。 |
| `A12` | 当前形式化是非形式化数学规范，不是 Lean 定理。 | explicit tool boundary | 没有 kernel receipt 就不得标记 verified。 | 共享预检：Lean 当前不可用。 |

## 最小语义失败测试与反证结果

1. **把 `rk_5≥2` 弱化为 `5 | #Cl(K)`：已反驳。** 最小抽象群见证
   `A=Z/5Z` 满足 `5|#A`，但 `dim_F5(A/5A)=1`，不是 2。
2. **把“5-class group noncyclic”宽化为“整个类群 noncyclic”：已反驳。**
   `A=Z/2Z×Z/2Z` 非循环，但 `A/5A=0`，5-rank 为 0。
3. **交换 `EXP-EPS` 的量词为存在同一 `c>0` 对所有 `ε>0` 有效：已反驳其等价性。**
   模型函数 `f(X)=X^a/log X` 对每个 `ε>0` 都满足 `f(X)≫_ε X^{a-ε}`；若同一
   `c` 对所有 `ε` 有效，令 `ε↓0` 会强迫 `f(X)≥cX^a`，这与 `1/log X→0` 矛盾。
4. **允许 `δ` 依赖 `X`：已反驳其“指数改进”含义。** 取 `δ(X)=1/log X`，则
   `X^{1/3+δ(X)}=eX^{1/3}`，只改变常数而没有固定正幂次增益。
5. **把 `N^-(5^2;X)` 读成 25-rank：被来源定义直接否定。** Bartz et al. PDF p.2
   明确先定义 `N^-(m^r;X)` 为 `rk_m Cl(k)≥r`，故这里是 `m=5,r=2`。

这些测试支持当前对象、条件和量词的必要性；它们不证明 `EXP-EPS`。支持证据仅为来源一致性和
定义等价；反驳搜索对主数论命题尚未运行，因此主命题状态保持 **inconclusive / open**。

## 剩余歧义与下一步

- 需由 Lead/研究者确认 `X^{1/3+δ-o(1)}` 是否采用 `EXP-EPS` 的标准 ε-损失语义；在确认前
  relation 保持 `unknown`。
- 需决定“explicit”是否仅要求列出 `δ`，还是采用更强的 `EXP-EFFECTIVE` 并追踪所有常数。
- 计划书的“positive frequency”没有给出 Cohen–Lenstra 的精确局部因子或目标密度常数；如要把
  启发式升级为比较定理，应另开来源审计并生成新 statementHash。
- 下一证明泳道应固定 `EXP-EPS` 的 hash 后，逐条重构 Bartz et al. Theorem 1.4 的依赖，区分
  genus 导致的 `1/(g+1)` 与定量专门化导致的 `(log X)^{-2}`；任何新增条件都必须改 hash。
