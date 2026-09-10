<a id="top"></a>
/ **[`main`](https://github.com/dmobius3/mode-identity-theory/tree/main/)** / **[`framework`](/files/framework/)** / **[`bedrock`](/files/framework/files/bedrock/)** / **[`working`](/files/framework/files/working/)** / **[`cosmos`](/files/cosmos/)** / **[`spectrum`](/files/spectrum/)** / **[`tools`](/files/tools/)** /

---

# The Plato Twist

**Type:** Note
**State:** Open
**Status (2026-09-10):** The value is accounted for geometrically: the spin lift of the Levi-Civita holonomy around the shortest closed geodesic of S³/2I has half-trace cos(π/10), where the flat 2I holonomy gives cos(π/5). Why the weak coupling carries the factor, at the first power, and alone, is underived and not being worked.
**Summary:** Where the weak coupling's cos(π/10) correction occurs in the geometry of S³/2I, which nearby constructions fail, and what a derivation of its insertion into the coupling would have to settle.
**Inputs:** `../../../../spectrum/files/fine-structure.md` §V, `scripts/plato-twist.test.py`

The weak row of the gauge ladder carries one multiplicative correction, $`\cos(\pi/10) \approx 0.951`$, the Plato twist. This note records where that number occurs in the geometry and what is still missing before it belongs to a derivation. In short: the number is a geometrically fixed invariant of the shortest geodesic class of the dodecahedral space; why that class, and why the number enters $`\alpha_W`$, are open.

## I. The factor and its first motivation

The weak coupling is read as

```math
\alpha_W = C(17/120)\,\Omega_\Lambda^{-1/120}\cos(\pi/10) = 0.0339
```

against the $`\overline{\text{MS}}`$ value $`\hat\alpha(M_Z)/\hat{s}_Z^2 = 0.0338`$. Without the factor the row misses by 5.5%; with it, by 0.3%. The factor was first motivated by halving the dodecahedron's vertex defect $`\pi/5`$ with the Möbius orientation $`Z_2`$. No computation stands behind that route.

## II. Two holonomies on the same loop

$`S^3/2I`$ is the dodecahedral space: a spherical dodecahedron with opposite faces glued after a twist of $`\pi/5`$. The twelve face-pairing elements of $`2I`$ are the order-10 elements at angular distance $`\pi/5`$ from the identity, and each closes a shortest geodesic running along a five-fold axis. Two natural holonomies live on that loop.

- **Flat.** The face-pairing element acting on the doublet has half-trace $`\cos(\pi/5) = \varphi/2`$. Its rotation of three-space is the 72° five-fold turn, so the 36° gluing twist is already the spinor half-angle of the deck element.
- **Levi-Civita, spin-lifted.** A frame carried once around the loop returns rotated by exactly $`\pi/5`$: the gluing twist, now as a rotation of the tangent space. Lifted to the manifold's unique spin structure, that rotation has half-trace $`\cos(\pi/10)`$.

On every geodesic class the frame rotation equals the class length, so the spin-lifted value is the half-angle of the flat one:

```math
\tfrac12\,\mathrm{tr}\,\mathrm{Hol}_\text{spin} = \sqrt{\tfrac12\left(1 + \tfrac12\,\mathrm{tr}\,\mathrm{Hol}_\text{flat}\right)}
```

On the shortest class this gives $`\cos(\pi/10) = \sqrt{(1+\cos(\pi/5))/2} = \sqrt{2+\varphi}/2`$.

| Construction on the shortest loop | Factor | Weak residual |
|---|---|---|
| Spin-lifted Levi-Civita holonomy, half-trace | $`\cos(\pi/10)`$ | +0.3% |
| The same, squared as an intensity | $`\cos^2(\pi/10)`$ | −4.6% |
| Flat $`2I`$ doublet, half-trace | $`\cos(\pi/5)`$ | −14.7% |

The two neighbours of the construction that lands both miss badly, which is what separates a geometrically fixed invariant from a symbolic rewrite of the wanted number.

## III. Why no trace of flat holonomy reaches it

Every character of $`2I`$ takes values in $`\mathbb{Q}(\sqrt5)`$. The number $`\cos(\pi/10)`$ is a root of $`16x^4 - 20x^2 + 5`$, irreducible by Eisenstein at 5, so it has degree four over $`\mathbb{Q}`$ and lies outside that field. No trace or normalized trace of flat $`2I`$ holonomy, in any representation and in any of the three flat vacua, and nothing rational in such traces, can equal it. The spin lift's half-angle is what supplies the missing square root.

The obstruction covers traces, not every construction from flat data. A matrix element on a chosen vector can carry a square root: for the face-pairing element and a spinor polarized along an adjacent two-fold axis, $`\lvert\langle\psi\vert U\vert\psi\rangle\rvert = \cos(\pi/10)`$ exactly. Constructions like that are why the loop, the representation, and the operation have to be fixed before the value is compared.

## IV. What the computed route changes

Both ingredients of the first motivation are replaced. The $`\pi/5`$ is the twist of the shortest closed geodesic, which for these Clifford translations equals the geodesic's length, not the flat dodecahedron's vertex defect; the two angles coincide but are different objects. The halving is the spin double cover $`SU(2) \to SO(3)`$, the same integer-versus-half-integer split that sorts the 60 and 120 grids, not the Möbius orientation $`Z_2`$, which the framework keeps distinct from that split.

The residual is unchanged at 0.3%. What changed is the accounting: the factor is no longer a number taken from the geometry for its value but a geometrically fixed invariant of the shortest geodesic class, and the open question has moved entirely to its insertion, which includes why that class.

## V. Open: the insertion

A derivation has to settle three things together.

1. **Which loop.** Only the shortest geodesic class gives the factor; the next classes give $`\cos(\pi/6)`$, $`\cos(\pi/5)`$, and smaller values. Why the primitive shortest orbit is privileged has to come from the dynamics, not from the target.
2. **Which power.** The framework reads couplings as intensity-like, which argues for squaring, and the square misses by 4.6%. The weak rung's all-spinorial assignment argues for the first power, but that assignment is itself a proposed rule.
3. **Which sector.** The spin connection transports every fermion, not only weak doublets. The factor is also even in the twist's orientation: the frame rotation is $`-\pi/5`$ on the quotient and $`+\pi/5`$ on its mirror image, and the half-trace is the same. So parity cannot be what the factor encodes; if chirality singles out the weak row, it enters elsewhere.

## VI. The test that would move the row

Computing the holonomy value blind would certify geometry and nothing more. The test worth running derives the effective gauge kinetic term from the quotient and its spin-bundle structure, schematically $`-\tfrac{1}{4g^2}F_{\mu\nu}F^{\mu\nu}`$, without inserting the factor, and asks whether $`g`$ or $`\alpha`$ acquires $`\tfrac12\,\mathrm{tr}\,\mathrm{Hol}_\text{spin}(\gamma_\text{min})`$. It must be allowed to return none of the above, and it has to fix the loop, the power, and the sector in the same computation. If one derivation does all three and lands on the existing weak formula, the row's status changes; until then the scorecard's "Conjectural (Plato-twist ansatz)" stands.

## Check

[plato-twist.test.py](scripts/plato-twist.test.py) builds $`2I`$ as 120 unit quaternions, checks closure and the half-trace set, integrates Levi-Civita parallel transport around every geodesic class, and asserts the flat and spin-lifted values, the half-angle relation, the matrix-element caveat, and the residuals printed above. Its mutation arm substitutes the deck element's own 72° rotation for the transported frame, and the $`\pi/5`$ check rejects it.

---

/ **[`↑top`](#top)** / **[`main`](https://github.com/dmobius3/mode-identity-theory/tree/main/)** / **[`framework`](/files/framework/)** / **[`bedrock`](/files/framework/files/bedrock/)** / **[`working`](/files/framework/files/working/)** / **[`cosmos`](/files/cosmos/)** / **[`spectrum`](/files/spectrum/)** / **[`tools`](/files/tools/)** /
