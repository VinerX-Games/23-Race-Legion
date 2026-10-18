# -*- coding: utf-8 -*-
"""Generate standardized JSON category registries for Race 26: Night Elf (Ночные эльфы) in docs/ui_text/

Outputs:
- docs/ui_text/nightelf_selection.json
- docs/ui_text/nightelf_buildings.json
- docs/ui_text/nightelf_units.json
- docs/ui_text/nightelf_heroes.json
- docs/ui_text/nightelf_abilities.json
- docs/ui_text/nightelf_research.json
- docs/ui_text/nightelf_audit.json
"""
import json
from pathlib import Path
import sys

sys.stdout.reconfigure(encoding='utf-8')
ROOT = Path(__file__).resolve().parent.parent

def main():
    plan_path = ROOT / "docs/ui_text/nightelf_plan.json"
    dump_path = ROOT / "scripts/nightelf_raw_dump.json"
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
    # 1. nightelf_selection.json
    # -------------------------------------------------------------
    sel_data = {
        "scope": "Ночные эльфы (Night Elf): подсказка выбора расы A0HL и маркеры",
        "object": "A0HL",
        "variants": ["SD"],
        "hotkey": {
            "value": "S"
        },
        "levels": 1,
        "evidence": [
            "04_race_selection.lua: InitTrig_Race_nightelf регистрирует способность A0HL.",
            "При выборе создаются 6 рабочих ewsp, исследуется маркер R07L, удаляется выбирающий юнит.",
            "Горячая клавиша S, создатель Escanor (Яхве), сложность 3/5 (●●●○○), период «WoW Vanilla — Legion»."
        ],
        "strings": [
            {
                "field": "name",
                "wts_id": 38863,
                "after": wts_updates[38863]
            },
            {
                "field": "tip1",
                "wts_id": 38864,
                "after": wts_updates[38864]
            },
            {
                "field": "ubertip1",
                "wts_id": 35173,
                "after": wts_updates[35173]
            }
        ],
        "markers": [
            {
                "id": "R07L",
                "name": "Ночные эльфы (маркер расы)",
                "strings": [
                    {"field": "name1", "wts_id": 10673, "after": wts_updates.get(10673)},
                    {"field": "tip1", "wts_id": 10674, "after": wts_updates.get(10674)},
                    {"field": "ubertip1", "wts_id": 20119, "after": wts_updates.get(20119)}
                ]
            }
        ]
    }
    (out_dir / "nightelf_selection.json").write_text(json.dumps(sel_data, ensure_ascii=False, indent=2), encoding="utf-8")
    print("Wrote nightelf_selection.json")

    # -------------------------------------------------------------
    # 2. nightelf_buildings.json
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
        "scope": f"Ночные эльфы (Night Elf): категория 1 — Здания ({len(bld_entries)} зданий)",
        "buildings_count": len(bld_entries),
        "variants": ["SD"],
        "buildings": bld_entries
    }
    (out_dir / "nightelf_buildings.json").write_text(json.dumps(bld_data, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"Wrote nightelf_buildings.json ({len(bld_entries)} buildings)")

    # -------------------------------------------------------------
    # 3. nightelf_units.json
    # -------------------------------------------------------------
    unit_entries = []
    all_units = dump["workers"] + dump["units"]
    seen_units = set()
    for u in all_units:
        u_id = u["id"]
        if u_id in seen_units or u_id not in plan["categories"]["units"]:
            continue
        seen_units.add(u_id)
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
        "scope": f"Ночные эльфы (Night Elf): категория 2 — Юниты ({len(unit_entries)} юнитов)",
        "units_count": len(unit_entries),
        "variants": ["SD"],
        "units": unit_entries
    }
    (out_dir / "nightelf_units.json").write_text(json.dumps(unit_data, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"Wrote nightelf_units.json ({len(unit_entries)} units)")

    # -------------------------------------------------------------
    # 4. nightelf_heroes.json
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
        "scope": f"Ночные эльфы (Night Elf): категория 3 — Герои ({len(hero_entries)} героев)",
        "heroes_count": len(hero_entries),
        "variants": ["SD"],
        "heroes": hero_entries
    }
    (out_dir / "nightelf_heroes.json").write_text(json.dumps(hero_data, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"Wrote nightelf_heroes.json ({len(hero_entries)} heroes)")

    # -------------------------------------------------------------
    # 5. nightelf_abilities.json
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
        "scope": f"Ночные эльфы (Night Elf): категория 4 — Способности ({len(abil_entries)} способностей)",
        "abilities_count": len(abil_entries),
        "variants": ["SD"],
        "abilities": abil_entries
    }
    (out_dir / "nightelf_abilities.json").write_text(json.dumps(abil_data, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"Wrote nightelf_abilities.json ({len(abil_entries)} abilities)")

    # -------------------------------------------------------------
    # 6. nightelf_research.json
    # -------------------------------------------------------------
    upg_entries = []
    upg_list = plan["categories"].get("research") or plan["categories"].get("upgrades") or []
    for u in dump["upgrades"]:
        u_id = u["id"]
        if u_id not in upg_list:
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
        "scope": f"Ночные эльфы (Night Elf): категория 5 — Исследования и маркеры ({len(upg_entries)} технологий)",
        "upgrades_count": len(upg_entries),
        "variants": ["SD"],
        "upgrades": upg_entries
    }
    (out_dir / "nightelf_research.json").write_text(json.dumps(upg_data, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"Wrote nightelf_research.json ({len(upg_entries)} upgrades)")

    # -------------------------------------------------------------
    # 7. nightelf_audit.json
    # -------------------------------------------------------------
    audit_data = {
        "race": "Ночные эльфы (Night Elf)",
        "race_id": 26,
        "selection_ability": "A0HL",
        "objects_audit": {
            "buildings": {
                "count": len(bld_entries),
                "ids": [b["id"] for b in bld_entries],
                "economy_building": {
                    "id": "emow",
                    "name": "Лунный колодец",
                    "food_provided": 40,
                    "gold_income_per_25s": 20,
                    "verified_via": "object data (fmade=40) and building description"
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
                    "E00V": "Хранитель рощи (Интеллект, дальний бой)",
                    "E011": "Лунная охотница (Катрис Звёздная Песня — Ловкость, дальний бой)",
                    "E00W": "Друид-мастер (Интеллект, дальний бой)"
                }
            },
            "abilities": {
                "count": len(abil_entries),
                "total_wts_updated": len(plan["wts_updates"])
            },
            "researches": {
                "count": len(upg_entries),
                "markers_list": {
                    "R07L": "Маркер расы Ночные эльфы",
                    "R0GB": "Служебный маркер выбора пути"
                }
            }
        },
        "items_audit": {
            "race_specific_items": [],
            "status": "No race-specific shop items or inventory artifacts found in war3map.w3t for Night Elf."
        },
        "messages_audit": {
            "race_specific_messages": [],
            "status": "No race-specific floating messages found in NightElf.lua."
        },
        "buffs_audit": {
            "custom_buffs": [],
            "status": "Standard melee and shared buffs used across abilities."
        },
        "total_wts_updates": len(plan["wts_updates"]),
        "total_checks": len(plan["checks_def"])
    }
    (out_dir / "nightelf_audit.json").write_text(json.dumps(audit_data, ensure_ascii=False, indent=2), encoding="utf-8")
    print("Wrote nightelf_audit.json")

if __name__ == "__main__":
    main()
