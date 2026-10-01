#!/usr/bin/env python3
"""Standing gate for projective-carrier.md. No args: the checks. --arms: each check must fail on a planted defect,
parent green first.

Run it from a checkout of this repository at origin/main, with network access and an authenticated gh CLI. P3 reads
anchor ids from GitHub's rendering of each linked page at HEAD, P4 renders the page through `gh api markdown`, and a
missing tool, a failed fetch or a checkout off origin/main stops the run with an error: nothing is skipped. Every
check reads the working tree, the state about to be committed. P3 takes an anchor from GitHub's ids only where a
page's bytes match HEAD, and there the local heading rule must agree with it; a page with uncommitted edits is
checked by the local rule alone. The page
quotes other pages, so rerun this gate whenever one of them changes. A commit that changes a quoted sentence, such as a
scope note, updates or dates the matching entry of the page's §X in the same commit."""
import hashlib, html, os, re, subprocess, sys, unicodedata, urllib.parse, urllib.request

HERE = os.path.dirname(os.path.abspath(__file__))
SCRIPTS = HERE


def sh(a, cwd=HERE, **kw):
    return subprocess.run(a, cwd=cwd, text=True, capture_output=True, check=True, **kw).stdout


REPO = sh(["git", "rev-parse", "--show-toplevel"]).strip()
WF = "files/framework/files/working/files"
PAGE = os.path.join(REPO, WF, "projective-carrier.md")
SELF_REL = WF + "/projective-carrier.md"
HEAD = sh(["git", "rev-parse", "HEAD"], REPO).strip()
if HEAD != sh(["git", "rev-parse", "origin/main"], REPO).strip():
    sys.exit("gate: the checkout is not at origin/main")
src = lambda rel: open(os.path.join(REPO, rel), encoding="utf-8").read()
_LIVE = {}
_HEAD = {}


def at_head(rel):
    if rel not in _HEAD:
        r = subprocess.run(["git", "show", f"HEAD:{rel}"], cwd=REPO, capture_output=True)
        _HEAD[rel] = r.stdout.decode("utf-8") if r.returncode == 0 else None
    return _HEAD[rel]


def live_ids(rel):
    if rel not in _LIVE:
        for attempt in range(4):
            try:
                page = urllib.request.urlopen(f"https://github.com/dmobius3/mode-identity-theory/blob/{HEAD}/{urllib.parse.quote(rel)}").read().decode()
                break
            except Exception:
                if attempt == 3:
                    raise
        _LIVE[rel] = {urllib.parse.unquote(i) for i in re.findall(r'user-content-([^"\\&\s]+)', page)}
    return _LIVE[rel]


KEEP = ("Lu", "Ll", "Lt", "Lm", "Lo", "Nd", "Mn")


def slug(h):
    """GitHub's heading id: link and math text kept, lowercased, spaces to hyphens; only letters, decimal digits,
    combining marks, hyphens and underscores survive, so superscript digits drop out."""
    h = re.sub(r"!?\[([^\]]*)\]\([^)]*\)", r"\1", h)
    h = re.sub(r"\$`([^`]*)`\$", r"\1", h)
    h = re.sub(r"`([^`]*)`", r"\1", h).strip().lower()
    return "".join("-" if ch == " " else ch for ch in h if ch in " -_" or unicodedata.category(ch) in KEEP)


def sections(md):
    """anchor -> (start, end) of its section: heading slugs, and explicit <a id> anchors above headings."""
    heads = [(m.start(), len(m.group(1)), m.group(2)) for m in re.finditer(r"^(#{1,6}) +(.*)$", md, re.M)]
    spans = {}
    for i, (pos, lvl, text) in enumerate(heads):
        end = next((p for p, l, _ in heads[i + 1:] if l <= lvl), len(md))
        spans.setdefault(slug(text), (pos, end))
    for m in re.finditer(r'<a id="([^"]+)"></a>\s*\n(#{1,6}) ', md):
        lvl = len(m.group(2))
        nxt = [p for p, l, _ in heads if p > m.end() and l <= lvl]
        spans[m.group(1)] = (m.start(), nxt[0] if nxt else len(md))
    return spans


