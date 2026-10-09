"""The mesh's right 2I action on the reduced unknowns, the discrete right-rotation derivatives X_a, orientations that
place a pinned subgroup inside right 2I, and the fixed spaces that Newton is solved in.

Conventions. Sections are rho-equivariant under LEFT multiplication, psi(g x) = rho(g) psi(x); the unknowns are the
values at one canonical point per left orbit of nodes. Right multiplication commutes with the left action, and the
mesh is invariant under right 2I, so (R_h psi)(x) = psi(x h) acts on the unknowns as a block permutation with blocks
rho(gamma). On the lowest level, psi_w(x) = T pi(x) w and R_h psi_w = psi_{pi(h) w}.

The Condon-Shortley axes: pi(exp(theta e/2)) = exp(i theta J) with e = k, j, i for J = J_x, J_y, J_z (checked in
selftest). X_c is the derivative along the left-invariant field x -> x e_c / 2 (it generates the right rotations), so
on the lowest level X_c psi_w = psi_{i J_c w}."""
import numpy as np
import scipy.sparse as sps
import scipy.sparse.linalg as spla
from scipy.sparse.csgraph import connected_components
from geometry import qmul, qconj, p2_nodes, PHI
from fem import p2_shape, tet_quadrature
from irreps import sym, su2

UNIT = {'x': np.array([0.0, 0, 0, 1]), 'y': np.array([0.0, 0, 1, 0]), 'z': np.array([0.0, 1, 0, 0])}


def quat_axis_angle(axis_cs, angle):
    """The unit quaternion acting on the lowest level as exp(i angle J.n) for the Condon-Shortley axis n."""
    n = np.asarray(axis_cs, float)
    n = n / np.linalg.norm(n)
    v = n[0] * UNIT['x'] + n[1] * UNIT['y'] + n[2] * UNIT['z']
    return np.concatenate([[np.cos(angle / 2)], np.sin(angle / 2) * v[1:]])


def cs_vector(q):
    """The Condon-Shortley axis vector of a pure quaternion."""
    return np.array([q[3], q[2], q[1]])


def dpi(j2, e, h=1e-6):
    q = lambda t: np.concatenate([[np.cos(t / 2)], np.sin(t / 2) * np.asarray(e, float)[1:]])
    return (sym(su2(q(h)), j2) - sym(su2(q(-h)), j2)) / (2 * h)


def spin_matrices(j2):
    """Condon-Shortley J_x, J_y, J_z on the basis k = m + j (the sym basis)."""
    j = j2 / 2
    m = np.arange(j2 + 1) - j
    Jz = np.diag(m).astype(complex)
    Jp = np.zeros((j2 + 1, j2 + 1), complex)
    for a in range(j2):
        Jp[a + 1, a] = np.sqrt(j * (j + 1) - m[a] * (m[a] + 1))
    Jm = Jp.conj().T
    return (Jp + Jm) / 2, (Jp - Jm) / 2j, Jz


