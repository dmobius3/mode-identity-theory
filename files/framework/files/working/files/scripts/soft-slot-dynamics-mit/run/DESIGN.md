# MIT's own computation: the design

*In the manifest, so the pin holds it. Everything here is written before any new solve.*

## 1. What this is

The sequel needs the values at the census's open items, so MIT computes them on its own side, as the census page's note of 2026-11-01 says and OpenWave's answer on #512 reads: the condition that nothing is repaired and rerun "does not reach what you compute in your own repository". Two rows beside them run too, T5J and the coherent row in `R5` (section 4). Neither is an open item in the census's catalog.

This is MIT's own computation. It is outside M8. Its code is off M8.16.1's pin, `8cc2d7e2d01a72fc3572adabf917656abf36cbddd70ed35532b73ae5451790dd`, so M8.16.1's qualification, the admission of 2026-10-15 and the adjudications of M8.17 and M8.18 do not carry to it. Its values take no part in S6, select no S5 stretch on OpenWave's record, are no M8 outcome and move no `MODELS.md` cell. On OpenWave's record the open items stay closed instrument-limited under S6.

## 2. What is and is not changed

Every file of `instrument/` and `run/` that M8.18's run used is here, and byte for byte M8.18's, except:
- `instrument/convergence.py`: the arm `same_resolution`, which is candidate A. Without the arm the rule is unchanged (`dev/test_regression.out`).

New files, none of which the solver imports:
- `run/changed.py`: candidate B, and the changed reading.
- `run/grid.py`: what is solved and read, and the pass marks.
- `run/jobs.py`, `run/runner.py`: one job at a time in its own process, side by side.
- `tools/pin.py`, `tools/inventory.py`, and what they write: `run/MANIFEST_PIN`, `run/FROZEN.json`, `run/FROZEN_PIN` and `SHA256SUMS`. `run/ENVIRONMENT.json` is this machine's reading, taken by M8.18's own `run/record_environment.py`.

**The solves do not touch the changes.** `branches`, `newton`, `functional`, `basis` and `certified` import neither `linear` nor `convergence`, and a solve runs inside `checks.withheld`, where every record path refuses. So no solve rests on A or B, and no spectrum exists until a read makes one.

**Tested before the pin, at the run's own setting** (`dev/runs/006_final_test/`). M8.18's six controls at `N = 24` and 32, solved again four at a time, equal its files in all 336 solve fields and 11,048 array entries. Its stored solutions at all three cutoffs, read again by this tree, equal its records at all 72 points, and the as-built readings, the readings beside them and both identities equal its own. The changed reading is converged at all 24 control points, moving exactly P5 and C3R/R4 at 0.25. The rule alone is tested on all 262 published readings (`dev/test_regression.out`), and the jobs' guards in `dev/test_jobs.out`. Every row and fresh point passes its admission and its seed's checks at `N = 24` and 40, with no solve (`dev/entries_check.out`).

## 3. The two changes

M8.18's control gate failed at two points, because two tolerances grow with the cutoff through ‖A‖ or ‖B‖, which grow about as `N²`, and each passed a feature that does not move.

**A: a set's members are compared at the top cutoff's linking distance at every cutoff.** `τ(λ) = max(margin, 10 sqrt(u ‖A‖ |λ|))` links two values into one group. At P5, `ε = 0.25`, a stable pair 1.1345×10⁻⁵ apart stayed two groups at `N = 24` and 32, and became one at `N = 40` alone, and the rule read the link as motion. A leaves every one-to-one match alone. It changes how a set's change is measured, and only for members within the top cutoff's `τ` of each other.

**B: n(D)'s gray zone is (10⁻⁸, 10⁻⁷) ‖B‖, a factor of 10 above its cut, as L's is, in place of the inherited factor of 1000.** At C3R/R4, `ε = 0.25`, D's eigenvalue -0.01596075 fell inside the old top at `N = 40` alone, by 2.3%. The cut stays, so `n(D)` and D's nullity cannot move. B moves only the flag.

