# M8.16.1, the harmonic Galerkin instrument's second and last qualification: reproduction

This is M8.16.1, the second and last qualification of M8.16's harmonic Galerkin instrument, which [the Slot Dynamics Census](../../slot-dynamics-census.md)'s step 4 admits after M8.16.
- **What it qualifies.** M8.16's instrument, byte for byte: each file under `instrument/` carries the SHA-256 it has in the manifest that [M8.16's](../soft-slot-dynamics-m8-16/REPRODUCE.md) pin covers. Only `run/` is new: the scoring, the cases, the guard and the tests. Its next-order bar reads the pyramid's quartet and Krein-positive pair, every predicted slow group of every row and of T5's second member, and the C3 ray's three groups, each against Proposition N's coefficient, frozen in `run/next_order_values.json`.
- **Its admission.** OpenWave's [#512](https://github.com/openwave-labs/openwave/discussions/512#discussioncomment-19071299) admitted it on 2026-10-20 as the instrument's last qualification, inside the boundary of 2026-10-15.
- **Before the freeze.** It was built and tested on the GO list. Amendment 5's ladder, `R5`'s coherent branch to `ε = 32`, failed two of its claims at the grid's top point, and the terms disclose both. `DEVLOG.md` records each step. It was frozen here before any sealed case ran.

The terms are `run/m8_16_task_details.md`. The census page gives their SHA-256 and the manifest pin.

`SHA256SUMS` pins every file here. `run/MANIFEST_PIN` is the SHA-256 of the instrument's manifest, which `manifest` in `instrument/devtools.py` builds.
- **What it lists:** one line `sha256  path` per file under `instrument/`, `run/` and `reference/m815/`, sorted by path.
- **What it leaves out:** `run/dry/`, `run/out/`, the pins, `run/FROZEN.json` and caches.
- **What it covers:** 48 files, the terms, `run/ENVIRONMENT.json`, the pinned values and the tests' outputs among them. The pin was written before the commit.
- **What it guards:** a sealed case runs only on a tree whose manifest equals the pin.

## What is here

