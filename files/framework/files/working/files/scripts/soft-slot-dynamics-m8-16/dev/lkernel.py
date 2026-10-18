#!/usr/bin/env python3
"""Step 1 of SLOWPAIR_PLAN.md: the controls' L kernel. Cases: theoremD:R3 (C1), C2a, C2b, C3.

Usage: lkernel.py CONTROL (C1, C2a, C2b or C3). Measured, not scored: the numbers set Step 2's proposal, which the
units review before any cut is chosen (UA). Nothing here changes the record.

Where (SLOWPAIR_PLAN.md, Step 1):
  C1 (D6's Theorem D member, R3): N = 16, 24, 32, 40 at eps in {0.5, 1, 2}, c = sqrt(eps) v exactly, lam = 8 + eps; no
     solve.
  C2a, C2b, C3: N = 16 and 24 along M8.15's full ladder(0.25, eps_max) from the germ, continued point by point as in
     d7_ladders.py; and N = 32 at eps in {0.5, 1, 2} from the germ at 0.5, as in D7's sample (d7_controls.py).

What, at each point (L = the Hessian F'', real symmetric of size 2m):
  - L's spectrum by |mu|: its kernel, the k smallest, k = V0's chains from EXPECTED_V0.md (C1 5, C2a 3, C2b 5, C3 4),
    and the lift, their largest |mu| against ||L|| (the largest |mu|); the smallest genuine |mu|, the (k+1)-th;
  - L's zero count under today's cut (1e-10 ||L||) against those chains (UB's zero-count check, on every control point);
  - ||L t|| / (||L|| ||t||) for every declared kernel tangent (UA): the right generators' T_a c, the phase i c, and in R2
    the fibre structure's J c and i J c (branches.tangent_vectors); at C1, its rigid family's five real directions,
    the lowest level's real span orthogonal to v. D4's identity, L (T c) = T F'(c), is used where D4 established it,
    for the generators, the phase and, in R2, J (d4_invariance.py's claim 3), never for C1's family directions: at a
    solution both sides sit near round-off, so ||T F'(c)|| is reported as the lift's predictor beside the measured
    ||L T c||, each over ||L|| ||T c||, with u for the round-off;
  - the Newton floor (the continuation's last accepted step);
  - at D7's points: the slow eigenvalues of A, typed outside the production gray zone and below 1; s_min, the slowest;
    rho = (the smallest genuine |mu|) / (2 omega s_min) (UB); and for each slow group, L restricted to the real span
    of its eigenvectors' position parts: its eigenvalues, the anisotropy r = |k_max| / |k_min|, and
    sqrt|k_min k_max| / (2 omega s), which is 1 at leading order for a soft-soft pair.
"""
import json
import os
import sys
import time
import numpy as np
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, ROOT)
sys.path.insert(0, HERE)
from instrument import basis, functional as fn, linear as ln, branches as br, devtools  # noqa: E402
import d7_ladders as d7l  # noqa: E402

U = np.finfo(float).eps
CUT = 1e-10                                   # L's zero cut today (linear.record's zero_rel)
out, rec = [], {}


def say(s=''):
    print(s, flush=True)
    out.append(s)


def chains(rows, name):
    row = rows[name]
    return row['dim'] - row['ranks'][0]


def measure_L(Fn, c, lam, k, tangents, gens):
    t0 = time.perf_counter()
    L = Fn.hess_dense(c, lam)
    t_h = time.perf_counter() - t0
    mu, Q = np.linalg.eigh(L)
    nL = float(np.abs(mu).max())
    order = np.argsort(np.abs(mu))
    kern = np.abs(mu[order[:k]]) / nL
    genuine = float(np.abs(mu[order[k]]) / nL)
    zeros = int(np.sum(np.abs(mu) <= CUT * nL))
    tres = [float(np.linalg.norm(L @ t) / (nL * np.linalg.norm(t))) for t in tangents]
    g = Fn.grad(c, lam)
    d4 = []                                   # per generator: (measured ||L T c||, D4's ||T F'(c)||), each over ||L|| ||T c||
    for Tc, Tg in gens(c, g):
        sc = nL * np.linalg.norm(Tc)
        d4.append((float(np.linalg.norm(L @ fn.to_real(Tc)) / sc), float(np.linalg.norm(Tg) / sc)))
    return dict(L=L, normL=nL, kernel=[float(x) for x in kern], lift=float(kern.max()), genuine=genuine, zeros=zeros,
                tangent_res=tres, d4=d4, seconds_hessian=t_h)


