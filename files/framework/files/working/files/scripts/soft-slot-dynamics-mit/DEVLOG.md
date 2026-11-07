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

## 10. 2026-11-04T14:24:32Z: the one look before the note, and the dated note

**The solve checks** (`dev/runs/010_solve_checks/`), the design's one look before the note, at solve fields alone (section 7, item 2). `solve_checks.py`, against M8.17's and M8.16.1's stored paths: 0 failures. Every path at `N = 24` and 32 on a stored grid equals its record field for field, T5 to 64, and where a grid is new a stored point's `m` differs by at most 8.48×10⁻⁷ relative. `slope_check.py`, written for the units' review of the note: at every such point that difference is dm/dε along the path times the difference in the amplitude reached, over `m`, within 0.5%, by central differences of the solve fields. So the two paths stop at slightly different amplitudes of one curve; whether the coarse path stepped onto another solution stays OPEN (UA).

**The dated note,** under the census page's § V, step 5, drafted from `NOTES_for_the_dated_note.md`. Both units reviewed v1: nothing FATAL, and their changes are in v2, 1562 words, which lands on Blake's word ("Gucci, post it"). It names the pin current on its date, `8a812b476074b3599416e7dc173e3d022d155b0a568329b1273c1b10a2dbd645`, and the solves', `391b097fa6164e502c341b384381d19207d943f5692bb67f43a1cb2c28d49c65`.

**The output, but the solutions** (UB). The note's commit carries `run/out` but its 30 `.npz` files: the 30 job records, which name the solve pin and log both files' SHA-256, each path's solve fields and log, and `RUNLOG.json`, 91 files, byte for byte the review packet's. Which solutions existed before any read is then on record, and `record_of` checks each against it at the read. The `.npz` files come with the record. Entry 9 left `run/out` out of its commit; this one takes all of it but the solutions.

**`SHA256SUMS`** lists the committed tree, 353 files. The manifest does not move, since `run/out` and `dev/` lie outside it.

**Next:** the reads, with the note's commit, the fresh controls first.

## 11. 2026-11-04T19:12:02Z: the fresh controls passed, and the rows' readings

**The fresh controls,** on Blake's word ("Start the reads"), with the note's commit `beb7eee2`: 12 reads, 8 identities, 4 readings and the check `fresh_4f6e521d36a7`, none failed. The check passed with no miss (`run/out/fresh_pass_4f6e521d36a7.json`): P5 at 0.24, C3R/R4 at 0.20 Unresolved as built and converged changed; P5 at 0.30, C3R/R4 at 0.30, C2b at 0.30, C2a/R5 at 0.30 converged both ways, each with the case's own type and indices at all three cutoffs, K1 and branch identity on both pairs, and the two Unresolved as built by their marks' causes, P5's link and C3R/R4's flag.

**The rows:** 18 reads, 12 identities and 6 readings, four at a time, from 15:36Z to 18:58Z, none failed. All 61 read-side job records name the manifest pin `8a812b47`, and every file they log has the SHA-256 they logged.

