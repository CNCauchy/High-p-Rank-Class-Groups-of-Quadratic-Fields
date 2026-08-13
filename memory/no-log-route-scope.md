---
schema: deepscientist.project_memory.entry.v2
title: BLT 显式曲线的 Stewart–Top 路线只绑定 NO-LOG
domain: mathematics
status: active
scope: 选择或审阅 BLT 显式 genus-2 曲线相关的下一步证明路线时使用。
source_refs:
  - kind: file
    ref: mathematics/worker/construction-route-audit.md
  - kind: file
    ref: mathematics/worker/verify-route-audit.py
  - kind: git
    ref: 58c4fabfa6b16757f54ec29e3890506ab6515159
stale_when: 局部同余、thin-set 与高度/重数兼容性被正式证明或反驳。
tags: [proof-route, no-log, stewart-top]
---

# BLT 显式曲线的 Stewart–Top 路线只绑定 NO-LOG

BLT 曲线 `C0` 的次数 6 二元型分解与模 7 无重根证书支持一条高可信候选：尝试用 Stewart–Top 强平方自由值定理去掉 `(log X)^2`。它只针对 `NO-LOG`（hash `234b34d918c1ce566f2aac5b9ad9f78e9c8abdb89918d4d97fecac8078a806b0`），不支持 `EXP-EPS`。局部同余、thin-set 排除及高度/重数兼容仍是必须先解决的决定性缺口。
