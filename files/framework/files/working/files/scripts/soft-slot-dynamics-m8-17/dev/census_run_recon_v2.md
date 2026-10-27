# The census run: what M8.16.1's record settles, row by row (recon, v2, 2026-10-25)

Read-only groundwork for the census run's pre-registration, made while OpenWave #653 waits on the maintainers' adjudication. It reads M8.16.1's record at MIT `292b158` (`RECORD.md` and `run/out/`), the census page's catalog and its account of the open rows (§§ II to IV), and the table of M8.15's decided points in M8.16's terms (§ K6). It proposes no run, sets no acceptance test, chooses no procedure, and moves no catalog status before the adjudication.

## Boundaries

- **The rows.** The nine rows M8.16.1's verdict qualifies: T1 to T4 in `R4` and `R5`, and T5 in `R2`. T5J, T5's second member, is not qualified and is not offered to this instrument again (the terms, § THE VERDICT RULE: WHAT CHANGES), so the census cannot carry it. That answers the catalog's "the other members untested" for this member. C3R/R4 is a control, not a census row.
- **Qualification is not certification.** K6 agreement means the same type, `K` and `k_i⁻` as M8.15 at a read point. The terms' § STATED LIMITS: WHAT IS ADDED leaves finite-amplitude adequacy to the census run (S4). A point the convergence rule leaves Unresolved is not labelled with a type here.
- **Five points stay closed.** M8.16.1 computed five ladder points that M8.15 left undecided. As registered, it solved them for continuation and did not read them (M8.16's terms, § K6):
  - T2/R4 at `ε` = 16 and 22.63;
  - T3/R4 at 32;
  - T3/R5 at 16;
  - T5/R2 at 45.25.

  No linear record exists at them: M8.16.1's driver solved and accepted each for continuation and refused every call that would compute its record (`checks.withheld`), so `run/out/` holds only the solve, its acceptance, reached amplitude, `λ`, `m = ‖φ‖²`, floor and timing. Their types, indices and convergence readings do not exist yet; the census run computes them. (Corrected 2026-10-26: this sentence said their readings sat in `run/out/`.) This memo lists them and does not open them. The census pre-registration states how they will be read, and only then are they opened. Their types, indices and convergence readings have not been read, here or by the record's builder. They enter the record only through K6's acceptance count.

## The windows

The census page, § II: from the registered smallest amplitude, 0.25, to `ε_max = λ₁ − λ₀`, which is 72 in `R4`, 32 in `R5` and 132 in `R2`. M8.15's grid is `ε_k = 0.25 × 2^{k/2}`, with 72 added at `R4`'s top. M8.16.1's ladders ran that grid to each branch's last decided point: 72 in `R4`, 32 in `R5`, and 90.51 for T5. Its samples ran `ε` = 0.25, 0.5, 1 and 2, skipping three of the grid's points below 2: 0.354, 0.707 and 1.414. The counts below describe coverage of M8.15's reference grid. They do not, by themselves, prescribe the grid of the future census run.

## The nine rows

| Row | Window | M8.15 to M8.15.2 (the catalog) | M8.16.1 computed | M8.16.1 reads | What S4 still needs |
| --- | --- | --- | --- | --- | --- |
| T1/R4 | 0.25 to 72 | INVALID | the sample: 0.25, 0.5, 1 and 2 | K5 holds; Elliptic, `(2, 0, 2)`, converged at all four points | 14 of M8.15's grid points unexplored: 0.354, 0.707 and 1.414, and 11 from 2 to 72 |
| T1/R5 | 0.25 to 32 | INVALID | the sample | K5 holds; Elliptic, `(2, 0, 2)`, at all four | 11 grid points unexplored: the three below 2, and 8 from 2 to 32 |
| T4/R4 | 0.25 to 72 | no ladder point (Newton's stopping test) | the sample | K5 holds; Elliptic, `(7, 1, 6)`, at all four | 14 grid points unexplored: the three below 2, and 11 from 2 to 72 |
| T4/R5 | 0.25 to 32 | no ladder point | the sample | K5 holds; Elliptic, `(7, 1, 6)`, at all four | 11 grid points unexplored: the three below 2, and 8 from 2 to 32 |
| T2/R4 | 0.25 to 72 | Elliptic to 11.31 (12 points), Hyperbolic at 32 to 72 (4). M8.15.2: `n(L)` changes within 16.2848 to 16.2977 at level 3 and 16.5178 to 16.5307 at level 2; the levels disagree | 18 points; 16 read; closed: 16, 22.63 | K5 holds; K6 agrees at all 16: Elliptic, `K = 0`, to 11.31; Hyperbolic, `K = 2`, from 32 | the change of type, inside (11.31, 32), where both closed points lie |
| T2/R5 | 0.25 to 32 | Elliptic at all 15; both persistence tests Persist | 15 points, all read | K5 holds; K6 agrees at all 15: Elliptic | no grid point left; a second discretization now agrees at all 15 |
| T3/R4 | 0.25 to 72 | Elliptic at 17, to 72; Invalid at 32, "to be decided" | 18 points; 17 read; closed: 32 | K5 holds; K6 agrees at 14; Unresolved at 16, 45.25 and 64 | 32; the three Unresolved points |
| T3/R5 | 0.25 to 32 | Elliptic to 11.31, Hyperbolic at 22.63 and 32. M8.15.2: a change of type located, under the frozen ceiling's clause 3; `n(L)` changes within 15.7803 to 15.7895 at level 3 and 15.7437 to 15.7529 at level 2 | 15 points; 14 read; closed: 16 | K5 holds; K6 agrees at all 14: Elliptic to 11.31; Hyperbolic at 22.63, `K = 4`, and at 32, `K = 3` | by the catalog, none: closed under the frozen ceiling. The closed point, 16, lies just above M8.15.2's intervals |
| T5/R2 | 0.25 to 132 | Elliptic at 17: to 32, at 64 and at 90.51. Unresolved at 45.25, 128 and 132, between the levels | 18 points, to 90.51; 17 read; closed: 45.25; 128 and 132 not run | K5 holds; K6 agrees at the 9 read points to 4; Unresolved at the 8 from 5.66 to 90.51 | the 8 Unresolved points; 45.25; 90.51 to 132, not computed |

Sources: `RECORD.md` § 5, the K6 tables and the samples' points; `run/out/<row>.json`, `checks.rows` for the read points and `readings` for the samples' four points; the census page, § III, with its notes on the prism in `R4` and the hexagon in `R5`; M8.16's terms, § K6.

## The three questions

**T2/R4: can the record narrow the transition?** Not beyond M8.15's bracket while the closed points stay closed.
- At all 16 read points the qualified instrument agrees with M8.15: Elliptic with `K = 0` through 11.31, and Hyperbolic with `K = 2` from 32. So on both discretizations the change of type lies in (11.31, 32).
- Inside that bracket sit M8.15.2's two `n(L)` intervals, which disagree between its levels, and the two closed points: 16, just below level 3's interval, and 22.63.
- Locating the change is OPEN.

**T1 and T4: how much of the window is unexplored?** Everything above `ε = 2`.
- M8.15 reached no valid point on either row.
- M8.16.1 qualified the instrument on both, in both slots, at four sample points each, all Elliptic with the expected indices and converged at every cutoff.
- Above 2 nothing exists on any qualified instrument: 2 to 72 in `R4` and 2 to 32 in `R5`, 11 and 8 points of M8.15's grid. Below 2 the samples skip three of its points, 0.354, 0.707 and 1.414.
- On M8.15's reference grid that leaves 14 points unexplored in each `R4` row and 11 in each `R5` row: 50 across the four rows. The stretch above 2 is the largest the census run would compute anew.

**T3 and T5: spectral questions or adequacy problems?** By the convergence rule's own stated reasons (`RECORD.md` § 5):
- **T3/R4.** Each of its three Unresolved points, 16, 45.25 and 64, fails on a tested set whose count differs between cutoffs: `N = 16`, 24 and 32 disagree on how many eigenvalues the set holds. That is a question of adequacy in `N`. M8.15 read Elliptic at all three, and the qualified instrument agrees with it at 22.63 and 72. Nothing read here points to a change of type (INFERRED). The closed point at 32, M8.15's Invalid one, is the row's one undecided grid point.
- **T3/R5.** Its change of type is a spectral question, and the catalog closes the row under the frozen ceiling. M8.15.2 located `n(L)`'s change within 15.7803 to 15.7895 at level 3 and 15.7437 to 15.7529 at level 2. The qualified instrument agrees at the read points on either side, Elliptic at 11.31 and Hyperbolic at 22.63. The closed point at 16 lies just above M8.15.2's intervals.
- **T5/R2.** From 5.66 to 32 a Krein-positive partner set near 4.9i to 5.8i fails: its count differs between cutoffs, or its change does not contract above the floor. These are the slow groups' partners, the same mechanism that left T5J Unresolved at 0.25. At 90.51 a partner set near 3.8i fails, and the rule also finds the structure differing between the cutoffs: the type, indices, `V₀` or Krein counts are not the same at `N = 16`, 24 and 32. M8.15 read Elliptic at 64 and at 90.51.
  - From 5.66 to 22.63 the only obstacles are partner sets, which reads as their convergence in `N` (INFERRED).
  - At 32 a tested set fails beside the partner set, and at 64 only tested groups and a tested set fail, each non-contracting or with a count differing between cutoffs (OPEN).
  - At 90.51 the cutoffs disagree on the structure itself, a question of adequacy in `N` (OPEN).
  - Near the window's top, M8.15's level 3 showed one complex quartet at 128 and 132, where its levels disagreed (the census page, § IV). Whether a change of type sits there is OPEN, and 90.51 to 132 has not been computed on this instrument.

## The questions for the census pre-registration

These are questions, not a plan:
- how the five closed points are read, and when they are opened;
- T1 and T4 above `ε = 2`, the largest uncomputed stretch, in four rows, and the three grid points below 2 their samples skip;
- what adequacy test S4 applies at a point the convergence rule leaves Unresolved: on a far partner set (T5), on tested sets or groups whose count differs between cutoffs or which do not contract (T3/R4, and T5 from 32), or where the cutoffs disagree on the structure (T5 at 90.51);
- T5 above 90.51, to the window's top at 132;
- whether K6's agreements at decided points enter the census as classifications, or are read again under the census's own adequacy tests.

No catalog status moves here. The maintainers' adjudication of #653 comes first.
