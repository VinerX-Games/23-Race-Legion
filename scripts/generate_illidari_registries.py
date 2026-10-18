# -*- coding: utf-8 -*-
"""Generate standardized JSON category registries for Race 10: Illidari in docs/ui_text/

Outputs:
- docs/ui_text/illidari_selection.json
- docs/ui_text/illidari_buildings.json
- docs/ui_text/illidari_units.json
- docs/ui_text/illidari_heroes.json
- docs/ui_text/illidari_abilities.json
- docs/ui_text/illidari_research.json
- docs/ui_text/illidari_audit.json
"""
import json
from pathlib import Path
import sys

sys.stdout.reconfigure(encoding='utf-8')
ROOT = Path(__file__).resolve().parent.parent

def main():
    plan_path = ROOT / "docs/ui_text/illidari_plan.json"
    mapping_path = ROOT / "scripts/illidari_wts_mapping.json"
    out_dir = ROOT / "docs/ui_text"
    out_dir.mkdir(parents=True, exist_ok=True)

    plan = json.loads(plan_path.read_text(encoding="utf-8"))
    mapping = json.loads(mapping_path.read_text(encoding="utf-8"))
    wts_updates = {int(k): v for k, v in plan["wts_updates"].items()}

    # -------------------------------------------------------------
    # 1. illidari_selection.json
    # -------------------------------------------------------------
    sel_data = {
        "scope": "Иллидари (Illidari): подсказка выбора расы A0OK",
        "object": "A0OK",
        "variants": ["SD"],
        "hotkey": {
            "value": "C"
        },
        "levels": 1,
        "evidence": [
            "04_race_selection.lua: InitTrig_Race_Illidari фильтрует способность A0OK.",
            "При выборе создаются стартовые юниты, исследуются маркеры R07H, R0KZ, R0L0.",
            "Горячая клавиша C, создатель Escanor (Яхве), сложность 3/5 (Средняя), период «Легион»."
        ],
        "strings": [
            {
                "field": "name",
                "wts_id": 38887,
                "after": wts_updates[38887]
            },
            {
                "field": "tip1",
                "wts_id": 38888,
                "after": wts_updates[38888]
            },
            {
                "field": "ubertip1",
                "wts_id": 35180,
                "after": wts_updates[35180]
            }
        ]
    }
    (out_dir / "illidari_selection.json").write_text(json.dumps(sel_data, ensure_ascii=False, indent=2), encoding="utf-8")
    print("Wrote illidari_selection.json")

    # -------------------------------------------------------------
    # 2. illidari_buildings.json
    # -------------------------------------------------------------
    bld_entries = []
    for b_id, b_info in mapping["buildings"].items():
        hk = b_info.get("hotkey")
        hk_val = hk[1] if isinstance(hk, list) and len(hk) > 1 else (hk if isinstance(hk, str) else None)
        entry = {
            "id": b_id,
            "hotkey": hk_val,
            "strings": []
        }
        for field, f_data in b_info.items():
            if isinstance(f_data, list) and len(f_data) >= 1 and isinstance(f_data[0], int):
                sid = f_data[0]
                if sid in wts_updates:
                    entry["strings"].append({
                        "field": field,
                        "wts_id": sid,
                        "after": wts_updates[sid]
                    })
        bld_entries.append(entry)

    bld_data = {
        "scope": "Иллидари (Illidari): категория 1 — Здания (13 зданий)",
        "buildings_count": len(bld_entries),
        "variants": ["SD"],
        "buildings": bld_entries
    }
    (out_dir / "illidari_buildings.json").write_text(json.dumps(bld_data, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"Wrote illidari_buildings.json ({len(bld_entries)} buildings)")

    # -------------------------------------------------------------
    # 3. illidari_units.json
    # -------------------------------------------------------------
    unit_entries = []
    for u_id, u_info in mapping["units"].items():
        hk = u_info.get("hotkey")
        hk_val = hk[1] if isinstance(hk, list) and len(hk) > 1 else (hk if isinstance(hk, str) else None)
        entry = {
            "id": u_id,
            "hotkey": hk_val,
            "strings": []
        }
        for field, f_data in u_info.items():
            if isinstance(f_data, list) and len(f_data) >= 1 and isinstance(f_data[0], int):
                sid = f_data[0]
                if sid in wts_updates:
                    entry["strings"].append({
                        "field": field,
                        "wts_id": sid,
                        "after": wts_updates[sid]
                    })
        unit_entries.append(entry)

    unit_data = {
        "scope": "Иллидари (Illidari): категория 2 — Юниты (13 юнитов)",
        "units_count": len(unit_entries),
        "variants": ["SD"],
        "units": unit_entries
    }
    (out_dir / "illidari_units.json").write_text(json.dumps(unit_data, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"Wrote illidari_units.json ({len(unit_entries)} units)")

    # -------------------------------------------------------------
    # 4. illidari_heroes.json
    # -------------------------------------------------------------
    hero_entries = []
    for h_id, h_info in mapping["heroes"].items():
        hk = h_info.get("hotkey")
        hk_val = hk[1] if isinstance(hk, list) and len(hk) > 1 else (hk if isinstance(hk, str) else None)
        entry = {
            "id": h_id,
            "hotkey": hk_val,
            "strings": []
        }
        for field, f_data in h_info.items():
            if isinstance(f_data, list) and len(f_data) >= 1 and isinstance(f_data[0], int):
                sid = f_data[0]
                if sid in wts_updates:
                    entry["strings"].append({
                        "field": field,
                        "wts_id": sid,
                        "after": wts_updates[sid]
                    })
        hero_entries.append(entry)

    hero_data = {
        "scope": "Иллидари (Illidari): категория 3 — Герои (4 героя)",
        "heroes_count": len(hero_entries),
        "variants": ["SD"],
        "heroes": hero_entries
    }
    (out_dir / "illidari_heroes.json").write_text(json.dumps(hero_data, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"Wrote illidari_heroes.json ({len(hero_entries)} heroes)")

    # -------------------------------------------------------------
    # 5. illidari_abilities.json
    # -------------------------------------------------------------
    abil_entries = []
    for a_id, a_info in mapping["abilities"].items():
        hk = a_info.get("hotkey")
        hk_val = hk[1] if isinstance(hk, list) and len(hk) > 1 else (hk if isinstance(hk, str) else None)
        entry = {
            "id": a_id,
            "hotkey": hk_val,
            "strings": []
        }
        for field, f_data in a_info.items():
            if isinstance(f_data, list) and len(f_data) >= 1 and isinstance(f_data[0], int):
                sid = f_data[0]
                if sid in wts_updates:
                    entry["strings"].append({
                        "field": field,
                        "wts_id": sid,
                        "after": wts_updates[sid]
                    })
        if entry["strings"]:
            abil_entries.append(entry)

    abil_data = {
        "scope": "Иллидари (Illidari): категория 4 — Способности (39 способностей)",
        "abilities_count": len(abil_entries),
        "variants": ["SD"],
        "abilities": abil_entries
    }
    (out_dir / "illidari_abilities.json").write_text(json.dumps(abil_data, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"Wrote illidari_abilities.json ({len(abil_entries)} abilities)")

    # -------------------------------------------------------------
    # 6. illidari_research.json
    # -------------------------------------------------------------
    upg_entries = []
    for u_id, u_info in mapping["upgrades"].items():
        hk = u_info.get("hotkey1") or u_info.get("hotkey")
        hk_val = hk[1] if isinstance(hk, list) and len(hk) > 1 else (hk if isinstance(hk, str) else None)
        entry = {
            "id": u_id,
            "hotkey": hk_val,
            "strings": []
        }
        for field, f_data in u_info.items():
            if isinstance(f_data, list) and len(f_data) >= 1 and isinstance(f_data[0], int):
                sid = f_data[0]
                if sid in wts_updates:
                    entry["strings"].append({
                        "field": field,
                        "wts_id": sid,
                        "after": wts_updates[sid]
                    })
        upg_entries.append(entry)

    upg_data = {
        "scope": "Иллидари (Illidari): категория 5 — Исследования и маркеры (22 технологии)",
        "upgrades_count": len(upg_entries),
        "variants": ["SD"],
        "upgrades": upg_entries
    }
    (out_dir / "illidari_research.json").write_text(json.dumps(upg_data, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"Wrote illidari_research.json ({len(upg_entries)} upgrades)")

    # -------------------------------------------------------------
    # 7. illidari_audit.json
    # -------------------------------------------------------------
    audit_data = {
        "race": "Иллидари (Illidari)",
        "race_id": 10,
        "selection_ability": "A0OK",
        "objects_audit": {
            "buildings": {
                "count": 13,
                "ids": ["h0E9", "h0EA", "h0EB", "h0EC", "h0ED", "h0EE", "h0EF", "h0EG", "h0EH", "h0EM", "h0EN", "o01C", "h011"],
                "economy_building": {
                    "id": "h0EC",
                    "name": "Накопитель энергии",
                    "food_provided": 15,
                    "gold_income_per_25s": 40,
                    "verified_via": "53_economy.lua and unit ability stats"
                }
            },
            "units": {
                "count": 13,
                "ids": ["h0EI", "h0EJ", "o01A", "o01B", "o019", "h0EK", "h0EL", "n02O", "n02M", "n02N", "h04Y", "h04Z", "h050"]
            },
            "heroes": {
                "count": 4,
                "ids": ["H043", "E01W", "E024", "E025"],
                "names": {
                    "H043": "Маг Крови (Интеллект, дальний бой)",
                    "E01W": "Охотник на демонов (Ловкость, ближний бой)",
                    "E024": "Охотник «Месть» (Сила, ближний бой)",
                    "E025": "Охотник «Истребление» (Ловкость, ближний бой)"
                }
            },
            "abilities": {
                "count": 39,
                "total_wts_updated": len(plan["wts_updates"])
            },
            "researches": {
                "count": 22,
                "technologies": 19,
                "markers": 3,
                "mutually_exclusive_branches": {
                    "R099": "Приоритет Наги (W) — +4 урона, +20 скорости бега нагам",
                    "R09A": "Приоритет Эльфы (E) — +50 HP, +15% скорости боя эльфам/охотникам",
                    "R09B": "Приоритет Орки (R) — +10 урона оркам Скверны",
                    "trigger_enforcement": "Trig_flot1_Copy_2_Actions, Trig_arm1_Copy_2_Actions, Trig_arm1_Copy_2_Copy_Actions"
                },
                "markers_list": {
                    "R07H": "Маркер расы Иллидари",
                    "R0KZ": "Маркер Иллидари или Наги",
                    "R0L0": "Маркер Эльфы Крови или Иллидари"
                }
            }
        },
        "items_audit": {
            "race_specific_items": [],
            "status": "No race-specific shop items or inventory artifacts found in war3map.w3t for Illidari."
        },
        "messages_audit": {
            "race_specific_messages": [],
            "status": "No race-specific floating messages or game UI strings found in war3map.wts for Illidari."
        },
        "buffs_audit": {
            "custom_buffs": [],
            "standard_buffs_used": [
                "BEer", "Bena", "Bpxf", "Bblo", "Bfae", "Bcyc", "Bfro", "Bpoi", "Bdef", "BOac", "Bcri", "Bspe", "Bshs"
            ],
            "status": "All buffs used by Illidari abilities are standard Warcraft III engine buffs. No custom text modification required."
        },
        "total_wts_updates": len(plan["wts_updates"]),
        "total_checks": len(plan["checks_def"])
    }
    (out_dir / "illidari_audit.json").write_text(json.dumps(audit_data, ensure_ascii=False, indent=2), encoding="utf-8")
    print("Wrote illidari_audit.json")

if __name__ == "__main__":
    main()
