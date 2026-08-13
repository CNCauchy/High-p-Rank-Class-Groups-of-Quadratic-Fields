# NO-LOG 五接口独立破坏性审阅

## 最终状态

**CANDIDATE**，绑定基提交
`6de3b6bcf1ab8d8c72f12a78e16e11f13cf93514`。

没有找到足以推翻五接口链的反例，但也不能升级为“全部由原文直接闭合”：接口 4 中，
Kulkarni–Levin 明写 thin set 在有界高度的 `α=φ(P)∈Q` 参数空间中为 `O(H)`，并明写所得二次域互异；
然而从所选 distinct squarefree `t` 到有理参数 `a_t/b_t` 的注入只在其证明中被隐式使用，
需要补写一个短的齐次性推论。接口 3 的无对数正盒结论也位于 Stewart–Top 的证明
passage，而非 Theorem 1 的字面陈述。因此本审阅既不判 `REFUTED`，也不把候选称为已证
NO-LOG，更不涉及 Lean、novelty 或 EXP-EPS。

## 原始来源身份

本审阅直接读取两篇原论文，不采用项目摘要作裁决依据。

1. C. L. Stewart and J. Top, *On Ranks of Twists of Elliptic Curves and
   Power-Free Values of Binary Forms*, JAMS **8** (1995), no. 4, 943–973，
   DOI `10.1090/S0894-0347-1995-1290234-5`。读取的 31 页 JAMS 扫描 PDF
   SHA-256 为
   `96fb376bf0d8a4d3b70338a89b630a5e26c3cb0354be90da8cf2224d2603ba97`，
   3,510,691 bytes。
2. Kaivalya R. Kulkarni and Aaron Levin, *Hilbert’s Irreducibility Theorem and
   Ideal Class Groups of Quadratic Fields*, Acta Arith. **205** (2022), no. 4,
   371–380，DOI `10.4064/aa211224-22-9`；读取的 arXiv `2111.15582` 九页作者
   PDF SHA-256 为
   `26a9e645b55d70a253be2017cc8d656be188ed9c02350c21884286c60b015aae`，
   161,972 bytes。

页码以下分别用 ST 的期刊印刷页码与 KL 作者稿页码。

## 五项接口裁决

| # | 接口 | 分类 | 裁决 |
|---|---|---|---|
| 1 | 固定同余类中数 distinct squarefree `t=F(a,b)/w²`，不是 pairs | **source explicit** | 通过 |
| 2 | `w` 是最终同余类的 maximal fixed square，且与高度无关 | **source explicit** | 通过 |
| 3 | 正盒及“每个充分大 H” | **immediate deduction**（证明 passage） | 通过，但不得称为 Theorem 1 字面陈述 |
| 4 | thin 参数空间、`t`/参数/域注入 | **additional lemma** | 未发现反例；需显式补写一行齐次性引理 |
| 5 | 是否缺少 uniform representation multiplicity | **source explicit** | 不缺；ST (13)–(15) 给出统一界 |

### 1. distinct values 而非 pairs — source explicit

ST p.948 先区分三个函数：`P_k` 数盒中的 pairs；`R_k` 数满足
`F(a,b)=t w^k` 的 **k-free integers t**。p.951 Theorem 1 给的是
`R_k(x) ≫ x^(2/r)`，不是 pair 数。p.953 在 (10)–(15) 之后又明确从 pair 集合
`T` 推出至少 `C21 u²` 个 distinct integers `F(a,b)`；除以固定 `w^k` 保持互异。

对 `k=2`，这些正是 distinct squarefree signed integers
`t=F(a,b)/w²`。因此 pair/value confusion 没有发生。

### 2. 类内 maximal `w` 与高度独立 — source explicit

ST p.948 在引入任何高度变量之前定义 `w`：它是使 `w^k` 对所有满足固定
`a≡A (mod M), b≡B (mod M)` 的整数 pair 都整除 `F(a,b)` 的最大正整数。
因此 `w=w(F,A,B,M,k)`，不依赖 `x,u,H`。p.949 的局部密度常数 `C13` 使用这个
`w`，并由其最大性推出每个局部因子非零；p.952–953 的后续常数同样只依赖
`F,M,k`。

这里的 `w` 绑定送入 ST 的最终同余类；不能用另一个同余类或全局样本计算出的平方因子
替换它。原文没有这种替换。

### 3. 正盒与全称高度 — immediate deduction

ST Theorem 1 的陈述用 `|t|≤x`，没有把 witness box 写进结论；但其证明是更精确的：

- p.952 在固定任意正实数 `u` 后，定义 pair 集合 `T`，并要求
  `1≤a,b≤u` 以及固定同余类；
- p.953 (10) 给 `|T|≫u²`，(11)–(15) 控制同值重数，随后得到至少
  `C21u²` 个 distinct values；
- 同页明确常数 `C20,C21` 只依赖 `F,M,k`，并对每个 `u>C20` 成立。

