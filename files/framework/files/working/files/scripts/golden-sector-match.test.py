#!/usr/bin/env python3
"""golden-sector-match.test.py -- OPH's golden triplets as the adjoints of the two flat SU(2) connections on S^3/2I (2026-09-11).

Companion to s3-2i-oph-dictionary.md. Reads OPH's committed Lean tables
(github.com/FloatingPragma/observer-patch-holography) at a pinned commit as data, executing
nothing from OPH, and builds the binary icosahedral group 2I as 120 exact unit quaternions over
Q(sqrt5). Exact arithmetic throughout; standard library only. Checks:

  1. OPH tables: the sixty port rotations (A5PortAction.perms), the committed adjacency
     (PortFrameGram.neighbors), the twenty oriented faces (LocalFaceMaxwellAction.faceVertices,
     equal to CoreAxioms.orientedFaces), and goldenPlusZ, goldenMinusZ (GoldenSectorCharacters
     plusA/plusB, minusA/minusB: twenty times the golden projectors, entries a + b*phi). The
     character facts GoldenSectorCharacters proves are reproduced: values by element order,
     Galois conjugation, the squaring rule, equivariance, the 12/12 split.
  2. The committed port frame (PortFrameGram, entries by graph distance) has, rotation by
     rotation, the character of W-, the image at lambda- = 3 - sqrt5.
  3. 2I closes at 120 elements, Ad Q preserves the icosahedron with vertices at the cyclic
     permutations of (0, +-1, +-phi), and chi(Sym^2 Q) = (tr Q)^2 - 1 takes 3, -1, 0 on the
     elements acting with order 1, 2, 3.
  4. The bridge. An order-five rotation is one-step when it moves each neighbour of its fixed
     vertex to an adjacent neighbour, a property every graph isomorphism preserves. On both
     sides the character is phi on one-step rotations and 1 - phi on two-step ones, so
     Sym^2 Q = W- and, by Galois conjugation, Sym^2 Q' = W+.
  5. faceNormalZ is 3I minus the face adjacency, and N goldenPlusZ = (3 + sqrt5) goldenPlusZ,
     N goldenMinusZ = (3 - sqrt5) goldenMinusZ, entrywise.
  Mutation arms, each run after its parent passes: comparing the port frame with W+ must break
  check 2, classifying MIT's rotations with the distance-two graph must break check 4, and
  swapping the two eigenvalues must break check 5.

Usage: OPH_CLONE=/path/to/observer-patch-holography python3 golden-sector-match.test.py [ref]
The ref defaults to the pinned commit recorded in golden-sector-match.out.
"""
import os
import re
import subprocess
import sys
from collections import Counter
from fractions import Fraction as Fr

CLONE = os.environ.get("OPH_CLONE", ".")
# Pinned to the OPH commit recorded in golden-sector-match.out; pass another ref to re-run elsewhere.
REF = sys.argv[1] if len(sys.argv) > 1 else "621edbb2a56b388b3590a5c766a59bd9d2012a17"
SHA = subprocess.run(["git", "-C", CLONE, "rev-parse", REF], capture_output=True, text=True, check=True).stdout.strip()


def show(path):
    return subprocess.run(["git", "-C", CLONE, "show", f"{SHA}:{path}"], capture_output=True, text=True, check=True).stdout


def block(text, start, end):
    i = text.index(start)
    j = text.index(end, i + len(start))
    return text[i:j + len(end)]


def fail(msg):
    raise SystemExit(f"CHECK FAILED: {msg}")


# ----------------------------- Z[phi], pairs (a, b) = a + b*phi ---------------------------
def zadd(x, y): return (x[0] + y[0], x[1] + y[1])
def zmul(x, y): return (x[0] * y[0] + x[1] * y[1], x[0] * y[1] + x[1] * y[0] + x[1] * y[1])
def zconj(x): return (x[0] + x[1], -x[1])
def zscale(n, x): return (n * x[0], n * x[1])
PHI, ONE_MINUS_PHI = (0, 1), (1, -1)
def zname(x): return {PHI: "phi", ONE_MINUS_PHI: "1-phi", (3, 0): "3", (-1, 0): "-1", (0, 0): "0"}.get(x, str(x))


