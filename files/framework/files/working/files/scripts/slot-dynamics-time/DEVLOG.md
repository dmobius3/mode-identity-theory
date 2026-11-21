# The slot dynamics in time: development log

Append-only. A correction is a new entry. Entry numbers come from the headings, times from the clock (UTC).

## 1. The development boundary (2026-11-20T20:59:15Z)

The registered controls are those of `DESIGN.md` § 8. They run only after the code that carries their seeds, durations and normalizations is committed, and the dry run that measures the floors is the record's first entry. Before that, development runs only to build and debug the new code, inside this boundary:

- **Seeds:** development draws use `numpy.random.default_rng` with seeds from 900001 up, never a registered control's seed.
- **Sizes:** cutoffs N ≤ 12.
- **Uses:** a development run debugs an implementation, and every one is logged here with what it showed. None is a control, none is in the record, and none reads a registered pass line as a result.
- **New code:** `fftcubic.py`, the steppers and the diagnostics. The instrument is imported unedited, behind `pin.py`.

## 2. The FFT cubic against the dense one, at N = 8 and 12 (2026-11-20T20:59:40Z)

`dev/dev_fft_vs_dense.py`, seeds 900001 to 900008, one normalized random state per (slot, N) in R1, R2, R3 and R4. The FFT cubic matched the instrument's `Functional.cubic` to at most 6.5e-16 relative, and the FFT quartic matched the instrument's quartic energy to at most 2.0e-14 relative, on the first build of `fftcubic.py`. No change followed.

## 3. The time arm's first build (2026-11-20T21:21:30Z)

`timearm.py`, first build, and `dev/dev_timearm.py`, seed 900101, at N = 12 in R1, R3, R4 and R2, at the step 1.6/√(N(N+2)):

- **Free modes,** cubic off, one coefficient at the top level: each stepper's angle per step matched Verlet's 2 arcsin(hω/2) and the splitting's hω, and the state after 400 steps matched the rotation to at most 6.5e-14.
- **The rigid lowest levels:** the FFT cubic equals ‖c‖²c to 3.3e-16 in R1 and 6.6e-16 in R3, and not in R4 (0.21) or R2 (0.56), as the census's rigid and soft slots require.
- **The matched rigid waves:** Verlet's held to 1.5e-14 after 400 steps. The splitting's, with its velocity from the eigenvector of R(h/2)S(κ)R(h/2) and κ the norm² at the step's ends, missed by 1.7e-2 in R1 and 2.0e-2 in R3.
- **Multi-level random states with momenta,** cubic on, 200 steps: every charge's drift at most 1.1e-14 of ‖D‖·|q|·|p|, reversibility at most 4.4e-14 and right-SU(2) equivariance at most 4.0e-15 of |(q, p)|, for both steppers.

## 4. The splitting's matched wave reads κ at its kick (2026-11-20T21:21:30Z)

The splitting's kick reads the state after the first half rotation, whose norm² differs from the norm² at the step's ends at O(h²). With κ read at the step's ends, the kick does not see κ, and the orbit is not a rotation. `matched` now normalizes the wave where the kick reads it: (1, μ) is the eigenvector of the map R(h)S(κ) from one kick to the next, and the step-end state is R(−h/2)(1, μ). DESIGN.md § 4's cos θ = cos(ω₀h) − (κh/2ω₀) sin(ω₀h) then holds, with κ = ‖c‖² read at the kick, the reading under which the map is linear on the orbit as § 4 says. The design does not say where ‖c‖² is read, so this reading goes to the code review. The closed forms are 1 − cos θ = 2 sin²(ω₀h/2) + (κh/2ω₀) sin(ω₀h), with no cancellation, and μ = κh/2 + iω₀ sin θ/sin(ω₀h).

Rerun of `dev/dev_timearm.py`: the splitting's matched wave held to 1.4e-13 in R1 and 1.6e-13 in R3 after 400 steps, its angle equal to the formula's. `dev/dev_matched_growth.py`, seed 900102, κ = 1, N = 12, to 3200 steps: the splitting's error grew fourfold with each doubling of the step count, to 1.3e-11 at 3200 steps, nearly all of it phase, while ‖c‖² drifted linearly, by +2.6e-13 in R1 and −4.1e-13 in R3. Verlet's stayed at most 1.3e-13, with no drift in ‖c‖².

## 5. The splitting's rotation as three shears (2026-11-20T21:21:30Z)

The drift of entry 4 came from the rounded rotation. With cs and sn the doubles nearest cos(ωh/2) and sin(ωh/2), the determinant cs² + sn² of each half rotation differs from 1 by a fixed amount, applied twice per step, so each mode's free energy moves by the same factor at every step. In exact arithmetic of the doubles, cs² + sn² − 1 is +4.6e-17 at R1's lowest level and −6.6e-17 at R3's, at this step: twice those per step are the measured drifts of ‖c‖², +8.1e-17 and −1.3e-16 per step.

