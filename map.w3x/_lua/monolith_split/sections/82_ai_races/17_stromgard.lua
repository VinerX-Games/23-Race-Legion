function Join_Stromgard(id, pi, u)

    if id == FourCC('h0G9') then

        GroupAddUnit(udg_Ai_builders[pi], u)

    elseif aiUnitJoinsCapitalGuard(u, pi) then

    else

        aiUnitJoinsArmy(u, pi)

    end

end



RegisterAiRace("Stromgard", {

    tokens = {"stromgard", "stromgarde"},

    weight = 1,

    altar = FourCC('h0H3'),

    start = startStromgard,

    buildings = {

        seed = FourCC('h0H2'),

        { FourCC('h0GZ'), 4, 4 }, { FourCC('h0H2'), 18, 4 },

        { FourCC('h0H3'), 3, 6 }, { FourCC('h0H4'), 10, 4 },

        { FourCC('h0HI'), 8, 6, gate = "tier2" }, { FourCC('h0HF'), 8, 6, gate = "tier2" },

        { FourCC('h0H5'), 5, 2 }, { FourCC('h0H6'), 5, 2 },

        { FourCC('h0HG'), 4, 2 }, { FourCC('h0HU'), 6, 4 },

    },

    gates = {

        tier2 = function(pi) return getAiCount(pi, FourCC('h0H0')) + getAiCount(pi, FourCC('h0H1')) >= 1 end,

    },

    production = {

        [FourCC('h0H4')] = {

            {FourCC('h0F4'), 3}, {FourCC('h0GT'), 3}, {FourCC('h0GU'), 2},

            {FourCC('h0GS'), 2}, {FourCC('h0GV'), 2},

        },

        [FourCC('h0HI')] = {

            {FourCC('h0GX'), 3}, {FourCC('h0GW'), 3},

        },

        [FourCC('h0HF')] = {

            {FourCC('h0L3'), 3}, {FourCC('h0GY'), 2},

        },

        [FourCC('h0HU')] = {

            {FourCC('h0HD'), 2},

        },

        [FourCC('h0H3')] = {

            {FourCC('H0HB'), 1, limit = 1}, {FourCC('H0HL'), 1, limit = 1}, {FourCC('H0HA'), 1, limit = 1},

        },

        worker = { id = FourCC('h0G9'), cap = 18, from = { FourCC('h0GZ'), FourCC('h0H0'), FourCC('h0H1') } },
},

    ecoWeights = {

        [FourCC('h0H2')] = 1, [FourCC('h0GZ')] = 2,

        [FourCC('h0H0')] = 5, [FourCC('h0H1')] = 8,

    },

    strategData = {

        gradeCap = 100,

        steps = {

            { at = 17, action = "random", branches = {

                { {FourCC('h0H6'),FourCC('Abds'),6},{FourCC('h0H5'),FourCC('Arlm'),6} },

                { {FourCC('h0H4'),FourCC('Abds'),6} },

                { {FourCC('h0HF'),FourCC('Abds'),6},{FourCC('h0HI'),FourCC('Abds'),6} },

            }},

            { at = 20, action = "tryBuy" },

            { at = 25, action = "techUp", from = FourCC('h0GZ'), to = FourCC('h0H0'), cap = 3 },

            { at = 55, action = "techUp", from = FourCC('h0H0'), to = FourCC('h0H1'), cap = 3 },

        },

    },

    attackerData = {

        [FourCC('h0F4')] = {

            { order = "defend",   chance = 4, type = "immediate" },

            { order = "berserk",  chance = 4, type = "immediate" },

        },

        [FourCC('h0GT')] = {

            { order = "thunderclap", chance = 4, type = "immediate" },

        },

        [FourCC('h0GX')] = {

            { order = "flamestrike", chance = 4, type = "point" },

            { order = "rainoffire",  chance = 4, type = "point" },

        },

        [FourCC('h0L3')] = {

            { order = "bloodlust", chance = 4, type = "target" },

            { order = "dispel",    chance = 4, type = "point" },

        },

        [FourCC('h0HD')] = {

            { order = "clusterrockets", chance = 4, type = "point" },

        },

    },

    attackedData = {

        [FourCC('h0F4')] = {

            { order = "defend",    chance = 3, type = "immediate" },

            { order = "undefend",  chance = 3, type = "immediate" },

        },

    },

    getLvlData = {

        [FourCC('H0HB')] = { skills = { FourCC('A0XM'), FourCC('A0XW'), FourCC('A0Y8'), FourCC('A0XZ') } },

        [FourCC('H0HL')] = { skills = { FourCC('A0XV'), FourCC('A0ZP'), FourCC('A0ZO'), FourCC('A0ZN') } },

        [FourCC('H0HA')] = { skills = { FourCC('A0ZQ'), FourCC('A0XK'), FourCC('A0Y6'), FourCC('A0Y7') } },

    },

    join = Join_Stromgard,

    wall = FourCC('h0HG'),

    shipyard = FourCC('h011'),  -- human worker (hpea) -> human Верфь


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
        [FourCC('h0G9')] = 0.2432,
        [FourCC('h0F4')] = 0.0811,
        [FourCC('h0GT')] = 0.0811,
        [FourCC('h0GX')] = 0.0811,
        [FourCC('h0GW')] = 0.0811,
        [FourCC('h0L3')] = 0.0811,
        [FourCC('h0GU')] = 0.0541,
        [FourCC('h0GS')] = 0.0541,
        [FourCC('h0GV')] = 0.0541,
        [FourCC('h0GY')] = 0.0541,
        [FourCC('h0HD')] = 0.0541,
        [FourCC('H0HB')] = 0.0270,
        [FourCC('H0HL')] = 0.0270,
        [FourCC('H0HA')] = 0.0270,
    },
})



---@param id integer

---@param pi integer

---@param u unit
