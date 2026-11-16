"""Generates the additional OpenMBEE / OpenSysML brand graphics (SVG) into brand/.

Run:  python3 graphics.py   (needs fontTools and the Inter font; text is converted to outlines
so the SVGs render the same everywhere without any font installed.)

NOTE: the brand typeface is ABeeZee. If you have ABeeZee-Regular.ttf, set FONT_DIR / the FONTS
entries below to it and re-run to get exact brand lettering.
"""
import math
import os
from fontTools.ttLib import TTFont
from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.pens.transformPen import TransformPen

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "brand")
FONT_DIR = "/usr/share/fonts/opentype/inter"
FONTS = {
    "light": "Inter-Light.otf",
    "regular": "Inter-Regular.otf",
    "semibold": "Inter-SemiBold.otf",
    "bold": "Inter-Bold.otf",
    "italic": "Inter-Italic.otf",
}
_cache = {}


def font(name):
    if name not in _cache:
        f = TTFont(os.path.join(FONT_DIR, FONTS[name]))
        _cache[name] = (f.getGlyphSet(), f.getBestCmap(), f["head"].unitsPerEm, f["hmtx"], f)
    return _cache[name]


def adv(ch, fname, size):
    gs, cmap, upm, hmtx, _ = font(fname)
    return hmtx[cmap[ord(ch)]][0] * size / upm


def text_width(text, fname, size, track=0):
    return sum(adv(c, fname, size) + track for c in text) - track


def glyph(ch, fname, size, px, py, phi=0.0):
    """Outline of one glyph: left edge of its advance box at local origin, baseline through (px,py),
    rotated by phi radians (SVG sense)."""
    gs, cmap, upm, hmtx, _ = font(fname)
    s = size / upm
    cs, sn = math.cos(phi), math.sin(phi)
    pen = SVGPathPen(gs)
    tp = TransformPen(pen, (s * cs, s * sn, s * sn, -s * cs, px, py))
    gs[cmap[ord(ch)]].draw(tp)
    return pen.getCommands()


def straight(text, fname, size, x, y, anchor="middle", track=0):
    w = text_width(text, fname, size, track)
    x0 = x - (w / 2 if anchor == "middle" else 0 if anchor == "start" else w)
    d, cx = [], x0
    for c in text:
        d.append(glyph(c, fname, size, cx, y))
        cx += adv(c, fname, size) + track
    return " ".join(d)


def arc(segments, size, cx, cy, r, where="top", track=0, centre=None):
    """Text on a circle. segments = [(text, fontname), ...]. Baseline on radius r.
    top: reads clockwise, glyph tops point outward. bottom: reads left to right, tops point inward."""
    chars = []
    for text, fname in segments:
        for c in text:
            chars.append((c, fname))
    total = sum(adv(c, f, size) + track for c, f in chars) - track
    mid = (-math.pi / 2 if where == "top" else math.pi / 2) if centre is None else centre
    d, pos = [], 0.0
    for c, f in chars:
        a = adv(c, f, size)
        off = pos + a / 2 - total / 2           # distance of glyph centre from text centre
        th = mid + off / r if where == "top" else mid - off / r
        phi = th + math.pi / 2 if where == "top" else th - math.pi / 2
        gx, gy = cx + r * math.cos(th), cy + r * math.sin(th)
        # shift so glyph centre (not left edge) sits at the point
        gx -= (a / 2) * math.cos(phi)
        gy -= (a / 2) * math.sin(phi)
        d.append(glyph(c, f, size, gx, gy, phi))
        pos += a + track
    return " ".join(d)


def arc_stroke(cx, cy, r, a0, a1):
    p0 = (cx + r * math.cos(math.radians(a0)), cy + r * math.sin(math.radians(a0)))
    p1 = (cx + r * math.cos(math.radians(a1)), cy + r * math.sin(math.radians(a1)))
    large = 1 if (a1 - a0) % 360 > 180 else 0
    return f"M{p0[0]:.2f} {p0[1]:.2f}A{r} {r} 0 {large} 1 {p1[0]:.2f} {p1[1]:.2f}"


