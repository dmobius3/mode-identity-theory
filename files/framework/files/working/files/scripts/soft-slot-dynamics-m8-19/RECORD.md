# M8.19 run record

The record of M8.19's registered run, the census's persistence tests (S5), from 2026-11-10T03:53:24Z to 2026-11-10T14:42:59Z. It ran under the governing terms, `run/m8_19_task_details.md` (SHA-256 `f2295e0b7f1d086a…`), merged in OpenWave [#698](https://github.com/openwave-labs/openwave/pull/698), on this folder as MIT `94a679ac` holds it and M8.15.x's solver at MIT `97a8c08`, its manifest at `2b9864ab185e47f9…`. The maintainer's go is [#698's comment](https://github.com/openwave-labs/openwave/pull/698#issuecomment-6749289423). The freeze is recorded by two blocks on OpenWave: `research/m8_19/freeze_block.md`, merged in [#702](https://github.com/openwave-labs/openwave/pull/702), and, after the [ruling](https://github.com/openwave-labs/openwave/pull/698#issuecomment-6755529199) that the freeze be written once more, `research/m8_19/freeze_block_2.md`, merged in [#703](https://github.com/openwave-labs/openwave/pull/703). Every number below is read from this folder's files, and `tools/build_record.py` builds this record from them: the run's in [`run/out/`](run/out/), the freeze's in `run/`, [`freeze/`](freeze/) and [`freeze2/`](freeze2/), and the facts it takes from `DEVLOG.md`. This record gives what the terms' § DEFINITION OF DONE asks: every stretch's outcome, the coherent row's ladder with its own, and the record, for adjudication. Adjudication is the maintainers'.

**The outcome.** The run completed in one launch, with no stop and no job left unfinished: all 17 jobs completed, each on its first start. **Gate 1 passed:** every control gave its stated verdict. **The coherent row in `R5`:** its ladder is established, Elliptic at all 15 points from 0.25 to 32, and its test, at `ε` = 32 with `T` = 1000, **Persists, valid**. **T1's three stretches and T4's two end Untested:** at every one of their 46 points the first gate that failed is gate 3, the cluster and the mode. No outcome claims orbital stability or instability.

**The stretches:**

| Stretch | Points | Outcome | Test | max d_⊥ | max d_rot | Reference floor |
|---|---|---|---|---|---|---|
| T1/R4, lower | 5, 0.25 to 1 | Untested: gate 3 first at every point | none | | | |
| T1/R4, upper | 8, 2 to 22.63 | Untested: gate 3 first at every point | none | | | |
| T1/R5 | 14, 0.25 to 22.63 | Untested: gate 3 first at every point | none | | | |
| T4/R4 | 8, 0.25 to 2.83 | Untested: gate 3 first at every point | none | | | |
| T4/R5 | 11, 0.25 to 8 | Untested: gate 3 first at every point | none | | | |
| The coherent row in R5 | 15, 0.25 to 32 | Persists, valid | `ε` = 32, `T` = 1000, 3.33 periods of `P` = 300.3 | 9.96×10⁻⁴ | 1.68×10⁻⁶ | 1.68×10⁻¹³ |

## 1. Custody

### 1.1 The order

The ruling's item 6 reads the run's log against the second freeze's written time and #703's opening; #702's approval read it against the go, the first freeze's written time and #702's opening. In order, each time from the file named:

| Event | Time | From |
|---|---|---|
| the go | 2026-11-09T19:25:45Z | DEVLOG.md, entry 11 |
| the folder checked against `SHA256SUMS` at `94a679ac` | 2026-11-09T19:52:58Z | DEVLOG.md, entry 11 |
| the first `run/ENVIRONMENT.json` recorded, from the shell | 2026-11-09T19:53:09Z | `freeze/first_freeze/run/ENVIRONMENT.json` |
| the first `run/FROZEN.json` written | 2026-11-09T19:53:23Z | `freeze/first_freeze/run/FROZEN.json` |
| #702 opened | 2026-11-09T20:36:41Z | DEVLOG.md, entry 14 |
| the launch on the first freeze refused, before its first job | 2026-11-09T20:46:43Z | DEVLOG.md, entry 16 |
| #702 merged | 2026-11-09T21:16:14Z | DEVLOG.md, entry 17 |
| the ruling | 2026-11-10T00:41:59Z | DEVLOG.md, entry 20 |
| the second `run/ENVIRONMENT.json` recorded, by the launch's route | 2026-11-10T00:55:03Z | `run/ENVIRONMENT.json` |
| the second `run/FROZEN.json` written | 2026-11-10T00:55:03Z | `run/FROZEN.json` |
| #703 opened | 2026-11-10T02:07:48Z | DEVLOG.md, entry 25 |
| #703 merged | 2026-11-10T03:07:14Z | DEVLOG.md, entry 26 |
| the launch: the run's log opens | 2026-11-10T03:53:24Z | `run/out/RUNLOG.json` |
| the run's log ends | 2026-11-10T14:42:59Z | `run/out/RUNLOG.json` |
| the environment read again, by the launch's route | 2026-11-10T15:36:59Z | `environment_postrun_2026-11-10.txt` |

The run's log opens after every event above it, 1 h 45 min after #703's opening: no job had started when either block's pull request was opened. It also opens 46 min after #703's merge, though #703's body allowed the launch once the pull request was open and its DCO check passed: the checks before the launch refused on mains power and Low Power Mode while it was open (`DEVLOG.md` entry 25), and passed after the merge (§ 1.4).

### 1.2 The first freeze, kept, and the refused launch

- **The first freeze.** `run/FROZEN.json` was written once, at 2026-11-09T19:53:23Z, by `run/write_guard.py`, after the go and with [its link](https://github.com/openwave-labs/openwave/pull/698#issuecomment-6749289423) as its `go`. It pins 16 files: the 15 under `run/` and `reference/` that `SHA256SUMS` lists at `94a679ac`, and `run/ENVIRONMENT.json`, recorded from the shell at 2026-11-09T19:53:09Z. Its pin is `1e5107d0c6117a7d…`, and #702's block carries it in full. The three files are kept in [`freeze/first_freeze/run/`](freeze/first_freeze/run/), every byte unchanged, as the ruling's item 1 has it:

  | File | SHA-256 |
  |---|---|
  | `freeze/first_freeze/run/ENVIRONMENT.json` | `43b7d084a46860ca1700030445569780d87edf5484b1801932b08903cdad3c3f` |
  | `freeze/first_freeze/run/FROZEN.json` | `1e5107d0c6117a7d45c378827b8ee6670c1ce8964b1099992be05e4769486393` |
  | `freeze/first_freeze/run/FROZEN_PIN` | `ea3320b424d620fb7b56c7da10808b7696b66f6e7265f7e6d4d8b034c8df7517` |

- **The refused launch.** On the first freeze, `python3 -I -B -u run/m819_run.py` refused before its first job, at 2026-11-09T20:46:43Z: `validate_frozen` passed, and the environment check read the four threading variables as `1`, where that record has them unset, every other field equal ("differences: ['threading.MKL_NUM_THREADS', 'threading.OMP_NUM_THREADS', 'threading.OPENBLAS_NUM_THREADS', 'threading.VECLIB_MAXIMUM_THREADS']"). The cause, which the ruling confirms: `main()` imports the driver, which sets the four variables, before it runs the check as a subprocess. It started no job and wrote no log, and counts toward no job's three launches (the ruling's item 5). Its output, [`freeze/launch_1_refused.out`](freeze/launch_1_refused.out), SHA-256 `422529a5a7b3abbb10f789f0a0a59fb1b140b03231862314997d22f7c01f3bf3`, is published as it is.

### 1.3 The second freeze

In the ruling's order, by `freeze2/freeze_2.py`, its output `freeze2/freeze_2.out` and each step's in `freeze2/out/`: the first freeze's three files moved out of `run/` to `freeze/first_freeze/run/`; the folder checked against `SHA256SUMS`; `run/ENVIRONMENT.json` recorded once more, at 2026-11-10T00:55:03Z, by the launch's route, the run's interpreter with `-I -B` from a process that had imported the driver; `run/FROZEN.json` written once more, at 2026-11-10T00:55:03Z, with the ruling's link as its `go`; and `main()`'s two calls replayed without `launch()`, `validate_frozen` passing and the check reading no difference (`freeze2/out/replay_main_checks.out`). The checks before it, read-only, are `freeze2/checks_before_write_2.py` and its output, and the read-back after it `freeze2/verify_frozen_2.py` and its output; its rehearsal on a scratch copy is `freeze2/freeze_2_rehearsal.out`.

- The second environment record differs from the first in `recorded` and the four threading fields alone, each from `null` to `"1"`. The second `FROZEN.json` differs from the first in the environment record's pin, `written` and `go` alone: the same 15 other pins at the same SHA-256, and the terms, the manifest, `solver_commit` and `freeze_numbers` unchanged. Its pin is `88940b293d440dd0…`, the pin the run's log records, and #703's block carries it in full.

  | File | SHA-256 |
  |---|---|
  | `run/ENVIRONMENT.json` | `9416dd934575ab88b778b8cbd0a72b02a0109fe6a07f2f193e75f50bb516a43e` |
  | `run/FROZEN.json` | `88940b293d440dd004377d1ba1ad948d945a38cf99e375e4640b1449fe9f445c` |
  | `run/FROZEN_PIN` | `fa1f859b1c702c727d488abed46ff2a3cebd7d31a615623f6b682d071fdc611f` |

### 1.4 Before the launch

- **The checks before the launch,** read-only, by `freeze2/preflight_checks_2_merged.py`, revised for #703's merge from `freeze2/preflight_checks_2.py` by the changes `freeze2/preflight_checks_2_to_merged.diff` shows. Its run before the launch, `freeze2/preflight_checks_2_merged_run2.out`, passed all 29. Among them: the bench's copy against `SHA256SUMS`, the commit's tree and the second freeze's three files and nothing else, with no `run/out/`; `validate_frozen` and the environment check by the launch's route, in a fresh process; the first freeze kept at #702's pins; the instrument at its manifest, with no cache; the go, the ruling and #703's approval unedited, #702 and #703 merged and the second block on OpenWave's `main` byte for byte; mains power, Low Power Mode off, no macOS update set to install itself and macOS the record's; disk and load; and no M8.19 process.
- **Its earlier runs stand,** with nothing launched after either: `freeze2/preflight_checks_2.out`, before #703's merge, 25 passed and 2 failed (on mains power; Low Power Mode off); and `freeze2/preflight_checks_2_merged.out`, 28 passed and 1 failed (no other process above 50% of a core), with `mds_stores`, Spotlight's indexer, above half a core.
- **The revised checks' mutation arms,** `freeze2/mutations_preflight_2_merged.py`, run three times. In the first two, the strict comparison marked 5 arms BAD in all, each with the load check red beside its named checks while a browser ran (`DEVLOG.md` entry 27); the third: "mutations_preflight_2_merged: PASS 7 arms and the control".
- **#703's merge, read back** by `freeze2/merge_703.py`: 19 checks passed, "merge 703: PASS"; its arms: "mutations_merge_703: PASS 6 arms and the control".
- **On the first freeze,** before the refused launch: `freeze/preflight_checks.py` and its output, "pre-flight: PASS".

### 1.5 The launch and the run

- **The launch.** One launch on the second freeze, on the author's word, by the command `DEVLOG.md` entry 30 records, from this folder, as a background task on mains power with Low Power Mode off: `python3 -I -B -u run/m819_run.py`, its console into `freeze2/launch_2.out`. Before `launch()`, `main()` ran `validate_frozen` and the environment check by the launch's route; the console shows the record, the live reading and "differences: none". `launch()` held `caffeinate -i -s -w` on the orchestrator's process.
- **The run.** Its log, `run/out/RUNLOG.json`, opened at 2026-11-10T03:53:24Z at the second freeze's pin, not on the bench, its launch numbered 1, and ended at 2026-11-10T14:42:59Z, 38975 s later. Each of its 17 jobs started once and completed, at most four at once and each on one thread; none ended its part of the run, none was not run, and no stop was recorded. The plan read the gates and added one test, `test_C2a_R5_1`. The environment, as `run/ENVIRONMENT.json` records it: CPython 3.13.13, NumPy 2.5.0 and SciPy 1.18.0, on Accelerate's BLAS and LAPACK as each reports them, under macOS 15.8.2 (24H232) on one Apple M3 (Mac15,13), 4 performance and 4 efficiency cores, the four threading variables at `1`.

  | Job | Wave | Started | Completed | Seconds | Peak resident, GB |
  |---|---|---|---|---|---|
  | `dyn_C1` | 1 | 2026-11-10T03:53:24Z | 2026-11-10T05:39:53Z | 6389 | 1.06 |
  | `dyn_C2a` | 1 | 2026-11-10T03:53:24Z | 2026-11-10T05:39:14Z | 6350 | 1.13 |
  | `dyn_C2b` | 1 | 2026-11-10T03:53:24Z | 2026-11-10T04:59:02Z | 3938 | 0.69 |
  | `dyn_C3` | 1 | 2026-11-10T03:53:24Z | 2026-11-10T05:43:01Z | 6577 | 1.13 |
  | `rate` | 1 | 2026-11-10T04:59:02Z | 2026-11-10T06:53:52Z | 6890 | 1.03 |
  | `p5a` | 1 | 2026-11-10T05:39:14Z | 2026-11-10T05:39:23Z | 9 | 0.73 |
  | `c3e3` | 1 | 2026-11-10T05:39:23Z | 2026-11-10T07:34:11Z | 6888 | 1.08 |
  | `c2a_dur` | 1 | 2026-11-10T05:39:53Z | 2026-11-10T09:30:23Z | 13830 | 6.04 |
  | `controls` | 1 | 2026-11-10T09:30:23Z | 2026-11-10T09:30:24Z | 1 | 0.08 |
  | `gates_T1_R4` | 2 | 2026-11-10T09:30:24Z | 2026-11-10T10:25:09Z | 3285 | 4.24 |
  | `gates_T1_R5` | 2 | 2026-11-10T09:30:24Z | 2026-11-10T11:20:51Z | 6627 | 6.69 |
  | `gates_T4_R4` | 2 | 2026-11-10T09:30:24Z | 2026-11-10T11:01:22Z | 5458 | 4.22 |
  | `gates_T4_R5` | 2 | 2026-11-10T09:30:24Z | 2026-11-10T13:00:19Z | 12595 | 8.43 |
  | `coherent_R5` | 2 | 2026-11-10T10:25:09Z | 2026-11-10T12:02:34Z | 5845 | 8.42 |
  | `plan` | 2 | 2026-11-10T13:00:19Z | 2026-11-10T13:00:20Z | 1 | 0.08 |
  | `test_C2a_R5_1` | 4 | 2026-11-10T13:00:20Z | 2026-11-10T14:42:58Z | 6158 | 1.28 |
  | `record` | 5 | 2026-11-10T14:42:58Z | 2026-11-10T14:42:59Z | 1 | 0.08 |

### 1.6 After the run

- **The outputs.** The run's log records 64 files for the completed jobs. 62 are published byte for byte, each at its logged SHA-256. The console logs of `gates_T4_R4` and `gates_T4_R5` are published as path-redacted archival copies, at SHA-256 values of their own (§ 1.7); `ARCHIVAL.json` gives each copy's SHA-256 and its original's, the one the log records. The originals are not in this folder, so their logged SHA-256 cannot be recomputed from the copies alone. No folder in `run/out/` stands outside the log, and the staging folder was empty when the run ended (`DEVLOG.md` entry 31).
- **The environment, read again** after the run, at 2026-11-10T15:36:59Z, by the launch's route, `tools/postrun_env.py`, which replays `main()`'s two calls as `freeze2/freeze_2.py` replayed them: `validate_frozen` passed, with 16 pins and the ruling as its go, and the check read no difference (`environment_postrun_2026-11-10.txt`).

### 1.7 The published files

- **As published from the run:** `run/out/`, 65 files, the log among them, each at the SHA-256 below; the 2 console logs marked are archival copies, each beside its original's SHA-256, the one the log records.

  | File | SHA-256 |
  |---|---|
  | `run/out/RUNLOG.json` | `a1ffbb0ec4523c92bbc13016d687702ad896f2d8360595b9bd2b06b8ab3255f7` |
  | `run/out/dyn_C1/console.log` | `b8025ffeb1b16fa4afc8b3b6f6c7a4b814234be9d53d75f384f317cadfcbc903` |
  | `run/out/dyn_C1/dynamics_C1.json` | `8c4ab8971757bcd166f3276dc20c7da4551262eb495adcd4f3e079f6fe7dfd25` |
  | `run/out/dyn_C1/dynamics_C1.npy` | `e29625fca70916e8ab5c8eec8eb077356835347ce06449cd58978cac64786201` |
  | `run/out/dyn_C1/job.json` | `8458c567a98fa3bb0fcc8cedc3ffd21880e2ca1a7e55b2fb5914b7e8f6ac66ab` |
  | `run/out/dyn_C2a/console.log` | `7169ed4065c6ca09b3dab455be8caa85e31af3e675bbf7aa63173da737aef0dc` |
  | `run/out/dyn_C2a/dynamics_C2a.json` | `1dce41f11c1b65134757d39d0bc0cfa22c85b83c6b80fce0e1c5109614e7c625` |
  | `run/out/dyn_C2a/dynamics_C2a.npy` | `73d85070daeb45d2ff91908f6e68ac927164f2b493b518c7cb27a6760ea6b693` |
  | `run/out/dyn_C2a/job.json` | `4f65cc09610284b29f26862c0c19e0ee7b9451743963c1364507616181b78da9` |
  | `run/out/dyn_C2b/console.log` | `2034ff2063915e30d1883b0c75d8f828d4717b97c0b32074c03a6a65746e6019` |
  | `run/out/dyn_C2b/dynamics_C2b.json` | `bd035b8d5b211b00deb4e0fe5cf19cd255fd0be959279233218b63e283013055` |
  | `run/out/dyn_C2b/dynamics_C2b.npy` | `2beb802872dd80d9fe0d6f977c051b885466b572b834e12ffd191bcbcdd4d116` |
  | `run/out/dyn_C2b/job.json` | `513f4bb41aaf3fdbdcd93e4ab39fb9a79059b6a45816bed542c7b5b6ba398694` |
  | `run/out/dyn_C3/console.log` | `f013f25ab6cbb443d8093e777f5f3c1fc762366d9387a3db3daefb2db21e5f24` |
  | `run/out/dyn_C3/dynamics_C3.json` | `c8a35bf788894a661e248475484fb9633f98366c02c9a97b5f514d7739806bd0` |
  | `run/out/dyn_C3/dynamics_C3.npy` | `598b434ab364a53f433f70ebecd637ac09606c7206a299bfe987f540849dc982` |
  | `run/out/dyn_C3/job.json` | `48bee20c74aa83802cd66afb794bc4bdd924f224ec60a6a3ad70449ae945bb71` |
  | `run/out/rate/console.log` | `c2078cadcf9751fe7c83207f1a933f986c302edbb85d2a8fa34b6f49794a6e00` |
  | `run/out/rate/dynamics_C3_rate.json` | `da039d1f1c7d8ac0ceee1e28d0eb23ac0d5b1f93bde6ebc1636d7ee4f1accc1c` |
  | `run/out/rate/dynamics_C3_rate.npy` | `cc0d9a958c0b84b851805021f4a7316b2fd5f279627dd11c38d829bbbc86503e` |
  | `run/out/rate/job.json` | `aceb377111a674add5d76d0eb01e6bd753ba09b34898273101cc16f0f83438e6` |
  | `run/out/p5a/console.log` | `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` |
  | `run/out/p5a/control_1a_arm.json` | `c80aeae4b15190ec9e281642bf0e2c5baa24ba427184dfdcfe43cef7af99160c` |
  | `run/out/p5a/job.json` | `53cfec67d6e5b0e2275bb1c78bb7e213f734c1daa00c1caac7adf888a0d9ae76` |
  | `run/out/c3e3/console.log` | `58af8f595b8a7db564a3dc58c3a4eb19dd27a7609a9d1480da3d880d932bfbbd` |
  | `run/out/c3e3/dynamics_C3_eps3.json` | `41da04854c86a9fda0b2cbe35400b63dfbdc276830b36650bffab653ca982503` |
  | `run/out/c3e3/dynamics_C3_eps3.npy` | `4788d0e065611475586ea285db15c2c50630acd7bae4c666d1f4fe456b8d69e6` |
  | `run/out/c3e3/job.json` | `97482c9a3045396714dbc73c1585e261c7c770b465de3f26997f014044489dbe` |
  | `run/out/c2a_dur/c2a.json` | `a009a7f4d75deb2c701ee65dee7691fd2d1f2a0263a5636b3f941a6eae6ca35e` |
  | `run/out/c2a_dur/console.log` | `02c74e9db9a1a5f303fe44977f8a3c673d94b7c3d7e2d7b9cc20fdc3d429b2f5` |
  | `run/out/c2a_dur/job.json` | `cc86890f82e4c4dfa906122080c3d763504d6251fb0c0d09a38a7bc593e3e645` |
  | `run/out/c2a_dur/test.npy` | `78e3c390ea2ef73ffd6b9743f2bc51234f75f57d694d702185b55c61d75c86f1` |
  | `run/out/controls/CONTROLS.json` | `05460c8d2a15bcffdf6224172df10d9988ce915d88de03405c3ff4735a083b2e` |
  | `run/out/controls/console.log` | `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` |
  | `run/out/controls/job.json` | `df4ad00ea43228522b2c66c878dbe606b0c246908928ea32d7fb679f898ee51e` |
  | `run/out/gates_T1_R4/console.log` | `ec74752d68203088d90b2088bf8a8832b080b9dbfc78fbaf31e7407efd04903f` |
  | `run/out/gates_T1_R4/gates.json` | `719cfaadcce80a9d813eadd4b1a07bd2185ecc601d78615b440715734cae9721` |
  | `run/out/gates_T1_R4/job.json` | `79778c1bfcc4e33bcedbff7b8619caf7059ba4e52b1d3e79753ddb59d63aaef4` |
  | `run/out/gates_T1_R4/states_L2.npz` | `4880a0060ff11e50aeb02c220b44a59f818a14a34e17a8e988528ffabe755917` |
  | `run/out/gates_T1_R5/console.log` | `96381fe3d656eb72af9626b25cdbca836f80d28189490e7b8acc064fdc292451` |
  | `run/out/gates_T1_R5/gates.json` | `0e65b3ea8f8f99d4cf94047934e11f580f29819c64a9d343321d9e9367e25688` |
  | `run/out/gates_T1_R5/job.json` | `9feba14be581122041222c5555cecbe9c346cf6fce1e497fe0bb7c11e2199858` |
  | `run/out/gates_T1_R5/states_L2.npz` | `273e4daa92862926913795ad65d5de222d7261ddd9d0441fecfaa45cc005a43d` |
  | `run/out/gates_T4_R4/console.log` | `3ea41e067989d558be8c118b2d10b63b41ad575b7512fe9bcd043c83b52de7d2`, an archival copy of `582ddfc36c7838be36eb7931749e8fde6b7afb1fbcc6d2562f1c003db1a286cd` |
  | `run/out/gates_T4_R4/gates.json` | `9eed29cf159f5623d4a6d73541c037d137cd9f5a82a7e22ec331c761d9c9d194` |
  | `run/out/gates_T4_R4/job.json` | `93199668566e6c5aec32c4c383336d34ce74ac567e34527309583eccd3c87592` |
  | `run/out/gates_T4_R4/states_L2.npz` | `ffe5b635b64f28a2d0dd0b376d27b6555edf28e2ed3177fd21cefb950aec4a09` |
  | `run/out/gates_T4_R5/console.log` | `1f75bbb731f0fd6e38152650820e6da83c8e706cc2a67cd1a5b2951ff332f703`, an archival copy of `6e458c3cfb7baf8f561f721dde5362c873ac80b559001d5ae9f1281d0471ef45` |
  | `run/out/gates_T4_R5/gates.json` | `6fdf76d46d148043e79a2d2ef6e603b88a633a2b125f068d8a7e51ade1d73e65` |
  | `run/out/gates_T4_R5/job.json` | `9e6bc03f5582209d2775037e02a464619029bb004f49551e9e12251717128b06` |
  | `run/out/gates_T4_R5/states_L2.npz` | `b52337b3a2259ea80e7b55f6ff149f868480144fe4f3101bccb625620fbbfaa2` |
  | `run/out/coherent_R5/console.log` | `70b9d201e7783493c061cedaa27cace1d0c0ea464c84b734783b7f1e9967ede3` |
  | `run/out/coherent_R5/gates.json` | `033fb00b47444de47123cf68f2d95ae89712eba235b4893830b8a51392b1796d` |
  | `run/out/coherent_R5/job.json` | `ec41fab00d22a171d366dc7c39015b0db9d370dbb9ff31ec937b5dfa7d915971` |
  | `run/out/coherent_R5/states_L2.npz` | `b4eac660b34ea4d4087be932caffb30b03414a4f31429d0f51778eec2b8bcf4b` |
  | `run/out/plan/PLAN.json` | `fdf0f9cb1c120b591f639938fc60b10c93697dc674672fc419be96af162a92df` |
  | `run/out/plan/console.log` | `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` |
  | `run/out/plan/job.json` | `f543d578710957faa8be19e58b8a072fcef47ec32436def241527dd891e6c76f` |
  | `run/out/test_C2a_R5_1/console.log` | `cef4e80fa5503ff7394fea6311a4bcfc08517c9a752f18ba3280630cdc4a0ec3` |
  | `run/out/test_C2a_R5_1/job.json` | `e510d2c7b0a18dfa16537189d5964fe1df4cc2543347cc1f82c1b65a6996712a` |
  | `run/out/test_C2a_R5_1/test.json` | `0e12fabbfb52b7cd815c2df8531ece465b6fdb27f8a1377fb697e8f603d1c646` |
  | `run/out/test_C2a_R5_1/test.npy` | `5d64efdf62541150b662626f7488c59eb529e28fd6abb6fe1b77fd7c0944852b` |
  | `run/out/record/RECORD.json` | `0a869b34c672837f3eee17bdff8b9d82fe51fc64a6077aa9d26e0079089ba2df` |
  | `run/out/record/console.log` | `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` |
  | `run/out/record/job.json` | `cb82b3a4d07e1071193decd5585e2787593b509e2a5f227ddf5ebbf0dceeecd4` |

- **The freeze's files,** from beside the folder on the bench: everything `freeze/` and `freeze2/` held but the bench's DEVLOG writers, its packet cover and the pull requests' text builders, which wrote prose, not records. 35 go out as they are:

  | File | SHA-256 |
  |---|---|
  | `freeze/bring_to_commit.out` | `7e577da91f83e5dc5a6c2d58565922183aee93149b4aa5befb376573617990f9` |
  | `freeze/first_freeze/run/ENVIRONMENT.json` | `43b7d084a46860ca1700030445569780d87edf5484b1801932b08903cdad3c3f` |
  | `freeze/first_freeze/run/FROZEN.json` | `1e5107d0c6117a7d45c378827b8ee6670c1ce8964b1099992be05e4769486393` |
  | `freeze/first_freeze/run/FROZEN_PIN` | `ea3320b424d620fb7b56c7da10808b7696b66f6e7265f7e6d4d8b034c8df7517` |
  | `freeze/freeze_block_build_v1.out` | `86ebcf8bb1f87564d14428b4fa9d5245df313d04ec10a1960e47fbacd4f58f9f` |
  | `freeze/freeze_block_build_v2.out` | `04c6137c63c4d3d9a36d640e235f654bc45fd1324d2f495b7dbd32868f476ff1` |
  | `freeze/launch_1_refused.out` | `422529a5a7b3abbb10f789f0a0a59fb1b140b03231862314997d22f7c01f3bf3` |
  | `freeze/preflight_checks.out` | `99d98e1f45b680a70c7f9ce4489d5f17da4f26424927780dc6a0b64158f71b78` |
  | `freeze/reconcile_copy_2.out` | `42fd4abe85ce4a365f8404dbc6f73f39d285899d64b1219e5ccee90d9e8a484a` |
  | `freeze/record_environment.out` | `5164b0c358be4de3715947306bd17874b5df244ebff81ea1746437c2675bf329` |
  | `freeze/record_environment_check.out` | `37ff13a0681f43a7454612ddc5ea580af7723af9acb9b7afb705e1003497b0b7` |
  | `freeze/rehearse_env.out` | `8f087655b5e38ef2003fb1460561b4827390c9804d28c73230ca10018c2d5c3f` |
  | `freeze/rehearse_launch.out` | `34233d1e91e32e288ed65cbc0604bdda5dd9e5a4af0556930278d143bc6a2d81` |
  | `freeze/sha256sums_check.out` | `2c6808d124e251f83335e6552cb873e95513a8adee1d824edd525bd4bc56a1b0` |
  | `freeze/sha256sums_check_2.out` | `63671df80e1b85a2a6f552cbd99d43fc5e9508683f4939e60e4d87cd027fad0a` |
  | `freeze/verify_frozen.out` | `576b605cd05a9897a075679a23e3a734dd8be6572449a2e00f8b4d7b98245d82` |
  | `freeze/verify_frozen_2.out` | `576b605cd05a9897a075679a23e3a734dd8be6572449a2e00f8b4d7b98245d82` |
  | `freeze/write_guard.out` | `ca9cbe95b86aa8bf29d028f2616b74e7c3f0237898b0a2a34cebb58b344e0208` |
  | `freeze2/checks_before_write_2.out` | `05aedb742616494b4375053c596d5027a4d005f1b2f69001ddd4515a487d015e` |
  | `freeze2/launch_2.out` | `13e2c5377565f01c4e19e9d0ef333e27d9b39a30d311b8baccd020e0994da43e` |
  | `freeze2/merge_703.out` | `3fbdeff7acaf567de88cc698296de54438a6f298d801f7cae4db4bd085c2863d` |
  | `freeze2/mutations_merge_703.out` | `e8497d345d54d9ad81cbaf70593f91139b30947346fcbeb01ff1457018963e34` |
  | `freeze2/mutations_merge_703.py` | `edc093bfa64acabc2329c17cd510da9f0470c6cb0704d8b0c410b653dc868857` |
  | `freeze2/mutations_preflight_2_merged.out` | `3bff852b10a2e0c892545a75e60e707f5eb65fb2590e31b005a6b1fd96920ce4` |
  | `freeze2/mutations_preflight_2_merged.py` | `c889bb7debf1b9aac958419305d5f9f349387a5c6c6abc9a88098c3505628242` |
  | `freeze2/mutations_preflight_2_merged_2.out` | `61bd54855e9e73c8ccfd833ad80fca06d235fc97e367dc3babe04abb75da4ae8` |
  | `freeze2/mutations_preflight_2_merged_3.out` | `d6cd33bd8b1e9699f595eb902163a17fb0c4367dd73b6c543e4113ea95e2e838` |
  | `freeze2/out/record_environment.out` | `2207799e6a05b5b74465e7e8173b9cd61ded4ed191d968f0915f284792044774` |
  | `freeze2/out/replay_main_checks.out` | `e7437c5fae7b3fa7ee78b05e69cdde087825dbec57082492b3dd4de703987ee2` |
  | `freeze2/out/sha256sums_check.out` | `901d5e597074d0c21b4cd6763508a4c2bb27ce9f23065cd81aff304996c8e4f4` |
  | `freeze2/out/sha256sums_check_after.out` | `901d5e597074d0c21b4cd6763508a4c2bb27ce9f23065cd81aff304996c8e4f4` |
  | `freeze2/preflight_checks_2.out` | `42f498f14a69489df6c982aee8eb48a2354a247c0dd8a50ede2587a9929bcaba` |
  | `freeze2/preflight_checks_2_merged.out` | `ab88ae95e8ff83bf3d059ee2ad66950dae3ecb6b62e4f31aea26d4ef4fc96840` |
  | `freeze2/preflight_checks_2_merged_run2.out` | `5c79716eae821572f56b08d1c4d8e612d55a8c702b87ae0d369f5811b5e5c374` |
  | `freeze2/verify_frozen_2.out` | `9c9ab4804d2e079b0247060ee1c719bd531b58ca1138acb918c658ad58cd5f73` |

- **The marked archival copies.** 24 files name a local path: 22 of the freeze's, and the 2 console logs. Each goes out as its original with each path replaced: in a script, a quoted path by `os.environ['M819_BENCH']`, `os.environ['M819_MIT_CLONE']` or `os.environ['M819_OPENWAVE_CLONE']`, plus the rest of the quoted text, and the clone's path from the home folder, inside `os.path.expanduser`, by `os.environ['M819_OPENWAVE_CLONE_FROM_HOME']`; in an output, the path by `<the bench>`, `<an MIT clone>` or `<an OpenWave clone>`, the placeholder the second block shows. `ARCHIVAL.json` gives the rule, and for each copy its original's SHA-256, its own and the lines where they differ; no copy claims its original's. A reader without the paths cannot rebuild an original; on the bench, putting them back gives each original byte for byte. Where a block or a pull request's body names the original's SHA-256, it is the one below.

  | Copy | Original's SHA-256 | The copy's SHA-256 | Lines that differ | The original named in |
  |---|---|---|---|---|
  | `freeze/bring_to_commit.py` | `6c4c0a500b494abb022278755dc93968a59e7ccf99eeca9877f8f9d8f549ad6e` | `45775b31effa3949af0dbe76a9b856c2434cce9d50f88f81d647177f235ba19f` | 5, 7 | this record |
  | `freeze/checks_before_write.out` | `9750a8fd8254dcf7084168f6264e8444baa327846304f74abeaa2db8774ba377` | `112a37fc313fdd0a8f1e8229ff7eb51105ef115ab1c9734b35434968face656e` | 14 | this record |
  | `freeze/checks_before_write.py` | `9faf8270ff1e4421b1bcee56db00a548df1dc32d00c265a87f3ba1cee0ab9e99` | `77ad10f688396daab06acab89d8dbb8833f4a0f304154e160e70f0301bd5d35a` | 5, 8, 11 | this record |
  | `freeze/freeze_block.py` | `0af0d171ce176effccdf8756edacb860e61dc8f793c150f8d01014e06e45f3a5` | `c48602ad040454cad601fd6ed2aaa6bf8743002ff5af5b89a4e3f406c4174c91` | 27, 29 | #702's body |
  | `freeze/preflight_checks.py` | `1c5daca4ca6da17bdf519a4be6f4c927b28d2050c563be1672da234a91a42f43` | `9d6494daa5f2e5feee9d3ebc775186c6f2e327755259d7aa16a2e781f1f45e33` | 7, 9, 13 | this record |
  | `freeze/reconcile_copy.out` | `d6a0a8eee28cd64a6793fd928896d3f6426b39484bd947f55d2c2dfa365c7626` | `a3c8abec9720dac3b272adf6011d9ce4b553683fdddbe076a505ab910c297be5` | 7 | this record |
  | `freeze/reconcile_copy.py` | `cd718a121fed5713fac6b64e24e9b1ddc4b9594d13246bd595b896059928427c` | `cea78109c95b67b72cc0ec58ccb5e0d3b89145cb49ce1119e7d5945085213387` | 8, 10 | this record |
  | `freeze/reconcile_copy_2.py` | `2baab12ba5d27f7c8396d72aa8e74ab2b555d00dace994cb4557316180f11382` | `ee40ae6bd5d755f65560d1758737104c229e8b531956456d78d7770b4da939f8` | 6, 8 | this record |
  | `freeze/rehearse_env.py` | `3ed5d9ab7c5438a9f583763cbd0827ec9387a8d5096893134f85eb3d2f280972` | `77650213361194b1a95b98382a3d3856e188a82ac617e46f24dce524f0abeb8d` | 5 | the second block's § The scripts |
  | `freeze/rehearse_launch.py` | `6d9ea94d736a8ce126258e9f78f66579b7bb02f8b9e5d7944fa46ee7d582a823` | `15f19455645f29f8d56fe787f21815e6751a76f130aef57e5ea9c5f5cca05310` | 8 | the second block's § The scripts |
  | `freeze/verify_frozen.py` | `229ad02ddec685d4040fcbe89b77bff1e7d671e688ca1d8184b16577a76434b6` | `80c21fb3761cfb8651f3115a6037bb82b76cafbc968fcf9121b02064496c64c8` | 5, 7 | this record |
  | `freeze2/checks_before_write_2.py` | `b4a936553e502a70c48a46109c54b0c90062d89a46bf17b8285d507d59984c5e` | `7bfd35083c5b8ea13cecf2511f01682e9391558b1e87f6924e0e586fa0ba2a41` | 9, 12, 15 | the second block's § The scripts |
  | `freeze2/freeze_2.out` | `e06eda9fb719740ef5de89ab70bfbd9fa53734d2bee9f40af349ae46836b63b2` | `8f4de6ca9cc611b772d20994a06bdb96cce55341a153f5a9d54c6e3cc074b2d8` | 1, 2, 18 | the second block's § The scripts |
  | `freeze2/freeze_2.py` | `c3ac9855a3daaea92918e7fc19ff4e7baeb43198b959882b8299eb1638bcc4b1` | `e64d688aab61d60a2232f8310c0ac3bef195dabcca0d73867746fde30c44a14d` | 21, 23 | the second block's § The scripts |
  | `freeze2/freeze_2_rehearsal.out` | `46f50cb82f1a5b45a2263d10abf688d0b8cc06734b41b62e4d4f603eab96400c` | `35afd6ee75899df3a3e5ccfa0a820b3396d79ba46ff7f14fe1840bc065302dca` | 19 | the second block's § The scripts |
  | `freeze2/freeze_block_2.py` | `8589c001c2e8caeb833c0af01f09aee0efffb31cb644fed26c4f3e3cd4711faf` | `b8562f996439f971ac827a52075bd09871de3cafa44ffbbb2248d6eca0a0e880` | 30, 34, 35 | #703's body |
  | `freeze2/merge_703.py` | `460db1cac031a0df03138d582e64f54e36dcd7356698de14a699d105686c9071` | `733100f0ec5f78e39ec66e8b3a15de037c2f77ee1240e0dfec35904a28698b55` | 12, 16 | this record |
  | `freeze2/out/write_guard.out` | `9e415ddf3487d07fef060ce8fde0a2374816e155a36d91e0f26f691efc490a88` | `7f80e65862b66ff10f2565fd3f24c585c5b5a4198f63a8c22a185df107b2a3dc` | 1 | this record |
  | `freeze2/preflight_checks_2.py` | `d21310cedb6199e3c91b8c214019032cb8476082af6da8b8952d42848c2d6a02` | `2fc7790e5b08d26a5f18ff38d6abd40fc3bc4d4dfbb7e42a208a603fe0787e2c` | 11, 14, 18 | this record |
  | `freeze2/preflight_checks_2_merged.py` | `f00f245b471c300f256350916130af741ff3770b7c333ccb015bd3443693a663` | `204b785127be342ecc15306d1bfe828cb0d2036a2670c5b89205e636791869d6` | 13, 16, 20 | this record |
  | `freeze2/preflight_checks_2_to_merged.diff` | `e8ccf2524fb80be25dc9e299338dcc71d2e2222e483ccbd61650153cbd5b6102` | `e8417273e09da9b4af204c2e1cf3601b3cc7e46db42ca5b5a57b95b7dc76f787` | 25 | this record |
  | `freeze2/verify_frozen_2.py` | `74c916d1c92ff94da6d1dac786101bdda9cd01934eb804c866c1c554c3298802` | `cc0291b9470a151937e9d96d842d9f4459b10cf99a58f6ecf10482cafc347937` | 8, 11 | the second block's § The scripts |
  | `run/out/gates_T4_R4/console.log` | `582ddfc36c7838be36eb7931749e8fde6b7afb1fbcc6d2562f1c003db1a286cd` | `3ea41e067989d558be8c118b2d10b63b41ad575b7512fe9bcd043c83b52de7d2` | 9 | the run log |
  | `run/out/gates_T4_R5/console.log` | `6e458c3cfb7baf8f561f721dde5362c873ac80b559001d5ae9f1281d0471ef45` | `1f75bbb731f0fd6e38152650820e6da83c8e706cc2a67cd1a5b2951ff332f703` | 12 | the run log |

- **Post-run files,** made or placed after the run, not records from it:
  - `environment_postrun_2026-11-10.txt` and `tools/postrun_env.py`, the reading after the run (§ 1.6);
  - `tools/build_record.py`, which builds this record from the files and, with `--check`, reports any difference;
  - `ARCHIVAL.json`, the index of the archival copies;
  - `DEVLOG.md`: entries 1 to 10 as MIT `94a679ac` holds them, then entries 11 to 34, kept beside the folder from the freeze to the record, since the go pins this file through `SHA256SUMS`, and copied here byte for byte. Their paths are the bench's: `../freeze/` and `../freeze2/` beside the folder are this folder's `freeze/` and `freeze2/`, and the review packets they name stay on the bench;
  - `SHA256SUMS`, regenerated over the published folder at the record's commit, one line per file but itself. The pre-run inventory stays at MIT `94a679ac`.

  | File | SHA-256 |
  |---|---|
  | `environment_postrun_2026-11-10.txt` | `32e3480665a86befb2fd37d8cfc5e1f4c72b9372940f5b48821a53970dfa51a8` |
  | `tools/postrun_env.py` | `c6759ede309116415abeea71d6509ea501ecfc4292f666393c88a68acbe3b270` |
  | `tools/build_record.py` | `db5e09a93d594db5c7398e908e05e2c98c7c47c633fb9e3abd897e173714cb57`, as it built this record |
  | `ARCHIVAL.json` | `b27af0869bc69121ad6e2b284370f74df4b2d023c3c7eb067f089d47e8a0266c` |

## 2. Gate 1: the controls

`controls` read the eight wave-1 records, and every control passed (`run/out/controls/CONTROLS.json`, `all_passed`). This record recomputes each dynamics verdict from its stored series with the frozen `persistence.evaluate`, and the rate as `job_controls` fits it; each equals its record.

| Control | The terms ask | The run reads | Passed |
|---|---|---|---|
| C1 at `ε` = 6 | Persists | Persists, max d_⊥ 1.00×10⁻³, valid | yes |
| C2a at `ε` = 1 | Persists | Persists, max d_⊥ 1.00×10⁻³, valid | yes |
| C2b at `ε` = 1 | Persists | Persists, max d_⊥ 1.00×10⁻³, valid | yes |
| C3 at `ε` = 1 | Fails | Fails at `t` = 583.28, valid | yes |
| C3's rate run, `η` = 1×10⁻⁷ | the fitted rate within 5% of the linear one | 0.009741 against 0.009737 at level 2, 0.03% apart, over 655 points | yes |
| `P5a`, control 1a | the seed solve stops under the repaired test below 10⁻¹¹ | stops at iteration 3, at 4.35×10⁻¹³ | yes |
| C3 at `ε` = 3 | Fails | Fails at `t` = 202.75, valid | yes |
| C2a/R4 at `ε` = 1, `T` by gate 6 | Persists, valid, at `T` = 2750 | Persists, valid, at `T` = 2750, max d_⊥ 1.00×10⁻³ | yes |

C3's rate run reads "Invalid (Fails on an invalid run)" under the frozen validity rule, as on M8.15's record; the control is its fit. C1, C2a, C2b and C3 reproduce M8.15's record: C3 Fails at 583.28 and the rate fits 0.009741 against 0.009737, as § Known outcomes gives them. The second energy rule, `valid_under_v6_energy_rule`, recorded and not scored, is false on every run the frozen rule reads valid, and true only on the rate run, which it reads invalid, as the terms disclose.

## 3. The gates

Each row was solved at levels 3 and 2 along its continuation path to its highest classified point, and gates 2 to 7 were read and written at every point before any target evolved. This record recomputes every point's gates from its stored input with the frozen `m819_gates.evaluate` and the instrument's `classify`, and each stretch's search with the driver's `stretch_tests`; all 61 points and every stretch equal their records, and so does the plan.

- **Gate 2 passed at all 61 points:** an accepted Newton solution at levels 3 and 2, on the continuation path from the seed, at T4's 19 points as at the others.
- **Gate 3 failed first at every point of T1 and T4,** 46 points. Its reasons, as each row's `gates.json` states them:
  - **T1/R4**, all 13 points: "level 3 cluster check; level 2 cluster check; level 3: no genuine imaginary mode with Krein sign -; level 2: no genuine imaginary mode with Krein sign -".
  - **T1/R5**, all 14 points: "level 3 cluster check; level 2 cluster check; level 3: no genuine imaginary mode with Krein sign -; level 2: no genuine imaginary mode with Krein sign -".
  - **T4/R4**, 8 points: at 0.25, 0.7071, 1, 1.41, 2 and 2.83: "level 3 cluster check; level 2 cluster check"; at 0.3536: "level 3 cluster check; level 2 cluster check; level 2: the mode is not identified: 2 candidates of Krein sign - within 5% of the slowest (moduli 4.05038e-05, 4.05038e-05), where the reference's multiplicity is 1"; at 0.5: "level 3 cluster check; level 2 cluster check; level 2: the mode is not identified: 2 candidates of Krein sign - within 5% of the slowest (moduli 7.25914e-05, 7.25914e-05), where the reference's multiplicity is 1".
  - **T4/R5**, 11 points: at 0.25: "level 3 cluster check; level 2: the mode is not identified: 2 candidates of Krein sign - within 5% of the slowest (moduli 8.41584e-05, 8.41584e-05), where the reference's multiplicity is 1"; at 0.3536: "level 3 cluster check; level 2: the mode is not identified: 2 candidates of Krein sign - within 5% of the slowest (moduli 0.000101051, 0.000101051), where the reference's multiplicity is 1"; at 0.5: "level 3 cluster check; level 2: the mode is not identified: 2 candidates of Krein sign - within 5% of the slowest (moduli 0.000124914, 0.000124914), where the reference's multiplicity is 1"; at 0.7071: "level 3 cluster check; level 2: the mode is not identified: 2 candidates of Krein sign - within 5% of the slowest (moduli 0.000156723, 0.000156723), where the reference's multiplicity is 1"; at 1, 1.41, 2, 2.83, 4, 5.66 and 8: "level 3 cluster check; level 2 cluster check".
- **The Krein count at level 2.** It does not balance at 8 of T4's 19 points: T4/R4 at 0.25, 0.3536 and 0.5; T4/R5 at 0.25, 0.3536, 0.5, 0.7071 and 8. There the frozen code ran its fast-spectrum search, which did not balance it either; elsewhere, at both levels and in every row, the count balances. No gate reads the count or the search (§ 9).

## 4. The coherent row in `R5`

- **The ladder.** C2a's case in `R5` from its seed along the ladder to 32, with M8.15's frozen linear types at level 3 cross-checked at level 2: 15 points, every one Elliptic, no change of type, each level's path reaching `ε_max`. The validity check at 0.25 passes, its worst relative 0.0133, and the types on the stretch on record, 0.25 to 2, are M8.16.1's, Elliptic, so the ladder is established, no cause named. Its stretch is the unbroken run of Elliptic points that contains 2, here the whole ladder, so there is no other Elliptic run, and nothing is newly identified.
- **The gates on its stretch,** each point's as `run/out/coherent_R5/gates.json` gives them: at gate 3 the identified mode's Krein sign and modulus at level 2; at gate 4 the levels' relative difference and, where OpenWave's record holds a harmonic reading, each level's from it; and gate 7's `r T` against its bound, ln(1/(10η)) = 4.6052:

  | `ε` | Reference | Gate 3 | Gate 4 | Gate 5 | Gate 6 | Gate 7: `r T` | First failed |
  |---|---|---|---|---|---|---|---|
  | 0.25 | harmonic | fails: "level 2: the mode is not identified: 2 candidates of Krein sign + within 5% of the slowest (moduli 0.000300995, 0.000300995), where the reference's multiplicity is 1" | not read | not read | not read | not read | 3 |
  | 0.3536 | level3 | Krein +, modulus 4.36×10⁻⁴ | fails: "levels 2 and 3 differ by 5.596%" | not read | not read | not read | 4 |
  | 0.5 | harmonic | Krein +, modulus 6.25×10⁻⁴ | levels 4%; the reading, 0.321% and 4.31% | 0.0122 | `P` 10056.6, `T` 10250 | 1.43×10⁻¹² | none |
  | 0.7071 | level3 | Krein +, modulus 8.90×10⁻⁴ | levels 2.87% | 0.0124 | `P` 7062.4, `T` 7250 | 6.48×10⁻¹³ | none |
  | 1 | harmonic | Krein +, modulus 1.26×10⁻³ | levels 2.07%; the reading, 0.164% and 2.23% | 0.0126 | `P` 4990.1, `T` 5000 | -5.64×10⁻¹⁴ | none |
  | 1.41 | level3 | Krein +, modulus 1.77×10⁻³ | levels 1.5% | 0.0128 | `P` 3546.6, `T` 3750 | -1.87×10⁻¹² | none |
  | 2 | harmonic | Krein +, modulus 2.48×10⁻³ | levels 1.09%; the reading, 0.0848% and 1.18% | 0.0130 | `P` 2536.9, `T` 2750 | -2.53×10⁻¹³ | none |
  | 2.83 | level3 | Krein +, modulus 3.44×10⁻³ | levels 0.801% | 0.0132 | `P` 1828.4, `T` 2000 | 3.19×10⁻¹³ | none |
  | 4 | level3 | Krein +, modulus 4.72×10⁻³ | levels 0.587% | 0.0135 | `P` 1330.4, `T` 1500 | -2.42×10⁻¹³ | none |
  | 5.66 | level3 | Krein +, modulus 6.41×10⁻³ | levels 0.425% | 0.0138 | `P` 980.1, `T` 1000 | -2.26×10⁻¹³ | none |
  | 8 | level3 | Krein +, modulus 8.56×10⁻³ | levels 0.297% | 0.0142 | `P` 733.8, `T` 1000 | -1.96×10⁻¹³ | none |
  | 11.31 | level3 | Krein +, modulus 1.12×10⁻² | levels 0.19% | 0.0148 | `P` 560.9, `T` 1000 | -3.14×10⁻¹³ | none |
  | 16 | level3 | Krein +, modulus 1.43×10⁻² | levels 0.0946% | 0.0155 | `P` 440.2, `T` 1000 | -3.01×10⁻¹³ | none |
  | 22.63 | level3 | Krein +, modulus 1.76×10⁻² | levels 0.00368% | 0.0164 | `P` 356.7, `T` 1000 | -4.83×10⁻¹³ | none |
  | 32 | level3 | Krein +, modulus 2.09×10⁻² | levels 0.0856% | 0.0176 | `P` 300.3, `T` 1000 | 8.07×10⁻¹⁴ | none |

- **The search.** The test point is the stretch's highest point at which gates 2 to 7 all pass, 32; gate 6 sets its `T` at 1000, from `P` = 300.3, so no test needs more than 2750 and no longer control runs (`run/out/plan/PLAN.json`).

## 5. The test

`test_C2a_R5_1` reloaded the stored level-2 state at 32, rebuilt its point and checked it equal to the stored one, read gates 3, 5, 6 and 7 again and found them equal, then ran the frozen `run_test` at `T` = 1000: one perturbation draw at `η` = 1×10⁻³ with the frozen seed, level 2, split mode. It **Persists, valid.** This record recomputes the verdict and every field below from `test.npy` with the frozen `persistence.evaluate`; they equal `test.json`.

| Field | Value | The frozen rule |
|---|---|---|
| verdict | Persists | Fails if d_⊥ exceeds 100η = 0.1 first; Invalid (drift) if d_rot exceeds √η = 0.0316 first; otherwise Persists if max d_⊥ ≤ 10η = 0.01 |
| max d_⊥ | 9.96×10⁻⁴, at `t` = 0 | ≤ 10η = 0.01 |
| max d | 9.96×10⁻⁴ | |
| max d_rot | 1.68×10⁻⁶ | ≤ √η = 0.0316 |
| the reference's distance, the floor | 1.68×10⁻¹³ | ≤ η = 0.001 |
| charge drift | 1.68×10⁻¹³ | ≤ 10⁻¹⁰ |
| energy oscillation, of the perturbation's energy | 0.0898 | ≤ 0.25 |
| secular drift, of the perturbation's energy | 9.60×10⁻⁴ | ≤ 10⁻² |
| read until | `t` = 999.77 | |
| `T`, periods of `P` = 300.3 | 1000, 3.33 | at least one period, never under 1000 |
| `r`, the margin's rate | 8.07×10⁻¹⁷ | `r T` ≤ ln(1/(10η)) |
| the step, steps, observations' cadence | 0.008187, 122150, every 122 steps | |
| seconds | 6148 | |

Its largest d_⊥ is at `t` = 0: the perturbation's own size, which it never exceeded. The second energy rule, recorded and not scored, is false here, as on every valid test on record.

## 6. The outcomes

Per stretch, with no aggregate, as the terms' § THE OUTCOMES gives them:

| Stretch | Outcome | As the terms read it |
|---|---|---|
| T1/R4, lower | Untested, gate 3 first at every point | "where no point passes the gates, with each point's cause" |
| T1/R4, upper | Untested, gate 3 first at every point | "where no point passes the gates, with each point's cause" |
| T1/R5 | Untested, gate 3 first at every point | "where no point passes the gates, with each point's cause" |
| T4/R4 | Untested, gate 3 first at every point | "where no point passes the gates, with each point's cause" |
| T4/R5 | Untested, gate 3 first at every point | "where no point passes the gates, with each point's cause" |
| The coherent row in R5 | Persists, valid, at `ε` = 32 with `T` = 1000 | "the stretch has its test, as S5 asks" |

The ladder's outcome, recorded apart: established, Elliptic at all 15 points to 32. No outcome claims orbital stability or instability: in the terms' words, "a test that Persists is evidence to `T`, not beyond". As the terms expected, and claimed as no evidence: T1's three stretches untested at the cluster check, as on M8.15's record, and the coherent row tested; for T4 they named no expected outcome. This record applies no ending under S5: under the answer of 2026-11-07 and the readings the approval of #698 confirmed, that is the adjudication's, stretch by stretch.

## 7. What is new

- **T4's standing waves on the finite-element instrument:** accepted Newton solutions at levels 3 and 2 at all 19 of its points, where M8.15's Newton failed at the seed (the terms, § Known outcomes).
- **The coherent row's ladder in `R5` above `ε` = 2,** on this instrument: Elliptic at all 15 points to 32.
- **The coherent row's first persistence test in `R5`,** at 32.
- **Each point's gate-3 cause** on T1 and T4, at both levels, and the Krein count at T4's level-2 points.
- **C2a/R4 at 1 at `T` = 2750,** a duration no record held, Persisting, valid.

## 8. Deviations

- **None in the run.** It ran in the terms' order, from the pinned tree, by one command, once on the second freeze, with no relaunch and no stop. The launch refused on the first freeze and the second writing are the ruling's, recorded in § 1, and are not deviations.

## 9. Corrections and reading notes

- **A correction to the second block.** Its § The scripts says that, but for the outputs of `freeze_2.py` and of its rehearsal, "the other outputs go out as they are". `freeze2/out/write_guard.out`, the writer's step output, names the clone of OpenWave the terms were read from, in its command line, so it goes out as a marked archival copy like them, its original at `9e415ddf3487d07fef060ce8fde0a2374816e155a36d91e0f26f691efc490a88`. The block shows that command with `<an OpenWave clone>`, the placeholder the copy uses.
- **Two console logs** go out as marked archival copies, `run/out/gates_T4_R4/console.log` and `run/out/gates_T4_R5/console.log`: each holds a warning that names the bench's path to the instrument. Their originals are at the SHA-256 the run's log records, and no other output names a path.
- **The fast-spectrum search.** That warning, a `ComplexWarning` from `linearize.py`, is the trace of the instrument's fast-spectrum search, whose defect M8.15.x's `REPRODUCE.md` records and leaves unrepaired: at its two real shifts the search hands a real factorization to complex ARPACK. In this run it ran only at level 2 of T4, at the points § 3 names, where the Krein count does not balance. Its output is in each point's record, `fast_search`. No gate reads it: the gates read each level's cluster check, `tau_re` and genuine modes alone (`level_data`), so the defect moves no gate (DERIVED from the frozen code). The count is recorded and read for nothing here.
- **Control 1a's arm.** `run/out/p5a/control_1a_arm.json` names its arm `bench`. That is the arm's name in M8.15.x's qualification, `qualification/control_1a.py`, which the driver writes; the run's mode is in its log, not on the bench.
- **The approval of #698, its note on the controls' stage.** On M8.15's record the five control runs took about 12.2 hours on one thread. Here they took 8.37 hours in all, each on one thread beside up to three other jobs, and the stage with `P5a` and C3 at 3, 10.29.
- **The approval of #698, what it did not check.** Whether T1's cluster check fails on M8.15.x's instrument as on M8.15's: it does, at both levels at all 27 points (§ 3). That M8.15.x's persistence code reproduces M8.15's: the controls reproduce M8.15's record, C3's failure at 583.28 and the rate fit, to its digits (§ 2).
- **The go, reading 3.** The coherent ladder's stretch is the whole ladder, so the record names no other Elliptic run, and the standing the go leaves to the adjudication does not arise. The ladder above 2 stays unruled, as the go and the answer of 2026-11-07 left it; its outcome is recorded apart (§ 4).
- **#702's approval, what it did not check.** The first freeze's three files: in `freeze/first_freeze/run/`, at the pins it restates (§ 1.2). `freeze_block.py`: an archival copy, its original at the SHA-256 it restates (§ 1.7). That the run had not started: the log opens at 2026-11-10T03:53:24Z, after the go, the first freeze's written time and #702's opening (§ 1.1).
- **#703's approval, what it did not check.** The published freeze files and the refused launch's output: at the hashes § 1.2 and § 1.3 give. The scripts and `freeze_block_2.py`: marked archival copies, each beside its original's SHA-256 (§ 1.7). The steps and the rehearsals: their outputs, published. That the run had not started: the log opens at 2026-11-10T03:53:24Z, after the second freeze's written time, 2026-11-10T00:55:03Z, and #703's opening, 2026-11-10T02:07:48Z (§ 1.1).

## 10. Follow-ups, outside M8.19

- **The catalog.** After the adjudication, the census page's dated note gives where S5 stands, in the go's words, and the roadmap's row its Done.
- **The coherent row's ladder above 2.** How the census counts it is unruled, for the adjudication.
- **T1 and T4.** Their types stand as adjudicated; their persistence is untested here, each point's cause named.
- **The Krein count at T4's level-2 points, and the fast-spectrum search's defect,** recorded, outside this registration.

## 11. Reproduction

From a copy of this folder, beside the instrument at `../soft-slot-dynamics-m8-15x/`:
- `shasum -a 256 -c SHA256SUMS`;
- `python3 -I -B tools/postrun_env.py OUT`, which replays `main()`'s two calls by the launch's route, `validate_frozen` and the environment check against `run/ENVIRONMENT.json`, into a new file `OUT`;
- **the registered run:** `python3 -I -B -u run/m819_run.py`, from a copy without `run/out/`;
- `python3 -I -B tools/build_record.py --check`, which rebuilds this record from the files, recomputes every gate, the search, the plan and every dynamics verdict, and reports any difference.

Bitwise agreement on another machine is not claimed: the reproduction rules compare bit for bit on the recorded environment, which the readings before and after the run equal.
