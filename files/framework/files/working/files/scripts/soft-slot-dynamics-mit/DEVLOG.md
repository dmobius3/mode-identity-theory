# MIT's own computation: development log

The record of the build. Entries are appended, never edited. A correction is a new entry. This is MIT's own computation, outside M8: `run/DESIGN.md` says what that means and what does not carry to it.

## 1. 2026-11-02T17:58:15Z: the folder, the two changes, the runner

On Blake's word ("Begin"), after recon v2 and the units' review of it, with C2a/R5 kept in.

- **The code.** `instrument/` and six files of `run/` are copied from M8.18's folder, and each is equal to M8.18's byte for byte but `instrument/convergence.py`, which gains the arm `same_resolution` (candidate A, as the preview had it), its `_blur`, and one import. `run/changed.py` holds candidate B and the changed reading. `instrument/linear.py` stays M8.18's: B reads its flag at the record's own call (`changed.capture`), which also keeps D's eigenvalues and L's eigenvalues nearest zero with each read point.
- **B's width,** which the preview did not fix: the gray zone's factor is 10, as L's is, in place of the inherited 1000, so its top is 10⁻⁷ ‖B‖. The cut stays, so `n(D)` and D's nullity cannot move.
- **The grid** (`run/grid.py`): the rows' windows; T5 with eleven added points from stored readings alone; six fresh control points and their pass marks.
- **The runner** (`run/runner.py`, `run/jobs.py`): one process per job, longest first, a checkpoint after every accepted point, and a job's files hashed when it completes. A read refuses until it is given a commit on `origin/main` whose census page names the manifest pin.
- **The pin** (`tools/pin.py`) reuses `devtools.frozen()` so `devtools.py`, `branches.py` and `seeds.py` stay M8.18's: it writes `run/MANIFEST_PIN`, `run/FROZEN.json` and `run/FROZEN_PIN`, again at each change. It is MIT's own manifest, not an OpenWave freeze.

**Regression** (`dev/test_regression.py`, `.out`): this tree's rule as built gives all 262 stored readings field for field; the changed reading moves exactly C3R/R4 and P5 at 0.25 on M8.18's ladder and T5J at 0.25 on M8.16.1's, and no reason elsewhere. A motion of 3×10⁻⁶ at `N = 40` alone, and a pair really closing, stay Unresolved. Five arms go red, each for its reason. My first two arms were wrong and did not go red: a `FACTOR` of 0.2 moves nothing, and a centroid catches a common shift. They are replaced: a `FACTOR` of 0.001, and the closing pair, which a centroid passes.

**The jobs' guards** (`dev/test_jobs.py`, `.out`), 25 claims. A path killed with SIGKILL after two of four points resumes and ends equal to M8.18's stored path. The note gate refuses no commit, a commit off `origin/main`, and a commit whose page lacks the pin.

**Each tolerance at each rung** (`dev/tolerances.py`, `.out`), the lesson of #692: at 79 stored points, no neighbouring pair in the tested set lies between `τ(32)` and `τ(40)`, or between `τ(32)` and `τ(48)`. The nearest stays 1.75 `τ(40)` away, at T1/R4 at 0.25. A's zero cluster stays at least 7 times clear, at T4/R4 at 5.66, and L's gray zone at least 2×10⁵ times.

## 2. 2026-11-02T17:58:15Z: the runner's first test: exact, but not four times as fast

`dev/runs/002_first_test/`. M8.18's six controls at `N = 24` and 32, twelve paths, four at a time, with `VECLIB_MAXIMUM_THREADS=1`, on the code of entry 1. `run/DESIGN.md` went into `run/` during the test, so the manifest moved and I re-pinned it before the queued sealed-seed jobs started; no code changed.

**The reproduction:** 12 paths, 336 solve fields and 11,048 array entries against M8.18's files: 0 differences. So neither one thread in place of unset nor three neighbours moved a float.

**The time:** each job took about 1.9 times what it took alone, 10,376 s in all against M8.18's 5,448 s, and the whole took 2,802 s. So four at once gave about 1.9 times the throughput, not 4, and cpu time equals wall time, so the jobs were not waiting on anything but the machine. The recon's "about a day" assumed about 4. The peak was 2.10 GB. `dev/runs/003_scaling/` measures why, and what count is best.

