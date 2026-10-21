"""Splice only named string modifications; preserve every unrelated byte record.

Unlike a general editor save, this does not normalize object data or skin files.
All effective text is read back in both SD and HD on a staged map before publish.
"""
import hashlib
import json
import re
import shutil
import struct
import sys
import tempfile
from pathlib import Path

from faceless_text_batch import ROOT
from implement_draenei_rework import object_records
from wc3_object_tools import cli, require
from wc3_hivewe import load_wts_strings

FIELDS = {
    "unit": {"name": "unam", "tip": "utip", "ubertip": "utub", "propernames": "upro", "awakentip": "uawt", "revivetip": "utpr"},
    "ability": {"name": "anam", "tip": "atp1", "ubertip": "aub1", "untip": "aut1", "unubertip": "auu1", "researchtip": "aret", "researchubertip": "arut", "requires": "areq"},
    "upgrade": {"name": "gnam", "tip": "gtp1", "ubertip": "gub1"},
    "buff": {"name": "fnam", "tip": "ftip", "ubertip": "fube", "editorname": "fnam", "bufftip": "ftip", "buffubertip": "fube"},
    "item": {"name": "unam", "tip": "utip", "ubertip": "utub", "description": "ides"},
}
EXTENSIONS = {"unit": "w3u", "ability": "w3a", "upgrade": "w3q", "buff": "w3h", "item": "w3t"}


def field_key(kind, field):
    import re
    match = re.fullmatch(r"(name|tip|ubertip|untip|unubertip)(\d+)", field)
    if match:
        return FIELDS[kind][match[1]], int(match[2]), 0
    return FIELDS[kind][field], 0, 0


def patch_blob(original, operations, kind, add_missing):
    extended = kind in ("ability", "upgrade")
    version, tables = object_records(original, extended)
    by_id = {}
    for op in operations:
        key = field_key(kind, op["field"])
        by_id.setdefault(op["id"], {})[key] = op["value"]
    output = bytearray(struct.pack("<I", version))
    changed = []
    known = {r["id"] for table in tables for r in table}
    base_overrides = {op["id"] for op in operations if op.get("base_object")}
    audited_bases = {"unit": {"nfgt", "uloc"}, "ability": {"Arst", "Argl", "Sch5"},
                     "buff": {"BEim", "BHab", "BHds", "BHtc", "BIcb", "BNab", "BNht", "BOsf", "BOwd", "BOwk", "BPSE", "BUan", "BUdd", "BUfa", "BUsl", "Bakb", "Bcrs", "Bena", "Beng", "Bfro", "Brej", "Bslo", "Bspl", "Bvng", "BEar", "BHad", "BOae"}}
    audited_bases["upgrade"] = {"Rugf", "Rhrt", "Rhlh", "Rhan"}
    assert base_overrides <= audited_bases.get(kind, set()), "Only audited standard objects may get new text overrides"
    if add_missing:
        assert set(by_id) - known <= base_overrides, "Target must have a main object record"
        # A standard unit can inherit all fields from CASC without a map record.
        # Add only string overrides in the original-object table, preserving base data.
        for code in sorted(set(by_id) - known):
            assert kind in ("unit", "ability", "buff", "upgrade")
            header = code.encode("ascii") + b"\0" * 4
            if version >= 3:
                header += struct.pack("<II", 1, 0)
            tables[0].append(dict(id=code, header=header, mods=[], raw=None))
    for table in tables:
        output += struct.pack("<I", len(table))
        for record in table:
            if record["id"] not in by_id:
                output += record["raw"]
                continue
            wanted = by_id[record["id"]]
            pending = set(wanted)
            mods = []
            for key, raw in record["mods"]:
                if key in wanted:
                    assert struct.unpack_from("<I", raw, 4)[0] == 3, key
                    offset = 16 if extended else 8
                    modified = raw[:offset] + wanted[key].encode("utf-8") + b"\0" + raw[-4:]
                    mods.append(modified)
                    pending.discard(key)
                    if modified != raw:
                        changed.append([record["id"], *key])
                else:
                    mods.append(raw)
            if add_missing:
                for key in sorted(pending):
                    raw = key[0].encode("ascii") + struct.pack("<I", 3)
                    if extended:
                        raw += struct.pack("<II", key[1], key[2])
                    raw += wanted[key].encode("utf-8") + b"\0" + record["header"][4:8]
                    mods.append(raw)
                    changed.append([record["id"], *key])
            output += record["header"] + struct.pack("<I", len(mods)) + b"".join(mods)
    # Independently prove preservation of every non-target record/modification.
    _, original_tables = object_records(original, extended)
    _, verified = object_records(bytes(output), extended)
    for before_table, after_table in zip(original_tables, verified):
        after_lookup = {record["id"]: record for record in after_table}
        assert set(after_lookup) - {record["id"] for record in before_table} <= base_overrides
        for before in before_table:
            after = after_lookup[before["id"]]
            assert before["id"] == after["id"]
            if before["id"] not in by_id:
                assert before["raw"] == after["raw"]
            else:
                allowed = by_id[before["id"]]
                assert before["header"] == after["header"]
                assert [(k, r) for k, r in before["mods"] if k not in allowed] == [(k, r) for k, r in after["mods"] if k not in allowed]
    return bytes(output), changed


