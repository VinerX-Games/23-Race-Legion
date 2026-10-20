"""Иконки командной панели Warcraft III (BTN/PAS/DIS) в формате BLP1 с палитрой и мипмапами."""
import struct
from pathlib import Path

from PIL import Image, ImageEnhance

SIZE = 64
LIGHT, DARK, INNER = (200, 200, 204), (110, 110, 114), (35, 33, 25)


def _blend(pixel, color, alpha):
    return tuple(round(p * (1 - alpha) + c * alpha) for p, c in zip(pixel, color))


def button(art):
    """Рамка активной кнопки: чёрный контур, светлые верх/лево, тёмные низ/право, тёмная внутренняя линия."""
    image = art.copy()
    px = image.load()
    last = SIZE - 1
    for y in range(SIZE):
        for x in range(SIZE):
            edge = min(x, y, last - x, last - y)
            if edge == 0:
                px[x, y] = (0, 0, 0)
            elif edge <= 2:
                # В углах, где сходятся полосы, граница идёт по побочной диагонали.
                px[x, y] = LIGHT if x + y < last else DARK
            elif edge == 3:
                px[x, y] = INNER
    return image


def passive(art):
    """Пассивная кнопка: тёмная утопленная рамка, плавно переходящая в рисунок."""
    image = art.copy()
    px = image.load()
    last = SIZE - 1
    for y in range(SIZE):
        for x in range(SIZE):
            edge = min(x, y, last - x, last - y)
            if edge <= 2:
                px[x, y] = (0, 0, 0)
            elif edge <= 6:
                px[x, y] = _blend(px[x, y], (0, 0, 0), (7 - edge) / 5)
    return image


def disabled(image):
    gray = ImageEnhance.Color(image).enhance(0.15)
    return ImageEnhance.Brightness(gray).enhance(0.5)


def write_blp1(image, path):
    """BLP1 с палитрой без альфы — формат уже импортированных в карту иконок."""
    image = image.convert('RGB')
    quantized = image.quantize(colors=256, method=Image.Quantize.MEDIANCUT, dither=Image.Dither.NONE)
    palette = quantized.getpalette()[:768]
    palette += [0] * (768 - len(palette))
    levels, size = [], SIZE
    while size >= 1:
        level = image if size == SIZE else image.resize((size, size), Image.LANCZOS)
        levels.append(level.quantize(palette=quantized, dither=Image.Dither.NONE).tobytes())
        size //= 2
    header_size = 4 + 6 * 4 + 16 * 4 * 2 + 256 * 4
    offsets, sizes, pos = [], [], header_size
    for level in levels:
        offsets.append(pos)
        sizes.append(len(level))
        pos += len(level)
    offsets += [0] * (16 - len(offsets))
    sizes += [0] * (16 - len(sizes))
    bgra = b''.join(bytes((palette[i * 3 + 2], palette[i * 3 + 1], palette[i * 3], 0)) for i in range(256))
    # compression=1 (палитра), alphaBits=0, ширина, высота, pictureType=5, hasMipmaps=1
    blob = (b'BLP1' + struct.pack('<6I', 1, 0, SIZE, SIZE, 5, 1)
            + struct.pack('<16I', *offsets) + struct.pack('<16I', *sizes) + bgra + b''.join(levels))
    assert len(blob) == pos
    Path(path).parent.mkdir(parents=True, exist_ok=True)
    Path(path).write_bytes(blob)


def icon_set(source, name, root):
    """Записать BTN/PASBTN и их неактивные варианты в root; вернуть относительные пути."""
    art = Image.open(source).convert('RGB').resize((SIZE, SIZE), Image.LANCZOS)
    outputs = {
        f'ReplaceableTextures/CommandButtons/BTN{name}.blp': button(art),
        f'ReplaceableTextures/PassiveButtons/PASBTN{name}.blp': passive(art),
        f'ReplaceableTextures/CommandButtonsDisabled/DISBTN{name}.blp': disabled(button(art)),
        f'ReplaceableTextures/CommandButtonsDisabled/DISPASBTN{name}.blp': disabled(passive(art)),
    }
    for relative, image in outputs.items():
        write_blp1(image, Path(root) / relative)
    return list(outputs)
