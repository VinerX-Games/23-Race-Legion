-- ============================================================
-- 23 Race Legion - Lua Rewrite
-- output/economy.lua — Gold/lumber income, consumption, corruption, logistics
-- ============================================================

-- ============================================================
-- StartInc: Initialize income arrays
-- ============================================================

function StartInc()
    for i = 0, 23 do
        G.income[i] = 0
        G.incomeW[i] = 0
        G.disincome[i] = 0
        G.logistic[i] = 0
        G.corruption[i] = 0
        G.balance[i] = 0
        G.additional[i] = 0
        G.AllyTax[i] = 0
    end
    -- Allmap is created in globals
    RegionAddRect(G.Allmap, GetWorldBounds())
end

-- ============================================================
-- Army Experience Bonus
-- ============================================================

function ArmyExpSetBonus(pi)
    local level = math.floor((G.ArmyExp[pi] / 500) + 1)
    if level > 11 then level = 11 end
    SetUnitAbilityLevel(G.ArmyExpBonus[pi], FourCC('arb1'), level)
    SetUnitAbilityLevel(G.ArmyExpBonus[pi], FourCC('arb0'), level)
end

-- ============================================================
-- AddCountDis: Add unit to consumption tracking
-- ============================================================

function AddCountDis(u, pi)
    if u == nil then return end
    local i

    -- Building case (or building simulator with ability A1IJ)
    if IsUnitType(u, UNIT_TYPE_STRUCTURE) or GetUnitAbilityLevel(u, FourCC('A1IJ')) > 0 then
        if IsUnitInGroup(u, G.udg_BuildedSctructure[1]) then
            G.income[pi] = G.income[pi] + GetUnitFoodMade(u)

            -- Income bonuses from abilities
            if GetUnitAbilityLevel(u, FourCC('A0AY')) >= 1 then
                G.income[pi] = G.income[pi] + (100.0 * GetUnitAbilityLevel(u, FourCC('A0AY')))
            elseif GetUnitAbilityLevel(u, FourCC('A0SM')) >= 1 then
                G.income[pi] = G.income[pi] + (75.0 * GetUnitAbilityLevel(u, FourCC('A0SM')))
            elseif GetUnitAbilityLevel(u, FourCC('A0VS')) == 1 then
                G.income[pi] = G.income[pi] + 100
            end

            -- Tax transfer between players (A1HS)
            if GetUnitAbilityLevel(u, FourCC('A1HS')) > 0 then
                G.income[pi] = G.income[pi] - 5
                i = HashLoadInteger(u, 0)
                G.income[i] = G.income[i] + 5
            end

            -- Lumber income (A0B5)
            i = GetUnitAbilityLevel(u, FourCC('A0B5'))
            if i > 0 then
                G.incomeW[pi] = G.incomeW[pi] + (50.0 * i)
            end
        end

    -- Unit case
    else
        -- Not a summonded unit resurrection
        if not IsUnitType(u, UNIT_TYPE_SUMMONED) then
            G.udg_UnitsCount[pi] = G.udg_UnitsCount[pi] + 1

            if IsUnitType(u, UNIT_TYPE_HERO) then
                G.disincome[pi] = G.disincome[pi] + 100.0
                -- Treasury ability (A0XV)
                if GetUnitAbilityLevel(u, FourCC('A0XV')) ~= 0 then
                    G.income[pi] = G.income[pi] + (100 + GetUnitAbilityLevel(u, FourCC('A0XV')) * 100)
                end
            else
                G.udg_Price = GetUnitGoldCost(GetUnitTypeId(u))
                G.disincome[pi] = G.disincome[pi] + (G.udg_Price * G.Tax)

                -- Goblin fuel (A0A5)
                if GetUnitAbilityLevel(u, FourCC('A0A5')) ~= 0 then
                    G.disincome[pi] = G.disincome[pi] + ((G.udg_Price * G.Tax) * (1.60 - (0.10 * GetUnitAbilityLevel(u, FourCC('A0A5')))))
                -- Silithid generations (A0VH)
                elseif GetUnitAbilityLevel(u, FourCC('A0VH')) == 1 then
                    G.disincome[pi] = G.disincome[pi] - (G.udg_Price * G.Tax / 2)
                elseif GetUnitAbilityLevel(u, FourCC('A0VH')) == 2 then
                    G.disincome[pi] = G.disincome[pi] - (G.udg_Price * G.Tax / 3 * 2)
                end
            end

        -- Cult summoned units (A1HL)
        elseif GetUnitAbilityLevel(u, FourCC('A1HL')) > 0 then
            G.udg_UnitsCount[pi] = G.udg_UnitsCount[pi] + 1
            G.udg_Price = GetUnitGoldCost(GetUnitTypeId(u))
            G.disincome[pi] = G.disincome[pi] + (G.udg_Price * G.Tax / 2)
        end
    end

    UpdateGraf(pi)
