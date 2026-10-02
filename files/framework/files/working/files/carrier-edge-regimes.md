<a id="top"></a>
/ **[`main`](https://github.com/dmobius3/mode-identity-theory/tree/main/)** / **[`framework`](/files/framework/)** / **[`bedrock`](/files/framework/files/bedrock/)** / **[`working`](/files/framework/files/working/)** / **[`cosmos`](/files/cosmos/)** / **[`spectrum`](/files/spectrum/)** / **[`tools`](/files/tools/)** /

---

# The Carrier's Edge Regimes

**Type:** Result
**State:** Closed
**Status (2026-10-01):** Derived, apart from §IV's two grounds: $`\Gamma = 0`$ (MOTIVATED, a reading of the bar) and keeping the conic band's own pinch (INFERRED); the listed identities and constructions are checked by script. With its edge free, the free-edged membrane energies the Tier 2 ground floor names do not select the unbent conic carrier $`M(W)`$, and the supported boundary does not on the totally geodesic support fitted to its edge. On unbent bands every energy of the free-edged membrane family without spontaneous curvature reduces to an effective sheet tension $`\Gamma`$ times area plus a line tension $`\sigma`$ times edge length. With line tension, the tension opens the cone point's pinch at first order at every width, so the carrier is not even a local minimizer; with the pinch held, the edge is geodesic only at $`\Gamma = 0`$, where the conic bands are the least-energy unbent bands, and with bending the least-energy bands for $`-2\kappa \le \bar\kappa \le 0`$, and $`W`$ is a flat direction. Without line tension, every unbent band ties at $`\Gamma = 0`$ and none is critical otherwise. On the two totally geodesic sheets through its edge lines, a support fitted to them, the carrier narrows for $`\Gamma > 0`$, widens for $`\Gamma < 0`$, and is flat in $`W`$ at $`\Gamma = 0`$; the framework supplies no support, and other supports stay open. The Λ seed forces a singular point that carries the twist, but neither the conic band's own pinch nor its geodesic laps; with the edge free, keeping that pinch is a further restriction, grounded on the carrier page only through the seed (INFERRED). The fixed edge of the carrier page's §IX stays the one regime here shown to hold the carrier stable with no null direction, for its declared class of variations, and there the edge is input.
**Summary:** Whether a variational regime with a movable edge selects the conic carrier: how the ground floor's regimes reduce on unbent bands, why line tension opens the pinch, what the supported boundary does, and what holding the pinch would and would not supply.
**Inputs:** `projective-carrier.md` (Lemma 0.1, Propositions 3, 3.1, 4.2 and 6, Corollary 2.1, Lemma 4, §IX, §XI 1b and 1c), `postulate-bridge.md` (the Tier 2 ground floor and the bar), `scripts/carrier-edge-regimes/`
**Parent:** `projective-carrier.md`

---

RESULT, a selection negative. The [projective carrier](projective-carrier.md)'s decision 1c asked whether the temporal edge is fixed data or is governed by one of the regimes the [Tier 2 ground floor](postulate-bridge.md#dynamical-direction) names: a supported boundary, line tension, or fourth-order bending of Willmore or Canham-Helfrich type. Here the unbent carrier is varied under each with its edge free. The free-edged energies select neither $`M(W)`$ nor $`W`$ in the full class the [bar](postulate-bridge.md#dynamical-direction) asks for, and do not supply 1b's geodesic edge there. The supported boundary does no better on the totally geodesic support fitted to the edge, and the framework supplies no other support. The Λ seed forces a singular point that carries the twist, not the geodesic laps (carrier Proposition 4.2).

**Related:** [The Projective Carrier](projective-carrier.md), [The Postulate Bridge](postulate-bridge.md), [The Tier 2 Fixed-Boundary Run](tier2-fixed-boundary.md), [First eigenvalue](../../bedrock/files/first-eigenvalue.md).

---

## I. The setting

$`R`$ is fixed throughout. An *unbent band* is a compact Möbius band $`M`$ that is a closed region of a totally geodesic $`\mathbb{RP}^2(R) \subset \mathbb{RP}^3(R)`$, with a piecewise-smooth edge whose only singular points are corners and two-sector pinches: the class of carrier Proposition 3. The conic band $`M(W)`$, $`0 < W < \pi R/2`$, is the double sector between two projective lines through its cone point $`p_c`$, with edge length $`2\pi R`$ and area $`4WR`$.

The energies form the free-edged membrane family

```math
E = \int_M \Big(\frac{\kappa}{2}H^2 + \bar\kappa K + \gamma\Big)\,dA + \sigma\,L(\partial M), \qquad \kappa, \sigma \ge 0,
```

with $`H = \mathrm{tr}\,A`$ and $`K`$ the Gauss curvature of the induced metric. Up to an overall coefficient it contains each energy the ground floor names, with the edge free:
- area with line tension, $`\kappa = \bar\kappa = 0`$;
- the bending energies of carrier Lemma 0.1, $`\int H^2`$ and $`\int\lvert A\rvert^2 = \int (H^2 - 2K + 2/R^2)`$;
- the two forms of the Willmore energy in $`S^3(R)`$, $`\int (H^2/4 + 1/R^2)`$ and $`\tfrac12\int\lvert \mathring A\rvert^2 = \int (H^2/4 - K + 1/R^2)`$, which differ on a band with an edge by the Gauss-Bonnet edge term;
- Canham-Helfrich without spontaneous curvature, with $`\kappa`$ and $`\bar\kappa`$ free.

Spontaneous curvature is left out. It needs a normal, which a Möbius band has only where its smooth locus is orientable; where it is defined, $`H_0 \neq 0`$ makes bending act at first order, since a normal bump $`\varphi\nu`$ changes $`E`$ by a nonzero multiple of $`(\kappa H_0/R^2)\int\varphi\,dA`$, so no unbent band is critical.

Two classes of competitors:
- the *full class*: every unbent band, with the edge moving freely in $`\mathbb{RP}^2`$, corners free to be cut and pinches to be resolved, tubes admitted and $`W`$ free;
- the *pinched class*: the bands of carrier Proposition 3.1, with one pinch formed by collapsing a transverse fibre and a core generating $`\pi_1(\mathbb{RP}^2)`$, the pinch kept while its position, the laps and $`W`$ vary.

In either class, with bending, the competitors also include the normal variations into $`\mathbb{RP}^3`$, smooth on the smooth locus and continuous up to the edge, which keep the core generating $`\pi_1(\mathbb{RP}^3)`$; in the pinched class they keep the pinch.

A band $`M`$ is *critical* in a class when no admissible family $`M_\varepsilon`$, $`\varepsilon \ge 0`$, that moves it by $`O(\varepsilon)`$ in Hausdorff distance, as the cuts of Lemma 3 do, has $`E(M_\varepsilon) \le E(M) - c\varepsilon`$ for some $`c > 0`$; for a smooth two-sided family that is $`\delta E = 0`$. The clarified bar tests stability on the full class: "Stability is tested on every admissible variation". It adds: "A restriction on the admissible variations counts only when the postulate motivates it and it is declared before the computation, never because it rescues a candidate."

## II. The reduction

**Lemma 1 (DERIVED).** On an unbent band $`A = 0`$, so $`H = 0`$ and, by Gauss's equation (carrier Lemma 0.1), $`K = 1/R^2`$. Hence

```math
E = \Gamma\,\mathrm{Area}(M) + \sigma\,L(\partial M), \qquad \Gamma = \gamma + \frac{\bar\kappa}{R^2},
```

and bending does not change $`E`$ at first order: under a normal variation $`\varphi\nu`$ the area element changes by $`-H\varphi\,dA = 0`$, $`H^2`$ and $`K - 1/R^2 = \det A`$ are quadratic in $`A`$, and the edge length does not change at first order either, since the edge's curvature vector and the rays at its corners and pinches lie in $`\mathbb{RP}^2`$, orthogonal to $`\nu`$.

$`\Gamma`$ is the energy density of an unbent sheet, its effective sheet tension, which can vanish while $`\gamma \neq 0`$. It vanishes for $`\int H^2`$, $`\int\lvert A\rvert^2`$ and $`\tfrac12\int\lvert\mathring A\rvert^2`$; it is $`\gamma`$ for area, $`1/R^2`$ for $`\int(H^2/4 + 1/R^2)`$, and $`\bar\kappa/R^2`$ for Canham-Helfrich without surface tension, each times the energy's coefficient.

**Lemma 2 (DERIVED; the edge law).** Move a smooth arc of the edge within $`\mathbb{RP}^2`$ with outward normal speed $`V`$. Then

```math
\delta E = \int (\Gamma + \sigma k_g)\,V\,ds,
```

with $`k_g`$ the arc's geodesic curvature, positive where it curves toward $`M`$. A smooth arc of a critical edge therefore has $`\sigma k_g = -\Gamma`$: it is geodesic exactly when $`\Gamma = 0`$, and otherwise it has constant geodesic curvature $`-\Gamma/\sigma`$. Without line tension the edge carries no force of its own: for $`\Gamma \neq 0`$ no unbent band is critical, and for $`\Gamma = 0`$ every unbent band has $`E = 0`$.

**Lemma 3 (DERIVED; corners).** Let two geodesic arcs of the edge meet at a point at angle $`\theta < \pi`$ on one side. Replacing their legs of length $`\varepsilon`$ on that side by the geodesic chord shortens the edge by $`2\varepsilon\big(1 - \sin(\theta/2)\big) + O(\varepsilon^3)`$, and adds or removes the chord's triangle, of area $`\tfrac12\varepsilon^2\sin\theta + O(\varepsilon^4)`$. For curved arcs the remainders are $`O(\varepsilon^2)`$ and $`O(\varepsilon^3)`$. Either way, for $`\sigma > 0`$ a critical edge has no corner that the class allows to be cut, whatever $`\Gamma`$, $`\kappa`$ and $`\bar\kappa`$.

**The pinch (DERIVED).** At $`p_c`$ the edge of $`M(W)`$ passes twice. Each pass runs from one of the two projective lines to the other across a complementary sector of opening $`\pi - 2W/R`$, so it is a corner with $`\theta = \pi - 2W/R`$ on the complement's side, and line tension pulls it into that sector with force $`2\sigma\sin(W/R)`$. Cutting it adds the chord's triangle to the band. The closure of the complement of $`M(W)`$ is the complementary double sector, a lune whose two vertices are identified at $`p_c`$; with one vertex cut off it is a closed disc. So the cut band is $`\mathbb{RP}^2`$ minus an open disc: a Möbius band of carrier Proposition 3's class whose core generates $`\pi_1`$, with that pass resolved and a reflex corner left at $`p_c`$ by the other. By Lemma 3,

```math
\Delta E = -2\sigma\varepsilon\Big(1 - \cos\frac{W}{R}\Big) + \frac{\Gamma\varepsilon^2}{2}\sin\frac{2W}{R} + O(\varepsilon^3),
```

negative for small $`\varepsilon`$ at every $`W`$. Bending cannot offset it: the cut stays in $`\mathbb{RP}^2`$, where only $`\Gamma`$ and $`\sigma`$ act (Lemma 1).

## III. What the regimes select

**Proposition 1 (DERIVED).**
1. *Line tension, full class.* For $`\sigma > 0`$, $`E`$ falls at first order along an admissible family through every conic band, cutting either pass, at any $`W`$ and for any $`\kappa`$, $`\bar\kappa`$ and $`\gamma`$. So no conic band is critical or a local minimizer. For $`\Gamma = 0`$ the infimum of $`E`$ over unbent bands is $`0`$, approached by tubes about a projective line whose edge, of length $`2\pi R\cos(W/R)`$, shrinks to a point, and not attained.
2. *Line tension, pinched class, $`\Gamma \neq 0`$.* No band is critical. By Lemmas 2 and 3 a critical lap would have no corner off the pinch and constant geodesic curvature $`-\Gamma/\sigma \neq 0`$, so it would lift to an arc of a circle that is not a great circle, running from a lift of the pinch to its antipode, and such a circle contains no antipodal pair.
3. *Line tension, pinched class, $`\Gamma = 0`$.* Every conic band is critical. Its laps are geodesic. The pinch is in balance: each edge line runs straight through $`p_c`$, so the two passes pull with opposite forces $`2\sigma\sin(W/R)`$. Moving $`p_c`$, turning the lines about it or changing $`W`$ leaves $`E = 2\pi R\sigma`$, and bending acts only at second order (Lemma 1). That value is the least energy among the unbent bands of the class (carrier Proposition 3.1). With bending admitted and $`-2\kappa \le \bar\kappa \le 0`$ it is the least among the class's bent competitors too, whose cores still generate $`\pi_1(\mathbb{RP}^3)`$ (§I): the density $`\tfrac{\kappa}{2}H^2 + \bar\kappa\det A`$ is then nonnegative, and each of the edge's two loops at the pinch is homotopic to the core, so non-contractible in $`\mathbb{RP}^3`$ and of length at least $`\pi R`$. For $`-2\kappa \le \bar\kappa < 0`$ the conic bands are the only bands that attain it. Inside the window the density is positive definite in $`A`$, so equality needs $`A = 0`$. At $`\bar\kappa = -2\kappa`$ it is $`\tfrac{\kappa}{2}(k_1 - k_2)^2`$, so equality needs a totally umbilic smooth locus; one sheet of its lift then lies in a round sphere $`\{\langle y, m\rangle = c\}`$ of $`S^3`$, whose closure holds a lap's lift from a lift of the pinch to its antipode, so $`c = 0`$ and again $`A = 0`$. Carrier Proposition 3.1's equality case then makes the band conic. Of the named energies, $`\int\lvert A\rvert^2`$ lies inside the window and $`\tfrac12\int\lvert\mathring A\rvert^2`$ at its lower end; $`\int H^2`$ lies at its upper end, $`\bar\kappa = 0`$, where other minimizers are not excluded here.
4. *The width.* Along the family $`dE/dW = 4R\,\Gamma`$, since the area is $`4WR`$. Where the family is critical, at $`\Gamma = 0`$, $`W`$ is an exactly flat direction that is not a symmetry, so under the bar it is a declared modulus, and no member is selected.
5. *No line tension.* For $`\sigma = 0`$ and $`\Gamma \neq 0`$ no unbent band is critical (Lemma 2). For $`\sigma = 0`$ and $`\Gamma = 0`$ every unbent band has $`E = 0`$. For $`-2\kappa \le \bar\kappa \le 0`$ every band has $`E \ge 0`$, so every unbent band, $`M(W)`$ among them, is a least-energy band, with its whole edge, its pinch and $`W`$ free at no cost; outside that window the density takes both signs. Nothing is selected either way.

**Proposition 2 (DERIVED; supported boundary).** Let $`\ell_\pm`$ be the edge lines of $`M(W)`$, and $`S_\pm`$ the totally geodesic projective plane through $`\ell_\pm`$ orthogonal to the band's $`\mathbb{RP}^2`$; the two cross along the projective line normal to the band at $`p_c`$. Let the edge slide on $`S = S_+ \cup S_-`$, with the pinch on that crossing. Then:
1. $`M(W)`$ is critical for every energy of the family. In-plane motions of the edge leave $`S`$, and motions along the normal have zero first variation (Lemma 1; the laps are geodesic).
2. Turn the band's plane by $`t`$ in the plane of $`c`$ and its normal $`\nu`$, where $`c`$ is the core's point farthest from $`p_c`$, or in the plane of $`d`$ and $`\nu`$, where $`d`$ is the point of the band's $`\mathbb{RP}^2`$ at distance $`\pi R/2`$ from both. Each turned plane meets $`S_\pm`$ in projective lines through $`p_c`$, and between them lies a conic band with its pinch at $`p_c`$ and its laps on $`S_\pm`$: $`M(W_t)`$ with $`\tan(W_t/R) = \cos t\,\tan(W/R)`$ for the first turn, $`M(W'_t)`$ with $`\tan(W'_t/R) = \tan(W/R)/\cos t`$ for the second. These bands are unbent, so along them $`E = 4\Gamma R W_t + 2\pi R\sigma`$, or the same with $`W'_t`$, whose second derivative at $`t = 0`$ is $`-2\Gamma R^2\sin(2W/R)`$ for the first turn and $`+2\Gamma R^2\sin(2W/R)`$ for the second.

So on $`S`$ the carrier is unstable at every width for every $`\Gamma \neq 0`$: it narrows for $`\Gamma > 0`$ and widens for $`\Gamma < 0`$. At $`\Gamma = 0`$ both turns are exactly flat and $`W`$ is again a modulus. The turns' velocities at $`t = 0`$ are the normal fields $`x_c\,\nu`$ and $`x_d\,\nu`$, the normal parts of the rotations in the planes of $`c`$ and $`\nu`$ and of $`d`$ and $`\nu`$ (carrier Lemma 4). The support is fitted to $`M(W)`$'s own edge lines, so it is input, as the fixed edge is. For area it is the one totally geodesic support on which $`M(W)`$ is critical, since a free edge on a support must meet it orthogonally.

*Proof of 2.* In $`\mathbb R^4`$, with $`p`$ a lift of $`p_c`$, the first turned plane is spanned by $`p`$, $`d`$ and $`c_t = \cos t\,c + \sin t\,\nu`$, and $`S_\pm`$ by $`p`$, $`u_\pm = \cos(W/R)\,c \pm \sin(W/R)\,d`$ and $`\nu`$. Solving $`a_1 d + a_2 c_t = b_1 u_\pm + b_2\nu`$ gives the direction $`\pm\sin(W/R)\cos t\,d + \cos(W/R)\,c_t`$, at angle $`W_t/R`$ from $`c_t`$ with $`\tan(W_t/R) = \cos t\tan(W/R)`$. The second turned plane is spanned by $`p`$, $`c`$ and $`d_t = \cos t\,d + \sin t\,\nu`$, and the same computation gives the direction $`\cos(W/R)\,c \pm (\sin(W/R)/\cos t)\,d_t`$, so $`\tan(W'_t/R) = \tan(W/R)/\cos t`$. At $`t = 0`$, $`(4RW_t)'' = -2R^2\sin(2W/R)`$ and $`(4RW'_t)'' = 2R^2\sin(2W/R)`$. ∎

**Remark (edge bending, not a named regime).** An edge energy with a bending term $`\beta\int k^2\,ds`$, $`k`$ the edge's curvature in $`\mathbb{RP}^3`$, is infinite on every conic band: each pass through $`p_c`$ is a corner, where the edge turns by $`2W/R`$.

## IV. Grounds

The ground floor names these regimes and fixes none: the postulate "does not yet select among these frameworks or fix their coefficients and boundary conditions". Keeping the conic family takes two further choices, and neither is derived: $`\Gamma = 0`$ has only a MOTIVATED reading of the bar, and keeping the conic band's own pinch has no ground on the carrier page but the seed, which forces only some singular point carrying the twist.
- *$`\Gamma = 0`$ (MOTIVATED).* For $`\Gamma > 0`$ and $`\sigma > 0`$ the unbent critical bands with a smooth edge are the tubes about a projective line of half-width $`R\arctan(\Gamma R/\sigma)`$: by Lemma 2 the edge is a circle, the band is $`\mathbb{RP}^2`$ minus the disc it bounds, and a tube's edge has geodesic curvature $`-\tan(W/R)/R`$ toward the band. Their width is set by the length $`\sigma/\Gamma`$. The bar asks for the coupling to the $`2I`$ sector to come "without an arbitrary new scale"; read as excluding any new length, that excludes $`\Gamma \neq 0`$ unless a framework number ties $`\sigma/\Gamma`$ to $`R`$, and nothing on the carrier page or the postulate bridge does. That motivates $`\Gamma = 0`$ without deriving it. The texts do not prefer the zero-sheet-tension energies otherwise: the bar pairs area with bending, "least-area (least-bending)", and the ground floor brings in line tension to make area well posed with a movable edge.
- *Keeping the pinch (INFERRED).* The pinched class is the one place the conic family is selected (Proposition 1(3)). With the edge free, the carrier page's only ground near it is carrier Corollary 2.1: an exact $`2/R^2`$ first positive level needs a singular point that the twist passes through. That is the Λ seed, and it forces some such point, not the conic band's own fibre-collapse pinch, so keeping that pinch is a further restriction. Read against the clarified bar, a restriction adopted for the seed does not count: the postulate does not motivate it, it was not declared before these computations, and it keeps the candidate. Granted anyway, the pinch does not bring the laps with it (carrier Proposition 4.2): in the pinched class the laps are geodesic because $`\Gamma = 0`$ and $`\sigma > 0`$, not because of the seed.

The fixed edge of carrier §IX remains the one regime here shown to hold $`M(W)`$ stable with no null direction: index 0 and nullity 0 for its declared class of variations, reproduced by its independent check ([The Fixed-Edge Stability Check](fixed-edge-check.md)), with the conic type held locally by carrier Proposition 6. There the edge is input, the regime 1c adopted on 2026-10-01 as a modeling input.

## V. What stays open

- Bent competitors in the full class: bent critical bands, and the infimum over bent bands. For $`\sigma > 0`$ the negative for $`M(W)`$ does not wait on them, since an in-plane cut already lowers the energy.
- The minimizers at the upper end of Proposition 1(3)'s window, $`\bar\kappa = 0`$, which is $`\int H^2`$.
- Supports that are not totally geodesic, and which supports the framework would supply.
- A derived ground for $`\Gamma = 0`$, a ground for keeping the conic band's own pinch that does not come from the target, and any mechanism that selects $`W`$.
- Regimes the ground floor does not name are not treated here.

## Files

In [`scripts/carrier-edge-regimes/`](scripts/carrier-edge-regimes/), with the SHA-256 of every other file in `SHA256SUMS`:
- `edge_regimes.py`: Lemma 1's family and $`\Gamma`$ for each named energy (E1) and its first order (E2); Lemma 2's sign convention (E3); Lemma 3's expansions with geodesic legs (E4); the passes through the pinch, traced from the band's rectangle with the Möbius gluing (E5); the cut band's topology, on a cell complex of $`S^2`$ symmetric under $`-I`$ (E6); Proposition 1(2)'s circles (E7); Proposition 1(3)'s window (E8); Proposition 2's two turned families (E9); the critical tubes' width and the tube edge (E10). Its `--arms` mode plants a defect for each check and requires it to fire. Its record is `edge_regimes.out`.

---

/ **[`↑top`](#top)** / **[`main`](https://github.com/dmobius3/mode-identity-theory/tree/main/)** / **[`framework`](/files/framework/)** / **[`bedrock`](/files/framework/files/bedrock/)** / **[`working`](/files/framework/files/working/)** / **[`cosmos`](/files/cosmos/)** / **[`spectrum`](/files/spectrum/)** / **[`tools`](/files/tools/)** /