QUOTES = [  # (exact bytes on the page, the corpus page that must contain them at HEAD)
    ("are antipodal maps on different spheres serving different purposes, and they must not be merged.", f"{WF}/sampler-first-test.md"),
    ("the band's $`\\mathbb{Z}_2`$ cannot be a $`2I`$-equivariant datum", f"{WF}/postulate-bridge.md"),
    ("cannot be identified with any $`2I`$-datum", f"{WF}/postulate-bridge.md"),
    ("The covering geometry constrains, but does not by itself fix, the extension", "files/framework/files/bedrock/files/first-eigenvalue.md"),
    ("the edge-identified quotient of a totally geodesic covering great-$`S^2`$ band in $`S^3`$", "files/cosmos/files/cosmological-constant.md"),
    ("transverse, not restrictive", f"{WF}/postulate-bridge.md"),
    ("time is the boundary of a non-orientable surface embedded in a closed three-space", "files/framework/README.md"),
    ("The twists and identifications live in that built structure", "files/framework/README.md"),
    ("and not the Möbius orientation sign of One Shape", "files/framework/README.md"),
    ("The Möbius sign flip and the central $`-I`$ of $`2I`$ are two distinct $`Z_2`$'s", "files/framework/README.md"),
    ("the framework does not collapse them into one", "README.md"),
    ("an embedded spectral carrier", "files/cosmos/files/cosmological-constant.md"),
    ("the Möbius surface embedded in $`S^3`$", "files/cosmos/files/euclid-dr1.md"),
    ("The dance runs on two distinct seams", "files/spectrum/files/the-waltz.md"),
    ("the orientation $`\\mathbb{Z}_2`$ is not a $`2I`$-equivariant datum", f"{WF}/postulate-bridge.md"),
    ("$`\\mathbb Z_2^{\\text{Möbius}} \\neq \\mathbb Z_2^{\\text{centre}}`$ as identified structures", f"{WF}/postulate-bridge.md"),
    ("the two $`\\mathbb{Z}_2`$ structures remain distinct", f"{WF}/postulate-bridge.md"),
    ("canonically trivial", f"{WF}/postulate-bridge.md"),
    ("a circle as the edge of a Möbius band embedded in $`S^3`$", f"{WF}/postulate-bridge.md"),
    ("postulate embedding", f"{WF}/postulate-bridge.md"),
    ("The zero-excitation equilibrium cannot be the totally geodesic embedding", f"{WF}/postulate-bridge.md"),
    ("The topology excludes the zero-bending configuration", f"{WF}/postulate-bridge.md"),
    ("The central $`2I`$ sign and the Möbius normal sign are independent structures", f"{WF}/sampler-first-test.md"),
    ("$`\\mathcal L`$'s $`\\mathbb Z_2`$ cannot be a $`2I`$ character", f"{WF}/sampler-first-test.md"),
    ("the two $`\\mathbb{Z}_2`$ structures are different objects", f"{WF}/variational-score-to-sample.md"),
    ("not the Möbius orientation $`Z_2`$, which the framework keeps distinct from that split", f"{WF}/plato-twist.md"),
    ("stays distinct both from the base edge $`Z_2`$ above and from the central $`-I`$ inside the lifted $`Z_4`$", "files/spectrum/files/mass-spectrum.md"),
    ("group each block carries", f"{WF}/scaling-law-uniqueness.md"),
    ("The postulate embedding must be a critical point of the independently motivated functional whose second variation is nonnegative on every admissible variation of the declared class", f"{WF}/postulate-bridge.md"),
    ("A restriction on the admissible variations counts only when the postulate motivates it and it is declared before the computation, never because it rescues a candidate.", f"{WF}/postulate-bridge.md"),
    ("only after a further mechanism selects the realized member", f"{WF}/postulate-bridge.md"),
    ("a singular surface model", "files/framework/files/bedrock/README.md"),
    ("the extension selection", f"{WF}/scaling-law-uniqueness.md"),
    ("spectrally an orientable object", "files/framework/files/bedrock/files/first-eigenvalue.md"),
    ("the one quantity in the model that the intrinsic geometry leaves free", "files/framework/files/bedrock/files/first-eigenvalue.md"),
    ("the framework's default", f"{WF}/scaling-law-uniqueness.md"),
    ("an Euler-Lagrange matching equation", f"{WF}/postulate-bridge.md"),
    ("assumed as an inclusion by hand", f"{WF}/postulate-bridge.md"),
    ("the Friedrichs realization is spectrally an orientable object, a Neumann lune", "files/framework/files/bedrock/files/first-eigenvalue.md"),
    ("a singular surface model, not a smooth totally geodesic submanifold of $`S^3/2I`$", "files/framework/files/bedrock/README.md"),
    ("not by seating the Möbius band inside $`S^3/2I`$", "files/framework/files/bedrock/README.md"),
    ("The deeper obstruction", f"{WF}/postulate-bridge.md"),
    ("The band lives upstairs on a great $`S^2 \\subset S^3`$", f"{WF}/postulate-bridge.md"),
    ("compose only if the surface is group-stable, and it is not", f"{WF}/postulate-bridge.md"),
    ("left translation by any non-central element moves the defining $`3`$-plane", f"{WF}/postulate-bridge.md"),
    ("the band does not descend (the deeper obstruction)", f"{WF}/postulate-bridge.md"),
    ("rules out descent of the band to $`X`$ as a $`2I`$-stable submanifold", f"{WF}/postulate-bridge.md"),
    ("the deck element $`-1`$ never stabilizes an admissible band", "files/framework/files/working/README.md"),
    ("Tier 2's totally geodesic candidate has been removed: it is topologically unavailable to a smooth Möbius band", f"{WF}/postulate-bridge.md"),
    ("the transverse-not-restrictive result as the residue", f"{WF}/postulate-bridge.md"),
    ("should not be rescued by modifying the band", f"{WF}/sampler-first-test.md"),
    ("of which the Möbius carrier is the edge-identified quotient", "files/cosmos/files/cosmological-constant.md"),
    ("an exact same-mode identity", f"{WF}/scaling-law-uniqueness.md"),
    ("Excited modes ($`m > 0`$) on the Möbius surface bend the embedding", "files/spectrum/files/the-waltz.md"),
    ("the extension question governs only the ground state, which the factorization never samples", f"{WF}/scaling-law-uniqueness.md"),
    ("even had $`S = \\{\\pm 1\\}`$ been achievable", f"{WF}/sampler-first-test.md"),
    ("nothing would have been resolved at sixty either", f"{WF}/sampler-first-test.md"),
    ("belong to a named operator on the embedded band's induced metric rather than being imported from the intrinsic conic pillar", f"{WF}/postulate-bridge.md"),
    ("This decouples the factorization from the extension selection", f"{WF}/scaling-law-uniqueness.md"),
    ("bridging extension (not Friedrichs; see §II)", f"{WF}/cone-point-coherence.md"),
    ("the holonomy picks out the twisted sector", "files/cosmos/files/cosmological-constant.md"),
    ("The holonomy selects the twisted sector in which the first positive level is identified", "files/cosmos/files/cosmological-constant.md"),
    ("The anti-periodic flip acts per lap", "files/framework/README.md"),
    ("The paper's model is intrinsic, and the paper places it in no three-dimensional space", "files/cosmos/files/black-hole.md"),
    ("These are different operations doing different jobs", "files/framework/README.md"),
    ("The two seams share one step without merging", "files/framework/README.md"),
    ("the orientation sign and the central $`-I`$ are carried by one loop", "files/framework/README.md"),
    ("which of the two layers is the carrier's physical domain is open", "files/framework/README.md"),
    ("enters separately", "files/framework/files/bedrock/README.md"),
    ("The quotient's central stage reaches the band itself", "files/framework/files/bedrock/README.md"),
    ("The carrier embeds unbent in the projective layer", "files/framework/files/bedrock/README.md"),
    ("embeds, unbent, in the space that results", "README.md"),
    ("first step is that same identification", "README.md"),
    ("The postulate embeds a non-orientable carrier, unbent, in its central quotient", "files/cosmos/files/cosmological-constant.md"),
]

