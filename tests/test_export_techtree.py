"""Keep research menus separate from upgrades affecting a unit or building."""
import sys
import unittest
from unittest.mock import patch
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
from export_techtree import normalize_research_edges, object_fields, export_race


class ResearchMenuTests(unittest.TestCase):
    def test_menu_target_missing_from_cli_graph_is_read_as_upgrade(self):
        graph = {"ok": True, "agent_view": {}, "nodes": [
            {"id": "w212", "category": "building", "name": "Логово черных драконов"}], "edges": []}
        with patch("export_techtree.cli", return_value=graph), patch("export_techtree.object_fields", side_effect=[
            {"w212": {"researches": ["Rovs"]}}, {"Rovs": {"name": "Отравленные копья", "levels": 1}}]):
            result = export_race("Horde", {})
        self.assertEqual(result["objects"]["Rovs"]["type"], "upgrade")
        self.assertEqual(result["objects"]["Rovs"]["name"], "Отравленные копья")
        self.assertNotIn("only_required", result["objects"]["Rovs"])
        self.assertIn("w212 researches Rovs", result["edges"])

    def test_nonstandard_ability_retains_its_building_requirement(self):
        graph = {"ok": True, "agent_view": {}, "nodes": [
            {"id": "n062", "category": "unit", "name": "Мам'тот"},
            {"id": "S00F", "category": "unknown", "name": ""},
            {"id": "o06K", "category": "building", "name": "Алтарь Мам'Тота"}],
            "edges": [{"from": "n062", "kind": "has-ability", "to": "S00F"}]}
        values = {"n062": {}, "o06K": {}, "S00F": {"name": "Аура Мам'Тота", "requires": ["o06K"]}}
        with patch("export_techtree.cli", return_value=graph), patch("export_techtree.object_fields", return_value=values) as read:
            result = export_race("IceTrols", {})
        self.assertIn("S00F", read.call_args.args[0]["ability"])
        self.assertEqual(result["objects"]["S00F"]["type"], "ability")
        self.assertIn("S00F requires o06K", result["edges"])

    def test_unknown_graph_research_is_promoted_only_after_typed_readback(self):
        graph = {"ok": True, "agent_view": {}, "nodes": [
            {"id": "h0E7", "category": "building", "name": "Верфь"},
            {"id": "kt01", "category": "unknown", "name": ""}],
            "edges": [{"from": "h0E7", "kind": "researches", "to": "kt01"}]}
        values = {"h0E7": {"researches": ["kt01"]}, "kt01": {"name": "Новые типы ядер", "levels": 1}}
        with patch("export_techtree.cli", return_value=graph), patch("export_techtree.object_fields", return_value=values) as read:
            result = export_race("KulTiras", {})
        self.assertIn("kt01", read.call_args.args[0]["upgrade"])
        self.assertEqual(result["objects"]["kt01"]["type"], "upgrade")
        self.assertEqual(result["objects"]["kt01"]["name"], "Новые типы ядер")

    def test_unreadable_research_reference_remains_unknown(self):
        graph = {"ok": True, "agent_view": {}, "nodes": [
            {"id": "h0E7", "category": "building", "name": "Верфь"},
            {"id": "zzzz", "category": "unknown", "name": ""}],
            "edges": [{"from": "h0E7", "kind": "researches", "to": "zzzz"}]}
        with patch("export_techtree.cli", return_value=graph), patch("export_techtree.object_fields", return_value={"h0E7": {"researches": ["zzzz"]}}):
            result = export_race("KulTiras", {})
        self.assertEqual(result["objects"]["zzzz"]["type"], "unknown")

    def test_lowercase_upgrade_keeps_effective_numbered_display_name(self):
        response = {"ok": True, "objects": [{"id": "kt01", "name": "|cffebc56cНовые типы ядер|r",
                    "fields": {"name": "", "maxlevel": "1"}}]}
        with patch("export_techtree.cli", return_value=response):
            actual = object_fields({"upgrade": ["kt01"]}, {})
        self.assertEqual(actual["kt01"]["name"], "Новые типы ядер")
        self.assertEqual(actual["kt01"]["levels"], 1)

    def test_altar_armor_upgrades_are_not_a_research_menu(self):
        nodes = {"halt": {"category": "building"}}
        actual = normalize_research_edges(
            {"halt researches Rhac", "halt researches Rgfo", "halt trains H0H7"}, nodes,
            {"halt": {"affected_by": ["Rhac", "Rgfo"]}})
        self.assertEqual(actual, {"halt affected-by Rhac", "halt affected-by Rgfo", "halt trains H0H7"})

    def test_shipyard_research_menu_and_masonry_can_coexist(self):
        nodes = {"dock": {"category": "building"}}
        actual = normalize_research_edges(
            {"dock researches Rhac", "dock researches R007"}, nodes,
            {"dock": {"affected_by": ["Rhac"], "researches": ["R007"]}})
        self.assertEqual(actual, {"dock affected-by Rhac", "dock researches R007"})

    def test_protective_unit_does_not_research_its_own_technology(self):
        nodes = {"h01O": {"category": "unit"}}
        actual = normalize_research_edges(
            {"h01O researches RDr3", "h01O has-ability ADr3"}, nodes,
            {"h01O": {"affected_by": ["RDr3"]}})
        self.assertEqual(actual, {"h01O affected-by RDr3", "h01O has-ability ADr3"})


if __name__ == "__main__":
    unittest.main()
