# T5's top at `N = 48`: the terms

*In the manifest, so the pin holds it. Written after the rows' reads, whose records are on main at `bcee21ad`, and before any solve at `N = 48`. DESIGN.md section 4 holds `N = 48` in reserve for T5's top, in `R2` alone, added by its own dated commit if `N = 40` leaves it open, and asks that commit to state first what counts as open, the ladder with its band and identity pairs, its own control evidence, and the three laws' values at `N = 48`. These terms state them. MIT's own computation, outside M8, as DESIGN.md states.*

## 1. What counts as open, and what runs

**The targets** are T5's points above 90.51 that the reads leave not classified on `N = 24`, 32 and 40, as built and changed alike (DEVLOG entry 11; `dev/runs/014_top48_expectations/`, A):

| Points | Records at `N = 24` / 32 / 40 | Why not classified |
|---|---|---|
| 116, 120 | Elliptic (4, 0, 4) at 116, Hyperbolic (4, 0, 4) at 120 / Elliptic (9, 3, 6) / Elliptic (9, 3, 6) | the rule: structure differs along the ladder, and a tested set's count differs between cutoffs; branch identity between 24 and 32: the records differ, with the aligned distance under the guard, 0.0096 and 0.0098 |
| 124 | Hyperbolic (4, 0, 4) / Elliptic (4, 0, 4) / Elliptic (4, 0, 4) | the rule: structure differs along the ladder, and two tested sets' counts differ between cutoffs; branch identity between 24 and 32: the records differ, aligned distance 0.0101 |
| 126 | Hyperbolic (4, 0, 4) at all three | the rule: the quartet's `U` = 3.88×10⁻³ exceeds one tenth of its distance to the axis, 7.50×10⁻⁴ (distance 7.50×10⁻³); branch identity between 24 and 32: aligned distance 0.0102, the records agree |
| 127, 128, 129, 130, 132 | Hyperbolic (4, 0, 4) at all three | branch identity between 24 and 32 alone: aligned distance 0.0103 to 0.0106, the records agree |

**The in-row controls** are T5's points above 90.51 that the reads classify: 100, 106 and 112, Elliptic (9, 3, 6) both ways, branch identity kept on both pairs. They are read at `N = 48` as controls, with marks (section 4), and are not targets.

**The supporting points** are the rest of T5's grid. Each cutoff runs on its own path from the seed (DESIGN.md section 4), so `N = 48` solves T5's whole grid, all 31 points, from 0.25 to 132, and reads only the nine targets and three in-row controls above. **Out of scope:** T5's two other unclassified points, 11.31 and 16, where a partner set's count differs between cutoffs; T5's second member, outside the design's reservation, whose 128 and 132 are not classified on the first ladder either; and every other row.

## 2. The ladder, its band and its identity pairs

- **The ladder** is `N = 32`, 40 and 48, all three required for classification. A point is classified on it as on any ladder (`census_lib.here`): accepted with K1 at each cutoff, the rule's reading converged with a type, and branch identity kept on (32, 40) and (40, 48). The type is the rule's, with `N = 48`'s indices.
- **The band** is unchanged: the rule scores the band above `N = 16`, level 17 in `R2`, with the reading on the band above `N = 24` beside it, unscored. It is the first ladder's band.
- **Branch identity's guard** stays at 10⁻² (`checks.IDENTITY`), its record test unchanged.
- **Both verdicts,** as built and changed, at every point, the changed one through `changed.identity`, as on the first ladder.
- **The first ladder's reading stays.** Each target's reading on `N = 24`, 32 and 40, not classified, with its causes, is the record, and is reported beside its reading on the new ladder. The new ladder does not replace it.
- **No four-rung ladder.** `N = 24`, 32, 40 and 48 together would hold the pair (24, 32), whose failure at these points is on record, and `census_lib.here` asks every pair. The question `N = 48` can answer is a different one: whether the type holds on `N = 32`, 40 and 48 together, under the same rule.

