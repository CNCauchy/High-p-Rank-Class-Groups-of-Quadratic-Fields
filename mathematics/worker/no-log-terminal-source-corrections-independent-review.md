# NO-LOG 终局原文修正独立对抗审阅

## 最终状态

**CANDIDATE**，绑定冻结基提交
`157331ec86dc64dbf0f99f6a545ed1be74926800`。

六项被指定的 ST/KL/BLT 来源接口均经受住了本轮破坏测试，但其中不全是原文定理的
字面结论：端点避让、偶次齐次性的参数注入、共轭点至域的至多二对一修正，以及
实数盒到整数盒的取整，都是需要显式保留的初等附加步骤。ST printed p.951 的剩余类
方向和 p.953 的最终对象名确有错误；前者因端点避让而完全不进入当前路线，后者由其
紧前的 (13)--(15) distinct-value 段落修复。没有发现新的致命缺口，因此不判
`REFUTED` 或 `BLOCKED`；但本结论只说指定的来源接口闭合，绝不自动升级为整个
NO-LOG 定理 `PROVED`，也不是 `VERIFIED`。

本轮不做联网、文献新颖性搜索、曲线重搜或 Lean 复核，也不涉及 EXP-EPS。

## 冻结来源与审阅边界

本轮直接读取下列原始 PDF，并用最新 Lead 审计定位待挑战的修正；另重放先前独立反例
commit `c9f980b13d9d818bbf978fe693ffa017e392fb4f`，没有把 Lead 的积极判断当作裁决。

| 来源 | 本地身份 | 使用锚点 |
| --- | --- | --- |
| C. L. Stewart、J. Top, *On Ranks of Twists of Elliptic Curves and Power-Free Values of Binary Forms*, JAMS 8 (1995), 943--973 | 31 页，3,510,691 bytes，SHA-256 `96fb376bf0d8a4d3b70338a89b630a5e26c3cb0354be90da8cf2224d2603ba97` | printed pp.948--953，尤其定义、Thm. 1 proof 与 (10)--(15) |
| Kaivalya R. Kulkarni、Aaron Levin, *Hilbert's Irreducibility Theorem and Ideal Class Groups of Quadratic Fields*, Acta Arith. 205 (2022), 371--380，arXiv:2111.15582v1 | 9 页，161,972 bytes，SHA-256 `26a9e645b55d70a253be2017cc8d656be188ed9c02350c21884286c60b015aae` | PDF pp.6--8，Lemmas 3.1--3.2、Thm. 1.2 proof、Thm. 4.1 与 Thm. 1.3 proof |
| L. Bartz、A. Levin、A. Thamminana, *Counting imaginary quadratic fields with an ideal class group of 5-rank at least 2*, Ramanujan J. 68 (2025), article 26 | 8 页，212,239 bytes，SHA-256 `1b63f04fa1daad0c16a76474bfdd91f7b8ffab01bfd1c55a550b2db75b82539b` | PDF p.7 的固定曲线 `C0` 与已发表 Magma torsion 输入 |

最新定位材料为
`mathematics/worker/no-log-st-lead-original-source-audit.md` 与
`mathematics/worker/no-log-kl-blt-lead-source-audit.md`；本审阅对其每个决定性修正另作
代数失败测试。原始页码判断优先于项目摘要。

## 六项逐义务裁决

### 1. KL `N1` 自由度、复合顺序和有限端点避让

**锚点。** KL Lemma 3.1（PDF p.6）先固定有限 place 集 `S` 与 `epsilon>0`，然后说
取一个整数 `N>1/epsilon`，并定义

\[
\psi(t)=\frac{1-Nt}{1+Nt},\qquad
\tau(s)=\psi^{-1}(s)=\frac{1-s}{N(1+s)}.
\]

原文不是只给一个特殊 `N`：任一超过阈值的整数都满足实端条件。又因
`psi^{-1}(1)=0`，原文随后才取 `A=B=1`，再令 `M` 含有限坏素数的充分高幂。
同页 Thm. 1.2 proof 的实际复合顺序是

