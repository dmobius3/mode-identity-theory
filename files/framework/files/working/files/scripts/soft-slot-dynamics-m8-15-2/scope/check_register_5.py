"""REGISTER_5's A1 table and quoted numbers against plant_oracle.out and recon_numbers.out.
Usage: check_register_5.py REGISTER ORACLE_OUT RECON_OUT. Exit 1 on any mismatch."""
import re, sys
reg, orc, rec = (open(f).read() for f in sys.argv[1:4])
R = reg.replace('−', '-')
bad = []
# 1. the A1 table: each row's level-3 and level-2 statuses must match the oracle's summary for that case
summ = {(s_, k, lv): v for s_, k, lv, v in re.findall(r'^   A1, slope sign ([+-]1), kappa/delta ([\d.]+), level (\d): (.*)$', orc, flags=re.M)}
def statuses(line):
    """The oracle summary's step statuses, without the classes: one per '; '-separated step."""
    return [re.match(r'(genuine|structural|Unresolved \([^)]*\))', part).group(1) for part in line.split('; ')]
rows = re.findall(r'^\| ([+-]1), ([\d.]+) \| (.*?) \| (.*?) \| (.*?) \|$', R, flags=re.M)
assert len(rows) == 14, len(rows)
def short(cell):
    """The statuses a table cell names, in order: genuine or Unresolved (reason)."""
    return re.findall(r'genuine(?! and)|Unresolved \([^)]*\)', cell)
for sg, k, c3, c2, result in rows:
    for lv, cell in (('3', c3), ('2', c2)):
        o = summ.get((sg, k, lv))
        if o is None:
            bad.append(f'A1 {sg}, {k}, level {lv}: not in the oracle'); continue
        want = [x for x in statuses(o) if x != 'structural']
        if sorted(short(cell)) != sorted(want):
            bad.append(f'A1 {sg}, {k}, level {lv}: table {short(cell)} against oracle {want}')
        if ('branch step' in cell) != ('branch step' in o):
            bad.append(f'A1 {sg}, {k}, level {lv}: branch flag differs')
    gen3, gen2 = 'genuine' in short(c3), 'genuine' in short(c2)
    if (gen3 and gen2) != result.startswith('located'):
        bad.append(f'A1 {sg}, {k}: result "{result}" against levels genuine {gen3}, {gen2}')
# 2. numbers quoted from the outputs
def trim(x):
    return x.rstrip('0').rstrip('.') if '.' in x else x
tol = re.search(r"controls' largest statistic is ([\d.]+)e-04 \((\w+), level (\d), at ([\d.]+)\); ten times it is ([\d.]+)e-03", rec)
need = [f'`τ_c = {tol.group(5)}×10⁻³`', f'`{tol.group(1)}×10⁻⁴` ({tol.group(2)}, level {tol.group(3)}, at {tol.group(4)}']
a20 = re.search(r'== A20.*?registered\): Unresolved \(solution continuity\); worst ([\d.e+-]+) at ([\d.]+)', orc, flags=re.S)
need.append(f'at {a20.group(2)} the statistic reads {float(a20.group(1)):.3f}')
a21 = re.search(r'== A21.*?over the tolerance: ([\d.]+) ([\d.e+-]+); ([\d.]+) ([\d.e+-]+); [\d.]+ ([\d.e+-]+)', orc, flags=re.S)
need.append(f'at {trim(a21.group(1))} ({float(a21.group(2)):.4f}) and {trim(a21.group(3))} ({float(a21.group(4)):.3f}), and across the step ({float(a21.group(5)):.4f})')
a27 = re.findall(r'== A27, kappa/delta 8, level (\d).*?Unresolved \(index bookkeeping\): n\(L\) ends ([\d.]+) to ([\d.]+)', orc, flags=re.S)
for lv, x, y in a27:
    need.append(f'on {trim(x)} to {trim(y)}')
a16 = re.search(r'== A16, S1 at level 3.*?clean ends ([\d.]+) to ([\d.]+)', orc, flags=re.S)
need.append(f'clean ends {float(a16.group(1)):g} and {a16.group(2)}')
a26 = re.search(r'== A26, guard region.*?over the tolerance: ([\d.]+) degenerate', orc, flags=re.S)
need.append(f'the first compared point, {trim(a26.group(1))}')
roots = []
for b in re.split(r'^== ', orc, flags=re.M):
    m = re.match(r'A1, slope sign [+-]1, kappa/delta [\d.]+, level (\d)', b)
    if m:
        r = 1.0130 if m.group(1) == '3' else 1.0181
        roots += [abs(float(x) - r) / r for x in re.findall(r'root ([\d.]+)', b)]
need.append(f'the oracle\'s largest offset is `{max(roots):.1e}`'.replace('e-04', '×10⁻⁴'))
full = re.search(r"full ladders, ([\d.]+) to ([\d.]+), the statistic reaches ([\d.]+)e-04 \((\w+), level (\d), at ([\d.]+)\)", rec)
need.append(f'full ladders, {full.group(1)} to {full.group(2)}, the statistic reaches `{full.group(3)}×10⁻⁴` ({full.group(4)}, level {full.group(5)}, at {full.group(6)}')
for n in need:
    if n.replace('−', '-') not in R:
        bad.append(f'MISSING: {n}')
print(f'A1 rows: {len(rows)}; quoted numbers: {len(need)}; mismatches: {len(bad)}')
for b in bad:
    print('  ', b)
sys.exit(1 if bad else 0)
