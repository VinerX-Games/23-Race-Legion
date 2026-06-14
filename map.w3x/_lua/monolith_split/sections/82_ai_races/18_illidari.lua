function Join_Illidari(id, pi, u)

    if id == FourCC('h0EI') then

        GroupAddUnit(udg_Ai_builders[pi], u)

    elseif aiUnitJoinsCapitalGuard(u, pi) then

    else

        aiUnitJoinsArmy(u, pi)

    end

end



RegisterAiRace("Illidari", {

    tokens = {"illidari", "illidan"},

    weight = 1,

    altar = FourCC('h0ED'),

    start = startIllidari,

    buildings = {

        seed = FourCC('h0EC'),

        { FourCC('h0E9'), 4, 4 }, { FourCC('h0EC'), 18, 4 },

        { FourCC('h0ED'), 3, 6 }, { FourCC('h0EE'), 10, 4 },

        { FourCC('h0EF'), 8, 6, gate = "tier2" }, { FourCC('h0EG'), 8, 6, gate = "tier2" },

        { FourCC('o01C'), 8, 4 }, { FourCC('h0EH'), 5, 2 },

        { FourCC('h0EM'), 5, 2 }, { FourCC('h0EN'), 4, 2 },

    },

    gates = {

        tier2 = function(pi) return getAiCount(pi, FourCC('h0EA')) + getAiCount(pi, FourCC('h0EB')) >= 1 end,

    },

    production = {

        [FourCC('h0EE')] = {

            {FourCC('h0EJ'), 3}, {FourCC('o01A'), 3}, {FourCC('o01B'), 2}, {FourCC('o019'), 2},

        },

        [FourCC('h0EF')] = {

            {FourCC('h0EK'), 3}, {FourCC('h0EL'), 3},

        },

        [FourCC('h0EG')] = {

            {FourCC('n02O'), 4}, {FourCC('n02M'), 3}, {FourCC('n02N'), 2},

        },

        [FourCC('o01C')] = {

            {FourCC('h04Y'), 3}, {FourCC('h04Z'), 3}, {FourCC('h050'), 2},

        },

        [FourCC('h0ED')] = {

            {FourCC('H043'), 1, limit = 1}, {FourCC('E01W'), 1, limit = 1}, {FourCC('E025'), 1, limit = 1},

        },

        worker = { id = FourCC('h0EI'), cap = 18, from = { FourCC('h0E9'), FourCC('h0EA'), FourCC('h0EB') } },
},

    ecoWeights = {

        [FourCC('h0EC')] = 1, [FourCC('h0E9')] = 2,

        [FourCC('h0EA')] = 5, [FourCC('h0EB')] = 8,

    },

    strategData = {

        gradeCap = 100,

        steps = {

            -- Real Illidari grades from the Forge (h0EM): fel weapon/armor + mastery.
            { at = 17, action = "research", rows = {
                {FourCC('h0EM'),FourCC('R08T'),6},  -- cursed weapon
                {FourCC('h0EM'),FourCC('R08U'),6},  -- defiled armor
                {FourCC('h0EM'),FourCC('R08W'),6},  -- fel weapon
                {FourCC('h0EM'),FourCC('R08V'),6},  -- fel reinforcement
                {FourCC('h0EM'),FourCC('R08X'),6},  -- magic mastery
            }},

            { at = 20, action = "tryBuy" },

            { at = 25, action = "techUp", from = FourCC('h0E9'), to = FourCC('h0EA'), cap = 3 },

            { at = 55, action = "techUp", from = FourCC('h0EA'), to = FourCC('h0EB'), cap = 3 },

        },

    },

    attackerData = {

        [FourCC('h0EK')] = {

            { order = "firebolt",    chance = 5, type = "target" },

            { order = "flamestrike", chance = 5, type = "point" },

        },

        [FourCC('h0EL')] = {

            { order = "thunderbolt", chance = 5, type = "target" },

            { order = "monsoon",     chance = 5, type = "point" },

        },

        [FourCC('n02O')] = {

            { order = "frostnova",   chance = 4, type = "target" },

            { order = "blizzard",    chance = 4, type = "point" },

        },

        [FourCC('n02M')] = {

            { order = "sleep",       chance = 4, type = "target" },

        },

        [FourCC('n02N')] = {

            { order = "carrionswarm", chance = 4, type = "point" },

            { order = "curse",        chance = 4, type = "target" },

        },

        [FourCC('h04Y')] = {

            { order = "blink",        chance = 4, type = "point" },

            { order = "shadowstrike", chance = 4, type = "target", notStructure = true },

        },

        [FourCC('h04Z')] = {

            { order = "faeriefire",   chance = 4, type = "target" },

            { order = "entanglingroots", chance = 4, type = "target" },

        },

    },

    join = Join_Illidari,

    wall = FourCC('h0EN'),

    shipyard = FourCC('h011'),  -- human worker (hpea) -> human Верфь


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
        [FourCC('h0EI')] = 0.2000,
        [FourCC('n02O')] = 0.0889,
        [FourCC('h0EJ')] = 0.0667,
        [FourCC('o01A')] = 0.0667,
        [FourCC('h0EK')] = 0.0667,
        [FourCC('h0EL')] = 0.0667,
        [FourCC('n02M')] = 0.0667,
        [FourCC('h04Y')] = 0.0667,
        [FourCC('h04Z')] = 0.0667,
        [FourCC('o01B')] = 0.0444,
        [FourCC('o019')] = 0.0444,
        [FourCC('n02N')] = 0.0444,
        [FourCC('h050')] = 0.0444,
        [FourCC('H043')] = 0.0222,
        [FourCC('E01W')] = 0.0222,
        [FourCC('E025')] = 0.0222,
    },
})



---@param id integer

---@param pi integer

---@param u unit
