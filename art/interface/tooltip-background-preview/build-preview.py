"""Review the single shared backdrop replacement without touching the map."""
from pathlib import Path
import base64
import hashlib
import json
import re
import sys
import zipfile
from PIL import Image

ROOT = Path(__file__).resolve().parents[3]
OUT = Path(__file__).resolve().parent
IMPORTED = '--imported' in sys.argv
html = (ROOT / '.cache/custom-ui-kit-before-clarification.html').read_text(encoding='utf-8')
match = re.search(r'const assets=(.*?), manifest=(.*?);\nconst safe=', html)
assert match
assets = json.loads(match.group(1))

def uri(path):
    return 'data:image/png;base64,' + base64.b64encode(Path(path).read_bytes()).decode()

# Reuse every original component. Only four examples receive the new backdrop.
for key in list(assets):
    if key.startswith('new-'):
        assets[key] = assets['old-' + key[4:]]
for name in ['welcome-panel', 'hud-board', 'tooltip', 'timer-chip']:
    for side in ['old', 'new']:
        assets[side + '-' + name] = uri(OUT / 'previews' / f'{side}-{name}.png')
assets['new-panel-background'] = uri(OUT / 'human-tooltip-background.png')
assets['old-panel-background'] = uri(OUT / 'original.png')
original = Image.open(OUT / 'original.png')
changed = Image.open(OUT / 'human-tooltip-background.png')
roundtrip = Image.open(ROOT / '.cache/tooltip-black-roundtrip.png')
assert original.size == changed.size == roundtrip.size == (64, 64)
assert original.getchannel('A').tobytes() == changed.getchannel('A').tobytes() == roundtrip.getchannel('A').tobytes()
assert changed.getextrema() == ((8, 8), (8, 8), (8, 8), (195, 195))
assert roundtrip.getextrema() == changed.getextrema()
manifest = {'status': 'imported_in_map' if IMPORTED else 'preview_only_not_imported',
            'original_game_path': 'UI/Widgets/ToolTips/Human/human-tooltip-background.blp',
            'original_rgba': [24,34,49,195], 'new_rgba': [8,8,8,195],
            'alpha_byte_identical_in_png_tga_blp': True,
            'files': [{'name':'panel-background', 'title':'Общая подложка — почти чёрная',
                       'frame':'ToolTipBackground → BoxedTextBackgroundTemplate / BoxedText',
                       'size':[64,64]}]}
html = html[:match.start()] + 'const assets=' + json.dumps(assets) + ', manifest=' + json.dumps(manifest, ensure_ascii=False) + ';\nconst safe=' + html[match.end():]
sections = "const sections=[['windows','Приветственное окно','Исходная рамка, кнопка и поле ссылки. Изменена только общая подложка.',welcome,''],['hud','Таблица игроков','Исходные рамка, иконки, полосы строк и переключатель.',board,'board-stage'],['hud','Таймеры','Та же подложка ToolTipBackground с исходной альфой.',timers,''],['hud','Подсказки','Та же замена в BoxedText. Золотая рамка сохранена.',tooltip,'']];"
html, count = re.subn(r'const sections=\[.*?\];\ndocument.getElementById', lambda _: sections + '\ndocument.getElementById', html, count=1, flags=re.S)
assert count == 1
html = html.replace('<title>23RaceForever · набор текстур интерфейса</title>', '<title>23RaceForever · чёрная подложка с исходной прозрачностью</title>')
html = html.replace('Один стиль для кастомных окон', 'Та же подложка, только чернее')
html = html.replace('Каменная планка, металлическая окантовка и приглушённая бирюзовая ткань из существующих текстур карты. Четырнадцать отдельных текстур для таблицы, таймеров, подсказок и приветственного окна.', 'Одна общая текстура: #182231 → #080808. Альфа сохранена побайтно: 195/255 (76,5% непрозрачности). Рамки, кнопки, логотип и остальные элементы исходные.')
html = html.replace('Окна и кнопки', 'Приветствие').replace('Файлы текстур · 14', 'Текстура 64 × 64')
html = html.replace('Материалы из кастомного интерфейса карты', 'Почти чёрный фон · та же прозрачность')
html = html.replace('../art/interface/custom-elements-preview/23raceforever-ui-textures.zip', '../art/interface/tooltip-background-preview/tooltip-background.zip')
html = html.replace('Скачать PNG + TGA', 'Скачать BLP + PNG + TGA')
html = html.replace('Готовые изображения', 'Одна текстура для общей подложки')
html = html.replace('Все фоны и окантовки уже находятся в файлах текстур. Надписи и игровые иконки в текстуры не запечены.', 'Исходная текстура 64 × 64 однотонная. Новая отличается только RGB; все 4096 значений альфы равны исходным. Рамка в неё не входит.')
html = html.replace('../art/interface/custom-elements-preview/textures/${file.name}.tga', '../art/interface/tooltip-background-preview/human-tooltip-background.tga')
html = re.sub(r'<div class="notice">.*?</div>', '<div class="notice">Это компоновка в браузере, не игровой скриншот. Слева исходная подложка, справа почти чёрная. Фон сцены намеренно заметен сквозь обе подложки. Переключите фон ниже, чтобы сравнить прозрачность. Карта, Lua и FDF не изменены.</div>', html, count=1, flags=re.S)
html = re.sub(r'<details>.*?</details>', '<details><summary>Что именно заменяется</summary><p class="legend"><code>UI/Widgets/ToolTips/Human/human-tooltip-background.blp</code></p><p class="legend"><code>BoxedTextBackgroundTemplate</code> использует ключ <code>ToolTipBackground</code>. От него созданы приветствие, таблица игроков, таймеры и подсказки BoxedText. Замена общей текстуры распространяется на использующие её элементы; фон кнопок и поля ввода — отдельные текстуры, они здесь сохранены исходными.</p><p class="legend">64 × 64, RGB: (24, 34, 49) → (8, 8, 8), альфа 195 → 195. Проверено также после кодирования в BLP.</p></details>', html, count=1, flags=re.S)
html = re.sub(r'<footer>.*?</footer>', '<footer>Файлы: <code>art/interface/tooltip-background-preview/</code>. В карту не импортировано. <a href="../art/interface/tooltip-background-preview/human-tooltip-background.blp" download>Скачать BLP отдельно</a>.</footer>', html, count=1, flags=re.S)
html = html.replace('</style>', '''
.stage{background:repeating-linear-gradient(28deg,#314536 0px,#314536 38px,#665e40 39px,#665e40 76px,#283d31 77px,#283d31 114px)}
body[data-scene="light"] .stage{background:#b5b2a6}
body[data-scene="checker"] .stage{background:repeating-conic-gradient(#bbbbbb 0% 25%,#555555 0% 50%) 50% / 36px 36px}
.scene-controls{display:flex;align-items:center;gap:10px;flex-wrap:wrap;margin:0 0 20px;color:#9bafb5}.scene-controls span{font-size:13px}
footer a{color:#9dd4d0}
</style>''')
html = html.replace('<div id="comparison">', '<div class="scene-controls"><span>Фон за подложкой:</span><button data-scene-choice="terrain">Земля и трава</button><button data-scene-choice="light">Светлый</button><button data-scene-choice="checker">Шахматный</button></div><div id="comparison">')
html = html.replace('</script>', "document.querySelectorAll('[data-scene-choice]').forEach(b=>b.onclick=()=>document.body.dataset.scene=b.dataset.sceneChoice);\n</script>")
destination = ROOT / 'diagnostics/custom-interface-textures-preview.html'
if IMPORTED:
    html = html.replace('Только превью · в карту не добавлено', 'Подложка сохранена в карту')
    html = html.replace('Карта, Lua и FDF не изменены.', 'Подложка импортирована в карту; Lua и FDF не изменены.')
    html = html.replace('В карту не импортировано.', 'Подложка импортирована по исходному пути текстуры.')