def main():
    plan_path = Path(sys.argv[1]).resolve()
    operations = json.loads(plan_path.read_text(encoding="utf-8"))["operations"]
    for op in operations:
        assert isinstance(op["value"], str) and "\0" not in op["value"]
        assert "\ufffd" not in op["value"] and not re.search(r"\?{3,}", op["value"]), "Possible text encoding corruption"
        field_key(op["type"], op["field"])
    source = ROOT / "map.w3x"
    hashes = {p.name: hashlib.sha256(p.read_bytes()).hexdigest() for p in source.glob("war3map*") if p.is_file()}
    with tempfile.TemporaryDirectory(prefix="faceless-text-", dir=ROOT / ".cache/wc3") as temporary:
        stage = Path(temporary)
        for name in hashes:
            shutil.copy2(source / name, stage / name)
        changed, checks = {}, []
        for kind in {op["type"] for op in operations}:
            ops = [op for op in operations if op["type"] == kind]
            for prefix in ("war3map", "war3mapSkin"):
                path = stage / (prefix + "." + EXTENSIONS[kind])
                if not path.exists():
                    continue
                updated, changes = patch_blob(path.read_bytes(), ops, kind, prefix == "war3map")
                if changes:
                    path.write_bytes(updated)
                    changed[path.name] = changes
            for hd in (False, True):
                ids = sorted({op["id"] for op in ops})
                fields = sorted({op["field"] for op in ops})
                args = ["get-objects-bulk", "--type", kind, "--ids", ",".join(ids), "--fields", ",".join(fields)]
                if hd:
                    args.append("--hd")
                data = require(cli(args, stage))
                if "objects" not in data:
                    raise ValueError("Object readback returned no objects: " + json.dumps(data, ensure_ascii=False))
                found = {obj["id"]: obj["fields"] for obj in data["objects"]}
                wts = load_wts_strings(stage / "war3map.wts")
                for op in ops:
                    actual = found[op["id"]][op["field"]]
                    if actual.startswith("TRIGSTR_"):
                        actual = wts[int(actual[8:])]
                    assert actual == op["value"], (hd, op["id"], op["field"], actual)
                    checks.append(dict(variant="HD" if hd else "SD", rawcode=op["id"], field=op["field"], exact_match=True))
        # No writer may have changed the workspace while the stage was checked.
        assert all(hashlib.sha256((source / name).read_bytes()).hexdigest() == digest for name, digest in hashes.items())
        backup = ROOT / ".cache/wc3" / (plan_path.stem + "_before")
        backup.mkdir(exist_ok=True)
        for name in changed:
            shutil.copy2(source / name, backup / name)
            shutil.copy2(stage / name, source / name)
        report = dict(ok=True, applied=True, method="Only explicit string modifications spliced; all unrelated records/mods byte-identical",
                      changes=changed, checks=checks, wts_unchanged=hashlib.sha256((source / "war3map.wts").read_bytes()).hexdigest() == hashes["war3map.wts"])
        plan_path.with_name(plan_path.stem.replace("_plan", "") + "_object_apply.json").write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        print(json.dumps(dict(ok=True, operations=len(operations), checked_fields=len(checks), files=list(changed))))


if __name__ == "__main__":
    main()
