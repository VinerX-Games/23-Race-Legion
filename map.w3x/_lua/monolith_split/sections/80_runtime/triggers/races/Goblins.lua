
--===========================================================================
-- Trigger: GoblinsOn
--===========================================================================
function Trig_GoblinsOn_Actions()
    EnableTrigger(gg_trg_CorrupTrain)
    EnableTrigger(gg_trg_CorrupPlus)
    EnableTrigger(gg_trg_CorrupMinus)
    EnableTrigger(gg_trg_Potreblenie)
    EnableTrigger(gg_trg_PotreblenieTrain)
    
    EnableTrigger(gg_trg_Brac)
    EnableTrigger(gg_trg_BracResearch)
    EnableTrigger(gg_trg_BracTrain)
    EnableTrigger(gg_trg_PodjogResearch)
    EnableTrigger(gg_trg_PodjogTrain)
    EnableTrigger(gg_trg_PodruvResearc)
    EnableTrigger(gg_trg_PodruvTrain)
    
    EnableTrigger(gg_trg_Samopodruv)
    EnableTrigger(gg_trg_Samopodjog)
    EnableTrigger(gg_trg_Adrenalin)
    
    
    
    
    EnableTrigger(gg_trg_Pulimetchik)
    EnableTrigger(gg_trg_Ognemetchik)
    EnableTrigger(gg_trg_Raketchik)
    EnableTrigger(gg_trg_Medic)
    EnableTrigger(gg_trg_Sniper)
    EnableTrigger(gg_trg_Saper)
    EnableTrigger(gg_trg_Car)
    EnableTrigger(gg_trg_Vezdehod)
    EnableTrigger(gg_trg_Tank)
    EnableTrigger(gg_trg_FireTank)
    EnableTrigger(gg_trg_Arta)
    EnableTrigger(gg_trg_Meha)
    EnableTrigger(gg_trg_OgneMeha)
    EnableTrigger(gg_trg_Eczo)
    EnableTrigger(gg_trg_Super)
    EnableTrigger(gg_trg_Submarina)
    EnableTrigger(gg_trg_Podlodka1)
    
    EnableTrigger(gg_trg_FarmLoseG)
    EnableTrigger(gg_trg_FarmBuildG)
   -- call EnableTrigger( gg_trg_SpellRecharge )
   -- call EnableTrigger( gg_trg_IconAutoRocket )
 
    
    
    
end
--===========================================================================
function InitTrig_GoblinsOn()
    gg_trg_GoblinsOn=CreateTrigger()
    TriggerAddAction(gg_trg_GoblinsOn, Trig_GoblinsOn_Actions)
end
--===========================================================================
-- Trigger: StartG
--===========================================================================
function goblinsStartLimits_act()
    SetPlayerTechResearchedSwap(FourCC('R04O'), 1, GetEnumPlayer())
    SetPlayerAbilityAvailableBJ(false, FourCC('A0AT'), GetEnumPlayer())
    SetPlayerTechMaxAllowedSwap(FourCC('H0BD'), 1, GetEnumPlayer())
    SetPlayerTechMaxAllowedSwap(FourCC('N018'), 1, GetEnumPlayer())
    SetPlayerTechMaxAllowedSwap(FourCC('N01A'), 1, GetEnumPlayer())
    SetPlayerTechMaxAllowedSwap(FourCC('N019'), 1, GetEnumPlayer())
    SetPlayerTechMaxAllowedSwap(FourCC('Nalc'), 1, GetEnumPlayer())
    SetPlayerTechMaxAllowedSwap(FourCC('Ntin'), 1, GetEnumPlayer())
    
    SetPlayerTechMaxAllowedSwap(FourCC('Gmex'), 1, GetEnumPlayer())
    SetPlayerTechMaxAllowedSwap(FourCC('Galh'), 1, GetEnumPlayer())
    
    
    SetPlayerTechMaxAllowedSwap(FourCC('h06L'), 0, GetEnumPlayer())
    SetPlayerTechMaxAllowedSwap(FourCC('h06N'), 0, GetEnumPlayer())
    SetPlayerTechMaxAllowedSwap(FourCC('h06Q'), 0, GetEnumPlayer())
    SetPlayerTechMaxAllowedSwap(FourCC('h06O'), 0, GetEnumPlayer())
    SetPlayerTechMaxAllowedSwap(FourCC('h078'), 0, GetEnumPlayer())
    SetPlayerTechMaxAllowedSwap(FourCC('h06M'), 0, GetEnumPlayer())
    SetPlayerTechMaxAllowedSwap(FourCC('h06P'), 0, GetEnumPlayer())
    SetPlayerTechMaxAllowedSwap(FourCC('h06U'), 0, GetEnumPlayer())
    SetPlayerTechMaxAllowedSwap(FourCC('h06Y'), 0, GetEnumPlayer())
    SetPlayerTechMaxAllowedSwap(FourCC('h06S'), 0, GetEnumPlayer())
    SetPlayerTechMaxAllowedSwap(FourCC('h06T'), 0, GetEnumPlayer())
    SetPlayerTechMaxAllowedSwap(FourCC('o00W'), 0, GetEnumPlayer())
    SetPlayerTechMaxAllowedSwap(FourCC('o00Y'), 0, GetEnumPlayer())
    SetPlayerTechMaxAllowedSwap(FourCC('o00X'), 0, GetEnumPlayer())
    SetPlayerTechMaxAllowedSwap(FourCC('h06R'), 0, GetEnumPlayer())
    SetPlayerTechMaxAllowedSwap(FourCC('h06V'), 0, GetEnumPlayer())
    SetPlayerTechMaxAllowedSwap(FourCC('h06W'), 0, GetEnumPlayer())
end
function goblinsStartLimits()
    ForForce(bj_FORCE_ALL_PLAYERS, goblinsStartLimits_act)
    ForForce(udg_Bots, goblinsStartLimits_act)
end
function Trig_StartG_Actions()
    goblinsStartLimits()
end
--===========================================================================
function InitTrig_StartG()
    gg_trg_StartG=CreateTrigger()
    TriggerRegisterTimerEventSingle(gg_trg_StartG, 5.00)
    TriggerAddAction(gg_trg_StartG, Trig_StartG_Actions)
end
--===========================================================================
-- Trigger: GoblinSold
--===========================================================================
function Trig_GoblinSold_Conditions()
    return GetUnitTypeId(GetTriggerUnit()) == FourCC('h073')
end
function Trig_GoblinSold_Func002Func001C()
    return (( GetOwningPlayer(GetTriggerUnit()) ~= GetOwningPlayer(GetSoldUnit()) )) and GetPlayerAlliance(GetOwningPlayer(GetTriggerUnit()), GetOwningPlayer(GetSoldUnit()), ALLIANCE_SHARED_ADVANCED_CONTROL)
end
function Trig_GoblinSold_Func002Func002C()
    return (( ( GetOwningPlayer(GetTriggerUnit()) == GetOwningPlayer(GetSoldUnit()) ) )) or GetPlayerAlliance(GetOwningPlayer(GetTriggerUnit()), GetOwningPlayer(GetSoldUnit()), ALLIANCE_SHARED_ADVANCED_CONTROL)
end
function Trig_GoblinSold_Func002C()
    return Trig_GoblinSold_Func002Func002C()
end
function Trig_GoblinSold_Actions()
    local pi= GetPlayerId(GetOwningPlayer(GetTriggerUnit()))
    if Trig_GoblinSold_Func002C() then
        if Trig_GoblinSold_Func002Func001C() then
            SetUnitOwner(GetSoldUnit(), GetOwningPlayer(GetTriggerUnit()), true)
            AddCountDis(GetSoldUnit() , GetPlayerId(GetOwningPlayer(GetTriggerUnit())))
            DelCountDis(GetSoldUnit() , GetPlayerId(GetOwningPlayer(GetSoldUnit())))
            GoldDifference[pi]=GoldDifference[pi] - GetUnitGoldCost(GetUnitTypeId(GetSoldUnit()))
            LumberDifference[pi]=LumberDifference[pi] - GetUnitWoodCost(GetUnitTypeId(GetSoldUnit()))
        end
        udg_LocalPosition2=GetUnitRallyPoint(GetTriggerUnit())
        IssuePointOrderLocBJ(GetSoldUnit(), "move", udg_LocalPosition2)
        RemoveLocation(udg_LocalPosition2)
    else
        RemoveUnit(GetSoldUnit())
        DelCountDis(GetSoldUnit() , GetPlayerId(GetOwningPlayer(GetSoldUnit())))
    end
