"""M8.15.2's guard, written once (REGISTER_5.md § 1): out/FROZEN.json in this folder, at M8.15.2's freeze, after the
maintainer's go. This step refuses if the file exists, and the driver never writes it.

  python3 write_guard.py TERMS GO [DESCRIPTION]     TERMS: M8.15.2's terms file; GO: the maintainer's go, a link

The guard holds every value of the instrument's out/freeze_numbers.json unchanged; frozen true; the terms' SHA-256; the
go; the instrument manifest's SHA-256, which must equal the pin in t1_branch.py; and the SHA-256 of this folder's
locate.py and t1_branch.py."""
import os, sys, json

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import locate, t1_branch


def guard_values(terms, go, description=None, instr=locate.INSTRUMENT):
    """Every value the guard holds."""
    manifest = t1_branch.check_instrument(instr)
    if manifest != t1_branch.MANIFEST_SHA256:
        raise SystemExit("refused: the instrument manifest's SHA-256 is not the pinned one")
    if not go:
        raise SystemExit('refused: no go')
    fn = json.load(open(os.path.join(instr, 'out', 'freeze_numbers.json')))
    return dict(fn, frozen=True, terms_sha256=t1_branch.sha(terms), terms=description or os.path.basename(terms), go=go,
                instrument_manifest_sha256=manifest,
                locator_sha256={f: t1_branch.sha(os.path.join(HERE, f)) for f in ('locate.py', 't1_branch.py')},
                written=t1_branch.now())


def write(terms, go, description=None, instr=locate.INSTRUMENT, path=t1_branch.GUARD):
    """Write the guard once: the text is built first, then the file is created exclusively, so nothing is overwritten."""
    if os.path.exists(path):
        raise SystemExit(f'refused: {path} exists; the guard is written once')
    text = json.dumps(guard_values(terms, go, description, instr), indent=1) + '\n'
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, 'x') as f:
        f.write(text)
    return path


if __name__ == '__main__':
    if len(sys.argv) not in (3, 4):
        raise SystemExit(__doc__)
    print('written:', write(sys.argv[1], sys.argv[2], sys.argv[3] if len(sys.argv) == 4 else None))
