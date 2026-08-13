# 数学研究执行环境

核验日期：2026-08-13（Asia/Shanghai）。

## 已安装并验证

| 组件 | 版本/状态 | 验证边界 |
| --- | --- | --- |
| Elan | 4.2.3 | 默认工具链 `lean-4.33.0-local` |
| Lean | 4.33.0, arm64 macOS, commit `d8b1897...` | 独立定理 `1+1=2` 编译通过；DeepScientist `lean_workspace` 报告 `available=true`, `batchCertification=true` |
| Lake | 5.0.0 | `lake --version` 通过 |
| VS Code Lean 4 | `leanprover.lean4@0.0.239` | VS Code CLI 可列出插件 |
| PARI/GP | 2.17.4 | `bnfinit` 独立复算 `D=-11199` 为 `[20,5]`、`D=-479` 为 `[25]` |

Lean 官方 macOS arm64 发布包大小为 `556168134` 字节，本地与官方发布元数据的 SHA-256 同为 `db5274b669be270af048b5e4f1e0ce571df6750e411956b3e1e6fcc2012410c2`。

## 能力边界

当前 DeepScientist 可以执行批量 Lean 编译与认证，但运行时不提供 live goals 或持久 Lean session。尚未为本项目创建 Mathlib 锁定项目，因为当前阶段没有任何可诚实绑定为所选开放数论命题证明的 Lean 声明；进入正式引理阶段时，应在项目内固定 `lean-toolchain`、`lakefile.toml` 与 Mathlib revision。

Magma 是商业软件，当前没有许可证或安装需求；SageMath 也不是当前最小复现路径。现阶段的类群独立复验由 PARI/GP 完成，代数恒等式与有限搜索由标准库 Python 完成。