## 3. 2026-11-02T19:39:21Z: how it scales, and one field that moved

**Scaling** (`dev/runs/003_scaling/`). Copies of one real path, C2a/R5 at `N = 24`, side by side, alone taking 172 s. Throughput against one job alone: 1.57 at two, 1.95 at three, 2.10 at four, 2.15 at six and 1.86 at eight, where cpu time falls below wall time. Something shared on the chip limits it, so four is the count: six gains nothing and eight loses. The cause is not established. The whole computation, about 75 hours in series, is then about a day and a half to two days, not the one day the recon said (INFERRED), and the longest single job, about 12 hours alone, takes about 23. Unset threads and one thread cost the same, 2.08 against 2.10 at four.

**The reread** (`dev/runs/004_reread/`), at one thread. M8.18's stored solutions at all six controls and all three cutoffs, read by this tree's code, four at a time: 2,800 s, peak 2.18 GB. Then `dev/test_end_to_end.py`: the as-built reading, the reading beside it and both identities equal M8.18's at every point, and the changed reading is converged at all 24 with the type and indices on the record, moving exactly P5 and C3R/R4 at 0.25.

**It failed on one field.** 20 of the 72 points differ from M8.18's record in `record/leak` alone, all at `N = 24`, in the round-off: 7.48×10⁻¹¹ against 6.54×10⁻¹¹, for instance. With `VECLIB_MAXIMUM_THREADS` unset, as M8.18 ran, the field is exact (`dev/runs/005_leak/leak.out`). So my choice of one thread moved a routine of Accelerate's at that size. The solves reproduced at one thread, and nothing the rule reads moved, but M8.18's setting has no cost, so the run takes it: `--threads 0` is the runner's default, and `run/ENVIRONMENT.json` is recorded unset. Entry 2's reproduction was at one thread, so both tests are repeated at the run's own setting (`dev/runs/006_final_test/`).

**Added to `dev/test_jobs.py`:** `read` itself, through the note gate, killed after its first point, resumed, and equal to M8.18's record. 28 claims pass.

## 4. 2026-11-02T21:44:23Z: the test at the run's setting, and the folder made ready for the pin

**The final test** (`dev/runs/006_final_test/`), on the code of entry 3, with `VECLIB_MAXIMUM_THREADS` unset, four at a time:
- M8.18's six controls at `N = 24` and 32, solved again: 12 paths, 336 solve fields and 11,048 array entries, 0 differences (`compare.out`). 2,980 s wall, 11,090 s of job time, peak 2.09 GB.
- Its stored solutions at all three cutoffs, read again: 72 points, 0 differences from M8.18's records, `record/leak` included. 2,762 s wall, peak 2.35 GB.
- The as-built reading, the reading beside it and both identities equal M8.18's at all six controls. The changed reading is converged at 24 of 24 with the type and indices on the record, moving exactly P5 and C3R/R4 at 0.25, and the classification differs at those 2 points alone (`end_to_end.out`).

So the failure of entry 3 was the thread setting, and at the run's setting it is gone.

**Every start** (`dev/entries_check.py`, `.out`). All ten entries of the solves at `N = 24` and 40: the admission and the seed's orbit checks, which is all a job does before its first solve. 20 starts, 0 refused, no solve run. The tests could not show this, since T1, T4, T5 and T5J had not been through this tree's admission.

**The last edits,** none of them code. `run/DESIGN.md` now says what was tested, the job count, the thread setting and where each input lives. The docstring of `run/grid.py` names `dev/` in place of the bench, and its syntax tree without the docstring equals the tested copy's. `run/changed.py`, `run/jobs.py` and `run/runner.py` equal the copies in `dev/runs/006_final_test/`. So the test's `RUNLOG.json` files carry the manifest before those edits, and the pin below differs from it in `run/DESIGN.md`, that docstring and the pin's own files.

