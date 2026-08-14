# NO-LOG candidate: complete proof draft and source ledger

## Status

**CANDIDATE.** This document assembles the complete human-readable argument for

\[
N^-_{5,2}(X)\gg X^{1/3},
\]

but it is not yet a `PROVED` project result. The two former local gates are now
closed: the endpoint/source-text corrections passed independent review, and the BLT
Theorem 2.1 sample has been explicitly identified with `C0`. One final gate remains:
an independent adversarial review of this updated complete proof.

The conditional Lean theorem certifies only the final numerical inference once the
analytic/arithmetic bridge below is supplied. It is not a kernel verification of this
unconditional theorem.

## Frozen sources

| Source | Frozen identity | Locations used |
| --- | --- | --- |
| Bartz--Levin--Thamminana (BLT), *Counting imaginary quadratic fields with an ideal class group of 5-rank at least 2* | Ramanujan J. 68 (2025), article 26; DOI `10.1007/s11139-025-01184-6`; local PDF SHA-256 `1b63f04fa1daad0c16a76474bfdd91f7b8ffab01bfd1c55a550b2db75b82539b` | PDF p.3 Thm. 1.4; pp.3--6 Thm. 2.1 and proof; p.7 the displayed curve `C0` |
| Kulkarni--Levin (KL), *Hilbert's Irreducibility Theorem and Ideal Class Groups of Quadratic Fields* | arXiv:2111.15582v1, SHA-256 `26a9e645b55d70a253be2017cc8d656be188ed9c02350c21884286c60b015aae`; Acta Arith. 205 (2022), 371--380; DOI `10.4064/aa211224-22-9` | PDF p.4 Thm. 2.1; p.6 Lemmas 3.1--3.2 and proof of Thm. 1.2; p.7 equations (3.1)--(3.2), counting inequality and Thm. 4.1; pp.7--8 proof of Thm. 1.3 |
| Stewart--Top (ST), *On Ranks of Twists of Elliptic Curves and Power-Free Values of Binary Forms* | JAMS 8 (1995), 943--973; DOI `10.1090/S0894-0347-1995-1290234-5`; SHA-256 `96fb376bf0d8a4d3b70338a89b630a5e26c3cb0354be90da8cf2224d2603ba97` | printed p.948 definitions; p.949 Lemma 2; pp.950--951 Thm. 1; pp.951--953 proof, especially (10)--(15) |
| Stewart, *On the Number of Solutions of Polynomial Congruences and Thue Equations* | JAMS 4 (1991), 793--835; DOI `10.1090/S0894-0347-1991-1119199-X`; SHA-256 `8824ab3dbe963c8d070aad1f1d593ce6217fed686665ca99d422c192f0e9eba7` | printed pp.795--797, Thm. 1 and Cor. 1 |

Page numbers below are physical PDF pages for BLT/KL and printed journal pages for ST.

## The fixed curve and normalized branch form

BLT p.7 displays

\[
C_0:y^2=f_0(x)=(5x+7)
(128x^4+549x^3+1007x^2+936x+368).
\]

The odd degree gives a rational Weierstrass point at infinity. With
\(u=640x\) and \(v=640^2y\), this is isomorphic over \(\mathbf Q\) to

\[
v^2=g(u)=640^4f_0(u/640),
\]

where

\[
g(u)=(u+896)
(u^4+2745u^3+3222400u^2+1916928000u+482344960000).
\]

Exact polynomial expansion, squarefreeness and the rational factor pattern have been
replayed independently: the quartic is irreducible over \(\mathbf Q\), and the
projective degree-six branch form has irreducible-factor degrees \(1,1,4\). Thus the
largest factor degree is four.

BLT Theorem 2.1 constructs the relevant curve as a genus-two curve whose Jacobian is
\((2,2)\)-isogenous to two elliptic curves with rational 5-torsion. Since the isogeny
degree is four, it is prime to five; hence the required conclusion is only

\[
\operatorname{rk}_5\operatorname{Jac}(C_0)(\mathbf Q)_{\rm tors}\ge2.
\]

For the sample \((t,u,z)=(2/3,-1/3,25)\), exact substitution in BLT's coefficient
formulas gives the even model `C_even` and the explicit \(\mathbf Q\)-isomorphism

\[
x_0=\frac{2(1-2x)}{5x-1},\qquad
y_0=\frac{59049y}{1024(5x-1)^3},
\]

with inverse