EXPECTED = {  # each record's PASS and ARM FIRED lines, exactly
    'smooth_band': ['ARM FIRED S1 RP² eigenfunctions at λ = 2 exactly', 'ARM FIRED S2 first twisted level below 2 at each sampled width', 'ARM FIRED S3 increasing across the sampled widths, within 2e-3 of 2 at W = 1.55', 'ARM FIRED S4 at each sampled width the k = ±1 branch lies below the k = 0 branch', 'PASS S1 RP² eigenfunctions at λ = 2 exactly', 'PASS S2 first twisted level below 2 at each sampled width', 'PASS S3 increasing across the sampled widths, within 2e-3 of 2 at W = 1.55', 'PASS S4 at each sampled width the k = ±1 branch lies below the k = 0 branch'],
    'identities': ['ARM FIRED I1 sum x² = R², sum |∇x|² = 2 on a generic surface in S³', 'ARM FIRED I2 −Δ sin(y/R) = (2/R²) sin(y/R)', 'ARM FIRED I3 the trivialization carries sin(y/R) to x_p/R', 'ARM FIRED I4 rotation field: Killing, tangent to S³, equals x_p ν on x4 = 0', 'ARM FIRED I5 great S² in Sⁿ, n = 3..8: tilt 2/R² = Jacobi term for every n; Ricci floor meets it only at n = 3', 'ARM FIRED I6 3/R² on S³, and n/R² = n(n−1)/(2R²) only at n = 3', "ARM FIRED I7 the tube's edge curvature tan(W/R)/R balances its area (Gauss-Bonnet, χ = 0)", "ARM FIRED I8 φ₀u₀ is an untwisted 2/R² mode, odd about the cone, with u₀'s intensity", 'ARM FIRED I9 second variation: exact area density, no first-order term, t² term (|∇φ|² − 2φ²/R²)/2', 'PASS I1 sum x² = R², sum |∇x|² = 2 on a generic surface in S³', 'PASS I2 −Δ sin(y/R) = (2/R²) sin(y/R)', 'PASS I3 the trivialization carries sin(y/R) to x_p/R', 'PASS I4 rotation field: Killing, tangent to S³, equals x_p ν on x4 = 0', 'PASS I5 great S² in Sⁿ, n = 3..8: tilt 2/R² = Jacobi term for every n; Ricci floor meets it only at n = 3', 'PASS I6 3/R² on S³, and n/R² = n(n−1)/(2R²) only at n = 3', "PASS I7 the tube's edge curvature tan(W/R)/R balances its area (Gauss-Bonnet, χ = 0)", "PASS I8 φ₀u₀ is an untwisted 2/R² mode, odd about the cone, with u₀'s intensity", 'PASS I9 second variation: exact area density, no first-order term, t² term (|∇φ|² − 2φ²/R²)/2'],
    'lift_trace': ['ARM FIRED L1 continuous and closes after one traversal [one-piece]', 'ARM FIRED L1 continuous and closes after one traversal [seam]', 'ARM FIRED L2 passes N once and S once [one-piece]', 'ARM FIRED L3 passes from L to −L and back, once at each pole [one-piece]', "ARM FIRED L4 the four stretches match §VII's table [seam]", "ARM FIRED L4 the four stretches match §VII's table [shift]", 'ARM FIRED L5 bounds the complementary lune; with −I, two great circles [shift]', 'PASS L1 continuous and closes after one traversal', 'PASS L2 passes N once and S once', 'PASS L3 passes from L to −L and back, once at each pole', "PASS L4 the four stretches match §VII's table", 'PASS L5 bounds the complementary lune; with −I, two great circles'],
    'bent_carrier': ['ARM FIRED B1 the lune in Fermi coordinates: 0 ≤ s ≤ π, |t| ≤ W, boundary tan|t| = tan W sin s [sin-boundary]', 'ARM FIRED B2 f lies on S³ [tilted-pole]', "ARM FIRED B3 isometric: the pullback metric is the lune's round metric [speed]", 'ARM FIRED B4 the pinch: N and S map to one point [short]', "ARM FIRED B5 embeds M(W): bi-Lipschitz from M(W)'s own metric [twice]", 'ARM FIRED B6 det A = 0 on the smooth locus [twist]', 'ARM FIRED B7 bent: H = κ/cos t with κ = √3, so never minimal [geodesic]', 'ARM FIRED B8 two-sided: every meridian loop returns the normal unchanged through the pinch [geodesic]', 'ARM FIRED B9 the pinch is planar: its two sectors lie in one plane [triangle]', 'PASS B1 the lune in Fermi coordinates: 0 ≤ s ≤ π, |t| ≤ W, boundary tan|t| = tan W sin s', 'PASS B2 f lies on S³', "PASS B3 isometric: the pullback metric is the lune's round metric", 'PASS B4 the pinch: N and S map to one point', "PASS B5 embeds M(W): bi-Lipschitz from M(W)'s own metric", 'PASS B6 det A = 0 on the smooth locus', 'PASS B7 bent: H = κ/cos t with κ = √3, so never minimal', 'PASS B8 two-sided: every meridian loop returns the normal unchanged through the pinch', 'PASS B9 the pinch is planar: its two sectors lie in one plane'],
    'bent_projective': ['ARM FIRED C1 f lies on S³ [off-sphere]', "ARM FIRED C2 isometric: the pullback metric is the lune's round metric [speed]", 'ARM FIRED C3 the pinch: every meridian runs from x to −x [moving-apex]', "ARM FIRED C4 embeds M(W) in RP³: bi-Lipschitz from M(W)'s own metric [twice]", 'ARM FIRED C5 det A = 0 on the smooth locus [twist]', 'ARM FIRED C6 bent: H = κ/sin θ with κ = cot ρ, so never minimal [great-arc]', 'ARM FIRED C7 one-sided: every meridian loop returns the normal reversed through −I [no-deck]', 'ARM FIRED C8 the pinch is not planar: its two sectors span T_x S³ [great-arc]', "ARM FIRED C9 the edge's lift: embedded, closed, through x and −x once each [one-piece]", 'PASS C1 f lies on S³', "PASS C2 isometric: the pullback metric is the lune's round metric", 'PASS C3 the pinch: every meridian runs from x to −x', "PASS C4 embeds M(W) in RP³: bi-Lipschitz from M(W)'s own metric", 'PASS C5 det A = 0 on the smooth locus', 'PASS C6 bent: H = κ/sin θ with κ = cot ρ, so never minimal', 'PASS C7 one-sided: every meridian loop returns the normal reversed through −I', 'PASS C8 the pinch is not planar: its two sectors span T_x S³', "PASS C9 the edge's lift: embedded, closed, through x and −x once each"],
    'seed_laps': ['ARM FIRED V1 on M(W) the bottom is 0 and 2/R² is the first positive level, simple, carried by the tilt x_p', 'ARM FIRED V2 the first variation along each profile matches (3/(4WR³)) ∫ (sin² − 2cos²)(s/R) V ds', 'ARM FIRED V3 turning the lap rigidly leaves the level at 2/R²', 'ARM FIRED V4 for each t a bracket in τ changes the sign of λ₁ − 2/R², each end at least 10 times its error', 'ARM FIRED V5 at each root 2/R² is the first positive level and simple', 'ARM FIRED V6 at each root the moved lap is curved, the fixed lap geodesic', 'ARM FIRED V7 at each root the 2/R² mode is not a rigid tilt', 'ARM FIRED V8 every band computed is embedded in RP²', 'PASS V1 on M(W) the bottom is 0 and 2/R² is the first positive level, simple, carried by the tilt x_p', 'PASS V2 the first variation along each profile matches (3/(4WR³)) ∫ (sin² − 2cos²)(s/R) V ds', 'PASS V3 turning the lap rigidly leaves the level at 2/R²', 'PASS V4 for each t a bracket in τ changes the sign of λ₁ − 2/R², each end at least 10 times its error', 'PASS V5 at each root 2/R² is the first positive level and simple', 'PASS V6 at each root the moved lap is curved, the fixed lap geodesic', 'PASS V7 at each root the 2/R² mode is not a rigid tilt', 'PASS V8 every band computed is embedded in RP²'],
}

