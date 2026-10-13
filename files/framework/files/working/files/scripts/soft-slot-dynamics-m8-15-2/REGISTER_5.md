# M8.15.2: the locator's v2, its tests registered before code (registered 2026-10-13, v3)

**Status:** registered, v3. It folds both units' reviews of v1 and v2. Both gave GO on v2 after one fix, the wording of R5's old-guard arm, which is taken here with their two optional notes; no rule changes. It turns the scope memo v7, which both units confirmed on 2026-10-12, into the locator's changes and its registered tests. Decisions 3, 7, 8 and 9 have Blake's go. It is frozen before any locator code is written, and its SHA-256 is recorded at registration (UB), so RESULT_5 can check that the committed file is this one. A later change is a dated amendment; this text is not edited.

**How it got here.**
- **v2** folded both units' reviews of v1: M8.15.2's own write-once guard, with R5's negative control (UA, UB); the ceiling applied in adjudication, from the record (UB); rule 10's slack and its place first; which reason wins; A7(b)'s reason and arm; the tolerance's basis named, with the full-ladder figure disclosed; and the smaller specifications.
- **v3** folds their reviews of v2: R5's old-guard arm worded so that it bites (UA, UB), A23's line (UB), and § 5's amendment wording matched to § 2 (UB).

**Where the numbers come from.**
- Every expected outcome that depends on a bisection path on the coupled mock comes from `m8_15_2/plant_oracle.py`. It is a counts-level model of the memo's rules 1 to 7 and 10, decision 7 and rule 11, run on the plants' explicit eigenvectors. It reads no record and runs no locator code, and its output is `plant_oracle.out`.
- The continuity tolerance comes from `m8_15_2/recon_numbers.py` (v8), with the full-ladder disclosure in its v9 line.
- At the locator's freeze, as REGISTER_4 was, this registration is committed in the new folder, with a `scope/` folder holding the scope memo v7, `recon_numbers.py`, `plant_oracle.py` and `check_register_5.py` with their outputs. At commit, `recon_numbers.py`'s default path becomes relative to its own folder, `../../soft-slot-dynamics-m8-15x-target1` (UA), and its output is regenerated and compared byte for byte.

## 1. What is built

**A folder of its own,** `scripts/soft-slot-dynamics-m8-15-2/` on MIT main, beside M8.15.1's locator and the instrument.
- It starts from M8.15.1's locator, `soft-slot-dynamics-m8-15x-target1/` at `324fde3`: `locate.py`, `t1_branch.py`, `tests/mock.py`, `tests/synthetic.py` and `tests/real.py`, copied byte for byte. They change only as this registration says. The diff against `324fde3` is part of RESULT_5.
- It reads the instrument read-only at `97a8c08`, from `../soft-slot-dynamics-m8-15x/m8_15x_solver/`. No instrument file changes, and no file in M8.15.1's locator folder changes.

**`locate.py`, what changes.** Each item names the memo's rule it carries.

1. **`bisect`: the branch (rules 1 to 6).** For a sub-interval whose ends' `n(L)` differ:
   - **Four points are carried:** a lower and an upper `n(L)` end, and a lower and an upper clean end. At the start each pair is the sub-interval's two ends.
   - **Each midpoint** is reached from the current lower `n(L)` end, failing or clean, by the frozen secant, as the frozen `bisect` starts from `lo`.
   - **A failing midpoint** whose failed checks are the structural subspace, the slowest pair's overlap, or both, with a converged Newton solve, is passed.
     - Its `n(L)` replaces the `n(L)` end it equals. If it equals neither, the step is Unresolved (passed midpoint matches neither end).
     - A failure of the span's gate or of coverage, alone or with a passable check, ends the step as in M8.15.1: Unresolved, with its checks as the reason. A Newton failure ends it as in M8.15.1.
     - A passed midpoint keeps its failed checks in its record.
   - **A clean midpoint** whose `(n(L), n_S)` equals one side's clean end's becomes both that side's `n(L)` end and its clean end.
   - **An exchanged-lift point.** After a failure, a clean midpoint whose `n(L)` equals one side's and whose `n_S` is below that side's clean end's is passed on `n(L)` alone. It replaces that side's `n(L)` end, is never a clean end, and certifies no crossing. Its `n_S` is compared with that side's preserved clean end, never with a passed point that moved the `n(L)` end (UA).
   - **Any other clean midpoint after a failure** with neither side's counts makes the step Unresolved (neither side's counts after a failure), including one whose `n_S` is above its side's. Before any failure, M8.15.1's split applies.
   - **The stop:** the `n(L)` ends within `10⁻³` of the lower one, as now.
   - **A sub-interval whose ends share `n(L)`** keeps M8.15.1's terminal branch, unchanged.
