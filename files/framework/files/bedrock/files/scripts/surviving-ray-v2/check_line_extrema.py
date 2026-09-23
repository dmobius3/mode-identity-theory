"""F2's claim: on their fixed lines, the pyramid and the C3 ray are maxima of r6, the prism and the D2 ray minima.
So at each sign of g, two census orbits are energy maxima on their own lines, which a minimise-on-each-fixed-set
procedure (Kawaguchi-Ueda's) cannot return. Exact, from the definition of r6, with planted failures."""
import sympy as sp
from sympy.physics.quantum.cg import CG
MS = [3, 2, 1, 0, -1, -2, -3]; IDX = {m: i for i, m in enumerate(MS)}
fails = []
def gate(name, ok):
    print(('PASS ' if ok else 'FAIL ') + name)
    if not ok:
        fails.append(name)
cg6 = {(a, Q - a, Q): CG(3, a, 3, Q - a, 6, Q).doit() for Q in range(-6, 7) for a in MS if Q - a in MS}
def r6(coef):
    """coef: dict m -> complex sympy number; returns ||rho6||^2 / ||u||^4 exactly."""
    u = [coef.get(m, 0) for m in MS]
    th = [(-1) ** (3 - m) * sp.conjugate(u[IDX[-m]]) for m in MS]
    comps = [sp.expand(sum(cg6[(a, Q - a, Q)] * u[IDX[a]] * th[IDX[Q - a]] for a in MS if Q - a in MS)) for Q in range(-6, 7)]
    tot = sum(sp.expand(c * sp.conjugate(c)) for c in comps)
    return sp.simplify(tot / sp.expand(sum(x * sp.conjugate(x) for x in u)) ** 2)
s = sp.symbols('s')
A, B = sp.symbols('A B', positive=True)
def on_line(expr):
    # expr is a function of A^2 and B^2 on the unit circle A^2 + B^2 = 1; write it in s = A^2
    e = sp.simplify(expr.subs(B, sp.sqrt(1 - A ** 2)))
    return sp.expand(sp.simplify(e.subs(A, sp.sqrt(s))))
# the C5 line {v3, v-2} and the C3 line {v2, v-1}, real amplitudes: rotation about z absorbs the relative phase
c5 = on_line(924 * r6({3: A, -2: B}))
c3 = on_line(924 * r6({2: B, -1: A}))
print('924 r6 on C5 line:', c5, ' | on C3 line:', c3)
gate('C5 line: downward parabola, interior critical point s = 12/25 is the line maximum (the pyramid, 1188/5)',
     sp.degree(c5, s) == 2 and sp.Poly(c5, s).LC() < 0 and sp.solve(sp.diff(c5, s), s) == [sp.Rational(12, 25)] and c5.subs(s, sp.Rational(12, 25)) == sp.Rational(1188, 5))
gate('C3 line: downward parabola, interior critical point s = 4/5 is the line maximum (the C3 ray v2 + 2 v-1, 1188/5)',
     sp.degree(c3, s) == 2 and sp.Poly(c3, s).LC() < 0 and sp.solve(sp.diff(c3, s), s) == [sp.Rational(4, 5)] and c3.subs(s, sp.Rational(4, 5)) == sp.Rational(1188, 5))
gate('the minima on those two lines are endpoints: coherent (1) on C5 and v2 (36) on C3',
     min(c5.subs(s, 0), c5.subs(s, 1)) == 1 and min(c3.subs(s, 0), c3.subs(s, 1)) == 36)
gate('arm: an upward parabola would fail the maximum test', not (sp.Poly(-c5, s).LC() < 0))
# the D3 line {v3 + v-3, v0} and the D2 line {v2 + v-2, v0}: values at M8.12's listed critical points
d3 = {'hexagon z=0': {3: 1, -3: 1}, 'prism z=sqrt(23/10)': {3: 1, 0: sp.sqrt(sp.Rational(23, 10)), -3: 1},
      'octahedron z=i sqrt(10)/2': {3: 1, 0: sp.I * sp.sqrt(10) / 2, -3: 1}, 'zonal z=inf': {0: 1}}
d2 = {'octahedron z=0': {2: 1, -2: 1}, 'hexagon z=sqrt(30)/3': {2: 1, 0: sp.sqrt(30) / 3, -2: 1},
      'D2 ray z=i sqrt(30)/5': {2: 1, 0: sp.I * sp.sqrt(30) / 5, -2: 1}, 'zonal z=inf': {0: 1}}
v3 = {k: 924 * r6(v) for k, v in d3.items()}; v2 = {k: 924 * r6(v) for k, v in d2.items()}
print('D3 line critical values:', {k: str(sp.simplify(v)) for k, v in v3.items()}); print('D2 line critical values:', {k: str(sp.simplify(v)) for k, v in v2.items()})
gate('D3 line: the prism (8800/43) is the lowest critical value, the hexagon (463) the highest',
     min(v3, key=v3.get).startswith('prism') and max(v3, key=v3.get).startswith('hexagon') and sp.simplify(v3['prism z=sqrt(23/10)'] - sp.Rational(8800, 43)) == 0)
gate('D2 line: the D2 ray (225) is the lowest critical value, a rotated hexagon (463) the highest',
     min(v2, key=v2.get).startswith('D2 ray') and max(v2, key=v2.get).startswith('hexagon') and sp.simplify(v2['D2 ray z=i sqrt(30)/5'] - 225) == 0)
print('ALL PASS' if not fails else f'{len(fails)} FAILED')