# ----------------------------- 1. OPH committed tables ------------------------------------
perm_block = block(show("Lean/Screen/A5PortAction.lean"), "def perms : List (List Nat) := [", "]]")
PERMS = [tuple(int(t) for t in row.split(",")) for row in re.findall(r"\[([0-9,\s]+)\]", perm_block)]
if len(PERMS) != 60 or len(set(PERMS)) != 60: fail("perms")
nb_block = block(show("Lean/Screen/PortFrameGram.lean"), "def neighbors : Fin 12 → List (Fin 12)", "\n\n")
ADJ = {int(k): set(int(t) for t in v.split(",")) for k, v in re.findall(r"\|\s*(\d+)\s*=>\s*\[([0-9,\s]+)\]", nb_block)}
if sorted(ADJ) != list(range(12)): fail("neighbors")
fv_block = block(show("Lean/Screen/LocalFaceMaxwellAction.lean"), "def faceVertices : Fin 20 → Fin 12 × Fin 12 × Fin 12 :=", "]")
FACES = [tuple(int(t) for t in m) for m in re.findall(r"\((\d+),\s*(\d+),\s*(\d+)\)", fv_block)]
core = block(show("Lean/ObserverPatchHolography/CoreAxioms.lean"), "def orientedFaces : List (Fin 12 × Fin 12 × Fin 12) :=", "]")
if FACES != [tuple(int(t) for t in m) for m in re.findall(r"\((\d+),\s*(\d+),\s*(\d+)\)", core)] or len(FACES) != 20:
    fail("faceVertices differs from CoreAxioms.orientedFaces")
gsc = show("Lean/Screen/GoldenSectorCharacters.lean")


def matrix(name):
    b = block(gsc, f"def {name} : Matrix (Fin 20) (Fin 20) ℤ :=", "\n\n")
    rows = [[int(t) for t in r.split(",")] for r in re.findall(r"!\[([-0-9,\s]+)\]", b)]
    if len(rows) != 20 or any(len(r) != 20 for r in rows): fail(f"{name} shape")
    return rows


pA, pB, mA, mB = (matrix(n) for n in ("plusA", "plusB", "minusA", "minusB"))
PLUS = [[(pA[i][j], pB[i][j]) for j in range(20)] for i in range(20)]
MINUS = [[(mA[i][j], mB[i][j]) for j in range(20)] for i in range(20)]
if any(MINUS[i][j] != zconj(PLUS[i][j]) for i in range(20) for j in range(20)): fail("minus is not the conjugate of plus")


def cyclic_eq(x, y): return x in (y, (y[1], y[2], y[0]), (y[2], y[0], y[1]))


def face_act(p):
    out = []
    for f in FACES:
        img = tuple(p[v] for v in f)
        hit = [(g, 1) for g, t in enumerate(FACES) if cyclic_eq(img, t)] + \
              [(g, -1) for g, t in enumerate(FACES) if cyclic_eq(img, (t[0], t[2], t[1]))]
        if len(hit) != 1: fail("face image not unique")
        out.append(hit[0])
    return out


def trace(Q, p):
    total = (0, 0)
    for f, (g, s) in enumerate(face_act(p)):
        total = zadd(total, zscale(s, Q[g][f]))
    return total


def comp(p, q): return tuple(p[q[k]] for k in range(12))
IDP = tuple(range(12))


def order(p):
    k, q = 1, p
    while q != IDP:
        q, k = comp(p, q), k + 1
    return k


def fixed_vertex(p): return next(v for v in range(12) if p[v] == v)


def step_type(p, adj):
    v = fixed_vertex(p)
    w = next(iter(adj[v]))
    return "one-step" if p[w] in adj[w] else "two-step"


# Self-checks: reproduce the values GoldenSectorCharacters proves, so a parse or convention
# error cannot pass silently.
signs = Counter(s for p in PERMS for _, s in face_act(p))
chi = {p: (trace(PLUS, p), trace(MINUS, p)) for p in PERMS}
for p, (cp, cm) in chi.items():
    o = order(p)
    want = {1: [(60, 0)], 2: [(-20, 0)], 3: [(0, 0)], 5: [(0, 20), (20, -20)]}[o]
    if cp not in want or cm != zconj(cp): fail(f"character values on a row of order {o}")
    if o == 5 and chi[comp(p, p)][0] != cm: fail("chi_+(g^2) != chi_-(g)")
for p in PERMS:
    acts = face_act(p)
    if any(PLUS[acts[i][0]][acts[j][0]] != PLUS[i][j] for i in range(20) for j in range(20)): fail("projector equivariance")
five = [p for p in PERMS if order(p) == 5]
if Counter(chi[p][0] for p in five) != Counter({(0, 20): 12, (20, -20): 12}): fail("12/12 split")
print(f"OPH tables at {SHA[:8]}: 60 rows, 20 faces; face signs {dict(signs)}; proven character values, "
      f"conjugation, squaring rule, equivariance and 12/12 split all reproduced")


