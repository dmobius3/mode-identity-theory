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
built from $`\psi\psi^{T}`$, is filtered by the same mechanism onto a different plane. A block state
at level 6 carries left spin 3 and a right index in a representation $`\sigma`$ of the binary
icosahedral group, and its density is a function on the quotient, so a channel of rank $`K`$
survives only when $`V_K`$ carries a $`2I`$-invariant. The density's left content spans ranks 0
through 6, that is levels 0 through 12, and inside that closed window exactly two carry one, at
$`K = 0`$ and $`K = 6`$. The quartic functional reduces with the interaction, to an affine function
of the top multipole $`\lVert \rho_6 \rVert^2`$ whose coefficient is not fitted but given in closed
form by the branching, and positive because both constituents are proper. The weight
$`\lVert R_6 \rVert^2`$ that produces it takes the same value in both sectors, because they are
complementary in $`\dim V_3 = 7`$; the normalised coefficient itself does not, and the two are
distinguished in Section 5.3. Separately, and with no icosahedral input at all, the spin-8 cubic
channel built from the same spin-3 data, of binary order 16, closes exactly on the
time-reversal-invariant rays: its zero set is $`U(1) \cdot \mathrm{Fix}(\Theta)`$, equivalently the
rays whose Majorana constellation is antipodally symmetric as a multiset. The ingredients are
classical: the Jacobian criterion for nonzero binary forms of equal degree, the Majorana
representation with its time-reversal reading, and Peter-Weyl on $`S^3`$. The result established
here is the channel filter and the selection it forces for that interaction, together with an
accounting of which parts of the surrounding arithmetic are icosahedral and which are universal
facts about spin 3 with time reversal.

---

## 1. Introduction

Spin-3 states carry a well-studied geometry. The Majorana representation sends a state to six points
on the sphere, rotations act on the constellation, and a substantial literature studies the
constellations that extremise natural invariants: the anticoherent states, whose low multipoles
vanish, and the polyhedral configurations that realise them. Barnett, Turner and Demler [BTD]
enumerate six-vertex spin-3 phases in that language. Within this setting the invariant quartics of a
spin-3 state form a four-dimensional space, and particular members of that family have been studied
along with the symmetric constellations attached to them. Any statement about a particular quartic
is therefore a statement about a member of a family the community will already recognise.

The question here is not which member is interesting but which member a geometry permits *for a
given interaction*. Modes on the spherical space form $`S^3/2I`$ organise into flat bundles indexed
by representations $`\sigma`$ of the binary icosahedral group. At level 6 a block state has left
spin 3, so its self-interaction lies in the four-dimensional family above; the question is what the
quotient does to that family. The answer is a filter. The density $`\lvert\psi\rvert^2`$ of a
section is a genuine function on $`S^3/2I`$, and by Peter-Weyl its level-$`2K`$ component factors
into a left multipole, built from the spin-3 data alone, and a right multipole, which lives in the
$`2I`$-invariants of $`V_K`$. Those invariants first appear at level 12 and next at level 20, so
across ranks 0 through 6 exactly two channels are open. Everything else is switched off, not because
the left-hand tensor vanishes, which it does not, but because its right-hand coefficient does.

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
in the classical invariant-theory literature is left open in Section 7 rather than settled here.

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

One boundary should be drawn explicitly. The configurations appearing below are known: the
octahedral constellation is the anticoherent state of order 3 in the standard classification, and
critical rays occur here with all four of the six-vertex shape types [BTD] names. Recognising a
configuration is not the same as selecting it, and *configuration prior art is not selection prior
art*. The contribution is which member of a known family a specific geometry forces, and the
surrounding accounting of what that forcing does and does not explain.

Two of the limits above are of record rather than of proof, and belong in one place. The sentences
naming the constellation literature rest on abstracts and not on bodies, and the search behind them
is reported as a search and not as a novelty finding (Section 7.3); the [BTD] count of six-vertex
phases is provisional pending a first-hand reading of that paper's body (Section 7.2). The
anticoherence fact used below is not taken on trust from that literature, and Section 5.8
establishes it here.

Section 2 fixes the state space and the time reversal, then the quotient's sectors and invariant
degrees and the interaction the rest of the paper uses. Its one transform is fed three different
arguments, not two. Section 3 gives the ambient proposition. Section 4 records the reduction that
isolates the four-dimensional family and states what it can and cannot touch. Section 5 proves the
selection theorem, computes the surviving weight, states the normalisation's own ceiling, connects
the ambient channel back to the quotient, maps the critical geometry the theorem leaves open, and
derives consequences across levels and sectors. Section 6 reads the result as a Lyapunov-Schmidt
interpretation, with its ceilings stated. Section 7 collects the discussion, the prior art, the open
historical question, and the limits of the arithmetic account.

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
Section 5.8 require. Statements about constellations below are statements about rays.

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

