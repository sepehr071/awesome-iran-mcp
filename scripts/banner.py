"""Draw assets/banner.svg (English) and assets/banner.fa.svg (Persian) in a frosted-glass style.

Also assets/release-<RELEASE>.svg and assets/release-<RELEASE>.fa.svg, the README's "What's new" banner (edit RELEASE and HIGHLIGHTS).

Counts come from servers.json, so run scripts/catalog.py first:  python scripts/banner.py

Also writes assets/social.svg (1280x640) for GitHub's social preview, which needs a PNG:
  chrome --headless=new --hide-scrollbars --window-size=1280,640 --screenshot=assets/social.png assets/social.svg
"""

import base64
import html
import io
import json
import pathlib
import re

from fontTools import subset
from fontTools.ttLib import TTFont

ROOT = pathlib.Path(__file__).resolve().parent.parent
W, H = 1280, 460
ZWNJ = "&#x200C;"

# Banner tiles: English label, Persian label, servers.json categories, accent colour.
# A new server lands in its category's tile; only a new category needs a line here.
GROUPS = [
    ("Buy &amp; sell", "خرید و فروش", {"shopping", "fashion", "beauty", "classifieds"}, "#2fe0cf"),
    ("Food &amp; groceries", "غذا و سوپرمارکت", {"food"}, "#ff5c8f"),
    ("Travel &amp; stays", "سفر و اقامت", {"travel"}, "#6aa0ff"),
    ("Doctors &amp; clinics", "پزشک و درمان", {"health"}, "#7ee08a"),
    # the banner fits 3 rows of 2 tiles, so public-data categories share the books tile
    ("Books, news &amp; data", "کتاب، خبر و داده", {"books", "learning", "software", "prices", "stocks", "news", "quakes", "law", "tax"}, "#ffc23d"),
    ("Your own accounts", f"حساب{ZWNJ}های شخصی", {"business", "messaging", "crypto"}, "#b88cff"),
]

# Vazirmatn is embedded into each banner (see embed_fonts); the rest is fallback
LATIN = PERSIAN = "Vazirmatn,Vazir,Tahoma,'Segoe UI',sans-serif"
WEIGHTS = {400: "Regular", 600: "SemiBold", 700: "Bold", 800: "ExtraBold"}
MONO = "'SF Mono','JetBrains Mono','Cascadia Code',Consolas,monospace"
FA_DIGITS = str.maketrans("0123456789", "۰۱۲۳۴۵۶۷۸۹")

DEFS = """<defs>
    <linearGradient id="bg" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0" stop-color="#080b24"/><stop offset="1" stop-color="#170a2e"/>
    </linearGradient>
    <g id="blobs">
      <circle cx="210" cy="90" r="190" fill="#18c8b8"/>
      <circle cx="560" cy="400" r="170" fill="#7b3fe4"/>
      <circle cx="860" cy="60" r="160" fill="#ff3d8b"/>
      <circle cx="1160" cy="380" r="210" fill="#ffb02e"/>
      <circle cx="420" cy="-40" r="120" fill="#3d7bff"/>
    </g>
    <filter id="soft" x="-50%" y="-50%" width="200%" height="200%"><feGaussianBlur stdDeviation="60"/></filter>
    <filter id="frost" x="-50%" y="-50%" width="200%" height="200%"><feGaussianBlur stdDeviation="28"/></filter>
    <filter id="lift" x="-30%" y="-30%" width="160%" height="170%">
      <feDropShadow dx="0" dy="10" stdDeviation="14" flood-color="#000" flood-opacity="0.35"/>
    </filter>
    <filter id="iconlift" x="-30%" y="-30%" width="160%" height="170%">
      <feDropShadow dx="0" dy="5" stdDeviation="5" flood-color="#000" flood-opacity="0.4"/>
    </filter>
    <linearGradient id="rim" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0" stop-color="#fff" stop-opacity="0.75"/>
      <stop offset="0.45" stop-color="#fff" stop-opacity="0.12"/>
      <stop offset="1" stop-color="#fff" stop-opacity="0.45"/>
    </linearGradient>
    <linearGradient id="sheen" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0" stop-color="#fff" stop-opacity="0.22"/>
      <stop offset="0.5" stop-color="#fff" stop-opacity="0.06"/>
      <stop offset="1" stop-color="#fff" stop-opacity="0.10"/>
    </linearGradient>
    <linearGradient id="gloss" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0" stop-color="#fff" stop-opacity="0.28"/>
      <stop offset="0.5" stop-color="#fff" stop-opacity="0"/>
    </linearGradient>
    <linearGradient id="ink" x1="0" y1="0" x2="1" y2="0">
      <stop offset="0" stop-color="#ffffff"/><stop offset="1" stop-color="#bff6ee"/>
    </linearGradient>
  </defs>"""