class RightAction:
    def __init__(self, mesh, R):
        self.mesh, self.R, self.d = mesh, R, R.shape[1]
        G = mesh.G
        # exact canonical points, from the element nodes: node = G[gidx] canon
        nodes = np.concatenate([p2_nodes(t) for t in mesh.T])
        orb, gi = mesh.orbit.ravel(), mesh.gidx.ravel()
        first = np.full(mesh.n_orb, -1)
        for p in range(len(orb)):
            if first[orb[p]] < 0:
                first[orb[p]] = p
        self.canon = qmul(G[mesh.inv[gi[first]]], nodes[first])
        self.lookup = {tuple(k): i for i, k in enumerate(np.round(mesh.canon, 9) + 0.0)}
        self._cache = {}

    def locate(self, pts):
        """For each point y: (orbit k, element index gamma) with y = G[gamma] canon_k."""
        G, mesh = self.mesh.G, self.mesh
        imgs = qmul(G[None, :, :], np.broadcast_to(pts[:, None, :], (len(pts), len(G), 4)).copy())
        Rr = np.round(imgs, 9) + 0.0
        order = np.lexsort(tuple(Rr[:, :, c] for c in (3, 2, 1, 0)), axis=1)
        best = order[:, -1]
        can = Rr[np.arange(len(pts)), best]
        k = np.array([self.lookup[tuple(c)] for c in can])
        return k, mesh.inv[best]

    def matrix(self, h):
        """R_h on the reduced unknowns, for h an index into G."""
        if h in self._cache:
            return self._cache[h]
        G, d = self.mesh.G, self.d
        y = qmul(self.canon, np.broadcast_to(G[h], self.canon.shape))
        k2, gam = self.locate(y)
        n = self.mesh.n_orb
        rows = (np.arange(n)[:, None, None] * d + np.arange(d)[None, :, None]).repeat(d, 2).ravel()
        cols = (k2[:, None, None] * d + np.arange(d)[None, None, :]).repeat(d, 1).ravel()
        vals = self.R[gam].ravel()
        Rh = sps.csr_matrix((vals, (rows, cols)), shape=(n * d, n * d))
        self._cache[h] = Rh
        return Rh

    def index(self, q, tol=1e-9):
        """Index into G of the quaternion q (or of -q is not accepted: the binary element itself)."""
        dist = np.linalg.norm(self.mesh.G - q[None, :], axis=1)
        i = int(np.argmin(dist))
        if dist[i] > tol:
            raise ValueError('not an element of 2I')
        return i


def m_orthonormal(V, M):
    """An M-orthonormal basis of span(V), by Cholesky (ARPACK's complex eigenvectors within a degenerate level are not
    M-orthogonal)."""
    C = V.conj().T @ (M @ V)
    Lc = np.linalg.cholesky((C + C.conj().T) / 2)
    return V @ np.linalg.inv(Lc).conj().T


def element_assemble(mesh, R, Ee):
    """Assemble an element-level matrix (nT, 10, 10) on the reduced unknowns, blocks Rn_i^dagger Rn_j."""
    d = R.shape[1]
    Rn = R[mesh.gidx]
    B = np.einsum('tiab,tjac->tijbc', Rn.conj(), Rn)
    nT = len(mesh.T)
    rows = np.broadcast_to((mesh.orbit[:, :, None, None, None] * d + np.arange(d)[None, None, None, :, None]), (nT, 10, 10, d, d)).ravel()
    cols = np.broadcast_to((mesh.orbit[:, None, :, None, None] * d + np.arange(d)[None, None, None, None, :]), (nT, 10, 10, d, d)).ravel()
    n = mesh.n_orb * d
    return sps.csr_matrix(((Ee[:, :, :, None, None] * B).ravel(), (rows, cols)), shape=(n, n))


def rotation_derivatives(mesh, R, nq=5):
    """D_c[i, j] = int phi_i (xi_c . grad phi_j), xi_c(x) = x e_c / 2, for c = x, y, z; X_c = M^-1 D_c.
    Its own 5-point collapsed rule: with 3 points, single entries miss skew-symmetry by 2e-3 at every level."""
    X = mesh.T
    nT = len(X)
    D = np.stack([X[:, 1] - X[:, 0], X[:, 2] - X[:, 0], X[:, 3] - X[:, 0]], -1)
    P, W = tet_quadrature(nq)
    De = {c: np.zeros((nT, 10, 10)) for c in 'xyz'}
    for xi, w in zip(P, W):
        L, N, dN = p2_shape(xi)
        y = np.einsum('a,tac->tc', L, X)
        ny = np.linalg.norm(y, axis=1)
        x = y / ny[:, None]
        Pm = np.eye(4)[None] - x[:, :, None] * x[:, None, :]
        J = np.einsum('tij,tjk->tik', Pm, D) / ny[:, None, None]
        Gm = np.einsum('tki,tkj->tij', J, J)
        Gi = np.linalg.inv(Gm)
        s = w * np.sqrt(np.linalg.det(Gm))
        for c in 'xyz':
            xi_c = qmul(x, np.broadcast_to(UNIT[c], x.shape)) / 2
            v = np.einsum('tij,tkj,tk->ti', Gi, J, xi_c)              # reference-coordinate components
            dNv = np.einsum('jk,tk->tj', dN, v)
            De[c] += s[:, None, None] * N[None, :, None] * dNv[:, None, :]
    return {c: element_assemble(mesh, R, De[c]) for c in 'xyz'}