\[
x=\frac{x_0+2}{5x_0+4},\qquad
y=\frac{8192y_0}{2187(5x_0+4)^3}.
\]

Writing `f_0` for the displayed quintic of `C0`, the replay checks the exact
cleared-denominator identity

\[
1024^2(5x-1)^6
f_0\!\left(\frac{2(1-2x)}{5x-1}\right)=59049^2P(x)
\]

coefficient by coefficient. It also checks

\[
5x_0+4=\frac6{5x-1},\qquad
\frac{x_0+2}{5x_0+4}=x,
\qquad
\frac{8192}{2187(5x_0+4)^3}
\frac{59049}{1024(5x-1)^3}=1.
\]

Thus both coordinate formulas compose exactly; the former inverse numerator
`1024` would give the last scalar as `1/8`. The coefficient and composition
verification is recorded in
`mathematics/worker/no-log-blt-c0-rank-replay.py`. Therefore the theorem-level
5-rank conclusion for `C_even` applies to the displayed `C0`.

BLT p.7 also reports the stronger Magma computation
\(\operatorname{Jac}(C_0)(\mathbf Q)_{\rm tors}\cong
\mathbf Z/5\mathbf Z\times\mathbf Z/10\mathbf Z\). The argument below does not need
that exact group equality.

## Two elementary bridge lemmas

### Lemma A: finite endpoint avoidance

Fix the KL bad-prime data, the shift \(N_0/M_0\), and the polynomial \(g\). In the
proof of KL Lemma 3.1 one may choose an arbitrary sufficiently large positive integer
\(N_1\), then set

\[
\psi(\alpha)=\frac{1-N_1\alpha}{1+N_1\alpha},\qquad
\tau(q)=\psi^{-1}(q)=\frac{1-q}{N_1(1+q)}.
\]

The two endpoint coefficients of the transformed projective branch form are nonzero
exactly when

\[
g\!\left(-\frac{N_0}{M_0}+\frac1{N_1}\right)\ne0,
\qquad
g\!\left(-\frac{N_0}{M_0}-\frac1{N_1}\right)\ne0.
\]

Each equality excludes only finitely many positive integers \(N_1\), because \(g\)
has finitely many roots. Hence \(N_1\) can be chosen sufficiently large for all KL
local neighborhoods while avoiding both finite exceptional sets. Only after this
choice are the residue class and modulus fixed. Consequently the final form has
nonzero leading and trailing coefficients, and the optional \(\mathrm{SL}_2(\mathbf Z)\)
preprocessing at ST p.951 is not used. The original KL positive cone is preserved.

### Lemma B: signed squarefree injection through an even form

Let \(F\) be homogeneous of even degree six and let \(w\ne0\) be fixed. Suppose

\[
F(a_i,b_i)=t_iw^2\quad(i=1,2),
\]

where \(t_i\) are signed squarefree integers. If \(a_1/b_1=a_2/b_2\), then
\((a_2,b_2)=\lambda(a_1,b_1)\) for some \(\lambda\in\mathbf Q^\times\), so

\[
\frac{t_2}{t_1}=\frac{F(a_2,b_2)}{F(a_1,b_1)}=\lambda^6=(\lambda^3)^2.
\]

Signed squarefree representatives of the same rational square class are equal;
therefore \(t_1=t_2\). The same remains true after applying the fixed invertible
Möbius map \(\tau\). Thus a chosen witness for every distinct \(t\) injects the
counted values into the KL rational-parameter space.

## Proof draft

### 1. Fix the KL local and thin-set data

Apply the construction in the proof of KL Theorem 1.3 (pp.7--8) to the monic odd
model \(v^2=g(u)\). Let \(S\) be the fixed finite set of bad primes and put
\(M_0=\prod_{p\in S}p\). Choose a fixed sufficiently large \(N_0\), coprime to
\(M_0\), so that

\[
g(u)<0\quad\text{whenever}\quad
\left|u+\frac{N_0}{M_0}\right|_\infty<1.
\]

Set \(\phi=u+N_0/M_0\). KL Theorem 4.1 supplies a fixed thin set
\(\Omega\subset\mathbf Q\) outside which the torsion specialization produces the
required class-group rank. These data and the implied constants are independent of
the later height parameter.

### 2. Encode every local condition in one positive residue class

