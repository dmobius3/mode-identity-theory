<a id="top"></a>
/ **[`main`](https://github.com/dmobius3/mode-identity-theory/tree/main/)** / **[`framework`](/files/framework/)** / **[`bedrock`](/files/framework/files/bedrock/)** / **[`working`](/files/framework/files/working/)** / **[`cosmos`](/files/cosmos/)** / **[`spectrum`](/files/spectrum/)** / **[`tools`](/files/tools/)** /

---

# The Shell-to-Radius Transfers

**Type:** Result
**State:** Closed
**Status (2026-09-15):** Complete as a classification, checked by one script. When a transfer may move a shell's power between wavenumbers and between shells, positivity, SU(2)-covariance, reality and normalization give each shell a probability measure over wavenumber and pair sum, and leave its radial profile free: any placement, any width, any mixing of shells at one wavenumber. P1's radial rule, shell N at k_N = √(N(N+2))/R, is selected by three further conditions. Carrying the S³ Laplacian to the flat one forces it exactly. The flat limit recovers it as N grows. Locality selects it at every N: matching a shell's correlations around the observer fixes its mean squared wavenumber at N(N+2)/R², no positive flat spectrum matches them to fourth order, and the profile with no width comes closest. A width acts first on the phases the ratio table's per-multipole structure carries, not on where the first shell lands.
**Summary:** What linearity, positivity and SU(2)-covariance allow when a map from the Molien source covariance to a flat power may redistribute it in wavenumber, what puts each shell back at k_N, and what a width would do to the ratio table.
**Inputs:** `directional-transfers.md` §II, `molien-p1-bridge.md` §V, `molien-ratio-table.md` §6, §8, `scripts/molien-ratio-table-runs/run-2/result_report.txt`, `scripts/radial-transfer/radial_check.py`
**Parent:** `stress-tensor-bridge.md`

---

## I. The question

[The Shell-to-Direction Transfers](directional-transfers.md) classified what a projection can do to a Molien shell's covariance over directions, shell by shell, conditioning on P1's premise that each shell keeps its wavenumber. This page drops the premise.

> What are all the positive, linear, SU(2)-covariant maps from the block-diagonal Molien source covariance $`\{A_N\}`$ to a nonnegative power over flat wave vectors, when power may move between wavenumbers and between shells, and what puts shell $`N`$ back at $`k_N`$?

## II. The family

A flat stationary field's covariance is a positive spectral measure on wave vectors (Bochner), so a transfer assigns to the source a positive measure $`P(dk, d\hat n)`$, with $`k`$ the wavenumber and $`\hat n`$ the direction. Linearity and positivity give, shell by shell, a positive operator-valued measure $`E_N(dk, d\hat n)`$ on $`\mathrm{Sym}^N`$ with $`P = \sum_N \mathrm{Tr}[A_N E_N]`$; no operator between two shells enters, since the source has no covariance between shells. Rotations turn $`\hat n`$ and leave $`k`$ alone, so for every set $`B`$ of wavenumbers the argument of [the directional page](directional-transfers.md) §II applies to $`E_N(B, \cdot)`$ unchanged. At the pole it is diagonal,

```math
E_N(B, \hat z) = \sum_{m=-j}^{j} \tau_{Nm}(B)\, \lvert j,m\rangle\langle j,m\rvert ,
```

with each $`\tau_{Nm}`$ a positive measure on $`k \ge 0`$. At $`k = 0`$ the stabilizer is all of SU(2), so an atom there takes only the trace, as a constant.

1. **Shells can mix at one wavenumber.** Nothing ties $`\tau_{Nm}`$ to $`\tau_{N'm'}`$. Every shell may contribute at one output wavenumber, isotropically or not, with weights of its own: shell 20's power can sit at $`k_{12}`$ and violate nothing.
2. **Normalization is per shell.** P1 keeps each shell's variance, so the condition is $`\sum_m \tau_{Nm}([0,\infty)) = 1`$ for every $`N`$, the directional page's $`\sum_m t_m = 1`$ integrated over $`k`$. Normalizing only the sum over shells would be weaker, and would let variance move between shells.
3. **Reality acts pointwise in $`k`$.** For each $`B`$, $`E_N(B, \hat z)`$ is diagonal, and the directional page's real-field argument applies to it: on a covariance that commutes with time reversal only $`u_{Nm}(B) = \tau_{Nm}(B) + \tau_{N,-m}(B)`$ act.

So a physical transfer is, for each shell, a probability measure on $`[0,\infty) \times \{0, 1, \ldots, N/2\}`$, recording where in $`k`$ each pair sum's weight goes. The directional page's simplex is the face on which all of shell $`N`$'s mass sits at $`k_N`$. Positivity, covariance, reality and normalization leave every shell's radial profile free. **(Pointer added 2026-09-15.)** This classification assumes covariance under every rotation of the flat target, whose status [The Effective-Metric Floors](effective-metric-floors.md) records and the Stress-Tensor Bridge carries as C10; §III's intertwining and locality arguments do not use it. [The Spatial Carriers](spatial-carriers.md) then asks which covariance transfers admit deterministic field-level shell lifts. In the full-rotation branch no nonzero finite-shell lift survives; under only $`A_5`$ equivariance, outside that full-rotation family, specific atomic carriers can exist.

## III. What puts shell N at k_N

**Spectral intertwining, exactly.** If the transfer carries the $`S^3`$ Laplacian to the flat one, a shell with eigenvalue $`\lambda_N = N(N+2)/R^2`$ becomes a flat field with $`-\nabla^2 = \lambda_N`$, whose spectral measure lies on $`k^2 = \lambda_N`$. Every $`\tau_{Nm}`$ then sits at $`k_N`$, and no shell contributes at another's wavenumber. Any injective function of the Laplacian also forces a single wavenumber, and the operator chosen fixes only the center: $`-\Delta + 1/R^2`$, the spatial operator of a conformally coupled field on the static $`\mathbb{R} \times S^3`$, puts the shell at $`(N+1)/R`$, 0.30% above $`k_N`$ at $`N = 12`$, which moves its landing at route A by 0.09 in $`\ell`$.

**The flat limit, as N grows.** [The P1 Bridge](molien-p1-bridge.md) §V carries a regular family to the flat shell kernel at $`k_N`$ as $`N \to \infty`$ at fixed $`k_N r`$. That fixes the center to leading order and sends the relative width to zero. It fixes nothing at $`N = 12`$, where the invariant-projector law's kernel on the sphere and its symbol transfer still differ by up to 0.35 at a separation of $`0.46R`$.

**Locality, at every N.** Compare the shell's correlations around the observer, pulled back to flat space by the exponential map, with a homogeneous flat field's, through their means over spheres about the observer. Pizzetti's formula writes those means through the flat Laplacians of the pullback $`\tilde f`$ at the observer, and for any function $`f`$ on shell $`N`$, isotropic or not,

```math
\nabla^2 \tilde f(0) = -\lambda_N\, f(0), \qquad \nabla^4 \tilde f(0) = \Bigl(\lambda_N^2 - \frac{4}{3}\,\frac{\lambda_N}{R^2}\Bigr) f(0),
```

the second holding for every function because the round $`S^3`$'s curvature is the same in every direction. A flat field's means are $`\langle j_0(kt)\rangle = \sum_p (-t^2)^p \langle k^{2p}\rangle/(2p+1)!`$, averaged over its spectral measure. So:

- a match through second order fixes $`\langle k^2\rangle = \lambda_N`$, exactly and at every $`N`$: $`k_N`$ is the shell's root-mean-square wavenumber;
- a match through fourth order would need $`\langle k^4\rangle < \langle k^2\rangle^2`$, which no positive spectrum allows;
- with the second order held, the fourth-order shortfall is $`\mathrm{Var}(k^2) + \tfrac43 \lambda_N/R^2`$, least exactly when the variance vanishes: the profile with no width, at $`k_N`$, with any directional weights.

The curvature's irreducible shortfall is $`\tfrac43/(N(N+2))`$ of $`\lambda_N^2`$: 0.79% at $`N = 12`$, 0.30% at $`N = 20`$ and 0.14% at $`N = 30`$.

So the premise does not stand alone: intertwining forces it exactly, locality selects it as the closest positive match at every $`N`$, and the flat limit recovers it as $`N`$ grows. Positivity, covariance, reality and normalization do not. Neither intertwining nor locality is supplied here; each is a statement about the projection that the effective-metric construction would have to deliver.

## IV. What a width would do

Locality prefers no width, but only by the size of its own shortfall. A profile of width $`\sigma`$ in $`k`$ adds $`\mathrm{Var}(k^2) \approx 4\lambda_N \sigma^2`$ to the fourth-order mismatch, as much as the curvature's $`\tfrac43\lambda_N/R^2`$ at $`\sigma = 1/(\sqrt3 R)`$, whatever $`N`$: 4.5% of $`k_{12}`$, 2.8% of $`k_{20}`$ and 1.9% of $`k_{30}`$. Below that scale locality tells a width from none by less than the curvature's own mismatch.

The ratio table is more sensitive than that, and not where the landing sits. A width moves the first shell's landing by only $`\chi_* \sigma`$ in $`\ell`$: at $`\sigma = 1/(\sqrt3 R)`$, 1.3 at route A and 0.41 at route B, against landings at $`k_{12}\chi_* = 29.3`$ and 9.1. What it removes first is the phase. Below its landing a shell at a single wavenumber feeds $`C_\ell`$ through $`\Delta_\ell(k_N)^2`$, which at fixed $`k`$ oscillates in $`\ell`$. On the Sachs-Wolfe term well below the landing, $`j_\ell(x)^2 \approx \bigl(1 - (-1)^\ell \cos 2x\bigr)/(2x^2)`$ with $`x = k\chi_*`$, and averaging over a width multiplies the oscillating part by $`e^{-2(\chi_*\sigma)^2}`$. The recorded table carries that phase. Below its landing, the first shell's share of $`C_\ell`$ runs from 1.0% at $`\ell = 13`$ to 82% at $`\ell = 22`$ at route A, and from 1.7% at $`\ell = 5`$ to 84% at $`\ell = 7`$ at route B ([run 2](scripts/molien-ratio-table-runs/run-2/result_report.txt)). The phase keeps 90% only for $`\chi_*\sigma \le 0.23`$, a width of 0.78% of $`k_{12}`$ at route A and 2.5% at route B. At locality's scale it keeps 0.033 at route A and 0.72 at route B.

So the table's per-multipole structure below the first shell's landing rests on each shell's wavenumber being exact to within about $`0.2/\chi_*`$. Intertwining supplies that; locality alone does not, at route A. The labels are not expected to rest on it: they come mostly from the deficit below $`k_{12}`$, and a width of order $`1/R`$ keeps the power near $`k_{12}`$ rather than filling that deficit; that is not computed. This bears on the table's second assumption, that the translation keeps each shell's wavenumber, whose consequences its §8 says the table computes without testing; it changes no recorded number.

## V. What this leaves

MIT's projection, whatever it is, induces a point of this family, and so owes two answers: where in $`k`$ each shell's power goes, and which directional point it induces at each $`k`$, the directional page's question, now asked pointwise in $`k`$. If the projection intertwines the Laplacians, the radial answer is exact placement and the ratio table's premise holds as computed. If it is only local, the placement is right on average, and the table's per-multipole structure at route A is not protected. [The Stress-Tensor Bridge](stress-tensor-bridge.md) carries this as C8: a candidate must declare which spectral operator, if any, it intertwines.

Not computed: the ratio table under any width, since a different source-to-sky map enters only in its own registration, before any computation ([the ratio table](molien-ratio-table.md) §6); what mixing shells would do; and which transfer MIT's projection induces.

## VI. Checks

[`radial_check.py`](scripts/radial-transfer/radial_check.py) needs sympy, numpy and scipy, and its record [`radial_check.out`](scripts/radial-transfer/radial_check.out) reproduces byte for byte from it. It checks the two Pizzetti identities exactly, on the whole-shell kernel for symbolic $`N`$ and on anisotropic shell functions at $`N = 3`$, 4 and 12; the fourth-order shortfall's minimum; the figures above; and the phase's damping, exactly by quadrature and on $`j_\ell(x)^2`$ at route A's first shell, with the first shell's shares read from run 2's record, whose SHA-256 it prints. Four mutation arms turn it red: a function off the shell, a wrong curvature coefficient, the shortfall's sign reversed, and the wrong damping law.

---

/ **[`↑top`](#top)** / **[`main`](https://github.com/dmobius3/mode-identity-theory/tree/main/)** / **[`framework`](/files/framework/)** / **[`bedrock`](/files/framework/files/bedrock/)** / **[`working`](/files/framework/files/working/)** / **[`cosmos`](/files/cosmos/)** / **[`spectrum`](/files/spectrum/)** / **[`tools`](/files/tools/)** /
