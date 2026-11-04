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

## 6. 2026-11-03T00:01:32Z: a limit of A, found for the reader's review

`dev/closing_within_tau.py`, `.out`, on P5's stored record at 0.25. Nothing is solved or read. `dev/test_regression.py`'s closing pair sits at 4×10⁻⁵ and 3×10⁻⁵, both above τ(40), so it never tested a pair inside τ(40). With the group of two at `N = 40` kept and other gaps at `N = 24` and 32:

- **Inside τ(40) at both,** 1.15×10⁻⁵ and 1.0×10⁻⁵, and 1.2×10⁻⁵ and 1.0×10⁻⁵: Unresolved as built, converged under A. A reads the pair by its centre alone at every cutoff, so a closing gap is not seen.
- **Above τ(40) at `N = 24` alone,** 1.25×10⁻⁵ and 1.0×10⁻⁵: the same. The members' change falls to zero at `N = 32` under A, and the rule reads that as contracting.
- **Stable above τ(40),** 1.25×10⁻⁵ at both: Unresolved under A, as it should be.
- **3×10⁻⁵ and 1.0×10⁻⁵:** converged both ways, since a falling change is what the rule passes.

A linked group keeps only its centre, so at a cutoff where the pair is linked the record cannot tell these from P5's stable pair. So a changed verdict alone does not show that a pair is stable, and the design's measure at T5J is too narrow. The proposal, for the units: wherever A alone moves a verdict, the pair's members are measured at every cutoff, and the changed verdict stands only if the gap's change between neighbouring cutoffs stays below the top cutoff's margin. Any change to `run/DESIGN.md` waits for the solves to end, since the manifest guards the sealed seeds.

## 7. 2026-11-03T07:49:23Z: the units on the reader, and the reader they asked for

Both units reviewed the changed reader. UA: HOLD for new readings until (b), (e), (f) and (g) are fixed and tested. UB: GO after fixes. Neither objects to the solves. Each finding was checked at source. The fixes are made in a copy of this folder on the bench, since nothing under `run/` or `instrument/` here changes while the solves run, and they come here after the last solve, by a dated commit.

**A, redesigned** (UA (a), (b), (e); UB (a), (b), (e)). Both units asked to keep a linked group's members and to guard the verdicts A moves by them. With the members kept, A needs no blur. A read now keeps each linked group's eigenvalues by the group's indices, beside its centre (`members`). Under A a set is read by its eigenvalues: its change between two cutoffs is the bottleneck distance between them, the measure the rule already uses between centres, and its row keeps them at every cutoff (`levels`). Every other step of the rule stands. The first A, pinned at `6063351ad376a8965936e0ad7001dec3c7d1b429`, is replaced before any read of this computation. `dev/closing_within_tau.py` needs its arm, so it moved with its output to `dev/runs/007_a_limit/`, and `dev/test_regression.py` holds its cases.

**One departure, for the units.** Both asked for a bound on the members' change: UA, where A alone turns Unresolved into converged, each adjacent gap change below the top cutoff's margin, which is entry 6's proposal narrowed to those verdicts; UB, wherever a set has a group linked at one cutoff and its members apart at another, each offset's change below the floor. This A puts the members to the rule's own test instead, now that a read keeps them: a change that contracts or stays under the floor, and a remaining error under a tenth of the distance to the nearest event. On P5's pair at 0.25, with the floor 5.53×10⁻⁷:

