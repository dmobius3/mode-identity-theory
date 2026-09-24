<a id="top"></a>
/ **[`main`](https://github.com/dmobius3/mode-identity-theory/tree/main/)** / **[`framework`](/files/framework/)** / **[`bedrock`](/files/framework/files/bedrock/)** / **[`working`](/files/framework/files/working/)** / **[`cosmos`](/files/cosmos/)** / **[`spectrum`](/files/spectrum/)** / **[`tools`](/files/tools/)** /

---

# The Tier 2 Fixed-Boundary Run

**Type:** Result
**State:** Closed
**Status (2026-09-23):** Run blind against terms frozen before it, reviewed, and checked against the literature. The specified band, Lawson's Möbius band, has Dirichlet index 2 and nullity 1 under the fixed-boundary area functional: it is unstable. The index was already stated in the literature, by Bernstein and Ketover the day before the freeze. The nullity follows by reflection from Morozov and Penskoi's nullity for Lawson's closed Klein bottle; a standalone statement of it was not located. The review adds that no smooth embedded Möbius band spanning a great circle attains the infimum of area; the infimum's value is open.
**Summary:** The postulate bridge's first Tier 2 computation: the Dirichlet Jacobi spectrum of a specified minimal Möbius band bounded by a great circle in $`S^3`$, run blind.
**Inputs:** `postulate-bridge.md` (the Tier 2 ground floor), `scripts/tier2-fixed-boundary/`
**Parent:** `postulate-bridge.md`

---

RESULT. The run adds nothing new mathematically. It asked what the fixed-boundary area problem does at one specified critical point. The index it found was already stated in the literature, and the nullity follows from a published computation, though a standalone statement of it was not located. The band $`B`$ is Lawson's Möbius band: the half of his Klein bottle $`\tau_{2,1}`$ bounded by a great circle $`\gamma \subset S^3(R)`$. A blind computation returned Dirichlet index $`I = 2`$, carried by the sectors $`m = \pm 1`$, and nullity $`N = 1`$, the rotation about $`\gamma`$: $`B`$ is unstable. Bernstein and Ketover stated the index the day before the terms were frozen. Both values also follow from Morozov and Penskoi's index and nullity for the closed Klein bottle, by a reflection that splits its spectrum into the Dirichlet and Neumann spectra of $`B`$ (§V). What the run contributes is a blind computation, frozen before it ran, that confirms both and agrees with the published closed-surface values. The review adds one consequence the search did not find stated: no smooth embedded Möbius band spanning a great circle attains the infimum of area, whose value stays open (§VI).

**Related:** [Postulate bridge](postulate-bridge.md), [First eigenvalue](../../bedrock/files/first-eigenvalue.md).

---

## I. The question, as frozen

The [postulate bridge](postulate-bridge.md)'s Tier 2 ground floor registered this computation on 2026-07-13. Fix a round great circle $`\gamma \subset S^3(R)`$ and the class $`\mathcal A_\gamma`$ of smooth embeddings of the Möbius band with boundary $`\gamma`$; extremize area; and compute the second variation on sections of the orientation line bundle, with the Dirichlet condition. The terms of the first run were frozen on 2026-09-23, before it ran, with no targets: no clock, no $`\Lambda`$, no recovery of $`2/R^2`$, no comparison with the first-eigenvalue pillar. They are held with the author, with SHA-256 `9609c2b11fccd3c3031fe8d5b189383f3786fc7f15e17391414b26eb8c42c846`.

The frozen target was the stability of one specified critical band, not of "the Möbius equilibrium":

```math
B:\quad p(s,t) = R\big[\cos t\,(\cos s\,e_1 + \sin s\,e_2) + \sin t\,(\cos\tfrac{s}{2}\,e_3 + \sin\tfrac{s}{2}\,e_4)\big],
```

with $`(s,t) \in [0, 2\pi] \times [-\tfrac{\pi}{2}, \tfrac{\pi}{2}]`$, $`(2\pi, t) \sim (0, -t)`$ and $`\gamma = S^3(R) \cap \mathrm{span}(e_3, e_4)`$. The band is embedded, minimal, and ruled by great semicircles through its core. It is invariant under the screw group $`G`$, which rotates the $`(e_1, e_2)`$-plane by $`c`$ and the $`(e_3, e_4)`$-plane by $`c/2`$. Its metric is $`R^2[f\,ds^2 + dt^2]`$ with $`f = 1 - \tfrac34\sin^2 t`$, and $`\lvert A\rvert^2 = 1/(2R^2 f^2)`$. Its Jacobi operator $`J = -\Delta - \lvert A\rvert^2 - 2/R^2`$ acts on sections of the orientation bundle and splits under $`G`$ into sectors $`\psi = e^{ims/2}\varphi(t)`$:

```math
R^2 J_m\varphi = -\frac{1}{\sqrt{f}}\big(\sqrt{f}\,\varphi'\big)' + V_m\varphi, \qquad V_m = \frac{m^2}{4f} - \frac{1}{2f^2} - 2,
```

on $`[0, \tfrac{\pi}{2}]`$, with $`\varphi(0) = 0`$ for even $`m`$, $`\varphi'(0) = 0`$ for odd $`m`$, and $`\varphi(\tfrac{\pi}{2}) = 0`$. Each sector with $`m \neq 0`$ counts twice, for $`e^{\pm ims/2}`$.

Two sectors were settled before the run and disclosed with the terms. Sectors with $`m^2 \geq 16`$ carry nothing, since $`V_m > 0`$ there. Sector $`m = 0`$ has index 0 and nullity 1: the rotation $`X_{12}`$ about $`\gamma`$ carries $`B`$ through a circle of congruent bands with the same boundary, and its Jacobi field is

```math
\psi_X = \langle X_{12}, \nu\rangle = \frac{\sqrt2\,R\sin 2t}{2\sqrt{3\cos 2t + 5}}.
```

The run's unknowns were the sectors $`m = \pm 1, \pm 2, \pm 3`$. The frozen method decided $`m = \pm 1, \pm 3`$ exactly, from the normal components of the four rotations that mix the two planes. It decided $`m = \pm 2`$ numerically, by a Sturm count from high-order shooting and by Chebyshev collocation at two resolutions. It carried three controls, each able to fail, and a near-zero rule: an eigenvalue at zero counts as nullity only against an exhibited exact Jacobi field.

## II. The blind result

The computation was run blind. The solver received only a transcription of the frozen setting, operator and method, and worked in a contained environment; the audit of its record found that it read nothing else. The transcription left out the frozen terms' framework context, and one clause stating that the plane-mixing rotation fields do not vanish on $`\gamma`$, which would have suggested the nullity in $`m = \pm 1, \pm 3`$. The method decides that point by its own symbolic check.

Eigenvalues are in units of $`1/R^2`$.

| sector | index | nullity | decided by | lowest eigenvalues |
| --- | --- | --- | --- | --- |
| m = 0 | 0 | 1 | collocation and shooting, with ψ_X exhibited | −1.4e−12 (the kernel), 11.6599 |
| m = ±1 | 1 each | 0 | exact: the rotation solution has one zero | −2.0000000000, 5.2454 |
| m = ±2 | 0 | 0 | numerical: Sturm count 0 | 1.8494 |
| m = ±3 | 0 | 0 | exact: the rotation solution is positive | 0.6916, 9.1229 |

The totals are $`I = 2`$ and $`N = 1`$, the frozen outcome O2: the band is unstable. The rotation profiles are

```math
m = 1:\ \ \varphi_K = \frac{3\sin^2 t - 2}{4\sqrt{f}}, \qquad m = 3:\ \ \varphi_K = \frac{1 + \cos^2 t}{4\sqrt{f}},
```

from $`X_{13} + X_{24}`$ and $`X_{13} - X_{24}`$. The first vanishes once in $`(0, \tfrac{\pi}{2})`$, where $`\sin^2 t = \tfrac23`$, and neither vanishes at $`\tfrac{\pi}{2}`$.

All three controls passed.
- The $`m = 0`$ sector returned index 0 and one near-zero eigenvalue, whose eigenfunction matches $`\psi_X`$ to about $`10^{-13}`$.
- The rotation profiles solve their sector equations symbolically, and the exact and numerical routes agree.
- Two mutated operators, one with the Ricci term $`3/R^2`$ and one with $`\lvert A\rvert^2`$ dropped, each fail the $`m = 0`$ control.

## III. What is exact and what is numerical

- $`I \geq 2`$: exact, without numerics (§V).
- $`m = \pm 1`$: one negative eigenvalue each, exact. The ground state is $`-2/R^2`$ exactly, and the rotation solution has one zero.
- $`m = 0`$ and $`m^2 \geq 16`$: exact, settled before the run.
- $`m = \pm 3`$: no negative or zero eigenvalue, exact. The rotation solution is positive, and nonzero at $`\tfrac{\pi}{2}`$.
- $`m = \pm 2`$: positive, numerically. Its lowest eigenvalue is 1.8494, and the run's collocation and the review's finite differences agree on it to $`10^{-6}`$.

On its own terms, then, the run completes its totals numerically in $`m = \pm 2`$. Given Morozov and Penskoi's values for the closed Klein bottle, the totals are exact (§V).

## IV. Audit and conformance

**Containment.** The audit of the solver's record found no access outside its two input files.

**Reproduction.** The solver's nine scripts, rerun, reproduce its recorded output line for line. The regenerated records are in `run-1/`.

**Conformance.** The solver followed the frozen method. Its return says the method was followed exactly, with no deviations and no underdetermined points, and that overstates it. The return is kept unedited, and this section is authoritative. Seven gaps are recorded, and none changes a value or a count.

1. **Resolutions.** "64 and 128 points" was read as Trefethen's $`N`$, so 65 and 129 nodes, without flagging the reading. The two resolutions agree to 5e−11.
2. **Root isolation.** It was done by an exact monotonicity argument, not a root-isolation routine: $`\varphi_K`$ has the sign of $`3\sin^2 t - 2`$, and $`\sin^2 t`$ increases on $`(0, \tfrac{\pi}{2})`$.
3. **Control C2.** Its verdict line in the controls script is typed text. Its substance is computed in the other scripts, and the review's reproduction verifies it.
4. **Controls script.** It exits with an error in its closing summary, after its three verdict lines print. That is a reporting defect, not a failed control.
5. **Output records.** The solver left them only in its terminal output. The rerun regenerates them.
6. **Decomposition print.** One check prints unsimplified residues that are zero. The sector-pure combinations are verified directly.
7. **Debugging.** The solver's first two collocation implementations were broken. One applied a symmetric eigensolver to a nonsymmetric matrix. The other had a sign error in its derivative matrix, which put the $`m = 1`$ ground state at −1.39, with the same index. The $`m = 0`$ control caught both before the final run, which is what it is for, and the solver then tested the matrix on known functions.

## V. Why the modes are what they are

**The unstable modes (known).** For a minimal surface in $`S^3(R) \subset \mathbb R^4`$ with unit normal $`\nu`$, $`\Delta\nu = -\lvert A\rvert^2\nu`$. So for a constant vector $`a`$,

```math
J\langle a, \nu\rangle = -\frac{2}{R^2}\langle a, \nu\rangle .
```

On $`\gamma`$, $`\nu`$ is orthogonal to the position vector and to $`\gamma'`$, which together span $`\mathrm{span}(e_3, e_4)`$, so $`\langle e_3, \nu\rangle`$ and $`\langle e_4, \nu\rangle`$ vanish on the boundary. For $`B`$ they are $`\cos t\sin(s/2)/\sqrt{f}`$ and $`-\cos t\cos(s/2)/\sqrt{f}`$, the ground states of $`m = \pm 1`$, at $`-2/R^2`$ exactly. That makes $`I \geq 2`$ exact. Bernstein and Ketover prove the general statement for non-orientable minimal surfaces bounded by a great circle: each one other than a hemisphere has Dirichlet index at least 2 ([7], Proposition 2.7, which credits the identity to Simons [2]). The review re-derived it before the search found it.

**The closed Klein bottle, by reflection.** *DERIVATION (review).* The antipodal copy of $`B`$ is $`B`$ rotated by $`\pi`$ about $`\gamma`$:

```math
-p(s, -t) = R_{12}(\pi)\,p(s, t).
```

The rotation fixes $`\gamma`$ pointwise and swaps the two halves of Lawson's Klein bottle $`\tau_{2,1} = B \cup (-B)`$. In each sector it acts as $`t \mapsto \pi - t`$, and $`V_m(\pi - t) = V_m(t)`$. So the closed bottle's Jacobi spectrum is the Dirichlet spectrum of $`B`$ together with its Neumann spectrum, the one with $`\varphi'(\tfrac{\pi}{2}) = 0`$.
- **The Neumann side has index 5:** $`m = 0`$ at −4.9245, $`m = \pm 1`$ at −4.4859 each, and $`m = \pm 2`$ at −2 exactly, the pair $`\langle e_1, \nu\rangle`$ and $`\langle e_2, \nu\rangle`$.
- **Its nullity is 4:** the four plane-mixing rotations, whose profiles have zero slope at $`\tfrac{\pi}{2}`$.
- **The sum.** Dirichlet (2, 1) plus Neumann (5, 4) is (7, 5), the index and nullity Morozov and Penskoi computed for $`\tau_{2,1}`$ [4]. The splitting holds eigenvalue by eigenvalue in every sector.

The count is exact, given their values.
- **Nullity.** 5 is the Dirichlet nullity plus the Neumann nullity, with the first at least 1 ($`\psi_X`$) and the second at least 4 (the rotations). So $`N = 1`$.
- **Index.** 7 is the Dirichlet index plus the Neumann index, with the first at least 2 (above) and the second at least 5. The Neumann problem imposes no condition on the boundary values, and five test functions in mutually orthogonal sectors each have negative second variation there. The first two are $`\langle e_1, \nu\rangle`$ and $`\langle e_2, \nu\rangle`$ in $`m = \pm 2`$, at $`-2/R^2`$. The next two are the constant profile in $`m = \pm 1`$, since with $`u = 1/f \in [1, 4]`$, $`V_1 = u/4 - u^2/2 - 2 \leq -\tfrac94`$. The last is $`\sin t`$ in $`m = 0`$. Its form is at most $`\int_0^{\pi/2}(\cos^2 t - 2\sin^2 t)\sqrt{f}\,dt`$ minus a positive term, and $`\tfrac12 \leq \sqrt{f} \leq 1`$ puts that integral at or below $`\tfrac{\pi}{4} - \tfrac{\pi}{4} = 0`$; the form's value is −2.107. So $`I = 2`$, and the numerics of $`m = \pm 2`$ drop out of both totals.
- **What it rests on.** Morozov and Penskoi's Theorem 2, which they prove by separating variables and analyzing the one-dimensional problems.

**The eigenvalue −2/R².** It is the eigenvalue of $`\langle a, \nu\rangle`$ on every minimal surface in $`S^3`$, so it carries no information about $`B`$, and none about $`\Lambda`$ (§VIII).

## VI. What follows for area

*DERIVATION (review), not a run result.*

**The band is not a local minimizer.** For $`\psi = \langle e_3, \nu\rangle`$ or $`\langle e_4, \nu\rangle`$, the normal variation $`B_\varepsilon = \exp_B(\varepsilon\psi\nu)`$ in $`S^3`$ fixes the boundary, and

```math
\mathrm{Area}(B_\varepsilon) = \mathrm{Area}(B) - \frac{\varepsilon^2}{R^2}\int_B \psi^2\,dA + O(\varepsilon^3).
```

Small Dirichlet perturbations of an embedded compact band stay embedded, so $`B`$ is not a local minimizer of area in $`\mathcal A_\gamma`$.

**Every minimal Möbius band spanning γ is unstable.** The mechanism does not use $`B`$. If $`\langle a, \nu\rangle`$ vanished identically on a connected minimal surface for some $`a \neq 0`$, differentiating would give $`A(a^\top) = 0`$, where $`a^\top`$ is the tangential part of $`a`$. Where $`a^\top \neq 0`$, the traceless symmetric $`A`$ then has a zero eigenvalue, so $`A = 0`$; and $`a^\top`$ cannot vanish on an open set. So a minimal surface spanning $`\gamma`$ that is not totally geodesic has Dirichlet index at least 2. No Möbius band is totally geodesic, so every minimal Möbius band spanning $`\gamma`$ is unstable, including any other $`G`$-invariant one. For non-orientable surfaces this is Bernstein and Ketover's Proposition 2.7 [7].

**No member of the class attains the infimum of area.** A least-area member of $`\mathcal A_\gamma`$ would be minimal, and its Dirichlet second variation would be nonnegative, since small Dirichlet variations stay in the class. The paragraph above forbids that. Within the class no regularity input is needed: its members are smooth up to $`\gamma`$ by definition. This was not located as a prior statement.

**The infimum's value stays open.** Every Möbius band spanning $`\gamma`$ has area greater than $`2\pi R^2`$, by the projection argument recorded with the frozen terms, and Bernstein and Ketover's Lemma 2.2 [7] gives the bound $`2\pi R^2`$ for every spanning map. Whether the infimum over embedded bands is $`2\pi R^2`$ or larger is open.

**Not Bernstein and Ketover's least-area band.** Their Theorem 5.4 [7] finds a least-area member among *minimal* Möbius bands spanning a great circle, embedded and of index 2. Minimizing within the critical subclass is not minimizing among all embedded bands: an index-2 band has embedded variations that lower area and are no longer minimal.

## VII. The literature

The frozen terms required a search for the band and its index before landing, reporting what was found, and "was not located" where nothing was. The run was not repeated or revised in light of it.

- **The band is Lawson's Möbius band.** Lawson's minimal Klein bottle $`\tau_{2,1}`$ [1] is cut by $`\gamma`$ into two embedded Möbius bands, and $`B`$ is one of them: Morozov and Penskoi's $`\Psi_{2,1}(x, y)`$ [4] is $`p(s, t)/R`$ with $`s = 2x`$ and $`t = y`$. Bernstein and Ketover [6, 7] write the band as $`\bar\tau_{1,2}`$, with the coordinate planes swapped. By their reading of Lawson's Proposition 7.2, these bands are the only ruled minimal surfaces bounded by a great circle.
- **The rotation family is old.** Hardt and Rosenberg [3] described the circle of these bands with a common boundary, the family behind $`N = 1`$. They asked whether these bands and the hemispheres are the only embedded minimal surfaces with that boundary, and Bernstein and Ketover [6] answered no.
- **White's band.** It is also the band of White's conjecture, which Guaraco and Parise [5] proved: the cone over it in $`\mathbb R^4`$ is area-minimizing mod 2. They state no index for the band itself.
- **The index was stated the day before the freeze.** Bernstein and Ketover [7], posted 2026-09-22, state that $`\bar\tau_{1,2}`$ has Morse index 2, in the Dirichlet sense used here. They cite an appendix of a companion paper, which was not located on 2026-09-23. The run was frozen and executed without knowledge of that statement.
- **The nullity was not located as a stated result.** It follows from Morozov and Penskoi's nullity for the closed bottle, by the reflection of §V.
- **The closed Klein bottle** has index 7 and nullity 5 [4]. §V connects those values to the run.

1. H. B. Lawson, Jr., *Complete minimal surfaces in S³*, Ann. of Math. 92 (1970), 335-374. [doi:10.2307/1970625](https://doi.org/10.2307/1970625)
2. J. Simons, *Minimal varieties in Riemannian manifolds*, Ann. of Math. 88 (1968), 62-105. [doi:10.2307/1970556](https://doi.org/10.2307/1970556)
3. R. Hardt and H. Rosenberg, *Open book structures and unicity of minimal submanifolds*, Ann. Inst. Fourier 40 (1990), 701-708. [doi:10.5802/aif.1229](https://doi.org/10.5802/aif.1229)
4. E. A. Morozov and A. V. Penskoi, *Index of minimal surfaces in the 3-sphere*, Russian Math. Surveys 78:2 (2023), 396-398. [doi:10.4213/rm10094e](https://doi.org/10.4213/rm10094e)
5. M. A. M. Guaraco and D. Parise, *White's cone over the Möbius band is area-minimising*, [arXiv:2609.24909](https://arxiv.org/abs/2609.24909) (2026).
6. J. Bernstein and D. Ketover, *Minimal equatorial fillings*, [arXiv:2609.26701](https://arxiv.org/abs/2609.26701) (2026).
7. J. Bernstein and D. Ketover, *On the Willmore energy of Möbius bands*, [arXiv:2609.26745](https://arxiv.org/abs/2609.26745) (2026).

## VIII. Guards

- $`-2/R^2`$ is minus the Ricci term, by construction: $`-\Delta - \lvert A\rvert^2`$ annihilates $`\langle a, \nu\rangle`$. It is reported as a number and counts for nothing. It is not read as $`\Lambda`$, and the $`2/R^2`$ arch stays dead.
- Every statement here concerns $`B`$, a specified critical band, or a derivation over the class. None concerns "the Möbius equilibrium".
- No physical reading of $`I`$ or $`N`$ is made.
- $`B`$ is smooth up to $`\gamma`$, so the first-eigenvalue pillar's defect and self-adjoint-extension machinery is not load-bearing here.

## Files

In [`scripts/tier2-fixed-boundary/`](scripts/tier2-fixed-boundary/), with the SHA-256 of every file in `SHA256SUMS`:
- `setup/`: checks of the facts disclosed with the frozen terms, with three mutation controls, and their record.
- `run-1/`: the solver's two input files, its return (SHA-256 `86abc5206347b275a825041318676278deef533691671ff48989c5a8c364e4bb`), its nine scripts, and their output records from the rerun.
- `review/`: `independent_check.py` checks the exact ground state, and runs finite differences, Radau shooting and a mutation arm. `neumann_check.py` checks the reflection, the Neumann spectrum, the closed-bottle totals and the exact bounds. Both come with their records.
