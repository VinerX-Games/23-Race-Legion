-- Split AI race definition: Elementals

---@param pi integer
---@return nothing
function startElementals(pi)
    local p = Player(pi)
    CreateNUnitsAtLoc(5, FourCC('e00F'), p, udg_LocalPoint, bj_UNIT_FACING)
    GroupAddGroup(GetLastCreatedGroup(), udg_Ai_units[pi])
    GroupAddGroup(GetLastCreatedGroup(), udg_Ai_builders[pi])
    CreateNUnitsAtLoc(1, FourCC('h0EQ'), p, udg_LocalPoint, bj_UNIT_FACING)
    GroupAddUnit(udg_Ai_units[pi], GetLastCreatedUnit())
    GroupAddUnit(udg_Ai_buildings[pi], GetLastCreatedUnit())
    NumberSet(pi, FourCC('e00F'), 5)
    NumberSet(pi, FourCC('h0EQ'), 1)
    AiData[pi][StringHash("Race")] = "EL"
    SetPlayerTechResearchedSwap(FourCC('R0A2'), 1, p)
    SetPlayerName(p, "Elementals (" .. I2S(pi + 1) .. ")")
    ElemOn()
    AiRace[pi] = "Elementals"
    ProbeLogWrite("[AI] startElementals pi=" .. tostring(pi) .. " workers=5e00F building=1h0EQ")
end

---@param id integer
---@param pi integer
---@param u unit
---@return nothing
function Join_Elementals(id, pi, u)
    if id == FourCC('e00F') then
        GroupAddUnit(udg_Ai_builders[pi], u)
    elseif aiUnitJoinsCapitalGuard(u, pi) then
    else
        aiUnitJoinsArmy(u, pi)
    end
end

