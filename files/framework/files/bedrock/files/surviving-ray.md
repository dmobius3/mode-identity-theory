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
built from $`\psi\psi^{T}`$, is filtered by the same mechanism onto a different plane. The density
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
numerically, the ground states. This version gives an audited census within a stated class,
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
when the six Majorana points are antipodally symmetric as a multiset. Ranks are quoted as spins
throughout, so that the spin-8 target and the rank-6 channel below are the same kind of index; the
classical invariant theory numbers the same object by its binary degree, 16, and that number is a
form degree and not a rank. The proof is short and rests on a classical fact about binary forms,
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
of the branching $`V_3\vert_{2I}`$ are proper. That norm takes the same value in both sectors,
because they are complementary in $`\dim V_3 = 7`$. The normalised coefficient $`w_6`$ does not, and
Section 5.3 keeps the two apart.

The derived weight and an earlier form fitted to the observed normalisation agree at both values of
$`\dim\sigma`$ that occur. Those two are the only ones the branching produces, so no measurement
inside this system distinguishes them. The correction is carried by the derivation alone.

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
purposes, but not by that theorem. That is a narrower claim and a sharper one, since it separates a
general piece of representation theory from the specific arithmetic of a quotient.

Spin 3 can say exactly what the selected channel is, at one point. The four-dimensional family is the
four-channel spin-3 interaction of the condensate literature [DH], [KU], and the surviving ray is one
coupling point of it: there the governing quartic is an affine image of the spin-3 mean-field energy,
by a polynomial identity (Proposition 6.1). At the paper's sign the energy is least on the coherent
states and greatest on the hexagon. The condensate literature has the stationary states at that point
and, from numerical minimisation, the ground states: [KU]'s second phase diagram places the paper's
point inside the ferromagnetic phase and the opposite point inside the phase of the hexagon. That
placement is numerical, and it is [KU]'s. The point is where this interaction lands, and not the
coupling of a physical condensate (Section 6.3).

At that point this version gives an audited census within a stated class, certified critical orbits
outside it, and exact results at the two ends (Section 7).
Within the class of orbits whose fixed locus has projective dimension at most one there are exactly
ten critical orbits, with their values and Morse indices; the classification is an audited argument,
and its values were reproduced blind [M8.12]. Three critical orbits outside the class are certified
by interval arithmetic, and one of them lies below the octahedron in value and above it in index, so
with them the index no longer increases with the value. The minimum of $`\widehat{r}_6`$ is
$`1/924`$, attained exactly on the coherent states: an identity writes the top multipole as the
squared Bombieri norm of the product of the Majorana sextics of $`u`$ and $`\Theta u`$, and the
Beauzamy-Bombieri-Enflo-Montgomery inequality [BBEM] with Reznick's equality case [Re] then completes
a statement of Björk et al. [Bj]. The maximum is $`463/924`$, attained exactly on the hexagon orbit
(Theorem 7.5). The value and the question are Romero et al.'s [RK]; the argument was audited on the
OpenWave M8 track [M8.13], and the proof marks each step the audit supplied.

Back on the quotient, the selected equation is a bifurcation problem on the flat bundles over
$`S^3/2I`$, with the nonlinearity kept as a hypothesis (Section 8). The first correction at the four
symmetry-pinned rays is exact and was reproduced blind [M8.10]; local branch germs exist, for
sufficiently small amplitude, at the six rays of Section 7.1, where they are expanded, and by the same
theorem at $`v_1`$ and $`v_2`$, as an audited argument [M8.11]. No radius is given for the germs, and
neither result implies stability.

The sections follow what does the work. The quotient selects, in Sections 2 to 5, through the two
facts named above. Spin 3 decides what the selected channel does, in Sections 6 and 7, at one coupling
point and with no icosahedral input. The selected equation then bifurcates on the quotient, in
Section 8, where the flat bundles over $`S^3/2I`$ return. Nothing at the point is offered as evidence
for the quotient or for anything physical.

One boundary should be drawn explicitly. The configurations appearing below are known: the octahedral
constellation is the anticoherent state of order 3 in the standard classification, and critical rays
occur here with all four of the six-vertex shape types [BTD] names. Recognising a configuration is not
the same as selecting it, and *configuration prior art is not selection prior art*. The contribution
of the selection is which member of a known family a specific geometry forces, and the surrounding
accounting of what that forcing does and does not explain. At the point the boundary has a companion:
*knowing the phases is not classifying the critical geometry*. The condensate literature has the
stationary states and, numerically, the ground states; a procedure that minimises the energy on each
fixed set finds line minima, and at each sign two census orbits are line maxima that such a procedure
cannot return (Section 7.2).

Two of the limits above are of record rather than of proof, and belong in one place. The sources of
Sections 6 and 7 were read in their own text for this version, except [BBEM], whose inequality enters
through [Re]'s statement of it; the sentences naming the wider constellation literature rest, as in the
first version, on abstracts and publisher records; and every search is reported as a search and not as
a novelty finding (Section 9.3). The anticoherence fact
used below is not taken on trust from that literature, and Section 7.1 establishes it here.

Section 2 fixes the state space and the time reversal, then the quotient's sectors and invariant
degrees and the interaction the rest of the paper uses. Its one transform is fed three different
arguments, not two. Section 3 gives the ambient proposition. Section 4 records the reduction that
isolates the four-dimensional family and states what it can and cannot touch. Section 5 proves the
selection theorem, computes the surviving weight, states the normalisation's own ceiling, connects
the ambient channel back to the quotient, and derives consequences across levels and sectors.
Section 6 places the selected interaction at its point of the condensate literature's coupling space.
Section 7 gives the critical geometry there: the first version's critical rays, the census within its
class with the three certified orbits outside it, and the two extremes. Section 8 returns to the
quotient for the first correction and the local branch germs, with their ceilings stated. Section 9
says what is not claimed, gives the prior art and the search, and closes with the open historical
question and where the family sits. After the references, three sections record the verification:
the first version's blind reproduction, the runs behind Sections 7 and 8, and this paper's own
certificates. A last section lists what changed from the first version.

---

## 2. Setup

### 2.1 The state space and the Majorana dictionary

Let $`V_j = \mathrm{Sym}^{2j}\mathbb{C}^2`$ be the irreducible $`\mathrm{SU}(2)`$ representation of
spin $`j`$ and dimension $`2j+1`$, with orthonormal weight basis $`v_m`$, $`-j \le m \le j`$. The
state space throughout is $`V_3`$, of dimension 7. A state $`u = \sum_m u_m v_m`$ is written as the
binary sextic

```math
F_u(z) \;=\; \sum_{m=-3}^{3} (-1)^{\,3-m}\sqrt{\binom{6}{3+m}}\; u_m\, z^{\,3-m} ,
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
The weight reversal and the relative $`(-1)^m`$ pattern are forced; only an overall phase is
conventional. Antilinear intertwiners of $`V_3`$ with itself are
$`\mathrm{Hom}_{\mathrm{SU}(2)}(\overline{V_3}, V_3)`$, which is one-dimensional by Schur since
$`V_3`$ is irreducible and self-dual, so $`\Theta`$ is unique up to a complex scalar. To identify
it, write $`\Theta v_m = c_m v_{-m}`$ with $`\Theta`$ antilinear, and impose
$`\Theta J_+ = -J_- \Theta`$. Since $`J_+ v_m = \alpha_m v_{m+1}`$ with
$`\alpha_m = \sqrt{j(j+1) - m(m+1)}`$, and $`J_- v_{-m} = \alpha'_m v_{-m-1}`$ with
$`\alpha'_m = \sqrt{j(j+1) - (-m)(-m-1)}`$, the two coefficients are equal because
$`(-m)(-m-1) = m(m+1)`$, and this reads $`\alpha_m c_{m+1} = -\alpha_m c_m`$, so $`c_{m+1} = -c_m`$
and $`c_m = c\,(-1)^m`$; antiunitarity fixes $`\lvert c \rvert = 1`$. The global constant is a
genuine convention and the $`m`$-dependence is not, which matters below because it is the
$`m`$-dependence that supplies the alternating sign in the operator of Section 5. One computes
$`\Theta^2 = (-1)^{2j}`$, so $`\Theta^2 = +1`$ here and $`\Theta^2 = -1`$ at half-integer spin.