def w_plus(p): return (chi[p][0][0] // 20, chi[p][0][1] // 20)
def w_minus(p): return (chi[p][1][0] // 20, chi[p][1][1] // 20)


# ----------------------------- 2. the committed port frame --------------------------------
def dist(a, b):
    seen, frontier, d = {a}, [a], 0
    while b not in seen:
        frontier = [y for x in frontier for y in ADJ[x] if y not in seen]
        seen |= set(frontier)
        d += 1
    return d


G5 = {0: (5, 0), 1: (0, 1), 2: (0, -1), 3: (-5, 0)}   # 5G by graph distance, (a, b) = a + b*sqrt5
def frame_char(p):
    a = sum(G5[dist(k, p[k])][0] for k in range(12))
    b = sum(G5[dist(k, p[k])][1] for k in range(12))
    ra, rb = Fr(a, 20), Fr(b, 20)          # ra + rb*sqrt5, and sqrt5 = 2*phi - 1
    x = (ra - rb, 2 * rb)
    if x[0].denominator != 1 or x[1].denominator != 1: fail("frame character not in Z[phi]")
    return (int(x[0]), int(x[1]))


if any(frame_char(p) != w_minus(p) for p in PERMS): fail("port-frame character differs from chi(W-)")
print("\nCommitted port frame: its character equals chi(W-) (lambda- = 3-sqrt5) on all sixty rotations")
if all(frame_char(p) == w_plus(p) for p in PERMS): fail("mutation arm: the port frame also matches W+")
print("Mutation arm: comparing the port frame with chi(W+) fails, as required")

table, oph_by_step = Counter(), {}
for p in five:
    st = step_type(p, ADJ)
    table[(st, zname(frame_char(p)), zname(w_plus(p)), zname(w_minus(p)))] += 1
    oph_by_step.setdefault(st, set()).add(w_minus(p))
print("\nOPH order-five port rotations: (step, port-frame character, chi on W+ (lambda+ = 3+sqrt5), chi on W- (lambda- = 3-sqrt5)): count")
for k, n in sorted(table.items()):
    print(f"  {k}: {n}")
if oph_by_step != {"one-step": {PHI}, "two-step": {ONE_MINUS_PHI}}: fail("the step classes do not separate chi(W-)")

# ----------------------------- 3. MIT side: 2I in SU(2) as unit quaternions ---------------
# Q(sqrt5) numbers (p, q) = p + q*sqrt5 with Fractions; quaternions as 4-tuples of those.
def qa(x, y): return (x[0] + y[0], x[1] + y[1])
def qm(x, y): return (x[0] * y[0] + 5 * x[1] * y[1], x[0] * y[1] + x[1] * y[0])
def qn(x): return (-x[0], -x[1])
Z0, H = (Fr(0), Fr(0)), (Fr(1, 2), Fr(0))
PHIq = (Fr(1, 2), Fr(1, 2))                                   # phi


def hmul(x, y):
    a1, b1, c1, d1 = x
    a2, b2, c2, d2 = y
    s = lambda *t: (sum(u[0] for u in t), sum(u[1] for u in t))
    return (s(qm(a1, a2), qn(qm(b1, b2)), qn(qm(c1, c2)), qn(qm(d1, d2))),
            s(qm(a1, b2), qm(b1, a2), qm(c1, d2), qn(qm(d1, c2))),
            s(qm(a1, c2), qn(qm(b1, d2)), qm(c1, a2), qm(d1, b2)),
            s(qm(a1, d2), qm(b1, c2), qn(qm(c1, b2)), qm(d1, a2)))


def hconj(x): return (x[0], qn(x[1]), qn(x[2]), qn(x[3]))


g1 = (H, H, H, H)                                         # (1 + i + j + k)/2
g2 = ((Fr(1, 4), Fr(1, 4)), (Fr(-1, 4), Fr(1, 4)), H, Z0)  # (phi + i/phi + j)/2
two_i, frontier = {g1, g2}, [g1, g2]
while frontier:
    new = []
    for x in frontier:
        for y in (g1, g2):
            z = hmul(x, y)
            if z not in two_i:
                two_i.add(z)
                new.append(z)
    frontier = new
if len(two_i) != 120: fail(f"2I closure has {len(two_i)} elements")

VERTS = []
for sx in (1, -1):
    for sy in (1, -1):
        base = [Z0, (Fr(sx), Fr(0)), (Fr(sy) * PHIq[0], Fr(sy) * PHIq[1])]   # (0, +-1, +-phi)
        for r in range(3):
            VERTS.append(tuple(base[(k - r) % 3] for k in range(3)))
VERTS = sorted(set(VERTS))
if len(VERTS) != 12: fail("icosahedron vertices")


def dot(u, v): return qa(qa(qm(u[0], v[0]), qm(u[1], v[1])), qm(u[2], v[2]))


def ad(g, v):
    w = hmul(hmul(g, (Z0,) + v), hconj(g))
    if w[0] != Z0: fail("Ad did not return a pure quaternion")
    return w[1:]


index = {v: n for n, v in enumerate(VERTS)}


def graph(value):
    g = {n: {m for m, w in enumerate(VERTS) if m != n and dot(v, w) == value} for n, v in enumerate(VERTS)}
    if any(len(s) != 5 for s in g.values()): fail("a vertex graph is not 5-regular")
    return g


NEAREST = graph(PHIq)                            # |v|^2 = phi + 2; nearest neighbours have dot phi
DIST_TWO = graph((Fr(-1, 2), Fr(-1, 2)))         # graph distance two: dot -phi
mit_rows = []                                    # (rotation of the 12 vertices, chi(Sym^2 Q) in Z[phi])
for g in two_i:
    perm = tuple(index.get(ad(g, v), -1) for v in VERTS)
    if -1 in perm: fail("Ad Q does not preserve the icosahedron")
    tr = qa(g[0], g[0])                                  # tr Q(g) = 2 * real part, in Q(sqrt5)
    c = qa(qm(tr, tr), (Fr(-1), Fr(0)))                  # (tr Q)^2 - 1
    x = (c[0] - c[1], 2 * c[1])                          # p + q*sqrt5 -> (p - q) + 2q*phi
    if x[0].denominator != 1 or x[1].denominator != 1: fail("chi(Sym^2 Q) not in Z[phi]")
    mit_rows.append((perm, (int(x[0]), int(x[1]))))
if {o: {c for perm, c in mit_rows if order(perm) == o} for o in (1, 2, 3)} != {1: {(3, 0)}, 2: {(-1, 0)}, 3: {(0, 0)}}:
    fail("chi(Sym^2 Q) on the elements of order 1, 2, 3")


def mit_steps(adj):
    counts, by_step = Counter(), {}
    for perm, c in mit_rows:
        if order(perm) == 5:
            st = step_type(perm, adj)
            counts[(st, zname(c))] += 1
            by_step.setdefault(st, set()).add(c)
    return counts, by_step


mit_table, mit_by_step = mit_steps(NEAREST)
print(f"\nMIT 2I: {len(two_i)} unit quaternions; Ad Q preserves the icosahedron (0, +-1, +-phi); "
      f"elements acting with order five: (step, chi on Sym^2 Q): count")
for k, n in sorted(mit_table.items()):
    print(f"  {k}: {n}")
print("  (each rotation appears twice, once for each of its two lifts +-g; Sym^2 Q' is the Galois conjugate)")
print("  chi(Sym^2 Q) = 3, -1, 0 on the elements acting with order 1, 2, 3")

# ----------------------------- 4. the bridge ----------------------------------------------
if mit_by_step != oph_by_step: fail("bridge: chi(Sym^2 Q) and chi(W-) differ on a step class")
print("\nBridge: chi(Sym^2 Q) = chi(W-) on every class (orders 1, 2, 3 and both step classes), "
      "so Sym^2 Q = W- and Sym^2 Q' = W+")
if mit_steps(DIST_TWO)[1] == oph_by_step: fail("mutation arm: the distance-two graph did not break the bridge")
print("Mutation arm: classifying MIT's rotations with the distance-two graph breaks the bridge, as required")

# ----------------------------- 5. eigenvalue labels, from OPH's committed N ----------------
sms = show("Lean/Screen/ScaledMaxwellStability.lean")
nz = block(sms, "def faceNormalZ : Matrix (Fin 20) (Fin 20) ℤ :=", "\n\n")
N = [[int(t) for t in r.split(",")] for r in re.findall(r"!\[([-0-9,\s]+)\]", nz)]
if len(N) != 20 or any(len(r) != 20 for r in N): fail("faceNormalZ is not a literal 20x20 table")


def shared(f, g): return len(set(FACES[f]) & set(FACES[g])) == 2


if any(N[f][g] != (3 if f == g else (-1 if shared(f, g) else 0)) for f in range(20) for g in range(20)):
    fail("faceNormalZ differs from 3I minus the face adjacency")
LAM_PLUS, LAM_MINUS = (2, 2), (4, -2)   # 3 + sqrt5 = 2 + 2phi, 3 - sqrt5 = 4 - 2phi


def eigen_ok(P, lam):
    for i in range(20):
        for j in range(20):
            lhs = (0, 0)
            for k in range(20):
                lhs = zadd(lhs, zscale(N[i][k], P[k][j]))
            if lhs != zmul(lam, P[i][j]):
                return False
    return True


if not (eigen_ok(PLUS, LAM_PLUS) and eigen_ok(MINUS, LAM_MINUS)): fail("N * projector != eigenvalue * projector")
print("\nOPH faceNormalZ = 3I - (face adjacency), and N*PLUS = (3+sqrt5)*PLUS, N*MINUS = (3-sqrt5)*MINUS, checked entrywise")
if eigen_ok(PLUS, LAM_MINUS) or eigen_ok(MINUS, LAM_PLUS): fail("mutation arm: swapped eigenvalues still pass")
print("Mutation arm: swapping the two eigenvalues breaks the entrywise check, as required")
print("\nALL PASS")
