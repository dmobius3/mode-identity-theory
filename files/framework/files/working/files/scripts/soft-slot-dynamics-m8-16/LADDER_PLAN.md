# M8.16: D7's full-window ladders, a bounded plan (2026-10-16; the units' conditions folded)

UA holds D7's last bullet, "the ladders to their windows, against M8.15's control ladders", until a plan is reviewed: which points are compared, at which cutoffs, and the measured budget. This plan answers those three questions. UA gave a conditional GO and UB a GO with changes; both are folded below. Nothing here runs before Blake approves the base budget.

## Which points

M8.15's own control ladders, like for like (DESIGN.md §10.1): `ladder(0.25, ε_max)` in `soft-slot-dynamics/m8_15_solver/continuation.py`, called in `m815_branch.py` as `ladder(0.25, emax)`. That is ε_k = 0.25 · 2^(k/2), with ε_max appended:

| Control | ε_max (the gap) | Points |
| --- | --- | --- |
| C2a, R4 coherent | 72 | 18: 0.25, 0.354, 0.5, 0.707, 1, 1.41, 2, 2.83, 4, 5.66, 8, 11.3, 16, 22.6, 32, 45.3, 64, 72 |
| C3, R4 octahedron | 72 | the same 18 |
| C2b, R2 weight 7/2 | 132 | 20: the same through 64, then 90.5, 128, 132 |

- **Continuation.** Each ladder starts from the germ at ε = 0.25 and continues along the ladder from the previous accepted point, as in M8.15 and DESIGN.md §6. The sample's ε = 0.5, 1 and 2 are ladder points.
- **What is compared at each point,** against M8.15's control ladders (`soft-slot-dynamics/m8_15_solver/out/branch_C2a_R4.json`, `branch_C2b_R2.json` and `branch_C3_R4.json` on MIT main, as committed at `6058f95`), which the census holds unscored:
  - the type, where both are resolved, which is the comparison;
  - K, against M8.15's `nL` − `nB_cluster`;
  - the slow Krein signs;
  - each slow eigenvalue divided by its reached ε, against M8.15's level 3, reported beside M8.15's own level-2 to level-3 change, unscored.

  n(L) and n(D) are reported beside M8.15's `nL` and `nB_cluster`, unscored. They differ by M8.15's lifted structural modes (REGISTER_4 §5): by 2 each in C2a and C2b through ε = 32 and by none beyond, and by 3 each in C3 throughout. An Unresolved point stays Unresolved, and is never re-typed. (UB's text, verbatim. Checked against the records at main, which equal `6058f95`'s: the readings of `nL` and `nB_cluster` hold at every point, and at the sample points M8.16's slow eigenvalues at N = 40 sit inside M8.15's level-2 to level-3 change, DEVLOG 99.)
- **The expected V₀.** Every point carries its row of `EXPECTED_V0.md`. Its extension to larger ε is INFERRED: it rests on REGISTER_4 §5's statement that these controls keep their genuine index along their ladders. A mismatch at a point is reported, never re-expected.

## Which cutoffs (UB's option)

- **N = 24 and N = 32 at every ladder point.** Each point reports its slow eigenvalues' change from N = 24 to 32, each divided by its reached ε, against the provisional fraction 10⁻⁶.
- **N = 40 at each ladder's top three points** (C2a and C3: 45.3, 64, 72; C2b: 90.5, 128, 132), **and at every point where the 24 → 32 change exceeds 10⁻⁶.**
  - Each N = 40 point is seeded from the N = 32 accepted point at the same ε, embedded in the N = 40 basis. The basis at N = 32 is the leading block of the basis at N = 40, level by level, because the intertwiners are canonical, so the embedding is exact.
  - This reads "the previous accepted point" (§6) across N. Both units accepted it, with UA's guard (below).
