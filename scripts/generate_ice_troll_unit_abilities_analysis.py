# -*- coding: utf-8 -*-
import json
from pathlib import Path

raw_path = Path("docs/ui_text/ice_troll_unit_abilities_raw.json")
data = json.loads(raw_path.read_text(encoding="utf-8"))

lines = ["# Аудит способностей войск, Лоа и призывов Ледяных троллей (31 способность)\n"]

for idx, item in enumerate(data, 1):
    aid = item['id']
    code = item['code']
    name = item['name']
    lvls = item['levels']
    hk = item['hotkey']
    unhk = item['unhotkey']
    holders = item['holders']
    fields = item['fields']
    
    lines.append(f"## {idx}. `{aid}` — {name}")
    lines.append(f"- **Код базы**: `{code}` | **Уровней**: {lvls} | **Горячая клавиша**: `{hk}` (отмена/авто: `{unhk}`)")
    lines.append(f"- **Носители**: {', '.join(holders) if holders else '—'}")
    
    for l in range(1, lvls + 1):
        sfx = str(l) if lvls > 1 or f'cool{l}' in fields else '1'
        c = fields.get(f'cool{sfx}', fields.get('cool', ''))
        m = fields.get(f'cost{sfx}', fields.get('cost', ''))
        d = fields.get(f'dur{sfx}', fields.get('dur', ''))
        hd = fields.get(f'herodur{sfx}', fields.get('herodur', ''))
        da = fields.get(f'dataa{sfx}', fields.get('dataa', ''))
        db = fields.get(f'datab{sfx}', fields.get('datab', ''))
        dc = fields.get(f'datac{sfx}', fields.get('datac', ''))
        dd = fields.get(f'datad{sfx}', fields.get('datad', ''))
        de = fields.get(f'datae{sfx}', fields.get('datae', ''))
        area = fields.get(f'area{sfx}', fields.get('area', ''))
        targ = fields.get(f'targs{sfx}', fields.get('targs', ''))
        cast = fields.get(f'cast{sfx}', fields.get('cast', ''))
        order = fields.get('order', '')
        orderon = fields.get('orderon', '')
        orderoff = fields.get('orderoff', '')
        lines.append(f"- **Механика L{l}**: Кулдаун: `{c}`с, Мана: `{m}`, Длит: `{d}`с (герои: `{hd}`с), Дальность: `{cast}`, Радиус: `{area}`")
        lines.append(f"  - Данные: `dataa={da}`, `datab={db}`, `datac={dc}`, `datad={dd}`, `datae={de}`")
        lines.append(f"  - Приказ: `{order}` (on: `{orderon}`, off: `{orderoff}`), Цели: `{targ}`")
        
    for ld in item['levels_data']:
        l = ld['level']
        lines.append(f"- **Текущий Tip L{l}**: `{ld['tip']}`")
        lines.append(f"- **Текущий Ubertip L{l}**: `{ld['ubertip']}`")
        if ld['untip'] or ld['unubertip']:
            lines.append(f"  - *Untip L{l}*: `{ld['untip']}`")
            lines.append(f"  - *Unubertip L{l}*: `{ld['unubertip']}`")
    lines.append("")

out_file = Path("docs/ui_text/ice_troll_unit_abilities_analysis.md")
out_file.write_text("\n".join(lines), encoding="utf-8")
print(f"Written analysis to {out_file}")
