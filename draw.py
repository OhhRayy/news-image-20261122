"""Draw the news-image-20261122 front page with PIL.

Build script only: it paints the 1024x1024 newspaper page for Sunday
22 November 2026 ("Morning Edition") and writes entry.png next to
itself. The entry program (main.py) only copies that file to the
output folder, so the graded runs are byte-identical by construction.

Six stories, all first reported on Sunday 22 November 2026:

1. BAHRAIN -- Iran's Revolutionary Guards fired missiles and drones
   at US military positions in Bahrain late on Saturday; Bahrain said
   on Sunday that a civilian industrial facility was hit and caught
   fire, no one was hurt, and air defences intercepted other attacks
   (Reuters / AFP).
2. COP31 -- climate talks in Antalya entered a second day of overtime
   on Sunday; a last-minute draft deal still fails to name fossil
   fuels, and nearly 200 nations must approve it at a closing session
   (Reuters).
3. INDONESIA -- rescuers searched on Sunday for 36 workers missing
   after a fire at a candy factory in Serang, west of Jakarta; 3
   killed, 4 hurt, 15 survived (AFP / Reuters).
4. NVIDIA -- the board will not bring back former chief Jensen Huang,
   who resigned over personal conduct; US Treasury chief Scott Bessent
   demanded answers on chip sales to China in a Sunday TV interview
   (FT / CNBC).
5. CAMBODIA -- first new mpox case in two and a half years, confirmed
   by the Health Ministry on Sunday; the patient tested positive on
   Friday and is in hospital (Xinhua).
6. CALIFORNIA -- record-high king tides run along the coast from
   Sunday to Thursday, with El Nino storms behind them; San Francisco's
   mayor urged residents to avoid non-essential travel (IANS / NWS).

Run:  python3 draw.py
"""

import math

from PIL import Image, ImageDraw, ImageFont

FONT_DIR = "/usr/share/fonts/truetype/dejavu"
SERIF_BOLD = f"{FONT_DIR}/DejaVuSerif-Bold.ttf"
SANS_BOLD = f"{FONT_DIR}/DejaVuSans-Bold.ttf"
SANS = f"{FONT_DIR}/DejaVuSans.ttf"

PAPER = (247, 243, 233)
CARD = (255, 255, 255)
INK = (20, 20, 20)
BODY = (58, 58, 58)
NAVY = (13, 34, 56)
DARK = (24, 40, 70)
GOLD = (198, 158, 38)
CRIMSON = (172, 32, 26)
TEAL = (14, 110, 110)
LEAF = (46, 118, 50)
EMBER = (228, 118, 28)
AMBER = (240, 186, 60)
MUTE = (110, 105, 92)
HAIRLINE = (198, 190, 172)
SKY = (140, 185, 220)
PALE_LEAF = (216, 232, 216)
PALE_GREY = (225, 230, 240)
PALE_ROSE = (240, 224, 220)
PALE_SKY = (214, 232, 244)
VIOLET = (112, 66, 150)

W = H = 1024


def font(path, size):
    return ImageFont.truetype(path, size)


def wrap(draw, text, fnt, max_w):
    """Greedy word wrap; every returned line fits max_w pixels."""
    lines, cur = [], ""
    for word in text.split(" "):
        trial = word if not cur else cur + " " + word
        if draw.textlength(trial, font=fnt) <= max_w:
            cur = trial
        else:
            if cur:
                lines.append(cur)
            cur = word
    if cur:
        lines.append(cur)
    return lines


def centred(draw, y, text, fnt, colour, x0=0, x1=W):
    w = draw.textlength(text, font=fnt)
    draw.text((x0 + (x1 - x0 - w) / 2, y), text, font=fnt, fill=colour)


# ---------------------------------------------------------------------------
# Emblems: one small flat picture per story, drawn with PIL primitives.
# ---------------------------------------------------------------------------

