# M8.15.x: § 1's controls, registered before they run (2026-10-08T20:52:39Z)

Written before control 1a runs, and before § 1b's code exists. The case is the pyramid in R4, non-target (SURVEY.md). It uses the frozen slice about its 5-fold axis and the seed solve that `Branch.first` makes at `ε_min`.

## 1a: the stopping test (§ 1a), off the critical angle

**The case.** `P5a` is the pyramid rotated about its 5-fold axis by `θ₀ = π/10`, so that `u₋₂` carries the phase `e^{5iθ₀}`. That angle is the midpoint between the symmetric critical points 0 and `π/5`, since the circle is periodic in `2π/5`.
- No angle solve: the slice holds the angle at `θ₀`.
- Level 2.

**Expected:**
- **The old-form test stalls.** That is the frozen `pinned.py` at `6058f95`, run through a harness that changes no file:
  - it never falls below `10⁻¹¹` within 40 iterations;
  - it plateaus at `|μ| ‖M p₀‖ / ‖M x‖` within `10⁻³` relative;
  - the plateau is at least `10⁻⁸`, three orders of magnitude above the tolerance.
- **The new-form test passes.** That is the bench `pinned.py` with every multiplier in the test: it falls below `10⁻¹¹` at the same fixed point, with `σ` equal to 12 digits.
- **The multipliers:**
  - `|ν| ≥ 10⁻⁸`;
  - `μ = −ν ⟨p, s⟩_M / ⟨p, p₀⟩_M` within `10⁻⁶` relative.
- **Reported:** `μ`, `ν`, the bordered residual, and the old-form and new-form residuals at every iteration.

If the plateau comes out below `10⁻⁸`, the arm has failed as registered, and the margin is reported as measured.

## 1b: the angle solve (§ 1b), back to a critical point

This runs after § 1b's code exists.

**Expected:**
- **Where it lands.** Started at `θ₀ = π/10`, the solve lands on a symmetric critical point, `θ ∈ {0, π/5}` modulo `2π/5`, with `|ν| ≤ 10⁻¹²` and `μ` at round-off. Both the old-form and the new-form tests pass there.
- **What it selects.** It selects the lower-energy of the two, by decision 1. Which one is the minimum is not known beforehand.
- **The reference run.** A level-2 reference run at that point holds `d_ref ≤ η` over `T`.

## The pyramid's paired lift against `τ₀`: the interpretation, registered

The pyramid's rotations perpendicular to its axis lift as a paired pair, as `v₂`'s did. Its size relative to `τ₀` is recorded at every level and point where the pyramid runs.
- **Above `τ₀`.** That point is Unresolved for that reason, and 2a's criterion, the class of the in-span mode, is read regardless.
- **Why it matters.** A lift above `τ₀` makes the pyramid a candidate 2b control, the non-target case needed to replace `τ₀` legitimately.

## § 1a's regression fields (rule 5)

**Allowed to change:**
- the recorded `residual` field. It is now the full bordered residual; without a slice `μ → 0` at a solution, so it can differ from the old value in its last digits;
- the new field `gauge_multipliers`, which records `μ`.

**Must reproduce bit for bit:** everything else, including every Newton iteration count, `σ`, `ε` and `m`, every eigenvalue, and every verdict field.

## Amendment (2026-10-08T22:00:59Z): the slice covector projected into the solve space

Written after control 1a, before its rerun and before any of § 1b's code. It follows 1a's unregistered floor finding (`RESULT_1.md`). Everything above stands as registered.

**The change.** The bordered system uses the slice covector `Ŝ = B_r B_rᵀ M s` in place of `M s`, both as the multiplier force and as the constraint. `B_r` is Newton's own orthonormal basis of the fixed space. `P` is not used, since it is a projector only to the accuracy of the fitted fibre maps.
- `B_rᵀ Ŝ = B_rᵀ M s`, so the Newton column and row are unchanged.
- `Ŝᵀ(x − x_ref) = (M s)ᵀ(x − x_ref)` for every Newton displacement, since each lies in the fixed space. So the slice constraint is unchanged.
- The reduced problem, its solution, and `σ`, `μ` and `ν` are therefore unchanged. Only the part of `M s` outside the fixed space goes. The reduced equations never saw it; the full residual did.