- **The terms,** `run/m8_16_task_details.md`, under the name the instrument's `devtools.frozen()` reads: the registration's text, built in `registration/` and confirmed by both review units.
- **The instrument,** `instrument/`: M8.16's, byte for byte, as [M8.16's note](../soft-slot-dynamics-m8-16/REPRODUCE.md#what-is-here) lists it.
- **The run,** `run/`:
  - `driver.py`, with `cases.py`, `checks.py` and `seeds.py`: the registered run, its cases, its checks, and the two seeds M8.16.1 adds, the C3 ray and T5's second member;
  - `next_order_values.py`: the pinned next-order values, `next_order_values.json`, from the reduced quartic alone, with no solve on the instrument;
  - `pin_manifest.py`, `write_guard.py`, `freeze_block.py` and `record_environment.py`: the freeze's steps and the environment record;
  - `targets.json`, written by `name_targets.py`: M8.15's five target records, named by path, commit and blob id, and unopened until the go;
  - `DRY.json`, written by `build_dry.py`: the plumbing pass's cases, or, with `ladder`, amendment 5's;
  - the tests, each with its output: the guard's, `test_guard.py`; the three tests of the frozen text, `test_verdicts.py`, `test_constants.py` and `test_imports.py`; K3's, `test_k3.py`; the record regression, `score_record.py`; and the scorers of the plumbing pass and the ladder, `score_plumbing.py` and `score_ladder.py`.
- **`reference/m815/`:** M8.15's branch records for the controls C2a/R4, C2b/R2 and C3/R4, which the driver reads.
- **The development record:**
  - `DEVLOG.md`: every development run, ruling and correction, in order, never edited. Each run's script and outputs are kept in `dev/runs/`, and its entry names them with their SHA-256;
  - `BOUNDARY.md`: amendment 5, written once before the ladder ran. The split, with amendments 1 to 4, is M8.16's [`BOUNDARY.md`](../soft-slot-dynamics-m8-16/BOUNDARY.md);
  - the plans: `DRIVER_PLAN.md` and `LADDER_PLAN.md`;
  - `dev/`: the development scripts and their outputs;
  - `registration/`: the terms' template, `terms_template_v7.md`, and its builder, `build_terms_v7.py`, with the answer of 2026-10-15 as fetched and the built text; and T5's second member, `t5_second_member.md`, with its two checks.
- **Left out:** `run/dry/`, the development runs' output folder. Its plumbing pass is byte-identical to its kept copy, `dev/runs/008_plumbing/`. The ladder's outputs were moved to `dev/runs/015_ladder/` after its run.

## Before running

- **Verify the bytes:** `shasum -a 256 -c SHA256SUMS`, from this folder.
- **Verify the manifest.** From this folder, this prints the SHA-256 in `run/MANIFEST_PIN`:

  ```bash
  python3 -I -B -c "import sys; sys.path.insert(0, '.'); from instrument import devtools; print(devtools.manifest('.')[1])"
  ```
- **The environment.** `python3 -I -B run/record_environment.py --check` reads this machine's environment and lists every difference from `run/ENVIRONMENT.json`. It runs on macOS only, since it reads `sw_vers` and `sysctl`.
  - **The recorded machine:** macOS 15.8 (24H23) on one Apple M3.
  - **The software:** Python 3.13.13, NumPy 2.5.0 and SciPy 1.18.0, on Accelerate's BLAS and LAPACK with no threading variable set. This is M8.16's recorded environment, unchanged.
  - **Other machines:** bitwise agreement is not promised.
- **Run every script with `python3 -I -B`.** Never use `-O`, which removes the code's asserts: the driver refuses it.
- **Run in a copy of this folder.** The tests write their outputs under `run/`. A write there outside `run/dry/` and `run/out/` that changes a byte changes the manifest, and the driver then refuses every sealed case.

## The runs

From a copy of this folder. `MIT_REPO` is a full clone of this repository. The tests read M8.16's record from its history at `87fc643`, M8.16's terms at `deec830` and M8.15.x's functions at `2c27cea`; `next_order_values.py` reads the landed next-order check, `scripts/soft-slot-branches/`, from its working tree.

- **The guard's tests:** `python3 -I -B run/test_guard.py MIT_REPO`. These are 126 tests on temporary trees, with nothing solved.
- **The three tests of the frozen text:**
  - `python3 -I -B run/test_verdicts.py MIT_REPO`: every verdict path, 57 checks, on records built from M8.16's;
  - `python3 -I -B run/test_constants.py MIT_REPO run/m8_16_task_details.md`: every constant of both terms' FROZEN VALUES, against the code;
  - `python3 -I -B run/test_imports.py dev/seed_check.json`: every import, with the seed check's record.
- **K3's tests:** `python3 -I -B run/test_k3.py MIT_REPO`.
- **The record regression:** `python3 -I -B run/score_record.py MIT_REPO`. M8.16's recorded outputs are read by this task's checks, with no solve.
- **The development runs' scorers,** each on its run's kept outputs, copied into `run/dry/` first:
  - the plumbing pass: `mkdir -p run/dry && cp -R dev/runs/008_plumbing run/dry/plumbing`, then `python3 -I -B run/score_plumbing.py`;
  - amendment 5's ladder: `mkdir -p run/dry && cp dev/runs/015_ladder/* run/dry/`, then `python3 -I -B run/score_ladder.py MIT_REPO`. It exits 1: two of its five claims fail at `ε = 32`, as `DEVLOG.md` entry 24 records.
- **The plumbing pass's list:** `python3 -I -B run/build_dry.py` writes `run/DRY.json`.
- **The pinned values:** `python3 -I -B run/next_order_values.py MIT_REPO run/next_order_values.json > run/next_order_values.out`. On the recorded machine it takes about 6 to 10 minutes (`DEVLOG.md` entries 6 and 7).

Each script writes its output under `run/`. On the recorded machine, in a copy of this folder, each output equals the one here, byte for byte. On another machine `test_k3.out`'s near-zero overlaps can differ in their last digits, with the same verdicts.

- **The development runs:**
  - the plumbing pass, `python3 -I -B run/driver.py --dry --cutoffs 12 16 20`, runs the cases of `run/DRY.json` at cutoffs the registered run never uses and writes `run/dry/plumbing/`. Its kept run took 126 s;
  - the ladder: `python3 -I -B run/build_dry.py ladder` writes its list, `python3 -I -B run/driver.py --dry` runs it into `run/dry/`, and `python3 -I -B run/build_dry.py` restores the plumbing list. It took 1.85 h;
  - every other development run: each `DEVLOG.md` entry names its script, its case and its kept outputs.
- **The registered run:** `python3 -I -B run/driver.py`, with its outputs in `run/out/`.
  - It refuses every sealed case until `run/FROZEN.json` and its pin, `run/FROZEN_PIN`, exist.
  - `write_guard.py MIT_REPO GO_LINK` writes them once, after the maintainer's go. `freeze_block.py` then writes the freeze block.
- **The terms' build:** `python3 -I -B registration/build_terms_v7.py MIT_REPO registration/ruling_1015.json 5b7a56b85d733d53e257cf7559b1b69ac05276a2 . registration OUT`, from this folder, with `gh` signed in. `OUT` must not exist.
  - It fills `registration/terms_template_v7.md` from the files it names. It reads MIT's pages at `HEAD`, which it requires to be `origin/main`, and OpenWave's copy of M8.16's terms through `gh`.
  - The terms were built at `deec830`. In a scratch full clone, run `git checkout --detach deec830` and `git update-ref refs/remotes/origin/main deec830`, so that both are `deec830`. Then `OUT` equals `registration/m8_16_1_task_details.md`, byte for byte. At a later `main` the builder runs without error, but its text cites that commit and so differs.
  - The text, not the builder, is the artifact.

**Resources:** for the registered run on the recorded machine, the terms estimate 13.6 to 17.3 hours of compute with its rows, M8.16's estimate, plus about 0.5 hours for the C3 ray and 0.2 hours for T5's second member.
