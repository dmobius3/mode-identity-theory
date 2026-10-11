# M8.15.x: control 2a, results (run finished 2026-10-09T04:54Z)

**Status:** closed under option (a), v2. It folds both review units' redlines of v1, and both units agree on (a).

**The registration** is `REGISTER_2.md` v2, registered at 01:21:48Z, before any of 2a's code.

**The code:**
- `cluster_rule.py`;
- the verdict's reclassify step. Its regression gate (`regress_verdict_refactor.log`) reproduced two reference records exactly;
- `control_2a.py`.

**The records:**
- `control_2a_L3.json` and `.log`: level 3, 18 ladder points, 2.9 h;
- `control_2a_L2.json` and `.log`: level 2, 18 points, 5 min;
- `control_2a.json` and `.log`: the evaluation.

The records stand as written. Where this page reads them differently from the evaluator's printed labels, it says so.

**Before the run,** the synthetic classifier tests passed 7 of 7, with 9 mutation arms (`control_2a_synthetic.log`). A plumbing pass, unrecorded, found that a pair's basis could pick up a round-off direction. Blocks were then held to the registered dimensions before the run.

## The verdict: 2a fails as registered

The candidate rule never anchored the in-span mode.
- **Where:** at its first resolved point, level 3 at `ε_min`, no Krein-negative imaginary pair exists. There, the in-span mode and the paired lift form a quartet.
- **Why that is final:** the anchor is a single attempt (§ 3.3), so the in-span block stays unanchored for the whole run.
- **What it tests:** 2a qualifies the instrument's rule, not the small-amplitude theorem. The rule failed to identify a mode, and that says nothing against the mode's predicted existence.

**The checks:**
1. **FAIL as registered.**
   - The check names the in-span block at level 3 and `ε_min`, where the mode has no block of its own. It is half of a quartet with the paired lift, which `G_tol` takes whole, giving dimension 8 against 6.
   - The evaluator found no block to name, since it identifies the block through the candidate rule's anchor.
   - From `ε = 0.354`, where the pair separates, the 0.9 rule takes the in-span pair into `G_tol` at every level-3 point. That is recorded evidence for memo § 2's first claim, read outside the registered point.
2. **PASS.** Both levels reach `ε = 72`, the selected angle stays at `π/5` throughout, and the slice force stays below `10⁻¹²`.
3. **FAIL.** The quartet anchored at 8.1% and the Krein+ pair at 0.15%. The in-span mode did not anchor at all.
4. **FAIL,** as a consequence of 3.
5. **FAIL,** as a consequence of 3: there is no in-span block to identify.
6. **FAIL.** The candidate rule's dimension is 8 at level 3, and 10 from `ε = 16`. At level 2 it is 12 throughout.
7. **FAIL.** The count balances, but with `[k_r, k_c, k_i⁻] = [0, 1, 0]`.
8. **Vacuous.** The evaluator printed PASS, but the veto never applied: no point had the frozen dimension at both levels, and its mutation arm had nothing to act on. It is not counted as qualifying the veto.
9. **Holds, but carries no information.** The cross-level check reads "class counts differ" at all 18 points, including those above `5.66`. It is not counted as qualifying the cross-level check.

**The readings.** § 4.3's three anchor-error outcomes do not apply, because there was no in-span block to measure. Validity at `ε_min` fails for the same reason.

**The mutation arms.** Those of checks 2 and 9 are caught. The others cannot be read:
- checks 1 and 3 to 7 have failing parents, and a mutation arm needs a green parent;
- check 8's arm has nothing to act on.

**The point verdicts.** Under both rules, every point at both levels reads Unresolved, for two reasons:
- the cluster dimension is wrong: 8 under the 0.9 rule; 8, 10 or 12 under the candidate;
- the paired lift lies above `τ₀`, the reason `REGISTER_1.md`'s paired-lift item names.

## Why: the paired lift

**The in-span pair and the lifts at level 3,** in the solver's units of `λ`, against `τ₀⁽³⁾ = 1.04×10⁻⁵`:

| `ε` | Predicted in-span `|λ|` | Computed in-span | Ratio | Paired lift | Radical lift |
|---|---|---|---|---|---|
| 0.25 | 2.37×10⁻⁴ | merged with the paired lift: a quartet at 1.34×10⁻⁴ | | | 1.64×10⁻⁴ |
| 0.354 | 3.35×10⁻⁴ | 2.14×10⁻⁴ | 0.639 | 1.18×10⁻⁴ | 1.95×10⁻⁴ |
| 0.5 | 4.74×10⁻⁴ | 3.75×10⁻⁴ | 0.790 | 9.50×10⁻⁵ | 2.31×10⁻⁴ |
| 1 | 9.48×10⁻⁴ | 8.52×10⁻⁴ | 0.899 | 8.20×10⁻⁵ | 3.25×10⁻⁴ |
| 1.414 | 1.34×10⁻³ | 1.24×10⁻³ | 0.921 | 7.90×10⁻⁵ | 3.85×10⁻⁴ |
| 2.828 | 2.68×10⁻³ | 2.50×10⁻³ | 0.934 | 7.54×10⁻⁵ | 5.37×10⁻⁴ |
| 5.657 | 5.36×10⁻³ | 4.88×10⁻³ | 0.910 | 7.61×10⁻⁵ | 7.44×10⁻⁴ |
| 11.31 | 1.07×10⁻² | 9.07×10⁻³ | 0.845 | 8.92×10⁻⁵ | 1.02×10⁻³ |
| 16 | 1.52×10⁻² | 1.20×10⁻² | 0.793 | 1.06×10⁻⁴ | 1.17×10⁻³ |
| 72 | 6.82×10⁻² | 2.84×10⁻² | 0.416 | 2.83×10⁻⁴ | 1.91×10⁻³ |

**How the columns were identified.**
- The in-span column is the Krein− imaginary pair nearest the predicted modulus. The paired-lift column is the Krein+ imaginary pair below half the predicted in-span modulus.
- The two blocks' planes lie 4.4° apart, so the identification rests on modulus and Krein sign, not on structure.
- **The logs' `paired lift / tau0` readout is not the lift.** It is the largest paired-kind block in `G`, and under the candidate rule `G` holds genuine blocks too. From `0.354` to `11.31` it reads the in-span pair, matching the table's in-span column. From `16` it reads the Krein− pair split off from the quartet. The table is the reading to use.

**What the table shows:**
- **The paired lift is far above the floor.** It sits at `7.5×10⁻⁵` to `1.2×10⁻⁴` wherever it is separate up to `ε = 16`, about 7 to 11 times `τ₀⁽³⁾`, and rises to `2.8×10⁻⁴` by `ε = 72`. It is roughly independent of `ε`, as a mesh effect would be.
- **So the resolution rule placed the anchor inside a collision.** The rule, `10 τ₀⁽³⁾ ≤ ε κ |τ|`, put the in-span mode's first resolved point at `ε_min`. There the mode lies within a factor of 2 of the lift: the two have collided into a quartet, and they separate at `0.354`.
- **Once separated,** the in-span pair lies 36% below leading order at `0.354` and 21% at `0.5`. It is within 10% only from `ε = 1.414` to `5.66`, where it lies 6.6 to 9.0% below and more than 15 times the lift. Beyond that, finite amplitude drives it further below, as C2a's genuine modes drift.
- **At level 2 the lifts are larger still.** At `ε = 5.66` the paired lift is `2.3×10⁻³` and the radical lift `3.4×10⁻³`, against an in-span pair of `2.7×10⁻³`, which is 50% below leading order. From level 2 to level 3 the paired lift shrinks about 30 times and the radical about 4.5 times.
- **The geometry was flagged before the run; the lift's size was missed.**
  - A review unit placed the in-span plane 4.4° from the paired lift's, with condition number 14.2. Both figures are reproduced here by an independent route (`verify_review_figures.py`).
  - But it took the lift to sit at `τ₀`, about 23 times below the mode. Measured, the lift sits at 7 to 11 `τ₀`, within a factor of 2 of the mode where the two meet, and the near-parallel pair collides.
  - The frozen `τ₀` could not see that.

## Two more findings