\[
s=a/b=\psi(\phi(P)),\qquad \phi(P)=\tau(s),
\]

不是反序复合。当前虚二次平移写成 `phi=u+N0/M0`，故旧坐标

\[
u=\tau(s)-N_0/M_0.
\]

最终齐次六次分支型在 `s=0,infinity` 的两个端点非零，恰等价于

\[
g(-N_0/M_0+1/N_1)\ne0,\qquad
g(-N_0/M_0-1/N_1)\ne0.
\]

固定平方自由五次 `g` 只有有限根；每个等式对正整数 `N1` 至多排除有限个值。因此先
固定 `C0,S,N0/M0,phi,Omega,epsilon`，再从所有 `N1>1/epsilon` 中避开有限禁集，
最后取 `A=B=1,M`。`N1` 增大只缩小实邻域；有限 place 的保持由选定 `N1` 后的
`M` 完成。正比值 `a/b>0` 始终落入 `tau((0,infinity))=(-1/N1,1/N1)`，故固定
负号邻域/正锥也保留。PGL2 换元不改变射影不可约因子次数；`C0` 的奇五次分支加
无穷远分支为 `1+1+4`，所以最终六次型最大因子次数仍为 4。

**失败测试。** 用 `C0` 的线性根 `-7/5` 人为取
`N0/M0=7/5+1/23`，并要求 `N1>20`；则 `N1=23` 确实使正端点命中根，而
`N1=21` 不命中。故“随便取第一个足够大的 `N1`”是错误推理，而有限避让确实能修复。

**分类与裁决：source explicit（自由度、复合顺序、局部保持） + additional
elementary finite-avoidance lemma；通过。** 数值模数 `M` 必须在 `N1` 后固定；所谓
“局部条件已固定”指 place、邻域和目标同余要求已固定，不是把最终 `M` 提前冻结。

### 2. ST p.951 的 `SL2` 剩余类方向错误是否完全未用

**锚点。** ST printed p.951 在首项或尾项为零时才引入 `L in SL2(Z)` 并令
`F_L=F o L`。其印刷文字把新同余类写成 `L(A,B)`，但保持原值集合所需的是
`L^{-1}(A,B)`。

**失败测试。** 模 5 取 `F(X,Y)=X`、原类 `(0,1)` 及
`L=[[1,1],[0,1]]`。印刷的新类 `(1,1)` 给 `F_L=2 mod 5`，原类却给
`F=0 mod 5`；逆像类 `(4,1)` 才给 `F_L=0 mod 5`。方向错误真实存在。

第 1 项已在调用 ST 之前保证最终六次型首尾系数都非零。因此 p.951 的条件分支根本
不执行；后续正盒 `1<=a,b<=u` 与固定类都是 KL 给出的原坐标。这里不是“错误虽用到但
无害”，而是“错误代码路径不可达”。

**分类与裁决：source-explicit typo + immediate non-use deduction；通过，但最终证明
必须明确跳过该分支。** 若端点避让被删除，此项立即退化为 `changes requested`。

### 3. ST p.953 pairs / distinct values 对象名错误

**锚点。** ST printed p.952 定义 `T` 为正盒、固定同余类中的参数 pair 集；p.953
(10) 给 `|T| >> u^2`。(11) 固定一个常见 gcd 并转到 primitive pairs；(13) 给
固定整数 `h` 的表示数上界；(14) 控制 `|F(a',b')|`；(15) 把 `omega(g)` 统一界在
只依赖 `w,D,r,theta` 的常数内。紧随 (15) 的段落明确得到至少 `C21 u^2` 个
**distinct integers** `F(a,b)`，`C20,C21` 只依赖固定 `F,M,k`。

最后一行字面写 `R_k(x)>=|T|` 是对象名错误，因为 `T` 仍是 pair 集；正确对象应为
上一段得到的 distinct-value 集 `V`，并写
`R_k(x)>=|V|>=C21 u^2`。固定除数 `w^2` 不改变互异性。

