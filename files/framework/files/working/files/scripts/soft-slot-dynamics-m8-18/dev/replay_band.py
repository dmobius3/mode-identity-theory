"""Read-only. The frozen rule on stored summaries at N = 24 and 32 alone: the band the rule's text gives for that ladder
(lowest cutoff 24) against M8.17's band (the level above 16). Controls and the twelve points. No solve."""
import glob, json, os, sys
BENCH, OUT8161 = sys.argv[1:3]; sys.path.insert(0, BENCH); sys.path.insert(0, os.path.join(BENCH, 'run'))
from instrument import convergence as cv
import checks as ck
def two(p24, p32, n_lo):
    return ck.reading([p24['summary'], p32['summary']], p32['eig'], p32['lam'], p32['record']['margin'], n_lo)
print('CONTROLS (type on the record | band above 24 | band above 16)')
for name in ('C2a', 'C2a_R5', 'C2b', 'C3', 'C3R_R4', 'P5'):
    r = json.load(open(os.path.join(OUT8161, f'{name}.json'), encoding='utf-8'))
    for k, p24 in r['cutoffs']['24']['points'].items():
        p32 = r['cutoffs']['32']['points'][k]
        a, b = two(p24, p32, 24), two(p24, p32, 16)
        print(f"  {name} {float(k):g}: {p32['record']['type']} | {a['verdict']} | {b['verdict']}")
        for tag, x in (('above 24', a), ('above 16', b)):
            for why in x['reasons']:
                print(f"      {tag}: {why}")
print('THE TWELVE')
PTS = {'T1_R4': (1.41421356237, 32, 45.254834, 64, 72), 'T1_R5': (32,), 'T4_R4': (4, 8, 11.313708499, 64, 72), 'T5_R2': (45.254834,)}
na = nb = 0
for name, eps in PTS.items():
    r = json.load(open(os.path.join(BENCH, 'run', 'out', f'{name}.json'), encoding='utf-8'))
    for e in eps:
        k = [x for x in r['readings'] if abs(float(x) - e) < 1e-6][0]
        p24, p32 = r['cutoffs']['24']['points'][k], r['cutoffs']['32']['points'][k]
        a, b = two(p24, p32, 24), two(p24, p32, 16)
        na += a['verdict'] == 'converged'; nb += b['verdict'] == 'converged'
        print(f"  {name} {e:g}: above 24: {a['verdict']}, {a['type']} | above 16: {b['verdict']}, {b['type']}")
        for tag, x in (('above 24', a), ('above 16', b)):
            for why in x['reasons']:
                print(f"      {tag}: {why}")
print(f'converged: {na} of 12 with the band above 24; {nb} of 12 with the band above 16')
# the failing control in detail
r = json.load(open(os.path.join(OUT8161, 'C2a_R5.json'), encoding='utf-8'))
k = [x for x in r['cutoffs']['24']['points'] if abs(float(x) - 2) < 1e-9][0]
print('\nC2a/R5 at 2, imaginary groups near 7.98i')
for N in ('16', '24', '32'):
    s = r['cutoffs'][N]['points'][k]['summary']
    gs = [(round(cv._c(g).imag, 6), g['size'], g.get('neg'), g['cls']) for g in s['groups'] if 7.6 < abs(cv._c(g)) < 8.4]
    print(f'  N = {N}:', gs)
