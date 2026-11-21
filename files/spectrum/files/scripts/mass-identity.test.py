"""Mass identity (2026-11-21): the representation theory behind mass-spectrum.md
sections II.3, II.4 and IV, recomputed from the 120 elements of 2I.

Every table this file checks is read from the page itself, so an edit to a
table that the group does not support fails here. It certifies:

  1. the group and its characters. 2I is built as the 120 unit quaternions of
     the 600-cell and checked to close under multiplication. The nine
     irreducible characters are R0, R1, R3, R6, R7, R8 = Sym^0 ... Sym^5 of the
     defining representation, R2 and R4 as the Galois conjugates of R1 and R3
     (chi(g^7), which sends sqrt5 to -sqrt5 on the character values), and
     R5 = R1 x R2; they are checked orthonormal. The McKay graph (tensoring
     with R1), the McKay distances, the first appearance of each irrep in
     Sym^k, and the Kostant exponents (the numerator of the covariant series
     over (1 - t^12)(1 - t^20)) are computed and compared with section II.3's
     master table;
  2. the three stabilizer decompositions of sections IV.1, IV.2 and IV.5.
     The reasons are standard character theory: (i) every element of 2I is
     conjugate to its inverse, so every character is real and a nontrivial
     character of Z3 occurs as often as its conjugate; (ii) the Z4 generator g
     has g^2 = -I, which acts as +1 on the integer-spin irreps and as -1 on the
     half-integer ones, so rho(g) has eigenvalues +-1 (real content) or +-i
     (complex pairs); (iii) the automorphism sqrt5 -> -sqrt5 of Q(sqrt5)
     extends to Q(zeta), zeta = exp(2 pi i/5), by zeta -> zeta^2, which carries
     the pairs (zeta, zeta^4) to (zeta^2, zeta^3) and back, so Galois-conjugate
     irreps have n1 and n2 exchanged;
  3. the j_first rule of section II.4: half the least McKay distance among the
     components of rho x ad(sigma), with ad(triv) = 3 R0, ad(std) = R3 and
     ad(gal) = R4. The rule is inferred from the table, which no earlier record
     derives; this check shows that it reproduces all 27 entries, that its
     trivial column is section II.3's dist/2, and that its R0 row is half the
     McKay distance of the vacuum's adjoint. The copies of the table in
     mass-null-test.py (_JF) and in the calculator (JFIRST) are checked against
     the page. The alternative rule without the adjoint, on rho x sigma itself,
     is checked to fail, so the adjoint is a real choice, adopted, not derived;
  4. the first stage of the isospin gate depends on the seat alone: j_first is
     an integer exactly where -I acts as +1 on rho, the 15 addresses of R0, R3,
     R4, R5 and R7. Under the rule this is forced, since ad(sigma) is
     integer-spin and a McKay distance has the parity of twice the spin;
  5. the gate's eleven featured evaluations in section IV.4: j_first, the
     (13, 17) status, the product rho x sigma and T3, recomputed from the rule
     and the two-stage gate.

Run: python3 mass-identity.test.py   (standard library only)
"""

import ast
import itertools
import math
import os
import re
from fractions import Fraction

HERE = os.path.dirname(os.path.abspath(__file__))
PAGE = open(os.path.join(HERE, '..', 'mass-spectrum.md'), encoding='utf-8').read()
NULL = open(os.path.join(HERE, '..', '..', '..', 'framework', 'files', 'working', 'files', 'scripts',
                         'mass-null-test.py'), encoding='utf-8').read()
CALC = open(os.path.join(HERE, '..', '..', '..', 'tools', 'files', 'calculator.html'), encoding='utf-8').read()


def check(label, condition, detail=""):
    if not condition:
        raise AssertionError(f"{label} FAILED  {detail}")
    print(f"  PASS  {label}" + (f"   {detail}" if detail else ""))


def section(start, end):
    i = PAGE.index(start)
    return PAGE[i:PAGE.index(end, i)]


IRR = [f'R{i}' for i in range(9)]
VAC = ['triv', 'std', 'gal']
SIGMA = {'triv': 'R0', 'std': 'R1', 'gal': 'R2'}
fmt = lambda f: str(f) if f.denominator == 1 else f'{f.numerator}/{f.denominator}'

# ================================================================ 1. the group
print("\nCHECK 1  2I, its nine characters, the McKay graph and the Kostant exponents")
PHI = (1 + 5 ** 0.5) / 2
key = lambda q: tuple(round(x, 9) + 0.0 for x in q)


