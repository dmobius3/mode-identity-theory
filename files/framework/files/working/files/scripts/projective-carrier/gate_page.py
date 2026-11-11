#!/usr/bin/env python3
"""Standing gate for projective-carrier.md and for the three pages that hold text moved from it, carrier-inventory.md
(its section X), carrier-proofs.md (four proofs) and carrier-decisions.md (its section XI from the sub-decisions on).
No args: the checks.  --arms: each check must fail on a planted defect, parent green first.

Run it from a checkout of this repository at origin/main, with network access and an authenticated gh CLI. P3 reads
anchor ids from GitHub's rendering of each linked page at HEAD, P4 renders each of the four pages through
`gh api markdown`, and a missing tool, a failed fetch or a checkout off origin/main stops the run with an error:
nothing is skipped. Every check reads the working tree, the state about to be committed. P3 takes an anchor from
GitHub's ids only where a page's bytes match HEAD, and there the local heading rule must agree with it; a page with
uncommitted edits is checked by the local rule alone. P1, P3 to P6, P9 and P10 run on each of the four pages; P2, P7,
P8, P11 to P14 and P22 read projective-carrier.md and the pages that point into it; P15 to P21 hold the four pages
together. The pages quote other pages, so rerun this gate whenever one of them changes. A commit that changes a quoted
sentence, such as a scope note, updates or dates the matching entry of carrier-inventory.md in the same commit. Each
quotation is listed with the pages that carry it, and is checked on each."""
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


