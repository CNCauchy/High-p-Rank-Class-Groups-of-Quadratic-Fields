# `NoLogNormalization` 重放与边界记录

## 已形式化的初等修复

`NoLogNormalization.lean` 只依赖 Lean 4 的 `Std.Tactic`，并给出四条命名引理：

1. `scaled_quadratic_reindex`：把来源高度 `L*H` 的二次下界重写为新高度
   `H` 下、主常数乘 `L²` 的下界；
2. `scaled_sixth_height`：同一次缩放把判别式高度常数乘 `L⁶`；
3. `sixth_selector_compares`：若 `H>0` 且下一高度已超出 `X`，则
   `X ≤ 64*D*H⁶`；
4. `sixth_selector_bounds`：把 `D*H⁶≤X` 与上一条合并成桥接所需双边界。

## 规范化声明与 statementHash

哈希按每行 UTF-8 文本、无末尾换行计算。

```text
IF mainConstant * (scale * H)^2 <= count, THEN (mainConstant * scale^2) * H^2 <= count.
FOR ALL natural discriminantConstant, scale, H, discriminantConstant * (scale * H)^6 = (discriminantConstant * scale^6) * H^6.
IF H > 0 AND X < discriminantConstant * (H+1)^6, THEN X <= (64 * discriminantConstant) * H^6.
IF H > 0, discriminantConstant * H^6 <= X, AND X < discriminantConstant * (H+1)^6, THEN discriminantConstant * H^6 <= X <= (64 * discriminantConstant) * H^6.
```

冻结 checkpoint 后将分别记录四个 statementHash 与平台 receipt。

- `scaled_quadratic_reindex`: `f37fbf2632de4fd1f011131a7ad56c435022ae2e287399c8266cfe8325b16870`
- `scaled_sixth_height`: `b9e42f21dc068c5b39ff1b3d0d2d6b58df7187e0fb99a30fd7e1cfba394f7ed4`
- `sixth_selector_compares`: `0ab2e44e0be0df0349f73f21cf246c86decd7438ff72d2aefcc5f26234e259fd`
- `sixth_selector_bounds`: `1073b17aa77f7be1710fc17c17819cf93641475c7f28f2bb09b34ea96639c09a`

## 重放命令

```bash
lean -q -t 0 mathematics/formal/NoLogNormalization.lean
rg -n -i '\b(sorry|admit|axiom)\b' mathematics/formal/NoLogNormalization.lean
```

预期：Lean 退出码 `0` 且无输出；禁止 token 扫描无匹配。

## 严格边界

这些引理不证明来源中 `c>0` 的存在，也不在无 Mathlib 环境中把实数 `c`
转成一个具体整数 `L`。它们只认证：一旦选择了满足所需主常数条件的固定
`L`，二次与六次常数的传播方向正确。

同样，`sixth_selector_bounds` 接受某个同时满足当前高度适配与下一高度失配的
`H`；它没有构造最大 `H`。最大元存在性是自然数有限初段的标准初等事实，仍需
在固定 `D>0` 的最终桥接结构中显式提供或另行形式化。
