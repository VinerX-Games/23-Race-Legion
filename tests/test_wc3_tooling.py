import contextlib
import io
import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import wc3_project as project
import wc3_checks as checks
import wc3_hivewe as hivewe
import wc3_object_tools as objects
import wc3_scenarios as scenarios


class ManifestAndIndexTests(unittest.TestCase):
    def fixture(self, root, texts):
        (root / "sections").mkdir()
        (root / "manifest.json").write_text(json.dumps({"sections": [{"file": name} for name in texts]}))
        for name, text in texts.items():
            (root / "sections" / name).write_text(text, encoding="utf-8")

    def test_shared_line_offsets_and_source_map_match_exact_concatenation(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            self.fixture(root, {"a.lua": "-- header\nx = ", "b.lua": "1\ny=2\n"})
            sections = project.load_sections(root)
            self.assertEqual(sections[1]["start_line"], 2)
            self.assertEqual(project.locate_offset(sections, 14)["file"], "b.lua")
            mapping = project.source_map(sections)
            self.assertEqual(mapping["sha256"], project.digest("-- header\nx = 1\ny=2\n"))

    def test_missing_duplicate_and_traversal_manifest_entries_fail(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary); (root / "sections").mkdir()
            for entries, exception in ((["absent.lua"], FileNotFoundError),
                                       (["../outside.lua"], ValueError),
                                       (["a.lua", "a.lua"], ValueError)):
                (root / "sections/a.lua").write_text("")
                (root / "manifest.json").write_text(json.dumps({"sections": [{"file": n} for n in entries]}))
                with self.assertRaises(exception):
                    project.load_sections(root)

    def test_function_boundaries_ignore_comments_strings_and_nested_blocks(self):
        text = '''local F = function(x)
 if x then
   local nested = function() return "end" end
 end
 -- function Fake() end
 return [=[function Wrong() end]=]
end
G = function() for i=1,2 do repeat i=i+1 until i>1 end end
'''
        index = project.build_index([{"text": text}])
        functions = {f["name"]: f for f in index["functions"]}
        self.assertEqual(set(functions), {"F", "nested", "G"})
        self.assertEqual(functions["F"]["end_line"], 7)
        self.assertNotIn("Fake", index["refs"])
        self.assertNotIn("Wrong", index["refs"])

    def test_changed_content_invalidates_cached_index(self):
        with tempfile.TemporaryDirectory() as temporary:
            first = project.index([{"text": "function A() end"}], temporary)
            second = project.index([{"text": "function B() end"}], temporary)
            self.assertNotEqual(first["sha256"], second["sha256"])
            self.assertEqual(second["functions"][0]["name"], "B")

    def test_old_source_map_does_not_show_changed_source_as_old_context(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            self.fixture(root, {"a.lua": "old=1\n"})
            mapping = project.source_map(project.load_sections(root))
            saved = root / "source-map.json"; saved.write_text(json.dumps(mapping))
            (root / "sections/a.lua").write_text("new=2\n")
            report = project.map_line(1, root, saved_map=saved, expected_hash=mapping["sha256"])
            self.assertTrue(report["results"][0]["stale_source"])
            self.assertEqual(report["results"][0]["context"], [])
            with self.assertRaisesRegex(ValueError, "hash"):
                project.map_line(1, root, saved_map=saved, expected_hash="wrong")

    def test_check_only_mismatch_returns_failure(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            self.fixture(root, {"a.lua": "x=1\n"})
            output = root / "war3map.lua"; output.write_text("x=2\n")
            result = subprocess.run([sys.executable, str(ROOT / "build_map_lua.py"),
                                     "--split-dir", str(root), "--output", str(output), "--check-only"],
                                    capture_output=True, text=True)
            self.assertNotEqual(result.returncode, 0)
            self.assertEqual(output.read_text(), "x=2\n")


class CheckAndContractTests(unittest.TestCase):
    def test_verify_fails_for_any_required_check(self):
        for failing in ("source-sync", "lua-syntax", "ai-races", "unittest"):
            with self.subTest(failing=failing):
                def response(name, *args):
                    return {"name": name, "ok": name != failing, "output": "", "seconds": 0,
                            "exit_code": 1 if name == failing else 0}
                with patch.object(checks, "run_check", side_effect=response):
                    self.assertFalse(checks.verify()["ok"])

    def test_cli_nonzero_exit_overrides_json_success(self):
        proc = subprocess.CompletedProcess([], 2, '{"ok":true}', "failed")
        with patch.object(hivewe, "find_hivewe_cli", return_value=Path("test.exe")), \
             patch.object(hivewe.subprocess, "run", return_value=proc):
            self.assertFalse(hivewe.run_cli_json([])["ok"])

    def test_search_uses_installed_cli_matches_schema(self):
        with patch.object(hivewe, "run_cli_json", return_value={"ok": True, "matches": [
                {"id": "h014", "name": "Worker"}]}), contextlib.redirect_stdout(io.StringIO()) as output:
            self.assertEqual(hivewe.cmd_search("Worker"), 0)
        self.assertIn("h014", output.getvalue())

    def test_diff_captures_fields_names_and_object_lifecycle(self):
        before = {"unit": {"h001": {"name": "Old", "fields": {"hp": "10"}}}}
        after = {"unit": {"h001": {"name": "New", "fields": {"hp": "20"}}, "h002": {"fields": {}}}}
        diff = objects.semantic_diff(before, after)
        self.assertEqual(len(diff), 3)
        self.assertTrue(any(c.get("field") == "hp" and c["before"] == "10" for c in diff))
        self.assertTrue(any(c.get("change") == "added" for c in diff))

    def test_reference_validation_uses_target_type(self):
        data = {"unit": {"h001": {"fields": {"trains": "h002", "abillist": "h002"}}, "h002": {"fields": {}}},
                "ability": {}}
        findings = objects.validate(data)
        self.assertEqual(len(findings), 1)
        self.assertEqual(findings[0]["field"], "abillist")

    def test_recovery_rejects_concurrent_changes(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary); target = root / "war3map.w3u"; target.write_bytes(b"concurrent")
            backup = root / "backup"; backup.write_bytes(b"before")
            journal = root / "journal.json"
            journal.write_text(json.dumps({"schema_version": 1, "state": "committed", "map": str(root),
                "files": [{"file": target.name, "backup": backup.name,
                           "before_sha256": objects.hash_file(backup), "after_sha256": "different"}]}))
            with self.assertRaisesRegex(ValueError, "Concurrent"):
                objects.recover(journal)
            self.assertEqual(target.read_bytes(), b"concurrent")

    def test_recovery_restores_wts_together_with_object_changes(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary); target = root / "war3map.wts"; target.write_bytes(b"after")
            backup = root / "backup"; backup.write_bytes(b"before")
            journal = root / "journal.json"
            journal.write_text(json.dumps({"schema_version": 1, "state": "committed", "map": str(root),
                "files": [{"file": target.name, "backup": backup.name,
                           "before_sha256": objects.hash_file(backup), "after_sha256": objects.hash_file(target)}]}))
            self.assertTrue(objects.recover(journal)["ok"])
            self.assertEqual(target.read_bytes(), b"before")

    def test_failed_live_expectation_fails_the_report(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            heartbeat = root / "23race_eval_hb.pld"; heartbeat.write_text("hb|1")
            scenario = root / "scenario.json"
            scenario.write_text(json.dumps({"schema_version": 1, "steps": [
                {"name": "expected-result", "lua": "return 'wrong'", "expected": "correct"}]}))
            def execute(code, *args):
                if code.startswith("__AgentScenarioSession="):
                    value = code.split('"')[1]
                else:
                    value = "wrong"
                return {"ok": True, "exit_code": 0, "output": "OK " + value, "error": ""}
            with patch.object(scenarios, "settings", return_value={"custom_data": str(root)}), \
                 patch.object(scenarios, "CACHE", root / "cache"), \
                 patch.object(scenarios, "execute", side_effect=execute), \
                 contextlib.redirect_stdout(io.StringIO()):
                report = scenarios.run(scenario, ready_timeout=1)
            self.assertFalse(report["ok"])
            self.assertIn("expected-result", report["error"])


if __name__ == "__main__":
    unittest.main()