class Rotations:
    """X_c Psi = M^-1 D_c Psi, the L2-projection of the derivative along the generator of right rotations about c."""
    def __init__(self, mesh, R, M):
        self.D = rotation_derivatives(mesh, R)
        self.lu = spla.splu(M.tocsc(), permc_spec='MMD_AT_PLUS_A')

    def apply(self, c, Psi):
        return self.lu.solve(self.D[c] @ Psi)

    def all(self, Psi):
        return [self.apply(c, Psi) for c in 'xyz']


# --- 2I axes and orientations -------------------------------------------------------------------------------------
def axes_2I(G):
    """Rotation axes of 2I (unit 3-vectors in quaternion imaginary coordinates, up to sign), by order 5, 3, 2."""
    out = {5: [], 3: [], 2: []}
    for g in G:
        re = g[0]
        v = g[1:]
        nv = np.linalg.norm(v)
        if nv < 1e-9:
            continue
        for order, c in ((5, np.cos(np.pi / 5)), (3, np.cos(np.pi / 3)), (2, 0.0)):
            if abs(re - c) < 1e-9:
                a = v / nv
                if not any(abs(abs(a @ b) - 1) < 1e-9 for b in out[order]):
                    out[order].append(a)
    return {k: np.array(v) for k, v in out.items()}


def frame_rotation(src, dst):
    """Unit quaternion q with q s q^-1 = t for the orthonormal pairs src = (s1, s2), dst = (t1, t2) of 3-vectors
    (imaginary quaternion coordinates). The third vectors follow by the cross product."""
    S = np.column_stack([src[0], src[1], np.cross(src[0], src[1])])
    T = np.column_stack([dst[0], dst[1], np.cross(dst[0], dst[1])])
    Rm = T @ S.T
    # rotation matrix -> quaternion (v -> q v q^-1)
    tr = np.trace(Rm)
    if tr > -0.99:
        w = np.sqrt(1 + tr) / 2
        q = np.array([w, (Rm[2, 1] - Rm[1, 2]) / (4 * w), (Rm[0, 2] - Rm[2, 0]) / (4 * w), (Rm[1, 0] - Rm[0, 1]) / (4 * w)])
    else:
        i = int(np.argmax(np.diag(Rm)))
        jx, kx = (i + 1) % 3, (i + 2) % 3
        s = np.sqrt(1 + Rm[i, i] - Rm[jx, jx] - Rm[kx, kx]) * 2
        q = np.zeros(4)
        q[0] = (Rm[kx, jx] - Rm[jx, kx]) / s
        q[1 + i] = s / 4
        q[1 + jx] = (Rm[jx, i] + Rm[i, jx]) / s
        q[1 + kx] = (Rm[kx, i] + Rm[i, kx]) / s
    return q / np.linalg.norm(q)


def rot3(q, v):
    """Rotate the 3-vector v (imaginary quaternion coordinates) by q: q v q^-1."""
    return qmul(qmul(q, np.concatenate([[0.0], v])), qconj(q))[1:]


def to_quat_vec(axis_cs):
    """Condon-Shortley axis -> imaginary-quaternion 3-vector."""
    n = np.asarray(axis_cs, float)
    n = n / np.linalg.norm(n)
    return (n[0] * UNIT['x'] + n[1] * UNIT['y'] + n[2] * UNIT['z'])[1:]