| Gaps at `N = 24`, 32, 40 (L: one group) | As built | This A | UA's bound | UB's bound |
|---|---|---|---|---|
| 1.1345×10⁻⁵ at all three, L at 40: stable, as stored | Unresolved | converged | converged | converged |
| 1.2×10⁻⁵, 1.0×10⁻⁵, L 8×10⁻⁶: closing | Unresolved | Unresolved | Unresolved | Unresolved |
| 1.15×10⁻⁵, 1.0×10⁻⁵, L 8.5×10⁻⁶: closing, slower | Unresolved | Unresolved | Unresolved | Unresolved |
| 1.2×10⁻⁵, 1.0×10⁻⁵, L 9.8×10⁻⁶: closing, its change falling | Unresolved | converged | Unresolved | Unresolved |
| L 6×10⁻⁶, 1.0×10⁻⁵, 1.4×10⁻⁵: opening | converged | Unresolved | Unresolved | Unresolved |
| 3×10⁻⁵, 1.0×10⁻⁵, L 5×10⁻⁶: closing fast | converged | converged | converged | Unresolved |
| 8.78×10⁻⁶ at all three, L at 32 and 40 | converged | converged | converged | converged |

The as-built and A columns are run (`dev/test_regression.out`); the bounds' columns are DERIVED from the gaps and the floor. In the fourth row each member moves 1.0×10⁻⁶ and then 1.0×10⁻⁷, so the remaining error is 1.1×10⁻⁸, and as built reads Unresolved because it takes the link at `N = 40` for motion, the cause P5 failed by. In the sixth, as built passes the pair by the same contraction. A one-to-one group with either row's steps converges under the rule, so a bound would put a set's members to a test no other group meets. What a bound adds is a guard against a slow rate under a faster one, which the rule's docstring names as its limit for every group. If the units rule for a bound, it goes into the changed verdict as they write it, before the note.

**Taken as given:**
- UA (f), UB (f): `reread` first calls `m818_files`, whose first line is UB's. It then refuses a source whose `SHA256SUMS` is not M8.18's, pinned in `run/jobs.py`, or whose files differ from it. `run/runner.py` refuses reads, identities, readings and `fresh` without `--note` and `--repo`, before it writes to `RUNLOG.json`, UB's line with `fresh` added.
- UA (g): `run/fresh.py` is new. The job `fresh` writes `fresh_pass.json`: each mark's misses, the marks, and the hashes of the reading files they rest on. `run/jobs.py` refuses a row's read, identity or reading without a pass for `run/grid.py`'s marks on unchanged files, and `run/runner.py` plans no row until then, so a default launch takes the fresh controls first. `dev/fresh_pass.py` now runs `run/fresh.py`.
- UB (c): `changed.identity`, UB's code with `bool()` around `same`, which changes nothing, and UB's replacement in `jobs.reading`, as written. The C2b case is section 12 of `dev/test_jobs.py`.
- UB (h): `dev/solve_checks.py` reports a failed point on a new path by its reason.
- UB (a), section 6: "in the tested set".
- UA (i), UB (i): section 4 says what the locator's job and `N = 48`'s commit must state before either reads, and T5J's members are in every read.

**Taken with a change:**
- UB (e): each group's members are stored as its indices and their eigenvalues, not as a bare list, so they carry the stable reference UA (e) asked for.
- UB (g): `link` gets no offset check of its own. Under this A the changed verdict at a fresh point reads the members itself, so its mark is that check. Section 5 says what a pass does not show.
- UA (a), UB (a), section 3: A is new, so the section is new. It says A can move a verdict either way, and "The A it replaces" says what the first one did.

**Kept:** UA (c), (d), (h); UB (d). UA's qualification goes into the notes for the dated note.

**The tests** (`dev/runs/008_reader_v2/`), on this copy's code, two at a time beside the four solves:
- `dev/test_regression.py`: the 262 stored readings of M8.18's controls, M8.16.1 and M8.17, as built, field for field. The change moves C3R/R4 at 0.25 alone among them, since no stored summary keeps the members. The table's seven cases read as stated, and 5 of 5 arms are red for their reasons.
- `dev/test_jobs.py`: 49 claims.
- M8.18's stored solutions at all three cutoffs, read again: 72 points, 0 differences from M8.18's records, the members aside. 18 rereads, 6,508 s wall, peak 2.41 GB.
- The as-built reading, the reading beside it and both identities equal M8.18's at all six controls. The changed reading is converged at 24 of 24 with the type and indices on the record, moving exactly P5 and C3R/R4 at 0.25, and the classification differs at those 2 points alone. P5's pair at 0.25 is `pair_gap.out`'s at each cutoff to 10⁻¹², its gap 1.1345×10⁻⁵, and its row reads d1 5.390×10⁻¹¹, d2 7.550×10⁻¹⁴ and U at the floor, 5.534×10⁻⁷ (`end_to_end.out`).
- `dev/fresh_pass.py --test` on these reads: the six known marks pass, three wrong marks are reported, and none is missed. Its output equals v1's (`dev/fresh_pass_test.out`).

