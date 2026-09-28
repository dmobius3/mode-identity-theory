#!/usr/bin/env python3
"""Proposition 0.2 of projective-carrier.md: the conic band bent isometrically into S³; R = 1.

M(W) is the lune L = {|longitude| ≤ W} on a unit S², with vertices N and S = −N, and with N and S identified (§I).
Fermi coordinates about L's central meridian: s ∈ [0, π] is arclength from N along the meridian's great circle, t the
signed distance from it; the metric is dt² + cos²t ds². Let Σ′ = S³ ∩ {x₄ = 0}, with pole B = e₄, and γ a unit-speed
simple closed curve of length π in Σ′: the circle of geodesic radius π/6 about e₁. The embedding is
    f(p) = cos t · γ(s) + sin t · B,   (s, t) the Fermi coordinates of the lune point p.

Checks at W ∈ {0.3, 0.7, 1.2, 1.5} (exit 1 on any failure):
  B1  L in Fermi coordinates: 0 ≤ s ≤ π, |t| ≤ W, width zero only at s = 0 and π; boundary tan|t| = tan W sin s
  B2  f lies on S³
  B3  f is isometric: its pullback metric is the lune's round metric
  B4  the pinch: N and S map to one point
  B5  f embeds M(W): bi-Lipschitz from M(W)'s own metric, the lune's with N and S identified. Near W = π/2 the
      constant falls like sin(π/2 − W), as the pinch's two sectors close up; at smaller W a pair across γ sets it
      (0.622 at W = 0.3). The check asks for half of sin(π/2 − W), below the constant at every sampled width.
      A cross-check of the analytic injectivity proof, not a certificate of it
  B6  det A = 0 on the smooth locus: one principal curvature vanishes, |κ_min| ≤ 10⁻⁴ (1 + |κ_max|)
  B7  f is bent: H = κ/cos t with κ = √3, the geodesic curvature of γ in Σ′, so f is never minimal
  B8  two-sided: along every meridian loop, whose tangent planes match at the planar pinch, the normal returns
      unchanged through the pinch, which S³ glues by the identity
  B9  the pinch is planar: its two sectors lie in one plane, as for the unbent carrier
--arms plants a defect for each check and requires it to fire."""
import sys
import numpy as np

WIDTHS = (0.3, 0.7, 1.2, 1.5)
E = np.eye(4)
KAPPA = np.sqrt(3.0)                      # geodesic curvature of a circle of radius π/6 in the unit S²


def circle(rad, speed=1.0):
    """Unit-speed (times speed) circle of geodesic radius rad about e₁ in Σ′, with its normal in Σ′."""
    def g(s):
        ph = speed * s / np.sin(rad)
        return np.cos(rad) * E[0] + np.sin(rad) * (np.cos(ph) * E[1] + np.sin(ph) * E[2])
    return g


def great(s):
    return np.cos(s) * E[1] + np.sin(s) * E[2]


def curve(plant):
    if plant == "speed":
        return circle(np.pi / 6, 1.1)
    if plant == "short":
        return circle(np.arcsin(0.45))             # length 0.9π: γ(π) ≠ γ(0)
    if plant == "twice":
        return circle(np.arcsin(0.25))             # length π/2, traversed twice by s = π
    if plant == "geodesic":
        return great
    if plant == "triangle":
        return triangle
    return circle(np.pi / 6)


V = [np.array([1.0, 0, 0, 0]), np.array([0.5, np.sqrt(3) / 2, 0, 0])]
V.append(np.array([0.5, 0.5 / np.sqrt(3), np.sqrt(2 / 3), 0]))    # an equilateral geodesic triangle of side π/3


def triangle(s):
    k = min(int(np.floor(3 * s / np.pi)), 2) if 0 <= s < np.pi else (0 if s < 0 else 2)
    a, b = V[k % 3], V[(k + 1) % 3]
    u = (b - a * (a @ b)) / np.linalg.norm(b - a * (a @ b))
    tt = s - k * np.pi / 3
    return np.cos(tt) * a + np.sin(tt) * u


def fermi(P):
    """Fermi coordinates (s, t) of a point of the unit S² ⊂ R³ about the great circle y = 0, from N = (0, 0, 1)."""
    t = np.arcsin(np.clip(P[1], -1, 1))
    s = np.arctan2(P[0], P[2])
    return s, t


def lune_point(th, la):                             # colatitude th from N, longitude la
    return np.array([np.sin(th) * np.cos(la), np.sin(th) * np.sin(la), np.cos(th)])


