"""Кандидаты в неиспользуемые импорты карты (модели и текстуры).

Импорт считается используемым, если его путь (без расширения) или имя файла встречается:
- в файлах карты war3map.* (object data, Skin, war3map.lua, WTS, w3i, wtg/wct) и txt/fdf/toc/slk импортов;
- в значениях всех полей всех объектов, включая стандартные значения игры (выгрузка HiveWE_cli, кэш
  в .cache/import_review/objdump_*.json) — ловит подмену файла, на который ссылается стандартный объект;
- в бинарнике используемой модели (до неподвижной точки, вместе с портретами используемых моделей).
Также используемыми считаются: вариации моделей декораций/разрушаемых (X0.mdx при ссылке на X),
неактивные DIS-иконки используемых иконок и файлы, путь которых есть в CASC игры (подмена ресурса).

Поиск по подстроке намеренно консервативен: лишнее совпадение оставляет файл, а не удаляет его.
Пути, целиком собранные в Lua из переменных, не видны (на 1.6.528 таких нет: имена иконок — литералы).

    python scripts/audit/unused_imports.py [--out .cache/import_review/candidates.json]
"""
import argparse
import json
import os
import re
import struct
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(Path(__file__).resolve().parent))
MAP = ROOT / 'map.w3x'
CACHE = ROOT / '.cache/import_review'
HIVEWE_CLI = r'F:\WARCRAFT III\WARCRAFT_SOFT\HiveWE\HiveWE_cli.exe'
WARCRAFT = 'F:/Games/Warcraft III'
OBJECT_TYPES = ('unit', 'item', 'ability', 'doodad', 'destructible', 'upgrade', 'buff')
MODELS = ('.mdx', '.mdl')
TEXTURES = ('.blp', '.dds', '.tga')
TEXT_EXT = ('.txt', '.fdf', '.toc', '.slk', '.j', '.ai')
# верхние папки стандартного архива игры: файл там без ссылок может подменять встроенный ресурс
STD_DIRS = {'textures', 'units', 'ui', 'terrainart', 'pathtextures', 'doodads', 'abilities', 'buildings',
            'objects', 'sharedmodels', 'environment', 'splats', 'replaceabletextures'}
ICON_DIRS = ('replaceabletextures/commandbuttons', 'replaceabletextures/passivebuttons',
             'replaceabletextures/commandbuttonsdisabled')


def norm(s):
    return re.sub(r'/+', '/', s.lower().replace('\\', '/'))


def key(rel):
    return norm(os.path.splitext(rel)[0])


def base(rel):
    return os.path.splitext(os.path.basename(rel))[0].lower()


def icon_root(name):
    """Неактивная иконка игры — «DIS» + имя активной: disbtnfoo → btnfoo, dispasfoo → pasfoo."""
    return name[3:] if name.startswith('dis') and len(name) > 6 else None


def blp_size(path):
    with open(path, 'rb') as f:
        h = f.read(20)
    if h[:4] == b'BLP1':
        return struct.unpack('<II', h[12:20])
    if h[:4] == b'BLP2':
        return struct.unpack('<II', h[8:16])
    return None


def mdx_textures(data):
    """Пути и replaceable id из чанка TEXS (MDX)."""
    out = []
    i = 4
    while i + 8 <= len(data):
        tag, size = data[i:i + 4], struct.unpack('<I', data[i + 4:i + 8])[0]
        if tag == b'TEXS':
            for j in range(i + 8, i + 8 + size, 268):
                rid = struct.unpack('<I', data[j:j + 4])[0]
                p = data[j + 4:j + 264].split(b'\0', 1)[0].decode('latin1')
                out.append({'path': p, 'replaceable': rid})
            break
        i += 8 + size
    return out


def cli(*args):
    for _ in range(3):
        r = subprocess.run([HIVEWE_CLI, *args], capture_output=True)
        try:
            return json.loads(r.stdout.decode('utf-8', 'replace'))
        except ValueError:
            pass
    raise RuntimeError('HiveWE_cli: ' + r.stderr.decode('utf-8', 'replace')[:300])


