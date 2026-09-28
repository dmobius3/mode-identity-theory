#!/usr/bin/env python3
"""Proposition 0.3 of projective-carrier.md: the conic band bent isometrically into RP³; R = 1.

M(W) is the lune L = {|longitude| ≤ W} on a unit S², with vertices N and S = −N identified (§I); the lune point p has
colatitude θ from N and longitude λ. Let x = e₁, and let c be a unit-speed arc of length 2W on a circle of geodesic
radius ρ about e₄ in the unit sphere of x^⊥, with geodesic curvature κ = cot ρ: ρ = π/4 (κ = 1) while 2W < 2π sin(π/4),
and sin ρ = 0.98 beyond. Such an arc is simple and never meets −c whenever 2W < 2π sin ρ. The embedding is
    f(θ, λ) = cos θ · x + sin θ · c(λ),
a cone with vertices x and −x: every meridian is a great semicircle from x to −x, so −I identifies N and S.

Checks at W ∈ {0.3, 0.7, 1.2, 1.5, 2.0, 3.0} (exit 1 on any failure). The last two lie past π/2, where the unbent
carrier no longer embeds: under (A′) the bound W < π/2 is spectral, not a limit of the embedding.
  C1  f lies on S³
  C2  f is isometric: its pullback metric is the lune's round metric, dθ² + sin²θ dλ²
  C3  the pinch: every meridian runs from x to −x, so N and S are one point of RP³
  C4  f embeds M(W) in RP³: bi-Lipschitz from M(W)'s own metric to the distance of RP³
  C5  det A = 0 on the smooth locus: one principal curvature vanishes, |κ_min| ≤ 10⁻⁴ (1 + |κ_max|)
  C6  f is bent: H = κ/sin θ with κ = cot ρ, so f is never minimal
  C7  one-sided: along every meridian loop, which passes straight through the pinch with matching tangent planes,
      the normal returns reversed through the deck map −I
  C8  the pinch is not planar: its two sectors, the cones over c and over −c at x, span all of T_x S³
  C9  the edge's lift is an embedded closed curve that passes x once and −x once, as in Proposition 5
--arms plants a defect for each check and requires it to fire."""
import sys
import numpy as np

WIDTHS = (0.3, 0.7, 1.2, 1.5, 2.0, 3.0)
E = np.eye(4)
X0 = E[0]


def rho_for(W):
    return np.pi / 4 if 2 * W < 2 * np.pi * np.sin(np.pi / 4) else np.arcsin(0.98)


def arc(rho, speed=1.0):
    """Unit-speed (times speed) arc on the circle of geodesic radius rho about e₄ in the unit sphere of x^⊥."""
    def c(la):
        ph = speed * la / np.sin(rho)
        return np.cos(rho) * E[3] + np.sin(rho) * (np.cos(ph) * E[1] + np.sin(ph) * E[2])
    return c


def make_f(W, plant=None):
    if plant == "great-arc":
        c = arc(np.pi / 2)                                   # a great-circle arc: the premise's carrier
    elif plant == "twice":
        c = arc(np.arcsin(W / (2 * np.pi)))                  # circumference W, run twice over length 2W
    elif plant == "speed":
        c = arc(np.pi / 4, 1.1)
    else:
        c = arc(rho_for(W))
    apex = (lambda la: X0)
    if plant == "moving-apex":
        apex = lambda la: (X0 + 0.1 * la * E[3]) / np.linalg.norm(X0 + 0.1 * la * E[3])
    tilt = 0.2 if plant == "off-sphere" else 0.0

    def f(th, la):
        cc = c(la)
        if plant == "twist":
            nrm = np.cross(np.r_[cc[1:]], np.r_[(c(la + 1e-6) - c(la - 1e-6))[1:] / 2e-6])
            cc = np.cos(0.4 * th) * cc + np.sin(0.4 * th) * np.r_[0.0, nrm / np.linalg.norm(nrm)]
        return np.cos(th) * apex(la) + np.sin(th) * cc + tilt * np.sin(th) * X0
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
    return X, Xa, Xb, n, g, np.linalg.solve(g, b)