**The grid's sources** are now in `dev/`: `stored_readings`, `t5_top` and `t5_laws`, rerun on the published records with their outputs unchanged, and `preview_fix` and `t5j_tau`, copied as they ran.

**Big outputs.** The reads of `dev/runs/004_reread/` and `006_final_test/`, 46 MB each, stay on the bench. `runner.py OUT rereads --source` regenerates them from M8.18's folder. Each run's `RUNLOG.json` and its `reread_*.json` comparisons stay here.

**The scan:** 220 files, 0 hits, its control string found. `run/record_environment.py --check`: no differences.

**The pin:** `a5c6958473e44702db3ee2e81106e7ee3c439e571fca1a3cc6f045f945bbdbee`.

## 5. 2026-11-02T23:38:54Z: the units on the pin, and the last changes before it

Both units gave a GO for the solves, and each finding was checked at source. No code a solve runs changed: `grid.entry`, `grid.solves` and `grid.allowlist` equal the tested copy's for all 16 tags and 30 jobs, and of `run/grid.py` only `PASS_MARKS` and its comment moved.

**Taken as given:**
- UA 3, on T5 in `run/DESIGN.md`, section 4: a difference in `m` at 128 beyond numerical tolerance is evidence of path dependence, and whether the coarse path stepped onto another solution stays OPEN. The same claim sat in the docstring of `dev/solve_checks.py`, which is fixed too, and that script now reports `eps_reached` beside `m`.
- UB 2: the tolerances grow through ‖A‖ and ‖B‖, which grow about as `N²`. `τ` itself grows about as `N`, as its values at P5 show: 7.173×10⁻⁶, 9.636×10⁻⁶ and 1.207×10⁻⁵.
- UB 4: the as-built marks at P5 0.24 and C3R/R4 0.20 now name their causes, a new link at `N = 40` alone and D's flag at `N = 40` alone. `PASS_MARKS` carries them, and `dev/fresh_pass.py` tests them from the records. On M8.18's controls the six known marks pass, and three wrong marks are reported, one by its verdict and two by their causes (`dev/fresh_pass_test.out`).

**Taken with a change:**
- UB 1: T5J and the coherent row in `R5` are named in a sentence of their own, not inside the sentence that cites the census note and the answer, since neither source speaks of them.
- UB 3: the separations are in, 8.7839×10⁻⁶ at `N = 16` and 8.7801×10⁻⁶ at `N = 24`. `N = 32` holds none, because a read keeps only a linked group's centre, and this computation's reads do the same. So the design now says the members are measured after the note, as M8.18's `pair_gap.py` measured P5's, and that whether the gap closes is reported beside any T5J verdict under A. That clause is mine.
- UB 5: the point stands, that the rung and the verdict must be fixed before the locator reads, and "both verdicts agree at its guard readings" is taken. The rungs are not UB's. UB wrote `N = 16`, 24 and 32, as M8.17's locator ran, but M8.18's terms already read that locator onto this ladder: `N = 32` and 40 deciding, `N = 24` bisected where its ends' `n(L)` is resolved and different and reported otherwise. `census_lib.ARM_A` holds the same, and `N = 16` is not read here.
- UB 8: `run/record_environment.py` is not new, since it equals M8.18's byte for byte. The new bullet names `tools/pin.py`, `tools/inventory.py` and what they write, and gives `run/ENVIRONMENT.json` as this machine's reading.

**UB's count.** The 221st file is `SHA256SUMS`, written after the first scan. It lies outside the manifest, which covers 27 files of `instrument/` and `run/`, as `dev/`, `tools/` and this log do, and it lists the other 220. The scan after it read 221 files, with 0 hits.

**Kept:** UA 1, 2 and 4 and UB 6 and 7. UB reproduced the three laws at `N = 40` from the stored values, within the inputs' rounding. UB 7 goes into the notes for the dated note, which says what `m` at T5's stored points showed.

**What the GO covers.** The solves alone. The changed reader has its separate review before any new reading.

**Repeated on the final tree:** `dev/entries_check.py`, 20 starts, 0 refused, no solve.

**The pin:** `391b097fa6164e502c341b384381d19207d943f5692bb67f43a1cb2c28d49c65`.
