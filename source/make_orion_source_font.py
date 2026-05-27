import fontforge

font = fontforge.font()
font.fontname = "OrionSourceTruth"
font.familyname = "Orion Source Truth"
font.fullname = "Orion Source Truth"
font.encoding = "UnicodeFull"
font.em = 1000
font.ascent = 800
font.descent = 200

def rect(g, x1, y1, x2, y2):
    pen = g.glyphPen()
    pen.moveTo((x1, y1))
    pen.lineTo((x2, y1))
    pen.lineTo((x2, y2))
    pen.lineTo((x1, y2))
    pen.closePath()

def make_char(ch):
    g = font.createChar(ord(ch), ch)
    g.width = 650
    rect(g, 100, 0, 550, 700)
    rect(g, 180, 80, 470, 620)
    g.correctDirection()

for ch in "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789":
    make_char(ch)

space = font.createChar(ord(" "), "space")
space.width = 300

for ch in ".:-_/":
    make_char(ch)

font.generate("fonts/OrionSourceTruth.ttf")
font.generate("fonts/OrionSourceTruth.otf")
font.close()