The rotation is now three shears, c += a v, v += b c, c += a v, with a = tan(φ/2)/ω, b = −ω sin φ and φ = ωh/2. In exact arithmetic it is the same map, the exact linear flow of § 4, and each shear has determinant exactly 1 for the rounded a and b. Rerun of both scripts: the splitting's matched wave held to at most 8.7e-14 through 3200 steps, with ‖c‖² within 8.2e-15 of κ. After 200 steps its charges moved at most 7.4e-16, its reversibility was 2.7e-15 and its equivariance 2.8e-15.

## 6. A run entry 4 leaves out (2026-11-20T21:24:10Z)

Between the first build and the closed forms of entry 4, one run of `dev/dev_timearm.py` took μ and θ from numpy's eigenvector of R(h)S(κ): the splitting's matched wave held to 1.8e-13 in R1 and 2.7e-13 in R3 after 400 steps.

## 7. The harness's first development run, and three fixes (2026-11-20T21:43:26Z)

`controls.py --dev`, its first build, into `dev/runs/20261120T213852Z/`, with its output in `dev/dev_controls_run1.out`: development seeds from 900201, N ≤ 12 and shorter durations. It stopped at control 1, as the stopping rule requires, on two arms that could not bite, and its dry run showed a third defect:

- **Control 6's read.** In the dry run the read failed at every step of the ladder. It expected n + 1 positive frequencies, but one trajectory excites one direction of each degenerate eigenspace, so the n-fold 2ω reads once. The read now expects the distinct values, 2ω and the radial frequency, or the one value 2θ/h with the cubic off. A degeneracy that the scheme split would read as further values.
- **The aliased grid.** Planted at M = 3N + 1, the arm stayed green, at most 7.7e-16. `dev/dev_arms.py`, seed 900104, at N = 8 and 12: M = 3N + 1 gave no alias in any of the four slots, while M = 4·max(levels), one point short of exactness for the levels present, aliased in R4 at N = 8 and 12 and in R3 at N = 12 (2.9e-4 to 1.2e-3), and not in R1, R2 or R3 at N = 8. INFERRED: the element i of 2I moves (α, β) along the Hopf torus, so each fibre component's frequencies keep one class of p + q mod 4, and at M ≡ 1 mod 4 an alias shifts that class unless it moves the frequencies further than the degree of |ψ|²ψ allows. Nothing here uses the smaller grid: the instrument's M = 4N + 1 stays. The arm is now planted at M = 4·max(levels).
- **The missing conjugation of A.** The arm stayed green, at 6.1e-16: the instrument's intertwiners are real, their imaginary parts at most 4.7e-17 at N ≤ 12. Control 1 now plants it in a basis whose intertwiners carry a complex phase per copy, against the instrument's cubic transformed to that basis. There the arm is red, 4.5e-2 to 2.0, and the FFT path itself agrees to 6.7e-16.

Every other number of the run was at round-off: the FFT cubic within 6.0e-16 of the instrument's; the dry run's floors at most 2.3e-15 for the multi-level runs, 5.7e-14 for the rigid states and 2.5e-14 for their energies; the dense cubic's symmetry floor at most 2.8e-15.

## 8. The harness's second development run: control 9's energy order (2026-11-20T21:53:45Z)

`controls.py --dev` after entry 7, into `dev/runs/20261120T214326Z/`, with its output in `dev/dev_controls_run2.out`. Controls 1 to 8 passed on the development inputs. Among them: the FFT cubic within 6.0e-16 of the instrument's, every arm red, and the phased basis within 6.7e-16; control 5's continuum-started waves converging at ratios of 4.0; control 6's read finding the two distinct frequencies at every step, its errors falling fourfold per halving. Control 9 failed in two parts:

- **The order.** On control 5's continuum-started rigid waves the energy error fell sixteenfold per halving, in R1 under Verlet 3.2e-5, 2.0e-6, 1.2e-7, 7.7e-9 and 4.8e-10: O(h⁴), outside [3.5, 4.5]. DERIVED: the scheme keeps a modified energy H̃ = H + h²G + O(h⁴), and G, like H, is invariant under the phase, so it is constant along a discrete rotation. The continuum start differs from the matched wave by O(h²), so G varies along the run by O(h²), and the energy error is O(h⁴). The line "at O(h²) under halving" is about a generic solution (§ 4), so control 9 now reads the order on the multi-level states of controls 4, 7 and 8, under halving over TA, with dry-run floors at each step of the ladder.
- **The drift.** It failed in R1 under Verlet and in R3 under both steppers. At the development duration T9 = 100, a pure oscillation at R1's radial frequency can move the two tenths' means apart by 4/(Ω T9/10) = 0.094 of its amplitude, above 10⁻²; at the registered T9 = 2000 the bound is 0.0047. The drift stays on the rigid waves, where the error oscillates at the single radial frequency.

