#!/usr/bin/env python3
"""The registered re-test of McKay Propagator Correction (registration of 2026-10-03).

Candidate: the literal path product of the page's §4.5, Pi_T(rho, sigma) = the product of T^2(i x sigma) over the
intermediate nodes i of the unique shortest McKay path from R0 to rho (§2.5; R0 and rho excluded), exponent 1, with no
fitted quantity. Two arms, declared both ways because the page does not say how Pi_T enters the mass: arm M multiplies the
predicted mass by Pi_T, arm D divides it by Pi_T. Each arm is re-benchmarked to the electron by applying the correction
relative to the electron's own factor at (R7, triv): arm M multiplies by Pi_T(rho, sigma) / Pi_T(R7, triv) and arm D
divides by that ratio, so the electron's prediction, which sets the scale, is unchanged.

Scored set: d at (R8, gal), mu and s at (R8, std), tau at (R4, gal), t at (R2, triv); r = log10(m_pred / m_obs).
Grade, per arm, all three required: (1) the uncentered RMS of r over the five falls; (2) every scored fermion ends within
the x3 window, |r| <= log10 3; (3) |r| falls for d and for tau. The test is positive if an arm passes (the two-arm
multiplicity reported), negative if both fail. Diagnostic only, not a p-value: the rank of the observed arrangement among
the 24 assignments of the four address corrections to the four addresses.

Inputs: ../mass-null-inputs.json, the torsion null test's frozen v1.1 inputs (SHA-256 pinned below); the McKay graph of
§2.5; mass-spectrum.md and mckay-propagator-correction.md at commit PIN, for the input gates.

Without --run: input gates and synthetic self-tests; no Pi_T is formed on the real table. --arms plants a defect for each
check and requires it to fire. With --run: refuses unless the script is unmodified at HEAD, HEAD is origin/main, the page
at HEAD carries this script's SHA-256 and no recorded run is at HEAD; then one run.
"""
import hashlib
import itertools
import json
import math
import os
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = subprocess.run(["git", "-C", HERE, "rev-parse", "--show-toplevel"], capture_output=True, text=True,
                      check=True).stdout.strip()
INPUTS = os.path.normpath(os.path.join(HERE, "..", "mass-null-inputs.json"))
INPUTS_SHA = "9efcd3f0766239d814745e184cab56dae2be2ba098cf773ea66a707e2d622237"
PIN = "3c7423b"
MS = "files/spectrum/files/mass-spectrum.md"
MP = "files/framework/files/working/files/mckay-propagator-correction.md"
EDGES = [("R0", "R1"), ("R1", "R3"), ("R3", "R6"), ("R6", "R7"), ("R7", "R8"), ("R8", "R5"), ("R5", "R2"), ("R8", "R4")]
VAC = ("triv", "std", "gal")
SCORED = [("d", "R8", "gal"), ("mu", "R8", "std"), ("s", "R8", "std"), ("tau", "R4", "gal"), ("t", "R2", "triv")]
BENCH = ("R7", "triv")
ADDRESSES = [("R8", "gal"), ("R8", "std"), ("R4", "gal"), ("R2", "triv")]
WINDOW = math.log10(3)
MASS_RTOL = 5e-3   # the page prints three figures and the frozen inputs carry published precision (C_geom 4 dp, mu_Lambda 2.25)
# each scored address and the benchmark, with its §III row key and its printed predicted mass, as mass-spectrum.md
# prints them at PIN (the row key and the strings are checked against the page by gate G5)
ROWS = {("R7", "triv"): ("| **10** | **$`R_7`$** | **4** | **triv** |", "5.21 \\times 10^{-4}", 5.21e-4),
        ("R8", "gal"): ("| 13 | $`R_8`$ | 5 | gal |", "1.51 \\times 10^{-2}", 1.51e-2),
        ("R8", "std"): ("| **15** | **$`R_8`$** | **5** | **std** |", "1.03 \\times 10^{-1}", 1.03e-1),
        ("R4", "gal"): ("| **17** | **$`R_4`$** | **6** | **gal** |", "4.89", 4.89),
        ("R2", "triv"): ("| **22** | **$`R_2`$** | **7** | **triv** |", "161.3", 161.3)}
# each scored fermion's observed mass as the page prints it on its address row (gate G6)
OBSERVED = {"d": ("4.67 \\times 10^{-3}", 4.67e-3), "mu": ("1.057 \\times 10^{-1}", 0.1057),
            "s": ("9.34 \\times 10^{-2}", 9.34e-2), "tau": ("1.777", 1.777), "t": ("172.7", 172.7)}


