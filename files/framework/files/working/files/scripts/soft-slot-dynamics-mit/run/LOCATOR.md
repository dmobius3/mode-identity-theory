# T4/R4's locator: the terms

*In the manifest, so the pin holds it. Written after the rows' reads, whose records are on main at `bcee21ad`, and before any midpoint is solved. MIT's own computation, outside M8, as DESIGN.md states.*

## 1. What it locates

T4/R4's change of type. The reads classify all 18 points of T4's row in `R4` at `N = 24`, 32 and 40, as built and changed alike: Elliptic (7, 1, 6) from 0.25 to 4, and Hyperbolic (6, 1, 5) from 5.66 to 72 (DEVLOG entry 11). So the sampled row gives one type-change bracket, between two consecutive grid points. By the rule DESIGN.md section 4 fixed before any solve, the bracket is (4, 5.66): it narrows from (2.83, 5.66) because the read at 4 classifies it Elliptic.

| End | `N = 24` | `N = 32` | `N = 40` | As built | Changed |
|---|---|---|---|---|---|
| 4 | Elliptic (7, 1, 6) | Elliptic (7, 1, 6) | Elliptic (7, 1, 6) | Elliptic (7, 1, 6) | Elliptic (7, 1, 6) |
| 5.66 | Hyperbolic (6, 1, 5) | Hyperbolic (6, 1, 5) | Hyperbolic (6, 1, 5) | Hyperbolic (6, 1, 5) | Hyperbolic (6, 1, 5) |

**The index evidence.** `n(L)` at the ends is 7 and 6, resolved at every cutoff, so `census_lib.bracket_kind` reads an index bracket, with a signed change of −1 at `N = 32` and 40. `N = 24` is bisected too, since its ends' `n(L)` are resolved and different; it is reported and does not decide.

## 2. The ladder and the rule

