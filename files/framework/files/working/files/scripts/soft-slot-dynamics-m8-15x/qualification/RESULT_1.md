# M8.15.x: § 1's controls, results

Each was registered in `REGISTER_1.md` before it ran.

## 1a: the stopping test, off the critical angle (run 2026-10-08T21:01Z)

The harness is `control_1a.py`, and its record is `control_1a.json` and `control_1a.log`. The case, level and seed solve are as registered: `P5a` in R4 at level 2, through `Branch.first` at `ε_min`. The frozen arm read 19 files, checked byte for byte against `6058f95` when the harness started.

**All seven registered checks pass.**
- **The old form stalls.**
  - It sits at `5.3836×10⁻⁵` from iteration 2 through 39, never below `10⁻¹¹`, and the frozen seed solve ends in a Newton failure.
  - That plateau is `5.4×10⁶` times the tolerance.
  - It equals `|μ| ‖M p₀‖ / ‖M x‖` to `5×10⁻¹¹` relative.
- **The new form passes,** at iteration 3, at `9.6×10⁻¹³`. Both arms reach `σ = 48.27504835508736`.
- **The multipliers.**
  - `ν = −1.6230×10⁻⁴`.
  - `μ = 5.3830×10⁻⁵`, which matches `−ν ⟨p, s⟩_M / ⟨p, p₀⟩_M` to `7×10⁻¹¹` relative.
  - The frozen arm's `μ` agrees with the bench's to `2.4×10⁻¹⁰`.
- **Every check can fail.** Ten mutation arms each push one check just past its threshold, and each is caught by that check alone (`control_1a_mutations.log`).

**Not registered: the new test's floor** (`control_1a_floor.py`). At the converged point, the full residual of `9.6×10⁻¹³` splits in two:
- `1.3×10⁻¹³` lies inside the fixed space, which is what Newton solves;
- `9.5×10⁻¹³` lies outside it, where Newton cannot reach. Of that, `8.5×10⁻¹³` is `ν` times the slice vector's own part outside the fixed space, which is `2.5×10⁻⁹` of `M s`. The rest is round-off.

So the floor grows with the slice force. It would reach the tolerance at a slice term of about `4×10⁻³`, twelve times this one. At § 1b's critical points `ν → 0` and the floor goes with it, but § 1b's grid solves run off the critical angle, as 1a does.

**For a decision before § 1b's code.** Project the slice into the fixed space where it is built (`LevelCase` in `m815_common.py`), and keep the test on the full residual.
- **Effect:** the floor falls to round-off for any slice force.
- **Scope:** it touches only the slice cases (C3s, T4 and the pyramid). None of them is a closing control, so the regression set is unchanged.
- **Registration:** `REGISTER_1.md` names the frozen slice for 1b, so the change would enter as a dated amendment before 1b runs.

Testing only the part inside the fixed space would also remove the floor, but the test would then no longer see anything outside it.

## 1a, rerun under the amendment (run 2026-10-08T22:03Z)

The amendment of 22:00:59Z in `REGISTER_1.md` projects the slice covector `M s` into the fixed space Newton solves in, with Newton's own basis: `Ŝ = B_r B_rᵀ M s`. The harness is `control_1a_amended.py`, and its record is `control_1a_amended.json` and `control_1a_amended.log`.

**All registered checks pass: 1a's seven again, and the amendment's seven.**
- **The floor** is `4.35×10⁻¹³`, against `9.61×10⁻¹³` before and the registered bound of `6×10⁻¹³`.
  - At the converged point, `1.32×10⁻¹³` lies inside the fixed space and `4.14×10⁻¹³` outside it, which is round-off.
  - The `ν` term outside is `1.6×10⁻¹⁹`, against `8.5×10⁻¹³` before. So the floor no longer depends on `ν`.
