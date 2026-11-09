# M8.19: development log

Bench log of M8.19's driver, from its first line to the freeze. Entries are never edited; numbers come from headings, times from the clock.

## 1. 2026-11-08T15:07:13Z: the start, and what the dry run may touch

Blake: "Yes, let's start the driver. And we should probably do a dry bench run up until a point (without looking at answers obviously) to make sure the instrument is ok. We only have one shot at this."

The driver sits beside M8.15.x's frozen solver, `soft-slot-dynamics-m8-15x/m8_15x_solver/` at `97a8c08`, and imports it in place from the repository. That folder's `SHA256SUMS` passes 196 of 196 here, and the freeze will pin those bytes.

The terms (`registration/m8_19_task_details.md`, merged on OpenWave #698) seal every target and the coherent row in `R5` until the freeze: no finite-element solve, no spectrum and no evolution on them. The dry run is held to that line:
- the whole pipeline end to end on the controls, at their recorded points: the orchestrator's waves of four single-thread jobs, the gates, each job's own record and the relaunch rule;
- the target code path run on a control standing in for a target;
- each target's case set up without a solve, so that a broken case definition shows before the freeze;
- the fresh controls, C3 at `ε` = 3 and C2a/R4 at 1 with `T` = 2750, read for plumbing only, at short `T`, and never for a verdict.

## 2. 2026-11-08T15:33:42Z: the design, and the dry run's scope narrowed

`DESIGN.md` v1 is written: the jobs, the gates as the driver reads them, the coherent row's case, the orchestrator and the dry run, with five readings for Blake to confirm or strike.

**The scope narrowed.** Entry 1 says the fresh controls are read "at short `T`". The terms are narrower for C3 at `ε` = 3: the driver "reaches C3 at `ε` = 3 and reads its gates there, without evolving it", and the sealing allows "no evolution of any state but the controls' recorded ones". So on the bench C3 at 3 is solved and its gates read, and it is never evolved. C2a/R4 at 1 is evolved only inside its recorded `T` = 1000, in the smoke test, where its path is M8.15's recorded C2a control's.

**What the dry run may evolve:** M8.15's recorded control states (C1 at 6, C2a, C2b and C3 at 1, C3's rate run) and M8.15.x's recorded C2a/R4 test at 8, at their recorded `T` or shorter. The stand-in's test refuses any other point or `T` before its first step.

**The layout.** The bench mirrors the repository: `../soft-slot-dynamics-m8-15x` is a link to the worktree's frozen folder, so the driver's relative path to the instrument is the one the run uses.

**The base of the bit-for-bit tests:** M8.15.x's own records from its qualification run on the frozen bytes, `qualification/solver/m8_15_solver/out/` (`branch_C2a_R4.json`, `persist_C2a_R4_8.npy`, the five `dynamics_*` records) and `qualification/qual_2026-10-09/controls/control_1a_rerun.json`. They were made on macOS 15.8; this machine runs 15.8.2 (24H232), so the first comparisons also test whether the OS move changed the instrument's bits.

## 3. 2026-11-08T16:08:42Z: the driver built; control 1a bit for bit; the order on a stub

**Built:** `run/m819_branch.py` (M8.15.x's `m815_branch.py` with its changes; `stage`, `write_json_atomic`, `cj` to `slow_lineage` and `decide` with the types and bisection loops checked verbatim against the frozen file), `run/m819_gates.py`, `run/m819_run.py`, `run/write_guard.py`, the terms as `run/m8_19_task_details.md` (SHA-256 `f2295e0b…`, equal to OpenWave's merged task document on `upstream/main`), and `reference/` by `tools/copy_from_mit.py`: M8.17's four T1 and T4 rows at `7b66f8a` and M8.16.1's C2a and C2a/R5 at `292b158`, each at the SHA-256 its run's log records. The stretches the driver derives from those records are the terms' table: 5 and 8 points, 14, 8, 11 and 4, every reference mode of count 1.

