function Join_Bezlikie(id, pi, u)

    if id == FourCC('u02D') then

        GroupAddUnit(udg_Ai_builders[pi], u)

    elseif aiUnitJoinsCapitalGuard(u, pi) then

    else

        aiUnitJoinsArmy(u, pi)

    end

end



RegisterAiRace("Bezlikie", {

    tokens = {"bezlikie", "faceless"},

    weight = 1,

    altar = FourCC('h0HY'),

    start = startBezlikie,

    buildings = {

        seed = FourCC('u02E'),

        { FourCC('h0HZ'), 4, 4 }, { FourCC('u02E'), 18, 4 },

        { FourCC('h0HY'), 3, 6 }, { FourCC('h0I1'), 10, 4 },

        { FourCC('h0I2'), 8, 6, gate = "tier2" }, { FourCC('h0I4'), 8, 6, gate = "tier2" },

        { FourCC('h0I6'), 5, 2 }, { FourCC('h0K3'), 4, 2 },

    },

    gates = {

        tier2 = function(pi) return getAiCount(pi, FourCC('h0I7')) + getAiCount(pi, FourCC('h0I8')) >= 1 end,

    },

    production = {

        [FourCC('h0I1')] = {

            {FourCC('h0MO'), 3}, {FourCC('h0MN'), 3}, {FourCC('h0I9'), 2},

            {FourCC('h0IA'), 2}, {FourCC('h0IB'), 2},

        },

        [FourCC('h0I2')] = {

            {FourCC('h0IE'), 3}, {FourCC('h0ID'), 2}, {FourCC('h0K2'), 2},

        },

        [FourCC('h0I4')] = {

            {FourCC('n05I'), 3}, {FourCC('h0IF'), 2}, {FourCC('h0IG'), 2}, {FourCC('h0IC'), 2},

        },

        [FourCC('h0HY')] = {

            {FourCC('U02H'), 1, limit = 1}, {FourCC('U02G'), 1, limit = 1}, {FourCC('U02I'), 1, limit = 1},

        },

        worker = { id = FourCC('u02D'), cap = 18, from = { FourCC('h0HZ'), FourCC('h0I7'), FourCC('h0I8') } },
},

    ecoWeights = {

        [FourCC('u02E')] = 1, [FourCC('h0HZ')] = 2,

        [FourCC('h0I7')] = 5, [FourCC('h0I8')] = 8,

    },

    strategData = {

        gradeCap = 100,

        steps = {

            { at = 17, action = "random", branches = {

                { {FourCC('h0I6'),FourCC('Abds'),6} },

                { {FourCC('h0I1'),FourCC('Abds'),6} },

            }},

            { at = 20, action = "tryBuy" },

            { at = 25, action = "techUp", from = FourCC('h0HZ'), to = FourCC('h0I7'), cap = 3 },

            { at = 55, action = "techUp", from = FourCC('h0I7'), to = FourCC('h0I8'), cap = 3 },

        },

    },

    attackerData = {

        [FourCC('h0MO')] = {

            { order = "carrionswarm", chance = 4, type = "point" },

            { order = "sleep",        chance = 4, type = "target" },

        },

        [FourCC('h0MN')] = {

            { order = "frostnova",   chance = 4, type = "target" },

        },

        [FourCC('h0IE')] = {

            { order = "thunderbolt",  chance = 4, type = "target" },

            { order = "parasite",     chance = 4, type = "target" },

        },

        [FourCC('n05I')] = {

            { order = "doom",         chance = 4, type = "target" },

            { order = "curse",        chance = 4, type = "target" },

        },

        [FourCC('h0IF')] = {

            { order = "flamestrike",  chance = 4, type = "point" },

        },

    },

    getLvlData = {

        [FourCC('U02H')] = { skills = { FourCC('A1CJ'), FourCC('A10N'), FourCC('A10L'), FourCC('A1CG') } },

        [FourCC('U02G')] = { skills = { FourCC('A10I'), FourCC('A10J'), FourCC('A10K'), FourCC('A10H') } },

        [FourCC('U02I')] = { skills = { FourCC('A10Q'), FourCC('A0WQ'), FourCC('A10R'), FourCC('A10S') } },

    },

    join = Join_Bezlikie,

    wall = FourCC('h0K3'),

    shipyard = FourCC('h0D1'),  -- standard shared Верфь (wall is not a shipyard)


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
        [FourCC('u02D')] = 0.2250,
        [FourCC('h0MO')] = 0.0750,
        [FourCC('h0MN')] = 0.0750,
        [FourCC('h0IE')] = 0.0750,
        [FourCC('n05I')] = 0.0750,
        [FourCC('h0I9')] = 0.0500,
        [FourCC('h0IA')] = 0.0500,
        [FourCC('h0IB')] = 0.0500,
        [FourCC('h0ID')] = 0.0500,
        [FourCC('h0K2')] = 0.0500,
        [FourCC('h0IF')] = 0.0500,
        [FourCC('h0IG')] = 0.0500,
        [FourCC('h0IC')] = 0.0500,
        [FourCC('U02H')] = 0.0250,
        [FourCC('U02G')] = 0.0250,
        [FourCC('U02I')] = 0.0250,
    },
})



---@param id integer

---@param pi integer

---@param u unit
