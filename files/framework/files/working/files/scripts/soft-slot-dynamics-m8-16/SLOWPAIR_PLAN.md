# M8.16: the slow-pair demonstration, a plan and its results (2026-10-17; the units' changes folded)

`DESIGN.md` §7 (v2.12) states the requirement: the record must resolve a slow pair below 1.04×10⁻⁵ at N = 40, M8.15's level-3 cluster tolerance. It is met only when this demonstration passes, and the qualification freeze waits for it.

The units' conditions:
- **UA.** It exercises both the spectral classifier and n(L), with its own mutation arms. If L's inertia cut prevents resolving the pair, the gate fails and needs its own bounded, documented correction, never a forced classification.
- **UB.** It recalibrates L's zero cut on the controls' measured L kernel.

Both units gave Step 1 a GO, and Blake approved its cost. The scout, `dev/slowpair_scout.py` (DEVLOG 129, rerun as 133 after the zero-count check), is the baseline before Step 2.

**Status (2026-10-17): closed.** Step 1 ran at its full scope (DEVLOG 136 to 139). Step 2's cut is adopted at 1000 u ‖L‖ with G_L = 10 (UB; UA, who first approved 100 u, accepts it), and the cheap checks pass on it (DEVLOG 142 to 145). Step 3 passed (DEVLOG 146), and both units confirm it: the slow-pair gate is closed (DEVLOG 148).

## What a slow pair needs, and where the record stood before Step 2

A genuine slow pair at s must clear three checks.
- **A's gray zone,** §7's calibration: s ≥ G margins. At N = 40 and m ≤ 0.2 that is 1.7×10⁻⁶.
- **L's inertia.** n(L) counts the pair's L eigenvalue μ only above L's gray zone, 10⁻⁷ ‖L‖ before Step 2. Between 10⁻¹⁰ and 10⁻⁷ ‖L‖ it was flagged, and below 10⁻¹⁰ ‖L‖ read as zero. n(L) is also unresolved where L's zero count differs from V₀'s chains: ker A = ker L × {0}, so the two are equal, and a μ read as zero is never a resolution. The record now checks this (UB; `dl_recal.py`'s claim 9).
- **V₀'s leak,** at most κ_L u‖A‖/gap, where the gap is now the pair itself.

**μ depends on the pair's structure.** For a block diag(l₁, l₂) under the frame's 2ωJ₀, the slow pair solves s⁴ + (4ω² + l₁ + l₂) s² + l₁l₂ = 0. Two cases:
- **S1, soft-soft:** diag(k, k), μ ≈ 2ωs. This is the generic slow mode: Theorem R's slow pairs come from two directions that are both soft.
- **Near a crossing,** one direction stiff (K = 1), μ ≈ 4ω²s²/K:
  - S2, imaginary, Krein-positive: diag(μ, K);
  - S3, imaginary, Krein-negative: diag(−μ, −K);
  - S4, real: diag(−μ, K).