## 3. The central question: a type on its own, or the failure set aside

Whether the new ladder establishes a type on its own, rather than discarding an inconvenient comparison, is the question these terms put to review first. What bears on it:
- **The ladder was fixed before `N = 40` was read.** DESIGN.md section 4, pinned at `6063351a` before any solve, says that "the stored 24-to-32 distance already fails the identity guard at 128 and 132 by 3.6% and 6.2%, so a clean reading there may need 32, 40 and 48". Its basis was M8.17's stored record. The failure was known, and named, when the ladder was chosen: the 24-to-32 distance over the guard, with the records agreeing, which the reads find at 126 to 132. At 116, 120 and 124 the first ladder fails because `N = 24`'s record has another type or other indices, which the design did not name; there the ladder was taken knowing why the first one failed, and the reason it sets `N = 24` aside is the INFERRED one below.
- **The numerical tests and thresholds are unchanged.** K1, the rule, its band, the guard and both verdicts are the first ladder's. The new ladder replaces `N = 24` with 48, so it tests convergence over a different range of cutoffs. The failed 24-to-32 comparison remains part of the evidence.
- **What is new is `N = 48`:** a new solve on its own path, a new read, a new identity pair, and the rule's contraction test across 32, 40 and 48. If a type is not settled by `N = 40`, `N = 48` is where it can show.
- **Why `N = 24` differs at the top** (INFERRED): the top's events moved with the cutoff. On the square-root law the collision sits at 118.08 at `N = 24`, 125.75 at 32 and 125.97 at 40; the index drop lies in (112, 116) at 24 and in (120, 124) at 32 and 40. So at 116 to 124, `N = 24` samples the other side of an event, and at 127 to 132 the quartet's real part steps 0.10 to 0.14 from 24 to 32 and 0.003 to 0.007 from 32 to 40.
- **What it cannot show:** a classification on the new ladder rests on three cutoffs, two of them the first ladder's. It establishes the type under this computation's rule at the three tested cutoffs, `N = 32`, 40 and 48. It does not establish the type at every higher cutoff. It does not show that `N = 24`'s record is wrong, and it does not remove the failure between 24 and 32, which stays in the record.

## 4. Control evidence at `N = 48`, first

No calibration carries to `N = 48` by itself. Every tolerance that grows with the cutoff is forecast there from the `N = 40` reads (`dev/runs/014_top48_expectations/`, E), and the controls below are solved and read at `N = 48` before any of T5's points is read there.

**The fresh controls at `N = 48`:** the same six points, on the same entries and paths, solved at `N = 48`, and read on the new ladder. Each passes only if it holds every mark: its seed's check at `N = 48`; accepted with K1, and the case's own type and indices, at 32, 40 and 48; branch identity on both pairs; the changed verdict converged with the case's type; and its as-built verdict, stated first:

| Point | As built on 32, 40, 48 | Why |
|---|---|---|
| P5, 0.30 | converged | no gap in its tested set falls between τ(40) and τ(48); the nearest above is 1.11 τ(48) |
| C2b, 0.30 | converged | `R2`; nothing near any tolerance |
| C2a/R5, 0.30 | converged | `R5`; nothing near any tolerance |
| C3R/R4, 0.20 | Unresolved, by D's flag at `N = 40` and 48 alone, B clearing it | D's eigenvalue −0.01286 lies in n(D)'s inherited gray zone at 40 and 48, whose top grows from 0.0163 to 0.0235 |
| C3R/R4, 0.30 | Unresolved, by D's flag at `N = 48` alone, B clearing it | D's eigenvalue −0.019016 lies outside that zone at 40 and inside it at 48 |
| P5, 0.24 | reported, not marked | its pair, 1.049×10⁻⁵ apart, is two groups at 32 and one at 40, and one at 48 by τ (at 4.02: 0.964, 1.207, 1.449 ×10⁻⁵ at 32, 40, 48). On this ladder the link holds at both higher cutoffs, so whether the as-built rule reads the step from 32 to 40 as motion turns on its contraction test, which the first ladder never put to it. Its changed verdict is marked |

