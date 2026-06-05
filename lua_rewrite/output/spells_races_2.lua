-- ============================================================
-- 23 Race Legion - Lua Rewrite
-- output/spells_races_2.lua — Silitids, Demons, Undead, IceTrolls,
--   Forsaken, Elementals, JungleTrolls, PvE spells
-- ============================================================

local function InitSpellTrig(events, cond, action)
    local t = CreateTrigger()
    if type(events) == "string" then
        TriggerRegisterAnyUnitEventBJ(t, events)
    else
        for _, ev in ipairs(events) do
            TriggerRegisterAnyUnitEventBJ(t, ev)
        end
    end
    if cond then TriggerAddCondition(t, Condition(cond)) end
    TriggerAddAction(t, action)
    return t
end

-- ============================================================
-- SILITIDS: Start + Uley system
-- ============================================================

function SilitidsOn()
    -- Enables all Silitid triggers (done during race init)
end

function StartSilitidsEach()
    for i = 0, 23 do
        local p = Player(i)
        -- Disable specific abilities
        SetPlayerAbilityAvailable(p, FourCC('A0KM'), false)
        SetPlayerAbilityAvailable(p, FourCC('A0KN'), false)
        SetPlayerAbilityAvailable(p, FourCC('A0IZ'), false)
        SetPlayerAbilityAvailable(p, FourCC('A1KF'), false)
        SetPlayerAbilityAvailable(p, FourCC('A0KL'), false)
        SetPlayerAbilityAvailable(p, FourCC('A1KD'), false)
        SetPlayerAbilityAvailable(p, FourCC('A1B7'), false)
        -- Hero caps
        SetPlayerTechMaxAllowed(p, FourCC('U024'), 1)
        SetPlayerTechMaxAllowed(p, FourCC('U025'), 1)
        SetPlayerTechMaxAllowed(p, FourCC('U023'), 1)
        SetPlayerTechMaxAllowed(p, FourCC('U02R'), 1)
        SetPlayerTechMaxAllowed(p, FourCC('R088'), 5)
        -- Block tank
        SetPlayerTechMaxAllowed(p, FourCC('e01P'), 0)
    end
end

-- QTunServe: transfer Ankirag neutrals to player
function QTunServe_Action()
    local u = GetTriggerUnit()
    local p = GetOwningPlayer(u)
    -- transfer Ankirag units, remove capital ability, replace stolica
    TriggerExecute(G.gg_trg_QTunDie)
end

-- MainSpawn2: Larvae spawner at Hive
G.SilitidHiveData = {} -- { [hiveHandle] = { count = int, timer = timer } }

function MainSpawn2_Action()
    local hive = GetConstructedStructure()
    local hiveId = GetUnitTypeId(hive)
    local maxCount = 1
    if hiveId == FourCC('e02I') or hiveId == FourCC('e020') then maxCount = 2
    elseif hiveId == FourCC('e01H') then maxCount = 1 end

    local t = CreateTimer()
    local id = tostring(GetHandleId(hive))
    G.SilitidHiveData[id] = { count = 0, max = maxCount, timer = t, unit = hive }
    TimerStart(t, 25.0, true, function()
        local d = G.SilitidHiveData[id]
        if d and d.count < d.max and GetUnitState(d.unit, UNIT_STATE_LIFE) > 0 then
            local lich = CreateUnit(GetOwningPlayer(d.unit), FourCC('e01I'), GetUnitX(d.unit), GetUnitY(d.unit), 0)
            d.count = d.count + 1
        end
    end)
end

-- ============================================================
-- DEMONS/LEGION: Elemental path selection
-- ============================================================

function DemonPickElement(p, elemId, enableUnits, disableUnits)
    local els = { FourCC('A0W9'), FourCC('A0W7'), FourCC('A0W8'), FourCC('A0WA') }
    for _, id in ipairs(els) do
        if id ~= elemId then
            SetPlayerAbilityAvailable(p, id, false)
        end
    end
    for _, uid in ipairs(disableUnits) do
        SetPlayerTechMaxAllowed(p, uid, 0)
    end
    for _, uid in ipairs(enableUnits) do
        SetPlayerTechMaxAllowed(p, uid, -1)
    end
end