2. **`analyse_step`: between the clean ends (rules 7 and 10, decision 7).** The step is analysed between its clean ends exactly as M8.15.1 analyses a final interval: the reading ends found outward from them, the crossing set by assignment, coverage, classes, bookkeeping, the rule against genuine and structural crossings in one step, and the root. Three things change.
   - **The clean window's limit,** checked first, on the clean ends, before the reading-end search (UB). A step whose clean ends lie more than one grid cell apart, beyond a relative `10⁻⁹`, is Unresolved (clean window over one grid cell). One grid cell is the bracket's width over 8. The slack absorbs rounding: on the mock a window exactly one cell wide computes one ulp over it (UB).
   - **A branch step** is a step whose reading interval holds a point that failed its checks, or an exchanged-lift point.
   - **In a branch step the classes are read first,** after the crossing set and coverage.
     - A crossing classed mixed is Unresolved (mixed overlap): the backstop, met before any identity test.
     - For the crossings classed genuine at both ends, two cosines are computed and recorded. One is the full one, as frozen. The other is the one outside `P`: each end's crossing vectors' components `M`-orthogonal to that end's own `P`, re-orthonormalized, then their principal cosines. Outside `P` below 0.9 is Unresolved (crossing identity), and so is a set outside `P` with fewer cosines than crossings, the frozen rank rule (UB).
     - The crossings classed structural keep the frozen check.
     - Outside a branch step, the frozen order and check stand.
3. **`continuity`: rule 11, a pass over each level's steps.** It runs after that level's scan and bisections end, and before any matching or guard. A step already Unresolved keeps its reason, and the pass records its comparisons beside it.
   - **The pool:** the bracket's evaluated points at that level at that moment, which are the guard region's ladder points, the grid points and every bisection midpoint. Every successful evaluation is kept as its own record, so the frozen pool's overwrite at an equal target hides none. The pool is ordered by reached `ε`.
   - **Duplicate targets:** two or more successful evaluations whose targets agree within `10⁻⁹`, relative. A step whose span, reading ends or predictors include one is Unresolved (solution continuity, duplicate target). The record says whether the records agree value for value (UB).
   - **The span:** the step's starting interval (the adjacent usable grid points between which its bisection began; the steps a split produces share it), widened to its reading ends where they lie outside. A step with no reading ends takes its starting interval. A point belongs to the span by its target `ε`; the pool is ordered by reached `ε` (UB).
   - **The comparisons:** each one tests a point's `m` against the straight line through the two pool points immediately below it in reached `ε`, a forward extrapolation.
     - **Along the span:** every pool point in the span except the lowest.
     - **Across the step:** the upper reading end, against the line through the lower reading end and the pool point immediately below that.
   - **The statistic:** the absolute miss over `h₂(h₁ + h₂)/2`, where `h₁` is the spacing of the two predictors and `h₂` the step to the compared point, both in reached `ε`.
   - **Degenerate comparisons:** fewer than two pool points below, or `h₁` or `h₂` not above `10⁻⁹` of the compared point's reached `ε`. The step is then Unresolved (solution continuity). No comparison is skipped.
   - **Which reason wins.** A step that meets a duplicate target and also a failing or degenerate comparison takes "solution continuity, duplicate target", with every comparison recorded (UB). A10 and A25 expect this.
   - **The tolerance,** `τ_c = 3.4601×10⁻³`, is ten times the largest statistic over each control bracket's pool, at both levels: `3.4601×10⁻⁴` (C3, level 3, at 12.485281; recon_numbers.py v8). Over the controls' full ladders, 0.25 to 72, the statistic reaches `4.1580×10⁻⁴` (C3, level 3, at 0.5; v9), disclosed; the basis stays the brackets' pools (UB). A comparison above it makes the step Unresolved (solution continuity). Only this multiple is scored. The record carries every statistic, so other multiples can be read from it as diagnostics.
   - **What it reads:** `m` and the reached `ε` of each stored record, the frozen point's `m` and `eps_reached`. It launches no solve, and the order of evaluation plays no part.
