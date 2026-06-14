function Join_Nerubs(id, pi, u)

    if id == FourCC('h0BE') then

        GroupAddUnit(udg_Ai_builders[pi], u)

    elseif id == FourCC('u019') then

        -- Cocoon built - upgrade to intended building

        local target = AiData[pi]["upgradeCocoon"]

        if target ~= nil and target ~= 0 then

            IssueImmediateOrderById(u, target)

            AiData[pi]["upgradeCocoon"] = nil

        end

    elseif aiUnitJoinsCapitalGuard(u, pi) then

    else

        aiUnitJoinsArmy(u, pi)

    end

end



RegisterAiRace("Nerubs", {

    tokens = {"nerub", "nerubs"},

    weight = 1,

    altar = FourCC('h0CU'),

    start = startNerubs,

    chooseBuild = function(pi)

        -- Nerubs workers can only build cocoons (u019), which then upgrade

        local realBuilding = AiRunChooseBuildings(pi, AiRaces["Nerubs"])

        if realBuilding ~= 0 then

            AiData[pi]["upgradeCocoon"] = realBuilding

            return FourCC('u019')

        end

        return 0

    end,

    buildings = {

        seed = FourCC('h0GH'),

        { FourCC('h0CO'), 4, 4 }, --{ FourCC('h0GH'), 18, 4 }, --Туннель нерубов

        { FourCC('h0CR'), 10, 4 }, { FourCC('h0CS'), 5, 2 },

        { FourCC('h0CU'), 3, 6 }, { FourCC('u01A'), 25, 1 },

        { FourCC('h0CT'), 8, 6, gate = "tier2" },

        { FourCC('h0CV'), 8, 6, gate = "tier2" },

    },

    gates = {

        tier2 = function(pi)

            return getAiCount(pi, FourCC('h0CP')) + getAiCount(pi, FourCC('h0CQ')) >= 1

        end,

    },

    production = {

        [FourCC('h0CR')] = {

            {FourCC('u01J'), 4}, {FourCC('u01G'), 4}, {FourCC('u01F'), 3},

        },

        [FourCC('h0CT')] = {

            {FourCC('u01C'), 3}, {FourCC('u01K'), 2, gate="tier2"},

            {FourCC('u01B'), 2, gate="tier2"}, {FourCC('u01I'), 3},

        },

        [FourCC('h0CV')] = {

            {FourCC('u01H'), 3}, {FourCC('u01D'), 3},

        },

        [FourCC('h0CU')] = {

            {FourCC('U01U'), 1, limit = 1}, {FourCC('U01V'), 1, limit = 1}, {FourCC('U01W'), 1, limit = 1},

        },

        worker = { id = FourCC('h0BE'), cap = 20, from = { FourCC('h0CO'), FourCC('h0CP'), FourCC('h0CQ') } },
},

    ecoWeights = {

        [FourCC('h0CO')] = 2,  -- main hall (was accidentally commented out with h0GH -> Nerubs eco stuck at 0)

        [FourCC('h0CP')] = 5, [FourCC('h0CQ')] = 8,

    },

    strategData = {

        gradeCap = 100,

        steps = {

            -- Real Nerub grades from the Vault (h0CS): forelimb (weapon) + torso/belly
            -- armor + blood/carapace/health/limb/nerub mutations + tools.
            { at = 17, action = "research", rows = {
                {FourCC('h0CS'),FourCC('R074'),6},  -- strong forelimbs (weapon)
                {FourCC('h0CS'),FourCC('R075'),6},  -- torso armor
                {FourCC('h0CS'),FourCC('R076'),6},  -- belly armor
                {FourCC('h0CS'),FourCC('R070'),6},  -- carapace mutation
                {FourCC('h0CS'),FourCC('R06Z'),6},  -- blood mutation
            }},

            { at = 20, action = "tryBuy" },

            { at = 45, action = "fleet", wall = FourCC('u01A') },

            { at = 25, action = "techUp", from = FourCC('h0CO'), to = FourCC('h0CP'), cap = 3 },

            { at = 55, action = "techUp", from = FourCC('h0CP'), to = FourCC('h0CQ'), cap = 3 },

        },

    },

    attackerData = {

        [FourCC('u01C')] = {

            { order = "parasite", chance = 4, type = "target" },

        },

        [FourCC('u01H')] = {

            { order = "heal", chance = 3, type = "heal", allyRange = 550 },

            { order = "dispel", chance = 3, type = "point" },

            { order = "lightningshield", chance = 3, type = "target" },

        },

        [FourCC('u01D')] = {

            { order = "thunderbolt", chance = 4, type = "target" },

            { order = "ward", chance = 4, type = "point" },

            { order = "entanglingroots", chance = 4, type = "target" },

        },

        [FourCC('u01E')] = {

            { order = "web", chance = 4, type = "target" },

            { order = "raisedead", chance = 5, type = "point" },

        },

    },

    join = Join_Nerubs,

    wall = FourCC('u01A'),

    shipyard = FourCC('h0D1'),  -- Undead Верфь (wall is Nerub Tower)

    naval = aiNavalTrain_Common,


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
        [FourCC('h0BE')] = 0.2308,
        [FourCC('u01J')] = 0.1026,
        [FourCC('u01G')] = 0.1026,
        [FourCC('u01F')] = 0.0769,
        [FourCC('u01C')] = 0.0769,
        [FourCC('u01I')] = 0.0769,
        [FourCC('u01H')] = 0.0769,
        [FourCC('u01D')] = 0.0769,
        [FourCC('u01K')] = 0.0513,
        [FourCC('u01B')] = 0.0513,
        [FourCC('U01U')] = 0.0256,
        [FourCC('U01V')] = 0.0256,
        [FourCC('U01W')] = 0.0256,
    },
})



---@param id integer

---@param pi integer

---@param u unit
