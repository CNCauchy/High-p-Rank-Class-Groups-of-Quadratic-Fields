import Std.Tactic

/-!
# Elementary normalization lemmas for the fixed-C0 NO-LOG bridge

These lemmas isolate the arithmetic part of the height rescaling and the
two-sided sixth-degree selector.  They do not produce the source asymptotic
constant or prove that a maximal selector exists.
-/

namespace NoLogNormalization

/-- Reindexing a quadratic count from source height `L * H`. -/
theorem scaled_quadratic_reindex
    {mainConstant scale H count : Nat}
    (h : mainConstant * (scale * H) ^ 2 ≤ count) :
    (mainConstant * scale ^ 2) * H ^ 2 ≤ count := by
  calc
    (mainConstant * scale ^ 2) * H ^ 2
        = mainConstant * (scale * H) ^ 2 := by
            simp [Nat.pow_succ]
            ac_rfl
    _ ≤ count := h

/-- A fixed height scale multiplies the sixth-degree height constant by `L^6`. -/
theorem scaled_sixth_height
    {discriminantConstant scale H : Nat} :
    discriminantConstant * (scale * H) ^ 6 =
      (discriminantConstant * scale ^ 6) * H ^ 6 := by
  simp [Nat.pow_succ]
  ac_rfl

/--
If `H` is positive and the next height no longer fits under `X`, then the
same `H` compares with `X` up to the uniform factor `64 = 2^6`.
-/
theorem sixth_selector_compares
    {discriminantConstant H X : Nat}
    (hH : 0 < H)
    (hNext : X < discriminantConstant * (H + 1) ^ 6) :
    X ≤ (64 * discriminantConstant) * H ^ 6 := by
  have hSucc : H + 1 ≤ 2 * H := by omega
  have hPow : (H + 1) ^ 6 ≤ (2 * H) ^ 6 :=
    Nat.pow_le_pow_left hSucc 6
  have hScaled : discriminantConstant * (H + 1) ^ 6 ≤
      discriminantConstant * (2 * H) ^ 6 :=
    Nat.mul_le_mul_left discriminantConstant hPow
  calc
    X ≤ discriminantConstant * (H + 1) ^ 6 := Nat.le_of_lt hNext
    _ ≤ discriminantConstant * (2 * H) ^ 6 := hScaled
    _ = (64 * discriminantConstant) * H ^ 6 := by
          simp [Nat.pow_succ]
          ac_rfl

/-- The exact pair of selector inequalities used by the bridge. -/
theorem sixth_selector_bounds
    {discriminantConstant H X : Nat}
    (hH : 0 < H)
    (hFits : discriminantConstant * H ^ 6 ≤ X)
    (hNext : X < discriminantConstant * (H + 1) ^ 6) :
    discriminantConstant * H ^ 6 ≤ X ∧
      X ≤ (64 * discriminantConstant) * H ^ 6 :=
  ⟨hFits, sixth_selector_compares hH hNext⟩

end NoLogNormalization
