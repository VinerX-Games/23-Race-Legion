-- ====================================================================
-- AI Brain (Phase 1 scaffolding): world model + squads + objective brain.
-- See AI_BRAIN_DESIGN.md. Behavior-inert by default: no race sets `brain`,
-- so AiBrainOf()=="swarm" and the legacy TryAttack path runs unchanged.
-- Opt a bot in via registry def.brain="objective" or (bridge) AiBrainForce[pi].
--
-- Logging: ProbeLogWrite("[BRAIN] ...") — written to probe-log always, shown
-- on screen only when the BRAIN tag is enabled: chat `-log on:BRAIN` / `-log
-- allon`, bridge `log:on:BRAIN`. Throttled to avoid flooding.
-- ====================================================================

AiSquads = AiSquads or {}          -- [pi] = { [sid] = squad }   (Phase 2+)
AiSquadSeq = AiSquadSeq or {}      -- [pi] = next squad id
AiBrainForce = AiBrainForce or {}  -- [pi] = "objective"|"swarm" override (bridge/test)

-- Robustness (Track R): isolate a faulty bot/race so it never stalls the whole AI.
-- AiBotFaults[pi] counts Lua errors caught in the protected tick; when it crosses
-- AiBotFaultLimit within a session the bot is quarantined (skipped, retried later).
AiBotFaults = AiBotFaults or {}        -- [pi] = error count (lifetime)
AiBotQuarantine = AiBotQuarantine or {} -- [pi] = tick until which bot is skipped
AiBotFaultLimit = AiBotFaultLimit or 8  -- faults before quarantine
AiBotQuarantineTicks = AiBotQuarantineTicks or 120 -- how long to sit out
AiRaceValidated = AiRaceValidated or {} -- [raceKey] = true once validated

-- Economy (Track E): build-order anti-thrash. When a worker is sent to build we
-- stamp the current brain tick; for AiBuildClaimTicks afterwards the worker is left
-- alone (walking → constructing) instead of being re-grabbed and re-ordered to a new
-- spot every 0.6s tick (the observed cause of builds never completing). Past the
-- window an idle claimed worker = failed build → recycled to harvest.
AiBuildClaim = AiBuildClaim or {}       -- [unit] = brain tick when last sent to build
AiBuildClaimTicks = AiBuildClaimTicks or 40  -- ticks a claimed worker is left alone before recycle/reuse
                                              -- (raised 20->40: a structure takes 30-60s to finish, ~0.8s/tick,
                                              -- so 20 recycled channeling builders mid-build and the foundation
                                              -- stalled — froze Naga/Pandarens. Proximity check still guards beyond this.)
AiBuildRingStart = AiBuildRingStart or 300  -- first ring radius from anchor
AiBuildRingStep  = AiBuildRingStep  or 300  -- step between rings
AiBuildMinSpacing = AiBuildMinSpacing or 300 -- minimum spacing between buildings (tighter = denser base, builds complete near home)
AiBuildRingCount = AiBuildRingCount or 14   -- how many rings to scan outward

-- Round-robin cursor: fair distribution across bots (replaces ForcePickRandomPlayer)
AiBrainBotList = AiBrainBotList or {}   -- [1..n] = pi, populated at createAiPlayer
AiBrainCursor = AiBrainCursor or 1      -- current position in list

