#!/usr/bin/env python3
"""
score-consistency.test.py -- regression test for the public Score tables. (2026-09-01)

The root README's Score is an aggregate of the two section landings: every row on
cosmos/README or spectrum/README also appears on the root. That duplication is
deliberate (the front door needs its number column, the landings need theirs), so
this test does not remove it; it makes a disagreement fail loudly instead of waiting
to be noticed.

What this buys, stated honestly: a cell like the KATRIN limit still lives twice, in
spectrum and in root. What changes is that a divergence becomes a failing assertion
rather than a discovery. On 2026-09-01 three cells had drifted between a landing and
the root (the alpha-route Lambda, the color-channel wording, and a superseded KATRIN
limit) and sat wrong until someone thought to compare by eye. If this test starts
failing often, that is the evidence that generating the root Score from the two
section tables has become worth the build step.

Repaired 2026-09-25. The Score header had gained a Standing column, which the parser
never matched, so every page parsed zero rows and the test passed while comparing
nothing. It now fails when a page lacks the header or parses no rows, compares every
column, Standing included, at an exact row width, and runs controls: planted defects,
each of which must fail before the test reports a pass.

Scope: internal propagation only. It does NOT check whether a value is scientifically
current -- that is a data-maintenance question and mixing it in would turn a
deterministic repo test into a monitor.

Convention: run after any edit to the root, cosmos, or spectrum Score tables.
Run:  python3 score-consistency.test.py     (stdlib only; exit 1 on drift, or when a control does not fail)
"""
import os, re, sys

# The Euclid card is a deposited pre-registration with its own header
# ("| Prediction | Value | Euclid DR1 channel | Falsified if |"). It is excluded by
# construction here rather than by luck: it must never be asserted against a landing.
SCORE_HEADER = "| Observable | Standing | Output | Observed | Agreement |"
# The data columns, read off the header, so a renamed or added column changes what is compared.
COLUMNS = [c.strip() for c in SCORE_HEADER.strip().strip("|").split("|")][1:]

LANDINGS = {"cosmos": "files/cosmos/README.md", "spectrum": "files/spectrum/README.md"}
ROOT = "README.md"


def repo_root():
    """Walk upward from this file until all three Score-bearing pages exist."""
    d = os.path.dirname(os.path.abspath(__file__))
    while d != os.path.dirname(d):
        if all(os.path.exists(os.path.join(d, p)) for p in [ROOT, *LANDINGS.values()]):
            return d
        d = os.path.dirname(d)
    sys.exit("could not locate the repository root from this file's position")


def canonical(target, page):
    """Resolve a link target to a repo-relative path so root's '/files/x/y.md' and a
    landing's 'files/y.md' or '../spectrum/z.md' compare equal."""
    path, _, anchor = target.partition("#")
    path = path.lstrip("/") if target.startswith("/") else os.path.join(os.path.dirname(page), path)
    return os.path.normpath(path) + ("#" + anchor if anchor else "")


def split_cells(line):
    """A table row's cells, split on unescaped pipes only, as GitHub splits them."""
    return [c.strip() for c in re.split(r"(?<!\\)\|", line.strip().strip("|"))]