def qmul(a, b):
    a0, a1, a2, a3 = a
    b0, b1, b2, b3 = b
    return (a0 * b0 - a1 * b1 - a2 * b2 - a3 * b3, a0 * b1 + a1 * b0 + a2 * b3 - a3 * b2,
            a0 * b2 - a1 * b3 + a2 * b0 + a3 * b1, a0 * b3 + a1 * b2 - a2 * b1 + a3 * b0)


G = {}
for i in range(4):
    for s in (1.0, -1.0):
        v = [0.0] * 4
        v[i] = s
        G[key(v)] = tuple(v)
for s in itertools.product((0.5, -0.5), repeat=4):
    G[key(s)] = s
EVEN = [p for p in itertools.permutations(range(4))
        if sum(p[i] > p[j] for i in range(4) for j in range(i + 1, 4)) % 2 == 0]
for p in EVEN:
    for s in itertools.product((1, -1), repeat=3):
        base = (0.0, s[0] * 0.5, s[1] * 0.5 / PHI, s[2] * PHI / 2)
        G[key(tuple(base[p[k]] for k in range(4)))] = tuple(base[p[k]] for k in range(4))
G = list(G.values())
keys = {key(g) for g in G}
check("120 unit quaternions closing under multiplication",
      len(G) == 120 and all(key(qmul(a, b)) in keys for a in G for b in G))
ANG = [math.acos(max(-1.0, min(1.0, g[0]))) for g in G]  # g has eigenvalues exp(+-i angle)


def sym(k, a):
    return sum(math.cos((k - 2 * m) * a) for m in range(k + 1))


CH = {'R0': lambda a: sym(0, a), 'R1': lambda a: sym(1, a), 'R2': lambda a: sym(1, 7 * a),
      'R3': lambda a: sym(2, a), 'R4': lambda a: sym(2, 7 * a), 'R5': lambda a: sym(1, a) * sym(1, 7 * a),
      'R6': lambda a: sym(3, a), 'R7': lambda a: sym(4, a), 'R8': lambda a: sym(5, a)}


def inner(f):
    x = sum(f(a) for a in ANG) / 120
    if abs(x - round(x)) > 1e-6:
        raise AssertionError(f"a multiplicity is not an integer: {x}")
    return round(x)


check("the nine characters are orthonormal",
      all(inner(lambda a, r=r, s=s: CH[r](a) * CH[s](a)) == (r == s) for r in IRR for s in IRR))
DIM = {r: round(CH[r](0.0)) for r in IRR}
SPIN = {r: 'Int' if round(CH[r](math.pi)) == DIM[r] else 'Half' for r in IRR}  # the sign -I carries
NONFIXED = {r for r in IRR if any(abs(CH[r](7 * a) - CH[r](a)) > 1e-6 for a in ANG)}
check("the Galois-nonfixed irreps are R1, R2, R3, R4", NONFIXED == {'R1', 'R2', 'R3', 'R4'})


def decompose(*reps):
    return [t for t in IRR for _ in range(inner(lambda a, t=t: CH[t](a) * math.prod(CH[r](a) for r in reps)))]


ADJ = {r: set(decompose(r, 'R1')) for r in IRR}
DIST = {'R0': 0}
frontier = ['R0']
while frontier:
    nxt = []
    for r in frontier:
        for t in ADJ[r]:
            if t not in DIST:
                DIST[t] = DIST[r] + 1
                nxt.append(t)
    frontier = nxt
first = {r: next(k for k in range(40) if inner(lambda a, r=r, k=k: CH[r](a) * sym(k, a)) > 0) for r in IRR}
check("each irrep first appears in Sym^k at k = its McKay distance", first == DIST)
KOSTANT = {}
for r in IRR:
    c = [inner(lambda a, r=r, k=k: CH[r](a) * sym(k, a)) for k in range(81)]
    num = [c[k] - (c[k - 12] if k >= 12 else 0) - (c[k - 20] if k >= 20 else 0) + (c[k - 32] if k >= 32 else 0)
           for k in range(81)]
    if any(x < 0 for x in num) or any(num[31:]) or sum(num) != 2 * DIM[r]:
        raise AssertionError(f"{r}: the covariant numerator is not a polynomial of 2 dim terms")
    KOSTANT[r] = sorted(k for k in range(31) for _ in range(num[k]))
master = {}
for m in re.finditer(r'^\| \$`R_(\d)`\$ \| (\d) \| (Int|Half) \| (\d) \| ([\d/]+) \| \{([^}]*)\} \|', PAGE, re.M):
    exps = []
    for tok in m.group(6).split(','):
        n = re.fullmatch(r'\s*(\d+)(²?)\s*', tok)
        exps += [int(n.group(1))] * (2 if n.group(2) else 1)
    master[f'R{m.group(1)}'] = (int(m.group(2)), m.group(3), int(m.group(4)), Fraction(m.group(5)), sorted(exps))
