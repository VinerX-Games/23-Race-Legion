---
name: wc3-model-assets
description: Инспекция MDL/MDX моделей карты, текстур и компактных превью через существующий MDLxL CLI при работе с импортированными ассетами.
---

# Model assets

Use scripts/wc3_models.py. Configure model_cli/mdlxl_home in wc3.local.json or WC3_MODEL_CLI/MDLXL_HOME.

```powershell
python scripts/wc3_models.py info map.w3x/PeasantFemale.mdx
python scripts/wc3_models.py validate map.w3x/PeasantFemale.mdx --limit 5
python scripts/wc3_models.py textures map.w3x/PeasantFemale.mdx --limit 5
python scripts/wc3_models.py render map.w3x/PeasantFemale.mdx --out .cache/wc3/peasant-preview.png
```

The wrapper diagnoses models and writes separate previews, preserving source models. stdout is bounded; full JSON is saved. --no-casc cannot prove a missing standard texture. Check resolved texture paths: the external CLI may search neighboring maps.

Before editing or optimizing, read the external CLI help and MDLxL project instructions. Write a new output model; verify diagnostics, textures and rendered motion. Do not remove intentional motion merely to silence warnings. Consult MDLxL OptimizeXL documentation before changing repairs.

