# M8.15.x: Target 1's locator, its tests registered before code (registered 2026-10-09, v3)

**Status:** registered, v3. It folds both review units' reviews of v1, v2 and v3. Both gave GO on v3, and their NITs on v3 were folded before this stamp. It is frozen before any locator code is written. A later change is a dated amendment; this text is not edited.

## 1. What is built

**A folder of its own,** beside the frozen instrument on MIT main.
- It reads the instrument read-only from `../soft-slot-dynamics-m8-15x/m8_15x_solver/`.
- No instrument file changes.

**`locate.py`, the locator:**
- **`structural_span`.**
  - It takes the exact fibre generators' vectors and `X_aΦ`, each `M`-normalized, without the phase partner `χ`.
  - The case's frozen continuum dimension `d` comes with it: 3 for C2a; 4 for C3, T2 and T3.
  - `P` is the top-`d` principal subspace.
  - The gap gate is `σ_d/σ₁ ≥ 0.1` and `σ_{d+1}/σ₁ ≤ 0.05`.
- **`near_zero_L`:**
  - the `k_L` eigenpairs of `(L, M)` nearest the shift `−10⁻⁶`, by shift-invert;
  - `k_L` starts at 16, and doubles to 32 and 64 on a coverage failure;
  - the factorization is built as `negative_index_L` builds it, and freed after use.
- **`classify`:**
  - each eigenvalue classed negative below `−tol_L` (the frozen `n(L)` threshold), nonnegative otherwise;
  - the coverage cosines between `P` and the eigenvectors' span;
  - each eigenvector's overlap with `P`, structural at 0.9 or more;
  - the structural subspace check: exactly `d` structural eigenvectors, whose span's cosines with `P` are all at least 0.9;
  - `n_S`.
- **`evaluate`:** the frozen point data (as `m815_branch.Point`), the near-zero data, and the slowest genuine pair's static overlap with `span{X_aΦ}`.
- **`locate`:**
  - the grid and the bisection;
  - the steps, with each crossing set matched between a step's ends by the assignment problem on squared `M`-overlaps;
  - the crossing identity check: the crossing set's spans at `lo` and `hi` have all principal cosines at least 0.9;
  - the spectral-coverage check on `Δn(L)`, the classes, and the bookkeeping checks.
- **`guards`.**
  - **Offset guards.** Each level is read at its own root's offset. The pair goes to `decide(e, p3, p2, third=True)`, with `e` the level-3 guard's `ε`.
  - **Region ends** read as the rerun ladder's own verdict at those points, with the ladder's `third = (i % 3 == 0)`.
  - **Decided.** A guard, region ends included, is decided only if the verdict is Elliptic or Hyperbolic and both of its points pass `evaluate`'s checks.
  - **The diagnostic.** The same-`ε` reading is computed beside each guard.
  - **Counting.** A guard counts only if each level's genuine index equals its step-end value on that side.
  - **The reading** on a side is the nearest counting decided guard. A side whose counting decided guards disagree is mixed.
- **`decide`,** the frozen closure itself.
  - It is extracted from the frozen `m815_branch.py` through its syntax tree.
  - Its free names are bound exactly as `run_branch` binds them, with the module's own globals:
    - `name` and `slot`;
    - `tau0_3`, `s2` and `dlev`;
    - `omega0`, from the level-2 case's `λ₀`;
    - `sch`, built from the full ladder, `ladder(0.25, EPS_MAX[slot])`.
  - The SHA-256 of the extracted source is recorded in every record and in the manifest.
- **`name`:** the naming, with each reading's offset and `ε` at each level, and the region-end qualification.

**`t1_branch.py`, the driver.**
- **The guard.** It refuses a target unless the instrument's `out/FROZEN.json` passes three checks:
  - it exists;
  - every value in the instrument's `out/freeze_numbers.json` appears in it unchanged;
  - it carries the terms' SHA-256 (computed from the terms file given) and a non-empty go.
