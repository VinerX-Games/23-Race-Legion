function Join_Alliance(id, pi, u)

    if id == FourCC('hpea') then

        GroupAddUnit(udg_Ai_builders[pi], u)

    elseif aiUnitJoinsCapitalGuard(u, pi) then

    else

        aiUnitJoinsArmy(u, pi)

    end

end



RegisterAiRace("Alliance", {

    tokens = {"alliance", "ally"},

    weight = 1,

    altar = FourCC('halt'),

    start = startAlliance,

    buildings = {

        seed = FourCC('hhou'),

        { FourCC('htow'), 4, 4 }, { FourCC('hhou'), 18, 4 },

        { FourCC('hbar'), 10, 4 }, { FourCC('halt'), 3, 6 },

        { FourCC('harm'), 5, 2 }, { FourCC('hbla'), 8, 6, gate = "tier2" },

        { FourCC('hars'), 8, 6, gate = "tier2" },

        { FourCC('hwtw'), 4, 2 },

    },

    gates = {

        tier2 = function(pi) return getAiCount(pi, FourCC('hkee')) + getAiCount(pi, FourCC('hcas')) >= 1 end,

    },

    production = {

        [FourCC('hbar')] = {

            {FourCC('hfoo'), 4}, {FourCC('hkni'), 3},

        },

        [FourCC('hbla')] = {

            {FourCC('hrif'), 3}, {FourCC('hmtm'), 2},

        },

        [FourCC('hars')] = {

            {FourCC('hsor'), 3}, {FourCC('hmpr'), 3},

        },

        [FourCC('halt')] = {

            {FourCC('Hpal'), 1, limit = 1}, {FourCC('Hamg'), 1, limit = 1}, {FourCC('Hmkg'), 1, limit = 1},

        },

        worker = { id = FourCC('hpea'), cap = 18, from = { FourCC('htow'), FourCC('hkee'), FourCC('hcas') } },
},

    ecoWeights = {

        [FourCC('hhou')] = 1, [FourCC('htow')] = 2,

        [FourCC('hkee')] = 5, [FourCC('hcas')] = 8,

    },

    strategData = {

        gradeCap = 100,

        steps = {
            { at = 17, action = "research", rows = {
                {FourCC('hbla'),FourCC('R0HO'),6},  -- ranged
                {FourCC('hbla'),FourCC('Rhar'),6},  -- armor
                {FourCC('hbla'),FourCC('Rhla'),6},  -- armor
                {FourCC('hbla'),FourCC('Rhme'),6},  -- melee
                {FourCC('hbla'),FourCC('Rhra'),6},  -- ranged
            }},


            { at = 17, action = "random", branches = {

                { {FourCC('harm'),FourCC('Abds'),6},{FourCC('harm'),FourCC('Arlm'),6} },

                { {FourCC('hbar'),FourCC('Abds'),6} },

                { {FourCC('hbla'),FourCC('Abds'),6},{FourCC('hars'),FourCC('Abds'),6} },

            }},

            { at = 20, action = "tryBuy" },

            { at = 25, action = "techUp", from = FourCC('htow'), to = FourCC('hkee'), cap = 3 },

            { at = 55, action = "techUp", from = FourCC('hkee'), to = FourCC('hcas'), cap = 3 },

        },

    },

    attackerData = {

        [FourCC('Hpal')] = {

            { order = "holybolt",     chance = 5, type = "target" },

            { order = "divineshield", chance = 5, type = "immediate" },

            { order = "resurrection", chance = 5, type = "immediate" },

        },

        [FourCC('Hamg')] = {

            { order = "blizzard",        chance = 5, type = "point" },

            { order = "waterelemental",  chance = 5, type = "immediate" },

            { order = "massteleport",    chance = 5, type = "immediate" },

        },

        [FourCC('Hmkg')] = {

            { order = "stormbolt",    chance = 5, type = "target" },

            { order = "thunderclap",  chance = 5, type = "immediate" },

            { order = "avatar",       chance = 5, type = "immediate" },

        },

        [FourCC('hsor')] = {

            { order = "slow",         chance = 4, type = "target" },

            { order = "polymorph",    chance = 4, type = "target", notStructure = true },

            { order = "invisibility", chance = 4, type = "target" },

        },

        [FourCC('hmpr')] = {

            { order = "heal",       chance = 4, type = "heal", allyRange = 550 },

            { order = "dispel",     chance = 4, type = "point", range = 490 },

            { order = "innerfire",  chance = 4, type = "target" },

        },

    },

    attackedData = {

        [FourCC('hfoo')] = {

            { order = "defend",   chance = 3, type = "immediate" },

            { order = "undefend", chance = 3, type = "immediate" },

        },

    },

    getLvlData = {

        [FourCC('Hpal')] = { ult = FourCC('AHre'), skills = { FourCC('AHhb'), FourCC('AHds'), FourCC('AHad') } },

        [FourCC('Hamg')] = { ult = FourCC('AHmt'), skills = { FourCC('AHbz'), FourCC('AHwe'), FourCC('AHab') } },

        [FourCC('Hmkg')] = { ult = FourCC('AHav'), skills = { FourCC('AHtc'), FourCC('AHtb'), FourCC('AHbh') } },

    },

    join = Join_Alliance,

    wall = FourCC('hgtw'),

    shipyard = FourCC('h011'),  -- human worker (hpea) -> human Верфь


    diplomat = "loyal",

    brain = "objective",

    brainWeights = {
        kind  = { capital = 100, cluster = 40, capture = 60, weak = 20, front = 15 },
        value = 1.0, dist = 0.002, claim = 25.0, siege = 0.5,
        focusMargin = 30.0, homeThreat = 20.0, tpDist = 6000.0,
        rHome = 2500.0, rCluster = 1600.0,
        clusterEvery = 8, topK = 8,
    },
    compTarget = {
        [FourCC('hpea')] = 0.3000,
        [FourCC('hfoo')] = 0.1333,
        [FourCC('hkni')] = 0.1000,
        [FourCC('hrif')] = 0.1000,
        [FourCC('hsor')] = 0.1000,
        [FourCC('hmpr')] = 0.1000,
        [FourCC('hmtm')] = 0.0667,
        [FourCC('Hpal')] = 0.0333,
        [FourCC('Hamg')] = 0.0333,
        [FourCC('Hmkg')] = 0.0333,
    },
})



---@param id integer

---@param pi integer

---@param u unit