**What the readings give** (`dev/runs/011_row_readings/`: `row_readings.py`, on the reading files alone, nothing solved or read again):
- **The twelve,** classified both ways at `N = 24`, 32 and 40, each with M8.17's stored type and indices at every cutoff: T1 Elliptic (2, 0, 2) at 1.41, 32, 45.25, 64 and 72 in `R4` and at 32 in `R5`; T4 in `R4` Elliptic (7, 1, 6) at 4 and Hyperbolic (6, 1, 5) at 8, 11.31, 64 and 72; T5 Elliptic (9, 3, 6) at 45.25. 12 of 12.
- **The rows,** classified as built and changed: T1 in `R4`, 18 of 18, and in `R5`, 15 of 15, all Elliptic (2, 0, 2); T4 in `R4`, 18 of 18, Elliptic (7, 1, 6) from 0.25 to 4 and Hyperbolic (6, 1, 5) from 5.66 to 72; the coherent row in `R5`, 15 of 15, all Elliptic (0, 0, 0) to 32; T5, 20 of 31, Elliptic (9, 3, 6) wherever classified; T5's second member, 15 of 20 as built and 16 changed, likewise. The two readings differ at one row point, the second member's 0.354.
- **T5's top.** From 127 to 132 each cutoff's record is Hyperbolic (4, 0, 4) with one quartet off the axis, K1 holds at each, and the rule reads every point converged both ways, `U` at most 0.0056 of its distance to the axis, where the bar is a tenth. None is classified: branch identity fails between `N = 24` and 32 alone, its aligned distance 0.0103 to 0.0106 against the guard of 10⁻², with the records agreeing, while between 32 and 40 it holds at 0.0030 to 0.0032. So `N = 40` leaves T5's top open, as section 4 allowed for from the stored distance between `N = 24` and 32. The quartet's real part at `N = 40`: 0.0649 at 127, 0.0913 at 128, 0.1116 at 129, 0.1285 at 130, 0.1568 at 132.
- **Below it** the type and indices move with the cutoff: (9, 3, 6) to 112 at `N = 24` and to 120 at 32 and 40; Elliptic (4, 0, 4) at 116 at `N = 24` and at 124 at 32 and 40; Hyperbolic from 120 at `N = 24` and from 126 at 32 and 40. So 116 to 124 differ in structure along the ladder, and at 126 the quartet lies 0.0075 off the axis at `N = 40`, with `U` above a tenth of that.
- **T5 at 11.31 and 16, and its second member at 4 and 5.66:** a partner set holds one eigenvalue at `N = 24` and two at 32 and 40.
- **T5's second member.** The pair at 0.25 lies 8.7801×10⁻⁶ apart at `N = 24`, two groups, and 8.7779×10⁻⁶ apart at 32 and 40, one group, its members equal to ten digits between them. The gap does not close, and the point is classified Elliptic (9, 3, 6) both ways. At 0.354 a partner pair 1.25×10⁻⁵ apart is one group at `N = 40` alone: as built its centre steps 6.23×10⁻⁶ and reads non-contracting above the floor, and under A its eigenvalues step 1.62×10⁻¹², so it reads converged. That is P5's mechanism, at a point no record holds. At 128 and 132 it reads as T5 does, Hyperbolic (4, 0, 4) with branch identity failing between `N = 24` and 32; its quartet's real part at `N = 40` is 0.0447 and 0.1233.

**Section 6, against the readings:**
- The twelve keep their stored type and indices at `N = 40`: **held,** 12 of 12.
- T5's quartet at `N = 40`: **missed.** Its real part is 0.0913 at 128 and 0.1568 at 132, above every law (0.035 to 0.053; 0.116 to 0.136). From `N = 32` it moved 0.0051 and 0.0035, where the laws asked 0.043 to 0.061 and 0.024 to 0.044.
- 132 off the axis, and 128 too close to call: 132 **held,** and 128 reads off the axis too, each converged by the rule.
- The collision near 127 at `N = 40`, with a limit of 127.5 to 128: **missed.** At `N = 40` it lies between 124, Elliptic, and 126, Hyperbolic. On the collision law, the real part squared linear in ε (its slope 0.00403 to 0.00416 between neighbours at `N = 40`), it sits at 125.97, with 118.08 at `N = 24` and 125.75 at 32, and an Aitken limit of 125.98 (INFERRED).
- An Elliptic stretch with `K` = 4 before the quartet: **held,** at every cutoff.
- No new link at `N = 40` alone at a stored point of the rows: **held.** The one new link at `N = 40` alone is the second member's at 0.354, which no record holds.

**Next:** T4/R4's locator on (4, 5.66), since the read at 4 classifies it Elliptic, and `N = 48` for T5's top, each by its own dated commit with its terms first (section 4), on Blake's word.

## 12. 2026-11-04T19:54:34Z: the reads' records, before the locator's terms

On Blake's word ("Go after considering"), with both units' reviews of the readings. UA: draft T4/R4's locator terms and its job, and send them for review before any midpoint is solved; no run of the locator yet; `N = 48` stays apart, and the two misses stay recorded as misses. UB: the terms are written knowing these readings, so the reads should be on main first, the outputs or at least their job records with each file's SHA-256, as item 6 on the note had it for the solves.

**This commit carries the reads' records:** the 61 new job records (30 reads, 20 identities, 10 readings and the fresh check), each naming the pin and the SHA-256 of every file it wrote; their 61 logs; `RUNLOG.json`; the 20 branch-identity files; and the fresh pass. The 30 read files and 10 reading files, 292 MB, stay on the bench with the 30 `.npz` solutions, for the record: each is named with its SHA-256 by the job record that wrote it, so the readings the terms are written knowing are fixed by records committed before them.

**The quartet's steps at full digits** (`dev/runs/011_row_readings/quartet_steps.py`, since UB took them from rounded values): at 128, 0.306709, 0.121869 and 0.005136 from `N = 16` to 40; at 132, 0.286455, 0.097391 and 0.003469. Entry 11's 0.0051 and 0.0035 stand; UB's 0.0057 and 0.0032 come from `N = 32` rounded to 0.097 and 0.160. This run's values at `N = 24` and 32 equal M8.17's to within 5.4×10⁻⁹ at 128 and 9.4×10⁻¹⁴ at 132, though its path into them is new.

