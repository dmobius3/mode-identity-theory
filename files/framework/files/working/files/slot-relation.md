<a id="top"></a>
/ **[`main`](https://github.com/dmobius3/mode-identity-theory/tree/main/)** / **[`framework`](/files/framework/)** / **[`bedrock`](/files/framework/files/bedrock/)** / **[`working`](/files/framework/files/working/)** / **[`cosmos`](/files/cosmos/)** / **[`spectrum`](/files/spectrum/)** / **[`tools`](/files/tools/)** /

---

# The Slot Relation: Registration

**Type:** Program
**State:** Active
**Status (2026-10-03):** Registered before any derivation: §§ I to VII are frozen, and no route has been worked. The relation's status is OPEN until this page reports.
**Summary:** Asks what MIT says the energies of stable states in the eight McKay slots obey, the energy relation OpenWave's M8.2 success ladder asks for in its last row; registered before any derivation and before any action is chosen.
**Inputs:** `../../../../spectrum/files/mass-spectrum.md` §II.3, `scaling-law-uniqueness.md`, the First Eigenvalue, Coexact Gap and Galois Pair papers (`../../bedrock/README.md`), `projective-carrier.md` §XI, `stress-tensor-bridge.md` (C11), OpenWave's M8.2 and M8.4 (pinned below)
**Frozen:** 2026-10-03 §§ I to VII, the registration, before any derivation

Sections I to VII are frozen as written. The report lands in §VIII, dated, and nothing above it is edited.

---

## I. The Question

OpenWave's field-dynamics contract for MIT, [M8.2](https://github.com/openwave-labs/openwave/blob/6e330a6f49141bc77f926d48e62a02093358b343/openwave/xperiments/m8_mit/research/findings/m8_2_preregistration.md) (locked 2026-07-27), grades a dynamics on $`S^3/2I`$ by a success ladder. Its last two rows read "Stable nonlinear branches / defects exist", a dynamical result, and "Their energies obey a separately pre-registered MIT relation", which it counts as eventual success on its open question OQ1 (§4 there). No MIT page states that relation.

MIT fixes where the slots sit. Each nontrivial irreducible representation $`\rho`$ of $`2I`$ first enters the harmonic tower at level $`\mathrm{dist}(\rho)`$, its distance from the trivial node on the McKay graph ([mass spectrum](../../../../spectrum/files/mass-spectrum.md) §II.3). That is kinematics, and representation theory alone supplies it: any Laplace-type kinetic term places the slots at $`d(d+2)/R^2`$, which OpenWave's [M8.4 kinematic close](https://github.com/openwave-labs/openwave/blob/6e330a6f49141bc77f926d48e62a02093358b343/openwave/xperiments/m8_mit/research/findings/m8_4_kinematic_close.md) calls "calibration, never evidence" and the stress-tensor bridge's C11 calls wiring ([C11](stress-tensor-bridge.md#ii-the-constraint-set-already-in-hand)). What the energies of stable states in the slots obey is dynamics. This page registers the attempt to state it from the framework's own structure, before any action is chosen.

## II. The Slots

| Slot | Dimension | Spin | $`\mathrm{dist}(\rho)`$ | $`j_\text{first}`$ | Note |
|---|---|---|---|---|---|
| $`R_1`$ | 2 | half-integer | 1 | 1/2 | $`Q`$, the defining doublet |
| $`R_2`$ | 2 | half-integer | 7 | 7/2 | $`Q'`$, its Galois conjugate |
| $`R_3`$ | 3 | integer | 2 | 1 | $`\mathrm{Sym}^2 Q`$ |
| $`R_4`$ | 3 | integer | 6 | 3 | $`\mathrm{Sym}^2 Q'`$ |
| $`R_5`$ | 4 | integer | 6 | 3 | |
| $`R_6`$ | 4 | half-integer | 3 | 3/2 | |
| $`R_7`$ | 5 | integer | 4 | 2 | |
| $`R_8`$ | 6 | half-integer | 5 | 5/2 | |

Labels, dimensions, spin classes and distances are the mass spectrum's (§II.3), with $`j_\text{first} = \mathrm{dist}(\rho)/2`$ and $`R_0`$ the trivial representation. The two slots at distance 6 are $`R_4`$ and $`R_5`$.

A field in slot $`\rho`$ is a section of the flat bundle $`E_\rho = S^3 \times_{2I} V_\rho`$ over $`S^3/2I`$, with $`2I`$ acting on $`S^3`$ by deck transformations and on $`V_\rho`$ through $`\rho`$. On such sections the Laplacian's levels are $`k(k+2)/R^2`$, with multiplicity $`(k+1)\,\mathrm{mult}(\rho, \mathrm{Sym}^k\mathbb{C}^2)`$, and the lowest is at $`k = \mathrm{dist}(\rho)`$ [Kostant 2004; Suter 2007]. Native single-valued fields on $`S^3/2I`$ carry none of the eight slots (the M8.4 kinematic close), so every slot field lives on a twisted bundle.

## III. The Object

The relation has the form

```math
E_\rho = E_*\,F(\rho), \qquad \rho \in \{R_1, \ldots, R_8\},
```

and it is stated conditionally: if an admissible realization, one action common to the eight sectors on $`\mathbb{R}_t \times S^3/2I`$ whose slot fields are sections of the $`E_\rho`$, has stable states in the eight sectors, then the energies of the states its comparison convention names obey the relation. Whether such a realization or such states exist is not this page's question; it belongs to the later run, M8.2's rows 2 to 6. Here $`t \in \mathbb{R}`$ is the lifted evolution parameter of the framework's phase coordinate: background phase quantities keep their $`4\pi`$ period, but full dynamical field states at $`t`$ and $`t + 4\pi`$ are not assumed to be identified.

**$`F`$ must:**
1. Be fully fixed and normalized by $`F(R_1) = 1`$, with no free parameter and none set per slot.
2. State its dependence on $`\rho`$. If $`F`$ depends on $`\mathrm{dist}(\rho)`$ alone, $`R_4`$ and $`R_5`$ are degenerate, and that degeneracy is part of the claim. Any further dependence, on dimension, spin class, Galois class or Kostant exponents, is named.
3. Come with its comparison convention: which state in each sector carries $`E_\rho`$, for instance the lowest stable nontrivial stationary state or the states at a common value of a conserved charge, since a branch's energy depends on where on the branch it is read. The convention includes the state selector, any conserved-charge condition, and the energy zero with any renormalization or subtraction rule; the zero is declared once, either each sector's own vacuum or a reference common to all sectors, and applied the same way in every sector. If the convention reads states at a common value of a conserved quantity, $`F`$ holds at every such value or the convention fixes the value. $`F`$ states whether it holds exactly or to a stated order, so that a run can set its tolerance. The convention is fixed from allowed inputs before a route evaluates or writes a candidate $`F`$, applies identically in every sector, and is not changed once a candidate relation is known.
4. Not be the free ladder. A relation the linear, zero-amplitude spectrum of some Laplace-type kinetic term already gives earns nothing: the levels $`\mathrm{dist}(\mathrm{dist}+2)/R^2`$, the frequencies they imply, such as $`(\mathrm{dist}+1)/R`$ under conformal coupling or $`\sqrt{\mathrm{dist}(\mathrm{dist}+2)/R^2 + \mu^2}`$ with one common mass, or the ordering by distance. If a route gives only that, the report says so.
5. Report its relation to MIT's mass formula. The formula's elevator $`(\sqrt{\Omega_\Lambda})^{\mathrm{dist}(\rho)/30}`$, with $`\sqrt{\Omega_\Lambda} \approx 10^{61}`$ the hierarchy number (R1's $`\sqrt{\Omega}`$, not the vacuum fraction), and its representation-local factors $`C_\text{geom}(\rho)`$ and $`T^2(\rho \otimes \sigma)`$ may appear in $`F`$ only as outputs of a declared route, and where $`F`$ departs from them the report states how.

**$`E_*`$** is one common normalization, not a slot parameter. For the relative relation it is $`E_{R_1}`$ under the registered comparison convention. A route may also derive its absolute value from scales the framework already has: the curvature radius $`R`$, the Planck scale through $`\Omega_\Lambda`$, or a calibrated sector anchor that is not a particle mass, such as $`\mu_\Lambda`$. No measured mass, slot energy or new constant enters as an input; that is the standard the postulate bridge's bar sets for the carrier's functional, "without an arbitrary new scale" ([the bar](postulate-bridge.md#dynamical-direction)). If no route fixes the absolute value, the relation's content is the seven ratios $`F(\rho) = E_\rho/E_{R_1}`$, and the report says so.

**A scope fact, stated in advance.** Every natural Laplace or Casimir operator on the round quotient, twisted by a flat bundle or not, scales as $`R^{-2}`$ ([The Ladder Rule](scaling-law-uniqueness.md#ladder-rule-grids)). So if $`F`$ carries a power of $`\Omega_\Lambda`$, a realization can meet it only through a term that carries $`\Omega_\Lambda`$, and that term must be motivated independently of $`F`$, or the run builds its target in. The report states what $`F`$ would require of a realization.

## IV. Inputs

**Allowed:**
- The postulate and the premises the framework fixes ([engine](../../../README.md)): $`S^1 = \partial(\text{Möbius})`$, with the Möbius band in $`\mathbb{RP}^3 = S^3/\{\pm I\}`$; the anti-periodic condition $`\psi(y + L) = -\psi(y)`$; $`\Psi = \cos(t/2)`$; matter as a sampled wave.
- The theorems of three [bedrock papers](../../bedrock/README.md): First Eigenvalue, Coexact Gap and Galois Pair. The Surviving Ray is not an input to R1 to R3: its nonlinear results come from an already chosen common-cubic action, and they enter this page only as the check R5, after $`F`$ is frozen. Its flat-bundle setup may be cited for notation or for standard bundle facts available independently, but not as evidence for $`F`$.
- The carrier rulings of [The Projective Carrier](projective-carrier.md) §XI: 1a and 1c to 1g, with 1b open.
- Canonical results fixed before this registration, each with its label: the scaling law's factored form, a conditional theorem for single-position observables in the spectral-boundary class, with integer depth $`n`$ ([Scaling Law Uniqueness](scaling-law-uniqueness.md)); the ladder rule's grids, derived under the image reading, and its exponent, not derived ([The Ladder Rule](scaling-law-uniqueness.md#ladder-rule-grids)); the McKay distances and first occurrences (mass spectrum, §II.3).
- Standard mathematics and published results, each cited: the representation theory of $`2I`$ and the McKay correspondence [McKay 1981; Kostant 1984, 1985]; the Poincaré series of the irreducible representations and the invariant ring of $`2I`$ on $`\mathbb{C}^2`$ [Kostant 2004; Suter 2007]; the Seifert structure of $`S^3/2I = \Sigma(2,3,5)`$ and the Chern-Simons invariants of flat connections on Seifert manifolds [Kirk and Klassen 1990; Auckly 1994; Nishi 1998; Gukov, Mariño and Putrov 2016].

**Excluded:**
- The 24-entry numeric mass table and any measured mass. M8.2 puts the table out of scope (its 2026-07-29 addendum: null `mass-null-v1.1`, $`p_A = 0.690`$, superseding the pre-correction `mass-null-v1.0`'s 0.174).
- The mass formula's factors as inputs or targets (§III, item 5).
- Any nonlinear energy datum from the Surviving Ray or OpenWave, whether numerical, symbolic, asymptotic or a branch-energy formula, and the Surviving Ray's nonlinear results as evidence for $`F`$ (above). OpenWave's level-6 rays and branch germs (M8.10 to M8.13), and any solver's output, are excluded too.
- Holonomy-sector vacuum energies as a source for $`F`$, Choi and Tachikawa's included. They enter only as checks (§VI).
- Per-slot constants, and scales the framework does not already have.
- A formula fitted to the two known Chern-Simons values (§V, R3).

## V. Routes

Three routes, declared now. No other route enters this page.

**R1. The scaling law.** The factored form $`A/A_P = C(\Theta)\,(\sqrt{\Omega})^{-n}`$ is a conditional theorem for single-position observables in the spectral-boundary class: on the conic band, under the adopted Friedrichs extension and below the critical width, it is equivalent to boundary-mode uniformity, which follows from adopted premises with its weight on the first-positive projection, which no registered sampler supplies, and its depth row is forced at integer $`n`$, definite weight ([Scaling Law Uniqueness](scaling-law-uniqueness.md), Status).
- *Question:* does a slot's energy lie in the theorem's observable class, and if so, what is its weight $`n`$? The page forces the power once definite weight $`n`$ is granted and leaves which $`n`$ an observable carries, its manifold index, to the next layer; does either step carry any dependence on the representation?
- *Success:* a derivation, within the theorem's stated scope, of a nontrivial $`F(\rho)`$. If the applicable rule gives one common $`n`$ for all eight slot energies, R1 closes as an obstruction, and no representation-dependent exponent is assigned by hand.
- *Known obstacles, stated now:* the depth row forces integer $`n`$, so a fractional exponent such as $`\mathrm{dist}/30`$ lies outside it; the mass sector's geometric-mean seat falls outside the theorem's lemma; and the ladder rule's exponent is a homothety weight that no spectral scaling supplies.

**R2. Invariant and covariant degrees.** The invariant ring of $`2I`$ on $`\mathbb{C}^2`$ has basic generators in degrees 12, 20 and 30, with Molien series $`(1 + t^{30})/\big((1 - t^{12})(1 - t^{20})\big)`$, and $`\rho`$ first occurs among the polynomial covariants in degree $`\mathrm{dist}(\rho)`$ [Kostant 2004; Suter 2007]. Under a common homothety $`z \mapsto sz`$, the degree-30 basic invariant scales as $`s^{30}`$ and the lowest $`\rho`$-covariant as $`s^{\mathrm{dist}(\rho)}`$. So a factor $`\varepsilon^{\mathrm{dist}(\rho)/30}`$ follows only if an independently motivated dynamics selects such a common homothetic branch and lets a normalized degree-30 basic invariant set its scale at $`\varepsilon`$ (MOTIVATED, not derived).
- *Questions, in this order:* (a) what supplies the common homothetic scaling; (b) why the degree-30 basic invariant, and not the degree-12 or degree-20 one, sets the scale; (c) what fixes the normalization of the degree-30 generator, and its value, from scales the framework already has; (d) how a state's energy, rather than a covariant's amplitude, inherits that scaling.
- *Success:* (a) to (d) derived from allowed inputs. No $`F`$ is written from this route before they are settled, and an answer to any of them whose only support is that it reproduces the mass formula's elevator does not count.

**R3. Seifert data and Chern-Simons.** $`S^3/2I`$ is the Seifert-fibred homology sphere $`\Sigma(2,3,5)`$. Each slot bundle $`E_\rho`$ carries the flat connection with holonomy $`\rho: 2I \to U(d_\rho)`$; since $`2I`$ is perfect, $`\det\rho`$ is trivial, so $`\rho`$ may be taken in $`SU(d_\rho)`$. Chern-Simons invariants of flat connections on Seifert manifolds are computable, for $`SU(2)`$ [Kirk and Klassen 1990; Auckly 1994] and for $`SU(n)`$ [Nishi 1998].
- *Admission:* R3 counts only if it first derives an energy dictionary, a rule by which a state's energy in a sector inherits that sector's flat-connection data, from allowed inputs and before any slot value is computed. The dictionary also states one trace normalization across the ranks $`d_\rho`$, and it is well defined under the Chern-Simons ambiguity mod 1, either by depending only on the class in $`\mathbb{R}/\mathbb{Z}`$ or by an independently derived canonical lift. Without these, R3 is recorded as DROPPED, and no Chern-Simons table of the eight slots is evaluated for this page.
- *A guard:* the two irreducible SU(2) flat connections on $`\Sigma(2,3,5)`$ have Chern-Simons invariants $`-49/120`$ and $`-1/120`$ mod 1 [Gukov, Mariño and Putrov 2016]. A source assigning them to the holonomies $`Q`$ and $`Q'`$ was not located, and a formula fitted to these two values is excluded.

## VI. Checks of a Frozen Relation

These run only after $`F`$ is frozen, and they never shape it.
- **R4, holonomy-sector vacuum energies.** For $`\mathcal N = 4`$ super Yang-Mills on $`S^3/\Gamma`$ the supersymmetric Casimir energy is independent of the gauge holonomy, for every $`\Gamma`$, $`2I`$ included [Choi and Tachikawa 2026, eq. (2.17)]; in general $`\mathcal N = 1`$ theories a nontrivial holonomy costs energy, shown for $`S^3/\mathbb{Z}_k`$ in their reference BNY11. The $`\mathcal N = 1`$ or non-supersymmetric computation on $`S^3/2I`$ was not located in a search. It needs a chosen action, so it can check a frozen $`F`$ and cannot supply one, and it bears on $`F`$ only if the registered convention measures energies from a zero common to all sectors; under a per-sector vacuum zero those energies are subtracted, and the report says R4 does not apply.
- **R5, the Surviving Ray's common-cubic branches.** These are MIT's one nonlinear slot computation, and as a source for $`F`$ they would be post hoc. OpenWave's [M8.4 pre-registration](https://github.com/openwave-labs/openwave/blob/6e330a6f49141bc77f926d48e62a02093358b343/openwave/xperiments/m8_mit/research/findings/m8_4_preregistration.md) reports small-amplitude continuation as "nonlinear persistence of the installed free structure", never as "dynamical realization".

## VII. Stopping Rule and Grades

**Stopping rule:**
- Each route is worked once, to a written result: a derivation with every step shown, or an obstruction at a named step.
- No route is added after the freeze. An idea met during the work that lies outside R1 to R3 is recorded as a candidate for a separate registration and does not enter this report.
- Nothing is tuned. Once a route's mechanism is stated, its consequences are worked out once, and a route that fails is not rescued.
- No target-bearing numerical experiment, fit or solver run bearing on $`F`$ is performed for this page. Exact computations of group-theoretic or topological data a route has already derived a need for (characters, Poincaré series, Seifert data and Chern-Simons invariants) are allowed only after that step calls for them, and for R3 only after its energy dictionary and normalization conventions are fixed.
- The report lands in §VIII whatever the grade.

**Grades:**
- **DERIVED:** the normalized $`F`$ and its comparison convention follow from allowed inputs with every step shown, and $`F`$ meets §III. $`F`$ is then filed as the relation M8.2's last row asks for, frozen on this repo before any run. Whether the absolute normalization $`E_*`$ is also derived is reported separately; an open absolute scale does not lower a derived ratio relation.
- **MOTIVATED:** a candidate $`F`$ of §III's form, with its underived step named. Whether to file it under that label or hold it is decided separately.
- **OPEN:** no route yields an $`F`$, and each route's obstruction is named at its step. A dynamics can still aim at M8.2's rows 2 to 6, a dynamical result with no claim on the relation, or wait for the carrier question; that is decided separately.

If routes yield different candidates for $`F`$, the report gives each with its grade, and DERIVED needs a single $`F`$. This registration claims nothing about which grade results.

## VIII. Report

Not yet written.

---

## References

- D. R. Auckly, "Topological methods to compute Chern-Simons invariants," Math. Proc. Cambridge Philos. Soc. 115, 229-251 (1994). [doi:10.1017/S0305004100072066](https://doi.org/10.1017/S0305004100072066)
- S. Choi, Y. Tachikawa, "On holography with ADE singularities," JHEP 04 (2026) 168. [doi:10.1007/JHEP04(2026)168](https://doi.org/10.1007/JHEP04(2026)168), [arXiv:2512.20307](https://arxiv.org/abs/2512.20307)
- S. Gukov, M. Mariño, P. Putrov, "Resurgence in complex Chern-Simons theory," [arXiv:1605.07615](https://arxiv.org/abs/1605.07615) (2016).
- P. A. Kirk, E. P. Klassen, "Chern-Simons invariants of 3-manifolds and representation spaces of knot groups," Math. Ann. 287, 343-367 (1990). [doi:10.1007/BF01446898](https://doi.org/10.1007/BF01446898)
- B. Kostant, "On finite subgroups of SU(2), simple Lie algebras, and the McKay correspondence," Proc. Natl. Acad. Sci. USA 81, 5275-5277 (1984). [doi:10.1073/pnas.81.16.5275](https://doi.org/10.1073/pnas.81.16.5275)
- B. Kostant, "The McKay correspondence, the Coxeter element and representation theory," Astérisque S131, 209-255 (1985). [Numdam](http://www.numdam.org/item/AST_1985__S131__209_0/)
- B. Kostant, "The Coxeter element and the branching law for the finite subgroups of SU(2)," [arXiv:math/0411142](https://arxiv.org/abs/math/0411142) (2004).
- J. McKay, "Graphs, singularities, and finite groups," Proc. Sympos. Pure Math. 37, 183-186 (1981). [doi:10.1090/pspum/037/604577](https://doi.org/10.1090/pspum/037/604577)
- H. Nishi, "SU(n)-Chern-Simons invariants of Seifert fibered 3-manifolds," Int. J. Math. 9, 295-330 (1998). [doi:10.1142/S0129167X98000130](https://doi.org/10.1142/S0129167X98000130)
- R. Suter, "Quantum affine Cartan matrices, Poincaré series of binary polyhedral groups, and reflection representations," Manuscripta Math. 122, 1-21 (2007). [doi:10.1007/s00229-006-0055-1](https://doi.org/10.1007/s00229-006-0055-1)
- OpenWave, M8 at commit [6e330a6](https://github.com/openwave-labs/openwave/tree/6e330a6f49141bc77f926d48e62a02093358b343/openwave/xperiments/m8_mit/research/findings): the M8.2 contract (`m8_2_preregistration.md`), the M8.4 kinematic close (`m8_4_kinematic_close.md`) and the M8.4 pre-registration (`m8_4_preregistration.md`).

---

/ **[`↑top`](#top)** / **[`main`](https://github.com/dmobius3/mode-identity-theory/tree/main/)** / **[`framework`](/files/framework/)** / **[`bedrock`](/files/framework/files/bedrock/)** / **[`working`](/files/framework/files/working/)** / **[`cosmos`](/files/cosmos/)** / **[`spectrum`](/files/spectrum/)** / **[`tools`](/files/tools/)** /