**Where.** The projection is made in `solve_pinned`, where the covector enters the bordered system. Every solve takes that path, the angle solve's included, so none can bypass it.
- The raw slice `s` stays in `LevelCase` for the orientation and overlap diagnostics.
- `d_sigma_phi` reads the slice only through `B_rᵀ`, so it is unaffected.
- The closing controls have no slice, so the regression set is untouched.

**Expected, on 1a's rerun** (both arms; the frozen arm is unchanged):
1. `‖B_rᵀ(Ŝ − M s)‖ / ‖B_rᵀ M s‖ ≤ 10⁻¹²`.
2. `Ŝ`'s part outside the fixed space, `‖Ŝ − B_r B_rᵀ Ŝ‖ / ‖Ŝ‖`, is at most `10⁻¹²`, against `2.5×10⁻⁹` for `M s`.
3. All seven registered checks of 1a pass again.
4. **The floor.** The bench arm's final test value is at most `6×10⁻¹³`.
   - It is expected near `4.4×10⁻¹³`: the inside part, `1.3×10⁻¹³`, combined with the round-off remainder outside, `4.2×10⁻¹³` (`control_1a_floor.log`).
   - The `ν` term outside the fixed space, `|ν| ‖Ŝ − B_r B_rᵀ Ŝ‖ / ‖M x‖`, is at most `10⁻¹⁵`, against `8.5×10⁻¹³` before. So the floor no longer depends on `ν`.
5. **The converged point is unchanged** against the unprojected run of 21:01Z: `σ` to 12 digits, and `μ` and `ν` to `10⁻⁹` relative.

**Armed mutations.**
- **Checks 2 and 4:** the unprojected run of 21:01Z is the mutation. Its `M s` lies `2.5×10⁻⁹` outside the fixed space, and its floor is `9.6×10⁻¹³`, so all three numbers must fail on it.
- **Check 1:** a projection that drops one of `B_r`'s columns.
- **Check 5:** threshold mutations, as 1a's were.
- **Check 3:** 1a's own ten mutation arms, rerun on the new record.

**1b** uses the amended solver: its slice at every angle enters through the same path.

## Amendment (2026-10-08T22:09:19Z): § 1b's frozen rule, and control 1b's checks

Written before any of § 1b's code. It fixes what memo v4's § 1b leaves to the implementation, and turns 1b's registered expectations above into exact checks. Those expectations stand.

**The circle.** The lifted circle is the rotation of the representative about the case's pinned axis, the axis of its first generator. For an `n`-fold axis its period is `2π/n`. At angle `θ`:
- **the seed** is the oriented germ interpolant of `D(θ) u`, where `D(θ)` is the rotation by `θ` about the axis;
- **the slice** is the rotation generator about that axis applied to that seed, as `LevelCase` builds it at `θ = 0`, and it enters the solver through the amended path above;
- **Newton** runs at fixed norm `m` from that seed, with that slice.

The slice force there is `ν(θ)`. Its zeros are discrete standing waves, with `μ = 0` there too.

**The energy** at fixed `m` is `H = ½ xᵀ K x + g V(x)`. It is the functional whose critical points at fixed norm are the standing waves.