**What they were chosen knowing.** Both were chosen knowing M8.18's gate failure, its 24 control readings and M8.17's stored readings at the twelve. All three. A preview ran over all 262 published readings, the twelve included, before this design (`dev/preview_fix.py`, `dev/preview_fix_all.out`). It changes none of M8.17's 115. Readings already on record are not new evidence for the changed code.

**What they reach.** Beyond M8.18's two failures, A moves T5J at `ε = 0.25`, a pair 8.78×10⁻⁶ apart merged at `N = 32` alone (`dev/t5j_tau.out`). That is P5's mechanism with one difference: T5J's members move by about 10⁻⁶ per rung, where P5's move by rounding. Its separation is 8.7839×10⁻⁶ at `N = 16` and 8.7801×10⁻⁶ at `N = 24`. `N = 32` stores none, since the pair is linked there and a read keeps only a linked group's centre, so after the note its members are measured at `N = 32` and 40, as `dev/runs/019_gate_cause/pair_gap.py` in M8.18's folder measured P5's, and whether the gap closes is reported beside any T5J verdict under A. M8.16.1's verdict on T5J stands. Any T5J verdict under A is MIT's own.

**Each point reports both verdicts.** As built and changed, side by side. Where they agree, that point rests on no changed code. The eigenvalues and the indices rest on none of it.

**Each tolerance at each rung's scale.** `dev/tolerances.out`, from M8.17's and M8.16.1's stored readings, before any solve: at 79 points with a record at `N = 32`, no neighbouring pair in the tested set lies between `τ(32)` and `τ(40)`, and none between `τ(32)` and `τ(48)`. The nearest stays 1.75 `τ(40)` away. A's zero cluster and L's gray zone stay at least 7 times and 2×10⁵ times clear. D's eigenvalues are not stored at any row, so the reads store them, and the as-built verdict there is reported beside the changed one.

## 4. What runs

The ladder is `N = 24`, 32 and 40, each cutoff on its own path from the seed. `N = 16` is not read. The rule's band is the level above `N = 16`, with the reading on the band above `N = 24` beside it, unscored, as M8.18's terms had it. Branch identity is read on both pairs, and its guard stays at 10⁻².

**Four jobs at a time,** longest first, with `VECLIB_MAXIMUM_THREADS` unset, as M8.18's run had it. Four gives about 2.1 times one job's throughput and six no more (`dev/runs/003_scaling/`), so the whole takes about a day and a half to two days (INFERRED). One thread leaves a solve unchanged but moves one record field at `N = 24` in its round-off (`dev/runs/005_leak/`), so the run keeps M8.18's setting. A job checkpoints after every point, and a killed job resumes equal to the path run through (`dev/test_jobs.out`).

| Entry | Grid | Why |
|---|---|---|
| `T1_R4` | 18 points to 72 | five of the twelve |
| `T4_R4` | 18 points to 72 | five of the twelve |
| `T1_R5` | 15 points to 32 | one of the twelve |
| `T5_R2` | 20 points to 132, and 11 added | 45.25, 128, 132, and where the index drop and the quartet sit |
| `T5J_R2` | 20 points to 132 | T5's second member |
| `C2a_R5` | 15 points to 32 | the coherent row's missing ladder; a known outcome for S5's pre-registration, which carries it |
| `fresh_*` | section 5 | read before any row |

**T5's added points** are 76, 100, 106, 112, 116, 120, 124, 126, 127, 129 and 130, chosen from M8.17's stored readings alone (section 6). They change the path into 128 and 132, so T5's `N = 24` and 32 readings above 90.51 are new solves, and the stored ones are known outcomes. If `m` at 128 from this finer path differs from the stored value beyond numerical tolerance, that is evidence of path dependence. Whether the coarse path stepped onto another solution remains OPEN.

**A failed step ends that path** at that point. The record says so. Nothing is rerun on another grid before the note.

