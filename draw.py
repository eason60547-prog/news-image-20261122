"""Draw the 22 November 2026 world-news front page to entry.png.

Pure PIL, deterministic: no randomness, no clock, no network.
Run:  python3 draw.py   -> writes entry.png (1024x1024) next to this file.
"""
import os
from PIL import Image, ImageDraw, ImageFont

W, H = 1024, 1024
PAPER = (247, 243, 232)
INK = (24, 24, 28)
NAVY = (18, 42, 76)
RED = (178, 34, 28)
TEAL = (14, 92, 96)
GOLD = (184, 134, 22)
GREY = (92, 92, 96)
LINE = (60, 60, 66)
SEA = (46, 108, 148)
SKY = (214, 230, 238)

FONT_DIR = "/usr/share/fonts/truetype/dejavu"
def font(name, size):
    path = os.path.join(FONT_DIR, name)
    try:
        return ImageFont.truetype(path, size)
    except OSError:
        return ImageFont.load_default()

F_TITLE = font("DejaVuSans-Bold.ttf", 58)
F_DATE = font("DejaVuSans-Bold.ttf", 30)
F_KICK = font("DejaVuSans-Bold.ttf", 21)
F_HEAD = font("DejaVuSans-Bold.ttf", 40)
F_SUB = font("DejaVuSans.ttf", 23)
F_BODY = font("DejaVuSans.ttf", 22)
F_PHEAD = font("DejaVuSans-Bold.ttf", 27)
F_PBODY = font("DejaVuSans.ttf", 20)
F_SMALL = font("DejaVuSans.ttf", 18)
F_FOOT = font("DejaVuSans-Bold.ttf", 19)

def wrap(draw, text, fnt, width):
    words, lines, cur = text.split(), [], ""
    for w in words:
        trial = (cur + " " + w).strip()
        if draw.textlength(trial, font=fnt) <= width:
            cur = trial
        else:
            if cur:
                lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines

def para(draw, x, y, text, fnt, width, fill=INK, gap=6):
    for line in wrap(draw, text, fnt, width):
        draw.text((x, y), line, font=fnt, fill=fill)
        y += fnt.size + gap
    return y

def rule(draw, x0, y, x1, wdt=2, fill=INK):
    draw.line([(x0, y), (x1, y)], fill=fill, width=wdt)

def panel(draw, x, y, w, h, kick, kick_fill, head, body, head_size=None):
    draw.rectangle([x, y, x + w, y + h], outline=LINE, width=2)
    draw.text((x + 16, y + 12), kick, font=F_KICK, fill=kick_fill)
    yy = y + 44
    yy = para(draw, x + 16, yy, head, F_PHEAD, w - 32, fill=INK, gap=4)
    para(draw, x + 16, yy + 4, body, F_PBODY, w - 32, fill=INK, gap=4)

def main():
    img = Image.new("RGB", (W, H), PAPER)
    d = ImageDraw.Draw(img)
    d.rectangle([6, 6, W - 7, H - 7], outline=INK, width=3)

    # ---- Masthead ----
    d.rectangle([6, 6, W - 7, 118], fill=NAVY)
    d.text((512, 16), "THE WORLD IN ONE DAY", font=F_TITLE,
           fill=(255, 255, 255), anchor="ma")
    d.text((512, 80), "SUNDAY  22  NOVEMBER  2026", font=F_DATE,
           fill=(255, 214, 90), anchor="ma")

    # ---- Lead story: Strait of Hormuz ----
    d.text((40, 138), "STRAIT OF HORMUZ  •  LEAD STORY", font=F_KICK, fill=RED)
    y = para(d, 40, 172, "Two tankers hit in the Strait of Hormuz",
             F_HEAD, 500, fill=INK, gap=4)
    y = para(d, 40, y + 6,
             "Torkel struck at the stern at 05:00 UTC and Arina in the "
             "engine room at 05:50 UTC on 21 November. No one was hurt.",
             F_SUB, 500, fill=INK, gap=5)
    y = para(d, 40, y + 8,
             "On 22 November Torkel was still burning. Bahrain has taken "
             "the attacks to the UN Security Council. The cause is "
             "disputed; claims the ships hit mines are unverified.",
             F_BODY, 500, fill=INK, gap=5)
    d.text((40, 500), "21 NOV  •  05:00 / 05:50 UTC  •  NO CASUALTIES",
           font=F_SMALL, fill=GREY)

    # Illustration: burning tanker at sea (right of lead text)
    ix0, iy0, ix1, iy1 = 576, 138, 984, 512
    d.rectangle([ix0, iy0, ix1, iy1], fill=SKY, outline=LINE, width=2)
    d.rectangle([ix0, 400, ix1, iy1], fill=SEA)
    d.rectangle([ix0, 396, ix1, 402], fill=(255, 255, 255))
    # tanker hull and deck
    d.rectangle([606, 330, 954, 396], fill=(52, 52, 56))
    d.rectangle([606, 330, 954, 344], fill=RED)
    d.rectangle([880, 268, 940, 330], fill=(220, 220, 214), outline=LINE)
    d.rectangle([896, 236, 924, 268], fill=(220, 220, 214), outline=LINE)
    # smoke
    for cx, cy, r in [(700, 210, 42), (742, 180, 52), (800, 200, 44),
                      (668, 250, 34), (836, 168, 38)]:
        d.ellipse([cx - r, cy - r, cx + r, cy + r], fill=(120, 120, 124))
    # flames at the stern
    for cx, cy, r, col in [(640, 300, 34, (255, 122, 26)),
                           (676, 316, 26, (255, 178, 44)),
                           (616, 322, 20, (255, 178, 44))]:
        d.ellipse([cx - r, cy - r, cx + r, cy + r], fill=col)
    d.text((780, 452), "TANKER TORKEL  •  STILL BURNING 22 NOV",
           font=F_SMALL, fill=(255, 255, 255), anchor="ma")
    d.text((780, 478), "STRAIT OF HORMUZ", font=F_SMALL,
           fill=(255, 255, 255), anchor="ma")

    rule(d, 40, 540, 984, 3)

    # ---- Second row ----
    panel(d, 40, 560, 462, 216, "CLIMATE  •  COP31", TEAL,
          "COP31 runs into overtime with no deal",
          "Talks extended past schedule and still no agreement. "
          "A draft text drops the fossil-fuel wording.")
    panel(d, 522, 560, 462, 216, "UKRAINE  •  DIPLOMACY", NAVY,
          "Zelenskyy seeks four-party talks",
          "Ukraine's president proposes talks with the US, Europe "
          "and Russia. A meeting has not yet taken place.")

    # ---- Third row ----
    panel(d, 40, 796, 462, 168, "PERU  •  EARTHQUAKE", RED,
          "Magnitude 6.7 quake strikes Peru",
          "A strong earthquake hit Peru on 20 November.")
    panel(d, 522, 796, 462, 168, "ALSO TODAY", GOLD,
          "Shenzhen talks; Sparta II hit at sea",
          "Three-party meeting in Shenzhen, 19 Nov. Cargo ship "
          "Sparta II attacked, 21 Nov.")

    # ---- Footer ----
    rule(d, 40, 976, 984, 2)
    d.text((512, 982), "22 NOVEMBER 2026  •  ALL TIMES UTC",
           font=F_FOOT, fill=GREY, anchor="ma")

    out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "entry.png")
    img.save(out, "PNG")
    print("wrote", out, img.size)

if __name__ == "__main__":
    main()
