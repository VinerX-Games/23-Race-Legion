
--===========================================================================
-- Trigger: StromgardOn
--===========================================================================
function Trig_StromgardOn_Actions()
    EnableTrigger(gg_trg_PaladinTank)
    EnableTrigger(gg_trg_PaladinVozdoyn)
    EnableTrigger(gg_trg_PaladinHeal)
    
    EnableTrigger(gg_trg_Tank1)
    EnableTrigger(gg_trg_Heal1)
    EnableTrigger(gg_trg_Vozdoyanie1)
    EnableTrigger(gg_trg_Tank2)
    EnableTrigger(gg_trg_Heal2)
    EnableTrigger(gg_trg_Vozdoyanie2)
    EnableTrigger(gg_trg_Priziv)
    EnableTrigger(gg_trg_Priziv2)
    EnableTrigger(gg_trg_Proffesian)
    EnableTrigger(gg_trg_Professian2)
    EnableTrigger(gg_trg_MassArmy)
    EnableTrigger(gg_trg_UpSystem)
    EnableTrigger(gg_trg_MassArmy)
    EnableTrigger(gg_trg_ShieldUp)
    EnableTrigger(gg_trg_MassArmy)
    
    
    
    
end
--===========================================================================
function InitTrig_StromgardOn()
    gg_trg_StromgardOn=CreateTrigger()
    TriggerAddAction(gg_trg_StromgardOn, Trig_StromgardOn_Actions)
end
--===========================================================================
-- Trigger: Priziv2
--===========================================================================
function Trig_Priziv2_Conditions()
    return GetResearched() == FourCC('R0D6')
end
function Trig_Priziv2_Actions()
    SetPlayerTechMaxAllowedSwap(FourCC('R0D5'), 1, GetOwningPlayer(GetTriggerUnit()))
end
--===========================================================================
function InitTrig_Priziv2()
    gg_trg_Priziv2=CreateTrigger()
    DisableTrigger(gg_trg_Priziv2)
    TriggerRegisterAnyUnitEventBJ(gg_trg_Priziv2, EVENT_PLAYER_UNIT_RESEARCH_CANCEL)
    TriggerAddCondition(gg_trg_Priziv2, Condition(Trig_Priziv2_Conditions))
    TriggerAddAction(gg_trg_Priziv2, Trig_Priziv2_Actions)
end
--===========================================================================
-- Trigger: Priziv
--===========================================================================
function Trig_Priziv_Conditions()
    return GetResearched() == FourCC('R0D6')
end
function Trig_Priziv_Actions()
    SetPlayerTechMaxAllowedSwap(FourCC('R0D5'), 0, GetOwningPlayer(GetTriggerUnit()))
end
--===========================================================================
function InitTrig_Priziv()
    gg_trg_Priziv=CreateTrigger()
    DisableTrigger(gg_trg_Priziv)
    TriggerRegisterAnyUnitEventBJ(gg_trg_Priziv, EVENT_PLAYER_UNIT_RESEARCH_FINISH)
    TriggerRegisterAnyUnitEventBJ(gg_trg_Priziv, EVENT_PLAYER_UNIT_RESEARCH_START)
    TriggerAddCondition(gg_trg_Priziv, Condition(Trig_Priziv_Conditions))
    TriggerAddAction(gg_trg_Priziv, Trig_Priziv_Actions)
end
--===========================================================================
-- Trigger: Professian2
--===========================================================================
function Trig_Professian2_Conditions()
    return GetResearched() == FourCC('R0D5')
end
function Trig_Professian2_Actions()
    SetPlayerTechMaxAllowedSwap(FourCC('R0D6'), 1, GetOwningPlayer(GetTriggerUnit()))
end
--===========================================================================
function InitTrig_Professian2()
    gg_trg_Professian2=CreateTrigger()
    DisableTrigger(gg_trg_Professian2)
    TriggerRegisterAnyUnitEventBJ(gg_trg_Professian2, EVENT_PLAYER_UNIT_RESEARCH_CANCEL)
    TriggerAddCondition(gg_trg_Professian2, Condition(Trig_Professian2_Conditions))
    TriggerAddAction(gg_trg_Professian2, Trig_Professian2_Actions)
