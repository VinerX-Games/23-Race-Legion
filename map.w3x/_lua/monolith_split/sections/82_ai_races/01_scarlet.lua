RegisterAiRace("Scarlet", {

    tokens = {"scarlet", "so"},

    weight = 1,

    altar = FourCC('h05X'),

    start = startScarlet,

    buildings = {

        seed = FourCC('h05Y'),

        { FourCC('h05U'), 4, 4 }, { FourCC('h05Y'), 15, 4 }, { FourCC('h05Z'), 15, 4 },

        { FourCC('h063'), 25, 1 }, { FourCC('h062'), 5, 2 }, { FourCC('h060'), 6, 2 },

        { FourCC('h05X'), 3, 5 },

        { FourCC('h064'), 7, 8, gate = "tier2" }, { FourCC('h061'), 15, 8, gate = "tier2" },

        { FourCC('h068'), 15, 10, gate = "church" },

    },

    gates = {

        tier2 = function(pi) return getAiCount(pi, FourCC('h05V')) + getAiCount(pi, FourCC('h05W')) >= 1 end,

        tier3 = function(pi) return getAiCount(pi, FourCC('h05W')) >= 1 end,

        church = function(pi) return getAiCount(pi, FourCC('h05W')) >= 1 end,

        has_h060 = function(pi) return getAiCount(pi, FourCC('h060')) >= 1 end,

        R040_church = function(pi) return (AiData[pi][FourCC('R040')] or false) and getAiCount(pi, FourCC('h05W')) >= 1 end,

        R03Z_church = function(pi) return (AiData[pi][FourCC('R03Z')] or false) and getAiCount(pi, FourCC('h05W')) >= 1 end,

    },

    production = {

        worker = { id = FourCC('h014'), cap = 20, from = { FourCC('h05U'), FourCC('h05V'), FourCC('h05W') } },

        [FourCC('h05Z')] = {

            { FourCC('h03B'), 1 },

            { FourCC('n007'), 1, gate = "has_h060" },

            { FourCC('h039'), 4, gate = "tier2" },

            { FourCC('h066'), 6, gate = "tier3" },

        },

        [FourCC('h064')] = {

            { FourCC('o00I'), 1 },

        },

        [FourCC('h061')] = {

            { FourCC('h067') }, { FourCC('n008') },

        },

        [FourCC('h05X')] = {

            { FourCC('H06C') }, { FourCC('H03H') }, { FourCC('H06B') },

        },

        [FourCC('h068')] = {

            { 0, 1 },

            { FourCC('h03F'), 1, gate = "R040_church" },

            { FourCC('h03D'), 1, gate = "R040_church" },

            { FourCC('h03I'), 1, gate = "R03Z_church" },

            { FourCC('h03G'), 1, gate = "R03Z_church" },

        },

        pre = function(id, pi, u)

            if id == FourCC('h05U') then

                local r = GetRandomInt(1, 3)

                if r == 1 and getAiCount(pi, FourCC('h014')) < 20 then

                    IssueImmediateOrderById(u, FourCC('h014'))

                elseif r == 2 and getAiCount(pi, FourCC('h03C')) < 15 then

                    IssueImmediateOrderById(u, FourCC('h03C'))

                elseif r == 3 and getAiCount(pi, FourCC('h03A')) < 15 then

                    IssueImmediateOrderById(u, FourCC('h03A'))

                end

                return true

            end

            return false

        end,

    },

    ecoWeights = {

        [FourCC('h05Y')] = 1, [FourCC('h05U')] = 2,

        [FourCC('h05V')] = 5, [FourCC('h05W')] = 8,

    },

    strategData = {

        gradeCap = 100,

        pre = function(i, pi, p)

            if i > 65 and getAiCount(pi, FourCC('h05V')) >= 1 then

                local r = GetRandomInt(1, 2)

                if r == 1 then

                    MakeGradeCheckCap(p, FourCC('h05W'), FourCC('R040'), 1)

                    AiData[pi][FourCC('R040')] = true

                else

                    MakeGradeCheckCap(p, FourCC('h05W'), FourCC('R03Z'), 1)

                    AiData[pi][FourCC('R03Z')] = true

                end

                MakeGradeCheckCap(p, FourCC('h068'), FourCC('R044'), 3)

                MakeGradeCheckCap(p, FourCC('h068'), FourCC('R043'), 3)

                MakeGradeCheckCap(p, FourCC('h068'), FourCC('R042'), 3)

                MakeGradeCheckCap(p, FourCC('h068'), FourCC('R041'), 3)

            end

        end,

        steps = {

            { at = 17, action = "research", rows = {

                {FourCC('h060'), FourCC('R04B'), 6}, {FourCC('h060'), FourCC('R04A'), 6}, {FourCC('h060'), FourCC('R049'), 6}, {FourCC('h060'), FourCC('R048'), 6}, {FourCC('h060'), FourCC('R04C'), 6},

                {FourCC('h062'), FourCC('RHac'), 6}, {FourCC('h062'), FourCC('Rhlh'), 6},

                {FourCC('h05Z'), FourCC('R03K'), 3},

            }},

            { at = 17, action = "tryBuy" },

            { at = 35, gate = "tier2", action = "research", rows = {

                {FourCC('h05Z'), FourCC('R03W'), 2}, {FourCC('h05Z'), FourCC('R03V'), 2},

                {FourCC('h05Z'), FourCC('R03L'), 2}, {FourCC('h05Z'), FourCC('R03M'), 2},

                {FourCC('h061'), FourCC('R03Y'), 3}, {FourCC('h061'), FourCC('R03X'), 3},

            }},

            { at = 35, gate = "tier2", action = "random", branches = {

                { {FourCC('h064'), FourCC('R03T'), 6} },

                { {FourCC('h064'), FourCC('R03S'), 6} },

            }},

            { at = 35, gate = "tier2", action = "research", rows = {

                {FourCC('h064'), FourCC('R047'), 6}, {FourCC('h064'), FourCC('R046'), 6}, {FourCC('h064'), FourCC('R045'), 6}, {FourCC('h064'), FourCC('R03U'), 6},

            }},

            { at = 25, action = "techUp", from = FourCC('h05U'), to = FourCC('h05V'), cap = 3 },

            { at = 55, action = "techUp", from = FourCC('h05V'), to = FourCC('h05W'), cap = 3 },

            { at = 60, action = "mageTp" },

        },

    },

    attackerData = {

        [FourCC('H06C')] = {

            { order = "firebolt", chance = 5, type = "target" },

            { order = "flamestrike", chance = 5, type = "point" },

            { order = "waterelemental", chance = 5, type = "immediate" },

        },

        [FourCC('H06B')] = {

            { order = "berserk", chance = 5, type = "immediate" },

            { order = "thunderclap", chance = 5, type = "immediate" },

            { order = "roar", chance = 5, type = "immediate" },

        },

        [FourCC('H03H')] = {

            { order = "firebolt", chance = 5, type = "heal", allyRange = 450 },

            { order = "roar", chance = 5, type = "immediate" },

            { order = "resurrection", chance = 5, type = "immediate" },

        },

        [FourCC('h067')] = {

            { order = "flamingarrows", chance = 4, type = "target" },

            { order = "devourmagic", chance = 4, type = "target", range = 525 },

        },

        [FourCC('n008')] = {

            { order = "flamingarrows", chance = 4, type = "target" },

            { order = "dispel", chance = 4, type = "point", range = 490 },

        },

        [FourCC('h03G')] = {

            { order = "berserk", chance = 3, type = "target" },

            { order = "roar", chance = 3, type = "point" },

        },

        [FourCC('h00Z')] = {

            { order = "ancestralspirit", chance = 6, type = "target", range = 125 },

            { order = "clusterrockets", chance = 6, type = "point", range = 300 },

            { order = "tranquility", chance = 6, type = "immediate", hp = 45 },

        },

        [FourCC('h00Y')] = {

            { order = "ancestralspirit", chance = 6, type = "target", range = 125 },

            { order = "clusterrockets", chance = 6, type = "point", range = 300 },

            { order = "tranquility", chance = 6, type = "immediate", hp = 45 },

        },

    },

    attackedData = {

        [FourCC('h039')] = {

            { order = "defend", chance = 5, type = "immediate" },

            { order = "magicdefense", chance = 5, type = "immediate" },

            { order = "undefend", chance = 5, type = "immediate" },

            { order = "magicundefense", chance = 5, type = "immediate" },

        },

        [FourCC('h03B')] = {

            { order = "defend", chance = 3, type = "immediate" },

            { order = "undefend", chance = 3, type = "immediate" },

        },

    },

    getLvlData = {

        [FourCC('H06C')] = { ult = FourCC('A09M'), skills = { FourCC('A09K'), FourCC('A09L'), FourCC('A09N') } },

        [FourCC('H06B')] = { ult = FourCC('A09J'), skills = { FourCC('A09F'), FourCC('A09G'), FourCC('A09I') } },

        [FourCC('H03H')] = { ult = FourCC('A09E'), skills = { FourCC('A097'), FourCC('A09C'), FourCC('A09D') } },

    },

    chooseBuild = ChooseBuildings_ScarletOrden,

    perebor = PereborBuildings_ScarletOrden,

    join = Join_Skarlet,

    shipyard = FourCC('h011'),  -- human worker (hpea) -> human Верфь (no wall building)

    strateg = Strateg_Scarlet,

    strategEC = Strateg_Scarlet_EC,

    upgrade = UpgradeScarlet,


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
        [FourCC('h066')] = 0.3529,
        [FourCC('h039')] = 0.2353,
        [FourCC('h03B')] = 0.0588,
        [FourCC('n007')] = 0.0588,
        [FourCC('o00I')] = 0.0588,
        [FourCC('h03F')] = 0.0588,
        [FourCC('h03D')] = 0.0588,
        [FourCC('h03I')] = 0.0588,
        [FourCC('h03G')] = 0.0588,
    },
})
