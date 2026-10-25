# M8.16.1 run record

The record of M8.16.1's registered run on 2026-10-25, under the governing terms, `run/m8_16_task_details.md` (SHA-256 `9d16712982e53889…`), merged in OpenWave [#650](https://github.com/openwave-labs/openwave/pull/650), and the instrument frozen at MIT `d1c0ec8` with its manifest pin, `8cc2d7e2d01a72fc…`. The maintainer's go is [#650's comment](https://github.com/openwave-labs/openwave/pull/650#issuecomment-6385959498), and the freeze block is OpenWave's `research/m8_16_1/freeze_block.md`, merged in [#652](https://github.com/openwave-labs/openwave/pull/652). Every number below is read from the run's files in [`run/out/`](run/out/), and `tools/build_record.py` builds this record from them. The case files hold every point's full readings at every cutoff. This record gives each point's type and indices, or the convergence rule's Unresolved; each case's deviations from leading order; every group's next-order reading at every cutoff (§ 11); and every check. The verdict is the one the driver wrote under the terms' verdict rule. Adjudication is the maintainers'.

**The outcome.** QUALIFIED. The instrument qualifies: the five controls passed every check, and the pyramid passed K1 to K4, with K3 resolved. Its quartet lies 5.76%, 5.78% and 5.78% from Theorem R's leading order at `ε = 0.25`, at `N = 16, 24` and 32, as M8.16 read it, and passes the next-order bar at every cutoff. All nine rows qualify: T1/R4, T1/R5, T4/R4, T4/R5, T2/R4, T2/R5, T3/R4, T3/R5, T5/R2. T5's second member, T5J/R2, is not qualified: its three groups read Unresolved by check 1 at `ε = 0.25`, where the convergence rule reads the point Unresolved (§ 6). The C3 ray passed, its discrimination holding.

**The cases, in the order run,** every case at its three cutoffs (C1 at four):

| Case | Role | Slot | Passed | Failed | Groups under the next-order bar | s |
|---|---|---|---|---|---|---|
| C1 | control | `R3` | K1, K4 | none | none | 730 |
| C2a | control | `R4` | K1, K4, converged, bar, trend, K2 | none | none | 845 |
| C2b | control | `R2` | K1, K4, converged, bar, trend, K2 | none | none | 352 |
| C3 | control | `R4` | K1, K4, converged, bar, trend | none | none | 1124 |
| C2a/R5 | R5gate | `R5` | K1, K4, converged, bar, trend | none | none | 1593 |
| P5 | pyramid | `R4` | K1, K2, K4, converged, bar, seeds, K3 | none | 2 pass | 1238 |
| C3R/R4 | ray | `R4` | K1, K2, bar, discrimination | none | 3 pass | 1301 |
| T1/R4 | row | `R4` | K5, bar | none | 5 pass | 1103 |
| T1/R5 | row | `R5` | K5, bar | none | 5 pass | 2114 |
| T4/R4 | row | `R4` | K5, bar | none | 4 pass | 1304 |
| T4/R5 | row | `R5` | K5, bar | none | 4 pass | 2452 |
| T5J/R2 | member | `R2` | none | K5, bar | 3 Unresolved | 506 |
| T2/R4 | row | `R4` | K5, bar, K6 | none | 2 pass | 6550 |
| T2/R5 | row | `R5` | K5, bar, K6 | none | 2 pass | 10708 |
| T3/R4 | row | `R4` | K5, bar, K6 | none | 2 pass | 6916 |
| T3/R5 | row | `R5` | K5, bar, K6 | none | 2 pass | 11131 |
| T5/R2 | row | `R2` | K5, bar, K6 | none | 3 pass | 2710 |

## 1. Custody

- **The freeze.** `run/FROZEN.json` was written once, at 2026-10-25T01:40:57Z, by `run/write_guard.py`, after the go. It holds the allowlist of 17 cases, the frozen values with the next-order coefficients by case, group and cutoff, the terms' SHA-256, the manifest's SHA-256 and the go, and the SHA-256 of M8.15's 5 target records, which it copied into `reference/m815_targets/` after each blob id matched the one named before the freeze. Its own SHA-256 is `run/FROZEN_PIN`.
- **The freeze block,** built by the pinned `run/freeze_block.py`, carries `FROZEN.json` in full. Its pull request, [#652](https://github.com/openwave-labs/openwave/pull/652), was opened at 2026-10-25T01:52:53Z, before the run started, and merged at 2026-10-25T13:35:02Z, during it. The maintainer's approval rebuilt the block byte for byte from the pinned code, and records one reading note: the column "equals its manifest line" in the seeds' file table compares each file with a manifest built from the same tree, so it shows only that the seed check loaded manifest files. That the seed check ran on these bytes stands on the log: `dev/seed_check.json` is byte for byte the record kept from its runs in `DEVLOG.md` entries 19 and 23; `run/seeds.py` has the SHA-256 entry 23 records after that step's changes; and the 12 files of `instrument/` are M8.16's, byte for byte.
- **Before the run,** read-only: `devtools.frozen()` validated the freeze, the tree against the manifest pin and the terms; `run/record_environment.py --check` found no difference from `run/ENVIRONMENT.json`; and `run/out/` did not exist.
- **The run.** `python3 -I -B -u run/driver.py`, from this folder, its output to `run/out/driver.log` through `tee`, on mains power at its launch (read at 2026-10-25T01:57:34Z, `DEVLOG.md` entry 59), with sleep held off for its length, in the recorded environment: Python 3.13.13, NumPy 2.5.0 and SciPy 1.18.0, on Accelerate's BLAS and LAPACK as each reports them, under macOS 15.8 (24H23) on one Apple M3. It started at 2026-10-25T01:57:38Z and wrote its verdict at 2026-10-25T16:35:38Z, 52680 s later, against 52681 s by its own clock. The cases' run times sum to 52677 s. Its log, `run/out/RUNLOG.json`, records the manifest's SHA-256 at the start, equal to `run/MANIFEST_PIN`, and each completed case's outputs with their SHA-256.
- **After the run:** every output equals the SHA-256 the log recorded; `devtools.frozen()` validates; and the environment, read again, equals `run/ENVIRONMENT.json`.
- **Post-run files.** These files beside this record were made after the run, and are not records from it:
  - `environment_postrun_2026-10-25.txt`: `run/record_environment.py --check`, read after the run, with no difference;
  - `tools/build_record.py`, which builds this record from the files and, with `--check`, reports any difference.
- **The run's files.** `run/out/driver.log` is the run's standard output and error, and equals `run/out/driver.out`, the transcript the driver wrote. The target records are M8.15's, copied at the freeze.

  | File | SHA-256 |
  |---|---|
  | `run/out/C1.json` | `356ffbf4fe71eb1429163e849d53a33f92643b5784124a9d11e9ef8c5e9b15ca` |
  | `run/out/C2a.json` | `0165455b6ba66d462888521a5273fc8f0a744d4430c808e2855f5e9d06d3c24f` |
  | `run/out/C2b.json` | `efd5c21e233f08897f5dc9ded449801bfa3fe8d5e8895b6099b1840dd2b5a0fd` |
  | `run/out/C3.json` | `8e7c303c2e7dfe35e39e3f581ace30d537a1f30073389f8e6aa199b30250d469` |
  | `run/out/C2a_R5.json` | `387ed7b8e04030a2e10569eedb313ca5713bea92bec5a6bac7bd2e6697e668be` |
  | `run/out/P5.json` | `c404e49c2a6e52b0754c97349b01c8097db3271af641bc56071fd72098082bd0` |
  | `run/out/P5.npz` | `64ea832e06882ba39f2a649977edb3496c900a8c79b9e20d46b2506f782e8aab` |
  | `run/out/C3R_R4.json` | `21706fd5b2548cdcb0bf8b44d2df0c6b62d34abad41363d0fb1e43a14a5c9fb6` |
  | `run/out/T1_R4.json` | `4371b7a7ed612e11031a97013f46632f25bd6afce80c5a2f5cc86f80a5657c63` |
  | `run/out/T1_R5.json` | `ede0e0591013f50a3fd3321f97fec8b508946aba0d711f1ab68a29d6cef74c0e` |
  | `run/out/T4_R4.json` | `e3e64fe89169a07e6a3bcaf44aa0b64aa91eef6b6aab3b2f7109d120ef2a8299` |
  | `run/out/T4_R5.json` | `94935f9b461afc33767d25ba624082e980bc62e7139caa63a9da47c0077b5349` |
  | `run/out/T5J_R2.json` | `ae839c5425f13ca9a48bb6f0fc020e91c74ab64b637be0da8a2a5ff752569463` |
  | `run/out/T2_R4.json` | `4f0ce100703e43d39b92caca466f31cdf788ebd381168f3bfa3fc8e72c51b6b1` |
  | `run/out/T2_R5.json` | `99de516f8b59d66db297dfbbf5426c6b9ad7f3ae3b154d0b02fe60b9d95ed7bd` |
  | `run/out/T3_R4.json` | `50167d9de8ed1f6e11152a0b48a631669de532ef6d5021abd916ef8ee81b9489` |
  | `run/out/T3_R5.json` | `6a581b98bf3687cd64b32d4e833c345a1932a00b2fbf513da9c0c825bc92f2b6` |
  | `run/out/T5_R2.json` | `cd627750e764006afd39fac9b100e526d995d9f0967b37259b800212a93b3ffa` |
  | `run/out/GATE.json` | `2d24df590150952a36545a403c34e6a8b1e7b975e7d181897ce899ab55621c19` |
  | `run/out/VERDICT.json` | `98cf1c684d4cf684cd84dd94acf6a18f1ec82aa501a8bcf6a882d769cc9e603b` |
  | `run/out/driver.out` | `5a2913687b8d6960fb11891ff21752362d502b5a807f5d397602a6bd2f96b967` |
  | `run/out/driver.log` | `5a2913687b8d6960fb11891ff21752362d502b5a807f5d397602a6bd2f96b967` |
  | `run/out/RUNLOG.json` | `84f2c9f6667e02d030dfe1d0f759ad183cd0bc6293228bd60e3aa0a2785edadb` |
  | `run/FROZEN.json` | `c258e299b8f0268e805712b4f087b3533c6e0cd3c37e237bf3d0639540c52a2d` |
  | `reference/m815_targets/branch_T2_R4.json` | `5b1758c9ec1c6566091fe9028a542f67fd6bd0ad51c927f7147d54c07d876b49` |
  | `reference/m815_targets/branch_T2_R5.json` | `a064683298ebc922ecbba06316a3af11b68a7b6193e7e04c63eaa9fc1ad931ba` |
  | `reference/m815_targets/branch_T3_R4.json` | `fe3497a3a4de45a5f3a6d2ce2a6c322feb5399610ad20d9da530acd8abdf3bc2` |
  | `reference/m815_targets/branch_T3_R5.json` | `660d0322d1921bb7b6c9e7e1b71bf3c54bea63a6c17a754e22582601b49aaee4` |
  | `reference/m815_targets/branch_T5_R2.json` | `6bcdb5cfd58980bf228b4c84271e51d1e6efa5b6052b0fd6cf98cce143a5884f` |

  The post-run files:

  | File | SHA-256 |
  |---|---|
  | `environment_postrun_2026-10-25.txt` | `5e12e201d9fa970e9ccc7db1ad32778c5f50d4a6014ba45bf6e42a0be7554390` |
  | `tools/build_record.py` | `4fc20d51b0de218122f0eab0ff2f05fa694aa5689ebd2886918bdafc4d1156f3`, as it built this record |

## 2. The controls

Every case ran every point and cutoff the terms set, each cutoff from its own seed. All 52 seeds of the run passed their check: every `Q(u)` within 4×10⁻¹⁵ of its exact value, relative, every criticality at most 3×10⁻¹⁵, against `10⁻¹²`, and every `(k, r_u)` the frozen case's. Quantities at the round-off level are given as bounds. Points' `m = ‖φ‖²` run from 0.1479 to 72.26; the calibration was fitted on `0.204` to `132` in `R2`, `R3` and `R4` (M8.16's terms, § STATED LIMITS). Below that range lie the points at `ε = 0.25` of T5J/R2, `m` down to 0.148; `ε = 0.25` of T3/R4, `m` down to 0.184; `ε = 0.25` of T5/R2, `m` down to 0.148. There the margin reads `max(m, m₀)` with `m₀ = 0.2`, an extrapolation, flagged. `R5`, the slot of C2a/R5, T1/R5, T4/R5, T2/R5, T3/R5, lies outside the slots it was fitted on, so the margin there is an extrapolation too.

**The margin's headroom.** M8.16's terms fit the margin on the controls' largest cluster coefficient, 0.0568, and state that its ten-fold headroom holds on the controls (§ STATED LIMITS). Over this run's 381 points the coefficient exceeds 0.0568 at 87, in 10 cases, and the zero cluster lies less than ten times below its gray zone's lower edge at 54, in 7 cases: P5, T5J/R2, T2/R4, T2/R5, T3/R4, T3/R5, T5/R2. The least headroom is 4.6 times, at T3/R5, `N = 24`, `ε = 4`. Points the bar scores are among them, in P5, T5J/R2, T2/R4, T2/R5, T3/R4, T3/R5, T5/R2. Every cluster stays separated, as K1 asks, and no eigenvalue outside it enters its gray zone: the nearest lies at least 10.1 times above the zone's upper edge. On `L`, the kernel's lift is at most 16.9 u‖L‖, against the cut of 1000 u‖L‖, and the smallest genuine eigenvalue at least 2.48×10⁹ u‖L‖, against the cut's gray zone, which ends at 10000 u‖L‖. No constant moves: the calibration is fixed with the instrument.

**C1, Theorem D at the rigid slot `R3`** (730 s). The exact branch, `c = √ε v`, `λ = λ₀ + ‖c‖²`, with no solve, at `ε ∈ {0.5, 1, 2}` and `N = 16, 24, 32` and 40. At all 12 points the residual is at most 3×10⁻¹⁶ of the size, against `10⁻¹⁵`; the cubic's part off the lowest level at most 2×10⁻¹⁵, against `10⁻¹⁴`; and the lowest level's spectrum Theorem D's to 4×10⁻¹⁴ relative, against `10⁻¹⁰`. Every point is Elliptic, `(n(L), n(D), K) = (0, 0, 0)`, with `V₀` as expected. K1 and K4 pass.

**C2a, C2b, C3 and C2a/R5,** at every point and at `N = 16, 24` and 32. The last column is the branch identity's aligned distance between `N = 24` and 32, against `10⁻²`.

| Case | Slot | `ε` | Type; `(n(L), n(D), K)` | Largest deviation from leading order, `N = 16, 24, 32` | Convergence | Aligned distance |
|---|---|---|---|---|---|---|
| C2a | `R4` | 0.25 | Elliptic; (0, 0, 0) | 0.70%, 0.73%, 0.73% | converged | 3.6×10⁻¹⁰ |
| C2a | `R4` | 0.5 | Elliptic; (0, 0, 0) | 1.40%, 1.45%, 1.45% | converged | 1.4×10⁻⁹ |
| C2a | `R4` | 1 | Elliptic; (0, 0, 0) | 2.76%, 2.86%, 2.86% | converged | 5.6×10⁻⁹ |
| C2a | `R4` | 2 | Elliptic; (0, 0, 0) | 5.40%, 5.59%, 5.59% | converged | 2.2×10⁻⁸ |
| C2b | `R2` | 0.25 | Elliptic; (0, 0, 0) | 0.39%, 0.46%, 0.46% | converged | 3.3×10⁻⁹ |
| C2b | `R2` | 0.5 | Elliptic; (0, 0, 0) | 0.78%, 0.91%, 0.91% | converged | 1.3×10⁻⁸ |
| C2b | `R2` | 1 | Elliptic; (0, 0, 0) | 1.55%, 1.81%, 1.81% | converged | 5.2×10⁻⁸ |
| C2b | `R2` | 2 | Elliptic; (0, 0, 0) | 3.07%, 3.56%, 3.56% | converged | 2.0×10⁻⁷ |
| C3 | `R4` | 0.25 | Hyperbolic; (6, 3, 3) | 0.45%, 0.51%, 0.51% | converged | 8.5×10⁻⁸ |
| C3 | `R4` | 0.5 | Hyperbolic; (6, 3, 3) | 0.90%, 1.02%, 1.02% | converged | 3.4×10⁻⁷ |
| C3 | `R4` | 1 | Hyperbolic; (6, 3, 3) | 1.77%, 2.02%, 2.02% | converged | 1.4×10⁻⁶ |
| C3 | `R4` | 2 | Hyperbolic; (6, 3, 3) | 3.47%, 3.96%, 3.96% | converged | 5.4×10⁻⁶ |
| C2a/R5 | `R5` | 0.25 | Elliptic; (0, 0, 0) | 0.88%, 0.93%, 0.93% | converged | 1.7×10⁻¹⁰ |
| C2a/R5 | `R5` | 0.5 | Elliptic; (0, 0, 0) | 1.75%, 1.85%, 1.85% | converged | 6.7×10⁻¹⁰ |
| C2a/R5 | `R5` | 1 | Elliptic; (0, 0, 0) | 3.45%, 3.65%, 3.65% | converged | 2.7×10⁻⁹ |
| C2a/R5 | `R5` | 2 | Elliptic; (0, 0, 0) | 6.72%, 7.10%, 7.10% | converged | 1.0×10⁻⁸ |

- **C2a** (`R4`, 845 s): K1 passes, K2 passes, and K4 passes. The largest deviation from leading order is 0.70%, 0.73%, 0.73% at `ε = 0.25` and 5.40%, 5.59%, 5.59% at `ε = 2`, at `N = 16, 24` and 32. Every floor is below 10⁻¹⁶, every tangent residual below 0.2 u, and every zero cluster below 0.03 of its margin. Beside the rule, unscored, the largest relative change between the two highest cutoffs is at most 2×10⁻⁹, within the retired fraction `10⁻⁶`.
- **C2b** (`R2`, 352 s): K1 passes, K2 passes, and K4 passes. The largest deviation from leading order is 0.39%, 0.46%, 0.46% at `ε = 0.25` and 3.07%, 3.56%, 3.56% at `ε = 2`, at `N = 16, 24` and 32. Every floor is below 10⁻¹⁶, every tangent residual below 5 u, and every zero cluster below 0.04 of its margin. Beside the rule, unscored, the largest relative change between the two highest cutoffs is at most 4×10⁻⁸, within the retired fraction `10⁻⁶`.
- **C3** (`R4`, 1124 s): K1 passes, and K4 passes. The largest deviation from leading order is 0.45%, 0.51%, 0.51% at `ε = 0.25` and 3.47%, 3.96%, 3.96% at `ε = 2`, at `N = 16, 24` and 32. Every floor is below 10⁻¹⁶, every tangent residual below 0.10 u, and every zero cluster below 0.03 of its margin. Beside the rule, unscored, the largest relative change between the two highest cutoffs is at most 3×10⁻⁷, within the retired fraction `10⁻⁶`.
- **C2a/R5** (`R5`, 1593 s): K1 passes, and K4 passes. The largest deviation from leading order is 0.88%, 0.93%, 0.93% at `ε = 0.25` and 6.72%, 7.10%, 7.10% at `ε = 2`, at `N = 16, 24` and 32. Every floor is below 10⁻¹⁶, every tangent residual below 0.2 u, and every zero cluster below 0.02 of its margin. Beside the rule, unscored, the largest relative change between the two highest cutoffs is at most 7×10⁻¹⁰, within the retired fraction `10⁻⁶`. Its margin is an extrapolation: `R5` lies outside the slots the calibration was fitted on (M8.16's terms, § STATED LIMITS).

## 3. The pyramid, P5

P5 is `R4`'s pyramid (1238 s). Every point is accepted, at every cutoff, and K1 and K2 hold at every point: the slow band holds exactly the three predicted groups. Each group's deviation from Theorem R's leading order, reported and unscored, is given at `N = 16, 24` and 32.

| `ε` | Type; `(n(L), n(D), K)` | The in-span pair | The quartet | The Krein-positive pair | Aligned distance |
|---|---|---|---|---|---|
| 0.25 | Hyperbolic; (5, 1, 4) | 0.28%, 0.35%, 0.35% | 5.76%, 5.78%, 5.78% | 0.12%, 0.20%, 0.20% | 8.6×10⁻⁸ |
| 0.5 | Hyperbolic; (5, 1, 4) | 0.56%, 0.69%, 0.69% | 11.33%, 11.35%, 11.35% | 0.23%, 0.40%, 0.40% | 3.4×10⁻⁷ |
| 1 | Hyperbolic; (5, 1, 4) | 1.12%, 1.38%, 1.38% | 21.95%, 21.95%, 21.95% | 0.48%, 0.80%, 0.80% | 1.4×10⁻⁶ |
| 2 | Hyperbolic; (5, 1, 4) | 2.24%, 2.75%, 2.75% | 41.66%, 41.50%, 41.50% | 0.98%, 1.63%, 1.63% | 5.3×10⁻⁶ |

Every floor is below 10⁻¹⁶, every tangent residual below 0.2 u, every zero cluster below 0.04 of its margin, and every `ε` converged. Beside the rule, unscored, the largest relative change between the two highest cutoffs is at most 2×10⁻⁸, 1×10⁻⁷, 7×10⁻⁷, 6×10⁻⁶ at `ε = 0.25, 0.5, 1` and 2, above the retired fraction `10⁻⁶` at `ε = 2`.

**The next-order bar,** on the quartet and the Krein-positive pair, at `ε = 0.25, 0.5` and 1. Both pass checks 1 to 4 at every cutoff. The columns give, at `N = 16, 24` and 32: check 3's spread over the ceiling `C_g(N)`; check 4's distance `|c_g(N) − ĉ₃|` over its tolerance, `max(spread, 0.1 C_g(N))`; and, reported and unscored, the two-term residual at `ε = 0.25`, relative to leading order (§ 11 gives every check).

| Group | `c_g/(κs_g)`, `N = 32` | Spread over `C_g(N)` | Check 4: distance over tolerance | Two-term residual at 0.25 |
|---|---|---|---|---|
| the quartet | −0.109831 − 0.20915 i | 0.024, 0.026, 0.026 | 0.071, 0.077, 0.077 | 0.19%, 0.20%, 0.20% |
| the Krein-positive pair | −0.00792389 | 8.0×10⁻⁴, 8.2×10⁻⁴, 8.2×10⁻⁴ | 1.7×10⁻⁴, 2.2×10⁻⁴, 2.2×10⁻⁴ | 0.0010%, 0.0007%, 0.0007% |

M8.16 read the quartet 5.76% to 5.78% from leading order at `ε = 0.25`, over its bar of 5%, and stopped there. This run reproduces M8.16's: at every point of the pyramid and the five controls, 72 points in all, its group centres equal those of M8.16's record at MIT `87fc643`, bit for bit, each of those files checked against M8.16's run log. Read against the next-order prediction `εκs_g + ε²c_g(N)`, the same readings pass. That is a known outcome on M8.16's record, read as INFERRED, not a check of Proposition N passed (the terms, § Known outcomes; the reading note of [#650's first review](https://github.com/openwave-labs/openwave/pull/650#pullrequestreview-5631395680)).

**K3 at `ε = 0.25`,** at every cutoff:

| `N` | (a) the kernel, by `L`'s certificate, and the slow band outside the in-span class | (b) the in-span pair | (c) the static overlaps, XY and Z | (d) |
|---|---|---|---|---|
| 16 | holds: tangent residual below 0.03 u, `L`'s zero count 4 = the chains, gray zone empty; the quartet and the Krein-positive pair pass the bar | holds: 0.28% | holds: 0.9970 and below 10⁻¹⁰; axis fraction 0.987 | holds |
| 24 | holds: tangent residual below 0.04 u, `L`'s zero count 4 = the chains, gray zone empty; the quartet and the Krein-positive pair pass the bar | holds: 0.35% | holds: 0.9970 and below 10⁻⁹; axis fraction 0.987 | holds |
| 32 | holds: tangent residual below 0.02 u, `L`'s zero count 4 = the chains, gray zone empty; the quartet and the Krein-positive pair pass the bar | holds: 0.35% | holds: 0.9970 and below 10⁻⁹; axis fraction 0.987 | holds |

- **K3 is resolved:** (a) to (d) hold at every cutoff. (a)'s slow band is read by the next-order bar, check 1 as K3(a) reads it. (d) reads the group (b) finds at `N = 32`: converged, its distance to the nearest event, A's gray zone, 532 times its uncertainty.
- **K4 passes:** converged at `ε = 0.25`, Hyperbolic with `(5, 1, 4)` at every cutoff, every seed passed, and both groups under the bar pass.

## 4. The C3 ray, C3R/R4

The ray in `R4`, a control that gates nothing (1301 s). K1 and K2 hold at its four points, and its 3 groups pass the next-order bar at every cutoff (§ 11). Its points, at `N = 16, 24` and 32, with the aligned distance between `N = 24` and 32:

| Case | Slot | `ε` | Type; `(n(L), n(D), K)` | Largest deviation from leading order, `N = 16, 24, 32` | Convergence | Aligned distance |
|---|---|---|---|---|---|---|
| C3R/R4 | `R4` | 0.25 | Hyperbolic; (5, 1, 4) | 2.63%, 2.61%, 2.61% | converged | 8.1×10⁻⁸ |
| C3R/R4 | `R4` | 0.5 | Hyperbolic; (5, 1, 4) | 5.21%, 5.18%, 5.18% | converged | 3.2×10⁻⁷ |
| C3R/R4 | `R4` | 1 | Hyperbolic; (5, 1, 4) | 10.28%, 10.22%, 10.22% | converged | 1.3×10⁻⁶ |
| C3R/R4 | `R4` | 2 | Hyperbolic; (5, 1, 4) | 20.17%, 20.08%, 20.08% | converged | 4.9×10⁻⁶ |

**The discrimination holds:** wherever checks 1 and 2 hold, the prediction with the off-ray part left out, `c_g°(N)`, fails check 4 at `c_g`'s tolerance. Its distance from `ĉ₃`, over that tolerance, at `N = 16, 24` and 32:

| Group | `|c_g°(N) − ĉ₃|` over the tolerance |
|---|---|
| 1: quartet | 306, 299, 299 |
| 2: imaginary pair, Krein-negative | 229, 185, 185 |
| 3: imaginary pair, Krein-positive | 46, 44, 44 |

The smallest is 44. The ray's outcome is "passed", as the driver wrote it.

## 5. The rows

**The points of the samples and the member,** at `N = 16, 24` and 32. A point the convergence rule leaves Unresolved is not labelled with a type (the terms, § STATED LIMITS: WHAT IS ADDED). The last column is the aligned distance between `N = 24` and 32.

| Case | Slot | `ε` | Type; `(n(L), n(D), K)` | Largest deviation from leading order, `N = 16, 24, 32` | Convergence | Aligned distance |
|---|---|---|---|---|---|---|
| T1/R4 | `R4` | 0.25 | Elliptic; (2, 0, 2) | 0.78%, 0.82%, 0.82% | converged | 1.2×10⁻⁸ |
| T1/R4 | `R4` | 0.5 | Elliptic; (2, 0, 2) | 1.56%, 1.63%, 1.63% | converged | 4.8×10⁻⁸ |
| T1/R4 | `R4` | 1 | Elliptic; (2, 0, 2) | 3.08%, 3.21%, 3.21% | converged | 1.9×10⁻⁷ |
| T1/R4 | `R4` | 2 | Elliptic; (2, 0, 2) | 5.99%, 6.25%, 6.25% | converged | 7.2×10⁻⁷ |
| T1/R5 | `R5` | 0.25 | Elliptic; (2, 0, 2) | 1.02%, 1.06%, 1.06% | converged | 7.2×10⁻⁹ |
| T1/R5 | `R5` | 0.5 | Elliptic; (2, 0, 2) | 2.02%, 2.10%, 2.10% | converged | 2.8×10⁻⁸ |
| T1/R5 | `R5` | 1 | Elliptic; (2, 0, 2) | 3.98%, 4.12%, 4.12% | converged | 1.1×10⁻⁷ |
| T1/R5 | `R5` | 2 | Elliptic; (2, 0, 2) | 7.71%, 7.98%, 7.98% | converged | 4.3×10⁻⁷ |
| T4/R4 | `R4` | 0.25 | Elliptic; (7, 1, 6) | 3.02%, 2.86%, 2.86% | converged | 7.9×10⁻⁸ |
| T4/R4 | `R4` | 0.5 | Elliptic; (7, 1, 6) | 6.07%, 5.75%, 5.75% | converged | 3.1×10⁻⁷ |
| T4/R4 | `R4` | 1 | Elliptic; (7, 1, 6) | 12.23%, 11.55%, 11.55% | converged | 1.2×10⁻⁶ |
| T4/R4 | `R4` | 2 | Elliptic; (7, 1, 6) | 24.67%, 23.19%, 23.19% | converged | 4.8×10⁻⁶ |
| T4/R5 | `R5` | 0.25 | Elliptic; (7, 1, 6) | 5.65%, 5.79%, 5.79% | converged | 4.8×10⁻⁸ |
| T4/R5 | `R5` | 0.5 | Elliptic; (7, 1, 6) | 10.91%, 11.16%, 11.16% | converged | 1.9×10⁻⁷ |
| T4/R5 | `R5` | 1 | Elliptic; (7, 1, 6) | 20.26%, 20.66%, 20.66% | converged | 7.7×10⁻⁷ |
| T4/R5 | `R5` | 2 | Elliptic; (7, 1, 6) | 34.39%, 34.82%, 34.82% | converged | 3.0×10⁻⁶ |
| T5J/R2 | `R2` | 0.25 | not labelled | 0.53%, 0.54%, 0.54% | Unresolved | 2.6×10⁻⁷ |
| T5J/R2 | `R2` | 0.5 | Elliptic; (9, 3, 6) | 1.05%, 1.07%, 1.07% | converged | 1.0×10⁻⁶ |
| T5J/R2 | `R2` | 1 | Elliptic; (9, 3, 6) | 2.09%, 2.13%, 2.13% | converged | 4.0×10⁻⁶ |
| T5J/R2 | `R2` | 2 | not labelled | 4.16%, 4.21%, 4.21% | Unresolved | 1.6×10⁻⁵ |

**K5,** at the samples and the ladders:

- **T1/R4** (`R4`, 1103 s): K5 holds. Every seed is checked, K1 holds at `ε = 0.25` at every cutoff, the point converges there, Elliptic with `(n(L), n(D), K) = (2, 0, 2)` as expected, and its 5 groups under the bar pass.
- **T1/R5** (`R5`, 2114 s): K5 holds. Every seed is checked, K1 holds at `ε = 0.25` at every cutoff, the point converges there, Elliptic with `(n(L), n(D), K) = (2, 0, 2)` as expected, and its 5 groups under the bar pass.
- **T4/R4** (`R4`, 1304 s): K5 holds. Every seed is checked, K1 holds at `ε = 0.25` at every cutoff, the point converges there, Elliptic with `(n(L), n(D), K) = (7, 1, 6)` as expected, and its 4 groups under the bar pass.
- **T4/R5** (`R5`, 2452 s): K5 holds. Every seed is checked, K1 holds at `ε = 0.25` at every cutoff, the point converges there, Elliptic with `(n(L), n(D), K) = (7, 1, 6)` as expected, and its 4 groups under the bar pass.
- **T2/R4** (`R4`, 6550 s): K5 holds. Every seed is checked, K1 holds at `ε = 0.25` at every cutoff, the point converges there, Elliptic with `(n(L), n(D), K) = (3, 3, 0)` as expected, and its 2 groups under the bar pass.
- **T2/R5** (`R5`, 10708 s): K5 holds. Every seed is checked, K1 holds at `ε = 0.25` at every cutoff, the point converges there, Elliptic with `(n(L), n(D), K) = (3, 3, 0)` as expected, and its 2 groups under the bar pass.
- **T3/R4** (`R4`, 6916 s): K5 holds. Every seed is checked, K1 holds at `ε = 0.25` at every cutoff, the point converges there, Elliptic with `(n(L), n(D), K) = (9, 3, 6)` as expected, and its 2 groups under the bar pass.
- **T3/R5** (`R5`, 11131 s): K5 holds. Every seed is checked, K1 holds at `ε = 0.25` at every cutoff, the point converges there, Elliptic with `(n(L), n(D), K) = (9, 3, 6)` as expected, and its 2 groups under the bar pass.
- **T5/R2** (`R2`, 2710 s): K5 holds. Every seed is checked, K1 holds at `ε = 0.25` at every cutoff, the point converges there, Elliptic with `(n(L), n(D), K) = (9, 3, 6)` as expected, and its 3 groups under the bar pass.

**The diagnosis,** reported, unscored (the terms, § THE VERDICT RULE: WHAT CHANGES): at T1 and T4, in both slots, K5 holds, with the kernel exact and the slow band matched under the bar, which is what the diagnosis predicts there. The record claims nothing beyond that.

**K6, at the ladders.** At every read point, the reading here against M8.15's record: its type, `K = n(B) − n(B|G_tol)` and `k_i⁻`, with the branch identity between `N = 24` and 32. Scored: every point accepted at every cutoff, no disagreement, and agreement at every read point with `ε ≤ 2`. An Unresolved point above `ε = 2` fails no row. M8.15's tracked slow eigenvalues against the nearest here, reported beside each and unscored, are in the case files. The rule's reasons are quoted as it writes them, with `j` for the imaginary unit.

**T2/R4** (`R4`, 6550 s): K6 holds. 18 points ran at every cutoff, all accepted, and 16 are read; `ε = 16, 22.6` ran unread, as registered. Every read point with `ε ≤ 2` agrees; above 2, 9 of 9 agree.

| `ε` | Here: type; `K`; `k_i⁻` | M8.15: type; `K`; `k_i⁻` | K6 | Aligned distance | The rule's reason |
|---|---|---|---|---|---|
| 0.25 | Elliptic; 0; 0 | Elliptic; 0; 0 | agrees | 6.0×10⁻⁸ |  |
| 0.354 | Elliptic; 0; 0 | Elliptic; 0; 0 | agrees | 1.2×10⁻⁷ |  |
| 0.5 | Elliptic; 0; 0 | Elliptic; 0; 0 | agrees | 2.4×10⁻⁷ |  |
| 0.707 | Elliptic; 0; 0 | Elliptic; 0; 0 | agrees | 4.8×10⁻⁷ |  |
| 1 | Elliptic; 0; 0 | Elliptic; 0; 0 | agrees | 9.5×10⁻⁷ |  |
| 1.41 | Elliptic; 0; 0 | Elliptic; 0; 0 | agrees | 1.9×10⁻⁶ |  |
| 2 | Elliptic; 0; 0 | Elliptic; 0; 0 | agrees | 3.8×10⁻⁶ |  |
| 2.83 | Elliptic; 0; 0 | Elliptic; 0; 0 | agrees | 7.4×10⁻⁶ |  |
| 4 | Elliptic; 0; 0 | Elliptic; 0; 0 | agrees | 1.5×10⁻⁵ |  |
| 5.66 | Elliptic; 0; 0 | Elliptic; 0; 0 | agrees | 2.9×10⁻⁵ |  |
| 8 | Elliptic; 0; 0 | Elliptic; 0; 0 | agrees | 5.6×10⁻⁵ |  |
| 11.3 | Elliptic; 0; 0 | Elliptic; 0; 0 | agrees | 1.1×10⁻⁴ |  |
| 32 | Hyperbolic; 2; 0 | Hyperbolic; 2; 0 | agrees | 6.4×10⁻⁴ |  |
| 45.3 | Hyperbolic; 2; 0 | Hyperbolic; 2; 0 | agrees | 1.1×10⁻³ |  |
| 64 | Hyperbolic; 2; 0 | Hyperbolic; 2; 0 | agrees | 1.6×10⁻³ |  |
| 72 | Hyperbolic; 2; 0 | Hyperbolic; 2; 0 | agrees | 1.9×10⁻³ |  |

**T2/R5** (`R5`, 10708 s): K6 holds. 15 points ran at every cutoff, all accepted, and 15 are read. Every read point with `ε ≤ 2` agrees; above 2, 8 of 8 agree.

| `ε` | Here: type; `K`; `k_i⁻` | M8.15: type; `K`; `k_i⁻` | K6 | Aligned distance | The rule's reason |
|---|---|---|---|---|---|
| 0.25 | Elliptic; 0; 0 | Elliptic; 0; 0 | agrees | 3.5×10⁻⁸ |  |
| 0.354 | Elliptic; 0; 0 | Elliptic; 0; 0 | agrees | 7.0×10⁻⁸ |  |
| 0.5 | Elliptic; 0; 0 | Elliptic; 0; 0 | agrees | 1.4×10⁻⁷ |  |
| 0.707 | Elliptic; 0; 0 | Elliptic; 0; 0 | agrees | 2.8×10⁻⁷ |  |
| 1 | Elliptic; 0; 0 | Elliptic; 0; 0 | agrees | 5.5×10⁻⁷ |  |
| 1.41 | Elliptic; 0; 0 | Elliptic; 0; 0 | agrees | 1.1×10⁻⁶ |  |
| 2 | Elliptic; 0; 0 | Elliptic; 0; 0 | agrees | 2.1×10⁻⁶ |  |
| 2.83 | Elliptic; 0; 0 | Elliptic; 0; 0 | agrees | 4.1×10⁻⁶ |  |
| 4 | Elliptic; 0; 0 | Elliptic; 0; 0 | agrees | 8.0×10⁻⁶ |  |
| 5.66 | Elliptic; 0; 0 | Elliptic; 0; 0 | agrees | 1.5×10⁻⁵ |  |
| 8 | Elliptic; 0; 0 | Elliptic; 0; 0 | agrees | 2.8×10⁻⁵ |  |
| 11.3 | Elliptic; 0; 0 | Elliptic; 0; 0 | agrees | 5.1×10⁻⁵ |  |
| 16 | Elliptic; 0; 0 | Elliptic; 0; 0 | agrees | 8.9×10⁻⁵ |  |
| 22.6 | Elliptic; 0; 0 | Elliptic; 0; 0 | agrees | 1.5×10⁻⁴ |  |
| 32 | Elliptic; 0; 0 | Elliptic; 0; 0 | agrees | 2.3×10⁻⁴ |  |

**T3/R4** (`R4`, 6916 s): K6 holds. 18 points ran at every cutoff, all accepted, and 17 are read; `ε = 32` ran unread, as registered. Every read point with `ε ≤ 2` agrees; above 2, 7 of 10 agree, and 3 read Unresolved.

| `ε` | Here: type; `K`; `k_i⁻` | M8.15: type; `K`; `k_i⁻` | K6 | Aligned distance | The rule's reason |
|---|---|---|---|---|---|
| 0.25 | Elliptic; 6; 3 | Elliptic; 6; 3 | agrees | 7.0×10⁻⁸ |  |
| 0.354 | Elliptic; 6; 3 | Elliptic; 6; 3 | agrees | 1.4×10⁻⁷ |  |
| 0.5 | Elliptic; 6; 3 | Elliptic; 6; 3 | agrees | 2.8×10⁻⁷ |  |
| 0.707 | Elliptic; 6; 3 | Elliptic; 6; 3 | agrees | 5.6×10⁻⁷ |  |
| 1 | Elliptic; 6; 3 | Elliptic; 6; 3 | agrees | 1.1×10⁻⁶ |  |
| 1.41 | Elliptic; 6; 3 | Elliptic; 6; 3 | agrees | 2.2×10⁻⁶ |  |
| 2 | Elliptic; 6; 3 | Elliptic; 6; 3 | agrees | 4.4×10⁻⁶ |  |
| 2.83 | Elliptic; 6; 3 | Elliptic; 6; 3 | agrees | 8.7×10⁻⁶ |  |
| 4 | Elliptic; 6; 3 | Elliptic; 6; 3 | agrees | 1.7×10⁻⁵ |  |
| 5.66 | Elliptic; 6; 3 | Elliptic; 6; 3 | agrees | 3.4×10⁻⁵ |  |
| 8 | Elliptic; 6; 3 | Elliptic; 6; 3 | agrees | 6.7×10⁻⁵ |  |
| 11.3 | Elliptic; 6; 3 | Elliptic; 6; 3 | agrees | 1.3×10⁻⁴ |  |
| 16 | not labelled | Elliptic; 6; 3 | unresolved | 2.5×10⁻⁴ | tested set at 2.79122e-15+3.51578j (+3): the set's count differs between cutoffs |
| 22.6 | Elliptic; 6; 3 | Elliptic; 6; 3 | agrees | 4.7×10⁻⁴ |  |
| 45.3 | not labelled | Elliptic; 6; 3 | unresolved | 1.6×10⁻³ | tested set at -7.05549e-16+3.23787j (+5): the set's count differs between cutoffs |
| 64 | not labelled | Elliptic; 6; 3 | unresolved | 2.8×10⁻³ | tested set at -2.67583e-15+3.03461j (+5): the set's count differs between cutoffs |
| 72 | Elliptic; 6; 3 | Elliptic; 6; 3 | agrees | 3.4×10⁻³ |  |

**T3/R5** (`R5`, 11131 s): K6 holds. 15 points ran at every cutoff, all accepted, and 14 are read; `ε = 16` ran unread, as registered. Every read point with `ε ≤ 2` agrees; above 2, 7 of 7 agree.

| `ε` | Here: type; `K`; `k_i⁻` | M8.15: type; `K`; `k_i⁻` | K6 | Aligned distance | The rule's reason |
|---|---|---|---|---|---|
| 0.25 | Elliptic; 6; 3 | Elliptic; 6; 3 | agrees | 4.9×10⁻⁸ |  |
| 0.354 | Elliptic; 6; 3 | Elliptic; 6; 3 | agrees | 9.8×10⁻⁸ |  |
| 0.5 | Elliptic; 6; 3 | Elliptic; 6; 3 | agrees | 2.0×10⁻⁷ |  |
| 0.707 | Elliptic; 6; 3 | Elliptic; 6; 3 | agrees | 3.9×10⁻⁷ |  |
| 1 | Elliptic; 6; 3 | Elliptic; 6; 3 | agrees | 7.7×10⁻⁷ |  |
| 1.41 | Elliptic; 6; 3 | Elliptic; 6; 3 | agrees | 1.5×10⁻⁶ |  |
| 2 | Elliptic; 6; 3 | Elliptic; 6; 3 | agrees | 3.0×10⁻⁶ |  |
| 2.83 | Elliptic; 6; 3 | Elliptic; 6; 3 | agrees | 5.9×10⁻⁶ |  |
| 4 | Elliptic; 6; 3 | Elliptic; 6; 3 | agrees | 1.1×10⁻⁵ |  |
| 5.66 | Elliptic; 6; 3 | Elliptic; 6; 3 | agrees | 2.2×10⁻⁵ |  |
| 8 | Elliptic; 6; 3 | Elliptic; 6; 3 | agrees | 4.1×10⁻⁵ |  |
| 11.3 | Elliptic; 6; 3 | Elliptic; 6; 3 | agrees | 7.6×10⁻⁵ |  |
| 22.6 | Hyperbolic; 4; 1 | Hyperbolic; 4; 1 | agrees | 2.2×10⁻⁴ |  |
| 32 | Hyperbolic; 3; 0 | Hyperbolic; 3; 0 | agrees | 3.5×10⁻⁴ |  |

**T5/R2** (`R2`, 2710 s): K6 holds. 18 points ran at every cutoff, all accepted, and 17 are read; `ε = 45.3` ran unread, as registered. Every read point with `ε ≤ 2` agrees; above 2, 2 of 10 agree, and 8 read Unresolved.

| `ε` | Here: type; `K`; `k_i⁻` | M8.15: type; `K`; `k_i⁻` | K6 | Aligned distance | The rule's reason |
|---|---|---|---|---|---|
| 0.25 | Elliptic; 6; 3 | Elliptic; 6; 3 | agrees | 2.6×10⁻⁷ |  |
| 0.354 | Elliptic; 6; 3 | Elliptic; 6; 3 | agrees | 5.1×10⁻⁷ |  |
| 0.5 | Elliptic; 6; 3 | Elliptic; 6; 3 | agrees | 1.0×10⁻⁶ |  |
| 0.707 | Elliptic; 6; 3 | Elliptic; 6; 3 | agrees | 2.0×10⁻⁶ |  |
| 1 | Elliptic; 6; 3 | Elliptic; 6; 3 | agrees | 4.0×10⁻⁶ |  |
| 1.41 | Elliptic; 6; 3 | Elliptic; 6; 3 | agrees | 8.0×10⁻⁶ |  |
| 2 | Elliptic; 6; 3 | Elliptic; 6; 3 | agrees | 1.6×10⁻⁵ |  |
| 2.83 | Elliptic; 6; 3 | Elliptic; 6; 3 | agrees | 3.1×10⁻⁵ |  |
| 4 | Elliptic; 6; 3 | Elliptic; 6; 3 | agrees | 6.1×10⁻⁵ |  |
| 5.66 | not labelled | Elliptic; 6; 3 | unresolved | 1.2×10⁻⁴ | partner set at 3.20878e-15+5.77121j (+1): the set's count differs between cutoffs |
| 8 | not labelled | Elliptic; 6; 3 | unresolved | 2.2×10⁻⁴ | partner set at 2.66246e-15+5.67184j (+1): the set's count differs between cutoffs |
| 11.3 | not labelled | Elliptic; 6; 3 | unresolved | 4.2×10⁻⁴ | partner set at -2.07388e-15+5.53882j (+1): the set's count differs between cutoffs |
| 16 | not labelled | Elliptic; 6; 3 | unresolved | 7.7×10⁻⁴ | partner set at -1.84007e-15+5.36336j (+1): non-contracting above the floor |
| 22.6 | not labelled | Elliptic; 6; 3 | unresolved | 1.4×10⁻³ | partner set at 1.67077e-16+5.13822j (+1): non-contracting above the floor |
| 32 | not labelled | Elliptic; 6; 3 | unresolved | 2.3×10⁻³ | partner set at 2.26776e-15+4.85989j (+1): non-contracting above the floor; tested set at 8.02228e-16+0.436471j (+1): the set's count differs between cutoffs |
| 64 | not labelled | Elliptic; 6; 3 | unresolved | 5.4×10⁻³ | tested group at -2.15883e-15+0.481689j: non-contracting above the floor; tested group at 1.05424e-15+0.39386j: non-contracting above the floor; tested set at -2.20149e-15+0.606222j (+2): the set's count differs between cutoffs |
| 90.5 | not labelled | Elliptic; 6; 3 | unresolved | 7.7×10⁻³ | partner set at 1.34931e-15+3.80019j (+1): the set's count differs between cutoffs; structure: the type, indices, V0 or Krein counts differ along the ladder; tested group at 2.8818e-15+0.263559j: non-contracting above the floor; tested set at -1.03234e-14+0.527107j (+2): the set's count differs between cutoffs |

## 6. T5's second member, T5J/R2

Scored for that member alone (506 s). Each of its three groups under the bar reads Unresolved by check 1 at `ε = 0.25`, at `N = 16, 24` and 32 (§ 11).
- **At that point** the seed is checked, the point accepted, K1 holds and each group is matched. The convergence rule, which reads the point once from its three cutoffs, reads it Unresolved: "partner set at -1.36528e-15+6.01511j (+1): non-contracting above the floor". That Krein-positive set is each slow group's partner, its nearest imaginary group of opposite Krein sign, which the rule reads wherever it lies; the reason stands once for each of the three groups. Its change from `N = 24` to 32, 4.8×10⁻⁶, exceeds both its change from 16 to 24, 9.7×10⁻⁷, and the floor, 4.1×10⁻⁷. The slow groups' own rows in that reading converge, their relative change 1.15×10⁻⁹ at most.
- **K5 fails** on the same reading: convergence at `ε = 0.25` is its own clause.
- **At `ε = 0.5` and 1** the point converges, Elliptic with `(n(L), n(D), K) = (9, 3, 6)` as expected, and K1 holds.
- **Reported, unscored:** at `ε = 2` the rule reads Unresolved again: "partner set at 2.61485e-16+5.93353j (+1): the set's count differs between cutoffs".
- **Its `ε = 0.25` points** lie below the calibration's fitted range of `m` (§ 2), as T5/R2's do, which converge there.
- **Its outcome is its own** (the terms, § T5'S SECOND MEMBER). It stops nothing, and it neither carries nor takes the verdict on T5's registered member, which qualified.

## 7. The gate record and the verdict

- **`run/out/GATE.json`,** written at 2026-10-25T03:35:40Z: no stop; the controls and the pyramid complete; the instrument qualified; the `R5` gate passed.
- **`run/out/VERDICT.json`:** QUALIFIED, with K3's outcome "resolved". The rows it qualifies: T1/R4, T1/R5, T4/R4, T4/R5, T2/R4, T2/R5, T3/R4, T3/R5, T5/R2. The member not qualified: T5J/R2. The C3 ray: passed.

## 8. Deviations

- **None in the run.** It ran in the order the terms set, from the pinned tree, by the one command above.

## 9. Corrections

- **None.** The reading note in the maintainer's approval of the freeze block (§ 1) needs no change to it.

## 10. Follow-ups, outside M8.16.1

- **The census run,** under its own pre-registration, runs only the nine rows qualified here (the terms, § DEFINITION OF DONE). Its adequacy tests still apply at the Unresolved points of § 5 (the terms, § STATED LIMITS: WHAT IS ADDED).
- **T5's second member** is not offered to this instrument again (the terms, § THE VERDICT RULE: WHAT CHANGES). Why the partner set near `6.015i` does not contract at `ε = 0.25` is OPEN.
- **The margin behind check 1** is measured, not certified: a reading note of the approval of [#650](https://github.com/openwave-labs/openwave/pull/650), with no stronger rule asked. On this run T5/R2's three groups depart from `εκs_g + ε²c_g(N)` at `ε = 1` by at most 0.0951 of a ceiling, where an exchange of its two lowest needs `ε³` terms toward each other of 4.5 to 5.5 ceilings each (`DEVLOG.md` entry 44), at least 47 times more.

## 11. The next-order readings, every group at every cutoff

Each case's groups under the bar, by ascending `|s_g|`, as the terms' table orders them. At each cutoff: `c_g(N)`, and, where check 1 holds, `ĉ₂` and `ĉ₃`, all three over `κs_g`; the ceiling `C_g(N) = max(0.1 |c_g(N)|, 10⁻³ |κs_g|)` over `|κs_g|`; the four checks; and, reported and unscored as § THE NEXT-ORDER BAR asks, the two-term residual at `ε = 0.25`, `|λ_g − εκs_g − ε²c_g| / (ε|κs_g|)`, beside 1%, and the deviation from leading order at `ε = 0.25, 0.5` and 1. Check 1: each point accepted, its seed checked, K1, converged, and K2's matching against `εκs_g + ε²c_g(N)`. Check 2: the association, and `E_c` over `C_g(N)/10`, at most 1. Check 3: the spread `|ĉ₃ − ĉ₂|` over `C_g(N)`, at most 1. Check 4: `|c_g(N) − ĉ₃|` over `max(spread, 0.1 C_g(N))`, at most 1. A group passes when checks 1 to 4 hold at every cutoff.

**P5**

| Group | `N` | `c_g`; `ĉ₂`; `ĉ₃`, over `κs_g` | `C_g(N)` over `|κs_g|` | Check 1 | Check 2 | Check 3 | Check 4 | Two-term residual | Deviation from leading order | Reading |
|---|---|---|---|---|---|---|---|---|---|---|
| 1: quartet | 16 | −0.112895 − 0.206203 i; −0.113295 − 0.205594 i; −0.112988 − 0.206066 i | 0.024 | holds | 3.6×10⁻⁶, holds | 0.024, holds | 0.071, holds | 0.19% | 5.76%, 11.33%, 21.95% | pass |
| 1: quartet | 24 | −0.109831 − 0.20915 i; −0.110261 − 0.208494 i; −0.109933 − 0.209 i | 0.024 | holds | 8.6×10⁻⁶, holds | 0.026, holds | 0.077, holds | 0.20% | 5.78%, 11.35%, 21.95% |  |
| 1: quartet | 32 | −0.109831 − 0.20915 i; −0.110261 − 0.208494 i; −0.109933 − 0.209 i | 0.024 | holds | 1.5×10⁻⁵, holds | 0.026, holds | 0.077, holds | 0.20% | 5.78%, 11.35%, 21.95% |  |
| 2: imaginary pair, Krein-positive | 16 | −0.00460195; −0.00460276; −0.00460197 | 0.0010 | holds | 1.9×10⁻⁶, holds | 8.0×10⁻⁴, holds | 1.7×10⁻⁴, holds | 0.0010% | 0.12%, 0.23%, 0.48% | pass |
| 2: imaginary pair, Krein-positive | 24 | −0.00792389; −0.00792473; −0.00792391 | 0.0010 | holds | 4.6×10⁻⁶, holds | 8.2×10⁻⁴, holds | 2.2×10⁻⁴, holds | 0.0007% | 0.20%, 0.40%, 0.80% |  |
| 2: imaginary pair, Krein-positive | 32 | −0.00792389; −0.00792473; −0.00792391 | 0.0010 | holds | 8.3×10⁻⁶, holds | 8.2×10⁻⁴, holds | 2.2×10⁻⁴, holds | 0.0007% | 0.20%, 0.40%, 0.80% |  |

**C3R/R4**

| Group | `N` | `c_g`; `ĉ₂`; `ĉ₃`, over `κs_g` | `C_g(N)` over `|κs_g|` | Check 1 | Check 2 | Check 3 | Check 4 | Two-term residual | Deviation from leading order | Reading |
|---|---|---|---|---|---|---|---|---|---|---|
| 1: quartet | 16 | +0.055299 + 0.0902736 i; +0.0553968 + 0.0902617 i; +0.0552695 + 0.0902816 i | 0.011 | holds | 8.5×10⁻⁵, holds | 0.012, holds | 0.029, holds | 0.07% | 2.63%, 5.21%, 10.28% | pass |
| 1: quartet | 24 | +0.0540938 + 0.0900495 i; +0.0541721 + 0.0900395 i; +0.0540692 + 0.0900566 i | 0.011 | holds | 2.0×10⁻⁴, holds | 0.0099, holds | 0.024, holds | 0.07% | 2.61%, 5.18%, 10.22% |  |
| 1: quartet | 32 | +0.0540938 + 0.0900495 i; +0.0541721 + 0.0900395 i; +0.0540692 + 0.0900566 i | 0.011 | holds | 3.7×10⁻⁴, holds | 0.0099, holds | 0.024, holds | 0.07% | 2.61%, 5.18%, 10.22% |  |
| 2: imaginary pair, Krein-negative | 16 | −0.0157961; −0.0158416; −0.0157879 | 0.0016 | holds | 3.5×10⁻⁶, holds | 0.034, holds | 0.052, holds | 0.04% | 0.36%, 0.64%, 0.96% | pass |
| 2: imaginary pair, Krein-negative | 24 | −0.0189471; −0.018986; −0.0189399 | 0.0019 | holds | 6.9×10⁻⁶, holds | 0.024, holds | 0.038, holds | 0.04% | 0.44%, 0.80%, 1.30% |  |
| 2: imaginary pair, Krein-negative | 32 | −0.0189471; −0.018986; −0.0189399 | 0.0019 | holds | 1.2×10⁻⁵, holds | 0.024, holds | 0.038, holds | 0.04% | 0.44%, 0.80%, 1.30% |  |
| 3: imaginary pair, Krein-positive | 16 | −0.00136602; −0.00137022; −0.00136613 | 0.0010 | holds | 2.5×10⁻⁶, holds | 0.0041, holds | 0.0011, holds | 0.0016% | 0.04%, 0.07%, 0.16% | pass |
| 3: imaginary pair, Krein-positive | 24 | −0.00449803; −0.00450204; −0.00449817 | 0.0010 | holds | 6.0×10⁻⁶, holds | 0.0039, holds | 0.0014, holds | 0.0014% | 0.11%, 0.23%, 0.47% |  |
| 3: imaginary pair, Krein-positive | 32 | −0.00449803; −0.00450204; −0.00449817 | 0.0010 | holds | 1.1×10⁻⁵, holds | 0.0039, holds | 0.0014, holds | 0.0014% | 0.11%, 0.23%, 0.47% |  |

**T1/R4**

| Group | `N` | `c_g`; `ĉ₂`; `ĉ₃`, over `κs_g` | `C_g(N)` over `|κs_g|` | Check 1 | Check 2 | Check 3 | Check 4 | Two-term residual | Deviation from leading order | Reading |
|---|---|---|---|---|---|---|---|---|---|---|
| 1: imaginary pair, Krein-negative | 16 | −0.0293849; −0.0293829; −0.0293849 | 0.0029 | holds | 4.9×10⁻⁵, holds | 6.6×10⁻⁴, holds | 1.4×10⁻⁴, holds | 0.0045% | 0.73%, 1.45%, 2.87% | pass |
| 1: imaginary pair, Krein-negative | 24 | −0.0306976; −0.0306954; −0.0306976 | 0.0031 | holds | 1.1×10⁻⁴, holds | 7.1×10⁻⁴, holds | 1.6×10⁻⁴, holds | 0.0048% | 0.76%, 1.52%, 2.99% |  |
| 1: imaginary pair, Krein-negative | 32 | −0.0306976; −0.0306954; −0.0306976 | 0.0031 | holds | 2.0×10⁻⁴, holds | 7.1×10⁻⁴, holds | 1.5×10⁻⁴, holds | 0.0048% | 0.76%, 1.52%, 2.99% |  |
| 2: imaginary pair, Krein-positive | 16 | −0.0026187; −0.00261996; −0.00261873 | 0.0010 | holds | 2.0×10⁻⁶, holds | 0.0012, holds | 3.2×10⁻⁴, holds | 0.0017% | 0.07%, 0.14%, 0.29% | pass |
| 2: imaginary pair, Krein-positive | 24 | −0.00416477; −0.00416618; −0.00416481 | 0.0010 | holds | 4.8×10⁻⁶, holds | 0.0014, holds | 3.9×10⁻⁴, holds | 0.0017% | 0.11%, 0.21%, 0.44% |  |
| 2: imaginary pair, Krein-positive | 32 | −0.00416477; −0.00416618; −0.00416481 | 0.0010 | holds | 8.6×10⁻⁶, holds | 0.0014, holds | 3.9×10⁻⁴, holds | 0.0017% | 0.11%, 0.21%, 0.44% |  |
| 3: imaginary pair, Krein-positive | 16 | −0.018164; −0.0181635; −0.018164 | 0.0018 | holds | 9.0×10⁻⁷, holds | 2.7×10⁻⁴, holds | 3.9×10⁻⁵, holds | 0.0017% | 0.45%, 0.90%, 1.79% | pass |
| 3: imaginary pair, Krein-positive | 24 | −0.0201379; −0.0201372; −0.0201379 | 0.0020 | holds | 1.9×10⁻⁶, holds | 3.3×10⁻⁴, holds | 5.1×10⁻⁵, holds | 0.0021% | 0.50%, 1.00%, 1.98% |  |
| 3: imaginary pair, Krein-positive | 32 | −0.0201379; −0.0201372; −0.0201379 | 0.0020 | holds | 3.5×10⁻⁶, holds | 3.3×10⁻⁴, holds | 5.1×10⁻⁵, holds | 0.0021% | 0.50%, 1.00%, 1.98% |  |
| 4: imaginary pair, Krein-positive | 16 | −0.0315831; −0.0315803; −0.031583 | 0.0032 | holds | 3.8×10⁻⁷, holds | 8.4×10⁻⁴, holds | 2.2×10⁻⁴, holds | 0.0053% | 0.78%, 1.56%, 3.08% | pass |
| 4: imaginary pair, Krein-positive | 24 | −0.0330517; −0.0330485; −0.0330516 | 0.0033 | holds | 8.6×10⁻⁷, holds | 9.3×10⁻⁴, holds | 2.6×10⁻⁴, holds | 0.0058% | 0.82%, 1.63%, 3.21% |  |
| 4: imaginary pair, Krein-positive | 32 | −0.0330517; −0.0330485; −0.0330516 | 0.0033 | holds | 1.6×10⁻⁶, holds | 9.3×10⁻⁴, holds | 2.6×10⁻⁴, holds | 0.0058% | 0.82%, 1.63%, 3.21% |  |
| 5: imaginary pair, Krein-positive | 16 | −0.0149448; −0.0149445; −0.0149448 | 0.0015 | holds | 6.6×10⁻⁷, holds | 2.2×10⁻⁴, holds | 3.2×10⁻⁵, holds | 0.0012% | 0.37%, 0.74%, 1.47% | pass |
| 5: imaginary pair, Krein-positive | 24 | −0.0166264; −0.016626; −0.0166264 | 0.0017 | holds | 1.4×10⁻⁶, holds | 2.6×10⁻⁴, holds | 3.7×10⁻⁵, holds | 0.0015% | 0.41%, 0.83%, 1.64% |  |
| 5: imaginary pair, Krein-positive | 32 | −0.0166264; −0.016626; −0.0166264 | 0.0017 | holds | 2.6×10⁻⁶, holds | 2.6×10⁻⁴, holds | 3.8×10⁻⁵, holds | 0.0015% | 0.41%, 0.83%, 1.64% |  |

**T1/R5**

| Group | `N` | `c_g`; `ĉ₂`; `ĉ₃`, over `κs_g` | `C_g(N)` over `|κs_g|` | Check 1 | Check 2 | Check 3 | Check 4 | Two-term residual | Deviation from leading order | Reading |
|---|---|---|---|---|---|---|---|---|---|---|
| 1: imaginary pair, Krein-negative | 16 | −0.0323578; −0.032356; −0.0323578 | 0.0032 | holds | 7.8×10⁻⁵, holds | 5.7×10⁻⁴, holds | 8.9×10⁻⁵, holds | 0.0048% | 0.80%, 1.60%, 3.16% | pass |
| 1: imaginary pair, Krein-negative | 24 | −0.0336794; −0.0336773; −0.0336794 | 0.0034 | holds | 1.8×10⁻⁴, holds | 6.2×10⁻⁴, holds | 1.0×10⁻⁴, holds | 0.0053% | 0.84%, 1.66%, 3.29% |  |
| 1: imaginary pair, Krein-negative | 32 | −0.0336794; −0.0336773; −0.0336794 | 0.0034 | holds | 3.2×10⁻⁴, holds | 6.2×10⁻⁴, holds | 1.0×10⁻⁴, holds | 0.0053% | 0.84%, 1.66%, 3.29% |  |
| 2: imaginary pair, Krein-positive | 16 | −0.0410768; −0.0410721; −0.0410767 | 0.0041 | holds | 8.5×10⁻⁷, holds | 0.0011, holds | 2.8×10⁻⁴, holds | 0.0084% | 1.02%, 2.02%, 3.98% | pass |
| 2: imaginary pair, Krein-positive | 24 | −0.0426299; −0.0426246; −0.0426298 | 0.0043 | holds | 2.0×10⁻⁶, holds | 0.0012, holds | 3.2×10⁻⁴, holds | 0.0091% | 1.06%, 2.10%, 4.12% |  |
| 2: imaginary pair, Krein-positive | 32 | −0.0426299; −0.0426246; −0.0426298 | 0.0043 | holds | 3.5×10⁻⁶, holds | 0.0012, holds | 3.2×10⁻⁴, holds | 0.0091% | 1.06%, 2.10%, 4.12% |  |
| 3: imaginary pair, Krein-positive | 16 | −0.0329856; −0.0329831; −0.0329855 | 0.0033 | holds | 8.7×10⁻⁷, holds | 7.4×10⁻⁴, holds | 1.6×10⁻⁴, holds | 0.0054% | 0.82%, 1.63%, 3.21% | pass |
| 3: imaginary pair, Krein-positive | 24 | −0.0349632; −0.0349602; −0.0349632 | 0.0035 | holds | 2.0×10⁻⁶, holds | 8.4×10⁻⁴, holds | 1.9×10⁻⁴, holds | 0.0061% | 0.87%, 1.72%, 3.40% |  |
| 3: imaginary pair, Krein-positive | 32 | −0.0349632; −0.0349602; −0.0349632 | 0.0035 | holds | 3.5×10⁻⁶, holds | 8.4×10⁻⁴, holds | 1.9×10⁻⁴, holds | 0.0061% | 0.87%, 1.72%, 3.40% |  |
| 4: imaginary pair, Krein-positive | 16 | −0.00632444; −0.00632502; −0.00632445 | 0.0010 | holds | 2.1×10⁻⁶, holds | 5.8×10⁻⁴, holds | 7.9×10⁻⁵, holds | 0.0009% | 0.16%, 0.32%, 0.65% | pass |
| 4: imaginary pair, Krein-positive | 24 | −0.00780072; −0.00780141; −0.00780073 | 0.0010 | holds | 5.0×10⁻⁶, holds | 6.8×10⁻⁴, holds | 1.2×10⁻⁴, holds | 0.0008% | 0.20%, 0.39%, 0.79% |  |
| 4: imaginary pair, Krein-positive | 32 | −0.00780072; −0.00780141; −0.00780073 | 0.0010 | holds | 9.1×10⁻⁶, holds | 6.7×10⁻⁴, holds | 1.1×10⁻⁴, holds | 0.0008% | 0.20%, 0.39%, 0.79% |  |
| 5: imaginary pair, Krein-positive | 16 | −0.0191069; −0.0191063; −0.0191069 | 0.0019 | holds | 9.1×10⁻⁷, holds | 3.3×10⁻⁴, holds | 6.3×10⁻⁵, holds | 0.0019% | 0.48%, 0.95%, 1.88% | pass |
| 5: imaginary pair, Krein-positive | 24 | −0.0207945; −0.0207937; −0.0207945 | 0.0021 | holds | 2.0×10⁻⁶, holds | 3.8×10⁻⁴, holds | 7.4×10⁻⁵, holds | 0.0023% | 0.52%, 1.03%, 2.04% |  |
| 5: imaginary pair, Krein-positive | 32 | −0.0207945; −0.0207937; −0.0207945 | 0.0021 | holds | 3.6×10⁻⁶, holds | 3.8×10⁻⁴, holds | 7.4×10⁻⁵, holds | 0.0023% | 0.52%, 1.03%, 2.04% |  |

**T4/R4**

| Group | `N` | `c_g`; `ĉ₂`; `ĉ₃`, over `κs_g` | `C_g(N)` over `|κs_g|` | Check 1 | Check 2 | Check 3 | Check 4 | Two-term residual | Deviation from leading order | Reading |
|---|---|---|---|---|---|---|---|---|---|---|
| 1: imaginary pair, Krein-negative | 16 | −0.120026; −0.120137; −0.120038 | 0.012 | holds | 7.6×10⁻⁴, holds | 0.0083, holds | 0.0099, holds | 0.02% | 3.02%, 6.07%, 12.23% | pass |
| 1: imaginary pair, Krein-negative | 24 | −0.113972; −0.114075 − 7.8709e-09 i; −0.113984 − 1.18851e-08 i | 0.011 | holds | 0.0019, holds | 0.0080, holds | 0.011, holds | 0.01% | 2.86%, 5.75%, 11.55% |  |
| 1: imaginary pair, Krein-negative | 32 | −0.113972; −0.114075 − 3.14917e-09 i; −0.113984 − 3.47603e-09 i | 0.011 | holds | 0.0035, holds | 0.0080, holds | 0.010, holds | 0.01% | 2.86%, 5.75%, 11.55% |  |
| 2: imaginary pair, Krein-negative | 16 | +0.0175212; +0.0175175; +0.0175205 | 0.0018 | holds | 3.7×10⁻⁵, holds | 0.0017, holds | 0.0042, holds | 0.0014% | 0.44%, 0.88%, 1.78% | pass |
| 2: imaginary pair, Krein-negative | 24 | +0.0151491; +0.0151458; +0.0151484 | 0.0015 | holds | 1.0×10⁻⁴, holds | 0.0017, holds | 0.0047, holds | 0.0011% | 0.38%, 0.76%, 1.53% |  |
| 2: imaginary pair, Krein-negative | 32 | +0.0151491; +0.0151458; +0.0151484 | 0.0015 | holds | 1.9×10⁻⁴, holds | 0.0017, holds | 0.0047, holds | 0.0011% | 0.38%, 0.76%, 1.53% |  |
| 3: imaginary pair, Krein-negative | 16 | −0.0654372; −0.0654304; −0.065437 | 0.0065 | holds | 1.1×10⁻⁶, holds | 0.0010, holds | 3.1×10⁻⁴, holds | 0.03% | 1.61%, 3.17%, 6.13% | pass |
| 3: imaginary pair, Krein-negative | 24 | −0.0678847; −0.0678761; −0.0678845 | 0.0068 | holds | 2.5×10⁻⁶, holds | 0.0012, holds | 3.5×10⁻⁴, holds | 0.03% | 1.67%, 3.29%, 6.36% |  |
| 3: imaginary pair, Krein-negative | 32 | −0.0678847; −0.0678761; −0.0678845 | 0.0068 | holds | 4.6×10⁻⁶, holds | 0.0012, holds | 3.5×10⁻⁴, holds | 0.03% | 1.67%, 3.29%, 6.36% |  |
| 4: imaginary pair, Krein-positive | 16 | −0.00495022; −0.00495171; −0.0049503 | 0.0010 | holds | 2.2×10⁻⁶, holds | 0.0014, holds | 7.8×10⁻⁴, holds | 0.0032% | 0.13%, 0.26%, 0.55% | pass |
| 4: imaginary pair, Krein-positive | 24 | −0.00801725; −0.00801891; −0.00801733 | 0.0010 | holds | 5.3×10⁻⁶, holds | 0.0016, holds | 8.4×10⁻⁴, holds | 0.0028% | 0.20%, 0.41%, 0.85% |  |
| 4: imaginary pair, Krein-positive | 32 | −0.00801725; −0.00801891; −0.00801733 | 0.0010 | holds | 9.5×10⁻⁶, holds | 0.0016, holds | 8.4×10⁻⁴, holds | 0.0028% | 0.20%, 0.41%, 0.85% |  |

**T4/R5**

| Group | `N` | `c_g`; `ĉ₂`; `ĉ₃`, over `κs_g` | `C_g(N)` over `|κs_g|` | Check 1 | Check 2 | Check 3 | Check 4 | Two-term residual | Deviation from leading order | Reading |
|---|---|---|---|---|---|---|---|---|---|---|
| 1: imaginary pair, Krein-negative | 16 | +0.233765; +0.233748 − 9.95241e-09 i; +0.233775 − 1.42941e-08 i | 0.023 | holds | 6.8×10⁻⁴, holds | 0.0012, holds | 0.0042, holds | 0.20% | 5.65%, 10.91%, 20.26% | pass |
| 1: imaginary pair, Krein-negative | 24 | +0.23999; +0.239951 + 6.75388e-09 i; +0.239999 + 9.22377e-09 i | 0.024 | holds | 0.0016, holds | 0.0020, holds | 0.0040, holds | 0.21% | 5.79%, 11.16%, 20.66% |  |
| 1: imaginary pair, Krein-negative | 32 | +0.23999; +0.239951 + 5.88092e-09 i; +0.24 + 6.59527e-09 i | 0.024 | holds | 0.0029, holds | 0.0020, holds | 0.0040, holds | 0.21% | 5.79%, 11.16%, 20.66% |  |
| 2: imaginary pair, Krein-negative | 16 | −0.058983; −0.0589667; −0.0589828 | 0.0059 | holds | 1.8×10⁻⁵, holds | 0.0027, holds | 2.6×10⁻⁴, holds | 0.01% | 1.46%, 2.90%, 5.70% | pass |
| 2: imaginary pair, Krein-negative | 24 | −0.0616253; −0.0616078; −0.061625 | 0.0062 | holds | 4.2×10⁻⁵, holds | 0.0028, holds | 3.9×10⁻⁴, holds | 0.01% | 1.53%, 3.03%, 5.95% |  |
| 2: imaginary pair, Krein-negative | 32 | −0.0616253; −0.0616078; −0.061625 | 0.0062 | holds | 7.6×10⁻⁵, holds | 0.0028, holds | 3.9×10⁻⁴, holds | 0.01% | 1.53%, 3.03%, 5.95% |  |
| 3: imaginary pair, Krein-negative | 16 | +0.0170735; +0.0171008; +0.0170747 | 0.0017 | holds | 7.0×10⁻⁶, holds | 0.015, holds | 0.0071, holds | 0.02% | 0.44%, 0.92%, 1.95% | pass |
| 3: imaginary pair, Krein-negative | 24 | +0.0143517; +0.0143811; +0.0143531 | 0.0014 | holds | 2.0×10⁻⁵, holds | 0.019, holds | 0.0095, holds | 0.02% | 0.38%, 0.78%, 1.68% |  |
| 3: imaginary pair, Krein-negative | 32 | +0.0143517; +0.0143811; +0.0143531 | 0.0014 | holds | 3.6×10⁻⁵, holds | 0.019, holds | 0.0095, holds | 0.02% | 0.38%, 0.78%, 1.68% |  |
| 4: imaginary pair, Krein-positive | 16 | −0.0197323; −0.0197363; −0.0197326 | 0.0020 | holds | 1.9×10⁻⁶, holds | 0.0019, holds | 0.0013, holds | 0.0003% | 0.49%, 0.99%, 1.98% | pass |
| 4: imaginary pair, Krein-positive | 24 | −0.0231059; −0.02311; −0.0231062 | 0.0023 | holds | 3.8×10⁻⁶, holds | 0.0016, holds | 0.0012, holds | 0.0004% | 0.58%, 1.15%, 2.30% |  |
| 4: imaginary pair, Krein-positive | 32 | −0.0231059; −0.02311; −0.0231062 | 0.0023 | holds | 6.9×10⁻⁶, holds | 0.0016, holds | 0.0012, holds | 0.0004% | 0.58%, 1.15%, 2.30% |  |

**T5J/R2**

| Group | `N` | `c_g`; `ĉ₂`; `ĉ₃`, over `κs_g` | `C_g(N)` over `|κs_g|` | Check 1 | Check 2 | Check 3 | Check 4 | Two-term residual | Deviation from leading order | Reading |
|---|---|---|---|---|---|---|---|---|---|---|
| 1: imaginary pair, Krein-negative | 16 | −0.0210247; not read | 0.0021 | fails at `ε = 0.25` | not read | not read | not read | not read | not read | Unresolved |
| 1: imaginary pair, Krein-negative | 24 | −0.0214702; not read | 0.0021 | fails at `ε = 0.25` | not read | not read | not read | not read | not read |  |
| 1: imaginary pair, Krein-negative | 32 | −0.0214702; not read | 0.0021 | fails at `ε = 0.25` | not read | not read | not read | not read | not read |  |
| 2: imaginary pair, Krein-negative | 16 | −0.0180491; not read | 0.0018 | fails at `ε = 0.25` | not read | not read | not read | not read | not read | Unresolved |
| 2: imaginary pair, Krein-negative | 24 | −0.018581; not read | 0.0019 | fails at `ε = 0.25` | not read | not read | not read | not read | not read |  |
| 2: imaginary pair, Krein-negative | 32 | −0.018581; not read | 0.0019 | fails at `ε = 0.25` | not read | not read | not read | not read | not read |  |
| 3: imaginary pair, Krein-negative | 16 | −0.0172354; not read | 0.0017 | fails at `ε = 0.25` | not read | not read | not read | not read | not read | Unresolved |
| 3: imaginary pair, Krein-negative | 24 | −0.0177909; not read | 0.0018 | fails at `ε = 0.25` | not read | not read | not read | not read | not read |  |
| 3: imaginary pair, Krein-negative | 32 | −0.0177909; not read | 0.0018 | fails at `ε = 0.25` | not read | not read | not read | not read | not read |  |

**T2/R4**

| Group | `N` | `c_g`; `ĉ₂`; `ĉ₃`, over `κs_g` | `C_g(N)` over `|κs_g|` | Check 1 | Check 2 | Check 3 | Check 4 | Two-term residual | Deviation from leading order | Reading |
|---|---|---|---|---|---|---|---|---|---|---|
| 1: imaginary pair, Krein-positive, double | 16 | −0.0502696; −0.0502638; −0.0502695 | 0.0050 | holds | 2.3×10⁻⁶, holds | 0.0011, holds | 1.2×10⁻⁴, holds | 0.0048% | 1.25%, 2.49%, 4.95% | pass |
| 1: imaginary pair, Krein-positive, double | 24 | −0.0532431; −0.0532369; −0.053243 | 0.0053 | holds | 5.2×10⁻⁶, holds | 0.0011, holds | 1.5×10⁻⁴, holds | 0.0059% | 1.33%, 2.64%, 5.23% |  |
| 1: imaginary pair, Krein-positive, double | 32 | −0.0532431; −0.0532369; −0.053243 | 0.0053 | holds | 9.3×10⁻⁶, holds | 0.0011, holds | 1.5×10⁻⁴, holds | 0.0059% | 1.33%, 2.64%, 5.23% |  |
| 2: imaginary pair, Krein-positive | 16 | −0.0149243; −0.0149235; −0.0149243 | 0.0015 | holds | 1.5×10⁻⁶, holds | 5.1×10⁻⁴, holds | 1.1×10⁻⁴, holds | 0.0018% | 0.37%, 0.74%, 1.46% | pass |
| 2: imaginary pair, Krein-positive | 24 | −0.0172923; −0.0172914; −0.0172923 | 0.0017 | holds | 3.2×10⁻⁶, holds | 5.5×10⁻⁴, holds | 1.2×10⁻⁴, holds | 0.0022% | 0.43%, 0.86%, 1.69% |  |
| 2: imaginary pair, Krein-positive | 32 | −0.0172923; −0.0172914; −0.0172923 | 0.0017 | holds | 5.8×10⁻⁶, holds | 5.5×10⁻⁴, holds | 1.2×10⁻⁴, holds | 0.0022% | 0.43%, 0.86%, 1.69% |  |

**T2/R5**

| Group | `N` | `c_g`; `ĉ₂`; `ĉ₃`, over `κs_g` | `C_g(N)` over `|κs_g|` | Check 1 | Check 2 | Check 3 | Check 4 | Two-term residual | Deviation from leading order | Reading |
|---|---|---|---|---|---|---|---|---|---|---|
| 1: imaginary pair, Krein-positive, double | 16 | +0.00135837; +0.00135145; +0.00135804 | 0.0010 | holds | 1.9×10⁻⁵, holds | 0.0066, holds | 0.0033, holds | 0.0048% | 0.03%, 0.05%, 0.06% | pass |
| 1: imaginary pair, Krein-positive, double | 24 | −0.00185628; −0.00186364; −0.00185665 | 0.0010 | holds | 4.5×10⁻⁵, holds | 0.0070, holds | 0.0037, holds | 0.0046% | 0.05%, 0.11%, 0.26% |  |
| 1: imaginary pair, Krein-positive, double | 32 | −0.00185628; −0.00186363; −0.00185665 | 0.0010 | holds | 8.2×10⁻⁵, holds | 0.0070, holds | 0.0037, holds | 0.0046% | 0.05%, 0.11%, 0.26% |  |
| 2: imaginary pair, Krein-positive | 16 | −0.00868442; −0.00868405; −0.00868441 | 0.0010 | holds | 3.9×10⁻⁶, holds | 3.6×10⁻⁴, holds | 1.4×10⁻⁴, holds | 0.0004% | 0.22%, 0.43%, 0.86% | pass |
| 2: imaginary pair, Krein-positive | 24 | −0.0112677; −0.0112672; −0.0112677 | 0.0011 | holds | 8.2×10⁻⁶, holds | 4.0×10⁻⁴, holds | 1.4×10⁻⁴, holds | 0.0008% | 0.28%, 0.56%, 1.11% |  |
| 2: imaginary pair, Krein-positive | 32 | −0.0112677; −0.0112672; −0.0112677 | 0.0011 | holds | 1.5×10⁻⁵, holds | 4.0×10⁻⁴, holds | 1.4×10⁻⁴, holds | 0.0008% | 0.28%, 0.56%, 1.11% |  |

**T3/R4**

| Group | `N` | `c_g`; `ĉ₂`; `ĉ₃`, over `κs_g` | `C_g(N)` over `|κs_g|` | Check 1 | Check 2 | Check 3 | Check 4 | Two-term residual | Deviation from leading order | Reading |
|---|---|---|---|---|---|---|---|---|---|---|
| 1: imaginary pair, Krein-negative, double | 16 | +0.00840142; +0.00840042; +0.00840139 | 0.0010 | holds | 2.3×10⁻⁶, holds | 9.8×10⁻⁴, holds | 3.1×10⁻⁴, holds | 0.0020% | 0.21%, 0.41%, 0.81% | pass |
| 1: imaginary pair, Krein-negative, double | 24 | +0.004905; +0.00490393; +0.00490497 | 0.0010 | holds | 5.5×10⁻⁶, holds | 0.0010, holds | 3.2×10⁻⁴, holds | 0.0019% | 0.12%, 0.24%, 0.46% |  |
| 1: imaginary pair, Krein-negative, double | 32 | +0.004905; +0.00490393; +0.00490497 | 0.0010 | holds | 1.0×10⁻⁵, holds | 0.0010, holds | 3.2×10⁻⁴, holds | 0.0019% | 0.12%, 0.24%, 0.46% |  |
| 2: imaginary pair, Krein-negative | 16 | −0.008384; −0.0083846; −0.00838402 | 0.0010 | holds | 1.7×10⁻⁶, holds | 5.7×10⁻⁴, holds | 2.0×10⁻⁴, holds | 0.0003% | 0.21%, 0.42%, 0.84% | pass |
| 2: imaginary pair, Krein-negative | 24 | −0.0113879; −0.0113885; −0.0113879 | 0.0011 | holds | 3.7×10⁻⁶, holds | 5.0×10⁻⁴, holds | 1.9×10⁻⁴, holds | 0.0001% | 0.28%, 0.57%, 1.14% |  |
| 2: imaginary pair, Krein-negative | 32 | −0.0113879; −0.0113885; −0.0113879 | 0.0011 | holds | 6.6×10⁻⁶, holds | 5.1×10⁻⁴, holds | 1.9×10⁻⁴, holds | 0.0001% | 0.28%, 0.57%, 1.14% |  |

**T3/R5**

| Group | `N` | `c_g`; `ĉ₂`; `ĉ₃`, over `κs_g` | `C_g(N)` over `|κs_g|` | Check 1 | Check 2 | Check 3 | Check 4 | Two-term residual | Deviation from leading order | Reading |
|---|---|---|---|---|---|---|---|---|---|---|
| 1: imaginary pair, Krein-negative, double | 16 | −0.0488139; −0.0488134; −0.0488139 | 0.0049 | holds | 7.5×10⁻⁷, holds | 1.1×10⁻⁴, holds | 1.1×10⁻⁴, holds | 0.0004% | 1.22%, 2.44%, 4.88% | pass |
| 1: imaginary pair, Krein-negative, double | 24 | −0.0530714; −0.0530709; −0.0530714 | 0.0053 | holds | 1.6×10⁻⁶, holds | 1.0×10⁻⁴, holds | 1.2×10⁻⁴, holds | 0.0015% | 1.33%, 2.65%, 5.28% |  |
| 1: imaginary pair, Krein-negative, double | 32 | −0.0530714; −0.0530709; −0.0530714 | 0.0053 | holds | 3.0×10⁻⁶, holds | 1.0×10⁻⁴, holds | 1.2×10⁻⁴, holds | 0.0015% | 1.33%, 2.65%, 5.28% |  |
| 2: imaginary pair, Krein-negative | 16 | −0.0266862; −0.0266864; −0.0266862 | 0.0027 | holds | 1.0×10⁻⁶, holds | 9.0×10⁻⁵, holds | 4.7×10⁻⁵, holds | 0.0010% | 0.67%, 1.34%, 2.68% | pass |
| 2: imaginary pair, Krein-negative | 24 | −0.0303976; −0.030398; −0.0303976 | 0.0030 | holds | 2.2×10⁻⁶, holds | 1.2×10⁻⁴, holds | 2.7×10⁻⁵, holds | 0.0003% | 0.76%, 1.52%, 3.04% |  |
| 2: imaginary pair, Krein-negative | 32 | −0.0303976; −0.030398; −0.0303976 | 0.0030 | holds | 3.9×10⁻⁶, holds | 1.2×10⁻⁴, holds | 2.8×10⁻⁵, holds | 0.0003% | 0.76%, 1.52%, 3.04% |  |

**T5/R2**

| Group | `N` | `c_g`; `ĉ₂`; `ĉ₃`, over `κs_g` | `C_g(N)` over `|κs_g|` | Check 1 | Check 2 | Check 3 | Check 4 | Two-term residual | Deviation from leading order | Reading |
|---|---|---|---|---|---|---|---|---|---|---|
| 1: imaginary pair, Krein-negative | 16 | −0.0202035; −0.0202036; −0.0202035 | 0.0020 | holds | 3.0×10⁻⁷, holds | 2.0×10⁻⁵, holds | 1.2×10⁻⁶, holds | 0.0007% | 0.50%, 1.01%, 2.01% | pass |
| 1: imaginary pair, Krein-negative | 24 | −0.0206729; −0.0206728; −0.0206729 | 0.0021 | holds | 1.1×10⁻⁶, holds | 4.0×10⁻⁵, holds | 4.3×10⁻⁶, holds | 0.0012% | 0.52%, 1.03%, 2.05% |  |
| 1: imaginary pair, Krein-negative | 32 | −0.0206729; −0.0206728; −0.0206729 | 0.0021 | holds | 2.1×10⁻⁶, holds | 4.4×10⁻⁵, holds | 1.4×10⁻⁶, holds | 0.0012% | 0.52%, 1.03%, 2.05% |  |
| 2: imaginary pair, Krein-negative | 16 | −0.0192194; −0.0192195; −0.0192194 | 0.0019 | holds | 3.2×10⁻⁷, holds | 2.1×10⁻⁵, holds | 1.1×10⁻⁶, holds | 0.0007% | 0.48%, 0.96%, 1.91% | pass |
| 2: imaginary pair, Krein-negative | 24 | −0.0197174; −0.0197173; −0.0197174 | 0.0020 | holds | 1.2×10⁻⁶, holds | 4.5×10⁻⁵, holds | 4.2×10⁻⁶, holds | 0.0012% | 0.49%, 0.98%, 1.95% |  |
| 2: imaginary pair, Krein-negative | 32 | −0.0197174; −0.0197173; −0.0197174 | 0.0020 | holds | 2.3×10⁻⁶, holds | 4.9×10⁻⁵, holds | 1.3×10⁻⁶, holds | 0.0012% | 0.49%, 0.98%, 1.95% |  |
| 3: imaginary pair, Krein-negative | 16 | −0.0168049; −0.0168049; −0.0168049 | 0.0017 | holds | 3.2×10⁻⁷, holds | 1.3×10⁻⁵, holds | 3.2×10⁻⁶, holds | 0.0005% | 0.42%, 0.84%, 1.67% | pass |
| 3: imaginary pair, Krein-negative | 24 | −0.017373; −0.0173729; −0.017373 | 0.0017 | holds | 1.2×10⁻⁶, holds | 3.8×10⁻⁵, holds | 2.2×10⁻⁶, holds | 0.0009% | 0.43%, 0.87%, 1.72% |  |
| 3: imaginary pair, Krein-negative | 32 | −0.017373; −0.0173729; −0.017373 | 0.0017 | holds | 2.2×10⁻⁶, holds | 4.3×10⁻⁵, holds | 5.1×10⁻⁷, holds | 0.0009% | 0.43%, 0.87%, 1.72% |  |

## 12. Reproduction

`REPRODUCE.md` gives every command. For the run, from a copy of this folder:
- `shasum -a 256 -c SHA256SUMS`, the manifest against `run/MANIFEST_PIN`, and `python3 -I -B run/record_environment.py --check`;
- **the registered run:** `python3 -I -B -u run/driver.py`, in a copy without `run/out/`. It validates the committed freeze, `run/FROZEN.json` against `run/FROZEN_PIN`, and refuses a tree that differs from the manifest pin. In a copy that keeps this `run/out/`, it checks every case's outputs against the SHA-256 the log recorded and solves nothing; it writes the same verdict, with a new transcript and log;
- `python3 -I -B tools/build_record.py MIT_REPO --check`, which rebuilds this record from the files and reports any difference.

Bitwise agreement on another machine is not claimed: the terms read every scored quantity against margins far above round-off.
