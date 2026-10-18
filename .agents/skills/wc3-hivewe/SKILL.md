---
name: wc3-hivewe
description: Инспекция object data карты, пакетное чтение полей, дерево технологий, структурный diff и предварительная проверка изменений через HiveWE CLI.
---

# HiveWE object tools

Use scripts/wc3_hivewe.py with paths configured in wc3.local.json.

```powershell
python scripts/wc3_hivewe.py search "Работник" --limit 10
python scripts/wc3_hivewe.py bulk h014,h05U --fields name,hp,builds --limit 5
python scripts/wc3_hivewe.py tree h014 --depth 2
python scripts/wc3_hivewe.py describe "Алый Орден"
python scripts/wc3_hivewe.py validate-map --limit 10
python scripts/wc3_hivewe.py diff before-map after-map --limit 10
```

race lists objects; use tree/describe/bulk for training and research details. Bound output and select fields. Full JSON artifacts live in .cache/wc3.

transaction plan.json previews operations on staged object files; --apply records changes and a recovery journal. Close the map in HiveWE before writing, since a GUI save can overwrite external edits. recover journal.json rejects concurrent changes. Multi-file recovery is journaled, not one filesystem-atomic commit.

Use capabilities/raw for native commands including batch-edit --dry-run, safe-move --dry-run, pathing-path --portals and regions-coverage. Static pathing excludes dynamic trees/gates. validate-map checks object references; CASC asset existence needs separate validation. See docs/TOOLING_WORKFLOW.md.

The patched CLI supports validate-map --assets and WTS validation. For initial placed obstacles, use scripts/wc3_pathing.py path/islands: it overlays footprints on a temporary WPM; live gate/tree changes require an in-game check. The native patch and reproducible build are in patches/README.md.

