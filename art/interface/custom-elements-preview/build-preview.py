"""Package native UI material variants and build a standalone visual comparison."""
from pathlib import Path
from html import escape
import base64
import hashlib
import json
import zipfile
from PIL import Image

ROOT = Path(__file__).resolve().parents[3]
OUT = Path(__file__).resolve().parent
INPUT = ROOT / '.cache/custom-ui-inputs'

roles = {
    'hud-board': ('Таблица игроков', 'BoxedTextBackgroundTemplate → hudBoard', ['UI/MiniMapBorder.dds', 'UI/Console/Human/HumanUITile-InventoryCover.dds']),
    'timer-chip': ('Таймеры', 'BoxedTextBackgroundTemplate → hudChip[1..4]', ['UI/MiniMapBorder.dds']),
    'tooltip': ('Подсказки', 'BoxedText → доход, экономика, колонки и расы', ['UI/MiniMapBorder.dds']),
    'welcome-panel': ('Приветственное окно', 'BoxedTextBackgroundTemplate → welcome', ['UI/MiniMapBorder.dds', 'UI/Console/Human/HumanUITile-InventoryCover.dds']),
    'button-normal': ('Кнопка · обычная', 'ScriptDialogButton / EscMenuButtonTemplate', ['UI/ButtonBorder.dds']),
    'button-hover': ('Кнопка · наведение', 'ControlMouseOverHighlight', ['UI/ButtonBorder.dds']),
    'button-pressed': ('Кнопка · нажатая', 'ControlPushedBackdrop', ['UI/ButtonBorder.dds']),
    'button-disabled': ('Кнопка · недоступная', 'ControlDisabledBackdrop', ['UI/ButtonBorder.dds']),
    'editbox': ('Поле ссылки', 'EscMenuEditBoxTemplate → welcomeLink', ['UI/MiniMapBorder.dds']),
    'toggle': ('Переключатель таблицы', 'HudToggleFace', ['UI/ButtonBorder.dds']),
    'row-stripe': ('Полоса строки', 'HudStripe / Textures/white.blp', ['UI/Console/Human/HumanUITile-InventoryCover.dds']),
    'separator': ('Разделитель', 'HudStripe / Textures/white.blp', ['UI/MiniMapBorder.dds']),
    'panel-background': ('Общий фон', 'Материал для BackdropBackground', ['UI/Console/Human/HumanUITile-InventoryCover.dds']),
    'panel-edge': ('Общая рамка', 'Восьмисекционный BackdropEdgeFile', ['UI/MiniMapBorder.dds']),
}

def data(path):
    return 'data:image/png;base64,' + base64.b64encode(Path(path).read_bytes()).decode('ascii')

manifest = {'status': 'preview_only_not_imported', 'style': 'existing custom stone and metal, muted turquoise at -40% saturation',
            'common_material': 'art/interface/23raceforever-inventory-cover.png; plain cloth sample x=222,y=514,w=182,h=124',
            'files': []}
for name, (title, frame, sources) in roles.items():
    path = OUT / 'textures' / f'{name}.png'
    im = Image.open(path)
    im.save(path.with_suffix('.tga'), format='TGA', compression='tga_rle')
    assert im.mode == 'RGBA' and all(v > 0 and v & (v-1) == 0 for v in im.size)
    assert Image.open(path.with_suffix('.tga')).tobytes() == im.tobytes()
    manifest['files'].append({'name': name, 'title': title, 'frame': frame, 'size': list(im.size),
                              'formats': ['PNG', 'TGA'], 'sources_in_map': sources,
                              'png_sha256': hashlib.sha256(path.read_bytes()).hexdigest()})
(OUT / 'manifest.json').write_text(json.dumps(manifest, ensure_ascii=False, indent=2), encoding='utf-8')

