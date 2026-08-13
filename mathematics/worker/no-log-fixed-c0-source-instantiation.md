# 固定 `C0` 的有理来源接口实例化候选

## 目的与认证边界

本文件把冻结人工引理 `strong-kl-no-log-lemma.md` 的集合
\(\mathcal T_H\) 映射到纯数值结构
`NoLogSourceBridge.RationalCountingBridge`。来源语义保留在本账本中，不再作为
对 Lean 证明无作用的装饰性 `Prop` 字段。新平台回执
`lean-be179a7b1c063b4bc53752a5` 只认证纯数值接口；历史回执
`lean-b450b5f91e03836f8ae94187` 已因声明对齐过宽而被取代。本文件必须与数值
定理分别接受独立冻结审阅，二者同时通过后才可作为 NO-LOG 的最后来源链接。

## 固定常数的量词顺序

冻结 strong-KL 引理给出

\[
\exists c,H_s,C_\Delta>0\quad \forall H\ge H_s,
\quad \#\mathcal T_H\ge cH^2,
\]

且每个 \(t\in\mathcal T_H\) 给出互异目标域，满足
\(|\operatorname{Disc}K_t|\le C_\Delta H^6\)。这里所有常数在高度 \(H\)
之前选定。

作以下一次性选择：

1. 由 (c>0) 与阿基米德性质，取正整数 (q) 使 (1/q\le c)，并令
   (p=1)；
2. 取自然数 `H0≥1` 且 (H_0\ge H_s)；
3. 取正自然数 `D` 且 (D\ge C_\Delta)。

于是对每个自然数 (T\ge H_0)，

\[
T^2=pT^2\le q\,cT^2\le q\#\mathcal T_T.
\]

这正是 `rationalQuadraticGoodCount`。注意 (p,q,D,H_0) 都固定在全称量词
`∀ T` 之前，绝不随 (T) 或最终判别式界 (X) 变化。

## 字段实例化

令 `N(X)=N^-_{5,2}(X)` 的自然数判别式截断版本，并定义

```text
goodCount(T) = card(T_T).
```

字段逐项如下。

| Lean 字段 | 冻结来源对象 | 论证 |
| --- | --- | --- |
| `H0,p,q,discriminantConstant` | 上节的 `H0,1,q,D` | 固定正自然数 |
| `rationalQuadraticGoodCount` | `#T_T≥cT²` 与 `1/q≤c` | 上节清分母 |
| `goodInjectsIntoFields` | `t↦Q(√t)` 的互异性与 `|Disc|≤CΔT⁶≤DT⁶` | strong-KL item 4 |
| `fieldCountMonotone` | 判别式截断集合包含关系 | `x≤y` 时 `N(x)≤N(y)` |

`goodCount(T)` 在两个数值字段中必须是同一个 post-thin-deletion 集合
\(\mathcal T_T\) 的基数。不能一个字段用 ST 删除前集合、另一个字段用 KL
删除后集合。

来源侧的正锥、固定同余类、类内 maximal `w²`、bounded witness、thin-set
排除和局部秩结论不是 Lean 结构字段；它们共同支持上述两个数值不等式，且必须
在本账本和来源审阅中保持可追踪。

## Lean 内部已经处理的步骤

`NoLogSourceBridge.no_log_of_rational_counting_bridge` 取源高度 (T=qH)，
由 `T²≤q·goodCount(T)` 消去正因子 (q)，得到主常数 (q) 的新高度下界；
判别式常数同步成为 (Dq^6)。该定理还递归构造最大适配六次高度，证明

\[
Dq^6H^6\le X< Dq^6(H+1)^6
\quad\Longrightarrow\quad
X\le64Dq^6H^6,
\]

并推出 (B X\le A N(X)^3)。这些步骤已由新平台收据认证为
`kernel_verified`。它们不再是来源审阅义务。

## 主动失败测试

以下任一项出现即应判 `changes_requested`：

- strong-KL 的 `c,H_s,CΔ` 可随 (H) 变化；
- `#T_H≥cH²` 只沿子序列成立，而不是每个充分大自然高度；
- `goodInjectsIntoFields` 使用了不同于计数下界的集合；
- 类内 maximal `w` 被替换为有限计算中的全局 `w=2`；
- 不同 `t` 在目标域计数中发生未控制碰撞；
- `D` 或 `q` 随 `T`/`X` 变化。

冻结 strong-KL 陈述逐字给出固定常数后 `∀H≥H0`、同一集合
\(\mathcal T_H\)、互异域与 (C_\Delta H^6) 高度界，因此当前人工判定为
`source-supported candidate`；独立审阅尚未写回本文件。
