"""Review of the first-positive transfer run, the numbers (2026-09-28). Reads the run's results in ../run-1/ and checks
them against transfer_kernel.py.
Each check prints PASS or FAIL; each has a planted defect that must trip it."""
import json, math, os, sys
from transfer_kernel import run, dimE
ROOM = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "run-1") + os.sep
key = lambda r: (r["tau"], r["n"], r["placement"], r["W"])
R = {key(r): r for r in json.load(open(ROOM + "results.json"))}
S = {key(r): r for r in json.load(open(ROOM + "results_sctm.json"))}
Gd = {key(r): r for r in json.load(open(ROOM + "results_ground.json"))}
TOL = 1e-3
ok = True
def report(name, passed, detail):
    global ok; ok &= passed; print(("PASS " if passed else "FAIL ") + name + ": " + detail); sys.stdout.flush()
# N1: closed forms. ||O0||^2 = 2 dim(E) W/pi^2 (kernel diagonal constant, <gq,q> = Re g);
#     ||O1||^2 = 2 n(n+2) dim(E) W/(3 pi^2) (the tangential density is constant and isotropic).
def n1(tf=lambda n: n * (n + 2)):
    w = 0
    for r in R.values():
        t, n, W = r["tau"], r["n"], r["W"]; dE = dimE(t, n)
        w = max(w, abs(r["hs_val"] / (2 * dE * W / math.pi ** 2) - 1))
        et = 2 * tf(n) * dE * W / (3 * math.pi ** 2)
        w = max(w, abs(r["hs_trans"] / et - 1) if et else abs(r["hs_trans"]))
    return w
w = n1(); report("N1 closed-form norms, all rows", w < TOL, f"{len(R)} rows, worst relative deviation {w:.2e}")
w = n1(lambda n: n * (n + 1)); print(f"   arm N1 (n(n+1) for n(n+2)): worst {w:.2e} -> {'trips' if w >= TOL else 'MISSED'}"); ok &= w >= TOL
# N2: the arm labels follow tau(-1): value output twisted iff tau is spinorial; transverse the reverse.
SPIN = {"2", "2p", "4p", "6"}
def n2(rows):
    return [k for k, r in rows.items() if (r["val_arm"] == "twisted") != (k[0] in SPIN) or (r["trans_arm"] == "twisted") != (k[0] not in SPIN)]
bad = n2(R); report("N2 arm labels", not bad, f"{len(R)} rows, {len(bad)} mislabeled")
k0 = next(iter(R)); mut = dict(R); mut[k0] = dict(R[k0], val_arm="twisted" if R[k0]["val_arm"] == "untwisted" else "untwisted")
print(f"   arm N2 (one label flipped): {len(n2(mut))} mislabeled -> {'trips' if n2(mut) else 'MISSED'}"); ok &= bool(n2(mut))
# N3: six rows reproduced: norm, first-positive projection (Friedrichs, and same-trace where untwisted), ground projection.
ROWS = [("1", 12, "generic", 0.25), ("4", 6, "3fold", 1.0), ("2p", 13, "5fold", 1.4),
        ("1", 20, "2fold", 0.5), ("6", 7, "generic", 1.0), ("3p", 10, "5fold", 0.5)]
def pairs(k, m):
    r, s, g = R[k], S[k], Gd[k]; out = []
    for samp in ("val", "trans"):
        a = "tw" if r[f"{samp}_arm"] == "twisted" else "un"; hs = m[f"hs_{samp}"]
        out += [(samp, "HS", r[f"hs_{samp}"], m[f"hs_{samp}"], hs), (samp, "P1 Friedrichs", r[f"proj_{samp}"], m[f"{samp}:{a}_F_P1"], hs),
                (samp, "P0 Friedrichs", g[f"proj0_{samp}"], m[f"{samp}:{a}_F_P0"], hs)]
        if a == "un": out.append((samp, "P1 same-trace", s[f"proj_{samp}_sctm"], m[f"{samp}:un_SCTM_P1"], hs))
    return out
worst = 0
for k in ROWS:
    m = run(*k)
    for samp, nm, u, me, hs in pairs(k, m):
        d = abs(u - me) / hs; worst = max(worst, d)
        print(f"   {str(k):28s} {samp:5s} {nm:14s} run {u:.6e}  review {me:.6e}  |diff|/norm {d:.1e}")
report("N3 six rows reproduced", worst < TOL, f"{len(ROWS)} rows, worst |diff|/norm {worst:.1e}")
# The unflipped map is the flipped one with w -> -w beyond the pinch, so only a w-odd target can see it: the same-trace
# mode for W > pi/4. The arm runs on the second row (W = 1, untwisted value output).
m = run(*ROWS[1], mutate="seam"); wm = max(abs(u - me) / hs for _, _, u, me, hs in pairs(ROWS[1], m))
print(f"   arm N3 (unflipped band map, second row): worst {wm:.1e} -> {'trips' if wm >= TOL else 'MISSED'}"); ok &= wm >= TOL
# N4: the margin. Every graded row leaks by far more than the run's quadrature error.
def n4(rows):
    fr = []
    for k, r in rows.items():
        if k[1] == 0: continue
        for samp in ("val", "trans"):
            hs = r[f"hs_{samp}"]; fr.append(r[f"lambda_{samp}"] / hs)
            p = S[k].get(f"proj_{samp}_sctm")
            if r[f"{samp}_arm"] == "untwisted" and p is not None: fr.append((hs - p) / hs)
    return min(fr), len(fr)
mn, cnt = n4(R); report("N4 leakage margin", mn > 100 * TOL, f"{cnt} graded values, smallest Lambda/norm {mn:.3f}")
mut = dict(R); k1 = ("3", 2, "generic", 0.25); mut[k1] = dict(R[k1], lambda_val=0.0)
print(f"   arm N4 (one planted zero): smallest {n4(mut)[0]:.3f} -> {'trips' if n4(mut)[0] <= 100 * TOL else 'MISSED'}"); ok &= n4(mut)[0] <= 100 * TOL
print("ALL PASS, every arm trips" if ok else "NOT ALL PASS")