THEMES = {
    # dark: self-contained navy disc, light artwork. light: transparent, dark artwork for white pages.
    "dark": dict(bg="#10052F", ink="#D6D6D6", acc="#64DDFA", fill=0.16, text="#D6D6D6", head="#FFFFFF"),
    "light": dict(bg=None, ink="#10052F", acc="#3E8DB5", fill=0.16, text="#10052F", head="#10052F"),
}


# ---------- shared ornaments ----------
def sq(x, y, t, s=11):
    return (f'<rect x="{x - s / 2:.1f}" y="{y - s / 2:.1f}" width="{s}" height="{s}" rx="2" '
            f'fill="{t["bg"] or "#fff"}" stroke="{t["ink"]}" stroke-width="3"/>')


def panel(x, y, w, h, t, r=9):
    return (f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{r}" fill="{t["bg"] or "#fff"}"/>'
            f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{r}" fill="{t["acc"]}" '
            f'fill-opacity="{t["fill"]}" stroke="{t["ink"]}" stroke-width="4"/>')


def frame(t, cx=300, cy=300):
    out = []
    if t["bg"]:
        out.append(f'<circle cx="{cx}" cy="{cy}" r="298" fill="{t["bg"]}"/>')
    out.append(f'<circle cx="{cx}" cy="{cy}" r="290" fill="none" stroke="{t["ink"]}" stroke-width="6"/>')
    out.append(f'<circle cx="{cx}" cy="{cy}" r="278" fill="none" stroke="{t["ink"]}" stroke-width="2" stroke-opacity=".7"/>')
    out.append(f'<circle cx="{cx}" cy="{cy}" r="186" fill="none" stroke="{t["ink"]}" stroke-width="4"/>')
    return out


def svg(w, h, body, title):
    return (f'<?xml version="1.0" encoding="UTF-8"?>\n'
            f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="{w}" height="{h}" '
            f'role="img" aria-label="{title}"><title>{title}</title>\n' + "\n".join(body) + "\n</svg>\n")