end

-- ============================================================
-- DelCountDis: Remove unit from consumption tracking
-- ============================================================

function DelCountDis(u, pi)
    if u == nil then return end
    local i

    -- Building case
    if IsUnitType(u, UNIT_TYPE_STRUCTURE) or GetUnitAbilityLevel(u, FourCC('A1IJ')) > 0 then
        if IsUnitInGroup(u, G.udg_BuildedSctructure[1]) then
            G.income[pi] = G.income[pi] - GetUnitFoodMade(u)

            if GetUnitAbilityLevel(u, FourCC('A0AY')) >= 1 then
                G.income[pi] = G.income[pi] - (100.0 * GetUnitAbilityLevel(u, FourCC('A0AY')))
            elseif GetUnitAbilityLevel(u, FourCC('A0SM')) >= 1 then
                G.income[pi] = G.income[pi] - (75.0 * GetUnitAbilityLevel(u, FourCC('A0SM')))
            end

            if GetUnitAbilityLevel(u, FourCC('A0VS')) == 1 then
                G.income[pi] = G.income[pi] - 100
            end

            -- Tax transfer (A1HS)
            if GetUnitAbilityLevel(u, FourCC('A1HS')) > 0 then
                G.income[pi] = G.income[pi] + 5
                i = HashLoadInteger(u, 0)
                G.income[i] = G.income[i] - 5
                HashFlushChild(u)
            end

            -- Lumber income
            i = GetUnitAbilityLevel(u, FourCC('A0B5'))
            if i > 0 then
                G.incomeW[pi] = G.incomeW[pi] - (50.0 * i)
            end
        end

    -- Unit case (not summoned)
    elseif not IsUnitType(u, UNIT_TYPE_SUMMONED) then
        G.udg_UnitsCount[pi] = G.udg_UnitsCount[pi] - 1

        if IsUnitType(u, UNIT_TYPE_HERO) then
            G.disincome[pi] = G.disincome[pi] - 100.0

            if GetUnitAbilityLevel(u, FourCC('A0XV')) ~= 0 then
                G.income[pi] = G.income[pi] - (100 + GetUnitAbilityLevel(u, FourCC('A0XV')) * 100)
            end
        else
            G.udg_Price = GetUnitGoldCost(GetUnitTypeId(u))
            G.disincome[pi] = G.disincome[pi] - (G.udg_Price * G.Tax)

            -- Goblin fuel
            if GetUnitAbilityLevel(u, FourCC('A0A5')) ~= 0 then
                G.disincome[pi] = G.disincome[pi] - ((G.udg_Price * G.Tax) * (1.60 - (0.10 * GetUnitAbilityLevel(u, FourCC('A0A5')))))
            -- Silithid generations
            elseif GetUnitAbilityLevel(u, FourCC('A0VH')) == 1 then
                G.disincome[pi] = G.disincome[pi] + (G.udg_Price * G.Tax / 2)
            elseif GetUnitAbilityLevel(u, FourCC('A0VH')) == 2 then
                G.disincome[pi] = G.disincome[pi] + (G.udg_Price * G.Tax / 3 * 2)
            elseif GetUnitAbilityLevel(u, FourCC('OR00')) ~= 0 then
                G.disincome[pi] = G.disincome[pi] - ((G.udg_Price * G.Tax) * ((GetUnitAbilityLevel(u, FourCC('OR00')) - 35) / 100.0))
            end
        end

    -- Cult summoned units
    elseif GetUnitAbilityLevel(u, FourCC('A1HL')) > 0 then
        G.udg_UnitsCount[pi] = G.udg_UnitsCount[pi] - 1
        G.udg_Price = GetUnitGoldCost(GetUnitTypeId(u))
        G.disincome[pi] = G.disincome[pi] - (G.udg_Price * G.Tax / 2)
    end

    UpdateGraf(pi)