def score_rows(text, page):
    """Parse the page's Score table only. Returns (header_found, rows, width_errors), with
    rows as {identity: (label, [data cells])}."""
    rows, errors, inside, found = {}, [], False, False
    for line in text.split("\n"):
        if line.strip() == SCORE_HEADER:
            inside = found = True
            continue
        if inside:
            if not line.startswith("|"):
                break
            # Separator detection must be structural: a line whose cells are ALL
            # dashes. A substring test for "---" would silently drop the w_eff row,
            # whose anchor slugifies "> -1" into a literal "---", and a row the parser
            # never sees is a row the test never checks.
            if set(line.strip()) <= set("|-: "):
                continue
            cells = split_cells(line)
            m = re.search(r"\[↗\]\(([^)]+)\)", cells[0])
            label = re.sub(r"\[↗\]\([^)]*\)", "", cells[0]).strip()
            # A row of the wrong width is an error in its own right: comparing it cell by
            # cell would silently skip a missing or extra trailing cell.
            if len(cells) != len(COLUMNS) + 1:
                errors.append(f"{page}: {label!r} has {len(cells)} cells, the header {len(COLUMNS) + 1}")
            # Identity is the link target PLUS the visible label. Target alone is not
            # unique: several rows share one anchor (#iii-the-24-entries carries four),
            # and keying on it silently collapses them, so rows would drop out of the
            # comparison and the test would pass by ignoring them. A label rename then
            # breaks identity, which surfaces as a presence WARNING for a human to
            # adjudicate rather than a false drift failure.
            ident = (canonical(m.group(1), page) if m else "", label)
            # Embedded link targets are resolved the same way row identity is: root
            # writes them absolute and the landings relative, which is notation rather
            # than drift. Everything else in the cell is compared literally.
            data = [re.sub(r"\]\(([^)]+)\)", lambda m: "](" + canonical(m.group(1), page) + ")", c)
                    for c in cells[1:]]
            rows[ident] = (label, data)
    return found, rows, errors


def compare(texts):
    """Check the three Score tables against each other. texts maps each page to its text.
    Returns (hard failures, warnings, (root rows, cosmos rows, spectrum rows, shared rows))."""
    hard, warn, parsed = [], [], {}
    # 0. every page must carry the header and parse rows; a missing header or an empty
    #    table is a failure, never a vacuous pass
    for page in [ROOT, *LANDINGS.values()]:
        found, rows, errors = score_rows(texts[page], page)
        if not found:
            hard.append(f"Score header missing on {page} (expected {SCORE_HEADER})")
        elif not rows:
            hard.append(f"zero rows parsed on {page}")
        hard += errors
        parsed[page] = rows
    r, c, s = parsed[ROOT], parsed[LANDINGS["cosmos"]], parsed[LANDINGS["spectrum"]]
    locals_ = {"cosmos": c, "spectrum": s}

    # 1. the landings partition: no row may be owned by two sections at once
    both = set(c) & set(s)
    if both:
        hard += [f"owned by BOTH landings: {b}" for b in sorted(both)]

    # 2. presence. Unmatched rows are a HARD failure by default, so that "every root
    #    row has an owner" is genuinely asserted and a deletion cannot slip through.
    #    The single exception is a demonstrable rename: exactly one unmatched row on
    #    each side sharing the same normalised link target, with only the visible label
    #    changed. That is downgraded to a warning, because renaming is legitimate
    #    maintenance and a checker that fails on it gets muted within a week. If the
    #    pairing is ambiguous, fail rather than guess.
    union = set(c) | set(s)
    only_local, only_root = sorted(union - set(r)), sorted(set(r) - union)
    for lk in list(only_local):
        cands = [rk for rk in only_root if rk[0] == lk[0]]
        peers = [x for x in only_local if x[0] == lk[0]]
        if len(cands) == 1 and len(peers) == 1:
            warn.append(f"probable rename on {lk[0]}: landing {lk[1]!r} vs root {cands[0][1]!r}")
            only_local.remove(lk); only_root.remove(cands[0])
    hard += [f"on a landing, absent from root (deletion or unpairable rename): {k}" for k in only_local]
    hard += [f"on root, no landing owns it (addition or unpairable rename):    {k}" for k in only_root]

    # 3. cell equality on every shared row, every column. This is unambiguous drift, so it
    #    is hard. Nothing is normalised except surrounding whitespace: math wrappers, signs,
    #    units, status words and numeric formatting are exactly what we want to catch.
    for owner, rows in locals_.items():
        for ident, (label, cells) in rows.items():
            if ident not in r:
                continue
            rl, rc = r[ident]
            for i in range(max(len(rc), len(cells))):
                a = rc[i] if i < len(rc) else "(no cell)"
                b = cells[i] if i < len(cells) else "(no cell)"
                if a != b:
                    col = COLUMNS[i] if i < len(COLUMNS) else f"col{i + 2}"
                    hard.append(f"{owner}: {label or rl}\n      [{col}]  root: {a}\n      "
                                f"{' ' * len(col)}   {owner}: {b}")
    return hard, warn, (len(r), len(c), len(s), len(set(r) & union))


