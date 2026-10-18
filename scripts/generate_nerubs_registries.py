# -*- coding: utf-8 -*-
"""Generate standardized JSON category registries for Race 21: Nerubs (Нерубы) in docs/ui_text/

Outputs:
- docs/ui_text/nerubs_selection.json
- docs/ui_text/nerubs_buildings.json
- docs/ui_text/nerubs_units.json
- docs/ui_text/nerubs_heroes.json
- docs/ui_text/nerubs_abilities.json
- docs/ui_text/nerubs_research.json
- docs/ui_text/nerubs_audit.json
"""
import json
from pathlib import Path
import sys

sys.stdout.reconfigure(encoding='utf-8')
ROOT = Path(__file__).resolve().parent.parent

def main():
    plan_path = ROOT / "docs/ui_text/nerubs_plan.json"
    dump_path = ROOT / "scripts/nerubs_raw_dump.json"
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
    # 1. nerubs_selection.json
    # -------------------------------------------------------------
    sel_data = {
        "scope": "Нерубы (Nerubs): подсказка выбора расы A0HT и маркеры",
        "object": "A0HT",
        "variants": ["SD"],
        "hotkey": {
            "value": "W"
        },
        "levels": 1,
        "evidence": [
            "04_race_selection.lua: InitTrig_Race_Nerubs_O регистрирует способность A0HT.",
            "При выборе создаются 3 рабочих h0BE, исследуется маркер R07N, удаляется выбирающий юнит.",
            "Горячая клавиша W, создатель Escanor (Яхве), куратор VinerX, сложность 3/5 (●●●○○), период «Wrath of the Lich King»."
        ],
        "strings": [
            {
                "field": "name",
                "wts_id": 38926,
                "after": wts_updates[38926]
            },
            {
                "field": "tip1",
                "wts_id": 38927,
                "after": wts_updates[38927]
            },
            {
                "field": "ubertip1",
                "wts_id": 35195,
                "after": wts_updates[35195]
            }
        ],
        "markers": [
            {
                "id": "R07N",
                "name": "Нерубы (маркер расы)",
                "strings": [
                    {"field": "name1", "wts_id": 10679, "after": wts_updates.get(10679)},
                    {"field": "tip1", "wts_id": 10680, "after": wts_updates.get(10680)},
                    {"field": "ubertip1", "wts_id": 20121, "after": wts_updates.get(20121)}
                ]
            }
        ]
    }
    (out_dir / "nerubs_selection.json").write_text(json.dumps(sel_data, ensure_ascii=False, indent=2), encoding="utf-8")
    print("Wrote nerubs_selection.json")

    # -------------------------------------------------------------
    # 2. nerubs_buildings.json
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
        "scope": f"Нерубы (Nerubs): категория 1 — Здания ({len(bld_entries)} зданий)",
        "buildings_count": len(bld_entries),
        "variants": ["SD"],
        "buildings": bld_entries
    }
    (out_dir / "nerubs_buildings.json").write_text(json.dumps(bld_data, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"Wrote nerubs_buildings.json ({len(bld_entries)} buildings)")

    # -------------------------------------------------------------
    # 3. nerubs_units.json
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
        "scope": f"Нерубы (Nerubs): категория 2 — Юниты ({len(unit_entries)} юнитов)",
        "units_count": len(unit_entries),
        "variants": ["SD"],
        "units": unit_entries
    }
    (out_dir / "nerubs_units.json").write_text(json.dumps(unit_data, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"Wrote nerubs_units.json ({len(unit_entries)} units)")

    # -------------------------------------------------------------
    # 4. nerubs_heroes.json
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
        "scope": f"Нерубы (Nerubs): категория 3 — Герои ({len(hero_entries)} героев)",
        "heroes_count": len(hero_entries),
        "variants": ["SD"],
        "heroes": hero_entries
    }
    (out_dir / "nerubs_heroes.json").write_text(json.dumps(hero_data, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"Wrote nerubs_heroes.json ({len(hero_entries)} heroes)")

    # -------------------------------------------------------------
    # 5. nerubs_abilities.json
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
        "scope": f"Нерубы (Nerubs): категория 4 — Способности ({len(abil_entries)} способностей)",
        "abilities_count": len(abil_entries),
        "variants": ["SD"],
        "abilities": abil_entries
    }
    (out_dir / "nerubs_abilities.json").write_text(json.dumps(abil_data, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"Wrote nerubs_abilities.json ({len(abil_entries)} abilities)")

    # -------------------------------------------------------------
    # 6. nerubs_research.json
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
        "scope": f"Нерубы (Nerubs): категория 5 — Исследования и маркеры ({len(upg_entries)} технологий)",
        "upgrades_count": len(upg_entries),
        "variants": ["SD"],
        "upgrades": upg_entries
    }
    (out_dir / "nerubs_research.json").write_text(json.dumps(upg_data, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"Wrote nerubs_research.json ({len(upg_entries)} upgrades)")

    # -------------------------------------------------------------
    # 7. nerubs_audit.json
    # -------------------------------------------------------------
    audit_data = {
        "race": "Нерубы (Nerubs)",
        "race_id": 21,
        "selection_ability": "A0HT",
        "objects_audit": {
            "buildings": {
                "count": len(bld_entries),
                "ids": [b["id"] for b in bld_entries],
                "economy_building": {
                    "id": "u019",
                    "name": "Кокон",
                    "food_provided": 40,
                    "gold_income_per_25s": 30,
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
                    "U01U": "Пророк (Гор'аман — Интеллект, дальний бой)",
                    "U01V": "Паучий лорд (Ануб'арак — Сила, ближний бой)",
                    "U01W": "Высший Страж (Омун-ул — Ловкость, дальний бой)",
                    "NERH": "Королева Нерубов (Нер-мун — Легендарный герой, Интеллект, дальний бой)"
                }
            },
            "abilities": {
                "count": len(abil_entries),
                "total_wts_updated": len(plan["wts_updates"])
            },
            "researches": {
                "count": len(upg_entries),
                "markers_list": {
                    "R07N": "Маркер расы Нерубы"
                }
            }
        },
        "items_audit": {
            "race_specific_items": [],
            "status": "No race-specific shop items or inventory artifacts found in war3map.w3t for Nerubs."
        },
        "messages_audit": {
            "race_specific_messages": [],
            "status": "No race-specific floating messages or game UI strings found in war3map.wts for Nerubs."
        },
        "buffs_audit": {
            "custom_buffs": ["B01D", "B040", "B04A", "B04E"],
            "standard_buffs_used": [
                "BUts", "BPSE", "BOwd", "BEer", "Brai", "Bhea", "Bakb", "BUim", "BUcs", "BUau", "BNlm"
            ],
            "status": "Standardized custom buffs with secondary color labels and clean descriptions."
        },
        "total_wts_updates": len(plan["wts_updates"]),
        "total_checks": len(plan["checks_def"])
    }
    (out_dir / "nerubs_audit.json").write_text(json.dumps(audit_data, ensure_ascii=False, indent=2), encoding="utf-8")
    print("Wrote nerubs_audit.json")

if __name__ == "__main__":
    main()
