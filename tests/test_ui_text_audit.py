"""Protect inventory boundaries: comments must not become translated UI text."""
import sys
import unittest
import json
import tempfile
import struct
import io
import hashlib
from contextlib import redirect_stdout
from unittest.mock import patch
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
from audit_ui_text import LUA_TOKEN, plain
import faceless_text_batch
import audit_ui_text


def literals(source):
    values = []
    for match in LUA_TOKEN.finditer(source):
        value = match["long"] if match["long"] is not None else match["quoted"]
        if value is not None:
            values.append(value)
    return values


class UiTextInventoryTests(unittest.TestCase):
    def test_comments_with_quotes_do_not_become_ui_candidates(self):
        source = '-- "comment"\n--[=[ "comment" ]=]\nDisplayText("Visible text")'
        self.assertEqual(literals(source), ["Visible text"])

    def test_escaped_quotes_and_comment_marker_inside_string(self):
        source = r'''DisplayText("He said \"hello\" -- still text", 'second')'''
        self.assertEqual(literals(source), [r'He said \"hello\" -- still text', "second"])

    def test_long_string_requires_matching_equals_delimiter(self):
        source = 'DisplayText([==[First ]] and ]=] then\nsecond line]==])'
        self.assertEqual(literals(source), ['First ]] and ]=] then\nsecond line'])

    def test_log_classification_uses_enclosing_call_not_previous_statement(self):
        source = 'ProbeLogWrite(string.format("log %s", "value")); DisplayText("player text")'
        found = [(m["quoted"], calls) for m, calls in audit_ui_text.lua_literals_with_calls(source)]
        self.assertEqual(found[0], ('log %s', ('ProbeLogWrite', 'string.format')))
        self.assertEqual(found[1], ('value', ('ProbeLogWrite', 'string.format')))
        self.assertEqual(found[2], ('player text', ('DisplayText',)))

    def test_menu_preview_preserves_unrequested_training_and_morph_paragraph(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            out = root / "docs/ui_text"
            out.mkdir(parents=True)
            races = root / "docs/techtree/races"
            races.mkdir(parents=True)
            original = ('|cffb99d66ЗДАНИЕ:|cffced4da Военный лагерь.'
                        '|n|nОбучает:|n- Рыцарь.'
                        '|n|nИсследования:|n- Старое название.'
                        '|n|nПерестраивается в:|n- Магическая башня.|r')
            audit_ui_text.write_json(out / "global_effective.json", {"sources": {}, "rows": [
                {"type": "unit", "id": "h0H4", "variant": v, "field": "ubertip", "text": original}
                for v in ("SD", "HD")]})
            audit_ui_text.write_json(races / "fixture.json", {
                "objects": {"Rfoo": {"type": "upgrade", "name": "Выучка рыцарей"},
                            "ufoo": {"type": "unit", "name": "Рыцарь"}},
                "edges": ["h0H4 researches Rfoo", "h0H4 trains ufoo"]})
            plan = out / "plan.json"
            audit_ui_text.write_json(plan, {"requests": [{"id": "h0H4", "sections": ["researches"]}]})
            with patch.multiple(audit_ui_text, ROOT=root, OUT=out), redirect_stdout(io.StringIO()):
                audit_ui_text.prepare_menu_batch(plan)
            result = json.loads(plan.read_text(encoding="utf-8"))["operations"][0]["value"]
            self.assertIn('Обучает:|n- Рыцарь.', result)
            self.assertIn('Перестраивается в:|n- Магическая башня.|r', result)
            self.assertIn('Выучка рыцарей', result)
            self.assertNotIn('Старое название', result)
            request = {"id": "h0H4", "sections": ["researches"], "reset_description": True,
                       "intro": "Подготавливает войска и исследует улучшения."}
            audit_ui_text.write_json(plan, {"requests": [request]})
            with patch.multiple(audit_ui_text, ROOT=root, OUT=out), redirect_stdout(io.StringIO()):
                with self.assertRaisesRegex(AssertionError, "Full replacement must include all confirmed menus"):
                    audit_ui_text.prepare_menu_batch(plan)
                request["sections"] = ["trains", "researches"]
                audit_ui_text.write_json(plan, {"requests": [request]})
                audit_ui_text.prepare_menu_batch(plan)
            replacement = json.loads(plan.read_text(encoding="utf-8"))["operations"][0]["value"]
            self.assertTrue(audit_ui_text.plain(replacement).startswith('ЗДАНИЕ:'))
            self.assertIn('Рыцарь', replacement)
            self.assertIn('Выучка рыцарей', replacement)

    def test_manual_visibility_review_is_revoked_when_source_changes(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            out = root / "docs/ui_text"
            out.mkdir(parents=True)
            map_path = root / "map.w3x"
            source = map_path / "_lua/monolith_split/sections/example.lua"
            source.parent.mkdir(parents=True)
            source.write_text('local label = "Visible sentence"; local x=1', encoding="utf-8")
            (map_path / "war3map.wts").write_text("", encoding="utf-8")
            script = root / "scripts/audit_ui_text.py"
            script.parent.mkdir()
            script.write_text("fixture", encoding="utf-8")
            relative = source.relative_to(root).as_posix()
            audit_ui_text.write_json(out / "global_lua_classification.json", {
                "sources": {relative: hashlib.sha256(source.read_bytes()).hexdigest()},
                "rows": [{"source": relative, "line": 1, "text": "Visible sentence",
                          "classification": "player_ui_data_requires_content_review", "reason": "Fixture review"}]})
            with patch.multiple(audit_ui_text, ROOT=root, MAP=map_path, OUT=out, __file__=str(script)):
                with redirect_stdout(io.StringIO()):
                    audit_ui_text.main()
                first = json.loads((out / "global_inventory.json").read_text(encoding="utf-8"))
                self.assertEqual(first["lua_candidates"][0]["classification"], "player_ui_data_requires_content_review")
                # Keep the literal and its line unchanged: only the source hash
                # distinguishes this unreviewed version from the approved one.
                source.write_text('local label = "Visible sentence"; local x=2', encoding="utf-8")
                with redirect_stdout(io.StringIO()):
                    audit_ui_text.main()
                second = json.loads((out / "global_inventory.json").read_text(encoding="utf-8"))
                self.assertEqual(second["lua_candidates"][0]["classification"], "needs_ui_or_debug_review")

    def test_colored_type_and_hotkey_are_visible_to_style_scan(self):
        self.assertEqual(plain('|cffb99d66СПОСОБНОСТЬ:|cffced4da Текст.|n|r'),
                         'СПОСОБНОСТЬ: Текст.')
        self.assertEqual(plain('|cffebc56cНазвание|r (|cffffffffW|r)'), 'Название (W)')

    def test_wts_batch_matches_padded_ids_and_preserves_other_bytes(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / "map.w3x").mkdir()
            path = root / "map.w3x/war3map.wts"
            original = b'STRING 043\r\n{\r\nBefore\r\n}\r\nSTRING 1043\r\n{\r\nOther\r\n}\r\n'
            path.write_bytes(original)
            binary = root / "map.w3x/war3map.w3u"
            binary.write_bytes(b'untouched\x00\xff')
            plan = root / "batch.json"
            plan.write_text(json.dumps({"strings": [{"reference_before": "TRIGSTR_043",
                                                     "before": "Before", "after": "После"}]}), encoding="utf-8")
            with patch.object(faceless_text_batch, "ROOT", root):
                result = faceless_text_batch.apply_wts_batch(plan)
            self.assertEqual(result["changed_wts_ids"], [43])
            self.assertEqual(path.read_bytes(), original.replace(b'Before', 'После'.encode('utf-8')))
            self.assertEqual(binary.read_bytes(), b'untouched\x00\xff')

    def test_technical_wts_consumers_are_not_mistaken_for_unreferenced_text(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            map_path, out = root / "map.w3x", root / "docs/ui_text"
            map_path.mkdir()
            out.mkdir(parents=True)
            script = root / "scripts/audit_ui_text.py"
            script.parent.mkdir()
            script.write_text("fixture", encoding="utf-8")
            (map_path / "war3map.wts").write_bytes(
                b'STRING 043\n{\nQ\n}\nSTRING 044\n{\nUnused prose\n}\nSTRING 045\n{\nratx\n}\n')
            mods = []
            for field, sid in [("ghk1", 43), ("gef1", 45)]:
                mods.append(field.encode() + struct.pack("<III", 3, 1, 0)
                            + f"TRIGSTR_{sid:03d}".encode() + b"\0" + b"\0" * 4)
            blob = (struct.pack("<II", 2, 1) + b"Rfoo" + b"\0" * 4
                    + struct.pack("<I", len(mods)) + b"".join(mods) + struct.pack("<I", 0))
            (map_path / "war3map.w3q").write_bytes(blob)
            with patch.multiple(audit_ui_text, ROOT=root, MAP=map_path, OUT=out, __file__=str(script)):
                with redirect_stdout(io.StringIO()):
                    audit_ui_text.main()
            result = json.loads((out / "global_inventory.json").read_text(encoding="utf-8"))
            strings = {r["sid"]: r for r in result["wts"]}
            self.assertEqual(strings[43]["roles"], ["hotkey"])
            self.assertEqual(strings[45]["roles"], ["effect_rawcode"])
            self.assertEqual(strings[43]["classification"], "technical_or_editor")
            self.assertEqual(len(strings[43]["references"]), 1)
            self.assertEqual(strings[44]["classification"], "unreferenced_legacy_storage")
            report = json.loads((out / "global_audit.json").read_text(encoding="utf-8"))
            self.assertNotIn(45, report["findings"].get("wts_latin_review", []))
            lua = map_path / "_lua/monolith_split/sections/example.lua"
            lua.parent.mkdir(parents=True)
            # Even a valid-looking literal prefix is not a constant key when
            # another expression is concatenated onto it.
            lua.write_text('GetLocalizedString("TRIGSTR_043" .. tostring(index))', encoding="utf-8")
            with patch.multiple(audit_ui_text, ROOT=root, MAP=map_path, OUT=out, __file__=str(script)):
                with redirect_stdout(io.StringIO()):
                    audit_ui_text.main()
            changed = json.loads((out / "global_inventory.json").read_text(encoding="utf-8"))
            self.assertFalse(changed["localization_key_audit"]["constant_keys_only"])
            unused = next(row for row in changed["wts"] if row["sid"] == 44)
            self.assertEqual(unused["classification"], "unreferenced_requires_review")


if __name__ == "__main__":
    unittest.main()
