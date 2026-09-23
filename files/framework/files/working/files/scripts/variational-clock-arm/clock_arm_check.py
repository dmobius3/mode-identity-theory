#!/usr/bin/env python3
"""The checks behind The Variational Clock Arm (variational-clock-arm.md): what the lapse equation decides.

  V1  the budget identity is the Rayleigh oscillator's energy integral, and the realized share is twice the wave's rate
  V2  T/N + N W is reparametrization invariant; T/N^a + N^b W only at a = b = 1; degree p needs T/N^(p-1) + N W
  V3  the lapse equation gives N^2 = T/W and eliminates to 2 sqrt(T W), symmetric in T and W; degree p gives
      N^p = (p-1) T/W
  V4  with the Rayleigh kinetic term, a potential c S^w gives N = S^((2-w)/2) / (2 sqrt c) and on-shell action
      sqrt(c) S^((2+w)/2); at c = 1/4 the three native levels give N = 1, S^(1/2), S
  V5  the constrained variation (N, S, Psi and the multiplier) admits the standing wave at every level w
  V6  the budget-metric kinetic term needs the potential 1/(4S), off the native levels, for N = S^(1/2)
  V7  the three named second consequences: the tick measure is the on-shell action, 2 N W, fixed by the choice that
      set the lapse; the realization-rate candidate has the same S^(3/2) weight and no R equation of its own here;
      the dressed lapse's Lambda piece is absent (beta = 0)
  V8  inside the class, with the levels at intensity and amplitude, the clock exponent is exactly 1/2; action times
      lapse is 2T whatever the potential, so the potential that gives N = S^(1/2+eps) makes the action S^(3/2-eps)
      against the eps family's tick S^(3/2+eps): the two meet only at eps = 0
The standing wave is Psi = cos(t/2), S = sin(t/2); along it Psi' = -S/2 and S' = Psi/2, so every check is written
in s = S > 0 and psi = Psi, and time derivatives are taken by that chain rule. Each check carries a control that
must come out the other way. Every quantity is exact.
"""
import sys

import sympy as sp

t = sp.symbols("t", real=True)
s, c, w, tp = sp.symbols("s c w tp", positive=True)
psi = sp.symbols("psi", real=True)
a, b, T, W, n = sp.symbols("a b T W n", positive=True)
q = sp.symbols("q", positive=True)   # degree p = q + 1 of the kinetic term
eps, al, be = sp.symbols("epsilon alpha beta", real=True)


def z(expr):
    """Exactly zero after simplification."""
    return sp.simplify(sp.powsimp(sp.expand(expr), force=True)) == 0


def ddt(f):
    """Time derivative along the standing wave: S' = Psi/2, Psi' = -S/2."""
    return sp.diff(f, s) * psi / 2 + sp.diff(f, psi) * (-s / 2)


def lapse(kinetic, potential):
    return sp.sqrt(kinetic / potential)


