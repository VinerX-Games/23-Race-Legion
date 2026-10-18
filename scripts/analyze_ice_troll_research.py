# -*- coding: utf-8 -*-
import json
from pathlib import Path

raw_path = Path("docs/ui_text/ice_troll_research_raw.json")
data = json.loads(raw_path.read_text(encoding="utf-8"))

lines = [f"# Аудит исследований расы Ледяных троллей ({len(data)} исследований)\n"]

for idx, item in enumerate(data, 1):
    qid = item['id']
    code = item['code']
    name = item['name']
    lvls = item['levels']
    hk = item['hotkey']
    researchers = item['researchers']
    consumers = item['consumers']
    fields = item['fields']
    
    lines.append(f"## {idx}. `{qid}` (база `{code}`, уровней: {lvls}, горячая клавиша: `{hk}`)")
    lines.append(f"- **Название**: `{name}`")
    lines.append(f"- **Где исследуется**: {', '.join(researchers) if researchers else '— (выдаётся триггером или маркер)'}")
    lines.append(f"- **Получатели (юниты)**: {', '.join(consumers) if consumers else '—'}")
    
    # Check effect fields: effect1..N, dataa1..N, datab1..N, etc.
    lines.append("- **Параметры эффектов**:")
    for l in range(1, lvls + 1):
        sfx = str(l)
        ef1 = fields.get(f'effect1', '')
        ef2 = fields.get(f'effect2', '')
        ef3 = fields.get(f'effect3', '')
        ef4 = fields.get(f'effect4', '')
        da1 = fields.get(f'dataa{sfx}', '')
        db1 = fields.get(f'datab{sfx}', '')
        dc1 = fields.get(f'datac{sfx}', '')
        dd1 = fields.get(f'datad{sfx}', '')
        gold = fields.get(f'gold{sfx}', fields.get('gold', ''))
        lumb = fields.get(f'lumb{sfx}', fields.get('lumb', ''))
        time = fields.get(f'time{sfx}', fields.get('time', ''))
        lines.append(f"  - Уровень {l}: золото={gold}, дерево={lumb}, время={time}с")
        lines.append(f"    - Эффекты: ef1={ef1}(base={fields.get('base1')}, mod={fields.get('mod1')}), ef2={ef2}(base={fields.get('base2')}, mod={fields.get('mod2')}), ef3={ef3}, ef4={ef4}")
        lines.append(f"    - Data: dataa={da1}, datab={db1}, datac={dc1}, datad={dd1}")
        
    for ld in item['levels_data']:
        l = ld['level']
        lines.append(f"- **Уровень {l}**: имя=`{ld['name']}`, tip=`{ld['tip']}`")
        lines.append(f"  - *ubertip*: `{ld['ubertip']}`")
    lines.append("")

out_file = Path("docs/ui_text/ice_troll_research_analysis.md")
out_file.write_text("\n".join(lines), encoding="utf-8")
print(f"Written analysis to {out_file}")
