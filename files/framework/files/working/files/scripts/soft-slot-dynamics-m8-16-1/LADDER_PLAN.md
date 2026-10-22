# M8.16.1: amendment 5's ladder, `R5`'s coherent branch to `ε = 32`, a plan (2026-10-22; v2, the units' reviews of v1 folded)

Development step 4 (`DEVLOG.md` entry 1; `DRIVER_PLAN.md` v2, What the plan does not do). Both units reviewed v1, and their fixes are folded in here, each verified at source (`DEVLOG.md` entry 22). Nothing in this plan is built or run before both units' GO and Blake's word. The plan covers:
- amendment 5's text;
- the points and cutoffs;
- how the driver runs them;
- the claims stated before the run, and what each outcome means;
- the measured budget.

`dev/ladder_plan_facts.py` reads each fact it states again from source, with nothing solved (`DEVLOG.md` entry 20).

## Amendment 5, for `BOUNDARY.md`

The draft of this folder's `BOUNDARY.md` went to the units with v1. It does four things:
- it cites M8.16's `BOUNDARY.md` by SHA-256, `a54619de…` at `deec830` (fact 2), as the split the ruling carries over;
- it records Blake's decision of 2026-10-20, with both units' agreement, which `DEVLOG.md` entry 22 quotes from the scope check;
- it adds amendment 5 in M8.16's form: the decision, why it leaks nothing, and why it is needed;
- it gives the ladder amendment 3's note's reading, with one difference (UB, UA). No constant is refitted on it, since the calibration's constants are in `instrument/linear.py`, which the terms fix byte for byte. A failed calibration condition is disclosed, and preserved and returned to Blake and the units before further development. A refit would be a revised instrument, which needs a separate maintainer ruling on #512.

It is written into the folder, as the units leave it, before the ladder runs, and its time stamps are the time of that writing (UB). It is not edited after that first write.

## Which points

- **The grid.** `cases.R5_LADDER`, M8.15's grid to 32: `ε_k = 0.25 · 2^(k/2)` for `k = 0` to 14. That is 15 points, all read: 0.25, 0.354, 0.5, 0.707, 1, 1.41, 2, 2.83, 4, 5.66, 8, 11.3, 16, 22.6, 32. In the registered run, T2 and T3 in `R5` run along it (fact 1).
- **The sample.** Its four points are the grid's `k = 0, 2, 4` and 6 (fact 1).
- **Continuation,** as the driver runs it. At each `N`, the path starts from the germ at 0.25, and each point continues from the previous accepted one. Each cutoff runs on its own path from the seed.
- **The expected row at every point.** It is `EXPECTED_R5.md`'s, as `cases.py` holds it for C2a/R5:
  - `(k, r_u) = (3, 1)`;
  - `V₀` of dimension 4, ranks [1, 0], with 3 chains;
  - Elliptic, `(n(L), n(D), K) = (0, 0, 0)`;
  - five slow pairs at `εκsτ`, with `s = 9/16`, all Krein-positive.
- **Beyond the sample, the row is INFERRED.**
  - C2a's `R4` ladder kept the row at all 39 of its points to `ε = 72` (fact 8; M8.16's `DEVLOG.md` entry 106).
  - `R5`'s leading order is `R4`'s scaled by 9/16. Its corrections are not assumed to match `R4`'s.
  - A mismatch is reported, never re-expected.

## Which cutoffs

- `N = 16, 24` and 32, as amendment 5 sets them. No `N = 40`.
- The convergence rule reads each point from the three cutoffs. The identity guard compares `N = 24` and 32 at each point, as it does at the sample.

## How it runs: the driver's dry mode, and the changes it needs

`run/driver.py --dry`, on a dry list of one case, `C2a/R5:ladder`. Four changes, each small:
1. **`run/build_dry.py`** takes a list's name.
   - `plumbing`, the default, writes `DRY.json` byte for byte as now.
   - `ladder` writes amendment 5's list. Its one case is C2a/R5's serialized case, named `C2a/R5:ladder`, with the role `dryladder` and the points of `cases.R5_LADDER`, all read.