check("section II.3's master table: nine rows read", sorted(master) == IRR)
check("dimensions, spin classes and McKay distances match section II.3",
      all(master[r][:3] == (DIM[r], SPIN[r], DIST[r]) for r in IRR))
check("section II.3's j_first column is dist/2", all(master[r][3] == Fraction(DIST[r], 2) for r in IRR))
check("the Kostant exponents match section II.3", all(master[r][4] == KOSTANT[r] for r in IRR))
PAIR = {r for r in IRR if 13 in KOSTANT[r] and 17 in KOSTANT[r]}
check("the Coxeter pair (13, 17) lies in the exponents of R2, R6 and R8 alone", PAIR == {'R2', 'R6', 'R8'})

# =================================================== 2. the three restrictions
print("\nCHECK 2  the face, edge and vertex decompositions of sections IV.1, IV.2, IV.5")


def restrict(r, n):
    out = []
    for m in range(n):
        x = sum(CH[r](2 * math.pi * k / n) * complex(math.cos(2 * math.pi * m * k / n), -math.sin(2 * math.pi * m * k / n))
                for k in range(n)) / n
        if abs(x.imag) > 1e-6 or abs(x.real - round(x.real)) > 1e-6:
            raise AssertionError(f"{r} on Z{n}: not an integer multiplicity: {x}")
        out.append(round(x.real))
    return out


Z3, Z4, Z5 = ({r: restrict(r, n) for r in IRR} for n in (3, 4, 5))
NONTRIV = IRR[1:]
p3 = section('### 1. Color from Faces', '### 2. Domain from Edges')
p4 = section('### 2. Domain from Edges', '### 3. The Eta Sign Gate')
p5 = section('### 5. The Vertex and the Twist', '### 6. Summary')
page3 = {f'R{m[0]}': (int(m[1]), int(m[2]), int(m[3]))
         for m in re.findall(r'^\| \$`R_(\d)`\$ \| (\d) \| (\d) \| (\d) \|', p3, re.M)}
check("section IV.1: singlets and conjugate pairs on Z3",
      sorted(page3) == NONTRIV and all(Z3[r][1] == Z3[r][2] and page3[r] == (DIM[r], Z3[r][0], Z3[r][1])
                                       for r in NONTRIV))
page4 = {}
for word, members, what in re.findall(r'(Half-integer|Integer-spin) irreps \$`\\\{([^}]*)\\\}`\$: all \$`Z_4`\$ content '
                                      r'is (complex pairs|real)', p4):
    for n in re.findall(r'R_(\d)', members):
        page4[f'R{n}'] = 'real' if what == 'real' else 'complex'
kind4 = {r: 'real' if Z4[r][1] + Z4[r][3] == 0 else 'complex' if Z4[r][0] + Z4[r][2] == 0 else 'mixed' for r in IRR}
check("section IV.2: real content on Z4 exactly for the integer-spin irreps",
      sorted(page4) == IRR and all(page4[r] == kind4[r] == ('real' if SPIN[r] == 'Int' else 'complex') for r in IRR))
page5 = {f'R{m[0]}': (int(m[1]), int(m[2]), int(m[3]), int(m[4]))
         for m in re.findall(r'^\| \$`R_(\d)`\$ \| (\d) \| (\d) / (\d) / (\d) \|', p5, re.M)}
check("section IV.5: (n0, n1, n2) on Z5",
      sorted(page5) == NONTRIV and all(Z5[r][1] == Z5[r][4] and Z5[r][2] == Z5[r][3]
                                       and page5[r] == (DIM[r], Z5[r][0], Z5[r][1], Z5[r][2]) for r in NONTRIV))
check("Galois conjugates exchange n1 and n2 (R1 with R2, R3 with R4); the rest have n1 = n2",
      Z5['R1'][1:3] == Z5['R2'][2:0:-1] and Z5['R3'][1:3] == Z5['R4'][2:0:-1]
      and all(Z5[r][1] == Z5[r][2] for r in IRR if r not in NONFIXED))

# ========================================================= 3. the j_first rule
print("\nCHECK 3  section II.4's j_first table and the rule that reproduces it")
AD = {'triv': ['R0', 'R0', 'R0'], 'std': ['R3'], 'gal': ['R4']}
check("ad(std) = Sym^2 R1 = R3 and ad(gal) = Sym^2 R2 = R4",
      inner(lambda a: CH['R3'](a) * sym(2, a)) == 1 and inner(lambda a: CH['R4'](a) * sym(2, 7 * a)) == 1)