Use KL Lemma 3.1, with the finite endpoint avoidance of Lemma A, to choose and fix
\(N_1\), then fixed integers \(A,B,M\) (the proof permits \(A=B=1\)). For positive
integers \(a,b\) in this residue class, write

\[
q=a/b=(\psi\circ\phi)(P),\qquad
\phi(P)=\tau(a/b).
\]

All finite local neighborhoods and the real neighborhood imposed in Step 1 hold.
Clear fixed denominators and remove square factors from the branch equation to get a
degree-six squarefree binary form \(F\in\mathbf Z[X,Y]\) and a rational function
\(R\) satisfying

\[
g\!\left(\tau(X/Y)-\frac{N_0}{M_0}\right)=F(X,Y)R(X,Y)^2.
\]

The projective coordinate change preserves separability and irreducible-factor
degrees, so \(F\) has factor degrees \(1,1,4\), nonzero discriminant and nonzero
endpoint coefficients.

### 3. Apply the strong Stewart--Top branch in the same positive box

For the final fixed residue class, define \(w\) exactly as on ST p.948: the maximal
positive integer such that

\[
w^2\mid F(a,b)
\]

for every integral pair in that class. It is class-wise and is fixed before the
height parameter. Its maximality gives positivity of the local density in ST Lemma 2
(p.949).

Apply ST Theorem 1 with \(k=2\), total degree \(r=6\), and maximal irreducible-factor
degree \(m=4\). Its condition \(m\le2k+1=5\) holds. The bare theorem counts distinct
values by \(|t|\); the bounded positive-witness statement used here is extracted from
its proof:

- ST pp.951--952 constructs the relevant set of pairs with
  \(1\le a,b\le H\), in the fixed residue class, and with
  \(F(a,b)/w^2\) squarefree;
- p.953 equation (10) gives \(\gg H^2\) such pairs;
- equations (11)--(15), using Stewart 1991 Corollary 1, uniformly bound the number
  of primitive representations of one value;
- the paragraph immediately after (15) concludes that there are \(\gg H^2\)
  **distinct integer values**.

The constants depend only on the already fixed data. The proof works for every
sufficiently large box parameter, not merely a subsequence. If it is read first for
integer boxes, \(\lfloor H\rfloor\ge H/2\) transfers it to every sufficiently large
real \(H\), after shrinking the constant.

Therefore, for fixed \(c_0>0,H_0\), every \(H\ge H_0\) produces at least
\(c_0H^2\) distinct signed squarefree integers \(t\) with a witness in the same box
and

\[
F(a,b)=tw^2.
\]

### 4. Preserve the imaginary sign and delete the thin set

For every such \(t\), choose one bounded witness. The real neighborhood gives
\(g(u(P))<0\), and the displayed square identity gives \(t<0\).

The fixed Möbius transformation has bounded height distortion, so
\(H(\phi(P_t))\ll H\). By Lemma B the map from distinct \(t\) to these rational
parameters is injective. KL Lemma 3.2 says that the fixed thin set \(\Omega\) contains
only \(O(H)\) rational parameters of height \(O(H)\). Deleting them therefore leaves

\[
c_0H^2-O(H)\gg H^2
\]

distinct negative squarefree \(t\).

### 5. Obtain distinct fields of 5-rank at least two

For each surviving value, the field calculation in the proof of KL Theorem 1.2,
equations (3.1)--(3.2) and the following paragraph, gives

\[
\mathbf Q(P_t)=\mathbf Q(\sqrt{F(a,b)})=\mathbf Q(\sqrt t).
\]

The local ramification and real-place choices in the proof of KL Theorem 1.3, together
with KL Theorem 4.1, imply

\[
\operatorname{rk}_5\operatorname{Cl}(\mathbf Q(\sqrt t))
\ge
\operatorname{rk}_5\operatorname{Jac}(C_0)(\mathbf Q)_{\rm tors}
\ge2.
\]

Because the \(t\) are distinct negative squarefree integers, they define distinct
imaginary quadratic fields. The two conjugate points above one parameter may define
the same field, but the proof counts distinct \(t\), not geometric points, so no field
multiplicity remains.

### 6. Convert box height to discriminant height

For a fixed degree-six binary form,

\[
|F(a,b)|\le C_FH^6\qquad(1\le a,b\le H).
\]

Since \(F(a,b)=tw^2\) and the fundamental discriminant of
\(\mathbf Q(\sqrt t)\) has absolute value at most \(4|t|\),

