# M8.18, the census's two remedies: reproduction

This is M8.18, the two remedies [#512](https://github.com/openwave-labs/openwave/discussions/512#discussioncomment-19278753) admitted after M8.17, on the rows [the Slot Dynamics Census](../../slot-dynamics-census.md) left not settled, with the instrument M8.16.1 qualified.
- **What it runs.** M8.16.1's instrument and run code, byte for byte: each file under `instrument/`, and M8.16.1's `run/cases.py`, `seeds.py`, `driver.py`, `checks.py`, `next_order_values.json`, `pin_manifest.py` and `record_environment.py`, carries the SHA-256 it has at MIT `d1c0ec8`. Only the census's code is new: `run/census_lib.py`, `run/census.py`, `run/write_guard.py` and `run/freeze_block.py`, with their tests. Their differences from M8.17's two code files are in `registration/`.
- **Its two arms.** Arm A reads twelve points on `N = 24`, 32 and 40, once the kernel at `N = 40` and six controls have passed, and locates any change of type the new readings bracket. Arm B runs M8.17's locator again on T4/R5's bracket, with a midpoint where K1 fails moved once.
- **Its admission.** OpenWave's [#512](https://github.com/openwave-labs/openwave/discussions/512#discussioncomment-19278753) admitted both remedies on 2026-10-29, and [fixed the first one's band](https://github.com/openwave-labs/openwave/discussions/512#discussioncomment-19296471) on 2026-10-30, inside the boundary of 2026-10-15.
- **Before the freeze.** It was built and tested with no solve at `N = 40`. One plumbing pass solved the GO-list control C2a at `N` = 12, 16 and 20, where the run never solves it, and a machine check solved the GO-list controls and C1 at `N` = 16, 24 and 32, since the OS moved after M8.17's run. `DEVLOG.md` records each step. It was frozen here before any sealed reading was computed.
- **The run.** The registered run began on 2026-10-31, after the maintainer's go and after the freeze block's pull request, [#688](https://github.com/openwave-labs/openwave/pull/688), opened, and it completed on 2026-11-01 with no stop. Arm B located T4/R5's change of type. Arm A ended at the control gate, where P5 and C3R/R4 at `ε = 0.25` read Unresolved, so none of the twelve was read. The maintainer adjudicated it on [#692](https://github.com/openwave-labs/openwave/pull/692#pullrequestreview-5730646319) (2026-11-01): it stands as recorded. `RECORD.md` gives all of it.
- **A correction (2026-11-01).** `RECORD.md` § 1 and the method note's §§ 3 and 8 say each of the 57 jobs was started once and completed. The run's log has 56 `started` events and 57 `completed`, since `gate` logs only its completion, as #692's approval notes. Nothing rests on it, and both files stay as the approval pins them.

The terms are `run/m8_16_task_details.md`, under the name the instrument's `devtools.frozen()` reads; `registration/m8_18_task_details.md` is the same text, with its diffs. The census page gives their SHA-256 and the manifest pin.

`SHA256SUMS` pins every file here. It was regenerated over the published folder at the record's commit, `5241a2d`, and again with the notes after the adjudication; the pre-run inventory is at MIT `4bd8bbd`. `run/MANIFEST_PIN` is the SHA-256 of the instrument's manifest, which `manifest` in `instrument/devtools.py` builds.
- **What it lists:** one line `sha256  path` per file under `instrument/` and `run/`, sorted by path.
- **What it leaves out:** `run/out/`, the pins, `run/FROZEN.json` and caches.
- **What it covers:** 37 files, the terms, `run/ENVIRONMENT.json` and the tests' outputs among them. The pin was written before the commit.
- **What it guards:** a sealed case runs only on a tree whose manifest equals the pin. At the freeze, `run/FROZEN.json` also pins every file under `reference/` at its SHA-256, and the driver checks them all before it runs.

## What is here

- **The record,** `RECORD.md`: the run's custody, Arm B's location, Arm A's gates, the twelve, the brackets and the row outcomes, built from the run's files by `tools/build_record.py`, with a diagnostic of the gate's failure in its § 4.
- **The terms,** `run/m8_16_task_details.md`, under the name the instrument's `devtools.frozen()` reads, as M8.16.1's terms placed theirs. `registration/` holds the same text, `m8_18_task_details.md`, with the diffs between its versions, and the code's diffs against M8.17's.
- **The instrument,** `instrument/`: M8.16.1's, byte for byte, as [M8.16.1's note](../soft-slot-dynamics-m8-16-1/REPRODUCE.md#what-is-here) lists it.
- **The run,** `run/`:
  - `driver.py`, with `cases.py`, `checks.py`, `seeds.py` and `next_order_values.json`: M8.16.1's, byte for byte;
  - `census_lib.py`: the points and ladders, the read's scope, the band, the reproduction rules, classifying a point, the brackets, the locator, the row outcomes and the record, with no solve;
  - `census.py`: the registered run, with solving and reading separate operations and the run cut into jobs;
  - `pin_manifest.py`, `write_guard.py`, `freeze_block.py` and `record_environment.py`: the freeze's steps and the environment record;
  - the tests, each with its output: `test_constants.py`, every number in the terms; `test_reader.py`, M8.17's readings reconstructed, the twelve refused, and the band; `test_gate.py`, the reproduction rules and the solve-state gate on data already on record, with a mutation of each compared field; `test_locator.py`, classification and the locator on synthetic records, each condition with its arm; `test_scope.py`, the gates and the read's scope through the run's whole order on stub solves, with a spy on the read and a mutation of each guard; and `test_freeze.py`, the guard's steps rehearsed on a temporary copy.
- **The run's files:**
  - `run/out/`: Arm B's record and stored solutions, each control's paths, stored solutions, reads, identities and case file, C1's file, the gate's record `GATE.json`, the census record `CENSUS.json`, the transcript `census.out`, the run's console output `census_console.log`, and its log `RUNLOG.json`, which records the SHA-256 of each completed job's files and of the record and the transcript;
  - `run/FROZEN.json` and `run/FROZEN_PIN`: the freeze, written once after the maintainer's go.
- **The launch,** `launch/`: the resume check every launch ran before `census.py`, `resume_check.py`, with its arms, `test_resume_check.py`, and their output; `prelaunch_checks.py`; and `test_launch_wrapper.py` with its output, the launch command's form run on stubs. They ran from the bench beside this folder, the check at `../resume_check/`, outside the pinned tree, and are published here byte for byte. The pre-launch checks and the wrapper test read files on the bench, such as `FILING_PLAN.md`, which are not published, so they rerun only beside them.
- **Post-run files,** made or placed after the run and not records from it: `prelaunch_checks_2026-10-31.txt`, the checks read just before the launch; `environment_postrun_2026-11-01.txt`, the environment read again after it; `launch/`; `run/out/census_console.log`, copied from beside this folder once the run had ended; `dev/runs/019_gate_cause/`, the diagnostic `RECORD.md` § 4 reads; and `tools/build_record.py`.
- **`reference/`:** files this run reads, copied byte for byte from this repository's history. They are M8.17's outputs on the five rows, its locator on T4/R5, its `CENSUS.json` and its two code files, and M8.16.1's controls. `SOURCES.json` names each one's commit, path, blob and SHA-256, and `tools/copy_from_mit.py` copies and checks them.
- **The development record:**
  - `DEVLOG.md`: every step, ruling and correction, in order, never edited;
  - `registration/`: the terms and the diffs;
  - `dev/`: the replay's scripts and the moved midpoint's values, the plumbing pass with its output, the machine check with its arm and their outputs, `gen_items.py`, which lists test 1's items from the terms, and `runs/`, the tests' kept runs and the post-run diagnostic.

## Before running

- **Verify the bytes:** `shasum -a 256 -c SHA256SUMS`, from this folder.
- **Verify the references:** `python3 -I -B tools/copy_from_mit.py MIT_REPO`, with `MIT_REPO` a full clone of this repository. It finds every copy present and equal to its blob, each with its pin, and writes nothing.
- **Verify the manifest.** From this folder, this prints the SHA-256 in `run/MANIFEST_PIN`:

  ```bash
  python3 -I -B -c "import sys; sys.path.insert(0, '.'); from instrument import devtools; print(devtools.manifest('.')[1])"
  ```
- **The environment.** `python3 -I -B run/record_environment.py --check` reads this machine's environment and lists every difference from `run/ENVIRONMENT.json`. It runs on macOS only, since it reads `sw_vers` and `sysctl`.
  - **The recorded machine:** macOS 15.8.2 (24H232) on one Apple M3.
  - **The software:** Python 3.13.13, NumPy 2.5.0 and SciPy 1.18.0, on Accelerate's BLAS and LAPACK with no threading variable set: M8.16.1's, unchanged. The OS is not: M8.16.1's and M8.17's records were made on macOS 15.8 (24H23), and the machine check below reproduces them on this one.
  - **Other machines:** bitwise agreement is not promised.
- **Run every script with `python3 -I -B`.** Never use `-O`, which removes the code's asserts: the run refuses it.
- **Run in a copy of this folder.** The tests write their outputs beside their scripts, most of them under `run/`. A write there outside `run/out/` that changes a byte changes the manifest, and the run then refuses every sealed case.

## The tests

From a copy of this folder, with nothing solved:
- `python3 -I -B run/test_constants.py run/m8_16_task_details.md`;
- `python3 -I -B run/test_reader.py`;
- `python3 -I -B run/test_gate.py`, in about 110 minutes;
- `python3 -I -B run/test_locator.py`;
- `python3 -I -B run/test_scope.py`;
- `python3 -I -B run/test_freeze.py`;
- `python3 -I -B launch/test_resume_check.py`, the resume check's arms, which rewrite `launch/test_resume_check.out`.

Each writes its output beside its script. On the recorded machine, in a copy of this folder, each output equals the one here, byte for byte. Tests 1 and 9 rehearse the freeze on temporary copies of their own, which leave out this folder's freeze files: the placed terms, the environment record, the pins and `FROZEN.json`. So they read the same before the freeze and after it, and they check that this folder's freeze files are as they were.

- **The plumbing pass:** `python3 -I -B dev/plumbing_census.py`, in 2 to 4 minutes. It solves the GO-list control C2a at cutoffs 12, 16 and 20, where the run never solves it, and writes `dev/plumbing_census.out`. Its output equals the one here apart from its timings and, on another machine, real parts below 10⁻¹⁴, which only move where a truncated line ends.
- **The machine check:** `python3 -I -B dev/os_reproduction.py N`, for `N` = 16, 24 and 32, and `python3 -I -B dev/os_reproduction.py C1`, in about an hour. NumPy and SciPy link Accelerate, which ships with the OS, and the reproduction gate compares every float exactly, so this run's OS had to reproduce records made on an earlier one. It solves the GO-list controls through the run's own path, read and comparison, and C1 through `run_c1`, against their records, and appends to `dev/os_reproduction.out`. On the recorded machine all 13 comparisons are exact. `python3 -I -B dev/os_reproduction_arm.py` moves one float of a record by one unit in the last place, and the comparison reports that leaf and no other.

## The freeze and the run

- **The freeze** was written once, after the maintainer's go: `python3 -I -B run/write_guard.py GO_LINK` wrote `run/FROZEN.json` and its pin, `run/FROZEN_PIN`, and `python3 -I -B run/freeze_block.py SOLVER_COMMIT OUT_MD` wrote the freeze block, filed on OpenWave as `research/m8_18/freeze_block.md` in [#688](https://github.com/openwave-labs/openwave/pull/688).
- **The registered run** ran once, by the launch command `RECORD.md` § 1 gives: it checks the resume check's SHA-256, runs the check, runs `run/record_environment.py --check`, and then `python3 -I -B -u run/census.py`, with its outputs in `run/out/`. `census.py` refuses to start until `run/FROZEN.json` and its pin validate.
  - To run it again, use a copy without `run/out/`, with `launch/` copied to `../resume_check/` beside it. In a copy that keeps `run/out/`, the resume check refuses, since the run has completed.
  - `python3 -I -B tools/build_record.py --check` rebuilds `RECORD.md` from the run's files, recomputes the gate and every row with `census_lib`, and reports any difference.

**Resources:** for the registered run on the recorded machine, the terms estimate about 55 to 70 hours of compute, with about 9 to 13 more for each new bracket in `R4`. It took 55569 s, about 15.4 hours, since the gate stopped Arm A before the targets (`RECORD.md`, § 1). Each stored solution is a few kilobytes.
