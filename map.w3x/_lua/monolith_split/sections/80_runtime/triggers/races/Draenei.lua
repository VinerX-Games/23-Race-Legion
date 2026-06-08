
--===========================================================================
-- Trigger: Draenei Build Abill
--===========================================================================
function Trig_Draenei_Build_Abill_Conditions()
    return GetUnitAbilityLevel(GetConstructingStructure(), FourCC('A0Z3')) > 0
end
function Trig_Draenei_Build_Abill_Actions()
    local u= GetConstructingStructure()
    --call BJDebugMsg("2")
    if Random(1 , 2) and GetPlayerTechCount(GetOwningPlayer(u), FourCC('R0EB'), true) > 0 then
        TriggerSleepAction(0)
        SetBuildingProgressTimed(u , 20 , 0)
        --call BJDebugMsg("3")
    end
    UnitRemoveAbility(u, FourCC('A0Z3'))
    u=nil
end
--===========================================================================
function InitTrig_Draenei_Build_Abill()
    gg_trg_Draenei_Build_Abill=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_Draenei_Build_Abill, EVENT_PLAYER_UNIT_CONSTRUCT_START)
    TriggerAddCondition(gg_trg_Draenei_Build_Abill, Condition(Trig_Draenei_Build_Abill_Conditions))
    TriggerAddAction(gg_trg_Draenei_Build_Abill, Trig_Draenei_Build_Abill_Actions)
end
--===========================================================================
-- Trigger: flot1
--===========================================================================
function Trig_flot1_Conditions()
    return GetResearched() == FourCC('R027')
end
function Trig_flot1_Actions()
    SetPlayerTechMaxAllowedSwap(FourCC('R02S'), 0, GetOwningPlayer(GetTriggerUnit()))
end
--===========================================================================
function InitTrig_flot1()
    gg_trg_flot1=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_flot1, EVENT_PLAYER_UNIT_RESEARCH_FINISH)
    TriggerRegisterAnyUnitEventBJ(gg_trg_flot1, EVENT_PLAYER_UNIT_RESEARCH_START)
    TriggerAddCondition(gg_trg_flot1, Condition(Trig_flot1_Conditions))
    TriggerAddAction(gg_trg_flot1, Trig_flot1_Actions)
end
--===========================================================================
-- Trigger: flot2
--===========================================================================
function Trig_flot2_Conditions()
    return GetResearched() == FourCC('R027')
end
function Trig_flot2_Actions()
    SetPlayerTechMaxAllowedSwap(FourCC('R02S'), 1, GetOwningPlayer(GetTriggerUnit()))
end
--===========================================================================
function InitTrig_flot2()
    gg_trg_flot2=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_flot2, EVENT_PLAYER_UNIT_RESEARCH_CANCEL)
    TriggerAddCondition(gg_trg_flot2, Condition(Trig_flot2_Conditions))
    TriggerAddAction(gg_trg_flot2, Trig_flot2_Actions)
end
--===========================================================================
-- Trigger: arm1
--===========================================================================
function Trig_arm1_Conditions()
    return GetResearched() == FourCC('R02S')
end
function Trig_arm1_Actions()
    SetPlayerTechMaxAllowedSwap(FourCC('R027'), 0, GetOwningPlayer(GetTriggerUnit()))
end
--===========================================================================
function InitTrig_arm1()
    gg_trg_arm1=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_arm1, EVENT_PLAYER_UNIT_RESEARCH_FINISH)
    TriggerRegisterAnyUnitEventBJ(gg_trg_arm1, EVENT_PLAYER_UNIT_RESEARCH_START)
    TriggerAddCondition(gg_trg_arm1, Condition(Trig_arm1_Conditions))
    TriggerAddAction(gg_trg_arm1, Trig_arm1_Actions)
end
--===========================================================================
-- Trigger: arm2
--===========================================================================
function Trig_arm2_Conditions()
    return GetResearched() == FourCC('R02S')
end
function Trig_arm2_Actions()
    SetPlayerTechMaxAllowedSwap(FourCC('R027'), 1, GetOwningPlayer(GetTriggerUnit()))
end
--===========================================================================
function InitTrig_arm2()
    gg_trg_arm2=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_arm2, EVENT_PLAYER_UNIT_RESEARCH_CANCEL)
    TriggerAddCondition(gg_trg_arm2, Condition(Trig_arm2_Conditions))
    TriggerAddAction(gg_trg_arm2, Trig_arm2_Actions)
end
--===========================================================================
-- Trigger: Auto pohichenie Copy
--===========================================================================
function Trig_Auto_pohichenie_Copy_Actions()
    IssueTargetOrderBJ(GetTriggerUnit(), "banish", GetSpellTargetUnit())
end
--===========================================================================
function InitTrig_Auto_pohichenie_Copy()
    gg_trg_Auto_pohichenie_Copy=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_Auto_pohichenie_Copy, EVENT_PLAYER_UNIT_SPELL_EFFECT)
    TriggerAddAction(gg_trg_Auto_pohichenie_Copy, function()
        if GetSpellAbilityId() ~= FourCC('A031') then return end
        Trig_Auto_pohichenie_Copy_Actions()
    end)
end