"""Guard byte preservation and valid v3 headers in the text-only object writer."""
import struct
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
from apply_faceless_object_text import patch_blob
from implement_draenei_rework import object_records


def modification(field, kind, value, end=b"e009"):
    return field.encode("ascii") + struct.pack("<I", kind) + value + end


def record(old, new, modifications):
    return (old + new + struct.pack("<II", 1, 0) + struct.pack("<I", len(modifications)) + b"".join(modifications))


def fixture(name_kind=3):
    # Preserve an unknown float with a noncanonical NaN bit pattern exactly.
    other = record(b"hfoo", b"\0" * 4, [modification("zzzz", 1, bytes.fromhex("0100c07f"), b"hfoo")])
    value = b"old title\0" if name_kind == 3 else struct.pack("<I", 123)
    target = record(b"espv", b"e009", [modification("unam", name_kind, value), modification("uhpm", 0, struct.pack("<I", 900))])
    return struct.pack("<II", 3, 1) + other + struct.pack("<I", 1) + target


class FacelessTextWriterTests(unittest.TestCase):
    def test_replaces_only_requested_string_and_keeps_unknown_numeric_bytes(self):
        original = fixture()
        updated, changes = patch_blob(original, [dict(id="e009", field="name", value="|cffebc56cКошмар|r")], "unit", True)
        _, before = object_records(original, False)
        _, after = object_records(updated, False)
        self.assertEqual(before[0][0]["raw"], after[0][0]["raw"])
        self.assertEqual(before[1][0]["header"], after[1][0]["header"])
        self.assertEqual(before[1][0]["mods"][1], after[1][0]["mods"][1])
        self.assertEqual(after[1][0]["mods"][0][1][8:-5].decode("utf-8"), "|cffebc56cКошмар|r")
        self.assertEqual(changes, [["e009", "unam", 0, 0]])

    def test_standard_unit_override_has_one_v3_set_and_no_numeric_modifications(self):
        original = fixture()
        updated, _ = patch_blob(original, [dict(id="nfgt", field="name", value="Щупальце", base_object=True)], "unit", True)
        _, before = object_records(original, False)
        _, after = object_records(updated, False)
        self.assertEqual(before[0][0]["raw"], after[0][0]["raw"])
        self.assertEqual(before[1][0]["raw"], after[1][0]["raw"])
        added = after[0][1]
        self.assertEqual(added["id"], "nfgt")
        # HiveWE and Warcraft consume a set flag after the v3 set count.
        self.assertEqual(struct.unpack_from("<II", added["header"], 8), (1, 0))
        self.assertEqual([key for key, _ in added["mods"]], [("unam", 0, 0)])
        self.assertEqual(struct.unpack_from("<I", added["mods"][0][1], 4)[0], 3)

    def test_refuses_unknown_unit_without_an_audited_base_override(self):
        with self.assertRaises(AssertionError):
            patch_blob(fixture(), [dict(id="new1", field="name", value="Title")], "unit", True)

    def test_refuses_to_replace_a_numeric_modification_with_text(self):
        with self.assertRaises(AssertionError):
            patch_blob(fixture(name_kind=0), [dict(id="e009", field="name", value="Title")], "unit", True)


if __name__ == "__main__":
    unittest.main()