readme = '''# 23RaceForever: варианты оформления кастомного интерфейса

Только отдельный набор для просмотра. В карту не импортирован; Lua/FDF не изменялись.

14 текстур в PNG и TGA (RGBA, размеры — степени двойки). TGA сохранены без потерь с RLE.
Основные материалы переиспользованы из UI/MiniMapBorder.dds, UI/ButtonBorder.dds и
текущего приглушённого бирюзового баннера. Верхняя каменная планка — из исходного
HumanUITile-InventoryCover.dds. Логотип в фоновые текстуры не запечён:
в приветственном окне он остаётся отдельным исходным изображением.

В HTML слева показана браузерная сборка текущих шаблонов из стандартных ресурсов
Human, извлечённых из установленной игры; справа — те же примеры с новым оформлением.
Это компоновка для выбора материалов, не скриншот запущенной игры. Данные таблицы
и таймеров демонстрационные. Неподключённые TasItemShop/TasButtonList не включены.

Состояния кнопок: normal, hover, pressed, disabled. Для hover до замены использовано
приближённое свечение, для остальных — реальные фон/рамка EscMenuButtonTemplate.
Восьмисекционная рамка panel-edge: L, R, T, B, TL, TR, BL, BR, каждая секция 16×16.
Текстуры целых панелей также сохранены отдельно для визуального сравнения.
При будущем подключении размерные панели лучше собирать из фона и рамки через FDF,
чтобы не растягивать толщину окантовки. Толщина и точный размер на экране требуют
проверки в игре после отдельного решения об импорте. Цвет текста и иконки не заменены.

manifest.json содержит назначение, размеры и источники. build-textures.ps1 и
build-preview.py воспроизводят набор, используя текущие материалы и извлечённые
исходники из .cache/custom-ui-inputs. До повторной сборки страницы проверяется
сохранность исходных файлов карты и архива по .cache/custom-ui-map-baseline.json.
'''
(OUT / 'README.md').write_text(readme, encoding='utf-8')

assets = {}
for name in roles:
    assets['new-' + name] = data(OUT / 'textures' / f'{name}.png')
    before = OUT / 'before' / f'{name}.png'
    if before.exists():
        assets['old-' + name] = data(before)
assets['logo'] = data(ROOT / '.cache/logo-preview.png')
for icon in ['units', 'cities', 'experience']:
    assets['icon-' + icon] = data(INPUT / f'icon-{icon}.png')
assets['old-panel-background'] = data(INPUT / 'ToolTipBackground.png')
assets['old-panel-edge'] = data(INPUT / 'ToolTipBorder.png')

