# 《Research Plan》来源一致性独立审阅

## 审阅结论

**判定：changes_requested。** 计划书的核心数值事实——Byeon 的
\(X^{1/4}\) 下界以及 Bartz–Levin–Thamminana（下称 BLT）的
\(X^{1/3}/(\log X)^2\) 下界——与所附论文一致，且从“非循环
5-class group”到“5-rank 至少 2”的转换在这里成立。不过，正式作为研究入口前应修订四点：

1. 摘要中的 “lower bound of order” 容易读成双边阶或渐近式；原文只证明
   \(\gg X^{1/3}/(\log X)^2\)。
2. Cohen–Lenstra 段落没有给出原始来源，且“large \(p\)-rank”只有解释为“每个固定秩阈值”时才是合适的正频率预测。
3. “current benchmark / present state” 是截至某日的全局文献状态主张；两次定向检索未发现更强的同题结果，但这不是系统综述，不能证明不存在后续改进。
4. \(N^-_{5,2}(X)\gg X^{1/3+\delta-o(1)}\) 混合了 Vinogradov 记号与变动指数，应改成无歧义的量词形式。

本审阅核查的是文献身份、陈述对齐和人工可复现推导。共享预检已说明 Lean
当前不可用；本轮没有 Lean receipt、声明哈希或内核重放，**不得标记为
`kernel_verified`**。

## 范围、来源与锚点规则

技术结论以工作树内三个 PDF 为主；页码均指 PDF 物理页（从 1 开始），同时在需要时给出论文内部定理号。

- `Research Plan.pdf`：3 页，SHA-256
  `af39b83d353d68de98f6db718313c5dea2c03b28cdc6be593119b111f716cb46`。
- `29_noncyclic_class57.pdf`（Byeon）：9 页，SHA-256
  `0b135b2651241d21d7b8f6bce9bf995d4f1fc4db1762bc64defb54bd014ee3cd`。
- `Counting imaginary quadratic fields with an ideal class group of 5-rank at least 2.pdf`
  （BLT）：8 页，SHA-256
  `1b63f04fa1daad0c16a76474bfdd91f7b8ffab01bfd1c55a550b2db75b82539b`。
- 定向身份检索（2026-08-13）：`paper_search` 的 Crossref/OpenAlex 记录，仅用于身份、日期和“未检出后续同题结果”的有限观察；技术定理仍以本地全文为准。

状态词含义：`supported` 表示给定来源直接支持；`overstated` 表示方向正确但强于来源；`ambiguous` 表示需限定解释或补充范围；`unsupported` 表示给定证据不足以承担该主张。

## 逐项主张核对

