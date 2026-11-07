# MIT's own computation: the record

MIT's own computation of the census's open items, labelled as MIT's own and outside M8. Its values are no M8 outcome, take no part in S6, select no S5 stretch on OpenWave's record and move no `MODELS.md` cell, and they change no closure the census records; the census page says why, in its notes from 2026-11-01 on ([§ V, step 5](../../slot-dynamics-census.md#v-the-program)). Its design is [`run/DESIGN.md`](run/DESIGN.md), with T4/R4's locator in [`run/LOCATOR.md`](run/LOCATOR.md) and T5's top at `N = 48` in [`run/TOP48.md`](run/TOP48.md). It ran in 21 launches from 2026-11-02 to 2026-11-07, 125 jobs in all, none failed. `tools/build_record.py` builds this record from the run's logged files in `run/out/` and its machine's reading in `run/ENVIRONMENT.json`, the statements made before the reads in `run/DESIGN.md` and `run/TOP48.md`, M8.17's stored records, the repository's commit history, and the outputs of `dev/runs/011_row_readings/` and `dev/runs/013_locator_reading/` where it cites them; its fits and extrapolations are labelled INFERRED. It also recomputes each point's classification, as built and changed, from its reading file with `census_lib`, 141 points on the two ladders, and finds every one equal to the file's. The solutions come with this record, as `DEVLOG.md` entry 10 said. The read and reading files stay on the bench, each named by its SHA-256 in the job record that wrote it, and can be read again from the solutions on the pinned trees.

**The chart,** on the ladder `N = 24`, 32 and 40, each cutoff on its own path from the seed. A point is classified when it is accepted with K1 at every cutoff, the rule reads it converged with a type, and branch identity holds on both pairs; the type is the rule's, with `N = 40`'s indices `(n(L), n(D), K)`.

| Row | Slot | Points | Classified, as built / changed | Wherever classified | Not classified |
|---|---|---|---|---|---|
| T1 | `R4` | 18, 0.25 to 72 | 18 / 18 | Elliptic (2, 0, 2) | none |
| T4 | `R4` | 18, 0.25 to 72 | 18 / 18 | Elliptic (7, 1, 6) from 0.25 to 4, Hyperbolic (6, 1, 5) from 5.66 to 72 | none; the change of type between 4 and 5.66 is not located (§ 5) |
| T1 | `R5` | 15, 0.25 to 32 | 15 / 15 | Elliptic (2, 0, 2) | none |
| The coherent row | `R5` | 15, 0.25 to 32 | 15 / 15 | Elliptic (0, 0, 0) | none |
| T5 | `R2` | 31, 0.25 to 132 | 20 / 20 | Elliptic (9, 3, 6) | 11.31, 16, 116 to 132 |
| T5's second member | `R2` | 20, 0.25 to 132 | 15 / 16 | Elliptic (9, 3, 6) | 0.354 as built, 4, 5.66, 128, 132 |

**On a second ladder,** `N = 32`, 40 and 48, T5's top reads, as built and changed alike: 116 and 120, converged, Elliptic (9, 3, 6); 124, converged, Elliptic (4, 0, 4); 126, Unresolved; 127 to 132, converged, Hyperbolic (4, 0, 4). None of it is classified there, because the rule does not read the classified points below it, 100 and 106, converged on that ladder (§ 6).

## 1. Custody

Five stages, each on its own manifest pin. Each read refuses until it is given the commit of the note that names its pin (`run/jobs.py`, `note_gate`), and refuses a path whose job record names a manifest the solves did not run under, or whose files differ. A stage is pinned at the first commit that writes its pin into `run/MANIFEST_PIN`, and noted at the first whose census page names it.

| Stage | Launches | Jobs | Ran | Manifest | Pinned at | Noted at |
|---|---|---|---|---|---|---|
| The solves at `N = 24`, 32 and 40 | 1 | 30 | 2026-11-02 23:39Z to 2026-11-04 04:50Z | `391b097f` | [`6063351a`](https://github.com/dmobius3/mode-identity-theory/commit/6063351ad376a8965936e0ad7001dec3c7d1b429) | [`beb7eee2`](https://github.com/dmobius3/mode-identity-theory/commit/beb7eee2c4bbd21037f63649f030c9f14b944161) |
| The reads at `N = 24`, 32 and 40, the fresh controls first | 7 | 61 | 2026-11-04, 15:22Z to 18:58Z | `8a812b47` | [`649bba39`](https://github.com/dmobius3/mode-identity-theory/commit/649bba39be33343c0f40722ee4c471d175c4a36a) | [`beb7eee2`](https://github.com/dmobius3/mode-identity-theory/commit/beb7eee2c4bbd21037f63649f030c9f14b944161) |
| T4/R4's locator, M8.18's location of T4/R5 reproduced first | 2 | 2 | 2026-11-04 21:00Z to 2026-11-05 10:02Z | `340684d5` | [`87dedb00`](https://github.com/dmobius3/mode-identity-theory/commit/87dedb009ae08d14ac9ffcbb2c8be60fe6540311) | [`87dedb00`](https://github.com/dmobius3/mode-identity-theory/commit/87dedb009ae08d14ac9ffcbb2c8be60fe6540311) |
| The solves at `N = 48` | 1 | 5 | 2026-11-06 06:10Z to 2026-11-07 05:21Z | `80df072c` | [`a27a093c`](https://github.com/dmobius3/mode-identity-theory/commit/a27a093c9e4522dec16a55c358b039f91b4f59bb) | [`82d14af3`](https://github.com/dmobius3/mode-identity-theory/commit/82d14af3b59326694a1eb55de76fc13cec0e4dd1) |
| The reads at `N = 48`, the recheck and the fresh controls first | 10 | 27 | 2026-11-07, 06:10Z to 08:14Z | `dbf9e7cf` | [`82d14af3`](https://github.com/dmobius3/mode-identity-theory/commit/82d14af3b59326694a1eb55de76fc13cec0e4dd1) | [`82d14af3`](https://github.com/dmobius3/mode-identity-theory/commit/82d14af3b59326694a1eb55de76fc13cec0e4dd1) |

- **Every job completed,** none failed, and none was resumed. Each job record names the manifest it ran under, and the 162 files the records logged match their SHA-256.
- **Before each note, the solves were checked at solve fields alone,** which hold no spectrum: `dev/runs/010_solve_checks/` before the note of 2026-11-04, and `dev/runs/015_solve_checks_48/` before the note of 2026-11-07, which also sets each point's reached amplitude at `N = 48` beside its record at `N = 40`, deciding nothing.
- **The recheck.** Before any read at `N = 48`, the stored reads at `N = 32` and 40 at every point the second ladder reads were read again on the run's machine, 36 point-reads, each equal to its stored read field for field, value and type, timings aside: 0 differences.
- **The reproduction.** The locator's job first ran M8.18's location of T4 in `R5` again on this tree: 0 differences from M8.18's record and 0 of 146 arrays unequal, so T4 in `R4` was read.
- **The machine:** Python 3.13.13, NumPy 2.5.0 and SciPy 1.18.0, on Accelerate, under macOS 15.8.2 (24H232) on one Apple M3.

## 2. The fresh controls

Six amplitudes no earlier record holds, next to M8.18's two failures, each with marks fixed before any read on its ladder: the case's own type and indices, K1 and branch identity at every cutoff, and the two verdicts below. No row was read until a pass for the first ladder's marks was on record, and no point of T5 at `N = 48` until a pass for the second's. Every point holds every mark on both ladders.

On `N = 24`, 32 and 40:

| Control | `ε` | Records, `(n(L), n(D), K)`; `k_r`, `k_c`, `k_i⁻` | As built | Changed | Marked, as built / changed | Identity, lower / upper pair |
|---|---|---|---|---|---|---|
| P5 | 0.24 | Hyperbolic (5, 1, 4); 0, 1, 1 | Unresolved | converged | Unresolved, by a new link at `N = 40` alone / converged | 7.95×10⁻⁸ / 4.80×10⁻¹¹ |
| P5 | 0.30 | Hyperbolic (5, 1, 4); 0, 1, 1 | converged | converged | converged / converged | 1.24×10⁻⁷ / 9.35×10⁻¹¹ |
| C3R/R4 | 0.20 | Hyperbolic (5, 1, 4); 0, 1, 1 / Hyperbolic (5, 1, 4); 0, 1, 1 / Hyperbolic (5, 1, 4); 0, 1, 1, D's flag | Unresolved | converged | Unresolved, by D's flag at `N = 40` alone, B clearing it / converged | 5.17×10⁻⁸ / 2.24×10⁻¹¹ |
| C3R/R4 | 0.30 | Hyperbolic (5, 1, 4); 0, 1, 1 | converged | converged | converged / converged | 1.16×10⁻⁷ / 7.53×10⁻¹¹ |
| C2b | 0.30 | Elliptic (0, 0, 0); 0, 0, 0 | converged | converged | converged / converged | 4.81×10⁻⁹ / 8.38×10⁻¹³ |
| C2a/R5 | 0.30 | Elliptic (0, 0, 0); 0, 0, 0 | converged | converged | converged / converged | 2.44×10⁻¹⁰ / 1.07×10⁻¹⁴ |

On `N = 32`, 40 and 48:

| Control | `ε` | Records, `(n(L), n(D), K)`; `k_r`, `k_c`, `k_i⁻` | As built | Changed | Marked, as built / changed | Identity, lower / upper pair |
|---|---|---|---|---|---|---|
| P5 | 0.24 | Hyperbolic (5, 1, 4); 0, 1, 1 | converged | converged | reported, not marked / converged | 4.80×10⁻¹¹ / 3.24×10⁻¹² |
| P5 | 0.30 | Hyperbolic (5, 1, 4); 0, 1, 1 | converged | converged | converged / converged | 9.35×10⁻¹¹ / 6.31×10⁻¹² |
| C3R/R4 | 0.20 | Hyperbolic (5, 1, 4); 0, 1, 1 / Hyperbolic (5, 1, 4); 0, 1, 1, D's flag / Hyperbolic (5, 1, 4); 0, 1, 1, D's flag | Unresolved | converged | Unresolved, by D's flag at `N = 40` and 48 alone, B clearing it / converged | 2.24×10⁻¹¹ / 1.81×10⁻¹² |
| C3R/R4 | 0.30 | Hyperbolic (5, 1, 4); 0, 1, 1 / Hyperbolic (5, 1, 4); 0, 1, 1 / Hyperbolic (5, 1, 4); 0, 1, 1, D's flag | Unresolved | converged | Unresolved, by D's flag at `N = 48` alone, B clearing it / converged | 7.53×10⁻¹¹ / 6.08×10⁻¹² |
| C2b | 0.30 | Elliptic (0, 0, 0); 0, 0, 0 | converged | converged | converged / converged | 8.38×10⁻¹³ / 7.71×10⁻¹⁴ |
| C2a/R5 | 0.30 | Elliptic (0, 0, 0); 0, 0, 0 | converged | converged | converged / converged | 1.07×10⁻¹⁴ / 4.13×10⁻¹⁵ |

## 3. The twelve

The twelve points M8.18's remedy did not read, read here on the first ladder. 12 of 12 keep M8.17's stored type and indices at every cutoff, classified both ways.

| Row | Slot | `ε` | M8.17's records at `N = 16`, 24, 32 | Records at `N = 24`, 32, 40 | As built | Changed | Identity, 24 to 32 / 32 to 40 |
|---|---|---|---|---|---|---|---|
| T1 | `R4` | 1.41 | Elliptic (2, 0, 2) | Elliptic (2, 0, 2) | Elliptic (2, 0, 2) | Elliptic (2, 0, 2) | 3.68×10⁻⁷ / 5.71×10⁻¹⁰ |
| T1 | `R4` | 32 | Elliptic (2, 0, 2) | Elliptic (2, 0, 2) | Elliptic (2, 0, 2) | Elliptic (2, 0, 2) | 7.43×10⁻⁵ / 1.67×10⁻⁶ |
| T1 | `R4` | 45.25 | Elliptic (2, 0, 2) | Elliptic (2, 0, 2) | Elliptic (2, 0, 2) | Elliptic (2, 0, 2) | 1.10×10⁻⁴ / 3.03×10⁻⁶ |
| T1 | `R4` | 64 | Elliptic (2, 0, 2) | Elliptic (2, 0, 2) | Elliptic (2, 0, 2) | Elliptic (2, 0, 2) | 1.54×10⁻⁴ / 5.00×10⁻⁶ |
| T1 | `R4` | 72 | Elliptic (2, 0, 2) | Elliptic (2, 0, 2) | Elliptic (2, 0, 2) | Elliptic (2, 0, 2) | 1.71×10⁻⁴ / 5.82×10⁻⁶ |
| T1 | `R5` | 32 | Elliptic (2, 0, 2) | Elliptic (2, 0, 2) | Elliptic (2, 0, 2) | Elliptic (2, 0, 2) | 3.99×10⁻⁵ / 3.77×10⁻⁷ |
| T4 | `R4` | 4 | Elliptic (7, 1, 6) | Elliptic (7, 1, 6) | Elliptic (7, 1, 6) | Elliptic (7, 1, 6) | 1.79×10⁻⁵ / 1.56×10⁻⁷ |
| T4 | `R4` | 8 | Hyperbolic (6, 1, 5) | Hyperbolic (6, 1, 5) | Hyperbolic (6, 1, 5) | Hyperbolic (6, 1, 5) | 6.43×10⁻⁵ / 1.06×10⁻⁶ |
| T4 | `R4` | 11.31 | Hyperbolic (6, 1, 5) | Hyperbolic (6, 1, 5) | Hyperbolic (6, 1, 5) | Hyperbolic (6, 1, 5) | 1.20×10⁻⁴ / 2.70×10⁻⁶ |
| T4 | `R4` | 64 | Hyperbolic (6, 1, 5) | Hyperbolic (6, 1, 5) | Hyperbolic (6, 1, 5) | Hyperbolic (6, 1, 5) | 0.00226 / 2.18×10⁻⁴ |
| T4 | `R4` | 72 | Hyperbolic (6, 1, 5) | Hyperbolic (6, 1, 5) | Hyperbolic (6, 1, 5) | Hyperbolic (6, 1, 5) | 0.00270 / 2.83×10⁻⁴ |
| T5 | `R2` | 45.25 | Elliptic (9, 3, 6) | Elliptic (9, 3, 6) | Elliptic (9, 3, 6) | Elliptic (9, 3, 6) | 0.00363 / 5.07×10⁻⁴ |

## 4. The rows, point by point

Each point's records at `N = 24`, 32 and 40, given once where they agree at all three, with `(n(L), n(D), K)` and the Krein counts `k_r`, `k_c`, `k_i⁻`; its classification as built and changed; and branch identity's aligned distance on both pairs, against the guard of 10⁻². Below each table, every point not classified, with the causes the run's code gives for it.

### T1 in `R4`

18 points, 18 classified as built and 18 changed.

| `ε` | Records at `N = 24`, 32, 40 | As built | Changed | Identity, 24 to 32 / 32 to 40 |
|---|---|---|---|---|
| 0.25 | Elliptic (2, 0, 2); 0, 0, 1 | Elliptic (2, 0, 2) | Elliptic (2, 0, 2) | 1.20×10⁻⁸ / 3.37×10⁻¹² |
| 0.354 | Elliptic (2, 0, 2); 0, 0, 1 | Elliptic (2, 0, 2) | Elliptic (2, 0, 2) | 2.40×10⁻⁸ / 9.48×10⁻¹² |
| 0.5 | Elliptic (2, 0, 2); 0, 0, 1 | Elliptic (2, 0, 2) | Elliptic (2, 0, 2) | 4.77×10⁻⁸ / 2.66×10⁻¹¹ |
| 0.707 | Elliptic (2, 0, 2); 0, 0, 1 | Elliptic (2, 0, 2) | Elliptic (2, 0, 2) | 9.46×10⁻⁸ / 7.43×10⁻¹¹ |
| 1 | Elliptic (2, 0, 2); 0, 0, 1 | Elliptic (2, 0, 2) | Elliptic (2, 0, 2) | 1.87×10⁻⁷ / 2.07×10⁻¹⁰ |
| 1.41 | Elliptic (2, 0, 2); 0, 0, 1 | Elliptic (2, 0, 2) | Elliptic (2, 0, 2) | 3.68×10⁻⁷ / 5.71×10⁻¹⁰ |
| 2 | Elliptic (2, 0, 2); 0, 0, 1 | Elliptic (2, 0, 2) | Elliptic (2, 0, 2) | 7.20×10⁻⁷ / 1.56×10⁻⁹ |
| 2.83 | Elliptic (2, 0, 2); 0, 0, 1 | Elliptic (2, 0, 2) | Elliptic (2, 0, 2) | 1.40×10⁻⁶ / 4.22×10⁻⁹ |
| 4 | Elliptic (2, 0, 2); 0, 0, 1 | Elliptic (2, 0, 2) | Elliptic (2, 0, 2) | 2.67×10⁻⁶ / 1.12×10⁻⁸ |
| 5.66 | Elliptic (2, 0, 2); 0, 0, 1 | Elliptic (2, 0, 2) | Elliptic (2, 0, 2) | 5.03×10⁻⁶ / 2.90×10⁻⁸ |
| 8 | Elliptic (2, 0, 2); 0, 0, 1 | Elliptic (2, 0, 2) | Elliptic (2, 0, 2) | 9.27×10⁻⁶ / 7.27×10⁻⁸ |
| 11.31 | Elliptic (2, 0, 2); 0, 0, 1 | Elliptic (2, 0, 2) | Elliptic (2, 0, 2) | 1.66×10⁻⁵ / 1.75×10⁻⁷ |
| 16 | Elliptic (2, 0, 2); 0, 0, 1 | Elliptic (2, 0, 2) | Elliptic (2, 0, 2) | 2.87×10⁻⁵ / 3.97×10⁻⁷ |
| 22.63 | Elliptic (2, 0, 2); 0, 0, 1 | Elliptic (2, 0, 2) | Elliptic (2, 0, 2) | 4.74×10⁻⁵ / 8.47×10⁻⁷ |
| 32 | Elliptic (2, 0, 2); 0, 0, 1 | Elliptic (2, 0, 2) | Elliptic (2, 0, 2) | 7.43×10⁻⁵ / 1.67×10⁻⁶ |
| 45.25 | Elliptic (2, 0, 2); 0, 0, 1 | Elliptic (2, 0, 2) | Elliptic (2, 0, 2) | 1.10×10⁻⁴ / 3.03×10⁻⁶ |
| 64 | Elliptic (2, 0, 2); 0, 0, 1 | Elliptic (2, 0, 2) | Elliptic (2, 0, 2) | 1.54×10⁻⁴ / 5.00×10⁻⁶ |
| 72 | Elliptic (2, 0, 2); 0, 0, 1 | Elliptic (2, 0, 2) | Elliptic (2, 0, 2) | 1.71×10⁻⁴ / 5.82×10⁻⁶ |

### T4 in `R4`

18 points, 18 classified as built and 18 changed.

| `ε` | Records at `N = 24`, 32, 40 | As built | Changed | Identity, 24 to 32 / 32 to 40 |
|---|---|---|---|---|
| 0.25 | Elliptic (7, 1, 6); 0, 0, 3 | Elliptic (7, 1, 6) | Elliptic (7, 1, 6) | 7.91×10⁻⁸ / 4.57×10⁻¹¹ |
| 0.354 | Elliptic (7, 1, 6); 0, 0, 3 | Elliptic (7, 1, 6) | Elliptic (7, 1, 6) | 1.58×10⁻⁷ / 1.29×10⁻¹⁰ |
| 0.5 | Elliptic (7, 1, 6); 0, 0, 3 | Elliptic (7, 1, 6) | Elliptic (7, 1, 6) | 3.14×10⁻⁷ / 3.61×10⁻¹⁰ |
| 0.707 | Elliptic (7, 1, 6); 0, 0, 3 | Elliptic (7, 1, 6) | Elliptic (7, 1, 6) | 6.23×10⁻⁷ / 1.01×10⁻⁹ |
| 1 | Elliptic (7, 1, 6); 0, 0, 3 | Elliptic (7, 1, 6) | Elliptic (7, 1, 6) | 1.23×10⁻⁶ / 2.82×10⁻⁹ |
| 1.41 | Elliptic (7, 1, 6); 0, 0, 3 | Elliptic (7, 1, 6) | Elliptic (7, 1, 6) | 2.43×10⁻⁶ / 7.81×10⁻⁹ |
| 2 | Elliptic (7, 1, 6); 0, 0, 3 | Elliptic (7, 1, 6) | Elliptic (7, 1, 6) | 4.78×10⁻⁶ / 2.15×10⁻⁸ |
| 2.83 | Elliptic (7, 1, 6); 0, 0, 3 | Elliptic (7, 1, 6) | Elliptic (7, 1, 6) | 9.30×10⁻⁶ / 5.84×10⁻⁸ |
| 4 | Elliptic (7, 1, 6); 0, 0, 3 | Elliptic (7, 1, 6) | Elliptic (7, 1, 6) | 1.79×10⁻⁵ / 1.56×10⁻⁷ |
| 5.66 | Hyperbolic (6, 1, 5); 1, 0, 2 | Hyperbolic (6, 1, 5) | Hyperbolic (6, 1, 5) | 3.42×10⁻⁵ / 4.12×10⁻⁷ |
| 8 | Hyperbolic (6, 1, 5); 1, 0, 2 | Hyperbolic (6, 1, 5) | Hyperbolic (6, 1, 5) | 6.43×10⁻⁵ / 1.06×10⁻⁶ |
| 11.31 | Hyperbolic (6, 1, 5); 1, 0, 2 | Hyperbolic (6, 1, 5) | Hyperbolic (6, 1, 5) | 1.20×10⁻⁴ / 2.70×10⁻⁶ |
| 16 | Hyperbolic (6, 1, 5); 1, 0, 2 | Hyperbolic (6, 1, 5) | Hyperbolic (6, 1, 5) | 2.21×10⁻⁴ / 6.79×10⁻⁶ |
| 22.63 | Hyperbolic (6, 1, 5); 1, 0, 2 | Hyperbolic (6, 1, 5) | Hyperbolic (6, 1, 5) | 4.07×10⁻⁴ / 1.69×10⁻⁵ |
| 32 | Hyperbolic (6, 1, 5); 1, 0, 2 | Hyperbolic (6, 1, 5) | Hyperbolic (6, 1, 5) | 7.38×10⁻⁴ / 4.12×10⁻⁵ |
| 45.25 | Hyperbolic (6, 1, 5); 1, 0, 2 | Hyperbolic (6, 1, 5) | Hyperbolic (6, 1, 5) | 0.00131 / 9.69×10⁻⁵ |
| 64 | Hyperbolic (6, 1, 5); 1, 0, 2 | Hyperbolic (6, 1, 5) | Hyperbolic (6, 1, 5) | 0.00226 / 2.18×10⁻⁴ |
| 72 | Hyperbolic (6, 1, 5); 1, 1, 1 | Hyperbolic (6, 1, 5) | Hyperbolic (6, 1, 5) | 0.00270 / 2.83×10⁻⁴ |

### T1 in `R5`

15 points, 15 classified as built and 15 changed.

| `ε` | Records at `N = 24`, 32, 40 | As built | Changed | Identity, 24 to 32 / 32 to 40 |
|---|---|---|---|---|
| 0.25 | Elliptic (2, 0, 2); 0, 0, 1 | Elliptic (2, 0, 2) | Elliptic (2, 0, 2) | 7.17×10⁻⁹ / 9.39×10⁻¹³ |
| 0.354 | Elliptic (2, 0, 2); 0, 0, 1 | Elliptic (2, 0, 2) | Elliptic (2, 0, 2) | 1.43×10⁻⁸ / 2.64×10⁻¹² |
| 0.5 | Elliptic (2, 0, 2); 0, 0, 1 | Elliptic (2, 0, 2) | Elliptic (2, 0, 2) | 2.84×10⁻⁸ / 7.39×10⁻¹² |
| 0.707 | Elliptic (2, 0, 2); 0, 0, 1 | Elliptic (2, 0, 2) | Elliptic (2, 0, 2) | 5.63×10⁻⁸ / 2.06×10⁻¹¹ |
| 1 | Elliptic (2, 0, 2); 0, 0, 1 | Elliptic (2, 0, 2) | Elliptic (2, 0, 2) | 1.11×10⁻⁷ / 5.73×10⁻¹¹ |
| 1.41 | Elliptic (2, 0, 2); 0, 0, 1 | Elliptic (2, 0, 2) | Elliptic (2, 0, 2) | 2.19×10⁻⁷ / 1.58×10⁻¹⁰ |
| 2 | Elliptic (2, 0, 2); 0, 0, 1 | Elliptic (2, 0, 2) | Elliptic (2, 0, 2) | 4.27×10⁻⁷ / 4.31×10⁻¹⁰ |
| 2.83 | Elliptic (2, 0, 2); 0, 0, 1 | Elliptic (2, 0, 2) | Elliptic (2, 0, 2) | 8.26×10⁻⁷ / 1.16×10⁻⁹ |
| 4 | Elliptic (2, 0, 2); 0, 0, 1 | Elliptic (2, 0, 2) | Elliptic (2, 0, 2) | 1.58×10⁻⁶ / 3.05×10⁻⁹ |
| 5.66 | Elliptic (2, 0, 2); 0, 0, 1 | Elliptic (2, 0, 2) | Elliptic (2, 0, 2) | 2.95×10⁻⁶ / 7.80×10⁻⁹ |
| 8 | Elliptic (2, 0, 2); 0, 0, 1 | Elliptic (2, 0, 2) | Elliptic (2, 0, 2) | 5.40×10⁻⁶ / 1.92×10⁻⁸ |
| 11.31 | Elliptic (2, 0, 2); 0, 0, 1 | Elliptic (2, 0, 2) | Elliptic (2, 0, 2) | 9.56×10⁻⁶ / 4.51×10⁻⁸ |
| 16 | Elliptic (2, 0, 2); 0, 0, 1 | Elliptic (2, 0, 2) | Elliptic (2, 0, 2) | 1.62×10⁻⁵ / 9.94×10⁻⁸ |
| 22.63 | Elliptic (2, 0, 2); 0, 0, 1 | Elliptic (2, 0, 2) | Elliptic (2, 0, 2) | 2.62×10⁻⁵ / 2.03×10⁻⁷ |
| 32 | Elliptic (2, 0, 2); 0, 0, 1 | Elliptic (2, 0, 2) | Elliptic (2, 0, 2) | 3.99×10⁻⁵ / 3.77×10⁻⁷ |

### The coherent row in `R5`

15 points, 15 classified as built and 15 changed.

| `ε` | Records at `N = 24`, 32, 40 | As built | Changed | Identity, 24 to 32 / 32 to 40 |
|---|---|---|---|---|
| 0.25 | Elliptic (0, 0, 0); 0, 0, 0 | Elliptic (0, 0, 0) | Elliptic (0, 0, 0) | 1.70×10⁻¹⁰ / 6.33×10⁻¹⁵ |
| 0.354 | Elliptic (0, 0, 0); 0, 0, 0 | Elliptic (0, 0, 0) | Elliptic (0, 0, 0) | 3.38×10⁻¹⁰ / 1.74×10⁻¹⁴ |
| 0.5 | Elliptic (0, 0, 0); 0, 0, 0 | Elliptic (0, 0, 0) | Elliptic (0, 0, 0) | 6.74×10⁻¹⁰ / 4.88×10⁻¹⁴ |
| 0.707 | Elliptic (0, 0, 0); 0, 0, 0 | Elliptic (0, 0, 0) | Elliptic (0, 0, 0) | 1.34×10⁻⁹ / 1.37×10⁻¹³ |
| 1 | Elliptic (0, 0, 0); 0, 0, 0 | Elliptic (0, 0, 0) | Elliptic (0, 0, 0) | 2.66×10⁻⁹ / 3.81×10⁻¹³ |
| 1.41 | Elliptic (0, 0, 0); 0, 0, 0 | Elliptic (0, 0, 0) | Elliptic (0, 0, 0) | 5.25×10⁻⁹ / 1.06×10⁻¹² |
| 2 | Elliptic (0, 0, 0); 0, 0, 0 | Elliptic (0, 0, 0) | Elliptic (0, 0, 0) | 1.03×10⁻⁸ / 2.92×10⁻¹² |
| 2.83 | Elliptic (0, 0, 0); 0, 0, 0 | Elliptic (0, 0, 0) | Elliptic (0, 0, 0) | 2.02×10⁻⁸ / 7.96×10⁻¹² |
| 4 | Elliptic (0, 0, 0); 0, 0, 0 | Elliptic (0, 0, 0) | Elliptic (0, 0, 0) | 3.90×10⁻⁸ / 2.14×10⁻¹¹ |
| 5.66 | Elliptic (0, 0, 0); 0, 0, 0 | Elliptic (0, 0, 0) | Elliptic (0, 0, 0) | 7.46×10⁻⁸ / 5.65×10⁻¹¹ |
| 8 | Elliptic (0, 0, 0); 0, 0, 0 | Elliptic (0, 0, 0) | Elliptic (0, 0, 0) | 1.40×10⁻⁷ / 1.45×10⁻¹⁰ |
| 11.31 | Elliptic (0, 0, 0); 0, 0, 0 | Elliptic (0, 0, 0) | Elliptic (0, 0, 0) | 2.57×10⁻⁷ / 3.60×10⁻¹⁰ |
| 16 | Elliptic (0, 0, 0); 0, 0, 0 | Elliptic (0, 0, 0) | Elliptic (0, 0, 0) | 4.59×10⁻⁷ / 8.54×10⁻¹⁰ |
| 22.63 | Elliptic (0, 0, 0); 0, 0, 0 | Elliptic (0, 0, 0) | Elliptic (0, 0, 0) | 7.88×10⁻⁷ / 1.91×10⁻⁹ |
| 32 | Elliptic (0, 0, 0); 0, 0, 0 | Elliptic (0, 0, 0) | Elliptic (0, 0, 0) | 1.29×10⁻⁶ / 4.00×10⁻⁹ |

### T5 in `R2`

31 points, 20 classified as built and 20 changed.

| `ε` | Records at `N = 24`, 32, 40 | As built | Changed | Identity, 24 to 32 / 32 to 40 |
|---|---|---|---|---|
| 0.25 | Elliptic (9, 3, 6); 0, 0, 3 | Elliptic (9, 3, 6) | Elliptic (9, 3, 6) | 2.56×10⁻⁷ / 2.36×10⁻¹⁰ |
| 0.354 | Elliptic (9, 3, 6); 0, 0, 3 | Elliptic (9, 3, 6) | Elliptic (9, 3, 6) | 5.11×10⁻⁷ / 6.67×10⁻¹⁰ |
| 0.5 | Elliptic (9, 3, 6); 0, 0, 3 | Elliptic (9, 3, 6) | Elliptic (9, 3, 6) | 1.02×10⁻⁶ / 1.88×10⁻⁹ |
| 0.707 | Elliptic (9, 3, 6); 0, 0, 3 | Elliptic (9, 3, 6) | Elliptic (9, 3, 6) | 2.03×10⁻⁶ / 5.29×10⁻⁹ |
| 1 | Elliptic (9, 3, 6); 0, 0, 3 | Elliptic (9, 3, 6) | Elliptic (9, 3, 6) | 4.03×10⁻⁶ / 1.48×10⁻⁸ |
| 1.41 | Elliptic (9, 3, 6); 0, 0, 3 | Elliptic (9, 3, 6) | Elliptic (9, 3, 6) | 8.00×10⁻⁶ / 4.16×10⁻⁸ |
| 2 | Elliptic (9, 3, 6); 0, 0, 3 | Elliptic (9, 3, 6) | Elliptic (9, 3, 6) | 1.58×10⁻⁵ / 1.16×10⁻⁷ |
| 2.83 | Elliptic (9, 3, 6); 0, 0, 3 | Elliptic (9, 3, 6) | Elliptic (9, 3, 6) | 3.11×10⁻⁵ / 3.21×10⁻⁷ |
| 4 | Elliptic (9, 3, 6); 0, 0, 3 | Elliptic (9, 3, 6) | Elliptic (9, 3, 6) | 6.07×10⁻⁵ / 8.83×10⁻⁷ |
| 5.66 | Elliptic (9, 3, 6); 0, 0, 3 | Elliptic (9, 3, 6) | Elliptic (9, 3, 6) | 1.17×10⁻⁴ / 2.40×10⁻⁶ |
| 8 | Elliptic (9, 3, 6); 0, 0, 3 | Elliptic (9, 3, 6) | Elliptic (9, 3, 6) | 2.24×10⁻⁴ / 6.41×10⁻⁶ |
| 11.31 | Elliptic (9, 3, 6); 0, 0, 3 | not classified | not classified | 4.20×10⁻⁴ / 1.68×10⁻⁵ |
| 16 | Elliptic (9, 3, 6); 0, 0, 3 | not classified | not classified | 7.67×10⁻⁴ / 4.24×10⁻⁵ |
| 22.63 | Elliptic (9, 3, 6); 0, 0, 3 | Elliptic (9, 3, 6) | Elliptic (9, 3, 6) | 0.00135 / 1.03×10⁻⁴ |
| 32 | Elliptic (9, 3, 6); 0, 0, 3 | Elliptic (9, 3, 6) | Elliptic (9, 3, 6) | 0.00228 / 2.37×10⁻⁴ |
| 45.25 | Elliptic (9, 3, 6); 0, 0, 3 | Elliptic (9, 3, 6) | Elliptic (9, 3, 6) | 0.00363 / 5.07×10⁻⁴ |
| 64 | Elliptic (9, 3, 6); 0, 0, 3 | Elliptic (9, 3, 6) | Elliptic (9, 3, 6) | 0.00545 / 0.00100 |
| 76 | Elliptic (9, 3, 6); 0, 0, 3 | Elliptic (9, 3, 6) | Elliptic (9, 3, 6) | 0.00651 / 0.00137 |
| 90.51 | Elliptic (9, 3, 6); 0, 0, 3 | Elliptic (9, 3, 6) | Elliptic (9, 3, 6) | 0.00769 / 0.00182 |
| 100 | Elliptic (9, 3, 6); 0, 0, 3 | Elliptic (9, 3, 6) | Elliptic (9, 3, 6) | 0.00842 / 0.00213 |
| 106 | Elliptic (9, 3, 6); 0, 0, 3 | Elliptic (9, 3, 6) | Elliptic (9, 3, 6) | 0.00886 / 0.00232 |
| 112 | Elliptic (9, 3, 6); 0, 0, 3 | Elliptic (9, 3, 6) | Elliptic (9, 3, 6) | 0.00928 / 0.00252 |
| 116 | Elliptic (4, 0, 4); 0, 0, 2 / Elliptic (9, 3, 6); 0, 0, 3 / Elliptic (9, 3, 6); 0, 0, 3 | not classified | not classified | 0.00956, fails / 0.00265 |
| 120 | Hyperbolic (4, 0, 4); 0, 1, 1 / Elliptic (9, 3, 6); 0, 0, 3 / Elliptic (9, 3, 6); 0, 0, 3 | not classified | not classified | 0.00983, fails / 0.00278 |
| 124 | Hyperbolic (4, 0, 4); 0, 1, 1 / Elliptic (4, 0, 4); 0, 0, 2 / Elliptic (4, 0, 4); 0, 0, 2 | not classified | not classified | 0.0101, fails / 0.00290 |
| 126 | Hyperbolic (4, 0, 4); 0, 1, 1 | not classified | not classified | 0.0102, fails / 0.00297 |
| 127 | Hyperbolic (4, 0, 4); 0, 1, 1 | not classified | not classified | 0.0103, fails / 0.00300 |
| 128 | Hyperbolic (4, 0, 4); 0, 1, 1 | not classified | not classified | 0.0104, fails / 0.00303 |
| 129 | Hyperbolic (4, 0, 4); 0, 1, 1 | not classified | not classified | 0.0104, fails / 0.00306 |
| 130 | Hyperbolic (4, 0, 4); 0, 1, 1 | not classified | not classified | 0.0105, fails / 0.00310 |
| 132 | Hyperbolic (4, 0, 4); 0, 1, 1 | not classified | not classified | 0.0106, fails / 0.00316 |

- **11.31,** both ways: the rule reads it Unresolved: partner set at -6.99597e-16+5.53881j (+1): the set's count differs between cutoffs.
- **16,** both ways: the rule reads it Unresolved: partner set at -2.7761e-15+5.36336j (+1): the set's count differs between cutoffs.
- **116,** both ways: the rule reads it Unresolved: structure: the type, indices, V0 or Krein counts differ along the ladder; tested set at -1.09137e-14+0.355471j (+2): the set's count differs between cutoffs; branch identity fails between N = 24 and 32: aligned distance 0.00956, the records differ.
- **120,** both ways: the rule reads it Unresolved: structure: the type, indices, V0 or Krein counts differ along the ladder; tested set at 4.50588e-15+0.326446j (+2): the set's count differs between cutoffs; branch identity fails between N = 24 and 32: aligned distance 0.00983, the records differ.
- **124,** both ways: the rule reads it Unresolved: structure: the type, indices, V0 or Krein counts differ along the ladder; tested set at 5.24784e-15+0.312519j (+1): the set's count differs between cutoffs; tested set at -2.54131e-15+5.03508j (+12): the set's count differs between cutoffs; branch identity fails between N = 24 and 32: aligned distance 0.0101, the records differ.
- **126,** both ways: the rule reads it Unresolved: tested group at 0.00750184+0.153725j: `U` = 3.88×10⁻³ exceeds one tenth of its distance to the imaginary axis, 7.50×10⁻⁴ (distance 7.50×10⁻³); branch identity fails between N = 24 and 32: aligned distance 0.0102, the records agree.
- **127,** both ways: branch identity fails between N = 24 and 32: aligned distance 0.0103, the records agree.
- **128,** both ways: branch identity fails between N = 24 and 32: aligned distance 0.0104, the records agree.
- **129,** both ways: branch identity fails between N = 24 and 32: aligned distance 0.0104, the records agree.
- **130,** both ways: branch identity fails between N = 24 and 32: aligned distance 0.0105, the records agree.
- **132,** both ways: branch identity fails between N = 24 and 32: aligned distance 0.0106, the records agree.

### T5's second member in `R2`

20 points, 15 classified as built and 16 changed.

| `ε` | Records at `N = 24`, 32, 40 | As built | Changed | Identity, 24 to 32 / 32 to 40 |
|---|---|---|---|---|
| 0.25 | Elliptic (9, 3, 6); 0, 0, 3 | Elliptic (9, 3, 6) | Elliptic (9, 3, 6) | 2.56×10⁻⁷ / 2.36×10⁻¹⁰ |
| 0.354 | Elliptic (9, 3, 6); 0, 0, 3 | not classified | Elliptic (9, 3, 6) | 5.11×10⁻⁷ / 6.67×10⁻¹⁰ |
| 0.5 | Elliptic (9, 3, 6); 0, 0, 3 | Elliptic (9, 3, 6) | Elliptic (9, 3, 6) | 1.02×10⁻⁶ / 1.88×10⁻⁹ |
| 0.707 | Elliptic (9, 3, 6); 0, 0, 3 | Elliptic (9, 3, 6) | Elliptic (9, 3, 6) | 2.03×10⁻⁶ / 5.29×10⁻⁹ |
| 1 | Elliptic (9, 3, 6); 0, 0, 3 | Elliptic (9, 3, 6) | Elliptic (9, 3, 6) | 4.03×10⁻⁶ / 1.48×10⁻⁸ |
| 1.41 | Elliptic (9, 3, 6); 0, 0, 3 | Elliptic (9, 3, 6) | Elliptic (9, 3, 6) | 8.00×10⁻⁶ / 4.16×10⁻⁸ |
| 2 | Elliptic (9, 3, 6); 0, 0, 3 | Elliptic (9, 3, 6) | Elliptic (9, 3, 6) | 1.58×10⁻⁵ / 1.16×10⁻⁷ |
| 2.83 | Elliptic (9, 3, 6); 0, 0, 3 | Elliptic (9, 3, 6) | Elliptic (9, 3, 6) | 3.11×10⁻⁵ / 3.21×10⁻⁷ |
| 4 | Elliptic (9, 3, 6); 0, 0, 3 | not classified | not classified | 6.07×10⁻⁵ / 8.83×10⁻⁷ |
| 5.66 | Elliptic (9, 3, 6); 0, 0, 3 | not classified | not classified | 1.17×10⁻⁴ / 2.40×10⁻⁶ |
| 8 | Elliptic (9, 3, 6); 0, 0, 3 | Elliptic (9, 3, 6) | Elliptic (9, 3, 6) | 2.24×10⁻⁴ / 6.41×10⁻⁶ |
| 11.31 | Elliptic (9, 3, 6); 0, 0, 3 | Elliptic (9, 3, 6) | Elliptic (9, 3, 6) | 4.20×10⁻⁴ / 1.68×10⁻⁵ |
| 16 | Elliptic (9, 3, 6); 0, 0, 3 | Elliptic (9, 3, 6) | Elliptic (9, 3, 6) | 7.67×10⁻⁴ / 4.24×10⁻⁵ |
| 22.63 | Elliptic (9, 3, 6); 0, 0, 3 | Elliptic (9, 3, 6) | Elliptic (9, 3, 6) | 0.00135 / 1.03×10⁻⁴ |
| 32 | Elliptic (9, 3, 6); 0, 0, 3 | Elliptic (9, 3, 6) | Elliptic (9, 3, 6) | 0.00228 / 2.37×10⁻⁴ |
| 45.25 | Elliptic (9, 3, 6); 0, 0, 3 | Elliptic (9, 3, 6) | Elliptic (9, 3, 6) | 0.00363 / 5.07×10⁻⁴ |
| 64 | Elliptic (9, 3, 6); 0, 0, 3 | Elliptic (9, 3, 6) | Elliptic (9, 3, 6) | 0.00545 / 0.00100 |
| 90.51 | Elliptic (9, 3, 6); 0, 0, 3 | Elliptic (9, 3, 6) | Elliptic (9, 3, 6) | 0.00769 / 0.00182 |
| 128 | Hyperbolic (4, 0, 4); 0, 1, 1 | not classified | not classified | 0.0104, fails / 0.00303 |
| 132 | Hyperbolic (4, 0, 4); 0, 1, 1 | not classified | not classified | 0.0106, fails / 0.00316 |

- **0.354,** as built: the rule reads it Unresolved: partner set at 3.63051e-16+6.01021j (+1): non-contracting above the floor.
- **4,** both ways: the rule reads it Unresolved: partner set at -4.77373e-16+5.84336j (+1): the set's count differs between cutoffs.
- **5.66,** both ways: the rule reads it Unresolved: partner set at -5.73596e-16+5.77108j (+1): the set's count differs between cutoffs.
- **128,** both ways: branch identity fails between N = 24 and 32: aligned distance 0.0104, the records agree.
- **132,** both ways: branch identity fails between N = 24 and 32: aligned distance 0.0106, the records agree.

## 5. T4's change of type in `R4`

The locator ran on (4, 5.66), Elliptic to Hyperbolic, with `n(L)` 7 and 6 at its ends, each midpoint solved from both ends of the current interval and read. The types below come from the records of the accepted midpoint solves, not from classified points. **`n(L)` changes from 7 to 6 inside [5.588897, 5.592133] at `N = 24`, 32 and 40; the change of type is not located; K1 stopped the bisection at 5.590515 and at the moved point 5.590192, at every cutoff.** The interval is not identified with the genuine index crossing. Its width, 0.00323604, is 0.000579 of its lower end, where completing asks below 0.0005.

| Midpoint | Records at `N = 24`, 32, 40, both solves | K1 | `n(L)` |
|---|---|---|---|
| 4.828427 | Elliptic (7, 1, 6) | holds | 7 |
| 5.242641 | Elliptic (7, 1, 6) | holds | 7 |
| 5.449747 | Elliptic (7, 1, 6) | holds | 7 |
| 5.553301 | Elliptic (7, 1, 6) | holds | 7 |
| 5.605078 | Hyperbolic (6, 1, 5) | holds | 6 |
| 5.579189 | Elliptic (7, 1, 6) | holds | 7 |
| 5.592133 | Hyperbolic (6, 1, 5) | holds | 6 |
| 5.585661 | Elliptic (7, 1, 6) | holds | 7 |
| 5.588897 | Elliptic (7, 1, 6) | holds | 7 |
| 5.590515 | Unresolved (6, 1, 5) / Unresolved (6, 2, 4) / Unresolved (6, 2, 4) | fails | 6 |
| 5.590192 (moved) | Unresolved (7, 1, 6) | fails | 7 |

Outside the locator's rule, and deciding nothing (`dev/runs/013_locator_reading/`, INFERRED): the eigenvalue of L that changes sign, on a straight line through the accepted midpoints near the interval, crosses zero at 5.590415 at `N = 24` and 5.590470 at 32 and 40. K1 cannot hold where A's eigenvalue on that mode lies within three margins of zero, a neighbourhood 9.3×10⁻⁴, 1.7×10⁻³ and 2.6×10⁻³ wide around that zero at `N = 24`, 32 and 40, where a completed interval must be narrower than 2.8×10⁻³. Both refused points lie inside it at every cutoff.

## 6. T5's top, on both ladders

T5's points above 90.51 on the first ladder, `N = 24`, 32 and 40, and on the second, `N = 32`, 40 and 48, each cutoff on its own path from the seed. The second ladder reads the nine points the first leaves open and the three classified points below them, 100, 106 and 112, as controls in the row. The records at 32 and 40 are the same reads on both ladders, read again before any read at 48 and found equal. On the second ladder no target is classified, because the controls at 100 and 106 are not, so each target's reading there is its raw one.

| `ε` | Records at `N = 24`, 32, 40, 48 | First ladder | Second ladder | The quartet's real part at 24 / 32 / 40 / 48 | Identity, 24 to 32 / 32 to 40 / 40 to 48 |
|---|---|---|---|---|---|
| 100 | Elliptic (9, 3, 6) at 24 to 48 | Elliptic (9, 3, 6) | not classified: a tested group does not contract | none / none / none / none | 0.00842 / 0.00213 / 2.72×10⁻⁴ |
| 106 | Elliptic (9, 3, 6) at 24 to 48 | Elliptic (9, 3, 6) | not classified: a tested group does not contract | none / none / none / none | 0.00886 / 0.00232 / 3.04×10⁻⁴ |
| 112 | Elliptic (9, 3, 6) at 24 to 48 | Elliptic (9, 3, 6) | Elliptic (9, 3, 6) | none / none / none / none | 0.00928 / 0.00252 / 3.37×10⁻⁴ |
| 116 | Elliptic (4, 0, 4) at 24; Elliptic (9, 3, 6) at 32 to 48 | not classified: the structure differs along the ladder; a tested set's count changes; identity fails, 24 to 32, the records differ | raw: converged, Elliptic (9, 3, 6) | none / none / none / none | 0.00956, fails / 0.00265 / 3.59×10⁻⁴ |
| 120 | Hyperbolic (4, 0, 4) at 24; Elliptic (9, 3, 6) at 32 to 48 | not classified: the structure differs along the ladder; a tested set's count changes; identity fails, 24 to 32, the records differ | raw: converged, Elliptic (9, 3, 6) | 0.0944 / none / none / none | 0.00983, fails / 0.00278 / 3.81×10⁻⁴ |
| 124 | Hyperbolic (4, 0, 4) at 24; Elliptic (4, 0, 4) at 32 to 48 | not classified: the structure differs along the ladder; a tested set's count changes; identity fails, 24 to 32, the records differ | raw: converged, Elliptic (4, 0, 4) | 0.1688 / none / none / none | 0.0101, fails / 0.00290 / 4.04×10⁻⁴ |
| 126 | Hyperbolic (4, 0, 4) at 24 to 40; Elliptic (4, 0, 4) at 48 | not classified: `U` above a tenth of the distance to the imaginary axis; identity fails, 24 to 32, the records agree | raw: the structure differs along the ladder; a tested set's count changes; identity fails, 40 to 48, the records differ | 0.1953 / 0.0309 / 0.0075 / none | 0.0102, fails / 0.00297 / 4.15×10⁻⁴, fails |
| 127 | Hyperbolic (4, 0, 4) at 24 to 48 | not classified: identity fails, 24 to 32, the records agree | raw: converged, Hyperbolic (4, 0, 4) | 0.2072 / 0.0717 / 0.0649 / 0.0634 | 0.0103, fails / 0.00300 / 4.21×10⁻⁴ |
| 128 | Hyperbolic (4, 0, 4) at 24 to 48 | not classified: identity fails, 24 to 32, the records agree | raw: converged, Hyperbolic (4, 0, 4) | 0.2183 / 0.0965 / 0.0913 / 0.0902 | 0.0104, fails / 0.00303 / 4.26×10⁻⁴ |
| 129 | Hyperbolic (4, 0, 4) at 24 to 48 | not classified: identity fails, 24 to 32, the records agree | raw: converged, Hyperbolic (4, 0, 4) | 0.2289 / 0.1159 / 0.1116 / 0.1106 | 0.0104, fails / 0.00306 / 4.32×10⁻⁴ |
| 130 | Hyperbolic (4, 0, 4) at 24 to 48 | not classified: identity fails, 24 to 32, the records agree | raw: converged, Hyperbolic (4, 0, 4) | 0.2389 / 0.1325 / 0.1285 / 0.1277 | 0.0105, fails / 0.00310 / 4.38×10⁻⁴ |
| 132 | Hyperbolic (4, 0, 4) at 24 to 48 | not classified: identity fails, 24 to 32, the records agree | raw: converged, Hyperbolic (4, 0, 4) | 0.2577 / 0.1603 / 0.1568 / 0.1560 | 0.0106, fails / 0.00316 / 4.49×10⁻⁴ |

- **The controls in the row.** At 100 and 106 the records keep Elliptic (9, 3, 6) at `N = 32`, 40 and 48, with nothing unresolved, K1 holds and branch identity holds on both pairs, but the rule reads each Unresolved, as built and changed alike, on one Krein-negative imaginary group, "non-contracting above the floor": at 100, the group at 0.3938i steps 3.59×10⁻⁵ from 32 to 40 and 3.68×10⁻⁵ from 40 to 48, above the floor of 1.30×10⁻⁵, and lies 0.394 from the nearest event, A's gray zone; at 106, the group at 0.3742i steps 3.12×10⁻⁵ from 32 to 40 and 5.34×10⁻⁵ from 40 to 48, above the floor of 1.35×10⁻⁵, and lies 0.374 from the nearest event, A's gray zone. With no shrinking step the rule shows no rate. At 112 the same group steps 7.78×10⁻⁴ and then 1.93×10⁻⁴, and the point is classified, Elliptic (9, 3, 6). On the first ladder all three were classified. Why the steps at 100 and 106 stop shrinking is OPEN.
- **The quartet.** From 127 to 132 its real part falls at every step from `N = 24` to 48, its step from 40 to 48 0.216 to 0.227 of its step from 32 to 40. On that ratio its limit would be about 0.0629 at 127, 0.0899 at 128, 0.1103 at 129, 0.1274 at 130, 0.1558 at 132 (INFERRED: three cutoffs cannot show the rate).
- **The change of type.** By the records it lies between 116, Elliptic (4, 0, 4), and 120 at `N = 24`; between 124, Elliptic (4, 0, 4), and 126 at `N = 32`; between 124, Elliptic (4, 0, 4), and 126 at `N = 40`; between 126, Elliptic (4, 0, 4), and 127 at `N = 48`. On the collision law, the real part squared linear in `ε` over the Hyperbolic points above 64, it sits at 118.078 at `N = 24`, 125.752 at `N = 32`, 125.969 at `N = 40`, 126.001 at `N = 48`, with a limit of about 126.01 on the last three (INFERRED; the rate is not shown).

## 7. Stated before the reads, and what they found

Each statement was made before any value it concerns was read, from known outcomes, all INFERRED and none a classification: `run/DESIGN.md` section 6 before the first ladder, `run/TOP48.md` section 5 before the second. Each stands as stated.

| Where | Stated | Found | |
|---|---|---|---|
| `DESIGN.md` § 6 | The twelve keep their stored type and indices at `N = 40` | 12 of 12 | held |
| `DESIGN.md` § 6 | The quartet's real part at `N = 40`: 0.035 to 0.053 at 128, 0.116 to 0.136 at 132 | 0.0913 and 0.1568, above every law | missed |
| `DESIGN.md` § 6 | 132 off the axis at `N = 40`, 128 too close to call | 132 off the axis, and 128 off it too | held, 128 called |
| `DESIGN.md` § 6 | The collision near 127 at `N = 40`, with a limit of 127.5 to 128 | between 124 and 126; 125.97 on the collision law (INFERRED) | missed |
| `DESIGN.md` § 6 | An Elliptic stretch with `K` = 4 before the quartet | at 116 at `N = 24`; at 124 at `N = 32`; at 124 at `N = 40` | held |
| `DESIGN.md` § 6 | No new link at `N = 40` alone at a stored point of the rows | none at a stored point; the one new link at `N = 40` alone is T5's second member's at 0.354, which no record holds (`dev/runs/011_row_readings/`) | held |
| `TOP48.md` § 5 | The design's laws at `N = 48`, as pinned: 0.0288, −0.0015 and 0.0420 at 128, 0.1159, 0.0925 and 0.1311 at 132 | 0.0902 and 0.1560 | missed again, as stated |
| `TOP48.md` § 5 | The same laws on `N = 24`, 32 and 40: the real part at 48, 0.0643 to 0.0647 at 127; 0.0909 to 0.0912 at 128; 0.1112 to 0.1115 at 129; 0.1282 to 0.1284 at 130; 0.1565 to 0.1567 at 132 | 0.0634, 0.0902, 0.1106, 0.1277, 0.1560 | missed, each below its range |
| `TOP48.md` § 5 | The real part's step from 40 to 48, about 1×10⁻⁴ to 7×10⁻⁴ | 7.5×10⁻⁴ to 1.5×10⁻³ | missed |
| `TOP48.md` § 5 | The collision at 125.98 at `N = 48` | between 126 and 127 by the records; 126.00 on the collision law (INFERRED) | missed |
| `TOP48.md` § 5 | The types at `N = 48`: Elliptic (9, 3, 6) at 116 and 120, Elliptic (4, 0, 4) at 124, Hyperbolic (4, 0, 4) from 126, 126 too close to call | as stated, but at 126, Elliptic (4, 0, 4) | held but at 126 |
| `TOP48.md` § 5 | Branch identity at (40, 48), 5×10⁻⁴ to 9×10⁻⁴ | 2.7×10⁻⁴ to 4.5×10⁻⁴, kept but at 126, where the records differ | missed, under the range |
| `TOP48.md` § 5 | The tolerances at `N = 48`: no gap between τ(40) and τ(48); A's smallest eigenvalue outside the cluster at least 200 times its gray zone's top; L's gray zone at least 10⁷ times clear; nothing in n(D)'s inherited zone | no gap; at least 211 times; at least 1.4×10⁷ times; nothing, from each point's records at 40 and 48 | held |
| `TOP48.md` § 5 | The branch: T5's path at `N = 48` reaches 132 on the branch it holds at 32 and 40 | branch identity at (40, 48) kept at every point but 126, where the record's type changes from `N = 40`'s | held but at 126 |

## 8. What stays open

Each with its values at every cutoff in the tables above, and its cause.

- **T4's change of type in `R4`,** between 4 and 5.66: not located, the stop in § 5.
- **T5 at 11.31 and 16** on the first ladder (§ 4).
- **T5's second member at 0.354, 4, 5.66, 128 and 132** on the first ladder (§ 4), 0.354 as built alone.
- **T5's top, 116 to 132:** not classified on the first ladder (§ 4), nor on the second, where the controls at 100 and 106 are not classified (§ 6).
- **Why the steps at 100 and 106 stop shrinking** on the second ladder: OPEN.

## 9. Deviations, and looks beyond the terms

- **None in the runs.** Each stage ran from its pinned tree, in its terms' order, and every job completed once.
- **Looks beyond the terms.** Between the two pins at `N = 48`, `run/TOP48.md` allows checks on each seed's check and each point's acceptance alone. `dev/runs/015_solve_checks_48/` also sets each point's reached amplitude against its record at `N = 40`, deciding nothing, and says so. After the reads, beyond the terms and deciding nothing: the quartet's limit on the ratio of its last two steps (§ 6), and the zero of L's sign-changing eigenvalue with K1's neighbourhood around it (§ 5), each INFERRED.
- **The statements in § 7** stand as stated, and their misses are kept.

## 10. Reproduction

From a copy of this folder whose `run/out/` also holds the bench's read and reading files:
- `shasum -a 256 -c SHA256SUMS`, and the manifest against `run/MANIFEST_PIN`;
- `python3 -I -B tools/build_record.py MIT_REPO --check`, which rebuilds this record from the files and the repository's history, recomputes each point's classification, and reports any difference;
- `dev/runs/011_row_readings/`, `dev/runs/013_locator_reading/` and `dev/runs/015_solve_checks_48/`, each read from the same files.

Bitwise agreement on another machine is not claimed: this run's own comparisons are bit for bit on the machine in § 1, and elsewhere they agree to round-off (`DEVLOG.md`, entry 17).
