function Join_Cult(id, pi, u)
    if id == FourCC('cD02') then
        GroupAddUnit(udg_Ai_builders[pi], u)
    elseif aiUnitJoinsCapitalGuard(u, pi) then
    else
        aiUnitJoinsArmy(u, pi)
    end
end

RegisterAiRace("Cult", {
    tokens = {"cult", "damned", "cultofdamned", "cultofthedamned", "kp"},
    weight = 1,
    altar = FourCC('cD30'),
    start = startCult,
    buildings = {
        seed = FourCC('cD26'),
        { FourCC('cD26'), 4, 4 }, { FourCC('cD29'), 6, 4 },
        { FourCC('cD28'), 8, 4 }, { FourCC('cD27'), 6, 4 },
        { FourCC('cD30'), 2, 6 }, { FourCC('cD31'), 2, 6 },
        { FourCC('cD12'), 4, 4 },
    },
    production = {
        [FourCC('cD29')] = {
            {FourCC('cD03'), 3}, {FourCC('cD05'), 2}, {FourCC('cD08'), 2}, {FourCC('cD13'), 2},
        },
        [FourCC('cD28')] = {
            {FourCC('cD11'), 3}, {FourCC('cD10'), 2}, {FourCC('cD09'), 2}, {FourCC('cD14'), 2},
        },
        [FourCC('cD27')] = {
            {FourCC('cD19'), 2}, {FourCC('cD18'), 2}, {FourCC('cD22'), 2},
            {FourCC('cD33'), 1}, {FourCC('cD34'), 1}, {FourCC('cD35'), 1},
        },
        [FourCC('cD30')] = {
            -- Altar cD30 trains THREE heroes (CD01, U02X, CD02) — the config was missing
            -- the third (CD02, uppercase ≠ the worker cD02). All three now buildable so the
            -- Cult fields a full hero roster like every other race.
            {FourCC('CD01'), 1, limit = 1}, {FourCC('U02X'), 1, limit = 1}, {FourCC('CD02'), 1, limit = 1},
        },
        worker = { id = FourCC('cD02'), cap = 18, from = { FourCC('cD26') } },
    },
    ecoWeights = {
        [FourCC('cD26')] = 2, [FourCC('cD29')] = 4,
        [FourCC('cD28')] = 5, [FourCC('cD27')] = 6,
    },
    -- Signature mechanic — COLLAPSE a cluster of own small units into one bigger one. Two casters:
    --  MEAT: Defiler cD05, ability cDa5 "Плотеобработка", eats meat units (cDa6: cD09/cD10/cD14/
    --        cD11) -> cD10->cD09/cD14->cD00 by summed HP.
    --  BONE: Necromancer cD03, ability cDar "Костесборка", eats skeletons (cDat: cD18/19/22/33/34/35).
    -- Both abilities are Channel-based (order "channel"); each caster's other abilities are NOT
    -- channel, so the order is unambiguous. BrainMergeTick fires them occasionally on a cluster.
    mergeCast = {
        { ability = FourCC('cDa5'), caster = FourCC('cD05'), order = "channel",
          consumeAbil = FourCC('cDa6'), range = 700.0, minCluster = 5, chance = 12 },
        { ability = FourCC('cDar'), caster = FourCC('cD03'), order = "channel",
          consumeAbil = FourCC('cDat'), range = 700.0, minCluster = 5, chance = 12 },
    },

    attackerData = {
        [FourCC('CD01')] = {
            { order = "deathcoil", needAbil = FourCC('A0CO'), chance = 2, notStructure = true },
            { order = "roar", needAbil = FourCC('A0CP'), type = "immediate", chance = 2 },
            { order = "fanofknives", needAbil = FourCC('A0CQ'), type = "immediate", range = 400, chance = 2 },
        },
        [FourCC('U02X')] = {
            { order = "frostnova", needAbil = FourCC('AUfn'), chance = 2, notStructure = true },
            -- Channel uses DataF=acidbomb; editor Order=blackarrowon is not its cast order.
            { order = "acidbomb", needAbil = FourCC('A1HE'), type = "point", range = 750, chance = 2 },
            { order = "deathanddecay", needAbil = FourCC('AUdd'), type = "point", chance = 3 },
        },
        [FourCC('CD02')] = {
            -- Firelord summon is 852667 in the engine; OrderId("slimemonster") returns 0.
            { orderId = 852667, needAbil = FourCC('A0CL'), type = "immediate", chance = 2 },
            { order = "raisedead", needAbil = FourCC('A1IL'), type = "immediate", chance = 2 },
            { order = "animatedead", needAbil = FourCC('A0CN'), type = "immediate", chance = 3 },
        },
    },
    getLvlData = {
        [FourCC('CD01')] = { ult = FourCC('A0CQ'), skills = { FourCC('A0CO'), FourCC('A0CP'), FourCC('A0CR') } },
        [FourCC('U02X')] = { ult = FourCC('AUdd'), skills = { FourCC('AUfn'), FourCC('A1HE'), FourCC('AUdr') } },
        [FourCC('CD02')] = { ult = FourCC('A0CN'), skills = { FourCC('A1IL'), FourCC('A0CL'), FourCC('A0CM') } },
    },

    strategData = {
        gradeCap = 100,
        steps = {
            -- Cult grades from the Graveyard (cD31) — real research upgrades.
            { at = 17, action = "research", rows = {
                {FourCC('cD31'), FourCC('cDr0'), 6},
                {FourCC('cD31'), FourCC('cDr1'), 6},
                {FourCC('cD31'), FourCC('cDr3'), 6},
                {FourCC('cD31'), FourCC('cDr4'), 6},
                {FourCC('cD31'), FourCC('cDR4'), 6},
                {FourCC('cD31'), FourCC('cDR9'), 6},
            }},
            { at = 20, action = "tryBuy" },
        },
    },
    shipyard = FourCC('h0D1'),  -- shared Undead Верфь (cult worker builds h0D1; everything else is its own)
    join = Join_Cult,
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
        [FourCC('cD02')] = 0.25,
        [FourCC('cD03')] = 0.10, [FourCC('cD05')] = 0.08, [FourCC('cD08')] = 0.08, [FourCC('cD13')] = 0.08,
        [FourCC('cD11')] = 0.08, [FourCC('cD10')] = 0.06, [FourCC('cD09')] = 0.06, [FourCC('cD14')] = 0.06,
        [FourCC('cD19')] = 0.05, [FourCC('cD18')] = 0.05, [FourCC('cD22')] = 0.05,
        [FourCC('CD01')] = 0.03, [FourCC('U02X')] = 0.03, [FourCC('CD02')] = 0.03,
    },
})



---@param id integer

---@param pi integer

---@param u unit