def glass(id_: str, x: float, y: float, w: float, h: float, r: float) -> str:
    """A frosted panel: blurred copy of the background inside, white sheen, bright rim."""
    return f"""<clipPath id="{id_}"><rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{r}"/></clipPath>
  <rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{r}" fill="#000" fill-opacity="0.01" filter="url(#lift)"/>
  <g clip-path="url(#{id_})">
    <rect x="{x}" y="{y}" width="{w}" height="{h}" fill="url(#bg)"/>
    <use href="#blobs" filter="url(#frost)" opacity="0.95"/>
    <rect x="{x}" y="{y}" width="{w}" height="{h}" fill="url(#sheen)"/>
  </g>
  <rect x="{x + 0.75}" y="{y + 0.75}" width="{w - 1.5}" height="{h - 1.5}" rx="{r}" fill="none" stroke="url(#rim)" stroke-width="1.5"/>"""


def pill(x: float, y: float, w: float, text: str, font: str, color: str, fa: bool) -> str:
    dot, mid = (x + w - 24, x + w / 2 - 10) if fa else (x + 24, x + w / 2 + 10)
    return f"""<rect x="{x}" y="{y}" width="{w}" height="48" rx="24" fill="#fff" fill-opacity="0.14" stroke="#fff" stroke-opacity="0.35"/>
  <circle cx="{dot}" cy="{y + 24}" r="6" fill="{color}"/>
  <text x="{mid}" y="{y + 31}" text-anchor="middle" font-family="{font}" font-size="19" font-weight="700" fill="#fff">{text}</text>"""


def tiles(catalog: list, px: float, py: float, fa: bool) -> str:
    known = set().union(*(g[2] for g in GROUPS))
    if missing := {s["category"] for s in catalog} - known:
        raise SystemExit(f"add categories {sorted(missing)} to GROUPS in scripts/banner.py")
    out = []
    w, h, gap_x, gap_y = 240, 100, 18, 16
    for i, (en, fa_name, cats, color) in enumerate(GROUPS):
        group = [s for s in catalog if s["category"] in cats]
        n, t = len(group), sum(s["tool_count"] for s in group)
        row, col = divmod(i, 2)
        if fa:
            col = 1 - col  # right to left
        x, y = px + col * (w + gap_x), py + row * (h + gap_y)
        if fa:
            # rtl keeps "n servers · t tools" in Persian order; under rtl, "start" is the right edge
            label, sub, font, anchor, tx, bar = fa_name, f"{n} سرور · {t} ابزار".translate(FA_DIGITS), PERSIAN, "start", x + w - 30, x + w - 14
        else:
            label, sub, font, anchor, tx, bar = en, f"{n} servers · {t} tools", LATIN, "start", x + 30, x + 8
        out.append(f"""<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="22" fill="#fff" fill-opacity="0.10" stroke="#fff" stroke-opacity="0.28"/>
  <rect x="{bar}" y="{y + 24}" width="6" height="{h - 48}" rx="3" fill="{color}"/>
  <text x="{tx}" y="{y + 45}" text-anchor="{anchor}" direction="{"rtl" if fa else "ltr"}" font-family="{font}" font-size="21" font-weight="700" fill="#fff">{label}</text>
  <text x="{tx}" y="{y + 73}" text-anchor="{anchor}" direction="{"rtl" if fa else "ltr"}" font-family="{font}" font-size="16" font-weight="600" fill="#fff" fill-opacity="0.8">{sub}</text>""")
    return "\n  ".join(out)