**Control 1a, bit for bit.** The `p5a` job's arm equals `control_1a_rerun.json`'s M8.15.x arm in every leaf but its two timings (`dev/compare_qual.py p5a`): the seed solve stops at iteration 3 at 4.3×10⁻¹³. So this OS reproduces a level-2 Newton solve of the qualification's.

**The sealed cases set up without a solve** (`dev/setup_sealed.py`, `.out`): T1 and T4 in both slots and C2a in `R5`, at levels 2 and 3, with C2a/R4 beside them. Every case builds; T4's third outside point is read from `d0de8ca`. The seed's `Q` against the exact one is within 4.2×10⁻⁵ at level 2 and 2.1×10⁻⁶ at level 3. The coherent row's, against the one constant the driver adds, 2289/2288, is −3.3×10⁻⁶ and −1.8×10⁻⁷, where C2a/R4's is +4.1×10⁻⁶ and +2.0×10⁻⁷.

**A defect found and fixed in the orchestrator.** The first stub run of the registered order hung: a job that exits fast can be reaped by Python's own `subprocess` cleanup, which polls the child of a dropped `Popen` when the next job starts, so the orchestrator's `os.waitpid(-1, 0)` never saw that job end. The orchestrator now holds each job's `Popen` and polls it once a second. Nothing had run on it but the stub.

**The registered order on a stub** (`dev/test_scope.py`, `.out`, with `dev/stub_branch.py`): 22 of 22 checks over four scenarios (the full order with the longest control at 15750; gate 1 failing; the longest control failing; a gates job raising on every start).

**The freeze rehearsed** (`dev/test_freeze.py`, `.out`): on a temporary copy, 14 files pinned, the freeze read back valid, and each of 8 arms refused for its reason. This folder's `run/` has no `FROZEN.json`.

**Running:** the stand-in's gates job (`dev/runs/002_standin_gates/`, started directly, ahead of its bench plan), and the failure-path tests on C1 at short `T`.

## 4. 2026-11-08T16:15:05Z: the stand-in's gates bit for bit; the arms and the failure paths

**The stand-in's gates job** (`dev/runs/002_standin_gates/`, the target path on C2a/R4 with every ladder point from 0.25 to 8 as its stretch) ran in 28 minutes. Its level-3 and level-2 points equal M8.15.x's qualification record `branch_C2a_R4.json` at all 11 points, 770 leaves at each level, residuals included (`dev/compare_qual.py standin`). So the move to macOS 15.8.2 changed no bit of the instrument at level 3 either.

**Its gates:** all 11 points pass gates 2 to 7, and the search lands at 8 with `T` = 1000, M8.15.x's recorded test. Gate 5's share runs from 0.111 to 0.116, with `B` two-dimensional at every point and `direction()` reproduced exactly; gate 4's levels differ by 2.8% at 0.25 down to 0.17% at 8, and the harmonic readings by at most 0.36%; gate 6 gives 2750 at 1, as the terms state for the duration control (`P` = 2717.7).

**The gates' mutation arms** (`dev/test_gates.py` on those points, `.out`): 36 of 36. Arm 0 reads every stored point again and gets its stored reading; each gate turns red for its named reason; gate 6 rounds as stated; a red top point moves the test down one point; the duration control does not read gate 4; and the guards refuse as named. One defect in the test script itself (a float key passed as a keyword) was fixed before the passing run.

**The failure paths** (`dev/test_launch.py`, `.out`, on C1 at a short `T`): 17 of 17 over four scenarios: a job raising on every start, a killed job, a killed orchestrator with the job outliving it, and a refusal stopping the run.

**Next:** the smoke test, then the dry run's full queue, with the stand-in going through the coherent row's own job (`job_coherent` on C2a/R4 to 8), so that the sealed row's path, types and validity included, is compared with M8.15.x's record too.

## 5. 2026-11-08T16:24:26Z: the smoke test; the dry run's queue started

