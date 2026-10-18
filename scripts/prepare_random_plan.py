# -*- coding: utf-8 -*-
"""Prepare complete standardization plan and registries for Race 37: Random (Случайная раса)."""
import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))

def main():
    folder = ROOT / "docs/ui_text"
    folder.mkdir(parents=True, exist_ok=True)

    wts_updates = {}
    checks_def = []

    # =========================================================================
    # 1. RACE SELECTION: A12Q
    # =========================================================================
    # A12Q: Случайная раса (F)
    wts_updates[24728] = "|cffe4cfa3Случайная раса|r"
    wts_updates[24729] = "|cffe4cfa3Случайная раса|r (|cffffffffF|r)"
    wts_updates[25197] = (
        "|cffa6afb8РАСА:|r |cffced4daВыбирает одну случайную игровую расу из всех доступных вариантов на карте.|n|n"
        "|cffa6afb8Особенность:|r |cffced4daПодходит для игроков, готовых адаптироваться к любой стратегии и ветке развития.|r"
    )
    checks_def.append({"type": "ability", "id": "A12Q", "field": "name", "expected": wts_updates[24728]})
    checks_def.append({"type": "ability", "id": "A12Q", "field": "tip1", "expected": wts_updates[24729]})
    checks_def.append({"type": "ability", "id": "A12Q", "field": "ubertip1", "expected": wts_updates[25197]})

    # Selection registry
    selection_registry = {
        "race": "Random",
        "race_name_ru": "Случайная раса",
        "selection_ability": "A12Q",
        "strings": {
            "24728": {"field": "name", "text": wts_updates[24728]},
            "24729": {"field": "tip1", "text": wts_updates[24729]},
            "25197": {"field": "ubertip1", "text": wts_updates[25197]}
        }
    }
    (folder / "random_selection.json").write_text(json.dumps(selection_registry, ensure_ascii=False, indent=2), encoding="utf-8")

    # Audit registry
    audit_registry = {
        "race": "Random",
        "race_name_ru": "Случайная раса",
        "categories": {
            "buildings": "Не применимо: у случайного выбора отсутствуют собственные здания.",
            "units": "Не применимо: у случайного выбора отсутствуют собственные юниты.",
            "heroes": "Не применимо: у случайного выбора отсутствуют собственные герои.",
            "abilities": "Единственная способность — кнопка выбора A12Q.",
            "research": "Не применимо: у случайного выбора отсутствуют собственные исследования.",
            "items_messages_interfaces": "Не применимо: отсутствуют собственные предметы, сообщения и фреймы."
        }
    }
    (folder / "random_audit.json").write_text(json.dumps(audit_registry, ensure_ascii=False, indent=2), encoding="utf-8")

    # Master plan
    master_plan = {
        "race": "Random",
        "race_name_ru": "Случайная раса",
        "race_id": 37,
        "wts_updates": {str(k): v for k, v in wts_updates.items()},
        "checks_def": checks_def
    }
    (folder / "random_plan.json").write_text(json.dumps(master_plan, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"Prepared Random plan: {len(wts_updates)} WTS strings, {len(checks_def)} checks.")

if __name__ == '__main__':
    main()