end
--===========================================================================
function InitTrig_GoblinSold()
    gg_trg_GoblinSold=CreateTrigger()
    DisableTrigger(gg_trg_GoblinSold)
    TriggerRegisterAnyUnitEventBJ(gg_trg_GoblinSold, EVENT_PLAYER_UNIT_SELL)
    TriggerAddCondition(gg_trg_GoblinSold, Condition(Trig_GoblinSold_Conditions))
    TriggerAddAction(gg_trg_GoblinSold, Trig_GoblinSold_Actions)
end
--===========================================================================
-- Trigger: IconAutoRocket
--===========================================================================
function Trig_IconAutoRocket_Conditions()
    return GetLearnedSkillBJ() == FourCC('A1N1')
end
function Trig_IconAutoRocket_Actions()
    UnitAddAbility(GetLearningUnit(), FourCC('A1N2'))
end
--===========================================================================
function InitTrig_IconAutoRocket()
    gg_trg_IconAutoRocket=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_IconAutoRocket, EVENT_PLAYER_HERO_SKILL)
    TriggerAddCondition(gg_trg_IconAutoRocket, Condition(Trig_IconAutoRocket_Conditions))
    TriggerAddAction(gg_trg_IconAutoRocket, Trig_IconAutoRocket_Actions)
end
--===========================================================================
-- Trigger: SpellRecharge
--===========================================================================
function Trig_SpellRecharge_Actions()
    BlzEndUnitAbilityCooldown(GetTriggerUnit(), FourCC('A0DU'))
    BlzEndUnitAbilityCooldown(GetTriggerUnit(), FourCC('A1N0'))
    BlzEndUnitAbilityCooldown(GetTriggerUnit(), FourCC('A1N3'))
    BlzEndUnitAbilityCooldown(GetTriggerUnit(), FourCC('A1N1'))
    
end
--===========================================================================
function InitTrig_SpellRecharge()
    gg_trg_SpellRecharge=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_SpellRecharge, EVENT_PLAYER_UNIT_SPELL_CAST)
    TriggerAddAction(gg_trg_SpellRecharge, function()
        if GetSpellAbilityId() ~= FourCC('A1N4') then return end
        Trig_SpellRecharge_Actions()
    end)
end
--===========================================================================
-- Trigger: CorrupTrain
--===========================================================================
function Trig_CorrupTrain_Conditions()
    return GetPlayerTechCountSimple(FourCC('R04O'), GetOwningPlayer(GetTriggerUnit())) >= 1
end
function Trig_CorrupTrain_Actions()
    SetUnitAbilityLevelSwapped(FourCC('A0AV'), GetTrainedUnit(), GetPlayerTechCountSimple(FourCC('R04O'), GetOwningPlayer(GetTriggerUnit())))
    SetUnitAbilityLevelSwapped(FourCC('A0AW'), GetTrainedUnit(), GetPlayerTechCountSimple(FourCC('R04O'), GetOwningPlayer(GetTriggerUnit())))
end
--===========================================================================
function InitTrig_CorrupTrain()
    gg_trg_CorrupTrain=CreateTrigger()
    DisableTrigger(gg_trg_CorrupTrain)
    TriggerRegisterAnyUnitEventBJ(gg_trg_CorrupTrain, EVENT_PLAYER_UNIT_TRAIN_FINISH)
    TriggerAddCondition(gg_trg_CorrupTrain, Condition(Trig_CorrupTrain_Conditions))
    TriggerAddAction(gg_trg_CorrupTrain, Trig_CorrupTrain_Actions)
end
--===========================================================================
-- Trigger: CorrupPlus
--===========================================================================
function Trig_CorrupPlus_Func008A()
    SetUnitAbilityLevelSwapped(FourCC('A0AW'), GetEnumUnit(), GetPlayerTechCountSimple(FourCC('R04O'), GetOwningPlayer(GetEnumUnit())))
    SetUnitAbilityLevelSwapped(FourCC('A0AV'), GetEnumUnit(), GetPlayerTechCountSimple(FourCC('R04O'), GetOwningPlayer(GetEnumUnit())))
end
function Trig_CorrupPlus_Actions()
    local t= CreateTimer()
    local tid= GetHandleId(t)
    local p= GetOwningPlayer(GetTriggerUnit())
    SetPlayerAbilityAvailableBJ(false, FourCC('A0AS'), p)
    SetPlayerAbilityAvailableBJ(false, FourCC('A0AT'), p)
    SetPlayerTechResearchedSwap(FourCC('R04O'), GetPlayerTechCountSimple(FourCC('R04O'), p) + 1, p)
    
    GroupEnumUnitsOfPlayer(udg_LocalOtrad2, p, nil)
    ForGroupBJ(udg_LocalOtrad2, Trig_CorrupPlus_Func008A)
    GroupClear(udg_LocalOtrad2)
    
	local p2 = p
	TimerStart(t, 60, false, function()
		if GetPlayerTechCountSimple(FourCC('R04O'), p2) == 6 then
			SetPlayerAbilityAvailableBJ(true, FourCC('A0AT'), p2)
		else
			SetPlayerAbilityAvailableBJ(true, FourCC('A0AS'), p2)
			SetPlayerAbilityAvailableBJ(true, FourCC('A0AT'), p2)
		end
		DestroyTimer(t)
	end)
    
    
    t=nil
end
--===========================================================================
function InitTrig_CorrupPlus()
    gg_trg_CorrupPlus=CreateTrigger()
    DisableTrigger(gg_trg_CorrupPlus)
    TriggerRegisterAnyUnitEventBJ(gg_trg_CorrupPlus, EVENT_PLAYER_UNIT_SPELL_EFFECT)
    TriggerAddAction(gg_trg_CorrupPlus, function()
        if GetSpellAbilityId() ~= FourCC('A0AS') then return end
        Trig_CorrupPlus_Actions()
    end)
end
--===========================================================================
-- Trigger: CorrupMinus
--===========================================================================
function Trig_CorrupMinus_Func008A()
    SetUnitAbilityLevelSwapped(FourCC('A0AW'), GetEnumUnit(), GetPlayerTechCountSimple(FourCC('R04O'), GetOwningPlayer(GetEnumUnit())))
    SetUnitAbilityLevelSwapped(FourCC('A0AV'), GetEnumUnit(), GetPlayerTechCountSimple(FourCC('R04O'), GetOwningPlayer(GetEnumUnit())))
end
function Trig_CorrupMinus_Actions()
    local t= CreateTimer()
    local tid= GetHandleId(t)
    local p= GetOwningPlayer(GetTriggerUnit())
    SetPlayerAbilityAvailableBJ(false, FourCC('A0AS'), p)
    SetPlayerAbilityAvailableBJ(false, FourCC('A0AT'), p)
    SetPlayerTechResearchedSwap(FourCC('R04O'), GetPlayerTechCountSimple(FourCC('R04O'), p) - 1, p)
    GroupEnumUnitsOfPlayer(udg_LocalOtrad2, p, nil)
    ForGroupBJ(udg_LocalOtrad2, Trig_CorrupMinus_Func008A)
    GroupClear(udg_LocalOtrad2)
    
    
	local p2 = p
	TimerStart(t, 60, false, function()
		if GetPlayerTechCountSimple(FourCC('R04O'), p2) == 1 then
			SetPlayerAbilityAvailableBJ(true, FourCC('A0AS'), p2)
		else
			SetPlayerAbilityAvailableBJ(true, FourCC('A0AS'), p2)
			SetPlayerAbilityAvailableBJ(true, FourCC('A0AT'), p2)
		end
		DestroyTimer(t)
	end)
    
   
    
    t=nil