**The smoke test** (`dev/smoke.py`, its first run kept as `dev/smoke_first.out` and `dev/runs/smoke_first/`): four jobs at once and never more; the terms' order, the fifth job starting only as one of the four ended; every job in its own folder, 23 files with no shared path. Each job's series to `T` = 20 equals the first rows of M8.15.x's recorded series for the same control, bit for bit, C2a/R4's duration control against the C2a control's, so the target path reaches M8.15's recorded C2a state at 1. Its gates pass with gate 6's `T` = 2750. Every sampled job ran on one thread. One check was defined wrongly: it required gate 1's reader, which runs about a second, to be sampled at a two-second interval. The check now covers the jobs that compute; the smoke test reruns after the dry run. At `T` = 20 the frozen evaluator reads every run Invalid, since its drift rule averages a tenth of so few observations; that is read for nothing.

**The dry run's queue** (`run/m819_run.py --bench dryrun`, into `dev/runs/dryrun/`) started: the stand-in through `job_coherent` on C2a/R4 to 8, its plan and its test; M8.15's dynamics controls and C3's rate run at `T` = 1000; `p5a`; C3 at 3 and C2a/R4 at 1 read without evolving; gate 1.

## 6. 2026-11-08T19:59:03Z: the dry run complete, bit for bit; the smoke test rerun

**The dry run's queue** (`dev/runs/dryrun/`, 16:24:16Z to 19:47:25Z, 3 h 23 min) completed all 12 jobs on their first start, with no relaunch, crash, refusal or stop. The 43 files the log records each equal their SHA-256 there, and nothing was left in staging. Nothing sealed was solved, given a spectrum or evolved.

**The stand-in through the coherent row's own job** (`job_coherent` on C2a/R4 to 8, 49 minutes): its level-3 and level-2 points equal `branch_C2a_R4.json` at all 11 points, 770 leaves at each level, and so do M8.15's frozen types at the 11 points, all Elliptic, the 4 cross-checks and the validity check at 0.25; neither record has a change of type through 8. The ladder reads as established, its stretch all 11 points. Its gates read as run 002's did, point for point. The plan holds one test, at 8 with `T` = 1000 (`P` = 404.7). The test (1 h 46 min) equals M8.15.x's recorded test at 8 in all 22 fields `run_test` returns, and its 1002-row series equals `persist_C2a_R4_8.npy` byte for byte. So the path the coherent row in `R5` takes, types and validity included, reproduces M8.15.x's record on C2a/R4.

**M8.15's dynamics gate:** C1, C2a, C2b, C3 and C3's rate run each equal the qualification's record in every field but its time, and their series byte for byte. Gate 1 reads C1, C2a and C2b Persisting and C3 Failing (`t_fail` = 583.3), each valid, and the rate run's fitted rate 0.0097405 against level 2's linear 0.0097375, 0.03% apart.

**Control 1a** (`p5a`): its arm equals M8.15.x's in all 73 leaves but the two timings, and the seed solve stops below 10⁻¹¹ under the repaired test.

**The two fresh controls, read without evolving.** C3 at 3 is reached at 2.99999999, residual 7.7×10⁻¹³; M8.15.x's own recorded points land up to 3.5×10⁻⁷ from their targets. Its cluster is closed at the frozen dimension 8, with an Ω-Gram ratio of 0.956; the margin holds at `T` = 1000, `r` = 7.1×10⁻¹⁶; the perturbation's `E_η` is 4.9×10⁻⁴. The duration control passes gates 2, 3, 5, 6 and 7 at 1, with a share of 0.115, `B` two-dimensional and the draw reproducing `direction()` exactly, and gate 6 gives `T` = 2750. Gate 1 reads both as not passed on the bench, as it must: C3 at 3 because the job did not evolve, the duration control by its rule, with `test` null in `c2a.json`. So `all_passed` is false on the bench; the registered run evolves both. The duration control's entry in `CONTROLS.json` carries its rule, not its verdict; the verdict is `c2a.json`'s.

**DESIGN's steps 8 and 10:** the gates' arms on the dry run's own `gates.json`, 36 of 36, each line equal to entry 4's (`dev/test_gates_dryrun.out`); `tools/periods.py`, in the registration folder, rerun on the repository's records, reproduces its committed `periods.out` byte for byte, 51 lines.

