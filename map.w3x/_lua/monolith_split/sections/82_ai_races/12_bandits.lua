function Join_Bandits(id, pi, u)

    if id == FourCC('h002') then

        GroupAddUnit(udg_Ai_builders[pi], u)

    elseif aiUnitJoinsCapitalGuard(u, pi) then

    else

        aiUnitJoinsArmy(u, pi)

    end

end



RegisterAiRace("Bandits", {

    tokens = {"bandit", "bandits"},

    weight = 1,

    altar = FourCC('h051'),

    start = startBandits,

    buildings = {

        seed = FourCC('h00A'),

        { FourCC('h007'), 4, 4 }, { FourCC('h00A'), 18, 4 },

        { FourCC('h051'), 3, 6 }, { FourCC('h00B'), 10, 4 },

        { FourCC('h01W'), 8, 4 }, { FourCC('h00O'), 8, 6, gate = "tier2" },

        { FourCC('h03O'), 5, 2 }, { FourCC('h03P'), 5, 2 },

        { FourCC('h03Q'), 4, 2 },

    },

    gates = {

        tier2 = function(pi) return getAiCount(pi, FourCC('h008')) + getAiCount(pi, FourCC('h009')) >= 1 end,

    },

    production = {

        [FourCC('h00B')] = {

            {FourCC('h003'), 4}, {FourCC('h005'), 3}, {FourCC('h006'), 2},

            {FourCC('n000'), 4}, {FourCC('n002'), 3}, {FourCC('n004'), 2},

        },

        [FourCC('h01W')] = {

            {FourCC('h02Q'), 3}, {FourCC('h02R'), 2}, {FourCC('h02S'), 2},

        },

        [FourCC('h00O')] = {

            {FourCC('h00P'), 3}, {FourCC('h00S'), 2}, {FourCC('h00U'), 1},

            {FourCC('h029'), 3}, {FourCC('h02A'), 2}, {FourCC('h02B'), 1},

        },

        [FourCC('h051')] = {

            {FourCC('H03S'), 1, limit = 1}, {FourCC('H047'), 1, limit = 1}, {FourCC('H048'), 1, limit = 1},

        },

        worker = { id = FourCC('h002'), cap = 18, from = { FourCC('h007'), FourCC('h008'), FourCC('h009') } },
},

    ecoWeights = {

        [FourCC('h00A')] = 1, [FourCC('h007')] = 2,

        [FourCC('h008')] = 5, [FourCC('h009')] = 8,

    },

    strategData = {

        gradeCap = 100,

        steps = {
            { at = 17, action = "research", rows = {
                {FourCC('h03O'),FourCC('R00J'),6},  -- melee
                {FourCC('h03O'),FourCC('R00L'),6},  -- melee
                {FourCC('h03O'),FourCC('R00M'),6},  -- armor
                {FourCC('h03O'),FourCC('R00N'),6},  -- armor
                {FourCC('h03O'),FourCC('R00X'),6},  -- melee
                {FourCC('h03P'),FourCC('R00V'),6},  -- armor
            }},


            { at = 17, action = "random", branches = {

                { {FourCC('h03O'),FourCC('Abds'),6},{FourCC('h03P'),FourCC('Arlm'),6} },

                { {FourCC('h00B'),FourCC('Abds'),6} },

            }},

            { at = 20, action = "tryBuy" },

            { at = 25, action = "techUp", from = FourCC('h007'), to = FourCC('h008'), cap = 3 },

            { at = 55, action = "techUp", from = FourCC('h008'), to = FourCC('h009'), cap = 3 },

        },

    },

    attackerData = {

        [FourCC('h003')] = {

            { order = "berserk",  chance = 4, type = "immediate" },

        },

        [FourCC('h005')] = {

            { order = "flamingarrows", chance = 4, type = "target" },

        },

        [FourCC('h00P')] = {

            { order = "thunderbolt", chance = 4, type = "target" },

            { order = "parasite",    chance = 4, type = "target" },

        },

        [FourCC('h00S')] = {

            { order = "curse",         chance = 4, type = "target" },

            { order = "faeriefire",    chance = 4, type = "target" },

        },

        [FourCC('h029')] = {

            { order = "carrionswarm",  chance = 4, type = "point" },

        },

    },

    getLvlData = {

        [FourCC('H03S')] = { skills = { FourCC('A01J'), FourCC('A01D'), FourCC('A01H'), FourCC('A01I') } },

        [FourCC('H047')] = { skills = { FourCC('A023'), FourCC('ANrf'), FourCC('AHab'), FourCC('ANlm') } },

        [FourCC('H048')] = { skills = { FourCC('A0WV'), FourCC('A026'), FourCC('A028'), FourCC('A029') } },

    },

    join = Join_Bandits,

    wall = FourCC('h03Q'),

    shipyard = FourCC('h011'),  -- human worker (hpea) -> human Верфь


    diplomat = "traitor",

    brain = "objective",

    brainWeights = {
        kind  = { capital = 100, cluster = 40, capture = 60, weak = 20, front = 15 },
        value = 1.0, dist = 0.002, claim = 25.0, siege = 0.5,
        focusMargin = 30.0, homeThreat = 20.0, tpDist = 6000.0,
        rHome = 2500.0, rCluster = 1600.0,
        clusterEvery = 8, topK = 8,
    },
    compTarget = {
        [FourCC('h002')] = 0.1837,
        [FourCC('h003')] = 0.0816,
        [FourCC('n000')] = 0.0816,
        [FourCC('h005')] = 0.0612,
        [FourCC('n002')] = 0.0612,
        [FourCC('h02Q')] = 0.0612,
        [FourCC('h00P')] = 0.0612,
        [FourCC('h029')] = 0.0612,
        [FourCC('h006')] = 0.0408,
        [FourCC('n004')] = 0.0408,
        [FourCC('h02R')] = 0.0408,
        [FourCC('h02S')] = 0.0408,
        [FourCC('h00S')] = 0.0408,
        [FourCC('h02A')] = 0.0408,
        [FourCC('h00U')] = 0.0204,
        [FourCC('h02B')] = 0.0204,
        [FourCC('H03S')] = 0.0204,
        [FourCC('H047')] = 0.0204,
        [FourCC('H048')] = 0.0204,
    },
})



---@param id integer

---@param pi integer

---@param u unit