end
--===========================================================================
function InitTrig_CorrupMinus()
    gg_trg_CorrupMinus=CreateTrigger()
    DisableTrigger(gg_trg_CorrupMinus)
    TriggerRegisterAnyUnitEventBJ(gg_trg_CorrupMinus, EVENT_PLAYER_UNIT_SPELL_EFFECT)
    TriggerAddAction(gg_trg_CorrupMinus, function()
        if GetSpellAbilityId() ~= FourCC('A0AT') then return end
        Trig_CorrupMinus_Actions()
    end)
end
--===========================================================================
-- Trigger: Potreblenie
--===========================================================================
function Trig_Potreblenie_Conditions()
    return GetResearched() == FourCC('R04N')
end
function Trig_Potreblenie_Func001C()
    return GetPlayerTechCountSimple(FourCC('R04N'), GetOwningPlayer(GetTriggerUnit())) == 6
end
function Trig_Potreblenie_Func002002()
    return GetUnitAbilityLevelSwapped(FourCC('A0A5'), GetFilterUnit()) ~= 0
end
function Trig_Potreblenie_Func005A()
    SetUnitAbilityLevelSwapped(FourCC('A0A5'), GetEnumUnit(), GetPlayerTechCountSimple(FourCC('R04N'), GetOwningPlayer(GetTriggerUnit())) + 1)
end
function Trig_Potreblenie_Actions()
    if Trig_Potreblenie_Func001C() then
        SetPlayerAbilityAvailableBJ(false, FourCC('A0A5'), GetOwningPlayer(GetTriggerUnit()))
        return
    end
    udg_Boolexpr = Trig_Potreblenie_Func002002
    GroupEnumUnitsOfPlayer(udg_LocalOtrad2, udg_LocalPlayer, udg_Boolexpr)
    ForGroupBJ(udg_LocalOtrad2, Trig_Potreblenie_Func005A)
    GroupClear(udg_LocalOtrad2)
end
--===========================================================================
function InitTrig_Potreblenie()
    gg_trg_Potreblenie=CreateTrigger()
    DisableTrigger(gg_trg_Potreblenie)
    TriggerRegisterAnyUnitEventBJ(gg_trg_Potreblenie, EVENT_PLAYER_UNIT_RESEARCH_FINISH)
    TriggerAddCondition(gg_trg_Potreblenie, Condition(Trig_Potreblenie_Conditions))
    TriggerAddAction(gg_trg_Potreblenie, Trig_Potreblenie_Actions)
end
--===========================================================================
-- Trigger: PotreblenieTrain
--===========================================================================
function Trig_PotreblenieTrain_Conditions()
    return GetUnitAbilityLevelSwapped(FourCC('A0A5'), GetTriggerUnit()) >= 1
end
function Trig_PotreblenieTrain_Actions()
    SetUnitAbilityLevelSwapped(FourCC('A0A5'), GetEnumUnit(), GetPlayerTechCountSimple(FourCC('R04N'), GetOwningPlayer(GetTriggerUnit())) + 1)
end
--===========================================================================
function InitTrig_PotreblenieTrain()
    gg_trg_PotreblenieTrain=CreateTrigger()
    DisableTrigger(gg_trg_PotreblenieTrain)
    TriggerRegisterAnyUnitEventBJ(gg_trg_PotreblenieTrain, EVENT_PLAYER_UNIT_TRAIN_FINISH)
    TriggerAddCondition(gg_trg_PotreblenieTrain, Condition(Trig_PotreblenieTrain_Conditions))
    TriggerAddAction(gg_trg_PotreblenieTrain, Trig_PotreblenieTrain_Actions)
end
--===========================================================================
-- Trigger: BracResearch
--===========================================================================
function Trig_BracResearch_Conditions()
    return GetResearched() == FourCC('R05W')
end
function Trig_BracResearch_Func001C()
    return GetPlayerTechCountSimple(FourCC('R05W'), GetOwningPlayer(GetTriggerUnit())) == 6
end
function Trig_BracResearch_Func002002()
    return GetUnitAbilityLevelSwapped(FourCC('A0A6'), GetFilterUnit()) ~= 0
end
function Trig_BracResearch_Func005A()
    SetUnitAbilityLevelSwapped(FourCC('A0A6'), GetEnumUnit(), GetPlayerTechCountSimple(FourCC('R05W'), GetOwningPlayer(GetTriggerUnit())))
end
function Trig_BracResearch_Actions()
    if Trig_BracResearch_Func001C() then
        SetPlayerAbilityAvailableBJ(false, FourCC('A0A6'), GetOwningPlayer(GetTriggerUnit()))
        return
    end
    udg_Boolexpr = Trig_BracResearch_Func002002
    GroupEnumUnitsOfPlayer(udg_LocalOtrad2, udg_LocalPlayer, udg_Boolexpr)
    ForGroupBJ(udg_LocalOtrad2, Trig_BracResearch_Func005A)
    GroupClear(udg_LocalOtrad2)
end
--===========================================================================
function InitTrig_BracResearch()
    gg_trg_BracResearch=CreateTrigger()
    DisableTrigger(gg_trg_BracResearch)
    TriggerRegisterAnyUnitEventBJ(gg_trg_BracResearch, EVENT_PLAYER_UNIT_RESEARCH_FINISH)
    TriggerAddCondition(gg_trg_BracResearch, Condition(Trig_BracResearch_Conditions))
    TriggerAddAction(gg_trg_BracResearch, Trig_BracResearch_Actions)
end
--===========================================================================
-- Trigger: BracTrain
--===========================================================================
function Trig_BracTrain_Conditions()
    return GetUnitAbilityLevelSwapped(FourCC('A0A6'), GetTriggerUnit()) >= 1
end
function Trig_BracTrain_Actions()
    SetUnitAbilityLevelSwapped(FourCC('A0A6'), GetEnumUnit(), GetPlayerTechCountSimple(FourCC('R05W'), GetOwningPlayer(GetTriggerUnit())))
end
--===========================================================================
function InitTrig_BracTrain()
    gg_trg_BracTrain=CreateTrigger()
    DisableTrigger(gg_trg_BracTrain)
    TriggerRegisterAnyUnitEventBJ(gg_trg_BracTrain, EVENT_PLAYER_UNIT_TRAIN_FINISH)
    TriggerAddCondition(gg_trg_BracTrain, Condition(Trig_BracTrain_Conditions))
    TriggerAddAction(gg_trg_BracTrain, Trig_BracTrain_Actions)
end
--===========================================================================
-- Trigger: PodjogResearch
--===========================================================================
function Trig_PodjogResearch_Conditions()
    return GetResearched() == FourCC('R04R')
end
function Trig_PodjogResearch_Func001C()
    return GetPlayerTechCountSimple(FourCC('R04R'), GetOwningPlayer(GetTriggerUnit())) == 6
end
function Trig_PodjogResearch_Func002002()
    return GetUnitAbilityLevelSwapped(FourCC('A0AR'), GetFilterUnit()) ~= 0
end
function Trig_PodjogResearch_Func005A()
    SetUnitAbilityLevelSwapped(FourCC('A0AR'), GetEnumUnit(), GetPlayerTechCountSimple(FourCC('R04R'), GetOwningPlayer(GetTriggerUnit())))
end
function Trig_PodjogResearch_Actions()
    if Trig_PodjogResearch_Func001C() then
        SetPlayerAbilityAvailableBJ(false, FourCC('A0AR'), GetOwningPlayer(GetTriggerUnit()))
        return
    end
    udg_Boolexpr = Trig_PodjogResearch_Func002002
    GroupEnumUnitsOfPlayer(udg_LocalOtrad2, udg_LocalPlayer, udg_Boolexpr)
    ForGroupBJ(udg_LocalOtrad2, Trig_PodjogResearch_Func005A)
    GroupClear(udg_LocalOtrad2)