Everything below concerns one interaction, fixed here so that Sections 4, 5 and 6 read off a single
definition rather than three. The problem is

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
move the tangential critical equation. So $`g = 1`$ is taken throughout, a normalisation rather than
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
appeared previously is left open in Section 7. Nothing in the paper's contribution rests on the
answer, since that contribution is the channel selection of Sections 4 and 5.

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
Section 2.4 leave exactly two survivors, at levels 0 and 12.

> **Lemma 4.1.** The density of a block state at level 6 has the form
>
> ```math
> \lvert\psi\rvert^2 \;=\; c_0 \;+\; d_{12} ,
> ```
>
> a constant plus a level-12 component. No intermediate level occurs.

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
exact computation. That is a separate fact and is not used below.

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
multiplicity-free such $`T`$ form a real four-dimensional space. The seven quartics span it, so they
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
is lost this way. Section 7.5 obtains the same relationship structurally, as an equivariant
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

### 5.8 The critical rays of the reduced quartic

Clause 5 of Theorem 5.1 is what this subsection resumes, after the normalisation ceiling and the
spin-8 payoff: the quartic is affine in $`\lVert\rho_6\rVert^2`$ alone, so its critical rays are
those of $`\lVert\rho_6\rVert^2`$ on the unit sphere in $`V_3`$, and since $`w_6 > 0`$ the maximiser
of one is the maximiser of the other. Both are questions about spin 3 with time reversal and neither
mentions $`2I`$. Four values, with $`\binom{12}{6}\lVert\rho_6\rVert^2`$ quoted as an integer:

| ray | constellation | $`924\,\lVert\rho_6\rVert^2`$ |
|---|---|---|
| $`v_3`$ | coherent, six coincident points | 1 |
| $`v_0`$ | zonal | 400 |
| $`(v_2 + v_{-2})/\sqrt{2}`$ | octahedron | 288 |
| $`(v_3 + v_{-3})/\sqrt{2}`$ | hexagon | 463 |

Those four rays are critical, which the table alone does not show.

> **Lemma 5.3.** Each of the four rays above is a critical point of $`\lVert\rho_6\rVert^2`$ on the
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
rather than at an isolated fixed point, so Lemma 5.3 does not cover them as stated and needs a
second clause.

> **Lemma 5.3(b).** Suppose the $`\chi`$-isotypic space of $`H`$ is two-dimensional, so the fixed
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
$`\lVert\rho_6\rVert^2`$ is constant transverse to the real curve and Lemma 5.3(b) applies along it;
the criterion confirms it, with $`M_6(u) = -\tfrac{9}{455}\sqrt{91}\,u`$. Its Majorana polynomial is
$`z(a + bz^5)`$ with $`a, b \neq 0`$, so the constellation is one point at a pole and five in a
ring, six distinct points: a non-degenerate pentagonal pyramid. The endpoints $`t = 0`$ and
$`t = \pi/2`$ are stationary too, but they are the weight states $`v_2`$ and $`v_{-3}`$, already
covered by Lemma 5.3; the interior point is the one this line contributes.

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
both directions and Lemma 5.3(b) applies along either axis. The rotation $`R_z(\pi/3)`$ acts on the
chart by $`z \mapsto -z`$, so the two signs in each pair are one orbit and the five points are three
orbits.

The point the chart omits is critical as well, and it is not a new ray. It lies on this locus
because $`v_0`$ spans one of the two $`\chi`$-isotypic directions, and it is critical by Lemma 5.3,
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
and not an antiprism, at heights $`\pm 0.5585\ldots`$. At $`y^2 = 5/2`$, $`s = i\sqrt{50}`$ and the
two roots are purely imaginary of opposite sign, with arguments $`+\pi/2`$ and $`-\pi/2`$; dividing
the difference of $`\pi`$ by three, the azimuths differ by $`60^\circ`$: the two are **staggered**,
and there $`h = 1/\sqrt{3}`$ exactly. A staggered pair of equilateral triangles at heights
$`\pm 1/\sqrt{3}`$ is the **regular octahedron**, which is the same statement as its full multipole
row there, $`1/7, 0, 0, 0, 6/11, 0, 24/77`$. Its reappearance is a check rather than a coincidence:
an octahedron has a three-fold axis through opposite faces, so it has to occur in this locus. The
tabulated state is exact by the same standard, with no root-finding: its sextic is a constant times
$`z(z^4+1)`$, of degree 5, so one root sits at the far pole, one at the origin and four at the
fourth roots of $`-1`$, spaced $`90^\circ`$ apart on the equator.

