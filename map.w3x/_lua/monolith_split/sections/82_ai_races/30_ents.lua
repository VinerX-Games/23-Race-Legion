function Join_Ents(id, pi, u)

    if id == FourCC('e02T') then

        GroupAddUnit(udg_Ai_builders[pi], u)

    elseif aiUnitJoinsCapitalGuard(u, pi) then

    else

        aiUnitJoinsArmy(u, pi)

    end

end



RegisterAiRace("Ents", {

    tokens = {"ent", "ents", "treant"},

    weight = 1,

    altar = FourCC('e02G'),

    start = startEnts,

    chooseBuild = function(pi)

        -- Ents workers build trees that uproot; same as standard

        local realBuilding = AiRunChooseBuildings(pi, AiRaces["Ents"])

        return realBuilding

    end,

    buildings = {

        -- seed is the base anchor + worker-training main hall. Was wrongly set to the
        -- Moon Well (e00N), which Ents can NEVER complete (0 ever built live — likely a
        -- missing prereq/placement req), so the brain sacrificed a wisp into a doomed
        -- Moon Well every tick and the base had no anchor. e02B (Древо Знаний) is the
        -- actual hall that trains the wisp worker. The dead e00N build row is dropped.
        seed = FourCC('e02B'),

        { FourCC('e02B'), 4, 4 },

        { FourCC('e02G'), 3, 6 }, { FourCC('e02F'), 10, 4 },

        { FourCC('e02H'), 8, 6, gate = "tier2" }, { FourCC('e02I'), 4, 2 },

    },

    gates = {

        tier2 = function(pi) return getAiCount(pi, FourCC('e02C')) + getAiCount(pi, FourCC('e02D')) >= 1 end,

    },

    production = {

        [FourCC('e02F')] = {

            {FourCC('e02J'), 3}, {FourCC('e02K'), 3}, {FourCC('e02L'), 2},

            {FourCC('e02O'), 2}, {FourCC('e03G'), 2},

        },

        [FourCC('e02H')] = {

            {FourCC('e02V'), 3}, {FourCC('e03A'), 2}, {FourCC('e02M'), 2}, {FourCC('e02N'), 2},

        },

        [FourCC('e02G')] = {

            {FourCC('E02S'), 1, limit = 1}, {FourCC('E02Q'), 1, limit = 1}, {FourCC('E02R'), 1, limit = 1},

        },

        worker = { id = FourCC('e02T'), cap = 18, from = { FourCC('e02B'), FourCC('e02C'), FourCC('e02D') } },
},

    ecoWeights = {

        [FourCC('e02B')] = 2,

        [FourCC('e02C')] = 5, [FourCC('e02D')] = 8,

    },

    strategData = {

        gradeCap = 100,

        steps = {

            -- Real Ents grades from the War Tree (e02F): poison sap, mana/life core
            -- empowerment, war mastery.
            { at = 17, action = "research", rows = {
                {FourCC('e02F'),FourCC('R09K'),6},  -- poison sap
                {FourCC('e02F'),FourCC('R0AH'),6},  -- war mastery
                {FourCC('e02F'),FourCC('R09N'),6},  -- mana core empowerment
                {FourCC('e02F'),FourCC('R0AF'),6},  -- life core empowerment
            }},

            { at = 20, action = "tryBuy" },

            { at = 25, action = "techUp", from = FourCC('e02B'), to = FourCC('e02C'), cap = 3 },

            { at = 55, action = "techUp", from = FourCC('e02C'), to = FourCC('e02D'), cap = 3 },

        },

    },

    attackerData = {

        [FourCC('e02J')] = {

            { order = "entanglingroots", chance = 4, type = "target" },

            { order = "forceofnature",   chance = 4, type = "target" },

        },

        [FourCC('e02K')] = {

            { order = "thornsaura",   chance = 4, type = "immediate" },

        },

        [FourCC('e02V')] = {

            { order = "tranquility",  chance = 5, type = "immediate", hp = 45 },

            { order = "cyclone",      chance = 5, type = "target", notStructure = true },

        },

        [FourCC('e03A')] = {

            { order = "roar",         chance = 4, type = "immediate" },

        },

        [FourCC('e02M')] = {

            { order = "faeriefire",   chance = 4, type = "target" },

            { order = "innerfire",    chance = 4, type = "target" },

        },

    },

    getLvlData = {

        [FourCC('E02S')] = { skills = { FourCC('A0PT'), FourCC('A0FW'), FourCC('A0PS'), FourCC('A0C9') } },

        [FourCC('E02Q')] = { skills = { FourCC('A0PI'), FourCC('A0PK'), FourCC('A0PJ'), FourCC('A0PL') } },

        [FourCC('E02R')] = { skills = { FourCC('A0PM'), FourCC('A0PN'), FourCC('A0V3'), FourCC('A0PP') } },

    },

    join = Join_Ents,

    wall = FourCC('e02I'),

    shipyard = FourCC('h0D8'),  -- night-elf worker (ewsp) -> night-elf Верфь


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
        [FourCC('e02T')] = 0.2727,
        [FourCC('e02J')] = 0.0909,
        [FourCC('e02K')] = 0.0909,
        [FourCC('e02V')] = 0.0909,
        [FourCC('e02L')] = 0.0606,
        [FourCC('e02O')] = 0.0606,
        [FourCC('e03G')] = 0.0606,
        [FourCC('e03A')] = 0.0606,
        [FourCC('e02M')] = 0.0606,
        [FourCC('e02N')] = 0.0606,
        [FourCC('E02S')] = 0.0303,
        [FourCC('E02Q')] = 0.0303,
        [FourCC('E02R')] = 0.0303,
    },
})
