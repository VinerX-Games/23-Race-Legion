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

---@param id integer
---@param pi integer
---@param u unit
function AiDispatchPerebor(id, pi, u)
    local race = AiRaceOf(pi)
    if race ~= nil and race.perebor ~= nil then
        race.perebor(id, pi, u)
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

---@param id integer
---@param pi integer
function AiDispatchStrategEC(id, pi)
    local race = AiRaceOf(pi)
    if race ~= nil and race.strategEC ~= nil then
        race.strategEC(id)
    end
end

---@param i integer
---@param pi integer
---@param p player
function AiDispatchStrateg(i, pi, p)
    local race = AiRaceOf(pi)
    if race ~= nil and race.strateg ~= nil then
        race.strateg(i, pi, p)
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
        church = function(pi) return getAiCount(pi, FourCC('h05W')) >= 1 end,
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
