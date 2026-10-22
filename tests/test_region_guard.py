import json
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import wc3_project as project


class LateRegionGuardTests(unittest.TestCase):
    """Поздний регион на всю карту ломает пути юнитов; сборка обязана это ловить."""

    def sections(self, texts):
        temporary = tempfile.TemporaryDirectory()
        self.addCleanup(temporary.cleanup)
        root = Path(temporary.name)
        (root / "sections").mkdir()
        (root / "manifest.json").write_text(json.dumps({"sections": [{"file": name} for name in texts]}))
        for name, text in texts.items():
            path = root / "sections" / name
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(text, encoding="utf-8")
        return project.load_sections(root)

    def test_map_sources_have_no_late_regions(self):
        self.assertEqual(project.late_region_violations(project.load_sections()), [])

    def test_root_allmap_is_allowed(self):
        sections = self.sections({"01_globals.lua": "Allmap = CreateRegion()\t---@type region\n"})
        self.assertEqual(project.late_region_violations(sections), [])

    def test_region_created_in_init_is_rejected(self):
        sections = self.sections({
            "01_globals.lua": "Allmap = CreateRegion()\nfunction InitGlobals()\n\tAllmap = CreateRegion()\nend\n",
            "races/Naga.lua": "-- CreateRegion() в комментарии не считается\n"
                              "function NagaCombat.Init()\n    NagaCombat.world = CreateRegion()\nend\n",
        })
        found = [(file, line, func) for file, line, func, _ in project.late_region_violations(sections)]
        self.assertEqual(found, [("01_globals.lua", 3, "InitGlobals"), ("races/Naga.lua", 7, "NagaCombat.Init")])


if __name__ == "__main__":
    unittest.main()
