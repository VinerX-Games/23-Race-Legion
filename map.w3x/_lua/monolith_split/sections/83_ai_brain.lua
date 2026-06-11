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
AiBuildClaimTicks = AiBuildClaimTicks or 20  -- ticks a claimed worker is left alone before recycle/reuse
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
AiBrainMaxProduce      = AiBrainMaxProduce      or 20  -- max unit-training orders per bot per tick
AiBrainMaxBuild        = AiBrainMaxBuild        or 10  -- max building-attempts per bot per tick
g_AiOrdered = g_AiOrdered or {}                        -- per-bot+unit training guard: [key] = last_tick
AiRetrainInterval = AiRetrainInterval or 15            -- ticks between re-issue of same unit order
AiBrainExpansionEvery  = AiBrainExpansionEvery  or 30  -- expansion-check every N brain-ticks
AiBrainNavalEvery      = AiBrainNavalEvery      or 15  -- naval-check every N brain-ticks
AiBrainNavalStartTick  = AiBrainNavalStartTick  or 23  -- first naval check after N brain-ticks (~4min w/ 16 bots)
AiBrainMaxPorts        = AiBrainMaxPorts        or 20  -- max shipyards/ports per bot
AiBrainLandingEvery     = AiBrainLandingEvery     or 16  -- landing tick every N brain-ticks
AiBrainLandingRadius    = AiBrainLandingRadius    or 800 -- load/unload radius
AiBrainLandingMaxTransports = AiBrainLandingMaxTransports or 6  -- max transports to load per tick

