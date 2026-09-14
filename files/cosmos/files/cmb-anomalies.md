<a id="top"></a>
/ **[`main`](https://github.com/dmobius3/mode-identity-theory/tree/main/)** / **[`framework`](/files/framework/)** / **[`bedrock`](/files/framework/files/bedrock/)** / **[`working`](/files/framework/files/working/)** / **[`cosmos`](/files/cosmos/)** / **[`spectrum`](/files/spectrum/)** / **[`tools`](/files/tools/)** /

---

# ♲ CMB Anomalies

<img src="https://pbs.twimg.com/media/HLmA7TCXsAEUMR-?format=jpg&name=4096x4096" width="100%" alt="CMB Anamolies">

Four large-angle features in the CMB have persisted across COBE, WMAP, and Planck: a low-ℓ power deficit, an anomalously low quadrupole, an odd-over-even parity preference ($`R_{TT} \approx 0.81`$), and a quadrupole-octupole alignment (the "axis of evil"). Each is modest (2-3σ), sensitive to the estimator and the mask, broadly consistent with ΛCDM, and still awaiting a polarization counterpart; the interest is less any single feature than the sector that carries the tension. Cosmic topology has long been proposed as a common origin.

This page fixes what the Poincaré homology sphere $`S^3/2I`$ contributes. Two facts about the manifold hold regardless of cosmology: it is chiral (§III), carrying no orientation-reversing self-isometry, and its $`2I`$-invariant scalar spectrum has the Molien shell gap (§IV), empty across $`N = 2`$ to $`10`$ with its first invariant at $`N = 12`$. The line the page draws is this: **the topology gives the shell gap, and the open problem is whether the independently read curvature radius $`R`$ puts that gap at the observed multipoles.** Chirality shuts one route to parity and leaves parity and alignment open to the eigenmode covariance; $`R`$ is read from the coupling and mass-spectrum routes rather than the CMB (§V).

## I. The four anomalies

At the largest angles ($`\ell < 30`$), Planck analyses continue to report four features first seen by COBE and WMAP:

- **Low-ℓ deficit.** Less large-angle power than best-fit ΛCDM.
- **Low quadrupole.** $`C_2`$ low relative to $`C_3`$ and the higher multipoles.
- **Parity asymmetry.** Odd-ℓ power exceeds even-ℓ at large scales; the Planck TT ratio is $`R_{TT} \approx 0.81`$ (unity is no preference).
- **Quadrupole-octupole alignment.** The $`\ell = 2`$ and $`\ell = 3`$ preferred axes align to within $`{\sim}10°`$.

Each is 2-3σ on its own, moves with the choice of estimator and mask, sits inside the spread ΛCDM realizations produce, and awaits a confirming signal in polarization. The case rests on their persistence across missions and their shared home at the largest scales, not on any one being decisive.

## II. The manifold

The spatial manifold is $`M = S^3/2I`$, where $`2I`$ is the binary icosahedral group of order 120, the largest exceptional finite subgroup of $`\mathrm{SU}(2) \cong S^3`$. It inherits the round metric of constant positive curvature, has $`\pi_1(M) = 2I`$ and $`b_1 = 0`$, and is orientable as a three-manifold. As the Poincaré homology sphere $`\Sigma(2,3,5)`$ it is chiral (§III). The Möbius surface of the broader framework selects the twisted sector in which the first-positive seed $`\Lambda_\text{top}`$ is realized; it is separate from the CMB spectrum. The curvature radius $`R`$ enters the harmonic spectrum (§IV); its value is the open problem of §V.

## III. Chirality theorem

The structural result is that $`S^3/2I`$ is chiral.

Every orientation-reversing isometry of $`S^3`$ has the form $`q \mapsto u\,\bar{q}\,v`$ in quaternion coordinates (conjugation reverses order). Since $`2I`$ acts by left multiplication, any such map turns that left action into a right one, and for a non-central element a left translation stays distinct from a right one. So $`S^3/2I`$ admits no orientation-reversing self-isometry: it is chiral. This matches the known property of $`\Sigma(2,3,5)`$ and the general fact that every closed three-dimensional spherical space form is orientable.

What this closes is one route to parity. An even/odd-ℓ grading driven by an orientation-reversing identification, a Möbius boundary condition of the kind earlier versions of this page invoked, would need exactly the self-isometry the theorem rules out; that grading route is shut, and the $`2I`$-invariant spectrum inherits no intrinsic parity selector from it. Parity itself stays open: a compact quotient can still carry parity-odd and aligned structure through the anisotropic covariance of its eigenmodes, a route cosmic-topology work has established in general (the COMPACT collaboration among them), where the covariance produces parity-odd correlations without parity-violating microphysics. The $`S^3/2I`$ channel specifically is the open calculation. So the parity asymmetry and the quadrupole-octupole alignment remain open to this topology, pending that calculation, rather than being assigned to it or removed from it.

## IV. The Molien shell gap

Scalar harmonics on $`S^3`$ are graded by polynomial degree $`N = 0, 1, 2, \ldots`$ with eigenvalue $`N(N+2)/R^2`$ and degeneracy $`(N+1)^2`$. On $`S^3/2I`$ only $`2I`$-invariant harmonics survive; the centre $`\{-1\}`$ acts on degree $`N`$ by $`(-1)^N`$, restricting invariants to even $`N`$. Among these the Molien series of the invariant ring is

```math
P(t) = \frac{1 - t^{60}}{(1 - t^{12})(1 - t^{20})(1 - t^{30})},
```

with generators at degrees 12, 20, and 30 (the three Klein icosahedral invariants). The first nontrivial invariant is at $`N = 12`$; the shells $`N = 2, 4, 6, 8, 10`$ are empty, and the surviving shells run $`N = 0, 12, 20, 24, 30, \ldots`$. This shell structure is topological and fixed, a spectral fact about $`S^3/2I`$ that holds independent of cosmology. What each surviving shell carries is worked out in [The Molien Shells](../../framework/files/working/files/molien-shells.md): up to $`N = 30`$ each holds a single invariant form, whose roots on the sphere are the icosahedron's vertices ($`N = 12`$), face centres ($`N = 20`$) and edge midpoints ($`N = 30`$), with $`N = 24`$ the square of the first.

Where the gap lands on the sky depends on $`R`$. Each shell maps to a characteristic multipole $`\ell_\mathrm{char}(N) = \sqrt{N(N+2)}\,\chi_*/R`$, with $`\chi_*`$ the comoving distance to last scattering, so the boundary set by the last empty shell ($`N = 10`$) scales as $`1/R`$: it falls near $`\ell \approx 28`$ at the measured-$`\Lambda`$ back-read $`R \approx 5.38`$ Gpc, near $`\ell \approx 24`$ at the coupling route's $`R \approx 6.1`$ Gpc, and between $`\ell \approx 14`$ and $`\ell \approx 7`$ across the mass sector's $`10.5`$ to $`20`$ Gpc span. The reach of the deficit into the observed range ($`\ell \lesssim 30`$) therefore rides on $`R`$. The comparison that matters is between the two *independent* readings, since the $`5.38`$ Gpc figure is the circular back-read of measured $`\Lambda`$ rather than a route: the coupling route lands the boundary in range, the mass sector points below it. The low quadrupole sits inside this same thinning; its $`C_2/C_3`$ value waits on the full projection (transfer functions, primordial weighting, observer position), held apart from the shell-gap result. Under the P1 spectral-transfer prescription, the low-ℓ spectrum at the coupling and electron-muon radii, computed with the full transfer function, is tabulated in [The Molien Shells: The Full-Transfer Ratio Table](../../framework/files/working/files/molien-ratio-table.md), as a theory result not scored against data.

## V. The curvature scale

The shell structure of §IV is fixed; what $`R`$ sets is where it lands, and $`R`$ is the framework's open problem rather than something the CMB supplies.

The operative cosmology is flat FLRW and CMB-consistent: spatial curvature enters as a static boundary condition rather than a Friedmann term, so the apparent $`\Omega_K`$ is zero and light propagates on flat-equivalent distances $`D_M = \chi_*`$. An earlier version of this analysis read $`R`$ off the deficit boundary, took it as a physical spatial-curvature radius, and applied the curved projection $`D_M = R\sin(\chi/R)`$, which moved the first acoustic peak to $`\ell \approx 42`$ and implied $`\Omega_\mathrm{tot} \approx 1.70`$; that step was a coordinate error, since the flat-FLRW distance relation leaves the acoustic scale and $`\Omega_\mathrm{tot}`$ at their measured values.

So the Molien gap fixes the shell structure, and $`R`$ fixes where that structure lands. Two independent routes read $`R`$, and they read it differently. The coupling ($`\alpha`$) route fixes $`\Omega_\Lambda`$, hence $`R \approx 6.1`$ Gpc and $`\Lambda_\text{ref}`$ about 23% below the measured value, which lands the gap near $`\ell \approx 24`$, inside the observed band. The canonical electron-muon mass reading gives an order-of-magnitude $`R`$ near 20 Gpc, which lands it near $`\ell \approx 7`$, below the band. That split, the well-conditioned route placing the deficit in range and the rough one below, is the open problem (tracked in [the R problem](../../framework/files/working/files/r-problem.md)). The hinge is falsifiable: the deficit must appear where the independently read $`R`$ puts it.

## VI. Matched circles

A compact quotient can produce matched circles where the last-scattering sphere meets its topological copies. Planck's searches returned a null over the topology classes and circle statistics tested, which constrains standard compact FLRW geometries whose fundamental domain reaches the last-scattering surface. This framework uses the topology as a global boundary condition while keeping CMB propagation flat-FLRW, so the standard curved-space circle exclusion describes a different geometry than the one here. The model therefore owes its own circle prediction, computed from the same $`R`$, transfer functions, and boundary prescription that set the low-ℓ spectrum. Until that calculation runs, the matched-circle null stays a consistency check, sitting to one side of both support and exclusion. Under the P1 spectral-transfer prescription of [The Molien Shells, Step Two](../../framework/files/working/files/molien-step-two.md), which identifies no points, the circle observable is N/A.

## VII. Falsification

| Claim | Falsified if |
|---|---|
| $`S^3/2I`$ is chiral | An orientation-reversing self-isometry of $`S^3/2I`$ is exhibited |
| The orientation-reversing grading route to parity is shut | A parity grading is derived from that route on the orientable quotient |
| Molien shell gap: first invariant at $`N = 12`$, shells 2-10 empty | A $`2I`$-invariant harmonic appears at $`N = 2, 4, 6, 8`$, or $`10`$ |
| The deficit lands at the observed multipoles | The independently read $`R`$ places the cutoff outside the observed $`\ell \lesssim 30`$ band |
| Under the P1 spectral-transfer prescription, the shell gap accounts for the low-ℓ deficit | $`\Delta \ln L \le -2`$ against ΛCDM at the coupling-route $`R`$, the out-of-support sentinel included |

---

The accounting is the result. Two facts about $`S^3/2I`$ hold independent of cosmology: it is chiral, and its $`2I`$-invariant scalar spectrum carries the Molien gap across $`N = 2`$ to $`10`$. From there the four anomalies sort. MIT reads the low-ℓ deficit, with the low quadrupole inside it, as the observational counterpart of the shell gap, and whether it reaches the observed multipoles rides on the independently read $`R`$: the coupling route, the better-conditioned one, places the last empty shell near $`\ell \approx 24`$ and lands the deficit in band; the mass-spectrum route, an order-of-magnitude reading, places it near $`\ell \approx 7`$, below the band. The parity asymmetry and the quadrupole-octupole alignment stay open to this topology through the eigenmode covariance, a calculation still to run. The matched-circle null stays a consistency check, pending the framework's own circle prediction. And the curvature radius is the open problem, read from the coupling and mass-spectrum routes rather than the CMB.

*The shell gap is the topology's to give; whether it lands where the data sees it is for $`R`$ to settle.*

---

/ **[`↑top`](#top)** / **[`main`](https://github.com/dmobius3/mode-identity-theory/tree/main/)** / **[`framework`](/files/framework/)** / **[`bedrock`](/files/framework/files/bedrock/)** / **[`working`](/files/framework/files/working/)** / **[`cosmos`](/files/cosmos/)** / **[`spectrum`](/files/spectrum/)** / **[`tools`](/files/tools/)** /