The flags are forecast with ‖B‖ taken as ‖A‖, which reproduces n(D)'s inherited flag, present or absent, at all 369 read records at `N = 24`, 32 and 40, and ‖A‖ at `N = 48` as the `N = 40` value plus the difference of `N(N + 2)`, as `dev/tolerances.py` took it (INFERRED). A mark's cause is tested from the records, as `run/fresh.py` tests the first ladder's. A control that misses a mark is diagnosed and disclosed, T5's top is not read at `N = 48`, and moving past the miss takes a dated decision.

**The in-row controls:** T5 at 100, 106 and 112 must be classified both ways on the new ladder, Elliptic (9, 3, 6). If any misses, no target is classified on the new ladder, and every target's reading there is reported raw, with the miss named.

**The reads at `N = 32` and 40, again.** Before any read at `N = 48`, the stored solutions at 32 and 40 at every point the new ladder reads are read again on the reads' tree and the run's machine, and each must equal its stored read field for field, timings aside. The new ladder's readings use the stored reads, so this shows that the machine and the code still read them as they were read.

## 5. Stated before any solve at `N = 48`

All INFERRED, from known outcomes (`dev/runs/014_top48_expectations/`). None is a classification. Three cutoffs cannot separate the laws.

- **The design's laws, as pinned.** Fitted to M8.17's `N = 16`, 24 and 32, they gave at 128: 0.0481, 0.0346 and 0.0534 at `N = 40`, and 0.0288, −0.0015 and 0.0420 at 48, geometric, algebraic and with its square geometric. At 132: 0.1272, 0.1161, 0.1359 at 40, and 0.1159, 0.0925, 0.1311 at 48 (`dev/t5_laws.out`). **At `N = 40` all three missed:** the reads give 0.0913 and 0.1568, above every law (DEVLOG entry 11). Their values at 48 stand as stated, and are expected to miss again.
- **The same laws on `N = 24`, 32 and 40.** The quartet's real part at 48: 127, 0.0643 to 0.0647; 128, 0.0909 to 0.0912; 129, 0.1112 to 0.1115; 130, 0.1282 to 0.1284; 132, 0.1565 to 0.1567. Its step from 40 to 48 is about 1×10⁻⁴ to 7×10⁻⁴, where 24 to 32 stepped about 0.1.
- **The collision** at 125.98 at `N = 48` (the zeros' ratio, 0.028, carried one rung; the Aitken limit is 125.976). The design's "near 127 at `N = 40`, with a limit of 127.5 to 128" missed at 40, where the collision sits at 125.97.
- **The types at `N = 48`:** Elliptic (9, 3, 6) at 116 and 120; Elliptic (4, 0, 4) at 124; Hyperbolic (4, 0, 4) from 126, with the quartet within about 0.01 of the axis at 126, too close to call, and off the axis by the values above from 127.
- **Branch identity at (40, 48):** 5×10⁻⁴ to 9×10⁻⁴ at every target and in-row control, 11 to 19 times under the guard, by the ratio of the last two pairs.
- **The tolerances at `N = 48`,** at every point it reads on T5: no gap falls between τ(40) and τ(48); K1's separation keeps A's smallest eigenvalue outside the cluster at least 200 times the top of its gray zone; L's gray zone stays at least 10⁷ times clear; and n(D)'s inherited zone holds no eigenvalue.
- **The branch:** T5's path at `N = 48` should reach 132 on the branch it holds at 32 and 40, which the in-row controls and identity at (40, 48) test.

## 6. What ends it, and what it claims

- **A target is classified on the new ladder** when the recheck has passed, the fresh controls' pass at `N = 48` is on record, every in-row control holds its marks, and `census_lib.here` classifies it on `N = 32`, 40 and 48. Each verdict, as built and changed, is reported with its type and indices, beside the point's reading on the first ladder; where the two agree, the point rests on no changed code (DESIGN.md section 3).
- **Otherwise it is not classified on the new ladder,** and its raw values at 32, 40 and 48 are reported with each cause: K1, the rule's reasons, branch identity's aligned distance and records. It stays open.
- **A failed step on T5's path at `N = 48`** ends the path there (DESIGN.md section 4). The points past it are not solved at 48 and stay open.
- **No further cutoff, tolerance, ladder or point** is added under these terms. Anything else takes another dated decision, with its terms first.
- **What a classification claims:** a type on `N = 32`, 40 and 48 under this instrument, MIT's own, outside M8. It is no M8.17 or M8.18 result, takes no part in S6, selects no S5 stretch and moves no `MODELS.md` cell. On the first ladder the point stays not classified, and the census reports both.

## 7. The two trees, and the order

No tree can name its own pin, since the pin hashes `run/jobs.py`, which holds `SOLVE_PINS`. So `N = 48` takes two commits, both planned here:

1. **The solves' tree:** these terms and the code for every step below, with `SOLVE_PINS` unchanged, re-pinned. One commit, pushed. It reads nothing, so it takes no note.
2. **The solves,** under that pin: `runner.py run/out solves48`, T5's whole grid and the four fresh entries at `N = 48`, four at a time, longest first. Between this pin and the next there are no spectral reads, no previews and no grid change from a result. The only checks are on solve fields: each seed's check and each point's acceptance.
3. **The reads' tree,** after the last solve: `SOLVE_PINS` gains the solves' pin, its one change, re-pinned. One commit, with the census page's dated note naming its pin and the solves' pin, since `jobs.note_gate` refuses every read without it.
4. **The reads,** under that pin, each kind refusing until the one before has passed: `rechecks48` (section 4); then the fresh controls, `reads48`, `identities48`, `readings48` and the check `fresh48`; then T5's points the same way; then `top48`, which tests the in-row marks and states each target's outcome.
5. **The record,** labelled as MIT's own, with the census page's note (DESIGN.md section 7).

## 8. The cost

INFERRED, from this run's path and read seconds at `N = 32` and 40, four jobs at a time (`dev/runs/014_top48_expectations/`, F). From 32 to 40 each entry's path grew 4.6 to 5.0 times, as `N` to the power 6.8 to 7.3; carried to 48 that is 3.5 to 3.8 times `N = 40`'s, and `N⁹` would give 5.2.
- **T5's whole grid at `N = 48`:** 35 to 49 hours at four jobs at a time, about half that alone. P5's two points 3.9 to 5.5 hours, C3R/R4's 4.2 to 5.9, C2a/R5's 1.6 to 2.4, C2b's 0.6 to 0.8. T5's path dominates the projected wall time: about one to two days, with uncertainty from concurrent-job contention. Its 35 to 49 hours assume four jobs at a time throughout; the fresh paths finish within its first six hours, and alone it runs about twice as fast (INFERRED).
- **The reads at `N = 48`:** about 7 to 10 minutes a point for T5, 6 to 48 for the controls, a few hours in all, with the recheck about an hour.
- **Memory:** at most 1.68 GiB a job at `N = 40`; more at 48, where the functional's chunks keep it bounded, on a machine of 24 GiB.
- A killed job resumes at its next point.

## 9. What it was chosen knowing

The reads at `N = 24`, 32 and 40 of T5's row, of T5's second member and of the fresh controls, as built and changed, whose records are on main at `bcee21ad`; DESIGN.md section 4's reservation and section 6's statements, pinned before any read, and their misses at `N = 40`; and M8.17's stored record at T5. Each is a known outcome. The targets follow from the readings by section 1's rule; the ladder is DESIGN.md's; the marks are restated from the `N = 40` records, and the in-row controls are T5's classified points above 90.51. T4/R4's locator plays no part.