-- R10: known transport unit types (from all shipyards + pirate). Maps shipyard→transport.
AiTransportTypes = {
    [FourCC('h0D1')] = FourCC('h0D2'), [FourCC('h0D8')] = FourCC('h0D9'),
    [FourCC('h03R')] = FourCC('h00X'), [FourCC('h011')] = FourCC('h00X'),
    [FourCC('h0D3')] = FourCC('h0D4'), [FourCC('h0HO')] = FourCC('h0D4'),
    [FourCC('h0E7')] = FourCC('h0E5'),
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
        kind  = { capital = 100, cluster = 40, capture = 60, weak = 20, front = 15 },
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
        kind  = { capital = 100, cluster = 40, capture = 60, weak = 20, front = 15 },
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
        playerCapital[pi] = pick
        -- NB: intentionally NOT calling aiCapitalEnter here — it runs a nested
        -- GroupEnumUnitsInRange/ForGroup, and a reentrant enum during the brain tick
        -- is an engine-stability risk. We only need the anchor reference.
        BrainLogTag(pi, "BRAIN", "adopted base anchor (capital) type="
            .. tostring(GetUnitTypeId(pick)))
    end
end

-- ---- perceive (slow, 1 player/tick) --------------------------------
-- Builds/updates the shared world model in AiData[pi].wm. Objective collection
-- is deferred to Phase 2; Phase 1 captures army geometry + home threat only.
---@param pi integer
---@return table
function AiBrainPerceive(pi)
    -- Ensure a base anchor exists (self-guards: enums only while unset/dead).
    AiEnsureCapital(pi)
    local wm = AiData[pi].wm
    if wm == nil then wm = {}; AiData[pi].wm = wm end
    wm.tick = (wm.tick or 0) + 1

    -- Clean dead units from udg_Ai_army (some races do KillUnit/ReplaceUnit)
    local armyGroup = udg_Ai_army[pi]
    if armyGroup ~= nil then
        local i = 0
        while i < BlzGroupGetSize(armyGroup) do
            local u = BlzGroupUnitAt(armyGroup, i)
            if u == nil then i = i + 1
            elseif GetUnitState(u, UNIT_STATE_LIFE) <= 0.405 then GroupRemoveUnit(armyGroup, u)
            else i = i + 1 end
        end
    end

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
    ProbeLogWrite("[SQDBG] ordmov-enter")
    local tmp = CreateGroup()
    ProbeLogWrite("[SQDBG] ordmov-cr1")
    local sub = CreateGroup()
    ProbeLogWrite("[SQDBG] ordmov-cr2")
    local sz = BlzGroupGetSize(g)
    ProbeLogWrite("[SQDBG] ordmov-sz=" .. tostring(sz))
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
        ProbeLogWrite("[SQDBG] ordmov-gpo")
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
    -- Dynamic cap: ~5 squads at 200 units, ~3 at 50, min 8
    local cap = math.max(8, math.ceil(armyCount / 5))
    local bestSid, bestDist = nil, 99999999.0
    local ux, uy = GetUnitX(u), GetUnitY(u)
    for sid, sq in pairs(squads) do
        if sq.role == "assault" then
            local cx, cy, _ = AiGroupCentroid(sq.members)
            local dx, dy = ux - cx, uy - cy
            local d = dx * dx + dy * dy
            if d < bestDist then bestDist = d; bestSid = sid end
        end
    end
    if bestSid ~= nil then
        local sq = squads[bestSid]
        GroupAddUnit(sq.members, u)
        return
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
        local i = 0
        while i < BlzGroupGetSize(g) do
            local u = BlzGroupUnitAt(g, i)
            if u == nil then i = i + 1
            elseif GetUnitState(u, UNIT_STATE_LIFE) <= 0.405 then GroupRemoveUnit(g, u)
            else i = i + 1 end
        end
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
function AiSquadTickMuster(pi, sid, sq, p, wm)
    ProbeLogWrite("[SQDBG] muster-enter sq" .. tostring(sid))
    ProbeLogWrite("[SQDBG] muster-sz-start")
    local sz = AiSquadSize(sq.members)
    ProbeLogWrite("[SQDBG] muster-sz=" .. tostring(sz))
    local cfg = AiBrainCfg(pi)
    ProbeLogWrite("[SQDBG] muster-cfg cm=" .. tostring(cfg.commitMin or AiSquadCommitMin))
    if sz >= (cfg.commitMin or AiSquadCommitMin) then
        ProbeLogWrite("[SQDBG] muster-pickobj")
        local obj = AiSquadPickObj(pi, sq, wm)
        if obj ~= nil then ProbeLogWrite("[SQDBG] muster->march"); sq.objective = obj; return "march" end
    end
    ProbeLogWrite("[SQDBG] muster-ordmov rx=" .. tostring(R2I(sq.rally.x)) .. " ry=" .. tostring(R2I(sq.rally.y)))
    AiSquadOrderMov(sq.members, sq.rally.x, sq.rally.y)
    ProbeLogWrite("[SQDBG] muster-done")
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
        local m = AiFindMageOnContinent(pi, oc)
        if m ~= nil then gPi = pi; gPlayer = p; PortTo(m); return "march" end
        local rt = AiPortalRoute(sc, oc)
        if rt ~= nil and #rt >= 2 then local portal = AiFindPortal(rt[1], rt[2])
            if portal ~= nil then AiSquadOrderMov(sq.members, GetUnitX(portal), GetUnitY(portal)); return "march" end
        end
        AiBrainTryLogistics(pi, p, obj, wm)
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
    if o.kind == "capture" then
        local prox = 4000.0 / dist
        return kindBase + (w.value or 1.0) * o.value + prox
    end
    return kindBase + (w.value or 1.0) * o.value - (w.dist or 0.002) * dist
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
function AiFindProdBuilding(pi, bldType)
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
            and GetUnitState(u, UNIT_STATE_LIFE) > 0.405 then
            local pct = GetUnitStatePercent(u, UNIT_STATE_LIFE, UNIT_STATE_MAX_LIFE)
            if pct >= 99.0 then return u end  -- complete & healthy: take it immediately
            if pct > bestPct then best = u; bestPct = pct end
        end
    end
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

-- E3: recycle idle build-pool workers back to harvesting. A worker that is idle
-- (order==0) and past its build-claim window did not complete a build → return it to
-- the lumber line instead of letting it pile up in buildersT (harvest=0 across all
-- bots was the smoking gun). Bounded per call to avoid order spam.
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
            local expired = c ~= nil and (now - c) >= AiBuildClaimTicks
            -- Recycle ONLY idle workers (order==0) with no claim or expired claim.
            -- NEVER touch workers with a current order (channeling build, moving, etc.)
            if GetUnitCurrentOrder(u) == 0 and (c == nil or expired) then
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

    local ordered = 0
    local maxN = AiBrainMaxProduce
    local now = AiBrainTickCounter or 0

    -- R7: build a set of legitimate producer building types — skip production
    -- entries whose bldType is NOT an actual building (e.g. Silitids larva e01I).
    local isBldType = {}
    local buildList = race.buildings
    if buildList then
        isBldType[buildList.seed] = true
        for _, row in ipairs(buildList) do
            if type(row[1]) == "number" then isBldType[row[1]] = true end
        end
    end

    -- 1) Workers: train independently of compTarget, always up to cap
    local w = prod.worker
    if w and w.from and w.id then
        local wCnt = getAiCount(pi, w.id) or 0
        if wCnt < (w.cap or 40) then
            for _, fromBldType in ipairs(w.from) do
                local bld = AiFindProdBuilding(pi, fromBldType)
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

    if not comp then return ordered end

    local totalMil = wm.armyCount or 0
    if totalMil < 1 then totalMil = 1 end

    -- 2) Military: scan compTarget for deficit, find building, issue order
    for unitId, targetRatio in pairs(comp) do
        if ordered >= maxN then break end
        if type(unitId) ~= "number" or targetRatio == nil then goto skipUnit end

        local current = getAiCount(pi, unitId) or 0
        if current < 0 then current = 0 end
        local currentRatio = current / totalMil
        if currentRatio >= targetRatio then goto skipUnit end

        -- Find which building produces this unit
        for bldType, rows in pairs(prod) do
            if bldType == "worker" then goto skipBld end
            if type(rows) ~= "table" then goto skipBld end
            if not isBldType[bldType] then goto skipBld end  -- R7: skip non-buildings (larva, eggs, etc.)
            for _, row in ipairs(rows) do
                local uid = row[1]
                if uid ~= nil and uid ~= 0 then
                    if uid == unitId then
                        local bld = AiFindProdBuilding(pi, bldType)
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
                        local bld = AiFindProdBuilding(pi, bldType)
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
    -- A production building is one listed as a key in race.production (excluding "worker").
    local prodKeys = {}
    if race.production then
        for k, _ in pairs(race.production) do
            if type(k) == "number" then prodKeys[k] = true end
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

    -- R5: resume stalled construction before recycling idle workers.
    -- Channeling races (Human, Forsaken) need the worker to stay; if the
    -- original builder was killed/recycled, the building site stays incomplete.
    BrainResumeBuildings(pi)

    -- E3: every tick, drain idle/failed workers from buildersT back to harvest
    -- (not just when built==0) so the build pool can't clog and lumber keeps flowing.
    AiRecycleBuilders(pi, 4)

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

    local limit = row[2] or 1
    local count = AiCountBuildingsOfType(pi, bldType)
    if count >= limit then return 0 end

    if row.gate then
        local gateFn = race.gates and race.gates[row.gate]
        if gateFn and not gateFn(pi) then return 0 end
    end

    local worker = AiFindFreeWorker(pi)
    if worker == nil then return 0 end

    TryBuild_u = worker
    TryBuildWithType(bldType)
    return 1
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
function BrainNavalDecision(pi, wm, race)
    local wallType = race.wall
    if wallType == nil then return end
    if AiCountBuildingsOfType(pi, wallType) >= AiBrainMaxPorts then return end

    -- Find water point near capital
    local cx, cy = wm.capX, wm.capY
    if cx == nil then return end
    if udg_WaterPoints ~= nil then
        local best, bestD = nil, 99999999.0
        for _, wp in ipairs(udg_WaterPoints) do
            local dx = wp.x - cx
            local dy = wp.y - cy
            local d = dx * dx + dy * dy
            if d < bestD then bestD = d; best = wp end
        end
        if best ~= nil then
            local worker = AiFindFreeWorker(pi)
            if worker ~= nil then
                TryBuild_u = worker
                TryBuildWithType(wallType, best.x, best.y)
                BrainLogEvery(pi, "brainnavy", 30, "shipyard at water point", "BRAINNAVY")
            end
        end
    end