A first launch, beside the solves, slowed them and was stopped. These reads are the second launch's, on mains, and `RUNLOG.json` holds it alone.

**Big outputs.** The reads, 51 MB, stay on the bench; `runner.py OUT rereads --source` regenerates them from M8.18's folder. The run's `RUNLOG.json` and its `reread_*.json` comparisons stay here.

**This copy's pin:** `b4a1faa5c85bfb0d433dc637f5861d246ee5c80367299b123cc317048840bf35`.

## 8. 2026-11-03T14:08:01Z: the units on reader v2, and their fixes

Both units reviewed reader v2 (entry 7). UA: GO, subject to the dated-note and fresh-control gates, with one operational NIT. UB: GO after fixes, two of them FIXABLE and two NITs. Neither objects to the solves. Each finding was checked at source, and the fixes are made in this copy on the bench, as entry 7's were.

**No bound.** Both units accept this A without a bound on the members' change: UA accepts the argument for the rule's own test, and UB withdraws its bound. UA's caution: a converged set does not show that a pair's internal gap is constant or that a collision cannot occur. Section 5 says what a pass does not show, and the notes for the dated note carry the caution.

**Taken as given:**
- UB 2: section 3's sentence, as written: "With the members kept, this A puts them to the rule's own test in place of a guard, with no blur and no new threshold. The guards asked for were stricter, and read Unresolved closing pairs this A reads converged (DEVLOG 7)."
- UB 4: `SOLVE_PINS` in `run/jobs.py`, the manifest the solves run under, and `stored` refusing a path whose job record names any other, as written, with UB's comment on the line above to keep the line's length. Section 7's item 4, as written. `reread` reads M8.18's files through `m818_files`, not `stored`, so it is unchanged.
- UB 6: the fresh check's job and file are named by the marks they test, `fresh_` and `fresh_pass_` with the first 12 hex digits of the SHA-256 of `json.dumps(marks_now())` (`fresh.names`). `refusal` reads the file for the current marks and refuses unless its SHA-256 is the one its job logged. A miss stays on record, and new marks get a pass of their own.
- UB 6, NIT: `run/runner.py` plans `fresh` only once every fresh control's reading is complete, and says which it waits for, so an early launch counts no start.
- UA (g), NIT: under UB 6's naming a failed check stays on record. Section 5 adds that no job record in the run's output is deleted or rewritten: a read made again goes to a new output folder, which its dated commit names.

**One more change:** the design's opening line said everything in it was written before any new solve, but entry 7 revised sections 2 to 7 after the solves began. It now reads "Written before any new solve, and revised before any read of one (DEVLOG 7 and 8)."

**Checked:** UB 5: `M818_SUMS` is the SHA-256 of M8.18's `SHA256SUMS` at `6063351a`, 285 lines; at M8.18's record commit `5241a2d5` that file hashes otherwise, so the pinned list is the close-out's. UA reran the stored-data tests on Python 3.13.5, NumPy 2.3.5 and SciPy 1.17.0, and UB reproduced four outputs byte for byte. The jobs test and the 72-point reread, which need M8.18's solutions and a clone, rest on this machine's runs alone.

**Pins to come:** `N = 48`'s commit adds its solves' pin to `SOLVE_PINS` the same way (UB 4), and so does the locator's job, which solves at its midpoints.

