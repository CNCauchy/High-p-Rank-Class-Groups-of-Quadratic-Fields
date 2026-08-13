import Std.Tactic

/-!
# A constructive sixth-root selector over the natural numbers

For a positive fixed height constant `D`, the recursion below maintains the
largest fitting height while the bound `X` is increased one unit at a time.
It is deliberately elementary and uses no real roots or Mathlib.
-/

namespace NoLogSelector

/-- Increment the current height exactly when the next sixth power fits. -/
def sixthSelector (D : Nat) : Nat → Nat
  | 0 => 0
  | X + 1 =>
      let H := sixthSelector D X
      if D * (H + 1) ^ 6 ≤ X + 1 then H + 1 else H

/-- The recursive selector fits, and its next height does not. -/
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

/-- For every bound, the selected height satisfies the lower fitting side. -/
theorem sixthSelector_fits (D X : Nat) (hD : 0 < D) :
    D * (sixthSelector D X) ^ 6 ≤ X :=
  (sixthSelector_spec D hD X).1

/-- For every bound, the successor of the selected height is already too large. -/
theorem sixthSelector_next_fails (D X : Nat) (hD : 0 < D) :
    X < D * (sixthSelector D X + 1) ^ 6 :=
  (sixthSelector_spec D hD X).2

end NoLogSelector
