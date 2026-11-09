# M8.19's driver: design (bench, v2)

The driver M8.19's terms ask for (`registration/m8_19_task_details.md`, merged on OpenWave #698), and the dry run before the freeze. Bench note: it changes as the build does, and nothing here is filed.

## Layout

The bench mirrors the repository, so every relative path is the one the run will use.

```
census_close/m8_19/
  soft-slot-dynamics-m8-15x/      the frozen instrument (on the bench, a link to the worktree's folder)
  soft-slot-dynamics-m8-19/
    DEVLOG.md, DESIGN.md
    reference/   the records the driver reads, copied byte for byte, with SOURCES.json (commit, path, blob, SHA-256)
    run/         m819_branch.py, m819_gates.py, m819_run.py, the terms, out/
    dev/         the dry run's scripts and outputs
```

`run/m819_branch.py` is M8.15.x's `m815_branch.py` copied, with the changes the terms list; its diff against the frozen file is part of the freeze. `Point`, `cross_level`, `bisect` and `slow_lineage` stay byte for byte, and so does `decide`, inside the coherent row's job. The frozen modules are imported in place from `../../soft-slot-dynamics-m8-15x/m8_15x_solver/`; nothing is written there, and every script runs as `python3 -I -B -u`, so no cache lands in it.

## Jobs

One process per job, `run/m819_branch.py JOB`, each on one thread. A job writes into its own staging folder, and only the orchestrator moves a finished job's folder to `out/<job>/` and logs its files' SHA-256.

| Wave | Job | What it does |
| --- | --- | --- |
| 1 | `dyn_C1`, `dyn_C2a`, `dyn_C2b`, `dyn_C3`, `rate` | M8.15's `dynamics`, with its output folder moved to the job's |
| 1 | `p5a` | control 1a's M8.15.x arm: P5a in `R4` at level 2, the seed solve traced |
| 1 | `c3e3` | C3 at `ε` = 3: `dynamics` on `ladder(0.25, 3.0)`, `T` = 1000 |
| 1 | `c2a_dur` | C2a/R4 at 1, levels 3 and 2, gates 3, 5, 6 and 7, then the test at gate 6's `T` |
| 1 | `controls` | gate 1 on the eight records: `CONTROLS.json` |
| 2 | `gates_T1_R4`, `gates_T1_R5`, `gates_T4_R4`, `gates_T4_R5` | the continuation at levels 3 and 2 to the row's highest classified point, and gates 2 to 7 at every classified point; the level-2 standing wave and spectrum stored at each |
| 2 | `coherent_R5` | C2a in `R5` along `ladder(0.25, 32)`: M8.15's types at level 3, cross-checked at level 2, the ladder's outcome, then the gates on its stretch |
| 2 | `plan` | each stretch's test point and `T`, and the longest `T`: `PLAN.json` |
| 3 | `c2a_long` | `c2a_dur` at the longest `T`, only if a test needs more than 2750 |
| 4 | `test_<stretch>` | the stored state reloaded, its level-2 point rebuilt and checked equal to the stored one bit for bit, gates 3, 5, 6 and 7 read again equal, then the frozen `run_test` at gate 6's `T` |
| 5 | `record` | the record, from the job folders alone |

A test runs in its own job, after every gate is written: the terms want every stretch's gates on record before any target evolves.

## The gates, as the driver reads them

