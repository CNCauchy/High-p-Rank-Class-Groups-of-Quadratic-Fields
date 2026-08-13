# NO-LOG 独立适用性审阅

## 判定

**passed（适用性审阅通过；非 Lean 内核验证）。** 独立复读 BLT、Kulkarni–Levin（KL）与 Stewart–Top（ST）的原始定理和证明后，没有发现将 BLT 的显式曲线 `C0` 接入 ST 强平方自由值定理的版本错配。相反，原始来源足以闭合此前保留的四个接口：固定局部同余、固定平方因子、thin-set 排除、判别式高度与互异域计数。由这些已发表输入可得到一个完整的人工证明骨架：

\[
N^-_{5,2}(X)\gg X^{1/3}.
\]

本判定只绑定 `NO-LOG`：

- `statementHash = 234b34d918c1ce566f2aac5b9ad9f78e9c8abdb89918d4d97fecac8078a806b0`；
- 哈希已从 `mathematics/worker/formalization-intake.json` 的规范化文本重算一致；
- 它**不支持** `EXP-EPS`（hash
  `6c6e7cf3f3128a0423dd33cc64e4bd57bbcd622caf92d96776f76158edf02d49`），因为没有产生任何正的指数增益。

“六次/无重根”只是必要输入之一，不是完整论证。通过判定还依赖下文 O2–O8 的来源接口。`lean_workspace` 在 MCP catalog 初查和一次有界重试中均为 0 个匹配；虽然共享预检报告 Lean CLI 可用，本轮没有 verifier receipt，故**不得称 `kernel_verified`**。

## 冻结输入与来源版本

本审阅从指派基线 `cacde3f788e1123f72d87813068df4563a815699` 开始，未信任既有路线结论，只复用其已提交文件作为待审对象。

| 输入 | 冻结标识/锚点 | 用途 |
| --- | --- | --- |
| BLT, *Counting imaginary quadratic fields with an ideal class group of 5-rank at least 2* | 本地 PDF SHA-256 `1b63f04fa1daad0c16a76474bfdd91f7b8ffab01bfd1c55a550b2db75b82539b`；PDF pp.2–3 Theorems 1.3–1.4，p.7 的 `C0` | 给出 `C0`、Jacobian 5-rank 2 与 KL 应用 |
| KL, *Hilbert's Irreducibility Theorem and Ideal Class Groups of Quadratic Fields* | arXiv:2111.15582v1，PDF SHA-256 `26a9e645b55d70a253be2017cc8d656be188ed9c02350c21884286c60b015aae`；Theorems 1.2/1.3，Lemma 3.1/3.2，Theorem 4.1 及 Theorem 1.3 的证明 | 局部化、thin set、秩与高度接口 |
| ST, *On Ranks of Twists of Elliptic Curves and Power-Free Values of Binary Forms* | JAMS 8 (1995), 943–973；公开 PDF SHA-256 `96fb376bf0d8a4d3b70338a89b630a5e26c3cb0354be90da8cf2224d2603ba97`；printed pp.948–954，特别是 Theorem 1 pp.950–951 及其证明 | 无对数的强平方自由值计数 |
| 既有路线脚本 | `mathematics/worker/verify-route-audit.py`，SHA-256 `f689861c7bd94243837dbebf7b28edd258c832095309e38ebc850f7ac5ba9d9e` | 待独立重放的代数检查 |

公开原始来源：

- KL: <https://arxiv.org/abs/2111.15582>
- ST: <https://uwaterloo.ca/pure-mathematics/sites/default/files/uploads/documents/s0894-0347-1995-1290234-5_0.pdf>

## 待审精确命题与证明接口

令

\[
f(x)=640x^5+3641x^4+8878x^3+11729x^2+8392x+2576
\]

且 `C0 : y²=f(x)`。其六次齐次分支型为

\[
F_0(A,B)=B^6f(A/B)
=B(5A+7B)Q_4(A,B),
\]

其中

\[
Q_4=128A^4+549A^3B+1007A^2B^2+936AB^3+368B^4.
\]