The hexagonal value is the largest of the four, and it is not this paper's. Romero, Klimov,
Goldberg, Leuchs and Sanchez-Soto give the closed form
$`\varrho^2_{2S} = \tfrac12 + \binom{4S}{2S}^{-1}`$ for the top multipole of the NOON state at
integer spin $`S`$ [RK]; at $`S = 3`$ that is $`463/924`$, and their NOON state is this paper's
hexagon up to a rotation. Their normalisation is the Parseval one used here, so the numbers are
directly comparable.

The question of whether it is the global maximum of $`\lVert\rho_6\rVert^2`$ is also theirs, and
they pose it for general $`S`$: they ask what the largest attainable highest-order multipole is,
sample $`6 \times 10^4`$ random constellations, and find none exceeding the NOON value. The table
does not settle it and four exact values do not determine a global extremum. What this section adds
at that ray is not the value but its position: it is one point of an exactly determined critical set
on each of two symmetry loci. The three time-reversal-invariant rays among them are the zonal,
octahedral and hexagonal ones, and by Lemma 2.2 their odd density multipoles vanish, which is
visible in the octahedral case as anticoherence of order exactly 3: its multipoles are
$`1/7, 0, 0, 0, 6/11, 0, 24/77`$, so ranks 1, 2 and 3 vanish and rank 4 does not.

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

This does not compete with Section 6.1's remark that level 6 is fixed by the choice of object rather
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
question about spin 3 with time reversal, which is why Section 5.8 could be carried out without the
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

## 6. The Lyapunov-Schmidt reading

This section interprets Theorem 5.1 and derives nothing. Without it, the theorem is a bare statement
about a quartic on a seven-dimensional space; the Lyapunov-Schmidt reading explains why that
particular quartic on that particular space is worth extremising.

### 6.1 The setting

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
critical rays of $`Q`$ are then the **critical directions of the leading reduced problem**, and not
solution branches: an actual branch requires the range equation described in Section 6.2, which is
not carried out. Section 5.8 records several symmetry-distinguished examples among them.

### 6.2 Two ceilings

**This is not a classification of the critical directions.** Section 5.8 lists critical rays that
are distinguished by their symmetry and are known in exact form. There is no theorem here that they
exhaust the critical set of $`Q`$ on the unit sphere, and numerical exploration locates critical
points beyond them. What is offered is a list of symmetry-distinguished critical directions, not a
classification, and no count is claimed.

**This is not a claim that the reduction is exact.** In a Lyapunov-Schmidt construction carried
through, the range equation is solved for the transverse component as a function of the kernel
variable, and that solution is substituted back, contributing corrections to the reduced equation at
higher order in the amplitude. Those corrections are not computed here and the transverse component
is not discarded by any argument; it is simply not treated. What is exact is the finite-dimensional
problem on the degenerate eigenspace at leading cubic order, which is what Sections 4 and 5
establish. Calling the result an exact reduction would overstate it by exactly one step, and that
step is the range equation.

### 6.3 What the reading is for

Everything in Sections 3 through 5 stands without this section. Proposition 3.3 is a statement about
binary sextics, Theorem 5.1 a statement about a four-dimensional space of equivariant maps and which
of them a quotient permits for the interaction of Section 2.5. Neither is a statement about the
dynamics that interaction came from. The Lyapunov-Schmidt language supplies the reason for the
question and makes the two ceilings above legible as ceilings rather than as omissions: it
identifies which parts of a complete bifurcation analysis are here and which are not.

The method itself is standard and is used rather than developed; the reduction from a degenerate
eigenspace is classical [GS] and no property of it is proved below.

---

## 7. Discussion

### 7.1 What is not claimed

Five limits are collected here rather than left scattered across the sections.

The critical set of $`Q`$ on the unit sphere is not classified: the rays recorded in Section 5.8 are
not shown to exhaust it, for the reasons given in Section 6.2. Relatedly, the value
$`463/\binom{12}{6}`$ is the largest of the four tabulated and is not shown to be the global
maximum. That question is not this paper's to begin with: it is posed for general spin in [RK],
probed numerically there, and not settled.