- **Branch identity, at every N = 40 point (UA).** It records:
  - the embedding: the N = 32 point's residual in the N = 40 equations, relative to the size;
  - the symmetry-aligned distance: the N = 40 solution less the embedded N = 32 point, with the orbit tangents at the seed projected out, relative to the seed's norm;
  - both norms ‖c‖², and both frequencies ω = λ^(1/2).

  The identity is ambiguous, and the comparison is marked Unresolved, never treated as one branch, if:
  - the aligned distance exceeds 10⁻²; or
  - the type, (n(L), n(D), K), the slow Krein signs or V₀'s dimension and ranks differ from N = 32's.

  10⁻² is mine, proposed and flagged: at ε ≤ 2 the slow eigenvalues moved by 10⁻¹¹ from N = 32 to 40, and a different branch at the same ε and norm differs at order one.
- **A pause (UA, with UB's pause made unconditional).** The base plan runs first, on all three ladders: N = 24 and 32 at every point, and N = 40 at the top three. Then the run stops, and reports how many points exceed the fraction, with their estimated cost. No extra N = 40 point runs before Blake authorizes a bounded extension. UB's text paused only when more than three points of a ladder exceed it; UA's rule is stricter, and is taken.
- **Convergence** is then judged on the two highest N where each point ran, by §10.2's rule.

## The budget, from measured times

Per point, from the first sample (DEVLOG 69 to 77): about 7 to 13 Newton evaluations per point, plus the record. "Point" includes the record.

| Slot | N = 24 | N = 32 | N = 40 |
| --- | --- | --- | --- |
| R4 (C2a, C3) | about 0.5 min | about 4 to 5 min | 16 to 33 min (the timed point: 15.5 min) |
| R2 (C2b) | about 0.15 min | about 1.3 min | about 12.5 min, and its setup 16.5 min with einsum |

- **The ladders at N = 24 and 32:** C2a about 90 min, C3 about 95 min, C2b about 31 min. About 3.6 hours.
- **N = 40 at the top three points,** seeded from N = 32: C2a about 60 min, C3 about 75 min, C2b about 40 min. About 3 hours.
- **N = 40 wherever 24 → 32 exceeds the fraction:** about 20 to 30 minutes each. The count is not known in advance; at ε ≤ 2 it was none.
- **The base plan, about 6.6 hours.** The extra points run only on a separate decision (the pause above). The GEMM accumulation (DEVLOG 86) should shorten R2's setup and may trim each evaluation. The budget is not cut for it until measured.
- **Running.** The run goes in a visible Terminal-panel tab, so Blake can watch it live, under the app's keep-awake. Compute and wall time are reported separately (DEVLOG 78).

## What the plan does not do

- No pyramid, no census target, no persistence test, no scoring and no filing.
- The margin, the gray zone and the leak bound stay as set. Their recalibration is before the freeze, from these ladders' measured clusters and gaps (UB's §7 text). It is not tuned during the run.
- The §10.2 fraction stays provisional at 10⁻⁶. It is fixed after these ladders, where convergence is slowest (UB), and it is not a guarantee for near-zero crossing modes (UA).

## Note (2026-10-16), after the base run

Note (2026-10-16): the ladders ran as sidebar tasks, at Blake's request (DEVLOG 100), with C3 as a parallel task (DEVLOG 102).

- **The comparison** at each point is read at the highest N it ran (UB).
- **The Krein comparison, as run (UA).**
  - Against M8.15, the driver compares the count k_i⁻ with `ki_minus`, not each slow mode's sign.
  - Across N, the guard compares each imaginary group's negative-sign count.
  - The per-mode signs agree at every point by an analysis of the records (DEVLOG 107), not by the driver.
- **The guard's fail-safe (UA).**
  - As run, a failed identity was recorded, but the comparison kept its type and counted as agreement.
  - The driver now marks it Unresolved, with no cross-N change. Mutation arms on the trial show it (DEVLOG 108 to 111).
  - All nine guards of the base run passed, so none of its points is affected.
- **Convergence** is now judged by `DESIGN.md` v2.10's §10.2, by what could change the type. The 10⁻⁶ fraction stays as a reported diagnostic and is retired as a gate (UA, UB). This supersedes the last section's bullet on the fraction.
- **The pause ended without an extension.** Both units held the 15 further N = 40 points, and higher N (DEVLOG 107).
