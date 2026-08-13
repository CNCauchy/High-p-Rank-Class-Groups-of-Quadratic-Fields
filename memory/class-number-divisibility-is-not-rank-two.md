---
schema: deepscientist.project_memory.entry.v2
title: 不要用 25 整除类数替代 5-rank≥2
domain: mathematics
status: active
scope: 用类数或有限判别式数据筛选 5-rank 至少 2 的虚二次域时使用。
source_refs:
  - kind: file
    ref: mathematics/worker/counterexample-boundary-audit.md
  - kind: file
    ref: mathematics/worker/counterexample-finite-search-output.txt
  - kind: git
    ref: 58c4fabfa6b16757f54ec29e3890506ab6515159
tags: [counterexample, class-group, finite-search]
---

# 不要用 25 整除类数替代 5-rank≥2

`D=-479` 满足 `h(D)=25`，但 PARI/GP 给出类群不变量 `[25]`，故 5-rank 只有 1。筛选条件必须检查类群结构或 `Cl(D)[5]` 的大小，不能仅检查 `25|h(D)`。
