import Std.Tactic

/-!
# A rational-constant numerical bridge for the fixed-C0 NO-LOG route

This self-contained file clears a positive rational main-term constant by a
fixed height rescaling, constructs a discrete sixth-root selector, and proves
the root-free cubic lower bound.  The Stewart--Top/Kulkarni--Levin inputs are
not encoded in this file: they belong to the separately reviewed source
instantiation ledger.
-/

namespace NoLogSourceBridge

/-- The root-free natural-number encoding of `N(X) ≫ X^(1/3)`. -/
def CubicLowerBound (N : Nat → Nat) : Prop :=
  ∃ X0 A B : Nat,
    0 < A ∧ 0 < B ∧
      ∀ X : Nat, X0 ≤ X → B * X ≤ A * (N X) ^ 3

/-- Increment the selected height exactly when the next sixth power fits. -/
def sixthSelector (D : Nat) : Nat → Nat
  | 0 => 0
  | X + 1 =>
      let H := sixthSelector D X
      if D * (H + 1) ^ 6 ≤ X + 1 then H + 1 else H

/-- The recursive selector fits and its next height does not. -/
theorem sixthSelector_spec (D : Nat) (hD : 0 < D) : ∀ X : Nat,
    D * (sixthSelector D X) ^ 6 ≤ X ∧
      X < D * (sixthSelector D X + 1) ^ 6 := by
  intro X
  induction X with
  | zero =>
      simp [sixthSelector, hD]
  | succ X ih =>
      simp only [sixthSelector]
      split
      case isTrue hFitsNext =>
        constructor
        · exact hFitsNext
        · have hNextPow : (sixthSelector D X + 1) ^ 6 <
              (sixthSelector D X + 2) ^ 6 :=
            Nat.pow_lt_pow_left (Nat.lt_succ_self _) (by decide)
          have hScaled : D * (sixthSelector D X + 1) ^ 6 <
              D * (sixthSelector D X + 2) ^ 6 :=
            Nat.mul_lt_mul_of_pos_left hNextPow hD
          have hSuccBelow : X + 1 ≤ D * (sixthSelector D X + 1) ^ 6 :=
            ih.2
          exact Nat.lt_of_le_of_lt hSuccBelow hScaled
      case isFalse hDoesNotFit =>
        constructor
        · exact Nat.le_trans ih.1 (Nat.le_succ X)
        · omega

/--
The numerical data needed after source-level thin-set deletion.

The positive integers `p,q` encode a rational quadratic lower bound
`p*T^2 ≤ q*goodCount(T)`.  This is the exact integer form obtained after
choosing any positive rational number below the source real constant.
-/
structure RationalCountingBridge (N : Nat → Nat) where
  goodCount : Nat → Nat
  H0 : Nat
  p : Nat
  q : Nat
  discriminantConstant : Nat
  pPositive : 0 < p
  qPositive : 0 < q
  discriminantConstantPositive : 0 < discriminantConstant

  rationalQuadraticGoodCount : ∀ T : Nat, H0 ≤ T →
    p * T ^ 2 ≤ q * goodCount T
  goodInjectsIntoFields : ∀ T : Nat, H0 ≤ T →
    goodCount T ≤ N (discriminantConstant * T ^ 6)
  fieldCountMonotone : ∀ x y : Nat, x ≤ y → N x ≤ N y

/--
The rational counting interface implies the cubic lower bound.

