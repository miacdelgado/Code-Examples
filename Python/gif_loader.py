__import__('os').system('pip install -qq Pillow')
from PIL import Image, ImageDraw, ImageColor

BORDER = ImageColor.getrgb('#7654B4')
CANVAS = ImageColor.getrgb('#3B1D98')
INK = ImageColor.getrgb('#967ECB')
F = 10  

def compute_state(old):
    state = [[0 for _ in range(27)] for _ in range(27)]
    for x in range(1, 26):
        for y in range(1, 26):
            total = sum(old[x-1][y-1:y+2])
            total += old[x][y-1] + old[x][y+1]
            total += sum(old[x+1][y-1:y+2])
            if total & 1:
                state[x][y] = 1
    return state

def draw_slide(state, step):
    image = Image.new('RGB', (27*F, 27*F), BORDER)
    draw = ImageDraw.Draw(image)
    draw.rectangle((1*F, 1*F, 26*F, 26*F), CANVAS)
    draw.text((0, 0), str(step))
    for x in range(1, 26):
        for y in range(1, 26):
            if state[x][y]:
                draw.rectangle((x*F, y*F, (x+1)*F, (y+1)*F), INK)
    return image


state = [[0 for _ in range(27)] for _ in range(27)]
state[13][13] = 1
slides = [draw_slide(state, 0)]
for step in range(1, 32):
    state = compute_state(state)
    slides.append(draw_slide(state, step))

slides[0].save('animate.png', format='gif', save_all=True, append_images=slides[1:], optimize=True, duration=1000, loop=1)
