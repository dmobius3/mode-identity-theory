# M8.15.x: Target 1's locator, its test results (final run finished 2026-10-11T05:00Z)

**Status:** v3. v2 folded both review units' review of v1. v3 carries the record fix and its rerun, after the units' review of the fast-spectrum defect, where both gave GO after fixes.

**The outcome.** The locator passes every registered test on its final code, and every arm is caught:
- S1 to S18c, on the mock evaluator: 20 tests;
- R1 to R5 and R4b, on the real solver, for orbits that are not targets.

Every record was made by the code as it now stands.

**What changed since v2.**
- **The fast-spectrum search.** A defect in the inherited search, at its two real shifts, was traced from the first run's log and reviewed. It is disclosed and not repaired, and the terms add a ceiling: no positive result rests on the search (`TARGET1_TERMS.md` v7, § Standing and § Naming).
- **The record fix.** The point record now carries the frozen point data the terms report, with a search result only where the search ran. It entered as a dated note, and it changes the record only.
- **The rerun.** Every test was rerun on the fixed code. Two bench checks confirm that the fix changed nothing else, and that every point carries its own frozen record.

**Two instrument facts surfaced.**
- The frozen instrument reads `n(L)` and `n(B|G_tol)` against different thresholds.
- The fast-spectrum search's two real shifts are not valid shift-invert steps (terms v7, § Standing).

**The registration** is `REGISTER_4.md` v3, registered 2026-10-09T21:58:26Z, before any locator code. Its five dated amendments and three notes:
1. **S8 restated,** before any code. A plant it named was geometrically impossible.
2. **A step's root interpolated,** before any recorded test.
3. **S1's arm,** which follows from 2.
4. **A step read between balanced ends, and the fast-spectrum search confined,** with S18. This came after R1 failed at level 3 in the first run.
5. **The reading end fails closed,** after the units' review of v1. With it:
   - S9 is re-planted so that its ends balance;
   - S18b and S18c are added;
   - the record changes are made.
   - **Two notes on S18b:** its plant needs two failing grid points, not one; and its fixture as it ran tilts the exact zero.
6. **A note on the point record** (2026-10-11T00:15:57Z): it carries the frozen point data. No check, decision or expected outcome changes.

**The code** is on the bench, in the locator's folder: `locate.py`, `t1_branch.py`, `tests/mock.py`, `tests/synthetic.py` and `tests/real.py`.
- It reads the frozen instrument at MIT `97a8c08` without changing it. Every run checks the instrument's files against its manifest, whose SHA-256 is recorded and matches the freeze's.
- `decide` is extracted from the frozen `m815_branch.py` through its syntax tree, and the SHA-256 of its source is in every record.
- Every driver record carries the SHA-256 of `locate.py` and `t1_branch.py`, and each matches the code as it stands.

**The records** are in the locator's `out/`:
- `synthetic.json` and `.log`;
- `r4b.json` and `r5.json`;
- the driver's records `t1_*.json`, with `run_*.log`;
- `real.json` and `.log`, and `chain.log`.

The earlier runs are kept:
- `out/run1_2026-10-09/` holds the first real-solver run, in which R1 failed at level 3;
- `out/run2_2026-10-10/` holds the second, on the code before amendment 5;
- `out/run3_2026-10-10/` holds the third, on the code before the record fix.

**The bench checks** are `compare_run3.py` and `record_frozen_check.py`, beside this page, with their outputs.

## The results (the final run, on the final code)

| Test | Outcome |
|---|---|
| S1 to S18c | 20 of 20 pass, each arm caught. |
| R1, C2a/R4 | Pass, arm caught. A structural step at each level, with `Δn(L) = Δn_S = −2` and a genuine change of 0. Named "no genuine crossing detected" at both levels. |
| R2, C3/R4 | Pass, arm caught. No step at either level over 11.31 to 16. `n(L) = 9` at all 9 points per level. |
| R3 | Pass, arm caught. The forced failure at the first level-2 midpoint, `ε = 14.536`, is recorded with all three failed attempts. Their residuals are `6.5×10⁻³`, `3.2×10⁻³` and `1.6×10⁻³`, the frozen half- and quarter-step retries included. The step is reported over `[14.243, 14.828]`, and the run exits normally. |
| R4, C3 and C2a | Pass. The driver's ladder and the extracted `decide` reproduce the qualification's branch records bit for bit: every type and reason, the cross-level records, and every point's data at both levels. The arm, `dlev = 0`, makes every C3 point Unresolved (level stability). |
| R4b | Pass. Each of the nine Unresolved reasons fires alone, and the two passing pairs read Elliptic and Hyperbolic. Each binding's arm is caught. |
| R5 | Pass. The guard refuses a target in each of its four cases, and passes when everything matches. The arm is caught. The real instrument folder was never written: its `SHA256SUMS` passes 24 of 24, and it holds no `FROZEN.json`. |

**R1's step, with the three quantities named separately:**

| Level | Final interval (the count changes) | Reading interval | Root (estimate) | Clamped |
|---|---|---|---|---|
| 3 | 33.916 to 33.942 | 33.916 to 34.071 | 34.042 | no |
| 2 | 14.243 to 14.252 | the same | 14.252 | yes: the unclamped zero is 14.2526 |

**Reading the table.**
- **Level 3.** The upper end, 33.942, lies in the window where the two counts disagree. So it reads at the first balanced point beyond, 34.071, and the root lies outside the final interval.
- **Level 2.** The zero lies `7.7×10⁻⁴` above the reading interval, within the terms' bound of `tol_L/|slope|`.