def object_values():
    """Все значения всех полей всех объектов (с учётом стандартных), одной строкой."""
    newest = max((MAP / f).stat().st_mtime for f in os.listdir(MAP) if f.startswith('war3map') and (MAP / f).is_file())
    out = []
    for typ in OBJECT_TYPES:
        cache = CACHE / f'objdump_{typ}.json'
        if cache.exists() and cache.stat().st_mtime >= newest:
            dump = json.loads(cache.read_text(encoding='utf-8'))
        else:
            cols = [f['column'] for f in cli('list-fields', '--map', str(MAP), '--type', typ,
                                              '--warcraft', WARCRAFT)['fields']]
            dump = cli('dump-objects', '--map', str(MAP), '--type', typ, '--fields', ','.join(cols),
                       '--max', '1000000', '--warcraft', WARCRAFT)
            cache.parent.mkdir(parents=True, exist_ok=True)
            cache.write_text(json.dumps(dump, ensure_ascii=False), encoding='utf-8')
        for o in dump['objects']:
            out.extend(str(v) for v in o.get('fields', {}).values())
    return '\n'.join(out)


def casc_paths():
    """Пути файлов игры без расширения и без слоёв (war3.w3mod:_hd.w3mod:_tilesets\\b.w3mod:… → путь)."""
    from wc3_casc import Casc
    return {os.path.splitext(norm(n).rsplit(':', 1)[-1])[0] for n in Casc(WARCRAFT).names}