def git_show(rev, path):
    return subprocess.run(["git", "-C", REPO, "show", f"{rev}:{path}"], capture_output=True, text=True,
                          check=True).stdout


def bfs(edges):
    adj = {}
    for a, b in edges:
        adj.setdefault(a, []).append(b)
        adj.setdefault(b, []).append(a)
    dist, paths, frontier = {"R0": 0}, {"R0": [["R0"]]}, ["R0"]
    while frontier:
        nxt = []
        for u in frontier:
            for v in adj[u]:
                if v not in dist:
                    dist[v], paths[v] = dist[u] + 1, [p + [v] for p in paths[u]]
                    nxt.append(v)
                elif dist[v] == dist[u] + 1 and u in frontier:
                    paths[v] += [p + [v] for p in paths[u] if p + [v] not in paths[v]]
        frontier = nxt
    return dist, paths


def intermediates(paths, plant=None):
    out = {}
    for v, ps in paths.items():
        if v == "R0":
            continue
        p = ps[0]
        out[v] = p[1:] if plant == "path-includes-target" else p[1:-1]
    return out


def load(plant=None):
    raw = open(INPUTS, "rb").read()
    d = json.loads(raw)
    if plant == "torsion":
        d["T2_base"]["R3"] *= 1.01
    if plant == "observed":
        d["fermions"]["d"][2] *= 1.01
    if plant == "mass-scale":
        d["mu_Lambda_GeV"] *= 1.01
    return raw, d


def t2(d, rho, sig):
    return math.prod(d["T2_base"][tau] ** n for tau, n in d["tensor_multiplicities_N"][f"{rho}_{sig}"].items())


def mass(d, dist, rho, sig):
    return d["mu_Lambda_GeV"] * d["C_geom"][rho] * d["sqrt_Omega_Lambda"] ** (dist[rho] / 30.0) * t2(d, rho, sig)


def pi_t(t2fn, inter, rho, sig):
    return math.prod(t2fn(i, sig) for i in inter[rho])


def deltas(t2fn, inter, plant=None):
    """log10 Pi_T at each scored address, re-benchmarked to the electron's own factor."""
    bench = 0.0 if plant == "no-benchmark" else math.log10(pi_t(t2fn, inter, *BENCH))
    return {a: math.log10(pi_t(t2fn, inter, *a)) - bench for a in ADDRESSES}


def rms(xs, plant=None):
    xs = list(xs)
    if plant == "centered":
        m = sum(xs) / len(xs)
        xs = [x - m for x in xs]
    return math.sqrt(sum(x * x for x in xs) / len(xs))


def grade(r0, delta, sign, plant=None):
    """r0: {fermion: r}; delta: {address: log10 correction}; sign +1 for arm M, -1 for arm D."""
    if plant == "sign-swap":
        sign = -sign
    addr = {f: (rho, sig) for f, rho, sig in SCORED}
    r1 = {f: r0[f] + sign * delta[addr[f]] for f in r0}
    c1 = rms(r1.values(), plant) < rms(r0.values(), plant)
    c2 = all(abs(x) <= WINDOW for x in r1.values())
    c3 = abs(r1["d"]) < abs(r0["d"]) and abs(r1["tau"]) < abs(r0["tau"])
    return r1, (c1, c2, c3), c1 and c2 and c3


def rank(r0, delta, sign, plant=None):
    """1 + the number of the 24 arrangements of the four address corrections with a strictly smaller corrected RMS,
    the observed arrangement among them; also the number of arrangements tied with it."""
    addr = {f: (rho, sig) for f, rho, sig in SCORED}
    def corrected(assign):
        return rms(r0[f] + sign * assign[addr[f]] for f in r0)
    obs = corrected(delta)
    vals = [corrected(dict(zip(ADDRESSES, [delta[a] for a in perm]))) for perm in itertools.permutations(ADDRESSES)]
    smaller = sum(v < obs - 1e-12 for v in vals)
    ties = sum(abs(v - obs) <= 1e-12 for v in vals) - 1
    return smaller + (2 if plant == "rank" else 1), ties, len(vals)


def decimals(s):
    return len(s.split(".")[1]) if "." in s else 0


