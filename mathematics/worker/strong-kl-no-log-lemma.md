# BLT \(C_0\) 的强 KL 引理：精确陈述、证明候选与反驳审计

## 判定

**accepted / source-supported proof candidate（非 Lean Verified）。** 对下面固定的
BLT 曲线，Stewart--Top（ST）Theorem 1 可以替换 Kulkarni--Levin（KL）Theorem
2.1：ST 原文证明而不只是其无界计数函数的定义，确实为每个最终计入的平方自由
整数提供同一正盒中的 witness；KL Lemma 3.1 的正锥坐标又可在选择时避开分支除子的
两个端点，所以无需再用可能破坏正锥的 ST 后置坐标变换。所得结论严格绑定

```text
NO-LOG statementHash = 234b34d918c1ce566f2aac5b9ad9f78e9c8abdb89918d4d97fecac8078a806b0
```

即存在 \(c>0,X_0>1\)，使每个 \(X\ge X_0\) 都满足

\[
N^-_{5,2}(X)\ge cX^{1/3}.
\]

这里按 \(\mathbf Q\)-同构类计数虚二次域，并要求
\(\dim_{\mathbf F_5}(\mathrm{Cl}(K)/5\mathrm{Cl}(K))\ge2\)。本文件不给出
Lean kernel receipt，不使用 “Lean Verified” 或 “kernel verified”。

## 冻结来源

| 简称 | 版本与 SHA-256 | 本文逐行锚点 |
| --- | --- | --- |
| BLT | 本地期刊 PDF，`1b63f04fa1daad0c16a76474bfdd91f7b8ffab01bfd1c55a550b2db75b82539b` | p.3 Theorem 1.4；p.7 的 \(C_0\)、因子分解、\(\operatorname{Jac}(C_0)(\mathbf Q)_{\rm tors}\) |
| KL | arXiv:2111.15582v1，`26a9e645b55d70a253be2017cc8d656be188ed9c02350c21884286c60b015aae` | p.4 Theorem 2.1；p.6 Lemmas 3.1--3.2；pp.6--7 proof of Theorem 1.2；p.7 Theorem 4.1；pp.7--8 proof of Theorem 1.3 |
| ST | JAMS 8 (1995), 943--973，公开 PDF `96fb376bf0d8a4d3b70338a89b630a5e26c3cb0354be90da8cf2224d2603ba97` | printed pp.948--954，特别是 p.948 的 \(w,R_k\)，pp.950--951 Theorem 1，pp.951--953 proof，p.954 Theorem 2 |

公开原文：KL <https://arxiv.org/abs/2111.15582>；ST
<https://uwaterloo.ca/pure-mathematics/sites/default/files/uploads/documents/s0894-0347-1995-1290234-5_0.pdf>。

## 可发表式强 KL 引理（固定 \(C_0\) 版）

令

\[
C_0:y^2=f_0(x),\qquad
f_0(x)=(5x+7)(128x^4+549x^3+1007x^2+936x+368).
\]

作有理坐标替换 \(u=640x,\ v=640^2y\)，得到同构的首一奇次数模型

\[
v^2=g(u)= (u+896)
(u^4+2745u^3+3222400u^2+1916928000u+482344960000).
\]

令 \(S\) 为 \(C_0\) 的坏约化素数集合，\(M_0=\prod_{p\in S}p\)。取充分大的
\(N_0\in\mathbf Z_{>0}\)，使 \((N_0,M_0)=1\) 且
\(g(u)<0\) whenever \(|u+N_0/M_0|<1\)，并令
\(\phi=u+N_0/M_0:C_0\to\mathbf P^1\)。令 \(\Omega\subset\mathbf Q\)
为 KL Theorem 4.1 对 \((C_0,\phi,m=5)\) 给出的 thin set。

**强 KL 引理。** 存在整数 \(A,B,M\)（可取 \(A=B=1\)）、一个
squarefree binary form \(F\in\mathbf Z[X,Y]\)、整数 \(w\ge1\) 以及常数
\(c,H_0,C_\Delta>0\)，使得：

1. \(F\) 的次数为 \(6\)，判别式非零，首尾系数非零，且它在
   \(\mathbf Q[X,Y]\) 上的不可约因子次数为 \(1,1,4\)；