**Where each missed expectation was stated** (UB): the quartet's real part at `N = 40`, in DESIGN.md section 6 and in the census page's note of 2026-11-04; the collision's place, near 127 with a limit of 127.5 to 128, in DESIGN.md section 6 alone. The note does not carry it.

**For the record and its note** (UB): the coherent row's census entry, that its ladder above 2 did not run, describes M8's record and stays true. A note says MIT's computation reads the row to 32.

**Next:** T4/R4's locator, its terms and its job, for the units' review before any midpoint is solved.

## 13. 2026-11-04T20:54:54Z: T4/R4's locator, its terms and its job, and its note

On Blake's word ("Land if/when gucci"), with both units' GO on v2. Nothing has been solved or read since the reads' records (`bcee21ad`).

**The terms,** `run/LOCATOR.md`, 1658 words. T4/R4's bracket is (4, 5.66), from the reads by section 4's rule. The bisection is `census_lib.settle`, byte for byte M8.18's, on Arm A's ladder, `N = 32` and 40 deciding and 24 bisected and reported. It takes Arm B's moved midpoint, as section 4 fixed it before the row was read, knowing that M8.18's terms gave a new bracket no moved midpoint and named this one the likeliest to stop on K1. A location is named only where both verdicts agree at the guard readings the locator takes. Before T4/R4 is read, M8.18's location of T4/R5's change is reproduced on this tree: the whole record against `ARM_B.json`, field for field, timings aside, and its 146 solution arrays entry for entry.

**The job,** `run/locate.py`, new. `grid.py` gains `LOCATOR`, and the allowlist gains T4/R5, the reproduction's case. `jobs.py` gains `locate_repro` and `locate` behind the note gate, `locate` behind the fresh gate too. A reproduction on record that did not pass exits nonzero, so the runner reports it failed. `runner.py` gains the kind `locate`, which plans the reproduction first, from `--source`, and T4/R4 once it has passed. Only the bracket's ends pass through `jobs.stored`. The midpoints' and guards' solutions are solved and read inside the job, so `SOLVE_PINS` stays `391b097f` alone: no tree can list its own pin.

**The review.** v1 (`locator_review_v1.zip`): both units GO after fixes, nothing FATAL. They kept all three readings: the moved midpoint per midpoint; both verdicts at the guards the locator takes, with no retry of their own; the note before the run. UB conceded that a tree cannot list its own pin, and withdrew the quartet's steps, which came from a rounded value. v2 takes UA's three redlines and UB's four as written, in the terms and the note. The note gives UA's sentence the page's names for the rows. UA's NIT is applied: the nonzero exit. A claim of my own is corrected: §6's rules were fixed "before the row was read", not "before any of them was read". On v2 both units GO, once the note carries its two changes and the new pin, and the checks pass on the final tree: they hold.

**Tests, on this tree:** `dev/test_locate.py`, 46 claims, PASS, on records alone, with nothing in `run/out` written. M8.18's own `run/test_locator.py`, 40 arms, rerun in a copy of its folder, gives its committed output byte for byte (`dev/runs/012_locator_tests/`).

**The note,** under the note of 2026-11-04, with the Inputs line naming `run/LOCATOR.md`. Its checks pass on this tree: the gate passes at the pin and refuses the base page and an off-main commit; GitHub renders 177 of 177 math expressions; the lint gives 0 FAIL, 0 WARN.

**Pins:** the manifest moves to `340684d5b5c9c9162e8dab76606b8f91607eeaab5a42fac461bb529fd0116c87`; the solves' pin is unchanged.

**Next,** on Blake's word: `runner.py run/out locate` twice, with `--source` M8.18's published folder, `--note` this commit and `--repo` MIT. First the reproduction, then T4/R4 if it passes.

## 14. 2026-11-05T11:43:07Z: the reproduction passed, and T4/R4 stopped on K1 at its change, not located

**The run,** on Blake's word ("Start it"): one background task under caffeinate, two launches of `runner.py run/out locate` with `--note 87dedb00`, both jobs under the manifest pin `340684d5`. The reproduction ran from 21:00:51Z to 02:28:10Z, 19639 s, and T4/R4 from 02:28:11Z to 10:02:33Z, 27262 s. Neither failed, and every file each job record logs has the SHA-256 it logged.

