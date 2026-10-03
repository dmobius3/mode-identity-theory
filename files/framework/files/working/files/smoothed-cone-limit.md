<a id="top"></a>
/ **[`main`](https://github.com/dmobius3/mode-identity-theory/tree/main/)** / **[`framework`](/files/framework/)** / **[`bedrock`](/files/framework/files/bedrock/)** / **[`working`](/files/framework/files/working/)** / **[`cosmos`](/files/cosmos/)** / **[`spectrum`](/files/spectrum/)** / **[`tools`](/files/tools/)** /

---

# The Smoothed-Cone Limit

**Type:** Program
**State:** Active
**Status (2026-10-03):** Declared before any computation (§§II-IV), then derived (§V): for the declared class the limit is the Friedrichs realization, eigenvalue by eigenvalue and in norm-resolvent sense under a fixed unitary identification, with the twisted bottom $`(1 + o(1))/(R^2\ln(4/\varepsilon))`$ (Proposition 1). Cross-checked (§VI) in the $`n = 0`$ sector: the twisted bottom approaches the declared curve and meets it to the integration's floor at $`\varepsilon \le 10^{-6}`$, and the twisted and untwisted levels merge. The extension of §II stays declared, and the rate $`O(1/\ln(1/\varepsilon))`$ for the other levels and for the merging stays a target. The first-eigenvalue paper carries Proposition 1's twisted case, with its proof, as its Proposition 7.1. §II's bridging outcome was in fact excluded for the class by nonnegativity (§V).
**Summary:** Whether smoothing the conic band's pinch selects the Friedrichs realization the carrier adopts or a transmitting one: the class it will be checked in, the curves the numbers will be compared with, and the claims it will not make.
**Inputs:** `../../bedrock/files/first-eigenvalue.md` (§7, Propositions 3.7 and 4.4, the conic trace coordinates), `projective-carrier.md` (§XI, 1e), `scaling-law-uniqueness.md`, `scripts/smoothed-cone-limit/`
**Parent:** `projective-carrier.md`

---

## I. The question

When this page was declared, the [first-eigenvalue paper](../../bedrock/files/first-eigenvalue.md) left open whether a geometric regularization of the conic band's pinch selects a canonical defect length $`\delta_0`$, for instance as a norm-resolvent limit of smoothed-cone Laplacians (its §7). Its §7 now carries §V's result for the twisted class, with its proof, as Proposition 7.1, and notes that no smoothing that keeps the Laplacian nonnegative can select a finite $`\delta_0`$, every bridging realization having a negative eigenvalue (2026-10-03). It expects a transmitting limit only under tuning to a zero-energy resonance, which the [projective carrier](projective-carrier.md)'s 1e grades MOTIVATED. 1e names a geometric regularization that selects a transmitting limit as the route that would overturn its Friedrichs realization, and the [scaling law](scaling-law-uniqueness.md) calls the smoothed-cone limit the check that could overturn it. This page fixes the class the check runs in before anything is computed.

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

## V. The limit

**Proposition 1 (DERIVED).** In the declared class, $`a_\varepsilon^2 = \cos^2(y/R) + \varepsilon^2`$ with $`0 < W < \pi R/2`$, as $`\varepsilon \to 0`$ and in each class:
1. the eigenvalues converge index by index, with multiplicity, to those of the Friedrichs realization;
2. under the unitary map $`J_\varepsilon f = (a_0/a_\varepsilon)^{1/2} f`$ from $`L^2(a_0\,dy\,dw)`$ to $`L^2(a_\varepsilon\,dy\,dw)`$, with $`a_0 = \lvert\cos(y/R)\rvert`$, the spectral projection onto the eigenvalues below any $`\Lambda`$ outside the Friedrichs spectrum converges in norm, and so does the resolvent at any $`z`$ off that spectrum;
3. the twisted bottom satisfies $`R^2 \ln(4/\varepsilon)\,\lambda_0^{\mathrm{tw}}(\varepsilon) \to 1`$, its eigenfunction tending to the zero mode $`\phi_0`$, and the next twisted level tends to $`2/R^2`$, its eigenfunction tending to the tilt $`\sin(y/R)`$.

So the limit is Friedrichs, the outcome §II declares as confirming: it is not a bridging realization at any finite $`\delta_0`$, and no other limit occurs.

*Proof.* Write $`\delta = y - \pi R/2`$ and $`F(\delta) = \int_0^\delta ds/a_\varepsilon(s)`$.
1. *Sectors.* The paper's reduction (its Proposition 3.7) needs only that $`a_\varepsilon`$ depend on $`y`$ alone. In each class the spectrum is the union over $`n \ge 0`$ of the problems $`-(aY')'/a + k_n^2 Y/a^2 = \lambda Y`$ on $`[0, \pi R]`$, with $`k_n = n\pi/2W`$, $`Y(0) = sY(\pi R)`$, $`Y'(0) = sY'(\pi R)`$ and $`s = \pm(-1)^n`$, the sign $`+`$ untwisted and $`-`$ twisted, and with the form $`q_n^\varepsilon(Y) = \int (\lvert Y'\rvert^2 + k_n^2 Y^2/a_\varepsilon^2)\,a_\varepsilon\,dy`$ on $`L^2(a_\varepsilon\,dy)`$; $`q_n^0`$ is the same with $`a_0`$. Since $`a_\varepsilon^2 \le 1 + \varepsilon^2`$, $`q_n^\varepsilon \ge k_n^2 (1+\varepsilon^2)^{-1}\lVert Y\rVert^2`$, so below any $`\Lambda`$ only finitely many sectors contribute, uniformly in $`\varepsilon \le 1`$, and it is enough to prove 1 and 2 sector by sector.
2. *The limit sectors.* For $`n \ge 1`$ the exponent $`k_n R > 1`$ makes the pinch limit point, so the limit problem has one realization; its form domain is the functions with $`q_n^0 < \infty`$, which vanish at the pinch. For $`n = 0`$ the pinch is limit circle, and the Friedrichs form domain is the maximal one, $`\int (\lvert Y'\rvert^2 + Y^2)\,a_0\,dy < \infty`$, with the two sides independent: the cut-off $`\min(1, \max(0, \ln(\lvert\delta\rvert/\eta^2)/\ln(1/\eta)))`$ costs energy of order $`1/\ln(1/\eta)`$, so after truncation the functions that vanish near the pinch are dense in it. Its spectrum is the Legendre spectrum $`\ell(\ell+1)/R^2`$, $`\ell \ge 0`$, in either class (the paper; on the interval cut at the pinch the seam's sign is gauged away).
3. *Upper bounds.* Take the first $`k`$ limit eigenfunctions of a sector. For $`n \ge 1`$ they vanish at the pinch like $`\lvert\delta\rvert^{k_n R}`$ and are admissible for $`\varepsilon > 0`$ as they are; since $`a_0 \le a_\varepsilon \le a_0 + \varepsilon`$, each form grows by at most $`\varepsilon \int \lvert Y'\rvert^2`$ and no norm shrinks. For $`n = 0`$ they may take different values $`A_\pm`$ on the two sides of the pinch; on $`\lvert\delta\rvert < \eta`$ replace them by $`c_0 + c_1 F(\delta)`$, matched at $`\pm\eta`$. That map is linear and adds at most $`(A_+ - A_-)^2/2F(\eta) + o_\eta(1)`$ to the form, with $`F(\eta) \ge R\ln(\eta/\varepsilon R)`$. Min–max gives $`\limsup \lambda_k(\varepsilon) \le \lambda_k(0) + o_\eta(1)`$ for each $`\eta`$, hence $`\limsup \lambda_k(\varepsilon) \le \lambda_k(0)`$.
4. *Lower bounds.* Take $`\varepsilon_j \to 0`$ and orthonormal eigenfunctions of the $`k`$ lowest levels of a sector; by step 3 their forms are bounded. Away from the pinch $`a_\varepsilon`$ is bounded below, so a subsequence converges uniformly on compact sets. No mass collects at the pinch: $`\lim_{\eta \to 0} \limsup_j \int_{\lvert\delta\rvert<\eta} Y_j^2 a_{\varepsilon_j} = 0`$. For $`n \ge 1`$ that mass is at most $`(\sin^2(\eta/R) + \varepsilon_j^2)\,q_n^{\varepsilon_j}(Y_j)/k_n^2`$. For $`n = 0`$, $`1/a_\varepsilon \le 1/a_0`$ gives $`\lvert Y(\delta) - Y(\delta')\rvert^2 \le q_0^\varepsilon(Y)\,R\,\lvert\ln(\tan(\lvert\delta\rvert/2R)/\tan(\lvert\delta'\rvert/2R))\rvert`$ on each side of the pinch, uniformly in $`\varepsilon`$; anchored at a fixed $`\eta_0`$, where uniform convergence bounds $`Y_j`$, it gives $`Y_j(\delta)^2 \le C(1 + \ln(\eta_0/\lvert\delta\rvert))`$, and with $`a_\varepsilon \le a_0 + \varepsilon`$ the mass is at most $`C(\eta^2 + \varepsilon_j\eta)(1 + \ln(1/\eta))`$. The limits are therefore orthonormal in $`L^2(a_0\,dy)`$, and by weak lower semicontinuity on compact sets, with Fatou's lemma for the $`k_n^2`$ term, they lie in the limit form domain with $`q_n^0`$ at most the lim inf of $`q_n^{\varepsilon_j}`$ on their span. For $`n = 0`$ that domain is the Friedrichs one (step 2). Min–max gives $`\lambda_k(0) \le \liminf \lambda_k(\varepsilon_j)`$.
5. *Eigenfunctions, projections and resolvents.* With steps 3 and 4, every limit point of a level's eigenfunctions lies in the limit eigenspace, so the eigenspaces converge, and uniform convergence away from the pinch with no mass at it gives the norm convergence of the projections in 2. Above $`\Lambda`$ both resolvents have norm at most $`1/\mathrm{dist}(z, [\Lambda, \infty))`$, the operators being self-adjoint and nonnegative, and below $`\Lambda`$ they converge in norm with the eigenvalues and eigenspaces; letting $`\varepsilon \to 0`$ and then $`\Lambda \to \infty`$ gives the norm convergence of the resolvents.
6. *The twisted bottom.* The twisted $`n = 0`$ problem is antiperiodic. For such $`Y`$ and any $`y`$, $`2\lvert Y(y)\rvert = \lvert Y(y + \pi R) - Y(y)\rvert \le q_0^\varepsilon(Y)^{1/2}(\int_0^{\pi R} dy/a_\varepsilon)^{1/2}`$, while $`\lVert Y\rVert^2 \le \max Y^2 \int_0^{\pi R} a_\varepsilon\,dy`$, so $`\lambda_0 \ge 4/(\int a_\varepsilon \int a_\varepsilon^{-1})`$. The antiperiodic function $`F(\delta)/F(\pi R/2)`$ has form $`2/F(\pi R/2)`$ and norm tending to $`\int a_0\,dy = 2R`$. Here $`\int_0^{\pi R} a_\varepsilon\,dy = 2R + o(1)`$ and $`\int_0^{\pi R} dy/a_\varepsilon = 2F(\pi R/2) = 2R\,K(k)/(1+\varepsilon^2)^{1/2} = 2R\ln(4/\varepsilon) + o(1)`$, with $`K`$ the complete elliptic integral and $`k = (1+\varepsilon^2)^{-1/2}`$, so both bounds are $`(1 + o(1))/(R^2\ln(4/\varepsilon))`$. The $`n \ge 1`$ sectors stay above $`k_1^2/(1+\varepsilon^2)`$, so this is the twisted bottom; by step 5 its eigenfunction tends to $`\phi_0`$, and the next twisted level tends to the second Friedrichs level, $`2/R^2`$, simple below the critical width, with the tilt as its eigenfunction. ∎

