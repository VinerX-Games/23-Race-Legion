import math
import struct
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
from wc3_pathing import placed_doodads, game_has_skins, blit


class PlacedPathingTests(unittest.TestCase):
    def placement(self, skin=False):
        data = b"W3do" + struct.pack("<III", 8, 11, 1)
        data += b"LTlt" + struct.pack("<I7f", 0, 100, 200, 0, 0, 1, 1, 1)
        if skin:
            data += b"LTlt"
        return data + struct.pack("<BBiII", 2, 100, -1, 0, 7)

    def test_placement_parser_consumes_classic_and_reforged_records(self):
        for skins in (False, True):
            row = placed_doodads(self.placement(skins), skins)[0]
            self.assertEqual(row["id"], "LTlt")
            self.assertEqual((row["x"], row["y"], row["creation"]), (100, 200, 7))
        with self.assertRaisesRegex(ValueError, "Truncated"):
            placed_doodads(self.placement()[:-1], False)

    def test_game_version_controls_skin_field(self):
        header = lambda minor: struct.pack("<7I", 31, 1, 1, 1, minor, 0, 0)
        self.assertFalse(game_has_skins(header(31)))
        self.assertTrue(game_has_skins(header(32)))

    def test_rotated_footprint_maps_colors_to_engine_flags(self):
        cells = bytearray(25)
        changed = blit(cells, 5, 5, 2, 2, 0, (2, 1, bytes([2, 4])))
        self.assertEqual(changed, 2)
        self.assertEqual(cells[1 * 5 + 2], 2)
        self.assertEqual(cells[2 * 5 + 2], 4)
        self.assertEqual(sum(bool(c) for c in cells), 2)

    def test_footprint_preserves_static_flags_and_clips_map_edges(self):
        cells = bytearray([8] * 4)
        blit(cells, 2, 2, 0, 0, math.pi / 2, (2, 2, bytes([2] * 4)))
        self.assertTrue(all(value & 8 for value in cells))
        self.assertTrue(any(value & 2 for value in cells))

    def test_non_cardinal_asymmetric_footprint_is_rejected(self):
        with self.assertRaisesRegex(ValueError, "Non-cardinal"):
            blit(bytearray(25), 5, 5, 2, 2, 0.25, (2, 1, bytes([2, 4])))


if __name__ == "__main__":
    unittest.main()