function DemonPickFire()
    local p = GetOwningPlayer(GetTriggerUnit())
    DemonPickElement(p, FourCC('A0W9'),
        { FourCC('h0F1'), FourCC('n07O'), FourCC('n034'), FourCC('n07Y') },
        { FourCC('n07N'), FourCC('n032'), FourCC('n07T'), FourCC('n035'), FourCC('n031'), FourCC('n07X'),
          FourCC('n02Z'), FourCC('n033'), FourCC('n02Y'), FourCC('n07S'), FourCC('n07W'),
          FourCC('n07R'), FourCC('n02P'), FourCC('n07Q'), FourCC('n07Z') })
    SetPlayerTechMaxAllowed(p, FourCC('n02R'), 0)
    SetPlayerTechMaxAllowed(p, FourCC('n02X'), 0)
end

function DemonPickWater()
    local p = GetOwningPlayer(GetTriggerUnit())
    DemonPickElement(p, FourCC('A0W7'),
        { FourCC('n032'), FourCC('n07T'), FourCC('n035'), FourCC('n07X') },
        { FourCC('n031'), FourCC('n07Y'), FourCC('n02Z'), FourCC('n033'), FourCC('n02Y'),
          FourCC('n07S'), FourCC('n07W'), FourCC('n07R'), FourCC('n02P'), FourCC('n07Q'),
          FourCC('n07Z'), FourCC('h0F1'), FourCC('n07O'), FourCC('n034'), FourCC('n07N') })
    SetPlayerTechMaxAllowed(p, FourCC('n02X'), 0)
    SetPlayerTechMaxAllowed(p, FourCC('n02U'), 0)
end

function DemonPickEarth()
    local p = GetOwningPlayer(GetTriggerUnit())
    DemonPickElement(p, FourCC('A0W8'),
        { FourCC('n02Z'), FourCC('n033'), FourCC('n02Y'), FourCC('n07W') },
        { FourCC('n07S'), FourCC('n032'), FourCC('n07T'), FourCC('n035'), FourCC('n07X'),
          FourCC('n031'), FourCC('n07Y'), FourCC('n07R'), FourCC('n02P'), FourCC('n07Q'),
          FourCC('n07Z'), FourCC('h0F1'), FourCC('n07O'), FourCC('n034'), FourCC('n07N') })
    SetPlayerTechMaxAllowed(p, FourCC('n02X'), 0)
    SetPlayerTechMaxAllowed(p, FourCC('n02W'), 0)
end

function DemonPickWind()
    local p = GetOwningPlayer(GetTriggerUnit())
    DemonPickElement(p, FourCC('A0WA'),
        { FourCC('n07R'), FourCC('n02P'), FourCC('n07Z') },
        { FourCC('n07Q'), FourCC('n02Z'), FourCC('n033'), FourCC('n02Y'), FourCC('n07S'),
          FourCC('n07W'), FourCC('n032'), FourCC('n07T'), FourCC('n035'), FourCC('n07X'),
          FourCC('n031'), FourCC('n07Y'), FourCC('h0F1'), FourCC('n07O'), FourCC('n034'), FourCC('n07N') })
    SetPlayerTechMaxAllowed(p, FourCC('n02X'), 0)
    SetPlayerTechMaxAllowed(p, FourCC('n02Q'), 0)
end

-- Sargeras return damage
function SargerasReturnDamage()
    local attacker = GetEventDamageSource()
    if GetUnitAbilityLevel(attacker, FourCC('A0MQ')) > 0 and GetEventDamage() > 0 then
        local level = GetUnitAbilityLevel(attacker, FourCC('A0MQ'))
        local target = GetTriggerUnit()
        local missingHP = (GetUnitState(target, UNIT_STATE_MAX_LIFE) - GetUnitState(target, UNIT_STATE_LIFE)) / GetUnitState(target, UNIT_STATE_MAX_LIFE)
        local modifier = 1
        if GetUnitAbilityLevel(attacker, FourCC('A0NC')) > 0 then
            modifier = 1 + GetUnitAbilityLevel(attacker, FourCC('A0NC')) * 0.01
        end
        local dmg = GetEventDamage() * level * 0.03 * (1 + missingHP) * modifier
        UnitDamageTarget(target, attacker, dmg, true, false, ATTACK_TYPE_CHAOS, DAMAGE_TYPE_UNKNOWN, nil)
    end
