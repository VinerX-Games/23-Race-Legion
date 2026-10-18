# -*- coding: utf-8 -*-
"""Generate standardized JSON category registries for Race 24: Gilneas / Worgens (Гилнеас) in docs/ui_text/

Outputs:
- docs/ui_text/gilneas_selection.json
- docs/ui_text/gilneas_buildings.json
- docs/ui_text/gilneas_units.json
- docs/ui_text/gilneas_heroes.json
- docs/ui_text/gilneas_abilities.json
- docs/ui_text/gilneas_research.json
- docs/ui_text/gilneas_audit.json
"""
import json
from pathlib import Path
import sys

sys.stdout.reconfigure(encoding='utf-8')
ROOT = Path(__file__).resolve().parent.parent

def main():
    plan_path = ROOT / "docs/ui_text/gilneas_plan.json"
    dump_path = ROOT / "scripts/gilneas_raw_dump.json"
    out_dir = ROOT / "docs/ui_text"
    out_dir.mkdir(parents=True, exist_ok=True)

    plan = json.loads(plan_path.read_text(encoding="utf-8"))
    dump = json.loads(dump_path.read_text(encoding="utf-8"))
    wts_updates = {int(k): v for k, v in plan["wts_updates"].items()}

    def parse_str_id(raw):
        if isinstance(raw, str) and raw.startswith("TRIGSTR_"):
            try:
                return int(raw[8:])
            except ValueError:
                return None
        return None

    # -------------------------------------------------------------
    # 1. gilneas_selection.json
    # -------------------------------------------------------------
    sel_data = {
        "scope": "Гилнеас (Gilneas / Worgens): подсказка выбора расы A121 и маркеры",
        "object": "A121",
        "variants": ["SD"],
        "hotkey": {
            "value": "A"
        },
        "levels": 1,
        "evidence": [
            "04_race_selection.lua: InitTrig_Race_Gilneas регистрирует способность A121.",
            "При выборе создаются 5 рабочих h0IT (Постройщик), исследуется маркер R0FX, удаляется выбирающий юнит.",
            "Горячая клавиша A, создатель Escanor (Яхве), куратор NiCAmCHiK, сложность 1/5 (●○○○○), период «Cataclysm — Battle for Azeroth»."
        ],
        "strings": [
            {
                "field": "name",
                "wts_id": 38899,
                "after": wts_updates[38899]
            },
            {
                "field": "tip1",
                "wts_id": 38900,
                "after": wts_updates[38900]
            },
            {
                "field": "ubertip1",
                "wts_id": 26678,
                "after": wts_updates[26678]
            }
        ],
        "markers": [
            {
                "id": "R0FX",
                "name": "Гилнеас (маркер расы)",
                "strings": [
                    {"field": "name1", "wts_id": 8429, "after": wts_updates.get(8429)},
                    {"field": "tip1", "wts_id": 25159, "after": wts_updates.get(25159)},
                    {"field": "ubertip1", "wts_id": 5600, "after": wts_updates.get(5600)}
                ]
            }
        ]
    }
    (out_dir / "gilneas_selection.json").write_text(json.dumps(sel_data, ensure_ascii=False, indent=2), encoding="utf-8")
    print("Wrote gilneas_selection.json")

    # -------------------------------------------------------------
    # 2. gilneas_buildings.json
    # -------------------------------------------------------------
    bld_entries = []
    for b in dump["buildings"]:
        b_id = b["id"]
        if b_id not in plan["categories"]["buildings"]:
            continue
        hk_val = b.get("hotkey")
        entry = {
            "id": b_id,
            "hotkey": hk_val,
            "strings": []
        }
        for f in ["name", "tip", "ubertip"]:
            raw_field = f"raw_{f}"
            sid = parse_str_id(b.get(raw_field))
            if sid and sid in wts_updates:
                entry["strings"].append({
                    "field": f,
                    "wts_id": sid,
                    "after": wts_updates[sid]
                })
        bld_entries.append(entry)

    bld_data = {
        "scope": f"Гилнеас (Gilneas / Worgens): категория 1 — Здания ({len(bld_entries)} зданий)",
        "buildings_count": len(bld_entries),
        "variants": ["SD"],
        "buildings": bld_entries
    }
    (out_dir / "gilneas_buildings.json").write_text(json.dumps(bld_data, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"Wrote gilneas_buildings.json ({len(bld_entries)} buildings)")

    # -------------------------------------------------------------
    # 3. gilneas_units.json
    # -------------------------------------------------------------
    unit_entries = []
    # Worker
    w = dump["worker"]
    w_entry = {
        "id": w["id"],
        "hotkey": w.get("hotkey"),
        "strings": []
    }
    for f in ["name", "tip", "ubertip"]:
        raw_field = f"raw_{f}"
        sid = parse_str_id(w.get(raw_field))
        if sid and sid in wts_updates:
            w_entry["strings"].append({
                "field": f,
                "wts_id": sid,
                "after": wts_updates[sid]
            })
    unit_entries.append(w_entry)

    for u in dump["units"]:
        u_id = u["id"]
        if u_id not in plan["categories"]["units"]:
            continue
        hk_val = u.get("hotkey")
        entry = {
            "id": u_id,
            "hotkey": hk_val,
            "strings": []
        }
        for f in ["name", "tip", "ubertip"]:
            raw_field = f"raw_{f}"
            sid = parse_str_id(u.get(raw_field))
            if sid and sid in wts_updates:
                entry["strings"].append({
                    "field": f,
                    "wts_id": sid,
                    "after": wts_updates[sid]
                })
        unit_entries.append(entry)

    unit_data = {
        "scope": f"Гилнеас (Gilneas / Worgens): категория 2 — Юниты ({len(unit_entries)} юнитов)",
        "units_count": len(unit_entries),
        "variants": ["SD"],
        "units": unit_entries
    }
    (out_dir / "gilneas_units.json").write_text(json.dumps(unit_data, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"Wrote gilneas_units.json ({len(unit_entries)} units)")

    # -------------------------------------------------------------
    # 4. gilneas_heroes.json
    # -------------------------------------------------------------
    hero_entries = []
    for h in dump["heroes"]:
        h_id = h["id"]
        if h_id not in plan["categories"]["heroes"]:
            continue
        hk_val = h.get("hotkey")
        entry = {
            "id": h_id,
            "hotkey": hk_val,
            "strings": []
        }
        for f in ["name", "propernames", "tip", "ubertip", "awakentip", "revivetip"]:
            raw_field = f"raw_{f}"
            sid = parse_str_id(h.get(raw_field))
            if sid and sid in wts_updates:
                entry["strings"].append({
                    "field": f,
                    "wts_id": sid,
                    "after": wts_updates[sid]
                })
        hero_entries.append(entry)

    hero_data = {
        "scope": f"Гилнеас (Gilneas / Worgens): категория 3 — Герои ({len(hero_entries)} героев)",
        "heroes_count": len(hero_entries),
        "variants": ["SD"],
        "heroes": hero_entries
    }
    (out_dir / "gilneas_heroes.json").write_text(json.dumps(hero_data, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"Wrote gilneas_heroes.json ({len(hero_entries)} heroes)")

    # -------------------------------------------------------------
    # 5. gilneas_abilities.json
    # -------------------------------------------------------------
    abil_entries = []
    for a in dump["abilities"]:
        a_id = a["id"]
        if a_id not in plan["categories"]["abilities"]:
            continue
        entry = {
            "id": a_id,
            "levels": a.get("levels", 1),
            "strings": []
        }
        # Name
        sid_name = parse_str_id(a.get("raw_name"))
        if sid_name and sid_name in wts_updates:
            entry["strings"].append({
                "field": "name",
                "wts_id": sid_name,
                "after": wts_updates[sid_name]
            })
        # Research tip / ubertip
        sid_rtip = parse_str_id(a.get("raw_researchtip"))
        if sid_rtip and sid_rtip in wts_updates:
            entry["strings"].append({
                "field": "researchtip",
                "wts_id": sid_rtip,
                "after": wts_updates[sid_rtip]
            })
        sid_rub = parse_str_id(a.get("raw_researchubertip"))
        if sid_rub and sid_rub in wts_updates:
            entry["strings"].append({
                "field": "researchubertip",
                "wts_id": sid_rub,
                "after": wts_updates[sid_rub]
            })
        # Level tips / ubertips
        for lvl_str, tips in a.get("tips", {}).items():
            sid = parse_str_id(tips.get("raw"))
            if sid and sid in wts_updates:
                entry["strings"].append({
                    "field": f"tip_{lvl_str}",
                    "wts_id": sid,
                    "after": wts_updates[sid]
                })
        for lvl_str, ubertips in a.get("ubertips", {}).items():
            sid = parse_str_id(ubertips.get("raw"))
            if sid and sid in wts_updates:
                entry["strings"].append({
                    "field": f"ubertip_{lvl_str}",
                    "wts_id": sid,
                    "after": wts_updates[sid]
                })
        if entry["strings"]:
            abil_entries.append(entry)

    abil_data = {
        "scope": f"Гилнеас (Gilneas / Worgens): категория 4 — Способности ({len(abil_entries)} способностей)",
        "abilities_count": len(abil_entries),
        "variants": ["SD"],
        "abilities": abil_entries
    }
    (out_dir / "gilneas_abilities.json").write_text(json.dumps(abil_data, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"Wrote gilneas_abilities.json ({len(abil_entries)} abilities)")

    # -------------------------------------------------------------
    # 6. gilneas_research.json
    # -------------------------------------------------------------
    upg_entries = []
    for u in dump["upgrades"]:
        u_id = u["id"]
        if u_id not in plan["categories"]["upgrades"]:
            continue
        entry = {
            "id": u_id,
            "levels": u.get("levels", 1),
            "strings": []
        }
        for lvl_str, names in u.get("names", {}).items():
            sid = parse_str_id(names.get("raw"))
            if sid and sid in wts_updates:
                entry["strings"].append({
                    "field": f"name_{lvl_str}",
                    "wts_id": sid,
                    "after": wts_updates[sid]
                })
        for lvl_str, tips in u.get("tips", {}).items():
            sid = parse_str_id(tips.get("raw"))
            if sid and sid in wts_updates:
                entry["strings"].append({
                    "field": f"tip_{lvl_str}",
                    "wts_id": sid,
                    "after": wts_updates[sid]
                })
        for lvl_str, ubertips in u.get("ubertips", {}).items():
            sid = parse_str_id(ubertips.get("raw"))
            if sid and sid in wts_updates:
                entry["strings"].append({
                    "field": f"ubertip_{lvl_str}",
                    "wts_id": sid,
                    "after": wts_updates[sid]
                })
        upg_entries.append(entry)

    upg_data = {
        "scope": f"Гилнеас (Gilneas / Worgens): категория 5 — Исследования и маркеры ({len(upg_entries)} технологий)",
        "upgrades_count": len(upg_entries),
        "variants": ["SD"],
        "upgrades": upg_entries
    }
    (out_dir / "gilneas_research.json").write_text(json.dumps(upg_data, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"Wrote gilneas_research.json ({len(upg_entries)} upgrades)")

    # -------------------------------------------------------------
    # 7. gilneas_audit.json
    # -------------------------------------------------------------
    audit_data = {
        "race": "Гилнеас (Gilneas / Worgens)",
        "race_id": 24,
        "selection_ability": "A121",
        "objects_audit": {
            "buildings": {
                "count": len(bld_entries),
                "ids": [b["id"] for b in bld_entries],
                "town_halls": {
                    "tier1": {"id": "h0IJ", "name": "Ратуша", "food": 50},
                    "tier2": {"id": "h0IK", "name": "Форт", "food": 100},
                    "tier3": {"id": "h0IL", "name": "Замок", "food": 150}
                },
                "farm": {"id": "h0IM", "name": "Ферма", "food": 40}
            },
            "units": {
                "count": len(unit_entries),
                "ids": [u["id"] for u in unit_entries],
                "worker": "h0IT (Постройщик)",
                "combat_units": [
                    "h0IU (Пехотинец волк)", "h0IV (Стрелок)", "h0IW (Рыцарь волк)",
                    "h0IX (Ворген друид)", "h0IY (Пехотинец человек)", "h0IZ (Рыцарь человек)",
                    "h0J0 (Ворген маг)", "h0J1 (Полудикий ворген)", "h0NA (Топорометатель)",
                    "o02T (Катапульта)"
                ]
            },
            "heroes": {
                "count": len(hero_entries),
                "ids": [h["id"] for h in hero_entries],
                "names": {
                    "H0J2": "Верховный охотник (Бузан Охотник — Сила, ближний бой, Обычный герой)",
                    "H0J6": "Лорд друид (Друид — Интеллект, ближний бой, Обычный герой)",
                    "H0J7": "Генерал Гилнеаса (Генерал — Сила, ближний бой, Обычный герой)",
                    "H0J8": "Полубог (Голдринн — Сила, ближний бой, Легендарный герой)"
                }
            },
            "abilities": {
                "count": len(abil_entries),
                "total_wts_updated": len(plan["wts_updates"])
            },
            "researches": {
                "count": len(upg_entries),
                "markers_list": {
                    "R0FX": "Маркер расы Гилнеас"
                }
            }
        },
        "items_audit": {
            "race_specific_items": [],
            "status": "No race-specific shop items or inventory artifacts found in war3map.w3t for Gilneas."
        },
        "messages_audit": {
            "race_specific_messages": [],
            "status": "No race-specific floating messages or game UI strings found in war3map.wts for Gilneas."
        },
        "buffs_audit": {
            "custom_buffs": ["B06A", "B06B", "B06C", "B06D"],
            "standard_buffs_used": [
                "BEar", "BHab", "BHtc", "BNms", "BOsf", "BPSE", "BUav", "BUcs", "Bblo", "Broa", "Brpl"
            ],
            "status": "Standardized 4 custom buffs with secondary color labels and clean descriptions."
        },
        "total_wts_updates": len(plan["wts_updates"]),
        "total_checks": len(plan["checks_def"])
    }
    (out_dir / "gilneas_audit.json").write_text(json.dumps(audit_data, ensure_ascii=False, indent=2), encoding="utf-8")
    print("Wrote gilneas_audit.json")

if __name__ == "__main__":
    main()
