import Std.Tactic

/-!
# A source-aligned post-deletion bridge for the fixed C0 route

`NoLogInference.AnalyticBridge` deliberately exposes both the raw strong
count and the thin-set deletion.  The source-supported strong KL lemma in the
project is stated after that deletion.  This file records the smaller honest
interface needed at that point of the argument.

It does not construct the analytic inputs.  In particular, the positive
natural-number coefficient in `quadraticGoodCount` must first be obtained
from the source real constant by a fixed height rescaling; the associated
sixth-degree discriminant constant must be rescaled at the same time.
-/

namespace NoLogBridge

/--
The same root-free natural-number lower-bound predicate used by
`NoLogInference.CubicLowerBound`, repeated here so this repair theorem has a
self-contained certification unit.
-/
def CubicLowerBound (N : Nat → Nat) : Prop :=
  ∃ X0 A B : Nat,
    0 < A ∧ 0 < B ∧
      ∀ X : Nat, X0 ≤ X → B * X ≤ A * (N X) ^ 3

/--
The exact post-deletion data needed to turn a fixed-C0 strong KL count into
the root-free cubic lower bound.
-/
structure FixedC0PostDeletionBridge (N : Nat → Nat) where
  goodCount : Nat → Nat
  H0 : Nat
  X0 : Nat
  mainConstant : Nat
  discriminantConstant : Nat
  comparisonConstant : Nat
  selectedHeight : Nat → Nat
  mainConstantPositive : 0 < mainConstant
  comparisonConstantPositive : 0 < comparisonConstant
  quadraticGoodCount : ∀ H : Nat, H0 ≤ H →
    mainConstant * H ^ 2 ≤ goodCount H
  goodInjectsIntoFields : ∀ H : Nat, H0 ≤ H →
    goodCount H ≤ N (discriminantConstant * H ^ 6)
  fieldCountMonotone : ∀ x y : Nat, x ≤ y → N x ≤ N y
  selectorLarge : ∀ X : Nat, X0 ≤ X → H0 ≤ selectedHeight X
  selectorFits : ∀ X : Nat, X0 ≤ X →
    discriminantConstant * (selectedHeight X) ^ 6 ≤ X
  selectorCompares : ∀ X : Nat, X0 ≤ X →
    X ≤ comparisonConstant * (selectedHeight X) ^ 6

/--
Once the post-deletion quadratic count, field injection, monotonicity and
sixth-degree selector are supplied, the cubic lower bound follows.
-/
theorem no_log_of_fixed_c0_post_deletion_bridge
    {N : Nat → Nat} (h : FixedC0PostDeletionBridge N) :
    CubicLowerBound N := by
  refine ⟨h.X0, h.comparisonConstant, h.mainConstant ^ 3,
    h.comparisonConstantPositive, Nat.pow_pos h.mainConstantPositive, ?_⟩
  intro X hX
  let H := h.selectedHeight X
  have hH : h.H0 ≤ H := h.selectorLarge X hX
  have hGood : h.mainConstant * H ^ 2 ≤ h.goodCount H :=
    h.quadraticGoodCount H hH
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

end NoLogBridge
