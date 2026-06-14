function Join_Undead(id, pi, u)

    if id == FourCC('u00P') then

        GroupAddUnit(udg_Ai_builders[pi], u)

    elseif aiUnitJoinsCapitalGuard(u, pi) then

    else

        aiUnitJoinsArmy(u, pi)

    end

end



RegisterAiRace("Undead", {

    tokens = {"undead", "scourge"},

    weight = 1,

    altar = FourCC('u00K'),

    start = startUndead,

    workerFighter = FourCC('u00P'),  -- ghouls harvest wood AND fight

    buildings = {

        seed = FourCC('u00H'),

        { FourCC('n014'), 4, 4 }, { FourCC('u00H'), 18, 4 },

        { FourCC('u00K'), 3, 6 }, { FourCC('u00M'), 10, 4 },

        { FourCC('u00N'), 8, 6, gate = "tier2" }, { FourCC('u00L'), 5, 2 },

        { FourCC('n012'), 8, 4 },

    },

    gates = {

        tier2 = function(pi) return getAiCount(pi, FourCC('u00F')) + getAiCount(pi, FourCC('u00G')) >= 1 end,

    },

    production = {

        [FourCC('n012')] = {

            {FourCC('n011'), 3}, {FourCC('n013'), 2}, {FourCC('u03E'), 2},

        },

        [FourCC('u00M')] = {

            {FourCC('u00A'), 4}, {FourCC('u00B'), 3}, {FourCC('u00D'), 2},

        },

        [FourCC('u00N')] = {

            {FourCC('u00C'), 3}, {FourCC('u008'), 3}, {FourCC('u00E'), 2},

        },

        [FourCC('u00K')] = {

            {FourCC('U00O'), 1, limit = 1}, {FourCC('U00V'), 1, limit = 1}, {FourCC('U00U'), 1, limit = 1},

        },

        worker = { id = FourCC('u00P'), cap = 18, from = { FourCC('n014'), FourCC('u00F'), FourCC('u00G') } },
},

    ecoWeights = {

        [FourCC('u00H')] = 1, [FourCC('n014')] = 2,

        [FourCC('u00F')] = 5, [FourCC('u00G')] = 8,

    },

    strategData = {

        gradeCap = 100,

        steps = {

            -- Real Undead grades from the Graveyard (u00L): monster weapon/armor +
            -- unholy weapon/armor + tools. Old rows issued abilities (Abds/Arlm) that
            -- never fire RESEARCH_FINISH so Grades stayed 0.
            { at = 17, action = "research", rows = {
                {FourCC('u00L'),FourCC('R05N'),6},  -- monster attack (weapon)
                {FourCC('u00L'),FourCC('R05P'),6},  -- monster armor
                {FourCC('u00L'),FourCC('R05O'),6},  -- unholy strength (weapon)
                {FourCC('u00L'),FourCC('R05Q'),6},  -- unholy armor
                {FourCC('u00L'),FourCC('R0DQ'),6},  -- improved tools
            }},

            { at = 20, action = "tryBuy" },

            { at = 25, action = "techUp", from = FourCC('n014'), to = FourCC('u00F'), cap = 3 },

            { at = 55, action = "techUp", from = FourCC('u00F'), to = FourCC('u00G'), cap = 3 },

        },

    },

    attackerData = {

        [FourCC('u00A')] = {

            { order = "cannibalize", chance = 4, type = "immediate", hp = 50 },

        },

        [FourCC('u00B')] = {

            { order = "web",    chance = 4, type = "target" },

            { order = "burrow", chance = 4, type = "immediate" },

        },

        [FourCC('u00C')] = {

            { order = "raisedead",     chance = 4, type = "point" },

            { order = "cripple",       chance = 4, type = "target" },

            { order = "unholyfrenzy",  chance = 4, type = "target" },

        },

        [FourCC('u008')] = {

            { order = "curse",             chance = 4, type = "target" },

            { order = "antimagicshell",    chance = 4, type = "target" },

            { order = "possession",        chance = 4, type = "target" },

        },

        [FourCC('u00D')] = {

            { order = "cannibalize", chance = 4, type = "immediate", hp = 50 },

        },

        [FourCC('u00E')] = {

            { order = "exhumecorpses", chance = 4, type = "immediate" },

        },

        [FourCC('u03E')] = {

            { order = "devourmagic", chance = 4, type = "target", range = 525 },

        },

        [FourCC('U00O')] = {

            { order = "deathcoil",    chance = 5, type = "target" },

            { order = "deathpact",    chance = 5, type = "target" },

            { order = "animatedead",  chance = 5, type = "immediate" },

        },

        [FourCC('U00V')] = {

            { order = "frostnova",    chance = 5, type = "target" },

            { order = "frostarmor",   chance = 5, type = "target" },

            { order = "darkritual",   chance = 5, type = "target" },

        },

        [FourCC('U00U')] = {

            { order = "impales",      chance = 5, type = "point" },

            { order = "carrionswarm", chance = 5, type = "point" },

            { order = "locustswarm",  chance = 5, type = "immediate" },

        },

    },

    attackedData = {

        [FourCC('u00A')] = {

            { order = "cannibalize", chance = 3, type = "immediate", hp = 50 },

        },

    },

    getLvlData = {

        [FourCC('U00O')] = { skills = { FourCC('A0CO'), FourCC('A0CP'), FourCC('A0CR'), FourCC('A0CN') } },

        [FourCC('U00V')] = { skills = { FourCC('AQ95'), FourCC('UN99'), FourCC('A0CS'), FourCC('AQ11') } },

        [FourCC('U00U')] = { skills = { FourCC('A0CK'), FourCC('A0CM'), FourCC('A0BW'), FourCC('A1Q7') } },

    },

    join = Join_Undead,

    wall = FourCC('u00I'),

    shipyard = FourCC('h0D1'),  -- Undead Верфь (wall is Spirit Tower)


    diplomat = "isolationist",

    brain = "objective",

    brainWeights = {
        kind  = { capital = 100, cluster = 40, capture = 60, weak = 20, front = 15 },
        value = 1.0, dist = 0.002, claim = 25.0, siege = 0.5,
        focusMargin = 30.0, homeThreat = 20.0, tpDist = 6000.0,
        rHome = 2500.0, rCluster = 1600.0,
        clusterEvery = 8, topK = 8,
    },
    compTarget = {
        [FourCC('u00P')] = 0.2500,
        [FourCC('u00A')] = 0.1111,
        [FourCC('n011')] = 0.0833,
        [FourCC('u00B')] = 0.0833,
        [FourCC('u00C')] = 0.0833,
        [FourCC('u008')] = 0.0833,
        [FourCC('n013')] = 0.0556,
        [FourCC('u03E')] = 0.0556,
        [FourCC('u00D')] = 0.0556,
        [FourCC('u00E')] = 0.0556,
        [FourCC('U00O')] = 0.0278,
        [FourCC('U00V')] = 0.0278,
        [FourCC('U00U')] = 0.0278,
    },
})



-- ====================================================================
-- Cult of the Damned (Культ Проклятых). A fully playable race that was never
-- ported to the AI: own building set (cD*) + acolyte worker cD02, shares only the
-- Undead Верфь (h0D1). Modeled on the Undead entry (same acolyte base). Single-tier
-- (Necropolis cD26 does not tier-up). Grades are real research upgrades at the
-- Graveyard cD31. FIRST VERSION — validate live (worker pooling, build order, no
-- freeze/crash) on next launch; unit ratios are best-effort without live data.
-- ====================================================================
---@param id integer
---@param pi integer
---@param u unit
