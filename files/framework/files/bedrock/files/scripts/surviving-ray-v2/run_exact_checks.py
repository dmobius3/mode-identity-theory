#!/usr/bin/env python3
"""Run the exact checks of Sections 6, 7.2 and 7.3 of Surviving Ray v2 and save one log for each.

The four scripts are self-contained (SymPy, and NumPy for one random-sampling line that is labelled as such) and read
no files. Each log opens with the SHA-256 of the script that wrote it, so a log names its own source without the
script having to hash itself, and the run passes only when every script exits 0 and its output ends in ALL PASS.
"""
import hashlib
import subprocess
import sys
from pathlib import Path

import mpmath
import numpy
import sympy

HERE = Path(__file__).resolve().parent
SCRIPTS = [('check_coupling_point.py', 'Section 6: Proposition 6.1, the point'),
           ('check_line_extrema.py', 'Section 7.2: the line extrema of the census orbits'),
           ('check_minimum_identity.py', 'Section 7.3: Lemma 7.3 and the minimum'),
           ('check_maximum_steps.py', 'Section 7.3: the steps of the maximum')]
print(f'script {Path(__file__).name}: SHA-256 {hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}')
print(f'python {sys.version.split()[0]}, sympy {sympy.__version__}, numpy {numpy.__version__}, mpmath {mpmath.__version__}')
ok_all = True
for name, what in SCRIPTS:
    src = HERE / name
    digest = hashlib.sha256(src.read_bytes()).hexdigest()
    run = subprocess.run([sys.executable, str(src)], capture_output=True, text=True, cwd=HERE)
    out = run.stdout + (run.stderr if run.stderr else '')
    log = HERE / name.replace('.py', '_log.txt')
    log.write_text(f'script {name}: SHA-256 {digest}\n' + out, encoding='utf-8')
    ok = run.returncode == 0 and out.rstrip().endswith('ALL PASS')
    ok_all = ok_all and ok
    n_pass = sum(1 for line in out.splitlines() if line.startswith('PASS'))
    print(f'{"PASS" if ok else "FAIL"} {name} ({what}): exit {run.returncode}, {n_pass} PASS lines, log {log.name}')
print('ALL PASS' if ok_all else 'SOME FAILED')
sys.exit(0 if ok_all else 1)
