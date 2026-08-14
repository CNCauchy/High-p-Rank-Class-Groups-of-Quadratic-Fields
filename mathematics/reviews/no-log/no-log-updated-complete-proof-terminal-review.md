# Terminal adversarial review of the fixed-`C0` NO-LOG proof

## Verdict

**`changes_requested`** at frozen base
`3051a59286a9953a7f6d58057e9399a7d8d3f611`.

The Stewart--Top/Kulkarni--Levin analytic bridge survives the requested
pair/value, positive-cone, congruence-direction, thin-set, signed-square-class,
conjugacy, sign, all-height and discriminant-height attacks.  The conditional
Lean files also replay cleanly.  The terminal proof nevertheless contains one
false formula in the new BLT `C0` rank bridge: the displayed inverse
`y`-coordinate has coefficient `1024/2187`, whereas direct composition forces
`8192/2187`.  The committed replay prints the false inverse but never checks it.

This is a local, cheaply repairable defect, not a refutation of the NO-LOG
theorem: the displayed forward map satisfies the exact curve identity, and the
correct inverse is obtained by replacing `1024` with `8192`.  A terminal
`passed` verdict is impermissible while the proof and replay assert the false
inverse.

Failure code: **`REVIEW_CHANGES_REQUESTED`**.

## Frozen boundary and primary sources

- Git base and reviewed HEAD before this review: full commit
  `3051a59286a9953a7f6d58057e9399a7d8d3f611`.
- Stewart--Top (ST), *On Ranks of Twists of Elliptic Curves and Power-Free
  Values of Binary Forms*, JAMS 8 (1995), 943--973, SHA-256
  `96fb376bf0d8a4d3b70338a89b630a5e26c3cb0354be90da8cf2224d2603ba97`.
  Audited: printed pp.948--953.
- Stewart, *On the Number of Solutions of Polynomial Congruences and Thue
  Equations*, JAMS 4 (1991), 793--835, especially printed pp.795--797,
  Theorem 1 and Corollary 1.
- Kulkarni--Levin (KL), arXiv:2111.15582v1, SHA-256
  `26a9e645b55d70a253be2017cc8d656be188ed9c02350c21884286c60b015aae`.
  Audited: PDF pp.5--8, especially Lemmas 3.1--3.2, the proof of Theorem 1.2,
  Theorem 4.1 and the proof of Theorem 1.3.
- Bartz--Levin--Thamminana (BLT), Ramanujan J. 68 (2025), article 26, local
  PDF SHA-256
  `1b63f04fa1daad0c16a76474bfdd91f7b8ffab01bfd1c55a550b2db75b82539b`.
  Audited: Theorem 2.1 and proof, the sample `(2/3,-1/3,25)`, and the displayed
  `C0` model.

The ST and KL primary PDFs were reread from the author-hosted/arXiv originals;
the BLT hash was recomputed from the committed project PDF.  No novelty search
or new research direction was undertaken.

## Decisive issue: the claimed inverse is false

The complete proof at
`mathematics/problems/no-log-candidate-complete-proof.md:67-84`, the
reconstruction at
`mathematics/worker/no-log-blt-c0-rank-reconstruction.md:91-98`, and the replay
at `mathematics/worker/no-log-blt-c0-rank-replay.py:133-156` give

\[
x_0=\frac{2(1-2x)}{5x-1},\qquad
y_0=\frac{59049y}{1024(5x-1)^3},
\]

and claim the inverse

\[
x=\frac{x_0+2}{5x_0+4},\qquad
y=\frac{1024y_0}{2187(5x_0+4)^3}.
\]

The `x` formula gives

\[
5x_0+4=\frac{6}{5x-1}.
\]

Substitution of the forward `y_0` into the claimed inverse therefore returns

\[
\frac{1024}{2187(5x_0+4)^3}
\frac{59049y}{1024(5x-1)^3}=\frac18y,
\]

not `y`.  The correct inverse is

\[
\boxed{\displaystyle
y=\frac{8192y_0}{2187(5x_0+4)^3}}.
\]

The cheapest decisive check used exact rational arithmetic and produced

```text
forward_curve_identity True
claimed_inverse_y_composite_multiplier 1/8
corrected_inverse_y_composite_multiplier 1
INVERSE_FORMULA_REFUTED; corrected coefficient = 8192/2187
```

