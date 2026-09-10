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

A gate is a *result, not a date*: a hard mathematical or physical prerequisite, shared across at least two distinct research programs, that must resolve before downstream work can advance. A page names a gate it is waiting on with `**Gated by:**`; a page trying to resolve one is listed here under **Worked by**. A page may work a gate or be gated by it, never both for the same gate. All eight are currently **Open**; closing one is a propagation event that stales every page that named it.

| Gate | Frontier | State | Worked by | What must resolve |
|------|----------|-------|-----------|-------------------|
| `gate:commutant` | Selection | Open | [`scaling-law-uniqueness.md`](files/scaling-law-uniqueness.md) | The no-cross-term observable commutant $`\mathcal{A}_\text{obs} = \mathcal{A}_\Theta \otimes \mathcal{A}_\text{spec}`$ the scaling law's factored form requires. |
| `gate:selection-rule` | Selection | Open | [`fibonacci-wells.md`](files/fibonacci-wells.md), [`scaling-law-uniqueness.md`](files/scaling-law-uniqueness.md) | Why the realized wells, grids, and exponents are selected from the topology rather than adopted as a postulate. |
| `gate:amplitude-stress-tensor-dictionary` | Dynamics | Open | [`stress-tensor-bridge.md`](files/stress-tensor-bridge.md) | The amplitude-to-$`T_{\mu\nu}`$ / $`E(S)`$ dictionary that would make the $`\Psi^2 \to S^2`$ transfer a stress-energy counterparty; downstream of the physical-$`\Lambda`$ interface. |
| `gate:clock-exponent-derivation` | Dynamics | Open | [`friedmann-as-output.md`](files/friedmann-as-output.md), [`variational-score-to-sample.md`](files/variational-score-to-sample.md) | Derive the Waltz clock exponent $`dt/d\tau = S^{-1/2}`$ from the postulate layer, without importing it from GR. |
| `gate:shell-unlock-map` | Dynamics | Open | [`entropy-as-realization-budget.md`](files/entropy-as-realization-budget.md) | The $`S \mapsto N_\text{max}(S)`$ Molien shell-unlock map that sets the accessible mode count $`W_\text{modes}(S)`$. |
| `gate:three-halves-identity` | Dynamics | Open | *(none)* | Whether the clock $`3/2`$ and the Gauss-Codazzi $`3/2`$, numerically equal, are the same object. |
| `gate:variational-independence-bar` | Dynamics | Open | [`variational-score-to-sample.md`](files/variational-score-to-sample.md) | Whether a global score-to-sample functional can be motivated independently of the target exponent, then varied to yield it. |
| `gate:galactic-curvature-sourcing` | galactic | Open | [`cone-point-coherence.md`](files/cone-point-coherence.md), [`oort-cloud-project.md`](files/oort-cloud-project.md) | What sources the curvature $`K_g`$ at galactic scale; GR tidal curvature in the flat-curve regime is structurally non-oscillatory. |

Two facts this registry makes visible. `gate:three-halves-identity` has dependents but no worker: two Dynamics programs are blocked by it and no page is currently resolving it. And the Frontier's Calibration-closure problem has no registered gate: the R-determination question that would be one was demoted as a single program's open question, so Calibration closure is tracked by [The R Problem](files/r-problem.md) directly rather than through a gate.

---

## :world_map: Maps

Orienting notes that index other work.

---

### [Claim Ledger](files/claim-ledger.md)

**Audit lens (2026-06-26):** A skeptical, framework-wide classification of every quantitative claim by epistemic type (forward prediction, zero-freedom structural result, internal theorem, loose comparison, calibration anchor, null result, open problem) and role. Separates the thin forward sector the framework lives or dies on (mostly Euclid DR1) from the retrodictions inside the calibration web, draws the web's eight cycles explicitly, and flags overclaims, double-counts, and the two real internal tensions: Cycle 2 ($`\alpha`$ is both input and output, so the 0.4% match is a consistency check) and Cycle 7 (the coupling-route and mass-route values of $`R`$ disagree ~3.2×). Built to keep the public pages honest, not as the framework's self-description; ends with a source-page triage queue.

**Inputs:** the whole framework's quantitative claims; see especially [The R Problem](files/r-problem.md) and [Calibration Structure](files/calibration-structure.md).

---

### [The R Problem](files/r-problem.md)

