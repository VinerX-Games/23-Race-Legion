-- Split AI race definition: Dragons

---@param pi integer
---@return nothing
function startDragons(pi)
    local p = Player(pi)
    CreateNUnitsAtLoc(5, FourCC('o01D'), p, udg_LocalPoint, bj_UNIT_FACING)
    GroupAddGroup(GetLastCreatedGroup(), udg_Ai_units[pi])
    GroupAddGroup(GetLastCreatedGroup(), udg_Ai_builders[pi])
    CreateNUnitsAtLoc(1, FourCC('dra0'), p, udg_LocalPoint, bj_UNIT_FACING)
    GroupAddUnit(udg_Ai_units[pi], GetLastCreatedUnit())
    GroupAddUnit(udg_Ai_buildings[pi], GetLastCreatedUnit())
    NumberSet(pi, FourCC('o01D'), 5)
    NumberSet(pi, FourCC('dra0'), 1)
    AiData[pi][StringHash("Race")] = "DR"
    SetPlayerTechResearchedSwap(FourCC('R0BY'), 1, p)
    SetPlayerName(p, "Dragons (" .. I2S(pi + 1) .. ")")
    DragonsOn()
    AiRace[pi] = "Dragons"
    ProbeLogWrite("[AI] startDragons pi=" .. tostring(pi) .. " workers=5o01D building=1dra0")
end

---@param id integer
---@param pi integer
---@param u unit
---@return nothing
function Join_Dragons(id, pi, u)
    if id == FourCC('o01D') then
        GroupAddUnit(udg_Ai_builders[pi], u)
    elseif id == FourCC('h0D9') or id == FourCC('h0DA') or id == FourCC('h0DB') then
        GroupAddUnit(udg_Ai_navy[pi], u)
        NumberAdd(pi, StringHash("NumberN"))
    elseif aiUnitJoinsCapitalGuard(u, pi) then
    else
        aiUnitJoinsArmy(u, pi)
    end
end

RegisterAiRace("Dragons", {

    tokens = {"dragon", "dragons"},

    weight = 1,

    altar = FourCC('n03Z'),

    start = startDragons,

    buildings = {

        seed = FourCC('dra0'),

        { FourCC('dra0'), 1, 4 },
        { FourCC('h0F9'), 6, 2 },
        { FourCC('n03I'), 4, 1 },
        { FourCC('n03Z'), 4, 4 },
        { FourCC('n041'), 4, 4 },
        { FourCC('n042'), 4, 4 },
        { FourCC('n043'), 4, 4 },
        { FourCC('n044'), 2, 2 },
        { FourCC('h0D8'), 2, 1 },

    },

    production = {

        worker = { id = FourCC('o01D'), cap = 12, from = {
            FourCC('dra0'),
            FourCC('n03Z'),
            FourCC('n041'),
            FourCC('n042'),
            FourCC('n043'),
            FourCC('n044'),
        } },

        [FourCC('dra0')] = {
            { FourCC('n03F'), 3 },
        },

        [FourCC('n03Z')] = {
            { FourCC('N040'), 1, limit = 1 },
            { FourCC('n03Q'), 4 },
            { FourCC('n03R'), 3 },
            { FourCC('n03S'), 2 },
        },

        [FourCC('n041')] = {
            { FourCC('N047'), 1, limit = 1 },
            { FourCC('n03T'), 4 },
            { FourCC('n03U'), 3 },
            { FourCC('n03V'), 2 },
        },

        [FourCC('n042')] = {
            { FourCC('N046'), 1, limit = 1 },
            { FourCC('n03K'), 4 },
            { FourCC('n03L'), 3 },
            { FourCC('n03M'), 2 },
        },

        [FourCC('n043')] = {
            { FourCC('N045'), 1, limit = 1 },
            { FourCC('n03W'), 4 },
            { FourCC('n03X'), 3 },
            { FourCC('n03Y'), 2 },
        },

        [FourCC('n044')] = {
            { FourCC('n03N'), 4 },
            { FourCC('n03O'), 3 },
            { FourCC('n03P'), 2 },
            { FourCC('n05Q'), 2 },
        },

    },

    ecoWeights = {

        [FourCC('dra0')] = 2,
        [FourCC('h0F9')] = 1,
        [FourCC('n03Z')] = 4,
        [FourCC('n041')] = 4,
        [FourCC('n042')] = 4,
        [FourCC('n043')] = 4,
        [FourCC('n044')] = 5,

    },

    strategData = {

        gradeCap = 100,

        steps = {
            { at = 17, action = "research", rows = {
                {FourCC('n03I'),FourCC('R0AV'),6},  -- melee
                {FourCC('n03I'),FourCC('R0AW'),6},  -- melee
                {FourCC('n03I'),FourCC('R0AX'),6},  -- melee
                {FourCC('n03I'),FourCC('R0AY'),6},  -- melee
                {FourCC('n03I'),FourCC('R0AZ'),6},  -- melee
            }},

            { at = 20, action = "tryBuy" },
        },

    },

    join = Join_Dragons,

    naval = aiNavalTrain_Common,

    shipyard = FourCC('h0D8'),

    wall = FourCC('h0D8'),

    diplomat = "isolationist",

    brain = "objective",

    brainWeights = {
        kind  = { capital = 100, cluster = 40, capture = 60, weak = 20, front = 15 },
        value = 1.0, dist = 0.002, claim = 25.0, siege = 0.5,
        focusMargin = 30.0, homeThreat = 20.0, tpDist = 6000.0,
        rHome = 2500.0, rCluster = 1600.0,
        clusterEvery = 8, topK = 8,
    },
    compTarget = {
        [FourCC('o01D')] = 0.1923,
        [FourCC('n03Q')] = 0.1154,
        [FourCC('n03T')] = 0.1154,
        [FourCC('n03K')] = 0.1154,
        [FourCC('n03W')] = 0.1154,
        [FourCC('n03N')] = 0.0769,
        [FourCC('n03R')] = 0.0769,
        [FourCC('n03U')] = 0.0769,
        [FourCC('n03L')] = 0.0769,
        [FourCC('n03X')] = 0.0769,
        [FourCC('n05Q')] = 0.0385,
        [FourCC('N040')] = 0.0154,
        [FourCC('N047')] = 0.0154,
        [FourCC('N046')] = 0.0154,
        [FourCC('N045')] = 0.0154,
    },
})
