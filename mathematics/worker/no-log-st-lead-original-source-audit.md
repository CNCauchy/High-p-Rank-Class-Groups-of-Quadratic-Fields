# NO-LOG：Stewart--Top 强分支原文 Lead 审计

## 结论与边界

对固定的 BLT 曲线 `C0`，Stewart--Top（ST）强分支所需的五项计数接口可以从
原文证明中提取，但不能只引用 ST Theorem 1 的裸陈述。精确情况是：

- 固定同余类、类内 maximal `w^2`、不同 squarefree values 是定义/定理层事实；
- 正盒内的 bounded witness 与统一表示重数是 proof-level 事实；
- 一般型的证明可能先做 `SL_2(Z)` 换元，不能自动保留原正锥；
- 对当前 `C0`，可在 KL Lemma 3.1 选择局部坐标时有限避开两个端点落在分支集，
  使最终六次型首尾系数均非零，因此 ST 的 `SL_2` 步完全不执行；
- 原文 p.951 与 p.953 各有一处可复现记号错误，均需显式校正，不能原样引用。

本审计未取代独立敌对复核；在该复核完成前项目总状态仍为 **CANDIDATE**。

## 原始来源

| 来源 | 身份与哈希 | 关键位置 |
| --- | --- | --- |
| C. L. Stewart and J. Top, *On Ranks of Twists of Elliptic Curves and Power-Free Values of Binary Forms* | JAMS 8 (1995), 943--973；DOI `10.1090/S0894-0347-1995-1290234-5`；公开出版 PDF 3,510,691 bytes；SHA-256 `96fb376bf0d8a4d3b70338a89b630a5e26c3cb0354be90da8cf2224d2603ba97` | printed pp.948--954，尤其 p.948 定义；p.949 Lemma 2；pp.950--951 Thm. 1；pp.951--953 proof (6)--(15) |
| C. L. Stewart, *On the Number of Solutions of Polynomial Congruences and Thue Equations* | JAMS 4 (1991), 793--835；DOI `10.1090/S0894-0347-1991-1119199-X`；公开出版 PDF 3,998,757 bytes；SHA-256 `8824ab3dbe963c8d070aad1f1d593ce6217fed686665ca99d422c192f0e9eba7` | printed pp.795--797，Thm. 1 与 Cor. 1；ST 1995 p.953 的外部表示重数输入 |

PDF p.1 分别对应 printed p.943 与 p.793。所有判断由完整 PDF 逐页 `txtwrite` 和
页面图像双重核对；截断下载样本未被采用。

## 五项决定性义务

### S1. 固定 admissible congruence class

**原文明示。** ST printed p.948 在定义所有计数函数前固定任意整数 `A,B,M,k`
（`M>=1,k>=2`），并把

\[
a\equiv A\pmod M,\qquad b\equiv B\pmod M
\]

写入 `N_k,P_k,R_k`。printed p.950--951 Theorem 1 对同样固定的 `A,B,M,k`
给出 `R_k(x) >> x^(2/r)`，常数只依赖固定 `M,k,F`。

**裁决：source explicit。** 不要求同余类随盒高度改变。

### S2. 类内 maximal fixed square `w^2`

**原文明示。** ST p.948 定义 `w` 为最大正整数，使对最终固定同余类中的全部
整数对都有 `w^k | F(a,b)`。这不是全局 primitive 参数族的 `w0`。p.949 在局部
密度 `C13` 的定义后指出，`w` 的最大性保证每个局部因子非零，故 `C13>0`；
Lemma 2 计数 `F(a,b)/w^k` 为 k-free 的正盒参数。

**裁决：source explicit。** `w` 在 `forall H` 之前固定；项目中的全局有限证书
`w=2` 不可替换这个类内 `w`，也不需要知道其数值。

### S3. 正盒和对所有充分大 `H` 的二次主项

ST Theorem 1 的陈述只限制最终值 `|t|<=x`，没有陈述 witness 的符号或高度。
决定性信息在证明：printed p.951 定义的基础集合使用 `1<=a,b<=u`；p.952 的
`T` 进一步保留该正盒、固定同余类和 `F(a,b)/w^k` k-free；p.953 (10) 给
`|T| >> u^2`，隐常数只依赖固定数据。

若最终型首尾系数均非零，p.951 开头的可选 `SL_2(Z)` 换元不执行，故这里的
`T` 正是原 KL 正锥中的参数，不是换元后的另一锥。

证明对每个充分大的实数 `u` 工作；即使只按整数盒读取，令 `u=floor(H)`，对充分大
实数 `H` 有 `u>=H/2` 且 `T(u) subset T(H)`，缩小固定常数即可得到对所有充分大
`H` 的 `>>H^2`。

**裁决：proof-level explicit + immediate floor lemma。** 这不是 Theorem 1 裸陈述，
但确实存在于同一原文证明中。

### S4. 不同 squarefree values，而非 parameter pairs

printed p.953 (11) 先选择常见 gcd 并缩放到 primitive pairs；(13) 给固定值的
表示数上界；(15) 将其中的 `omega(g)` 压到只依赖固定数据的常数。紧接 (15) 的
段落明确得到至少 `C21 u^2` 个**不同整数值** `F(a,b)`。由于 `w^k` 固定，
不同 `F(a,b)` 等价于不同 `t=F(a,b)/w^k`。