HEADER = [r"\*\*Type:\*\* ", r"\*\*State:\*\* ", r"\*\*Status \(\d{4}-\d{2}-\d{2}\):\*\* ", r"\*\*Summary:\*\* ",
          r"\*\*Inputs:\*\* ", r"\*\*Parent:\*\* ", r"\*\*Frozen:\*\* \d{4}-\d{2}-\d{2} "]
FROZEN = re.compile(r"^\*Registered .*?^  - Unresolved:[^\n]*", re.M | re.S)
SCOPE_NOTES = {  # page -> {section anchor: how many dated scope notes (or the ruling's pointer) linking this page it holds}
    WF + "/postulate-bridge.md": {"top": 1, "what-was-tried-and-why-it-failed": 1, "route-1": 1, "a-sampler-reading": 1,
                                  "dynamical-direction": 1, "variational-reading": 1},
    WF + "/sampler-first-test.md": {"10-scope-and-non-claims": 1},
    WF + "/variational-score-to-sample.md": {"3-phase-domain-and-möbius-sign": 1},
    WF + "/plato-twist.md": {"iv-what-the-computed-route-changes": 1},
    WF + "/scaling-law-uniqueness.md": {"proof-the-schur-separation": 2, "linear-readout-two-routes-and-a-no-go": 1},
}
INBOUND = {  # page -> the link into projective-carrier.md it must carry
    WF.rsplit("/", 1)[0] + "/README.md": "files/projective-carrier.md",
    WF + "/postulate-bridge.md": "projective-carrier.md",
    "files/cosmos/files/cosmological-constant.md": "../../framework/files/working/files/projective-carrier.md",
}
PUBLIC = {  # canonical page -> {section anchor: links into this page that its reworded sign, seam or placement text carries}
    "files/framework/README.md": {"one-shape": 2, "surface": 1, "the-two-seams": 1},
    "files/spectrum/files/the-waltz.md": {"i-the-two-partners": 1},
    "files/spectrum/files/mass-spectrum.md": {"5-the-vertex-and-the-twist": 1},
    "files/framework/files/bedrock/README.md": {"postulate-bridge": 1},
}