end

-- ============================================================
-- UNDEAD: Arthas spells
-- ============================================================

function ArthasResurrection()
    local killer = GetKillingUnit()
    if GetUnitAbilityLevel(killer, FourCC('A0WB')) > 0 then
        local u = GetTriggerUnit()
        local dummy = CreateUnit(GetOwningPlayer(killer), FourCC('H0BN'), GetUnitX(u), GetUnitY(u), 0)
        UnitAddAbility(dummy, FourCC('A0WC'))
        if IssueTargetOrder(dummy, "animatedead", u) then
            -- success
        end
        UnitApplyTimedLife(dummy, FourCC('BTLF'), 1.0)
    end
end

function ArthasMassCoils()
    local caster = GetTriggerUnit()
    local target = GetSpellTargetUnit()
    local level = GetUnitAbilityLevel(caster, FourCC('A0WD'))
    local p = GetOwningPlayer(caster)
    local g = CreateGroup()

    GroupEnumUnitsInRange(g, GetUnitX(target), GetUnitY(target), 125, nil)
    ForGroup(g, function()
        local eu = GetEnumUnit()
        if IsUnitEnemy(eu, p) then
            local d = CreateUnit(p, FourCC('H0BN'), GetUnitX(target), GetUnitY(target), 0)
            UnitAddAbility(d, FourCC('AUdc'))
            SetUnitAbilityLevel(d, FourCC('AUdc'), level)
            IssueTargetOrder(d, "deathcoil", eu)
            UnitApplyTimedLife(d, FourCC('BTLF'), 1.0)
        end
    end)
    DestroyGroup(g)
end

function ArthasMassNova()
    local caster = GetTriggerUnit()
    local level = GetUnitAbilityLevel(caster, FourCC('A0WE'))
    local p = GetOwningPlayer(caster)
    local g = CreateGroup()

    GroupEnumUnitsInRange(g, GetUnitX(caster), GetUnitY(caster), 240, nil)
    ForGroup(g, function()
        local eu = GetEnumUnit()
        if IsUnitEnemy(eu, p) then
            local d = CreateUnit(p, FourCC('H0BN'), GetUnitX(caster), GetUnitY(caster), 0)
            UnitAddAbility(d, FourCC('A0WF'))
            SetUnitAbilityLevel(d, FourCC('A0WF'), level)
            IssuePointOrder(d, "frostnova", GetUnitX(eu), GetUnitY(eu))
            UnitApplyTimedLife(d, FourCC('BTLF'), 1.0)
        end
    end)
    DestroyGroup(g)
end

-- Passive Talisra: escape on lethal damage
function PassiveTalisra()
    local u = GetTriggerUnit()
    if IsUnitType(u, UNIT_TYPE_HERO) then return end
    local hp = GetUnitState(u, UNIT_STATE_LIFE)
    local maxHP = GetUnitState(u, UNIT_STATE_MAX_LIFE)
    local dmg = GetEventDamage()
    if hp - dmg <= 0 then
        local pi = GetPlayerId(GetOwningPlayer(u))
        local chance = 0.25 + 0.0625 * math.max(GetUnitAbilityLevel(u, FourCC('B08J')), GetUnitAbilityLevel(u, FourCC('B08K')))
        if GetRandomReal(0, 1) <= chance then
            local g2 = CreateGroup()
            GroupEnumUnitsInRange(g2, GetUnitX(u), GetUnitY(u), 650, nil)
            local hasSavior = false
            ForGroup(g2, function()
                if GetUnitAbilityLevel(GetEnumUnit(), FourCC('A1OS')) > 0 then hasSavior = true end
            end)
            DestroyGroup(g2)

            if hasSavior and G.playerCapital[pi] ~= nil then
                SetUnitX(u, GetUnitX(G.playerCapital[pi]))
                SetUnitY(u, GetUnitY(G.playerCapital[pi]))
                SetUnitState(u, UNIT_STATE_LIFE, maxHP * 0.1)
                BlzSetEventDamage(0)
            end
        end
    end
end

-- ============================================================
-- ICE TROLLS: Loa choice system
-- ============================================================

