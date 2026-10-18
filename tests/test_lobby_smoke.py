"""Run the mocked lobby scenario in an isolated process with strict assertions."""
import subprocess
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


class LobbySmokeTests(unittest.TestCase):
    def test_map_load_and_lobby_expiry(self):
        result = subprocess.run([sys.executable, str(ROOT / "tests/fixtures/lobby_smoke.py")],
                                cwd=ROOT, capture_output=True, text=True, encoding="utf-8",
                                errors="replace", timeout=90)
        self.assertEqual(result.returncode, 0, (result.stdout + result.stderr)[-6000:])


if __name__ == "__main__":
    unittest.main()