2. **`run/cases.py`:** a ladder case `X:ladder` is admitted under its base case `X`, and takes `X`'s representative, in `admission` and `serialize`. This replaces M8.16's special case for `C2a:ladder`, which no list names (fact 3). The rule is `seeds.base`, one function, which the driver reads too.
3. **`run/driver.py`:**
   - `run_case` seeds a ladder case from its base, in place of the same special case.
   - `checks_of` reads a `dryladder` case with `checks.check_control`, the `R5` control's K1 and K4. Today it reads K6 against M8.15's ladder record. M8.15's outputs hold no branch of C2a in `R5`, and `reference/m815/` holds no `R5` record (fact 4).
   - `load` refuses a dry case whose base is in `branches.SEALED` or `seeds.NEW`, whatever its admission field says (UB). Today its second test reads the full name against `branches.SEALED`, which matches neither a `:ladder` name nor either new seed.
   - The gate record and the verdict already leave the `dryladder` role out. The gate names the six gating cases absent, and the verdict reads incomplete.
4. **`run/score_ladder.py`,** new: the claims below, scored from the run's outputs. Its SHA-256 is logged before the run.

**What stays as it is.** `instrument/` does not change: `devtools.GO` already admits C2a/R5, under amendments 3 and 4 (fact 3). The outputs go to `run/dry/`, which holds only the plumbing pass's folder, and move to `dev/runs/` after the run.

**Before the run,** after the changes, everything that imports a changed file is run again:
- `test_guard.py`, with two new tests of the base-case rule (UB):
  - `C2a/R5:ladder` admitted in dry mode and seeded equal to C2a/R5's seed;
  - a dry list naming `P5:ladder`, `T2/R5:ladder`, `C3R/R4:ladder` or `T5J/R2:ladder` refused, by `load` and, with its admission field edited to a GO name, by the seed constructor;
- `test_verdicts.py`, and `score_record.py`, the record regression;
- `test_constants.py`, whose reverse scan must still pass, since the changes add no literal;
- `dev/seed_check.py`, which reads `run/seeds.py`, then `test_imports.py` on its new record;
- `build_dry.py plumbing`, which must reproduce `DRY.json` byte for byte.

## The claims, derived before the run

`run/score_ladder.py MIT_REPO` reads two inputs, each against the SHA-256 its run's log records:
- the ladder's outputs;
- the registered run's C2a/R5, from MIT at `87fc643`.

The claims:
1. **Acceptance.** At `N = 16, 24` and 32, the seed passes, and all 15 points are accepted. The secant reaches each target within 10⁻⁶, and every Newton step is accepted.
2. **The row, at every point and cutoff.**
   - K1 holds at every point: `V₀` as expected, the leak within its bound, 3 chains and the zero cluster separated.
   - `checks.k2` holds at every point to `ε = 2`, the sample's range, as at the registered sample (fact 9). The slow band then holds exactly the five predicted pairs, matched by class and Krein sign, with nothing in the gray zone. Beyond `ε = 2`, `k2` is reported, unscored (UB). Its band is twice the largest `εκsτ`, a measure made for small amplitude: on C2a's `R4` ladder, the slow modes sit at 0.99 of `εκsτ` at 0.25, 0.80 to 0.85 at 8, and 0.48 to 0.57 at 32 (`DEVLOG.md` entry 22).
   - The record reads Elliptic, (0, 0, 0), with nothing unresolved.
   - The convergence rule reads every `ε` converged, Elliptic.
3. **The calibration's conditions, as they stand,** at every point and cutoff. These are the conditions amendment 3's note names, as M8.16's `R5` sample scored them (its `DEVLOG.md` entry 202, claim 5):
   - (a) the cluster coefficient is at most `(κ/G)/10 = 1/15`;
   - (b) `L`'s kernel lift is at most `100 u ‖L‖`;
   - (c) `L`'s smallest genuine eigenvalue is at least `10⁵ u ‖L‖`.
4. **Theorem R's leading order, as the `R5` control's K4 reads it.** At `ε = 0.25`, every slow mode lies within 5%, and the largest deviation there is below that at `ε = 2`, at each `N`.
5. **The sample, against the registered run.**
   - At `ε = 0.25`, both runs take the same first step from the germ, on the same environment (fact 5). Each `N`'s point there equals the registered run's, field for field apart from its two timings. So do its convergence reading and its identity record. The plumbing pass's point at `N = 16` already does (fact 6).
   - At `ε = 0.5`, 1 and 2, reached along another path, the record's type, indices, `V₀`'s dimension and ranks, chains and Krein counts equal the registered run's.

