function Join_Gnomes(id, pi, u)

    if id == FourCC('h0FA') then

        GroupAddUnit(udg_Ai_builders[pi], u)

    elseif aiUnitJoinsCapitalGuard(u, pi) then

    else

        aiUnitJoinsArmy(u, pi)

    end

end



RegisterAiRace("Gnomes", {

    tokens = {"gnome", "gnomes"},

    weight = 1,

    altar = FourCC('h0G7'),

    start = startGnomes,

    buildings = {

        seed = FourCC('h0FI'),

        { FourCC('h0FK'), 4, 4 }, { FourCC('h0FI'), 18, 4 },

        { FourCC('h0FL'), 8, 4 }, { FourCC('h0G7'), 3, 6 },

        { FourCC('h0G3'), 10, 4 }, { FourCC('h0FY'), 8, 4 },

        { FourCC('h0G0'), 8, 6, gate = "tier2" }, { FourCC('h0FZ'), 4, 2 },

    },

    gates = {

        tier2 = function(pi) return getAiCount(pi, FourCC('h0FR')) + getAiCount(pi, FourCC('h0FS')) >= 1 end,

    },

    production = {

        [FourCC('h0G3')] = {

            {FourCC('h0FC'), 3}, {FourCC('h0FB'), 2}, {FourCC('h0FD'), 2},

            {FourCC('h0FE'), 2}, {FourCC('h0FU'), 2}, {FourCC('h0FM'), 2},

        },

        [FourCC('h0FY')] = {

            {FourCC('h0FP'), 3}, {FourCC('h0G1'), 3}, {FourCC('h0FX'), 2},

            {FourCC('h0G4'), 2}, {FourCC('h0G5'), 2}, {FourCC('h0FH'), 2},

            {FourCC('h0G2'), 2}, {FourCC('h0FW'), 2}, {FourCC('h0FV'), 2},

        },

        [FourCC('h0G0')] = {

            {FourCC('h0FQ'), 3}, {FourCC('h0FN'), 2}, {FourCC('h0FO'), 2},

            {FourCC('h0FJ'), 2}, {FourCC('h0FF'), 2}, {FourCC('h0FG'), 2}, {FourCC('h0FT'), 2},

        },

        [FourCC('h0G7')] = {

            {FourCC('H0GG'), 1, limit = 1}, {FourCC('H0GE'), 1, limit = 1}, {FourCC('H0GC'), 1, limit = 1},

        },

        worker = { id = FourCC('h0FA'), cap = 18, from = { FourCC('h0FK'), FourCC('h0FR'), FourCC('h0FS') } },
},

    ecoWeights = {

        [FourCC('h0FI')] = 1, [FourCC('h0FK')] = 2,

        [FourCC('h0FR')] = 5, [FourCC('h0FS')] = 8,

        [FourCC('h0FL')] = 1, [FourCC('h0G7')] = 3,

        [FourCC('h0G3')] = 2, [FourCC('h0FY')] = 2,

        [FourCC('h0G0')] = 4, [FourCC('h0FZ')] = 4,

    },

    strategData = {

        gradeCap = 100,

        steps = {

            -- Core 6-level weapon/armor grades live on the MAIN HALL line (h0FK/h0FR/h0FS
            -- all research R0CT/R0CU). The old config never researched these and hosted
            -- every other grade on h0FY/h0G0, which do NOT carry those upgrades (the
            -- R0B*/R0C* specials are all on the armory h0FZ) — so every order silently
            -- failed and Gnomes sat at grd~0. Each upgrade is now hosted on the building
            -- that actually carries it (verified via object `researches`). When the hall is
            -- teched up past h0FK the MakeGrade fallback grants R0CT/R0CU directly.
            { at = 12, action = "research", rows = {
                {FourCC('h0FK'), FourCC('R0CT'), 6}, {FourCC('h0FK'), FourCC('R0CU'), 6},
            }},

            { at = 30, action = "research", rows = {
                {FourCC('h0FY'), FourCC('R0CX'), 6}, {FourCC('h0G0'), FourCC('R0CW'), 6},
                {FourCC('h0G3'), FourCC('R0CV'), 6},
            }},

            -- Special single-level unlocks — all on the armory h0FZ (were wrongly h0FY/h0G0).
            { at = 25, action = "random", branches = {
                { {FourCC('h0FZ'), FourCC('R0B7'), 1} },
                { {FourCC('h0FZ'), FourCC('R0B8'), 1} },
                { {FourCC('h0FZ'), FourCC('R0BJ'), 1} },
                { {FourCC('h0FZ'), FourCC('R0BA'), 1} },
            }},

            { at = 45, action = "random", branches = {
                { {FourCC('h0FZ'), FourCC('R0BB'), 1}, {FourCC('h0FZ'), FourCC('R0BC'), 1} },
                { {FourCC('h0FZ'), FourCC('R0BE'), 1}, {FourCC('h0FZ'), FourCC('R0BD'), 1} },
                { {FourCC('h0FZ'), FourCC('R0BF'), 1}, {FourCC('h0FZ'), FourCC('R0BG'), 1} },
            }},

            { at = 20, action = "tryBuy" },

            { at = 25, action = "techUp", from = FourCC('h0FK'), to = FourCC('h0FR'), cap = 3 },

            { at = 55, action = "techUp", from = FourCC('h0FR'), to = FourCC('h0FS'), cap = 3 },

        },

    },

    attackerData = {

        [FourCC('h0FC')] = {

            { order = "clusterrockets", chance = 4, type = "point" },

        },

        [FourCC('h0FB')] = {

            { order = "thunderclap", chance = 4, type = "immediate" },

        },

        [FourCC('h0FP')] = {

            { order = "silence",     chance = 4, type = "point" },

            { order = "flamestrike", chance = 4, type = "point" },

        },

        [FourCC('h0FQ')] = {

            { order = "thunderbolt",  chance = 4, type = "target" },

            { order = "chainlightning", chance = 4, type = "target" },

        },

        [FourCC('h0FN')] = {

            { order = "healingspray", chance = 4, type = "self" },

            { order = "acidbomb",     chance = 4, type = "target" },

        },

    },

    getLvlData = {

        [FourCC('H0GG')] = { skills = { FourCC('A0TK'), FourCC('A0TJ'), FourCC('A0D5'), FourCC('A0GW') } },

        [FourCC('H0GE')] = { skills = { FourCC('A0TH'), FourCC('A0TG'), FourCC('A0TF'), FourCC('A0TE') } },

        [FourCC('H0GC')] = { skills = { FourCC('A0TD'), FourCC('ANab'), FourCC('A0TC'), FourCC('AHfs') } },

    },

    join = Join_Gnomes,

    wall = FourCC('h0FZ'),

    shipyard = FourCC('h011'),  -- human worker (hpea) -> human Верфь


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
        [FourCC('h0FA')] = 0.1500,
        [FourCC('h0FC')] = 0.0500,
        [FourCC('h0FP')] = 0.0500,
        [FourCC('h0G1')] = 0.0500,
        [FourCC('h0FQ')] = 0.0500,
        [FourCC('h0FB')] = 0.0333,
        [FourCC('h0FD')] = 0.0333,
        [FourCC('h0FE')] = 0.0333,
        [FourCC('h0FU')] = 0.0333,
        [FourCC('h0FM')] = 0.0333,
        [FourCC('h0FX')] = 0.0333,
        [FourCC('h0G4')] = 0.0333,
        [FourCC('h0G5')] = 0.0333,
        [FourCC('h0FH')] = 0.0333,
        [FourCC('h0G2')] = 0.0333,
        [FourCC('h0FW')] = 0.0333,
        [FourCC('h0FV')] = 0.0333,
        [FourCC('h0FN')] = 0.0333,
        [FourCC('h0FO')] = 0.0333,
        [FourCC('h0FJ')] = 0.0333,
        [FourCC('h0FF')] = 0.0333,
        [FourCC('h0FG')] = 0.0333,
        [FourCC('h0FT')] = 0.0333,
        [FourCC('H0GG')] = 0.0167,
        [FourCC('H0GE')] = 0.0167,
        [FourCC('H0GC')] = 0.0167,
    },
})



---@param id integer

---@param pi integer

---@param u unit
