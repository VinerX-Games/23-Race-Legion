function Join_Vrykul(id, pi, u)

    if id == FourCC('h0C9') then

        GroupAddUnit(udg_Ai_builders[pi], u)

    elseif aiUnitJoinsCapitalGuard(u, pi) then

    else

        aiUnitJoinsArmy(u, pi)

    end

end



RegisterAiRace("Vrykul", {

    tokens = {"vrykul", "vryculs"},

    weight = 1,

    altar = FourCC('h0BU'),

    start = startVrykul,

    buildings = {

        seed = FourCC('h0BT'),

        { FourCC('h0BQ'), 4, 4 }, { FourCC('h0BT'), 18, 4 },

        { FourCC('h0BU'), 3, 6 }, { FourCC('h0BV'), 10, 4 },

        { FourCC('h0BX'), 8, 6, gate = "tier2" }, { FourCC('wk01'), 8, 4 },

        { FourCC('h0BW'), 5, 2 },

    },

    gates = {

        tier2 = function(pi) return getAiCount(pi, FourCC('h0BR')) + getAiCount(pi, FourCC('h0BS')) >= 1 end,

    },

    production = {

        [FourCC('h0BV')] = {

            {FourCC('h0AA'), 3}, {FourCC('h0AD'), 3}, {FourCC('h0A5'), 2}, {FourCC('h0A6'), 2},

        },

        [FourCC('h0BX')] = {

            {FourCC('h0BP'), 3}, {FourCC('h0A9'), 2}, {FourCC('h0AC'), 2}, {FourCC('h0AE'), 2},

        },

        [FourCC('wk01')] = {

            {FourCC('wk08'), 3}, {FourCC('wk02'), 2}, {FourCC('wk00'), 2},

        },

        [FourCC('h0BU')] = {

            {FourCC('H0C6'), 1, limit = 1}, {FourCC('H0C5'), 1, limit = 1}, {FourCC('H0C7'), 1, limit = 1},

        },

        worker = { id = FourCC('h0C9'), cap = 18, from = { FourCC('h0BQ'), FourCC('h0BR'), FourCC('h0BS') } },
},

    ecoWeights = {

        [FourCC('h0BT')] = 1, [FourCC('h0BQ')] = 2,

        [FourCC('h0BR')] = 5, [FourCC('h0BS')] = 8,

    },

    strategData = {

        gradeCap = 100,

        steps = {

            -- Real Vrykul grades from the Lumber Mill (h0BW): iron weapon/armor +
            -- marksmanship + studded armor + axes + sword/defense mastery.
            { at = 17, action = "research", rows = {
                {FourCC('h0BW'),FourCC('R069'),6},  -- iron swords
                {FourCC('h0BW'),FourCC('R06A'),6},  -- iron armor
                {FourCC('h0BW'),FourCC('R06B'),6},  -- marksmanship
                {FourCC('h0BW'),FourCC('R06C'),6},  -- studded leather armor
                {FourCC('h0BW'),FourCC('R06D'),6},  -- improved axes
                {FourCC('h0BW'),FourCC('R06E'),6},  -- sword mastery
                {FourCC('h0BW'),FourCC('R06F'),6},  -- defense mastery
            }},

            { at = 20, action = "tryBuy" },

            { at = 45, action = "fleet", wall = FourCC('h0D1') },

            { at = 25, action = "techUp", from = FourCC('h0BQ'), to = FourCC('h0BR'), cap = 3 },

            { at = 55, action = "techUp", from = FourCC('h0BR'), to = FourCC('h0BS'), cap = 3 },

        },

    },

    attackerData = {

        [FourCC('h0AA')] = {

            { order = "berserk",    chance = 4, type = "immediate" },

            { order = "roar",       chance = 4, type = "immediate" },

        },

        [FourCC('h0AD')] = {

            { order = "thunderclap", chance = 4, type = "immediate" },

        },

        [FourCC('h0BP')] = {

            { order = "flamestrike",      chance = 4, type = "point" },

            { order = "breathoffire",     chance = 4, type = "point" },

        },

        [FourCC('h0A9')] = {

            { order = "stomp",       chance = 4, type = "immediate" },

        },

        [FourCC('wk08')] = {

            { order = "bloodlust",   chance = 4, type = "target" },

            { order = "lightningshield", chance = 4, type = "target" },

        },

    },

    getLvlData = {

        [FourCC('H0C6')] = { skills = { FourCC('A0ET'), FourCC('A0ES'), FourCC('A0EQ'), FourCC('A0ER') } },

        [FourCC('H0C5')] = { skills = { FourCC('A0EN'), FourCC('A0EO'), FourCC('A0EM'), FourCC('A0EP') } },

        [FourCC('H0C7')] = { skills = { FourCC('A0EU'), FourCC('A0EV'), FourCC('A0EW'), FourCC('A0EX') } },

    },

    wall = FourCC('h0D1'),

    naval = aiNavalTrain_Common,

    join = Join_Vrykul,


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
        [FourCC('h0C9')] = 0.2368,
        [FourCC('h0AA')] = 0.0789,
        [FourCC('h0AD')] = 0.0789,
        [FourCC('h0BP')] = 0.0789,
        [FourCC('wk08')] = 0.0789,
        [FourCC('h0A5')] = 0.0526,
        [FourCC('h0A6')] = 0.0526,
        [FourCC('h0A9')] = 0.0526,
        [FourCC('h0AC')] = 0.0526,
        [FourCC('h0AE')] = 0.0526,
        [FourCC('wk02')] = 0.0526,
        [FourCC('wk00')] = 0.0526,
        [FourCC('H0C6')] = 0.0263,
        [FourCC('H0C5')] = 0.0263,
        [FourCC('H0C7')] = 0.0263,
    },
})



---@param id integer

---@param pi integer

---@param u unit