4. **The record (rule 9).** Each step adds:
   - its starting interval, `n(L)` ends, clean ends and span;
   - every failing midpoint and every exchanged-lift point, with its checks, counts and near-zero spectrum;
   - whether such a point lies inside the reading interval (the branch flag);
   - in a branch step, both identity cosines for every crossing classed genuine at both ends;
   - every continuity comparison: its three points, its two steps, the miss and the statistic;
   - every duplicate target, with both point records and whether they agree value for value (UB).
5. **The ceiling, applied in adjudication from the record** (UB). M8.15.1's terms apply the ceiling "in adjudication, from the record; the record's own names do not apply it", and so does M8.15.2.
   - `locate.py` records clause 3's trigger, item 4's branch flag per step and level, and keeps M8.15.1's frozen names.
   - The terms name a genuine step that is a branch step at either level, and whose readings locate a change of type, in these words: "A change of type is located between the registered guard readings. Its identification with the genuine index crossing at this step is not established: the crossing subspaces agree after removal of the structural directions, and the full spectral crossing identity remains unresolved. The step's classification crossed a structural-subspace or slowest-pair failure, or a point whose structural count fell below its side's, by a rule whose changed branch has synthetic controls only." The record's automatic name is reported beside it. Clauses 1 and 2 are unchanged.
   - For the tests, `tests/synthetic.py` gains one function that applies clauses 1 to 3 to a record in the terms' words. "Named with the qualifier" below means that function's name; the record keeps "a located change of type".
6. **The new reasons:** passed midpoint matches neither end; neither side's counts after a failure; clean window over one grid cell; solution continuity; solution continuity, duplicate target. Expectations compare whole reason strings, since "solution continuity" sits inside the last (UB).

Everything else in `locate.py` is unchanged: `structural_span`, `near_zero_L`, `classify`, `evaluate`, `reading_end`, the root rule, the guards, the extracted `decide` and the collision read.

**`t1_branch.py`, what changes.**
- **The registered brackets:** the primary brackets of T2/R4 and T3/R5 at both levels, as M8.15.1 registered them. The secondary is not run.
- **The ladder** runs to the largest registered region end: 32 for T2/R4, 22.63 for T3/R5.
- **M8.15.2's own guard** (UA, UB). The inherited guard admits a target only when the instrument's `m8_15x_solver/out/FROZEN.json` carries the terms' SHA-256. That file has been on main since `c4e2f7f`, carrying M8.15.1's terms hash `fc566c04…` and #624's go, so it would refuse M8.15.2's terms.
  - **The file:** `scripts/soft-slot-dynamics-m8-15-2/out/FROZEN.json`, written once at M8.15.2's freeze, after the maintainer's go, by a step that refuses if the file exists. The driver never writes it.
  - **It holds:** every value of the instrument's `freeze_numbers.json` unchanged; `frozen` true; M8.15.2's terms' SHA-256; the maintainer's go, a non-empty link; the SHA-256 of the instrument's `MANIFEST.json`, which must equal the pinned `2b9864ab…`; and the SHA-256 of the new folder's `locate.py` and `t1_branch.py`.
  - **The driver refuses a target** unless that file exists and every one of those values matches: the freeze values, the terms file given, the instrument's manifest as `check_instrument` computes it, and the running `locate.py` and `t1_branch.py`. Each refusal comes before any solve.
  - **It never reads the instrument's own `FROZEN.json`.** M8.15.1's guard, and the instrument's folder, stay exactly as M8.15.1 left them.

**`tests/synthetic.py` and `tests/real.py`, what changes** (UB). `tests/synthetic.py` gains the A plants, their arms and the ceiling function of item 5. `tests/real.py` points R5 at the new guard (§ 3) and adds rule 11's consistency read to R1 to R4.

