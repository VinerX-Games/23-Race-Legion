# -*- coding: utf-8 -*-
"""Generate standardized JSON category registries for Race 15: Blood Elves (Эльфы Крови) in docs/ui_text/

Outputs:
- docs/ui_text/blood_elves_selection.json
- docs/ui_text/blood_elves_buildings.json
- docs/ui_text/blood_elves_units.json
- docs/ui_text/blood_elves_heroes.json
- docs/ui_text/blood_elves_abilities.json
- docs/ui_text/blood_elves_research.json
- docs/ui_text/blood_elves_audit.json
"""
import json
from pathlib import Path
import sys

sys.stdout.reconfigure(encoding='utf-8')
ROOT = Path(__file__).resolve().parent.parent

def main():
    plan_path = ROOT / "docs/ui_text/blood_elves_plan.json"
    dump_path = ROOT / "scripts/blood_elves_raw_dump.json"
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
    # 1. blood_elves_selection.json
    # -------------------------------------------------------------
    sel_data = {
        "scope": "Эльфы Крови (Blood Elves): подсказка выбора расы A0HQ и маркеры",
        "object": "A0HQ",
        "variants": ["SD"],
        "hotkey": {
            "value": "E"
        },
        "levels": 1,
        "evidence": [
            "04_race_selection.lua: InitTrig_Race_BloodElves фильтрует способность A0HQ.",
            "При выборе создаются стартовые здания и юниты Эльфов Крови, исследуются маркеры R07C, R0L0.",
            "Горячая клавиша E, создатель VinerX, сложность 3/5 (Средняя), период «Burning Crusade — Legion»."
        ],
        "strings": [
            {
                "field": "name",
                "wts_id": 38917,
                "after": wts_updates[38917]
            },
            {
                "field": "tip1",
                "wts_id": 38918,
                "after": wts_updates[38918]
            },
            {
                "field": "ubertip1",
                "wts_id": 41060,
                "after": wts_updates[41060]
            }
        ],
        "markers": [
            {
                "id": "R07C",
                "name": "Эльфы Крови (маркер расы)",
                "strings": [
                    {"field": "name1", "wts_id": 7984, "after": wts_updates.get(7984)},
                    {"field": "tip1", "wts_id": 7985, "after": wts_updates.get(7985)},
                    {"field": "ubertip1", "wts_id": 20110, "after": wts_updates.get(20110)}
                ]
            },
            {
                "id": "R0L0",
                "name": "Эльфы Крови или Иллидари (общий маркер)",
                "strings": [
                    {"field": "name1", "wts_id": 12039, "after": wts_updates.get(12039)},
                    {"field": "tip1", "wts_id": 12062, "after": wts_updates.get(12062)},
                    {"field": "ubertip1", "wts_id": 20115, "after": wts_updates.get(20115)}
                ]
            }
        ]
    }
    (out_dir / "blood_elves_selection.json").write_text(json.dumps(sel_data, ensure_ascii=False, indent=2), encoding="utf-8")
    print("Wrote blood_elves_selection.json")

    # -------------------------------------------------------------
    # 2. blood_elves_buildings.json
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
        "scope": f"Эльфы Крови (Blood Elves): категория 1 — Здания ({len(bld_entries)} зданий)",
        "buildings_count": len(bld_entries),
        "variants": ["SD"],
        "buildings": bld_entries
    }
    (out_dir / "blood_elves_buildings.json").write_text(json.dumps(bld_data, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"Wrote blood_elves_buildings.json ({len(bld_entries)} buildings)")

    # -------------------------------------------------------------
    # 3. blood_elves_units.json
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
        "scope": f"Эльфы Крови (Blood Elves): категория 2 — Юниты ({len(unit_entries)} юнитов)",
        "units_count": len(unit_entries),
        "variants": ["SD"],
        "units": unit_entries
    }
    (out_dir / "blood_elves_units.json").write_text(json.dumps(unit_data, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"Wrote blood_elves_units.json ({len(unit_entries)} units)")

    # -------------------------------------------------------------
    # 4. blood_elves_heroes.json
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
        "scope": f"Эльфы Крови (Blood Elves): категория 3 — Герои ({len(hero_entries)} героев)",
        "heroes_count": len(hero_entries),
        "variants": ["SD"],
        "heroes": hero_entries
    }
    (out_dir / "blood_elves_heroes.json").write_text(json.dumps(hero_data, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"Wrote blood_elves_heroes.json ({len(hero_entries)} heroes)")

    # -------------------------------------------------------------
    # 5. blood_elves_abilities.json
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
        "scope": f"Эльфы Крови (Blood Elves): категория 4 — Способности ({len(abil_entries)} способностей)",
        "abilities_count": len(abil_entries),
        "variants": ["SD"],
        "abilities": abil_entries
    }
    (out_dir / "blood_elves_abilities.json").write_text(json.dumps(abil_data, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"Wrote blood_elves_abilities.json ({len(abil_entries)} abilities)")

    # -------------------------------------------------------------
    # 6. blood_elves_research.json
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
        "scope": f"Эльфы Крови (Blood Elves): категория 5 — Исследования и маркеры ({len(upg_entries)} технологий)",
        "upgrades_count": len(upg_entries),
        "variants": ["SD"],
        "upgrades": upg_entries
    }
    (out_dir / "blood_elves_research.json").write_text(json.dumps(upg_data, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"Wrote blood_elves_research.json ({len(upg_entries)} upgrades)")

    # -------------------------------------------------------------
    # 7. blood_elves_audit.json
    # -------------------------------------------------------------
    audit_data = {
        "race": "Эльфы Крови (Blood Elves)",
        "race_id": 15,
        "selection_ability": "A0HQ",
        "objects_audit": {
            "buildings": {
                "count": len(bld_entries),
                "ids": [b["id"] for b in bld_entries],
                "economy_building": {
                    "id": "h04M",
                    "name": "Сторожка",
                    "food_provided": 15,
                    "gold_income_per_25s": 40,
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
                    "H043": "Маг Крови (Интеллект, дальний бой)",
                    "Hjnd": "Ренджер (Ловкость, дальний бой)",
                    "H045": "Верховный Рыцарь Крови (Сила, ближний бой)",
                    "H044": "Верховный Магистр Роммат (Интеллект, дальний бой, столица)",
                    "H05H": "Матриарх Рыцарей Крови Леди Лиадрин (Сила, ближний бой, столица)",
                    "H05I": "Лорд-Регент Лортемар Терон (Ловкость, дальний бой, столица)",
                    "Hkal": "Принц Кель'тас (Интеллект, дальний бой, особый герой)"
                }
            },
            "abilities": {
                "count": len(abil_entries),
                "total_wts_updated": len(plan["wts_updates"])
            },
            "researches": {
                "count": len(upg_entries),
                "mutually_exclusive_priorities": {
                    "R025": "Ведьмаки (Q) — улучшает защиту и запас маны ведьмаков",
                    "R026": "Рыцари крови (W) — усиливает броню и ауры рыцарей крови",
                    "R03C": "Странники (E) — повышает меткость и скорость атаки следопытов",
                    "R03D": "Анклав магов (R) — ускоряет восстановление маны и силу заклинаний",
                    "trigger_enforcement": "Взаимная отмена при исследовании через Lua-триггеры"
                },
                "specialization_wells": {
                    "R01D": "Аркана (Arcana) — превращает святилище в Колодец арканы",
                    "R01G": "Скверна (Fel) — превращает святилище в Колодец скверны",
                    "R01H": "Бездна (Void) — превращает святилище в Колодец бездны",
                    "R01I": "Свет (Light) — превращает святилище в Колодец света"
                },
                "markers_list": {
                    "R07C": "Маркер расы Эльфы Крови (Син'Дорай)",
                    "R0L0": "Маркер Эльфы Крови или Иллидари"
                }
            }
        },
        "items_audit": {
            "race_specific_items": [],
            "status": "No race-specific shop items or inventory artifacts found in war3map.w3t for Blood Elves."
        },
        "messages_audit": {
            "race_specific_messages": [],
            "status": "No race-specific floating messages or game UI strings found in war3map.wts for Blood Elves."
        },
        "buffs_audit": {
            "custom_buffs": [],
            "standard_buffs_used": [
                "Bblo", "Bpxf", "Bfae", "Bcyc", "Bfro", "Bpoi", "Bdef", "BOac", "Bcri", "Bspe", "Bshs"
            ],
            "status": "All buffs used by Blood Elves abilities are standard Warcraft III engine buffs. No custom text modification required."
        },
        "total_wts_updates": len(plan["wts_updates"]),
        "total_checks": len(plan["checks_def"])
    }
    (out_dir / "blood_elves_audit.json").write_text(json.dumps(audit_data, ensure_ascii=False, indent=2), encoding="utf-8")
    print("Wrote blood_elves_audit.json")

if __name__ == "__main__":
    main()