需要验证的不是“`F0` 无重根，所以 NO-LOG”，而是：KL 为坏素数、实处和 thin set 选择局部邻域后，能否用 ST 强 Theorem 1 代替 KL 使用的弱 Theorem 2，同时保持全部输出语义。

## 逐义务独立审阅矩阵

| ID | 决定性义务/主动挑战 | 状态 | 原始来源与独立核验 |
| --- | --- | --- | --- |
| O1 | **定理版本**：是否误把 ST Theorem 2 的 `/(log x)^2` 结论当作无对数结论？ | passed | ST printed pp.950–951 的 **Theorem 1** 才是强版本：若二元型次数 `r≥3`、判别式非零，最大不可约因子次数 `m≤2k+1`（或 `k=2,m=6`），则固定同余类中的不同 `k`-free 表示值为 `≫x^(2/r)`。printed p.954 的 Theorem 2 才给 `≫x^(2/r)/(log x)^2`。本路线明确用前者。 |
| O2 | **因子次数**：KL 所需的首一奇次数模型与 Möbius 局部变换会不会把 `1+1+4` 变成不可控的六次不可约因子？ | passed | BLT 显示模型的首项 640 不首一，但 KL 使用的首一奇次数模型由 rational Weierstrass point 经 Q-有理超椭圆坐标变换取得；相应六点分支除子仍是 `F0` 的 `PGL₂(Q)` 变量替换。KL Lemma 3.1 再施加一个 `PGL₂(Q)` 变换。此类自同构保持 Q 上齐次不可约因子的次数与重数，故最大次数仍为 4。KL 在实处所用的整数 `N` 可在所有充分大值中选择；再排除使 `τ(0)` 或 `τ(∞)` 命中六个分支点的有限集合，可令变换后首末系数均非零。这样无需借用 ST 证明中的额外 `SL₂(Z)` 变换，避免破坏 KL 所需的正象限解释。 |
| O3 | **六次/可分性**：`F0` 是否真为 reduced 的次数 6 型，而不是有隐藏重因子？ | passed | Python 精确展开得到 `[2576,8392,11729,8878,3641,640]`。PARI/GP 2.17.4 给 `factor(f)=(5x+7)q4`，`q4` 在 Q 上不可约，`gcd(f,f')=1`，`disc(f)=625203093250768896000≠0`。`B` 与五次齐次化不相交，因为首项系数 640 非零，故 `F0` 的二元判别式也非零；模 7 gcd 为非零常数。 |
| O4 | **局部条件/正象限**：ST 强版本能否同时施加 KL 的坏素数和实处条件？ | passed | KL Lemma 3.1 把任意有限地方邻域编码为 `a≡A (mod M), b≡B (mod M), a,b>0`。ST Theorem 1 对任意固定 `A,B,M` 陈述；更关键地，其 printed pp.952–954 在首末系数非零的坐标中，从 `1≤a,b≤u` 且满足该同余类的集合 `T` 构造不同值。O2 说明可在 KL 选坐标时先保证首末系数非零，故不需后来改变正象限。所有固定局部同余因此被保留。 |
| O5 | **固定平方因子**：允许同余类会不会令每个值都有不可去掉的平方因子，使强筛失效？ | passed | ST printed p.948 定义 `w` 为使同余类内每个 `F(a,b)` 均被 `w^k` 整除的最大整数；Theorem 1 的 `R_k` 正计数 `F(a,b)=t w^k` 的不同 `k`-free `t`。printed p.949 由 `w` 的最大性得所有局部密度为正。故固定平方障碍被定理原生吸收，无需证明 `w=1`。对平方类/二次域，除去固定 `w²` 没有影响。 |
| O6 | **thin set**：去掉 KL 的异常集是否会吞掉强定理的主项？ | passed | KL Lemma 3.2：高度 `<B` 的 thin rational parameters 只有 `O(B)`。ST Theorem 1 的证明实际给 `≫B²` 个不同平方自由 `t`，每个有一个 `1≤a,b≤B`（常数缩放后）的 witness。固定参数 `a/b` 决定唯一平方类；次数 6 为偶数，非原始倍数也只乘一个平方。因此删去 thin 参数至多删 `O(B)` 个 `t`，留下 `≫B²`。这里必须引用 ST 的证明内有界 witness；仅引用其无界表述不够。 |
| O7 | **互异域/重数**：不同 `t` 是否可能给同一二次域，或不同 witness 重数破坏计数？ | passed | ST 已按不同 squarefree integers `t` 计数，而非按 `(a,b)` 计数。两个非零平方自由整数给同一 Q-二次域当且仅当相等；至多丢弃 `t=1` 这一退化值。witness 重数已在 ST Theorem 1 的 Thue 方程估计中处理，不能再用 BLT 的 21,088/548/85 曲线数作乘数。 |
| O8 | **判别式高度**：六次型值界能否转为绝对域判别式 `≤X` 且保持 `1/3`？ | passed | 对 `a,b≤B`，`|t|≤|F(a,b)|/w²≪B⁶`；平方自由 `t` 对应 `Q(√t)` 的基本判别式绝对值至多 `4|t|`。这与 KL Theorem 1.3 的证明中 `d_K≪B^(2g+2)`（`g=2`）一致。取 `B≈X^(1/6)`，`≫B²` 即 `≫X^(1/3)`。 |
| O9 | **类群秩与虚二次符号**：强筛是否只计域，却丢掉 5-rank 2 或虚性？ | passed | KL Theorem 4.1 给 thin set 外的类群秩下界；其 Theorem 1.3 证明通过坏素数分歧和实处邻域控制 S-unit 修正与符号。虚二次时单位秩为 0，得到完整的 Jacobian torsion rank。BLT p.7 已给 `Jac(C0)(Q)_tors≅Z/5×Z/10`，故 5-rank 为 2。O4 保留 KL 的所有局部条件，所以更换计数定理不改变这些结论。 |
| O10 | **命题对齐**：上述论证是否产生 `EXP-EPS`？ | refuted | 输出恰为 `≫X^(1/3)`，只支持 NO-LOG。没有降低六次判别式高度，也没有增加独立参数维数；因此没有任何 `δ>0` 的指数收益。把本审阅用于 EXP-EPS 是 statementHash 错配。 |
| O11 | **Lean 内核边界**：代数证书是否有真实 verifier receipt？ | unavailable | `ALL_TOOLS` 对逻辑工具 `lean_workspace` 初查与 2 秒后有界重试均为 match count 0。没有调用 Lean CLI 作为替代；无 theoremDeclarationHash、proofHash 或 receipt，故本报告不是 `kernel_verified`。Python/PARI 是独立可重放计算证据。 |

