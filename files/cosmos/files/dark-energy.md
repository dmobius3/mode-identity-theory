<a id="top"></a>
/ **[`main`](https://github.com/dmobius3/mode-identity-theory/tree/main/)** / **[`framework`](/files/framework/)** / **[`bedrock`](/files/framework/files/bedrock/)** / **[`working`](/files/framework/files/working/)** / **[`cosmos`](/files/cosmos/)** / **[`spectrum`](/files/spectrum/)** / **[`tools`](/files/tools/)** /

---

# 👻 Dark Energy

<img src="https://github.com/dmobius3/mode-identity-theory/blob/main/files/assets/The_Phantom_in_the_Machine.jpg?raw=true" width="100%" alt="The Phantom in the Machine: decoding dark energy's apparent evolution as observer phase-shift on a static three-sphere">

DESI DR2 reports a 2.8–4.2σ preference for dynamical dark energy, with CPL fits favoring an apparent crossing of $`w = -1`$. We show that a non-phantom distance-redshift relation can produce such crossings when analyzed with two-parameter templates (CPL, BA, JBP), and that Mode Identity Theory provides that relation from a static geometric foundation.

The cosmos is a finite, static three-sphere $`S^3`$. The standing wave $`\Psi = \cos(t/2)`$ on the temporal edge, with the Waltz clock $`dt/d\tau = S^{-1/2}`$, gives the effective distance-redshift relation

```math
\frac{H^2(z)}{H_0^2} = \frac{1-\Omega_\Lambda}{1-s_0^2}(1+z)^3 - \frac{(1-\Omega_\Lambda)s_0^2}{1-s_0^2}(1+z) + \Omega_\Lambda,
```

where $`\Omega_\Lambda = 0.685`$ is held fixed as the fiducial vacuum-fraction anchor, matching the ΛCDM/Planck-scale normalization rather than derived from topology here, and $`s_0 = \sin(t_{\text{now}}/2)`$ is the single phase parameter. Here $`\Omega_\Lambda`$ is the vacuum density fraction $`f_\Lambda \approx 0.685`$ in the conventional ΛCDM sense, distinct from the MIT hierarchy $`\Omega_\Lambda = (R_\Lambda/\ell_P)^2`$ used in the scaling-law and mass pages. Under the fixed fiducial-matter split, the diagnostic effective equation of state satisfies $`w_{\text{eff}}(z) > -1`$ for all $`z`$. The stronger, decomposition-independent statement is that the underlying $`H(z)`$ is fixed and introduces no independent phantom fluid; whether the residual reads as phantom depends on what is subtracted as matter (§III).

Fitting CPL, BA, and JBP templates to MIT noise-free distances produces apparent phantom crossings from this non-phantom relation, showing that these three commonly-used two-parameter templates can manufacture the artifact. At data-allowed $`s_0`$ the induced CPL distortion is about a tenth of DESI's reported amplitude and opposite in sign for $`w_a`$ (+0.29 vs −0.86): this establishes the mechanism, not that DESI's signal is primarily template bias. Joint MCMC fits to Pantheon+ (1701 SNe) and DESI DR2 BAO (13 data points) yield $`\Delta\chi^2 = +0.11`$ relative to flat ΛCDM at the same parameter count, with $`s_0 < 0.19`$ (95% CL). The model predicts a negative $`(1+z)^1`$ term in $`H^2(z)`$, a distinctive signature absent from the four canonical FLRW components; whether next-generation BAO surveys can detect it depends on the phase $`s_0`$, and Euclid's DR1 BAO is marginal for it (§VI).

**Pantheon+ & DESI DR2 BAO**

| Quantity | Value |
|---|---|
| $`\Delta\chi^2`$ vs ΛCDM (SN+BAO) | +0.11 (same $`k`$) |
| Phase parameter | $`s_0 < 0.19`$ (95% CL) |
| Phantom crossing | none in $`H(z)`$; $`w_\text{eff}(z) > -1`$ at all $`z`$ under the fiducial split (proven) |
| Distinctive signature | Negative $`(1+z)^1`$ term in $`H^2(z)`$ |

## I. The Observational Landscape

The DESI DR2 results present the most precise baryon acoustic oscillation measurements to date, drawing from over 14 million galaxies and quasars across 11 billion years of cosmic history. When combined with CMB data and supernova compilations, the results indicate that dark energy's equation of state $`w`$ may not equal -1 as assumed in ΛCDM.

The emerging picture: present value $`w_0 \approx -0.85`$ to -0.70 (less negative than $`\Lambda`$), past behavior $`w < -1`$ at higher redshifts (phantom-like), and a "phantom crossing" through $`w = -1`$ near $`z \approx 0.5`$. Single-field models face fundamental difficulties crossing $`w = -1`$; proposed solutions require exotic field content. Cortês and Liddle flag the crossing location at the center of the observable window as a "substantial and unsettling coincidence." The DESI extended analysis reports consistent phantom-crossing behavior across five additional parameterizations (BA, JBP, exponential, logarithmic, and model-free binned).

The possibility that apparent phantom crossings can arise from parameterization choice has been recognized. Linder and Huterer demonstrated that the CPL form introduces systematic bias when the true $`w(z)`$ lies outside its functional family. Shafieloo, Sahni, and Starobinsky showed that model-dependent reconstruction can produce spurious features, including phantom crossings, when applied to models outside the fitting basis.

MIT sharpens this question. The Möbius spectral problem has first positive eigenvalue $`2/R^2`$ under its stated geometric conditions. MIT reads this as $`\Lambda_\text{top}`$; the Gauss equation lifts it to $`6/R^2`$, and the imported de Sitter vacuum relation normalizes that to the reference $`\Lambda_\text{ref} = 3/R^2`$. The logarithmic slope $`d\ln C/d\Theta`$ vanishes exactly at the antinode, so $`\Lambda`$ is stationary to first order in the phase position. It is not invariant: the same one-step displacement that moves $`H_0`$ by 8.4% moves $`\Lambda`$ by $`-0.27\%`$, about thirty times less. That differential, not exact protection, is what makes the fixed-$`\Lambda`$ reading hold at the precision this paper works to. What varies is the observer's phase position on the standing wave. The question this paper answers: does a static $`\Lambda`$ viewed from a moving phase produce distances that standard templates misread as dynamical dark energy?

## II. The Phase-Clock Distance-Redshift Relation

### The Static Baseline

The cosmos is a finite, static three-sphere; what the data sees is a flat-FLRW cosmology, the spatial curvature a static boundary condition rather than a Friedmann term, so the apparent $`\Omega_K`$ is zero. Its curvature radius enters as the de Sitter scale $`R_\Lambda = \sqrt{3/\Lambda} \approx 5.38`$ Gpc, read back from the observed $`\Lambda`$ and so circular as a derivation. Two routes reach $`R`$ independently of that circle: the coupling ($`\alpha`$) route lands near 6.1 Gpc, and the particle mass spectrum gives an order-of-magnitude reading near 20 Gpc, roughly three times the coupling-route radius. Closing that gap is the open [R problem](../../framework/files/working/files/r-problem.md). The Möbius surface forces the wave to flip sign halfway around, giving the standing wave $`\Psi = \cos(t/2)`$ with a full phase period of $`4\pi`$ (a duration in Gyr requires the still-open phase-to-clock map). The quantity $`S = \sin(t/2)`$ is the realization amplitude of the model, the bounded fraction of the wave expressed as resolvable modes at phase $`t`$; turning it into a matter density or $`T_{\mu\nu}`$ is an open step. It starts at 0 and grows to 1.

Redshift is a ratio of phase positions:

```math
1 + z = \frac{s_0}{S}, \qquad s_0 = \sin(t_\text{now}/2)
```

This introduces exactly one new degree of freedom: the observer's current phase $`s_0 \in (0, 1)`$. The fiducial flat ΛCDM limit is recovered as $`s_0 \to 0`$, where $`S/s_0`$ reduces to a conventional scale factor. The mechanism behind the ratio, the phase sampling and its thermal corollary cooling, is laid out in [Redshift and Cooling](../../framework/files/working/files/redshift-and-cooling.md); this section is the distance relation it feeds.

### The Waltz Clock

Phase time $`t`$ and proper time $`\tau`$ are related by a clock rate. From $`S = \sin(t/2)`$:

```math
\frac{1}{S}\frac{dS}{d\tau} = \frac{\cos(t/2)}{2\sin(t/2)} \cdot \frac{dt}{d\tau}
```

For a power-law clock $`dt/d\tau = S^n`$, the requirement that the non-vacuum sector reproduce the observed matter-era scaling $`H^2 \propto (1+z)^3`$ at high redshift selects $`n = -1/2`$:

```math
\frac{dt}{d\tau} = S^{-1/2}
```

This is the Waltz clock. At early times $`S \ll 1`$, the clock $`dt/d\tau \propto S^{-1/2}`$ makes $`H \propto S^{-3/2} \propto (1+z)^{3/2}`$, which squares to the familiar matter-density scaling. The exponent is a 3/2, the ratio of matter dilution to the Friedmann square root; identifying that with the face/edge stabilizer ratio of the icosahedral group native to $`S^3`$ ($`|2I| = 120`$) is a conjectured correspondence, not derived. Integer alternatives ($`n = 0, -1, +1`$) produce $`(1+z)^1`$, $`(1+z)^2`$, and $`(1+z)^0`$ scalings respectively; all three are ruled out at $`\Delta\chi^2 > 60`$ against Pantheon+ (Appendix A of the companion analysis).

### The Hubble Rate

With the Waltz clock, the exact non-vacuum kernel is:

```math
K(z;\, s_0) = \frac{(1+z)^3 - s_0^2\,(1+z)}{1 - s_0^2}
```

normalized so $`K(0;\, s_0) = 1`$. The cosmological constant, a vacuum energy density independent of the phase evolution, enters as a separate additive component:

```math
\frac{H^2(z)}{H_0^2} = (1 - \Omega_\Lambda)\,K(z;\, s_0) + \Omega_\Lambda
```

with $`\Omega_\Lambda = 0.685`$ held fixed as the fiducial vacuum-fraction anchor. The topology supplies the seed $`\lambda_1 = 2/R^2`$, lifted by the Gauss equation and normalized by the imported de Sitter vacuum relation to the reference $`\Lambda_\text{ref} = 3/R^2`$ (net $`\times 3/2`$: the 3 derived, the $`\tfrac{1}{2}`$ imported), which is dimensionful; the dimensionless fraction $`\Omega_\Lambda = \Lambda c^2/(3H_0^2) \approx 0.685`$ matches the fiducial ΛCDM/Planck-scale normalization and is not derived independently from the topology in this paper. Expanding:

```math
\frac{H^2(z)}{H_0^2} = \frac{1 - \Omega_\Lambda}{1 - s_0^2}(1+z)^3 - \frac{(1 - \Omega_\Lambda)\,s_0^2}{1 - s_0^2}(1+z) + \Omega_\Lambda
```

Defining $`\alpha \equiv (1-\Omega_\Lambda)/(1-s_0^2)`$ and $`\beta \equiv (1-\Omega_\Lambda)\,s_0^2/(1-s_0^2)`$, the expression reads $`H^2/H_0^2 = \alpha(1+z)^3 - \beta(1+z) + \Omega_\Lambda`$, with $`\alpha - \beta + \Omega_\Lambda = 1`$ enforcing $`E(0) = 1`$.

With $`\Omega_\Lambda = 0.685`$ held as the fiducial vacuum-fraction anchor, flat closure gives the matter fraction $`\Omega_m = 1 - \Omega_\Lambda = 0.315`$. The $`(1+z)^3`$ coefficient $`\alpha = \Omega_m/(1 - s_0^2)`$ is a dressed version; at any $`s_0`$, $`\alpha(1 - s_0^2) = \Omega_m = 0.315`$.

### The $`(1+z)^1`$ Term

The negative $`(1+z)^1`$ term is absent from the four canonical FLRW density components:

| Component | Redshift scaling |
|---|---|
| Radiation | $`(1+z)^4`$ |
| Matter | $`(1+z)^3`$ |
| Curvature | $`(1+z)^2`$ |
| Cosmological constant | $`(1+z)^0`$ |
| Phase-clock correction | $`(1+z)^1`$ |

Its coefficient $`-\beta = -(1-\Omega_\Lambda)\,s_0^2/(1-s_0^2)`$ is strictly negative for $`s_0 > 0`$ and vanishes in the ΛCDM limit. This term is the fingerprint of the bounded phase parameterization: the $`\sqrt{1 - S^2}`$ factor in the non-vacuum kernel equals unity at high $`z`$ and generates the correction at low $`z`$. It is the paper's primary falsifiable prediction.

## III. $`w_\text{eff}(z) > -1`$ at All Redshifts (Fiducial Split)

To define a diagnostic effective dark energy equation of state, we adopt the fiducial-matter split: deviations from the fiducial matter scaling are assigned to the effective dark-energy sector, using $`\Omega_m = 1 - \Omega_\Lambda = 0.315`$ (the fiducial matter fraction, independent of $`s_0`$).

The effective dark energy density is:

```math
X(z) = E^2(z) - \Omega_m(1+z)^3 = \frac{\Omega_m\,s_0^2}{1 - s_0^2}\bigl[(1+z)^3 - (1+z)\bigr] + \Omega_\Lambda
```

For an effective fluid with density $`X(z)`$ obeying $`d\rho/dz = 3\rho(1+w)/(1+z)`$, the equation of state is:

```math
w_\text{eff}(z) = -1 + \frac{(1+z)}{3X}\frac{dX}{dz}
```

Computing the derivative:

```math
\frac{dX}{dz} = \frac{\Omega_m\,s_0^2}{1 - s_0^2}\bigl[3(1+z)^2 - 1\bigr]
```

The correction to $`w = -1`$ is therefore:

```math
w_\text{eff}(z) + 1 = \frac{\Omega_m\,s_0^2\,(1+z)\bigl[3(1+z)^2 - 1\bigr]}{3(1 - s_0^2)\bigl[\frac{\Omega_m\,s_0^2}{1 - s_0^2}\bigl((1+z)^3 - (1+z)\bigr) + \Omega_\Lambda\bigr]}
```

For $`z \geq 0`$ and $`s_0 \in (0, 1)`$:

- **Numerator:** $`3(1+z)^2 - 1 \geq 2`$ (equality at $`z = 0`$). Strictly positive.
- **Denominator:** $`(1+z)^3 - (1+z) = (1+z)(z)(2+z) \geq 0`$ for $`z \geq 0`$, and the additive $`\Omega_\Lambda > 0`$ ensures $`X(z)`$ is strictly positive at every $`z`$. The denominator is strictly positive at every redshift.

Therefore:

```math
w_\text{eff}(z) > -1
```

for the fiducial-matter diagnostic split, for all $`z \geq 0`$, $`s_0 \in (0, 1)`$.

At $`s_0 = 0`$, $`w_\text{eff} = -1`$ everywhere (the fiducial flat ΛCDM limit). For $`s_0 > 0`$, the correction is positive and begins at order $`s_0^2`$.

Whether you see phantom behavior depends on what you subtract as "matter." The dressed split (subtracting $`\alpha(1+z)^3`$) assigns the correction to the matter sector and yields $`w_\text{eff} < -1`$ at high $`z`$. Both are valid decompositions of the same distance-redshift relation; neither changes the physical distances or the Hubble rate. This paper adopts the fiducial split because it holds the matter fraction fixed as $`s_0`$ varies, making the diagnostic equation of state a function of the single new parameter alone. The convention-dependence is itself part of the template bias finding: the same $`H(z)`$ is diagnosed as phantom or non-phantom depending on the subtraction.

## IV. Template Bias Demonstration

### Method

To test whether standard $`w(z)`$ parameterizations produce apparent phantom crossings from phase-clock distances, we generate noise-free BAO observables (comoving distance $`D_M`$, Hubble distance $`D_H`$, and volume-averaged distance $`D_V`$, all scaled by the sound horizon $`r_d`$) from the MIT $`H(z)`$ at the seven DESI DR2 effective redshifts ($`z = 0.295, 0.510, 0.706, 0.934, 1.321, 1.484, 2.330`$), using $`H_0 = 67.4`$ km/s/Mpc and $`r_d = 147.1`$ Mpc. We then fit four $`w(z)`$ parameterizations to these mock observables using the published DESI covariance structure, with $`\Omega_m = 0.315`$ held fixed to isolate the effect of the $`w(z)`$ parameterization.

The four parameterizations are CPL, Barboza-Alcaniz (BA), Jassal-Bagla-Padmanabhan (JBP), and a three-parameter polynomial in $`(1-a)`$. Each is a standard fitting form used in the DESI extended analysis. The mock exercise uses $`s_0 = 0.389`$ to maximize visibility of the effect; this is the Pantheon+-only value, above the joint SN+BAO constraint $`s_0 < 0.19`$ (§V), so the figure shows a distortion roughly twice what current data permit. The threshold scan below tracks the effect down into the data-allowed range, where it shrinks. The template bias mechanism operates at any $`s_0 > 0`$.

### Results

Three of four parameterizations produce phantom crossings from input that satisfies $`w > -1`$ everywhere (Section III):

| Parameterization | Best-fit parameters | $`\chi^2`$ | Crosses $`w = -1`$? |
|---|---|---|---|
| CPL: $`w_0 + w_a(1-a)`$ | $`w_0 = -1.045`$, $`w_a = 0.925`$ | 1.31 | Yes |
| BA: $`w_0 + w_a\frac{a(1-a)}{a^2-2a+2}`$ | $`w_0 = -1.200`$, $`w_a = 2.654`$ | 11.48 | Yes |
| JBP: $`w_0 + w_a\,a(1-a)`$ | $`w_0 = -1.167`$, $`w_a = 2.197`$ | 7.21 | Yes |
| Polynomial (3-param) | $`w_0 = -0.918`$, $`w_1 = -0.213`$, $`w_2 = 1.739`$ | 0.004 | No |

<img src="https://img1.wsimg.com/isteam/ip/21cc2ac0-6dc4-4b19-93ef-6a7079ac9d3c/Screenshot%202026-06-24%20at%208.25.31%E2%80%AFPM.png/:/rs=w:2560,h:1648" width="100%" alt="Dark-energy equation of state w(z): the framework Lambda-cos curve stays above the phantom divide w = -1 at all z, while the CPL, BA, and JBP two-parameter templates dip below -1 near z = 0 and diverge at high z, and the three-parameter polynomial tracks the framework without crossing.">

*The diagnostic $`w(z)`$ from a non-phantom truth. The framework's exact relation (Λcos, solid) stays above the phantom divide $`w = -1`$ at every redshift, while the two-parameter CPL, BA, and JBP templates fit to the same distances dip below $`-1`$ near $`z = 0`$ and diverge at high $`z`$. Only the three-parameter polynomial tracks the truth without a spurious crossing.*

The polynomial, with one additional free parameter, fits the phase-clock distances to $`\chi^2 \approx 0`$ and does not produce a phantom crossing. The apparent crossing in the two-parameter forms is purely a basis-restriction artifact: the effect arises from projecting the curvature of the MIT distance-redshift relation onto a restricted two-parameter basis, absorbing the residual into phantom-crossing parameter values.

CPL carries the sharp form of the argument: it fits well ($`\chi^2 = 1.31`$) yet still produces a crossing, so a good-fitting template manufactures the artifact. BA and JBP have $`5.5\times`$ to $`8.8\times`$ larger $`\chi^2`$ ($`11.5`$ and $`7.2`$ against CPL's $`1.31`$), so part of their crossing may instead reflect a form that does not capture the underlying shape at all, a weaker point.

### Threshold Scan

To determine the amplitude of the template bias at data-allowed values of $`s_0`$, we repeat the CPL fit across $`s_0 \in [0.01, 0.40]`$:

| $`s_0`$ | $`w_0`$ | $`w_a`$ | $`w_0`$ deviation from -1 |
|---|---|---|---|
| 0.01 | -1.00007 | +0.001 | $`7 \times 10^{-5}`$ |
| 0.06 | -1.003 | +0.030 | 0.003 |
| 0.18 | -1.022 | +0.261 | 0.022 |
| 0.39 | -1.044 | +0.928 | 0.044 |
| DESI DR2 (BAO+CMB+SN) | -0.75 | -0.86 | 0.25 |

The crossing occurs at every sampled value in $`s_0 \in [0.01, 0.40]`$. At the largest $`s_0`$ still allowed by data, the template-induced crossing is real but tiny: about a tenth of what DESI reports.

### Comparison with the DESI Best Fit

The DESI DR2 CPL best fit for the BAO+CMB+SN combination reports $`w_0 \approx -0.75`$ and $`w_a \approx -0.86`$. The phase-clock-induced distortion at data-allowed $`s_0`$ differs in both amplitude ($`|w_0 + 1| = 0.02`$ vs 0.25, a factor of ~10) and sign ($`w_a = +0.29`$ vs -0.86).

The template bias mechanism is demonstrated for these three templates: a non-phantom $`H(z)`$ produces apparent phantom crossings under CPL, BA, and JBP. The phase-clock model at its current constraint does not reproduce the DESI best-fit parameters quantitatively. Bridging the amplitude gap would require either a larger bounded deformation ($`s_0 \gtrsim 0.4`$, ruled out by current data) or a different functional form for the effective dark-energy sector.

## V. Observational Constraints

### Data

Joint fits use the Pantheon+ supernova compilation (1701 SNe Ia with full statistical and systematic covariance) and DESI DR2 BAO measurements (1 isotropic $`D_V/r_d`$ at $`z = 0.295`$ and 6 anisotropic $`D_M/r_d`$, $`D_H/r_d`$ pairs at $`z = 0.51`$–2.33, with published cross-correlations). The total dataset comprises 1714 observables.

### Primary Fit: SN+BAO

MCMC sampling uses an affine-invariant ensemble sampler (32 walkers, 5000 steps, 1000 burn-in). Flat ΛCDM free parameters: $`\Omega_m`$, $`H_0 r_d`$, $`M_B`$ (the standardised peak brightness of Type Ia supernovae). MIT free parameters: $`s_0`$, $`H_0 r_d`$, $`M_B`$. Both models have three free parameters, with $`\Omega_\Lambda = 0.685`$ fixed in the MIT case.

| | Flat ΛCDM | MIT |
|---|---|---|
| Primary parameter (posterior median) | $`\Omega_m = 0.312`$ [0.304, 0.321] | $`s_0 = 0.076`$ [0.023, 0.143] |
| $`H_0 r_d`$ (km/s) | 10043 [9977, 10111] | 10008 [9972, 10040] |
| $`M_B`$ | -19.355 [-19.360, -19.350] | -19.353 [-19.357, -19.350] |
| $`\chi^2_\text{min}`$ | 1772.5 | 1772.6 |
| $`\chi^2_\text{SN}`$ / $`\chi^2_\text{BAO}`$ | 1759.9 / 12.6 | 1759.0 / 13.5 |

The phase-clock best-fit sits at $`s_0 = 0.001`$ (the numerical prior floor; the analytic ΛCDM limit is $`s_0 = 0`$). The 95th percentile gives:

```math
s_0 < 0.19 \quad (95\%\ \text{CL, flat prior})
```

$`\Delta\chi^2 = +0.11`$ at equal parameter count: no preference for either model. The two distance-redshift relations are indistinguishable at current precision.

### Robustness

**Prior sensitivity.** The 95% upper limit ranges from 0.12 (log-flat prior) to 0.21 (flat in $`s_0^2`$). The constraint is prior-sensitive in detail but data-driven in character: all priors yield $`s_0 \ll 1`$.

**$`\Omega_\Lambda`$ sensitivity.** The qualitative fit conclusion, no preference over ΛCDM, is stable across $`\Omega_\Lambda = 0.68`$–0.715, with the best $`\Delta\chi^2`$ near $`\Omega_\Lambda = 0.69`$. The inferred $`s_0`$, however, is materially correlated with the fixed vacuum anchor: at the CMB-preferred $`\Omega_\Lambda = 0.715`$ the preferred deformation shifts to $`s_0 \simeq 0.288`$ and the model is mildly disfavored ($`\Delta\chi^2 = +2.38`$). The scan shows smooth dependence on $`\Omega_\Lambda`$, not independence.

**CMB distance priors.** Adding compressed Planck 2018 distance priors (summary constraints on the distance to the CMB, not the full Planck likelihood) and freeing $`\Omega_\Lambda`$ gives a four-parameter fit indistinguishable from non-flat ΛCDM ($`\Delta\chi^2 = +0.28`$ at equal parameter count).

**Low-redshift supernovae.** The Pantheon+ compilation used here contains 111 light curves at $`z < 0.01`$, a range commonly excluded in supernova cosmology analyses because peculiar-velocity systematics dominate. Applying the same $`z > 0.01`$ cut leaves the result unchanged in character: with 1590 SNe the best fit remains at the ΛCDM limit ($`s_0 = 0.001`$), and compared on the same profile-likelihood estimator the cut tightens the 95% upper limit from $`s_0 < 0.177`$ to $`s_0 < 0.149`$. The very-low-redshift subset was therefore not driving the deformation. The model remains statistically indistinguishable from ΛCDM under the cut ($`\Delta\chi^2 = +1.34`$ at equal parameter count against flat ΛCDM, within the fixed-$`\Omega_\Lambda`$ sensitivity reported above), and a harsher $`z > 0.1`$ stress cut (960 SNe) gives the same picture ($`\Delta\chi^2 = +1.90`$, best fit again at the ΛCDM limit).

**Growth of structure.** Under the standard GR linear-growth equation with the modified background $`H(z)`$ (Einstein equations unchanged; no phase-clock-derived perturbation theory yet), the model is consistent with current growth data: fitting DESI DR1 ShapeFit+BAO ($`f\sigma_8`$ at six tracer effective redshifts) gives $`\Delta\chi^2_\text{RSD} < 0.3`$ relative to flat ΛCDM across the data-allowed $`s_0`$ range. The $`(1+z)^1`$ correction enters growth only through $`H(z)`$, with no perturbation-level clustering parameter. (Full solve: [temporal-budget §XI.C](../../framework/files/working/files/temporal-budget.md).)

### Context: wCDM

A constant-<i>w</i> model (wCDM, 4 free parameters) fitted to the same SN+BAO dataset yields $`w = -0.855`$ [-0.89, -0.82] with $`\Delta\text{AIC} = -11.0`$ relative to ΛCDM. *The data favour some departure from $`w = -1`$, but do not require a phantom crossing.* The question is whether that departure is a constant shift toward $`w > -1`$ (as wCDM captures) or a phantom crossing (as CPL captures). The phase-clock model, for which $`w_\text{eff} > -1`$ at all redshifts, is consistent with the wCDM direction but at data-allowed $`s_0`$ the departure is too small to produce a detectable signal. The wCDM preference identifies a real tension with ΛCDM that the phase-clock at current constraints does not resolve. Whether that tension is a statistical fluctuation or a hint of additional structure will be clarified by Euclid.

## VI. Predictions and Falsification

### The $`(1+z)^1`$ Signature

The joint SN+BAO fit constrains $`|\beta| < 0.012`$ at 95% CL (from $`s_0 < 0.19`$ with $`\Omega_m = 0.315`$). The predicted fractional contribution to $`H^2(z)`$ at $`z = 1`$ is:

```math
\frac{|\beta|(1+z)}{E^2(z)} < 0.8\% \quad (95\%\ \text{CL at}\ z = 1)
```

This is below the precision of current BAO measurements (DESI DR2: ~2–3% per bin in $`D_H/r_d`$) but potentially within reach of the next generation. Euclid spectroscopic BAO ($`z = 0.9`$–1.8, four redshift bins) is forecast at 1–2% per bin, marginal for detection; that measurement is a higher-level science product and arrives with the full DR1 release in mid 2027, not with the November 2026 DR1-Foundation release, which carries raw data, calibrated images, catalogues and spectra but no cosmology-derived products. The discriminating regime is DESI full-survey and Euclid DR2 at ~0.5% per bin, where the $`(1+z)^1`$ signature reaches approximately 1.5σ per bin for $`s_0 \sim 0.15`$, with correlated bins improving aggregate sensitivity.

A statistically significant detection of a negative $`(1+z)^1`$ component in $`H^2(z)`$ would constitute evidence for a non-standard contribution to the distance-redshift relation. While a domain-wall fluid ($`w = -2/3`$) produces the same scaling, the phase-clock term is distinguished by the tied coefficient $`-\beta(s_0)`$ rather than an independent energy density.

### Falsification Criteria

All predictions are registered on Zenodo in advance of the data. Both criteria below read spectroscopic BAO, a higher-level science product delivered with the full Euclid DR1 release in mid 2027; ESA notes that release dates remain tentative:

| Observable | MIT prediction | Falsified if |
|---|---|---|
| **$`(1+z)^1`$ coefficient in $`H^2(z)`$** (primary) | Non-positive, magnitude tied to $`s_0`$; inferred from a fit that includes a free $`(1+z)^1`$ term alongside the standard FLRW components | Positive coefficient detected, or magnitude inconsistent with fitted $`s_0`$ |
| Diagnostic $`w_\text{eff}(z)`$ (derived consistency check) | $`> -1`$ under the fiducial split, any $`s_0 > 0`$ | Fiducial split gives $`w_\text{eff} < -1`$ at $`\geq 2\sigma`$ |

### Connection to $`a_0(z)`$

The same $`H(z)`$ derived here determines the epoch-dependent acceleration scale. Because $`a_0`$ and $`H`$ are both edge modes on the 120-domain (the discrete phase grid native to $`S^3/2I`$, the quotient of the three-sphere by the binary icosahedral group $`2I`$ with $`|2I| = 120`$), their ratio is fixed by Fibonacci wells: $`a_0/cH = 0.184`$. This ratio holds at every epoch, giving $`a_0(z) = a_0(0) \times H(z)/H_0`$. The two cornerstone papers embody the static universe from opposite sides: $`\Lambda`$ stays constant while $`a_0`$ evolves, both measured from the same standing wave.

---

The vacuum reference remains what the framework requires: a boundary condition seeded by the surface mode, not a field that evolves.

*What "evolves" is not Λ, but perspective.*

---

/ **[`↑top`](#top)** / **[`main`](https://github.com/dmobius3/mode-identity-theory/tree/main/)** / **[`framework`](/files/framework/)** / **[`bedrock`](/files/framework/files/bedrock/)** / **[`working`](/files/framework/files/working/)** / **[`cosmos`](/files/cosmos/)** / **[`spectrum`](/files/spectrum/)** / **[`tools`](/files/tools/)** /
