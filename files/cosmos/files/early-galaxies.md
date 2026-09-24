<a id="top"></a>
/ **[`main`](https://github.com/dmobius3/mode-identity-theory/tree/main/)** / **[`framework`](/files/framework/)** / **[`bedrock`](/files/framework/files/bedrock/)** / **[`working`](/files/framework/files/working/)** / **[`cosmos`](/files/cosmos/)** / **[`spectrum`](/files/spectrum/)** / **[`tools`](/files/tools/)** /

---

# 🌌 Early Galaxies

<img src="https://github.com/dmobius3/mode-identity-theory/blob/main/files/assets/early%20galaxy%20banner.png?raw=true" width="100%" alt="Early Galaxies">

JWST has found galaxies too massive, too early. Stellar masses of $`\sim 10^{10}\,M_\odot`$ at $`z \approx 10`$ push the inferred star formation efficiency toward or past unity, the limit at which every available baryon has become stars, under standard ΛCDM halo abundances.

Mode Identity Theory offers a reading that eases it. The MOND acceleration scale $`a_0`$ and the Hubble rate $`H`$ are both edge modes ($`n = 1`$) on the 120-domain (the discrete phase grid native to $`S^3/2I`$, the quotient of the three-sphere by the binary icosahedral group $`2I`$ with $`|2I| = 120`$). Their ratio is fixed by the Fibonacci wells:

```math
\frac{a_0}{cH} = \frac{C(13/120)}{C(34/120)} = 0.184
```

Because the ratio holds at every epoch, $`a_0(z) = a_0(0) \times H(z)/H_0`$, where $`H(z)`$ is the phase-clock Hubble rate derived from the static $`S^3`$ baseline. At $`z = 10`$, this gives $`a_0 \approx 20.5 \times`$ the local value, enhancing effective gravitational acceleration and, on an upper-bound estimate taken against constant-$`a_0`$ MOND (§III), reducing the implied star formation efficiency to $`\varepsilon_\text{SF} \sim 0.5`$, within the physically permitted range; clearing any individual candidate is a separate question.

MIT predicts $`a_0`$ evolves while $`\Lambda`$ is epoch-independent: the inverse of standard assumptions. This is the companion to the dark energy cornerstone, where the same $`H(z)`$ introduces no independent phantom fluid. One static universe, two signatures.

**Edge mode scaling**

| Quantity | Value |
|---|---|
| Scaling law | $`a_0(z) = a_0(0) \times H(z)/H_0`$ |
| $`a_0/(cH_0)`$ ratio | predicted: 0.184 / observed: 0.183 (SPARC $`a_0`$, Planck $`H_0`$; $`a_0`$ uncertain at tens of percent) |
| At $`z = 10`$ | $`a_0 \approx 2.46 \times 10^{-9}`$ m/s² (20.5× local) |
| Collapse speedup | ~2.1× faster (upper-bound estimate against constant-$`a_0`$ MOND: $`\varepsilon_\text{SF} \sim 0.5`$) |

## I. The Observational Tension

JWST observations (Labbé et al.) reveal stellar masses $`M_\star \sim 10^{10}\,M_\odot`$ already assembled at $`z \approx 10`$, roughly 500 Myr after the standing wave began its cycle. These masses approach or exceed the maximal baryon abundance permitted in standard dark matter halos under ΛCDM, creating the "impossibly early galaxy" problem.

The tension is quantitative. Assembling $`10^{10}\,M_\odot`$ of stars in 500 Myr requires converting nearly every available baryon into stars. Under standard ΛCDM halo abundances, the implied star formation efficiency $`\varepsilon_\text{SF}`$ approaches or exceeds unity, the physical limit. Either the observations contain systematic errors, the mass estimates are wrong, or the gravitational physics governing early collapse is different from what we assume locally.

MIT takes the third option. The acceleration scale governing collapse is not constant; it tracks the phase clock.

Whether the candidates sit past that limit at all is less settled than the problem's name suggests. [Boylan-Kolchin (2023)](https://doi.org/10.1038/s41550-023-01937-7) finds that the stellar-mass densities of the two most massive Labbé et al. candidates imply conversion efficiencies of 0.99 at $`z \approx 9.1`$ and 0.84 at $`z \approx 7.5`$, at or below the full-efficiency ceiling rather than above it, and the wider JWST measurements above $`z \approx 10`$ that the [Euclid card](euclid-dr1.md) examines lie inside that ceiling. Whether the population persists in Euclid's wide-area data is the card's Row IV (§V).

## II. Epoch-Dependent Acceleration Scale

### Static Baseline

The cosmos is a static three-sphere $`S^3`$. The phase-clock Hubble rate $`H(z)`$ is derived from the standing wave $`\Psi = \cos(t/2)`$ and the Waltz clock $`dt/d\tau = S^{-1/2}`$:

```math
\frac{H^2(z)}{H_0^2} = \frac{1 - \Omega_\Lambda}{1 - s_0^2}(1+z)^3 - \frac{(1 - \Omega_\Lambda)\,s_0^2}{1 - s_0^2}(1+z) + \Omega_\Lambda
```

with $`\Omega_\Lambda = 0.685`$ held fixed as the fiducial vacuum-fraction anchor and $`s_0 = \sin(t_\text{now}/2)`$ the single phase parameter. Here $`\Omega_\Lambda`$ is the vacuum density fraction $`f_\Lambda \approx 0.685`$ in the conventional ΛCDM sense, distinct from the MIT hierarchy $`\Omega_\Lambda = (R_\Lambda/\ell_P)^2`$. Both $`a_0`$ and $`H`$ are edge modes ($`n = 1`$) on the 120-domain. What follows is why their ratio is locked.

### The Ratio from the Scaling Law

The MIT scaling law relates any observable $`A`$ to the Planck reference $`A_P`$ through a phase coefficient and a power of the hierarchy number $`\sqrt{\Omega}`$:

```math
\frac{A}{A_P} = C(\Theta) \cdot (\sqrt{\Omega})^{-n}
```

where $`C(\Theta) = 2\sin^2(\pi\Theta)`$ is the phase operator (derived from the anti-periodic first positive mode on the Möbius surface, normalised to unit mean) and $`n`$ is the manifold depth: $`n = 1`$ for edge modes, $`n = 2`$ for surface modes.

Both $`a_0`$ and $`H`$ sit on the temporal edge ($`n = 1`$), referencing the same hierarchy number $`\Omega_H`$. In the ratio, the Planck scales and the $`\sqrt{\Omega_H}`$ factors cancel, leaving only the phase coefficients:

```math
\frac{a_0}{cH} = \frac{C(13/120)}{C(34/120)} = \frac{2\sin^2(13\pi/120)}{2\sin^2(34\pi/120)} = \frac{0.223}{1.208} = 0.184
```

With $`H_0 = 67.4`$ km/s/Mpc (the measured Planck anchor), $`cH_0 = 6.55 \times 10^{-10}`$ m/s², giving observed $`a_0/(cH_0) = 1.2/6.55 = 0.183`$, with $`a_0`$ itself uncertain at tens of percent ([Update 1](early-galaxies-update1.md)). The positions 13/120 and 34/120 are Fibonacci numbers on the 120-grid, occupying stability wells where destructive interference is minimised.

Two scope notes follow from this. The absolute scale is calibrated off the measured $`H_0`$ through the kinematic hierarchy $`\Omega_H = (c/(H\ell_P))^2`$, so the prediction does not depend on the open curvature radius $`R`$; only the companion claim that $`\Lambda`$ is constant touches it (the open [R problem](../../framework/files/working/files/r-problem.md)). And the ratio rests on the edge-mode positions alone, not on the galactic coherence mechanism $`L_f = v_c^2/a_0`$ that the SPARC test falsified.

### The Evolutionary Law

<img src="https://github.com/dmobius3/mode-identity-theory/blob/main/files/assets/eg-rising-a0.png?raw=true" width="70%" alt="a0(z)/a0(0) = H(z)/H0 on a log axis, rising to 20.5 times the local value at z = 10, where JWST finds its early galaxies, against the flat line of constant a0 in standard MOND">

Because the ratio is fixed at every epoch, the acceleration scale inherits the full redshift dependence of $`H(z)`$:

```math
a_0(z) = a_0(0) \times \frac{H(z)}{H_0}
```

This is the paper's central prediction. $`a_0`$ is not a fundamental constant; it is an edge mode that tracks the phase clock. At high redshift, $`H(z)/H_0`$ grows large, and the acceleration scale that governs gravitational collapse grows with it. The consequences for early structure formation follow in Section III.

## III. Early Structure Formation at z = 10

<img src="https://github.com/dmobius3/mode-identity-theory/blob/main/files/assets/eg-boost-cascade.png?raw=true" width="95%" alt="The boost step by step: a0 times 20.5 at z = 10 gives effective gravity times 4.5 in deep MOND, collapse about 2.1 times faster, and a star-formation efficiency down from about 1 or more to about 0.5; upper bounds, taken against constant-a0 MOND">

### The Boost

Using the phase-clock $`H(z)`$ from the static baseline, with $`\Omega_\Lambda = 0.685`$ and $`s_0 < 0.19`$:

```math
\frac{H^2(z)}{H_0^2} = \frac{1 - \Omega_\Lambda}{1 - s_0^2}(1+z)^3 - \frac{(1 - \Omega_\Lambda)\,s_0^2}{1 - s_0^2}(1+z) + \Omega_\Lambda
```

At $`z = 10`$, $`(1+z)^3 = 1331`$. The matter term dominates: $`\frac{1-\Omega_\Lambda}{1-s_0^2}(1+z)^3`$ contributes about 419 as $`s_0 \to 0`$ and about 435 at the $`s_0`$ bound, while the $`(1+z)^1`$ correction subtracts about 0.1 even at the bound. The result barely depends on $`s_0`$, rising from 20.5 as $`s_0 \to 0`$ to about 20.9 at the bound:

```math
\frac{H(z{=}10)}{H_0} \approx \sqrt{420} \approx 20.5
```

Applying the evolutionary law:

```math
a_0(z{=}10) \approx 20.5 \times a_0(0) \approx 2.46 \times 10^{-9}\ \text{m/s}^2
```

The acceleration scale governing gravitational collapse at $`z = 10`$ is twenty times the local value.

### Collapse Dynamics

In the deep-MOND regime ($`g \ll a_0`$), the effective gravitational acceleration scales as $`g_\text{eff} \propto \sqrt{g_N \times a_0}`$. Comparing an epoch-dependent $`a_0`$ to the standard constant assumption:

```math
\frac{g_\text{eff}(z{=}10)}{g_\text{eff}(\text{constant})} = \sqrt{\frac{a_0(z{=}10)}{a_0(0)}} = \sqrt{20.5} \approx 4.5
```

This is a factor of 4.5 enhancement in effective gravitational acceleration at fixed epoch. Both MIT and constant- $`a_0`$ MOND see the same $`H(z)`$ at $`z = 10`$; the difference is solely the strength of the acceleration floor.

Since free-fall timescale scales as $`t_\text{ff} \propto 1/\sqrt{g}`$, structures at $`z = 10`$ collapse approximately 2.1× faster than constant- $`a_0`$ MOND would predict. The enhancement is maximal in the deep-MOND limit; inner regions of forming halos where $`g`$ approaches $`a_0(z)`$ see a smaller correction, so these estimates are upper bounds.

### Easing the Constraint

For the Labbé et al. observations, whose implied $`\varepsilon_\text{SF}`$ approaches or exceeds 1 under standard ΛCDM assumptions, the 2.1× faster collapse brings the implied efficiency down to $`\varepsilon_\text{SF} \sim 0.5`$, inside the physically permitted range. That ratio is taken against constant-$`a_0`$ MOND, which is the baseline the 2.1$`\times`$ is computed from, rather than against the ΛCDM halos the original efficiency was derived in. That eases the "impossibly early galaxy" tension without invoking exotic physics, new particles, or any modification to general relativity. Clearing any individual candidate is a separate question, set by halo-mass assumptions the framework leaves untouched.

*The acceleration scale was simply larger when those galaxies formed.*

## IV. Contrasting Predictions: Edge vs Surface

MIT's dimensional hierarchy draws a sharp line between modes that live on the temporal edge and modes that live on the spatial surface:

| Observable | Manifold depth | Evolves? | Prediction |
|---|---|---|---|
| $`a_0`$ (acceleration) | $`n = 1`$ (edge) | Yes, tracks $`H(z)`$ | Evolves with epoch |
| $`\Lambda`$ (cosmological constant) | $`n = 2`$ (surface) | No | Epoch-independent: fixed by the static radius |

This is an inversion of standard assumptions, where $`\Lambda`$ is often treated as potentially evolving (the DESI phantom-crossing signal) while $`a_0`$ is assumed constant (standard MOND). MIT predicts the opposite: $`\Lambda`$ is fixed by the static curvature radius, and $`a_0`$ rides the phase clock.

The companion paper (*Phantom Dark Energy: Template Artifact in Static Space*) shows that the underlying $`H(z)`$ introduces no independent phantom fluid, and that restricted two-parameter templates can manufacture an apparent crossing from it. This paper predicts that $`a_0`$ evolves with $`H(z)`$; on an upper-bound estimate taken against constant-$`a_0`$ MOND (§III), the faster collapse roughly halves the implied star-formation efficiency of the JWST galaxies. Together, the two cornerstones embody the static universe from opposite sides: one observable constant, one evolving, both measured from the same standing wave.

Observations of both quantities at high redshift provide complementary tests. A universe where $`\Lambda`$ evolves and $`a_0`$ stays constant would falsify MIT. The converse does not confirm it: a rising $`a_0`$ also follows from other evolving-scale models and from ΛCDM simulations, so the discriminating content is the locked form and the exponent structure, not the direction of the climb.

## V. Falsification

| Observable | Test | Falsified if |
|---|---|---|
| $`a_0`$ universality in lensing (conditional) | Euclid DR1 stacked galaxy–galaxy lensing at $`z \approx 0.5`$ to $`2`$, under a relativistic completion carrying the $`E(z)`$ scaling into the lensing potential | The inferred $`M_\text{dyn}/M_b`$ enhancement is mass- or aperture-dependent in the ΛCDM sense, rather than the framework's mass-independent $`\sqrt{E(z)}`$ scaling |
| $`a_0(z)`$ evolution | Rotation curves / RAR / BTFR at $`z > 2`$ | $`a_0(z)/a_0(0) = 1`$, or the trend is inconsistent with $`E(z)`$ under matched systematics |
| $`\Lambda`$ epoch-independence | SNe Ia / BAO at high $`z`$ | $`\Lambda`$ varies with redshift at $`\geq 2\sigma`$ |
| Abundance above $`10^{10}\,M_\odot`$ at $`z > 10`$ | The first qualifying Euclid wide-area measurement of the cumulative number and stellar-mass densities | Either density lies inside the full-efficiency ceiling of [Boylan-Kolchin (2023)](https://doi.org/10.1038/s41550-023-01937-7) at $`\geq 2\sigma`$ |

The first row would be the cleanest discriminator and is conditional on a relativistic completion the framework has not supplied; the second is the necessary direction-and-rate check, and it carries the near-term weight. A rising $`a_0`$ alone is now corroborated but non-discriminating. The third row does not say how matter is subtracted when the dark-energy density is reconstructed, and in the phase-clock background no subtraction leaves an exactly flat residual. The Euclid card set its matching row's rule on 2026-09-21 for that reason; the note there gives the rule used for DR1 ([Euclid DR1](euclid-dr1.md) §I). The fourth row is the page's own population, scored as Row IV of the Euclid card against that ceiling since 2026-09-23. It can score before Euclid's full release, on the first qualifying measurement, and the JWST measurements the card examines lie inside the ceiling, so the row points toward failure. A failure would record that ΛCDM reaches the measured abundance below full efficiency, not that massive galaxies are absent above $`z = 10`$ ([Euclid DR1](euclid-dr1.md) §IV).

At $`z = 2`$, the prediction is $`a_0(z{=}2) \approx 3 \times a_0(0)`$. This is within reach of resolved rotation curves from JWST/NIRSpec and the ELT; Euclid's slitless NISP delivers redshifts rather than resolved rotation curves. These predictions distinguish MIT from both standard MOND (constant $`a_0`$) and ΛCDM (no acceleration threshold).

MUSE-DARK III (2026) supplies the first robust intermediate-redshift corroboration of the rising direction; the observational record and caveats are tracked on the [Euclid DR1 page](euclid-dr1.md), with the full comparison in [Update 1](early-galaxies-update1.md).

---

In 1983, Milgrom identified $`a_0`$ as a fundamental acceleration scale. For four decades the coincidence $`a_0 \approx cH_0`$ has had no settled explanation. MIT reads both as edge modes, with the ratio set by where they sit on the standing wave, and predicts that $`a_0`$ evolves with $`H(z)`$.

*Read this way, the galaxies found too early were formed under a stronger tide.*

---

/ **[`↑top`](#top)** / **[`main`](https://github.com/dmobius3/mode-identity-theory/tree/main/)** / **[`framework`](/files/framework/)** / **[`bedrock`](/files/framework/files/bedrock/)** / **[`working`](/files/framework/files/working/)** / **[`cosmos`](/files/cosmos/)** / **[`spectrum`](/files/spectrum/)** / **[`tools`](/files/tools/)** /
