<a id="top"></a>
/ **[`main`](https://github.com/dmobius3/mode-identity-theory/tree/main/)** / **[`framework`](/files/framework/)** / **[`bedrock`](/files/framework/files/bedrock/)** / **[`working`](/files/framework/files/working/)** / **[`cosmos`](/files/cosmos/)** / **[`spectrum`](/files/spectrum/)** / **[`tools`](/files/tools/)** /

---

# 𝄢 Cosmological Constant

<img src="https://pbs.twimg.com/media/HLlsyI3W8AAYqUP?format=jpg&name=4096x4096" width="100%" alt="Cosmological Constant">

This page reads the cosmological constant as geometry. Its coefficient is set by the curvature of the closed spatial domain, with an embedded Möbius surface acting as the selection rule rather than as the source of the scale: the holonomy picks out the twisted sector, and the curvature of the covering great-$`S^2`$ band fixes the level's value. That seed converts through the standard Gauss and de Sitter relations to the dimensionless relation $`\Lambda R^2 = 3`$. The value of $`\Lambda`$ additionally needs the curvature radius $`R`$, which remains open, so this is a coefficient, not a number, and §IV records what identifying that coefficient with the physical constant still assumes.

## I. The relationship

In general relativity Λ sits on the geometric side of the field equations,

```math
G_{\mu\nu} + \Lambda g_{\mu\nu} = 8\pi G T_{\mu\nu}
```

multiplying the metric: pure geometry. General relativity is local. It gives dynamics on a domain but fixes neither the domain nor the value of Λ; on a flat, simply connected, non-compact background the coefficient is unconstrained. Reversing the hierarchy, the present closed-domain construction supplies a distinguished first-positive spectral level, $`\lambda_+ = \Lambda_\text{top} = 2/R^2`$. The covering surface's intrinsic curvature scalar carries the same value, $`R_\Sigma = 2/R^2`$; the standard Gauss and de Sitter relations lift that curvature to the vacuum-reference $`\Lambda_\text{ref} = 3/R^2`$.

Moved to the matter side, $`\rho_\Lambda = \Lambda c^4 / 8\pi G`$ reads as a vacuum energy density, and the zero-point estimate overshoots observation by roughly 122 orders of magnitude, the cosmological-constant problem. This construction does not derive the observed Λ from that mode sum; it instead treats Λ as global geometric data and returns in §VI to the unresolved radiative-stability question.

Einstein's 1917 setting was a closed $`S^3`$ with Λ as geometry. This construction reclaims that setting, not his matter-Λ equilibrium: it does not use a matter-Λ force balance, and $`R`$ remains open, so the result is the coefficient $`\Lambda R^2 = 3`$, not the observed number.

## II. The geometry

The domain is the minimal closed one. $`S^3`$ is the unique simply connected closed 3-manifold (Poincaré). The postulate embeds a non-orientable carrier in it:

```math
S^1 = \partial(\text{Möbius}) \hookrightarrow S^3, \qquad \partial S^3 = \emptyset.
```

The ambient space is closed and has no boundary. The Möbius band is an embedded spectral carrier, not a boundary of $`S^3`$; its own boundary is the circle $`S^1`$. It is built as the edge-identified quotient of a totally geodesic covering great-$`S^2`$ band in $`S^3`$, and inherits that band's constant-curvature metric. Among non-orientable surfaces with one boundary component (a disk removed from a connected sum of $`k`$ crosscaps) the framework adopts the minimal case, $`k = 1`$, the Möbius band. That minimality is an adopted, natural criterion, not a derived necessity.

The observable spatial quotient is $`S^3/2I`$, the hypersphere modulo the binary icosahedral group ($`\lvert 2I\rvert = 120`$), the largest exceptional finite subgroup of $`\mathrm{SU}(2) \cong S^3`$. The local curvature geometry of §§III-IV lives on the cover $`S^3(R)`$; the quotient enters later only as the large-scale harmonic selection rule.

## III. The spectral seed

The operator is the twisted Laplacian on sections of the orientation line bundle over the curved Möbius carrier. The Möbius holonomy imposes anti-equivariance. In the full curved conic problem the spectral bottom is extension-dependent, zero for the Friedrichs realization (a discontinuous constant-sector mode) and negative for the bridging family, and no self-adjoint extension has a strictly positive bottom. The robust datum is therefore not a ground state but the first positive level, and in the narrow-band class it is stable at

```math
\lambda_+ = \frac{2}{R^2},
```

the $`\ell = 1`$ zonal mode $`\sin(y/R)`$, common to the Friedrichs and bridging extensions for $`\delta_0 > 2R/e`$. The framework takes the narrow band $`W \le \pi R/2`$ as a physical input on the carrier, not a derived fact. The holonomy selects the twisted sector in which the first positive level is identified; the curvature of the covering great-$`S^2`$ band, of which the carrier is the edge-identified quotient, fixes its value. (On a flat strip the same anti-periodic mode returns only $`1/R^2`$; the band's curvature supplies an equal $`1/R^2`$, doubling it to the scalar-curvature value.) The [first-eigenvalue paper](../../framework/files/bedrock/files/first-eigenvalue.md) carries the proof.

The same coefficient appears independently as the ambient Ricci term in the Weitzenböck bound on coexact $`1`$-forms, $`\lambda \ge 2/R^2`$ from $`\mathrm{Ric} = (2/R^2)g`$; the operators and spectral statements are distinct, and that bound is a curvature floor rather than an attained eigenvalue. See the [coexact-gap paper](../../framework/files/bedrock/files/coexact-gap.md).

## IV. The conversion

<img src="https://github.com/dmobius3/mode-identity-theory/blob/main/files/assets/cc-conversion-chain.png?raw=true" width="90%" alt="The conversion chain: the surface seed 2/R², times 3 by the Gauss equation to spatial curvature 6/R², divided by 2 by the vacuum constraint to the vacuum reference 3/R²; identifying it with the observed Λ is open">

The surface seed carries no Λ; the standard general-relativistic chain converts it, in two stages with distinct totally-geodesic conditions.

Stage 1, surface to spatial. For the totally geodesic covering great-$`S^2`$ band $`\Sigma^2 \subset S^3`$ (second fundamental form $`A_{ij} = 0`$), of which the Möbius carrier is the edge-identified quotient, in an isotropic space, the Gauss equation gives

```math
R_\Sigma = \frac{2}{R^2} \Longrightarrow {}^{(3)}R = 3R_\Sigma = \frac{6}{R^2}.
```

Stage 2, spatial to Λ. On the round time-symmetric $`S^3`$ slice of four-dimensional de Sitter ($`S^3 \subset \mathrm{dS}_4`$, extrinsic curvature $`K_{ij} = 0`$, vacuum $`T_{\mu\nu} = 0`$), the vacuum Hamiltonian constraint gives

```math
{}^{(3)}R = 2\Lambda \Longrightarrow \Lambda = \frac{3}{R^2}.
```

The 3 is the isotropic spatial Ricci trace under $`A_{ij} = 0`$ on the great-$`S^2`$ band (derived); the 2 is the de Sitter / vacuum-constraint normalization on the time-symmetric slice (imported from general relativity); their ratio $`3/2`$ is the Gauss-equation interface. The coefficient $`\Lambda R^2 = 3`$ is the standard de Sitter value once a round time-symmetric $`S^3(R)`$ vacuum is assumed; the content here is the spectral origin of the upstream seed, not the coefficient.

Which metric Stage 2 belongs to. The time-symmetric slice it uses is the throat of four-dimensional de Sitter, $`a(t) = \sqrt{3/\Lambda}\cosh(t\sqrt{\Lambda/3})`$: a moment at which $`\dot a = 0`$, not a static state, since $`\ddot a > 0`$ there and the vacuum solution grows away from it. The round closed vacuum cosmology used in that step is not static: with $`\rho = p = 0`$ and $`k = +1`$ the Friedmann equations admit no solution with $`\dot a = \ddot a = 0`$. The framework's spatial domain is static with a fixed radius, so Stage 2 is a vacuum reference normalization of the spectral geometry, the constant general relativity assigns to that curvature in its de Sitter dictionary, rather than the field equation governing the physical domain.

For a static closed domain carrying a homogeneous isotropic perfect fluid, the unchanged Einstein equations give instead

```math
\Lambda R^2 = \frac{\rho + 3p}{\rho + p} = 1 + \frac{2p}{\rho + p} = 3 - \frac{2}{1 + w}, \qquad p = w\rho,
```

A closed static radius requires $`\rho + p > 0`$, since $`1/R^2 = 4\pi G(\rho + p)`$. The middle form above makes the rest exact: given that condition, $`\Lambda R^2 < 3`$ if and only if $`\rho > 0`$, with $`\rho = 0`$ attaining 3 and $`\rho < 0`$ exceeding it. For a positive-density fluid it returns 1 for dust and 3/2 for radiation and approaches 3 only as $`w \to \infty`$, never reaching it. Whether $`\Lambda_\text{ref} = 3/R^2`$ is the physical constant of the static domain therefore depends on the stress tensor its mode content actually carries, which the framework has not determined. The chain is spectrally seeded, geometrically lifted, GR-normalized, and then observationally identified; the last step is the one still open.

<img src="https://github.com/dmobius3/mode-identity-theory/blob/main/files/assets/cc-static-fluid.png?raw=true" width="60%" alt="ΛR² = 3 − 2/(1 + w) for a static closed domain filled with a perfect fluid: dust gives 1, radiation 3/2, and any positive density stays below the de Sitter value 3">

| Step | Status |
|---|---|
| Möbius first positive level $`2/R^2`$ | Companion spectral result |
| Surface-to-spatial factor 3 | Standard Gauss geometry (isotropic covering great-$`S^2`$ band, $`A_{ij} = 0`$) |
| Time-symmetric vacuum relation $`{}^{(3)}R = 2\Lambda`$ | Standard GR input ($`K_{ij} = 0`$, vacuum); a reference normalization, not the static domain's field equation |
| Stress tensor of the static mode content | Open, and gating: it selects the coefficient |
| $`\Lambda R^2 = 3`$ | Standard de Sitter coefficient, with a proposed spectral seed |
| Scale $`R`$ | Open |

## V. The open radius

$`\Lambda_\text{ref} = 3/R^2`$ yields a number only with an independent $`R`$. Reading $`R`$ off $`\Lambda`$ through $`R = \sqrt{3/\Lambda}`$ is circular. Two live routes provide candidate independent estimates of $`R`$, without using $`\Lambda`$, the CMB, or the de Sitter relation: the coupling ($`\alpha`$) route, better conditioned, returns $`\Lambda_\text{ref} = 3/R^2`$ to within about 23%; the particle mass spectrum gives $`R \approx 10.5`$ to 20 Gpc, depending on the assigned pair read, as an order-of-magnitude cross-check. Neither yet closes the prediction. Details in [The R Problem](../../framework/files/working/files/r-problem.md) and [R from the mass spectrum](../../framework/files/working/files/r-from-mass-spectrum.md).

Read back from the observed value, the consistency radius is $`R = \sqrt{3/\Lambda_\text{obs}} \approx 5.38`$ Gpc and $`\Lambda_\text{obs}\ell_P^2 \approx 2.845 \times 10^{-122}`$, on the Planck 2018 TT,TE,EE+lowE+lensing anchor named in the framework's [Inputs and Calibration](../../framework/README.md#inputs-and-calibration); this is a calibration read-back, not an independent determination. The $`S^3/2I`$ quotient also produces a low-shell Molien gap relevant to CMB power, but that structure does not independently determine $`R`$; it is treated in [The R Problem](../../framework/files/working/files/r-problem.md) and the CMB notes.

## VI. Test and scope

Einstein's field equations are unchanged; Λ stays on the geometric side. The direct test of the relation is

```math
\Lambda_\text{obs}R_\text{ind}^2 = 3
```

with $`R_\text{ind}`$ obtained without the Λ-radius relation, stated in advance of the European Space Agency's Euclid Data Release 1. The cosmology-relevant tests read against the spectroscopic BAO and weak-lensing analyses that arrive with the full DR1 in mid 2027; the DR1-Foundation release of November 2026 carries data but no cosmology-derived products, and ESA notes its release dates are tentative. A departure from 3 at $`> 5\sigma`$, with $`R`$ obtained independently, would falsify the coefficient relation. Robust evidence that the dark-energy density evolves with redshift would instead falsify the broader identification of the observed component with a true cosmological constant.

*Note added 2026-09-24; the test as stated above is unchanged.* **As stated, the test cannot yet be scored, and Euclid's data will not score it alone.** The observed Λ is already known to a couple of percent; what the test lacks is an uncertainty on $`R_\text{ind}`$, and no route to $`R`$ yet states one. The better-conditioned route, through the fine-structure constant, gives $`\Lambda_\text{obs}R_\text{ind}^2 \approx 3.9`$, the α formula's 0.4% residual magnified through a sixty-fold lever, and the framework states the formula's accuracy nowhere except as that residual. Read as exact, the formula leaves the loop through α unclosed; read as uncertain by its own residual, the departure is approximately one standard deviation, essentially by construction. Neither reading is adopted. The route also rests on choices besides that accuracy, the energy scale at which α is read among them, so a departure there would indict those choices as much as the coefficient. The test becomes live when a route to $`R`$ brings an error budget of its own and fixes every choice it depends on, on grounds independent of this comparison and frozen before the scoring run: an independent central value is not enough. Until then the α route returns the conditional reference value $`3/R^2`$ about 23% below $`\Lambda_\text{obs}`$, and the coefficient test remains unscored. The accounting is in [The R Problem](../../framework/files/working/files/r-problem.md#the-coefficient-test).

This construction treats Λ as global geometric data rather than deriving it from a zero-point mode sum. That reframes the role assigned to Λ, but it does not by itself establish radiative stability: quantum vacuum stress still contributes to the effective gravitational equations, and whether it can renormalize or disturb the proposed spectral relation remains open.

The gating open problem for the coefficient itself is the stress tensor carried by the static mode content, discussed in §IV. Until that is determined, general relativity does not select among the available coefficients, and the identification of the vacuum reference value $`3/R^2`$ with the physical constant is an assumption rather than a result. The compulsoriness of the Möbius carrier and the dynamical stability of the cosmology are likewise open.

---

The twisted Möbius problem realizes the round curvature scale $`2/R^2`$ as a stable first positive level despite an extension-dependent spectral bottom. Under the standard time-symmetric de Sitter conversion, that seed corresponds to $`\Lambda R^2 = 3`$; determining $`R`$ independently remains open. Einstein's instinct to treat Λ geometrically remains the useful one here.

---

/ **[`↑top`](#top)** / **[`main`](https://github.com/dmobius3/mode-identity-theory/tree/main/)** / **[`framework`](/files/framework/)** / **[`bedrock`](/files/framework/files/bedrock/)** / **[`working`](/files/framework/files/working/)** / **[`cosmos`](/files/cosmos/)** / **[`spectrum`](/files/spectrum/)** / **[`tools`](/files/tools/)** /
