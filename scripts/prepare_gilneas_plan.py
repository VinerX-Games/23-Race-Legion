# -*- coding: utf-8 -*-
"""Prepare complete standardization plan and registries for Gilneas / Worgens race (Race 24)."""
import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))

from build_gilneas_plan_data import build_plan
import generate_gilneas_registries

def main():
    folder = ROOT / "docs/ui_text"
    folder.mkdir(parents=True, exist_ok=True)

    wts_updates, checks_def, categories = build_plan()

    plan_path = folder / "gilneas_plan.json"
    plan_data = {
        "race": "Gilneas / Worgens (Гилнеас)",
        "race_number": 24,
        "categories": categories,
        "wts_updates": {str(k): v for k, v in wts_updates.items()},
        "checks_def": checks_def
    }
    plan_path.write_text(json.dumps(plan_data, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"Saved {plan_path} with {len(wts_updates)} WTS updates.")

    # Generate JSON registries
    generate_gilneas_registries.main()

if __name__ == "__main__":
    main()
