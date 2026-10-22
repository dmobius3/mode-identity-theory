"""Cross-checks of the two units' T5 second members (bench, 2026-10-20). Exact arithmetic.
  python3 -I -B cross_check.py SOFT_SLOT_BRANCHES_SCRIPTS
1. UA's certificate (Majorana root multiplicities) on u, UA's u* = (u + Theta u)/sqrt2 and UB's u2 = (u - i Theta u)/sqrt2.
2. UB's certificate (the slow polynomial read with i, via branches_check.analyse) on UA's u*."""
import sys
import sympy as sp
sys.argv, SCRIPTS = sys.argv[:1], sys.argv[1]
sys.path.insert(0, SCRIPTS)
import branches_check as bc  # noqa: E402

z = sp.symbols('z')
h = sp.Rational(7, 2)
ms = [h - a for a in range(8)]                      # 7/2, 5/2, ..., -7/2
r3, r7 = sp.sqrt(sp.Rational(3, 10)), sp.sqrt(sp.Rational(7, 10))
u = {h: r3, sp.Rational(-3, 2): r7}
theta = lambda v: {-m: (-1) ** int(h - m) * sp.conjugate(c) for m, c in v.items()}   # Theta v_m = (-1)^(7/2-m) v_-m, antilinear
add = lambda a, b, cb=1: {m: sp.nsimplify(a.get(m, 0) + cb * b.get(m, 0)) for m in ms if a.get(m, 0) + cb * b.get(m, 0) != 0}
ustar = add(u, theta(u))                              # UA: u + Theta u (times sqrt2)
u2 = add(u, theta(u), -sp.I)                          # UB: u - i Theta u (times sqrt2)
assert sp.simplify(u2[sp.Rational(3, 2)] - sp.I * sp.sqrt(sp.Rational(7, 10))) == 0, "u2's m = 3/2 component"


def majorana(v):
    return sp.expand(sum((-1) ** int(h - m) * sp.sqrt(sp.binomial(7, h + m)) * c * z ** int(h + m) for m, c in v.items()))


for name, v in (('u (registered)', u), ("UA's u*", ustar), ("UB's u2", u2)):
    P = sp.Poly(majorana(v), z)
    g = sp.gcd(P, P.diff(z))
    lead = P.LC()
    print(f'1. {name}: components {dict((str(m), c) for m, c in v.items())}')
    print(f'   P/lc = {sp.expand(P.as_expr() / lead)}; degree {P.degree()}; gcd(P, P\') degree {g.degree()}; '
          f'discriminant of P/lc = {sp.nsimplify(sp.discriminant(sp.expand(P.as_expr() / lead), z))}')

J, T = bc.J0(7), bc.theta(7)
U = sp.Matrix(bc.vec(7, {0: 1, 5: 7}))
reads = {"UA's u* = u + Theta u": U + T * U, "UB's u2 = u - i Theta u": U - J * (T * U), 'u, registered': U}
polys = {}
for name, v in reads.items():
    a = bc.analyse(7, bc.Q2, list(v), True, structure=J)
    polys[name] = sp.Poly(a['Pu'].as_expr(), bc.NU)
    print(f"2. {name}, read with i: Q {a['Q']}, sig {a['sig']}, k {a['k']}, r {a['r']}, zero mult {a['mS']}, {a['typ']}; "
          f"slow polynomial {sp.factor(polys[name].as_expr())}")
names = list(reads)
print(f"   UA's u* and UB's u2 have the same slow polynomial: {polys[names[0]] == polys[names[1]]}; "
      f"UA's u* against the registered: resultant nonzero {polys[names[0]].resultant(polys[names[2]]) != 0}")