The harness also changed in four smaller ways. A development run now continues past a stopping failure, so that every part of the harness runs. The outputs print paths relative to this folder, and tracebacks carry no machine path: the logs of runs 1 and 2 print this machine's path in their first line, so their outputs stay out of the repository, and the seeded scripts regenerate them. A failure in control 11 is now recorded, and the summary still written. The cost run takes its margin from `REG`.

## 9. The harness's third development run: control 11's map (2026-11-20T22:05:45Z)

`controls.py --dev` after entry 8, into `dev/runs/20261120T215345Z/`, its output on the bench. Every part of the harness ran:

- **Control 9.** The energy order, now read on the multi-level states, held at ratios near 4 wherever it was read, in all four slots under both steppers. The rigid waves' drift at the development T9 = 100 stayed near 10⁻² of the largest oscillation in R3, 1.07e-2 to 1.26e-2, nearly the same at every step of the ladder, as an averaging residual is; the registered T9 is twenty times longer. So control 9 failed there, and the rule of § 4 kept Verlet, since the splitting had not passed controls 3 to 9.
- **Control 10.** The cost runs ran, each in its own process.
- **Control 11.** It reported a convention residual of 1.6: the Galerkin sections failed the finite element's equivariance, so its distances, up to 0.96, meant nothing.

The cause is that the two instruments use different copies of 2I in SU(2). The instrument's 96 further elements are the even permutations of (0, ±1/2, ±1/(2φ), ±φ/2), and the finite element's the even permutations of (0, ±1/2, ±φ/2, ±1/(2φ)). The two copies share the 24 elements of the binary tetrahedral group, and each of the binary octahedral group's 24 other elements conjugates one onto the other. Control 11 now maps through the first of these in a fixed order, u = (j + k)/√2. Its Galerkin state is ψ'(x) = ψ(u⁻¹x), an isometric image of the Galerkin state, which obeys the finite element's equivariance with ρ'(g) = ρ(u⁻¹gu).

Each u⁻¹gu is taken as the instrument's exact element. The computed product sat 2.8e-15 off it, and the instrument's spin matrices take their angle as arccos(|a|), which near |a| = 1 turns that into a homomorphism defect of 8.9e-8. The same holds for any point near those poles, so a nodal value there may carry an error near 1e-8, far below what control 11 reads. `dev/dev_fecheck.py`, seed 900301, at the development duration: the intertwiner residual 1.1e-15, the convention residual 1.1e-14, the M-norm ratio 0.9991, and the relative M-distance 3.2e-3 at t = 1.64, beside the finite element's lowest-level mean eigenvalue 48.0253 for 48.

## 10. The code under review, end to end (2026-11-20T22:17:13Z)

`controls.py --dev` on the code the review receives, after entry 9 and the clearer refusal outside a git checkout, into `dev/runs/20261120T220841Z/`, its outputs kept with the review rather than in the repository. Every part of the harness ran. Controls 1 to 8 passed on the development inputs. Control 9 failed only on the rigid waves' drift at the development T9 = 100, as in entry 9: R1 under Verlet at h₀, 1.05e-2 of the largest oscillation, and R3 under both steppers, up to 1.26e-2. So the rule of § 4 kept Verlet. Control 11's map held, with the intertwiner residual 1.5e-15 and the convention residual 2.5e-14; the M-norm ratio was 0.99909 and the relative M-distance 3.0e-3 at t = 1.64. The outputs carry no machine path.

## 11. Control 6's fitted moduli (2026-11-20T22:48:08Z)

The review asked about the moduli of control 6's fitted eigenvalues: in entry 10's outputs their largest deviation from 1 reached 0.28 in R1 and 0.53 in R3 at h₀, falling fourfold with each halving. `dev/dev_dmd_moduli.py`, development seeds, N = 12, R1 and R3, both steppers, the ladder's first two steps:

- The read eigenvalues, at ±2ω and ± the radial frequency, sat on the unit circle to at most 1.24e-9.
- The large deviations belong to zero-frequency eigenvalues, fitted from the data's weakly excited directions, whose singular values are 2.3e-5 of the largest and below.
- In R3 a pair at ±0.15 to ±0.16, below the read's cut of a quarter of 2ω, came out 3.0e-4 to 7.9e-4 inside the circle.