def spans(t):
    return re.findall(r"\$`(.*?)`\$", t, re.S) + re.findall(r"```math\n(.*?)```", t, re.S)


def lint(t):
    """metadata-lint over the working layer, with t standing in for the page."""
    tmp = None
    if t != open(PAGE, encoding="utf-8").read():
        tmp = os.path.join(REPO, WF, "projective-carrier.gate-arm.md")
        open(tmp, "w", encoding="utf-8").write(t)
    try:
        out = subprocess.run([sys.executable, os.path.join(REPO, WF, "scripts/metadata-lint.py")], cwd=REPO, text=True,
                             capture_output=True, check=False).stdout
    finally:
        if tmp:
            os.remove(tmp)
    m = re.search(r"(\d+) FAIL, (\d+) WARN", out)
    return (bool(m) and m.groups() == ("0", "0")), (m.group(0) if m else out[-120:])


def tracked(folder):
    """The folder's files as git would commit them: tracked, or untracked and not ignored; SHA256SUMS excluded."""
    rel = os.path.relpath(folder, REPO)
    names = sh(["git", "ls-files", "--cached", "--others", "--exclude-standard", "--", rel], REPO).split()
    return sorted(os.path.relpath(os.path.join(REPO, n), folder) for n in names if not n.endswith("/SHA256SUMS"))


