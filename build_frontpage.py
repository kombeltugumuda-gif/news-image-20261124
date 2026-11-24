#!/usr/bin/env python3
"""Draw the 24 November 2026 world-news front page (1024 x 1024).

All words on the page are typeset here with real fonts (PIL), so no
headline can come out garbled: the AI picture is used only as the hero
photograph panel, labelled "Illustration" in its caption.
Writes entry.png next to this script.
"""
from PIL import Image, ImageDraw, ImageFont, ImageOps

W, H = 1024, 1024
PAD = 28
CW = W - 2 * PAD  # content width

PAPER = (253, 252, 247)
INK = (18, 18, 18)
RED = (178, 34, 34)
NAVY = (20, 48, 92)
GREEN = (0, 110, 70)
PURPLE = (122, 60, 140)
ORANGE = (150, 90, 0)
GREY = (90, 90, 90)
RULE = (200, 198, 190)

SERIF_B = "/usr/share/fonts/truetype/liberation/LiberationSerif-Bold.ttf"
SANS_B = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
SANS = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
SANS_I = "/usr/share/fonts/truetype/liberation/LiberationSans-Italic.ttf"


def font(path, size):
    return ImageFont.truetype(path, size)


def wrap(draw, text, fnt, width):
    """Greedy word wrap to the given pixel width."""
    lines, cur = [], ""
    for word in text.split():
        trial = (cur + " " + word).strip()
        if draw.textlength(trial, font=fnt) <= width:
            cur = trial
        else:
            if cur:
                lines.append(cur)
            cur = word
    if cur:
        lines.append(cur)
    return lines


def block(draw, lines, x, y, fnt, fill, step):
    """Draw lines top to bottom; return the y after the last line."""
    for line in lines:
        draw.text((x, y), line, font=fnt, fill=fill)
        y += step
    return y


# (kicker, colour, headline, body)
STORIES = [
    ("BUSINESS", GREEN,
     "Nvidia brings Huang back as CEO; shares jump 31%",
     "Jensen Huang returns to lead Nvidia after an independent "
     "investigation, reinstated by a unanimous board vote as shares "
     "surge more than 31% in a day."),
    ("EUROPE", ORANGE,
     "Lisbon votes on budget as unions strike",
     "Portugal's parliament holds the final vote on the 2027 budget as "
     "unions strike and rally outside, and a housing camp keeps its "
     "tents up until the vote."),
    ("MIDDLE EAST", NAVY,
     "Gaza's injured children flown to UK",
     "Critically injured children from Gaza are evacuated to Britain "
     "for treatment, as Israeli fire kills a Palestinian and Gaza's "
     "health crisis deepens."),
    ("WORLD", PURPLE,
     "UN chief calls for global AI rules in a year",
     "Guterres urges nations to agree a multilateral framework for AI "
     "risk management within a year, warning of \u2018the biggest "
     "transfer of power in the history of humankind\u2019."),
]