end
--===========================================================================
function InitTrig_PodjogResearch()
    gg_trg_PodjogResearch=CreateTrigger()
    DisableTrigger(gg_trg_PodjogResearch)
    TriggerRegisterAnyUnitEventBJ(gg_trg_PodjogResearch, EVENT_PLAYER_UNIT_RESEARCH_FINISH)
    TriggerAddCondition(gg_trg_PodjogResearch, Condition(Trig_PodjogResearch_Conditions))
    TriggerAddAction(gg_trg_PodjogResearch, Trig_PodjogResearch_Actions)
end
--===========================================================================
-- Trigger: PodjogTrain
--===========================================================================
function Trig_PodjogTrain_Conditions()
    return GetUnitAbilityLevelSwapped(FourCC('A0AR'), GetTrainedUnit()) >= 1
end
function Trig_PodjogTrain_Actions()
    SetUnitAbilityLevelSwapped(FourCC('A0AR'), GetTrainedUnit(), GetPlayerTechCountSimple(FourCC('R04R'), GetOwningPlayer(GetTriggerUnit())))
end
--===========================================================================
function InitTrig_PodjogTrain()
    gg_trg_PodjogTrain=CreateTrigger()
    DisableTrigger(gg_trg_PodjogTrain)
    TriggerRegisterAnyUnitEventBJ(gg_trg_PodjogTrain, EVENT_PLAYER_UNIT_TRAIN_FINISH)
    TriggerAddCondition(gg_trg_PodjogTrain, Condition(Trig_PodjogTrain_Conditions))
    TriggerAddAction(gg_trg_PodjogTrain, Trig_PodjogTrain_Actions)
end
--===========================================================================
-- Trigger: PodruvResearc
--===========================================================================
function Trig_PodruvResearc_Conditions()
    return GetResearched() == FourCC('R04Q')
end
function Trig_PodruvResearc_Func001C()
    return GetPlayerTechCountSimple(FourCC('R04Q'), GetOwningPlayer(GetTriggerUnit())) == 6
end
function Trig_PodruvResearc_Func002002()
    return GetUnitAbilityLevelSwapped(FourCC('A0A9'), GetFilterUnit()) ~= 0
end
function Trig_PodruvResearc_Func005A()
    SetUnitAbilityLevelSwapped(FourCC('A0A9'), GetEnumUnit(), GetPlayerTechCountSimple(FourCC('R04Q'), GetOwningPlayer(GetTriggerUnit())) + 1)
end
function Trig_PodruvResearc_Actions()
    if Trig_PodruvResearc_Func001C() then
        SetPlayerAbilityAvailableBJ(false, FourCC('A0A9'), GetOwningPlayer(GetTriggerUnit()))
        return
    end
    udg_Boolexpr = Trig_PodruvResearc_Func002002
    GroupEnumUnitsOfPlayer(udg_LocalOtrad2, udg_LocalPlayer, udg_Boolexpr)
    ForGroupBJ(udg_LocalOtrad2, Trig_PodruvResearc_Func005A)
    GroupClear(udg_LocalOtrad2)
end
--===========================================================================
function InitTrig_PodruvResearc()
    gg_trg_PodruvResearc=CreateTrigger()
    DisableTrigger(gg_trg_PodruvResearc)
    TriggerRegisterAnyUnitEventBJ(gg_trg_PodruvResearc, EVENT_PLAYER_UNIT_RESEARCH_FINISH)
    TriggerAddCondition(gg_trg_PodruvResearc, Condition(Trig_PodruvResearc_Conditions))
    TriggerAddAction(gg_trg_PodruvResearc, Trig_PodruvResearc_Actions)
end
--===========================================================================
-- Trigger: PodruvTrain
--===========================================================================
function Trig_PodruvTrain_Conditions()
    return GetUnitAbilityLevelSwapped(FourCC('A0A9'), GetTrainedUnit()) >= 1
end
function Trig_PodruvTrain_Actions()
    SetUnitAbilityLevelSwapped(FourCC('A0A9'), GetTrainedUnit(), GetPlayerTechCountSimple(FourCC('R04Q'), GetOwningPlayer(GetTriggerUnit())))
end
--===========================================================================
function InitTrig_PodruvTrain()
    gg_trg_PodruvTrain=CreateTrigger()
    DisableTrigger(gg_trg_PodruvTrain)
    TriggerRegisterAnyUnitEventBJ(gg_trg_PodruvTrain, EVENT_PLAYER_UNIT_TRAIN_FINISH)
    TriggerAddCondition(gg_trg_PodruvTrain, Condition(Trig_PodruvTrain_Conditions))
    TriggerAddAction(gg_trg_PodruvTrain, Trig_PodruvTrain_Actions)
end
--===========================================================================
-- Trigger: Brac
--===========================================================================
function Trig_Brac_Conditions()
    return GetUnitAbilityLevel(GetTriggerUnit(), FourCC('B028')) > 0 and GetUnitAbilityLevel(GetEventDamageSource(), FourCC('A0A6')) > 0
end
function Trig_Brac_Actions()
    local t
    CreateTextTagUnitBJ("TRIGSTR_7336", GetEventDamageSource(), - 20.00, 5.00, 100, 100, 100, 0.00)
    t=GetLastCreatedTextTag()
    SetTextTagPermanentBJ(t, false)
    SetTextTagLifespanBJ(t, 2.00)
    SetTextTagFadepointBJ(t, 2.00)
    SetTextTagVelocityBJ(t, 75.00, 90)
    RemoveTextTagTimed(t , 2.1)
    t=nil
end
--===========================================================================
function InitTrig_Brac()
    gg_trg_Brac=CreateTrigger()
    DisableTrigger(gg_trg_Brac)
    TriggerRegisterAnyUnitEventBJ(gg_trg_Brac, EVENT_PLAYER_UNIT_DAMAGED)
    TriggerAddCondition(gg_trg_Brac, Condition(Trig_Brac_Conditions))
    TriggerAddAction(gg_trg_Brac, Trig_Brac_Actions)
end
--===========================================================================
-- Trigger: Samopodruv
--===========================================================================
function Trig_Samopodruv_Conditions()
    return GetUnitAbilityLevel(GetAttacker(), FourCC('A0A9')) > 0
end
function Trig_Samopodruv_Actions()
    local t
    if GetRandomInt(1, 100) < 35 + ( - 5 * GetUnitAbilityLevel(GetAttacker(), FourCC('A0A9')) ) then
        SetUnitLifeBJ(GetAttacker(), GetUnitStateSwap(UNIT_STATE_LIFE, GetAttacker()) - 15.00)
        CreateTextTagUnitBJ("TRIGSTR_433", GetAttacker(), - 20.00, 5.00, 100, 100, 100, 0.00)
        t=GetLastCreatedTextTag()
        SetTextTagPermanentBJ(t, false)
        SetTextTagLifespanBJ(t, 2.00)
        SetTextTagFadepointBJ(t, 2.00)
        SetTextTagVelocityBJ(t, 75.00, 90)
        RemoveTextTagTimed(t , 2.1)
    end
    t=nil
end
--===========================================================================
function InitTrig_Samopodruv()
    gg_trg_Samopodruv=CreateTrigger()
    DisableTrigger(gg_trg_Samopodruv)
    TriggerRegisterAnyUnitEventBJ(gg_trg_Samopodruv, EVENT_PLAYER_UNIT_ATTACKED)
    TriggerAddCondition(gg_trg_Samopodruv, Condition(Trig_Samopodruv_Conditions))
    TriggerAddAction(gg_trg_Samopodruv, Trig_Samopodruv_Actions)
end
--===========================================================================
-- Trigger: Samopodjog
--===========================================================================
function Trig_Samopodjog_Conditions()
     return GetUnitAbilityLevel(GetAttacker(), FourCC('A0AR')) > 0