def emblem_missile(d, x, y, w, h):
    d.rectangle([x, y, x + w, y + h], fill=DARK)
    d.line([x + 16, y + 34, x + w - 40, y + h - 46], fill=CARD, width=3)
    d.line([x + 40, y + h - 40, x + w - 16, y + 50], fill=SKY, width=3)
    d.line([x + 76, y + 16, x + w - 76, y + 56], fill=CARD, width=3)
    cx, cy = x + w // 2, y + h // 2 + 12
    pts = []
    for i in range(24):
        r = 78 if i % 2 == 0 else 44
        a = math.pi * i / 12
        pts.append((cx + r * math.cos(a), cy + r * math.sin(a)))
    d.polygon(pts, fill=AMBER)
    d.ellipse([cx - 32, cy - 32, cx + 32, cy + 32], fill=EMBER)
    d.ellipse([cx - 17, cy - 17, cx + 17, cy + 17], fill=AMBER)
    d.ellipse([cx - 8, cy - 8, cx + 8, cy + 8], fill=CARD)


def emblem_globe(d, x, y, s):
    d.rectangle([x, y, x + s, y + s], fill=PALE_LEAF)
    cx, cy, r = x + s // 2, y + s // 2 + 2, 32
    d.ellipse([cx - r, cy - r, cx + r, cy + r], fill=LEAF, outline=INK, width=2)
    d.arc([cx - r, cy - r, cx + r, cy + r], 200, 340, fill=CARD, width=2)
    d.line([cx - 30, cy - 13, cx + 30, cy - 13], fill=CARD, width=2)
    d.line([cx - 32, cy + 3, cx + 32, cy + 3], fill=CARD, width=2)
    d.line([cx - 28, cy + 19, cx + 28, cy + 19], fill=CARD, width=2)
    d.line([cx, cy - r, cx, cy + r], fill=CARD, width=2)
    sx, sy = x + s - 22, y + 18
    d.ellipse([sx - 7, sy - 7, sx + 7, sy + 7], fill=EMBER)
    for i in range(8):
        a = 2 * math.pi * i / 8
        d.line(
            [sx + 10 * math.cos(a), sy + 10 * math.sin(a),
             sx + 15 * math.cos(a), sy + 15 * math.sin(a)],
            fill=EMBER, width=2,
        )


def emblem_factory(d, x, y, s):
    d.rectangle([x, y, x + s, y + s], fill=PALE_GREY)
    d.rectangle([x + 10, y + 44, x + 56, y + 70], fill=(90, 96, 104))
    d.rectangle([x + 56, y + 52, x + 76, y + 70], fill=(70, 76, 84))
    d.rectangle([x + 14, y + 26, x + 22, y + 44], fill=(70, 76, 84))
    d.ellipse([x + 12, y + 14, x + 24, y + 26], fill=(160, 166, 174))
    flame = [(x + 34, y + 46), (x + 28, y + 30), (x + 38, y + 36),
             (x + 42, y + 22), (x + 48, y + 36), (x + 56, y + 30),
             (x + 52, y + 46)]
    d.polygon(flame, fill=EMBER)
    d.polygon([(x + 38, y + 46), (x + 40, y + 36), (x + 46, y + 46)],
              fill=AMBER)
    d.rectangle([x + 8, y + 70, x + 78, y + 74], fill=INK)
    d.rectangle([x + 62, y + 58, x + 70, y + 66], fill=AMBER)


def emblem_chip(d, x, y, s):
    d.rectangle([x, y, x + s, y + s], fill=PALE_SKY)
    cx, cy = x + s // 2, y + s // 2
    for i in range(4):
        off = -24 + i * 16
        d.line([cx + off, y + 8, cx + off, y + 24], fill=INK, width=3)
        d.line([cx + off, y + s - 8, cx + off, y + s - 24], fill=INK, width=3)
        d.line([x + 8, cy + off, x + 24, cy + off], fill=INK, width=3)
        d.line([x + s - 8, cy + off, x + s - 24, cy + off], fill=INK, width=3)
    d.rectangle([cx - 26, cy - 26, cx + 26, cy + 26], fill=NAVY)
    d.rectangle([cx - 14, cy - 14, cx + 14, cy + 14], fill=TEAL)
    d.rectangle([cx - 5, cy - 5, cx + 5, cy + 5], fill=GOLD)


