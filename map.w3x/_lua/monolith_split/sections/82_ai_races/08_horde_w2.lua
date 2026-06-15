function Join_HordeW2(id, pi, u)

    if id == FourCC('w200') then

        GroupAddUnit(udg_Ai_builders[pi], u)

    elseif id == FourCC('w201') or id == FourCC('w220') then

        GroupAddUnit(udg_Ai_navy[pi], u)

    elseif aiUnitJoinsCapitalGuard(u, pi) then

    else

        aiUnitJoinsArmy(u, pi)

    end

end



RegisterAiRace("HordeW2", {

    tokens = {"hw2", "hordew2", "orda2"},

    weight = 1,

    altar = FourCC('w20a'),

    start = startHordeW2,

    buildings = {

        seed = FourCC('w20y'),

        { FourCC('w20q'), 4, 4 }, { FourCC('w20y'), 18, 4 },

        { FourCC('w20r'), 10, 4 }, { FourCC('w214'), 5, 2 },

        { FourCC('w20a'), 3, 6 },

        { FourCC('w20i'), 8, 6, gate = "tier2" },

        { FourCC('w20t'), 8, 6, gate = "tier2" },

        { FourCC('w210'), 4, 4, gate = "tier2" },

        { FourCC('w212'), 4, 4, gate = "tier2" },

        { FourCC('w20u'), 25, 1 },

    },

    gates = {

        tier2 = function(pi)

            return getAiCount(pi, FourCC('w20w')) + getAiCount(pi, FourCC('w20e')) >= 1

        end,

        dark = function(pi)
            return HordeW2GetSubrace(pi) == "dark"
        end,

        dragonmaw = function(pi)
            return HordeW2GetSubrace(pi) == "dragonmaw"
        end,

        base = function(pi)
            return HordeW2GetSubrace(pi) == "base"
        end,

        not_dragonmaw = function(pi)
            return HordeW2GetSubrace(pi) ~= "dragonmaw"
        end,

        not_dark = function(pi)
            return HordeW2GetSubrace(pi) ~= "dark"
        end,

    },

    branches = {

        dark = function(pi)
            return HordeW2GetSubrace(pi) == "dark"
        end,

        dragonmaw = function(pi)
            return HordeW2GetSubrace(pi) == "dragonmaw"
        end,

    },

    production = {

        [FourCC('w20r')] = {

            {FourCC('w203'), 4, gate = "not_dragonmaw"},
            {FourCC('w204'), 3, gate = "base"},
            {FourCC('w204'), 5, gate = "dark"},
            {FourCC('xd04'), 4, gate = "dragonmaw"},
            {FourCC('w208'), 3, gate = "tier2"},
            {FourCC('w208'), 4, gate = "dark"},
            {FourCC('w208'), 4, gate = "dragonmaw"},

        },

        [FourCC('w20i')] = {

            {FourCC('w201'), 2, gate = "base"},
            {FourCC('w201'), 1, gate = "dark"},
            {FourCC('xd05'), 3, gate = "dragonmaw"},
            {FourCC('w206'), 3, gate = "base"},
            {FourCC('xd02'), 4, gate = "dark"},
            {FourCC('w206'), 1, gate = "dragonmaw"},
            {FourCC('w207'), 2, gate = "tier2"},
            {FourCC('w207'), 3, gate = "dark"},
            {FourCC('w207'), 1, gate = "dragonmaw"},

        },

        [FourCC('w20t')] = {

            {FourCC('w205'), 3, gate = "base"},
            {FourCC('xd01'), 4, gate = "dark"},
            {FourCC('xd06'), 4, gate = "dragonmaw"},
            {FourCC('w209'), 2, gate = "tier2"},
            {FourCC('w209'), 3, gate = "dark"},
            {FourCC('w209'), 1, gate = "dragonmaw"},
            {FourCC('w211'), 3, gate = "base"},
            {FourCC('w211'), 2, gate = "dark"},
            {FourCC('w211'), 4, gate = "dragonmaw"},

        },

        [FourCC('w20a')] = {

            {FourCC('W200'), 1, limit = 1},
            {FourCC('W201'), 1, limit = 1},
            {FourCC('W202'), 1, gate = "not_dark", limit = 1},
            {FourCC('W203'), 1, gate = "dark", limit = 1},

        },

        [FourCC('w210')] = {
            {FourCC('w202'), 2, gate = "base"},
            {FourCC('xd07'), 2, gate = "dark"},
            {FourCC('w202'), 4, gate = "dragonmaw"},
        },

        [FourCC('w212')] = {
            {FourCC('w213'), 2, gate = "base"},
            {FourCC('xd03'), 4, gate = "dark"},
            {FourCC('w213'), 1, gate = "dragonmaw"},
        },

        worker = { id = FourCC('w200'), cap = 20, from = { FourCC('w20q'), FourCC('w20w'), FourCC('w20e') } },
},

    ecoWeights = {

        [FourCC('w20y')] = 1, [FourCC('w20q')] = 2,

        [FourCC('w20w')] = 5, [FourCC('w20e')] = 8,

    },

    strategData = {

        gradeCap = 100,

        steps = {

            { before = 20, action = "research", rows = {
                {FourCC('w20r'), FourCC('w2r7'), 4},
                {FourCC('w20r'), FourCC('w2r8'), 4},
            }, gate = "dark"},

            { before = 20, action = "research", rows = {
                {FourCC('w20t'), FourCC('w2r4'), 4},
                {FourCC('w20t'), FourCC('w2r6'), 4},
            }, gate = "dragonmaw"},

            { at = 17, action = "random", branches = {

                { {FourCC('w214'),FourCC('w2r0'),6},{FourCC('w214'),FourCC('w2r1'),6},{FourCC('w214'),FourCC('w2r2'),6},{FourCC('w214'),FourCC('w2rb'),6} },

                { {FourCC('w20r'),FourCC('w2r7'),6},{FourCC('w20r'),FourCC('w2r8'),6},{FourCC('w20r'),FourCC('w2r9'),6} },

                { {FourCC('w20t'),FourCC('w2r4'),6},{FourCC('w20t'),FourCC('w2r5'),6},{FourCC('w20t'),FourCC('w2r6'),6} },

            }},

            { at = 20, action = "tryBuy" },

            { at = 25, action = "techUp", from = FourCC('w20q'), to = FourCC('w20w'), cap = 3 },

            { at = 55, action = "techUp", from = FourCC('w20w'), to = FourCC('w20e'), cap = 3 },

        },

    },

    attackerData = {

        [FourCC('w208')] = {

            { order = "frenzy", chance = 4, type = "immediate" },

        },

        [FourCC('w201')] = {

            { order = "windwalk", chance = 4, type = "immediate" },

        },

        [FourCC('w206')] = {

            { order = "selfdestruct", chance = 6, type = "immediate", hp = 30 },

        },

        [FourCC('w205')] = {

            { order = "bloodlust", chance = 4, type = "target" },

            { order = "spiritwolf", chance = 5, type = "immediate" },

        },

        [FourCC('xd01')] = {

            { order = "bloodlust", chance = 4, type = "target" },

            { order = "lightningshield", chance = 5, type = "target" },

        },

        [FourCC('xd06')] = {

            { order = "bloodlust", chance = 4, type = "target" },

            { order = "purge", chance = 5, type = "target" },

        },

        [FourCC('w209')] = {

            { order = "frostarmor", chance = 4, type = "target" },

            { order = "raisedead", chance = 5, type = "point" },

        },

        [FourCC('w211')] = {

            { order = "heal", chance = 4, type = "heal", allyRange = 550 },

            { order = "dispel", chance = 4, type = "point" },

            { order = "slow", chance = 4, type = "target" },

        },

        [FourCC('w202')] = {

            { order = "flamestrike", chance = 4, type = "point" },

            { order = "breathoffire", chance = 4, type = "point" },

        },

        [FourCC('xd05')] = {

            { order = "ensnare", chance = 4, type = "target" },

        },

    },

    join = Join_HordeW2,

    wall = FourCC('w20u'),

    shipyard = FourCC('h0HO'),  -- orc worker (opeo) -> orc/goblin Верфь


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
        [FourCC('w200')] = 0.2045,
        [FourCC('w203')] = 0.0750,
        [FourCC('w204')] = 0.0909,
        [FourCC('xd04')] = 0.0800,
        [FourCC('w208')] = 0.0800,
        [FourCC('w206')] = 0.0400,
        [FourCC('xd02')] = 0.0600,
        [FourCC('w205')] = 0.0682,
        [FourCC('xd01')] = 0.0500,
        [FourCC('xd06')] = 0.0500,
        [FourCC('w211')] = 0.0682,
        [FourCC('w202')] = 0.0800,
        [FourCC('w213')] = 0.0800,
        [FourCC('xd03')] = 0.0500,
        [FourCC('xd05')] = 0.0500,
        [FourCC('xd07')] = 0.0400,
        [FourCC('w201')] = 0.0455,
        [FourCC('w207')] = 0.0455,
        [FourCC('w209')] = 0.0455,
        [FourCC('W200')] = 0.0227,
        [FourCC('W201')] = 0.0227,
        [FourCC('W202')] = 0.0227,
        [FourCC('W203')] = 0.0227,
    },
})



---@param id integer

---@param pi integer

---@param u unit