html = r'''<!doctype html><html lang="ru"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>23RaceForever · набор текстур интерфейса</title>
<style>
:root{color-scheme:dark;--gold:#ebc56c;--text:#ced4da;--muted:#99adb5;--line:#304047;--accent:#76c1bd}*{box-sizing:border-box}body{margin:0;background:#10181c;color:#ecf0f2;font:15px/1.5 system-ui,sans-serif}main{max-width:1320px;margin:auto;padding:38px 28px 64px}header{display:flex;align-items:start;justify-content:space-between;gap:20px}.eyebrow{font-size:12px;letter-spacing:2px;color:var(--accent);text-transform:uppercase}h1{font-size:32px;line-height:1.2;margin:9px 0 13px;letter-spacing:-.7px}h2{font-size:21px;margin:0 0 5px}p{color:var(--muted);margin:0 0 14px}.status{padding:8px 14px;background:#19302f;border:1px solid #355653;border-radius:25px;color:#a4d4cb;white-space:nowrap;font-size:13px}.intro{max-width:820px}button,.download{border:1px solid #43585f;background:#1c2c33;border-radius:7px;color:#e7edef;padding:9px 14px;font:inherit;cursor:pointer;text-decoration:none}button:hover,.download:hover{border-color:var(--accent)}button.active{background:#276068;border-color:#87c6c5}.toolbar{display:flex;flex-wrap:wrap;gap:9px;align-items:center;margin:24px 0 28px;position:sticky;top:0;z-index:50;background:#10181cee;padding:12px 0;backdrop-filter:blur(10px)}.toolbar .download{margin-left:auto}.compare-header{display:grid;grid-template-columns:1fr 1fr;gap:20px;margin:0 0 12px}.compare-header>div{padding:12px 18px;border:1px solid var(--line);border-radius:8px;background:#162127}.compare-header strong{display:block}.compare-header small{color:var(--muted)}.compare-header .after strong{color:var(--accent)}.section{margin:0 0 34px}.section-description{font-size:13px;margin-bottom:12px}.pair{display:grid;grid-template-columns:1fr 1fr;gap:20px}.stage{position:relative;min-height:240px;padding:26px;display:flex;align-items:center;justify-content:center;border:1px solid var(--line);border-radius:10px;background:radial-gradient(ellipse at 45% 30%,#263932,#152326 68%);overflow:hidden}.board-stage{align-items:start;min-height:455px}.ui{font-family:Georgia,'Times New Roman',serif;color:#ced4da;text-shadow:1px 1px 2px #000;background-repeat:no-repeat;background-size:100% 100%}.ui strong,.ui .title{color:#ebc56c;font-weight:normal}.ui-panel{padding:22px 18px}.board{width:100%;max-width:450px;min-height:385px;padding:22px 20px}.board-head,.row{display:grid;grid-template-columns:minmax(110px,1fr) 54px 54px 54px;align-items:center;gap:5px}.board-head{margin-bottom:10px;height:30px}.board-head .name{display:flex;align-items:center;gap:8px}.board-head img{width:25px;height:25px;margin:auto}.row{height:40px;padding:0 5px;font-size:16px}.row>span:not(:first-child){text-align:center;color:#fff}.player{white-space:nowrap}.dot{display:inline-block;width:9px;height:9px;margin-right:7px;background:var(--player);box-shadow:0 1px 3px #000}.sep{height:5px;margin:12px 0 8px;background-size:100% 100%}.board-foot{font-size:12px;color:#b99d66;padding-top:12px}.toggle{border:0;width:27px;height:27px;padding:0;background-color:transparent;background-size:100% 100%;color:#fff;text-shadow:1px 1px 2px #000;font-family:Georgia;font-size:18px;border-radius:0}.timer-stack{display:grid;gap:14px;max-width:330px;width:100%}.chip{height:48px;display:flex;align-items:center;justify-content:center;gap:14px;font-size:17px}.chip b{color:#fff;font-weight:normal}.tip{width:100%;max-width:450px;min-height:205px;padding:24px;font-size:17px}.tip .title{font-size:20px;margin-bottom:14px}.tip .label{color:#b99d66}.tip p{font:inherit;color:#ced4da;margin:10px 0}.tip .white{color:white}.tip .gold{color:#ebc56c}.tip .positive{color:#c8e087}.welcome{width:100%;max-width:450px;min-height:492px;padding:28px 26px;text-align:center}.welcome-logo{width:240px;max-width:90%;height:auto;filter:drop-shadow(0 2px 4px #000);margin:4px auto 18px}.welcome h3{font-size:19px;font-weight:normal;color:var(--gold);margin:0 0 16px}.welcome p{font:16px/1.5 Georgia;color:#ced4da;text-align:left;margin-bottom:18px}.welcome .version{font-size:14px;margin:18px 0}.entry{width:100%;padding:11px 15px;color:#fff;font:16px Georgia;border:0;outline:none;text-shadow:1px 1px 2px #000;background-color:transparent;background-size:100% 100%;height:47px}.game-button{border:0;border-radius:0;background-color:transparent;background-size:100% 100%;width:184px;height:46px;color:#ebc56c;font:18px Georgia;text-shadow:1px 1px 3px #000;cursor:pointer;padding:0}.game-button:disabled{color:#849095;cursor:default}.states{display:grid;grid-template-columns:1fr 1fr;gap:20px}.state{text-align:center}.state small{display:block;color:#aebfc4;margin-top:8px}.states .game-button{width:180px;max-width:100%}.form-stage{min-height:170px;display:block}.form-stage label{display:block;color:#b99d66;font-family:Georgia;margin:12px 0 7px}.section[data-category=details] .stage{min-height:150px}.samples{width:100%}.stripe-example{height:36px;padding:5px 12px;background-size:100% 100%;font:16px Georgia;color:#fff}.single-panel .old-stage{display:none}.single-panel .pair{grid-template-columns:1fr}.single-panel .compare-header{grid-template-columns:1fr}.single-panel .compare-header .before{display:none}.notice{padding:15px 18px;border-left:3px solid #688e8e;background:#17252b;color:#b7c8ce;font-size:13px;margin:26px 0}.gallery{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:16px}.tile{border:1px solid var(--line);border-radius:9px;background:#162127;padding:16px;min-width:0}.tile-name{font-weight:600}.tile-code{color:var(--muted);font:12px ui-monospace,monospace;margin:4px 0 12px;overflow-wrap:anywhere}.texture-preview{height:175px;display:flex;align-items:center;justify-content:center;background:repeating-conic-gradient(#10191e 0% 25%,#18252b 0% 50%) 50%/16px 16px;border:1px solid #263941;border-radius:5px}.texture-preview img{max-width:100%;max-height:100%;object-fit:contain}.tile a{color:#9dd4d0;font-size:13px;margin-right:12px}.tile-meta{font-size:12px;color:var(--muted);margin:10px 0}details{margin-top:26px;border-top:1px solid var(--line);padding-top:18px}summary{cursor:pointer;color:#c6dadc}table{border-collapse:collapse;width:100%;font-size:13px;margin-top:15px}td,th{text-align:left;padding:10px;border-bottom:1px solid #293d45}td{color:#acbfc5}code{font-size:12px;color:#9dd4d0;overflow-wrap:anywhere}footer{margin-top:32px;color:#8fa5af;font-size:13px}.gallery-view{display:none}.hidden{display:none!important}.legend{margin-top:18px;font-size:13px}.legend b{color:var(--gold);font-weight:normal}@media(max-width:1040px){.states{grid-template-columns:1fr}.stage{padding:17px}.board{padding:22px 14px}.row{font-size:14px}.board-head,.row{grid-template-columns:minmax(85px,1fr) 42px 42px 42px}.gallery{grid-template-columns:1fr 1fr}}@media(max-width:740px){main{padding:24px 12px}.pair{grid-template-columns:1fr}.compare-header{grid-template-columns:1fr}.compare-header .before{display:none}header{display:block}.status{display:inline-block;margin-top:10px}.toolbar .download{margin-left:0}.old-stage:before{content:'ДО';position:absolute;top:9px;left:12px;font:11px system-ui;color:#8ca2aa;letter-spacing:2px}.new-stage:before{content:'НОВОЕ';position:absolute;top:9px;left:12px;font:11px system-ui;color:#8fc7c2;letter-spacing:2px}.stage{padding:28px 15px}.gallery{grid-template-columns:1fr}.board-stage{min-height:440px}h1{font-size:27px}.states{grid-template-columns:1fr 1fr}}
</style></head><body><main>
<header><div><div class="eyebrow">23RaceForever / материалы интерфейса</div><h1>Один стиль для кастомных окон</h1><p class="intro">Каменная планка, металлическая окантовка и приглушённая бирюзовая ткань из существующих текстур карты. Четырнадцать отдельных текстур для таблицы, таймеров, подсказок и приветственного окна.</p></div><div class="status">Только превью · в карту не добавлено</div></header>
<div class="toolbar"><button class="active" data-view="all">Все элементы</button><button data-view="hud">Таблица и таймеры</button><button data-view="windows">Окна и кнопки</button><button data-view="gallery">Файлы текстур · 14</button><button id="mode">Только новое</button><a class="download" href="../art/interface/custom-elements-preview/23raceforever-ui-textures.zip" download>Скачать PNG + TGA</a></div>
<div id="comparison"><div class="compare-header"><div class="before"><strong>До</strong><small>Текущие стандартные материалы Human</small></div><div class="after"><strong>Новая текстура</strong><small>Материалы из кастомного интерфейса карты</small></div></div>
<div id="sections"></div></div>
<div class="gallery-view" id="gallery"><h2>Готовые изображения</h2><p>Все фоны и окантовки уже находятся в файлах текстур. Надписи и игровые иконки в текстуры не запечены.</p><div class="gallery" id="tiles"></div></div>
<div class="notice">Это браузерная компоновка для сравнения материалов, а не скриншот игры. Текст и значения показаны как пример. Слева использованы реальные стандартные фоновые текстуры и рамки из установленной Warcraft III; свечение наведения приближено. Подключение к Lua/FDF и импорт в карту не выполнялись.</div>
<details><summary>Назначение текстур и использованные материалы</summary><table><thead><tr><th>Элемент</th><th>Точка применения</th><th>Размер</th></tr></thead><tbody id="mapping"></tbody></table><p class="legend">Источники: <code>UI/MiniMapBorder.dds</code>, <code>UI/ButtonBorder.dds</code> и ткань баннера с насыщенностью <b>−40%</b>. Верхняя каменная планка взята из исходной текстуры баннера. Для изменяемого размера сохранены общий фон и восьмисекционная рамка FDF. Тёмная ткань выбрана для читаемости текста.</p><p class="legend">Тексты, иконки юнитов/рас и ресурсы сохранены. Неиспользуемые шаблоны TasItemShop и TasButtonList в этот набор не включены.</p></details>
<footer>Набор находится в <code>art/interface/custom-elements-preview/</code>. PNG и TGA без потерь, RGBA. Архив карты и исходные Lua/FDF не изменены.</footer>
</main><script>
const assets=__ASSETS__, manifest=__MANIFEST__;
const safe=s=>String(s).replace(/[&<>"']/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]));
function bg(v,name){return `style="background-image:url('${assets[v+'-'+name]}')"`}
function icon(name){return `<img src="${assets['icon-'+name]}" alt="${{units:'Юниты',cities:'Города',experience:'Опыт'}[name]}">`}
function board(v){let names=['Игрок 1','Игрок 2','Игрок 3','Игрок 4','Игрок 5'],colors=['#ff0303','#0042ff','#1ce6b9','#540081','#fffc01'];return `<div class="ui board" ${bg(v,'hud-board')}><div class="board-head"><div class="name"><button class="toggle" ${bg(v,'toggle')} aria-label="Свернуть таблицу">−</button><strong>Игроки: 5</strong></div>${icon('units')}${icon('cities')}${icon('experience')}</div>${names.map((name,i)=>`<div class="row" ${i%2===0?bg(v,'row-stripe'):''}><span class="player"><i class="dot" style="--player:${colors[i]}"></i>${name}</span><span>${[32,25,40,18,29][i]}</span><span>${[12,9,15,6,10][i]}%</span><span>${[180,124,205,87,153][i]}</span></div>`).join('')}<div class="sep" ${bg(v,'separator')}></div><div class="row"><span>Всего</span><span>144</span><span>52%</span><span>749</span></div><div class="board-foot">Названия, цвет игроков и значения — отдельный текст.</div></div>`}
function timers(v){return `<div class="timer-stack"><div class="ui chip" ${bg(v,'timer-chip')}><strong>Доход</strong><b>00:18</b></div><div class="ui chip" ${bg(v,'timer-chip')}><strong>Таймер</strong><b>03:42</b></div></div>`}
function tooltip(v){return `<div class="ui tip" ${bg(v,'tooltip')}><div class="title">Доход</div><p><span class="label">Следующее начисление:</span> <span class="white">00:18</span></p><p><span class="label">Золото:</span> <span class="white">+125</span></p><p>Подсказки экономики, рас и заголовков таблицы используют общую рамку и тёмную подложку.</p></div>`}
function button(v,state,text='Закрыть'){return `<button class="game-button" ${bg(v,'button-'+state)} ${state==='disabled'?'disabled':''} data-side="${v}" data-base="${state}">${text}</button>`}
function entry(v){return `<input class="entry" ${bg(v,'editbox')} value="discord.gg/UV5tbXXunU" readonly aria-label="Ссылка на Discord">`}
function welcome(v){return `<div class="ui welcome" ${bg(v,'welcome-panel')}><img class="welcome-logo" src="${assets.logo}" alt="23RaceForever"><h3>Добро пожаловать в 23 RACE: FOREVER!</h3><p>Поддержкой и обновлениями в данный момент занимаются: <strong>VinerX</strong> и <strong>Ageron</strong>.<br><br>Вступайте в наш дискорд-сервер по 23 расам:</p>${entry(v)}<p class="version"><span style="color:#b99d66">Версия карты:</span> <span style="color:white">1.6.515</span></p>${button(v,'normal')}</div>`}
function states(v){return `<div class="states">${[['normal','Обычная'],['hover','Наведение'],['pressed','Нажатая'],['disabled','Недоступная']].map(([state,label])=>`<div class="state">${button(v,state)}<small>${label}</small></div>`).join('')}</div>`}
function form(v){return `<div class="samples"><label>Ссылка на сервер</label>${entry(v)}</div>`}
function details(v){return `<div class="samples"><div class="stripe-example" ${bg(v,'row-stripe')}>Чередующаяся строка таблицы</div><div class="stripe-example">Следующая строка таблицы</div><div class="sep" ${bg(v,'separator')}></div><div style="display:flex;align-items:center;gap:12px;margin-top:16px"><button class="toggle" ${bg(v,'toggle')} aria-label="Свернуть">−</button><span class="ui">Кнопка сворачивания</span></div></div>`}
const sections=[['hud','Таблица игроков','Тёмная ткань, каменная верхняя планка, общий металлический контур.',board,'board-stage'],['hud','Таймеры','Компактная рамка без тяжёлой каменной планки.',timers,''],['hud','Подсказки','Единое оформление для дохода, экономики, рас и колонок.',tooltip,''],['windows','Приветственное окно','Логотип, текст и содержимое поля остаются отдельными элементами.',welcome,''],['windows','Кнопка в четырёх состояниях','Наведи курсор на кнопку «Закрыть» в окне выше, чтобы проверить смену текстур.',states,''],['windows','Поле ввода','Утопленный тёмный фон и тонкая рамка в стиле остального интерфейса.',form,'form-stage'],['details','Строки, разделитель и переключатель','Материалы для мелких элементов таблицы.',details,'']];
document.getElementById('sections').innerHTML=sections.map(([category,title,description,render,cl])=>`<section class="section" data-category="${category}"><h2>${title}</h2><p class="section-description">${description}</p><div class="pair"><div class="stage old-stage ${cl}">${render('old')}</div><div class="stage new-stage ${cl}">${render('new')}</div></div></section>`).join('');
document.getElementById('tiles').innerHTML=manifest.files.map(file=>`<article class="tile"><div class="tile-name">${safe(file.title)}</div><div class="tile-code">${safe(file.name)}</div><div class="texture-preview"><img src="${assets['new-'+file.name]}" alt="${safe(file.title)}"></div><div class="tile-meta">${file.size.join(' × ')} · RGBA</div><a href="${assets['new-'+file.name]}" download="${file.name}.png">PNG</a><a href="../art/interface/custom-elements-preview/textures/${file.name}.tga" download>TGA</a></article>`).join('');
document.getElementById('mapping').innerHTML=manifest.files.map(file=>`<tr><td>${safe(file.title)}</td><td><code>${safe(file.frame)}</code></td><td>${file.size.join(' × ')}</td></tr>`).join('');
let single=false;
document.getElementById('mode').onclick=e=>{single=!single;document.getElementById('comparison').classList.toggle('single-panel',single);e.currentTarget.textContent=single?'До / после рядом':'Только новое'};
document.querySelectorAll('[data-view]').forEach(btn=>btn.onclick=()=>{document.querySelectorAll('[data-view]').forEach(b=>b.classList.toggle('active',b===btn));const view=btn.dataset.view;document.getElementById('gallery').style.display=view==='gallery'?'block':'none';document.getElementById('comparison').style.display=view==='gallery'?'none':'block';document.getElementById('mode').style.display=view==='gallery'?'none':'';document.querySelectorAll('.section').forEach(s=>s.classList.toggle('hidden',view!=='all'&&s.dataset.category!==view));});
document.querySelectorAll('.welcome .game-button').forEach(btn=>{const v=btn.dataset.side;const set=s=>btn.style.backgroundImage=`url('${assets[v+'-button-'+s]}')`;btn.onmouseenter=()=>set('hover');btn.onmouseleave=()=>set('normal');btn.onmousedown=()=>set('pressed');btn.onmouseup=()=>set('hover');});
</script></body></html>'''
html = html.replace('__ASSETS__', json.dumps(assets)).replace('__MANIFEST__', json.dumps(manifest, ensure_ascii=False))
destination = ROOT / 'diagnostics/custom-interface-textures-preview.html'
destination.write_text(html, encoding='utf-8')

archive = OUT / '23raceforever-ui-textures.zip'
with zipfile.ZipFile(archive, 'w', compression=zipfile.ZIP_DEFLATED) as z:
    for path in sorted((OUT / 'textures').iterdir()):
        z.write(path, 'textures/' + path.name)
    z.write(OUT / 'README.md', 'README.md')
    z.write(OUT / 'manifest.json', 'manifest.json')

baseline = json.loads((ROOT / '.cache/custom-ui-map-baseline.json').read_text())
changed = [path for path, value in baseline.items() if hashlib.sha256((ROOT / path).read_bytes()).hexdigest() != value]
assert not changed, 'Map files changed during preview creation: ' + repr(changed)
print(json.dumps({'html': str(destination), 'textures': len(roles), 'formats': ['PNG', 'TGA'],
                  'archive': str(archive), 'map_and_source_files_unchanged': len(baseline)}, ensure_ascii=False, indent=2))