RegisterAiRace("Elementals", {

    tokens = {"element", "elemental", "elementals", "elem"},

    weight = 1,

    altar = FourCC('h0EY'),

    start = startElementals,

    buildings = {

        seed = FourCC('h0EQ'),

        { FourCC('h0EQ'), 1, 4 },
        { FourCC('h0ER'), 3, 5 },
        { FourCC('h0ES'), 3, 6 },
        { FourCC('h0EO'), 8, 4 },
        { FourCC('h0EP'), 2, 1 },
        { FourCC('h0ET'), 8, 4 },
        { FourCC('h0EU'), 8, 4 },
        { FourCC('h0EV'), 4, 2 },
        { FourCC('h0EW'), 8, 4 },
        { FourCC('h0EX'), 4, 2 },
        { FourCC('h0EY'), 3, 6 },

    },

    gates = {

        tier2 = function(pi) return getAiCount(pi, FourCC('h0ER')) >= 1 or getAiCount(pi, FourCC('h0ES')) >= 1 end,
        tier3 = function(pi) return getAiCount(pi, FourCC('h0ES')) >= 1 end,
        tier3_fire = function(pi) return getAiCount(pi, FourCC('h0ES')) >= 1 and getAiCount(pi, FourCC('h0EO')) >= 1 end,
        tier3_water = function(pi) return getAiCount(pi, FourCC('h0ES')) >= 1 and getAiCount(pi, FourCC('h0ET')) >= 1 end,

    },

    production = {

        worker = { id = FourCC('e00F'), cap = 18, from = {
            FourCC('h0EQ'),
            FourCC('h0ER'),
            FourCC('h0ES'),
        } },

        [FourCC('h0EO')] = {
            { FourCC('n02R'), 4 },
            { FourCC('n02S'), 3, gate = "tier2" },
            { FourCC('n036'), 2, gate = "tier2" },
            { FourCC('h0F1'), 1, gate = "tier3_fire" },
            { FourCC('n07O'), 1, gate = "tier3_fire" },
        },

        [FourCC('h0ET')] = {
            { FourCC('n02U'), 4 },
            { FourCC('n02T'), 3, gate = "tier2" },
            { FourCC('n02Z'), 2, gate = "tier2" },
            { FourCC('n07C'), 2, gate = "tier2" },
            { FourCC('n032'), 1, gate = "tier3_water" },
            { FourCC('n07T'), 1, gate = "tier3_water" },
        },

        [FourCC('h0EU')] = {
            { FourCC('n02Q'), 4 },
            { FourCC('n02V'), 3, gate = "tier2" },
            { FourCC('n07P'), 2, gate = "tier2" },
            { FourCC('n02P'), 1, gate = "tier3" },
            { FourCC('n07R'), 1, gate = "tier3" },
            { FourCC('n07U'), 1, gate = "tier3" },
        },

        [FourCC('h0EW')] = {
            { FourCC('n02W'), 4 },
            { FourCC('n02X'), 3, gate = "tier2" },
            { FourCC('n07V'), 2, gate = "tier2" },
            { FourCC('n02Y'), 1, gate = "tier3" },
            { FourCC('n031'), 1, gate = "tier3" },
            { FourCC('n033'), 1, gate = "tier3" },
            { FourCC('n034'), 1, gate = "tier3_fire" },
            { FourCC('n035'), 1, gate = "tier3_water" },
            { FourCC('n07N'), 1, gate = "tier3_fire" },
            { FourCC('n07Q'), 1, gate = "tier3" },
            { FourCC('n07S'), 1, gate = "tier3" },
        },

        [FourCC('h0ES')] = {
            { FourCC('n07W'), 1, limit = 1 },
            { FourCC('n07X'), 1, limit = 1 },
            { FourCC('n07Y'), 1, limit = 1 },
            { FourCC('n07Z'), 1, limit = 1 },
        },

        [FourCC('h0EY')] = {
            { FourCC('H0EZ'), 1, limit = 1 },
            { FourCC('H0F0'), 1, limit = 1 },
            { FourCC('N037'), 1, limit = 1 },
        },

    },

    ecoWeights = {

        [FourCC('h0EQ')] = 1,
        [FourCC('h0ER')] = 5,
        [FourCC('h0ES')] = 8,

    },

    strategData = {

        gradeCap = 100,

        steps = {
            { at = 17, action = "research", rows = {
                { FourCC('h0EV'), FourCC('R09G'), 6 },
                { FourCC('h0EV'), FourCC('R09H'), 6 },
                { FourCC('h0EV'), FourCC('R09I'), 6 },
                { FourCC('h0EV'), FourCC('R09J'), 6 },
            }},
            { at = 20, action = "tryBuy" },
            { at = 25, action = "techUp", from = FourCC('h0EQ'), to = FourCC('h0ER'), cap = 3 },
            { at = 55, action = "techUp", from = FourCC('h0ER'), to = FourCC('h0ES'), cap = 3 },
        },

    },

    join = Join_Elementals,

    wall = FourCC('h0EP'),

    diplomat = "balanced",

    brain = "objective",

    brainWeights = {
        kind  = { capital = 100, cluster = 40, capture = 60, weak = 20, front = 15 },
        value = 1.0, dist = 0.002, claim = 25.0, siege = 0.5,
        focusMargin = 30.0, homeThreat = 20.0, tpDist = 6000.0,
        rHome = 2500.0, rCluster = 1600.0,
        clusterEvery = 8, topK = 8,
    },
    compTarget = {
        [FourCC('e00F')] = 0.2000,
        [FourCC('n02R')] = 0.1000,
        [FourCC('n02U')] = 0.1000,
        [FourCC('n02Q')] = 0.1000,
        [FourCC('n02W')] = 0.1000,
        [FourCC('n02S')] = 0.0600,
        [FourCC('n02T')] = 0.0600,
        [FourCC('n02V')] = 0.0600,
        [FourCC('n02X')] = 0.0600,
        [FourCC('n07W')] = 0.0200,
        [FourCC('n07X')] = 0.0200,
        [FourCC('n07Y')] = 0.0200,
        [FourCC('n07Z')] = 0.0200,
        [FourCC('H0EZ')] = 0.0100,
        [FourCC('H0F0')] = 0.0100,
        [FourCC('N037')] = 0.0100,
    },
})
