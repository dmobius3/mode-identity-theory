"""S^3 = unit quaternions, the binary icosahedral group 2I, the 600-cell, and its 2I-equivariant red refinement.

The deck group 2I acts on S^3 by LEFT multiplication, x -> g x. It permutes the 600-cell's vertices (2I itself),
edges and cells freely, so the cells fall into 5 orbits. Only one representative cell per orbit is ever stored:
refining a representative gives representatives of the children's orbits, and every node is identified with
(its orbit, the group element carrying the orbit's canonical point to it)."""
import itertools
import numpy as np

PHI = (1 + 5 ** 0.5) / 2


def qmul(p, q):
    a1, b1, c1, d1 = p[..., 0], p[..., 1], p[..., 2], p[..., 3]
    a2, b2, c2, d2 = q[..., 0], q[..., 1], q[..., 2], q[..., 3]
    return np.stack([a1 * a2 - b1 * b2 - c1 * c2 - d1 * d2,
                     a1 * b2 + b1 * a2 + c1 * d2 - d1 * c2,
                     a1 * c2 - b1 * d2 + c1 * a2 + d1 * b2,
                     a1 * d2 + b1 * c2 - c1 * b2 + d1 * a2], -1)


def qconj(q):
    return q * np.array([1.0, -1.0, -1.0, -1.0])


def _parity(p):
    p, s = list(p), 0
    for i in range(len(p)):
        while p[i] != i:
            j = p[i]
            p[i], p[j] = p[j], p[i]
            s ^= 1
    return s


def binary_icosahedral():
    els = []
    for i in range(4):
        for s in (1.0, -1.0):
            v = np.zeros(4)
            v[i] = s
            els.append(v)
    for signs in itertools.product((0.5, -0.5), repeat=4):
        els.append(np.array(signs))
    for p in itertools.permutations(range(4)):
        if _parity(p):
            continue
        for s in itertools.product((1.0, -1.0), repeat=3):
            vals = [0.0, s[0] * 0.5, s[1] * PHI / 2, s[2] / (2 * PHI)]
            v = np.zeros(4)
            for k in range(4):
                v[p[k]] = vals[k]
            els.append(v)
    G = np.array(els)
    # order: put the identity first for convenience
    idx = int(np.argmin(np.linalg.norm(G - np.array([1.0, 0, 0, 0]), axis=1)))
    G[[0, idx]] = G[[idx, 0]]
    return G


def group_tables(G, tol=1e-9):
    """Multiplication table and inverses as indices into G."""
    n = len(G)
    P = qmul(G[:, None, :], G[None, :, :]).reshape(-1, 4)
    d = np.linalg.norm(P[:, None, :] - G[None, :, :], axis=2)
    mt = np.argmin(d, axis=1)
    assert np.all(d[np.arange(len(P)), mt] < tol), 'not closed'
    mt = mt.reshape(n, n)
    inv = np.array([int(np.where(mt[i] == 0)[0][0]) for i in range(n)])
    return mt, inv


def galois(G):
    """The outer automorphism of 2I: sqrt5 -> -sqrt5 on the coordinates, then a rotation of the imaginary part."""
    H = G.copy()
    a, b = PHI / 2, 1 / (2 * PHI)
    for idx in np.ndindex(H.shape):
        x = G[idx]
        if abs(abs(x) - a) < 1e-12:
            H[idx] = -np.sign(x) * b
        elif abs(abs(x) - b) < 1e-12:
            H[idx] = -np.sign(x) * a
    # the coordinate conjugation lands in the mirror copy of 2I (odd permutations); the rotation by 90 degrees about
    # i, (w, x, y, z) -> (w, x, z, -y), an algebra automorphism of the quaternions, carries it back to 2I
    return np.stack([H[..., 0], H[..., 1], H[..., 3], -H[..., 2]], -1)


def six_hundred_cell_reps(G):
    """The 5 orbit representatives among the 20 cells at the identity vertex."""
    one = G[0]
    nb = [i for i in range(len(G)) if abs(G[i] @ one - PHI / 2) < 1e-9]
    assert len(nb) == 12
    cells = []
    for a, b, c in itertools.combinations(nb, 3):
        if all(abs(G[x] @ G[y] - PHI / 2) < 1e-9 for x, y in ((a, b), (a, c), (b, c))):
            cells.append((0, a, b, c))
    assert len(cells) == 20
    keys = {}
    for cell in cells:
        X = G[list(cell)]
        best = None
        for g in G:
            Y = qmul(np.broadcast_to(g, X.shape), X)
            key = tuple(sorted(tuple(np.round(y, 8)) for y in Y))
            best = key if best is None or key < best else best
        keys.setdefault(best, []).append(cell)
    assert len(keys) == 5 and all(len(v) == 4 for v in keys.values())
    return [G[list(v[0])] for v in sorted(keys.values())]