- **The covector.** `B_rᵀ Ŝ` equals `B_rᵀ M s` to `4.3×10⁻¹⁶`. `Ŝ` lies `4.6×10⁻¹⁶` outside the fixed space, against `2.5×10⁻⁹` for `M s`.
- **The converged point is unchanged,** still at iteration 3.
  - Against the 21:01Z run, `σ` agrees to `1.5×10⁻¹⁶`, `ν` to `5.8×10⁻¹²` and `μ` to `1.9×10⁻¹⁰`.
  - `μ` is about 10⁶ times smaller than `σ`, so round-off is that much larger relative to it.
- **Every check can fail.** Seventeen mutation arms are each caught by their own check alone:
  - the unprojected run, for the floor and the covector;
  - a projection missing one basis column;
  - threshold moves;
  - 1a's ten arms, on the new record.

**Not registered.** The frozen arm reproduced the 21:01Z record exactly, iteration by iteration.

**Wording.** The 1a section above recommended projecting "the slice". The amendment projects the slice covector `M s` into the fixed solve space instead, which leaves the reduced problem unchanged.

## 1b: the angle solve on the pyramid's circle (run finished 2026-10-08T23:30:14Z)

The registration is `REGISTER_1.md`'s amendment of 22:09:19Z, written before any of § 1b's code. The code is `solver/m8_15_solver/angle.py`, and the harness is `control_1b.py`. The record is `control_1b.json` and `control_1b.log`, with the two reference series in `control_1b_ref_sel.npy` and `control_1b_ref_off.npy`. The case is `P5` in R4 at level 2, at the seed norm of `ε_min`, with the grid started at `π/10`.

**All six registered checks pass, and nine mutation arms are each caught by their own check alone.**
1. **Where it lands.** The circle has two critical points per period, at `π/5` and `2π/5 ≡ 0`, within `2.4×10⁻¹²` and `5.4×10⁻¹²` of them.
2. **The multipliers.** At the selected minimum, `ν = −4.9×10⁻¹⁶` and `μ = 8.5×10⁻¹⁵`.
3. **Both tests pass there.**
   - The frozen solver at `6058f95`, from the seed at the selected angle, passes its own test at iteration 3, at `3.9×10⁻¹³`.
   - The bench solver passes the new one, at `3.9×10⁻¹³`.
4. **The selection is `π/5`.** Its energy is `1.16×10⁻⁵` below that of `0`, which is the circle's maximum. So the oriented seed's own angle is the maximum here, not the minimum.
5. **The symmetry rule.** Over two periods the minimum is found at `π/5` and `3π/5`. The two copies overlap to round-off, and they are counted once.
6. **The reference run.** At the selected point, `d_ref` stays below `1.6×10⁻¹²` over the whole run, against `η = 10⁻³`.
   - The observation times are M8.15's: every 122 steps to `t = 999.77`, integrating to `T_int = 1000.002`.
   - The charge drifts by `7.5×10⁻¹⁴`.

The grid's energies are mirror-symmetric about `π/5` to the last printed digit, so the discrete reflection symmetry that fixes the critical angles is exact.

**Not registered: the drift § 1b removes.** At 1a's off-critical angle, the same reference run passes `η` at `t = 41.9` and reaches `6.6×10⁻²` by `T`. That point's slice force is `ν = −1.62×10⁻⁴`. So the off-critical reference drifts out of the band within a twentieth of the run, while the critical one holds to `10⁻¹²`.

## The carry: the angle along a branch (run finished 2026-10-09T00:13:25Z)

The registration is `REGISTER_1.md`'s amendment of 23:57:20Z, written before any of the carry's code.
- **The code:** `carry_solve`, `track_others` and `AngleBranch`, added to `solver/m8_15_solver/angle.py`. `solve_pinned` gained a reference argument.
- **The harness:** `control_carry.py`. The record is `control_carry.json` and `control_carry.log`.
- **The regression gate,** `regress_carry_edit.py`, was run before the tests. Control 1a's bench arm reproduced its record exactly, and so did control 1b's angle solve, apart from the one field the carry added, `maximum`.

