# M8.16: `R5`'s coherent control, its expected values (2026-10-17)

Stated before the control runs, by BOUNDARY.md's amendment 3 and its note (UB): derived and logged as C2a's were in `EXPECTED_V0.md`. The control's driver reads the row only after its SHA-256 matches the one DEVLOG.md logged before the run.

## The row

| Control | Slot, state | E₀ (level, real dimension) | `Q(u)` | `(n₋, n₀, n₊)` | k, r_u | Nonzero slow pairs | type; `(n(L), n(D), K)` | `expected` |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| C2a/R5 (amendment 3) | R5, coherent v₃ | 6, 14 | 2289/2288 | (0, 0, 10) | 3, 1 | 5: τ = 28/143, 56/429, 140/99, 112/39, 896/1287, each times s = 9/16; all Krein + | Elliptic; (0, 0, 0) | dim 4, ranks [1, 0] |

## Where it comes from (DERIVED)

- **R5 is R4 with `q_J − 1` scaled by 9/16** (the Soft-Slot Branches, § IV), so its signatures and types are R4's, with every slow eigenvalue scaled by exactly 9/16. The coherent orbit in R5 therefore has C2a's signature (0, 0, 10), `(k, r_u) = (3, 1)`, and slow frequencies `τ × 9/16` in the `h` normalization.
- **`Q`.** The same rule gives `Q₅ = 1 + (9/16)(Q₄ − 1) = (9Q₄ + 7)/16`. From C2a's `Q₄ = 1288/1287` it gives 2289/2288. The rule reproduces the published R5 values of T1, T2 and T3 exactly (581/572, 609/559, 2751/2288), and T4's to double precision (`dev/seed_check.py`, claim 4).
- **The physical slow eigenvalues** at leading order are `ε κ s τ`, with `κ = 1/(8 √48 Q₅)` and `s = 9/16`.
- **`V₀` and the indices** are C2a's, by `EXPECTED_V0.md`'s rule: dimension `k + r_u = 4`, ranks [1, 0]; `n(L) = n₋ = 0`; `K = 0`, every slow pair being Krein-positive (Theorem R(c)); so `n(D) = 0`.
- **E₀.** R5 occurs once at level 6, by 2I's characters (D1), so E₀ has real dimension 14.

## After it runs (BOUNDARY.md's note)

The control reports its cluster coefficient, `L`'s kernel and the convergence rule's readings against the calibration as it stands. No constant is refitted on it unless one of the calibration's own conditions fails, and any change is disclosed.
