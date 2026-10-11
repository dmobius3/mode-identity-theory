<a id="top"></a>
/ **[`main`](https://github.com/dmobius3/mode-identity-theory/tree/main/)** / **[`framework`](/files/framework/)** / **[`bedrock`](/files/framework/files/bedrock/)** / **[`dynamics`](/files/framework/files/dynamics/)** / **[`working`](/files/framework/files/working/)** / **[`cosmos`](/files/cosmos/)** / **[`spectrum`](/files/spectrum/)** / **[`tools`](/files/tools/)** /

---

# The Volume Cap

**Type:** Result
**State:** Closed
**Status (2026-10-11):** Derived under a declared convention, checked by one script. A point map from a flat ball into $`S^3/2I`$ that is locally Lipschitz, injective almost everywhere and never compresses volume needs the ball's volume to be at most the domain's. With the ball in today's comoving lengths and the domain at radius $`\Omega_0 R`$, that caps the ball's radius at $`(\pi/80)^{1/3}\,\Omega_0 R \approx 0.3399\,\Omega_0 R`$, and at $`(3\pi/2)^{1/3}\,\Omega_0 R \approx 1.6765\,\Omega_0 R`$ on the cover $`S^3`$. The flat dictionary's ball out to $`z = 2.33`$, of radius 5.77 Gpc at the anchor's $`H_0`$ and 5.32 Gpc at SH0ES's, exceeds the quotient's cap at the readings A (6.13 Gpc) and C (10.5 Gpc) in both rows, and fits at B (19.7 Gpc). For maps in the class, $`\Omega_0 R \ge 16.96`$ Gpc at the anchor's $`H_0`$ and 15.64 Gpc at SH0ES's. The convention is declared, not derived, and covers point maps only: the field-to-field projection the bridge seeks does not inherit the cap.
**Summary:** How large a flat ball can sit point by point in the static domain without overlapping itself or compressing volume, and what that says at the radius readings on record. The second target the stress-tensor bridge named in its §X.
**Inputs:** `stress-tensor-bridge.md` (§VI, §X), `nonflat-distance-comparison.md` (§0, §2, Results), `missing-spatial-projection.md` (§III, §IV), `propagation-theorem.md` (§I), `scripts/volume-cap/volume_cap_check.py`
**Parent:** `stress-tensor-bridge.md`

---

RESULT, a derivation with no pre-committed pass condition, under a convention declared before it (§I). A locally Lipschitz point map from a flat ball into the static domain that neither overlaps itself nor compresses volume needs the ball's volume to be at most the domain's.
- [The stress-tensor bridge](stress-tensor-bridge.md) named this as a target (§X, 2026-10-09). This page proves it under the convention ruled 2026-10-11, and evaluates it at the radius readings on record.
- The cap constrains a family of point maps, declared in §I. It neither repeats nor strengthens [the nonflat distance comparison](nonflat-distance-comparison.md)'s exclusion (§III).
- The projection the bridge seeks is field to field, and does not inherit the cap (§IV).

**Related:** [The Stress-Tensor Bridge](stress-tensor-bridge.md), [The Nonflat Distance Comparison](nonflat-distance-comparison.md), [The Missing Spatial Projection](missing-spatial-projection.md), [The Propagation Theorem](propagation-theorem.md).

---

## I. The setting, and the declared convention

**The domain.** $`M = S^3/2I`$, with the round metric $`h`$ of curvature radius $`R`$, is the quotient of $`SU(2)`$ by $`2I`$ acting on the left ([The Propagation Theorem](propagation-theorem.md) §I). $`2I`$ has order 120 and acts freely by isometries, so at radius $`\rho`$ the domain's volume is $`2\pi^2\rho^3/120`$, a 120th of its cover's.

**The flat ball.** $`B_r`$ is the open ball of radius $`r`$ in $`\mathbb{R}^3`$, with the Euclidean metric. The ball of interest is the flat dictionary's region out to $`z = 2.33`$, DESI DR2's deepest BAO redshift, under the comparison's model in its flat limit at the published fit, $`\Omega_\Lambda = 0.685`$ and $`s_0 = 0.001`$ ([the comparison](nonflat-distance-comparison.md) §0 and §2):

```math
r = \frac{c}{H_0}\int_0^{2.33}\frac{dz}{E(z)}, \qquad E^2(z) = \frac{1-\Omega_\Lambda}{1-s_0^2}\left[(1+z)^3 - s_0^2(1+z)\right] + \Omega_\Lambda .
```

**The convention (ruled 2026-10-11).** It is declared, not derived.
- **The tie.** The ball is measured in today's comoving lengths. The domain carries $`\Omega_0^2 h`$, the round metric of radius $`\Omega_0 R`$ in today's comoving lengths, with $`\Omega_0 = 1`$ as the primary identification, as [the comparison](nonflat-distance-comparison.md) declared it (§0, ruled 2026-10-10). So the cap bounds $`\Omega_0 R`$, the quantity the comparison's data constrain, and cannot separate $`\Omega_0`$ from $`R`$.
- **The maps.** A point map $`\phi: B_r \to M`$ is in the class when it is locally Lipschitz, injective off a set of measure zero, and has volume Jacobian $`J_\phi \ge 1`$ almost everywhere, measured from the Euclidean metric to $`\Omega_0^2 h`$. Being locally Lipschitz, $`\phi`$ is differentiable almost everywhere, so $`J_\phi`$ is defined.
- **The scope.** Point maps only. Nothing here assumes that the projection the bridge seeks is a point map (§IV).

## II. The theorem

**Theorem.** If $`\phi: B_r \to M`$ is in the class of §I, then

```math
\frac{4}{3}\pi r^3 \le \frac{2\pi^2(\Omega_0 R)^3}{120}, \qquad\text{so}\qquad r \le \left(\frac{\pi}{80}\right)^{1/3}\Omega_0 R \approx 0.3399\,\Omega_0 R .
```

For a map into the cover $`S^3`$, with 1 in place of 120, the same statement gives $`r \le (3\pi/2)^{1/3}\,\Omega_0 R \approx 1.6765\,\Omega_0 R`$.

**Proof.** *Lift.* The ball is simply connected, so $`\phi`$ lifts through the covering $`S^3 \to M`$ to $`\tilde\phi: B_r \to S^3`$, where $`S^3 \subset \mathbb{R}^4`$ is the round sphere of radius $`\Omega_0 R`$. The covering is a local isometry, so $`\tilde\phi`$ is locally Lipschitz, hence Lipschitz on every closed sub-ball, with $`J_{\tilde\phi} = J_\phi`$ almost everywhere. The round metric is the one $`\mathbb{R}^4`$ induces, so the Euclidean Jacobian of $`\tilde\phi`$ as a map into $`\mathbb{R}^4`$ is $`J_\phi`$, and the three-dimensional Hausdorff measure $`\mathcal{H}^3`$ on $`S^3`$ is its volume.

*Disjoint translates.* Let $`A`$ be a set of full measure on which $`\phi`$ is injective. Points of $`A`$ have distinct images in $`M`$, so their lifts lie in distinct $`2I`$ orbits, and $`\tilde\phi(A)`$ meets each orbit at most once. Since $`2I`$ acts freely, the 120 translates of $`\tilde\phi(A)`$ are pairwise disjoint, and since it acts by isometries of $`\mathbb{R}^4`$, they have equal measure. So $`\mathcal{H}^3(\tilde\phi(A)) \le 2\pi^2(\Omega_0 R)^3/120`$.

*Area formula.* Fix $`s < r`$, and extend $`\tilde\phi`$ from the closed ball $`\bar B_s`$ to a Lipschitz map on $`\mathbb{R}^3`$, which changes nothing on $`B_s`$. The area formula for Lipschitz maps $`\mathbb{R}^3 \to \mathbb{R}^4`$ ([Evans and Gariepy](https://doi.org/10.1201/b18333)), with $`\tilde\phi`$ injective on $`A`$ and $`J_\phi \ge 1`$, gives

```math
\frac{4}{3}\pi s^3 \le \int_{A \cap B_s} J_\phi\,dx = \mathcal{H}^3\big(\tilde\phi(A \cap B_s)\big) \le \frac{2\pi^2(\Omega_0 R)^3}{120} .
```

Letting $`s \to r`$ gives the cap. With the trivial group in place of $`2I`$, the same steps give the cover's. ∎

**The contrapositive.** Past the cap, no point map keeps all three conditions of §I. A point map of the ball into the domain then overlaps itself on a set of positive measure, compresses volume ($`J_\phi < 1`$ on a set of positive measure), or is not locally Lipschitz; otherwise the realization is not a point map at all.

Below the cap the theorem is silent. It uses volume alone and constructs no map.

## III. At the readings on record

The flat ball's radius is 5.77 Gpc at the anchor's $`H_0 = 67.36`$ km/s/Mpc and 5.32 Gpc at SH0ES's 73.04, the comparison's two scale rows ([the comparison](nonflat-distance-comparison.md) §2); the integral is 1.2954. At the three radius readings on record, with $`\Omega_0 = 1`$, so that $`\Omega_0 R`$ is the reading:

| reading | $`R`$ | cap on $`S^3/2I`$ | ball volume over domain volume, anchor's $`H_0`$ | at SH0ES's |
|---|---|---|---|---|
| A | 6.13 Gpc | 2.08 Gpc | 21.19 | 16.62 |
| C | 10.5 Gpc | 3.57 Gpc | 4.22 | 3.31 |
| B | 19.7 Gpc | 6.70 Gpc | 0.64 | 0.50 |

- **A and C exceed the quotient's volume in both rows, and B fits in both.** At A and C, a locally Lipschitz point map of the ball into $`S^3/2I`$ that is injective almost everywhere and never compresses volume is impossible; any realization gives up at least one declared condition (§II). At B, volume does not exclude one.
- **The cover, for comparison.** On $`S^3`$ the ratios are 0.177 and 0.138 at A, 0.035 and 0.028 at C, and 0.005 and 0.004 at B, so the ball fits at every reading. What binds is the quotient's order, 120.
- **The bound form.** For maps in the class, $`\Omega_0 R \ge r/0.3399`$: 16.96 Gpc at the anchor's $`H_0`$ and 15.64 Gpc at SH0ES's. These are conditional geometric thresholds, not observational confidence limits. The ball is the flat dictionary's geometric region out to the deepest BAO redshift; SN+BAO sample directions and redshifts inside it, not every point of it.

**Beside the comparison.** Under the same tie the two results bound the same quantity. [The comparison](nonflat-distance-comparison.md)'s bound is $`\Omega_0 R \ge 15.2`$ Gpc at the anchor's $`H_0`$ and 14.0 Gpc at SH0ES's (nominal one-sided 95%, its Results). They constrain different families of realizations. The comparison's closed metric keeps the radial distance $`\chi`$ and shrinks the transverse one to $`\Omega_0 R\sin\big(\chi/(\Omega_0 R)\big)`$. Read as a map from the flat ball, it has volume Jacobian

```math
J(\chi) = \left[\frac{\sin\big(\chi/(\Omega_0 R)\big)}{\chi/(\Omega_0 R)}\right]^2 < 1 \qquad (\chi > 0),
```

so it compresses volume and lies outside the cap's class. The cap therefore neither repeats nor strengthens the comparison's exclusion: it constrains a different family of maps, declared in §I, and leaves the comparison's record as it stands.

## IV. What it does not close

- **The projection.** The projection the bridge seeks does not inherit the cap. [The Missing Spatial Projection](missing-spatial-projection.md)'s §III closes smooth pullbacks, and its §IV asks for a field-to-field map that is not one (the bridge's C9). The cap bounds point identifications of a flat effective description, and it reaches a candidate projection only through a point map the candidate carries. If the candidate pulls its fields back along that map, §III requires the map not to be smooth, since it closes smooth pullbacks of a nonconstant homogeneous law to a non-degenerate translation-homogeneous flat field, and the cap reaches the map only if it is also locally Lipschitz. Escaping §III does not establish a viable projection: a candidate must still meet, independently, the field-level requirements of that page's §IV.
- **Below the cap.** The theorem uses volume alone and constructs no map, so B's fit says only that volume does not exclude one.
- **Other ties.** The tie is declared. Another $`\Omega_0`$ moves only the target's radius, so the bound reads on $`\Omega_0 R`$. A tie made at another epoch, or through another scale standard, would bound a different radius.
- **Other maps.** Maps that overlap on a set of positive measure, compress volume somewhere, are not locally Lipschitz, or are not point maps lie outside the class.
- **The data.** The cap is not an observational limit. It does not re-grade the comparison or bear on its record.

## V. Bearing on the bridge

[The stress-tensor bridge](stress-tensor-bridge.md) adopts flat effective slices (§VI) and named this cap as a target (§X). For a flat effective description that identifies points of its slice with points of the domain, the cap gives (DERIVED, given the convention of §I):
- at A and C, the identification of the ball out to $`z = 2.33`$ overlaps itself, compresses volume, or gives up local Lipschitz regularity;
- at B, volume alone permits it.

The adopted flat dictionary stands: the cap constrains how its slice could be identified point by point with the domain, not the adoption. The convention ties scales for this theorem only, so the projection still owes its own comoving tie ([The Missing Spatial Projection](missing-spatial-projection.md) §IV, item 4).

## VI. Checks

[`volume_cap_check.py`](scripts/volume-cap/volume_cap_check.py) needs numpy and scipy, and its record [`volume_cap_check.out`](scripts/volume-cap/volume_cap_check.out) reproduces byte for byte from it. It checks the arithmetic the page carries; the theorem rests on the proof of §II. It checks:
- the caps, $`(\pi/80)^{1/3}`$ and $`(3\pi/2)^{1/3}`$, from $`\big(3\pi/(2\lvert G\rvert)\big)^{1/3}`$ at $`\lvert G\rvert = 120`$ and $`\lvert G\rvert = 1`$;
- the integral to $`z = 2.33`$ by adaptive quadrature, against the Λcos pipeline's own numerics, a 4000-point trapezoid on $`[0, 2.5]`$, to a relative $`10^{-6}`$;
- the volume ratios at the three readings in both rows: A and C exceed the quotient, B fits it, and all three fit the cover;
- the bound $`r/0.3399`$ in both rows, with A and C below it and B above.

Four mutation arms, one per check, each turn it red:
- the caps with $`\lvert G\rvert = 60`$;
- the pipeline's grid cut to 40 points;
- the readings A and B swapped;
- the bound with the cover's factor.

## References

- L. C. Evans and R. F. Gariepy, *Measure Theory and Fine Properties of Functions*, [revised edition, Chapman and Hall/CRC, 2015](https://doi.org/10.1201/b18333): Rademacher's theorem and the area formula for Lipschitz maps $`\mathbb{R}^n \to \mathbb{R}^m`$.

---

/ **[`↑top`](#top)** / **[`main`](https://github.com/dmobius3/mode-identity-theory/tree/main/)** / **[`framework`](/files/framework/)** / **[`bedrock`](/files/framework/files/bedrock/)** / **[`dynamics`](/files/framework/files/dynamics/)** / **[`working`](/files/framework/files/working/)** / **[`cosmos`](/files/cosmos/)** / **[`spectrum`](/files/spectrum/)** / **[`tools`](/files/tools/)** /