QUOTES = [  # (exact bytes, the corpus page that must contain them at HEAD, the pages of FAMILY that carry them)
    ("are antipodal maps on different spheres serving different purposes, and they must not be merged.", f"{WF}/sampler-first-test.md", ('page',)),
    ("the band's $`\\mathbb{Z}_2`$ cannot be a $`2I`$-equivariant datum", f"{WF}/postulate-bridge.md", ('page', 'inventory')),
    ("cannot be identified with any $`2I`$-datum", f"{WF}/postulate-bridge.md", ('inventory',)),
    ("The covering geometry constrains, but does not by itself fix, the extension", "files/framework/files/bedrock/files/first-eigenvalue.md", ('page',)),
    ("the edge-identified quotient of a totally geodesic covering great-$`S^2`$ band in $`S^3`$", "files/cosmos/files/cosmological-constant.md", ('inventory',)),
    ("transverse, not restrictive", f"{WF}/postulate-bridge.md", ('page', 'inventory')),
    ("time is the boundary of a non-orientable surface embedded in a closed three-space", "files/framework/README.md", ('page',)),
    ("The twists and identifications live in that built structure", "files/framework/README.md", ('page',)),
    ("and not the Möbius orientation sign of One Shape", "files/framework/README.md", ('inventory',)),
    ("The Möbius sign flip and the central $`-I`$ of $`2I`$ are two distinct $`Z_2`$'s", "files/framework/README.md", ('inventory',)),
    ("the framework does not treat them as interchangeable", "README.md", ('inventory',)),
    ("an embedded spectral carrier", "files/cosmos/files/cosmological-constant.md", ('inventory',)),
    ("The dance runs on two distinct seams", "files/spectrum/files/the-waltz.md", ('inventory',)),
    ("the orientation $`\\mathbb{Z}_2`$ is not a $`2I`$-equivariant datum", f"{WF}/postulate-bridge.md", ('inventory',)),
    ("$`\\mathbb Z_2^{\\text{Möbius}} \\neq \\mathbb Z_2^{\\text{centre}}`$ as identified structures", f"{WF}/postulate-bridge.md", ('inventory',)),
    ("the two $`\\mathbb{Z}_2`$ structures remain distinct", f"{WF}/postulate-bridge.md", ('inventory',)),
    ("canonically trivial", f"{WF}/postulate-bridge.md", ('page', 'inventory')),
    ("a circle as the edge of a Möbius band embedded in $`S^3`$", f"{WF}/postulate-bridge.md", ('inventory',)),
    ("postulate embedding", f"{WF}/postulate-bridge.md", ('page', 'inventory', 'decisions')),
    ("The zero-excitation equilibrium cannot be the totally geodesic embedding", f"{WF}/postulate-bridge.md", ('page', 'inventory')),
    ("The topology excludes the zero-bending configuration", f"{WF}/postulate-bridge.md", ('inventory',)),
    ("The central $`2I`$ sign and the Möbius normal sign are independent structures", f"{WF}/sampler-first-test.md", ('inventory',)),
    ("$`\\mathcal L`$'s $`\\mathbb Z_2`$ cannot be a $`2I`$ character", f"{WF}/sampler-first-test.md", ('inventory',)),
    ("the two $`\\mathbb{Z}_2`$ structures are different objects", f"{WF}/variational-score-to-sample.md", ('inventory',)),
    ("not the Möbius orientation $`Z_2`$, which the framework keeps distinct from that split", f"{WF}/plato-twist.md", ('inventory',)),
    ("stays distinct both from the base edge $`Z_2`$ above and from the central $`-I`$ inside the lifted $`Z_4`$", "files/spectrum/files/mass-spectrum.md", ('inventory',)),
    ("group each block carries", f"{WF}/scaling-law-uniqueness.md", ('inventory',)),
    ("The postulate embedding must be a critical point of the independently motivated functional whose second variation is nonnegative on every admissible variation of the declared class", f"{WF}/postulate-bridge.md", ('page',)),
    ("A restriction on the admissible variations counts only when the postulate motivates it and it is declared before the computation, never because it rescues a candidate.", f"{WF}/postulate-bridge.md", ('page',)),
    ("only after a further mechanism selects the realized member", f"{WF}/postulate-bridge.md", ('page',)),
    ("a singular surface model", "files/framework/files/bedrock/README.md", ('page', 'inventory')),
    ("the extension selection", f"{WF}/scaling-law-uniqueness.md", ('inventory', 'decisions')),
    ("spectrally an orientable object", "files/framework/files/bedrock/files/first-eigenvalue.md", ('page', 'inventory', 'decisions')),
    ("the one quantity in the model that the intrinsic geometry leaves free", "files/framework/files/bedrock/files/first-eigenvalue.md", ('decisions',)),
    ("the framework's default", f"{WF}/scaling-law-uniqueness.md", ('inventory', 'decisions')),
    ("an Euler-Lagrange matching equation", f"{WF}/postulate-bridge.md", ('decisions',)),
    ("assumed as an inclusion by hand", f"{WF}/postulate-bridge.md", ('decisions',)),
    ("the Friedrichs realization is spectrally an orientable object, a Neumann lune", "files/framework/files/bedrock/files/first-eigenvalue.md", ('page',)),
    ("a singular surface model, not a smooth totally geodesic submanifold of $`S^3/2I`$", "files/framework/files/bedrock/README.md", ('inventory',)),
    ("not by seating the Möbius band inside $`S^3/2I`$", "files/framework/files/bedrock/README.md", ('inventory',)),
    ("The deeper obstruction", f"{WF}/postulate-bridge.md", ('inventory',)),
    ("The band lives upstairs on a great $`S^2 \\subset S^3`$", f"{WF}/postulate-bridge.md", ('inventory',)),
    ("compose only if the surface is group-stable, and it is not", f"{WF}/postulate-bridge.md", ('inventory',)),
    ("left translation by any non-central element moves the defining $`3`$-plane", f"{WF}/postulate-bridge.md", ('inventory',)),
    ("the band does not descend (the deeper obstruction)", f"{WF}/postulate-bridge.md", ('inventory',)),
    ("rules out descent of the band to $`X`$ as a $`2I`$-stable submanifold", f"{WF}/postulate-bridge.md", ('inventory',)),
    ("the deck element $`-1`$ never stabilizes an admissible band", "files/framework/files/working/README.md", ('inventory',)),
    ("Tier 2's totally geodesic candidate has been removed: it is topologically unavailable to a smooth Möbius band", f"{WF}/postulate-bridge.md", ('inventory',)),
    ("the transverse-not-restrictive result as the residue", f"{WF}/postulate-bridge.md", ('inventory',)),
    ("should not be rescued by modifying the band", f"{WF}/sampler-first-test.md", ('inventory',)),
    ("of which the Möbius carrier is the edge-identified quotient", "files/cosmos/files/cosmological-constant.md", ('decisions',)),
    ("an exact same-mode identity", f"{WF}/scaling-law-uniqueness.md", ('page',)),
    ("Excited modes ($`m > 0`$) on the Möbius surface bend the embedding", "files/spectrum/files/the-waltz.md", ('page', 'decisions')),
    ("the extension question governs only the ground state, which the factorization never samples", f"{WF}/scaling-law-uniqueness.md", ('decisions',)),
    ("even had $`S = \\{\\pm 1\\}`$ been achievable", f"{WF}/sampler-first-test.md", ('inventory',)),
    ("nothing would have been resolved at sixty either", f"{WF}/sampler-first-test.md", ('inventory',)),
    ("belong to a named operator on the embedded band's induced metric rather than being imported from the intrinsic conic pillar", f"{WF}/postulate-bridge.md", ('inventory',)),
    ("This decouples the factorization from the extension selection", f"{WF}/scaling-law-uniqueness.md", ('inventory',)),
    ("bridging extension (not Friedrichs; see §II)", f"{WF}/cone-point-coherence.md", ('inventory',)),
    ("the holonomy picks out the twisted sector", "files/cosmos/files/cosmological-constant.md", ('inventory',)),
    ("The holonomy selects the twisted sector in which the first positive level is identified", "files/cosmos/files/cosmological-constant.md", ('inventory',)),
    ("The anti-periodic flip acts per lap", "files/framework/README.md", ('inventory',)),
    ("The paper's model is intrinsic, and the paper places it in no three-dimensional space", "files/cosmos/files/black-hole.md", ('page',)),
    ("These are different operations doing different jobs", "files/framework/README.md", ('inventory',)),
    ("The two seams share one step without merging", "files/framework/README.md", ('inventory',)),
    ("the orientation sign and the central $`-I`$ are carried by one loop", "files/framework/README.md", ('inventory',)),
    ("the carrier's physical domain is $`\\mathbb{RP}^3`$, the layer where it embeds", "files/framework/README.md", ('inventory',)),
    ("enters separately", "files/framework/files/bedrock/README.md", ('inventory',)),
    ("The quotient's central stage reaches the band itself", "files/framework/files/bedrock/README.md", ('inventory',)),
    ("The carrier embeds unbent in the projective layer", "files/framework/files/bedrock/README.md", ('inventory',)),
    ("the resulting projective three-space admits an unbent Möbius surface with a single continuous edge", "README.md", ('inventory',)),
    ("includes that same identification of opposite points as an initial step", "README.md", ('inventory',)),
    ("The postulate embeds a non-orientable carrier, unbent, in its central quotient", "files/cosmos/files/cosmological-constant.md", ('inventory',)),
]

