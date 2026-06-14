function Join_Pandarens(id, pi, u)

    if id == FourCC('pa01') then

        GroupAddUnit(udg_Ai_builders[pi], u)

    elseif aiUnitJoinsCapitalGuard(u, pi) then

    else

        aiUnitJoinsArmy(u, pi)

    end

end



RegisterAiRace("Pandarens", {

    tokens = {"pandaren", "pandarens", "panda"},

    weight = 1,

    altar = FourCC('pa27'),

    start = startPandarens,

    buildings = {

        seed = FourCC('pa26'),

        { FourCC('pa23'), 4, 4 }, { FourCC('pa26'), 18, 4 },

        { FourCC('pa27'), 3, 6 }, { FourCC('pa28'), 10, 4 },

        { FourCC('pa31'), 8, 4 }, { FourCC('pa32'), 8, 6, gate = "tier2" },

        { FourCC('pa33'), 8, 6, gate = "tier2" }, { FourCC('pa30'), 5, 2 },

        { FourCC('h0NZ'), 6, 4 }, { FourCC('h0P5'), 4, 2 },

    },

    gates = {

        tier2 = function(pi) return getAiCount(pi, FourCC('pa24')) + getAiCount(pi, FourCC('pa25')) >= 1 end,

    },

    production = {

        [FourCC('pa28')] = {

            {FourCC('pa06'), 3}, {FourCC('pa05'), 3}, {FourCC('pa12'), 2},

            {FourCC('pa11'), 2}, {FourCC('pa22'), 2},

        },

        [FourCC('pa31')] = {

            {FourCC('pa04'), 3}, {FourCC('pa10'), 2}, {FourCC('pa14'), 2},

        },

        [FourCC('pa32')] = {

            {FourCC('pa08'), 3}, {FourCC('pa13'), 2}, {FourCC('pa07'), 2},

        },

        [FourCC('pa33')] = {

            {FourCC('pa29'), 3}, {FourCC('pa35'), 2}, {FourCC('pa38'), 2}, {FourCC('pa09'), 2},

        },

        [FourCC('pa27')] = {

            {FourCC('PA36'), 1, limit = 1}, {FourCC('PA37'), 1, limit = 1}, {FourCC('PA38'), 1, limit = 1}, {FourCC('PA40'), 1, limit = 1},

        },

        worker = { id = FourCC('pa01'), cap = 20, from = { FourCC('pa23'), FourCC('pa24'), FourCC('pa25') } },
},

    ecoWeights = {

        [FourCC('pa26')] = 1, [FourCC('pa23')] = 2,

        [FourCC('pa24')] = 5, [FourCC('pa25')] = 8,

    },

    strategData = {

        gradeCap = 100,

        steps = {

            { at = 17, action = "random", branches = {

                { {FourCC('pa30'),FourCC('Abds'),6},{FourCC('pa30'),FourCC('Arlm'),6} },

                { {FourCC('pa28'),FourCC('Abds'),6} },

            }},

            { at = 20, action = "tryBuy" },

            { at = 25, action = "techUp", from = FourCC('pa23'), to = FourCC('pa24'), cap = 3 },

            { at = 55, action = "techUp", from = FourCC('pa24'), to = FourCC('pa25'), cap = 3 },

        },

    },

    attackerData = {

        [FourCC('pa06')] = {

            { order = "drunkenhaze", chance = 4, type = "target" },

            { order = "breathoffire", chance = 4, type = "point" },

        },

        [FourCC('pa05')] = {

            { order = "berserk",    chance = 4, type = "immediate" },

        },

        [FourCC('pa08')] = {

            { order = "stomp",       chance = 4, type = "immediate" },

        },

        [FourCC('pa29')] = {

            { order = "heal",        chance = 4, type = "heal", allyRange = 550 },

            { order = "dispel",      chance = 4, type = "point", range = 490 },

        },

        [FourCC('pa35')] = {

            { order = "cyclone",     chance = 4, type = "target", notStructure = true },

            { order = "monsoon",     chance = 4, type = "point" },

        },

    },

    getLvlData = {

        [FourCC('PA36')] = { skills = { FourCC('pa44'), FourCC('PA77'), FourCC('PA76'), FourCC('PA15') } },

        [FourCC('PA37')] = { skills = { FourCC('PA02'), FourCC('PA51'), FourCC('PA50'), FourCC('PA78') } },

        [FourCC('PA38')] = { skills = { FourCC('PA75'), FourCC('pa37'), FourCC('PA60') } },

        [FourCC('PA40')] = { skills = { FourCC('PA77'), FourCC('PA57'), FourCC('PA03'), FourCC('PA59'), FourCC('PA55') } },

    },

    join = Join_Pandarens,

    wall = FourCC('h0P5'),

    shipyard = FourCC('h011'),  -- human worker (hpea) -> human Верфь


    diplomat = "diplomat",

    brain = "objective",

    brainWeights = {
        kind  = { capital = 100, cluster = 40, capture = 60, weak = 20, front = 15 },
        value = 1.0, dist = 0.002, claim = 25.0, siege = 0.5,
        focusMargin = 30.0, homeThreat = 20.0, tpDist = 6000.0,
        rHome = 2500.0, rCluster = 1600.0,
        clusterEvery = 8, topK = 8,
    },
    compTarget = {
        [FourCC('pa01')] = 0.1875,
        [FourCC('pa06')] = 0.0625,
        [FourCC('pa05')] = 0.0625,
        [FourCC('pa04')] = 0.0625,
        [FourCC('pa08')] = 0.0625,
        [FourCC('pa29')] = 0.0625,
        [FourCC('pa12')] = 0.0417,
        [FourCC('pa11')] = 0.0417,
        [FourCC('pa22')] = 0.0417,
        [FourCC('pa10')] = 0.0417,
        [FourCC('pa14')] = 0.0417,
        [FourCC('pa13')] = 0.0417,
        [FourCC('pa07')] = 0.0417,
        [FourCC('pa35')] = 0.0417,
        [FourCC('pa38')] = 0.0417,
        [FourCC('pa09')] = 0.0417,
        [FourCC('PA36')] = 0.0208,
        [FourCC('PA37')] = 0.0208,
        [FourCC('PA38')] = 0.0208,
        [FourCC('PA40')] = 0.0208,
    },
})



---@param id integer

---@param pi integer

---@param u unit
