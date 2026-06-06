AiRaces = AiRaces or {}
AiRaceTokens = AiRaceTokens or {}
AiRaceOrder = AiRaceOrder or {}

local function AiNormalizeToken(token)
    if token == nil then
        return nil
    end
    return string.lower(token)
end

---@param key string
---@param def table
function RegisterAiRace(key, def)
    if key == nil or key == "" or def == nil then
        return
    end
    def.key = key
    if AiRaces[key] == nil then
        AiRaceOrder[#AiRaceOrder + 1] = key
    end
    AiRaces[key] = def
    if def.tokens ~= nil then
        for _, token in ipairs(def.tokens) do
            local normalized = AiNormalizeToken(token)
            if normalized ~= nil and normalized ~= "" then
                AiRaceTokens[normalized] = key
            end
        end
    end
end

---@param pi integer
---@return table|nil
function AiRaceOf(pi)
    return AiRaces[AiRace[pi]]
end

---@param token string|nil
---@return table|nil
function AiRaceByToken(token)
    local normalized = AiNormalizeToken(token)
    if normalized == nil or normalized == "" then
        return nil
    end
    local key = AiRaceTokens[normalized]
    if key == nil then
        return nil
    end
    return AiRaces[key]
end

---@return table|nil
function AiRacePickRandom()
    local total = 0
    for _, key in ipairs(AiRaceOrder) do
        local race = AiRaces[key]
        local weight = race and race.weight or 0
        if weight > 0 then
            total = total + weight
        end
    end
    if total <= 0 then
        return nil
    end
    local roll = GetRandomInt(1, total)
    for _, key in ipairs(AiRaceOrder) do
        local race = AiRaces[key]
        local weight = race and race.weight or 0
        if weight > 0 then
            roll = roll - weight
            if roll <= 0 then
                return race
            end
        end
    end
    return nil
end

---@param pi integer
---@param race table|nil
---@return boolean
function AiStartRace(pi, race)
    if race == nil or race.start == nil then
        return false
    end
    race.start(pi)
    return true
end

---@param pi integer
---@param worker unit
---@param x real
---@param y real
---@return boolean
function AiDispatchWallBuild(pi, worker, x, y)
    local race = AiRaceOf(pi)
    if race == nil or race.wall == nil then
        return false
    end
    IssueBuildOrderById(worker, race.wall, x, y)
    return true
end

---@param pi integer
---@return boolean
function AiRaceUsesWaterPoint(pi)
    local race = AiRaceOf(pi)
    return race == nil or race.usesWaterPoint ~= false
end

-- ====================================================================
-- Phase 3: data-driven AI engine (declarative race tables + generic runner).
-- A race may provide `buildings` data; if present the engine is used, else we
-- fall back to the procedural `chooseBuild`. Migrate races one at a time, with
-- the procedural fn kept as a safety net until parity is confirmed.
--
-- def.buildings = {
--   seed = FourCC('h0N2'),                 -- always-present first candidate
--   { FourCC('h0N5'), 4, 4 },              -- { id, limit, power }
--   { FourCC('h0MX'), 8, 6, gate="tier2" },-- optional named gate predicate
-- }
-- def.gates = { tier2 = function(pi) return ... end }   -- race-specific
-- Mirrors ChooseBuildings_* exactly: seed tArray, CheckAndAddBuilding per row
-- (add `power` copies if getAiCount < limit and gate passes), random pick.
-- ====================================================================
---@param pi integer
---@param def table
---@return integer
function AiRunChooseBuildings(pi, def)
    local list = def.buildings
    tArray[0] = 1
    tArray[1] = list.seed
    for _, row in ipairs(list) do
        local gateOk = true
        if row.gate ~= nil then
            local g = def.gates and def.gates[row.gate]
            gateOk = (g == nil) or g(pi)
        end
        if gateOk and getAiCount(pi, row[1]) < row[2] then
            AddBuilding(row[1], row[3])
        end
    end
    return tArray[GetRandomInt(1, tArray[0])]
end

---@param pi integer
---@return integer
function AiDispatchChooseBuild(pi)
    local race = AiRaceOf(pi)
    if race ~= nil then
        if race.buildings ~= nil then
            return AiRunChooseBuildings(pi, race)
        elseif race.chooseBuild ~= nil then
            return race.chooseBuild(pi)
        end
    end
    return 0
end

---@param id integer
---@param pi integer
---@param u unit
function AiDispatchJoin(id, pi, u)
    local race = AiRaceOf(pi)
    if race ~= nil and race.join ~= nil then
        race.join(id, pi, u)
    end
end

-- ====================================================================
-- Phase 3: data-driven production (Perebor) engine.
-- def.production = {
--   [FourCC('h0MY')] = {  -- buildingId → weighted unit pool
--     { FourCC('o04M'), 5 },                      -- { unitId, weight }
--     { FourCC('o05E'), 1, gate = "tier2" },      -- optional named gate
--     { branch = "jt", black = FourCC('o04N'), other = FourCC('o04P'), weight = 4 },
--     { 0, 1 },                                    -- unitId=0 = "train nobody"
--   },
--   worker = { id = FourCC('o04Q'), cap = 18,
--              from = { FourCC('h0N5'), FourCC('h0N1'), FourCC('h0N6') } },
--   pre = function(id, pi, u) ... end,  -- per-building procedural hook
-- }
-- def.branches = { jt = function(pi) return ... end }
-- def.gates   = { tier2 = function(pi) return ... end }
-- ====================================================================
---@param id integer
---@param pi integer
---@param u unit
---@param def table
---@return boolean
function AiRunProduction(id, pi, u, def)
    local prod = def.production
    if not prod then return false end
    local w = prod.worker
    if w and w.from then
        for _, b in ipairs(w.from) do
            if id == b then
                if getAiCount(pi, w.id) < w.cap then
                    IssueImmediateOrderById(u, w.id)
                    return true
                end
                return false
            end
        end
    end
    if prod.pre and prod.pre(id, pi, u) then
        return true
    end
    local rows = prod[id]
    if not rows then return false end
    tArray[0] = 0
    for _, row in ipairs(rows) do
        if row.gate then
            local g = def.gates and def.gates[row.gate]
            if g and not g(pi) then goto continue end
        end
        if row.branch then
            local f = def.branches and def.branches[row.branch]
            local pick = (f and f(pi)) and row.black or row.other
            if pick ~= nil and pick ~= 0 then
                if row.limit and getAiCount(pi, pick) >= row.limit then goto continue end
                AddUnit(pick, row.weight or 1)
            end
        else
            local uid = row[1]
            if uid ~= nil and uid ~= 0 then
                if row.limit and getAiCount(pi, uid) >= row.limit then goto continue end
                AddUnit(uid, row[2] or 1)
            end
        end
        ::continue::
    end
    if tArray[0] > 0 then
        IssueImmediateOrderById(u, tArray[GetRandomInt(1, tArray[0])])
    end
    return true
end

---@param id integer
---@param pi integer
---@param u unit
function AiDispatchPerebor(id, pi, u)
    local race = AiRaceOf(pi)
    if race ~= nil then
        if race.production ~= nil and AiRunProduction(id, pi, u, race) then
            return
        end
        if race.perebor ~= nil then
            race.perebor(id, pi, u)
        end
    end
end

---@param u unit
---@param pi integer
function AiDispatchNaval(u, pi)
    local race = AiRaceOf(pi)
    if race ~= nil and race.naval ~= nil then
        race.naval(u, pi)
    end
end

-- ====================================================================
-- Phase 3: data-driven Strateg (research / techUp) engine.
-- def.strateg = {
--   gradeCap = 100,
--   steps = {
--     { at=17, action="research", rows={{bld,tech,cap},...} },
--     { at=17, action="random", branches={ {{bld,tech,cap},...}, ...} },
--     { at=25, action="techUp", from=bldT1, to=bldT2, cap=3 },
--     { at=45, action="fleet", wall=bldWall },
--     { at=20, action="tryBuy" },
--     { at=60, action="mageTp" },
--     -- gate="name" on any step for conditional execution
--     -- before=N to run when i < N
--   },
-- }
-- def.ecoWeights = { [FourCC('h0N2')]=1, [FourCC('h0N5')]=2, ... }
-- ====================================================================
---@param i integer
---@param pi integer
---@param p player
---@param def table
---@return boolean
function AiRunStrateg(i, pi, p, def)
    local s = def.strategData
    if not s then return false end
    if Grades[pi] >= s.gradeCap then
        warRace(Grades[pi], p)
        return true
    end
    if s.pre and s.pre(i, pi, p) then
    end
    for _, step in ipairs(s.steps) do
        if step.at and i <= step.at then goto cont end
        if step.before and i >= step.before then goto cont end
        if step.gate then
            local g = def.gates and def.gates[step.gate]
            if g and not g(pi) then goto cont end
        end
        local a = step.action
        if a == "research" or a == "random" then
            local rows = step.rows
            if a == "random" and step.branches then
                rows = step.branches[GetRandomInt(1, #step.branches)]
            end
            if rows then
                for _, up in ipairs(rows) do
                    MakeGradeCheckCap(p, up[1], up[2], up[3])
                end
            end
        elseif a == "techUp" then
            if getAiCount(pi, step.to) < step.cap then
                BuildT(p, step.from, step.to)
            end
        elseif a == "fleet" then
            strategFleetGrades(i, p, step.wall)
        elseif a == "tryBuy" then
            if GetPlayerState(p, PLAYER_STATE_RESOURCE_GOLD) > 2000 then
                TryBuy(p, i)
            end
        elseif a == "mageTp" then
            if getAiCount(pi, FourCC('h07A')) < (step.cap or (i / 35)) then
                MakeMageTp(pi)
            end
        end
        ::cont::
    end
    return true
end

---@param id integer
---@param def table
---@return boolean
function AiRunStrategEC(id, def)
    local w = def.ecoWeights
    if not w then return false end
    local add = w[id]
    if add then
        udg_LocalInteger3 = udg_LocalInteger3 + add
        return true
    end
    return false
end

---@param i integer
---@param pi integer
---@param p player
function AiDispatchStrateg(i, pi, p)
    local race = AiRaceOf(pi)
    if race ~= nil then
        if race.strategData ~= nil and AiRunStrateg(i, pi, p, race) then
            return
        end
        if race.strateg ~= nil then
            race.strateg(i, pi, p)
        end
    end
end

---@param id integer
---@param pi integer
function AiDispatchStrategEC(id, pi)
    local race = AiRaceOf(pi)
    if race ~= nil then
        if race.ecoWeights ~= nil and AiRunStrategEC(id, race) then
            return
        end
        if race.strategEC ~= nil then
            race.strategEC(id)
        end
    end
end

---@param id integer
---@param attacker unit
---@param target unit
---@param p player
function AiDispatchAttacker(id, attacker, target, p)
    local pi = GetPlayerId(p)
    local race = AiRaceOf(pi)
    if race ~= nil and race.attacker ~= nil then
        race.attacker(id, attacker, target, p)
    end
end

---@param u unit
---@param pi integer
function AiDispatchAttacked(u, pi)
    local race = AiRaceOf(pi)
    if race ~= nil and race.attacked ~= nil then
        race.attacked(u)
    end
end

---@param u unit
---@param pi integer
function AiDispatchGetLvl(u, pi)
    local race = AiRaceOf(pi)
    if race ~= nil and race.getLvl ~= nil then
        race.getLvl(u)
    end
end

---@param pi integer
---@param id integer
function AiDispatchUpgrade(pi, id)
    local race = AiRaceOf(pi)
    if race ~= nil and race.upgrade ~= nil then
        race.upgrade(pi, id)
    end
end

RegisterAiRace("Scarlet", {
    tokens = {"scarlet", "so"},
    weight = 1,
    start = startScarlet,
    buildings = {
        seed = FourCC('h05Y'),
        { FourCC('h05U'), 4, 4 }, { FourCC('h05Y'), 15, 4 }, { FourCC('h05Z'), 15, 4 },
        { FourCC('h063'), 25, 1 }, { FourCC('h062'), 5, 2 }, { FourCC('h060'), 6, 2 },
        { FourCC('h05X'), 3, 5 },
        { FourCC('h064'), 7, 8, gate = "tier2" }, { FourCC('h061'), 15, 8, gate = "tier2" },
        { FourCC('h068'), 15, 10, gate = "church" },
    },
    gates = {
        tier2 = function(pi) return getAiCount(pi, FourCC('h05V')) + getAiCount(pi, FourCC('h05W')) >= 1 end,
        tier3 = function(pi) return getAiCount(pi, FourCC('h05W')) >= 1 end,
        church = function(pi) return getAiCount(pi, FourCC('h05W')) >= 1 end,
        has_h060 = function(pi) return getAiCount(pi, FourCC('h060')) >= 1 end,
        R040_church = function(pi) return LoadBoolean(AiData, pi, FourCC('R040')) and getAiCount(pi, FourCC('h05W')) >= 1 end,
        R03Z_church = function(pi) return LoadBoolean(AiData, pi, FourCC('R03Z')) and getAiCount(pi, FourCC('h05W')) >= 1 end,
    },
    production = {
        [FourCC('h05Z')] = {
            { FourCC('h03B'), 1 },
            { FourCC('n007'), 1, gate = "has_h060" },
            { FourCC('h039'), 4, gate = "tier2" },
            { FourCC('h066'), 6, gate = "tier3" },
        },
        [FourCC('h064')] = {
            { FourCC('o00I'), 1 },
        },
        [FourCC('h061')] = {
            { FourCC('h067') }, { FourCC('n008') },
        },
        [FourCC('h05X')] = {
            { FourCC('H06C') }, { FourCC('H03H') }, { FourCC('H06B') },
        },
        [FourCC('h068')] = {
            { 0, 1 },
            { FourCC('h03F'), 1, gate = "R040_church" },
            { FourCC('h03D'), 1, gate = "R040_church" },
            { FourCC('h03I'), 1, gate = "R03Z_church" },
            { FourCC('h03G'), 1, gate = "R03Z_church" },
        },
        pre = function(id, pi, u)
            if id == FourCC('h05U') then
                local r = GetRandomInt(1, 3)
                if r == 1 and getAiCount(pi, FourCC('h014')) < 20 then
                    IssueImmediateOrderById(u, FourCC('h014'))
                elseif r == 2 and getAiCount(pi, FourCC('h03C')) < 15 then
                    IssueImmediateOrderById(u, FourCC('h03C'))
                elseif r == 3 and getAiCount(pi, FourCC('h03A')) < 15 then
                    IssueImmediateOrderById(u, FourCC('h03A'))
                end
                return true
            end
            return false
        end,
    },
    ecoWeights = {
        [FourCC('h05Y')] = 1, [FourCC('h05U')] = 2,
        [FourCC('h05V')] = 5, [FourCC('h05W')] = 8,
    },
    strategData = {
        gradeCap = 100,
        pre = function(i, pi, p)
            if i > 65 and getAiCount(pi, FourCC('h05V')) >= 1 then
                local r = GetRandomInt(1, 2)
                if r == 1 then
                    MakeGradeCheckCap(p, FourCC('h05W'), FourCC('R040'), 1)
                    SaveBoolean(AiData, pi, FourCC('R040'), true)
                else
                    MakeGradeCheckCap(p, FourCC('h05W'), FourCC('R03Z'), 1)
                    SaveBoolean(AiData, pi, FourCC('R03Z'), true)
                end
                MakeGradeCheckCap(p, FourCC('h068'), FourCC('R044'), 3)
                MakeGradeCheckCap(p, FourCC('h068'), FourCC('R043'), 3)
                MakeGradeCheckCap(p, FourCC('h068'), FourCC('R042'), 3)
                MakeGradeCheckCap(p, FourCC('h068'), FourCC('R041'), 3)
            end
        end,
        steps = {
            { at = 17, action = "research", rows = {
                {FourCC('h060'), FourCC('R04B'), 6}, {FourCC('h060'), FourCC('R04A'), 6}, {FourCC('h060'), FourCC('R049'), 6}, {FourCC('h060'), FourCC('R048'), 6}, {FourCC('h060'), FourCC('R04C'), 6},
                {FourCC('h062'), FourCC('RHac'), 6}, {FourCC('h062'), FourCC('Rhlh'), 6},
                {FourCC('h05Z'), FourCC('R03K'), 3},
            }},
            { at = 17, action = "tryBuy" },
            { at = 35, gate = "tier2", action = "research", rows = {
                {FourCC('h05Z'), FourCC('R03W'), 2}, {FourCC('h05Z'), FourCC('R03V'), 2},
                {FourCC('h05Z'), FourCC('R03L'), 2}, {FourCC('h05Z'), FourCC('R03M'), 2},
                {FourCC('h061'), FourCC('R03Y'), 3}, {FourCC('h061'), FourCC('R03X'), 3},
            }},
            { at = 35, gate = "tier2", action = "random", branches = {
                { {FourCC('h064'), FourCC('R03T'), 6} },
                { {FourCC('h064'), FourCC('R03S'), 6} },
            }},
            { at = 35, gate = "tier2", action = "research", rows = {
                {FourCC('h064'), FourCC('R047'), 6}, {FourCC('h064'), FourCC('R046'), 6}, {FourCC('h064'), FourCC('R045'), 6}, {FourCC('h064'), FourCC('R03U'), 6},
            }},
            { at = 45, action = "fleet", wall = FourCC('h011') },
            { at = 25, action = "techUp", from = FourCC('h05U'), to = FourCC('h05V'), cap = 3 },
            { at = 55, action = "techUp", from = FourCC('h05V'), to = FourCC('h05W'), cap = 3 },
            { at = 60, action = "mageTp" },
        },
    },
    chooseBuild = ChooseBuildings_ScarletOrden,
    perebor = PereborBuildings_ScarletOrden,
    join = Join_Skarlet,
    strateg = Strateg_Scarlet,
    strategEC = Strateg_Scarlet_EC,
    attacker = Attacker_Skarlet,
    attacked = AttackedScarlet,
    getLvl = GetLvlScarlet,
    upgrade = UpgradeScarlet,
    naval = aiNavalTrain_Common,
    wall = FourCC('h011'),
})

RegisterAiRace("BloodElves", {
    tokens = {"be", "bloodelves", "ek"},
    weight = 1,
    start = startBloodElves,
    buildings = {
        seed = FourCC('h04M'),
        { FourCC('h04C'), 4, 4 }, { FourCC('h04M'), 15, 4 }, { FourCC('h04D'), 15, 4 },
        { FourCC('h04N'), 25, 1 }, { FourCC('h04Q'), 5, 2 }, { FourCC('h04R'), 6, 2 },
        { FourCC('h05J'), 3, 8 },
        { FourCC('h04G'), 15, 8, gate = "tier2" }, { FourCC('h04E'), 15, 8, gate = "tier2" },
        { FourCC('h04F'), 12, 2 },
    },
    gates = {
        tier2 = function(pi) return getAiCount(pi, FourCC('h04B')) + getAiCount(pi, FourCC('h04A')) >= 1 end,
        tier3 = function(pi) return getAiCount(pi, FourCC('h04A')) >= 1 end,
        has_h04R = function(pi) return getAiCount(pi, FourCC('h04R')) >= 1 end,
    },
    production = {
        [FourCC('h04D')] = {
            { FourCC('h03V'), 1 },
            { FourCC('n00I'), 1, gate = "has_h04R" },
            { FourCC('h03X'), 4, gate = "tier2" },
            { FourCC('h03Y'), 6, gate = "tier3" },
        },
        [FourCC('h04G')] = {
            { FourCC('e001'), 1, gate = "tier2" },
            { FourCC('h046'), 2, gate = "tier2" },
            { FourCC('e030'), 1, gate = "tier2" },
            { FourCC('h03Z'), 6, gate = "tier3" },
        },
        [FourCC('h04E')] = {
            { FourCC('h03W') }, { FourCC('h040') }, { FourCC('h041') }, { FourCC('h042') },
        },
        [FourCC('h05J')] = {
            { FourCC('Hjnd') }, { FourCC('H043') }, { FourCC('H045') },
        },
        worker = { id = FourCC('h04K'), cap = 20,
                   from = { FourCC('h04C') } },
    },
    ecoWeights = {
        [FourCC('h04M')] = 1, [FourCC('h04C')] = 2,
        [FourCC('h04B')] = 5, [FourCC('h04A')] = 8,
    },
    strategData = {
        gradeCap = 100,
        steps = {
            { at = 17, action = "random", branches = {
                { {FourCC('h04R'), FourCC('R01L'), 6}, {FourCC('h04R'), FourCC('R01J'), 6}, {FourCC('h04R'), FourCC('R01K'), 6}, {FourCC('h04R'), FourCC('R01M'), 6} },
                { {FourCC('h04R'), FourCC('R01R'), 6}, {FourCC('h04Q'), FourCC('R03I'), 6}, {FourCC('h04Q'), FourCC('R03J'), 6}, {FourCC('h04Q'), FourCC('R01N'), 6} },
                { {FourCC('h04Q'), FourCC('R01T'), 6}, {FourCC('h04Q'), FourCC('R03E'), 6}, {FourCC('h04Q'), FourCC('R03F'), 6}, {FourCC('h04D'), FourCC('R03K'), 1} },
            }},
            { at = 35, gate = "tier2", action = "random", branches = {
                { {FourCC('h04D'), FourCC('R01Y'), 1}, {FourCC('h04D'), FourCC('R01X'), 1}, {FourCC('h04D'), FourCC('R01W'), 2}, {FourCC('h04E'), FourCC('R0BU'), 1}, {FourCC('h04E'), FourCC('R01O'), 6} },
                { {FourCC('h04E'), FourCC('R01P'), 6}, {FourCC('h04E'), FourCC('R01Q'), 6}, {FourCC('h04E'), FourCC('R01S'), 1}, {FourCC('h04G'), FourCC('R03N'), 6}, {FourCC('h04G'), FourCC('R021'), 6} },
                { {FourCC('h04G'), FourCC('R021'), 6}, {FourCC('h04G'), FourCC('R03Q'), 6}, {FourCC('h04G'), FourCC('R021'), 6}, {FourCC('h04G'), FourCC('Rhcd'), 6} },
            }},
            { at = 35, gate = "tier2", action = "random", branches = {
                { {FourCC('h04F'), FourCC('R03R'), 3} },
                { {FourCC('h04F'), FourCC('R01H'), 3} },
                { {FourCC('h04F'), FourCC('R01I'), 3} },
                { {FourCC('h04F'), FourCC('R01G'), 3} },
                { {FourCC('h04F'), FourCC('R01D'), 3} },
            }},
            { at = 45, gate = "tier2", action = "fleet", wall = FourCC('h011') },
            { at = 20, action = "tryBuy" },
            { at = 25, action = "techUp", from = FourCC('h04C'), to = FourCC('h04B'), cap = 3 },
            { at = 55, action = "techUp", from = FourCC('h04B'), to = FourCC('h04A'), cap = 3 },
            { at = 60, action = "mageTp", cap = 3 },
        },
    },
    chooseBuild = ChooseBuildings_BloodElves,
    perebor = PereborBuildings2_BloodElves,
    join = Join_BloodElves,
    strateg = Strateg_BloodElves,
    strategEC = Strateg_BloodElves_EC,
    attacker = Attacker_BloodElves,
    attacked = AttackedBloodElves,
    getLvl = GetLvlBloodElves,
    upgrade = UpgradeBloodElves,
    naval = aiNavalTrain_Common,
    wall = FourCC('h011'),
})

RegisterAiRace("Goblins", {
    tokens = {"goblins", "gob"},
    weight = 1,
    start = startGoblins,
    buildings = {
        seed = FourCC('h077'),
        { FourCC('h070'), 4, 5 }, { FourCC('h077'), 20, 3 }, { FourCC('h073'), 18, 7 },
        { FourCC('h07S'), 30, 1 }, { FourCC('h079'), 5, 3 }, { FourCC('h076'), 18, 4 },
        { FourCC('o016'), 3, 8 },
        { FourCC('h074'), 15, 2, gate = "grades8" }, { FourCC('h075'), 15, 2, gate = "grades8" },
    },
    gates = {
        grades8 = function(pi) return Grades[pi] > 8 end,
    },
    production = {
        [FourCC('h070')] = {
            { FourCC('n00V'), 2, limit = 25 },
        },
        [FourCC('h074')] = {
            { FourCC('h06S'), 2 }, { FourCC('h06U'), 2 },
            { FourCC('h06Y'), 4 }, { FourCC('h06R'), 3 }, { FourCC('h06T'), 3 },
        },
        [FourCC('h075')] = {
            { FourCC('o00W'), 2 }, { FourCC('o00Y'), 2 },
            { FourCC('o00X'), 3 }, { FourCC('h06P'), 3 },
        },
        [FourCC('o016')] = {
            { FourCC('H0BD'), 1, limit = 1 },
            { FourCC('Galh'), 1, limit = 1 },
            { FourCC('Gmex'), 1, limit = 1 },
        },
        pre = function(id, pi, u)
            if id == FourCC('h073') then
                if Random(1, 6) then
                    IssueNeutralImmediateOrderById(Player(pi), u, FourCC('h07R'))
                else
                    return false
                end
                return true
            end
            return false
        end,
        [FourCC('h073')] = {
            { FourCC('h06K'), 2 },
            { FourCC('h060'), 1, gate = "grades8" },
            { FourCC('h06Q'), 3, gate = "grades8" },
            { FourCC('h06L'), 3, gate = "grades8" },
            { FourCC('h06N'), 3, gate = "grades8" },
            { FourCC('h078'), 3, gate = "grades8" },
            { FourCC('h06M'), 3, gate = "grades8" },
        },
    },
    ecoWeights = {
        [FourCC('h077')] = 1, [FourCC('h070')] = 4,
    },
    strategData = {
        gradeCap = 150,
        steps = {
            { at = 17, action = "research", rows = {
                {FourCC('h076'), FourCC('R04P'), 6}, {FourCC('h076'), FourCC('R04E'), 6}, {FourCC('h076'), FourCC('R04F'), 6}, {FourCC('h076'), FourCC('R04G'), 6}, {FourCC('h076'), FourCC('R04H'), 6},
                {FourCC('h076'), FourCC('R04I'), 6}, {FourCC('h076'), FourCC('R04J'), 6}, {FourCC('h076'), FourCC('R04K'), 6}, {FourCC('h076'), FourCC('R04L'), 6}, {FourCC('h076'), FourCC('R04M'), 6},
                {FourCC('h079'), FourCC('R056'), 6}, {FourCC('h079'), FourCC('R07A'), 6}, {FourCC('h079'), FourCC('R05X'), 6}, {FourCC('h079'), FourCC('R05Y'), 6}, {FourCC('h079'), FourCC('R04N'), 6},
                {FourCC('h079'), FourCC('R04Q'), 6}, {FourCC('h079'), FourCC('R04R'), 6}, {FourCC('h079'), FourCC('R053'), 6}, {FourCC('h079'), FourCC('R05W'), 6},
                {FourCC('h070'), FourCC('R0D4'), 6},
            }},
            { at = 17, action = "tryBuy" },
            { at = 60, action = "mageTp" },
        },
    },
    chooseBuild = ChooseBuildings_Goblins,
    perebor = PereborBuildings_Goblins,
    join = Join_Goblins,
    strateg = Strateg_Goblins,
    strategEC = Strateg_Goblins_EC,
    attacker = Attacker_Goblins,
    attacked = AttackedGoblins,
    getLvl = GetLvlGoblins,
    naval = aiNavalTrain_Goblins,
    wall = FourCC('h0D7'),
})

RegisterAiRace("Naga", {
    tokens = {"naga"},
    weight = 1,
    start = startNaga,
    buildings = {
        seed = FourCC('nnfm'),
        { FourCC('nntt'), 3, 5 }, { FourCC('nnfm'), 20, 4 }, { FourCC('nnsg'), 18, 6 },
        { FourCC('nntg'), 30, 1 }, { FourCC('h0JW'), 5, 2 }, { FourCC('nnad'), 3, 6 },
        { FourCC('nnsa'), 15, 2 }, { FourCC('n055'), 15, 3 },
    },
    chooseBuild = ChooseBuildings_Naga,
    perebor = PereborBuildings_Naga,
    production = {
        [FourCC('nnsg')] = {
            { FourCC('n04Z'), 2 },
            { FourCC('nsnp'), 2, gate = "has_h0JW" },
            { FourCC('nhyc'), 1, gate = "has_h0JX" },
            { branch = "murloc", black = FourCC('n052'), other = FourCC('nmyr'), weight = 3, gate = "has_h0JX" },
        },
        [FourCC('nnsa')] = {
            { FourCC('n053'), 6, gate = "murloc_h0JX" },
            { FourCC('n054'), 6, gate = "murloc_h0JX" },
            { FourCC('n051'), 1, gate = "naga_h0JX" },
            { FourCC('nnsw'), 4, gate = "naga_h0JX" },
        },
        [FourCC('n055')] = {
            { branch = "murloc", black = FourCC('n050'), other = FourCC('nnrg'), weight = 2, gate = "has_h0JY" },
            { FourCC('n056'), 1, gate = "has_h0JY" },
            { FourCC('nwgs'), 1 },
        },
        [FourCC('nnad')] = {
            { FourCC('N07A'), 1, limit = 1 },
            { FourCC('H0JV'), 1, limit = 1 },
            { branch = "murloc", black = FourCC('H0OZ'), other = FourCC('H0JU'), weight = 1, limit = 1 },
        },
        worker = { id = FourCC('nmpe'), cap = 25,
                   from = { FourCC('nntt'), FourCC('h0JX'), FourCC('h0JY') } },
        pre = function(id, pi, u)
            if id == FourCC('nntt') or id == FourCC('h0JX') or id == FourCC('h0JY') then
                if getAiCount(pi, FourCC('nmpe')) >= 25 and GetRandomInt(1, 2) == 1 then
                    IssueImmediateOrderById(u, FourCC('nnmg'))
                    return true
                end
                return false
            end
            return false
        end,
    },
    gates = {
        has_h0JW = function(pi) return getAiCount(pi, FourCC('h0JW')) > 0 end,
        has_h0JX = function(pi) return getAiCount(pi, FourCC('h0JX')) > 0 end,
        has_h0JY = function(pi) return getAiCount(pi, FourCC('h0JY')) > 0 end,
        murloc = function(pi) return GetPlayerTechResearched(Player(pi), FourCC('R0FF'), true) end,
        naga = function(pi) return not GetPlayerTechResearched(Player(pi), FourCC('R0FF'), true) end,
        murloc_h0JX = function(pi) return GetPlayerTechResearched(Player(pi), FourCC('R0FF'), true) and getAiCount(pi, FourCC('h0JX')) > 0 end,
        naga_h0JX = function(pi) return not GetPlayerTechResearched(Player(pi), FourCC('R0FF'), true) and getAiCount(pi, FourCC('h0JX')) > 0 end,
    },
    branches = {
        murloc = function(pi) return GetPlayerTechResearched(Player(pi), FourCC('R0FF'), true) end,
    },
    ecoWeights = {
        [FourCC('nnfm')] = 1, [FourCC('nntt')] = 4,
        [FourCC('h0JX')] = 6, [FourCC('h0JY')] = 8,
    },
    strategData = {
        gradeCap = 150,
        steps = {
            { before = 50, action = "research", rows = {
                {FourCC('nntt'), FourCC('R0FE'), 1}, {FourCC('nntt'), FourCC('R0FF'), 1},
            }},
            { at = 17, action = "research", rows = {
                {FourCC('h0JW'), FourCC('R0FD'), 6}, {FourCC('h0JW'), FourCC('R0FH'), 6}, {FourCC('h0JW'), FourCC('Rnat'), 6}, {FourCC('h0JW'), FourCC('Rnam'), 6}, {FourCC('h0JW'), FourCC('Rnsb'), 6},
                {FourCC('nnsa'), FourCC('Rnsw'), 6}, {FourCC('nnsa'), FourCC('Rnsi'), 6},
                {FourCC('nnsg'), FourCC('R0FR'), 6}, {FourCC('nnsg'), FourCC('Rnen'), 6},
            }},
            { at = 17, action = "tryBuy" },
            { at = 25, action = "techUp", from = FourCC('nntt'), to = FourCC('h0JX'), cap = 3 },
            { at = 55, action = "techUp", from = FourCC('h0JX'), to = FourCC('h0JY'), cap = 3 },
            { at = 60, action = "mageTp" },
        },
    },
    join = Join_Naga,
    strateg = Strateg_Naga,
    strategEC = Strateg_Naga_EC,
    attacker = Attacker_Naga,
    attacked = AttackedNaga,
    getLvl = GetLvlNaga,
    upgrade = UpgradeNaga,
    naval = aiNavalTrain_Naga,
    wall = FourCC('n04L'),
    usesWaterPoint = false,
})

RegisterAiRace("Horde", {
    tokens = {"horde"},
    weight = 1,
    start = startHorde,
    buildings = {
        seed = FourCC('otrb'),
        { FourCC('ogre'), 3, 5 }, { FourCC('otrb'), 20, 3 }, { FourCC('obar'), 3, 7 },
        { FourCC('obar'), 18, 3 }, { FourCC('obea'), 18, 2 }, { FourCC('owtw'), 30, 1 },
        { FourCC('ofor'), 5, 3 }, { FourCC('oalt'), 3, 6 },
        { FourCC('osld'), 15, 10, gate = "spirit" }, { FourCC('otto'), 15, 10, gate = "spirit" },
        { FourCC('osld'), 15, 1 }, { FourCC('otto'), 15, 1 }, { FourCC('ovln'), 1, 6 },
    },
    gates = {
        spirit = function(pi) return getAiCount(pi, FourCC('ostr')) + getAiCount(pi, FourCC('ofrt')) > 0 end,
        ironHorde = function(pi) return GetPlayerTechResearched(Player(pi), FourCC('R0EA'), true) end,
        notIronHorde = function(pi) return not GetPlayerTechResearched(Player(pi), FourCC('R0EA'), true) end,
        spirit_notIron = function(pi) return not GetPlayerTechResearched(Player(pi), FourCC('R0EA'), true) and getAiCount(pi, FourCC('ostr')) + getAiCount(pi, FourCC('ofrt')) > 0 end,
        fortress = function(pi) return getAiCount(pi, FourCC('ofrt')) > 0 end,
    },
    production = {
        [FourCC('obar')] = {
            { FourCC('o01N'), 2, gate = "ironHorde" },
            { FourCC('ogru'), 2, gate = "notIronHorde" },
            { FourCC('o029'), 3, gate = "spirit_notIron" },
            { FourCC('orai'), 5, gate = "fortress" },
            { FourCC('otau'), 5, gate = "fortress" },
        },
        [FourCC('obea')] = {
            { FourCC('o02B'), 2, gate = "ironHorde" },
            { FourCC('ohun'), 2, gate = "notIronHorde" },
            { FourCC('o01P'), 3, gate = "spirit_notIron" },
            { FourCC('okod'), 5, gate = "fortress" },
        },
        [FourCC('osld')] = {
            { FourCC('oshm'), 8 },
            { FourCC('o01W'), 2 },
        },
        [FourCC('otto')] = {
            { FourCC('ocat'), 2 },
            { FourCC('o022'), 1 },
            { FourCC('h0CY'), 2, gate = "ironHorde" },
        },
        [FourCC('oalt')] = {
            { FourCC('Ofar'), 1, limit = 1 },
            { FourCC('Obla'), 1, limit = 1 },
            { FourCC('Otch'), 1, limit = 1 },
        },
        worker = { id = FourCC('opeo'), cap = 25,
                   from = { FourCC('ogre'), FourCC('ostr'), FourCC('ofrt') } },
    },
    ecoWeights = {
        [FourCC('nnfm')] = 1, [FourCC('ogre')] = 4,
        [FourCC('ostr')] = 6, [FourCC('ofrt')] = 8,
    },
    strategData = {
        gradeCap = 150,
        steps = {
            { before = 50, action = "research", rows = {
                {FourCC('nntt'), FourCC('R0FE'), 1}, {FourCC('nntt'), FourCC('R0FF'), 1},
            }},
            { at = 17, action = "research", rows = {
                {FourCC('ogre'), FourCC('Ropg'), 1},
                {FourCC('ofor'), FourCC('R0G5'), 6}, {FourCC('ofor'), FourCC('R0E6'), 6}, {FourCC('ofor'), FourCC('Rome'), 6}, {FourCC('ofor'), FourCC('Roar'), 6}, {FourCC('ofor'), FourCC('Rora'), 6}, {FourCC('ofor'), FourCC('Rosp'), 3}, {FourCC('ofor'), FourCC('Rorb'), 3},
                {FourCC('obar'), FourCC('R0EC'), 3}, {FourCC('obea'), FourCC('R0ED'), 3}, {FourCC('otto'), FourCC('R0EF'), 3},
                {FourCC('osld'), FourCC('Rost'), 3}, {FourCC('osld'), FourCC('Rowt'), 3}, {FourCC('osld'), FourCC('Rowd'), 3},
            }},
            { at = 17, action = "tryBuy" },
            { at = 17, action = "fleet", wall = FourCC('h0HO') },
            { action = "random", branches = {
                { {FourCC('ovln'), FourCC('R0F3'), 1}, {FourCC('ovln'), FourCC('R0F4'), 1}, {FourCC('ovln'), FourCC('R0EH'), 1}, {FourCC('ovln'), FourCC('R0EI'), 1} },
                { {FourCC('ovln'), FourCC('R0EE'), 1}, {FourCC('ovln'), FourCC('R0EA'), 1}, {FourCC('ovln'), FourCC('R0E9'), 1}, {FourCC('ovln'), FourCC('R0E5'), 1} },
                { {FourCC('ovln'), FourCC('R0E4'), 1}, {FourCC('ovln'), FourCC('R0E3'), 1}, {FourCC('ovln'), FourCC('R0E1'), 1}, {FourCC('ovln'), FourCC('R0E0'), 1} },
                { {FourCC('ovln'), FourCC('R0DZ'), 1}, {FourCC('ovln'), FourCC('R0DY'), 1}, {FourCC('ovln'), FourCC('R0DX'), 1}, {FourCC('ovln'), FourCC('R0DW'), 1} },
                { {FourCC('ovln'), FourCC('R0EB'), 1}, {FourCC('ovln'), FourCC('R0EH'), 1}, {FourCC('ovln'), FourCC('R0DZ'), 1}, {FourCC('ovln'), FourCC('R0E5'), 1} },
            }},
        },
    },
    chooseBuild = ChooseBuildings_Horde,
    perebor = PereborBuildings_Horde,
    join = Join_Horde,
    strateg = Strateg_Horde,
    strategEC = Strateg_Horde_EC,
    attacker = Attacker_Goblins,
    attacked = AttackedNaga,
    getLvl = GetLvlHorde,
    upgrade = UpgradeHorde,
    naval = aiNavalTrain_Horde,
    wall = FourCC('h0HO'),
})

RegisterAiRace("JungleTrolls", {
    tokens = {"jt", "jungletrolls", "trolls"},
    weight = 1,
    start = startJungleTrolls,
    -- Phase 3 declarative build order (engine: AiRunChooseBuildings). Mirrors
    -- ChooseBuildings_JungleTrolls exactly. chooseBuild kept as fallback.
    buildings = {
        seed = FourCC('h0N2'),
        { FourCC('h0N5'), 4, 4 },
        { FourCC('h0N2'), 18, 4 },
        { FourCC('h0MY'), 10, 4 },
        { FourCC('h0N3'), 5, 2 },
        { FourCC('h0N0'), 3, 6 },
        { FourCC('h0MX'), 8, 6, gate = "tier2" },
        { FourCC('h0MW'), 8, 6, gate = "tier2" },
        { FourCC('h0D3'), 2, 1, gate = "tier2" },
    },
    gates = {
        tier2 = function(pi)
            return getAiCount(pi, FourCC('h0N1')) + getAiCount(pi, FourCC('h0N6')) >= 1
        end,
        tier3 = function(pi)
            return getAiCount(pi, FourCC('h0N6')) >= 1
        end,
    },
    -- Phase 3 declarative production (engine: AiRunProduction).
    production = {
        [FourCC('h0MY')] = {
            { FourCC('o04M'), 5 },
            { FourCC('o04L'), 4 },
            { FourCC('o05E'), 1, gate = "tier2" },
        },
        [FourCC('h0MX')] = {
            { FourCC('o04O'), 3 },
            { FourCC('o04R'), 3 },
            { branch = "jt", black = FourCC('o04N'), other = FourCC('o04P'), weight = 4 },
        },
        [FourCC('h0MW')] = {
            { FourCC('o04S'), 3 },
            { FourCC('o04U'), 4 },
            { FourCC('o05J'), 2, gate = "tier2" },
            { FourCC('o05G'), 2, gate = "tier3" },
        },
        [FourCC('h0N0')] = {
            { FourCC('O054') }, { FourCC('O05A') }, { FourCC('O05D') },
            { branch = "jt", black = FourCC('O05L'), other = FourCC('O055') },
        },
        worker = { id = FourCC('o04Q'), cap = 18,
                   from = { FourCC('h0N5'), FourCC('h0N1'), FourCC('h0N6') } },
    },
    branches = {
        jt = function(pi) return JungleTrollsBranchIsBlack(pi) end,
    },
    -- Phase 3 declarative strategy (engine: AiRunStrateg).
    ecoWeights = {
        [FourCC('h0N2')] = 1,
        [FourCC('h0N5')] = 2,
        [FourCC('h0N1')] = 5,
        [FourCC('h0N6')] = 8,
    },
    strategData = {
        gradeCap = 100,
        steps = {
            { at = 17, action = "random", branches = {
                { {FourCC('h0N3'), FourCC('R0I8'), 6}, {FourCC('h0N3'), FourCC('R0I9'), 6}, {FourCC('h0N3'), FourCC('R0IA'), 6}, {FourCC('h0N3'), FourCC('R0II'), 2} },
                { {FourCC('h0MY'), FourCC('R0IK'), 6}, {FourCC('h0MY'), FourCC('R0IM'), 6}, {FourCC('h0N2'), FourCC('R0IJ'), 6} },
                { {FourCC('h0MX'), FourCC('R0IB'), 6}, {FourCC('h0MX'), FourCC('R0IC'), 6}, {FourCC('h0MX'), FourCC('R0ID'), 6} },
                { {FourCC('h0MW'), FourCC('R0IL'), 6}, {FourCC('h0MW'), FourCC('R0IN'), 6}, {FourCC('h0MW'), FourCC('R0IJ'), 6} },
            }},
            { at = 45, action = "fleet", wall = FourCC('h0D3') },
            { at = 20, action = "tryBuy" },
            { at = 25, action = "techUp", from = FourCC('h0N5'), to = FourCC('h0N1'), cap = 3 },
            { at = 55, action = "techUp", from = FourCC('h0N1'), to = FourCC('h0N6'), cap = 3 },
        },
    },
    chooseBuild = ChooseBuildings_JungleTrolls,
    perebor = PereborBuildings2_JungleTrolls,
    join = Join_JungleTrolls,
    strateg = Strateg_JungleTrolls,
    strategEC = Strateg_JungleTrolls_EC,
    attacker = Attacker_JungleTrolls,
    attacked = AttackedJungleTrolls,
    getLvl = GetLvlJungleTrolls,
    upgrade = UpgradeJungleTrolls,
    naval = aiNavalTrain_JungleTrolls,
    wall = FourCC('h0N2'),
})

-- ====================================================================
-- ForestTrolls (Phase 3 data-driven)
-- TODO: verify building/unit mappings and research assignments
-- ====================================================================
---@param id integer
---@param pi integer
---@param u unit
---@return nothing
function Join_ForestTrolls(id, pi, u)
    if id == FourCC('o04V') then
        GroupAddUnit(udg_Ai_builders[pi], u)
    elseif aiUnitJoinsCapitalGuard(u, pi) then
    else
        aiUnitJoinsArmy(u, pi)
    end
end

RegisterAiRace("ForestTrolls", {
    tokens = {"ft", "foresttrolls"},
    weight = 1,
    start = startForestTrolls,
    buildings = {
        seed = FourCC('h0MV'),
        { FourCC('h0MT'), 4, 4 }, { FourCC('h0MV'), 18, 4 },
        { FourCC('h0MS'), 10, 4 }, { FourCC('h0N7'), 5, 2 },
        { FourCC('h0MU'), 3, 6 }, { FourCC('h0N4'), 25, 1 },
        { FourCC('h0MZ'), 8, 6, gate = "tier2" },
        { FourCC('h0MR'), 8, 6, gate = "tier2" },
    },
    gates = {
        tier2 = function(pi)
            return getAiCount(pi, FourCC('h0N8')) + getAiCount(pi, FourCC('h0N9')) >= 1
        end,
    },
    production = {
        [FourCC('h0MS')] = {
            { FourCC('o04W'), 5 },
            { FourCC('o053'), 4 },
            { FourCC('o04Z'), 3, gate = "tier2" },
            { FourCC('o04Y'), 3, gate = "tier2" },
        },
        [FourCC('h0MZ')] = {
            { FourCC('o051'), 3 },
            { FourCC('o052'), 3 },
            { FourCC('o064'), 2 },
        },
        [FourCC('h0MR')] = {
            { FourCC('o050'), 4 },
            { FourCC('o05F'), 2, gate = "tier2" },
        },
        [FourCC('h0MU')] = {
            { FourCC('O059') }, { FourCC('O056') },
            { FourCC('O058') }, { FourCC('O057') },
        },
        worker = { id = FourCC('o04V'), cap = 20,
                   from = { FourCC('h0MT'), FourCC('h0N8'), FourCC('h0N9') } },
    },
    ecoWeights = {
        [FourCC('h0MV')] = 1, [FourCC('h0MT')] = 2,
        [FourCC('h0N8')] = 5, [FourCC('h0N9')] = 8,
    },
    strategData = {
        gradeCap = 100,
        steps = {
            { at = 17, action = "random", branches = {
                { {FourCC('h0N7'), FourCC('R0D2'), 6}, {FourCC('h0N7'), FourCC('R0D3'), 6} },
                { {FourCC('h0MS'), FourCC('R0DY'), 6}, {FourCC('h0MS'), FourCC('R0EE'), 6} },
                { {FourCC('h0MZ'), FourCC('R0EH'), 6}, {FourCC('h0MZ'), FourCC('R0EI'), 6} },
            }},
            { at = 20, action = "tryBuy" },
            { at = 25, action = "techUp", from = FourCC('h0MT'), to = FourCC('h0N8'), cap = 3 },
            { at = 55, action = "techUp", from = FourCC('h0N8'), to = FourCC('h0N9'), cap = 3 },
        },
    },
    join = Join_ForestTrolls,
    naval = aiNavalTrain_JungleTrolls,
    wall = FourCC('h0N4'),
})