The existing script ends in `PASS` because it checks the inverse `x`-formula
at four sample values but only **prints** the inverse `y`-formula.  It neither
composes the two `y` maps nor checks the full rational map identity.

Required repair:

1. replace `1024` by `8192` in both prose files and in the script's inverse
   output;
2. add an exact assertion that the forward map takes the BLT even equation to
   `C0`;
3. add exact symbolic composition assertions for both inverse coordinates;
4. rerun the terminal review on the repaired commit.

## Audit of every `NoLogInference.AnalyticBridge` field

The old `AnalyticBridge` is not the final numerical route: direct unscaled
instantiation was correctly rejected as `B-NORM-1`, and the updated proof uses
`NoLogSourceBridge.RationalCountingBridge`.  Nonetheless, every old field can
be honestly instantiated after one fixed height scaling.  The following audit
does not treat the decorative `Prop` fields as self-authenticating; their
intended mathematical meanings are checked against the sources.

| Field | Anchor or complete construction | Result |
| --- | --- | --- |
| `A` | Take `1`, after choosing `N1`, as in KL Lemma 3.1 proof. | passed |
| `B` | Take `1`, after choosing `N1`, as in KL Lemma 3.1 proof. | passed |
| `M` | Fixed positive modulus containing sufficiently high powers of all finite bad primes, chosen after `N1`; KL Lemma 3.1. | passed |
| `w` | Final-class maximal fixed square divisor; ST printed p.948. | passed |
| `modulusPositive` | The modulus in KL is chosen as a positive common multiple; take at least `1`. | passed |
| `fixedSquarePositive` | ST defines `w` as a largest **positive** integer; `w>=1`. | passed |
| `positiveConeAndFixedCongruence` | Define it to state `1<=a,b` and `a=A`, `b=B (mod M)` imply all fixed KL local neighborhoods. KL Lemma 3.1 plus endpoint avoidance proves it. | passed |
| `positiveConeAndFixedCongruenceHolds` | Proof is KL Lemma 3.1 with `N1` chosen before `M`; the optional ST `SL2` branch is unreachable. | passed |
| `classWiseMaximalFixedSquare` | Define it by the ST p.948 maximality property for the final class, not by the earlier global computation `w=2`. | passed |
| `classWiseMaximalFixedSquareHolds` | ST pp.948--949; existence is also elementary because the class contains a nonzero value and every common square divisor divides it. | passed |
| `boundedWitnessForEachSquarefreeValue` | Define it using the same ST positive-box value set at source height `L*H`. | passed |
| `boundedWitnessForEachSquarefreeValueHolds` | ST p.952 defines the positive-box pair set; p.953 (11)--(15) produces distinct values from that same set for every sufficiently large height. | passed |
| `thinParameterInjectionAndLocalRank` | Define it to include the chosen-witness injection into `tau(a/b)`, exclusion from `Omega`, KL Theorem 4.1, sign, and rank at least two. | passed |
| `thinParameterInjectionAndLocalRankHolds` | KL Lemma 3.2/Theorem 4.1 plus the degree-six signed-squarefree lemma proved below. | passed |
| `rawCount` | Cardinality of distinct squarefree `t=F(a,b)/w^2` with a chosen witness in the final class and box `1<=a,b<=L*H`. | passed |
| `thinCount` | Cardinality of those same raw `t` whose chosen `tau(a/b)` lies in the fixed `Omega`. | passed |
| `goodCount` | Cardinality of the complementary subset of the **same** raw family. | passed |
| `H0` | A natural maximum of the ST threshold, KL thin-height threshold, `1`, and the linear/quadratic domination threshold, after fixed scaling `L`. | passed |
| `X0` | With integer discriminant constant `D`, take `D*(max H0 1)^6`. | passed |
| `mainConstant` | Take `1` after choosing fixed `L` with `c*L^2>=2`. | passed |
| `thinConstant` | Take an integer ceiling of the fixed KL thin constant after height distortion and scaling; an additive `+1` is absorbed for `H>=1`. | passed |
| `discriminantConstant` | Take a positive integer `D>=C_Delta*L^6`. | passed |
| `comparisonConstant` | Take `64*D`. | passed |
| `selectedHeight` | Use the maximal/discrete sixth-root selector `NoLogSourceBridge.sixthSelector D`. | passed |
| `mainConstantPositive` | Immediate from `mainConstant=1`. | passed |
| `comparisonConstantPositive` | `64*D>0` because `D>0`. | passed |
| `strongSquarefreeCount` | Source gives `raw(LH)>=cL^2H^2`; the fixed choice `cL^2>=2` gives `2*(1*H^2)<=rawCount(H)`. | passed |
| `thinCountBound` | `H(tau(a/b))<=2N1*L*H`; KL Lemma 3.2 gives a fixed linear bound, and injection turns parameter count into `thinCount`. | passed |
| `thinIsDominated` | Enlarge `H0` so `thinConstant<=H`; then `thinConstant*H<=H^2`. | passed |
| `deletePartition` | The raw set is the disjoint union according to whether its **chosen** parameter lies in `Omega`; hence equality, stronger than the field. | passed |
| `goodInjectsIntoFields` | Each good `t` yields `Q(sqrt(t))`, rank at least two, and discriminant `<=D*H^6`; signed-squarefree injectivity gives distinct fields. | passed subject to corrected `C0` rank isomorphism prose/replay |
| `fieldCountMonotone` | Inclusion of field sets when the discriminant cutoff increases. | passed |
| `selectorLarge` | `sixthSelector_spec` and `X0=D*(max H0 1)^6`; replayed Lean proof. | passed |
| `selectorFits` | First inequality of `sixthSelector_spec`. | passed |
| `selectorCompares` | Maximality gives `X<D(H+1)^6`; for `H>=1`, `(H+1)^6<=(2H)^6=64H^6`. | passed |

