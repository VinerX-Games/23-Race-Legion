function Join_Demons(id, pi, u)

    if id == FourCC('e02Y') then

        GroupAddUnit(udg_Ai_builders[pi], u)

    elseif aiUnitJoinsCapitalGuard(u, pi) then

    else

        aiUnitJoinsArmy(u, pi)

    end

end



RegisterAiRace("Demons", {

    tokens = {"demon", "demons", "legion"},

    weight = 1,

    altar = FourCC('h0DX'),

    start = startDemons,

    buildings = {

        seed = FourCC('h0DS'),

        { FourCC('h0DU'), 4, 4 }, { FourCC('h0DS'), 18, 4 },

        { FourCC('h0DT'), 8, 4 }, { FourCC('h0DX'), 3, 6 },

        { FourCC('h0DY'), 10, 4 }, { FourCC('h0E1'), 8, 6, gate = "tier2" },

        { FourCC('h0E0'), 8, 6, gate = "tier2" },

        { FourCC('h0DZ'), 5, 2 }, { FourCC('n02C'), 4, 2 },

    },

    gates = {

        tier2 = function(pi) return getAiCount(pi, FourCC('h0DV')) + getAiCount(pi, FourCC('h0DW')) >= 1 end,

    },

    production = {

        [FourCC('h0DY')] = {

            {FourCC('n025'), 4}, {FourCC('n023'), 4}, {FourCC('n026'), 3},

            {FourCC('n027'), 3}, {FourCC('n02D'), 2}, {FourCC('n02E'), 2},

        },

        [FourCC('h0E1')] = {

            {FourCC('n024'), 3}, {FourCC('n022'), 2}, {FourCC('n021'), 2},

        },

        [FourCC('h0E0')] = {

            {FourCC('n020'), 3}, {FourCC('n028'), 2},

        },

        [FourCC('h0DX')] = {

            {FourCC('N02F'), 1, limit = 1}, {FourCC('N02A'), 1, limit = 1}, {FourCC('U028'), 1, limit = 1},

        },

        worker = { id = FourCC('e02Y'), cap = 20, from = { FourCC('h0DU'), FourCC('h0DV'), FourCC('h0DW') } },
},

    ecoWeights = {

        [FourCC('h0DS')] = 1, [FourCC('h0DU')] = 2,

        [FourCC('h0DV')] = 5, [FourCC('h0DW')] = 8,

    },

    strategData = {

        gradeCap = 100,

        steps = {
            { at = 17, action = "research", rows = {
                {FourCC('h0DZ'),FourCC('R08J'),6},  -- melee
                {FourCC('h0DZ'),FourCC('R08K'),6},  -- armor
                {FourCC('h0DZ'),FourCC('R08L'),6},  -- ranged
                {FourCC('h0DZ'),FourCC('R08M'),6},  -- armor
            }},


            { at = 17, action = "random", branches = {

                { {FourCC('h0DZ'),FourCC('Abds'),6},{FourCC('h0DZ'),FourCC('Arlm'),6} },

                { {FourCC('h0DY'),FourCC('Abds'),6} },

                { {FourCC('h0E0'),FourCC('Abds'),6},{FourCC('h0E1'),FourCC('Abds'),6} },

            }},

            { at = 20, action = "tryBuy" },

            { at = 25, action = "techUp", from = FourCC('h0DU'), to = FourCC('h0DV'), cap = 3 },

            { at = 55, action = "techUp", from = FourCC('h0DV'), to = FourCC('h0DW'), cap = 3 },

        },

    },

    attackerData = {

        [FourCC('n025')] = {

            { order = "carrionswarm", chance = 5, type = "point" },

        },

        [FourCC('n023')] = {

            { order = "firebolt",   chance = 5, type = "target" },

            { order = "thunderbolt", chance = 5, type = "target" },

        },

        [FourCC('n026')] = {

            { order = "frostnova", chance = 5, type = "target" },

        },

        [FourCC('n024')] = {

            { order = "banish",    chance = 4, type = "target" },

            { order = "sleep",     chance = 4, type = "target" },

        },

        [FourCC('n022')] = {

            { order = "flamestrike", chance = 4, type = "point" },

            { order = "rainoffire", chance = 4, type = "point" },

        },

        [FourCC('n020')] = {

            { order = "doom",       chance = 5, type = "target" },

            { order = "chainlightning", chance = 5, type = "target" },

        },

    },

    attackerData = {

        [FourCC('n025')] = {

            { order = "carrionswarm", chance = 5, type = "point" },

        },

        [FourCC('n023')] = {

            { order = "firebolt",   chance = 5, type = "target" },

            { order = "thunderbolt", chance = 5, type = "target" },

        },

        [FourCC('n026')] = {

            { order = "frostnova", chance = 5, type = "target" },

        },

        [FourCC('n024')] = {

            { order = "banish",    chance = 4, type = "target" },

            { order = "sleep",     chance = 4, type = "target" },

        },

        [FourCC('n022')] = {

            { order = "flamestrike", chance = 4, type = "point" },

            { order = "rainoffire", chance = 4, type = "point" },

        },

        [FourCC('n020')] = {

            { order = "doom",       chance = 5, type = "target" },

            { order = "chainlightning", chance = 5, type = "target" },

        },

    },

    getLvlData = {

        [FourCC('N02F')] = { skills = { FourCC('A0M8'), FourCC('A0MB'), FourCC('A0MC'), FourCC('A0M9') } },

        [FourCC('N02A')] = { skills = { FourCC('A0MF'), FourCC('A0MA'), FourCC('A0ME'), FourCC('A0MD') } },

        [FourCC('U028')] = { skills = { FourCC('A0MG'), FourCC('A0MO'), FourCC('A0MN'), FourCC('A0MP') } },

    },

    join = Join_Demons,

    wall = FourCC('n02C'),

    shipyard = FourCC('h0D8'),  -- night-elf worker (ewsp) -> night-elf Верфь


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
        [FourCC('e02Y')] = 0.2143,
        [FourCC('n025')] = 0.0952,
        [FourCC('n023')] = 0.0952,
        [FourCC('n026')] = 0.0714,
        [FourCC('n027')] = 0.0714,
        [FourCC('n024')] = 0.0714,
        [FourCC('n020')] = 0.0714,
        [FourCC('n02D')] = 0.0476,
        [FourCC('n02E')] = 0.0476,
        [FourCC('n022')] = 0.0476,
        [FourCC('n021')] = 0.0476,
        [FourCC('n028')] = 0.0476,
        [FourCC('N02F')] = 0.0238,
        [FourCC('N02A')] = 0.0238,
        [FourCC('U028')] = 0.0238,
    },
})



---@param id integer

---@param pi integer

---@param u unit
