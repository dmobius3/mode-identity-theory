<a id="top"></a>
/ **[`main`](https://github.com/dmobius3/mode-identity-theory/tree/main/)** / **[`framework`](/files/framework/)** / **[`bedrock`](/files/framework/files/bedrock/)** / **[`working`](/files/framework/files/working/)** / **[`cosmos`](/files/cosmos/)** / **[`spectrum`](/files/spectrum/)** / **[`tools`](/files/tools/)** /

---

# The Slot Ground States

**Type:** Result
**State:** Closed
**Status (2026-10-04):** Derived. Under the frozen slot action, every slot has energy minimizers at each fixed nonzero charge; each is a standing wave, and the set of them is orbitally stable (Theorem A). Whether the sets in the soft slots, R2, R4 and R5, form branches remains open. In the five rigid slots and the control the minimizers are the exact lowest-level family, which the slot action's §VI item 6 records for the five slots and which in the control is the constant sections. It is orbitally stable as a set at every nonzero charge (Theorem B), supplying §VII's orbital-stability alternative for those branches under M8.4's persistence label; on OpenWave, the rung is a filing's to adjudicate. In R4 and R5 no ground state lies entirely in the lowest free eigenspace; in R2 the same question is whether a spin-6 multipole can vanish, and it stays open. The soft blocks' reduced quartic is derived in closed form, which gives OpenWave's D7 weights and R2's coefficients. The stability mechanism is generic; what is specific to 2I is which slots are rigid, the coherent orbit that minimizes the reduced quartic in R4 and R5, and the closed form.
**Summary:** Whether the frozen slot action carries orbitally stable nonlinear states without a run: energy minimizers at fixed charge in every slot, the rigid slots' exact branches, and the soft blocks' reduced quartic in closed form.
**Inputs:** `slot-action.md` (§V, §VI item 6, §VII, §IX), OpenWave's M8.12 record (the bridge from the block quartic to r̂₆, and G1) at `344f416`, `scripts/slot-ground-states/`
**Parent:** `slot-action.md`

---

RESULT, a derivation with no pre-committed pass condition. [The slot action](slot-action.md) froze one law for the eight slot fields and recorded what it decides without a run (§VI); the stability of its nonlinear branches it left to a pre-registered persistence test or an orbital-stability theorem (§VII). This page proves that theorem by minimizing the energy at fixed charge, both for the rigid slots' exact branches, at every nonzero charge, and for the ground-state sets of every slot, and it derives the soft blocks' reduced quartic in closed form. Nothing here is a run, and nothing here bears on the slot relation, which stays OPEN.

**Related:** [The Slot Action](slot-action.md), [The Slot Relation](slot-relation.md), [The Surviving Ray](../../bedrock/files/surviving-ray.md).

## I. The Setting

For each sector $`\rho`$, the control $`R_0`$ and the slots $`R_1`$ to $`R_8`$, the fields are the slot action's sections $`\psi`$ of $`E_\rho`$ over $`X = S^3/2I`$, of volume $`V = 2\pi^2R^3/120`$. The phase space is $`\mathcal{H} = H^1(X; E_\rho) \times L^2(X; E_\rho)`$, with points $`(\psi, \pi)`$, $`\pi = \partial_T\psi`$. The energy and charge of §V are

```math
E = \int_X dV \left[ \frac{1}{2c^2}\lvert\pi\rvert^2 + \frac{1}{2}\lvert\nabla\psi\rvert^2 + \frac{g}{4}\lvert\psi\rvert^4 \right],
\qquad
N = \frac{1}{c^2}\int_X dV\; \mathrm{Im}\left(\psi^{\dagger}\pi\right),
```

with $`g = g_4 > 0`$. The lowest eigenvalue of $`-\Delta`$ on $`E_\rho`$ is $`\lambda_0 = n(n+2)/R^2`$ with $`n = \mathrm{dist}(\rho)`$: a slot's first occurrence is its bundle's lowest level, and $`\lambda_0 = 0`$ for $`R_0`$.

**Well-posedness.** In three dimensions $`H^1 \subset L^6`$, so $`\psi \mapsto \lvert\psi\rvert^2\psi`$ is locally Lipschitz from $`H^1`$ to $`L^2`$, and Picard iteration on the linear Klein–Gordon group gives local solutions in $`\mathcal{H}`$ that conserve $`E`$ and $`N`$. The energy bounds $`\lVert\nabla\psi\rVert^2`$ and $`\lVert\pi\rVert^2`$, and by Lemma 1(c) also $`\lVert\psi\rVert^2`$, so solutions are global.

## II. Three Lemmas

**Lemma 1 (the lower bound).** For $`(\psi, \pi) \in \mathcal{H}`$ with $`m = \int_X \lvert\psi\rvert^2 dV > 0`$,

```math
E \;\ge\; F(m; N) = \frac{c^2N^2}{2m} + \frac{\lambda_0 m}{2} + \frac{g\,m^2}{4V},
```

each term from one inequality, with its equality case:
- (a) Cauchy–Schwarz on the charge, $`c^2\lvert N\rvert \le \lVert\psi\rVert\,\lVert\pi\rVert`$: equality if and only if $`\pi = i\alpha\psi`$ with $`\alpha`$ real;
- (b) the spectral bound $`\int \lvert\nabla\psi\rvert^2 \ge \lambda_0 m`$: equality if and only if $`\psi`$ lies in the lowest eigenspace;
- (c) Jensen, $`\int \lvert\psi\rvert^4 \ge m^2/V`$: equality if and only if $`\lvert\psi\rvert`$ is constant on X.

So equality in $`E \ge F`$ holds exactly when (a), (b) and (c) hold together.

**Lemma 2 (precompactness of minimizing sequences).** Fix $`N_0 \ne 0`$, let $`e(N_0)`$ be the infimum of $`E`$ over $`\lbrace N = N_0 \rbrace`$, and let $`(\psi_k, \pi_k)`$ satisfy $`N = N_0`$ and $`E \to e(N_0)`$. Then a subsequence converges strongly in $`\mathcal{H}`$ to a minimizer.
- *Bounded.* $`F(m; N_0) \to \infty`$ as $`m \to 0`$ and as $`m \to \infty`$, so by Lemma 1 the $`m_k`$ stay in a compact interval of $`(0, \infty)`$, and $`E`$ bounds $`\lVert\nabla\psi_k\rVert^2`$ and $`\lVert\pi_k\rVert^2`$.
- *A minimizing limit.* On a compact 3-manifold $`H^1`$ embeds compactly in $`L^2`$ and $`L^4`$ (Rellich–Kondrachov), so a subsequence has $`\psi_k \to \psi`$ strongly in $`L^2`$ and $`L^4`$, $`\nabla\psi_k \rightharpoonup \nabla\psi`$ and $`\pi_k \rightharpoonup \pi`$. The charge passes to the limit under strong-times-weak convergence, so $`N(\psi, \pi) = N_0`$, and $`m > 0`$. The energy is weakly lower semicontinuous, so $`(\psi, \pi)`$ is a minimizer.
- *Strong convergence.* The quartic term converges, the energy converges to $`E(\psi, \pi)`$, and each of $`\lVert\nabla\psi_k\rVert^2`$ and $`\lVert\pi_k\rVert^2`$ is weakly lower semicontinuous, so each converges to its limit's norm. Weak convergence with convergence of norms is strong convergence.

**Lemma 3 (lowest-level standing waves).** Let $`\psi \ne 0`$ lie in the lowest eigenspace. Then $`e^{i\omega T}\psi`$ solves the field equation if and only if $`\lvert\psi\rvert`$ is constant, and then $`\omega^2 = c^2(\lambda_0 + g\lvert\psi\rvert^2)`$. The equation reduces to $`(\lambda_0 - \omega^2/c^2)\psi + g\lvert\psi\rvert^2\psi = 0`$, so $`\lvert\psi\rvert^2 = (\omega^2/c^2 - \lambda_0)/g`$ wherever $`\psi \ne 0`$; a nonzero eigensection is real-analytic, so its zero set has empty interior, and by continuity $`\lvert\psi\rvert`$ is constant everywhere. The converse is substitution.

## III. The Theorems

**Theorem A (ground states, every sector).** Fix a sector and $`N_0 \ne 0`$.
1. The infimum $`e(N_0)`$ is attained.
2. Every minimizer has $`\pi = i\omega\psi`$ for a real $`\omega`$, and $`(-\Delta - \omega^2/c^2)\psi + g\lvert\psi\rvert^2\psi = 0`$: it is a standing wave $`e^{i\omega T}\psi`$, a ground state.
3. The set $`G(N_0)`$ of minimizers is orbitally stable in $`\mathcal{H}`$: for every $`\varepsilon > 0`$ there is $`\delta > 0`$ such that data within $`\delta`$ of $`G(N_0)`$ stay within $`\varepsilon`$ of it for all time.

*Proof.* Item 1 is Lemma 2. For item 2, $`N_0 \ne 0`$ makes $`dN \ne 0`$ at a minimizer, so a Lagrange multiplier $`\omega`$ exists; varying $`\pi`$ gives $`\pi = i\omega\psi`$, and varying $`\psi`$ gives $`-\Delta\psi + g\lvert\psi\rvert^2\psi = (\omega/c^2)(-i\pi) = (\omega^2/c^2)\psi`$. Item 3 follows the constrained-minimization contradiction of Cazenave and Lions, written for the Schrödinger equation on $`\mathbb{R}^N`$; for Klein–Gordon standing waves that minimize the energy at fixed charge see Shatah. The Klein–Gordon phase-space and charge steps are supplied here. If item 3 failed, there would be data converging to $`G(N_0)`$ and times $`T_k`$ at which the solutions, which are global by §I, sit at distance at least $`\varepsilon`$ from it. Conservation and continuity give $`E \to e(N_0)`$ and $`N \to N_0`$ along the sequence at the $`T_k`$; rescaling $`\pi_k`$ by $`N_0/N_k`$ restores the constraint and changes $`E`$ by $`o(1)`$; by Lemma 2 a subsequence converges strongly to a point of $`G(N_0)`$, a contradiction.

**Theorem B (the rigid sectors).** Take $`R_0, R_1, R_3, R_6, R_7`$ or $`R_8`$, where $`\rho = \pi_n`$ restricted to 2I with $`n = \mathrm{dist}(\rho) \le 5`$. For $`N_0 \ne 0`$ let $`m`$ be the unique positive root of $`c^2N_0^2/m^2 = \lambda_0 + g\,m/V`$. Then

```math
G(N_0) = \left\lbrace \big(\pi_n(x)\,v,\ i\omega\,\pi_n(x)\,v\big) \;:\; \lvert v\rvert^2 = m/V \right\rbrace,
\qquad
\omega = \frac{c^2N_0}{m},\qquad \omega^2 = c^2\left(\lambda_0 + g\lvert v\rvert^2\right),
```

the exact lowest-level family at that frequency: the family of the slot action's §VI item 6 in the five slots, and the constant sections in the control, where $`\pi_0`$ is trivial. It is orbitally stable as a set, at every nonzero charge, and along each direction of $`v`$ it is a branch continuous in the charge.

*Proof.* In these sectors every lowest-level section is $`\pi_n(x)v`$, and $`\lvert\pi_n(x)v\rvert = \lvert v\rvert`$ is constant. So all three equalities of Lemma 1 hold for $`(\pi_n(x)v, i\alpha\,\pi_n(x)v)`$, and $`E = F(m; N)`$. $`F`$ is strictly convex in $`m`$, so it has one minimizing $`m`$, the stated root, which depends continuously on $`N_0`$; equality in $`E \ge F(m) \ge F(m^*)`$ picks out exactly the stated set, and stationarity of $`F`$ there gives $`\omega^2 = c^2(\lambda_0 + g\lvert v\rvert^2)`$. Orbital stability is Theorem A.3.

The family contains every fibre-symmetry and right-SU(2) orbit through it, so the claim is about the family as a set, as the slot action's §IX asks. No spectral or nondegeneracy analysis enters.

## IV. The Soft Slots

**The reduced quartic in closed form.** For a lowest-level section $`\psi_w`$ of a soft slot, write $`Q(w) = V\int\lvert\psi_w\rvert^4/(\int\lvert\psi_w\rvert^2)^2`$, the Jensen ratio of Lemma 1(c), which is 1 exactly at constant norm. The soft slots are $`R_4`$ and $`R_5`$ at level 6 and $`R_2`$ at level 7. Among the spins 0 to 7, 2I has invariant vectors only at 0 and 6, so a 2I-invariant operator on the block has spin components only at those two spins. The slot projector is therefore $`P = (r/d)\,\mathrm{Id} + P_6`$ with $`\lVert P_6\rVert^2 = r - r^2/d`$, where $`d = \mathrm{dist} + 1`$ is the block's dimension and $`r = \dim\rho`$. Schur orthogonality on the spin-6 representation then gives

```math
Q(w) = 1 + \beta_\rho\,\frac{\lVert (w w^{\dagger})_6 \rVert^2}{\lVert w\rVert^4},
\qquad
\beta_\rho = \frac{d\,(d-r)}{13\,r},
```

with $`(ww^{\dagger})_6`$ the spin-6 component of $`ww^{\dagger}`$ under conjugation, in the Hilbert–Schmidt norm. For spin 3 the last factor is M8.12's $`\hat r_6`$.

| slot | d | r | $`\beta_\rho`$ |
| --- | --- | --- | --- |
| $`R_4`$ ($`3'`$) | 7 | 3 | 28/39, OpenWave's D7 value |
| $`R_5`$ ($`4`$) | 7 | 4 | 21/52, OpenWave's D7 value |
| $`R_2`$ ($`2'`$) | 8 | 2 | 24/13 |

Recoupled to the pairing channels, $`Q = \sum_J q_J f_J`$, where the channel fractions $`f_J = \lVert[w\otimes w]_J\rVert^2/\lVert w\rVert^4`$ sum to 1 and, with $`j = (d-1)/2`$ the block's spin,

```math
q_J = 1 + 13\,\beta_\rho\begin{Bmatrix} j & j & 6 \\ j & j & J \end{Bmatrix},
```

which for $`R_2`$ gives $`(q_7, q_5, q_3, q_1) = (144/143,\ 196/143,\ 28/11,\ 0)`$.

**Proposition C.**
1. *In $`R_4`$ and $`R_5`$, no ground state lies entirely in the lowest free eigenspace, at any nonzero charge.* Every symmetric-channel coefficient exceeds 1: $`(1288/1287, 35/33, 14/9, 7/3)`$ in $`R_4`$ and $`(2289/2288, 91/88, 21/16, 7/4)`$ in $`R_5`$, at $`F = (6, 4, 2, 0)`$. So $`Q > 1`$, no lowest-level section has constant norm, and Lemma 3 excludes a lowest-level ground state. This does not exclude a ground state lying in one higher free eigenspace with constant norm; whether such sections exist is not examined, and at large charge the quartic term, which grows as $`m^2`$, can outweigh the level term, which grows as $`m`$.
2. *In $`R_2`$ the same holds if and only if no unit vector of the block has $`(ww^{\dagger})_6 = 0`$.* Whether one does is OPEN; the smallest $`Q`$ found numerically is 144/143.
3. *At small charge in $`R_4`$ and $`R_5`$*, the ground states should concentrate on the lowest level with their direction tending to the coherent orbit. That the coherent orbit is the unique minimizer of $`Q`$ is derived: $`q_6`$ is the strictly smallest coefficient, and $`f_6 = 1`$ exactly on coherent states. The limit itself is INFERRED, from a rescaling argument not written here.

## V. What It Earns, and What It Does Not

**What it earns.** Theorem B gives the rigid slots' exact branches an orbital-stability theorem at every nonzero charge. That supplies the orbital-stability alternative of the slot action's §VII for those branches, under M8.4's label "nonlinear persistence of the installed free structure", since their shape never changes; on OpenWave, the rung is a filing's to adjudicate. Theorem A gives every slot, at every nonzero charge, an orbitally stable set of standing-wave ground states. In the soft slots that is a stable set at each charge, not a branch shown continuous in the charge, and M8.2's literal rung asks for "stable nonlinear branches / defects", so there a filing must also adjudicate whether sets suffice, unless that continuity is proved.

**The stability mechanism is generic.** Theorem A holds for a defocusing quartic on any compact manifold of dimension at most three. Theorem B applies wherever the whole lowest eigenspace consists of constant-norm sections, and 2I's representation theory decides that this happens here exactly in the control and in $`R_1, R_3, R_6, R_7`$ and $`R_8`$, the slots §VI item 6 of the slot action names. What is specific to 2I is which slots are rigid, the coherent orbit that minimizes the reduced quartic in $`R_4`$ and $`R_5`$ (its role as the small-charge limit is INFERRED, Proposition C3), and the closed form of §IV. The common structure across the eight slots meets the letter of M8.4's "common finite-amplitude branch or stability structure across the eight under one action", not its intent, and must not be presented as earning more than persistence.

**What it does not give.** It does not give:
- the stability of non-minimizing branches;
- whether a ground-state set is a single orbit;
- smooth dependence on the charge in the soft slots;
- $`R_2`$'s constant-norm question;
- any relation among slot energies (the slot relation is OPEN);
- any physical particle state.

## VI. What Stays Open

- The soft-slot ground states at finite charge: their shape, whether each set is one orbit, and whether they form branches.
- Proposition C2 and C3's limit.
- Non-minimizing branches: the maximum and the saddles of the reduced quartic.

## References

- T. Cazenave and P.-L. Lions, "Orbital stability of standing waves for some nonlinear Schrödinger equations", *Commun. Math. Phys.* **85** (1982) 549–561, doi:[10.1007/BF01403504](https://doi.org/10.1007/BF01403504).
- J. Shatah, "Stable standing waves of nonlinear Klein-Gordon equations", *Commun. Math. Phys.* **91** (1983) 313–327, doi:[10.1007/BF01208779](https://doi.org/10.1007/BF01208779).
- OpenWave M8.12, the bridge $`Q_\sigma = 1 + w_6(\sigma)\,\hat r_6`$ ([method note §1.5](https://github.com/openwave-labs/openwave/blob/344f4162eb2bc256728c240c31382db277f399b1/openwave/xperiments/m8_mit/research/findings/m8_12_method_note.md#L84)) and G1 ([task](https://github.com/openwave-labs/openwave/blob/344f4162eb2bc256728c240c31382db277f399b1/openwave/xperiments/m8_mit/research/tasks/m8_12_task_details.md#L151)).

## Files

In [`scripts/slot-ground-states/`](scripts/slot-ground-states/), with the SHA-256 of every other file in `SHA256SUMS`:
- `soft_quartic.py`: the group, its characters and McKay distances; each soft slot's projector and its spin content; the closed form of §IV against the group-sum quartic on random states, with a 1% error in $`\beta_\rho`$ as the control; the exact coefficients, with a spin-4 control; and Proposition C1's inequalities. Self-contained, a few seconds.
- `soft_quartic.out`: its output.

---

/ **[`↑top`](#top)** / **[`main`](https://github.com/dmobius3/mode-identity-theory/tree/main/)** / **[`framework`](/files/framework/)** / **[`bedrock`](/files/framework/files/bedrock/)** / **[`working`](/files/framework/files/working/)** / **[`cosmos`](/files/cosmos/)** / **[`spectrum`](/files/spectrum/)** / **[`tools`](/files/tools/)** /