| # | 计划书主张 | 状态 | 证据锚点与审阅意见 |
|---|---|---|---|
| 1 | 对素数 \(p\)，\(\operatorname{rk}_p\mathrm{Cl}(K)=\dim_{\mathbf F_p}(\mathrm{Cl}(K)/p\mathrm{Cl}(K))\)。 | supported | 计划书 p.1。对有限阿贝尔群，这等于其 \(p\)-初等商的维数，也等于可嵌入的 \((\mathbf Z/p\mathbf Z)^r\) 的最大 \(r\)。BLT p.1–2 用“含 \((\mathbf Z/m\mathbf Z)^r\) 子群的最大 \(r\)”定义一般 \(m\)-rank；两种定义在本题 \(m=p=5\) 时一致。不要把商空间公式无说明推广到复合 \(m\)。 |
| 2 | \(N^-_{5,2}(X)\) 计数 \(|\Delta_K|\le X\) 且 5-rank 至少 2 的虚二次域。 | supported | 计划书 p.1；BLT p.2 定义 \(N^-(m^r;X)\) 为同一计数对象。下标记号与原文排版不同，但语义一致。 |
| 3 | “非循环 5-class group”可用于推出 5-rank 至少 2。 | supported | Byeon p.2，Theorem 1.1 明确要求类群含有 \(\mathbf Z/g\mathbf Z\times\mathbf Z/g\mathbf Z\)（\(g=5,7\)）；取 \(g=5\) 即 5-rank 至少 2。反向也由有限阿贝尔群结构定理成立。注意“整个类群非循环”本身不够，必须说“5-primary 部分非循环”。 |
| 4 | Cohen–Lenstra 预测奇素数 \(p\) 的非平凡 \(p\)-挠以及高 \(p\)-rank 以正频率出现。 | ambiguous | 对每个**固定** \(p\) 和固定秩阈值 \(r\)，这是 Cohen–Lenstra 分布的合适推论；若“large”意指随 \(|\Delta|\) 增长的秩，则原句不成立或至少未被说明。Byeon p.1 只转述“给定 \(g\) 整除类数”的正概率，并在参考文献 [3] 列出 Cohen–Lenstra；它不足以直接支撑 rank \(\ge2\) 的精确预测。计划书应引 Cohen–Lenstra 原文或可靠综述并加入“for each fixed \(r\)”限定。 |
| 5 | 这类正频率强度的定量结果在许多情形仍远超已知。 | ambiguous | BLT p.2 说明奇数 \(m\) 的更好无条件下界似乎只在 \(m=3,5,7\) 已知，并说明某些 \(p\ge5\) 结果依赖 abc；这支持“困难/有差距”的方向性描述，但“many cases”没有规定参数范围或截止日期。建议明确为“截至 2025 年 BLT 的文献综述”。 |
| 6 | Byeon 证明 \(N^-_{5,2}(X)\gg X^{1/4}\)。 | supported | Byeon p.2，Theorem 1.1：对 \(g=5\) 或 7，虚（也包括实）二次域中含 \((\mathbf Z/g\mathbf Z)^2\) 子群者至少 \(\gg x^{1/4}\)；p.5 Lemma 4.2 给虚 5-class 构造，p.7 完成定理。BLT p.2，Theorem 1.2 也按同一记号复述该结论。 |
| 7 | BLT（2025）证明 \(N^-_{5,2}(X)\gg X^{1/3}/(\log X)^2\)。 | supported | BLT p.2，Theorem 1.3；摘要 p.1 同样陈述该下界。这里是单边下界，不是渐近公式。 |
| 8 | 摘要称已有 “quantitative lower bound of order \(X^{1/3}/(\log X)^2\)”。 | overstated | BLT 只给 \(\gg\)，没有匹配上界或 \(\asymp\)。改为 “a lower bound \(\gg X^{1/3}/(\log X)^2\)” 即与来源严格一致。 |
| 9 | BLT 的证明从 genus-2 曲线的充分大有理 5-挠及定量特化得到所需二次域。 | supported | BLT p.1 摘要；p.3，Theorem 1.4 给带有有理 Weierstrass 点的 genus-\(g\) 超椭圆曲线对应 \(X^{1/(g+1)}/(\log X)^2\) 下界；p.3 说明只需 genus 2 且 \(\operatorname{rk}_5\operatorname{Jac}(C)(\mathbf Q)_{\rm tors}\ge2\)；p.7 给显式曲线 \(C_0\) 并将其与 Theorem 1.4 合用。更精确的计划书措辞应补上“有理 Weierstrass 点”和“5-rank 恰为 2”。 |
| 10 | \(1/3\) 指数和 \((\log X)^{-2}\) 的损失尚需定位。 | ambiguous | 作为研究任务成立，但高层来源已经很清楚：二者直接出现在 BLT p.3 的 Kulkarni–Levin Theorem 1.4；代入 \(g=2\) 得 \(1/(g+1)=1/3\)。因此第一优先级应是审计 Theorem 1.4 及其原论文，而不是先把损失归因于 genus-2 搜索。它们是否可在别的方法中避免，所附两篇论文没有回答。 |
| 11 | BLT 下界是该问题的 “current benchmark”，且“present state”仍有上述差距。 | ambiguous | BLT 在 2025 年当然把 Theorem 1.3 作为对 Byeon 的改进。2026-08-13 的一次精确题名检索命中 arXiv:2502.00845 和期刊 DOI，未检出同题后续改进；但仅两次定向检索且 Semantic Scholar 返回 429，不能推出全局无后续工作。改为“BLT 论文截至 2025 年给出的 benchmark”，或补一项带日期的系统文献审查。 |
| 12 | 改善对数因子（\(\alpha<2\) 或去掉对数）是严格改进。 | supported | 在相同隐常数/充分大 \(X\) 语境下，\(X^{1/3}/(\log X)^\alpha\)（\(\alpha<2\)）确实强于现有下界。这是研究目标而非已有结论。 |
| 13 | 目标 \(N^-_{5,2}(X)\gg X^{1/3+\delta-o(1)}\)，其中显式 \(\delta>0\)。 | ambiguous | “\(\gg\)”与“\(-o(1)\)”并列没有明确量词。建议写成 \(N^-_{5,2}(X)\ge X^{1/3+\delta-o(1)}\)，或写成“存在显式 \(\delta>0\)，使对每个 \(\varepsilon>0\)，\(N^-_{5,2}(X)\gg_{\varepsilon}X^{1/3+\delta-\varepsilon}\)”。这是目标，不是来源支持的现状。 |
| 14 | 把 \((p,r)=(5,2)\) 扩展到更高 5-rank、\(p=7\) 和一般奇素数是自然方向。 | supported | 这是合理的研究规划，不是事实性定理；Byeon p.2 同时覆盖 5、7，BLT p.2 讨论一般 \(m\) 与已知的 3、5、7 情形，足以说明这些方向与现有文献相邻。不能由此推断同一方法能给出更强结果。 |

