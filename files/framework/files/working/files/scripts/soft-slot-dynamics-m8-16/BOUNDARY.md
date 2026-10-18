# M8.16 development: the build-versus-qualification boundary

Fixed 2026-10-15T19:41:15Z, before any M8.16 code exists. Blake's ruling of 2026-10-15, on UA's and UB's positions after the census landed at 787aef1. This file is not edited after its first write: a change enters as a dated amendment at the bottom, and DEVLOG.md records each one.

## The ruling, verbatim

> Agreed: the GO list (synthetic and manufactured tests, Theorem D at a rigid slot, C2a and C2b), UA's disclosure condition (development runs logged and disclosed, including how they informed tolerances; no qualification credit before registration; their later registered results count as conformance and regression evidence, not independent confirmation), and the post-freeze rule (every control runs against the registered criteria, a failure stands as registered, no repair-and-rerun under the same qualification identity).
>
> Tightening: seal the pyramid control at every amplitude, not only the smallest. A development solve of the pyramid's branch at larger ε would show whether its in-span mode separates, and the trend would give away the smallest-amplitude result before registration. So the pyramid branch is not solved at all until M8.16's pre-registration freezes.
>
> SEALED, as amended:
> * the pyramid control, at every amplitude;
> * Theorem R's frequencies on census target rows;
> * all unresolved census targets.
>
> Also for the draft: the rigid slot used for Theorem D is one of R1, R3, R6, R7 or R8, and every control stays off the trivial sector, per the ruling's "nontrivial sectors". Put the split, with this amendment, in one explicit paragraph of the M8.16 draft.
>
> Disposition: GO to author-side development under the amended split. No pyramid solve, target-row exposure, scored qualification or OpenWave filing authorized yet.

## The lists, as they bind the build

