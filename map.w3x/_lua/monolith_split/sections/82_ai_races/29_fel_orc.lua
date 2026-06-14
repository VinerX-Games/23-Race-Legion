function Join_FelOrc(id, pi, u)

    if id == FourCC('n06B') then

        GroupAddUnit(udg_Ai_builders[pi], u)

    elseif aiUnitJoinsCapitalGuard(u, pi) then

    else

        aiUnitJoinsArmy(u, pi)

    end

end



RegisterAiRace("FelOrc", {

    tokens = {"felorc", "felorcs", "felork"},

    weight = 1,

    altar = FourCC('o05Y'),

    start = startFelOrc,

    buildings = {

        seed = FourCC('o060'),

        { FourCC('o05V'), 4, 4 }, { FourCC('o060'), 18, 4 },

        { FourCC('o05Y'), 3, 6 }, { FourCC('o05Z'), 10, 4 },

        { FourCC('o061'), 8, 6, gate = "tier2" }, { FourCC('o062'), 8, 6, gate = "tier2" },

        { FourCC('o05T'), 5, 2 }, { FourCC('o067'), 8, 4 },

    },

    gates = {

        tier2 = function(pi) return getAiCount(pi, FourCC('o05W')) + getAiCount(pi, FourCC('o05X')) >= 1 end,

    },

    production = {

        [FourCC('o05Z')] = {

            {FourCC('n06T'), 3}, {FourCC('n06Q'), 3}, {FourCC('n06W'), 2},

            {FourCC('n06L'), 2}, {FourCC('n06M'), 2}, {FourCC('n06J'), 2},

            {FourCC('n068'), 2}, {FourCC('n06G'), 2}, {FourCC('n06D'), 2},

        },

        [FourCC('o061')] = {

            {FourCC('n06R'), 3}, {FourCC('n06S'), 2}, {FourCC('n06N'), 2},

            {FourCC('n06O'), 2}, {FourCC('n067'), 2}, {FourCC('n06C'), 2},

        },

        [FourCC('o062')] = {

            {FourCC('n06V'), 3}, {FourCC('n06K'), 2}, {FourCC('n06U'), 2},

            {FourCC('n069'), 2}, {FourCC('n06A'), 2},

        },

        [FourCC('o05Y')] = {

            {FourCC('N072'), 1, limit = 1}, {FourCC('N073'), 1, limit = 1}, {FourCC('N06P'), 1, limit = 1},

        },

        worker = { id = FourCC('n06B'), cap = 18, from = { FourCC('o05V'), FourCC('o05W'), FourCC('o05X') } },
},

    ecoWeights = {

        [FourCC('o060')] = 1, [FourCC('o05V')] = 2,

        [FourCC('o05W')] = 5, [FourCC('o05X')] = 8,

    },

    strategData = {

        gradeCap = 100,

        steps = {

            -- Real FelOrc grades from the Lumber Mill (o05T): steel melee/ranged
            -- weapon + steel armor + improved saws (tools).
            { at = 17, action = "research", rows = {
                {FourCC('o05T'),FourCC('R0JS'),6},  -- steel melee weapon
                {FourCC('o05T'),FourCC('R0JQ'),6},  -- iron ranged weapon
                {FourCC('o05T'),FourCC('R0JR'),6},  -- steel armor
                {FourCC('o05T'),FourCC('R0K1'),6},  -- improved saws
            }},

            { at = 20, action = "tryBuy" },

            { at = 45, action = "fleet", wall = FourCC('h0D3') },

            { at = 25, action = "techUp", from = FourCC('o05V'), to = FourCC('o05W'), cap = 3 },

            { at = 55, action = "techUp", from = FourCC('o05W'), to = FourCC('o05X'), cap = 3 },

        },

    },

    attackerData = {

        [FourCC('n06T')] = {

            { order = "bloodlust",  chance = 4, type = "target" },

            { order = "berserk",    chance = 4, type = "immediate" },

        },

        [FourCC('n06Q')] = {

            { order = "lightningshield", chance = 4, type = "target" },

            { order = "purge",           chance = 4, type = "target" },

        },

        [FourCC('n06W')] = {

            { order = "carrionswarm", chance = 4, type = "point" },

            { order = "firebolt",     chance = 4, type = "target" },

        },

        [FourCC('n06R')] = {

            { order = "flamestrike",      chance = 4, type = "point" },

            { order = "rainoffire",       chance = 4, type = "point" },

        },

        [FourCC('n06S')] = {

            { order = "windwalk",    chance = 4, type = "immediate" },

        },

        [FourCC('n06V')] = {

            { order = "healingspray", chance = 4, type = "self" },

            { order = "dispel",       chance = 4, type = "point" },

        },

    },

    getLvlData = {

        [FourCC('N072')] = { skills = { FourCC('A1J8'), FourCC('A0EN'), FourCC('A1MD'), FourCC('A1J9') } },

        [FourCC('N073')] = { skills = { FourCC('AOwk'), FourCC('AOcr'), FourCC('A1JK'), FourCC('AOww') } },

        [FourCC('N06P')] = { skills = { FourCC('A0N7'), FourCC('A0BE'), FourCC('A1II'), FourCC('A0B7') } },

    },

    wall = FourCC('h0D3'),

    naval = aiNavalTrain_JungleTrolls,

    join = Join_FelOrc,


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
        [FourCC('n06B')] = 0.1607,
        [FourCC('n06T')] = 0.0536,
        [FourCC('n06Q')] = 0.0536,
        [FourCC('n06R')] = 0.0536,
        [FourCC('n06V')] = 0.0536,
        [FourCC('n06W')] = 0.0357,
        [FourCC('n06L')] = 0.0357,
        [FourCC('n06M')] = 0.0357,
        [FourCC('n06J')] = 0.0357,
        [FourCC('n068')] = 0.0357,
        [FourCC('n06G')] = 0.0357,
        [FourCC('n06D')] = 0.0357,
        [FourCC('n06S')] = 0.0357,
        [FourCC('n06N')] = 0.0357,
        [FourCC('n06O')] = 0.0357,
        [FourCC('n067')] = 0.0357,
        [FourCC('n06C')] = 0.0357,
        [FourCC('n06K')] = 0.0357,
        [FourCC('n06U')] = 0.0357,
        [FourCC('n069')] = 0.0357,
        [FourCC('n06A')] = 0.0357,
        [FourCC('N072')] = 0.0179,
        [FourCC('N073')] = 0.0179,
        [FourCC('N06P')] = 0.0179,
    },
})



---@param id integer

---@param pi integer

---@param u unit
