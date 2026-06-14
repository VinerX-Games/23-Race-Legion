function Join_Forsaken(id, pi, u)

    if id == FourCC('h0J5') then

        GroupAddUnit(udg_Ai_builders[pi], u)

    elseif aiUnitJoinsCapitalGuard(u, pi) then

    else

        aiUnitJoinsArmy(u, pi)

    end

end



RegisterAiRace("Forsaken", {

    tokens = {"forsaken", "fors", "ud"},

    weight = 1,

    altar = FourCC('h0JR'),

    start = startForsaken,

    buildings = {

        seed = FourCC('h0JD'),

        { FourCC('h0JP'), 4, 4 }, { FourCC('h0JD'), 18, 4 },

        { FourCC('h0JJ'), 10, 4 }, { FourCC('h0JO'), 5, 2 },

        { FourCC('h0JR'), 3, 6 }, { FourCC('h0JM'), 25, 1 },

        { FourCC('h0JI'), 4, 2, gate = "tier2" },

        { FourCC('h0JK'), 8, 6, gate = "tier2" },

    },

    gates = {

        tier2 = function(pi)

            return getAiCount(pi, FourCC('h0JQ')) + getAiCount(pi, FourCC('h0JL')) >= 1

        end,

    },

    production = {

        [FourCC('h0JJ')] = {

            {FourCC('n04T'), 4}, {FourCC('h0JC'), 4},

            {FourCC('h0JN'), 3, gate = "tier2"}, {FourCC('n04U'), 2, gate = "tier2"},

        },

        [FourCC('h0JK')] = {

            {FourCC('n04Y'), 3}, {FourCC('n04X'), 3},

            {FourCC('n04V'), 2, gate = "tier2"}, {FourCC('h0JA'), 1, gate = "tier2"},

        },

        [FourCC('h0JI')] = {

            {FourCC('o02X'), 3}, {FourCC('u02C'), 2, gate = "tier2"}, {FourCC('o02Y'), 2, gate = "tier2"},

        },

        [FourCC('h0JR')] = {

            {FourCC('N058'), 1, limit = 1}, {FourCC('O031'), 1, limit = 1}, {FourCC('O030'), 1, limit = 1},

        },

        worker = { id = FourCC('h0J5'), cap = 22, from = { FourCC('h0JP'), FourCC('h0JQ'), FourCC('h0JL') } },
},

    ecoWeights = {

        [FourCC('h0JD')] = 1, [FourCC('h0JP')] = 2,

        [FourCC('h0JQ')] = 5, [FourCC('h0JL')] = 8,

    },

    strategData = {

        gradeCap = 100,

        steps = {

            -- Forge (h0JO) weapon/armor grades — the real 6/6 upgrades. The old
            -- entries issued abilities (Arlm=Return Lumber, Abds=Blight Dispel),
            -- which never fire RESEARCH_FINISH so Grades[pi] stayed 0.
            { at = 17, action = "research", rows = {
                { FourCC('h0JO'), FourCC('R0FJ'), 6 },  -- Iron Swords (weapon)
                { FourCC('h0JO'), FourCC('R0FK'), 6 },  -- Iron Armor
                { FourCC('h0JO'), FourCC('R0FL'), 6 },  -- Iron Projectiles
                { FourCC('h0JO'), FourCC('R0FM'), 6 },  -- Light Armor
                { FourCC('h0JO'), FourCC('R0FI'), 6 },  -- Improved Tools
            }},

            -- Unit/spell upgrades from death workshop + laboratory (real R-upgrades)
            { at = 30, action = "research", rows = {
                { FourCC('h0JK'), FourCC('R0FN'), 1 },  -- Banshee initiation
                { FourCC('h0JK'), FourCC('R0FO'), 1 },  -- Mage training
                { FourCC('h0JK'), FourCC('R0FZ'), 1 },  -- Val'kyr empowerment
                { FourCC('h0JK'), FourCC('R0G0'), 1 },  -- Assassin training
                { FourCC('h0JI'), FourCC('R0FB'), 1 },  -- Enhance lethality
            }},

            { at = 20, action = "tryBuy" },

            { at = 25, action = "techUp", from = FourCC('h0JP'), to = FourCC('h0JQ'), cap = 3 },

            { at = 55, action = "techUp", from = FourCC('h0JQ'), to = FourCC('h0JL'), cap = 3 },

        },

    },

    attackerData = {

        [FourCC('n04T')] = {

            { order = "cannibalize", chance = 4, type = "immediate", hp = 50 },

        },

        [FourCC('h0JN')] = {

            { order = "shadowstrike", chance = 4, type = "target", notStructure = true },

        },

        [FourCC('n04U')] = {

            { order = "cannibalize", chance = 4, type = "immediate", hp = 50 },

            { order = "defend", chance = 3, type = "immediate" },

        },

        [FourCC('n04Y')] = {

            { order = "curse", chance = 5, type = "target" },

            { order = "faeriefire", chance = 6, type = "target" },

        },

        [FourCC('n04X')] = {

            { order = "carrionswarm", chance = 4, type = "point" },

            { order = "rainoffire", chance = 4, type = "point" },

            { order = "cannibalize", chance = 5, type = "immediate", hp = 50 },

        },

        [FourCC('n04V')] = {

            { order = "windwalk", chance = 4, type = "immediate" },

            { order = "cannibalize", chance = 4, type = "immediate", hp = 50 },

        },

        [FourCC('h0JA')] = {

            { order = "animatedead", chance = 4, type = "point" },

            { order = "raisedead", chance = 4, type = "point" },

            { order = "resurrection", chance = 5, type = "immediate" },

        },

        [FourCC('o02X')] = {

            { order = "channel", chance = 4, type = "self" },

        },

        [FourCC('u02C')] = {

            { order = "cannibalize", chance = 4, type = "immediate", hp = 50 },

        },

    },

    join = Join_Forsaken,

    wall = FourCC('h0JM'),

    shipyard = FourCC('h0D1'),  -- Undead Верфь (wall is a defensive tower)


    diplomat = "traitor",

    brain = "objective",

    brainWeights = {
        kind  = { capital = 100, cluster = 40, capture = 60, weak = 20, front = 15 },
        value = 1.0, dist = 0.002, claim = 25.0, siege = 0.5,
        focusMargin = 30.0, homeThreat = 20.0, tpDist = 6000.0,
        rHome = 2500.0, rCluster = 1600.0,
        clusterEvery = 8, topK = 8,
    },
    compTarget = {
        [FourCC('h0J5')] = 0.2195,
        [FourCC('n04T')] = 0.0976,
        [FourCC('h0JC')] = 0.0976,
        [FourCC('h0JN')] = 0.0732,
        [FourCC('n04Y')] = 0.0732,
        [FourCC('n04X')] = 0.0732,
        [FourCC('o02X')] = 0.0732,
        [FourCC('n04U')] = 0.0488,
        [FourCC('n04V')] = 0.0488,
        [FourCC('u02C')] = 0.0488,
        [FourCC('o02Y')] = 0.0488,
        [FourCC('h0JA')] = 0.0244,
        [FourCC('N058')] = 0.0244,
        [FourCC('O031')] = 0.0244,
        [FourCC('O030')] = 0.0244,
    },
})



---@param id integer

---@param pi integer

---@param u unit
