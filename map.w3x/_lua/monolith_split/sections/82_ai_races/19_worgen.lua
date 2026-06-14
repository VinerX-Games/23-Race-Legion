function Join_Worgen(id, pi, u)

    if id == FourCC('h0IT') then

        GroupAddUnit(udg_Ai_builders[pi], u)

    elseif aiUnitJoinsCapitalGuard(u, pi) then

    else

        aiUnitJoinsArmy(u, pi)

    end

end



RegisterAiRace("Worgen", {

    tokens = {"worgen", "gilneas"},

    weight = 1,

    altar = FourCC('h0IN'),

    start = startWorgen,

    buildings = {

        seed = FourCC('h0IM'),

        { FourCC('h0IK'), 4, 4 }, { FourCC('h0IM'), 18, 4 },

        { FourCC('h0IN'), 3, 6 }, { FourCC('h0IO'), 10, 4 },

        { FourCC('h0IR'), 8, 6, gate = "tier2" }, { FourCC('h0IS'), 8, 6, gate = "tier2" },

        { FourCC('h0IQ'), 5, 2 }, { FourCC('h0JT'), 4, 2 },

    },

    gates = {

        tier2 = function(pi) return getAiCount(pi, FourCC('h0IL')) >= 1 end,

    },

    production = {

        [FourCC('h0IO')] = {

            {FourCC('h0IU'), 3}, {FourCC('h0IV'), 3}, {FourCC('o02T'), 2},

        },

        [FourCC('h0IR')] = {

            {FourCC('h0NA'), 2}, {FourCC('h0IW'), 3}, {FourCC('h0J0'), 2},

        },

        [FourCC('h0IS')] = {

            {FourCC('h0J1'), 3}, {FourCC('h0IX'), 2},

        },

        [FourCC('h0IN')] = {

            {FourCC('H0J2'), 1, limit = 1}, {FourCC('H0J6'), 1, limit = 1}, {FourCC('H0J7'), 1, limit = 1},

        },

        worker = { id = FourCC('h0IT'), cap = 18, from = { FourCC('h0IK'), FourCC('h0IL') } },
},

    ecoWeights = {

        [FourCC('h0IM')] = 1, [FourCC('h0IK')] = 2,

        [FourCC('h0IL')] = 8,

    },

    strategData = {

        gradeCap = 100,

        steps = {

            -- Real weapon/armor research (was Abds placeholders = no-ops, so Worgen's
            -- grades stuck at 0 and its army never upgraded). h0IQ is the blacksmith;
            -- R0EM..R0EP are 6-level, R0EQ is 3-level. Tier-2 forges h0IR/h0IS unlock
            -- the higher upgrades once tier2 is reached.
            { at = 17, action = "research", rows = {
                {FourCC('h0IQ'), FourCC('R0EM'), 6}, {FourCC('h0IQ'), FourCC('R0EN'), 6},
                {FourCC('h0IQ'), FourCC('R0EO'), 6}, {FourCC('h0IQ'), FourCC('R0EP'), 6},
                {FourCC('h0IQ'), FourCC('R0EQ'), 3},
            }},

            { at = 35, gate = "tier2", action = "research", rows = {
                {FourCC('h0IR'), FourCC('R0IP'), 3}, {FourCC('h0IR'), FourCC('R0F6'), 3},
                {FourCC('h0IR'), FourCC('R0F5'), 3}, {FourCC('h0IR'), FourCC('R0EZ'), 3},
                {FourCC('h0IS'), FourCC('R0F1'), 3}, {FourCC('h0IS'), FourCC('R0F0'), 3},
                {FourCC('h0IS'), FourCC('R0F2'), 3},
            }},

            { at = 20, action = "tryBuy" },

            { at = 25, action = "techUp", from = FourCC('h0IK'), to = FourCC('h0IL'), cap = 3 },

        },

    },

    attackerData = {

        [FourCC('h0IU')] = {

            { order = "frenzyon",    chance = 4, type = "immediate" },

            { order = "berserk",     chance = 4, type = "immediate" },

        },

        [FourCC('h0IV')] = {

            { order = "windwalk",     chance = 4, type = "immediate" },

            { order = "shadowstrike", chance = 4, type = "target", notStructure = true },

        },

        [FourCC('o02T')] = {

            { order = "howlofterror", chance = 4, type = "immediate" },

            { order = "roar",         chance = 4, type = "immediate" },

        },

        [FourCC('h0NA')] = {

            { order = "carrionswarm", chance = 4, type = "point" },

        },

        [FourCC('h0IW')] = {

            { order = "cannibalize", chance = 4, type = "immediate", hp = 50 },

        },

        [FourCC('h0J1')] = {

            { order = "faeriefire", chance = 4, type = "target" },

            { order = "curse",      chance = 4, type = "target" },

        },

    },

    getLvlData = {

        [FourCC('H0J2')] = { skills = { FourCC('A11I'), FourCC('A11H'), FourCC('A11J'), FourCC('A11K') } },

        [FourCC('H0J6')] = { skills = { FourCC('A11L'), FourCC('A11N'), FourCC('A11M'), FourCC('A11O') } },

        [FourCC('H0J7')] = { skills = { FourCC('A11Q'), FourCC('A11P'), FourCC('A11R'), FourCC('A11S') } },

    },

    join = Join_Worgen,

    wall = FourCC('h0JT'),

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
        [FourCC('h0IT')] = 0.2069,
        [FourCC('h0IU')] = 0.1034,
        [FourCC('h0IV')] = 0.1034,
        [FourCC('h0IW')] = 0.1034,
        [FourCC('h0J1')] = 0.1034,
        [FourCC('o02T')] = 0.0690,
        [FourCC('h0NA')] = 0.0690,
        [FourCC('h0J0')] = 0.0690,
        [FourCC('h0IX')] = 0.0690,
        [FourCC('H0J2')] = 0.0345,
        [FourCC('H0J6')] = 0.0345,
        [FourCC('H0J7')] = 0.0345,
    },
})



---@param id integer

---@param pi integer

---@param u unit
