RegisterAiRace("Horde", {

    tokens = {"horde"},

    weight = 1,

    altar = FourCC('oalt'),

    start = startHorde,

    buildings = {

        seed = FourCC('otrb'),

        { FourCC('ogre'), 3, 5 }, { FourCC('otrb'), 20, 3 }, { FourCC('obar'), 3, 7 },

        { FourCC('obar'), 18, 3 }, { FourCC('obea'), 18, 2 }, { FourCC('owtw'), 30, 1 },

        { FourCC('ofor'), 5, 3 }, { FourCC('oalt'), 3, 6 },

        { FourCC('osld'), 15, 10, gate = "spirit" }, { FourCC('otto'), 15, 10, gate = "spirit" },

        { FourCC('osld'), 15, 1 }, { FourCC('otto'), 15, 1 }, { FourCC('ovln'), 1, 6 },

    },

    gates = {

        spirit = function(pi) return getAiCount(pi, FourCC('ostr')) + getAiCount(pi, FourCC('ofrt')) > 0 end,

        ironHorde = function(pi) return GetPlayerTechResearched(Player(pi), FourCC('R0EA'), true) end,

        notIronHorde = function(pi) return not GetPlayerTechResearched(Player(pi), FourCC('R0EA'), true) end,

        spirit_notIron = function(pi) return not GetPlayerTechResearched(Player(pi), FourCC('R0EA'), true) and getAiCount(pi, FourCC('ostr')) + getAiCount(pi, FourCC('ofrt')) > 0 end,

        fortress = function(pi) return getAiCount(pi, FourCC('ofrt')) > 0 end,

    },

    production = {

        [FourCC('obar')] = {

            { FourCC('o01N'), 2, gate = "ironHorde" },

            { FourCC('ogru'), 2, gate = "notIronHorde" },

            { FourCC('o029'), 3, gate = "spirit_notIron" },

            { FourCC('orai'), 5, gate = "fortress" },

            { FourCC('otau'), 5, gate = "fortress" },

        },

        [FourCC('obea')] = {

            { FourCC('o02B'), 2, gate = "ironHorde" },

            { FourCC('ohun'), 2, gate = "notIronHorde" },

            { FourCC('o01P'), 3, gate = "spirit_notIron" },

            { FourCC('okod'), 5, gate = "fortress" },

        },

        [FourCC('osld')] = {

            { FourCC('oshm'), 8 },

            { FourCC('o01W'), 2 },

        },

        [FourCC('otto')] = {

            { FourCC('ocat'), 2 },

            { FourCC('o022'), 1 },

            { FourCC('h0CY'), 2, gate = "ironHorde" },

        },

        [FourCC('oalt')] = {

            { FourCC('Ofar'), 1, limit = 1 },

            { FourCC('Obla'), 1, limit = 1 },

            { FourCC('Otch'), 1, limit = 1 },

        },

        worker = { id = FourCC('opeo'), cap = 25,

                   from = { FourCC('ogre'), FourCC('ostr'), FourCC('ofrt') } },

    },

    ecoWeights = {

        [FourCC('otrb')] = 1, [FourCC('ogre')] = 4,

        [FourCC('ostr')] = 6, [FourCC('ofrt')] = 8,

        [FourCC('obar')] = 3, [FourCC('obea')] = 2,

        [FourCC('ofor')] = 2, [FourCC('oalt')] = 3,

    },

    strategData = {

        gradeCap = 150,

        steps = {

            { before = 50, action = "research", rows = {

                {FourCC('ovln'), FourCC('Abds'), 1}, {FourCC('ovln'), FourCC('Arlm'), 1},

            }},

            { at = 17, action = "research", rows = {

                {FourCC('ogre'), FourCC('Ropg'), 1},

                {FourCC('ofor'), FourCC('R0G5'), 6}, {FourCC('ofor'), FourCC('R0E6'), 6}, {FourCC('ofor'), FourCC('Rome'), 6}, {FourCC('ofor'), FourCC('Roar'), 6}, {FourCC('ofor'), FourCC('Rora'), 6}, {FourCC('ofor'), FourCC('Rosp'), 3}, {FourCC('ofor'), FourCC('Rorb'), 3},

                {FourCC('obar'), FourCC('R0EC'), 3}, {FourCC('obea'), FourCC('R0ED'), 3}, {FourCC('otto'), FourCC('R0EF'), 3},

                {FourCC('osld'), FourCC('Rost'), 3}, {FourCC('osld'), FourCC('Rowt'), 3}, {FourCC('osld'), FourCC('Rowd'), 3},

            }},

            { at = 17, action = "tryBuy" },

            { at = 17, action = "fleet", wall = FourCC('h0HO') },

            { at = 25, action = "techUp", from = FourCC('ogre'), to = FourCC('ostr'), cap = 3 },

            { at = 55, action = "techUp", from = FourCC('ostr'), to = FourCC('ofrt'), cap = 3 },

            { at = 60, action = "mageTp" },

            { action = "random", branches = {

                { {FourCC('ovln'), FourCC('R0F3'), 1}, {FourCC('ovln'), FourCC('R0F4'), 1}, {FourCC('ovln'), FourCC('R0EH'), 1}, {FourCC('ovln'), FourCC('R0EI'), 1} },

                { {FourCC('ovln'), FourCC('R0EE'), 1}, {FourCC('ovln'), FourCC('R0EA'), 1}, {FourCC('ovln'), FourCC('R0E9'), 1}, {FourCC('ovln'), FourCC('R0E5'), 1} },

                { {FourCC('ovln'), FourCC('R0E4'), 1}, {FourCC('ovln'), FourCC('R0E3'), 1}, {FourCC('ovln'), FourCC('R0E1'), 1}, {FourCC('ovln'), FourCC('R0E0'), 1} },

                { {FourCC('ovln'), FourCC('R0DZ'), 1}, {FourCC('ovln'), FourCC('R0DY'), 1}, {FourCC('ovln'), FourCC('R0DX'), 1}, {FourCC('ovln'), FourCC('R0DW'), 1} },

                { {FourCC('ovln'), FourCC('R0EB'), 1}, {FourCC('ovln'), FourCC('R0EH'), 1}, {FourCC('ovln'), FourCC('R0DZ'), 1}, {FourCC('ovln'), FourCC('R0E5'), 1} },

            }},

        },

    },

    attackerData = {

        [FourCC('o01W')] = {

            { order = "bloodlust", chance = 4, type = "target" },

            { order = "lightningshield", chance = 4, type = "target" },

            { order = "purge", chance = 4, type = "target" },

        },

        [FourCC('h0CY')] = {

            { order = "berserk", chance = 3, type = "immediate" },

            { order = "selfdestruct", chance = 6, type = "immediate", hp = 20 },

        },

        [FourCC('o01J')] = {

            { order = "bloodlust", chance = 4, type = "target" },

            { order = "lightningshield", chance = 4, type = "target" },

            { order = "purge", chance = 4, type = "target" },

            { order = "dispel", chance = 4, type = "point" },

        },

        [FourCC('o01V')] = {

            { order = "soulburn", chance = 4, type = "target" },

            { order = "waterelemental", chance = 4, type = "immediate" },

            { order = "monsoon", chance = 4, type = "point" },

            { order = "dispel", chance = 4, type = "point" },

        },

        [FourCC('o023')] = {

            { order = "flamestrike", chance = 4, type = "point" },

            { order = "stampede", chance = 5, type = "point" },

        },

        [FourCC('o024')] = {

            { order = "evileye", chance = 4, type = "point" },

            { order = "stasistrap", chance = 4, type = "point" },

            { order = "healingward", chance = 4, type = "self" },

        },

        [FourCC('o02L')] = {

            { order = "evileye", chance = 4, type = "point" },

            { order = "stasistrap", chance = 4, type = "point" },

            { order = "healingward", chance = 4, type = "self" },

            { order = "acidbomb", chance = 5, type = "target" },

        },

        [FourCC('Obla')] = {

            { order = "windwalk", chance = 3, type = "immediate" },

            { order = "roar", chance = 5, type = "immediate" },

            { order = "whirlwind", chance = 5, type = "immediate" },

        },

        [FourCC('Ofar')] = {

            { order = "chainlightning", chance = 4, type = "target" },

            { order = "spiritwolf", chance = 6, type = "immediate" },

            { order = "monsoon", chance = 6, type = "point" },

        },

        [FourCC('Otch')] = {

            { order = "stomp", chance = 4, type = "immediate" },

            { order = "carrionswarm", chance = 6, type = "point" },

        },

        [FourCC('O02Z')] = {

            { order = "stomp", chance = 4, type = "immediate" },

            { order = "carrionswarm", chance = 6, type = "point" },

        },

        [FourCC('h0D0')] = {

            { order = "clusterrockets", chance = 4, type = "point" },

            { order = "blackarrowon", chance = 5, type = "target" },

            { order = "tranquility", chance = 6, type = "immediate", hp = 40 },

        },

    },

    getLvlData = {

        [FourCC('Obla')] = { ult = FourCC('AOww'), skills = { FourCC('A12F'), FourCC('AOcr') } },

        [FourCC('Ofar')] = { skills = { FourCC('A12E'), FourCC('AOcl'), FourCC('AOsf'), FourCC('AOfs') } },

        [FourCC('Otch')] = { ult = FourCC('AOre'), skills = { FourCC('AOre'), FourCC('AOr2'), FourCC('A026') } },

        [FourCC('O02Z')] = { ult = FourCC('AOre'), skills = { FourCC('AOre'), FourCC('AOr2'), FourCC('A026') } },

    },

    chooseBuild = ChooseBuildings_Horde,

    perebor = PereborBuildings_Horde,

    join = Join_Horde,

    strateg = Strateg_Horde,

    strategEC = Strateg_Horde_EC,

    upgrade = UpgradeHorde,

    naval = aiNavalTrain_Horde,

    wall = FourCC('h0HO'),

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

        [FourCC('oshm')] = 0.20,

        [FourCC('orai')] = 0.125,

        [FourCC('otau')] = 0.125,

        [FourCC('okod')] = 0.125,

        [FourCC('o029')] = 0.075,

        [FourCC('o01P')] = 0.075,

        [FourCC('o01N')] = 0.05,

        [FourCC('ogru')] = 0.05,

        [FourCC('o02B')] = 0.05,

        [FourCC('ohun')] = 0.05,

        [FourCC('o01W')] = 0.05,

        [FourCC('ocat')] = 0.05,

        [FourCC('h0CY')] = 0.05,

        [FourCC('o022')] = 0.025,

    },

})