- **Gate 2:** the ladder point reached at both levels, on the path from the seed (`Branch.run`'s accepted point at `ε_k`).
- **Gate 3:** `Point.cluster_ok` at levels 3 and 2; and the mode identified at each level:
  - the candidates are the level's genuine representatives the frozen `classify` puts in `imag+` or `imag−`, with the reference's Krein sign;
  - the mode is the slowest candidate, and the candidates within 5% of its modulus (gate 4's band) are counted;
  - identified when that count is the reference's multiplicity; otherwise not identified, recorded with the count and the candidates' moduli, which says nothing of the modes' own multiplicity.
- **The reference:** the harmonic reading at the point, its slowest `imag` row above 10⁻⁹ (M8.17's for T1 and T4, M8.16.1's for the coherent row at 0.25 to 2, as `tools/periods.py` reads them). Every such row on record has count 1. On the coherent row above 2, level 3's slowest genuine imaginary mode is the reference, and it must be found once there.
- **Gate 4:** `|λ₂ − λ₃| ≤ 0.05 max(|λ₂|, |λ₃|)`; and, with a harmonic reading, `||λ_h| − λ_ref| ≤ 0.05 λ_ref` at each level `h`.
- **Gate 5:** at level 2, `v` drawn exactly as `persistence.direction` draws it, `v_s = (P_S − P_G)v`, and `B` the real span of the identified mode's eigenvectors and their Hamiltonian partners (eigenvalues matching `λ`, `−λ`, `λ̄` or `−λ̄` to the frozen closure tolerance), orthonormal in the phase-space inner product; the share `‖P_B v_s‖²/‖v_s‖²`, in the energy norm `persistence.energy_norm` scales in, at least 0.01. The job checks that `direction()` returns exactly the scaled `v_s` plus the scaled fast half, bit for bit.
- **Gate 6:** `T = max(1000, 250⌈P/250⌉)`, `P = 2π/|λ₂|`.
- **Gate 7:** `r T ≤ ln(1/(10η))`, `r` the largest real part among level 2's lifted or rigid eigenvalues, 0 if none (`persistence.margin_ok`).
- **The search:** the test point is the stretch's highest classified point where gates 2 to 7 all pass; each point's first failed gate is its recorded cause.

## The coherent row in `R5`

- **The case:** C2a's definition with `slot = 5`, which `PinnedCase` takes; `FROZEN_DIM` and `SPECTRA` are C2a's, and `predicted` scales by 9/16 in `R5` as for every row. The one constant added is `QEXACT[('C2a', 5)] = 2289/2288`, `Q5[6]` of `soft-slot-branches/branches_check.py`, as `QEXACT[('C2a', 4)]` is its `Q4[6]` = 1288/1287. Checked at setup against the finite-element seed's `Q` at both levels.
- **Established** when the validity check at 0.25 passes and the types at 0.25, 0.5, 1 and 2 are Elliptic, as M8.16.1's.
- **The stretch:** if established, the run of consecutive Elliptic ladder points that contains 2; otherwise the record's four points.
- **Other Elliptic runs:** any other run of Elliptic points an established ladder reads goes in its outcome with its points, with no gates and no test, and the record names it apart from the terms' stretches, as a newly identified Elliptic stretch with no test fixed: S5 stays open for it, for the maintainer. A ladder not established names none, since its types establish nothing. If the row's job does not complete, the record gives the ladder's outcome as that job's cause, for adjudication.

## The run

- **The orchestrator,** `run/m819_run.py`, frozen with the driver: at most four jobs at once, a job starting as another ends, in the terms' order; a job starts only when every job it depends on has completed.
- **RUNLOG.json,** written by the orchestrator alone, atomically after every event: the manifest pin, each launch, each job's start (with its count) before the process starts, each end (exit status or signal), each completion with its files' SHA-256, and any stop.
- **Three launches:** a launch starts each job at most once, so a job's starts, counted from the log across launches, are the launches that started it. A start that ends without completing leaves the job pending: what does not depend on it carries on, and the launch ends when nothing more can start. Its staging folder is moved to `out/interrupted/`, at once, or by the next launch if the orchestrator itself was stopped; nothing in it is read. After a third launch has started the job and left it unfinished, the job ends its part of the run: what depends on it does not run, and its cause (the crash record, or the exit status) is recorded.
- **A relaunch** is the whole run, through the same launch: `FROZEN.json` validated and the environment read again against `run/ENVIRONMENT.json`. It never starts a chosen job, no pinned file changes between launches, and the run is relaunched until no job is pending. It refuses while any process the log started is still alive.
- **Guards in the driver:** a sealed job (T1, T4, C2a in `R5`) refuses unless `run/FROZEN.json` validates and `controls` completed with every control as stated; a test with `T` > 2750 refuses unless `c2a_long` Persisted, valid, at the longest `T`; test hooks and a shortened `T` refuse on any sealed job, as in `m815_branch.py`.

## The dry run, inside the sealing

Nothing sealed is solved, given a spectrum or evolved, and no state is evolved but the controls' recorded ones.
1. **Control 1a,** the `p5a` job, against `control_1a_rerun.json`'s M8.15.x arm, every field but the two timings.
2. **The stand-in:** C2a/R4 run through the whole target path on a test stretch of 0.25 to 8, with M8.16.1's C2a readings as gate 4's reference at 0.25 to 2. Its test must land at 8 with `T` = 1000, a recorded state; any other point or `T` stops it before evolving. Its records at 0.25 to 8 and its test are compared with M8.15.x's qualification records bit for bit.
3. **M8.15's dynamics gate** run whole, C1, C2a, C2b, C3 and the rate run, against the qualification's records, then gate 1 read on them.
4. **The fresh controls' gates without evolution:** `c3e3` stops where `run_test` would take its first step, after the solve, the cluster, the margin and the perturbation's `E_η` (`pre_evolution`, `run_test`'s own lines up to that step); `c2a_dur` stops after its gates, and its gate 6 must give 2750.
5. **The smoke test:** four jobs at once through the orchestrator at `T` = 20 on the recorded controls, read for nothing: one thread each, separate folders, the order.
6. **Failure paths,** on cheap control jobs: a forced exception over three launches, a killed job relaunched, a killed orchestrator, the third start, the staging folder moved aside, and no launch starting a job twice.
7. **The sealed cases set up without a solve:** `PinnedCase`, `Standing` and the rotations at levels 2 and 3 for T1 and T4 in both slots and C2a in `R5`, the seed's `Q` against `QEXACT`; no Newton step, no eigenvalue.
8. **The gates' mutation arms,** on the stand-in's stored points: each gate red for its named reason.
9. **The guards,** each refusal provoked.
10. **`tools/periods.py`,** rerun against its committed output.

## The readings, as Blake ruled them (DEVLOG, entry 8)

Readings 1, 2, 3 and 5 confirmed, with the reviews' additions; reading 4 struck, with relaunches by hand, as in M8.18. They interpret the filed terms, and they go into the request for the go.

1. **Multiplicity:** gate 3 counts the candidates of the reference's Krein sign within 5% of the slowest (gate 4's band), and the mode is identified when that count is the reference's multiplicity. A count that differs leaves the mode not identified, recorded with the count and the candidates' moduli; that says nothing of the modes' own multiplicity. Every reference row on record has multiplicity 1.
2. **The coherent row above 2:** the reference is level 3's slowest genuine imaginary mode, of either Krein sign, found once there; gate 3 then identifies the mode with that sign at both levels, and gate 4 compares the values.
3. **The coherent row's stretch:** the run of Elliptic points through 2. Any other Elliptic run an established ladder reads is named apart from the terms' stretches, as a newly identified Elliptic stretch with no test fixed: S5 stays open for it, for the maintainer. It is never recorded as Untested.
4. **Relaunches are by hand** (struck: automatic restarts). A launch starts each job at most once, and a relaunch is the whole run, through the frozen check and the environment check, as M8.18's every relaunch was. A job that three launches start and leave unfinished ends its part of the run.
5. **An exception is a crash, never a gate failure:** it ends the job's start, as `m815_branch.py` records it, so a defect in the driver cannot pass for a scientific cause. A job whose part of the run ends sends its stretches to the maintainer's adjudication, never to an ending of S5. An unfinished control leaves gate 1 unpassed, so no target runs, and an unfinished longest control holds back every test longer than 2750.

**Note (2026-11-09), on the readings' words.** The request for the go words readings 3 to 5 more exactly, and its words are the ones the maintainer is asked to confirm. Reading 3's stretch is the unbroken run of Elliptic ladder points that contains 2, as far below and above it as it goes. Reading 4's comparison is M8.18's launch chain, which refuses a changed environment on a first launch and on every relaunch; M8.18's run never relaunched. Reading 5's record writes no ending for the stretches of a job that three launches start and leave unfinished: they go to the maintainer's adjudication on its recorded cause, as the approval's § 1 has it.