**GO before the freeze (development, logged in DEVLOG.md):**
- synthetic and manufactured tests: quadrature or recoupling exactness to degree, invariance under right SU(2) and the fibre group, the Hessian identities on synthetic states, convergence on toy problems, manufactured solutions;
- Theorem D at a rigid slot, one of R1, R3, R6, R7 or R8 (M8.15's C1 is R3's exact branch);
- C2a, R4's coherent branch, and C2b, R2's weight-7/2 branch with complex structure i (M8.15's controls table).

**SEALED until M8.16's pre-registration freezes:**
- the pyramid control (P5 in R4, the M8.15.x qualification's non-target case), at every amplitude: its branch is not solved at all;
- Theorem R's frequencies on census target rows: T1, T4, T2 in both slots, T3 in both slots, and T5;
- every unresolved census target: T1, T4, the prism in R4, and T5's upper window. M8.15's adjudicated ladders on the target rows are sealed with them.

**Not on either list, so not run unless the list is amended:** M8.15's C3 (R4's octahedron), and any other census orbit.

**Every run, at every stage:** nothing on the trivial sector R0, which was C2's own control arena.

**The disclosure condition (UA).** Every development run is logged in DEVLOG.md with its script hash, its case and its outcome, including how it informed any tolerance. Development runs earn no qualification credit. Their later registered results count as conformance and regression evidence, not as independent confirmation.

**The post-freeze rule.** Every control runs against its registered criteria. A failure stands as registered. There is no repair-and-rerun under the same qualification identity.

## The admission it sits inside

xrodz, #512, comment 18955679 (2026-10-15): a stationary continuation and linear-spectrum record of named branches under the frozen slot action, on its nontrivial sectors, with a law the program derives and pins itself and nothing from `m8_5c/design_inputs/` or the C2 room. Outside it: time integration in a harmonic basis, any route for the two MODELS.md criteria, the census's persistence tests, and anything of M8.4. His §3 boundary paragraph is quoted verbatim in the M8.16 pre-registration.

## UA's technical priority

The exact zero modes must follow from the discrete action's symmetry. No zero is inserted by hand, and no troublesome mode is projected away, or the instrument would reproduce the appearance of a fix without removing the measurement problem.

## Amendment 1, 2026-10-15T20:01:50Z: C3 joins the GO list

Blake's decision, on both units' recommendation. M8.15's C3, R4's octahedron, moves from "not on either list" to the GO list, on the same terms as C2a and C2b: logged in DEVLOG.md, disclosed, and with no qualification credit; its registered rerun after the freeze counts as conformance and regression evidence, not as independent confirmation.

**Why it leaks nothing.** Its outcome is known twice over: Theorem R(b) gives it born hyperbolic, and M8.15 adjudicated its ladder Hyperbolic at all 18 points to 72. It says nothing about the pyramid's in-span mode or any unresolved target.

**Why it is needed.** It is the only real-pair check before the freeze: the one control that shows the instrument finds an instability, and that Theorem K holds with k_r > 0.

Everything else above stands as written. R4 is a nontrivial sector.

## Correction 1 to amendment 1, 2026-10-15T20:35:32Z

Amendment 1's "M8.15 adjudicated its ladder Hyperbolic at all 18 points to 72" reads "M8.15's control ladder, unscored and run under its frozen rules, reads Hyperbolic at all 18 points to 72", as the census records it (its catalog row and its line on the controls: "They are unscored"). UB found it. The decision stands.

## Amendment 2, 2026-10-17T20:10:47Z: a lowest-level check of each sealed seed

Blake's decision, before the units' final review of the M8.16 registration, where they see it. Before the freeze, each sealed case's seed, the pyramid's and every census target row's, may be constructed and evaluated on the lowest level only: `Q(u)` against the Result's exact value, the criticality residual on the lowest level, and `(k, r_u)` from the orbit tangents and `σ`, as `branches.orbit_checks` computes them. Nothing more: no Newton step, no branch at any nonzero amplitude, no Hessian, no linear record and no spectrum.

**Why it leaks nothing.** Each of the three is a value the Result publishes (the Soft-Slot Branches, § IV). None depends on the instrument's behavior at any amplitude, so none gives away the pyramid's in-span mode or any target's finite-amplitude spectrum.

**Why it is needed.** A seed error, in the prism's three-weight phases, in T4's conversion from its certified point, or in `R5`'s quartic, would otherwise first show at the registered run's own seed check, after the freeze, and stand there as registered.

It is logged in DEVLOG.md and disclosed, and it earns no qualification credit. Everything else above stands as written.

## Amendment 3, 2026-10-17T20:12:26Z: `R5`'s coherent branch joins the GO list, for development only

Blake's decision, before the units' final review of the M8.16 registration, where they see it. `R5`'s coherent branch, `v₃` on `R5`'s lowest level, moves from "not on either list" to the GO list as a development control: its sample, `ε ∈ {0.25, 0.5, 1, 2}` at `N = 16, 24` and 32, logged in DEVLOG.md and disclosed, with no qualification credit. It is not a registered control.

**Why it leaks nothing.** Its small-amplitude answer is Theorem R(c)'s, C2a's slow spectrum scaled by 9/16, with `R5`'s own `Q`. It is neither the pyramid nor a census target row, and its readings say nothing about the pyramid's in-span mode or any target.

**Why it is needed.** `R5` carries four target branches, T1 to T4, and no `R5` branch has been solved. The sample tests the solve, the kernel and the record in `R5`, shows whether the calibration fitted on `R2`, `R3` and `R4` holds there, and measures `R5`'s cost in place of a scaling.

Everything else above stands as written.

## Note to amendments 2 and 3, 2026-10-17T20:21:58Z: their scope and conditions, from the units' review (UA, UB)

**Amendment 2.** At each sealed seed the check evaluates only `Q(u)`, criticality on the lowest level and `(k, r_u)`, against the frozen values. No Newton step is taken, and no Hessian, slow matrix, `L` or `A` is formed at any sealed seed (UB). The check stays algebraic and pre-solve: no stationary branch, no finite-amplitude Hessian, no linear spectrum, no Theorem R frequency and no stability classification at any sealed case (UA). A failed check is recorded as failed before the implementation is corrected. The correction goes into the seed's constructor, never into the frozen expectation, before the freeze, and is disclosed (UA, UB).

**Amendment 3.** Before `R5`'s coherent sample runs, its expected values are derived and logged, as C2a's were: `Q`, `(k, r_u)`, `V₀`, the type, the indices, and the slow spectrum at `s = 9/16`. Its seed check confirms `Q` to `10⁻¹²` (UB). After it runs, it reports its cluster coefficient, `L`'s kernel and the convergence rule's readings against the calibration as it stands. No constant is refitted on it unless one of the calibration's own conditions fails, and any change is disclosed (UB).

Everything else above stands as written.

## Amendment 4, 2026-10-17T21:55:49Z: `R5`'s coherent branch also runs in the registered run, gating the `R5` rows only

Blake's decision, before step 3's dry run, on UB's recommendation. UA placed the decision with Blake and asked only that it be explicit. Amendment 3 kept `R5`'s coherent branch for development only. It now also runs in the registered run, in the controls' phase, at the controls' points, against `EXPECTED_R5.md`'s row.

**What its outcome governs.** It gates the four `R5` rows only:
- if it fails, T1 to T4 in `R5` are recorded as not qualified, with the failing check named, and the run continues;
- it never stops the run, and neither the pyramid's test nor the `R2` and `R4` rows depend on it.

Its development sample counts as conformance evidence, not independent confirmation. Everything else above stands as written.