**失败测试。** 对六次型 `F=X^6+Y^6`，二十个对角 pair `(n,n)` 全给
`F(n,n)=2(n^3)^2`，squarefree 商都为 `t=2`。这证明仅凭 (10) 绝不能从 pairs
推出 values；但 (13)--(15) 正是所需的统一重数步骤，所以反例没有击穿完整 passage。

**分类与裁决：proof-level source explicit + object-name correction；通过。** 不能引用
错误的末行，必须引用 (13)--(15) 后的 distinct-value 段落。

### 4. thin `O(H)` 的参数空间及两次注入

**锚点。** KL p.6 Lemma 3.2 数的是固定 thin set `Omega subset Q` 内高度 `<H` 的
有理数 `alpha=phi(P)`，数量 `O(H)`。同页 Thm. 1.2 proof 先令 `T(H)` 为
**distinct squarefree integers `t`**，再为每个 `t` 选一个同盒 witness
`(a_t,b_t)`。ST/KL 参数为 `s_t=a_t/b_t=psi(alpha_t)`；固定可逆 Möbius 变换
`tau=psi^{-1}` 给 `alpha_t=tau(s_t)`，且只把高度乘一个固定常数。KL p.7 的计数式
明确减去 `2|Omega(H)|`。

需单列的初等注入是：若两个所选 witness 有相同射影比，则互为有理倍数 `lambda`；
六次齐次性给两个 `F` 值之比 `lambda^6=(lambda^3)^2`。除以同一个类内固定
`w^2` 后，两个 signed squarefree `t` 属于同一有理平方类，只能相等。因此

\[
t\hookrightarrow a_t/b_t\xrightarrow{\tau}\alpha_t.
\]

不同 signed squarefree `t` 也注入 `Q(sqrt(t))`。于是一个 thin 参数至多删除一个
已选 `t`（若沿几何点计则至多出现二覆盖的固定因子 2），不会吞掉 `H^2` 主项。

**失败测试。** 重放 `lambda=2,3/2,5/3` 验证 `lambda^6` 恒为平方，并穷举
`[-80,80]` 内 signed squarefree 代表，未找到两个不同代表之比为有理平方。若次数为
奇数，此论证会失败；当前最终次数恰为 6。

**分类与裁决：thin 空间和 bounded witness 为 source explicit；projective/square-
class 注入为 additional elementary lemma；通过。** KL Lemma 3.2 本身不能被误说成
distinct fields 定理。

### 5. `Q(P)` 的共轭点重复是否只损失常数 2

**锚点。** KL p.7 逐式得到

\[
Q(P)=Q(\sqrt{f(\phi(P))})=Q(\sqrt{F(a_t,b_t)})=Q(\sqrt t).
\]

紧接着的 “fields `Q(P)`, `P in R(x)`, are all distinct” 若把 `R(x)` 当几何点集
逐点理解并不正确：同一非分支参数通常有两个共轭点 `+sqrt(t),-sqrt(t)`，它们生成
同一个域。可是 `C -> P1` 在这里是二覆盖，每个参数纤维至多两个点；按不同 `t`
直接计域，或先按点计再除以 2，都只改变固定常数。第 4 项又排除了不同 `t` 产生同一
域。

**失败测试。** 单个二次纤维 `y^2=t` 已给最小反例：两个共轭点但只有一个二次域。
它反驳逐点单射，却同时证明最大重复数正是覆盖次数 2；没有出现随 `H` 增长的域重数。

**分类与裁决：source-explicit field identity + additional elementary degree-two
correction；通过。** 原文 p.7 的 `-2|Omega(H)|` 也与二覆盖的固定纤维界一致，但
不能把那一行误述成“trace 或原文明说逐点域注入”。

### 6. 所有固定量是否先于 `H/X`

**锚点与量词。** ST printed p.948 在高度之前、针对最终固定
`(F,A,B,M,k)` 定义类内 maximal `w`；p.949 的局部密度由其最大性为正；p.953
(13)--(15) 后的 `C20,C21` 只依赖固定 `F,M,k`，并对每个 `u>C20` 给正盒内
`C21u^2` 个不同值。因此没有只沿子序列的量词。对实数 `H`，取
`u=floor(H)>=H/2`（充分大时）即可保持全称高度并只改常数。

