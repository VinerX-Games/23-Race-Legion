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
    focusMargin  = 25.0,     -- hysteresis: keep current focus unless beaten by this
    homeThreat   = 20.0,     -- enemy power near capital that triggers defend/recall
    tpDist       = 6000.0,   -- focus farther than this -> consider TP logistics
    weights = {
        kind  = { capital = 100, cluster = 40, capture = 30, weak = 20, front = 15 },
        value = 1.0, dist = 0.002, claim = 25.0, siege = 0.5,
    },
}

-- Optional per-building-type bonus/override added on top of the live income
-- valuation below. [typeId] = extra value. Empty by default.
AiBuildingValue = AiBuildingValue or {}

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

-- ---- squad bookkeeping (stubs; populated in Phase 2) ---------------
---@param pi integer
---@return table
function AiSquadsOf(pi)
    local t = AiSquads[pi]
    if t == nil then t = {}; AiSquads[pi] = t end
    return t
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
    local dist = SquareRoot(dx * dx + dy * dy)
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
    while true do
        local u = FirstOfGroup(gAllyGroup)
        if u == nil then break end
        GroupRemoveUnit(gAllyGroup, u)
        GroupAddUnit(gSubGroup, u)
        cnt = cnt + 1
        ordered = ordered + 1
        if cnt >= 12 then
            GroupPointOrder(gSubGroup, "attack", x, y)
            GroupClear(gSubGroup)
            cnt = 0
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

-- Entry point when a bot has an active brain ("objective"). Perceive → refresh
-- objectives on schedule → pick a focus (force concentration) → order idle army
-- there. Falls back to swarm when there are no objectives. Phase 3 adds defense
-- recall + TP logistics; persistent squad FSM is a later refinement.
---@param pi integer
---@param p player
function AiBrainArmyTick(pi, p)
    local wm = AiBrainPerceive(pi)
    BrainLogEvery(pi, "perceive", 5,
        "perceive army=" .. tostring(wm.armyCount)
        .. " threatHome=" .. tostring(R2I(wm.threatHome or 0))
        .. " capHP=" .. tostring(R2I(wm.capHP or 0)))

    -- Defense takes priority: recall the field army home when the capital is
    -- threatened or actively under siege. The standing AiCapitalGuard reserve is
    -- already parked at the capital (aiUnitJoinsCapitalGuard).
    if wm.defendHome and wm.capX ~= nil then
        local recalled = AiBrainOrderIdleTo(pi, p, wm.capX, wm.capY)
        BrainLogEvery(pi, "defend", 3, "DEFEND threatHome=" .. tostring(R2I(wm.threatHome or 0))
            .. " capHP=" .. tostring(R2I(wm.capHP or 0)) .. " siege=" .. tostring(wm.capSiege)
            .. " recalled=" .. tostring(recalled), "BRAINDEF")
        return
    end

    local cfg = AiBrainCfg(pi)
    local every = cfg.clusterEvery or AiBrainDefaults.clusterEvery
    if wm.objectives == nil or (wm.tick % every) == 0 then
        AiBrainCollectObjectives(pi, wm)
    end

    local focus = AiBrainPickFocus(pi, wm)
    if focus == nil then
        BrainLogEvery(pi, "nofocus", 5, "no objectives -> swarm fallback")
        AiArmyLegacyTick(p)
        return
    end

    AiBrainTryLogistics(pi, p, focus, wm)
    local ordered = AiBrainOrderIdleTo(pi, p, focus.x, focus.y)
    if wm.focusKey ~= wm.lastLoggedFocus then
        wm.lastLoggedFocus = wm.focusKey
        BrainLogTag(pi, "BRAINFOC", "focus kind=" .. tostring(focus.kind)
            .. " x=" .. tostring(R2I(focus.x)) .. " y=" .. tostring(R2I(focus.y))
            .. " val=" .. tostring(R2I(focus.value)) .. " cnt=" .. tostring(focus.count)
            .. " score=" .. tostring(R2I(focus.score or 0)) .. " ordered=" .. tostring(ordered))
    else
        BrainLogEvery(pi, "act", 8, "focus stable ordered=" .. tostring(ordered))
    end
end

-- ====================================================================
-- Production track P1: deterministic building placement (vs random ring).
-- Independent of the army brain; opt-in via global AiSmartBuild (default off,
-- random ring stays the fallback). Searches expanding rings/sectors around the
-- capital (or builder) for the nearest placeable, non-crowded spot. Tag BRAINBLD.
-- ====================================================================
AiSmartBuild = AiSmartBuild or false

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
AiSmartProduce = AiSmartProduce or false

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
