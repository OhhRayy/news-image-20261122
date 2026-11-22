#!/usr/bin/env python3
"""Draw the Sunday Edition front page for 22 November 2026.

A single-page newspaper, 1024x1024, built from scratch with Pillow.
Six stories, all first reported on Sunday 22 November 2026.
Run:  python3 draw.py   -> writes entry.png next to this file.
"""

import textwrap
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

W, H = 1024, 1024
PAPER = (253, 252, 247)
INK = (17, 17, 17)
NAVY = (20, 33, 61)
RED = (178, 34, 34)
GREY = (90, 90, 90)
RULE = (180, 175, 160)
CARD_BG = (255, 255, 255)

SERIF_B = "/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf"
SERIF = "/usr/share/fonts/truetype/dejavu/DejaVuSerif.ttf"
SANS_B = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
SANS = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
SANS_O = "/usr/share/fonts/truetype/liberation/LiberationSans-Italic.ttf"


def font(path, size):
    return ImageFont.truetype(path, size)


F_MAST = font(SERIF_B, 58)
F_SUB = font(SANS_B, 21)
F_KICK = font(SANS_B, 17)
F_HEAD = font(SERIF_B, 30)
F_HEAD_SM = font(SERIF_B, 25)
F_BODY = font(SERIF, 20)
F_SRC = font(SANS_O, 16)
F_FOOT = font(SANS, 16)


def wrap(d, text, fnt, width):
    """Greedy word wrap using real pixel widths."""
    lines, cur = [], ""
    for word in text.split():
        trial = (cur + " " + word).strip()
        if d.textlength(trial, font=fnt) <= width:
            cur = trial
        else:
            if cur:
                lines.append(cur)
            cur = word
    if cur:
        lines.append(cur)
    return lines


def draw_story(d, x, y, w, h, kicker, headline, body, source,
               head_font=F_HEAD_SM, accent=RED):
    d.rounded_rectangle([x, y, x + w, y + h], radius=6,
                        fill=CARD_BG, outline=RULE, width=1)
    d.rectangle([x, y, x + 6, y + h], fill=accent)
    tx = x + 20
    tw = w - 40
    cy = y + 14
    d.text((tx, cy), kicker, font=F_KICK, fill=accent)
    cy += 26
    for ln in wrap(d, headline, head_font, tw):
        d.text((tx, cy), ln, font=head_font, fill=INK)
        cy += int(head_font.size * 1.18)
    cy += 4
    for ln in wrap(d, body, F_BODY, tw):
        d.text((tx, cy), ln, font=F_BODY, fill=INK)
        cy += 26
    d.text((tx, y + h - 26), source, font=F_SRC, fill=GREY)


def draw_strip(d, x, y, w, h, kicker, headline, body, source, accent=NAVY):
    """Short horizontal strip: kicker + headline on one line, body below."""
    d.rounded_rectangle([x, y, x + w, y + h], radius=6,
                        fill=CARD_BG, outline=RULE, width=1)
    d.rectangle([x, y, x + 6, y + h], fill=accent)
    tx = x + 20
    tw = w - 40
    f_head = font(SERIF_B, 24)
    d.text((tx, y + 10), kicker + "  —  ", font=F_KICK, fill=accent)
    kx = tx + d.textlength(kicker + "  —  ", font=F_KICK)
    d.text((kx, y + 8), headline, font=f_head, fill=INK)
    cy = y + 44
    for ln in wrap(d, body, F_BODY, tw):
        d.text((tx, cy), ln, font=F_BODY, fill=INK)
        cy += 25
    d.text((tx, y + h - 24), source, font=F_SRC, fill=GREY)