So the moduli are an extraction diagnostic, not growth or decay rates. The outputs now record the read ones apart from the rest.

## 12. The review's fixes, and a run of them (2026-11-20T22:58:18Z)

The review of the code asked for these, each checked at source before it was taken:

- **The guard at the start.** Both steppers now check ‖c‖² against C̄ at step 0 as well.
- **The rule of § 4, measured.** It had scaled the splitting's error at h₀ by (τ_s/τ_v)². It now evolves the registered perturbation at the splitting's equal-cost step, h₀ τ_s/τ_v, over T6, and reads it as control 6 does.
- **Verlet's force carried.** In control 10's cost runs and in the timing that sets τ, Verlet's force at the end of one call now enters the next, so each timing counts one cubic per step. Before, each timed call evaluated one extra cubic.
- **Control 6's line and moduli.** Its line now names Theorem 3.7's distinct nonzero E0 frequencies, and its outputs record the read eigenvalues' moduli apart from the rest (entry 11).
- **The interlock.** `DESIGN.md` and `SHA256SUMS` join the files the registered run requires committed and unchanged.
- **The stopping reading,** Blake's choice: a failure of control 4, 7, 8 or 9 by the splitting alone disqualifies the splitting under the rule of § 4, and the controls go on with Verlet. A failure by Verlet, a failure of control 1 or 2, or a run past C̄ stops them. It is the sixteenth reading.
- **The bound's use.** Each nonlinear run records its largest ‖c‖² over its observations, over C̄. Readings 1, 9, 10, 11 and 14 gained the review's wording.

`controls.py --dev` with these fixes, into `dev/runs/20261120T224925Z/`:

- Every part ran. Controls 1 to 8 passed on the development inputs, and control 9 failed only on the rigid waves' drift at the development T9 = 100, as in entries 9 and 10.
- The dense cubic's cost per step at N = 12 under Verlet fell from 7.2 ms to 5.6 ms, about the three quarters that one cubic fewer in four predicts.
- The rule's measured runs: τ_s/τ_v was 1.099 in R1 and 0.954 in R3. At the equal-cost step the splitting's errors were 1.03e-4 and 2.76e-4 in R1, against Verlet's 1.36e-3 and 1.59e-3, and 3.27e-5 and 9.34e-5 in R3, against 2.91e-3 and 3.10e-3. Each comparison held, and the rule kept Verlet, because the splitting failed control 9 there.
- Control 6's read eigenvalues sat on the unit circle to 1.2e-9 at most. The rigid runs used 14% to 17% of C̄.
- After the run, control 4's rows gained the field for the bound's use. Control 4 alone, in R2 at the development seeds, then passed, its runs using 26% and 29% of C̄.

None of this is a control: the registered run takes its seeds, sizes and durations from REG.

## 13. The rule's failure path, and the code as committed, end to end (2026-11-20T23:32:13Z)

The confirmation of the review found one path unguarded. The rule of § 4 ran outside any `try`, so a run past C̄ in its equal-cost runs, or any other failure there, would have ended a registered run with no `12_rule.json` and no summary. The rule, control 11 and the summary now sit in `finish()`. A run past C̄ in the rule stops the controls there, as reading 16 says, and `12_rule.json` records it; any other failure there is a harness error. Either way control 11 does not run, and the summary is written. A development context may now write into a given folder, for a test.

`dev/dev_rule_stop.py` injects two faults, with stand-ins for what controls 3 to 9 hand the rule:

- **The ceiling.** With C̄ for the rule's runs set just above κ, the equal-cost trajectory crossed it at step 6. `12_rule.json` recorded the ceiling, the summary stopped after the rule, and control 11 did not run.
- **An error.** With the rule's setup raising, the summary recorded the error at the rule, with no machine path in its traceback, and neither `12_rule.json` nor `11_c11.json` was written.

`controls.py --dev` on the code as committed (`controls.py` `86e167e4a9a3…`, `timearm.py` `975ff084e1d1…`, `fftcubic.py` `cf31a82c65d8…`, `fecheck.py` `e58766e20874…`), into `dev/runs/20261120T232238Z/`:

- Every part ran. Controls 1 to 8 passed on the development inputs, and control 9 failed only on the rigid waves' drift at the development T9 = 100.
- The rule's measured runs: τ_s/τ_v was 1.143 in R1 and 0.939 in R3. At the equal-cost step the splitting's errors were 1.11e-4 and 2.98e-4 in R1, against Verlet's 1.36e-3 and 1.59e-3, and 3.16e-5 and 9.03e-5 in R3, against 2.91e-3 and 3.10e-3. The rule kept Verlet, since the splitting failed control 9 there.
- Control 11's figures were those of entry 10.
