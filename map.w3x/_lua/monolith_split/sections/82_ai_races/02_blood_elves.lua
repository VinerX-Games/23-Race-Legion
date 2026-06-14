RegisterAiRace("BloodElves", {

    tokens = {"be", "bloodelves", "ek"},

    weight = 1,

    altar = FourCC('h05J'),

    start = startBloodElves,

    buildings = {

        seed = FourCC('h04M'),

        { FourCC('h04C'), 4, 4 }, { FourCC('h04M'), 15, 4 }, { FourCC('h04D'), 15, 4 },

        { FourCC('h04N'), 25, 1 }, { FourCC('h04Q'), 5, 2 }, { FourCC('h04R'), 6, 2 },

        { FourCC('h05J'), 3, 8 },

        { FourCC('h04G'), 15, 8, gate = "tier2" }, { FourCC('h04E'), 15, 8, gate = "tier2" },

        { FourCC('h04F'), 12, 2 },

    },

    gates = {

        tier2 = function(pi) return getAiCount(pi, FourCC('h04B')) + getAiCount(pi, FourCC('h04A')) >= 1 end,

        tier3 = function(pi) return getAiCount(pi, FourCC('h04A')) >= 1 end,

        has_h04R = function(pi) return getAiCount(pi, FourCC('h04R')) >= 1 end,

    },

    production = {

        [FourCC('h04D')] = {

            { FourCC('h03V'), 1 },

            { FourCC('n00I'), 1, gate = "has_h04R" },

            { FourCC('h03X'), 4, gate = "tier2" },

            { FourCC('h03Y'), 6, gate = "tier3" },

        },

        [FourCC('h04G')] = {

            { FourCC('e001'), 1, gate = "tier2" },

            { FourCC('h046'), 2, gate = "tier2" },

            { FourCC('e030'), 1, gate = "tier2" },

            { FourCC('h03Z'), 6, gate = "tier3" },

        },

        [FourCC('h04E')] = {

            { FourCC('h03W') }, { FourCC('h040') }, { FourCC('h041') }, { FourCC('h042') },

        },

        [FourCC('h05J')] = {

            { FourCC('Hjnd') }, { FourCC('H043') }, { FourCC('H045') },

        },

        worker = { id = FourCC('h04K'), cap = 20,

                   from = { FourCC('h04C') } },

    },

    ecoWeights = {

        [FourCC('h04M')] = 1, [FourCC('h04C')] = 2,

        [FourCC('h04B')] = 5, [FourCC('h04A')] = 8,

    },

    strategData = {

        gradeCap = 100,

        steps = {

            { at = 17, action = "random", branches = {

                { {FourCC('h04R'), FourCC('R01L'), 6}, {FourCC('h04R'), FourCC('R01J'), 6}, {FourCC('h04R'), FourCC('R01K'), 6}, {FourCC('h04R'), FourCC('R01M'), 6} },

                { {FourCC('h04R'), FourCC('R01R'), 6}, {FourCC('h04Q'), FourCC('R03I'), 6}, {FourCC('h04Q'), FourCC('R03J'), 6}, {FourCC('h04Q'), FourCC('R01N'), 6} },

                { {FourCC('h04Q'), FourCC('R01T'), 6}, {FourCC('h04Q'), FourCC('R03E'), 6}, {FourCC('h04Q'), FourCC('R03F'), 6}, {FourCC('h04D'), FourCC('R03K'), 1} },

            }},

            { at = 35, gate = "tier2", action = "random", branches = {

                { {FourCC('h04D'), FourCC('R01Y'), 1}, {FourCC('h04D'), FourCC('R01X'), 1}, {FourCC('h04D'), FourCC('R01W'), 2}, {FourCC('h04E'), FourCC('R0BU'), 1}, {FourCC('h04E'), FourCC('R01O'), 6} },

                { {FourCC('h04E'), FourCC('R01P'), 6}, {FourCC('h04E'), FourCC('R01Q'), 6}, {FourCC('h04E'), FourCC('R01S'), 1}, {FourCC('h04G'), FourCC('R03N'), 6}, {FourCC('h04G'), FourCC('R021'), 6} },

                { {FourCC('h04G'), FourCC('R021'), 6}, {FourCC('h04G'), FourCC('R03Q'), 6}, {FourCC('h04G'), FourCC('R021'), 6}, {FourCC('h04G'), FourCC('Rhcd'), 6} },

            }},

            { at = 35, gate = "tier2", action = "random", branches = {

                { {FourCC('h04F'), FourCC('R03R'), 3} },

                { {FourCC('h04F'), FourCC('R01H'), 3} },

                { {FourCC('h04F'), FourCC('R01I'), 3} },

                { {FourCC('h04F'), FourCC('R01G'), 3} },

                { {FourCC('h04F'), FourCC('R01D'), 3} },

            }},

            { at = 45, gate = "tier2", action = "fleet", wall = FourCC('h011') },

            { at = 20, action = "tryBuy" },

            { at = 25, action = "techUp", from = FourCC('h04C'), to = FourCC('h04B'), cap = 3 },

            { at = 55, action = "techUp", from = FourCC('h04B'), to = FourCC('h04A'), cap = 3 },

            { at = 60, action = "mageTp", cap = 3 },

        },

    },

    attackerData = {

        [FourCC('H043')] = {

            { order = "banish", chance = 6, type = "target" },

            { order = "steal", chance = 6, type = "target" },

            { order = "flamestrike", chance = 6, type = "point" },

            { order = "summonphoenix", chance = 6, type = "immediate" },

        },

        [FourCC('Hjnd')] = {

            { order = "shadowstrike", chance = 3, type = "target", notStructure = true },

            { order = "faeriefire", chance = 3, type = "target" },

        },

        [FourCC('H045')] = {

            { order = "roar", chance = 5, type = "immediate" },

            { order = "fanofknives", chance = 5, type = "immediate" },

            { order = "resurrection", chance = 5, type = "immediate" },

        },

        [FourCC('H03H')] = {

            { order = "berserk", chance = 4, type = "immediate" },

        },

        [FourCC('n040')] = {

            { order = "frostarmoron", chance = 5, type = "immediate" },

            { order = "curseon", chance = 5, type = "immediate" },

            { order = "carrionswarm", chance = 5, type = "point", range = 490 },

        },

        [FourCC('h041')] = {

            { order = "polymorph", chance = 3, type = "target", notStructure = true },

            { order = "devourmagic", chance = 3, type = "target", range = 490 },

        },

        [FourCC('h042')] = {

            { order = "faeriefireon", chance = 6, type = "immediate" },

            { order = "curseon", chance = 6, type = "immediate" },

            { order = "bloodluston", chance = 6, type = "immediate" },

        },

        [FourCC('H03Y')] = {

            { order = "healingwave", chance = 3, type = "heal", allyRange = 550 },

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

        [FourCC('h03V')] = {

            { order = "defend", chance = 5, type = "immediate" },

            { order = "manashieldon", chance = 5, type = "immediate" },

            { order = "undefend", chance = 5, type = "immediate" },

        },

        [FourCC('h03B')] = {

            { order = "defend", chance = 3, type = "immediate" },

            { order = "undefend", chance = 3, type = "immediate" },

        },

    },

    getLvlData = {

        [FourCC('H043')] = { ult = FourCC('AHpx'), skills = { FourCC('AHfs'), FourCC('AHdr'), FourCC('AHpx') } },

        [FourCC('Hjnd')] = { ult = FourCC('A07V'), skills = { FourCC('A07U'), FourCC('A0LQ'), FourCC('AEar') } },

        [FourCC('H045')] = { ult = FourCC('AHre'), skills = { FourCC('A08H'), FourCC('A07W'), FourCC('AHbh') } },

    },

    chooseBuild = ChooseBuildings_BloodElves,

    perebor = PereborBuildings2_BloodElves,

    join = Join_BloodElves,

    strateg = Strateg_BloodElves,

    strategEC = Strateg_BloodElves_EC,

    upgrade = UpgradeBloodElves,

    naval = aiNavalTrain_Common,

    wall = FourCC('h011'),


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
        [FourCC('h03Y')] = 0.2727,
        [FourCC('h03Z')] = 0.2727,
        [FourCC('h03X')] = 0.1818,
        [FourCC('h046')] = 0.0909,
        [FourCC('h03V')] = 0.0455,
        [FourCC('n00I')] = 0.0455,
        [FourCC('e001')] = 0.0455,
        [FourCC('e030')] = 0.0455,
    },
})