def banner(fa: bool, catalog: list, h: int = H) -> str:
    servers, tools = len(catalog), sum(s["tool_count"] for s in catalog)
    card_x, panel_x = (650, 40) if fa else (40, 670)
    if fa:
        anchor, tx = "end", card_x + 590 - 44
        subtitle = f"وب ایران، آماده برای ایجنت{ZWNJ}های هوش مصنوعی"
        stats = [(f"{servers} سرور".translate(FA_DIGITS), "#2fe0cf", 140),
                 (f"{tools} ابزار".translate(FA_DIGITS), "#ffc23d", 140),
                 ("قیمت به تومان", "#ff5c8f", 186)]
        font, desc = PERSIAN, f"{servers} سرور MCP و {tools} ابزار برای ایجنت{ZWNJ}های هوش مصنوعی"
    else:
        anchor, tx = "start", card_x + 44
        subtitle = "The Iranian web, wired for AI agents."
        stats = [(f"{servers} servers", "#2fe0cf", 150), (f"{tools} tools", "#ffc23d", 140),
                 ("Toman prices", "#ff5c8f", 170)]
        font, desc = LATIN, f"{servers} MCP servers and {tools} tools that give AI agents the Iranian web"

    return frame(fa, h, desc, f"""<rect x="{tx - (490 if fa else 0)}" y="70" width="490" height="38" rx="19" fill="#000" fill-opacity="0.28" stroke="#fff" stroke-opacity="0.25"/>
  <text x="{tx + (-245 if fa else 245)}" y="95" text-anchor="middle" font-family="{MONO}" font-size="15" fill="#d9fff9">/plugin marketplace add sepehr071/awesome-iran-mcp</text>
  <text x="{tx}" y="196" text-anchor="{anchor}" font-family="{LATIN}" font-size="58" font-weight="800" fill="url(#ink)" letter-spacing="-1.5">awesome-iran-mcp</text>
  <text x="{tx}" y="250" text-anchor="{anchor}" font-family="{font}" font-size="25" fill="#fff" fill-opacity="0.92">{subtitle}</text>
  {pills(tx, stats, font, fa)}
  <text x="{tx}" y="396" text-anchor="{anchor}" font-family="{LATIN}" font-size="15" fill="#fff" fill-opacity="0.7">Claude Code plugins · Agent Skills · any MCP client</text>

  {tiles(catalog, panel_x + 36, 49, fa)}""")


# Release banner: version and the changelog's headline numbers, updated by hand each release.
# (figure, Persian figure, English line, Persian line, colour)
RELEASE = "v2.0"
HIGHLIGHTS = [
    ("+12", "+۱۲", "new servers", "سرور تازه", "#2fe0cf"),
    ("7", "۷", "new categories", "دستهٔ تازه", "#ffc23d"),
    ("10", "۱۰", "news sources", "منبع خبری", "#ff5c8f"),
    ("Same", "همان", "tools and parameters", "ابزارها و پارامترها", "#7c3aed"),
]


def release(fa: bool, catalog: list, h: int = H) -> str:
    servers, tools = len(catalog), sum(s["tool_count"] for s in catalog)
    card_x, panel_x = (650, 40) if fa else (40, 670)
    if fa:
        anchor, tx, font = "end", card_x + 590 - 44, PERSIAN
        title, subtitle, changes = "۱۲ سرور تازه", "قیمت، خبر، قانون و اپ", "همهٔ تغییرها: CHANGELOG.md"
        stats = [(f"{servers} سرور".translate(FA_DIGITS), "#2fe0cf", 140),
                 (f"{tools} ابزار".translate(FA_DIGITS), "#ffc23d", 140),
                 ("فقط خواندنی", "#ff5c8f", 170)]
        desc = f"awesome-iran-mcp {RELEASE}: " + "، ".join(f"{n} {fa_line}" for _, n, _, fa_line, _ in HIGHLIGHTS)
    else:
        anchor, tx, font = "start", card_x + 44, LATIN
        title, subtitle, changes = "12 new servers.", "Prices, news, law, apps.", "Full changelog: CHANGELOG.md"
        stats = [(f"{servers} servers", "#2fe0cf", 150), (f"{tools} tools", "#ffc23d", 140),
                 ("Read-only", "#ff5c8f", 150)]
        desc = f"awesome-iran-mcp {RELEASE}: " + ", ".join(f"{n} {en_line}" for n, _, en_line, _, _ in HIGHLIGHTS)

    out = []
    w, th, gap = 240, 164, 18
    for i, (num, fa_num, en_line, fa_line, color) in enumerate(HIGHLIGHTS):
        row, col = divmod(i, 2)
        if fa:
            col = 1 - col
        x, y = panel_x + 36 + col * (w + gap), 57 + row * (th + gap)
        nx, num, line = (x + w - 28, fa_num, fa_line) if fa else (x + 28, num, en_line)
        # figures stay left-to-right in both languages; under rtl, "start" is the right edge
        out.append(f"""<rect x="{x}" y="{y}" width="{w}" height="{th}" rx="26" fill="#fff" fill-opacity="0.10" stroke="#fff" stroke-opacity="0.28"/>
  <text x="{nx}" y="{y + 88}" text-anchor="{"end" if fa else "start"}" font-family="{LATIN}" font-size="60" font-weight="800" fill="{color}" letter-spacing="-1">{num}</text>
  <text x="{nx}" y="{y + 130}" text-anchor="start" direction="{"rtl" if fa else "ltr"}" font-family="{font}" font-size="18" font-weight="600" fill="#fff" fill-opacity="0.85">{line}</text>""")

    return frame(fa, h, desc, f"""<rect x="{tx - (220 if fa else 0)}" y="70" width="220" height="38" rx="19" fill="#000" fill-opacity="0.28" stroke="#fff" stroke-opacity="0.25"/>
  <text x="{tx + (-110 if fa else 110)}" y="95" text-anchor="middle" font-family="{MONO}" font-size="15" fill="#d9fff9">awesome-iran-mcp {RELEASE}</text>
  <text x="{tx}" y="186" text-anchor="{anchor}" font-family="{font}" font-size="58" font-weight="800" fill="url(#ink)" letter-spacing="{0 if fa else -1.5}">{title}</text>
  <text x="{tx}" y="240" text-anchor="{anchor}" font-family="{font}" font-size="30" font-weight="600" fill="#fff" fill-opacity="0.92">{subtitle}</text>
  {pills(tx, stats, font, fa)}
  <text x="{tx}" y="396" text-anchor="start" direction="{"rtl" if fa else "ltr"}" font-family="{font}" font-size="15" fill="#fff" fill-opacity="0.7">{changes}</text>

  {chr(10).join(out)}""")


