import Std.Tactic

/-!
# Clearing a positive rational lower-bound constant by fixed height rescaling

The analytic source may supply a non-effective real constant `c > 0`.
Choosing any positive rational `p/q ≤ c` converts its consequence at source
height `q * H` into a natural-number quadratic lower bound.  This file checks
only the integer clearing step after such `p,q` have been supplied.
-/

namespace NoLogRationalScale

/--
If `count(qH)` satisfies the cleared rational bound
`p(qH)^2 ≤ q count(qH)`, then it satisfies the natural bound
`(pq)H^2 ≤ count(qH)`.
-/
theorem rational_lower_bound_after_scale
    {p q H count : Nat}
    (hq : 0 < q)
    (h : p * (q * H) ^ 2 ≤ q * count) :
    (p * q) * H ^ 2 ≤ count := by
  apply Nat.le_of_mul_le_mul_left (c := q) ?_ hq
  calc
    q * ((p * q) * H ^ 2) = p * (q * H) ^ 2 := by
      simp [Nat.pow_succ]
      ac_rfl
    _ ≤ q * count := h

/--
Using source height `2qH` gives the factor `2` required by the older
pre-deletion interface, with natural main constant `2pq`.
-/
theorem doubled_rational_lower_bound_after_scale
    {p q H count : Nat}
    (hq : 0 < q)
    (h : p * ((2 * q) * H) ^ 2 ≤ q * count) :
    2 * ((2 * p * q) * H ^ 2) ≤ count := by
  apply Nat.le_of_mul_le_mul_left (c := q) ?_ hq
  calc
    q * (2 * ((2 * p * q) * H ^ 2)) =
        p * ((2 * q) * H) ^ 2 := by
      simp [Nat.pow_succ]
      ac_rfl
    _ ≤ q * count := h

end NoLogRationalScale
