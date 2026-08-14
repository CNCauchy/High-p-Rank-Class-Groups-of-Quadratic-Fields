# Recheck of manuscript Proposition 4.1

Date: 2026-08-14  
Manuscript: `log-free-5-rank.tex`  
Proposition: `prop:localized-ST` (Proposition 4.1)  
Disposition: **source-supported; Lean-checked only for the separable arithmetic interface**

## Exact scope

The proposition asserts that a squarefree binary sextic `F` with nonzero
endpoint coefficients and largest rational irreducible-factor degree at most
five has, in any fixed residue class, quadratically many distinct signed
squarefree quotients `t = F(a,b)/w^2` with positive witnesses in the box
`1 <= a,b <= H`, uniformly for every sufficiently large real `H`. Here `w^2`
is the maximal square dividing every value in that residue class.

The review used the author-hosted primary sources:

- C. L. Stewart and J. Top, *On ranks of twists of elliptic curves and
  power-free values of binary forms*, JAMS 8 (1995), 943--973,
  <https://uwaterloo.ca/pure-mathematics/sites/default/files/uploads/documents/s0894-0347-1995-1290234-5_0.pdf>.
- C. L. Stewart, *On the number of solutions of polynomial congruences and
  Thue equations*, JAMS 4 (1991), 793--835,
  <https://uwaterloo.ca/pure-mathematics/sites/default/files/uploads/documents/s0894-0347-1991-1119199-x_0.pdf>.

## Obligation-by-obligation result

| Obligation | Source check | Verdict |
| --- | --- | --- |
| Fixed residue class and maximal `w^2` | Stewart--Top p.948 defines `w` for the same fixed congruence class and defines `R_k` by `F(a,b)=t w^k`. | passed |
| Applicable strong theorem | Stewart--Top Theorem 1, pp.950--951, applies for `k=2` when the largest factor degree is at most `2k+1=5` (and even separately permits `m=6`). | passed |
| Positive bounded witnesses | The proof defines `U` and then `T` using `1<=a,b<=u` and the original congruence conditions, pp.951--953. Because Proposition 4.1 assumes both endpoint coefficients nonzero, the optional preliminary `SL_2(Z)` change is unnecessary. | passed |
| Quadratically many eligible pairs | Equation (10), p.953, gives `|T| >> u^2`. | passed |
| Uniform value multiplicity | Equations (11)--(15) first fix a common divisor `d|w`, pass to primitive pairs, invoke Stewart 1991 Corollary 1, and bound `omega(g)` uniformly in the fixed data. | passed |
| Distinct values, not merely pairs | The paragraph following (15) explicitly obtains at least `C_21 u^2` distinct integers represented from the same box family. The printed last line `R_k(x) >= |T|` is a notation slip; the preceding distinct-value conclusion is the valid object. | passed with disclosed source typo |
| Distinct squarefree quotients | Every retained value is `t w^2` with the same nonzero `w`; multiplication by a fixed nonzero square is injective. | passed; Lean theorem `fixed_square_preserves_distinct_values` |
| Every sufficiently large height | The source proof is uniform for every sufficiently large integral `u`. For real `H`, take `u=floor H`; after `H>=2`, `u>=H/2`, so the constant shrinks by four. | passed; rational cleared-denominator analogue Lean-checked |

## Source-text cautions

Two previously identified source-text issues do not invalidate this localized
statement but must not be copied silently:

1. The optional `SL_2(Z)` change on p.951 writes the transformed residue class
   in the forward direction although equality of value sets uses the inverse
   action. Proposition 4.1 assumes nonzero endpoint coefficients, so this
   branch is not used.
2. The last displayed comparison on p.953 writes `R_k(x) >= |T|`, although
   `T` is the pair set. The immediately preceding paragraph has already
   extracted a separate set of at least `C_21 u^2` distinct represented
   integers; that distinct-value set is the correct object.

The manuscript proof was tightened to spell out the common-gcd step and the
fixed-square injection.

## Lean boundary

`mathematics/formal/LocalizedStewartTop.lean` uses Lean 4.33 with `Std.Tactic`
and contains no `sorry`, `admit`, or project-defined axiom. It checks:

1. `fixed_square_preserves_distinct_values`;
2. `natural_box_lower_bound_of_source`;
3. `numerator_le_twice_denominator_floor`;
4. `rational_box_lower_bound_of_integer_boxes`.

The caller-bound normalized statement hashes are:

| Lean theorem | `statementHash` |
| --- | --- |
| `fixed_square_preserves_distinct_values` | `c21a98ba4a4fe8ee639ba5d2a4d3449f642d4f9654092521353865e46ac45c1c` |
| `natural_box_lower_bound_of_source` | `f5abb5a7f854286e2ee558d05ce79578220a428cb0aad948e63c086f77aa46fe` |
| `numerator_le_twice_denominator_floor` | `a7b45ac37ec11f25dbf3020ef9028c3e7c430a25f688a68bfa1c6ce55b2d8ff1` |
| `rational_box_lower_bound_of_integer_boxes` | `d5ad82e253fc763c383984b8aa6510f392ce4a15bd9d8ddf67330aee41a88c5f` |

The fourth theorem is the denominator-cleared rational form of the
`floor H >= H/2` argument. The analytic sieve, the positivity of the local
density, and Stewart's Thue-equation bound are not formalized; they remain
external source inputs. Consequently this review does **not** label the full
Proposition 4.1 as Lean Verified. A kernel receipt for the four named bridge
theorems certifies only these separable arithmetic consequences.