--- Add a bot to the round-robin list (idempotent).
function AiBrainBotListAdd(pi)
    for _, existing in ipairs(AiBrainBotList) do
        if existing == pi then return end
    end
    AiBrainBotList[#AiBrainBotList + 1] = pi
end

--- Remove a bot.
function AiBrainBotListRemove(pi)
    for i, existing in ipairs(AiBrainBotList) do
        if existing == pi then
            table.remove(AiBrainBotList, i)
            if AiBrainCursor > #AiBrainBotList then AiBrainCursor = 1 end
            return
        end
    end
end

--- Return next N player indices via round-robin.
function AiBrainBotListNext(n)
    local out = {}
    local total = #AiBrainBotList
    if total == 0 then return out end
    n = n or 1
    if AiBrainCursor > total then AiBrainCursor = 1 end
    for _ = 1, n do
        out[#out + 1] = AiBrainBotList[AiBrainCursor]
        AiBrainCursor = AiBrainCursor + 1
        if AiBrainCursor > total then AiBrainCursor = 1 end
    end
    return out
end

-- ====================================================================
-- Log buffer: batch ProbeLogWrite calls, flush once per tick or on demand.
-- Replaces individual ProbeLogWrite calls that cost ~0.1ms each (string
-- concat + preloader write). Buffer grows, flushed in AiBrainArmyTick exit.
-- ====================================================================
AiBrainLogBuf = AiBrainLogBuf or {}
AiBrainLogMaxLines = AiBrainLogMaxLines or 64

function AiBrainLogAppend(msg)
    AiBrainLogBuf[#AiBrainLogBuf + 1] = msg
    if #AiBrainLogBuf >= AiBrainLogMaxLines then
        AiBrainLogFlush()
    end
end

function AiBrainLogFlush()
    if #AiBrainLogBuf == 0 then return end
    ProbeLogWrite(table.concat(AiBrainLogBuf, "|"))
    AiBrainLogBuf = {}
end

-- Tunables: set via bridge live (AiBrainBatchSize=6) or leave defaults.
-- All values affect the unified brain tick only; swarm mode ignores them.
AiBrainBatchSize       = AiBrainBatchSize       or 1   -- bots processed per PlayerGet1 fire

-- 4.4: Throttle AiEnemyPowerAround region scans; stale-handle blacklist safety.
gStaleBlacklist = gStaleBlacklist or {} -- [handleId] = tick when freed (aiFixTrainBefore)
gStaleBlacklistGcEvery = gStaleBlacklistGcEvery or 120  -- clean old entries every N ticks
gStaleBlacklistMaxAge = gStaleBlacklistMaxAge or 600     -- keep entries for ~300s
AiThreatHomeCache = AiThreatHomeCache or {} -- [pi] = { val, tick }
AiEpaRefreshEvery = AiEpaRefreshEvery or 4  -- recalc every N perceives
AiEpaObjRefreshEvery = AiEpaObjRefreshEvery or 8  -- recalcy obj/squad EPA every N ticks

-- ====================================================================
-- Profiler: cumulative ms per section, dumped every AiProfileEvery ticks.
-- Bridge: AiProfileReset(pi) to zero; AiProfileDump(pi) for instant read.
-- ====================================================================
AiProfileData = AiProfileData or {}   -- [pi] = { perceive=ms, produce=ms, build=ms, focus=ms, naval=ms, reap=ms, orphan=ms, other=ms, ticks=n }
AiProfileEvery = AiProfileEvery or 30  -- dump to probe log every N brain-ticks per bot

function AiProfileReset(pi)
    AiProfileData[pi] = { ticks = 0 }
end

function AiProfileDump(pi)
    local d = AiProfileData[pi]
    if not d or d.ticks == 0 then return "no data" end
    local t = (d.perceive or 0) + (d.produce or 0) + (d.build or 0) + (d.focus or 0) + (d.naval or 0) + (d.reap or 0) + (d.orphan or 0) + (d.other or 0)
    local parts = {}
    for _, k in ipairs{"perceive","produce","build","focus","naval","reap","orphan","other"} do
        local v = d[k] or 0
        parts[#parts+1] = k .. "=" .. string.format("%.1f", v / d.ticks) .. "ms"
    end
    return "[PROF] pi=" .. tostring(pi) .. " ticks=" .. tostring(d.ticks) .. " total=" .. string.format("%.1f", t) .. "ms avg=" .. string.format("%.1f", t / d.ticks) .. "ms | " .. table.concat(parts, " ")
end
AiDiplomatEnabled = false  -- R14: disable diplomacy entirely (chat spam, CPU, unwanted alliances)
AiBrainMaxProduce      = AiBrainMaxProduce      or 20  -- max unit-training orders per bot per tick
AiBrainMaxBuild        = AiBrainMaxBuild        or 10  -- max building-attempts per bot per tick
g_AiOrdered = g_AiOrdered or {}                        -- per-bot+unit training guard: [key] = last_tick
AiRetrainInterval = AiRetrainInterval or 15            -- ticks between re-issue of same unit order
AiLimitedBuildTicks = AiLimitedBuildTicks or 120       -- a limited unit (hero) ordered within this
                                                       -- many ticks counts as filling its slot, so a
                                                       -- slow-building hero isn't ordered 2-3x before
                                                       -- getAiCount sees it (Cult had 2x CD02).
AiBrainExpansionEvery  = AiBrainExpansionEvery  or 30  -- expansion-check every N brain-ticks
AiBrainNavalEvery      = AiBrainNavalEvery      or 6   -- naval-check every N brain-ticks (was 15:
                                                       -- with 1 bot/~10s a shipyard attempt fired
                                                       -- only every ~2.5min; the multi-step desant
                                                       -- handshake then took many minutes. 6 keeps
                                                       -- it responsive without flooding orders.)
AiBrainNavalStartTick  = AiBrainNavalStartTick  or 23  -- first naval check after N brain-ticks (~4min w/ 16 bots)
AiBrainMaxPorts        = AiBrainMaxPorts        or 20  -- max shipyards/ports per bot
AiMaxHeroes            = AiMaxHeroes            or 3   -- safety ceiling on a bot's TOTAL heroes. The
                                                       -- REAL limit is the hero FOOD budget (cap ceiling
                                                       -- 3; army costs 0 food, a hero ~2 → ~1 hero),
                                                       -- now applied to bots in createAiPlayer. This
                                                       -- count is just a backstop = the 3-food ceiling.
                                                       -- Per-race override race.maxHeroes (Dragons=1,
                                                       -- whose altar heroes are mutually exclusive).
AiBrainLandingEvery     = AiBrainLandingEvery     or 6   -- landing tick every N brain-ticks (was 16 ->
                                                         -- ~2.7min/step; phased desant needs to step
                                                         -- through toEmbark/loading/loaded faster)
AiBrainLandingRadius    = AiBrainLandingRadius    or 800 -- load/unload radius
-- Perf (profiler showed BrainFocus = the dominant per-tick cost, ~50%+, and reap 2nd):
-- BrainFocus only re-tasks IDLE units, so running it every single brain-tick is wasteful.
-- Throttle it + reap to alternating ticks (focus on odd, reap on even, aligned with the
-- every-2-tick orphan/squad scan) — roughly halves both hotspots and spreads the load.
AiFocusEvery            = AiFocusEvery            or 2   -- run BrainFocus every N brain-ticks
AiBrainLandingMaxTransports = AiBrainLandingMaxTransports or 6  -- max transports to load per tick
AiBrainMinArmy = AiBrainMinArmy or 50  -- train regardless of ratio until total army reaches this
-- R16: army-SIZE target, decoupled from current size. The old code used
-- ratioBase = max(totalMil, AiBrainMinArmy); once army passed MinArmy the per-unit
-- targets summed to exactly the *current* total, so net growth pressure vanished and
-- every army plateaued at ~MinArmy. We now drive composition toward an absolute
-- desired size so deficits persist until the bot is actually big (food-gated below).
AiBrainDesiredArmy = AiBrainDesiredArmy or 120  -- composition is filled up to this many units (food permitting)

-- GLOBAL size multiplier. One knob that scales DOWN how much every bot fields — army, fleet
-- (ports) AND each building type's count — to cut the total unit/building count and reduce lag.
-- Applied per-type and ROUNDED UP (max(1,ceil)) so nothing a bot needs gets zeroed: at 0.5 a
-- building capped at 4 -> 2, a hall capped at 1 -> 1, DesiredArmy 120 -> 60. 1.0 = no change.
AiSizeScale = AiSizeScale or 1.0
---@param n number
---@return integer
function AiScaled(n)
    local s = AiSizeScale or 1.0
    if s >= 1.0 then return n end
    local r = math.ceil(n * s)
    if r < 1 then r = 1 end
    return r
end

-- ====================================================================
-- Bot advantage regulation. Three dials let you trade bot COUNT vs bot STRENGTH:
--   * army size : AiBrainDesiredArmy (global) / race.desiredArmy (per-race)
--   * unit HP   : AiBotHPMult   (per-player HP handicap, 1.0 = like a player)
--   * unit dmg  : AiBotDmgMult  (per-player damage handicap, 1.0 = like a player)
-- Defaults are NEUTRAL (1.0) — bots play exactly like players until you dial them.
-- Examples: "few player-like bots" = mults 1.0, DesiredArmy 120. "Many strong bots with
-- small armies" = AiBotHPMult/DmgMult 1.5-2.0 + a low DesiredArmy (e.g. 40-60). Applied
-- per bot in createAiPlayer; the handicap scales ALL of that bot's units (current+future).
-- ====================================================================
AiBotHPMult  = AiBotHPMult  or 1.0
AiBotDmgMult = AiBotDmgMult or 1.0
---@param pi integer
function AiApplyBotHandicap(pi)
    local p = Player(pi)
    SetPlayerHandicap(p, AiBotHPMult)
    if SetPlayerHandicapDamage ~= nil then SetPlayerHandicapDamage(p, AiBotDmgMult) end
end

-- Map-wide advantage auras for bots (apply the "Преимущество" buff aia0). Each entry is
-- {abilityId, level}. aib0 = Endurance/Command (+5%..+50% attack & move speed at lvl 1..10),
-- aib1 = Devotion (+armor, up to +7). Both have area=99999 (whole map) targeting player,self,
-- so ONE carrier (the capital) buffs the bot's entire army. Empty list = OFF (default).
-- Set e.g. AiBotAuras = {{FourCC('aib0'),6},{FourCC('aib1'),6}} to test small-but-strong bots.
AiBotAuras = AiBotAuras or {}
---@param pi integer
function AiApplyBotAuras(pi)
    if #AiBotAuras == 0 then return end
    local cap = playerCapital[pi]
    if cap == nil or GetUnitState(cap, UNIT_STATE_LIFE) <= 0.405 then return end
    for _, a in ipairs(AiBotAuras) do
        if GetUnitAbilityLevel(cap, a[1]) == 0 then UnitAddAbility(cap, a[1]) end
        SetUnitAbilityLevel(cap, a[1], a[2])
    end
end

-- R8 fix: udg_WaterPoints was never initialized → BrainNavalDecision skipped entirely.
-- Hardcode the water points from GoToWaterPoint (97_ai_water.lua) so shipyards get built.
if udg_WaterPoints == nil then
    udg_WaterPoints = {
        -- Eastern Kingdoms
        { x = 30150, y = -3454 }, { x = 25504, y = -16284 },
        { x = 19258, y = 5665 },  { x = 10979, y = 10501 },
        -- Kalim
        { x = -28610, y = 16300 }, { x = -15796, y = -10105 },
        { x = -12405, y = 96678 }, { x = -27443, y = 11058 },
        -- Nord
        { x = -4711, y = 20912 },  { x = 8753, y = 22230 },
        { x = 1273, y = 20088 },   { x = -15652, y = 21381 },
        -- BrokenIsles
        { x = 2500, y = 12654 },   { x = 4121, y = 621 },
        -- Pandaria
        { x = -9460, y = -12451 }, { x = -3941, y = -22869 },
    }
end

-- R10: known transport unit types (from all shipyards + pirate). Maps shipyard→transport.
AiTransportTypes = {
    [FourCC('h0D1')] = FourCC('h0D2'), [FourCC('h0D8')] = FourCC('h0D9'),
    [FourCC('h03R')] = FourCC('h00X'), [FourCC('h011')] = FourCC('h00X'),
    [FourCC('h0D3')] = FourCC('h0D4'), [FourCC('h0HO')] = FourCC('h0D4'),
    [FourCC('h0E7')] = FourCC('h0E5'),
    [FourCC('h0D7')] = FourCC('h06U'),  -- Goblins' own Верфь (wall) -> Murloc transport
    [FourCC('h0OX')]    = FourCC('h0OX'),  -- pirate transport (use as self)
}
AiTransportSet = {}
for _, t in pairs(AiTransportTypes) do AiTransportSet[t] = true end

-- Tunables (global defaults; races may override via def.brainWeights). Phase 2+
-- consumes the weights; Phase 1 uses only the geometry/threat radii.
AiBrainDefaults = {
    brain        = "swarm",
    topK         = 8,        -- objectives kept per player
    clusterEvery = 8,        -- recompute objective pool every N perceive ticks
    rCluster     = 1600.0,   -- cluster aggregation radius
    rHome        = 2500.0,   -- capital threat scan radius
    squadCap     = 8,
    commitMin    = 4,
    guardFrac    = 0.2,
    focusMargin  = 25.0,     -- hysteresis: keep current focus unless beaten by this
    homeThreat   = 20.0,     -- enemy power near capital that triggers defend/recall
    tpDist       = 6000.0,   -- focus farther than this -> consider TP logistics
    weights = {
        kind  = { capital = 100, cluster = 40, capture = 150, weak = 20, front = 15 },
        value = 1.0, dist = 0.002, claim = 25.0, siege = 0.5,
    },
}

-- Optional per-building-type bonus/override added on top of the live income
-- valuation below. [typeId] = extra value. Empty by default.
AiBuildingValue = AiBuildingValue or {
    [FourCC('e00N')] = 10,
    [FourCC('e01H')] = 20,
    [FourCC('e01J')] = 10,
    [FourCC('e020')] = 80,
    [FourCC('e021')] = 50,
    [FourCC('e02B')] = 20,
    [FourCC('e02C')] = 50,
    [FourCC('e02D')] = 80,
    [FourCC('h007')] = 20,
    [FourCC('h008')] = 50,
    [FourCC('h009')] = 80,
    [FourCC('h00A')] = 10,
    [FourCC('h015')] = 20,
    [FourCC('h016')] = 50,
    [FourCC('h017')] = 80,
    [FourCC('h01X')] = 20,
    [FourCC('h01Y')] = 50,
    [FourCC('h01Z')] = 80,
    [FourCC('h024')] = 10,
    [FourCC('h030')] = 20,
    [FourCC('h031')] = 10,
    [FourCC('h04A')] = 80,
    [FourCC('h04B')] = 50,
    [FourCC('h04C')] = 20,
    [FourCC('h04M')] = 10,
    [FourCC('h05C')] = 10,
    [FourCC('h05U')] = 20,
    [FourCC('h05V')] = 50,
    [FourCC('h05W')] = 80,
    [FourCC('h05Y')] = 10,
    [FourCC('h070')] = 40,
    [FourCC('h077')] = 10,
    [FourCC('h0BQ')] = 20,
    [FourCC('h0BR')] = 50,
    [FourCC('h0BS')] = 80,
    [FourCC('h0BT')] = 10,
    [FourCC('h0CO')] = 20,
    [FourCC('h0CP')] = 50,
    [FourCC('h0CQ')] = 80,
    [FourCC('h0DS')] = 10,
    [FourCC('h0DU')] = 20,
    [FourCC('h0DV')] = 50,
    [FourCC('h0DW')] = 80,
    [FourCC('h0E9')] = 20,
    [FourCC('h0EA')] = 50,
    [FourCC('h0EB')] = 80,
    [FourCC('h0EC')] = 10,
    [FourCC('h0FI')] = 10,
    [FourCC('h0FK')] = 20,
    [FourCC('h0FL')] = 10,
    [FourCC('h0FR')] = 50,
    [FourCC('h0FS')] = 80,
    [FourCC('h0FY')] = 20,
    [FourCC('h0FZ')] = 40,
    [FourCC('h0G0')] = 40,
    [FourCC('h0G3')] = 20,
    [FourCC('h0G7')] = 30,
    --[FourCC('h0GH')] = 10, --Туннель нерубов
    [FourCC('h0GZ')] = 20,
    [FourCC('h0H0')] = 50,
    [FourCC('h0H1')] = 80,
    [FourCC('h0H2')] = 10,
    [FourCC('h0HZ')] = 20,
    [FourCC('h0I7')] = 50,
    [FourCC('h0I8')] = 80,
    [FourCC('h0IK')] = 20,
    [FourCC('h0IL')] = 80,
    [FourCC('h0IM')] = 10,
    [FourCC('h0JD')] = 10,
    [FourCC('h0JL')] = 80,
    [FourCC('h0JP')] = 20,
    [FourCC('h0JQ')] = 50,
    [FourCC('h0JX')] = 60,
    [FourCC('h0JY')] = 80,
    [FourCC('h0MS')] = 20,
    [FourCC('h0MT')] = 20,
    [FourCC('h0MU')] = 30,
    [FourCC('h0MV')] = 10,
    [FourCC('h0MY')] = 20,
    [FourCC('h0N0')] = 30,
    [FourCC('h0N1')] = 50,
    [FourCC('h0N2')] = 10,
    [FourCC('h0N3')] = 20,
    [FourCC('h0N5')] = 20,
    [FourCC('h0N6')] = 80,
    [FourCC('h0N7')] = 20,
    [FourCC('h0N8')] = 50,
    [FourCC('h0N9')] = 80,
    [FourCC('hcas')] = 80,
    [FourCC('hhou')] = 10,
    [FourCC('hkee')] = 50,
    [FourCC('htow')] = 20,
    [FourCC('n014')] = 20,
    [FourCC('nnfm')] = 10,
    [FourCC('nntt')] = 40,
    [FourCC('o035')] = 20,
    [FourCC('o036')] = 10,
    [FourCC('o03D')] = 50,
    [FourCC('o03E')] = 80,
    [FourCC('o046')] = 20,
    [FourCC('o047')] = 50,
    [FourCC('o048')] = 80,
    [FourCC('o04C')] = 10,
    [FourCC('o05V')] = 20,
    [FourCC('o05W')] = 50,
    [FourCC('o05X')] = 80,
    [FourCC('o060')] = 10,
    [FourCC('oalt')] = 30,
    [FourCC('obar')] = 30,
    [FourCC('obea')] = 20,
    [FourCC('ofor')] = 20,
    [FourCC('ofrt')] = 80,
    [FourCC('ogre')] = 40,
    [FourCC('ostr')] = 60,
    [FourCC('otrb')] = 10,
    [FourCC('pa23')] = 20,
    [FourCC('pa24')] = 50,
    [FourCC('pa25')] = 80,
    [FourCC('pa26')] = 10,
    [FourCC('u00F')] = 50,
    [FourCC('u00G')] = 80,
    [FourCC('u00H')] = 10,
    [FourCC('u02E')] = 10,
    [FourCC('w20e')] = 80,
    [FourCC('w20q')] = 20,
    [FourCC('w20w')] = 50,
    [FourCC('w20y')] = 10,
}          -- [pi] = { [sid] = squad }   (Phase 2+)
AiSquadSeq = AiSquadSeq or {}      -- [pi] = next squad id
AiBrainForce = AiBrainForce or {}  -- [pi] = "objective"|"swarm" override (bridge/test)

-- Tunables (global defaults; races may override via def.brainWeights). Phase 2+
-- consumes the weights; Phase 1 uses only the geometry/threat radii.
AiBrainDefaults = {
    brain        = "swarm",
    topK         = 8,        -- objectives kept per player
    clusterEvery = 8,        -- recompute objective pool every N perceive ticks
    rCluster     = 1600.0,   -- cluster aggregation radius
    rHome        = 2500.0,   -- capital threat scan radius
    squadCap     = 8,
    commitMin    = 4,
    guardFrac    = 0.2,
    focusMargin  = 25.0,     -- hysteresis: keep current focus unless beaten by this
    homeThreat   = 20.0,     -- enemy power near capital that triggers defend/recall
    tpDist       = 6000.0,   -- focus farther than this -> consider TP logistics
    weights = {
        kind  = { capital = 100, cluster = 40, capture = 150, weak = 20, front = 15 },
        value = 1.0, dist = 0.002, claim = 25.0, siege = 0.5,
    },
}

-- Optional per-building-type bonus/override added on top of the live income
-- valuation below. [typeId] = extra value. Empty by default.
AiBuildingValue = AiBuildingValue or {
    [FourCC('ogre')] = 30,  [FourCC('ostr')] = 40,  [FourCC('ofrt')] = 50,
    [FourCC('h00V')] = 30,  [FourCC('h00W')] = 40,  [FourCC('h00X')] = 50,
    [FourCC('h00A')] = 30,  [FourCC('h00B')] = 40,  [FourCC('h00C')] = 50,
    [FourCC('h02Z')] = 30,  [FourCC('h030')] = 40,  [FourCC('h031')] = 50,
    [FourCC('unp1')] = 30,  [FourCC('unp2')] = 40,  [FourCC('unpl')] = 50,
    [FourCC('o029')] = 30,  [FourCC('o02A')] = 40,  [FourCC('o02B')] = 50,
    [FourCC('hvlt')] = 30,  [FourCC('hkee')] = 40,  [FourCC('hcas')] = 50,
    [FourCC('h0AO')] = 14,  [FourCC('h0AP')] = 20,  [FourCC('h0AQ')] = 30,
    [FourCC('h0AL')] = 14,  [FourCC('h0AM')] = 20,  [FourCC('h0AN')] = 30,
}

-- Live income value of a building instance, mirroring the economy module
-- AddCountDis (_lib/54_count_dis.lua): food made + income-upgrade abilities
-- (A0AY *100 | A0SM *75 | A0VS 100) + lumber income (A0B5 *50). This is the real
-- worth of capturing/denying that enemy economic node — not its HP. A per-type
-- AiBuildingValue entry is added as a bonus; floored at 1 so plain capturables
-- still register. Computed per actual unit (ability levels vary at runtime).
---@param u unit
---@return real
function AiBldValueUnit(u)
    local v = I2R(GetUnitFoodMade(u))
    local lay = GetUnitAbilityLevel(u, FourCC('A0AY'))
    if lay >= 1 then
        v = v + 100.0 * I2R(lay)
    else
        local lsm = GetUnitAbilityLevel(u, FourCC('A0SM'))
        if lsm >= 1 then
            v = v + 75.0 * I2R(lsm)
        elseif GetUnitAbilityLevel(u, FourCC('A0VS')) == 1 then
            v = v + 100.0
        end
    end
    local lb5 = GetUnitAbilityLevel(u, FourCC('A0B5'))
    if lb5 > 0 then
        v = v + 50.0 * I2R(lb5)
    end
    local ov = AiBuildingValue[GetUnitTypeId(u)]
    if ov ~= nil then v = v + ov end
    if v < 1.0 then v = 1.0 end
    return v
end

---@param pi integer
---@return table
function AiBrainCfg(pi)
    local r = AiRaceOf(pi)
    if r ~= nil and r.brainWeights ~= nil then
        return r.brainWeights
    end
    return AiBrainDefaults
end

---@param pi integer
---@return string
function AiBrainOf(pi)
    if AiBrainForce[pi] ~= nil then
        return AiBrainForce[pi]
    end
    local r = AiRaceOf(pi)
    if r ~= nil and r.brain ~= nil then
        return r.brain
    end
    return AiBrainDefaults.brain
end

---@param pi integer
---@return boolean
function AiBrainEnabled(pi)
    return AiBrainOf(pi) ~= "swarm"
end

-- ---- logging -------------------------------------------------------
-- Tags (toggle independently with `-log on:<TAG>`): BRAIN (general/perceive),
-- BRAINOBJ (objective collection), BRAINFOC (focus pick + ordering). All silent
-- until enabled. Write generously — we tune the verbosity in bulk later.
---@param pi integer
---@param tag string
---@param msg string
function BrainLogTag(pi, tag, msg)
    ProbeLogWrite("[" .. tag .. "] pi=" .. tostring(pi) .. " " .. msg)
end
---@param pi integer
---@param msg string
function BrainLog(pi, msg)
    BrainLogTag(pi, "BRAIN", msg)
end

-- Log at most once per `n` calls of (pi,key). Counter lives in the world model.
-- Optional `tag` (default BRAIN) lets each call site be toggled independently.
---@param pi integer
---@param key string
---@param n integer
---@param msg string
---@param tag? string
function BrainLogEvery(pi, key, n, msg, tag)
    local wm = AiData[pi].wm
    if wm == nil then BrainLogTag(pi, tag or "BRAIN", msg); return end
    local kk = "logn_" .. key
    local c = (wm[kk] or 0) + 1
    wm[kk] = c
    if c % n == 0 then
        BrainLogTag(pi, tag or "BRAIN", msg)
    end
end

-- ---- light world-model primitives ----------------------------------
-- Combat power proxy = gold cost * 0.01 (mirrors 50_lib_new_functions).
---@param u unit
---@return real
function AiUnitPower(u)
    local g = GetUnitGoldCost(GetUnitTypeId(u))
    if g == nil or g <= 0 then
        return 1.0
    end
    return I2R(g) * 0.01
end

-- Non-destructive centroid over a unit group. Returns x, y, livingCount.
---@param g group
---@return real, real, integer
function AiGroupCentroid(g)
    if g == nil then return 0.0, 0.0, 0 end
    local sx, sy, n = 0.0, 0.0, 0
    local ok, size = pcall(BlzGroupGetSize, g)
    if not ok then return 0.0, 0.0, 0 end
    local i = 0
    while i < size do
        local u = BlzGroupUnitAt(g, i)
        if u ~= nil and GetUnitState(u, UNIT_STATE_LIFE) > 0.405 then
            sx = sx + GetUnitX(u)
            sy = sy + GetUnitY(u)
            n = n + 1
        end
        i = i + 1
    end
    if n == 0 then return 0.0, 0.0, 0 end
    return sx / n, sy / n, n
end

-- Summed enemy power within `radius` of (x,y), as seen by player p. One enum.
-- CRASH FIX (the recurring 0x6C ACCESS_VIOLATION, localized here by breadcrumb): the
-- old version enumerated with a Lua Condition filter (f_BrainEnemyPow) that had a
-- side effect (accumulating into a global). The engine evaluates that Lua filter
-- per-unit DURING the native enum; on a unit in a transitional state it dereferenced
-- a null unit (+0x6C) and hard-crashed (uncatchable). Safe pattern (matches
-- AiGroupCentroid/AiSquadPower): collect with NO filter, then iterate in Lua with
-- nil+alive guards — the engine never runs Lua mid-enum.
---@param p player
---@param x real
---@param y real
---@param radius real
---@return real
function AiEnemyPowerAround(p, x, y, radius)
    AiBrainScanGroup = AiBrainScanGroup or CreateGroup()
    GroupEnumUnitsInRange(AiBrainScanGroup, x, y, radius, nil)
    -- GC blacklist periodically
    local now = AiBrainTickCounter or 0
    local gcAge = gStaleBlacklistMaxAge or 600
    if now % (gStaleBlacklistGcEvery or 120) == 0 then
        for hid, t in pairs(gStaleBlacklist) do
            if now - t > gcAge then gStaleBlacklist[hid] = nil end
        end
    end
    local pow = 0.0
    local sz = BlzGroupGetSize(AiBrainScanGroup)
    local i = 0
    while i < sz do
        local u = BlzGroupUnitAt(AiBrainScanGroup, i)
        if u ~= nil then
            -- Safe checks first: handleId blacklist + hidden + owner + enemy
            local hid = GetHandleId(u)
            if gStaleBlacklist[hid] == nil and not IsUnitHidden(u) then
                local owner = GetOwningPlayer(u)
                if owner ~= nil and IsPlayerEnemy(owner, p)
                    and GetUnitState(u, UNIT_STATE_LIFE) > 0.405 then
                    pow = pow + AiUnitPower(u)
                end
            end
        end
        i = i + 1
    end
    GroupClear(AiBrainScanGroup)
    return pow
end

-- E2 (shared logic): AI bots are never assigned a capital — only Scourge calls
-- MakeFakeCapital, and human capitals come from a player-cast ability. So
-- playerCapital[pi] is nil for every bot, which silently disables build-anchoring,
-- defense recall and expansion for ALL races. Lazily adopt the bot's own
-- capital-able building (ability A0IQ, like HaveCapitalAbility but without the
-- UnitAlive-returns-nil pitfall) as the base anchor. Cheap once set (nil+alive guard).
AiCapEnumGroup = AiCapEnumGroup or nil
---@param pi integer
function AiEnsureCapital(pi)
    local cap = playerCapital[pi]
    if cap ~= nil and GetUnitState(cap, UNIT_STATE_LIFE) > 0.405 then return end
    playerCapital[pi] = nil
    if AiCapEnumGroup == nil then AiCapEnumGroup = CreateGroup() end
    local g = AiCapEnumGroup
    GroupEnumUnitsOfPlayer(g, Player(pi), nil)
    local sz = BlzGroupGetSize(g)
    local pick = nil
    for i = 0, sz - 1 do
        local u = BlzGroupUnitAt(g, i)
        if u ~= nil and GetUnitState(u, UNIT_STATE_LIFE) > 0.405
            and GetUnitAbilityLevel(u, FourCC('A0IQ')) ~= 0 then
            pick = u
            break
        end
    end
    GroupClear(g)
    if pick ~= nil then
        -- Apply the FULL player-style capital treatment, not just a reference. The
        -- original createAiPlayer MakeCapital almost never runs (the seed building
        -- doesn't exist yet when createAiPlayer fires — buildings spawn async), so bots
        -- were left with a plain ~1500-HP building as "capital": no 10000 HP, no armor,
        -- no shared vision, and NOT in udg_StolicaGroups — which also disabled the
        -- destroy-capital=defeat mechanic for every bot. MakeCapital sets HP 10000,
        -- armor 30, sight, vision-sharing, registers the StolicaAttacked/death triggers,
        -- adds to StolicaGroups, and sets playerCapital[pi]. It does NOT call
        -- aiCapitalEnter (the nested-enum path the old comment warned about), so it is
        -- safe inside the perceive tick (checkMovingCity/unitShareVisionAll are plain
        -- player loops, no group enum).
        MakeCapital(pick)
        BrainLogTag(pi, "BRAIN", "adopted + MakeCapital base anchor type="
            .. tostring(GetUnitTypeId(pick)))
    end
end

-- ---- perceive (slow, 1 player/tick) --------------------------------
-- Builds/updates the shared world model in AiData[pi].wm. Objective collection
-- is deferred to Phase 2; Phase 1 captures army geometry + home threat only.
---@param pi integer
-- Compact a unit group in place: drop NIL slots (left by RemoveUnit — these can't be
-- GroupRemoveUnit'd by reference) and dead units. The whole codebase does 100s of
-- RemoveUnit/ReplaceUnit without pulling the unit from the AI pools first, so the
-- groups silently fill with nils — BlzGroupGetSize inflates (army 14% nil, buildersT
-- 61%, navy 100% nil → BrainLandingTick saw zero ships), counts/centroids/ratios skew,
-- and iteration wastes cycles. Rebuild via a temp group since nils have no handle.
gAiCompactTmp = gAiCompactTmp or nil
function AiCompactGroup(g)
    if g == nil then return end
    if gAiCompactTmp == nil then gAiCompactTmp = CreateGroup() end
    GroupClear(gAiCompactTmp)
    local sz = BlzGroupGetSize(g)
    local dirty = false
    for i = 0, sz - 1 do
        local u = BlzGroupUnitAt(g, i)
        if u ~= nil and GetUnitState(u, UNIT_STATE_LIFE) > 0.405 then
            GroupAddUnit(gAiCompactTmp, u)
        else
            dirty = true
        end
    end
    if dirty then
        GroupClear(g)
        GroupAddGroup(gAiCompactTmp, g)
    end
    GroupClear(gAiCompactTmp)
end

-- Heroes are trained/revived through paths that never call aiUnitJoinsArmy, so for brain
-- bots they were NEVER in udg_Ai_army → BrainFocus never moved or fought them. They idled
-- at the capital forever, just soaking up tryBuy items (live: pi=7's 2 heroes sat full-
-- inventory at the BrokenIsles portal while the army was elsewhere). Enlist any live hero
-- not yet in the army so it marches and fights with everyone else. 1 bot/tick (amortized).
AiBrainHeroEnumGrp = AiBrainHeroEnumGrp or CreateGroup()
function AiBrainEnlistHeroes(pi)
    local army = udg_Ai_army[pi]
    if army == nil then return end
    local g = AiBrainHeroEnumGrp
    GroupClear(g)
    GroupEnumUnitsOfPlayer(g, Player(pi), LiveHero)
    local sz = BlzGroupGetSize(g)
    for i = 0, sz - 1 do
        local u = BlzGroupUnitAt(g, i)
        if u ~= nil and not IsUnitInGroup(u, army) then
            GroupAddUnit(army, u)
            if AiSquadAssign ~= nil then AiSquadAssign(pi, u) end
        end
    end
    GroupClear(g)
end

-- One enum of the player's units → { [unitTypeId] = aliveCount }. Reused table to avoid
-- per-tick garbage. Ground truth for cap/limit checks where the drifting g_AiCounts lies.
AiBrainAcountGrp = AiBrainAcountGrp or CreateGroup()
function AiBrainActualCounts(pi, reuse)
    local t = reuse or {}
    for k in pairs(t) do t[k] = nil end
    local army = udg_Ai_army[pi]
    local g = AiBrainAcountGrp
    GroupClear(g)
    GroupEnumUnitsOfPlayer(g, Player(pi), nil)
    local sz = BlzGroupGetSize(g)
    for i = 0, sz - 1 do
        local u = BlzGroupUnitAt(g, i)
        if u ~= nil and GetUnitState(u, UNIT_STATE_LIFE) > 0.405 then
            local id = GetUnitTypeId(u)
            t[id] = (t[id] or 0) + 1
            -- Perf: fold hero-enlist into this SAME pass (was a second full per-player enum
            -- every tick). Enlist any live hero not yet in the army so the brain moves/fights
            -- it (heroes never go through aiUnitJoinsArmy).
            if army ~= nil and IsUnitType(u, UNIT_TYPE_HERO) and not IsUnitInGroup(u, army) then
                GroupAddUnit(army, u)
                if AiSquadAssign ~= nil then AiSquadAssign(pi, u) end
            end
        end
    end
    GroupClear(g)
    return t
end

---@return table
function AiBrainPerceive(pi)
    -- Ensure a base anchor exists (self-guards: enums only while unset/dead).
    AiEnsureCapital(pi)
    local wm = AiData[pi].wm
    if wm == nil then wm = {}; AiData[pi].wm = wm end
    wm.tick = (wm.tick or 0) + 1

    AiApplyBotAuras(pi)  -- map-wide advantage auras (no-op unless AiBotAuras configured)

    -- Purge nil/dead from this bot's pools (1 bot/tick via round-robin, so amortized).
    -- Must run before centroid/count/produce so sizes and ratios are accurate.
    AiCompactGroup(udg_Ai_army[pi])
    AiCompactGroup(udg_Ai_navy[pi])
    AiCompactGroup(udg_Ai_buildersT[pi])
    AiCompactGroup(udg_Ai_builders[pi])
    AiCompactGroup(udg_Ai_buildings[pi])
    AiCompactGroup(udg_Ai_harvest[pi])

    -- Actual live unit-type counts (one enum/tick, 1 bot/tick via round-robin). getAiCount
    -- reads a hashtable counter (g_AiCounts) that DRIFTS — deaths/morphs/RemoveUnit paths
    -- don't all call NumberRem, so e.g. Silitids drones read 18 while 0 are alive, and the
    -- worker block never retrains. wm.acount is the ground truth for cap/limit checks.
    wm.acount = AiBrainActualCounts(pi, wm.acount)

    local cx, cy, n = AiGroupCentroid(udg_Ai_army[pi])
    wm.cx, wm.cy, wm.armyCount = cx, cy, n
    wm.armyContinent = n > 0 and AiContinentOf(cx, cy) or nil

    local cfg = AiBrainCfg(pi)
    local prevCapHP = wm.capHP
    local cap = playerCapital[pi]
    if cap ~= nil and GetUnitState(cap, UNIT_STATE_LIFE) > 0.405 then
        wm.capX, wm.capY = GetUnitX(cap), GetUnitY(cap)
        wm.capHP = GetUnitState(cap, UNIT_STATE_LIFE)
        -- EPA permanently disabled: 100s of RemoveUnit paths can't all get aiFixTrainBefore.
        -- Use capHP drop as threat signal + self-defence from army presence.
        local prevHP = wm._prevCapHP
        wm._prevCapHP = wm.capHP
        if prevHP ~= nil and wm.capHP > 0 and wm.capHP < prevHP then
            wm.threatHome = (prevHP - wm.capHP) + 1.0
        else
            wm.threatHome = 0
        end
    else
        wm.capHP = 0
        wm.threatHome = 0
    end
    -- Active siege = capital HP dropped since last perceive (someone hitting it).
    wm.capSiege = (prevCapHP ~= nil and wm.capHP > 0 and wm.capHP < prevCapHP - 1.0)
    local homeThreat = cfg.homeThreat or AiBrainDefaults.homeThreat
    wm.defendHome = (wm.capHP > 0) and ((wm.threatHome or 0) > homeThreat or wm.capSiege)
    return wm
end

-- ---- builder pacing -----------------------------------------------
-- Returns desired number of active builders (building, not harvesting).
-- Early game: aggressive building. Mid game: balanced. Late: less.
-- totalWrk = T + HV (builders + harvesters). Race can override via AiBuildersCfg.
AiBuildersCfg = AiBuildersCfg or {
    minBld = 5,    -- minimum builders always
    maxBld = 20,   -- maximum builders at peak
    frac    = 0.35, -- fraction of workers that should be building
}
---@param pi integer
---@param totalWrk integer total workers (builders + harvesters)
---@return integer desired builder count
function AiBuildersTarget(pi, totalWrk)
    local cfg = AiBuildersCfg
    local r = AiRaceOf(pi)
    if r ~= nil and r.buildersCfg ~= nil then cfg = r.buildersCfg end
    local bld = math.floor(totalWrk * (cfg.frac or 0.35))
    if bld < (cfg.minBld or 5) then bld = cfg.minBld end
    if bld > (cfg.maxBld or 20) then bld = cfg.maxBld end
    return bld
end

-- ---- squad system -------------------------------------------------
-- AiSquads[pi][sid] = { members=group, state, objective, rally={x,y}, role }
AiSquadCommitMin = AiSquadCommitMin or 4
ProbeLogEnableFlush()

---@param pi integer
---@return table
function AiSquadsOf(pi)
    local t = AiSquads[pi]
    if t == nil then t = {}; AiSquads[pi] = t end
    return t
end

---@param pi integer
---@return integer
function AiSquadNextId(pi)
    local id = (AiSquadSeq[pi] or 0) + 1
    AiSquadSeq[pi] = id
    return id
end

---@param g group
---@return integer
function AiSquadSize(g)
    if g == nil then return 0 end
    local n = 0
    local ok, sz = pcall(BlzGroupGetSize, g)
    if not ok then return 0 end
    local i = 0
    while i < sz do
        local u = BlzGroupUnitAt(g, i)
        if u ~= nil and GetUnitState(u, UNIT_STATE_LIFE) > 0.405 then
            n = n + 1
        end
        i = i + 1
    end
    return n
end

---@param g group
---@return real
function AiSquadPower(g)
    local pow = 0.0
    if g == nil then return pow end
    local sz = BlzGroupGetSize(g)
    local i = 0
    while i < sz do
        local u = BlzGroupUnitAt(g, i)
        if u ~= nil and GetUnitState(u, UNIT_STATE_LIFE) > 0.405 then
            pow = pow + AiUnitPower(u)
        end
        i = i + 1
    end
    return pow
end

-- Order squad members to attack-move via temp copy (safe for persistent groups).
---@param g group
---@param x real
---@param y real
---@return integer
function AiSquadOrderAtk(g, x, y)
    local tmp = CreateGroup()
    local sub = CreateGroup()
    local sz = BlzGroupGetSize(g)
    local k = 0
    while k < sz do
        local u = BlzGroupUnitAt(g, k)
        if u ~= nil and GetUnitState(u, UNIT_STATE_LIFE) > 0.405
            and not IsUnitType(u, UNIT_TYPE_STRUCTURE)
            and not IsUnitType(u, UNIT_TYPE_PEON) then
            GroupAddUnit(tmp, u)
        end
        k = k + 1
    end
    local ordered = 0
    while true do
        local u = FirstOfGroup(tmp)
        if u == nil then break end
        GroupRemoveUnit(tmp, u)
        GroupAddUnit(sub, u)
        ordered = ordered + 1
        if ordered % 12 == 0 then
            GroupPointOrder(sub, "attack", x, y)
            GroupClear(sub)
        end
    end
    if BlzGroupGetSize(sub) > 0 then
        GroupPointOrder(sub, "attack", x, y)
        GroupClear(sub)
    end
    DestroyGroup(tmp)
    DestroyGroup(sub)
    return ordered
end

---@param g group
---@param x real
---@param y real
---@return integer
function AiSquadOrderMov(g, x, y)
    local tmp = CreateGroup()
    local sub = CreateGroup()
    local sz = BlzGroupGetSize(g)
    local k = 0
    while k < sz do
        local u = BlzGroupUnitAt(g, k)
        if u ~= nil and GetUnitState(u, UNIT_STATE_LIFE) > 0.405
            and not IsUnitType(u, UNIT_TYPE_STRUCTURE)
            and not IsUnitType(u, UNIT_TYPE_PEON) then
            GroupAddUnit(tmp, u)
        end
        k = k + 1
    end
    local ordered = 0
    while true do
        local u = FirstOfGroup(tmp)
        if u == nil then break end
        GroupRemoveUnit(tmp, u)
        GroupAddUnit(sub, u)
        ordered = ordered + 1
        if ordered % 12 == 0 then
            GroupPointOrder(sub, "smart", x, y)
            GroupClear(sub)
        end
    end
    if BlzGroupGetSize(sub) > 0 then
        GroupPointOrder(sub, "smart", x, y)
        GroupClear(sub)
    end
    DestroyGroup(tmp)
    DestroyGroup(sub)
    return ordered
end

---@param pi integer
---@param u unit
function AiSquadAssign(pi, u)
    local squads = AiSquadsOf(pi)
    local armyCount = AiData[pi].wm and AiData[pi].wm.armyCount or 0

    -- Capital garrison: keep ONE defense-role squad filled to a FRACTION (AiGarrisonPct) of the
    -- army. Non-hero units go here first (heroes roam with the assault). It holds at the capital
    -- and never marches to far objectives, so the home is never left wide open — but early game
    -- the target is ~0-1 (tiny army) so almost everyone still goes capturing nearby points.
    local capU = playerCapital[pi]
    if capU ~= nil and GetUnitState(capU, UNIT_STATE_LIFE) > 0.405
        and not IsUnitType(u, UNIT_TYPE_HERO) then
        local target = math.ceil(armyCount * (AiGarrisonPct or 0.20))
        if target > (AiGarrisonMax or 9999) then target = AiGarrisonMax end
        if target >= 1 then
            local defSq = nil
            for _, sq in pairs(squads) do if sq.role == "defense" then defSq = sq; break end end
            if defSq == nil then
                local sid = AiSquadNextId(pi)
                local g = CreateGroup(); GroupAddUnit(g, u)
                squads[sid] = { members = g, state = "defense", objective = nil,
                    rally = { x = GetUnitX(capU), y = GetUnitY(capU) }, role = "defense" }
                return
            elseif AiSquadSize(defSq.members) < target then
                GroupAddUnit(defSq.members, u)
                return
            end
        end
    end

    -- Assault: scale the NUMBER of squads with army size instead of dumping everyone into one.
    -- Add to the nearest assault squad that still has ROOM (< AiSquadTargetSize); only spin up
    -- a new squad when every existing one is full AND we're under AiSquadMaxCount. So a small
    -- army = one small squad, a big army = several full squads (the count grows on its own).
    local ux, uy = GetUnitX(u), GetUnitY(u)
    local assaultCount = 0
    local roomSid, roomDist = nil, 1.0e30   -- nearest assault squad with room
    local anySid, anyDist = nil, 1.0e30     -- nearest assault squad of any (overflow fallback)
    for sid, sq in pairs(squads) do
        if sq.role == "assault" then
            assaultCount = assaultCount + 1
            local cx, cy, _ = AiGroupCentroid(sq.members)
            local d = (ux - cx) * (ux - cx) + (uy - cy) * (uy - cy)
            if d < anyDist then anyDist = d; anySid = sid end
            if AiSquadSize(sq.members) < (AiSquadTargetSize or 24) and d < roomDist then
                roomDist = d; roomSid = sid
            end
        end
    end
    if roomSid ~= nil then
        GroupAddUnit(squads[roomSid].members, u); return
    end
    if assaultCount >= (AiSquadMaxCount or 6) and anySid ~= nil then
        GroupAddUnit(squads[anySid].members, u); return  -- at the cap: overflow into nearest
    end
    local sid = AiSquadNextId(pi)
    local rx, ry
    local capU = playerCapital[pi]
    if capU ~= nil and GetUnitState(capU, UNIT_STATE_LIFE) > 0.405 then
        rx, ry = GetUnitX(capU), GetUnitY(capU)
    else
        rx, ry = ux, uy
    end
    local g = CreateGroup()
    GroupAddUnit(g, u)
    squads[sid] = { members = g, state = "muster", objective = nil, rally = { x = rx, y = ry }, role = "assault" }
end

---@param pi integer
function AiSquadReapDead(pi)
    local squads = AiSquadsOf(pi)
    local toRemove = {}
    for sid, sq in pairs(squads) do
        local g = sq.members
        -- Snapshot size ONCE, collect dead, then remove. The old loop re-read
        -- BlzGroupGetSize every iteration and did GroupRemoveUnit WITHOUT advancing i —
        -- if a stale handle read dead but didn't actually leave the group, i never moved
        -- and size never shrank => infinite loop (the squad-FSM hang risk). No mutation
        -- during indexed iteration now.
        local sz = BlzGroupGetSize(g)
        local dead = {}
        for i = 0, sz - 1 do
            local u = BlzGroupUnitAt(g, i)
            if u ~= nil and GetUnitState(u, UNIT_STATE_LIFE) <= 0.405 then
                dead[#dead + 1] = u
            end
        end
        for _, u in ipairs(dead) do GroupRemoveUnit(g, u) end
        -- Remove empty squads (dead units accumulated, squad becomes hollow)
        if AiSquadSize(g) == 0 then
            DestroyGroup(g)
            toRemove[#toRemove + 1] = sid
        end
    end
    for _, sid in ipairs(toRemove) do
        squads[sid] = nil
    end
end

-- Recovery for the teleport-hang: a mage/Zahvat caster (darksummoning) can die or be
-- interrupted mid-channel, leaving the units it was porting idle with a stale order, far
-- from home AND the front AND the army — they hang forever (the old periodic aiRep re-scan
-- used to un-stick them). This is the lightweight replacement: (1) purge dead casters from
-- the AiUnitsToPort queue so the TP system stops trying to use them; (2) re-mobilize
-- orphaned IDLE military units (idle + far from capital + far from the army blob) by sending
-- them back to rejoin the army. Conservative thresholds + a per-call cap so it never thrashes
-- legitimately-deployed units (those aren't idle).
AiRecoverEvery = AiRecoverEvery or 4      -- run every N brain-ticks
AiRecoverFar   = AiRecoverFar   or 5000.0 -- "orphaned" if this far from BOTH home and the army
function AiBrainRecoverStranded(pi, wm)
    -- 1) purge dead/nil TP casters from the port queue
    local q = AiUnitsToPort and AiUnitsToPort[pi]
    if q ~= nil then
        local qs = BlzGroupGetSize(q)
        local dead = {}
        for i = 0, qs - 1 do
            local u = BlzGroupUnitAt(q, i)
            if u == nil or GetUnitState(u, UNIT_STATE_LIFE) <= 0.405 then dead[#dead + 1] = u end
        end
        for _, u in ipairs(dead) do if u ~= nil then GroupRemoveUnit(q, u) end end
    end
    -- 2) re-mobilize orphaned idle units back to the army centroid
    local army = udg_Ai_army[pi]
    if army == nil or wm.cx == nil then return end
    local cx, cy = wm.cx, wm.cy
    local capx, capy = wm.capX, wm.capY
    local far2 = AiRecoverFar * AiRecoverFar
    local sz = BlzGroupGetSize(army)
    local moved = 0
    for i = 0, sz - 1 do
        if moved >= 12 then break end
        local u = BlzGroupUnitAt(army, i)
        if u ~= nil and GetUnitState(u, UNIT_STATE_LIFE) > 0.405
           and not IsUnitType(u, UNIT_TYPE_STRUCTURE) and not IsUnitType(u, UNIT_TYPE_PEON)
           and GetUnitCurrentOrder(u) == 0 then
            local ux, uy = GetUnitX(u), GetUnitY(u)
            local dcx, dcy = ux - cx, uy - cy
            local dC = dcx * dcx + dcy * dcy
            local dH = far2 + 1.0
            if capx ~= nil then local dhx, dhy = ux - capx, uy - capy; dH = dhx * dhx + dhy * dhy end
            if dC > far2 and dH > far2 then
                IssuePointOrder(u, "move", cx, cy)   -- rejoin the army blob
                moved = moved + 1
            end
        end
    end
end

-- ====================================================================
-- Squad FSM dispatcher (OPT-IN). The army normally moves as a single front via
-- BrainFocus; flip AiSquadFsmEnabled=true to instead command the bot's squads through
-- the muster/march/engage/retreat FSM (a couple of squads, not dozens — AiSquadAssign
-- funnels units into the nearest existing squad so the count stays low). Crash-proofing
-- the user asked for: (1) compact each squad's group first so handlers never touch a nil/
-- stale handle; (2) pcall-isolate every handler so a fault logs + skips instead of taking
-- down the tick; (3) apply exactly ONE validated transition per squad per tick — no
-- re-entry loop. Disabled by default so current behaviour is unchanged.
-- ====================================================================
AiSquadFsmEnabled = AiSquadFsmEnabled or false
AiSquadFsmStates = nil  -- built lazily (handlers are defined further down the file)
function AiSquadFsmTick(pi, p, wm)
    if AiSquadFsmStates == nil then
        AiSquadFsmStates = {
            muster  = AiSquadTickMuster,  march   = AiSquadTickMarch,
            engage  = AiSquadTickEngage,  retreat = AiSquadTickRetreat,
            defense = AiSquadTickDefense,
        }
    end
    local squads = AiSquadsOf(pi)
    for sid, sq in pairs(squads) do
        if sq ~= nil and sq.members ~= nil then
            AiCompactGroup(sq.members)  -- purge nil/dead BEFORE any handler reads the group
            if AiSquadSize(sq.members) > 0 then
                local st = sq.state or "muster"
                local handler = AiSquadFsmStates[st]
                if handler == nil then sq.state = "muster"; handler = AiSquadTickMuster end
                local ok, newState = pcall(handler, pi, sid, sq, p, wm)
                if ok then
                    if type(newState) == "string" and AiSquadFsmStates[newState] ~= nil then
                        sq.state = newState  -- one transition; next tick re-enters fresh
                    end
                else
                    AiBrainLogTagSafe(pi, "SQERR", "squad " .. tostring(sid)
                        .. " state=" .. tostring(st) .. " err=" .. tostring(newState))
                end
            end
        end
    end
end

---@param pi integer
---@return table|nil
function AiSquadPickObj(pi, sq, wm)
    local objs = wm.objectives
    if objs == nil or #objs == 0 then return nil end
    local best, bestScore = nil, -1e30
    for _, o in ipairs(objs) do
        o.score = AiObjScore(pi, wm, o)
        if o.score > bestScore then best = o; bestScore = o.score end
    end
    return best and bestScore > 0 and best or nil
end

---@param pi integer
---@param o table
---@return real
function AiObjNeededPower(pi, o)
    local now = AiBrainTickCounter or 0
    local stale = o._epaPowCache ~= nil and (now - (o._epaPowTick or 0)) < (AiEpaObjRefreshEvery or 8)
    if not stale then
        o._epaPowCache = AiEnemyPowerAround(Player(pi), o.x, o.y, 1600.0)
        o._epaPowTick = now
    end
    local pow = o._epaPowCache or 0
    if o.kind == "capital" then pow = pow * 1.5 end
    return math.max(pow, 5.0)
end

---@param pi integer
---@param o table
---@return real
function AiObjCommittedPower(pi, o)
    local pwr = 0.0
    for _, sq in pairs(AiSquadsOf(pi)) do
        if sq.objective ~= nil and sq.objective.key == o.key then
            pwr = pwr + AiSquadPower(sq.members)
        end
    end
    return pwr
end

-- FSM handlers
AiMusterTimeout = AiMusterTimeout or 20  -- bot-ticks a small squad musters before committing anyway
function AiSquadTickMuster(pi, sid, sq, p, wm)
    local sz = AiSquadSize(sq.members)
    local cfg = AiBrainCfg(pi)
    sq.musterTicks = (sq.musterTicks or 0) + 1
    -- Commit at the threshold OR after waiting too long with whatever we've got. A bot whose
    -- whole army is below commitMin (e.g. 3 units, weak/slow economy) otherwise musters at the
    -- capital FOREVER and looks totally passive — better to march the trickle than never attack.
    if sz >= (cfg.commitMin or AiSquadCommitMin) or (sz >= 1 and sq.musterTicks >= AiMusterTimeout) then
        local obj = AiSquadPickObj(pi, sq, wm)
        if obj ~= nil then sq.objective = obj; sq.musterTicks = 0; return "march" end
    end
    AiSquadOrderMov(sq.members, sq.rally.x, sq.rally.y)
    return "muster"
end

function AiSquadTickMarch(pi, sid, sq, p, wm)
    local obj = sq.objective
    if obj == nil then return "muster" end
    local alive = false
    if wm.objectives ~= nil then for _, o in ipairs(wm.objectives) do if o.key == obj.key then alive = true; break end end end
    if not alive then sq.objective = nil; return "muster" end
    local cx, cy, _ = AiGroupCentroid(sq.members)
    local d = SquareRoot((cx - obj.x) * (cx - obj.x) + (cy - obj.y) * (cy - obj.y))
    if d < 600.0 then return "engage" end
    if d < 1200.0 then return "engage" end
    local oc, sc = AiContinentOf(obj.x, obj.y), AiContinentOf(cx, cy)
    if oc ~= nil and sc ~= nil and oc ~= sc then
        -- Cross-continent: must reach the objective via a portal/teleport. NEVER fall through
        -- to a direct attack-move (walks the army straight at an off-continent target = into the
        -- sea / stuck "in the south" — the live bug). Try, in order: mage TP, a waygate on the
        -- first hop, then the WEB (sell) portal network (most continent links are n003 web
        -- portals, NOT waygates, so AiFindPortal returns nil and we must fall back to web).
        local m = AiFindMageOnContinent(pi, oc)
        if m ~= nil then gPi = pi; gPlayer = p; PortTo(m); return "march" end
        local rt = AiPortalRoute(sc, oc)
        if rt ~= nil and #rt >= 2 then
            local portal = AiFindPortal(rt[1], rt[2])
            if portal ~= nil then AiSquadOrderMov(sq.members, GetUnitX(portal), GetUnitY(portal)); return "march" end
        end
        -- Web-portal fallback: route over the web graph and march to the first hop's web portal
        -- (BrainWebPortalTick performs the actual mass-teleport once the army gathers there).
        local wrt = AiWebRoute(sc, oc)
        if wrt ~= nil and #wrt >= 2 then
            local wp = AiFindWebPortal(wrt[1], wrt[2], cx, cy)
            if wp ~= nil then AiSquadOrderMov(sq.members, wp.x, wp.y); return "march" end
        end
        -- No usable portal to the objective's continent: don't march into the sea. Nudge the
        -- TP logistics and drop this objective so the focus re-picks a reachable one.
        AiBrainTryLogistics(pi, p, obj, wm)
        sq.objective = nil
        return "muster"
    end
    AiSquadOrderAtk(sq.members, obj.x, obj.y)
    return "march"
end

function AiSquadTickEngage(pi, sid, sq, p, wm)
    local sz = AiSquadSize(sq.members)
    if sz == 0 then return "muster" end
    if wm.defendHome then sq.rally.x, sq.rally.y = wm.capX, wm.capY; return "retreat" end
    local obj = sq.objective
    local alive = false
    if obj ~= nil and wm.objectives ~= nil then for _, o in ipairs(wm.objectives) do if o.key == obj.key then alive = true; break end end end
    if not alive then
        sq.objective = AiSquadPickObj(pi, sq, wm)
        if sq.objective ~= nil then return "march" end
        sq.rally.x, sq.rally.y = wm.capX or 0.0, wm.capY or 0.0; return "retreat"
    end
    if sz < (AiBrainCfg(pi).commitMin or AiSquadCommitMin) / 2 then
        sq.rally.x, sq.rally.y = wm.capX or 0.0, wm.capY or 0.0; return "retreat"
    end
    if obj ~= nil then AiSquadOrderAtk(sq.members, obj.x, obj.y) end
    return "engage"
end

function AiSquadTickRetreat(pi, sid, sq, p, wm)
    if AiSquadSize(sq.members) == 0 then return "muster" end
    local rx, ry = wm.capX or sq.rally.x, wm.capY or sq.rally.y
    sq.rally.x, sq.rally.y = rx, ry
    local cx, cy, _ = AiGroupCentroid(sq.members)
    local d = SquareRoot((cx - rx) * (cx - rx) + (cy - ry) * (cy - ry))
    if d < 800.0 and not (wm.defendHome or false) then return "muster" end
    AiSquadOrderMov(sq.members, rx, ry)
    return "retreat"
end

-- Garrison: a "defense"-role squad never marches to far objectives — it holds at the capital
-- and engages whatever sieges it. This is the standing home guard (the assault squads still
-- get recalled on top via the defendHome retreat). Without it a bot sends its WHOLE single
-- front out and an enemy strolls into the undefended capital (live: a Goblin walked up to a
-- Silitid capital unopposed). Stays in state "defense" forever.
-- Home-guard size as a FRACTION of the bot's army (not a flat count): early game the army is
-- small so the garrison is tiny (almost everyone goes capturing nearby points), and it scales
-- up proportionally as the army grows. AiGarrisonMax is an optional absolute cap.
AiGarrisonPct = AiGarrisonPct or 0.20   -- 20% of the army held back to defend the capital
AiGarrisonMax = AiGarrisonMax or 9999   -- hard cap on garrison size (off by default)
-- Assault squad sizing (count scales with army instead of one giant blob). A new assault squad
-- spins up only when every existing one is full (AiSquadTargetSize) and we're under the cap.
AiSquadTargetSize = AiSquadTargetSize or 24  -- target units per assault squad
AiSquadMaxCount   = AiSquadMaxCount   or 6   -- max assault squads (overflow into nearest beyond)
function AiSquadTickDefense(pi, sid, sq, p, wm)
    if AiSquadSize(sq.members) == 0 then return "defense" end
    local cx, cy = wm.capX, wm.capY
    if cx == nil then return "defense" end
    sq.rally.x, sq.rally.y = cx, cy
    if wm.defendHome then
        AiSquadOrderAtk(sq.members, cx, cy)  -- under siege: attack-move at home acquires attackers
    else
        local gx, gy, _ = AiGroupCentroid(sq.members)
        local dx, dy = gx - cx, gy - cy
        if (dx * dx + dy * dy) > (900.0 * 900.0) then AiSquadOrderMov(sq.members, cx, cy) end
    end
    return "defense"
end

-- Wrap aiUnitJoinsArmy for brain bots
do
    local _orig = aiUnitJoinsArmy
    function aiUnitJoinsArmy(u, pi)
        _orig(u, pi)
        if AiBrainEnabled(pi) then AiSquadAssign(pi, u) end
    end
end

-- ---- objectives (cluster collection + scoring) ---------------------
-- Grid-bucket capturable/enemy buildings into objective clusters. One pass over
-- the curated groups udg_StolicaGroups (capitals) and udg_ZahvatBuildings (Risk
-- capture targets) — bounded, no full-map enum. Value sums per cluster; NOT HP.
---@param pi integer
---@param wm table
---@return table
function AiBrainCollectObjectives(pi, wm)
    local cfg = AiBrainCfg(pi)
    local cell = cfg.rCluster or AiBrainDefaults.rCluster
    local me = Player(pi)
    local buckets = {}

    local function consider(u, kind)
        if u == nil or GetUnitState(u, UNIT_STATE_LIFE) <= 0.405 then return end
        local owner = GetOwningPlayer(u)
        if owner == me or IsPlayerAlly(owner, me) then return end
        if kind == "capital" and not IsPlayerEnemy(owner, me) then return end
        local x, y = GetUnitX(u), GetUnitY(u)
        local key = R2I(x / cell) * 100000 + R2I(y / cell)
        local b = buckets[key]
        if b == nil then
            b = { sx = 0.0, sy = 0.0, value = 0.0, count = 0, kind = kind }
            buckets[key] = b
        end
        b.sx = b.sx + x
        b.sy = b.sy + y
        b.value = b.value + AiBldValueUnit(u)
        b.count = b.count + 1
        if kind == "capital" then b.kind = "capital" end
    end

    local function scanGroup(g, kind)
        if g == nil then return end
        local n = BlzGroupGetSize(g)
        local i = 0
        while i < n do
            consider(BlzGroupUnitAt(g, i), kind)
            i = i + 1
        end
    end

    scanGroup(udg_StolicaGroups, "capital")
    -- udg_StolicaGroups is only populated by MakeCapital; bots that got their capital
    -- via MakeFakeCapital (the common AI path) set playerCapital[pi] but were NEVER
    -- added to the group, so it sits EMPTY and the brain saw 0 enemy capitals -> it
    -- never attacked anyone and nobody got eliminated. Collect capitals from the
    -- reliable playerCapital[] array too (consider() filters to living enemies).
    if playerCapital ~= nil then
        for cpi = 0, 23 do
            consider(playerCapital[cpi], "capital")
        end
    end
    scanGroup(udg_ZahvatBuildings, "capture")

    local objs = {}
    for key, b in pairs(buckets) do
        objs[#objs + 1] = {
            key = key, kind = b.kind, count = b.count, value = b.value,
            x = b.sx / b.count, y = b.sy / b.count, score = 0.0,
        }
    end
    wm.objectives = objs
    BrainLogTag(pi, "BRAINOBJ", "collected n=" .. tostring(#objs)
        .. " (capitals+capture, cell=" .. tostring(R2I(cell)) .. ")")
    return objs
end

---@param pi integer
---@param wm table
---@param o table
---@return real
function AiObjScore(pi, wm, o)
    local cfg = AiBrainCfg(pi)
    local w = cfg.weights or AiBrainDefaults.weights
    local kindBase = (w.kind and w.kind[o.kind]) or 0
    local dx = (wm.cx or 0.0) - o.x
    local dy = (wm.cy or 0.0) - o.y
    local dist = math.max(SquareRoot(dx * dx + dy * dy), 100.0)

    -- R11: heavily penalise objectives on a different continent — straight-line
    -- distance is misleading across water; land units walk to the shore and stop.
    -- Skip for amphibious races (Naga can swim).
    local race = AiRaceOf(pi)
    local isAmphib = race and (race.continentalNaga == true)
    local capCont = wm.cx and AiContinentOf(wm.cx, wm.cy)
    local objCont = AiContinentOf(o.x, o.y)
    local diffCont = (capCont and objCont and capCont ~= objCont)
    local waterPenalty = 1.0
    if diffCont and not isAmphib then
        -- Portal-aware: a continent reachable by a waygate route (e.g. BrokenIsles->Argus,
        -- the ONLY neighbour of BrokenIsles) is reachable on foot through the portal, so it
        -- must NOT score the same as a truly cross-water landmass. Before this, a BrokenIsles
        -- bot rated its portal-linked Argus enemy at the same crushing 0.05 as unreachable
        -- continents and wandered toward the wrong shore instead of taking the portal.
        -- AiSquadTickMarch already routes a cross-continent squad to the portal — this just
        -- makes the FOCUS actually pick the portal-reachable enemy. One hop 0.6, decaying.
        local rt = AiPortalRoute(capCont, objCont)
        if rt ~= nil and #rt >= 2 then
            waterPenalty = 0.6 - 0.08 * (#rt - 2)
            if waterPenalty < 0.3 then waterPenalty = 0.3 end
        elseif AiContinentOceanBordering(capCont) and AiContinentOceanBordering(objCont) then
            -- No waygate route, but BOTH continents border the single great ocean → the army
            -- can reach it by naval desant (BrainLandingTick sails transports to the target's
            -- coast). Score it like a ~2-hop portal target so the focus actually commits to a
            -- cross-water enemy instead of treating it as unreachable.
            waterPenalty = 0.35
        else
            -- No waygate route, and not reachable by sea either (a void-walled dimension or
            -- dungeon — Argus/Outland/Undercity/... have no ocean coast). Genuinely
            -- unreachable: keep it negligible so a huge-base enemy capital here can't pull the
            -- army onto a continent it can't get to (live: Argus bot stuck on the Pandaria
            -- capital @3999). 0.001 keeps relative order among unreachable objs.
            waterPenalty = 0.001
        end
    end

    -- Per-bot deterministic jitter (±6%) so multiple bots don't all stack on the SAME top
    -- target (live: 5 bots beelined one capital, adjacent bots ignored each other). Hashing
    -- (pi, objective cell) perturbs each bot's ranking differently, spreading them across
    -- targets, while staying deterministic (no desync) and small enough not to invert clear
    -- value gaps. Capture/capital ties (scores within ~3%) get broken per-bot.
    local jh = (pi * 1103515245 + R2I(o.x) * 40503 + R2I(o.y) * 12345) % 100000
    local jitter = 1.0 + (jh / 100000.0 - 0.5) * 0.12

    if o.kind == "capture" then
        local prox = 8000.0 / dist
        return (kindBase + (w.value or 1.0) * o.value + prox) * waterPenalty * jitter
    end
    -- capital: scale priority with the attacker's own army so a strong bot commits to
    -- crushing an enemy capital instead of perpetually re-capturing neutrals (capture
    -- base 150 > capital base 100, so without this the army never graduates to killing
    -- capitals — bots were never eliminating each other). A small army keeps low capital
    -- priority and won't suicide into a 10000-HP capital; armyCount 30 -> 2x base,
    -- 60 -> 3x, 90+ -> 4x, at which point capitals dominate and the army concentrates.
    local armyBoost = 1.0 + math.min((wm.armyCount or 0) / 30.0, 3.0)
    -- Additive army push: a big neutral-capture CLUSTER (many buildings in one cell)
    -- accumulates huge o.value and outscored even a 4x-boosted capital, so titans
    -- (Horde U=96) kept capturing and never assaulted. armyCount*20 makes a strong
    -- army's capital priority decisively dominate capture clusters (96 -> +1920),
    -- while a small army adds little and keeps developing/capturing first.
    local armyPush = (wm.armyCount or 0) * 20.0
    return (kindBase * armyBoost + armyPush + (w.value or 1.0) * o.value - (w.dist or 0.002) * dist) * waterPenalty * jitter
end

-- Highest-scoring objective with hysteresis: stick to current focus unless a
-- candidate beats it by focusMargin, so the army doesn't thrash every tick.
---@param pi integer
---@param wm table
---@return table|nil
function AiBrainPickFocus(pi, wm)
    local objs = wm.objectives
    if objs == nil or #objs == 0 then
        wm.focusKey = nil
        return nil
    end
    local best, bestScore = nil, -1e30
    local cur, curScore = nil, nil
    for _, o in ipairs(objs) do
        o.score = AiObjScore(pi, wm, o)
        if o.score > bestScore then best = o; bestScore = o.score end
        if wm.focusKey ~= nil and o.key == wm.focusKey then cur = o; curScore = o.score end
    end
    local margin = AiBrainCfg(pi).focusMargin or AiBrainDefaults.focusMargin
    if cur ~= nil and bestScore <= curScore + margin then
        return cur
    end
    wm.focusKey = best.key
    return best
end

-- Order all currently-idle army units (B_Lazy) toward (x,y) as attack-move, in
-- chunks. Concentration of force: everyone converges on one point instead of
-- each picking a random local enemy. Used for both focus push and defend recall.
---@param pi integer
---@param p player
---@param x real
---@param y real
---@return integer
function AiBrainOrderIdleTo(pi, p, x, y)
    if gAllyGroup == nil then gAllyGroup = CreateGroup() end
    if gSubGroup == nil then gSubGroup = CreateGroup() end
    CheckPlayer = p
    LazyCount = 0
    GroupEnumUnitsOfPlayer(gAllyGroup, p, nil)
    -- Safe post-filter: remove units that fail IsAiCombatRetaskable + army membership
    local armyGrp = udg_Ai_army[pi]
    local sz = BlzGroupGetSize(gAllyGroup)
    local i = 0
    while i < sz do
        local u = BlzGroupUnitAt(gAllyGroup, i)
        if u ~= nil and IsAiCombatRetaskable(u) and armyGrp ~= nil and IsUnitInGroup(u, armyGrp) then
            LazyCount = LazyCount + 1; i = i + 1
        else
            if u ~= nil then GroupRemoveUnit(gAllyGroup, u) end
            sz = sz - 1
        end
    end
    GroupClear(gSubGroup)
    local ordered, cnt = 0, 0
    local gSize = BlzGroupGetSize(gAllyGroup)
    for gIdx = 1, gSize do
        local u = BlzGroupUnitAt(gAllyGroup, gIdx)
        if u ~= nil then
            GroupAddUnit(gSubGroup, u)
            cnt = cnt + 1
            ordered = ordered + 1
            if cnt >= 12 then
                GroupPointOrder(gSubGroup, "attack", x, y)
                GroupClear(gSubGroup)
                cnt = 0
            end
        end
    end
    if cnt > 0 then
        GroupPointOrder(gSubGroup, "attack", x, y)
        GroupClear(gSubGroup)
    end
    return ordered
end

-- TP logistics hook. If the focus is far and the bot has port-capable mages
-- queued (AiUnitsToPort), kick the existing teleport machinery so the army can
-- redeploy instead of walking the whole map. NOTE: the existing RequestPort
-- ports allies to a port-mage near *any* enemy, not specifically to the focus —
-- true focus-targeted TP needs the continent/portal graph (later phase). For now
-- this nudges the existing system and logs intent. Returns true if it fired.
---@param pi integer
---@param p player
---@param focus table
---@param wm table
---@return boolean
function AiBrainTryLogistics(pi, p, focus, wm)
    local cfg = AiBrainCfg(pi)
    local tpDist = cfg.tpDist or AiBrainDefaults.tpDist
    local dx = (wm.cx or 0.0) - focus.x
    local dy = (wm.cy or 0.0) - focus.y
    local dist = SquareRoot(dx * dx + dy * dy)
    if dist <= tpDist then return false end
    local mages = AiUnitsToPort[pi]
    if mages == nil or FirstOfGroup(mages) == nil then return false end
    BrainLogEvery(pi, "tp", 3, "logistics far focus dist=" .. tostring(R2I(dist))
        .. " -> RequestPort (focus-targeted TP pending portal graph)", "BRAINTP")
    -- Nudge the existing teleport system using a capital as the owning anchor.
    if playerCapital[pi] ~= nil then
        RequestPort(playerCapital[pi])
    end
    return true
end

-- ---- army tick dispatch --------------------------------------------
-- Legacy swarm body, extracted verbatim from PlayerArmy so both the swarm path
-- and the (Phase 1 observational) brain path share one implementation.
---@param p player
function AiArmyLegacyTick(p)
    gPlayer = p
    LazyCount = 0
    if gAllyGroup == nil then
        gAllyGroup = CreateGroup()
    end
    GroupEnumUnitsOfPlayer(gAllyGroup, gPlayer, B_Lazy)
    if FirstOfGroup(gAllyGroup) ~= nil then
        udg_LocalInteger = 1
        while true do
            if udg_LocalInteger > AiMass or FirstOfGroup(gAllyGroup) == nil then break end
            udg_LocalUnit2 = BlzGroupUnitAt(gAllyGroup, GetRandomInt(0, LazyCount - 1))
            GroupRemoveUnit(gAllyGroup, udg_LocalUnit2)
            LazyCount = LazyCount - 1
            if GetUnitTypeId(udg_LocalUnit2) == FourCC('h03C') then
                if Random(1, 2) then
                    IssueImmediateOrder(udg_LocalUnit2, "autoharvestlumber")
                else
                    TryAttack()
                end
            else
                TryAttack()
            end
            udg_LocalInteger = udg_LocalInteger + 1
        end
    end
end

-- Order idle army to a portal unit: "smart" toward it (not attack), give A1GZ
-- portal vision. Enumerates only idle units within 4000 of the portal (not whole
-- map). If army centroid is within 2500, activate portal + push units through.
---@param pi integer
---@param p player
---@param portal unit
---@return integer number of units ordered
function AiBrainOrderToPortal(pi, p, portal)
    if gAllyGroup == nil then gAllyGroup = CreateGroup() end
    if gSubGroup == nil then gSubGroup = CreateGroup() end
    CheckPlayer = p
    local px, py = GetUnitX(portal), GetUnitY(portal)
    GroupEnumUnitsInRange(gAllyGroup, px, py, 4000, B_LazyF)
    local allyCount = CountUnitsInGroup(gAllyGroup)
    if allyCount == 0 then return 0 end
    GroupClear(gSubGroup)
    local gSize = BlzGroupGetSize(gAllyGroup)
    for gIdx = 1, gSize do
        local u = BlzGroupUnitAt(gAllyGroup, gIdx)
        if u ~= nil then
            UnitAddAbility(u, FourCC('A1GZ'))
            GroupAddUnit(gSubGroup, u)
        end
    end
    local cx, cy, _ = AiGroupCentroid(udg_Ai_army[pi])
    local dx, dy = cx - px, cy - py
    local dist = SquareRoot(dx * dx + dy * dy)
    if dist <= 2500 then
        IssueImmediateOrder(portal, "web")
        BlzEndUnitAbilityCooldown(portal, FourCC('A0HY'))
        GroupPointOrder(gSubGroup, "smart", px, py)
        BrainLogEvery(pi, "portalact", 5, "portal activate " .. tostring(R2I(px)) .. "," .. tostring(R2I(py)) .. " allies=" .. tostring(allyCount), "BRAINPORTAL")
    else
        GroupPointOrder(gSubGroup, "smart", px, py)
        BrainLogEvery(pi, "portalmove", 5, "portal walk to " .. tostring(R2I(px)) .. "," .. tostring(R2I(py)) .. " dist=" .. tostring(R2I(dist)) .. " allies=" .. tostring(allyCount), "BRAINPORTAL")
    end
    GroupClear(gSubGroup)
    return allyCount
end

-- ====================================================================
-- Brain-driven production helpers: find a free building of a type, count
-- buildings of a type, find a free worker — all without GroupEnumUnitsOfPlayer.
-- ====================================================================

---@param pi integer
---@param bldType integer
---@return unit|nil
-- `used` (optional): a per-tick set of handle ids already handed out, so successive train
-- orders in ONE BrainProduce pass go to DIFFERENT buildings. Without this, every order piled
-- onto the same first-complete building (which can only train one at a time), so a bot with
-- 97 production buildings + capped gold still fielded a tiny army — most orders silently
-- failed. Spreading across distinct buildings lets them train in parallel.
function AiFindProdBuilding(pi, bldType, used)
    local grp = udg_Ai_buildings[pi]
    if grp == nil then return nil end
    local sz = BlzGroupGetSize(grp)
    -- Return the HEALTHIEST matching building, not just the first. A building still
    -- under construction ramps its HP from ~10% up to 100% and REJECTS train orders;
    -- the first-in-group is frequently a constructing one. (Observed: Illidari built
    -- 10 barracks but trained 0 units — AiFindProdBuilding kept handing BrainProduce a
    -- half-built barracks, so IssueImmediateOrderById silently returned false every
    -- tick. Training from a >=99% barracks worked immediately.) Preferring max HP%
    -- skips constructing buildings whenever a completed one of the same type exists,
    -- and still returns the best available (e.g. a damaged-but-complete one) otherwise.
    local best, bestPct = nil, -1.0
    for i = 0, sz - 1 do
        local u = BlzGroupUnitAt(grp, i)
        if u ~= nil and GetUnitTypeId(u) == bldType
            and GetUnitState(u, UNIT_STATE_LIFE) > 0.405
            and (used == nil or not used[GetHandleId(u)]) then
            local pct = GetUnitStatePercent(u, UNIT_STATE_LIFE, UNIT_STATE_MAX_LIFE)
            if pct >= 99.0 then
                if used ~= nil then used[GetHandleId(u)] = true end
                return u  -- complete & healthy: take it immediately
            end
            if pct > bestPct then best = u; bestPct = pct end
        end
    end
    if best ~= nil and used ~= nil then used[GetHandleId(best)] = true end
    return best
end

---@param pi integer
---@param bldType integer
---@return integer
function AiCountBuildingsOfType(pi, bldType)
    local grp = udg_Ai_buildings[pi]
    if grp == nil then return 0 end
    local n = 0
    local sz = BlzGroupGetSize(grp)
    for i = 0, sz - 1 do
        local u = BlzGroupUnitAt(grp, i)
        if u ~= nil and GetUnitTypeId(u) == bldType
            and GetUnitState(u, UNIT_STATE_LIFE) > 0.405 then
            -- R5: skip incomplete buildings (HP < max HP). Channeling races
            -- leave pristine foundations when the builder is yanked/killed.
            local maxHp = BlzGetUnitMaxHP(u)
            if maxHp > 1 and GetUnitState(u, UNIT_STATE_LIFE) < maxHp - 0.5 then
                -- incomplete — don't count; BrainResumeBuildings will fix it
            else
                n = n + 1
            end
        end
    end
    return n
end

---@param pi integer
---@return unit|nil
function AiFindFreeWorker(pi)
    -- Try builders pool first, then buildersT (only ones NOT mid-build-claim),
    -- then pull from harvest.
    local function alive(u)
        return u ~= nil and GetUnitState(u, UNIT_STATE_LIFE) > 0.405
    end
    local now = AiBrainTickCounter or 0
    local grp = udg_Ai_builders[pi]
    if grp ~= nil then
        local sz = BlzGroupGetSize(grp)
        for i = 0, sz - 1 do
            local u = BlzGroupUnitAt(grp, i)
            if alive(u) then return u end
        end
    end
    local grpT = udg_Ai_buildersT[pi]
    if grpT ~= nil then
        local sz = BlzGroupGetSize(grpT)
        for i = 0, sz - 1 do
            local u = BlzGroupUnitAt(grpT, i)
            -- Any idle worker in buildersT is available — claim guard is redundant
            -- now that AiRecycleBuilders no longer yanks channeling workers.
            if alive(u) and GetUnitCurrentOrder(u) == 0 then return u end
        end
    end
    local grpH = udg_Ai_harvest[pi]
    if grpH ~= nil then
        local sz = BlzGroupGetSize(grpH)
        for i = 0, sz - 1 do
            local u = BlzGroupUnitAt(grpH, i)
            if alive(u) then return u end
        end
    end
    return nil
end

---@param pi integer
---@param minCount integer|nil
---@return integer
function AiEnsureBuilderReserve(pi, minCount)
    local want = minCount or 2
    local grp = udg_Ai_builders[pi]
    local grpH = udg_Ai_harvest[pi]
    if grp == nil or grpH == nil then return 0 end

    local aliveBuilders = 0
    local sz = BlzGroupGetSize(grp)
    for i = 0, sz - 1 do
        local u = BlzGroupUnitAt(grp, i)
        if u ~= nil and GetUnitState(u, UNIT_STATE_LIFE) > 0.405 then
            aliveBuilders = aliveBuilders + 1
            if aliveBuilders >= want then
                return 0
            end
        end
    end

    local moved = 0
    local szH = BlzGroupGetSize(grpH)
    for i = 0, szH - 1 do
        if aliveBuilders + moved >= want then break end
        local u = BlzGroupUnitAt(grpH, i)
        if u ~= nil
            and GetUnitState(u, UNIT_STATE_LIFE) > 0.405
            and GetUnitCurrentOrder(u) ~= 851972
            and GetUnitCurrentOrder(u) ~= 851976 then
            GroupAddUnit(grp, u)
            GroupRemoveUnit(grpH, u)
            moved = moved + 1
        end
    end
    return moved
end

-- Is this worker actually constructing? True if an OWN incomplete structure sits
-- within build range of the worker. Used to protect channeling builders (Human/
-- Forsaken peasants stand at the site) from being recycled, while still freeing
-- workers that merely hold a stale order (852018 harvest/move, etc.) but aren't
-- building anything — the buildersT-clog that drains harvest to 0 for some races.
---@param pi integer
---@param u unit
---@return boolean
function AiWorkerIsBuilding(pi, u)
    local p = Player(pi)
    -- A worker actively repairing/resuming a structure is building even if it is
    -- still walking toward it (no incomplete structure within range yet). 852024 =
    -- "repair" (the order BrainResumeBuildings issues to finish a stalled foundation).
    local ord = GetUnitCurrentOrder(u)
    if ord == 852024 then return true end
    if gWorkerProbe == nil then gWorkerProbe = CreateGroup() end
    -- 400, not 256: a 4x4 building's centre sits ~256-300 from where a channeling
    -- builder stands at the footprint edge, so 256 missed large structures and the
    -- builder got recycled mid-build. 400 covers the largest footprints.
    GroupEnumUnitsInRange(gWorkerProbe, GetUnitX(u), GetUnitY(u), 400, nil)
    local sz = BlzGroupGetSize(gWorkerProbe)
    local building = false
    for k = 0, sz - 1 do
        local b = BlzGroupUnitAt(gWorkerProbe, k)
        if b ~= nil and GetOwningPlayer(b) == p
            and IsUnitType(b, UNIT_TYPE_STRUCTURE)
            and GetUnitState(b, UNIT_STATE_LIFE) > 0.405
            and GetUnitStatePercent(b, UNIT_STATE_LIFE, UNIT_STATE_MAX_LIFE) < 99.0 then
            building = true
            break
        end
    end
    GroupClear(gWorkerProbe)
    return building
end

-- E3: recycle stuck/idle build-pool workers back to harvesting. A worker past its
-- build-claim window that is NOT adjacent to an own incomplete structure isn't
-- building anything → return it to the lumber line instead of letting it pile up in
-- buildersT (harvest=0 across several races was the smoking gun — stuck workers held
-- order 852018/852017 forever and never went idle). Channeling builders (next to an
-- incomplete structure) are preserved. Bounded per call to avoid order spam.
---@param pi integer
---@param maxMove integer
function AiRecycleBuilders(pi, maxMove)
    local grpT = udg_Ai_buildersT[pi]
    if grpT == nil then return end
    local grpH = udg_Ai_harvest[pi]
    if grpH == nil then return end
    local now = AiBrainTickCounter or 0
    -- GC stale reservations
    if now % 60 == 0 then
        for k, t in pairs(g_BuildSpotReserved) do
            if now - t >= g_BuildReserveTicks then g_BuildSpotReserved[k] = nil end
        end
    end
    local sz = BlzGroupGetSize(grpT)
    -- Collect victims FIRST (never mutate the group while iterating it by index —
    -- that is an engine footgun); move + order them after the read loop.
    local victims = nil
    local found = 0
    local cap = maxMove or 4
    local i = 0
    while i < sz and found < cap do
        local u = BlzGroupUnitAt(grpT, i)
        if u ~= nil and GetUnitState(u, UNIT_STATE_LIFE) > 0.405 then
            local c = AiBuildClaim[u]
            local expired = c == nil or (now - c) >= AiBuildClaimTicks
            -- Naval builders walk far to an open-water shipyard spot, so during the
            -- long approach there's no incomplete structure next to them — without this
            -- grace the proximity check below would recycle them mid-walk and the
            -- shipyard would never start. Protect them for a longer window.
            local navalUntil = AiNavalBuildUntil[u]
            local navalBusy = navalUntil ~= nil and now < navalUntil
            -- Recycle when the claim window has passed AND the worker is not actually
            -- building (no own incomplete structure nearby). This frees both idle
            -- (order==0) workers and ones stuck holding a stale harvest/move order,
            -- while protecting active channeling builders (nearby incomplete bld).
            if expired and not navalBusy and not AiWorkerIsBuilding(pi, u) then
                if victims == nil then victims = {} end
                found = found + 1
                victims[found] = u
            end
        end
        i = i + 1
    end
    if victims == nil then return end
    for k = 1, found do
        local u = victims[k]
        GroupRemoveUnit(grpT, u)
        GroupAddUnit(grpH, u)
        AiBuildClaim[u] = nil
        AiNavalBuildUntil[u] = nil
        IssueImmediateOrder(u, "autoharvestlumber")
    end
end

-- ====================================================================
-- R5: resume stalled construction — scan udg_Ai_buildings for incomplete
-- buildings (HP < max HP) and send idle workers to repair/resume them.
-- Fixes channeling races where a worker was killed or (before the
-- channeling-yank fix) recycled mid-build, permanently stalling the site.
-- ====================================================================

---@param pi integer
---@return integer
function BrainResumeBuildings(pi)
    local grp = udg_Ai_buildings[pi]
    if grp == nil then return 0 end
    local sz = BlzGroupGetSize(grp)
    if sz == 0 then return 0 end

    local resumed = 0
    local maxN = AiBrainMaxBuild

    for i = 0, sz - 1 do
        if resumed >= maxN then break end
        local b = BlzGroupUnitAt(grp, i)
        if b ~= nil and GetUnitState(b, UNIT_STATE_LIFE) > 0.405 then
            local hp = GetUnitState(b, UNIT_STATE_LIFE)
            local maxHp = BlzGetUnitMaxHP(b)
            if maxHp > 1 and hp < maxHp - 0.5 then
                local worker = AiFindFreeWorker(pi)
                if worker ~= nil then
                    GroupAddUnit(udg_Ai_buildersT[pi], worker)
                    GroupRemoveUnit(udg_Ai_builders[pi], worker)
                    GroupRemoveUnit(udg_Ai_harvest[pi], worker)
                    AiBuildClaim[worker] = AiBrainTickCounter or 0
                    IssueTargetOrder(worker, "repair", b)
                    resumed = resumed + 1
                end
            end
        end
    end
    return resumed
end

-- ====================================================================
-- BrainProduce: scan compTarget → deficit → find building → issue train order.
-- No random, no GroupEnum. Configurable via AiBrainMaxProduce.
-- ====================================================================

---@param pi integer
---@param wm table
---@param race table
---@return integer
function BrainProduce(pi, wm, race)
    local prod = race.production
    local comp = race.compTarget
    if not prod then return 0 end

    -- Per-tick set of production buildings already issued an order, so each train order this
    -- pass goes to a DIFFERENT building (parallel training instead of piling on one).
    local usedBld = {}
    local ordered = 0
    local maxN = AiBrainMaxProduce
    local now = AiBrainTickCounter or 0

    -- R7: build a set of legitimate producer building types — skip production
    -- entries whose bldType is NOT an actual building (e.g. Silitids larva e01I).
    -- ALSO include production keys so non-structure producers (larvae, eggs) work.
    local isBldType = {}
    local buildList = race.buildings
    if buildList then
        isBldType[buildList.seed] = true
        for _, row in ipairs(buildList) do
            if type(row[1]) == "number" then isBldType[row[1]] = true end
        end
    end
    if prod then
        for k, _ in pairs(prod) do
            if type(k) == "number" then isBldType[k] = true end
        end
    end

    -- 1) Workers: train independently of compTarget, always up to cap
    local w = prod.worker
    if w and w.from and w.id then
        local wCnt = (wm.acount and wm.acount[w.id]) or 0  -- actual live count (getAiCount drifts)
        if wCnt < (w.cap or 40) then
            for _, fromBldType in ipairs(w.from) do
                local bld = AiFindProdBuilding(pi, fromBldType, usedBld)
                if bld ~= nil then
                    local key = pi * 1000000 + w.id
                    local last = g_AiOrdered[key]
                    if not last or (now - last) > AiRetrainInterval then
                        IssueImmediateOrderById(bld, w.id)
                        g_AiOrdered[key] = now
                        ordered = ordered + 1
                    end
                    break  -- one worker order per tick is enough
                end
            end
        end
    end

    -- 1b) HERO PRIORITY: train altar units (heroes) before the mass army drains the gold.
    -- Heroes have a tiny compTarget ratio (~0.03) and high cost, so in the gold-starved
    -- general loop below they lose every gold race and never get built (live: Alliance bot
    -- gold=0, 0 heroes despite 2 altars). Every race's heroes sit at race.altar, so issuing
    -- those first — up to each row's limit — is a general fix. Order fails harmlessly when
    -- gold is short and retries next tick; issuing FIRST means the hero grabs gold before
    -- cheaper army orders spend it below the hero's cost.
    if race.altar ~= nil and prod[race.altar] ~= nil then
        -- TOTAL hero cap. The map's LimitHero trigger only caps each hero TYPE to 1, with no
        -- overall limit, so the bot trained ONE OF EVERY altar hero (Cult: CD01+CD02+CD03 = 3)
        -- while a human picks a single hero. Count live + in-flight heroes across ALL altar rows
        -- and stop at AiMaxHeroes so bots field the same hero count a player does. Tunable per
        -- race later via race.maxHeroes if some race is meant to have more.
        local heroMax = race.maxHeroes or AiMaxHeroes
        local heroCount = 0
        for _, row in ipairs(prod[race.altar]) do
            local hid = row[1]
            if hid ~= nil and hid ~= 0 then
                heroCount = heroCount + ((wm.acount and wm.acount[hid]) or 0)
                local ll = g_AiOrdered[pi * 1000000 + hid]
                if ll ~= nil and (now - ll) < AiLimitedBuildTicks then heroCount = heroCount + 1 end
            end
        end
        for _, row in ipairs(prod[race.altar]) do
            if ordered >= maxN then break end
            if heroCount >= heroMax then break end  -- bot already at its hero quota
            local hid = row[1]
            if hid ~= nil and hid ~= 0 then
                local cur = (wm.acount and wm.acount[hid]) or 0  -- actual live count (getAiCount drifts → hero dupes)
                local lim = row.limit or row[2] or 1
                local lk = pi * 1000000 + hid
                local ll = g_AiOrdered[lk]
                local inFlight = (ll ~= nil and (now - ll) < AiLimitedBuildTicks) and 1 or 0
                if cur + inFlight < lim then
                    local bld = AiFindProdBuilding(pi, race.altar, usedBld)
                    if bld ~= nil then
                        IssueImmediateOrderById(bld, hid)
                        g_AiOrdered[lk] = now
                        ordered = ordered + 1
                        heroCount = heroCount + 1
                    end
                end
            end
        end
    end

    if not comp then return ordered end

    local totalMil = wm.armyCount or 0
    if totalMil < 1 then totalMil = 1 end
    -- R16: drive composition toward an absolute desired size, NOT toward the current
    -- size. ratioBase = max(totalMil, desired) keeps per-unit targets above the current
    -- counts until the army actually reaches `desired`, so growth never stalls at MinArmy.
    -- Food headroom is the real ceiling (gated just below). Per-race override: a config
    -- `desiredArmy` field lets swarm races (Silitids etc.) field bigger numbers than the
    -- global default without touching everyone else.
    local desired = AiScaled(race.desiredArmy or AiBrainDesiredArmy)
    local ratioBase = math.max(totalMil, desired)

    -- R16: food gate. If the bot is supply-capped there is no point spamming train
    -- orders (they just fail). Stop military production when food headroom is gone;
    -- workers were already handled above and are cheap. A small margin lets a farm/
    -- upkeep building finish before we resume.
    do
        local pl = Player(pi)
        local foodCap  = GetPlayerState(pl, PLAYER_STATE_RESOURCE_FOOD_CAP)
        local foodUsed = GetPlayerState(pl, PLAYER_STATE_RESOURCE_FOOD_USED)
        if foodCap > 0 and foodUsed >= foodCap then
            return ordered  -- supply-capped: skip military this tick
        end
    end

    -- R15: only distribute ratios across UNITS THAT CAN ACTUALLY BE TRAINED.
    -- Most races have 1-2 trainable units out of 5-13 listed — the rest require
    -- tech or different buildings. If we include untrainable units in the budget,
    -- the trainable ones hit their ratio at 3-5 army and growth stalls.
    local trainableSum = 0.0
    local isTrainable = {}
    for unitId, targetRatio in pairs(comp) do
        if type(unitId) ~= "number" then goto nextSum end
        -- Check if any building can produce this unit
        for bldType, rows in pairs(prod) do
            if bldType == "worker" then goto nextBldSum end
            if type(rows) ~= "table" then goto nextBldSum end
            if not isBldType[bldType] then goto nextBldSum end
            for _, row in ipairs(rows) do
                if row[1] == unitId then
                    if AiFindProdBuilding(pi, bldType) ~= nil then
                        isTrainable[unitId] = true
                        trainableSum = trainableSum + targetRatio
                        goto found
                    end
                elseif row.branch then
                    local pick
                    if race.branches and race.branches[row.branch] then
                        pick = race.branches[row.branch](pi)
                    end
                    pick = pick and row.black or row.other
                    if pick == unitId then
                        if AiFindProdBuilding(pi, bldType) ~= nil then
                            isTrainable[unitId] = true
                            trainableSum = trainableSum + targetRatio
                            goto found
                        end
                    end
                end
            end
            ::found::
            ::nextBldSum::
        end
        ::nextSum::
    end
    if trainableSum <= 0 then trainableSum = 1.0 end  -- avoid div/zero

    -- 2) Military: scan compTarget for deficit, find building, issue order
    for unitId, targetRatio in pairs(comp) do
        if ordered >= maxN then break end
        if type(unitId) ~= "number" or targetRatio == nil then goto skipUnit end
        if not isTrainable[unitId] then goto skipUnit end  -- R15: skip untrainable

        local current = (wm.acount and wm.acount[unitId]) or getAiCount(pi, unitId) or 0  -- actual live count
        if current < 0 then current = 0 end
        -- R15: scale target to only-trainable pool. E.g. 9% out of 18% total → 50%
        local scaledTarget = targetRatio / trainableSum
        local currentRatio = current / ratioBase
        if currentRatio >= scaledTarget then goto skipUnit end

        -- Find which building produces this unit
        for bldType, rows in pairs(prod) do
            if bldType == "worker" then goto skipBld end
            if type(rows) ~= "table" then goto skipBld end
            if not isBldType[bldType] then goto skipBld end  -- R7: skip non-buildings (larva, eggs, etc.)
            for _, row in ipairs(rows) do
                local uid = row[1]
                if uid ~= nil and uid ~= 0 then
                    if uid == unitId then
                        -- Respect a per-row hard cap (e.g. heroes limit=1). Count units
                        -- still IN TRAINING (ordered within AiLimitedBuildTicks) toward the
                        -- cap — getAiCount only sees finished units, so a slow hero was
                        -- ordered 2-3x before the first appeared (Cult got 2x CD02).
                        if row.limit then
                            local lk = pi * 1000000 + unitId
                            local ll = g_AiOrdered[lk]
                            local inFlight = (ll ~= nil and (now - ll) < AiLimitedBuildTicks) and 1 or 0
                            if current + inFlight >= row.limit then goto skipBld end
                        end
                        local bld = AiFindProdBuilding(pi, bldType, usedBld)
                        if bld ~= nil then
                            local key = pi * 1000000 + unitId
                            local last = g_AiOrdered[key]
                            if not last or (now - last) > AiRetrainInterval then
                                IssueImmediateOrderById(bld, unitId)
                                g_AiOrdered[key] = now
                                ordered = ordered + 1
                            end
                        end
                        goto skipBld
                    end
                elseif row.branch then
                    local pick
                    if race.branches and race.branches[row.branch] then
                        pick = race.branches[row.branch](pi)
                    end
                    pick = pick and row.black or row.other
                    if pick == unitId then
                        if row.limit then
                            local lk = pi * 1000000 + unitId
                            local ll = g_AiOrdered[lk]
                            local inFlight = (ll ~= nil and (now - ll) < AiLimitedBuildTicks) and 1 or 0
                            if current + inFlight >= row.limit then goto skipBld end
                        end
                        local bld = AiFindProdBuilding(pi, bldType, usedBld)
                        if bld ~= nil then
                            local key = pi * 1000000 + unitId
                            local last = g_AiOrdered[key]
                            if not last or (now - last) > AiRetrainInterval then
                                IssueImmediateOrderById(bld, unitId)
                                g_AiOrdered[key] = now
                                ordered = ordered + 1
                            end
                        end
                        goto skipBld
                    end
                end
            end
            ::skipBld::
        end
        ::skipUnit::
    end

    return ordered
end

-- ====================================================================
-- BrainBuild: read race.buildings → find unbuilt → free worker → TryBuild.
-- Expansion + naval decisions on schedule. Configurable via AiBrainMaxBuild,
-- AiBrainExpansionEvery, AiBrainNavalEvery.
-- ====================================================================

---@param pi integer
---@param wm table
---@param race table
---@return integer
function BrainBuild(pi, wm, race)
    local buildOrder = race.buildings
    if not buildOrder then return 0 end

    AiEnsureBuilderReserve(pi, 3)

    local built = 0
    local maxN = AiBrainMaxBuild

    -- Handle seed building first (named key)
    local seedType = buildOrder.seed
    if seedType and type(seedType) == "number" then
        local count = AiCountBuildingsOfType(pi, seedType)
        if count < 1 then
            local worker = AiFindFreeWorker(pi)
            if worker ~= nil then
                TryBuild_u = worker
                TryBuildWithType(seedType)
                built = built + 1
            end
        end
    end

    -- R9: separate production buildings (barracks, etc.) from other buildings.
    -- Production buildings get priority — they make army, which captures cities.
    -- A production building is one listed as a key in race.production (excluding "worker"),
    -- OR a building that trains workers (worker.from).
    local prodKeys = {}
    if race.production then
        for k, _ in pairs(race.production) do
            if type(k) == "number" then prodKeys[k] = true end
        end
        -- R14: buildings that train workers get production priority (e.g. Silitids hives)
        local wk = race.production.worker
        if wk and wk.from then
            for _, fromBld in ipairs(wk.from) do
                prodKeys[fromBld] = true
            end
        end
    end

    local prodRows, otherRows = {}, {}
    for _, row in ipairs(buildOrder) do
        local bldType = row[1]
        if type(bldType) == "number" then
            if prodKeys[bldType] then
                prodRows[#prodRows + 1] = row
            else
                otherRows[#otherRows + 1] = row
            end
        end
    end

    -- PASS 1: production buildings first
    for _, row in ipairs(prodRows) do
        if built >= maxN then break end
        built = built + BrainBuildOne(pi, race, row)
    end

    -- PASS 2: everything else
    for _, row in ipairs(otherRows) do
        if built >= maxN then break end
        built = built + BrainBuildOne(pi, race, row)
    end

    -- Expansion check: brain decides to seed a new cluster far from capital
    if wm.tick % AiBrainExpansionEvery == 0 then
        BrainExpandDecision(pi, wm, race)
    end

    -- Naval check: build shipyard / fleet after startup delay
    if wm.tick > AiBrainNavalStartTick and wm.tick % AiBrainNavalEvery == 0 then
        BrainNavalDecision(pi, wm, race)
    end

    -- R13: tier-up buildings (techUp from strategData.steps). Upgrades town halls,
    -- hives, etc. so tier2 production buildings unlock.
    if race.strategData and race.strategData.steps then
        BrainStrategTick(pi, p, race, wm)
    end
    if race.mergeCast ~= nil and (wm.tick % 5) == 0 then
        BrainMergeTick(pi, wm, race)
    end

    -- R5: resume stalled construction before recycling idle workers.
    -- Channeling races (Human, Forsaken) need the worker to stay; if the
    -- original builder was killed/recycled, the building site stays incomplete.
    BrainResumeBuildings(pi)

    -- E3: every tick, drain idle/failed workers from buildersT back to harvest
    -- (not just when built==0) so the build pool can't clog and lumber keeps flowing.
    AiRecycleBuilders(pi, 6)

    return built
end

-- Helper: try to build one row from the buildings table. Returns 1 if built, 0 otherwise.
---@param pi integer
---@param race table
---@param row table
---@return integer
function BrainBuildOne(pi, race, row)
    local bldType = row[1]
    if type(bldType) ~= "number" then return 0 end

    local limit = AiScaled(row[2] or 1)  -- per-type building count, scaled by AiSizeScale (round up)
    local count = AiCountBuildingsOfType(pi, bldType)
    if count >= limit then return 0 end

    if row.gate then
        local gateFn = race.gates and race.gates[row.gate]
        if gateFn and not gateFn(pi) then return 0 end
    end

    local worker = AiFindFreeWorker(pi)
    if worker == nil then return 0 end

    TryBuild_u = worker
    if TryBuildWithType(bldType) then return 1 end
    return 0
end

---@param pi integer
---@param wm table
---@param race table
function BrainExpandDecision(pi, wm, race)
    -- DISABLED: this used to grab a free worker and "move" it AiBuildingRadius*7 away
    -- with no follow-up build order — the worker walked far from base and sat idle,
    -- one of the causes of "groups of workers wandering off" and a drain on the build/
    -- harvest pool. Real map expansion happens by the army capturing neutral cities
    -- (StolicaGroups / ZahvatBuildings objectives). Kept as a no-op so the call site
    -- and any future real expansion logic have a home.
    return
end

---@param pi integer
---@param wm table
---@param race table
-- Terrain helpers. Engine semantics (verified live): a WATER tile is blocked for
-- WALKABILITY and open for FLOATABILITY; a LAND tile is the reverse.
local function AiTerrainWater(x, y) return not IsTerrainPathable(x, y, PATHING_TYPE_FLOATABILITY) end
local function AiTerrainLand(x, y)  return not IsTerrainPathable(x, y, PATHING_TYPE_WALKABILITY) end

-- A shipyard (h0D1 etc.) has preventplace=unfloat and a 4x4 footprint, so it can ONLY
-- be placed on OPEN WATER: the center and its whole footprint must be floatable. A
-- ground worker still builds it, so reachable shore (land) must be nearby. The old
-- code called AiBuildPlaceable (land-only — it rejects every water tile) on the far
-- hardcoded udg_WaterPoints, so the order was always rejected and navy stayed 0.
-- This sampling pattern was confirmed live: the issued build order was accepted.
local function AiNavalFootprintWater(x, y)
    if not AiTerrainWater(x, y) then return false end
    local r1, r2 = 256.0, 128.0
    local o = { {r1,0},{-r1,0},{0,r1},{0,-r1},{r1,r1},{-r1,-r1},{r1,-r1},{-r1,r1},
                {r2,0},{-r2,0},{0,r2},{0,-r2} }
    for i = 1, 12 do
        if not AiTerrainWater(x + o[i][1], y + o[i][2]) then return false end
    end
    return true
end
local function AiNavalLandWithin(x, y, rad)
    for i = 0, 11 do
        local a = (I2R(i) / 12.0) * 2.0 * bj_PI
        if AiTerrainLand(x + rad * Cos(a), y + rad * Sin(a)) then return true end
    end
    return false
end

-- A worker sent to build a shipyard is protected from build-pool recycling until this
-- tick (it walks far to open water with no incomplete structure beside it en route).
AiNavalBuildUntil = AiNavalBuildUntil or {}
AiNavalBuildGrace = AiNavalBuildGrace or 360  -- ticks a shipyard-builder is protected from
                                              -- recycle. Raised 120->360: with the distance cap
                                              -- removed a worker may trek far across the map to a
                                              -- designated water point, so it needs longer before
                                              -- the build pool reclaims it.

-- Open-water-near-shore shipyard spots around the capital, nearest first. Cached per
-- bot (the terrain scan is heavy and water doesn't move).
g_NavalSpots = g_NavalSpots or {}
---@param pi integer
---@param cx real
---@param cy real
---@return table
-- Only consider water reasonably close to the capital. For a coastal capital the
-- nearest open-water-near-shore spot is its OWN coastline (a ground worker can reach
-- it). For an inland capital the nearest such spot is across other land/water and the
-- worker can't path to it — so we cap the range and simply skip naval there instead of
-- stranding a worker trekking across the map.
AiNavalMaxRange = AiNavalMaxRange or 10000.0
function AiFindNavalSpots(pi, cx, cy)
    if g_NavalSpots[pi] ~= nil then return g_NavalSpots[pi] end
    local cand = {}
    -- 0) Curated hand-placed spots on the bot's OWN continent (same landmass = a ground
    --    worker can always path there, so NO range cap needed). These are exact coords where
    --    a shipyard was successfully built during testing, so they're guaranteed buildable
    --    and cover coastlines the capital ring-scan misses. Highest priority.
    if AiCuratedNavalSpots ~= nil then
        local capCont = AiContinentOf(cx, cy)
        local list = capCont and AiCuratedNavalSpots[capCont]
        if list ~= nil then
            for _, sp in ipairs(list) do
                local dx, dy = cx - sp[1], cy - sp[2]
                cand[#cand + 1] = { x = sp[1], y = sp[2], d = SquareRoot(dx * dx + dy * dy) }
            end
        end
    end
    -- WHY the rework (session 2): removing the distance cap (earlier request) made every
    -- bot target the globally-nearest designated point even when it sat 12k-17k away on a
    -- DIFFERENT landmass — a land worker can't path there, so the build order issued but
    -- the shipyard was never placed (live: nearest WaterPoint for some bots = 16986). So
    -- we now bound BOTH sources to AiNavalMaxRange and, crucially, also scan the bot's OWN
    -- coastline (contiguous from the capital = actually reachable).
    -- 1) Designer-placed points within reach (curated shoreline spots, center-water only —
    --    their footprint corners touch land so the strict footprint scan would reject them).
    if type(udg_WaterPoints) == "table" then
        local i = 1
        while udg_WaterPoints[i] ~= nil do
            local p = udg_WaterPoints[i]
            if p.x ~= nil then
                local dx, dy = cx - p.x, cy - p.y
                local d = SquareRoot(dx * dx + dy * dy)
                if d <= AiNavalMaxRange and AiTerrainWater(p.x, p.y) then
                    cand[#cand + 1] = { x = p.x, y = p.y, d = d }
                end
            end
            i = i + 1
        end
    end
    -- 2) Ring-scan the bot's OWN coastline (open-water-near-shore within reach). These are
    --    contiguous with the capital so a ground worker can always path to them.
    local r = 384.0
    while r <= AiNavalMaxRange and #cand < 12 do
        local s = 0
        while s < 36 do
            local ang = (I2R(s) / 36.0) * 2.0 * bj_PI
            local x = cx + r * Cos(ang)
            local y = cy + r * Sin(ang)
            if AiNavalFootprintWater(x, y) and AiNavalLandWithin(x, y, 700.0) then
                cand[#cand + 1] = { x = x, y = y, d = r }
            end
            s = s + 1
        end
        r = r + 384.0
    end
    table.sort(cand, function(a, b) return a.d < b.d end)
    local spots = {}
    for _, c in ipairs(cand) do spots[#spots + 1] = { x = c.x, y = c.y } end
    -- 3) Last resort for an island/inland bot with NO spot in range: allow the far
    --    designated points so it at least attempts (better than never trying).
    if #spots == 0 and type(udg_WaterPoints) == "table" then
        local far = {}
        local i = 1
        while udg_WaterPoints[i] ~= nil do
            local p = udg_WaterPoints[i]
            if p.x ~= nil and AiTerrainWater(p.x, p.y) then
                local dx, dy = cx - p.x, cy - p.y
                far[#far + 1] = { x = p.x, y = p.y, d = SquareRoot(dx * dx + dy * dy) }
            end
            i = i + 1
        end
        table.sort(far, function(a, b) return a.d < b.d end)
        for _, c in ipairs(far) do spots[#spots + 1] = { x = c.x, y = c.y } end
    end
    g_NavalSpots[pi] = spots
    return spots
end

-- Scan rings outward from (x,y) for the nearest buildable open-water-near-shore spot.
-- Returns spot coords or nil. Bounded radius so it stays cheap when called per-worker.
local function AiNavalSpotNear(x, y, maxr)
    local r = 256.0
    while r <= maxr do
        local s = 0
        while s < 16 do
            local ang = (I2R(s) / 16.0) * 2.0 * bj_PI
            local px, py = x + r * Cos(ang), y + r * Sin(ang)
            if AiNavalFootprintWater(px, py) and AiNavalLandWithin(px, py, 700.0) then
                return px, py
            end
            s = s + 1
        end
        r = r + 256.0
    end
    return nil, nil
end

-- "Shallow water under the builder": find an existing idle/harvesting worker that already
-- stands next to buildable open water and return (worker, spotX, spotY). Catches coastlines
-- the capital-ring scan misses (island expansions, coastal goldmines) with no long trek.
-- Stops at the first qualifying worker; bounded worker count keeps the per-tick cost low.
local function AiNavalOpportunistic(pi)
    local checked = 0
    local function scan(grp, idleOnly)
        if grp == nil then return nil end
        local sz = BlzGroupGetSize(grp)
        for i = 0, sz - 1 do
            local u = BlzGroupUnitAt(grp, i)
            if u ~= nil and GetUnitState(u, UNIT_STATE_LIFE) > 0.405
               and (not idleOnly or GetUnitCurrentOrder(u) == 0) then
                checked = checked + 1
                local sx, sy = AiNavalSpotNear(GetUnitX(u), GetUnitY(u), 768.0)
                if sx ~= nil then return u, sx, sy end
                if checked >= 12 then return nil end
            end
        end
        return nil
    end
    local u, sx, sy = scan(udg_Ai_harvest[pi], false)
    if u ~= nil then return u, sx, sy end
    u, sx, sy = scan(udg_Ai_builders[pi], false)
    if u ~= nil then return u, sx, sy end
    return scan(udg_Ai_buildersT[pi], true)
end

function BrainNavalDecision(pi, wm, race)
    local shipType = race.wall
    -- R8b: race.wall is a defensive tower for some races (Forsaken h0JM, etc.),
    -- not a shipyard. Fall back to race.shipyard if set.
    if shipType == nil or not AiTransportTypes[shipType] then
        shipType = race.shipyard
    end
    if shipType == nil or not AiTransportTypes[shipType] then return end
    if AiCountBuildingsOfType(pi, shipType) >= AiScaled(AiBrainMaxPorts) then return end

    local now = AiBrainTickCounter or 0

    -- PASS A: opportunistic "shallow water under the builder" — build at a worker already
    -- standing on the coast (no trek, distributes shipyards along the whole shoreline).
    local ow, osx, osy = AiNavalOpportunistic(pi)
    if ow ~= nil then
        local key = pi .. ",nav," .. R2I(osx) .. "," .. R2I(osy)
        local resAt = g_BuildSpotReserved[key]
        if resAt == nil or (now - resAt) >= g_BuildReserveTicks then
            TryBuild_u = ow
            if TryBuildWithType(shipType, osx, osy) then
                g_BuildSpotReserved[key] = now
                AiNavalBuildUntil[ow] = now + AiNavalBuildGrace
                BrainLogEvery(pi, "brainnavy", 30, "shipyard under builder", "BRAINNAVY")
                return
            end
        end
    end

    -- PASS B: capital-ring spots (a free worker walks to the nearest open-water spot).
    local cx, cy = wm.capX, wm.capY
    if cx == nil then return end
    local spots = AiFindNavalSpots(pi, cx, cy)
    if #spots == 0 then return end
    local worker = AiFindFreeWorker(pi)
    if worker == nil then return end
    -- Pick the nearest spot not recently committed (reservation prevents piling every
    -- shipyard on the same point before the first finishes).
    for _, sp in ipairs(spots) do
        local key = pi .. ",nav," .. R2I(sp.x) .. "," .. R2I(sp.y)
        local resAt = g_BuildSpotReserved[key]
        if resAt == nil or (now - resAt) >= g_BuildReserveTicks then
            TryBuild_u = worker
            -- Only reserve + return when the order actually ISSUES. Previously we
            -- returned after the first unreserved spot even if TryBuild failed, so one
            -- bad spot blocked all others for that whole naval tick.
            if TryBuildWithType(shipType, sp.x, sp.y) then
                g_BuildSpotReserved[key] = now
                AiNavalBuildUntil[worker] = now + AiNavalBuildGrace
                BrainLogEvery(pi, "brainnavy", 30, "shipyard at open water", "BRAINNAVY")
                return
            end
        end
    end
end

-- ====================================================================
-- R13: tier-up buildings from strategData.steps (techUp). Upgrades town halls,
-- hives, etc. so tier2 production buildings unlock. Called every brain tick.
-- ====================================================================
---@param pi integer
---@param p player
---@param race table
---@param wm table
-- Self-merge cast (Cult "Плотеобработка"/MeatDeal etc.): the race's signature mechanic that
-- COLLAPSES a cluster of the bot's own small units into one bigger unit. Data-driven via
-- race.mergeCast = { ability, caster, order, consumeAbil, range, minCluster, chance }. A free
-- caster unit (type `caster`, owning ability `ability`) point-casts `order` at the centroid of
-- a cluster of >= minCluster friendly units carrying `consumeAbil`, within `range`. Gated by a
-- small per-call chance + run every few ticks so it merges occasionally, as intended.
---@param pi integer
---@param wm table
---@param race table
function BrainMergeTick(pi, wm, race)
    local mc = race.mergeCast
    if mc == nil then return end
    if GetRandomInt(1, 100) > (mc.chance or 8) then return end
    local army = udg_Ai_army[pi]
    if army == nil then return end
    local sz = BlzGroupGetSize(army)
    local caster = nil
    for i = 0, sz - 1 do
        local u = BlzGroupUnitAt(army, i)
        if u ~= nil and GetUnitTypeId(u) == mc.caster
           and GetUnitState(u, UNIT_STATE_LIFE) > 0.405
           and GetUnitAbilityLevel(u, mc.ability) > 0
           and GetUnitCurrentOrder(u) == 0 then
            caster = u; break
        end
    end
    if caster == nil then return end
    local cx, cy = GetUnitX(caster), GetUnitY(caster)
    local g = CreateGroup()
    GroupEnumUnitsInRange(g, cx, cy, mc.range or 700.0, nil)
    local gs = BlzGroupGetSize(g)
    local n, sxc, syc = 0, 0.0, 0.0
    local pl = Player(pi)
    for i = 0, gs - 1 do
        local u = BlzGroupUnitAt(g, i)
        if u ~= nil and GetOwningPlayer(u) == pl
           and GetUnitState(u, UNIT_STATE_LIFE) > 0.405
           and GetUnitAbilityLevel(u, mc.consumeAbil) > 0 then
            n = n + 1; sxc = sxc + GetUnitX(u); syc = syc + GetUnitY(u)
        end
    end
    DestroyGroup(g)
    if n >= (mc.minCluster or 5) then
        IssuePointOrder(caster, mc.order or "channel", sxc / n, syc / n)
    end
end

function BrainStrategTick(pi, p, race, wm)
    local steps = race.strategData.steps
    if not steps then return end
    for _, step in ipairs(steps) do
        if step.action == "research" then
            -- Military "grades" (weapon/armor/tools/etc.) declared in strategData. The brain
            -- previously handled ONLY techUp, so every "research" step was silently skipped and
            -- grades stuck at 0 for most races (live: FelOrc/KulTiras/Worgen/Dragons/ForestTrolls
            -- grades pinned at 0.0). Each row is {hostBuilding, researchId, levelCap}.
            -- MakeGradeCheckCap researches it at the host building, or (AI bots only) grants it
            -- directly when the race owns no such building — the same path the legacy
            -- AiRunStrateg used. Throttled so it doesn't re-issue every single tick.
            if step.at and wm.tick > step.at and step.rows and (wm.tick % 4) == 0 then
                for _, row in ipairs(step.rows) do
                    MakeGradeCheckCap(p, row[1], row[2], row[3])
                end
            end
            goto nextStep
        end
        if step.action ~= "techUp" then goto nextStep end
        if not step.at or wm.tick <= step.at then goto nextStep end
        if step.gate then
            local g = race.gates and race.gates[step.gate]
            if g and not g(pi) then goto nextStep end
        end
        local cap = step.cap or 3
        if getAiCount(pi, step.to) >= cap then goto nextStep end
        -- Find a building of type step.from and upgrade it
        local grp = udg_Ai_buildings[pi]
        if not grp then goto nextStep end
        local sz = BlzGroupGetSize(grp)
        for i = 0, sz - 1 do
            local u = BlzGroupUnitAt(grp, i)
            if u ~= nil and GetUnitTypeId(u) == step.from
                and GetUnitState(u, UNIT_STATE_LIFE) > 0.405 then
                IssueImmediateOrderById(u, step.to)
                break  -- one upgrade per tick
            end
        end
        ::nextStep::
    end
end

--- Deterministic TryBuild variant: place a specific building type at a forced spot
--- or via AiFindBuildSpot. Returns true if a build order was issued, false if no spot.
---@param bldType integer
---@param fx real|nil
---@param fy real|nil
---@return boolean
function TryBuildWithType(bldType, fx, fy)
    local u = TryBuild_u
    if u == nil or bldType == nil then return false end
    local pi = GetPlayerId(GetOwningPlayer(u))

    GroupAddUnit(udg_Ai_buildersT[pi], u)
    GroupRemoveUnit(udg_Ai_builders[pi], u)
    GroupRemoveUnit(udg_Ai_harvest[pi], u)
    AiBuildClaim[u] = AiBrainTickCounter or 0
    local now = AiBrainTickCounter or 0

    local function reserve(x, y)
        local key = pi .. "," .. R2I(x) .. "," .. R2I(y)
        g_BuildSpotReserved[key] = now
    end

    if fx ~= nil and fy ~= nil then
        reserve(fx, fy)
        IssueBuildOrderById(u, bldType, fx, fy)
        return true
    end

    if AiSmartBuild then
        local bx, by = AiFindBuildSpot(pi, u)
        if bx ~= nil then
            reserve(bx, by)
            IssueBuildOrderById(u, bldType, bx, by)
            return true
        end
    end
    -- Random fallback: try a few rings, but only commit to a footprint-clear spot.
    local ux0, uy0 = GetUnitX(u), GetUnitY(u)
    for _ = 1, 8 do
        local ang = GetRandomReal(0, 360) * bj_DEGTORAD
        local ux = ux0 + AiBuildingRadius * Cos(ang)
        local uy = uy0 + AiBuildingRadius * Sin(ang)
        if AiBuildPlaceable(ux, uy) then
            reserve(ux, uy)
            IssueBuildOrderById(u, bldType, ux, uy)
            return true
        end
    end
    -- R17: if no placeable spot found, return worker to harvest immediately
    -- instead of stranding them at an unplaceable last-resort spot.
    GroupAddUnit(udg_Ai_harvest[pi], u)
    GroupRemoveUnit(udg_Ai_buildersT[pi], u)
    AiBuildClaim[u] = nil
    IssueImmediateOrder(u, "autoharvestlumber")
end

-- ====================================================================
-- BrainFocus: pick best objective, order idle army units there.
-- Uses local udg_Ai_army[pi] group — no GroupEnumUnitsOfPlayer.
-- ====================================================================

---@param pi integer
---@param p player
---@param wm table
---@return integer
function BrainFocus(pi, p, wm)
    local focus = AiBrainPickFocus(pi, wm)
    -- DYNAMIC DEFENSE: under home siege, override the offensive focus and recall the whole
    -- army to the capital to engage attackers. The FSM's defend/retreat states are dormant
    -- (AiSquadFsmEnabled=false), so without this the live single-front bot kept marching off
    -- on offense while an enemy razed its undefended capital (live bug). A capital-centred
    -- pseudo-focus makes targetFor() attack-move every unit home (same-continent => "attack").
    if wm.defendHome and wm.capX ~= nil then
        focus = { x = wm.capX, y = wm.capY, kind = "defend", key = "DEFEND" }
    end
    if focus == nil then return 0 end

    -- BrainFocus is the LIVE army-command path (the AiSquadTick* FSM with portal routing is
    -- never dispatched). The army is a SINGLE front (one objective), but each unit's order
    -- depends on ITS OWN continent, NOT the army centroid: a unit already on the objective
    -- continent attacks the objective; a unit still behind a portal MOVES onto the waygate
    -- toward it. Centroid routing told units that had ALREADY crossed to walk back to the
    -- origin-side portal — the "orc reached Pandaria but his units run back to Kalimdor" bug.
    local oc = AiContinentOf(focus.x, focus.y)

    -- Kick the TP machinery if a port-mage already sits on the objective continent.
    if oc ~= nil then
        local sc = wm.cx and AiContinentOf(wm.cx, wm.cy)
        if sc ~= nil and sc ~= oc then
            local m = AiFindMageOnContinent(pi, oc)
            if m ~= nil then gPi = pi; gPlayer = p; PortTo(m) end
        end
    end

    -- Memoize (continent -> {x,y,order}) so AiContinentOf is the only per-unit cost. MOVE
    -- (not attack) onto a waygate so units step through instead of stopping to fight near it.
    local destCache = {}
    local function targetFor(ux, uy)
        local uc = AiContinentOf(ux, uy)
        if uc == nil or oc == nil or uc == oc then return focus.x, focus.y, "attack" end
        local c = destCache[uc]
        if c ~= nil then return c.x, c.y, c.ord end
        -- Cross-continent: route to a PORTAL, never attack-move straight at the off-continent
        -- objective (that walks the army into the sea / strands it — the live "goes south
        -- instead of the portal" bug). Try a waygate hop first, then the WEB (sell) portal
        -- network (most continent links are n003 web portals, so AiFindPortal returns nil and
        -- we MUST fall back to web). If neither exists, return nil order = hold (naval desant
        -- handles ocean-separated targets; the scorer already buries portal-unreachable ones).
        local rx, ry, ro = nil, nil, nil
        local rt = AiPortalRoute(uc, oc)
        if rt ~= nil and #rt >= 2 then
            local portal = AiFindPortal(rt[1], rt[2])
            if portal ~= nil then rx, ry, ro = GetUnitX(portal), GetUnitY(portal), "move" end
        end
        if ro == nil then
            local wrt = AiWebRoute(uc, oc)
            if wrt ~= nil and #wrt >= 2 then
                local wp = AiFindWebPortal(wrt[1], wrt[2], ux, uy)
                if wp ~= nil then rx, ry, ro = wp.x, wp.y, "move" end
            end
        end
        destCache[uc] = { x = rx, y = ry, ord = ro }
        return rx, ry, ro
    end

    local cnt = 0
    local function orderIdle(u)
        local tx, ty, ord = targetFor(GetUnitX(u), GetUnitY(u))
        if ord == nil then return end   -- cross-water, no portal route: hold (don't swim)
        IssuePointOrder(u, ord, tx, ty)
        cnt = cnt + 1
    end

    local army = udg_Ai_army[pi]
    if army ~= nil then
        local armySz = BlzGroupGetSize(army)
        for i = 0, armySz - 1 do
            local u = BlzGroupUnitAt(army, i)
            if u ~= nil and GetUnitState(u, UNIT_STATE_LIFE) > 0.405 then
                local o = GetUnitCurrentOrder(u)
                if o == 0 or o == 851972 or o == 851976 then orderIdle(u) end
            end
        end
    end

    -- R6: races with workerFighter (Undead ghouls) — pull idle harvest workers into combat
    local race = AiRaceOf(pi)
    if race and race.workerFighter then
        local wfId = race.workerFighter
        local grpH = udg_Ai_harvest[pi]
        if grpH ~= nil then
            local szH = BlzGroupGetSize(grpH)
            for j = 0, szH - 1 do
                local u = BlzGroupUnitAt(grpH, j)
                if u ~= nil and GetUnitTypeId(u) == wfId
                    and GetUnitState(u, UNIT_STATE_LIFE) > 0.405
                    and GetUnitCurrentOrder(u) == 0 then orderIdle(u) end
            end
        end
    end
    return cnt
end

-- ====================================================================
-- BrainWebPortalTick: mass-teleport a BIG gathered army across continents via the
-- sell-portal network instead of trickling it through a walk-on waygate (which a
-- large blob collision-jams on — observed 173-unit Horde army stuck @ Dark Portal,
-- 0 crossings). BrainFocus already MOVES cross-continent units onto the co-located
-- waygate, so they gather at the web-portal naturally; once enough are within its
-- teleport radius we fire AiPortalTeleport (own-army only). See [[portal-sell-teleport]].
-- ====================================================================
AiWebTpEnabled    = (AiWebTpEnabled == nil) and true or AiWebTpEnabled
AiWebMinArmy      = AiWebMinArmy      or 16   -- only mass-TP armies this big (small ones just walk)
AiWebGatherFrac   = AiWebGatherFrac   or 0.40 -- fire once this fraction of the army is at the portal
AiWebMinGathered  = AiWebMinGathered  or 10   -- ...but never fewer than this many units
AiWebCooldownTicks = AiWebCooldownTicks or 16 -- per-portal cooldown (lets stragglers re-gather)

---@param pi integer
---@param p player
---@param wm table
function BrainWebPortalTick(pi, p, wm)
    if not AiWebTpEnabled then return end
    if wm == nil or wm.defendHome then return end   -- under home siege: stay and defend
    local army = udg_Ai_army[pi]
    if army == nil then return end

    -- Where do we want to go? The current single-front objective.
    local focus = AiBrainPickFocus(pi, wm)
    if focus == nil then return end
    local oc = AiContinentOf(focus.x, focus.y)
    if oc == nil then return end

    -- Bucket the army's military units by the continent/zone they're standing on. A split
    -- army (e.g. half stranded in a dungeon, half on the mainland) gets each cluster handled
    -- on its own, so a group trapped behind a jammy walk-on waygate is teleported out toward
    -- the objective hop by hop.
    local sz = BlzGroupGetSize(army)
    local buckets = {}   -- cont -> {n, sumx, sumy}
    local mil = 0
    for i = 0, sz - 1 do
        local u = BlzGroupUnitAt(army, i)
        if u ~= nil and GetUnitState(u, UNIT_STATE_LIFE) > 0.405
           and not IsUnitType(u, UNIT_TYPE_STRUCTURE) and not IsUnitType(u, UNIT_TYPE_PEON) then
            local ux, uy = GetUnitX(u), GetUnitY(u)
            local c = AiContinentOf(ux, uy)
            if c ~= nil then
                local b = buckets[c]
                if b == nil then b = { n = 0, sx = 0.0, sy = 0.0 }; buckets[c] = b end
                b.n = b.n + 1; b.sx = b.sx + ux; b.sy = b.sy + uy
                mil = mil + 1
            end
        end
    end
    if mil < AiWebMinArmy then return end            -- small army: walk-on is fine

    local now = AiBrainTickCounter or 0
    -- Consider the biggest off-objective cluster first (most units to unstick).
    local bestCont, bestN
    for c, b in pairs(buckets) do
        if c ~= oc and (bestN == nil or b.n > bestN) then bestCont, bestN = c, b.n end
    end
    if bestCont == nil then return end               -- everyone already on the objective continent
    local b = buckets[bestCont]
    if b.n < AiWebMinGathered then return end        -- too few here to bother mass-TPing
    local cx, cy = b.sx / b.n, b.sy / b.n

    -- Route this cluster toward the objective over the WEB network so the next hop always
    -- has a real portal; pick the nearest such portal to the cluster centroid.
    local rt = AiWebRoute(bestCont, oc)
    local nextCont = (rt ~= nil and #rt >= 2) and rt[2] or oc
    local wp = AiFindWebPortal(bestCont, nextCont, cx, cy)
    if wp == nil then return end

    -- Per-portal cooldown so we don't re-TP the same trickle every tick.
    local key = tostring(wp.unit)
    local last = AiWebPortalCast[key]
    if last ~= nil and (now - last) < AiWebCooldownTicks then return end

    -- Only fire once a real chunk of this cluster has gathered within the portal's radius.
    local need = math.max(AiWebMinGathered, math.ceil(b.n * AiWebGatherFrac))
    local within, r2 = 0, wp.radius * wp.radius
    for i = 0, sz - 1 do
        local u = BlzGroupUnitAt(army, i)
        if u ~= nil and GetUnitState(u, UNIT_STATE_LIFE) > 0.405
           and not IsUnitType(u, UNIT_TYPE_STRUCTURE) and not IsUnitType(u, UNIT_TYPE_PEON) then
            local dx, dy = GetUnitX(u) - wp.x, GetUnitY(u) - wp.y
            if dx * dx + dy * dy <= r2 then within = within + 1 end
        end
    end
    if within < need then return end                 -- still gathering; BrainFocus keeps herding them

    -- Never ship the home garrison off on an offensive teleport — collect the defense
    -- squad(s) as a skip-set so the capital keeps its guard (live: a bot mass-TP'd its
    -- whole army incl. the defense squad across a continent, leaving the capital naked).
    local garrison = nil
    for _, sq in pairs(AiSquadsOf(pi)) do
        if sq.role == "defense" and sq.members ~= nil then
            local gsz = BlzGroupGetSize(sq.members)
            for gi = 0, gsz - 1 do
                local gu = BlzGroupUnitAt(sq.members, gi)
                if gu ~= nil then garrison = garrison or {}; garrison[gu] = true end
            end
        end
    end

    local moved = AiPortalTeleport(pi, wp.unit, wp.rect, wp.radius, garrison)
    AiWebPortalCast[key] = now
    if moved > 0 then
        BrainLogTag(pi, "BRAINWEB", "mass-TP " .. tostring(moved) .. " units "
            .. tostring(bestCont) .. " -> " .. tostring(wp.dstCont) .. " (obj " .. tostring(oc) .. ")")
    end
end

-- ====================================================================
-- BrainNavalFocus: iterate udg_Ai_navy[pi] (local group, no enum), send
-- idle naval units via TryAttackN. Replaces PlayerNavy + TimerSmall4.
-- ====================================================================

---@param pi integer
---@param p player
---@return integer
function BrainNavalFocus(pi, p)
    local navy = udg_Ai_navy[pi]
    if navy == nil then return 0 end
    local sz = BlzGroupGetSize(navy)
    if sz == 0 then return 0 end

    local processed = 0
    local maxN = AiBrainMaxProduce -- reuse the same cap, or dedicated naval cap

    for i = 0, sz - 1 do
        if processed >= maxN then break end
        local u = BlzGroupUnitAt(navy, i)
        if u ~= nil and GetUnitState(u, UNIT_STATE_LIFE) > 0.405 then
            if not AiTransportSet[GetUnitTypeId(u)] then  -- transports handled by BrainLandingTick
                local o = GetUnitCurrentOrder(u)
                if o == 0 or o == 851972 or o == 851976 then
                    CheckPlayer = p
                    udg_LocalUnit3 = u
                    TryAttackN()
                    processed = processed + 1
                end
            end
        end
    end
    return processed
end

-- ====================================================================
-- R10: Amphibious landing (десант). Load idle army onto transports, sail to
-- enemy shore, unload. Transports are detected by unit type (AiTransportSet).
-- ====================================================================

-- Pick a landing target: enemy objective that's water-separated from capital.
---@param pi integer
---@param wm table
---@return table|nil  {x, y, name}
function AiBrainPickLandingTarget(pi, wm)
    local objs = wm.objectives
    if objs == nil or #objs == 0 then return nil end
    local cx, cy = wm.capX, wm.capY
    if cx == nil then return nil end

    -- Desant only makes sense FROM an ocean-bordering home TO a DIFFERENT ocean-bordering
    -- continent (both on the single great ocean). Same-continent targets are walked to; and
    -- dimensions/dungeons (no naval spots, void-walled — e.g. Argus, Outland) are portal-only,
    -- so a transport must never be sent at them. Without this gate the old code picked the
    -- farthest enemy regardless of water and sailed straight at its inland tile, stalling.
    local homeCont = AiContinentOf(cx, cy)
    if not AiContinentOceanBordering(homeCont) then return nil end

    -- Prefer distant enemy capitals/cities on a reachable continent.
    local best, bestScore, bestCont = nil, -1, nil
    for _, obj in ipairs(objs) do
        local objCont = AiContinentOf(obj.x, obj.y)
        if objCont ~= nil and objCont ~= homeCont and AiContinentOceanBordering(objCont) then
            local dx = obj.x - cx
            local dy = obj.y - cy
            local d = dx * dx + dy * dy
            local sc = d
            if obj.kind == "capital" then sc = sc * 3
            elseif obj.kind == "city" then sc = sc * 2
            end
            if d > 3000 * 3000 and sc > bestScore then
                bestScore = sc; best = obj; bestCont = objCont
            end
        end
    end
    if best == nil then return nil end

    -- Sail to the open-water spot nearest the target's coast, NOT the inland objective —
    -- transports can't path onto land, so an unloadall near the shore is what lands troops.
    local sx, sy = AiNearestNavalSpot(bestCont, best.x, best.y)
    if sx == nil then return nil end
    return { x = best.x, y = best.y, name = best.name, sailX = sx, sailY = sy, continent = bestCont }
end

-- Count loaded units on a transport (units with the transport as their current order target).
-- WC3 doesn't expose cargo count, so we approximate: if transport is moving/has "load" order
-- from nearby units, it's busy. We track by AI-side state table.
AiLandingState = AiLandingState or {}  -- [unit] = { phase, targetX, targetY }

---@param pi integer
---@param p player
---@param wm table
---@return integer
-- wm.ticks the transport HOLDS at the embark spot for the army to walk over and board
-- before it sails to the target. (Landing runs every AiBrainLandingEvery wm.ticks.)
AiLandingLoadDwell = AiLandingLoadDwell or 2

function BrainLandingTick(pi, p, wm)
    if wm.tick < AiBrainNavalStartTick then return 0 end  -- no ports yet
    local race = AiRaceOf(pi)
    if race and (race.key == "Naga" or race.key == "naga") then return 0 end  -- Naga skip

    local army = udg_Ai_army[pi]
    local navy = udg_Ai_navy[pi]
    if navy == nil then return 0 end
    local sz = BlzGroupGetSize(navy)
    if sz == 0 then return 0 end

    local target = AiBrainPickLandingTarget(pi, wm)
    if target == nil then return 0 end
    local tx, ty = target.sailX, target.sailY   -- near-shore UNLOAD point by the enemy coast

    -- Embark spot: open water beside the army's OWN coast. Phased flow per transport:
    -- sail to embark FIRST -> arrive & hold -> THEN order army to "load" (they walk over and
    -- board) -> sail to the target's unload point -> unloadall. Sailing before loading avoids
    -- the moving ship pulling boarders around. Dwell is counted in wm.ticks (deterministic).
    local homeCont = (wm.capX and AiContinentOf(wm.capX, wm.capY)) or (wm.cx and AiContinentOf(wm.cx, wm.cy))
    local ex, ey = AiNearestNavalSpot(homeCont, wm.cx or wm.capX, wm.cy or wm.capY)
    if ex == nil then ex, ey = wm.cx or wm.capX, wm.cy or wm.capY end

    local R2 = AiBrainLandingRadius * AiBrainLandingRadius
    local now = wm.tick
    local processed = 0
    local maxN = AiBrainLandingMaxTransports

    for i = 0, sz - 1 do
        if processed >= maxN then break end
        local u = BlzGroupUnitAt(navy, i)
        if u == nil then goto nextShip end
        if GetUnitState(u, UNIT_STATE_LIFE) <= 0.405 then goto nextShip end
        if not AiTransportSet[GetUnitTypeId(u)] then goto nextShip end  -- combat ship, skip

        local order = GetUnitCurrentOrder(u)
        local st = AiLandingState[u]
        local ux, uy = GetUnitX(u), GetUnitY(u)

        if st ~= nil and st.phase == "loaded" then
            local dx, dy = ux - tx, uy - ty
            if dx * dx + dy * dy < R2 then
                IssueImmediateOrder(u, "unloadall")
                AiLandingState[u] = { phase = "done", t = now }
            elseif order == 0 or order == 851972 then
                IssuePointOrder(u, "move", tx, ty)
            end
            processed = processed + 1
        elseif st ~= nil and st.phase == "loading" then
            -- holding at the embark spot: order nearest army units to board (they walk over)
            local k = 0
            if army ~= nil then
                local asz = BlzGroupGetSize(army)
                for j = 0, asz - 1 do
                    if k >= 6 then break end
                    local a = BlzGroupUnitAt(army, j)
                    if a ~= nil and GetUnitState(a, UNIT_STATE_LIFE) > 0.405
                       and not IsUnitType(a, UNIT_TYPE_HERO) then
                        IssueTargetOrder(a, "load", u)
                        k = k + 1
                    end
                end
            end
            if (now - (st.t or now)) >= AiLandingLoadDwell then
                AiLandingState[u] = { phase = "loaded", t = now }
                IssuePointOrder(u, "move", tx, ty)
                BrainLogTag(pi, "LAND", "loaded -> sail (" .. tostring(R2I(tx)) .. "," .. tostring(R2I(ty)) .. ")")
            end
            processed = processed + 1
        elseif st == nil or st.phase == "toEmbark" then
            local dx, dy = ux - ex, uy - ey
            if dx * dx + dy * dy < R2 then
                IssueImmediateOrder(u, "stop")           -- arrived & hold; load starts next tick
                AiLandingState[u] = { phase = "loading", t = now }
            else
                if st == nil or order == 0 then IssuePointOrder(u, "move", ex, ey) end
                AiLandingState[u] = { phase = "toEmbark", t = now }
            end
            processed = processed + 1
        elseif st ~= nil and st.phase == "done" and order == 0 then
            if wm.capX ~= nil then
                IssuePointOrder(u, "move", wm.capX, wm.capY)
                AiLandingState[u] = { phase = "returning", t = now }
            end
        end
        ::nextShip::
    end
    return processed
end

-- Entry point when a bot has an active brain ("objective"). Perceive → refresh
-- objectives on schedule → pick a focus (force concentration) → order idle army
-- there. Falls back to swarm when there are no objectives.
---@param pi integer
---@param p player
-- R4: race-data validator. Runs once per race (first time a bot of that race ticks).
-- Logs structural problems under tag BRAINVALID so the systemic race-fragility
-- (most races economically stuck) becomes visible data instead of a silent stall.
-- Never throws (called inside pcall); never blocks the bot.
---@param rk string
function AiValidateRace(rk)
    local race = AiRaces and AiRaces[rk]
    if race == nil then
        BrainLogTag(0, "BRAINVALID", "race '" .. tostring(rk) .. "' has NO def")
        return
    end
    local problems = {}

    -- Worker production: needed to ever build/expand.
    local prod = race.production
    if prod == nil then
        problems[#problems + 1] = "no .production table"
    else
        local w = prod.worker
        if w == nil then
            problems[#problems + 1] = "no production.worker"
        else
            if w.id == nil then problems[#problems + 1] = "worker.id nil" end
            if w.from == nil or #w.from == 0 then
                problems[#problems + 1] = "worker.from empty (cannot train workers)"
            end
        end
    end

    -- Buildings: build order must reference numeric type ids.
    local blds = race.buildings
    if blds == nil then
        problems[#problems + 1] = "no .buildings table"
    else
        if blds.seed ~= nil and type(blds.seed) ~= "number" then
            problems[#problems + 1] = "buildings.seed not a number"
        end
        local n = 0
        for _, row in ipairs(blds) do
            n = n + 1
            if type(row[1]) ~= "number" then
                problems[#problems + 1] = "buildings[" .. n .. "][1] not a number"
            end
        end
        if n == 0 and blds.seed == nil then
            problems[#problems + 1] = "buildings list empty"
        end
    end

    -- compTarget: every targeted unit should have a producer building, else its
    -- order silently no-ops and the army never reaches target composition.
    local comp = race.compTarget
    if comp ~= nil and prod ~= nil then
        for unitId, _ in pairs(comp) do
            if type(unitId) == "number" then
                local found = false
                for bldType, rows in pairs(prod) do
                    if bldType ~= "worker" and type(rows) == "table" then
                        for _, row in ipairs(rows) do
                            if row[1] == unitId
                                or (row.branch and (row.black == unitId or row.other == unitId)) then
                                found = true; break
                            end
                        end
                    end
                    if found then break end
                end
                if not found then
                    problems[#problems + 1] = "compTarget unit " .. tostring(unitId)
                        .. " has no producer building"
                end
            end
        end
    end

    if #problems == 0 then
        BrainLogTag(0, "BRAINVALID", "race '" .. rk .. "' OK")
    else
        BrainLogTag(0, "BRAINVALID", "race '" .. rk .. "' problems: "
            .. table.concat(problems, "; "))
    end
end

-- ====================================================================
-- BrainCaptureSquad: dedicated same-continent neutral-capture detail.
--
-- Problem this solves: BrainFocus picks the single highest-scoring objective
-- and sends the whole army there. Enemy capitals outscore neutral capture
-- points (kindBase), so a bot will ignore an uncaptured neutral building
-- *sitting on its own continent* and march everyone off to attack an enemy.
-- The user observed bots leaving their home continent half-uncaptured.
--
-- Fix: every few ticks, peel off a fixed fraction of the army and send it to
-- the nearest uncaptured neutral ZahvatBuilding that is on the bot's OWN
-- continent (AiContinentOf match). Units are chosen by group index so the
-- same detail stays on capture duty across ticks (no random thrash). This
-- runs AFTER BrainFocus, so it overrides the focus order for that subset only.
-- ====================================================================
AiCaptureSquadFrac    = AiCaptureSquadFrac    or 0.35   -- fraction of army for capture
AiCaptureSquadMin     = AiCaptureSquadMin     or 4      -- but at least this many...
AiCaptureSquadArmyMin = AiCaptureSquadArmyMin or 8      -- ...only if army >= this
AiCaptureSquadEvery   = AiCaptureSquadEvery   or 3      -- run every N army ticks
AiCaptureSquadDisableArmy = AiCaptureSquadDisableArmy or 35 -- once army >= this, STOP peeling
                                                            -- units to neutrals: a strong bot must
                                                            -- concentrate its whole force on enemy
                                                            -- capitals (else captures starve the
                                                            -- assault and nobody gets eliminated).

-- Find nearest uncaptured neutral ZahvatBuilding on the bot's own continent.
---@param pi integer
---@param wm table
---@return real|nil, real|nil
function AiFindOwnContinentNeutral(pi, wm)
    local g = udg_ZahvatBuildings
    if g == nil or wm.cx == nil then return nil, nil end
    local me = Player(pi)
    local capCont = AiContinentOf(wm.cx, wm.cy)
    if capCont == nil then return nil, nil end
    local bestX, bestY, bestD = nil, nil, 1e30
    local n = BlzGroupGetSize(g)
    local i = 0
    while i < n do
        local u = BlzGroupUnitAt(g, i)
        i = i + 1
        if u ~= nil and GetUnitState(u, UNIT_STATE_LIFE) > 0.405 then
            local owner = GetOwningPlayer(u)
            -- still neutral / not ours and not an ally's
            if owner ~= me and not IsPlayerAlly(owner, me) then
                local x, y = GetUnitX(u), GetUnitY(u)
                if AiContinentOf(x, y) == capCont then
                    local dx, dy = wm.cx - x, wm.cy - y
                    local d = dx * dx + dy * dy
                    if d < bestD then bestD = d; bestX = x; bestY = y end
                end
            end
        end
    end
    return bestX, bestY
end

---@param pi integer
---@param p player
---@param wm table
---@return integer ordered count
function BrainCaptureSquad(pi, p, wm)
    if (wm.tick % AiCaptureSquadEvery) ~= 0 then return 0 end
    local army = udg_Ai_army[pi]
    if army == nil then return 0 end
    local armySz = BlzGroupGetSize(army)
    if armySz < AiCaptureSquadArmyMin then return 0 end
    -- Strong army: stand down the capture detail so the FULL force concentrates on
    -- enemy capitals via BrainFocus. Without this, 35% kept peeling to neutrals and
    -- assaults never had the mass to break a 10000-HP capital (eliminations stalled).
    if armySz >= AiCaptureSquadDisableArmy then return 0 end

    local tx, ty = AiFindOwnContinentNeutral(pi, wm)
    if tx == nil then return 0 end

    local want = R2I(armySz * AiCaptureSquadFrac)
    if want < AiCaptureSquadMin then want = AiCaptureSquadMin end

    if gSubGroup == nil then gSubGroup = CreateGroup() end
    GroupClear(gSubGroup)
    local cnt, ordered = 0, 0
    local i = 0
    while i < armySz and ordered < want do
        local u = BlzGroupUnitAt(army, i)
        i = i + 1
        if u ~= nil and GetUnitState(u, UNIT_STATE_LIFE) > 0.405
            and not IsUnitType(u, UNIT_TYPE_PEON)
            and not IsUnitType(u, UNIT_TYPE_STRUCTURE) then
            GroupAddUnit(gSubGroup, u)
            cnt = cnt + 1
            ordered = ordered + 1
            if cnt >= 12 then
                GroupPointOrder(gSubGroup, "attack", tx, ty)
                GroupClear(gSubGroup)
                cnt = 0
            end
        end
    end
    if cnt > 0 then
        GroupPointOrder(gSubGroup, "attack", tx, ty)
        GroupClear(gSubGroup)
    end
    if ordered > 0 then
        BrainLogEvery(pi, "capsquad", 4, "capture detail n=" .. tostring(ordered)
            .. " -> own-continent neutral (" .. tostring(R2I(tx)) .. ","
            .. tostring(R2I(ty)) .. ")", "BRAINCAP")
    end
    return ordered
end

-- R1/R2/R3: protected wrapper. A Lua error in one bot's tick is caught, counted,
-- and (past AiBotFaultLimit) quarantines that bot for a while — the round-robin and
-- every other bot keep running. NOTE: a hard C++ crash (e.g. the old squad FSM) is
-- NOT catchable here; this guards the far more common Lua-level errors that race-data
-- fragility produces. See AI_OVERHAUL_PLAN.md §2 (Track R).
function AiBrainArmyTick(pi, p)
    -- Quarantine: skip a repeatedly-faulting bot for a window, then retry.
    local qUntil = AiBotQuarantine[pi]
    if qUntil ~= nil then
        if AiBrainTickCounter ~= nil and AiBrainTickCounter < qUntil then return end
        AiBotQuarantine[pi] = nil  -- window elapsed, give it another chance
    end
    local ok, err = pcall(AiBrainArmyTickInner, pi, p)
    if not ok then
        AiBotFaults[pi] = (AiBotFaults[pi] or 0) + 1
        AiBrainLogTagSafe(pi, "BRAINERR", "tick fault #" .. tostring(AiBotFaults[pi])
            .. " pi=" .. tostring(pi) .. " err=" .. tostring(err))
        if AiBotFaults[pi] >= AiBotFaultLimit then
            AiBotQuarantine[pi] = (AiBrainTickCounter or 0) + AiBotQuarantineTicks
            AiBotFaults[pi] = 0  -- reset the window counter
            AiBrainLogTagSafe(pi, "BRAINERR", "pi=" .. tostring(pi)
                .. " QUARANTINED for " .. tostring(AiBotQuarantineTicks) .. " ticks")
        end
    end
end

-- BRAINERR logging that can't itself throw (used inside the fault handler).
function AiBrainLogTagSafe(pi, tag, msg)
    pcall(function() BrainLogTag(pi, tag, msg) end)
end

function AiBrainArmyTickInner(pi, p)
    AiBrainTickCounter = (AiBrainTickCounter or 0) + 1
    -- R4: validate this bot's race once, log any data problems (does not block).
    local rk = AiRace[pi]
    if rk ~= nil and not AiRaceValidated[rk] then
        AiRaceValidated[rk] = true
        pcall(AiValidateRace, rk)
    end
    local t0 = os.clock and os.clock() or 0
    local d = AiProfileData[pi] or { ticks = 0 }
    AiProfileData[pi] = d
    d.ticks = d.ticks + 1
    local function lap(key)
        if t0 == 0 then return end
        local now = os.clock()
        local ms = (now - t0) * 1000
        d[key] = (d[key] or 0) + ms
        t0 = now
    end

    local wm = AiBrainPerceive(pi)
    local race = AiRaceOf(pi)

    lap("perceive")

    if race ~= nil then
        BrainProduce(pi, wm, race)
        lap("produce")
        BrainBuild(pi, wm, race)
        lap("build")
    end

    local cfg = AiBrainCfg(pi)
    if wm.objectives == nil or (wm.tick % (cfg.clusterEvery or 8)) == 0 then
        AiBrainCollectObjectives(pi, wm)
    end
    if wm.objectives == nil or #wm.objectives == 0 then lap("other"); AiArmyLegacyTick(p); return end

    if wm.defendHome and wm.capX ~= nil then
        for _, sq in pairs(AiSquadsOf(pi)) do
            if sq.role == "assault" and sq.state ~= "retreat" then
                sq.state = "retreat"; sq.rally.x, sq.rally.y = wm.capX, wm.capY
            end
        end
    end

    if (wm.tick % 2) == 0 then
        AiSquadReapDead(pi)
    end
    if (wm.tick % AiRecoverEvery) == 0 then
        AiBrainRecoverStranded(pi, wm)
    end
    lap("reap")

    if (wm.tick % 2) == 0 then
        local armyGroup = udg_Ai_army[pi]
        if armyGroup ~= nil then
            local squads = AiSquadsOf(pi)
            local assignedGroup = CreateGroup()
            for _, sq in pairs(squads) do
                local sz = BlzGroupGetSize(sq.members)
                local j = 0
                while j < sz do
                    local u = BlzGroupUnitAt(sq.members, j)
                    if u ~= nil then GroupAddUnit(assignedGroup, u) end
                    j = j + 1
                end
            end
            local armySz = BlzGroupGetSize(armyGroup)
            local j = 0
            while j < armySz do
                local u = BlzGroupUnitAt(armyGroup, j)
                if u ~= nil and GetUnitState(u, UNIT_STATE_LIFE) > 0.405
                    and not IsUnitType(u, UNIT_TYPE_PEON)
                    and not IsUnitType(u, UNIT_TYPE_STRUCTURE)
                    and not IsUnitInGroup(u, assignedGroup) then
                    AiSquadAssign(pi, u)
                end
                j = j + 1
            end
            DestroyGroup(assignedGroup)
        end
    end
    lap("orphan")

    if (wm.tick % AiFocusEvery) == 1 then
        if AiSquadFsmEnabled then
            AiSquadFsmTick(pi, p, wm)  -- opt-in squad FSM (commands squads instead of single front)
        else
            BrainFocus(pi, p, wm)
        end
    end
    lap("focus")

    BrainCaptureSquad(pi, p, wm)
    lap("capsquad")

    -- Mass-teleport a big gathered army across continents (sell-portal network) instead
    -- of jamming it on a walk-on waygate. Runs in both single-front and FSM modes.
    if (wm.tick % AiFocusEvery) == 0 then
        BrainWebPortalTick(pi, p, wm)
    end
    lap("webtp")

    if (wm.tick % 4) == 0 then
        BrainNavalFocus(pi, p)
    end

    if (wm.tick % AiBrainLandingEvery) == 0 then
        BrainLandingTick(pi, p, wm)
    end

    if (wm.tick % 8) == 0 then AiBuyPirateFleet(pi) end
    if AiDiplomatEnabled and (wm.tick % 4) == 0 then AiDiplomatTick(pi) end
    lap("other")

    if d.ticks % AiProfileEvery == 0 then
        AiBrainLogAppend(AiProfileDump(pi))
    end
end

-- ====================================================================
-- Production track P1: deterministic building placement (vs random ring).
-- Independent of the army brain; opt-in via global AiSmartBuild (default off,
-- random ring stays the fallback). Searches expanding rings/sectors around the
-- capital (or builder) for the nearest placeable, non-crowded spot. Tag BRAINBLD.
-- ====================================================================
AiSmartBuild = AiSmartBuild or true

---@return boolean
function f_AnyStructure()
    local u = GetFilterUnit()
    return u ~= nil and IsUnitType(u, UNIT_TYPE_STRUCTURE) and GetUnitState(u, UNIT_STATE_LIFE) > 0.405
end

---@param x real
---@param y real
---@param radius real
---@return boolean
g_BuildSpotReserved = g_BuildSpotReserved or {}   -- ["pi,x,y"] = tick (spot claimed by worker en route)
g_BuildReserveTicks = g_BuildReserveTicks or 40   -- how long a reservation lives

function AiBuildSpotOccupied(x, y, radius)
    AiBuildScanGroup = AiBuildScanGroup or CreateGroup()
    GroupEnumUnitsInRange(AiBuildScanGroup, x, y, radius, nil)
    local sz = BlzGroupGetSize(AiBuildScanGroup)
    for i = 0, sz - 1 do
        local u = BlzGroupUnitAt(AiBuildScanGroup, i)
        if u ~= nil and IsUnitType(u, UNIT_TYPE_STRUCTURE) and GetUnitState(u, UNIT_STATE_LIFE) > 0.405 then
            return true
        end
    end
    -- Check reserved spots (workers en route)
    local now = AiBrainTickCounter or 0
    for key, t in pairs(g_BuildSpotReserved) do
        if now - t < g_BuildReserveTicks then
            local px, py, pr = key:match("^(%-?%d+),(%-?%d+),(%-?%d+)$")
            if px then
                local dx = x - tonumber(px)
                local dy = y - tonumber(py)
                if dx*dx + dy*dy < radius*radius then return true end
            end
        end
    end
    return false
end

-- IsTerrainPathable is inverted: true == blocked for that pathing type (matches
-- the `not IsTerrainPathable(..WALKABILITY)` idiom used in 98_ai_build.lua).
-- E1: a single-point check passes spots whose full FOOTPRINT collides (water/cliff
-- at a corner) — the engine then silently rejects IssueBuildOrderById and the worker
-- goes idle (observed root cause of the stuck build pipeline). So sample the center
-- plus a ring of points spanning the building footprint; reject if ANY is blocked.
---@param x real
---@param y real
---@param half? real  half-footprint radius to sample (default ~one build cell)
---@return boolean
function AiBuildPlaceable(x, y, half)
    half = half or (AiBuildingRadius and AiBuildingRadius * 0.2) or 192.0
    -- Center must be walkable (rejects cliffs AND deep water — deep water is non-walkable).
    -- SHALLOW water is walkable, so it's now allowed: an island/coastal bot can build on it
    -- (physically valid in this map). Previously we also rejected every floatable tile, which
    -- locked island Silitids out of building their base entirely.
    if IsTerrainPathable(x, y, PATHING_TYPE_WALKABILITY) then return false end
    -- Footprint ring: reject only DEEP water (floatable AND non-walkable). A friendly building
    -- on a corner is non-walkable but NOT floatable (land under it), so it's allowed (dense
    -- base, the reason we don't sample walkability alone). Shallow-water corners (walkable) are
    -- allowed; deep-water corners make the engine silently reject the order, so we catch those.
    local offs = { {half,0},{-half,0},{0,half},{0,-half} }
    for i = 1, 4 do
        local fx, fy = x + offs[i][1], y + offs[i][2]
        if (not IsTerrainPathable(fx, fy, PATHING_TYPE_FLOATABILITY))
            and IsTerrainPathable(fx, fy, PATHING_TYPE_WALKABILITY) then
            return false  -- deep water corner
        end
    end
    return true
end

-- Nearest placeable spot around the player's anchor. Returns x,y or nil,nil.
---@param pi integer
---@param builder unit
---@return real|nil, real|nil
-- Expanding-ring scan around one anchor; returns first placeable, non-crowded spot.
---@param ax real
---@param ay real
---@param rad real
---@param phase integer
---@return real|nil, real|nil
function AiScanBuildRings(ax, ay, rad, phase)
    local minSpacing = AiBuildMinSpacing
    local sectors = 12
    local ring = 0
    while ring < (AiBuildRingCount or 14) do
        local r = AiBuildRingStart + ring * AiBuildRingStep
        local s = 0
        while s < sectors do
            local ang = (I2R(s + phase) / I2R(sectors)) * 2.0 * bj_PI
            local x = ax + r * Cos(ang)
            local y = ay + r * Sin(ang)
            if AiBuildPlaceable(x, y) and not AiBuildSpotOccupied(x, y, minSpacing) then
                return x, y
            end
            s = s + 1
        end
        ring = ring + 1
    end
    return nil, nil
end

-- Nearest placeable spot. Prefer the capital anchor (keeps the base clustered); if
-- that base is hemmed in (dense/corner — every nearby cell blocked), fall back to the
-- builder's own position, which is what produced working bases before the capital
-- anchor existed. Returns x,y or nil,nil.
---@param pi integer
---@param builder unit
---@return real|nil, real|nil
function AiFindBuildSpot(pi, builder)
    local rad = AiBuildingRadius
    if rad == nil or rad <= 0 then rad = 256.0 end
    local phase = pi % 12
    -- Prefer builder's position: worker can reach it immediately, rapid initial expansion
    if builder ~= nil then
        local x, y = AiScanBuildRings(GetUnitX(builder), GetUnitY(builder), rad, phase)
        if x ~= nil then return x, y end
    end
    -- Fallback: capital anchor for base clustering
    local cap = playerCapital[pi]
    if cap ~= nil and GetUnitState(cap, UNIT_STATE_LIFE) > 0.405 then
        local x, y = AiScanBuildRings(GetUnitX(cap), GetUnitY(cap), rad, phase)
        if x ~= nil then return x, y end
    end
    return nil, nil
end

-- ====================================================================
-- Production track P2: unit ordering by target composition (vs weighted random).
-- Opt-in via global AiSmartProduce + race def.compTarget = { [unitId]=fraction }.
-- Picks, among the candidate unit ids already gathered in tArray by AiRunProduction
-- (gates/branch/limit applied), the one with the largest share deficit
-- (target - current), pulling the army toward the desired mix. Returns nil when
-- none of the candidates are listed in compTarget -> caller keeps random.
-- ====================================================================
AiSmartProduce = AiSmartProduce or true

---@param pi integer
---@param def table
---@return integer|nil
function AiPickByComposition(pi, def)
    local comp = def.compTarget
    if comp == nil then return nil end
    local total = getAiCount(pi, StringHash("Number"))
    if total < 1 then total = 1 end
    local bestId, bestDef = nil, -1e30
    local seen = {}
    local n = tArray[0]
    local i = 1
    while i <= n do
        local id = tArray[i]
        if not seen[id] then
            seen[id] = true
            local target = comp[id]
            if target ~= nil then
                local deficit = target - I2R(getAiCount(pi, id)) / I2R(total)
                if deficit > bestDef then bestDef = deficit; bestId = id end
            end
        end
        i = i + 1
    end
    return bestId
end

-- ====================================================================
-- Pirate Ports: buy fleet from neutral shipyards (n04K).
-- Sells: h0OY escort (345g) + h0OX transport (300g).
-- Toggle: PiratePortEnabled via bridge. Default on.
-- ====================================================================
PiratePorts = PiratePorts or {}
PiratePortEnabled = PiratePortEnabled or true

function AiPiratePortsScan()
    if #PiratePorts > 0 then return end
    local g = CreateGroup()
    GroupEnumUnitsOfPlayer(g, Player(PLAYER_NEUTRAL_PASSIVE), nil)
    local s = BlzGroupGetSize(g)
    local i = 0
    while i < s do
        local u = BlzGroupUnitAt(g, i)
        if GetUnitTypeId(u) == FourCC('n04K') then
            PiratePorts[#PiratePorts + 1] = { unit = u, x = GetUnitX(u), y = GetUnitY(u) }
        end
        i = i + 1
    end
    DestroyGroup(g)
    BrainLog(-1, "PiratePorts: scanned n=" .. tostring(#PiratePorts))
end

if PiratePortEnabled then
    AiPiratePortsScan()
end

function AiBuyPirateFleet(pi)
    if not PiratePortEnabled then return false end
    if PiratePorts == nil or #PiratePorts == 0 then
        -- The boot-time AiPiratePortsScan() ran before CreateAllUnits, so it always
        -- found 0. Retry now that units exist; cap tries so a truly portless map
        -- doesn't re-enumerate every call forever.
        AiPiratePortsScanTries = (AiPiratePortsScanTries or 0)
        if AiPiratePortsScanTries < 12 then
            AiPiratePortsScanTries = AiPiratePortsScanTries + 1
            AiPiratePortsScan()
        end
        if PiratePorts == nil or #PiratePorts == 0 then return false end
    end

    local p = Player(pi)
    local gold = GetPlayerState(p, PLAYER_STATE_RESOURCE_GOLD)
    if gold < 300 then return false end

    local navyCount = (udg_Ai_navy[pi] and BlzGroupGetSize(udg_Ai_navy[pi])) or 0
    if navyCount >= 6 then return false end

    local cx, cy
    local cap = playerCapital[pi]
    if cap ~= nil and UnitAlive(cap) then
        cx, cy = GetUnitX(cap), GetUnitY(cap)
    end
    if cx == nil then
        local ax, ay, an = 0.0, 0.0, 0
        local g2 = CreateGroup()
        GroupEnumUnitsOfPlayer(g2, p, nil)
        local s2 = BlzGroupGetSize(g2)
        local j = 0
        while j < s2 do
            local u = BlzGroupUnitAt(g2, j)
            if GetUnitState(u, UNIT_STATE_LIFE) > 0.405 then
                ax = ax + GetUnitX(u)
                ay = ay + GetUnitY(u)
                an = an + 1
            end
            j = j + 1
        end
        DestroyGroup(g2)
        if an > 0 then cx = ax / an; cy = ay / an end
    end
    if cx == nil then return false end

    local bestPort, bestDist = nil, 99999999.0
    for _, port in ipairs(PiratePorts) do
        local dx = port.x - cx
        local dy = port.y - cy
        local d = dx * dx + dy * dy
        if d < bestDist then bestDist = d; bestPort = port end
    end
    if bestPort == nil then return false end

    local hasUnitNear = false
    local g3 = CreateGroup()
    GroupEnumUnitsOfPlayer(g3, p, nil)
    local s3 = BlzGroupGetSize(g3)
    local k = 0
    while k < s3 do
        local u = BlzGroupUnitAt(g3, k)
        if GetUnitState(u, UNIT_STATE_LIFE) > 0.405 then
            local dx = GetUnitX(u) - bestPort.x
            local dy = GetUnitY(u) - bestPort.y
            if dx * dx + dy * dy < 500.0 * 500.0 then
                hasUnitNear = true
                break
            end
        end
        k = k + 1
    end
    DestroyGroup(g3)

    if not hasUnitNear then
        local best, bestD = nil, 99999999.0
        local g4 = CreateGroup()
        GroupEnumUnitsOfPlayer(g4, p, nil)
        local s4 = BlzGroupGetSize(g4)
        local m = 0
        while m < s4 do
            local u = BlzGroupUnitAt(g4, m)
            if GetUnitState(u, UNIT_STATE_LIFE) > 0.405 and not IsUnitType(u, UNIT_TYPE_HERO) then
                local dx = GetUnitX(u) - cx
                local dy = GetUnitY(u) - cy
                local d = dx * dx + dy * dy
                if d < bestD then bestD = d; best = u end
            end
            m = m + 1
        end
        DestroyGroup(g4)
        if best ~= nil then
            local bx = bestPort.x + GetRandomReal(-300, 300)
            local by = bestPort.y + GetRandomReal(-300, 300)
            IssuePointOrder(best, "move", bx, by)
            BrainLogEvery(pi, "pirateSend", 20, "sending unit to pirate port dist=" .. tostring(R2I(math.sqrt(bestDist))), "BRAINFOC")
        end
        return false
    end

    local bought = false
    if not UnitAlive(bestPort.unit) then return false end
    if gold >= 345 then
        local r = IssueNeutralImmediateOrderById(p, bestPort.unit, FourCC('h0OY'))
        if r then
            local g5 = CreateGroup()
            GroupEnumUnitsOfPlayer(g5, p, nil)
            local s5 = BlzGroupGetSize(g5)
            local n = 0
            while n < s5 do
                local u = BlzGroupUnitAt(g5, n)
                if GetUnitTypeId(u) == FourCC('h0OY') and not IsUnitInGroup(u, udg_Ai_navy[pi]) then
                    GroupAddUnit(udg_Ai_navy[pi], u)
                    NumberAdd(pi, StringHash("NumberN"))
                    BrainLogTag(pi, "BRAINFOC", "pirate buy escort h0OY")
                    bought = true
                    break
                end
                n = n + 1
            end
            DestroyGroup(g5)
        end
    end

    gold = GetPlayerState(p, PLAYER_STATE_RESOURCE_GOLD)
    if gold >= 300 then
        local r = IssueNeutralImmediateOrderById(p, bestPort.unit, FourCC('h0OX'))
        if r then
            local g6 = CreateGroup()
            GroupEnumUnitsOfPlayer(g6, p, nil)
            local s6 = BlzGroupGetSize(g6)
            local n = 0
            while n < s6 do
                local u = BlzGroupUnitAt(g6, n)
                if GetUnitTypeId(u) == FourCC('h0OX') and not IsUnitInGroup(u, udg_Ai_navy[pi]) then
                    GroupAddUnit(udg_Ai_navy[pi], u)
                    NumberAdd(pi, StringHash("NumberN"))
                    BrainLogTag(pi, "BRAINFOC", "pirate buy transport h0OX")
                    bought = true
                    break
                end
                n = n + 1
            end
            DestroyGroup(g6)
        end
    end

    return bought
end
