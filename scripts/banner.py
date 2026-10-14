"""Draw assets/banner.svg (English) and assets/banner.fa.svg (Persian) in a frosted-glass style.

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

# English name, Persian name, logo in assets/logos, inner padding (0 = logo fills the tile)
APPS = [
    ("Digikala", f"دیجی{ZWNJ}کالا", "digikala.png", 0),
    ("Snappfood", f"اسنپ{ZWNJ}فود", "snappfood.svg", 8),
    ("Okala", "اکالا", "okala.png", 0),
    ("Technolife", "تکنولایف", "technolife.png", 0),
    ("MasterKala", "مسترکالا", "masterkala.png", 0),
    ("Khanoumi", "خانومی", "khanoumi.png", 0),
    ("Asal Banoo", "عسل بانو", "asalbanoo.png", 0),
    ("Shopino", "شاپینو", "shopino.png", 0),
    ("Jabama", "جاباما", "jabama.png", 0),
    ("Otaghak", "اتاقک", "otaghak.png", 0),
    ("MrBilit", "مستربلیط", "mrbilit.svg", 0),
    ("Flytoday", f"فلای{ZWNJ}تودی", "flytoday.png", 0),
    ("Paziresh24", "پذیرش۲۴", "paziresh24.png", 0),
    ("Doctoreto", "دکترتو", "doctoreto.png", 0),
    ("ExirYab", "اکسیریاب", "exiryab.png", 0),
    ("Taaghche", "طاقچه", "taaghche.png", 0),
    ("Fidibo", "فیدیبو", "fidibo.png", 0),
    ("30book", f"سی{ZWNJ}بوک", "30book.png", 0),
    ("PayPing", f"پی{ZWNJ}پینگ", "payping.png", 0),
    ("Bale", "بله", "bale.png", 0),
    ("SwapWallet", f"سواپ{ZWNJ}ولت", "swapwallet.png", 0),
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


def logo(file: str) -> str:
    data = (ROOT / "assets" / "logos" / file).read_bytes()
    mime = "image/svg+xml" if file.endswith(".svg") else "image/png"
    return f"data:{mime};base64,{base64.b64encode(data).decode()}"


def icons(px: float, py: float, fa: bool) -> str:
    out = []
    size, pitch_x, pitch_y, cols = 64, 86, 94, 6
    full_rows, last_count = divmod(len(APPS), cols)
    for i, (en, fa_name, file, pad) in enumerate(APPS):
        row, col = divmod(i, cols)
        if fa:
            col = cols - 1 - col  # right to left
        # centre a short last row
        last_row_offset = (cols - last_count) * pitch_x / 2 if row == full_rows else 0
        x = px + col * pitch_x + (-last_row_offset if fa else last_row_offset)
        y = py + row * pitch_y
        label, font = (fa_name, PERSIAN) if fa else (en, LATIN)
        fit = "xMidYMid meet" if pad else "xMidYMid slice"
        out.append(f"""<clipPath id="c{i}"><rect x="{x}" y="{y}" width="{size}" height="{size}" rx="18"/></clipPath>
  <g filter="url(#iconlift)">
    <rect x="{x}" y="{y}" width="{size}" height="{size}" rx="18" fill="#fff"/>
    <image x="{x + pad}" y="{y + pad}" width="{size - 2 * pad}" height="{size - 2 * pad}" preserveAspectRatio="{fit}" clip-path="url(#c{i})" href="{logo(file)}"/>
    <rect x="{x}" y="{y}" width="{size}" height="{size / 2}" rx="18" fill="url(#gloss)"/>
    <rect x="{x + 0.5}" y="{y + 0.5}" width="{size - 1}" height="{size - 1}" rx="17.5" fill="none" stroke="#fff" stroke-opacity="0.45"/>
  </g>
  <text x="{x + size / 2}" y="{y + size + 16}" text-anchor="middle" font-family="{font}" font-size="12.5" font-weight="600" fill="#fff" fill-opacity="0.92">{label}</text>""")
    return "\n  ".join(out)


def banner(fa: bool, servers: int, tools: int, h: int = H) -> str:
    """h > H centres the banner on a taller full-bleed canvas (GitHub social preview is 1280x640)."""
    oy, rx = (h - H) // 2, 28 if h == H else 0
    card_x, panel_x = (650, 40) if fa else (40, 670)
    card_w, panel_w = 590, 570
    if fa:
        anchor, tx = "end", card_x + card_w - 44
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

    pills, x = [], tx
    for text, color, w in stats:
        if fa:
            x -= w
        pills.append(pill(x, 300, w, text, font, color, fa))
        x = x + w + 14 if not fa else x - 14

    return f"""<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" width="{W}" height="{h}" viewBox="0 0 {W} {h}" role="img" aria-labelledby="t d">
  <title id="t">awesome-iran-mcp</title>
  <desc id="d">{desc}</desc>
  {DEFS}

  <rect width="{W}" height="{h}" rx="{rx}" fill="url(#bg)"/>
  <g transform="translate(0 {oy})">
  <g clip-path="url(#frame)"><use href="#blobs" filter="url(#soft)" opacity="0.85"/></g>
  <clipPath id="frame"><rect y="{-oy}" width="{W}" height="{h}" rx="{rx}"/></clipPath>

  {glass("card", card_x, 30, card_w, 400, 40)}
  {glass("panel", panel_x, 30, panel_w, 400, 40)}

  <rect x="{tx - (490 if fa else 0)}" y="70" width="490" height="38" rx="19" fill="#000" fill-opacity="0.28" stroke="#fff" stroke-opacity="0.25"/>
  <text x="{tx + (-245 if fa else 245)}" y="95" text-anchor="middle" font-family="{MONO}" font-size="15" fill="#d9fff9">/plugin marketplace add sepehr071/awesome-iran-mcp</text>
  <text x="{tx}" y="196" text-anchor="{anchor}" font-family="{LATIN}" font-size="58" font-weight="800" fill="url(#ink)" letter-spacing="-1.5">awesome-iran-mcp</text>
  <text x="{tx}" y="250" text-anchor="{anchor}" font-family="{font}" font-size="25" fill="#fff" fill-opacity="0.92">{subtitle}</text>
  {chr(10).join(pills)}
  <text x="{tx}" y="396" text-anchor="{anchor}" font-family="{LATIN}" font-size="15" fill="#fff" fill-opacity="0.7">Claude Code plugins · Agent Skills · any MCP client</text>

  {icons(panel_x + 38, 46, fa)}
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
    for name, fa, h in (("banner.svg", False, H), ("banner.fa.svg", True, H), ("social.svg", False, 640)):
        svg = embed_fonts(banner(fa, servers, tools, h))
        (ROOT / "assets" / name).write_text(svg, encoding="utf-8", newline="\n")
    print(f"banners written: {servers} servers, {tools} tools")


if __name__ == "__main__":
    main()