- **Records.** It writes the record on every end, atomically, and a crash record on an instrument exception, as M8.15.x's § 4 does.
- **Test hooks,** for controls only: a forced Newton `maxit` at a chosen midpoint, and a bracket given on the command line.

**A failed solve's residual history.**
- The failed solve is rerun under a trace of `solve_pinned`'s stopping-test locals, as control 1a traced its arms.
- The solve is deterministic, so the trace reproduces the failure.
- `pinned.py` is not changed.

## 2. The synthetic tests (S), on a mock evaluator

**The mock evaluator.** It replaces the solver. It plants spectra, and the locator reads them through the frozen functions.

**The static spectrum.** The mock space has 80 dimensions, with `M = I`, so up to 64 eigenpairs can be returned. At each `ε` and level it holds:
- **4 structural eigenpairs,** spanning the planted structural span `P` (`d = 4`): an exact zero, at `10⁻¹⁴`, and three lifts at `−10⁻⁵`.
- **A genuine doubled crossing pair,** `s_h(ε) = a(r_h − ε)` with `a = 0.05`. It is positive below the root and negative above it, and its eigenvectors are orthogonal to `P`.
- **74 inert positive spectators,** at `0.05 × 40^(k/73)` for `k = 0` to 73 (0.05 to 2.0).

**The counts are physical.**
- `n(L)` is the count of planted eigenvalues classed negative: 3 below the root and 5 above.
- The cluster's frozen dimension is 8, as T2's is, and `n(B|G_tol)` is planted at 3.
- So the genuine index is 0 below the root and 2 above. That agrees with the Krein count: no unstable or Krein-negative mode below, two real pairs above.
- Every test keeps this consistency, except S9, which breaks it on purpose.

**The Hamiltonian genuine set.**
- The crossing pair, `λ_h² = c(ε − r_h)` with `c = 0.01`, doubled. It is imaginary with Krein sign + below the root, and real above it.
- Another imaginary pair at `0.0745 i ε`, Krein +, the same at both levels.
- Both members of each pair are planted, as `Verdict.genuine_all` holds them.

**Each field `decide` reads is derived from the plant by the frozen rules:**
- **The counts.** `genuine` is `representatives(genuine_all, τ_Re)`, the frozen function. `k_r`, `k_c` and `k_i⁻` follow `Verdict.count`'s rules, called on the mock.
- **`balanced`:** whether `k_r + 2k_c + 2k_i⁻` equals `n(L) − n(B|G_tol)`.
- **`zero_crossing`:** whether any genuine `|λ|` is at most `τ₀`.
- **`cluster_ok`:**
  - the planted dimension (8) equals the frozen one;
  - the cluster is closed;
  - the Ω-Gram value is 1.
- **`fast`:** none when balanced. When unbalanced, the mock's fast search finds nothing.
- **`bwe`:** the planted backward error, `10⁻¹²`.
- **The lifted modes:** `10⁻⁶`, of the paired kind. That is `Point`'s rule for a case outside `RADICAL_ALL` with no slice.

**Frozen values and the case.** The mock uses R4's `s₂ = 6.739×10⁻⁴`, `ω₀ = √48`, `τ₀ = τ_Re = 1.040×10⁻⁵`, `δ_lev = 10⁻²` and `tol_L = 10⁻⁹`. The mock case is not in `SPECTRA`, so the first-resolved and radical-bound reasons are left to R4b.

**The region ends** are ladder points 0.6 and 1.4, at ladder indices 11 and 14. They mirror T2/R4's 11.31 and 32, and so are read with `third` false.

**The baseline plant:**
- the bracket `[0.8, 1.2]` and the guard region `[0.6, 1.4]`;
- `r₃ = 1.0130` and `r₂ = 1.0181`, a shift of +0.50%, both off the grid's points (`0.8 + 0.05k`);
- no collision, and Newton never fails.

Each test below changes only what it names.

