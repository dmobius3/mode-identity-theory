# The slot dynamics in time: the design

*Committed with the dated note on [the slot dynamics in time](../../slot-dynamics-time.md), and unedited once the prototype starts. Written before the prototype runs.*

## 0. What this is

This is MIT's own computation. It is outside M8. It reads MIT at `e0fd45bf`. Before it, nothing ran except a timing of the existing instrument's cubic (`timing/timing_r4.out`) and a check, at random points, of the identity of the basis that § 5 uses. Whether any of it may run in M8 is for OpenWave to rule.

## 1. What it is for

The Standing-Wave Branches leave the branches' dynamics to a sequel: "the response to perturbations over several directions, amplitudes and durations, time integration that keeps the continuous symmetry, and evolution near the bracketed changes of type", which "needs a new discretization first, since the Galerkin method was qualified without time integration" (§ 6.2). The sequel's question is whether the small-amplitude spectral types predict the response to perturbation: an elliptic branch staying near its family, a hyperbolic one leaving at its predicted rate, the effect of Krein-negative modes, and couplings the linear spectrum misses.

The prototype builds the instrument for that question and runs only cheap controls. It evolves no soft-slot branch. Of the census's rows it evolves only the rigid families, closed analytically, as exact controls.

## 2. The equation

The frozen slot action, unchanged (the paper's § 2.2): (1/c²)∂²_Tψ − Δψ + g₄|ψ|²ψ = 0 on ℝ × X, for ψ a section of E_ρ, in the Killing time T, with g₄ = 1 and units R = c = 1. No new clock and no new term.

In the instrument's basis (complete levels n ≤ N, orthonormal in the normalized measure, −Δ = n(n+2) on level n), with the real form q = (Re c, Im c) and p = q̇, the equation is Hamiltonian:

- H(q, p) = ½|p|² + ½qᵀKq + V₄(q), with K = diag(n(n+2)) and V₄(q) = ¼∫|ψ|⁴ dμ;
- q̈ = −Kq − ∇V₄(q), where ∇V₄ is the instrument's `cubic(c)`: "The Galerkin projection of |psi|^2 psi".

The overall factor vol(X), which the instrument drops, drops from the equations of motion as it does from the critical points. It enters only when an energy or a charge is reported in the paper's units.

A standing wave e^{iωT}φ is one of the instrument's critical points, at λ = ω². In its rotating frame, ψ = e^{iωT}(φ + ζ), the linearization is the instrument's own triple, ζ'' + 2iωζ' + Lζ = 0 (`linear.py`), with L = K − ω² + ∇²V₄(φ). A reader transforms both position and velocity: ζ = e^{−iωT}ψ − φ and ζ̇ = e^{−iωT}(ψ̇ − iωψ). So a frequency read in time, in that frame and demodulated at the scheme's own discrete rotation, compares with the linear record's eigenvalues up to O(h²). In R1, R2, R6 and R8 the frame is the member's own phase generator, which takes the place of J0, multiplication by i, in the triple (the paper's § 2.3).

## 3. Space: M8.16.1's instrument, at its frozen commit, unedited

Every script here imports `soft-slot-dynamics-m8-16-1/instrument/` and edits nothing in it. Those 12 files are the instrument M8.16.1 qualified, frozen at MIT `d1c0ec8` with its manifest pin `8cc2d7e2…`, and they are unchanged on main at `e0fd45bf`.

- `INSTRUMENT.sha256` holds the 12 files' SHA-256, computed from git at that commit. `pin.py` refuses to run if any imported file differs, or if the instrument folder holds anything else, `__pycache__` aside, rather than trusting whichever SHA256SUMS sits beside the import.
- MIT's own computation of the census's open items uses a copy that differs only in `convergence.py`, which takes it off that pin. No script here imports `convergence.py`.
- The time arm, the stepper and the FFT cubic, is new code. Neither M8.16.1's qualification nor the admission of 2026-10-15 covers it.

The instrument's rule is exact to degree 4N, so it computes the restricted functional, its gradient and its Hessian exactly.

**Symmetry (DERIVED from `basis.py`, `functional.py` and the Galerkin construction).** Each complete level is invariant under right translation, which acts on each (n, i) block by π_n. The phase acts pointwise. In the quaternionic slots R1, R2, R6 and R8, the structure J acts "level by level". The discrete V₄ is the exact restriction of ¼∫|ψ|⁴ to the truncation space. So it is invariant under right SU(2), the phase and, in those slots, Sp(1), and its gradient is equivariant. K commutes with every generator, because every generator preserves levels. In the real slots, charge conjugation is also an orthogonal symmetry commuting with K and with the nonlinear force: a discrete symmetry, with no continuous charge (the paper's § 2.3).

## 4. Time: the stepper

**The reference: Störmer–Verlet,** the finite-element instrument's scheme (`m8_15x_solver/integrate.py`), in velocity form:

- p ← p − (h/2)(Kq + ∇V₄(q));
- q ← q + h p;
- p ← p − (h/2)(Kq + ∇V₄(q)).

It takes one cubic per step, since the force at the end of a step is the next step's first force. It is explicit, second order, symmetric and symplectic.

**What it keeps exactly, in exact arithmetic (DERIVED).** Each conserved charge is J_D = pᵀDq for a real skew generator D with DK = KD; with D = J0 this is the paper's charge, Im(c†ċ). There are three kinds:

- the phase charge;
- the three right-SU(2) charges;
- in R1, R2, R6 and R8, the two further Sp(1) charges, generated by J and iJ (the paper's § 2.3).

Each substep keeps every J_D:

- the drift, because pᵀDp = 0;
- the kick, because ∇U(q)ᵀDq = qᵀKDq + ∇V₄(q)ᵀDq, where qᵀKDq = 0 (KD is skew) and ∇V₄(q)ᵀDq = 0 (the invariance of V₄).

The scheme commutes with every orthogonal map that commutes with the vector field, the real slots' charge conjugation among them. So evolving a transformed state gives the transformed evolution. In floating point both properties acquire numerical errors, whose accumulation is measured and gated over the control durations.

**What it does not keep.** The energy is not conserved. At fixed N and over a fixed finite duration, Verlet's energy error is O(h²) for a sufficiently regular bounded solution. Long-time near-conservation requires further hypotheses. Cohen, Hairer and Lubich, *Numer. Math.* 110 (2008) 113–143, treat Störmer–Verlet on spectral semi-discretizations of semilinear wave equations in a weakly nonlinear setting, by modulated Fourier expansions. Their step-size and non-resonance conditions were not checked here, and whether their result reaches this twisted-bundle Galerkin system is not established. So the energy is measured and gated (§ 8).

**Discrete frequencies.** Verlet carries a linear mode of frequency ω at ω̃ = (2/h) arcsin(hω/2). At the free-field limit of the step of § 5, the highest free mode has hω = 1.6, and its numerical frequency is 2 arcsin(0.8)/1.6 = 1.159 times the continuum's. So stability alone cannot choose the step.

In a rigid slot every lowest-level section has constant norm (the paper's § 2.4). On the orbit e^{iθ}φ the cubic is therefore exactly ‖c‖²c, and the force is linear in q. Started with the matched velocity, as `standing_velocity` sets it, the standing wave is carried as an exact rotation by 2 arcsin(hΩ/2) per step, with Ω² = n₀(n₀+2) + ‖c‖² (DERIVED). That control is exact to round-off. A control started from the continuum standing wave has an error of O(h²) instead, and both run, so that an exactly kept numerical wave cannot hide a wrong physical frequency.

**The alternative: a splitting with the exact linear flow.** It rotates each mode exactly at ω_j = √(n(n+2)) over h/2, kicks by −h∇V₄(q), then rotates again over h/2.

- It is symmetric and symplectic, and costs one cubic per step.
- It keeps the same charges exactly, because the linear flow commutes with every generator.
- Its free modes come out at exactly ω_j, and the linear part imposes no step bound.
- On a rigid orbit its map is linear too, so it carries the matched standing wave as an exact rotation by θ, with cos θ = cos(ω₀h) − (κh/2ω₀) sin(ω₀h), ω₀ = √(n₀(n₀+2)) and κ = ‖c‖² (DERIVED: the trace of R(h/2)·S·R(h/2)).
- Its risk is step-size resonance where hω_j nears a multiple of π, which filtered trigonometric integrators address (MOTIVATED).

**The rule that chooses (fixed here, before anything runs).** Verlet stays the reference in every case. The splitting is adopted for production only if, at equal wall-clock per unit of evolved time, its error on Theorem 3.7's frequencies read in time in R1 and R3 is at most a quarter of Verlet's, at a step with hω_max < π, below its first resonance. For a second-order method a factor of 4 is worth one step halving.

## 5. Step bound and margin

The step is fixed for the whole run before evolution, from a bound valid along it.

- For this basis Σ_j f_j(x)f_j(x)† = (m/r)I_r, with m the number of coefficients and r the fibre dimension. So sup|ψ|² ≤ (m/r)‖c‖² (DERIVED; the identity checked at random points to 10⁻¹⁴).
- The bound needs ‖c‖², and along a Verlet run H can exceed H(0) by up to 1/(1 − h²ω²/4), 2.78 at hω = 1.6. Verlet's exactly conserved linear energy, H̃ = ½Σ_j(p_j² + ω_j²(1 − h²ω_j²/4)q_j²) ≤ H(0), gives ‖c‖² ≤ C̄ = 2H(0)/((1 − 0.8²)λ₀) at the step below, with λ₀ the lowest level's n₀(n₀+2), fixed before evolution (DERIVED for the linear part; the stop rule covers the nonlinear rest).
- The pointwise Hessian of ¼|x|⁴ is |x|²I + 2xxᵀ, between 0 and 3|x|², so ω_max² ≤ N(N+2) + 3 sup|ψ|² (DERIVED).

Together, ω_max² ≤ ω̄² = N(N+2) + 3(m/r)C̄, and h = 0.8 · 2/ω̄, M8.19's margin, so that hω_j/2 ≤ 0.8 for every mode, as C̄ assumes. Its free part is N(N+2), so h < 0.0606 at N = 32. At small amplitude the bound adds little: h ≈ 0.048 at N = 32, about 21,000 steps for T = 1000.

- Power iteration on the instrument's `hess_apply` at λ = 0 reports the margin and never sets h, since it approaches ω_max from below.
- A run whose ‖c‖² exceeds C̄ stops, checked at every step, because the bound's premise has then failed.
- The step never changes within a run.
- At large amplitude the bound is conservative; a tighter certified bound, if the qualification needs one, is the qualification's to settle.

## 6. Range of N

The census read the Galerkin instrument at N = 16, 24 and 32, deciding at 24 and 32. MIT's own computation went on to 40 and 48. The sequel can use the same ladder, with 40 and 48 if the cost of § 7 allows. The prototype's controls run at N = 8 to 16, its FFT check to N = 32, and its cost runs at N = 16, 24 and 32. Convergence in time (step halving at fixed N) is tested apart from convergence in space (N-refinement at fixed h).

## 7. Cost, measured, and the FFT

**Measured** (`timing/timing_r4.out`; R4, on the machine that ran it, one cubic on a random state, after a first call):

| N | coefficients | rule nodes | basis tables | cached | one cubic |
|---|---|---|---|---|---|
| 16 | 50 | 71,825 | 0.17 GB | yes | 0.02 s |
| 24 | 138 | 235,225 | 1.56 GB | yes | 0.30 s |
| 32 | 316 | 549,153 | 8.33 GB | no | 8.0 s |

Above N = 24 the tables exceed the instrument's 2 GB cache and are rebuilt at every evaluation. A T = 1000 run at N = 32 in R4 is then about 21,000 × 8.0 s, about 46.7 hours, and the larger slots cost more (R8's tables are 31.5 GB).

**The FFT path (DERIVED from `basis.py`'s factorization; to be verified in the prototype).** The basis evaluates π_n at a t node as "pi_n(x)_{lk} = e^{i alpha (n - l - k)} e^{i beta (l - k)} d_{lk}", with d^n(φ) real. So at each t node, each fibre component of ψ on the node's M × M angular grid is a two-dimensional Fourier series in (α, β), with frequencies |p|, |q| ≤ N:

- Ĉ_g[r; p, q] = Σ_{n,i} √(n+1) A_{n,i}[r, l] d^n_{lk}(φ_g) c_{n,i,k}, where (l, k) = ((n − p + q)/2, (n − p − q)/2) is fixed by (n, p, q).
- A contribution enters only when l and k are integers in [0, n]. Contributions from different levels and intertwiner copies that share a frequency bin are summed.

With NumPy's default FFT normalization:

1. place Ĉ_g in the bins (p mod M, q mod M), with α along axis 0 and β along axis 1;
2. evaluate ψ on the grid as M² times `ifft2`;
3. form |ψ|²ψ, the density summed over the fibre components before it multiplies each one;
4. take `fft2` of it, divided by M²: the normalized coefficients F̂_g;
5. project: G_{n,i,k} = √(n+1) Σ_g w_g Σ_{r,l} conj(A_{n,i}[r, l]) d^n_{lk}(φ_g) F̂_g[r; n − l − k, l − k], with w_g the rule's Gauss weight `rule.wt[g]`.

The angular normalization 1/M² is applied once. The dense path's `node_weight(g)` already includes it, so it is never applied again to normalized coefficients. The traps to plant as mutation arms are a wrong transform sign, a misplaced negative frequency, an overwritten repeated bin, a missing conjugation of A, a doubled normalization and an aliased grid.

The forward transform is alias-free for the components needed. |ψ|²ψ has frequencies up to 3N, and an alias of a frequency |p| ≤ N would need |p′ − p| ≥ M = 4N + 1, more than |p′| + |p| ≤ 4N allows. At M = 4N + 1, the dense path's own grid, the FFT path computes the same finite sums, so in exact arithmetic it gives the same exact projection with the same symmetry. The rule is exact for any M ≥ 4N + 1, so a faster transform size may follow once equivalence is shown; it then agrees to round-off rather than as the same sums. The path needs no basis tables, only the d^n(φ_g), a few megabytes.

Its transforms cost some 2 to 3 × 10⁸ flop per cubic at N = 32 in R4, before the d-contractions. The dense path takes 8 × 10⁹ flop there, plus the tables' rebuild. This supplies an operation-count motivation for the FFT path. A T = 1000 run at N = 32 would take under an hour if the complete step, diagnostics included, averages about 0.17 s or less. Whether it does is to be measured. The scheduled diagnostics use the same Fourier assembly, for instance the quartic energy through the unchanged rule, so that they do not spend the saving. The instrument's dense cubic stays the reference: the FFT path is adopted only if it agrees with it to round-off.

## 8. The prototype's controls, before anything is read

**Inputs.**

- Multi-level states, not only lowest-level ones, so that the controls exercise shared frequency bins, intertwiner multiplicities and the coupling between levels.
- Positions and momenta chosen so that every charge that applies is nonzero at the start.
- A short nonlinear test in R2, beside R1 (rigid and quaternionic), R3 (rigid and real) and R4 (soft and real). R2 has the Sp(1) charges on states of non-constant norm. No R2 or R4 branch is evolved.
- In R4 the free modes sit off the lowest level, so that no control reads the reduced quartic's slow flow, which is the qualification's.

**Controls, in order:**

1. **The FFT cubic against the instrument's,** at N = 8 to 32, on random multi-level states and on a lowest-level state, in R1, R2, R3 and R4: a normalized discrepancy of at most 10⁻¹¹, with absolute errors recorded. Each mutation arm of § 7 turns it red.
2. **Energy and gradient:** the FFT cubic is the gradient of the quartic energy evaluated through the same assembly, and that energy equals the instrument's `energy`, each at most 10⁻¹¹ normalized.
3. **Free modes:** single-level states with the cubic switched off, so that only the scheme's dispersion is read: at (2/h) arcsin(hω_n/2) for Verlet and at ω_n for the splitting, within the ceiling of control 4.
4. **Reversibility:** evolving forward, then backward over the same steps, returns to the start within a fixed ceiling of 10⁻¹⁰, relative to |(q, p)|, with the floor recorded.
5. **The rigid standing waves,** in R1 and R3: each stepper's matched discrete wave within the ceiling of control 4, and the continuum-started wave converging at second order.
6. **Theorem 3.7's spectrum read in time,** in R1 and R3, under step halving, for both steppers: the quantity the rule of § 4 compares.
7. **Charges,** in R1, R2, R3 and R4: every applicable J_D within 10⁻¹⁰ relative to ‖D‖·|q|·|p|, a normalization that stays defined at zero charge, and reported against ten times a floor measured on a dry run.
8. **Equivariance,** under right SU(2), the phase, Sp(1) and, in the real slots, charge conjugation: within the ceiling of control 4.
9. **Convergence and energy:** halving ratios in [3.5, 4.5], read only where hω_max ≤ 0.5 and above the measured floor. Unperturbed controls carry the relative total-energy error |H(t) − H(0)|/H(0), at O(h²) under halving, with its secular drift (the absolute difference between the means over the last and first tenths of the observations) within 10⁻² of its largest oscillation. M8.15's gates, 0.25 E_η and 10⁻² E_η, are candidate tolerances only for perturbations of positive excess energy E_η, which the prototype does not run. Under linear Verlet at the step of § 5, a random multi-level state with momenta stays under C̄.
10. **Cost:** complete-step time with diagnostics, and peak memory, at N = 16, 24 and 32, for each stepper and each cubic.
11. **The finite-element cross-check,** last and report-only: M8.15.x's Verlet from the same initial data in R4 at small amplitude, compared where the mesh's symmetry lift is small. The finite elements keep the phase and Sp(1) but break right SU(2), so they are not an authority on the Galerkin instrument.

**Stopping and recording.** A failure of force equivalence (1, 2), reversibility (4), conservation (7), equivariance (8) or convergence (9) stops the controls after it, because a faster instrument that fails equivalence does not qualify. The splitting can be chosen by the rule of § 4 only after it has passed controls 3 to 9 itself. A failure is recorded as it stands; nothing is retuned without a new dated note.

The seeds, durations and normalizations are fixed in committed code before each control runs, and are never redrawn. Every run records Python, numpy, scipy and the platform. The dry run that measures the floors is the record's first entry, before any pass line is read. From the start the record says which results rest on new code: the stepper and the FFT cubic. The prototype also records the quadratic energy at each level, H_n^(2) = ½Σ_{j∈n}(|p_j|² + n(n+2)|c_j|²), as a diagnostic for later use, with no threshold.

## 9. What the prototype leaves to the qualification and to the sequel

- **The prototype** settles the instrument, the stepper rule, whether the FFT path is adopted, and the cost.
- **The qualification,** after OpenWave's ruling on time integration and with criteria frozen in its own dated note, tests the instrument on what is already established. It recovers the small-amplitude frequencies of Theorem 4.2 at every soft-slot branch, the hexagon's "one double frequency; Krein −" among them, and the known growth rates, and it establishes floors, durations and convergence in space.
- **The sequel** is the science: persistence, finite-amplitude instability, the next-order values of Proposition 4.7, mode coupling and transfer between levels. M8.1.3 reproduced Proposition 4.7's values as values of a formula, so a time read of them checks whether the formula is the next-order term.

Noted for the qualification and the sequel:

- A perturbation experiment compares against a reference trajectory under the same stepper, so that the carrier's numerical phase is not read as a departure from the family.
- The qualification measures the floor below which a next-order correction cannot be resolved, before the sequel fixes its amplitude ladder.
- A Krein sign is read from the signed quadratic form on the mode, never from a frequency.

## 10. Separations, in the 2026-10-15 boundary's own terms

The [boundary](https://github.com/openwave-labs/openwave/discussions/512#discussioncomment-18955679) separated the stationary instrument from the closed chassis. It used "nothing from `m8_5c/design_inputs/` or the C2 room"; it is "not a second qualification of the spectral chassis that `M8.5-C2-FAILED` closed"; and "M8.5-C2 does not rerun, no M8.4 observable enters, `M8.4-R1` never files, and its results say nothing about that chassis in either direction".

The time integrator takes the same separations, and it is what the boundary left outside: "time integration in a harmonic basis, which is the closed route's evolving half and needs a ruling on this thread". The prototype runs it on MIT, as MIT's own computation; the ruling is OpenWave's.

- It is built on M8.16.1's own instrument.
- No code in that instrument names `m8_5c`, and none of the new code will. The name appears only in the boundary's own text, in `.md` and `.json` records.
- No M8.4 observable enters, and its results say nothing about the closed chassis.

The census's twelve unclassified points are not read: "nothing is repaired and rerun under any ID" binds M8. What MIT computes in its own repository, the maintainer's condition "does not reach" ([#512, 2026-11-01](https://github.com/openwave-labs/openwave/discussions/512#discussioncomment-19339563)).

## 11. Where it lives

- **This folder,** `scripts/slot-dynamics-time/`: this design, the frozen `INSTRUMENT.sha256` with its check `pin.py`, the timing, and, as the prototype runs, the stepper, the FFT cubic, the controls with their mutation arms, a record built from logged outputs, and SHA256SUMS.
- **The page,** [`slot-dynamics-time.md`](../../slot-dynamics-time.md): the dated note, then the prototype's record, the qualification and, later, the science. The dynamics index lists it.