**The floors at N = 40 before Step 2** (‖L‖ ≈ ‖A‖ ≈ 1,734, ω from 7 to 14, the controls' range there): μ clears L's gray zone for S1 only above s ≈ 6.2×10⁻⁶ to 1.2×10⁻⁵, and near a crossing only above 4.7×10⁻⁴ to 9.4×10⁻⁴.

**The scout** (DEVLOG 129; 5 mixings at each of ω = 7 and 14, s = 10⁻⁵ and 5×10⁻⁶, m = 0.2; 20 readings per structure below 1.04×10⁻⁵):
- **S1** resolves at 5 of 20, and only at ω = 14, s = 1.0×10⁻⁵. Elsewhere it reads n(L) Unresolved.
- **S2** read clean at 11 of 20 (DEVLOG 129), but only by reading μ as zero. With the zero-count check it resolves at 0 of 20 (DEVLOG 133).
- **S3 and S4** resolve at 0 and 0 of 20: the index fails to balance, or V₀'s leak exceeds its bound.
- **Near a crossing the leak runs 1.0×10⁻¹ to 6.1 times its bound.** The nearby pair, itself close to a Jordan chain, tilts the computed V₀ by about u‖A‖/σ_min(T₂₂), the smallest singular value of the Schur form's outside block. It falls like gap² near a crossing and equals the gap for S1 (UB). The leak tracks it at 0.008 to 0.10 on all four structures (a scratch check here).
- **No reading gives a wrong type.** The record stays safe, but before Step 2 it met the requirement for none of the four structures.

## Step 1: measure the controls' L kernel (runs, for Blake's cost decision)

- **What.** At each point:
  - L's eigenvalues nearest zero: its kernel, as many as V₀'s chains (C1 5, C2a 3, C2b 5, C3 4), and their largest |μ| against ‖L‖, the lift;
  - the smallest genuine |μ|;
  - ‖L t‖ for every declared kernel tangent: the symmetry tangents, R2's fibre directions J c and i J c, and C1's rigid-family directions, the five real directions of its lowest level orthogonal to v. D4's identity, ‖L T c‖ = ‖T F′(c)‖, is compared only where its symmetry hypothesis holds, never as a universal account of the lift (UA);
  - the Newton floor;
  - at D7's points, ρ = (the smallest genuine |μ|)/(2ω s_min), with s_min the point's slowest pair from its record. It is amplitude-free at leading order, so it carries the controls' slow-pair structure to the requirement's scale (UB). Beside it, each slow pair's anisotropy r, read from L restricted to the pair's position span;
  - L's zero count against V₀'s chains from `EXPECTED_V0.md`, confirming the zero-count check at every control point (UB).
- **Where,** bounded:
  - (i) D6's C1 at N = 16 to 40, ε ∈ {0.5, 1, 2}: exact, with no solve;
  - (ii) D7's three controls at N = 16 and 24, along their full ladders from the germ, where the floor and the lift grow;
  - (iii) D7's sample at N = 32, ε ∈ {0.5, 1, 2}.

  D7 at N = 40, and the ladders' tops at N = 32, are not run. There the lift is read from its predictor, checked against D6's N = 40 (INFERRED).
- **The script.** A new dev script, `dev/lkernel.py`, logged like any run. No sealed case.
- **Cost, from the recorded times on these points:**
  - D6, about 16 min;
  - the N = 24 ladders, about 20 min;
  - the N = 16 ladders, about 2 min;
  - the N = 32 sample, about 31 min.

  So about 69 minutes on these points: the solves and Hessians, since L's eigenvalues replace A's eigendecomposition (D6's times include its record, so they run a little high).

## Step 2: recalibrate L's zero cut (a proposal, after Step 1)

- **The rule.** The cut is κ_z times the controls' largest lift against ‖L‖, with a gray zone up to G_L times the cut. κ_z and G_L are set so that two conditions hold, §7's cluster condition applied to L:
  - the controls' kernel sits at least ten times below the cut;
  - their smallest genuine eigenvalue sits at least ten times above the gray zone.

  The constants are set after Step 1, disclosed, and provisional until you review them. The measurements decide whether such a cut exists, not the result Step 3 wants. If the two conditions cannot hold at once, Step 2 fails and reports the incompatibility; no threshold is chosen to make Step 3 pass (UA).
- **What it must reach,** at ω = 7:
  - for the soft-soft pair at 1.04×10⁻⁵, L's gray zone must top out at or below 8.4×10⁻⁸ ρ_min ‖L‖, with ρ_min the controls' smallest ρ (Step 1): about 6.5×10⁻⁸ ‖L‖ at C3's 0.78 (UB). The cut before Step 2, 10⁻⁷, misses;
  - near a crossing (K = 1), at or below 1.2×10⁻¹¹ ‖L‖, about four decades below the cut before Step 2.
- **D's cut is not part of this.** It is n(D)'s, on V₀, at 10⁻⁸ ‖B‖, and reads the chains' partner energies, not a slow pair.

## Step 3: the synthetic demonstration (cheap; after Step 2)

- **The systems.** The scout's four structures, at N = 40's scale, ω ∈ {7, 14}, 10 mixings each:
  - s = 1.0×10⁻⁵ and 5×10⁻⁶, with 3×10⁻⁵ as a control, at m = 0.2;
  - at m = 72, where A's gray zone blocks the pairs below 3×10⁻⁵, with s = 10⁻⁴ as a control.
- **The expected outcomes,** derived before the run from each system's exact ‖A‖ and ‖L‖ and the pair's exact μ.
  - **"Resolved" means:**
    - the type, n(L), n(D), K and the balance as derived;
    - the pair labelled and its Krein group definite, with the derived sign;
    - L's zero count equal to the kernel's, so a μ read as zero is not a resolution.
  - **Wherever one of the three checks blocks it,** the reading is Unresolved, never a wrong type.
- **The gate, pass or fail:** the soft-soft pair in each of its sign patterns, resolved as derived at every mixing for s = 1.0×10⁻⁵ and 5×10⁻⁶, at m = 0.2 and both ω (UB):
  - S1+, diag(k, k), imaginary and Krein-positive (C2a, C2b);
  - S1−, diag(−k, −k), imaginary and Krein-negative;
  - S1r, diag(−k₁, r k₁), real, at the controls' largest measured r from Step 1 (C3's 1.65 at N = 16, ε = 0.5, UB's reading).

  The pyramid's in-span mode is sealed, so the gate covers each type it could have (UB). If it fails, the gate fails (UA), and a correction is proposed separately, bounded and documented.
- **What a pass shows:** the minimum demonstrated resolution capability, for slow pairs of the controls' structure. It is not proof that the sealed in-span mode will resolve; only the frozen qualification run can establish that (UA).
- **Characterized, not gating:** S1r at r = 10 and 100, the unequal-stiffness check (UA). A mode whose leading τ vanishes is strongly anisotropic, with k_min = 2ωs/√r, and falls toward S2 to S4's floors; their floors are reported (UB).
- **S2 to S4** are scored on their own derived outcomes, under the recalibrated cut and today's leak bound: resolved where all the checks clear, Unresolved otherwise, never a wrong type. A μ read as zero is never relabelled a resolution (UA). Their resolvable floors are reported, and their rows give σ_min(T₂₂) beside the gap (UB).
- **The arms,** each of which must turn red:
  - the L cut before Step 2, where the S1 gate fails;
  - L's gray zone removed (G_L = 1), where a μ placed inside the recalibrated gray zone loses its flag;
  - a cut below the controls' measured lift, where a synthetic kernel lifted by that amount is miscounted;
  - the zero-count check dropped, where S2's μ read as zero reads Elliptic with nothing unresolved (UB). Under Step 2's cut this needs claim 9's construction, K = 1000 (Step 3's results).
- **The baseline.** The scout is the baseline before Step 2.

## What the plan does not do

- No pyramid, no census target, no qualification run and no filing. Nothing sealed is touched.
- §7's A-side calibration is unchanged.
- The leak bound is not recalibrated (UA, UB). Near a crossing it is what keeps a tilted V₀ from passing.

## The units' rulings (2026-10-17)

- **The gate's scope.** Both units keep S1 as the gate, with S2 to S4 characterized. UB widens the gate to the soft-soft pair's three sign patterns. UA asks for an unequal-stiffness check, characterized and not gating, and for a pass to be read as minimum capability only. All three are folded above. The unequal stiffness enters the gate only at the controls' measured r, and r = 10 and 100 are characterized.
- **Step 1:** GO, subject to Blake's approval of its cost, with UA's tangent measurements and UB's ρ added. No new expensive ladder is authorized.
- **Step 2:** the method is confirmed. The constants wait for Step 1's measurements, which go back to the units first (UA).
- **Step 3:** the design is confirmed, with the gate widened, S2 to S4's σ_min(T₂₂), and a fourth arm. Its run waits for Step 2.
- **The leak bound:** kept as calibrated (UA, UB). A σ_min(T₂₂) form of it would change no outcome, and would come with its own arm if it were ever proposed (UB).

## Step 1's results, and Step 2's proposal (2026-10-17, DEVLOG 136 to 140; for the units)

**Step 1 ran at its full scope:** 133 points, about 90 minutes on battery (DEVLOG 136 to 139).
- **The kernel's lift is round-off.** It is at most 1.4×10⁻¹⁵ ‖L‖, 6.2 u, at C2b, N = 24, ε = 132, over the kernel's eigenvalues and every declared tangent. By N it is at most 5.9, 6.2, 4.2 and 2.4 u at N = 16, 24, 32 and 40, so it does not grow with N.
- **No floor-driven lift is measurable.** D4's predictor, ‖T F′(c)‖, is at most 1.9×10⁻¹⁶ over ‖L‖ ‖T c‖, against u = 2.2×10⁻¹⁶. At the largest Newton floor, 4.7×10⁻¹³ (C2b, N = 24, ε = 128), it is 7.4×10⁻¹⁷. The data cannot establish that the solve contributes nothing below floating-point resolution (UA). So the lift at the unmeasured points, D7 at N = 40 and the N = 32 tops, is read as round-off too (INFERRED).
- **L's zero count equals V₀'s chains at all 133 points,** so the zero-count check holds on every control point.
- **The smallest genuine |μ|** is 1.4×10⁻⁵ ‖L‖, at C2a, N = 24, ε = 0.25: the slowest mode at the smallest amplitude.
- **The controls' slow-pair structure:**
  - ρ runs from 0.777 (C3, N = 16, ε = 0.25) to 1.009;
  - r reaches 1.66, at C3's smallest amplitude. C3's r falls toward 1.0 near ε = 32 and rises to about 1.3 at its top;
  - over all 407 slow groups, √|k_min k_max|/(2ωs) is 0.973 to 1.049, so the soft-soft relation holds to within 5 percent.

**A cut exists.** The kernel ten times below the cut needs a cut of at least 1.4×10⁻¹⁴ ‖L‖. The smallest genuine eigenvalue ten times above the gray zone needs the gray zone to top out at or below 1.4×10⁻⁶ ‖L‖. With G_L = 10 that leaves about seven decades.

**Step 2's proposal, as adopted** (UB's cut; the units' rulings below):
- **The cut is 1000 u ‖L‖ (2.2×10⁻¹³ ‖L‖), with the gray zone up to G_L = 10 times it (2.2×10⁻¹² ‖L‖) (UB).** The lift is round-off, so the cut is set in units of u, the unit that travels across machines. Within the seven decades the two conditions leave, the cut gives the kernel's round-off, the side that varies by machine, 160 times headroom. The S1 target is still met about 3×10⁴ times over, and the smallest genuine eigenvalue sits 6×10⁶ times above the gray zone.
- **The S1 gate's target,** 8.4×10⁻⁸ ρ_min ‖L‖ = 6.5×10⁻⁸ ‖L‖, is met with about 3×10⁴ times to spare.
- **Near a crossing** (K = 1, ω = 7), L's inertia then resolves pairs down to about 4.4×10⁻⁶. But V₀'s leak, through σ_min(T₂₂), still blocks them first (the scout), so S2 to S4 stay characterized.
- **A cut too tight fails safe.** A kernel eigenvalue above the cut makes L's zero count fall short of the chains, which reads Unresolved, never a wrong type.
- **D's cut (n(D), on V₀) is unchanged.**

## The units' rulings on Step 1 and Step 2 (2026-10-17)

- **Both units CONFIRM Step 1,** recomputed from its four JSONs, and keep the widened gate: S1+, S1− and S1r at the measured r = 1.66, with r = 10 and 100 characterized and a pass read as minimum capability. No regression reruns: Step 1 measured L at every regression point (UB), and no new expensive control work is authorized (UA).
- **UA:**
  - GO for Step 2 at 100 u ‖L‖ with G_L = 10;
  - a conditional GO for Step 3: keep DL's original calibration and outputs; give L its own gray-zone factor, leaving A's gray zone and n(D)'s cut unchanged; keep the registered gate; run the four arms; keep S2 to S4's limits visible, without loosening the leak rule. The cheap tests establish the cut's implementation before Step 3 scores;
  - a wording qualification on Step 1, folded above, and a provenance note on entry 140's plan hash, DEVLOG 141;
  - if Step 3 passes, close this pre-freeze numerical gate and move to the M8.16 registration draft and freeze review.
- **UB:**
  - the cut at 1000 u ‖L‖, not 100 u. The kernel's side varies by machine, and gets 162 times headroom instead of 16. The other two sides keep four decades or more, and the lower floor near a crossing buys nothing, since V₀'s leak blocks S2 to S4 there first. UB's replacement text is folded above;
  - claims 7 and 9 re-derived before `dl_recal.py` reruns: both are written around the earlier cut, and both fail under either proposed cut.
- **The adjudication, mine.** UB's 1000 u is adopted. Both cuts meet both of Step 2's conditions, and the choice within the window is the judgment UB argues from Step 1's data alone: the side that varies by machine gets the larger headroom. Flagged to UA, who approved 100 u.
- **Implemented** (`instrument/linear.py`): L's cut, `L_CUT` = 1000 u, and its own gray-zone factor, `G_L` = 10. `ORIGINAL` keeps the earlier 10⁻¹⁰ and 10³, so DL's original claims run unchanged. A's gray zone and D's cut are untouched.
- **The cheap checks** (DEVLOG 142 to 145):
  - DL is byte-identical to entry 93's.
  - `dl_recal.py`: 0 failed, with 10 scored claims and 8 arms. Claim 7 is re-derived: its pairs at 3×10⁻⁵ and 10⁻⁴ read Elliptic, and its new arm, the earlier cut, reads the first n(L) Unresolved. Claim 9 is rebuilt as UB wrote it: k₁ at 42.5 u ‖L‖, the item at 10 of 10, and 10 of 10 clean Elliptic with the check dropped.
  - The change report moves from 1 to 3 of 31. The two new changes are counts inside readings that stay Unresolved, never a type: claim 6(a)'s L eigenvalue, −1.2×10⁻¹² ‖L‖, now lies in L's gray zone, and claim 10's, −8.8×10⁻¹¹ ‖L‖, is now read as negative.
  - Entries 142 and 143 ran before an attribution fix in one comment of `linear.py`. Entries 144 and 145 reran on the final file, with outputs identical to entries 93 and 143.

## Step 3's results (2026-10-17, DEVLOG 146; for the units)

**Step 3 passed.** `dev/slowpair_demo.py` read 96 rows of 10 mixings, 960 readings, in about 5 seconds. Each row's outcome was derived before the run from the system's exact ‖A‖ and ‖L‖ and the pair's exact μ, and the script prints the derivation first.

- **"Resolved," as scored:** the derived type, counts, (k_r, k_c, k_i⁻) and balance; nothing unresolved; the pair and its partner within s/2 of their exact places and labelled as derived, with an imaginary pair's group definite and of the derived Krein sign; and L's zero count 2, equal to V₀'s chains.
- **The gate:** 12 of 12 rows resolved at every mixing, for S1+, S1− and S1r at r = 1.66, at s = 10⁻⁵ and 5×10⁻⁶, m = 0.2 and ω = 7 and 14. The leak ran at most 8.2×10⁻⁴ of its bound, and the pair sat within 1.6×10⁻⁹ s of its exact place.
- **Every other row as derived,** 84 of 84:
  - the S1 controls resolve, at s = 3×10⁻⁵ (m = 0.2) and 10⁻⁴ (m = 72);
  - at m = 72, every structure at 5×10⁻⁶ and 10⁻⁵ reads Unresolved with the separation flagged;
  - S1r at r = 10 and 100 resolves at every s and mixing, its leak at most 7.4×10⁻³ of its bound;
  - S2 to S4 resolve, or read Unresolved through V₀'s leak alone.
- **No wrong type** in 960 readings.
- **Near a crossing, V₀'s leak sets the floor.** Every mixing resolves from 3×10⁻⁵, except S4 at ω = 7, which resolves at 9 of 10 there and at every mixing at 10⁻⁴. Resolved, of 10:

  | | ω | 5×10⁻⁶ | 10⁻⁵ | 3×10⁻⁵ | 10⁻⁴ (m = 72) |
  |---|---|---|---|---|---|
  | S2 | 7 | 2 | 4 | 10 | 10 |
  | S2 | 14 | 4 | 9 | 10 | 10 |
  | S3 | 7 | 0 | 2 | 10 | 10 |
  | S3 | 14 | 3 | 8 | 10 | 10 |
  | S4 | 7 | 1 | 4 | 9 | 10 |
  | S4 | 14 | 4 | 9 | 10 | 10 |

  - L's floor there is 4.4×10⁻⁶ at ω = 7 and 2.2×10⁻⁶ at ω = 14, and A's is 1.65×10⁻⁶, so neither binds. The leak ran up to 6.3 times its bound.
  - σ_min(T₂₂) beside the gap (UB): it equals the gap for S1± and the gap over √r for S1r, each to 0.25 percent, and 2ωs² near a crossing at K = 1, to 0.8 percent (a fit to these rows, INFERRED).
- **The arms,** each red:
  - (a) **The cut before Step 2,** on the gate's own systems: the gate resolves at 30 of 120 readings, only at ω = 14 and s = 10⁻⁵, where μ clears 10⁻⁷ ‖L‖. Elsewhere n(L) is flagged, and S1r reads Hyperbolic with n(L) unresolved: the type right, its count withheld.
  - (b) **G_L = 1.** A pair near a crossing, K = 1000 at ω = 14, with μ at the gray zone's geometric centre, 3.16 L_CUT: s = 2.59×10⁻⁵, 15.7 G margins out, with the leak bound held vacuous. Under G_L = 10 its gray-zone item fires at 10 of 10; under G_L = 1 all 10 read clean Elliptic.
  - (c) **A cut of 1 u ‖L‖.** The phase chains lifted by the controls' largest measured lift, 1.37×10⁻¹⁵ ‖L‖, computed at 5.8 to 6.6 u, at m = 72: under L_CUT 20 of 20 resolve; under 1 u none do, each flagged for L's gray zone and its zero count.
  - (d) **The zero-count check dropped,** on claim 9's construction (k₁ at 42.5 u ‖L‖): with the check, its item at 10 of 10; without it, 10 of 10 clean Elliptic.
- **What the pass shows:** the minimum demonstrated resolution capability for slow pairs of the controls' structure, under Step 2's cut and §7's calibration, down to 5×10⁻⁶ at m = 0.2 in each sign pattern. It is not proof that the sealed in-span mode will resolve; only the frozen qualification run can establish that (UA). Near a crossing, pairs up to about 3×10⁻⁵ can read Unresolved through V₀'s leak, never a wrong type, and the leak rule is unchanged.
- **Where the run fixes what the plan left open, flagged:**
  - the fourth arm uses claim 9's construction, K = 1000: under Step 2's cut, S2's μ at K = 1 sits above L's gray zone (UB's finding on claim 9);
  - arms (b) and (c) use the constructions above; the plan named only their intent;
  - at m = 72 the grid is s = 5×10⁻⁶ and 10⁻⁵, which A's gray zone blocks, with 10⁻⁴ as the control;
  - the pair is located within s/2 of its exact place. Near a crossing its computed place moves by up to 1.4×10⁻⁵ s, a near-chain's ill-conditioning, far inside that;
  - each arm reads the same systems as its claim, built once and read twice.

## The units' rulings on Step 3: the gate is closed (2026-10-17)

- **Both units CONFIRM** the adjudication, the implementation, `dl_recal.py`'s claims 7 and 9, Step 3's derivation and results, `DESIGN.md` v2.14 and `RECAL_PLAN.md`'s dated note. The slow-pair gate is closed (DEVLOG 148).
- **UA:**
  - accepts 1000 u ‖L‖ over its own 100 u. Both meet the conditions, and the larger cut protects better against machine-dependent round-off without approaching the controls' smallest genuine eigenvalue. It is an empirically calibrated cut, not a universal error bound;
  - reproduced the 12 gate rows independently, and found the archive's hashes for the Step 3 script, the instrument and the outputs matching DEVLOG 146;
  - accepts the fourth arm on claim 9's construction, as a disclosed implementation of the planned zero-count test;
  - keeps open what the demonstration cannot show: that the sealed pyramid's predicted in-span slow mode resolves. The qualification tests that, without adjusting the accepted instrument or criteria;
  - sees no need for further development controls or costly runs on account of this gate, and gives a GO to draft and review the M8.16 qualification registration, within #512's admission boundary and the normal freeze review. The registration is filed before any scored qualification run, and does not authorize the separate census preregistration.
- **UB:**
  - reran DL, `dl_recal.py` and Step 3 under python3 -I, all as shipped, with the gate's 12 rows matching mixing for mixing;
  - reran Step 3 with L's cut at 100 u: the same verdicts, so the choice of cut decides only the kernel side's headroom. Reproduced here, in scratch and unlogged;
  - the counts near a crossing vary by machine: at 3×10⁻⁵ and ω = 7, S2 resolves at 9 of 10 on UB's machine and S4 at 10 of 10, against 10 and 9 here. "Pairs up to about 3×10⁻⁵ can read Unresolved" covers both;
  - S1r at r = 10 and 100 resolves at every mixing outside A's gray zone on both machines, its leak at most 4.5×10⁻³ of its bound there and 7.4×10⁻³ here, so an anisotropic soft-soft pair resolves to r = 100. UB's sentence for §7 is folded, verbatim (`DESIGN.md` v2.15);
  - closes the gate: §7's requirement is met for slow pairs of the controls' structure at N = 40's scale, as minimum capability, with the record's stated limits kept. The other pre-freeze items stay as written in `DESIGN.md`.
- **Folded** in `DESIGN.md` v2.15: UB's §7 sentence, and UA's reading of the cut as an empirical calibration.