EXPECTED = {  # each record's PASS and ARM FIRED lines, exactly
    'smooth_band': ['ARM FIRED S1 RP² eigenfunctions at λ = 2 exactly', 'ARM FIRED S2 first twisted level below 2 at each sampled width', 'ARM FIRED S3 increasing across the sampled widths, within 2e-3 of 2 at W = 1.55', 'ARM FIRED S4 at each sampled width the k = ±1 branch lies below the k = 0 branch', 'PASS S1 RP² eigenfunctions at λ = 2 exactly', 'PASS S2 first twisted level below 2 at each sampled width', 'PASS S3 increasing across the sampled widths, within 2e-3 of 2 at W = 1.55', 'PASS S4 at each sampled width the k = ±1 branch lies below the k = 0 branch'],
    'identities': ['ARM FIRED I1 sum x² = R², sum |∇x|² = 2 on a generic surface in S³', 'ARM FIRED I2 −Δ sin(y/R) = (2/R²) sin(y/R)', 'ARM FIRED I3 the trivialization carries sin(y/R) to x_p/R', 'ARM FIRED I4 rotation field: Killing, tangent to S³, equals x_p ν on x4 = 0', 'ARM FIRED I5 great S² in Sⁿ, n = 3..8: tilt 2/R² = Jacobi term for every n; Ricci floor meets it only at n = 3', 'ARM FIRED I6 3/R² on S³, and n/R² = n(n−1)/(2R²) only at n = 3', "ARM FIRED I7 the tube's edge curvature tan(W/R)/R balances its area (Gauss-Bonnet, χ = 0)", "ARM FIRED I8 φ₀u₀ is an untwisted 2/R² mode, odd about the cone, with u₀'s intensity", 'ARM FIRED I9 second variation: exact area density, no first-order term, t² term (|∇φ|² − 2φ²/R²)/2', 'PASS I1 sum x² = R², sum |∇x|² = 2 on a generic surface in S³', 'PASS I2 −Δ sin(y/R) = (2/R²) sin(y/R)', 'PASS I3 the trivialization carries sin(y/R) to x_p/R', 'PASS I4 rotation field: Killing, tangent to S³, equals x_p ν on x4 = 0', 'PASS I5 great S² in Sⁿ, n = 3..8: tilt 2/R² = Jacobi term for every n; Ricci floor meets it only at n = 3', 'PASS I6 3/R² on S³, and n/R² = n(n−1)/(2R²) only at n = 3', "PASS I7 the tube's edge curvature tan(W/R)/R balances its area (Gauss-Bonnet, χ = 0)", "PASS I8 φ₀u₀ is an untwisted 2/R² mode, odd about the cone, with u₀'s intensity", 'PASS I9 second variation: exact area density, no first-order term, t² term (|∇φ|² − 2φ²/R²)/2'],
    'lift_trace': ['ARM FIRED L1 continuous and closes after one traversal [one-piece]', 'ARM FIRED L1 continuous and closes after one traversal [seam]', 'ARM FIRED L2 passes N once and S once [one-piece]', 'ARM FIRED L3 passes from L to −L and back, once at each pole [one-piece]', "ARM FIRED L4 the four stretches match §VII's table [seam]", "ARM FIRED L4 the four stretches match §VII's table [shift]", 'ARM FIRED L5 bounds the complementary lune; with −I, two great circles [shift]', 'PASS L1 continuous and closes after one traversal', 'PASS L2 passes N once and S once', 'PASS L3 passes from L to −L and back, once at each pole', "PASS L4 the four stretches match §VII's table", 'PASS L5 bounds the complementary lune; with −I, two great circles'],
    'bent_carrier': ['ARM FIRED B1 the lune in Fermi coordinates: 0 ≤ s ≤ π, |t| ≤ W, boundary tan|t| = tan W sin s [sin-boundary]', 'ARM FIRED B2 f lies on S³ [tilted-pole]', "ARM FIRED B3 isometric: the pullback metric is the lune's round metric [speed]", 'ARM FIRED B4 the pinch: N and S map to one point [short]', "ARM FIRED B5 embeds M(W): bi-Lipschitz from M(W)'s own metric [twice]", 'ARM FIRED B6 det A = 0 on the smooth locus [twist]', 'ARM FIRED B7 bent: H = κ/cos t with κ = √3, so never minimal [geodesic]', 'ARM FIRED B8 two-sided: every meridian loop returns the normal unchanged through the pinch [geodesic]', 'ARM FIRED B9 the pinch is planar: its two sectors lie in one plane [triangle]', 'PASS B1 the lune in Fermi coordinates: 0 ≤ s ≤ π, |t| ≤ W, boundary tan|t| = tan W sin s', 'PASS B2 f lies on S³', "PASS B3 isometric: the pullback metric is the lune's round metric", 'PASS B4 the pinch: N and S map to one point', "PASS B5 embeds M(W): bi-Lipschitz from M(W)'s own metric", 'PASS B6 det A = 0 on the smooth locus', 'PASS B7 bent: H = κ/cos t with κ = √3, so never minimal', 'PASS B8 two-sided: every meridian loop returns the normal unchanged through the pinch', 'PASS B9 the pinch is planar: its two sectors lie in one plane'],
    'bent_projective': ['ARM FIRED C1 f lies on S³ [off-sphere]', "ARM FIRED C2 isometric: the pullback metric is the lune's round metric [speed]", 'ARM FIRED C3 the pinch: every meridian runs from x to −x [moving-apex]', "ARM FIRED C4 embeds M(W) in RP³: bi-Lipschitz from M(W)'s own metric [twice]", 'ARM FIRED C5 det A = 0 on the smooth locus [twist]', 'ARM FIRED C6 bent: H = κ/sin θ with κ = cot ρ, so never minimal [great-arc]', 'ARM FIRED C7 one-sided: every meridian loop returns the normal reversed through −I [no-deck]', 'ARM FIRED C8 the pinch is not planar: its two sectors span T_x S³ [great-arc]', "ARM FIRED C9 the edge's lift: embedded, closed, through x and −x once each [one-piece]", 'PASS C1 f lies on S³', "PASS C2 isometric: the pullback metric is the lune's round metric", 'PASS C3 the pinch: every meridian runs from x to −x', "PASS C4 embeds M(W) in RP³: bi-Lipschitz from M(W)'s own metric", 'PASS C5 det A = 0 on the smooth locus', 'PASS C6 bent: H = κ/sin θ with κ = cot ρ, so never minimal', 'PASS C7 one-sided: every meridian loop returns the normal reversed through −I', 'PASS C8 the pinch is not planar: its two sectors span T_x S³', "PASS C9 the edge's lift: embedded, closed, through x and −x once each"],
    'symmetric_edge': ['ARM FIRED E1 2I: 120 elements, closed, 31 axes [drop]', 'ARM FIRED E1 2I: 120 elements, closed, 31 axes [nudge]', 'ARM FIRED E2 Σ ∩ gΣ is the great circle G_a [wrong-circle]', 'ARM FIRED E3 axis elements keep G_a, moving a point through 2, 3 or 5 points [other-axis]', 'ARM FIRED E4 G_a and G_b cross at ±a×b at the angle between a and b [wrong-crossing]', 'ARM FIRED E5 no non-central element keeps the two-loop edge [same-axis]', 'PASS E1 2I: 120 elements, closed, 31 axes', 'PASS E2 Σ ∩ gΣ is the great circle G_a', 'PASS E3 axis elements keep G_a, moving a point through 2, 3 or 5 points', 'PASS E4 G_a and G_b cross at ±a×b at the angle between a and b', 'PASS E5 no non-central element keeps the two-loop edge'],
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


FAMILY = {  # the page, and the three pages that hold text moved from it (2026-11); all four sit in one folder
    "page": SELF_REL,
    "inventory": WF + "/carrier-inventory.md",
    "proofs": WF + "/carrier-proofs.md",
    "decisions": WF + "/carrier-decisions.md",
}
TITLES = {"inventory": "# The Projective Carrier: Scope Inventory", "proofs": "# The Projective Carrier: Supporting Proofs",
          "decisions": "# The Projective Carrier: Decision Records"}
EM = chr(0x2014)
DATE_RE = r"\d{4}-\d{2}-\d{2}"
CLAUSE = re.compile(r"\b(?:Decided|Ruled)\b[^:.]*?" + DATE_RE + r"[^:.]*(?=:)")
MOVED_PROOFS = {  # proposition -> (its heading on the proofs page, the anchor on the page of the section that states it)
    "4.1": ("Proposition 4.1", "vi-lemma-4-the-2r2-mode-is-the-bands-tilt"),
    "4.2": ("Proposition 4.2", "vi-lemma-4-the-2r2-mode-is-the-bands-tilt"),
    "6": ("Proposition 6", "ix-fixed-edge-stability"),
    "7": ("Proposition 7", "ix-fixed-edge-stability"),
}
_RENDER = {}
_LINT = {}


def spans(t):
    return re.findall(r"\$`(.*?)`\$", t, re.S) + re.findall(r"```math\n(.*?)```", t, re.S)


def render(t):
    """GitHub's rendering of t, fetched once for each distinct text."""
    if t not in _RENDER:
        _RENDER[t] = subprocess.run(["gh", "api", "markdown", "-f", "mode=gfm", "-f", "context=dmobius3/mode-identity-theory", "-F", "text=@-"],
                                    input=t, capture_output=True, text=True, check=True).stdout
    return _RENDER[t]


def lint(t):
    """metadata-lint over the working layer, with t standing in for the page."""
    if t in _LINT:
        return _LINT[t]
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
    _LINT[t] = (bool(m) and m.groups() == ("0", "0")), (m.group(0) if m else out[-120:])
    return _LINT[t]


def tracked(folder):
    """The folder's files as git would commit them: tracked, or untracked and not ignored; SHA256SUMS excluded."""
    rel = os.path.relpath(folder, REPO)
    names = sh(["git", "ls-files", "--cached", "--others", "--exclude-standard", "--", rel], REPO).split()
    return sorted(os.path.relpath(os.path.join(REPO, n), folder) for n in names if not n.endswith("/SHA256SUMS"))


def markdown_files():
    """Every markdown file git would commit, by its path from the repository's root."""
    return sorted(n for n in sh(["git", "ls-files", "-z", "--cached", "--others", "--exclude-standard", "--", "*.md"], REPO).split("\0") if n)


def section_of(md, anchor):
    sp = sections(md).get(anchor)
    return md[sp[0]:sp[1]] if sp else ""


def into_page(rel, p):
    """True when the link target p, written on the page rel, is this page at its live state: relative or rooted, or
    GitHub's main branch; a link pinned to a commit shows that commit's page and is not."""
    if p.startswith("http"):
        return not re.search(r"/blob/[0-9a-f]{7,40}/", p) and p.endswith("/blob/main/" + SELF_REL)
    dest = p.lstrip("/") if p.startswith("/") else os.path.normpath(os.path.join(os.path.dirname(rel), p))
    return dest == SELF_REL


def linked_pages(rel, line):
    # The local pages other than this one that a line of the page rel links, by their paths from the root.
    out = []
    for m in re.finditer(r"\]\(([^)#\s]+\.md)(?:#[^)\s]*)?\)", line):
        p = m.group(1)
        if p.startswith("http") or into_page(rel, p):
            continue
        dest = p.lstrip("/") if p.startswith("/") else os.path.normpath(os.path.join(os.path.dirname(rel), p))
        if os.path.isfile(os.path.join(REPO, dest)):
            out.append(dest)
    return out


def checks(fam, ctx):
    """fam: the three pages' texts by key.  Checks named for one page read fam["page"]."""
    r = {}
    t = fam["page"]
    outs, files, manifest = ctx["outs"], ctx["files"], ctx["manifest"]
    own = {rel: key for key, rel in FAMILY.items()}
    read = lambda rel: fam[own[rel]] if rel in own else (ctx["sources"][rel] if rel in ctx["sources"] else src(rel))
    bad = []
    for key, x in fam.items():
        bare = re.sub(r"```math\n.*?```", "", re.sub(r"\$`.*?`\$", "", x, flags=re.S), flags=re.S)
        found = ["em-dash"] * ("\u2014" in x) + ["bare $"] * ("$" in bare) + re.findall(r"\[[^\]]*\$`[^\]]*\]\(", x) + re.findall(r"\b(?:F1|F2|F3|F4|redline)\b", x)
        bad += [(key, f) for f in found]
    r["P1 hygiene on each of the four pages: no em-dash, bare dollar, math in link text or unit attribution"] = (not bad, bad)
    lines = t.split("\n")
    i = lines.index("# The Projective Carrier")
    got = [l for l in lines[i + 1:i + 12] if l.startswith("**")]
    order = len(got) == len(HEADER) and all(re.match(h, g) for g, h in zip(got, HEADER))
    lint_ok, lint_info = lint(t)
    r["P2 header in schema order, Frozen included; metadata-lint 0 FAIL 0 WARN"] = (order and lint_ok, (got[:2], lint_info))
    bad = []
    for key, x in fam.items():
        for tgt in re.findall(r"\]\(([^)\s]+)\)", x):
            if tgt.startswith("http") or tgt.startswith("/files/") or tgt == "#top":
                continue
            p, _, a = tgt.partition("#")
            if p.startswith("scripts/projective-carrier/"):
                if not os.path.exists(os.path.join(SCRIPTS, p[len("scripts/projective-carrier/"):])):
                    bad.append((key, tgt))
                continue
            rel = os.path.normpath(os.path.join(WF, p))
            if not os.path.exists(os.path.join(REPO, rel)):
                bad.append((key, tgt))
            elif a:
                text = read(rel)
                local = a in sections(text)
                ok = (local and a in live_ids(rel)) if text == at_head(rel) else local
                if not ok:
                    bad.append((key, tgt))
        for tgt in re.findall(r"`((?:\.\./)*[\w./-]+\.md)`", x):
            if not os.path.exists(os.path.join(REPO, os.path.normpath(os.path.join(WF, tgt)))):
                bad.append((key, tgt))
    r["P3 on each page every link resolves; each anchor is a heading id of the committed-to-be page, live on GitHub where unchanged"] = (not bad, bad)
    bad, counts = [], {}
    for key, x in fam.items():
        gh = render(x)
        n = len(re.findall(r"<math-renderer", gh))
        counts[key] = (n, len(spans(x)))
        if n != len(spans(x)) or "$`" in html.unescape(re.sub(r"<[^>]+>", " ", gh)):
            bad.append(key)
    r["P4 GitHub renders every math span on each page"] = (not bad, counts)
    budget = {key: sum(1 + s.count("{") for s in spans(x)) for key, x in fam.items()}
    r["P5 math budget under 2000 on each page"] = (all(b < 2000 for b in budget.values()), budget)
    miss = [(q[:40], c) for q, rel, carriers in QUOTES for c in carriers if q not in fam[c]] + [(q[:40], rel) for q, rel, _ in QUOTES if q not in read(rel)]
    miss += [(q[:40], "carried nowhere") for q, _, carriers in QUOTES if not carriers]
    r["P6 every quoted phrase is on each page recorded as carrying it and verbatim on its source page"] = (not miss, miss)
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
    known = {q for q, _, _ in QUOTES}
    loose = []
    for key, x in fam.items():
        prose = re.sub(r'<a id="[^"]*"></a>', "", x)  # an anchor's id is not a quotation
        loose += [(key, q[:40]) for q in re.findall(r'"([^"\n]{12,})"', prose) if q not in known]
    r["P9 every quotation on each page is on the verified list"] = (not loose, loose)
    bad = []
    link_re = re.compile(r"\]\(([^)#\s]+\.md)#([^)\s]+)\)")
    for key, x in fam.items():
        for para in x.split("\n"):
            links = list(link_re.finditer(para))
            for k, m in enumerate(links):
                nxt = links[k + 1].start() if k + 1 < len(links) else len(para)
                q = re.match(r'[^"\n]{0,60}?"([^"\n]{12,})"', para[m.end():nxt])
                if not q:
                    continue
                md = read(os.path.normpath(os.path.join(WF, m.group(1))))
                sp = sections(md).get(m.group(2))
                if sp is None or q.group(1) not in md[sp[0]:sp[1]]:
                    bad.append((key, m.group(2), q.group(1)[:40]))
    r["P10 on each page a quotation that directly follows a section link lies in that section"] = (not bad, bad)
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

    # The checks below came with the move of 2026-11: section X's body and four proofs now sit on the two other pages.
    heads = sections(t)
    bad, seen = [], 0
    for rel in ctx["markdown"]:
        if rel == SELF_REL:
            continue
        text = read(rel)
        if "projective-carrier.md" not in text:
            continue
        for m in re.finditer(r"\]\(([^)#\s]*projective-carrier\.md)#([^)\s]+)\)", text):
            p = m.group(1)
            if p.startswith("http"):
                if re.search(r"/blob/[0-9a-f]{7,40}/", p) or not p.endswith("/blob/main/" + SELF_REL):
                    continue  # a link pinned to a commit shows that commit's page; a link to another site is not this page
                dest = SELF_REL
            else:
                dest = p.lstrip("/") if p.startswith("/") else os.path.normpath(os.path.join(os.path.dirname(rel), p))
            if dest != SELF_REL:
                continue
            seen += 1
            if m.group(2) not in heads:
                bad.append((rel, m.group(2)))
    r["P14 every anchor that another page links on this page is a heading here"] = (not bad and seen >= 20, bad or seen)
    bad = []
    for prop, (heading, _) in MOVED_PROOFS.items():
        starts = [m.start() for m in re.finditer(r"^\*\*Proposition " + re.escape(prop) + r" \(", t, re.M)]
        if len(starts) != 1:
            bad.append((prop, "statement"))
            continue
        rest = t[starts[0] + 1:]
        end = re.search(r"^(\*\*Proposition |\*\*Lemma |\*\*Theorem |\*\*Corollary |## )", rest, re.M)
        seg = rest[:end.start()] if end else rest
        if not re.search(r"^\*Proof\.\* On \[[^\]]+\]\(carrier-proofs\.md#" + re.escape(slug(heading)) + r"\)", seg, re.M):
            bad.append((prop, "pointer"))
    if "](carrier-inventory.md)" not in section_of(t, "x-what-this-page-does-not-do"):
        bad.append(("section X", "link"))
    if "](carrier-decisions.md)" not in section_of(t, "xi-the-ruling"):
        bad.append(("section XI", "link"))
    r["P15 every moved block has a link where it stood: a pointer under each of the four statements, and a link in each of sections X and XI"] = (not bad, bad)
    proofs = fam["proofs"]
    psec = sections(proofs)
    pointers = re.findall(r"^\*Proof\.\* On \[[^\]]+\]\(carrier-proofs\.md#([^)\s]+)\)", t, re.M)
    want = sorted(slug(h) for h, _ in MOVED_PROOFS.values())
    bad = [a for a in pointers if a not in psec] + ([("pointers", sorted(pointers))] if sorted(pointers) != want else [])
    bad += [h for h, _ in MOVED_PROOFS.values() if not re.search(r"^## " + re.escape(h) + r"$", proofs, re.M)]
    r["P16 every proof pointer resolves to its proposition's heading on the proofs page"] = (not bad, bad)
    bad = []
    for prop, (heading, anchor) in MOVED_PROOFS.items():
        sec = section_of(proofs, slug(heading))
        if f"](projective-carrier.md#{anchor})" not in sec or anchor not in heads or not re.search(r"^\*Proof\.\*", sec, re.M):
            bad.append(prop)
    r["P17 every proof on the proofs page links back to the section that states its proposition"] = (not bad, bad)
    bad = []
    for prop, (heading, anchor) in MOVED_PROOFS.items():
        sec = section_of(proofs, slug(heading))
        m = re.search(r"\]\(projective-carrier\.md#" + re.escape(anchor) + r"\):\n(.*?)\n\*Proof\.\*", sec, re.S)
        copy = m.group(1).strip("\n") if m else ""
        if not copy.startswith(f"**Proposition {prop} (") or t.count(copy + "\n\n*Proof.* On [") != 1:
            bad.append(prop)
    r["P18 every statement copied to the proofs page equals its lines on this page"] = (not bad, bad)
    bad = [key for key in TITLES if "](projective-carrier.md" not in fam[key] or "\n**Parent:** `projective-carrier.md`\n" not in fam[key]]
    bad += [key for key in TITLES if f"]({os.path.basename(FAMILY[key])}" not in t]
    r["P19 each new page links its parent and names it as Parent, and this page links each new page"] = (not bad, bad)
    bad = []
    for key, title in TITLES.items():
        ls = fam[key].split("\n")
        got = [l for l in ls[ls.index(title) + 1:ls.index(title) + 10] if l.startswith("**")] if title in ls else []
        if len(got) != len(HEADER) - 1 or not all(re.match(h, g) for g, h in zip(got, HEADER[:-1])):
            bad.append((key, [g[:14] for g in got]))
    r["P20 each new page's header is in schema order: Type, State, Status, Summary, Inputs, Parent"] = (not bad, bad)
    dl = fam["decisions"].split("\n")
    xi = section_of(t, "xi-the-ruling")
    bad, subs = [], []
    starts = [i for i, l in enumerate(dl) if l.startswith("**What stays to decide.**")]
    ends = [i for i, l in enumerate(dl) if l.startswith("**The ledger.**")]
    if len(starts) != 1 or len(ends) != 1 or ends[0] < starts[0]:
        bad.append(("decisions page", "its sub-decisions are not between What stays to decide and The ledger"))
    else:
        for l in dl[starts[0] + 1:ends[0]]:
            m = re.match(r"^- \*\*(1[a-g]\. .+?)\.\*\*", l)
            if m:
                subs.append([m.group(1), [], l])
            elif subs and l.startswith("  - "):
                subs[-1][1].append(l[4:])
                subs[-1][2] += "\n" + l
    rows = re.findall(r"^\| (1[a-g]\. [^|]+?) \| ([^|]+?) \|$", xi, re.M)
    if [l for l, _ in rows] != [x[0] for x in subs] or len(rows) != 7:
        bad.append(("rows", [l[:3] for l, _ in rows], [x[0][:3] for x in subs]))
    decided = set()
    for label, items, blk in subs:
        row = next((c for l, c in rows if l == label), None)
        if row is None:
            continue
        need = []
        for it in items:
            m = re.match(r"^\*\*([^*]+)\*\*", it) or re.match(r"^\*([^*]+)\*", it)
            lead = m.group(1).rstrip(".") if m else ""
            clauses = CLAUSE.findall(it)
            if lead and re.search(DATE_RE, lead):
                need.append(lead)
            elif clauses:
                need += [f"{lead}: {c}" for c in clauses]
            if lead.startswith("Decided") or any(c.startswith("Decided") for c in clauses):
                decided.add(label[:2])
        bad += [(label[:2], "missing from its row: " + x[:50]) for x in need if x not in row]
        pieces = [p.rstrip(".") for part in row.split(". ") for p in part.split(": ")]
        bad += [(label[:2], "not on the decisions page under it: " + p[:50]) for p in pieces if p and p != "Open" and p not in blk]
        if row.startswith("Open. ") == (label[:2] in decided):
            bad.append((label[:2], "marked open" if label[:2] in decided else "not marked open"))
    m = re.search(r"((?:1[a-g], )*1[a-g]) and (1[a-g]) have since been decided", xi)
    listed = set(re.findall(r"1[a-g]", m.group(0))) if m else set()
    if listed != decided:
        bad.append(("the ruling's list of decided sub-decisions", sorted(listed), "against the decisions page", sorted(decided)))
    r["P21 \u00a7XI's table gives each sub-decision its label, its dated lead-ins and its standing in the decisions page's words, and marks open exactly the sub-decisions the ruling's sentence leaves undecided"] = (not bad, bad)
    known = {q for q, _, _ in QUOTES}
    bad, seen = [], 0
    for rel in ctx["markdown"]:
        if rel in own:
            continue
        text = read(rel)
        if "projective-carrier.md" not in text:
            continue
        for line in text.split("\n"):
            anchors = {m.group(2) for m in re.finditer(r"\]\(([^)#\s]*projective-carrier\.md)#([^)\s]+)\)", line) if into_page(rel, m.group(1))}
            if not anchors:
                continue
            seen += 1
            for q in re.findall(r'"([^"\n]{12,})"', re.sub(r'<a id="[^"]*"></a>', "", line)):
                if q in known:
                    continue
                if not any(q in x for x in fam.values()):
                    if not any(q in read(d) for d in linked_pages(rel, line)):
                        bad.append((rel.split("/")[-1], sorted(anchors), q[:50], "on none of these pages, nor on another page the line links"))
                    continue
                if not any(q in section_of(t, a) for a in anchors):
                    bad.append((rel.split("/")[-1], sorted(anchors), q[:50]))
    r["P22 a quotation that another page sets beside a link to one of this page's sections lies in that section, unless it quotes another page that line links"] = (not bad and seen >= 20, bad or seen)
    return r


def context():
    return {"outs": {f"{n}.out": open(os.path.join(SCRIPTS, f"{n}.out"), encoding="utf-8").read() for n in EXPECTED},
            "files": {nm: open(os.path.join(SCRIPTS, nm), "rb").read() for nm in tracked(SCRIPTS)},
            "manifest": open(os.path.join(SCRIPTS, "SHA256SUMS"), encoding="utf-8").read(),
            "markdown": markdown_files(),
            "sources": {}}


def main():
    fam = {key: src(rel) for key, rel in FAMILY.items()}
    t = fam["page"]
    ctx = context()
    res = checks(fam, ctx)
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

    def on(key, old, new):
        """The family with one string of one page changed; the string has to be there."""
        assert old in fam[key], (key, old)
        return dict(fam, **{key: fam[key].replace(old, new, 1)})

    def more(key, tail):
        return dict(fam, **{key: fam[key] + tail})

    bc = ctx["outs"]["bent_carrier.out"]
    first_pass = next(l for l in bc.split("\n") if l.startswith("PASS "))
    lam = "files/cosmos/files/cosmological-constant.md"
    bridge = WF + "/postulate-bridge.md"
    waltz = "files/spectrum/files/the-waltz.md"
    contributing = "CONTRIBUTING.md"
    slot_action = WF + "/slot-action.md"
    big = "\n" + "$`" + "{" * 2100 + "}" * 2100 + "`$\n"
    arms = [  # (check, where the defect is planted, the family, the context)
        ("P1", "the page", on("page", "The premise is adopted by ruling", "The premise is adopted \u2014 by ruling"), ctx),
        ("P1", "the inventory", more("inventory", "\n\u2014\n"), ctx),
        ("P1", "the proofs", more("proofs", "\n\u2014\n"), ctx),
        ("P2", "the page", on("page", "**State:** Active", "**State:** Running"), ctx),
        ("P3", "the page", on("page", "scaling-law-uniqueness.md#linear-readout-two-routes-and-a-no-go", "scaling-law-uniqueness.md#linear-readout-two-roads"), ctx),
        ("P3", "the inventory", on("inventory", "postulate-bridge.md#route-1", "postulate-bridge.md#route-one"), ctx),
        ("P3", "the bridge's anchor, reached from the inventory", fam, with_("P3", source=(bridge, src(bridge).replace('<a id="route-1"></a>', '<a id="route-one"></a>', 1)))),
        ("P3", "the proofs", on("proofs", "projective-carrier.md#ix-fixed-edge-stability", "projective-carrier.md#ix-fixed-edge"), ctx),
        ("P4", "the page", on("page", "$`\\mathbb{RP}^3 = S^3/\\{\\pm I\\}`$, the one space form", "$`\\mathbb{RP}^3 = S^3/\\{\\pm I\\}$, the one space form"), ctx),
        ("P4", "the inventory", on("inventory", "lying in $`\\mathbb{RP}^3`$.", "lying in $`\\mathbb{RP}^3$."), ctx),
        ("P4", "the proofs", on("proofs", "On the smooth locus $`x_e`$ solves", "On the smooth locus $`x_e$ solves"), ctx),
        ("P5", "the page", more("page", big), ctx),
        ("P5", "the inventory", more("inventory", big), ctx),
        ("P5", "the proofs", more("proofs", big), ctx),
        ("P6", "the page", on("page", "they must not be merged.", "they must never be merged."), ctx),
        ("P6", "the inventory", on("inventory", "These are different operations doing different jobs", "These are different operations doing separate jobs"), ctx),
        ("P7", "the page", on("page", "| 1.0212 | 1.0891 |", "| 1.0213 | 1.0891 |"), ctx),
        ("P8", "a record", fam, with_("P8", out=("bent_carrier.out", bc.replace(first_pass + "\n", "", 1)))),
        ("P8", "a record", fam, with_("P8", out=("bent_carrier.out", bc + "PASS B10 an unexpected check\n"))),
        ("P9", "the page", on("page", "transverse, not restrictive", "transverse, not restricting"), ctx),
        ("P9", "the inventory", on("inventory", "The dance runs on two distinct seams", "The dance runs on two separate seams"), ctx),
        ("P9", "the proofs", more("proofs", '\nA page that says "this is not on the verified list" fails.\n'), ctx),
        ("P10", "the page", on("page", "the-waltz.md#the-surface-leads-only-the-vacuum) \"Excited modes", "the-waltz.md#i-the-two-partners) \"Excited modes"), ctx),
        ("P10", "the inventory", on("inventory", "#iii-the-spectral-seed) \"The holonomy selects", "#ii-the-geometry) \"The holonomy selects"), ctx),
        ("P11", "the page", on("page", "- **Tolerance.** The extrapolated bottom", "- **Tolerance.** The extrapolated  bottom"), ctx),
        ("P12", "a script", fam, with_("P12", file=("lift_trace.py", ctx["files"]["lift_trace.py"] + b"\n"))),
        ("P12", "the manifest", fam, with_("P12", manifest=ctx["manifest"] + "0" * 64 + "  stray.txt\n")),
        ("P13", "the Λ page", fam, with_("P13", source=(lam, src(lam).replace("projective-carrier.md#ii-lemma-1", "projective-carrier.md#ii-lemma-one", 1)))),
        ("P13", "the bridge", fam, with_("P13", source=(bridge, re.sub(r"\n\n\*\*Scope under the ruling \([^)]*\)\.\*\* Both walls stand\.[^\n]*", "", src(bridge), count=1)))),
        ("P13", "the Waltz", fam, with_("P13", source=(waltz, src(waltz).replace("working/files/projective-carrier.md", "working/files/plato-twist.md", 1)))),
        ("P14", "CONTRIBUTING's link to section XI", fam, with_("P14", source=(contributing, src(contributing).replace("projective-carrier.md#xi-the-ruling", "projective-carrier.md#xi-the-rulings", 1)))),
        ("P14", "the list of files scanned", fam, with_("P14", markdown=[])),
        ("P15", "the pointer under Proposition 6", on("page", "(carrier-proofs.md#proposition-6)", "(carrier-proofs.md#proposition-7)"), ctx),
        ("P15", "section X's link", on("page", "It is now [The Projective Carrier: Scope Inventory](carrier-inventory.md), moved", "It is now The Projective Carrier: Scope Inventory, moved"), ctx),
        ("P16", "a heading on the proofs page", on("proofs", "\n## Proposition 6\n", "\n## Proposition Six\n"), ctx),
        ("P17", "a link back on the proofs page", on("proofs", "[The Projective Carrier, §IX](projective-carrier.md#ix-fixed-edge-stability):", "The Projective Carrier, §IX:"), ctx),
        ("P18", "a statement's copy on the proofs page", on("proofs", "Let $`D`$ be the strip", "Let $`D`$ be a strip"), ctx),
        ("P18", "a statement on the page", on("page", "least area with the edge fixed).** Let $`M'`$ be a competitor", "least area with the edge fixed).** Let $`M'`$ be any competitor"), ctx),
        ("P18", "a statement's copy cut short on the proofs page", on("proofs", "\n\nSo under the Friedrichs realization the exact $`2/R^2`$, kept as the first positive level, forces a singular point that carries the twist (Corollary 2.1) but not geodesic laps.", ""), ctx),
        ("P19", "the inventory's Parent", on("inventory", "**Parent:** `projective-carrier.md`", "**Parent:** `postulate-bridge.md`"), ctx),
        ("P19", "the page's links to the proofs page", dict(fam, page=re.sub(r"\]\(carrier-proofs\.md[^)]*\)", "](lipschitz-comparison.md)", t)), ctx),
        ("P20", "the proofs page's header", on("proofs", "**Type:** Result\n**State:** Closed", "**State:** Closed\n**Type:** Result"), ctx),
        ("P20", "the inventory's header", dict(fam, inventory=re.sub(r"\n\*\*Inputs:\*\*[^\n]*", "", fam["inventory"], count=1)), ctx),
        ("P1", "the decisions", more("decisions", "\n" + EM + "\n"), ctx),
        ("P3", "the decisions", on("decisions", "scaling-law-uniqueness.md#linear-readout-two-routes-and-a-no-go", "scaling-law-uniqueness.md#linear-readout-two-roads"), ctx),
        ("P4", "the decisions", on("decisions", "$`A_{ij} = 0`$. It is the only cell", "$`A_{ij} = 0$. It is the only cell"), ctx),
        ("P5", "the decisions", more("decisions", big), ctx),
        ("P6", "the decisions", on("decisions", "spectrally an orientable object", "spectrally an oriented object"), ctx),
        ("P9", "the decisions", more("decisions", '\nA page that says "this is not on the verified list" fails.\n'), ctx),
        ("P10", "the proofs", more("proofs", '\n[Route 1](postulate-bridge.md#route-1) "The dance runs on two distinct seams"\n'), ctx),
        ("P10", "the decisions", more("decisions", '\n[Route 1](postulate-bridge.md#route-1) "The dance runs on two distinct seams"\n'), ctx),
        ("P15", "section XI's link", on("page", "are on [The Projective Carrier: Decision Records](carrier-decisions.md), moved there", "are on The Projective Carrier: Decision Records, moved there"), ctx),
        ("P19", "the decisions page's Parent", on("decisions", "**Parent:** `projective-carrier.md`", "**Parent:** `postulate-bridge.md`"), ctx),
        ("P20", "the decisions page's header", on("decisions", "**Type:** Result\n**State:** Open", "**State:** Open\n**Type:** Result"), ctx),
        ("P21", "a lead-in reworded in its row", on("page", "| Decided 2026-09-29: Friedrichs in both sectors |", "| Decided 2026-09-29: Friedrichs in the twisted sector |"), ctx),
        ("P21", "a label without its reading tags", on("page", "| 1d. The sampler (A, A\u2032) |", "| 1d. The sampler |"), ctx),
        ("P21", "a dated note dropped from its row", on("page", ". Note (2026-10-05), on Proposition 8 |", " |"), ctx),
        ("P21", "the open sub-decision shown as decided", on("page", "| Open. Ruled 2026-09-30", "| Ruled 2026-09-30"), ctx),
        ("P21", "a decision on the decisions page that the table lacks", on("decisions", "  - *Ruled 2026-09-30: the framework's two-lap sentence binds as topology only.*", "  - *Decided 2026-11-12: a planted decision.*\n  - *Ruled 2026-09-30: the framework's two-lap sentence binds as topology only.*"), ctx),
        ("P22", "slot-action.md's link moved to \u00a7I", fam, with_("P22", source=(slot_action, src(slot_action).replace("projective-carrier.md#xi-the-ruling", "projective-carrier.md#i-the-projective-layer", 1)))),
        ("P22", "the words slot-action.md quotes, dropped from \u00a7XI's table", on("page", "where the sampler's target bundles live, reached", "reached"), ctx),
        ("P22", "the list of files scanned", fam, with_("P22", markdown=[])),
        ("P22", "the words slot-action.md quotes, reworded on all four pages", {k: v.replace("where the sampler's target bundles live", "where the sampler's target bundles sit") for k, v in fam.items()}, ctx),
    ]
    rc = silent = 0
    for key, where, bfam, bctx in arms:
        assert (bfam, bctx) != (fam, ctx), (key, where)
        name = next(k for k in res if k.startswith(key + " "))
        ok, info = checks(bfam, bctx)[name]
        fired = not ok
        print(("ARM FIRED " if fired else "ARM SILENT ") + f"{key} [{where}] " + name[len(key) + 1:] + (f"  {str(info)[:150]}" if fired else ""))
        rc |= 0 if fired else 1
        silent += 0 if fired else 1
    print(f"arms: {len(arms) - silent} of {len(arms)} fired")
    return rc


if __name__ == "__main__":
    sys.exit(main())