## 完整人工证明骨架（只针对 NO-LOG）

1. BLT 的 `C0` 是有 Q-有理 Weierstrass 点的 genus-2 曲线，且其 Jacobian 有理挠子群的 5-rank 为 2（BLT pp.3,7）。
2. 对 `C0` 应用 KL Theorem 4.1，并完全沿用 KL Theorem 1.3 证明为坏约化素数和实处选择的局部邻域及 thin set `Ω`。这保证 thin set 外的合格专门化产生虚二次域且 5-rank 至少 2。
3. KL Lemma 3.1 给 Möbius 变换 `τ` 和一个固定正同余类 `(A,B) mod M`。选择其中的充分大辅助整数时再避开使 `τ(0),τ(∞)` 成为分支点的有限个值。相应平方类由 `F=F0∘L` 给出，其中 `L∈GL₂(Q)`；清分母后 `F∈Z[X,Y]` 仍是次数 6、无重根、首末系数非零，最大 Q-不可约因子次数为 4。
4. 以 `k=2,r=6,m=4` 应用 ST Theorem 1。由其证明内的有界构造，在 `1≤a,b≤B`、指定同余类中得到 `≫B²` 个不同平方自由整数 `t`，满足 `F(a,b)=t w²`。
5. KL Lemma 3.2 给 `Ω` 中高度 `O(B)` 的参数数目为 `O(B)`；每个参数只决定一个平方类，故剔除后仍有 `≫B²` 个不同 `t`。
6. 各 `t` 给不同二次域；局部条件给虚性与 5-rank 至少 2；并有 `|Disc Q(√t)|≪B⁶`。令 `B` 为 `X^(1/6)` 的适当常数倍，即得 `N^-_{5,2}(X)≫X^(1/3)`。