def main():
    img = Image.new("RGB", (W, H), PAPER)
    d = ImageDraw.Draw(img)
    d.rectangle([6, 6, W - 7, H - 7], outline=INK, width=4)

    y = 20
    # Masthead
    f_mast = font(SERIF_B, 62)
    mast = "THE WORLD TODAY"
    d.text(((W - d.textlength(mast, font=f_mast)) / 2, y), mast,
           font=f_mast, fill=INK)
    y += 76
    d.rectangle([PAD, y, W - PAD, y + 4], fill=RED)
    y += 12

    # Date strip
    f_date = font(SANS_B, 23)
    date_txt = "TUESDAY, 24 NOVEMBER 2026  \u2022  THE DAY IN WORLD NEWS"
    d.rectangle([PAD, y, W - PAD, y + 40], fill=INK)
    d.text(((W - d.textlength(date_txt, font=f_date)) / 2, y + 7),
           date_txt, font=f_date, fill=(255, 255, 255))
    y += 52

    # Hero photograph (AI illustration, cropped to fill)
    hero = Image.open("hero.png").convert("RGB")
    hero = ImageOps.fit(hero, (CW, 258), method=Image.LANCZOS)
    img.paste(hero, (PAD, y))
    d.rectangle([PAD, y, W - PAD, y + 258], outline=INK, width=2)
    y += 258 + 6
    f_cap = font(SANS_I, 14)
    cap = ("A court in China hands down a death sentence for passing "
           "state secrets to a foreign country.  Illustration.")
    d.text((PAD, y), cap, font=f_cap, fill=GREY)
    y += 24

    # Lead headline + deck
    f_head = font(SANS_B, 36)
    head = "CHINA SENTENCES OFFICIAL TO DEATH FOR SPY LEAKS"
    while d.textlength(head, font=f_head) > CW and f_head.size > 27:
        f_head = font(SANS_B, f_head.size - 1)
    d.text((PAD, y), head, font=f_head, fill=INK)
    y += 47
    f_deck = font(SANS, 19)
    deck = ("A Chinese court sentences a state official to death for "
            "leaking 100 intelligence reports \u2014 35 of them state "
            "secrets \u2014 to a foreign country.")
    y = block(d, wrap(d, deck, f_deck, CW), PAD, y, f_deck, INK, 25)
    y += 8
    d.line([PAD, y, W - PAD, y], fill=INK, width=2)
    y += 12

    # 2 x 2 story grid
    col_w = (CW - 24) // 2
    row_h = 130
    f_kick = font(SANS_B, 14)
    f_sh = font(SANS_B, 21)
    f_sb = font(SANS, 16)
    for i, (kick, color, sh, sb) in enumerate(STORIES):
        cx = PAD + (i % 2) * (col_w + 24)
        cy = y + (i // 2) * (row_h + 10)
        d.text((cx, cy), kick, font=f_kick, fill=color)
        y2 = block(d, wrap(d, sh, f_sh, col_w), cx, cy + 20,
                   f_sh, INK, 26)
        block(d, wrap(d, sb, f_sb, col_w), cx, y2 + 2,
              f_sb, (40, 40, 40), 20)
        if i % 2 == 0:
            d.line([cx + col_w + 12, cy, cx + col_w + 12, cy + row_h - 8],
                   fill=RULE, width=1)
    y += 2 * row_h + 10 + 6
    d.line([PAD, y, W - PAD, y], fill=INK, width=2)
    y += 10

    # South Korea strip
    f_strip = font(SANS, 17)
    strip = ("SOUTH KOREA \u2014  The education minister steps down over "
             "AI cheating regulations.")
    y = block(d, wrap(d, strip, f_strip, CW), PAD, y, f_strip, INK, 22)
    y += 10

    # Ticker
    f_tick = font(SANS_B, 15)
    tick = ("ALSO TODAY  \u2022  El Chapo Isidro to face trial in Mexico  "
            "\u2022  450 German schools get bomb threats by email  \u2022  "
            "Lahore tops world pollution list as AQI passes 500  \u2022  "
            "4.0 quake hits Pakistan near Afghan border  \u2022  O'Hare "
            "ground stop in Thanksgiving rush  \u2022  Bangladesh garment "
            "workers reject pay offer")
    tlines = wrap(d, tick, f_tick, CW - 16)
    th = len(tlines) * 20 + 14
    d.rectangle([PAD, y, W - PAD, y + th], fill=INK)
    ty = y + 7
    for ln in tlines:
        d.text((PAD + 8, ty), ln, font=f_tick, fill=(255, 255, 255))
        ty += 20
    y += th + 10

    # Footer
    f_foot = font(SANS, 13)
    foot = ("All stories reported on 24 November 2026.  Sources: Times "
            "of India, UN News, The Portugal Brief, AP.")
    d.text(((W - d.textlength(foot, font=f_foot)) / 2, y), foot,
           font=f_foot, fill=GREY)

    img.save("entry.png", format="PNG", optimize=True)
    print("saved entry.png", img.size)


if __name__ == "__main__":
    main()
