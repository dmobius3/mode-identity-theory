# M8.15 post-run diagnostics

These files sit outside the record. Nothing here changes a branch record or M8.15's outcome. They diagnose why T4's frozen continuation ended at the seed in both slots. Paths are relative to `m8_15_solver/`.

## The files

- **The exact replays** (`m815_replay_l3.py`, `replay_T4_R4.log`, `replay_T4_R5.log`). Each T4 level-3 continuation was rerun from the frozen modules with the same inputs, with only the continuation's log switched on. Both reproduce the run, with no ladder point and no accepted Newton solution. Both recover the end reason the driver's crash hid: `Newton failure at the seed`.
- **The post-hoc Newton trace** (`m815_posthoc_newton.py`, `posthoc_T4_R4.log`). This is the seed solve `Branch.first` makes, with the solver's verbose switch on. The residual falls from 1.65 to 1.08e-6 by iteration 3 and stays there through iteration 39, with σ fixed. The frozen tolerance is 1e-11.
- **The gauge-term check** (`t4_gauge.py` and the four `gauge_*.log` files). This is the same solve with the multipliers printed: at level 2 for T4/R4, T4/R5 and the slice control C3s/R4, and at level 3 for T4/R4. The check was declared in the bench log before it ran, and it reproduces an independent review's earlier level-2 bench check.

## The declaration, before the check ran (2026-10-08 14:06 UTC)

At level 2, the cause counts as reproduced if all six conditions hold:
1. T4's slice M-cosine with iΦ is 0.1256 to four digits;
2. the phase multiplier μ is nonzero (above 1e-8) and equals its phase-invariance prediction to 1e-6 relative;
3. the residual with every multiplier is at most 1e-11 at the fixed iterate;
4. the frozen stopping test is flat by iteration 3 and equals |μT|/|Mx| to 1e-3 relative;
5. the residual off the fixed space is at most 1e-11;
6. C3s's M-cosine is at most 1e-10 and its μ at most 1e-12, so its frozen test passes.

If all six hold, the check runs at level 3 on T4/R4 only, once. The expected outcome there:
- the multiplier-augmented Newton equation solved to round-off;
- a nonzero phase multiplier, kept because the frozen slice is not phase-orthogonal;
- only the frozen stopping test failing, at 1.08e-6 = |μT|/|Mx|;
- the residual off the fixed space at round-off.

Any material deviation is recorded, not reconciled.

**Outcome.** All six hold, and level 3 came out as expected. `t4_gauge.py` prints C3s's cosine as −0.000000, which cannot show 1e-10, so the cosine was computed separately at full precision: −5.5e-16. That computation uses the same formula (the script's lines 37 to 41) at the same scaled seed, printed with `%e`. At level 3, σ follows the post-hoc trace digit for digit. The trace's iteration-1 value is larger, 9.52e-6 against 2.684e-6, because it includes the frozen test's |c₀|/m norm term, which `t4_gauge.py` leaves out; the term vanishes from iteration 2.

## The diagnosis

A post-run diagnosis attributes the failure to the instrument's stopping test.

- **The equation is solved.** The frozen Newton solves T4's bordered equation to round-off. With every multiplier included, the residual is 3.5e-13 (R4, level 2), 3.8e-13 (R5, level 2) and 1.9e-12 (R4, level 3). The part outside the pinned fixed space is at the same level.
- **The stopping test leaves out the phase multiplier.** The test (`pinned.py` line 219) omits the phase multiplier's term. That term is nonzero because T4's slice overlaps the phase direction and the slice force is nonzero. The multiplier equals its phase-invariance prediction, −ν⟨iΦ, Ms⟩/⟨iΦ, T⟩, to the printed digits.
- **Where the test stalls.**
  - R4: at |μT|/|Mx| = 1.085e-6 at level 3 (M-cosine 0.1256).
  - R5: at 1.654e-5 at level 2 (M-cosine 0.1256); level 3 was not run.
- **The control.** The slice control C3s had neither condition: its M-cosine is −5.5e-16, μ is about 2e-15, and its test passes at 3.4e-13.
- **The terms.** Their premise that "the gauge multipliers vanish at a solution" (line 85) fails for this slice. Under line 44, a defect claim is reproduced by the maintainer with independent code before it is ratified.

## Running them

- **The replay and trace scripts** reach the solver through the `SOLVER` path set at their top. Set it to this folder's grandparent, `m8_15_solver/`.
- **`t4_gauge.py`** takes the solver folder as an argument, for example `NIT=8 python3 t4_gauge.py <m8_15_solver> 2 T4 4`.
- **The bytes as run:**
  - `m815_replay_l3.py` `69828db03993997e…`;
  - `m815_posthoc_newton.py` `c887d0c9c7337821…`;
  - `t4_gauge.py` `b7e9d11a3858fb30…`. The copy here, `92992b61413346e4…`, differs only in its first docstring line, where the author's label is removed.