**The fast-spectrum search, per point.**
- C2a at level 3: 16 points "not needed" and 2 "skipped", the two points inside the window.
- C2a at level 2, and C3 at both levels: every point "not needed".
- Nothing ran it there. The ladder's full points balanced.

**The span gate.**
- **C2a.** `σ₃/σ₁` is 0.3587 to 0.3588 at both levels, against the frozen frame's continuum value of 0.3587. The mesh residual `σ₄/σ₁` is `6.9×10⁻³` at level 2 and `1.7×10⁻³` at level 3.
- **C3.** 1.0.
- **The other point checks.** Coverage and the structural subspace pass at every evaluated point of R1 and R2.

## The record fix, checked

- **The rerun equals run 3** (`compare_run3.py`). Every driver record equals its run-3 counterpart value for value, once three things are set aside: the new field in each point record, the start and finish times, and the locator's SHA-256. The top-level block of frozen values is compared. The synthetic log matches line for line after its time stamp. Two arms are caught: a number in a point record perturbed, and the top-level `r_f3` changed to 99.0.
  - The script's first version set aside every field named `frozen`, the top-level block of frozen values included. The review found it. The script now sets aside the point field only, and the second arm tests that.
- **Every point carries its own frozen record** (`record_frozen_check.py`). There are 93 points: 91 "not needed" and 2 "skipped".
  - Each frozen record agrees with the locator's `n(L)`, `n(B|G_tol)`, `k_c` and balance.
  - It carries a search result exactly where the search ran.
  - Three record arms are caught.
  - No control reaches a full point that does not balance, so no record holds the state "run". The code path is checked on stub points in all three states, and a copy of `locate.py` without the line that drops the stand-in's output is caught.

## How the tests got here

**The first run, R1's failure.**
- **The cause.** In the frozen instrument, `n(L)` counts an eigenvalue negative below `−10⁻⁹ max(1, |σ − λ₀,min|)`, about `−3.4×10⁻⁸` at `ε = 34`. `n(B|G_tol)` reads the cluster's form against `10⁻⁹` of its own largest eigenvalue.
- **What it did to C2a at level 3.** Its doubled structural eigenvalue rises through zero slowly, so between `ε ≈ 33.93` and about 34.0 the two counts disagree, by a genuine index of −2. No Krein count balances that.
  - The locator's step saw `n(L)` change and `n(B|G_tol)` not, so its bookkeeping failed.
  - The frozen point ran its 3-hour fast-spectrum search at the two unbalanced points. The run took 8 h.
- **Level 2** passed, and every other test passed.
- **The fix** was amendment 4: reading ends that balance, and the search confined to verdicts, with S18.

**The second run** passed every test.
- The units' review then found the reading end failing open in two ways: it stepped past a failed point, and it kept an unbalanced end when no balanced one was found.
- Amendment 5 closes both. An unbalanced step is now Unresolved (no balanced reading end), never classified.

**S18b's fixture,** found by an unrecorded plumbing pass before the third run.
- Tilting a negative lift out of `P` also changes `n_S` at the failing points. The search would then stop there on a change of counts, so the arm could not tell the rules apart.
- The plant therefore tilts the exact zero's eigenvector instead. That fails the same check, the structural subspace, and leaves `n_S` unchanged.

**The third run** passed every test. The units' review of the fast-spectrum defect then led to two changes:
- the ceiling, in the terms;
- the record fix, found while checking that the ceiling can be read from the record.

**The fourth run,** this one, on the fixed code. A session restart stopped it once, during C3 and before C3 wrote anything. C3 and C2a were then run in full.

**The instrument facts, for the record.**
- **The two thresholds** differ in the frozen instrument. A point is affected only where a near-zero eigenvalue lies between them. No frozen file changes, and the locator reads around such windows.
- **The fast-spectrum defect** has run only in the first run, at the two C2a points inside the window, before the search was confined. That run recorded no search result.

**For Target 1.** T3/R5's level-3 bracket holds a structural step that may meet such a window.
- **The structural step** is read across the window, without a 3-hour search at each point inside it.
- **A guard inside a window** runs the search, about 3 hours at level 3, reads Unresolved, and does not count.
- **A genuine step whose end lies in a window** reads Unresolved, and that result stands (terms v7).

## What is not covered

- **No real-solver test has a genuine crossing,** because no non-target control has one. The genuine-crossing logic and the matched-offset reading are tested on the mock evaluator only.
- **The guard readings on real data** are exercised through R4 and R4b, through the same frozen `decide` the guards call.
- **The point record's "run" state** is checked on stub points only.

## Next

1. **The locator's freeze,** in a folder of its own on MIT main, with its manifest and `SHA256SUMS`. It is built locally and shown to the maintainer before any push.
2. **The terms go to OpenWave,** as M8.15's did, and their SHA-256 lands on MIT main.
3. **Then:**
   - the instrument's `REPRODUCE.md` note, its check's exclusion of `out/FROZEN.json`, and a new `SHA256SUMS`;
   - the maintainer's go, and `FROZEN.json`;
   - T2/R4, then T3/R5.

*v1 written 2026-10-10T14:04Z; v2 2026-10-10T19:35Z, after the final run; v3 2026-10-11T05:03Z, after the rerun on the fixed record.*
