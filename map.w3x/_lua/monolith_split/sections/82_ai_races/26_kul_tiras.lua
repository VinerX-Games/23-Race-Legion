function Join_KulTiras(id, pi, u)

    if id == FourCC('h013') then

        GroupAddUnit(udg_Ai_builders[pi], u)

    elseif aiUnitJoinsCapitalGuard(u, pi) then

    else

        aiUnitJoinsArmy(u, pi)

    end

end



RegisterAiRace("KulTiras", {

    tokens = {"kultiras", "kul-tiras"},

    weight = 1,

    altar = FourCC('h021'),

    start = startKulTiras,

    buildings = {

        seed = FourCC('h024'),

        { FourCC('h01X'), 4, 4 }, { FourCC('h024'), 18, 4 },

        { FourCC('h021'), 3, 6 }, { FourCC('h022'), 10, 4 },

        { FourCC('h026'), 8, 6, gate = "tier2" }, { FourCC('h027'), 8, 6, gate = "tier2" },

        { FourCC('h023'), 5, 2 }, { FourCC('h020'), 5, 2 },

        { FourCC('h025'), 4, 2 }, { FourCC('kt02'), 6, 4 },

    },

    gates = {

        tier2 = function(pi) return getAiCount(pi, FourCC('h01Y')) + getAiCount(pi, FourCC('h01Z')) >= 1 end,

    },

    production = {

        [FourCC('h022')] = {

            {FourCC('h019'), 3}, {FourCC('h01E'), 3}, {FourCC('h01D'), 2}, {FourCC('h01C'), 2},

        },

        [FourCC('h026')] = {

            {FourCC('h01F'), 3}, {FourCC('h01G'), 2},

        },

        [FourCC('h027')] = {

            {FourCC('h01H'), 3}, {FourCC('h01A'), 2}, {FourCC('h01I'), 2},

        },

        [FourCC('h021')] = {

            {FourCC('H01L'), 1, limit = 1}, {FourCC('H01N'), 1, limit = 1}, {FourCC('H01K'), 1, limit = 1},

        },

        worker = { id = FourCC('h013'), cap = 18, from = { FourCC('h01X'), FourCC('h01Y'), FourCC('h01Z') } },
},

    ecoWeights = {

        [FourCC('h024')] = 1, [FourCC('h01X')] = 2,

        [FourCC('h01Y')] = 5, [FourCC('h01Z')] = 8,

    },

    strategData = {

        gradeCap = 100,

        steps = {
            { at = 17, action = "research", rows = {
                {FourCC('h023'),FourCC('R0KL'),6},  -- armor
                {FourCC('h020'),FourCC('R035'),6},  -- ranged
                {FourCC('h020'),FourCC('R036'),6},  -- melee
                {FourCC('h020'),FourCC('R037'),6},  -- armor
                {FourCC('h020'),FourCC('R038'),6},  -- armor
                {FourCC('h020'),FourCC('R039'),6},  -- ranged
            }},


            { at = 17, action = "random", branches = {

                { {FourCC('h023'),FourCC('Abds'),6},{FourCC('h023'),FourCC('Arlm'),6} },

                { {FourCC('h022'),FourCC('Abds'),6} },

            }},

            { at = 20, action = "tryBuy" },

            { at = 45, action = "fleet", wall = FourCC('h0E7') },

            { at = 25, action = "techUp", from = FourCC('h01X'), to = FourCC('h01Y'), cap = 3 },

            { at = 55, action = "techUp", from = FourCC('h01Y'), to = FourCC('h01Z'), cap = 3 },

        },

    },

    attackerData = {

        [FourCC('h019')] = {

            { order = "defend",   chance = 4, type = "immediate" },

            { order = "berserk",  chance = 4, type = "immediate" },

        },

        [FourCC('h01E')] = {

            { order = "roar",       chance = 4, type = "immediate" },

        },

        [FourCC('h01F')] = {

            { order = "monsoon",     chance = 4, type = "point" },

            { order = "chainlightning", chance = 4, type = "target" },

        },

        [FourCC('h01H')] = {

            { order = "heal",        chance = 4, type = "heal", allyRange = 550 },

            { order = "dispel",      chance = 4, type = "point", range = 490 },

            { order = "innerfire",   chance = 4, type = "target" },

        },

    },

    getLvlData = {

        [FourCC('H01L')] = { skills = { FourCC('A0TM'), FourCC('A1MF'), FourCC('A07F'), FourCC('A07C') } },

        [FourCC('H01N')] = { skills = { FourCC('A075'), FourCC('A076'), FourCC('A078'), FourCC('A077') } },

        [FourCC('H01K')] = { skills = { FourCC('A07B'), FourCC('A07A'), FourCC('A079'), FourCC('A05I') } },

    },

    naval = aiNavalTrain_Common,

    join = Join_KulTiras,

    wall = FourCC('h0E7'),


    diplomat = "pragmatic",

    brain = "objective",

    brainWeights = {
        kind  = { capital = 100, cluster = 40, capture = 60, weak = 20, front = 15 },
        value = 1.0, dist = 0.002, claim = 25.0, siege = 0.5,
        focusMargin = 30.0, homeThreat = 20.0, tpDist = 6000.0,
        rHome = 2500.0, rCluster = 1600.0,
        clusterEvery = 8, topK = 8,
    },
    compTarget = {
        [FourCC('h013')] = 0.2647,
        [FourCC('h019')] = 0.0882,
        [FourCC('h01E')] = 0.0882,
        [FourCC('h01F')] = 0.0882,
        [FourCC('h01H')] = 0.0882,
        [FourCC('h01D')] = 0.0588,
        [FourCC('h01C')] = 0.0588,
        [FourCC('h01G')] = 0.0588,
        [FourCC('h01A')] = 0.0588,
        [FourCC('h01I')] = 0.0588,
        [FourCC('H01L')] = 0.0294,
        [FourCC('H01N')] = 0.0294,
        [FourCC('H01K')] = 0.0294,
    },
})



---@param id integer

---@param pi integer

---@param u unit