Two labels used throughout should be read as representation theory and nothing more. *Spin 3* names
the irreducible $`\mathrm{SU}(2)`$ representation $`V_3`$ and the harmonic level it sits at; it is
not a claim that anything described here has physical spin 3. And $`\Theta`$ is the standard
antiunitary intertwiner of that representation with its conjugate. The equation studied below is
elliptic and stationary, with no time in it, so nothing here establishes a physical time-reversal
symmetry of a dynamics; $`\Theta`$ earns its name from its algebra, not from an evolution it
commutes with.

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
\mathcal{M}_K(P)_N \;=\; \sum_{n+n' = N} \langle 3\,n;\, 3\,n' \mid K\,N \rangle \, (-1)^{n'} P_{n,\,-n'} ,
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
\rho_K(u) \;=\; \mathcal{M}_K\!\left(u u^{\dagger}\right) ,
```

and it does not vanish for odd $`K`$ in general.

The **right multipole** is the same transform at a different argument, $`R_K = \mathcal{M}_K(P)`$
with $`P`$ the isotypic projector of Section 2.4. Same map, different matrix; the two multiply
rather than merge, and Section 5 turns on that.

The factorisation of Section 5 uses this one $`\mathcal{M}_K`$ on both sides, which is what makes
the two multipoles multiply: the time-reversal phase sits inside $`\mathcal{M}_K`$ itself, and
$`\rho_K(u) = \mathcal{M}_K(u u^{\dagger})`$ holds because
$`(\Theta u)_{n'} = (-1)^{n'}\overline{u_{-n'}}`$ is exactly the factor the definition carries.

Three notational distinctions matter throughout. $`\rho_K`$ with a subscript is always a density
multipole and never a representation of $`2I`$; representations are written $`\sigma`$ throughout.
The index $`K`$ on a multipole is a spin, while the $`J`$ on $`B_J`$ is the same kind of index; no
quantity in this paper is indexed by a binary form degree except where that is said explicitly.
Spins do not all live on one axis either: a multipole of the density is indexed by its own rank, a
channel of the nonlinearity by the spin of its target, and these label different decompositions.
Section 3 works at output spin 8, Section 5 at density rank 6 and output spin 3; the 6 and the 8 are
not comparable as indices. Section 5.7 does relate the two objects, but as a coupling of a rank-6
multipole to the state, not as an identity between labels.

> **Lemma 2.1.** $`B_J`$ and $`\rho_J`$ agree on $`\mathrm{Fix}(\Theta)`$, and differ over
> $`\mathbb{C}`$.

On $`\mathrm{Fix}(\Theta)`$ the two coincide because $`\Theta u = u`$, so in particular $`\rho_J`$
inherits the vanishing of $`B_J`$ at odd $`J`$ there. Off that locus they part company, and not
slightly: the coherent state $`v_3`$ has $`B_2(v_3) = 0`$, since $`v_3 \otimes v_3`$ has weight 6
and cannot meet a spin-2 summand at all, while its density quadrupole $`\rho_2(v_3)`$ is nonzero.
Every $`\mathrm{Fix}(\Theta)`$ statement below is stated for $`\rho_J`$ and would be false for
$`B_J`$, and conversely; the distinction is not bookkeeping. $`\square`$

The vanishing of the odd multipoles is a separate statement. Section 3 reaches the same locus by a
different route, through the Jacobian kernel, so the two are a check on each other rather than one
serving the other.

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
the functions $`\psi \colon \mathrm{SU}(2) \to \mathbb{C}^{\dim\sigma}`$, written as rows,
satisfying $`\psi(gh) = \psi(g)\,\sigma(h)`$ for $`h \in 2I`$. An intertwiner
$`\eta \in \mathrm{Hom}_{2I}(\sigma, V_j)`$ is correspondingly a map with
$`D^j(h)\,\eta = \eta\,\sigma(h)`$, and by Peter-Weyl the sections at level $`\ell = 2j`$ are
$`V_j \otimes \mathrm{Hom}_{2I}(\sigma,\, V_j)`$, realised as

```math
\psi_a(g) \;=\; \sum_{m,n} u_m\, D^j_{mn}(g)\, \eta_{na} ,
```

so the left index is free and the right index carries the sector. The convention is fixed here
because dual-looking Peter-Weyl formulas are both defensible and only one of them matches the
factorisation of Section 5. Since $`\sigma`$ is unitary,
$`\lvert\psi(gh)\rvert^2 = \lvert\psi(g)\rvert^2`$, so the density really is a function on $`X`$. A
*block state* at level 6 is one for which $`j = 3`$, so its left index runs over the $`V_3`$ of
Section 2.1 and its right index over a multiplicity space that the branching below shows to be
one-dimensional. **Level 6 is the scope of the selection theorem of Sections 4 through 5.5.** What
fixes it is the choice of object: this paper is about spin-3 states, so the left index is $`V_3`$
and the level is $`2 \cdot 3`$. Within the two sectors multiplicity stays at one wherever they
occur, at levels 12 and 16 as well; the table in Section 4.3 shows both the repetition it does
permit elsewhere, $`\mathbf{5}`$ twice at level 16, and the absence of $`\mathbf{3}'`$ at level 12.
What is special about level 6 is that fixing the left spin fixes the level, and at that level the
branching happens to be multiplicity-free, which is what the Schur argument of Section 5.1 needs.
Section 3 is ambient spin-3 mathematics and is not scoped by any of this.

Two facts about $`2I`$ drive the selection theorem, both classical and both recomputed here from the
group rather than cited. They are the two inputs named in Section 5.1. First, the dimensions of the
invariants,

```math
\dim (V_j)^{2I} \;=\; 1,\,0,\,0,\,0,\,0,\,0,\,1,\,0,\,0,\,0,\,1,\,0,\,1,\,0,\,0,\,1
\qquad (j = 0,\dots,15),
```

so invariants occur at levels 0, 12, 20, 24 and 30. All three generator degrees of the invariant
ring of $`2I`$ appear, 12, 20 and 30, and 24 is the first product, $`I_{12}^2`$. Only the gap below
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
$`\eta^{\dagger}\eta = c\, I_\sigma`$; rescale so that $`c = 1`$, so that $`P = \eta\eta^{\dagger}`$
is the orthogonal projector onto the $`\sigma`$-summand of $`V_3`$. Without that normalisation $`P`$
is a multiple of the projector and every quantity built from it carries an undetermined constant, so
it is fixed here once.

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
each. Choosing real orthonormal models then gives $`\sigma(h)\sigma(h)^{T} = I`$. Hence
$`\psi\psi^{T}`$ is also a genuine function on $`X`$ and $`\int\lvert\psi\psi^{T}\rvert^2`$ is a
second local, $`2I`$-invariant quartic. The filter of Section 4 applies to it unchanged, since its
right-hand factor is the plain Clebsch-Gordan projection of $`\eta\eta^{T}`$, carrying neither the
$`\Theta`$ phase nor the index reversal that $`\mathcal{M}_K`$ carries. That is exactly why the
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

This section uses no icosahedral input, and everything in it holds for spin 3 with time reversal. It
is not, however, a separate note. The trilinear data $`(u, \Theta u, u)`$ admits an equivariant
contraction into every $`V_J`$ occurring in $`\mathrm{Sym}^2 V_3 \otimes V_3`$, and those
contractions are the channels of a single object indexed by the spin of the target. The physical
self-interaction is the spin-3 channel, which Sections 4 and 5 select within; the covariant below is
the spin-8 channel. The uniqueness proved here and the four-parameter family found there are the
same weight count run at two targets. That is the shallow reason both belong in one paper; the real
one is Section 5.7, which shows the spin-8 channel is populated on $`X`$ and that the states
annihilating it are exactly the time-reversal-invariant ones. This is stated as a proposition and
not a theorem. Its ingredients are classical: the multiplicity count, the first transvectant, and
the Jacobian criterion. Whether the joint covariant of two independent sextics of bidegree
$`(2,1)`$, or this particular time-reversal specialisation of it along $`g = \Theta f`$, has
appeared previously is left open in Section 9. Nothing in the paper's contribution rests on the
answer, since that contribution is the channel selection of Sections 4 and 5 and the
study of the selected channel in Sections 6 to 8.

### 3.1 The cubic covariant

The maps in this paper are not holomorphic cubics, and the distinction has to be made before any
multiplicity is quoted. Holomorphic cubics $`V_3 \to V_J`$ are counted by
$`\mathrm{Hom}_{\mathrm{SU}(2)}(\mathrm{Sym}^3 V_3,\, V_J)`$, and
$`\mathrm{Sym}^3 V_3 = V_1 \oplus 2V_3 \oplus V_4 \oplus V_5 \oplus V_6 \oplus V_7 \oplus V_9`$, of
dimension $`\binom{9}{3} = 84`$ with spin 3 occurring twice: it contains no $`V_8`$, so no
holomorphic cubic into the spin-8 target exists at all. The maps here are of type $`(2,1)`$,
quadratic in the state and antilinear in it through time reversal, so the space to count is

```math
\mathscr{E}_J \;:=\; \mathrm{Hom}_{\mathrm{SU}(2)}\!\left(\mathrm{Sym}^2 V_3 \otimes \overline{V_3},\, V_J\right)
\;\simeq\;
\mathrm{Hom}_{\mathrm{SU}(2)}\!\left(\mathrm{Sym}^2 V_3 \otimes V_3,\, V_J\right) ,
```

the isomorphism induced by $`\Theta`$, which supplies the linear intertwiner
$`\overline{V_3} \simeq V_3`$. This notation is used for the rest of the paper. An exact weight
count gives

```math
\dim \mathscr{E}_8 \;=\; 2 - 1 \;=\; 1 ,
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
\mathcal{C}(u) \;:=\; T(u,\, \Theta u,\, u) \;=\; -\tfrac{\kappa}{2}\, F \,(F, \Theta F)_1 ,
```

the second term of the polarisation dropping out because $`(F,F)_1 = 0`$ by antisymmetry.

The two specialisations look independent and are not. Setting $`a = u`$ and $`b = \Theta u`$ in the
first gives $`T(u, u, \Theta u) = \kappa F (F, \Theta F)_1 = -2\,\mathcal{C}(u)`$, so they differ by
a constant. That is not a coincidence: $`\dim\mathscr{E}_8 = 1`$ leaves no room for two independent
objects, and the $`-2`$ is the proportionality that uniqueness forces.

Following Section 2.3, $`\mathcal{C}`$ takes values in $`V_8`$, and is referred to as the spin-8
cubic channel. Classical invariant theory numbers the same object by the degree of the binary form,
16; that is a form degree, not a spin, and it is not used as an index anywhere below.

### 3.2 The classical input

One classical fact is used. It is short enough to prove, which is done here rather than cited, so
that its hypotheses are visible in the argument that needs them.

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

The hypotheses are used in order and each is visible: characteristic zero so that the positive
degree $`n`$ is nonzero in the field and can be cancelled after Euler, whose identity itself needs
no such hypothesis, $`f \neq 0`$ to divide, and equal degree for the last step, since $`g/f`$ is
homogeneous of degree zero only when the degrees agree. The two forms in Section 3.3 are both
sextics, so the degree hypothesis is automatic there; Section 5.7 needs a weaker unequal-degree
form, developed where it is used. Nonvanishing is supplied by the next remark.

Because $`\Theta`$ is injective and the dictionary from states to sextics is linear, $`F \neq 0`$
and $`\Theta F \neq 0`$ whenever $`u \neq 0`$. So Lemma 3.1 applies to the pair $`(F, \Theta F)`$ at
every nonzero state.

### 3.3 The kernel, and the proposition that follows from it

> **Lemma 3.2.** For $`a \neq 0`$, the kernel of the linear map $`b \mapsto T(a,a,b)`$ is exactly
> $`\mathbb{C}a`$.

By the diagonal specialisation, $`T(a,a,b) = \kappa f (f,g)_1`$, and $`\kappa \neq 0`$ with
$`f \neq 0`$, so the kernel is cut out by $`(f,g)_1 = 0`$. By Lemma 3.1 this holds exactly when
$`g`$ is proportional to $`f`$, that is when $`b \in \mathbb{C}a`$. $`\square`$

> **Proposition 3.3.** For $`u \neq 0`$, $`\mathcal{C}(u) = 0`$ if and only if $`[u]`$ is
> time-reversal invariant. Equivalently,
>
> ```math
> Z(\mathcal{C}) \;=\; U(1)\cdot\mathrm{Fix}(\Theta) .
> ```

Apply Lemma 3.2 at $`a = u`$, $`b = \Theta u`$. Its kernel condition reads $`T(u,u,\Theta u) = 0`$
if and only if $`\Theta u \in \mathbb{C}u`$, and by Section 3.1 that left side is
$`-2\,\mathcal{C}(u)`$. Antiunitarity makes the constant a phase, so $`\Theta u = \lambda u`$ with
$`\lvert\lambda\rvert = 1`$, which by Section 2.2 is exactly membership in
$`U(1)\cdot\mathrm{Fix}(\Theta)`$. $`\square`$

So the proposition is a corollary rather than a parallel result: one classical criterion, applied
once, yields both statements. The slot distinction that Section 2.3 insists on is a distinction
between $`B_J`$ and $`\rho_K`$, and it remains; what does not survive is the idea that these two
zero sets are reached independently.

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

Section 3 was ambient. From here the quotient enters, and this section covers the first of the two
ways it does so: it decides which levels a density is allowed to have. The second, the
multiplicity-free branching that scalarises the right-index contraction and fixes the weight, enters
in Section 5.

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

This is the first of the paper's two icosahedral inputs, the invariant-degree filter. It gives five
vanishings and is silent both on whether the surviving ranks select single maps and on whether the
surviving weight is nonzero. Both of those come from the second input, the multiplicity-free
branching of Section 2.4: it scalarises the right-index contraction in Section 5.1 and supplies the
weight in Section 5.3. Lemma 4.1 is a statement about the *coefficients* of the density's expansion,
not about the tensors that carry them. The level-$`2K`$ component of the density factorises, and
Lemma 4.1 says the right-hand factor vanishes for $`K = 1,\dots,5`$. It does not say the left-hand
factor does, and in general the left-hand factor does not: the density multipoles $`\rho_K(u)`$ of
Section 2.3 are generically nonzero across the whole range, and at the octahedral state $`\rho_4`$
is the *largest* of them. A vanishing coefficient is not a vanishing tensor.

### 4.2 The four-dimensional family

The other side of the reduction is what there is to select from: the type-$`(2,1)`$ self-maps of
$`V_3`$, which by Section 3.1 form the space $`\mathscr{E}_3`$. The weight count gives

```math
\dim \mathscr{E}_3 \;=\; 16 - 12 \;=\; 4 ,
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
\mathscr{E}_3 \;=\; \bigoplus_{J = 0,2,4,6} \mathrm{Hom}_{\mathrm{SU}(2)}\!\left(V_J \otimes V_3,\, V_3\right) ,
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

So the family has two natural indexings, and they are the two objects Section 2.3 warns must be kept
apart: the canonical basis $`N_J`$ is indexed by the ranks of the holomorphic square, and the set
$`M_K`$ by the ranks of the density. They are related by recoupling. The $`M_K`$ are seven vectors
in a four-dimensional space and are therefore linearly dependent, which is worth remembering before
drawing any conclusion from the index $`K`$ alone. Since $`M_0`$ turns out to be the radial
direction, the selection theorem needs only that $`M_6`$ is *not* radial, which is what makes the
surviving ray a ray rather than nothing. That is proved in Section 5 from material the theorem needs
anyway, and is not assumed here. The seven $`M_K`$ together span $`\mathscr{E}_3`$, verified by
exact computation. That is a separate fact: the selection argument does not use it, and Section 5.2
uses it only to explain how the weights $`w_K`$ are defined.

### 4.3 The spine

These are the two targets named at the head of Section 3, and the contrast between them is what
gives the paper its shape. Put the counts side by side.

```math
\dim \mathscr{E}_8 = 1 , \qquad \dim \mathscr{E}_3 = 4 .
```

The spin-8 target is rigid: its type-$`(2,1)`$ covariant space is one-dimensional, so there is no
nontrivial projective choice for a geometry to make within it. A geometry might still decide whether
that channel appears, or with what coefficient; what it cannot do is choose among projectively
distinct maps, because there is only one ray. The spin-3 target is four-dimensional, so channel
selection has genuine content there.

The same method answers the corresponding *availability* question, whether the quotient supplies a
compatible spin-8 target slot at all. Both $`V_3`$ and $`V_8`$ have integer spin and so factor
through $`A_5`$, and the branching is

| level | dim | $`\mathbf{1}`$ | $`\mathbf{3}`$ | $`\mathbf{3}'`$ | $`\mathbf{4}`$ | $`\mathbf{5}`$ |
|---|---|---|---|---|---|---|
| 6 | 7 | 0 | 0 | 1 | 1 | 0 |
| 12 | 13 | 1 | 1 | 0 | 1 | 1 |
| 16 | 17 | 0 | 0 | 1 | 1 | 2 |

The two constituents of $`V_3`$ are $`\mathbf{3}'`$ and $`\mathbf{4}`$, and both occur in $`V_8`$
with multiplicity one, so both sectors occurring at level 6 also occur at level 16 and the spin-8
target is available in either. That is what the table establishes and all that is claimed here: it
says the slot exists, not that the particular covariant has nonzero coefficient into it, which would
need a right-index contraction for $`\mathcal{C}`$ of the kind Section 5 carries out for the
density. The slot is at least reachable: by Lemma 4.1 the density has levels 0 and 12 only, level 0
times level 6 returns level 6 alone, and level 12 times level 6 spans levels 6 through 18. So the
entire level-16 output comes from $`d_{12}\psi`$, and the only obstruction is whether the right-hand
factor vanishes. That is settled in Section 5.7, which needs the weight computed in Section 5.3 and
so cannot be argued here: it does not vanish, and the channel is populated in both sectors. The
level-12 row is the one Lemma 4.1 turns on, the trivial representation appearing there being the
density's surviving channel, so the bandlimit and the output channel can be read off a single table.
This is why the two halves of the paper have different characters. Proposition 3.3 is a statement
about a canonical object and is true for any spin-3 system with time reversal. The selection theorem
is a statement about which member of a genuine family a particular quotient permits, and it has no
content at all without the family being larger than one.

### 4.4 What the reduction cannot touch

Lemma 4.1 constrains the density's spectrum and nothing else. It says nothing about
$`\mathscr{E}_3`$ itself, which remains whatever spin-3 representation theory makes it: the
dimension, the canonical basis $`N_J`$, the operators $`A_K`$ and their weight structure, the maps
$`M_K`$, an overcomplete family, and the relations among them are all fixed before $`2I`$ is
mentioned, and are the same for any system carrying spin 3 with time reversal. What the quotient
supplies is a set of coefficients, most of them zero.

Stated as a slogan: the family is universal, and the quotient selects the nonradial ray and its
weight. Section 5 carries out that choice and computes the one coefficient that survives.

---

## 5. The selection theorem

### 5.1 Statement

> **Theorem 5.1.** Let $`\psi`$ be a block state at level 6 on $`X = S^3/2I`$, in the sector
> $`\sigma`$, write $`d = \dim\sigma \in \{3,4\}`$, and take the self-interaction and the quartic
> to be those of Section 2.5, namely the block projection of $`\lvert\psi\rvert^2\psi`$ and the
> ratio built from $`\int\lvert\psi\rvert^4`$. Then:
>
> 1. the self-interaction lies in $`\mathrm{span}\{M_0, M_6\} \subset \mathscr{E}_3`$;
> 2. $`M_0`$ is radial, $`M_0(u) = -\lVert u\rVert^2 u/\sqrt{7}`$;
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

The theorem uses two icosahedral inputs and no others, and naming them exactly matters here, since
the scalarisation just used is one of them. They are **the invariant-degree filter**, which leaves
density ranks 0 and 6 and is Lemma 4.1; and **the multiplicity-free complementary branching**
$`V_3\vert_{2I} = \sigma_3 \oplus \sigma_4`$, which does two jobs, scalarising the right-index
contraction here by Schur and supplying the weight in Section 5.3. Multiplicity one and
complementarity are two consequences of that one branching statement, which is why the count is two
and not three.

### 5.2 The quartic, and the Peter-Weyl factorisation

Two preliminaries. First, clause 2. The rank-0 coupling contracts $`u`$ against $`\Theta u`$ to a
scalar,

```math
\rho_0(u) \;=\; [u \otimes \Theta u]_0 \;=\; -\frac{\lVert u\rVert^2}{\sqrt{7}} ,
\qquad\text{so}\qquad
M_0(u) \;=\; [\rho_0(u) \otimes u]_3 \;=\; -\frac{\lVert u\rVert^2}{\sqrt{7}}\, u ,
```

which is clause 2. Within $`\mathscr{E}_3`$, "radial" and "proportional to $`M_0`$" are the same
condition: a radial equivariant map has the form $`\lambda(u)u`$ with $`\lambda`$ an invariant of
type $`(1,1)`$, and $`\mathrm{Hom}_{\mathrm{SU}(2)}(V_3 \otimes \overline{V_3}, \mathbf{1})`$ is
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
explicitly. With Haar measure normalised and $`\eta^{\dagger}\eta = I_\sigma`$,

```math
\int \lvert\psi\rvert^2 \;=\; \frac{1}{7}\lVert u\rVert^2\, \mathrm{tr}\,P \;=\; \frac{d}{7}\lVert u\rVert^2 ,
```

so $`(\int\lvert\psi\rvert^2)^2 = (d^2/49)\lVert u\rVert^4`$ and there is no undetermined factor
anywhere.

By the convention fixed in Section 2.4 a section is
$`\psi_a(g) = \sum_{m,n} u_m D^3_{mn}(g)\,\eta_{na}`$. Expanding the density and using
$`D^3 D^3 = \sum_K \langle\cdot\rangle\langle\cdot\rangle D^K`$ separates the two indices: the
level-$`2K`$ component of $`\lvert\psi\rvert^2`$ is

```math
d_{2K} \;=\; \rho_K(u) \otimes R_K(P) , \qquad P = \eta\eta^{\dagger} ,
```

with both factors the *same* transform $`\mathcal{M}_K`$ of Section 2.3, applied to $`uu^{\dagger}`$
on the left and to $`P`$ on the right. Peter-Weyl orthogonality,
$`\int D^K_{MN}\overline{D^{K'}_{M'N'}} = \delta/(2K+1)`$, gives the numerator, while the
normalisation above gives the denominator:

```math
A(u) \;:=\; \int\lvert\psi\rvert^4 \;=\; \sum_K \frac{\lVert\rho_K(u)\rVert^2\,\lVert R_K(P)\rVert^2}{2K+1} ,
\qquad
B(u) \;:=\; \int\lvert\psi\rvert^2 \;=\; \frac{d}{7}\lVert u\rVert^2 .
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

The formula is also what defines the individual $`w_K`$, because the seven quartics
$`\lVert\rho_K(u)\rVert^2`$ are not linearly independent. A real $`\mathrm{SU}(2)`$-invariant
quartic of type $`(2,2)`$ on $`V_3`$ has the form $`\langle u \otimes u,\, T(u \otimes u)\rangle`$
for a Hermitian equivariant endomorphism $`T`$ of
$`\mathrm{Sym}^2 V_3 = V_6 \oplus V_4 \oplus V_2 \oplus V_0`$, and because that decomposition is
multiplicity-free such $`T`$ form a real four-dimensional space. The seven quartics span it: by
Euler's identity the map $`\widetilde{Q} \mapsto \nabla_{\bar u}\widetilde{Q}`$ is injective on
homogeneous quartics (Section 9.5), it sends $`\lVert\rho_K\rVert^2`$ to $`c_K M_K`$ with every
$`c_K`$ nonzero (Section 5.5), and the seven $`M_K`$ span $`\mathscr{E}_3`$ (Section 4.2). So they
satisfy three independent linear relations, and $`Q`$ alone does not fix the coefficients of an
expansion in them: the $`w_K`$ are the ones the Peter-Weyl factorisation produces, not coefficients
read off from $`Q`$. Nothing downstream turns on this. Only $`w_0`$ and $`w_6`$ are nonzero, since
$`R_K(P) = 0`$ for $`K = 1,\dots,5`$, and the $`K = 0`$ term is the constant $`w_0/7 = 1`$, so

```math
Q([u]) \;=\; 1 + w_6\,\frac{\lVert\rho_6(u)\rVert^2}{\lVert u\rVert^4} .
```

The ratio on the right is not constant on rays, so $`Q`$ determines $`w_6`$ as its slope against
that ratio: the weight derived in Section 5.3 belongs to the functional, not to the way it is
written.

### 5.3 The weight

> **Lemma 5.2.** $`\lVert R_6(P)\rVert^2 = d(7-d)/7`$, and $`\lVert R_0(P)\rVert^2 = d^2/7`$.

Three steps. First, $`\mathcal{M}_K`$ obeys a Parseval identity,
$`\sum_K \lVert \mathcal{M}_K(P)\rVert^2 = \lVert P\rVert_F^2`$ for any $`7\times 7`$ matrix $`P`$.
Second, $`P`$ is an orthogonal projector by the normalisation fixed in Section 2.4, so
$`\lVert P\rVert_F^2 = \mathrm{tr}\,P = d`$. Third, $`R_0(P)_0 = -\mathrm{tr}(P)/\sqrt{7}`$, so
$`\lVert R_0\rVert^2 = d^2/7`$. Lemma 4.1 removes every other term from the Parseval sum, leaving

```math
\lVert R_6 \rVert^2 \;=\; d - \frac{d^2}{7} \;=\; \frac{d(7-d)}{7} . \qquad \square
```

**This is where the second icosahedral input does its second job.** It has already entered, in
Section 5.1, where multiplicity one scalarised the right-index contraction; here the same branching
supplies the weight. The expression $`d(7-d)/7`$ is positive exactly when $`0 < d < 7`$, and Section
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

That $`R_K(P) = 0`$ for $`K = 1,\dots,5`$ is not a separate fact: $`P`$ is $`2I`$-invariant, so its
multipoles lie in $`(V_K)^{2I}`$, and Lemma 4.1 says those vanish.

### 5.4 The surviving operator, and the map it generates

Write $`\Lambda_m = (-1)^{3+m}\binom{6}{3+m}`$, the alternating sixth row of Pascal's triangle. At
weight states the frozen-density operator of Section 4.2 is an outer product,

```math
A_6(v_i)\, v_j \;=\; c\, \Lambda_i \Lambda_j\, v_j ,
\qquad
c \;=\; -\frac{1}{\binom{12}{6}}\sqrt{\frac{\dim V_3}{\dim V_6}} ,
```

diagonal in the second slot. Feeding the same state back in gives the cubic map, which carries
$`\Lambda`$ **squared**:

```math
M_6(v_i) \;=\; c\, \Lambda_i^2\, v_i ,
\qquad
\Lambda^2 \;=\; (1,\, 36,\, 225,\, 400,\, 225,\, 36,\, 1) .
```

The outer product belongs to the operator and the square to the map; they are different objects.

The two tensor factors of $`\Lambda\otimes\Lambda`$ have **different origins**, which is worth
recording because the alternation is the whole content. The multiplication slot alternates by
itself; the density slot does not, and takes its alternation from the phase in $`\Theta`$:

```math
\langle 3\,m;\, 3\,{-m} \mid 6\,0\rangle \;=\; \tfrac{\sqrt{231}}{462}\,(1,\,6,\,15,\,20,\,15,\,6,\,1) ,
\qquad
\langle 6\,0;\, 3\,m \mid 3\,m\rangle \;=\; \tfrac{\sqrt{429}}{858}\,\Lambda .
```

The first is strictly positive, in the fixed Condon-Shortley convention, and in closed form
$`\langle j\,m;\, j\,{-m}\mid 2j\,0\rangle = \frac{(2j)!}{\sqrt{(4j)!}}\binom{2j}{j+m}`$. So it is
not the case that both Clebsch-Gordan evaluations produce an alternating row. The density row comes
out with unsigned magnitudes and time reversal supplies its signs; the multiplication row displayed
above is already alternating. The two factors of $`\Lambda`$ therefore reach $`\Lambda^2`$ by
different routes, which is the point of the next paragraph.

What the alternation buys is that $`\Lambda`$ is a sixth finite difference:

```math
\sum_m \Lambda_m\, m^k \;=\; 0 \quad (k = 0,\dots,5) , \qquad \sum_m \Lambda_m\, m^6 \;=\; 720 .
```

The unsigned row annihilates no even moment, giving $`64, 96, 384`$ at $`k = 0, 2, 4`$. Both rows
are even in $`m`$, so both kill every odd moment by parity; that is a shared symmetry carrying no
information, and the separation is entirely in the even moments.

### 5.5 That $`M_6`$ is not radial, and the quartic

Clause 3 is one line from Section 5.4. By Section 5.2, radial and proportional to $`M_0`$ are the
same condition in $`\mathscr{E}_3`$, so suppose $`M_6 = \alpha M_0`$. Evaluating both at the weight
state $`v_i`$ gives $`c\,\Lambda_i^2 = -\alpha/\sqrt{7}`$ for every $`i`$, so $`\Lambda^2`$ would be
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
the pairing is $`(d/7)\,\langle u, \mathcal{N}(u)\rangle = A(u)`$, the $`d/7`$ being the block inner
product inherited from $`\int\lvert\psi\rvert^2 = (d/7)\lVert u\rVert^2`$. For a fixed sector
$`\sigma`$, $`t_0`$ and $`t_6`$ are constants determined by the right contractions, and they are not
assumed related. If $`t_6`$ vanished, the self-interaction would be $`t_0 M_0`$, so $`A(u)`$ would
be proportional to $`\langle u, M_0(u)\rangle = -\lVert u\rVert^4/\sqrt{7}`$, hence constant on the
unit sphere. It is not: by clause 5, $`\widetilde{Q} = (49/d^2)A`$ is
$`w_0/7 + w_6\lVert\rho_6\rVert^2`$ with $`w_6 > 0`$, and a positive multiple of $`A`$ is constant
only if $`A`$ is, and $`\lVert\rho_6\rVert^2`$ takes the values $`1/\binom{12}{6}`$ and
$`400/\binom{12}{6}`$ at $`v_3`$ and $`v_0`$. So $`t_6 \neq 0`$, and with clauses 1 and 2 that is
clause 4. $`\square`$

The same non-constancy appears on the quartic side as an identity worth recording,

```math
\binom{12}{6}\, \lVert \rho_6(v_m)\rVert^2 \;=\; \Lambda_m^2 ,
```

which is an identity rather than a sample: at a weight state $`\rho_6`$ has only its zonal
component, so $`\lVert\rho_6\rVert^2 = \binom{6}{3+m}^2/\binom{12}{6}`$. The $`\binom{12}{6}`$ here
is the same constant as in $`c`$ above and for the same reason, the normalisation of the stretched
Clebsch-Gordan coefficient, and the $`\Lambda^2`$ carried by the cubic map and the $`\Lambda^2`$
appearing here are one fact seen twice.

Both coefficients of the self-interaction are available, not only the nonvanishing of the second.
Pairing it with $`u`$ and evaluating at $`v_3`$ and $`v_0`$ gives two linear equations whose
solution, written $`\mathcal{N}`$ from here on, is

```math
\mathcal{N}(u) \;=\; \frac{d}{7}\lVert u\rVert^2 u \;-\; \frac{7-d}{\sqrt{91}}\, M_6(u) ,
```

the radial part carrying the expected sign. Solved from two states, it holds at the octahedral and
hexagonal rays as well, so it is determined rather than fitted.

Relating the two sides away from weight states is a separate identity:

```math
\nabla_{\bar u} \lVert \rho_K(u)\rVert^2 \;=\; c_K\, M_K(u) ,
\qquad
c_K \;=\; (-1)^{K+1}\, 2\sqrt{\frac{\dim V_K}{\dim V_3}} ,
```

so the quartic weight and the cubic weight differ by a fixed nonzero factor **per channel**, and it
is not the case that the same coefficient appears in both. Every $`c_K`$ is nonzero, so no channel
is lost this way. Section 9.5 obtains the same relationship structurally, as an equivariant
isomorphism from the invariant quartics onto $`\mathscr{E}_3`$; the identity here is that
correspondence written out rank by rank. The two are not interchangeable as stated: the $`M_K`$ are
seven vectors in a four-dimensional space and so are linearly dependent, and reading nonvanishing of
every $`c_K`$ as injectivity would need the spanning fact of Section 4.2, which is not used here.
This holds as an identity in $`u`$ and $`\bar u`$, carried as fourteen independent variables rather
than checked at finitely many states. Nothing in Theorem 5.1 depends on it: clause 3 comes from
$`\Lambda^2`$ and clause 4's bridge from the pairing argument above, neither of which needs a
per-channel gradient. It is stated here because the per-channel factor is easy to assume away.

One last calculation completes clause 4's second sentence, that on the unit sphere the tangential
critical problem is governed by $`M_6`$ alone. Since $`Q = A/B^2`$,

```math
\nabla_{\bar u} Q \;=\; \frac{1}{B^2}\nabla_{\bar u}A \;-\; \frac{2A}{B^3}\nabla_{\bar u}B ,
```

and $`B(u) = (d/7)\lVert u\rVert^2`$, so $`\nabla_{\bar u}B = (d/7)\,u`$ and the second term is
radial. The first is proportional to the projected self-interaction $`\mathcal{N}`$. Projecting onto
$`u^{\perp}`$,

```math
\Pi_{u^{\perp}} \nabla_{\bar u} Q \;\propto\; \Pi_{u^{\perp}} \mathcal{N}(u)
\qquad (\lVert u\rVert = 1) ,
```

so the denominator contributes only the radial, Lagrange-multiplier term. With clause 1 and $`M_0`$
radial, the tangential equation involves $`M_6`$ alone, and by the bridge above with a nonzero
coefficient. That is clause 4 in full, and none of it uses the per-channel identity.

### 5.6 The normalisation, and what it does not settle

The theorem is complete; one ceiling belongs here before the discussion, on the constant its weight
is built from. The sector normalisation is $`N = \binom{12}{6}/w_6`$, and Section 5.3 gives it in
closed form:

```math
N \;=\; \binom{12}{6}\,\frac{\dim V_6}{\dim V_3}\,\frac{d}{7-d}
\;=\; \binom{13}{6}\,\frac{d}{7-d} ,
\qquad 1287 \text{ at } d = 3 , \quad 2288 \text{ at } d = 4 .
```

The first form is canonical because it is what the derivation produces: the left Clebsch-Gordan
constant, times the Peter-Weyl dimension ratio, times the sector. The binomial identity
$`\binom{12}{6}\cdot 13/7 = \binom{13}{6}`$ is noticed afterwards and is not a new primitive.

Two ceilings belong here rather than in the discussion. First, an earlier form of this
normalisation, $`N = 143\,d^2`$, is **exactly correct on both sectors** and always will be, since
$`d(7-d) = 12`$ at $`d = 3`$ and $`d = 4`$. What the derivation shows is that it is not the
primitive form: the quadratic shape is a consequence of the two sectors being complementary in 7.
Second, and more sharply, $`d = 3`$ and $`d = 4`$ are the only values that occur, so **no
measurement inside this system separates the two formulas**. They agree on every available case. The
correction is carried entirely by the derivation above and has no empirical content of its own.
Agreement on every available case invites the assumption that the choice between the two formulas
was measured; it was not.

### 5.7 The spin-8 channel on the quotient

Section 4.3 left one question open, whether the spin-8 channel whose target slot exists in both
sectors actually carries a nonzero coefficient there. With Lemma 5.2 in hand it closes.

This section's tool is the unequal-degree form of Lemma 3.1. Without equal degree the statement
genuinely fails, and a two-line witness shows what replaces it: $`f = X^2`$ and $`g = X^3`$ have
$`J(f,g) = 0`$ and are not proportional, while $`f^{\deg g} = g^{\deg f} = X^6`$, which is the
weaker conclusion available at unequal degrees. The same Euler computation with degrees
$`m = \deg f`$ and $`n = \deg g`$ gives $`Y \cdot J(f,g) = n f_X g - m f g_X`$. Homogeneity alone
settles nothing here, since $`f^{n}`$ and $`g^{m}`$ both have degree $`mn`$ whatever $`J`$ does, and
a degree-zero homogeneous rational function need not be constant, as $`X/Y`$ shows. The vanishing is
used through the derivative instead:
$`\partial_X(f^{n}/g^{m}) = f^{\,n-1}(n f_X g - m f g_X)/g^{\,m+1}`$, which is zero when
$`J(f,g) = 0`$. So $`f^{n}/g^{m}`$ is independent of $`X`$, and being homogeneous of degree zero it
is constant, exactly as at equal degree in Section 3.2. Since $`\mathbb{C}[X,Y]`$ is a unique
factorisation domain, a proportionality $`f^{n} \propto g^{m}`$ constrains the root multisets: if
$`f`$ has a root of multiplicity $`\mu`$ then $`g`$ has the same root with multiplicity $`\mu n/m`$.
The witness above checks it: $`f = X^2`$ has a double root and $`g = X^3`$ a triple one, and
$`\mu n/m = 2\cdot 3/2 = 3`$.

The right-hand factor of the level-16 output is built from $`R_6(P)`$, which lies in $`(V_6)^{2I}`$.
That space is one-dimensional by Section 2.4, and its generator has **twelve simple roots**, which
the orbit structure forces and the picture only suggests. The zero divisor of a $`2I`$-invariant
binary form is $`2I`$-invariant, hence a union of orbits of $`A_5`$ on $`\mathbb{P}^1`$, and those
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
$`\eta`$ leaves the right-hand factor nonzero in both sectors. One sector suffices for the norm:
$`P_{\mathbf{3}'} + P_{\mathbf{4}} = I`$ and $`\mathcal{M}_6(I) = 0`$, so
$`R_6(P_{\mathbf{3}'}) = -R_6(P_{\mathbf{4}})`$ and the two norms are equal for that reason rather
than by separate computation. The left-hand factor is $`[\rho_6(u)\otimes u]_8`$. Since
$`\dim\mathscr{E}_8 = 1`$ leaves no other equivariant map, it is *some* multiple of
$`\mathcal{C}(u)`$, say $`\alpha\,\mathcal{C}(u)`$; that $`\mathcal{C}`$ is itself nonzero does not
yet make $`\alpha`$ nonzero, so the constant is evaluated rather than inferred. At $`u = v_3`$,
$`\rho_6(v_3) = -\tfrac{\sqrt{231}}{462}\,v^{(6)}_0`$ and coupling to spin 8 gives
$`[\rho_6(v_3)\otimes v_3]_{8,3} = \tfrac{\sqrt{273}}{1092} \neq 0`$. Hence $`\alpha \neq 0`$. The
level-16 component of the nonlinearity therefore does not vanish identically, and Proposition 3.3
becomes a statement about $`X`$ rather than an ambient one:

> Among block states at level 6, those whose cubic nonlinearity has no level-16 component are
> exactly the time-reversal-invariant ones.

That also settles what Section 3 is doing in this paper. It is not an independent note sharing a
state space, and not merely the same weight count at a second target: the ambient proposition
describes a channel that the quotient leaves open, and the states it distinguishes are states of
$`X`$.

### 5.9 Three corollaries

Theorem 5.1 is a statement about one level and one interaction. Three consequences follow from it
using the same representation-theoretic machinery, and they bracket it from below, across and above.
They are not free: the first needs a character computation the theorem did not, and a rank-zero
evaluation at general spin. Throughout this subsection write

```math
\widehat{r}_6([u]) \;:=\; \frac{\lVert\rho_6(u)\rVert^2}{\lVert u\rVert^4} ,
```

which is the projective form of the top multipole and agrees with $`\lVert\rho_6\rVert^2`$ on the
unit sphere of $`V_3`$. The distinction matters in the third corollary, where the normalisation
imposed is on the section and not on the fibre representative.

> **Corollary 5.4.** *Nothing projective below level 6.* For a single-sector block state with the
> density-type interaction of Section 2.5, the projected self-interaction is radial at every
> level $`\ell < 6`$. Level 6 is the first level at which $`S^3/2I`$ permits a non-radial cubic
> self-interaction at all.

Two pieces of notation first, since the statement ranges over levels and Section 2.3 fixed its
transform on $`V_3`$ alone. Replacing $`3`$ by $`j`$ there is not quite enough: the sign
$`(-1)^{n'}`$ inside $`\mathcal{M}_K`$ is real only at integer $`n'`$. Write instead

```math
\mathcal{M}^{(j)}_K(P)_N \;=\; \sum_{n+n' = N}
\langle j\,n;\, j\,n' \mid K\,N \rangle \;
\varepsilon_j\,(-1)^{\,j+n'}\, P_{n,\,-n'} ,
```

with $`\rho^{(j)}_K`$ and $`M^{(j)}_K`$ built from it as in Section 2.3, and write the time-reversal
phase as

```math
\Theta_j v_m \;=\; \varepsilon_j\,(-1)^{\,j-m}\, v_{-m} ,
\qquad \lvert\varepsilon_j\rvert = 1 ,
```

which is defined at every $`j`$, integer or half-integer, because $`j - m`$ is an integer in both
cases. The exponent $`m`$ used in Section 2.2 is not, which is why the convention is written this
way here. As there, $`\varepsilon_j`$ is a free global phase and only the $`m`$-dependence is
forced; Section 2.2's choice at $`j = 3`$ is $`\varepsilon_3 = -1`$, since $`(-1)^m = -(-1)^{3-m}`$.

Below level 6 the restriction $`V_j\vert_{2I}`$ is irreducible: the character sum gives
$`\langle\chi,\chi\rangle = 1`$ at $`2j = 1,\dots,5`$ and first gives 2 at $`2j = 6`$, where the
restriction becomes $`\mathbf{3}' \oplus \mathbf{4}`$. So at every level below 6 the sector fills
$`V_j`$ and its isotypic projector is the identity. The identity is invariant under all of
$`\mathrm{SU}(2)`$, not merely under $`2I`$, so $`\mathcal{M}_K(I)`$ is an
$`\mathrm{SU}(2)`$-invariant vector in $`V_K`$ and vanishes for every $`K > 0`$. The Peter-Weyl
factorisation of Section 5.2 therefore retains the $`K = 0`$ term alone.

That term is radial. The rank-zero map is equivariant and built from one state, so by Schur it is a
multiple of $`\lVert u\rVert^2 u`$, and carrying the Clebsch-Gordan evaluation through gives

```math
M^{(j)}_0(u) \;=\; \frac{\varepsilon_j}{\sqrt{2j+1}}\,
\lVert u\rVert^2 u .
```

The scalar has modulus $`(2j+1)^{-1/2}`$ at every level and its phase is carried by the convention,
so only the modulus is a fact about the map. At $`j = 3`$ with $`\varepsilon_3 = -1`$ this is
$`-1/\sqrt{7}`$, which is Section 5.2's constant, and the two statements agree. None of that is
needed below: what matters is that the scalar is nonzero, so the projected self-interaction is a
multiple of the state and no projective direction is selected. $`\square`$

The argument covers half-integer $`j`$ as readily as integer $`j`$: the character sum does not care,
and the phase above is defined there, so levels 1, 3 and 5 are covered on the same footing as 2 and
4. Those are the levels whose sectors are the spinorial representations of $`2I`$, which do not
factor through $`A_5`$; nothing in the argument needed them to. Separately, it does not invoke the
Molien row at all: the vanishing is Schur's lemma applied to the identity, not the icosahedral
invariant gap. The gap is what makes level 6 interesting, but it is not what makes the levels below
it radial. The conclusion is not the empty one that there was nothing to select from. A level-$`2j`$
density carries every rank $`0 \le K \le 2j`$ and, at a generic state, carries them all
nontrivially; what removes them is the right factor, not an absent left one. The negative reading is
the more useful one: this interaction cannot supply shape selection to any level below 6, so a
lower-level slot that needs a preferred direction has to get it from somewhere else.

This does not compete with Section 8.1's remark that level 6 is fixed by the choice of object rather
than by the geometry. Which level one studies is fixed by putting the left index in $`V_3`$. What
the corollary adds is independent of that choice: below level 6 there would have been nothing
projective to study.

> **Corollary 5.5.** *The two sectors select the same shapes.* The reduced quartics of the two
> sectors have the same critical set on $`\mathbb{P}(V_3)`$, with the same ordering of values.

By clause 5, $`Q_d([u]) = w_0/7 + w_6(d)\,\widehat{r}_6([u]) = 1 + w_6(d)\,\widehat{r}_6([u])`$,
since $`w_0 = 7`$ in both sectors. The two quartics are therefore the same increasing affine
function of $`\widehat{r}_6`$ up to the positive slope $`w_6(d)`$, and an increasing affine
reparameterisation moves neither the critical set nor the order of the values on it. Hence

```math
\mathrm{Crit}\, Q_{\mathbf{3}'} \;=\; \mathrm{Crit}\, Q_{\mathbf{4}} .
```

So once the filter has selected rank 6, the shape problem stops being icosahedral and becomes a
question about spin 3 with time reversal, which is why Section 7.1 could be carried out without the
group appearing again. The consequence worth recording is negative: at leading cubic order this
interaction cannot make one sector prefer a different configuration from the other. Whatever
distinguishes the two sectors, it is not the projective shape their self-interaction selects.

> **Corollary 5.6.** *But their nonlinear shifts differ.* Let $`[u]`$ be a critical ray and let
> $`\psi`$ be the corresponding block state normalised so that $`\int_X \lvert\psi\rvert^2 = 1`$.
> Then the projected self-interaction acts on $`\psi`$ by the scalar $`Q_d([u])`$, and
> $`Q_{\mathbf{3}'} - Q_{\mathbf{4}} = \tfrac{49}{156}\,\widehat{r}_6([u])`$.

At a critical ray the tangential part vanishes, so $`\mathcal{N}(\psi) = \beta\psi`$ for some scalar
$`\beta`$. Pairing with $`\psi`$ and using that the block projection is self-adjoint with $`\psi`$
in its range gives $`\beta \int\lvert\psi\rvert^2 = \int\lvert\psi\rvert^4`$, so with the stated
normalisation $`\beta = \int\lvert\psi\rvert^4 = Q_d([u])`$. The difference is then
$`(28/39 - 21/52)\,\widehat{r}_6 = \tfrac{49}{156}\,\widehat{r}_6`$. $`\square`$

The normalisation is the whole content of the statement and is easy to lose. Imposing
$`\lVert u\rVert = 1`$ on the fibre instead gives a coefficient
$`d/7 + \tfrac{7-d}{13}\lVert\rho_6\rVert^2`$ whose leading term is an artefact of
$`B(u) = (d/7)\lVert u\rVert^2`$. Normalising the section removes that term, and what survives is
$`w_6`$, which Section 5.3 derived. The two shifts agree only where $`\widehat{r}_6 = 0`$, so they
differ at every ray whose top multipole is nonzero, the four tabulated ones included.

Taken together the three say: nothing projective below level 6, one projective channel at level 6,
and above it two sectors that agree about shape and disagree about scale. None of the three needs
the range equation, and none of them is a statement about solutions; they are statements about the
leading reduced problem, on the same footing as Theorem 5.1 itself.

---

## 6. The selected point

Theorem 5.1 places the self-interaction on a single projective ray of the four-dimensional family of
Section 4.2, which that section identifies with the four-channel spin-3 interaction of the
condensate literature [DH], [KU]. What remains is to say where in that family the ray lies. The
answer is one point, and at that point the quartic of Theorem 5.1 is exactly an affine image of a
mean-field energy the condensate literature has already studied. Nothing icosahedral enters
here: the quotient did its work in Theorem 5.1, and everything below is spin 3.

### 6.1 The point

For $`u \in V_3`$ write $`f(u) = \langle u, F u\rangle \in \mathbb{R}^3`$ for its spin density, with
$`F = (F_x, F_y, F_z)`$ the spin-3 generators, and keep the holomorphic squares
$`B_J(u) = [u \otimes u]_J`$ of Section 2.3. The pair amplitudes of [KU] are $`\sqrt{7}\,B_J`$, so in
the present notation their spin-3 mean-field energy reads, up to an additive constant,

```math
\widetilde{E}(u) \;=\; c_\gamma\,\lvert f\rvert^2 \;+\; 7c_\alpha\,\lVert B_0\rVert^2 \;+\; 7c_\beta\,\lVert B_2\rVert^2 ,
```

with the three couplings fixed combinations of the four scattering lengths.

> **Proposition 6.1** (the selected point)**.** On the unit sphere of $`V_3`$,
>
> ```math
> \widehat{r}_6 \;=\; \frac{64 + 7\,\widetilde{E}}{924}
> \qquad\text{at}\qquad (c_\gamma, c_\alpha, c_\beta) = (-1,\, 32,\, 12) .
> ```

*Proof.* Multiplied by $`\lVert u\rVert^4`$, both sides are real quartics of bidegree $`(2,2)`$ in
$`(u, \bar u)`$, invariant under $`\mathrm{U}(1) \times \mathrm{SU}(2)`$. Polynomials of bidegree
$`(2,2)`$ are $`\mathrm{Sym}^2 V_3^{*} \otimes \mathrm{Sym}^2 \overline{V}_3^{*}`$, that is, sesquilinear
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
$`924\,\lVert\rho_6\rVert^2 = \binom{6}{3+m}^2`$, the values $`1, 36, 225, 400`$ (Section 5.5), and at
$`(c_\gamma, c_\alpha, c_\beta) = (-1, 32, 12)`$ the right-hand side gives
$`64 - 63`$, $`64 - 28`$, $`64 + 161`$ and $`64 + 336`$, the same four numbers. $`\square`$

The same identity reads $`\widehat{r}_6 = (64 - 7\widetilde{E})/924`$ at the opposite point
$`(1, -32, -12)`$, since $`\widetilde{E}`$ is linear in the couplings. The values at the weight
states agree with the energies [KU] tabulate for their inert states.

### 6.2 The two signs, and where the literature places them

The equation of Section 2.5 is the Euler-Lagrange equation of an energy whose quartic term is a
positive multiple of $`g\int\lvert\psi\rvert^4`$, Section 2.5 fixes $`g = 1`$, and clause 5 of
Theorem 5.1 makes the quartic an increasing affine function of $`\widehat{r}_6`$, since $`w_6 > 0`$
(Section 5.5). So at the paper's normalisation the reduced energy increases with $`\widehat{r}_6`$.
By Proposition 6.1 it then increases with $`\widetilde{E}`$ at $`(-1, 32, 12)`$: at the paper's
normalisation, the selected interaction is the condensate energy at that point, and the opposite
normalisation, $`g = -1`$, is the point $`(1, -32, -12)`$. Write $`(n_-, n_0, n_+)`$ for the
signature of the second variation of $`\widehat{r}_6`$ at a critical ray, the numbers of its
negative, zero and positive eigenvalues. The critical rays, their values of $`\widehat{r}_6`$ and
these signatures do not depend on the sign. The Morse index of each ray as a critical point of the
energy does, being $`n_-`$ at $`g = 1`$ and $`n_+`$ at $`g = -1`$, and so does which ray carries the
least energy. Section 7 gives the indices at both signs.

[KU] also draw the spin-3 phase diagram, determined by comparing the energies of their
symmetry-classified states and by solving the stationary equation directly. In the coordinates of
their second diagram, the form $`\tilde c_1 \lvert f\rvert^2 + \tilde c_2 \lVert B_0\rVert^2 +
\tilde c_3\,\mathrm{Tr}\,\mathcal{N}^2`$, where their $`A_{00}`$ is the present $`B_0`$ and
$`\mathcal{N}_{\mu\nu} = \mathrm{Re}\,\langle u, F_\mu F_\nu u\rangle`$ is the nematic tensor, of trace
12 on the unit sphere, the paper's point lies
at $`(\tilde c_3/\lvert\tilde c_1\rvert,\, \tilde c_2/\lvert\tilde c_1\rvert) = (1/9,\, 14)`$ with
$`\tilde c_1 < 0`$, inside the ferromagnetic phase FF and near its boundary with the phase F. The
opposite point lies at $`(-1/9,\, -14)`$ with $`\tilde c_1 > 0`$, well inside the phase [KU] call A,
whose state is the hexagon $`(v_3 + v_{-3})/\sqrt{2}`$. Thus the two states that Section 7.3
identifies exactly as the ends of $`\widehat{r}_6`$ already occur in the literature as the
numerically determined ground states at the two signs: the coherent state at the paper's sign and
the hexagon at the other. That placement is numerical and it is [KU]'s. Section 7.3 gives
the exact statement about both ends.

### 6.3 What the identity is, and what it is not

It is an identity: the two sides are one function in two coordinate systems. The ten census orbits of
Section 7 are therefore represented among [KU]'s stationary-state families, with the same values,
and Section 7 identifies them one by one. That is not corroboration of anything, and it should not be
read as such.

The point is where the density interaction of Section 2.5 lands under the quotient's selection.
Nothing here says it is the coupling of a physical condensate, and no claim is made about chromium
or any other spin-3 atom.

What the literature has at the point, and what it does not, is where the rest of the paper does its
work. [KU] and [BTD07] give stationary states and locate the ground state numerically. They do not
claim to list every critical point on each symmetry-fixed set: [KU]'s procedure computes the minimum
of the energy on each such set, and it excludes by construction states with no symmetry at all.
Section 7 classifies every critical orbit within a stated symmetry class, and at each sign two of
those orbits are maxima of the energy on their own fixed lines, which a procedure that minimises on
each set does not return. Recognising a configuration is not selecting it, as Section 9.2 puts it,
and knowing the phases is not classifying the critical geometry.

---

## 7. The critical geometry at the point

Section 6 placed the quartic at one point of the four-channel family. This section describes its
critical set there: the critical rays of $`\widehat{r}_6`$ on $`\mathbb{P}(V_3)`$, with their values
and their signatures, which by Section 6.2 give the Morse indices of the reduced energy at both
signs. Nothing in it uses $`2I`$. Its parts carry different standing, and each says which. Section
7.1 derives six critical rays by symmetry, exactly. Section 7.2 reports a census of every critical
orbit within a symmetry class, an audited argument reproduced blind [M8.12], and certifies three
further orbits outside that class. Section 7.3 proves the two ends.

### 7.1 Six rays found by symmetry

By clause 5 of Theorem 5.1 the reduced quartic is an increasing affine function of
$`\widehat{r}_6`$ (Section 6.2), so its critical rays are those of $`\widehat{r}_6`$ on
$`\mathbb{P}(V_3)`$. On the unit sphere $`\widehat{r}_6 = \lVert\rho_6\rVert^2`$, and this subsection
computes with the latter. The question is about spin 3 with time reversal, and it does not mention
$`2I`$. Four values, with $`\binom{12}{6}\lVert\rho_6\rVert^2 = 924\,\lVert\rho_6\rVert^2`$ quoted as
an integer:

| ray | constellation | [KU] | $`924\,\lVert\rho_6\rVert^2`$ |
|---|---|---|---|
| $`v_3`$ | coherent, six coincident points | FF | 1 |
| $`v_0`$ | zonal | Q | 400 |
| $`(v_2 + v_{-2})/\sqrt{2}`$ | octahedron | D | 288 |
| $`(v_3 + v_{-3})/\sqrt{2}`$ | hexagon | A | 463 |

The [KU] column names the state of [KU]'s Table II whose order parameter is that ray, up to rotation
and phase; through Proposition 6.1 their energy for it gives the value in the last column. Those four
rays are critical, which the table alone does not show.

> **Lemma 7.1.** Each of the four rays above is a critical point of $`\lVert\rho_6\rVert^2`$ on the
> unit sphere.

Let $`H`$ be the stabiliser of $`[u]`$ in $`\mathrm{SO}(3)`$, acting on $`u`$ by a character
$`\chi`$. Since $`\lVert\rho_6\rVert^2`$ is $`\mathrm{SO}(3)`$-invariant its gradient is
equivariant, so the tangential gradient at $`[u]`$ lies in the $`H`$-fixed part of the projective
tangent space, which is $`\mathrm{Hom}_H(\chi, V_3)`$ modulo $`\mathbb{C}u`$. For each of the four
rays that quotient is zero, because the $`\chi`$-isotypic subspace of $`V_3`$ is one-dimensional and
$`u`$ already spans it. Hence the tangential gradient vanishes. $`\square`$

For the two weight states the cyclic group of rotations about the quantisation axis suffices: the
projective tangent weights are $`\pm 1, \pm 2, \pm 3`$ at $`[v_0]`$ and $`-1, \dots, -6`$ at
$`[v_3]`$, and none of them is zero. For the octahedral ray a subgroup of order 8 already isolates
it, and for the hexagonal ray the dihedral group of order 12 does. No orientation is assumed: in
each case the stabiliser is computed rather than posited.

Two further critical rays do not appear in that table. Each lies on a fixed locus of dimension one
rather than at an isolated fixed point, so Lemma 7.1 does not cover them as stated, and a second
lemma does.

> **Lemma 7.2.** Suppose the $`\chi`$-isotypic space of $`H`$ is two-dimensional, so the fixed
> locus is a projective line. If $`\lVert\rho_6\rVert^2`$ is stationary along a real curve in that
> line and a further symmetry makes it even in the transverse coordinate, the ray is critical.

The transverse derivative vanishes by that evenness, and those two real directions exhaust the
tangential fixed space, so the whole tangential gradient vanishes. Both rays below satisfy it, and
both can be checked against the relation

```math
\langle u, M_6(u)\rangle \;=\; \frac{2}{c_6}\,\lVert\rho_6\rVert^2 \;=\; -\frac{\sqrt{91}}{13}\,\lVert\rho_6\rVert^2 ,
```

which follows from the gradient identity by Euler and holds at every state, critical or not. Where
$`M_6(u) = \lambda u`$ the constant is therefore read off the value rather than quoted beside it.

The **pentagonal pyramid**. On the line $`u = \cos t\, v_2 + \sin t\, v_{-3}`$,

```math
\lVert\rho_6\rVert^2 \;=\; -\tfrac{125}{132}\sin^4 t \;+\; \tfrac{10}{11}\sin^2 t \;+\; \tfrac{3}{77} ,
```

stationary in the interior at $`\sin^2 t = 12/25`$, where $`\lVert\rho_6\rVert^2 = 9/35`$ and
$`\binom{12}{6}\lVert\rho_6\rVert^2 = 1188/5`$, the first such value that is not an integer. The
rotations of order 5 about the quantisation axis act on $`\mathrm{span}\{v_2, v_{-3}\}`$ by a single
character, so that line is a fixed locus. Rotation about the same axis carries the line to itself
and advances the relative phase of the two components at five times its own angle, so
$`\lVert\rho_6\rVert^2`$ is constant transverse to the real curve and Lemma 7.2 applies along it;
the criterion confirms it, with $`M_6(u) = -\tfrac{9}{455}\sqrt{91}\,u`$. Its Majorana polynomial is
$`z(a + bz^5)`$ with $`a, b \neq 0`$, so the constellation is one point at a pole and five in a
ring, six distinct points: a non-degenerate pentagonal pyramid. The endpoints $`t = 0`$ and
$`t = \pi/2`$ are stationary too, but they are the weight states $`v_2`$ and $`v_{-3}`$,
critical by the argument of Lemma 7.1; the interior point is the one this line contributes.

In [KU]'s Table II the pyramid is state H, whose parameter takes the value $`\eta = 2/5`$ at the
point. It shares its value with a second orbit, the C3 ray of Section 7.2, which is their state I, at
$`\eta = -2/5`$. [KU]'s energies for H and I are one function of the couplings, so the two states are
degenerate wherever both exist, as [KU] note, and [BTD07] report the second as a state degenerate
with H. Section 7.2 separates the two orbits.

The **trigonal prism**, and with it the octahedron. Take
$`H = \langle R_z(2\pi/3), R_x(\pi)\rangle \cong D_3`$, with $`R_x`$ the in-plane axis through a
vertex column: it acts by $`-1`$ on both $`v_3 + v_{-3}`$ and $`v_0`$, so the $`\chi`$-isotypic
space is $`\mathrm{span}\{v_3+v_{-3},\, v_0\}`$ and the fixed locus is the projective line
$`\mathbb{P}\,\mathrm{span}\{v_3+v_{-3},\, v_0\}`$. A second family of in-plane axes, turned by
$`30^\circ`$ from these, acts by $`+1`$ on $`v_3+v_{-3}`$ and does not fix this line. The
distinction is easy to state wrongly. With three columns, the line through one of them runs between
the other two on the far side, so *through a column* and *between two columns* pick out the same
three lines; what separates the two families is the $`30^\circ`$ turn, and they give opposite
answers. The chart $`u = v_3 + z\,v_0 + v_{-3}`$ covers that line except at one point, the zonal ray
$`[v_0]`$ at $`z = \infty`$, which is treated below. On the chart, writing $`z = x + iy`$,

```math
\lVert\rho_6\rVert^2 \;=\; \frac{100\lvert z\rvert^4 - 20x^2 + 148y^2 + 463}{231\,(\lvert z\rvert^2+2)^2} ,
```

whose critical set on the chart is five points: $`z = 0`$, the hexagon at $`463/924`$;
$`z = \pm\sqrt{23/10}`$, where $`\lVert\rho_6\rVert^2 = 200/903`$ and
$`\binom{12}{6}\lVert\rho_6\rVert^2 = 8800/43`$; and $`z = \pm i\sqrt{5/2}`$, where the value is
$`24/77`$. The expression is even in each of $`x`$ and $`y`$ separately, so each is stationary in
both directions and Lemma 7.2 applies along either axis. The rotation $`R_z(\pi/3)`$ acts on the
chart by $`z \mapsto -z`$, so the two signs in each pair are one orbit and the five points are three
orbits.

The point the chart omits is critical as well, and it is not a new ray. It lies on this locus
because $`v_0`$ spans one of the two $`\chi`$-isotypic directions, and it is critical by Lemma 7.1,
which already covers it: it is the zonal ray of the table above, at
$`\lVert\rho_6\rVert^2 = 100/231`$, that is $`400/924`$. The reason to argue it that way rather than
by differentiating in the complementary chart is that the derivative there settles nothing. Since
$`v_0`$ is critical on the whole sphere, the gradient vanishes along every line through it,
including lines that have nothing to do with $`D_3`$. Counting both charts, the locus carries six
critical points in four orbits, and the hexagon's $`463/924`$ is the largest value on it.

The real axis carries the eclipsed pairs of triangles, Majorana polynomial $`z^6 - sz^3 + 1`$ with
$`s = \sqrt{20}\,x`$ real, and the imaginary axis the staggered ones, where $`s`$ is purely
imaginary. No rotation relates the two: a rotation preserves shape, and these families are not
congruent. What $`R_z(\pi/6)`$ does is carry this line to the other $`\chi`$-isotypic line
$`\mathrm{span}\{v_3-v_{-3},\, v_0\}`$, which is the same fact as its conjugating the $`-1`$ family
of axes onto the $`+1`$ family: applied to a prism it returns a prism, turned by $`30^\circ`$, which
on a configuration with a three-fold axis is indistinguishable from a turn of $`90^\circ`$ the other
way. Both rays are identified exactly, and the quadratic does it. In $`w = z^3`$ the Majorana
polynomial is $`w^2 - sw + 1`$, whose two roots multiply to $`1`$, so the triangles sit at
reciprocal radii; since $`\lvert z\rvert \mapsto 1/\lvert z\rvert`$ sends $`\theta`$ to
$`\pi - \theta`$, they sit at heights $`\pm h`$ for a common $`h`$ whatever $`s`$ is. The argument
of $`w`$ separates the two axes. At $`x^2 = 23/10`$, $`s = \sqrt{46}`$ and both roots are real and
positive, so $`\arg w = 0`$ and each triangle has vertices at azimuths
$`0^\circ, 120^\circ, 240^\circ`$: the two are **aligned**, which makes the ray a **trigonal prism**
and not an antiprism, at heights $`\pm 0.5585\ldots`$. It is [KU]'s state E, at
$`\eta = 3/43`$. At $`y^2 = 5/2`$, $`s = i\sqrt{50}`$ and the two roots are purely imaginary of
opposite sign, with arguments $`+\pi/2`$ and $`-\pi/2`$; dividing the difference of $`\pi`$ by three,
the azimuths differ by $`60^\circ`$: the two are **staggered**, and there $`h = 1/\sqrt{3}`$ exactly.
A staggered pair of equilateral triangles at heights $`\pm 1/\sqrt{3}`$ is the **regular
octahedron**, which is the same statement as its full multipole row there,
$`1/7, 0, 0, 0, 6/11, 0, 24/77`$. Its reappearance is a check rather than a coincidence: an
octahedron has a three-fold axis through opposite faces, so it has to occur in this locus. The
tabulated state is exact by the same standard, with no root-finding: its sextic is a constant times
$`z(z^4+1)`$, of degree 5, so one root sits at the far pole, one at the origin and four at the
fourth roots of $`-1`$, spaced $`90^\circ`$ apart on the equator. Figure 2 draws the four shapes.

<img src="https://github.com/dmobius3/mode-identity-theory/blob/main/files/assets/majorana-constellations.png?raw=true" width="90%" alt="Majorana constellations on the unit sphere: a hexagon on the equator, an octahedron, a pentagonal pyramid and a trigonal prism, each labelled with its value of the rank-6 multipole norm">

**Figure 2.** Majorana constellations of the four six-vertex shapes among the critical rays of Section 7.1, each drawn on the unit sphere with its value of $`\lVert\rho_6\rVert^2`$: the hexagon $`(v_3 + v_{-3})/\sqrt{2}`$, the octahedron $`(v_2 + v_{-2})/\sqrt{2}`$, the pentagonal pyramid on the line $`\cos t\, v_2 + \sin t\, v_{-3}`$ at $`\sin^2 t = 12/25`$, and the trigonal prism $`v_3 + \sqrt{23/10}\, v_0 + v_{-3}`$, whose two triangles are aligned. Filled points face the viewer, and dashed edges are hidden.

The hexagonal value is the largest of the four, and it is not this paper's. Romero, Klimov,
Goldberg, Leuchs and Sánchez-Soto give the closed form
$`\varrho^2_{2S} = \tfrac12 + \binom{4S}{2S}^{-1}`$ for the top multipole of the NOON state at
integer spin $`S`$ [RK]; at $`S = 3`$ that is $`463/924`$, and their NOON state is this paper's
hexagon up to a rotation. Their normalisation is the Parseval one used here, so the numbers are
directly comparable.

The question of whether it is the global maximum of $`\lVert\rho_6\rVert^2`$ is also theirs, and
they pose it for general $`S`$: they ask what the largest attainable highest-order multipole is,
sample $`6 \times 10^4`$ random constellations, and find none exceeding the NOON value. The table
does not settle it, since four exact values do not determine a global extremum; at spin 3, Section
7.3 does. What this subsection adds at that ray is not the value but its position: it is one point
of an exactly determined critical set on each of two symmetry loci. The three
time-reversal-invariant rays among them are the zonal, octahedral and hexagonal ones, and by Lemma
2.2 their odd density multipoles vanish, which is visible in the octahedral case as anticoherence of
order exactly 3: its multipoles are $`1/7, 0, 0, 0, 6/11, 0, 24/77`$, so ranks 1, 2 and 3 vanish and
rank 4 does not. [KU] list the same three, Q, D and A, as the only time-reversal-invariant states of
their table.

### 7.2 The census, and three orbits outside its class

Lemmas 7.1 and 7.2 are cases of one principle. For a closed subgroup $`H`$ of $`\mathrm{SO}(3)`$ and
a character $`\chi`$ of $`H`$, the vectors $`u`$ with $`D(h)u = \chi(h)\,u`$ for every $`h \in H`$
form a subspace $`V_3^{(H,\chi)}`$, the fixed space of a group of symmetries of $`\widehat{r}_6`$,
each $`h`$ acting together with the phase $`\chi(h)^{-1}`$. By Palais' principle of symmetric
criticality, a critical point of $`\widehat{r}_6`$ restricted to its projectivisation is critical on
$`\mathbb{P}(V_3)`$. Lemma 7.1 is the case in which that projectivisation is a point, and Lemma 7.2
a case in which it is a line.

**The census.** Take every such locus of projective dimension at most one, and every critical point
on it. There are six loci that are points and seven that are lines; the complete critical set on
each line is found by elimination, not by a numerical solver; and the union, modulo rotation and
phase, is exactly ten orbits [M8.12]. At each orbit the signature $`(n_-, n_0, n_+)`$ of the second
variation of $`\widehat{r}_6`$ is computed exactly, from its characteristic polynomial, on the space
transverse to the phase and rotation directions, of dimension 10 at the weight states and 9
elsewhere. The census was pre-registered by the author, then derived again from the definitions
alone, offline, in two independent rooms; an adversarial audit graded the classification, the
completeness on each locus, the criticality and the second-variation formula sound in both rooms,
and the orbits, values and signatures were reproduced in both rooms and by the audit [M8.12]. It is
an audited argument, and it stands here as one.

Two notions of symmetry appear in the tables, and both are given for every orbit. The *rotation
stabiliser* is the stabiliser of the ray in $`\mathrm{SO}(3)`$. The *full isotropy* is the stabiliser
of the vector in the group generated by $`\mathrm{U}(1) \times \mathrm{SO}(3)`$ and time reversal
$`\Theta`$: rotations and antiunitary maps $`\Theta \circ R`$, each with the phase that lifts it. The tables print
it as a point group. Forgetting the phases maps it isomorphically onto the symmetry group of the
constellation in $`\mathrm{O}(3)`$: $`\Theta`$ acts on constellations as the antipodal map (Section
3.4), and a ray is determined by its constellation, so $`\Theta \circ R`$ fixes the ray exactly when
the improper rotation $`-R`$ fixes the six points. For the prism, the pyramid and the D2 ray the full
isotropy is certified at the point by the machinery described below. The other seven constellations
are explicit, and their point groups follow from them directly: points at the poles with their
multiplicities for the four weight states, the regular octahedron and hexagon, and for the C3 ray one
point at one pole, two at the other and three on a ring between. In every row the point group agrees
with the isotropy group [KU] list, once their generators are translated this way.

| orbit | $`924\,\widehat{r}_6`$ | rotation stabiliser | full isotropy | [KU] | $`(n_-, n_0, n_+)`$ |
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
at $`g = -1`$ (Section 6.2). The names C3 ray and D2 ray come from the census's loci, and so from
rotation stabilisers; the full symmetry of the D2 ray is $`D_{2d}`$.

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
$`\mathcal{O}_1, \mathcal{O}_2, \mathcal{O}_3`$, in increasing order of value. This paper
certifies them using 60-digit interval arithmetic, with $`\widehat{r}_6`$ in the form of Lemma 7.3
and nothing from the searches but the numerical states.

- *Each is a critical orbit.* It is certified inside the fixed set of its full isotropy group, a real
  subspace of $`V_3`$, as a zero of the critical-point system of $`\widehat{r}_6`$ on the unit sphere of
  that subspace, with a linear slice fixing each continuous symmetry that preserves it: none for
  $`\mathcal{O}_1`$ and $`\mathcal{O}_3`$, one rotation for $`\mathcal{O}_2`$. The Krawczyk operator
  maps a box of radius $`10^{-55}`$ around the computed zero into its own interior, so the box holds
  exactly one zero, and the system's Jacobian is nonsingular throughout it. The slice multiplier
  vanishes: pairing the equation with the symmetry direction leaves only the multiplier times that
  direction's squared length, since the gradient and the sphere's normal are both orthogonal to it,
  and the direction is nonzero, or the Jacobian would be singular. So the zero is critical on the
  fixed set, and by symmetric criticality on all of $`\mathbb{P}(V_3)`$.
- *Its full isotropy is certified.* From below, the group fixes the certified point, which lies in its
  fixed set. From above, the six Majorana points of the same box are enclosed in disjoint boxes; a
  symmetry must permute them and preserve every pairwise distance, and the permutations that pass that
  test, with the sign of a determinant separating proper from improper, number exactly the group's
  order.
- *Its signatures are certified.* Over the same box, the bordered second variation is congruent to a
  matrix each of whose Gershgorin discs avoids zero, which fixes its inertia, and with it the
  signature, by Sylvester's law: on the whole sphere, where the critical point has the same Lagrange
  multiplier, and on each fixed set modulo the continuous symmetries that preserve it. In particular
  the transverse second variation has no kernel.

Every entry of a row of the table below is computed at that one certified point. The same machinery
reproduces the census's exact full signatures at the pyramid, the prism and the D2 ray from their own
fixed sets, and at all six of its orbits with finite stabilisers from the whole sphere, and the tests
were run beside planted failures, which they caught. The certificates section at the end of the paper
gives the scripts, their logs and their hashes.

| orbit | $`924\,\widehat{r}_6`$ | rotation stabiliser | full isotropy | $`(n_-, n_0, n_+)`$ | on the isotropy fixed set | on the $`C_2`$ fixed set |
|---|---|---|---|---|---|---|
| $`\mathcal{O}_1`$ | 215.7757925… | $`C_2`$ | $`C_{2v}`$ | (4, 0, 5) | (1, 0, 2) | (2, 0, 3) |
| $`\mathcal{O}_2`$ | 238.0165289… | $`C_1`$ | $`C_s`$ | (6, 0, 3) | (4, 0, 1) | n/a |
| $`\mathcal{O}_3`$ | 238.3568547… | $`C_2`$ | $`C_{2v}`$ | (7, 0, 2) | (2, 0, 1) | (3, 0, 2) |

With the two-fold axis of $`\mathcal{O}_1`$ or $`\mathcal{O}_3`$ as the $`z`$-axis, the fixed set of
its rotation $`C_2`$, with its phase, is the odd-weight subspace
$`\mathrm{span}\{v_3, v_1, v_{-1}, v_{-3}\}`$, and the fixed set of its full isotropy is a real form
of that subspace, of real dimension four. The fixed set of the full isotropy of $`\mathcal{O}_2`$ is
a real form of $`V_3`$. The value of $`\mathcal{O}_2`$ lies in a certified interval of width
$`3.1 \times 10^{-52}`$ that contains $`28800/121`$; no exact point is in hand, and the value is not
claimed to be that fraction.

**The indices in order of value.** At $`g = 1`$ the census's indices, in increasing order of value,
are 0, 2, 3, 4, 5, 5, 5, 6, 8, 9. The census's pre-registration recorded this sequence, noted that 1
and 7 were absent, and left open whether the deferred orbits would break the ordering [M8.12]. They
do. The indices of the outside orbits are 4, 6 and 7. $`\mathcal{O}_3`$ lies below the octahedron in
value, 238.36… against 288, and above it in index, 7 against 6, a certified index against an exact
one, so once the orbits outside the class are included, the index no longer increases with the value.
$`\mathcal{O}_3`$ fills the gap at 7, and no known orbit has index 1.

**What [KU] have at the point.** All ten census orbits are [KU]'s states, and [KU]'s formulas
evaluated at the point give their values (Section 6.3). Their procedure does not return all of them.
For each subgroup $`H`$ of their symmetry group, which contains time reversal, it takes the minimum
of the energy on the fixed set of $`H`$ ("calculate the minimum of $`f`$ in the submanifold
$`\mathcal{M}_H`$" [KU, § II.B]), and then compares the minima. At $`g = 1`$ the pyramid
and the C3 ray are maxima of the energy on their own fixed lines, where the energy is a downward
parabola in the squared amplitude (Section 7.1 gives the pyramid's), and minimising on those lines
returns the coherent state and $`v_2`$. At $`g = -1`$ the prism and the D2 ray are the lowest
critical values of $`\widehat{r}_6`$ on their lines, so maxima of the energy there, and minimising
returns the hexagon; that pair rests on the census's critical sets for those two lines being
complete. [KU] have those four states because formulas derived where they are minima still solve the
stationary equation at this point.

For the three outside orbits the statement is stronger. Each has, inside the fixed set of its full
isotropy, both a direction in which the energy decreases and one in which it increases, at either
sign (the restricted signatures above). Any symmetry-fixed set that contains one of these orbits
contains the fixed set of its full isotropy, and restricting a quadratic form to a subspace can
raise neither count, so the same holds on every such set. None of the three is a local minimum of the
energy on any symmetry-fixed set containing it, at either sign, so no procedure that returns local
minima on those sets returns them, [KU]'s included. That includes the domain on which
[KU] computed their state C numerically, complex vectors of the form $`(a, 0, b, 0, c, 0, d)`$, the
odd-weight subspace [KU, § IV.C]: $`\mathcal{O}_1`$ and $`\mathcal{O}_3`$ lie in it, with the
signatures of the last column.

Whether a [KU] formula, evaluated at the point, coincides with one of the three is a separate
question, and a search. $`\mathcal{O}_1`$ and $`\mathcal{O}_3`$ are of the isotropy type of [KU]'s
state C, not state C: [KU] computed C only numerically, as the minimum on its fixed set, so there is
no formula to compare. Of the other rows that might supply one at the point, G and R do not exist
there, since their parameters would need square roots of negative numbers, and J reduces to P. No row
has the isotropy type of $`\mathcal{O}_2`$, whose only nontrivial element is antiunitary: [KU]'s
discrete cases are indexed by rotation groups, $`O`$, $`T`$, $`D_n`$ and $`C_n`$ [KU, § IV.C], and
the rotation stabiliser of $`\mathcal{O}_2`$ is trivial. [KU] compute no Hessians, and neither the
census's signatures nor the certified ones were located in [KU], in [HY], who build a Hessian to test
the stability of ground states of a chromium condensate in a field, or in [BPR], who treat only the
hexagon at spin 3, by symmetry and without energies.

**What is not claimed.** Outside the class the critical set is not classified: the three orbits
above are the ones the numerical censuses found, and nothing here says there are no others. The
signatures are Morse data of $`\widehat{r}_6`$, and so of the reduced energy on the block at each
sign; they are not stability statements about the local branch germs of Section 8.

### 7.3 The extremes

The table of Section 7.1 runs from $`1/924`$ at the coherent state to $`463/924`$ at the hexagon, and
[RK] ask, for every spin, whether the NOON state, which at spin 3 is the hexagon, has the largest top
multipole a state can reach. At spin 3 both ends are exact:

```math
\frac{1}{924} \;\le\; \widehat{r}_6 \;\le\; \frac{463}{924}
\qquad\text{on } \mathbb{P}(V_3),
```

with the lower value attained exactly on the coherent states and the upper exactly on the orbit of
the hexagon $`(v_3 + v_{-3})/\sqrt{2}`$ under rotations and phase. By Section 6.2 these are the
bottom and the top of the reduced energy at the paper's sign $`g = 1`$, and they exchange roles at
$`g = -1`$. The two ends are not on the same footing. The lower one follows in a few lines from a
classical inequality, once an identity connects that inequality to $`\widehat{r}_6`$, and it comes
first. The upper one is the theorem of this subsection.

**The minimum.** For $`u \in V_3`$ write

```math
P_u(x, y) \;=\; \sum_{m=-3}^{3} u_m \sqrt{\binom{6}{3+m}}\; x^{3+m}\, y^{3-m} ,
```

so that $`P_u(1, -z)`$ is the Majorana sextic of Section 2.1, and give binary forms of
degree $`n`$ the Bombieri norm

```math
\Bigl[\, \sum_{k} c_k\, x^k y^{n-k} \Bigr]^2 \;=\; \sum_{k} \frac{\lvert c_k\rvert^2}{\binom{n}{k}} .
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

Since $`P_{\Theta u}(x, y) = -\overline{P_u}(y, -x)`$, where the bar conjugates the coefficients,
the twelve roots of $`P_u P_{\Theta u}`$ are the constellation of $`u`$ together with its antipodal
image, and $`\widehat{r}_6`$ is the squared Bombieri norm of that degree-12 form.

> **Proposition 7.4** (the minimum)**.** On $`\mathbb{P}(V_3)`$, $`\widehat{r}_6 \ge 1/924`$, with
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
$`[P_u] = [P_{\Theta u}] = \lVert u\rVert`$ it is $`\widehat{r}_6 \ge 1/924`$. Equality therefore
makes $`P_u`$ the sixth power of a linear form: $`u`$ is coherent, its constellation a single point
of multiplicity six. Conversely, a coherent state is $`g v_3`$ up to phase for some
$`g \in \mathrm{SU}(2)`$. Since $`\Theta`$ commutes with rotations (Section 2.2) and
$`\Theta v_3 = -v_{-3}`$, the forms $`P_u`$ and $`P_{\Theta u}`$ are then multiples of
$`(g \cdot x)^6`$ and $`(g \cdot y)^6`$, where $`g`$ acts on linear forms by substitution: sixth
powers of orthogonal forms, so equality holds. $`\square`$

The minimum has been stated before. Björk, Klimov, de la Hoz, Grassl, Leuchs and Sánchez-Soto [Bj]
state that the coherent states maximise the cumulative sum of the multipole lengths of orders 1 to
$`M`$, for every $`M`$. Since the multipole lengths of a pure state sum to 1 in the normalisation
used here and the monopole is fixed, the order $`M = 2S - 1`$ is the statement that the coherent
states minimise the top multipole. Their appendix reduces the question to weight states by an
assertion it does not prove, and it makes no uniqueness claim. Lemma 7.3 was not located in the
sources read, [Bj] and [RK] among them; with it, the classical inequality and its equality case give
the whole statement.

**The maximum.**

> **Theorem 7.5.** On $`\mathbb{P}(V_3)`$, $`\widehat{r}_6 \le 463/924`$, with equality exactly on
> the orbit of the hexagon $`(v_3 + v_{-3})/\sqrt{2}`$ under rotations and phase.

The argument is the author's. An independent audit graded every step of it established, found no
gap and no false statement, and supplied steps that the author's text left out. The proof below
follows that argument, restructured in a few places, and a dagger † marks each supplied step it
still uses, one-line facts included; the certification and audit section at the end of the paper
names the restructurings and maps each dagger to the audit's record. Work on the unit sphere of $`V_3`$, with $`f`$ and
$`\mathcal{N}`$ as in Section 6, $`F_\pm = F_x \pm i F_y`$, $`\lambda_{\max}`$ for the largest
eigenvalue of a hermitian operator, and $`K = 15/\sqrt{6}`$, so that $`K^2 = 75/2`$.

*Step 1: an invariant form.* The five functions $`\lVert\rho_6\rVert^2`$, $`\lVert u\rVert^4`$,
$`\lvert f\rvert^2`$, $`\lVert B_0\rVert^2`$ and $`\mathrm{Tr}\,\mathcal{N}^2`$ are real quartics of
bidegree $`(2,2)`$ in $`(u, \bar u)`$, invariant under $`\mathrm{U}(1) \times \mathrm{SU}(2)`$.† By the
argument of Proposition 6.1, which identifies such quartics with the invariant hermitian forms on
$`\mathrm{Sym}^2 V_3`$,† they lie in a real space of dimension four. The last four take at
$`v_3, v_2, v_1, v_0`$ the values

```math
\left(1, 9, 0, \tfrac{171}{2}\right), \quad (1, 4, 0, 48), \quad \left(1, 1, 0, \tfrac{123}{2}\right), \quad \left(1, 0, \tfrac17, 72\right),
```

with determinant $`180/7`$. They are therefore a basis, and matching the values $`1, 36, 225, 400`$
over 924 gives, on the unit sphere,

```math
\widehat{r}_6 \;=\; -\frac{5}{231} \;-\; \frac{\lvert f\rvert^2}{22} \;+\; \frac{7}{11}\,\lVert B_0\rVert^2 \;+\; \frac{\mathrm{Tr}\,\mathcal{N}^2}{198} .
```

*Step 2: two bounds.* $`\lvert f\rvert^2 \ge 0`$, with equality exactly when $`f = 0`$. Since
$`B_0 = -\langle \Theta u, u\rangle/\sqrt{7}`$ and $`\lVert\Theta u\rVert = \lVert u\rVert`$, the
Cauchy-Schwarz inequality gives $`\lVert B_0\rVert^2 \le 1/7`$, with equality exactly when
$`\Theta u`$ is a multiple of $`u`$.

*Step 3: the nematic bound.* $`\mathrm{Tr}\,\mathcal{N}^2 \le 171/2`$, with equality only when
$`u`$ lies in $`\mathrm{span}\{R v_3, R v_{-3}\}`$ for a rotation $`R`$. [KU] state this bound,
attained at the eigenvalues $`(9, \tfrac32, \tfrac32)`$ of $`\mathcal{N}`$; the justification they
give, the trace and the range $`[0, 9]`$ of the eigenvalues, would also admit $`(9, 3, 0)`$, where
$`\mathrm{Tr}\,\mathcal{N}^2 = 90`$.

(3a) Since $`\mathrm{Tr}\,\mathcal{N} = 12`$,† write $`\mathcal{N} = 4I + \mathring{\mathcal N}`$,
with $`\mathring{\mathcal N}`$ the trace-free part, so that
$`\mathrm{Tr}\,\mathcal{N}^2 = 48 + \lVert\mathring{\mathcal N}\rVert^2`$. For a real symmetric
traceless $`E`$ of unit norm, $`\mathrm{Tr}(\mathring{\mathcal N} E) = \langle u, A_E u\rangle`$ with
$`A_E = \sum_{\mu\nu} E_{\mu\nu}(F_\mu F_\nu + F_\nu F_\mu)/2`$,† and
$`\lVert\mathring{\mathcal N}\rVert = \max_E \mathrm{Tr}(\mathring{\mathcal N} E)`$, attained at
$`E = \mathring{\mathcal N}/\lVert\mathring{\mathcal N}\rVert`$ by the Cauchy-Schwarz inequality.† It
therefore suffices to show $`\lambda_{\max}(A_E) \le K`$ for every
such $`E`$. Rotating $`E`$ conjugates $`A_E`$ by the action of the rotation on $`V_3`$,† so
$`\lambda_{\max}(A_E)`$ depends only on the eigenvalues $`e_1, e_2, e_3`$ of $`E`$, and for diagonal
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

and the last eigenvalue, 0, is below $`K`$. The sign on the fourth basis vector makes $`M_2`$
literally $`M_1`$ at $`-b`$; without it the two are conjugate by $`\mathrm{diag}(1, -1)`$, with the
same spectrum, which is how the audit recorded it.

(3b) On the ellipse $`N = 1`$ one has $`a + 6b \le \sqrt6`$† and $`\lvert a\rvert \le \sqrt{3/2}`$,†
since $`6N^2 - (a + 6b)^2 = 3(a - 2b)^2`$ and $`\tfrac32 N^2 - a^2 = 12b^2`$.

- $`M_1`$. Its larger eigenvalue is $`a + 6b + \sqrt{16a^2 - 48ab + 96b^2}`$, and
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
- $`M_2`$ is $`M_1`$ with $`b`$ replaced by $`-b`$, and the ellipse is even in $`b`$.
- $`M_3`$. Its larger eigenvalue is $`-2a + \sqrt{4a^2 + 240b^2}`$, which on the ellipse is
  $`-2a + \sqrt{30 - 16a^2}`$,† with $`30 - 16a^2 \ge 6`$.† Since
  $`K + 2a \ge K - 2\sqrt{3/2} = 9/\sqrt6 > 0`$, the bound is equivalent to
  $`(K + 2a)^2 \ge 30 - 16a^2`$, and $`(K + 2a)^2 - (30 - 16a^2) = 20\,(a + \sqrt6/4)^2 \ge 0`$.

Hence $`\lambda_{\max}(A_E) \le K`$ for every $`E`$, so $`\lVert\mathring{\mathcal N}\rVert \le K`$ and
$`\mathrm{Tr}\,\mathcal{N}^2 \le 48 + 75/2 = 171/2`$.

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

(3d) Equality in the nematic bound.† If $`\mathrm{Tr}\,\mathcal{N}^2 = 171/2`$ then
$`\lVert\mathring{\mathcal N}\rVert = K`$. Put $`E_* = \mathring{\mathcal N}/K`$. Then
$`K = \mathrm{Tr}(\mathring{\mathcal N} E_*) = \langle u, A_{E_*}u\rangle \le \lambda_{\max}(A_{E_*}) \le K`$, so both are
equalities: $`u`$ lies in the top eigenspace of $`A_{E_*}`$, and $`E_*`$ is an equality point,
$`E_* = (3\hat n\hat n^{\mathsf T} - I)/\sqrt6`$.

(3e) For $`\hat n = \hat z`$ the operator $`(3F_z^2 - 12)/\sqrt6`$ is diagonal in the weight basis,
with entries $`(3m^2 - 12)/\sqrt6`$, and its largest value, $`15/\sqrt6 = K`$, occurs only at
$`m = \pm 3`$.† So the top eigenspace is $`\mathrm{span}\{R v_3, R v_{-3}\}`$, for a rotation $`R`$
taking $`\hat z`$ to $`\hat n`$.

*Step 4: the combination.* In Step 1 the coefficients of $`\lvert f\rvert^2`$,
$`\lVert B_0\rVert^2`$ and $`\mathrm{Tr}\,\mathcal{N}^2`$ are $`-1/22`$, $`7/11`$ and $`1/198`$: all
nonzero, with the signs that make Steps 2 and 3 upper bounds for their terms. So

```math
\widehat{r}_6 \;\le\; -\frac{5}{231} + \frac{7}{11}\cdot\frac17 + \frac{1}{198}\cdot\frac{171}{2} \;=\; \frac{463}{924} ,
```

with equality only if all three bounds are equalities. In particular
$`\mathrm{Tr}\,\mathcal{N}^2 = 171/2`$, so by Step 3, after a rotation, $`u = \alpha v_3 + \beta v_{-3}`$
with $`\lvert\alpha\rvert^2 + \lvert\beta\rvert^2 = 1`$. On that span
$`f = (0, 0, 3(\lvert\alpha\rvert^2 - \lvert\beta\rvert^2))`$,† so $`f = 0`$ forces
$`\lvert\alpha\rvert = \lvert\beta\rvert = 1/\sqrt2`$; then $`\langle\Theta u, u\rangle = -2\alpha\beta`$
has modulus 1, so $`\lVert B_0\rVert^2 = 1/7`$ holds as well.† Explicitly, on the span
$`\mathcal{N} = \mathrm{diag}(\tfrac32, \tfrac32, 9)`$ and
$`\lVert B_0\rVert^2 = 4\lvert\alpha\beta\rvert^2/7`$,† and Step 1 gives†

```math
\widehat{r}_6 \;=\; \frac{463}{924} \;-\; \frac12\left(\lvert\alpha\rvert^2 - \lvert\beta\rvert^2\right)^2 .
```

The remaining relative phase is a rotation about the axis, since rotating by $`\tau`$ about it
multiplies $`v_{\pm 3}`$ by $`e^{\mp 3i\tau}`$.† So every maximiser is the hexagon up to rotation and
phase, and every such state attains $`463/924`$. $`\square`$

Step 3 alone does not decide $`\widehat{r}_6`$: the whole span of $`v_3`$ and $`v_{-3}`$ saturates
the nematic bound, and on that span $`\widehat{r}_6`$ runs from $`1/924`$ at the coherent ends to
$`463/924`$ at the balanced point. It is Step 4 that picks the orbit.

At spin 3 this answers the question [RK] pose (Section 7.1): no state has a larger top multipole than
the NOON state, and only its orbit attains it. [KU]'s phase diagram shows the same fact numerically at
the opposite sign, where the hexagon is the ground state (Section 6.2). The exact statement, with its
maximiser set, was not located in the sources read.

The two ends differ in kind, and the product of forms shows why. For binary forms of degrees $`m`$
and $`n`$,

```math
\frac{m!\,n!}{(m+n)!} \;\le\; \frac{[pq]^2}{[p]^2\,[q]^2} \;\le\; 1 .
```

The lower bound is [BBEM]'s. Reznick records the upper, with equality at powers of one linear form
[Re, § 5 and Corollary 5.9], and it has a one-line proof: with forms identified with symmetric
tensors so that the Bombieri norm is the tensor norm, the product $`pq`$ is the orthogonal
projection of $`p \otimes q`$ onto the symmetric tensors. The lower bound is attained by powers of
two orthogonal linear forms, a configuration the constraint $`q = P_{\Theta u}`$ admits, since a
coherent state and its time reverse are exactly such powers; so it decides the minimum. The upper
bound is attained by powers of one linear form, which the constraint excludes, since the time
reverse of a sixth power is the sixth power of the orthogonal form. It gives only
$`\widehat{r}_6 \le 1`$, and the maximum needs the argument above.

---

## 8. Local branch germs on the quotient

Section 8.1 interprets Theorem 5.1 and derives nothing. Without it, the theorem is a bare statement
about a quartic on a seven-dimensional space; the Lyapunov-Schmidt reading explains why that
particular quartic on that particular space is worth extremising. Sections 8.2 and 8.3 then report
how far the problem it poses has been carried since, each result at the standing its record gives
it: the first correction at four rays, exact and reproduced blind [M8.10], and local branch germs, for
sufficiently small amplitude, at eight rays, expanded at six of them, an audited argument [M8.11].
Section 8.4 says what remains out of reach.

### 8.1 The setting

The equation is the one fixed in Section 2.5,

```math
(-\Delta - \lambda)\psi \;+\; \lvert\psi\rvert^2\psi \;=\; 0 ,
```

with $`\lambda`$ a spectral parameter near $`\lambda_6 = 48/R^2`$, the level-6 eigenvalue of the
Laplacian on $`S^3`$. The kernel that Lyapunov-Schmidt needs is the kernel of the *linearisation*
$`-\Delta - \lambda`$ at $`\lambda = \lambda_6`$, not of $`-\Delta`$, and that is exactly the
level-6 eigenspace $`V_3 \otimes \mathrm{Hom}_{2I}(\sigma, V_3)`$, of dimension seven since the
branching is multiplicity-free. Without the parameter there is no kernel and no reduction; it is the
parameter that makes this a bifurcation problem at all. Near that value Lyapunov-Schmidt splits the
equation into a projection onto the kernel and a complementary range equation.

Level 6 is not an extra choice, but neither is it forced by the geometry: it is fixed by the choice
of object, since spin-3 states put the left index in $`V_3`$. What *is* a fact about the quotient is
that the two sectors in which the question can then be posed, $`\mathbf{3}'`$ and $`\mathbf{4}`$,
first occur at that level, so the block eigenspace is the bottom of the spectrum on each of their
bundles and the bifurcation read below is one from the lowest linear eigenvalue on each of those
bundles. No claim is made that the resulting states minimise anything, so the word ground state is
avoided. Odd levels are excluded by parity: at $`\ell = 2j`$ with $`j`$ half-integer, $`-I`$ acts as
$`-1`$, whereas $`\mathbf{3}'`$ and $`\mathbf{4}`$ factor through $`A_5 = 2I/\{\pm I\}`$ and have
$`-I`$ acting trivially. For the even levels below 6, extending the branching table of Section 4.3
downward gives $`V_0 = \mathbf{1}`$, $`V_1 = \mathbf{3}`$, $`V_2 = \mathbf{5}`$.

The leading cubic term of that reduction is the projection of the nonlinearity back onto the
eigenspace, which is exactly the self-interaction of Sections 4 and 5. Under that reading, Theorem
5.1 says the reduced equation's cubic term is confined to $`\mathrm{span}\{M_0, M_6\}`$, that
$`M_0`$ contributes only a radial rescaling and therefore acts as a Lagrange multiplier rather than
as a tangential direction, and that the tangential content is the single ray $`[M_6]`$, with the
coefficients computed in Section 5.5. The quartic $`Q`$ plays the part of the reduced energy:
Section 5.5 shows that on the unit sphere the tangential gradient of $`Q`$ is proportional to the
tangential projection of the self-interaction, the denominator contributing only a radial term. The
critical rays of $`Q`$ are then the **critical directions of the leading reduced problem**, and not by
themselves solutions of the equation: a solution needs the range equation as well, which the first
version of this paper did not carry out. Section 7 gives the critical set within a symmetry class,
and Sections 8.2 and 8.3 report how far the range equation has since been carried.

Both records work with $`(-\Delta - \lambda)\psi + g\lvert\psi\rvert^2\psi = 0`$ at general real
$`g \neq 0`$ and state every value per power of $`g`$, which covers both signs of Section 6.2. They
work in the convention $`R = 1`$, so the bifurcation eigenvalue is 48; in the paper's general
notation the linear bifurcation point is $`48/R^2`$, and the correction coefficients below are quoted
in the records' $`R = 1`$ convention. Each block section $`\Phi`$ is normalised by
$`\int_X \lvert\Phi\rvert^2 = 1`$ on the normalised measure, as in Corollary 5.6, and gradients are
taken in the real inner product $`\mathrm{Re}\langle\cdot,\cdot\rangle`$. The values move with these
conventions, and with the orientation of a tangent where one enters [M8.10], [M8.11].

### 8.2 The first correction at four rays

In a Lyapunov-Schmidt construction carried through, the range equation is solved for the transverse
component as a function of the kernel variable, and that solution is substituted back, contributing
corrections to the reduced equation at higher order in the amplitude. [M8.10] carries this one order
at the four symmetry-pinned rays of Section 7.1, the coherent, zonal, octahedral and hexagonal rays,
in both sectors. With $`\Phi`$ a critical ray's block section and $`K`$ the level-6 block, expand

```math
\psi \;=\; a\Phi + a^3\xi + O(a^5), \qquad \lambda \;=\; 48 + \lambda_2 a^2 + \lambda_4 a^4 + O(a^6),
```

with the phase fixed so that $`\langle\Phi, \psi\rangle`$ is real and $`\Pi_K \xi = 0`$. At order
$`a^3`$ the block part gives $`\lambda_2 = gQ`$, where $`Q = \int_X \lvert\Phi\rvert^4`$ is the scalar
of Corollary 5.6, $`Q = 1 + w_6(\sigma)\,\widehat{r}_6`$ with $`w_6(\mathbf{3}') = 28/39`$ and
$`w_6(\mathbf{4}) = 21/52`$; the range part gives $`A\xi = -g\,\Pi_\perp N(\Phi)`$, with
$`N(\psi) = \lvert\psi\rvert^2\psi`$ and $`A = -\Delta - 48`$ inverted on $`K^\perp`$. At order $`a^5`$
the block part gives

```math
\lambda_4 \;=\; g\,\langle \Phi, DN_\Phi[\xi]\rangle \;=\; -3g^2 \sum_{n \neq 6} \frac{\lVert \Pi_n N(\Phi)\rVert^2}{n(n+2) - 48} ,
\qquad DN_\Phi[h] \;=\; 2\,\mathrm{Re}(\Phi^\dagger h)\,\Phi + \lvert\Phi\rvert^2 h ,
```

provided its part orthogonal to $`\Phi`$ vanishes, which is the condition for the ray to persist at
this order. The sum is finite, since the cubic of a level-6 section has no content above level 18.
[M8.10] finds the condition met at all four rays, with these values:

| ray | $`\lambda_2/g`$, $`\mathbf{3}'`$ | $`\lambda_2/g`$, $`\mathbf{4}`$ | $`\lambda_4/g^2`$, $`\mathbf{3}'`$ | $`\lambda_4/g^2`$, $`\mathbf{4}`$ |
|---|---|---|---|---|
| coherent $`v_3`$ | 1288/1287 | 2289/2288 | −608931967/36722893315680 | −368688201/38687492546560 |
| zonal $`v_0`$ | 1687/1287 | 168/143 | −1871763250/229518083223 | −15820875/15112301776 |
| octahedron | 175/143 | 161/143 | −2203040/944518861 | −162530109/75561508880 |
| hexagon | 1750/1287 | 2751/2288 | −1921938515/459036166446 | −226441775133/38687492546560 |

Two agents, a solver and an auditor, derived every entry blind, with separate implementations, by
exact symbolic routes and without seeing a claimed value, and the auditor then confirmed the solver
value by value [M8.10]. They are exact results reproduced blind, and they stand here as that. The
first two columns are $`1 + w_6\,\widehat{r}_6`$ at the values of Section 7.1, as Corollary 5.6
requires.

Every $`\lambda_4/g^2`$ is negative, and the sign needs two facts, both in the paper. No level of
either sector lies below 6 (Section 8.1), and levels are even, so every $`n \neq 6`$ in the sum has
$`n \ge 8`$ and a positive denominator. And $`Q > 1`$, since $`w_6 > 0`$ and
$`\widehat{r}_6 \ge 1/924`$ (Proposition 7.4), so $`\lvert\Phi\rvert^2`$ is not constant, and with
Parseval the strict Cauchy-Schwarz inequality gives

```math
\sum_{n \neq 6} \lVert \Pi_n N(\Phi)\rVert^2 \;=\; \int_X \lvert\Phi\rvert^6 - Q^2 \;>\; 0 .
```

So $`\lambda_4 < 0`$ for $`g \neq 0`$ wherever the formula holds. This is the solver's route in
[M8.10], with its level hypothesis written out.

At leading order the two sectors differ by one factor at every ray,
$`(\lambda_2(\mathbf{3}') - g)/(\lambda_2(\mathbf{4}) - g) = w_6(\mathbf{3}')/w_6(\mathbf{4}) = 16/9`$,
which is Corollary 5.6's statement that they agree about shape and disagree about scale. At the next
order they stop being proportional: the four ratios $`\lambda_4(\mathbf{3}')/\lambda_4(\mathbf{4})`$
are pairwise distinct [M8.10].

At the pentagonal pyramid the same expansion fails. There the order-$`a^5`$ block equation has a part
orthogonal to $`\Phi`$, in both sectors, so no $`\lambda_4`$ is defined for a fixed direction. [M8.10]
ran the pyramid as a negative control, with its worklist asking the same questions at all five rays,
and both agents found the failure blind. The pyramid lies on a fixed line rather than at an isolated
fixed point (Lemma 7.2), so its direction is free to move along that line at the next order, and
Section 8.3 lets it.

### 8.3 Local branch germs at six rays

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
coefficients [M8.11]. The equation maps $`H^{s+2} \times \mathbb{R}`$ to $`H^s`$ for $`s > 3/2`$, where
$`H^s`$ is an algebra, so the cubic is real-analytic. The block part of $`X_H`$ has complex dimension
$`m`$, which is 1 at the four pinned rays and 2 at the pyramid and the prism. Write
$`\psi = a(\Phi + k) + a^3 w`$ and $`\lambda = 48 + a^2\mu`$, and divide by $`a^3`$: that removes the
trivial solution $`\psi = 0`$, at which the implicit function theorem cannot be applied, since before
the division the radial equation's $`\lambda`$-derivative vanishes at $`a = 0`$. The range equation is
then solved in $`X_H`$ by the implicit function theorem, $`A`$ being invertible on $`K^\perp`$ with a
gap of 32 in sector $`\mathbf{4}`$ and 72 in sector $`\mathbf{3}'`$ above the level-6 eigenvalue, and
what remains is the gradient of a reduced functional on a slice through the ray. At the ray its Jacobian
is block-triangular, with blocks $`-1`$ and $`\tfrac14\,\mathrm{Hess}_T Q`$. At the four pinned rays
$`m = 1`$, the slice is a point, and no nondegeneracy condition enters: the symmetry pins the germ. At
the pyramid and the prism $`m = 2`$, and the slice Hessian must be invertible. It is, through a bridge
the record proves: for a unit tangent $`E`$ in the block, real-orthogonal to $`\Phi`$,

```math
\frac{d^2}{ds^2}\, Q(\cos s\,\Phi + \sin s\,E)\Big|_{s=0} \;=\; 4\big(\langle E, DN_\Phi E\rangle_{\mathbb{R}} - Q(\Phi)\big),
```

so the linear operator of the next order is
$`L_T = \tfrac14\,\mathrm{Hess}_T Q = \tfrac14\,w_6\,\mathrm{Hess}_T\,\widehat{r}_6`$, and one set of
numbers decides both the nondegeneracy and the tilt below. At the pyramid the slice is the real curve
$`\cos t\, v_2 + \sin t\, v_{-3}`$ of Section 7.1, with $`\mathrm{Hess}_T\,\widehat{r}_6 = -104/55`$
along its unit tangent $`e_t`$; the other direction in the line, $`i e_t`$, is a rotation and null. At
the prism the slice is the whole chart of Section 7.1, with
$`\mathrm{Hess}_T\,\widehat{r}_6 = \mathrm{diag}(920/473,\ 8/11)`$ in the unit tangents $`\tau_x`$ and
$`\tau_y = i\tau_x`$, and no cross term. Neither vanishes, in either sector.

The weight states $`v_1`$ and $`v_2`$ satisfy the hypothesis too, with $`m = 1`$, each weight space
being one-dimensional, and the frozen task of [M8.11] records them as covered by the theorem; that run
neither expanded nor scored them, so no values are given for them here. The degeneracy of $`v_1`$ found
in Section 7.2 does not obstruct its germ: rotations about the axis act on its kernel,
$`\mathrm{span}\{v_{-3}, i v_{-3}\}`$ [M8.12], by a different character from the one on $`v_1`$, so the
kernel lies outside the fixed space, and it means only that the germ need not be isolated among all
solutions, which the theorem does not claim. No germ statement is made here for the C3 and D2 rays or
for the three orbits outside the class.

At the pyramid and the prism the direction moves at order $`a^2`$:
$`\psi = a\Phi + a^3(v + \xi) + O(a^5)`$, with the tilt $`v`$ in the block, orthogonal to $`\Phi`$ and
in the slice, fixed by the tangential part of the order-$`a^5`$ block equation,
$`L_T v = -\Pi_T DN_\Phi[\xi]`$. Without the tilt that part is the forcing
$`\langle E, DN_\Phi[\xi]\rangle_{\mathbb{R}}`$ along the slice, which at the pyramid is the obstruction
of Section 8.2, up to the normalisation of the tangent; with it, the part vanishes. At the prism the
tilt has no $`\tau_y`$ component, by a symmetry: $`S = R_z(\pi/3) \circ \Theta`$ acts on the chart as
$`z \mapsto \bar z`$, fixes the prism, and lifts to sections as a rotation composed with fibre
conjugation, so it maps solutions to solutions. The forcing is $`S`$-even, $`\tau_y`$ is $`S`$-odd and
$`L_T`$ has no cross term, so $`v_y = 0`$ exactly. The values, in unit section tangents, with $`e_t`$
along increasing $`t`$ and $`\tau_x`$ along increasing $`x`$ at $`z_0 = +\sqrt{23/10}`$:

| ray | sector | tilt over $`g`$ | $`\lVert v\rVert^2/g^2`$ |
|---|---|---|---|
| pyramid | $`\mathbf{3}'`$ | $`\beta = 1026977\sqrt{39}/3930264000`$ along $`e_t`$ | 1054681758529/396076284864000000 |
| pyramid | $`\mathbf{4}`$ | $`\beta = -931693\sqrt{39}/1746784000`$ along $`e_t`$ | 2604155538747/234711872512000000 |
| prism | $`\mathbf{3}'`$ | $`v_x = 17225159\sqrt{115}/64285514280`$, $`v_y = 0`$ | 296706102575281/35935889967339860160 |
| prism | $`\mathbf{4}`$ | $`v_x = -10210963\sqrt{115}/28571339680`$, $`v_y = 0`$ | 104263765387369/7098447400956021760 |

At each ray the tilt points opposite ways in the two sectors, as the forcing does. The signs of
$`\beta`$ and $`v_x`$ turn with the orientation of the tangent; $`\lVert v\rVert^2`$ does not.

The tilt does not change $`\lambda_4`$ at this order, by [M8.11]'s lemma. Pairing the order-$`a^5`$
block equation with $`\Phi`$, the tilt contributes $`g(2X + \bar X)`$ with
$`X = \langle N(\Phi), v\rangle = \langle \Pi_K N(\Phi), v\rangle = Q\langle\Phi, v\rangle = 0`$, by
criticality. So $`\lambda_4`$ is given by the formula of Section 8.2 at the pyramid and the prism too,
and its sign by the argument there. Criticality is essential: at a non-critical point of the pyramid's
curve the pairing survives, which [M8.11] ran as a negative control. The values:

| ray | $`\lambda_2/g`$, $`\mathbf{3}'`$ | $`\lambda_2/g`$, $`\mathbf{4}`$ | $`\lambda_4/g^2`$, $`\mathbf{3}'`$ | $`\lambda_4/g^2`$, $`\mathbf{4}`$ |
|---|---|---|---|---|
| pyramid | 77/65 | 287/260 | −267786421/58544557500 | −4797453339/2497901120000 |
| prism | 5831/5031 | 609/559 | −336158940460/150812349114141 | −11093213145/4965015608696 |

Two agents, a solver and an auditor, derived these values, the second variations, the forcing and the
tilt blind, and the auditor computed every one of them exactly [M8.11]. The record's own sign step for
this lemma is one line, "By M8.10's argument $`\lambda_4 < 0`$, since $`Q \neq 1`$ at both rays". The
audit received a copy from which the citation had been removed and graded that sentence a defect, for
leaving its level hypothesis unstated; the designer overruled the grade as an artifact of the change,
and recorded that the sentence does not stand alone [M8.11]. Section 8.2 states both facts the sign
needs, from the paper itself.

At the paper's sign $`g = 1`$ (Section 6.2), $`\lambda - 48 = Q a^2 + O(a^4)`$ with $`Q > 1`$, so every
germ leaves the linear point upward in $`\lambda`$, and at $`g = -1`$ downward. The next coefficient
$`\lambda_4/g^2`$ is negative at all six rays in both sectors, whatever the sign. This is read off the
records' values, which are stated per power of $`g`$, and it completes Section 6.2's list of what
depends on the sign.

### 8.4 The ceilings that remain

**The critical set is classified within a class, not outside it.** Section 7.2 gives every critical
orbit within a symmetry class and certifies three outside it. Nothing says the critical set holds no
others.

**The reduction is carried through at six rays, and only locally.** What this paper derives itself is
exact at leading cubic order: the finite-dimensional problem on the degenerate eigenspace, from Sections
4 and 5. Beyond that order it derives the sign of $`\lambda_4`$ (Section 8.2) from facts of its own; the
coefficients and the germs are the records'. At the six rays of Section 7.1 the records carry the range
equation to the order the germs need, and there the formal expansion is the Taylor expansion of a local
branch germ, as an audited argument. Everything else stays out of reach. There is no radius, since no
lower bound on $`\varepsilon`$ is given. There is no stability of any kind, and the Morse indices of
Section 7 are data of the reduced energy, not stability statements about the germs. Nothing is claimed
at finite amplitude. At the weight states $`v_1`$ and $`v_2`$ the theorem applies but gives no values,
since the run did not expand them, and no germ statement is made at the C3 and D2 rays or at the three
orbits outside the class. The values hold in the records' conventions and move with them.

Everything in Sections 3 through 5 stands without this section. Proposition 3.3 is a statement about
binary sextics, Theorem 5.1 a statement about a four-dimensional space of equivariant maps and which
of them a quotient permits for the interaction of Section 2.5. Neither is a statement about the
dynamics that interaction came from, and neither are the germs: they solve the equation of Section
2.5, whose nonlinearity is a hypothesis of the paper. The Lyapunov-Schmidt language supplies the
reason for the question and makes the ceilings above legible as ceilings rather than as omissions: it
identifies which parts of a complete bifurcation analysis are here and which are not. The method
itself is standard and is used rather than developed; the reduction from a degenerate eigenspace is
classical [GS], and no property of it is proved in this paper.

---

## 9. Discussion

### 9.1 What is not claimed

Six limits are collected here rather than left scattered across the sections.

The critical set of $`\widehat{r}_6`$ on $`\mathbb{P}(V_3)`$ is classified only within a symmetry
class: Section 7.2 gives every critical orbit whose fixed locus has projective dimension at most one,
as an audited argument, and certifies three orbits outside that class, and nothing says the critical
set holds no others. The two ends are settled at spin 3 (Section 7.3); the question [RK] pose for
general spin, whether the NOON state has the largest top multipole, is not addressed here beyond spin
3.

The range equation is carried at six rays, by the records of Section 8, and there the formal
expansions are Taylor expansions of local branch germs, for sufficiently small amplitude, as an
audited argument. At the weight states $`v_1`$ and $`v_2`$ the same theorem applies without values,
and no germ statement is made at the C3 and D2 rays or at the three orbits outside the class (Section
8.3). There is no radius, no stability of any kind and no statement at finite amplitude (Section
8.4).

The point of Section 6 is where the density interaction of Section 2.5 lands under the quotient's
selection. It is not the coupling of a physical condensate, and no claim is made about chromium or
any other spin-3 atom (Section 6.3).

The ten census rays are matched to [KU]'s states at the point, exactly (Sections 7.1 and 7.2). The three
orbits outside the class are not: $`\mathcal{O}_1`$ and $`\mathcal{O}_3`$ share the isotropy type of
[KU]'s state C, and the type of $`\mathcal{O}_2`$ has no row in their table (Section 7.2). [BTD]'s own
figure gives coefficients for its four shapes, which were not extracted, so no statement here rests on
that figure.

The closed form for the sector normalisation carries a ceiling of its own, stated with the formula
in Section 5.6 and not repeated here.

Everything above concerns a single block state in a single sector. No statement is made about a
field occupying distinct flat-bundle sectors at once, or about a nonlinearity coupling one sector's
density to another's amplitude. Corollaries 5.5 and 5.6 compare the two sectors; they do not
describe a configuration containing both. The mixed problem is not posed here, let alone solved.

### 9.2 Prior art, and where the boundary falls

The setting and many of the objects of Sections 6 and 7 are known, to three literatures with different
questions: spinor condensates, which ask for ground states and their stability at physical couplings;
the literature on Majorana constellations, multipoles and anticoherence; and the classical theory of
binary forms. What each source establishes is stated separately, with the section of this paper that
uses it, because the items are in different conditions.

*The coupling point and its states.* Diener and Ho [DH] write the spin-3 mean-field energy in the forms
used here and in [KU], name its phases, and draw zero-field phase diagrams over the coupling plane, one
for each sign of the spin coupling, from a combination of analytic and numerical minimisation. Santos
and Pfau [SP] draw the ground-state diagram at chromium's measured scattering lengths, varying the
unknown singlet length and the field. Barnett, Turner and Demler show the hexagon, the pentagonal
pyramid, the prism and the octahedron as spin-3 phases [BTD], and later minimise numerically over all
seven complex amplitudes at every value of the scattering lengths, reproduce both diagrams without
redrawing them, and tabulate the phases' wave functions [BTD07]. Kawaguchi and Ueda [KU] classify the
stationary states by their symmetry groups, give formulas for all but one of them, and draw two
diagrams. Among the published spin-3 diagrams checked here, only [KU]'s second reaches the point of
Section 6, which places the point in phase FF at the paper's sign and in phase A at the other (Section
6.2). [DH]'s coordinates put the point at $`(\alpha, \beta, \gamma) = (32, 12, -1)`$ at the paper's
sign, outside both of their drawn windows, and it is not on [SP]'s slice, along which the ratio of their
spin and nematic couplings is fixed near $`-59/2`$, against $`-17/2`$ at the point. [KU]'s formulas,
evaluated at the point, give all ten census orbits of Section 7.2 with their values, as identities
(Section 6.3); their procedure takes the minimum on each fixed set, so at each sign it returns neither
that sign's two line maxima (Section 7.2) nor the three orbits outside the class, and it claims no
completeness. One naming clash matters: [SP]'s polar phase P is the family
$`\cos\theta\, v_3 + \sin\theta\, v_{-3}`$, which contains the hexagon, while [KU]'s state P is the
weight state $`v_1`$. Up to rotation and phase that family is the whole span of $`v_3`$ and $`v_{-3}`$,
on which Section 7.3 shows the nematic bound saturated throughout and $`\widehat{r}_6`$ running from the
coherent state's $`1/924`$ to the hexagon's $`463/924`$.

*The critical geometry at the point.* None of these sources computes it. [KU] compute no Hessians. He
and Yi [HY] build the Hessian of the mean-field energy to test whether ground states of a chromium
condensate in a magnetic field, with dipolar interactions, are stable, which is a different question.
Barnett, Podolsky and Refael [BPR] classify the collective modes of the hexagon by symmetry alone,
without energies. The Morse indices of Section 7.2, the census's and the certified ones, were not
located in [KU], [HY] or [BPR]. [BTD]'s four shapes all occur among the critical rays of Section 7.1
(Figure 2), the pyramid and the prism as one member each of continuous families, fixed there by
criticality. One identification is worth stating, because the natural guess is wrong: the pyramid is
*not* the weight state $`v_2`$, whose Majorana polynomial $`-\sqrt6\,z`$ has one root at the origin
and five at infinity, giving five coincident points and one antipodal, a degenerate configuration
rather than a polyhedron. It occurs at an interior point of
the line through $`v_2`$ and $`v_{-3}`$, at neither end.

*The two ends.* The hexagon is the ground state at the opposite sign in [KU]'s diagram, and the coherent
state at the paper's sign, both placed there numerically in [KU]. Romero, Klimov, Goldberg, Leuchs and
Sánchez-Soto give the top multipole of the NOON state in closed form,
$`\varrho^2_{2S} = \tfrac12 + \binom{4S}{2S}^{-1}`$, which at $`S = 3`$ is the hexagon's $`463/924`$,
and ask, for every spin, whether it is the largest a state can reach, probing the question numerically
[RK]. Both the value and the question belong to them (Section 7.1). What is not in that paper is the
critical set: they ask which state maximises the top multipole, while Section 7 gives the critical
orbits within a class and proves that only the hexagon's orbit attains the maximum. The exact maximiser
set at spin 3, Theorem 7.5, was not located in the sources read. The minimum was stated by Björk and
coauthors, as one order of a claim about cumulative multipoles, with an appendix step unproved and no
uniqueness claim [Bj]; with Lemma 7.3 it is the inequality of Beauzamy, Bombieri, Enflo and Montgomery
[BBEM] with Reznick's equality case [Re] (Section 7.3). [KU] and their review [KU-rev] state the nematic
bound $`\mathrm{Tr}\,\mathcal{N}^2 \le 171/2`$, with a justification that alone admits 90; Step 3 of
Section 7.3 proves it.

*The octahedral state is anticoherent of order exactly 3.* The lower bound is prior art in a clean
form: Crann, Pereira and Kribs [CPK] prove that a Majorana constellation which is both the orbit of
a finite subgroup of $`\mathrm{O}(3)`$ and a spherical $`t`$-design gives an anticoherent state of
order $`t`$, and the octahedron is both, at $`t = 3`$. That statement is a one-way implication and
carries the group-orbit hypothesis, so it bounds the order below and not above. The **sharpness is
computed in Section 7.1** and does not follow from it: the multipole row is
$`1/7, 0, 0, 0, 6/11, 0, 24/77`$, so rank 4 is nonzero and the order is exactly 3 rather than at
least 3.

Recognising a configuration is not the same as selecting it. The result established here is which
member of a known family a specific quotient forces, and the boundary between those two things is
the reason Section 3 is billed as a proposition and Section 5 as a theorem. Its pair, for Sections 6
and 7, is that knowing the phases is not classifying the critical geometry: the condensate literature
has the states and the ground states at the point, and what this paper adds there is the identity that
places the ray at the point, the census within a class and its Morse indices, three certified orbits
outside it, and the two ends proved.

### 9.3 The search, stated as a search

Three searches were run at different times and they are in different conditions, so they are reported
separately.

The first asked whether the results of Section 3 are known. The polarised identity of Section 3.1
and the zero-set statement of Proposition 3.3 were not located. Every reference below was verified
against its publisher or preprint record rather than from recall, and one gap closed in the process:
the order-3 lower bound has a clean source in [CPK], which the first pass had not surfaced.

The second asked the question the contribution actually rests on, whether the selection statement of
Section 5 has been made before. It ran ten queries across six lines of approach: nonlinear
Schrödinger and semilinear elliptic problems on spherical space forms; equivariant bifurcation with
icosahedral symmetry; harmonic analysis on the Poincaré dodecahedral space; spin-3 spinor
condensates and their interaction channels; anticoherent states and multipoles from Majorana
constellations; and symmetry selection rules for nonlinear couplings. Four sources were then read
rather than skimmed.

Nothing was found that filters a cubic interaction by a finite subgroup on a space form, and nothing
that puts $`\lvert\psi\rvert^2\psi`$ on a flat bundle over $`S^3/2I`$. Three adjacencies were found
and are now cited where they belong rather than here: the four-dimensional family is the known
four-channel spin-3 interaction [DH], [KU]; the transform of Section 2.3 is the standard
state-multipole expansion [Fa], [RK]; and the hexagonal value $`463/924`$, together with the
global-maximum question attached to it, is prior art [RK]. The last of those was a headline number
of the first version and is now attributed.

The third, for this version, read the sources of Sections 6 and 7 at the level of their own text:
[KU], [KU-rev], [DH], [SP], [BTD], [BTD07], [HY], [BPR], [RK] and [Bj] from their preprint sources, and
[Re] in full; [BBEM] itself was not read, and its inequality enters through [Re]'s statement of it.
Each thing Section 9.2 says this paper adds at the point was not located in them: the identity of
Proposition 6.1, whose application to the ray of Theorem 5.1 is specific to the selection made here; the
completeness of the census within its class, which [KU] do not claim; the Morse indices of Section 7.2;
the three orbits outside the class, with one caveat, since $`\mathcal{O}_1`$ and $`\mathcal{O}_3`$ are of
the isotropy type of [KU]'s state C, which [KU] computed only numerically, as the minimum on its fixed
set, and at the point that minimum is the coherent state or the hexagon (Section 7.2), while the type of
$`\mathcal{O}_2`$ has no row; the identity of Lemma 7.3, which completes the proof of the minimum; and
the exact maximiser set of Theorem 7.5.

What the searches do not establish is also worth saying. **Not surfaced is not the same as new.** Ten
queries and a reading of the sources above amount to a real search, not an exhaustive one. Three gaps
are known: the equivariant bifurcation literature is largely in monographs that search engines index
poorly; the older invariant-theory literature was not worked; and no subscription index was used,
which is the instrument the question really wants. Section 9.2 gives the per-item status of the
prior-art statements rather than a blanket one, because the items are in different conditions.

### 9.4 The open historical question

The object

```math
\Phi(F,G) \;=\; F \,(F,G)_1
```

is a joint covariant of two independent binary sextics, of bidegree $`(2,1)`$ and order 16, and it
is entirely possible that it is named in Grace and Young [GY], Elliott, or Gordan. That is a
question worth putting to someone who works in classical invariant theory.

The question this paper's object raises is a different one, and the difference is easy to lose. The
covariant here is the real-analytic specialisation $`G = \Theta F`$ along the time-reversal
diagonal, and a specialist asked about $`\Phi`$ will answer about $`\Phi`$, correctly, and about a
different statement. Both questions should be asked, in that order, and kept apart in whatever
answer comes back.

### 9.5 Where the family sits

The homogeneous quartic $`\widetilde{Q}`$, not its projective normalisation $`Q`$, is one member of
a four-dimensional space of $`\mathrm{SU}(2)`$-invariant quartics on spin 3. That space has the same
dimension as $`\mathscr{E}_3`$, and for the same reason: both are counted by the four summands
$`V_0 \oplus V_2 \oplus V_4 \oplus V_6`$ of $`\mathrm{Sym}^2 V_3`$, so selecting a quartic and
selecting a cubic map are the same problem in two costumes. Equal dimension alone would not say
that, so here is the map: $`\widetilde{Q} \mapsto \nabla_{\bar u}\widetilde{Q}`$ is equivariant and
linear from invariant homogeneous quartics to $`\mathscr{E}_3`$, and injective, since Euler's
identity recovers a homogeneous quartic from its gradient. Both spaces have dimension four, so it is
an isomorphism; Section 5.5 exhibits it channel by channel, as the per-rank identity
$`\nabla_{\bar u}\lVert\rho_K\rVert^2 = c_K M_K`$ with every $`c_K`$ nonzero. The community that
studies anticoherence works with members of that space and with the symmetric constellations
attached to them. Anyone in that community will recognise the family immediately, which is a reason
to say so here rather than to leave it to be noticed: the contribution is not the family, and not
the quartic considered in isolation, but which member of it the icosahedral quotient permits, for
the density-type interaction of Section 2.5.

Section 6 says where in the family that member lies. It is one point, $`(c_\gamma, c_\alpha, c_\beta)
= (-1, 32, 12)`$ in [KU]'s coordinates at the paper's sign, and the condensate literature has studied
the family around it for other reasons: its phases, their vortices and their collective modes. At the
point, everything Sections 6 and 7 compute is spin 3, and nothing in it is evidence for the quotient or
for anything physical.

That framing also explains the shape of the paper. Almost everything on the way to the answer is
universal: the four-dimensional family, the canonical basis, the operator structure and its
alternating row, the forced time-reversal phase, and the critical geometry of the surviving channel.
For Theorem 5.1 the quotient supplies two facts, the invariant-degree filter and the
multiplicity-free complementary branching, and those two are the whole of its icosahedral content;
the branching is one statement doing two jobs, scalarisation and weight. Branching computations
appear elsewhere for other purposes, in Section 4.3 for the availability of the spin-8 target and in
Section 8.1 for the first occurrence of each sector, and neither feeds the theorem. Chronologically
the icosahedron came first and led to the ambient proposition rather than requiring it, but the
logical dependence runs the other way, and the paper is ordered by the logic.

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

Twenty-one claims pre-registered from the first version have been reproduced on the OpenWave M8 track by an independent, blind computation. Two agents, a solver and an auditor, built every object from its definition in their own code, working from a two-stage handout with no access to the paper, its title or any value it claims. The group entered only as the two unit quaternions that generate it, and both agents derived its order, perfectness, invariant degrees and branching from those generators instead of importing them from a recognised group. The auditor worked on disjoint primitives, with its own Racah-formula couplings, the group in exact $`\mathbb{Q}(\sqrt{5}, i)`$ arithmetic, projectors from Casimir operators and a Haar quadrature that does not use Schur orthogonality, and then tried to refute every answer the solver gave. It refuted no value: 80 of its 81 exact comparisons agreed outright, and the last differed by a change of convention that the audit proved.

All twenty-one pre-registered claims reproduced. On the ambient side, $`\mathrm{Sym}^3 V_3 = V_1 \oplus 2V_3 \oplus V_4 \oplus V_5 \oplus V_6 \oplus V_7 \oplus V_9`$ came out with no $`V_8`$, $`M_0(u) = -\lVert u\rVert^2 u/\sqrt{7}`$ is radial, and $`M_6`$ is diagonal on the weight basis with entries proportional to the squared binomials $`1, 36, 225, 400, 225, 36, 1`$. Proposition 3.3 is where the run was built to be hardest. The first stage withheld the normalisation that points toward the first transvectant, and both agents still found that route on their own and proved, rather than sampled, that the spin-8 channel vanishes exactly on the time-reversal-invariant rays.

On the quotient, the invariants among ranks 0 to 6 sit only at ranks 0 and 6, and $`V_3`$ restricts to two constituents of dimensions 3 and 4. Theorem 5.1 reproduced: the self-interaction came out as $`(d/7)\lVert u\rVert^2 u - ((7-d)/\sqrt{91})\,M_6(u)`$ in the sector of dimension $`d`$, a radial term plus a nonzero multiple of $`M_6`$, the single projective ray of clause 4, with $`\lVert R_6\rVert^2 = 12/7`$ in both sectors, $`w_0 = 7`$, $`w_6/w_0 = (7-d)/(13d)`$ and normalisations 1287 and 2288. The degree-12 invariant $`I_{12}`$ has twelve simple roots, and the transvectant map Section 5.7 builds on it is injective. The tabulated critical rays came out at $`924\,\lVert\rho_6\rVert^2 = 1, 400, 288, 463`$, the chart carries exactly five critical points, found by Gröbner elimination and confirmed by an independent Newton census, and the named shapes came out as Section 7.1 gives them: the trigonal prism and the regular octahedron on the three-fold locus, and the pentagonal pyramid at $`9/35`$. Corollaries 5.4 to 5.6 reproduced as stated, down to $`Q_{\mathbf{3}'} - Q_{\mathbf{4}} = \tfrac{49}{156}\,\widehat{r}_6`$. The second quartic, built from $`\psi\psi^{T}`$, lands on a different plane: the four maps involved have rank 4.

The audit also supplied a clarification rather than a correction. The seven multipole quartics $`\lVert\rho_K(u)\rVert^2`$ satisfy three linear relations, so the individual weights of Section 5.2 are fixed by its Peter-Weyl formula rather than by the quartic alone; that section records the point, and no reported value depends on it. This is a blind recomputation of what the first version claims, from definitions, not a second proof: the proofs were not checked line by line, the run stops at level 6 and at the two interactions built there, the general-spin constant of Section 5.9 was left out of the claims because checking several spins does not verify a formula in $`j`$, and no dynamics was run. The [method note](https://github.com/openwave-labs/openwave/blob/b0b078678ca75ad31b8813806d6b61a0a386d1e0/openwave/xperiments/m8_mit/research/findings/m8_1_2_method_note.md) carries the full record.

---

## Independent certification and audit of Sections 7 and 8

[![OpenWave](/files/assets/openwave-banner-graphite.svg)](https://github.com/openwave-labs/openwave/blob/b0b078678ca75ad31b8813806d6b61a0a386d1e0/openwave/xperiments/m8_mit/research/m8_roadmap.md)

Four later runs on the OpenWave M8 track reproduced or audited the results of Sections 7 and 8: the first
correction and the local branch germs (M8.10 and M8.11), and the census and the maximum (M8.12 and
M8.13). Each record's standing is stated with it, and every link below points to the track's
repository at one commit, `b0b07867`.

### The first correction (M8.10)

The values of Section 8.2 were reproduced blind in the same way: two agents computed the 36 level norms
and the eight values of $`\lambda_4/g^2`$ from definitions by exact symbolic routes, and the auditor then
confirmed the solver value by value. The run's findings record that every frozen claim reproduced
blind, that the values the task had filed as rational identifications stand as exact results, and
that the negative control fired blind at the pyramid, where no $`\lambda_4`$ is defined. The records are
the [task](https://github.com/openwave-labs/openwave/blob/b0b078678ca75ad31b8813806d6b61a0a386d1e0/openwave/xperiments/m8_mit/research/tasks/m8_10_task_details.md)
and the [method note](https://github.com/openwave-labs/openwave/blob/b0b078678ca75ad31b8813806d6b61a0a386d1e0/openwave/xperiments/m8_mit/research/findings/m8_10_method_note.md).

### The local branch germs (M8.11)

The theorem of Section 8.3 is an audited argument. The run graded it step by step: every step of the
existence theorem was graded ESTABLISHED, the identification step with one supplied step, an analytic
reparametrisation, and every other graded statement was ESTABLISHED but one: the sign step of the
$`\lambda_4`$ lemma, graded a DEFECT and overruled with its reason recorded, as Section 8.3 describes.
One discrepancy between the run's documents is recorded here rather than resolved: the method note lists
the weight states $`v_1`$ and $`v_2`$ as "out of scope by the task's own statement", while the frozen
task says they are "covered by T, not expanded or scored". Section 8.3 follows the frozen task, which is
the pre-registration. The records are the
[task](https://github.com/openwave-labs/openwave/blob/b0b078678ca75ad31b8813806d6b61a0a386d1e0/openwave/xperiments/m8_mit/research/tasks/m8_11_task_details.md)
and the [method note](https://github.com/openwave-labs/openwave/blob/b0b078678ca75ad31b8813806d6b61a0a386d1e0/openwave/xperiments/m8_mit/research/findings/m8_11_method_note.md).

### The census (M8.12)

The census of Section 7.2 was reproduced in two blind rooms working from one packet, again on the
maintainer's own route, and under an adversarial audit that wrote its own code. The adjudication
records every claim reproduced, none defective, the classification's arguments sound in both rooms,
and one clause unresolved: the uniqueness of the maximum, which the run reproduced in value and
attainment only. Its frozen table gives an exact representative of every census orbit, and
the certificates section below uses those representatives as controls. The records are the
[task](https://github.com/openwave-labs/openwave/blob/b0b078678ca75ad31b8813806d6b61a0a386d1e0/openwave/xperiments/m8_mit/research/tasks/m8_12_task_details.md)
and the [method note](https://github.com/openwave-labs/openwave/blob/b0b078678ca75ad31b8813806d6b61a0a386d1e0/openwave/xperiments/m8_mit/research/findings/m8_12_method_note.md).

### The maximum (M8.13)

The uniqueness of the maximum was audited in a run of its own. An offline auditor reached the complete
maximiser set by its own route before it saw the author's, then graded the author's argument part by
part: ten verdicts, no gap and no defect. The adjudication records the uniqueness as an audited
argument, with the branch analysis of step 3c, the equality locus of $`M_2`$, the whole of step 3d and the
eigenspace computation of step 3e supplied by the auditor. Four independent derivations of the equality
set agree. The adjudication also records what it did not verify. The pre-registration's own
instruments were withheld by design until the author's package landed, so, in its words, "the gate's
97 checks and the mutation suite's 66 arms remain the author's report"; and the note's attribution of
the nematic bound was not checked against its sources. The package has since landed,
[with those instruments](https://github.com/openwave-labs/openwave/blob/b0b078678ca75ad31b8813806d6b61a0a386d1e0/openwave/xperiments/m8_mit/research/scripts/m8_13_author/MANIFEST.md),
and Section 9.2 attributes the bound from the sources themselves. The records are the
[task, with the adjudication](https://github.com/openwave-labs/openwave/blob/b0b078678ca75ad31b8813806d6b61a0a386d1e0/openwave/xperiments/m8_mit/research/tasks/m8_13_task_details.md),
the [auditor's return](https://github.com/openwave-labs/openwave/blob/b0b078678ca75ad31b8813806d6b61a0a386d1e0/openwave/xperiments/m8_mit/research/m8_13/run/stage2b_return.md)
and the [author's dated correction](https://github.com/openwave-labs/openwave/blob/b0b078678ca75ad31b8813806d6b61a0a386d1e0/openwave/xperiments/m8_mit/research/scripts/m8_12_author/S0_S3_MAXIMUM_CORRECTION.md).

Section 7.3 carries that argument as a complete proof, restructured in five named places, with a
dagger on each step the audit supplied, one-line facts included. The three records list different
items: (A) the auditor's return, (B) the adjudication's list, on which the maintainer's independent
grading and the auditor's agree, and (C) the author's correction, which summarises (B). The dagger means
one thing, that the audit supplied the step, and Section 7.3 marks the union of (A) and (B) where it
uses the step. The table maps each of the 24 daggers to all three, so a reader holding any one record
can match every mark. The records write $`Q`$ for the trace-free nematic tensor, which is
$`\mathring{\mathcal{N}}`$ here.

| # | where | supplied step | (A) | (B) | (C) |
| --- | --- | --- | --- | --- | --- |
| 1 | Step 1 | the five functions are invariant quartics of bidegree (2,2) | S1.2 (for $`\lVert\rho_6\rVert^2`$) | row 1, "invariance of each of the four functions" | not listed |
| 2 | Step 1 | the identification with invariant hermitian forms on $`\mathrm{Sym}^2 V_3`$, with injectivity | S1.1 | not listed (its note records the same one-line proof for the auditor's own stage-1 argument) | not listed |
| 3 | 3a | $`\mathrm{Tr}\,\mathcal{N} = 12`$ | S3a.1 | not listed | listed only among what the checker does not gate |
| 4 | 3a | $`\mathrm{Tr}(QE) = \langle u, A_E u\rangle`$ | verified in 3a, not listed as supplied | row 3a | not listed |
| 5 | 3a | $`\lVert Q\rVert = \max_E \mathrm{Tr}(QE)`$, both halves | S3a.2 | row 3a | "the variational identity" |
| 6 | 3a | rotating $`E`$ conjugates $`A_E`$ | S3a.3 | row 3a | "the equivariance" |
| 7 | 3a | the block basis and entries | S3a.5 | row 3a | "the block basis" |
| 8 | 3b | $`a + 6b \le \sqrt6`$ on the ellipse | computed in the return's § 5, not listed as supplied | row 3b $`M_1`$ | "the on-ellipse maxima" |
| 9 | 3b | $`\lvert a\rvert \le \sqrt{3/2}`$ on the ellipse | S3b3.2 | row 3b $`M_3`$ | "the on-ellipse maxima" |
| 10 | 3b $`M_1`$ | the squaring and homogenising algebra, written out | 3b $`M_1`$, Supplied | not listed | not listed |
| 11 | 3b $`M_1`$ | the second squaring is reversible when $`a + 6b > 0`$ | 3b $`M_1`$, Supplied | not listed | not listed |
| 12 | 3b $`M_3`$ | $`\lambda_{\max} = -2a + \sqrt{30 - 16a^2}`$ is the on-ellipse form | S3b3.1 | row 3b $`M_3`$ | not listed |
| 13 | 3b $`M_3`$ | $`30 - 16a^2 \ge 6`$, so the radicand stays positive | S3b3.3 | row 3b $`M_3`$ | not listed |
| 14 | 3c | the branch $`a + 6b \le 0`$ has no equality point | S3c.3 | row 3c | listed |
| 15 | 3c | the sign conditions are forced | S3c.2 | row 3c | listed |
| 16 | 3c | the equality locus of $`M_2`$, by reflection | S3c.1 | row 3c | listed |
| 17 | 3c | the locus of $`M_3`$ meets the ellipse, so $`M_3`$ attains the bound | S3c.4 | row 3c | listed |
| 18 | 3d | the whole $`E^{*} = Q/\lVert Q\rVert`$ chain | 3d, Supplied in full | row 3d | listed |
| 19 | 3e | the spectrum, top eigenspace exactly $`\mathrm{span}\{v_3, v_{-3}\}`$ | 3e, Supplied | row 3e, "and its multiplicity two" | listed |
| 20 | 4 | $`f = (0, 0, 3(\lvert\alpha\rvert^2 - \lvert\beta\rvert^2))`$ on the span | step 4, Supplied | not listed | not listed |
| 21 | 4 | $`\lVert B_0\rVert^2 = 1/7`$ follows at $`\lvert\alpha\rvert = \lvert\beta\rvert`$ | step 4, Supplied | not listed | not listed |
| 22 | 4 | $`\lVert B_0\rVert^2 = 4\lvert\alpha\beta\rvert^2/7`$ on the span | not listed (only the balanced value is computed) | row 4 | listed |
| 23 | 4 | the profile $`\widehat{r}_6 = 463/924 - (\lvert\alpha\rvert^2 - \lvert\beta\rvert^2)^2/2`$ on the span | step 4, Supplied ("the strictness") | not listed | not listed (its second refinement states the same profile as $`2\lvert\alpha\rvert^2\lvert\beta\rvert^2 + 1/924`$) |
| 24 | 4 | the relative phase is a rotation about the axis | step 4, Supplied | not listed | not listed |

Three supplied steps are not used, because Section 7.3's proof goes another way at each:

| supplied step | (A) | (B) | (C) | why Section 7.3 does not need it |
| --- | --- | --- | --- | --- |
| $`\mathrm{U}(1)`$-invariance forces bidegree (2,2) | S1.3 | row 1, "the $`\mathrm{U}(1)`$ type restriction" | listed | Step 1 works in bidegree (2,2) from the start, as Proposition 6.1 does |
| the swap of the two maxima | S3a.4 | row 3a | listed | 3a argues sufficiency, $`\lVert Q\rVert \le \max_E \lambda_{\max}(A_E)`$, not equivalence |
| the homogeneous $`M_1`$ inequality holds for all $`(a, b)`$ | 3b $`M_1`$, Supplied (a remark) | not listed | not listed | Section 7.3 uses it on the ellipse only |

The proof departs from the audited note in five places. Step 1 goes through Proposition 6.1, in bidegree
(2,2) throughout, with the basis
$`\lVert u\rVert^4, \lvert f\rvert^2, \lVert B_0\rVert^2, \mathrm{Tr}\,\mathcal{N}^2`$ and
$`B_0 = -\langle\Theta u, u\rangle/\sqrt7`$ in place of Kawaguchi and Ueda's $`a_{00}`$. Step 3a proves
sufficiency, so the swap of the maxima drops out. The basis of 3a carries a sign on its fourth vector
that makes $`M_2`$ literally $`M_1`$ at $`-b`$. Step 3b proves the two ellipse bounds by identities,
$`6N^2 - (a + 6b)^2 = 3(a - 2b)^2`$ and $`(3/2)N^2 - a^2 = 12b^2`$, where the audit supplied them as
computed maxima; the daggers mark the bounds, not these proofs. Step 4 keeps the note's own argument and
adds the supplied profile as its explicit form. Unchanged from the note, and without daggers: step 2 and
the bound of $`M_2`$, both graded ESTABLISHED as written, the eigenvalue formula of $`M_1`$, the two
identities of 3b that the note uses (a sum of squares and a completed square), the three equality loci
and the statement of 3c's conclusion.

Two steps the audit supplied to the maximum argument also appear in Section 6. Proposition 6.1's proof
uses the identification of invariant quartics with invariant hermitian forms on $`\mathrm{Sym}^2 V_3`$,
which the audit supplied to the author's argument, and Section 6.2 states the spin-3 identity
$`\mathrm{Tr}\,\mathcal{N} = 12`$, another step the audit supplied to that argument. Section 6 is
self-contained and carries no daggers; the daggers in Section 7.3 mark both steps within the audited
argument. Step 1 of that proof works in bidegree (2,2) from the start, as Proposition 6.1 does, so the
audit's restriction from $`\mathrm{U}(1)`$-invariance to that bidegree is not used.

---

## The certificates of Section 7.2

The three orbits of Section 7.2 outside the census's class are certified by this paper, in 60-digit
interval arithmetic; the certificates are its own computation, not a reproduction. They are published
with their scripts in [one folder](/files/framework/files/bedrock/files/scripts/surviving-ray-v2/), in
two layers.

The record is the certification as it ran, unmodified. Its three work items were fixed in advance by
frozen packets, published with the scripts and their logs, and the two runs after them, the
one-certificate rows and the export of the boxes, are marked as supplements. Each log opens with the
SHA-256 of its script and of the files it rests on, and the second work item's failed first run, stopped
by a control, is kept beside its second. The certificates start from points of an exploratory numerical
census, which the first packet pins by hash and which is not distributed, so the archived scripts are not
meant to be rerun. A certificate does not depend on where its starting point came from: given the system
and the box, the Krawczyk inclusion holds or it does not.

The reproduction is what a reader reruns. The data file gives, for each orbit, the fixed set of its
full isotropy, its slices, the box centre recorded to 64 digits and the radius, $`10^{-55}`$. The verifier
rebuilds each system from that data and repeats the Krawczyk test, both bounds on the isotropy, the
signatures and the value enclosure. Its controls start from the census's exact representatives
[M8.12], not from boxes: the model's values at the four weight states; the six census orbits with
finite stabilisers, each certified from its exact point with the exact signature and value the census
records; the pyramid and the prism in their own fixed sets, with isotropy of orders 10 and 12 and their
line extrema; and the D2 ray's isotropy, of order 8. Planted failures, each on a passing parent, are
caught. Each statement of Section 7.2 maps to the log lines that give it:

| Section 7.2 says | as run | re-checked |
| --- | --- | --- |
| each outside orbit is a critical orbit, certified in the fixed set of its full isotropy at radius $`10^{-55}`$ | `one_certificate_rows_log.txt` | `verify_certificates_log.txt` |
| the rotation stabiliser and the full isotropy of each row | `one_certificate_rows_log.txt` | `verify_certificates_log.txt` |
| the three signatures of each row, and no transverse kernel | `one_certificate_rows_log.txt` | `verify_certificates_log.txt` |
| the values, and $`\mathcal{O}_2`$'s interval of width $`3.1 \times 10^{-52}`$ containing $`28800/121`$ | `one_certificate_rows_log.txt` | `verify_certificates_log.txt` |
| the census's exact full signatures at the pyramid, the prism and the D2 ray, from their own fixed sets | `one_certificate_rows_log.txt` | `verify_certificates_log.txt`, the pyramid and the prism |
| the same at all six census orbits with finite stabilisers, from the whole sphere | `certify_inertia_log.txt` | `verify_certificates_log.txt` |

Five exact checks accompany them, each with its log, of arguments the text gives itself: Proposition 6.1,
the line extrema of Section 7.2, Lemma 7.3 with the minimum, the steps of the maximum, and the prior
diagrams of Section 9.2. The folder's `SHA256SUMS` lists the SHA-256 of the 29 other files in it, and
`shasum -a 256 -c SHA256SUMS` checks them; the manifest's own SHA-256 is
`c4086a985e55cb91aeb7af764a06d9409f281def494479845e0924d3eec399b4`.

---

## Changes from the first version

The first version stays deposited as it was. This one extends it.

- **Moved.** The first version's Section 5.8 is Section 7.1 here, and its Lemmas 5.3 and 5.3(b) are
  Lemmas 7.1 and 7.2. Its Section 6 grows into Section 8, and its Section 7 is revised as Section 9. Its certification
  block is carried at the end, as before, with its opening scoped to the claims that run reproduced.
- **Carried with cross-reference updates.** Sections 2 to 5, less the section that moved, and apart from
  three sentences, two in Section 2.5 and one in Section 3, that now name the sections this version adds;
  the first version's numbers are kept, so there is no Section 5.8.
- **Rewritten.** Section 1.
- **New.** The selected point (Section 6); the census within its class, the three certified orbits
  outside it and the extremes (Sections 7.2 and 7.3); the first correction and the local branch germs
  (Sections 8.2 and 8.3); and, at the end, the records of the runs behind Sections 7 and 8 and of this
  paper's certificates.
- **What the first version said and this one does not.** It left the critical set unclassified and did
  not show that $`463/924`$ is the global maximum. Section 7.2 classifies the critical orbits within a
  stated class and certifies three outside it, and Section 7.3 answers the maximum at spin 3
  (Theorem 7.5). It also gave the Majorana polynomial of $`v_2`$ as $`z^5`$, which up to scale is that of
  $`v_{-2}`$; it is $`-\sqrt6\,z`$, as Section 9.2 now says.

---

/ **[`↑top`](#top)** / **[`main`](https://github.com/dmobius3/mode-identity-theory/tree/main/)** / **[`framework`](/files/framework/)** / **[`bedrock`](/files/framework/files/bedrock/)** / **[`working`](/files/framework/files/working/)** / **[`cosmos`](/files/cosmos/)** / **[`spectrum`](/files/spectrum/)** / **[`tools`](/files/tools/)** /