# ---------- 1. OpenSysML badge ----------
def opensysml_badge(t):
    c = 300
    b = frame(t)
    b.append(f'<circle cx="{c}" cy="{c}" r="138" fill="none" stroke="{t["acc"]}" stroke-width="3.5" stroke-dasharray="11 11"/>')
    D, H = 118, 40  # panel centre distance, half size
    # connectors
    for dx, dy in ((0, -1), (0, 1), (-1, 0), (1, 0)):
        x0, y0 = c + dx * 48, c + dy * 48
        x1, y1 = c + dx * (D - H), c + dy * (D - H)
        b.append(f'<line x1="{x0}" y1="{y0}" x2="{x1}" y2="{y1}" stroke="{t["acc"]}" stroke-width="4"/>')
    # octagon hub with open padlock
    pts = " ".join(f"{c + 50 * math.cos(math.radians(22.5 + 45 * i)):.1f},{c + 50 * math.sin(math.radians(22.5 + 45 * i)):.1f}" for i in range(8))
    b.append(f'<polygon points="{pts}" fill="{t["acc"]}" fill-opacity="{t["fill"]}" stroke="{t["ink"]}" stroke-width="4" stroke-linejoin="round"/>')
    b.append(f'<path d="M{c - 11} {c - 4}V{c - 18}a11 11 0 0 1 22 0V{c - 12}" fill="none" stroke="{t["acc"]}" stroke-width="6" stroke-linecap="round"/>')
    b.append(f'<rect x="{c - 19}" y="{c - 4}" width="38" height="30" rx="5" fill="{t["acc"]}"/>')
    b.append(f'<circle cx="{c}" cy="{c + 8}" r="5" fill="{t["bg"] or "#fff"}"/><rect x="{c - 2}" y="{c + 10}" width="4" height="9" fill="{t["bg"] or "#fff"}"/>')
    # top panel: list
    px, py = c - H, c - D - H
    b.append(panel(px, py, 2 * H, 2 * H, t))
    for i in range(4):
        yy = py + 17 + i * 15.5
        b.append(f'<circle cx="{px + 17}" cy="{yy}" r="3.6" fill="{t["acc"]}"/><line x1="{px + 29}" y1="{yy}" x2="{px + 64}" y2="{yy}" stroke="{t["acc"]}" stroke-width="4.5" stroke-linecap="round"/>')
    # left panel: f(x)
    px, py = c - D - H, c - H
    b.append(panel(px, py, 2 * H, 2 * H, t))
    b.append(f'<path d="{glyph("f", "italic", 50, px + 14, py + 55)}" fill="{t["acc"]}"/>')
    for i, wlen in enumerate((20, 20)):
        b.append(f'<line x1="{px + 46}" y1="{py + 32 + i * 15}" x2="{px + 46 + wlen}" y2="{py + 32 + i * 15}" stroke="{t["acc"]}" stroke-width="4.5" stroke-linecap="round"/>')
    # right panel: block diagram
    px, py = c + D - H, c - H
    b.append(panel(px, py, 2 * H, 2 * H, t))
    b.append(f'<rect x="{px + 12}" y="{py + 12}" width="34" height="14" rx="2" fill="{t["acc"]}"/>')
    b.append(f'<rect x="{px + 38}" y="{py + 33}" width="30" height="14" rx="2" fill="{t["acc"]}"/>')
    b.append(f'<rect x="{px + 38}" y="{py + 54}" width="30" height="14" rx="2" fill="{t["acc"]}"/>')
    b.append(f'<path d="M{px + 29} {py + 26}V{py + 40}H{px + 38}M{px + 29} {py + 40}V{py + 61}H{px + 38}" fill="none" stroke="{t["acc"]}" stroke-width="3.5"/>')
    # bottom panel: flowchart
    px, py = c - H, c + D - H
    b.append(panel(px, py, 2 * H, 2 * H, t))
    b.append(f'<rect x="{px + 22}" y="{py + 10}" width="36" height="14" rx="3" fill="{t["acc"]}"/>')
    b.append(f'<path d="M{px + 40} {py + 24}v8" stroke="{t["acc"]}" stroke-width="3.5"/>')
    b.append(f'<path d="M{px + 40} {py + 32}l12 12l-12 12l-12 -12z" fill="none" stroke="{t["acc"]}" stroke-width="4"/>')
    b.append(f'<path d="M{px + 40} {py + 56}v6M{px + 52} {py + 44}h10v18" fill="none" stroke="{t["acc"]}" stroke-width="3.5"/>')
    b.append(f'<rect x="{px + 24}" y="{py + 62}" width="52" height="12" rx="3" fill="{t["acc"]}"/>')
    # connector squares
    for dx, dy in ((0, -1), (0, 1), (-1, 0), (1, 0)):
        b.append(sq(c + dx * 48, c + dy * 48, t))
        b.append(sq(c + dx * (D - H), c + dy * (D - H), t))
    # text
    b.append(f'<path fill="{t["text"]}" d="{arc([("OPENSYSML", "bold")], 56, c, c, 218, "top", track=5)}"/>')
    b.append(f'<path fill="{t["text"]}" d="{arc([("SYSML V2", "semibold")], 46, c, c, 241, "bottom", track=4)}"/>')
    b.append(f'<path fill="{t["acc"]}" d="{arc([("OPENSYSML.ORG", "regular")], 21, c, c, 270, "bottom", track=3)}"/>')
    # side arcs
    for a0, a1 in ((148, 212), (-32, 32)):
        b.append(f'<path d="{arc_stroke(c, c, 232, a0, a1)}" fill="none" stroke="{t["acc"]}" stroke-width="4" stroke-linecap="round"/>')
    return svg(600, 600, b, "OpenSysML badge: SysML v2, opensysml.org")