这不是“由六次/无重根自动得到”的跳步；O4–O9 是不可删除的证明义务。

## 证据平衡与主动证伪结局

### 支持线

- 原始 ST Theorem 1 明确允许固定同余类和固定 `w²`，其证明给正象限的有界 witnesses。
- KL Lemmas 3.1–3.2 恰把局部条件化为同余类，并把 thin set 限制到 `O(B)`。
- BLT/KL 的 genus、torsion/rank、符号与判别式高度接口保持不变。
- Python 与 PARI/GP 两条独立代数路径一致。

### 反驳线

主动尝试了五个最低成本失败信号：错误引用 ST 弱版本、PGL₂ 变换后出现高次不可约因子、固定平方局部障碍、thin set 与 `B²` 同阶、域重数吞掉计数。逐项由 O1/O2/O5/O6/O7 排除。未发现会反驳适用性的 witness。

**falsification outcome: survived。** 精确假设“ST 强 Theorem 1 可在保留 KL 全部局部/thin/高度条件的情况下用于 `C0`，从而证明 NO-LOG”在本轮决定性来源检查中存活。相反，“该路线支持 EXP-EPS”被 O10 明确反驳。

## 验证 transcript 与重放

完整命令和输出保存在：

`mathematics/worker/no-log-independent-replay.txt`

主要重放入口：

```sh
python3 mathematics/worker/verify-route-audit.py

gp -fq <<'GP'
f=640*x^5+3641*x^4+8878*x^3+11729*x^2+8392*x+2576;
q=128*x^4+549*x^3+1007*x^2+936*x+368;
print(version()); print(factor(f)); print(factor(q));
print(gcd(f,deriv(f))); print(poldisc(f));
GP

python3 -c 'import hashlib,json,pathlib; d=json.loads(pathlib.Path(
"mathematics/worker/formalization-intake.json").read_text()); s=next(x for x in
d["statements"] if x["id"]=="NO-LOG"); print(hashlib.sha256(
s["normalized"].encode()).hexdigest()==s["statementHash"])'
```

## 最便宜的下一决定性测试

**冻结并逐行写出一份最小“强 KL”引理，然后由另一名审阅者只核对 ST Theorem 1 证明中的有界 witness 抽取。** 该引理应明确量化：给定 KL Lemma 3.1 产生的 `τ,A,B,M`，变换后的六次型 `F`、固定 `w`、高度盒、thin set 删除量与判别式常数。成本只是一页左右的来源驱动证明，不需要新的曲线搜索或大规模计算；失败信号是无法从 ST printed pp.952–954 为每个已计 `t` 选出 `a,b≪|t|^(1/6)` 的 witness。原文当前显示该 witness 存在，因此这是独立复核而非重新探索。

Lean 若后续恢复，应只认证 `F0` 展开和一个选定有限域无重根证书，并用真实 `lean_workspace` receipt 标为局部 `kernel_verified`；这仍不能把解析计数定理整体标作内核验证。

## 限制

- 本轮未形式化 KL/ST 的解析数论定理；`passed` 是独立人工适用性判定，不是形式证明助手的全定理认证。
- ST 公开 PDF 为扫描/OCR 文本；公式以扫描页和上下文复读，哈希已记录。
- 没有计算 KL 对 `C0` 的具体坏素数集合、`M,A,B,w`；其存在性已由 KL Lemma 3.1 与 ST 对任意固定同余类的定理覆盖。NO-LOG 是非有效 `≫` 下界，故不要求显式常数。