**`tests/mock.py`, what changes.** REGISTER_4 § 2's mock stays the default for every S test. It gains:
- **The solution norm and the reached `ε`.** Every point carries `m` and a reached `ε`. By default the reached `ε` is the target, and `m = 1 + 0.15(ε − 1) + ½·3.4601×10⁻⁴·(ε − 1)²`, taken at the reached `ε`. So the statistic reads exactly `3.4601×10⁻⁴` at every comparison, a tenth of `τ_c` (DERIVED: a quadratic's linear-extrapolation miss is `½|m″|h₂(h₁ + h₂)` exactly).
- **The coupling.** The genuine pair (e4, e5) couples to two lifts (e2, e3) by `κ`, in two blocks `[[g, κ], [κ, −δ]]`, with `g = σa(r − ε)`, `a = 0.05`, `δ = 10⁻⁵` and the slope sign `σ = ±1`. e1 stays a lift at `−δ`, e0 the exact zero.
  - The crossing pair's Hamiltonian type change sits where each block is singular, `r + σκ²/(aδ)`. The pair is imaginary with Krein sign + on the side where the genuine index is 0, and real on the other.
  - `n(B|G_tol)` balances, as now, so every clean point balances and its reading ends are its clean ends.
- **Plant hooks:**
  - a lift line, the two lifts following `b(ε − ε_s)` (S2's);
  - tilt points, e0's eigenvector turned toward e6 to a set overlap at listed `ε` (S18b's fixture);
  - an extra genuine eigenvalue on e7, with its own type change; A4's glitch also sits on e7;
  - a glitch, an extra negative eigenvalue at one point;
  - a rotation of the genuine pair outside `P`, toward spectators other than e6 (A5 uses e8 and e9);
  - a span-gate or coverage failure at one point;
  - a second `m` path, `m + J`, over a target range;
  - reached-`ε` slack, alternating `±10⁻⁶`, relative, in evaluation order, with the counter per level and starting at `+10⁻⁶` (UB);
  - a re-evaluation of an evaluated target on a second path;
  - the guard region, seeding only that region's ladder points (UB: `mock.run` seeds all four today, and 0.6 would give A26's 0.8125 its second predecessor);
  - the genuine pair held at a constant value, for A2 and A28's lift line;
  - the A17 and A18 constructions (§ 2).

## 2. The synthetic tests, on the mock

### M8.15.1's tests, S1 to S18c

- **Each keeps its plant, expectation and arm,** except S10. Each also expects rule 11 to pass at every step on the default path.
- **S10, changed.**
  - Under M8.15.1, S10's step is Unresolved (structural subspace) over the bracket reached.
  - Under the new rule, the bisection passes the tilted midpoint at 1.025, a structural-subspace failure, and its `n(L)` replaces the upper `n(L)` end. The step is located as in S1, through the unchanged identity and bookkeeping checks.
  - The record shows the failing midpoint at 1.025, outside the clean window. So the step is not a branch step, clause 3 does not apply, and it is named "a located change of type".
  - **Its arm:** the tilt at 0.95. Then no failure is recorded, and the expectation fails.
- **A dry run** of the new code on the mock, unrecorded, may show that an S test's outcome changes. If so, that test's new expectation and its reason are registered as a dated amendment, which reaches both units before any recorded test runs, as REGISTER_4's amendments were. S18b is named: its failing points are grid points, which gave "no balanced reading end", and that must stay.
- **No S test has a lone failing grid point** (UB): S18b's two are consecutive, and S10's failing point is a midpoint. So the duplicate rule changes no S expectation.

### The plants

**A1: a genuine crossing through the mixing window,** the coupled mock at `κ/δ` of 0.3, 1, 2, 2.5, 3, 4 and 6, with both slope signs, at both levels (roots 1.0130 and 1.0181). The oracle registers each case:

| Slope sign, `κ/δ` | Level 3 | Level 2 | The bracket |
|---|---|---|---|
| +1, 0.3 | genuine, branch step | genuine | located, with the qualifier |
| +1, 1 | genuine, branch step | Unresolved (crossing identity), classes mixed | cross-level disagreement |
| +1, 2 | Unresolved (mixed overlap), branch step | genuine, branch step | cross-level disagreement |
| +1, 2.5 | genuine, branch step, an exchanged-lift point passed | genuine, branch step | located, with the qualifier |
| +1, 3 | genuine, branch step | genuine, branch step, an exchanged-lift point passed | located, with the qualifier |
| +1, 4 | genuine, branch step, an exchanged-lift point passed | genuine, branch step, two passed | located, with the qualifier |
| +1, 6 | genuine, branch step, two passed | Unresolved (structural subspace) and Unresolved (index bookkeeping), classes structural | cross-level disagreement |
| −1, 0.3 | genuine | genuine, branch step | located, with the qualifier |
| −1, 1 | genuine, branch step | genuine, branch step | located, with the qualifier |
| −1, 2 | genuine, branch step | Unresolved (mixed overlap), branch step | cross-level disagreement |
| −1, 2.5 | genuine, branch step | genuine, branch step (A15) | located, with the qualifier |
| −1, 3 | genuine, branch step, an exchanged-lift point passed | genuine, branch step, an exchanged-lift point passed | located, with the qualifier |
| −1, 4 | genuine, branch step, two passed | genuine, branch step, an exchanged-lift point passed | located, with the qualifier |
| −1, 6 | genuine, branch step, an exchanged-lift point passed | Unresolved (index bookkeeping), classes structural, and Unresolved (structural subspace) | cross-level disagreement |