The proof uses source height `q*H`, hence natural main constant `p*q` and
rescaled discriminant constant `D*q^6`.  The recursive selector supplies the
same height in both discriminant inequalities, with comparison factor `64`.
-/
theorem no_log_of_rational_counting_bridge
    {N : Nat → Nat} (h : RationalCountingBridge N) :
    CubicLowerBound N := by
  let D' := h.discriminantConstant * h.q ^ 6
  let Hbase := max h.H0 1
  have hD' : 0 < D' :=
    Nat.mul_pos h.discriminantConstantPositive (Nat.pow_pos h.qPositive)
  have hMain : 0 < h.p * h.q := Nat.mul_pos h.pPositive h.qPositive
  refine ⟨D' * Hbase ^ 6, 64 * D', (h.p * h.q) ^ 3,
    Nat.mul_pos (by decide) hD', Nat.pow_pos hMain, ?_⟩
  intro X hX
  let H := sixthSelector D' X
  have hSelector := sixthSelector_spec D' hD' X
  have hBaseFits : D' * Hbase ^ 6 ≤ X := hX
  have hHbase : Hbase ≤ H := by
    by_cases hLe : Hbase ≤ H
    · exact hLe
    · have hSuccLe : H + 1 ≤ Hbase := by omega
      have hPowLe : (H + 1) ^ 6 ≤ Hbase ^ 6 :=
        Nat.pow_le_pow_left hSuccLe 6
      have hNextFits : D' * (H + 1) ^ 6 ≤ X :=
        Nat.le_trans (Nat.mul_le_mul_left D' hPowLe) hBaseFits
      exact False.elim ((Nat.not_lt_of_ge hNextFits) hSelector.2)
  have hOneBase : 1 ≤ Hbase := Nat.le_max_right _ _
  have hHPositive : 0 < H :=
    Nat.lt_of_lt_of_le Nat.zero_lt_one (Nat.le_trans hOneBase hHbase)
  have hH0 : h.H0 ≤ H := Nat.le_trans (Nat.le_max_left _ _) hHbase
  have hHtoScaled : H ≤ h.q * H := Nat.le_mul_of_pos_left H h.qPositive
  have hSourceHeight : h.H0 ≤ h.q * H := Nat.le_trans hH0 hHtoScaled
  have hRational := h.rationalQuadraticGoodCount (h.q * H) hSourceHeight
  have hGood : (h.p * h.q) * H ^ 2 ≤ h.goodCount (h.q * H) := by
    apply Nat.le_of_mul_le_mul_left (c := h.q) ?_ h.qPositive
    calc
      h.q * ((h.p * h.q) * H ^ 2) = h.p * (h.q * H) ^ 2 := by
        simp [Nat.pow_succ]
        ac_rfl
      _ ≤ h.q * h.goodCount (h.q * H) := hRational
  have hFieldsAtHeight := h.goodInjectsIntoFields (h.q * H) hSourceHeight
  have hHeightIdentity :
      h.discriminantConstant * (h.q * H) ^ 6 = D' * H ^ 6 := by
    simp [D', Nat.pow_succ]
    ac_rfl
  have hFits : h.discriminantConstant * (h.q * H) ^ 6 ≤ X := by
    rw [hHeightIdentity]
    exact hSelector.1
  have hMonotone :
      N (h.discriminantConstant * (h.q * H) ^ 6) ≤ N X :=
    h.fieldCountMonotone _ _ hFits
  have hCount : (h.p * h.q) * H ^ 2 ≤ N X :=
    Nat.le_trans hGood (Nat.le_trans hFieldsAtHeight hMonotone)
  have hSucc : H + 1 ≤ 2 * H := by omega
  have hPow : (H + 1) ^ 6 ≤ (2 * H) ^ 6 :=
    Nat.pow_le_pow_left hSucc 6
  have hCompare : X ≤ (64 * D') * H ^ 6 := by
    calc
      X ≤ D' * (H + 1) ^ 6 := Nat.le_of_lt hSelector.2
      _ ≤ D' * (2 * H) ^ 6 := Nat.mul_le_mul_left D' hPow
      _ = (64 * D') * H ^ 6 := by
        simp [Nat.pow_succ]
        ac_rfl
  have hCube : ((h.p * h.q) * H ^ 2) ^ 3 ≤ (N X) ^ 3 :=
    Nat.pow_le_pow_left hCount 3
  have hScaledCompare : (h.p * h.q) ^ 3 * X ≤
      (h.p * h.q) ^ 3 * ((64 * D') * H ^ 6) :=
    Nat.mul_le_mul_left ((h.p * h.q) ^ 3) hCompare
  have hScaledCube : (64 * D') * ((h.p * h.q) * H ^ 2) ^ 3 ≤
      (64 * D') * (N X) ^ 3 :=
    Nat.mul_le_mul_left (64 * D') hCube
  calc
    (h.p * h.q) ^ 3 * X
        ≤ (h.p * h.q) ^ 3 * ((64 * D') * H ^ 6) := hScaledCompare
    _ = (64 * D') * ((h.p * h.q) * H ^ 2) ^ 3 := by
      simp [Nat.pow_succ]
      ac_rfl
    _ ≤ (64 * D') * (N X) ^ 3 := hScaledCube

end NoLogSourceBridge
