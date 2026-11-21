"""Development (DEVLOG entry 13): faults injected into the rule of section 4, to check what the records say. Not a
control. A development context writes into a temporary folder, with stand-ins for what controls 3 to 9 hand the rule.
Two cases:
  - the ceiling: C-bar for the rule's equal-cost runs is set just above kappa, the member's norm^2 at the splitting's
    kick, so that the perturbed trajectory crosses it after its start. The records must hold 12_rule.json, failed with
    the ceiling's step; SUMMARY.json, stopped after the rule; and no 11_c11.json.
  - an error: the rule's setup raises. SUMMARY.json must hold the error at the rule, and there must be neither
    12_rule.json nor 11_c11.json."""
import json
import os
import sys
import tempfile

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import controls as C  # noqa: E402


def stand_ins(ctx):
    res = {c: dict(passed=True, by_kind={'verlet': True, 'strang': True})
           for c in ('c1', 'c2', 'c3', 'c4', 'c5', 'c6', 'c7', 'c8', 'c9')}
    for slot in ctx.P['rigid']:
        ctx.c6[slot] = dict(tau={'verlet': 1.0, 'strang': 1.0}, verlet=[{'errors': {'2omega': 1e-3, 'radial': 1e-3}}])
    return res


real = C.setup_B


def near_kappa(ctx, slot):
    R = real(ctx, slot)
    R['cbar'] = R['kappa'] * (1 + 1e-9)
    return R


def raises(ctx, slot):
    raise RuntimeError('a fault injected into the rule')


ok = 0
for case, setup in (('ceiling', near_kappa), ('error', raises)):
    out = os.path.join(tempfile.mkdtemp(), 'run')
    ctx = C.Ctx(True, out=out)
    C.setup_B = setup
    try:
        stopped, error = C.finish(ctx, stand_ins(ctx), None, None, dict(env=ctx.env))
    finally:
        C.setup_B = real
    files = sorted(os.listdir(out))
    with open(os.path.join(out, 'SUMMARY.json'), encoding='utf-8') as f:
        summary = json.load(f)
    if case == 'ceiling':
        with open(os.path.join(out, '12_rule.json'), encoding='utf-8') as f:
            rule = json.load(f)['result']
        good = (stopped == 'rule' and error is None and summary['stopped_after'] == 'rule' and rule['passed'] is False
                and 'at step' in rule['ceiling'] and not rule['ceiling'].endswith('at step 0')
                and '11_c11.json' not in files)
        print(f'ceiling: {rule["ceiling"]}; stopped after {summary["stopped_after"]}; files {files}')
    else:
        good = (stopped is None and summary['error']['control'] == 'rule' and 'RuntimeError' in
                summary['error']['traceback'] and '12_rule.json' not in files and '11_c11.json' not in files)
        print(f'error: recorded at {summary["error"]["control"]}; files {files}')
    ok += good
print(f'fault injection: {ok} of 2 cases recorded as required')
