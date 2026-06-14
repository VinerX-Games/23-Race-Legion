function Join_Silitids(id, pi, u)

    if id == FourCC('e01G') then

        GroupAddUnit(udg_Ai_builders[pi], u)

    elseif aiUnitJoinsCapitalGuard(u, pi) then

    else

        aiUnitJoinsArmy(u, pi)

    end

end



RegisterAiRace("Silitids", {

    tokens = {"silitid", "silitids", "qiraji"},

    weight = 1,

    desiredArmy = 220,  -- swarm race: field a bigger army than the global default (120)

    altar = FourCC('h00C'),

    start = startSilitids,

    buildings = {

        seed = FourCC('e01J'),

        { FourCC('e01H'), 16, 8 }, { FourCC('h00C'), 3, 6 }, 

        { FourCC('o015'), 10, 4 }, { FourCC('e01J'), 18, 4 },

        { FourCC('e01L'), 5, 2 },

        { FourCC('e01K'), 7, 2 },

        { FourCC('e01M'), 7, 2, gate = "tier2" },

        { FourCC('e00B'), 4, 2 }, { FourCC('o017'), 4, 2 },

    },

    gates = {

        tier2 = function(pi) return getAiCount(pi, FourCC('e021')) + getAiCount(pi, FourCC('e020')) >= 1 end,

    },

    production = {

        -- Hive e01H is the economic ENGINE: each one runs the egg-spawner (e01I eggs ->
        -- drones + army). Listing it as a production key makes BrainBuild treat it as a
        -- PASS-1 priority building (built before defensive/eco rows) so the egg->drone->
        -- army supply ramps. Without this the hive sat in low-priority PASS 2 and the
        -- drone count stayed ~8-9 (build pool starved, few structures). e01R = Swarm
        -- Mother, the only thing a hive trains directly (kept low so it's not spammed).
        [FourCC('e01H')] = {

            {FourCC('e01R'), 1, limit = 2},

        },

        [FourCC('o015')] = {

            {FourCC('u020'), 3}, {FourCC('u022'), 3}, {FourCC('e01N'), 2},

        },

        [FourCC('e01I')] = {

            {FourCC('e01G'), 4}, {FourCC('e01Z'), 3}, {FourCC('e02W'), 3},

            {FourCC('e01V'), 2}, {FourCC('e01T'), 2}, {FourCC('e01U'), 2},

            {FourCC('e01Q'), 2}, {FourCC('e01S'), 2}, {FourCC('e01O'), 2},

            {FourCC('e01P'), 2},

        },

        [FourCC('h00C')] = {

            {FourCC('U025'), 1, limit = 1}, {FourCC('U024'), 1, limit = 1}, {FourCC('U023'), 1, limit = 1},

        },

        -- The real builder is e01G (Трутень / Drone, type=Peon, builds= all hives &
        -- structures), trained from the auto-spawned e01I eggs. The old config named
        -- e01R (Мать роя / Swarm Mother — a caster with no `builds`) as the worker, so
        -- BrainProduce trained casters as "workers" (they fell through to the army) and
        -- never maintained a drone workforce → no free builder → hives/economy stalled.
        worker = { id = FourCC('e01G'), cap = 18, from = { FourCC('e01I') } },
},

    ecoWeights = {

        [FourCC('e01J')] = 1, [FourCC('e01H')] = 2,

        [FourCC('e021')] = 5, [FourCC('e020')] = 8,

    },

    strategData = {

        gradeCap = 100,

        steps = {

            { at = 17, action = "random", branches = {

                { {FourCC('e01L'),FourCC('Abds'),6},{FourCC('e01L'),FourCC('Arlm'),6} },

                { {FourCC('o015'),FourCC('Abds'),6} },

                { {FourCC('e01I'),FourCC('Abds'),6} },

            }},

            { at = 20, action = "tryBuy" },

            { at = 25, action = "techUp", from = FourCC('e01H'), to = FourCC('e021'), cap = 3 },

            { at = 30, action = "research", rows = {
                {FourCC('e01K'), FourCC('R089'), 1},
                {FourCC('e01K'), FourCC('R08B'), 1},
            }},

            { at = 45, action = "research", rows = {
                {FourCC('e01M'), FourCC('R08C'), 1},
                {FourCC('e01M'), FourCC('R08E'), 1},
            }},

            { at = 55, action = "techUp", from = FourCC('e021'), to = FourCC('e020'), cap = 3 },

        },

    },

    attackerData = {

        [FourCC('e01T')] = {

            { order = "forkedlightning", chance = 4, type = "point" },

            { order = "parasiteon",      chance = 4, type = "immediate" },

            { order = "carrionswarm",    chance = 4, type = "point" },

        },

        [FourCC('e01U')] = {

            { order = "web", chance = 4, type = "target" },

        },

        [FourCC('u020')] = {

            { order = "replenishmana", chance = 4, type = "immediate" },

            { order = "replenishlife", chance = 4, type = "immediate" },

        },

        [FourCC('u022')] = {

            { order = "devourmagic", chance = 4, type = "target", range = 525 },

        },

        [FourCC('e01R')] = {
            -- A0ZU "Создать личинку" (Create Larva): Channel-based, order "channel", no target.
            { order = "channel",        chance = 4, type = "immediate" },
            -- A0KQ "Волна исцеления" (Healing Wave): heals a damaged ally in range.
            { order = "healingwave",    chance = 4, type = "heal", allyRange = 700 },
        },

        [FourCC('U025')] = {

            { order = "earthquake",  chance = 5, type = "immediate" },

            { order = "hex",         chance = 5, type = "target", notStructure = true },

        },

        [FourCC('U024')] = {

            { order = "locustswarm", chance = 5, type = "immediate" },

            { order = "impales",    chance = 5, type = "point" },

        },

        [FourCC('U023')] = {

            { order = "controlmagic",  chance = 4, type = "target" },

            { order = "impales",       chance = 5, type = "point" },

            { order = "carrionswarm",  chance = 5, type = "point" },

            { order = "deathpact",     chance = 5, type = "target" },

        },

    },

    getLvlData = {

        [FourCC('U025')] = { skills = { FourCC('AEtq'), FourCC('AUau'), FourCC('AOhx'), FourCC('A0ST') } },

        [FourCC('U024')] = { skills = { FourCC('AUls'), FourCC('AEah'), FourCC('AUts'), FourCC('A0SQ') } },

        [FourCC('U023')] = { skills = { FourCC('A0J2'), FourCC('A0SU'), FourCC('A0SV'), FourCC('A0J1') } },

    },

    join = Join_Silitids,

    shipyard = FourCC('h0D8'),  -- night-elf worker (ewsp) -> night-elf Верфь (no wall building)


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
        [FourCC('e01R')] = 0.2045,
        [FourCC('e01G')] = 0.0909,
        [FourCC('u020')] = 0.0682,
        [FourCC('u022')] = 0.0682,
        [FourCC('e01Z')] = 0.0682,
        [FourCC('e02W')] = 0.0682,
        [FourCC('e01N')] = 0.0455,
        [FourCC('e01V')] = 0.0455,
        [FourCC('e01T')] = 0.0455,
        [FourCC('e01U')] = 0.0455,
        [FourCC('e01Q')] = 0.0455,
        [FourCC('e01S')] = 0.0455,
        [FourCC('e01O')] = 0.0455,
        [FourCC('e01P')] = 0.0455,
        [FourCC('U025')] = 0.0227,
        [FourCC('U024')] = 0.0227,
        [FourCC('U023')] = 0.0227,
    },
})



---@param id integer

---@param pi integer

---@param u unit