- **Where located:** one genuine step per level, `Δn(L) = 2σ'` with `Δn_S = 0`, where `σ' = +1` for slope sign +1 and −1 for −1.
  - Each root lies within `3×10⁻⁴` of its plant's `r`, relative; the oracle's largest offset is `1.7×10⁻⁴`.
  - The shift `δ` lies within 0.2% of +0.50%.
  - Each side has a decided, counting reading: Elliptic below and Hyperbolic above for slope sign +1, the reverse for −1. The offsets are recorded, not registered.
  - The name is clause 3's.
- **Where not located,** each level's steps are as tabled, and the bracket is named "an index crossing located; the change of type remains unresolved" (cross-level disagreement).
- **Why some cases are not located (DERIVED in the model). Both causes fail closed.**
  - **Mixed overlap and crossing identity at `κ/δ` 1 or 2.** Both clean ends sit at the edges of the mixing window, where each crossing vector carries a lift admixture of up to 25.8°. The frozen assignment matches the character-preserving pair at `cos²Θ` against the cross pair at `sin²Θ`, where `Θ` is the two admixture angles' sum. So for `Θ` above 45° it pairs the genuine-like vector with the lift-like one. At the targets' M8.15.1 clean ends, the two-level angle is 15.8° to 36.5°.
  - **The split at `κ/δ = 6`, level 2.** The `n(L)` change, at `r₂ + 7.2×10⁻³`, passes the first midpoint, 1.025. That midpoint meets the clean interval before any failure, so the split applies.

**The other plants.** Plants without a stated root use S1's (1.0130, 1.0181). "Tilts" are e0's eigenvector turned to overlap 0.85 at the listed points; they fail the structural subspace check and leave `n_S` unchanged.

