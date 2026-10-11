# M8.15.x: control 2a, the cluster rule (registered 2026-10-09T01:21:48Z)

**Status:** registered, v2. It folds both review units' redlines of draft v1, and adds one change of my own, flagged in § 3.4. It is frozen before any of 2a's code.

## 1. What 2a must show (memo v4, § 2)

1. **The 0.9 rule fails** on a genuine mode inside the structural span, on an orbit that is not a target.
2. **The candidate rule** (decision 2, tracking anchored to the theorem) classifies that mode genuine at every level and ladder point where it is resolved.
3. **C1, C2a, C2b and C3 reproduce their M8.15 classifications** under the candidate rule. Their reruns belong to qualification (§ 6), and this check is read from them there.

## 2. The case

- **The pyramid `P5` in R4,** with § 1's carry: `AngleBranch` with `track=True`. Its first grid starts at `θ_start = 0`, as the frozen rule sets it for every case but control 1b.
- **The ladder:** M8.15's R4 ladder from `ε_min = 0.25` to `72`, at level 3, then at level 2.
- **The linear record only:** there is no change-of-type bisection and no persistence run.

**The predicted spectrum.** It comes from the reduced quartic at unit `u`, in the continuum (`continuum_overlap_survey.py`; reproduced independently by a review unit), with `Q = 77/65` and `κ = 1/(8 √48 Q)`.
- **The frozen cluster dimension is 6,** the census zero multiplicity. It is made of the phase's Jordan pair, the paired lift of the rotations about `x` and `y`, and the radical lift about `z`.
- **Resolution:** a block is resolved at level `h` at `ε` if `10 τ₀⁽ʰ⁾ ≤ ε κ |τ|`, with `τ₀⁽³⁾ = 1.04×10⁻⁵` and `τ₀⁽²⁾ = 3.97×10⁻⁴`.

| Block | `τ` | Krein | Overlap with `U` | Condition number | First resolved: level 3 / level 2 |
|---|---|---|---|---|---|
| Imaginary pair (in span) | 0.0622348691 | − | 0.997 | 14.2 | `0.25` / `5.66` |
| Quartet | 0.0417352860 + 0.0609168609 i | none | 0.000 | 3.7 | `0.25` / `4` |
| Imaginary pair | 1.0951854883 | + | 0.368 | 1.2 | `0.25` / `0.25` |