**All ten registered checks pass, and sixteen mutation arms are each caught by their own check alone.**
- **Synthetic 1, a root faster than the bracket.** At `1.5 w` per step the root is carried by the fallback at every step, to round-off. At `2.5 w` the branch ends "lost" at `ε = 1`.
- **Synthetic 2, annihilation.** The minimum is carried to `−arcsin ε` through `ε = 0.9`. The branch ends "lost" at `1.05`.
- **Synthetic 3, exchange.** The selected minimum stays at `π` throughout. "No longer the lowest minimum" is recorded once, at `ε = 0.1`, and nothing is re-selected.
- **Synthetic 4, a kind flip.** The branch ends "the carried root is not a minimum" at `ε = 1.2`.
- **Pyramid 1, past the basin.** The kick at the third ladder step, toward `ε = 0.5`, starts the carry `0.05 P` from the maximum. The local solve finds the maximum, at `4×10⁻¹²` from `0`, and the branch ends "the carried root is not a minimum". All five accepted points lie at `π/5`.
- **Pyramid 2, the moving coordinate.** At all fifteen accepted points the coordinate lies at `π/5 − δ_k` and the physical angle at `π/5`, within `10⁻⁷`.
  - `|ν| ≤ 3×10⁻¹⁵` and `|μ| ≤ 1.1×10⁻¹⁴`.
  - No fallback was used, and the branch reached `ε = 2`.
- **Pyramid 3, both critical points.** At all seven ladder points the minimum lies at `π/5` and the maximum at `0`. The minimum stays below the maximum throughout, so no swap occurred. The gap between them grows from `1.16×10⁻⁵` at `ε_min` to `1.00×10⁻⁴` at `ε = 2`.

**Cost.** A carry solve takes about eleven Newton solves. Arm 2's ladder to `ε = 2` took 163 solves and 165 s at level 2.

**A limit found while building the tests.** A root that falls on a grid point, to round-off, cannot be classified by the rule's interval test, since its `H` equals that at an interval end.
- **The synthetic first grids** therefore start at `0.05`, off every root. That is a harness choice.
- **On the pyramid,** with the targets' default `θ_start = 0`, both of its critical angles would be grid points. That is why control 1b started at `π/10`. T4's roots are generic, so the limit does not bite there.
- **A remedy, if wanted before T4:** classify by `ν`'s sign pattern across the root instead. It would need its own amendment.

## The kind from ν's sign, and the carry's record (run finished 2026-10-09T00:51:56Z)

The registration is `REGISTER_1.md`'s amendment of 00:42:42Z, written before its code.
- **The code:** `kind_of` in `angle.py`, used by the full rule and by the carry.
- **The harness:** `control_kind.py`. Its record is `control_kind.json` and `control_kind.log`.
- **The carry's tests reran as `control_carry_kind.*`,** so the first run's record stands as it was.

**All seven registered checks pass, and ten mutation arms are each caught by their own check alone.**
- **(a) The pyramid's full rule at `θ_start = 0`,** where both critical angles are grid points.
  - It finds `0` as a maximum and `π/5` as a minimum, each once, and selects `π/5`.
  - Its `H` matches control 1b's selected point to `10⁻¹⁶` relative.
  - The `H`-only rule, on the same samples, classifies neither root.
- **(b) Synthetic `−cos θ` with its grid from `0`:** a minimum at `0` and a maximum at `π`, each once.
- **(c) A flipped sign convention on control 1b's grid** leaves both roots unresolved. Without the `H` cross-check it would have classified them reversed.
- **(d) Regression.**
  - § 1b's angle solve reproduces control 1b's roots, kinds and selection, over one period and over two.
  - The carry's ten checks pass again, with the same ends. The physical angles move by at most `3×10⁻¹⁰`, from Brent stopping at the bar.
- **(e) A kicked carry inside `goto`** returns no point, records "the carried root is not a minimum", and leaves the accepted points unchanged.
- **(f) Pyramid arm 1's end** records a trial norm of `0.0696`, above the last accepted `0.0492`.

**The saving from stopping Brent at the bar:** the Newton solves fell from 64, 163 and 207 to 41, 82 and 86 in the three pyramid arms.

This closes § 1 on the bench. The limit recorded in the carry's section above is resolved.