没有一项核心定理被所附原文直接反驳；`overstated` 仅出现在把单边下界称为
“of order”的表述。主要缺口是引文范围与“截至目前”的时间边界，而不是
\(X^{1/4}\) 或 \(X^{1/3}/(\log X)^2\) 数值本身。

## 两篇论文身份、年份与计划书用法

### Byeon

- **身份**：Dongho Byeon, *Quadratic fields with noncyclic 5- or 7-class groups*。
- **期刊身份**：*The Ramanujan Journal* **19** (2009), no. 1, 71–77；计划书参考文献与 BLT p.7 的参考文献 [4] 一致。
- **DOI/日期细节**：定向 Crossref 检索返回 DOI
  `10.1007/s11139-008-9129-x`，元数据日期为 2008-07-19。2008 是 online/DOI
  元数据年份，2009 是卷期年份；两者不是论文身份冲突。所附 PDF 的创建日期为
  2008-04-08，且缺失 Title/Author PDF 元数据，所以不能单凭文件元数据定卷期年。
- **主结论锚点**：PDF p.2，Theorem 1.1；\(g=5,7\)，实、虚二次域均给
  \(\gg x^{1/4}\)。
- **计划书用法**：正确；对本题取虚二次域、\(g=5\)。

### Bartz–Levin–Thamminana

- **身份**：Kollin Bartz, Aaron Levin, Aman Dhruva Thamminana,
  *Counting imaginary quadratic fields with an ideal class group of 5-rank at least 2*。
- **期刊身份**：*The Ramanujan Journal* **68** (2025), Article 26；DOI
  `10.1007/s11139-025-01184-6`。计划书参考文献准确。
- **版本日期**：期刊 PDF p.1 记载 received 2025-01-31、accepted 2025-07-18、online
  2025-08-01；PDF 元数据 Title/Author/Subject/DOI 与正文一致。定向检索还命中
  arXiv:2502.00845（2025-02-02），属于同一工作的预印本身份，不是另一篇结果。
- **主结论锚点**：PDF p.2，Theorem 1.3；核心输入为 p.3，Theorem 1.4；显式
  genus-2 例子及最终应用在 p.7。
- **计划书用法**：核心下界和几何路线正确；应避免将 \(\gg\) 写成“of order”，并把“current”加上检索截止日期。

## 会改变研究方向的关键问题（gap report）

1. **Kulkarni–Levin 定量定理中的真正瓶颈是什么？** BLT p.3 已表明
   \(1/3\) 和 \((\log X)^{-2}\) 都由 Theorem 1.4 的
   \(X^{1/(g+1)}/(\log X)^2\) 继承。应先读取 Kulkarni–Levin 原论文，逐项分解高度—判别式关系、Hilbert 不可约性、重数控制和对数筛损失。若该黑箱在固定 genus 2 上封顶 \(1/3\)，继续搜索更多同型曲线不会改善指数。
2. **是否存在比 genus-2 单参数特化更有利的参数空间？** 需要明确：增加曲线族参数维数是否增加不同二次域的产出，还是被高度、判别式次数或重复值抵消。这个问题决定是优化现有黑箱，还是更换计数机制。
3. **“正频率”到底是远景还是本阶段可检验目标？** Cohen–Lenstra 对每个固定
   rank 阈值给正比例预测，但当前项目只要求幂指数小幅改善。应写清中期成功标准，避免把
   \(X^{1/3+\delta}\) 与正比例 \(\asymp X\) 混为一个未分层目标。
4. **截至 2026-08-13 是否已有后续改进？** 两次定向检索未检出，但不是穷尽证明。
   在投入证明前，应做一次可复现的 MathSciNet/zbMATH/Google Scholar 引用链审查，覆盖
   BLT、Kulkarni–Levin 及后续引用；若有新预印本，当前 benchmark 和路线选择都会改变。
5. **要改善的是对数、指数，还是条件性结果？** BLT p.2 指出对某些更一般
   \(p\)-rank 结果存在 abc 条件。计划书应预先区分“无条件改进”和“条件性改进”；否则成功标准会在研究中漂移。
6. **符号与等价关系是否固定在 \(p=5\)？** 若长程计划允许复合 \(m\)，计划书当前
   \(\dim_{\mathbf F_p}\mathrm{Cl}/p\mathrm{Cl}\) 定义与 BLT 的一般 \(m\)-rank 不能直接互换，需另立定义。

## 证伪尝试与结果

