"""Review of the first-positive transfer run: an independent evaluation of its quantities (2026-09-28).
Method: the block kernel factored through spin-j matrices,
  K_E(a, b) = (n+1)/(2 pi^2) * (d_tau/120) * tr(D(a)^dag Pi D(b)),  Pi = sum_g chi_tau(g) D(g),
so each projection is a trace of 2D band integrals A = int e(y,w) D(P(y,w)) dA; the transverse sampler uses the exact
derivative of D along the real unit. The band grid is split at the pinch y = pi/2 (Gauss-Legendre on each half).
mutate="seam" uses the unflipped band map (d_y = d throughout), a planted defect for the review's arm."""
import numpy as np, itertools, math
phi = (1 + 5 ** .5) / 2
_els = set()
for i in range(4):
    for s in (1, -1):
        q = [0] * 4; q[i] = s; _els.add(tuple(q))
for s in itertools.product((1, -1), repeat=4):
    _els.add(tuple(x / 2 for x in s))
_even = [p for p in itertools.permutations(range(4))
         if sum(1 for a in range(4) for b in range(a + 1, 4) if p[a] > p[b]) % 2 == 0]
for p in _even:
    for s in itertools.product((1, -1), repeat=3):
        v = [0, s[0], s[1] / phi, s[2] * phi]; q = [0] * 4
        for a in range(4): q[p[a]] = v[a] / 2
        _els.add(tuple(round(x, 12) for x in q))
G = np.array(sorted(_els)); assert len(G) == 120 and np.allclose(np.sum(G ** 2, 1), 1)
def _sig(r):
    for a, b in ((phi / 2, -1 / (2 * phi)), (-phi / 2, 1 / (2 * phi))):
        if abs(r - a) < 1e-9: return b
        if abs(r - b) < 1e-9: return a
    return r
_c2 = 2 * G[:, 0]; _c2p = np.array([2 * _sig(r) for r in G[:, 0]])
CH = {"1": np.ones(120), "2": _c2, "2p": _c2p, "3": _c2 ** 2 - 1, "3p": _c2p ** 2 - 1, "4": _c2 * _c2p,
      "4p": _c2 ** 3 - 2 * _c2, "5": _c2 ** 4 - 3 * _c2 ** 2 + 1, "6": _c2 ** 5 - 4 * _c2 ** 3 + 3 * _c2}
DIM = {k: int(round(v[np.argmax(G[:, 0])])) for k, v in CH.items()}
for a in CH:
    for b in CH:
        assert abs(np.dot(CH[a], CH[b]) / 120 - (a == b)) < 1e-9
def Q(x):
    x0, x1, x2, x3 = x
    return np.array([[x0 + 1j * x1, x2 + 1j * x3], [-x2 + 1j * x3, x0 - 1j * x1]])
def Sym(M, n):
    a, b = M[0]; c, d = M[1]; D = np.zeros((n + 1, n + 1), complex)
    for k in range(n + 1):
        p1 = np.array([1 + 0j]); p2 = np.array([1 + 0j])
        for _ in range(k): p1 = np.convolve(p1, [c, a])
        for _ in range(n - k): p2 = np.convolve(p2, [d, b])
        p = np.convolve(p1, p2)
        for l in range(n + 1):
            D[l, k] = p[l] * math.sqrt(math.factorial(l) * math.factorial(n - l) / (math.factorial(k) * math.factorial(n - k)))
    return D
def dSym0(x, n):   # exact d/de Sym^n(Q(x) + e I) at e = 0: a polynomial of degree n in e, read off on a circle
    N = n + 2; r = 0.5; acc = 0
    for k in range(N):
        w = np.exp(2j * math.pi * k / N); acc = acc + Sym(Q(x) + r * w * np.eye(2), n) * np.conj(w)
    return acc / (N * r)
def U(n, x):
    th = math.acos(max(-1, min(1, x))); s = math.sin(th)
    return (n + 1) * (1 if x > 0 else (-1) ** n) if abs(s) < 1e-12 else math.sin((n + 1) * th) / s
def dimE(tau, n):
    m = sum(CH[tau][i] * U(n, G[i, 0]) for i in range(120)) / 120
    assert abs(m - round(m)) < 1e-9
    return DIM[tau] * int(round(m)) * (n + 1)
PL = {"generic": (np.array([0, 1, 2, 3]) / 14 ** .5, np.array([0, 2, -1, 0]) / 5 ** .5),
      "2fold": (np.array([0, 1, 0, 0.]), np.array([0, 0, 1, 0.])),
      "3fold": (np.array([0, 1, 1, 1]) / 3 ** .5, np.array([0, 1, -1, 0]) / 2 ** .5),
      "5fold": (np.array([0, 1 / phi, 1, 0]) / (1 + phi ** -2) ** .5, np.array([0, 0, 0, 1.]))}
def grid(W, ny=48, nw=48):
    xg, wg = np.polynomial.legendre.leggauss(ny); ys = []; wy = []
    for lo, hi in ((0, math.pi / 2), (math.pi / 2, math.pi)):
        ys.append((hi - lo) / 2 * xg + (hi + lo) / 2); wy.append((hi - lo) / 2 * wg)
    ys = np.concatenate(ys); wy = np.concatenate(wy)
    xw, ww = np.polynomial.legendre.leggauss(nw)
    Y, Wm = np.meshgrid(ys, W * xw, indexing="ij")
    return Y, Wm, np.outer(wy, W * ww) * np.abs(np.cos(Y))
def run(tau, n, pl, W, mutate=None):
    p, c = PL[pl]; d = np.concatenate([[0], np.cross(p[1:], c[1:])])
    Y, Wm, A = grid(W)
    sgn = np.where(Y <= math.pi / 2, 1.0, -1.0)
    flip = np.ones_like(Y) if mutate == "seam" else sgn
    Pi = sum(CH[tau][i] * Sym(Q(G[i]), n) for i in range(120))
    pref = (n + 1) / (2 * math.pi ** 2) * DIM[tau] / 120
    Dv = np.zeros(Y.shape + (n + 1, n + 1), complex); Dt = np.zeros_like(Dv)
    for idx in np.ndindex(Y.shape):
        y, w = Y[idx], Wm[idx]
        P = math.cos(y) * (math.cos(w) * c + math.sin(w) * flip[idx] * d) + math.sin(y) * p
        Dv[idx] = Sym(Q(P), n); Dt[idx] = dSym0(P, n)
    alpha = math.pi / (2 * W)
    targets = {"tw_F_P1": np.sin(Y), "tw_F_P0": sgn, "un_F_P1": sgn * np.sin(Y), "un_F_P0": np.ones_like(Y),
               "un_SCTM_P1": (3 * np.sin(Y) ** 2 - 1) / 2 if W <= math.pi / 4
               else sgn * np.abs(np.cos(Y)) ** alpha * np.sin(math.pi * Wm / (2 * W))}
    out = {}
    for samp, DD in (("val", Dv), ("trans", Dt)):
        out[f"hs_{samp}"] = pref * sum(A[i] * np.real(np.trace(DD[i].conj().T @ Pi @ DD[i])) for i in np.ndindex(Y.shape))
        for tn, e in targets.items():
            Am = np.einsum("ij,ijab->ab", A * e, DD)
            out[f"{samp}:{tn}"] = pref * np.real(np.trace(Am.conj().T @ Pi @ Am)) / np.sum(A * e * e)
    return out