def make_f(plant=None):
    g = curve(plant)
    if plant == "tilted-pole":
        B = lambda s: (E[3] + 0.2 * E[0]) / np.linalg.norm(E[3] + 0.2 * E[0])
    elif plant == "twist":
        c = circle(np.pi / 6)
        nu = lambda s: (np.cos(s / 0.5) * E[1] + np.sin(s / 0.5) * E[2]) * np.cos(np.pi / 6) - np.sin(np.pi / 6) * E[0]
        B = lambda s: np.cos(0.5 * s) * E[3] + np.sin(0.5 * s) * nu(s)
    else:
        B = lambda s: E[3]

    def f(th, la):
        s, t = fermi(lune_point(th, la))
        return np.cos(t) * g(s) + np.sin(t) * B(s)
    return f


def geometry(f, th, la, h=1e-4):
    X = f(th, la)
    Xa = (f(th + h, la) - f(th - h, la)) / (2 * h)
    Xb = (f(th, la + h) - f(th, la - h)) / (2 * h)
    Xaa = (f(th + h, la) - 2 * X + f(th - h, la)) / h**2
    Xbb = (f(th, la + h) - 2 * X + f(th, la - h)) / h**2
    Xab = (f(th + h, la + h) - f(th + h, la - h) - f(th - h, la + h) + f(th - h, la - h)) / (4 * h * h)
    g = np.array([[Xa @ Xa, Xa @ Xb], [Xb @ Xa, Xb @ Xb]])
    n = np.linalg.svd(np.vstack([X, Xa, Xb]))[2][-1]
    b = np.array([[Xaa @ n, Xab @ n], [Xab @ n, Xbb @ n]])
    S = np.linalg.solve(g, b)
    return X, g, S


def core_frame(f, th, la=0.0, h=1e-4):
    X = f(th, la)
    Xa = (f(th + h, la) - f(th - h, la)) / (2 * h)
    Xb = (f(th, la + h) - f(th, la - h)) / (2 * h)
    return X, Xa, Xb, np.linalg.svd(np.vstack([X, Xa, Xb]))[2][-1]


