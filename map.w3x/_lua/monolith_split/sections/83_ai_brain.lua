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
AiBrainMaxBuild        = AiBrainMaxBuild        or 6   -- max building-attempts per bot per tick
AiBrainExpansionEvery  = AiBrainExpansionEvery  or 30  -- expansion-check every N brain-ticks
AiBrainNavalEvery      = AiBrainNavalEvery      or 60  -- naval-check every N brain-ticks
AiBrainNavalStartTick  = AiBrainNavalStartTick  or 300 -- first naval check after this many brain-ticks (~5min)

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

AiBrainPowAcc = 0.0
---@return boolean
function f_BrainEnemyPow()
    local u = GetFilterUnit()
    if u ~= nil and GetUnitState(u, UNIT_STATE_LIFE) > 0.405 and IsPlayerEnemy(GetOwningPlayer(u), CheckPlayer) then
        AiBrainPowAcc = AiBrainPowAcc + AiUnitPower(u)
    end
    return false
end

-- Summed enemy power within `radius` of (x,y), as seen by player p. One enum.
---@param p player
---@param x real
---@param y real
---@param radius real
---@return real
function AiEnemyPowerAround(p, x, y, radius)
    CheckPlayer = p
    AiBrainPowAcc = 0.0
    AiBrainEnemyPowCond = AiBrainEnemyPowCond or Condition(f_BrainEnemyPow)
    AiBrainScanGroup = AiBrainScanGroup or CreateGroup()
    GroupEnumUnitsInRange(AiBrainScanGroup, x, y, radius, AiBrainEnemyPowCond)
    return AiBrainPowAcc
end

-- ---- perceive (slow, 1 player/tick) --------------------------------
-- Builds/updates the shared world model in AiData[pi].wm. Objective collection
-- is deferred to Phase 2; Phase 1 captures army geometry + home threat only.
---@param pi integer
---@return table
function AiBrainPerceive(pi)
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
        wm.threatHome = AiEnemyPowerAround(Player(pi), wm.capX, wm.capY, cfg.rHome or AiBrainDefaults.rHome)
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
    local pow = AiEnemyPowerAround(Player(pi), o.x, o.y, 1600.0)
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
    if d < 600.0 or AiEnemyPowerAround(p, cx, cy, 800.0) > 1.0 then return "engage" end
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
    GroupEnumUnitsOfPlayer(gAllyGroup, p, B_Lazy)
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
    for i = 0, sz - 1 do
        local u = BlzGroupUnitAt(grp, i)
        if u ~= nil and GetUnitTypeId(u) == bldType
            and GetUnitState(u, UNIT_STATE_LIFE) > 0.405 then
            return u
        end
    end
    return nil
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
            n = n + 1
        end
    end
    return n
end

---@param pi integer
---@return unit|nil
function AiFindFreeWorker(pi)
    -- Try builders pool first, then buildersT, then pull from harvest
    local function alive(u)
        return u ~= nil and GetUnitState(u, UNIT_STATE_LIFE) > 0.405
    end
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

    -- 1) Workers: train independently of compTarget, always up to cap
    local w = prod.worker
    if w and w.from and w.id then
        local wCnt = getAiCount(pi, w.id) or 0
        if wCnt < (w.cap or 40) then
            for _, fromBldType in ipairs(w.from) do
                local bld = AiFindProdBuilding(pi, fromBldType)
                if bld ~= nil then
                    local key = pi * 1000000 + w.id
                    if not g_AiOrdered[key] then
                        IssueImmediateOrderById(bld, w.id)
                        g_AiOrdered[key] = true
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
            for _, row in ipairs(rows) do
                local uid = row[1]
                if uid ~= nil and uid ~= 0 then
                    if uid == unitId then
                        local bld = AiFindProdBuilding(pi, bldType)
                        if bld ~= nil then
                            local key = pi * 1000000 + unitId
                            if not g_AiOrdered[key] then
                                IssueImmediateOrderById(bld, unitId)
                                g_AiOrdered[key] = true
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
                            if not g_AiOrdered[key] then
                                IssueImmediateOrderById(bld, unitId)
                                g_AiOrdered[key] = true
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

    -- Handle array entries: each is { bldType, limit, ... }
    for _, row in ipairs(buildOrder) do
        if built >= maxN then break end
        local bldType = row[1]
        if type(bldType) ~= "number" then goto skipBld end

        local limit = row[2] or 1
        local count = AiCountBuildingsOfType(pi, bldType)
        if count >= limit then goto skipBld end

        -- Check gate (tier2, etc.) if present
        if row.gate then
            local gateFn = race.gates and race.gates[row.gate]
            if gateFn and not gateFn(pi) then goto skipBld end
        end

        local worker = AiFindFreeWorker(pi)
        if worker ~= nil then
            TryBuild_u = worker
            TryBuildWithType(bldType)
            built = built + 1
        end
        ::skipBld::
    end

    -- Expansion check: brain decides to seed a new cluster far from capital
    if wm.tick % AiBrainExpansionEvery == 0 then
        BrainExpandDecision(pi, wm, race)
    end

    -- Naval check: build shipyard / fleet after startup delay
    if wm.tick > AiBrainNavalStartTick and wm.tick % AiBrainNavalEvery == 0 then
        BrainNavalDecision(pi, wm, race)
    end

    return built