end
function Trig_Samopodjog_Actions()
    local t
    if GetRandomInt(1, 100) < 35 + ( - 5 * GetUnitAbilityLevel(GetAttacker(), FourCC('A0AR')) ) then
        SetUnitLifeBJ(GetAttacker(), GetUnitStateSwap(UNIT_STATE_LIFE, GetAttacker()) - 15.00)
        CreateTextTagUnitBJ("TRIGSTR_433", GetAttacker(), - 20.00, 5.00, 100, 100, 100, 0.00)
        t=GetLastCreatedTextTag()
        SetTextTagPermanentBJ(t, false)
        SetTextTagLifespanBJ(t, 2.00)
        SetTextTagFadepointBJ(t, 2.00)
        SetTextTagVelocityBJ(t, 75.00, 90)
        RemoveTextTagTimed(t , 2.1)
    end
    t=nil
end
--===========================================================================
function InitTrig_Samopodjog()
    gg_trg_Samopodjog=CreateTrigger()
    DisableTrigger(gg_trg_Samopodjog)
    TriggerRegisterAnyUnitEventBJ(gg_trg_Samopodjog, EVENT_PLAYER_UNIT_ATTACKED)
    TriggerAddCondition(gg_trg_Samopodjog, Condition(Trig_Samopodjog_Conditions))
    TriggerAddAction(gg_trg_Samopodjog, Trig_Samopodjog_Actions)
end
--===========================================================================
-- Trigger: Adrenalin
--===========================================================================
function Trig_Adrenalin_Actions()
    SetUnitLifePercentBJ(GetTriggerUnit(), GetUnitLifePercent(GetTriggerUnit()) - 15.00)
end
--===========================================================================
function InitTrig_Adrenalin()
    gg_trg_Adrenalin=CreateTrigger()
    DisableTrigger(gg_trg_Adrenalin)
    TriggerRegisterAnyUnitEventBJ(gg_trg_Adrenalin, EVENT_PLAYER_UNIT_SPELL_EFFECT)
    TriggerAddAction(gg_trg_Adrenalin, function()
        if GetSpellAbilityId() ~= FourCC('A0D2') then return end
        Trig_Adrenalin_Actions()
    end)
end
--===========================================================================
-- Trigger: GazloySpellheals
--===========================================================================
function Trig_GazloySpellheals_Conditions()
    
    return GetUnitAbilityLevel(GetEventDamageSource(), FourCC('A1KK')) > 0 and IsPlayerEnemy(GetOwningPlayer(GetEventDamageSource()), GetOwningPlayer(GetTriggerUnit()))
    
    
    
end
function Trig_GazloySpellheals_Actions()
    local u= GetEventDamageSource()
    local level= GetUnitAbilityLevel(u, FourCC('A1KK'))
    local damage= GetEventDamage()
    local e= AddSpecialEffectTargetUnitBJ("Chest", u, "AbilitiesSpellsItemsVampiricPotionVampPotionCaster.mdl")
    SetUnitState(u, UNIT_STATE_LIFE, GetUnitState(u, UNIT_STATE_LIFE) + damage * ( 0.01 * level ))
  
    
    u=nil
    DestroyEffect(e)
    e=nil
end
--===========================================================================
function InitTrig_GazloySpellheals()
    gg_trg_GazloySpellheals=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_GazloySpellheals, EVENT_PLAYER_UNIT_DAMAGED)
    TriggerAddCondition(gg_trg_GazloySpellheals, Condition(Trig_GazloySpellheals_Conditions))
    TriggerAddAction(gg_trg_GazloySpellheals, Trig_GazloySpellheals_Actions)
end
--===========================================================================
-- Trigger: FarmBuildG
--===========================================================================
function Gtiers()
    local phash= Gfarm
    local puhash= Gtier
    PData[pi] = PData[pi] or {}
    local count= PData[pi][phash] or 0
    local u= PData[pi][puhash]
    local id= GetUnitTypeId(u)
   
    if count < 6 then
        KillUnit(u)
    elseif count < 12 then
        KillUnit(u)
        u=CreateUnit(Player(pi), FourCC('h001'), 0, 0, 0.0)
    else
        KillUnit(u)
        u=CreateUnit(Player(pi), FourCC('h0P6'), 0, 0, 0.0)
    end
    PData[pi][puhash] = u
    u=nil
end
function Trig_FarmBuildG_Conditions()
    gUnit=GetTriggerUnit()
    gInt=GetUnitTypeId(gUnit)
    gPi=GetPlayerId(GetOwningPlayer(gUnit))
    return gInt == FourCC('h076') -- Lab
end
function Trig_FarmBuildG_Actions()
    ChangeObjectsCount(gPi , Gfarm , 1)
    Gtiers(gPi)
end
--===========================================================================
function InitTrig_FarmBuildG()
    gg_trg_FarmBuildG=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_FarmBuildG, EVENT_PLAYER_UNIT_CONSTRUCT_FINISH)
    TriggerAddCondition(gg_trg_FarmBuildG, Condition(Trig_FarmBuildG_Conditions))
    TriggerAddAction(gg_trg_FarmBuildG, Trig_FarmBuildG_Actions)
end
--===========================================================================
-- Trigger: FarmLoseG
--===========================================================================
function Trig_FarmLoseG_Conditions()
    gUnit=GetTriggerUnit()
    gInt=GetUnitTypeId(gUnit)
    gPi=GetPlayerId(GetOwningPlayer(gUnit))
    return gInt == FourCC('h076') -- Lab
end
function Trig_FarmLoseG_Actions()
    ChangeObjectsCount(gPi , Gfarm , - 1)
    Gtiers(gPi)
end
--===========================================================================
function InitTrig_FarmLoseG()
    gg_trg_FarmLoseG=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_FarmLoseG, EVENT_PLAYER_UNIT_DEATH)
    TriggerAddCondition(gg_trg_FarmLoseG, Condition(Trig_FarmLoseG_Conditions))
    TriggerAddAction(gg_trg_FarmLoseG, Trig_FarmLoseG_Actions)
end
--===========================================================================
-- Trigger: Pulimetchik
--===========================================================================
function Trig_Pulimetchik_Func002C()
    return (( ( GetResearched() == FourCC('R04E') ) )) or (( ( GetResearched() == FourCC('R04K') ) ))
end
function Trig_Pulimetchik_Func003C()
    return (( GetPlayerTechCountSimple(FourCC('R04E'), GetOwningPlayer(GetTriggerUnit())) >= 2 )) and (( GetPlayerTechCountSimple(FourCC('R04K'), GetOwningPlayer(GetTriggerUnit())) >= 2 ))
end
function Trig_Pulimetchik_Conditions()
    return (Trig_Pulimetchik_Func002C()) and (Trig_Pulimetchik_Func003C())
end
function Trig_Pulimetchik_Actions()
    SetPlayerTechMaxAllowedSwap(FourCC('h06L'), - 1, GetOwningPlayer(GetTriggerUnit()))
end
--===========================================================================
function InitTrig_Pulimetchik()
    gg_trg_Pulimetchik=CreateTrigger()
    DisableTrigger(gg_trg_Pulimetchik)
    TriggerRegisterAnyUnitEventBJ(gg_trg_Pulimetchik, EVENT_PLAYER_UNIT_RESEARCH_FINISH)
    TriggerAddCondition(gg_trg_Pulimetchik, Condition(Trig_Pulimetchik_Conditions))
    TriggerAddAction(gg_trg_Pulimetchik, Trig_Pulimetchik_Actions)
end
--===========================================================================
-- Trigger: Ognemetchik
--===========================================================================
function Trig_Ognemetchik_Func002C()
    return (( ( GetResearched() == FourCC('R04G') ) )) or (( ( GetResearched() == FourCC('R04K') ) ))
end
function Trig_Ognemetchik_Func003C()
    return (( GetPlayerTechCountSimple(FourCC('R04G'), GetOwningPlayer(GetTriggerUnit())) >= 2 )) and (( GetPlayerTechCountSimple(FourCC('R04K'), GetOwningPlayer(GetTriggerUnit())) >= 2 ))
end
function Trig_Ognemetchik_Conditions()
    return (Trig_Ognemetchik_Func002C()) and (Trig_Ognemetchik_Func003C())