| Plant | What it plants | Expected |
|---|---|---|
| A2 | A structural crossing through the window: the lifts e2 and e3 rise through zero at 1.0130 as `0.05(ε − 1.0130)`, coupled by `κ` = 0.3δ, δ and 2δ to the genuine pair held at `+10⁻⁵`, at both levels | Structural at 0.3δ; Unresolved (crossing identity) at δ; Unresolved (mixed overlap) at 2δ. Never genuine |
| A3 | S1 at level 3 with e1 rising through zero at 1.0127 as `0.01(ε − 1.0127)`, tilts at 1.0140625 and 1.01328125; level 2 with e1's crossing only | Level 3: Unresolved (genuine and structural crossings in one step), a branch step. Level 2: a structural step at 1.0127 and a genuine step. The bracket: cross-level disagreement |
| A4 | S1 with S10's tilt at 1.025 and an extra negative eigenvalue there, `−10⁻³`, so the passed midpoint's `n(L)` is 6 | Unresolved (passed midpoint matches neither end) |
| A5 | A12's plant, with the genuine pair turned 30° toward spectators outside `P` from the root up | Unresolved (crossing identity): outside `P` and in full, `cos 30° = 0.866` |
| A6 | A27's plant: at level 3, the sub-interval 1.0 to 1.025 has ends `(3, 3)` and `(3, 1)`, sharing `n(L)`, and a failing midpoint at 1.0125 | M8.15.1's terminal branch: that sub-interval is Unresolved (structural subspace) |
| A7 | S1 at 1.025 with (a) the span's gate failing; (b) coverage failing at every `k_L`; (c) the span's gate failing with S10's tilt | Terminal: (a) and (c) Unresolved with the structural span among the reasons; (b) Unresolved with spectral coverage among the reasons, since a coverage failure brings the structural subspace failure with it (UB, DERIVED: the structural vectors are a subset of the near-zero ones) |
| A8 | S1 with the slowest pair's overlap at 0.95 at 1.025 | Passed: the step located as S10's new expectation, not a branch step |
| A9 | S1 with S10's tilt at 1.025, e0 falling through zero at 1.004 as `−0.01(ε − 1.004)`, and an extra genuine eigenvalue rising through zero at 1.006 | Unresolved (neither side's counts after a failure): the clean midpoint 1.0125 carries `(4, 4)`, the lower side's `n(L)` with `n_S` above it |
| A10 | S1 with a tilt at the grid point 1.0 | The bisection starts across 0.95 to 1.05, and its first midpoint re-evaluates 1.0. The clean window stays within a cell, so the step is Unresolved (solution continuity, duplicate target), its records at 1.0 agreeing value for value |
| A11 | A12's plant with (a) a genuine quartet at 1.0125; (b) `n(B\|G_tol)` one too high at 1.0125 | (a) A collision: "an index crossing located; the change of type remains unresolved". (b) Exempt from clause 2, with clause 3 firing: located with the qualifier, without clause 2's words |
| A12 | S1 with tilts at level 3 at 1.0125 and 1.01328125, so both `n(L)` ends are failing points; level 2 untilted | Level 3 classified between the clean ends 1.0 and 1.0140625: genuine, a branch step. Level 2 genuine. Located, with the qualifier |
| A13 | A12's plant: clause 3's trigger at level 3 only | The qualifier applies |
| A14 | The coupled mock with slope sign −1, `κ = 7.5δ`, roots 1.0120 and 1.0130: the `n(L)` change 1.11% below each root | Genuine at both levels, branch steps. The lower guards at `d = 0.01` lie between the `n(L)` change and the root and do not count. The lower reading comes from `d = 0.02`, Hyperbolic, and the upper is Elliptic. Located, with the qualifier |
| A15 | A1 at slope sign −1, `κ = 2.5δ`, level 2 | Genuine with the full cosine at 0.746 and the cosine outside `P` at 1.000: named with the qualifier, never with a positive identification |
| A16 | S1 with tilts at the grid points 0.95 and 1.0 and at the midpoints 0.975 and 1.0125 | Level 3: Unresolved (clean window over one grid cell), clean ends 0.9 and 1.013086. Level 2: genuine. The bracket: cross-level disagreement |
| A17 | The construction below, in A12's branch step | Unresolved (crossing identity): outside `P` 0.891, though the full cosine passes at 0.911 |
| A18 | The construction below, in A12's branch step | Unresolved (crossing identity), with the cosine outside `P` recorded below 0.9 |
| A19 | S1 with S10's tilt and the slowest pair at 0.95, both at 1.025 | Passed: as A8 |
| A20 | S1, targets above 1.0150 on a second path, `m + 10⁻⁶` | Unresolved (solution continuity): at 1.015625 the statistic reads 0.546, with that comparison recorded |
| A21 | S1 with a tilt at 1.0125, so the lower clean end stays 1.0, and targets above 1.0050 on a second path, `m + 10⁻⁵` | Unresolved (solution continuity): along the span at 1.0125 (0.0259) and 1.013281 (0.120), and across the step (0.0241), each recorded |
| A22 | A1 at slope sign +1, `κ = 2.5δ`, with the reached `ε` alternating by `±10⁻⁶`, relative | As A1: rule 11 passes, at most `3.46×10⁻⁴` |
| A23 | S3 with its structural crossing at 1.005, inside the genuine crossing's cell, so the bisection splits | Two steps per level, structural and genuine, located as S3; rule 11 passes through the registered comparisons |
| A24 | A23 with targets in (1.0025, 1.0058) on a second path, `m + 10⁻⁵`, around the structural step's sub-interval | Both steps Unresolved (solution continuity), at the switch's entry and exit |
| A25 | A10 with the re-evaluation at 1.0 on a second path, `m + 10⁻⁵` | Unresolved (solution continuity, duplicate target), its records at 1.0 differing by `10⁻⁵` |
| A26 | Guard region 0.8 to 1.4, roots 0.82 and 0.8241, a step in the first cell | Unresolved (solution continuity): the first compared point, 0.8125, has one point below it |
| A27 | The coupled mock at `κ = 8δ`, slope sign +1 | Level 3: Unresolved (structural subspace) on 1.0 to 1.025, failing at 1.0125; Unresolved (index bookkeeping) on 1.025781 to 1.026562, classes structural, `Δn(L) = Δn_S = +2`, `Δh = +2`. Level 2: Unresolved (structural subspace) on 1.0125 to 1.025; Unresolved (index bookkeeping) on 1.030469 to 1.03125, classes structural. "No genuine crossing detected" at both levels: the genuine crossing reads as a structural step that fails its bookkeeping (UB) |
| A28 | A2's plant at `κ` = 2.5δ, 3δ, 4δ and 6δ | Structural at each, branch steps with exchanged-lift points passed at 2.5δ, 4δ and 6δ. Never genuine |
| A29 | S1 with S10's tilt at 1.025, e1 rising through zero at 1.004 as `0.01(ε − 1.004)`, and an extra genuine eigenvalue falling through zero at 1.006 | Unresolved (genuine and structural crossings in one step), a branch step: the clean midpoint 1.0125, `(3, 2)`, is passed as an exchanged-lift point, and the classification between 1.0 and 1.013281 meets both crossings |