def emblem_virus(d, x, y, s):
    d.rectangle([x, y, x + s, y + s], fill=PALE_ROSE)
    cx, cy, r = x + s // 2, y + s // 2, 24
    for i in range(10):
        a = 2 * math.pi * i / 10
        ex, ey = cx + (r + 12) * math.cos(a), cy + (r + 12) * math.sin(a)
        d.line([cx + r * math.cos(a), cy + r * math.sin(a), ex, ey],
               fill=VIOLET, width=3)
        d.ellipse([ex - 4, ey - 4, ex + 4, ey + 4], fill=VIOLET)
    d.ellipse([cx - r, cy - r, cx + r, cy + r], fill=VIOLET)
    d.ellipse([cx - 12, cy - 14, cx + 2, cy + 0], fill=(150, 110, 185))
    d.ellipse([cx + 4, cy + 4, cx + 14, cy + 14], fill=(150, 110, 185))


def emblem_wave(d, x, y, s):
    d.rectangle([x, y, x + s, y + s], fill=(30, 90, 140))
    sx, sy = x + s - 24, y + 20
    d.ellipse([sx - 9, sy - 9, sx + 9, sy + 9], fill=AMBER)
    for i in range(8):
        a = 2 * math.pi * i / 8
        d.line([sx + 12 * math.cos(a), sy + 12 * math.sin(a),
                sx + 17 * math.cos(a), sy + 17 * math.sin(a)],
               fill=AMBER, width=2)
    for k, (base, col) in enumerate(((46, CARD), (58, SKY), (70, (190, 220, 240)))):
        pts = []
        for px in range(0, s + 1, 4):
            pts.append((x + px, y + base + 7 * math.sin(px / 14.0 + k * 1.6)))
        pts += [(x + s, y + s), (x, y + s)]
        d.polygon(pts, fill=col)


# ---------------------------------------------------------------------------
# Stories.
# ---------------------------------------------------------------------------

LEAD = {
    "tag": "MIDDLE EAST",
    "tag_colour": CRIMSON,
    "headline": "IRAN'S MISSILES HIT BAHRAIN",
    "body": ("Bahrain on Sunday condemned Iranian missile and drone "
             "strikes on US military positions. A civilian "
             "industrial facility was hit and caught fire; no one "
             "was hurt. Air defences intercepted other attacks."),
    "source": "Sources: Reuters, AFP - 22 Nov 2026",
}

CELLS = [
    {
        "tag": "CLIMATE", "colour": LEAF,
        "title": "COP31 TALKS DRAG INTO OVERTIME",
        "blurb": ("Climate talks in Antalya entered a second day of "
                  "overtime on Sunday. A last-minute draft deal still "
                  "fails to name fossil fuels."),
        "emblem": emblem_globe,
    },
    {
        "tag": "ASIA", "colour": EMBER,
        "title": "36 STILL MISSING AFTER FACTORY FIRE",
        "blurb": ("Rescuers in Indonesia searched on Sunday for 36 "
                  "workers missing after a fire at a candy factory in "
                  "Serang, west of Jakarta. Three were killed."),
        "emblem": emblem_factory,
    },
    {
        "tag": "TECH", "colour": TEAL,
        "title": "NVIDIA BOARD REJECTS HUANG COMEBACK",
        "blurb": ("Nvidia's board will not bring back former chief "
                  "Jensen Huang. US Treasury chief Scott Bessent "
                  "demanded answers on chip sales to China."),
        "emblem": emblem_chip,
    },
    {
        "tag": "HEALTH", "colour": VIOLET,
        "title": "MPOX BACK IN CAMBODIA AFTER 30 MONTHS",
        "blurb": ("Cambodia confirmed its first new mpox case in two "
                  "and a half years on Sunday; the patient is in "
                  "hospital."),
        "emblem": emblem_virus,
    },
]

STRIP = {
    "tag": "WEATHER", "colour": (30, 90, 140),
    "title": "CALIFORNIA BRACES FOR KING TIDES",
    "blurb": ("Record-high king tides run along California's coast from "
              "Sunday to Thursday, with El Nino storms behind them. "
              "San Francisco's mayor urged residents to avoid "
              "non-essential travel."),
    "emblem": emblem_wave,
}


