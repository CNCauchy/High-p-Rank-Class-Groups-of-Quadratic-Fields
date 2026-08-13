# NO-LOG 可分离代数引理：Lean 4.33 重放清单

## 结论与边界

**passed（仅三个命名小引理，本地 Lean kernel 重放）。** 冻结的证明提交在 Lean
4.33.0、`--trust=0` 下以退出码 0 编译。证明文件没有 `sorry`、`admit` 或项目自设
`axiom`，且导入闭包只有 Lean `Init` 与 `Std.Tactic`。本结果不形式化
Stewart–Top/Kulkarni–Levin 的解析定理，不认证 strong KL 引理或 NO-LOG 总命题，也没有
DeepScientist `lean_workspace` receipt；因此不得把 NO-LOG 标成 `kernel_verified`。

Mathlib 在冻结 worktree 与当前 Lean prefix 中均不可见，任务又禁止安装软件，所以按指派降级到
`import Std.Tactic`。降级后的精确范围是：

1. `C0` 因子式在每个整数输入处的展开恒等式；它忠实对应整数求值版本，但没有建立
   `Polynomial Int` 对象层的等式。
2. 用 `List Nat` 表示有限端点禁集，证明可在任意自然数界以上避开它。
3. 在显式假设六次齐次缩放律时，非零整数缩放把值乘以一个非零整数平方；没有构造
   `Qˣ/Qˣ²` 商群或证明一般有理缩放版本。

## 冻结边界

| 字段 | 值 |
| --- | --- |
| `assignmentId` | `stage-no-log-lean-algebra-v1` |
| `baseCommit` | `bab963ed21c9dcab7483bbca74f8273ab2cf4297` |
| `targetCommit`（证明文件冻结提交） | `3faae5799779fa4ec6d08342bd9b60eee5dfcb5b` |
| `proofPath` | `mathematics/formal/NoLogAlgebra.lean` |
| `proofHash` / 文件 SHA-256 | `3a4b1494f0ea9b2c727bd136d00964871213249344d7dbb192a9ee44bf3562cc` |
| `cwd` | `/Users/hao/Desktop/WestlakeNLP/algebraic number theory/.deepscientist/agent-worktrees/mathematics-research-team/019ff98c-0ec5-7d11-ac56-29cfbab47432/mathematics-research-team-worker-for/stage-no-log-lean-algebra-v1-f497fd0efa` |
| 网络策略 | 不需要网络；重放未访问网络 |
| 资源界 | 本地 CPU；单文件；命令外层 30 s 等待界；Lean `-t 0` 不设 heartbeat 限制 |

`targetCommit` 直接由 `baseCommit` 经两次只修改同一证明文件的提交得到；manifest 在其后的
单独提交中记录重放结果，从而避免把 manifest 自身写成循环 `targetCommit`。

## 工具链与依赖

```text
Lean (version 4.33.0, arm64-apple-darwin24.6.0,
      commit d8b18978322de05a8f3dba51ef03cf5461676c17, Release)
Lake version 5.0.0-src+d8b1897 (Lean version 4.33.0)
lean executable: /Users/hao/.elan/bin/lean
lean executable SHA-256:
8754858b6549a9b06f4a019e7145a5e1e19f933983734388920a10781a7537db
```

冻结树没有 `lean-toolchain`、`lakefile.lean`、`lakefile.toml` 或 `toolchain.lock`，所以没有可报告的
`toolchain.lock` hash；上面的版本、Lean commit 与可执行文件 hash 是本任务的替代锁定信息。
`lean --deps mathematics/formal/NoLogAlgebra.lean` 只列出：

```text
/Users/hao/.elan/manual-toolchains/lean-4.33.0/lib/lean/Init.olean
/Users/hao/.elan/manual-toolchains/lean-4.33.0/lib/lean/Std/Tactic.olean
```

没有 Mathlib 依赖。

## 命名定理与 statementHash

哈希规则统一为 `sha256(UTF-8(normalizedStatement))`；下面代码块中的单行内容就是输入字节，
不含代码块换行。它们是稳定的候选 statementHash，而不是 NO-LOG 的 statementHash。

### 1. `NoLogAlgebra.c0_explicit_factor_expansion`

```text
FOR ALL x IN Z, (5*x+7)*(128*x^4+549*x^3+1007*x^2+936*x+368)=640*x^5+3641*x^4+8878*x^3+11729*x^2+8392*x+2576.
```

`statementHash = d176822772cb5d42d42af8dd0a8a6da0ca9779e4ba863353f2bc9612e641e7fd`

Lean `#check` 类型文本的 SHA-256 候选为
`26eb42e9daf32a7b70d371f14cfcf892517a714098352ef0248c62190125599e`。

