function Join_Draenei(id, pi, u)

    if id == FourCC('h012') then

        GroupAddUnit(udg_Ai_builders[pi], u)

    elseif aiUnitJoinsCapitalGuard(u, pi) then

    else

        aiUnitJoinsArmy(u, pi)

    end

end



RegisterAiRace("Draenei", {

    tokens = {"draenei", "draeneis"},

    weight = 1,

    altar = FourCC('h057'),

    start = startDraenei,

    buildings = {

        seed = FourCC('h05C'),

        { FourCC('h015'), 4, 4 }, { FourCC('h05C'), 18, 4 },

        { FourCC('h057'), 3, 6 }, { FourCC('h033'), 10, 4 },

        { FourCC('h058'), 8, 6, gate = "tier2" }, { FourCC('h056'), 8, 6, gate = "tier2" },

        { FourCC('h055'), 5, 2 }, { FourCC('h05A'), 8, 4 },

    },

    gates = {

        tier2 = function(pi) return getAiCount(pi, FourCC('h016')) + getAiCount(pi, FourCC('h017')) >= 1 end,

    },

    production = {

        [FourCC('h033')] = {

            {FourCC('h01S'), 3}, {FourCC('h01P'), 3}, {FourCC('e000'), 4},

        },

        [FourCC('h058')] = {

            {FourCC('h01O'), 2}, {FourCC('h01R'), 3}, {FourCC('h059'), 3}, {FourCC('h01T'), 2},

        },

        [FourCC('h056')] = {

            {FourCC('h01U'), 3}, {FourCC('h01Q'), 3},

        },

        [FourCC('h05A')] = {

            {FourCC('n005'), 4}, {FourCC('h05E'), 2}, {FourCC('h05D'), 2},

        },

        [FourCC('h057')] = {

            {FourCC('H05K'), 1, limit = 1}, {FourCC('H05L'), 1, limit = 1}, {FourCC('H05M'), 1, limit = 1},

        },

        worker = { id = FourCC('h012'), cap = 18, from = { FourCC('h015'), FourCC('h016'), FourCC('h017') } },
},

    ecoWeights = {

        [FourCC('h05C')] = 1, [FourCC('h015')] = 2,

        [FourCC('h016')] = 5, [FourCC('h017')] = 8,

    },

    strategData = {

        gradeCap = 100,

        steps = {
            { at = 17, action = "research", rows = {
                {FourCC('h055'),FourCC('R023'),6},  -- melee
                {FourCC('h055'),FourCC('R024'),6},  -- armor
                {FourCC('h055'),FourCC('R02P'),6},  -- melee
            }},


            { at = 17, action = "random", branches = {

                { {FourCC('h055'),FourCC('Abds'),6},{FourCC('h055'),FourCC('Arlm'),6} },

                { {FourCC('h033'),FourCC('Abds'),6} },

                { {FourCC('h056'),FourCC('Abds'),6},{FourCC('h058'),FourCC('Abds'),6} },

            }},

            { at = 20, action = "tryBuy" },

            { at = 25, action = "techUp", from = FourCC('h015'), to = FourCC('h016'), cap = 3 },

            { at = 55, action = "techUp", from = FourCC('h016'), to = FourCC('h017'), cap = 3 },

        },

    },

    attackerData = {

        [FourCC('h01S')] = {

            { order = "defend",   chance = 5, type = "immediate" },

            { order = "berserk",   chance = 5, type = "immediate" },

        },

        [FourCC('H05K')] = {

            { order = "healingwave",  chance = 5, type = "heal", allyRange = 550 },

        },

    },

    attackedData = {

        [FourCC('h01S')] = {

            { order = "defend",   chance = 3, type = "immediate" },

            { order = "undefend", chance = 3, type = "immediate" },

        },

    },

    getLvlData = {

        [FourCC('H05K')] = { skills = { FourCC('AOhw'), FourCC('A06C'), FourCC('A068'), FourCC('A069') } },

    },

    join = Join_Draenei,

    shipyard = FourCC('h011'),  -- human worker (hpea) -> human Верфь (no wall building)


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
        [FourCC('h012')] = 0.1957,
        [FourCC('e000')] = 0.0870,
        [FourCC('n005')] = 0.0870,
        [FourCC('h01S')] = 0.0652,
        [FourCC('h01P')] = 0.0652,
        [FourCC('h01R')] = 0.0652,
        [FourCC('h059')] = 0.0652,
        [FourCC('h01U')] = 0.0652,
        [FourCC('h01Q')] = 0.0652,
        [FourCC('h01O')] = 0.0435,
        [FourCC('h01T')] = 0.0435,
        [FourCC('h05E')] = 0.0435,
        [FourCC('h05D')] = 0.0435,
        [FourCC('H05K')] = 0.0217,
        [FourCC('H05L')] = 0.0217,
        [FourCC('H05M')] = 0.0217,
    },
})



---@param id integer

---@param pi integer

---@param u unit
