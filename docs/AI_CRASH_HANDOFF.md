# Handoff: hard C++ crash hunt (0x6C) — continue here

Status: **ROOT NOT YET FIXED.** Localized to `AiEnemyPowerAround` native enum hitting
a bad unit handle. This doc is a self-contained guide for the next agent to finish.
Branch: **`ai-brain-overhaul`** (off `main`). Read also [AI_OVERHAUL_PLAN.md](AI_OVERHAUL_PLAN.md),
[DEBUG_WC3_MAP.md](DEBUG_WC3_MAP.md) (now has a "Жёсткие C++-краши" section).

---

## 0. The one-paragraph summary

There is a **deterministic, recurring hard crash**: `ACCESS_VIOLATION reading 0x6C`,
same engine instruction across 20+ crash dumps. It is **NOT catchable by `pcall`**
(it's C++). Via single-slot unbuffered breadcrumbs it was localized to
**`AiEnemyPowerAround`** ([83_ai_brain.lua](map.w3x/_lua/monolith_split/sections/83_ai_brain.lua)).
It crashes inside the native `GroupEnumUnitsInRange` / the following `GetUnitState`
when the enum yields a **stale or transitional unit handle** (offset `0x6C` is the
unit's life field → deref of a freed/invalid unit). Removing the Lua Condition
filter did **not** fix it (proving it's the enumerated unit, not the filter). Most
likely culprit: **portal-system units mid-teleport** (`ShowUnitHide` +
`SetUnitPositionLoc` in [06_transport_portals.lua](map.w3x/_lua/monolith_split/sections/80_runtime/triggers/06_transport_portals.lua))
leave units in a state that makes area-enums deref them. The AI drives heavy region
scanning (`AiEnemyPowerAround` ~3×/bot/tick × 22 bots) and heavy portal traffic, so
it exposed a long-latent engine hazard (the same crash dumps exist all through
2026-06-09 during AI testing).

---

## 1. The crash signature & where dumps live (THIS is the debug method — use it)

**WC3 writes a crash dump on every hard crash** — do NOT use the hanging per-line
probe-log; use these:
```
%USERPROFILE%\Documents\Warcraft III\Errors\<YYYY-MM-DD HH.MM.SS hash>\
  Crash.txt   — <Exception.Summary:> has the signature + a stack of engine addresses
  War3.dmp    — minidump
  War3Log.txt — engine/NGDP log (NOT our BJDebugMsg; not useful for our trace)
```
Signature (constant low bits `…CC59`; high bits vary by ASLR):
```
ACCESS_VIOLATION (Failed to read address 0x6C at instruction 0x7FF6..CC59)
```
- `0x6C` = field offset on a **null/freed unit pointer**.
- The stack shows a **repeating address cycle** → engine enum/visit dispatch.
- Compare all dumps to confirm "same crash":
  ```bash
  for d in "$USERPROFILE/Documents/Warcraft III/Errors/"*/; do \
    grep -ao "address 0x[0-9A-Fa-f]* at instruction 0x[0-9A-Fa-f]*" "$d/Crash.txt"|head -1; done
  ```
  (06-06 dumps are a DIFFERENT old crash `0x0`; ours is `0x6C`, starts 06-09 16:44.)

---

## 2. What is RULED OUT / CONFIRMED (don't re-do these)

| Hypothesis | Result | How tested |
|---|---|---|
| Diplomat alliance cascade | **NOT the cause** | crashed identically with `AiDiplomatEnabled=false` |
| AI portal initiation (`RequestPort`/`MakeMageTp`) | **NOT sufficient to stop it** | crashed with both no-op'd |
| Lua Condition **filter** in `AiEnemyPowerAround` | **NOT the cause** | removed filter (collect-then-iterate); still crashed, same sig |
| Locus = `AiEnemyPowerAround` | **CONFIRMED (2×)** | breadcrumb caught it twice (parent `AiBrainPerceive`, then exact) |
| Crash predates this session's changes | **YES** | identical dumps all through 06-09 |

**Note:** a diplomat reentrancy guard (`gAllianceClearing`) was added anyway (commit
`9abbe13`) — it fixes a *real* secondary cascade/churn bug, just not THIS crash.

---

## 3. The breadcrumb method (how localization was done — reuse it)

Repo has **`_crumb.lua`** (runtime, applied via bridge — no rebuild). It wraps suspect
functions; each writes its name to a **single file, immediately flushed** (unbuffered
`PreloadGenEnd`), so after the hard crash the file holds the **last function entered**.
The buffered `.pld`/`AiBrainLogBuf` "last log" is UNRELIABLE (lost on mid-tick crash) —
that is why earlier `.pld` tails wrongly looked like portal/diplomat.

```bash
# after the map is loaded + bots spawned:
python agent_bridge.py exec --file _crumb.lua
# crumb file (overwritten each call):
#   %USERPROFILE%\Documents\Warcraft III\CustomMapData\23race_crumb.pld
```
On crash, read it: `cat .../23race_crumb.pld | tr -d '\000' | grep -oE 'Preload\( "[^"]*"'`.
(The `depth=N` in crumbs is unreliable — it LEAKS on thrown Lua errors, so it is NOT a
true nesting count. Ignore it.)

---

## 4. NEXT STEPS (do these, in order)

### 4.1 Identify the exact killer unit (one reproduction)
Replace `AiEnemyPowerAround` at runtime (bridge) with an instrumented version that,
**right before** the `GetUnitState` on each enumerated unit, writes an unbuffered
crumb with that unit's identity:
```lua
-- pseudo: for each u in AiBrainScanGroup:
--   Crumb("EPA u="..GetHandleId(u).." pos="..R2I(GetUnitX(u))..","..R2I(GetUnitY(u))
--         .." hidden?="..tostring(IsUnitHidden(u)))   -- BEFORE GetUnitState(u,...)
--   then GetUnitState(u, UNIT_STATE_LIFE) ...
```
After the crash, the crumb names the **handle id + position + hidden-state** of the unit
that killed it. Cross-reference:
- Is it hidden (`IsUnitHidden`) → confirms portal-traveller-mid-teleport hypothesis.
- Its position → what's there / what just died/teleported there.
- Watch `[TPM]`/`[CONT]` in the probe log around that tick.

`GetHandleId(u)` / `GetUnitX(u)` may themselves be unsafe on a truly freed handle — if
even those crash, the unit is fully removed (improper `RemoveUnit`), not just hidden;
pivot to 4.3.

### 4.2 If it's a transitional/hidden portal unit
Likely fix locations (portal periodic teleport): the `ShowUnitHide` +
`SetUnitPositionLoc` dance in [06_transport_portals.lua](map.w3x/_lua/monolith_split/sections/80_runtime/triggers/06_transport_portals.lua)
(see ~lines 995–1140). Options:
- Ensure travellers are not left enumerable while hidden/mid-move (e.g. move them off
  the map / to a holding rect, or `SetUnitPathing`/locust during transit).
- Make AI area-scans **skip hidden units cheaply**: but note `GetUnitState` is the crash,
  so the skip must use a check that is safe on the bad handle — there may be none, which
  is why the upstream fix (don't leave bad units enumerable) is preferred.

### 4.3 If it's a fully-removed unit (improper RemoveUnit)
`RemoveUnit`/`ReplaceUnit` are scattered (see counts: `04_race_selection`(38),
`93_continental_main`(28), `15_ai_portals_cities`(22), `05_common_spells`(11),
`Alliance.lua` has 14× `ReplaceUnit(GetTrainedUnit(),...)`). Find a removal that runs
in an AI-frequent path (city capture / training upgrade / continental) and leaves the
handle referenced or in a group. The classic WC3 footgun: `RemoveUnit` while the unit
is being enumerated, or destroying/clearing a group mid-`ForGroup`.

### 4.4 Mitigation to ship in parallel (reduces crash rate ~10×, not a fix)
Cache `wm.threatHome` and throttle ALL 3 `AiEnemyPowerAround` call sites
([83_ai_brain.lua](map.w3x/_lua/monolith_split/sections/83_ai_brain.lua) lines ~535
perceive, ~785 objective scoring, ~830 squad) to run every N ticks, not every tick.
Far fewer region scans = far fewer chances to hit a bad unit. Gate behind a flag.

### 4.5 Audit other side-effect / filtered enums
The same engine instruction can be hit by ANY area enum over a bad unit. Other AI
enums to harden the same way (collect-then-iterate, or throttle):
`AiBuildSpotOccupied` (`Condition(f_AnyStructure)`), the legacy `94_ai_attack.lua`
filters (`CheckPlayer`-based, `04_AI0.lua`, `40_bool_exprs.lua`), `AiBuyPirateFleet`,
`AiBrainCollectObjectives`. Also two **caught** `[CALLBACK-ERR]` nil-boolexpr bugs to
fix (not the crash, but real): `checkGreenArea` → filter `alienToDream` is nil
(war3map.lua:12154); `Trig_NoTpNearCapital_Actions` → filter `CapitalOfEnemy` is nil
(war3map.lua:21796). And `war3map.lua:9819` arithmetic-on-nil (`ArmyExp[pi]` nil).

---

## 5. Repro / tooling cheat-sheet (exact commands that work here)

```bash
CLI="/c/Games/HiveWE_VinerX_Edition/build/Release/Release/HiveWE_cli.exe"

# 1) ALWAYS purge stale bridge eval files first (else the fresh map replays old evals!)
rm -f "/c/Users/Dmitry/Documents/Warcraft III/CustomMapData/23race_eval_"*.pld \
      "/c/Users/Dmitry/Documents/Warcraft III/CustomMapData/23race_crumb.pld"

# 2) launch detached (run_in_background); loads map.w3x (must be rebuilt first)
"$CLI" probe-map --map "C:/Games/23 Race/23-Race-Legion/map.w3x" \
  --warcraft "F:/Games/Warcraft III" --args "-window -nowfpause" \
  --click-after 60 --wait 320 --probe-log 23Race_probe_log.pld --keep-open

# 3) wait for bridge: poll hb file fresh (<20s old):
#    /c/Users/Dmitry/Documents/Warcraft III/CustomMapData/23race_eval_hb.pld  -> "hb|1" = clean
cd "C:\Games\23 Race\23-Race-Legion"
python agent_bridge.py reset
python agent_bridge.py exec "return 1"          # first one may TIMEOUT; retry
python agent_bridge.py exec "for pi=2,23 do if not AiRace[pi] then createAiPlayer(pi) end end return 'spawned'"
python agent_bridge.py exec --file _crumb.lua    # install breadcrumbs

# build + verify (NOTE: luaparser via 'rb' errors in this env — read as text):
python build_map_lua.py
python -c "from luaparser import ast; ast.parse(open('map.w3x/war3map.lua', encoding='utf-8', errors='replace').read()); print('PARSE OK')"

# kill WC3 between runs:  taskkill //F //IM "Warcraft III.exe"
```
- Crash hits ~90–180s after spawn with 22 bots — reproduces fast.
- Watch via: poll `tasklist | grep "Warcraft III.exe"`; on death read the crumb file.
- Bridge can't launch WC3 via PowerShell here (deny rule) — run the .exe directly.

---

## 6. What ELSE got fixed this session (committed on `ai-brain-overhaul`)

- `64af4f6` **F0+F1**: robustness (`pcall`-isolated bot tick + fault quarantine,
  `AiValidateRace`) and build-pipeline fix (`AiEnsureCapital` base anchor — bots had
  NO capital; footprint-aware `AiBuildPlaceable`; anti-thrash `AiBuildClaim`;
  `AiRecycleBuilders`). **Validated**: previously-stuck races now build & harvest.
- `9abbe13` **diplomat**: alliance-cascade reentrancy guard (`gAllianceClearing`) +
  `DipMode` clamp + anti-churn hysteresis. (Fixes churn + a *secondary* cascade crash,
  not the 0x6C one.)
- `c09d0ad` **0x6C attempt**: removed the Condition filter from `AiEnemyPowerAround`
  (did NOT fix the crash — kept because collect-then-iterate is the safer pattern) +
  item-litter fix in `TryBuy` (`UnitInventorySize` + don't drop on full) + this method
  documented in DEBUG_WC3_MAP.md.

Scratch files in repo root (gitignored/untracked, safe to keep): `_crumb.lua`,
`_eco_snap.lua`, `_val_probe.lua`, `_prod_probe.lua`, `_hotpatch_f1.lua`.

---

## 7. Key mental model for the next agent

1. **It's an engine crash on a bad unit handle, not your Lua logic.** You cannot
   `pcall` it. You must stop the bad unit from being *enumerated*, or stop it from
   *existing in a bad state* (upstream).
2. **Trust the crash dumps + unbuffered breadcrumbs; distrust the buffered `.pld` tail.**
3. **Reproduce with breadcrumbs, read the one crumb, narrow one level, repeat.** That's
   how it got from "somewhere" → `AiBrainPerceive` → `AiEnemyPowerAround` → (next:
   the exact unit).
4. The AI exposed a latent bug by scanning regions and using portals far more than a
   human ever did. The fix protects a map mechanic many systems share.
