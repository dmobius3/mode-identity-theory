# M8.15.x Target 1's locator: reproduction

The locator finds where `L`'s negative index changes on T2/R4 and T3/R5, and reads the full verdict at guard offsets on each side of every genuine crossing. It reads the frozen M8.15.x instrument, `../soft-slot-dynamics-m8-15x/m8_15x_solver/` at `97a8c08`, and never changes it. It was qualified on the tests below and frozen here before any target ran.

`SHA256SUMS` pins every file here. `MANIFEST.json` is the freeze's record. It holds:
- the SHA-256 of the locator's code and tests, and of the frozen `decide` source the locator extracts;
- every file the instrument's manifest lists, with its SHA-256 recomputed here and equal to the manifest's, and the manifest's own SHA-256, which every run checks;
- the registration and the tests' outcomes, read from their records.

## What is here

- **`REGISTER_4.md`:** the locator's registration, written before any locator code (2026-10-09T21:58:26Z). Its amendments and notes are dated and appended at its foot.
- **`RESULT_4.md`:** the tests' results.
- **The code:**
  - `locate.py`: the grid, the bisection, the steps, the guards and the naming, with the evaluator over the frozen instrument;
  - `t1_branch.py`: the driver, with the guard a target must pass;
  - `tests/`: the synthetic tests on a mock evaluator, and the real-solver controls.
- **`out/`:** the final run's records. `run1_2026-10-09/`, `run2_2026-10-10/` and `run3_2026-10-10/` hold the earlier runs, as `RESULT_4.md` describes.
- **The checks, with their outputs:**
  - `span_gate_continuum.py` and `span_rank_controls.py` give the span gate's registered values;
  - `compare_run3.py` and `record_frozen_check.py` check the final run's records.

## Before running

- **Verify the bytes:** `shasum -a 256 -c SHA256SUMS`, from this folder.
- **The instrument** sits beside this folder, as on `main`. Every run checks its files against its manifest.
- **The environment** is the instrument's. The scripts pin BLAS to one thread themselves.

## The runs

From this folder. Each run writes into `out/`, so run in a copy to keep the records.

- **The synthetic tests:** `python3 tests/synthetic.py`.
- **The real-solver controls:**
  - `python3 tests/real.py r4b`, then `python3 tests/real.py r5 TERMS`, with `TERMS` the terms' file;
  - `python3 tests/real.py run NAME` for `r3`, `r3arm`, `r1arm`, `c3` and `c2a`;
  - then `python3 tests/real.py evaluate QUALDIR`, with `QUALDIR` the qualification's branch records, `../soft-slot-dynamics-m8-15x/qualification/solver/m8_15_solver/out/`.
- **The record checks:** `python3 record_frozen_check.py` and `python3 compare_run3.py`.
- **The span checks** ran in a working folder, with the instrument's path written out. From here, that path is `../soft-slot-dynamics-m8-15x/m8_15x_solver/`.

**A target,** `python3 t1_branch.py T2 4 --terms PATH`, is refused until the instrument's `out/FROZEN.json` exists. It must hold every value of the instrument's `out/freeze_numbers.json`, the terms' SHA-256 and the go.

**Resources:** a level-3 phase peaks near 6.4 GB resident, so one branch runs at a time. The real-solver controls take about 3 to 5 hours in all.
