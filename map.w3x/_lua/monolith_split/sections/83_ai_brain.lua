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

-- Tunables (global defaults; races may override via def.brainWeights). Phase 2+
-- consumes the weights; Phase 1 uses only the geometry/threat radii.
AiBrainDefaults = {
    brain        = "swarm",
    topK         = 8,        -- objectives kept per player
    clusterEvery = 8,        -- recompute objective pool every N perceive ticks
    rCluster     = 1600.0,   -- cluster aggregation radius
    rHome        = 2500.0,   -- capital threat scan radius
    squadCap     = 12,
    commitMin    = 8,
    guardFrac    = 0.2,
    weights = {
        kind  = { capital = 100, cluster = 40, capture = 30, weak = 20, front = 15 },
        value = 1.0, dist = 0.002, claim = 25.0, siege = 0.5,
    },
}

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
---@param pi integer
---@param msg string
function BrainLog(pi, msg)
    ProbeLogWrite("[BRAIN] pi=" .. tostring(pi) .. " " .. msg)
end

-- Log at most once per `n` calls of (pi,key). Counter lives in the world model.
---@param pi integer
---@param key string
---@param n integer
---@param msg string
function BrainLogEvery(pi, key, n, msg)
    local wm = AiData[pi].wm
    if wm == nil then BrainLog(pi, msg); return end
    local kk = "logn_" .. key
    local c = (wm[kk] or 0) + 1
    wm[kk] = c
    if c % n == 0 then
        BrainLog(pi, msg)
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
    local size = BlzGroupGetSize(g)
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

    local cx, cy, n = AiGroupCentroid(udg_Ai_army[pi])
    wm.cx, wm.cy, wm.armyCount = cx, cy, n

    local cap = playerCapital[pi]
    if cap ~= nil and GetUnitState(cap, UNIT_STATE_LIFE) > 0.405 then
        local cfg = AiBrainCfg(pi)
        wm.capX, wm.capY = GetUnitX(cap), GetUnitY(cap)
        wm.capHP = GetUnitState(cap, UNIT_STATE_LIFE)
        wm.threatHome = AiEnemyPowerAround(Player(pi), wm.capX, wm.capY, cfg.rHome or AiBrainDefaults.rHome)
    else
        wm.capHP = 0
        wm.threatHome = 0
    end
    return wm
end

-- ---- squad bookkeeping (stubs; populated in Phase 2) ---------------
---@param pi integer
---@return table
function AiSquadsOf(pi)
    local t = AiSquads[pi]
    if t == nil then t = {}; AiSquads[pi] = t end
    return t
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

-- Entry point when a bot has an active brain. Phase 1: observe (perceive + log)
-- then fall back to swarm so behavior is unchanged. Phase 2 replaces the body
-- with objective planning + squad ticks.
---@param pi integer
---@param p player
function AiBrainArmyTick(pi, p)
    local wm = AiBrainPerceive(pi)
    BrainLogEvery(pi, "perceive", 5,
        "perceive army=" .. tostring(wm.armyCount)
        .. " threatHome=" .. tostring(R2I(wm.threatHome or 0))
        .. " capHP=" .. tostring(R2I(wm.capHP or 0)))
    AiArmyLegacyTick(p)
end
