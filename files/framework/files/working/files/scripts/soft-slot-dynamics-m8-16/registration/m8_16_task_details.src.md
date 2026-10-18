# M8.16: QUALIFYING THE STATIONARY HARMONIC GALERKIN INSTRUMENT, a pre-registered continuation and linear-spectrum record under the frozen slot action

Pre-registration, for review. It governs nothing until the maintainer's go. **No sealed case is solved before the freeze:** not the pyramid at any amplitude, and no census target row. Only development cases run, each logged with its script's SHA-256 and disclosed below (§ The split).

## TASK PLANNING

### The question

The author's [Slot Dynamics Census]({{CEN_URL}}) (commit `{{CEN}}`) lists four rows, born elliptic, that M8.15's finite-element instrument could not settle: `v₂` (T1), the third outside orbit (T4), the prism in `R4`, and T5's upper window. Its leading diagnosis for the first three is the mesh's breaking of right `SU(2)`.
- The rotations of a branch, its structural zero modes, lift off zero.
- At the smallest amplitude, a genuine slow mode lying nearly in their plane then merges with the lifted pair.
- M8.15.x's qualification measured that merger on a case outside the targets, the pyramid in `R4` ([`RESULT_2.md`]({{QX_URL}}/RESULT_2.md)).

A discretization that keeps the symmetry exactly keeps the structural modes at zero, and its genuine near-zero modes are then separated from them by eigenvalue (DERIVED, the census, § IV). [#512](https://github.com/openwave-labs/openwave/discussions/512#discussioncomment-18955679) admitted one, a stationary harmonic Galerkin instrument, inside a stated boundary (below).

This task asks one question: **does that instrument qualify?** The census's step 4 states what qualifying means, and this task registers it as written.
- **Before any target:**
  - the structural kernel at round-off on every control;
  - no lifted pair where the finite-element instrument measured one: the pyramid control, C2a and C2b;
  - the pyramid control's in-span mode resolved at the smallest amplitude, where the finite-element instrument merged it.
- **Then:**
  - Theorem D reproduced at a rigid slot;
  - Theorem R's slow frequencies at small amplitude on every census row;
  - agreement with M8.15's adjudicated ladders, where they decided.

If the in-span mode is not resolved while the kernel is exact, the diagnosis is wrong, and the program says so. A pass qualifies the instrument for the census run.

### Standing

- **The ruling it files under** is #512's answer of 2026-10-15. This task meets its conditions:
  - **identity:** M8.16 for the qualification, which is this task; the census run takes the next free ID;
  - **order:** the census run's pre-registration waits for M8.16's adjudication;
  - **word budget:** about {{WORDS}} words, inside `PR_REVIEW_STANDARDS.md` § 12.2's cap of about 8,000;
  - **maintainer reproduction,** for any claim that frozen text is defective (§ Ownership);
  - **the roadmap:** both M8 status rows record M8.16 in the pull request that files it.
- **Run-before-write** (§ 12.2) is met. M8.15.2 ran and was adjudicated on 2026-10-14 ([#632](https://github.com/openwave-labs/openwave/pull/632)). Since then the column has landed only that run's after-verdict records ([#633](https://github.com/openwave-labs/openwave/pull/633)) and housekeeping ([#635](https://github.com/openwave-labs/openwave/pull/635)).
- **ID.** The ruling fixes M8.16, which no M8 file or open pull request carries; the BACKLOG row this pull request creates allocates it (`ROADMAP_STANDARDS.md` § 6).

### The boundary (#512, § 3, verbatim)

{{BOUNDARY}}

Every case below runs inside it.

### What this task is not

- **Not the census run.** It decides no census row; the census run's own pre-registration does, after this one is adjudicated. So the ladders read the spectrum only at M8.15's decided points, and at the five undecided points the branch is solved for continuation alone (§ THE RUN).
- **No time integration and no persistence test,** per the boundary.
- **No M8.4 object.** None of M8.4's § 7 observables, its pre-registration, the slot-to-mass assignment, the mass table or any comparison target enters.
- **No slot relation, no mass, no particle state.** The slot action is MOTIVATED, an effective model, and M8.2's ceiling stays at row 6.
- **No re-test of theorems.** Theorems B, D and R are the author's. A disagreement with them at the smallest amplitudes indicts the instrument.
- **No re-reading of M8.15.** Its adjudicated verdicts stand as adjudicated. A disagreement between the two instruments is recorded as one, and what it means is the adjudication's to say.

### The split, and the development record

**The split, ruled on 2026-10-15 before any M8.16 code existed, with its amendments.** Author-side development runs only the GO list: synthetic and manufactured tests; Theorem D at the rigid slot `R3`; M8.15's controls C2a and C2b, joined the same day by C3, whose outcome Theorem R(b) and M8.15's unscored control ladder already give; and, by amendments of 2026-10-17, `R5`'s coherent branch, whose answer is Theorem R(c)'s and which also runs in the registered run as a control gating the `R5` rows only, and a check of each sealed seed on the lowest level only, of `Q(u)`, criticality and `(k, r_u)`, values the Result publishes, with no solve and no spectrum. SEALED until this pre-registration freezes: the pyramid control at every amplitude, its branch not solved at all; Theorem R's frequencies on the census target rows; and every unresolved census target, with M8.15's adjudicated ladders on the target rows. Every run, at every stage, stays off the trivial sector `R0` and on the slot action's nontrivial sectors. Every development run is logged with its script's SHA-256, its case and its outcome, including how it informed a tolerance, and is disclosed here. Development runs earn no qualification credit: their registered reruns below count as conformance and regression evidence, not as independent confirmation. After the freeze, every control runs against the criteria registered here, a failure stands as registered, and there is no repair-and-rerun under the M8.16 identity.

**What development ran, and what it informed.** The log, `DEVLOG.md`, is filed with the instrument, and `DESIGN.md` § 8 summarizes it.
- **D1 to D5 and DL:** the group, the basis, the quadrature's exactness, invariance, Newton on manufactured solutions, which set the acceptance bound, and the linear record on synthetic matrices and the Hamiltonian–Krein page's models, each with mutation arms.
- **D6:** Theorem D at `R3`. As first run it failed at `N = 24` and 32, from accumulation error in the cubic; with GEMM accumulation it passes at every `N` to 40.
- **D7:** C2a, C2b and C3 at `ε ∈ {0.5, 1, 2}`, and their full ladders at `N = 24` and 32, with `N = 40` at each ladder's top three points. All 121 ladder points are accepted, with the expected kernel, and the type, `K` and `k_i⁻` equal M8.15's control ladders at each.
- **Fitted or tested on these controls and on synthetic families, with mutation arms:** the calibration (§ FROZEN VALUES); the slow-pair demonstration, whose synthetic pairs down to `5×10⁻⁶`, at the controls' largest measured anisotropy, resolve at every mixing; and the convergence rule's factor and set rule (§ THE CONVERGENCE RULE).
- **Failures on record,** each standing as logged: the calibration's ten-fold headroom, missed at 2 of 40 synthetic mixings; a mutation arm first coded with two roles, corrected with the rule unchanged; C2a's sample, which failed on one-to-one matching and led to the set rule; and the dry run's two failures (§ BEFORE THE FREEZE).

### Ownership and run format

- **The author's agents build and run** the instrument under the frozen terms. They publish the scripts, data and records with a reproduction route (`REPRODUCE.md`).
- **The frozen terms' SHA-256 lands on MIT `main` before any sealed case runs,** on the census page, so the run can be checked against terms fixed in advance.
- **No obligation on the maintainers.** Reproduction is optional and declinable per run. A claim that frozen text is defective is reproduced by the maintainer with independent code before it is ratified (#512, § 4).
- **Adjudication** is the maintainer's, against the checks and rules below.

### Sources of record

| Source | What it supplies |
| --- | --- |
| MIT [`slot-action.md`]({{SA_URL}}) §§ I to VIII, at `{{SA}}` | the frozen law: the field equation, the energy, the charge, the slots |
| the same page, § IX's dated notes, at `{{SA9}}` | the fibre symmetry; stability stated relative to the stationary family |
| MIT [The Soft-Slot Branches]({{SSB_URL}}), at `{{SSB}}` | Lemma G; Theorem R; § IV's orbits, with representatives, values, signatures, `(k, r_u)` and slow spectra; the third outside orbit's certificate |
| MIT [The Slot Ground States]({{SGS_URL}}), at `{{SGS}}` | Theorems A, B and D |
| MIT [The Hamiltonian–Krein Identification]({{HKI_URL}}), at `{{HKI}}` | Theorem K, `k_r + 2k_c + 2k_i⁻ = n(L) − n(D)`, and the generalized kernel |
| MIT [The Slot Dynamics Census]({{CEN_URL}}), at `{{CEN}}` | step 4; the diagnosis; the rows |
| M8.15: its terms (OpenWave `{{M815T}}`), [`RECORD.md`]({{REC_URL}}) and branch records (MIT `{{REC}}`), and [#620](https://github.com/openwave-labs/openwave/pull/620) | the targets; the `ε` grid; the decided ladder points |
| M8.15.x's qualification, [`REGISTER_2.md`]({{QX_URL}}/REGISTER_2.md) and `RESULT_2.md` (MIT `{{QX}}`) | the pyramid control: its continuum slow spectrum and overlaps; the finite-element merger |
| #512, comment 18955679 | the admission and its conditions |

## SETTING

- **Units.** `R = c = g = 1` in every reported number.
- **The field equation.** `ψ` is a section of the slot bundle `E_ρ` over `X = S³/2I`, a field on `S³` with `ψ(γx) = ρ(γ)ψ(x)` for `γ ∈ 2I` acting on the left. It obeys `ψ_TT − Δψ + |ψ|²ψ = 0`, with `|·|` the fibre norm at each point.
- **Standing waves** are `e^{iωT}φ`, with `λ = ω²` (M8.15's `σ`). They solve `F′(φ) = 0`, where `F(φ) = ½⟨(−Δ − λ)φ, φ⟩ + ¼∫|φ|⁴`.
- **The soft slots' levels** are exact in this instrument:
  - `λ₀ = 48` in `R4` and `R5` (`K = 6`), and 63 in `R2` (`K = 7`);
  - the next levels where each slot occurs are 120, 80 and 195.
- **The amplitude** is `ε = λ − λ₀`. The window's top is `ε_max = λ₁ − λ₀`: 72 in `R4`, 32 in `R5` and 132 in `R2`, as in M8.15.
- **The leading order** (Theorem R). A slow eigenvalue is `ε κ s τ` at leading order:
  - `κ = 1/(8 √λ₀ Q(u))`, with each case's own `Q`;
  - `s = 9/16` in `R5` and 1 otherwise (OpenWave's D7);
  - `τ` is the frozen small-amplitude spectrum for unit `u` in `R4`'s `h` normalization (§ FROZEN VALUES).
- **Exact symmetries of the stationary problem:** right `SU(2)`; the phase, with charge conjugation in `R4` and `R5`; and `Sp(1)` in `R2`. Stability is stated relative to the stationary family (the slot action, § IX).

## THE INSTRUMENT, AND THE SEPARATION STATEMENT

**The basis.**
- At level `n` it is `f_{n,i,k}(x) = √(n+1) A_i π_n(x) e_k`, where:
  - `π_n` is the spin-`n/2` representation;
  - `e_k` is its weight basis;
  - `A_i` is an orthonormal basis of `Hom_2I(V_n, W_ρ)`, fixed canonically: the group average of the elementary matrices in a fixed order, then Gram–Schmidt, both applied twice.
- By Schur orthogonality the basis is orthonormal in `L²`, with the normalized measure, so the coefficients' own inner product is the `L²` product.
- The truncation keeps every level `n ≤ N`.
- By Peter–Weyl the truncated space is invariant under right `SU(2)` and the fibre group (DERIVED). That is the census's condition (a).

**The quartic, exactly.**
- **The rule.** A product rule in Hopf coordinates, `a = √t e^{iα}` and `b = √(1−t) e^{iβ}`, with `4N + 1` uniform nodes in each angle and `N + 1` Gauss–Legendre nodes in `t`.
- **Why it is exact.** It integrates every monomial of degree at most `4N` exactly (DERIVED). So `F`, its gradient and its Hessian on levels `≤ N` are exact to round-off.
- **Not collocation.** The scheme is variational Galerkin, the census's condition (b).
- **The full rule runs everywhere.** The optional order-10 reduction is not used.

**The exact kernel.** `F` is invariant to round-off on the truncated space. Differentiating that invariance twice at a critical point puts every orbit tangent in the Hessian's kernel to round-off (DERIVED): `T_aφ`, `iφ`, and in `R2` also `Jφ` and `iJφ`. No zero is inserted, and no mode is projected away.

**The solve, and the acceptance bound, settled here.**
- **Newton** runs on `(φ, λ)` at fixed `m = ‖φ‖²`, bordered by an orthonormal basis of the orbit tangents' span at the previous accepted point, its rank read by a pivoted QR. The multipliers vanish at a solution. The borders act only in the solve, and the spectrum is read on the unbordered `L`, the census's condition (c).
- **Acceptance.** Newton runs to its own round-off floor: once the residual is below `10⁻⁸` of the size before cancellation, `‖(−Δ)φ‖ + λ‖φ‖ + ‖|φ|²φ‖`, it steps until the residual stops halving, and keeps the smallest. A point is accepted only if that floor, the unbordered residual and the multipliers are each below `10⁻¹⁵` of that size.
- **Why `10⁻¹⁵`.** Every development point met it, the 121 ladder points of C2a, C2b and C3 included. A looser floor breaks each symmetry chain more, splitting it as the square root of the breaking: at `10⁻¹³` the split can reach the cluster's gray zone at the upper `ε`.

**Continuation,** in `m` with `ε` an output, as in M8.15. From the accepted point at `ε_{k−1}`, the seed is that point scaled to the predicted `m`, and a secant in `m` is iterated until `|ε − ε_k| ≤ 10⁻⁶`, at most 8 times. A secant slope that is not positive is a fold, which ends the branch at its last accepted point. A Newton failure, or a secant that does not reach `ε_k`, ends the branch there, with no retries.

**Seeds.** At `ε = 0.25` the case's representative on the lowest level (§ THE CASES), unit in the coefficient norm, is scaled to the leading-order norm `m = ε/Q(u)`. Before any solve it is checked: `Q(u)` against its exact value to `10⁻¹²` relative, criticality on the lowest level to `10⁻¹²`, and `(k, r_u)` from the orbit tangents and `σ` against the Result's. A failed check ends the case as an instrument failure. Every cutoff `N` is continued from its own seed, along the same targets.

**The linear record,** at every point where the spectrum is read (`DESIGN.md` § 7):
- **the spectrum:** the dense eigendecomposition of the first-order matrix `A = [[0, I], [−L, −2ωJ₀]]`;
- **the generalized kernel `V₀`:** the invariant subspace of the separated near-zero cluster, from an ordered real Schur form. Its dimension and the ranks of `A` and `A²` on it must equal the case's expected `V₀`; it must contain the exact symmetry directions, with their leak within `κ_L u‖A‖/gap`, capped at `10⁻⁴`; and the cluster must lie within the margin;
- **the groups:** outside the cluster, eigenvalues linked within `τ(λ) = max(margin, κ_d √(u‖A‖ |λ|))`, each typed real, imaginary or complex by its centre. An imaginary group's Krein signature comes from `B` on its eigenvectors, or from its real Schur subspace at a defective group, and a group carrying both signs is a collision within the resolution, reported unresolved;
- **the indices:** `n(L)` by inertia at `L`'s cut, with its gray zone; `n(D)` on `V₀`, its nullity checked against the number of Jordan chains; and Theorem K, `K = n(L) − n(D) = k_r + 2k_c + 2k_i⁻`, checked at every point;
- **the type:** Hyperbolic when a group off the imaginary axis by more than `τ` lies outside the cluster's gray zone and `V₀` is as expected; Elliptic only when nothing is unresolved; Unresolved otherwise. A balanced `K` never stands in for the type.

**The separation statement.**
- **On method the instrument overlaps the closed chassis,** as the ruling says plainly: continuation of named branches in a truncated harmonic basis, Newton on a bordered system, and the spectrum read on the unbordered Jacobian. What separates it is the ruling's list: a law it derives and pins itself; named branches, each with a theorem at the smallest amplitude; no time arm; M8.15's lineage; and a record that quotes the verdict, `M8.5-C2-FAILED`, instrument-attributed ([#506](https://github.com/openwave-labs/openwave/issues/506)). This task's results say nothing about that chassis in either direction.
- **The law** is derived in the instrument from the slot action's § V, with its own symbolic check of the first and second variations.
- **Nothing from `m8_5c/design_inputs/` or the C2 room has been opened.** The M8.5-C2 protocol's public text was read twice: §§ 0 to 3, 5 to 9 and Addendum 1, to state the overlap the ruling acknowledges; and § 4.1, after the design's first version was hashed, to check a review unit's comparison. The product rule has C2's production form, with `N + 1` Gauss–Legendre nodes in `t` where C2 used `2N + 1`; the design derives it.
- **M8.15's separation statement.** It excluded "truncation in harmonic space, or Galerkin projection onto a harmonic basis", and this instrument is such a truncation. #512, § 2 says that M8.15's statement stands as written, for the design M8.15 built, and reads the ruling more broadly than § 0 does. From here, § 3 governs.

**The instrument, fixed.** The code is frozen at a commit on MIT `main`, in `scripts/soft-slot-dynamics-m8-16/`, with `REPRODUCE.md` and `SHA256SUMS`. The manifest records the environment: Python 3.13.13, NumPy 2.5.0, SciPy 1.18.0, and Apple Accelerate's BLAS and LAPACK at default threading, on one Apple M3. Bitwise reproducibility is not claimed: every scored quantity is read against margins far above round-off variation, and the calibration's tail statistics vary across machines (§ STATED LIMITS).

## THE CASES

**The controls.** All are on the GO list except the pyramid.

| ID | slot | orbit (Condon–Shortley `v_m`) | `Q(u)` | `(n₋, n₀, n₊)` | `k, r_u` | expected `V₀`: dimension; ranks of `A`, `A²` | type; `(n(L), n(D), K)` at small amplitude |
| --- | --- | --- | --- | --- | --- | --- | --- |
| C1 | `R3` | Theorem D's fixed generic member, `v₁ + (0.6 + 0.3i) v₀ − 0.4i v₋₁`, normalized | 1 | n/a | 4, 2 | 6; 1, 0 | Elliptic; (0, 0, 0) |
| C2a | `R4` | coherent `v₃` | 1288/1287 | (0, 0, 10) | 3, 1 | 4; 1, 0 | Elliptic; (0, 0, 0) |
| C2b | `R2` | `v_{7/2}`, with complex structure `i` | 144/143 | (0, 0, 10) | 5, 1 | 6; 1, 0 | Elliptic; (0, 0, 0) |
| C3 | `R4` | octahedron `v₂ + v₋₂` | 175/143 | (6, 0, 3) | 4, 4 | 8; 4, 0 | Hyperbolic, three real pairs; (6, 3, 3) |
| C2a/R5 | `R5` | coherent `v₃`, the `R5` control | 2289/2288 | (0, 0, 10) | 3, 1 | 4; 1, 0 | Elliptic; (0, 0, 0) |
| P5 | `R4` | pyramid `√12 v₃ + √13 v₋₂` | 77/65 | (5, 0, 4) | 4, 2 | 6; 2, 0 | Hyperbolic: one quartet, one Krein-negative pair, one Krein-positive pair; (5, 1, 4) |

**The census rows,** sealed until the freeze. They are M8.15's frozen targets.

| ID | slots | orbit | `Q(u)` | `(n₋, n₀, n₊)` | `k, r_u` | expected `V₀` | type; `(n(L), n(D), K)` |
| --- | --- | --- | --- | --- | --- | --- | --- |
| T1 | `R4`, `R5` | `v₂` | 147/143, 581/572 | (2, 0, 8) | 3, 1 | 4; 1, 0 | Elliptic; (2, 0, 2) |
| T2 | `R4`, `R5` | prism `v₃ + √(23/10) v₀ + v₋₃` | 5831/5031, 609/559 | (3, 0, 6) | 4, 4 | 8; 4, 0 | Elliptic; (3, 3, 0) |
| T3 | `R4`, `R5` | hexagon `v₃ + v₋₃` | 1750/1287, 2751/2288 | (9, 0, 0) | 4, 4 | 8; 4, 0 | Elliptic; (9, 3, 6) |
| T4 | `R4`, `R5` | the third outside orbit, at its certified point | 1.185203461338846…, 1.104176947003101… | (7, 0, 2) | 4, 2 | 6; 2, 0 | Elliptic; (7, 1, 6) |
| T5 | `R2` | the member with complex structure `i` of `√(3/10) v_{7/2} + √(7/10) v_{−3/2}` | 22/13 | (9, 0, 0) | 6, 4 | 10; 4, 0 | Elliptic; (9, 3, 6) |

**Where the expected columns come from** (DERIVED, before any sealed case runs).
- **The soft-slot cases,** every case but C1, at nondegenerate orbits (`n₀ = 0`):
  - **`V₀`.** `ker A = ker L × {0}` is spanned by the `k` orbit tangents, and each direction in the `σ`-radical of their span carries a Jordan partner (the Result's hypothesis (Z); the Hamiltonian–Krein page). So `dim V₀ = k + r_u`, `A` has rank `r_u` on `V₀`, and `A² = 0` there. These equal the zero multiplicities M8.15 froze for its targets (4, 8, 8, 6 and 10) and for C2a, C2b and C3 (4, 6 and 8), and the 6 that M8.15.x froze for the pyramid.
  - **`n(L) = n₋` at small amplitude.** On the lowest level `L` is the reduced quartic's Hessian, with the orbit tangents in its kernel and the norm direction positive. Every higher level is positive below `ε_max`.
  - **Theorem R fixes the slow Krein structure.** `k_i⁻` counts the Krein-negative slow pairs, `k_c` the quartets and `k_r` the real pairs. Every fast pair is Krein-positive at small amplitude, as at `φ = 0`.
  - **Theorem K then gives `n(D) = n(L) − K`.** Each `n(D)` is at most `r_u`, the number of Jordan chains, as it must be.
- **C1 is the exception.** Its expected values are Theorem D's, as D6 registered them: the rigid family's five tangent directions, four of them the orbit's, and one partner, the phase's, so `V₀` has dimension 6 with `A` of rank 1, where the orbit alone has `r_u = 2`.
- **The development cross-check.** C1's, C2a's, C2b's and C3's rows are the ones D6 and D7 confirmed at every development point, and C2a/R5's the one its development sample confirmed.

**T5 is one member,** as in M8.15. Its verdict is not extended to the other members of its `Sp(1)` family.

**The representatives' coordinates.** The instrument's `e_k` on level `n` is the Condon–Shortley `|n/2, (n − 2k)/2⟩`, with no phase (§ BEFORE THE FREEZE). T4 is the Result's certified point, converted from its weighted coordinates `p_m` by the Result's own `w_m = p_m √((j+m)! (j−m)!)`, as M8.15's `pinned.py` converts it.

## THE CHECKS

### Before any target: global-control failures stop the run; C2a/R5 gates `R5` rows only

The controls' points are `ε ∈ {0.25, 0.5, 1, 2}` at `N = 16, 24` and 32, and C1's are Theorem D's (§ THE RUN).

**K1. The structural kernel at round-off, on every control.** At every point and cutoff:
- the point is accepted;
- `V₀` has its expected dimension and ranks, and contains the exact symmetry directions, with their leak within its bound;
- the zero cluster lies within the margin, separated from the rest of the spectrum.

**K2. No lifted pair: the pyramid, C2a and C2b.** At every point and cutoff, the slow band holds exactly the predicted slow modes and nothing else. The slow band is every group with `|λ|` at most twice the largest predicted slow eigenvalue at that `ε`.
- Each predicted mode is matched one to one, by class and Krein sign with multiplicity.
- Nothing outside the zero cluster lies within its gray zone.

**K3. The pyramid's in-span mode, resolved at the smallest amplitude.** This is the decisive check. At `ε = 0.25`, at every cutoff:
- **(a)** the point is accepted, and K1 and K2 hold there;
- **(b)** exactly one imaginary group of negative Krein signature lies in the slow band, definite, outside the gray zone, and within 5% of `0.25 κ τ_in`, where `τ_in` is the in-span mode's frozen value (§ FROZEN VALUES);
- **(c)** its static overlap is at least 0.9 with `span{T_xφ, T_yφ}` and at most 0.1 with `T_zφ`, both taken inside the rotation span with `iφ` and the phase partner's static part projected out, as M8.15.x's `control_2a.py` forms them: `T_zφ`'s projection there, and its complement. The overlap is the `L²` norm of the static part of the group's eigenvector projected onto the `L²`-orthonormalized span, over that part's norm: M8.15.x's registered `verdict.static_overlap`, by which its continuum survey predicts 0.997 and 0.000. Below `10⁻⁶` of `‖T_zφ‖` that projection is undefined and (c) fails; the fraction is reported at every cutoff, and a review unit, from the Result's coefficients alone, puts it near 0.987 at the sealed seed;
- **(d)** its separation, read from the three cutoffs (§ THE CONVERGENCE RULE), passes.

Its outcome is one of three:
- **Resolved:** (a) to (d) pass.
- **Not resolved, with the kernel exact:** (a) passes and (b), (c) or (d) fails. The diagnosis is wrong, and the program says so.
- **Instrument failure:** (a) fails. The point is not accepted, the kernel is not exact, or a lifted pair appears, and the diagnosis is untested.

Both failures stand as registered.

**K4. The controls' known answers.** This is conformance: development ran C1, C2a, C2b, C3 and `R5`'s coherent branch (§ The split).
- **C1, Theorem D,** as D6 registered it, at `N = 16, 24, 32` and 40 and `ε ∈ {0.5, 1, 2}`: the exact branch `c = √ε v`, `λ = λ₀ + ‖c‖²`, needing no solve, with its residual below `10⁻¹⁵` of the size and its cubic's part off the lowest level below `10⁻¹⁴`; the lowest level's spectrum Theorem D's to `10⁻¹⁰` relative, `2iω` twice and `i√(4ω² + 2ε)`; the record Elliptic, `(n(L), n(D), K) = (0, 0, 0)`, with five chains; and the type, `n(L)`, `K` and those eigenvalues, to `10⁻¹²`, unchanged in `N`.
- **C2a, C2b, C3 and C2a/R5,** at every point:
  - converged with the expected type and `(n(L), n(D), K)`;
  - at `ε = 0.25`, every predicted slow mode within 5% of `εκsτ`, matched as in K2;
  - the largest relative deviation at `ε = 0.25` smaller than at `ε = 2`.
- **The pyramid, at `ε = 0.25`:**
  - converged, Hyperbolic, with `(n(L), n(D), K) = (5, 1, 4)`;
  - its quartet and its Krein-positive pair each within 5% of leading order.

  Its readings at 0.5, 1 and 2 are reported, unscored, apart from K1 and K2.
- **C2a/R5's K1 and K4 gate the `R5` rows only** (§ THE RUN).

### Then, the census rows: no row's outcome stops another

**K5. Theorem R at small amplitude, on every row.** T1 to T4 in both slots, and T5. At `ε = 0.25`, at every cutoff:
- the point is accepted, with its seed check passed;
- `V₀` is as expected, under K1's conditions;
- every predicted slow mode is within 5% of `εκsτ`, matched as in K2;
- the point is converged, with the expected type and `(n(L), n(D), K)`.

At `ε = 0.5`, 1 and 2 the same readings, with each mode's deviation, are reported, unscored. Where K6 reads the same point, its scoring applies.

Every predicted slow mode is resolvable at `ε = 0.25` at `N = 32` (§ FROZEN VALUES). The smallest, T4's in `R5`, lies about {{T4R5_MARGINS}} margins outside the gray zone. So M8.15's per-mode resolution schedule is not needed.

**K6. Agreement with M8.15's adjudicated ladders, where they decided.** The ladders run on M8.15's grid, from 0.25 to each branch's last decided point, at `N = 16, 24` and 32 (§ THE RUN). M8.15 decided 79 points:

| branch | M8.15's decided points | undecided, not read here |
| --- | --- | --- |
| T2/R4 | Elliptic from 0.25 to 11.31 (12); Hyperbolic at 32, 45.25, 64 and 72 (4) | 16, 22.63 |
| T2/R5 | Elliptic at all 15, to 32 | none |
| T3/R4 | Elliptic at 17, to 72 | 32 (Invalid) |
| T3/R5 | Elliptic from 0.25 to 11.31 (12); Hyperbolic at 22.63 and 32 (2) | 16 |
| T5/R2 | Elliptic at 17: from 0.25 to 32, and at 64 and 90.51 | 45.25; 128 and 132 lie above the last decided point and are not run |

At each decided point the reading is one of three:
- **agrees:** converged, with branch identity kept, the type M8.15 decided, `K` equal to M8.15's `n(B) − n(B|G_tol)`, and `k_i⁻` equal to M8.15's;
- **disagrees:** converged, with branch identity kept, and the type, `K` or `k_i⁻` different;
- **unresolved:** otherwise.

**Branch identity,** at each read point, holds between `N = 24` and 32 when two conditions hold:
- the `N = 24` solution, embedded exactly in the `N = 32` basis, differs from the `N = 32` solution by at most `10⁻²` of its norm, with the difference's orbit-tangent components removed (UA's guard in D7);
- the two records' type, indices, Krein counts and `V₀` are equal.

**Scored, per branch:**
1. every point up to the last decided point is accepted at every cutoff;
2. no decided point disagrees;
3. every decided point with `ε ≤ 2` agrees: seven per branch.

**Reported, unscored:**
- the number that agree above 2;
- each unresolved reading's reason;
- each of M8.15's tracked slow eigenvalues, against the nearest here of its class, per unit `ε`, beside M8.15's own level-2 to level-3 change, as D7 read the controls.

**Why 2.** On the controls the rule converged at every point to 2.83, even at `N = 16` and 24, and on C2b and C3 well beyond. Above that, an unresolved reading near a window's top is the rule's honest outcome (§ STATED LIMITS). A disagreement anywhere is scored.

## THE CONVERGENCE RULE (as built, frozen)

A point's classification is converged when two things hold:
- its type, `n(L)`, `K`, `V₀` and each imaginary group's negative Krein count are the same at every cutoff;
- its eigenvalues pass the separation test below.

**Tested:**
- every typed group below half the band edge, `√(n₁(n₁+2)) − √λ`. Here `n₁` is the first level above the lowest truncation cutoff, `N = 16`, at which the slot occurs: {{N1_R2}} in `R2`, and {{N1_R4}} in `R4` and `R5`. It is where the lowest cutoff's basis first lacks modes that the higher cutoffs carry, not the slot's next level above `λ₀`;
- every Krein-negative or off-axis group, wherever it lies;
- each tested imaginary group's nearest group of opposite Krein sign.

**Matched** one to one and both ways across the cutoffs. A match is unique only if the next candidate is at least twice as far.
- **The set rule.** Where a group's one-to-one match fails and it has candidates of its own class and Krein sign, of any size, it and those competitors form a set. The set is closed under the same test at every cutoff, and its count is taken with multiplicity. Closures that share a group are one set, their union, so a set does not depend on which of its groups is read first, and every group to be read is read (§ BEFORE THE FREEZE).
- **A set matches** when that count agrees at every cutoff. Its change is the bottleneck distance, and its distance to an event is its nearest member's.
- **A missing partner,** or a changed count, reads Unresolved.

**The uncertainty `U`** is the largest of three:
- the remaining error `d₂²/(d₁ − d₂)`, from the changes `d₁` and `d₂` across the three cutoffs. It reads Unresolved where `d₂` does not contract and exceeds the margin;
- the larger margin of the two highest cutoffs' records, as a floor;
- the numerical estimate `‖P_g‖ max(‖R_g‖, u‖A‖)`. `P_g` is a spectral projector built from right eigenvectors, the left eigenvector at `λ` being `W x` at `−λ̄`, and it is usable only if its span, left-residual, conditioning and `P X = X` checks pass.

**The events:**
- the zero cluster's gray zone, at distance `|λ| − G·margin`;
- the imaginary axis, at `|Re λ|`, for a group off it;
- the nearest imaginary group of opposite Krein sign, for an imaginary group.

**The test:** `U ≤ d/10` for every tested group or set, with `d` the distance to its nearest event. Otherwise the point is Unresolved.

**The band edge's floor.**
- At the highest read point in each slot the band edge is {{BAND_R4}} in `R4` (`ε = 72`), {{BAND_R5}} in `R5` (`ε = 32`) and {{BAND_R2}} in `R2` (`ε = 90.51`), its least value. So every group below {{HALF_MIN}} is tested at every read point.
- The slot's next level, whose free frequency nears zero at a window's top, lies inside that band.
- The driver reads a point Unresolved if half its band edge falls within the zero cluster's gray zone (UA). In this plan it cannot.

**Reported beside it:** the relative change between the two highest cutoffs, against `10⁻⁶`, the provisional fraction that this rule retired as a gate.

## THE RUN

**The order:**
1. **The freeze** (§ FIXED AT THE FREEZE). No sealed case runs before the maintainer's go and the terms' hash on MIT `main`.
2. **The controls,** in order: C1, C2a, C2b, C3, then C2a/R5. A failed check of C1 to C3 stops the run. C2a/R5's never does: if it fails, T1 to T4 in `R5` are recorded as not qualified, with its failing check named, and are not run.
3. **The pyramid.** A failed check stops the run. The driver then writes the gate record, with K1 to K4.
4. **The rows:**
   - the samples of T1 and T4, in both slots;
   - the ladders of T2 and T3, in both slots, and of T5.

   The guard refuses a row until the gate record shows K1 to K4 passed.

**The points.**
- **C2a, C2b, C3, C2a/R5, P5, T1 and T4:** `ε ∈ {0.25, 0.5, 1, 2}`, continued in that order from the seed, at `N = 16, 24` and 32, each cutoff on its own path.
- **C1:** Theorem D's exact branch at `ε ∈ {0.5, 1, 2}`, at `N = 16, 24, 32` and 40.
- **T2, T3 and T5:** M8.15's grid, `ε_k = 0.25 × 2^{k/2}`, from 0.25 to the last decided point, at `N = 16, 24` and 32, each cutoff on its own path. The last decided points are 72 for T2/R4 and T3/R4, 32 in `R5`, and 90.51 for T5.
  - At the five undecided points the branch is solved and accepted for continuation, and no record is computed.
  - The grid's points at 0.25, 0.5, 1 and 2 serve K5.

**An interruption** (power, a crash) is resumed. The log records the manifest's SHA-256 at the start. A resume refuses a changed tree or a recorded stop, checks each completed case's outputs against their logged SHA-256, and reads its stop test again. Partial outputs move to `run/out/interrupted/`, unscored. The run is made on mains power, with sleep off.

**The cost (INFERRED, before the freeze).** Per point, at `N = 16, 24` and 32 together, nearly all of it at 32, development measured about 5.5 to 8 minutes in `R4` and 2.5 in `R2`. `R5` costs {{R5_LO}} to {{R5_HI}} times `R4`, measured on its coherent branch in development and in the dry run.

| phase | points | estimate |
| --- | --- | --- |
| the controls, C1 to C3 | 4 each; C1's 3 at four cutoffs | about {{H_CTRL}} h |
| C2a/R5 | 4 | about {{H_R5C}} h |
| the pyramid | 4 | about {{H_P5}} h |
| T1 and T4, `R4` | 8 | about {{H_S4}} h |
| T1 and T4, `R5` | 8 | about {{H_S5}} h |
| the ladders of T2 and T3, `R4` | 36 | about {{H_L4}} h |
| the ladders of T2 and T3, `R5` | 30 | about {{H_L5}} h |
| the ladder of T5 | 18 | about {{H_L2}} h |
| total | | about {{H_TOT}} h of compute |

The `R5` rows carry the most doubt: no `R5` ladder has run. On the registered driver, the dry run's controls' phase, C1 to C3 and C2a/R5, took {{DRY_CTRL}} h.

## THE VERDICT RULE, AND STOP CONDITIONS

- **The instrument qualifies** if K1 to K4 pass on C1 to C3 and the pyramid.
- **A row qualifies,** for the census run, if the instrument qualifies and the row passes K5, and also K6 where the row has a ladder; an `R5` row also needs C2a/R5's K1 and K4. A row that fails any of these is recorded as not qualified, with the failing check named.
- **The verdict** is one of two:
  - QUALIFIED, with the qualified rows named;
  - NOT QUALIFIED, with the failing check named.

  At a stop the verdict is NOT QUALIFIED, naming the failing check. If K3 fails with the kernel exact, the record says that the diagnosis is wrong.
- **A failure stands as registered.**
  - There is no repair-and-rerun under the M8.16 identity.
  - A defect claim in frozen text goes to maintainer reproduction (#512, § 4).
  - A revised instrument is a new pre-registration, under a new ID.
- **Validity.**
  - A point that breaks the acceptance bound, or a seed that fails its check, is invalid, and is never scored as agreeing.
  - Output produced outside the order above is quarantined, and is never scored.
- **No search.** Every computed number is reported, and nothing is tuned toward a target or toward M8.15. Any change to these terms after the go is a new pre-registration.

## STATED LIMITS

- **The convergence rule's limits.**
  - A slow rate hidden under a faster one is beyond any reading of a few cutoffs. A synthetic family at 15 margins, and another read from two cutoffs, both read converged.
  - The rule rests on the leading rate dominating at the highest cutoffs. The controls' rates there are at most 0.033.
  - Its factor is an operational adequacy test, not a bound on every spectral error.
  - Each next-level mode near zero at a window's top is not identified as such. Every group below half the band edge, at least {{HALF_MIN}} at every read point, is tested, so none is omitted.
- **The calibration's limits.**
  - The margin is fitted on the controls: their largest cluster coefficient, 0.0568 over 169 points, in `R2`, `R3` and `R4`, with `m` from 0.204 to 132 and `N` from 16 to 40. Outside that range it is an extrapolation, flagged in the record wherever it applies. `R5` lies outside the slots it was fitted on.
  - The ten-fold headroom holds on the controls, not throughout the synthetic stress family (§ The split).
  - `L`'s cut is an empirical calibration, not a universal error bound.
  - The slow-pair gate is the minimum demonstrated capability for slow pairs of the controls' structure. It is not proof that the sealed in-span mode will resolve.
- **`R5` has one development branch,** its coherent branch's sample (BOUNDARY.md's amendment 3), which runs again as the `R5` rows' gate (amendment 4). No `R5` target branch is solved before the freeze.
- **The smallest amplitude** is M8.15's `ε_min = 0.25`. Theorem R does not give the range of `ε` in which its leading order holds.
- **One discretization family.** Agreement is read across three cutoffs of one basis, and `N = 40` does not run on the rows.

## FROZEN VALUES

**Small-amplitude slow spectra** for unit `u` in `R4`'s `h` normalization (the Result, § IV). In `R5` they are multiplied by 9/16, and each case has its own `Q`.

| case | slow spectrum |
| --- | --- |
| C2a | `τ = 28/143, 56/429, 140/99, 112/39, 896/1287`, all Krein + |
| C2b | `τ = 112/143, 168/143, 336/143, 504/143, 560/143`, all Krein + |
| C2a/R5 | C2a's |
| C3 | a real pair at `√ν`, `ν = 250880/552123`, three times |
| P5 | the in-span pair, `τ_in = 0.0622348691`, Krein −; a quartet at `τ = 0.0417352860 + 0.0609168609 i`; `τ = 1.0951854883`, Krein + |
| T1 | `τ = 56/1287`, Krein −; `112/143, 112/117, 224/143, 560/429`, Krein + |
| T2 | `τ² = 5770240/7913763`; `19066880/278420571` twice; all Krein + |
| T3 | `τ² = 90160/61347`; `501760/552123` twice; all Krein − |
| T4 | `τ ≈ 1.01209160489`, Krein +; `0.310692742362, 0.139251832964, 0.00573685922309`, Krein −; all simple, from the certified point |
| T5 | `τ² = 153664/20449`, and `τ² = −ν` at the two roots of `418161601ν² + 6989958976ν + 28677390336`, with `ν = s²` the Result's variable: both roots are negative, so `τ ≈ {{T5_TAU_A}}` and `{{T5_TAU_B}}`; all Krein − |

- **P5's values** are the continuum's, from the reduced quartic at unit `u`, by M8.15.x's `continuum_overlap_survey.py` at MIT `{{QX}}`, and reproduced independently there by a review unit, with the overlaps 0.997 and 0.000 (`REGISTER_2.md`, § 2).
- **The predicted modes at `ε = 0.25`, and how far the smallest lies outside the gray zone at `N = 32`** (INFERRED, with `‖A‖ ≈ N(N+2)`):

{{RESOLUTION_TABLE}}

**The calibration** (`DESIGN.md` § 7), with `u = 2.22×10⁻¹⁶`, double precision's machine epsilon, as the code reads it:
- the margin `κ √(u‖A‖ max(m, m₀))`, with `κ = 2` and `m₀ = 0.2`, and its gray zone from `margin/G` to `G·margin`, with `G = 3`;
- the group link `κ_d = 10`;
- the leak bound's `κ_L = 200`, capped at `10⁻⁴`;
- `L`'s inertia cut `1000 u‖L‖`, with its gray zone to `G_L = 10` times it;
- `D`'s cut `10⁻⁸ ‖B‖`.

**The solve:** acceptance at `10⁻¹⁵`, the halving rule's threshold at `10⁻⁸`, the secant to `10⁻⁶` within 8 iterations, and the seed check at `10⁻¹²`.

**The checks:**
- 5% against leading order;
- the overlaps 0.9 and 0.1;
- the identity guard at `10⁻²`, and K3's axis guard at `10⁻⁶`;
- the separation factor 1/10, with the projector's checks: the span at `10⁻⁶`, the left residual at `10⁴ u`, the conditioning at `10⁻²/u`, and `P X = X` at `10⁻⁶`.

**The grid and the cutoffs:** `ε_k = 0.25 × 2^{k/2}`; `N = 16, 24` and 32, with C1 also at 40.

## BEFORE THE FREEZE

Done, on the GO list, each logged and disclosed in `DEVLOG.md`. None solved a sealed case or read a sealed spectrum.
- **The seeds.** The instrument's `e_k` is the Condon–Shortley `|n/2, (n − 2k)/2⟩`, with no phase. All 15 seeds, 10 sealed, equal the Result's representatives. On the lowest level only (BOUNDARY.md's amendment 2), `Q(u)` is within 3.2×10⁻¹⁵ of the Result's, criticality within 1.1×10⁻¹⁵, and `(k, r_u)` is the Result's.
- **`R5`'s coherent branch** (amendment 3): every point accepted, with `V₀` and the type as derived; every slow mode within 0.93% of leading order at `ε = 0.25`; every `ε` converged; and the calibration's conditions held, with no refit.
- **The registered driver** passed its guard's tests, none constructing or solving a sealed case. Its dry run failed twice before it closed. The first stopped at C2a, at `ε = 2`: the set rule's closure turned on the eigensolver's output order. A symmetric repair, previewed first, joined sets to the whole spectrum and was rejected; the closure took its present form (§ THE CONVERGENCE RULE). The rerun passed every check, but its claims code crashed on development records without eigenvalues. Scored from its kept outputs, against records saved before it ran, all six claims held.
- **The expected values** of § THE CASES go into `FROZEN.json` at the freeze.

## FIXED AT THE FREEZE

- **The order of the freeze:** `pin_manifest.py` writes `run/MANIFEST_PIN`; the pin is published on MIT `main` with the solver commit; the maintainer's go; `write_guard.py` writes `run/FROZEN.json` and `run/FROZEN_PIN`; the freeze block; the run. So the go covers the pinned instrument, and `write_guard.py` refuses any tree that differs from it.
- **The guard, the frozen allowlist.** `FROZEN.json` is written once, by `write_guard.py`, after the maintainer's go; the file is created exclusively, the driver never writes it, and its own SHA-256 is its pin. It holds:
  - the allowlist of the 15 cases, with each one's slot, representative, `Q`, `(k, r_u)`, expected `V₀`, expected type and indices, and frozen spectrum;
  - every point, with whether its spectrum is read;
  - the cutoffs and every frozen value above;
  - the terms' SHA-256, the go, and the instrument manifest's SHA-256;
  - the SHA-256 of M8.15's target records, copied by `write_guard.py` after the go only if each git blob id equals the one named before the freeze.
- **The driver refuses:**
  - any run under `python -O`;
  - any case not on the allowlist;
  - `R0`, always;
  - a sealed case when `FROZEN.json` is absent or differs from its pin, when its manifest hash is not the instrument's, or when its terms hash is not that of the terms file in the run folder;
  - a row before the gate record shows K1 to K4 passed. The gate record's SHA-256 is logged in the run's log when it is written;
  - a resume on a changed tree, or past a recorded stop (§ THE RUN).
- **The freeze block** (`research/m8_16/freeze_block.md`), all before the run:
  - the solver commit, the SHA-256 of every file in the manifest, and both pins;
  - the terms' SHA-256;
  - the environment;
  - the cases' seeds, each with its `Q(u)`, criticality and `(k, r_u)` against the Result's (§ BEFORE THE FREEZE);
  - `FROZEN.json` in full.
- **Provenance.** The solver commit, and a terms-hash line on the MIT census page, are provenance. The pre-registration itself is OpenWave's merge of this task and its BACKLOG row, and no sealed case runs before it.

## DEFINITION OF DONE

- **The record:** every point's readings at every cutoff; K1 to K6, each with its outcome; the gate record; and the logs. It is published with scripts, data and `REPRODUCE.md`, on MIT `main`.
- **Adjudication** by the maintainer, under the rule above.
- **Records,** all by the author:
  - a method note, equations first, with an equation-to-code map;
  - the roadmap's Done row, stating the maintainer's adjudicated verdict;
  - after the verdict, a dated note on the census page.
- **What follows.** The census run runs only the rows qualified here.
- **What does not move.** No `MODELS.md` cell, and M8.7's gate is unchanged.
