function Join_Ogres(id, pi, u)

    if id == FourCC('o03W') then

        GroupAddUnit(udg_Ai_builders[pi], u)

    elseif aiUnitJoinsCapitalGuard(u, pi) then

    else

        aiUnitJoinsArmy(u, pi)

    end

end



RegisterAiRace("Ogres", {

    tokens = {"ogre", "ogres"},

    weight = 1,

    altar = FourCC('o037'),

    start = startOgres,

    buildings = {

        seed = FourCC('o036'),

        { FourCC('o035'), 4, 4 }, { FourCC('o036'), 18, 4 },

        { FourCC('o037'), 3, 6 }, { FourCC('o03A'), 10, 4 },

        { FourCC('o039'), 8, 4 }, { FourCC('o03J'), 8, 6, gate = "tier2" },

        { FourCC('o03C'), 8, 6, gate = "tier2" }, { FourCC('o03B'), 5, 2 },

        { FourCC('o038'), 4, 2 },

    },

    gates = {

        tier2 = function(pi) return getAiCount(pi, FourCC('o03D')) + getAiCount(pi, FourCC('o03E')) >= 1 end,

    },

    production = {

        [FourCC('o03A')] = {

            {FourCC('o03I'), 3}, {FourCC('o03H'), 3}, {FourCC('o03G'), 2}, {FourCC('o03F'), 2},

        },

        [FourCC('o039')] = {

            {FourCC('o03L'), 3}, {FourCC('o03M'), 2}, {FourCC('o03K'), 2},

        },

        [FourCC('o03J')] = {

            {FourCC('o03P'), 3}, {FourCC('o03N'), 2}, {FourCC('o03O'), 2},

        },

        [FourCC('o03C')] = {

            {FourCC('o03U'), 3}, {FourCC('o03T'), 3}, {FourCC('o03V'), 2},

            {FourCC('o03Q'), 2}, {FourCC('o03R'), 2}, {FourCC('o03S'), 2},

        },

        [FourCC('o037')] = {

            {FourCC('N05L'), 1, limit = 1}, {FourCC('N05K'), 1, limit = 1}, {FourCC('N05J'), 1, limit = 1},

        },

        worker = { id = FourCC('o03W'), cap = 18, from = { FourCC('o035'), FourCC('o03D'), FourCC('o03E') } },
},

    ecoWeights = {

        [FourCC('o036')] = 1, [FourCC('o035')] = 2,

        [FourCC('o03D')] = 5, [FourCC('o03E')] = 8,

    },

    strategData = {

        gradeCap = 100,

        steps = {
            { at = 17, action = "research", rows = {
                {FourCC('o03B'),FourCC('R0GL'),6},  -- melee
                {FourCC('o03B'),FourCC('R0GM'),6},  -- armor
                {FourCC('o03B'),FourCC('R0GN'),6},  -- ranged
            }},


            { at = 17, action = "random", branches = {

                { {FourCC('o03B'),FourCC('Abds'),6},{FourCC('o03B'),FourCC('Arlm'),6} },

                { {FourCC('o03A'),FourCC('Abds'),6} },

            }},

            { at = 20, action = "tryBuy" },

            { at = 25, action = "techUp", from = FourCC('o035'), to = FourCC('o03D'), cap = 3 },

            { at = 55, action = "techUp", from = FourCC('o03D'), to = FourCC('o03E'), cap = 3 },

        },

    },

    attackerData = {

        [FourCC('o03I')] = {

            { order = "stomp",    chance = 4, type = "immediate" },

            { order = "berserk",  chance = 4, type = "immediate" },

        },

        [FourCC('o03H')] = {

            { order = "bloodlust", chance = 4, type = "target" },

        },

        [FourCC('o03G')] = {

            { order = "cannibalize", chance = 4, type = "immediate", hp = 50 },

        },

        [FourCC('o03P')] = {

            { order = "flamestrike",   chance = 4, type = "point" },

            { order = "rainoffire",    chance = 4, type = "point" },

        },

        [FourCC('o03N')] = {

            { order = "windwalk",     chance = 4, type = "immediate" },

        },

        [FourCC('o03U')] = {

            { order = "heal",         chance = 4, type = "heal", allyRange = 550 },

            { order = "chainlightning", chance = 4, type = "target" },

        },

    },

    getLvlData = {

        [FourCC('N05L')] = { skills = { FourCC('A16V'), FourCC('A16U'), FourCC('A16X'), FourCC('A16W') } },

        [FourCC('N05K')] = { skills = { FourCC('A173'), FourCC('A175'), FourCC('A172'), FourCC('A174') } },

        [FourCC('N05J')] = { skills = { FourCC('A16Y'), FourCC('A170'), FourCC('A175'), FourCC('A171') } },

    },

    join = Join_Ogres,

    wall = FourCC('o038'),

    shipyard = FourCC('h0HO'),  -- orc worker (opeo) -> orc/goblin Верфь


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
        [FourCC('o03W')] = 0.1800,
        [FourCC('o03I')] = 0.0600,
        [FourCC('o03H')] = 0.0600,
        [FourCC('o03L')] = 0.0600,
        [FourCC('o03P')] = 0.0600,
        [FourCC('o03U')] = 0.0600,
        [FourCC('o03T')] = 0.0600,
        [FourCC('o03G')] = 0.0400,
        [FourCC('o03F')] = 0.0400,
        [FourCC('o03M')] = 0.0400,
        [FourCC('o03K')] = 0.0400,
        [FourCC('o03N')] = 0.0400,
        [FourCC('o03O')] = 0.0400,
        [FourCC('o03V')] = 0.0400,
        [FourCC('o03Q')] = 0.0400,
        [FourCC('o03R')] = 0.0400,
        [FourCC('o03S')] = 0.0400,
        [FourCC('N05L')] = 0.0200,
        [FourCC('N05K')] = 0.0200,
        [FourCC('N05J')] = 0.0200,
    },
})



---@param id integer

---@param pi integer

---@param u unit