**The reproduction passed.** M8.18's Arm B, T4/R5 on (8, 11.31), recomputed on this tree: no stop, no difference from `ARM_B.json` field for field, timings aside, and 0 of 146 solution arrays unequal. The six files it compared are M8.18's published files byte for byte (`dev/runs/013_locator_reading/`).

**T4/R4 is not located.** At `N = 24`, 32 and 40 alike, nine midpoints were accepted from both ends with K1, `n(L)` agreeing both ways and the aligned distance at most 6.1×10⁻⁸. They narrowed (4, 5.66) to [5.588897336915544, 5.592133380371584], `n(L)` 7 below and 6 above: 0.003236 wide, 5.79×10⁻⁴ of its lower end, where a cutoff completes below 5×10⁻⁴. The tenth midpoint, 5.590515, was accepted from both ends, and K1 failed at both: the zero cluster is not separated, an eigenvalue of A lying in (margin/3, 3 margin), and at `N = 32` and 40 V0's dimension is also 8 against 6. Moved once, to 5.590192, it was accepted and K1 failed again, not separated: a stop. The record's verdict is the terms' own: "N = 32: an unsuccessful stop: K1 fails; N = 40: an unsuccessful stop: K1 fails". No guard was read, so neither verdict was taken at a guard. The bracket stays not located, with the exact stop in the record (LOCATOR §3). M8.18's terms named this bracket the likeliest to stop on K1 (§2).

**What the records show besides, INFERRED** (`dev/runs/013_locator_reading/`, section 3, on the records alone; it decides nothing):
- The eigenvalue of L that changes sign, the fifth nearest zero after the four structural zeros below 10⁻¹⁰, is close to linear in ε here, slope 0.01885, and changes sign between the two refused points: at `N = 40`, −5.641×10⁻⁶ at 5.590192 and +4.491×10⁻⁷ at 5.590515. Its zero is 5.59049 by interpolation between them at `N = 32` and 40, and 5.59044 at 24. The line through the five accepted midpoints within 0.02 puts it at 5.59047 at 32 and 40.
- A's eigenvalue on that mode goes as the root of L's: |λ|²/|μ| lies between 2.517×10⁻⁶ and 2.531×10⁻⁶ at those seven points, the two refused ones included.
- K1 then fails wherever |λ| < 3 margin: within 4.7×10⁻⁴ of the zero at `N = 24`, 8.4×10⁻⁴ at 32 and 1.32×10⁻³ at 40, as the margin grows with `N`. At `N = 40` that neighbourhood is 0.00264 wide, against the 0.00279 within which a cutoff completes. At `N = 32` and 40 the tenth midpoint fell 4.5×10⁻⁵ above the zero, and the moved point 2.8×10⁻⁴ below it.
- So the stop sits at the change itself, at every cutoff.

**Next,** on Blake's word: `N = 48` for T5's top, by its own dated commit with its terms first, for the units' review before it runs; then the record, labelled as MIT's own, with the census page's note. T4/R4 stays as recorded; any other rule for it takes a dated commit, chosen knowing this stop.

## 15. 2026-11-05T13:58:43Z: T5's top at `N = 48`, its terms, its two trees and the solves' tree

Drafted on Blake's word ("Draft if/when gucci") and staged on his word ("get me to the point where all I need to say is 'go'"). This tree's commit, its push and the solves follow his "go". Nothing at `N = 48` has been solved or read.

**The terms,** `run/TOP48.md`, 2899 words, as DESIGN.md section 4 asks of `N = 48`'s commit: what counts as open, the ladder with its band and identity pairs, its own control evidence, and the three laws' values at `N = 48`, first. The targets are T5's nine points above 90.51 not classified on `N = 24`, 32 and 40, both ways: 116 to 132. The in-row controls, 100, 106 and 112, Elliptic (9, 3, 6), gate them: if one misses on the new ladder, no target is classified there. `N = 48` solves T5's whole grid, 31 points, and reads those twelve. The ladder is `N = 32`, 40 and 48, all three required for classification, with the first ladder's band, guard and both verdicts, and each point's reading on the first ladder stays the record, beside the new one. At 127 to 132 the new ladder tests the failure the design named, the 24-to-32 distance over the guard with the records agreeing. At 116, 120 and 124 it sets aside `N = 24`'s other type or indices, which the design did not name, for an INFERRED reason, the events' motion with the cutoff. A classification on it establishes the type under this computation's rule at the three tested cutoffs, not at every higher one. The six fresh points are solved and read at `N = 48` first, with marks restated for the new ladder: C3R/R4 at 0.30 is marked Unresolved as built, by D's flag at 48 alone, and P5 at 0.24's as-built verdict is reported, not marked. Before any read at 48, the stored reads at 32 and 40 are read again on the run's machine and must equal their records. The expectations (`dev/runs/014_top48_expectations/`, INFERRED) keep the design's pinned laws at 48, with their miss at 40, and set the same laws refitted on 24, 32 and 40 beside them.