| # | Planted | Expected |
|---|---|---|
| S1 | The baseline. | One genuine step per level, with `Δn(L) = +2`, `Δn_S = 0` and a genuine change of +2. Each root within `10⁻³` relative of its plant, and `δ` within 0.2% of +0.50%. Readings at `d = 0.01` on both sides: Elliptic below, Hyperbolic above. Named "a located change of type". The same-`ε` diagnostic is Unresolved at `d = 0.01, 0.02, 0.05` and `0.10` on both sides. |
| S2 | No genuine crossing. Two of the three existing lifts become a structural crossing: their eigenvalue follows `0.01(ε − 0.9137)` at both levels, and `n(B\|G_tol)` falls with them from 3 to 1. | One structural step per level (`Δn(L) = Δn_S = −2`), and no genuine step. "No genuine crossing detected" at both levels. |
| S3 | S1, plus S2's structural crossing. | Two steps per level, one structural and one genuine. The genuine one is named as in S1. |
| S4 | S1, with a backward error of `10⁻⁹` at every upper guard and at the region's upper end. | No reading above: "an index crossing located; the change of type remains unresolved". |
| S5 | S1, with the two real pairs replaced by one Krein-negative imaginary pair at both levels' points of the upper guard `d = 0.05`, so the genuine index stays 2 and the levels agree. | The upper side is mixed (Hyperbolic at 0.01, Elliptic at 0.05); unresolved. |
| S6 | S1, with a genuine quartet at one bisection midpoint inside the level-3 step. | A collision is recorded; unresolved. |
| S7 | S1, with a Newton failure at the first midpoint inside the level-3 step. | That step is Unresolved (Newton failure), over the bracket reached, with the planted residual history; unresolved. |
| S8 | S1, with one level-3 crossing eigenvector's overlap with `P` at 0.95 at `hi` and 0.60 at `lo`. | Mixed overlap; that step is Unresolved, and so is the result. |
| S9 | S1, with `n(B\|G_tol)` planted so that the genuine change is +1 while two genuine eigenvalues cross. | Index bookkeeping; that step is Unresolved. |
| S10 | S1, with one lift's eigenvector tilted out of `P` to overlap 0.85 at the first level-3 bisection midpoint. The rest of that direction of `P` goes to the inert spectator at 0.05, which is among the nearest 16, so coverage passes. | The structural subspace check fails there; that bisection stops, and the step is Unresolved (structural subspace) over the bracket reached. |
| S11 | S1, with the slowest pair's overlap at 0.90 at the upper guard `d = 0.01`. | That guard is Unresolved. The reading is taken at `d = 0.02`, and the result is still located. |
| S12 | S1, with level 2's root moved to 1.30, outside the bracket. | One genuine step at level 3 and none at level 2: a cross-level disagreement; unresolved. |
| S13 | S1, with a shift of +2.0% (`r₂ = 1.0333`). | The matched readings fail the cross-level check through the other pair at every offset. The upper region end fails it through the crossing pair at the same `ε`. The lower region end, read as the ladder read it with no cross-level check, reads Elliptic. With no reading above, this is the registered limit: "an index crossing located; the change of type remains unresolved". |
| S14 | A genuine crossing exactly on a grid point, at 1.0000 at both levels. | One step per level, neither lost nor doubled, with its root within `10⁻³` relative. |
| S15 | S1, with 16 of the inert spectators moved to `+10⁻⁷ k` (`k = 1` to 16). They are nearer the shift than the three lifts and, at the step's ends, than the crossing pair, and they leave `n(L)` unchanged. | At `k_L = 16` the three lifts are missed, so coverage fails. The enlargement to 32 recovers them, and the result is as in S1, with `k_L = 32` recorded. |
| S16 | S1, with every upper offset guard Unresolved (S4's backward error, at those guards only), and a second genuine crossing at 1.25 at both levels, between the last offset guard and the region's end. | The region end's genuine index differs from the step's end value, so it does not count. No reading above; unresolved. |
| S17 | S1, with the crossing pair's computed basis rotated inside its two-dimensional eigenspace by `θ(ε) = 2π ε/0.01`, about 28° across a final step of width `0.05/2⁶ = 7.8×10⁻⁴`. | As S1: the same steps, classes and readings. The crossing set is matched as a subspace. |

**The mutation arms.** Each test has one. The arm moves the input that its expectation turns on across the threshold, and the expectation must then fail:

| # | The arm |
|---|---|
| S1 | A bisection width of `10⁻²` (the root check). |
| S2 | The two lifts' eigenvectors tilted out of `P` to overlap 0.85, the rest of those directions going to the inert spectators at 0.05 and 0.0526, among the nearest 16. Coverage passes, and the structural subspace check fails at every point. |
| S3 | As S2's arm. |
| S4 | The backward error back to `10⁻¹²`. |
| S5 | No replacement. |
| S6 | No quartet. |
| S7 | No failure. |
| S8 | 0.60 at both ends. |
| S9 | A consistent `n(B\|G_tol)`. |
| S10 | 0.95. |
| S11 | 0.89, read at 0.01. |
| S12 | Level 2's root restored. |
| S13 | A shift of 0.5%. |
| S14 | The crossing set classed by `s ≤ 0` while `n(L)` keeps its threshold. |
| S15 | `k_L` capped at 16 (Unresolved, spectral coverage). |
| S16 | No second crossing, so the region end counts. Read with the ladder's `third`, it is Hyperbolic, and the result is located with a region-end reading named as such. |
| S17 | Matching by individual overlaps of at least 0.9, with no subspace check. At 28° those overlaps are 0.88, so the step is Unresolved (crossing identity). |

The parent passes before each arm runs.

## 3. The real-solver controls (R), on orbits that are not targets

**R1. C2a/R4, a structural crossing.**
- **Where.** Its `n(L)` and `n(B|G_tol)` fall from 2 to 0 together:
  - at level 3, between 32 and 45.25;
  - at level 2, between 11.31 and 16.

  M8.15's committed control record and the qualification's rerun both show it.
- **The brackets** are those two ladder intervals, at their own levels.
- **Expected, at each level:**
  - exactly one step, with `Δn(L) = Δn_S = −2`;
  - its two crossing eigenvectors structural, with overlap at least 0.9 at both ends;
  - a genuine change of 0;
  - at every evaluated point, the span's gate passing with `d = 3`, and coverage and the structural subspace passing.
  - The bracket is named "no genuine crossing detected".
- **The gate's expected values.**
  - `σ₃/σ₁` near 0.3587, its frozen frame's continuum value (`span_gate_continuum.out`). Level 2 measured 0.3588 (`span_rank_controls.out`).
  - `σ₄/σ₁` at most 0.05. It is a mesh residual: `7×10⁻³` at level 2, and expected smaller at level 3.
- **The arm:** rerun the classification with `span{X_aΦ}` left out of the structural span. The crossing eigenvectors then read genuine, and the expectation must fail.

**R2. C3/R4, no crossing.**
- **The bracket:** 11.31 to 16, at both levels.
- **Expected:**
  - no step;
  - `n(L) = 9` at every evaluated point, as at all 18 of C3's ladder points at both levels;
  - the span's gate passing with `d = 4`. The statistic is near 1.0, its frozen frame's continuum value; level 2 measured 1.0;
  - coverage and the structural subspace passing, with `n_S` recorded;
  - the bracket named "no genuine crossing detected".
- **The arm:** R2's evaluation, applied to R1's record, must fail.

**R3. A forced Newton failure.**
- **The run:** C2a/R4 at level 2, bracket 11.31 to 16, with Newton forced to one iteration at the first bisection midpoint.
- **Expected:**
  - that bisection ends there;
  - its step is reported over the bracket reached, as Unresolved (Newton failure);
  - the residual history of every failed attempt is recorded, the frozen retries included;
  - a record is written, and the exit is normal.
- **The arm:** the hook off. R3's expectation must fail.

**R4. The extracted verdict on the control ladders.**
- **The run:** the driver's ladder and the extracted `decide`, on C3/R4 and C2a/R4 at both levels, over their full ladders, without persistence.
- **Expected:**
  - every type and every reason equals the qualification's branch records exactly;
  - every ladder point's frozen data is bit for bit, apart from the fields the locator adds.
- **The arm:** the extracted `decide` bound with `dlev = 0`. C3's two levels' rates differ (`d₃ = 1.25×10⁻⁴`), so every C3 point must then read Unresolved (level stability), and the regression must fail.

**R4b. The nine Unresolved reasons.**
- **The run.** On constructed point pairs for control cases (C2a for a paired lift, C3 for a radical one), each reason is triggered alone. The extracted and bound `decide` must return exactly that reason:
  - a mode before its first-resolved point (at `e = 0.2`, below `ε_min`);
  - the cluster check;
  - a zero crossing;
  - an unbalanced Krein count;
  - the radical bound;
  - a paired lifted mode above `τ₀`;
  - an eigenpair residual;
  - a cross-level disagreement;
  - level stability.
- **Two passing pairs** must give Elliptic and Hyperbolic.
- **The arms:** each binding mutated in turn (`tau0_3`, `s2`, `omega0`, `dlev`, `sch`). For each, at least one case's reason must change.

**R5. The guard's validation.** This runs on a scratch copy of the instrument's folder; the real `out/` is never written.
- **Expected:** the driver refuses a target in each of these cases:
  - with no `FROZEN.json`;
  - with one value in it differing from `freeze_numbers.json`;
  - with a terms hash that differs from the terms file's;
  - with an empty go.
- **The pass case:** with a complete, matching `FROZEN.json`, it gets past the guard. The test then stops before any solve.
- **The arm:** the equality check disabled. The second case must then pass, and the test must fail.

## 4. Qualification and freeze of the locator

1. **This registration,** frozen before code.
2. **The code.** Plumbing dry runs are allowed on controls only. They are unrecorded, and never run on a target.
3. **The tests:** S1 to S17 and R1 to R5, R4b included, each with its arm. A green parent is required before each arm.
   - All must pass, R1 and R2 at level 3 included, before any target is admitted.
   - Any failure stops the work before the terms freeze. A fix is registered as a dated amendment, and the tests are rerun.
4. **The freeze:** the locator's folder with its own manifest and `SHA256SUMS` on MIT main.
   - The manifest records the SHA-256 of the locator's files, and of the extracted `decide` source.
   - It also records the instrument files the locator reads, which must equal the hashes in `97a8c08`'s manifest.
5. **The instrument's freeze tooling.** `freeze_manifest.py check` flags every unpinned file in the instrument's folder, so it would flag `out/FROZEN.json` once the guard is written.
   - **The fix:** before the guard is written, the check excludes `out/FROZEN.json`, with a dated note in that folder's `REPRODUCE.md` and a new `SHA256SUMS`.
   - No instrument file changes.
   - The guard's contents are validated separately, by the locator (R5).

## 5. What is not covered

- **No real-solver test has a genuine crossing.** None of the non-target controls has one:
  - C2a, C2b, C3 and the pyramid each keep their genuine index along their ladders;
  - C2a's and C2b's changes in `n(L)` are structural;
  - C1 runs at one point.

  So the genuine-crossing logic, and the matched-offset reading of the guards, are tested on the mock evaluator only. The real-solver plumbing is tested on a structural crossing and on no crossing. The terms say so, and both units accepted the matched-offset reading on that basis (the memo's rule 2).
- **The span's gate at the targets.** It rests on the continuum values in their frozen frames, 0.966 for T2/R4 and 0.408 for T3/R5, with no real-solver measurement before the run. A target point that fails it reads Unresolved (structural span).

*Registered at 2026-10-09T21:58:26Z, before any locator code.*

## Amendment (2026-10-09T22:02:55Z): S8, before any locator code or test ran

**What is wrong with S8 as registered.** It plants a crossing eigenvector with overlap 0.60 with `P` at `lo`. No plant can do that while `lo` passes the structural subspace check.
- If the structural eigenvectors' span has every principal cosine with `P` at least 0.9, every other eigenvector, being orthogonal to that span, has overlap with `P` at most `√(1 − 0.81) = 0.436` (DERIVED).
- So the plant would stop the bisection by the structural subspace check, not by the mixed-overlap rule S8 expects.

**The general consequence (DERIVED).** The mixed-overlap rule cannot fire at a step whose ends pass the structural subspace check and whose crossing passes the identity check.
- A crossing direction would have to move from an overlap of at most 0.436 to one of at least 0.9: a turn of at least 38.4°.
- The identity check allows at most 25.8°.
- The rule stays as a conservative backstop.

**S8 is replaced by:** S1, with one level-3 crossing eigenvector turning toward `P` across the final step.
- Its overlap goes from 0.40 at `lo` to 0.95 at `hi`.
- The structural eigenvector it displaces falls to 0.31 at `hi`, so both ends pass the structural subspace check.

**Expected:** the step is Unresolved by the crossing identity check (the turn is about 48°), and so is the result.

**Its arm:** 0.40 at both ends. The step is then genuine, and the result located.

Nothing else in this registration changes.

## Amendment (2026-10-09T22:10:11Z): the root of a step, before any recorded test ran

**What a plumbing run on the mock found** (unrecorded, as § 4 allows). With each step's root taken as the midpoint of its final interval, S1's upper guard at `d = 0.01` fails level stability.
- A root located to a width of `10⁻³` is off by up to `5×10⁻⁴` relative, which is 5% of a 1% offset.
- Through `λ ∝ √(ε − r)`, that moves the crossing pair by up to 2.5%. The two levels' errors do not cancel.
- In the run, the located roots were `1.01289` and `1.01836` against the planted 1.0130 and 1.0181. The upper `d = 0.01` reading then differed by about 1.85%, against level stability's 1%.
- The registered expectations, worked by hand, had assumed exact roots.

**The change.** Each step's root is the zero of its crossing eigenvalue, interpolated linearly between `lo` and `hi`: the mean over the crossing set's eigenvalues, kept inside `[lo, hi]`.
- The interval and its midpoint are reported with the root.
- An Unresolved step keeps its interval, without a root.
- The interpolation's error is second order in the width. For the mock's linear crossing it is exact.

**Why not a finer bisection.** A narrower final interval sits nearer the root. There the crossing eigenvalue approaches the lifts' eigenvalues, and a mode sharing their symmetry can mix with them, which the structural subspace and identity checks would then report as Unresolved (INFERRED).

**What does not change:** every test and expectation. They are run after this amendment. The terms take the same change in their next draft.

## Amendment (2026-10-09T22:10:53Z): S1's arm, before any recorded test ran

**Why S1's arm must change.** With the root interpolated (the amendment above), the mock's linear crossing is located exactly at any bisection width. So S1's registered arm, a width of `10⁻²`, no longer touches what S1's expectation turns on, and a plumbing run confirmed it is not caught.

**The new arm:** each step's root is taken as its final interval's midpoint, the rule the amendment replaced. S1's expectation must then fail. As the plumbing run found, the upper reading at `d = 0.01` is lost to level stability.

Every other test, expectation and arm stands.

## Amendment (2026-10-10T09:58:33Z): R1 failed at level 3; a step is read between balanced ends

**What happened.** R1 failed at level 3, as registered.
- **The cause.** C2a's doubled structural eigenvalue rises slowly there, about `2.8×10⁻⁷` per unit of `ε` near 34. The instrument reads it against two different thresholds:
  - `n(L)` counts it negative below `−tol_L = −10⁻⁹ max(1, |σ − λ₀,min|)`, about `−3.4×10⁻⁸` at `ε = 34`;
  - `n(B|G_tol)` reads the cluster's restricted form against `10⁻⁹` of that form's own largest eigenvalue.
- **The result.** Between `ε ≈ 33.93` and about 34.0, the instrument gives `n(L) = 0` and `n(B|G_tol) = 2`: a genuine index of −2, which no Krein count balances.
  - The locator's final interval, `[33.916, 33.942]`, has `n(L)` changing and `n(B|G_tol)` not.
  - So its bookkeeping failed: Unresolved (index bookkeeping).
  - The frozen point also ran its fast-spectrum search at the two unbalanced points it evaluated, about 3 hours each at level 3.
- **Level 2.** The slope is steeper, both counts change inside one final interval, and R1 passed there.
- **The rest.** Every other expectation of R1 holds at both levels. R2, R3, R4 (C3 and C2a), R4b and R5 pass, each arm caught.

**The changes.**
1. **A step is read between balanced ends.**
   - If an end of a step's final interval does not balance its slow Krein count, its reading end moves outward to the nearest evaluated point on that side that does balance and has the same `(n(L), n_S)`.
   - The crossing set, the identity, the classes, the bookkeeping and the root are read between the reading ends. The final interval is reported with them.
   - With no such point, the step is read at its final interval, as before.
2. **The fast-spectrum search runs only where a verdict is read.**
   - It runs at the offset guards, with the full frozen point.
   - Grid points, bisection midpoints and the guard region's ladder points are read with the frozen point data, the slow spectrum, as the terms list it. The search is not run there, and its skipping is recorded.
   - A region end's verdict is the ladder's own, which ran it.
3. **A new synthetic test, S18.**
   - **The plant:** S2's structural crossing, with `n(B|G_tol)` falling 0.01 later in `ε` than `n(L)`, so that the points between are unbalanced.
   - **Expected:** one structural step per level, read across the window (`Δn(L) = Δn_S = −2`, a genuine change of 0), and "no genuine crossing detected".
   - **Its arm:** the step read at its final interval's ends. It is then Unresolved (index bookkeeping).

**The reruns:** every test, on the final code: S1 to S18, R1 to R5, and R4b.

## Amendment (2026-10-10T16:12:12Z): the reading end fails closed, after both units' review of the results

Both review units gave GO after fixes on `RESULT_4.md` v1. This amendment carries their one blocking fix and the record changes they asked for. No threshold changes. Every test is rerun once on the final code.

1. **The reading end fails closed.** Amendment 4's rule had two openings:
   - its search stepped past a point that failed its checks (a review unit's finding);
   - with no balanced point found, it kept the unbalanced end, and the step could still be classified (the other unit's).

   The rule now reads as follows. An end whose slow Krein count does not balance moves outward, point by evaluated point:
   - **It stops at the first point** that fails its checks, or whose `(n(L), n_S)` differs.
   - **It takes the first point** that passes its checks, has the same counts and balances.
   - **If none is found, the step is Unresolved (no balanced reading end).** It is never classified from an unbalanced end.

   This can only turn a classified step into an Unresolved one. The registered text of amendment 4 also left out "passes the point checks", which the terms and the code include. It is now stated.
2. **S9's plant reaches the bookkeeping check.**
   - Under item 1, S9's plant as registered, `n(B|G_tol)` off by one above the root, leaves its upper ends unbalanced. It would stop at "no balanced reading end".
   - So S9 now plants the inconsistency where the ends still balance: two genuine eigenvalues of `L` cross, but the Hamiltonian genuine set gains only one real pair, the other staying imaginary with Krein sign +. `n(B|G_tol)` is planted so that the count balances.
   - The genuine change is then +1, against a signed crossing count of 2: index bookkeeping, as registered.
   - **Its arm:** both pairs become real. The step is then genuine, and the result located.
3. **Two new tests:**
   - **S18b.** S18's window, with a point inside it that fails the structural subspace check.
     - Expected: the move stops there, and the step is Unresolved (no balanced reading end).
     - Arm: the search skips failed points. It then reaches the balanced point beyond, and the step reads structural.
   - **S18c.** S2's structural crossing, with `n(B|G_tol)` one too high at every point, so that no point balances.
     - Expected: Unresolved (no balanced reading end).
     - Arm: the fallback to the unbalanced end. The step is then classified structural, which is the opening item 1 closes.
4. **The record names three things separately:**
   - **the final interval,** where the count changes;
   - **the reading interval,** between the balanced reading ends;
   - **the root,** the interpolated zero, an estimate read from the reading interval.

   The root carries no `10⁻³` guarantee of position. It is kept inside the reading interval. Each crossing's unclamped zero, and whether the clamp applied, are recorded.
5. **Each point's fast-spectrum search is recorded in one of three states:**
   - **not needed:** the slow count balances;
   - **skipped:** it does not balance, at a point where only counts are read;
   - **run:** it does not balance, at a full frozen point.

   The full frozen point is built on the rerun ladder, at the offset guards, and for the same-`ε` diagnostic. Every unbalanced evaluated point between a step's readings is listed beside its collisions.
6. **Two reasons are added to the terms' list:** "no balanced reading end", and "genuine and structural crossings in one step".

**The reruns:** S1 to S18c, R1 to R5 and R4b, once, on the final code.

## Note (2026-10-10T16:13:38Z): S18b's plant, before any code or run

The reading-end rule only meets points the bisection kept: grid points, and the guard region's ladder points.
- A single failing grid point inside S18b's window would be the midpoint of the merged sub-interval around it, so the bisection would stop there first.
- So S18b plants the window over two consecutive grid points that both fail the structural subspace check: the structural crossing at 0.9237, `n(B|G_tol)` lagging by 0.15, and the failures at the grid points 0.95 and 1.0.
- **Expected,** as registered: the reading end's search stops at 0.95, and the step is Unresolved (no balanced reading end).
- **The arm:** the search skips the failed points. It then reaches the first balanced point beyond the window, and the step reads structural.

## Note (2026-10-10T23:41:02Z): S18b's fixture as it ran

**What changed, and when.** S18b's plant tilts the exact zero's eigenvector out of `P` at the failing grid points 0.95 and 1.0, at both levels. An unrecorded plumbing pass, before the final run, showed the tilt has to fall there:
- **Tilting a negative lift,** as first written, also changes `n_S` at those points. The search would then stop on a change of counts, and the arm could not tell the rules apart.
- **The exact zero is nonnegative.** Tilting it fails the same structural subspace check and leaves `n_S` unchanged.

**What ran.** The final run used this fixture: S18b passed and its arm was caught. Both review units confirmed the trace.

## Note (2026-10-11T00:15:57Z): the point record carries the frozen point data

**What changes.** The point record now carries the frozen point's own record beside the locator's fields, at every evaluated point:
- the cluster, the slow spectrum with Krein signs and the counts, as the frozen driver records them;
- where the fast-spectrum search ran, what it found and its counts;
- where it did not run, no search result. Where it was skipped, the stand-in that replaces it returns nothing, and that output is not a search result.

**Why.** The terms report the frozen point data at every evaluated point (`TARGET1_TERMS.md`, § Reported; step 2 defines the data). The locator's record carried only `n(L)`, `n(B|G_tol)` and `k_c` of it, and no search result. The gap was found before the freeze, in the review of the fast-spectrum search's two real-axis shifts: the claim ceiling that draft v7 of the terms adds is read from the record, and an independent check of a reading needs what the search found.

**What it changes.** The record only. No check, decision, threshold or expected outcome changes. The code's references to the terms move from draft v6 to v7. Every test is rerun on the fixed code before the freeze, and the earlier records are kept in `out/run3_2026-10-10/`.