def generators(Fn, K):
    def gens(c, g):
        out_ = [(T @ c, T @ g) for T in fn.right_generators(Fn.B)] + [(1j * c, 1j * g)]
        if K is not None:
            out_ += [(K @ c.conj(), K @ g.conj()), (1j * (K @ c.conj()), 1j * (K @ g.conj()))]
        return out_
    return gens


def slow_structure(L, A, lam, m_amp, normA):
    """The slow eigenvalues of A (typed outside the production gray zone, below 1), s_min, and each slow group's L
    restricted to the real span of its eigenvectors' position parts."""
    ev, V = np.linalg.eig(A)
    mg = ln.margin(normA, m_amp)
    a = np.abs(ev)
    slow = np.where((a >= ln.GRAY * mg) & (a < 1.0))[0]
    if not len(slow):
        return None
    omega = np.sqrt(lam)
    n2 = L.shape[0]
    groups, used = [], set()
    for j in slow[np.argsort(a[slow])]:
        if j in used:
            continue
        idx = [i for i in slow if abs(a[i] - a[j]) <= 1e-6 * a[j]]
        used.update(idx)
        P = V[:n2, idx]
        R = np.concatenate([P.real, P.imag], axis=1)
        Uq, sv, _ = np.linalg.svd(R, full_matrices=False)
        Qs = Uq[:, sv > 1e-8 * sv.max()]
        kk = np.linalg.eigvalsh(Qs.T @ L @ Qs)
        kmin, kmax = float(np.abs(kk).min()), float(np.abs(kk).max())
        groups.append(dict(s=float(a[j]), n=len(idx), k=[float(x) for x in kk], r=kmax / kmin,
                           lead=float(np.sqrt(kmin * kmax) / (2 * omega * a[j]))))
    return dict(s_min=float(a[slow].min()), omega=float(omega), groups=groups)


def point(name, N, eps, Fn, c, lam, k, K, steps=None, with_slow=False, t_solve=0.0):
    t0 = time.perf_counter()
    tangents = br.tangent_vectors(Fn, c, K)
    family = []
    if name == 'C1':
        B = Fn.B
        low = np.array([n == B.levels[0] for n, _, _ in B.index])
        E = np.eye(B.m)[:, low]
        R = np.concatenate([np.concatenate([E, np.zeros_like(E)]), np.concatenate([np.zeros_like(E), E])], axis=1)
        v = fn.to_real(c) / np.linalg.norm(c)
        R = R - np.outer(v, v @ R)
        Uq, sv, _ = np.linalg.svd(R, full_matrices=False)
        family = list(Uq[:, sv > 1e-8].T)
    m_ = measure_L(Fn, c, lam, k, tangents + family, generators(Fn, K))
    floor = steps[-1]['floor'] if steps else None
    entry = dict(N=N, eps=eps, lam=lam, m=float(np.vdot(c, c).real), floor=floor, normL=m_['normL'],
                 kernel=m_['kernel'], lift=m_['lift'], genuine=m_['genuine'], zeros=m_['zeros'], chains=k,
                 tangent_res_sym=m_['tangent_res'][:len(tangents)], tangent_res_family=m_['tangent_res'][len(tangents):],
                 d4=m_['d4'], seconds_hessian=m_['seconds_hessian'], seconds_solve=t_solve)
    if with_slow:
        A, _, _ = ln.first_order(m_['L'], np.sqrt(lam))
        sl = slow_structure(m_['L'], A, lam, entry['m'], np.linalg.norm(A, 2))
        if sl:
            entry.update(s_min=sl['s_min'], rho=m_['genuine'] * m_['normL'] / (2 * sl['omega'] * sl['s_min']),
                         slow_groups=sl['groups'])
    entry['seconds'] = time.perf_counter() - t0 + t_solve
    rec[f'N{N}_eps{eps}'] = entry
    tr = entry['tangent_res_sym'] + entry['tangent_res_family']
    line = (f"   N {N} eps {eps:8.4f}: lift {entry['lift']:.1e} ||L|| (tangents {max(tr):.1e}); genuine {entry['genuine']:.1e};"
            f" zeros {entry['zeros']} of {k} chains; D4's ||T F'|| {max(x[1] for x in entry['d4']):.1e}")
    if floor is not None:
        line += f"; floor {floor:.1e}"
    if 'rho' in entry:
        line += (f"; s_min {entry['s_min']:.2e}, rho {entry['rho']:.3f}, r "
                 f"{', '.join(f'{g_["r"]:.2f}' for g_ in entry['slow_groups'][:3])}")
    say(line + f"; {entry['seconds']:.0f} s")