end

--- Deterministic TryBuild variant: place a specific building type at a forced spot
--- or via AiFindBuildSpot. Skips random water-point and far-walk.
---@param bldType integer
---@param fx real|nil
---@param fy real|nil
function TryBuildWithType(bldType, fx, fy)
    local u = TryBuild_u
    if u == nil or bldType == nil then return end
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
        return
    end

    if AiSmartBuild then
        local bx, by = AiFindBuildSpot(pi, u)
        if bx ~= nil then
            reserve(bx, by)
            IssueBuildOrderById(u, bldType, bx, by)
            return
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
            return
        end
    end
    -- last resort: issue anyway so the worker isn't stranded without an order
    local rx, ry = ux0 + AiBuildingRadius * Cos(0), uy0 + AiBuildingRadius * Sin(0)
    reserve(rx, ry)
    IssueBuildOrderById(u, bldType, rx, ry)
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
    if focus == nil then return 0 end

    local army = udg_Ai_army[pi]

    if gSubGroup == nil then gSubGroup = CreateGroup() end
    GroupClear(gSubGroup)

    local cnt = 0

    -- Process main army group
    if army ~= nil then
        local armySz = BlzGroupGetSize(army)
        for i = 0, armySz - 1 do
            local u = BlzGroupUnitAt(army, i)
            if u ~= nil and GetUnitState(u, UNIT_STATE_LIFE) > 0.405 then
                local o = GetUnitCurrentOrder(u)
                if o == 0 or o == 851972 or o == 851976 then
                    GroupAddUnit(gSubGroup, u)
                    cnt = cnt + 1
                    if cnt % 12 == 0 then
                        GroupPointOrder(gSubGroup, "attack", focus.x, focus.y)
                        GroupClear(gSubGroup)
                    end
                end
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
                if u ~= nil
                    and GetUnitTypeId(u) == wfId
                    and GetUnitState(u, UNIT_STATE_LIFE) > 0.405
                    and GetUnitCurrentOrder(u) == 0 then
                    GroupAddUnit(gSubGroup, u)
                    cnt = cnt + 1
                    if cnt % 12 == 0 then
                        GroupPointOrder(gSubGroup, "attack", focus.x, focus.y)
                        GroupClear(gSubGroup)
                    end
                end
            end
        end
    end

    if BlzGroupGetSize(gSubGroup) > 0 then
        GroupPointOrder(gSubGroup, "attack", focus.x, focus.y)
        GroupClear(gSubGroup)
    end
    return cnt
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

    -- Prefer enemy capitals / ZahvatBuildings that are far (>3000) from ours
    local best, bestScore = nil, -1
    for _, obj in ipairs(objs) do
        local dx = obj.x - cx
        local dy = obj.y - cy
        local d = dx * dx + dy * dy
        -- Score: prefer distant enemy capitals
        local sc = d
        if obj.kind == "capital" then sc = sc * 3
        elseif obj.kind == "city" then sc = sc * 2
        end
        if d > 3000 * 3000 and sc > bestScore then
            bestScore = sc; best = obj
        end
    end
    return best