def gates(plant=None):
    """G1-G6 on the real inputs. None forms Pi_T."""
    res = {}
    raw, d = load(plant)
    pinned = INPUTS_SHA if plant != "inputs-hash" else INPUTS_SHA[:-1] + ("0" if INPUTS_SHA[-1] != "0" else "1")
    res["G1 the inputs file carries the pinned SHA-256"] = hashlib.sha256(raw).hexdigest() == pinned
    edges = EDGES if plant != "graph" else [e if e != ("R8", "R4") else ("R5", "R4") for e in EDGES]
    dist, paths = bfs(edges)
    res["G2 the graph's distances match the inputs and every shortest path is unique"] = (
        all(dist.get(r) == d["mckay_distance"][r] for r in d["mckay_distance"]) and all(len(p) == 1 for p in paths.values()))
    inter = intermediates(paths, plant)
    page_mp = git_show(PIN, MP)
    ok3 = True
    for v in sorted(d["mckay_distance"]):
        row = f"| {v} | {'→'.join(paths[v][0])} | {dist[v]} | {', '.join(inter[v]) if inter[v] else 'none'} |"
        ok3 &= row in page_mp
    res["G3 every path and its intermediate nodes match §2.5's table"] = ok3
    page_ms = git_show(PIN, MS)
    i0 = page_ms.index("The 24 vacuum torsion values follow from")
    block = page_ms[i0:page_ms.index("### 5. Independent Reproduction", i0)]
    ok4, seen = True, 0
    for line in block.split("\n"):
        if line.startswith("| $`R_") and line.count("|") == 5:
            cells = [c.strip() for c in line.strip("|").split("|")]
            rho = "R" + cells[0].split("R_")[1][0]
            for sig, cell in zip(VAC, cells[1:]):
                ok4 &= abs(t2(d, rho, sig) - float(cell)) <= 0.5 * 10 ** -decimals(cell) + 1e-12
                seen += 1
    res["G4 the 24 torsion values reproduce mass-spectrum §4's table"] = ok4 and seen == 24
    lines = page_ms.split("\n")
    ok5 = True
    for (rho, sig), (key, printed, value) in ROWS.items():
        row = [l for l in lines if l.startswith(key)]
        ok5 &= len(row) == 1 and printed in row[0]
        ok5 &= abs(mass(d, dist, rho, sig) / value - 1) <= MASS_RTOL
    res["G5 the predicted masses at the scored addresses and the benchmark reproduce §III"] = ok5
    ok6 = True
    for f, rho, sig in SCORED:
        key = ROWS[(rho, sig)][0]
        row = [l for l in lines if l.startswith(key)]
        printed, value = OBSERVED[f]
        ok6 &= len(row) == 1 and printed in row[0] and d["fermions"][f][2] == value
    res["G6 the observed masses match the inputs and §III"] = ok6
    return res, (d, dist, inter)


def selftests(plant=None):
    """S1-S4 on synthetic inputs."""
    res = {}
    dist, paths = bfs([("R0", "A"), ("A", "B"), ("B", "C")])
    inter = intermediates(paths, plant)
    toy = {"A": 2.0, "B": 3.0, "C": 5.0}
    res["S1 the path product takes the intermediate nodes only"] = pi_t(lambda i, s: toy[i], inter, "C", "x") == 6.0
    only_r1 = lambda i, s: 7.0 if i == "R1" else 1.0   # R1 is an intermediate node on every scored path and the benchmark's
    inter_real = intermediates(bfs(EDGES)[1])
    res["S2 a factor common to every address and the benchmark cancels"] = all(
        abs(v) < 1e-12 for v in deltas(only_r1, inter_real, plant).values())
    r0 = {"d": 0.5, "mu": 0.0, "s": 0.0, "tau": 0.4, "t": 0.0}
    cancel = {("R8", "gal"): 0.5, ("R8", "std"): 0.0, ("R4", "gal"): 0.4, ("R2", "triv"): 0.0}
    _, _, pass_d = grade(r0, cancel, -1, plant)
    _, _, pass_m = grade(r0, cancel, +1, plant)
    # a correction that leaves every residual at +0.35: uncentered RMS rises, so the arm fails; a centered RMS would pass it
    shift = {("R8", "gal"): 0.15, ("R8", "std"): -0.35, ("R4", "gal"): 0.05, ("R2", "triv"): -0.35}
    _, _, pass_shift = grade(r0, shift, -1, plant)
    res["S3 the grade passes an exact cancellation in its own arm only and fails a uniform shift"] = (
        pass_d and not pass_m and not pass_shift)
    r0s = {"d": 0.5, "mu": 0.1, "s": 0.1, "tau": 0.3, "t": -0.2}
    dl = {("R8", "gal"): 0.5, ("R8", "std"): 0.1, ("R4", "gal"): 0.3, ("R2", "triv"): -0.2}
    rk, ties, n = rank(r0s, dl, -1, plant)
    res["S4 the diagnostic ranks the exact cancellation first among 24"] = (rk, ties, n) == (1, 0, 24)
    return res


