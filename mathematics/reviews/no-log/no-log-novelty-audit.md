# 固定 (C_0) 的 NO-LOG 命题：有范围的新颖性审计

## 裁决

**截至 2026-08-14：`scoped_not_found`。** 在本次冻结的 A、B 两条检索线所覆盖的原文、引用后继和数据库范围内，没有找到一项明确证明下述精确命题的既有结果：

\[
\exists c>0\ \exists X_0>1\ \forall X\ge X_0:\quad
N^-_{5,2}(X)\ge cX^{1/3}.
\]

这里的否定只针对已记录范围；它**不是**“绝对首创”或全球完备的文献不存在证明。C 线在第二轮广义同义词检索完成前连续中断，状态必须写作 `runtime-incomplete`，本审计不把它计入支持新颖性的证据。

本审计只回答“冻结的 NO-LOG 命题是否在已查范围内找到明确先例”，不重新评审项目中的证明候选，也不把证明候选的正确性当作新颖性证据。

## 1. 精确目标与等价记号

令

\[
N^-_{5,2}(X)=\#\bigl\{[K]_{\mathbf Q}: [K:\mathbf Q]=2,
K\text{ 无实嵌入},\ |\operatorname{Disc}K|\le X,
\dim_{\mathbf F_5}(\operatorname{Cl}(K)/5\operatorname{Cl}(K))\ge2\bigr\}.
\]

审计目标是项目 `NO-LOG` 命题，规范化 statementHash 为
`234b34d918c1ce566f2aac5b9ad9f78e9c8abdb89918d4d97fecac8078a806b0`。其完整量词是：存在固定的 (c>0,X_0>1)，使每个实数 (X\ge X_0) 都满足 (N^-_{5,2}(X)\ge cX^{1/3})。

BLT 写作 (N^-(5^2;X))。其中 (5^2) 是其一般记号 (N^-(m^r;X)) 的 ((m,r)=(5,2))，不是“25-rank”；对有限阿贝尔类群，“含有 ((\mathbf Z/5\mathbf Z)^2)”与上述 5-rank 至少 2 等价。因此，下列比较均在同一个计数对象上进行。

必须同时满足的五个坐标是：

1. 虚二次域；
2. 绝对判别式至多 (X)；
3. 5-rank 至少 2；
4. 无条件；
5. 下界 (X^{1/3}) 且没有负的对数幂。

只命中其中一部分的论文不构成精确先例。

## 2. 可重放的直接先例

