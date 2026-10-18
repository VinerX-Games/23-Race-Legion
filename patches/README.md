# HiveWE CLI patch

Source: [VinerX/HiveWE](https://github.com/VinerX/HiveWE), commit
`f3fad1892e2856b9c7daac0c870937613d98c436`. The patch is kept here; checkouts, dependencies,
build outputs and logs stay in gitignored `.cache/`.

Implemented natively:

- `capabilities`, schema version 1 on JSON output, structured exception failures;
- `dump-objects --all-fields` and rejection of unknown `set-field` columns;
- `validate-map [--assets] [--limit N]` for object references, WTS and map/CASC asset lookup;
- `asset-exists --path <asset>`;
- `probe-map --ready-file <heartbeat> --stop-when-ready`, requiring a fresh heartbeat;
- `HIVEWE_CLI_ONLY=ON`, avoiding Qt/editor dependencies and privileged data-directory symlinks.
- writing merged main/Skin values without leaving stale Skin overrides; counting only serialized fields;
- allocating a separate WTS entry for ordinary text edits (`--shared-string` explicitly changes the shared entry).

Build on Windows with Visual Studio 2022 17.14+:

```powershell
python scripts/wc3_build_hivewe.py
python scripts/wc3_build_hivewe.py --verify-only --activate
```

The helper pins HiveWE and vcpkg revisions, applies the patch, installs only CLI dependencies,
builds a separate executable and checks capabilities plus a minimal MPQ packaging contract. It never overwrites installed HiveWE.
`--activate` updates only the CLI path in `wc3.local.json`, preserving other settings.
Use the fork's `overlay-ports` when installing both CascLib and StormLib: the CLI needs their Unicode builds.
Existing ASCII packages in this dedicated cache must be removed/reinstalled with the overlay.
CascLib detects the mismatch at compilation; StormLib can otherwise fail packaging at runtime.

Wrapper-level features live in the map repository: semantic diff, staged/journaled edits,
live assertions, model inspection and placed-obstacle pathing. `wc3_pathing.py` uses a temporary
WPM and follows HiveWE's footprint rotation/color rules; runtime changes to gates, trees and
scripted obstacles still require an in-game check.

Native validation reports existing defects; it does not repair map data. Asset lookup failures
are warnings because game aliases/flavours and replacements can require further inspection.