def orient(G, cs_axes, orders):
    """An orientation g0 with g0^-1 (pinned subgroup) g0 inside 2I. cs_axes: one or two Condon-Shortley axes of the
    representative's pinned subgroup, with their rotation orders (the second perpendicular to the first). Returns g0
    and the 2I axes used. Deterministic: the first matching 2I axes in axes_2I order."""
    A = axes_2I(G)
    s = [to_quat_vec(a) for a in cs_axes]
    if len(s) == 1:
        t1 = A[orders[0]][0]
        perp = np.cross(s[0], [1.0, 0, 0]) if abs(s[0][0]) < 0.9 else np.cross(s[0], [0, 1.0, 0])
        perp /= np.linalg.norm(perp)
        tperp = np.cross(t1, [1.0, 0, 0]) if abs(t1[0]) < 0.9 else np.cross(t1, [0, 1.0, 0])
        tperp /= np.linalg.norm(tperp)
        src, dst = (s[0], perp), (t1, tperp)
    else:
        found = None
        for t1 in A[orders[0]]:
            for t2 in A[orders[1]]:
                for sg in (1, -1):
                    if abs(t1 @ t2) < 1e-9:
                        found = (t1, sg * t2)
                        break
                if found:
                    break
            if found:
                break
        src, dst = (s[0], s[1]), found
    # q maps the 2I axes onto the representative's axes: q t q^-1 = s; then g0 = q, and g0^-1 h0 g0 has axis t
    q = frame_rotation(dst, src)
    return q


# --- fixed spaces ---------------------------------------------------------------------------------------------------
def characters(pi_of, w, hs):
    """chi(h) = <w, pi(h) w>/<w, w> for each h (unit modulus when h fixes w up to phase)."""
    out = []
    for h in hs:
        v = pi_of(h) @ w
        c = np.vdot(w, v) / np.vdot(w, w)
        if np.linalg.norm(v - c * w) > 1e-9 * np.linalg.norm(w):
            raise ValueError('h does not fix the representative up to a phase')
        out.append(c)
    return np.array(out)


def subgroup_closure(mt, gens):
    """All elements generated by the given indices (with the multiplication table mt)."""
    S = {0}
    frontier = set(gens)
    while frontier:
        S |= frontier
        new = set()
        for a in S:
            for b in gens:
                c = int(mt[a, b])
                if c not in S:
                    new.add(c)
        frontier = new
    return sorted(S)