`census_lib.settle` is unchanged, on M8.18's `ARM_A` ladder. This MIT-side locator additionally applies M8.18's T4/R5 moved-midpoint exception to T4/R4, as fixed in `DESIGN.md` §4 before the row was read:
- The ladder is `N = 24`, 32 and 40. `N = 32` and 40 decide, and `N = 24` is bisected and reported.
- Each midpoint is solved from both ends of the current interval, by continuation from each end's solution at that cutoff, the stored ones first and then the midpoints the bisection keeps, and read. K1 is asked of both solutions, and `n(L)` is read by inertia.
- The two solutions must agree: their aligned distance at most 10⁻² (`census_lib.AGREE`, branch identity's guard), and the same `n(L)`.
- The half whose ends differ in `n(L)` is kept. A cutoff's bisection completes when its interval is narrower than `W/2` = 5×10⁻⁴ of its lower end.
- **The moved midpoint** (DESIGN.md, section 4): where both solves are accepted and K1 fails at either, the midpoint is moved once, to the point 0.4 of the interval above its lower end (`census_lib.MOVED`), and solved there from both ends. The refused midpoint stays in the record and decides nothing.
- **The stops.** Each of these ends a cutoff's bisection unsuccessfully: K1 failing at a moved point; a solve that fails or is not accepted; `n(L)` unresolved; the two solutions disagreeing; and an `n(L)` that matches neither end. A midpoint where a solve fails is not moved.
- There is no other retry, step, tolerance or fallback.

**The moved midpoint is K1's exception, not a search method.** Its fraction and its end are Arm B's. M8.18 chose them for T4/R5 from M8.17's record there, and DESIGN.md took them unchanged before any read of this computation; nothing about T4/R4's bracket chose them. Whether a midpoint here needs moving, and whether a moved one passes K1, is unknown until the run. M8.18's terms named this change the likeliest new bracket to stop on K1, since its ends carry T4/R5's indices, and gave a new bracket no moved midpoint. DESIGN.md gave this one Arm B's knowing both, outside M8.

## 3. The location, and what ends it

- **The location** (`census_lib.location`): both deciding cutoffs complete, each interval narrower than `W/2` of its lower end; the two intervals' interiors overlap; their union is narrower than `W` = 10⁻³ of its lower end; and the signed change of `n(L)` is the same at both, and not zero.
- **The guard readings** (`census_lib.guards`): one at the union's lower end times 1 − δ, continued from the bracket's lower end, 4, and one at its upper end times 1 + δ, continued from its upper end, 5.66. δ is 0.01, then 0.05 as a single retry. Each is read at all three cutoffs and classified as every point is: K1 at each cutoff, the rule converged with a type, and branch identity on both pairs (`census_lib.here`). Each side's first classified reading counts, and it must carry its end's type: Elliptic below, Hyperbolic above. A guard outside the row's window is not computed.
- **Both verdicts** (DESIGN.md, section 4): at each guard reading that counts, the changed classification, made from the same records as the rows' readings make it (the changed reading, and branch identity through `changed.identity`), must also be classified, with the same type. Otherwise the bracket is not located, and the guard is named (`locate.both_verdicts`).
- **The name,** if located, is M8.17's: "a change of type located between the guard readings, with `n(L)` changing by -1 inside the interval at `N = 32` and 40".
- **Otherwise** the bracket stays not located, with the exact stop in the record. Nothing is rerun under another rule, tolerance or ladder without a dated commit.

## 4. The reproduction, first

Before T4/R4 is read, the job reproduces one stored location on this tree.
- **Which:** M8.18's Arm B, the location of T4/R5's change at (8.720990, 8.724874), on Arm B's ladder, `N = 16`, 24 and 32, with 24 and 32 deciding. It exercises the moved midpoint: at `N = 24` and 32 K1 refused the midpoint 8.721638, and the moved point 8.720990 completed each bisection.
- **How:** as M8.18's `census.py` ran it, through `census_lib.locate`. Each cutoff's path is recomputed from its seed to 11.31, and every recomputed point must equal M8.17's record (`census_lib.gate_full`), and each of M8.17's midpoints its record (`census_lib.gate_midpoints`). Then `settle` runs with the moved midpoint, the location and the guards. T4/R5's case here must equal M8.18's frozen case field for field, and M8.17's bracket must be Arm B's. The read is this computation's own (`jobs.Cut`), with its new fields set aside (`locate.as_m818`), so the records compare in M8.18's form.
- **What is compared, and the pass:** the whole record against M8.18's `ARM_B.json`, field for field (`census_lib.differences`), timings aside. That covers the recomputed path, the ends, every midpoint from both ends with its acceptance, K1, `n(L)` and record, each aligned distance, the moved point, each interval, the union, the guard readings with their records, and the name. In addition every array of the midpoints' and guards' solutions must equal M8.18's `arm_b_solutions.npz`, entry for entry, 146 arrays. It passes with no stop, no difference and no unequal array. M8.18's files come from its published folder, each by its `SHA256SUMS`, whose SHA-256 `jobs.M818_SUMS` pins.
- **If it fails,** T4/R4 is not read (`locate.refusal`). The failure is diagnosed and disclosed, and moving past it takes a dated commit.

## 5. Where it starts, and what it keeps

- **The ends:** this computation's stored solutions at 4 and 5.66 at each cutoff, through `jobs.stored`, so each passes `SOLVE_PINS` and its files' SHA-256. Each must be accepted, with its `lam` the reads' own. The ends' records are the reads', from the reading file checked against its job record, both ways.
- **What it keeps:** the ends' records and their classifications both ways; at each cutoff, every midpoint, the refused one included, with both solves' acceptance, K1, `n(L)` and record, and their aligned distance; each interval and each stop; the union; every guard reading, as built and changed, with its records; and the midpoints' and guards' solutions, in a file of their own.
- **The pins:** the job runs under this tree's manifest, and its reads wait for the census page's note naming it (`jobs.note_gate`). Its midpoints' and guards' solutions are solved and read inside the job and never loaded through `jobs.stored`. A later tree that loads them adds this tree's pin to `SOLVE_PINS` in its own commit, since no tree can name its own pin.

## 6. What it was chosen knowing, and what it claims

- **Chosen knowing:** the row's reads at all three cutoffs, as built and changed, whose records are on main at `bcee21ad`; M8.17's stored readings and its locator record on T4/R5; M8.18's terms, which gave a new bracket no moved midpoint and named this one the likeliest to stop on K1; and M8.18's Arm B record. Each is a known outcome. The bracket follows from the reads by DESIGN.md section 4's rule. Every rule above was fixed before the row was read: in `census_lib`, M8.17's and M8.18's, and in DESIGN.md section 4. This document adds the choice of the reproduction and its pass, and the job's plumbing.
- **What it claims:** a location, if one is found, is "a change of type located between the guard readings", as M8.17's terms name one, with `n(L)` changing inside the interval. It is not identified with the genuine index crossing: a numerical location does not by itself show that the change of type coincides with it. It is MIT's own, outside M8. It is no M8.17 or M8.18 result, takes no part in S6, selects no S5 stretch and moves no `MODELS.md` cell.

## 7. The run

- One job at a time: the reproduction, then T4/R4. Each is a job of `run/jobs.py`, launched by `run/runner.py`'s kind `locate`, which plans the reproduction first, from `--source`, M8.18's published folder, and T4/R4 once the reproduction has passed. It refuses without `--note` and `--repo`.
- **Rough cost** (INFERRED): M8.18's Arm B took 5 h 20 min on this machine. T4/R4's bisections run at `N = 40`, where each step costs more. A killed job starts again from the beginning, up to the runner's three starts.
- T5's `N = 48` is not part of these terms.
