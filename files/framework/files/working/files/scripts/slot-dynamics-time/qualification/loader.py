"""The stored-record loader (the terms, § THE READ, step 1): M8.16.1's stored records, each pinned by the SHA-256 its
RECORD.md lists, and its FROZEN.json, pinned by its FROZEN_PIN; and Theorem 4.2's leading order at a point, from the
frozen values. A stored point carries its case, cutoff and amplitude, and a read refuses one that does not match its
own, before any value is compared. Development code: nothing here is registered until the freeze."""
import hashlib
import json
import math
import os
import re
from fractions import Fraction

HERE = os.path.dirname(os.path.abspath(__file__))
M8161 = os.path.realpath(os.path.join(HERE, '..', '..', 'soft-slot-dynamics-m8-16-1'))
SLOW_RADIUS = 1.0
CASES = {'C2a': 'C2a', 'C2a_R5': 'C2a/R5', 'C2b': 'C2b', 'C3': 'C3', 'P5': 'P5', 'C3R_R4': 'C3R/R4', 'T3_R4': 'T3/R4'}


class Refused(Exception):
    """The loader refused a record: its pin, case, cutoff or amplitude is not the read's."""


def _sha(path):
    with open(path, 'rb') as f:
        return hashlib.sha256(f.read()).hexdigest()


def pins():
    """The SHA-256 of every run/out file, as M8.16.1's RECORD.md lists them, and of run/FROZEN.json."""
    with open(os.path.join(M8161, 'RECORD.md'), encoding='utf-8') as f:
        rows = re.findall(r'^\s*\| `(run/[^`]+)` \| `([0-9a-f]{64})` \|', f.read(), re.M)
    table = dict(rows)
    with open(os.path.join(M8161, 'run', 'FROZEN_PIN'), encoding='utf-8') as f:
        assert table['run/FROZEN.json'] == f.read().strip(), 'RECORD.md and FROZEN_PIN disagree'
    return table


PINS = pins()


def frozen():
    path = os.path.join(M8161, 'run', 'FROZEN.json')
    if _sha(path) != PINS['run/FROZEN.json']:
        raise Refused('FROZEN.json differs from its pin')
    with open(path, encoding='utf-8') as f:
        return json.load(f)


FROZEN = frozen()


class StoredPoint:
    def __init__(self, stem, N, eps, pt, sha):
        self.stem, self.case, self.N, self.eps, self.sha = stem, CASES[stem], int(N), float(eps), sha
        self.eps_reached, self.lam, self.m = pt['eps_reached'], pt['lam'], pt['m']
        self.groups = [dict(c=complex(*g['c']), cls=g['cls'], size=g['size'], neg=g['neg'], status=g['status'])
                       for g in pt['groups'] if abs(complex(*g['c'])) < SLOW_RADIUS]
        self.type = pt['record']['type']


def load(stem, N, eps):
    """The stored point of member `stem` at cutoff N and nominal amplitude eps, from its pinned record."""
    rel = f'run/out/{stem}.json'
    path = os.path.join(M8161, rel)
    sha = _sha(path)
    if PINS.get(rel) != sha:
        raise Refused(f'{rel} differs from its pin')
    with open(path, encoding='utf-8') as f:
        j = json.load(f)
    cut = j['cutoffs'].get(str(N))
    if cut is None:
        raise Refused(f'{stem} has no record at N = {N}')
    keys = [k for k in cut['points'] if abs(float(k) - eps) < 1e-9]
    if len(keys) != 1:
        raise Refused(f'{stem} has no single stored point at eps = {eps}, N = {N}')
    return StoredPoint(stem, N, eps, cut['points'][keys[0]], sha)


def check(point, stem, N, eps):
    """A read at (stem, N, eps) refuses a stored point of another case, cutoff, amplitude or pin, before any value is compared."""
    if point.stem != stem or point.N != int(N) or abs(point.eps - eps) > 1e-12:
        raise Refused(f'the stored point is {point.stem} at N = {point.N}, eps = {point.eps}; the read is {stem} at N = {N}, eps = {eps}')
    if PINS.get(f'run/out/{stem}.json') != point.sha:
        raise Refused('the stored point is not from the pinned record')


def _num(x):
    return float(Fraction(x['frac'])) if x.get('frac') else x['value']


def leading(stem, eps):
    """Theorem 4.2's leading order L_g = eps kappa s tau_g at amplitude eps, kappa = 1/(8 sqrt(lam0) Q(u)), as M8.16.1
    froze it: one entry per frozen spectrum group, with its class, sign and multiplicity, in the representative quadrant."""
    f = FROZEN['cases'][CASES[stem]]
    ks = _num(f['s']) / (8 * math.sqrt(f['lam0']) * _num(f['Q']))
    out = []
    for x in f['spectrum']:
        t = x['tau']
        if x['cls'] == 'complex':
            z = complex(t['re'], t['im'])
        elif x['cls'] == 'imag':
            z = complex(0, _num(t))
        else:
            z = complex(_num(t), 0)
        out.append(dict(L=eps * ks * z, cls=x['cls'], sign=x['sign'], size=x['mult']))
    return out


def pair_leading(point):
    """Each stored slow group with its leading-order value, matched within class and Krein sign by ascending modulus."""
    lead = leading(point.stem, point.eps_reached)
    out = []
    for cls in ('imag', 'real', 'complex'):
        for sign in (1, -1, None):
            st = [g for g in point.groups if g['cls'] == cls and (cls != 'imag' or (g['neg'] == g['size']) == (sign == -1))]
            ld = [x for x in lead if x['cls'] == cls and (cls != 'imag' or x['sign'] == sign)]
            if cls == 'imag' and sign is None or cls != 'imag' and sign is not None:
                continue
            if len(st) != len(ld) or sorted(g['size'] for g in st) != sorted(x['size'] for x in ld):
                raise Refused(f'{point.stem}: the stored {cls} groups do not match the frozen spectrum')
            for g, x in zip(sorted(st, key=lambda g: abs(g['c'])), sorted(ld, key=lambda x: abs(x['L']))):
                out.append(dict(g, L=x['L']))
    if len(out) != len(point.groups):
        raise Refused(f'{point.stem}: {len(out)} of {len(point.groups)} stored groups matched to the frozen spectrum')
    return out
