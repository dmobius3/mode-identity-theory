#!/usr/bin/env python3
"""T5's second member against the registered one, in exact arithmetic (UB, 2026-10-20).

Usage: python3 -I -B t5_member_check.py SOFT_SLOT_BRANCHES_SCRIPTS
  SOFT_SLOT_BRANCHES_SCRIPTS: MIT's files/framework/files/working/files/scripts/soft-slot-branches/ at 54f3d7c;
  branches_check.py's exact quartic, metric, complex structure J0 and quaternionic structure theta are imported
  from it, unchanged.

T5's registered member is u = sqrt(3/10) v_{7/2} + sqrt(7/10) v_{-3/2} in R2, read with complex structure i. The
second member is u2 = u p0 with p0 = (1 + k)/sqrt2, so p0 i p0^{-1} = j: in orthonormal components
u2 = sqrt(3/20) v_{7/2} + i sqrt(7/20) v_{3/2} + sqrt(7/20) v_{-3/2} - i sqrt(3/20) v_{-7/2}, i.e. (u - i Theta u)/sqrt2.
In branches_check.py's weighted coordinates both are rational, so every polynomial below is exact.

Claims:
  A  u and u2 are critical on the same orbit: Q = 22/13, signature (9, 0, 0), k = 6, r_u = 4, zero multiplicity 10,
     elliptic, at both, read with i.
  B  u2 read with i has the slow polynomial of u read with Theta (the page's Families in R2: S_{up} ~ R_{pip^-1} M_u),
     and so does (u + i Theta u)/sqrt2, the other sign convention for k.
  C  that polynomial differs from the registered member's, which is the terms' frozen T5 spectrum, and the two share
     no root: their resultant is nonzero.
Arm: u in place of u2, which must make claim C fail (the same member twice).
Exit status 1 if a claim fails or the arm stays green."""
import sys

import sympy as sp

sys.argv, SCRIPTS = sys.argv[:1], sys.argv[1]
sys.path.insert(0, SCRIPTS)
import branches_check as bc  # noqa: E402

J, T = bc.J0(7), bc.theta(7)
U = sp.Matrix(bc.vec(7, {0: 1, 5: 7}))           # weighted coordinates: index 0 is m = 7/2, index 5 is m = -3/2
FROZEN_T5 = (20449 * bc.NU + 153664) * (418161601 * bc.NU**2 + 6989958976 * bc.NU + 28677390336)


def read(v, S):
    return bc.analyse(7, bc.Q2, list(v), True, structure=S)


def poly(a):
    return sp.Poly(a['Pu'].as_expr(), bc.NU)


def components(v):
    n, out = 8, {}
    for a in range(n):
        m = sp.Rational(7 - 2 * a, 2)
        c = v[a] + sp.I * v[n + a]
        if c != 0:
            out[str(m)] = sp.nsimplify(c * sp.sqrt(sp.factorial(sp.Rational(7, 2) + m) * sp.factorial(sp.Rational(7, 2) - m)))
    return out


def claims(u2):
    ok = True
    reg, sec = read(U, J), read(u2, J)
    a_ok = all(x['Q'] == sp.Rational(22, 13) and x['sig'] == (9, 0, 0) and x['k'] == 6 and x['r'] == 4 and x['mS'] == 10
               and x['typ'].startswith('elliptic') for x in (reg, sec))
    print('A  registered: Q %s, sig %s, k %s, r %s, zero mult %s, %s' % (reg['Q'], reg['sig'], reg['k'], reg['r'], reg['mS'], reg['typ']))
    print('   second:     Q %s, sig %s, k %s, r %s, zero mult %s, %s' % (sec['Q'], sec['sig'], sec['k'], sec['r'], sec['mS'], sec['typ']))
    print('   %s' % ('PASS' if a_ok else 'FAIL'))
    ok &= a_ok
    p_reg, p_sec = poly(reg), poly(sec)
    p_theta = poly(read(U, T))
    p_other = poly(read(U + J * (T * U), J))
    b_ok = p_sec == p_theta and p_other == p_theta
    print('B  second read with i:      %s' % sp.factor(p_sec.as_expr()))
    print('   u read with Theta:       %s' % sp.factor(p_theta.as_expr()))
    print('   (u + i Theta u) with i:  equal: %s' % (p_other == p_theta))
    print('   %s' % ('PASS' if b_ok else 'FAIL'))
    ok &= b_ok
    res = p_reg.resultant(p_sec)
    frozen_ok = sp.expand(p_reg.as_expr() * sp.Poly(FROZEN_T5, bc.NU).LC() - FROZEN_T5 * p_reg.LC()) == 0
    c_ok = frozen_ok and p_reg != p_sec and res != 0
    tau = lambda P: sorted(float(sp.sqrt(-r)) for r in sp.Poly(P, bc.NU).nroots())
    print('C  registered (the terms\' frozen T5 spectrum: %s): %s' % (frozen_ok, sp.factor(p_reg.as_expr())))
    print('   tau, registered: %s; second: %s' % (['%.10f' % t for t in tau(p_reg.as_expr())], ['%.10f' % t for t in tau(p_sec.as_expr())]))
    print('   resultant nonzero (no common root): %s' % (res != 0))
    print('   %s' % ('PASS' if c_ok else 'FAIL'))
    ok &= c_ok
    return ok, (a_ok, b_ok, c_ok)


def main():
    u2 = U - J * (T * U)
    print('T5\'s second member: u2 = u p0, p0 = (1 + k)/sqrt2, in orthonormal components (unnormalized): %s' % components(u2))
    ok, _ = claims(u2)
    print('arm: u in place of u2')
    _, (a2, b2, c2) = claims(U)
    arm_red = not c2
    print('   arm %s' % ('RED' if arm_red else 'GREEN'))
    print('%s; arm %s' % ('all claims pass' if ok else 'a claim FAILED', 'red' if arm_red else 'GREEN'))
    sys.exit(0 if ok and arm_red else 1)


if __name__ == '__main__':
    main()