所以在首尾系数非零的坐标中，令 `u=H` 就得到正第一象限盒内、对每个充分大实数
`H` 的全称结论，不是 subsequence。若首尾系数为零，ST p.951 会先作
`SL2(Z)` 坐标替换；因此“原坐标中的某个更窄任意正锥”并非其无条件字面结论。
KL pp.4–5 Theorem 2.1 及 proof sketch 独立处理正整数和 bounded witnesses，但其一般
版本为 `/log²`。本接口只支持 ST proof 中的正盒，不外推任意预指定子锥。

### 4. thin 参数与两次注入 — additional lemma

KL p.6 Lemma 3.2 数的是 `α=φ(P)∈Q` 坐标中满足 `H(α)<x` 的 thin 参数，数量
`O(x)`。ST 侧的参数是 `q=a/b=ψ(α)`；因 `ψ` 是固定可逆线性分式变换，
`q↔α=τ(q)` 一一对应且高度相差固定乘法常数。因此也可等价地在 `q` 坐标删除
`O(x)` 个参数，但不能混称两个坐标。KL pp.6–7 的 Theorem 1.2 proof：

1. 先令 `T(x)` 为 distinct squarefree integers `t`，每个 `t` 选一个 bounded
   witness `(a_t,b_t)`；
2. ST 参数是 `q=ψ(φ(P))=a_t/b_t`，且 `H(q)≤x`；thin 参数则是
   `α=φ(P)=τ(q)`，其高度为 `O(x)`；
3. 删除 `α∈Ω` 后，公式 (3.1)–(3.2) 保留局部条件；
4. p.7 逐式得到 `Q(P)=Q(sqrt(t))`，并断言所得域互异。

需要显式补写、但无需新深定理的引理是：若 `F` 为偶次 `r` 的齐次型，两个所选 pair
给同一有理比，则两 pair 互为有理倍数，故两个 `F` 值之比是有理 `r` 次幂，因 `r`
为偶数而是平方；两个 signed squarefree 商于是相同。故 distinct `t` 到参数
`a_t/b_t` 注入。再者，distinct signed squarefree `t` 是不同的有理平方类，所以
`Q(sqrt(t))` 互异。

KL 的最终估计以 `|T'|-2|Ω(x)|` 正在使用上述注入，但原文没有把它单列为 lemma。
故此接口分类为 **additional lemma**，而非 source explicit；它目前未被反例推翻。

### 5. uniform representation multiplicity — source explicit

不能只从 `|T|≫u²` 得 distinct values；ST 明确处理了这一点。p.953：

- (13) 对固定值 `h` 的表示数给出依赖 `ω(g)` 的上界；
- (14) 给 `|F(a',b')|≤rHu^r`；
- (15) 将 `ω(g)` 由只依赖 `w,D,r,δ` 的常数控制；
- 合并 (9)、(11)、(13)、(15) 后得到 `C20,C21`，只依赖 `F,M,k`，并给
  `C21u²` 个 distinct values。

因此并不需要一条未给出的 uniform multiplicity 假设；所需界已在原证明中建立。

## 主动反证尝试

### pair/value confusion 的具体见证

取合法的六次齐次型 `F(X,Y)=X^6+Y^6`。它判别式非零，首尾系数非零，且最大不可约
因子次数不超过 4，符合 ST `k=2` 强情形。对每个正整数 `n`，

```text
F(n,n)=2 n^6 = 2 (n^3)^2.
```

因此盒中可有任意多个不同 pairs，却全部给同一个 squarefree `t=2`。这击穿任何把
pair 下界直接当 value 下界的论证。它没有击穿 ST，因为 pp.952–953 的 (13)–(15)
正是把同值表示重数控制后才宣布 distinct values。

### 参数碰撞与重复域尝试

尝试令 distinct `t,t'` 的 witness 有同一 `a/b`。偶次齐次性迫使 `t/t'` 为有理平方，
signed squarefree 唯一性又迫使 `t=t'`，所以不能构造碰撞。尝试令 distinct signed
squarefree `t,t'` 产生同一二次域也同样失败：二次域相同意味着它们代表同一有理平方
类。

### hidden quantifier / H-dependent constant 尝试

ST p.953 的 `C20,C21` 明确只依赖 `F,M,k`，而 `u` 在其后任意取；p.948 的 `w` 也在
高度变量之前固定。没有发现只沿子序列、或常数依赖 `H` 的 passage。

## 致命链与剩余义务

没有致命链，故不判 `REFUTED`。当前最小剩余义务仅是把接口 4 的齐次性注入引理在正式
论证中显式写出，并在引用接口 3 时准确说“ST Theorem 1 的 pp.952–953 proof-level
bounded-box consequence”，而不是误称为定理字面陈述。完成这两点仍只表示五接口来源链
闭合；它本身不是整个无条件 NO-LOG 的证明。

重放命令、哈希与锚点输出见
`mathematics/worker/no-log-adversarial-five-interface-replay.txt`。
