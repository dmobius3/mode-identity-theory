# M8.15 solver: reproduction

The solver and the control records behind the M8.15 pre-registration, frozen on 2026-10-07 before any target was run.
`SHA256SUMS` pins every file in this folder. `m8_15_solver/out/MANIFEST.json` is the frozen record: the SHA-256 of
every file the run executes, the frozen numbers, and the environment the controls ran in.

## Before running

- **Clone with full history,** or at least back to `d0de8ca`. The third outside orbit's certified point is read with
  `git show d0de8ca:files/framework/files/working/files/scripts/soft-slot-branches/branches_check.py` from inside this
  repository, so a shallow clone or a source archive cannot find it. `m8_15_math/outside3_p.npy` is a pinned copy of
  that point for comparison, and `outside3_krein.py` prints whether the two agree.
- **Verify the bytes:** `shasum -a 256 -c SHA256SUMS`, from this folder.
- **The environment:** Python with numpy, scipy, sympy and mpmath. `MANIFEST.json` records the versions and builds the
  controls ran with. The scripts pin BLAS to one thread themselves. The results are deterministic under that
  environment; bit-for-bit agreement on other machines is not promised.

## The runs

From `m8_15_solver/`:

- **The closing controls:** `python3 m815_controls.py linear 3`, then `linear 2`, `theoremD 3`, `spreads`,
  `dynamics C1`, `dynamics C2a`, `dynamics C2b`, `dynamics C3` and `rate`, then `summarize`. They write to `out/`, and
  `summarize` writes `out/freeze_numbers.json`. `out/dt_L2.json` records each slot's level-2 `omega_max`, as
  `integrate.omega_max` computes it; each persistence test recomputes its step, `dt = 0.8 * 2 / omega_max`.
- **A control's full ladder** under the frozen rules, as rehearsed: `python3 m815_branch.py C2a 4`, `C2b 2` or `C3 4`.
- **The setup record and the manifest:** `python3 m815_freeze.py orientations`, then `python3 m815_freeze.py manifest`.
- **The targets** (`python3 m815_branch.py T1 4` and the rest) refuse to run until `out/FROZEN.json` exists. It is
  written after the maintainer's go on the pre-registration.

From `m8_15_math/`: `python3 outside3_krein.py` prints the third outside orbit's frozen frequencies and Krein signs, as
recorded in `outside3_krein.out`.

**Resources.** A level-3 phase peaks near 6.4 GB resident and takes about an hour per branch; a persistence test takes
about 1.5 hours. The fast-spectrum fallback takes about 3 hours per level-3 point, at any point that needs it.
