function Join_Dalaran(id, pi, u)

    if id == FourCC('u001') then

        GroupAddUnit(udg_Ai_builders[pi], u)

    elseif aiUnitJoinsCapitalGuard(u, pi) then

    else

        aiUnitJoinsArmy(u, pi)

    end

end



RegisterAiRace("Dalaran", {

    tokens = {"dalaran"},

    weight = 1,

    altar = FourCC('h02V'),

    start = startDalaran,

    buildings = {

        seed = FourCC('h031'),

        { FourCC('h030'), 4, 4 }, { FourCC('h031'), 18, 4 },

        { FourCC('h02V'), 3, 6 }, { FourCC('h02W'), 10, 4 },

        { FourCC('h02X'), 8, 4 }, { FourCC('h037'), 8, 4 },

        { FourCC('h034'), 6, 4 }, { FourCC('h02Y'), 5, 2 },

    },

    production = {

        [FourCC('h02W')] = {

            {FourCC('h02J'), 3}, {FourCC('h02K'), 3}, {FourCC('h02M'), 2}, {FourCC('h02P'), 2},

        },

        [FourCC('h02X')] = {

            {FourCC('n00B'), 3}, {FourCC('h02L'), 3}, {FourCC('h02I'), 2}, {FourCC('h02O'), 2},

        },

        [FourCC('h037')] = {

            {FourCC('n00C'), 3}, {FourCC('n00D'), 2},

        },

        [FourCC('h02V')] = {

            {FourCC('H04S'), 1, limit = 1}, {FourCC('H04W'), 1, limit = 1}, {FourCC('H04X'), 1, limit = 1},

        },

        worker = { id = FourCC('u001'), cap = 18, from = { FourCC('h030') } },
},

    ecoWeights = {

        [FourCC('h031')] = 1, [FourCC('h030')] = 2,

    },

    strategData = {

        gradeCap = 100,

        steps = {

            -- Real Dalaran grades from the Magic Forge (h02Y): magic swords, cloth
            -- cloak (armor), staff empowerment, fire/ice defense.
            { at = 17, action = "research", rows = {
                {FourCC('h02Y'),FourCC('R00Q'),6},  -- magic swords (weapon)
                {FourCC('h02Y'),FourCC('R00T'),6},  -- cloth cloak (armor)
                {FourCC('h02Y'),FourCC('R012'),6},  -- staff empowerment
                {FourCC('h02Y'),FourCC('R013'),6},  -- fire defense
                {FourCC('h02Y'),FourCC('R014'),6},  -- ice defense
            }},

            { at = 20, action = "tryBuy" },

            { at = 45, action = "fleet", wall = FourCC('h011') },

        },

    },

    attackerData = {

        [FourCC('H04S')] = {

            { order = "waterelemental", chance = 5, type = "immediate" },

            { order = "frostnova",      chance = 5, type = "target" },

            { order = "blizzard",       chance = 5, type = "point" },

        },

        [FourCC('H04W')] = {

            { order = "flamestrike",   chance = 5, type = "point" },

            { order = "rainoffire",    chance = 5, type = "point" },

            { order = "summonphoenix", chance = 5, type = "immediate" },

        },

        [FourCC('H04X')] = {

            { order = "massteleport", chance = 5, type = "immediate" },

            { order = "dispel",       chance = 5, type = "point" },

        },

        [FourCC('n00C')] = {

            { order = "parasite",   chance = 4, type = "target" },

        },

        [FourCC('n00D')] = {

            { order = "carrionswarm", chance = 4, type = "point" },

        },

    },

    attackerData = {

        [FourCC('H04S')] = {

            { order = "waterelemental", chance = 5, type = "immediate" },

            { order = "frostnova",      chance = 5, type = "target" },

            { order = "blizzard",       chance = 5, type = "point" },

        },

        [FourCC('H04W')] = {

            { order = "flamestrike",   chance = 5, type = "point" },

            { order = "rainoffire",    chance = 5, type = "point" },

            { order = "summonphoenix", chance = 5, type = "immediate" },

        },

        [FourCC('H04X')] = {

            { order = "massteleport", chance = 5, type = "immediate" },

            { order = "dispel",       chance = 5, type = "point" },

        },

        [FourCC('n00C')] = {

            { order = "parasite",   chance = 4, type = "target" },

        },

        [FourCC('n00D')] = {

            { order = "carrionswarm", chance = 4, type = "point" },

        },

    },

    getLvlData = {

        [FourCC('H04S')] = { skills = { FourCC('A03K'), FourCC('A03J'), FourCC('A03I'), FourCC('A03D') } },

        [FourCC('H04W')] = { skills = { FourCC('A03Q'), FourCC('A03O'), FourCC('A03M'), FourCC('A03L') } },

        [FourCC('H04X')] = { skills = { FourCC('A044'), FourCC('A03V'), FourCC('A03U'), FourCC('A1FQ') } },

    },

    wall = FourCC('h011'),

    naval = aiNavalTrain_Common,

    join = Join_Dalaran,


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
        [FourCC('u001')] = 0.0968,
        [FourCC('h02J')] = 0.0968,
        [FourCC('h02K')] = 0.0968,
        [FourCC('n00B')] = 0.0968,
        [FourCC('h02L')] = 0.0968,
        [FourCC('n00C')] = 0.0968,
        [FourCC('h02M')] = 0.0645,
        [FourCC('h02P')] = 0.0645,
        [FourCC('h02I')] = 0.0645,
        [FourCC('h02O')] = 0.0645,
        [FourCC('n00D')] = 0.0645,
        [FourCC('H04S')] = 0.0323,
        [FourCC('H04W')] = 0.0323,
        [FourCC('H04X')] = 0.0323,
    },
})



---@param id integer

---@param pi integer

---@param u unit