与人工声明关系：对 `strong-kl-no-log-lemma.md` 第 1 步所用的整数求值展开为
`equivalent`；若目标被读成 `Polynomial Int` 内的对象等式，则此版本为 `weaker`。

### 2. `NoLogAlgebra.exists_large_nat_avoiding_finite_endpoints`

```text
FOR ALL finite lists forbidden OF N AND FOR ALL bound IN N, EXISTS n IN N SUCH THAT bound<n AND n IS NOT AN ELEMENT OF forbidden.
```

`statementHash = fcc5da303045d5ac7041f83c2660657811bf2a3d793abf5d34cdf6d084016e5b`

Lean `#check` 类型文本的 SHA-256 候选为
`6817b5afd39d94ec292b489d5800cc7f16896a16f180832f712c525e71fe69dc`。

与人工声明关系：`equivalent`。列表允许重复，但成员关系只看有限禁集，量词顺序是
`∀ forbidden ∀ bound ∃ n`。

### 3. `NoLogAlgebra.degree_six_homogeneous_scaling_is_nonzero_square_multiple`

```text
FOR ALL F:Z->Z->Z SATISFYING FOR ALL d,a,b IN Z, F(d*a,d*b)=d^6*F(a,b), FOR ALL nonzero d IN Z AND ALL a,b IN Z, EXISTS nonzero q IN Z SUCH THAT F(d*a,d*b)=F(a,b)*q^2.
```

`statementHash = 881c20defb40343e6c977d371ab3d2417d8ac5799b266977509b944d5a590e6b`

Lean `#check` 类型文本的 SHA-256 候选为
`a0d8a593b345e439dd6c00ba89021d8e7d6643fd48271b632901946bc89ba92a`。

与人工声明关系：对“六次齐次整数型在非零整数缩放下只乘平方”为 `equivalent`；对完整的
有理平方类商群断言为 `weaker`。齐次性是显式前提，不由任意函数自动获得；见证为 `q=d^3`。

## 精确重放与观察

从上述 `cwd`、冻结 `targetCommit` 运行：

```sh
lean -q -t 0 mathematics/formal/NoLogAlgebra.lean
```

预期退出码为 0。实测：退出码 0，stdout 0 bytes，stderr 0 bytes；两者 SHA-256 均为
`e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`。

禁止占位符检查：

```sh
if rg -n -i '\b(sorry|admit|axiom)\b' mathematics/formal/NoLogAlgebra.lean; then
  exit 2
else
  echo 'forbidden-token-scan=PASS'
fi
```

实测 `forbidden-token-scan=PASS`。这证明源码没有这些 token，特别是没有项目自设公理。

为审计实际逻辑依赖，在证明文件后追加以下诊断而不修改冻结文件：

```lean
#print axioms NoLogAlgebra.c0_explicit_factor_expansion
#print axioms NoLogAlgebra.exists_large_nat_avoiding_finite_endpoints
#print axioms NoLogAlgebra.degree_six_homogeneous_scaling_is_nonzero_square_multiple
```

Lean 对三者均报告 `[propext, Quot.sound]`。这是 Lean/Std 自动化证明项使用的内置逻辑基础，
不是本项目声明的公理；manifest 不把它隐藏，也不声称空公理依赖。运行时未提供
`lean_workspace`，因此没有平台 certification receipt 或 theorem declaration hash receipt。
上列 `#check` 类型文本哈希只是可重算候选，不能替代这种 verifier-generated receipt。

## 最小失败测试与证伪结局

假设：三个可分离代数声明能在无 Mathlib、无占位符、无自设公理的 Lean 4.33/Std 环境中诚实重放。

最便宜的失败测试及失败信号：

- 直接 `lean -q -t 0`：任何非零退出码、open goal 或诊断即失败。观察为退出码 0、无输出。
- 扫描 `sorry/admit/axiom`：任何命中即失败。观察为无命中。
- 依赖检查：出现 Mathlib 即违反降级边界。观察只有 `Init` 与 `Std.Tactic`。
- 端点边界：禁集为空、含重复元素或包含 `bound` 时，归纳证明仍构造严格更大的 `n`；定理不声称
  一个统一 `n` 可同时服务所有 `bound`。
- 缩放边界：`d=0` 被显式排除；去掉该假设会使“非零平方见证”不再由当前证明给出。齐次缩放律也
  是前提，防止把结论错误推广到任意函数。

**falsification outcome: survived。** 没有观察到编译、占位符、依赖或边界失败信号；存活范围仅为
上述三个 statementHash。它不为任何解析计数、thin-set 渐近或 NO-LOG 总命题提供 Lean 认证。