KL pp.7--8 在选择坏素数、平移和负实邻域后再计点；虚二次结尾明确改取固定平移使
`f<0`，同一证明适用。局部恒等式
`f(tau(a/b))=F(a,b)R(a,b)^2` 与 `w^2>0` 使所计 squarefree `t` 同号为负。
KL p.8 又给固定 `f,M,N` 的
`|Disc Q(P)| <= c' H^(2g+2)`；`g=2` 时指数为 6。也可直接用固定六次型
`|F(a,b)|<=C_F H^6` 和二次判别式至多 `4|t|`。BLT p.7 固定

\[
C_0:y^2=(5x+7)(128x^4+549x^3+1007x^2+936x+368)
\]

并给已发表的 Magma 输入
`Jac(C0)(Q)_tors = Z/5Z x Z/10Z`；该计算是来源输入，不是本轮 kernel 认证。

完整依赖顺序可写为

\[
(C_0,g,S,N_0/M_0,\phi,\Omega,\epsilon)
\to N_1\to(A,B,M,F)\to w\to(c,H_0,C_\Delta)
\to \forall H\ge H_0\to t\to X.
\]

所有决定指数和常数的数据都在 `forall H` 与最终 `X` 之前固定。

**失败测试。** 类内 `w` 不能偷换为全局值：对 `F=X^6+Y^6`，模 2 类 `(0,1)`
已有值 1，故固定平方因子 `w=1`；类 `(0,0)` 的每个值都含 `2^6`，且 `(2,4)`
恰给 2-adic 次数 6，故其 2-primary 固定平方因子为 `2^6=(2^3)^2`。两个类的 `w`
确实不同。原始 `C0` 分支六次型 `Yg(X/Y)` 的系数绝对值和为 35,856，给出显式模板
`|Disc|<=4*35856*H^6`；最终 PGL2 型的数值常数会改变但仍在变换后固定。逐个测试
半整数 `H>=2` 又验证 `floor(H)^2>=H^2/4`，所以取整不会把全称充分大高度变成
子序列。若错误地令 `w=w(H)` 或只在高度子序列取 `M`，将直接违反
p.948/p.953 的定义与量词。

**分类与裁决：source explicit combination + immediate floor/sign/discriminant
deductions；通过。** BLT torsion 等式仍是已发表计算机支持事实，不是本审阅重新认证。

## Issue list 与证伪结论

1. **已确认但已隔离的错误：** ST p.951 的前向剩余类方向错误。当前端点避让使该
   分支不可达；若未来改坐标导致端点系数为零，必须用逆像类重写。
2. **已确认且必须显式修正的错误：** ST p.953 最后一行的 `|T|` 应替换为上一段的
   distinct-value 集 `V`。
3. **已确认且必须显式修正的措辞：** KL p.7 不能声称几何点逐点给不同域；按不同
   signed squarefree `t` 计，或除以至多 2。
4. **不能擦除的附加引理：** `N1` 有限端点避让与六次齐次 projective 注入必须出现在
   正式论证中；仅引用 ST/KL 定理名不够。
5. **范围边界：** 来源接口通过不等于总定理已由内核验证，也不认证 BLT Magma 计算、
   新颖性、EXP-EPS 或任何未在本轮审阅的桥。

证伪假设为“六项中至少一项因隐藏量词、错误换元、pair/value 混淆、thin 参数碰撞、
共轭点重复或高度依赖常数而失效”。最便宜的具体反例确实击中了三处危险的裸表述
（`N1=23` 端点、模 5 前向类、`X^6+Y^6` 对角 pairs），但保留上述显式修正后没有
得到致命链。**证伪结果：survived（仅限六项来源接口）；最终状态 CANDIDATE。**

确定性命令与保存输出见
`mathematics/worker/no-log-terminal-source-corrections-independent-replay.txt`。