def _proj(x):
    return x / np.linalg.norm(x)


def red_refine(T):
    """Red refinement of a spherical tetrahedron (4 x 4 array of unit quaternions): 8 children, midpoints projected,
    the inner octahedron split along its shortest diagonal."""
    a, b, c, d = T
    m = {('a', 'b'): _proj(a + b), ('a', 'c'): _proj(a + c), ('a', 'd'): _proj(a + d),
         ('b', 'c'): _proj(b + c), ('b', 'd'): _proj(b + d), ('c', 'd'): _proj(c + d)}
    ab, ac, ad, bc, bd, cd = (m[k] for k in (('a', 'b'), ('a', 'c'), ('a', 'd'), ('b', 'c'), ('b', 'd'), ('c', 'd')))
    kids = [np.array([a, ab, ac, ad]), np.array([b, ab, bc, bd]), np.array([c, ac, bc, cd]), np.array([d, ad, bd, cd])]
    diags = [(ab, cd, [ac, ad, bd, bc]), (ac, bd, [ab, ad, cd, bc]), (ad, bc, [ab, ac, cd, bd])]
    p, q, ring = min(diags, key=lambda t: np.linalg.norm(t[0] - t[1]))
    for i in range(4):
        kids.append(np.array([p, q, ring[i], ring[(i + 1) % 4]]))
    return kids


def sym_refine(T):
    """Canonical refinement of a spherical tetrahedron into 12: the 4 corner tetrahedra of the red refinement, and the
    inner octahedron split from its centre (the projected centroid) into 8. No choice is made, so every isometry of
    the coarse mesh is an isometry of the refined one: left and right multiplication by 2I both survive."""
    a, b, c, d = T
    ab, ac, ad, bc, bd, cd = (_proj(a + b), _proj(a + c), _proj(a + d), _proj(b + c), _proj(b + d), _proj(c + d))
    o = _proj(a + b + c + d)
    kids = [np.array([a, ab, ac, ad]), np.array([b, ab, bc, bd]), np.array([c, ac, bc, cd]), np.array([d, ad, bd, cd])]
    faces = [(ab, ac, ad), (ab, bc, bd), (ac, bc, cd), (ad, bd, cd), (ab, ac, bc), (ab, ad, bd), (ac, ad, cd), (bc, bd, cd)]
    for f in faces:
        kids.append(np.array([o, f[0], f[1], f[2]]))
    return kids


def representatives(level, G, rule='sym'):
    reps = six_hundred_cell_reps(G)
    ref = sym_refine if rule == 'sym' else red_refine
    for _ in range(level):
        reps = [k for T in reps for k in ref(T)]
    return np.array(reps)


def p2_nodes(T):
    """The 10 P2 nodes of a spherical tet: its 4 vertices, then the projected midpoints of edges 01,02,03,12,13,23."""
    pts = list(T)
    for i, j in ((0, 1), (0, 2), (0, 3), (1, 2), (1, 3), (2, 3)):
        pts.append(_proj(T[i] + T[j]))
    return np.array(pts)


def orbit_ids(points, G, decimals=9):
    """For each point x, (orbit index, k) with x = G[k] * canonical(orbit). The canonical point of an orbit is its
    lexicographically largest image after rounding."""
    imgs = qmul(G[None, :, :], np.broadcast_to(points[:, None, :], (len(points), len(G), 4)).copy())
    # images h x for all h; canonical = lexicographic max over h of round(h x)
    R = np.round(imgs, decimals) + 0.0
    order = np.lexsort(tuple(R[:, :, c] for c in (3, 2, 1, 0)), axis=1)
    best_h = order[:, -1]
    canon = R[np.arange(len(points)), best_h]
    keys, inv = np.unique(canon, axis=0, return_inverse=True)
    # x = h^-1 canon: the element carrying the canonical point to x is the inverse of best_h
    return inv.ravel(), best_h, keys