**The code.** `grid.py` gains the new ladder, the targets, the in-row controls, `PATHS_48` and `PASS_MARKS_48`. `fresh.py` tests marks on any ladder, the first ladder's test unchanged, and gains the new ladder's pass and refusal. `jobs.py` gains `recheck48`, `read48`, `identity48`, `reading48`, `fresh48` and `top48`, each behind its gate. The old `read` and `identity` refuse `N = 48`, and a path at 48 outside `PATHS_48` refuses. `ladder_reading` gives every first-ladder reading file on record, field for field. `runner.py` gains the kinds. `SOLVE_PINS` stays `391b097f` alone: this tree solves at 48 and reads nothing there, and the reads' tree adds its pin, with its own note.

**The review.** v1 (`top48_review_v1.zip`): both units GO after fixes, nothing FATAL, keeping the ladder, the control gates, the recheck, note B's structure and all six of my choices. v2 (`top48_fixes_v2.zip`) applied UA 2, 3 and 4 and UB 3 and 4 as written, and UA 5, UA 6 and UB 1 with changes of mine: "this computation's rule" for "the registered rule"; the wall time "about one to two days", with its basis; and "the 24-to-32 distance over the guard ... which the reads find at 126 to 132" for "identity alone ... as at 126 to 132". UB kept all four changes, and UA asked for no further fixes. Off this machine, both found `test_top48`'s first-ladder reading of T5 one unit in the last place of an unscored field at 129; it is exact here, and section 4 names the run's machine for the recheck. On v2 both units GO for the solves alone; the reads' tree and note B take their own commit.

**Tests, on this tree:** `dev/test_top48.py`, 66 claims; `dev/test_jobs.py`, 58; `dev/test_locate.py`, 46; all PASS. A defect of mine is fixed: `test_locate.py`'s allowlist claim read the repo's `FROZEN.json`, which has held T4/R5 since the locator landed, so every rerun after `87dedb00` failed it. It now reads `FROZEN.json` at the reads' commit.

**The locator's records** ride with this commit: entry 14, `dev/runs/013_locator_reading/`, the two job records, their logs and `RUNLOG.json`. Its output files stay on the bench, each named by its SHA-256 in its job record.

**Pins:** the manifest moves to `80df072cca091ce8722ba593b79580e4132b37db0e9a62a31bc324c445f9ebcf`; the solves' pin is unchanged.

**Next,** on Blake's "go": this commit, pushed, then `runner.py run/out solves48`, T5's whole grid and the four fresh paths at `N = 48`, four at a time, about one to two days (INFERRED). After the last solve, on his word, the reads' tree and note B.

## 16. 2026-11-07T05:33:01Z: the solves at `N = 48` ended, every point accepted

**The solves** at `N = 48` ended at 2026-11-07 05:21:14Z, 23.2 hours after their launch on Blake's "go": all five path jobs, T5's whole grid and the four fresh paths, completed with exit 0, and none failed. Every path log has all its points accepted, 37 in all: T5's 31, P5's and C3R/R4's two each, C2a/R5's and C2b's one each. Each seed's check at 48 passed. Every job record names the manifest the solves ran under, `80df072cca091ce8722ba593b79580e4132b37db0e9a62a31bc324c445f9ebcf`, and the 10 files the records logged match their SHA-256; the manifest equalled that pin at the end. These are the only checks `run/TOP48.md` section 7 allows between the two pins, on solve fields alone. Nothing at `N = 48` has been read.

**The reached points.** Every point's reached ε lies within 2.8×10⁻⁶ of its target, relatively. The fresh paths reached the same ε as at `N = 40`, bit for bit. T5's differ from `N = 40`'s at 20 of its 31 points, by at most 2.8×10⁻¹² of the target, as between the earlier cutoffs: 8.2×10⁻¹⁰ from 24 to 32, and 5.6×10⁻¹¹ from 32 to 40.

**The cost,** against section 8's INFERRED projection. T5's path took 83430 s, 23.2 hours: four jobs at a time for its first 5.3 hours and alone after, its points alone taking 1.96 to 2.55 times their `N = 40` time. P5's took 5.32 hours, C3R/R4's 4.88, C2a/R5's 2.34 and C2b's 0.73, each inside its projected range. The peak resident size was 1.21 to 1.54 GiB a job.