\[
|\Delta_{\mathbf Q(\sqrt t)}|
\le \frac{4C_F}{w^2}H^6=:C_\Delta H^6.
\]

Given sufficiently large \(X\), take
\(H=\lfloor(X/C_\Delta)^{1/6}\rfloor\). Then \(H\gg X^{1/6}\), all surviving
fields have discriminant at most \(X\), and their number is

\[
\gg H^2\gg X^{1/3}.
\]

This proves the claimed lower bound, subject only to independent terminal review of
the complete assembled argument.

## The ten requested obligations

| # | Obligation | Evidence level and verdict |
| --- | --- | --- |
| 1 | Fixed admissible congruence class | **Source explicit:** ST p.948 fixes arbitrary `A,B,M,k`; Thm. 1 retains them. Passed. |
| 2 | Positive box/cone keeps \(\gg H^2\) | **Proof-level explicit:** ST pp.951--953. Lemma A ensures the optional cone-changing `SL2` step is skipped. Passed independent correction review. |
| 3 | Final-class maximal \(w^2\) | **Source explicit:** ST pp.948--949 defines `w` for the final class before height and uses maximality for positive local density. Passed; no global `w=2` substitution is used. |
| 4 | Distinct squarefree values, not pairs | **Proof-level explicit:** ST p.953 (10)--(15) and the next paragraph pass from pairs to distinct values. Passed, with the source's final object-name typo corrected. |
| 5 | Uniform representation multiplicity | **Source combination:** ST p.953 (13),(15) plus Stewart 1991 Cor. 1; fixed-content normalization changes only fixed constants. Passed. |
| 6 | Thin set contributes only \(O(H)\) | **Source explicit + Lemma B:** KL Lemma 3.2 counts rational parameters; Lemma B injects chosen distinct values into that space. Passed independent correction review. |
| 7 | Deletion leaves distinct fields | **Source calculation + elementary correction:** KL p.7 identifies the field; distinct signed squarefree `t` give distinct fields. Count by `t`, not by both conjugate points. Passed. |
| 8 | Imaginary sign preserves order | **Source proof + immediate sign transfer:** KL pp.7--8 fixes the real neighborhood; ST remains in the same positive cone; deleting \(O(H)\) from \(\gg H^2\) preserves the order. Passed independent correction review. |
| 9 | Uniform \(|\Delta_K|=O(H^6)\) | **Immediate:** fixed sextic bound and \(|\Delta_{\mathbf Q(\sqrt t)}|\le4|t|\); also agrees with KL p.8 exponent \(2g+2=6\). Passed. |
| 10 | Exact ST/KL/BLT hypotheses | ST's `r=6,k=2,m=4` satisfies Thm. 1; KL local/thin hypotheses are kept. BLT Theorem 2.1 supplies 5-rank 2, and the sample-to-`C0` model identification is proved by an explicit rational isomorphism. Passed. |

## Source-text corrections that must remain visible

1. **ST p.951 residue direction.** If `F_L=F o L`, the residue class preserving the
   original values is acted on by \(L^{-1}\), not by \(L\). Lemma A makes this step
   unused in the present proof.
2. **ST p.953 final `|T|`.** The pair set `T` is not itself the distinct-value set.
   Equations (11)--(15) first produce a distinct-value set of size \(\gg H^2\), which
   is the object that injects into `R_2`.
3. **KL p.7 distinct-field sentence.** Two conjugate points can generate the same
   quadratic field. Counting distinct signed squarefree `t`, or dividing a point count
   by at most two, is the correct statement.

None of these corrections changes the exponent. None may be omitted or attributed as
a literal theorem statement of the cited source.

## Quantifier order

The dependency order used above is

\[
C_0\Longrightarrow(S,M_0,N_0,\phi,\Omega)
\Longrightarrow N_1
\Longrightarrow(A,B,M,F,w,c_0,H_0,C_\Delta)
\Longrightarrow \forall H\ge H_0
\Longrightarrow \forall X\ge X_0.
\]

In particular, \(w\), the residue class, the thin set, all exceptional sets and every
implied constant are fixed before \(H\) and \(X\).

## Formal-verification boundary

The Lean files in `mathematics/formal/` certify elementary algebra and the conditional
implication from an explicit rational counting bridge to a cubic lower bound. They do
not formalize ST, KL, BLT, the construction of `C0`, or the unconditional analytic
bridge. Consequently this result cannot be called `VERIFIED` on the current evidence.
