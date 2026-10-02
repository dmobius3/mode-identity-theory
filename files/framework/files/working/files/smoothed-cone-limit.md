<a id="top"></a>
/ **[`main`](https://github.com/dmobius3/mode-identity-theory/tree/main/)** / **[`framework`](/files/framework/)** / **[`bedrock`](/files/framework/files/bedrock/)** / **[`working`](/files/framework/files/working/)** / **[`cosmos`](/files/cosmos/)** / **[`spectrum`](/files/spectrum/)** / **[`tools`](/files/tools/)** /

---

# The Smoothed-Cone Limit

**Type:** Program
**State:** Active
**Status (2026-10-02):** Declared before any computation: the smoothing class, what counts, the cross-check curves and what the result will not claim (§§II-IV). Nothing is computed yet; the theorem in §II is the target.
**Summary:** Whether smoothing the conic band's pinch selects the Friedrichs realization the carrier adopts or a transmitting one: the class it will be checked in, the curves the numbers will be compared with, and the claims it will not make.
**Inputs:** `../../bedrock/files/first-eigenvalue.md` (§7, Propositions 3.7 and 4.4, the conic trace coordinates), `projective-carrier.md` (§XI, 1e), `scaling-law-uniqueness.md`
**Parent:** `projective-carrier.md`

---

## I. The question

The [first-eigenvalue paper](../../bedrock/files/first-eigenvalue.md) leaves open whether a geometric regularization of the conic band's pinch selects a canonical defect length $`\delta_0`$, for instance as a norm-resolvent limit of smoothed-cone Laplacians (its §7). It expects a transmitting limit only under tuning to a zero-energy resonance, which the [projective carrier](projective-carrier.md)'s 1e grades MOTIVATED, not computed. 1e names a geometric regularization that selects a transmitting limit as the route that would overturn its Friedrichs realization, and the [scaling law](scaling-law-uniqueness.md) calls the smoothed-cone limit the check that could overturn it. This page fixes the class the check runs in before anything is computed.

## II. Declared (2026-10-02)

- **Fixed data.** The band's rectangle $`[0, \pi R] \times [-W, W]`$, its seam $`(0, w) \sim (\pi R, -w)`$, its Neumann edges and the orientation bundle's holonomy, as in the paper, with $`0 < W < \pi R/2`$.
- **The class.** The metric $`dy^2 + a_\varepsilon(y)^2\,dw^2`$ with $`a_\varepsilon(y)^2 = \cos^2(y/R) + \varepsilon^2`$. The collapsed fibre becomes a neck of width scale $`\varepsilon R`$; the topology is unchanged and no interaction is added.
- **Declared now, not claimed.** The later extension: $`a_\varepsilon`$ depending on $`y`$ alone, smooth and positive, smooth across the seam, symmetric about the pinch, and converging to $`\lvert\cos(y/R)\rvert`$ uniformly on $`[0, \pi R]`$, which excludes necks that bubble to finite area.
- **The operator.** The paper's: the Laplacian on functions and on sections of the orientation bundle, the untwisted and twisted classes. No potential.
- **What counts.** Index-by-index convergence of the eigenvalues to the Friedrichs realization, the Neumann lune, as $`\varepsilon \to 0`$, with resolvent convergence in a sense fixed with the proof, confirms Friedrichs for the class. Convergence to a bridging realization at a finite $`\delta_0`$ overturns 1e for the class. Any other limit is reported as found.
- **The theorem target.** As $`\varepsilon \to 0`$ both spectra converge index by index to the Friedrichs spectrum: the twisted bottom to $`0`$ with its eigenfunction to the zero mode, and the next level to $`2/R^2`$. A rate $`O(1/\ln(1/\varepsilon))`$, and the merging of the two classes at that rate, are targets, not results.

## III. The cross-check curves

One-dimensional eigenvalues for the class, down to $`\varepsilon`$ of about $`10^{-12}`$, will be compared with curves fixed here:
- the twisted bottom with the root in $`(0, 2/R^2)`$ of the paper's secular condition $`G(\lambda) = \ln(\varepsilon/4)`$ (its Proposition 4.4), the bridging condition at $`\delta_0 = \varepsilon R/2`$, where the neck's zero-energy matching puts the low spectrum to leading order, which is $`1/(R^2(\ln(4/\varepsilon) - 1))`$ to the first two orders;
- the next twisted level with $`2/R^2`$;
- the twisted and untwisted spectra, which should merge.

The grade is analytic: these numbers check it and do not decide it.

## IV. What the result will not claim

- Nothing about smoothings with a potential, such as a curvature term, with a neck of fixed size, or with any other resonantly tuned regularization; those are the transmitting routes, outside the class.
- Nothing about the later extension of §II until it is proved.
- No answer to 1e's sampling question, whether a sampled smooth ambient field should see a transmitting pinch.
- For smoothed bands, $`2/R^2`$ as the first positive level is claimed only in the limit.

---

/ **[`↑top`](#top)** / **[`main`](https://github.com/dmobius3/mode-identity-theory/tree/main/)** / **[`framework`](/files/framework/)** / **[`bedrock`](/files/framework/files/bedrock/)** / **[`working`](/files/framework/files/working/)** / **[`cosmos`](/files/cosmos/)** / **[`spectrum`](/files/spectrum/)** / **[`tools`](/files/tools/)** /