### Complete fixed-scaling lemma used in the table

Let the source proof give fixed `c>0`, `Hs`, `C_Delta>0`, and for every real
`T>=Hs` a finite raw set with at least `cT^2` distinct values, each carrying a
chosen witness in the `T`-box.  Let the fixed Möbius height constant be
`C_tau` and let KL Lemma 3.2 give `#Omega(x)<=Kx` for `x>=x0`.

Choose once and for all a natural `L>=1` with `cL^2>=2`.  At bridge height
`H`, define all three counts from the source family at the single height
`T=LH`.  For `a,b<=LH`, direct evaluation of
`tau(a/b)=(b-a)/(N1(a+b))` gives
`H(tau(a/b))<=2N1LH`; taking `x=2N1LH+1` handles the strict inequality in
KL Lemma 3.2.  Choose a natural `thinConstant` above
`K(2N1L+1)`, and enlarge the natural `H0` so all source/thin thresholds hold
and `thinConstant<=H0`.  Then

\[
2H^2\le\#\mathrm{Raw}_{LH},\qquad
\#\mathrm{Thin}_{LH}\le \mathrm{thinConstant}\,H\le H^2,
\]

and the complement has at least `H^2` elements.  Choose a positive natural
`D>=C_Delta L^6`.  The same good family injects into the desired fields below
`DH^6`.  Finally use the maximal sixth-root selector with
`X0=D(max(H0,1))^6` and comparison constant `64D`.  These choices precede
every `H` and `X`.  This supplies all numeric fields without the impossible
unscaled natural coefficient identified in `B-NORM-1`.

## Ten requested source/proof obligations