end

-- ============================================================
-- UpdateGraf: Refresh multiboard display
-- ============================================================

function UpdateGraf(pi)
    local p = Player(pi)
    local r = math.floor(G.udg_UnitsCount[pi] / 25.0)
    G.logistic[pi] = ((500 + 100 * (r - 1)) / 2 * r)

    -- Additional cost modifier
    if GetPlayerTechCount(p, FourCC('R0DV'), true) + GetPlayerTechCount(p, FourCC('R0GZ'), true) >= 1 then
        G.additional[pi] = G.disincome[pi] * (G.udg_MainPrice[pi] / (-100.0))
    end

    if G.DisOn then
        G.balance[pi] = G.income[pi] - G.disincome[pi] + G.corruption[pi] - G.logistic[pi] + G.additional[pi]
    else
        G.balance[pi] = G.income[pi]
    end

    -- Multiboard update
    MultiboardSetItemValue(G.MultiboardItem[G.MultiboardItemOwnerIndex[pi] * 2 + 1], tostring(G.udg_UnitsCount[pi]))
    PercentGraph(pi)
    ArmyExpGraph(pi)
end

-- ============================================================
-- PercentGraph: Show domination percentage
-- ============================================================

function PercentGraph(pi)
    if G.CityCount == 0 then return end
    MultiboardSetItemValue(G.ThirdColumn[pi], R2SW_Polyfill(G.CityPlayerCount[pi] * 100.0 / G.CityCount) .. "%")
end

-- ============================================================
-- ArmyExpGraph: Show army experience in multiboard
-- ============================================================

function ArmyExpGraph(pi)
    MultiboardSetItemValue(G.ArmyPowerColumn[pi], R2SW_Polyfill(G.ArmyExp[pi]))
end

-- ============================================================
-- TimerIncome: Periodic gold/lumber income & army XP
-- ============================================================

function TimerIncome()
    local p, t, r
    for i = 0, 23 do
        p = Player(i)

        if G.DisOn then
            -- Logistics (progressive tax per 25 units)
            r = math.floor(G.udg_UnitsCount[i] / 25.0)
            G.logistic[i] = ((500 + 100 * (r - 1)) / 2 * r)

            -- Corruption (tech R04O)
            t = GetPlayerTechCount(p, FourCC('R04O'), true)
            if t > 1 then
                G.corruption[i] = G.disincome[i] * ((t - 1) * 0.15)
                if G.EcLog then
                    G.udg_LocalText2 = "Коррупция" .. tostring(math.floor(G.corruption[i]))
                    DisplayTimedTextToPlayer(p, 0, 0, 7, G.udg_LocalText2)
                end
            end

            -- Additional cost (R0DV, R0GZ)
            t = GetPlayerTechCount(p, FourCC('R0DV'), true) + GetPlayerTechCount(p, FourCC('R0GZ'), true)
            if t >= 1 then
                G.additional[i] = G.disincome[i] * (G.udg_MainPrice[i] / (-100.0))
                if G.EcLog then
                    G.udg_LocalText2 = "Дополнительно: " .. tostring(math.floor(G.additional[i]))
                    DisplayTimedTextToPlayer(p, 0, 0, 7, G.udg_LocalText2)
                end
            end

            G.balance[i] = G.income[i] * (G.IncomeMod - G.AllyTax[i]) - G.disincome[i] - G.logistic[i] + G.corruption[i] + G.additional[i]
        else
            G.balance[i] = G.income[i] * (G.IncomeMod - G.AllyTax[i])
        end

        -- Debug logging
        if G.EcLog then
            G.udg_LocalText2 = "Доход: " .. R2S(G.income[i] * G.IncomeMod)
            DisplayTimedTextToPlayer(p, 0, 0, 7, G.udg_LocalText2)
            G.udg_LocalText2 = "Расход: " .. R2S(G.disincome[i])
            DisplayTimedTextToPlayer(p, 0, 0, 7, G.udg_LocalText2)
            G.udg_LocalText2 = "Логистика: " .. R2S(G.logistic[i])
            DisplayTimedTextToPlayer(p, 0, 0, 7, G.udg_LocalText2)
            G.udg_LocalText2 = "Юнитов: " .. tostring(G.udg_UnitsCount[i])
            DisplayTimedTextToPlayer(p, 0, 0, 7, G.udg_LocalText2)
            G.udg_LocalText2 = "Итого: " .. R2S(G.balance[i])
            DisplayTimedTextToPlayer(p, 0, 0, 7, G.udg_LocalText2)
            G.udg_LocalText2 = "Древесины: " .. R2S(G.incomeW[i])
            DisplayTimedTextToPlayer(p, 0, 0, 7, G.udg_LocalText2)
        end

        -- Apply income
        SetPlayerState(p, PLAYER_STATE_RESOURCE_GOLD, GetPlayerState(p, PLAYER_STATE_RESOURCE_GOLD) + math.floor(G.balance[i]))
        SetPlayerState(p, PLAYER_STATE_RESOURCE_LUMBER, GetPlayerState(p, PLAYER_STATE_RESOURCE_LUMBER) + math.floor(G.incomeW[i]))

        ArmyExpSetBonus(i)
    end
