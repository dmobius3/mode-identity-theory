"""M8.15.x control 2a, § 5 of REGISTER_2.md (registered 2026-10-09T01:21:48Z): the synthetic classifier tests, on
constructed block data with the classifier's own functions (cluster_rule.py), in R^N with the Euclidean inner product.
Writes control_2a_synthetic.json and control_2a_synthetic.log."""
import os, sys, json, copy, datetime
import numpy as np
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, 'solver', 'm8_15_solver'))
from cluster_rule import anchor, track, advance, start_tracks, orth, pcos_min

N = 40
inner = lambda A, B: A.T @ B
rng = np.random.default_rng(20261009)


def frame(k):
    Q, _ = np.linalg.qr(rng.standard_normal((N, k)))
    return Q


def rot_in(W, k):
    """k orthonormal columns inside span(W), rotated arbitrarily."""
    Q, _ = np.linalg.qr(rng.standard_normal((W.shape[1], W.shape[1])))
    return W @ Q[:, :k]


def blk(cls, lam, basis):
    return dict(cls=cls, lam=complex(lam), basis=orth(basis, inner))


def near(W, angle):
    """A subspace at the given principal angle from span(W) in every direction."""
    E = frame(W.shape[1])
    E = E - W @ (W.T @ E)
    E = orth(E, inner)
    return orth(W * np.cos(angle) + E * np.sin(angle), inner)


def test1():
    W = frame(4)
    b = [blk('imag+', 1.02j, rot_in(W, 2)), blk('imag+', 0.99j, None if False else W @ np.linalg.qr(rng.standard_normal((4, 4)))[0][:, :2]),
         blk('imag-', 0.5j, frame(2)), blk('imag+', 1e-6j, frame(2))]
    b[1]['basis'] = orth(W - b[0]['basis'] @ (b[0]['basis'].T @ W), inner)[:, :2]      # the rest of W, so the two span it
    a = anchor(b, [dict(label='M', cls='imag+', mult=2)], {'M': 1.0j})
    tracks = []
    start_tracks(tracks, a, b, inner)
    W2 = near(W, np.radians(8))
    B2a = rot_in(W2, 2)
    B2b = orth(W2 - B2a @ (B2a.T @ W2), inner)[:, :2]
    b2 = [blk('imag+', 1.40j, B2a), blk('imag+', 1.44j, B2b), blk('imag-', 0.7j, frame(2))]
    r = track(tracks, b2, np.sqrt(2), inner)
    return dict(anchor_ok=a['M']['ok'], anchored=sorted(a['M'].get('blocks') or []), tracked_ok=r['M']['ok'],
                tracked=sorted(r['M']['blocks'] or []))


def test2():
    W = frame(4)
    B1 = rot_in(W, 2)
    B2 = orth(W - B1 @ (B1.T @ W), inner)[:, :2]
    b = [blk('imag+', 1.02j, B1), blk('imag+', 0.99j, B2), blk('imag+', 1.03j, frame(2))]
    a = anchor(b, [dict(label='M', cls='imag+', mult=2)], {'M': 1.0j})
    return dict(ok=a['M']['ok'], why=a['M'].get('why'), margin=a['M'].get('margin'))


def test3():
    out = {}
    for name, (c1, c2) in (('close', (1.02j, 1.06j)), ('apart', (1.01j, 1.08j))):
        b = [blk('imag-', c1, frame(2)), blk('imag-', c2, frame(2))]
        a = anchor(b, [dict(label='P', cls='imag-', mult=1)], {'P': 1.0j})
        out[name] = dict(ok=a['P']['ok'], blocks=a['P'].get('blocks'), margin=a['P'].get('margin'))
    return out


def test4():
    b = [blk('quartet', 0.5 + 1.15j, frame(4)), blk('imag+', 3j, frame(2))]
    a = anchor(b, [dict(label='Q', cls='quartet', mult=1)], {'Q': 0.5 + 1.0j})
    tracks = []
    start_tracks(tracks, a, b, inner)
    r = track(tracks, [blk('quartet', 0.7 + 1.4j, frame(4))], np.sqrt(2), inner)
    return dict(anchor_ok=a['Q']['ok'], nearest=a['Q']['nearest'], alive=tracks[0]['alive'],
                tracked_later='Q' in r)


def test5():
    A = frame(2)
    b = [blk('imag+', 1.0j, A)]
    a = anchor(b, [dict(label='T', cls='imag+', mult=1)], {'T': 1.0j})
    tracks = []
    start_tracks(tracks, a, b, inner)
    b2 = [blk('real', 0.9, near(A, np.radians(10))), blk('imag+', 1.3j, frame(2))]
    r = track(tracks, b2, 1.0, inner)
    advance(tracks, r, b2, inner)
    return dict(ok=r['T']['ok'], change=r['T']['change'], cls_now=tracks[0]['cls'])


