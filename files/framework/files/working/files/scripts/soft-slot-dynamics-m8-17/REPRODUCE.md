# M8.17, the slot dynamics census run: reproduction

This is M8.17, the census run of [the Slot Dynamics Census](../../slot-dynamics-census.md)'s step 5, on the instrument M8.16.1 qualified.
- **What it runs.** M8.16.1's instrument and run code, byte for byte: each file under `instrument/`, and M8.16.1's `run/cases.py`, `seeds.py`, `driver.py`, `checks.py`, `next_order_values.json`, `pin_manifest.py` and `record_environment.py`, carries the SHA-256 it has at MIT `d1c0ec8`. Only the census's code is new: `run/census_lib.py`, `run/census.py`, `run/write_guard.py` and `run/freeze_block.py`, with their tests.
- **Its rows.** The nine rows M8.16.1 qualified, through their windows: 56 first-time readings, sealed until the freeze, and each change of type the classified points bracket, located on `n(L)`.
- **Its admission.** OpenWave's [#512](https://github.com/openwave-labs/openwave/discussions/512#discussioncomment-19071299) set the census run's conditions on 2026-10-20, inside the boundary of 2026-10-15.
- **Before the freeze.** It was built and tested with no solve on any sealed case. One plumbing pass solved the GO-list control C2a, at cutoffs the run never uses. `DEVLOG.md` records each step. It was frozen here before any sealed reading was computed.
- **The run.** The registered run began on 2026-10-27, after the maintainer's go and after the freeze block's pull request, [#673](https://github.com/openwave-labs/openwave/pull/673), merged. It completed on 2026-10-28 with no stop: four rows meet an S4 completion condition, and five end not settled by this run. `RECORD.md` gives every point, bracket and row outcome. Adjudication is the maintainers'.

The terms are `run/m8_16_task_details.md`, under the name the instrument's `devtools.frozen()` reads; `registration/m8_17_task_details.md` is the same text, with its diffs. The census page gives their SHA-256 and the manifest pin.

`SHA256SUMS` pins every file here. It was regenerated over the published folder at the record's commit, and the pre-run inventory is at MIT `338b873`. `run/MANIFEST_PIN` is the SHA-256 of the instrument's manifest, which `manifest` in `instrument/devtools.py` builds.
- **What it lists:** one line `sha256  path` per file under `instrument/` and `run/`, sorted by path.
- **What it leaves out:** `run/out/`, the pins, `run/FROZEN.json` and caches.
- **What it covers:** 35 files, the terms, `run/ENVIRONMENT.json` and the tests' outputs among them. The pin was written before the commit.
- **What it guards:** a sealed case runs only on a tree whose manifest equals the pin. At the freeze, `run/FROZEN.json` also pins every file under `reference/` at its SHA-256, and the driver checks them all before it runs.

## What is here

- **The record,** `RECORD.md`: the run's custody, the reproduction gate, every point's classification, the brackets and the row outcomes, built from the run's files by `tools/build_record.py`.
- **The terms,** `run/m8_16_task_details.md`, under the name the instrument's `devtools.frozen()` reads, as M8.16.1's terms placed theirs. `registration/` holds the same text, `m8_17_task_details.md`, with its diffs from v1 to the filed version.
- **The instrument,** `instrument/`: M8.16.1's, byte for byte, as [M8.16.1's note](../soft-slot-dynamics-m8-16-1/REPRODUCE.md#what-is-here) lists it.
- **The run,** `run/`:
  - `driver.py`, with `cases.py`, `checks.py`, `seeds.py` and `next_order_values.json`: M8.16.1's, byte for byte. The census solves and records each point with `driver.run_case` and `driver.read_point`, and reads it with `checks.k1` and `checks.reading`;
  - `census_lib.py`: the points, the three reproduction rules, classifying a point, the brackets, the locator, the row outcomes and the record, with no solve;
  - `census.py`: the registered run;
  - `pin_manifest.py`, `write_guard.py`, `freeze_block.py` and `record_environment.py`: the freeze's steps and the environment record;
  - the tests, each with its output: `test_constants.py`, every number in the terms; `test_reader.py`, M8.16.1's readings reconstructed and the sealed points refused; `test_gate.py`, the reproduction rules on data already on record, with a mutation of each compared field; `test_locator.py`, the locator and the classification on synthetic records, each condition with its arm; and `test_freeze.py`, the guard's steps rehearsed on a temporary copy.
- **The run's files:**
  - `run/out/`: each row's outputs, the locator's file for each bracket, the census record `CENSUS.json`, the transcript `census.out`, the run's console output `census_console.log`, and its log `RUNLOG.json`, which records the SHA-256 of each completed job's file and of the record and the transcript;
  - `run/FROZEN.json` and `run/FROZEN_PIN`: the freeze, written once after the maintainer's go.
- **The launch,** `launch/`: the resume check every launch ran before `census.py`, `resume_check.py`, with its arms, `test_resume_check.py`, and their output; `prelaunch_checks.py`; and `test_launch_wrapper.py` with its output, the launch command's form run on stubs. They ran from the bench beside this folder, the check at `../resume_check/`, outside the pinned tree, and are published here byte for byte. The wrapper test's first check reads the command from the bench's `FILING_PLAN.md`, which is not published, so it reruns only beside that plan.
- **Post-run files,** made or placed after the run and not records from it: `prelaunch_checks_2026-10-27.txt`, the checks read just before the launch; `environment_postrun_2026-10-28.txt`, the environment read again after it; `launch/`; `run/out/census_console.log`, copied from beside this folder once the run had ended; and `tools/build_record.py`.
- **`reference/`:** files this run reads, copied byte for byte from this repository's history. They are M8.16.1's outputs, its `FROZEN.json` and its filed terms; M8.15's adjudicated readings, as M8.16.1 copied them; M8.16's controls; amendment 5's ladder; and M8.15.2's T3/R5 record. `SOURCES.json` names each one's commit, path, blob and SHA-256, and `tools/copy_from_mit.py` copies and checks them.
- **The development record:**
  - `DEVLOG.md`: every step, ruling and correction, in order, never edited;
  - `registration/`: the terms and their diffs;
  - `dev/`: the recon memos, the grouping check, and the plumbing pass with its output.

## Before running

- **Verify the bytes:** `shasum -a 256 -c SHA256SUMS`, from this folder.
- **Verify the references:** `python3 -I -B tools/copy_from_mit.py MIT_REPO`, with `MIT_REPO` a full clone of this repository. It finds every copy present and equal to its blob, each with its pin, and writes nothing.
- **Verify the manifest.** From this folder, this prints the SHA-256 in `run/MANIFEST_PIN`:

  ```bash
  python3 -I -B -c "import sys; sys.path.insert(0, '.'); from instrument import devtools; print(devtools.manifest('.')[1])"
  ```
- **The environment.** `python3 -I -B run/record_environment.py --check` reads this machine's environment and lists every difference from `run/ENVIRONMENT.json`. It runs on macOS only, since it reads `sw_vers` and `sysctl`.
  - **The recorded machine:** macOS 15.8 (24H23) on one Apple M3.
  - **The software:** Python 3.13.13, NumPy 2.5.0 and SciPy 1.18.0, on Accelerate's BLAS and LAPACK with no threading variable set. This is M8.16.1's recorded environment, unchanged.
  - **Other machines:** bitwise agreement is not promised.
- **Run every script with `python3 -I -B`.** Never use `-O`, which removes the code's asserts: the run refuses it.
- **Run in a copy of this folder.** The tests write their outputs under `run/`. A write there outside `run/out/` that changes a byte changes the manifest, and the run then refuses every sealed case.

## The tests

From a copy of this folder, with nothing solved:
- `python3 -I -B run/test_constants.py run/m8_16_task_details.md`;
- `python3 -I -B run/test_reader.py`, in a copy without `run/FROZEN.json` and `run/FROZEN_PIN`: its claim 6 checks that the tree is not yet frozen;
- `python3 -I -B run/test_gate.py`, in about 10 minutes;
- `python3 -I -B run/test_locator.py`;
- `python3 -I -B run/test_freeze.py`;
- `python3 -I -B launch/test_resume_check.py`, the resume check's arms, which rewrite `launch/test_resume_check.out`.

Each writes its output beside its script. On the recorded machine, in a copy of this folder, each output equals the one here, byte for byte, test 2's in a copy without the freeze's two files. Tests 1 and 5 rehearse the freeze on temporary copies of their own, which leave out this folder's freeze files: the placed terms, the environment record, the pins and `FROZEN.json`. So they read the same before the freeze and after it, and they check that this folder's freeze files are as they were.

- **The plumbing pass:** `python3 -I -B dev/plumbing_census.py`, in about 5 minutes. It solves the GO-list control C2a at cutoffs 12, 16 and 20, which the run never uses, and writes `dev/plumbing_census.out`. Its output equals the one here apart from its timings and, on another machine, real parts below 10⁻¹⁴, which only move where a truncated line ends.

## The freeze and the run

- **The freeze** was written once, after the maintainer's go: `python3 -I -B run/write_guard.py GO_LINK` wrote `run/FROZEN.json` and its pin, `run/FROZEN_PIN`, and `python3 -I -B run/freeze_block.py SOLVER_COMMIT OUT_MD` wrote the freeze block, filed on OpenWave as `research/m8_17/freeze_block.md` in [#673](https://github.com/openwave-labs/openwave/pull/673).
- **The registered run** ran once, by the launch command `RECORD.md` § 1 gives: it checks the resume check's SHA-256, runs the check, and then `python3 -I -B -u run/census.py`, with its outputs in `run/out/`. `census.py` refuses to start until `run/FROZEN.json` and its pin validate.
  - To run it again, use a copy without `run/out/`, with `launch/` copied to `../resume_check/` beside it. In a copy that keeps `run/out/`, the resume check refuses, since the run has completed.
  - `python3 -I -B tools/build_record.py --check` rebuilds `RECORD.md` from the run's files, recomputes every row's record with `census_lib.assemble`, and reports any difference.

**Resources:** for the registered run on the recorded machine, the terms estimate about 15 to 16 hours of compute, with each further bracket adding about 2 to 6 hours in `R4`, about 2 in `R2` and about 4 to 9 in `R5`. It took 73635 s, about 20.5 hours, with two brackets (`RECORD.md`, § 1).
