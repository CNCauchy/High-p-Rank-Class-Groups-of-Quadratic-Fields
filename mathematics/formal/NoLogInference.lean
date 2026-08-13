import Std.Tactic

/-!
# The explicit inference interface for the C0 NO-LOG candidate

This file does **not** formalize the analytic theorems of Stewart--Top or
Kulkarni--Levin.  Instead, it records those inputs as named, quantified
hypotheses and kernel-checks the complete counting implication that remains.

The conclusion uses the cubed natural-number form

`B * X ≤ A * (N X)^3`.

For positive constants `A` and `B`, this is the division- and root-free form
of `N X ≫ X^(1/3)`.  It is convenient in the Lean core/Std environment and
does not hide a real-analysis library assumption.
-/

namespace NoLogInference

/-- A root-free natural-number encoding of `N(X) ≫ X^(1/3)`. -/
def CubicLowerBound (N : Nat → Nat) : Prop :=
  ∃ X0 A B : Nat,
    0 < A ∧ 0 < B ∧
      ∀ X : Nat, X0 ≤ X → B * X ≤ A * (N X) ^ 3

/--
The complete interface between the source-supported strong KL argument and
the final counting implication.

The four proposition/proof pairs keep the mathematical meaning of the
analytic inputs visible.  The numerical fields state exactly the cardinality
consequences used by the kernel-checked inference:

* `strongSquarefreeCount` is the Stewart--Top positive-box lower bound in the
  fixed congruence class and with the class-wise maximal `w^2` removed;
* `thinCountBound`, `thinIsDominated`, and `deletePartition` express the KL
  thin-set deletion;
* `goodInjectsIntoFields` includes the local class-group-rank and distinct-field
  conclusions;
* `selector*` is the sixth-degree discriminant-height conversion for every
  sufficiently large discriminant bound.
-/
structure AnalyticBridge (N : Nat → Nat) where
  /-- Fixed congruence data from the positive-cone localization. -/
  A : Nat
  B : Nat
  M : Nat
  w : Nat
  modulusPositive : 0 < M
  fixedSquarePositive : 0 < w

  /-- The source-level local and geometric obligations, kept explicit. -/
  positiveConeAndFixedCongruence : Prop
  positiveConeAndFixedCongruenceHolds : positiveConeAndFixedCongruence
  classWiseMaximalFixedSquare : Prop
  classWiseMaximalFixedSquareHolds : classWiseMaximalFixedSquare
  boundedWitnessForEachSquarefreeValue : Prop
  boundedWitnessForEachSquarefreeValueHolds :
    boundedWitnessForEachSquarefreeValue
  thinParameterInjectionAndLocalRank : Prop
  thinParameterInjectionAndLocalRankHolds : thinParameterInjectionAndLocalRank

  /-- Counts before deletion, in the thin set, and after deletion. -/
  rawCount : Nat → Nat
  thinCount : Nat → Nat
  goodCount : Nat → Nat

  /-- Fixed constants and the box-height selector attached to a bound `X`. -/
  H0 : Nat
  X0 : Nat
  mainConstant : Nat
  thinConstant : Nat
  discriminantConstant : Nat
  comparisonConstant : Nat
  selectedHeight : Nat → Nat
  mainConstantPositive : 0 < mainConstant
  comparisonConstantPositive : 0 < comparisonConstant

  /-- Strong squarefree-value count in the same positive box and class. -/
  strongSquarefreeCount : ∀ H : Nat, H0 ≤ H →
    2 * (mainConstant * H ^ 2) ≤ rawCount H

  /-- Only linearly many bounded parameters lie in the KL thin set. -/
  thinCountBound : ∀ H : Nat, H0 ≤ H →
    thinCount H ≤ thinConstant * H

  /-- The linear exceptional term is dominated after enlarging `H0`. -/
  thinIsDominated : ∀ H : Nat, H0 ≤ H →
    thinConstant * H ≤ mainConstant * H ^ 2

  /-- Deleting the thin parameters partitions the raw count. -/
  deletePartition : ∀ H : Nat, H0 ≤ H →
    rawCount H ≤ goodCount H + thinCount H

  /-- Distinct good squarefree values inject into the desired fields. -/
  goodInjectsIntoFields : ∀ H : Nat, H0 ≤ H →
    goodCount H ≤ N (discriminantConstant * H ^ 6)

  /-- Counting fields is monotone in the discriminant bound. -/
  fieldCountMonotone : ∀ x y : Nat, x ≤ y → N x ≤ N y

  /-- The selected sixth-root height is in the asymptotic range. -/
  selectorLarge : ∀ X : Nat, X0 ≤ X → H0 ≤ selectedHeight X

  /-- Its associated discriminant bound lies below `X`. -/
  selectorFits : ∀ X : Nat, X0 ≤ X →
    discriminantConstant * (selectedHeight X) ^ 6 ≤ X

  /-- Conversely, `X` is at most a fixed multiple of the selected sixth power. -/
  selectorCompares : ∀ X : Nat, X0 ≤ X →
    X ≤ comparisonConstant * (selectedHeight X) ^ 6