def fixed_space_basis(RA, H, chi):
    """Orthonormal (Euclidean) complex basis B (n x p, sparse) of {Psi : R_h Psi = chi(h) Psi for all h in H}, with
    chi a homomorphism H -> U(1). Built block by block on the orbits of H on the node orbits."""
    n = RA.mesh.n_orb * RA.d
    d = RA.d
    P = sum(np.conj(c) * RA.matrix(h) for h, c in zip(H, chi)) / len(H)
    P = P.tocsc()
    # H-orbits of node orbits, from the permutation structure of the R_h
    nob = RA.mesh.n_orb
    rr, cc = [], []
    for h in H:
        C = RA.matrix(h).tocoo()
        rr.append(C.row // d)
        cc.append(C.col // d)
    rr, cc = np.concatenate(rr), np.concatenate(cc)
    Bnode = sps.csr_matrix((np.ones(len(rr)), (rr, cc)), shape=(nob, nob))
    ncomp, lab = connected_components(Bnode, directed=False)
    cols = []
    for comp in range(ncomp):
        nodes = np.where(lab == comp)[0]
        idx = (nodes[:, None] * d + np.arange(d)[None, :]).ravel()
        Pb = P[idx][:, idx].toarray()
        U, s, _ = np.linalg.svd(Pb)
        r = int((s > 0.5).sum())
        for k in range(r):
            v = np.zeros(n, complex)
            v[idx] = U[:, k]
            cols.append(sps.csr_matrix(v[:, None]))
    B = sps.hstack(cols, format='csr')
    return B


def selftest(level=1):
    import time
    from fem import Mesh
    from irreps import irreps
    from standing import Standing, germ_seed
    t0 = time.time()
    G, Rs = irreps()
    for j2 in (2, 6, 7):
        Jx, Jy, Jz = spin_matrices(j2)
        ok = (np.allclose(dpi(j2, UNIT['x']), 1j * Jx, atol=1e-7) and np.allclose(dpi(j2, UNIT['y']), 1j * Jy, atol=1e-7)
              and np.allclose(dpi(j2, UNIT['z']), 1j * Jz, atol=1e-7))
        print(f'  Condon-Shortley axes x, y, z <-> quaternion k, j, i at spin {j2}/2: {ok}')
    mesh = Mesh(level, nq=3)
    for slot, j2 in ((4, 6), (3, 2), (2, 7)):
        R = Rs[slot]
        st = Standing(mesh, R)
        RA = RightAction(mesh, R)
        rng = np.random.default_rng(1)
        hs = [5, 17, 63]
        Rh = [RA.matrix(h) for h in hs]
        uni = max(abs(r.conj().T @ r - sps.identity(r.shape[0])).max() for r in Rh)
        comK = max(abs(r.conj().T @ st.K @ r - st.K).max() / abs(st.K).max() for r in Rh)
        comM = max(abs(r.conj().T @ st.M @ r - st.M).max() / abs(st.M).max() for r in Rh)
        hom = abs(RA.matrix(int(mesh.mt[5, 17])) - Rh[0] @ Rh[1]).max()
        Psi = rng.normal(size=st.K.shape[0]) + 1j * rng.normal(size=st.K.shape[0])
        quart = abs(st.q.energy(Rh[2] @ Psi) - st.q.energy(Psi)) / st.q.energy(Psi)
        w = rng.normal(size=j2 + 1) + 1j * rng.normal(size=j2 + 1)
        S0 = germ_seed(mesh, R, j2, w, G)
        S1 = germ_seed(mesh, R, j2, sym(su2(G[hs[0]]), j2) @ w, G)
        lowest = np.linalg.norm(Rh[0] @ S0 - S1) / np.linalg.norm(S1)
        print(f'  slot R{slot}: R_h unitary {uni:.1e}; commutes with K {comK:.1e}, M {comM:.1e}; homomorphism {hom:.1e}; '
              f'quartic invariant {quart:.1e}; R_h psi_w = psi_(pi(h) w) {lowest:.1e}')
        rot = Rotations(mesh, R, st.M)
        skew = max(abs(rot.D[c] + rot.D[c].conj().T).max() / abs(rot.D[c]).max() for c in 'xyz')
        Js = spin_matrices(j2)
        errs = []
        for c, Jc in zip('xyz', Js):
            target = germ_seed(mesh, R, j2, 1j * Jc @ w, G)
            got = rot.apply(c, S0)
            errs.append(np.sqrt(np.real(np.vdot(got - target, st.M @ (got - target))) / np.real(np.vdot(target, st.M @ target))))
        # on the discrete lowest level: leakage out of it, and the restricted generators' spectra (i m, m = -j..j)
        n0 = j2 + 1
        lam, V = spla.eigsh(st.K, k=n0, M=st.M, sigma=-0.5)
        V = m_orthonormal(V, st.M)                                 # ARPACK's vectors in a degenerate level are not
        leak, specerr = 0.0, 0.0
        for c in 'xyz':
            XV = np.column_stack([rot.apply(c, V[:, k]) for k in range(n0)])
            C = V.conj().T @ (st.M @ XV)
            res = XV - V @ C
            leak = max(leak, np.sqrt(np.real(np.vdot(res, st.M @ res)) / np.real(np.vdot(XV, st.M @ XV))))
            ev = np.sort(np.linalg.eigvals(C).imag)
            specerr = max(specerr, abs(ev - (np.arange(n0) - j2 / 2)).max())
        print(f'    X_c: D_c skew-Hermitian to {skew:.1e}; on the discrete lowest level: leakage {leak:.1e}, '
              f'eigenvalues i m to {specerr:.1e}; against interpolants psi_(iJ_c w): {max(errs):.1e}')
    print(f'  ({time.time() - t0:.0f}s)')


if __name__ == '__main__':
    import sys
    selftest(int(sys.argv[1]) if len(sys.argv) > 1 else 1)