def collect_files():
    files = []
    for r, ds, fs in os.walk(MAP):
        rel_dir = os.path.relpath(r, MAP)
        ds[:] = [d for d in ds if not d.startswith('_')]
        for f in fs:
            rel = os.path.normpath(os.path.join(rel_dir, f)).replace(os.sep, '/')
            if rel.startswith('war3map') or rel.startswith('_'):
                continue
            files.append(rel)
    return files


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--out', default=str(ROOT / '.cache/import_review/candidates.json'))
    args = ap.parse_args()

    files = collect_files()
    ext = lambda p: os.path.splitext(p)[1].lower()

    corpus = []
    for f in os.listdir(MAP):
        if f.startswith('war3map') and (MAP / f).is_file() and f not in (
                'war3map.wpm', 'war3map.shd', 'war3map.w3e', 'war3map.imp', 'war3map.mmp'):
            corpus.append((MAP / f).read_bytes())
    for rel in files:
        if ext(rel) in TEXT_EXT:
            corpus.append((MAP / rel).read_bytes())
    corpus = norm(b'\n'.join(corpus).decode('latin1') + '\n' + object_values())
    game = casc_paths()

    def referenced(rel, text):
        b = base(rel)
        return key(rel) in text or (len(b) >= 4 and b in text)

    assets = [p for p in files if ext(p) in MODELS + TEXTURES]
    used = {p for p in assets if referenced(p, corpus)}
    overrides = {p for p in assets if p not in used and key(p) in game}
    used |= overrides
    # вариации моделей декораций/разрушаемых: игра дописывает номер к пути из object data
    for p in assets:
        m = re.match(r'^(.*[a-z_ ])\d+$', key(p))
        if p not in used and ext(p) in MODELS and m and m.group(1) in corpus:
            used.add(p)

    # неподвижная точка: всё, на что ссылаются используемые модели, и портреты используемых моделей
    model_bin = {p: norm((MAP / p).read_bytes().decode('latin1')) for p in assets if ext(p) in MODELS}
    portraits = {p: re.sub(r'_portrait$', '', key(p)) for p in assets if re.search(r'_portrait\.md[xl]$', p, re.I)}
    scanned = set()
    while True:
        used_keys = {key(q) for q in used}
        for p, main_key in portraits.items():
            if p not in used and main_key in used_keys:
                used.add(p)
        new = [p for p in used if p in model_bin and p not in scanned]
        if not new:
            break
        text = '\n'.join(model_bin[p] for p in new)
        scanned.update(new)
        for p in assets:
            if p not in used and referenced(p, text):
                used.add(p)

    # неактивная иконка используется вместе с активной
    used_bases = {base(p) for p in used}
    for p in assets:
        r = icon_root(base(p))
        if p not in used and r and (r in used_bases or r in corpus):
            used.add(p)

    lower_index = {norm(p): p for p in files}
    by_base = {}
    for p in files:
        by_base.setdefault(os.path.basename(norm(p)), []).append(p)

    def resolve(tex_path):
        n = norm(tex_path)
        if not n:
            return None
        if n in lower_index:
            return lower_index[n]
        for alt in (os.path.splitext(n)[0] + e for e in TEXTURES):
            if alt in lower_index:
                return lower_index[alt]
        hits = by_base.get(os.path.basename(n))
        return hits[0] if hits and len(hits) == 1 else None

    cand_models = sorted(p for p in assets if ext(p) in MODELS and p not in used)
    cand_textures = {p for p in assets if ext(p) in TEXTURES and p not in used}

    models = []
    tex_users = {}
    for p in cand_models:
        data = (MAP / p).read_bytes()
        texs = []
        if ext(p) == '.mdx':
            for t in mdx_textures(data):
                rel = resolve(t['path'])
                texs.append({'path': t['path'], 'replaceable': t['replaceable'], 'file': rel,
                             'status': 'map' if rel else ('replaceable' if not t['path'] else 'game')})
                if rel in cand_textures:
                    tex_users.setdefault(rel, []).append(p)
        # другие кандидаты-модели, на которые ссылается эта (эмиттеры моделей)
        text = model_bin[p]
        refs = [q for q in cand_models if q != p and key(q) in text]
        portrait = bool(re.search(r'_portrait\.md[xl]$', p, re.I))
        models.append({'path': p, 'size': len(data), 'textures': texs, 'models': refs, 'portrait': portrait,
                       'std_dir': p.split('/')[0].lower() in STD_DIRS})
    # текстуры, на которые ссылаются кандидаты-модели, но которые не разрешились точным путём
    for p in cand_textures:
        if p in tex_users:
            continue
        b = base(p)
        for m in cand_models:
            if (len(b) >= 4 and b in model_bin[m]) or key(p) in model_bin[m]:
                tex_users.setdefault(p, []).append(m)

    cand_keys = {key(m['path']): m['path'] for m in models}
    for m in models:
        if m['portrait']:
            m['main'] = cand_keys.get(re.sub(r'_portrait$', '', key(m['path'])))

    textures = []
    for p in sorted(cand_textures):
        sz = blp_size(MAP / p) if ext(p) == '.blp' else None
        top = p.split('/')[0].lower()
        textures.append({'path': p, 'size': (MAP / p).stat().st_size, 'dims': list(sz) if sz else None,
                         'users': sorted(tex_users.get(p, [])),
                         'std_dir': top in STD_DIRS and not norm(p).startswith(ICON_DIRS),
                         'icon': icon_root(base(p))})

    out = Path(args.out)
    out.parent.mkdir(parents=True, exist_ok=True)
    result = {'models': models, 'textures': textures,
              'stats': {'assets': len(assets), 'used': len(used), 'std_overrides': len(overrides),
                        'cand_models': len(models), 'cand_models_mb': round(sum(m['size'] for m in models) / 1e6, 1),
                        'cand_textures': len(textures),
                        'cand_textures_mb': round(sum(t['size'] for t in textures) / 1e6, 1),
                        'textures_only_in_cand_models': sum(1 for t in textures if t['users']),
                        'orphan_textures': sum(1 for t in textures if not t['users'])}}
    out.write_text(json.dumps(result, ensure_ascii=False, indent=1), encoding='utf-8')
    print(json.dumps(result['stats'], ensure_ascii=False))


if __name__ == '__main__':
    main()