**`N = 48`** is in reserve for T5's top, in `R2` alone, added by its own dated commit if `N = 40` leaves it open. The stored 24-to-32 distance already fails the identity guard at 128 and 132 by 3.6% and 6.2%, so a clean reading there may need 32, 40 and 48.

**T4/R4's locator** is M8.17's, `census_lib.settle`, on the bracket (2.83, 5.66), narrowed to (4, 5.66) if the read at 4 classifies it Elliptic. It runs on this ladder as M8.18's terms read M8.17's locator there: `N = 32` and 40 deciding, `N = 24` bisected where its ends' `n(L)` is resolved and different and reported otherwise, K1 asked at every midpoint, and a location is named only where both verdicts agree at its guard readings. It reads at its midpoints, so it runs after the note. Its job lands by its own dated commit.

## 5. Fresh controls, pass marks first

Amplitudes no record holds, next to the failures. Each is read before any row, and each passes only if it holds the case's own type and indices at all three cutoffs, K1, branch identity on both pairs, and both marks below.

| Point | As built | Changed | Why |
|---|---|---|---|
| P5, 0.24 | Unresolved, by a new link at `N = 40` alone | converged | its pair's gap falls between `τ(32)` and `τ(40)` for ε from about 0.230 to 0.258 |
| P5, 0.30 | converged | converged | outside that window |
| C3R/R4, 0.20 | Unresolved, by D's flag at `N = 40` alone | converged | D's eigenvalue falls between the two gray-zone tops for ε from about 0.159 to 0.256 |
| C3R/R4, 0.30 | converged | converged | outside that window |
| C2b, 0.30 | converged | converged | `R2`, no change expected |
| C2a/R5, 0.30 | converged | converged | `R5`, no change expected |

The two windows are INFERRED, from the stored gaps at 0.25 and 0.5 (`dev/runs/019_gate_cause` in M8.18's folder). A control that misses a mark is diagnosed and disclosed before any row is read, and tested on further fresh points. The pass marks live in `run/grid.py`, and `dev/fresh_pass.py` tests them, each cause from the records.

## 6. Stated before any read

All INFERRED, from stored known outcomes (`dev/stored_readings.out`, `dev/t5_top.out`, `dev/t5_laws.out`). None is a classification.

- **The twelve** should keep their stored type and indices at `N = 40`. A disagreement is a finding.
- **T5's quartet at `N = 40`.** The real part at 128 reads about 0.048 if it is geometric in `N`, 0.035 if algebraic, and 0.053 if its square is geometric, the law near a Krein collision. At 132: 0.127, 0.116, 0.136.
- **Every law keeps 132 off the axis,** and 128 is too close to call. On the collision law the collision sits near 127 at `N = 40`, with a limit of 127.5 to 128.
- **An Elliptic stretch with `K` = 4** should appear before the quartet, because the index drop and the quartet look like separate events. A collision moves no index, and the three low pairs at 90.51 are all Krein-negative, so one has to pass through zero before two can leave the axis.
- **No new link at `N = 40` alone** at any stored point of the rows (`dev/tolerances.out`).

## 7. The order

1. The pin: one MIT commit, pushed, holding this folder.
2. The solves, on the pinned code, side by side. Between the pin and the note there are no spectral reads, no diagnostic previews and no grid change from a result. The only checks are on solve fields (`dev/solve_checks.py`): that `N = 24` and 32 paths reproduce the stored ones where their grids agree, and that `m` at T5's stored points does.
3. The review of the design and the changed code, with the solves running. Any change after the pin gets its own dated commit.
4. The dated note on the census page, which names the manifest pin. `run/jobs.py` refuses every read of this computation's solutions until it is given that commit.
5. The reads: the fresh controls, against their marks (`dev/fresh_pass.py`), then each row's classified points, then the items.
6. T4/R4's locator, and T5's top.
7. The record, labelled as MIT's own, then a census-page note.

If something stays open, the table reports the raw values at every rung with the cause beside them.