TARGETS = {"inputs-hash": ["G1"], "graph": ["G2", "G3"], "path-includes-target": ["G3", "S1"], "torsion": ["G4"],
           "mass-scale": ["G5"], "observed": ["G6"], "no-benchmark": ["S2"], "centered": ["S3"], "sign-swap": ["S3"],
           "rank": ["S4"]}


def checks(plant=None):
    g, ctx = gates(plant)
    s = selftests(plant)
    return {**g, **s}, ctx


def guard():
    me = os.path.relpath(os.path.abspath(__file__), REPO)
    sha = hashlib.sha256(open(__file__, "rb").read()).hexdigest()
    tracked = subprocess.run(["git", "-C", REPO, "ls-files", "--error-unmatch", me], capture_output=True).returncode == 0
    clean = tracked and subprocess.run(["git", "-C", REPO, "diff", "--quiet", "HEAD", "--", me]).returncode == 0
    head = subprocess.run(["git", "-C", REPO, "rev-parse", "HEAD"], capture_output=True, text=True).stdout.strip()
    main = subprocess.run(["git", "-C", REPO, "rev-parse", "origin/main"], capture_output=True, text=True).stdout.strip()
    registered = sha in git_show("HEAD", MP)
    out = os.path.relpath(os.path.join(HERE, "retest.out"), REPO)
    unrun = subprocess.run(["git", "-C", REPO, "cat-file", "-e", f"HEAD:{out}"], capture_output=True).returncode != 0
    return {"the script is unmodified at HEAD": clean, "HEAD is origin/main": head == main and bool(head),
            "the page at HEAD carries this script's SHA-256": registered, "no recorded run is at HEAD": unrun}


def run(ctx):
    d, dist, inter = ctx
    t2fn = lambda rho, sig: t2(d, rho, sig)
    r0 = {f: math.log10(mass(d, dist, rho, sig) / d["fermions"][f][2]) for f, rho, sig in SCORED}
    delta = deltas(t2fn, inter)
    addr = {f: (rho, sig) for f, rho, sig in SCORED}
    arms = {"M (multiply by Pi_T)": +1, "D (divide by Pi_T)": -1}
    graded = {name: grade(r0, delta, s) for name, s in arms.items()}
    print(f"{'f':4s} {'address':12s} {'r before':>9s} {'log10 Pi_T rel. e':>18s} {'r, arm M':>9s} {'r, arm D':>9s}")
    for f, rho, sig in SCORED:
        print(f"{f:4s} {'(' + rho + ', ' + sig + ')':12s} {r0[f]:+9.3f} {delta[addr[f]]:+18.3f} "
              f"{graded['M (multiply by Pi_T)'][0][f]:+9.3f} {graded['D (divide by Pi_T)'][0][f]:+9.3f}")
    print(f"uncentered RMS before: {rms(r0.values()):.3f}")
    passed = []
    for name, s in arms.items():
        r1, (c1, c2, c3), ok = graded[name]
        rk, ties, n = rank(r0, delta, s)
        print(f"arm {name}: RMS after {rms(r1.values()):.3f}; (1) RMS falls {c1}; (2) all within x3 {c2}; "
              f"(3) d and tau shrink {c3}: {'PASS' if ok else 'FAIL'}; diagnostic rank {rk} of {n}, {ties} tied")
        if ok:
            passed.append(name)
    print("VERDICT: " + (f"POSITIVE, arm {passed[0]} of two declared arms, suggestive only" if len(passed) == 1 else
                         "POSITIVE, both arms (check)" if passed else "NEGATIVE, both arms fail"))


def main():
    res, ctx = checks()
    for name, ok in res.items():
        print(("PASS " if ok else "FAIL ") + name)
    green = all(res.values())
    rc = 0 if green else 1
    if "--arms" in sys.argv:
        assert green, "arms need a green parent"
        for plant, targets in TARGETS.items():
            try:
                r_p, _ = checks(plant)
            except (ValueError, KeyError, IndexError):
                r_p = None
            for target in targets:
                fired = r_p is None or not next(ok for name, ok in r_p.items() if name.startswith(target + " "))
                print(("ARM FIRED " if fired else "ARM SILENT ") + f"{target} [{plant}]")
                rc |= 0 if fired else 1
    if "--run" in sys.argv:
        if not green:
            print("REFUSED: a check fails")
            return 1
        g = guard()
        for name, ok in g.items():
            print(("PASS " if ok else "REFUSED ") + "guard: " + name)
        if not all(g.values()):
            return 1
        run(ctx)
    return rc


if __name__ == "__main__":
    sys.exit(main())