**A17's construction (DERIVED),** at level 3, in A12's branch step. At every point, the lift e1 is tilted out of `P` by `α`, with `cos α = 0.905`, toward `u(ε) = cos φ e8 + sin φ e9`. The genuine pair's first vector is `g(ε) = −sin α e1 + cos α u(ε)`, orthogonal to it. `φ` is 0 below the root and 27° from it up. Columns 1, 4, 8 and 9 carry the tilted lift, `g`, `w = −sin φ e8 + cos φ e9`, and e4 as a spectator, so the eigenvectors stay orthonormal (UB).
- The full cosine between the clean ends' `g` is `sin²α + cos²α cos 27° = 0.911`, so the frozen check passes.
- Outside `P` it is `cos 27° = 0.891`, so the comparison outside `P` fails.
- `g`'s overlap with `P` is `sin α = 0.425`, so it stays genuine.

**A18's construction (DERIVED).** As A17, with a second genuine doublet held negative at `−2×10⁻⁴` on e10 and e11.
- From the root up, the eigenvalues swap directions: the crossing doublet's first vector is e10, and the second doublet's first vector is the 27°-turned `g` (stated as a function of `ε`, since the upper clean end depends on the path; UB).
- The assignment pairs the lower end's crossing vector with the second doublet's, the wrong one, at a full cosine of 0.911.
- The comparison outside `P` reads 0.891 and stops it. The stop comes from A17's turn: with `φ = 0`, the same wrong pairing passes both checks, as UA's counterexample predicts, and clause 3's name carries that case (UB).

**The arms.** Every test has one; a green parent runs before each. Each arm moves what its expectation turns on:
- **A1:** three arms. Restoring M8.15.1's terminal branch must fail it. Restoring v4's tiered names must fail +1, 0.3, where the level-3 full cosine is 0.988. Treating an exchanged-lift point as a contradiction, as v6 did, must fail +1, 4 and −1, 4 (UB).
- **A2 and A28:** every crossing classed genuine.
- **A3:** the rule against genuine and structural crossings in one step removed.
- **A4:** no glitch, giving S10's outcome.
- **A5:** a turn of 20°, at cosine 0.940.
- **A6:** the terminal branch removed for ends that share `n(L)`.
- **A7:** the span's gate passable, for (a) and (c); coverage passable, for (b) (UB).
- **A8:** a slowest-pair failure made terminal.
- **A9:** a point whose `n_S` is above its side's also passed. The reason then changes to genuine and structural crossings in one step.
- **A10:** the latest evaluation kept at a duplicate target. Rule 11 then passes.
- **A11:** (a) no quartet; (b) clause 2 applied to the failing midpoint, in the ceiling function. M8.15.1's clause 2 already exempts a point inside a genuine step's reading interval, so A11(b) is met with the locator unchanged (UB).
- **A12:** the step classified between its `n(L)` ends instead of its clean ends.
- **A13:** the qualifier only when both levels trigger, in the ceiling function.
- **A14:** every decided guard counting.
- **A15, A17 and A18:** the comparison outside `P` dropped, leaving the full check alone.
- **A16:** rule 10 off.
- **A19:** a midpoint failing both passable checks made terminal.
- **A20:** the bare miss, against a tolerance that clears a grid cell (`τ_c × 0.05² = 8.65×10⁻⁶`). It passes the `10⁻⁶` jump (UB).
- **A21 and A24:** the continuity check dropped. A24 also takes the comparisons restricted to the step's final sub-interval, which pass both steps (UB).
- **A22:** the target `ε` as abscissa. The statistic then reads up to 1.00.
- **A23:** each point's predictors taken in evaluation order. Some comparison then has a non-positive step, which is degenerate (UA). The memo planned a curved path. The default path serves, since on a quadratic path the signed statistic equals `|m″|` for any three distinct points in any order (DERIVED, Lagrange's remainder), so evaluation order shows only through a step's sign, which the degenerate rule catches (UB).
- **A25:** the latest evaluation kept. The step then fails as a path switch, not a duplicate.
- **A26:** a degenerate comparison skipped. The step then passes.
- **A27:** the bookkeeping check removed. The second sub-step then reads structural.
- **A29:** an exchanged-lift point taken as a clean end. The step is then classified between 1.0125 and 1.013281: genuine (UA).

## 3. The real-solver controls