def lune_point(th, la):
    return np.array([np.sin(th) * np.cos(la), np.sin(th) * np.sin(la), np.cos(th)])


def core_normals(f, deck, la=0.0):
    """Unit normals along the meridian at longitude la, carried continuously; the first, the last, the tangent planes."""
    ths = np.linspace(0.01, np.pi - 0.01, 2001)
    prev, first = None, None
    for th in ths:
        X, Xa, Xb, n, _, _ = geometry(f, th, la)
        if prev is not None and n @ prev < 0:
            n = -n
        if first is None:
            first, plane0 = n, np.linalg.qr(np.vstack([Xa, Xb]).T)[0]
        prev = n
    plane1 = np.linalg.qr(np.vstack([Xa, Xb]).T)[0]
    return first, deck * prev, plane0, deck * plane1


def checks(W, plant=None):
    f = make_f(W, plant)
    kappa = 1 / np.tan(rho_for(W))
    r = {}
    ths = np.linspace(0.05, np.pi - 0.05, 40)
    las = np.linspace(-W, W, 9)
    on = iso = null = bent = 0.0
    for th in ths:
        for la in las:
            X, _, _, _, g, S = geometry(f, th, la)
            on = max(on, abs(np.linalg.norm(X) - 1))
            iso = max(iso, np.abs(g - np.diag([1.0, np.sin(th) ** 2])).max())
            ev = np.linalg.eigvals(S).real
            null = max(null, abs(ev[np.argmin(abs(ev))]) / (1 + abs(ev).max()))
            bent = max(bent, abs(abs(np.trace(S)) - kappa / np.sin(th)))
    r["C1 f lies on S³"] = on < 1e-12
    r["C2 isometric: the pullback metric is the lune's round metric"] = iso < 1e-5
    x = f(0.0, 0.0)
    apexes = [np.linalg.norm(f(0.0, la) - x) + np.linalg.norm(f(np.pi, la) + x) for la in las]
    r["C3 the pinch: every meridian runs from x to −x"] = max(apexes) < 1e-12
    pts = [(th, la) for th in np.linspace(0, np.pi, 61) for la in np.linspace(-W, W, 7)]
    P = np.array([lune_point(*p) for p in pts])
    F = np.array([f(*p) for p in pts])
    arcd = lambda U, V: 2 * np.arcsin(np.clip(np.linalg.norm(U - V, axis=-1) / 2, 0, 1))
    dL = arcd(P[:, None, :], P[None, :, :])
    dN, dS = arcd(P, np.array([0, 0, 1.0])), arcd(P, np.array([0, 0, -1.0]))
    dM = np.minimum(dL, np.minimum(dN[:, None] + dS[None, :], dS[:, None] + dN[None, :]))
    dRP = np.minimum(np.linalg.norm(F[:, None, :] - F[None, :, :], axis=2), np.linalg.norm(F[:, None, :] + F[None, :, :], axis=2))
    mask = dM > 1e-6
    ratio = (dRP[mask] / dM[mask]).min()
    r["C4 embeds M(W) in RP³: bi-Lipschitz from M(W)'s own metric"] = ratio > 0.05
    r["C5 det A = 0 on the smooth locus"] = null < 1e-4
    r["C6 bent: H = κ/sin θ with κ = cot ρ, so never minimal"] = bent < 1e-4
    deck = +1.0 if plant == "no-deck" else -1.0
    ok7 = True
    for la in las:
        n0, n1, pl0, pl1 = core_normals(f, deck, la)
        same_plane = np.linalg.svd(pl0.T @ pl1)[1].min() > 1 - 10 * 0.01**2   # the ends sit 0.01 from the pinch
        ok7 &= bool(n0 @ n1 < -0.99 and same_plane)                          # the sign decides
    r["C7 one-sided: every meridian loop returns the normal reversed through −I"] = ok7
    eps = 1e-4
    dirs = [f(eps, la) - x for la in las] + [-(f(np.pi - eps, la)) - x for la in las]
    dirs = np.array([d / np.linalg.norm(d) for d in dirs])
    sv = np.linalg.svd(dirs)[1]
    r["C8 the pinch is not planar: its two sectors span T_x S³"] = sv[2] > 1e-3
    # C9: trace the continuous lift of the band's edge, as lift_trace.py does for the unbent carrier
    ys = np.linspace(0, np.pi, 4001)
    ys = ys[np.abs(ys - np.pi / 2) > 1e-9]
    band = [(yv, +W) for yv in ys] + [(yv, -W) for yv in ys]
    to_lune = lambda yv, wv: (np.pi / 2 - yv, wv) if yv <= np.pi / 2 else (3 * np.pi / 2 - yv, -wv)
    lift = []
    for yv, wv in band:
        q = f(*to_lune(yv, wv))
        if lift and plant != "one-piece" and np.linalg.norm(-q - lift[-1]) < np.linalg.norm(q - lift[-1]):
            q = -q
        lift.append(q)
    lift = np.array(lift)
    steps = np.linalg.norm(np.diff(lift, axis=0), axis=1)
    closes = np.linalg.norm(lift[-1] - lift[0]) < 0.05
    runs = lambda target: int(np.sum(np.diff((np.linalg.norm(lift - target, axis=1) < 0.02).astype(int)) == 1)
                              + (np.linalg.norm(lift[0] - target) < 0.02))
    idx = np.arange(len(lift))
    sub = idx[::20]
    D = np.linalg.norm(lift[sub][:, None, :] - lift[sub][None, :, :], axis=2)
    gap = np.abs(sub[:, None] - sub[None, :])
    gap = np.minimum(gap, len(lift) - gap)
    embedded = D[gap > 200].min() > 0.02
    r["C9 the edge's lift: embedded, closed, through x and −x once each"] = bool(steps.max() < 0.05 and closes and embedded
                                                                            and runs(x) == 1 and runs(-x) == 1)
    return r, ratio, sv[2]


