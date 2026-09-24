<a id="top"></a>
/ **[`main`](https://github.com/dmobius3/mode-identity-theory/tree/main/)** / **[`framework`](/files/framework/)** / **[`bedrock`](/files/framework/files/bedrock/)** / **[`working`](/files/framework/files/working/)** / **[`cosmos`](/files/cosmos/)** / **[`spectrum`](/files/spectrum/)** / **[`tools`](/files/tools/)** /

---

# 💫 Surviving Ray

<img src="https://github.com/dmobius3/mode-identity-theory/blob/main/files/assets/surviving_ray.png?raw=true" width="100%" alt="Surviving Ray">

The spin-3 representation admits a four-dimensional family of equivariant cubic self-maps, the
family known in the spinor-condensate literature as the four total-spin scattering channels. On
$`S^3/2I`$, for a block state at level 6 with the density-type interaction
$`\lvert\psi\rvert^2\psi`$, binary-icosahedral symmetry restricts that family to two channels, one
of them radial; modulo the radial direction the surviving interaction is a single projective ray.
The interaction is a hypothesis and not a consequence: a different local $`2I`$-invariant quartic,
built from $`\psi\psi^T`$, is filtered by the same mechanism onto a different plane. The density
of a block state is a function on the quotient, so a channel of rank $`K`$ survives only when $`V_K`$
carries a $`2I`$-invariant, and in the density's window, ranks 0 through 6, only $`K = 0`$ and
$`K = 6`$ do. The quartic functional reduces with the interaction, to an affine function of the top
multipole $`\lVert \rho_6 \rVert^2`$ whose coefficient is given in closed form by the branching, not
fitted. Separately, and with no icosahedral input, the spin-8 cubic channel built from the same
spin-3 data closes exactly on the time-reversal-invariant rays. The ingredients are classical: the
Jacobian criterion for nonzero binary forms of equal degree, the Majorana representation with its
time-reversal reading, and Peter-Weyl on $`S^3`$. One result established here is the channel filter
and the selection it forces for that interaction, together with an accounting of which parts of the
arithmetic are icosahedral and which are universal facts about spin 3 with time reversal.

In the coordinates of that literature the surviving ray is one coupling point, by a polynomial
identity with the spin-3 mean-field energy, where the literature has the stationary states and,
numerically, the ground states. This paper gives an audited census within a stated class,
certified critical orbits outside it, and exact results at the two ends. Within the class of orbits
whose fixed locus has projective dimension at most one there are exactly ten critical orbits, with
their Morse indices; three outside it are certified by interval arithmetic, and with them the index
no longer increases with the value. On the unit sphere, $`\lVert\rho_6\rVert^2`$ is least exactly on
the coherent states, through an identity that brings in the Beauzamy-Bombieri-Enflo-Montgomery
inequality with Reznick's equality case, and greatest, at $`463/924`$, exactly on the hexagon orbit
(Theorem 7.5), with the steps an audit supplied marked in its proof. Back on the quotient, the first
correction at the four symmetry-pinned rays is exact and was reproduced blind, and local branch germs
exist, for sufficiently small amplitude, at the six rays of Section 7.1, where they are expanded, and
by the same theorem at $`v_1`$ and $`v_2`$, as an audited argument. The icosahedral content is the
selection and the setting of the branch problem; everything at the point is spin 3, and the point is
where this interaction lands, not the coupling of a physical condensate.

---

## 1. Introduction

Spin-3 states carry a well-studied geometry. The Majorana representation sends a state to six points
on the sphere, rotations act on the constellation, and a substantial literature studies the
constellations that extremise natural invariants: the anticoherent states, whose low multipoles
vanish, and the polyhedral configurations that realise them. Barnett, Turner and Demler [BTD]
show four six-vertex constellations as spin-3 phases in that language. Within this setting the
invariant quartics of a spin-3 state form a four-dimensional space, and particular members of that
family have been studied along with the symmetric constellations attached to them. Any statement
about a particular quartic is therefore a statement about a member of a family the community will
already recognise.

The question here is not which member is interesting but which member a geometry permits *for a given
interaction*. Modes on the spherical space form $`S^3/2I`$ organise into flat bundles indexed by
representations $`\sigma`$ of the binary icosahedral group. At level 6 a block state has left spin 3,
so its self-interaction lies in the four-dimensional family above; the question is what the quotient
does to that family. The answer is a filter. The density $`\lvert\psi\rvert^2`$ of a section is a
genuine function on $`S^3/2I`$, and by Peter-Weyl its level-$`2K`$ component factors into a left
multipole, built from the spin-3 data alone, and a right multipole, which lives in the
$`2I`$-invariants of $`V_K`$. Beyond the scalar invariant at level 0, the next appears at level 12 and
the next after that at level 20, so across ranks 0 through 6 exactly two channels are open. Everything
else is switched off, not because the left-hand tensor vanishes, which it does not, but because its
right-hand coefficient does.

Two results follow. As proved they are independent, neither using the other; Section 5.7 later
combines the ambient proposition with the quotient calculation.

The first is ambient and uses no icosahedral input. For spin 3 with time reversal $`\Theta`$, the
spin-8 cubic channel assembled from a state, its time reverse, and itself again vanishes precisely
on the time-reversal-invariant rays. In the language of constellations, the channel closes exactly
when the six Majorana points are antipodally symmetric as a multiset. The proof is short and rests on a classical fact about binary forms,
that two nonzero forms of the same degree with vanishing Jacobian are proportional, so it is billed
as a proposition rather than a theorem; the possibility that the underlying joint covariant is named
in the classical invariant-theory literature is left open in Section 9 rather than settled here.

The second is the selection, and it takes three steps rather than one. The invariant-degree filter
leaves the density only ranks 0 and 6. The multiplicity-free branching then scalarises the
right-index contraction, without which surviving ranks would not select single maps at all, and puts
the self-interaction in the plane spanned by the rank-0 and rank-6 maps. The rank-0 map is radial,
and the rank-6 coefficient is nonzero, which is earned separately by pairing the interaction against
the quartic. Only then does the self-interaction reduce, modulo the radial direction, to the single
ray generated by the rank-6 map. The governing quartic reduces with it, to an affine function of the
top multipole alone.

The weight attached to the surviving channel is not fitted: it is built from $`\lVert R_6\rVert^2`$,
the norm of the right multipole of an isotypic projector, and is positive because both constituents
of the branching $`V_3\vert_{2I}`$ are proper (Section 5.3).

Little of the surrounding structure is icosahedral. The four-dimensional family, the structure of
the surviving operator, the alternating row of binomial coefficients its weight matrix carries, the
forced form of the time-reversal phase, and the critical rays of the reduced quartic together with
their Majorana constellations are all universal facts about spin 3 with time reversal. None of them
requires $`2I`$ *once the rank-6 channel has been selected*, which is the distinction worth keeping:
$`2I`$ selects, and spin-3 mathematics determines what the selected channel is. For the selection
theorem the icosahedron contributes exactly two facts: the invariant-degree filter, which leaves
density ranks 0 and 6, and the multiplicity-free complementary branching
$`V_3\vert_{2I} = \sigma_3 \oplus \sigma_4`$, which both scalarises the right-index contraction and
supplies the weight. The quotient's representation theory is used elsewhere in the paper for other
purposes, but not by that theorem.

The four-dimensional family is the four-channel spin-3 interaction of the condensate literature [DH],
[KU], and the surviving ray is one coupling point of it: there the governing quartic is an affine image
of the spin-3 mean-field energy, by a polynomial identity (Proposition 6.1). The condensate literature
has the stationary states at that point and, from numerical minimisation, the ground states. The point
is where this interaction lands, and not the coupling of a physical condensate (Section 6.3), and
nothing at the point is offered as evidence for the quotient or for anything physical.

At that point, within the class of orbits whose fixed locus has projective dimension at most one,
there are exactly ten critical orbits, with their values and Morse indices (Section 7); the
classification is an audited argument, and its values were reproduced blind [M8.12]. Three critical
orbits outside the class are certified by interval arithmetic. The minimum of $`\widehat r_6`$ is
$`1/924`$, attained exactly on the coherent states, by an identity that brings the
Beauzamy-Bombieri-Enflo-Montgomery inequality [BBEM], with Reznick's equality case [Re], to the top
multipole; it completes a statement of Björk et al. [Bj]. The maximum is $`463/924`$, attained
exactly on the hexagon orbit (Theorem 7.5); the value and the question are Romero et al.'s [RK], and
the argument was audited on the OpenWave M8 track [M8.13].

Back on the quotient, the selected equation is a bifurcation problem on the flat bundles over
$`S^3/2I`$, with the nonlinearity kept as a hypothesis (Section 8). The first correction at the four
symmetry-pinned rays is exact and was reproduced blind [M8.10]; local branch germs exist, for
sufficiently small amplitude, at the six rays of Section 7.1, where they are expanded, and by the same
theorem at $`v_1`$ and $`v_2`$, as an audited argument [M8.11]. No radius is given for the germs, and
neither result implies stability.

One boundary should be drawn explicitly. The configurations appearing below are known: the octahedral
constellation is the anticoherent state of order 3 in the standard classification, and critical rays
occur here with all four of the six-vertex shape types [BTD] names. Recognising a configuration is not
the same as selecting it, and *configuration prior art is not selection prior art*. The contribution
of the selection is which member of a known family a specific geometry forces, and the surrounding
accounting of what that forcing does and does not explain. At the point the boundary has a companion:
*knowing the phases is not classifying the critical geometry* (Section 7.2).

The sentences above naming the wider constellation literature rest on abstracts and publisher records, and every search is reported as a search (Section 9.3).

Sections 2 to 5 set up the state space, the quotient and the interaction, prove the ambient proposition
and the selection theorem, and derive its consequences across levels and sectors. Section 6 places the
selected interaction in the condensate literature's coupling space, Section 7 gives the critical
geometry there, and Section 8 returns to the quotient. Section 9 gives the limits, the prior art, the
search and the open historical question; the certification closes the page.

---

## 2. Setup

### 2.1 The state space and the Majorana dictionary

Let $`V_j = \mathrm{Sym}^{2j}\mathbb C^2`$ be the irreducible $`\mathrm{SU}(2)`$ representation of
spin $`j`$ and dimension $`2j+1`$, with orthonormal weight basis $`v_m`$, $`-j \le m \le j`$. The
state space throughout is $`V_3`$, of dimension 7. A state $`u = \sum_m u_m v_m`$ is written as the
binary sextic

```math
F_u(z) \;=\; \sum_{m=-3}^3 (-1)^{\,3-m}\sqrt{\binom 6{3+m}}\; u_m\, z^{\,3-m} ,
```

whose six roots on the Riemann sphere are the *Majorana constellation* [Maj] of $`u`$, a multiset of
six points determined by the ray $`[u]`$ and carried by rotations. A finite root $`r`$ is the point
with polar angle $`\theta = 2\arctan\lvert r\rvert`$ and azimuth $`\varphi = \arg r`$, and each
degree by which the polynomial falls short of 6 contributes one point at $`\theta = \pi`$. That
fixes absolute coordinates rather than a shape up to rotation, which is what the identifications in
Section 7.1 require. Statements about constellations below are statements about rays.

### 2.2 Time reversal

Time reversal is the antiunitary $`\Theta`$ on $`V_3`$ acting on coefficients by

```math
\Theta\!\left(\sum_m u_m v_m\right) \;=\; \sum_m (-1)^m\, \overline{u_m}\, v_{-m} ,
```

written in shorthand as $`\Theta v_m = (-1)^m v_{-m}`$ with $`\Theta`$ understood to be antilinear.
Only the overall phase is conventional: antilinear intertwiners of $`V_3`$ with itself form a
one-dimensional space by Schur, and $`\Theta J_+ = -J_- \Theta`$ forces the pattern $`(-1)^m`$, which
supplies the alternating sign in the operator of Section 5. One computes $`\Theta^2 = (-1)^{2j}`$, so
$`\Theta^2 = +1`$ here and $`\Theta^2 = -1`$ at half-integer spin.

*Spin 3* and *time reversal* are representation theory here: nothing below claims a physical spin 3,
and the equation studied is elliptic and stationary, with no time in it, so nothing here establishes a
physical time-reversal symmetry of a dynamics.

A ray is *time-reversal invariant* when $`\Theta u = \lambda u`$ for some $`\lambda`$ of modulus
one, and the set of such $`u`$ is $`U(1)\cdot\mathrm{Fix}(\Theta)`$. The condition is projective:
for $`a \in \mathrm{Fix}(\Theta)`$ and any phase, $`u = e^{it}a`$ has $`\Theta u = e^{-2it}u`$,
which is in general neither $`+u`$ nor $`-u`$. In constellation language a ray is time-reversal
invariant exactly when its six Majorana points are antipodally symmetric *as a multiset*,
coincidences included.

### 2.3 One transform, and three things it is applied to

For $`0 \le J \le 6`$ let $`[\,\cdot \otimes \cdot\,]_J`$ denote the projection of
$`V_3 \otimes V_3`$ onto its spin-$`J`$ summand. For a $`7 \times 7`$ matrix $`P`$ define

```math
\mathcal M_K(P)_N \;=\; \sum_{n+n' = N} \langle 3\,n;\, 3\,n' \mid K\,N \rangle \, (-1)^{n'} P_{n,\,-n'} ,
\qquad 0 \le K \le 6 .
```

This is the state-multipole, or statistical-tensor, expansion of a density matrix in irreducible
tensor operators, standard since [Fa] and used in exactly this form to read multipoles off a
Majorana constellation [RK]. It is written out here because three different arguments are fed to it
below and the paper turns on keeping them apart.

The **holomorphic square** $`B_J(a) = [a \otimes a]_J`$ takes both arguments to be the same state.
Exchanging two identical slots multiplies the spin-$`J`$ summand of $`V_3 \otimes V_3`$ by
$`(-1)^{3+3-J} = (-1)^J`$, so $`B_J`$ vanishes identically for odd $`J`$.

The **density multipole** $`\rho_K(u) = [u \otimes \Theta u]_K`$ is sesquilinear, linear in $`u`$
and antilinear in it through $`\Theta u`$. It equals the transform above at the state's own
projector,

```math
\rho_K(u) \;=\; \mathcal M_K\!\left(u u^\dagger\right) ,
```

and it does not vanish for odd $`K`$ in general.

The **right multipole** is the same transform at a different argument, $`R_K = \mathcal M_K(P)`$
with $`P`$ the isotypic projector of Section 2.4. Same map, different matrix; the two multiply
rather than merge, and Section 5 turns on that.

The factorisation of Section 5 uses this one $`\mathcal M_K`$ on both sides, which is what makes
the two multipoles multiply: the time-reversal phase sits inside $`\mathcal M_K`$ itself, and
$`\rho_K(u) = \mathcal M_K(u u^\dagger)`$ holds because
$`(\Theta u)_{n'} = (-1)^{n'}\overline{u_{-n'}}`$ is exactly the factor the definition carries.

Two notational distinctions matter throughout. $`\rho_K`$ with a subscript is always a density
multipole and never a representation of $`2I`$; representations are written $`\sigma`$ throughout.
The index $`K`$ on a multipole is a spin, as is the $`J`$ on $`B_J`$, and spins on different
decompositions are not comparable: Section 3 works at output spin 8, Section 5 at density rank 6.

> **Lemma 2.2.** $`\rho_1(u) = \rho_3(u) = \rho_5(u) = 0`$ if and only if $`[u]`$ is
> time-reversal invariant.

If $`\Theta u = \lambda u`$ then $`\rho_K(u) = \lambda [u \otimes u]_K`$, which vanishes for odd
$`K`$ by the exchange sign. Conversely, if every odd projection of $`u \otimes \Theta u`$ vanishes
then the tensor is supported in the even summands, on which the exchange acts trivially, so
$`u \otimes \Theta u = \Theta u \otimes u`$; for a nonzero simple tensor that forces $`\Theta u`$
proportional to $`u`$, and antiunitarity makes the constant a phase. $`\square`$

### 2.4 The quotient, its sectors, and the invariant degrees

Identify $`S^3`$ with $`\mathrm{SU}(2)`$ carrying the round metric, let
$`2I \subset \mathrm{SU}(2)`$ be the binary icosahedral group of order 120 acting by right
translation, and write $`X = S^3/2I`$ for the resulting spherical space form. A finite-dimensional
unitary representation $`\sigma`$ of $`2I`$ determines a flat bundle on $`X`$, whose sections are
the functions $`\psi \colon \mathrm{SU}(2) \to \mathbb C^{\dim\sigma}`$, written as rows,
satisfying $`\psi(gh) = \psi(g)\,\sigma(h)`$ for $`h \in 2I`$. An intertwiner
$`\eta \in \mathrm{Hom}_{2I}(\sigma, V_j)`$ is correspondingly a map with
$`D^j(h)\,\eta = \eta\,\sigma(h)`$, and by Peter-Weyl the sections at level $`\ell = 2j`$ are
$`V_j \otimes \mathrm{Hom}_{2I}(\sigma,\, V_j)`$, realised as

```math
\psi_a(g) \;=\; \sum_{m,n} u_m\, D^j_{mn}(g)\, \eta_{na} ,
```

so the left index is free and the right index carries the sector. Since $`\sigma`$ is unitary,
$`\lvert\psi(gh)\rvert^2 = \lvert\psi(g)\rvert^2`$, so the density really is a function on $`X`$. A
*block state* at level 6 is one for which $`j = 3`$, so its left index runs over the $`V_3`$ of
Section 2.1 and its right index over a multiplicity space that the branching below shows to be
one-dimensional. **Level 6 is the scope of the selection theorem of Sections 4 through 5.5.** What
fixes it is the choice of object: this paper is about spin-3 states, so the left index is $`V_3`$
and the level is $`2 \cdot 3`$.

Two facts about $`2I`$ drive the selection theorem, both classical and both recomputed here from the
group rather than cited. They are the two inputs named in Section 5.1. First, the dimensions of the
invariants,

```math
\dim (V_j)^{2I} \;=\; 1,\,0,\,0,\,0,\,0,\,0,\,1,\,0,\,0,\,0,\,1,\,0,\,1,\,0,\,0,\,1
\qquad (j = 0,\dots,15),
```

so invariants occur at levels 0, 12, 20, 24 and 30. Only the gap below
level 12 is used below. Second, the branching of the state space itself. $`V_3`$ has integer spin,
so $`-I`$ acts trivially and $`V_3`$ factors through $`2I/\{\pm I\} \cong A_5`$, whose irreducible
dimensions are $`1, 3, 3, 4, 5`$. The character sum gives $`\langle \chi, \chi \rangle = 2`$, so the
restriction is multiplicity-free with two constituents, and $`\dim (V_3)^{2I} = 0`$ excludes the
trivial one. The two-dimensional irreducible representations of $`2I`$ are spinorial, so they cannot
occur where $`-I`$ acts trivially, which is precisely what factoring through $`A_5`$ means; $`A_5`$
itself has no two-dimensional irreducible representation. Hence

```math
V_3\vert_{2I} \;=\; \sigma_3 \oplus \sigma_4 , \qquad \dim\sigma_3 + \dim\sigma_4 = 3 + 4 = 7 .
```

The two sectors a block state can occupy are therefore **complementary in** $`\dim V_3`$. What that
buys is specific: the surviving weight computed in Section 5 is $`\lVert R_6 \rVert^2 = d(7-d)/7`$
with $`d = \dim\sigma`$, an expression symmetric under $`d \leftrightarrow 7-d`$, so the symmetry
itself makes the two sectors carry the same value, and it is positive for both because
$`0 < d < 7`$.

Since $`\sigma`$ occurs with multiplicity one, $`\mathrm{Hom}_{2I}(\sigma, V_3)`$ is
one-dimensional. For any nonzero intertwiner $`\eta`$ in it, Schur gives
$`\eta^\dagger\eta = c\, I_\sigma`$; rescale so that $`c = 1`$, so that $`P = \eta\eta^\dagger`$
is the orthogonal projector onto the $`\sigma`$-summand of $`V_3`$.

### 2.5 The interaction, and what the results are relative to

Everything below concerns one interaction, fixed here so that Sections 4 to 8 read off a single
definition rather than several. The problem is

```math
(-\Delta - \lambda)\psi \;+\; g\,\lvert\psi\rvert^2\psi \;=\; 0 ,
\qquad \lambda \text{ near the level-6 eigenvalue,}
```

**the self-interaction** means the block projection of $`\lvert\psi\rvert^2\psi`$ onto the level-6
eigenspace, and the quartic is the ratio
$`Q = \int\lvert\psi\rvert^4 / (\int\lvert\psi\rvert^2)^2`$.

Nothing below determines $`g`$. For the channel-selection question a nonzero magnitude can be
absorbed into the amplitude, since the problem is projective in $`\psi`$ and $`g`$ rescales the
amplitude at which a given ray solves it. Absorbing $`\lvert g\rvert`$ leaves the sign, which no
rescaling removes, and that sign is immaterial here because an overall nonzero real factor does not
move the tangential critical equation, though it matters in Sections 6 to 8, where the indices, the
least-energy ray and the direction of the germs depend on it (Section 6.2). So $`g = 1`$ is taken throughout, a normalisation rather than
a result: its sign and its physical scale are not derived here, and the 1 is not a computed
coupling.

The choice of interaction is not vacuous: a second local $`2I`$-invariant quartic genuinely exists.
Both $`\sigma_3`$ and $`\sigma_4`$ are real representations: $`V_3`$ has integer spin, so
$`\Theta^2 = +1`$ makes $`\Theta`$ a real structure on it, and the restriction is multiplicity-free
with constituents of *different* dimensions, so $`\Theta`$ cannot exchange them and must preserve
each. Choosing real orthonormal models then gives $`\sigma(h)\sigma(h)^T = I`$. Hence
$`\psi\psi^T`$ is also a genuine function on $`X`$ and $`\int\lvert\psi\psi^T\rvert^2`$ is a
second local, $`2I`$-invariant quartic. The filter of Section 4 applies to it unchanged, since its
right-hand factor is the plain Clebsch-Gordan projection of $`\eta\eta^T`$, carrying neither the
$`\Theta`$ phase nor the index reversal that $`\mathcal M_K`$ carries. That is exactly why the
left-hand factor comes out holomorphic. Either way it lands in the same invariants. Its surviving
left-hand factors are the *holomorphic* squares $`B_0`$ and $`B_6`$ of Section 2.3 rather than
$`\rho_0`$ and $`\rho_6`$, so its interaction is confined to a genuinely different plane; Section
5.5 identifies that plane and shows it differs from the one selected here.

Whether that second plane also reduces to a single ray is **not examined here**; the analogues of
clauses 3 and 4 for the $`N`$ pair have not been computed. What the filter fixes is the plane.
*Which* plane depends on the interaction, so the selection theorem is a statement about the
density-type quartic above and not about local $`2I`$-invariant quartics in general.

---

## 3. The ambient proposition

This section uses no icosahedral input, and everything in it holds for spin 3 with time reversal. The
trilinear data $`(u, \Theta u, u)`$ contracts equivariantly into every $`V_J`$ in
$`\mathrm{Sym}^2 V_3 \otimes V_3`$, and those contractions are the channels of one object indexed by
the spin of the target: the self-interaction is the spin-3 channel, which Sections 4 and 5 select
within, and the covariant below is the spin-8 channel. Section 5.7 shows the spin-8 channel is
populated on $`X`$, with exactly the time-reversal-invariant states annihilating it. The result is a
proposition and not a theorem, its ingredients are classical, and whether the covariant has appeared
before is left open in Section 9; nothing in the paper's contribution rests on the answer.

### 3.1 The cubic covariant

The maps in this paper are not holomorphic cubics, and the distinction has to be made before any
multiplicity is quoted. Holomorphic cubics $`V_3 \to V_J`$ are counted by
$`\mathrm{Hom}_{\mathrm{SU}(2)}(\mathrm{Sym}^3 V_3,\, V_J)`$, and
$`\mathrm{Sym}^3 V_3 = V_1 \oplus 2V_3 \oplus V_4 \oplus V_5 \oplus V_6 \oplus V_7 \oplus V_9`$, of
dimension $`\binom 93 = 84`$ with spin 3 occurring twice: it contains no $`V_8`$, so no
holomorphic cubic into the spin-8 target exists at all. The maps here are of type $`(2,1)`$,
quadratic in the state and antilinear in it through time reversal, so the space to count is

```math
\mathscr E_J \;:=\; \mathrm{Hom}_{\mathrm{SU}(2)}\!\left(\mathrm{Sym}^2 V_3 \otimes \overline{V_3},\, V_J\right)
\;\simeq\;
\mathrm{Hom}_{\mathrm{SU}(2)}\!\left(\mathrm{Sym}^2 V_3 \otimes V_3,\, V_J\right) ,
```

the isomorphism induced by $`\Theta`$, which supplies the linear intertwiner
$`\overline{V_3} \simeq V_3`$. This notation is used for the rest of the paper. An exact weight
count gives

```math
\dim \mathscr E_8 \;=\; 2 - 1 \;=\; 1 ,
```

the weight-8 subspace of $`\mathrm{Sym}^2 V_3 \otimes V_3`$ having dimension 2 and the weight-9
subspace dimension 1, so the covariant is unique up to scale. Call a nonzero representative $`T`$,
taken in polarised form,

```math
T(x,y,z) \;=\; \tfrac{\kappa}{2}\left[\, x\,(y,z)_1 \;+\; y\,(x,z)_1 \,\right] ,
\qquad \kappa \neq 0 ,
```

where $`x, y, z`$ are the binary sextics attached to three states and $`(\cdot,\cdot)_1`$ is the
first transvectant in the classical sense [GY]. Only the vanishing of $`(f,g)_1`$ is used below, and
$`(f,g)_1`$ is a nonzero constant multiple of the Jacobian

```math
J(f,g) \;=\; f_X\, g_Y - f_Y\, g_X ,
```

so the two are interchangeable for that purpose. The constant $`\kappa`$ depends on the
normalisation of $`T`$ and of the transvectant and is not quoted here; that $`\kappa \neq 0`$ is
what the argument uses, and it holds because $`T`$ is nonzero.

The polarised form is the primary statement and its two specialisations are one line each. Setting
$`y = x`$ gives the holomorphic diagonal,

```math
T(a,a,b) \;=\; \kappa\, f \,(f,g)_1 ,
```

and setting $`y = \Theta u`$, $`z = u`$ gives the ambient spin-8 channel used in this paper,

```math
\mathcal C(u) \;:=\; T(u,\, \Theta u,\, u) \;=\; -\tfrac{\kappa}{2}\, F \,(F, \Theta F)_1 ,
```

the second term of the polarisation dropping out because $`(F,F)_1 = 0`$ by antisymmetry.

The two specialisations look independent and are not. Setting $`a = u`$ and $`b = \Theta u`$ in the
first gives $`T(u, u, \Theta u) = \kappa F (F, \Theta F)_1 = -2\,\mathcal C(u)`$, so they differ by
a constant.

Following Section 2.3, $`\mathcal C`$ takes values in $`V_8`$, and is referred to as the spin-8
cubic channel.

### 3.2 The classical input

One classical fact is used, short enough to prove here.

> **Lemma 3.1** (Jacobian criterion). Let $`f, g`$ be **nonzero** binary forms of the **same**
> degree $`n > 0`$ over a field of **characteristic zero**. If $`J(f,g) = 0`$ then $`f`$ and $`g`$ are
> proportional.

Euler's relation gives $`Y f_Y = n f - X f_X`$, and likewise for $`g`$, so that

```math
Y \cdot J(f,g) \;=\; n\left(f_X\, g - f\, g_X\right)
```

as a polynomial identity. Hence $`J(f,g) = 0`$ forces $`f_X g = f g_X`$, that is
$`\partial_X(g/f) = 0`$ wherever $`f \neq 0`$. So $`g/f`$ does not depend on $`X`$, and being
homogeneous of degree 0 it is constant. $`\square`$

The two forms in Section 3.3 are both sextics, so the degree hypothesis is automatic there; Section 5.7
needs a weaker unequal-degree form, developed where it is used.

Because $`\Theta`$ is injective and the dictionary from states to sextics is linear, $`F \neq 0`$
and $`\Theta F \neq 0`$ whenever $`u \neq 0`$. So Lemma 3.1 applies to the pair $`(F, \Theta F)`$ at
every nonzero state.

### 3.3 The kernel, and the proposition that follows from it

> **Lemma 3.2.** For $`a \neq 0`$, the kernel of the linear map $`b \mapsto T(a,a,b)`$ is exactly
> $`\mathbb Ca`$.

By the diagonal specialisation, $`T(a,a,b) = \kappa f (f,g)_1`$, and $`\kappa \neq 0`$ with
$`f \neq 0`$, so the kernel is cut out by $`(f,g)_1 = 0`$. By Lemma 3.1 this holds exactly when
$`g`$ is proportional to $`f`$, that is when $`b \in \mathbb Ca`$. $`\square`$

> **Proposition 3.3.** For $`u \neq 0`$, $`\mathcal C(u) = 0`$ if and only if $`[u]`$ is
> time-reversal invariant. Equivalently,
>
> ```math
> Z(\mathcal C) \;=\; U(1)\cdot\mathrm{Fix}(\Theta) .
> ```

Apply Lemma 3.2 at $`a = u`$, $`b = \Theta u`$. Its kernel condition reads $`T(u,u,\Theta u) = 0`$
if and only if $`\Theta u \in \mathbb Cu`$, and by Section 3.1 that left side is
$`-2\,\mathcal C(u)`$. Antiunitarity makes the constant a phase, so $`\Theta u = \lambda u`$ with
$`\lvert\lambda\rvert = 1`$, which by Section 2.2 is exactly membership in
$`U(1)\cdot\mathrm{Fix}(\Theta)`$. $`\square`$

So the proposition is a corollary rather than a parallel result: one classical criterion, applied
once, yields both statements.

### 3.4 The constellation reading

One standard fact is used: time reversal acts on the Majorana constellation as the antipodal map of
the sphere. Everything else follows in a line. The constellation is the root multiset of the sextic
$`F`$, so by the fundamental theorem of algebra it determines $`[u]`$ and is determined by it; and
$`\Theta u`$ proportional to $`u`$ says exactly that the antipodal map fixes that multiset, that is,
that the six points are antipodally symmetric, coincidences included. Combining with Proposition
3.3:

> The spin-8 cubic channel closes exactly on the rays whose Majorana constellation is antipodally
> symmetric.

Section 2's Lemma 2.2 reaches the same locus by a different route, through the vanishing of the odd
density multipoles, and the agreement is a useful check rather than a second proof: one argument
runs through the Jacobian criterion on binary forms, the other through the exchange symmetry of a
simple tensor.

---

## 4. The reduction

### 4.1 The density is bandlimited

Let $`\psi`$ be a block state at level 6, so its left index runs over $`V_3`$. Its density
$`\lvert\psi\rvert^2`$ is a function on $`X = S^3/2I`$, and by Section 2.4 its level-$`2K`$
component lies in

```math
V_K \otimes \left(V_K\right)^{2I} ,
```

the left factor built from the spin-3 data and the right factor from the sector. A level therefore
survives only when $`\left(V_K\right)^{2I} \neq 0`$.

The density's left content is $`V_3 \otimes \overline{V_3}`$, which spans ranks 0 through 6, that is
levels 0 through 12. That window is closed: the density cannot reach beyond level 12, so what
happens at level 20 and above is irrelevant to it. Within the window, the dimensions recorded in
Section 2.4 leave exactly two survivors, at levels 0 and 12 (Figure 1).

> **Lemma 4.1.** The density of a block state at level 6 has the form
>
> ```math
> \lvert\psi\rvert^2 \;=\; c_0 \;+\; d_{12} ,
> ```
>
> a constant plus a level-12 component. No intermediate level occurs.

<img src="https://github.com/dmobius3/mode-identity-theory/blob/main/files/assets/channel-filter.png?raw=true" width="75%" alt="The channel filter: the left factor is nonzero at every rank from 0 to 6, the right factor only at ranks 0 and 6, so the self-interaction lies in the span of M0 and M6 and, modulo the radial M0, is the single ray M6">

**Figure 1.** The channel filter. At level 6 the left factor $`\rho_K(u)`$ of the density's level-$`2K`$ component is generically nonzero at every rank $`K = 0, \dots, 6`$, but the right factor $`R_K(P)`$ lies in $`(V_K)^{2I}`$, which is zero except at $`K = 0`$ and $`K = 6`$ (Lemma 4.1). Only those two channels survive: the self-interaction lies in $`\mathrm{span}\{M_0, M_6\}`$ with $`M_0`$ radial, and modulo the radial direction it spans the single projective ray $`[M_6]`$ (Theorem 5.1).

This is the first of the paper's two icosahedral inputs, the invariant-degree filter; the second, the
multiplicity-free branching, scalarises the right-index contraction in Section 5.1 and supplies the
weight in Section 5.3. Lemma 4.1 concerns the coefficients of the density's expansion, not the tensors
that carry them: the density multipoles $`\rho_K(u)`$ are generically nonzero at every rank.

### 4.2 The four-dimensional family

The other side of the reduction is what there is to select from: the type-$`(2,1)`$ self-maps of
$`V_3`$, which by Section 3.1 form the space $`\mathscr E_3`$. The weight count gives

```math
\dim \mathscr E_3 \;=\; 16 - 12 \;=\; 4 ,
```

the weight-3 subspace having dimension 16 and the weight-4 subspace dimension 12. Both counts in
this paper are of that form and both can be checked on the page.

This family is not new. A spin-3 contact interaction is specified by four scattering lengths, one
for each total-spin channel $`S = 0, 2, 4, 6`$, and the resulting mean-field energy is the
corresponding four-parameter combination [DH], [KU]. That is the same four-dimensional space, in the
$`N_J`$ indexing below. Nothing in this paper claims the family; what is claimed is what the
quotient does to it.

There is also a structural derivation, and it comes with a basis. Since
$`\mathrm{Sym}^2 V_3 = V_0 \oplus V_2 \oplus V_4 \oplus V_6`$, each summand once, and since $`V_3`$
occurs exactly once in $`V_J \otimes V_3`$ for every $`J \le 6`$,

```math
\mathscr E_3 \;=\; \bigoplus_{J = 0,2,4,6} \mathrm{Hom}_{\mathrm{SU}(2)}\!\left(V_J \otimes V_3,\, V_3\right) ,
```

four summands, each one-dimensional. A generator of the $`J`$-th is

```math
N_J(u) \;=\; \left[\, [u \otimes u]_J \otimes \Theta u \,\right]_3 ,
\qquad J = 0, 2, 4, 6 ,
```

built from the *holomorphic* square of Section 2.3, which is why only even $`J`$ occurs: the odd
$`N_J`$ vanish identically by the exchange sign, the same fact as $`B_J = 0`$ for odd $`J`$.

The maps the selection is naturally phrased in are indexed instead by the density's ranks. For
$`0 \le K \le 6`$ put

```math
A_K(u)\,v \;=\; \left[\, \rho_K(u) \otimes v \,\right]_3 ,
\qquad
M_K(u) \;=\; A_K(u)\, u ,
```

so $`A_K(u)`$ is a *linear operator* on $`V_3`$ with the density frozen at $`u`$, and $`M_K`$ is the
*cubic self-map* obtained by feeding the same state back in. The distinction is not cosmetic and
Section 5 will need it.

So the family has two natural indexings, which Section 2.3 keeps apart: the canonical basis $`N_J`$ by
the ranks of the holomorphic square, and the $`M_K`$ by the ranks of the density, related by
recoupling. The seven $`M_K`$ are linearly dependent and span $`\mathscr E_3`$, verified by exact
computation; the selection argument does not use the spanning, and needs only that $`M_6`$ is not
radial, which Section 5 proves.

### 4.3 The spine

These are the two targets named at the head of Section 3, and the contrast between them is what
gives the paper its shape. Put the counts side by side.

```math
\dim \mathscr E_8 = 1 , \qquad \dim \mathscr E_3 = 4 .
```

The spin-8 target is rigid: its type-$`(2,1)`$ covariant space is one-dimensional, so there is no
nontrivial projective choice for a geometry to make within it. A geometry might still decide whether
that channel appears, or with what coefficient; what it cannot do is choose among projectively
distinct maps, because there is only one ray. The spin-3 target is four-dimensional, so channel
selection has genuine content there.

The same method answers the corresponding *availability* question, whether the quotient supplies a
compatible spin-8 target slot at all. Both $`V_3`$ and $`V_8`$ have integer spin and so factor
through $`A_5`$, and the branching is

| level | dim | $`\mathbf 1`$ | $`\mathbf 3`$ | $`\mathbf 3'`$ | $`\mathbf 4`$ | $`\mathbf 5`$ |
|---|---|---|---|---|---|---|
| 6 | 7 | 0 | 0 | 1 | 1 | 0 |
| 12 | 13 | 1 | 1 | 0 | 1 | 1 |
| 16 | 17 | 0 | 0 | 1 | 1 | 2 |

The two constituents of $`V_3`$ are $`\mathbf 3'`$ and $`\mathbf 4`$, and both occur in $`V_8`$
with multiplicity one, so both sectors occurring at level 6 also occur at level 16 and the spin-8
target is available in either. That is what the table establishes and all that is claimed here: it
says the slot exists, not that the particular covariant has nonzero coefficient into it, which would
need a right-index contraction for $`\mathcal C`$ of the kind Section 5 carries out for the
density. The slot is at least reachable: by Lemma 4.1 the density has levels 0 and 12 only, level 0
times level 6 returns level 6 alone, and level 12 times level 6 spans levels 6 through 18. So the
entire level-16 output comes from $`d_{12}\psi`$, and the only obstruction is whether the right-hand
factor vanishes. That is settled in Section 5.7, which needs the weight computed in Section 5.3 and
so cannot be argued here: it does not vanish, and the channel is populated in both sectors.

### 4.4 What the reduction cannot touch

Lemma 4.1 constrains the density's spectrum and nothing else: $`\mathscr E_3`$, its canonical basis
$`N_J`$, the operators $`A_K`$ and the maps $`M_K`$ are fixed before $`2I`$ is mentioned, the same for
any system carrying spin 3 with time reversal. The family is universal, and the quotient selects the
nonradial ray and its weight.

---

## 5. The selection theorem

### 5.1 Statement

> **Theorem 5.1.** Let $`\psi`$ be a block state at level 6 on $`X = S^3/2I`$, in the sector
> $`\sigma`$, write $`d = \dim\sigma \in \{3,4\}`$, and take the self-interaction and the quartic
> to be those of Section 2.5, namely the block projection of $`\lvert\psi\rvert^2\psi`$ and the
> ratio built from $`\int\lvert\psi\rvert^4`$. Then:
>
> 1. the self-interaction lies in $`\mathrm{span}\{M_0, M_6\} \subset \mathscr E_3`$;
> 2. $`M_0`$ is radial, $`M_0(u) = -\lVert u\rVert^2 u/\sqrt 7`$;
> 3. $`M_6`$ is not radial;
> 4. modulo the radial direction the self-interaction spans the **single projective ray**
>    $`[M_6]`$, its coefficient being nonzero by the argument in Section 5.5; on the unit sphere the
>    tangential critical problem is then governed by $`M_6`$ alone;
> 5. on the unit sphere the governing quartic is $`Q = w_0/7 + w_6 \lVert\rho_6\rVert^2`$, with
>
> ```math
> \frac{w_6}{w_0} \;=\; \frac{7-d}{13\,d} \;>\; 0 .
> ```

Clause 1 needs one step beyond Lemma 4.1, which constrains the density and not the self-interaction.
The level-$`2K`$ component of the density multiplies $`\psi`$; the left factor couples to give
$`A_K(u)u = M_K(u)`$, and the right factor contracts against $`\eta`$ to a scalar, by Schur, since
the multiplicity is one. So each surviving level contributes a multiple of its own $`M_K`$ and the
vanishing levels contribute nothing, which with Lemma 4.1 is clause 1. Clauses 2 through 5 are
proved below.

### 5.2 The quartic, and the Peter-Weyl factorisation

Two preliminaries. First, clause 2. The rank-0 coupling contracts $`u`$ against $`\Theta u`$ to a
scalar,

```math
\rho_0(u) \;=\; [u \otimes \Theta u]_0 \;=\; -\frac{\lVert u\rVert^2}{\sqrt 7} ,
\qquad\text{so}\qquad
M_0(u) \;=\; [\rho_0(u) \otimes u]_3 \;=\; -\frac{\lVert u\rVert^2}{\sqrt 7}\, u ,
```

which is clause 2. Within $`\mathscr E_3`$, "radial" and "proportional to $`M_0`$" are the same
condition: a radial equivariant map has the form $`\lambda(u)u`$ with $`\lambda`$ an invariant of
type $`(1,1)`$, and $`\mathrm{Hom}_{\mathrm{SU}(2)}(V_3 \otimes \overline{V_3}, \mathbf 1)`$ is
one-dimensional, so $`\lambda \propto \lVert u\rVert^2`$ and the map is a multiple of $`M_0`$.

Second, the quartic itself, which has two forms. The homogeneous one is

```math
\widetilde{Q}(u) \;=\; \sum_K w_K \lVert \rho_K(u)\rVert^2 ,
```

and the functional actually extremised is its projective normalisation

```math
Q([u]) \;=\; \frac{\widetilde{Q}(u)}{\lVert u\rVert^4} , \qquad u \neq 0 ,
```

which descends to rays and agrees with $`\widetilde{Q}`$ on the unit sphere. Since
$`\lVert\rho_0(u)\rVert^2 = \lVert u\rVert^4/7`$, clause 5 is the value of $`Q`$ there.

The scale of the $`w_K`$ is not a convention either, because the denominator can be carried
explicitly. With Haar measure normalised and $`\eta^\dagger\eta = I_\sigma`$,

```math
\int \lvert\psi\rvert^2 \;=\; \frac 17\lVert u\rVert^2\, \mathrm{tr}\,P \;=\; \frac d7\lVert u\rVert^2 ,
```

so $`(\int\lvert\psi\rvert^2)^2 = (d^2/49)\lVert u\rVert^4`$ and there is no undetermined factor
anywhere.

By the convention fixed in Section 2.4 a section is
$`\psi_a(g) = \sum_{m,n} u_m D^3_{mn}(g)\,\eta_{na}`$. Expanding the density and using
$`D^3 D^3 = \sum_K \langle\cdot\rangle\langle\cdot\rangle D^K`$ separates the two indices: the
level-$`2K`$ component of $`\lvert\psi\rvert^2`$ is

```math
d_{2K} \;=\; \rho_K(u) \otimes R_K(P) , \qquad P = \eta\eta^\dagger ,
```

with both factors the *same* transform $`\mathcal M_K`$ of Section 2.3, applied to $`uu^\dagger`$
on the left and to $`P`$ on the right. Peter-Weyl orthogonality,
$`\int D^K_{MN}\overline{D^{K'}_{M'N'}} = \delta/(2K+1)`$, gives the numerator, while the
normalisation above gives the denominator:

```math
A(u) \;:=\; \int\lvert\psi\rvert^4 \;=\; \sum_K \frac{\lVert\rho_K(u)\rVert^2\,\lVert R_K(P)\rVert^2}{2K+1} ,
\qquad
B(u) \;:=\; \int\lvert\psi\rvert^2 \;=\; \frac d7\lVert u\rVert^2 .
```

Hence

```math
Q([u]) \;=\; \frac{A(u)}{B(u)^2} \;=\; \frac{1}{\lVert u\rVert^4}\sum_K w_K \lVert\rho_K(u)\rVert^2 ,
\qquad
w_K \;=\; \frac{49}{d^2}\cdot\frac{\lVert R_K(P)\rVert^2}{2K+1} ,
```

and $`\widetilde{Q}(u) = \sum_K w_K\lVert\rho_K(u)\rVert^2 = (49/d^2)A(u)`$. With the measure fixed
that way there is no free constant left anywhere, and in particular $`w_0 = (49/d^2)(d^2/7) = 7`$ is
**derived**, not chosen. The measure is the one choice being made, and it is worth saying what
depends on it: $`Q = A/B^2`$ scales inversely with the measure, so the individual $`w_K`$ and the
normalisation of Section 5.6 inherit that choice, while the ratio $`w_6/w_0`$, the selection theorem
and the critical set do not.

Lemma 4.1 in this language says $`R_K(P) = 0`$ for $`K = 1,\dots,5`$, which is a statement about
$`P`$ and leaves $`\rho_K(u)`$ untouched.

The formula is also what defines the individual $`w_K`$: by Sections 9.5, 5.5 and 4.2 the seven
quartics $`\lVert\rho_K\rVert^2`$ span a four-dimensional space, so they satisfy three linear
relations, and the $`w_K`$ are the ones the Peter-Weyl factorisation produces, not coefficients read
off from $`Q`$. Nothing downstream turns on this. Only $`w_0`$ and $`w_6`$ are nonzero, since
$`R_K(P) = 0`$ for $`K = 1,\dots,5`$, and the $`K = 0`$ term is the constant $`w_0/7 = 1`$, so

```math
Q([u]) \;=\; 1 + w_6\,\frac{\lVert\rho_6(u)\rVert^2}{\lVert u\rVert^4} .
```

The ratio on the right is not constant on rays, so $`Q`$ determines $`w_6`$ as its slope against
that ratio: the weight derived in Section 5.3 belongs to the functional, not to the way it is
written.

### 5.3 The weight

> **Lemma 5.2.** $`\lVert R_6(P)\rVert^2 = d(7-d)/7`$, and $`\lVert R_0(P)\rVert^2 = d^2/7`$.

Three steps. First, $`\mathcal M_K`$ obeys a Parseval identity,
$`\sum_K \lVert \mathcal M_K(P)\rVert^2 = \lVert P\rVert_F^2`$ for any $`7\times 7`$ matrix $`P`$.
Second, $`P`$ is an orthogonal projector by the normalisation fixed in Section 2.4, so
$`\lVert P\rVert_F^2 = \mathrm{tr}\,P = d`$. Third, $`R_0(P)_0 = -\mathrm{tr}(P)/\sqrt 7`$, so
$`\lVert R_0\rVert^2 = d^2/7`$. Lemma 4.1 removes every other term from the Parseval sum, leaving

```math
\lVert R_6 \rVert^2 \;=\; d - \frac{d^2}{7} \;=\; \frac{d(7-d)}{7} . \qquad \square
```

The expression $`d(7-d)/7`$ is positive exactly when $`0 < d < 7`$, and Section
2.4 supplies that: $`V_3\vert_{2I}`$ is multiplicity-free with two constituents, of dimensions 3 and
4, so both are proper and neither $`d`$ is 0 or 7. The expression is also symmetric under
$`d \leftrightarrow 7-d`$, so the two sectors carry the *same* value,

```math
\lVert R_6\rVert^2 \;=\; \frac{3 \cdot 4}{7} \;=\; \frac{12}{7} \quad\text{in both},
```

for a reason rather than by coincidence: they are complementary in $`\dim V_3`$. Combining with
Section 5.2,

```math
\frac{w_6}{w_0} \;=\; \frac{\lVert R_6\rVert^2/13}{\lVert R_0\rVert^2/1} \;=\; \frac{7-d}{13\,d}
\;>\; 0 ,
```

which is clause 5. Since $`w_0 = 7`$ was derived rather than chosen, the absolute weight follows
too: $`w_6 = 7(7-d)/(13d)`$, namely $`21/52`$ at $`d = 4`$ and $`28/39`$ at $`d = 3`$.

### 5.4 The surviving operator, and the map it generates

Write $`\Lambda_m = (-1)^{3+m}\binom 6{3+m}`$, the alternating sixth row of Pascal's triangle. At
weight states the frozen-density operator of Section 4.2 is an outer product,

```math
A_6(v_i)\, v_j \;=\; c\, \Lambda_i \Lambda_j\, v_j ,
\qquad
c \;=\; -\frac{1}{\binom{12}6}\sqrt{\frac{\dim V_3}{\dim V_6}} ,
```

diagonal in the second slot. Feeding the same state back in gives the cubic map, which carries
$`\Lambda`$ **squared**:

```math
M_6(v_i) \;=\; c\, \Lambda_i^2\, v_i ,
\qquad
\Lambda^2 \;=\; (1,\, 36,\, 225,\, 400,\, 225,\, 36,\, 1) .
```

The outer product belongs to the operator and the square to the map; they are different objects.

The two factors of $`\Lambda\otimes\Lambda`$ have different origins. In the Condon-Shortley convention

```math
\langle 3\,m;\, 3\,{-m} \mid 6\,0\rangle \;=\; \tfrac{\sqrt{231}}{462}\,(1,\,6,\,15,\,20,\,15,\,6,\,1) ,
\qquad
\langle 6\,0;\, 3\,m \mid 3\,m\rangle \;=\; \tfrac{\sqrt{429}}{858}\,\Lambda ,
```

so the multiplication slot alternates by itself, while the density slot's row is positive and takes its
signs from the phase in $`\Theta`$.

### 5.5 That $`M_6`$ is not radial, and the quartic

Clause 3 is one line from Section 5.4. By Section 5.2, radial and proportional to $`M_0`$ are the
same condition in $`\mathscr E_3`$, so suppose $`M_6 = \alpha M_0`$. Evaluating both at the weight
state $`v_i`$ gives $`c\,\Lambda_i^2 = -\alpha/\sqrt 7`$ for every $`i`$, so $`\Lambda^2`$ would be
constant. It is $`(1, 36, 225, 400, 225, 36, 1)`$. Hence $`M_6`$ is not radial. The same row is why
the second interaction of Section 2.5 lands in the genuinely different plane
$`\mathrm{span}\{N_0, N_6\}`$: $`N_0`$ annihilates every weight state $`v_i`$ with $`i \neq 0`$ and
does not annihilate $`v_0`$, while no combination of $`M_0`$ and $`M_6`$ does that, since this row
is not constant off the centre.

That is not yet clause 4, which also needs the self-interaction to *contain* $`M_6`$ with nonzero
coefficient. Write the self-interaction as $`t_0 M_0 + t_6 M_6`$, which clause 1 permits. It is the
block projection of $`\lvert\psi\rvert^2\psi`$, and the block projection is self-adjoint with
$`\psi`$ in its range, so pairing it with $`\psi`$ returns $`\int\lvert\psi\rvert^4`$, that is
$`\widetilde{Q}`$ up to the normalisation of Section 5.2. Carrying that normalisation explicitly,
the pairing is $`(d/7)\,\langle u, \mathcal I(u)\rangle = A(u)`$, the $`d/7`$ being the block inner
product inherited from $`\int\lvert\psi\rvert^2 = (d/7)\lVert u\rVert^2`$. For a fixed sector
$`\sigma`$, $`t_0`$ and $`t_6`$ are constants determined by the right contractions, and they are not
assumed related. If $`t_6`$ vanished, the self-interaction would be $`t_0 M_0`$, so $`A(u)`$ would
be proportional to $`\langle u, M_0(u)\rangle = -\lVert u\rVert^4/\sqrt 7`$, hence constant on the
unit sphere. It is not: by clause 5, $`\widetilde{Q} = (49/d^2)A`$ is
$`w_0/7 + w_6\lVert\rho_6\rVert^2`$ with $`w_6 > 0`$, and a positive multiple of $`A`$ is constant
only if $`A`$ is, and $`\lVert\rho_6\rVert^2`$ takes the values $`1/\binom{12}6`$ and
$`400/\binom{12}6`$ at $`v_3`$ and $`v_0`$. So $`t_6 \neq 0`$, and with clauses 1 and 2 that is
clause 4. $`\square`$

The same non-constancy appears on the quartic side as an identity worth recording,

```math
\binom{12}6\, \lVert \rho_6(v_m)\rVert^2 \;=\; \Lambda_m^2 ,
```

which is an identity rather than a sample: at a weight state $`\rho_6`$ has only its zonal
component, so $`\lVert\rho_6\rVert^2 = \binom 6{3+m}^2/\binom{12}6`$.

Both coefficients of the self-interaction are available, not only the nonvanishing of the second.
Pairing it with $`u`$ and evaluating at $`v_3`$ and $`v_0`$ gives two linear equations whose
solution, written $`\mathcal I`$ from here on, is

```math
\mathcal I(u) \;=\; \frac d7\lVert u\rVert^2 u \;-\; \frac{7-d}{\sqrt{91}}\, M_6(u) ,
```

the radial part carrying the expected sign. Solved from two states, it holds at the octahedral and
hexagonal rays as well, so it is determined rather than fitted.

Relating the two sides away from weight states is a separate identity:

```math
\nabla_{\bar u} \lVert \rho_K(u)\rVert^2 \;=\; c_K\, M_K(u) ,
\qquad
c_K \;=\; (-1)^{K+1}\, 2\sqrt{\frac{\dim V_K}{\dim V_3}} ,
```

so the quartic weight and the cubic weight differ by a fixed nonzero factor per channel, as an identity
in $`u`$ and $`\bar u`$; Section 9.5 obtains the same correspondence structurally, as an equivariant
isomorphism from the invariant quartics onto $`\mathscr E_3`$. Nothing in Theorem 5.1 depends on it.
Reading nonvanishing of every $`c_K`$ as injectivity would need the spanning fact of Section 4.2, which
is not used here.

One last calculation completes clause 4's second sentence, that on the unit sphere the tangential
critical problem is governed by $`M_6`$ alone. Since $`Q = A/B^2`$ with $`B(u) = (d/7)\lVert u\rVert^2`$,
the gradient of the denominator is radial, so for $`\lVert u\rVert = 1`$,
$`\Pi_{u^\perp}\nabla_{\bar u} Q \propto \Pi_{u^\perp}\mathcal I(u)`$: with clause 1 and $`M_0`$ radial,
the tangential equation involves $`M_6`$ alone, with the nonzero coefficient above. That is clause 4 in full.

### 5.6 The normalisation, and what it does not settle

The theorem is complete; one ceiling belongs here before the discussion, on the constant its weight
is built from. The sector normalisation is $`N = \binom{12}6/w_6`$, and Section 5.3 gives it in
closed form:

```math
N \;=\; \binom{12}6\,\frac{\dim V_6}{\dim V_3}\,\frac{d}{7-d}
\;=\; \binom{13}6\,\frac{d}{7-d} ,
\qquad 1287 \text{ at } d = 3 , \quad 2288 \text{ at } d = 4 .
```

The first form is canonical because it is what the derivation produces: the left Clebsch-Gordan
constant, times the Peter-Weyl dimension ratio, times the sector. The binomial identity
$`\binom{12}6\cdot 13/7 = \binom{13}6`$ is noticed afterwards and is not a new primitive.

Two ceilings belong here rather than in the discussion. First, an earlier form of this
normalisation, $`N = 143\,d^2`$, is **exactly correct on both sectors** and always will be, since
$`d(7-d) = 12`$ at $`d = 3`$ and $`d = 4`$. What the derivation shows is that it is not the
primitive form: the quadratic shape is a consequence of the two sectors being complementary in 7.
Second, and more sharply, $`d = 3`$ and $`d = 4`$ are the only values that occur, so **no
measurement inside this system separates the two formulas**. The
correction is carried entirely by the derivation above and has no empirical content of its own.

### 5.7 The spin-8 channel on the quotient

Section 4.3 left one question open, whether the spin-8 channel whose target slot exists in both
sectors actually carries a nonzero coefficient there. With Lemma 5.2 in hand it closes.

This section's tool is the unequal-degree form of Lemma 3.1. With degrees $`m = \deg f`$ and
$`n = \deg g`$ the same Euler computation gives $`Y \cdot J(f,g) = n f_X g - m f g_X`$, and
$`\partial_X(f^n/g^m) = f^{\,n-1}(n f_X g - m f g_X)/g^{\,m+1}`$, which is zero when
$`J(f,g) = 0`$. So $`f^n/g^m`$ is independent of $`X`$, and being homogeneous of degree zero it is
constant: $`f^n \propto g^m`$, the weaker conclusion available at unequal degrees. Since
$`\mathbb C[X,Y]`$ is a unique factorisation domain, a root of multiplicity $`\mu`$ in $`f`$ then has
multiplicity $`\mu n/m`$ in $`g`$.

The right-hand factor of the level-16 output is built from $`R_6(P)`$, which lies in $`(V_6)^{2I}`$.
That space is one-dimensional by Section 2.4, and its generator has **twelve simple roots**, which
the orbit structure forces and the picture only suggests. The zero divisor of a $`2I`$-invariant
binary form is $`2I`$-invariant, hence a union of orbits of $`A_5`$ on $`\mathbb P^1`$, and those
orbits have sizes 12, 20, 30 and 60, with stabilisers the cyclic groups of orders 5, 3, 2 and 1. A
divisor of degree 12 must therefore be the size-12 orbit taken once, so its roots are twelve
distinct points, the icosahedron's vertices. Lemma 5.2 gives
$`\lVert R_6(P)\rVert^2 = 12/7 \neq 0`$, so $`R_6(P)`$ is a nonzero multiple of that invariant;
write it $`I_{12}`$.

The coupling $`V_6 \otimes V_3 \to V_8`$ is unique up to scale and is the first transvectant, the
degrees $`12`$ and $`6`$ giving order $`12 + 6 - 2 = 16`$. So the question is whether
$`v \mapsto (I_{12}, f_v)_1`$ can kill a nonzero $`v`$. It cannot. If $`(I_{12}, f)_1 = 0`$ with
$`f \neq 0`$, the unequal-degree form gives $`I_{12}^{\,6} \propto f^{\,12}`$, so each root of
$`I_{12}`$ occurs on the left with multiplicity $`6\mu`$ and on the right with multiplicity
$`12\nu`$, forcing $`\mu = 2\nu`$. A root of $`I_{12}`$ has $`\mu \ge 1`$, so $`\nu = 0`$ would give
$`\mu = 0`$, while $`\nu \ge 1`$ gives $`\mu \ge 2`$. Both contradict twelve simple roots.

So $`v \mapsto (I_{12}, f_v)_1`$ is injective, and composing it with the nonzero intertwiner
$`\eta`$ leaves the right-hand factor nonzero in both sectors. The left-hand factor is $`[\rho_6(u)\otimes u]_8`$. Since
$`\dim\mathscr E_8 = 1`$ leaves no other equivariant map, it is *some* multiple of
$`\mathcal C(u)`$, say $`\alpha\,\mathcal C(u)`$; that $`\mathcal C`$ is itself nonzero does not
yet make $`\alpha`$ nonzero, so the constant is evaluated rather than inferred. At $`u = v_3`$,
$`\rho_6(v_3) = -\tfrac{\sqrt{231}}{462}\,v^{(6)}_0`$ and coupling to spin 8 gives
$`[\rho_6(v_3)\otimes v_3]_{8,3} = \tfrac{\sqrt{273}}{1092} \neq 0`$. Hence $`\alpha \neq 0`$. The
level-16 component of the nonlinearity therefore does not vanish identically, and Proposition 3.3
becomes a statement about $`X`$ rather than an ambient one:

> Among block states at level 6, those whose cubic nonlinearity has no level-16 component are
> exactly the time-reversal-invariant ones.

### 5.9 Three corollaries

Three consequences of Theorem 5.1 bracket it from below, across and above. Throughout this
subsection write

```math
\widehat r_6([u]) \;:=\; \frac{\lVert\rho_6(u)\rVert^2}{\lVert u\rVert^4} ,
```

the projective form of the top multipole, which agrees with
$`\lVert\rho_6\rVert^2`$ on the unit sphere of $`V_3`$.

> **Corollary 5.4.** *Nothing projective below level 6.* For a single-sector block state with the
> density-type interaction of Section 2.5, the projected self-interaction is radial at every
> level $`\ell < 6`$. Level 6 is the first level at which $`S^3/2I`$ permits a non-radial cubic
> self-interaction at all.

The transform of Section 2.3 extends to every level with the time-reversal phase written as
$`\Theta_j v_m = \varepsilon_j\,(-1)^{\,j-m}\, v_{-m}`$, $`\lvert\varepsilon_j\rvert = 1`$, which is
defined at integer and half-integer $`j`$ alike, since $`j - m`$ is an integer; Section 2.2's choice
at $`j = 3`$ is $`\varepsilon_3 = -1`$. Below level 6 the restriction $`V_j\vert_{2I}`$ is
irreducible: the character sum gives $`\langle\chi,\chi\rangle = 1`$ at $`2j = 1,\dots,5`$ and first
gives 2 at $`2j = 6`$. So at every level below 6 the sector fills $`V_j`$ and its isotypic projector
is the identity, which is invariant under all of $`\mathrm{SU}(2)`$; $`\mathcal M_K(I)`$ vanishes for
every $`K > 0`$, and the Peter-Weyl factorisation of Section 5.2 retains the $`K = 0`$ term alone.
That term is radial, $`M^{(j)}_0(u) = \varepsilon_j\,(2j+1)^{-1/2}\,\lVert u\rVert^2 u`$, with a
nonzero scalar, so the projected self-interaction is a multiple of the state and no projective
direction is selected. $`\square`$

The argument covers half-integer $`j`$ as readily as integer $`j`$, so levels 1, 3 and 5 are covered on
the same footing as 2 and 4, and it uses Schur's lemma, not the icosahedral invariant gap.

> **Corollary 5.5.** *The two sectors select the same shapes.* The reduced quartics of the two
> sectors have the same critical set on $`\mathbb P(V_3)`$, with the same ordering of values.

By clause 5, $`Q_d([u]) = w_0/7 + w_6(d)\,\widehat r_6([u]) = 1 + w_6(d)\,\widehat r_6([u])`$,
since $`w_0 = 7`$ in both sectors. The two quartics are therefore the same increasing affine
function of $`\widehat r_6`$ up to the positive slope $`w_6(d)`$, and an increasing affine
reparameterisation moves neither the critical set nor the order of the values on it. Hence

```math
\mathrm{Crit}\, Q_{\mathbf 3'} \;=\; \mathrm{Crit}\, Q_{\mathbf 4} .
```

So once the filter has selected rank 6, the shape problem stops being icosahedral and becomes a
question about spin 3 with time reversal, which is why Section 7.1 could be carried out without the
group appearing again.

> **Corollary 5.6.** *But their nonlinear shifts differ.* Let $`[u]`$ be a critical ray and let
> $`\psi`$ be the corresponding block state normalised so that $`\int_X \lvert\psi\rvert^2 = 1`$.
> Then the projected self-interaction acts on $`\psi`$ by the scalar $`Q_d([u])`$, and
> $`Q_{\mathbf 3'} - Q_{\mathbf 4} = \tfrac{49}{156}\,\widehat r_6([u])`$.

At a critical ray the tangential part vanishes, so $`\mathcal I(\psi) = \beta\psi`$ for some scalar
$`\beta`$. Pairing with $`\psi`$ and using that the block projection is self-adjoint with $`\psi`$
in its range gives $`\beta \int\lvert\psi\rvert^2 = \int\lvert\psi\rvert^4`$, so with the stated
normalisation $`\beta = \int\lvert\psi\rvert^4 = Q_d([u])`$. The difference is then
$`(28/39 - 21/52)\,\widehat r_6 = \tfrac{49}{156}\,\widehat r_6`$. $`\square`$

The two shifts agree only where $`\widehat r_6 = 0`$, so they
differ at every ray whose top multipole is nonzero, the four tabulated ones included.

None of the three corollaries is a statement about solutions of the equation; like Theorem 5.1, they
concern the leading reduced problem.

---

## 6. The selected point

Theorem 5.1 places the self-interaction on a single projective ray of the four-dimensional family of
Section 4.2, which that section identifies with the four-channel spin-3 interaction of the
condensate literature [DH], [KU]. What remains is to say where in that family the ray lies. The
answer is one point, and at that point the quartic of Theorem 5.1 is exactly an affine image of a
mean-field energy the condensate literature has already studied. Nothing icosahedral enters
here: the quotient did its work in Theorem 5.1, and everything below is spin 3.

### 6.1 The point

For $`u \in V_3`$ write $`f(u) = \langle u, F u\rangle \in \mathbb R^3`$ for its spin density, with
$`F = (F_x, F_y, F_z)`$ the spin-3 generators, and keep the holomorphic squares
$`B_J(u) = [u \otimes u]_J`$ of Section 2.3. The pair amplitudes of [KU] are $`\sqrt 7\,B_J`$, so in
the present notation their spin-3 mean-field energy reads, up to an additive constant,

```math
\widetilde{E}(u) \;=\; c_\gamma\,\lvert f\rvert^2 \;+\; 7c_\alpha\,\lVert B_0\rVert^2 \;+\; 7c_\beta\,\lVert B_2\rVert^2 ,
```

with the three couplings fixed combinations of the four scattering lengths.

> **Proposition 6.1** (the selected point)**.** On the unit sphere of $`V_3`$,
>
> ```math
> \widehat r_6 \;=\; \frac{64 + 7\,\widetilde{E}}{924}
> \qquad\text{at}\qquad (c_\gamma, c_\alpha, c_\beta) = (-1,\, 32,\, 12) .
> ```

*Proof.* Multiplied by $`\lVert u\rVert^4`$, both sides are real quartics of bidegree $`(2,2)`$ in
$`(u, \bar u)`$, invariant under $`\mathrm U(1) \times \mathrm{SU}(2)`$. Polynomials of bidegree
$`(2,2)`$ are $`\mathrm{Sym}^2 V_3^{*} \otimes \mathrm{Sym}^2 \overline V_3^{*}`$, that is, sesquilinear
forms on $`\mathrm{Sym}^2 V_3`$ evaluated on squares, and the real ones are the hermitian forms. So
the invariant real quartics of this bidegree are the invariant hermitian forms on
$`\mathrm{Sym}^2 V_3 = V_0 \oplus V_2 \oplus V_4 \oplus V_6`$, which is multiplicity-free, and by
Schur's lemma they form a real space of dimension four, the count of Section 9.5. The four quartics
$`\lVert u\rVert^4`$, $`\lvert f\rvert^2`$, $`\lVert B_0\rVert^2`$ and $`\lVert B_2\rVert^2`$ lie in it,
and they are independent:
at the weight states $`v_3, v_2, v_1, v_0`$ they take the values

```math
(1, 9, 0, 0), \quad (1, 4, 0, 0), \quad \left(1, 1, 0, \tfrac27\right), \quad \left(1, 0, \tfrac17, \tfrac{4}{21}\right),
```

computed from the Clebsch-Gordan coefficients, and those four rows have determinant $`10/49`$. They are
therefore a basis, and the identity holds everywhere once it holds at those four states. There
$`924\,\lVert\rho_6\rVert^2 = \binom 6{3+m}^2`$, the values $`1, 36, 225, 400`$ (Section 5.5), and at
$`(c_\gamma, c_\alpha, c_\beta) = (-1, 32, 12)`$ the right-hand side gives
$`64 - 63`$, $`64 - 28`$, $`64 + 161`$ and $`64 + 336`$, the same four numbers. $`\square`$

The same identity reads $`\widehat r_6 = (64 - 7\widetilde{E})/924`$ at the opposite point
$`(1, -32, -12)`$, since $`\widetilde{E}`$ is linear in the couplings. The values at the weight
states agree with the energies [KU] tabulate for their inert states.

### 6.2 The two signs, and where the literature places them

The equation of Section 2.5 is the Euler-Lagrange equation of an energy whose quartic term is a
positive multiple of $`g\int\lvert\psi\rvert^4`$, Section 2.5 fixes $`g = 1`$, and clause 5 of
Theorem 5.1 makes the quartic an increasing affine function of $`\widehat r_6`$, since $`w_6 > 0`$
(Section 5.5). So at the paper's normalisation the reduced energy increases with $`\widehat r_6`$.
By Proposition 6.1 it then increases with $`\widetilde{E}`$ at $`(-1, 32, 12)`$: at the paper's
normalisation, the selected interaction is the condensate energy at that point, and the opposite
normalisation, $`g = -1`$, is the point $`(1, -32, -12)`$. Write $`(n_-, n_0, n_+)`$ for the
signature of the second variation of $`\widehat r_6`$ at a critical ray, the numbers of its
negative, zero and positive eigenvalues. The critical rays, their values of $`\widehat r_6`$ and
these signatures do not depend on the sign. The Morse index of each ray as a critical point of the
energy does, being $`n_-`$ at $`g = 1`$ and $`n_+`$ at $`g = -1`$, and so does which ray carries the
least energy. Section 7 gives the indices at both signs.

[KU] also draw the spin-3 phase diagram, determined by comparing the energies of their
symmetry-classified states and by solving the stationary equation directly. In the coordinates of
their second diagram, the form $`\tilde c_1 \lvert f\rvert^2 + \tilde c_2 \lVert B_0\rVert^2 +
\tilde c_3\,\mathrm{Tr}\,\mathcal N^2`$, where their $`A_{00}`$ is the present $`B_0`$ and
$`\mathcal N_{\mu\nu} = \mathrm{Re}\,\langle u, F_\mu F_\nu u\rangle`$ is the nematic tensor, of trace
12 on the unit sphere, the paper's point lies
at $`(\tilde c_3/\lvert\tilde c_1\rvert,\, \tilde c_2/\lvert\tilde c_1\rvert) = (1/9,\, 14)`$ with
$`\tilde c_1 < 0`$, inside the ferromagnetic phase FF and near its boundary with the phase F. The
opposite point lies at $`(-1/9,\, -14)`$ with $`\tilde c_1 > 0`$, well inside the phase [KU] call A,
whose state is the hexagon $`(v_3 + v_{-3})/\sqrt 2`$. Thus the two states that Section 7.3
identifies exactly as the ends of $`\widehat r_6`$ already occur in the literature as the
numerically determined ground states at the two signs: the coherent state at the paper's sign and
the hexagon at the other. That placement is numerical and it is [KU]'s.

### 6.3 What the identity is, and what it is not

It is an identity: the two sides are one function in two coordinate systems. The ten census orbits of
Section 7 are therefore represented among [KU]'s stationary-state families, with the same values.
That is not corroboration of anything, and it should not be
read as such.

The point is where the density interaction of Section 2.5 lands under the quotient's selection.
Nothing here says it is the coupling of a physical condensate, and no claim is made about chromium
or any other spin-3 atom.

---

## 7. The critical geometry at the point

Section 6 placed the quartic at one point of the four-channel family. This section describes its
critical set there: the critical rays of $`\widehat r_6`$ on $`\mathbb P(V_3)`$, with their values
and their signatures, which by Section 6.2 give the Morse indices of the reduced energy at both
signs. Nothing in it uses $`2I`$.

### 7.1 Six rays found by symmetry

By clause 5 of Theorem 5.1 the reduced quartic is an increasing affine function of
$`\widehat r_6`$ (Section 6.2), so its critical rays are those of $`\widehat r_6`$ on
$`\mathbb P(V_3)`$. On the unit sphere $`\widehat r_6 = \lVert\rho_6\rVert^2`$, and this subsection
computes with the latter. The question is about spin 3 with time reversal, and it does not mention
$`2I`$. Four values, with $`\binom{12}6\lVert\rho_6\rVert^2 = 924\,\lVert\rho_6\rVert^2`$ quoted as
an integer:

| ray | constellation | [KU] | $`924\,\lVert\rho_6\rVert^2`$ |
|---|---|---|---|
| $`v_3`$ | coherent, six coincident points | FF | 1 |
| $`v_0`$ | zonal | Q | 400 |
| $`(v_2 + v_{-2})/\sqrt 2`$ | octahedron | D | 288 |
| $`(v_3 + v_{-3})/\sqrt 2`$ | hexagon | A | 463 |

The [KU] column names the state of [KU]'s Table II whose order parameter is that ray, up to rotation
and phase; through Proposition 6.1 their energy for it gives the value in the last column. Those four
rays are critical, which the table alone does not show.

> **Lemma 7.1.** Each of the four rays above is a critical point of $`\lVert\rho_6\rVert^2`$ on the
> unit sphere.

Let $`H`$ be the stabiliser of $`[u]`$ in $`\mathrm{SO}(3)`$, acting on $`u`$ by a character
$`\chi`$. Since $`\lVert\rho_6\rVert^2`$ is $`\mathrm{SO}(3)`$-invariant its gradient is
equivariant, so the tangential gradient at $`[u]`$ lies in the $`H`$-fixed part of the projective
tangent space, which is $`\mathrm{Hom}_H(\chi, V_3)`$ modulo $`\mathbb Cu`$. For each of the four
rays that quotient is zero, because the $`\chi`$-isotypic subspace of $`V_3`$ is one-dimensional and
$`u`$ already spans it. Hence the tangential gradient vanishes. $`\square`$

For the two weight states the cyclic group of rotations about the quantisation axis suffices: the
projective tangent weights are $`\pm 1, \pm 2, \pm 3`$ at $`[v_0]`$ and $`-1, \dots, -6`$ at
$`[v_3]`$, and none of them is zero. For the octahedral ray a subgroup of order 8 already isolates
it, and for the hexagonal ray the dihedral group of order 12 does.

Two further critical rays do not appear in that table. Each lies on a fixed locus of dimension one
rather than at an isolated fixed point, so Lemma 7.1 does not cover them as stated, and a second
lemma does.

> **Lemma 7.2.** Suppose the $`\chi`$-isotypic space of $`H`$ is two-dimensional, so the fixed
> locus is a projective line. If $`\lVert\rho_6\rVert^2`$ is stationary along a real curve in that
> line and a further symmetry makes it even in the transverse coordinate, the ray is critical.

The transverse derivative vanishes by that evenness, and those two real directions exhaust the
tangential fixed space, so the whole tangential gradient vanishes. Both rays below satisfy it.

The **pentagonal pyramid**. On the line $`u = \cos t\, v_2 + \sin t\, v_{-3}`$,

```math
\lVert\rho_6\rVert^2 \;=\; -\tfrac{125}{132}\sin^4 t \;+\; \tfrac{10}{11}\sin^2 t \;+\; \tfrac{3}{77} ,
```

stationary in the interior at $`\sin^2 t = 12/25`$, where $`\lVert\rho_6\rVert^2 = 9/35`$ and
$`\binom{12}6\lVert\rho_6\rVert^2 = 1188/5`$, the first such value that is not an integer. The
rotations of order 5 about the quantisation axis act on $`\mathrm{span}\{v_2, v_{-3}\}`$ by a single
character, so that line is a fixed locus. Rotation about the same axis carries the line to itself
and advances the relative phase of the two components at five times its own angle, so
$`\lVert\rho_6\rVert^2`$ is constant transverse to the real curve and Lemma 7.2 applies along it.
Its Majorana polynomial is
$`z(a + bz^5)`$ with $`a, b \neq 0`$, so the constellation is one point at a pole and five in a
ring, six distinct points: a non-degenerate pentagonal pyramid.

In [KU]'s Table II the pyramid is state H, whose parameter takes the value $`\eta = 2/5`$ at the
point. It shares its value with a second orbit, the C3 ray of Section 7.2, which is their state I, at
$`\eta = -2/5`$. [KU]'s energies for H and I are one function of the couplings, so the two states are
degenerate wherever both exist, as [KU] note, and [BTD07] report the second as a state degenerate
with H. Section 7.2 separates the two orbits.

The **trigonal prism**, and with it the octahedron. Take
$`H = \langle R_z(2\pi/3), R_x(\pi)\rangle \cong D_3`$, with $`R_x`$ the in-plane axis through a
vertex column: it acts by $`-1`$ on both $`v_3 + v_{-3}`$ and $`v_0`$, so the $`\chi`$-isotypic
space is $`\mathrm{span}\{v_3+v_{-3},\, v_0\}`$ and the fixed locus is the projective line
$`\mathbb P\,\mathrm{span}\{v_3+v_{-3},\, v_0\}`$. The chart $`u = v_3 + z\,v_0 + v_{-3}`$ covers that line except at one point, the zonal ray
$`[v_0]`$ at $`z = \infty`$, which is treated below. On the chart, writing $`z = x + iy`$,

```math
\lVert\rho_6\rVert^2 \;=\; \frac{100\lvert z\rvert^4 - 20x^2 + 148y^2 + 463}{231\,(\lvert z\rvert^2+2)^2} ,
```

whose critical set on the chart is five points: $`z = 0`$, the hexagon at $`463/924`$;
$`z = \pm\sqrt{23/10}`$, where $`\lVert\rho_6\rVert^2 = 200/903`$ and
$`\binom{12}6\lVert\rho_6\rVert^2 = 8800/43`$; and $`z = \pm i\sqrt{5/2}`$, where the value is
$`24/77`$. The expression is even in each of $`x`$ and $`y`$ separately, so each is stationary in
both directions and Lemma 7.2 applies along either axis. The rotation $`R_z(\pi/3)`$ acts on the
chart by $`z \mapsto -z`$, so the two signs in each pair are one orbit and the five points are three
orbits.

The point the chart omits is critical as well, and it is not a new ray. It lies on this locus
because $`v_0`$ spans one of the two $`\chi`$-isotypic directions, and it is critical by Lemma 7.1,
which already covers it: it is the zonal ray of the table above, at
$`\lVert\rho_6\rVert^2 = 100/231`$, that is $`400/924`$. Counting both charts, the locus carries six
critical points in four orbits, and the hexagon's $`463/924`$ is the largest value on it.

The real axis carries the eclipsed pairs of triangles, Majorana polynomial $`z^6 - sz^3 + 1`$ with
$`s = \sqrt{20}\,x`$ real, and the imaginary axis the staggered ones, where $`s`$ is purely
imaginary. In $`w = z^3`$ the Majorana polynomial is $`w^2 - sw + 1`$, whose two roots multiply to
$`1`$, so the triangles sit at reciprocal radii; since $`\lvert z\rvert \mapsto 1/\lvert z\rvert`$ sends
$`\theta`$ to $`\pi - \theta`$, they sit at heights $`\pm h`$ for a common $`h`$ whatever $`s`$ is. At
$`x^2 = 23/10`$, $`s = \sqrt{46}`$ and both roots are real and positive, so the two triangles are
**aligned**, which makes the ray a **trigonal prism** and not an antiprism, at heights
$`\pm 0.5585\ldots`$. It is [KU]'s state E, at $`\eta = 3/43`$. At $`y^2 = 5/2`$, $`s = i\sqrt{50}`$
and the two roots are purely imaginary of opposite sign, so the azimuths differ by $`60^\circ`$: the
triangles are **staggered**, at $`h = 1/\sqrt 3`$ exactly, which is the **regular octahedron**. The
tabulated octahedron is exact the same way: its sextic is a constant times $`z(z^4+1)`$, with roots
at both poles and at the fourth roots of $`-1`$ on the equator. Figure 2 draws the four shapes.

<img src="https://github.com/dmobius3/mode-identity-theory/blob/main/files/assets/majorana-constellations.png?raw=true" width="90%" alt="Majorana constellations on the unit sphere: a hexagon on the equator, an octahedron, a pentagonal pyramid and a trigonal prism, each labelled with its value of the rank-6 multipole norm">

**Figure 2.** Majorana constellations of the four six-vertex shapes among the critical rays of Section 7.1, each with its value of $`\lVert\rho_6\rVert^2`$: the hexagon, the octahedron, the pentagonal pyramid and the trigonal prism, whose two triangles are aligned. Filled points face the viewer, and dashed edges are hidden.

The hexagonal value is not this paper's. Romero, Klimov, Goldberg, Leuchs and Sánchez-Soto give the
closed form $`\varrho^2_{2S} = \tfrac12 + \binom{4S}{2S}^{-1}`$ for the top multipole of the NOON state
at integer spin $`S`$, in the Parseval normalisation used here [RK]; at $`S = 3`$ that is
$`463/924`$, and their NOON state is this paper's hexagon up to a rotation. The question of whether
it is the global maximum of $`\lVert\rho_6\rVert^2`$ is also theirs, posed for general $`S`$ and
probed numerically; at spin 3, Section 7.3 answers it, and it is not addressed here beyond spin 3.
The three time-reversal-invariant rays in the
table are the zonal, octahedral and hexagonal ones, [KU]'s Q, D and A, and by Lemma 2.2 their odd
density multipoles vanish; the octahedron's are $`1/7, 0, 0, 0, 6/11, 0, 24/77`$, so rank 4 does not,
and it is anticoherent of order exactly 3.

### 7.2 The census, and three orbits outside its class

Lemmas 7.1 and 7.2 are cases of one principle. For a closed subgroup $`H`$ of $`\mathrm{SO}(3)`$ and
a character $`\chi`$ of $`H`$, the vectors $`u`$ with $`D(h)u = \chi(h)\,u`$ for every $`h \in H`$
form a subspace $`V_3^{(H,\chi)}`$, the fixed space of a group of symmetries of $`\widehat r_6`$,
each $`h`$ acting together with the phase $`\chi(h)^{-1}`$. By Palais' principle of symmetric
criticality, a critical point of $`\widehat r_6`$ restricted to its projectivisation is critical on
$`\mathbb P(V_3)`$. Lemma 7.1 is the case in which that projectivisation is a point, and Lemma 7.2
a case in which it is a line.

**The census.** Take every such locus of projective dimension at most one, and every critical point
on it. There are six loci that are points and seven that are lines; the complete critical set on
each line is found by elimination, not by a numerical solver; and the union, modulo rotation and
phase, is exactly ten orbits [M8.12]. At each orbit the signature $`(n_-, n_0, n_+)`$ of the second
variation of $`\widehat r_6`$ is computed exactly, from its characteristic polynomial, on the space
transverse to the phase and rotation directions, of dimension 10 at the weight states and 9
elsewhere. The census was pre-registered by the author and reproduced blind in two rooms under an adversarial
audit, which graded its arguments sound [M8.12]; it is an audited argument.

Both tables give two notions of symmetry. The *rotation stabiliser* is the stabiliser of the ray in
$`\mathrm{SO}(3)`$. The *full isotropy* is the stabiliser of the vector in the group generated by
$`\mathrm U(1) \times \mathrm{SO}(3)`$ and time reversal $`\Theta`$: rotations and antiunitary maps
$`\Theta \circ R`$, each with the phase that lifts it. Forgetting the phases maps it isomorphically
onto the symmetry group of the constellation in $`\mathrm O(3)`$, since $`\Theta`$ acts on
constellations as the antipodal map (Section 3.4) and a ray is determined by its constellation, and the
tables print it as that point group. It is certified for the prism, the pyramid and the D2 ray and read
off the explicit constellations for the other seven, and in every row it agrees with the isotropy
group [KU] list, once their generators are translated this way.

| orbit | $`924\,\widehat r_6`$ | rotation stabiliser | full isotropy | [KU] | $`(n_-, n_0, n_+)`$ |
|---|---|---|---|---|---|
| coherent $`v_3`$ | 1 | $`C_\infty`$ | $`C_{\infty v}`$ | FF | (0, 0, 10) |
| $`v_2`$ | 36 | $`C_\infty`$ | $`C_{\infty v}`$ | F | (2, 0, 8) |
| trigonal prism | 8800/43 | $`D_3`$ | $`D_{3h}`$ | E | (3, 0, 6) |
| $`v_1`$ | 225 | $`C_\infty`$ | $`C_{\infty v}`$ | P | (4, 2, 4) |
| D2 ray | 225 | $`D_2`$ | $`D_{2d}`$ | B | (5, 0, 4) |
| pentagonal pyramid | 1188/5 | $`C_5`$ | $`C_{5v}`$ | H | (5, 0, 4) |
| C3 ray | 1188/5 | $`C_3`$ | $`C_{3v}`$ | I | (5, 0, 4) |
| octahedron | 288 | $`O`$ | $`O_h`$ | D | (6, 0, 3) |
| zonal $`v_0`$ | 400 | $`D_\infty`$ | $`D_{\infty h}`$ | Q | (8, 0, 2) |
| hexagon | 463 | $`D_6`$ | $`D_{6h}`$ | A | (9, 0, 0) |

The index of an orbit as a critical point of the reduced energy is $`n_-`$ at $`g = 1`$ and $`n_+`$
at $`g = -1`$ (Section 6.2).

Two ties in value are separated by the census. The C3 ray and the pyramid share their value, every
invariant quartic and their signature, and differ in rotation stabiliser, $`C_3`$ against $`C_5`$,
and in transverse spectrum. The D2 ray and $`v_1`$ share the value 225 and differ in signature:
$`v_1`$ is the only degenerate orbit of the census, and its two kernel directions beyond the orbit
are the tangent of the line through it that rotations of order four fix [M8.12]. [KU]'s state J is a
family on that line, up to rotation, and at the point its parameter is $`\eta = -1`$, where its order
parameter is a weight state of weight $`\pm 1`$: J reduces to P. At the two ends the signatures are
$`(0, 0, 10)`$ and $`(9, 0, 0)`$, so the coherent orbit and the hexagon are nondegenerate local
extrema; Section 7.3 shows that they are the global ones.

**Three orbits outside the class.** The class leaves out every orbit whose rotation stabiliser is
$`C_2`$, or $`C_3`$ acting on its three-dimensional fixed space, or trivial, since the loci of those
groups have projective dimension two or more, and the census does not look there. Numerical
censuses of the critical set found three critical orbits outside the class, and the census's
pre-registration disclosed them, with their values and without indices [M8.12]. Call them
$`\mathcal O_1, \mathcal O_2, \mathcal O_3`$, in increasing order of value. This paper
certifies them using 60-digit interval arithmetic, with $`\widehat r_6`$ in the form of Lemma 7.3
and nothing from the searches but the numerical states.

Each is certified at one point. Inside the fixed set of its full isotropy group, a real subspace of
$`V_3`$, a Krawczyk inclusion on a box of radius $`10^{-55}`$ proves that the box holds exactly one zero
of the critical-point system of $`\widehat r_6`$ on the unit sphere, with a slice for the one
continuous symmetry of $`\mathcal O_2`$, and that the system's Jacobian is nonsingular throughout.
The slice multiplier vanishes, since pairing the equation with the symmetry direction leaves only the
multiplier times that direction's squared length, the gradient and the sphere's normal both being
orthogonal to it, and the direction is nonzero or the Jacobian would be singular; so the zero is critical on the fixed set, and by symmetric criticality on all of
$`\mathbb P(V_3)`$. Its full isotropy is certified: from below because the point lies in the group's
fixed set, and from above because the six Majorana points of the certified state are enclosed in
disjoint boxes, so a symmetry must permute them and preserve every pairwise distance, and the
permutations that pass that test, proper and improper told apart by a determinant's sign, number
exactly the group's order. Its signatures are certified: a Gershgorin test on the bordered second variation fixes each by
Sylvester's law, on the whole sphere, where the critical point has the same Lagrange multiplier, and
on each fixed set modulo its continuous symmetries, so the
transverse second variation has no kernel. Every entry of a row of the table below is computed at
that one certified point. The same machinery reproduces the census's exact full signatures at the
pyramid, the prism and the D2 ray from their own fixed sets, and at all six of its orbits with finite
stabilisers from the whole sphere, and planted failures trip; the certificates section at the end of the paper gives the scripts.

| orbit | $`924\,\widehat r_6`$ | rotation stabiliser | full isotropy | $`(n_-, n_0, n_+)`$ | on the isotropy fixed set | on the $`C_2`$ fixed set |
|---|---|---|---|---|---|---|
| $`\mathcal O_1`$ | 215.7757925… | $`C_2`$ | $`C_{2v}`$ | (4, 0, 5) | (1, 0, 2) | (2, 0, 3) |
| $`\mathcal O_2`$ | 238.0165289… | $`C_1`$ | $`C_s`$ | (6, 0, 3) | (4, 0, 1) | n/a |
| $`\mathcal O_3`$ | 238.3568547… | $`C_2`$ | $`C_{2v}`$ | (7, 0, 2) | (2, 0, 1) | (3, 0, 2) |

With the two-fold axis of $`\mathcal O_1`$ or $`\mathcal O_3`$ as the $`z`$-axis, the fixed set of
its rotation $`C_2`$, with its phase, is the odd-weight subspace
$`\mathrm{span}\{v_3, v_1, v_{-1}, v_{-3}\}`$, and the fixed set of its full isotropy is a real form
of that subspace, of real dimension four. The fixed set of the full isotropy of $`\mathcal O_2`$ is
a real form of $`V_3`$. The value of $`\mathcal O_2`$ lies in a certified interval of width
$`3.1 \times 10^{-52}`$ that contains $`28800/121`$; no exact point is in hand, and the value is not
claimed to be that fraction.

**The indices in order of value.** At $`g = 1`$ the census's indices, in increasing order of value,
are 0, 2, 3, 4, 5, 5, 5, 6, 8, 9. The census's pre-registration recorded this sequence, noted that 1
and 7 were absent, and left open whether the deferred orbits would break the ordering [M8.12]. They
do. The indices of the outside orbits are 4, 6 and 7. $`\mathcal O_3`$ lies below the octahedron in
value, 238.36… against 288, and above it in index, 7 against 6, a certified index against an exact
one, so once the orbits outside the class are included, the index no longer increases with the value.
$`\mathcal O_3`$ fills the gap at 7, and no known orbit has index 1.

**What [KU] have at the point.** All ten census orbits are [KU]'s states, and [KU]'s formulas
evaluated at the point give their values (Section 6.3), but their procedure does not return all of
them. For each subgroup $`H`$ of their symmetry group, which contains time reversal, it takes the
minimum of the energy on the fixed set of $`H`$ ("calculate the minimum of $`f`$ in the submanifold
$`\mathcal M_H`$" [KU, § II.B]), and then compares the minima. At $`g = 1`$ the pyramid and the C3
ray are maxima of the energy on their own fixed lines, where the energy is a downward parabola in
the squared amplitude (Section 7.1 gives the pyramid's), and minimising on those lines returns the
coherent state and $`v_2`$. At $`g = -1`$ the prism and the D2 ray are the lowest critical values of
$`\widehat r_6`$ on theirs, so maxima of the energy there, and minimising returns the hexagon; that
pair rests on the census's critical sets for those two lines being complete.

For the three outside orbits the statement is stronger. Each has, inside the fixed set of its full
isotropy, both a direction in which the energy decreases and one in which it increases, at either
sign (the restricted signatures above). Any symmetry-fixed set that contains one of these orbits
contains the fixed set of its full isotropy, and restricting a quadratic form to a subspace can raise
neither count, so none of the three is a local minimum of the energy on any symmetry-fixed set
containing it, at either sign, so no procedure that returns local minima on those sets returns them,
[KU]'s included, even on the odd-weight subspace where [KU] computed their state C numerically
[KU, § IV.C], which contains $`\mathcal O_1`$ and $`\mathcal O_3`$. Of [KU]'s other rows that might
supply a formula at the point, G and R do not exist there, since their parameters would need square
roots of negative numbers, and J reduces to P, so none supplies a formula for one of them; Section 9.2
compares their isotropy types with [KU]'s table.

**What is not claimed.** Outside the class the critical set is not classified: the three orbits
above are the ones the numerical censuses found, and nothing here says there are no others. The
signatures are Morse data of $`\widehat r_6`$, and so of the reduced energy on the block at each
sign; they are not stability statements about the local branch germs of Section 8.

### 7.3 The extremes

The table of Section 7.1 runs from $`1/924`$ at the coherent state to $`463/924`$ at the hexagon, and
at spin 3 both ends are exact:

```math
\frac{1}{924} \;\le\; \widehat r_6 \;\le\; \frac{463}{924}
\qquad\text{on } \mathbb P(V_3),
```

with the lower value attained exactly on the coherent states and the upper exactly on the orbit of
the hexagon $`(v_3 + v_{-3})/\sqrt 2`$ under rotations and phase.

**The minimum.** For $`u \in V_3`$ write

```math
P_u(x, y) \;=\; \sum_{m=-3}^3 u_m \sqrt{\binom 6{3+m}}\; x^{3+m}\, y^{3-m} ,
```

so that $`P_u(1, -z)`$ is the Majorana sextic of Section 2.1, and give binary forms of
degree $`n`$ the Bombieri norm

```math
\Bigl[\, \sum_k c_k\, x^k y^{n-k} \Bigr]^2 \;=\; \sum_k \frac{\lvert c_k\rvert^2}{\binom nk} .
```

The map $`u \mapsto P_u`$ is an $`\mathrm{SU}(2)`$-equivariant isometry from $`V_3`$ onto the binary
sextics: it is the standard realisation of spin 3 on forms of degree 6.

> **Lemma 7.3.** For every $`u \in V_3`$, $`\lVert\rho_6(u)\rVert^2 = [P_u P_{\Theta u}]^2`$.

*Proof.* Multiplication of forms, $`(u, w) \mapsto P_u P_w`$, is $`\mathrm{SU}(2)`$-equivariant
from $`V_3 \otimes V_3`$ to the forms of degree 12, which carry $`V_6`$, and so is
$`u \otimes w \mapsto [u \otimes w]_6`$. Since $`V_6`$ occurs once in $`V_3 \otimes V_3`$, Schur's
lemma makes the first a multiple of the second, under the isometric identification of $`V_6`$ with
the forms of degree 12. At $`u = w = v_3`$ both give the unit top vector, $`x^{12}`$ on one side and
$`\langle 3\,3;\, 3\,3 \mid 6\,6\rangle = 1`$ on the other, so the multiple is 1. Put
$`w = \Theta u`$ and take norms. $`\square`$

> **Proposition 7.4** (the minimum)**.** On $`\mathbb P(V_3)`$, $`\widehat r_6 \ge 1/924`$, with
> equality exactly on the coherent states.

*Proof.* For a form $`f`$ write $`\lVert f\rVert^2 = f(D)\,\bar f`$ for its apolar norm, where
$`f(D)`$ replaces each variable by the corresponding partial derivative and the bar conjugates the
coefficients; for a form of degree $`n`$ it is $`n!\,[f]^2`$ [Re, § 2]. For all forms $`p`$ and $`q`$,
$`\lVert pq\rVert \ge \lVert p\rVert\,\lVert q\rVert`$: this is the inequality of Beauzamy, Bombieri,
Enflo and Montgomery [BBEM] in Reznick's form [Re, (1.3)]. Reznick's main theorem is that equality
holds if and only if $`p`$ and $`q`$ are unitarily disjoint, that is, forms in disjoint sets of
variables after a unitary change of variables [Re, Main Theorem]. For binary forms this leaves only
powers of two orthogonal linear forms, as Reznick notes [Re, p. 1064], since in two variables a
nonzero form in a single variable is a multiple of a power of it. For two sextics the inequality
reads $`[pq]^2 \ge (6!\,6!/12!)\,[p]^2 [q]^2 = [p]^2 [q]^2/924`$, and with Lemma 7.3 and
$`[P_u] = [P_{\Theta u}] = \lVert u\rVert`$ it is $`\widehat r_6 \ge 1/924`$. Equality therefore
makes $`P_u`$ the sixth power of a linear form: $`u`$ is coherent, its constellation a single point
of multiplicity six. Conversely, a coherent state is $`g v_3`$ up to phase for some
$`g \in \mathrm{SU}(2)`$. Since $`\Theta`$ commutes with rotations (Section 2.2) and
$`\Theta v_3 = -v_{-3}`$, the forms $`P_u`$ and $`P_{\Theta u}`$ are then multiples of
$`(g \cdot x)^6`$ and $`(g \cdot y)^6`$, where $`g`$ acts on linear forms by substitution: sixth
powers of orthogonal forms, so equality holds. $`\square`$

The minimum has been stated before. Björk and coauthors [Bj] state that the coherent states maximise
the cumulative sum of the multipole lengths of orders 1 to $`M`$, for every $`M`$. Since the multipole
lengths of a pure state sum to 1 in the normalisation used here and the monopole is fixed, the order
$`M = 2S - 1`$ is the statement that the coherent states minimise the top multipole. Their appendix
reduces the question to weight states by an assertion it does not prove, and it makes no uniqueness
claim. Lemma 7.3 was not located in
the sources read, [Bj] and [RK] among them; with it, the classical inequality and its equality case
give the whole statement.

**The maximum.**

> **Theorem 7.5.** On $`\mathbb P(V_3)`$, $`\widehat r_6 \le 463/924`$, with equality exactly on
> the orbit of the hexagon $`(v_3 + v_{-3})/\sqrt 2`$ under rotations and phase.

The argument is the author's. An independent audit graded every step of it established, found no
gap and no false statement, and supplied steps that the author's text left out. The proof below
follows that argument, restructured in a few places, and a dagger † marks each supplied step it
still uses, one-line facts included; a [map](/files/framework/files/bedrock/files/scripts/surviving-ray-v2/dagger-map.md) in the paper's scripts folder
names the restructurings and matches each dagger to the audit's records. Work on the unit sphere of $`V_3`$, with $`f`$ and
$`\mathcal N`$ as in Section 6, $`F_\pm = F_x \pm i F_y`$, $`\lambda_\max`$ for the largest
eigenvalue of a hermitian operator, and $`K = 15/\sqrt 6`$, so that $`K^2 = 75/2`$.

*Step 1: an invariant form.* The five functions $`\lVert\rho_6\rVert^2`$, $`\lVert u\rVert^4`$,
$`\lvert f\rvert^2`$, $`\lVert B_0\rVert^2`$ and $`\mathrm{Tr}\,\mathcal N^2`$ are real quartics of
bidegree $`(2,2)`$ in $`(u, \bar u)`$, invariant under $`\mathrm U(1) \times \mathrm{SU}(2)`$.† By the
argument of Proposition 6.1, which identifies such quartics with the invariant hermitian forms on
$`\mathrm{Sym}^2 V_3`$,† they lie in a real space of dimension four. The last four take at
$`v_3, v_2, v_1, v_0`$ the values

```math
\left(1, 9, 0, \tfrac{171}{2}\right), \quad (1, 4, 0, 48), \quad \left(1, 1, 0, \tfrac{123}{2}\right), \quad \left(1, 0, \tfrac17, 72\right),
```

with determinant $`180/7`$. They are therefore a basis, and matching the values $`1, 36, 225, 400`$
over 924 gives, on the unit sphere,

```math
\widehat r_6 \;=\; -\frac{5}{231} \;-\; \frac{\lvert f\rvert^2}{22} \;+\; \frac{7}{11}\,\lVert B_0\rVert^2 \;+\; \frac{\mathrm{Tr}\,\mathcal N^2}{198} .
```

*Step 2: two bounds.* $`\lvert f\rvert^2 \ge 0`$, with equality exactly when $`f = 0`$. Since
$`B_0 = -\langle \Theta u, u\rangle/\sqrt 7`$ and $`\lVert\Theta u\rVert = \lVert u\rVert`$, the
Cauchy-Schwarz inequality gives $`\lVert B_0\rVert^2 \le 1/7`$, with equality exactly when
$`\Theta u`$ is a multiple of $`u`$.

*Step 3: the nematic bound.* $`\mathrm{Tr}\,\mathcal N^2 \le 171/2`$, with equality only when
$`u`$ lies in $`\mathrm{span}\{R v_3, R v_{-3}\}`$ for a rotation $`R`$.

(3a) Since $`\mathrm{Tr}\,\mathcal N = 12`$,† write $`\mathcal N = 4I + \mathring{\mathcal N}`$,
with $`\mathring{\mathcal N}`$ the trace-free part, so that
$`\mathrm{Tr}\,\mathcal N^2 = 48 + \lVert\mathring{\mathcal N}\rVert^2`$. For a real symmetric
traceless $`E`$ of unit norm, $`\mathrm{Tr}(\mathring{\mathcal N} E) = \langle u, A_E u\rangle`$ with
$`A_E = \sum_{\mu\nu} E_{\mu\nu}(F_\mu F_\nu + F_\nu F_\mu)/2`$,† and
$`\lVert\mathring{\mathcal N}\rVert = \max_E \mathrm{Tr}(\mathring{\mathcal N} E)`$, attained at
$`E = \mathring{\mathcal N}/\lVert\mathring{\mathcal N}\rVert`$ by the Cauchy-Schwarz inequality.† It
therefore suffices to show $`\lambda_\max(A_E) \le K`$ for every
such $`E`$. Rotating $`E`$ conjugates $`A_E`$ by the action of the rotation on $`V_3`$,† so
$`\lambda_\max(A_E)`$ depends only on the eigenvalues $`e_1, e_2, e_3`$ of $`E`$, and for diagonal
$`E`$ the operator is $`e_1 F_x^2 + e_2 F_y^2 + e_3 F_z^2`$. Since $`E`$ is traceless, put
$`e_3 = 2a/3`$ and $`e_1 - e_2 = 4b`$; unit norm becomes $`N^2 := \tfrac23 a^2 + 8b^2 = 1`$, and the
operator becomes $`a(F_z^2 - 4) + b(F_+^2 + F_-^2)`$. In the orthonormal basis, taken in pairs,
$`(v_3 + v_{-3})/\sqrt2`$, $`(v_1 + v_{-1})/\sqrt2`$; $`(v_3 - v_{-3})/\sqrt2`$,
$`-(v_1 - v_{-1})/\sqrt2`$; $`(v_2 + v_{-2})/\sqrt2`$, $`v_0`$; and $`(v_2 - v_{-2})/\sqrt2`$, it is
block diagonal,†

```math
M_1 = \begin{pmatrix} 5a & \sqrt{60}\,b \\ \sqrt{60}\,b & -3a + 12b \end{pmatrix}, \qquad
M_2 = M_1\big|_{b \to -b}, \qquad
M_3 = \begin{pmatrix} 0 & \sqrt{240}\,b \\ \sqrt{240}\,b & -4a \end{pmatrix}, \qquad
0 ,
```

and the last eigenvalue, 0, is below $`K`$.

(3b) On the ellipse $`N = 1`$ one has $`a + 6b \le \sqrt6`$† and $`\lvert a\rvert \le \sqrt{3/2}`$,†
since $`6N^2 - (a + 6b)^2 = 3(a - 2b)^2`$ and $`\tfrac32 N^2 - a^2 = 12b^2`$.

$`M_1`$. Its larger eigenvalue is $`a + 6b + \sqrt{16a^2 - 48ab + 96b^2}`$, and
$`K - a - 6b \ge K - \sqrt6 = 9/\sqrt6 > 0`$, so the bound is equivalent to
$`(K - a - 6b)^2 \ge 16a^2 - 48ab + 96b^2`$, that is, to
$`K^2 - 2K(a + 6b) - 15a^2 + 60ab - 60b^2 \ge 0`$. Replacing $`K^2`$ by
$`K^2N^2 = 25a^2 + 300b^2`$ and $`K`$ by $`KN`$ makes this homogeneous, and after division by 10 it
reads†

```math
\frac{3}{\sqrt6}\,(a + 6b)\,N \;\le\; a^2 + 6ab + 24b^2 \;=\; (a + 3b)^2 + 15b^2 .
```

When $`a + 6b \le 0`$ this holds because the right side is nonnegative. When $`a + 6b > 0`$ both
sides are nonnegative, so it is equivalent to its square,† and
$`(a^2 + 6ab + 24b^2)^2 - \tfrac32 (a + 6b)^2 N^2 = 36\,b^2 (a + 2b)^2 \ge 0`$.

$`M_2`$ is $`M_1`$ with $`b`$ replaced by $`-b`$, and the ellipse is even in $`b`$.

$`M_3`$. Its larger eigenvalue is $`-2a + \sqrt{4a^2 + 240b^2}`$, which on the ellipse is
$`-2a + \sqrt{30 - 16a^2}`$,† with $`30 - 16a^2 \ge 6`$.† Since
$`K + 2a \ge K - 2\sqrt{3/2} = 9/\sqrt6 > 0`$, the bound is equivalent to
$`(K + 2a)^2 \ge 30 - 16a^2`$, and $`(K + 2a)^2 - (30 - 16a^2) = 20\,(a + \sqrt6/4)^2 \ge 0`$.

Hence $`\lambda_\max(A_E) \le K`$ for every $`E`$, so $`\lVert\mathring{\mathcal N}\rVert \le K`$ and
$`\mathrm{Tr}\,\mathcal N^2 \le 48 + 75/2 = 171/2`$.

(3c) Equality in the eigenvalue bound. In $`M_1`$, on the branch $`a + 6b \le 0`$, equality would
need $`a + 6b = 0`$ and $`(a + 3b)^2 + 15b^2 = 0`$, hence $`a = b = 0`$, which is off the
ellipse.† On the branch $`a + 6b > 0`$ it needs $`b(a + 2b) = 0`$, which on the ellipse leaves
$`(a, b) = (\sqrt6/2, 0)`$ and $`(-\sqrt6/4, \sqrt6/8)`$, the signs being forced by
$`a + 6b > 0`$.† The equality points of $`M_2`$ are the reflections $`(\sqrt6/2, 0)`$ and
$`(-\sqrt6/4, -\sqrt6/8)`$.† In $`M_3`$ equality needs $`a = -\sqrt6/4`$, which meets the ellipse at
$`b = \pm\sqrt6/8`$, so $`M_3`$ attains the bound there, tangentially.† The three points give
$`e = (-1, -1, 2)/\sqrt6`$, $`(2, -1, -1)/\sqrt6`$ and $`(-1, 2, -1)/\sqrt6`$: equality holds
exactly when $`E = (3\hat n\hat n^{\mathsf T} - I)/\sqrt6`$ for a unit vector $`\hat n`$, and then
$`A_E = (3(\hat n \cdot F)^2 - 12)/\sqrt6`$.

(3d) Equality in the nematic bound.† If $`\mathrm{Tr}\,\mathcal N^2 = 171/2`$ then
$`\lVert\mathring{\mathcal N}\rVert = K`$. Put $`E_* = \mathring{\mathcal N}/K`$. Then
$`K = \mathrm{Tr}(\mathring{\mathcal N} E_*) = \langle u, A_{E_*}u\rangle \le \lambda_\max(A_{E_*}) \le K`$, so both are
equalities: $`u`$ lies in the top eigenspace of $`A_{E_*}`$, and $`E_*`$ is an equality point,
$`E_* = (3\hat n\hat n^{\mathsf T} - I)/\sqrt6`$.

(3e) For $`\hat n = \hat z`$ the operator $`(3F_z^2 - 12)/\sqrt6`$ is diagonal in the weight basis,
with entries $`(3m^2 - 12)/\sqrt6`$, and its largest value, $`15/\sqrt6 = K`$, occurs only at
$`m = \pm 3`$.† So the top eigenspace is $`\mathrm{span}\{R v_3, R v_{-3}\}`$, for a rotation $`R`$
taking $`\hat z`$ to $`\hat n`$.

*Step 4: the combination.* In Step 1 the coefficients of $`\lvert f\rvert^2`$,
$`\lVert B_0\rVert^2`$ and $`\mathrm{Tr}\,\mathcal N^2`$ are $`-1/22`$, $`7/11`$ and $`1/198`$: all
nonzero, with the signs that make Steps 2 and 3 upper bounds for their terms. So

```math
\widehat r_6 \;\le\; -\frac{5}{231} + \frac{7}{11}\cdot\frac17 + \frac{1}{198}\cdot\frac{171}{2} \;=\; \frac{463}{924} ,
```

with equality only if all three bounds are equalities. In particular
$`\mathrm{Tr}\,\mathcal N^2 = 171/2`$, so by Step 3, after a rotation, $`u = \alpha v_3 + \beta v_{-3}`$
with $`\lvert\alpha\rvert^2 + \lvert\beta\rvert^2 = 1`$. On that span
$`f = (0, 0, 3(\lvert\alpha\rvert^2 - \lvert\beta\rvert^2))`$,† so $`f = 0`$ forces
$`\lvert\alpha\rvert = \lvert\beta\rvert = 1/\sqrt2`$; then $`\langle\Theta u, u\rangle = -2\alpha\beta`$
has modulus 1, so $`\lVert B_0\rVert^2 = 1/7`$ holds as well.† Explicitly, on the span
$`\mathcal N = \mathrm{diag}(\tfrac32, \tfrac32, 9)`$ and
$`\lVert B_0\rVert^2 = 4\lvert\alpha\beta\rvert^2/7`$,† and Step 1 gives†

```math
\widehat r_6 \;=\; \frac{463}{924} \;-\; \frac12\left(\lvert\alpha\rvert^2 - \lvert\beta\rvert^2\right)^2 .
```

The remaining relative phase is a rotation about the axis, since rotating by $`\tau`$ about it
multiplies $`v_{\pm 3}`$ by $`e^{\mp 3i\tau}`$.† So every maximiser is the hexagon up to rotation and
phase, and every such state attains $`463/924`$. $`\square`$

The whole span of $`v_3`$ and $`v_{-3}`$ saturates the nematic bound, so Step 3 alone does not pick
the orbit; Step 4 does.

Reznick's upper bound, $`[pq] \le [p]\,[q]`$ with equality at powers of one linear form [Re, § 5 and
Corollary 5.9], gives only $`\widehat r_6 \le 1`$: time reversal excludes its equality case, since the
time reverse of a sixth power is the sixth power of the orthogonal form.

---

## 8. Local branch germs on the quotient

Section 8.1 interprets Theorem 5.1 and derives nothing: its Lyapunov-Schmidt reading explains why the
quartic is worth extremising, and Sections 8.2 and 8.3 report how far the problem it poses has since
been carried.

### 8.1 The setting

The equation is the one fixed in Section 2.5, $`(-\Delta - \lambda)\psi + \lvert\psi\rvert^2\psi = 0`$,
with $`\lambda`$ a spectral parameter near $`\lambda_6 = 48/R^2`$, the level-6 eigenvalue of the
Laplacian on $`S^3`$. The kernel that Lyapunov-Schmidt needs is that of the linearisation
$`-\Delta - \lambda`$ at $`\lambda = \lambda_6`$, the level-6 eigenspace
$`V_3 \otimes \mathrm{Hom}_{2I}(\sigma, V_3)`$, of dimension seven since the branching is
multiplicity-free, and near that value the equation splits into a projection onto the kernel and a
complementary range equation. Level 6 is fixed by the choice of object, since spin-3 states put the
left index in $`V_3`$, and it is the bottom of the spectrum on both bundles: odd levels are excluded by
parity, since $`-I`$ acts on them as $`-1`$ while $`\mathbf 3'`$ and $`\mathbf 4`$ factor through
$`A_5 = 2I/\{\pm I\}`$, and, extending the branching table of Section 4.3 downward, the even levels
below 6 carry $`\mathbf 1`$, $`\mathbf 3`$ and $`\mathbf 5`$. No claim is made that the states
bifurcating at level 6 minimise anything, so the word ground state is avoided.

The leading cubic term of the reduction is the projection of the nonlinearity onto the eigenspace,
which is the self-interaction of Sections 4 and 5, and the quartic $`Q`$ plays the part of the reduced
energy (Section 5.5). The critical rays of $`Q`$ are therefore the **critical directions of the leading
reduced problem**, and not by themselves solutions of the equation: a solution needs the range equation
as well.

Both records work with $`(-\Delta - \lambda)\psi + g\lvert\psi\rvert^2\psi = 0`$ at general real
$`g \neq 0`$ and state every value per power of $`g`$, which covers both signs of Section 6.2. They
work in the convention $`R = 1`$, so the bifurcation eigenvalue is 48, with each block section $`\Phi`$
normalised by $`\int_X \lvert\Phi\rvert^2 = 1`$, as in Corollary 5.6; their values move with these
conventions [M8.10], [M8.11].

### 8.2 The first correction at four rays

[M8.10] carries the reduction one order further at the four symmetry-pinned rays of Section 7.1, the
coherent, zonal, octahedral and hexagonal rays, in both sectors. With $`\Phi`$ a critical ray's block
section and $`K`$ the level-6 block, expand

```math
\psi \;=\; a\Phi + a^3\xi + O(a^5), \qquad \lambda \;=\; 48 + \lambda_2 a^2 + \lambda_4 a^4 + O(a^6),
```

with $`\langle\Phi, \psi\rangle`$ real and $`\Pi_K \xi = 0`$. At order $`a^3`$ the block part gives
$`\lambda_2 = gQ`$, with $`Q = \int_X \lvert\Phi\rvert^4 = 1 + w_6(\sigma)\,\widehat r_6`$ the scalar
of Corollary 5.6, and the range part gives $`A\xi = -g\,\Pi_\perp N(\Phi)`$, with
$`N(\psi) = \lvert\psi\rvert^2\psi`$ and $`A = -\Delta - 48`$ inverted on $`K^\perp`$. At order $`a^5`$
the block part gives

```math
\lambda_4 \;=\; g\,\langle \Phi, DN_\Phi[\xi]\rangle \;=\; -3g^2 \sum_{n \neq 6} \frac{\lVert \Pi_n N(\Phi)\rVert^2}{n(n+2) - 48} ,
\qquad DN_\Phi[h] \;=\; 2\,\mathrm{Re}(\Phi^\dagger h)\,\Phi + \lvert\Phi\rvert^2 h ,
```

provided its part orthogonal to $`\Phi`$ vanishes, which is the condition for the ray to persist at
this order; the sum is finite, since the cubic of a level-6 section has no content above level 18.
[M8.10] finds the condition met at all four rays and gives the eight values of $`\lambda_4/g^2`$, two
sectors at each ray, as exact results reproduced blind.

Every $`\lambda_4/g^2`$ is negative, and the sign needs two facts, both in the paper. No level of
either sector lies below 6 (Section 8.1), and levels are even, so every $`n \neq 6`$ in the sum has
$`n \ge 8`$ and a positive denominator. And $`Q > 1`$, since $`w_6 > 0`$ and
$`\widehat r_6 \ge 1/924`$ (Proposition 7.4), so $`\lvert\Phi\rvert^2`$ is not constant, and with
Parseval the strict Cauchy-Schwarz inequality gives
$`\sum_{n \neq 6} \lVert \Pi_n N(\Phi)\rVert^2 = \int_X \lvert\Phi\rvert^6 - Q^2 > 0`$. So
$`\lambda_4 < 0`$ for $`g \neq 0`$ wherever the formula holds. This is the solver's route in [M8.10], with
its level hypothesis written out. At leading order the two sectors differ by one factor at every ray,
$`(\lambda_2(\mathbf 3') - g)/(\lambda_2(\mathbf 4) - g) = w_6(\mathbf 3')/w_6(\mathbf 4) = 16/9`$,
which is Corollary 5.6's statement that they agree about shape and disagree about scale; at the next
order they stop being proportional: the four ratios $`\lambda_4(\mathbf 3')/\lambda_4(\mathbf 4)`$
are pairwise distinct [M8.10].

At the pentagonal pyramid the same expansion fails: the order-$`a^5`$ block equation has a part
orthogonal to $`\Phi`$ in both sectors, so no $`\lambda_4`$ is defined for a fixed direction, and
[M8.10] ran the pyramid as a negative control that fired blind. The pyramid lies on a fixed line
(Lemma 7.2), so its direction can move along it, and Section 8.3 lets it.

### 8.3 Local branch germs

[M8.11] asks whether the formal expansions are the Taylor expansions of actual solutions, at the four
pinned rays and at the two rays of Lemma 7.2, the pentagonal pyramid and the trigonal prism. Its
answer is a local existence theorem, which stands here at the standing its record gives it: an
audited argument, checked step by step by one AI auditor and read by the designer, with AI agents on
both the drafting and the checking side, and not a verified theorem.

> **Local branch germs** [M8.11]. Let $`[u]`$ be a critical ray, $`H`$ its stabiliser in
> $`\mathrm{SO}(3)`$, acting on it by a character, $`X_H`$ the closed subspace of sections that $`H`$
> fixes up to that character, and $`m`$ the complex dimension of the block part of $`X_H`$. Suppose that
> $`m = 1`$, or that the Hessian of $`Q`$ at the ray, on a slice of the projectivised block part of
> $`X_H`$ transverse to the continuous symmetries that preserve it, is invertible. Then for each sector
> and each $`g \neq 0`$ there are a neighbourhood of $`(0, 48)`$ and an $`\varepsilon > 0`$ such that,
> for every amplitude $`a`$ with $`0 < \lvert a\rvert < \varepsilon`$, exactly one solution
> $`(\psi, \lambda)`$ in that neighbourhood has $`\psi \in X_H`$, in the gauge of the expansion
> ($`\langle\Phi, \psi\rangle = a`$ real, the range part orthogonal to $`K`$), with its block part near
> the ray on that slice. Both $`\lambda`$ and $`\psi/a`$ are analytic in $`a^2`$, their Taylor
> coefficients are those of the formal expansion, and rotations carry the germ to equivalent germs at
> the conjugate rays. No lower bound on $`\varepsilon`$ is given. The hypothesis holds at the six rays
> of Section 7.1: $`m = 1`$ at the four pinned rays, and at the pyramid and the prism the slice Hessian
> is invertible, as shown below.

The argument has the standard architecture [GS]. The audit graded every step of the theorem established,
with one step it supplied, an analytic change of parameter in the identification of the Taylor
coefficients [M8.11]. After dividing by $`a^3`$ to remove the trivial solution, the range
equation is solved in $`X_H`$ by the implicit function theorem, $`A`$ being invertible on $`K^\perp`$ with
a gap of 32 in sector $`\mathbf 4`$ and 72 in sector $`\mathbf 3'`$ above the level-6 eigenvalue,
and what remains is the gradient of a reduced functional on a slice through the ray. At the ray its
Jacobian is block-triangular, with blocks $`-1`$ and
$`\tfrac14\,\mathrm{Hess}_T Q = \tfrac14\,w_6\,\mathrm{Hess}_T\,\widehat r_6`$, by a bridge the
record proves. At the four pinned rays $`m = 1`$, the slice is a point, and no nondegeneracy condition
enters: the symmetry pins the germ. At the pyramid and the prism $`m = 2`$, and the slice Hessian is
$`\mathrm{Hess}_T\,\widehat r_6 = -104/55`$ along the pyramid's real curve of Section 7.1, the other
direction in its line being a rotation, and $`\mathrm{diag}(920/473,\ 8/11)`$ on the prism's chart, with
no cross term. Neither vanishes, in either sector.

The weight states $`v_1`$ and $`v_2`$ satisfy the hypothesis too, with $`m = 1`$, each weight space
being one-dimensional, and the frozen task of [M8.11] records them as covered by the theorem; that run
neither expanded nor scored them, so no values are given for them here. The degeneracy of $`v_1`$ found
in Section 7.2 does not obstruct its germ: rotations about the axis act on its kernel,
$`\mathrm{span}\{v_{-3}, i v_{-3}\}`$ [M8.12], by a different character from the one on $`v_1`$, so the
kernel lies outside the fixed space, and it means only that the germ need not be isolated among all
solutions, which the theorem does not claim.

At the pyramid and the prism the direction also moves, at order $`a^2`$, by a tilt in the slice fixed by
the tangential part of the order-$`a^5`$ block equation. At each ray it points opposite ways in the two
sectors, as the forcing does, at the prism it lies along one real direction of the chart by a symmetry
of the prism, and [M8.11] gives the exact values. The tilt does not change $`\lambda_4`$ at this order,
by [M8.11]'s lemma, since criticality removes its contribution, so $`\lambda_4`$ at the pyramid and the
prism is given by the formula of Section 8.2, with the sign argued there; [M8.11] gives the values. A
solver and an auditor derived these values, the second variations, the forcing and the tilt blind,
and the auditor computed every one of them exactly [M8.11].

At the paper's sign $`g = 1`$ (Section 6.2), $`\lambda - 48 = Q a^2 + O(a^4)`$ with $`Q > 1`$, so every
germ leaves the linear point upward in $`\lambda`$, and at $`g = -1`$ downward. The next coefficient
$`\lambda_4/g^2`$ is negative at all six rays in both sectors, whatever the sign.

### 8.4 The ceilings that remain

**The reduction is carried through at six rays, and only locally.** What this paper derives itself is
exact at leading cubic order: the finite-dimensional problem on the degenerate eigenspace, from Sections
4 and 5. Beyond that order it derives the sign of $`\lambda_4`$ (Section 8.2) from facts of its own; the
coefficients and the germs are the records'. At the six rays of Section 7.1 the records carry the range
equation to the order the germs need, and there the formal expansions are the Taylor expansions of local
branch germs, for sufficiently small amplitude, as an audited argument. Everything else stays out of reach. There is no radius, since no
lower bound on $`\varepsilon`$ is given. There is no stability of any kind, and the Morse indices of
Section 7 are data of the reduced energy, not stability statements about the germs. Nothing is claimed
at finite amplitude. No germ statement is made here for the C3 and D2 rays or
for the three orbits outside the class.

Everything in Sections 3 through 5 stands without this section, and neither it nor the germs is a
statement about the dynamics the interaction came from: the nonlinearity of Section 2.5 is a hypothesis
of the paper. The reduction from a degenerate eigenspace is classical [GS], used here rather than
developed, and no property of it is proved in this paper.

---

## 9. Discussion

### 9.1 What is not claimed

Everything above concerns a single block state in a single sector. No statement is made about a
field occupying distinct flat-bundle sectors at once, or about a nonlinearity coupling one sector's
density to another's amplitude. Corollaries 5.5 and 5.6 compare the two sectors; they do not
describe a configuration containing both. The mixed problem is not posed here, let alone solved.

### 9.2 Prior art, and where the boundary falls

The setting and many of the objects of Sections 6 and 7 are known, to the condensate literature, to the
literature on Majorana constellations and anticoherence, and to the classical theory of binary forms.

*The coupling point and its states.* Diener and Ho [DH] write the spin-3 mean-field energy in the forms
used here and in [KU] and draw its zero-field phase diagrams, and Santos and Pfau [SP] draw the
ground-state diagram at chromium's measured scattering lengths. Barnett, Turner and Demler show the
hexagon, the pentagonal pyramid, the prism and the octahedron as spin-3 phases [BTD], in a figure whose
coefficients were not extracted, so no statement here rests on it, and later tabulate the phases' wave
functions from a numerical minimisation over all seven amplitudes [BTD07]. Kawaguchi
and Ueda [KU] classify the stationary states by their symmetry groups, give formulas for all but one of
them, and draw two diagrams. Among the published spin-3 diagrams checked here, only [KU]'s second
reaches the point of Section 6, and it places the point numerically, in phase FF at the paper's sign and
in phase A at the other (Section 6.2). [DH]'s coordinates put the point at
$`(\alpha, \beta, \gamma) = (32, 12, -1)`$ at the paper's sign, outside both of their drawn windows, and it
is not on [SP]'s slice, along which the ratio of their spin and nematic couplings is fixed near
$`-59/2`$, against $`-17/2`$ at the point. [KU]'s formulas give all ten census orbits at the point (Section
6.3), but their procedure takes the minimum on each fixed set, so at each sign it returns neither that
sign's two line maxima nor the three orbits outside the class (Section 7.2), and it claims no
completeness. The three are not among [KU]'s states: $`\mathcal O_1`$ and $`\mathcal O_3`$ share the
isotropy type of [KU]'s state C, which [KU] computed only numerically, as the minimum on its fixed set,
and at the point that minimum is the coherent state or the hexagon; the type of $`\mathcal O_2`$ has no
row in their table.

*The critical geometry at the point.* None of these sources computes it. [KU] compute no Hessians. He
and Yi [HY] build the Hessian of the mean-field energy to test whether chromium ground states in a
magnetic field are stable, which is a different question, and Barnett, Podolsky and Refael [BPR]
classify the collective modes of the hexagon by symmetry alone, without energies. The Morse indices of
Section 7.2, the census's and the certified ones, were not located in [KU], [HY] or [BPR]. [BTD]'s four
shapes all occur among the critical rays of Section 7.1 (Figure 2), but the pyramid is *not* the weight
state $`v_2`$, whose Majorana polynomial $`-\sqrt6\,z`$ has one root at the origin and five at infinity,
a degenerate configuration rather than a polyhedron; it is an interior point of the line through
$`v_2`$ and $`v_{-3}`$.

*The two ends.* Romero, Klimov, Goldberg, Leuchs and Sánchez-Soto give the hexagon's value $`463/924`$,
as the top multipole of the NOON state at spin 3, and ask, for every spin, whether it is the largest a
state can reach, probing the question numerically [RK]. Both the value and the question belong to them
(Section 7.1); the exact maximiser set at spin 3, Theorem 7.5, was not located in the sources read. The
minimum was stated by Björk and coauthors, as one order of a claim about cumulative multipoles, with an
appendix step unproved and no uniqueness claim [Bj]; with Lemma 7.3 it is the inequality of Beauzamy,
Bombieri, Enflo and Montgomery [BBEM] with Reznick's equality case [Re] (Section 7.3). [KU] and their
review [KU-rev] state the nematic bound $`\mathrm{Tr}\,\mathcal N^2 \le 171/2`$ and justify it by the
trace, 12, and the range $`[0, 9]`$ of the eigenvalues, which also admit $`(9, 3, 0)`$, where
$`\mathrm{Tr}\,\mathcal N^2 = 90`$; Step 3 of Section 7.3 proves the bound.

*The octahedral state is anticoherent of order exactly 3.* Crann, Pereira and Kribs [CPK] prove that a
Majorana constellation which is both the orbit of a finite subgroup of $`\mathrm O(3)`$ and a spherical
$`t`$-design is anticoherent of order at least $`t`$, and the octahedron is both at $`t = 3`$; the
**sharpness is computed in Section 7.1**, where rank 4 is nonzero.

Recognising a configuration is not the same as selecting it, and knowing the phases is not classifying
the critical geometry: the condensate literature has the states and the ground states at the point, and
what this paper adds there is the identity that places the ray at the point, the census within a class
and its Morse indices, three certified orbits outside it, and the two ends proved.

### 9.3 The search, stated as a search

Three searches were run. The first asked whether the results of Section 3 are known; the polarised
identity of Section 3.1 and the zero-set statement of Proposition 3.3 were not located. The second,
ten queries across six lines of approach, asked the question the contribution rests on, whether the
selection statement of Section 5 has been made before: nothing was found that filters a cubic
interaction by a finite subgroup on a space form, or that puts $`\lvert\psi\rvert^2\psi`$ on a flat
bundle over $`S^3/2I`$, and the adjacencies it found are cited where they belong. The third read the
sources of Sections 6 and 7 in their own text: [KU], [KU-rev], [DH], [SP], [BTD], [BTD07], [HY], [BPR],
[RK] and [Bj] from their preprint sources, and [Re] in full; [BBEM] itself was not read, and its
inequality enters through [Re]'s statement of it. Each thing Section 9.2 says this paper adds at the
point was not located in them: the identity of Proposition 6.1, whose application to the ray of Theorem
5.1 is specific to the selection made here; the completeness of the census within its class, which [KU]
do not claim; the Morse indices of Section 7.2; the three orbits outside the class, with the caveat of
Section 9.2; the identity of Lemma 7.3, which completes the proof of the minimum; and the exact
maximiser set of Theorem 7.5.

**Not surfaced is not the same as new.** The searches were real but not exhaustive: the equivariant
bifurcation literature is largely in monographs that search engines index poorly, the older
invariant-theory literature was not worked, and no subscription index was used.

### 9.4 The open historical question

The object $`\Phi(F,G) = F\,(F,G)_1`$ is a joint covariant of two independent binary sextics, of
bidegree $`(2,1)`$ and order 16, and it is entirely possible that it is named in Grace and Young [GY],
Elliott, or Gordan. The covariant of Section 3 is its specialisation $`G = \Theta F`$ along the
time-reversal diagonal, and whether that has appeared before is a separate question from whether
$`\Phi`$ has. Both are left open here.

### 9.5 Where the family sits

The homogeneous quartic $`\widetilde{Q}`$, not its projective normalisation $`Q`$, is one member of
a four-dimensional space of $`\mathrm{SU}(2)`$-invariant quartics on spin 3. That space has the same
dimension as $`\mathscr E_3`$, and for the same reason: both are counted by the four summands
$`V_0 \oplus V_2 \oplus V_4 \oplus V_6`$ of $`\mathrm{Sym}^2 V_3`$, so selecting a quartic and
selecting a cubic map are the same problem in two costumes. Equal dimension alone would not say
that, so here is the map: $`\widetilde{Q} \mapsto \nabla_{\bar u}\widetilde{Q}`$ is equivariant and
linear from invariant homogeneous quartics to $`\mathscr E_3`$, and injective, since Euler's
identity recovers a homogeneous quartic from its gradient. Both spaces have dimension four, so it is
an isomorphism; Section 5.5 exhibits it channel by channel, as the per-rank identity
$`\nabla_{\bar u}\lVert\rho_K\rVert^2 = c_K M_K`$ with every $`c_K`$ nonzero. The contribution is not the family, and not the quartic considered in isolation, but
which member of it the icosahedral quotient permits, for the density-type interaction of Section 2.5.

---

## References

- **[BBEM]** B. Beauzamy, E. Bombieri, P. Enflo and H. L. Montgomery, Products of polynomials in many variables. *J. Number Theory* **36** (1990), no. 2, 219–245.
- **[Bj]** G. Björk, A. B. Klimov, P. de la Hoz, M. Grassl, G. Leuchs and L. L. Sánchez-Soto, Extremal quantum states and their Majorana constellations. *Phys. Rev. A* **92** (2015), 031801(R); arXiv:1503.03446.
- **[BPR]** R. Barnett, D. Podolsky and G. Refael, Geometrical approach to hydrodynamics and low-energy excitations of spinor condensates. *Phys. Rev. B* **80** (2009), 024420; arXiv:0812.3403 and arXiv:0903.1863.
- **[BTD]** R. Barnett, A. Turner and E. Demler, Classifying novel phases of spinor atoms. *Phys. Rev. Lett.* **97** (2006), 180412; arXiv:cond-mat/0607253.
- **[BTD07]** R. Barnett, A. Turner and E. Demler, Classifying vortices in $`S = 3`$ Bose-Einstein condensates. *Phys. Rev. A* **76** (2007), 013605; arXiv:cond-mat/0611230.
- **[CPK]** J. Crann, R. Pereira and D. W. Kribs, Spherical designs and anticoherent spin states. *J. Phys. A: Math. Theor.* **43** (2010), 255307.
- **[DH]** R. B. Diener and T.-L. Ho, $`^{52}`$Cr spinor condensate: a biaxial or uniaxial spin nematic. *Phys. Rev. Lett.* **96** (2006), 190405; arXiv:cond-mat/0511751.
- **[Fa]** U. Fano, Description of states in quantum mechanics by density matrix and operator techniques. *Rev. Mod. Phys.* **29** (1957), 74.
- **[GS]** M. Golubitsky and D. G. Schaeffer, Singularities and Groups in Bifurcation Theory, Volume I. Applied Mathematical Sciences **51**, Springer (1985).
- **[GY]** J. H. Grace and A. Young, The Algebra of Invariants. Cambridge University Press (1903).
- **[HY]** L. He and S. Yi, Magnetic properties of a spin-3 chromium condensate. *Phys. Rev. A* **80** (2009), 033618; arXiv:0902.4276.
- **[KU]** Y. Kawaguchi and M. Ueda, Symmetry classification of spinor Bose-Einstein condensates. *Phys. Rev. A* **84** (2011), 053616; arXiv:1109.0400.
- **[KU-rev]** Y. Kawaguchi and M. Ueda, Spinor Bose-Einstein condensates. *Phys. Rep.* **520** (2012), 253–381; arXiv:1001.2072.
- **[M8.10]** OpenWave M8 track, M8.10: first correction at the level-6 critical rays. The [task record](https://github.com/openwave-labs/openwave/blob/b0b078678ca75ad31b8813806d6b61a0a386d1e0/openwave/xperiments/m8_mit/research/tasks/m8_10_task_details.md) and [method note](https://github.com/openwave-labs/openwave/blob/b0b078678ca75ad31b8813806d6b61a0a386d1e0/openwave/xperiments/m8_mit/research/findings/m8_10_method_note.md), 2026.
- **[M8.11]** OpenWave M8 track, M8.11: local branch germs at the level-6 critical rays. The [task record](https://github.com/openwave-labs/openwave/blob/b0b078678ca75ad31b8813806d6b61a0a386d1e0/openwave/xperiments/m8_mit/research/tasks/m8_11_task_details.md) and [method note](https://github.com/openwave-labs/openwave/blob/b0b078678ca75ad31b8813806d6b61a0a386d1e0/openwave/xperiments/m8_mit/research/findings/m8_11_method_note.md), 2026.
- **[M8.12]** OpenWave M8 track, M8.12: the reduced Morse census of the level-6 quartic. The [task record](https://github.com/openwave-labs/openwave/blob/b0b078678ca75ad31b8813806d6b61a0a386d1e0/openwave/xperiments/m8_mit/research/tasks/m8_12_task_details.md) and [method note](https://github.com/openwave-labs/openwave/blob/b0b078678ca75ad31b8813806d6b61a0a386d1e0/openwave/xperiments/m8_mit/research/findings/m8_12_method_note.md), 2026.
- **[M8.13]** OpenWave M8 track, M8.13: audit of the uniqueness of the top-multipole maximum at spin 3. The [task record](https://github.com/openwave-labs/openwave/blob/b0b078678ca75ad31b8813806d6b61a0a386d1e0/openwave/xperiments/m8_mit/research/tasks/m8_13_task_details.md), with the adjudication, 2026.
- **[Maj]** E. Majorana, Atomi orientati in campo magnetico variabile. *Nuovo Cimento* **9** (1932), 43.
- **[Re]** B. Reznick, An inequality for products of polynomials. *Proc. Amer. Math. Soc.* **117** (1993), no. 4, 1063–1073.
- **[RK]** J. L. Romero, A. B. Klimov, A. Z. Goldberg, G. Leuchs and L. L. Sánchez-Soto, Multipoles from Majorana constellations. *Phys. Rev. A* **109** (2024), 012214; arXiv:2401.07904.
- **[Sh]** B. Shatto, The Surviving Ray: channel selection for a cubic self-interaction on $`S^3/2I`$. *Zenodo* (2026), [https://doi.org/10.5281/zenodo.22681502](https://doi.org/10.5281/zenodo.22681502).
- **[SP]** L. Santos and T. Pfau, Spin-3 chromium Bose-Einstein condensates. *Phys. Rev. Lett.* **96** (2006), 190404; arXiv:cond-mat/0510634.

---

## Citation

```
Shatto, B. (2026).
The Surviving Ray: channel selection for a cubic self-interaction on S³/2I.
SSRN.
https://ssrn.com/abstract=7443959
```

---

## Independent numerical certification

[![OpenWave](/files/assets/openwave-banner-graphite.svg)](https://github.com/openwave-labs/openwave/blob/b0b078678ca75ad31b8813806d6b61a0a386d1e0/openwave/xperiments/m8_mit/research/findings/m8_1_2_method_note.md)

Twenty-one claims pre-registered from the concept paper [Sh] have been reproduced on the OpenWave M8 track
by an independent, blind computation. Two agents, a solver and an auditor, built every object from its
definition in their own code, with no access to the paper, its title or any value it claims, and the
auditor, working on disjoint primitives, tried to refute every answer the solver gave and refuted none.
This is a blind recomputation of those claims, from definitions, not a second proof:
the proofs were not checked line by line, the run stops at level 6 and at the two interactions built
there, the general-spin constant of Section 5.9 was left out of the claims, and no dynamics was run.
The [method note](https://github.com/openwave-labs/openwave/blob/b0b078678ca75ad31b8813806d6b61a0a386d1e0/openwave/xperiments/m8_mit/research/findings/m8_1_2_method_note.md) carries the full record.

Four later runs on the track reproduced or audited the results of Sections 7 and 8, and every link to
its records points to its repository at one commit, `b0b07867`. M8.10 reproduced the eight values of
the first correction in Section 8.2 blind, as exact results, and its negative control at the pyramid
fired blind ([task](https://github.com/openwave-labs/openwave/blob/b0b078678ca75ad31b8813806d6b61a0a386d1e0/openwave/xperiments/m8_mit/research/tasks/m8_10_task_details.md), [method note](https://github.com/openwave-labs/openwave/blob/b0b078678ca75ad31b8813806d6b61a0a386d1e0/openwave/xperiments/m8_mit/research/findings/m8_10_method_note.md)).
M8.11 audited the local branch germs: the theorem of Section 8.3 is an audited argument, with one
supplied step, and the one-line sign step of its $`\lambda_4`$ lemma was graded a defect and overruled
with the reason recorded; the run's method note puts the weight states $`v_1`$ and $`v_2`$ out of
scope, while its frozen task, which Section 8.3 follows, covers them
([task](https://github.com/openwave-labs/openwave/blob/b0b078678ca75ad31b8813806d6b61a0a386d1e0/openwave/xperiments/m8_mit/research/tasks/m8_11_task_details.md), [method note](https://github.com/openwave-labs/openwave/blob/b0b078678ca75ad31b8813806d6b61a0a386d1e0/openwave/xperiments/m8_mit/research/findings/m8_11_method_note.md)).
M8.12 reproduced the census of Section 7.2 in two blind rooms under an adversarial audit; the
adjudication records every claim reproduced and the classification's arguments sound, with one clause
left open, the uniqueness of the maximum
([task](https://github.com/openwave-labs/openwave/blob/b0b078678ca75ad31b8813806d6b61a0a386d1e0/openwave/xperiments/m8_mit/research/tasks/m8_12_task_details.md), [method note](https://github.com/openwave-labs/openwave/blob/b0b078678ca75ad31b8813806d6b61a0a386d1e0/openwave/xperiments/m8_mit/research/findings/m8_12_method_note.md)).
M8.13 audited that uniqueness: an offline auditor reached the complete maximiser set by its own route
before it saw the author's, then graded the author's argument part by part, ten verdicts with no gap
and no defect. The adjudication records the uniqueness as an audited argument. It did not check the
note's attribution of the nematic bound, which Section 9.2 takes from the sources themselves, and in its
words, "the gate's 97 checks and the mutation suite's 66 arms remain the author's report"; the package
has since landed, [with those instruments](https://github.com/openwave-labs/openwave/blob/b0b078678ca75ad31b8813806d6b61a0a386d1e0/openwave/xperiments/m8_mit/research/scripts/m8_13_author/MANIFEST.md)
([task, with the adjudication](https://github.com/openwave-labs/openwave/blob/b0b078678ca75ad31b8813806d6b61a0a386d1e0/openwave/xperiments/m8_mit/research/tasks/m8_13_task_details.md),
[auditor's return](https://github.com/openwave-labs/openwave/blob/b0b078678ca75ad31b8813806d6b61a0a386d1e0/openwave/xperiments/m8_mit/research/m8_13/run/stage2b_return.md),
[author's dated correction](https://github.com/openwave-labs/openwave/blob/b0b078678ca75ad31b8813806d6b61a0a386d1e0/openwave/xperiments/m8_mit/research/scripts/m8_12_author/S0_S3_MAXIMUM_CORRECTION.md)).

Section 7.3 carries the author's argument as a complete proof, with a dagger on each step the audit
supplied. The [dagger map](/files/framework/files/bedrock/files/scripts/surviving-ray-v2/dagger-map.md) names the proof's five departures from the audited
note, matches each dagger to the audit's three records, and notes the two supplied steps that Section 6
also uses.

---

## The certificates of Section 7.2

The three orbits of Section 7.2 outside the census's class are certified by this paper, in 60-digit
interval arithmetic; the certificates are its own computation, not a reproduction. They are published
in [one folder](/files/framework/files/bedrock/files/scripts/surviving-ray-v2/), in two layers: the record, the certification as it ran under frozen packets,
which starts from an exploratory census that is not distributed and so is not meant to be rerun; and
the reproduction, a verifier that rebuilds each certified box from a published data file and repeats
every test, with controls started from the census's exact representatives [M8.12]. The folder's
[README](/files/framework/files/bedrock/files/scripts/surviving-ray-v2/README.md) maps each statement of Section 7.2 to the log lines that give it, and its
`SHA256SUMS` lists the SHA-256 of the 31 other files in it, which `shasum -a 256 -c SHA256SUMS`
checks; the manifest's own SHA-256 is `6a3e3027683e6baad41fafa8204acd21e52b7226a99d616a6e9af36c6d00a03f`.

---

/ **[`↑top`](#top)** / **[`main`](https://github.com/dmobius3/mode-identity-theory/tree/main/)** / **[`framework`](/files/framework/)** / **[`bedrock`](/files/framework/files/bedrock/)** / **[`working`](/files/framework/files/working/)** / **[`cosmos`](/files/cosmos/)** / **[`spectrum`](/files/spectrum/)** / **[`tools`](/files/tools/)** /