**裁决：proof-level explicit。** 参数 pair 数没有被直接冒充 value 数。

### S5. 统一表示重数

ST 1995 p.953 (13) 引用 Stewart 1991 Corollary 1：对固定非零判别式的 primitive
二元型，primitive Thue representations 至多

\[
2800(1+(4\epsilon r)^{-1})r^{1+\omega(g)}.
\]

ST 取固定 `epsilon=1/12`，故出现 `5600 r^(1+omega(g))`；其 (15) 又给

\[
\omega(g)\le \omega(wD)+(r+1)/\theta,
\]

右侧只依赖固定 `F,M,k`，不依赖 `u,H` 或被表示值。因此在所需范围内重数统一有界。

Stewart 1991 Cor. 1 表述为 content 1。对一般固定 content `c`，对 primitive pair
有 `c | h`，将方程除以 `c` 后应用于 primitive part `F/c`；所有被移除的素数属于
固定有限集合，阈值与常数只改变固定倍数。ST 1995 p.952 也明确指出 content divides
the fixed discriminant `D`，其后所有异常素数均被固定集合 `wD` 吸收。

**裁决：source explicit combination + elementary fixed-content normalization。** 不存在
随 `H` 增长的表示重数。

## 当前 `C0` 为何不需要改变正锥

KL 的虚二次构造先固定 `C0`、坏素数集、平移 `phi=u+N0/M0` 和 thin set。对
KL Lemma 3.1 的证明选择任意充分大的整数 `N1`，令

\[
\psi(q)=\frac{1-N_1q}{1+N_1q},\qquad
\tau(s)=\psi^{-1}(s)=\frac{1-s}{N_1(1+s)}.
\]

然后才固定 `A=B=1` 和含全部有限局部条件的模数 `M`。变换后的 squarefree 六次
分支型首尾系数非零，当且仅当

\[
g(-N_0/M_0+1/N_1)\ne0,\qquad
g(-N_0/M_0-1/N_1)\ne0.
\]

`g` 只有有限多个根，每个等式只排除有限多个正整数 `N1`。因此可同时令 `N1`
充分大以满足 KL 的所有局部邻域，并避开这两个有限禁集。选定 `N1` 后再固定
`A,B,M`；所有数据均先于 `forall H` 固定。

PGL2 变量替换保持射影不可约因子的次数；原奇五次分支加无穷远分支的模式为
`1+1+4`，故最终六次型的最大不可约因子次数为 4，满足 ST `k=2` 的
`m<=2k+1=5`。端点避让保证最高/最低系数非零，因而 p.951 的 `SL_2` 预处理
完全跳过。

**裁决：additional elementary finite-avoidance lemma，已在此证明。** 它不是 ST
或 KL 的定理陈述，但只使用 KL Lemma 3.1 证明中“`N1` 可任意充分大”的自由度。

## 原文两处不能静默继承的记号错误

### E1. p.951 剩余类的矩阵方向

原文定义 `F_L=F o L`，却把新剩余类写成 `L(A,B)` 并声称值集合等于原类。
一般正确类应为 `L^{-1}(A,B)`。最小反例：模 5，取
`L=[[1,1],[0,1]]`、原类 `(A,B)=(0,1)`、`F(X,Y)=X`。原文给新类 `(1,1)`，
则 `F_L(a,b)=a+b=2 mod 5`，而原类 `F(a,b)=0 mod 5`，值集合不等。

这是局部代数方向错误，不否定 Theorem 1；用逆矩阵类即可修复。对当前路线更重要的
是，端点避让使该换元根本不执行，因此 E1 不进入最终证明。

### E2. p.953 最后一行的 `|T|`

`T` 在 p.952 明确定义为 pair 集合，故末行字面上的 `R_k(x)>=|T|` 不成立。
但紧前一段已经由 (11)--(15) 得到 `>=C21u^2` 个不同值。正确结尾应令 `V`
为这些 distinct values，并写 `R_k(x)>=|V|>=C21u^2`。固定除数 `w^k` 保持
distinctness。

这是可复现的对象名称错误；前一段已经证明所需 distinct-value 下界。因此修正不引入
新的数论假设，但最终人类证明必须使用 `V`，不能逐字照抄 `|T|`。

## 量词汇总

对固定 `C0`，先选择并固定

\[
(S,N_0,\phi,\Omega,N_1,A,B,M,F,w,c,H_0).
\]

其中 `N1` 先满足局部半径与有限端点避让，`M` 随后固定；`w` 是该最终类内的
maximal fixed square。然后对每个实数 `H>=H0`，ST proof-level positive-box
argument 给至少 `cH^2` 个不同负 squarefree `t`，每个有同一盒内 witness。
所有常数只依赖固定数据，不依赖 `H`。

## 当前总裁决

ST 原文接口在加入有限避让、固定 content 正规化以及 E1/E2 两处显式校正后闭合；
没有发现固定类、正盒、distinct value、representation multiplicity 或 `H`-uniformity
方面的致命反例。由于独立敌对审阅尚未交付，项目状态暂不升级，仍为 **CANDIDATE**。