**The tests** (`dev/runs/009_unit_fixes/`), on this copy's code, one at a time beside the four solves:
- `dev/test_regression.py`, `dev/tolerances.py` and `dev/fresh_pass.py --test`: each output equals its `.out`, byte for byte.
- `dev/test_jobs.py`: 58 claims, PASS. New: the solve-pin gate both ways, a path solved under this tree refusing and the same path passing once its record names the solve pin; and the fresh check by its marks, an early launch waiting with no start counted, the check planned under its marks' name once the readings are complete, a pass file other than the one its job logged refusing, and a miss staying on record when the marks change, the new marks needing a pass of their own and the old marks still refusing. The test's path is solved under this tree, so its reads run `jobs.py` with this tree's pin added to the solve pins (`jobs_here`), in the test alone.
- `dev/test_end_to_end.py`, from run 008's rereads of M8.18's six controls, since no fix touches a read, with the identities and readings run again on this code through the note gate: the as-built readings, the readings beside them and both identities equal M8.18's at all six controls; the changed reading is converged at 24 of 24, moving exactly P5 and C3R/R4 at 0.25; P5's pair equals `pair_gap.out` at each cutoff. PASS, its output equal to run 008's, timings aside. Its path records are the test's own, written under this tree, so its identities run through `jobs_here` too.

The first launch of these ran before the copy was re-pinned. The jobs test stopped at its note-gate claim and the end-to-end test at its first identity, each on "the running tree differs from run/MANIFEST_PIN", the gate refusing as it should. Their temporary outputs were removed, the copy was re-pinned, and every test ran again.

**Outputs.** The end-to-end run's identities and readings, with their job records, stay on the bench beside run 008's reads. `dev/runs/009_unit_fixes/` keeps the changed code as run and both outputs, and `dev/test_jobs.out` is this run's.

**This copy's pin:** `8a812b476074b3599416e7dc173e3d022d155b0a568329b1273c1b10a2dbd645`.

## 9. 2026-11-04T05:05:18Z: the solves ended, and the reader lands

**The solves** ended at 2026-11-04 04:50Z, 29.2 hours after their launch: all 30 path jobs, the six rows and the four fresh controls at `N = 24`, 32 and 40, completed with exit 0, and none failed. Every path log has all its points accepted, 369 in all. Every job record names the manifest the solves ran under, `391b097fa6164e502c341b384381d19207d943f5692bb67f43a1cb2c28d49c65`, and the 60 files the records logged match their SHA-256; the manifest equalled that pin to the end. Nothing of this computation has been read.

**The reader lands.** On Blake's word, the bench copy of entries 7 and 8 replaced this folder's files outside `run/out`, which no step touched, so the folder outside `run/out` equals the copy file for file. Against the pin commit's tree, 38 files are added and 18 changed, none removed. `run/fresh.py` is new; `run/changed.py`, `run/jobs.py`, `run/runner.py`, `run/DESIGN.md` and `instrument/convergence.py` are the copy's, with `dev/`'s tests, their outputs and runs 007 to 009. The folder's two files the copy lacked, entry 6's `dev/closing_within_tau.py` and its output, were removed here, since entry 7 moved them byte for byte to `dev/runs/007_a_limit/`.

**The pin.** `tools/pin.py` gives `8a812b476074b3599416e7dc173e3d022d155b0a568329b1273c1b10a2dbd645`, the copy's, so `run/MANIFEST_PIN`, `run/FROZEN.json` and `run/FROZEN_PIN` equal the copy's byte for byte. `run/jobs.py`'s `SOLVE_PINS` holds the solves' manifest alone, so the reads take these paths and refuse any path solved under another.

**The commit** leaves out `run/out`: the solves' outputs come with the record (DESIGN section 7). `SHA256SUMS`, written last, lists the committed tree, 258 files.

**Next:** the dated note on the census page, naming both pins, on Blake's word; then the fresh controls, their pass on record, the rows and the items.