The Lyapunov-Schmidt reduction is not carried out: the range equation is untreated, for the reasons
given in Section 6.2.

The four shape types are located, but not matched to [BTD]'s phase orbits. Rays of all four types
that paper names are found in Section 5.8. Identifying them with its phase orbits is not attempted,
since two of the four are continuous families and the source consulted lists names rather than
representatives.

The closed form for the sector normalisation carries a ceiling of its own, stated with the formula
in Section 5.6 and not repeated here.

Everything above concerns a single block state in a single sector. No statement is made about a
field occupying distinct flat-bundle sectors at once, or about a nonlinearity coupling one sector's
density to another's amplitude. Corollaries 5.5 and 5.6 compare the two sectors; they do not
describe a configuration containing both. The mixed problem is not posed here, let alone solved.

### 7.2 Prior art, and where the boundary falls

The configurations appearing in Section 5.8 are known objects, and the three statements about them
have different provenance, so they are given separately rather than as one prior-art paragraph.

*The octahedral state is anticoherent of order exactly 3.* The lower bound is prior art in a clean
form: Crann, Pereira and Kribs [CPK] prove that a Majorana constellation which is both the orbit of
a finite subgroup of $`\mathrm{O}(3)`$ and a spherical $`t`$-design gives an anticoherent state of
order $`t`$, and the octahedron is both, at $`t = 3`$. That statement is a one-way implication and
carries the group-orbit hypothesis, so it bounds the order below and not above. The **sharpness is
computed in Section 5.8** and does not follow from it: the multipole row is
$`1/7, 0, 0, 0, 6/11, 0, 24/77`$, so rank 4 is nonzero and the order is exactly 3 rather than at
least 3.

*Critical rays occur here with all four of the shape types [BTD] names*: the hexagon at $`463/924`$,
the octahedron at $`288/924`$, the pentagonal pyramid at $`9/35`$ and the trigonal prism at
$`200/903`$, the last two found in Section 5.8 on symmetric loci rather than at isolated points.

That is a statement about shape types and not yet about that paper's phase orbits, and the
difference is real. "Pentagonal pyramid" is not one ray but a one-parameter family, a pole plus a
ring at any latitude, of which Section 5.8 selects one; the eclipsed prisms likewise carry a
continuous shape parameter. Matching a ray to a phase would mean comparing representatives, and the
source consulted here is an abstract, which lists shape names and no parameters. So the four-way
correspondence is at the level of type, and is stated at that level. The list of four, the hexagon,
the pentagonal-base pyramid, the prism and the octahedron, is stated in that paper's own abstract,
which is therefore the source for it; its body has not been read, and no claim here rests on the
body.

The type count is four and complete, since [BTD] names four. One identification is worth stating,
because the natural guess is wrong: the pyramid is *not* the weight state $`v_2`$, whose Majorana
polynomial is $`z^5`$, giving five coincident points and one antipodal, a degenerate configuration
rather than a polyhedron. It occurs at an interior point of the line through $`v_2`$ and $`v_{-3}`$,
at neither end.

None of this classifies the critical set, which remains open: it contains rays of those types and
others besides. Every weight state is critical, and the seven of them realise four distinct values
of $`\binom{12}{6}\lVert\rho_6\rVert^2`$, namely 1, 36, 225 and 400.

*The hexagonal value and the question attached to it are prior art.* Romero, Klimov, Goldberg,
Leuchs and Sanchez-Soto give $`\varrho^2_{2S} = \tfrac12 + \binom{4S}{2S}^{-1}`$ for the top
multipole of the NOON state [RK], which at $`S = 3`$ is the $`463/924`$ tabulated above, their NOON
state being this paper's hexagon up to a rotation. They also raise the question of the largest
attainable top multipole and probe it numerically without settling it. Both the value and the
question therefore belong to them, and Section 5.8 says so where it records them. What is not in
that paper is the critical set: they ask which state maximises the top multipole, while Section 5.8
solves for every critical point on two symmetry loci and finds the hexagon sitting among five
others.

Recognising a configuration is not the same as selecting it. The result established here is which
member of a known family a specific quotient forces, and the boundary between those two things is
the reason Section 3 is billed as a proposition and Section 5 as a theorem.

### 7.3 The search, stated as a search

Two searches were run at different times and they are in different conditions, so they are reported
separately.