function KillLoa_Action()
    local p = GetOwningPlayer(GetTriggerUnit())
    SetPlayerTechResearched(p, FourCC('R0IX'), 1)
    -- Disable both loa spells, enable alternative path
    SetPlayerAbilityAvailable(p, FourCC('A1FS'), false)
    SetPlayerAbilityAvailable(p, FourCC('A1FR'), false)
    -- Enable Soul Caller, Golem, Loa consumption
    SetPlayerTechMaxAllowed(p, FourCC('n07B'), -1)
    SetPlayerTechResearched(p, FourCC('R09L'), 1)
    SetPlayerTechMaxAllowed(p, FourCC('o04T'), -1)
    SetPlayerTechResearched(p, FourCC('R09P'), 1)
    SetPlayerTechResearched(p, FourCC('R0AI'), 1)
    SetPlayerTechResearched(p, FourCC('R0AJ'), 1)
    SetPlayerTechResearched(p, FourCC('R0AD'), 1)
end

function ServeLoa_Action()
    local p = GetOwningPlayer(GetTriggerUnit())
    SetPlayerTechResearched(p, FourCC('R0IY'), 1)
    SetPlayerAbilityAvailable(p, FourCC('A1FS'), false)
    SetPlayerAbilityAvailable(p, FourCC('A1FR'), false)
    -- Enable Mamont, Magnataur, Loa units, Loa altars
    SetPlayerTechMaxAllowed(p, FourCC('n05W'), -1)
    SetPlayerTechMaxAllowed(p, FourCC('n05X'), -1)
    SetPlayerTechResearched(p, FourCC('R0I5'), 1)
    SetPlayerTechMaxAllowed(p, FourCC('n061'), 1)
    SetPlayerTechMaxAllowed(p, FourCC('n062'), 1)
    SetPlayerTechMaxAllowed(p, FourCC('o05B'), 1)
    SetPlayerTechMaxAllowed(p, FourCC('o06J'), 1)
    SetPlayerTechMaxAllowed(p, FourCC('o06K'), 1)
    SetPlayerTechMaxAllowed(p, FourCC('o06I'), 1)
end

-- ============================================================
-- FORSAKEN: Plague stances (simplified pattern)
-- ============================================================

function ForsakenSwitchStance(p, removeAbils, addAbil, abilCD, globalAbil, globalCD)
    for _, rid in ipairs(removeAbils) do
        SetPlayerAbilityAvailable(p, rid, false)
    end
    SetPlayerAbilityAvailable(p, addAbil, true)
    if abilCD > 0 then BlzStartUnitAbilityCooldown(GetTriggerUnit(), addAbil, abilCD) end
    if globalAbil and globalCD > 0 then BlzStartUnitAbilityCooldown(GetTriggerUnit(), globalAbil, globalCD) end
end

function ForsakenInfect()    ForsakenSwitchStance(GetOwningPlayer(GetTriggerUnit()), {FourCC('A13O'), FourCC('A13M')}, FourCC('A13N'), 12, FourCC('A13K'), 45) end
function ForsakenZagraz()    ForsakenSwitchStance(GetOwningPlayer(GetTriggerUnit()), {FourCC('A13N'), FourCC('A13M')}, FourCC('A13O'), 12, FourCC('A13K'), 45) end
function ForsakenKorroz()    ForsakenSwitchStance(GetOwningPlayer(GetTriggerUnit()), {FourCC('A13L'), FourCC('A13P')}, FourCC('A13Q'), 19.5, FourCC('A13J'), 45) end
function ForsakenSafety()    ForsakenSwitchStance(GetOwningPlayer(GetTriggerUnit()), {FourCC('A13L'), FourCC('A13Q')}, FourCC('A13P'), 19.5, FourCC('A13J'), 45) end

-- ============================================================
-- ELEMENTALS: Gnev (Wrath) and Necropol mutual exclusion
-- ============================================================

function ElementalMutualExclusion(startTech, blockTech, cancelTech, unblockTech)
    local p = GetOwningPlayer(GetTriggerUnit())
    SetPlayerTechMaxAllowed(p, blockTech, 0)
end

function ElementalMutualExclusionCancel(startTech, blockTech)
    local p = GetOwningPlayer(GetTriggerUnit())
    SetPlayerTechMaxAllowed(p, blockTech, -1)
end

-- ============================================================
-- JUNGLE TROLLS: Ultimate summon
-- ============================================================

