import contextlib
import importlib.util
import io
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch


BRIDGE_PATH = Path(__file__).resolve().parents[1] / "agent_bridge.py"
SPEC = importlib.util.spec_from_file_location("agent_bridge", BRIDGE_PATH)
bridge = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(bridge)


class AgentBridgeResetTests(unittest.TestCase):
    def configure_paths(self, root):
        bridge.IN_GLOB = str(root / "23race_eval_[0-9]*.pld")
        bridge.OUT_GLOB = str(root / "23race_eval_out_[0-9]*.pld")
        bridge.EVAL_OUT = str(root / "23race_eval_out.pld")
        bridge.HB_FILE = str(root / "23race_eval_hb.pld")

    def test_reset_removes_inbox_outbox_and_heartbeat(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            self.configure_paths(root)
            files = [
                root / "23race_eval_0001.pld",
                root / "23race_eval_out_0001.pld",
                root / "23race_eval_out.pld",
                root / "23race_eval_hb.pld",
            ]
            for path in files:
                path.write_text("stale", encoding="utf-8")

            with contextlib.redirect_stdout(io.StringIO()):
                result = bridge.cmd_reset()

            self.assertEqual(result, 0)
            self.assertTrue(all(not path.exists() for path in files))

    def test_reset_fails_when_any_bridge_file_cannot_be_removed(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            self.configure_paths(root)
            stale = root / "23race_eval_0001.pld"
            stale.write_text("stale", encoding="utf-8")

            with patch.object(bridge.os, "remove", side_effect=PermissionError):
                with contextlib.redirect_stdout(io.StringIO()):
                    result = bridge.cmd_reset()

            self.assertEqual(result, 1)
            self.assertTrue(stale.exists())


if __name__ == "__main__":
    unittest.main()
