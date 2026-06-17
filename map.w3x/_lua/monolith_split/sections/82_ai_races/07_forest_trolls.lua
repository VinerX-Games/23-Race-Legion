function Join_ForestTrolls(id, pi, u)

    if id == FourCC('o04V') then

        GroupAddUnit(udg_Ai_builders[pi], u)

    elseif aiUnitJoinsCapitalGuard(u, pi) then

    else

        aiUnitJoinsArmy(u, pi)

    end

end



RegisterAiRace("ForestTrolls", {

    tokens = {"ft", "foresttrolls"},

    weight = 1,

    altar = FourCC('h0MU'),

    start = startForestTrolls,

    buildings = {

        seed = FourCC('h0MV'),

        { FourCC('h0MT'), 4, 4 }, { FourCC('h0MV'), 18, 4 },

        { FourCC('h0MS'), 10, 4 }, { FourCC('h0N7'), 5, 2 },

        { FourCC('h0MU'), 3, 6 }, { FourCC('h0N4'), 25, 1 },

        { FourCC('h0MZ'), 8, 6, gate = "tier2" },

        { FourCC('h0MR'), 8, 6, gate = "tier2" },

    },

    gates = {

        tier2 = function(pi)

            return getAiCount(pi, FourCC('h0N8')) + getAiCount(pi, FourCC('h0N9')) >= 1

        end,

    },

    production = {

        worker = { id = FourCC('o04V'), cap = 20, from = { FourCC('h0MT'), FourCC('h0N8'), FourCC('h0N9') } },

        [FourCC('h0MT')] = {

            { FourCC('o04X'), 1 },

        },

        [FourCC('h0N8')] = {

            { FourCC('o04X'), 1 },

        },

        [FourCC('h0N9')] = {

            { FourCC('o04X'), 1 },

        },

        [FourCC('h0MS')] = {

            { FourCC('o04W'), 5 },

            { FourCC('o04X'), 3 },

            { FourCC('o04Y'), 3, gate = "tier2" },

            { FourCC('o05F'), 2, gate = "tier2" },

        },

        [FourCC('h0MZ')] = {

            { FourCC('o051'), 3 },

            { FourCC('o052'), 3 },

        },

        [FourCC('h0MR')] = {

            { FourCC('o04Z'), 3 },

            { FourCC('o050'), 4 },

            { FourCC('o053'), 4 },

        },

        [FourCC('h0MU')] = {

            { FourCC('O059') }, { FourCC('O058') }, { FourCC('O057') },

            { FourCC('o05M'), 1, limit = 1, gate = "tier2" },

            { FourCC('o05N'), 1, limit = 1, gate = "tier2" },

            { FourCC('o05O'), 1, limit = 1, gate = "tier2" },

        },

    },

    ecoWeights = {

        [FourCC('h0MV')] = 1, [FourCC('h0MT')] = 2,

        [FourCC('h0N8')] = 5, [FourCC('h0N9')] = 8,

        [FourCC('h0MS')] = 2, [FourCC('h0N7')] = 2,

        [FourCC('h0MU')] = 3,

    },

    strategData = {

        gradeCap = 100,

        steps = {
            { at = 17, action = "research", rows = {
                {FourCC('h0N7'),FourCC('R0IU'),6},  -- melee
            }},


            { at = 17, action = "random", branches = {

                { {FourCC('h0N7'), FourCC('R0D2'), 6}, {FourCC('h0N7'), FourCC('R0D3'), 6} },

                { {FourCC('h0MS'), FourCC('R0DY'), 6}, {FourCC('h0MS'), FourCC('R0EE'), 6} },

                { {FourCC('h0MZ'), FourCC('R0EH'), 6}, {FourCC('h0MZ'), FourCC('R0EI'), 6} },

            }},

            { at = 20, action = "tryBuy" },

            { at = 25, action = "techUp", from = FourCC('h0MT'), to = FourCC('h0N8'), cap = 3 },

            { at = 55, action = "techUp", from = FourCC('h0N8'), to = FourCC('h0N9'), cap = 3 },

        },

    },

    attackerData = {

        [FourCC('o04W')] = {

            { order = "berserk", chance = 4, type = "immediate" },

        },

        [FourCC('o04Y')] = {

            { order = "berserk", chance = 4, type = "immediate" },

        },

        [FourCC('o04Z')] = {

            { order = "berserk", chance = 3, type = "immediate" },

        },

        [FourCC('o053')] = {

            { order = "thunderbolt", chance = 4, type = "target" },

            { order = "berserk", chance = 4, type = "immediate" },

        },

        [FourCC('o050')] = {

            { order = "Thornyshield", chance = 4, type = "target" },

        },

        [FourCC('o051')] = {

            { order = "clusterrockets", chance = 4, type = "point" },

            { order = "ward", chance = 4, type = "point" },

        },

        [FourCC('o052')] = {

            { order = "heal", chance = 4, type = "heal", allyRange = 550 },

            { order = "dispel", chance = 4, type = "point" },

            { order = "innerfire", chance = 4, type = "target" },

        },

        [FourCC('o05M')] = {

            { order = "roar", chance = 4, type = "immediate" },

        },

        [FourCC('o05N')] = {

            { order = "howlofterror", chance = 4, type = "immediate" },

            { order = "berserk", chance = 4, type = "immediate" },

        },

        [FourCC('o05O')] = {

            { order = "chainlightning", chance = 4, type = "target" },

            { order = "monsoon", chance = 4, type = "point" },

        },

    },

    join = Join_ForestTrolls,

    naval = aiNavalTrain_JungleTrolls,

    wall = FourCC('h0N4'),

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
        [FourCC('o04V')] = 0.2000,
        [FourCC('o04X')] = 0.1333,
        [FourCC('o04W')] = 0.1111,
        [FourCC('o050')] = 0.0889,
        [FourCC('o053')] = 0.0889,
        [FourCC('o04Y')] = 0.0667,
        [FourCC('o051')] = 0.0667,
        [FourCC('o052')] = 0.0667,
        [FourCC('o04Z')] = 0.0667,
        [FourCC('o05F')] = 0.0444,
        [FourCC('o05M')] = 0.0222,
        [FourCC('o05N')] = 0.0222,
        [FourCC('o05O')] = 0.0222,
    },
})



---@param id integer

---@param pi integer

---@param u unit