def first_row(text):
    """The first data row of a page's Score table."""
    lines = text.split("\n")
    k = next(i for i, l in enumerate(lines) if l.strip() == SCORE_HEADER)
    return next(l for l in lines[k + 1:] if not set(l.strip()) <= set("|-: "))


def controls(texts):
    """Planted defects, each of which must fail. Returns [(name, fired)]."""
    out = []
    sp, co = LANDINGS["spectrum"], LANDINGS["cosmos"]
    # a drifted Standing cell on a landing must fail, naming the row and the column
    row = first_row(texts[sp])
    cells = re.split(r"(?<!\\)\|", row)
    label = re.sub(r"\[↗\]\([^)]*\)", "", cells[1]).strip()
    cells[2] = " `planted` "
    hard, _, _ = compare({**texts, sp: texts[sp].replace(row, "|".join(cells), 1)})
    out.append((f"a drifted Standing cell on {sp}", any(label in h and "[Standing]" in h for h in hard)))
    # a renamed header must fail as a missing header, not pass as an empty table
    hard, _, _ = compare({**texts, co: texts[co].replace(SCORE_HEADER, SCORE_HEADER.replace(" Standing |", ""), 1)})
    out.append((f"the Score header renamed on {co}", any("Score header missing on " + co in h for h in hard)))
    # a header with no rows under it must fail
    lines = texts[sp].split("\n")
    k = next(i for i, l in enumerate(lines) if l.strip() == SCORE_HEADER)
    body = [i for i in range(k + 1, len(lines)) if lines[i].startswith("|")]
    body = body[:next((j for j, i in enumerate(body) if i != body[0] + j), len(body))]
    kept = [l for i, l in enumerate(lines) if i not in body or set(l.strip()) <= set("|-: ")]
    hard, _, _ = compare({**texts, sp: "\n".join(kept)})
    out.append((f"the Score rows removed on {sp}", any("zero rows parsed on " + sp in h for h in hard)))
    # a root row missing its last cell must fail on width
    rrow = first_row(texts[ROOT])
    short = "|".join(re.split(r"(?<!\\)\|", rrow.rstrip())[:-2]) + "|"
    hard, _, _ = compare({**texts, ROOT: texts[ROOT].replace(rrow, short, 1)})
    out.append(("a root row missing its last cell", any("cells, the header" in h for h in hard)))
    return out


def main():
    root = repo_root()
    texts = {p: open(os.path.join(root, p), encoding="utf-8").read() for p in [ROOT, *LANDINGS.values()]}
    hard, warn, (nr, nc, ns, shared) = compare(texts)
    if nr != nc + ns and not hard:
        hard.append(f"root {nr} rows, but cosmos {nc} + spectrum {ns}")
    ran = not any("Score header missing" in h or "zero rows parsed" in h for h in hard)
    ctl = controls(texts) if ran else []

    for w in warn:
        print(f"  WARN  {w}")
    for h in hard:
        print(f"  FAIL  {h}")
    for name, fired in ctl:
        print(f"  {'control fails as required' if fired else 'CONTROL DID NOT FAIL'}: {name}")
    missed = [n for n, f in ctl if not f]
    if hard or missed or not ctl:
        print(f"\nFAIL: {len(hard)} scorecard disagreement(s)"
              + (f"; {len(missed)} control(s) did not fail" if missed else "")
              + ("; controls not run" if not ctl else ""))
        return 1
    print(f"PASS: root {nr} = cosmos {nc} + spectrum {ns}; {shared} shared rows match; "
          f"{len(ctl)}/{len(ctl)} controls fail as required"
          + (f"; {len(warn)} warning(s) needing human adjudication" if warn else ""))
    return 0


if __name__ == "__main__":
    sys.exit(main())