**The smoke test, rerun** with its check fixed (`dev/smoke.out`, `dev/runs/smoke/`): 11 of 11 checks, 19:49:32Z to 19:58:25Z: four jobs at once and never more; one thread each, every computing job sampled; the terms' order, the fifth job starting only after one of the four completed; every job in its own folder, 23 files with no shared path; and each job's series to `T` = 20 equal to the first rows of M8.15.x's recorded series, bit for bit, the duration control's against C2a's.

**Times, from the log:** the stand-in's gates 49 minutes and its test 1 h 46 min; C1 2 h 2 min, C2a 1 h 59 min, C2b 1 h 15 min, C3 1 h 47 min, the rate run 1 h 24 min; the duration control 8 minutes; `p5a`, `c3e3`, the plan and gate 1 under half a minute each. C1, C2a and C2b ran beside three other jobs throughout and took 1.27 to 1.36 times the qualification's recorded seconds; C3 and the rate run, beside fewer jobs for part of their time, 1.01 and 1.05.

**Next:** the report to Blake, with DESIGN's five readings to confirm or strike.

## 7. 2026-11-08T20:01:27Z: the record job on the dry run's real outputs

**Why:** the dry run's queue did not include wave 5's record job, and `dev/test_scope.py` had run it only on the stub's records.

**`dev/test_record.py`** (`.out`) runs `job_record` as written on the dry run's folders, each file checked against the log's SHA-256, writing only to temporary folders: 9 of 9.
- With `ROWS` narrowed to the stand-in's gates job, the record holds gate 1 as filed, and the stand-in's stretch with its points, causes and test point as `gates.json` holds them. Its test at 8 is as `test.json` holds it: Persists, valid, `T` = 1000, 2.47 periods.
- Read as the coherent row, the ladder's outcome is recorded apart, established.
- With the registered `ROWS` on the same root, where no target's job ran, all six stretches the terms name are in the record, each sent for adjudication with its job's cause.

The dry run's folder is unchanged: every file is at its logged SHA-256, and no `record/` is in it.

**Next:** the report to Blake, with DESIGN's five readings to confirm or strike.

## 8. 2026-11-09T01:35:05Z: the five readings as ruled; the driver changed and its tests rerun

**The ruling:** Blake's go, on two reviews of the report that followed entry 7: readings 1, 2, 3 and 5 confirmed, with the reviews' additions, and reading 4 struck. `DESIGN.md`, now v2, has the readings as ruled, and they go into the request for the go.

**What changed:**
- `run/m819_gates.py`, reading 1: when the count of candidates within 5% of the slowest differs from the reference's multiplicity, gate 3 now records that the mode is not identified, with the count and the candidates' moduli, and no longer calls the count the mode's multiplicity. The gate is unchanged, and no stored reading of the dry run has that refusal. For reading 3, `other_elliptic_runs` is new: the Elliptic runs of an established ladder that share no point with its stretch, and none on a ladder not established.
- `run/m819_branch.py`, reading 3: `job_coherent` takes its other runs from `other_elliptic_runs`. Before, it listed them on an unestablished ladder too, where a run holding the record's own points could appear. `job_record` names each in `newly_identified`, apart from the terms' stretches, with the outcome "no test fixed": a newly identified Elliptic stretch, which these terms fix no test for, so S5 stays open for it, for the maintainer. If the coherent row's job does not complete, `coherent_ladder` carries that job's cause, for adjudication, where it was null.
- `run/m819_run.py`, reading 4 struck: a launch starts each job at most once. A crashed or killed start leaves the job pending, what does not depend on it carries on, and the launch ends when nothing more can start. A job's three starts are three launches, each through `validate_frozen` and the environment check in `main()`.
- `dev/stub_branch.py`: the stub's coherent outcome carries `other_elliptic_runs`, which the record now reads.
- `DESIGN.md` also says that other Elliptic runs get no gates read, as the code always had it.
- `dev/m819_branch_vs_m815_branch.diff`, regenerated: 1,007 lines.