**Tracker:** Maps every route to an independent spatial curvature radius $`R`$ and where each stands. $`\Lambda_\text{ref} = 3/R^2`$ becomes a conditional output only with an $`R`$ not read off $`\Lambda`$, and identifying that reference value with the physical $`\Lambda`$ stays gated by the Interface: de Sitter is circular, the Molien gap is not independent, the CMB L-ratio factor of 8 is dead (no topological derivation), and the particle mass spectrum is the one live route (executed, order of magnitude). Includes the shared E₈ / $`h = 30`$ engine tying the L ratio to the mass formula, and flags the Molien sparse-zone CMB result as the independent survivor of the L work.

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

**Tracker:** The two bedrock results sit on the two pieces of the postulate $`S^1 = \partial(\text{Möbius}) \hookrightarrow S^3`$, and whether a theorem connects them is open. The naive bridge through the shared $`2/R^2`$ is dead: the surface eigenvalue is $`\Gamma`$-blind and the Ricci floor is the only $`\Gamma`$-independent slot in the gap, so the match is a forced curvature-scale coincidence, not a spectral link, and $`2I`$'s perfectness ($`H^1 = 0`$) closes the orientation route as well. The one live route is index theory on the $`E_8`$ plumbing that $`S^3/2I`$ bounds, where the McKay correspondence identifies the intersection-form $`E_8`$ with the gauge $`E_8`$; the gatekeeper is whether the boundary spectral asymmetry distinguishes the Galois connection $`Q'`$ from $`Q`$ by the same distance-six anomaly that gives the $`36/R^2`$ gap. Steps 1 to 3 are done (the gate is open; the framework and sign are fixed; the interior classes are computed and Galois-blind: [η-gatekeeper](files/eta-gatekeeper.md), [Step 2](files/step2-analytic-setup.md), [Step 3](files/step3-interior-classes.md)); the staged route is now complete, as a split: the gauge dictionary is proved (the $`E_8`$ filling carries the boundary's Galois asymmetry exactly) and the Möbius channel decouples route-specifically ([part one](files/step4-bookkeeping.md), [part two](files/step4-coupling.md)); no universal independence claim is made, and the result is now published as the standalone bedrock pillar [Galois pair](../bedrock/files/galois-pair.md).

A sampler reading of that split is recorded open: the quotient carries the native spectrum while the Möbius geometry supplies a phase-sensitive readout, under which the recorded negatives are what the architecture predicts. Its new object is the observation map $`f = \pi \circ i : M \to S^3/2I`$, which needs no descent of the band as a submanifold, and the sampling operator $`\mathcal O_M`$ it would carry. Its first test, whether an intensity observable factors through $`2I/\{\pm 1\} \cong I`$, is [run and closed negative twice over](files/sampler-first-test.md): no compact surface in $`S^3`$ with a single boundary circle is antipodally invariant, so the deck element $`-1`$ never stabilizes the band; and independently, equivariance makes the transverse sampler's intensity profile identical on all $`120`$ deck translates, so no invariant scalar readout distinguishes lifts at any stabilizer size. The engine's projection is untouched, resting on $`\lvert\psi\rvert^2`$ alone. The residue is structural: the natural Möbius sampler is transverse rather than restrictive, and its open question is mode transfer rather than label identification.

A variational reading now sits over both, as program architecture rather than a fourth tier: the dynamics problem is a variational principle for the global score-to-sample relation, not a search for a conventional $`L(q,\dot q,t)`$. The corpus phase $`t`$ stays fundamental and observer time is reconstructed through a lapse $`d\tau_H = N(t)\,dt`$, with the two-level descent $`\mathcal{S}_\text{MIT} \to \mathcal{S}_\text{eff}`$ carrying the sampled degrees of freedom. Its promotion gate is the observer clock: whether $`\delta\mathcal{S}_\text{MIT}/\delta N = 0`$ forces $`N = S^{1/2}`$ without the exponent being inserted by hand, with $`\Psi^2 + S^2 = 1`$ entering only as an on-shell constraint. The gate, the fixed conventions, the one bounded computation and its pre-registered PASS and FAIL conditions are on the program page, [Variational Score-to-Sample](files/variational-score-to-sample.md). Nothing is derived there: no candidate functional is fixed, and no lapse equation is solved.

**Gated by:** `gate:variational-independence-bar`

**Inputs:** [First eigenvalue](../bedrock/files/first-eigenvalue.md), [Coexact gap](../bedrock/files/coexact-gap.md).

---

## :house: Physics Foundation

Closing any one of these upgrades everything downstream.

---

### [Variational Score-to-Sample](files/variational-score-to-sample.md)

**Tracker (motivated, nothing derived):** The program page for the variational reading, and the one entry here that both foundations wait on: it is the sole worker on `gate:variational-independence-bar`, which [The Postulate Bridge](files/postulate-bridge.md) and [The Stress-Tensor Bridge](files/stress-tensor-bridge.md) each declare as a prerequisite, and the bridge already names the variational route preferred for its construction step. It frames the dynamics problem as a variational principle for the global score-to-sample relation rather than a search for a conventional $`L(q,\dot q,t)`$: the corpus phase $`t`$ stays fundamental, observer time is reconstructed through a lapse $`d\tau_H = N(t)\,dt`$, and a two-level descent $`\mathcal{S}_\text{MIT} \to \mathcal{S}_\text{eff}`$ carries the sampled degrees of freedom. The page fixes the corpus conventions any candidate must respect, states that architecture, names one bounded computation (vary $`N`$, $`S`$, and the constraint multiplier, then read off the lapse law), and pre-registers PASS and FAIL before the run, including the dressed-lapse case scored in advance so that "another clock" is not adjudicated afterwards. The clock exponent is not this page's to score: the program enters [Friedmann as Output](files/friedmann-as-output.md)'s route menu as R-VAR and promotes only on that page's terms. Nothing is derived: no candidate functional is fixed, and no lapse equation is solved.

**Inputs:** [The Postulate Bridge](files/postulate-bridge.md), [Temporal Budget](files/temporal-budget.md), [Friedmann as Output](files/friedmann-as-output.md), [The Stress-Tensor Bridge](files/stress-tensor-bridge.md), the engine (chronon, sign flip, Hubble clock).

---

### [The Stress-Tensor Bridge](files/stress-tensor-bridge.md)

**Tracker:** Program page for the framework's one missing map, the ledger's $`E(S)`$: from the realized budget state to a stress tensor with a declared placement (which metric's Einstein equations it sources). The same object gates four opens at once: the Λ coefficient's physical identification ([cosmological constant](../../../cosmos/files/cosmological-constant.md) §IV), the Ψ²→S² counterparty, the cooling-energy accounting, and the matter-scaling import in $`H(z)`$. The page assembles the constraint set (static source, the perfect-fluid coefficient gate, the Friedmann mechanism fence, the Killing ledger, the fitted dictionary, the coincidence fences), states the three-way placement fork (physical-static, effective-metric, shifted coefficient), and carries the first cycle's results: the minimal scalar reading dead on its registered expectations; the fitted dictionary's tie promoted to a structural identity; two newly named metric-definition questions (curvature placement, Λ-dressing of the effective clock); the full flat D+Λ source and lapse pinned under the fixed $`a_\text{eff} = a_\ast S`$ placement; and the variational route ([postulate-bridge](files/postulate-bridge.md) dynamical tiers) promoted to preferred for the construction step. Nothing is derived: no $`X \to g_\text{eff}`$, no $`X \to T_\text{eff}`$, no action.

**Gated by:** `gate:variational-independence-bar`

**Inputs:** [cosmological constant](../../../cosmos/files/cosmological-constant.md) §IV, [The Budget Map](files/budget-map.md), [Friedmann as Output](files/friedmann-as-output.md), [Temporal Budget](files/temporal-budget.md), [Redshift and Cooling](files/redshift-and-cooling.md), [postulate-bridge](files/postulate-bridge.md).

---

### [Scaling Law Uniqueness](files/scaling-law-uniqueness.md)

**Status (two rows forced, factorization argued):** $`A/A_P = C(\Theta) \cdot (\sqrt{\Omega})^{-n}`$ began as a declared measurement postulate. Two rows are forced: the anti-periodic BC forces $`C(\Theta)`$'s sinusoidal family and background symmetry (isotropy + orthogonality) selects the first-positive member; units force the integer hierarchy $`(\sqrt{\Omega})^{-n}`$ on the dilution sector. The factored form *separates* on a Schur + homothety + Lemma 8 argument within the spectral-boundary observable class, but is not yet closed: independent coordinates do not forbid a cross-term, so the no-cross-term step needs the commutant theorem $`A_\text{obs} = A_\Theta \otimes A_\text{spec}`$ (the open target). Whether the class exhausts the physical observables is a further premise. Off the form: the $`\alpha_W`$ twist, the extension *selection* (ground state only), and the $`\Omega_H = \Omega_\Lambda`$ coincidence.

**Inputs:** Sector $`\mathcal{A}`$ eigenvalue, Lemma 8 (spectral inaccessibility), Möbius topology axioms.

---

### [Friedmann as Output](files/friedmann-as-output.md)

**Tracker (the half-power clock, ε-scored):** The phase-clock $`H(z)`$ imports the Friedmann equation through exactly one line, the Waltz clock exponent $`-1/2`$, forced by $`S^3`$ dimensionality plus GR and empirically unique in its family ($`\Delta\chi^2 > 60`$ against integer alternatives). The tracker reduces the derivation to that exponent and enumerates the topologically native clock candidates; one, the self-dual clock under level exchange, lands $`-1/2`$ arithmetically through a three-gate argument ([the involution](files/half-power-involution.md), [the tick lemma](files/tick-lemma.md), a second consequence on the [entropy page](files/entropy-as-realization-budget.md)). The [registered measurement](files/clock-asymmetry-fit.md) meant to complete the case, the continuous $`\epsilon`$ fit, has run: zero excluded at 95% in both tiers, but diagnostics found the dial contaminated as a probe on this data, so the result neither confirms nor cleanly refutes. Adjudicated: P2 [supported by reduction](files/sampling-kernel-symmetry.md), empirically unscored; the FORCED label stays FORCED.

**Gated by:** `gate:shell-unlock-map`, `gate:three-halves-identity`

**Inputs:** [Temporal budget identity](files/temporal-budget.md), Waltz clock, spatial budget $`u_0^2 + J^2 = 1`$, Gauss-Codazzi embedding (assembly stage only).

---

### [Temporal Budget Identity](files/temporal-budget.md)

**Problem:** The phase-clock derivation rests on $`\Psi^2 + S^2 = 1`$ and the Waltz clock $`d\tau/dt = S^{1/2}`$, which, with $`\Omega_\Lambda = 0.685`$ held fixed, inherits $`\Omega_m = 0.315`$ by flat closure and fits at $`\Delta\chi^2 = +0.11`$ vs flat ΛCDM. The clock exponent $`n = -1/2`$ is empirically supported only against its discrete family (integer alternatives ruled out at $`\Delta\chi^2 > 60`$); the registered continuous diagnostic returned unscored, its dial diagnosed contaminated, and the exponent is not derived from the embedding. The two phase parameterizations ($`\Phi`$ engine phase and $`t`$ budget phase) are not yet reconciled.

**Gated by:** `gate:clock-exponent-derivation`, `gate:amplitude-stress-tensor-dictionary`, `gate:three-halves-identity`

**Inputs:** Möbius spatial budget $`u_0^2 + J^2 = 1`$, Sector $`\mathcal{A}`$ eigenvalue.

---

### [Fibonacci Wells](files/fibonacci-wells.md)

**Status (structurally reduced):** Why the stable sampling positions land at the Fibonacci wells $`\{13, 21, 34, 55\}`$. The external golden-ratio/Hurwitz route is abandoned (a rounded golden rotation selects a parity class, not the wells). The wells are reframed as the additive continuation of the icosahedral branch orders $`(2,3,5)`$ on the locked 120-grid, bounded below by the lcm seam ($`13`$ is the first Fibonacci not dividing $`120 = \text{lcm}(1,2,3,5,8)`$; divisors tile, non-divisors sample) and above by the antinode reflection $`C(k)=C(120-k)`$. The residual: define the boundary-native anti-periodic interference functional whose minima are the recurrence positions; the mirror's Lemma 8 rules out any bulk functional (the spectral side is $`\Theta`$-blind), and $`\varphi`$ enters internally through the $`\mathbb{Q}(\sqrt5)`$ character field, not Hurwitz.

**Gated by:** `gate:commutant`

**Inputs:** Scaling law uniqueness (phase operator $`C(\Theta)`$), the-mirror.md (Lemma 8, $`\mathbb{Q}(\sqrt5)`$, character ceiling), 120-domain selection.

---

### [Cone Point Coherence](files/cone-point-coherence.md)

**Problem:** Galactic coherence (all observers measuring the same $`\mathbb{R}^4`$) may be the $`W`$-independence of a nested eigenvalue problem, guaranteed by a cone point at galactic scale. The cone point analysis (Frobenius, Friedrichs, excision) that makes the cosmic eigenvalue well-defined must be re-established at galactic scale with equal rigor. Critical fork: GR tidal curvature in the flat-curve regime is Euler-type with power-law Jacobi solutions that structurally cannot zero, so the curvature has to come from the topology-gravity interface. SPARC has since falsified $`L_f = v_c^2/a_0`$ as the galactic coherence radius, which removes the empirical anchor for that reading and leaves the sourcing question open against an unknown $`L_g`$; Reading A and the Frobenius chain are untouched.

**Inputs:** Sector $`\mathcal{A}`$ eigenvalue, phase field coherence scale $`L_f`$ (SPARC-falsified; the unknown galactic scale is $`L_g`$), 120-grid scale-free projection.

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

**Problem:** [Black Double Zero's](../../../cosmos/files/black-hole.md) claims a "double zero" at the horizon, $`\Theta\to0`$ (derived) alongside $`\Omega_\Psi\to0`$ (conjectured). Even granting both, $`\Omega_\Psi`$ enters the scaling law inversely ($`\Omega_\Psi^{-n/2}`$), so the compound limit is $`0\times\infty`$, undetermined without the relation $`\Omega_\Psi(\Theta)`$. Frozen here, before any attempt, as: derive $`\Omega_\Psi(\Theta)`$ for a specified observer congruence (static, infalling, invariant norm, or a preferred MIT clock, these give physically different answers) and find the exponent $`p`$ in $`\Omega_\Psi\sim\Theta^p`$; the gate is $`C\cdot\Omega_\Psi^{-n/2}\sim\Theta^{2-pn/2}`$, vanishing/finite/divergent depending on $`p`$ versus $`4/n`$. A null result is a complete answer and requires no further correction to the now-hedged main page.

**Inputs:** [Black Double Zero's](../../../cosmos/files/black-hole.md) §II, §VIII.1.

---

### [Oort Cloud Project: Nested Coherence Domains](files/oort-cloud-project.md)

**Problem:** Does MIT's structure project into every gravitationally coherent scale, or only the cosmological one? If the 120-grid and 3/2 conversion nest, the Oort Cloud (~144,000 AU) is the solar-system-scale coherence boundary. Central open question: what sets the coherence scale at each level. $`L_f = v_c^2/a_0`$ was the candidate, and SPARC falsified it as the galactic radius, so the generalization now runs from an unknown $`L_g`$ rather than from $`L_f`$. Downstream predictions include CMB-ecliptic alignment as a local sampling fingerprint.

**Inputs:** Sector $`\mathcal{A}`$ eigenvalue, phase field coherence scale $`L_f`$ (tested, falsified by SPARC; the unknown galactic coherence scale is $`L_g`$), 120-grid scale-free projection, 3/2 conversion (Gauss lift + de Sitter vacuum).

---

**Coupling and scaling exponents.** Each is a distinct single-principle-derivation gap on a gauge or scaling exponent; the load-bearing number stays in place.

- **dist/30 Hierarchy Exponent:** Three convergent paths connect McKay graph distance to the Coxeter number of $`E_8`$ as the scaling exponent; single-principle derivation open. *Deps:* McKay correspondence, $`E_8`$ Coxeter number.
- **Scale Consistency:** Three gauge couplings evaluated at different energy scales; $`\alpha`$ hits 0.4% at low energy but 6.2% at $`M_Z`$, so the framework must commit to one evaluation scale or derive running from MIT structure. *Deps:* gauge coupling derivation (engine §15), scaling law.
- **$`\alpha`$ Exponent:** The $`\alpha`$ exponent equals the minimum grid step; two convergent paths remain and the uniqueness scan confirms, but single-principle derivation is open. *Deps:* grid structure, scaling law.
- **Plato Twist Derivation:** the value $`\cos(\pi/10)`$ has a computed geometric realization, the spin lift of the Levi-Civita holonomy around the shortest closed geodesic of $`S^3/2I`$, where the flat $`2I`$ holonomy gives $`\cos(\pi/5)`$ instead; the open link is its insertion into the weak coupling: which loop, which power, and why the weak row alone. See [The Plato Twist](files/plato-twist.md). *Deps:* spin structure of $`S^3/2I`$, stabilizer decomposition.

---

**Selection rules.** Why one structure is picked over its alternative, not yet derived.

- **Grid Ladder Selection Rule:** Three convergent paths connect interaction character to grid resolution ($`D = 60`$ vs $`D = 120`$); formal derivation open. *Deps:* stabilizer decomposition, boson/fermion domain split.
- **Anti-periodic BC Selection:** 4 of 8 charged fermion masses within ×3 after sector-first adjudication, 5 with a compatible entry (descriptive; the ×3 count is density, per the [torsion null test](files/mass-null-test.md)); first-principles derivation of why anti-periodic boundary conditions are selected over periodic remains open. *Deps:* Möbius non-orientability, mass formula.

---

**Neutrino sector.**

- **Neutrino Mass Ratios:** $`\mu_\Lambda`$ as the neutrino floor is motivated; the octave selection and multipliers (4, 22) are identified but not derived from the group theory. *Deps:* mass formula, $`\Lambda`$ eigenvalue.

---

**Superseded and secondary routes.**

- **240 Alternative for $`\alpha_s`$:** $`C(17/120) \times \Omega^{-1/240}`$ sits 1% behind the primary formula, with $`240 = 2 \times 120`$; requires independent justification or exclusion. *Deps:* grid ladder selection rule, scaling law.
- **$`L_\text{strip}/L_\text{fund}`$ Ratio:** The factor of 8 has no topological derivation, so this is a dead route to $`R`$, superseded by the mass spectrum (see [The R Problem](files/r-problem.md)); the only open remnant is the residual ~3% spectral-vs-observational gap (8.17 ± 0.1 vs 7.93).

---

## :white_check_mark: Results

Closed: executed computations and derivations with verdicts in hand.

---

### [R from the Particle Mass Spectrum](files/r-from-mass-spectrum.md)

**Result (2026-06-15):** Determines the spatial curvature radius $`R`$ from the fermion mass formula's dependence on the hierarchy factor $`\Omega_\Lambda`$, independently of $`\Lambda`$, the CMB, and the de Sitter relation, breaking the R-problem circularity. Electron + muon give $`R \sim 20`$ Gpc and $`\Lambda \sim 8.1 \times 10^{-54}\,\text{m}^{-2}`$, about 13.4× (one order of magnitude) below the observed value. Precision is capped at order of magnitude by the McKay-lever amplification (60× for $`\delta d = 1`$) acting on the mass formula's irreducible few-percent residual scatter; a pair scan shows no fermion pair beats electron-muon. The third and only non-excluded route to $`R`$.

**Inputs:** Fermion mass formula and torsion table, McKay residual scatter (sets the precision floor), $`\Omega_\Lambda`$ hierarchy, $`\Lambda_\text{ref} = 3/R^2`$ reference relation.

---

### [McKay Propagator Correction](files/mckay-propagator-correction.md)

**Reopened by the torsion correction (2026-07-28):** The 2026-06 verdict (no parameter-free propagator or branch-point correction tracks the high-distance mass residuals; the route was closed, the residuals read as irreducible scatter) was computed on the pre-correction torsion table. The [half-integer torsion correction](files/torsion-correction.md) revised twelve of the twenty-four products and the whole mass comparison, so the propagator question is reopened; the frozen 2026-06 record, with its overshoot figures and vacuum-dependent hits, is preserved on the [linked page](files/mckay-propagator-correction.md) under its 2026-07-28 banner. Separately, the Coxeter-Galois gate still locks all $`R_4`$ entries to $`T_3 = -1/2`$, and charm remains unplaced.

**Inputs:** McKay graph for $`2I`$, $`C_\text{geom}`$ values for all irreps, torsion table $`T^2(\rho \otimes \sigma)`$ across vacua, Coxeter-Galois gate.

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

**Result (2026-05-19):** The discrete two-cluster prediction is not supported. The dip test fails to reject unimodality in every configuration (primary p = 0.217); the Gaussian mixture's 2-component preference is statistically negligible (ΔBIC < 1.2) and points to clusters at 68.4 / 73.2 rather than 67 / 73; the predicted 69-71 gap contains TRGB / CCHP at 69.8. The data sorts by calibration class but does not quantize.

**Respecification (2026-09-02):** The original test compared against two clusters, but the [hubble-tension](../../../cosmos/files/hubble-tension.md) lattice has three values (67.40, 70.24, 73.04) and the middle one falls inside the 69-71 gap this test treated as empty. Re-running with the three centres fixed removes that specification defect and still returns no lattice-specific evidence: the fixed-centre model is the nominal BIC minimum in all eight cells, but its middle component carries weight exactly zero in every one, including on the current TRGB value sitting 0.15 from that centre.

---

### [Torsion Null Test (Mass Scorecard)](files/mass-null-test.md)

**Test:** Does the fermion mass scorecard's within-×3 hit rate carry information about the specific torsion values, or is it density? Pre-registered design frozen at tag `mass-null-v1.0`, one registered run (Generator PCG64, seed 120, $`M = 100{,}000`$). Statistic: the compatible-coverage count $`S_1`$ under four nulls (permute the 24 torsions across slots, within-vacuum, log-uniform redraw, within-spin-class exact), verdict fixed on Null A.

**Result (2026-07-28):** The ×3 count is uninformative about the torsion values. Randomly reassigning the 24 torsion factors across the fixed quantum-number slots reproduces or exceeds the observed coverage in 69.0% of draws (Null A, $`p_A = 0.690`$; the null $`S_1`$ mean of 5.02 sits at the observed coverage of 5, and the B / C / D secondaries stay far above the 0.01 information band). The mass table's evidential weight rests on the structural outputs (the 24-entry count, the $`T_3`$ gate evaluations, the $`\varphi^{-4}`$ ratio) and the falsifiable outliers, not on the ×3 proximity count; the test does not validate those structural outputs, it removes the proximity scorecard as torsion evidence. This is the re-run on the corrected torsion table (tag `mass-null-v1.1`); the pre-correction run (`mass-null-v1.0`, $`p_A = 0.174`$) is retained as history. Design frozen before each run (tag on the frozen bundle), results committed separately.

---

## :bar_chart: Waiting on External Data

- **$`\nu_2`$ Mass:** Predicted at 8.6 meV with the corrected $`R_1`$ ladder placing the nearest entry at 7.3 meV, ratio 0.85; JUNO and DUNE are expected to resolve the neutrino mass hierarchy and test this value directly. *Deps:* mass formula, neutrino sector assignments.
- **Black Hole Node Distribution on Static $`S^3`$:** If $`S^3`$ is static and black holes are topological nodes (double zeros where $`\Theta \to 0`$ and $`\Omega_\Psi \to 0`$), their spatial distribution should reflect the symmetry of the 120-cell rather than FLRW comoving evolution; quasar catalogs (Milliquas, SDSS) provide ~900,000 angular positions and redshifts, and the missing piece is the $`z`$-to-$`S^3`$-position map (converting redshift to location on the static 3-sphere without assuming spatial expansion), after which supermassive black hole positions can be tested against 120-cell structure. *Deps:* Friedmann as Output (provides the static $`S^3`$ coordinate system), $`z`$-to-phase map from temporal budget.
- **Dead Zone:** 8 of 24 mass formula entries are unassigned: 6 in the dead zone ($`10^{-9}`$ to $`10^{-6}`$ GeV), 1 entry the source labels a target but reads as a structural residual by default (rank 16, ~418 MeV), 1 unassigned up-type address (rank 14, ~31.6 MeV, the up quark's vacated slot); the dead zone is probed by sterile neutrino and warm dark matter searches. *Deps:* mass formula, full assignment table.
- **Physical Observation Scale:** $`\sqrt{\ell_P \cdot R_\Lambda} \sim 50\,\mu\text{m}`$ places the observer at the cellular scale; the geometric midpoint is derived, but the dimensionless derivation connecting this to biological observation is pending. *Deps:* observer position at $`\sqrt{\Omega}`$, scale hierarchy.
- **Next Cycle Initiation:** What happens at $`t = 4\pi`$ is outside the current framework; the standing wave completes its period, and whether the cycle repeats, terminates, or transforms is not addressed. *Deps:* none within the current framework.

---

/ **[`↑top`](#top)** / **[`main`](https://github.com/dmobius3/mode-identity-theory/tree/main/)** / **[`framework`](/files/framework/)** / **[`bedrock`](/files/framework/files/bedrock/)** / **[`cosmos`](/files/cosmos/)** / **[`spectrum`](/files/spectrum/)** / **[`tools`](/files/tools/)** /