end
function Trig_Ognemetchik_Actions()
    SetPlayerTechMaxAllowedSwap(FourCC('h06Q'), - 1, GetOwningPlayer(GetTriggerUnit()))
end
--===========================================================================
function InitTrig_Ognemetchik()
    gg_trg_Ognemetchik=CreateTrigger()
    DisableTrigger(gg_trg_Ognemetchik)
    TriggerRegisterAnyUnitEventBJ(gg_trg_Ognemetchik, EVENT_PLAYER_UNIT_RESEARCH_FINISH)
    TriggerAddCondition(gg_trg_Ognemetchik, Condition(Trig_Ognemetchik_Conditions))
    TriggerAddAction(gg_trg_Ognemetchik, Trig_Ognemetchik_Actions)
end
--===========================================================================
-- Trigger: Raketchik
--===========================================================================
function Trig_Raketchik_Func002C()
    return (( ( GetResearched() == FourCC('R04F') ) )) or (( ( GetResearched() == FourCC('R04K') ) ))
end
function Trig_Raketchik_Func003C()
    return (( GetPlayerTechCountSimple(FourCC('R04F'), GetOwningPlayer(GetTriggerUnit())) >= 2 )) and (( GetPlayerTechCountSimple(FourCC('R04K'), GetOwningPlayer(GetTriggerUnit())) >= 2 ))
end
function Trig_Raketchik_Conditions()
    return (Trig_Raketchik_Func002C()) and (Trig_Raketchik_Func003C())
end
function Trig_Raketchik_Actions()
    SetPlayerTechMaxAllowedSwap(FourCC('h06N'), - 1, GetOwningPlayer(GetTriggerUnit()))
end
--===========================================================================
function InitTrig_Raketchik()
    gg_trg_Raketchik=CreateTrigger()
    DisableTrigger(gg_trg_Raketchik)
    TriggerRegisterAnyUnitEventBJ(gg_trg_Raketchik, EVENT_PLAYER_UNIT_RESEARCH_FINISH)
    TriggerAddCondition(gg_trg_Raketchik, Condition(Trig_Raketchik_Conditions))
    TriggerAddAction(gg_trg_Raketchik, Trig_Raketchik_Actions)
end
--===========================================================================
-- Trigger: Medic
--===========================================================================
function Trig_Medic_Func002C()
    return (( ( GetResearched() == FourCC('R04P') ) )) or (( ( GetResearched() == FourCC('R04K') ) ))
end
function Trig_Medic_Func003C()
    return (( GetPlayerTechCountSimple(FourCC('R04P'), GetOwningPlayer(GetTriggerUnit())) >= 2 )) and (( GetPlayerTechCountSimple(FourCC('R04K'), GetOwningPlayer(GetTriggerUnit())) >= 2 ))
end
function Trig_Medic_Conditions()
    return (Trig_Medic_Func002C()) and (Trig_Medic_Func003C())
end
function Trig_Medic_Actions()
    SetPlayerTechMaxAllowedSwap(FourCC('h06O'), - 1, GetOwningPlayer(GetTriggerUnit()))
end
--===========================================================================
function InitTrig_Medic()
    gg_trg_Medic=CreateTrigger()
    DisableTrigger(gg_trg_Medic)
    TriggerRegisterAnyUnitEventBJ(gg_trg_Medic, EVENT_PLAYER_UNIT_RESEARCH_FINISH)
    TriggerAddCondition(gg_trg_Medic, Condition(Trig_Medic_Conditions))
    TriggerAddAction(gg_trg_Medic, Trig_Medic_Actions)
end
--===========================================================================
-- Trigger: Sniper
--===========================================================================
function Trig_Sniper_Func002C()
    return (( ( GetResearched() == FourCC('R04M') ) )) or (( ( GetResearched() == FourCC('R04E') ) )) or (( ( GetResearched() == FourCC('R04K') ) ))
end
function Trig_Sniper_Func003C()
    return (( GetPlayerTechCountSimple(FourCC('R04E'), GetOwningPlayer(GetTriggerUnit())) >= 3 )) and (( GetPlayerTechCountSimple(FourCC('R04M'), GetOwningPlayer(GetTriggerUnit())) >= 2 )) and (( GetPlayerTechCountSimple(FourCC('R04K'), GetOwningPlayer(GetTriggerUnit())) >= 2 ))
end
function Trig_Sniper_Conditions()
    return (Trig_Sniper_Func002C()) and (Trig_Sniper_Func003C())
end
function Trig_Sniper_Actions()
    SetPlayerTechMaxAllowedSwap(FourCC('h06M'), - 1, GetOwningPlayer(GetTriggerUnit()))
end
--===========================================================================
function InitTrig_Sniper()
    gg_trg_Sniper=CreateTrigger()
    DisableTrigger(gg_trg_Sniper)
    TriggerRegisterAnyUnitEventBJ(gg_trg_Sniper, EVENT_PLAYER_UNIT_RESEARCH_FINISH)
    TriggerAddCondition(gg_trg_Sniper, Condition(Trig_Sniper_Conditions))
    TriggerAddAction(gg_trg_Sniper, Trig_Sniper_Actions)
end
--===========================================================================
-- Trigger: Saper
--===========================================================================
function Trig_Saper_Func002C()
    return (( ( GetResearched() == FourCC('R04F') ) )) or (( ( GetResearched() == FourCC('R04K') ) ))
end
function Trig_Saper_Func003C()
    return (( GetPlayerTechCountSimple(FourCC('R04F'), GetOwningPlayer(GetTriggerUnit())) >= 3 )) and (( GetPlayerTechCountSimple(FourCC('R04K'), GetOwningPlayer(GetTriggerUnit())) >= 2 ))
end
function Trig_Saper_Conditions()
    return (Trig_Saper_Func002C()) and (Trig_Saper_Func003C())
end
function Trig_Saper_Actions()
    SetPlayerTechMaxAllowedSwap(FourCC('h078'), - 1, GetOwningPlayer(GetTriggerUnit()))
end
--===========================================================================
function InitTrig_Saper()
    gg_trg_Saper=CreateTrigger()
    DisableTrigger(gg_trg_Saper)
    TriggerRegisterAnyUnitEventBJ(gg_trg_Saper, EVENT_PLAYER_UNIT_RESEARCH_FINISH)
    TriggerAddCondition(gg_trg_Saper, Condition(Trig_Saper_Conditions))
    TriggerAddAction(gg_trg_Saper, Trig_Saper_Actions)
end
--===========================================================================
-- Trigger: Car
--===========================================================================
function Trig_Car_Func002C()
    return (( ( GetResearched() == FourCC('R04F') ) )) or (( ( GetResearched() == FourCC('R04L') ) )) or (( ( GetResearched() == FourCC('R04I') ) ))
end
function Trig_Car_Func003C()
    return (( GetPlayerTechCountSimple(FourCC('R04F'), GetOwningPlayer(GetTriggerUnit())) >= 2 )) and (( GetPlayerTechCountSimple(FourCC('R04L'), GetOwningPlayer(GetTriggerUnit())) >= 1 )) and (( GetPlayerTechCountSimple(FourCC('R04I'), GetOwningPlayer(GetTriggerUnit())) >= 1 ))
end
function Trig_Car_Conditions()
    return (Trig_Car_Func002C()) and (Trig_Car_Func003C())
end
function Trig_Car_Actions()
    SetPlayerTechMaxAllowedSwap(FourCC('h06R'), - 1, GetOwningPlayer(GetTriggerUnit()))
end
--===========================================================================
function InitTrig_Car()
    gg_trg_Car=CreateTrigger()
    DisableTrigger(gg_trg_Car)
    TriggerRegisterAnyUnitEventBJ(gg_trg_Car, EVENT_PLAYER_UNIT_RESEARCH_FINISH)
    TriggerAddCondition(gg_trg_Car, Condition(Trig_Car_Conditions))
    TriggerAddAction(gg_trg_Car, Trig_Car_Actions)