**The frozen rule** (decision 1). The same rule runs at both levels.
1. **The grid:** `N_grid = 10` angles over one period, `θ_k = θ_start + k · period / 10`. `θ_start = 0`, the oriented seed's angle, except in control 1b.
2. **The roots:** Brent's method on `ν` in every grid interval where `ν` changes sign, wrapping around the period, to `|ν| ≤ 10⁻¹²`. A root that does not reach that is recorded as unresolved, and never used.
3. **Minima:** a root is a minimum if its `H` lies below `H` at both ends of its interval.
4. **Selection:** the minimum with the lowest `H`.
5. **Symmetry:** two minima count as one if a mesh symmetry carries one onto the other. The test is that the largest normalized `M`-overlap over the 120 elements of the right action is at least `1 − 10⁻⁸`.
6. **Near-degenerate minima:** any inequivalent minimum whose `H` lies within a tenth of the grid's energy range of the lowest is recorded beside the selection.

**Control 1b.** It runs on the pyramid `P5` in R4 at level 2, at the norm of `Branch.first`'s seed solve at `ε_min`, with `θ_start = π/10`. No grid point then lies on a symmetric angle. The checks:
1. **Where it lands:** every root lies within `10⁻⁷` of `0` or `π/5`, modulo `2π/5`.
2. **The multipliers:** at the selected minimum, `|ν| ≤ 10⁻¹²` and `|μ| ≤ 10⁻¹²`.
3. **Both tests pass there:**
   - the frozen solver at `6058f95`, run from the seed at the selected angle, passes its own test;
   - the bench solver passes the new one.
4. **The selection** is the lower-energy of the two symmetric angles.
5. **The symmetry rule:** the same solve over two periods finds the selected minimum twice, and counts it once.
6. **The reference run:** at level 2 over `T = 1000`, with M8.15's step and alignment, the reference at the selected point holds `d_ref ≤ η = 10⁻³`.

**Unregistered diagnostic:** the same reference run at 1a's off-critical point. It measures the drift § 1b removes.

**Mutations:** each check gets at least one, as 1a's did.

**Not in this step:** the angle carried along a branch at every continuation step, with the selected minimum tracked. It comes next, with its own registered test, before 2a.

## Amendment (2026-10-08T23:57:20Z): the angle carried along a branch, and its tests

Written before any of the carry's code. It completes § 1b: "the angle is an unknown at every continuation step, carried from the previous accepted point."

**Why the tests take this form.**
- **No certified non-target orbit has a moving critical angle.** The pyramid's are fixed by its mirror symmetry at every norm, and one review unit found the C3 ray's fixed the same way: both have real Condon-Shortley coefficients. T4's representative is generic and complex, so it will be the first case where the roots move.
- **So the moving-root logic is covered two other ways:**
  - a moving coordinate on the pyramid, whose physical answer is certified;
  - synthetic tests on analytic functions. These are software tests, so the rule that acceptance rules come from controls does not apply to them.

**The carry rule.** It is applied at every continuation solve: every secant iterate, fold-search point and bisection point.
1. **The start.** It starts from the carried angle `θ_c`, the angle of the accepted point being continued from. Newton at each trial angle starts from that point's solution, rotated to the trial angle to first order by the rotation generator. The slice and its reference are those of the seed at the trial angle, as in § 1b.
2. **The local solve.** The bracket is `[θ_c − w, θ_c + w]`, with `w` one grid spacing, `period / 10`. If `ν` changes sign across it, Brent's method runs to `|ν| ≤ 10⁻¹²`.
3. **The kind check.** The root must be of the tracked kind: a minimum if its `H` lies below `H` at both ends of the bracket, a maximum if above both.
4. **The fallback.** If `ν` does not change sign across the bracket, the full rule of § 1b runs at that norm, with `θ_start = θ_c`. Its resolved root of the tracked kind nearest `θ_c` is taken, if it lies within two grid spacings. The record notes that the fallback was used.
5. **The registered ends** of the selected track. Each is recorded with its angle and norm, and none is ever followed by a re-selection:
   - "the carried root is not a minimum", when step 3 fails;
   - "the carried root is lost", when the fallback finds no minimum within two grid spacings;
   - "the carried root is unresolved", when Brent ends above `10⁻¹²`.