def checks(t, ctx):
    r = {}
    outs, files, manifest = ctx["outs"], ctx["files"], ctx["manifest"]
    read = lambda rel: ctx["sources"][rel] if rel in ctx["sources"] else src(rel)
    bare = re.sub(r"```math\n.*?```", "", re.sub(r"\$`.*?`\$", "", t, flags=re.S), flags=re.S)
    bad = ["em-dash"] * ("\u2014" in t) + ["bare $"] * ("$" in bare) + re.findall(r"\[[^\]]*\$`[^\]]*\]\(", t) + re.findall(r"\b(?:F1|F2|F3|F4|redline)\b", t)
    r["P1 hygiene: no em-dash, bare dollar, math in link text or unit attribution"] = (not bad, bad)
    lines = t.split("\n")
    i = lines.index("# The Projective Carrier")
    got = [l for l in lines[i + 1:i + 12] if l.startswith("**")]
    order = len(got) == len(HEADER) and all(re.match(h, g) for g, h in zip(got, HEADER))
    lint_ok, lint_info = lint(t)
    r["P2 header in schema order, Frozen included; metadata-lint 0 FAIL 0 WARN"] = (order and lint_ok, (got[:2], lint_info))
    bad = []
    for tgt in re.findall(r"\]\(([^)\s]+)\)", t):
        if tgt.startswith("http") or tgt.startswith("/files/") or tgt == "#top":
            continue
        p, _, a = tgt.partition("#")
        if p.startswith("scripts/projective-carrier/"):
            if not os.path.exists(os.path.join(SCRIPTS, p[len("scripts/projective-carrier/"):])):
                bad.append(tgt)
            continue
        rel = os.path.normpath(os.path.join(WF, p))
        if not os.path.exists(os.path.join(REPO, rel)):
            bad.append(tgt)
        elif a:
            text = read(rel)
            local = a in sections(text)
            ok = (local and a in live_ids(rel)) if text == at_head(rel) else local
            if not ok:
                bad.append(tgt)
    for tgt in re.findall(r"`((?:\.\./)*[\w./-]+\.md)`", t):
        if not os.path.exists(os.path.join(REPO, os.path.normpath(os.path.join(WF, tgt)))):
            bad.append(tgt)
    r["P3 every link resolves; each anchor is a heading id of the committed-to-be page, live on GitHub where unchanged"] = (not bad, bad)
    gh = subprocess.run(["gh", "api", "markdown", "-f", "mode=gfm", "-f", "context=dmobius3/mode-identity-theory", "-F", "text=@-"],
                        input=t, capture_output=True, text=True, check=True).stdout
    n = len(re.findall(r"<math-renderer", gh))
    r["P4 GitHub renders every math span"] = (n == len(spans(t)) and "$`" not in html.unescape(re.sub(r"<[^>]+>", " ", gh)), (n, len(spans(t))))
    budget = sum(1 + s.count("{") for s in spans(t))
    r["P5 math budget under 2000"] = (budget < 2000, budget)
    miss = [q[:40] for q, rel in QUOTES if q not in t or q not in read(rel)]
    r["P6 every quoted phrase is verbatim on its source page"] = (not miss, miss)
    table = re.search(r"\| \$`\\lambda_0 R\^2`\$ \|(.*)\|", t).group(1).split("|")
    got = [x.strip() for x in table]
    rec = {f"{float(l.split()[0]):.2f}": l.split()[3] for l in outs["smooth_band.out"].split("\n") if re.match(r"^\d\.\d\d ", l)}
    want = [rec[w] for w in ("0.25", "0.50", "1.00", "1.40", "1.50")]
    r["P7 the tube table matches smooth_band.out"] = (got == want, (got, want))
    bad = []
    for name, lines_exp in EXPECTED.items():
        o = outs[f"{name}.out"]
        have = sorted(l for l in o.split("\n") if l.startswith("PASS ") or l.startswith("ARM FIRED "))
        if f"`{name}.py`" not in t or have != lines_exp or re.search(r"^(FAIL|ARM SILENT)", o, re.M):
            bad.append(name)
    r["P8 each named script's record carries exactly its expected checks and arms"] = (not bad, bad)
    known = {q for q, _ in QUOTES}
    prose = re.sub(r'<a id="[^"]*"></a>', "", t)  # an anchor's id is not a quotation
    loose = [q[:40] for q in re.findall(r'"([^"\n]{12,})"', prose) if q not in known]
    r["P9 every quotation on the page is on the verified list"] = (not loose, loose)
    bad = []
    link_re = re.compile(r"\]\(([^)#\s]+\.md)#([^)\s]+)\)")
    for para in t.split("\n"):
        links = list(link_re.finditer(para))
        for k, m in enumerate(links):
            nxt = links[k + 1].start() if k + 1 < len(links) else len(para)
            q = re.match(r'[^"\n]{0,60}?"([^"\n]{12,})"', para[m.end():nxt])
            if not q:
                continue
            md = read(os.path.normpath(os.path.join(WF, m.group(1))))
            sp = sections(md).get(m.group(2))
            if sp is None or q.group(1) not in md[sp[0]:sp[1]]:
                bad.append((m.group(2), q.group(1)[:40]))
    r["P10 a quotation that directly follows a section link lies in that section"] = (not bad, bad)
    fz = re.search(r"^\*\*Frozen:\*\* (\d{4}-\d{2}-\d{2}) .*SHA-256 `([0-9a-f]{64})`", t, re.M)
    span = FROZEN.search(t)
    reg = re.search(r"^\*Registered (\d{4}-\d{2}-\d{2})", t, re.M)
    ok = bool(fz and span and reg) and fz.group(1) == reg.group(1) and hashlib.sha256(span.group(0).encode("utf-8")).hexdigest() == fz.group(2)
    r["P11 the Frozen entry's SHA-256 and date match §IX's registered span"] = (ok, fz.group(1) if fz else None)
    listed = {}
    for l in manifest.strip().split("\n"):
        h, _, nm = l.partition("  ")
        listed[nm] = h
    ok = sorted(listed) == sorted(files) and all(hashlib.sha256(files[nm]).hexdigest() == h for nm, h in listed.items() if nm in files)
    r["P12 SHA256SUMS lists exactly the folder's other files, each hash matching"] = (ok, sorted(set(listed) ^ set(files)))
    bad = []
    for rel, target in INBOUND.items():
        links = re.findall(r"\]\(" + re.escape(target) + r"(?:#([^)\s]+))?\)", read(rel))
        if not links or os.path.normpath(os.path.join(os.path.dirname(rel), target)) != SELF_REL:
            bad.append(rel)
        for a in links:
            if a and a not in sections(t):
                bad.append((rel, a))
    for rel, want in SCOPE_NOTES.items():
        text = read(rel)
        spans_ = sections(text)
        for a, n in want.items():
            sp = (0, text.index("\n## ")) if a == "top" else spans_.get(a)
            body = text[sp[0]:sp[1]] if sp else ""
            notes = [p for p in body.split("\n\n") if re.match(r"\*\*(Scope under the ruling|Where the carrier sits) \(", p.strip())
                     and "](projective-carrier.md)" in p]
            if len(notes) < n:
                bad.append((rel.split("/")[-1], a, len(notes)))
    for rel, want in PUBLIC.items():
        text = read(rel)
        spans_ = sections(text)
        for a, n in want.items():
            sp = spans_.get(a)
            body = text[sp[0]:sp[1]] if sp else ""
            got = [m for m in re.finditer(r"\]\(([^)#\s]+)(?:#([^)\s]+))?\)", body)
                   if os.path.normpath(os.path.join(os.path.dirname(rel), m.group(1))) == SELF_REL]
            if len(got) < n or any(m.group(2) and m.group(2) not in sections(t) for m in got):
                bad.append((rel.split("/")[-1], a, len(got)))
    row = next((l for l in read(WF + "/claim-ledger.md").split("\n") if l.startswith("| Boundary-mode uniformity")), "")
    if "](projective-carrier.md)" not in row:
        bad.append(("claim-ledger.md", "uniformity row"))
    r["P13 the pages that point into this page carry their links and dated scope notes"] = (not bad, bad)
    return r