function JungleUltStart()
    local hero = GetTriggerUnit()
    local p = GetOwningPlayer(hero)
    if GetPlayerState(p, PLAYER_STATE_RESOURCE_GOLD) < 8000 or GetPlayerState(p, PLAYER_STATE_RESOURCE_LUMBER) < 8000 then return end
    SetPlayerState(p, PLAYER_STATE_RESOURCE_GOLD, GetPlayerState(p, PLAYER_STATE_RESOURCE_GOLD) - 8000)
    SetPlayerState(p, PLAYER_STATE_RESOURCE_LUMBER, GetPlayerState(p, PLAYER_STATE_RESOURCE_LUMBER) - 8000)
    UnitAddAbility(hero, FourCC('MIM4'))
    PauseUnit(hero, true)
    TimerStart(CreateTimer(), 50.0, false, function()
        PauseUnit(hero, false)
        IssueImmediateOrder(hero, "stomp")
    end)
end

function JungleUltSummon()
    local hero = GetTriggerUnit()
    local x, y = GetUnitX(hero), GetUnitY(hero)
    local u = CreateUnit(GetOwningPlayer(hero), FourCC('mim1'), x, y, 0)
    UnitRemoveAbility(hero, FourCC('MIM4'))
end

function MassHex()
    local caster = GetTriggerUnit()
    local target = GetSpellTargetLoc()
    local level = GetUnitAbilityLevel(caster, FourCC('VLJ1'))
    local p = GetOwningPlayer(caster)
    local g = CreateGroup()
    GroupEnumUnitsInRange(g, GetLocationX(target), GetLocationY(target), 300, nil)
    ForGroup(g, function()
        local eu = GetEnumUnit()
        if IsUnitEnemy(eu, p) then
            local d = CreateUnit(p, FourCC('repD'), GetUnitX(eu), GetUnitY(eu), 0)
            UnitAddAbility(d, FourCC('VLJ5'))
            SetUnitAbilityLevel(d, FourCC('VLJ5'), level)
            IssueTargetOrder(d, "hex", eu)
            UnitApplyTimedLife(d, FourCC('BTLF'), 1.0)
        end
    end)
    DestroyGroup(g)
    RemoveLocation(target)
end

-- ============================================================
-- PvE: Lord spells
-- ============================================================

function LordWave()
    local caster = GetTriggerUnit()
    local p = GetOwningPlayer(caster)
    local target = GetSpellTargetLoc()
    local g = CreateGroup()
    GroupEnumUnitsInRange(g, GetUnitX(caster), GetUnitY(caster), 700, nil)
    ForGroup(g, function()
        local eu = GetEnumUnit()
        local utype = GetUnitTypeId(eu)
        if utype == FourCC('lord') or utype == FourCC('nq01') then
            UnitAddAbility(eu, FourCC('NQ14'))
            IssuePointOrder(eu, "carrionswarm", GetLocationX(target), GetLocationY(target))
            UnitRemoveAbility(eu, FourCC('NQ14'))
        end
    end)
    DestroyGroup(g)
    RemoveLocation(target)
end

function LordSpawnEgg()
    local caster = GetTriggerUnit()
    local p = GetOwningPlayer(caster)
    local level = GetUnitAbilityLevel(caster, FourCC('NQ06'))
    local lordCount = 0
    local g = CreateGroup()
    GroupEnumUnitsOfPlayer(g, p, nil)
    ForGroup(g, function()
        if GetUnitTypeId(GetEnumUnit()) == FourCC('lord') then lordCount = lordCount + 1 end
    end)
    DestroyGroup(g)

    if (level == 1 and lordCount == 0) or (level >= 2 and lordCount < 3) then
        local target = GetSpellTargetUnit()
        local x, y = GetUnitX(target), GetUnitY(target)
        RemoveUnit(target)
        local egg = CreateUnit(p, FourCC('lorE'), x, y, 0)
        UnitApplyTimedLife(egg, FourCC('BTLF'), 60)
    end
end

function LordEggBirth()
    local egg = GetTriggerUnit()
    CreateUnit(GetOwningPlayer(egg), FourCC('lord'), GetUnitX(egg), GetUnitY(egg), 0)
end

-- ============================================================
-- Init triggers registration
-- ============================================================

