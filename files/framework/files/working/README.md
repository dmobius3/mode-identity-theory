<a id="top"></a>
/ **[`main`](https://github.com/dmobius3/mode-identity-theory/tree/main/)** / **[`framework`](/files/framework/)** / **[`bedrock`](/files/framework/files/bedrock/)** / **[`cosmos`](/files/cosmos/)** / **[`spectrum`](/files/spectrum/)** / **[`tools`](/files/tools/)** /

---

# :memo: Working Files

Research-in-progress across the framework. Organized by status: an orienting map first, then open problems (foundational upgrades, then technical gaps), then closed results and the data tests run against public datasets, then items gated on external data. Within each section, most important first.

---

## :clipboard: Metadata Header

<details>
<summary><b>Every working page carries a research-status header</b>: the schema (click to expand). The sections below are a <em>view</em> of these values; the pages own them. Live example: <a href="files/h0-bimodality-test.md"><code>h0-bimodality-test.md</code></a> (a Test with every field). Checked by <a href="files/scripts/metadata-lint.py"><code>scripts/metadata-lint.py</code></a>.</summary>

```markdown
**Type:** Map | Program | Test | Result | Note
**State:** Open | Active | Blocked | Waiting | Closed | Reopened | Superseded
**Verdict:** Positive | Negative | Mixed | Inconclusive | Uninformative
**Status (YYYY-MM-DD):** ...
**Summary:** ...
**Gated by:** `gate:...`
**Inputs:** `page.md`, ...
**Parent:** `page.md`
**Frozen:** DATE surface; DATE surface
**Superseded by:** `page.md`
```

Field semantics, load-bearing:

- **Type** is the page's stable purpose. *Map* indexes work owned elsewhere; *Program* owns a research question; *Test* scores a claim against a pre-committed criterion; *Result* records a computation or derivation with no pre-committed pass condition; *Note* is a research sketch. Execution does not change Type: a Test stays a Test after it runs.
- **State** describes the page's current live research object, not the states of its internal branches; historical or branch-local states belong in Status. *Open* = unresolved, no concrete next action named. *Active* = unresolved, a concrete next research action is named. *Closed* = the investigation reached its endpoint. *Reopened* = a page that had reached closure and later became live again. *Superseded* requires a named **Superseded by:** successor; without one, use Closed. *Waiting* means the page itself cannot advance until an external condition arrives, not merely that future work exists elsewhere.
- **Verdict** appears only on `Type: Test`. A Result's outcome lives in State + Status; framework grades (MOTIVATED / SUPPORTED / DERIVED / CERTIFIED / FALSIFIED) are claim-strength, not a Verdict, and are never crosswalked. A Reopened test carries no current Verdict; its prior verdict is a Status fact.
- **Status** is mutable and dated: it changes when research advances, and its date is the date that research state was established (recovered from the last body-touching commit, never the cleanup-commit date). **Summary** is stable: it changes only if what the page is about changes. *If a sentence changes when a computation or derivation lands, it is Status; if only when the subject changes, it is Summary.*
- **Gated by** names a hard prerequisite result this page must *receive* from elsewhere. **Inputs** names material the page uses that does not block it. A page that *works* a gate is listed under the gate's **Worked by:**, and is never also **Gated by** that same gate.
- **Parent** is the *immediate* owning research record, not the highest-level program. A child sits directly under the record it is a subordinate execution or analysis of. A Map indexing a detail page is *not* its parent; that is what Related and Inputs are for.
- **Frozen** describes historical material *physically present in this page* that must not be repaired. A page that merely references frozen work owned by a child page does not carry the field.

`Related:` is retained untouched and is out of this schema's scope for now.

The metadata records the current research state; it does not replace the research record. Page bodies remain authoritative for derivation history, branch outcomes, and detailed adjudication.

</details>

---

## :closed_lock_with_key: Research Gates

A gate is a *result, not a date*: a hard mathematical or physical prerequisite, shared across at least two distinct research programs, that must resolve before downstream work can advance. A page names a gate it is waiting on with `**Gated by:**`; a page trying to resolve one is listed here under **Worked by**. A page may work a gate or be gated by it, never both for the same gate. All seven are currently **Open**; closing one is a propagation event that stales every page that named it.

| Gate | Frontier | State | Worked by | What must resolve |
|------|----------|-------|-----------|-------------------|
| `gate:selection-rule` | Selection | Open | [`fibonacci-wells.md`](files/fibonacci-wells.md), [`scaling-law-uniqueness.md`](files/scaling-law-uniqueness.md) | Why the realized wells, grids, and exponents are selected from the topology rather than adopted as a postulate. |
| `gate:amplitude-stress-tensor-dictionary` | Dynamics | Open | [`stress-tensor-bridge.md`](files/stress-tensor-bridge.md) *(construction parked 2026-09-24)* | The amplitude-to-$`T_{\mu\nu}`$ / $`E(S)`$ dictionary that would make the $`\Psi^2 \to S^2`$ transfer a stress-energy counterparty; downstream of the physical-$`\Lambda`$ interface. |
| `gate:clock-exponent-derivation` | Dynamics | Open | [`friedmann-as-output.md`](files/friedmann-as-output.md) | Derive the Waltz clock exponent $`dt/d\tau = S^{-1/2}`$ from the postulate layer, without importing it from GR. |
| `gate:shell-unlock-map` | Dynamics | Open | [`entropy-as-realization-budget.md`](files/entropy-as-realization-budget.md) | The $`S \mapsto N_\text{max}(S)`$ Molien shell-unlock map that sets the accessible mode count $`W_\text{modes}(S)`$. |
| `gate:three-halves-identity` | Dynamics | Open | *(none)* | Whether the clock $`3/2`$ and the Gauss-Codazzi $`3/2`$, numerically equal, are the same object. |
| `gate:variational-independence-bar` | Dynamics | Open | [`variational-score-to-sample.md`](files/variational-score-to-sample.md) *(parked 2026-09-23)* | Whether a proposed variational principle or action can be motivated independently of the outcome it is asked to produce, and then actually yield that outcome under variation. |
| `gate:galactic-curvature-sourcing` | galactic | Open | [`cone-point-coherence.md`](files/cone-point-coherence.md), [`oort-cloud-project.md`](files/oort-cloud-project.md) | What sources the curvature $`K_g`$ at galactic scale; GR tidal curvature in the flat-curve regime is structurally non-oscillatory. |

Two facts this registry makes visible. One gate has dependents but no worker: `gate:three-halves-identity`, which blocks two Dynamics programs and which no page is currently resolving. Two have only parked workers: since 2026-09-23, `gate:variational-independence-bar`, whose worker, [the variational program](files/variational-score-to-sample.md#16-parked), is parked under a standing admission bar while both foundations wait on it; and since 2026-09-24, `gate:amplitude-stress-tensor-dictionary`, whose worker, [the stress-tensor bridge](files/stress-tensor-bridge.md), has parked its construction step. And the Frontier's Calibration-closure problem has no registered gate: the R-determination question that would be one was demoted as a single program's open question, so Calibration closure is tracked by [The R Problem](files/r-problem.md) directly rather than through a gate. The scaling law's factorization was demoted the same way on 2026-09-23: its one registered dependent, the Fibonacci wells, does not need it, and its open step was restated from an algebra statement (`gate:commutant`) to boundary-mode uniformity, tracked on [Scaling Law Uniqueness](files/scaling-law-uniqueness.md) directly.

---

## :world_map: Maps

Orienting notes that index other work.

---

### [Claim Ledger](files/claim-ledger.md)

**Audit lens (2026-06-26):** A skeptical, framework-wide classification of every quantitative claim by epistemic type (forward prediction, zero-freedom structural result, internal theorem, loose comparison, calibration anchor, null result, open problem) and role. Separates the thin forward sector the framework lives or dies on (mostly Euclid DR1) from the retrodictions inside the calibration web, draws the web's eight cycles explicitly, and flags overclaims, double-counts, and the two real internal tensions: Cycle 2 ($`\alpha`$ is both input and output, so the 0.4% match is a consistency check) and Cycle 7 (the coupling-route and mass-route values of $`R`$ disagree ~3.2×). Built to keep the public pages honest, not as the framework's self-description; ends with a source-page triage queue.

**Inputs:** the whole framework's quantitative claims; see especially [The R Problem](files/r-problem.md) and [Calibration Structure](files/calibration-structure.md).

---

### [The R Problem](files/r-problem.md)

**Tracker:** Maps every route to an independent spatial curvature radius $`R`$ and where each stands. $`\Lambda_\text{ref} = 3/R^2`$ becomes a conditional output only with an $`R`$ not read off $`\Lambda`$, and identifying that reference value with the physical $`\Lambda`$ stays gated by the Interface: de Sitter is circular, the Molien gap is not independent, the CMB L-ratio factor of 8 is dead (no topological derivation), the coupling (α) route is the best-conditioned determination, and the particle mass spectrum is an independent, lower-resolution cross-check (executed, order of magnitude). Includes the shared E₈ / $`h = 30`$ engine tying the L ratio to the mass formula, and flags the Molien sparse-zone CMB result as the independent survivor of the L work.

**Inputs:** [R from the mass spectrum](files/r-from-mass-spectrum.md), fermion mass formula, $`\Lambda_\text{ref} = 3/R^2`$ reference relation.

---

### [Calibration Structure](files/calibration-structure.md)

**Summary:** Reframes the engine as a calibration scheme: one measured anchor per sector ($`H_0`$ edge, $`\Lambda`$ surface, $`m_e`$ mass-sector normalization), with the topology supplying the exponents, well assignments, and ratios. Localizes the R problem to a single demotion: $`\Lambda`$ moves from absolute prediction to measured calibration input, and nothing downstream collapses. Draft for a new engine section.

**Inputs:** a0 paper Appendix A.2, Λ eigenvalue, scaling law.

---

### [The Budget Map](files/budget-map.md)

**Tracker:** The inventory of what is a budget and what is read off one. There is a single conserved budget in this sector, the temporal $`\Psi^2 + S^2 = 1`$ (with the spatial $`u_0^2 + J^2 = 1`$ as its twin); temperature ($`T \propto 1/S`$) and entropy ($`\Sigma = k_B \ln W_\text{micro}`$) are two readings of its state $`S`$, not budgets, and the Waltz clock is a map from phase to time. Pins the distinction so the readings are not miscounted as parallel ledgers, the error the entropy note had to fix.

**Inputs:** [Temporal Budget](files/temporal-budget.md), [Energy as Resolution Amplitude](files/energy-as-resolution-amplitude.md), [Entropy as Realization Budget](files/entropy-as-realization-budget.md).

---

## :mountain_snow: Math Foundation

Closing any one of these upgrades everything downstream.

---

### [The Postulate Bridge](files/postulate-bridge.md)

**Tracker:** The two bedrock results sit on the two pieces of the postulate $`S^1 = \partial(\text{Möbius}) \hookrightarrow S^3`$, and whether a theorem connects them is open. The naive bridge through the shared $`2/R^2`$ is dead: the surface eigenvalue is $`\Gamma`$-blind and the Ricci floor is the only $`\Gamma`$-independent slot in the gap, so the match is a forced curvature-scale coincidence, not a spectral link, and $`2I`$'s perfectness ($`H^1 = 0`$) closes the orientation route as well. The route that ran is index theory on the $`E_8`$ plumbing that $`S^3/2I`$ bounds, where the McKay correspondence identifies the intersection-form $`E_8`$ with the gauge $`E_8`$; its gatekeeper was whether the boundary spectral asymmetry distinguishes the Galois connection $`Q'`$ from $`Q`$ by the same distance-six anomaly that gives the $`36/R^2`$ gap. Steps 1 to 3 are done (the gate is open; the framework and sign are fixed; the interior classes are computed and Galois-blind: [η-gatekeeper](files/eta-gatekeeper.md), [Step 2](files/step2-analytic-setup.md), [Step 3](files/step3-interior-classes.md)); the staged route is now complete, as a split: the gauge dictionary is proved (the $`E_8`$ filling carries the boundary's Galois asymmetry exactly) and the Möbius channel decouples route-specifically ([part one](files/step4-bookkeeping.md), [part two](files/step4-coupling.md)); no universal independence claim is made, and the result is now published as the standalone bedrock pillar [Galois pair](../bedrock/files/galois-pair.md).

A sampler reading of that split is recorded, now closed negative: the quotient carries the native spectrum while the Möbius geometry supplies a phase-sensitive readout, under which the recorded negatives are what the architecture predicts. Its new object, for a band in $`S^3`$, is the observation map $`f = \pi \circ i : M \to S^3/2I`$, which needs no descent of the band as a submanifold, and the sampling operator $`\mathcal O_M`$ it would carry. Its first test, whether an intensity observable factors through $`2I/\{\pm 1\} \cong I`$, is [run and closed negative twice over](files/sampler-first-test.md): no compact surface in $`S^3`$ with a single boundary circle is antipodally invariant, so the deck element $`-1`$ never stabilizes an admissible band; and independently, equivariance makes the transverse sampler's intensity profile identical on all $`120`$ deck translates, so no invariant scalar readout distinguishes lifts at any stabilizer size. Observables are assigned to the engine's 60R and 120 resolutions by the grid dictionary; the intensity is sign-blind in every sector, so it does not do the assigning. The residue is structural: for such bands the natural Möbius sampler is transverse rather than restrictive, and its open question is mode transfer rather than label identification.

A variational reading now sits over both, as program architecture rather than a fourth tier: the dynamics problem, at the level of the postulate, is a variational principle for the global score-to-sample relation, not a search for a conventional $`L(q,\dot q,t)`$; a conventional field action enters downstream, at $`\mathcal{S}_\text{eff}`$. The corpus phase $`t`$ stays fundamental and observer time is reconstructed through a lapse $`d\tau_H = N(t)\,dt`$, with the two-level descent $`\mathcal{S}_\text{MIT} \to \mathcal{S}_\text{eff}`$ carrying the sampled degrees of freedom. Its promotion gate is the observer clock: whether $`\delta\mathcal{S}_\text{MIT}/\delta N = 0`$ forces $`N = S^{1/2}`$ without the exponent being inserted by hand, with $`\Psi^2 + S^2 = 1`$ entering only as an on-shell constraint. The gate, the fixed conventions, the one bounded computation and its pre-registered PASS and FAIL conditions are on the program page, [Variational Score-to-Sample](files/variational-score-to-sample.md). Its first clock arm has run ([The Variational Clock Arm](files/variational-clock-arm.md)): in the program's class, a quadratic kinetic term with the lapse equation a genuine constraint, the potential's level sets the lapse and the variation selects none, so the independent route fails and the half power returns only as R-HALF's operator realization. It is now parked on the one question left, why the potential carries amplitude weight, with a standing admission bar for any proposal that claims to answer it.

The dynamical direction's Tier 2 has run its first computation ([The Tier 2 Fixed-Boundary Run](files/tier2-fixed-boundary.md)). The specified band, Lawson's Möbius band, is unstable under the fixed-boundary area functional, with index 2 and nullity 1. The index was already stated in the literature, and the nullity follows from a published computation. Every minimal Möbius band spanning a great circle is unstable the same way, so in that regime no smooth embedded band attains the infimum of area.

Where the carrier sits is ruled (2026-09-27) on [The Projective Carrier](files/projective-carrier.md): the vacuum carrier itself is unbent, so the carrier is realized through the projective layer, lifting to and embedding in $`\mathbb{RP}^3 = S^3/\{\pm I\}`$ with its core the central $`-I`$, and in the spinorial sectors the central sign is its Möbius holonomy. Its physical domain is $`\mathbb{RP}^3`$, by ruling (2026-10-02), and $`S^3/2I`$ is its observable domain; its pose relative to $`2I`$ is free. The conic band is the leading realization, not uniquely selected. Its stability is derived for the fixed-edge area problem, and an independent check frozen before the run has reproduced it blind: a fixed-edge theorem, not vacuum stability, which counts toward the Tier 2 bar only once the realization and the fixed edge are grounded. The alternatives the ruling set aside stay on that page as the decision's record, beside its inventory of the pages the ruling changed. Its cone extension is decided (2026-09-29): Friedrichs in both sectors, which needs no defect length. Its sampler is decided the same day: the transverse derivative, normalized at unit radius, for every block, one operator independent of spin and statistics. Its temporal edge is decided with it: time runs on the abstract boundary circle, of which the figure-eight is the image. Its boundary regime is decided (2026-10-01): the edge is held fixed, as a modeling input rather than a derived law.

**Gated by:** `gate:variational-independence-bar`

**Inputs:** [First eigenvalue](../bedrock/files/first-eigenvalue.md), [Coexact gap](../bedrock/files/coexact-gap.md).

---

## :house: Physics Foundation

Closing any one of these upgrades everything downstream.

---

### [Variational Score-to-Sample](files/variational-score-to-sample.md)

**Tracker (motivated; parked):** The program page for the variational reading, and the one entry here that both foundations wait on: its question is `gate:variational-independence-bar`, which [The Postulate Bridge](files/postulate-bridge.md) and [The Stress-Tensor Bridge](files/stress-tensor-bridge.md) each declare as a prerequisite, and the bridge already names the variational route preferred for its construction step. It frames the dynamics problem, at the level of the postulate, as a variational principle for the global score-to-sample relation rather than a search for a conventional $`L(q,\dot q,t)`$, a conventional field action entering downstream at $`\mathcal{S}_\text{eff}`$: the corpus phase $`t`$ stays fundamental, observer time is reconstructed through a lapse $`d\tau_H = N(t)\,dt`$, and a two-level descent $`\mathcal{S}_\text{MIT} \to \mathcal{S}_\text{eff}`$ carries the sampled degrees of freedom. The page fixes the corpus conventions any candidate must respect, states that architecture, names one bounded computation (vary $`N`$, $`S`$, and the constraint multiplier, then read off the lapse law), and pre-registers PASS and FAIL before the run, including the dressed-lapse case scored in advance so that "another clock" is not adjudicated afterwards. The clock exponent is not this page's to score: the program enters [Friedmann as Output](files/friedmann-as-output.md)'s route menu as R-VAR and promotes only on that page's terms. The first clock arm has run ([The Variational Clock Arm](files/variational-clock-arm.md)): the independent route fails, since the Rayleigh oscillator's own potential gives $`N = 1`$, and the half power returns only when the potential is assigned the amplitude level, as R-HALF's operator realization below the promotion bar. What remains is why the potential carries amplitude weight. The program is parked on that question (2026-09-23): no search is run, its later arms stay closed behind the clock gate, and a standing admission bar governs any future proposal, so the gate has no worker until a construction motivated for its own reasons meets it.

**Inputs:** [The Postulate Bridge](files/postulate-bridge.md), [Temporal Budget](files/temporal-budget.md), [Friedmann as Output](files/friedmann-as-output.md), [The Stress-Tensor Bridge](files/stress-tensor-bridge.md), the engine (chronon, sign flip, Hubble clock).

---

### [The Stress-Tensor Bridge](files/stress-tensor-bridge.md)

**Tracker:** Program page for the framework's one missing map, the ledger's $`E(S)`$: from the realized budget state to a stress tensor with a declared placement (which metric's Einstein equations it sources). The same object gates four opens at once: the Λ coefficient's physical identification ([cosmological constant](../../../cosmos/files/cosmological-constant.md) §IV), the Ψ²→S² counterparty, the cooling-energy accounting, and the matter-scaling import in $`H(z)`$. The page assembles the constraint set (static source, the perfect-fluid coefficient gate, the Friedmann mechanism fence, the Killing ledger, the fitted dictionary, the coincidence fences), states the three-way placement fork (physical-static, effective-metric, shifted coefficient), and carries the first cycle's results: the minimal scalar reading dead on its registered expectations; the fitted dictionary's tie promoted to a structural identity; two newly named metric-definition questions (curvature placement, Λ-dressing of the effective clock); the full flat D+Λ source and lapse pinned under the fixed $`a_\text{eff} = a_\ast S`$ placement; and the variational route ([postulate-bridge](files/postulate-bridge.md) dynamical tiers) promoted to preferred for the construction step. [The P1 Bridge](files/molien-p1-bridge.md) is folded in as of 2026-09-15: a candidate must now declare the fluctuation map it induces on the Molien shells and classify what that map carries (C7), and the spatial projection has its own route (R7), beside the variational route rather than under it, filling the spatial part of a hole where the page's success bar required the $`g_\text{static} \to g_\text{eff}`$ map that no assigned route could produce. R7's first calculation has since run on the fluctuation half, [The Shell-to-Direction Transfers](files/directional-transfers.md), classifying the admissible transfers shell by shell and stating exactly a sufficient axiom for the Q class. Its second, [The Shell-to-Radius Transfers](files/radial-transfers.md), classifies the radial transfers and adds C8: a candidate must declare which spectral operator, if any, its induced map intertwines. A construction attempt then found no spatial projection in the existing machinery, [The Missing Spatial Projection](files/missing-spatial-projection.md), and adds C9: no smooth pullback. The admissibility question for the new object that negative requires, [The Effective-Metric Floors](files/effective-metric-floors.md), found four floors on any candidate and nothing that says what the object is, and adds C10: a candidate must declare how the domain's isometries act on the flat target's rotations. A carrier theorem then classified what a deterministic field-level lift of one shell can be ([The Spatial Carriers](files/spatial-carriers.md)): finitely atomic spectra, no separately homogeneous deterministic field-level lift of P1 at finite N, and under A5 a shell's icosahedral orbit exactly when the shell contains its module. The OpenWave M8 program's results enter by citation as of 2026-09-24: its frozen slot target sits upstream of the map, a consumer the map alone leaves unpaid, and its kinematic close adds C11: native single-valued fields on the quotient, read geometrically, carry none of the eight nontrivial McKay slots, so a candidate's matter fields must leave that class; on the quotient the demonstrated realization is through twisted bundles. Construction is parked as of 2026-09-24 (§IX): no candidate action exists and none is built against the pinned target; candidates enter from the postulate bridge's target-free tiers, under the variational bar, or through the OpenWave M8 column, and meet one entry test. Nothing is derived: no $`X \to g_\text{eff}`$, no $`X \to T_\text{eff}`$, no action.

**Gated by:** `gate:variational-independence-bar` (the variational route R6 only; R7 is not gated by it)

**Inputs:** [cosmological constant](../../../cosmos/files/cosmological-constant.md) §IV, [The Budget Map](files/budget-map.md), [Friedmann as Output](files/friedmann-as-output.md), [Temporal Budget](files/temporal-budget.md), [Redshift and Cooling](files/redshift-and-cooling.md), [postulate-bridge](files/postulate-bridge.md), [The P1 Bridge](files/molien-p1-bridge.md), [The Molien Shells](files/molien-shells.md), [Surviving Ray](../bedrock/files/surviving-ray.md) §2.4.

---

### [The Slot Relation](files/slot-relation.md)

**Status (reported OPEN, 2026-10-04):** What MIT says the energies of stable states in the eight McKay slots obey: the energy relation OpenWave's M8.2 success ladder asks for in its last row. Registered before any derivation (frozen 2026-10-03), with the relation $`E_\rho = E_* F(\rho)`$ normalized by $`F(R_1) = 1`$ and three declared routes, and reported OPEN: none yields a relation. A slot energy's membership in the scaling law's class is not established, and the law's two rules for the weight are each blind to the representation; the inclusion $`S^3 \subset \mathbb{C}^2`$ gives the invariant-degree route a common homothety only geometrically, at the radius, one power of $`\sqrt{\Omega}`$ per McKay step rather than the elevator's $`1/30`$, and neither the degree-30 generator's role nor its normalization is derived; the Chern-Simons route was dropped, since no energy dictionary exists without an action. No relation is filed for M8.2's last row; a dynamics can still aim at its rows 2 to 6 without that claim.

**Inputs:** the mass spectrum's McKay distances, Scaling Law Uniqueness, the First Eigenvalue, Coexact Gap and Galois Pair papers (the Surviving Ray only as a later check), The Projective Carrier's rulings, OpenWave's M8.2 and M8.4.

---

### [The Slot Action](files/slot-action.md)

**Status (selected and frozen, 2026-10-04):** One common action for the eight slot fields on $`\mathbb{R} \times S^3/2I`$, selected without using any target behaviour and frozen: the wave operator of the slot bundles' Laplacian with the density quartic, the only common quartic built from the fibre metric alone and the Surviving Ray's density-type interaction, the restoring sign, no mass and no curvature coupling ($`\xi = 0`$, the minimal-coupling side of a published disagreement, with $`\xi = 1/6`$ the named alternative). It is the effective slot-amplitude theory an OpenWave M8 run would use, not MIT's physical matter action, and it is MOTIVATED, not derived. The frozen action decides M8.2's rows 2 and 3 for the zero background, and the lowest-level branches of five slots, without a run. Those lowest-level families have since received an orbital-stability theorem, as sets at every nonzero charge, and linear spectral stability at every member; every slot has an orbitally stable fixed-charge ground-state set ([The Slot Ground States](files/slot-ground-states.md)). Whether the sets in $`R_2`$, $`R_4`$ and $`R_5`$ form branches, and the stability of non-minimizing branches, remain open; there a run can still add continuation and stability. The Lorentz row has a frozen ceiling of local covariance.

**Inputs:** The Slot Relation, the Coexact Gap and Surviving Ray papers, the postulate bridge's bar, the variational program's freeze rule, the stress-tensor bridge's C11, The Projective Carrier's ruling, OpenWave's M8.2, M8.4 and MODELS.md.

---

### [Scaling Law Uniqueness](files/scaling-law-uniqueness.md)

**Status (phase family and hierarchy forced, factorization a conditional theorem):** $`A/A_P = C(\Theta) \cdot (\sqrt{\Omega})^{-n}`$ began as a declared measurement postulate. The phase family and the hierarchy are forced: the anti-periodic BC forces $`C(\Theta)`$'s sinusoidal family for the twisted class, which the untwisted class reads through $`\phi_0`$ under Friedrichs, and background symmetry (isotropy + orthogonality) selects the first-positive member, whose reading as an intensity at a fixed weight is a conditional theorem on adopted measurement premises; units fix the dimensional prefactor and exact homothety at definite weight fixes the power $`(\sqrt{\Omega})^{-n}`$ on the dilution sector. The factored form *separates* on a Schur + homothety + Lemma 8 argument within the spectral-boundary observable class: independent coordinates do not forbid a cross-term, and neither does a factored observable algebra, so the step, restated 2026-09-23, is boundary-mode uniformity: every contributing spectral block carries the first-positive profile $`C(\Theta)`$ times a fixed spectral weight, and for single-position observables a derived block-by-block lemma makes the factored form equivalent to it; the mass sector's geometric-mean seat is its own question. Since 2026-09-29 uniformity is a conditional theorem, for the pillar's operator on M(W) under the adopted Friedrichs extension (1e) and W < πR/2: its linear-readout half rests on adopted measurement premises, a quadratic readout among them, and its shared-boundary-mode half on the first-positive projection, an adopted premise that carries the keystone and that no registered sampler supplies ([The First-Positive Transfer Run](files/first-positive-transfer.md)). Whether the class exhausts the physical observables is a further premise. Off the form: the $`\alpha_W`$ twist, the extension *selection*, adopted as Friedrichs in both sectors (1e), and the $`\Omega_H = \Omega_\Lambda`$ coincidence.

**Inputs:** first positive eigenvalue (first-eigenvalue paper), Lemma 8 (spectral inaccessibility), Möbius topology axioms.

---

### [Friedmann as Output](files/friedmann-as-output.md)

**Tracker (the half-power clock, ε-scored):** The phase-clock $`H(z)`$ imports the Friedmann equation through exactly one line, the Waltz clock exponent $`-1/2`$, forced by $`S^3`$ dimensionality plus GR and empirically unique in its family ($`\Delta\chi^2 > 60`$ against integer alternatives). The tracker reduces the derivation to that exponent and enumerates the topologically native clock candidates; one, the self-dual clock under level exchange, lands $`-1/2`$ arithmetically through a three-gate argument ([the involution](files/half-power-involution.md), [the tick lemma](files/tick-lemma.md), a second consequence on the [entropy page](files/entropy-as-realization-budget.md)). The [registered measurement](files/clock-asymmetry-fit.md) meant to complete the case, the continuous $`\epsilon`$ fit, has run: zero excluded at 95% in both tiers, but diagnostics found the dial contaminated as a probe on this data, so the result neither confirms nor cleanly refutes. Adjudicated: P2 [supported by reduction](files/sampling-kernel-symmetry.md), empirically unscored; the FORCED label stays FORCED.

**Gated by:** `gate:shell-unlock-map`, `gate:three-halves-identity`

**Inputs:** [Temporal budget identity](files/temporal-budget.md), Waltz clock, spatial budget $`u_0^2 + J^2 = 1`$, Gauss-Codazzi embedding (assembly stage only).

---

### [Temporal Budget Identity](files/temporal-budget.md)

**Problem:** The phase-clock derivation rests on $`\Psi^2 + S^2 = 1`$ and the Waltz clock $`d\tau/dt = S^{1/2}`$, which, with $`\Omega_\Lambda = 0.685`$ held fixed, inherits $`\Omega_m = 0.315`$ by flat closure and fits at $`\Delta\chi^2 = +0.11`$ vs flat ΛCDM. The clock exponent $`n = -1/2`$ is empirically supported only against its discrete family (integer alternatives ruled out at $`\Delta\chi^2 > 60`$); the registered continuous diagnostic returned unscored, its dial diagnosed contaminated, and the exponent is not derived from the embedding. The two phase parameterizations ($`\Phi`$ engine phase and $`t`$ budget phase) are not yet reconciled.

**Gated by:** `gate:clock-exponent-derivation`, `gate:amplitude-stress-tensor-dictionary`, `gate:three-halves-identity`

**Inputs:** Möbius spatial budget $`u_0^2 + J^2 = 1`$, first positive eigenvalue (first-eigenvalue paper).

---

### [Fibonacci Wells](files/fibonacci-wells.md)

**Status (structurally reduced):** Why the stable sampling positions land at the Fibonacci wells $`\{13, 21, 34, 55\}`$. The external golden-ratio/Hurwitz route is abandoned (a rounded golden rotation selects a parity class, not the wells). The wells are reframed as the additive continuation of the icosahedral branch orders $`(2,3,5)`$ on the locked 120-grid, bounded below by the lcm seam ($`13`$ is the first Fibonacci not dividing $`120 = \text{lcm}(1,2,3,5,8)`$; divisors tile, non-divisors sample) and above by the antinode reflection $`C(k)=C(120-k)`$. The residual was a boundary-native anti-periodic interference functional, since the mirror's Lemma 8 rules out any bulk functional (the spectral side is $`\Theta`$-blind); a sweep of eight natural boundary-mode functionals selects the wells in none, so the residual most likely reads as structural rather than variational: why the post-lcm continuation of the icosahedral branch recurrence defines the wells. $`\varphi`$ enters internally through the $`\mathbb{Q}(\sqrt5)`$ character field, not Hurwitz.

**Inputs:** Scaling law uniqueness (phase operator $`C(\Theta)`$), the-mirror.md (Lemma 8, $`\mathbb{Q}(\sqrt5)`$, character ceiling), 120-domain selection.

---

### [Cone Point Coherence](files/cone-point-coherence.md)

**Problem:** Galactic coherence (all observers measuring the same $`\mathbb{R}^4`$) may be the $`W`$-independence of a nested eigenvalue problem, guaranteed by a cone point at galactic scale. The cone point analysis (Frobenius, Friedrichs, excision) that makes the cosmic eigenvalue well-defined must be re-established at galactic scale with equal rigor. Critical fork: GR tidal curvature in the flat-curve regime is Euler-type with power-law Jacobi solutions that structurally cannot zero, so the curvature has to come from the topology-gravity interface. SPARC has since falsified $`L_f = v_c^2/a_0`$ as the galactic coherence radius, which removes the empirical anchor for that reading and leaves the sourcing question open against an unknown $`L_g`$; Reading A and the Frobenius chain are untouched.

**Inputs:** first positive eigenvalue (first-eigenvalue paper), phase field coherence scale $`L_f`$ (SPARC-falsified; the unknown galactic scale is $`L_g`$), 120-grid scale-free projection.

---

### [Energy as Resolution Amplitude](files/energy-as-resolution-amplitude.md)

**Problem:** $`E^2 = (mc^2)^2 + (pc)^2`$ may be the Pythagorean theorem on the mode decomposition of the sampling operation: temporal-mode amplitude (rest mass) orthogonal to spatial-mode amplitude (momentum). Five promotion steps unwalked: spatial-mode coupling, orthogonality proof, $`c^2`$ factor from $`S^1`$ structure, Lorentz recovery as sampling symmetry, connection to mass formula.

**Inputs:** Standing wave $`\Psi = \cos(t/2)`$, scaling law, mass formula.

---

### [Redshift and Cooling](files/redshift-and-cooling.md)

**Note:** How a static universe reddens light and cools a bath, both readings of the budget's state $`S`$. Redshift is the phase ratio $`1 + z = S(t_\text{obs})/S(t_\text{emit})`$ on the standing wave; cooling is that same ratio on a blackbody, which stays a blackbody at $`T \propto 1/S`$ (ESTABLISHED as a kinematic equivalence with the FLRW thermal law). Not tired light, not expansion; the distance side rides on the Waltz clock.

**Inputs:** Temporal budget identity, standing wave $`\Psi = \cos(t/2)`$, Waltz clock.

---

### [Entropy as Realization Budget](files/entropy-as-realization-budget.md)

**Problem:** A static universe cools by budget transfer $`\Psi^2 \to S^2`$ ([Redshift and Cooling](files/redshift-and-cooling.md)), but the thermodynamic entropy is unsettled. Candidate: entropy is the spread of the resolution-amplitude budget over realized modes, so the second law is the transfer direction and the low past is forced by $`\Psi(0) = +1`$. The load-bearing open step is the shell-unlock map $`S \mapsto N_\text{max}(S)`$ from the $`2I`$ Molien shells, which sets the accessible-mode count $`W_\text{modes}(S)`$; entropy is the microstate count over it. Without the map the rising entropy is circular. Scoped to the realization sector, with the gravitational ledger (Penrose) left open.

**Inputs:** Temporal budget identity, Redshift and Cooling, energy as resolution amplitude, $`S^3/2I`$ Molien shell spectrum.

---

## :mag_right: Open Gaps

Technical gaps with specific paths forward.

---

### [Ω_Ψ(Θ): Frozen Derivation Question](files/omega-h-derivation.md)

**Problem:** [Black Double Zero's](../../../cosmos/files/black-hole.md) claims a "double zero" at the horizon, $`\Theta\to0`$ (derived) alongside $`\Omega_\Psi\to0`$ (conjectured). Even granting both, $`\Omega_\Psi`$ enters the scaling law inversely ($`\Omega_\Psi^{-n/2}`$), so the compound limit is $`0\times\infty`$, undetermined without the relation $`\Omega_\Psi(\Theta)`$. Frozen here, before any attempt, as: derive $`\Omega_\Psi(\Theta)`$ for a specified observer congruence (static, infalling, invariant norm, or a preferred MIT clock, these give physically different answers) and find the exponent $`p`$ in $`\Omega_\Psi\sim\Theta^p`$; the gate is $`C\cdot\Omega_\Psi^{-n/2}\sim\Theta^{2-pn/2}`$, vanishing/finite/divergent depending on $`p`$ versus $`4/n`$. A null result is a complete answer and requires no further correction to the now-hedged main page. The program is blocked on the congruence choice: the static channel gives $`p = 2`$, and a freely falling one $`p = 4`$ or a nonzero constant, so the compound limit stays underdetermined until the clock field is specified ([§V](files/omega-h-derivation.md#v-static-channel-resolved-general-question-underdetermined)).

**Inputs:** [Black Double Zero's](../../../cosmos/files/black-hole.md) §II, §VIII.1.

---

### [Oort Cloud Project: Nested Coherence Domains](files/oort-cloud-project.md)

**Problem:** Does MIT's structure project into every gravitationally coherent scale, or only the cosmological one? If the 120-grid and 3/2 conversion nest, the Oort Cloud (~144,000 AU) is the solar-system-scale coherence boundary. Central open question: what sets the coherence scale at each level. $`L_f = v_c^2/a_0`$ was the candidate, and SPARC falsified it as the galactic radius, so the generalization now runs from an unknown $`L_g`$ rather than from $`L_f`$. Downstream predictions include CMB-ecliptic alignment as a local sampling fingerprint.

**Inputs:** first positive eigenvalue (first-eigenvalue paper), phase field coherence scale $`L_f`$ (tested, falsified by SPARC; the unknown galactic coherence scale is $`L_g`$), 120-grid scale-free projection, 3/2 conversion (Gauss lift + de Sitter vacuum).

---

### [S³/2I and the OPH Carrier](files/s3-2i-oph-dictionary.md)

**Dictionary (2026-10-03):** Where MIT's reading of $`S^3/2I`$ meets the twelve-port carrier of Observer Patch Holography, each side computing in its own terms. Classically, the carrier's coset geometry is the base of the Seifert fibration of $`S^3/2I`$, and OPH's compatibility condition $`xyz = 1`$ is that base's orbifold relation. Computed in exact arithmetic against OPH's committed tables, OPH's two golden triplets are the adjoints $`\mathrm{Sym}^2 Q`$ and $`\mathrm{Sym}^2 Q^\prime`$ of the two irreducible flat connections, with the committed port frame on $`\mathrm{Sym}^2 Q`$; the shared Galois ordering is recorded as an ordering only. The Molien-shell work it named next has since been done in [The Molien Shells](files/molien-shells.md), whose sky step closed Uninformative ([step two](files/molien-step-two.md)); OPH's angular packet enters neither page.

**Inputs:** [Coexact gap](../bedrock/files/coexact-gap.md) §4.4, OPH's committed tables at commit 621edbb2, [golden-sector-match.test.py](files/scripts/golden-sector-match.test.py).

---

### [The Molien Shells](files/molien-shells.md)

**Source structure (2026-09-14):** What the surviving Molien shells of $`S^3/2I`$ carry, as MIT's CMB source structure. Up to $`N = 30`$ each shell holds a single $`2I`$-invariant form, and those forms' roots on the sphere are the icosahedron's vertices ($`N = 12`$), face centres ($`N = 20`$) and edge midpoints ($`N = 30`$), with $`N = 24`$ the square of the first; an executable checks the counts, the patterns and the even-spin descent to $`A_5`$, with four deliberately broken variants. The sky step's preregistered test, [The Molien Shells, Step Two](files/molien-step-two.md), closed Uninformative at its CAMB reproduction gate before any P1 quantity was computed; under its P1 prescription no points are identified, so the matched-circle observable is N/A. A theory-only registration of P1's full-transfer spectrum, [The Molien Shells: The Full-Transfer Ratio Table](files/molien-ratio-table.md), tabulates it at both radii: after an erratum to its interpolation, its second run found both routes Departing and Separated, a theory result not scored against data. [The Molien Shells: The P1 Bridge](files/molien-p1-bridge.md) answers the geometric part of what the source needs from MIT to reach the sky: the flat limit sends the canonical laws to P1, and below $`N = 60`$ a Q-symbol flattening would give a definite icosahedral pattern of directional power.

**Inputs:** [CMB Anomalies](../../../cosmos/files/cmb-anomalies.md) §IV, [molien-shells.test.py](files/scripts/molien-shells.test.py).

---

**Coupling and scaling exponents.** Each is a distinct single-principle-derivation gap on a gauge or scaling exponent; the load-bearing number stays in place.

- **dist/30 Hierarchy Exponent:** The McKay elevator's denominator is the Coxeter number $`h(E_8) = 30`$, stated on [the mass spectrum](../../../spectrum/files/mass-spectrum.md) page and not derived; a single-principle derivation is open. *Deps:* McKay correspondence, $`E_8`$ Coxeter number.
- **Scale Consistency:** Three gauge couplings evaluated at different energy scales; $`\alpha`$ hits 0.4% at low energy but 6.2% at $`M_Z`$, so the framework must commit to one evaluation scale or derive running from MIT structure. *Deps:* gauge coupling derivation (engine §15), scaling law.
- **$`\alpha`$ Exponent:** The $`\alpha`$ exponent equals the minimum grid step; two convergent paths motivate it and the uniqueness scan checks it, its two possible grids are derived from the central sign, and the Casimir route to forcing the exponent is closed ([Scaling Law](files/scaling-law-uniqueness.md#ladder-rule-grids)); a single-principle derivation is open. *Deps:* grid structure, scaling law.
- **Plato Twist Derivation:** the value $`\cos(\pi/10)`$ has a computed geometric realization, the spin lift of the Levi-Civita holonomy around the shortest closed geodesic of $`S^3/2I`$, where the flat $`2I`$ holonomy gives $`\cos(\pi/5)`$ instead; the open link is its insertion into the weak coupling: which loop, which power, and why the weak row alone. See [The Plato Twist](files/plato-twist.md). *Deps:* spin structure of $`S^3/2I`$, stabilizer decomposition.

---

**Selection rules.** Why one structure is picked over its alternative, not yet derived.

- **Grid Ladder Selection Rule:** The two nontrivial image orders, $`D = 60`$ and $`D = 120`$, are fixed by the central sign ([Scaling Law](files/scaling-law-uniqueness.md#ladder-rule-grids)); which carrier or target roles are assigned to the integer-spin or spinorial class stays the motivated ladder assignment. *Deps:* stabilizer decomposition, boson/fermion domain split.
- **Anti-periodic BC Selection:** 4 of 8 charged fermion masses within ×3 after sector-first adjudication, 5 with a compatible entry (descriptive; the ×3 count is density, per the [torsion null test](files/mass-null-test.md)); first-principles derivation of why anti-periodic boundary conditions are selected over periodic remains open. *Deps:* Möbius non-orientability, mass formula.

---

**Neutrino sector.**

- **Neutrino Mass Ratios:** $`\mu_\Lambda`$ as the neutrino floor is motivated; the octave selection and multipliers (4, 22) are identified but not derived from the group theory. *Deps:* mass formula, $`\Lambda`$ eigenvalue.

---

**Superseded and secondary routes.**

- **240 Alternative for $`\alpha_s`$:** $`C(17/120) \times \Omega^{-1/240}`$ sits 1% behind the primary formula, with $`240 = 2 \times 120`$; excluded under the image reading of the grid, since no quotient of $`2I`$ has order 240 ([Scaling Law](files/scaling-law-uniqueness.md#ladder-rule-grids)), and it survives only under another reading of 240. *Deps:* grid ladder selection rule, scaling law.
- **$`L_\text{strip}/L_\text{fund}`$ Ratio:** The factor of 8 has no topological derivation, so this is a dead route to $`R`$, superseded by the coupling (α) route, the best-conditioned determination, with the mass spectrum an independent, lower-resolution cross-check (see [The R Problem](files/r-problem.md)).

---

## :white_check_mark: Results

Closed: executed computations and derivations with their outcomes in hand.

---

### [The Slot Ground States](files/slot-ground-states.md)

**Result (2026-10-05):** Whether the frozen slot action carries orbitally stable nonlinear states without a run. At every nonzero charge, every slot has energy minimizers at fixed charge, each a standing wave, and the set of them is orbitally stable; whether the sets in $`R_2`$, $`R_4`$ and $`R_5`$ form branches remains open. In the five rigid slots and the control they are the exact lowest-level family, orbitally stable as a set at every nonzero charge, with the linearization's whole spectrum on the imaginary axis at every member; that supplies both parts of the slot action's §VII stability protocol for those branches under M8.4's persistence label, and on OpenWave the rung is a filing's to adjudicate. In $`R_4`$ and $`R_5`$ no ground state lies entirely in the lowest free eigenspace; in $`R_2`$ that question stays open. The soft blocks' reduced quartic comes out in closed form, giving OpenWave's D7 weights and $`R_2`$'s coefficients. The stability mechanism is generic.

**Inputs:** [The Slot Action](files/slot-action.md) §V, §VI item 6, §VII and §IX, OpenWave's M8.12 record, [scripts](files/scripts/slot-ground-states/).

**Parent:** [The Slot Action](files/slot-action.md)

---

### [The First-Positive Transfer Run](files/first-positive-transfer.md)

**Result (2026-09-29):** Condition 1's first transfer computation, run blind against terms frozen before it: how much of the sampled output of eighteen ambient harmonic blocks, two for every irreducible of $`2I`$, reaches the conic band's first positive mode. None stays there. Under the value and the transverse sampler, in the twisted and the untwisted class, under every registered cone condition and at every registered placement and width, at least two thirds of each block's sampled norm lies outside the first-positive eigenspace, and under Friedrichs most of it lies at higher levels. The lowest blocks settle this at every pose and width without numerics. So neither registered sampler supplies the first-positive projection, and the scaling law carries it as an adopted premise; nothing is falsified. From the run's spectral step, corrected in review for a missed negative level, the review adds that under the same cone-trace matching the untwisted problem has no level at $`2/R^2`$ below the critical width, for any $`\delta_0`$; with the premise, uniformity then fails for untwisted contributing blocks.

**Inputs:** [Scaling Law Uniqueness](files/scaling-law-uniqueness.md) Step C, [The Projective Carrier](files/projective-carrier.md) §II, [First eigenvalue](../bedrock/files/first-eigenvalue.md), [scripts](files/scripts/first-positive-transfer/).

**Parent:** [Scaling Law Uniqueness](files/scaling-law-uniqueness.md)

---

### [The Carrier's Edge Regimes](files/carrier-edge-regimes.md)

**Result (2026-10-01):** Whether a variational regime with a movable edge selects the conic carrier. With the edge free, the free-edged membrane energies the Tier 2 ground floor names do not. On unbent bands each reduces to an effective sheet tension times area plus a line tension times edge length. With line tension, the tension opens the cone point's pinch at first order at every width; with the pinch held and zero effective sheet tension, the conic bands are the least-energy unbent bands, with the width a flat direction. Without line tension every unbent band ties at zero effective sheet tension, and none is critical otherwise. For the supported boundary, the totally geodesic support fitted to the carrier's edge lines leaves it unstable under nonzero effective sheet tension and flat in its width at zero; the framework supplies no support, and other supports stay open. The fixed edge stays the one regime here shown to hold the carrier stable with no null direction, for its declared class of variations, and there the edge is input.

**Inputs:** [The Projective Carrier](files/projective-carrier.md) Propositions 3.1 and 4.2, §XI 1b and 1c, [The Postulate Bridge](files/postulate-bridge.md) Tier 2, [scripts](files/scripts/carrier-edge-regimes/).

**Parent:** [The Projective Carrier](files/projective-carrier.md)

---

### [The Smoothed-Cone Limit](files/smoothed-cone-limit.md)

**Program (2026-10-03):** Declared before any computation: whether smoothing the conic band's pinch selects the Friedrichs realization the carrier adopts (1e) or a transmitting one. The class is the metric $`dy^2 + (\cos^2(y/R) + \varepsilon^2)\,dw^2`$, the pinch opened into a neck; what counts, the cross-check curves and the nonclaims are fixed. Proposition 1 then derives the limit for the class: Friedrichs, eigenvalue by eigenvalue, with the twisted bottom of order $`1/\ln(1/\varepsilon)`$; the first-eigenvalue paper carries its twisted case as Proposition 7.1. The cross-check computes the $`n = 0`$ levels: the twisted bottom approaches the declared curve and meets it to the integration's floor at $`\varepsilon \le 10^{-6}`$, and the twisted and untwisted levels merge at a rate consistent with $`1/\ln(1/\varepsilon)`$.

**Inputs:** [First eigenvalue](../bedrock/files/first-eigenvalue.md) §7, [The Projective Carrier](files/projective-carrier.md) §XI 1e, [Scaling Law Uniqueness](files/scaling-law-uniqueness.md), [scripts](files/scripts/smoothed-cone-limit/).

**Parent:** [The Projective Carrier](files/projective-carrier.md)

---

### [The Fixed-Edge Stability Check](files/fixed-edge-check.md)

**Result (2026-10-01):** The independent check registered with the projective carrier's §IX, run blind on OpenWave as M8.14 and scored against the frozen terms: Reproduced. Two blind rooms derived the reduction to the lune, each by its own route, and its Dirichlet spectrum, and the frozen cross-check matched the lune's bottom at all five widths, with a largest miss of three parts in ten million. The check cannot see the seam's twist, and the result is a fixed-edge theorem, not vacuum stability.

**Inputs:** [The Projective Carrier](files/projective-carrier.md) §IX, [the M8.14 record](https://github.com/openwave-labs/openwave/blob/63c5d03db2e22d7c94200886ead7f63037f41b7b/openwave/xperiments/m8_mit/research/findings/m8_14_method_note.md).

**Parent:** [The Projective Carrier](files/projective-carrier.md)

---

### [R from the Particle Mass Spectrum](files/r-from-mass-spectrum.md)

**Result (2026-06-15):** Determines the spatial curvature radius $`R`$ from the fermion mass formula's dependence on the hierarchy factor $`\Omega_\Lambda`$, independently of $`\Lambda`$, the CMB, and the de Sitter relation, breaking the R-problem circularity. Electron + muon give $`R \sim 20`$ Gpc and $`\Lambda \sim 8.1 \times 10^{-54}\,\text{m}^{-2}`$, about 13.4× (one order of magnitude) below the observed value. Precision is capped at order of magnitude by the McKay-lever amplification (60× for $`\delta d = 1`$) acting on the mass formula's current few-percent residual scatter. Since the 2026-07-28 torsion correction the muon-top pair is the best assigned pair ($`R \approx 10.5`$ Gpc, $`\Lambda`$ within 3.8×), and electron-muon remains the lepton-only cross-check. The route is an independent, lower-resolution cross-check on the coupling (α) route, the best-conditioned determination of $`R`$ ([The R Problem](files/r-problem.md)).

**Inputs:** Fermion mass formula and torsion table, McKay residual scatter (sets the precision floor), $`\Omega_\Lambda`$ hierarchy, $`\Lambda_\text{ref} = 3/R^2`$ reference relation.

---

### [McKay Propagator Correction](files/mckay-propagator-correction.md)

**Result (2026-10-03):** negative. The registered re-test of the literal $`\Pi_T`$ path product failed in both directions on the corrected table ([result](files/mckay-propagator-correction.md#retest-result)); with the page's other parameter-free forms failing the same grade after the run and its remaining forms outside the parameter-free class, no parameter-free propagator form on it survives, and d and τ stand as two overshoots, with no common mechanism claimed. The question had been reopened by the torsion correction (2026-07-28): the 2026-06 verdict (no parameter-free propagator or branch-point correction tracks the high-distance mass residuals; the route was closed, the residuals read as irreducible scatter) was computed on the pre-correction torsion table. The [half-integer torsion correction](files/torsion-correction.md) revised twelve of the twenty-four products and the whole mass comparison, so the propagator question was reopened; the frozen 2026-06 record, with its overshoot figures and vacuum-dependent hits, is preserved on the [linked page](files/mckay-propagator-correction.md) under its 2026-07-28 banner. Separately, the Coxeter-Galois gate still locks all $`R_4`$ entries to $`T_3 = -1/2`$, and charm remains unplaced.

**Inputs:** McKay graph for $`2I`$, $`C_\text{geom}`$ values for all irreps, torsion table $`T^2(\rho \otimes \sigma)`$ across vacua, Coxeter-Galois gate, [scripts](files/scripts/mckay-propagator-retest/).

---

### [The Variational Clock Arm](files/variational-clock-arm.md)

**Result (2026-09-23):** The variational program's first clock arm, run in the class the program names: a quadratic kinetic term, with the lapse equation a genuine constraint. There the lapse exponent is half the level difference between the kinetic and potential terms, and the standing wave solves the constrained variation at every potential level, so the variation selects nothing. With the Rayleigh form as the kinetic term, at the intensity level on shell because the realized share is twice the wave's rate, the oscillator's own potential gives $`N = 1`$, the dead phase clock: the independent route fails. $`N = S^{1/2}`$ appears only with the potential at the amplitude level, and then the on-shell action carries the $`S^{3/2}`$ tick weight automatically: an operator realization of R-HALF, below the promotion bar, with gate (iii) unmet on all three pre-named second consequences. Reparametrization invariance supplies the geometric mean once the levels are chosen, which also means a clean $`\epsilon \neq 0`$ would cost the class or the native-level assignment, not just a premise. Variational mechanics supplies the mean; MIT still has to supply the level pair. A script checks every statement against a control.

**Inputs:** [Variational Score-to-Sample](files/variational-score-to-sample.md) §4, §7, §11, §14, [The Half-Power Clock](files/friedmann-as-output.md) §II, §III, [The Tick Lemma](files/tick-lemma.md) §III, [The Clock-Asymmetry Fit](files/clock-asymmetry-fit.md), [clock_arm_check.py](files/scripts/variational-clock-arm/clock_arm_check.py).

**Parent:** [Variational Score-to-Sample](files/variational-score-to-sample.md)

---

### [The Tier 2 Fixed-Boundary Run](files/tier2-fixed-boundary.md)

**Result (2026-09-23):** The postulate bridge's first Tier 2 computation, run blind against terms frozen before it: the Dirichlet Jacobi spectrum of a specified minimal Möbius band bounded by a great circle in $`S^3`$. The band is Lawson's Möbius band, half of his Klein bottle $`\tau_{2,1}`$. Its index is 2, carried by $`\langle e_3, \nu\rangle`$ and $`\langle e_4, \nu\rangle`$ at $`-2/R^2`$ exactly, and its nullity is 1, the rotation about the boundary circle: it is unstable. Both values follow by reflection from Morozov and Penskoi's index 7 and nullity 5 for the closed Klein bottle. The index was also stated by Bernstein and Ketover the day before the freeze; a standalone statement of the nullity was not located. The review adds that no smooth embedded Möbius band spanning a great circle attains the infimum of area, whose value stays open. The eigenvalue $`-2/R^2`$ belongs to every minimal surface in $`S^3`$ and counts for nothing.

**Inputs:** [The Postulate Bridge](files/postulate-bridge.md) (the Tier 2 ground floor), [scripts](files/scripts/tier2-fixed-boundary/).

**Parent:** [The Postulate Bridge](files/postulate-bridge.md)

---

### [The Molien Shells: The Full-Transfer Ratio Table](files/molien-ratio-table.md)

**Result (2026-09-14):** The low-ℓ temperature spectrum that the P1 spectral-transfer prescription gives the Molien shells of $`S^3/2I`$ at MIT's two radii, as per-multipole ratios to ΛCDM through CAMB 2.0.4's full transfer function, with no data. Both routes come out Departing and Separated, in the frozen computation and in a repeat at a higher accuracy boost. At the coupling radius, 6130 Mpc, the quadrupole sits at 7.6% of ΛCDM's and the ratios reach 1.6 at ℓ = 27 and 28, with K_min = 109; at the electron-muon radius, 19700 Mpc, the quadrupole sits at 29%, ℓ = 7 to 9 at 1.3 to 1.6 times, and the ratios within 0.84 to 1.2 from ℓ = 12 up, with K_min = 9.6. So no Planck-era likelihood test is built for either route; the table is a theory result, not scored against data. The first run stopped at the shell-sum gate, and an erratum to the interpolation preceded the second.

**Inputs:** [The Molien Shells](files/molien-shells.md), [The Molien Shells, Step Two](files/molien-step-two.md), CAMB 2.0.4 at the Planck 2018 best fit base_plikHM_TTTEEE_lowE.

---

### [The Shell-to-Direction Transfers](files/directional-transfers.md)

**Result (2026-09-15):** The first calculation of the [Stress-Tensor Bridge](files/stress-tensor-bridge.md)'s R7, on the fluctuation half of the static-to-effective projection. The positive, linear, SU(2)-covariant maps from a Molien shell's source covariance to a power over flat wave-vector directions form an $`(N+1)`$-parameter cone, which normalization cuts to an $`N`$-simplex, so positivity, covariance and normalization select no member: P1's spectral transfer is the simplex's barycenter and the Q-symbol transfer one of its vertices. On a real field only the pair sums $`t_m + t_{-m}`$ act, which leaves an $`N/2`$-simplex in which Q and the antipodal Q are one vertex. Preserving the nodal directions of every pure source on the shell selects Q, as a theorem, once the transfer is normalized, and on a real field the Q class; preserving them only for the shell's own invariant, the version that can be formulated from the realized source alone below $`N = 60`$, leaves the predicted directional pattern 2, 5 and 8 free parameters at $`N = 12, 20`$ and $`30`$, enough to reverse the sign of its leading icosahedral multipole, with an explicit second member at each that the weak condition cannot separate from Q. A sufficient axiom for the Q class is thereby stated exactly; absent it, the projection must supply its own point in the family. A script checks the classification, the real-field quotient, both hypotheses, what reaches a single-state source, and the nodal sets, independently reproducing step one's constellations.

**Inputs:** [The Molien Shells: The P1 Bridge](files/molien-p1-bridge.md) §II, §V-VI, [The Molien Shells](files/molien-shells.md), [The Stress-Tensor Bridge](files/stress-tensor-bridge.md), [The Surviving Ray](../bedrock/files/surviving-ray.md) §2.2, §3.4, §5.7, [transfer_classification.py](files/scripts/directional-transfer/transfer_classification.py).

**Parent:** [The Stress-Tensor Bridge](files/stress-tensor-bridge.md)

---

### [The Shell-to-Radius Transfers](files/radial-transfers.md)

**Result (2026-09-15):** The second calculation of the [Stress-Tensor Bridge](files/stress-tensor-bridge.md)'s R7, on the radial label the first took as given. When a transfer from a Molien shell's source covariance to a flat power may move power between wavenumbers and between shells, positivity, SU(2)-covariance, reality and normalization give each shell a probability measure over wavenumber and pair sum, and leave its radial profile free. P1's rule, shell $`N`$ at $`k_N = \sqrt{N(N+2)}/R`$, is selected three ways: exactly by carrying the $`S^3`$ Laplacian to the flat one, as $`N`$ grows by the flat limit, and at every $`N`$ by locality, since matching a shell's correlations around the observer fixes its mean squared wavenumber at $`N(N+2)/R^2`$, no positive flat spectrum matches them to fourth order, and no width comes closest. Locality prefers zero width but leaves finite width possible: a width of about $`1/(\sqrt3 R)`$, 4.5% of $`k_{12}`$, costs no more at fourth order than the curvature already does. A width acts first on the phases behind the ratio table's per-multipole structure, which at route A needs each shell's width below about $`0.2/\chi_*`$, 0.78% of $`k_{12}`$; the bridge carries this as C8. A script checks the two local identities exactly, on anisotropic shell functions too, and every figure.

**Inputs:** [The Shell-to-Direction Transfers](files/directional-transfers.md) §II, [The Molien Shells: The P1 Bridge](files/molien-p1-bridge.md) §V, [The Molien Shells: The Full-Transfer Ratio Table](files/molien-ratio-table.md) §6, §8, [radial_check.py](files/scripts/radial-transfer/radial_check.py).

**Parent:** [The Stress-Tensor Bridge](files/stress-tensor-bridge.md)

---

### [The Missing Spatial Projection](files/missing-spatial-projection.md)

**Result (2026-09-15):** R7's construction attempt, run under a work order frozen before it, and a registered negative: MIT's existing sampler, embedding and observer machinery supplies no map from the static $`S^3/2I`$ to flat three-space, since every permitted object lands on the domain, the Möbius band, the phase circle or a scalar readout. Two routes to a flat target are closed by theorem: no smooth pullback carries a nonconstant homogeneous law to a translation-homogeneous one, since $`A_5`$ isotropy ties its gradient covariance to the metric and the domain is curved, and no translations can be inherited from the domain's isometries. The third route, linear maps that are neither, stays open, and the existing objects supply none. The missing object is specified: a flat target with its own translations, a map that does not preserve distances, linearity and positivity, and a comoving scale tie. A script checks the obstructions against their controls.

**Inputs:** [The Stress-Tensor Bridge](files/stress-tensor-bridge.md), [The Shell-to-Radius Transfers](files/radial-transfers.md), [The Molien Shells: The P1 Bridge](files/molien-p1-bridge.md) §II, §V, [postulate-bridge](files/postulate-bridge.md), [missing_projection_check.py](files/scripts/missing-spatial-projection/missing_projection_check.py).

**Parent:** [The Stress-Tensor Bridge](files/stress-tensor-bridge.md)

---

### [The Effective-Metric Floors](files/effective-metric-floors.md)

**Result (2026-09-15):** The admissibility question for the new effective-metric object that [The Missing Spatial Projection](files/missing-spatial-projection.md) found MIT to lack, run under a work order frozen before it: does anything in MIT constrain the spatial projection independently of wanting flat space, and does any such constraint say what the projection is? Four constraints survive and none says what it is, so no candidate is written down. They are floors on any future object: the same map at every point, with only the isotropy group $`A_5`$ inherited at a fixed observer; locality, with root-mean-square wavenumber $`k_N`$; no new dimensionful scale; and time dependence by the phase ratio over a static substrate. The domain's transitive $`SO(3)`$ is identified with the flat target's rotations only in the flat limit, so the directional and radial classifications of the transfer family rest on an identification a candidate must earn. Without it a shell's directional pattern can be any nonnegative $`A_5`$-invariant function, and the conservation of each shell's power, on which the ratio table's weights rest, becomes a condition of its own; the bridge carries this as C10. A script checks the $`A_5`$ statements against their controls.

**Inputs:** [The Missing Spatial Projection](files/missing-spatial-projection.md), [The Stress-Tensor Bridge](files/stress-tensor-bridge.md), [The Shell-to-Direction Transfers](files/directional-transfers.md) §II, §V, [The Shell-to-Radius Transfers](files/radial-transfers.md) §II-III, [The Molien Shells: The P1 Bridge](files/molien-p1-bridge.md) §II, §IV, §V, [a5_family_check.py](files/scripts/effective-metric-floors/a5_family_check.py).

**Parent:** [The Stress-Tensor Bridge](files/stress-tensor-bridge.md)

---

### [The Spatial Carriers](files/spatial-carriers.md)

**Result (2026-09-15):** What form a deterministic field-level lift of one Molien shell can take, asked under a work order frozen before it. A linear map from a shell's fields to fields on flat space, whose contribution is separately homogeneous, has a finitely atomic spectrum with at most $`m_N(N+1)`$ atoms, and the bound is attained. P1's uniform angular measure is not atomic, so no such map induces it at finite $`N`$, and [the ratio table](files/molien-ratio-table.md) stands as the exact result of the frozen P1 prescription. Full rotation equivariance leaves only the zero map at the tested shells. At those shells a nonzero $`A_5`$-equivariant carrier is a single icosahedral orbit, and which a shell admits is decided by whether the shell contains the orbit's module, not by counting: none at $`N = 12`$ once locality is imposed, the twelve five-fold directions at $`N = 20`$, those or the twenty three-fold directions at $`N = 30`$. Where a carrier exists it reproduces the table's contribution for that shell, since only the angle-integrated power enters $`C_\ell`$. Those carriers do not assemble, since an object owes every shell its power and the first admits none, so across the tested shells there is no admissible $`A_5`$-equivariant field-level lift and no replacement for the table. A script checks the bound, both tests, the carriers and the scalar power conservation fixes, each against a control.

**Inputs:** [The Effective-Metric Floors](files/effective-metric-floors.md) §III, §V, [The Missing Spatial Projection](files/missing-spatial-projection.md) §IV, [The Stress-Tensor Bridge](files/stress-tensor-bridge.md) C7-C10, [The Shell-to-Direction Transfers](files/directional-transfers.md) §II, [The Shell-to-Radius Transfers](files/radial-transfers.md) §II-III, [The Molien Shells: The P1 Bridge](files/molien-p1-bridge.md) §II, §IV, [carrier_check.py](files/scripts/spatial-carriers/carrier_check.py).

**Parent:** [The Stress-Tensor Bridge](files/stress-tensor-bridge.md)

---

### [The Molien Shells: The P1 Bridge](files/molien-p1-bridge.md)

**Result (2026-09-14):** What the Molien-shell source needs from MIT to reach the sky, answered for its geometric part. $`S^3/2I`$ is homogeneous with isotropy group $`A_5`$ at every point, so under any map that preserves it the quadrupole is isotropic and uncorrelated with the octupole. A construction that keeps only the shells' spectrum gives an isotropic law, P1's counterpart; the quotient's own law carries P2's identifications, which no homogeneous flat law can keep. The flat limit sends both canonical laws to P1, so the fork between flattenings is localized to the low shells, while from $`N = 60`$ a non-scalar source shape can carry an anisotropy to high $`N`$. Below $`N = 60`$ a Q-symbol flattening would give a definite icosahedral pattern of directional power, with zeros on the invariant forms' roots; why MIT's flattening would act that way is the missing statement.

**Inputs:** [The Molien Shells](files/molien-shells.md), [The Molien Shells, Step Two](files/molien-step-two.md), [The Stress-Tensor Bridge](files/stress-tensor-bridge.md), [isotropy_check.py](files/scripts/molien-p1-bridge/isotropy_check.py), [quotient_half_check.py](files/scripts/molien-p1-bridge/quotient_half_check.py), [flattening_check.py](files/scripts/molien-p1-bridge/flattening_check.py).

---

## :file_cabinet: Data Tests

Registered and exploratory tests run against public datasets, with verdicts.

---

### [Phase Field Coherence Scale (SPARC)](files/sparc-phase-field.md)

**Test:** Does $`L_f = v_c^2/a_0`$ behave as a galactic coherence radius across the SPARC sample, after controlling for ordinary size scaling? Pre-registered pipeline, frozen at tag `v1.0-preregistration` (DOI 10.5281/zenodo.20271702), run once against 123 quality-filtered galaxies.

**Result (2026-05-19):** The registered predictions are not borne out. The transition radius tracks $`L_f`$ with slope ≈ 0.23 (registered [0.7, 1.3]); 53.7% of flat-curve galaxies fall below the closure threshold (registered limit 5%). Verdicts stable across all 27 sensitivity-grid cells. $`L_f`$ is not the coherence radius the framework posited, and the closure identity does not hold. The lattice arithmetic is untouched.

---

### [H₀ Bimodality (Discrete-vs-Continuous Fork)](files/h0-bimodality-test.md)

**Test:** Do published H₀ measurements cluster into two discrete populations (~67 and ~73), as the Hubble-tension Section V fork predicts, or form a continuous spread? Hartigan dip test, Gaussian mixture, and gap test on 18 compiled measurements (13-row independent subset). Exploratory, not pre-registered.

**Result (2026-05-19):** The discrete two-cluster prediction is not supported. The dip test fails to reject unimodality in every configuration (primary p = 0.217); the Gaussian mixture's 2-component preference is statistically negligible (ΔBIC < 1.2) and points to clusters at 68.4 / 73.5 rather than 67 / 73; the predicted 69-71 gap contains TRGB / CCHP at 69.8. The data sorts by calibration class but does not quantize.

**Respecification (2026-09-02):** The original test compared against two clusters, but the [hubble-tension](../../../cosmos/files/hubble-tension.md) lattice has three values (67.40, 70.24, 73.04) and the middle one falls inside the 69-71 gap this test treated as empty. Re-running with the three centres fixed removes that specification defect and still returns no lattice-specific evidence: the fixed-centre model is the nominal BIC minimum in all eight cells, but its middle component carries weight exactly zero in every one, including on the current TRGB value sitting 0.15 from that centre.

---

### [Torsion Null Test (Mass Scorecard)](files/mass-null-test.md)

**Test:** Does the fermion mass scorecard's within-×3 hit rate carry information about the specific torsion values, or is it density? Pre-registered design frozen at tag `mass-null-v1.0`, one registered run (Generator PCG64, seed 120, $`M = 100{,}000`$). Statistic: the compatible-coverage count $`S_1`$ under four nulls (permute the 24 torsions across slots, within-vacuum, log-uniform redraw, within-spin-class exact), verdict fixed on Null A.

**Result (2026-07-28):** The ×3 count is uninformative about the torsion values. Randomly reassigning the 24 torsion factors across the fixed quantum-number slots reproduces or exceeds the observed coverage in 69.0% of draws (Null A, $`p_A = 0.690`$; the null $`S_1`$ mean of 5.02 sits at the observed coverage of 5, and the B / C / D secondaries stay far above the 0.01 information band). The mass table's evidential weight rests on the structural outputs (the 24-entry count, the $`T_3`$ gate evaluations, the $`\varphi^{-4}`$ ratio) and the falsifiable outliers, not on the ×3 proximity count; the test does not validate those structural outputs, it removes the proximity scorecard as torsion evidence. This is the re-run on the corrected torsion table (tag `mass-null-v1.1`); the pre-correction run (`mass-null-v1.0`, $`p_A = 0.174`$) is retained as history. Design frozen before each run (tag on the frozen bundle), results committed separately.

---

### [The Molien Shells, Step Two (Preregistered Low-ℓ Test)](files/molien-step-two.md)

**Test:** How does the Molien shell spectrum of $`S^3/2I`$, carried to the sky by the P1 spectral-transfer prescription, score against ΛCDM on the Planck 2018 low-ℓ temperature likelihood, at each of MIT's two independently read radii? Frozen before any run: the prescription, the shell weights, both radii, the codes and data pinned by hash, three gates, and ±2 decision bands on $`\Delta \ln L`$. Route A (the coupling radius, 6.13 Gpc) sets the Verdict; route B (the electron-muon radius, 19.7 Gpc) is reported beside it. The expectation recorded before the freeze: route A strongly disfavoured, route B unsettled.

**Result (2026-09-13):** Uninformative. Both runs stopped at G1b, CAMB 2.0.4's reproduction of Planck's baseline spectrum (2.22 × 10⁻³, then 2.16 × 10⁻³ after erratum E1, against 2 × 10⁻³), before any P1 quantity was computed, so the prescription was never scored against the data. A diagnosis after the verdict finds CAMB's low-ℓ output moving at the 10⁻³ level with the late reionization history and with kη_max, the order of the gate's tolerance.

---

## :bar_chart: Waiting on External Data

- **Neutrino Ladder:** The $`R_1`$ sector's entries, 0.87, 7.3 and 66.7 meV, sit in ordered qualitative resemblance to the lightest, solar (8.65 meV) and atmospheric (50.1 meV) scales; the solar and atmospheric values are splitting proxies rather than masses, so the rows carry no scorecard weight and no generation assignment is claimed ([mass spectrum](../../../spectrum/files/mass-spectrum.md#the-neutrino-ladder)). As absolute masses the ladder is excluded by the measured splittings; the proxy reading assumes a hierarchical normal ordering and is falsified if the NuFIT global fit or a successor favors the inverted ordering with $`\chi^2_\text{NO} - \chi^2_\text{IO} \geq 9`$. *Deps:* mass formula, the $`R_1`$ sector.
- **Black Hole Node Distribution on Static $`S^3`$:** If $`S^3`$ is static and black holes are topological nodes (the conjectured double zero, $`\Theta \to 0`$ with $`\Omega_\Psi \to 0`$; on the static channel the edge readout has a single zero of reduced order, and the general limit is underdetermined: [the Ω_Ψ derivation](files/omega-h-derivation.md)), their spatial distribution should reflect the symmetry of the 120-cell rather than FLRW comoving evolution; quasar catalogs (Milliquas, SDSS) provide ~900,000 angular positions and redshifts, and the missing piece is the $`z`$-to-$`S^3`$-position map (converting redshift to location on the static 3-sphere without assuming spatial expansion), after which supermassive black hole positions can be tested against 120-cell structure. *Deps:* the missing $`z`$-to-$`S^3`$-position map above, and the $`z`$-to-phase map from the temporal budget.
- **Dead Zone:** 19 of the 24 mass formula entries carry no adjudicated Standard Model assignment: 3 neutrino-scale proxy rows and 16 with no SM relation ([mass spectrum](../../../spectrum/files/mass-spectrum.md#v-dead-zone-targets-and-exclusions)). Among the 16 are 6 in the dead zone ($`10^{-9}`$ to $`10^{-6}`$ GeV), 1 entry the source labels a target but reads as a structural residual by default (rank 16, ~418 MeV), and 1 unassigned up-type address (rank 14, ~31.6 MeV, the up quark's vacated slot); the dead zone is probed by sterile neutrino and warm dark matter searches. *Deps:* mass formula, full assignment table.
- **Physical Observation Scale:** $`\sqrt{\ell_P \cdot R_\Lambda} \sim 50\,\mu\text{m}`$ places the observer at the cellular scale; the geometric midpoint is derived, but the dimensionless derivation connecting this to biological observation is pending. *Deps:* observer position at $`\sqrt{\Omega}`$, scale hierarchy.
- **Next Cycle Initiation:** What happens at $`t = 4\pi`$ is outside the current framework; the standing wave completes its period, and whether the cycle repeats, terminates, or transforms is not addressed. *Deps:* none within the current framework.

---

/ **[`↑top`](#top)** / **[`main`](https://github.com/dmobius3/mode-identity-theory/tree/main/)** / **[`framework`](/files/framework/)** / **[`bedrock`](/files/framework/files/bedrock/)** / **[`cosmos`](/files/cosmos/)** / **[`spectrum`](/files/spectrum/)** / **[`tools`](/files/tools/)** /
