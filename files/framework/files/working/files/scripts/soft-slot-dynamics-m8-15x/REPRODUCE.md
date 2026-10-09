# M8.15.x solver: reproduction

The M8.15.x instrument is M8.15's solver, revised. M8.15's solver was frozen in `../soft-slot-dynamics/` at `6058f95`. The revision was qualified against it on 2026-10-09 and frozen here before any of its targets ran.

`SHA256SUMS` pins every file of the freeze. `m8_15x_solver/out/MANIFEST.json` is the frozen record. It holds:
- the SHA-256 of every instrument file, of the M8.15 files it reads, and of its static inputs;
- the environment;
- the solver it was derived from, and which files changed;
- the qualification's outcomes.

## What changed from M8.15's solver

- **`pinned.py`.**
  - The stopping test reads the full bordered residual, every multiplier included, evaluated from Newton's own residual.
  - A slice covector is projected into the space Newton solves in.
  - The gauges and slices take an optional reference point.
  - Two control cases are added, `P5` and `P5a`.
- **`angle.py` (new).** The angle solve on the lifted circle, and the carry along a branch, for slice cases.
- **`continuation.py` and `m815_controls.py`.** The gauge multipliers are recorded at every point.
- **`m815_branch.py`.**
  - A record is written on every end.
  - A crash record is written with its stage, traceback and frozen block.
  - There are test hooks, for controls only.
  - The gauge multipliers are recorded at every point.
- **`m815_common.py`.** A control case's frozen spectrum and dimension, and a quartet type in `predicted`.
- **`verdict.py`.** The classification is split into reusable steps, with no change in output.
- **`persistence.py`.** The summary records `N_obs`, `N_step` and `T_int`.

Every other instrument file is byte-identical to M8.15's, as `MANIFEST.json` records. `m815_freeze.py` is M8.15's, unchanged:
- its `orientations` step runs here;
- its `manifest` step expects M8.15's layout. This folder's manifest is written by `freeze_manifest.py`.

## Before running

- **Verify the bytes:** `shasum -a 256 -c SHA256SUMS`, from this folder.
  - `python3 freeze_manifest.py check` reruns the freeze's checks: the hashes, a clean import of the solver from its own folder, the static inputs against M8.15's, and both folders' `SHA256SUMS`.
- **The history.** Clone as M8.15's `REPRODUCE.md` describes. The third outside orbit's certified point is read from `d0de8ca` by M8.15's `m8_15_math/outside3_krein.py`.
- **The environment** is M8.15's, which `MANIFEST.json` records. The manifest was written only after the environment matched.
  - The scripts pin BLAS to one thread themselves.
  - The results are deterministic under that environment. Bit-for-bit agreement on other machines is not promised.
- **The static inputs** in `m8_15x_solver/out/` are M8.15's, byte for byte: `freeze_numbers.json`, `dt_L2.json` and `orientations.json`. The frozen values govern.
  - `theoremD_L3.json` is the qualification's Theorem D record, byte-identical to M8.15's.

## The runs

From `m8_15x_solver/`:

- **The closing controls,** as in M8.15: `python3 m815_controls.py linear 3`, then `linear 2`, `theoremD 3`, `spreads`, `dynamics C1`, `dynamics C2a`, `dynamics C2b`, `dynamics C3` and `rate`, then `summarize`.
  - `summarize` writes `out/freeze_numbers.json` over the frozen copy. Restore that copy afterwards, since the frozen values govern.
- **A control's full ladder:** `python3 m815_branch.py C3 4` or `C2a 4`.
- **The targets** (`python3 m815_branch.py T2 4` and the rest) refuse to run until `out/FROZEN.json` exists. It is written once the first target's terms are frozen on `main`, before any target runs.

**Resources:** as M8.15's. A level-3 phase peaks near 6.4 GB resident.