def main():
    checks, controls = [], []
    rayleigh_T = (s / 2) ** 2                      # Psi'^2 on the standing wave
    budget_T = (s / 2) ** 2 + (psi / 2) ** 2       # Psi'^2 + S'^2

    # V1
    P, Q = sp.cos(t / 2), sp.sin(t / 2)
    v1 = [sp.diff(P, t, 2) + P / 4, 4 * (sp.diff(P, t) ** 2 + P ** 2 / 4) - 1, Q + 2 * sp.diff(P, t)]
    checks.append(("V1 budget identity = Rayleigh energy integral; S = -2 Psi'", all(sp.simplify(e) == 0 for e in v1),
                   "Psi'' + Psi/4, 4(Psi'^2 + Psi^2/4) - 1 and S + 2 Psi' all vanish"))
    Pw, Qw = sp.cos(t), sp.sin(t)
    controls.append(("V1 the whole-angle wave's energy integral is not its budget",
                     sp.simplify(4 * (sp.diff(Pw, t) ** 2 + Pw ** 2 / 4) - (Pw ** 2 + Qw ** 2)) != 0))

    # V2: under t -> t(sigma), a degree-p kinetic term goes T -> T tp^p, N -> N tp, and L dt -> L tp dsigma
    def reparam_gap(pa, pb, deg=2):
        return (T * tp ** deg / (n * tp) ** pa + (n * tp) ** pb * W) - (T / n ** pa + n ** pb * W) * tp
    checks.append(("V2 T/N + N W is reparametrization invariant; degree p needs T/N^(p-1)",
                   z(reparam_gap(1, 1)) and z(reparam_gap(q, 1, deg=q + 1)), "gap vanishes at a = b = 1, and at a = p - 1 for degree p"))
    controls.append(("V2 T/N^2 + N W is not", not z(reparam_gap(2, 1))))

    # V3
    Nstar = sp.solve(sp.diff(T / n + n * W, n), n)
    val = sp.simplify(sp.powsimp((T / n + n * W).subs(n, Nstar[0]), force=True))
    Np = (q * T / W) ** (1 / (q + 1))                             # the degree-p lapse, p = q + 1
    deg_p = z(sp.diff(T / n ** q + n * W, n).subs(n, Np))
    checks.append(("V3 N^2 = T/W, eliminated value 2 sqrt(T W), symmetric; degree p: N^p = (p-1) T/W",
                   len(Nstar) == 1 and z(Nstar[0] ** 2 - T / W) and z(val - 2 * sp.sqrt(T * W)) and deg_p
                   and z(val - val.subs({T: W, W: T}, simultaneous=True)), "N = %s, value = %s" % (Nstar[0], val)))
    Nab = sp.solve(sp.diff(T / n ** 2 + n * W, n), n)[0]
    vab = sp.simplify(sp.powsimp((T / n ** 2 + n * W).subs(n, Nab), force=True))
    controls.append(("V3 unequal powers eliminate to an asymmetric mean",
                     not z(vab - vab.subs({T: W, W: T}, simultaneous=True))))

    # V4
    Nw = sp.simplify(sp.powsimp(lapse(rayleigh_T, c * s ** w), force=True))
    act = sp.simplify(sp.powsimp(2 * sp.sqrt(rayleigh_T * c * s ** w), force=True))
    general = z(Nw - s ** ((2 - w) / 2) / (2 * sp.sqrt(c))) and z(act - sp.sqrt(c) * s ** ((2 + w) / 2))
    rows, want = [], {2: (1, s ** 2 / 2), 1: (sp.sqrt(s), s ** sp.Rational(3, 2) / 2), 0: (s, s / 2)}
    for lev, (wantN, wantA) in want.items():
        NN = sp.simplify(Nw.subs({w: lev, c: sp.Rational(1, 4)}))
        AA = sp.simplify(act.subs({w: lev, c: sp.Rational(1, 4)}))
        rows.append(z(NN - wantN) and z(AA - wantA))
    checks.append(("V4 the level table: N = 1, S^(1/2), S at w = 2, 1, 0", general and all(rows),
                   "N = %s, action = %s" % (Nw, act)))
    controls.append(("V4 with the budget-metric kinetic term the amplitude level misses",
                     not z(sp.simplify(lapse(sp.Rational(1, 4), s / 4)) - sp.sqrt(s))))

    # V5: L = Psi'^2/N + N c S^w + lam (Psi^2 + S^2 - 1), varied in N, S, Psi, lam
    Pv, dPv, Sv, Nv, lam = sp.symbols("Pv dPv Sv Nv lam")
    L = dPv ** 2 / Nv + Nv * c * Sv ** w + lam * (Pv ** 2 + Sv ** 2 - 1)
    on = {Pv: psi, dPv: -s / 2, Sv: s}
    Ns = s ** ((2 - w) / 2) / (2 * sp.sqrt(c))
    lam_s = sp.solve(sp.diff(L, Sv).subs(on).subs(Nv, Ns), lam)[0]
    E_N = sp.diff(L, Nv).subs(on).subs({Nv: Ns, lam: lam_s})
    mom = sp.diff(L, dPv).subs(on).subs(Nv, Ns)
    E_P = ddt(mom) - sp.diff(L, Pv).subs(on).subs({Nv: Ns, lam: lam_s})
    checks.append(("V5 the standing wave solves the constrained variation at every w",
                   z(E_N) and z(sp.simplify(E_P / psi)), "multiplier = %s" % sp.simplify(lam_s)))
    E_P0 = ddt(mom) - sp.diff(L, Pv).subs(on).subs({Nv: Ns, lam: 0})
    controls.append(("V5 without the constraint force the amplitude level fails",
                     not z(sp.simplify((E_P0 / psi).subs(w, 1)))))

    # V6
    Tb = sp.simplify(budget_T.subs(psi, sp.sqrt(1 - s ** 2)))
    Wneed = sp.simplify(Tb / s)
    checks.append(("V6 budget metric needs W = 1/(4S) for N = S^(1/2)", z(Tb - sp.Rational(1, 4)) and z(Wneed - 1 / (4 * s)),
                   "T' = %s, W = %s" % (Tb, Wneed)))
    controls.append(("V6 no native level gives the half power with the budget metric",
                     all(not z(sp.simplify(lapse(Tb, s ** lv / 4)) - sp.sqrt(s)) for lv in (0, 1, 2))))

    # V7
    N1 = sp.simplify(Nw.subs({w: 1, c: sp.Rational(1, 4)}))
    A1 = sp.simplify(act.subs({w: 1, c: sp.Rational(1, 4)}))
    welded = z(act - 2 * Nw * c * s ** w)
    tick = z(A1 - s ** sp.Rational(3, 2) / 2)
    rate_same = z(s * sp.diff(sp.log(A1), s) - sp.Rational(3, 2))   # the rate law's S^(3/2) is the same power
    dressed = sp.solve(sp.Poly(sp.expand(sp.together((1 / N1 ** 2 - 4 * al / s - 4 * be * s ** 2 / (1 - s ** 2))
                                                     * s * (1 - s ** 2))), s).coeffs(), [al, be], dict=True)
    checks.append(("V7 tick measure is 2 N W; rate candidate same weight; Lambda piece absent",
                   welded and tick and rate_same and dressed == [{al: sp.Rational(1, 4), be: 0}],
                   "action = 2 N W; action at amplitude = %s; dressed fit %s" % (A1, dressed)))
    with_lambda = sp.solve(sp.Poly(sp.expand(sp.together((1 / s + s ** 2 / (1 - s ** 2) - 4 * al / s
                                                          - 4 * be * s ** 2 / (1 - s ** 2)) * s * (1 - s ** 2))), s).coeffs(),
                           [al, be], dict=True)
    controls.append(("V7 a lapse carrying a Lambda piece fits with beta != 0", with_lambda == [{al: sp.Rational(1, 4), be: sp.Rational(1, 4)}]))

    # V8
    exp_ab = sp.simplify(s * sp.diff(sp.log(sp.solve(sp.diff(s ** 2 / n + n * s, n), n)[0]), s))
    off_W = sp.simplify(rayleigh_T / s ** (1 + 2 * eps))          # the potential that gives N = S^(1/2 + eps)
    ratio = sp.simplify(sp.powsimp(2 * sp.sqrt(rayleigh_T * off_W) / s ** (sp.Rational(1, 2) + eps), force=True))
    prod = z(act * Nw - 2 * rayleigh_T)                           # action times lapse is 2T, whatever the potential
    a_eps = sp.simplify(s * sp.diff(sp.log(sp.powsimp(2 * sp.sqrt(rayleigh_T * off_W), force=True)), s))
    meet = sp.solve(sp.Eq(a_eps, sp.Rational(3, 2) + eps), eps)   # the class's action against the family's tick
    checks.append(("V8 exponent 1/2 in the class; action x lapse = 2T; class and eps family meet only at eps = 0",
                   z(exp_ab - sp.Rational(1, 2)) and prod and z(a_eps - (sp.Rational(3, 2) - eps)) and meet == [0]
                   and z(sp.simplify(ratio - 2 * off_W)) and not z(ratio.subs(eps, sp.Rational(1, 10)) - s / 2),
                   "exponent %s; potential for S^(1/2+eps): %s; class action exponent %s; meet at eps = %s"
                   % (exp_ab, off_W, a_eps, meet)))
    exp_12 = sp.simplify(s * sp.diff(sp.log(sp.solve(sp.diff(s ** 2 / n + n ** 2 * s, n), n)[0]), s))
    controls.append(("V8 unequal lapse powers move the exponent", not z(exp_12 - sp.Rational(1, 2))))

    for name, ok, info in checks:
        print("%s  %s\n      %s" % ("PASS" if ok else "FAIL", name, info))
    for name, came_out in controls:
        print("control  %-66s %s" % (name, "as required" if came_out else "DID NOT"))
    ok = all(ck[1] for ck in checks) and all(ct[1] for ct in controls)
    print("%d/%d checks pass; %d/%d controls as required" % (
        sum(ck[1] for ck in checks), len(checks), sum(ct[1] for ct in controls), len(controls)))
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