**待证伪假设**：计划书的核心文献链准确，即 Byeon 给出同一计数问题的
\(X^{1/4}\) 下界，BLT 将其无条件提升到
\(X^{1/3}/(\log X)^2\)，并通过 genus-2 Jacobian 的有理 5-挠和定量特化实现。

**最低成本决定性测试**：直接比较计划书 p.1 的对象/定义和 p.1–2 的两个下界，与
Byeon Theorem 1.1、BLT Theorems 1.3–1.4 及 BLT p.7 的最终应用；另外搜索是否出现
不同论文身份或明确更强的 2024–2026 同题记录。

**结果：survived（带措辞限定）**。定理对象和指数未发现反例或错引；论文身份一致。
假设的“核心文献链”存活。但两个更强表述没有通过：`of order` 超出单边下界，
`current benchmark` 也不能由本轮有限检索决定性证明。因此总体审阅仍为
`changes_requested`，而不是无条件 `passed`。

## 验证 transcript

执行目录均为所分配的隔离工作树：

```text
/Users/hao/Desktop/WestlakeNLP/algebraic number theory/.deepscientist/agent-worktrees/
mathematics-research-team/019ff98c-0ec5-7d11-ac56-29cfbab47432/
mathematics-research-team-worker-ver/cl-intake-independent-verifi-02261855d3
```

1. Git 边界：

   ```sh
   git rev-parse --show-toplevel
   git rev-parse HEAD
   git branch --show-current
   git status --short
   ```

   观察：工作树路径与指派完全一致；起始 HEAD 为
   `aec794ba22ff941faed7346bcdda8d98110dabd4`；分支为
   `deepscientist/agents/mathematics-research-team/019ff98c-0ec5-7d11-ac56-29cfbab47432/mathematics-research-team-worker-ver/cl-intake-independent-verifi-02261855d3`；开始审阅时干净。

2. PDF 元数据和内容读取：

   ```sh
   for f in *.pdf; do pdfinfo "$f"; shasum -a 256 "$f"; done
   gs -q -dBATCH -dNOPAUSE -sDEVICE=txtwrite -sOutputFile=- 'Research Plan.pdf'
   gs -q -dBATCH -dNOPAUSE -sDEVICE=txtwrite -sOutputFile=- '29_noncyclic_class57.pdf'
   gs -q -dBATCH -dNOPAUSE -sDEVICE=txtwrite -sOutputFile=- \
     'Counting imaginary quadratic fields with an ideal class group of 5-rank at least 2.pdf'
   ```

   观察：三份 PDF 分别为 3、9、8 页，均可由 Ghostscript `txtwrite` 完整提取；
   SHA-256 如“范围、来源”所列。系统没有 `pdftotext`，但这不妨碍已授权的
   Ghostscript 重放。

3. 两次定向 `paper_search`：

   ```text
   query 1: "Quadratic fields with noncyclic 5 or 7-class groups" Byeon 2009 Ramanujan
   years: 2008–2010
   observed: Crossref 命中准确题名、Dongho Byeon、DOI 10.1007/s11139-008-9129-x；
             Semantic Scholar 返回 429。

   query 2: "Counting imaginary quadratic fields with an ideal class group of 5-rank at least 2"
   years: 2024–2026
   observed: OpenAlex 命中 arXiv:2502.00845 和期刊 DOI
             10.1007/s11139-025-01184-6；结果列表未出现更强同题后续；
             Semantic Scholar 返回 429。
   ```

   限制：这是身份/状态的定向核查，不是完整引用网络或“无后续结果”的证明。

4. 产物完整性（提交前运行）：

   ```sh
   test -s mathematics/worker/source-consistency-review.md
   rg -n 'supported|overstated|ambiguous|unsupported|changes_requested|kernel_verified|gap report|survived' \
     mathematics/worker/source-consistency-review.md
   git diff --check
   git status --short
   ```

## 限制与建议修订文本

- 未获得 Lean 能力，未进行形式化声明对齐、内核编译或 kernel replay；本结论是独立来源审阅。
- 未读取 Cohen–Lenstra 与 Kulkarni–Levin 的原始全文；涉及它们的具体机制只能标为下一步，而不能在这里证明。
- 两次检索达到任务上限，且一个数据源遭遇 429；“当前最佳”仍需更系统检索。

可直接将计划书摘要中的关键句改为：

> Bartz, Levin, and Thamminana (2025) proved the unconditional lower bound
> \(N^-_{5,2}(X)\gg X^{1/3}/(\log X)^2\), improving Byeon's
> \(\gg X^{1/4}\) bound. The present project asks whether the logarithmic loss
> or the exponent can be improved; any claim that this remains the best known
> bound will be dated to a documented literature search.

并将 Cohen–Lenstra 句限定为“for each fixed odd prime \(p\) and fixed rank threshold
\(r\)”后补充原始引文。
