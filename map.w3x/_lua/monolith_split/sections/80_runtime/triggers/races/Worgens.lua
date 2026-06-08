
--===========================================================================
-- Trigger: StartWorgens
--===========================================================================
function Trig_StartWorgens_Func001A()
    SetPlayerTechMaxAllowedSwap(FourCC('H0J2'), 1, GetEnumPlayer())
    SetPlayerTechMaxAllowedSwap(FourCC('H0J6'), 1, GetEnumPlayer())
    SetPlayerTechMaxAllowedSwap(FourCC('H0J7'), 1, GetEnumPlayer())
    SetPlayerTechMaxAllowedSwap(FourCC('H0J8'), 1, GetEnumPlayer())
end
function Trig_StartWorgens_Actions()
    ForForce(udg_AllPlayers, Trig_StartWorgens_Func001A)
end
--===========================================================================
function InitTrig_StartWorgens()
    gg_trg_StartWorgens=CreateTrigger()
    TriggerRegisterTimerEventSingle(gg_trg_StartWorgens, 0.01)
    TriggerAddAction(gg_trg_StartWorgens, Trig_StartWorgens_Actions)
end
--===========================================================================
-- Trigger: LegGer
--===========================================================================
function Trig_LegGer_Actions()
    local u= GetTriggerUnit()
    
    
    if GetUnitAbilityLevelSwapped(FourCC('A11U'), GetTriggerUnit()) == 1 then
        UnitAddAbilityBJ(FourCC('A11V'), u)
        RemoveAbilityTimed(u , FourCC('A11V') , 15)
    
    elseif GetUnitAbilityLevelSwapped(FourCC('A11U'), GetTriggerUnit()) == 2 then
        UnitAddAbilityBJ(FourCC('A11W'), u)
        RemoveAbilityTimed(u , FourCC('A11W') , 15)
    
    elseif GetUnitAbilityLevelSwapped(FourCC('A11U'), GetTriggerUnit()) == 3 then
        UnitAddAbilityBJ(FourCC('A11X'), u)
        RemoveAbilityTimed(u , FourCC('A11X') , 15)
    
    elseif GetUnitAbilityLevelSwapped(FourCC('A11U'), GetTriggerUnit()) == 4 then
        UnitAddAbilityBJ(FourCC('A11Y'), u)
        RemoveAbilityTimed(u , FourCC('A11Y') , 15)
      
    end
    u=nil
end
--===========================================================================
function InitTrig_LegGer()
    gg_trg_LegGer=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_LegGer, EVENT_PLAYER_UNIT_SPELL_EFFECT)
    TriggerAddAction(gg_trg_LegGer, function()
        if GetSpellAbilityId() ~= FourCC('A11U') then return end
        Trig_LegGer_Actions()
    end)
end
--===========================================================================
-- Trigger: SpellOpletenie
--===========================================================================
function Trig_SpellOpletenie_Actions()
   -- call BJDebugMsg("")
    MassSpell(GetTriggerUnit() , GetSpellAbilityId() , FourCC('A1MA') , "firebolt" , nil , 600 , 1 , false)
end
--===========================================================================
function InitTrig_SpellOpletenie()
    gg_trg_SpellOpletenie=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_SpellOpletenie, EVENT_PLAYER_UNIT_SPELL_EFFECT)
    TriggerAddAction(gg_trg_SpellOpletenie, function()
        if GetSpellAbilityId() ~= FourCC('A1M9') then return end
        Trig_SpellOpletenie_Actions()
    end)
end
--===========================================================================
-- Trigger: flot1 Copy O
--===========================================================================
function Trig_flot1_Copy_O_Conditions()
    return GetResearched() == FourCC('R073')
end
function Trig_flot1_Copy_O_Actions()
    SetPlayerTechMaxAllowedSwap(FourCC('R072'), 0, GetOwningPlayer(GetTriggerUnit()))
end
--===========================================================================
function InitTrig_flot1_Copy_O()
    gg_trg_flot1_Copy_O=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_flot1_Copy_O, EVENT_PLAYER_UNIT_RESEARCH_FINISH)
    TriggerRegisterAnyUnitEventBJ(gg_trg_flot1_Copy_O, EVENT_PLAYER_UNIT_RESEARCH_START)
    TriggerAddCondition(gg_trg_flot1_Copy_O, Condition(Trig_flot1_Copy_O_Conditions))
    TriggerAddAction(gg_trg_flot1_Copy_O, Trig_flot1_Copy_O_Actions)
end
--===========================================================================
-- Trigger: flot2 Copy O
--===========================================================================
function Trig_flot2_Copy_O_Conditions()
    return GetResearched() == FourCC('R073')
end
function Trig_flot2_Copy_O_Actions()
    SetPlayerTechMaxAllowedSwap(FourCC('R072'), 1, GetOwningPlayer(GetTriggerUnit()))