def pills(tx: float, stats: list, font: str, fa: bool) -> str:
    out, x = [], tx
    for text, color, w in stats:
        if fa:
            x -= w
        out.append(pill(x, 300, w, text, font, color, fa))
        x = x + w + 14 if not fa else x - 14
    return "\n".join(out)


def frame(fa: bool, h: int, desc: str, body: str) -> str:
    """The shared canvas: background blobs and two glass panels (card with text, panel beside it).
    h > H centres it on a taller full-bleed canvas (GitHub social preview is 1280x640)."""
    oy, rx = (h - H) // 2, 28 if h == H else 0
    card_x, panel_x = (650, 40) if fa else (40, 670)
    return f"""<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" width="{W}" height="{h}" viewBox="0 0 {W} {h}" role="img" aria-labelledby="t d">
  <title id="t">awesome-iran-mcp</title>
  <desc id="d">{desc}</desc>
  {DEFS}

  <rect width="{W}" height="{h}" rx="{rx}" fill="url(#bg)"/>
  <g transform="translate(0 {oy})">
  <g clip-path="url(#frame)"><use href="#blobs" filter="url(#soft)" opacity="0.85"/></g>
  <clipPath id="frame"><rect y="{-oy}" width="{W}" height="{h}" rx="{rx}"/></clipPath>

  {glass("card", card_x, 30, 590, 400, 40)}
  {glass("panel", panel_x, 30, 570, 400, 40)}

  {body}
  </g>
</svg>
"""


def embed_fonts(svg: str) -> str:
    """GitHub shows SVGs as <img>, which can't load fonts, so subset Vazirmatn to the banner's text and inline it."""
    text = "".join(html.unescape(t) for t in re.findall(r"<text[^>]*>([^<]*)</text>", svg))
    faces = []
    for weight, style in WEIGHTS.items():
        font = TTFont(ROOT / "assets" / "fonts" / f"Vazirmatn-{style}.woff2", recalcTimestamp=False)  # stable bytes
        opts = subset.Options()
        opts.flavor, opts.layout_features, opts.hinting = "woff2", ["*"], False  # keep Persian joining forms
        sub = subset.Subsetter(opts)
        sub.populate(text=text)
        sub.subset(font)
        buf = io.BytesIO()
        font.save(buf)
        data = base64.b64encode(buf.getvalue()).decode()
        faces.append(
            f"@font-face{{font-family:Vazirmatn;font-weight:{weight};src:url(data:font/woff2;base64,{data}) format('woff2')}}"
        )
    return svg.replace("<defs>", f"<defs>\n    <style>{''.join(faces)}</style>", 1)


def main() -> None:
    catalog = json.loads((ROOT / "servers.json").read_text(encoding="utf-8"))
    servers, tools = len(catalog), sum(s["tool_count"] for s in catalog)
    for name, draw, fa, h in (("banner.svg", banner, False, H), ("banner.fa.svg", banner, True, H),
                              ("social.svg", banner, False, 640),
                              # versioned names: a new URL per release, so GitHub's image cache can't show the old one
                              (f"release-{RELEASE}.svg", release, False, H),
                              (f"release-{RELEASE}.fa.svg", release, True, H)):
        svg = embed_fonts(draw(fa, catalog, h))
        (ROOT / "assets" / name).write_text(svg, encoding="utf-8", newline="\n")
    print(f"banners written: {servers} servers, {tools} tools")


if __name__ == "__main__":
    main()
