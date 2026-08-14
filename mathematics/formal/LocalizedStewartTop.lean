import Std.Tactic

/-!
# Auditable arithmetic consequences of the localized Stewart--Top input

This file does not formalize the analytic sieve or the Thue-equation estimate
in Stewart--Top, Theorem 1.  Those results remain external mathematical input.
It kernel-checks three separable steps used in Proposition 4.1 of the
manuscript:

1. division by one fixed nonzero square preserves distinct signed values;
2. an integer-box lower bound gives the expected natural-height interface;
3. after shrinking the constant by four, the same bound holds at every
   positive rational height, expressed without division by clearing the
   denominator.

The last theorem is the exact rational analogue of the manuscript's
`floor H >= H / 2` step.  Passing from rational to real height additionally
uses that a box of integral witnesses depends only on `floor H`; real numbers
are not available in the project's Std-only Lean environment.
-/

namespace LocalizedStewartTop

/-- The natural-height counting conclusion extracted from the source proof. -/
def NaturalBoxLowerBound (count : Nat → Nat) : Prop :=
  ∃ c H0 : Nat,
    0 < c ∧ 0 < H0 ∧
      ∀ H : Nat, H0 ≤ H → c * H ^ 2 ≤ count H

/--
The same conclusion at a positive rational height `p / q`, with denominators
cleared.  The inequality

`c * p^2 ≤ q^2 * count (p / q)`

is equivalent to `count (floor (p/q)) ≥ c * (p/q)^2`.
-/
def RationalBoxLowerBound (count : Nat → Nat) : Prop :=
  ∃ c H0 : Nat,
    0 < c ∧ 0 < H0 ∧
      ∀ p q : Nat, 0 < q → H0 * q ≤ p →
        c * p ^ 2 ≤ q ^ 2 * count (p / q)

/-- Cancelling the class-wise fixed square does not merge distinct values. -/
theorem fixed_square_preserves_distinct_values
    {w t₁ t₂ : Int} (hw : w ≠ 0)
    (h : t₁ * w ^ 2 = t₂ * w ^ 2) :
    t₁ = t₂ := by
  exact Int.eq_of_mul_eq_mul_right (Int.pow_ne_zero hw) h

/-- The integer-box conclusion is already uniform in every natural height. -/
theorem natural_box_lower_bound_of_source
    {count : Nat → Nat}
    (c H0 : Nat) (hc : 0 < c) (hH0 : 0 < H0)
    (hsource : ∀ H : Nat, H0 ≤ H → c * H ^ 2 ≤ count H) :
    NaturalBoxLowerBound count := by
  exact ⟨c, H0, hc, hH0, hsource⟩

/-- If `p/q ≥ 2`, then `p/q ≤ 2 * floor(p/q)`. -/
theorem numerator_le_twice_denominator_floor
    (p q : Nat) (hq : 0 < q) (hTwo : 2 * q ≤ p) :
    p ≤ 2 * q * (p / q) := by
  let n := p / q
  have hnTwo : 2 ≤ n := by
    exact (Nat.le_div_iff_mul_le hq).2 hTwo
  have hmod : p % q < q := Nat.mod_lt p hq
  have hdecomp : q * n + p % q = p := by
    simpa [n] using Nat.div_add_mod p q
  have hpLt : p < q * n + q := by
    omega
  have hnSucc : n + 1 ≤ 2 * n := by
    omega
  have hmul : q * (n + 1) ≤ q * (2 * n) :=
    Nat.mul_le_mul_left q hnSucc
  calc
    p ≤ q * (n + 1) := by
      apply Nat.le_of_lt
      simpa [Nat.mul_add] using hpLt
    _ ≤ q * (2 * n) := hmul
    _ = 2 * q * (p / q) := by
      simp [n]
      ac_rfl

/--
The floor step used to pass from sufficiently large integral box parameters to
every sufficiently large rational height.  The source constant is written as
`4*c` so that the conclusion has constant `c` after `floor(p/q) ≥ p/(2q)`.
-/
theorem rational_box_lower_bound_of_integer_boxes
    {count : Nat → Nat}
    (c U0 : Nat) (hc : 0 < c) (hU0 : 0 < U0)
    (hsource : ∀ n : Nat, U0 ≤ n →
      4 * c * n ^ 2 ≤ count n) :
    RationalBoxLowerBound count := by
  let H0 := max U0 2
  have hH0 : 0 < H0 := Nat.lt_of_lt_of_le hU0 (Nat.le_max_left _ _)
  refine ⟨c, H0, hc, hH0, ?_⟩
  intro p q hq hHeight
  let n := p / q
  have hU0Scaled : U0 * q ≤ p :=
    Nat.le_trans (Nat.mul_le_mul_right q (Nat.le_max_left U0 2)) hHeight
  have hTwoScaled : 2 * q ≤ p :=
    Nat.le_trans (Nat.mul_le_mul_right q (Nat.le_max_right U0 2)) hHeight
  have hnU0 : U0 ≤ n := by
    exact (Nat.le_div_iff_mul_le hq).2 hU0Scaled
  have hp : p ≤ 2 * q * n := by
    simpa [n] using numerator_le_twice_denominator_floor p q hq hTwoScaled
  have hpSq : p ^ 2 ≤ 4 * q ^ 2 * n ^ 2 := by
    have := Nat.pow_le_pow_left hp 2
    calc
      p ^ 2 ≤ (2 * q * n) ^ 2 := this
      _ = 4 * q ^ 2 * n ^ 2 := by
        simp [Nat.pow_succ]
        ac_rfl
  have hScaledFloor : c * p ^ 2 ≤ c * (4 * q ^ 2 * n ^ 2) :=
    Nat.mul_le_mul_left c hpSq
  have hCount := hsource n hnU0
  have hCountScaled : q ^ 2 * (4 * c * n ^ 2) ≤ q ^ 2 * count n :=
    Nat.mul_le_mul_left (q ^ 2) hCount
  calc
    c * p ^ 2 ≤ c * (4 * q ^ 2 * n ^ 2) := hScaledFloor
    _ = q ^ 2 * (4 * c * n ^ 2) := by ac_rfl
    _ ≤ q ^ 2 * count n := hCountScaled
    _ = q ^ 2 * count (p / q) := by simp [n]

end LocalizedStewartTop
