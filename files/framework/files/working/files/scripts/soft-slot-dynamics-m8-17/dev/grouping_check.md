# The census run: the grouping check at the read Unresolved points (2026-10-26)

Read-only, from M8.16.1's record (MIT `292b158`, `run/out/`). It answers UB's question after #653's approval: does the link-tolerance merge behind T5J's failure also sit behind the convergence rule's Unresolved readings on the census rows? It proposes no adequacy test and changes no instrument. `grouping_check.py` (SHA-256 `a69dd214142225177026de9b891102f65d04e9323ababdb9bd5b472839f4d19d`) reproduces every number here.

## What was read

- **The points:** K6's read points that the rule leaves Unresolved, 11 in all. T3/R4 has three, at `ε` = 16, 45.25 and 64, and T5/R2 has eight, from 5.66 to 90.51. The five points the run solved but did not read stay closed, and the script refuses to open them.
- **The replay.** At each point, the frozen rule (`instrument/convergence.py`) was run again on the three cutoffs' stored summaries. It gives the recorded verdict and reasons at every point.
- **The test,** UB's three steps:
  1. each failing set's members at `N = 16`, 24 and 32;
  2. their spacings against each cutoff's link tolerance, `τ = max(margin, 10 √(u‖A‖|λ|))` (`instrument/linear.py`);
  3. a flag where a spacing falls between two cutoffs' tolerances.
- **The control:** T5J/R2 at `ε = 0.25`, where entry 75 of M8.16.1's log found the merge. The test must flag it.

## What it finds

**The merge does not recur (DERIVED, at these points).**
- There are 16 failing readings, after removing repeats where several tested groups share one partner set. They are not independent: at T5/R2's 64 the tested set near 0.606i contains the tested groups at 0.482i and 0.394i; at T5/R2's 90.51 the tested set near 0.527i contains the tested group at 0.264i.
- At none of them does a spacing fall between two cutoffs' tolerances. The members of every failing set lie at least 5.25×10⁻⁴ apart, while the largest tolerance at any of them is 1.111×10⁻⁵: from the unrounded values the spacings are at least 47.2 times the tolerance.
- Where a set's count is the same at all three cutoffs, so are its members' sizes. Sizes change only in sets that gain members.
- The control is flagged at both of its split cutoffs: the pair's 8.8×10⁻⁶ spacing lies between `N = 16`'s tolerance and `N = 32`'s.

**What the failures are (DERIVED, from the replay):**
- **10 count changes.** In 9 of them, `N = 16` holds fewer eigenvalues in the set than `N = 24` and 32, which agree. In 1 (T5/R2 at 11.31), `N = 16` and 24 hold one and `N = 32` two.
- **6 non-contractions,** all at T5/R2 from `ε = 16` up. The change from `N = 24` to 32, by the rule's own measure, is 1.85×10⁻³ to 2.49×10⁻²: larger than the change from 16 to 24, and at least 558 times the floor.
- **At T5/R2's 90.51,** the cutoffs also disagree on the structure: `N = 16`'s record differs from `N = 24`'s and 32's in type and indices. The point carries no type from this instrument.

**The reading.** No T5J-style link-tolerance merge is found at these 11 points. At 9 of the 10 count changes, the cutoff whose set holds fewer eigenvalues holds a same-class, same-sign eigenvalue outside the set, at 1.08 to 1.45 times the closure's reach from a member at the adjacent cutoff (DERIVED, against the rule's own window, twice the nearest candidate's distance); only T5/R2's tested set at 90.51 has none. Read by proximity, that eigenvalue is the member the set lacks at seven: T3/R4 at 16 and 64, and T5/R2 at 5.66, 8, 11.31 and 32 and its partner set at 90.51. There the cutoff's eigenvalues sit shifted against the next cutoff's, by about the members' own spacing, and by several spacings at T3/R4's 64, and the closure's window takes in only one of a pair. At T3/R4's 45.25, `N = 16` holds five of the six, and at T5/R2's tested set at 64 the nearest such eigenvalue lies outside the set's span. So the closure's window, more than missing eigenvalues, sets most of these counts (INFERRED: identifying a counterpart by proximity is a reading, not the rule's, and `grouping_check.py` lists every eigenvalue it rests on). The non-contractions are eigenvalues still moving between 24 and 32 at T5's larger amplitudes.

