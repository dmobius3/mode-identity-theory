# M8.16's harmonic Galerkin instrument: reproduction

This is the instrument for M8.16, the qualification that [the Slot Dynamics Census](../../slot-dynamics-census.md)'s step 4 asks for.
- **What it does.** It expands the sections of `E_ρ` in the twisted harmonics, keeping every level up to a cutoff, and computes the quartic exactly. It follows named branches by stationary continuation and records the linear spectrum where the terms read it.
- **Its admission.** OpenWave's [#512](https://github.com/openwave-labs/openwave/discussions/512#discussioncomment-18955679) admitted it for that use only.
- **Before the freeze.** It was built and tested on the GO list. Its dry run failed twice before it closed; the maintainer's review on [#637](https://github.com/openwave-labs/openwave/pull/637) then found three departures in the driver, since repaired, and the final dry run passed on the repaired tree. `DEVLOG.md` records each step. It was frozen here before any sealed case ran.

The terms are `run/m8_16_task_details.md`. The census page gives their SHA-256 and the manifest pin.

`SHA256SUMS` pins every file here. `run/MANIFEST_PIN` is the SHA-256 of the instrument's manifest, which `manifest` in `instrument/devtools.py` builds.
- **What it lists:** one line `sha256  path` per file under `instrument/`, `run/` and `reference/m815/`, sorted by path.
- **What it leaves out:** `run/dry/`, `run/out/`, the pins, `run/FROZEN.json` and caches.
- **What it covers:** the terms, `run/ENVIRONMENT.json` and the tests' outputs. The pin was written before the commit.
- **What it guards:** a sealed case runs only on a tree whose manifest equals the pin.

## What is here

- **The terms,** `run/m8_16_task_details.md`: the registration's text, built in `registration/` and confirmed by both review units.
- **The instrument,** `instrument/`:
  - `su2.py` and `group2i.py`: SU(2) with its spin representations, and 2I with its eight nontrivial slot representations;
  - `basis.py`: the complete-level twisted harmonic basis;
  - `quadrature.py` and `functional.py`: the exact product rule on S³, and the discrete functional with its symmetries;
  - `newton.py`: Newton at fixed norm, with optional slice borders;
  - `branches.py`: the seeds, the orbit checks and the continuation;
  - `certified.py`: the third outside orbit's certified point;
  - `linear.py` and `convergence.py`: the linear record and the separation rule;
  - `devtools.py`: the case guard, the manifest and the development log.
- **The run,** `run/`:
  - `driver.py`, with `cases.py` and `checks.py`: the registered run, its cases and its checks;
  - `pin_manifest.py`, `write_guard.py` and `record_environment.py`: the freeze's steps and the environment record;
  - `targets.json`, written by `name_targets.py`: M8.15's five target records, named by path, commit and blob id, and unopened until the go;
  - `DRY.json`, written by `build_dry.py`: the dry run's cases;
  - the tests, `test_guard.py`, `test_k3.py`, `test_claims.py` and `score_dry.py`, each with its output.
- **`reference/m815/`:** M8.15's branch records for the controls C2a/R4, C2b/R2 and C3/R4, which the driver reads.
- **The development record:**
  - `DEVLOG.md`: every development run, ruling and correction, in order, never edited. Each logged run's outputs are kept in `dev/runs/`, named by the entry's number, with their SHA-256 in the entry;
  - `BOUNDARY.md`: what development may run, fixed before any code, with its dated amendments;
  - `DESIGN.md`: the design. Its § 8 lists the development tests;
  - the plans: `DRIVER_PLAN.md`, `LADDER_PLAN.md`, `RECAL_PLAN.md`, `SEPARATION_PLAN.md` and `SLOWPAIR_PLAN.md`;
  - `EXPECTED_V0.md` and `EXPECTED_R5.md`: the controls' expected values, stated before they ran;
  - `dev/`: the development scripts and their outputs;
  - `registration/`: the terms' source and its builder, `fill_terms.py`.
- **Left out:** `run/dry/`, the dry run's output folder. It is byte-identical to its kept copies, `dev/runs/312_*`, the final dry run's.

## Before running

- **Verify the bytes:** `shasum -a 256 -c SHA256SUMS`, from this folder.
- **Verify the manifest.** From this folder, this prints the SHA-256 in `run/MANIFEST_PIN`:

  ```bash
  python3 -I -B -c "import sys; sys.path.insert(0, '.'); from instrument import devtools; print(devtools.manifest('.')[1])"
  ```
- **The environment.** `python3 -I -B run/record_environment.py --check` reads this machine's environment and lists every difference from `run/ENVIRONMENT.json`. It runs on macOS only, since it reads `sw_vers` and `sysctl`.
  - **The recorded machine:** macOS 15.8 (24H23) on one Apple M3.
  - **The software:** Python 3.13.13, NumPy 2.5.0 and SciPy 1.18.0, on Accelerate's BLAS and LAPACK with no threading variable set.
  - **Other machines:** bitwise agreement is not promised. The terms read every scored quantity against margins far above round-off (§ STATED LIMITS).
- **Run every script with `python3 -I -B`.** Never use `-O`, which removes the code's asserts: the driver refuses it, and the log refuses any run made under it.
- **Run in a copy of this folder.** The tests and the dry run log themselves in `DEVLOG.md`, and the tests write their outputs under `run/`. Any write under `run/` outside `run/dry/` and `run/out/`, a test's output included, changes the manifest, and the driver then refuses every sealed case.

## The runs

From a copy of this folder:

- **The guard's tests:** `python3 -I -B run/test_guard.py`. These are 84 tests on temporary trees, with nothing solved.
- **K3's tests:** `python3 -I -B run/test_k3.py MIT_REPO`, then again with `--synthetic-only`. `MIT_REPO` is a clone of this repository, from which the test reads three of M8.15's functions at `2c27cea`.
- **The dry run's claims:**
  - `python3 -I -B run/test_claims.py`, on entry 218's kept outputs;
  - `python3 -I -B run/score_dry.py`, on entry 245's.

  Each test writes its output under `run/` and logs itself in `DEVLOG.md`, keeping a copy in `dev/runs/`. On the recorded machine, in a copy of this folder, each output equals the one here, byte for byte. On another machine `test_k3.out`'s near-zero overlaps can differ in their last digits, with the same verdicts.
- **The dry run:** `python3 -I -B run/driver.py --dry`. It runs the GO cases of `run/DRY.json` and writes `run/dry/`. The final dry run, entry 312, took 124 minutes.
- **The registered run:** `python3 -I -B run/driver.py`, with its outputs in `run/out/`.
  - It refuses every sealed case until `run/FROZEN.json` and its pin, `run/FROZEN_PIN`, exist.
  - `write_guard.py MIT_REPO GO_LINK` writes them once, after the maintainer's go.
- **The development runs:** each DEVLOG entry names its script and its case.

**Resources:** the terms estimate about 13.6 to 17.3 hours of compute for the registered run on the recorded machine.
