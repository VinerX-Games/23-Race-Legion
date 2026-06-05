# Lua Rewrite Progress

## 2026-06-06

- Added `probe-map` and `read-war3-log` commands to `HiveWE_cli` for automated `run -> wait -> collect War3Log` loops.
- Verified that Lua root errors are written to `War3Log.txt` with `war3map.lua` line numbers.
- Verified that the generated map folder `lua_rewrite/map_lua.w3m` loads without an immediate root error.
- Determined that `23_race_1_6_505 Lua.w3m` is currently a lightweight placeholder map, while `lua_rewrite/map_lua.w3m` contains the full script conversion attempt.
- Added `lua_rewrite/build_lua_map.py` to build a separate probe artifact from module files with injected Debug Utils.
- Added `map_lua.w3m/debug_probe.lua` and instrumented `main.lua` with labeled init checkpoints.
- Important: the module-based probe build is currently much smaller than the large conversion monolith, so it is kept as a separate artifact: `lua_rewrite/war3map.probe.generated.lua`.
- Restored `map_lua.w3m/war3map.lua` from the larger conversion artifact after verifying the probe build path.
- Tried FileIO-based disk logging to `CustomMapData`, but no output file appeared under the current `-loadfile` probe environment. This remains an unresolved environment/runtime issue.
- Next: decide whether to instrument the large conversion monolith directly or extend the module coverage until the probe build becomes functionally representative.

## 2026-06-07

- Split the large converted `lua_rewrite/war3map.lua` into an exact rebuildable source tree under `lua_rewrite/monolith_split/`.
- Added `lua_rewrite/split_war3map.py` so the split source can be rebuilt back into `war3map.lua` deterministically.
- Verified the initial split by rebuilding an exact text match against the original monolith before any fixes.
- Discovered the real execution blocker: `lua_rewrite/map_lua.w3m/war3map.w3i` still had the Lua flag disabled, so Warcraft was not executing `war3map.lua` at all.
- Added `lua_rewrite/set_w3i_lua_flag.py` and switched `map_lua.w3m/war3map.w3i` into Lua mode.
- Added `lua_rewrite/normalize_converted_lua.py` to mechanically fix repeated JASS->Lua artifacts in the split source.
- Normalized several systemic conversion defects:
  - named callback references like `Condition(function Foo)` -> `Condition(Foo)`
  - inline JASS comments `//`
  - `!=` -> `~=`
  - `local array name` -> `local name = {}`
  - `loop` -> `while true do`
- Fixed the first allocator/deallocator conversion defect manually (`...V[this] = -1` / `~= -1`) using the original `war3map.j` as reference.
- Added runtime probe logging through `PreloadGenEnd` into `CustomMapData` and taught `HiveWE_cli probe-map` to read that log back.
- Added optional auto-click support to `HiveWE_cli probe-map` for maps that stop on the post-load click gate.
- Current runtime state:
  - root Lua compile errors are cleared for the current tested build
  - deferred init now completes through `InitCustomTriggers` and `RunInitializationTriggers`
  - current blockers moved into runtime callback errors caused by rawcode strings passed where WC3 Lua expects numeric ids, e.g. `SetPlayerTechMaxAllowed` / `GetPlayerTechCount`