def checks(W, plant=None):
    f = make_f(plant)
    r = {}
    # B1: the lune in Fermi coordinates
    ok1 = True
    for th in np.linspace(0, np.pi, 181):
        for la in np.linspace(-W, W, 41):
            s, t = fermi(lune_point(th, la))
            ok1 &= -1e-12 <= s <= np.pi + 1e-12 and abs(t) <= W + 1e-12
            if th in (0.0, np.pi):
                ok1 &= abs(t) < 1e-12
        for la in (-W, W):
            s, t = fermi(lune_point(th, la))
            bound = np.arcsin(np.sin(W) * np.sin(s)) if plant == "sin-boundary" else np.arctan(np.tan(W) * np.sin(s))
            ok1 &= abs(abs(t) - bound) < 1e-12
    s, t = fermi(lune_point(np.pi / 2, W))
    r["B1 the lune in Fermi coordinates: 0 ≤ s ≤ π, |t| ≤ W, boundary tan|t| = tan W sin s"] = bool(ok1 and abs(t - W) < 1e-12)
    # samples on the smooth locus
    ths = np.linspace(0.05, np.pi - 0.05, 40)
    las = np.linspace(-W, W, 9)
    on, iso, null, bent = 0.0, 0.0, 0.0, 0.0
    for th in ths:
        for la in las:
            X, g, S = geometry(f, th, la)
            on = max(on, abs(np.linalg.norm(X) - 1))
            iso = max(iso, np.abs(g - np.diag([1.0, np.sin(th) ** 2])).max())
            ev = np.linalg.eigvals(S).real
            null = max(null, abs(ev[np.argmin(abs(ev))]) / (1 + abs(ev).max()))
            s, t = fermi(lune_point(th, la))
            bent = max(bent, abs(abs(np.trace(S)) - KAPPA / np.cos(t)))
    r["B2 f lies on S³"] = on < 1e-12
    r["B3 isometric: the pullback metric is the lune's round metric"] = iso < 1e-5
    r["B4 the pinch: N and S map to one point"] = np.linalg.norm(f(0.0, 0.0) - f(np.pi, 0.0)) < 1e-12
    # B5: bi-Lipschitz lower bound from M(W)'s metric (the lune is convex, so its distance is the sphere's)
    pts = [(th, la) for th in np.linspace(0, np.pi, 61) for la in np.linspace(-W, W, 7)]
    P = np.array([lune_point(*p) for p in pts])
    F = np.array([f(*p) for p in pts])
    arc = lambda U, V: 2 * np.arcsin(np.clip(np.linalg.norm(U - V, axis=-1) / 2, 0, 1))
    dL = arc(P[:, None, :], P[None, :, :])
    dN, dS = arc(P, np.array([0, 0, 1.0])), arc(P, np.array([0, 0, -1.0]))
    dM = np.minimum(dL, np.minimum(dN[:, None] + dS[None, :], dS[:, None] + dN[None, :]))
    dF = np.linalg.norm(F[:, None, :] - F[None, :, :], axis=2)
    mask = dM > 1e-6
    ratio = (dF[mask] / dM[mask]).min()
    r["B5 embeds M(W): bi-Lipschitz from M(W)'s own metric"] = ratio > 0.5 * np.sin(np.pi / 2 - W)
    r["B6 det A = 0 on the smooth locus"] = null < 1e-4
    r["B7 bent: H = κ/cos t with κ = √3, so never minimal"] = bent < 1e-4
    xN, xS = f(0.0, 0.0), f(np.pi, 0.0)
    deck = +1.0 if np.linalg.norm(xN - xS) < 1e-9 else (-1.0 if np.linalg.norm(xN + xS) < 1e-9 else 0.0)
    ok8 = bool(deck)
    for la in (las if deck else []):
        ths = np.linspace(0.01, np.pi - 0.01, 2001)
        prev = first = None
        for th in ths:
            X, Xa, Xb, n = core_frame(f, th, la)
            if prev is not None and n @ prev < 0:
                n = -n
            if first is None:
                first, pl0 = n, np.linalg.qr(np.vstack([Xa, Xb]).T)[0]
            prev = n
        pl1 = np.linalg.qr(np.vstack([Xa, Xb]).T)[0]
        same_plane = np.linalg.svd(pl0.T @ pl1)[1].min() > 1 - 10 * 0.01**2
        ok8 &= bool(first @ (deck * prev) > 0.99 and same_plane)         # the sign decides; the ends sit 0.01 from the pinch
    r["B8 two-sided: every meridian loop returns the normal unchanged through the pinch"] = ok8
    eps = 1e-4
    dirs = [f(eps, la) - xN for la in las] + [f(np.pi - eps, la) - xS for la in las]
    dirs = np.array([d / np.linalg.norm(d) for d in dirs])
    r["B9 the pinch is planar: its two sectors lie in one plane"] = np.linalg.svd(dirs)[1][2] < 1e-3
    return r, ratio


def main():
    res = {W: checks(W) for W in WIDTHS}
    allres = {W: v[0] for W, v in res.items()}
    names = list(next(iter(allres.values())))
    for name in names:
        ok = all(allres[W][name] for W in WIDTHS)
        print(("PASS " if ok else "FAIL ") + name)
    print("bi-Lipschitz constant by width, against sin(π/2 − W): "
          + ", ".join(f"W = {W}: {res[W][1]:.3f} ({np.sin(np.pi / 2 - W):.3f})" for W in WIDTHS))
    green = all(all(v.values()) for v in allres.values())
    if "--arms" in sys.argv:
        assert green, "arms need a green parent"
        rc = 0
        B1, B2, B3, B4, B5, B6, B7, B8, B9 = names
        plants = {"sin-boundary": [B1],      # the lune's edge written sin|t| = sin W sin s
                  "tilted-pole": [B2],       # the pole not orthogonal to Σ′
                  "speed": [B3],             # γ run at speed 1.1
                  "short": [B4],             # γ of length 0.9π: the vertices separate
                  "twice": [B5],             # a circle of length π/2 run twice: closed, not simple
                  "twist": [B6],             # the ruling direction turning along γ: not developable
                  "geodesic": [B7, B8],     # γ a great circle: the unbent lune, glued through −I, one-sided
                  "triangle": [B9]}         # γ a geodesic triangle with a corner at the pinch: sectors not coplanar
        for plant, targets in plants.items():
            out, _ = checks(0.7, plant)
            for tname in targets:
                fired = not out[tname]
                print(("ARM FIRED " if fired else "ARM SILENT ") + f"{tname} [{plant}]")
                rc |= 0 if fired else 1
        return rc
    return 0 if green else 1


if __name__ == "__main__":
    sys.exit(main())
