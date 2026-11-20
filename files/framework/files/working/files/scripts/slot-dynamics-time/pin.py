"""The instrument's pin. Every script in this folder calls instrument_path() before it imports the instrument. The 12
paths in INSTRUMENT.sha256, resolved, must be distinct, must lie in M8.16.1's instrument folder, and must be exactly
the files present there, `__pycache__` aside (and a Finder `.DS_Store`, which nothing imports), so that no file is
skipped, repeated or shadowed: Python's importer takes a package directory or an extension module of the same name
before a `.py` file. Each file must match the SHA-256 computed from git at M8.16.1's frozen commit, d1c0ec8. Otherwise
the script stops. It returns the folder to put on sys.path for `from instrument import ...`."""
import hashlib
import os

HERE = os.path.dirname(os.path.abspath(__file__))
FOLDER = os.path.realpath(os.path.join(HERE, '..', 'soft-slot-dynamics-m8-16-1'))
INSTRUMENT = os.path.join(FOLDER, 'instrument')
ASIDE = {'__pycache__', '.DS_Store'}


def instrument_path():
    with open(os.path.join(HERE, 'INSTRUMENT.sha256'), encoding='utf-8') as f:
        rows = [line.split(None, 1) for line in f if line.strip()]
    pinned = {}
    for digest, rel in rows:
        path = os.path.realpath(os.path.join(HERE, rel.strip()))
        if os.path.dirname(path) != INSTRUMENT:
            raise SystemExit(f'refused: {rel.strip()} is not in M8.16.1\'s instrument folder')
        if path in pinned:
            raise SystemExit(f'refused: {rel.strip()} is pinned twice')
        pinned[path] = digest
    present = {os.path.realpath(os.path.join(INSTRUMENT, f)) for f in os.listdir(INSTRUMENT) if f not in ASIDE}
    if len(pinned) != 12 or set(pinned) != present:
        raise SystemExit('refused: the pinned files are not exactly the 12 files of the instrument folder')
    for path, digest in pinned.items():
        if not os.path.isfile(path):
            raise SystemExit(f'refused: {os.path.basename(path)} is not a file')
        with open(path, 'rb') as g:
            if hashlib.sha256(g.read()).hexdigest() != digest:
                raise SystemExit(f'refused: {os.path.basename(path)} differs from its frozen SHA-256')
    return FOLDER
