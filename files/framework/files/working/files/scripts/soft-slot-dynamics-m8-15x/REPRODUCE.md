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

## Note (2026-10-11T05:13:14Z): the qualification's record, the guard file, and a defect in the fast-spectrum search

**The qualification's record** is now in `qualification/`, with a README. `SHA256SUMS` pins it with the rest of the folder. The instrument's files and `MANIFEST.json` are unchanged.

**The guard file.** `m8_15x_solver/out/FROZEN.json` is written once the first target's terms are frozen on `main`. Check 5a flags any file `SHA256SUMS` does not pin, so `freeze_manifest.py` now leaves that one file out of the sums and out of the check. Nothing else in the check changes.

**A defect in the fast-spectrum search** (`verdict.py`, `fast_search`), recorded and not repaired. M8.15's solver carries the same code.
- **What it is.** The search tries 82 shifts. At its two real ones, `1e-3` and `ω/40`, `shift_invert` builds a real factorization, and the search hands it to complex ARPACK. The operator is then exact on real vectors and wrong on complex ones: the solve casts its right-hand side to real, while the second block, `y1 + s z`, keeps `y1`'s imaginary part. So those two steps are not valid shift-invert steps. Python reports a `ComplexWarning` from `linearize.py` when they run.
- **What it does not touch:** the other 80 shifts; the slow spectrum, in real arithmetic; `n(L)`, a real symmetric solve; the closing controls' frequency check, which uses imaginary shifts.
- **What it can do.** Every eigenvalue the search keeps passes a backward-error test against the true matrices. That test does not prove the kept eigenvalues distinct and correctly classified, so the defect is not shown to act only by missing modes.
- **Where it has run.** No point of M8.15's run or of this instrument's qualification ran the search.
- **Why it is not repaired.** A repair would change the verdict both instruments share, and the repaired instrument would not be the one the qualification qualified. Target 1's locator records what the search did at every point.

## Note (2026-10-12T11:24:24Z): a correction, after the M8.15.1 run

**What the earlier note got wrong.** The note of 2026-10-11 above says that no point of M8.15's run or of this instrument's qualification ran the fast-spectrum search. One qualification point did: P5 in `qualification/regress_verdict_before.json`, at level 2 and `ε = 0.25`. It does not balance, and the search found 83 eigenvalues there with counts `[0, 0, 0]`, which left it unbalanced.

**Its standing.** The maintainer's approval of OpenWave #624 records the correction, and calls P5 "the refactor's regression gate, not a target or a control". No rule, threshold or verdict rests on the earlier statement. M8.15.1's target run did not run the search; its record is `../soft-slot-dynamics-m8-15x-target1/RECORD.md`.

**What this note changes.** It is a post-run documentation change. It rewrites this page and `SHA256SUMS`. The instrument's files, `MANIFEST.json` and the guard file are unchanged. The `SHA256SUMS` in force during the M8.15.1 run is the one at `ae3ad04`, and the run record gives its SHA-256.