def render_lead(d, x, y, w, h):
    d.rectangle([x, y, x + w, y + h], fill=CARD, outline=INK, width=2)
    emblem_missile(d, x + 12, y + 12, 272, h - 24)
    tx = x + 12 + 272 + 24
    tw = x + w - 12 - tx
    d.text((tx, y + 14), LEAD["tag"], font=font(SANS_BOLD, 20),
           fill=LEAD["tag_colour"])
    d.text((tx, y + 42), LEAD["headline"], font=font(SANS_BOLD, 36),
           fill=INK)
    by = y + 92
    for line in wrap(d, LEAD["body"], font(SANS, 19), tw):
        d.text((tx, by), line, font=font(SANS, 19), fill=BODY)
        by += 24
    d.text((tx, y + h - 26), LEAD["source"], font=font(SANS, 15), fill=MUTE)


def render_cell(d, x, y, w, h, art):
    d.rectangle([x, y, x + w, y + h], fill=CARD, outline=INK, width=2)
    art["emblem"](d, x + 12, y + 12, 88)
    tx = x + 12 + 88 + 12
    tw = x + w - 12 - tx
    d.text((tx, y + 12), art["tag"], font=font(SANS_BOLD, 18),
           fill=art["colour"])
    hy = y + 34
    for line in wrap(d, art["title"], font(SANS_BOLD, 24), tw):
        d.text((tx, hy), line, font=font(SANS_BOLD, 24), fill=INK)
        hy += 27
    by = hy + 6
    for line in wrap(d, art["blurb"], font(SANS, 17), tw):
        d.text((tx, by), line, font=font(SANS, 17), fill=BODY)
        by += 21


def render_strip(d, x, y, w, h, art):
    d.rectangle([x, y, x + w, y + h], fill=CARD, outline=INK, width=2)
    art["emblem"](d, x + 12, y + 12, 120)
    tx = x + 12 + 120 + 20
    tw = x + w - 12 - tx
    d.text((tx, y + 14), art["tag"], font=font(SANS_BOLD, 18),
           fill=art["colour"])
    d.text((tx, y + 38), art["title"], font=font(SANS_BOLD, 27), fill=INK)
    by = y + 74
    for line in wrap(d, art["blurb"], font(SANS, 18), tw):
        d.text((tx, by), line, font=font(SANS, 18), fill=BODY)
        by += 22


def build():
    img = Image.new("RGB", (W, H), PAPER)
    d = ImageDraw.Draw(img)

    # Masthead.
    d.rectangle([0, 0, W, 128], fill=NAVY)
    d.rectangle([0, 128, W, 132], fill=GOLD)
    centred(d, 22, "THE WORLD IN ONE PAGE", font(SERIF_BOLD, 58), CARD)
    centred(d, 86, "SUNDAY, 22 NOVEMBER 2026", font(SANS_BOLD, 30), GOLD)
    centred(d, 142, "Morning Edition - six stories from the world news "
                     "of Sunday 22 November 2026",
            font(SANS, 18), INK)

    # Lead story, then a 2x2 grid, then a full-width strip.
    render_lead(d, 32, 168, 960, 212)
    render_cell(d, 32, 394, 464, 200, CELLS[0])
    render_cell(d, 528, 394, 464, 200, CELLS[1])
    render_cell(d, 32, 608, 464, 200, CELLS[2])
    render_cell(d, 528, 608, 464, 200, CELLS[3])
    render_strip(d, 32, 818, 960, 144, STRIP)

    # Footer.
    d.line([32, 972, 992, 972], fill=HAIRLINE, width=2)
    centred(d, 982, "Morning Edition - stories as reported by 06:00 UTC, "
                     "Sunday 22 November 2026",
            font(SANS, 15), MUTE)
    centred(d, 1002, "Sources: Reuters, AFP, AP, Xinhua, FT, CNBC, IANS  |  "
                      "make.fun - news-image-20261122",
            font(SANS, 15), MUTE)
    return img


if __name__ == "__main__":
    build().save("entry.png", format="PNG", optimize=True)
    print("wrote entry.png")
