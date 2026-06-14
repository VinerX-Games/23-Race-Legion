RegisterAiRace("Naga", {

    tokens = {"naga"},

    weight = 1,

    altar = FourCC('nnad'),

    start = startNaga,

    buildings = {

        seed = FourCC('nnfm'),

        { FourCC('nntt'), 3, 5 }, { FourCC('nnfm'), 20, 4 }, { FourCC('nnsg'), 18, 6 },

        { FourCC('nntg'), 30, 1 }, { FourCC('h0JW'), 5, 2 }, { FourCC('nnad'), 3, 6 },

        { FourCC('nnsa'), 15, 2 }, { FourCC('n055'), 15, 3 },

    },

    chooseBuild = ChooseBuildings_Naga,

    perebor = PereborBuildings_Naga,

    production = {

        [FourCC('nnsg')] = {

            { FourCC('n04Z'), 2 },

            { FourCC('nsnp'), 2, gate = "has_h0JW" },

            { FourCC('nhyc'), 1, gate = "has_h0JX" },

            { branch = "murloc", black = FourCC('n052'), other = FourCC('nmyr'), weight = 3, gate = "has_h0JX" },

        },

        [FourCC('nnsa')] = {

            { FourCC('n053'), 6, gate = "murloc_h0JX" },

            { FourCC('n054'), 6, gate = "murloc_h0JX" },

            { FourCC('n051'), 1, gate = "naga_h0JX" },

            { FourCC('nnsw'), 4, gate = "naga_h0JX" },

        },

        [FourCC('n055')] = {

            { branch = "murloc", black = FourCC('n050'), other = FourCC('nnrg'), weight = 2, gate = "has_h0JY" },

            { FourCC('n056'), 1, gate = "has_h0JY" },

            { FourCC('nwgs'), 1 },

        },

        [FourCC('nnad')] = {

            { FourCC('N07A'), 1, limit = 1 },

            { FourCC('H0JV'), 1, limit = 1 },

            { branch = "murloc", black = FourCC('H0OZ'), other = FourCC('H0JU'), weight = 1, limit = 1 },

        },

        worker = { id = FourCC('nmpe'), cap = 25,

                   from = { FourCC('nntt'), FourCC('h0JX'), FourCC('h0JY') } },

        pre = function(id, pi, u)

            if id == FourCC('nntt') or id == FourCC('h0JX') or id == FourCC('h0JY') then

                if getAiCount(pi, FourCC('nmpe')) >= 25 and GetRandomInt(1, 2) == 1 then

                    IssueImmediateOrderById(u, FourCC('nnmg'))

                    return true

                end

                return false

            end

            return false

        end,

    },

    gates = {

        has_h0JW = function(pi) return getAiCount(pi, FourCC('h0JW')) > 0 end,

        has_h0JX = function(pi) return getAiCount(pi, FourCC('h0JX')) > 0 end,

        has_h0JY = function(pi) return getAiCount(pi, FourCC('h0JY')) > 0 end,

        murloc = function(pi) return GetPlayerTechResearched(Player(pi), FourCC('R0FF'), true) end,

        naga = function(pi) return not GetPlayerTechResearched(Player(pi), FourCC('R0FF'), true) end,

        murloc_h0JX = function(pi) return GetPlayerTechResearched(Player(pi), FourCC('R0FF'), true) and getAiCount(pi, FourCC('h0JX')) > 0 end,

        naga_h0JX = function(pi) return not GetPlayerTechResearched(Player(pi), FourCC('R0FF'), true) and getAiCount(pi, FourCC('h0JX')) > 0 end,

    },

    branches = {

        murloc = function(pi) return GetPlayerTechResearched(Player(pi), FourCC('R0FF'), true) end,

    },

    ecoWeights = {

        [FourCC('nnfm')] = 1, [FourCC('nntt')] = 4,

        [FourCC('h0JX')] = 6, [FourCC('h0JY')] = 8,

    },

    strategData = {

        gradeCap = 150,

        steps = {

            { before = 50, action = "research", rows = {

                {FourCC('nntt'), FourCC('R0FE'), 1}, {FourCC('nntt'), FourCC('R0FF'), 1},

            }},

            { at = 17, action = "research", rows = {

                {FourCC('h0JW'), FourCC('R0FD'), 6}, {FourCC('h0JW'), FourCC('R0FH'), 6}, {FourCC('h0JW'), FourCC('Rnat'), 6}, {FourCC('h0JW'), FourCC('Rnam'), 6}, {FourCC('h0JW'), FourCC('Rnsb'), 6},

                {FourCC('nnsa'), FourCC('Rnsw'), 6}, {FourCC('nnsa'), FourCC('Rnsi'), 6},

                {FourCC('nnsg'), FourCC('R0FR'), 6}, {FourCC('nnsg'), FourCC('Rnen'), 6},

            }},

            { at = 17, action = "tryBuy" },

            { at = 25, action = "techUp", from = FourCC('nntt'), to = FourCC('h0JX'), cap = 3 },

            { at = 55, action = "techUp", from = FourCC('h0JX'), to = FourCC('h0JY'), cap = 3 },

            { at = 60, action = "mageTp" },

        },

    },

    attackerData = {

        pre = {

            { order = "blight", chance = 1, type = "immediate", terrain = "water", notAbil = FourCC('S00E'), ret = true },

        },

        [FourCC('H0JV')] = {

            { order = "berserk", chance = 3, type = "immediate" },

            { order = "clusterrockets", chance = 5, type = "point" },

            { order = "blink", chance = 5, type = "point" },

        },

        [FourCC('N07A')] = {

            { order = "banish", chance = 5, type = "target" },

            { order = "rainoffire", chance = 5, type = "point" },

            { order = "tranquility", chance = 5, type = "immediate" },

        },

        [FourCC('H0JU')] = {

            { order = "doom", chance = 6, type = "target" },

            { order = "frostnova", chance = 6, type = "target" },

            { order = "stomp", chance = 6, type = "immediate" },

        },

        [FourCC('H0OZ')] = {

            { order = "doom", chance = 6, type = "target" },

            { order = "frostnova", chance = 6, type = "target" },

            { order = "stomp", chance = 6, type = "immediate" },

        },

        [FourCC('n051')] = {

            { order = "healon", chance = 4, type = "immediate" },

            { order = "dispel", chance = 4, type = "point" },

        },

        [FourCC('nnsw')] = {

            { order = "cyclone", chance = 6, type = "target", notStructure = true },

            { order = "frostarmoron", chance = 6, type = "immediate" },

            { order = "parasiteon", chance = 6, type = "immediate" },

        },

        [FourCC('nnrg')] = {

            { order = "thunderbolt", chance = 6, type = "target" },

            { order = "carrionswarm", chance = 6, type = "point" },

        },

    },

    getLvlData = {

        [FourCC('H0JV')] = { ult = FourCC('A13C'), skills = { FourCC('A13A'), FourCC('AEbl') } },

        [FourCC('H0JU')] = { skills = { FourCC('A14I'), FourCC('A14G') } },

        [FourCC('N07A')] = { ult = FourCC('ANrg'), skills = { FourCC('ANsy'), FourCC('ANcs'), FourCC('ANeg') } },

    },

    join = Join_Naga,

    strateg = Strateg_Naga,

    strategEC = Strateg_Naga_EC,

    upgrade = UpgradeNaga,

    naval = aiNavalTrain_Naga,

    wall = FourCC('n04L'),  -- Naga Serpent's Lair (amphibious race, continentalNaga); no transport shipyard needed

    usesWaterPoint = false,

    continentalNaga = true,


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
        [FourCC('n053')] = 0.1579,
        [FourCC('n054')] = 0.1579,
        [FourCC('nnsw')] = 0.1053,
        [FourCC('n052')] = 0.0789,
        [FourCC('nmyr')] = 0.0789,
        [FourCC('n04Z')] = 0.0526,
        [FourCC('nsnp')] = 0.0526,
        [FourCC('n050')] = 0.0526,
        [FourCC('nnrg')] = 0.0526,
        [FourCC('nhyc')] = 0.0263,
        [FourCC('n051')] = 0.0263,
        [FourCC('n056')] = 0.0263,
        [FourCC('nwgs')] = 0.0263,
        [FourCC('N07A')] = 0.0263,
        [FourCC('H0JV')] = 0.0263,
        [FourCC('H0OZ')] = 0.0263,
        [FourCC('H0JU')] = 0.0263,
    },
})
