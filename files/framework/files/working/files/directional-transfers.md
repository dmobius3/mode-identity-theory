<a id="top"></a>
/ **[`main`](https://github.com/dmobius3/mode-identity-theory/tree/main/)** / **[`framework`](/files/framework/)** / **[`bedrock`](/files/framework/files/bedrock/)** / **[`working`](/files/framework/files/working/)** / **[`cosmos`](/files/cosmos/)** / **[`spectrum`](/files/spectrum/)** / **[`tools`](/files/tools/)** /

---

# The Shell-to-Direction Transfers

**Type:** Result
**State:** Closed
**Status (2026-09-15):** Complete as a classification, checked by one script. The positive SU(2)-covariant transfers from a shell covariance to a directional power form an (N+1)-parameter cone, which normalization cuts to an N-simplex, with P1's spectral transfer at its barycenter and the Q-symbol transfer at a vertex. On a real field only the pair sums t_m + t_{-m} act, so the physically distinct transfers form an N/2-simplex, in which Q and the antipodal Q are one vertex. Requiring a normalized transfer to preserve the nodal directions of every pure source selects Q exactly, as a theorem; on a real field the same requirement selects the Q class, with the coherent-state convention quotiented out. Requiring it only for the shell's own invariant, the version that can be formulated from the realized source alone below N = 60, does not: the predicted directional pattern keeps 2, 5 and 8 free parameters at N = 12, 20 and 30, enough to reverse the sign of its leading icosahedral multipole, and an explicit second member is exhibited at each. Strong zero preservation is thereby stated exactly as a sufficient axiom for the Q class; absent it, the projection must supply its own point in the family.
**Summary:** What linearity, positivity and SU(2)-covariance allow for a map from a Molien shell's source covariance to a power over flat wave-vector directions, what a real field reduces that family to, how much of it reaches the prediction, and which extra condition picks the Q class out of it.
**Inputs:** `molien-p1-bridge.md` §II, §V-VI, `molien-shells.md`, `stress-tensor-bridge.md` C7 and R7, `../../bedrock/files/surviving-ray.md` §2.2, §2.3, §3.4, §5.3, §5.7, §5.9, `scripts/directional-transfer/transfer_classification.py`
**Parent:** `stress-tensor-bridge.md`

---

## I. The question

[The P1 Bridge](molien-p1-bridge.md) left one statement missing: why MIT's projection from the static $`S^3`$ to flat slices should act on the source as the Q-symbol map, or as any other. It argued for Q on positivity, and said so plainly: positivity singles out Q among the standard symbols, and does not derive it, since other positive covariant transforms can be built.

This page builds them. It asks the classification question directly.

> What are all the positive, linear, SU(2)-covariant maps from a shell covariance operator on $`\mathrm{Sym}^N`$ to a nonnegative power over directions on $`S^2`$?

The answer is a cone of $`N+1`$ nonnegative weights, which normalization cuts to an $`N`$-simplex; on a real field only the pair sums $`t_m + t_{-m}`$ act, which leaves an $`N/2`$-simplex. P1 sits at the barycenter and Q at a vertex, so the choice between them is not a choice between a natural map and an exotic one; it is a choice of a point in a family that the geometry fixes and does not choose from. Most of that freedom never reaches the prediction, because below $`N = 60`$ the source on a shell is a single state. What selects a point is an extra condition, and the calculation below finds one that works, finds that the realized source alone cannot formulate it, and measures the gap in the prediction itself.

This is [the Stress-Tensor Bridge](stress-tensor-bridge.md)'s R7, first calculation. Within the fluctuation half of the projection's specification it classifies the directional part, shell by shell (§II), and it touches neither the background half nor the lapse.

## II. The classification

Shell $`N`$ carries $`\mathrm{Sym}^N`$, the spin-$`j`$ irreducible with $`j = N/2`$. A transfer $`\Phi_N`$ takes a covariance $`A`$ on that space to a power $`A^\text{eff}(\hat n)`$ over directions. Ask three things of it: linearity, positivity ($`A \succeq 0`$ gives $`A^\text{eff}(\hat n) \ge 0`$ at every $`\hat n`$), and SU(2)-covariance.

Linearity on a finite-dimensional operator space gives, for each direction, an operator $`E_N(\hat n)`$ with

```math
\Phi_N(A)(\hat n) = \mathrm{Tr}\!\left[A\, E_N(\hat n)\right].
```

Positivity is then exactly $`E_N(\hat n) \succeq 0`$, since $`\mathrm{Tr}[AE] \ge 0`$ for every $`A \succeq 0`$ holds precisely when $`E \succeq 0`$. Covariance is

```math
E_N(g\hat n) = \rho_N(g)\, E_N(\hat n)\, \rho_N(g)^\dagger ,
```

so the whole transfer is fixed by its value at one direction. Take the pole. The stabilizer of $`\hat z`$ is the $`U(1)`$ of rotations about it, so $`E_N(\hat z)`$ commutes with $`J_z`$, whose spectrum on a single irreducible is simple. Hence $`E_N(\hat z)`$ is diagonal in the spin basis:

```math
E_N(\hat z) = \sum_{m=-j}^{j} t_m\, \lvert j,m\rangle\langle j,m\rvert, \qquad t_m \ge 0 .
```

Conversely, every such diagonal $`E_N(\hat z)`$ defines a covariant family, since the rotations carrying $`\hat z`$ to $`\hat n`$ differ only by a rotation about $`\hat z`$, which commutes with it.

**This calculation is shell-local.** It conditions on the premise it inherits from [the P1 Bridge](molien-p1-bridge.md), that each shell keeps its wavenumber: shell $`N`$ is carried to the flat radial shell at $`k_N = \sqrt{N(N+2)}/R`$, where every homogeneous flat map in that page's §V puts it, and the remaining question is how its covariance is distributed over directions. Invariance under the quotient's isometries makes the source covariance block-diagonal in $`N`$ (the P1 Bridge §II), which removes covariance between shells, but it does not by itself prove that an effective projection cannot mix the surviving diagonal blocks: each $`\mathrm{End}(\mathrm{Sym}^N)`$ holds every rank from 0 to $`N`$, so different shells share their low ranks, and a positive covariant map could add, say, one shell's trace to another shell's output. Radial-shell mixing, and anything else a projection does to the radial label, is outside this classification. **(Pointer added 2026-09-15.)** [The Shell-to-Radius Transfers](radial-transfers.md) takes up the radial label.

**The family.** The admissible transfers are the nonnegative vectors $`(t_{-j}, \ldots, t_j)`$, an $`(N+1)`$-parameter cone. Normalization fixes the total power over directions at the value P1 and Q share, $`\int \Phi_N(A)\, d\Omega = 4\pi\, \mathrm{Tr}[A]/(N+1)`$, which is the condition $`\sum_m t_m = 1`$, and it cuts the cone to an $`N`$-simplex. The record checks the key step on random rotations at $`N = 12, 20, 24`$ and $`30`$: a diagonal $`E_N(\hat z)`$ gives a covariant family to below $`10^{-12}`$, and a generic one misses covariance by more than $`10^{-3}`$.

**The same family, rank by rank.** Operators on $`\mathrm{Sym}^N`$ split under rotation into multipole ranks $`k = 0, \ldots, N`$, the state-multipole expansion that [the Surviving Ray](../../bedrock/files/surviving-ray.md) §2.3 works in. Because $`E_N(\hat z)`$ commutes with $`J_z`$, it lies in the span of the zonal operators, one at each rank, and the diagonal operators reach every rank once, so the weights $`t_m`$ and the $`N+1`$ rank responses $`e_k(t)`$ determine each other. Covariance then makes a transfer act rank by rank: $`\Phi_N(A)(\hat n) = \sum_k e_k(t)\, a_k(\hat n)`$, with $`a_k`$ the rank-$`k`$ multipole of $`A`$ read along $`\hat n`$, a spherical harmonic of degree $`k`$. P1 answers at rank 0 alone, which is why it keeps only the trace; Q answers at every rank. The zonal operators are even or odd under $`m \to -m`$ as $`k`$ is even or odd, so moving weight between $`t_m`$ and $`t_{-m}`$ changes only the odd-rank responses.

**The real-field quotient.** The source is a real field. Complex conjugation of the harmonics, $`\overline{D^j_{mn}} = (-1)^{m-n} D^j_{-m,-n}`$, acts on each factor of the shell as time reversal $`\Theta`$, so a real field's covariance commutes with $`\Theta`$, and so does the covariance a transfer receives. On such a covariance only the pair sums $`u_0 = t_0`$ and $`u_m = t_m + t_{-m}`$ act: $`\Theta`$ exchanges the eigenstates of $`J\cdot\hat n`$ with eigenvalues $`m`$ and $`-m`$, so $`\langle \hat n, -m|A|\hat n, -m\rangle = \langle \hat n, m|A|\hat n, m\rangle`$ whenever $`A`$ commutes with $`\Theta`$. In rank terms, such a covariance has no odd multipoles, and the antisymmetric part of $`t`$ moves only odd ranks. The physically distinct normalized transfers therefore form the simplex $`u_m \ge 0`$, $`\sum_{m=0}^{j} u_m = 1`$, of dimension $`j = N/2`$, an integer because $`-1 \in 2I`$ acts on $`\mathrm{Sym}^N`$ as $`(-1)^N`$, so every Molien shell has even $`N`$; the record finds no further degeneracy on a generic real covariance (T7). The $`N`$-simplex remains the classification of the complexified problem; the $`N/2`$-simplex is the physical one, and in it Q and the antipodal Q are a single vertex, the Q class.

So **positivity, covariance and normalization do not derive Q.** They do not narrow the choice to a short list either. Whatever selects a transfer is a further condition, and it has $`N`$ directions in which to act, $`N/2`$ of them on a real field.

## III. P1 is the barycenter of the simplex, and Q a vertex

The two maps the bridge kept apart are two distinguished members of this family, which is worth stating in those terms.

| $`t`$ | $`E_N(\hat n)`$ | $`\Phi_N(A)(\hat n)`$ | place in the simplex | the bridge's name |
|---|---|---|---|---|
| uniform, $`t_m = 1/(N+1)`$ | $`I/(N+1)`$, the same at every direction | $`\mathrm{Tr}[A]/(N+1)`$, constant over directions | the barycenter | P1, the spectral transfer |
| $`t_m = \delta_{m,j}`$ | $`\lvert\hat n\rangle\langle\hat n\rvert`$ | $`\langle\hat n\vert A\vert\hat n\rangle`$ | a vertex | the Q-symbol transfer |

The vertices of the simplex are the $`N+1`$ transfers that put all the weight on one $`m`$, and uniform weight is their average, the barycenter, the one member whose $`E_N(\hat z)`$ is invariant under every rotation. That member keeps the trace alone and discards every direction, which is exactly P1's prescription, recovered here as the barycenter of the simplex rather than as a prescription. The vertex at $`m = j`$ puts all the weight on the highest state, which is the coherent state at the pole, and gives the Q-symbol. The vertex at $`m = -j`$ gives the same symbol read at the antipode, $`\langle -\hat n\vert A\vert -\hat n\rangle`$. On a real field (§II) the vertices at $`m`$ and $`-m`$ act alike, so Q and the antipodal Q are one vertex of the physical simplex.

The record checks both named members on a random positive covariance at $`N = 12`$: uniform $`t`$ is direction-independent and equals the trace law to below $`10^{-12}`$, the vertex at $`m = j`$ spans $`7.31`$ over five directions, and the vertex at $`m = -j`$ matches Q at the antipode to below $`10^{-12}`$.

This reframes the bridge's fork. Its §V table sorted three maps by what they carry; two of those, the spectral transfer and the symbol transfer, are now seen to lie in one connected family, the first at the barycenter of the simplex and the second at a vertex, with a continuum of transfers between and around them that carry part of the direction dependence. The pullback stays outside this classification, since it is not homogeneous and does not deliver a power over flat wave-vector directions at all.

## IV. Strong zero preservation selects the ray through Q

Here is a condition that does pick one, a ray of the cone and, with normalization, a vertex. It is the one the Molien shells make natural to ask about, since their sources have nodal directions and those nodes are the geometry's own signature.

> **Strong zero preservation.** For every pure source $`|\psi\rangle`$ on the shell, a direction with no source amplitude keeps none: $`\langle \hat n|\psi\rangle = 0`$ implies $`\Phi_N(|\psi\rangle\langle\psi|)(\hat n) = 0`$.

**Theorem.** A positive, SU(2)-covariant transfer satisfies strong zero preservation if and only if it lies on the ray of the cone through the Q-symbol transfer, that is, if it is a nonnegative multiple of it. Among normalized transfers it is exactly Q.

*Proof.* Every multiple of Q satisfies it, since $`\Phi_Q(|\psi\rangle\langle\psi|)(\hat n) = |\langle\hat n|\psi\rangle|^2`$. Conversely, evaluate at the pole, where the coherent state is $`|j,j\rangle`$. For any $`m_0 \ne j`$, the state $`|j,m_0\rangle`$ is orthogonal to $`|j,j\rangle`$, so the pole is one of its nodal directions, and

```math
\Phi_N(|j,m_0\rangle\langle j,m_0|)(\hat z) = \sum_m t_m \,\bigl|\langle j,m|j,m_0\rangle\bigr|^2 = t_{m_0} .
```

Zero preservation forces $`t_{m_0} = 0`$ for every $`m_0 \ne j`$, so $`E_N(\hat z) = t_j\, |j,j\rangle\langle j,j|`$ and covariance gives $`E_N(\hat n) = t_j\, |\hat n\rangle\langle\hat n|`$: the ray through Q. Normalization, $`\sum_m t_m = 1`$, sets $`t_j = 1`$. $`\blacksquare`$

What the theorem says should be read exactly. The hypothesis names "no source amplitude" by the coherent-state overlap, whose zeros are the Q-symbol's own zeros, so its content is that no other ray of the cone respects those zeros for every pure state, and after normalization no other member of the simplex does, not even one arbitrarily close to Q. The zeros themselves belong to the source rather than to the map: in the stellar convention they are the antipodes of the source's Majorana stars, so the condition asks a transfer to respect a feature every source carries. Written with the lowest-weight state in place of the highest, the same argument selects the vertex at $`m = -j`$ instead. The two conventions disagree about which directions are nodal for a generic source, but not for a source whose constellation is antipodally closed, as is every unique invariant below $`N = 60`$ considered here (§V, §VII), and on such a source the two vertices give the same power.

**On a real field.** The theorem quantifies over every pure state, and a real field supplies only the time-reversal-fixed ones. Among those, $`|j,0\rangle`$ and $`(|j,m_0\rangle + e^{i\alpha}|j,-m_0\rangle)/\sqrt 2`$ for $`0 < m_0 < j`$ are nodal at the pole, where they receive $`u_0`$ and $`u_{m_0}/2`$. So strong zero preservation over the fixed states kills every pair sum below $`u_j`$, and normalization sets $`u_j = t_j + t_{-j} = 1`$. It cannot separate $`t_j`$ from $`t_{-j}`$, and on a real field nothing can: every point of that edge acts as one transfer, the Q class. The coherent-state convention that separates Q from the antipodal Q in the theorem above is quotiented out.

So Q is not merely the symbol that happens to stay nonnegative: it is the unique normalized transfer in the admissible family that never puts power in a direction where the source's coherent-state overlap vanishes, for any source on the shell, and on a real field the Q class is the unique such class.

## V. Weak zero preservation does not select Q

The theorem quantifies over every pure state on the shell. The source does not supply every pure state. Below $`N = 60`$ the shell's covariance is $`\tilde\Sigma_N = P_N|\psi_N\rangle\langle\psi_N|`$ with $`\psi_N`$ the single invariant, so the preservation hypothesis that can be formulated from the realized source alone is the one about that state. Either way preservation is a condition on the map: the source supplies its nodal set, not the preservation of it.

> **Weak zero preservation.** For the shell's own invariant $`\psi_N`$, a direction with no source amplitude keeps none.

Rotate a nodal direction $`v`$ to the pole and write $`\psi_v = D_v^\dagger \psi_N`$. Then $`\Phi_N(|\psi_N\rangle\langle\psi_N|)(v) = \sum_m t_m |\langle j,m|\psi_v\rangle|^2`$, a sum of nonnegative terms, so the condition kills $`t_m`$ exactly on the support of $`\psi_v`$ and constrains nothing else. Because $`\psi_N`$ is invariant and the nodal set is a single $`A_5`$ orbit, every nodal direction gives the same constraint. The symmetries of the nodal axis bound that support. The $`k`$-fold rotation about $`v`$ allows only $`m \equiv 0 \pmod k`$, and the half-turns about axes perpendicular to $`v`$, which also preserve the axis, send $`|j,0\rangle`$ to $`(-1)^j|j,0\rangle`$, so the $`m = 0`$ amplitude vanishes when $`j`$ is odd.

| $`N`$ | nodal set | stabilizer | $`m`$ allowed | support | weights killed | cone left | pair sums left |
|---|---|---|---|---|---|---|---|
| 12 | 12 vertices | 5-fold | 3 values | 3 | 3 of 13 | 10 | 5 of 7 |
| 20 | 20 face centres | 3-fold | 7 values | 7 | 7 of 21 | 14 | 7 of 11 |
| 30 | 30 edge midpoints | 2-fold | 15 values | 14, since $`j = 15`$ is odd | 14 of 31 | 17 | 9 of 16 |

**What reaches the prediction.** The cone measures the freedom left in the map, and most of it never reaches the prediction, because the source the map acts on is a single state. By §II the predicted pattern is $`\sum_k e_k(t)\, s_k(\hat n)`$, with $`s_k`$ the rank-$`k`$ density multipole of $`\psi_N`$, so only the ranks at which the source has a multipole can register, and two facts remove most of them. The source is $`2I`$-invariant, so each of its multipoles lies in the invariants of $`V_k`$, the mechanism [the Surviving Ray](../../bedrock/files/surviving-ray.md) §5.3 applies to its projector, and those exist only at the degrees that carry an $`A_5`$ invariant. And the source is fixed by time reversal, so its odd multipoles vanish, the Surviving Ray's Lemma 2.2, whose argument holds at every integer spin.

For a real field the fixing is automatic at every $`N`$, since its covariance commutes with time reversal (§II); below $`N = 60`$ uniqueness forces it even without reality. Time reversal, here the antiunitary intertwiner of the representation with its conjugate as in the Surviving Ray §2.2 and nothing dynamical, commutes with rotations, so it maps invariants to invariants, and a unique invariant is fixed up to phase. In the functions $`f_m(\hat n) = |\langle j,m|D_{\hat n}^\dagger\psi_N\rangle|^2`$ through which the weights act, the same fact reads $`f_{-m} = f_m`$, since time reversal exchanges the eigenstates of $`J\cdot\hat n`$ with eigenvalues $`m`$ and $`-m`$ while preserving the modulus of an overlap. The extreme pair alone decides it: $`f_j`$ is the Majorana modulus $`|\langle\hat n|\psi_N\rangle|^2`$ and $`f_{-j}(\hat n) = f_j(-\hat n)`$, so $`f_j = f_{-j}`$ already makes the constellation antipodally closed, which fixes the state and matches every pair. At $`N = 60`$, where the invariants form a plane, a generic invariant vector is not fixed by time reversal and its pairing fails, while the fixed ones still pair (T6). Such a vector is a complexified control, not a physical source: a real field's covariance there still commutes with time reversal, and what opens at $`N = 60`$ is only that uniqueness no longer forces it. A fixed state's constellation is antipodally closed, since time reversal acts on constellations as the antipodal map (the Surviving Ray §3.4); T5 sees the same fact from the nodal sets.

What survives is one multipole at each even degree up to $`N`$ that carries an $`A_5`$ invariant, and the record finds every one of them nonzero: ranks 0, 6, 10 and 12 at $`N = 12`$, seven ranks at $`N = 20`$ and twelve at $`N = 30`$. The predicted patterns therefore span exactly 4, 7 and 12 dimensions, and those are the ranks the record measures directly for the span of the $`f_m`$. At $`N = 30`$ degree 30 carries two independent invariants, but the source puts a single multipole there, so the count is 12 and not the 13 invariant harmonics of even degree up to 30. Under weak preservation the spans are 3, 6 and 9. Every $`f_m`$ integrates to $`4\pi/(N+1)`$, so normalization is one condition, and after it:

| $`N`$ | map, complexified | map, real field | weak, complexified | weak, real field | predicted pattern | predicted pattern, weak |
|---|---|---|---|---|---|---|
| 12 | 12 | 6 | 9 | 4 | 3 | **2** |
| 20 | 20 | 10 | 13 | 6 | 6 | **5** |
| 30 | 30 | 15 | 16 | 8 | 11 | **8** |

These counts are dimensions. The complexified and real-field columns differ by the quotient of §II, which is general: moving weight between the vertices at $`m`$ and $`-m`$ changes nothing on any real source. The transfer with $`t_{\pm j} = (1 \pm 1/2)/(N+1)`$ and every other weight at $`1/(N+1)`$ gives $`\psi_N`$ exactly P1's flat pattern, to below $`10^{-12}`$, yet on the coherent source at the pole, which no real field supplies, it puts $`1/(N+1)`$ more power at the pole than at its antipode (T6). What separates the real-field columns from the pattern columns is particular to this source, whose multipoles fill only the invariant degrees: a real-field map keeps 3, 4 and 4 directions that $`\psi_N`$ cannot see, and under weak preservation 2, 1 and none, so at $`N = 30`$ every real-field transfer that weak preservation allows gives a pattern of its own. So on the realized source a directional transfer need not be distinguishable from the spectral one. Q is distinguishable, since its pattern vanishes on the nodal set, but that fingerprint is shared by every member of the weak-preservation family.

What the family leaves open between the common zeros is more than a scale. Across it, the transfer's leading anisotropic response, rank 6 against rank 0, runs from $`-0.91`$ to $`+1.96`$ times Q's value at $`N = 12`$, from $`-0.99`$ to $`+1.00`$ times it at $`N = 20`$ and from $`-0.83`$ to $`+1.00`$ times it at $`N = 30`$ (T7); these are ratios to Q, so no normalization convention moves them. Every member vanishes on the nodal set, but the far end reverses the sign of the pattern's leading icosahedral multipole, and at $`N = 20`$ and 30 Q itself is the positive end, the most anisotropic member in that multipole. The second member the record exhibits, uniform weight on the surviving $`m`$, is an interior sample, at 0.68, 0.09 and 0.02 of Q's value. It vanishes at every nodal direction to below $`10^{-15}`$, and at a non-nodal axis returns $`0.0864`$, $`0.0620`$ and $`0.0408`$ where Q returns $`0.1152`$, $`0.0997`$ and $`0.0801`$. Weak zero preservation cannot tell any of them apart, so the gap a further axiom has to close spans a reversal of sign, not only a rescaling.

## VI. What this leaves

Within shell-local transfers, a sufficient axiom that selects the Q class is now stated exactly; absent it, the projection must supply its own point in the family. An eventual projection owes two separate answers: what it does to the radial label, which this page takes as given (§II), and which point of the physical directional simplex it induces, the family this page classifies.

- **If MIT supplies strong zero preservation**, the Q class follows once the transfer is normalized: Q and the antipodal Q, which act alike on a real field. The bridge's §VI prediction below $`N = 60`$ then becomes a consequence rather than a candidate: the icosahedral pattern of directional power, with zeros on the invariant forms' roots, up to the shell amplitudes and one orientation. R7 would then own the directional part of the fluctuation half outright; the radial label would still rest on the premise of §II.
- **If MIT supplies only weak zero preservation**, the version scoped to the source's own content, the transfer is undetermined, and so is the prediction, by less: two free parameters in the directional pattern at $`N = 12`$, five at $`N = 20`$ and eight at $`N = 30`$, against four, six and eight in the real-field map and nine, thirteen and sixteen in the complexified one. What stays open includes the sign of the pattern's leading icosahedral multipole.
- **If MIT supplies neither**, the classification still stands as the admissible family, and the question becomes which point of the real-field simplex the projection's own construction induces; on a single-state source, only the part of that point visible through the $`f_m`$ matters.

The load-bearing question is therefore physical and sharply posed: **does MIT's projection from the static $`S^3`$ to flat slices have a reason that a direction carrying no source amplitude must carry no effective power, for arbitrary states on the shell and not only for the realized one?** A reason that quantifies over every pure state is a statement about the projection as a map, not about the particular source it is applied to, which is the right shape for something the effective-metric construction would deliver.

Nothing here decides that. Nothing here touches the background half of the projection, the curvature placement or the Λ-dressing of the clock, and nothing here is a cosmological quantity: the ratio table's spectrum is untouched, since power per multipole reads only the angle average.

## VII. Checks

[`transfer_classification.py`](scripts/directional-transfer/transfer_classification.py) is pure representation theory and linear algebra, needing only numpy and scipy, and its record [`transfer_classification.out`](scripts/directional-transfer/transfer_classification.out) reproduces byte for byte from it. Quantities at the roundoff level are printed as bounds, so that differences in roundoff between machines do not reach the record. The script builds $`2I`$ as 120 unit quaternions, takes the spin-$`j`$ representation by exponentiating the su(2) generators on each element's axis and angle, and recovers the rotation axes by order as 12 five-fold, 20 three-fold and 30 two-fold directions. It then checks that covariance forces the diagonal form, against a generic control that fails (T1); the barycenter and the vertex, with the vertex at $`m = -j`$ as the antipodal symbol (T2); the coherent state the strong-preservation proof uses (T3); the weak-preservation supports, the half-turn that removes $`m = 0`$ at $`N = 30`$, and the explicit second member (T4); the nodal sets, with each zero simple (T5); what reaches a single-state source (T6): the source's multipole ranks, the rank reach of the diagonal transfers and the parity of the weight swap, the pairing and where it stops at $`N = 60`$, the common integral, the two spans, and a transfer off the barycenter with P1's pattern on the source; and the real-field quotient (T7): transfers with equal pair sums agreeing on a random time-reversal-invariant covariance and differing on a generic one, the independence of the pair sums, the time-reversal-fixed states behind the real-field theorem, the real-field counts, and the range of the leading anisotropic response across the weak family. Time reversal throughout is $`e^{-i\pi J_y}`$ followed by complex conjugation, the Surviving Ray's $`\Theta_j`$ of §5.9 with its free phase set to 1.

T5 is an independent reproduction of step one's constellations from a different construction: the invariant's overlap with the coherent states vanishes on 12 of 12 five-fold axes at $`N = 12`$, 20 of 20 three-fold axes at $`N = 20`$, and 30 of 30 two-fold axes at $`N = 30`$, with no zeros on the other axis classes, and the count matches the $`2j = N`$ zeros a degree-$`2j`$ Majorana polynomial must have. The orbit-size argument that [the Surviving Ray](../../bedrock/files/surviving-ray.md) §5.7 gives at degree 12 explains all three: the zero set of a $`2I`$-invariant binary form is a union of $`A_5`$ orbits, whose sizes are 12, 20, 30 and 60, so a form of degree 12, 20 or 30 vanishes on the single orbit of that size, each zero simple. Each nodal set is antipodally closed, so the zero set of the overlap and the Majorana constellation agree as sets on these shells; that agreement is a property of these states and is not claimed in general.

Not computed: anything about the background projection, any cosmological quantity, and any reason for either preservation hypothesis.

---

/ **[`↑top`](#top)** / **[`main`](https://github.com/dmobius3/mode-identity-theory/tree/main/)** / **[`framework`](/files/framework/)** / **[`bedrock`](/files/framework/files/bedrock/)** / **[`working`](/files/framework/files/working/)** / **[`cosmos`](/files/cosmos/)** / **[`spectrum`](/files/spectrum/)** / **[`tools`](/files/tools/)** /
