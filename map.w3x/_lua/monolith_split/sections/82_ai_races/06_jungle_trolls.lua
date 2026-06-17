RegisterAiRace("JungleTrolls", {

    tokens = {"jt", "jungletrolls", "trolls"},

    weight = 1,

    altar = FourCC('h0N0'),

    start = startJungleTrolls,

    -- Phase 3 declarative build order (engine: AiRunChooseBuildings). Mirrors

    -- ChooseBuildings_JungleTrolls exactly. chooseBuild kept as fallback.

    buildings = {

        seed = FourCC('h0N2'),

        { FourCC('h0N5'), 4, 4 },

        { FourCC('h0N2'), 18, 4 },

        { FourCC('h0MY'), 10, 4 },

        { FourCC('h0N3'), 5, 2 },

        { FourCC('h0N0'), 3, 6 },

        { FourCC('h0MX'), 8, 6, gate = "tier2" },

        { FourCC('h0MW'), 8, 6, gate = "tier2" },

        { FourCC('h0D3'), 2, 1, gate = "tier2" },

    },

    gates = {

        tier2 = function(pi)

            return getAiCount(pi, FourCC('h0N1')) + getAiCount(pi, FourCC('h0N6')) >= 1

        end,

        tier3 = function(pi)

            return getAiCount(pi, FourCC('h0N6')) >= 1

        end,

    },

    -- Phase 3 declarative production (engine: AiRunProduction).

    production = {

        [FourCC('h0MY')] = {

            { FourCC('o04M'), 5 },

            { FourCC('o04L'), 4 },

            { FourCC('o05E'), 1, gate = "tier2" },

        },

        [FourCC('h0MX')] = {

            { FourCC('o04O'), 3 },

            { FourCC('o04R'), 3 },

            { branch = "jt", black = FourCC('o04N'), other = FourCC('o04P'), weight = 4 },

        },

        [FourCC('h0MW')] = {

            { FourCC('o04S'), 3 },

            { FourCC('o04U'), 4 },

            { FourCC('o05J'), 2, gate = "tier2" },

            { FourCC('o05G'), 2, gate = "tier3" },

        },

        [FourCC('h0N0')] = {

            { FourCC('O054'), 1, limit = 1 }, { FourCC('O05A'), 1, limit = 1 }, { FourCC('O05D'), 1, limit = 1 },

            { branch = "jt", black = FourCC('O05L'), other = FourCC('O055'), limit = 1 },

        },

        worker = { id = FourCC('o04Q'), cap = 18,

                   from = { FourCC('h0N5'), FourCC('h0N1'), FourCC('h0N6') } },

    },

    branches = {

        jt = function(pi) return JungleTrollsBranchIsBlack(pi) end,

    },

    -- Phase 3 declarative strategy (engine: AiRunStrateg).

    ecoWeights = {

        [FourCC('h0N2')] = 1,

        [FourCC('h0N5')] = 2,

        [FourCC('h0N1')] = 5,

        [FourCC('h0N6')] = 8,

        [FourCC('h0MY')] = 2, [FourCC('h0N3')] = 2,

        [FourCC('h0N0')] = 3,

    },

    strategData = {

        gradeCap = 100,

        steps = {
            { at = 17, action = "research", rows = {
                {FourCC('h0N3'),FourCC('R0I8'),6},  -- melee
            }},


            { at = 17, action = "random", branches = {

                { {FourCC('h0N3'), FourCC('R0I8'), 6}, {FourCC('h0N3'), FourCC('R0I9'), 6}, {FourCC('h0N3'), FourCC('R0IA'), 6}, {FourCC('h0N3'), FourCC('R0II'), 2} },

                { {FourCC('h0MY'), FourCC('R0IK'), 6}, {FourCC('h0MY'), FourCC('R0IM'), 6}, {FourCC('h0N2'), FourCC('R0IJ'), 6} },

                { {FourCC('h0MX'), FourCC('R0IB'), 6}, {FourCC('h0MX'), FourCC('R0IC'), 6}, {FourCC('h0MX'), FourCC('R0ID'), 6} },

                { {FourCC('h0MW'), FourCC('R0IL'), 6}, {FourCC('h0MW'), FourCC('R0IN'), 6}, {FourCC('h0MW'), FourCC('R0IJ'), 6} },

            }},

            { at = 45, action = "fleet", wall = FourCC('h0D3') },

            { at = 20, action = "tryBuy" },

            { at = 25, action = "techUp", from = FourCC('h0N5'), to = FourCC('h0N1'), cap = 3 },

            { at = 55, action = "techUp", from = FourCC('h0N1'), to = FourCC('h0N6'), cap = 3 },

        },

    },

    attackerData = {

        [FourCC('o04U')] = {

            { order = "berserk", chance = 3, type = "immediate" },

        },

        [FourCC('o04O')] = {

            { order = "bloodlust", chance = 4, type = "target" },

            { order = "dispel", chance = 4, type = "point" },

            { order = "slow", chance = 4, type = "target" },

        },

        [FourCC('o04R')] = {

            { order = "stasistrap", chance = 4, type = "point" },

            { order = "evileye", chance = 4, type = "point" },

            { order = "healingward", chance = 4, type = "self" },

        },

        [FourCC('o04N')] = {

            { order = "flamingarrows", chance = 4, type = "target" },

            { order = "Vengeance", chance = 5, type = "target" },

            { order = "hex", chance = 4, type = "target", notStructure = true },

        },

        [FourCC('o04P')] = {

            { order = "frostarmor", chance = 4, type = "target" },

            { order = "blizzard", chance = 4, type = "point" },

        },

        [FourCC('o04S')] = {

            { order = "ravenform", chance = 4, type = "immediate" },

        },

        [FourCC('o05J')] = {

            { order = "ravenform", chance = 4, type = "immediate" },

        },

        [FourCC('o04M')] = {

            { order = "chemicalrage", chance = 4, type = "immediate" },

        },

        [FourCC('O054')] = {

            { order = "hex", chance = 3, type = "target", notStructure = true },

        },

        [FourCC('O05A')] = {

            { order = "whirlwind", chance = 4, type = "immediate" },

        },

    },

    getLvlData = {

        [FourCC('O054')] = { ult = FourCC('AOsw'), skills = { FourCC('AOhw'), FourCC('A1E0'), FourCC('A1D0') } },

        [FourCC('O05A')] = { ult = FourCC('A1E4'), skills = { FourCC('A1E2'), FourCC('A1E3'), FourCC('A1D0') } },

        [FourCC('O05D')] = { ult = FourCC('A1E8'), skills = { FourCC('A1E6'), FourCC('A1E9'), FourCC('A1EA') } },

        [FourCC('O055')] = { ult = FourCC('A1DM'), skills = { FourCC('A1DB'), FourCC('A1DC'), FourCC('A1EL') } },

        [FourCC('O05L')] = { ult = FourCC('A1ET'), skills = { FourCC('A1ES'), FourCC('A1EV'), FourCC('A1EY') } },

    },

    chooseBuild = ChooseBuildings_JungleTrolls,

    perebor = PereborBuildings2_JungleTrolls,

    join = Join_JungleTrolls,

    strateg = Strateg_JungleTrolls,

    strategEC = Strateg_JungleTrolls_EC,

    upgrade = UpgradeJungleTrolls,

    naval = aiNavalTrain_JungleTrolls,

    wall = FourCC('h0N2'),

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
        [FourCC('o04M')] = 0.1316,
        [FourCC('o04L')] = 0.1053,
        [FourCC('o04U')] = 0.1053,
        [FourCC('o04N')] = 0.1053,
        [FourCC('o04P')] = 0.1053,
        [FourCC('o04O')] = 0.0789,
        [FourCC('o04R')] = 0.0789,
        [FourCC('o04S')] = 0.0789,
        [FourCC('o05J')] = 0.0526,
        [FourCC('o05G')] = 0.0526,
        [FourCC('o05E')] = 0.0263,
        [FourCC('O054')] = 0.0263,
        [FourCC('O05A')] = 0.0263,
        [FourCC('O05D')] = 0.0263,
    },
})



-- ====================================================================

-- ForestTrolls (Phase 3 data-driven)

-- TODO: verify building/unit mappings and research assignments

-- ====================================================================

---@param id integer

---@param pi integer

---@param u unit

---@return nothing