end

-- ============================================================
-- DisIncomeStart: Enable consumption system (after 600s)
-- ============================================================

function DisIncomeStart()
    ForForce(G.udg_AllPlayers, function()
        TimerDialogDisplayForPlayerBJ(false, G.udg_TimerToDis, GetEnumPlayer())
    end)
    TimerDialogDisplayBJ(false, G.udg_TimerToDis)
    G.DisOn = true
end

-- ============================================================
-- Income moderators (host abilities A1N6 = 0.75x, A1N7 = 1x)
-- ============================================================

function SetIncomeMod075()
    G.IncomeMod = 0.75
    DisplayTextToForce(GetPlayersAll(), "Доходы теперь 75% от нормальных")
end

function SetIncomeMod100()
    G.IncomeMod = 1.0
    DisplayTextToForce(GetPlayersAll(), "Доходы установлены по умолчанию")
end

-- ============================================================
-- Eclog commands
-- ============================================================

function EnableEcLog()
    G.EcLog = true
end

function DisableEcLog()
    G.EcLog = false
end

-- ============================================================
-- Income upgrade (A0VM -> A0VS)
-- ============================================================

function Trigger_Upgrade_Income()
    local pi = GetPlayerId(GetOwningPlayer(GetTriggerUnit()))
    UnitAddAbility(GetTriggerUnit(), FourCC('A0VS'))

    G.income[pi] = G.income[pi] + 100
    UpdateGraf(pi)

    UnitRemoveAbility(GetTriggerUnit(), FourCC('A0VJ'))

    UnitAddAbilityBJ(FourCC('A1M5'), GetTriggerUnit())
    BlzStartUnitAbilityCooldown(GetTriggerUnit(), FourCC('A1M5'), 5)
    RemoveAbilityTimed(GetTriggerUnit(), FourCC('A1M5'), 5)
    AddAbilityTimed(GetTriggerUnit(), FourCC('A146'), 5)
end

-- ============================================================
-- Economy filters (for InitForEconomics)
-- ============================================================

G.IncomeBuildings = nil
G.IncomeLumber = nil
G.DisFilter = nil

function f_IncomeBuildings()
    return GetUnitState(GetFilterUnit(), UNIT_STATE_LIFE) > 0 and GetUnitFoodMade(GetFilterUnit()) >= 1 and IsUnitInGroup(GetFilterUnit(), G.udg_BuildedSctructure[1])
end

function f_IncomeLumber()
    return GetUnitAbilityLevel(GetFilterUnit(), FourCC('A0B5')) >= 1
end

function f_DisFilter()
    return not IsUnitType(GetFilterUnit(), UNIT_TYPE_STRUCTURE) and GetUnitState(GetFilterUnit(), UNIT_STATE_LIFE) > 0
end

function InitForEconomics()
    G.IncomeBuildings = Filter(f_IncomeBuildings)
    G.IncomeLumber = Filter(f_IncomeLumber)
    G.DisFilter = Filter(f_DisFilter)
end