/-- Thin deletion leaves the required quadratic-sized family in each box. -/
theorem good_count_lower_bound
    {N : Nat → Nat} (h : AnalyticBridge N)
    (H : Nat) (hH : h.H0 ≤ H) :
    h.mainConstant * H ^ 2 ≤ h.goodCount H := by
  have hStrong := h.strongSquarefreeCount H hH
  have hThin := h.thinCountBound H hH
  have hDominated := h.thinIsDominated H hH
  have hPartition := h.deletePartition H hH
  omega

/--
All explicit strong-KL interface hypotheses imply the NO-LOG cubic lower
bound.  This theorem certifies the full *inference*, not the analytic input
theorems themselves.
-/
theorem no_log_of_strong_kl_interface
    {N : Nat → Nat} (h : AnalyticBridge N) :
    CubicLowerBound N := by
  refine ⟨h.X0, h.comparisonConstant, h.mainConstant ^ 3,
    h.comparisonConstantPositive, Nat.pow_pos h.mainConstantPositive, ?_⟩
  intro X hX
  let H := h.selectedHeight X
  have hH : h.H0 ≤ H := h.selectorLarge X hX
  have hGood : h.mainConstant * H ^ 2 ≤ h.goodCount H :=
    good_count_lower_bound h H hH
  have hFieldsAtHeight : h.goodCount H ≤
      N (h.discriminantConstant * H ^ 6) :=
    h.goodInjectsIntoFields H hH
  have hFits : h.discriminantConstant * H ^ 6 ≤ X := h.selectorFits X hX
  have hMonotone : N (h.discriminantConstant * H ^ 6) ≤ N X :=
    h.fieldCountMonotone _ _ hFits
  have hCount : h.mainConstant * H ^ 2 ≤ N X :=
    Nat.le_trans hGood (Nat.le_trans hFieldsAtHeight hMonotone)
  have hCube : (h.mainConstant * H ^ 2) ^ 3 ≤ (N X) ^ 3 :=
    Nat.pow_le_pow_left hCount 3
  have hCompare : X ≤ h.comparisonConstant * H ^ 6 :=
    h.selectorCompares X hX
  have hScaledCompare : h.mainConstant ^ 3 * X ≤
      h.mainConstant ^ 3 * (h.comparisonConstant * H ^ 6) :=
    Nat.mul_le_mul_left (h.mainConstant ^ 3) hCompare
  have hScaledCube : h.comparisonConstant *
      (h.mainConstant * H ^ 2) ^ 3 ≤
      h.comparisonConstant * (N X) ^ 3 :=
    Nat.mul_le_mul_left h.comparisonConstant hCube
  calc
    h.mainConstant ^ 3 * X
        ≤ h.mainConstant ^ 3 * (h.comparisonConstant * H ^ 6) :=
          hScaledCompare
    _ = h.comparisonConstant * (h.mainConstant * H ^ 2) ^ 3 := by
          simp [Nat.pow_succ]
          ac_rfl
    _ ≤ h.comparisonConstant * (N X) ^ 3 := hScaledCube

end NoLogInference