**The reruns,** each output in place of the one before:
- `dev/test_gates.py`: 40 of 40, on the dry run's `gates.json` (`dev/test_gates_dryrun.out`) and on the stand-in's rerun below (`dev/test_gates.out`), line for line the same. They are entry 4's 36, with the two gate-3 arms' expected wording changed, plus one arm for the near twin's moduli and three for the other runs.
- `dev/test_record.py`: 14 of 14. New: two other Elliptic runs are named apart from the terms' stretches, each with no test fixed and S5 open for it, and neither Untested; and with no target's job run, the coherent row's ladder goes for adjudication with its job's cause.
- `dev/test_launch.py`: 23 of 23. A job raising on every start takes three launches, one start each; the first two end with it and what needs it pending, and on the third it ends and what needs it is not run. A killed job waits for the relaunch, which completes it. No launch started any job twice.
- `dev/test_scope.py`: 30 of 30, the registered order on the stub. Its scenario D now spans three launches, with the plan waiting for the third. The coherent row's ladder is recorded apart in A and sent for adjudication in B, gate 1 named, and no launch started a job twice.
- `dev/test_freeze.py`: 25 of 25.
- `dev/setup_sealed.py`: entry 3's 15 lines, apart from times.
- `dev/smoke.py`: 11 of 11, 01:16:38Z to 01:32:53Z.
- **The stand-in's gates job on the new code** (`dev/runs/003_standin_gates/`, 00:22:35Z to 01:15:50Z, with the SHA-256 of `m819_branch.py` and `m819_gates.py` the same at its end as at its start). Its `gates.json` equals the dry run's in 2,840 of its 2,841 leaves, the one apart being the level-3 time. Its 33 stored level-2 arrays equal the dry run's bit for bit, and `dev/compare_qual.py standin` finds its ladder equal to M8.15.x's record at both levels, types, cross-checks, validity and changes included (`compare_qual.out` there). Its test at 8 did not run again: its code did not change, and every input it reads is equal.

Nothing sealed was solved, given a spectrum or evolved.

**Wall time, INFERRED from the bench:** with jobs running 1.27 to 1.36 times slower four at once (entry 6), the expected run takes about 20 to 35 hours of wall time, not the terms' 15 to 25. T4's long tests, if their gates pass, run beside fewer jobs, where C3 and the rate run took 1.01 and 1.05 times their recorded seconds, so they should slow less.

**Next:** on Blake's word, the folder into the repository; then the request for the go on #698, with the five readings, which Blake posts; then the freeze.

## 9. 2026-11-09T16:23:34Z: the reviews' conditions met; the tests before the freeze on the final code; the folder to publish

**The word:** Blake's "continue if/when good", on two reviews of entry 8. One gives its go to publishing this folder and to drafting the request for the go, and holds the freeze and the run. The other gives its go once two more failure paths are confirmed, and asks that the stand-in's test at 8 run again on the code to be frozen, or be tagged INFERRED. It ran again, below.

**Two failure paths,** in `dev/test_scope.py`, now 43 of 43, on the stub, which raises for the jobs a scenario names:
- E. A wave-1 control, C2a, raises on every start. It takes one start in each of three launches; gate 1 runs only after the third, and fails on it; no gates job or plan ever starts, and each is not run, with gate 1 named; no sealed guard is called; and the record sends all six stretches and the coherent row's ladder to adjudication.
- F. The longest control raises on every start, over three launches. The test longer than 2750 never starts and is not run, with "c2a_long did not complete"; the tests up to 2750 complete on the first launch; and the record sends that stretch to adjudication with the cause. Its relaunches run the plan again, through `extend()`, which no test had covered.

No launch started a job twice in scenarios A to F.