end

---@param pi integer
---@param wm table
---@param race table
function BrainExpandDecision(pi, wm, race)
    -- Pick a random expansion spot far from capital (AiBuildingRadius*7)
    local cx, cy = wm.capX, wm.capY
    if cx == nil then return end
    local ex = cx + AiBuildingRadius * 7 * Cos(GetRandomReal(0, 360) * bj_DEGTORAD)
    local ey = cy + AiBuildingRadius * 7 * Sin(GetRandomReal(0, 360) * bj_DEGTORAD)
    local worker = AiFindFreeWorker(pi)
    if worker ~= nil then
        IssuePointOrder(worker, "move", ex, ey)
        BrainLogEvery(pi, "brainexpd", 30, "expand to " .. tostring(R2I(ex)) .. "," .. tostring(R2I(ey)), "BRAINEXP")
    end
end

---@param pi integer
---@param wm table
---@param race table
function BrainNavalDecision(pi, wm, race)
    -- If already has a shipyard, skip
    local wallType = race.wall
    if wallType == nil then return end
    if AiCountBuildingsOfType(pi, wallType) > 0 then return end

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

    if fx ~= nil and fy ~= nil then
        IssueBuildOrderById(u, bldType, fx, fy)
        return
    end

    if AiSmartBuild then
        local bx, by = AiFindBuildSpot(pi, u)
        if bx ~= nil then
            IssueBuildOrderById(u, bldType, bx, by)
            return
        end
    end
    local ux, uy = GetUnitX(u), GetUnitY(u)
    ux = ux + AiBuildingRadius * Cos(GetRandomReal(0, 360) * bj_DEGTORAD)
    uy = uy + AiBuildingRadius * Sin(GetRandomReal(0, 360) * bj_DEGTORAD)
    IssueBuildOrderById(u, bldType, ux, uy)
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
    if army == nil then return 0 end
    local armySz = BlzGroupGetSize(army)
    if armySz == 0 then return 0 end

    if gSubGroup == nil then gSubGroup = CreateGroup() end
    GroupClear(gSubGroup)

    local cnt = 0
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
            local o = GetUnitCurrentOrder(u)
            if o == 0 or o == 851972 or o == 851976 then
                CheckPlayer = p
                udg_LocalUnit3 = u
                TryAttackN()
                processed = processed + 1
            end
        end
    end
    return processed
end

-- Entry point when a bot has an active brain ("objective"). Perceive → refresh
-- objectives on schedule → pick a focus (force concentration) → order idle army
-- there. Falls back to swarm when there are no objectives.
---@param pi integer
---@param p player
function AiBrainArmyTick(pi, p)
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
function AiBuildSpotOccupied(x, y, radius)
    AiBuildScanGroup = AiBuildScanGroup or CreateGroup()
    AiStructCond = AiStructCond or Condition(f_AnyStructure)
    GroupEnumUnitsInRange(AiBuildScanGroup, x, y, radius, AiStructCond)
    return FirstOfGroup(AiBuildScanGroup) ~= nil
end

-- IsTerrainPathable is inverted: true == blocked for that pathing type (matches
-- the `not IsTerrainPathable(..WALKABILITY)` idiom used in 98_ai_build.lua).
---@param x real
---@param y real
---@return boolean
function AiBuildPlaceable(x, y)
    if IsTerrainPathable(x, y, PATHING_TYPE_WALKABILITY) then return false end   -- blocked
    if IsTerrainPathable(x, y, PATHING_TYPE_FLOATABILITY) then return false end  -- water
    return true
end

-- Nearest placeable spot around the player's anchor. Returns x,y or nil,nil.
---@param pi integer
---@param builder unit
---@return real|nil, real|nil
function AiFindBuildSpot(pi, builder)
    local rad = AiBuildingRadius
    if rad == nil or rad <= 0 then rad = 256.0 end
    local ax, ay
    local cap = playerCapital[pi]
    if cap ~= nil and GetUnitState(cap, UNIT_STATE_LIFE) > 0.405 then
        ax, ay = GetUnitX(cap), GetUnitY(cap)
    else
        ax, ay = GetUnitX(builder), GetUnitY(builder)
    end
    local minSpacing = rad * 1.4
    local sectors = 12
    local phase = pi % sectors            -- vary the start angle per player
    local ring = 0
    while ring < 6 do
        local r = rad * 2.0 + ring * rad * 1.5
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
    if PiratePorts == nil or #PiratePorts == 0 then return false end

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