end
--===========================================================================
-- Trigger: Vezdehod
--===========================================================================
function Trig_Vezdehod_Func002C()
    return (( ( GetResearched() == FourCC('R04E') ) )) or (( ( GetResearched() == FourCC('R04L') ) )) or (( ( GetResearched() == FourCC('R04I') ) ))
end
function Trig_Vezdehod_Func003C()
    return (( GetPlayerTechCountSimple(FourCC('R04E'), GetOwningPlayer(GetTriggerUnit())) >= 2 )) and (( GetPlayerTechCountSimple(FourCC('R04L'), GetOwningPlayer(GetTriggerUnit())) >= 1 )) and (( GetPlayerTechCountSimple(FourCC('R04I'), GetOwningPlayer(GetTriggerUnit())) >= 1 ))
end
function Trig_Vezdehod_Conditions()
    return (Trig_Vezdehod_Func002C()) and (Trig_Vezdehod_Func003C())
end
function Trig_Vezdehod_Actions()
    SetPlayerTechMaxAllowedSwap(FourCC('h06U'), - 1, GetOwningPlayer(GetTriggerUnit()))
end
--===========================================================================
function InitTrig_Vezdehod()
    gg_trg_Vezdehod=CreateTrigger()
    DisableTrigger(gg_trg_Vezdehod)
    TriggerRegisterAnyUnitEventBJ(gg_trg_Vezdehod, EVENT_PLAYER_UNIT_RESEARCH_FINISH)
    TriggerAddCondition(gg_trg_Vezdehod, Condition(Trig_Vezdehod_Conditions))
    TriggerAddAction(gg_trg_Vezdehod, Trig_Vezdehod_Actions)
end
--===========================================================================
-- Trigger: Tank
--===========================================================================
function Trig_Tank_Func002C()
    return (( ( GetResearched() == FourCC('R04F') ) )) or (( ( GetResearched() == FourCC('R04L') ) )) or (( ( GetResearched() == FourCC('R04I') ) ))
end
function Trig_Tank_Func003C()
    return (( GetPlayerTechCountSimple(FourCC('R04F'), GetOwningPlayer(GetTriggerUnit())) >= 2 )) and (( GetPlayerTechCountSimple(FourCC('R04L'), GetOwningPlayer(GetTriggerUnit())) >= 2 )) and (( GetPlayerTechCountSimple(FourCC('R04I'), GetOwningPlayer(GetTriggerUnit())) >= 2 ))
end
function Trig_Tank_Conditions()
    return (Trig_Tank_Func002C()) and (Trig_Tank_Func003C())
end
function Trig_Tank_Actions()
    SetPlayerTechMaxAllowedSwap(FourCC('h06T'), - 1, GetOwningPlayer(GetTriggerUnit()))
end
--===========================================================================
function InitTrig_Tank()
    gg_trg_Tank=CreateTrigger()
    DisableTrigger(gg_trg_Tank)
    TriggerRegisterAnyUnitEventBJ(gg_trg_Tank, EVENT_PLAYER_UNIT_RESEARCH_FINISH)
    TriggerAddCondition(gg_trg_Tank, Condition(Trig_Tank_Conditions))
    TriggerAddAction(gg_trg_Tank, Trig_Tank_Actions)
end
--===========================================================================
-- Trigger: FireTank
--===========================================================================
function Trig_FireTank_Func002C()
    return (( ( GetResearched() == FourCC('R04G') ) )) or (( ( GetResearched() == FourCC('R04L') ) ))
end
function Trig_FireTank_Func003C()
    return (( GetPlayerTechCountSimple(FourCC('R04G'), GetOwningPlayer(GetTriggerUnit())) >= 2 )) and (( GetPlayerTechCountSimple(FourCC('R04L'), GetOwningPlayer(GetTriggerUnit())) >= 2 )) and (( GetPlayerTechCountSimple(FourCC('R04I'), GetOwningPlayer(GetTriggerUnit())) >= 2 ))
end
function Trig_FireTank_Conditions()
    return (Trig_FireTank_Func002C()) and (Trig_FireTank_Func003C())
end
function Trig_FireTank_Actions()
    SetPlayerTechMaxAllowedSwap(FourCC('h06S'), - 1, GetOwningPlayer(GetTriggerUnit()))
end
--===========================================================================
function InitTrig_FireTank()
    gg_trg_FireTank=CreateTrigger()
    DisableTrigger(gg_trg_FireTank)
    TriggerRegisterAnyUnitEventBJ(gg_trg_FireTank, EVENT_PLAYER_UNIT_RESEARCH_FINISH)
    TriggerAddCondition(gg_trg_FireTank, Condition(Trig_FireTank_Conditions))
    TriggerAddAction(gg_trg_FireTank, Trig_FireTank_Actions)
end
--===========================================================================
-- Trigger: Arta
--===========================================================================
function Trig_Arta_Func002C()
    return (( ( GetResearched() == FourCC('R04F') ) )) or (( ( GetResearched() == FourCC('R04M') ) )) or (( ( GetResearched() == FourCC('R04L') ) ))
end
function Trig_Arta_Func003C()
    return (( GetPlayerTechCountSimple(FourCC('R04F'), GetOwningPlayer(GetTriggerUnit())) >= 2 )) and (( GetPlayerTechCountSimple(FourCC('R04L'), GetOwningPlayer(GetTriggerUnit())) >= 1 )) and (( GetPlayerTechCountSimple(FourCC('R04M'), GetOwningPlayer(GetTriggerUnit())) >= 2 )) and (( GetPlayerTechCountSimple(FourCC('R04I'), GetOwningPlayer(GetTriggerUnit())) >= 1 ))
end
function Trig_Arta_Conditions()
    return (Trig_Arta_Func002C()) and (Trig_Arta_Func003C())
end
function Trig_Arta_Actions()
    SetPlayerTechMaxAllowedSwap(FourCC('h06Y'), - 1, GetOwningPlayer(GetTriggerUnit()))
end
--===========================================================================
function InitTrig_Arta()
    gg_trg_Arta=CreateTrigger()
    DisableTrigger(gg_trg_Arta)
    TriggerRegisterAnyUnitEventBJ(gg_trg_Arta, EVENT_PLAYER_UNIT_RESEARCH_FINISH)
    TriggerAddCondition(gg_trg_Arta, Condition(Trig_Arta_Conditions))
    TriggerAddAction(gg_trg_Arta, Trig_Arta_Actions)
end
--===========================================================================
-- Trigger: Meha
--===========================================================================
function Trig_Meha_Func002C()
    return (( ( GetResearched() == FourCC('R04H') ) )) or (( ( GetResearched() == FourCC('R04L') ) )) or (( ( GetResearched() == FourCC('R04J') ) ))
end
function Trig_Meha_Func003C()
    return (( GetPlayerTechCountSimple(FourCC('R04H'), GetOwningPlayer(GetTriggerUnit())) >= 2 )) and (( GetPlayerTechCountSimple(FourCC('R04L'), GetOwningPlayer(GetTriggerUnit())) >= 1 )) and (( GetPlayerTechCountSimple(FourCC('R04J'), GetOwningPlayer(GetTriggerUnit())) >= 1 ))
end
function Trig_Meha_Conditions()
    return (Trig_Meha_Func002C()) and (Trig_Meha_Func003C())
end
function Trig_Meha_Actions()
    SetPlayerTechMaxAllowedSwap(FourCC('o00W'), - 1, GetOwningPlayer(GetTriggerUnit()))
end
--===========================================================================
function InitTrig_Meha()
    gg_trg_Meha=CreateTrigger()
    DisableTrigger(gg_trg_Meha)
    TriggerRegisterAnyUnitEventBJ(gg_trg_Meha, EVENT_PLAYER_UNIT_RESEARCH_FINISH)
    TriggerAddCondition(gg_trg_Meha, Condition(Trig_Meha_Conditions))
    TriggerAddAction(gg_trg_Meha, Trig_Meha_Actions)
end
--===========================================================================
-- Trigger: OgneMeha
--===========================================================================
function Trig_OgneMeha_Func002C()
    return (( ( GetResearched() == FourCC('R04G') ) )) or (( ( GetResearched() == FourCC('R04L') ) )) or (( ( GetResearched() == FourCC('R04J') ) ))