The first asked whether the results of Section 3 are known. The polarised identity of Section 3.1
and the zero-set statement of Proposition 3.3 were not located. Every reference below was verified
against its publisher or preprint record rather than from recall, and one gap closed in the process:
the order-3 lower bound has a clean source in [CPK], which the first pass had not surfaced.

The second asked the question the contribution actually rests on, whether the selection statement of
Section 5 has been made before. It ran ten queries across six lines of approach: nonlinear
Schrodinger and semilinear elliptic problems on spherical space forms; equivariant bifurcation with
icosahedral symmetry; harmonic analysis on the Poincare dodecahedral space; spin-3 spinor
condensates and their interaction channels; anticoherent states and multipoles from Majorana
constellations; and symmetry selection rules for nonlinear couplings. Four sources were then read
rather than skimmed.

Nothing was found that filters a cubic interaction by a finite subgroup on a space form, and nothing
that puts $`\lvert\psi\rvert^2\psi`$ on a flat bundle over $`S^3/2I`$. Three adjacencies were found
and are now cited where they belong rather than here: the four-dimensional family is the known
four-channel spin-3 interaction [DH], [KU]; the transform of Section 2.3 is the standard
state-multipole expansion [Fa], [RK]; and the hexagonal value $`463/924`$, together with the
global-maximum question attached to it, is prior art [RK]. The last of those was a headline number
of Section 5.8 and is now attributed.

What the second search does not establish is also worth saying. **Not surfaced is not the same as
new.** Ten queries and four papers amount to a real search, not an exhaustive one. Three gaps are
known: the equivariant bifurcation literature is largely in monographs that search engines index
poorly; the older invariant-theory literature was not worked; and no subscription index was used,
which is the instrument the question really wants. Section 7.2 gives the per-item status of the
prior-art statements rather than a blanket one, because the items are in different conditions.

### 7.4 The open historical question

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

### 7.5 Where the family sits

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

That framing also explains the shape of the paper. Almost everything on the way to the answer is
universal: the four-dimensional family, the canonical basis, the operator structure and its
alternating row, the forced time-reversal phase, and the critical geometry of the surviving channel.
For Theorem 5.1 the quotient supplies two facts, the invariant-degree filter and the
multiplicity-free complementary branching, and those two are the whole of its icosahedral content;
the branching is one statement doing two jobs, scalarisation and weight. Branching computations
appear elsewhere for other purposes, in Section 4.3 for the availability of the spin-8 target and in
Section 6.1 for the first occurrence of each sector, and neither feeds the theorem. Chronologically
the icosahedron came first and led to the ambient proposition rather than requiring it, but the
logical dependence runs the other way, and the paper is ordered by the logic.

---

## References

- **[BTD]** R. Barnett, A. Turner and E. Demler, Classifying novel phases of spinor atoms. *Phys. Rev. Lett.* **97** (2006), 180412; arXiv:cond-mat/0607253.
- **[CPK]** J. Crann, R. Pereira and D. W. Kribs, Spherical designs and anticoherent spin states. *J. Phys. A: Math. Theor.* **43** (2010), 255307.
- **[DH]** R. B. Diener and T.-L. Ho, $`^{52}`$Cr spinor condensate: a biaxial or uniaxial spin nematic. *Phys. Rev. Lett.* **96** (2006), 190405; arXiv:cond-mat/0511751.
- **[Fa]** U. Fano, Description of states in quantum mechanics by density matrix and operator techniques. *Rev. Mod. Phys.* **29** (1957), 74.
- **[GS]** M. Golubitsky and D. G. Schaeffer, Singularities and Groups in Bifurcation Theory, Volume I. Applied Mathematical Sciences **51**, Springer (1985).
- **[GY]** J. H. Grace and A. Young, The Algebra of Invariants. Cambridge University Press (1903).
- **[KU]** Y. Kawaguchi and M. Ueda, Symmetry classification of spinor Bose-Einstein condensates. *Phys. Rev. A* **84** (2011), 053616; arXiv:1109.0400.
- **[Maj]** E. Majorana, Atomi orientati in campo magnetico variabile. *Nuovo Cimento* **9** (1932), 43.
- **[RK]** J. L. Romero, A. B. Klimov, A. Z. Goldberg, G. Leuchs and L. L. Sanchez-Soto, Multipoles from Majorana constellations. *Phys. Rev. A* **109** (2024), 012214; arXiv:2401.07904.

---

## Citation

```
Shatto, B. (2026).
The Surviving Ray: channel selection for a cubic self-interaction on S³/2I.
Zenodo.
https://doi.org/10.5281/zenodo.22681501
```

