function Join_IceTrolls(id, pi, u)

    if id == FourCC('o045') then

        GroupAddUnit(udg_Ai_builders[pi], u)

    elseif aiUnitJoinsCapitalGuard(u, pi) then

    else

        aiUnitJoinsArmy(u, pi)

    end

end



RegisterAiRace("IceTrolls", {

    tokens = {"icetroll", "icetrolls", "drakkari"},

    weight = 1,

    altar = FourCC('o049'),

    start = startIceTrolls,

    buildings = {

        seed = FourCC('o04C'),

        { FourCC('o046'), 4, 4 }, { FourCC('o04C'), 18, 4 },

        { FourCC('o049'), 3, 6 }, { FourCC('o04A'), 10, 4 },

        { FourCC('o04E'), 8, 6, gate = "tier2" }, { FourCC('o04D'), 8, 4 },

        { FourCC('o04J'), 8, 4 }, { FourCC('o04B'), 5, 2 },

    },

    gates = {

        tier2 = function(pi) return getAiCount(pi, FourCC('o047')) + getAiCount(pi, FourCC('o048')) >= 1 end,

    },

    production = {

        [FourCC('o04A')] = {

            {FourCC('n05S'), 3}, {FourCC('n05T'), 3}, {FourCC('o04F'), 2},

        },

        [FourCC('o04E')] = {

            {FourCC('n05Z'), 3}, {FourCC('n05U'), 2}, {FourCC('n07B'), 2},

        },

        [FourCC('o04D')] = {

            {FourCC('n05Y'), 3}, {FourCC('o04T'), 2},

        },

        [FourCC('o04J')] = {

            {FourCC('n05V'), 3}, {FourCC('n05W'), 2}, {FourCC('n05X'), 2},

        },

        [FourCC('o049')] = {

            {FourCC('O04H'), 1, limit = 1}, {FourCC('O04G'), 1, limit = 1}, {FourCC('O04I'), 1, limit = 1},

        },

        worker = { id = FourCC('o045'), cap = 18, from = { FourCC('o046'), FourCC('o047'), FourCC('o048') } },
},

    ecoWeights = {

        [FourCC('o04C')] = 1, [FourCC('o046')] = 2,

        [FourCC('o047')] = 5, [FourCC('o048')] = 8,

    },

    strategData = {

        gradeCap = 100,

        steps = {

            { at = 17, action = "random", branches = {

                { {FourCC('o04B'),FourCC('Abds'),6},{FourCC('o04B'),FourCC('Arlm'),6} },

                { {FourCC('o04A'),FourCC('Abds'),6} },

            }},

            { at = 20, action = "tryBuy" },

            { at = 45, action = "fleet", wall = FourCC('h0HO') },

            { at = 25, action = "techUp", from = FourCC('o046'), to = FourCC('o047'), cap = 3 },

            { at = 55, action = "techUp", from = FourCC('o047'), to = FourCC('o048'), cap = 3 },

        },

    },

    attackerData = {

        [FourCC('n05S')] = {

            { order = "berserk",   chance = 4, type = "immediate" },

        },

        [FourCC('n05T')] = {

            { order = "cannibalize", chance = 4, type = "immediate", hp = 50 },

        },

        [FourCC('n05Z')] = {

            { order = "frostnova",   chance = 4, type = "target" },

            { order = "frostarmor",  chance = 4, type = "target" },

        },

        [FourCC('n05U')] = {

            { order = "blizzard",    chance = 4, type = "point" },

        },

        [FourCC('n05Y')] = {

            { order = "healingwave", chance = 4, type = "heal", allyRange = 550 },

            { order = "bloodlust",   chance = 4, type = "target" },

        },

        [FourCC('n05V')] = {

            { order = "parasite",    chance = 4, type = "target" },

            { order = "curse",       chance = 4, type = "target" },

        },

    },

    getLvlData = {

        [FourCC('O04H')] = { skills = { FourCC('A1DR'), FourCC('A1DA'), FourCC('A1DS'), FourCC('A1EB') } },

        [FourCC('O04G')] = { skills = { FourCC('AOhw'), FourCC('A1DL'), FourCC('AOsw'), FourCC('AOvd') } },

        [FourCC('O04I')] = { skills = { FourCC('A1EE'), FourCC('A1ED'), FourCC('A1EC'), FourCC('A1EF') } },

    },

    wall = FourCC('h0HO'),

    naval = aiNavalTrain_Horde,

    join = Join_IceTrolls,


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
        [FourCC('o045')] = 0.2308,
        [FourCC('n05S')] = 0.0769,
        [FourCC('n05T')] = 0.0769,
        [FourCC('n05Z')] = 0.0769,
        [FourCC('n05Y')] = 0.0769,
        [FourCC('n05V')] = 0.0769,
        [FourCC('o04F')] = 0.0513,
        [FourCC('n05U')] = 0.0513,
        [FourCC('n07B')] = 0.0513,
        [FourCC('o04T')] = 0.0513,
        [FourCC('n05W')] = 0.0513,
        [FourCC('n05X')] = 0.0513,
        [FourCC('O04H')] = 0.0256,
        [FourCC('O04G')] = 0.0256,
        [FourCC('O04I')] = 0.0256,
    },
})



---@param id integer

---@param pi integer

---@param u unit