R1 to R5 and R4b rerun on the new locator, each with REGISTER_4's expectation and arm, except R5, which moves to M8.15.2's guard. "RESULT_4's runs" are the records in `soft-slot-dynamics-m8-15x-target1/out/` at `324fde3`. They also carry:
- **The new branch never fires.** The structural subspace check passed at every evaluated point of R1 and R2 (RESULT_4.md), and R3 stops at its forced Newton failure.
- **Rule 11 passes at every control step.** The statistic reads at most `2.6×10⁻⁶` on C2a's steps (recon_numbers.py v5), and C3 has no step. Its tolerance comes from these records, so this is a consistency check, not a test of the tolerance.
- **Each record reproduces RESULT_4's runs value for value,** outside the fields of § 4.
- **If the branch or rule 11 fires on a control,** that is a finding, and the qualification stops.

**R5, M8.15.2's guard** (UA, UB). It runs on a scratch copy of the new folder; no real guard file is written.
- **Refused, before any solve:** no guard file; a freeze value differing from `freeze_numbers.json`; a terms hash differing from the terms file's; an empty go; an instrument manifest hash differing; a `locate.py` or `t1_branch.py` hash differing.
- **M8.15.1's guard authorizes nothing** (UA): with the instrument's `FROZEN.json` present, as on main, and no M8.15.2 guard, the driver refuses; with M8.15.1's file copied to the new guard's path, it refuses on the terms hash and on the missing identifiers.
- **The pass case:** a complete, matching guard gets past the check, and the test stops before any solve.
- **The arms:**
  - the terms-hash check disabled, which must pass the third case;
  - the inherited guard restored: M8.15.1's entire `validate_guard` predicate, with its original file path and its four checks alone, without M8.15.2's identifier checks. With M8.15.1's terms and the instrument's existing `FROZEN.json`, that mutant must pass before any solve, while the registered guard refuses for want of its own file (UA, UB). Reading the old file alone would still refuse, on the missing identifiers, and would not bite: M8.15.1's file carries `solver_commit` and `locator_commit` but no manifest or locator hashes (UB).

## 4. Regression: the fields allowed to change

- **On every record:**
  - the fields of § 1 item 4;
  - the locator's SHA-256;
  - the start and finish times;
  - on targets, the terms' hash.
- **On the controls:** nothing else. Every other field reproduces RESULT_4's runs value for value.
- **On the targets:** up to each step's first failing midpoint, the new run evaluates M8.15.1's points in the same order, and they reproduce M8.15.1's point records value for value. The ladder reproduces M8.15's to 22.63 on T3/R5, and to 32 on T2/R4.

## 5. Qualification and freeze

1. **This registration,** frozen before code, after both units' GO and Blake's go.
2. **The code.** Plumbing dry runs are allowed on the mock and the controls only. They are unrecorded, and never run on a target. A dry run that shows a registered expectation is wrong is registered as a dated amendment, with its reason, which reaches both units before any recorded test runs (UB).
3. **The tests:** S1 to S18c, A1 to A29, and R1 to R5 with R4b, each with its arm, a green parent before each arm. Any failure stops the work. A fix is a dated amendment, and every test reruns.
4. **RESULT_5,** with the diff against `324fde3`, then the units.
5. **The terms,** a delta on M8.15.1's merged terms: the rule, its continuity check, clause 3, the brackets, the disclosure and this register. Everything else stays governed by M8.15.1's terms, pinned by their hash.
6. **The freeze:** the folder's manifest and `SHA256SUMS`, and the terms' hash on MIT main. Then the OpenWave filing (row M8.15.2) and the maintainer's go. Then the guard file is written once (§ 1), and the targets run.

## 6. What is not covered

- **No real-solver control exercises the new branch, the exchanged-lift pass or a path switch.** They are tested on the mock only, and clause 3 carries it.
- **The oracle is a counts-level model.** It gives the steps, classes, reasons, roots and continuity statistics. Guard readings are registered by type, not offset, except A14's lower guard.
- **The frozen assignment pairs across characters** once the clean ends' admixture angles sum past 45°. Such steps end Unresolved (A1 at `κ/δ` 1 and 2, and A2). That fails closed.
- **Very strong mixing ends Unresolved** when the first midpoint meets the clean interval before any failure, so the split applies (A27, and A1 at `κ/δ = 6` on level 2). That fails closed too.

*Draft v1, 2026-10-12, built from the scope memo v7 and both units' confirmation of it; v2 after both units' review of v1; v3 after their review of v2. Registered at 2026-10-13T02:17:12Z, before any locator code.*