-- ============================================================
-- Unit Enter Map: Add to economy
-- ============================================================

G.gTriggerUnit = nil

function UnitEnterMap_Action()
    local u = G.gTriggerUnit

    -- Skip if dead
    if GetUnitState(u, UNIT_STATE_LIFE) < 0.7 then
        if not IsUnitInGroup(u, G.DeadGroup) then
            GroupAddUnit(G.DeadGroup, u)
            TriggerRegisterUnitStateEvent(G.gg_trg_UnitRevive, u, UNIT_STATE_LIFE, GREATER_THAN, 0.60)
        end
        return
    end

    AddCountDis(u, GetPlayerId(GetOwningPlayer(u)))
end

-- ============================================================
-- Unit Built: Track structure construction
-- ============================================================

function UnitBuilded_Action()
    local u = GetConstructedStructure()
    local p = GetOwningPlayer(u)
    local pi = GetPlayerId(p)

    GroupAddUnit(G.udg_BuildedSctructure[1], u)
    AddCountDis(u, pi)
end

-- ============================================================
-- Unit Dead: Remove from economy
-- ============================================================

function UnitDead_Action()
    local u = GetTriggerUnit()
    local p = GetOwningPlayer(u)
    local pi = GetPlayerId(p)

    -- Add army XP to killer
    addArmyExp(u, GetPlayerId(GetOwningPlayer(GetKillingUnit())))

    if GetUnitAbilityLevel(u, FourCC('BUan')) == 0 then
        DelCountDis(u, pi)
    else
        TimedCount(u) -- Recheck owner after 0.3s
    end

    SetUnitLifeBJ(u, 0)
    if not IsUnitInGroup(u, G.DeadGroup) then
        GroupAddUnit(G.DeadGroup, u)
        TriggerRegisterUnitStateEvent(G.gg_trg_UnitRevive, u, UNIT_STATE_LIFE, GREATER_THAN, 0.01)
    end
end

-- ============================================================
-- Unit Revive: Re-add to economy
-- ============================================================

function UnitRevive_Action()
    local u = GetTriggerUnit()
    local pi = GetPlayerId(GetOwningPlayer(u))
    AddCountDis(u, pi)
end

-- ============================================================
-- Initialize economy triggers
-- ============================================================

function InitEconomyTriggers()
    -- Income timer trigger
    TriggerRegisterTimerExpireEvent(CreateTrigger(), G.udg_IncomeTimerSecond)
    TriggerAddAction(bj_lastCreatedTrigger, TimerIncome)

    -- DisIncomeStart timer trigger (600s)
    TriggerRegisterTimerExpireEvent(CreateTrigger(), G.udg_IncomeTimerFirst)
    TriggerAddAction(bj_lastCreatedTrigger, DisIncomeStart)

    -- EcLog commands
    local t1 = CreateTrigger()
    TriggerRegisterPlayerChatEvent(t1, Player(0), "-EcLogOn", true)
    TriggerAddAction(t1, EnableEcLog)

    local t2 = CreateTrigger()
    TriggerRegisterPlayerChatEvent(t2, Player(0), "-EcLogOff", true)
    TriggerAddAction(t2, DisableEcLog)

    -- Income modifiers
    local t3 = CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(t3, EVENT_PLAYER_UNIT_SPELL_EFFECT)
    TriggerAddCondition(t3, Condition(function() return GetSpellAbilityId() == FourCC('A1N6') end))
    TriggerAddAction(t3, SetIncomeMod075)

    local t4 = CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(t4, EVENT_PLAYER_UNIT_SPELL_EFFECT)
    TriggerAddCondition(t4, Condition(function() return GetSpellAbilityId() == FourCC('A1N7') end))
    TriggerAddAction(t4, SetIncomeMod100)

    -- Income upgrade (A0VM)
    local t5 = CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(t5, EVENT_PLAYER_UNIT_SPELL_EFFECT)
    TriggerAddCondition(t5, Condition(function()
        return GetSpellAbilityId() == FourCC('A0VM') and IsUnitSelected(GetTriggerUnit(), GetOwningPlayer(GetTriggerUnit()))
    end))
    TriggerAddAction(t5, Trigger_Upgrade_Income)

    -- InitForEconomics
    InitForEconomics()
end