1. **A gap in the tracking rule (FIXABLE), recorded for the next revision.**
   - **What happened.** Between `ε = 11.3` and `16`, the genuine quartet splits into two imaginary pairs, a change of type under both rules. The rule carried the tracked quartet to the pair in band. The other genuine pair was out of band and fell into `G`, so level 3's candidate dimension rises from 8 to 10 at `ε = 16`.
   - **The defect.** A tracked block can be carried to a candidate of smaller dimension. A 2-dimensional pair lying inside a tracked 4-dimensional quartet passes the principal-cosine test, since that test measures the smaller subspace inside the larger.
   - **Two fixes, neither implemented now:**
     - require a candidate to match the tracked block's dimension, so that a split or a merger reads Unresolved, as decision 2's "a merger or collision" does;
     - carry a block to the union of what it splits into, together with the mirror case, two pairs merging into a quartet. This changes decision 2, and it would need its own synthetic and non-target tests.
   - **The quartet track is one block throughout.** Its overlaps stay above 0.9997, with runner-ups below `10⁻⁹`, from `0.354` to `11.31`.
   - **Why its error is not monotone.**
     - The error is a complex distance, and the block's argument swings: from 51° at `ε_min` it falls to 6° at `ε = 4`, nearly a real pair, then returns to 74° at `11.31` before the split.
     - The prediction's argument is fixed at 56°.
     - So the error runs 9.7% at `0.354`, 22% at `1` and 76% at `4`, and falls back to 31% at `8`.
2. **The anchor and the tracking work on a clean mode.**
   - The Krein+ pair was anchored at both levels: 0.15% at level 3 and 0.21% at level 2, at `ε_min`. Level 2 anchored it through level 3, to 0.05%.
   - It was tracked to `ε = 72`, its drift from leading order growing to 48%, as C2a's did.

## What it means

1. **The memo's fallback applies.** Per memo v4 § 2, the candidate rule does not qualify on this control as registered. "If 2a cannot be found or armed, the new cluster rule does not qualify. The instrument then keeps the 0.9 rule, and T4 and T1 stay blocked. Target 1 can still run."
2. **The frozen `τ₀` declares the in-span mode resolved before it is spectrally separated from the paired lift.**
   - The candidate rule fails to anchor that mode, while the 0.9 rule places the merged cluster in `G_tol`.
   - Changing the threshold alone has not been shown to repair either classifier.
   - Until the floor is addressed, which is the memo's 2b question, T1 and T4 are gated under either cluster rule, and a § 2 retry would meet the same floor.
   - `REGISTER_1.md` registered that a lift above `τ₀` makes the pyramid a 2b candidate. It now has a measured lift at both levels and at every ladder point.
3. **For T4 (INFERRED).**
   - T4's smallest mode lies 8.2° from T4's paired-lift plane (cosines 0.998 and 0.990), with condition number 29.8, twice the pyramid's. These are a review unit's continuum figures, reproduced here by an independent route.
   - Its predicted `|λ|` at its first resolved point (`ε = 1.41`) is `1.2×10⁻⁴`, the same size as the pyramid's measured paired lift at level 3.
   - So if T4's lift is of the pyramid's size, the same collision would meet any rule there.
   - This stays INFERRED, because T4's own lift is unmeasured. It would change if that lift were measured well below T4's smallest mode.
4. **§ 3.4, the level-2 anchor through level 3, stays outside the qualified instrument.** Its reason, C2a's drift at `ε = 4` to `5.66`, stands for the next revision.
   - There, level 2's anchor should be harmonized with the cross-level check, which tests the same agreement at a tighter tolerance: 1% plus `s₂/ω₀`, against 10%.
   - Late theorem anchors at level 3 share the drift problem, T4's at `1.41` among them.
   - § 3.4 did not change this verdict: level 2 had no in-span track at level 3 to anchor through, and level 2's quartet lay 87% from level 3's.

## The decision: option (a), agreed by both review units

- **Close 2a as failed,** keep the 0.9 rule, and go on to qualification (§ 6). Then Target 1 runs under the 0.9 rule.
- **Target 1 does not depend on the failed replacement rule.** It can run under the retained 0.9 rule, with three safeguards:
  - structural overlaps checked at every bisection midpoint and guard offset;
  - the registered cross-level gates enforced;
  - the registered dynamical gates enforced.
- **Target 1's orbits sit clear of this mechanism.** These are a review unit's continuum figures, reproduced here by an independent route:
  - T2's slowest pair is doubled, and its planes lie about 50 to 54° from the rotations, with condition number 1.7;
  - T3's slow modes have no overlap with the rotations, with condition numbers 1.0 to 1.1;
  - compare the pyramid's 4.4° and 14.2.
- **2b is studied separately.** T4 and T1 stay blocked until it lands.
  - The pyramid's measured lifts can motivate a 2b proposal, but they cannot be its sole qualifying evidence.
  - One lead for scoping: the lift's size looks tied to how nearly parallel the genuine mode is to the lift's plane. That was noticed after this run, so it cannot be qualified on it.
