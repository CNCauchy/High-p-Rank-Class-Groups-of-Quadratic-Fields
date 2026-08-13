import Std.Tactic

/-!
# Separable algebraic lemmas for the C0 NO-LOG route

This file deliberately contains no Stewart--Top or Kulkarni--Levin analytic
claim.  It uses only Lean and Std, because Mathlib is not available in the
frozen worktree/toolchain.
-/

namespace NoLogAlgebra

/-- The quartic factor displayed for the BLT curve `C0`. -/
def c0Quartic (x : Int) : Int :=
  128 * x ^ 4 + 549 * x ^ 3 + 1007 * x ^ 2 + 936 * x + 368

/-- The expanded degree-five polynomial displayed for `C0`. -/
def c0Expanded (x : Int) : Int :=
  640 * x ^ 5 + 3641 * x ^ 4 + 8878 * x ^ 3 +
    11729 * x ^ 2 + 8392 * x + 2576

/-- The displayed linear-times-quartic factorization expands to `c0Expanded`. -/
theorem c0_explicit_factor_expansion (x : Int) :
    (5 * x + 7) * c0Quartic x = c0Expanded x := by
  have h1 : 5 * x * (128 * x ^ 4) = 640 * x ^ 5 := by
    simp [Int.pow_succ, Int.mul_comm, Int.mul_left_comm, Int.mul_assoc]
  have h2 : 5 * x * (549 * x ^ 3) = 2745 * x ^ 4 := by
    simp [Int.pow_succ, Int.mul_comm, Int.mul_left_comm, Int.mul_assoc]
  have h3 : 5 * x * (1007 * x ^ 2) = 5035 * x ^ 3 := by
    simp [Int.pow_succ, Int.mul_comm, Int.mul_left_comm, Int.mul_assoc]
  have h4 : 5 * x * (936 * x) = 4680 * x ^ 2 := by
    simp [Int.pow_succ, Int.mul_comm, Int.mul_left_comm, Int.mul_assoc]
  have h5 : 5 * x * 368 = 1840 * x := by omega
  have h6 : 7 * (128 * x ^ 4) = 896 * x ^ 4 := by omega
  have h7 : 7 * (549 * x ^ 3) = 3843 * x ^ 3 := by omega
  have h8 : 7 * (1007 * x ^ 2) = 7049 * x ^ 2 := by omega
  have h9 : 7 * (936 * x) = 6552 * x := by omega
  simp only [c0Quartic, c0Expanded, Int.add_mul, Int.mul_add]
  rw [h1, h2, h3, h4, h5, h6, h7, h8, h9]
  omega

/-- A finite list of forbidden natural numbers can be avoided above any bound. -/
theorem exists_large_nat_avoiding_finite_endpoints
    (forbidden : List Nat) (bound : Nat) :
    ∃ n : Nat, bound < n ∧ n ∉ forbidden := by
  induction forbidden generalizing bound with
  | nil =>
      exact ⟨bound + 1, by omega, by simp⟩
  | cons endpoint rest ih =>
      obtain ⟨n, hn, hrest⟩ := ih (max bound endpoint)
      refine ⟨n, ?_, ?_⟩
      · exact Nat.lt_of_le_of_lt (Nat.le_max_left bound endpoint) hn
      · have hendpoint : endpoint < n :=
          Nat.lt_of_le_of_lt (Nat.le_max_right bound endpoint) hn
        simp [Nat.ne_of_gt hendpoint, hrest]

/-- Two integers are in the same (integral) square class when the second is
the first multiplied by an integer square.  This one-way relation is exactly
the strength needed for homogeneous rescaling below. -/
def SameIntegralSquareClass (u v : Int) : Prop :=
  ∃ q : Int, v = u * q ^ 2

/-- If an integer-valued binary form is homogeneous of degree six, scaling
both inputs by `d` changes its value by the square `(d^3)^2`.

This is the even-degree algebraic fact used in the thin-set injectivity
argument.  No assertion that an arbitrary function is homogeneous is hidden:
the degree-six scaling law is an explicit premise.
-/
theorem degree_six_homogeneous_scaling_same_square_class
    (F : Int → Int → Int)
    (hHomogeneous : ∀ d a b : Int,
      F (d * a) (d * b) = d ^ 6 * F a b)
    (d a b : Int) :
    SameIntegralSquareClass (F a b) (F (d * a) (d * b)) := by
  refine ⟨d ^ 3, ?_⟩
  rw [hHomogeneous]
  simp [Int.pow_succ]
  ac_rfl

end NoLogAlgebra
