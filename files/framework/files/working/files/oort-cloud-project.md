<a id="top"></a>
/ **[`main`](https://github.com/dmobius3/mode-identity-theory/tree/main/)** / **[`framework`](/files/framework/)** / **[`bedrock`](/files/framework/files/bedrock/)** / **[`working`](/files/framework/files/working/)** / **[`cosmos`](/files/cosmos/)** / **[`spectrum`](/files/spectrum/)** / **[`tools`](/files/tools/)** /

---

# Oort Cloud Project: Nested Coherence Domains and the Realization Boundary

**Type:** Program
**State:** Active
**Status (2026-09-16):** Working bench: Section II derived, Section III joints under load, Section IV pieces motivated, Section V gaps. The central question is whether the 120-grid nests at every gravitationally coherent scale.
**Summary:** Asks whether MIT's structure projects into every gravitationally coherent scale, making the Oort Cloud the solar-scale coherence boundary.
**Inputs:** the first positive eigenvalue (first-eigenvalue paper), the phase-field coherence scale (L_f SPARC-falsified, L_g open), the 120-grid scale-free projection, the 3/2 conversion

> The grid doesn't set a size; it sets a structure.

Working bench. Locked parts (Section II) are derived. Joints (Section III) are under load. Pieces (Section IV) are motivated but not yet joined. Gaps (Section V) are genuinely open.

**Related:** [Cone point coherence notes](cone-point-coherence.md) (geometric mechanism behind $`L_f`$), [SPARC phase field notes](sparc-phase-field.md) (empirical test of $`L_f`$ across 175 galaxies), [Black Double Zero's](../../../../cosmos/files/black-hole.md) §VIII.1 (the killed absolute-$`\Phi`$ bridge to the horizon, Joint 4).

---

## I. The Question

Does MIT's structure project into every gravitationally coherent scale, or only the cosmological one?

If it projects, the Oort Cloud (~144,000 AU) is the solar-system-scale coherence boundary: the domain within which the observer's 3/2 reconstruction (Gauss lift + de Sitter vacuum) is anchored to the solar mode. If it doesn't, the Oort Cloud is just where gravity hands off, and the 144,000 is a coincidence.

Everything on this bench serves that question.

---

## II. Parts (Locked)

Derived, tested, load-bearing. Pick up and use.

| Part | What it is | Derived from | Reference |
|------|-----------|--------------|-----------|
| $`\Psi(t) = \cos(t/2)`$ | Cosmic wave, period $`4\pi`$ | Anti-periodic BC on $`S^1`$ | MIT II.B |
| $`C(\Theta) = 2\sin^2(\pi\Theta)`$ | Phase operator | Anti-periodic BC, unit normalization | MIT II.D |
| 120-grid | Phase resolution native to $`S^3`$ | Binary icosahedral group ($`\|2I\| = 120`$) | MIT II.D |
| $`\sqrt{\Omega} = 10^{61}`$ | Observer midpoint | UV-IR fixed point on bounded domain | MIT II.C |
| $`(\sqrt{\Omega})^{-n}`$ | Hierarchy factor | Volume dilution in $`n`$-manifold | MIT II.C |
| 3/2 conversion | Perception geometry: surface-to-venue | Gauss/Ricci lift (the 3), de Sitter vacuum normalization (the 1/2), minimal embedding, isotropy | [The Waltz](../../../../spectrum/files/the-waltz.md) |
| $`\Lambda_\text{ref} = 3/R_\Lambda^2`$ | Vacuum-reference value, not a prediction | Scaling law gives the seed $`\Lambda_\text{top} = 2/R_\Lambda^2`$; the 3/2 lift gives the reference. On the $`\Lambda`$-anchored default it reproduces the measured $`2.845 \times 10^{-122}`$ by construction, since $`R_\Lambda`$ is back-read from $`\Lambda`$; the non-circular $`\alpha`$ route lands ~23% low | [The Waltz](../../../../spectrum/files/the-waltz.md) |
| $`\tau = T/120`$ | Chronon at any scale | 120-grid applied to mode period $`T`$ | Chronon note |
| $`\tau_c/\tau_P = \sqrt{\Omega}`$ | Chronon ratio spans $`10^{61}`$ | Same midpoint, temporal channel | Chronon note |
| $`L_f = v_c^2/a_0`$ | Coherence scale (galactic, ~13 kpc). SPARC-falsified as single coherence radius; retained as the tested candidate | Phase field mechanics | MIT II.G |
| $`\Delta\Theta_{\min} = 2/120`$ | Minimum bosonic step | 60R resolution, $`\lvert I\rvert = 60`$ | MIT II.D |
| $`\Theta_f^{\text{env}} \approx 2/120`$ (MW) | Environmental phase shift | Minimum step at Milky Way potential | MIT II.G |

---

## III. Joints (Connections Under Load)

### Joint 1: The 3/2 is the geometry of perception

The topology produces $`\Lambda_{\text{top}}`$ on a 2D surface. The observer infers $`\Lambda_{\text{obs}}`$ in 3D. The Gauss equation for minimal embedding in an isotropic venue:

```math
R_\Sigma = R_{\text{spatial}} - 2\,\text{Ric}(n,n) = R_{\text{spatial}} - \frac{2}{3}R_{\text{spatial}} = \frac{1}{3}R_{\text{spatial}}
```

Invert: $`R_{\text{spatial}} = 3\,R_\Sigma`$. With de Sitter relation $`R_{\text{spatial}} = 2\Lambda_{\text{obs}}`$:

```math
2\Lambda_{\text{obs}} = 3\Lambda_{\text{top}} \quad \Rightarrow \quad \Lambda_{\text{obs}} = \frac{3}{2}\Lambda_{\text{top}}
```

| Factor | Source |
|--------|--------|
| 3 | Ricci trace (isotropy distributes curvature equally across 3 spatial directions; normal gets 1/3) |
| 2 | Friedmann dynamics ($`R_{\text{spatial}} = 2\Lambda`$ in de Sitter) |
| 3/2 | Perception geometry: how observers see the 3D venue through a 2D reception surface |

Status: DERIVED. Solid.

### Joint 2: The 120-grid is scale-free

The grid is group-theoretic, not dimensional. It doesn't know meters or seconds. Applied to any mode with period $`T`$:

| Scale | $`T`$ | $`\tau = T/120`$ |
|-------|-----|-----------------|
| Planck | $`t_P \approx 5.4 \times 10^{-44}`$ s | $`\tau_P \approx 4.5 \times 10^{-46}`$ s |
| Cosmic | 33 Gyr $`\approx 10^{18}`$ s | $`\tau_c \approx 275`$ Myr |

Ratio: $`\tau_c/\tau_P \approx 10^{61} = \sqrt{\Omega}`$. The observer's structural midpoint appears in temporal scaling, not just spatial.

Status: DERIVED. The 120-grid projects identically at every scale.

A second setting: the Molien series on $`S^3/2I`$ shows $`2I`$ filtering scalar harmonics on the full 3D $`S^3`$, producing a gap in the invariant spectrum that MIT reads as the counterpart of the CMB low-<i>ℓ</i> deficit. The gap is a spectral fact about the quotient and holds independent of cosmology; where it lands on the sky rides on the independently read curvature radius, and reaching a multipole at all takes a spatial projection the framework does not yet derive ([CMB Anomalies](../../../../cosmos/files/cmb-anomalies.md) §IV). The same algebra that sets the 120 domain on the surface operates on the 3D harmonics of the venue, so the filtering is genuinely volumetric rather than confined to the 2D Möbius surface. That much supports the claim that the 120-grid projects into every gravitationally coherent scale, at both the 2D surface eigenvalue and the 3D cavity spectrum; whether it projects onto the sky is a separate question, and open.

### Joint 3: Observation is sampling through a coherent domain

Phase field mechanics: $`\Theta = \Theta_0 + \Theta_f`$, where $`\Theta_f`$ depends on environment (gravitational potential). Sampling requires a domain where potential is coherent. At galactic scale, the proposed coherence radius was $`L_f \approx 13`$ kpc (SPARC-falsified).

Status: The principle (coherence required for sampling) is DERIVED and general. The specific galactic scale $`L_f = v_c^2/a_0`$ was derived, tested against SPARC, and falsified. The galactic coherence scale $`L_g`$ is open.

The [cone point coherence notes](cone-point-coherence.md) explore the geometric mechanism: whether the $`W`$-independence of the zonal first-positive eigenvalue is the structural reason coherence holds within $`L_g`$. The zonal eigenvalue $`2/R^2`$ does not depend on $`W`$ because the zonal equation contains no $`W`$: the constant transverse mode has $`\mu = 0`$ ([first-eigenvalue paper](../../bedrock/files/first-eigenvalue.md) §4.1). It is the first positive eigenvalue only for the narrow band, $`W \le \pi R/2`$ (Theorem 1.2). Key findings from the coherence notes: GR tidal curvature in the flat-curve regime is Euler-type with power-law Jacobi solutions that structurally cannot zero, so the needed curvature lives at the topology-gravity interface; and SPARC falsified $`L_f = v_c^2/a_0`$ as the coherence radius, shifting the cone-point target from $`L_f`$ to whatever $`L_g`$ turns out to be.

### Joint 4: Black hole collapse and coherence-domain boundaries are NOT the same response law

Tempting unification: both are gravitationally-driven boundaries on the same phase operator $`C(\Theta)`$, so is a coherence-domain boundary (Oort Cloud, $`L_g`$, $`R_\Lambda`$) just a small instance of the same mechanism that drives $`\Theta \to 0`$ at a horizon?

Tested directly. [Black Double Zero's](../../../../cosmos/files/black-hole.md) §VIII.1 forces the leading behavior $`C/C_0\sim1-r_s/r`$ at the horizon; taking that as the global form (the minimal extension, not a further derivation) gives $`\delta\Theta \approx [\tan(\pi\Theta_0)/\pi]\cdot|\Phi|/c^2`$ near a well $`\Theta_0`$. Run at galactic potential ($`v_c = 220`$ km/s): predicted shift $`\sim 2\times10^{-7}`$, five orders of magnitude short of the established bosonic step (2/120) needed for the Hubble-tension mechanism. Run at the Sun's potential at 144,000 AU ($`GM_\odot/rc^2 \sim 7\times10^{-14}`$): predicted shift $`\sim 3\times10^{-14}`$, utterly negligible, no boundary of any kind. (A different global extension could in principle change the weak-field number, but only via an ad hoc, undemonstrated rescaling with no independent motivation, itself an additional mechanism, not a rescue of this one.)

Diagnosis: a category mismatch, not a missing generalization. The horizon mechanism is a single-well, absolute-potential-depth response, with a natural zero from asymptotic flatness. Coherence-domain nesting (Piece B) is a tidal *dominance crossover* between two competing, comparably shallow potentials, a different physical quantity, and (for an extended mass distribution like a galaxy) absolute $`\Phi`$ isn't even uniquely defined the way it is for Schwarzschild.

Status: DEAD. The absolute-$`\Phi`$ bridge from the horizon to ordinary coherence-domain boundaries is falsified by orders of magnitude, not a hair. What survives independently: the horizon-as-node picture (unaffected, see Black Double Zero's) and coherence-domain nesting via tidal dominance (Piece B/C below, still open on its own terms). Black Double Zero's has been corrected to stop asserting this unification (its former working-note companion is now consolidated into that page, §VIII.6).

---

## IV. Pieces on the Bench (Motivated, Not Yet Joined)

### Piece A: 2D angular + 1D radial = perceived 3D

The observer's actual reception channels:

| Channel | Dimension | MIT source | Character |
|---------|-----------|------------|-----------|
| Angular reception | 2D ($`\theta, \varphi`$) | Möbius surface ($`n = 2`$) | Native. Observer receives on the surface. |
| Radial sampling | 1D ($`z`$, via redshift) | Phase-reading along $`S^1`$ | The edge carries the wave; redshift is what phase-reading looks like from the edge looking outward. |
| Temporal flow | 1D ($`c`$) | $`S^1`$ edge | The edge IS time. Not a container. |

Nobody perceives 3D volume directly. It is constructed: 2D angular + 1D radial = perceived "3D."

This gives the 3/2 a physical interpretation: the topology produces 2, the observer constructs 3, and the Gauss-Codazzi conversion is the formal expression of that construction. The observer is already inside $`S^3`$. Already in the venue. The 3/2 is how observation works through the Möbius twist, not a toll levied for the privilege.

Status: MOTIVATED. Structurally clean. The radial channel (phase-reading along $`S^1`$) is conceptually identified; formal operator definition remains open.

### Piece B: Coherence domains nest

If the 120-grid is scale-free (Joint 2), and sampling requires coherence (Joint 3), then every gravitationally bound mode defines its own coherence boundary: the region within which that mode's potential dominates and sampling channels are phase-locked to its symmetry.

**Dominance, made precise.** "Dominates" is a tidal comparison, not an absolute-potential one: the ambient next-mode-up acceleration is locally uniform across the bound system and cancels in its free-fall frame (equivalence principle), so what actually sets a boundary is where the local mode's tidal strength equals the next mode's:

```math
\mathcal{D}(r) = \frac{\text{local mode's tidal strength}}{\text{next mode's tidal strength}}, \qquad \mathcal{D}(r_c) = 1
```

Tested for the solar/Oort case in Piece C: standard dynamics alone (no MIT content) puts $`r_c`$ in the right neighborhood. This is also the reason Joint 4's attempt to reuse the black hole's absolute-$`\Phi`$ response here fails: that map answers a different question (how deep is the local well) than the one a coherence boundary asks (which of two wells wins).

| Mode | Dominant potential | Coherence boundary | Approximate scale |
|------|-------------------|------------------------|--------------------|
| Cosmic | $`\Lambda`$ | $`R_\Lambda`$ (de Sitter horizon) | $`\sim 10^{26}`$ m |
| Galactic | Dark matter halo | $`L_g`$ (unknown; original candidate $`L_f`$ falsified) | $`\sim 4 \times 10^{20}`$ m |
| Stellar | Solar gravity | Oort Cloud | $`\sim 2 \times 10^{16}`$ m (~144,000 AU) |
| Planetary | Earth gravity | Hill sphere | $`\sim 1.5 \times 10^{9}`$ m |

At each boundary: the dominant mode changes. The observer transitions from one coherence domain to the next. What changes is which instrument the observer is listening through, not what's being listened to.

The machinery that derives $`L_f = v_c^2/a_0`$ at galactic scale has not been run at other scales, and it used the wrong kind of variable (absolute potential/velocity, not a tidal comparison; see above). The question: does the tidal-dominance definition generalize to $`L_g`$ and the other boundaries, and separately, does crossing $`\mathcal{D}=1`$ have any derived effect on the sampling operator, or only a standard-dynamics location?

Status: MOTIVATED. The dominance criterion is now precise; whether it does anything to $`\Theta`$ or $`C`$ is the central open question of the project.

### Piece C: Oort Cloud $`\approx`$ 144,000 AU is the solar coherence boundary

Physical reality (not disputed by anyone):

| Inside solar mode | Outside solar mode |
|--------|---------|
| Sun's gravity dominates | Galactic tides dominate |
| Objects orbit the Sun | Objects drift |
| Ecliptic defines symmetry plane | No preferred plane |

MIT-specific claim:

| Inside solar mode | Outside solar mode |
|--------|---------|
| Angular + radial channels phase-locked to solar mode | Sampling transitions to galactic mode |
| 2D-to-3D perception anchored to ecliptic | Perception anchored to galactic plane |
| $`\Theta_f`$ referenced to solar potential | $`\Theta_f`$ referenced to galactic potential |

**Boundary test (standard dynamics, no MIT content).** Dominance made precise (Piece B) as a tidal-crossover condition:

```math
\mathcal{D}(r) = \frac{GM_\odot/r^3}{\lambda_z}, \qquad \lambda_z \simeq 4\pi G\rho_0 \;\text{(leading vertical galactic tide; Oort-constant correction }2(A^2-B^2)\text{ subdominant near the Sun)}
```

Setting $`\mathcal{D}(r_c)=1`$: $`r_c = (M_\odot/4\pi\rho_0)^{1/3}`$. With $`\rho_0 \approx 0.1\,M_\odot\,\text{pc}^{-3}`$ (order-of-magnitude local density; $`r_c \propto \rho_0^{-1/3}`$, so a $`\pm1.5\times`$ density range gives $`r_c \approx (1.67`$–$`2.19)\times10^5`$ AU):

```math
r_c \approx 1.91\times10^5\text{ AU}
```

That is standard celestial mechanics, the same galactic-tide balance that sets the real Oort cloud's outer edge, not an MIT result. It lands within the project's own broad 50,000–200,000 AU observational range (Piece D), about 33% beyond 144,000 AU: at 144,000 AU itself, $`\mathcal{D}\approx2.3`$, solar tide still winning by roughly a factor of 2, true equality nearer 191,000 AU. Standard dynamics gives a crossover of the right *order*; it does not uniquely select 144,000 specifically, and the real cloud's outer edge is set by a mix of the galactic tide and passing-star perturbations depending on the cloud's extent, not a single sharp static tidal surface.

**What this does and doesn't establish.** It shows the tidal-dominance definition (Piece B) is physically sound and lands in the right neighborhood using nothing but standard gravity, no sampling operator, no $`\Theta`$, no $`C`$. It says nothing about whether crossing $`\mathcal{D}=1`$ does anything to those quantities. That question is untouched.

Status: MOTIVATED. Requires Piece B to lock first. Tidal-dominance boundary test passed (order of magnitude, standard dynamics); the MIT-specific bridge (does $`\mathcal{D}=1`$ affect $`\Theta`$/$`C`$/sampling) remains fully open.

### Piece D: 144,000 = $`12^2 \times 10^3`$

The number 144,000 sits at a junction of structures native to $`S^3`$:

| Path | Value | Structure |
|------|-------|-----------|
| Fibonacci | $`F_{12} = 144`$ | 12th Fibonacci number |
| 12-fold | $`12^2 = 144`$ | Square of the zodiacal/structural division |
| 120-grid | $`120 = 12 \times 10`$ | 12 is a factor of 120 |

The 12-fold structure is native to $`S^3`$ (12 is a factor of 120; the icosahedron has 12 vertices). Fibonacci wells live on the 120-grid. $`144 = F_{12} = 12^2`$. The two sequences that MIT treats as fundamental (Fibonacci stability and 12-fold partition) intersect at this number.

Caution: the Oort Cloud radius is observationally estimated between ~50,000 and ~200,000 AU depending on the source. 144,000 falls within that range but is not a precision measurement. Whether the number is structural or approximate is genuinely open.

**Bearing on "predicts vs. accommodates."** Piece C's tidal-dominance boundary test shows standard gravity alone, no MIT content, already produces a crossover of this general order ($`\sim1.9\times10^5`$ AU, using only $`M_\odot`$ and the local galactic density). That doesn't kill the numerology, but it raises the bar: 144,000 needs to be more than "the right order of magnitude," since ordinary astrophysics already delivers that. Tilts the open question toward "accommodates" until something ties $`12^2\times10^3`$ to the tidal-crossover formula itself, not just to the same broad range.

Status: OBSERVATION. The numerical coincidence is real. Whether MIT predicts it or merely accommodates it is unresolved.

### Piece E: CMB-ecliptic alignment

Standard cosmology calls it the "axis of evil": the CMB quadrupole and octupole align with our ecliptic plane. No causal mechanism in ΛCDM connects a cosmological signal to a local solar system feature.

MIT reading: if the observer's coherence domain is anchored to the ecliptic (Piece C), then the CMB is resolved through the ecliptic sampling frame. The alignment is not contamination; it is the sampling theorem operating through the local coherence domain.

Prediction (if the chain holds): an observer in another stellar system would resolve CMB features through THEIR local symmetry plane. Not a different CMB: the same signal, sampled through a different coherence domain.

Status: DOWNSTREAM, with both topological avenues now closed. The even/odd-ℓ grading route is dead: the quotient is chiral, carrying no orientation-reversing identification (see [CMB Anomalies](../../../../cosmos/files/cmb-anomalies.md), [R problem](r-problem.md)). The source-side covariance route is dead too, and it closes in a way that bears on this piece directly: the quotient's isotropy group $`A_5`$ forces the quadrupole isotropic and uncorrelated with the octupole, so any Gaussian source reaching the sky by an $`A_5`$-preserving map leaves the two axes' relative orientation uniform ([The P1 Bridge](molien-p1-bridge.md) §II). The locality reading above survives precisely by not being such a map: the ecliptic is no axis of the observer's $`A_5`$, so an ecliptic-anchored coherence domain breaks it by construction. That promotion matters. Breaking the observer's $`A_5`$ was an incidental feature of the reading and is now its load-bearing requirement, and the one a sampling-frame mechanism would have to deliver explicitly rather than assume. The reading still competes with the mundane ecliptic-systematics explanation, and it still requires Pieces A, B, and C. If they lock, this follows; if any fail, no foundation.

### Piece F: Galactic Year $`\approx`$ cosmic chronon

| Quantity | Value |
|----------|-------|
| $`\tau_c = T_{\text{cosmic}}/120`$ | $`\approx 275`$ Myr |
| Galactic Year (MW orbital period) | $`\approx 225-250`$ Myr |

These are close. If the cosmic chronon is the minimum resolvable phase advance at cosmic scale, and the Milky Way orbits at roughly one chronon per revolution, that suggests the galaxy is operating near one "tick" of cosmic resolution.

If the 120-grid nests (Piece B), the galactic orbital period is the galactic-scale instance of $`\tau = T/120`$ for some appropriate $`T`$. But which $`T`$? And why should $`T_{\text{galactic}}/120 \approx T_{\text{cosmic}}/120`$? That would require $`T_{\text{galactic}} \approx T_{\text{cosmic}}`$, which is not obvious.

Status: OBSERVATION. Intriguing. Possibly coincidence. Requires nested chronon derivation.

---

## V. Gaps (What's Missing)

| # | Gap | What would fill it | Priority |
|---|-----|--------------------|----------|
| 1 | Nested $`L_g`$ derivation | Piece B's tidal-dominance definition ($`\mathcal{D}(r)=1`$) is the candidate general mechanism, tested (order of magnitude only) for the solar/Oort case (Piece C). Not yet run for $`L_g`$ itself (galactic vs. cosmic tidal crossover) or any other boundary. | HIGH (everything depends on this) |
| 2 | Oort Cloud radius from first principles | Answered in part: standard tidal-dominance dynamics (no MIT content) predicts a crossover of the right order, $`\sim1.9\times10^5`$ AU, not a precision hit on 144,000 specifically (Piece C). MIT has not yet added anything beyond standard celestial mechanics here; see Gap 8. | Downgraded to MEDIUM: the standard-physics half is answered, the MIT half is Gap 8 |
| 3 | Galactic Year $`\approx \tau_c`$ coupling | Derive the relationship or demonstrate independence. | MEDIUM |
| 4 | The radial channel (formal operator) | Conceptually identified: phase-reading along $`S^1`$. Redshift is the observable expression. Formal operator definition connecting this to the sampling theorem remains open. | LOW (concept clear; formalism follows) |
| 5 | $`\times 1000`$ factor | 144 appears at the structural level ($`F_{12}`$, $`12^2`$). The physical boundary is at 144,000 AU. Where does the $`\times 10^3`$ come from? Scaling between hierarchy levels? | MEDIUM |
| 6 | Oort Cloud observational precision | Literature review: how well is the boundary actually constrained? Is 144,000 AU within the uncertainty, or is it a specific measured value? | LOW (but determines whether Piece D is meaningful) |

| 7 | Arpeggio structure | Black hole (node) → galaxy (first harmonic) → universe (fundamental) → octave (Möbius double cover). If the cone point nests, each scale is a partial of the same standing wave, and the progression across scales is an arpeggio through the chord. Is the relationship between nested coherence domains harmonic? Does the node-to-mode progression follow the same spectral structure at every level? Note: Joint 4 killed the literal reading (black hole = same $`\Phi\to\Theta`$ response as a coherence boundary); whatever "node" means in this arpeggio, it isn't that. | MEDIUM (conceptual; sharpens after Gap 1) |
| 8 | Does crossing $`\mathcal{D}=1`$ do anything? | The tidal-dominance boundary test (Piece C) succeeds at the level of standard dynamics. Whether crossing it has any derived effect on $`\Theta`$, $`C(\Theta)`$, or the sampling operator is untouched. This is now the sharpest form of the project's central question (Section I). | HIGH (this is now the actual open question, not the boundary location) |

The [cone point coherence notes](cone-point-coherence.md) add a ninth gap upstream of Gap 1: **what sources the curvature $`K_g`$ at galactic scale?** The Frobenius program in that file determines whether the cone point mechanism provides the geometric foundation for nested coherence. Gap 1 here and the curvature sourcing question there are coupled: both ask how the topological structure interfaces with the gravitational field at sub-cosmic scales.

---

## VI. The Picture (If It All Connects)

```
Cosmic mode (T = 33 Gyr, boundary = R_Λ)
    |
    |--- 120-grid projects into cosmic chronon (τ_c ≈ 275 Myr)
    |
    |--- Galactic mode (T ≈ Galactic Year, boundary = L_g)
    |        |
    |        |--- 120-grid projects into galactic chronon
    |        |
    |        |--- Black holes = nodes (double zeros: Θ → 0, Ω_H → 0)
    |        |
    |        |--- Stellar mode (T = ?, boundary ≈ 144,000 AU)
    |                 |
    |                 |--- Ecliptic defines local sampling plane
    |                 |--- 2D angular + 1D radial = 3D perception
    |                 |--- 3/2 perception geometry operates here
    |                 |--- CMB-ecliptic alignment = sampling fingerprint
    |                 |
    |                 |--- Planetary mode (T = ?, boundary = Hill sphere)
    |                          |
    |                          |--- (further nesting, not yet explored)
    |
    Arpeggio: node → harmonic → fundamental → octave (Möbius double cover)
```

At every level:
- The 120-grid is the same (scale-free structure)
- $`\sqrt{\Omega}`$ is the same (observer is always at the midpoint)
- 3/2 is the same (how the observer perceives the venue through the twist)
- The coherence domain is different (set by the dominant gravitational mode)
- The chronon is different ($`\tau = T/120`$ for the local $`T`$)

The structure doesn't change. The scale does. The coherence domain does.

---

## VII. Build Order

| Step | Action | Unlocks |
|------|--------|---------|
| 1 | Formalize the radial channel operator (Gap 4) | Locks Piece A (concept already clear; formalism needed) |
| 2 | Derive $`L_g`$ at arbitrary gravitational mode (Gap 1) | Locks Piece B |
| 3 | Apply the $`L_g`$ derivation to solar system (Gap 2) | Locks Piece C |
| 4 | Literature review on Oort Cloud constraints (Gap 6) | Determines if Piece D is structural or approximate |
| 5 | Derive or exclude Galactic Year coupling (Gap 3) | Resolves Piece F |
| 6 | Trace $`\times 1000`$ factor (Gap 5) | Strengthens or weakens the 144,000 identification |
| 7 | State CMB-ecliptic prediction with conditions (Piece E) | Testable output of the full chain |

---

## VIII. Falsification

| Prediction | Falsified if... |
|------------|-----------------|
| Observer-isolation guardrail | Any derivation implying two observers' realities become disconnected rather than differently sampled. Treated as a flag on the derivation, not a result. |
| Coherence domains nest | Phase field effects shown to operate ONLY at galactic scale with no sub-galactic structure |
| Oort Cloud is a coherence boundary | An observer outside the Oort Cloud (interstellar probe) measures identical CMB multipole alignment |
| CMB-ecliptic alignment is local | Multiple independent stellar systems shown to share the SAME CMB alignment axis |
| 144,000 AU is structural | Oort Cloud boundary precisely measured at a value incompatible with 144,000 (e.g., 80,000 or 300,000 AU with tight error bars) |

---

## IX. Notes

**On the 3/2 and this project.** The 3/2 conversion is already locked at cosmological scale ([The Waltz](../../../../spectrum/files/the-waltz.md)). This project asks whether it also operates at local scale, with the Oort Cloud defining where "local" ends. The ratio doesn't change. The realization site does.

**On what "coherence boundary" means.** Not a wall. Not a force field. The boundary where one gravitational mode's dominance gives way to the next. Inside: sampling channels are phase-locked to that mode's symmetry. Outside: they phase-lock to the next mode up. The wave is coherent everywhere. The exchange rate ($`G`$) is the same everywhere. The coherence domain changes.

**On claim discipline.** This file contains DERIVED parts, MOTIVATED pieces, and genuinely OPEN gaps. The temptation is to treat the whole chain as derived because the parts feel right together. Resist. Each joint needs its own derivation. The workbench exists so we can see what's bolted and what's just sitting next to each other.

---

*The grid doesn't set a size. It sets a structure. The structure projects into every scale. This project asks: does it?*

---

/ **[`↑top`](#top)** / **[`main`](https://github.com/dmobius3/mode-identity-theory/tree/main/)** / **[`framework`](/files/framework/)** / **[`bedrock`](/files/framework/files/bedrock/)** / **[`working`](/files/framework/files/working/)** / **[`cosmos`](/files/cosmos/)** / **[`spectrum`](/files/spectrum/)** / **[`tools`](/files/tools/)** /