destination.write_text(html, encoding='utf-8')
(OUT / 'manifest.json').write_text(json.dumps(manifest, ensure_ascii=False, indent=2), encoding='utf-8')
(OUT / 'README.md').write_text('''# Общая подложка ToolTipBackground

Только превью. В карту не импортировано.

Исходник: UI/Widgets/ToolTips/Human/human-tooltip-background.blp.
Размер: 64×64. Цвет #182231 заменён на #080808. Альфа 195/255
сохранена побайтно в PNG, TGA и BLP; это 76,47% непрозрачности.
BLP проверен обратным декодированием: RGBA совпадает с подготовленным PNG.

Применение: общий ключ ToolTipBackground в BoxedTextBackgroundTemplate,
BoxedText и использующих его фреймах. Рамка ToolTipBorder, кнопки и поле
ввода не менялись. Стандартные подсказки, использующие тот же путь, также
могут получить замену при будущем импорте по исходному пути.

original.png сохранён для сравнения. previews/ содержит только браузерные
сборки рамки с подложкой, а не текстуры для импорта. Для импорта подготовлен
один файл human-tooltip-background.blp; решение об импорте ещё не принято.
''', encoding='utf-8')
if IMPORTED:
    readme = OUT / 'README.md'
    text = readme.read_text(encoding='utf-8').replace('Только превью. В карту не импортировано.', 'Подложка импортирована в карту по исходному пути текстуры.')
    text = text.replace('решение об импорте ещё не принято.', 'файл также зарегистрирован в war3map.imp.')
    readme.write_text(text, encoding='utf-8')
with zipfile.ZipFile(OUT / 'tooltip-background.zip', 'w', zipfile.ZIP_DEFLATED) as z:
    for name in ['human-tooltip-background.png', 'human-tooltip-background.tga', 'human-tooltip-background.blp', 'original.png', 'README.md', 'manifest.json']:
        z.write(OUT / name, name)
if IMPORTED:
    assert (ROOT / 'map.w3x/UI/Widgets/ToolTips/Human/human-tooltip-background.blp').read_bytes() == (OUT / 'human-tooltip-background.blp').read_bytes()
else:
    baseline=json.loads((ROOT / '.cache/custom-ui-map-baseline.json').read_text())
    assert all(hashlib.sha256((ROOT/path).read_bytes()).hexdigest()==sha for path,sha in baseline.items())
print('Shared backdrop PNG / TGA / BLP RGBA verified. Imported: ' + str(IMPORTED))