**Reported, unscored:**
- the largest deviation from `εκsτ`, at every point and cutoff;
- each point's convergence reading: its smallest ratio and the band edge;
- the cluster coefficient, the lift and the smallest genuine eigenvalue, at every point;
- the leak, against its bound;
- the identity from `N = 24` to 32: the aligned distance, and whether the record is the same;
- at `ε = 0.5`, 1 and 2, the slow eigenvalues' relative differences from the registered run's;
- the seconds per point and per Newton evaluation, at each `N`.

## What each outcome means

- **All five hold.** `R5`'s acceptance and calibration hold along the grid to 32, as they stand. This is disclosed, and it changes nothing.
- **Claim 1 fails.** That cutoff's path ends at the failed point, as the driver's rule has it, and the solver's reason is recorded. T2 and T3 in `R5` run along this grid, so what follows for them is Blake's decision before the freeze, with the units.
- **Claim 2 fails at a point.** Either the row's extension fails there, or the instrument cannot resolve the point. It is reported, never re-expected.
- **Claim 3 fails.** The failure is preserved and returned to Blake and the units before further development (amendment 3's note, UA). No constant moves. No recalibration is available inside M8.16.1 (`BOUNDARY.md`, amendment 5). What follows for T2 and T3 in `R5` is Blake's decision before the freeze, with the units (UB).
- **Claim 4 or 5 fails (UA).** Preserve which comparison failed. At `ε = 0.25`, a difference from the registered record is a reproducibility or custody anomaly requiring investigation, since both runs take the same first step. At `ε = 0.5`, 1 or 2, a difference may arise from the changed continuation path and is not by itself a code defect. A failed K4 trend may also be a genuine reading of the ladder. Report the failure, its evidence and any proposed diagnosis to Blake and the units before a repair or rerun. No expectation or constant moves on that basis alone.

## The budget, from measured times

- **Rates,** from the registered run's C2a/R5 on this machine (fact 7):
  - per Newton evaluation: 0.3 s at `N = 16`, 6.2 to 6.4 s at 24, and 42.7 to 44.6 s at 32;
  - per record: 0.4 s, 6.8 to 7.0 s, and 54.7 to 58.1 s.
- **Counts,** from C2a's `R4` ladder on the same grid (fact 8): 4 to 12 evaluations per point, 129 in all at `N = 24` and 125 at 32. `R5`'s counts are not known in advance.
- **The estimate (INFERRED):** about 1 min at `N = 16`, 15 to 16 min at 24 and 103 to 107 min at 32, so about 2 h in all, setup aside. The terms' 2 to 4 h stands.
- **Running.** A sidebar task, under `caffeinate`, with `python -u` and no pipe, on mains power. Compute and wall time are reported separately. An interruption restarts the case, with its partial outputs moved aside, as the driver's resume does.

## Then

1. After the units' GO and Blake's word: `BOUNDARY.md` written, the four changes, the tests above, and the scorer's SHA-256 logged. Then the run.
2. `score_ladder.py` scores the run. `DEVLOG.md` records the run and its scoring, each script and output with its SHA-256. The outputs move to `dev/runs/`.
3. `build_dry.py plumbing` restores `DRY.json`, byte for byte, its SHA-256 checked against entry 15's, so the ladder's list does not become the default (UA).
4. The results and the changes' diffs go to the units. Nothing else runs until they reply.
5. Step 5, terms v4, on Blake's word with the units first. It takes the ladder's outcome among the development runs it discloses.

**The record (UB).** Each run's script and outputs are copied to `dev/runs/` before the next run starts, so no entry depends on a reconstruction.

## What the plan does not do

- No row and no sealed case solved: no C3 ray, no T5J and no pyramid. The seed check's rerun builds the sealed seeds on the lowest level only, within amendment 2's scope.
- No `N = 40`, and no point past `ε = 32`.
- No change to `instrument/`, to the frozen values or to any calibration constant, and no credit.
- Amendment 4's registered sample stays as it is. The `R5` gate is read only in the registered run.

## For the units

Both reviewed v1. UA held on two wording corrections, and UB gave GO after three fixes; all five are in (`DEVLOG.md` entry 22). With the run's results, the units receive:
- (a) `BOUNDARY.md` as written;
- (b) the changes' diffs and the tests' outputs;
- (c) the scored claims and the reported values;
- (d) the run's times against the estimate.