end
--===========================================================================
-- Trigger: Proffesian
--===========================================================================
function Trig_Proffesian_Conditions()
    return GetResearched() == FourCC('R0D5')
end
function Trig_Proffesian_Actions()
    SetPlayerTechMaxAllowedSwap(FourCC('R0D6'), 0, GetOwningPlayer(GetTriggerUnit()))
end
--===========================================================================
function InitTrig_Proffesian()
    gg_trg_Proffesian=CreateTrigger()
    DisableTrigger(gg_trg_Proffesian)
    TriggerRegisterAnyUnitEventBJ(gg_trg_Proffesian, EVENT_PLAYER_UNIT_RESEARCH_FINISH)
    TriggerRegisterAnyUnitEventBJ(gg_trg_Proffesian, EVENT_PLAYER_UNIT_RESEARCH_START)
    TriggerAddCondition(gg_trg_Proffesian, Condition(Trig_Proffesian_Conditions))
    TriggerAddAction(gg_trg_Proffesian, Trig_Proffesian_Actions)
end
--===========================================================================
-- Trigger: MassArmy
--===========================================================================
function Trig_MassArmy_Conditions()
    local id=GetUnitTypeId(GetTrainedUnit())
    return GetPlayerTechCountSimple(FourCC('R0D6'), GetOwningPlayer(GetTriggerUnit())) == 1 and ( id == FourCC('h0GS') or id == FourCC('h0GV') or id == FourCC('h0GU') or id == FourCC('h0GW') or id == FourCC('h0GX') or id == FourCC('h0L3') )
end
function Trig_MassArmy_Actions()
    local l= GetUnitLoc(GetTriggerUnit())
    local u=  CreateUnitAtLoc(GetOwningPlayer(GetTriggerUnit()), GetUnitTypeId(GetTrainedUnit()), l, bj_UNIT_FACING)
    RemoveLocation(l)
    l=GetUnitRallyPoint(GetTriggerUnit())
    IssuePointOrderLoc(GetTrainedUnit(), "move", l)
    IssuePointOrderLoc(u, "move", l)
    RemoveLocation(l)
    l=nil
    u=nil
end
--===========================================================================
function InitTrig_MassArmy()
    gg_trg_MassArmy=CreateTrigger()
    DisableTrigger(gg_trg_MassArmy)
    TriggerRegisterAnyUnitEventBJ(gg_trg_MassArmy, EVENT_PLAYER_UNIT_TRAIN_FINISH)
    TriggerAddCondition(gg_trg_MassArmy, Condition(Trig_MassArmy_Conditions))
    TriggerAddAction(gg_trg_MassArmy, Trig_MassArmy_Actions)
end
--===========================================================================
-- Trigger: UpSystem
--===========================================================================
function Trig_UpSystem_Conditions()
    return GetUnitAbilityLevelSwapped(FourCC('A0VI'), GetKillingUnitBJ()) >= 1
end
function Trig_UpSystem_Func001C()
    return GetUnitAbilityLevelSwapped(FourCC('A0VI'), GetKillingUnitBJ()) >= 2
end
function Trig_UpSystem_Actions()
    if Trig_UpSystem_Func001C() then
        local u = GetKillingUnitBJ()
        local pi = GetPlayerId(GetOwningPlayer(u))
        aiFixTrainBefore(u, pi)
        ReplaceUnit(u , FourCC('h0HE') , bj_UNIT_STATE_METHOD_RELATIVE)
        aiFixTrainAfter(GetLastReplacedUnitBJ(), pi)
        udg_LocalUnit2 = GetLastReplacedUnitBJ()
    else
        IncUnitAbilityLevelSwapped(FourCC('A0VI'), GetKillingUnitBJ())
    end
end
--===========================================================================
function InitTrig_UpSystem()
    gg_trg_UpSystem=CreateTrigger()
    DisableTrigger(gg_trg_UpSystem)
    TriggerRegisterAnyUnitEventBJ(gg_trg_UpSystem, EVENT_PLAYER_UNIT_DEATH)
    TriggerAddCondition(gg_trg_UpSystem, Condition(Trig_UpSystem_Conditions))
    TriggerAddAction(gg_trg_UpSystem, Trig_UpSystem_Actions)
