"""Synchronize renamed ability references in the related unit/building cards."""
import json
from faceless_text_batch import ROOT
from wc3_object_tools import cli, require
from wc3_hivewe import load_wts_strings


def main():
    wts = load_wts_strings()
    resolve = lambda s: wts[int(s[8:])] if s.startswith("TRIGSTR_") else s
    replacements = {"Стать слугой Йогг`Сарона": "Служение Йогг`Сарону", "Породить придаток": "Порождение придатка", "Породить Кошмар": "Порождение Кошмара"}
    ops, strings, sources = [], [], []
    for kind, ids, fields in [("unit", "U02F,h0HZ,h0I7,h0I8,u02E,h0K2", "ubertip,isbldg"),
                              ("ability", "A16N", "name,tip1,ubertip1")]:
        data = require(cli(["get-objects-bulk", "--type", kind, "--ids", ids, "--fields", fields]))
        sources.append(data)
        for obj in data["objects"]:
            for field, value in obj["fields"].items():
                if field == "isbldg":
                    continue
                before = resolve(value)
                after = before
                for old, new in replacements.items():
                    after = after.replace(old, new)
                if before == after:
                    continue
                op = dict(type=kind, id=obj["id"], field=field, value=after)
                if kind == "unit":
                    op["marker"] = "ЗДАНИЕ:" if obj["fields"]["isbldg"] == "1" else "ГЕРОЙ:" if obj["id"][0].isupper() else "ЮНИТ:"
                ops.append(op)
                strings.append(dict(rawcode=obj["id"], field=field, before=before, after=after))
    folder = ROOT / "docs/ui_text"
    inv = dict(scope="Согласование названий Служения, Порождения придатка и Порождения Кошмара", sources=sources, strings=strings, in_game_checked=False)
    for name, value in [("faceless_name_sync", inv), ("faceless_name_sync_plan", dict(operations=ops))]:
        (folder / (name + ".json")).write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
