# M8.15.2: locating through the avoided crossing (scope memo v7, 2026-10-12)

The aim is one change to M8.15.1's locator and one added check. The change lets a bisection pass a point where the structural classification fails, so that the primary steps on T2/R4 and T3/R5 can reach the guards. The check stops a step whose points do not lie on one solution path. This is bench scope, not a target pre-registration. It is drafted against MIT `37c7eed`, where the M8.15.x folders are as they were at `a261c7a`, apart from the after-verdict records `b13e0f4` added beside the locator's record:
- the instrument, frozen at `97a8c08`;
- the locator, frozen at `324fde3`;
- M8.15.1's record at `c4e2f7f`, with its post-run correction at `a261c7a`, and its post-adjudication note and two dated post-run verifications at `b13e0f4`.

M8.15.1's terms were merged on OpenWave in `dcc63851`. Its record, OpenWave #625, was adjudicated on 2026-10-12, and the corrected method note merged at `99b2ca07`. No change of type is located. Both primaries read "no genuine crossing detected", each with an Unresolved step (structural subspace), and the secondary is not located. Nothing executable is drafted before both units' GO on this memo and your go.

**What changed from v6.** Both units confirmed v6. Designing A1's plant for REGISTER_5 then exposed a gap in rule 4. You chose to close it, and both units agreed, on conditions all taken here. This round reviews that change only.
- **The gap.** For strong mixing the two-level model predicts clean points between the mixing window and the `n(L)` change, where the coupled lifts sit above zero: `n(L)` equals one side's, and `n_S` is below that side's. v6's rule 4 made such a point, met after a failure, end the step Unresolved, against A1's registered expectation (§ 2, the model's fourth fact).
- **The fix** (rule 4). After a failure, a clean midpoint with one side's `n(L)` and an `n_S` below that side's is passed on `n(L)` alone. It is never a clean end, certifies no crossing, makes the step a branch step, and the qualifier names it. A clean midpoint whose `n_S` is above its side's stays Unresolved.
- **Plants A27 to A29, A1's range and A9 restated, and three new arms** (§ 4).
- **Disclosure** (ground rule 4). A rough two-level fit at the targets' failing midpoints prompted closing the gap rather than only registering it. The fix's ground is the two-level model alone.

Every number below is printed by `m8_15_2/recon_numbers.py` (v7), and its output is saved beside it. The numbers about the targets come from M8.15.1's two target records, and the continuity tolerance's basis from its two real-solver control records. The v3 section reads no record: it prints § 2's bounds and UA's counterexample. The v4 section prints the continuity numbers and the secondary's two paths. The v5 section prints rule 11's comparisons on M8.15.1's steps and decision 7's numbers from no record. The v6 section prints the tighter bound and the first-cell facts. The v7 section, last, prints the exchanged-lift threshold, a counts-level simulation of rules 1 to 6 on the coupled mock, and the targets' rough fit. Every line before it is unchanged: the output's first 72 lines are v6's output, SHA-256 `d0f56f09…`.

## The question

M8.15.1's records show the structural classification failing at points inside each primary step. The total inertia `n(L)`, and the counts at the clean points on either side, stay well defined. Read from the spectra, the failure is an avoided crossing (§ 1, INFERRED).

M8.15.2 asks whether the genuine index change can be located through it:
- bracketed by `n(L)`, which no mixing among eigenvectors can change;
- classified from clean points fixed in advance on each side;
- confirmed by the full verdict at the guard offsets.

This follow-up exists because M8.15.1's primary steps ended Unresolved. The mechanism it addresses was named in REGISTER_4 before any run. That naming is not a prediction of M8.15.1's outcome.

## Ground rules

M8.15.x's five ground rules (the instrument memo v4) carry over. Here is how each applies.

1. **Repairs: none.** The instrument at `97a8c08` is unchanged. Its fast-spectrum defect stays disclosed, and the ceiling's two clauses carry over (§ 3).
2. **Two new rules.** § 2's change and its continuity check (rule 11) are new rules, so they enter as rule 2 requires: frozen before any target runs, qualified on controls, never justified by target outcomes. The change's grounds:
   - **The mechanism,** registered before any recorded test or target ran. REGISTER_4's amendment of 2026-10-09T22:10:11Z says that near the root the crossing eigenvalue approaches the lifts' eigenvalues. A mode sharing their symmetry can mix with them, and the structural subspace and identity checks would then report Unresolved.
   - **A property of the count.** `n(L)` is the number of eigenvalues of `(L, M)` below `−tol_L`. It is a function of the eigenvalues alone, so no mixing among eigenvectors changes it (DERIVED).
   - **The mechanism reduced to two levels** (§ 2, DERIVED in the model), including its fourth fact, the exchanged-lift points, which ground rule 4's pass (v7).
   - **The bounds on the comparison outside `P`** (§ 2, DERIVED).
   - **The synthetic plants of § 4.**

   The continuity check's grounds are step 8 of M8.15.1's terms (§ THE LOCATOR), a standard fact about singular Jacobians, and its plants (§ 2, rule 11). Its tolerance comes from the controls' records.
3. **Controls.**
   - No real-solver control exercises the new branch (§ 4). The terms say so, and the ceiling carries it (§ 3).
   - No real-solver control switches paths either, so the continuity check's failing branch has synthetic controls only (§ 4).
   - Nothing runs on a target before the freeze.
4. **Disclosure.** The terms state:
   - every M8.15 and M8.15.1 record;
   - M8.15.1's method note, post-run correction, overnight log and `summarize_t1.py`;
   - the recon of 2026-10-12, whose findings are this memo's § 1 and § 5 together with the assessment that T5/R2 is not a usable control;
   - `recon_numbers.py` with its full output, committed with REGISTER_5 and pinned;
   - the independent review of the recon;
   - both units' reviews of M8.15.1's record and of every version of this memo, including UB's two-level reading and identity prediction, and UA's counterexample;
   - #625's thread, and in it:
     - the adjudication, review 5492753760, with its question on a pitchfork;
     - the approvals, reviews 5495195497 and 5495207564;
     - the method note's fix `c6ad6cc5`, merged at `99b2ca07`;
     - the reply, issuecomment-6128592936, with its bifurcation reading;
   - the after-verdict records: MIT `b13e0f4` (the post-adjudication note in `RECORD.md`, its two dated post-run verifications, and the § VI note in `soft-slot-branches.md`), and OpenWave #628, merged at `9bb7672b` after the approval, review 5496563777, with its two notes: level 2's primaries on one path by a cross-level test, and T2/R4's levels placing the change apart;
   - the unit review in which v4's three changes were proposed after #625, and both units' agreement to them;
   - the counts-level simulation and the rough two-level fit at the targets' failing midpoints (recon_numbers.py v7), and both units' agreement to close rule 4's gap, with their conditions.

   **What rests on the records:** the scope. They chose the question: the two primary steps, both run, and the secondary dropped. Nothing in § 2's rule rests on them. #625's finding prompted the continuity check, and its grounds do not rest on the records either: the terms foresaw the singular Jacobian, and the tolerance comes from the controls. The check's cost under this rule, disclosed: its statistic was also computed on the target records, and recon_numbers.py prints the values (its v4 and v5 sections), so its tolerance's multiple is set with them in view (decision 8). The rough fit at the targets' failing midpoints prompted closing rule 4's gap rather than only registering it; the fix's ground is the two-level model alone (UB).
5. **Regression.** The register lists the fields allowed to change. Everything else reproduces value for value:
   - the controls, against RESULT_4's runs;
   - the targets' points, against M8.15.1's records, up to each step's first failure.

   The driver runs the ladder to the largest registered region end. With the secondary dropped, T3/R5's ladder ends at 22.63, and its comparison with M8.15's ladder covers the points up to there.

## 1. What failed

| | Level 3: ends; failing midpoint | Level 2: ends; failing midpoint | `h` at the ends |
|---|---|---|---|
| T2/R4 | 16.258883, 16.310660; 16.284772 | 16.0, 16.828427; 16.414214 | 0 → 2 |
| T3/R5 | 15.780330, 15.798636; 15.789483 | 15.707107, 16.0; 15.853553 | 6 → 4 |

- **What the locator does.** In all four bisections both ends pass every check, and a midpoint fails the structural subspace check. The frozen locator ends the bisection there and records the step Unresolved, without analysing it (`locate.py`, `bisect`). REGISTER_4's S10 registered exactly this.
- **The clean ends read as a genuine doublet.** `Δh = ±2` with `Δn_S = 0`, and `n(B|G_tol) = 5` on both sides, at both levels.
- **One change of `n(L)` per step.** At every failing midpoint, `n(L)` equals one end's value: the lower end's on T2/R4, the upper end's on T3/R5.
- **The eigenvalue that changes `n(L)` is mostly structural at level 3.** Across the `n(L)` interval its overlap with `P` goes:
  - from 0.80 to 0.99 on T2/R4;
  - from 0.97 to 0.86 on T3/R5.

  At level 2 it goes from 0.82 to 0.99 on T2/R4, and from 0.95 to 0.49 on T3/R5. The crossing pair's interpolated zero lies outside the `n(L)` interval at level 3 on both targets and at level 2 on T2/R4. On T3/R5 at level 2 it lies inside (§ 5).
- **The reading (INFERRED from the near-zero spectra).** The genuine doublet crosses zero and meets the rotation doublet. The mesh has split that doublet off zero: at level 3's clean ends it sits between `−4.2×10⁻⁵` and `−1.8×10⁻⁴`, the largest next to a failure. The two share a symmetry, so they mix instead of crossing.
  - At the clean ends the genuine doublet's overlap with `P` is 0.13 to 0.40, and the rotation doublet's is 0.92 to 0.99. The 0.40 is at T3/R5's level-3 upper end, next to the failure.
  - At the failing midpoints both doublets sit between, at 0.49 to 0.87, so exactly `d` structural eigenvectors cannot be found.
  - At every common `ε` where both levels pass their checks, the rotation doublet's offset from zero is larger at level 2, by 4.3 to 17.3 times. On T3/R5 from 11.3137 to 14.8284, away from the crossing, the factor is 11.8 to 12.3. That is consistent with a zero mode split by the mesh (INFERRED); near the crossing, repulsion differs between the levels.
- **The frozen cluster count misreads too.** At T3/R5's failing midpoints `n(B|G_tol) = 1`, against 5 on both sides, so `h` reads 8 there.
- **The slowest pair's overlap with the rotations behaves differently on the two targets.**
  - On T3/R5 it peaks at the failing midpoints: 0.868 at level 3 and 0.892 at level 2, against 0.22 to 0.455 at the clean ends.
  - On T2/R4 it is below `10⁻¹¹` at the failing midpoints, against 0.655 to 0.832 at the clean ends.
- **Provenance.** REGISTER_4's amendment of 2026-10-09T22:10:11Z named this mechanism as the reason not to bisect below `10⁻³`. It bit above that width:
  - at level 3, at widths of 3.18×10⁻³ (T2/R4) and 1.16×10⁻³ (T3/R5) of the lower end;
  - at level 2, at the first midpoint (T2/R4) and the second (T3/R5).

## 2. What changes

**The mechanism, reduced to two levels (DERIVED in the model, for one component of the doublet).** The model has three ingredients:
- a lift at `−δ`, with `δ > 0`;
- the genuine pair's unmixed eigenvalue `g = s(ε − r)`;
- a coupling `κ` between them.

It gives four facts, which are the model's, not the targets':
- **Where `n(L)` changes.** `n(L)` changes where `det = −gδ − κ² = 0`, at `ε − r = −κ²/(sδ)`. That is `κ²/(|s|δ)` from the pair's zero `r`: above it when `s < 0`, below it when `s > 0`.
- **Which eigenvector carries the change.** The eigenvector whose eigenvalue crosses zero there is `(δ, κ)`, normalized, in (genuine, lift). Its lift fraction is `κ²/(κ² + δ²)`, so for `κ > δ` the eigenvalue that changes `n(L)` is mostly lift.
- **The identity angle.** The genuine-like eigenvector carries a lift admixture at an angle `θ`, with `sin θ` its overlap with `P`, and the admixture changes sign across the crossing. So the full crossing vectors at the two clean ends differ by `θ_lo + θ_hi`, while their components outside `P` agree. The two vectors lie on different spectral branches: the genuine character passes from one branch to the other.
- **Where the lifts sit above zero (v7).** The structural subspace check fails where the lift-like eigenvector's overlap with `P` falls below 0.9, which is where `|g + δ| < 1.580κ`. Above `κ/δ = 2.06` the `n(L)` change lies outside that window, and a clean interval separates the two. In it the coupled lifts' eigenvalues are positive, so `n(L)` equals one side's, and `n_S` is lower than that side's by the number of coupled lifts. These are the exchanged-lift points.

**The rule.**
1. **Where the branch applies:** a step whose ends' `n(L)` differ. A step whose ends share `n(L)` keeps M8.15.1's terminal branch.
2. **Which failures it passes (decision 1).** A midpoint passes when its failing checks are the structural subspace, the slowest pair's overlap, or both, and its Newton solve converged. A failure of the span's gate or of coverage stays terminal, as does a Newton failure. A passed midpoint's failed checks stay failed: the point is Unresolved as a point, and the branch takes only its `n(L)`.
   - **Why not the span's gate or coverage (DERIVED).** The span's gate is computed from `P` alone, which is built from the exact generators, so mixing among `L`'s eigenvectors cannot reach it. Coverage compares `P` with the span of the near-zero eigenvectors, and mixing between two of them leaves that span unchanged.
   - **Why these two:**
     - the branch takes only `n(L)` from a passed midpoint, and no mixing changes `n(L)`;
     - the slowest-pair check stays in force at the clean ends and at the guards, where it gates what is read;
     - the mechanism puts rotation content into the crossing pair, which can trip either check (INFERRED for the slowest pair, whose vectors are the Hamiltonian slow pair's). A branch that stopped at a slowest-pair failure would stop where the mixing is strongest.
   - **The check is no detector of the mechanism.** On the targets it never failed: at the failing midpoints it read below `10⁻¹¹` on T2/R4, and 0.868 and 0.892 on T3/R5 (disclosure). The grounds above do not rest on it.
   - **M8.15.x's ruling stands.** Before any target ran, M8.15.x's memo (its § 2) anticipated the crossing pair's overlap reaching 0.9 at bisection midpoints, and ruled such points Unresolved. They still are; the branch uses only their `n(L)`.
3. **A passed midpoint** replaces the end whose `n(L)` it shares, as that side's `n(L)` end. If its `n(L)` equals neither end's, the step is Unresolved.
4. **Each side keeps a clean end.** It is the last point the bisection evaluated on that side that passes every point check and carries that side's `(n(L), n_S)`.
   - A passing midpoint with one side's counts becomes both that side's `n(L)` end and its clean end.
   - **An exchanged-lift point (v7).** After a failure, a passing midpoint whose `n(L)` equals one side's and whose `n_S` is below that side's is passed on `n(L)` alone. It replaces that side's `n(L)` end, as a failing midpoint does (rule 3). It is never a clean end, certifies no crossing, and makes the step a branch step. Its ground is the model's fourth fact.
   - **On the coupled mock** (a counts-level simulation of rules 1 to 6; the mock's `a = 0.05`, `δ = 10⁻⁵`, `r = 1.0130`): v6's rule 4 classifies `κ/δ` 0.3, 1, 2 and 3 genuine-looking and leaves 2.5, 4, 6 and 8 Unresolved. With the fix, only 8 stays Unresolved, where the first midpoint meets the clean interval before any failure (A27).
   - After a failure, any other passing midpoint with neither side's counts makes the step Unresolved, including one whose `n_S` is above its side's. Before any failure, the existing split applies.
   - **What it leaves alone.** The classification between the clean ends, the continuity check and the guards are unchanged.
5. **Each midpoint is reached by continuation from the current lower `n(L)` end,** failing or clean, as the frozen `bisect` starts from `lo`.
6. **The bisection stops** when the `n(L)` ends are within `10⁻³` of the lower one, as now. A Newton failure still ends it.
7. **The step is analysed between the clean ends, unchanged except for decision 7:**
   - the balance search outward from each end (the existing reading ends);
   - the crossing set, by assignment;
   - identity, coverage, classes and bookkeeping;
   - the rule against genuine and structural crossings in one step.

   Any failure leaves the step Unresolved, with its reason.
8. **The root is unchanged:** each crossing eigenvalue's zero, interpolated between the reading ends (REGISTER_4's amendment of 2026-10-09T22:10:11Z). It is an estimate for placing the guards, not a certified zero. The guard counting rule and the cross-level check decide. The `n(L)` interval is reported beside the root, with the gap between them.
9. **The record adds, for each step:**
   - the `n(L)` interval;
   - the clean window;
   - every failing midpoint, with its checks, counts and near-zero spectrum, and every exchanged-lift point passed under rule 4, with its counts and near-zero spectrum;
   - whether a failing point lies inside the reading interval;
   - in a branch step, both identity cosines for every crossing classed genuine at both ends: the full one, and the one outside `P`;
   - the step's starting interval and span, and every continuity comparison (rule 11): its three points, its two steps, the miss and the statistic.
10. **The clean window's limit.** A step whose clean window spans more than one grid cell is Unresolved (clean window over one grid cell). One grid cell is the frozen grid's own resolution: the interval M8.15.1 bisects from when no grid point fails.
11. **Solution continuity (new in v4).** Every step at both levels, branch step or not, must pass the continuity check below. A step that fails it is Unresolved (solution continuity). A step already Unresolved keeps its reason, and the record adds rule 11's result beside it.

**A branch step** is a step whose reading interval holds a point that failed its checks, or an exchanged-lift point passed under rule 4. A lone failing grid point is re-evaluated as the bisection's first midpoint, so there a failing grid point and a failing midpoint coincide. With two consecutive failing grid points they need not, and the failing points govern. Under rule 11 a lone failing grid point and its re-evaluation are a duplicate target, so such a step is Unresolved (solution continuity), unless it already is.

**The identity check in a branch step (decision 7).**
- **Two comparisons.** In a branch step the classes are read first. For each crossing classed genuine at both ends, two cosines are computed and recorded:
  - the full one, as frozen;
  - the one outside `P`: the crossing vectors' components `M`-orthogonal to each end's own `P`, each re-orthonormalized.

  A crossing classed structural keeps the frozen check. Outside branch steps, the frozen order and check are unchanged.
- **The outcome: one name (v5).**
  - **The cosine outside `P` below 0.9:** Unresolved (crossing identity).
  - **The cosine outside `P` at least 0.9:** the step is classified genuine so that its guards run, as this registration provides. Its name says the identification is not established, whatever the full cosine (§ 3). Both cosines are recorded.
- **What the comparison outside `P` shows (DERIVED).**
  - **Its bound at a clean end.** The structural subspace check puts the structural eigenvectors' span within 25.8° of `P` (cosine 0.9). A genuine eigenvector is `M`-orthogonal to that span, so its overlap with `P` is at most 0.436. The projection keeps at least 0.9 of its norm, and a projected orthonormal pair's Gram eigenvalues are at least 0.81.
  - **Distinct directions stay apart.** Two `M`-orthogonal genuine vectors at one point span a plane whose projected Gram eigenvalues lie in [0.81, 1]. So by Wielandt's inequality they agree outside `P` to at most 0.105 (UB, in place of the looser 0.235).
  - **What it can pass.** The comparison can pass a full turn of up to 57.4° (full cosine 0.539), provided all of the turn beyond 25.8° lies inside `P`. Under the mechanism, that excess is the lift admixture.
- **What it cannot show: UA's counterexample (verified).** Take `L(g) = [[g, 1.1], [1.1, −1]]` with `P = span(e₂)`, and compare `g = −4.5` with `g = 3`.
  - Both ends pass the structural subspace check, at 0.961 and 0.969.
  - The genuine-like vectors agree outside `P` exactly (1.000), and in full at 0.862.
  - They lie on different spectral branches: the lower at `g = −4.5`, the upper at `g = 3`. The eigenvalue that changes `n(L)`, at `g = −1.21`, is 55% lift.

  So agreement outside `P` identifies the genuine direction, not the spectral branch that crosses zero. Two different genuine directions differ outside `P`; two spectral branches that exchange one genuine direction need not.
- **Why one name: the full cosine does not test branch identity either (UB, verified).** In UA's family, moving the ends away from the mixing raises the full cosine from 0.862 to 0.994 at `g = ±20` and 0.999 at `g = ±60`. The genuine-like vector still lies on the lower branch at one end and the upper at the other. So the full cosine measures distance from the mixing, not which spectral branch crosses.
  - The locator has no test of spectral-branch identity, so no branch step claims it.
  - Both targets sit in that position at level 3, where the eigenvalue that changes `n(L)` is mostly structural (§ 1).
- **v4's tiers, withdrawn.** They gave the positive form when the full cosine also reached 0.9. On the targets that would have favoured T2/R4 only because its clean ends sit further from the mixing.
- **UB's overlap gate, not adopted.** It grants the positive form only when the eigenvalue that changes `n(L)` has overlap with `P` at most 0.436 at both ends of the `n(L)` interval.
  - In the two-level model that holds for `κ/δ` at most 0.484, not for every `κ < δ`.
  - The `n(L)` interval's ends can be failing points, where the 0.436 bound does not hold.
  - On the records it would give both targets the weaker name too.
- **The frozen check's limit (UB).** In any step, M8.15.1's frozen identity check compares eigenvectors at the reading ends, so it cannot see a spectral-branch exchange whose mixing lies between them. Outside branch steps the frozen check and names are unchanged, and this limit is disclosed.
- **Dropped: the outermost points** (v2). Both units set it aside, because it widens the comparison and gives up the narrowing.
- **The rule-4 cost, disclosed.** The comparison outside `P` was prompted by UB's reading of the target records, which predicts that T3/R5 fails the full check at both levels (§ 5). Its grounds are the registered mechanism, the two-level model and the bounds above.

**The solution-continuity check (rule 11, decision 8).**
- **Why.** No registered check compares the solutions at a step's two ends. #625 found the secondary's steps joining two solution paths, and level 2's step passed every check. The crossing identity check compares eigenvectors, and near a bifurcation the two paths' critical modes are nearly parallel, so it cannot see a switch (#625).
- **When it runs.** At each level, after the bracket's scan and bisections have ended, and before any step is matched across levels or any guard is evaluated, so that a failure takes the step out of the matching. It reads stored point records only: it launches no solve, and the order in which the points were evaluated plays no part.
- **The pool.** The bracket's evaluated points at that level at that moment: the guard region's ladder points, the grid points and every bisection midpoint. Every successful evaluation is kept as its own record, so the frozen pool's overwrite at an equal target hides none. The pool is ordered by reached `ε`.
- **Duplicate targets fail closed (UA).** Two or more successful evaluations whose targets agree within `10⁻⁹`, relative, are a duplicate target. A step whose span, reading ends or predictors include one is Unresolved (solution continuity, duplicate target). No evaluation is chosen over another.
  - **Where one arises.** A lone failing grid point is re-evaluated as its bisection's first midpoint, which lies within 2.0×10⁻¹⁶ of it, relative, on the targets' brackets. So a step whose bisection starts across a lone failing grid point is Unresolved, unless it already is.
  - **On the targets.** M8.15.1's primaries have 0 failing grid points, and the regression reproduces their grid value for value.
- **A step's span.** The step's starting interval is the pair of adjacent usable grid points between which its bisection began: one grid cell, or two where the scan skipped a failing grid point. The steps a split produces share it. The span runs from the lower of the starting interval's lower end and the step's lower reading end, to the higher of its upper end and the upper reading end. A step with no reading ends takes its starting interval.
- **The comparisons.** Each is a forward extrapolation: a point's `m`, the norm in which the frozen continuation runs, with `ε` its output (`continuation.py`), against the straight line through the two pool points immediately below it.
  - **Along the span:** every pool point in the span except the lowest. Their predictors may lie below the span.
  - **Across the step:** the upper reading end, against the line through the lower reading end and the pool point immediately below that. In a branch step this spans the clean window, which can be a grid cell wide.
- **The statistic** is the miss over `h₂(h₁ + h₂)/2`, where `h₁` is the spacing of the two predictors and `h₂` the step to the compared point, both in reached `ε`.
  - Along one smooth path the miss is `|d²m/dε²| h₂(h₁ + h₂)/2` to leading order, so the statistic estimates the path's own curvature at any width (DERIVED).
  - The bare miss scales as `h₂(h₁ + h₂)`, the square of the step when the two steps are equal. A tolerance on it that cleared a grid cell would therefore be far looser at the bisection's last steps, while one tolerance on the statistic serves both.
- **Degenerate comparisons fail closed.** A comparison with fewer than two pool points below it, or with `h₁` or `h₂` not above `10⁻⁹` of `ε`, makes the step Unresolved (solution continuity). No comparison is skipped. On M8.15.1's records, 0 comparisons lack their two points, and 0 pairs of targets coincide.
  - **The first cell, by construction (UB).** Where a guard region starts at its bracket's lower end, that end is the pool's lowest point, so a step in the bracket's first cell has a compared point with one predecessor and is Unresolved.
  - T3/R5's guard region and primary bracket both start at 11.313708, so a step between there and 11.899495 would be Unresolved; M8.15.1 has 0 steps there. T2/R4's guard region starts at 11.313708, below its bracket's 16.
  - The mock's guard region extends below its bracket (`tests/mock.py`), so no existing test exercises the case, and A26 plants it.
- **Against the reached `ε`.** The frozen secant stops once the reached `ε` is within `10⁻⁶` of the target, relative (`continuation.py`), and each point's frozen data records the `ε` its solution reached. On C2a the statistic reads at most 2.9×10⁻⁶ against the reached `ε`. Against the target, the slack alone lifts it to 5.1×10⁻³ at level 3.
- **The tolerance** is 10 times the controls' largest statistic (decision 8). The basis comes from the controls' ladders: the real-solver controls' records (RESULT_4's runs), every point at both levels, each against the two before it. There the statistic reads at most 2.9×10⁻⁶ on C2a and 3.5×10⁻⁴ on C3. REGISTER_5 fixes the value before any target runs, and it never comes from the targets.
  - **Only the registered multiple is scored.** The record carries every comparison's statistic, so other multiples, such as 3 and 30, can be read from it as diagnostics. None can replace the scored one.
  - **Its floor is each branch's own curvature,** not an irreducible one, and the two controls' differ by two orders of magnitude. A branch more curved than the tolerance fails closed.
- **What it reads.** `m` and the reached `ε`, from the stored records. No other check reads its result.
- **Fail-closed.** It adds a reason for Unresolved and removes none, so it can stop a result but never rescue one.
- **Its grounds** (ground rule 2), none of them #625's records:
  - **Foreseen in the terms.** M8.15.1's terms (§ THE LOCATOR, step 8) expect Newton's bordered Jacobian to be nearly singular near the root of a crossing whose mode lies in the pinned fixed space, and allow that the secondary's single crossing may lie there. They register only the Newton failure this can cause.
  - **What a singular Jacobian allows.** Where it is singular the implicit function theorem fails, so the solutions need not form one path there, and a converged solve need not stay on the path it started from (DERIVED, a standard fact).
  - **Where the bisection goes, and the condition (UB).** M8.15.2's bisection closes in on the `n(L)` change, where `L` is singular to within `tol_L`, and it passes the points where M8.15.1's stopped. Step 8 ties the bordered Jacobian's near-singularity to a crossing whose mode lies in the pinned fixed space, and the terms expect the primaries' doubled crossings to lie outside it (INFERRED). So the check guards against a possibility, not an expected switch.
- **Prompted by #625** (ground rule 4).
- **Not certified.** It is an operational screen on one scalar, not a proof that a step's points lie on one branch.
  - **It is local to the step's span.** A step whose span lies wholly on another path, reached by a switch outside it, passes. At #625's level 2, every point from 28.485281 up to, but not including, the bracket's upper end at 32 lay on the second path.
  - **Where two paths meet they share `m`,** so a switch near that point changes the statistic little (DERIVED). On #625's records the first point of level 3's second path, 27.899495, reads 4.8×10⁻⁴, and level 2's grid switch at 28.485281 reads 1.7×10⁻³: both below a tolerance of 3.5×10⁻³ (disclosure).
- **On the targets (disclosure, not grounds).**
  - **#625's reading.** At every primary step of 0.026 or less, `m` lands within `4×10⁻⁷` of linear continuation from the two points before it, failing midpoints included. Those steps are all at level 3, since no level-2 primary step is that short. #628's approval found level 2 on one path by another test: the offset of its `m` from level 3's at the same `ε` is smooth through each failing midpoint. Across the secondary's switches it misses by `2.8×10⁻³` (level 3) and `1.9×10⁻²` (level 2). These are bare misses, which recon_numbers.py reproduces against the target `ε`.
  - **The statistic.** Over the primaries' recorded points it reads at most 3.8×10⁻⁴ (T2/R4) and 7.9×10⁻⁴ (T3/R5), 2.3 times the controls' largest. Across the switches it reads 8.4 (level 3) and 55.8 (level 2).
  - **Rule 11 on M8.15.1's steps.** Over the comparisons rule 11 makes, the primaries read at most 3.8×10⁻⁴ (T2/R4) and 7.5×10⁻⁴ (T3/R5), 2.2 times the controls' largest; the controls' steps read at most 2.6×10⁻⁶.
    - On #625's secondary, level 3's starting interval reads 8.7×10⁻³ at 27.972718 and 8.4 at 28.485281, and level 2's reads 55.8 at 32. Both switches stop at a multiple of 10.
    - Over the first step's split sub-interval alone it would read at most 2.4×10⁻³, and pass. That is why the span covers the whole starting interval (UB).
  - **The effect on the primaries.** On M8.15.1's records every multiple from 2.2 to 2.4×10⁴ gives one outcome: the primaries pass and both switches stop. So the target values in view do not select 10 (UB). Above 2.2 the check is expected not to change the primaries (INFERRED from M8.15.1's points, and from step 8's expectation that the doubled crossings lie outside the pinned fixed space).

**The bounds, fixed before any target.**
- **No point is evaluated to find a clean end.** Clean ends are points the bisection evaluated, and its midpoints are fixed. So a clean end lies between the adjacent usable grid points where the bisection started. That is one grid cell, or more where the frozen scan skipped a failing grid point. The wider window is registered behaviour, with its own controls (A10, A16). Its width is recorded, and rule 10 limits it to one grid cell.
- **Clean** means every point check passes, with that side's counts. The checks are the structural subspace, coverage, the span's gate and the slowest pair's overlap.
- **Inside the clean window only `n(L)` steers the bisection and the bookkeeping.** `n(B|G_tol)`, `n_S` and `h` are read at the clean ends.
- **Failing midpoints stay in the later reads.** Every failing midpoint stays in the collision read and in clause 2's read. Inside the reading interval, clause 2 exempts it, and clause 3 carries it.
- **The trigger's two windows agree.** The reading-end search stops at any point that fails its checks, so the stretch between a clean end and its reading end holds no failing point. It also stops at any point whose `(n(L), n_S)` differs, so no exchanged-lift point lies there either. So such a point lies inside the reading interval exactly when it lies inside the clean window (DERIVED from `reading_end`).
- **Not certified.** Like any interval here, the clean window is not certified free of further crossings whose net change is zero (M8.15.1's terms, The question). The `n(L)` bisection locates a change; it does not make the crossing unique.

**Why the root stays.**
- The change is confined to the branch, and the root rule is frozen behaviour.
- The matched offsets compare the two levels' roots. In the model the `n(L)` change sits `κ²/(|s|δ)` from the pair's zero, and the lift's coupling `κ` and split `δ` differ between the levels. That displacement would feed into the cross-level shift; the pair's own zero carries no such term.
- On the mesh the type change sits at the `n(L)` change: with `J` invertible, `JL` is singular exactly where `L` is (INFERRED for the real system). The counting rule keeps every counting guard outside it.
- § 5 gives the sizes on the targets as disclosure, not grounds.

**Parked.** The constrained index stays out. It is the inertia of `L` on the `M`-orthogonal complement of `P`, read from the bordered matrix `[[L, MP], [PᵀM, 0]]`. That matrix's inertia is the constrained inertia plus `(d, d, 0)` when `MP` has full rank (DERIVED, a standard identity). It counts at 0, where `n(L)` counts below `−tol_L`. It is the next step if M8.15.2 cannot classify the steps.

## 3. The ceiling

- **Clauses 1 and 2,** fast-spectrum dependence, carry over unchanged.
- **Clause 3, new.**
  - **The trigger.** A branch step at either level (§ 2): a point that failed its checks, or an exchanged-lift point passed under rule 4, lies inside the step's reading interval, or equivalently inside its clean window.
  - **The name in a branch step,** at either level, in words the terms fix: "A change of type is located between the registered guard readings. Its identification with the genuine index crossing at this step is not established: the crossing subspaces agree after removal of the structural directions, and the full spectral crossing identity remains unresolved. The step's classification crossed a structural-subspace or slowest-pair failure, or a point whose structural count fell below its side's, by a rule whose changed branch has synthetic controls only."
  - **v4's second form is withdrawn** (decision 7). It said the identification "is qualified" when the full cosine also reached 0.9, a test that does not measure spectral-branch identity (§ 2).
  - **Where it applies.** The words are required wherever the name is cited. The record's automatic name is reported beside it, as now.
- **Why a qualifier.** The readings come from the full verdict at the guard offsets, which the change does not touch. What rests on the new branch is the step's classification as genuine. On it rests the identification of the confirmed type change with this crossing.
- **The alternative** is a full downgrade to "an index crossing located; the change of type remains unresolved" (decision 3).
- **The continuity check adds no clause.** It can only make a step Unresolved (§ 2, rule 11).
- **Its limit travels with any located change of type (UA).** Wherever one is reported, the record and the terms state beside it that the continuity check does not certify which branch the step lies on, least of all where two branches share `m`.

## 4. Controls

**Synthetic, on M8.15.1's mock.** The mock gains a coupling `κ` between the genuine pair and two lifts, so the eigenvectors mix where the pair passes the lifts' level. No parameter is taken from a target. Where the plant has a type change, it sits at the `n(L)` change, where `L` is singular. For the real system this placement is INFERRED: with `J` invertible, `JL` is singular exactly where `L` is.

For the continuity check the mock also gains a solution norm `m` and a reached `ε` at every point. By default every point lies on one smooth path, with the reached `ε` equal to the target. A20, A21 and A24 add a second path, A22 the secant's slack, A23 an out-of-order bisection, A25 two records at one target, and A26 a guard region that starts at the bracket's lower end. Every other plant and every S test keeps the default. A1 at strong mixing, A9 and A27 to A29 exercise the exchanged-lift points.

| Plant | What it plants | Expected |
|---|---|---|
| A1 | A genuine crossing through the mixing window: `κ` from below `δ` to `6δ`, past the exchanged-lift threshold, both signs of the slope, and `κ` values where `θ_lo + θ_hi` passes 25.8°. The plant registers both zeros: the unmixed pair's at `r`, and the coupled matrix's where `n(L)` changes | Registered per `κ` from the plant: the `n(L)` change `κ²/(\|s\|δ)` from `r` on the model's side; the root within a registered tolerance of `r`; both cosines recorded, and the name that says the identification is not established at every `κ`, whether or not the full cosine reaches 0.9; clause 3 firing. Located where a counting guard exists on each side; otherwise "an index crossing located; the change of type remains unresolved", since the fixed offsets cannot always bracket the actual crossing |
| A2 | A structural crossing through the window, in the same regime: a lift crosses `−tol_L` while mixed with a genuine pair that does not cross | Structural or Unresolved, never genuine |
| A3 | A genuine and a structural crossing inside one window | Unresolved |
| A4 | A passed midpoint whose `n(L)` equals neither end's | Unresolved |
| A5 | The genuine pair's components outside `P` rotated between the clean ends until the identity cosines fall below 0.9 | Unresolved (crossing identity) |
| A6 | Ends with equal `n(L)` and differing `n_S`, with a failing midpoint | M8.15.1's terminal branch: Unresolved |
| A7 | A midpoint failing the span's gate or coverage, alone or together with a passable check | Terminal: Unresolved |
| A8 | A midpoint failing only the slowest pair's overlap | Passed, as in A1 |
| A9 | After a failure, a passing midpoint with one side's `n(L)` and an `n_S` above that side's (v7) | Unresolved |
| A10 | A failing grid point, so the bisection starts across two grid cells | Unresolved: (clean window over one grid cell) if the clean window spans both cells, and otherwise (solution continuity, duplicate target), since the bisection's first midpoint re-evaluates the failing grid point (v6) |
| A11 | A quartet at a failing midpoint inside the window; separately, an unbalanced failing midpoint there | A collision, unresolved; for the unbalanced point, exempt from clause 2, with clause 3 firing |
| A12 | Failures on both sides, so both `n(L)` ends are failing points | Classified between the clean ends |
| A13 | Clause 3's trigger at one level only | The qualifier applies |
| A14 | The `n(L)` change further from the interpolated zero than the smallest guard offset | The guards between them do not count; the reading comes from a larger offset, or there is none |
| A15 | UA's counterexample, embedded with the other structural directions and a doubled pair: both clean ends pass the structural subspace check, the comparison outside `P` passes, the full one fails, and the genuine-like vectors sit on different spectral branches | The name says the identification is not established |
| A16 | Enough failing grid points that the clean window spans more than one grid cell | Unresolved (clean window over one grid cell) |
| A17 | The components outside `P` turn past 25.8° while the components inside `P` align, so the full check passes | Unresolved (crossing identity) |
| A18 | Two genuine doublets near zero at one clean end, with the assignment pairing the wrong one | Unresolved (crossing identity), from the comparison outside `P` |
| A19 | A midpoint failing both passable checks at once | Passed, as in A1 |
| A20 | A path switch inside a step: from one bisection midpoint on, the points lie on a second path whose `m` departs from the first by more than the tolerance allows there, while every other check passes. The jump is sized so that a tolerance on the bare miss that clears a grid cell lets it through | Unresolved (solution continuity), with the failing comparison recorded at the planted point: its three points and its statistic as registered |
| A21 | A path switch inside a wide clean window: every midpoint on one side fails its checks, so the clean window spans the grid cell, and the switch lies between the clean ends | Unresolved (solution continuity), with the failing comparison recorded as registered |
| A22 | A1's plant, with `m` on one smooth path at the controls' largest curvature, and each reached `ε` offset from its target by up to the secant's `10⁻⁶`, relative, at offsets REGISTER_5 fixes | As A1: the continuity check passes |
| A23 | A split bisection that evaluates points out of `ε` order, on one smooth path curved enough that predictors taken in evaluation order miss by more than the tolerance | As A1: the continuity check passes, through the registered comparisons |
| A24 | After a split, a path switch inside the starting interval but outside the step's final sub-interval | Unresolved (solution continuity) |
| A25 | Two successful evaluations at one target, within `10⁻⁹`, on different solution paths, inside a step's span | Unresolved (solution continuity, duplicate target), with both records kept |
| A26 | A guard region that starts at the bracket's lower end, with a step in the bracket's first cell | Unresolved (solution continuity) |
| A27 | A1 at `κ = 8δ`, where the bisection's first midpoint meets the clean interval before any failure | No genuine step: the existing split applies, one half ends Unresolved in M8.15.1's terminal branch, and the other fails its bookkeeping |
| A28 | A2 in the strong regime, `κ` from `2.5δ` to `6δ`: a lift crosses `−tol_L` while mixed with a genuine pair that does not cross | Structural or Unresolved, never genuine |
| A29 | Cancelling changes: inside a genuine step, a structural eigenvalue rises through `−tol_L` while a second genuine eigenvalue falls through it, so a clean midpoint after a failure carries one side's `n(L)` and an `n_S` below it | Unresolved (genuine and structural crossings in one step), never genuine |

- **S10's expectation changes.**
  - Under M8.15.1, S10's step is Unresolved (structural subspace) over the bracket reached.
  - Under the new rule, the bisection passes the tilted midpoint at 1.025. The step is located as in S1, through the unchanged identity and bookkeeping checks.
  - The expectation includes the record field: a failing midpoint at 1.025, outside the clean window. So clause 3 does not apply, and S10's arm (the tilt at 0.95, which records no failure) is caught.
  - The register states the old expectation, the new one, and why.
- **Every other S test keeps its expectation,** unless a dry run of the new rule on the mock shows otherwise before the register freezes. The dry run also lists any S test with a lone failing grid point, which the duplicate rule makes Unresolved. S18b is named in that dry run: its failing points are grid points, which gave "no balanced reading end", and that must stay. Any test whose outcome changes is listed beside S10, with its reason.
- **The arms.** Every test has an arm that must be caught. Thirteen are named now:
  - one restores M8.15.1's terminal branch, and must fail A1;
  - one drops the comparison outside `P`, and must fail A17 and A18;
  - one restores v4's tiered names, giving the positive form where the full cosine also reaches 0.9, and must fail A1;
  - one drops the continuity check, and must fail A20, A21 and A24;
  - one reads the target `ε` in place of the reached one, and must fail A22;
  - one compares the bare miss, with a tolerance that clears a grid cell, and must fail A20 (UB);
  - one takes each point's predictors in evaluation order, and must fail A23 (UA);
  - one restricts the comparisons to the step's final sub-interval, and must fail A24 (UB);
  - one keeps the latest of two evaluations at one target, and must fail A25 (UA);
  - one skips a degenerate comparison, and must fail A26 (UB);
  - one treats an exchanged-lift point as a contradiction, as v6 did, and must fail A1 at strong mixing (UB);
  - one also passes a point whose `n_S` is above its side's, and must fail A9;
  - one takes an exchanged-lift point as a clean end, and must fail A29 (UA).

**Real, regression only.**
- The real-solver suite (R1 to R5) reruns on the new locator.
- The structural subspace check passed at every evaluated point of R1 and R2 (RESULT_4.md), and R3 stops at its forced Newton failure. So the new branch should never fire.
- Every record must reproduce RESULT_4's runs outside the listed fields. If the branch fires, that is a finding, and the qualification stops.
- The continuity check runs at every real control step. Its tolerance comes from these records, so their passing it is a consistency check, not a test of the tolerance.

**The limitation, as it is.**
- No real-solver control exercises the new branch:
  - no non-target control has a genuine crossing (REGISTER_4 § 5);
  - none failed the structural subspace check.
- No real-solver control switches paths, so the continuity check's failing branch has synthetic controls only.
- The targets are the branch's first real use. Clause 3 carries this.

## 5. The targets

- **T2/R4 and T3/R5, primary brackets only,** at both levels. M8.15.1's brackets, guard regions, guard offsets, matching and names all carry over, under the ceiling's three clauses.
- **The secondary is dropped** from T3/R5's registered brackets. Its steps lie on or across two solution paths near a likely bifurcation (#625): level 3's first step lies on the second path, and level 3's second step and level 2's step span switches between the paths.
  - **Two paths.** Above 27.313708 the run evaluated points on two solution paths. On the ladder's branch the index change lies between 27.313708 and 28.485281 at level 3, and between 27.313708 and 32 at level 2. No evaluated point of that branch falls inside either interval, so the run does not locate it (#625).
  - **The bifurcation reading (INFERRED).** At level 3, on the ladder's path, the critical eigenvalue's local slopes from 26.142136 to 29.656854 are +0.091 to +0.102, and it crosses zero near 27.82. On the second path it fits `−0.183(ε − 27.78)` over the 10 points the bisection evaluated between 27.313708 and 28.485281, with residuals at most `1.3×10⁻³`. The slope ratio, −1.8 to −2.0, is consistent with the −2 of a pitchfork normal form rather than the −1 of a transcritical one, and the two zeros nearly coincide. Which symmetry the second path breaks, and whether it bifurcates from T3/R5's branch, are open.
  - **Dropping it is still right.** Neither § 2's change nor the continuity check locates a change along one branch through a bifurcation; the check would only stop the secondary's steps. That needs a rule for staying on the ladder's branch through the bifurcation, which M8.15.2 does not attempt.
- **Both targets run.** A frozen rule that classifies one and not the other says something, and so does one that classifies both.
- **Regression on the targets.** Up to each step's first failing midpoint, the new run evaluates M8.15.1's points in the same order. They must reproduce M8.15.1's point records value for value.

**Stated before the run: disclosure, not grounds.**

| | T2/R4 | T3/R5 |
|---|---|---|
| The crossing pair's interpolated zero, level 3 / level 2 | 16.281034 / 16.345786 | 15.793527 / 15.829021 |
| Its gap between the levels | +0.40% | +0.22% |
| Where `n(L)` changes, level 3 | (16.284772, 16.310660] | (15.780330, 15.789483] |
| Where `n(L)` changes, level 2 | (16.414214, 16.828427] | (15.707107, 15.853553] |
| The gap between the levels' `n(L)` changes | +0.63% to +3.34% | −0.52% to +0.46% |
| The pair's slope, difference between the levels | 0.74% | 3.86% |
| The two-level identity angle, level 3 / level 2 | 15.8° (0.962) / 16.0° (0.961) | 36.5° (0.804) / 28.2° (0.881) |

- **UB's two-level reading.** Both targets fit `κ > δ`. The eigenvalue that changes `n(L)` is mostly structural at level 3 (§ 1). At level 3 the pair's zero lies outside the `n(L)` interval, on the side the model gives: below it on T2/R4, where `s < 0`, and above it on T3/R5, where `s > 0`.
- **The identity prediction.**
  - **The full check:** the model predicts T3/R5 failing it at both levels, while T2/R4 passes at 0.96.
  - **The model's assumption.** It takes all of a crossing vector's overlap with `P` as lift admixture that changes sign; any overlap intrinsic to the genuine mode makes the angles smaller.
  - **Under one name** (decision 7), the model predicts the comparison outside `P` passing on both targets, so both would carry the name that says the identification is not established. Under v4's tiers T2/R4 would have taken the positive form, only because its clean ends sit further from the mixing (UB).
- **The interpolated zeros assume** that the assignment pairs the genuine doublets, as their overlaps with `P` suggest. The records carry no eigenvectors.
- **The level-2 guards.**
  - On T2/R4, `n(L)` changes up to 2.95% above the interpolated zero. A level-2 guard between the two reads the other side's `h` and does not count. So the smallest offsets may give no reading there, and the reading may come from a larger offset. That fails closed.
  - On T3/R5, `n(L)` changes within 0.77% of the zero, inside the smallest offset.
- **The mock's limit.** In the mock, a 2% gap between the levels' roots (S13) defeated the matched readings at every offset.
- **The continuity check** is expected not to change the primaries under a multiple above 2.2 (§ 2, rule 11; decision 8).
- **The exchanged-lift points (disclosure, v7).** A rough two-level fit at each failing midpoint gives `κ/δ` of 2.25 (T2/R4, level 3), 3.08 (T2/R4, level 2), 2.31 (T3/R5, level 3) and 2.16 (T3/R5, level 2). On that fit, T2/R4 level 2's next midpoints meet a clean interval from 16.4608 to 16.5286, at 16.5178, where v6's rule 4 would have ended the step Unresolved; no other step meets one. The fit is rough, and it is not grounds.

## 6. Qualification and filing

1. **#625 is adjudicated** (2026-10-12). Nothing below starts before both units' GO on this memo and your go.
2. **REGISTER_5,** before any code: the plants, every expected outcome, S10's change, the arms, the continuity tolerance from the controls' records, and the regression field lists. `recon_numbers.py` and its output are committed with it, its default path made relative to the repository.
3. **The new locator** goes in its own folder. M8.15.1's folder at `324fde3` is untouched, and the instrument is read at `97a8c08`.
4. **The tests run:** the S tests, A1 to A29 and R1 to R5, each against its registered outcome, with every arm caught. Then RESULT_5, and the units.
5. **The terms** are a delta on M8.15.1's merged terms: § 2's rule and its continuity check, the ceiling's clause 3, the brackets, the disclosure and the register. Everything else stays governed by M8.15.1's terms, pinned by their hash.
6. **The freeze, as M8.15.1's:** the manifest, `SHA256SUMS`, and the terms' hash on MIT `main`. Then the OpenWave filing (row M8.15.2, ROADMAP_STANDARDS § 6) and the maintainer's go.

**Cost.** M8.15.1's two target runs took 6.5 hours: T2/R4 took 1.3, and T3/R5 took 5.1 with the secondary. The guards add full-verdict points and the secondary is dropped, so plan on one overnight run.

## 7. Decisions

1. **The rule:** bisect through a classification failure on `n(L)`, and classify between the clean ends (§ 2).
   - The branch passes structural-subspace and slowest-pair failures, as UB proposed. UA now concurs, and both units keep it.
   - Span-gate, coverage and Newton failures stay terminal.
   - The constrained index stays parked.
2. **The root:** unchanged, on UB's corrected ground (§ 2). Both units keep it.
3. **The ceiling's clause 3:** a qualifier (§ 3), in one form under decision 7. Both units keep the qualifier. The alternative is a full downgrade.
4. **The secondary:** dropped (§ 5), now on #625's reason: two solutions near a likely bifurcation. A unit proposed the new reason, and both agreed.
5. **Both primaries run** (§ 5). Both units keep it.
6. **The terms:** a delta on M8.15.1's (§ 6). Both units keep it.
7. **The identity check in a branch step: the comparison outside `P` required, and one name** (§ 2, § 3).
   - **v3's tiers** gave the positive form when the full cosine also reached 0.9. On UA's own family, UB showed that the full cosine reaches 0.994 and 0.999 while the genuine-like vector lies on different spectral branches at the two ends.
   - **UA withdrew the tiers** on that computation, and both units now keep one name.
   - **UB's overlap gate is not adopted,** and UB concedes its limits (§ 2).
   - On the records one name gives both targets the weaker name, so it rescues nothing.
8. **The continuity check** (§ 2, rule 11), new in v4 and specified in full in v5 and v6.
   - **Its details.** The normalized statistic and the reached `ε` were mine in v4, and both units keep them. The pool, the span and the comparisons follow both units' reviews. Degenerate comparisons and duplicate targets fail closed (UA), and the first cell's consequence is registered (UB).
   - **The multiple: 10,** which both units keep, as the only scored one. Its ground is a decade over the largest curvature a real control has shown. On M8.15.1's records every multiple from 2.2 to 2.4×10⁴ gives one outcome, so the target values in view do not select it (UB). Other multiples can be read from the record as diagnostics only.
   - **UB's optional relative statistic is not adopted:** the units agreed that the scale comes from the controls.

9. **The exchanged-lift pass** (§ 2, rule 4), new in v7. You chose to close the gap, and both units agreed on conditions, all taken:
   - its ground is the two-level model alone, and the rough fit is disclosed as what prompted it (UB);
   - only the model's signature passes, a clean point with one side's `n(L)` and an `n_S` below it, and a point whose `n_S` is above stays Unresolved (UB, UA);
   - the point steers by `n(L)` only, is never a clean end, certifies no crossing, makes the step a branch step, is named in the qualifier and is recorded with its counts (UA, UB);
   - the classification, continuity and guard checks are unchanged (UA);
   - plants for strong mixing up to `6δ`, beyond it, A2 in the same regime and cancelling changes, with an arm that restores v6's reading (UB, UA).

Decisions 3, 7 and 8 have your go (2026-10-12), and both units keep each as written. Decision 9 needs both units' review of this change only; REGISTER_5 follows their GO.
