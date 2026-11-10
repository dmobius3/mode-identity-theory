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

## 11. 2026-11-09T19:55:00Z: the go; the folder checked and the freeze written

**The go,** [`issuecomment-6749289423`](https://github.com/openwave-labs/openwave/pull/698#issuecomment-6749289423), at 2026-11-09T19:25:45Z, unedited: go for M8.19, covering the four SHA-256 values the request named and, beyond them, only `run/ENVIRONMENT.json`, written after the go and pinned by `FROZEN.json`. It confirms M8.18's order step for step and reads the terms' "before the go" as met. Readings 1, 2, 4 and 5 are confirmed as worded. Reading 3 is confirmed as a reading of how the record is written: any other Elliptic run is recorded apart, with no test fixed and never as Untested, so the record assigns it no ending under S5, and its standing under S5 is for the maintainer's adjudication. The ladder above 2 stays unruled, as the answer of 2026-11-07 left it. The adjudication applies the terms, the approval's four readings and the go. Kept as `../go_request_v1/go.json`.

**On reading 3:** the go does not take up the request's "S5 stays open for it", which `job_record` still writes as the reason beside the outcome "no test fixed". That outcome assigns no ending, as the go has it. The code stays as the go names it, and the adjudication reads the go's words.

**The checks before the write,** read-only (`../freeze/checks_before_write.py`, its output beside it), 31 of 31: the go live equals its kept copy and is unedited, by an OpenWave member; OpenWave's merged task document, read by API and from a clone's `upstream/main`, is at the terms' SHA-256, as is `run/m8_19_task_details.md`; MIT's `origin/main` is at `94a679ac`, no commit since touches this folder or the instrument, and the worktree's copies of both equal the commit's, with nothing untracked; the instrument link resolves to the worktree's instrument, whose manifest is at the go's SHA-256 and equal to its blob at `97a8c08`, whose `.py` files are at the manifest and equal to their blobs at `97a8c08`, whose `out/freeze_numbers.json` equals its blob, and which holds no cache; there is no `run/ENVIRONMENT.json`, `run/FROZEN.json`, `run/FROZEN_PIN` or `run/out/`; the 175 listed files the bench held are each at their SHA-256, and it lacked only `registration/`'s 8 and `SHA256SUMS`; no unlisted file is under `run/` or `reference/`, the unlisted ones all being under `dev/runs/launch_tests` and `dev/runs/scope_tests`, the scratch the failure-path and scope tests rebuild; no cache or `.DS_Store`; the 8 reference copies equal their blobs and `SOURCES.json`, which is at the go's SHA-256.

**The bench brought to the commit's tree:** `registration/`'s 8 files and `SHA256SUMS`, written by exclusive create from their blobs at `94a679ac`, each at its SHA-256 (`../freeze/bring_to_commit.py`).

**The check:** `shasum -a 256 -c SHA256SUMS` in this folder at 2026-11-09T19:52:58Z: 183 of 183 OK, exit 0 (`../freeze/sha256sums_check.out`, for the freeze block). This entry is the only change to a listed file since.

**The environment:** `python3 -I -B run/record_environment.py` wrote `run/ENVIRONMENT.json` at 2026-11-09T19:53:09Z, 1953 bytes, SHA-256 `43b7d084a46860ca1700030445569780d87edf5484b1801932b08903cdad3c3f`, and `--check` reads no difference. It equals M8.18's record in every field but the time: Python 3.13.13, NumPy 2.5.0 and SciPy 1.18.0 on Accelerate, no threading variable set, macOS 15.8.2 (24H232), the Apple M3 with 4 performance cores.

**The freeze:** `python3 -I -B run/write_guard.py` with the go's link, the terms read against the clone's `upstream/main`, wrote `run/FROZEN.json` at 2026-11-09T19:53:23Z, 9431 bytes, SHA-256 `1e5107d0c6117a7d45c378827b8ee6670c1ce8964b1099992be05e4769486393`, and `run/FROZEN_PIN`, which holds that SHA-256. It pins 16 files: the 6 under `run/` and 9 under `reference/` that `SHA256SUMS` lists, each at its line there, and `run/ENVIRONMENT.json`, as the go's § 1 has it. Read back (`../freeze/verify_frozen.py`, its output beside it): the go's link; the terms' SHA-256, the solver commit `97a8c08` and the manifest's SHA-256, each as the go names it; `freeze_numbers` equal to the instrument's; no other field; the driver's `validate_frozen` passes in a fresh process, and the environment check reads no difference. Nothing has run: there is no `run/out/`, and no solve.

**Next, each on Blake's word:** the freeze block, with `FROZEN.json` in full and the check's output, in a pull request Blake opens; the prelaunch checks, on mains power with sleep off and no macOS update before or during the run, since a launch refuses an environment that differs from this record; then the launch.

## 12. 2026-11-09T20:28:39Z: the freeze block reviewed; the run's copy back at the go's bytes; the block, v2

**The reviews of the freeze block, v1,** relayed by Blake: both give their go on the pull request, one with a custody point before the launch and the other with three NITs. Taken:
- **the copy the run uses, back at the go's bytes** (the first review). Since the check, `DEVLOG.md` had changed by entry 11, so the copy no longer held every byte the go names, though nothing the run reads had changed. `DEVLOG.md` is back at its blob at `94a679ac`, and the entries from 11 on stay beside the folder, in `../DEVLOG_after_freeze.md`, byte for byte, until the run's record is published, when they come back to this file in order. Beyond the review's ask, the tests' scratch, which no line of `SHA256SUMS` lists, is beside the folder too, in `../bench_scratch_aside/`, with its relative paths: 393 files, and the 4 empty `.staging` folders under `dev/runs/`. The copy now holds the commit's tree and the freeze's three files, nothing else. The first pass of the script stopped after four moves, its list of `.staging` folders taken before any move holding those inside the scratch already moved; `reconcile_copy_2.py` finished it and read the copy back. Both outputs are kept in `../freeze/`. No pinned file was touched;
- **the check again,** at 2026-11-09T20:24:49Z: 183 of 183 OK, exit 0, the same lines as the first. `validate_frozen` passes in a fresh process, and the environment check reads no difference (`../freeze/verify_frozen_2.out`). `FROZEN.json` is unchanged;
- **in the block** (the other review): the check before the freeze and again after it, with what the copy holds beside the listed files, the three the freeze wrote, which the run reads; and how each manifest row stands: the solver's 17 `.py` files against their rows, `out/freeze_numbers.json` by content against `FROZEN.json`'s `freeze_numbers`, and the other 6, read only by `m815_freeze.py`, which nothing in the run imports;
- **in the pull request's body** (the other review): the builder by name and SHA-256, published with the record in MIT's M8.19 folder; and the check "before the freeze and again after it", so that the body does not offer the first check as a current pass (the first review's point).

**Kept, as both reviews have it:** the order section; the sealing in its own words; the launch once the pull request is open and its DCO check passes, without waiting for the merge, as the go's § 2 and M8.18's run have it; the builder outside the pinned tree; all 24 manifest rows.

**The block, v2:** 1046 lines (`../freeze_block_v2/freeze_block.md`), built by `../freeze/freeze_block.py`, SHA-256 `0af0d171ce176effccdf8756edacb860e61dc8f793c150f8d01014e06e45f3a5`. Its check, 73 checks with `--live`, passes, and its 25 mutation arms and the control each read as named.

**Next, on Blake's word:** the branch from OpenWave's `upstream/main`, one commit adding `research/m8_19/freeze_block.md`, pushed to the fork and read back; Blake opens the pull request. Then the prelaunch checks, on mains power with sleep off and no macOS update, the copy checked once more against `SHA256SUMS` and for no other file; then the launch.

## 13. 2026-11-09T20:32:44Z: the freeze block's branch, pushed to the fork

Blake, on v2: "If you're good I'm good", so v2 goes to the pull request without another review round: both reviews of v1 gave their go, and v2 takes their points.

**The branch,** `m8-19-freeze-block-2026-11-09`, on OpenWave's `upstream/main` `015640cb`, adds one file, `openwave/xperiments/m8_mit/research/m8_19/freeze_block.md`: `../freeze_block_v2/freeze_block.md`, byte for byte, SHA-256 `c5fc339af85500e6cf25f2acc94e29cf40f2f1ecda1e877200354b12427d3a01`. The commit, `b0a8173a68cc3c99c661703b4adec4a1ee4de53a`, is Blake's DCO identity, with the message `../freeze_block_v2/commit_msg_v2.txt` byte for byte, its sign-off and co-author lines included.

**Pushed to the fork,** and read back through GitHub's API: the branch's head is the commit; the file equals the block; against OpenWave's `main` the branch is one commit ahead and none behind, with one file added. The body, `../freeze_block_v2/pr_body_v2.md`, is on Blake's clipboard, the title `M8.19: the freeze block`. The builder the body names by its SHA-256, `../freeze/freeze_block.py`, stays as it is.

**Next:** Blake opens the pull request. Once it is open and its DCO check passes, on Blake's word: the prelaunch checks, the copy checked once more against `SHA256SUMS` and for no file beyond the commit's tree and the freeze's three, on mains power with sleep off and no macOS update; then the launch.

## 14. 2026-11-09T20:38:41Z: the freeze block's pull request, #702

Blake opened [#702](https://github.com/openwave-labs/openwave/pull/702) at 2026-11-09T20:36:41Z. Read back through GitHub's API (`../freeze_block_v2/posted/`): the title as drafted; the body as drafted but for its closing reviewer line, which the posted body does not hold, every other line equal; the head `b0a8173a68cc3c99c661703b4adec4a1ee4de53a`, one commit, one file, the block byte for byte; DCO passes, at 2026-11-09T20:36:45Z. The pull request is open and not merged, so the terms' "after the maintainer's go and the freeze block's pull request" is met, as the go's § 2 and M8.18's run read it.

**Next, on Blake's word:** the prelaunch checks, the copy against `SHA256SUMS` and for no file beyond the commit's tree and the freeze's three, `validate_frozen` and the environment check, on mains power with sleep off and no macOS update; then the launch.

## 15. 2026-11-09T20:44:41Z: the checks before the launch

**On #702's body:** Blake dropped its closing reviewer line on purpose, since the pull request touches no prose: "that placeholder is for a PR that touches prose".

**The checks before the launch,** on Blake's word, read-only (`../freeze/preflight_checks.py`, its output beside it), 23 of 23:
- the copy the run uses: `shasum -a 256 -c SHA256SUMS`, 183 of 183 OK; its files the commit's tree and the freeze's three, nothing else; no `run/out/`, empty folder, cache or `.DS_Store`; `validate_frozen` passes in a fresh process, with the go's link; `record_environment.py --check` reads no difference; `FROZEN_PIN` holds `FROZEN.json`'s SHA-256;
- the instrument: the link resolves to the worktree's instrument; the worktree's instrument, `m8_15_math` and M8.19 folder equal the folder commit's, with nothing changed or untracked; no cache;
- OpenWave: the go live equals its kept copy, unedited; nothing posted on #698 or #702 since the go by anyone else; #702 open, its head the freeze block's commit, its DCO check passed;
- the machine: on mains power, Low Power Mode off; the lid closed with an external display, which keeps the Mac awake on mains; no macOS update set to download or install by itself, and no scheduled restart, shutdown or sleep; macOS the environment record's; 294 GB free; no other process above half a core.

Caffeine was off when read; the orchestrator holds the machine awake for its own life with `caffeinate -i -s -w`. An idle local server of another project, a Python process at no CPU, was running and was left alone.

**Next, on Blake's word:** the launch from this folder, `python3 -I -B -u run/m819_run.py`, as a task in the app's background-tasks sidebar.

## 16. 2026-11-09T20:50:51Z: the launch refused at its environment check; nothing ran

**The launch,** on Blake's word: `python3 -I -B -u run/m819_run.py` from this folder, as a task in the app's sidebar, ending at Z. It refused before its first job. `validate_frozen` passed, and `record_environment.py --check` read the four threading variables as `1`, where `run/ENVIRONMENT.json` has them unset, every other field equal. The output is kept in `../freeze/launch_1_refused.out`. The refusal came before `launch()`, so there is no `run/out/`, run log, job start or `caffeinate`, and no job's start is counted. The copy still matches `SHA256SUMS`, and `validate_frozen` passes.

**The cause, in the frozen code:** the registered path of `m819_run.py`'s `main()` imports `m819_branch` to run `validate_frozen`, and that import sets the four threading variables to `1`, in `m819_branch.py`'s first lines, so that every job runs on one thread. The environment check then runs as a subprocess and inherits them. `run/ENVIRONMENT.json` was written by `record_environment.py` from the shell, before any such import. The two readings can never agree, so every registered launch of the frozen code against this record refuses.

**Why the tests before the freeze missed it:** `dev/test_freeze.py` ran the registered orchestrator only before `FROZEN.json` existed, where it refuses at `validate_frozen`, ahead of the environment check; the launch, scope and failure-path tests ran the bench path or a stub driver. The registered path past `validate_frozen` first ran at this launch.

**Rehearsed in scratch copies only** (`../freeze/rehearse_env.py`, its output beside it): with the environment recorded from the shell, the launch's check reads the four differences, as here; recorded by the launch's own route, `m819_branch` imported first and `record_environment.py` run beneath it, the check reads no difference. That record differs from this one in the four threading fields and the time alone.

**The remedies,** for Blake, then the maintainer: (A) keep the freeze's three files aside, record the environment by the launch's route, write `FROZEN.json` again with the go's link, and file the new block on #702, with no pinned file changed; or (B) change `m819_run.py` so that its check reads the environment as recorded, which changes a pinned file and needs a new go. Either departs from the go's "writes ... once".

**Next:** Blake's choice, and the maintainer's ruling on it, before anything is rewritten or launched.

**Correction to this entry:** the launch ended at 2026-11-09T20:46:43Z, the time of its output's last write; the time above was lost to a shell error in the script that wrote the entry.

## 17. 2026-11-09T21:49:11Z: #702 merged; the ask on the refusal drafted

**#702** was approved by xrodz at 2026-11-09T21:16:10Z, "approve and merge, no findings, no maintainer edits", and merged at 2026-11-09T21:16:14Z as `734eb28f`, after the refused launch and without word of it. The merged block equals the pull request's head, byte for byte. The approval restates the first freeze's pins and reads the run's log, at the adjudication, against `FROZEN.json`'s written time and #702's opening.

**The reviews of the refusal:** one review, HOLD on the launch and remedy A with the maintainer's express authorization only, its three points asked together: the first freeze kept, one more writing of the freeze with no pinned file changed, and the form of its record, a successor to #702, which is merged; and which link `FROZEN.json` carries as its go. The text relayed as the other review was this session's own report, so that review is not yet in.

**The ask,** v1, drafted for both reviews (`../launch_refusal_ask_v1/`), for #698, where the go was given. Nothing in the freeze is moved or rewritten before the maintainer's ruling.

## 18. 2026-11-10T00:19:36Z: the reviews of the ask; the launch rehearsed past both checks; the ask, v2

**The reviews of the ask, v1:** both GO on conditions. The first: ruling 2's heading, "with no pinned file changed", is imprecise, `run/ENVIRONMENT.json` being one of `FROZEN.json`'s 16 pins; v2 reads "with every pinned input but the environment record unchanged". The same words stand in entries 16 and 17 of this record, where "no pinned file changed" means no file that `SHA256SUMS` lists. Its caution, to replay the two checks on the bench without the production launcher once the second freeze is written, is ruling 2's last clause as it stands. The second: (1) the refusal came 29 minutes before #702's approval and merge and was not reported on #702 first, now said in the ask's opening; (2) the registered path past both checks had never run with the real driver and a real `FROZEN.json`, so it was rehearsed before posting, below; (3) a one-line pointer on #702 to the ask, once it is posted. Its earlier review of the refusal, with four items, was not the text relayed to this session, which entry 17 records as that review not yet in: the full-path rehearsal, the old-against-new differences, the recording procedure's hash and the link choice. The second and third go into the second block.

**The launch rehearsed past both checks,** in a scratch copy only (`../freeze/rehearse_launch.py`, its output beside it, every check passed), launched at 2026-11-10T00:09:14Z: with the environment recorded by the launch's route and a rehearsal go, `python3 -I -B -u run/m819_run.py` passed both checks, entered `launch()` and started its first four jobs, `dyn_C1`, `dyn_C2a`, `dyn_C2b` and `dyn_C3`, M8.15's dynamics controls; no target can start before the controls job has completed with gate 1 passed. After 30 s, SIGTERM ended the launch as an interrupted launch ends: each start's end logged, nothing completed, no stop, and no process or `caffeinate` left. This folder's `run/` was unchanged, with no `run/out/`, and the instrument unwritten. At this entry the copy matches `SHA256SUMS`, 183 of 183, and `validate_frozen` passes with its 16 pins.

**The ask, v2** (`../launch_refusal_ask_v2/`): v1 with those three changes. Its 38 checks, 7 of them live, and its 32 mutation arms and the control pass, and pass again from the unpacked zip. The pointer's builder, `pointer_702/build_pointer.py`, refuses until the ask is on #698. Nothing is posted, and nothing in the freeze is moved or rewritten before the maintainer's ruling.

**Next, on Blake's word:** the ask on #698, then the pointer on #702.

## 19. 2026-11-10T00:30:24Z: the reviews of the ask's v2; the ask on #698 and the pointer on #702

**The reviews of v2:** both GO, with no further change. The first: no more redlines, and until the maintainer rules, no file of the first freeze moved or rewritten, no second freeze prepared as the record, and no launch. Its later detail, for the record's publication: the scripts in `../freeze/` name this bench's home folder, so they are published as marked archival copies with the bench's path configurable, the originals and their outputs kept byte for byte. The second: GO, with an optional clause on the jobs' CPU time, not taken: it is an inference the rehearsal did not check, and the claim that each job runs on one thread rests on the driver's lines the ask links.

**Posted, on Blake's word** ("Yes, post both"), by `gh` from the files, after a live check that nothing was new on #698 or #702: the ask, `../launch_refusal_ask_v2/ask_v2.md`, on #698 at 2026-11-10T00:29:22Z (https://github.com/openwave-labs/openwave/pull/698#issuecomment-6755323610); then the pointer, built by `pointer_702/build_pointer.py` from the posted ask, on #702 at 2026-11-10T00:29:35Z (https://github.com/openwave-labs/openwave/pull/702#issuecomment-6755327374). Read back: both unedited, each body equal to its file, and they are the only comments on #698 since the go and on #702. The responses and the read-backs are in `../launch_refusal_ask_v2/posted/`.

**Next:** the maintainer's ruling. Until it, nothing in the freeze is moved or rewritten, and nothing launches.

## 20. 2026-11-10T00:53:14Z: the maintainer's ruling; the second writing prepared and rehearsed

**The ruling,** [`issuecomment-6755529199`](https://github.com/openwave-labs/openwave/pull/698#issuecomment-6755529199), at 2026-11-10T00:41:59Z, unedited, by xrodz, an OpenWave member. The diagnosis holds: the order carried over from M8.18, whose launch chain ran the check from the shell before any import, did not show it, and the review of #702 read both facts without tracing them through `main()`. All three requests are granted. (1) The first freeze is kept, every byte, beside the folder, and published with the record together with the refused launch's output; #702 stays as merged, the record of that freeze. (2) The freeze is written once more, a one-time exception to § 2 of the go, in this order: the three files moved out of `run/`; the folder checked against `SHA256SUMS`; `run/ENVIRONMENT.json` recorded by the launch's route, the run's interpreter with `-I -B` from a process that has imported the driver, differing from the first in the four threading fields and the time alone; `write_guard.py` once more, the same 15 pins and the new record, with the terms, the manifest, the solver commit and the frozen numbers unchanged; `main()`'s two calls replayed without `launch()`; the second block in its pull request; then the run. No other byte changes, and if a check refuses again, nothing is rewritten and it is reported on #698. (3) The second block shows the exact command that recorded the environment, the two records side by side, the two `FROZEN.json`, differing in the environment pin, `written` and `go` alone, the replayed calls' output, and where the first freeze is kept; the scratch rehearsals' scripts and output go with the record and are read for nothing. (4) `FROZEN.json`'s `go` is the ruling's own link, not the go's, so that `FROZEN.json` shows the second writing ruled before it was made. (5) The refused launch counts toward no job's three launches. (6) The adjudication reads the run's log against the second freeze's written time and the opening of the second block's pull request, and applies the terms, the four readings, the go and the ruling. Kept as `../launch_refusal_ask_v2/ruling/ruling.json`.

**The second writing, prepared.** The checks before it, read-only (`../freeze2/checks_before_write_2.py`, its output beside it), 25 of 25: the ruling and the go live, equal to their kept copies and unedited, nothing posted on #698 or #702 since the ruling; the terms on OpenWave's main, by API and from the clone's fetched `upstream/main`, and in this folder; no commit on MIT's `origin/main` since `94a679ac` touches this folder or the instrument; the instrument at its manifest and blobs, with no cache; the first freeze in `run/` at the pins #702 and the ruling name, `validate_frozen` passing on it; `SHA256SUMS` 183 of 183; the copy the commit's tree and the first freeze's three files, nothing from a rehearsal under `run/` or `reference/`; macOS the first record's; and, in a scratch copy only, the environment recorded by the launch's route differing from the first in the four threading fields and the time alone. The steps, in the ruling's order, are `../freeze2/freeze_2.py`, which stops at the first failure and then rewrites nothing; rehearsed whole on a scratch copy of this folder with the ruling's link (`../freeze2/freeze_2_rehearsal.out`), every step passed, and this folder was not touched. The first freeze's three files are to be kept in `../freeze/first_freeze/run/`, beside the refused launch's output.

**Next, on Blake's word:** `freeze_2.py` on this folder; then the second block, for a pull request Blake opens; the checks before the launch; the launch.

## 21. 2026-11-10T00:56:31Z: the freeze written once more, in the ruling's order

**On Blake's word** ("Go, on the bench"), after a live check that nothing had been posted on #698 or #702 since the ruling and that it was unedited: `python3 -I -B -u freeze_2.py ../soft-slot-dynamics-m8-19 ../freeze/first_freeze out`, from `../freeze2/`, its output in `../freeze2/freeze_2.out` and each step's in `../freeze2/out/`. Every step passed:

- (a) the first freeze's three files moved out of `run/` to `../freeze/first_freeze/run/`, each byte and time unchanged: `ENVIRONMENT.json` at `43b7d084a46860ca1700030445569780d87edf5484b1801932b08903cdad3c3f`, `FROZEN.json` at `1e5107d0c6117a7d45c378827b8ee6670c1ce8964b1099992be05e4769486393`, `FROZEN_PIN` at `ea3320b424d620fb7b56c7da10808b7696b66f6e7265f7e6d4d8b034c8df7517`;
- (b) `shasum -a 256 -c SHA256SUMS`: 183 of 183 OK, exit 0, `SHA256SUMS` at the go's SHA-256, and the folder's files the tree at `94a679ac`, nothing else;
- (c) `run/ENVIRONMENT.json` recorded by the launch's route, the run's interpreter with `-I -B` from a process that had imported the driver, at 2026-11-10T00:55:03Z, 1949 bytes, SHA-256 `9416dd934575ab88b778b8cbd0a72b02a0109fe6a07f2f193e75f50bb516a43e`: it differs from the first in the four threading fields, now `1`, and the time alone, the interpreter's path and flags included;
- (d) `write_guard.py` with the ruling's link, the terms read against the clone's `upstream/main` as at the first writing: `run/FROZEN.json` written at 2026-11-10T00:55:03Z, 9431 bytes, SHA-256 `88940b293d440dd004377d1ba1ad948d945a38cf99e375e4640b1449fe9f445c`, and `run/FROZEN_PIN`; 16 pins, differing from the first `FROZEN.json` in the environment record's pin, `written` and `go` alone;
- (e) `main()`'s two calls replayed without `launch()`: `validate_frozen` passes, with the ruling's link, and `record_environment.py --check`, as its subprocess, reads no difference.

**Read back** (`../freeze2/verify_frozen_2.py`, its output beside it), 18 of 18: every field of the second `FROZEN.json` against the go, the ruling, `SHA256SUMS` and the instrument; the first freeze as kept, at the pins #702 and the ruling name; the folder the commit's tree and the second freeze's three files, with no `run/out/` or cache; the worktree's folder and instrument unchanged; the launch's two checks passing in a fresh process. From the shell, with the threading variables unset, the environment check now reads the four differences, as the launch's route never does; so the checks before this launch run it by the launch's route.

**Next, each on Blake's word:** the second block, `research/m8_19/freeze_block_2.md`, as the ruling's item 3 sets it, for a pull request Blake opens; the checks before the launch; then the launch.

## 22. 2026-11-10T01:43:33Z: the second freeze block, drafted for review

**On Blake's word** ("Yes, draft it"): `research/m8_19/freeze_block_2.md`, 1221 lines, SHA-256 `f3cddba1417dd8d263aa409861fab0bc6ce1f84dea94763e76875b7d2a33cf55`, built by `../freeze2/freeze_block_2.py`, SHA-256 `4c037aa44ebd77d1d89c3f9d61c30badf4a3aa4336d93f92861cb93c3870629f`, outside the pinned tree, on the first block's form; the first block's builder, `../freeze/freeze_block.py`, is unchanged. It carries each item of the ruling's item 3: the exact command that recorded the environment; the two records side by side, and both in full; the two `FROZEN.json` side by side and line by line, and the second in full, the first in full being in #702's block, which it links; the replayed calls' command and output; and where the first freeze is kept. The pull request's title, body and commit message are built by `../freeze2/pr_text_2.py` from the packet's sources; the body carries no reviewer line, as #702's did not.

**Checked:** `check_block_2.py`, 47 checks, 4 of them live, each claim against the packet's sources; `mutations_block_2.py`, 38 arms and the control, each arm red for its named check; both pass again from the unpacked zip. The packet, `../freeze_block_2_v1/freeze_block_2_review_v1.zip`, SHA-256 `a2b804b5cd5029f60293819944da26619b5fa76975e19e3e44d5a148083efdc0`, goes to both reviews.

**Next, each on Blake's word:** the reviews; the branch from OpenWave's `upstream/main`, one commit, pushed to the fork; the pull request, which Blake opens; the checks before the launch, the environment check run by the launch's route; then the launch, once the pull request is open and its DCO check passes.

## 23. 2026-11-10T01:57:29Z: the reviews of the second block's v1; its v2

**The reviews of v1:** the first GO, with no change and its four choices kept; it adds a condition for the record's publication, that each archival copy name its original's digest and give its own, the path-only change marked, and no copy be said to have its original's SHA-256. The second GO after two fixes: the block's line on the published scripts promised copies at hashes they will not have, and the body credited the ruling with launching on the open pull request once its DCO check passes, which is #702's practice, not the ruling's words. Two optional points: pin the links to the first block, and show `write_guard.py`'s command with the clone's path as a placeholder.

**v2** (`../freeze_block_2_v2/`): both fixes and both optional points. The line on the published copies is narrowed to fit the files: the scripts, and the outputs of `freeze_2.py` and of its rehearsal, name the bench's home folder or a scratch path and go out as marked archival copies, the path configurable in a script and a placeholder in an output; the other four outputs name neither and go out as they are. The first block's builder goes out the same way, at `0af0d171…`, the hash #702's body names; the second review gave `142b5155…`, that builder at v1, as the first block's review record has it. The links pin #702's merge commit, `734eb28f`. The block, 1226 lines, SHA-256 `78f04167473b6f315f9d7b20f3cb0ff16e86e8c2c064d35ed125b8ba11162c4a`, is built by `../freeze2/freeze_block_2.py`, SHA-256 `8589c001c2e8caeb833c0af01f09aee0efffb31cb644fed26c4f3e3cd4711faf`, which the body names. Its 51 checks, 5 of them live, and its 47 mutation arms and the control pass, and pass again from the unpacked zip, SHA-256 `18427af0476774fdfb8a7b85f3cc5a9ae9bee6bd43eed6d596db7f023c56d4da`.

**Next, each on Blake's word:** the branch from OpenWave's `upstream/main`, one commit, pushed to the fork and read back; the pull request, which Blake opens; the checks before the launch, the environment check run by the launch's route; then the launch, once the pull request is open and its DCO check passes.

## 24. 2026-11-10T02:03:29Z: the second block's branch, pushed to the fork

**On Blake's word** ("Yes, push it"), after the block's checks passed live again: in the OpenWave clone, the branch `m8-19-freeze-block-2-2026-11-10` from `upstream/main` at `734eb28f`, #702's merge; one commit, `bbb91265`, by Blake Shatto with the noreply address and its DCO sign-off, adding `research/m8_19/freeze_block_2.md`, the v2 block, SHA-256 `78f04167473b6f315f9d7b20f3cb0ff16e86e8c2c064d35ed125b8ba11162c4a`, with `../freeze_block_2_v2/commit_msg.txt` as its message; pushed to the fork, `dmobius3/openwave`.

**Read back from GitHub** (`../freeze_block_2_v2/posted/`): the fork's branch at the commit; its one parent #702's merge; its one file added, equal to the block byte for byte; its message equal to the file; against OpenWave's main, 1 ahead and 0 behind. The pull request's title and body are `pr_title.txt` and `pr_body.md`, the body on Blake's clipboard.

**Next, each on Blake's word:** the pull request, which Blake opens; its read-back and DCO check; the checks before the launch, the environment check run by the launch's route; then the launch.

## 25. 2026-11-10T02:11:15Z: the second block's pull request, #703; the checks before the launch refuse on power

**#703**, opened by Blake at 2026-11-10T02:07:48Z (https://github.com/openwave-labs/openwave/pull/703): from `dmobius3:m8-19-freeze-block-2-2026-11-10` at `bbb91265`, the pushed commit, onto `main` at `734eb28f`; its title and body equal to `pr_title.txt` and `pr_body.md`; it adds the second block alone; its DCO check passed at 2026-11-10T02:07:51Z. Read back as `../freeze_block_2_v2/posted/pr_new.json` and `pr_new_checks.json`.

**The checks before the launch on the second freeze**, read-only (`../freeze2/preflight_checks_2.py`, its output beside it), on the first one's form, with the environment check run by the launch's route: 25 passed and 2 failed. Passed: the copy at the go's bytes and the second freeze's three files, nothing else, with no `run/out/`; `validate_frozen` with the ruling's link and the environment check reading no difference, by the launch's route in a fresh process; the first freeze as kept; the instrument; the go and the ruling unedited, nothing posted since the ruling, #702 merged, #703 open at the pushed commit with its DCO check passed; no macOS update set to install, nothing scheduled but wakes, macOS the record's; disk and load; no M8.19 process running. Failed: on mains power (Now drawing from 'Battery Power', 93%; discharging) and Low Power Mode off (it was on). The lid was open, with the built-in display alone.

**Nothing launched.** Next: mains power, Low Power Mode off, and the lid open or an external display with the lid closed; the checks run again; then the launch, on Blake's word.

## 26. 2026-11-10T03:24:02Z: #703 approved and merged

**#703** was approved by xrodz at 2026-11-10T03:07:09Z, "approve and merge, no findings, no maintainer edits", on the pushed commit `bbb91265`, and merged by xrodz at 2026-11-10T03:07:14Z as `47ce7a48`: its parents #702's merge, `734eb28f`, and the pushed commit; its tree the pushed commit's. The block on OpenWave's `main` equals the pushed block byte for byte, and `main` was at the merge when read. The pull request's body and the review were never edited, and nothing else was posted on #698, #702 or #703 since the ruling.

**The approval** checked the block with the reviewer's own code, reading only git objects from MIT at the folder and solver commits, #702's block and this one's text, and running none of ours; seven changed inputs each turned it red. Among its checks, the second `FROZEN.json`, rebuilt in `write_guard.py`'s layout, equals the block's copy byte for byte. It restates five pins, each equal to ours (the head, the block, the second `FROZEN.json` and `ENVIRONMENT.json`, and `freeze_block_2.py`), and each short hash it gives names one of ours. It leaves to the adjudication the published freeze files and the refused launch's output, against the hashes it gives; the published scripts, marked archival copies, each against its original's SHA-256; the steps, the three files' leaving `run/` and the rehearsals, as the block's statements, consistent with the tree and with each other; and that the run has not started, read from the run's log against the second freeze's written time and #703's opening at 2026-11-10T02:07:48Z.

**Read back and checked** by `../freeze2/merge_703.py`: 19 checks passed, its output beside it; its 6 mutation arms and the control pass (`mutations_merge_703.out`); the read-back in `../freeze_block_2_v2/posted/merged/`.

**The checks before the launch, as written, cannot pass now:** `preflight_checks_2.py` asks for #703 open, and counts the approval as posted since the ruling by someone else. Its first run stands, its output kept. Next: a revision for the merged state beside it, on Blake's word; the checks again on mains power with Low Power Mode off; then the launch, on Blake's word.

## 27. 2026-11-10T03:35:07Z: the checks before the launch, revised for the merge

**`../freeze2/preflight_checks_2_merged.py`**, on Blake's word ("Yes, revise it"), beside `preflight_checks_2.py`, whose first run stands with its output: its OpenWave checks for #703 merged in place of open, the rest unchanged (`preflight_checks_2_to_merged.diff`). Nothing posted since the ruling by anyone else but the approval; the approval as kept and unedited, by the merger, on the pushed commit, before the merge; #703 merged as kept, its head the pushed commit, the merge's parents #702's merge and the head; the block on OpenWave's `main` byte for byte. Each is read against the merge's read-back, `../freeze_block_2_v2/posted/merged/`.

**Rehearsed** once, its output in the session's scratch folder, on battery: 27 passed, and only the machine's two failed, mains power and Low Power Mode.

**Its mutation arms**, 7 and the control (`mutations_preflight_2_merged.py`), run twice: in both runs every arm turned its named checks red, and no check outside the machine's besides, and the control failed only power and Low Power Mode. The strict comparison still marked arms BAD, 1 in the first run and 4 in the second, each for the load check alone, a browser's renderer above half a core while that arm ran (Microsoft Edge Helper (Renderer); Opera Helper (Renderer)). Both outputs stand (`mutations_preflight_2_merged.out`, `mutations_preflight_2_merged_2.out`). The arms run once more with the checks for the record, the browsers quiet.

**Next, each on Blake's word:** mains power, Low Power Mode off, the lid open or an external display, the browsers quiet; the arms and the checks for the record, into new outputs; then the launch.

## 28. 2026-11-10T03:44:02Z: the arms clean; the checks for the record refuse on load alone

**On Blake's word** ("Set, run them"), the browsers quiet: the arms of `../freeze2/mutations_preflight_2_merged.py` a third time, 7 arms and the control passing, the control failing nothing (`mutations_preflight_2_merged_3.out`). Then **the checks before the launch for the record** (`preflight_checks_2_merged.py`, its output `preflight_checks_2_merged.out`): 28 passed and 1 failed. Passed: all that the rehearsal passed, and now mains power (Now drawing from 'AC Power'), Low Power Mode off, and the lid closed on an external display (LG IPS FULLHD). Failed: no other process above half a core, with Spotlight's indexer, `mds_stores`, at 84%; it stayed busy when sampled after.

**Nothing launched.** The run's code, the instrument's and `m8_15_math` use the clock only to record durations: a search for a time limit, deadline, budget or alarm found none, so load can lengthen the run and its recorded seconds but not change its numbers. Next, on Blake's word: the checks again into a new output once the indexer is quiet, or the launch with this refusal on record.

## 29. 2026-11-10T03:51:04Z: the checks before the launch pass

**On Blake's word** ("Wait, then rerun"): a watch on the load from 2026-11-10T03:46:26Z, reading it as the checks do, every five seconds, until no other process had used more than half a core for two minutes. It got there at 2026-11-10T03:50:03Z, after 217 s, quiet for 121 s; Spotlight's indexer was already quiet when it began, and above half a core while it waited were `AMPLibraryAgent` at 86%; `WindowServer` at 51%. Then, chained to it, **the checks before the launch** (`preflight_checks_2_merged.py`, into `preflight_checks_2_merged_run2.out`): all 29 passed. The copy at the go's bytes, with the second freeze's three files and no `run/out/`; `validate_frozen` with the ruling's link, and the environment check reading no difference, by the launch's route; the first freeze kept; the instrument; OpenWave as merged, the approval as kept and unedited, the block on `main` byte for byte; mains power, Low Power Mode off, the lid closed on an external display (LG IPS FULLHD); no macOS update set to install, nothing scheduled but wakes, macOS the record's; disk; no other process above half a core (the busiest: 7% WindowServer; 6% tccd; 5% syspolicyd; 3% Claude Helper; 3% Claude Helper (Renderer)); no M8.19 process running. The watch's output is in the session's scratch folder; the earlier runs' outputs stand.

**Next:** the launch, on Blake's word: `python3 -I -B -u run/m819_run.py` from the bench copy, as a task in the app's sidebar, its console into `../freeze2/launch_2.out`.

## 30. 2026-11-10T03:54:38Z: the launch

**On Blake's word** ("send it"), at 2026-11-10T03:53:24Z: `python3 -I -B -u run/m819_run.py` from the bench copy, as a task in the app's sidebar, its console into `../freeze2/launch_2.out`. Checked just before it: mains power, Low Power Mode off, the lid closed on the LG display, no `run/out/`, `python3` on the path the environment record's interpreter, and no M8.19 process. `main()`'s two checks passed: `validate_frozen`, and the environment check, which read the record and the live environment with no difference, the threading at `1` in both. The run log, `run/out/RUNLOG.json`, opened at the second freeze's pin, `88940b29`, not on the bench, its launch numbered 1; `caffeinate -i -s -w` holds the machine awake on the orchestrator's pid; the first wave's first 4 jobs started at 2026-11-10T03:53:24Z: `dyn_C1`, `dyn_C2a`, `dyn_C2b`, `dyn_C3`, each its first start, each alive under the orchestrator when this entry was written.

**The order, for the adjudication:** the ruling at 2026-11-10T00:41:59Z; the second freeze written at 2026-11-10T00:55:03Z; #703 opened at 2026-11-10T02:07:48Z and merged at 2026-11-10T03:07:14Z; the launch at 2026-11-10T03:53:24Z. The refused launch (entry 16) counts toward no job's starts, as ruled.

**Next:** the run, to its end; its record; the adjudication.

## 31. 2026-11-10T14:48:45Z: the run ends

**The launch ended** at 2026-11-10T14:42:59Z, 10 h 49 min after it began, the console's last line `launch ended; pending []; stop None` and the task's exit 0. All 17 jobs completed, each on its first start; none ended its part of the run, none was not run, and nothing stopped it. The staging folder is empty, there is no `interrupted/`, and no M8.19 process or `caffeinate` is left. Every completed job's files, 64 in all, match the run log's SHA-256, and no folder in `run/out/` stands outside the log.

**Gate 1 passed,** every control as stated: C1, C2a and C2b Persist and C3 Fails at `t = 583.28`, with C3's rate run fitting 0.009741 against a linear 0.009737, M8.15's record to its digits; `P5a`'s seed solve stops under the repaired test below 10⁻¹¹; C3 at 3 Fails; C2a/R4 at 1 Persists, valid, at `T` = 2750.

**The gates** were read at all 61 points of the five rows, and gate 2 passed at every one: an accepted Newton solution at levels 3 and 2 on the continuation path, at T4's 19 points as at the others. **The plan** set one test, needed no longer control, and left 5 stretches Untested (T1/R4, lower; T1/R4, upper; T1/R5; T4/R4; T4/R5), each point's first failed gate 3, the cluster and the mode. The level-3 cluster check failed at every one of their 46 points. At T1's 27 the level-2 check failed too, and no genuine imaginary mode of Krein sign − was found at either level. At T4's 19 the level-2 check failed at 15, and at 6 the level-2 mode was not identified: two candidates of Krein sign − of the same recorded modulus, where the reference's multiplicity is 1 (2 points have both). As the terms expected, T1's three stretches are untested at the cluster check; for T4 they expected nothing.

**The coherent row in `R5`:** its ladder is established, 15 points from 0.25 to 32, every one Elliptic, with no change of type, the validity check at 0.25 passing and the types on the stretch on record M8.16.1's; it has no other Elliptic run, so nothing is newly identified. At 0.25 gate 3 failed, the level-2 mode not identified (two candidates of Krein sign + of the same recorded modulus); at 0.3536 gate 4 failed; from 0.5 to 32 every gate passed, and the test went to the top.

**The test** (`test_C2a_R5_1`) **Persists, valid,** at ε = 32 with `T` = 1000, 3.33 periods of `P` = 300.3: max d_⊥ 9.96×10⁻⁴, max d_rot 1.68×10⁻⁶, the reference floor 1.68×10⁻¹³. Its evolution took 6,148 s, at a peak of 1.28 GB. The second energy rule, recorded and not scored, is false on the test and on every control valid under the frozen rule, and true only on C3's rate run, which the frozen rule reads as invalid: as the terms disclose.

**Next, on Blake's word:** the record, filed for adjudication, as the terms' definition of done asks; on adjudication, the census page's dated note on where S5 stands.

## 32. 2026-11-10T16:09:19Z: the record, drafted, v1

**On Blake's word** ("k, let's draft the record"), in M8.18's form, on the bench in `../record_v1/`; nothing committed, pushed or posted. **The environment, read again after the run** by the launch's route (`postrun/postrun_env.py`, which replays `freeze_2.py`'s step (e) in the same words), at 2026-11-10T15:36:59Z: `validate_frozen` passed with the ruling as its go, and the check read no difference.

**The tree** (`build_tree.py`): MIT's M8.19 folder as the record's commit would leave it, 314 files. The run's folder byte for byte, its `run/out/` included; the freeze's files from `../freeze/` and `../freeze2/`, 35 as they are and 22 as marked archival copies where a file names a local path, each copy giving its original back byte for byte once its paths are put back (`ARCHIVAL.json`); left out, the DEVLOG writers, the packet cover and the pull requests' text builders; `DEVLOG.md` with entries 11 to 31 after entry 10, byte for byte; `SHA256SUMS` fresh. **`RECORD.md`** (391 lines), built by `tools/build_record.py`, every refusal holding: each logged output at its SHA-256; `validate_frozen`; the two freezes and the two records differing only as ruled; the gates at all 61 points recomputed from their stored inputs with the frozen gates, with the search and the plan; all 8 dynamics series' verdicts recomputed with the frozen evaluator; `RECORD.json` against the folders; and each fact taken from `DEVLOG.md`.

**Found while drafting.** Two of the run's console logs, T4's gates jobs', hold a `ComplexWarning` that names the bench's path to the instrument's `linearize.py`: the trace of the fast-spectrum search, the defect M8.15.x's record keeps unrepaired, which ran at the 8 level-2 points of T4 whose Krein count does not balance; no gate reads its output, since `level_data` gives the gates the cluster check, `tau_re` and the genuine modes alone. Those 2 logs go out as archival copies, their originals at the run log's SHA-256. The second writing's `write_guard.out` names the OpenWave clone's path, which the second block's "the other outputs go out as they are" missed: it goes out as an archival copy too, a correction the record's § 9 states. Control 1a's record names its arm `bench`, the arm's name in M8.15.x's qualification.

**The filing texts** (`openwave/`): the method note for OpenWave (35 code links at the pinned commits), the pull request's title and body, the roadmap with the M8.19 row's gate moved to the adjudication (OpenWave `main` at `ec51a0b8`), and MIT's commit message; their links to the record's commit wait for it. OpenWave's `check_roadmaps.py`, `check_models_md.py` and `check_no_local.py` are clean on the note and the roadmap, in a scratch export of `main`. **The checks:** `checks/check_record_v1.py`, 28 checks, PASS; its 11 arms and the control, PASS. **The packet** for review, `record_review_v1.zip`, SHA-256 `90623dc0132cb5ea…`, `reference/` left out as MIT's at `94a679ac`; its cover, `record_packet_v1.md`, on the clipboard, with 7 choices, the first, how the two console logs go out, Blake's.

**Next:** the reviews; Blake's choice on the two console logs; the tree rebuilt for the commit, with this entry; then MIT's commit, on Blake's word.

## 33. 2026-11-10T16:34:29Z: the reviews of the record's v1; its v2

**The reviews,** relayed by Blake. Both give GO after their fixes, and neither asks for a change to the frozen driver, the run's outputs, a gate, an outcome or either freeze. The first: three wording corrections, the record's § 1.6 and § 1.7 to separate the outputs published byte for byte from the two path-redacted console logs, and the method note's definitions of d_⊥ and d_rot and its claims on what is published and checked; choices A to G kept. The second: it reproduced the record on another machine apart from the rate's fit, in its last digits, and asked that the builder compare the fit within a tolerance and that § 1.1 say the launch came after #703's merge, though #703's body allowed it once open; on choice A it leans toward the logs as they are, and accepts the copies. Their fates, 5 findings adopted, in `../record_v1/reviews_v1_adjudication.md`; the definitions verified in the frozen code, `G` being the verdict's tracked cluster `G_tol`, and #703's sentence in its body as posted.

**v2,** rebuilt from the builders as changed: the tree in `../record_v1/tree_6/`, `RECORD.md` changed in 5 places (`RECORD_v1_to_v2.diff`, the post-run files' hashes and this log's last entry among them), the method note in 4 (`openwave/note_v1_to_v2.diff`), the pull request's texts and the commit message unchanged. `checks/check_record_v1.py` on v2, 28 checks, PASS; its 11 arms and the control, PASS.

**Next:** Blake's choice on the two console logs; then the tree rebuilt with this log's entries for the commit, and MIT's commit, on Blake's word.

## 34. 2026-11-10T16:47:36Z: choice A, the two console logs as archival copies

**Blake's choice** ("Archival copies"): `run/out/gates_T4_R4/console.log` and `run/out/gates_T4_R5/console.log` go out as marked archival copies, their originals at the SHA-256 the run's log records, as v2 has them; v2's wording on the two kinds of hash stands. No content changes. Next: the tree rebuilt with this log's entries, the checks run again, and MIT's commit, prepared and rehearsed for Blake's word.