| 文献 | 精确结果 | 与目标的关系 | 裁决 |
|---|---|---|---|
| Bartz–Levin–Thamminana（BLT），*Counting imaginary quadratic fields with an ideal class group of 5-rank at least 2*，Ramanujan J. 68 (2025), Art. 26，[DOI](https://doi.org/10.1007/s11139-025-01184-6)，[arXiv:2502.00845](https://arxiv.org/abs/2502.00845) | Theorem 1.3：(N^-(5^2;X)\gg X^{1/3}/(\log X)^2)。本地出版 PDF SHA-256 `1b63f04fa1daad0c16a76474bfdd91f7b8ffab01bfd1c55a550b2db75b82539b`。 | 对象、符号、rank 和 (1/3) 指数都相同；仍有 ((\log X)^{-2})。 | `closest_prior_art / weaker`；**不支持** NO-LOG。 |
| Byeon，*Quadratic fields with noncyclic 5- or 7-class groups*，Ramanujan J. 19 (2009), 71–77，[DOI](https://doi.org/10.1007/s11139-008-9129-x) | Theorem 1.1 的 (g=5)、虚二次专门化：(N^-_{5,2}(X)\gg X^{1/4})。本地 PDF SHA-256 `0b135b2651241d21d7b8f6bce9bf995d4f1fc4db1762bc64defb54bd014ee3cd`。 | 同一对象且无条件，但指数 (1/4<1/3)。 | `prior_weaker`；**不支持** NO-LOG。 |
| Kulkarni–Levin（KL），*Hilbert's Irreducibility Theorem and Ideal Class Groups of Quadratic Fields*，Acta Arith. 205 (2022), 371–380，[DOI](https://doi.org/10.4064/aa211224-22-9)，[arXiv:2111.15582](https://arxiv.org/abs/2111.15582) | Corollary 1.4 给 (N^-(m^2;X)\gg X^{1/m}/(\log X)^2)，故 (m=5) 时为 (X^{1/5}/(\log X)^2)；Theorem 1.3 的曲线专门化仍保留 ((\log X)^{-2})。arXiv v1 PDF SHA-256 `26a9e645b55d70a253be2017cc8d656be188ed9c02350c21884286c60b015aae`。 | 是 BLT 的定量输入，不陈述 (m=5,r=2) 的 (X^{1/3}) NO-LOG。 | `method_prior_art / weaker`；**不支持**精确目标。 |
| Chattopadhyay–Saikia，*On the p-ranks of the ideal class groups of imaginary quadratic fields*，Ramanujan J. 62 (2023), 571–581，[arXiv:2112.00472](https://arxiv.org/abs/2112.00472) | Theorem 1 以 abc 猜想为条件，给 (N^2_p(X)\gg X^{1/(p-1)-\varepsilon})；(p=5) 为 (X^{1/4-\varepsilon})。已保留 arXiv PDF SHA-256 `a2680cfc0faedef55955a37da4e76d9866e6bfc83d1ffe0c5d85918706f368f5`。 | 同为虚二次 5-rank 至少 2，但有 abc 条件且指数更小。 | `conditional_and_weaker`；**不支持**无条件 NO-LOG。 |

这些来源形成清楚的强度链：Byeon 的 (X^{1/4}) 被 BLT 的 (X^{1/3}/(\log X)^2) 改进；KL 提供 BLT 所用的带对数定量框架；Chattopadhyay–Saikia 是条件结果。没有一项可通过忽略条件或删除对数因子而改写成目标命题。

## 3. B 线的后继文献裁决

B 线在 OpenAlex、Semantic Scholar、Crossref 与 arXiv API 中检查了 BLT/KL 的引用后继、当前 arXiv 条目和命中目标关键词的相邻原文，并逐项比对对象、实/虚符号、rank、(X) 指数与对数因子。其冻结的总体观察是：**所审语料中没有无条件 (N^-_{5,2}(X)\gg X^{1/3}) 命中。**

任务指定的作者组按可保留证据作如下裁决：

| 作者/文献簇 | B 线裁决 | 是否计入“已有精确先例” | 证据边界 |
|---|---|---|---|
| Ouyang–Song–Zhang | `not_supporting_in_audited_scope`：B 线逐坐标检查未发现其命中上述五项精确目标。 | 否 | 当前任务收据未保留可核验的精确题名、DOI、定理号或原文摘录；不得据此进一步声称其证明了某个更具体的弱命题。 |
| Hoque–Kotyada | `not_supporting_in_audited_scope`。 | 否 | 同上；作者名命中本身不是定理证据。 |
| Kim | `not_supporting_in_audited_scope`；A 线保留的若干出版页请求还遭遇反爬页面。 | 否 | 没有保留可归责到唯一论文的 DOI/定理摘录，因此本审计不补猜书目身份。 |
| Bagshaw | `not_supporting_in_audited_scope`。 | 否 | B 线总体收据可支持“未命中目标”，但没有保留本项的逐篇原文锚点；只能作受限排除，不能作完整先例说明。 |

上述四项是**证据不足时的降级裁决**：它们没有给目标提供支持，但其逐篇书目身份也没有在现有收据中达到可发表引用标准。特别地，本审计不会虚构 DOI，也不会把“检索命中作者名”写成“已排除该作者全部工作”。在论文定稿前，这四项应以原始 B 线查询快照或重新核验的书目记录补齐；本任务按指示没有新增检索。

## 4. 数据库与查询范围

| 资源 | B 线已报告范围 | 本审计保留的 URL | 覆盖说明 |
|---|---|---|---|
| OpenAlex | BLT/KL 题名、作者、引用后继和目标术语组合；截至 2026-08-14 的索引快照 | [Works API](https://api.openalex.org/works) | 元数据/引用图覆盖；未保留逐请求 URL、结果总数或原始 JSON。 |
| Semantic Scholar | BLT/KL 引用后继与相邻论文 | [Graph API paper search](https://api.semanticscholar.org/graph/v1/paper/search) | 覆盖受 API 可达性和索引延迟影响；未保留逐请求响应。 |
| Crossref | 题名、作者、DOI 元数据与出版记录 | [Works API](https://api.crossref.org/works) | 适合身份核对，不等同于全文定理检索。 |
| arXiv | 当前 math.NT 语料中的题名/摘要关键词及相关公开全文，时间上界 2026-08-14 | [arXiv API](https://export.arxiv.org/api/query) | 不覆盖未上 arXiv 的全部期刊文献；B 线报告未见精确命中。 |
| 项目原文 | BLT 出版 PDF、Byeon PDF；A 线保留 KL 与 Chattopadhyay–Saikia arXiv 原文 | 见上表的 DOI/arXiv URL | 四项直接先例可按哈希重放。 |

检索比较使用的概念簇包括：`imaginary quadratic field`、`5-rank`、`noncyclic 5-class group`、`rank at least 2`、`N^-(5^2;X)`、`X^(1/3)`、`log`/`log-free`/`no logarithmic loss`，以及 BLT/KL 的题名、作者与引用后继。由于逐请求字符串和命中计数没有随 B 线终端收据保存，这里不伪造“精确 query replay”。

未纳入或未完整覆盖的资源包括 MathSciNet、zbMATH、Web of Science、Scopus、ProQuest 学位论文、非公开预印本、尚未被上述数据库索引的 2026 年新稿，以及不同语言/不同记号下未被 A、B 线命中的文献。C 线本来用于扩大同义词与方法先例覆盖，但其第二轮没有产出可审计表，因此必须留在限制项。

## 5. 证据余额

### 支持 `scoped_not_found`

- 四项最邻近直接先例均由原文定理和稳定标识符固定，且全部严格弱于或附加条件于目标。
- B 线覆盖四个开放元数据/预印本数据库、BLT/KL 引用后继和相邻原文；其冻结结果没有五坐标同时命中的论文。
- 目标的对象、rank、符号、判别式截断和量词已规范化，避免把“类数被 5 整除”、rank 1、实二次或 (X^{1/3}/(\log X)^2) 当作等价命题。

### 反对更强新颖性表述

- 负面检索不能证明全球不存在先例。
- C 线 `runtime-incomplete`，未形成可计入的广义同义词/方法先例第二轮。
- B 线没有保留原始响应、逐请求字符串、命中总数和若干指定作者组的精确书目锚点。
- 开放数据库有索引延迟和覆盖盲区；付费数据库、学位论文、未公开稿件及未来回溯索引均未穷尽。
- 项目中的 NO-LOG 结果仍标为人工证明候选；本审计不把它提升为已发表定理或 Lean Verified 结论。

因此证据余额只允许 `scoped_not_found`，不允许 `novel_proved`、`first`、`no_prior_art_exists` 或类似措辞。

## 6. 主动证伪结果

待证伪假设是：“已审语料中存在一篇在同一计数对象上、无条件且无对数损失地证明 (X^{1/3}) 下界的先例。”最便宜的决定性失败信号是任一原文定理同时命中第 1 节五个坐标。

观察结果：A 线四项直接先例均未命中；B 线的引用后继与当前 arXiv 审计也报告无命中。故该假设在 A、B 的已记录范围内**未获支持**。这只给出 `scoped_not_found`，并没有证伪“全球所有已发表或未索引文献中存在先例”的可能性。C 线不计分。

## 7. 论文安全措辞

可在稿件中使用：

> 据我们截至 2026 年 8 月 14 日对 OpenAlex、Semantic Scholar、Crossref、arXiv 及所列直接先例的有范围检索，尚未发现文献明确证明虚二次域 5-rank 至少 2 的无对数下界 (N^-_{5,2}(X)\gg X^{1/3})。现有最接近的无条件结果是 Bartz–Levin–Thamminana 的 (X^{1/3}/(\log X)^2) 下界。此陈述是有范围的“据我们所知”，不是完备或绝对首创主张。

不应使用：“我们首次证明”“此前无人证明”“这是绝对新的”“完整文献中不存在该结果”。提交论文前应补做带原始查询快照的更新检索，并请熟悉二次域类群计数文献的专家复核。

## 8. 可重放入口

- 精确命题与等价记号：`mathematics/worker/formalization-intake.md`、`mathematics/worker/formalization-intake.json`。
- 直接来源身份与页码：`mathematics/worker/source-consistency-review.md`、`mathematics/worker/no-log-kl-blt-lead-source-audit.md`。
- NO-LOG 当前证明状态：`mathematics/problems/no-log-candidate-complete-proof.md`。
- 机器可读审计：`mathematics/reviews/no-log/no-log-novelty-audit-sources.json`。