**The terms' tests before the freeze, on the final code** (`dev/runs/004_final_code/`, through `dev/launch_runner.py`): one launch, 14:39:34Z to 16:17:45Z, every job completed on its first start. `PIN.txt` there holds the SHA-256 of `m819_branch.py`, `m819_gates.py` and `m819_run.py`, and the six files under `run/` had the same SHA-256 at its end as at its start, the ones `SHA256SUMS` lists.
- The stand-in, C2a/R4 to 8 through the coherent row's own path: `dev/compare_qual.py standin` finds its points at both levels, its types, cross-checks, validity check and changes equal to `branch_C2a_R4.json`, and its test at 8, `T` = 1000, equal to M8.15.x's in all 22 fields `run_test` returns, its 1002-row series equal to `persist_C2a_R4_8.npy` byte for byte (`compare_qual.out`). Entry 8 inferred the test unchanged; it has now run on the code to be frozen.
- Control 1a: equal to M8.15.x's arm in all 73 leaves but its two timings (`compare_qual_p5a.out`).
- C3 at 3, reached and its gates read without evolving it; the duration control at 1, with `T` = 2750 from gate 6, without evolving it.
- Against the dry run (`dev/compare_runs.py`, new; `compare_dryrun.out`): every record of the six jobs equals the dry run's but in its times and memory peaks, and the 33 stored level-2 arrays and the test's series are equal byte for byte.

Nothing sealed was solved, given a spectrum or evolved.

**Entry 8's wall time, made precise.** Its 1.27 to 1.36 are entry 6's ratios: C1, C2a and C2b, each beside three other jobs throughout, against the seconds the qualification recorded for them. The terms' hours are M8.15's recorded times, so that is the comparison the estimate scales, and the estimate stands, INFERRED: about 20 to 35 hours for the expected run. The ratios are not a comparison with the same jobs run alone here. In this rerun the stand-in's level-3 ladder, beside other jobs for its first 7 minutes and alone after, took 1,724 s, against the dry run's 2,849 s beside three other jobs; its test at 8, alone, took 4,113 s, against 6,361 s.

**The folder to publish:** this folder at the commit, without caches, and without `dev/runs/launch_tests/` and `dev/runs/scope_tests/`. The failure-path and scope tests rebuild those two on every run, and the scope test's holds the stub's made-up records under the targets' names, which are not results; the tests' outputs, `dev/test_launch.out` and `dev/test_scope.out`, are in. The dry run's records are in, under `dev/runs/`. As M8.18's, `SHA256SUMS` lists every file in the folder but itself, `registration/` included, which is in the repository already and does not change.

**Next:** the folder into the repository, and the request for the go on #698, which Blake posts. At the go, `record_environment.py` writes `run/ENVIRONMENT.json` once and `write_guard.py` writes the freeze, on Blake's word; then the freeze block and the run.

## 10. 2026-11-09T17:32:31Z: the request for the go, reviewed; DESIGN.md's note on the readings' words

**The reviews,** relayed by Blake: both give their go on the request after fixes. Taken:
- the wall time also names the terms' longer case, about 2 to 3.5 months if T4's gates pass only at its stretches' lowest points (one review);
- the order: the folder checked against its `SHA256SUMS` before the freeze, since `write_guard.py` hashes the folder as it stands, so that `FROZEN.json` holds the bytes the request names (the other); the terms' "before the go", read literally, stated beside the reading the request asks the maintainer to confirm, with a stop if the freeze must come first (both);
- reading 3's stretch as the unbroken run of Elliptic ladder points that contains 2, as far below and above it as it goes, since "through 2" could be read as ending at 2 (the other). It starts at 0.25 only if the ladder's points at 0.354, 0.707 and 1.414, which M8.16.1 has no types for, read Elliptic, so the request does not say "from 0.25";
- reading 5 in the terms' words, "start and leave unfinished"; the opening names the setups' one decomposition, the symmetry projector's SVD; and `write_guard.py` as modelled on M8.18's, while `record_environment.py` is M8.18's byte for byte (the other, narrowed).

**DESIGN.md:** the other review asks for its readings in the request's words, since the go covers it and its reading 4 says "as M8.18's every relaunch was", where M8.18's run never relaunched. The readings as ruled stay as made, and a dated note after them gives the request's words for readings 3 to 5, the ones the maintainer is asked to confirm. No file under `run/` or `reference/` changed, so no test reran.

**Next:** on Blake's word, this folder into the repository with its new `SHA256SUMS`, and the request's hashes and links moved to that commit; then Blake posts the request on #698.