| Row | `ε` | Reading | Why | Count at `N` = 16, 24, 32 | Least spacing | Largest tolerance | Change, 16 to 24 and 24 to 32 | Nearest outside the set, times the closure's reach |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| T3/R4 | 16 | tested set, near 3.516i | the set's count differs between cutoffs | 2, 4, 4 | 4.9×10⁻³ | 9.1×10⁻⁶ | 6.5×10⁻⁴, 2.3×10⁻⁶ | 1.08, at N = 16 |
| T3/R4 | 45.25 | tested set, near 3.238i | the set's count differs between cutoffs | 3, 6, 6 | 1.6×10⁻³ | 8.8×10⁻⁶ | 5.7×10⁻³, 2.7×10⁻³ | 1.18, at N = 16 |
| T3/R4 | 64 | tested set, near 3.035i | the set's count differs between cutoffs | 5, 6, 6 | 2.3×10⁻² | 8.6×10⁻⁶ | 4.6×10⁻², 6.3×10⁻³ | 1.18, at N = 16 |
| T5/R2 | 5.657 | partner set, near 5.771i | the set's count differs between cutoffs | 1, 2, 2 | 5.3×10⁻⁴ | 1.1×10⁻⁵ | 1.7×10⁻⁴, 2.4×10⁻⁴ | 1.11, at N = 16 |
| T5/R2 | 8 | partner set, near 5.672i | the set's count differs between cutoffs | 1, 2, 2 | 8.0×10⁻⁴ | 1.1×10⁻⁵ | 2.0×10⁻⁴, 4.7×10⁻⁴ | 1.19, at N = 16 |
| T5/R2 | 11.31 | partner set, near 5.539i | the set's count differs between cutoffs | 1, 1, 2 | 1.2×10⁻³ | 1.1×10⁻⁵ | 3.7×10⁻⁴, 3.1×10⁻⁴ | 1.18, at N = 24 |
| T5/R2 | 16 | partner set, near 5.363i | non-contracting above the floor | 2, 2, 2 | 2.0×10⁻³ | 1.1×10⁻⁵ | 1.1×10⁻³, 1.9×10⁻³ | - |
| T5/R2 | 22.63 | partner set, near 5.138i | non-contracting above the floor | 2, 2, 2 | 3.2×10⁻³ | 1.1×10⁻⁵ | 4.2×10⁻⁴, 3.6×10⁻³ | - |
| T5/R2 | 32 | tested set, near 0.436i | the set's count differs between cutoffs | 1, 2, 2 | 3.0×10⁻² | 4.4×10⁻⁶ | 8.5×10⁻³, 1.6×10⁻⁴ | 1.32, at N = 16 |
| T5/R2 | 32 | partner set, near 4.860i | non-contracting above the floor | 2, 2, 2 | 5.5×10⁻³ | 1.0×10⁻⁵ | 3.5×10⁻³, 7.1×10⁻³ | - |
| T5/R2 | 64 | tested set, near 0.606i | the set's count differs between cutoffs | 2, 3, 3 | 8.8×10⁻² | 6.6×10⁻⁶ | 5.8×10⁻³, 6.3×10⁻³ | 1.45, at N = 16 |
| T5/R2 | 64 | tested group, near 0.482i | non-contracting above the floor | 1, 1, 1 | - | 6.6×10⁻⁶ | 1.8×10⁻⁴, 3.7×10⁻³ | - |
| T5/R2 | 64 | tested group, near 0.394i | non-contracting above the floor | 1, 1, 1 | - | 6.6×10⁻⁶ | 5.8×10⁻³, 6.3×10⁻³ | - |
| T5/R2 | 90.51 | tested set, near 0.527i | the set's count differs between cutoffs | 1, 3, 3 | 9.8×10⁻² | 8.2×10⁻⁶ | 1.0×10⁻², 2.5×10⁻² | none |
| T5/R2 | 90.51 | tested group, near 0.264i | non-contracting above the floor | 1, 1, 1 | - | 8.2×10⁻⁶ | 1.0×10⁻², 2.5×10⁻² | - |
| T5/R2 | 90.51 | partner set, near 3.800i | the set's count differs between cutoffs | 1, 2, 2 | 2.6×10⁻² | 9.5×10⁻⁶ | 4.7×10⁻³, 5.0×10⁻² | 1.13, at N = 16 |
| T5J/R2, the control | 0.25 | partner set, near 6.015i | non-contracting above the floor | 2, 2, 2 | 8.8×10⁻⁶ | 1.1×10⁻⁵ | 9.7×10⁻⁷, 4.8×10⁻⁶ | - |

The change column is directional: between two cutoffs, the largest distance from a member at the lower cutoff to the nearest member at the higher one, so a member the lower cutoff lacks does not enter it. Where the rule measures a change itself, at the non-contractions, it uses the bottleneck distance, and the text above quotes that.

## For the pre-registration

These are questions, not a design:
- **The link tolerance.** Nothing at these points asks S4's adequacy test to answer it. That holds for these 11 points only, not for the five closed points or the unexplored grid.
- **Points where a lower cutoff's eigenvalues shift by about the set's own spacing,** so the closure takes in fewer of them than 24 and 32 agree on: whether S4 reads them from its two highest cutoffs, and under what bar.
- **T5/R2 at 11.31,** where `N = 24` lacks the member too: it appears only at `N = 32`, 1.2×10⁻³ from the other, so a reading from the two highest cutoffs does not reach it.
- **Points where the eigenvalues still move by 10⁻³ to 10⁻² between `N = 24` and 32,** at T5/R2 from `ε = 16` up. A higher cutoff first needs the structural kernel measured on the controls against M8.16.1's K1, with the calibration unchanged (the census page, § V, the note of 2026-10-20).

## Not checked

- That an eigenvalue outside a set is the same mode as the member the set lacks: the reading above is by proximity.
- Any solve: the readings are the run's own, and the check reads its stored summaries.
