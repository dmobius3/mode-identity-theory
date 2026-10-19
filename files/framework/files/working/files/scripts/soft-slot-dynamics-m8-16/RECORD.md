# M8.16 run record

The record of M8.16's registered run on 2026-10-18, under the governing terms, `run/m8_16_task_details.md` (SHA-256 `86992a5f7a278d63…`), merged in OpenWave [#637](https://github.com/openwave-labs/openwave/pull/637), and the instrument frozen at MIT `c1ea8f2` with its manifest pin, `a5f4517360672bd6…`. The maintainer's go is [#637's comment](https://github.com/openwave-labs/openwave/pull/637#issuecomment-6253316435), and the freeze block is OpenWave's `research/m8_16/freeze_block.md`, merged in [#639](https://github.com/openwave-labs/openwave/pull/639). Every number below is read from the run's files in [`run/out/`](run/out/), and `tools/build_record.py` builds this record from them. The case files hold every point's full readings at every cutoff; this record gives each point's type, indices and deviations from leading order, and every check. The verdict is the one the driver wrote under the terms' verdict rule. Adjudication is the maintainer's.

**The outcome.** NOT QUALIFIED, failing K3 and K4, both on the pyramid, P5. The five controls passed every check. The pyramid's quartet lies 5.76%, 5.78% and 5.78% from Theorem R's leading order at `ε = 0.25`, at `N = 16, 24` and 32, over the bar of 5%, and that one reading fails both K4 and K3's part (a). The run stopped at the pyramid, as the terms require, and no census row ran.

## 1. Custody

- **The freeze.** `run/FROZEN.json` was written once, at 2026-10-18T19:15:37Z, by `run/write_guard.py`, after the go. It holds the allowlist of 15 cases, the frozen values, the terms' SHA-256, the manifest's SHA-256 and the go, and the SHA-256 of M8.15's 5 target records, which it copied into `reference/m815_targets/` after each blob id matched the one named before the freeze. Its own SHA-256 is `run/FROZEN_PIN`. The freeze block carries it in full.
- **Before the run,** read-only: `devtools.frozen()` validated the freeze, the tree against the manifest pin, the terms and the target records; `run/record_environment.py --check` found no difference from `run/ENVIRONMENT.json`; and `run/out/` did not exist.
- **The run.** `python3 -I -B -u run/driver.py`, from this folder, its output to `run/out/driver.log`, on mains power at its launch (read at 2026-10-18T21:44:50Z, `DEVLOG.md` entry 330), with sleep held off for its length, in the recorded environment: Python 3.13.13, NumPy 2.5.0 and SciPy 1.18.0, on Accelerate's BLAS and LAPACK as each reports them, under macOS 15.8 (24H23) on one Apple M3. It started at 2026-10-18T21:44:54Z and wrote its verdict at 2026-10-18T23:22:34Z, 5860 s later, equal to its own clock. Its log, `run/out/RUNLOG.json`, records the manifest's SHA-256 at the start, equal to `run/MANIFEST_PIN`, and each completed case's outputs with their SHA-256.
- **After the run:** every output equals the SHA-256 the log recorded; `devtools.frozen()` validates; and the environment, read again, equals `run/ENVIRONMENT.json`.
- **Post-run files.** These files beside this record were made after the run, and are not records from it:
  - `environment_postrun_2026-10-18.txt`: `run/record_environment.py --check`, read after the run, with no difference;
  - `tools/p5_extrapolation.py` and its output, `tools/p5_extrapolation.out`: the pyramid's slow eigenvalues extrapolated to zero amplitude, unscored (§ 3);
  - `tools/build_record.py`, which builds this record from the files and, with `--check`, reports any difference.
- **The run's files.** `run/out/driver.log` is the run's standard output and error, and equals `run/out/driver.out`, the transcript the driver wrote. The target records are M8.15's, copied at the freeze.

  | File | SHA-256 |
  |---|---|
  | `run/out/C1.json` | `8a91e9aa3abcec24512e983b65ce413130dd633180ba2f282b7a5987e2cbe4bc` |
  | `run/out/C2a.json` | `f7441cf3d3d826dc4734f7490d2eb5dd426e3693ef950b8aeca3fdb69df71c34` |
  | `run/out/C2b.json` | `d5a2e872cae8cbff8232772291b4d9103973bc5c1fb9c3f967c4dbcd9d7252f0` |
  | `run/out/C3.json` | `f599204030edddc2a8e2020042b9fb37700cbb14fd2929d0c4b98dda4d83b733` |
  | `run/out/C2a_R5.json` | `db83da0ca3f042ad0178cf679b26df53f16e6daf75eef23355b4fb96295c5082` |
  | `run/out/P5.json` | `dceba2fd5fbacf950d49abfe6b5f21fb3c2f8c8aa5d0defe64d2f12aa4ceddb2` |
  | `run/out/P5.npz` | `64ea832e06882ba39f2a649977edb3496c900a8c79b9e20d46b2506f782e8aab` |
  | `run/out/GATE.json` | `88d1fdffb65e2497ac41c124c239e6233b3b470a7867de42c8d717736773081c` |
  | `run/out/VERDICT.json` | `796cf7f098b2defc48966f9fddbfe26a724d8b71b47bfca11157e77f07311f84` |
  | `run/out/driver.out` | `81422ed69d72e1f3e13e3b52c862e58b89345b9f8326ec2f417db3b69147652c` |
  | `run/out/driver.log` | `81422ed69d72e1f3e13e3b52c862e58b89345b9f8326ec2f417db3b69147652c` |
  | `run/out/RUNLOG.json` | `d9a9f812b9f8df4a48a5ada40d73cbcf76a3662515ae69f0de3c8d9beb285a4b` |
  | `run/FROZEN.json` | `ce685c8336b43fad28f279ce3198be654c712c60c9b38fac0e3bc357af56c852` |
  | `reference/m815_targets/branch_T2_R4.json` | `5b1758c9ec1c6566091fe9028a542f67fd6bd0ad51c927f7147d54c07d876b49` |
  | `reference/m815_targets/branch_T2_R5.json` | `a064683298ebc922ecbba06316a3af11b68a7b6193e7e04c63eaa9fc1ad931ba` |
  | `reference/m815_targets/branch_T3_R4.json` | `fe3497a3a4de45a5f3a6d2ce2a6c322feb5399610ad20d9da530acd8abdf3bc2` |
  | `reference/m815_targets/branch_T3_R5.json` | `660d0322d1921bb7b6c9e7e1b71bf3c54bea63a6c17a754e22582601b49aaee4` |
  | `reference/m815_targets/branch_T5_R2.json` | `6bcdb5cfd58980bf228b4c84271e51d1e6efa5b6052b0fd6cf98cce143a5884f` |

  The post-run files:

  | File | SHA-256 |
  |---|---|
  | `environment_postrun_2026-10-18.txt` | `5e12e201d9fa970e9ccc7db1ad32778c5f50d4a6014ba45bf6e42a0be7554390` |
  | `tools/p5_extrapolation.py` | `f3771710254ad6bfcfb6ca7b798399cb3107aac1c9445d2ff0ca821c45729f54` |
  | `tools/p5_extrapolation.out` | `50ac607444fcde336f5a7c69fad82786e9cb0f94ca9ae7ead6a9f4dd868befea` |
  | `tools/build_record.py` | `2fa312b11144ec68f3ded3e541ba0f1faa93f60cbdea578d0f4ca5af90a4bcb3`, as it built this record |

## 2. The controls

Each control ran every point and cutoff the terms set, each cutoff from its own seed. All 19 seeds of the run passed their check: every `Q(u)` within 3×10⁻¹⁵ of its exact value, relative, and every criticality at most 3×10⁻¹⁵, against `10⁻¹²`, and every `(k, r_u)` the Result's. Quantities at the round-off level are given as bounds. Every point's `m = ‖φ‖²` lies inside the range the calibration was fitted on, `0.204` to `132`: from 0.2043 to 2.0000, read from each point's margin.

**C1, Theorem D at the rigid slot `R3`** (726 s). The exact branch, `c = √ε v`, `λ = λ₀ + ‖c‖²`, with no solve, at `ε ∈ {0.5, 1, 2}` and `N = 16, 24, 32` and 40. At all 12 points the residual is at most 3×10⁻¹⁶ of the size, against `10⁻¹⁵`; the cubic's part off the lowest level at most 2×10⁻¹⁵, against `10⁻¹⁴`; and the lowest level's spectrum Theorem D's to 4×10⁻¹⁴ relative, against `10⁻¹⁰`. Every point is Elliptic, `(n(L), n(D), K) = (0, 0, 0)`, with `V₀` as expected, and the type, `n(L)`, `K` and those eigenvalues are unchanged in `N` to `10⁻¹²`. K1 and K4 pass.

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

- **C2a** (`R4`, 846 s): K1 passes, K2 passes, and K4 passes. The largest deviation from leading order is 0.70%, 0.73%, 0.73% at `ε = 0.25` and 5.40%, 5.59%, 5.59% at `ε = 2`, at `N = 16, 24` and 32. Every floor is below 10⁻¹⁶, every tangent residual below 0.2 u, and every zero cluster below 0.03 of its margin. Beside the rule, unscored, the largest relative change between the two highest cutoffs is at most 2×10⁻⁹, within the retired fraction `10⁻⁶`.
- **C2b** (`R2`, 353 s): K1 passes, K2 passes, and K4 passes. The largest deviation from leading order is 0.39%, 0.46%, 0.46% at `ε = 0.25` and 3.07%, 3.56%, 3.56% at `ε = 2`, at `N = 16, 24` and 32. Every floor is below 10⁻¹⁶, every tangent residual below 5 u, and every zero cluster below 0.04 of its margin. Beside the rule, unscored, the largest relative change between the two highest cutoffs is at most 4×10⁻⁸, within the retired fraction `10⁻⁶`.
- **C3** (`R4`, 1124 s): K1 passes, and K4 passes. The largest deviation from leading order is 0.45%, 0.51%, 0.51% at `ε = 0.25` and 3.47%, 3.96%, 3.96% at `ε = 2`, at `N = 16, 24` and 32. Every floor is below 10⁻¹⁶, every tangent residual below 0.10 u, and every zero cluster below 0.03 of its margin. Beside the rule, unscored, the largest relative change between the two highest cutoffs is at most 3×10⁻⁷, within the retired fraction `10⁻⁶`.
- **C2a/R5** (`R5`, 1584 s): K1 passes, and K4 passes. The largest deviation from leading order is 0.88%, 0.93%, 0.93% at `ε = 0.25` and 6.72%, 7.10%, 7.10% at `ε = 2`, at `N = 16, 24` and 32. Every floor is below 10⁻¹⁶, every tangent residual below 0.2 u, and every zero cluster below 0.02 of its margin. Beside the rule, unscored, the largest relative change between the two highest cutoffs is at most 7×10⁻¹⁰, within the retired fraction `10⁻⁶`. Its margin is an extrapolation: `R5` lies outside the slots the calibration was fitted on (the terms, § STATED LIMITS).

## 3. The pyramid, P5

P5 is `R4`'s pyramid, the first sealed case in the order (1227 s). Every point is accepted, at every cutoff, and K1 and K2 hold at every point: the slow band holds exactly the three predicted groups. Each group's deviation from Theorem R's leading order is given at `N = 16, 24` and 32.

| `ε` | Under K4 | Type; `(n(L), n(D), K)` | The in-span pair | The quartet | The Krein-positive pair | Aligned distance |
|---|---|---|---|---|---|---|
| 0.25 | scored | Hyperbolic; (5, 1, 4) | 0.28%, 0.35%, 0.35% | 5.76%, 5.78%, 5.78% | 0.12%, 0.20%, 0.20% | 8.6×10⁻⁸ |
| 0.5 | reported, unscored | Hyperbolic; (5, 1, 4) | 0.56%, 0.69%, 0.69% | 11.33%, 11.35%, 11.35% | 0.23%, 0.40%, 0.40% | 3.4×10⁻⁷ |
| 1 | reported, unscored | Hyperbolic; (5, 1, 4) | 1.12%, 1.38%, 1.38% | 21.95%, 21.95%, 21.95% | 0.48%, 0.80%, 0.80% | 1.4×10⁻⁶ |
| 2 | reported, unscored | Hyperbolic; (5, 1, 4) | 2.24%, 2.75%, 2.75% | 41.66%, 41.50%, 41.50% | 0.98%, 1.63%, 1.63% | 5.3×10⁻⁶ |

Every floor is below 10⁻¹⁶, every tangent residual below 0.2 u, every zero cluster below 0.04 of its margin, and every `ε` converged. Beside the rule, unscored, the largest relative change between the two highest cutoffs is at most 2×10⁻⁸, 1×10⁻⁷, 7×10⁻⁷, 6×10⁻⁶ at `ε = 0.25, 0.5, 1` and 2, above the retired fraction `10⁻⁶` at `ε = 2`.

**K3 at `ε = 0.25`,** at every cutoff:

| `N` | (a) the kernel, by `L`'s certificate | (a) the slow band outside the in-span class | (b) the in-span pair | (c) the static overlaps, XY and Z | (d) |
|---|---|---|---|---|---|
| 16 | holds: tangent residual below 0.03 u, `L`'s zero count 4 = the chains, gray zone empty | fails: the quartet 5.76% | holds: 0.28% | holds: 0.9970 and below 10⁻¹⁰; axis fraction 0.987 | holds |
| 24 | holds: tangent residual below 0.04 u, `L`'s zero count 4 = the chains, gray zone empty | fails: the quartet 5.78% | holds: 0.35% | holds: 0.9970 and below 10⁻⁹; axis fraction 0.987 | holds |
| 32 | holds: tangent residual below 0.02 u, `L`'s zero count 4 = the chains, gray zone empty | fails: the quartet 5.78% | holds: 0.35% | holds: 0.9970 and below 10⁻⁹; axis fraction 0.987 | holds |

- **(a) fails at every cutoff,** on the quartet alone. K3's outcome is therefore "instrument failure: the diagnosis is untested": the terms list "the slow band departs from Theorem R outside the in-span pair" under the instrument failure.
- **The verdict rule's K3 sentence.** § THE VERDICT RULE says: "If K3 fails with the kernel exact, the record says that the diagnosis is wrong." Read alone, it would fit P5, whose kernel certificate holds while K3 fails. K3's own list defines that outcome as "(a) passes and (b), (c) or (d) fails", and lists a slow band that departs from Theorem R outside the in-span pair under the instrument failure. The driver follows K3's list, and so does this record; the sentence is noted here for the adjudication.
- **(b), (c) and (d) hold at every cutoff,** and decide nothing once (a) fails. (d) reads the group (b) finds at `N = 32`: converged, its distance to the nearest event, A's gray zone, 532 times its uncertainty.
- **K4 fails:** converged, Hyperbolic with `(5, 1, 4)` at every cutoff, and every seed passed, but the quartet is over the bar at every cutoff. The Krein-positive pair is within it, at 0.12%, 0.20%, 0.20%.

**Post-run, unscored** (`tools/p5_extrapolation.out`). Each group's eigenvalue over `ε`, extrapolated to `ε → 0` from the registered points, against Theorem R's `κsτ`, at `N = 32`:

| Group | At `ε = 0.25` | First order removed | Second order removed |
|---|---|---|---|
| the in-span pair | 0.35% | 0.001% | 0.0001% |
| the quartet | 5.78% | 0.355% | 0.0602% |
| the Krein-positive pair | 0.20% | 0.001% | 0.0001% |

## 4. The gate record and the verdict

- **`run/out/GATE.json`,** written at 2026-10-18T23:22:34Z: the stop "P5 failed K3, K4"; the controls and the pyramid complete; the instrument not qualified; the `R5` gate passed.
- **`run/out/VERDICT.json`:** NOT QUALIFIED, failing K3 and K4, both the pyramid's, with K3's outcome as above.
- **The rows did not run:** T1/R4, T1/R5, T4/R4, T4/R5, T2/R4, T2/R5, T3/R4, T3/R5, T5/R2. The row gate refuses a row until the gate record shows K1 to K4 passed, so K5 and K6 have no outcome.
- **A resume is refused:** the gate record names a stop.

## 5. Deviations

- **`FROZEN.json`'s values.** § FIXED AT THE FREEZE says `FROZEN.json` holds "the cutoffs and every frozen value above". Its values omit two items of § FROZEN VALUES: `D`'s cut `10⁻⁸ ‖B‖`, the literal at `instrument/linear.py:233`, and K3's axis guard `10⁻⁶`, `AXIS_MIN` at `run/checks.py:23`. The maintainer's approval of [#639](https://github.com/openwave-labs/openwave/pull/639) records it. Neither could move: the run reads its constants from the pinned code and never reads the values, and `devtools.frozen()` refuses a tree that differs from the manifest pin `FROZEN.json` carries. `FROZEN.json` is written once and stands as written. At adjudication the two values are read from the pinned code, as the approval says.
- **None in the run.** It ran in the order the terms set, from the pinned tree, by the one command above.

## 6. Corrections

- **The freeze block's seeds line.** It says that the instrument files `dev/seed_check.py` reads, seven named, are unchanged in the pinned tree. The seed check imports eleven: those seven and `__init__.py`, `devtools.py`, `newton.py` and `linear.py`. The maintainer's approval of [#639](https://github.com/openwave-labs/openwave/pull/639) records it. Against the hashes `DEVLOG.md` entry 269 logged at the seed check, ten of the twelve instrument files are unchanged at MIT `c1ea8f2`. Of the eleven read, only `linear.py` changed, by one line in `record()` that adds `l_resolved` to its output. The seed values never reach `record()`: the seed check's claim 5 makes it raise throughout the seed evaluation, and no sentinel fired. The seed values stand on the pinned code.

## 7. Follow-ups, outside M8.16

- **A revised instrument, or another qualification run,** is a new pre-registration under a new ID, as the terms' verdict rule requires.
- **The census rows** did not run. The census run runs only rows that a qualification qualifies.
- **The quartet at `ε = 0.25`.** The post-run reading of § 3 is unscored. How a bar at the smallest amplitude allows for a mode's next-order term is for a later pre-registration to settle.

## 8. Reproduction

`REPRODUCE.md` gives every command. For the run, from a copy of this folder:
- `shasum -a 256 -c SHA256SUMS`, the manifest against `run/MANIFEST_PIN`, and `python3 -I -B run/record_environment.py --check`;
- **the registered run:** `python3 -I -B -u run/driver.py`, in a copy without `run/out/`. It validates the committed freeze, `run/FROZEN.json` against `run/FROZEN_PIN`, and refuses a tree that differs from the manifest pin. In a copy that keeps this `run/out/`, it reads the log and refuses to resume, since the gate record names a stop;
- `python3 -I -B tools/p5_extrapolation.py`, which re-reads the pyramid's outputs;
- `python3 -I -B tools/build_record.py MIT_REPO --check`, which rebuilds this record from the files and reports any difference.

Bitwise agreement on another machine is not claimed: the terms read every scored quantity against margins far above round-off.
