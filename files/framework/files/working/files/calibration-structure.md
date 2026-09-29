<a id="top"></a>
/ **[`main`](https://github.com/dmobius3/mode-identity-theory/tree/main/)** / **[`framework`](/files/framework/)** / **[`bedrock`](/files/framework/files/bedrock/)** / **[`working`](/files/framework/files/working/)** / **[`cosmos`](/files/cosmos/)** / **[`spectrum`](/files/spectrum/)** / **[`tools`](/files/tools/)** /

---

# Calibration Structure (draft for the framework engine)

**Type:** Map
**State:** Active
**Status (2026-09-27):** The calibration architecture, the η / √Ω notation register and the named anchor's rounding and mass-ladder exception are current; the effective scale factor is normalized to a_* (settled 2026-09-02). Route reconciliation for R stays open, tracked in the R problem.
**Summary:** The map of the framework's calibration scheme, one measured anchor per sector with the topology supplying exponents and ratios, plus the notation register and the named anchor in full; a draft for the engine.
**Inputs:** the a0 paper Appendix A.2 (selection rule), the first-positive eigenvalue 2/R², the scaling law

**Notation.** Use $`\sqrt{\Omega}`$ where a quantity dilutes from the observer, since the observer sits at $`\sqrt{\Omega} = R/\ell_P`$: the master law and the mass elevator. Use bare $`\Omega`$ when stating the hierarchy as a quantity (its definition, its value) and for the coupling grid step $`\Omega^{-1/|\mathrm{grid}|}`$, which quantizes the full $`\Omega`$ rather than diluting from the observer. In these framework pages $`\Omega_\Lambda = (R_\Lambda/\ell_P)^2 \approx 10^{122}`$ is the surface hierarchy, the native ledger variable. The cosmological vacuum density fraction $`\rho_\Lambda/\rho_c \approx 0.685`$ is a different quantity, about 122 orders away, and is written $`f_\Lambda`$ when disambiguation is needed. The distance-fit pages state the FLRW background in conventional ΛCDM notation, where that fraction is $`\Omega_\Lambda`$; each says so and identifies its $`\Omega_\Lambda`$ with $`f_\Lambda`$. Where a redshift-dependent dark-energy fraction is written $`\Omega_\text{DE}(z)`$, its $`z = 0`$ value under the fiducial constant-$`\Lambda`$ split is $`f_\Lambda`$; that relation is recorded here and not propagated, since $`\Omega_\text{DE}(z)`$ also carries the pre-registered Euclid flatness prediction.

**$`\eta`$ carries three senses, and the overload is the literature's rather than this corpus's.** The APS eta invariant of index theory holds the large majority of uses (the [bedrock](../../bedrock/) papers, [the-mirror](../../../../spectrum/files/the-mirror.md), the Eta Sign Gate in [mass-spectrum](../../../../spectrum/files/mass-spectrum.md), and the step notes); the photon-to-baryon ratio $`\eta \approx 6 \times 10^{-10}`$ appears in [entropy-as-realization-budget](entropy-as-realization-budget.md); and conformal time appears once, in the imported GR comparison row of [friedmann-as-output](friedmann-as-output.md). Each is the field-standard symbol in its own field, so none is renamed. The rule this register runs on: **use the field-standard symbol locally, and disambiguate only where the senses coexist in one argument, or where a native symbol could be mistaken for an imported one.** That is why $`f_\Lambda`$ needed a corpus-wide symbol, the hierarchy and the density fraction meet inside the scaling law, while $`\eta`$ needs only this map.

**The effective scale factor's normalization is $`a_\ast`$, settled 2026-09-02.** The effective distance relation carries $`a_\text{eff} = a_\ast S`$, and $`a_\ast`$ is the constant that fixes its units. The star is not decoration: $`a_0`$ is the acceleration scale throughout the [SPARC work](sparc-phase-field.md), [cone point coherence](cone-point-coherence.md), the [framework page](../../../README.md) and the distance-fit pages, where it sits in $`L_f = v_c^2/a_0`$ and $`K_g = \pi^2 a_0^2/v_c^4`$, and the two senses meet on any page that states both a background and an acceleration. The rule above then applies directly: disambiguate where the senses coexist in one argument. The [stress-tensor bridge](stress-tensor-bridge.md) and the pages citing its placement previously wrote $`a_0 S`$ for the same constant; they now read $`a_\ast`$, including the $`a_\ast^2`$ coefficients of the pinned flat D+$`\Lambda`$ source. Nothing about the placement or the pinned target changed: the symbol did, and only in the scale-factor sense. Any new page stating the normalization uses $`a_\ast`$.

---

## Calibration Structure

The framework is a calibration scheme, not an oracle that produces every absolute scale without input. One measured reference observable anchors each sector's normalization. What the framework supplies are the sector exponents, grid assignments, well locations, and dimensionless ratios. In other words, the measured anchor fixes the ruler; the topology fixes where the marks on the ruler fall.

This is the same logic used throughout effective physical theory. The Standard Model does not derive the numerical values of the gauge couplings from first principles; it measures them at reference scales and predicts how they run and relate across processes. In the same way, $`H_0`$ is not a failed prediction when it is used as the edge-sector anchor. It plays the role of a measured reference input. The prediction is not the existence of a number called $`H_0`$; the prediction is that the same calibrated edge hierarchy also fixes $`a_0`$, through the ratio of the two wells.

| Sector | Locus | Hierarchy | Anchor | Status |
|---|---|---|---|---|
| Edge $`(n=1)`$ | $`S^1`$ boundary; kinematic locus, no intrinsic eigenvalue | $`\Omega_H = (c/H\ell_P)^2`$ | $`H_0`$ measured | Live |
| Surface $`(n=2)`$ | Möbius strip; carries first positive eigenvalue $`2/R^2`$ | $`\Omega_\Lambda = (R/\ell_P)^2`$ | $`\Lambda`$ measured, fixing $`R`$ (and $`\Omega_\Lambda`$ once the Planck scale is set) | Live as calibration |
| Space $`(n=3)`$ | $`S^3`$ slice; inherits surface eigenvalue | $`\Omega_\Lambda`$ | Via surface sector | Live with surface |
| Mass | 120-wells, McKay distance, torsion | $`\mu_\Lambda`$ and $`(\sqrt{\Omega_\Lambda})^{\mathrm{dist}/30}`$ | $`\Omega_\Lambda`$ from surface; one mass-sector normalization if needed | Live |
| Couplings | Grid wells and fractional hierarchy steps | $`\Omega_\Lambda^{-1/60}`$, $`\Omega_\Lambda^{-1/120}`$ | $`\Omega_\Lambda`$ from surface | Live |

The prediction/calibration split is sector-by-sector. In the edge sector, the measured value of $`H_0`$ calibrates the edge hierarchy. If the two rows carry one weight, which the [scaling law's audit](scaling-law-uniqueness.md#audit-uniformity-by-observable) records as assumed, the acceleration scale then follows from the ratio of wells:

```math
\frac{a_0}{cH_0}=\frac{C(13/120)}{C(34/120)}.
```

Thus $`H_0`$ is the anchor, while $`a_0/H_0`$ is the prediction.

In the surface sector, the eigenvalue statement remains intact. The first positive eigenvalue is

```math
\frac{2}{R^2},
```

with the ground state the extension-dependent zero mode (Friedrichs zero gives the $`m_h = 0`$ background).

What failed was the independent over-determination of $`R`$ through the CMB-Molien path. Without an independent value of $`R`$, that path no longer predicts the physical $`\Lambda`$ absolutely; two other routes determine $`R`$ independently and return $`\Lambda_\text{ref}`$ as a conditional output (below). Instead, measured $`\Lambda`$ calibrates the surface radius $`R`$ by substitution into the reference relation $`\Lambda_\text{ref} = 3/R^2`$, which is the identification the Interface holds open, imported here as a calibration choice, and hence the surface hierarchy

```math
\Omega_\Lambda = (R/\ell_P)^2
```

once the Planck scale is fixed by the second dial.

The eigenvalue structure survives; the absolute surface radius is the open piece. Two paths return $`\Lambda_\text{ref}`$ to a prediction. The first anchors on measured $`\alpha`$: it fixes $`\Omega_\Lambda`$ directly, needs no independent $`R`$, and returns $`\Lambda_\text{ref}\ell_P^2`$ to within 23%. The second is the mass-spectrum route, where two masses at different McKay distances overdetermine $`R`$ but currently land $`\Lambda_\text{ref}`$ about 13.4x low. The coupling route is the tighter of the two; the gap between them is an open consistency item. See the two-dial reading below.

More fully, the scaling law has one hierarchy variable $`\Omega_\Lambda`$ with three independent readings of it. Inverting any one fixes $`\Omega_\Lambda`$ and predicts the rest; which one you invert is calibration, the relationships between them are physics:

| Anchor | Reads $`\Omega_\Lambda`$ from | $`\Lambda_\text{ref}`$ | $`\alpha`$ | Role |
|---|---|---|---|---|
| Measured $`\Lambda`$ (sets $`R`$) | the radius $`R`$ | circular | 0.4% | current default |
| Measured $`\alpha`$ | the coupling | 23% (genuine) | circular | best-conditioned |
| Mass spectrum ($`m_\mu/m_e`$) | the mass ratio | ~13.4x (genuine) | ~few % | independent cross-check |

The three readings are one inversion through the same 60-fold lever, and they differ in input conditioning ($`\alpha`$ to ~0.4%, the mass ratio to ~4.5%). The two non-circular routes do not presently agree: the canonical electron-muon reading sits 10.5x from the coupling route in $`\Lambda_\text{ref}`$. Against the measured value that same reading lands about 13.4x low. The lever amplifies small input residuals, but that amplification does not by itself explain the disagreement, and the present machinery does not distinguish conditioning from structural inconsistency. Reconciling the routes is open; see [the R problem](r-problem.md).

This localizes the blast radius. Losing the independent CMB-Molien anchor demotes exactly one claim: $`\Lambda`$ is no longer an absolute prediction. It becomes the measured surface-sector calibration input. Downstream mass and coupling calculations do not collapse, because they require the value of $`\Omega_\Lambda`$, which is fixed once $`R`$ (from measured $`\Lambda`$) and the Planck scale (the second dial) are specified. The McKay mass elevator uses powers of $`\sqrt{\Omega_\Lambda}`$; the gauge couplings use fractional powers of $`\Omega_\Lambda`$ such as $`\Omega_\Lambda^{-1/60}`$. They do not require $`R`$ to be independently predicted, only consistently calibrated.

The edge sector is untouched by this correction. It references $`\Omega_H`$, not $`\Omega_\Lambda`$, and is anchored by $`H_0`$. The surface and space sectors reference $`\Omega_\Lambda`$, now set through measured $`\Lambda`$ (which fixes $`R`$) and the Planck scale. The mass and coupling sectors inherit that calibrated hierarchy. Thus the correction does not propagate as a global failure; it changes the status of one surface-sector claim from prediction to calibration.

This also clarifies the role of measured inputs. The framework predicts structural relations: the integer floors $`n=1,2,3`$, the McKay exponents, the grid fractions, the well assignments, and the dimensionless ratios between observables at the same depth, where the hierarchy factor cancels. It does not claim that every absolute normalization is derived without empirical reference. A measured anchor per sector is part of the calibration architecture. $`\mu_\Lambda = \rho_\Lambda^{1/4}`$ is the vacuum floor inherited from the calibrated surface sector; $`m_e`$ is a mass-sector normalization/benchmark, not a second vacuum floor.

The status is therefore honest. The selection rules and well assignments were fixed before this calibration reinterpretation, so the downstream agreements are not produced by retuning them after the fact. But the selection rule itself remains a postulate of the framework, not yet a theorem derived from the topology alone. A first-principles derivation from the Hurwitz/Fibonacci structure of the 120-domain remains open.

---

## The named anchor

The [engine](../../../README.md#inputs-and-calibration) names the $`\Lambda`$-anchored default: Planck 2018 base-ΛCDM, TT,TE,EE+lowE+lensing, $`H_0 = 67.36`$ km s⁻¹ Mpc⁻¹ and $`f_\Lambda = 0.6847`$, giving $`\Lambda\,\ell_P^2 = 2.845 \times 10^{-122}`$, $`\Omega_\Lambda = 1.054 \times 10^{122}`$ and $`R_\Lambda = 5.38`$ Gpc.

Working prose rounds that row to $`H_0 = 67.4`$ and $`0.685`$, which returns the same $`2.85 \times 10^{-122}`$ to three figures. That agreement is specific to $`\Lambda`$, which rounds to $`2.85`$ from either pair. $`R_\Lambda`$ does not: the two straddle a boundary at 5.375 Gpc (5.3787 named against 5.3740 working), so a radius derived from the rounded pair would print 5.37. The corpus quotes $`R_\Lambda = 5.38`$ Gpc, from the named row.

The one documented exception to deriving absolutes from the named row is the published mass ladder: its pinned inputs, $`\mu_\Lambda = 2.25`$ meV and $`\sqrt{\Omega_\Lambda} = 1.019 \times 10^{61}`$, encode the Planck 2018 +BAO row rather than the named row, which would print about $`2.24`$ meV and $`1.027 \times 10^{61}`$. Those two are mutually derivable and pinned to the table they generated, so retargeting either alone corrupts that table rather than updating it; the split is recorded in the [mass spectrum's calibration note](../../../../spectrum/files/mass-spectrum.md) and enforced by its regression guard.

---

## Proposed Inputs table patch

Replaces the current "Measured scales" table in the engine.

| Input | Role | Status |
|---|---|---|
| $`H_0`$ | Edge-sector anchor; fixes $`\Omega_H`$ | Measured calibration |
| $`\Lambda`$ | Surface-sector anchor; fixes $`R`$ through $`\Lambda_\text{ref} = 3/R^2`$ | Measured calibration |
| $`\alpha`$ | Alternative surface anchor; measured $`\alpha`$ fixes $`\Omega_\Lambda`$ directly | Measured (dimensionless); returns $`\Lambda_\text{ref}\ell_P^2`$ as a prediction to 23% |
| $`R`$ | Surface radius in the first positive eigenvalue $`2/R^2`$ and $`\Omega_\Lambda=(R/\ell_P)^2`$ | Calibrated from $`\Lambda`$ today; measured $`\alpha`$ pins $`\Omega_\Lambda`$ (hence $`R`$) to 23%, and the mass-spectrum route (two masses at different distances) is a further, looser path to an independent $`R`$ |
| $`m_e`$ or one measured mass | Mass-sector normalization / second dial for the mass-gravity system | Measured calibration or benchmark |

---

## Mass/gravity reading: the two dials (draft for the-waltz.md §II)

The mass-and-gravity sector is one closed system. The topology fixes the dimensionless ratios between observables at the same depth; two dimensionful dials, $`R`$ (calibrated from measured $`\Lambda`$ through the reference relation) and $`G`$, set the absolute scales. Ratios across depths carry $`R`$, which is what lets the spectrum read $`R`$ back. The mass-spectrum reading and the gravity-constant reading are the same system read from different dials, not competing claims.

| Anchors used | Solves for | Reading |
|---|---|---|
| $`\Lambda`$ and $`G`$ | Absolute fermion masses | Mass-spectrum reading |
| $`\Lambda`$ and one measured mass | $`G`$ and the remaining masses | Gravity-constant reading |
| Two masses at different McKay distances | $`R`$, hence $`\Lambda_\text{ref}`$ as a prediction, and $`G`$ | R-from-spectrum reading (open; needs the $`(\rho,\sigma)\to(T_3,Y)`$ rule) |
| Measured $`\alpha`$ (dimensionless) | $`\Omega_\Lambda`$, hence $`\Lambda_\text{ref}\ell_P^2`$ as a prediction | $`\alpha`$ route; $`\Lambda_\text{ref}\ell_P^2 \propto \alpha^{60}`$, within 23% (the 60-fold lever) |
| Same-distance or same-exponent ratios | $`m_i/m_j`$ at fixed distance; $`\alpha_s/\alpha_W`$ | Anchor-free structural core |

The anchor-free core is narrower than "all ratios." A mass ratio drops the overall floor $`\mu_\Lambda`$, which cancels in any ratio, but it keeps the McKay elevator $`(\sqrt{\Omega_\Lambda})^{\mathrm{dist}/30}`$ unless both particles sit at the same distance. Across distances the elevator survives, so the ratio carries $`(R/\ell_P)^{\Delta\mathrm{dist}/30}`$, and the mass hierarchy itself is that surviving factor. The same holds in the coupling sector: $`\alpha_s/\alpha_W`$ is anchor-free because both forces share the confinement grid, while $`\alpha_s/\alpha_{EM}`$ carries $`R`$ because the grids differ. So the genuinely anchor-free predictions are the same-depth ratios, and the cross-depth ratios are the lever for reading $`R`$.

Key phrase: **same two-dial system, different readout.**

---

/ **[`↑top`](#top)** / **[`main`](https://github.com/dmobius3/mode-identity-theory/tree/main/)** / **[`framework`](/files/framework/)** / **[`bedrock`](/files/framework/files/bedrock/)** / **[`working`](/files/framework/files/working/)** / **[`cosmos`](/files/cosmos/)** / **[`spectrum`](/files/spectrum/)** / **[`tools`](/files/tools/)** /