| # | Obligation and adversarial test | Evidence | Verdict |
| --- | --- | --- | --- |
| 1 | Fixed congruence class and class-wise maximal `w`; attack: let either vary with `H`. | KL Lemma 3.1 fixes `A=B=1,M` after `N1`; ST p.948 fixes the maximal class-wise `w` before height. | passed |
| 2 | Positive box and endpoint avoidance; attack: force ST's cone-changing `SL2` branch. | KL p.6 permits any sufficiently large `N1`; avoiding the finitely many branch hits makes both endpoint coefficients nonzero. The original positive cone is retained. | passed |
| 3 | Distinct squarefree values, not representations; attack: `X^6+Y^6` has many diagonal pairs but one squarefree class. | ST p.953 (11)--(15) and the paragraph after (15), not the erroneous final `R_k>=|T|`, give `>>H^2` distinct values. | passed |
| 4 | Bounded witness for every sufficiently large `H`; attack: theorem statement gives only a value bound or a subsequence. | ST p.952's `T` lies in `1<=a,b<=u`; the distinct values come from the same `T`; `floor(H)>=H/2` transfers to all large real `H`. | passed |
| 5 | Thin deletion on the same surviving family; attack: count before deletion but inject a different family afterward. | One witness is selected for each raw `t`; thin and good counts partition that same selected family. | passed |
| 6 | Even-degree projective injection; attack: two values on one ray. | If ratios agree, homogeneity gives `t2/t1=lambda^6=(lambda^3)^2`; signed squarefree uniqueness forces `t1=t2`. | passed |
| 7 | Distinct signed squarefree `t` give distinct imaginary fields, including conjugate factor; attack: two points over one parameter. | Equality of quadratic fields forces the same rational square class, hence the same signed squarefree `t`. The two conjugate points give one field, but the proof counts `t`, not points. | passed |
| 8 | Sign; attack: square removal or deletion changes sign. | KL's fixed real neighborhood has `g(u)<0`; `g=F R^2` and `w^2>0` give `t<0`. Deletion only removes values. | passed |
| 9 | Discriminant `O(H^6)`; attack: hidden witness or constant dependence. | Fixed sextic gives `|F(a,b)|<=C_FH^6`; `|Disc Q(sqrt(t))|<=4|t|`; all data precede `H`. | passed |
| 10 | BLT `C0` rank via explicit rational isomorphism; attack: compose both displayed maps. | BLT Theorem 2.1 supplies the theorem-level 5-rank input and the forward curve identity is exact, but the committed inverse returns `y/8`. | **changes requested** |

The proof draft's additional uniform-representation obligation is also sound:
ST p.953 (13),(15) invokes Stewart 1991 Corollary 1; passing to the primitive
part of a fixed-content form divides both the form and represented value by a
fixed integer and changes only fixed constants.

## Source-correction attack results

All previously identified source-text hazards were actively replayed:

- a genuinely forbidden large endpoint choice (`N1=23`) exists, but the set is
  finite and avoidable;
- ST p.951's printed forward residue-class action is wrong (the mod-5 test gives
  residue `2` instead of `0`), while the inverse action is correct; endpoint
  avoidance makes this branch unused;
- twenty diagonal pairs for `X^6+Y^6` all give squarefree part `2`, so pair
  counting alone is invalid; ST (11)--(15) is essential;
- no collision among distinct signed squarefree representatives was found in
  the bounded sanity check, consistent with the complete valuation proof;
- two conjugate points were explicitly counted as one field;
- class-wise fixed squares differ between residue classes, confirming that the
  earlier global `w=2` must not be substituted;
- the real-to-integer box floor inequality and the fixed sextic coefficient
  bound replayed successfully.

These tests support the analytic bridge but do not repair the false BLT inverse.

## Conditional verification boundary

The following frozen numerical files are unchanged from their receipt commits
and replay with Lean 4.33.0:

- `NoLogInference.lean`, SHA-256
  `f4d7c0ecdac058a7b351eecea2ddb1513707d9584be954fbf6c20af974d6d564`;
- `NoLogSourceBridge.lean`, SHA-256
  `a2f7350f7b474c6675db8b4c63eaeb5633e53f0ee2e327bf1a4b45b8b11f19e8`.

Both compile with no `sorry`, `admit`, or `axiom`.  This verifies only the
conditional numerical implications.  ST, KL, BLT, the `C0` construction and
the unconditional analytic bridge are not Lean-formalized, and this review
does not claim full Lean verification.

## Evidence balance and final decision

Supporting evidence is strong for obligations 1--9: exact primary-source
anchors, complete elementary bridge lemmas, deterministic adversarial checks,
and clean replay of the conditional numerical theorem all agree.  No decisive
counterexample was found against the analytic counting chain.

Refuting evidence is decisive for one literal assertion in obligation 10: the
claimed inverse `y` map composes to multiplication by `1/8`.  Because the
forward identity passes and the coefficient correction is explicit, the
underlying `C_even`--`C0` identification remains salvageable; the appropriate
terminal status is therefore **`changes_requested`**, not `refuted` or
`inconclusive`.

The next reproducible action is exactly the four-part repair listed under the
decisive issue, followed by the same replay and a new frozen terminal review.
