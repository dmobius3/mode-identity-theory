# M8.15.x solver: the qualification's record

This folder records how the M8.15.x instrument was scoped, tested and qualified before its freeze at `97a8c08`. The instrument is `../m8_15x_solver/`, and `../REPRODUCE.md` describes it.

## The documents, in order

- **`M8_15x_instrument_memo_v4.md`:** the scope memo, frozen for code on 2026-10-08. The registrations cite it as "the memo".
- **`SURVEY.md`:** the memo's § 2 survey. It is continuum mathematics on public spectra (`continuum_overlap_survey.py`, `survey_v1.out`).
- **`REGISTER_1.md` and `RESULT_1.md`:** controls 1a and 1b, the carry, and the kind of a root.
- **`REGISTER_2.md` and `RESULT_2.md`:** control 2a, the candidate cluster rule (`solver/m8_15_solver/cluster_rule.py`). It failed as registered, and the module was left out of the freeze.
- **`REGISTER_3.md` and `RESULT_3.md`:** the qualification run against M8.15's records.

Each register was written before the work it registers. Its amendments and notes are dated and appended at its foot; the registered text above them was not edited.

## The records

- **`qual_2026-10-09/`:** the qualification run.
  - `QUALIFICATION.json` holds every step's outcome.
  - `logs/` and `controls/` hold the runs.
  - `baseline/` holds M8.15's records that the run was compared against.
- **`solver/m8_15_solver/out/`:** the run's outputs. Among them are the branch records `branch_C2a_R4.json` and `branch_C3_R4.json`, which Target 1's locator reproduces (its test R4). `out_pre_qual_2026-10-09/` holds that folder as it stood before the run.
- **The controls' and checks' scripts, with their outputs,** as the documents cite them: `control_*`, `regress_*`, `diag_residual.*`, `freeze_arms.*`, `FREEZE_2026-10-09.log`, `arm4a.log` and `arm4b.log`.

## Reading the record

- **"A review unit"** in these documents is one of the two independent reviews. This copy of the memo relabels them Review A and Review B (see its top note).
  - `REGISTER_2.md` cites a reviewer's script, `ub_2a_review.py`, which is not carried here.
  - `verify_review_figures.py` reproduces, by an independent route, the reviewer's figures that `RESULT_2.md` cites.
- **Where the scripts ran.** They ran in a working folder laid out as this one, with the solver at `solver/m8_15_solver/`.
  - That solver, less `cluster_rule.py`, is `../m8_15x_solver/`, file for file and byte for byte.
  - A few scripts write out an absolute path to a working copy of this repository: `qual_run.py`, `control_1a.py`, `continuum_overlap_survey.py` and `verify_review_figures.py`. They are kept as they ran.
- **The review exchanges** themselves are not part of the record.
