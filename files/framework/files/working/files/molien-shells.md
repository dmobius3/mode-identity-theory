<a id="top"></a>
/ **[`main`](https://github.com/dmobius3/mode-identity-theory/tree/main/)** / **[`framework`](/files/framework/)** / **[`bedrock`](/files/framework/files/bedrock/)** / **[`working`](/files/framework/files/working/)** / **[`cosmos`](/files/cosmos/)** / **[`spectrum`](/files/spectrum/)** / **[`tools`](/files/tools/)** /

---

# The Molien Shells

**Type:** Program
**State:** Active
**Status (2026-09-14):** Step one is done: up to N = 30 each surviving shell of S³/2I holds a single 2I-invariant form, whose roots on the sphere are the icosahedron's vertices (N = 12), face centres (N = 20) and edge midpoints (N = 30), with N = 24 the square of the first; the counts, the patterns and the even-spin descent to A5 are checked independently. The sky step's preregistered test, [The Molien Shells, Step Two](molien-step-two.md), closed Uninformative at its CAMB reproduction gate, before any P1 quantity was computed; a theory-only registration of P1's full-transfer spectrum, [The Molien Shells: The Full-Transfer Ratio Table](molien-ratio-table.md), tabulates it at both radii: after an erratum to its shell-sum interpolation, its second run found both routes Departing and Separated, a theory result not scored against data. [The Molien Shells: The P1 Bridge](molien-p1-bridge.md) answers the geometric part of what the source needs from MIT to reach the sky: the flat limit sends the canonical laws to P1, and below N = 60 a Q-symbol flattening would give a definite icosahedral pattern of directional power.
**Summary:** The Molien shells of S³/2I as MIT's CMB source structure: what the surviving shells carry, checked by an executable of its own, and the preregistered test that would take them to the sky.
**Inputs:** `../../../../cosmos/files/cmb-anomalies.md` §IV, `scripts/molien-shells.test.py`

In MIT's reading the low-ℓ deficit rests on the Molien shell gap of $`S^3/2I`$ ([CMB Anomalies](../../../../cosmos/files/cmb-anomalies.md) §IV): only $`2I`$-invariant harmonics survive, and none do between $`N = 2`$ and $`N = 10`$. That page counts the shells. This one records what the surviving shells carry, before any question about the sky, and fixes the gate the sky question has to pass. Here $`N`$ is the degree of a scalar harmonic on $`S^3`$, with Laplacian eigenvalue $`N(N+2)/R^2`$, so the first nonconstant shell sits at $`168/R^2`$. $`R`$ is the radius of the $`S^3`$ whose spectrum this is, which MIT's reading takes as a static boundary condition rather than a Friedmann curvature term, so it is not the radius the apparent $`\Omega_K`$ measures ([CMB Anomalies](../../../../cosmos/files/cmb-anomalies.md) §V); it plays no part in the checks below.

## I. What the surviving shells carry

The script checks the four statements below independently. Section IV lists the prior literature; exact statement-level attribution will be checked before any literature-priority claim is made.

1. **Counts.** Up to $`N = 30`$ the shells are $`N = 0, 12, 20, 24, 30`$, each with a single invariant, carrying 1, 13, 21, 25 and 31 surviving modes. The counts match both closed forms of the Molien series, $`(1 + t^{30})/((1 - t^{12})(1 - t^{20}))`$ and the three-generator form on the CMB page, and the rank of the group average over the 120 unit quaternions of $`2I`$ reproduces them independently.
2. **Structure.** Scalar harmonics at level $`N`$ on $`S^3`$ transform as $`\mathrm{Sym}^N\mathbb{C}^2 \otimes (\mathrm{Sym}^N\mathbb{C}^2)^*`$, with $`2I`$ acting on one factor. For these low shells the invariant subspace of that factor is one-dimensional, so the $`N + 1`$ surviving modes share one invariant-factor state, and therefore one Majorana constellation, while differing in the free spin label, of spin $`N/2`$. This is representation-space source structure, not yet a spatial or sky pattern.
3. **Patterns.** Each invariant form, read through its roots on the sphere, its Majorana constellation:
   - $`N = 12`$: the 12 vertices of a regular icosahedron, 6 axes;
   - $`N = 20`$: the 20 face centres of that icosahedron, 10 axes;
   - $`N = 24`$: the square of the $`N = 12`$ form, the vertices doubled;
   - $`N = 30`$: the 30 edge midpoints, 15 axes.

   These are Klein's vertex, face and edge forms, on the same 12, 20 and 30 point sets as the cone-point orbits of the Seifert base in [S³/2I and the OPH Carrier](s3-2i-oph-dictionary.md). The antipodal root sets are the Maxwell multipole directions of the corresponding harmonics, the description from which Lachièze-Rey and Weeks build these modes (Section IV).
4. **The even-spin descent, as the fixture.** $`-I`$ acts on $`\mathrm{Sym}^N\mathbb{C}^2`$ as $`(-1)^N`$, so odd degrees carry nothing and the even ones descend to $`A_5`$: the invariant count in degree $`N = 2\ell`$ equals the count of $`A_5`$-invariant harmonics at level $`\ell`$, exactly, for every $`\ell \le 30`$ (the known rows $`\ell = 2, 6, 10, 15, 30`$ give 0, 1, 1, 1, 2). So the patterns above are the $`\ell = 6, 10, 12, 15`$ icosahedral harmonics. This $`\ell`$ is an angular level of the source pattern, not a sky multipole.

## II. How the checks can fail

Four deliberately broken variants, each run after the check it breaks has passed:

- $`A_5`$ indexed by half-angle instead of rotation angle: the counts stop being integers.
- $`2I`$ indexed by rotation angle instead of half-angle: the known rows give 1, 4, 6, 9, 17, integers that look plausible and are wrong. The known rows catch this; integrality alone would not.
- Averaging over the binary tetrahedral subgroup instead of $`2I`$: an invariant appears at $`N = 6`$, where $`2I`$ has none.
- A generic degree-12 invariant of that subgroup: its roots do not form an icosahedron.

## III. The sky step, gated

The sky question: given this source structure, one invariant-factor state per shell times the free spin label, what does an observer at a point of $`S^3/2I`$ see at low sky multipoles? That needs MIT's own projection (the CMB page lists transfer functions, primordial weighting and observer position) and the radius $`R`$ from the independent routes ([The R Problem](r-problem.md)). Nothing runs until a preregistration contract is written and frozen, fixing in advance:

- the projection and all its inputs, with no parameter left free to tune after the fact;
- what counts as a hit and what as a miss for the low-ℓ spectrum;
- MIT's own matched-circle prediction from the same inputs, which [CMB Anomalies](../../../../cosmos/files/cmb-anomalies.md) §VI says the framework owes, stated as circle radii and judged against a named search. Whether a null excludes a model turns on those radii and on the search's sensitivity, which is where the published dispute over the Poincaré space lives (Caillerie et al. 2007), so the contract fixes both in advance. For instance, Cornish et al. 2004 found no matched circles, back-to-back or nearly so, of radius above 25° in the WMAP first-year maps. Circles predicted within the named search's reach, where it found none, would be a miss.

Flatness is not a test here, because MIT's reading keeps the apparent $`\Omega_K`$ at zero by construction. The published analyses of the conventional Poincaré-space model work in a finite, positively curved space, $`\Omega_0 \approx 1.013`$ in Luminet et al. 2003 and $`\Omega_0 = 1.018`$ in Caillerie et al. 2007. Their fits do not transfer to MIT's flat reading, so the circle test runs through MIT's own prediction.

The contract is frozen as [The Molien Shells, Step Two](molien-step-two.md). It fixes the projection as the P1 spectral-transfer prescription and the hit and miss as ±2 decision bands on the Planck low-ℓ likelihood. Since P1 identifies no points, the contract rules the circle observable N/A and records the countermodel that would carry circles, with the searches that exclude it.

## IV. Sources

Relevant prior literature, with metadata checked on 2026-09-13 against arXiv, Crossref, MathSciNet and zbMATH. These references locate the calculation in the existing Poincaré-space literature; they are not used as receipts for the executable results above unless a specific statement is attributed to a page or theorem.

- A. Ikeda, On the spectrum of homogeneous spherical space forms, *Kodai Math. J.* 18 (1995), 57-67, doi:[10.2996/kmj/1138043353](https://doi.org/10.2996/kmj/1138043353). The spectrum of $`S^3/2I`$ among the homogeneous spherical space forms.
- J. R. Weeks, Exact polynomial eigenmodes for homogeneous spherical 3-manifolds, *Class. Quantum Grav.* 23 (2006), 6971-6988, [arXiv:math/0502566](https://arxiv.org/abs/math/0502566); M. Lachièze-Rey, Eigenmodes of dodecahedral space, *Class. Quantum Grav.* 21 (2004), 2455-2464, [arXiv:gr-qc/0402035](https://arxiv.org/abs/gr-qc/0402035); M. Lachièze-Rey and S. Caillerie, Laplacian eigenmodes for spherical spaces, *Class. Quantum Grav.* 22 (2005), 695-708, doi:[10.1088/0264-9381/22/4/004](https://doi.org/10.1088/0264-9381/22/4/004). The eigenmodes as explicit invariant polynomials.
- P. Kramer, Invariant operator due to F. Klein quantizes H. Poincaré's dodecahedral 3-manifold, *J. Phys. A* 38 (2005), 3517-3540, [arXiv:gr-qc/0410094](https://arxiv.org/abs/gr-qc/0410094). Closest to the route through Klein's invariant, with the deck group acting on $`\mathrm{SU}(2)`$ by right multiplication. Its abstract describes the lowest eigenstates, at degree 12, as "12 partners of Klein's invariant polynomial"; how that count sits against the 13 modes here is one of the statement-level checks still owed.
- M. Lachièze-Rey and J. Weeks, Orbifold construction of the modes of the Poincaré dodecahedral space, [arXiv:0801.4232](https://arxiv.org/abs/0801.4232) (2008). Closest to the multipole-vector reading: the modes built from the Hopf map, Maxwell's multipole vectors and orbifolds, with the \*235 orbifold as a parameter space for the modes.
- J. Gundermann, Predicting the CMB power spectrum for binary polyhedral spaces, [arXiv:astro-ph/0503014](https://arxiv.org/abs/astro-ph/0503014) (2005).
- F. Klein, *Vorlesungen über das Ikosaeder und die Auflösung der Gleichungen vom fünften Grade*, Teubner, Leipzig, 1884 (JFM 16.0061.01). The invariant forms of degrees 12, 20 and 30.
- J.-P. Luminet, J. Weeks, A. Riazuelo, R. Lehoucq and J.-P. Uzan, Dodecahedral space topology as an explanation for weak wide-angle temperature correlations in the cosmic microwave background, *Nature* 425 (2003), 593-595, doi:[10.1038/nature01944](https://doi.org/10.1038/nature01944); S. Caillerie, M. Lachièze-Rey, J.-P. Luminet, R. Lehoucq, A. Riazuelo and J. Weeks, A new analysis of Poincaré dodecahedral space model, [arXiv:0705.0217](https://arxiv.org/abs/0705.0217) (2007). The conventional Poincaré-space model.
- N. J. Cornish, D. N. Spergel, G. D. Starkman and E. Komatsu, Constraining the topology of the universe, *Phys. Rev. Lett.* 92 (2004), 201302, [arXiv:astro-ph/0310233](https://arxiv.org/abs/astro-ph/0310233). A matched-circle search.

## Check

[molien-shells.test.py](scripts/molien-shells.test.py) checks the counts two ways, the exact Molien series and the rank of the Reynolds projector over the 120 unit quaternions of $`2I`$, the root patterns against a single regular icosahedron, and the even-spin descent to $`A_5`$ as an exact fixture in $`\mathbb{Z}[\varphi]`$, with the four mutation arms of Section II. The run is recorded in [molien-shells.out](scripts/molien-shells.out). It needs numpy and runs in about three seconds.

---

/ **[`↑top`](#top)** / **[`main`](https://github.com/dmobius3/mode-identity-theory/tree/main/)** / **[`framework`](/files/framework/)** / **[`bedrock`](/files/framework/files/bedrock/)** / **[`working`](/files/framework/files/working/)** / **[`cosmos`](/files/cosmos/)** / **[`spectrum`](/files/spectrum/)** / **[`tools`](/files/tools/)** /