def main():
    res = {W: checks(W) for W in WIDTHS}
    allres = {W: v[0] for W, v in res.items()}
    names = list(next(iter(allres.values())))
    for name in names:
        ok = all(allres[W][name] for W in WIDTHS)
        print(("PASS " if ok else "FAIL ") + name)
    print("RP³ bi-Lipschitz constant by width: " + ", ".join(f"W = {W}: {res[W][1]:.3f}" for W in WIDTHS))
    print("pinch's third singular value by width: " + ", ".join(f"W = {W}: {res[W][2]:.3f}" for W in WIDTHS))
    green = all(all(v.values()) for v in allres.values())
    if "--arms" in sys.argv:
        assert green, "arms need a green parent"
        rc = 0
        C1, C2, C3, C4, C5, C6, C7, C8, C9 = names
        plants = {"off-sphere": [C1],        # a component along x added to the rulings
                  "speed": [C2],             # c run at speed 1.1
                  "moving-apex": [C3],       # the apex drifts with the longitude
                  "twice": [C4],             # c wraps its circle twice: not simple
                  "twist": [C5],             # each ruling turned out of its plane: not developable
                  "great-arc": [C6, C8],     # c a great arc: the unbent carrier, with a planar pinch
                  "no-deck": [C7],           # the pinch glued by the identity instead of −I
                  "one-piece": [C9]}         # the lift kept on one sheet: it jumps at the pinch
        for plant, targets in plants.items():
            out, _, _ = checks(0.7, plant)
            for tname in targets:
                fired = not out[tname]
                print(("ARM FIRED " if fired else "ARM SILENT ") + f"{tname} [{plant}]")
                rc |= 0 if fired else 1
        return rc
    return 0 if green else 1


if __name__ == "__main__":
    sys.exit(main())