function InitSpellsRaces2()
    -- Silitids: MainSpawn2
    InitSpellTrig(EVENT_PLAYER_UNIT_CONSTRUCT_FINISH,
        function() return GetUnitTypeId(GetConstructedStructure()) == FourCC('e01H') end,
        MainSpawn2_Action)

    -- Demons: Element picks
    InitSpellTrig(EVENT_PLAYER_UNIT_SPELL_EFFECT, function() return GetSpellAbilityId() == FourCC('A0W9') end, DemonPickFire)
    InitSpellTrig(EVENT_PLAYER_UNIT_SPELL_EFFECT, function() return GetSpellAbilityId() == FourCC('A0W7') end, DemonPickWater)
    InitSpellTrig(EVENT_PLAYER_UNIT_SPELL_EFFECT, function() return GetSpellAbilityId() == FourCC('A0W8') end, DemonPickEarth)
    InitSpellTrig(EVENT_PLAYER_UNIT_SPELL_EFFECT, function() return GetSpellAbilityId() == FourCC('A0WA') end, DemonPickWind)

    -- Demons: Sargeras return damage
    InitSpellTrig(EVENT_PLAYER_UNIT_DAMAGED, nil, SargerasReturnDamage)

    -- Undead: Arthas
    InitSpellTrig(EVENT_PLAYER_UNIT_DEATH,
        function() return GetUnitAbilityLevel(GetKillingUnit(), FourCC('A0WB')) > 0 end,
        ArthasResurrection)
    InitSpellTrig(EVENT_PLAYER_UNIT_SPELL_EFFECT, function() return GetSpellAbilityId() == FourCC('A0WD') end, ArthasMassCoils)
    InitSpellTrig(EVENT_PLAYER_UNIT_SPELL_EFFECT, function() return GetSpellAbilityId() == FourCC('A0WE') end, ArthasMassNova)

    -- Undead: Passive Talisra
    InitSpellTrig(EVENT_PLAYER_UNIT_DAMAGED, nil, PassiveTalisra)

    -- Elementals: Gnev/Necropol research mutual exclusion
    InitSpellTrig({ EVENT_PLAYER_UNIT_RESEARCH_FINISH, EVENT_PLAYER_UNIT_RESEARCH_START },
        function() return GetResearched() == FourCC('R05B') end,
        function() ElementalMutualExclusion(FourCC('R05B'), FourCC('R05K')) end)
    InitSpellTrig({ EVENT_PLAYER_UNIT_RESEARCH_FINISH, EVENT_PLAYER_UNIT_RESEARCH_START },
        function() return GetResearched() == FourCC('R05K') end,
        function() ElementalMutualExclusion(FourCC('R05K'), FourCC('R05B')) end)

    -- Jungle Trolls
    InitSpellTrig(EVENT_PLAYER_UNIT_SPELL_EFFECT, function() return GetSpellAbilityId() == FourCC('VLJ1') end, MassHex)

    -- PvE: Lord spells
    InitSpellTrig(EVENT_PLAYER_UNIT_SPELL_EFFECT, function() return GetSpellAbilityId() == FourCC('NQ02') end, LordWave)
    InitSpellTrig(EVENT_PLAYER_UNIT_SPELL_EFFECT, function() return GetSpellAbilityId() == FourCC('NQ06') end, LordSpawnEgg)
    InitSpellTrig(EVENT_PLAYER_UNIT_DEATH, function() return GetUnitTypeId(GetTriggerUnit()) == FourCC('lorE') end, LordEggBirth)

    -- Silitids: Lich dead/Yley dead
    InitSpellTrig(EVENT_PLAYER_UNIT_DEATH,
        function()
            local uid = GetUnitTypeId(GetTriggerUnit())
            return uid == FourCC('e01I') or uid == FourCC('e01H')
        end,
        function()
            local u = GetTriggerUnit()
            local id = tostring(GetHandleId(u))
            local d = G.SilitidHiveData[id]
            if d then
                if GetUnitTypeId(u) == FourCC('e01I') then
                    d.count = math.max(0, d.count - 1)
                else
                    d.max = 0
                    d.count = 0
                    PauseTimer(d.timer)
                    G.SilitidHiveData[id] = nil
                end
            end
        end)
end