def rule(r, s):
    return Fraction(min(DIST[t] for a in AD[s] for t in decompose(r, a)), 2)


table = {}
p2 = section('### 4. Torsion Factors', 'Every irrep has an exact closed form.')
for m in re.findall(r'^\| \$`R_(\d)`\$ \| ([\d/]+) \| ([\d/]+) \| ([\d/]+) \|$', p2, re.M):
    for s, v in zip(VAC, m[1:]):
        table[(f'R{m[0]}', s)] = Fraction(v)
check("the table has 27 entries", len(table) == 27)
check("the rule reproduces all 27", all(rule(r, s) == table[(r, s)] for r in IRR for s in VAC))
check("its trivial column is section II.3's dist/2", all(table[(r, 'triv')] == Fraction(DIST[r], 2) for r in IRR))
check("its R0 row is half the McKay distance of the vacuum's adjoint",
      [table[('R0', s)] for s in VAC] == [Fraction(DIST[AD[s][0]], 2) for s in VAC],
      "0, 1, 3 (ad at distance 0, 2, 6)")
JF = ast.literal_eval(re.search(r'^_JF = (\{.*?\}\})', NULL, re.M | re.S).group(1))
check("mass-null-test.py's _JF matches the table at the 24 nontrivial seats",
      sum(Fraction(v).limit_denominator(2) == table[(r, s)] for r, row in JF.items() for s, v in row.items()) == 24)
calc = re.search(r'const JFIRST = \{(.*?)\n\};', CALC, re.S).group(1)
cj = {(f'R{m[0]}', s): Fraction(v).limit_denominator(2) for m in re.findall(r'(\d): \{([^}]*)\}', calc)
      for s, v in re.findall(r'(triv|std|gal):\s*([\d.]+)', m[1])}
check("the calculator's JFIRST matches the table at the 24 nontrivial seats",
      len(cj) == 24 and all(v == table[k] for k, v in cj.items()))
alt = {(r, s): Fraction(min(DIST[t] for t in decompose(r, SIGMA[s])), 2) for r in IRR for s in VAC}
miss = sorted(k for k in table if alt[k] != table[k])
check("rho x sigma without the adjoint does not reproduce the table", miss and ('R1', 'std') in miss,
      f"{len(miss)} of 27 differ, (R1, std) among them: {fmt(alt[('R1', 'std')])} against 1/2")

# ================================================ 4. the first stage, seat alone
print("\nCHECK 4  j_first is an integer exactly where -I acts as +1 on the seat")
integral = sorted(k for k, v in table.items() if v.denominator == 1)
check("the integer entries are the integer-spin seats in every vacuum",
      integral == sorted((r, s) for r in IRR for s in VAC if SPIN[r] == 'Int'),
      f"{len(integral)} of 27: " + ', '.join(r for r in IRR if SPIN[r] == 'Int'))

# ================================================== 5. the featured evaluations
print("\nCHECK 5  section IV.4's eleven featured evaluations, recomputed")
feat = section('**Gate evaluation at eleven featured addresses**', '**Hypercharge and electric charge')
rows = re.findall(r'^\| (\d+) \| \$`R_(\d)`\$ \| (triv|std|gal) \| ([\d/]+) \| ([^|]+) \| \$`([^`]*)`\$ \|[^|]*\|[^|]*\| ([^|]*) \|$',
                  feat, re.M)
check("eleven rows read", len(rows) == 11)
for rank, n, s, jf, pair, prod, t3 in rows:
    r = f'R{n}'
    j = rule(r, s)
    status = 'N/A' if r not in PAIR else 'kept' if s == 'triv' else 'stripped'
    comps = decompose(r, SIGMA[s])
    T3 = Fraction(-1, 2) if j.denominator == 1 else (
        Fraction(-1, 2) if status == 'stripped' and any(c in NONFIXED for c in comps) else Fraction(1, 2))
    page_t3 = Fraction(re.search(r'([+-]1/2)', t3).group(1))
    check(f"rank {rank} ({r}, {s})",
          Fraction(jf) == j and pair.strip() == status and sorted(re.findall(r'R_(\d)', prod)) == sorted(c[1:] for c in comps)
          and page_t3 == T3, f"j_first {fmt(j)}, {status}, T3 {fmt(T3)}")

print("\nALL CHECKS PASSED\n")