6. **The other critical points.** Those found at the first point are carried beside the selected minimum, by the same rule, at every ladder point. For each, the record keeps its angle, kind and `H`.
   - If a carried minimum falls below the selected one, the record says "no longer the lowest minimum" at the first point where that happens. The selected track continues, and is not re-selected.
   - If another track fails its kind check or is lost, that is recorded, and that track stops.
7. **The record** carries the coordinate angle, the physical angle, `ν` and `μ` at every accepted point, together with the fallback flag and the Newton solve count.

**The synthetic tests.** These have period `2π`, so `w = 2π/10`, with `ν = −∂H/∂θ`. The carry runs from the selected minimum of the full rule at the first `ε`.
1. **A root faster than the bracket.**
   - `H = −cos(θ − 1.5 w ε)` for `ε = 0, 1, …, 5`: the root is carried to `1.5 w ε` within `10⁻⁹` at every step, by the fallback at every step after the first.
   - The same with `2.5 w`: the branch ends "lost" at `ε = 1`.
2. **Annihilation.** `H = −cos θ + ε θ` for `ε = 0, 0.15, …, 0.9, 1.05`. The minimum is carried to `−arcsin ε` within `10⁻⁹` through `ε = 0.9`. The branch ends "lost" at `ε = 1.05`, where the minimum and the maximum have annihilated.
3. **Exchange.** `H = −cos 2θ − ε cos θ` for `ε = −0.5, −0.3, −0.1, 0.1, 0.3, 0.5`.
   - The selected minimum is `π`, and it is carried there within `10⁻⁹` throughout, never re-selected.
   - "No longer the lowest minimum" is recorded first at `ε = 0.1`.
4. **A kind flip.** `H = −(1 − ε) cos θ` for `ε = 0, 0.4, 0.8, 1.2`. The branch ends "the carried root is not a minimum" at `ε = 1.2`, and is never re-selected onto `π`.

**The pyramid arms.** Each is `P5` in R4 at level 2, on the ladder from `ε_min` to `ε = 2`, with the full rule's first point started at `θ_start = π/10`. Write `P = 2π/5` for the period.
1. **Past the basin.** At the third ladder step, the first carry solve starts from `π/5 − 0.45 P`, which is `0.05 P` from the maximum at `0`. The branch must end there with "the carried root is not a minimum". Its last accepted point must lie at `π/5` within `10⁻⁷`, and no point may be accepted at the maximum.
2. **A moving coordinate.** The physical angle is the coordinate plus `δ_k` at ladder step `k`, with `δ = (0, +0.05, −0.03, +0.06, −0.02, +0.04, −0.01) P` for `k = 0, …, 6`. The schedule is frozen here, and nothing measured feeds it. Each change is under `w`. At every accepted point:
   - the coordinate lies at `π/5 − δ_k` and the physical angle at `π/5`, both modulo `P` and within `10⁻⁷`;
   - `|ν| ≤ 10⁻¹²` and `|μ| ≤ 10⁻¹²`;
   - no fallback is used.

   The branch reaches `ε = 2`.
3. **Both critical points.** The maximum is carried beside the minimum. At every ladder point the two lie at `π/5` and `0`, modulo `P` and within `10⁻⁷`, half a period apart, and both `H` are recorded.
   - If the minimum stays below the maximum throughout, the arm passes.
   - If the order swaps, the swap must be caught as registered: the selected track ends with "the carried root is not a minimum" at the first point where its kind flips.
   - Since a real swap may not occur, synthetic test 4 is what arms this logic.

**Mutations:** each registered check gets at least one, as before.

**Known limit:** `overlap_classes` compares states up to a U(1) phase only. An `R2` slice case would need the Sp(1) fibre there. No `R2` slice case is in scope.

## Amendment (2026-10-09T00:42:42Z): a root's kind from ν's sign, and the carry's record and wiring

