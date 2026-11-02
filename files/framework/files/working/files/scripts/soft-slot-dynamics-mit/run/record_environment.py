#!/usr/bin/env python3
"""The environment the manifest records (the terms: THE INSTRUMENT, FIXED; UA, UB at step 1 of the freeze).

Usage: record_environment.py            write run/ENVIRONMENT.json once, by exclusive create, before the pin
       record_environment.py --check    read the live environment again and compare it with the record

Run it with the run's own interpreter and flags, `python3 -I -B`. It reads the interpreter, NumPy and SciPy with
their BLAS and LAPACK configuration, the threading variables those libraries read, the macOS version and build that
ship Accelerate, and the machine. Nothing else in the environment is read. The check compares every field except the
time of the reading, prints both readings, and exits 1 on any difference; at the freeze block, a difference goes to
the units before the run starts (UB).
"""
import datetime
import hashlib
import json
import os
import platform
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
PATH = os.path.join(HERE, 'ENVIRONMENT.json')
THREADS = ('VECLIB_MAXIMUM_THREADS', 'OMP_NUM_THREADS', 'OPENBLAS_NUM_THREADS', 'MKL_NUM_THREADS')


def _cmd(*args):
    return subprocess.run(args, capture_output=True, text=True, check=True).stdout.strip()


def _linalg(module):
    deps = module.show_config(mode='dicts')['Build Dependencies']
    return {'version': module.__version__, 'blas': deps['blas'], 'lapack': deps['lapack']}


def read():
    import numpy
    import scipy
    sysctl = lambda key: _cmd('/usr/sbin/sysctl', '-n', key)
    return {
        'interpreter': {'executable': sys.executable, 'implementation': platform.python_implementation(),
                        'version': platform.python_version(), 'build': sys.version,
                        'flags': {'isolated': sys.flags.isolated, 'dont_write_bytecode': sys.flags.dont_write_bytecode,
                                  'optimize': sys.flags.optimize}},
        'numpy': _linalg(numpy),
        'scipy': _linalg(scipy),
        'threading': {v: os.environ.get(v) for v in THREADS},
        'os': {'product': _cmd('/usr/bin/sw_vers', '-productName'), 'version': platform.mac_ver()[0],
               'build': _cmd('/usr/bin/sw_vers', '-buildVersion'), 'kernel': platform.release()},
        'machine': {'arch': platform.machine(), 'model': sysctl('hw.model'),
                    'cpu': sysctl('machdep.cpu.brand_string'), 'cores': int(sysctl('hw.ncpu')),
                    'performance_cores': int(sysctl('hw.perflevel0.physicalcpu')),
                    'efficiency_cores': int(sysctl('hw.perflevel1.physicalcpu'))},
    }


def _flat(d, pre=''):
    for k, v in d.items():
        if isinstance(v, dict):
            yield from _flat(v, f'{pre}{k}.')
        else:
            yield f'{pre}{k}', v


def check():
    with open(PATH, encoding='utf-8') as f:
        rec = json.load(f)
    live = read()
    rec.pop('recorded', None)
    a, b = dict(_flat(rec)), dict(_flat(live))
    diff = sorted(k for k in set(a) | set(b) if a.get(k) != b.get(k))
    print('recorded:', json.dumps(rec, indent=1, sort_keys=True))
    print('live:', json.dumps(live, indent=1, sort_keys=True))
    print('differences:', diff if diff else 'none')
    return not diff


if __name__ == '__main__':
    if sys.argv[1:] == ['--check']:
        raise SystemExit(0 if check() else 1)
    if sys.argv[1:]:
        raise SystemExit(__doc__)
    env = read()
    env['recorded'] = datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')
    text = json.dumps(env, indent=1, sort_keys=True) + '\n'
    with open(PATH, 'x', encoding='utf-8') as f:
        f.write(text)
    print(text, end='')
    print('ENVIRONMENT.json written;', hashlib.sha256(text.encode('utf-8')).hexdigest())
