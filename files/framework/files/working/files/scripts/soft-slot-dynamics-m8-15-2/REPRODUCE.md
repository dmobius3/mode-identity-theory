# M8.15.2's locator v2: reproduction

The locator v2 finds where `L`'s negative index changes on T2/R4 and T3/R5. Where a bisection meets a structural-subspace or slowest-pair failure, it bisects on `n(L)` and classifies the step between clean ends; every step passes a solution-continuity check; and the full verdict is read at guard offsets on each side of every genuine crossing. It reads the frozen M8.15.x instrument, `../soft-slot-dynamics-m8-15x/m8_15x_solver/` at `97a8c08`, and never changes it, and it leaves M8.15.1's locator, `../soft-slot-dynamics-m8-15x-target1/` at `324fde3`, unchanged. It was qualified on the tests below and frozen here before any target ran.

`SHA256SUMS` pins every file here. `MANIFEST.json` is the freeze's record. It holds:
- the SHA-256 of the locator's code, tests and checks, and of the frozen `decide` source it extracts;
- the base: M8.15.1's five files at `324fde3`, from which the code starts (`diff_324fde3.patch`);
- every file the instrument's manifest lists, with its SHA-256 recomputed here and equal to the manifest's, and the manifest's own SHA-256, which every run checks and the driver pins;
- the registration and the tests' outcomes, read from their records.

## What is here

- **`REGISTER_5.md`:** the registration, written before any locator code (2026-10-13T02:17:12Z). `REGISTER_5.sha256` holds the SHA-256 recorded at registration.
- **`RESULT_5.md`:** the tests' results, confirmed by both review units, with a dated note.
- **The code:**
  - `locate.py`: the grid, the bisection, the steps, the continuity check, the guards and the naming, with the evaluator over the frozen instrument;
  - `t1_branch.py`: the driver, with M8.15.2's own guard;
  - `write_guard.py`: the step that writes the guard once;
  - `adjudicate.py`: the adjudication reading, the tests' `ceiling` applied to a target's record;
  - `tests/`: the synthetic tests on a mock evaluator, and the real-solver controls.
- **`out/`:** the recorded qualification's records.
- **The checks, with their outputs:**
  - `tools/compare_s_records.py`: every S plant through M8.15.1's locator and this one;
  - `tools/check_result_5.py`: RESULT_5's quoted numbers against the records;
  - `adjudicate.py --check`, with `adjudicate_check.out`.
- **Custody:** `prerun_sha256.txt`, the code's SHA-256 at the recorded run's launch; `run_qualification.py`, the chain that ran the recorded qualification on the bench, with a `--from` resume option added during the run and not used; and `diff_324fde3.patch`.
- **`scope/`:** the scope memo v7; `recon_numbers.py` and `plant_oracle.py` with their outputs; `check_register_5.py` with its output; and `check_terms_numbers.py`, which checks the terms' numbers.

## Before running

- **Verify the bytes:** `shasum -a 256 -c SHA256SUMS`, from this folder.
- **The instrument and M8.15.1's locator** sit beside this folder, as on `main`. Every run checks the instrument's files against its manifest.
- **The environment** is the instrument's. The scripts pin BLAS to one thread themselves.

## The runs

From this folder. Each run writes into `out/`, so run in a copy to keep the records.

- **The synthetic tests:** `python3 tests/synthetic.py`.
- **The real-solver controls:**
  - `python3 tests/real.py r4b`, then `python3 tests/real.py r5 TERMS OLD_TERMS`. `TERMS` stands in for M8.15.2's terms (the recorded run used `REGISTER_5.md`), and `OLD_TERMS` is M8.15.1's (its filed text, SHA-256 `fc566c04…`);
  - `python3 tests/real.py run NAME` for `r3`, `r3arm`, `r1arm`, `c3` and `c2a`;
  - then `python3 tests/real.py evaluate QUALDIR`, with `QUALDIR` the qualification's branch records, `../soft-slot-dynamics-m8-15x/qualification/solver/m8_15_solver/out/`.

  The recorded run took these one at a time, through the chain, from 2026-10-13T03:08Z to 06:41Z.
- **The checks:**
  - `python3 tools/compare_s_records.py ..`;
  - `python3 tools/check_result_5.py RESULT_5.md . diff_324fde3.patch tools/compare_s_records.out --mutations`;
  - `python3 adjudicate.py --check`.
- **The scope:** from `scope/`, `python3 recon_numbers.py` and `python3 plant_oracle.py` reproduce their outputs, and `python3 check_register_5.py ../REGISTER_5.md plant_oracle.out recon_numbers.out` checks the registration's numbers.

**A target,** `python3 t1_branch.py T2 4 --terms PATH`, is refused until this folder's `out/FROZEN.json` exists, written once by `write_guard.py` after the maintainer's go. It must hold every value of the instrument's `out/freeze_numbers.json`, `frozen` true, the terms' SHA-256, the go, the instrument manifest's SHA-256 and the SHA-256 of `locate.py` and `t1_branch.py`. Before it is written, the run's pre-run check confirms this folder against `SHA256SUMS`.

**Adjudication:** `python3 adjudicate.py out/t1_T2_R4.json` prints each bracket's adjudicated names, with the record's own names beside them.

**Resources:** a level-3 phase peaks near 6.4 GB resident, so one branch runs at a time. The real-solver controls took about 3.5 hours in all.