Written before any of this amendment's code. It closes § 1 before 2a.

**1. A root's kind comes from `ν`'s sign,** in the full rule and in the carry alike. The amendment of 22:09:19Z (step 3) and that of 23:57:20Z (step 3) read it from `H`; that is replaced.
- **The convention.** `ν = −c ∂H/∂θ` with `c > 0`, which is control 1b's (`c = 5.613` on its grid).
- **The test.** A resolved root is a minimum if `ν > 0` at the nearest solved angle below it and `ν < 0` at the nearest solved angle above it, and a maximum for the reverse.
  - Only solved angles with `|ν| > 10⁻¹²` count. The solved angles are those the rule has already solved at that norm, grid points and Brent iterates, taken modulo the period.
  - A root that meets neither condition has an unresolved kind. It is set aside, and never selected.
- **Grid points that are roots.** A grid point with `|ν| ≤ 10⁻¹²` is itself a root and enters once. Grid intervals with such an end are not searched.
- **The `H` cross-check.** `H` at the interval's ends stays in the record. For a grid-point root these are its neighbouring grid points.
  - The test is decisive where both ends differ from the root's `H` by more than `10⁻¹³`.
  - Where it is decisive and disagrees with `ν`'s sign, the kind is unresolved.
- **Selection** still takes the lowest `H` among minima.
- **In the carry,** a root of unresolved kind ends the selected track with a fourth registered end: "the carried root's kind is unresolved".

**2. The carry's local solve.**
- **When it searches.** It searches the bracket only if `ν` changes sign across it and neither end is itself a root. Otherwise the fallback runs.
- **When Brent stops.** Brent stops at the first iterate with `|ν| ≤ 10⁻¹²`, as step 2 registered, rather than running on to its own tolerance. This applies to the carry only; § 1b's full rule and its record stay as they are.

**3. The carry's record and wiring.**
- **An end's trial norm.** An end records its trial norm beside the last accepted norm, so the end is bracketed between them.
- **An end inside a change-of-type bisection** fails that bisection step, as a Newton failure does. It is recorded as an event, and the branch stays as it is.
- **Copies of the selected minimum.** The other critical points carried at ladder points exclude the copies of the selected minimum, those in its symmetry class.
- **The fallback's solve count** is its own, not the circle's running total.
- **Unregistered diagnostic:** the `M`-overlap of a fallback root with the source point.

**4. A dated note on step 1's wording.** The carry's Newton does not start from the accepted point's solution "rotated to the trial angle to first order by the rotation generator". It starts from that solution scaled to the trial norm, plus the change in the seed from that point's angle to the trial angle, both scaled to the trial norm. This is what the code has done since it was written. It sets only where Newton starts: the solved point is the same constrained solution.

**Checks:**
- **(a) The pyramid's full rule at `θ_start = 0`,** where both critical angles are grid points.
  - It finds exactly two roots per period, each once: `0`, a maximum, and `π/5`, a minimum.
  - It selects `π/5`, whose `H` and `σ` lie within `10⁻¹²` relative of control 1b's selected point.
- **(b) Synthetic `H = −cos θ`** with its grid started at `0`: one minimum at `0` and one maximum at `π`, each once.
- **(c) A flipped sign convention** on control 1b's recorded grid: both roots unresolved, caught by the `H` cross-check.
- **(d) Regression.**
  - § 1b's angle solve reproduces control 1b's roots, kinds and selection.
  - The carry's ten checks pass again, with the same kinds, selections and ends.
- **(e) An end inside a bisection.** On the pyramid, a kicked carry inside `goto` returns no point, records the event, and leaves the accepted points unchanged.
- **(f) Pyramid arm 1's end** records a trial norm above the last accepted one.

**Mutations:** each check gets at least one. For (a), the `H`-only rule on the same samples classifies neither root. For (b), a duplicated grid-point root and reversed neighbour signs.