def context():
    return {"outs": {f"{n}.out": open(os.path.join(SCRIPTS, f"{n}.out"), encoding="utf-8").read() for n in EXPECTED},
            "files": {nm: open(os.path.join(SCRIPTS, nm), "rb").read() for nm in tracked(SCRIPTS)},
            "manifest": open(os.path.join(SCRIPTS, "SHA256SUMS"), encoding="utf-8").read(),
            "sources": {}}


def main():
    t = open(PAGE, encoding="utf-8").read()
    ctx = context()
    res = checks(t, ctx)
    for k, (ok, info) in res.items():
        print(("PASS " if ok else "FAIL ") + k + ("" if ok else f"  {info}"))
    green = all(ok for ok, _ in res.values())
    if "--arms" not in sys.argv:
        return 0 if green else 1
    assert green, "arms need a green parent"

    def with_(key, **kw):
        c = {k: (dict(v) if isinstance(v, dict) else v) for k, v in ctx.items()}
        for k, v in kw.items():
            if k == "out":
                name, new = v
                c["outs"][name] = new
            elif k == "file":
                name, new = v
                c["files"][name] = new
            elif k == "source":
                rel, new = v
                c["sources"][rel] = new
            else:
                c[k] = v
        return c

    bc = ctx["outs"]["bent_carrier.out"]
    first_pass = next(l for l in bc.split("\n") if l.startswith("PASS "))
    lam = "files/cosmos/files/cosmological-constant.md"
    bridge = WF + "/postulate-bridge.md"
    waltz = "files/spectrum/files/the-waltz.md"
    arms = [
        ("P1", t.replace("The premise is adopted by ruling", "The premise is adopted \u2014 by ruling", 1), ctx),
        ("P2", t.replace("**State:** Active", "**State:** Running", 1), ctx),
        ("P3", t.replace("postulate-bridge.md#route-1", "postulate-bridge.md#route-one", 1), ctx),
        ("P3", t, with_("P3", source=(bridge, src(bridge).replace('<a id="route-1"></a>', '<a id="route-one"></a>', 1)))),
        ("P4", t.replace("$`\\mathbb{RP}^3 = S^3/\\{\\pm I\\}`$, the one space form", "$`\\mathbb{RP}^3 = S^3/\\{\\pm I\\}$, the one space form", 1), ctx),
        ("P5", t + "\n" + "$`" + "{" * 2100 + "}" * 2100 + "`$\n", ctx),
        ("P6", t.replace("they must not be merged.", "they must never be merged.", 1), ctx),
        ("P7", t.replace("| 1.0212 | 1.0891 |", "| 1.0213 | 1.0891 |", 1), ctx),
        ("P8", t, with_("P8", out=("bent_carrier.out", bc.replace(first_pass + "\n", "", 1)))),
        ("P8", t, with_("P8", out=("bent_carrier.out", bc + "PASS B10 an unexpected check\n"))),
        ("P9", t.replace("The dance runs on two distinct seams", "The dance runs on two separate seams", 1), ctx),
        ("P10", t.replace("#iii-the-spectral-seed) \"The holonomy selects", "#ii-the-geometry) \"The holonomy selects", 1), ctx),
        ("P11", t.replace("- **Tolerance.** The extrapolated bottom", "- **Tolerance.** The extrapolated  bottom", 1), ctx),
        ("P12", t, with_("P12", file=("lift_trace.py", ctx["files"]["lift_trace.py"] + b"\n"))),
        ("P12", t, with_("P12", manifest=ctx["manifest"] + "0" * 64 + "  stray.txt\n")),
        ("P13", t, with_("P13", source=(lam, src(lam).replace("projective-carrier.md#ii-lemma-1", "projective-carrier.md#ii-lemma-one", 1)))),
        ("P13", t, with_("P13", source=(bridge, re.sub(r"\n\n\*\*Scope under the ruling \([^)]*\)\.\*\* Both walls stand\.[^\n]*", "", src(bridge), count=1)))),
        ("P13", t, with_("P13", source=(waltz, src(waltz).replace("working/files/projective-carrier.md", "working/files/plato-twist.md", 1)))),
    ]
    rc = 0
    for key, bt, bctx in arms:
        assert (bt, bctx) != (t, ctx), key
        name = next(k for k in res if k.startswith(key + " "))
        fired = not checks(bt, bctx)[name][0]
        print(("ARM FIRED " if fired else "ARM SILENT ") + name)
        rc |= 0 if fired else 1
    return rc


if __name__ == "__main__":
    sys.exit(main())