end
--===========================================================================
function InitTrig_flot2_Copy_O()
    gg_trg_flot2_Copy_O=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_flot2_Copy_O, EVENT_PLAYER_UNIT_RESEARCH_CANCEL)
    TriggerAddCondition(gg_trg_flot2_Copy_O, Condition(Trig_flot2_Copy_O_Conditions))
    TriggerAddAction(gg_trg_flot2_Copy_O, Trig_flot2_Copy_O_Actions)
end
--===========================================================================
-- Trigger: arm1 Copy O
--===========================================================================
function Trig_arm1_Copy_O_Conditions()
    return GetResearched() == FourCC('R072')
end
function Trig_arm1_Copy_O_Actions()
    SetPlayerTechMaxAllowedSwap(FourCC('R073'), 0, GetOwningPlayer(GetTriggerUnit()))
end
--===========================================================================
function InitTrig_arm1_Copy_O()
    gg_trg_arm1_Copy_O=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_arm1_Copy_O, EVENT_PLAYER_UNIT_RESEARCH_FINISH)
    TriggerRegisterAnyUnitEventBJ(gg_trg_arm1_Copy_O, EVENT_PLAYER_UNIT_RESEARCH_START)
    TriggerAddCondition(gg_trg_arm1_Copy_O, Condition(Trig_arm1_Copy_O_Conditions))
    TriggerAddAction(gg_trg_arm1_Copy_O, Trig_arm1_Copy_O_Actions)
end
--===========================================================================
-- Trigger: arm2 Copy O
--===========================================================================
function Trig_arm2_Copy_O_Conditions()
    return GetResearched() == FourCC('R072')
end
function Trig_arm2_Copy_O_Actions()
    SetPlayerTechMaxAllowedSwap(FourCC('R073'), 1, GetOwningPlayer(GetTriggerUnit()))
end
--===========================================================================
function InitTrig_arm2_Copy_O()
    gg_trg_arm2_Copy_O=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_arm2_Copy_O, EVENT_PLAYER_UNIT_RESEARCH_CANCEL)
    TriggerAddCondition(gg_trg_arm2_Copy_O, Condition(Trig_arm2_Copy_O_Conditions))
    TriggerAddAction(gg_trg_arm2_Copy_O, Trig_arm2_Copy_O_Actions)
end
--===========================================================================
-- Trigger: BuidAltar
--===========================================================================
function Trig_BuidAltar_Conditions()
    return GetUnitTypeId(GetTriggerUnit()) == FourCC('h0CV')
end
function Trig_BuidAltar_Actions()
    UnitAddAbilityBJ(FourCC('Asud'), GetTriggerUnit())
    AddUnitToStockBJ(FourCC('h07A'), GetTriggerUnit(), 1, 1)
end
--===========================================================================
function InitTrig_BuidAltar()
    gg_trg_BuidAltar=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_BuidAltar, EVENT_PLAYER_UNIT_UPGRADE_FINISH)
    TriggerAddCondition(gg_trg_BuidAltar, Condition(Trig_BuidAltar_Conditions))
    TriggerAddAction(gg_trg_BuidAltar, Trig_BuidAltar_Actions)
end
--===========================================================================
-- Trigger: Auto set Copy O
--===========================================================================
function Trig_Auto_set_Copy_O_Actions()
    IssueTargetOrderBJ(GetTriggerUnit(), "ensnare", GetSpellTargetUnit())
end
--===========================================================================
function InitTrig_Auto_set_Copy_O()
    gg_trg_Auto_set_Copy_O=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_Auto_set_Copy_O, EVENT_PLAYER_UNIT_SPELL_EFFECT)
    TriggerAddAction(gg_trg_Auto_set_Copy_O, function()
        if GetSpellAbilityId() ~= FourCC('A09U') then return end
        Trig_Auto_set_Copy_O_Actions()
    end)
end
--===========================================================================
-- Trigger: AutocastSlowOn
--===========================================================================
function Trig_AutocastSlowOn_Conditions()
    return GetResearched() == FourCC('R04S') and GetPlayerTechCount(GetOwningPlayer(GetTriggerUnit()), FourCC('R04S'), true) == 2
end
function Trig_AutocastSlowOn_Actions()
    GlobalIssue(FourCC('A09S') , GetOwningPlayer(GetTriggerUnit()) , "slowon")
end
--===========================================================================
function InitTrig_AutocastSlowOn()
    gg_trg_AutocastSlowOn=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_AutocastSlowOn, EVENT_PLAYER_UNIT_RESEARCH_FINISH)
    TriggerAddCondition(gg_trg_AutocastSlowOn, Condition(Trig_AutocastSlowOn_Conditions))
    TriggerAddAction(gg_trg_AutocastSlowOn, Trig_AutocastSlowOn_Actions)
end