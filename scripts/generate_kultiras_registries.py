# -*- coding: utf-8 -*-
"""Generate standardized JSON category registries for Race 17: Kul Tiras (Кул-Тирас) in docs/ui_text/

Outputs:
- docs/ui_text/kultiras_selection.json
- docs/ui_text/kultiras_buildings.json
- docs/ui_text/kultiras_units.json
- docs/ui_text/kultiras_heroes.json
- docs/ui_text/kultiras_abilities.json
- docs/ui_text/kultiras_research.json
- docs/ui_text/kultiras_audit.json
"""
import json
from pathlib import Path
import sys

sys.stdout.reconfigure(encoding='utf-8')
ROOT = Path(__file__).resolve().parent.parent

def main():
    plan_path = ROOT / "docs/ui_text/kultiras_plan.json"
    dump_path = ROOT / "scripts/kultiras_raw_dump.json"
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
    # 1. kultiras_selection.json
    # -------------------------------------------------------------
    sel_data = {
        "scope": "Кул-Тирас (Kul Tiras): подсказка выбора расы A0HO и маркеры",
        "object": "A0HO",
        "variants": ["SD"],
        "hotkey": {
            "value": "X"
        },
        "levels": 1,
        "evidence": [
            "04_race_selection.lua: InitTrig_Race_KulTiras_O фильтрует способность A0HO.",
            "При выборе создаются стартовые работники и исследуются маркеры R07D, R0HX.",
            "Горячая клавиша X, создатель Escanor, куратор VinerX, сложность 1/5 (Очень простая), период «Битва за Азерот»."
        ],
        "strings": [
            {
                "field": "name",
                "wts_id": 38869,
                "after": wts_updates[38869]
            },
            {
                "field": "tip1",
                "wts_id": 38870,
                "after": wts_updates[38870]
            },
            {
                "field": "ubertip1",
                "wts_id": 28524,
                "after": wts_updates[28524]
            }
        ],
        "markers": [
            {
                "id": "R07D",
                "name": "Кул-Тирас (маркер расы)",
                "strings": [
                    {"field": "name1", "wts_id": 9500, "after": wts_updates.get(9500)},
                    {"field": "tip1", "wts_id": 9591, "after": wts_updates.get(9591)},
                    {"field": "ubertip1", "wts_id": 20111, "after": wts_updates.get(20111)}
                ]
            },
            {
                "id": "R0HX",
                "name": "Кул-Тирас или Альянс (общий маркер)",
                "strings": [
                    {"field": "name1", "wts_id": 30266, "after": wts_updates.get(30266)},
                    {"field": "tip1", "wts_id": 29942, "after": wts_updates.get(29942)}
                ]
            }
        ]
    }
    (out_dir / "kultiras_selection.json").write_text(json.dumps(sel_data, ensure_ascii=False, indent=2), encoding="utf-8")
    print("Wrote kultiras_selection.json")

    # -------------------------------------------------------------
    # 2. kultiras_buildings.json
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
        "scope": f"Кул-Тирас (Kul Tiras): категория 1 — Здания ({len(bld_entries)} зданий)",
        "buildings_count": len(bld_entries),
        "variants": ["SD"],
        "buildings": bld_entries
    }
    (out_dir / "kultiras_buildings.json").write_text(json.dumps(bld_data, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"Wrote kultiras_buildings.json ({len(bld_entries)} buildings)")

    # -------------------------------------------------------------
    # 3. kultiras_units.json
    # -------------------------------------------------------------
    unit_entries = []
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
        "scope": f"Кул-Тирас (Kul Tiras): категория 2 — Юниты ({len(unit_entries)} юнитов)",
        "units_count": len(unit_entries),
        "variants": ["SD"],
        "units": unit_entries
    }
    (out_dir / "kultiras_units.json").write_text(json.dumps(unit_data, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"Wrote kultiras_units.json ({len(unit_entries)} units)")

    # -------------------------------------------------------------
    # 4. kultiras_heroes.json
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
        for f in ["name", "propernames", "tip", "ubertip"]:
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
        "scope": f"Кул-Тирас (Kul Tiras): категория 3 — Герои ({len(hero_entries)} героев)",
        "heroes_count": len(hero_entries),
        "variants": ["SD"],
        "heroes": hero_entries
    }
    (out_dir / "kultiras_heroes.json").write_text(json.dumps(hero_data, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"Wrote kultiras_heroes.json ({len(hero_entries)} heroes)")

    # -------------------------------------------------------------
    # 5. kultiras_abilities.json
    # -------------------------------------------------------------
    abil_entries = []
    for a in dump["abilities"]:
        a_id = a["id"]
        if a_id not in plan["categories"]["abilities"]:
            continue
        entry = {
            "id": a_id,
            "strings": []
        }
        # name
        name_sid = parse_str_id(a.get("raw_name"))
        if name_sid and name_sid in wts_updates:
            entry["strings"].append({
                "field": "name",
                "wts_id": name_sid,
                "after": wts_updates[name_sid]
            })
        # researchtip / researchubertip
        rtip_sid = parse_str_id(a.get("raw_researchtip"))
        if rtip_sid and rtip_sid in wts_updates:
            entry["strings"].append({
                "field": "researchtip",
                "wts_id": rtip_sid,
                "after": wts_updates[rtip_sid]
            })
        rubertip_sid = parse_str_id(a.get("raw_researchubertip"))
        if rubertip_sid and rubertip_sid in wts_updates:
            entry["strings"].append({
                "field": "researchubertip",
                "wts_id": rubertip_sid,
                "after": wts_updates[rubertip_sid]
            })
        # tips and ubertips
        for lvl_str, tips in a.get("tips", {}).items():
            sid = parse_str_id(tips.get("raw"))
            if sid and sid in wts_updates:
                entry["strings"].append({
                    "field": lvl_str,
                    "wts_id": sid,
                    "after": wts_updates[sid]
                })
        for lvl_str, ubertips in a.get("ubertips", {}).items():
            sid = parse_str_id(ubertips.get("raw"))
            if sid and sid in wts_updates:
                entry["strings"].append({
                    "field": lvl_str,
                    "wts_id": sid,
                    "after": wts_updates[sid]
                })
        if entry["strings"]:
            abil_entries.append(entry)

    abil_data = {
        "scope": f"Кул-Тирас (Kul Tiras): категория 4 — Способности ({len(abil_entries)} способностей)",
        "abilities_count": len(abil_entries),
        "variants": ["SD"],
        "abilities": abil_entries
    }
    (out_dir / "kultiras_abilities.json").write_text(json.dumps(abil_data, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"Wrote kultiras_abilities.json ({len(abil_entries)} abilities)")

    # -------------------------------------------------------------
    # 6. kultiras_research.json
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
                    "field": lvl_str,
                    "wts_id": sid,
                    "after": wts_updates[sid]
                })
        for lvl_str, tips in u.get("tips", {}).items():
            sid = parse_str_id(tips.get("raw"))
            if sid and sid in wts_updates:
                entry["strings"].append({
                    "field": lvl_str,
                    "wts_id": sid,
                    "after": wts_updates[sid]
                })
        for lvl_str, ubertips in u.get("ubertips", {}).items():
            sid = parse_str_id(ubertips.get("raw"))
            if sid and sid in wts_updates:
                entry["strings"].append({
                    "field": lvl_str,
                    "wts_id": sid,
                    "after": wts_updates[sid]
                })
        upg_entries.append(entry)

    upg_data = {
        "scope": f"Кул-Тирас (Kul Tiras): категория 5 — Исследования и маркеры ({len(upg_entries)} технологий)",
        "upgrades_count": len(upg_entries),
        "variants": ["SD"],
        "upgrades": upg_entries
    }
    (out_dir / "kultiras_research.json").write_text(json.dumps(upg_data, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"Wrote kultiras_research.json ({len(upg_entries)} upgrades)")

    # -------------------------------------------------------------
    # 7. kultiras_audit.json
    # -------------------------------------------------------------
    audit_data = {
        "race": "Кул-Тирас (Kul Tiras)",
        "race_id": 17,
        "selection_ability": "A0HO",
        "objects_audit": {
            "buildings": {
                "count": len(bld_entries),
                "ids": [b["id"] for b in bld_entries],
                "economy_building": {
                    "id": "h024",
                    "name": "Ферма",
                    "food_provided": 40,
                    "gold_income_per_25s": 20,
                    "verified_via": "53_economy.lua and unit object stats"
                }
            },
            "units": {
                "count": len(unit_entries),
                "ids": [u["id"] for u in unit_entries]
            },
            "heroes": {
                "count": len(hero_entries),
                "ids": [h["id"] for h in hero_entries],
                "names": {
                    "H01L": "Капитан (Ловкость, ближний бой)",
                    "H01N": "Верховная Жрица Морей (Интеллект, дальний бой)",
                    "H01K": "Адмирал (Сила, ближний бой)"
                }
            },
            "abilities": {
                "count": len(abil_entries),
                "total_wts_updated": len(plan["wts_updates"])
            },
            "researches": {
                "count": len(upg_entries),
                "mutually_exclusive_paths": {
                    "R027": "Инвестировать в Флот — усиливает корабли, исключает армию",
                    "R02S": "Инвестировать в Армию — усиливает пехоту, исключает флот"
                },
                "markers_list": {
                    "R07D": "Маркер расы Кул-Тирас",
                    "R0HX": "Маркер Кул-Тирас или Альянс"
                }
            }
        },
        "items_audit": {
            "race_specific_items": [],
            "status": "No race-specific shop items or inventory artifacts found in war3map.w3t for Kul Tiras."
        },
        "messages_audit": {
            "race_specific_messages": [],
            "status": "No race-specific floating messages or game UI strings found in war3map.wts for Kul Tiras."
        },
        "buffs_audit": {
            "custom_buffs": [],
            "standard_buffs_used": [
                "Bdef", "Bfro", "Bblo", "Binf", "BOac", "Bcri", "Bshs"
            ],
            "status": "All buffs used by Kul Tiras abilities are standard Warcraft III engine buffs. No custom text modification required."
        },
        "total_wts_updates": len(plan["wts_updates"]),
        "total_checks": len(plan["checks_def"])
    }
    (out_dir / "kultiras_audit.json").write_text(json.dumps(audit_data, ensure_ascii=False, indent=2), encoding="utf-8")
    print("Wrote kultiras_audit.json")

if __name__ == "__main__":
    main()