end
--===========================================================================
-- Trigger: ShieldUp
--===========================================================================
function Trig_ShieldUp_Func001C()
    return GetUnitAbilityLevelSwapped(FourCC('A0WI'), GetTriggerUnit()) == 1
end
function Trig_ShieldUp_Actions()
    if Trig_ShieldUp_Func001C() then
        UnitRemoveAbilityBJ(FourCC('A0WI'), GetTriggerUnit())
    else
        UnitAddAbilityBJ(FourCC('A0WI'), GetTriggerUnit())
    end
end
--===========================================================================
function InitTrig_ShieldUp()
    gg_trg_ShieldUp=CreateTrigger()
    DisableTrigger(gg_trg_ShieldUp)
    TriggerRegisterAnyUnitEventBJ(gg_trg_ShieldUp, EVENT_PLAYER_UNIT_SPELL_EFFECT)
    TriggerAddAction(gg_trg_ShieldUp, function()
        if GetSpellAbilityId() ~= FourCC('A0WG') then return end
        Trig_ShieldUp_Actions()
    end)
end
--===========================================================================
-- Trigger: EnterKazna
--===========================================================================
function Trig_EnterKazna_Conditions()
    return GetLearnedSkill() == FourCC('A0XV')
end
function Trig_EnterKazna_Actions()
    local pi= GetPlayerId(GetOwningPlayer(GetTriggerUnit()))
    income[pi]=income[pi] + ( 100 + GetUnitAbilityLevel(GetTriggerUnit(), FourCC('A0XV')) * 100 )
    -- ??????????? ????? ? ??????? ????? ?????????
end
--===========================================================================
function InitTrig_EnterKazna()
    gg_trg_EnterKazna=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_EnterKazna, EVENT_PLAYER_HERO_SKILL)
    TriggerAddCondition(gg_trg_EnterKazna, Condition(Trig_EnterKazna_Conditions))
    TriggerAddAction(gg_trg_EnterKazna, Trig_EnterKazna_Actions)
end
--===========================================================================
-- Trigger: ChillBonus
--===========================================================================
function Trig_ChillBonus_Conditions()
    return GetUnitAbilityLevel(GetKillingUnit(), FourCC('A1R3')) > 0 and GetUnitAbilityLevel(GetKillingUnit(), FourCC('A1R5')) == 0
end
function Trig_ChillBonus_Actions()
        UnitAddAbility(GetKillingUnit(), FourCC('A1R5'))
        RemoveAbilityTimed(GetKillingUnit() , FourCC('A1R5') , 9)
end
--===========================================================================
function InitTrig_ChillBonus()
    gg_trg_ChillBonus=CreateTrigger()
    --call DisableTrigger( gg_trg_ChillBonus )
    TriggerRegisterAnyUnitEventBJ(gg_trg_ChillBonus, EVENT_PLAYER_UNIT_DEATH)
    TriggerAddCondition(gg_trg_ChillBonus, Condition(Trig_ChillBonus_Conditions))
    TriggerAddAction(gg_trg_ChillBonus, Trig_ChillBonus_Actions)
end
--===========================================================================
-- Trigger: Passive
--===========================================================================
function Trig_Passive_Conditions()
    return GetLearnedSkillBJ() == FourCC('A1CJ')
end
function Trig_Passive_Actions()
    UnitAddAbilityBJ(FourCC('A1CI'), GetTriggerUnit())
    SetUnitAbilityLevelSwapped(FourCC('A1CI'), GetTriggerUnit(), GetUnitAbilityLevelSwapped(FourCC('A1CJ'), GetTriggerUnit()))
    UnitAddAbilityBJ(FourCC('A1CH'), GetTriggerUnit())
    SetUnitAbilityLevelSwapped(FourCC('A1CH'), GetTriggerUnit(), GetUnitAbilityLevelSwapped(FourCC('A1CJ'), GetTriggerUnit()))
end
--===========================================================================
function InitTrig_Passive()
    gg_trg_Passive=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_Passive, EVENT_PLAYER_HERO_SKILL)
    TriggerAddCondition(gg_trg_Passive, Condition(Trig_Passive_Conditions))
    TriggerAddAction(gg_trg_Passive, Trig_Passive_Actions)
end