def run_ladder(name, N, targets, rows, E):
    case, slot, n0 = br.CASES[name]
    B = basis.Basis(slot, N)
    Fn = fn.Functional(B)
    K = fn.fibre_structure_matrix(Fn)[1] if slot == 'R2' else None
    u = br.seed_state(name, B)
    chk = br.orbit_checks(Fn, u, K)
    k = chains(rows, name)
    say(f"{name} N = {N}, m = {B.m}: {len(targets)} points from the germ; Q(u) {chk['Q']:.12f}, (k, r_u) = ({chk['k']}, {chk['r']})")
    c_prev, lam_prev, slope, acc = np.sqrt(targets[0] / chk['Q']) * u, E['lam0'] + targets[0], 1 / chk['Q'], False
    fails = 0
    for eps in targets:
        t0 = time.perf_counter()
        res = br.continue_to(Fn, E['lam0'], eps, c_prev, lam_prev, slope, K=K, prev_accepted=acc)
        if not res['ok'] or not all(s['accepted'] for s in res['steps']):
            say(f"   N {N} eps {eps:.4f}: NOT ACCEPTED ({res.get('reason')}); the ladder ends here")
            fails += 1
            break
        point(name, N, eps, Fn, res['c'], res['lam'], k, K, res['steps'], with_slow=True, t_solve=time.perf_counter() - t0)
        c_prev, lam_prev, slope, acc = res['c'], res['lam'], res['slope'], True
    return fails


def main():
    name = sys.argv[1]
    assert name in ('C1', 'C2a', 'C2b', 'C3')
    case = br.CASES[name][0]
    devtools.require(case)
    rows, sha = br.expected_v0(ROOT)
    t_all = time.perf_counter()
    fails = 0
    say(f"lkernel, {name}: L's kernel at the control's points (SLOWPAIR_PLAN.md, Step 1); EXPECTED_V0.md SHA-256 {sha},"
        f" chains {chains(rows, name)}")
    if name == 'C1':
        for N in (16, 24, 32, 40):
            B = basis.Basis('R3', N)
            Fn = fn.Functional(B)
            v = br.seed_state('C1', B)
            say(f"C1 N = {N}, m = {B.m}")
            for eps in (0.5, 1.0, 2.0):
                point('C1', N, eps, Fn, np.sqrt(eps) * v, 8.0 + eps, chains(rows, 'C1'), None)
    else:
        E = d7l.EXPECT[name]
        full = d7l.ladder(0.25, E['eps_max'])
        for N in (16, 24):
            fails += run_ladder(name, N, full, rows, E)
        fails += run_ladder(name, 32, [0.5, 1.0, 2.0], rows, E)
    pts = list(rec.values())
    lift = max(p['lift'] for p in pts)
    tres = max(max(p['tangent_res_sym'] + p['tangent_res_family']) for p in pts)
    gen = min(p['genuine'] for p in pts)
    mism = [(p['N'], p['eps'], p['zeros']) for p in pts if p['zeros'] != p['chains']]
    rho = [p['rho'] for p in pts if 'rho' in p]
    rr = [g_['r'] for p in pts for g_ in p.get('slow_groups', [])]
    d4m = max(x[0] for p in pts for x in p['d4'])
    d4p = max(x[1] for p in pts for x in p['d4'])
    say(f"{name}: {len(pts)} points; the kernel's largest lift {lift:.1e} ||L|| (its tangents' {tres:.1e}); the smallest"
        f" genuine |mu| {gen:.1e} ||L||; L's zero count differs from the chains at {len(mism)} points {mism[:6]}; the"
        f" generators' ||L T c|| up to {d4m:.1e} against D4's ||T F'(c)|| up to {d4p:.1e} and u = {U:.1e}"
        + (f"; rho {min(rho):.3f} to {max(rho):.3f}; r up to {max(rr):.2f}" if rho else '')
        + f"; {fails} ladders ended early; compute {(time.perf_counter() - t_all) / 60:.1f} min")
    path = os.path.join(HERE, f'lkernel_{name}.out')
    jpath = os.path.join(HERE, f'lkernel_{name}.json')
    with open(path, 'w', encoding='utf-8') as f:
        f.write('\n'.join(out) + '\n')
    with open(jpath, 'w', encoding='utf-8') as f:
        json.dump(rec, f, indent=1, default=float)
    devtools.log_run(os.path.abspath(__file__), case,
                     [f"Step 1, {name}: {len(pts)} points measured; largest kernel lift {lift:.1e} ||L||, smallest genuine"
                      f" {gen:.1e} ||L||; zero-count mismatches {len(mism)}; {fails} ladders ended early. Measured, not scored.",
                      f'EXPECTED_V0.md SHA-256 {sha} (as logged before any control ran).'], outputs=(path, jpath))


if __name__ == '__main__':
    main()