# ---------- 2. Workshop 2027 badge ----------
def workshop_badge(t, venue="INCOSE IW"):
    c = 300
    bgc = t["bg"] or "#fff"
    out = []
    if t["bg"]:
        out.append(f'<circle cx="{c}" cy="{c}" r="298" fill="{t["bg"]}"/>')
    out.append(f'<circle cx="{c}" cy="{c}" r="290" fill="none" stroke="{t["ink"]}" stroke-width="6"/>')
    out.append(f'<circle cx="{c}" cy="{c}" r="278" fill="none" stroke="{t["ink"]}" stroke-width="2" stroke-opacity=".7"/>')
    out.append(f'<circle cx="{c}" cy="{c}" r="202" fill="none" stroke="{t["ink"]}" stroke-width="4"/>')
    out.append(f'<circle cx="{c}" cy="{c}" r="189" fill="none" stroke="{t["acc"]}" stroke-width="3.5" stroke-dasharray="11 11"/>')
    # icon drawn in the original artwork's coordinate space (centre 516,385), scaled to fit the ring
    g = []
    ink, acc, W = t["ink"], t["acc"], 6.5

    def sqr(x, y):
        return (f'<rect x="{x - 9}" y="{y - 9}" width="18" height="18" rx="3" fill="{bgc}" stroke="{ink}" stroke-width="5"/>')

    def blk(x, y, w, h, op=.32):
        return (f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="9" fill="{bgc}"/>'
                f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="9" fill="{acc}" fill-opacity="{op}" stroke="{ink}" stroke-width="{W}"/>')

    # document (fold at top-left)
    dx0, dy0, dx1, dy1, f = 340, 232, 547, 530, 44
    doc = (f'M{dx0 + f} {dy0}H{dx1 - 9}a9 9 0 0 1 9 9V{dy1 - 9}a9 9 0 0 1-9 9H{dx0 + 9}a9 9 0 0 1-9-9V{dy0 + f}Z')
    g.append(f'<path d="{doc}" fill="{bgc}"/>')
    g.append(f'<path d="{doc}" fill="{acc}" fill-opacity="{t["fill"]}" stroke="{ink}" stroke-width="{W}" stroke-linejoin="round"/>')
    g.append(f'<path d="M{dx0 + f} {dy0}V{dy0 + f}H{dx0}" fill="{ink}" fill-opacity=".25" stroke="{ink}" stroke-width="{W}" stroke-linejoin="round"/>')
    for i, ln in enumerate((150, 150, 104)):
        g.append(f'<line x1="{dx0 + 34}" y1="{dy0 + 84 + i * 30}" x2="{dx0 + 34 + ln}" y2="{dy0 + 84 + i * 30}" stroke="{ink}" stroke-width="7" stroke-linecap="round" stroke-opacity=".8"/>')
    g.append(f'<circle cx="{dx0 + 52}" cy="{dy0 + 196}" r="19" fill="{acc}" fill-opacity=".45"/><path d="M{dx0 + 52} {dy0 + 196}v-19a19 19 0 0 1 19 19z" fill="{acc}"/>')
    for i, bh in enumerate((34, 52, 72)):
        g.append(f'<rect x="{dx0 + 32 + i * 26}" y="{dy1 - 32 - bh}" width="16" height="{bh}" rx="2" fill="{acc}" fill-opacity="{.55 + i * .2}"/>')
    for i, ln in enumerate((70, 70, 50)):
        g.append(f'<line x1="{dx0 + 112}" y1="{dy1 - 80 + i * 22}" x2="{dx0 + 112 + ln}" y2="{dy1 - 80 + i * 22}" stroke="{ink}" stroke-width="6" stroke-linecap="round" stroke-opacity=".7"/>')
    # connectors (under the blocks)
    g.append(f'<path d="M557 400H575M575 300V500M575 300H592M575 400H592M575 500H592" fill="none" stroke="{ink}" stroke-width="{W - 1.5}"/>')
    g.append(f'<path d="M700 300h22a10 10 0 0 1 10 10v80a10 10 0 0 1-10 10h-22M700 400h22a10 10 0 0 1 10 10v80a10 10 0 0 1-10 10h-22" fill="none" stroke="{ink}" stroke-width="{W - 1.5}"/>')
    # blocks: A overlaps the document edge, T / B / C stack on the right
    g.append(blk(448, 368, 109, 64, .45))
    g.append(blk(592, 268, 108, 64))
    g.append(blk(592, 368, 108, 64))
    g.append(blk(592, 468, 108, 64))
    for x, y in ((557, 400), (592, 300), (592, 400), (592, 500), (700, 300), (700, 400), (700, 500)):
        g.append(sqr(x, y))
    out.append(f'<g transform="translate({c} {c}) scale(.74) translate(-516 -385)">' + "".join(g) + "</g>")
    # text: OPEN light + MBEE bold, as in the logo wordmark
    out.append(f'<path fill="{t["text"]}" d="{arc([("OPEN", "light"), ("MBEE", "bold")], 52, c, c, 217, "top", track=6)}"/>')
    out.append(f'<path fill="{t["text"]}" d="{arc([("2027 WORKSHOP", "semibold")], 44, c, c, 242, "bottom", track=4)}"/>')
    out.append(f'<path fill="{t["acc"]}" d="{arc([(f"at {venue}", "regular")], 24, c, c, 269, "bottom", track=2)}"/>')
    for a0, a1 in ((150, 210), (-30, 30)):
        out.append(f'<path d="{arc_stroke(c, c, 240, a0, a1)}" fill="none" stroke="{t["acc"]}" stroke-width="4" stroke-linecap="round"/>')
    return svg(600, 600, out, f"OpenMBEE 2027 Workshop at {venue} badge")


# ---------- 3. DocGen language lockup ----------
def docgen(t):
    W, H = 1000, 560
    b = []
    if t["bg"]:
        b.append(f'<rect width="{W}" height="{H}" rx="28" fill="{t["bg"]}"/>')
    ink, acc = t["ink"], t["acc"]
    sw = 6
    # SysML block (left)
    x, y, w, h = 250, 110, 190, 150
    b.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" fill="{acc}" fill-opacity="{t["fill"]}" stroke="{ink}" stroke-width="{sw}"/>')
    b.append(f'<line x1="{x}" y1="{y + 38}" x2="{x + w}" y2="{y + 38}" stroke="{ink}" stroke-width="{sw}"/>')
    b.append(f'<line x1="{x + 70}" y1="{y + 38}" x2="{x + 70}" y2="{y + h}" stroke="{ink}" stroke-width="{sw}"/>')
    b.append(f'<line x1="{x + 70}" y1="{y + 94}" x2="{x + w}" y2="{y + 94}" stroke="{ink}" stroke-width="{sw}"/>')
    b.append(f'<path fill="{ink}" d="{straight("SYSML", "bold", 22, x + w / 2, y + 27, track=1)}"/>')
    b.append(f'<line x1="{x + w / 2}" y1="{y}" x2="{x + w / 2}" y2="{y - 24}" stroke="{ink}" stroke-width="{sw}"/>')
    b.append(f'<rect x="{x + w / 2 - 8}" y="{y - 38}" width="16" height="16" fill="{t["bg"] or "#fff"}" stroke="{ink}" stroke-width="5"/>')
    b.append(f'<line x1="{x + w / 2}" y1="{y + h}" x2="{x + w / 2}" y2="{y + h + 24}" stroke="{ink}" stroke-width="{sw}"/>')
    b.append(f'<rect x="{x + w / 2 - 8}" y="{y + h + 22}" width="16" height="16" fill="{t["bg"] or "#fff"}" stroke="{ink}" stroke-width="5"/>')
    for yy in (y + 62, y + 108):
        b.append(f'<line x1="{x}" y1="{yy}" x2="{x - 20}" y2="{yy}" stroke="{ink}" stroke-width="{sw}"/>')
        b.append(f'<rect x="{x - 42}" y="{yy - 10}" width="22" height="20" fill="{t["bg"] or "#fff"}" stroke="{ink}" stroke-width="5"/>')
    # arrow
    b.append(f'<path d="M462 185h62v-26l54 40-54 40v-26h-62z" fill="{acc}"/>')
    # document stack
    for i, (dx, dy) in enumerate(((36, -12), (18, -6), (0, 0))):
        fx, fy = 610 + dx, 100 + dy
        b.append(f'<path d="M{fx} {fy + 8}a8 8 0 0 1 8-8h96l34 34v136a8 8 0 0 1-8 8h-122a8 8 0 0 1-8-8z" fill="{t["bg"] or "#fff"}" stroke="{ink}" stroke-width="{sw}" stroke-linejoin="round"/>')
        if i == 2:
            b.append(f'<path d="M{fx + 104} {fy}v34h34" fill="none" stroke="{ink}" stroke-width="{sw}" stroke-linejoin="round"/>')
            for j, ln in enumerate((86, 86, 56)):
                b.append(f'<line x1="{fx + 18}" y1="{fy + 56 + j * 18}" x2="{fx + 18 + ln}" y2="{fy + 56 + j * 18}" stroke="{ink}" stroke-width="5" stroke-linecap="round" stroke-opacity=".75"/>')
            for j, bh in enumerate((18, 32, 48, 64)):
                b.append(f'<rect x="{fx + 22 + j * 22}" y="{fy + 168 - bh}" width="14" height="{bh}" rx="2" fill="{acc}"/>')
            b.append(f'<line x1="{fx + 16}" y1="{fy + 169}" x2="{fx + 116}" y2="{fy + 169}" stroke="{ink}" stroke-width="3" stroke-opacity=".7"/>')
    b.append(f'<path fill="{t["head"]}" d="{straight("OPENSYSML", "bold", 118, W / 2, 428, track=4)}"/>')
    b.append(f'<path fill="{acc}" d="{straight("DOCGEN LANGUAGE", "semibold", 50, W / 2, 500, track=5)}"/>')
    return svg(W, H, b, "OpenSysML DocGen Language")


# ---------- 4. Clear-space diagram for the OpenSysML badge ----------
def clear_space(badge=None, label="OpenSysML badge"):
    t = THEMES["light"]
    badge = badge or opensysml_badge
    S, B = 700, 440
    x0 = (S - B) / 2
    z = B / 8
    inner = badge(t)
    inner = inner[inner.index("<svg"):].replace(' width="600" height="600"', "", 1)
    inner = inner.replace('<svg xmlns="http://www.w3.org/2000/svg"', f'<svg x="{x0}" y="{x0}" width="{B}" height="{B}" xmlns="http://www.w3.org/2000/svg"', 1)
    ink, acc = t["ink"], t["acc"]
    a, b2 = x0 - z, x0 + B + z
    body = [f'<rect x="{a}" y="{a}" width="{b2 - a}" height="{b2 - a}" fill="{acc}" fill-opacity=".12"/>',
            f'<rect x="{x0}" y="{x0}" width="{B}" height="{B}" fill="#fff"/>',
            inner,
            f'<rect x="{a}" y="{a}" width="{b2 - a}" height="{b2 - a}" fill="none" stroke="{acc}" stroke-width="3" stroke-dasharray="10 8"/>']
    mid = S / 2
    for (px, py) in ((mid, (a + x0) / 2), (mid, (b2 + x0 + B) / 2), ((a + x0) / 2, mid), ((b2 + x0 + B) / 2, mid)):
        body.append(f'<path fill="{ink}" d="{straight("x", "semibold", 30, px, py + 10)}"/>')
    for (x1, y1, x2, y2) in ((mid + 50, a, mid + 50, x0), (mid + 50, x0 + B, mid + 50, b2),
                             (a, mid + 50, x0, mid + 50), (x0 + B, mid + 50, b2, mid + 50)):
        body.append(f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{ink}" stroke-width="2.5"/>')
    return svg(S, S, body, f"{label} with its clear space marked: x equals one eighth of the badge width")


ITEMS = {
    "opensysml-badge": opensysml_badge,
    "openmbee-workshop-2027": workshop_badge,
    "openmbee-workshop-2027-caltech": lambda t: workshop_badge(t, "Caltech"),
    "opensysml-docgen": docgen,
}

if __name__ == "__main__":
    for name, fn in ITEMS.items():
        for tn, t in THEMES.items():
            path = os.path.join(OUT, f"{name}-{tn}.svg")
            with open(path, "w", encoding="utf-8") as fh:
                fh.write(fn(t))
            print("wrote", path)
    with open(os.path.join(OUT, "opensysml-clear-space.svg"), "w", encoding="utf-8") as fh:
        fh.write(clear_space())
    with open(os.path.join(OUT, "openmbee-workshop-clear-space.svg"), "w", encoding="utf-8") as fh:
        fh.write(clear_space(workshop_badge, "OpenMBEE workshop badge"))
    print("wrote clear space")
