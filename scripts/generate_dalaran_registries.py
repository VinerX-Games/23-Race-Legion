# -*- coding: utf-8 -*-
"""Generate standardized JSON category registries for Race 16: Dalaran (Даларан) in docs/ui_text/

Outputs:
- docs/ui_text/dalaran_selection.json
- docs/ui_text/dalaran_buildings.json
- docs/ui_text/dalaran_units.json
- docs/ui_text/dalaran_heroes.json
- docs/ui_text/dalaran_abilities.json
- docs/ui_text/dalaran_research.json
- docs/ui_text/dalaran_audit.json
"""
import json
from pathlib import Path
import sys

sys.stdout.reconfigure(encoding='utf-8')
ROOT = Path(__file__).resolve().parent.parent

def main():
    plan_path = ROOT / "docs/ui_text/dalaran_plan.json"
    dump_path = ROOT / "scripts/dalaran_raw_dump.json"
    out_dir = ROOT / "docs/ui_text"
    out_dir.mkdir(parents=True, exist_ok=True)

    plan = json.loads(plan_path.read_text(encoding="utf-8"))
    dump = json.loads(dump_path.read_text(encoding="utf-8"))
    wts_updates = {int(k): v for k, v in plan["wts_updates"].items()}

    # Helper to parse TRIGSTR_ID
    def parse_str_id(raw):
        if isinstance(raw, str) and raw.startswith("TRIGSTR_"):
            try:
                return int(raw[8:])
            except ValueError:
                return None
        return None

    # -------------------------------------------------------------
    # 1. dalaran_selection.json
    # -------------------------------------------------------------
    sel_data = {
        "scope": "Даларан (Dalaran): подсказка выбора расы A0HN и маркеры",
        "object": "A0HN",
        "variants": ["SD"],
        "hotkey": {
            "value": "S"
        },
        "levels": 1,
        "evidence": [
            "04_race_selection.lua: InitTrig_Race_Dalaran фильтрует способность A0HN.",
            "При выборе создаются стартовые здания и юниты Даларана, исследуются маркеры R0BW, R0KK.",
            "Горячая клавиша S, создатель Escanor, куратор VinerX, сложность 4/5 (Сложная), период «Wrath of the Lich King — Legion»."
        ],
        "strings": [
            {
                "field": "name",
                "wts_id": 38867,
                "after": wts_updates[38867]
            },
            {
                "field": "tip1",
                "wts_id": 38868,
                "after": wts_updates[38868]
            },
            {
                "field": "ubertip1",
                "wts_id": 21869,
                "after": wts_updates[21869]
            }
        ],
        "markers": [
            {
                "id": "R0BW",
                "name": "Даларан (маркер расы)",
                "strings": [
                    {"field": "name1", "wts_id": 9238, "after": wts_updates.get(9238)},
                    {"field": "tip1", "wts_id": 9239, "after": wts_updates.get(9239)},
                    {"field": "ubertip1", "wts_id": 20124, "after": wts_updates.get(20124)}
                ]
            },
            {
                "id": "R0KK",
                "name": "Даларан или Альянс (общий маркер)",
                "strings": [
                    {"field": "name1", "wts_id": 16408, "after": wts_updates.get(16408)},
                    {"field": "tip1", "wts_id": 16409, "after": wts_updates.get(16409)},
                    {"field": "ubertip1", "wts_id": 16416, "after": wts_updates.get(16416)}
                ]
            }
        ]
    }
    (out_dir / "dalaran_selection.json").write_text(json.dumps(sel_data, ensure_ascii=False, indent=2), encoding="utf-8")
    print("Wrote dalaran_selection.json")

    # -------------------------------------------------------------
    # 2. dalaran_buildings.json
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
        "scope": f"Даларан (Dalaran): категория 1 — Здания ({len(bld_entries)} зданий)",
        "buildings_count": len(bld_entries),
        "variants": ["SD"],
        "buildings": bld_entries
    }
    (out_dir / "dalaran_buildings.json").write_text(json.dumps(bld_data, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"Wrote dalaran_buildings.json ({len(bld_entries)} buildings)")

    # -------------------------------------------------------------
    # 3. dalaran_units.json
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
        "scope": f"Даларан (Dalaran): категория 2 — Юниты ({len(unit_entries)} юнитов)",
        "units_count": len(unit_entries),
        "variants": ["SD"],
        "units": unit_entries
    }
    (out_dir / "dalaran_units.json").write_text(json.dumps(unit_data, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"Wrote dalaran_units.json ({len(unit_entries)} units)")

    # -------------------------------------------------------------
    # 4. dalaran_heroes.json
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
        "scope": f"Даларан (Dalaran): категория 3 — Герои ({len(hero_entries)} героев)",
        "heroes_count": len(hero_entries),
        "variants": ["SD"],
        "heroes": hero_entries
    }
    (out_dir / "dalaran_heroes.json").write_text(json.dumps(hero_data, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"Wrote dalaran_heroes.json ({len(hero_entries)} heroes)")

    # -------------------------------------------------------------
    # 5. dalaran_abilities.json
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
        for lvl_str, names in a.get("names", {}).items():
            sid = parse_str_id(names.get("raw"))
            if sid and sid in wts_updates:
                entry["strings"].append({
                    "field": f"name_{lvl_str}",
                    "wts_id": sid,
                    "after": wts_updates[sid]
                })
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
        for lvl_str, utips in a.get("unubertips", {}).items():
            sid = parse_str_id(utips.get("raw"))
            if sid and sid in wts_updates:
                entry["strings"].append({
                    "field": f"unubertip_{lvl_str}",
                    "wts_id": sid,
                    "after": wts_updates[sid]
                })
        if entry["strings"]:
            abil_entries.append(entry)

    abil_data = {
        "scope": f"Даларан (Dalaran): категория 4 — Способности ({len(abil_entries)} способностей)",
        "abilities_count": len(abil_entries),
        "variants": ["SD"],
        "abilities": abil_entries
    }
    (out_dir / "dalaran_abilities.json").write_text(json.dumps(abil_data, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"Wrote dalaran_abilities.json ({len(abil_entries)} abilities)")

    # -------------------------------------------------------------
    # 6. dalaran_research.json
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
        "scope": f"Даларан (Dalaran): категория 5 — Исследования и маркеры ({len(upg_entries)} технологий)",
        "upgrades_count": len(upg_entries),
        "variants": ["SD"],
        "upgrades": upg_entries
    }
    (out_dir / "dalaran_research.json").write_text(json.dumps(upg_data, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"Wrote dalaran_research.json ({len(upg_entries)} upgrades)")

    # -------------------------------------------------------------
    # 7. dalaran_audit.json
    # -------------------------------------------------------------
    audit_data = {
        "race": "Даларан (Dalaran)",
        "race_id": 16,
        "selection_ability": "A0HN",
        "objects_audit": {
            "buildings": {
                "count": len(bld_entries),
                "ids": [b["id"] for b in bld_entries],
                "economy_building": {
                    "id": "h031",
                    "name": "Конденсатор Маны",
                    "food_provided": 40,
                    "gold_income_per_25s": 20,
                    "verified_via": "53_economy.lua and unit ability stats"
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
                    "H04S": "Верховный маг (Интеллект, дальний бой)",
                    "H04W": "Огненный мастер (Интеллект, дальний бой)",
                    "H04X": "Мастер Тайной магии (Интеллект, дальний бой)",
                    "H052": "Глава Кирин-Тора - Ронин (Интеллект, дальний бой, легендарный герой)",
                    "H053": "Хранитель - Кадгар (Интеллект, дальний бой, легендарный герой)"
                }
            },
            "abilities": {
                "count": len(abil_entries),
                "total_wts_updated": len(plan["wts_updates"])
            },
            "researches": {
                "count": len(upg_entries),
                "markers_list": {
                    "R0BW": "Маркер расы Даларан",
                    "R0KK": "Маркер Даларан или Альянс"
                }
            }
        },
        "items_audit": {
            "race_specific_items": [],
            "status": "No race-specific shop items or inventory artifacts found in war3map.w3t for Dalaran."
        },
        "messages_audit": {
            "race_specific_messages": [],
            "status": "No race-specific floating messages or game UI strings found in war3map.wts for Dalaran."
        },
        "buffs_audit": {
            "custom_buffs": [],
            "standard_buffs_used": [
                "Bblo", "Bfae", "Bcyc", "Bfro", "Bpoi", "Bdef", "BOac", "Bcri", "Bspe", "Bshs"
            ],
            "status": "All buffs used by Dalaran abilities are standard Warcraft III engine buffs. No custom text modification required."
        },
        "total_wts_updates": len(plan["wts_updates"]),
        "total_checks": len(plan["checks_def"])
    }
    (out_dir / "dalaran_audit.json").write_text(json.dumps(audit_data, ensure_ascii=False, indent=2), encoding="utf-8")
    print("Wrote dalaran_audit.json")

if __name__ == "__main__":
    main()
