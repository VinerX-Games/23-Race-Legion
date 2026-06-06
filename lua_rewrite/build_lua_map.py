from __future__ import annotations

import runpy
from pathlib import Path


if __name__ == "__main__":
    repo_root = Path(__file__).resolve().parent.parent
    runpy.run_path(str(repo_root / "build_map_lua.py"), run_name="__main__")