- **What it confirms.** Friedrichs, for the declared class. It does not reach the extension of §II, potentials, necks of fixed size or 1e's sampling question (§IV).
- **The bridging outcome (2026-10-03).** §II's overturning outcome, a bridging limit at finite $`\delta_0`$, could not occur in the declared class: the class is nonnegative, every bridging realization has the negative eigenvalue $`\lambda_b(\delta_0)`$, and a norm- or strong-resolvent limit of nonnegative operators is nonnegative. What Proposition 1 decides is which nonnegative limit occurs. The first-eigenvalue paper's §7 states the obstruction.
- **Rates.** Item 3 gives the twisted bottom's rate, two-sided at leading order. For the other levels, and for the merging of the two classes, the rate $`O(1/\ln(1/\varepsilon))`$ stays a target; step 3 gives upper bounds of that order for levels whose limit eigenfunctions jump at the pinch.
- **The cross-check.** Step 6's two bounds hold at every $`\varepsilon`$, not only in the limit, so each computed twisted bottom must lie between them. With $`L = \ln(4/\varepsilon)`$ they are $`(1 + O(\varepsilon^2 L))/(R^2 L)`$ and, the test function's norm falling short of $`2R`$ by $`4R\ln 2/L`$ at leading order, $`(1 + 2\ln 2/L)/(R^2 L)`$; the declared curve $`1/(R^2(L - 1)) = (1 + 1/L)/(R^2 L) + O(L^{-3})`$ lies between them, and the cross-check of §III tests it.
- **Literature.** Smooth families converging to a conical singularity are treated by D. A. Sher, *Conic degeneration and the determinant of the Laplacian*, [J. Anal. Math. 126, 175–226 (2015)](https://doi.org/10.1007/s11854-015-0015-3). Here separation of variables reduces the two-ended neck, the twisted bundle and the Neumann edges to one-dimensional problems, so the proof stands on its own.

## VI. The cross-check

With $`R = 1`$, `scripts/smoothed-cone-limit/cross_check.py` computes the four lowest twisted levels $`t_k`$ and untwisted levels $`u_k`$ of the $`n = 0`$ sector, $`k = 0, \dots, 3`$, at eight values of $`\varepsilon`$ from $`10^{-1}`$ to $`10^{-12}`$; that sector carries §III's curves and does not depend on $`W`$, and $`u_0 = 0`$ is the constant. It integrates from the pinch to the seam in the variable $`F(\delta)`$ of §V, in which the sector reads $`-d^2Y/dF^2 = \lambda a_\varepsilon^2 Y`$; a second integration, in $`\delta`$, agrees with it on every computed level to relative $`10^{-8}`$ at $`\varepsilon = 10^{-1}, 10^{-2}, 10^{-3}`$. It was run after the declaration and the proof landed, and each of its six checks carries a planted defect that fires. The checks and their thresholds were set before its first run and not changed after it. After that run its machinery was corrected in five places: the root finder's tolerance, raised to the floor it accepts; the first integration's absolute tolerance on $`\delta`$, put on the neck's scale; the half-length $`F(\pi R/2)`$, now computed by the arithmetic-geometric mean after its elliptic integral lost digits to cancellation at small $`\varepsilon`$, a loss the seam check caught; the level scan's ceiling, raised from 14 to 22 to reach the fourth untwisted level at $`\varepsilon = 10^{-1}`$; and the agreement check's planted defect, replaced because a constant factor on $`a_\varepsilon`$ cancels from the equation and so planted nothing. Its record is `cross_check.out`.

| $`\varepsilon`$ | twisted bottom $`t_0`$ | declared curve | relative gap | lower bound | upper bound | $`t_1 - 2`$ |
| --- | --- | --- | --- | --- | --- | --- |
| $`10^{-1}`$ | 0.359014232362 | 0.362751787720 | $`1.03 \times 10^{-2}`$ | 0.266011 | 0.392079 | $`-7.83 \times 10^{-2}`$ |
| $`10^{-2}`$ | 0.198867539859 | 0.198895058070 | $`1.38 \times 10^{-4}`$ | 0.166853 | 0.210834 | $`-1.50 \times 10^{-3}`$ |
| $`10^{-3}`$ | 0.136634650202 | 0.136634889444 | $`1.75 \times 10^{-6}`$ | 0.120568 | 0.142716 | $`-2.19 \times 10^{-5}`$ |
| $`10^{-4}`$ | 0.104000178247 | 0.104000180458 | $`2.13 \times 10^{-8}`$ | 0.094370 | 0.107666 | $`-2.88 \times 10^{-7}`$ |
| $`10^{-6}`$ | 0.070351107453 | 0.070351107453 | $`2.33 \times 10^{-12}`$ | 0.065782 | 0.072100 | $`-4.06 \times 10^{-11}`$ |
| $`10^{-8}`$ | 0.053144902948 | 0.053144902947 | $`1.38 \times 10^{-12}`$ | 0.050487 | 0.054165 | $`4.50 \times 10^{-12}`$ |
| $`10^{-10}`$ | 0.042698966151 | 0.042698966151 | $`2.14 \times 10^{-12}`$ | 0.040963 | 0.043366 | $`7.07 \times 10^{-12}`$ |
| $`10^{-12}`$ | 0.035684104623 | 0.035684104623 | $`3.09 \times 10^{-12}`$ | 0.034462 | 0.036154 | $`9.70 \times 10^{-12}`$ |

- **The declared curve holds.** The twisted bottom approaches the root of $`G(\lambda) = \ln(\varepsilon/4)`$, the bridging condition at $`\delta_0 = \varepsilon R/2`$: the relative gap falls from $`1.03 \times 10^{-2}`$ at $`\varepsilon = 10^{-1}`$ to $`2.13 \times 10^{-8}`$ at $`10^{-4}`$, and at $`\varepsilon \le 10^{-6}`$ it is at the level of the integration's relative tolerance, $`10^{-12}`$.
- **Proposition 1's bounds hold** at every $`\varepsilon`$.
- **The next twisted level tends to 2**, from below and much faster than the bottom tends to 0: its distance from 2 falls from $`7.83 \times 10^{-2}`$ at $`\varepsilon = 10^{-1}`$ to $`4.06 \times 10^{-11}`$ at $`10^{-6}`$, and at $`\varepsilon \le 10^{-8}`$ it is at the integration's floor, about $`10^{-11}`$. Its limit eigenfunction, the tilt, takes the same value on both sides of the pinch, while $`\phi_0`$ changes sign there, and the cost of order $`1/\ln(1/\varepsilon)`$ in step 3 comes from such a jump (§V, Rates).
- **The two classes merge.** For each $`k`$ the difference $`\lvert t_k - u_k\rvert`$ shrinks at every step as $`\varepsilon`$ goes to 0, and so, slowly, does $`\ln(4/\varepsilon)\lvert t_k - u_k\rvert`$: for $`k = 1`$ from 4.54 at $`\varepsilon = 10^{-1}`$ to 3.14 at $`10^{-12}`$. That is consistent with merging at the rate $`O(1/\ln(1/\varepsilon))`$, which stays a target (§V, Rates). The differences $`\lvert t_k - u_k\rvert`$:

| $`\varepsilon`$ | $`k = 0`$ | $`k = 1`$ | $`k = 2`$ | $`k = 3`$ |
| --- | --- | --- | --- | --- |
| $`10^{-1}`$ | 0.3590 | 1.2306 | 2.3984 | 3.8396 |
| $`10^{-2}`$ | 0.1989 | 0.6360 | 1.1407 | 1.6973 |
| $`10^{-3}`$ | 0.1366 | 0.4284 | 0.7504 | 1.0931 |
| $`10^{-4}`$ | 0.1040 | 0.3227 | 0.5587 | 0.8060 |
| $`10^{-6}`$ | 0.0704 | 0.2160 | 0.3694 | 0.5276 |
| $`10^{-8}`$ | 0.0531 | 0.1623 | 0.2757 | 0.3919 |
| $`10^{-10}`$ | 0.0427 | 0.1299 | 0.2199 | 0.3117 |
| $`10^{-12}`$ | 0.0357 | 0.1083 | 0.1829 | 0.2587 |

- **What it does not do.** The numbers check the analysis and do not decide it (§III), and they cover only the $`n = 0`$ sector.

## Files

In [`scripts/smoothed-cone-limit/`](scripts/smoothed-cone-limit/), with the SHA-256 of every other file in `SHA256SUMS`:
- `cross_check.py`: §VI's levels by two integrations of the $`n = 0`$ sector, with six checks: the two integrations agree, the first lands on the seam, the twisted bottom lies between Proposition 1's bounds and meets the declared curve, the next twisted level meets 2, and the two classes merge, each with a planted defect that must fire. Its record is `cross_check.out`, from Python 3.13, NumPy 2.5.0, SciPy 1.18.0 and mpmath 1.3.0; elsewhere the digits at the integration's floor may differ.

---

/ **[`↑top`](#top)** / **[`main`](https://github.com/dmobius3/mode-identity-theory/tree/main/)** / **[`framework`](/files/framework/)** / **[`bedrock`](/files/framework/files/bedrock/)** / **[`working`](/files/framework/files/working/)** / **[`cosmos`](/files/cosmos/)** / **[`spectrum`](/files/spectrum/)** / **[`tools`](/files/tools/)** /