def test6():
    E = frame(4)
    A = E[:, :2]
    Bv = orth(np.column_stack([E[:, 0] * np.cos(np.radians(20)) + E[:, 2] * np.sin(np.radians(20)),
                               E[:, 1] * np.cos(np.radians(20)) + E[:, 3] * np.sin(np.radians(20))]), inner)
    Cv = orth(np.column_stack([E[:, 0] * np.cos(np.radians(10)) + E[:, 2] * np.sin(np.radians(10)),
                               E[:, 1] * np.cos(np.radians(10)) + E[:, 3] * np.sin(np.radians(10))]), inner)
    tracks = [dict(label='A', cls='imag+', mult=1, basis=A, lam=1.0j, alive=True),
              dict(label='B', cls='imag+', mult=1, basis=Bv, lam=1.1j, alive=True)]
    r = track(tracks, [blk('imag+', 1.05j, Cv)], 1.0, inner)
    return dict(A=dict(ok=r['A']['ok'], why=r['A']['why']), B=dict(ok=r['B']['ok'], why=r['B']['why']))


def test7():
    A = frame(2)
    tracks = [dict(label='T', cls='imag+', mult=1, basis=A, lam=1.0j, alive=True)]
    r = track(tracks, [blk('imag+', 2.5j, A)], 1.0, inner)
    return dict(ok=r['T']['ok'], why=r['T']['why'], overlap_of_the_only_block=pcos_min(A, orth(A, inner), inner))


def evaluate(R):
    t1, t2, t3, t4, t5, t6, t7 = (R[f't{k}'] for k in range(1, 8))
    return [
        ('1. a doubled mode is matched uniquely as one multiplet, and tracked as one subspace',
         t1['anchor_ok'] and t1['anchored'] == [0, 1] and t1['tracked_ok'] and t1['tracked'] == [0, 1]),
        ('2. with an external block inside the window and the margin, Unresolved',
         (not t2['ok']) and t2['why'] is not None and t2['why'].startswith('not unique')),
        ('3. one predicted block, two candidates: Unresolved within 0.05, unique beyond it',
         (not t3['close']['ok']) and t3['apart']['ok'] and t3['apart']['blocks'] == [0]),
        ('4. a sole candidate outside 0.10: unanchored, and Unresolved later',
         (not t4['anchor_ok']) and t4['nearest'] > 0.10 and (not t4['alive']) and not t4['tracked_later']),
        ('5. a class change in band and overlap: tracked, the change recorded',
         t5['ok'] and t5['change'] and t5['cls_now'] == 'real'),
        ('6. two tracks qualifying for one block: Unresolved',
         (not t6['A']['ok']) and (not t6['B']['ok']) and t6['A']['why'] == t6['B']['why'] == 'two tracks take the same block'),
        ('7. overlap but modulus outside the band: not taken, Unresolved',
         (not t7['ok']) and t7['why'] == 'no candidate' and t7['overlap_of_the_only_block'] >= 0.9),
    ]


def mutations(R):
    arms = [
        (0, 'the multiplet split into two anchors', lambda r: r['t1'].__setitem__('anchored', [0])),
        (0, 'the multiplet lost in tracking', lambda r: r['t1'].__setitem__('tracked_ok', False)),
        (1, 'the competitor taken as unique', lambda r: r['t2'].__setitem__('ok', True)),
        (2, 'the close pair resolved', lambda r: r['t3']['close'].__setitem__('ok', True)),
        (2, 'the apart pair picking the wrong block', lambda r: r['t3']['apart'].__setitem__('blocks', [1])),
        (3, 'the outside candidate anchored', lambda r: r['t4'].__setitem__('anchor_ok', True)),
        (4, 'the class change not recorded', lambda r: r['t5'].__setitem__('change', False)),
        (5, 'one of the colliding tracks kept', lambda r: r['t6']['A'].__setitem__('ok', True)),
        (6, 'the out-of-band block taken', lambda r: r['t7'].__setitem__('ok', True)),
    ]
    parent = [ok for _, ok in evaluate(R)]
    out = []
    for k, label, f in arms:
        r = copy.deepcopy(R)
        f(r)
        got = [ok for _, ok in evaluate(r)]
        out.append(dict(check=k + 1, mutation=label,
                        caught=bool(parent[k] and not got[k] and all(got[j] == parent[j] for j in range(len(got)) if j != k))))
    return out


if __name__ == '__main__':
    R = dict(t1=test1(), t2=test2(), t3=test3(), t4=test4(), t5=test5(), t6=test6(), t7=test7())
    checks = evaluate(R)
    muts = mutations(R)
    S = dict(test='control 2a, the synthetic classifier tests (REGISTER_2.md § 5)',
             written=datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ'),
             checks=[dict(check=c, passed=bool(ok)) for c, ok in checks], all_passed=all(ok for _, ok in checks),
             mutations=muts, all_mutations_caught=all(m['caught'] for m in muts), results=R)
    json.dump(S, open(os.path.join(HERE, 'control_2a_synthetic.json'), 'w'), indent=1, default=str)
    L = [f'control 2a, synthetic classifier tests: {S["written"]}'] + [f'  {k}: {v}' for k, v in R.items()] + ['']
    L += [f'  {"PASS" if ok else "FAIL"}  {c}' for c, ok in checks]
    L.append(f'all registered checks passed: {S["all_passed"]}')
    L += [f'  {"caught" if m["caught"] else "MISSED"}  check {m["check"]}: {m["mutation"]}' for m in muts]
    L.append(f'every mutation caught by its own check alone: {S["all_mutations_caught"]}')
    open(os.path.join(HERE, 'control_2a_synthetic.log'), 'w').write('\n'.join(L) + '\n')
    print('\n'.join(L))