The condition numbers are frozen from the continuum (a review unit's `ub_2a_review.py`). The in-span mode is the spectrum's most sensitive eigenvalue.

## 3. The candidate rule, frozen

1. **Blocks and classes.**
   - A block is a slow eigenvalue's Hamiltonian pair or quartet. Its subspace is the real span of its eigenvectors: two dimensions for a pair, four for a quartet.
   - Imaginary pairs are split by Krein sign; real pairs and quartets are classes of their own, read at `τ_Re` as M8.15's representatives are.
   - Blocks whose static part lies at least 0.9 on the fibre and phase-partner span are the exact fibre vectors. They are exempt, and always in `G`.
2. **Multiplets.** Predicted blocks with the same class and the same frozen `τ` form one multiplet of multiplicity `r`.
   - It is matched to `r` computed blocks as a set, so permutations inside it are one assignment, not competing ones.
   - It is tracked as one subspace, the union of its blocks.
3. **The anchor at level 3.** It is a single attempt, at each predicted block's first resolved point.
   - Within each class, the computed blocks outside the fibre, and not already tracked, are matched one to one to the newly resolved predicted blocks.
   - A computed block's cost against a predicted one is `|λ_c − λ_p| / |λ_p|`, on first-quadrant representatives, so a quartet's argument counts. A class's cost `C` is the mean over its predicted blocks.
   - Every assigned block must lie within 0.10.
   - Among all assignments meeting that bound, distinct up to permutations inside multiplets, the best `C` must beat the next-best by at least 0.05. With one predicted block in a class, this compares the two nearest computed blocks.
   - **A failed anchor** leaves the block unanchored: that point, and every later point at that level, is Unresolved for it.
4. **The anchor at level 2 (my addition, not in either review).**
   - **The rule.** At a block's first resolved point at level 2, the reference is level 3's tracked block at the same `ε`, not the theorem. The same window and margin apply. If level 3's block is not tracked there, level 2's is unanchored.
   - **The reason.** Level 2 first resolves the quartet at `ε = 4` and the in-span mode at `5.66`, where finite amplitude has moved every genuine mode off leading order. M8.15's own C2a record has its genuine modes 8 to 11% below leading order at `ε = 4`, and 11 to 15% below at `5.66`, at both levels alike. A theorem anchor there would fail for that reason alone, not for the classifier's. C2a is a closing control, so the rule rests on controls only.
5. **The tracking,** from each ladder point to the next at the same level.
   - **A candidate** is a computed block outside the fibre that meets two conditions:
     - its smallest principal cosine with the tracked subspace, in the phase-space inner product as `slow_lineage` reads it, is at least 0.9;
     - its `|λ|` lies within a factor of 2 of the tracked `|λ|` times `ε_{k+1}/ε_k`.
   - **The search.** Its own class is searched first, and another class only if none in its own qualifies. That case is a tracked class change: it is recorded, with whether the Krein count balances at both points. The phrase "change of type" stays reserved for Target 1.
   - **A multiplet** takes exactly `r` candidates whose own subspaces lie at least 0.9 inside its union, and whose union passes the same test.
   - **Unresolved,** with the track lost and never re-anchored, if any of these happens:
     - no candidate qualifies;
     - two qualify in the class searched;
     - two tracked blocks take the same computed block.
   - The candidates are fixed for every tracked block before any conflict is checked, so the outcome does not depend on order.
6. **`G`** is the fibre blocks plus every computed block not taken by a tracked genuine block.
7. **The refinement veto.** It applies at each ladder point where both levels' `G` have the frozen dimension. Elsewhere it is recorded as not applicable.
   - The lifts in `G` are matched across levels by sorted moduli, within each kind. A lift is radical if its static part lies at least half on the slice direction, as M8.15's points read it, and paired otherwise.
   - Each lift whose level-3 `|λ|` is at least `r_f⁽³⁾` must shrink by at least a factor of 2 from level 2 to level 3. A failure makes the point Unresolved.
8. **Everything else is M8.15's:**
   - the cluster dimension, closure and the Ω-Gram check;
   - the Krein count;
   - the representatives;
   - the cross-level check;
   - validity at `ε_min`, with the 5% bar that § 3 kept.

## 4. The checks

1. **The 0.9 rule fails.** Run on the same points, at level 3 and `ε_min`, it puts the in-span block in `G_tol`, and the cluster dimension is 8 against 6. 2a does not depend on how often it fails elsewhere; its classification is recorded at every point.
2. **The ladder is complete.** The selected track reaches `ε = 72` at both levels. A selected-track end before `ε_max` fails 2a.
3. **The level-3 anchor at `ε_min`.** All three blocks are anchored, each within 0.10, uniquely. The in-span block's anchor error `e` reads as one of three registered outcomes:
   - `e ≤ 5%`: validity and the anchor both pass;
   - `5% < e ≤ 10%`: the branch reads INVALID under the kept 5% bar, while the anchor passes. That is § 3's missing evidence, a non-target control the 5% bar misjudges. The class is read regardless;
   - `e > 10%`: the anchor fails, and 2a fails as registered.
4. **The in-span block stays genuine.**
   - It is tracked and genuine at every level-3 ladder point from `0.25`, and at every level-2 point from `5.66`, for as long as its tracked `|λ|` stays resolved.
   - A loss of track while it is resolved fails 2a.
   - If it leaves the resolved band, the check ends at that point, and what follows is recorded.
5. **Identity, at level 3 and `ε_min`.** The block classified as the in-span mode has:
   - a static overlap of at least 0.9 with `span(X_x Φ, X_y Φ)`, and at most 0.1 with `X_z Φ` (predicted 0.997 and 0.000);
   - a `|λ|` at least ten times the paired lift's.
6. **The candidate rule's cluster dimension.**
   - At level 3 it is 6 wherever all three blocks are tracked.
   - At level 2 it is 12 below `ε = 4` and 8 on `[4, 5.66)`, since unresolved blocks sit in `G`. From `5.66` it is 6, while all three are tracked.
7. **The Krein count** under the candidate rule, at level 3 and `ε_min`: balanced, with `k_c = 1`, `k_i⁻ = 1` and `k_r = 0`.
8. **The veto** passes wherever it applies, expected from `5.66`.
9. **The cross-level points below `5.66`** read Unresolved, from unequal class counts, as M8.15 reads a disagreement. The level-3 class is read regardless.

**Recorded at every ladder point, at both levels:**
- every block's relative anchor error;
- the runner-up overlap at each tracking step;
- the in-span block's overlap with the paired-lift block;
- the paired lift against `τ₀`;
- the tracked class changes;
- the 0.9 rule's classification.

## 5. The synthetic classifier tests, before 2a runs

These are software tests on constructed block data, with the classifier's own functions.
1. **A doubled predicted mode.** Its two computed blocks are rotated arbitrarily inside one 4-dimensional subspace. It is matched uniquely as one multiplet, and tracked as one subspace across a step in which the computed basis rotates inside it.
2. **The same, with an external block** of the same class inside the window and within 0.05 in mean cost. It is Unresolved.
3. **One predicted block with two candidates** inside the window: Unresolved when their mean costs differ by less than 0.05, unique when they differ by more.
4. **A sole candidate outside 0.10:** unanchored, and Unresolved at that point and every later one.
5. **A tracked block whose class changes,** with overlap at least 0.9 and its modulus in band: tracked, with a tracked class change recorded.
6. **Two tracked blocks** that qualify for the same computed block: Unresolved.
7. **A candidate with overlap 0.9 or more but its modulus outside the factor-2 band:** not taken, so Unresolved.

**Mutations:** every check here and in § 4 gets at least one.

**R5** is not run: one slot carries 2a's claim, and R4 has the stronger resolution margin.