---

## Independent numerical certification

[![OpenWave](/files/assets/openwave-banner-graphite.svg)](https://github.com/openwave-labs/openwave/blob/main/openwave/xperiments/m8_mit/research/findings/m8_1_2_method_note.md)

The results of this paper have been reproduced on the OpenWave M8 track by an independent, blind computation. Two agents, a solver and an auditor, built every object from its definition in their own code, working from a two-stage handout with no access to the paper, its title or any value it claims. The group entered only as the two unit quaternions that generate it, and both agents derived its order, perfectness, invariant degrees and branching from those generators instead of importing them from a recognised group. The auditor worked on disjoint primitives, with its own Racah-formula couplings, the group in exact $`\mathbb{Q}(\sqrt{5}, i)`$ arithmetic, projectors from Casimir operators and a Haar quadrature that does not use Schur orthogonality, and then tried to refute every answer the solver gave. It refuted no value: 80 of its 81 exact comparisons agreed outright, and the last differed by a change of convention that the audit proved.

All twenty-one pre-registered claims reproduced. On the ambient side, $`\mathrm{Sym}^3 V_3 = V_1 \oplus 2V_3 \oplus V_4 \oplus V_5 \oplus V_6 \oplus V_7 \oplus V_9`$ came out with no $`V_8`$, $`M_0(u) = -\lVert u\rVert^2 u/\sqrt{7}`$ is radial, and $`M_6`$ is diagonal on the weight basis with entries proportional to the squared binomials $`1, 36, 225, 400, 225, 36, 1`$. Proposition 3.3 is where the run was built to be hardest. The first stage withheld the normalisation that points toward the first transvectant, and both agents still found that route on their own and proved, rather than sampled, that the spin-8 channel vanishes exactly on the time-reversal-invariant rays.

On the quotient, the invariants among ranks 0 to 6 sit only at ranks 0 and 6, and $`V_3`$ restricts to two constituents of dimensions 3 and 4. Theorem 5.1 reproduced: the self-interaction came out as $`(d/7)\lVert u\rVert^2 u - ((7-d)/\sqrt{91})\,M_6(u)`$ in the sector of dimension $`d`$, a radial term plus a nonzero multiple of $`M_6`$, the single projective ray of clause 4, with $`\lVert R_6\rVert^2 = 12/7`$ in both sectors, $`w_0 = 7`$, $`w_6/w_0 = (7-d)/(13d)`$ and normalisations 1287 and 2288. The degree-12 invariant $`I_{12}`$ has twelve simple roots, and the transvectant map Section 5.7 builds on it is injective. The tabulated critical rays came out at $`924\,\lVert\rho_6\rVert^2 = 1, 400, 288, 463`$, the chart carries exactly five critical points, found by Gröbner elimination and confirmed by an independent Newton census, and the named shapes came out as Section 5.8 gives them: the trigonal prism and the regular octahedron on the three-fold locus, and the pentagonal pyramid at $`9/35`$. Corollaries 5.4 to 5.6 reproduced as stated, down to $`Q_{\mathbf{3}'} - Q_{\mathbf{4}} = \tfrac{49}{156}\,\widehat{r}_6`$. The second quartic, built from $`\psi\psi^{T}`$, lands on a different plane: the four maps involved have rank 4.

The audit also supplied a clarification rather than a correction. The seven multipole quartics $`\lVert\rho_K(u)\rVert^2`$ satisfy three linear relations, so the individual weights of Section 5.2 are fixed by its Peter-Weyl formula rather than by the quartic alone; that section records the point, and no reported value depends on it. This is a blind recomputation of what the paper claims, from definitions, not a second proof: the proofs were not checked line by line, the run stops at level 6 and at the two interactions built there, the general-spin constant of Section 5.9 was left out of the claims because checking several spins does not verify a formula in $`j`$, and no dynamics was run. The [method note](https://github.com/openwave-labs/openwave/blob/main/openwave/xperiments/m8_mit/research/findings/m8_1_2_method_note.md) carries the full record.

---

/ **[`↑top`](#top)** / **[`main`](https://github.com/dmobius3/mode-identity-theory/tree/main/)** / **[`framework`](/files/framework/)** / **[`bedrock`](/files/framework/files/bedrock/)** / **[`working`](/files/framework/files/working/)** / **[`cosmos`](/files/cosmos/)** / **[`spectrum`](/files/spectrum/)** / **[`tools`](/files/tools/)** /