2. \(w\) 是满足
   \[
   w^2\mid F(a,b)\quad
   (a\equiv A\pmod M, b\equiv B\pmod M)
   \]
   的最大正整数；
3. 对每个实数 \(H\ge H_0\)，集合
   \[
   \begin{split}
   \mathcal T_H=\{t\in\mathbf Z:\;&t\text{ squarefree},\ t<0,\\
   &\exists\,1\le a,b\le H:\ a\equiv A\pmod M,\ b\equiv B\pmod M,\\
   &F(a,b)=tw^2,\quad \tau(a/b)\notin\Omega\}
   \end{split}
   \]
   满足 \(\#\mathcal T_H\ge cH^2\)。这里
   \(\tau=\psi^{-1}\)，\(\psi(q)=(1-N_1q)/(1+N_1q)\)，而 \(N_1>1\)
   是下面证明中选定的固定整数；
4. 每个 \(t\in\mathcal T_H\) 给出一个互异的虚二次域
   \(K_t=\mathbf Q(\sqrt t)\)，并且
   \[
   \dim_{\mathbf F_5}\mathrm{Cl}(K_t)/5\mathrm{Cl}(K_t)\ge2,
   \qquad |\operatorname{Disc}(K_t)|\le C_\Delta H^6.
   \]

量词顺序是

\[
(C_0,S,N_0,\phi,\Omega)\quad\Longrightarrow\quad
\exists(A,B,M,F,w,c,H_0,C_\Delta,N_1)\quad
\forall H\ge H_0.
\]

所有隐常数只依赖上述固定数据，不依赖 \(H,t,a,b\)。这里 \(B\) 是 ST/KL
同余剩余数；盒高度另记为 \(H\)，避免两种用法混淆。

## 逐步证明候选

1. **固定几何输入。** BLT p.7 给出 \(C_0\) 的上述方程并报告
   \(\operatorname{Jac}(C_0)(\mathbf Q)_{\rm tors}\cong
   \mathbf Z/5\mathbf Z\times\mathbf Z/10\mathbf Z\)，故其 5-rank 为 2。
   直接代入验证
   \(g(u)=640^4f_0(u/640)\)，所以 \((x,y)\mapsto(640x,640^2y)\)
   给出所写首一模型。原因子分解及精确 PARI 计算给出 quartic 在
   \(\mathbf Q\) 上不可约且 \(\gcd(g,g')=1\)。

2. **KL 的虚二次局部数据。** KL proof of Theorem 1.3（pp.7--8）正是对首一
   奇次数 \(g\) 取 \(S,M_0,N_0,\phi\) 如上；对所有
   \(|\phi(P)|_v<1\ (v\in S\cup\{\infty\})\)，每个 \(p\in S\) 在
   \(\mathbf Q(P)\) 中分歧，实处条件给 \(g(u(P))<0\)。KL Theorem 4.1
   在 \(\phi(P)\notin\Omega\) 时给类群秩下界；虚二次域的单位秩修正为零，故下界
   等于 Jacobian torsion 的 5-rank，即 2。

3. **正锥且首尾系数非零的同一次选择。** 对 KL Lemma 3.1 取
   \(\epsilon=1\) 与 \(S\cup\{\infty\}\)。其证明允许取任意充分大的整数
   \(N_1>1\)，令
   \[
   \psi(q)=\frac{1-N_1q}{1+N_1q},\qquad
   \tau(s)=\frac{1-s}{N_1(1+s)},
   \]
   再取 \(A=B=1\) 及被各有限 \(p\in S\) 的充分高次幂整除的 \(M\)。于是
   \(a,b>0\) 且指定同余类推出所有 KL 局部邻域条件。

   额外避开有限集合
   \[
   g\!\left(-N_0/M_0+1/N_1\right)
   g\!\left(-N_0/M_0-1/N_1\right)=0.
   \]
   每个等式对正整数 \(N_1\) 只有有限多个解，因此仍可选择充分大的 \(N_1\)。
   这保证变换后的分支型在 \([1:0]\) 与 \([0:1]\) 均不消失，即首尾系数非零。
   因而后面不调用 ST printed p.951 为零首/尾系数准备的 \(SL_2(\mathbf Z)\)
   修正；KL 的正锥保持不变。这一步是 A002 所指出“可能缺失的正锥保持强局部化
   引理”的最小补全。

4. **构造 \(F\) 并保持因子次数。** 如 KL proof of Theorem 1.2（p.6），选取
   \(R\in\mathbf Q(X,Y)\)，使
   \[
   g(\tau(X/Y)-N_0/M_0)=F(X,Y)R(X,Y)^2
   \]
   且 \(F\in\mathbf Z[X,Y]\) 是 squarefree 齐次型；此等式也固定了 \(F\) 的
   实符号。这是原射影分支型
   \(Y^6g(X/Y)\) 的 \(\mathrm{PGL}_2(\mathbf Q)\) 变量替换；清分母与乘非零常数
   不改变 \(\mathbf Q\)-不可约因子次数。原分支型由无穷远线性因子、
   \(u+896\) 和不可约 quartic 组成，所以 \(F\) 的次数模式仍为 \(1+1+4\)，
   判别式非零。第 3 步给首尾系数非零。

5. **类内最大固定平方。** 按 ST printed p.948，对固定
   \((A,B)\bmod M\) 定义最大 \(w\)。这里必须使用“类内” \(w\)，不能把既有有限
   证书在全体原始参数上算出的 \(w=2\) 偷换进来。ST printed p.949 的局部密度
   论证由 \(w\) 的最大性得到正性；Lemma 2 与 Theorem 1 原生计数
   \(F(a,b)/w^2\) 的平方自由值，不要求 \(w=1\)。

6. **ST 强计数的有界 witness。** 对 \(k=2,r=6,m=4\) 应用 ST Theorem 1
   （printed pp.950--951），满足 \(m\le2k+1=5\)。其陈述中的 \(R_2(x)\)
   本身没有限制 witness 大小，所以仅引用定理陈述不足。决定性信息在证明：printed
   p.952 定义的 \(T\) 明确要求 \(1\le a,b\le u\)、固定同余及
   \(F(a,b)/w^2\) squarefree；printed p.953 的 (10)--(15) 从该 \(T\) 得到
   至少 \(C_{21}u^2\) 个不同值，并在末段用
   \(|F(a,b)|\le rH_Fu^r\) 转为 \(R_2(x)\) 的界。因此存在 \(c_1,H_1>0\)，
   每个 \(H\ge H_1\) 在目标正盒和同余类中产生至少 \(c_1H^2\) 个不同
   squarefree \(t\)，且每个都有 \(1\le a,b\le H\) 的 witness。

7. **thin set 删除的方向。** 对每个上述 \(t\) 固定一个 bounded witness，令
   \(q_t=\tau(a_t/b_t)\)。固定分式线性变换的高度不等式给
   \(H(q_t)\le C_\tau H\)。若 \(q_{t_1}=q_{t_2}\)，两组整数对表示同一正有理数；
   由于 \(F\) 的次数 6 为偶数，两值之比是一个有理平方。两个带符号平方自由整数
   处于同一 \(\mathbf Q^\times/\mathbf Q^{\times2}\) 类只可能相等，故
   \(t_1=t_2\)。所以 \(t\mapsto q_t\) 是单射，而 KL Lemma 3.2 只允许
   \(O(H)\) 个高度 \(O(H)\) 的 \(q_t\in\Omega\)。删除它们后仍有
   \(c_1H^2-O(H)\gg H^2\)。这不是“一个 thin 参数删除多个平方类”的错误方向，
   也没有引入第二参数：\((a,b)\) 只表示一个射影参数 \(a/b\)。

8. **符号、域、秩与高度。** 第 2--3 步的实处条件使对应的
   \(g(u(P))<0\)，而 KL p.7 的函数域计算给
   \(\mathbf Q(P)=\mathbf Q(\sqrt{F(a,b)})=\mathbf Q(\sqrt t)\)；故
   \(t<0\)。第 7 步已给不同 \(t\)，带符号平方自由代表的唯一性给互异二次域。
   KL Theorem 4.1 与第 2 步给 5-rank 至少 2。最后，固定六次型满足
   \(|t|=|F(a,b)|/w^2\le C_FH^6/w^2\)，平方自由 \(t\) 的基本判别式为
   \(t\) 或 \(4t\)，故 \(|\operatorname{Disc}K_t|\le C_\Delta H^6\)。

9. **推出 NO-LOG。** 取
   \(H=\lfloor(X/C_\Delta)^{1/6}\rfloor\)（对充分大 \(X\)），则第 8 步给
   \(\gg H^2\gg X^{1/3}\) 个所需虚二次域。

## 假设账本

状态只用 `proved`、`source-supported`、`unknown`、`failed`。`proved` 表示本文给出
了可复查推导或确定性代数核验；`source-supported` 表示直接调用冻结的已发表输入。

| ID | 精确假设/接口 | 状态 | 依据与作用 |
| --- | --- | --- | --- |
| A1 | NO-LOG 的规范化量词及 hash 如开头所列 | proved | 从 `formalization-intake.json` 重新 SHA-256；防止误报 EXP-EPS |
| A2 | BLT 的 \(C_0\) 及 Jacobian 5-rank 为 2 | source-supported | BLT p.7；供应类群秩输入 |
| A3 | \(C_0\cong\{v^2=g(u)\}\)，且 \(g\) 首一、奇五次、squarefree，分解次数 \(1+4\) | proved | 精确坐标代入、PARI factor/gcd；连同无穷远给分支次数 \(1+1+4\) |
| A4 | KL Theorem 4.1 产生 thin \(\Omega\) 及类群秩下界 | source-supported | KL p.7 |
| A5 | KL Theorem 1.3 proof 的坏素数分歧、虚符号、单位秩和 \(B^6\) 高度接口 | source-supported | KL pp.7--8，\(g(C_0)=2\) |
| A6 | KL Lemma 3.1 把全部固定地方邻域编码为 \(a,b>0\) 与一个固定同余类 | source-supported | KL p.6；可取 \(A=B=1\) |
| A7 | 可同时让变换后 \(F\) 首尾系数非零且不改变 KL 正锥 | proved | 在 Lemma 3.1 的充分大 \(N_1\) 中删除有限个端点命中分支点的值 |
| A8 | PGL\(_2(\mathbf Q)\) 变换保持分支型的可分性与 \(1+1+4\) 因子次数 | proved | 射影分支除子的双射；清分母只乘非零标量 |
| A9 | 任意固定同余类的 maximal \(w^2\) 被 ST 强定理原生吸收 | source-supported | ST pp.948--950；不假设 \(w=1\) 或等于全局证书的 2 |
| A10 | 每个最终计数的 \(t\) 有 \(1\le a,b\le H\) 的正盒 witness | source-supported | ST proof printed pp.952--953，不是仅由 Theorem 1 的无界定义推出 |
| A11 | 高度 \(O(H)\) 的 thin 参数只有 \(O(H)\) | source-supported | KL Lemma 3.2 p.6 |
| A12 | thin 删除至多删除 \(O(H)\) 个不同平方类 | proved | 次数 6 偶齐次性给 \(t\mapsto\tau(a/b)\) 单射 |
| A13 | 不同带符号 squarefree \(t<0\) 给不同二次域 | proved | \(\mathbf Q^\times/\mathbf Q^{\times2}\) 中的唯一 squarefree 代表；实处同时排除 \(t=1\) |
| A14 | \(|\operatorname{Disc}\mathbf Q(\sqrt t)|\ll H^6\) | proved | \(|F(a,b)|\ll H^6\) 且基本判别式至多 \(4|t|\) |
| A15 | 本解析论证已有 Lean kernel receipt | unknown | 没有 receipt；不是本引理成立的前提，且不得称 Lean Verified |

没有决定性假设被标为 `unknown` 或 `failed`；A15 仅记录验证边界。

## 独立审阅矩阵与 A002/A005 调和

| 挑战 | 失败信号 | 观察 | 判定 |
| --- | --- | --- | --- |
| (i) ST 是否只计无界表示 | 找不到逐个 \(t\) 的 \(1\le a,b\le H\) witness | p.952 的 \(T\) 在正盒中；p.953 从同一 \(T\) 得不同值并转到 \(R_k\) | proved；失败信号未出现 |
| (ii) KL 正锥与 ST 首尾修正是否冲突 | 必须在 ST 阶段施加任意 \(SL_2(\mathbf Z)\)，破坏正锥 | 先在 KL 的 \(N_1\) 选择中有限避让两个端点，故不施加该修正 | proved；失败信号未出现 |
| (iii) 类内 maximal \(w^2\) 是否原生吸收 | 强定理要求 \(w=1\)，或只吸收全局 \(w\) | ST p.948 对所选同余类定义 \(w\)，pp.949--950 直接筛 \(F/w^2\) | source-supported |
| (iv) thin set 是否发生多参数/方向错误 | 一个 bad 参数能对应很多被计 square classes，吞掉 \(H^2\) | 偶次数齐次性使固定 \(a/b\) 只有一个 square class；KL Lemma 3.2 给 \(O(H)\) | proved |
| (v) \(H^6\) 高度与互异域是否保持 | witness 无盒界，或平方自由值仍大量域碰撞 | 有盒 witness；signed squarefree radicand 唯一；判别式 \(\le4|t|\ll H^6\) | proved |

A002 的恢复线索是正确的缺口定位：若只拼接 KL Lemma 3.1 与 ST Theorem 1 的
陈述，确实没有“正锥保持的强局部化引理”。本文第 3 与第 6 步补上它：有限端点避让
让 ST 证明直接在 KL 正锥中运行。A005 的 `passed` 结论因此得到支持，但需收紧两点：
(a) bounded witness 来自 ST printed pp.952--953 的证明，不来自 \(R_k\) 的无界定义；
(b) 类内 \(w\) 只需存在，不应沿用有限局部证书中的全局数值 \(w=2\)。

## 主动证伪结果

**hypothesis.** ST Theorem 1 可在不丢失 KL 的正锥、地方条件、thin 排除和高度控制时
替换 KL Theorem 2.1，并对 BLT \(C_0\) 给出 NO-LOG。

**test.** 逐页检查 ST printed pp.948--954：若最终不同 \(t\) 没有同一盒内 witness，
或其首尾系数修正不可避免地把 KL 正锥移走，则立即 `changes_requested`；另检查
PGL\(_2\) 是否改变 \(1+1+4\) 因子次数，以及 thin 删除映射的方向。

**outcome: survived.** ST pp.952--953 提供所需 bounded witnesses；KL Lemma 3.1
中的充分大 \(N_1\) 可有限避让端点，从而不调用破坏正锥的修正。因子次数与 thin 删除
方向也保持。没有用有限搜索替代解析量词。

## 重放命令

在本隔离 worktree 根目录运行：

```bash
python3 mathematics/worker/verify-route-audit.py

gp -fq <<'GP'
g=x^5+3641*x^4+5681920*x^3+4804198400*x^2+2199912448000*x+432181084160000;
print(factor(g));
print(gcd(g,deriv(g)));
GP

python3 - <<'PY'
import hashlib, json, pathlib
d=json.loads(pathlib.Path('mathematics/worker/formalization-intake.json').read_text())
s=next(x for x in d['statements'] if x['id']=='NO-LOG')
print(hashlib.sha256(s['normalized'].encode()).hexdigest()==s['statementHash'])
PY

python3 -m json.tool mathematics/worker/strong-kl-no-log-source-matrix.json >/dev/null
git diff --check
```

## 限制与 memory candidate

- 这是对已发表解析输入的人工形式化与来源审计，不是完整定理的 proof-assistant
  formalization。
- 常数 \(M,w,c,H_0,C_\Delta\) 只按来源证明其存在；NO-LOG 是非有效
  Vinogradov 下界，不需要把它们数值化。
- 可复用方法（memory candidate）：当局部化引理把参数送入正锥、而强筛证明为零首尾
  系数准备了可能破坏正锥的线性变换时，应在局部化变换的自由整数参数中先有限避让
  分支端点。来源指针为 KL Lemma 3.1 p.6 与 ST proof printed p.951；本文件第 3 步给
  精确实施。
