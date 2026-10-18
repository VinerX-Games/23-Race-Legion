"""Audit saved race inventories against explicit text batches, without editing map data."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
FOLDER = ROOT / "docs/ui_text"


def main():
    initial = []
    related = {
        row["reference_before"]: row["after"]
        for row in json.loads((FOLDER / "faceless_units_02.json").read_text(encoding="utf-8"))["strings"]
        if row.get("rawcode") == "related"
    }
    for filename, kind, marker in (
        ("faceless_selection.json", "ability", None),
        ("faceless_buildings_01.json", "unit", "ЗДАНИЕ:"),
        ("faceless_buildings_02.json", "unit", "ЗДАНИЕ:"),
        ("faceless_altar.json", "unit", "ЗДАНИЕ:"),
        ("shared_teleport_mage.json", "unit", "ЮНИТ:"),
    ):
        inventory = json.loads((FOLDER / filename).read_text(encoding="utf-8"))
        for row in inventory["strings"]:
            value = related.get("TRIGSTR_" + str(row.get("wts_id")), row["after"])
            op = dict(type=kind, id=row["rawcode"], field=row["field"], value=value)
            if marker:
                op["marker"] = marker
            elif filename == "faceless_selection.json":
                op["marker"] = "РАСА:"
            initial.append(op)
    (FOLDER / "faceless_initial_batches_plan.json").write_text(json.dumps(dict(operations=initial), ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    covered = set()
    for filename in FOLDER.glob("*_plan.json"):
        for op in json.loads(filename.read_text(encoding="utf-8")).get("operations", []):
            covered.add((op["type"], op["id"], op["field"]))
    excluded = {"n01P", "n01Q", "n01R", "n01S", "n01U"}
    report = []
    for kind in ("unit", "ability", "upgrade", "buff", "item"):
        for obj in json.loads((FOLDER / f"faceless_{kind}_inventory.json").read_text(encoding="utf-8")):
            code = obj["id"]
            if code in excluded and kind == "unit":
                report.append(dict(type=kind, id=code, status="unavailable_legacy", evidence="faceless_legacy_reachability.json"))
                continue
            required = ("name", "tip", "ubertip") if kind == "unit" else ("name", "tip1", "ubertip1") if kind == "ability" else ("name1", "tip1", "ubertip1")
            missing = [f for f in required if (kind, code, f) not in covered]
            report.append(dict(type=kind, id=code, status="missing_text_batch" if missing else "batch_present", missing=missing))
    output = dict(ok=all(r["status"] != "missing_text_batch" for r in report), inventory=report,
                  limitations=["Saved race-suffix inventory only; shared dependencies and Lua-created forms need separate reachability audit",
                               "Presence of a batch does not prove gameplay effects, all levels, current readback or UI rendering",
                               "Current SD/HD values are checked independently by check_faceless_text.py"])
    (FOLDER / "faceless_inventory_coverage.json").write_text(json.dumps(output, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(dict(ok=output["ok"], inventory_objects=len(report), missing=[r for r in report if r["status"] == "missing_text_batch"])))


if __name__ == "__main__":
    main()