def main():
    img = Image.new("RGB", (W, H), PAPER)
    d = ImageDraw.Draw(img)

    # ---- Masthead ----
    d.rectangle([0, 0, W, 120], fill=NAVY)
    d.text((W // 2, 12), "THE WORLD IN ONE PAGE",
           font=F_MAST, fill=(255, 255, 255), anchor="ma")
    d.text((W // 2, 82), "SUNDAY EDITION  •  22 NOVEMBER 2026  •  SIX STORIES FIRST REPORTED TODAY",
           font=F_SUB, fill=(255, 214, 90), anchor="ma")

    # ---- Lead story: COP31 ----
    draw_story(
        d, 28, 132, 968, 188,
        "CLIMATE  —  ANTALYA, TURKIYE",
        "COP31 collapses with no deal",
        "Climate talks in Antalya ended without consensus: the draft "
        "\u201cAntalya Pact\u201d was not adopted after deadlock over "
        "fossil-fuel transition language and adaptation finance targets. "
        "Warming is now set to pass 1.5\u00b0C.",
        "Sources: WRI (Antalya, 22 Nov)  •  Reuters via Sowetan",
        head_font=F_HEAD, accent=RED)

    # ---- Row 1: Ukraine + Nepal ----
    draw_story(
        d, 28, 332, 476, 244,
        "WAR IN UKRAINE",
        "186 drones strike overnight",
        "Russia launched 186 drones from 18:00 Saturday, 72 jet-powered; "
        "161 were shot down, including 56 jet-powered. A five-storey "
        "block near Kyiv collapsed: 9 evacuated, at least 14 feared trapped.",
        "Sources: 112.ua, 22 Nov 09:12 EET  •  EuropeSays")
    draw_story(
        d, 520, 332, 476, 244,
        "SOUTH ASIA  —  NEW DELHI",
        "Nepal PM arrives in Delhi",
        "Balendra Shah begins a two-day state visit (22\u201323 Nov), his "
        "first bilateral trip abroad since taking office in March 2026. "
        "Talks with PM Modi on Monday; a delegation of about 35.",
        "Sources: IANS, New Delhi, 22 Nov  •  New Kerala")

    # ---- Row 2: Cricket + factory fire ----
    draw_story(
        d, 28, 588, 476, 244,
        "CRICKET  —  WELLINGTON",
        "India declare at 720/9",
        "Highest Test total ever in New Zealand, on day four at Basin "
        "Reserve \u2014 the first time all seven first partnerships passed "
        "50. KL Rahul 136, Rishabh Pant 128; NZ 119/2 at stumps, "
        "trailing by 233.",
        "Sources: GeoSuper / AFP, 22 Nov  •  ESPNcricinfo")
    draw_story(
        d, 520, 588, 476, 244,
        "INDONESIA  —  SERANG, BANTEN",
        "Candy factory fire: 3 dead",
        "Fire broke out at PT Fonusa Agung Mulia in Cikande on Saturday "
        "at 17:00. Officials said Sunday: 3 dead, 36\u201350 workers "
        "missing, 15 rescued including 4 injured; about 300 were inside.",
        "Sources: AP, 22 Nov  •  Reuters, 22 Nov")

    # ---- Bottom story: South Korea ----
    draw_strip(
        d, 28, 844, 968, 128,
        "SOUTH KOREA",
        "Education minister resigns over exam AI-cheating chaos",
        "Choi Kyo-jin stepped down; President Lee Jae Myung accepted the resignation on Sunday "
        "after Suneung exam chaos (550,000 students) and 111 suspected cheating cases.",
        "Sources: Korea JoongAng Daily, 22 Nov 06:18 UTC  •  TBS News",
        accent=NAVY)

    # ---- Footer ----
    d.text((W // 2, 986),
           "All six stories first reported Sunday 22 November 2026  •  Sources named on each story",
           font=F_FOOT, fill=GREY, anchor="ma")

    out = Path(__file__).resolve().parent / "entry.png"
    img.save(out, format="PNG")
    print(f"wrote {out}  {out.stat().st_size} bytes")


if __name__ == "__main__":
    main()