end
function Trig_OgneMeha_Func003C()
    return (( GetPlayerTechCountSimple(FourCC('R04G'), GetOwningPlayer(GetTriggerUnit())) >= 2 )) and (( GetPlayerTechCountSimple(FourCC('R04L'), GetOwningPlayer(GetTriggerUnit())) >= 2 )) and (( GetPlayerTechCountSimple(FourCC('R04J'), GetOwningPlayer(GetTriggerUnit())) >= 1 ))
end
function Trig_OgneMeha_Conditions()
    return (Trig_OgneMeha_Func002C()) and (Trig_OgneMeha_Func003C())
end
function Trig_OgneMeha_Actions()
    SetPlayerTechMaxAllowedSwap(FourCC('o00X'), - 1, GetOwningPlayer(GetTriggerUnit()))
end
--===========================================================================
function InitTrig_OgneMeha()
    gg_trg_OgneMeha=CreateTrigger()
    DisableTrigger(gg_trg_OgneMeha)
    TriggerRegisterAnyUnitEventBJ(gg_trg_OgneMeha, EVENT_PLAYER_UNIT_RESEARCH_FINISH)
    TriggerAddCondition(gg_trg_OgneMeha, Condition(Trig_OgneMeha_Conditions))
    TriggerAddAction(gg_trg_OgneMeha, Trig_OgneMeha_Actions)
end
--===========================================================================
-- Trigger: Eczo
--===========================================================================
function Trig_Eczo_Func002C()
    return (( ( GetResearched() == FourCC('R04H') ) )) or (( ( GetResearched() == FourCC('R04L') ) )) or (( ( GetResearched() == FourCC('R04J') ) ))
end
function Trig_Eczo_Func003C()
    return (( GetPlayerTechCountSimple(FourCC('R04H'), GetOwningPlayer(GetTriggerUnit())) >= 1 )) and (( GetPlayerTechCountSimple(FourCC('R04L'), GetOwningPlayer(GetTriggerUnit())) >= 1 )) and (( GetPlayerTechCountSimple(FourCC('R04J'), GetOwningPlayer(GetTriggerUnit())) >= 1 ))
end
function Trig_Eczo_Conditions()
    return (Trig_Eczo_Func002C()) and (Trig_Eczo_Func003C())
end
function Trig_Eczo_Actions()
    SetPlayerTechMaxAllowedSwap(FourCC('o00Y'), - 1, GetOwningPlayer(GetTriggerUnit()))
end
--===========================================================================
function InitTrig_Eczo()
    gg_trg_Eczo=CreateTrigger()
    DisableTrigger(gg_trg_Eczo)
    TriggerRegisterAnyUnitEventBJ(gg_trg_Eczo, EVENT_PLAYER_UNIT_RESEARCH_FINISH)
    TriggerAddCondition(gg_trg_Eczo, Condition(Trig_Eczo_Conditions))
    TriggerAddAction(gg_trg_Eczo, Trig_Eczo_Actions)
end
--===========================================================================
-- Trigger: Super
--===========================================================================
function Trig_Super_Func002C()
    return (( ( GetResearched() == FourCC('R04E') ) )) or (( ( GetResearched() == FourCC('R04L') ) )) or (( ( GetResearched() == FourCC('R04J') ) )) or (( ( GetResearched() == FourCC('R04P') ) ))
end
function Trig_Super_Func003C()
    return (( GetPlayerTechCountSimple(FourCC('R04P'), GetOwningPlayer(GetTriggerUnit())) >= 2 )) and (( GetPlayerTechCountSimple(FourCC('R04L'), GetOwningPlayer(GetTriggerUnit())) >= 1 )) and (( GetPlayerTechCountSimple(FourCC('R04J'), GetOwningPlayer(GetTriggerUnit())) >= 1 )) and (( GetPlayerTechCountSimple(FourCC('R04E'), GetOwningPlayer(GetTriggerUnit())) >= 2 ))
end
function Trig_Super_Conditions()
    return (Trig_Super_Func002C()) and (Trig_Super_Func003C())
end
function Trig_Super_Actions()
    SetPlayerTechMaxAllowedSwap(FourCC('h06P'), - 1, GetOwningPlayer(GetTriggerUnit()))
end
--===========================================================================
function InitTrig_Super()
    gg_trg_Super=CreateTrigger()
    DisableTrigger(gg_trg_Super)
    TriggerRegisterAnyUnitEventBJ(gg_trg_Super, EVENT_PLAYER_UNIT_RESEARCH_FINISH)
    TriggerAddCondition(gg_trg_Super, Condition(Trig_Super_Conditions))
    TriggerAddAction(gg_trg_Super, Trig_Super_Actions)
end
--===========================================================================
-- Trigger: Submarina
--===========================================================================
function Trig_Submarina_Func002C()
    return (( ( GetResearched() == FourCC('R04F') ) )) or (( ( GetResearched() == FourCC('R04L') ) )) or (( ( GetResearched() == FourCC('R04I') ) ))
end
function Trig_Submarina_Func003C()
    return (( GetPlayerTechCountSimple(FourCC('R04F'), GetOwningPlayer(GetTriggerUnit())) >= 1 )) and (( GetPlayerTechCountSimple(FourCC('R04L'), GetOwningPlayer(GetTriggerUnit())) >= 1 )) and (( GetPlayerTechCountSimple(FourCC('R04I'), GetOwningPlayer(GetTriggerUnit())) >= 1 ))
end
function Trig_Submarina_Conditions()
    return (Trig_Submarina_Func002C()) and (Trig_Submarina_Func003C())
end
function Trig_Submarina_Actions()
    SetPlayerTechMaxAllowedSwap(FourCC('h06V'), - 1, GetOwningPlayer(GetTriggerUnit()))
end
--===========================================================================
function InitTrig_Submarina()
    gg_trg_Submarina=CreateTrigger()
    DisableTrigger(gg_trg_Submarina)
    TriggerRegisterAnyUnitEventBJ(gg_trg_Submarina, EVENT_PLAYER_UNIT_RESEARCH_FINISH)
    TriggerAddCondition(gg_trg_Submarina, Condition(Trig_Submarina_Conditions))
    TriggerAddAction(gg_trg_Submarina, Trig_Submarina_Actions)
end
--===========================================================================
-- Trigger: Podlodka1
--===========================================================================
function Trig_Podlodka1_Func002C()
    return (( ( GetResearched() == FourCC('R04F') ) )) or (( ( GetResearched() == FourCC('R04L') ) )) or (( ( GetResearched() == FourCC('R04I') ) ))
end
function Trig_Podlodka1_Func003C()
    return (( GetPlayerTechCountSimple(FourCC('R04L'), GetOwningPlayer(GetTriggerUnit())) >= 2 )) and (( GetPlayerTechCountSimple(FourCC('R04I'), GetOwningPlayer(GetTriggerUnit())) >= 2 )) and (( GetPlayerTechCountSimple(FourCC('R04F'), GetOwningPlayer(GetTriggerUnit())) >= 2 ))
end
function Trig_Podlodka1_Conditions()
    return (Trig_Podlodka1_Func002C()) and (Trig_Podlodka1_Func003C())
end
function Trig_Podlodka1_Actions()
    SetPlayerTechMaxAllowedSwap(FourCC('h06W'), - 1, GetOwningPlayer(GetTriggerUnit()))
end
--===========================================================================
function InitTrig_Podlodka1()
    gg_trg_Podlodka1=CreateTrigger()
    DisableTrigger(gg_trg_Podlodka1)
    TriggerRegisterAnyUnitEventBJ(gg_trg_Podlodka1, EVENT_PLAYER_UNIT_RESEARCH_FINISH)
    TriggerAddCondition(gg_trg_Podlodka1, Condition(Trig_Podlodka1_Conditions))
    TriggerAddAction(gg_trg_Podlodka1, Trig_Podlodka1_Actions)
end