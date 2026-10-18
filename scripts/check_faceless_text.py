"""Read back the migrated batches in SD/HD and check text formatting."""
import json
import re
from pathlib import Path

from wc3_object_tools import cli, require
from wc3_hivewe import load_wts_strings

ROOT = Path(__file__).resolve().parent.parent
PALETTE = {"ced4da", "ffffff", "c8e087", "e69a8d", "e6c07b", "e4cfa3", "a6afb8", "a9c7de"}


def main():
    checks = []
    errors = []
    wts = load_wts_strings()
    filenames = ("faceless_units_01_plan.json", "faceless_units_02_plan.json", "faceless_abilities_01_plan.json", "faceless_abilities_02_plan.json", "faceless_heroes_plan.json", "faceless_research_plan.json", "faceless_shards_plan.json", "faceless_related_cards_plan.json", "faceless_hero_abilities_plan.json", "faceless_remaining_abilities_plan.json", "faceless_summons_plan.json", "faceless_yogg_unlocks_plan.json", "faceless_name_sync_plan.json", "faceless_custom_buffs_plan.json", "faceless_shared_commands_plan.json", "faceless_markers_plan.json", "faceless_shared_buffs_plan.json")
    filenames += ("faceless_teleport_mage_plan.json", "faceless_naval_research_plan.json", "faceless_naval_abilities_plan.json")
    filenames += ("faceless_flagship_plan.json", "faceless_naval_cards_plan.json")
    filenames += ("faceless_ulduar_plan.json", "faceless_naval_buffs_plan.json")
    filenames += ("faceless_cosmetic_plan.json",)
    filenames += ("faceless_trade_plan.json",)
    filenames += ("faceless_requirement_names_plan.json",)
    filenames = ("faceless_initial_batches_plan.json",) + filenames
    plans = {filename: json.loads((ROOT / "docs/ui_text" / filename).read_text(encoding="utf-8")) for filename in filenames}
    owners = {(op["type"], op["id"], op["field"]): filename for filename, plan in plans.items() for op in plan["operations"]}
    effective = [op for filename, plan in plans.items() for op in plan["operations"] if owners[(op["type"], op["id"], op["field"])] == filename]
    actual_cache = {}
    for kind in {op["type"] for op in effective}:
        relevant = [op for op in effective if op["type"] == kind]
        ids = sorted({op["id"] for op in relevant})
        fields = sorted({op["field"] for op in relevant})
        for variant in ("SD", "HD"):
            args = ["get-objects-bulk", "--type", kind, "--ids", ",".join(ids), "--fields", ",".join(fields)]
            if variant == "HD":
                args.append("--hd")
            data = require(cli(args))
            actual_cache[kind, variant] = {obj["id"]: obj["fields"] for obj in data["objects"]}
    for filename in filenames:
        plan = {"operations": [op for op in plans[filename]["operations"] if owners[(op["type"], op["id"], op["field"])] == filename]}
        for variant in ("SD", "HD"):
            for kind in {op["type"] for op in plan["operations"]}:
                ops = [op for op in plan["operations"] if op["type"] == kind]
                actual = actual_cache[kind, variant]
                for op in ops:
                    value = actual[op["id"]][op["field"]]
                    reference = value
                    if value.startswith("TRIGSTR_"):
                        value = wts[int(value[8:])]
                    label = variant + ":" + op["id"] + "." + op["field"]
                    if value != op["value"]:
                        errors.append(label + ": readback mismatch")
                    if "\ufffd" in value or re.search(r"\?{3,}", value):
                        errors.append(label + ": possible text encoding corruption")
                    colors = set(re.findall(r"\|cff([0-9a-fA-F]{6})", value))
                    if {color.lower() for color in colors} - PALETTE:
                        errors.append(label + ": unknown palette color")
                    controls = re.findall(r"\|c[0-9a-fA-F]{8}|\|r", value)
                    if not controls or controls[-1] != "|r" or value.endswith("|n|r"):
                        errors.append(label + ": missing reset / trailing newline")
                    plain = re.sub(r"\|c[0-9a-fA-F]{8}|\|r", "", value)
                    if op["field"].startswith(("ubertip", "unubertip")) or op["field"] in ("researchubertip", "buffubertip", "description"):
                        marker = (("ГЕРОЙ:" if op["id"][0].isupper() else "ЮНИТ:") if kind == "unit" else
                                  "ИССЛЕДОВАНИЕ:" if kind == "upgrade" else "ЭФФЕКТ:" if kind == "buff" else "ПРЕДМЕТ:" if kind == "item" else "СПОСОБНОСТЬ:")
                        marker = op.get("marker", marker)
                        if not value.startswith("|cffa6afb8" + marker + "|cffced4da "):
                            errors.append(label + ": incorrect type marker")
                    elif re.match(r"(?i)(обучить|нанять|построить|исследовать|изучить|призвать|породить|активировать|отключить|train|hire|build|research|summon|learn)\b", plain):
                        errors.append(label + ": command prefix")
                    checks.append(dict(variant=variant, rawcode=op["id"], field=op["field"],
                                       reference=reference, exact_match=value == op["value"]))
    interface = json.loads((ROOT / "docs/ui_text/faceless_interface.json").read_text(encoding="utf-8"))
    for row in interface["strings"]:
        sid = int(row["reference_before"][8:])
        value = wts[sid]
        label = "FrameDef:" + str(sid)
        if value != row["after"]:
            errors.append(label + ": readback mismatch")
        if "\ufffd" in value or re.search(r"\?{3,}", value):
            errors.append(label + ": possible text encoding corruption")
        if {c.lower() for c in re.findall(r"\|cff([0-9a-fA-F]{6})", value)} - PALETTE:
            errors.append(label + ": unknown palette color")
        controls = re.findall(r"\|c[0-9a-fA-F]{8}|\|r", value)
        if not controls or controls[-1] != "|r":
            errors.append(label + ": missing reset")
        checks.append(dict(variant="WTS", rawcode="FrameDef", field=str(sid), exact_match=value == row["after"]))
    report = dict(ok=not errors, checks=checks, errors=errors,
                  limitations=["Checks only the explicitly listed migrated batches.",
                               "Does not prove gameplay effects or visual fit in Warcraft III."])
    output = ROOT / "docs/ui_text/faceless_batches_check.json"
    output.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(dict(ok=not errors, checked_fields=len(checks), errors=errors), ensure_ascii=False))
    raise SystemExit(bool(errors))


if __name__ == "__main__":
    main()
