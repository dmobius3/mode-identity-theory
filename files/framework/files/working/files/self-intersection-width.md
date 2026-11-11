<a id="top"></a>
| **[`main`](https://github.com/dmobius3/mode-identity-theory/tree/main/)** | **[`framework`](/files/framework/)** | **[`bedrock`](/files/framework/files/bedrock/)** | **[`dynamics`](/files/framework/files/dynamics/)** | **[`working`](/files/framework/files/working/)** | **[`cosmos`](/files/cosmos/)** | **[`spectrum`](/files/spectrum/)** | **[`tools`](/files/tools/)** |

---

# The First Self-Intersection Width

**Type:** Result
**State:** Closed
**Status (2026-11-10):** Derived. Place the unbent conic carrier $`M(W)`$ in $`\mathbb{RP}^3`$ at any pose, and let $`W_*`$ be the width at which its image in $`S^3/2I`$ first meets itself. It is the least, over the 31 icosahedral axes, of an explicit entry width (Proposition 1). At every pose $`W_* \le \tfrac12\arctan(3 - \sqrt5)\,R \approx 0.326\,R`$, with equality exactly at 30 double lunes, each the lift of the narrower conic band of the projective carrier's Proposition 3.2 for an adjacent three-fold and five-fold pair of axes (Theorem 3). The bound's proof uses two axes, seven numerical comparisons certified in interval arithmetic, and an exact computation at the extremal pose. The result selects no pose and caps no width: the carrier's physical domain is $`\mathbb{RP}^3`$ by the ruling of 2026-10-02, and $`W_*`$ is a property of the observation map. Its symmetry strata are not classified.
**Summary:** The width at which the unbent conic carrier's image in $`S^3/2I`$ first meets itself, as a function of the carrier's pose, and its maximum over poses.
**Inputs:** `projective-carrier.md` (§I, Proposition 0.4; §IV, Proposition 3.2; §XI 1f), `scripts/self-intersection-width/`
**Parent:** `projective-carrier.md`

---

RESULT, a derivation with no pre-committed pass condition. [The Projective Carrier](projective-carrier.md#i-the-projective-layer)'s Proposition 0.4 shows that at every pose the unbent carrier's image in $`S^3/2I`$ meets itself before the width reaches $`\pi R/2`$. This page computes the width at which it first does so, at every pose, and the largest value that width takes. Each statement carries its hypotheses on its face, and §VI lists the scripts that check them.

**Related:** [The Projective Carrier](projective-carrier.md), [The Carrier's Edge Regimes](carrier-edge-regimes.md), [The Lipschitz Comparison](lipschitz-comparison.md).

## I. The Setting

As in Proposition 0.4's proof, write $`S^3(R)`$ as $`R`$ times the unit quaternions, with $`2I`$ acting by left multiplication, and let $`\Sigma`$ be the great sphere of purely imaginary quaternions, so that $`qp = -\langle q, p\rangle + q \times p`$ for unit $`p, q \in \Sigma`$. Lengths below are on the unit sphere: a width $`W`$ on the sphere of radius $`R`$ enters as $`W/R`$.

A *pose* is an orthonormal pair $`(N, e)`$ in $`\Sigma`$: $`\pm N`$ are the double lune's vertices, and $`e`$ is the point where the core crosses the lune's equator. Put $`b = N \times e`$, and write $`x_e, x_b, x_N`$ for the components of $`x \in \Sigma`$ in the frame $`(e, b, N)`$. For a unit vector $`n`$ let $`G_n = \Sigma \cap n^\perp`$, the great circle orthogonal to $`n`$. The core's lift lies on $`G_b`$, which is the $`G_0`$ of Proposition 0.4, and the longitude $`\delta(x) \in [0, \pi/2]`$ of a point $`x \ne \pm N`$ from it has $`\tan\delta = \lvert x_b\rvert/\lvert x_e\rvert`$, with $`\delta = \pi/2`$ where $`x_e = 0`$. So with $`T = \tan(W/R)`$ the double lune is

```math
D(W) = \lbrace x \in \Sigma : \lvert x_b\rvert \le T\,\lvert x_e\rvert \rbrace, \qquad 0 < W < \pi R/2,
```

and the carrier is $`M(W) = D(W)/\lbrace\pm 1\rbrace`$. Two of its points have one image in $`S^3/2I`$ exactly when two points of $`D(W)`$, not related by $`\pm 1`$, lie in one $`2I`$-orbit, and $`W_*`$ is the infimum of the widths at which that happens. The infimum is attained unless it is $`0`$.

An *axis* is a line $`\mathbb{R}n`$, $`n \in \Sigma`$, such that $`2I`$ has an element other than $`\pm 1`$ in the span of $`1`$ and $`n`$. There are 31, the rotation axes of the icosahedral group that $`2I`$ covers: 15 two-fold, 10 three-fold and 6 five-fold. The elements of $`2I`$ on an axis of order $`m`$ are $`\cos(\pi j/m) + \sin(\pi j/m)\,n`$ for $`j = 0, \dots, 2m - 1`$. Write $`c_m = \cot(\pi/m)`$, so $`c_2 = 0`$, $`c_3 = 1/\sqrt3`$ and $`c_5 = \cot(\pi/5)`$. A three-fold axis and a five-fold axis are *adjacent* when the angle between them is the least one such a pair makes, $`\theta = \arctan(3 - \sqrt5) \approx 37.3774^\circ`$.

## II. The Statement

**Proposition 1 (DERIVED).** For an axis $`n`$ of order $`m`$ put

```math
T(n) = \frac{1 - n_b^2}{\sqrt{c_m^2\,n_N^2 + (1 - n_e^2)(1 - n_b^2)} + c_m\lvert n_N\rvert},
```

with $`T(n) = 0`$ for $`n = \pm b`$ and $`T(n) = \infty`$ for $`n = \pm e`$, the two cases in which the quotient is $`0/0`$ or $`1/0`$. Then at every pose

```math
W_*(N, e) = R\,\min_n \arctan T(n),
```

the minimum over the 31 axes. Call $`R\arctan T(n)`$ the *entry width* of the axis. For a two-fold axis $`T(n) = \sqrt{(1 - n_b^2)/(1 - n_e^2)}`$.

**Theorem 3 (DERIVED).** At every pose

```math
W_* \le \tfrac12\arctan(3 - \sqrt5)\,R \approx 0.32618\,R,
```

which is $`\theta/2 \approx 18.6887^\circ`$ on the unit sphere. Equality holds exactly when $`b = \pm M`$ and $`N = \pm P`$, where $`a`$ (three-fold) and $`a'`$ (five-fold) are adjacent axes taken as unit vectors at the angle $`\theta`$, $`M`$ is the midpoint of the arc between them, and $`P`$ is the unit normal of their plane, a two-fold axis. The edges of $`D(W)`$ at that width lie on $`G_a`$ and $`G_{a'}`$. There are 30 such double lunes, one for each adjacent pair of axes, and they form one orbit of the icosahedral rotation group.

## III. The Function

**Lemma A.** Let $`p, q \in \Sigma`$ with $`q \ne \pm p`$. Then $`q = gp`$ for some $`g \in 2I`$ exactly when some axis $`n`$ of order $`m`$ is orthogonal to both and the angle from $`p`$ to $`q`$ is a multiple of $`\pi/m`$.

*Proof.* The equation $`q = gp`$ forces $`g = -qp = \langle p, q\rangle + p \times q`$: its real part is the cosine of the angle from $`p`$ to $`q`$, and its imaginary part lies along the normal of their plane. That is an element of $`2I`$ exactly under the stated condition. ∎

**Lemma B.** For an axis $`n`$ of order $`m`$ and $`T > 0`$ put

```math
Q_n(T) = (1 - n_b^2) - (1 - n_e^2)\,T^2 - 2c_m\lvert n_N\rvert\,T .
```

Then $`D(W)`$, with $`T = \tan(W/R)`$, contains two points of $`G_n`$, not related by $`\pm 1`$, one carried to the other by an element of $`2I`$ on the axis $`n`$, exactly when $`Q_n(T) \le 0`$.

*Proof.* Put $`A^2 = 1 - n_e^2`$ and $`B^2 = 1 - n_b^2`$. If $`B = 0`$ then $`G_n`$ is the core's circle, inside every $`D(W)`$, and $`Q_n = -T^2 < 0`$. If $`A = 0`$ then $`x_e = 0`$ on $`G_n`$, so $`G_n`$ meets $`D(W)`$ only in $`\pm N`$, and $`Q_n = 1`$. Otherwise the restrictions of $`x_b`$ and $`x_e`$ to $`G_n`$ are $`B \sin s`$ and $`A \cos(s - \varsigma)`$ in a suitable arc length $`s`$, with $`\cos\varsigma = \lvert n_N\rvert/(AB)`$, because the projections of $`b`$ and $`e`$ to the plane orthogonal to $`n`$ have lengths $`B`$ and $`A`$ and inner product $`-n_b n_e`$, and $`A^2B^2 - n_b^2n_e^2 = n_N^2`$. So on $`G_n`$

```math
\frac{x_b}{x_e} = k\,\frac{\sin s}{\cos(s - \varsigma)}, \qquad k = B/A .
```

If $`n_N = 0`$ this ratio is the constant $`\pm k`$ and $`G_n`$ passes through $`\pm N`$: it lies in $`D(W)`$ when $`T \ge k`$ and meets it only in $`\pm N`$ otherwise, and $`Q_n = B^2 - A^2T^2`$. If $`n_N \ne 0`$ the ratio increases from $`-\infty`$ to $`\infty`$ over each half turn, so $`G_n`$ meets $`D(W)`$ in an arc from $`s_-`$ to $`s_+`$ about $`s = 0`$, where the ratio is $`\mp T`$, and in its antipode. Replacing a point by its antipode, a pair of the lemma lies in that arc at a separation that is a multiple of $`\pi/m`$, so one exists exactly when $`\ell = s_+ - s_- \ge \pi/m`$. From $`k \sin s_\pm = \pm T\cos(s_\pm - \varsigma)`$,

```math
\cot \ell = \frac{k^2 - T^2}{2kT\cos\varsigma},
```

and the cotangent decreases on $`(0, \pi)`$, where $`\ell`$ lies. Hence $`\ell \ge \pi/m`$ exactly when $`\cot\ell \le c_m`$, that is $`k^2 - T^2 - 2kTc_m\cos\varsigma \le 0`$, which is $`Q_n(T) \le 0`$ after multiplying by $`A^2`$. ∎

*Proof of Proposition 1.* By Lemma A, two points of $`\Sigma`$ in one orbit, not related by $`\pm 1`$, lie on some $`G_n`$, and an element on the axis $`n`$ carries one to the other. So by Lemma B, $`W_*/R`$ is the infimum of the $`W/R`$ at which $`Q_n(\tan(W/R)) \le 0`$ for some axis. Each $`Q_n`$ decreases in $`T \ge 0`$ from $`Q_n(0) = 1 - n_b^2 \ge 0`$, strictly unless $`n = \pm e`$, where it is constantly $`1`$ and has no root, which is $`T(n) = \infty`$. Otherwise its one non-negative root is $`T(n)`$: it is $`0`$ at $`n = \pm b`$, and elsewhere it is the positive root of $`(1 - n_e^2)\,T^2 + 2c_m\lvert n_N\rvert\,T - (1 - n_b^2) = 0`$, which is the displayed quotient. ∎

**Corollary 2.** $`T(n) \le \tan\angle(n, b)`$, with equality exactly when $`n \perp N`$: for $`n_b \ne 0`$, at $`T = \tan\angle(n, b)`$, $`Q_n = -(1 - n_b^2)\,n_N^2/n_b^2 - 2c_m\lvert n_N\rvert\,T \le 0`$; for $`n_b = 0`$ the right side is infinite. So $`W_*/R`$ is at most the angle from $`b`$ to the nearest axis.

**Lemma C.** Fix $`W_0 \in (0, \pi/2)`$ and $`t_0 = \tan W_0`$, and let $`d = \angle(n, b) \in [0, \pi/2]`$. Then $`T(n) \ge t_0`$ exactly when $`Q_n(t_0) \ge 0`$, which after multiplying by $`\cos^2 W_0`$ reads

```math
\sin^2 d - \sin^2 W_0 \;\ge\; \sin^2 W_0\; n_N^2 + c_m\sin(2W_0)\,\lvert n_N\rvert .
```

In particular $`d \ge W_0`$, and for $`c_m > 0`$, $`\lvert n_N\rvert \le (\sin^2 d - \sin^2 W_0)/(c_m \sin 2W_0)`$.

## IV. The Maximum

From here on $`W_0 = \theta/2`$ and $`t_0 = \tan W_0`$.

*Proof of Theorem 3.* The fifteen planes orthogonal to the two-fold axes cut $`\Sigma`$ into 120 triangles with angles $`\pi/2`$, $`\pi/3`$ and $`\pi/5`$ at a two-fold, a three-fold and a five-fold axis point. Let $`\Delta`$ be a closed one containing $`b`$, with three-fold vertex $`a`$ and five-fold vertex $`a'`$; its side $`aa'`$ has length $`\theta = 2W_0`$. Suppose $`T(a) \ge t_0`$ and $`T(a') \ge t_0`$. It is enough to show that $`b = M`$ and $`N = \pm P`$.

Let $`d = \angle(b, a)`$ and $`d' = \angle(b, a')`$. Both are at most $`\theta`$, since the disc of radius $`\theta < \pi/2`$ about either vertex is convex and contains the three vertices. By Lemma C, $`d, d' \ge W_0`$. In the triangle with vertices $`a`$, $`b`$, $`a'`$ let $`\gamma`$ be the angle at $`b`$, and $`\omega \le \pi/3`$, $`\omega' \le \pi/5`$ the angles at $`a`$ and $`a'`$, which are at most those of $`\Delta`$ because $`b \in \Delta`$. Put $`\sigma = d + d' - \theta \ge 0`$.

**Step 1, the two distances.** The cosine rule at $`a'`$ gives $`\cos d \ge h_5(d')`$ with $`h_5(x) = \cos\theta\cos x + \cos(\pi/5)\sin\theta\sin x`$, and at $`a`$ it gives $`\cos d' \ge h_3(d)`$ with $`h_3(x) = \cos\theta\cos x + \tfrac12\sin\theta\sin x`$. Both functions are positive on $`[0, \pi/2]`$ and satisfy $`h'' = -h`$, so they are concave there and least at an end of an interval. Since $`h_5(W_0) < h_5(\theta)`$ **(a)**, $`d \le d_{\max} = \arccos h_5(W_0) \approx 24.478^\circ`$. Since $`h_3(d_{\max}) < h_3(W_0)`$ **(b)**, $`d' \le d'_{\max} = \arccos h_3(d_{\max}) \approx 31.897^\circ`$.

**Step 2, the two windows.** Let $`\vartheta`$ and $`\vartheta'`$ be the angles at $`b`$ between $`N`$ and the arcs from $`b`$ to $`a`$ and to $`a'`$. Since $`N \perp b`$, $`a_N = \sin d\cos\vartheta`$ and $`a'_N = \sin d'\cos\vartheta'`$, and Lemma C gives $`\lvert\cos\vartheta\rvert \le \xi_3(d)`$ and $`\lvert\cos\vartheta'\rvert \le \xi_5(d')`$, where

```math
\xi_m(x) = \frac{\sin^2 x - \sin^2 W_0}{c_m \sin\theta\,\sin x}
```

increases with $`x`$. With $`\xi_3(d_{\max}) < 1`$ and $`\xi_5(d'_{\max}) < 1`$ **(c)**, set $`\beta = \arcsin\xi_3(d)`$, $`\beta' = \arcsin\xi_5(d')`$ and $`\bar\beta = \arcsin\xi_3(d_{\max}) + \arcsin\xi_5(d'_{\max}) \approx 0.90648`$, so that $`\beta + \beta' \le \bar\beta`$. In the tangent plane at $`b`$ the two arcs leave at the angle $`\gamma`$ from each other, and $`N`$ is within $`\beta`$ of perpendicular to the first and within $`\beta'`$ of perpendicular to the second. Hence $`\min(\gamma, \pi - \gamma) \le \beta + \beta'`$.

**Step 3, which side.** The angles of a spherical triangle sum to at least $`\pi`$, so $`\gamma \ge \pi - \pi/3 - \pi/5 = 7\pi/15 > \bar\beta`$ **(1)**. Hence $`\pi - \gamma \le \beta + \beta'`$.

**Step 4, the angle between the arcs.** The cosine rule at $`b`$ gives $`\sin d\sin d'\,(1 + \cos\gamma) = \cos\theta - \cos(d + d') = 2\sin(\theta + \sigma/2)\sin(\sigma/2)`$. With $`\sin d\sin d' \le \sin^2(W_0 + \sigma/2)`$ and $`\sin(\theta + \sigma/2)\sin(\sigma/2) = \sin^2(W_0 + \sigma/2) - \sin^2 W_0`$,

```math
\sin\frac{\gamma}{2} \le \frac{\sin W_0}{\sin(W_0 + \sigma/2)}, \qquad\text{so}\qquad \pi - \gamma \;\ge\; g(\sigma) := 2\arccos\frac{\sin W_0}{\sin(W_0 + \sigma/2)} .
```

Here $`g(0) = 0`$, and $`g'(\sigma) = \sin W_0\cos y / \big(\sin y\,\sqrt{\sin^2 y - \sin^2 W_0}\big)`$ with $`y = W_0 + \sigma/2`$ is positive and decreasing while $`y < \pi/2`$. That holds on the whole range $`\sigma \le d_{\max} + d'_{\max} - \theta`$, where even $`\theta + \sigma/2 < \pi/2`$ **(3)**. So $`g`$ is increasing and concave on the range of $`\sigma`$.

**Step 5, the windows are too narrow.** Write $`d = W_0 + s`$ and $`d' = W_0 + s'`$, so that $`s + s' = \sigma`$. Since $`\sin(2W_0 + s)/\sin(W_0 + s)`$ decreases in $`s \ge 0`$,

```math
\xi_m(W_0 + s) = \frac{\sin s\,\sin(2W_0 + s)}{c_m\sin\theta\,\sin(W_0 + s)} \le \frac{s}{c_m \sin W_0} .
```

With $`\arcsin x \le \pi x/2`$ and $`c_5 > c_3 = 1/\sqrt3`$, $`\beta + \beta' \le \dfrac{\pi\sqrt3}{2\sin W_0}\,\sigma = \bar\beta\,\sigma/\sigma^*`$, where $`\sigma^* = 2\bar\beta\sin W_0/(\pi\sqrt3) \approx 0.10676`$, which lies inside the range of step 4 **(4)**. And $`g(\sigma^*) \approx 1.05200 > \bar\beta`$ **(2)**. If $`0 < \sigma \le \sigma^*`$, concavity gives $`g(\sigma) \ge g(\sigma^*)\,\sigma/\sigma^* > \bar\beta\,\sigma/\sigma^* \ge \beta + \beta'`$. If $`\sigma \ge \sigma^*`$, $`g(\sigma) \ge g(\sigma^*) > \bar\beta \ge \beta + \beta'`$. Either way $`\pi - \gamma > \beta + \beta'`$, against step 3. So $`\sigma = 0`$.

**Step 6, the pose.** With $`d, d' \ge W_0`$, $`\sigma = 0`$ gives $`d = d' = W_0`$ and puts $`b`$ on the arc $`aa'`$: $`b = M`$. Lemma C at $`d = W_0`$ leaves $`0 \ge \sin^2 W_0\,n_N^2 + c_m\sin\theta\,\lvert n_N\rvert`$ for $`n = a`$ and $`n = a'`$, so $`N`$ is orthogonal to both: $`N = \pm P`$. There $`T(a) = T(a') = t_0`$ by Corollary 2, and $`Q_n(t_0) \ge 0`$ for all 31 axes, with equality for ten of them, in exact arithmetic **(E)**. So $`W_* = W_0 R`$ at that pose. The edges of $`D(W)`$ at that width lie on the great circles through $`\pm N`$ orthogonal to the two directions at angle $`W_0`$ from $`b`$ in the plane orthogonal to $`N`$, and those directions are $`a`$ and $`a'`$. Changing the sign of $`N`$ or of $`e`$ does not change $`D(W)`$, so the pair fixes the pose up to those signs. Each of the 6 five-fold axes has 5 adjacent three-fold axes, which makes 30 pairs, and the icosahedral rotations permute them transitively and preserve $`W_*`$. ∎

## V. What It Settles, and What It Does Not

- **Proposition 0.4, sharpened.** Its $`W_* < \pi R/2`$ becomes $`W_* \le \tfrac12\arctan(3 - \sqrt5)\,R`$. At the pose of each of the 30 double lunes the image is embedded for every $`W < W_0 R`$, and at $`W_0 R`$ it first meets itself, along its edge. At every other pose it meets itself at a smaller width. So $`W_0 R`$ is the supremum of the widths at which the conic carrier's image embeds, and no pose attains it.
- **The band of Proposition 3.2.** The extremal band is the conic band of [Proposition 3.2](projective-carrier.md#iv-proposition-3-no-zero-bending-band-has-a-smooth-geodesic-edge) for an adjacent three-fold and five-fold pair, with $`2W/R = \theta`$ rather than $`\pi - \theta`$: its two edge loops are the projective lines that $`G_a`$ and $`G_{a'}`$ cover. Theorem 3 characterizes that member by a property of the observation map. It grounds no rule that would pick it.
- **It selects nothing and caps nothing.** Under the ruling of 2026-10-02 the carrier's physical domain is $`\mathbb{RP}^3`$, where it embeds at every width, and $`W_*`$ is a property of the observation map ([§XI, 1f](projective-carrier.md#xi-the-ruling)). That ruling asks that a rule using $`W_*`$ to choose a pose or a width have its own ground, declared before its values are computed. The values are computed here with no ground declared, so a rule that chose by $`W_*`$ would postdate them. This page evaluates no observable at the extremal pose or width.
- **What the proof uses.** Step 5 needs only $`c_3 > 0`$ and $`c_5 \ge c_3`$. The value of $`c_5`$ enters through $`\bar\beta`$, in comparisons (c), (1), (2) and (4). A scan shows that the bound itself survives lowering $`c_5`$ to $`c_3`$, though this proof's comparisons (1) and (2) would not. With the three-fold axis read as two-fold, $`c_3 = 0`$, the bound fails.
- **Open.** The symmetry strata of $`W_*`$ are not classified: the regions of the three-parameter family of poses on which a given axis sets the minimum, the walls between them, and any local maxima other than the global one. The question stands among the open problems of [CONTRIBUTING](/CONTRIBUTING.md).

## VI. Check

[`scripts/self-intersection-width/`](scripts/self-intersection-width/) holds three scripts, each with its recorded output beside it, and the SHA-256 of every other file in `SHA256SUMS` (Python 3.13.13, numpy 2.5.0, scipy 1.18.0, mpmath 1.3.0). Each script asserts its own checks, so a failed check stops it. Quantities at the roundoff level are printed as bounds, and the random poses come from numpy's legacy generator, whose stream does not change between versions. Run each from that folder, as `python3 -u w_star.py`.

- [`w_star.py`](scripts/self-intersection-width/w_star.py), with its record [`w_star.out`](scripts/self-intersection-width/w_star.out), checks Proposition 1 against the definition. At 120 random poses it minimizes the larger of the two longitudes over every element $`g`$ of $`2I`$ other than $`\pm 1`$ and every point $`p`$ with $`gp \in \Sigma`$, by quaternion multiplication alone. The two routes agree within $`10^{-12}`$ rad, and two mutated formulas, planted as arms, miss by a tenth of a radian. It then searches for the maximum from $`3 \times 10^6`$ random poses with 240 refinements and a grid over one triangle, and finds $`18.688684^\circ`$ with nothing above it. Last it samples $`W_*`$ over $`2 \times 10^6`$ Haar-random poses: the median is $`6.806^\circ`$, the 5% and 95% quantiles are $`2.170^\circ`$ and $`12.111^\circ`$, and the axis that sets the minimum is five-fold at 47.6% of poses, three-fold at 30.7% and two-fold at 21.7%.
- [`w_star_max.py`](scripts/self-intersection-width/w_star_max.py), with its record [`w_star_max.out`](scripts/self-intersection-width/w_star_max.out), builds the extremal pose from the axes and evaluates $`T(n)`$ for all 31 at 60 digits: the minimum agrees with $`\tan(\theta/2)`$ to $`10^{-55}`$, ten axes attain it, and the other 21 exceed it by at least 0.232. The definition gives the same width at that pose. It checks Corollary 2 on $`2 \times 10^6`$ poses and scans the directions for $`b`$ that Corollary 2 alone leaves open, $`7.5 \times 10^7`$ poses, finding nothing above the bound.
- [`w_star_proof.py`](scripts/self-intersection-width/w_star_proof.py), with its record [`w_star_proof.out`](scripts/self-intersection-width/w_star_proof.out), carries the checks the proof cites. Part E works in exact arithmetic in $`\mathbb{Q}(\sqrt5)(\cos\theta)`$: $`\tan\theta = 3 - \sqrt5`$; the triangle with vertices $`a`$, $`a'`$ and its two-fold vertex has a right angle there and the angles $`\pi/3`$ and $`\pi/5`$ at $`a`$ and $`a'`$; and at $`b = M`$, $`N = P`$, $`Q_n(t_0) \ge 0`$ for all 31 axes, with equality for ten: 2 two-fold, 3 three-fold and 5 five-fold. Part I certifies comparisons (a), (b), (c) and (1) to (4) in 50-digit interval arithmetic. Part S scans the two-axis statement itself, the least of $`T(a)`$ and $`T(a')`$ over one triangle at $`8.2 \times 10^7`$ poses: its largest value is $`t_0`$, at $`M`$. Two mutations, planted as arms, exceed the bound as they must: the three-fold axis read as two-fold, and the five-fold axis replaced by the other one in the same plane. One control, $`c_5`$ lowered to $`c_3`$, leaves the bound in place. `python3 -u w_star_proof.py quick` runs parts E and I alone, in seconds.

---

| **[`↑top`](#top)** | **[`main`](https://github.com/dmobius3/mode-identity-theory/tree/main/)** | **[`framework`](/files/framework/)** | **[`bedrock`](/files/framework/files/bedrock/)** | **[`dynamics`](/files/framework/files/dynamics/)** | **[`working`](/files/framework/files/working/)** | **[`cosmos`](/files/cosmos/)** | **[`spectrum`](/files/spectrum/)** | **[`tools`](/files/tools/)** |
