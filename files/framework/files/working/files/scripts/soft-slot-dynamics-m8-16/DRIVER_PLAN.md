# M8.16: the registered driver and its dry run (step 3 of the pre-freeze build; plan v4, the units' rulings on the dry run folded, 2026-10-18)

Built only after both units' GO. It turns the terms v3's THE RUN, THE CHECKS, THE VERDICT RULE and FIXED AT THE FREEZE into code, and runs that code on the GO controls as a dry run. Nothing sealed is constructed outside amendment 2's check, or solved, or read. The real `FROZEN.json` is not written: that happens once, after the maintainer's go.

## What is built

**1. The frozen allowlist replaces the freeze file** (UA's condition, `DESIGN.md` § 6).
- `instrument/devtools.py` gains `frozen()`. It loads `run/FROZEN.json` and validates it: its manifest SHA-256 must equal the running instrument's, and its terms SHA-256 must equal that of `run/m8_16_task_details.md`, the filed terms copied byte for byte.
- `require(case)` admits a GO case as now, and a sealed case only when `frozen()` validates and lists it. `R0` is never admitted.
- `branches.seed_state` admits a sealed seed on the same test, in place of the `FREEZE` file's existence. `sealed_seed_for_check` and the seedcheck guard are unchanged.
- **The manifest** is the SHA-256 of every file in `instrument/`, `run/` and `reference/m815/`, in a fixed order, except `FROZEN.json`, `run/FROZEN_PIN`, `run/MANIFEST_PIN` and the run's outputs under `run/out/` and `run/dry/`. Its own SHA-256 is the pin. The pin is held in `run/MANIFEST_PIN`, outside what it pins, as M8.15.2 held its pin in `t1_branch.py`, and is copied into the freeze block. The target rows' records are pinned in `FROZEN.json` (item 5) (UB).
- **The freeze pin** (UA). `FROZEN.json`'s own SHA-256 is written beside it, in `run/FROZEN_PIN`, and published in the freeze block. `frozen()` refuses unless the file's SHA-256 equals the pin, before it reads anything else, so an allowlist edited with its embedded hashes left intact is refused.

**2. `run/write_guard.py`, in M8.15.2's pattern.** It writes `run/FROZEN.json` once, by exclusive create, given the go's link. It refuses if the file exists, if there is no go, or if the manifest differs from its pin. The file holds:
- the 14 cases, each with its slot, representative (as `branches.representative` gives it), `Q`, `(k, r_u)`, expected `V₀`, type and indices, and frozen slow spectrum;
- every point: its `ε`, its cutoffs, and whether its spectrum is read (the five undecided points are not);
- the frozen values: the calibration as `linear.py` carries it, the solve's bounds and the checks' thresholds;
- the terms' SHA-256, the go, and the manifest's SHA-256.

**3. `run/driver.py`, the run in the terms' order.**
- The controls C1, C2a, C2b and C3 run first, then the pyramid. Each case runs all its points at every cutoff, and its checks are read once it completes. A failed check stops the run before the next case, and the gate record is written then, with what ran and the failing check named (UB).
- The gate record, `run/out/GATE.json`, holds K1 to K4 with their outcomes. Its SHA-256 goes into the run's log.
- At the end, and at a stop, `VERDICT.json` and the driver's transcript, `run/out/driver.out`, are written, each with its SHA-256 in the run's log. At a stop the verdict is NOT QUALIFIED, naming the failing check; `incomplete` is kept for a dry run and for an interruption.
- The rows follow: T1's and T4's samples in both slots, then T2's and T3's ladders in both slots and T5's. Each is refused until the gate record shows K1 to K4 passed.
- At a withheld point the branch is solved and accepted, and `ln.record` is not called.
- Every point's summary, levels and record are saved. Each cutoff runs on its own path from the seed.
- **An interruption** (power, a crash) is logged and resumed. The run's log records the manifest's SHA-256 when the run starts, and a resume refuses a tree whose manifest differs. On resume, each completed case is loaded with its outputs checked against the SHA-256 the log recorded, and its stop test is read again before the next case runs: a completed control or pyramid that failed a check stops the resumed run there, as it stopped the first, and a log whose gate record names a stop refuses any resume. The driver restarts at the first case whose outputs are incomplete. An incomplete case's partial outputs move to `run/out/interrupted/`, reported, unscored. The run is made on mains power, with sleep off (UB).
- **`R5`'s coherent branch** (BOUNDARY.md's amendment 4; Blake's decision before the dry run, UB): it runs in the controls' phase as a registered control that gates the `R5` rows only. If it fails, T1 to T4 in `R5` are recorded as not qualified, with the `R5` control's failing check named, and are not run; the run continues. The dry run runs it with the other controls, about 36 min more.

**4. `run/checks.py`, K1 to K6 as the terms state them.**
- **K1 and K2** come from the record: `V₀`, the leak, the cluster, and the slow band against the frozen spectrum.
- **K3's overlap** is M8.15.x's `static_overlap` (UB): `‖Q_Uᵀ s‖/‖s‖`, with `s` the eigenvector's static part. The spans are formed as M8.15.x's `control_2a.py` forms them (`point_record`, MIT `2c27cea`): the rotation span `{T_xφ, T_yφ, T_zφ}`, with the fibre direction `iφ` and the phase partner's static part projected out, made `L²`-orthonormal; `Q_Z`, the rotation about the seed's axis, `T_zφ`, projected into that span (M8.15.x's slice direction); and `Q_XY`, the span's complement to `Q_Z`. At the pyramid's seed `T_zφ`'s unit vector has a component of 0.158 along `iφ`, so the projection matters (UB). It is tested on a synthetic vector of known overlap, and against M8.15.x's own `static_overlap`, `real_orthonormal` and `project_out`, applied to the same arrays with `M = I` at C3's points, to 10⁻¹². `k3_spans` also reports the axis rotation's part outside the fibre span, ‖P_R z‖/‖z‖, at every cutoff; where it is below 10⁻⁶, `Q_Z` is undefined and (c) reads failed, with that reason. At the pyramid's seed it is about 0.987, since its four orbit tangents are independent (UB's figure, not recomputed before the freeze: the seed is sealed). `test_k3.py` also reads C3's saved points at order one, `T_xφ` and `T_yφ` as (XY 1, Z 0) and `T_zφ` as (XY 0, Z 1), to 10⁻¹² in both implementations, with C2a's saved points as the arm: its axis rotation lies in the fibre span, and (c) reads failed with that reason (UB).
- **K4:** C1 as D6 registered it; C2a, C2b, C3 and P5 as the terms state.
- **K5:** the 5% match by class and Krein sign, with multiplicity, by the assignment problem.
- **K6:** the reading at each decided point against M8.15's records (the type, `K = n(B) − n(B|G_tol)`, and `k_i⁻`), with branch identity between `N = 24` and 32: D7's aligned distance at most 10⁻², and the two records equal.
- **The band-edge guard:** a point reads Unresolved if half its band edge lies within the zero cluster's gray zone (UA).
- **The verdict:** QUALIFIED on K1 to K4, with each row qualified on K5, and on K6 where it has a ladder; or NOT QUALIFIED, with the failing check named. K3 keeps its three outcomes.

**5. M8.15's records for K6.** The controls' records are in `reference/m815/`. The target rows' records, T2 and T3 in both slots and T5, are sealed with their rows until the freeze (BOUNDARY.md's sealed list). Before it, `run/` names each by MIT commit, path and git blob id, as `git ls-tree` lists them, and the files stay unopened. After the go, `write_guard.py` copies them into `reference/m815_targets/`, refuses unless each blob id matches, and writes each one's SHA-256 into `FROZEN.json`, where `frozen()` checks them. K6's reader is built and tested on the controls' records (UB).

## The dry run (development, GO cases only)

`run/driver.py --dry` runs against `run/DRY.json`, the dry run's case list: C1, C2a, C2b, C3 and `R5`'s coherent branch. Only the driver reads it; `require` and `seed_state` read `FROZEN.json` alone, so admission stays with today's GO list (UB). Its outputs go under `run/dry/`. The dry run's withheld point exists only in `DRY.json`: a real run takes its points, the five withheld among them, from `FROZEN.json` alone (UA).
- **The controls' phase, exactly as registered:** C1 at Theorem D's points; C2a, C2b, C3 and `R5`'s coherent branch at `ε ∈ {0.25, 0.5, 1, 2}` and `N = 16, 24, 32`. K1, K2 (on C2a and C2b) and K4 are evaluated and written to a dry gate record, with the `R5` gate beside them.
- **The pyramid and every row are refused,** since `DRY.json` lists none of them.
- **K6's path, on a control:** C2a's ladder on M8.15's grid from 0.25 to 2 at `N = 16, 24, 32`, read against M8.15's C2a record. One point, `ε = 0.707`, is marked withheld, to show it is solved and not recorded.

**Expected, derived before the run:**
- K1, K2 and K4 pass on C1 to C3, as in development, and the `R5` control passes as its development sample did (`EXPECTED_R5.md`). The dry gate record shows each as passed on the GO controls, with the pyramid's parts and K3 marked absent, and the row gate refuses it (§ The guard's tests);
- K5's and K3's code runs on the controls' records, unscored: K5 passes on C2a, C2b and C3 at `ε = 0.25` with their frozen spectra; K3 on C2a at `ε = 0.25` reads Not resolved with the kernel exact, at (b), since C2a's slow pairs are all Krein-positive, with (c) and (d) computed on its smallest pair and reported;
- K6 reads C2a's six read points as agreeing with M8.15;
- the withheld point is accepted and has no record;
- at 0.25, 0.5, 1 and 2, C2a's ladder segment and C2a's sample read the same type and indices, with every slow eigenvalue within the larger margin of the two records;
- where they overlap, the readings equal development's: the type and the indices, with every slow eigenvalue within the larger margin of the two records (UB).

## The guard's tests (no solve; temporary folders)

Each case below must be refused:
- a case off the allowlist; `R0`, also when a test `FROZEN.json` lists it; and a sealed name placed in `DRY.json`;
- a sealed case without `FROZEN.json`, with a `FREEZE` file alone present, and with a `FROZEN.json` whose manifest SHA-256 or terms SHA-256 is wrong;
- a `FROZEN.json` with a case entry edited and its embedded hashes left intact, against its pin (UA);
- a row before the gate record shows K1 to K4 passed, a gate record whose SHA-256 differs from the logged one, and the dry gate record;
- `write_guard.py` with `FROZEN.json` present, without a go, with a manifest that differs from `run/MANIFEST_PIN`, or with a target record whose blob id differs from the named one (on synthetic files);
- `frozen()` with a target record whose SHA-256 differs from `FROZEN.json`'s (on synthetic files);
- a point whose band edge is forced into the gray zone, which must read Unresolved (UA);
- at a withheld point, each call that would compute its record: `first_order`, `record`, `summarize`, and any reading of `L`'s inertia or spectrum. Newton's own `hess_dense` stays open, since the solve needs it;
- a resume on a changed manifest, a resume whose completed control failed a check with no gate record, and a resume whose gate record names a stop, with a clean interruption as the green parent (UA, UB);
- a real run given other cutoffs, under `python -O` (UB);
- under `python -O`, every run, at `require`; and each guard converted from an `assert`, against its own mutation: `R0` in `basis.py`, `EXPECTED_V0.md`'s pin, the bases' embedding, and `log_run`'s kept outputs (UA, UB).

**The green parents** are the same calls under a valid test `FROZEN.json` that lists GO cases only. **The frozen path's own green parent:** in the test's process, with `devtools.GO` emptied and C2a entered in `branches.SEALED` at its own slot and level, C2a is admitted by `require` and its seed built by `seed_state` through a valid test `FROZEN.json` that lists it, and both refuse once that file is removed. So the path that admits the sealed cases after the go runs before it, on a GO case. A sealed name has no green parent: the tests read its refusal on the name alone, and no test constructs or solves a sealed seed (UB).

## The cost, at development's measured rates

- **The dry run:** C1 about 16 min; the samples of C2a, C2b and C3 about 24, 10 and 31 min; C2a's ladder segment about 39 min. About 2.0 hours in all, at rates measured on battery.
- **The tests:** seconds.
- **The regression after the instrument changes:** under a minute. It covers DL, `dl_recal`, the separation claims, the re-reads and the seed check.

## What the plan does not do

- No real `FROZEN.json`, no go, no sealed solve, and no filing.
- No change to the record, the calibration or Newton. The convergence rule changed once, after the dry run found that its sets depended on the order of the groups (DEVLOG 218, 232 and 234).
- The terms' text follows in their next version, v4, with steps 1 to 3's outcomes.

## For the units

- (a) the allowlist mechanism in place of the freeze file;
- (b) the driver's order, its gate and its withheld points;
- (c) K1 to K6 as planned, especially K3's overlap and K6's identity and comparison;
- (d) the dry run's scope, with C2a's ladder segment for K6, and its expected outcomes;
- (e) the guard's tests;
- (f) GO or HOLD on step 3.
