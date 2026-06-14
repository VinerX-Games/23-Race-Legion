RegisterAiRace("Goblins", {

    tokens = {"goblins", "gob"},

    weight = 1,

    altar = FourCC('o016'),

    start = startGoblins,

    buildings = {

        seed = FourCC('h077'),

        { FourCC('h070'), 4, 5 }, { FourCC('h077'), 20, 3 }, { FourCC('h073'), 18, 7 },

        { FourCC('h07S'), 30, 1 }, { FourCC('h079'), 5, 3 }, { FourCC('h076'), 18, 4 },

        { FourCC('o016'), 3, 8 },

        { FourCC('h074'), 15, 2, gate = "grades8" }, { FourCC('h075'), 15, 2, gate = "grades8" },

    },

    gates = {

        grades8 = function(pi) return Grades[pi] > 8 end,

    },

    production = {

        worker = { id = FourCC('n00V'), cap = 25, from = { FourCC('h070') } },

        [FourCC('h074')] = {

            { FourCC('h06S'), 2 }, { FourCC('h06U'), 2 },

            { FourCC('h06Y'), 4 }, { FourCC('h06R'), 3 }, { FourCC('h06T'), 3 },

        },

        [FourCC('h075')] = {

            { FourCC('o00W'), 2 }, { FourCC('o00Y'), 2 },

            { FourCC('o00X'), 3 }, { FourCC('h06P'), 3 },

        },

        [FourCC('o016')] = {

            { FourCC('H0BD'), 1, limit = 1 },

            { FourCC('Galh'), 1, limit = 1 },

            { FourCC('Gmex'), 1, limit = 1 },

        },

        pre = function(id, pi, u)

            if id == FourCC('h073') then

                if Random(1, 6) then

                    IssueNeutralImmediateOrderById(Player(pi), u, FourCC('h07R'))

                else

                    return false

                end

                return true

            end

            return false

        end,

        [FourCC('h073')] = {

            { FourCC('h06K'), 2 },

            { FourCC('h060'), 1, gate = "grades8" },

            { FourCC('h06Q'), 3, gate = "grades8" },

            { FourCC('h06L'), 3, gate = "grades8" },

            { FourCC('h06N'), 3, gate = "grades8" },

            { FourCC('h078'), 3, gate = "grades8" },

            { FourCC('h06M'), 3, gate = "grades8" },

        },

    },

    ecoWeights = {

        [FourCC('h077')] = 1, [FourCC('h070')] = 4,

    },

    strategData = {

        gradeCap = 150,

        steps = {

            { at = 17, action = "research", rows = {

                {FourCC('h076'), FourCC('R04P'), 6}, {FourCC('h076'), FourCC('R04E'), 6}, {FourCC('h076'), FourCC('R04F'), 6}, {FourCC('h076'), FourCC('R04G'), 6}, {FourCC('h076'), FourCC('R04H'), 6},

                {FourCC('h076'), FourCC('R04I'), 6}, {FourCC('h076'), FourCC('R04J'), 6}, {FourCC('h076'), FourCC('R04K'), 6}, {FourCC('h076'), FourCC('R04L'), 6}, {FourCC('h076'), FourCC('R04M'), 6},

                {FourCC('h079'), FourCC('R056'), 6}, {FourCC('h079'), FourCC('R07A'), 6}, {FourCC('h079'), FourCC('R05X'), 6}, {FourCC('h079'), FourCC('R05Y'), 6}, {FourCC('h079'), FourCC('R04N'), 6},

                {FourCC('h079'), FourCC('R04Q'), 6}, {FourCC('h079'), FourCC('R04R'), 6}, {FourCC('h079'), FourCC('R053'), 6}, {FourCC('h079'), FourCC('R05W'), 6},

                {FourCC('h070'), FourCC('R0D4'), 6},

            }},

            { at = 17, action = "tryBuy" },

            { at = 60, action = "mageTp" },

        },

    },

    attackerData = {

        [FourCC('h06K')] = {

            { order = "flamestrike", chance = 4, type = "point" },

        },

        [FourCC('h06Y')] = {

            { order = "bearform", chance = 4, type = "immediate" },

        },

        [FourCC('h06Z')] = {

            { order = "bearform", chance = 4, type = "immediate" },

        },

        [FourCC('h06P')] = {

            { order = "berserk", chance = 3, type = "immediate" },

            { order = "dispel", chance = 6, type = "point", range = 280 },

            { order = "ward", chance = 6, type = "point" },

        },

        [FourCC('H0BD')] = {

            { order = "silence", chance = 5, type = "point" },

            { order = "clusterrockets", chance = 5, type = "point" },

            { order = "blizzard", chance = 5, type = "point" },

        },

        [FourCC('Galh')] = {

            { order = "transmute", chance = 5, type = "target" },

            { order = "acidbomb", chance = 5, type = "target" },

            { order = "chemicalrage", chance = 5, type = "immediate" },

            { order = "healingspray", chance = 5, type = "self" },

        },

        [FourCC('Gmex')] = {

            { order = "summonfactory", chance = 5, type = "point" },

            { order = "clusterrockets", chance = 5, type = "point" },

            { order = "robogoblin", chance = 5, type = "immediate" },

        },

        [FourCC('h06X')] = {

            { order = "berserk", chance = 4, type = "immediate" },

            { order = "blackarrowon", chance = 5, type = "target" },

            { order = "tranquility", chance = 6, type = "immediate", hp = 40 },

        },

        [FourCC('h06V')] = {

            { order = "ravenform", chance = 4, type = "immediate" },

        },

        [FourCC('h06W')] = {

            { order = "ravenform", chance = 4, type = "immediate" },

        },

        post = {

            { order = "berserk", chance = 4, type = "immediate", needAbil = FourCC('A0BL') },

        },

    },

    getLvlData = {

        [FourCC('H0BD')] = { ult = FourCC('A0D7'), skills = { FourCC('A0D8'), FourCC('AEar'), FourCC('A0D5') } },

        [FourCC('Galh')] = { ult = FourCC('ANtm'), skills = { FourCC('ANhs'), FourCC('ANab'), FourCC('ANcr') } },

        [FourCC('Gmex')] = { ult = FourCC('ANrg'), skills = { FourCC('ANsy'), FourCC('ANcs'), FourCC('ANeg') } },

    },

    chooseBuild = ChooseBuildings_Goblins,

    perebor = PereborBuildings_Goblins,

    join = Join_Goblins,

    strateg = Strateg_Goblins,

    strategEC = Strateg_Goblins_EC,

    naval = aiNavalTrain_Goblins,

    wall = FourCC('h0D7'),  -- Goblins' own Верфь (registered in AiTransportTypes); wall IS the shipyard


    diplomat = "diplomat",

    brain = "objective",

    brainWeights = {
        kind  = { capital = 100, cluster = 40, capture = 60, weak = 20, front = 15 },
        value = 1.0, dist = 0.002, claim = 25.0, siege = 0.5,
        focusMargin = 30.0, homeThreat = 20.0, tpDist = 6000.0,
        rHome = 2500.0, rCluster = 1600.0,
        clusterEvery = 8, topK = 8,
    },
    compTarget = {
        [FourCC('h06Y')] = 0.0851,
        [FourCC('h06R')] = 0.0638,
        [FourCC('h06T')] = 0.0638,
        [FourCC('o00X')] = 0.0638,
        [FourCC('h06P')] = 0.0638,
        [FourCC('h06Q')] = 0.0638,
        [FourCC('h06L')] = 0.0638,
        [FourCC('h06N')] = 0.0638,
        [FourCC('h078')] = 0.0638,
        [FourCC('h06M')] = 0.0638,
        [FourCC('n00V')] = 0.0426,
        [FourCC('h06S')] = 0.0426,
        [FourCC('h06U')] = 0.0426,
        [FourCC('o00W')] = 0.0426,
        [FourCC('o00Y')] = 0.0426,
        [FourCC('h06K')] = 0.0426,
        [FourCC('H0BD')] = 0.0213,
        [FourCC('Galh')] = 0.0213,
        [FourCC('Gmex')] = 0.0213,
        [FourCC('h060')] = 0.0213,
    },
})
