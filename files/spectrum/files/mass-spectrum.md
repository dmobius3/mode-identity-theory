<a id="top"></a>
/ **[`main`](https://github.com/dmobius3/mode-identity-theory/tree/main/)** / **[`framework`](/files/framework/)** / **[`bedrock`](/files/framework/files/bedrock/)** / **[`working`](/files/framework/files/working/)** / **[`cosmos`](/files/cosmos/)** / **[`spectrum`](/files/spectrum/)** / **[`tools`](/files/tools/)** /

---

# ⚛️ Mass Spectrum

<img src="https://img1.wsimg.com/isteam/ip/21cc2ac0-6dc4-4b19-93ef-6a7079ac9d3c/Mass%20Spectrum.png" width="100%" alt="Mass Spectrum">

The Standard Model contains 12 fundamental fermions spanning 12 orders of magnitude in mass. The Higgs mechanism explains how particles acquire mass. It does not explain why they have the masses they do. This page constructs a mass formula from four ingredients, each traced to a single topological postulate: $`S^1 = \partial(\text{Möbius}) \hookrightarrow S^3, \quad \partial S^3 = \emptyset`$. 

The formula is applied to the 8 nontrivial irreducible representations of the binary icosahedral group across 3 isolated flat connections, producing 24 ranked entries under a uniform topological normalization: 22 acyclic torsion invariants and 2 non-acyclic diagonal entries at their canonical topological value (§II.4). Every torsion factor is an exact algebraic closed form in $`\mathbb{Q}(\varphi)`$, built from irrep-level closed forms that two independent methods reproduce (§II.5).

Lined up against the measured fermions, with the electron as the benchmark that sets the absolute scale, five of the remaining 8 charged fermions have a quantum-number-compatible entry within a factor of 3, and four within ×3 after sector-first adjudication (§III). The down quark sits just outside at 3.2; the up and charm quarks are unassigned. The three neutrinos rest on absolute masses nobody has measured; the $`R_1`$ entries (0.87, 7.3, 66.7 meV) sit in ordered qualitative resemblance to the observed splitting scales, a proxy comparison carrying no scorecard weight (§V).

This is a comparison, not a prediction. The entries and their quantum numbers are fixed a priori by the topology; which entry lands on which measured fermion is read against the data. A pre-registered null test (`mass-null-v1.1`) returns $`p_A = 0.690`$, so the ×3 proximity count is not itself evidence for the specific torsion values. The weight rests on the exact structural outputs: the closed-form torsion algebra, the isospin gate, and the 24-entry construction. The gate carries one caveat the [claim ledger](../../framework/files/working/files/claim-ledger.md) records and this page must not drop: the rule is bespoke, written with the known assignments in view, so its eleven consistent evaluations are a consistency check on a rule built for this set rather than an independent prediction.

| Result | Count |
|---|---|
| Compatible coverage within ×3 | 5 of 8 charged fermions ($`m_e`$ is the benchmark) |
| Adjudicated assignments within ×3 | 4 of 8 under the sector-first no-slide rule (d adjudicated but outside ×3 at 3.2; u, c unassigned; b compatible at 1.17 but outside its structural sector; μ/s share rank 15; τ at 2.75) |
| Neutrinos | 3 proxy rows (lightest / solar / atmospheric scale); absolute masses unmeasured; ordered resemblance to the splitting scales, not hits |
| Unassigned | $`u`$ (no compatible entry within ×3); $`c`$ (no compatible entry within ×3); $`b`$ (compatible coverage at rank 17, no assignment in its $`R_2`$ sector) |
| Nature | comparison, not prediction |

## I. The Formula

```math
\Large \boxed{m(\rho, \sigma) = \mu_\Lambda \cdot C_{\text{geom}}(\rho) \cdot \left(\sqrt{\Omega_\Lambda}\right)^{\text{dist}(\rho)/30} \cdot T^2(\rho \otimes \sigma)}
```

Four factors. Four sources. Each traces independently to the topological postulate.

| Factor | Role | Value |
|---|---|---|
| $`\mu_\Lambda`$ | Vacuum energy floor. Fourth root of cosmological constant energy density. Sets the overall mass scale. | $`\rho_\Lambda^{1/4} \approx 2.25 \text{ meV}`$ |
| $`C_{\text{geom}}(\rho)`$ | Phase factor. Geometric mean of $`C(e/D) = 2\sin^2(\pi e/D)`$ over Kostant exponents. Encodes each irrep's position on the domain. | $`D = 60`$ (integer spin) or 120 (half-integer) |
| $`(\sqrt{\Omega_\Lambda})^{\text{dist}/30}`$ | Hierarchy exponent. McKay graph distance from $`R_0`$ determines orders of magnitude from the vacuum floor. Denominator is $`h(E_8) = 30`$. | $`\sqrt{\Omega_\Lambda} \approx 1.019 \times 10^{61}`$ |
| $`T^2(\rho \otimes \sigma)`$ | Matter-local-system torsion: Reidemeister on the 22 acyclic products, canonical integral-cohomology normalization on the 2 non-acyclic diagonal products. Vacuum-dependent fine structure within each mass shell. | 24 values from 8 irreps × 3 vacua |

## II. The Factors

### 1. Mass-Sector Floor  $`\mu_\Lambda`$ 

The vacuum energy density of the cosmological constant defines the overall mass scale:

```math
\mu_\Lambda \equiv \rho_\Lambda^{1/4} \approx 2.25 \text{ meV}
```

This is the fourth root of that vacuum energy density, the mass-sector anchor inherited from the calibrated surface sector. All particle masses trace back to this vacuum energy floor, scaled by the hierarchical factors that place each irrep at its position on the spectrum. The Λ entering here is the measured cosmological constant taken as the surface-sector calibration input, so $`\mu_\Lambda`$ is the mass sector's anchor into that calibration, the scale every ratio multiplies, rather than a quantity the framework predicts (see [Three readings of one hierarchy](../../framework/README.md#three-readings-of-one-hierarchy)). Running the mass ratios backwards as an alternative determination of $`R_\Lambda`$ is a separate inverse use of this formula, tracked in the working [R from the mass spectrum](../../framework/files/working/files/r-from-mass-spectrum.md) analysis, which has been executed and misses: the mass route lands $`R_\Lambda \approx 20`$ Gpc against the measured $`\approx 5.4`$, a $`\sim13.4\times`$ miss in $`\Lambda_\text{ref}`$ and about $`3.8\times$ for the best assigned pair. That disagreement is the corpus's largest internal tension, not a pending check.

**Calibration note.** $`\mu_\Lambda`$ carries two jobs at once: it is the fourth root of the vacuum energy density, and it is the absolute normalization of the ladder in §III. The printed value therefore participates in the ladder normalization as well as the vacuum-density definition, so it cannot be retargeted to the framework's [named Planck row](../../framework/README.md#inputs-and-calibration) as a one-number replacement. Two things block that. The same calibration enters both $`\mu_\Lambda \propto \Lambda^{1/4}`$ and the hierarchy $`\Omega_\Lambda \propto \Lambda^{-1}`$, so an entry at McKay distance $`d`$ moves as $`\Lambda^{(15-d)/60}`$ rather than uniformly, which is where the electron's $`m_e \propto \Lambda^{11/60}`$ comes from. Both printed inputs belong to that one pinned calibration: the $`\mu_\Lambda`$ above and the $`\sqrt{\Omega_\Lambda}`$ of §II.3 were generated together, and neither sits on the framework's named Planck row by itself. Freshening either alone corrupts the table it generated rather than updating it, because the two move in opposite directions under any change of anchor. And the absolute ladder carries one end of the $`m_e \leftrightarrow \Lambda`$ closure, whose 2% and ~11% widths are quoted across the corpus as properties of the framework. Retargeting therefore requires rerunning the mass formula and the Waltz $`G`$-closure together, not editing this figure. One class is genuinely exempt, and for a reason the same exponent supplies: a ratio of two entries at the same $`\rho`$ shares both $`C_\text{geom}`$ and the McKay distance, so it reduces to a pure torsion ratio $`T^2/T^2`$ and carries no $`\Lambda`$ at all. The $`R_1`$ neutrino ladder is exactly that, one $`\rho`$ across three vacua. Nothing else here is anchor-free: expressions in $`\mu_\Lambda`$ units still carry $`\Omega_\Lambda^{d/60}`$, and a measured scale compared against $`\mu_\Lambda`$, such as the $`\sim 4`$ and $`\sim 22`$ below, scales as $`\Lambda^{-1/4}`$. Those survive at printed precision because the shift is small, not because they are independent of the anchor. The coupling is executable rather than advisory: [mass-ladder.test.py](scripts/mass-ladder.test.py) inverts the printed $`\sqrt{\Omega_\Lambda}`$ to the $`\Lambda`$ it implies, regenerates $`\mu_\Lambda`$ from that same $`\Lambda`$, and fails if either figure is freshened without the other. That same inversion names the row. Both printed figures encode the Planck 2018 **+BAO** combination ($`H_0 = 67.66`$, $`\Omega_\Lambda = 0.6889`$), which gives $`\sqrt{\Omega_\Lambda} = 1.019 \times 10^{61}`$ and $`\mu_\Lambda = 2.25`$ meV; the framework's [named row](../../framework/README.md#inputs-and-calibration), TT,TE,EE+lowE+lensing, would give $`1.027 \times 10^{61}`$ and $`2.24`$ meV. The two combinations differ by more than the printed precision, so the question is decidable and both inputs answer it the same way: the mass ladder sits on +BAO, not on the row the rest of the corpus quotes. Both are published Planck combinations and neither is wrong; the point is that the two sectors are anchored on different ones, which is the concrete content of the coupling described above. It also recomputes all 24 entries against §III, recovers the $`\Lambda^{(15-d)/60}`$ shift law by perturbation, and confirms the $`R_1`$ ladder is the table's only anchor-free family.

The neutrino mass sector provides direct access to this scale:

| Splitting | Value | Ratio to $`\mu_\Lambda`$ |
|---|---|---|
| Solar: $`\sqrt{\Delta m^2_{21}}`$ | $`\approx 8.6`$ meV | $`\sim 4\,\mu_\Lambda`$ |
| Atmospheric: $`\sqrt{\Delta m^2_{31}}`$ | $`\approx 50.6`$ meV | $`\sim 22\,\mu_\Lambda`$ |

The ratios (≈4, ≈22) are observational comparison ratios, the measured splitting scales over $`\mu_\Lambda`$, not outputs of the mass formula; the formula's own $`R_1`$ entries sit at 0.39, 3.26, and 29.6 $`\mu_\Lambda`$ (§V). KATRIN and cosmological bounds provide the falsification window.

### 2. Kostant Sunflower  $`C_{\text{geom}}(\rho)`$ 

Each irrep sits at a specific position on the finite domain, encoded by its Kostant exponents. The geometric mean of the phase factor $`C(e/D) = 2\sin^2(\pi e/D)`$ over these exponents gives the irrep's amplitude on the spectrum.

```math
C_\text{geom}(\rho) = \bigl(\prod_e 2\sin^2(\pi e/D)\bigr)^{1/(2\,\dim\rho)}
```

The domain size depends on spin: $`D = 60`$ for integer-spin, $`D = 120`$ for half-integer. This encodes the fundamental distinction between bosons and fermions in the geometry. The domain size traces to the edge stabilizer $`Z_4 \subset 2I`$: integer-spin irreps carry only real $`Z_4`$ content ($`D = 60 = |I|`$), half-integer carry only complex pairs ($`D = 120 = |2I|`$).

| Irrep | Spin | $`D`$ | $`C_\text{geom}`$ |
|---|---|---|---|
| $`R_1`$ | Half | 120 | 0.0988 |
| $`R_2`$ | Half | 120 | 0.2436 |
| $`R_3`$ | Int | 60 | 0.5553 |
| $`R_4`$ | Int | 60 | 0.7970 |
| $`R_5`$ | Int | 60 | 0.8017 |
| $`R_6`$ | Half | 120 | 0.2098 |
| $`R_7`$ | Int | 60 | 0.7564 |
| $`R_8`$ | Half | 120 | 0.2382 |

### 3. McKay Elevator  $`(\sqrt{\Omega_\Lambda})^{\text{dist}/30}`$ 

The McKay graph encodes the distance of each irrep from the trivial representation $`R_0`$. Distance determines orders of magnitude separation from the vacuum floor via the hierarchy exponent $`(\sqrt{\Omega_\Lambda})^{\,\text{dist}/30}`$, where the denominator $`h(E_8) = 30`$ is the Coxeter number.

```
R0(1) -- R1(2) -- R3(3) -- R6(4) -- R7(5) -- R8(6) -- R5(4) -- R2(2)
                                                 |
                                                R4(3)  dist 6
  0        1        2        3        4         5        6        7
```

Half-integer spin: R₁, R₂, R₆, R₈. Integer spin: R₀, R₃, R₄, R₅, R₇.

| Irrep | dim | Spin | dist | $`j_\text{first}`$ | Kostant exponents | $`E_8`$? |
|---|---|---|---|---|---|---|
| $`R_0`$ | 1 | Int | 0 | 0 | {0, 30} | No |
| $`R_1`$ | 2 | Half | 1 | 1/2 | {1, 11, 19, 29} | All 4 |
| $`R_2`$ | 2 | Half | 7 | 7/2 | {7, 13, 17, 23} | All 4 |
| $`R_3`$ | 3 | Int | 2 | 1 | {2, 10, 12, 18, 20, 28} | No |
| $`R_4`$ | 3 | Int | 6 | 3 | {6, 10, 14, 16, 20, 24} | No |
| $`R_5`$ | 4 | Int | 6 | 3 | {6, 8, 12, 14, 16, 18, 22, 24} | No |
| $`R_6`$ | 4 | Half | 3 | 3/2 | {3, 9, 11, 13, 17, 19, 21, 27} | 4/8 |
| $`R_7`$ | 5 | Int | 4 | 2 | {4, 8, 10, 12, 14, 16, 18, 20, 22, 26} | No |
| $`R_8`$ | 6 | Half | 5 | 5/2 | {5, 7, 9, 11, 13, 15², 17, 19, 21, 23, 25} | 6/12 |

The $`j_\text{first}`$ rule follows from the McKay multiplicity structure: the spin-<i>j</i> representation of $`SU(2)`$, restricted to $`2I`$, first contains irrep $`\rho`$ at exactly $`j = \text{dist}(\rho)/2`$. This holds for both spin parities and is a consequence of the McKay correspondence between the $`2I`$ representation graph and the extended $`E_8`$ Dynkin diagram.

### 4. Torsion Factors  $`T^2(\rho \otimes \sigma)`$

Three flat SU(2) connections on $`S^3/2I`$ label the three vacuum sectors. Each connection has $`H^1 = 0`$, so the flat vacua are infinitesimally rigid, with no continuous moduli. The factor $`T^2(\rho\otimes\sigma)`$ is the torsion of the flat bundle $`E_{\rho\otimes\sigma}`$:

- **$`\rho \neq \sigma`$ (22 of the 24 products): acyclic.** The torsion is an ordinary Ray-Singer scalar, equal to the metric-independent Reidemeister invariant: the fine structure within each mass shell.
- **$`\rho = \sigma`$ (the 2 diagonal products, a particle in its own vacuum): non-acyclic.** The trivial representation appears, $`H^0 = H^3 = \mathbb{C}`$, and the ledger uses the canonical integral-cohomology value $`T^2(R_0) = 1`$. The unit-radius analytic torsion $`\pi^4/3600 = \mathrm{Vol}(S^3/2I)^2`$ is a harmonic zero-mode normalization, metric-dependent, not a topological invariant, and is not used.

A standing check follows, one a reader can apply to the table directly: a genuine topological torsion on this space form is an algebraic (cyclotomic) number, and every elementary value below is algebraic. A transcendental factor would be the fingerprint of a zero mode carrying geometry.

| Irrep | $`j_\text{first}`$ (trivial) | $`j_\text{first}`$ (standard) | $`j_\text{first}`$ (Galois) |
|---|---|---|---|
| $`R_0`$ | 0 | 1 | 3 |
| $`R_1`$ | 1/2 | 1/2 | 5/2 |
| $`R_2`$ | 7/2 | 5/2 | 3/2 |
| $`R_3`$ | 1 | 0 | 2 |
| $`R_4`$ | 3 | 2 | 0 |
| $`R_5`$ | 3 | 2 | 1 |
| $`R_6`$ | 3/2 | 1/2 | 3/2 |
| $`R_7`$ | 2 | 1 | 1 |
| $`R_8`$ | 5/2 | 3/2 | 1/2 |

Every irrep has an exact closed form. The full Ray-Singer combination on this space form is $`\log T^2 = \zeta'_{\text{coexact}}(0) - 2\,\zeta'_{\text{scalar}}(0)`$; for half-integer irreps the scalar tower is supported at half-integer $`j`$ (odd $`n`$; $`V_1|_{2I} = R_1`$ is the first example):

| Irrep | $`T^2`$ | $`\log T^2`$ |
|---|---|---|
| $`R_0`$ | $`1`$ | $`0`$ |
| $`R_1`$ | $`\varphi^{-4}/4`$ | -3.311 |
| $`R_2`$ | $`\varphi^{4}/4`$ | +0.539 |
| $`R_3`$ | $`(4/5)\varphi^{-2}`$ | -1.186 |
| $`R_4`$ | $`(4/5)\varphi^{2}`$ | +0.739 |
| $`R_5`$ | 25/9 | +1.022 |
| $`R_6`$ | $`1`$ | $`0`$ |
| $`R_7`$ | 9/4 | +0.811 |
| $`R_8`$ | $`4`$ | +1.386 |

$`R_0`$ (trivial representation) is non-acyclic; the ledger uses its canonical topological value $`1`$ (§4 above). Every value is an elementary algebraic invariant in $`\mathbb{Q}(\varphi)`$, uniformly across both spin parities, with $`\varphi`$ entering through the scalar term.

The closed forms interlock: the Galois pairs satisfy $`T^2(R_3)/T^2(R_4) = \varphi^{-4}`$ and $`T^2(R_1)/T^2(R_2) = \varphi^{-8}`$ exactly, and each pair swaps under $`\varphi \to -1/\varphi`$ as Galois conjugates must; the Galois-fixed irreps $`R_6`$ and $`R_7`$, $`R_5`$, $`R_8`$ carry the rational values $`1`$ and $`9/4`$, $`25/9`$, $`4`$. The integer-spin product $`T^2(R_3)\,T^2(R_7)\,T^2(R_5)\,T^2(R_4) = 4`$ and the half-integer product $`T^2(R_1)\,T^2(R_2)\,T^2(R_6)\,T^2(R_8) = 1/4`$ are exact inverses. Every value is verified by a reproducible artifact ([torsion-correction](../../framework/files/working/files/torsion-correction.md), with a mutation-tested `.test.py`) and independently reproduced by a second method (§II.5).

The 24 vacuum torsion values follow from $`\log T^2(\rho \otimes \sigma) = \sum_\tau N_{\rho\sigma\tau} \log T^2(\tau)`$:

| $`\rho`$ | $`T^2(\rho,`$ triv$`)`$ | $`T^2(\rho,`$ std$`)`$ | $`T^2(\rho,`$ gal$`)`$ |
|---|---|---|---|
| $`R_1`$ | 0.0365 | 0.306 | 2.778 |
| $`R_2`$ | 1.714 | 2.778 | 2.094 |
| $`R_3`$ | 0.306 | 0.0365 | 4.000 |
| $`R_4`$ | 2.094 | 4.000 | 1.714 |
| $`R_5`$ | 2.778 | 6.854 | 0.146 |
| $`R_6`$ | 1.000 | 0.688 | 4.712 |
| $`R_7`$ | 2.250 | 4.000 | 4.000 |
| $`R_8`$ | 4.000 | 13.090 | 1.910 |

The two diagonal products contain the trivial representation, $`R_1 \otimes \text{std} = R_0 + R_3`$ and $`R_2 \otimes \text{gal} = R_0 + R_4`$, so both carry the factor $`T^2(R_0) = 1`$: $`T^2(R_1,\text{std}) = 0.306`$ and $`T^2(R_2,\text{gal}) = 2.094`$. $`R_7`$ is Galois-blind, $`T^2(R_7,\text{std}) = T^2(R_7,\text{gal}) = 4`$ exactly, and the $`R_5`$ pair takes the values $`\varphi^{4}`$ and $`\varphi^{-4}`$ exactly.

### 5. Independent Reproduction

[![OpenWave M8.8](/files/assets/openwave-banner-graphite.svg)](https://github.com/openwave-labs/openwave/blob/main/openwave/xperiments/m8_mit/research/findings/m8_8_adjudication_record.md)

The torsion closed forms are reproduced by an independent method on the OpenWave M8 track. This page computes $`T^2`$ analytically, from the Ray-Singer spectral-zeta combination $`\log T^2 = \zeta'_{\text{coexact}}(0) - 2\,\zeta'_{\text{scalar}}(0)`$. The OpenWave run computes it combinatorially, as the Reidemeister torsion of a based chain complex of $`S^3/2I`$, with no spectral, zeta, or heat-kernel input anywhere in its path.

The two definitions are joined by the Cheeger-Müller theorem, which equates the analytic and combinatorial torsions for an acyclic unitary flat bundle, so the agreement is a theorem verified concretely rather than a shared computation repeated. All eight nontrivial values are exactly equal in $`\mathbb{Q}(\varphi)`$, and both Galois ratios and both sector products follow, up to the single global orientation convention in the definition of the torsion, which is fixed once at $`R_7`$. The run was context-isolated, and the supplied topological model was verified, not independently derived. Full record: [M8.8 adjudication](https://github.com/openwave-labs/openwave/blob/main/openwave/xperiments/m8_mit/research/findings/m8_8_adjudication_record.md).

## III. The 24 Entries

24 entries from the formula. The table below shows the comparison to Standard Model (SM) fermions and the entries with no SM match. Bold rows are the preferred SM assignments counted in the headline scorecard. Unbolded repeated labels show nearby candidate entries or mass-shell clusters; they are not counted as separate assignments.

The assignment is constrained, not free. The formula produces 24 ranked entries; four structural filters narrow which entries can correspond to which fermions. The Coxeter-Galois gate (§IV.4) assigns weak isospin $`T_3 = \pm 1/2`$ to each entry. The $`Z_3`$ face decomposition (§IV.1) restricts color-charged assignments to irreps carrying colored pairs. The $`Z_4`$ edge decomposition (§IV.2) fixes the domain for each spin parity. The eta sign gate (§IV.3) restricts positive electric charge to negative-eta entries. Together these filters determine the quantum numbers $`(T_3, Y, Q)`$ at each $`(\rho, \sigma)`$ pair before any mass comparison is made.

Assignment then proceeds **sector-first**: where the vertex structure (§IV.5) names a fermion's irrep sector (the neutrinos on $`R_1`$, the top and bottom on $`R_2`$, the electron on $`R_7`$), the fermion is assigned to its nearest compatible address within that sector, and does not slide onto a compatible address outside it to fill a gap. Fermions without a vertex-named sector go to their nearest quantum-number-compatible entry. This is why the bottom quark, whose nearest compatible entry sits at ratio 1.17 on $`(R_4,\text{gal})`$, is nevertheless unassigned: its sector is $`R_2`$, where its nearest entry is 38× away. Compatible coverage and adjudicated assignment are therefore reported as separate counts.

A pre-registered null test quantifies the table's counting caveat. Randomly reassigning the torsion factors across the fixed quantum-number slots (`mass-null-v1.1`) reproduces or exceeds the observed compatible-coverage score in 69.0% of draws ($`p_A = 0.690`$), the null distribution centered on the observed count (mean 5.02 against the observed 5). The ×3 proximity count is therefore uninformative about whether the specific torsion values occupy the correct slots: the count is the typical outcome of a random torsion assignment.

The mass table's evidential weight rests on the exact structural outputs: the 24-entry construction, the $`T_3`$ gate evaluations (bespoke, per the caveat above), and the closed-form torsion algebra (the Galois pairs $`\varphi^{-4}`$ and $`\varphi^{-8}`$, the exact-inverse sector products $`4`$ and $`1/4`$, $`R_7`$'s Galois-blind $`4`$), now reproduced by an independent method (§II.5), together with the falsifiable outliers, not on the ×3 proximity count.

The three counts answer progressively stricter questions: raw mass density covers 5 of 8 charged fermions within ×3; enforcing the frozen quantum-number gates leaves compatible coverage at the same 5 of 8; retaining the adjudicated no-slide assignments gives the ledger's 4 of 8.

```math
5 = \text{raw density}, \qquad 5 = \text{compatible density}, \qquad 4 = \text{adjudicated assignments}
```

| Rank | $`\rho`$ | dist | $`\sigma`$ | Mass (GeV) | SM | Observed (GeV) | Ratio |
|---|---|---|---|---|---|---|---|
| 1 | $`R_1`$ | 1 | triv | $`8.75 \times 10^{-13}`$ | lightest-scale proxy (not a hit) | unmeasured | — |
| 2 | $`R_1`$ | 1 | std | $`7.33 \times 10^{-12}`$ | solar-scale proxy (not a hit) | $`8.6 \times 10^{-12}`$ | 0.85 |
| 3 | $`R_1`$ | 1 | gal | $`6.67 \times 10^{-11}`$ | atmospheric-scale proxy (not a hit) | $`5.06 \times 10^{-11}`$ | 1.32 |
| 4 | $`R_3`$ | 2 | std | $`5.30 \times 10^{-10}`$ | | dead zone | |
| 5 | $`R_3`$ | 2 | triv | $`4.45 \times 10^{-9}`$ | | dead zone | |
| 6 | $`R_3`$ | 2 | gal | $`5.83 \times 10^{-8}`$ | | dead zone | |
| 7 | $`R_6`$ | 3 | std | $`4.09 \times 10^{-7}`$ | | dead zone | |
| 8 | $`R_6`$ | 3 | triv | $`5.94 \times 10^{-7}`$ | | dead zone | |
| 9 | $`R_6`$ | 3 | gal | $`2.80 \times 10^{-6}`$ | | dead zone | |
| **10** | **$`R_7`$** | **4** | **triv** | $`\mathbf{5.21 \times 10^{-4}}`$ | **$`e`$** | $`\mathbf{5.11 \times 10^{-4}}`$ | **1.02** (benchmark) |
| 11 | $`R_7`$ | 4 | std | $`9.26 \times 10^{-4}`$ | $`e`$ candidate | $`5.11 \times 10^{-4}`$ | 1.81 |
| 12 | $`R_7`$ | 4 | gal | $`9.26 \times 10^{-4}`$ | $`e`$ candidate | $`5.11 \times 10^{-4}`$ | 1.81 |
| 13 | $`R_8`$ | 5 | gal | $`1.51 \times 10^{-2}`$ | $`d`$ | $`4.67 \times 10^{-3}`$ | 3.23 |
| 14 | $`R_8`$ | 5 | triv | $`3.16 \times 10^{-2}`$ | (up-type entry, unassigned) | | |
| **15** | **$`R_8`$** | **5** | **std** | $`\mathbf{1.03 \times 10^{-1}}`$ | **$`\mu`$ / $`s`$** | $`\mathbf{1.057 \times 10^{-1}}`$ / $`\mathbf{9.34 \times 10^{-2}}`$ | **0.97** / **1.10** |
| 16 | $`R_5`$ | 6 | gal | $`4.18 \times 10^{-1}`$ | | structural residual by default | |
| **17** | **$`R_4`$** | **6** | **gal** | **4.89** | **$`\tau`$** (singlet) / $`b`$ nearest (colored, uncounted) | **1.777** / 4.18 | **2.75** / 1.17 |
| 18 | $`R_4`$ | 6 | triv | 5.97 | $`b`$ neighborhood | 4.18 | 1.43 |
| 19 | $`R_5`$ | 6 | triv | 7.96 | $`b`$ neighborhood | 4.18 | 1.91 |
| 20 | $`R_4`$ | 6 | std | 11.41 | | | |
| 21 | $`R_5`$ | 6 | std | 19.64 | | | |
| **22** | **$`R_2`$** | **7** | **triv** | **161.3** | **$`t`$** | **172.7** | **0.93** |
| 23 | $`R_2`$ | 7 | gal | 197 | (gate-held down-type; no compatible SM) | | |
| 24 | $`R_2`$ | 7 | std | 261.46 | $`t`$ bracket (next-nearest, uncounted) | 172.7 | 1.51 |

**Notes on the table:**

*The electron (rank 10).* $`m_e`$ is the benchmark that sets the absolute mass scale, so its 1.02 is not a forward comparison but the $`m_e \leftrightarrow \Lambda`$ loop closing: entering instead from $`\Lambda`$ through $`\mu_\Lambda = \rho_\Lambda^{1/4}`$ reproduces $`m_e`$ to 2%, which inverts to ~11% in $`\Lambda`$. The forward comparisons are the other charged fermions; neither end of the loop is privileged. See the calibration web on the [framework](../../framework/) page.

*Neutrino rows (ranks 1-3).* The $`R_1`$ sector spans 0.87, 7.3, 66.7 meV in ascending order (triv, std, gal): the lightest mass is unmeasured, the solar scale $`\sqrt{\Delta m^2_{21}} \approx 8.6`$ meV sits 0.85 of rank 2, the atmospheric scale $`\sqrt{\Delta m^2_{31}} \approx 50.6`$ meV sits 1.32 of rank 3. These are proxy comparisons, not assignments and not scorecard hits: all three absolute masses are experimentally unknown, and no generation is claimed from proximity alone. KATRIN, JUNO, and Project 8 will constrain the absolute scale; see §V for the splitting-level comparison.

*The down quark (rank 13).* The ratio of 3.23 is the only assigned charged fermion outside the ×3 window. The down quark mass itself carries large uncertainty (4.67 $`\pm`$ 0.5 MeV from lattice QCD), but even at the upper end of the allowed range the tension remains. Whether this reflects a systematic residual at high McKay distance or a needed correction in the $`R_8`$ Galois vacuum sector is open.

*Rank 15 resolution.* Rank 15 sits between the muon (105.7 MeV) and strange quark (93.4 MeV). The Coxeter-Galois gate (§IV.4) assigns $`T_3 = -1/2`$ to this entry. The $`Z_3`$ face decomposition then splits the mass shell: the singlet component carries the muon ($`Q = -1`$), the colored component carries the strange quark ($`Q = -1/3`$). Both particles occupy the same $`(\rho, \sigma)`$ address in different color sectors.

*Rank 17 resolution ($`\tau`$ and $`b`$).* Rank 17 is $`(R_4, \text{gal})`$ at 4.89 GeV, with $`j_\text{first} = 0`$ (integer), so Stage 1 of the gate assigns $`T_3 = -1/2`$. The $`Z_3`$ split then works exactly as at rank 15: the singlet channel carries the tau ($`Q = -1`$, ratio 2.75), and the colored channel is the bottom quark's nearest compatible entry ($`Q = -1/3`$, ratio 1.17), recorded but not promoted (see the bottom-quark note). The tau is the weakest counted hit; at 2.75 it is the first entry that would fall under any tightening of the ×3 isolation window, a policy question for the whole table at once, not settled here.

*The top quark (ranks 22 and 24).* The gate holds $`(R_2, \text{triv})`$ up-type ($`T_3 = +1/2`$, the pair kept in the trivial vacuum). The top's nearest compatible entry is rank 22 at 0.93, with $`(R_2, \text{std})`$ at 1.51 the next-nearest bracket, uncounted under one-fermion-one-address. The top is bracketed by its own irrep's entries from both sides (0.93 and 1.51).

*The up quark (rank 14, unassigned).* $`(R_8, \text{triv})`$ sits at 31.6 MeV, 14.6× the up mass, and no other up-type entry sits anywhere near 2.16 MeV. The up quark is unassigned.

*The bottom quark.* Its $`R_2`$-sector entries sit at 161.3, 197, and 261.5 GeV, all $`\geq 38\times`$ the bottom mass, so the vertex-structure sector that carries top/bottom offers b no hit. The nearest quantum-number-compatible entry to 4.18 GeV is the colored channel of $`(R_4, \text{gal})`$ at ratio 1.17 (rank 17), with the $`R_4`$/$`R_5`$ shell above it (1.43, 1.91, 2.73, 4.70). That entry is recorded but **not** promoted to hold the count: the ledger assigns a fermion to its nearest compatible address within its structurally named sector where one exists (§III), and moving the bottom from its $`R_2`$ sector onto the compatible $`R_4`$ address would change the selection rule rather than merely select a nearer mass. The observed mass sitting inside an acyclic fan of compatible entries is exactly the kind of coincidence `mass-null-v1.1` is designed to test. Recorded, visible, uncounted.

## IV. Particle Identity

The mass formula assigns each Standard Model fermion to a pair $`(\rho, \sigma)`$. The mass-formula factor is the torsion; the identity comes from the stabilizer structure of the icosahedron.

The binary icosahedral group $`2I`$ inherits three stabilizer subgroups from the icosahedron: face ($`Z_3`$, order 3), edge ($`Z_2`$, lifting to $`Z_4`$ in the double cover), and vertex ($`Z_5`$, order 5). Each irrep of $`2I`$ restricts to these subgroups, producing three independent decompositions. MIT reads the face and edge decompositions as color and domain/spin structure; the vertex decomposition supplies the Galois distinction the Coxeter-Galois gate uses. The Möbius twist enters separately, as the motivated weak-coupling correction in §IV.5.

### 1. Color from Faces

The face stabilizer $`Z_3 \subset 2I`$ is generated by order-3 elements. Color is read off the propagating mode $`\rho \otimes \sigma`$, the same object that carries weak isospin in §IV.4. Restricting it to $`Z_3`$ splits it into color singlets (the channel a lepton can occupy) and color triplet/anti-triplet pairs (the channel a quark can occupy). The channel columns below are the $`\sigma = \text{triv}`$ slice, where $`\rho \otimes R_0 = \rho`$, so they read off each bare irrep. This shows which color channels are available, not by itself whether an entry is a lepton or a quark: the full $`(\rho, \sigma)`$ assignment fixes that, with the charge closed in §IV.4 by Gell-Mann-Nishijima.

| Irrep | dim | Singlets | Colored pairs | SM role / compatible channel |
|---|---|---|---|---|
| $`R_1`$ | 2 | 0 | 1 | neutrino ladder (singlet via $`\rho\otimes\sigma`$) |
| $`R_3`$ | 3 | 1 | 1 | (dead zone) |
| $`R_6`$ | 4 | 2 | 1 | (dead zone) |
| $`R_7`$ | 5 | 1 | 2 | $`e`$ |
| $`R_8`$ | 6 | 2 | 2 | $`d`$, $`\mu/s`$ (the up-type triv entry is unassigned) |
| $`R_5`$ | 4 | 2 | 1 | (structural residual by default / heavy shell) |
| $`R_4`$ | 3 | 1 | 1 | $`\tau`$, $`b`$ |
| $`R_2`$ | 2 | 0 | 1 | $`t`$ |

The $`b`$ label on $`R_4`$ marks the colored channel of the tau's rank-17 address, the bottom quark's nearest compatible entry; the bottom quark itself is uncounted (see §III). Every assigned fermion has the color channel it needs in its propagating mode $`\rho \otimes \sigma`$. The electron (color singlet) sits on $`R_7`$, which already carries 1 singlet at the bare level. The quarks sit on irreps with colored pairs. The neutrinos sit on $`R_1`$, which has no singlet content as a bare irrep; the singlet channel appears only once $`R_1`$ is tensored with the vacuum connection, and this is where reading from $`\rho \otimes \sigma`$ rather than bare $`R_1`$ does real work. It does so without special pleading, because the whole $`R_1`$ sector falls out at once: $`R_1 \otimes \text{std} = R_0 + R_3`$ carries $`1 + 1 = 2`$ singlets, $`R_1 \otimes \text{gal} = R_5`$ carries 2 singlets, and the one $`R_1`$ mode with no singlet channel, $`R_1 \otimes \text{triv} = R_1`$ itself, is rank 1, the sub-solar entry at 0.87 meV. The mode rule gives singlet (SM-neutrino) channels to the two splitting-scale entries and withholds one from the third, so the apparent clash between $`R_1`$ having zero bare singlets and carrying neutrinos is a consistency check the $`R_1`$ sector reading passes. (This is a *channel* argument: $`R_1`$ carries the neutrino singlet content, independent of mass. The mass is separate: the $`R_1`$ ladder parallels the observed proxy scales, but all three absolute masses are unmeasured and no generation is claimed from proximity; see §V.)

The face stabilizer $`Z_3`$ corresponds to the $`SU(3)`$ color factor under the McKay correspondence: removing $`R_3`$ (the node killed by $`Z_3`$ alongside $`R_4`$ and $`R_8`$) from the extended $`E_8`$ Dynkin diagram produces the maximal subalgebra $`SU(3) \times E_6`$.

Color is generation-independent. The equivariant eta at the order-6 face class is perfectly vacuum-invariant: $`\eta = 2`$ in all three vacua. The face geometry looks the same from every vacuum. This matches the Standard Model: color charge is the same across generations.

### 2. Domain from Edges

The domain size $`D = 60`$ vs 120 introduced in §II.2 traces to a deeper structure. The edge stabilizer $`Z_2`$ lifts to $`Z_4 \subset 2I`$, generated by order-4 elements. The $`Z_4`$ decomposition enforces an exact binary:

- Half-integer irreps $`\{R_1, R_6, R_8, R_2\}`$: all $`Z_4`$ content is complex pairs. Domain $`D = 120`$.
- Integer-spin irreps $`\{R_0, R_3, R_7, R_5, R_4\}`$: all $`Z_4`$ content is real. Domain $`D = 60`$.

The real/complex $`Z_4`$ split is exact. MIT reads it as the domain and spin-statistics distinction the mass formula then uses through $`C_\text{geom}`$, which evaluates the Kostant exponents on the $`D = 60`$ or $`D = 120`$ grid.

### 3. The Eta Sign Gate

The Dirac eta invariant $`\eta(\rho, \sigma)`$ varies with the vacuum. Across the mass-formula entries, a strict constraint links it to the charge slot the gates fix:

```math
\eta(\rho, \sigma) > 0 \implies Q \leq 0
```

Equivalently: positive electric charge requires negative eta. All up-type ($`Q = +2/3`$) entries have $`\eta < 0`$. All entries with $`\eta > 0`$ (the addresses at ranks 2, 13, 16, 23) sit in $`Q = 0`$ or $`Q = -1/3`$ slots; rank 23 is such a down-type slot but carries no assigned fermion (it sits 47× the bottom mass, see §III). The eta values are per-address invariants.

The eta invariant measures spectral asymmetry: the parity content of the mode. This gate connects parity to electric charge through the spectral geometry.

### 4. Weak Isospin from the Coxeter-Galois Gate

The same irrep carries different fermions in different vacua. $`R_8`$ supplies an unassigned up-type address in the trivial vacuum, the down-quark address in the Galois vacuum, and the muon/strange address in the standard vacuum. The vacuum $`\sigma`$ selects the electroweak identity. The rule determining weak isospin $`T_3`$ at each $`(\rho, \sigma)`$ is a two-stage filter, computable entirely from Tools 2-4 before any mass is evaluated.

**Stage 1: Spectral parity.** If $`j_\text{first}(\rho, \sigma) \in \mathbb{Z}`$ (integer), the mode enters the Dirac spectrum through the bosonic channel: $`T_3 = -1/2`$.

**Stage 2: Coxeter-Galois gate.** For half-integer $`j_\text{first}`$, evaluate two conditions. First: does $`\rho`$ carry the Coxeter conjugate pair $`(13, 17)`$ under $`h(E_8) = 30`$, and is it stripped by the vacuum? The pair lives in the Kostant exponents of $`R_2`$, $`R_6`$, and $`R_8`$ (all half-integer). The trivial vacuum preserves it ($`\rho \otimes R_0 = \rho`$). The nontrivial vacua strip it (half-integer $`\otimes`$ half-integer $`\to`$ integer-spin components, which carry none of the eight $`E_8`$ exponents). Second: does the tensor product $`\rho \otimes \sigma`$ contain a Galois-nonfixed irrep? The four Galois-nonfixed irreps are $`\{R_1, R_2, R_3, R_4\}`$, whose characters involve $`\sqrt{5}`$; the Galois-fixed irreps $`\{R_0, R_5, R_6, R_7, R_8\}`$ are invariant under $`\sqrt{5} \to -\sqrt{5}`$.

Both conditions must hold for $`T_3 = -1/2`$. If either $`(13, 17)`$ is preserved (trivial vacuum, or $`\rho`$ lacks the pair) or the product is entirely Galois-fixed, then $`T_3 = +1/2`$.

In one line:

```math
T_3 = -\tfrac{1}{2} \iff j_\text{first} \in \mathbb{Z},\ \text{or}\ (13,17)\ \text{stripped and}\ \rho \otimes \sigma\ \text{has Galois-nonfixed content.}
```

**Gate evaluation at eleven featured addresses** (the gate's inputs and outputs are per-address, fixed before any mass is evaluated):

| Rank | $`\rho`$ | $`\sigma`$ | $`j_\text{first}`$ | $`(13,17)`$ | $`\rho \otimes \sigma`$ | Galois-nonfixed? | Path | $`T_3`$ |
|---|---|---|---|---|---|---|---|---|
| 2 | $`R_1`$ | std | 1/2 | N/A | $`R_0 + R_3`$ | (irrelevant) | no pair $`\to`$ +1/2 | +1/2 ✓ |
| 3 | $`R_1`$ | gal | 5/2 | N/A | $`R_5`$ | (irrelevant) | no pair $`\to`$ +1/2 | +1/2 ✓ |
| 10 | $`R_7`$ | triv | 2 | N/A | $`R_7`$ | — | $`j_\text{first} \in \mathbb{Z}`$ | -1/2 ✓ |
| 13 | $`R_8`$ | gal | 1/2 | stripped | $`R_7 + R_5 + R_3`$ | $`R_3`$ yes | both $`\to`$ -1/2 | -1/2 ✓ |
| 14 | $`R_8`$ | triv | 5/2 | kept | $`R_8`$ | — | pair kept $`\to`$ +1/2 | +1/2 (unassigned up-type) |
| 15 | $`R_8`$ | std | 3/2 | stripped | $`R_7 + R_5 + R_4`$ | $`R_4`$ yes | both $`\to`$ -1/2 | -1/2 ✓ |
| 17 | $`R_4`$ | gal | 0 | N/A | $`R_2 + R_6`$ | — | $`j_\text{first} \in \mathbb{Z}`$ | -1/2 ✓ |
| 20 | $`R_4`$ | std | 2 | N/A | $`R_8`$ | — | $`j_\text{first} \in \mathbb{Z}`$ | -1/2 (unassigned) |
| 22 | $`R_2`$ | triv | 7/2 | kept | $`R_2`$ | — | pair kept $`\to`$ +1/2 | +1/2 ✓ |
| 23 | $`R_2`$ | gal | 3/2 | stripped | $`R_0 + R_4`$ | $`R_4`$ yes | both $`\to`$ -1/2 | -1/2 ✓ |
| 24 | $`R_2`$ | std | 5/2 | stripped | $`R_5`$ | all fixed | Galois-fixed $`\to`$ +1/2 | +1/2 ✓ |

Every featured address evaluates consistently with the fermion it carries or the structural role it plays. Five addresses carry the assigned charged fermions (10 the electron; 13 the down; 15 the muon/strange; 17 the tau with the bottom's compatible colored channel; 22 the top), two carry the neutrino-scale proxy rows (2 and 3, not assignments), and four are structural checks: rank 14 is an unassigned up-type address; rank 20 is an unassigned address; rank 23 is the gate's refusal case, at 197 GeV numerically near the top yet held as down-type ($`T_3 = -1/2`$), so the gate declines the tempting reassignment; that shows the rule is not merely permissive, and no more, since the rule is bespoke; rank 24 is up-type by structural inertia ($`R_2 \otimes R_1 = R_5`$, Galois-fixed, nothing for the involution to act on) and brackets the top from above. Eleven featured addresses in all.

**Hypercharge and electric charge follow from $`Z_3`$.** Once $`T_3`$ is fixed, the $`Z_3`$ face decomposition (§IV.1) determines color, and the Gell-Mann-Nishijima formula $`Q = T_3 + Y/2`$ closes the circuit:

| $`Z_3`$ sector | $`T_3`$ | $`Q`$ | $`Y`$ |
|---|---|---|---|
| Singlet (lepton) | +1/2 | 0 (neutrino) | -1 |
| Singlet (lepton) | -1/2 | -1 (charged lepton) | -1 |
| Triplet (quark) | +1/2 | +2/3 (up-type) | +1/3 |
| Triplet (quark) | -1/2 | -1/3 (down-type) | +1/3 |

All ingredients are representation-theoretic: $`j_\text{first}`$ from SU(2) $`\to`$ 2I branching rules, Kostant exponents from the McKay correspondence, tensor product decompositions from the character table, and Galois-fixed/nonfixed status from Gal($`\mathbb{Q}(\sqrt{5})/\mathbb{Q}`$). The quantum numbers $`(T_3, Y, Q)`$ are determined before mass. Particle identity is not: fermions in one family share every quantum number the gates can see (the three charged leptons are all $`Q = -1`$, $`T_3 = -1/2`$, color singlet), so which entry is the electron, muon, or tau is settled by the measured mass, not by the gates. The gates fix the kind; the mass fixes the generation.

### 5. The Vertex and the Twist

The vertex stabilizer $`Z_5 \subset 2I`$ produces a well-defined decomposition of each irrep into three components $`(n_0, n_1, n_2)`$, where $`n_1`$ counts $`(\zeta, \zeta^4)`$ pairs and $`n_2`$ counts $`(\zeta^2, \zeta^3)`$ pairs under the fifth roots of unity. The Galois conjugation $`\sqrt{5} \to -\sqrt{5}`$ swaps $`n_1 \leftrightarrow n_2`$.

| Irrep | dim | $`Z_5`$: $`n_0`$ / $`n_1`$ / $`n_2`$ |
|---|---|---|
| $`R_1`$ | 2 | 0 / 1 / 0 |
| $`R_3`$ | 3 | 1 / 0 / 1 |
| $`R_6`$ | 4 | 0 / 1 / 1 |
| $`R_7`$ | 5 | 1 / 1 / 1 |
| $`R_8`$ | 6 | 2 / 1 / 1 |
| $`R_5`$ | 4 | 0 / 1 / 1 |
| $`R_4`$ | 3 | 1 / 1 / 0 |
| $`R_2`$ | 2 | 0 / 0 / 1 |

$`R_1`$ (neutrinos) and $`R_2`$ (top/bottom structural sector) are pure and complementary under the Galois action. $`R_7`$ (electron) is maximally democratic. The two nontrivial vacua are $`R_1`$ and $`R_2`$ themselves, Galois conjugates that differ precisely in their $`Z_5`$ content: $`R_1`$ carries only $`n_1`$, $`R_2`$ carries only $`n_2`$. MIT reads this complementary $`Z_5`$/Galois distinction between the nontrivial vacua as their electroweak address; the $`T_3`$ assignment itself comes from the Coxeter-Galois gate of §IV.4.

The gauge-ladder ansatz multiplies the weak coupling by $`\cos(\pi/10) = \sqrt{(2+\varphi)}/2`$, and the number sits on this vertex structure: the shortest closed geodesics of $`S^3/2I`$ run along the five-fold axes, the Levi-Civita holonomy around one is a rotation by $`\pi/5`$, and its spin lift has half-trace $`\cos(\pi/10)`$, the half-angle of the flat value $`\cos(\pi/5)`$ ([The Plato Twist](../../framework/files/working/files/plato-twist.md)). The halving there is the spin double cover, not the Möbius orientation $`Z_2`$, which stays distinct both from the base edge $`Z_2`$ above and from the central $`-I`$ inside the lifted $`Z_4`$. The step from that holonomy to a multiplicative weak-coupling correction is not derived. In the companion gauge coupling analysis, the correction uniquely improves $`\alpha_W`$ (from 5.5% to 0.3% error) and uniquely degrades $`\alpha`$ and $`\alpha_s`$ if misapplied. Within the ladder reading, the weak row is the only coupling assigned this twist correction.

$`R_7`$ occupies a special position in this structure. $`R_7 \otimes R_1 = R_7 \otimes R_2 = R_6 + R_8`$: the two nontrivial vacua produce identical torsion at $`R_7`$. The Dirac eta invariant captures this through the antisymmetric vacuum combination $`(5/2)(\eta_\text{std} - \eta_\text{gal})`$, which equals an integer for every irrep and is uniquely zero at $`R_7`$. The irrep that carries the electron sees both vacua identically. It sits at the center of the vertex structure, where the Galois distinction vanishes.

### 6. Summary

| Structure | Decomposition | MIT reading | Status |
|---|---|---|---|
| Face ($`Z_3`$, order 3) | trivial characters and conjugate nontrivial pairs | color singlet and triplet/anti-triplet channels | decomposition exact; the color identification is the reading |
| Edge ($`Z_2`$, lifting to $`Z_4`$) | real versus complex $`Z_4`$ content | domain $`D = 60`$ vs 120, integer versus half-integer | decomposition exact; the spin-statistics identification is the reading |
| Vertex ($`Z_5`$, order 5) | fifth-root sectors and the Galois distinction | electroweak address; with $`j_\text{first}`$ parity it feeds the two-stage Coxeter-Galois gate whose output is $`T_3`$ | decomposition and gate evaluation exact; the electroweak identification is the reading |
| Face / base-edge ratio | $`3/2 = \lvert Z_3 \rvert / \lvert Z_{2,\text{base}} \rvert`$, the face order over the base edge order | gravity correspondence to the vacuum-reference 3/2 (3 Gauss/Ricci, 1/2 de Sitter) | conjectural correspondence |
| Vertex through the twist | $`\cos(\pi/10)`$ | weak-coupling correction | motivated, not derived |

The three stabilizer orders 2, 3, 5 are the primes dividing $`|2I| = 120`$ and the conductors of the four surviving Dirichlet characters in the torsion L-basis. The stabilizers determine the subgroup decompositions; MIT reads those as color, domain, and electroweak structure, while the 3/2 gravity correspondence and the vertex-twist weak correction are interface readings rather than quantities the stabilizer orders generate. The stabilizer structure fixes the available channels; the formula says where each entry sits. Which entry lands on which measured fermion is the comparison, read against the data.

---

## V. Dead Zone, Targets, and Exclusions

Nineteen of the 24 entries carry no adjudicated Standard Model assignment. Three of these are the neutrino-scale proxy rows (ranks 1-3; see The Neutrino Ladder below), which hold comparisons but no assignments. The remaining sixteen have no SM relation at all. Six fall in the "dead zone" (ranks 4-9), the mass range between sub-eV and keV where no known fundamental fermion exists and experimental sensitivity to new states is limited. Two are the sub-benchmark electron candidates (ranks 11-12). One is an unassigned up-type address (rank 14, 31.6 MeV). One is a structural residual by default (rank 16, 418 MeV), with a physical interpretation requiring suppressed non-gravitational couplings. Four form the heavy down-type shell above the bottom (ranks 18-21, 5.97 to 19.6 GeV). Rank 23 ($`R_2`$ gal) at 197 GeV has no quantum-number-compatible SM assignment: it is numerically near $`t`$ (172.7 GeV), but the pre-mass isospin gate rejects it as down-type ($`T_3 = -1/2`$), the behavior a working gate should show when a mass coincidence tempts a wrong assignment. It is a refusal rather than a hit, and it is a refusal by a bespoke rule, so it demonstrates that the gate is not merely permissive without establishing that the rule was fixed independently of the set it sorts. Rank 24 brackets the top from above, uncounted under one-fermion-one-address.

The dead zone is actively probed by sterile neutrino and warm dark matter searches. Physical states at these masses require extremely suppressed non-gravitational couplings. The framework is agnostic about whether these entries correspond to propagating particles or are structural residuals of the spectrum with no physical realization. If physical, they are candidates for sterile neutrino or warm dark matter searches in the eV-keV window.

Rank 16 ($`R_5`$, gal) at 418 MeV sits in a normal mass range between the strange quark and charm quark. No measured fermion occupies this mass. An ordinary colored state there is excluded, so the structural-residual reading is the default; a physical state would require a coupling-suppression mechanism not supplied here.

| Rank | $`\rho`$ | dist | $`\sigma`$ | Mass (GeV) | Range | Status |
|---|---|---|---|---|---|---|
| 4 | $`R_3`$ | 2 | std | $`5.30 \times 10^{-10}`$ | ~0.5 eV | dead zone |
| 5 | $`R_3`$ | 2 | triv | $`4.45 \times 10^{-9}`$ | ~4 eV | dead zone |
| 6 | $`R_3`$ | 2 | gal | $`5.83 \times 10^{-8}`$ | ~58 eV | dead zone |
| 7 | $`R_6`$ | 3 | std | $`4.09 \times 10^{-7}`$ | ~0.4 keV | dead zone |
| 8 | $`R_6`$ | 3 | triv | $`5.94 \times 10^{-7}`$ | ~0.6 keV | dead zone |
| 9 | $`R_6`$ | 3 | gal | $`2.80 \times 10^{-6}`$ | ~3 keV | dead zone |
| 14 | $`R_8`$ | 5 | triv | $`3.16 \times 10^{-2}`$ | ~32 MeV | unassigned up-type address |
| 16 | $`R_5`$ | 6 | gal | $`4.18 \times 10^{-1}`$ | ~418 MeV | structural residual by default |
| 18-21 | $`R_4`$/$`R_5`$ | 6 | | 5.97 / 7.96 / 11.41 / 19.64 | GeV | heavy down-type shell |
| 23 | $`R_2`$ | 7 | gal | $`197`$ | ~197 GeV | no compatible SM (near $`t`$, gate-rejected as down-type) |

### The Neutrino Ladder

The $`R_1`$ sector spans 0.87 meV (triv), 7.3 meV (std), 66.7 meV (gal) in ascending order, against the observed proxy scales: an unmeasured lightest mass, the solar scale 8.6 meV (ratio 0.85 to rank 2), and the atmospheric scale 50.6 meV (ratio 1.32 to rank 3). The three entries sit in ordered qualitative resemblance to the three observed scales. At the splitting level, taking the ladder as absolute masses would give $`\Delta m^2_{21} \approx 5.3 \times 10^{-5}`$ eV² and $`\Delta m^2_{31} \approx 4.5 \times 10^{-3}`$ eV² against the measured $`\approx 7.4 \times 10^{-5}`$ and $`\approx 2.5 \times 10^{-3}`$ eV²: ratios 0.72 and 1.8, an ordered resemblance, not a close reproduction of both splittings. The honesty constraint is firm: all three absolute neutrino masses are experimentally unknown, the solar and atmospheric values are splitting proxies rather than masses, so these rows are proxy comparisons carrying no scorecard weight, and no generation assignment is claimed from proximity. KATRIN, JUNO, Project 8, and the cosmological mass sum will constrain the absolute scale; a measured hierarchy and scale incompatible with (0.87, 7.3, 66.7) meV would falsify the ladder reading outright.

---

## VI. Open Problems

| Item | Status |
|------|--------|
| Entry rule | Open, and unargued rather than tested. The fourth factor enters as $`T^2(\rho\otimes\sigma)`$ rather than $`T`$, on the tensor product rather than on $`\rho`$ alone, multiplying the Kostant seat. Each choice is used throughout and none is derived here. The reproduction (§II.5) certifies the values these choices are applied to, not the choices; the null test (§III) scores the placement of the results, not their construction. |
| $`T_3`$ assignment rule (status note, not an open item) | Established as a gate rule though bespoke, with the reading of its output as weak isospin carried per §IV.6. Two-stage filter: $`j_\text{first}`$ parity + Coxeter-Galois gate. Eleven featured evaluations consistent: five carrying assigned charged fermions, two carrying neutrino-scale proxy rows, and four serving as structural checks. See §IV.4. |
| $`\mu`$/$`s`$ single-entry count | Rank 15 supplies both the muon and the strange via the $`R_8`$ singlet/triplet color split, so two fermions are credited to one $`(\rho,\sigma)`$ address; rank 17 repeats the pattern with $`\tau`$ counted and $`b`$ recorded. Whether a shared address is one hit or two is a standing convention question (a strict one-entry-one-hit reading would give 3 of 8). |
| Up quark assignment | Open. $`(R_8,\text{triv})`$ sits at 31.6 MeV, 14.6× the up mass, and no up-type entry sits near 2.16 MeV. |
| Charm quark assignment | Open. No compatible entry within ×3 anywhere: the nearest entry (rank 16, 418 MeV) is 3.04 away and carries $`T_3 = -1/2`$. All $`R_4`$ entries have integer $`j_\text{first}`$ ($`T_3 = -1/2`$), so charm cannot live on $`R_4`$. |
| $`R_1`$ neutrino ladder | The sector sits in ordered qualitative resemblance to the observed proxy scales (§V: splitting-level ratios 0.72 and 1.8); proxy comparisons only, no assignments, no scorecard weight; falsifiable by hierarchy and absolute-scale measurements. |
| Down quark tension | Rank 13 ratio 3.23, the lone assigned charged fermion outside ×3. Systematic residual at high McKay distance or $`R_8`$ Galois correction is open. |
| Fermion mass residual | Open. The two large residuals are overshoots at Galois vacua (d +0.51 at dist 5; τ +0.44 at dist 6); whether a distance or branch correction captures them is unresolved (see [mckay-propagator-correction](../../framework/files/working/files/mckay-propagator-correction.md)). |
| Dead zone physical status | 6 entries, sub-eV to keV. Propagating states or structural residuals: experimentally distinguishable. |
| Rank 16 | 418 MeV entry ($`R_5`$, gal) with no measured match. A colored state at that mass with ordinary couplings is excluded, so the structural-residual reading is the default here; the physical reading needs an explicit coupling-suppression argument this page does not have. |
| Heavy down-type shell | Ranks 18-21 (5.97 to 19.6 GeV): four down-type entries above the bottom with no SM occupants. Excluded as ordinary colored states at those masses, so these read as structural residuals on the same terms as rank 16. Taken together with it, the honest cost is that the construction over-produces entries in the normal range, which is a charge against the entry rule above rather than a set of open targets. |

---

*The topology permits and Ψ settles. The formula composes; where its entries land is what the data, and this page's own null test, are still deciding.*

---

/ **[`↑top`](#top)** / **[`main`](https://github.com/dmobius3/mode-identity-theory/tree/main/)** / **[`framework`](/files/framework/)** / **[`bedrock`](/files/framework/files/bedrock/)** / **[`working`](/files/framework/files/working/)** / **[`cosmos`](/files/cosmos/)** / **[`spectrum`](/files/spectrum/)** / **[`tools`](/files/tools/)** /
