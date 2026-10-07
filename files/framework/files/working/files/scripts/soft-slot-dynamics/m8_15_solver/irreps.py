"""The nine irreducible unitary representations of 2I, as explicit matrices on its 120 elements.

R0 = 1, R1 = 2 (the natural SU(2)), R2 = 2' (R1 after the outer automorphism), R3 = Sym^2 = 3, R4 = 3' = Sym^2 of 2',
R5 = 4 = 2 (x) 2', R6 = Sym^3 = 4', R7 = Sym^4 = 5, R8 = Sym^5 = 6. McKay distances 0, 1, 7, 2, 6, 6, 3, 4, 5."""
import numpy as np
from math import comb, factorial
from geometry import binary_icosahedral, galois, group_tables


def su2(q):
    a, b, c, d = q
    return np.array([[a + 1j * b, c + 1j * d], [-c + 1j * d, a - 1j * b]])


def sym(U, n):
    """Spin n/2: U acting on homogeneous polynomials of degree n, orthonormal basis x^k y^(n-k)/sqrt(k!(n-k)!)."""
    (al, be), (ga, de) = U
    M = np.zeros((n + 1, n + 1), complex)
    # (x, y) -> (al x + ga y, be x + de y) on the variables, i.e. f -> f((x, y) U)
    for k in range(n + 1):
        # expand (al x + ga y)^k (be x + de y)^(n-k)
        poly = np.zeros(n + 1, complex)
        for i in range(k + 1):
            for j in range(n - k + 1):
                poly[i + j] += comb(k, i) * comb(n - k, j) * al ** i * ga ** (k - i) * be ** j * de ** (n - k - j)
        for m in range(n + 1):
            M[m, k] = poly[m] * np.sqrt(factorial(m) * factorial(n - m) / (factorial(k) * factorial(n - k)))
    return M


def irreps():
    G = binary_icosahedral()
    S = galois(G)
    U = np.array([su2(g) for g in G])
    Up = np.array([su2(g) for g in S])
    R = {0: np.ones((120, 1, 1), complex), 1: U, 2: Up,
         3: np.array([sym(u, 2) for u in U]), 4: np.array([sym(u, 2) for u in Up]),
         5: np.array([np.kron(u, v) for u, v in zip(U, Up)]),
         6: np.array([sym(u, 3) for u in U]), 7: np.array([sym(u, 4) for u in U]), 8: np.array([sym(u, 5) for u in U])}
    return G, R


if __name__ == '__main__':
    G, R = irreps()
    mt, inv = group_tables(G)
    S = galois(G)
    d = np.linalg.norm(S[:, None, :] - G[None, :, :], axis=2).min(axis=1)
    print('outer automorphism lands in 2I:', bool(np.all(d < 1e-9)))
    ok_hom = all(np.allclose(R[k][mt[i, j]], R[k][i] @ R[k][j]) for k in R for i in range(0, 120, 11) for j in range(0, 120, 7))
    ok_uni = all(np.allclose(R[k][i].conj().T @ R[k][i], np.eye(R[k].shape[1])) for k in R for i in range(120))
    chars = np.array([[np.trace(R[k][i]) for i in range(120)] for k in range(9)])
    gram = chars.conj() @ chars.T / 120
    print('homomorphisms:', ok_hom, ' unitary:', ok_uni, ' characters orthonormal:', np.allclose(gram, np.eye(9)))
    print('dimensions:', [R[k].shape[1] for k in range(9)])
    # McKay multiplicities m_K(rho) in V_{K/2}: chi_K(g) = sin((K+1) t)/sin t with cos t = Re g
    t = np.arccos(np.clip(G[:, 0], -1, 1))
    def chiK(K):
        out = np.empty(120)
        for i, th in enumerate(t):
            out[i] = (K + 1) if abs(np.sin(th)) < 1e-12 and np.cos(th) > 0 else ((-1) ** K * (K + 1) if abs(np.sin(th)) < 1e-12 else np.sin((K + 1) * th) / np.sin(th))
        return out
    first = []
    for k in range(9):
        m = [int(round((chars[k].conj() @ chiK(K)).real / 120)) for K in range(0, 31)]
        first.append(next(K for K in range(31) if m[K] > 0))
    print('first occurrence level (McKay distance):', first)