end

-- Count loaded units on a transport (units with the transport as their current order target).
-- WC3 doesn't expose cargo count, so we approximate: if transport is moving/has "load" order
-- from nearby units, it's busy. We track by AI-side state table.
AiLandingState = AiLandingState or {}  -- [unit] = { phase, targetX, targetY }

---@param pi integer
---@param p player
---@param wm table
---@return integer
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
    local tx, ty = nil, nil
    if target ~= nil then tx, ty = target.x, target.y end

    local processed = 0
    local maxN = AiBrainLandingMaxTransports

    for i = 0, sz - 1 do
        if processed >= maxN then break end
        local u = BlzGroupUnitAt(navy, i)
        if u == nil then goto nextShip end
        if GetUnitState(u, UNIT_STATE_LIFE) <= 0.405 then goto nextShip end
        local uid = GetUnitTypeId(u)
        if not AiTransportSet[uid] then goto nextShip end  -- combat ship, skip

        local order = GetUnitCurrentOrder(u)
        local st = AiLandingState[u]
        local ux, uy = GetUnitX(u), GetUnitY(u)

        if tx ~= nil and st ~= nil and st.phase == "loaded" then
            -- Sailing to target
            local dx = ux - tx; local dy = uy - ty
            local dist = dx * dx + dy * dy
            if dist < AiBrainLandingRadius * AiBrainLandingRadius then
                -- Arrived: unload
                IssueImmediateOrder(u, "unloadall")
                st.phase = "done"
                AiLandingState[u] = nil
                processed = processed + 1
            elseif order == 0 or order == 851972 then
                -- Keep sailing
                IssuePointOrder(u, "move", tx, ty)
                processed = processed + 1
            end
        elseif tx ~= nil and (st == nil or st.phase == "idle") and order == 0 then
            -- Idle transport: load nearby army
            if army ~= nil then
                local loaded = false
                local asz = BlzGroupGetSize(army)
                for j = 0, asz - 1 do
                    local a = BlzGroupUnitAt(army, j)
                    if a == nil then goto nextArmy end
                    if GetUnitState(a, UNIT_STATE_LIFE) <= 0.405 then goto nextArmy end
                    if IsUnitType(a, UNIT_TYPE_HERO) then goto nextArmy end
                    local ao = GetUnitCurrentOrder(a)
                    if ao ~= 0 and ao ~= 851972 and ao ~= 851976 then goto nextArmy end
                    local ax, ay = GetUnitX(a), GetUnitY(a)
                    local adx = ax - ux; local ady = ay - uy
                    if adx * adx + ady * ady < AiBrainLandingRadius * AiBrainLandingRadius then
                        IssueTargetOrder(a, "load", u)
                        loaded = true
                        -- Stop after loading 6 units per transport
                        if j - i >= 6 then break end
                    end
                    ::nextArmy::
                end
                if loaded then
                    AiLandingState[u] = { phase = "loaded", targetX = tx, targetY = ty }
                    processed = processed + 1
                end
            end
        elseif st ~= nil and st.phase == "done" and order == 0 then
            -- Empty after unload: return to port
            local cx, cy = wm.capX, wm.capY
            if cx ~= nil then
                IssuePointOrder(u, "move", cx, cy)
                AiLandingState[u] = { phase = "returning" }
                processed = processed + 1
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

    AiSquadReapDead(pi)
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

    BrainFocus(pi, p, wm)
    lap("focus")

    if (wm.tick % 4) == 0 then
        BrainNavalFocus(pi, p)
    end

    if (wm.tick % AiBrainLandingEvery) == 0 then
        BrainLandingTick(pi, p, wm)
    end

    if (wm.tick % 8) == 0 then AiBuyPirateFleet(pi) end
    if (wm.tick % 4) == 0 then AiDiplomatTick(pi) end
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
    -- Center must be walkable (not cliff/blocked) and not water.
    if IsTerrainPathable(x, y, PATHING_TYPE_WALKABILITY) then return false end
    if not IsTerrainPathable(x, y, PATHING_TYPE_FLOATABILITY) then return false end
    -- Footprint ring: sample WATER only. Walkability under the center's neighbours is
    -- often "blocked" simply because friendly buildings sit there (dense base) — that
    -- is a spacing concern (AiBuildSpotOccupied), not a terrain one, and sampling it
    -- locked dense bases out of building entirely. Water at a footprint corner, though,
    -- makes the engine silently reject the order — that we must catch.
    local offs = { {half,0},{-half,0},{0,half},{0,-half} }
    for i = 1, 4 do
        if not IsTerrainPathable(x + offs[i][1], y + offs[i][2], PATHING_TYPE_FLOATABILITY) then
            return false
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
