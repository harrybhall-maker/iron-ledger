import sys
from PIL import Image, ImageDraw
out = sys.argv[1]
def icon(n):
    S = 1024
    im = Image.new('RGB', (S, S), sys.argv[2] if len(sys.argv) > 2 else '#B8441F'); d = ImageDraw.Draw(im)
    c = '#EDEEE7'; cy = S//2
    d.rounded_rectangle([300, cy-34, 724, cy+34], 20, fill=c)            # bar
    for x0, x1, h in [(196, 286, 420), (300, 372, 300)]:                 # plates
        d.rounded_rectangle([x0, cy-h//2, x1, cy+h//2], 26, fill=c)
        d.rounded_rectangle([S-x1, cy-h//2, S-x0, cy+h//2], 26, fill=c)
    d.rounded_rectangle([150, cy-60, 196, cy+60], 16, fill=c)            # collars
    d.rounded_rectangle([S-196, cy-60, S-150, cy+60], 16, fill=c)
    return im.resize((n, n), Image.LANCZOS)
for n in (180, 192, 512): icon(n).save(f'{out}/icon-{n}.png')