**Next,** on Blake's word: the reads' tree (section 7, step 3), `SOLVE_PINS` gaining `80df072c`, re-pinned, in one commit with note B on the census page, its four values filled. Then the reads, each kind after the one before has passed: the recheck, the fresh controls, T5's points, and `top48`.

## 17. 2026-11-07T06:04:36Z: the reads' tree and note B, before any read at `N = 48`

On Blake's word ("commit and push if/when good"), after both units' GO on v1 with no fixes. Nothing at `N = 48` has been read.

**The tree.** `run/jobs.py`'s `SOLVE_PINS` gains `80df072c`, the manifest the five paths at `N = 48` ran under, read from their job records. It is the tree's one change in the manifest, which moves to the pin below; with that line reverted, the tree re-pins to `80df072c` (the packet's arm 1, which UB checked against main). `dev/test_top48.py`'s pin claim follows the change: it asks for the two pins, and two claims beside it ask that each path at `N = 48` pass the solve-state gate, its whole entry held and every point accepted, and that with the first pin alone each refuse, naming "not a solve pin". `dev/runs/015_solve_checks_48/` holds the checks between the two pins: each seed's check, each point's acceptance, each job record's manifest and files, and the launch's events, with 0 failures. Beyond `run/TOP48.md` section 7's two checks, and deciding nothing, it also sets each point's reached amplitude against its record at `N = 40`, as entry 16 reports. Both units kept that look, in the script and in note B, so the record shows where it went past the terms' "only checks".

**The review.** `reads48_review_v1.zip` (`646ac29b`): both units GO with no fixes, keeping all five of my choices: `test_top48` changed in place, the solves' tree's version staying on main at `a27a093c`; the commit's contents, as the dated note's commit chose them; the date; the Status line unchanged; and this entry with the commit. The arms that must go red, the packet's `checks/mutations_v1.py`, went red as named.

**Rerun elsewhere.** Three claims are exact on the run's machine alone, and elsewhere agree to round-off, not bit for bit. `test_top48`'s section 2 claim for T5 differs by one unit in the last place of the unscored `rel_change` at 129, so the packet's mutation check, which asks that exactly two claims fail, finds three. `test_jobs`'s "the resumed path equals the stored one" and "the resumed read equals M8.18's record" fail off this machine, with 16 and 5453 differences where UB ran them. Re-solving C2b at `N = 24`, UB found the solutions agreeing to 1.6×10⁻¹⁶ to 3.6×10⁻¹⁵ relative, `m`, `lam` and the amplitude to the last digit or two, `floor_rel` differing by a factor of 2.2 and Newton's evaluation count at one point: round-off from another machine, not a defect.

**Tests, on this tree:** `dev/test_top48.py`, 68 claims; `dev/test_jobs.py`, 58; `dev/test_locate.py`, 46; all PASS, with outputs equal to the reviewed ones but for a temporary folder's name in `test_jobs.out`.

**The solves' records** ride with this commit: entry 16, the five paths' solve fields at `N = 48`, their job records and logs, and `RUNLOG.json`. Their solutions stay on the bench, each named by its SHA-256 in its job record.

**Note B,** on the census page under § V, step 5, after the locator's note: v2's wording with its four values filled, the date, the two pins and the solves, and the Inputs line naming `run/TOP48.md`. It names this tree's pin, so `jobs.note_gate` passes on its commit.

**Pins:** the manifest moves to `dbf9e7cfce8bce4186421b1cc126c991e7f99212299a2c4a8b7917d1624aba9e`; the solves at `N = 48` ran under `80df072cca091ce8722ba593b79580e4132b37db0e9a62a31bc324c445f9ebcf`.

**Next,** on Blake's word: the reads under this pin, each given this commit: `rechecks48` first; then the fresh controls' `reads48`, `identities48`, `readings48` and `fresh48`; then T5's; then `top48`.

## 18. 2026-11-07T09:17:02Z: the reads at `N = 48` ended: the fresh controls passed, the in-row controls at 100 and 106 missed, and no target is classified on the new ladder

On Blake's "Yes, start them". One task ran the reads under `dbf9e7cf` from 06:10:28Z to 08:14:48Z on 2026-11-07, 124 minutes, each launch given the note's commit: 10 launches in `run/TOP48.md` section 7's order, 27 jobs, all completed with exit 0 and none failed. Every job record names the manifest `dbf9e7cf`, and the 27 files the records logged match their SHA-256. No solution was written. The peak resident size was 1.96 GiB a job.

**The recheck passed.** The stored solutions at `N = 32` and 40, read again on this tree and machine at every point the new ladder reads, 36 point-reads in all (the fresh controls' six points and T5's twelve, at each cutoff), equal their stored reads field for field, value and type, timings aside: 0 differences. 55 minutes of job time and 22 of wall time, where section 8 put about an hour.

**The fresh controls passed at `N = 48`:** all six points hold every mark, the pass on record in `fresh48_pass_d74efe6efa48.json`. Each seed's check passed at 32, 40 and 48; K1 and the case's indices hold at each cutoff; branch identity is kept on both pairs, 4.1×10⁻¹⁵ to 6.3×10⁻¹² at (40, 48); the changed verdict is converged with the case's type at all six. As built: converged at P5 0.30, C2b and C2a/R5; Unresolved at C3R/R4 0.20 by D's flag at `N = 40` and 48 alone, and at C3R/R4 0.30 by D's flag at 48 alone, B clearing it each time, as stated. P5 at 0.24, reported and not marked: as built converged, Hyperbolic (5, 1, 4). Its pair, read as one set, steps 5.2×10⁻⁶ from 32 to 40 and 1.3×10⁻¹⁴ from 40 to 48, which the as-built rule reads as contraction.

**T5 at `N = 48`.** The seed's check passed, and the twelve points read. Branch identity at (40, 48) runs 2.7×10⁻⁴ to 4.5×10⁻⁴, 22 to 37 times under the guard, kept at every point but 126, where the records differ.

**The in-row controls at 100 and 106 missed.** At both, the records at 32, 40 and 48 are Elliptic (9, 3, 6), with nothing unresolved, K1 holds, and branch identity is kept on both pairs. The rule reads both Unresolved, as built and changed alike, on one tested group each, the Krein-negative imaginary group at 0.3938i at 100 and 0.3742i at 106: "non-contracting above the floor". Its step from 40 to 48 is 3.68×10⁻⁵ at 100 and 5.34×10⁻⁵ at 106, against 3.59×10⁻⁵ and 3.12×10⁻⁵ from 32 to 40, above the floor of 1.30×10⁻⁵ and 1.35×10⁻⁵, so the rule shows no rate (`instrument/convergence.py`, step 4). Its distance to the nearest event, A's gray zone, is 0.394 and 0.374. On the first ladder both points were classified: there the step from 24 to 32 was 1.61×10⁻² for this group at 100, and 4.15×10⁻² for the set that held it at 106, and the sequence contracted. At 112 the in-row control holds, Elliptic (9, 3, 6) both ways, its group at 0.3924i stepping 7.78×10⁻⁴ and then 1.93×10⁻⁴. The cause of the two misses is not established by these records (OPEN).

**So no target is classified on the new ladder.** By `run/TOP48.md` sections 4 and 6, each target's reading there is reported raw with the miss named, and each stays open; on the first ladder each stays not classified, with its causes (entry 11). The raw readings on 32, 40 and 48, the same as built and changed at every target:
- **116 and 120:** converged, Elliptic (9, 3, 6).
- **124:** converged, Elliptic (4, 0, 4).
- **126:** Unresolved. The type differs along the ladder: Hyperbolic (4, 0, 4) at 32 and 40, Elliptic (4, 0, 4) at 48, where the quartet at 0.0075 + 0.1537i at 40 is two imaginary groups, 0.1421i (Krein positive) and 0.1653i (Krein negative). Two tested sets' counts differ between cutoffs, and branch identity fails between 40 and 48: aligned distance 4.15×10⁻⁴, under the guard, the records differ.
- **127 to 132:** converged, Hyperbolic (4, 0, 4), the quartet 140 to 753 times its uncertainty from the axis.

**Against section 5's statements,** all INFERRED before any solve:
- **The types:** as stated at 116, 120, 124 and 127 to 132. At 126, stated Hyperbolic and too close to call, the record at 48 is Elliptic. At `N = 48` the type changes between 126 and 127, where the collision was stated at 125.98.
- **The quartet's real part at 48:** 0.0634 at 127, 0.0902 at 128, 0.1106 at 129, 0.1277 at 130 and 0.1560 at 132, each below the range stated from the laws on `N = 24`, 32 and 40. Its step from 40 to 48 is 7.5×10⁻⁴ to 1.5×10⁻³, against the stated 1×10⁻⁴ to 7×10⁻⁴, and 0.216 to 0.227 of the step from 32 to 40. The design's laws as pinned missed again, as stated: 0.0288, −0.0015 and 0.0420 at 128, and 0.1159, 0.0925 and 0.1311 at 132.
- **Branch identity at (40, 48):** 2.7×10⁻⁴ to 4.5×10⁻⁴, under the stated 5×10⁻⁴ to 9×10⁻⁴.
- **The branch:** identity at (40, 48) holds to the top but for 126's change of type, and 112 holds its marks; the misses at 100 and 106 are the rule's contraction test, not branch identity.
- **The tolerances at 48** (no gap between τ(40) and τ(48), K1's separation, L's gray zone, n(D)'s zone): K1 holds, and n(D)'s inherited zone flags nothing at T5, at every point and cutoff; the stated margins are not computed here.
- **The cost:** T5's read took 2860 s for its twelve points, about 4.0 minutes a point, under the stated 7 to 10; the controls' reads 11 to 42 minutes a point, within the stated 6 to 48.

**Next,** on Blake's word: `run/TOP48.md` section 7, step 5, the record labelled MIT's own, with the census page's note. Section 6 adds nothing under these terms: no further cutoff, tolerance, ladder or point without another dated decision, its terms first.

## 19. 2026-11-07T15:25:58Z: the record and note C, with the reads' records at `N = 48` and the solutions

On Blake's word ("commit and push if gucci"), after both units' GO on v2.

**The record.** `RECORD.md`, built by `tools/build_record.py`, both new and both outside the manifest, which stays at the pin below. It gives custody by stage, the fresh controls on both ladders, the twelve, the rows point by point, T4/R4's locator, T5's top on both ladders, the statements made before the reads beside what they found, what stays open, deviations and looks beyond the terms, and reproduction. The builder reads the run's logged files in `run/out/`, `run/ENVIRONMENT.json`, the statements in `run/DESIGN.md` and `run/TOP48.md`, M8.17's stored records, the repository's commit history, and the outputs of `dev/runs/011_row_readings/` and `dev/runs/013_locator_reading/`. It refuses a failed launch, a launch out of its stage's order, a logged file off its SHA-256 (162 files), a classification that does not recompute from its reading file with `census_lib` (141 points), a quoted statement the terms do not hold, and a dev run's output that does not say what the record takes from it. Its fits and extrapolations are labelled INFERRED: the quartet's limit on the ratio of its last two steps, the collision law, and the zero of L's sign-changing eigenvalue with K1's neighbourhood around it.

**The review.** On v1 (`record_review_v1.zip`, `491382dc`) both units gave GO after fixes. UA asked that the record name every source the builder reads, that the bar on `U` at 126 be given as `run/TOP48.md` section 1 gives it, 7.50×10⁻⁴ against the distance 7.50×10⁻³, and that note C name branch identity's failure at 126, where the records' types differ. UB asked that the solutions come with the record, as entry 10 said; that note C set "none of the top is classified" beside the raw values; that section 7's branch-identity row read "missed, under the range"; and that section 9 name the two looks after the reads. Both kept the four looks beyond the terms. v2 carried every fix, the builder also checking `dev/runs/011_row_readings/` for the new link section 7 cites, and both units gave GO on it. Before the push they asked for three confirmations, which the landing makes, stopping on any miss: every solution in the commit, listed in `SHA256SUMS` and equal to the SHA-256 its job record logged; the builder's `--check` on the final tree, with the bench's read and reading files linked beside it; and only the note's bullets on the census page, no comment and no unit named.

**The commit carries** `RECORD.md`, the builder, entries 18 and 19, and the reads' records at `N = 48`: 27 job records with each file's SHA-256, their logs, `TOP48.json`, the fresh controls' pass, the ten rechecks and the five identity files at (40, 48), with `RUNLOG.json`. It also carries the 37 solutions, 3.26 MB, the `.npz` files entry 10 said come with the record, and `SHA256SUMS`, which lists the committed tree. The read and reading files, the locator's two records among them, stay on the bench, 52 files and 412 MB, each named by its SHA-256 in the job record that wrote it; they can be read again from the solutions on the pinned trees, and UA asks that they be kept for a supplementary archive.

**Note C,** on the census page under § V, step 5, after note B: the rows, the twelve, T4's change of type in `R4`, T5's top on the second ladder, what stays open, and the statements made before the reads beside what they found. The Inputs line names `RECORD.md`.

**Pin:** the manifest stays at `dbf9e7cfce8bce4186421b1cc126c991e7f99212299a2c4a8b7917d1624aba9e`.

**Next,** on Blake's word, each with its terms first: what the eigenmodes do on the geometry, the softening modes behind T4's index change in `R4` and T5's moving quartet, with the misses at 100 and 106 kept as part of the evidence; and why the steps at 100 and 106 stop shrinking, which only a new rule under its own terms could test.
