
--===========================================================================
-- Trigger: Blood1 Copy 3
--===========================================================================
function Trig_Blood1_Copy_3_Conditions()
    return GetResearched() == FourCC('R08H')
end
function Trig_Blood1_Copy_3_Actions()
    SetPlayerTechMaxAllowedSwap(FourCC('n026'), 0, GetOwningPlayer(GetTriggerUnit()))
    SetPlayerTechMaxAllowed(GetOwningPlayer(GetTriggerUnit()), FourCC('n02D'), - 1)
end
--===========================================================================
function InitTrig_Blood1_Copy_3()
    gg_trg_Blood1_Copy_3=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_Blood1_Copy_3, EVENT_PLAYER_UNIT_RESEARCH_FINISH)
    TriggerAddCondition(gg_trg_Blood1_Copy_3, Condition(Trig_Blood1_Copy_3_Conditions))
    TriggerAddAction(gg_trg_Blood1_Copy_3, Trig_Blood1_Copy_3_Actions)
end
--===========================================================================
-- Trigger: Blood Copy
--===========================================================================
function Trig_Blood_Copy_Conditions()
    return GetResearched() == FourCC('R004')
end
function Trig_Blood_Copy_Actions()
    SetPlayerTechMaxAllowedSwap(FourCC('n025'), 0, GetOwningPlayer(GetTriggerUnit()))
    SetPlayerTechMaxAllowed(GetOwningPlayer(GetTriggerUnit()), FourCC('n026'), - 1) --???????? ?????
end
--===========================================================================
function InitTrig_Blood_Copy()
    gg_trg_Blood_Copy=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_Blood_Copy, EVENT_PLAYER_UNIT_RESEARCH_FINISH)
    TriggerAddCondition(gg_trg_Blood_Copy, Condition(Trig_Blood_Copy_Conditions))
    TriggerAddAction(gg_trg_Blood_Copy, Trig_Blood_Copy_Actions)
end
--===========================================================================
-- Trigger: Blood2 Copy
--===========================================================================
function Trig_Blood2_Copy_Conditions()
    return GetResearched() == FourCC('R08I')
end
function Trig_Blood2_Copy_Actions()
    SetPlayerTechMaxAllowedSwap(FourCC('n02D'), 0, GetOwningPlayer(GetTriggerUnit()))
    SetPlayerTechMaxAllowed(GetOwningPlayer(GetTriggerUnit()), FourCC('n02E'), - 1)
end
--===========================================================================
function InitTrig_Blood2_Copy()
    gg_trg_Blood2_Copy=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_Blood2_Copy, EVENT_PLAYER_UNIT_RESEARCH_FINISH)
    TriggerAddCondition(gg_trg_Blood2_Copy, Condition(Trig_Blood2_Copy_Conditions))
    TriggerAddAction(gg_trg_Blood2_Copy, Trig_Blood2_Copy_Actions)
end
--===========================================================================
-- Trigger: ?????????? ??????? 001 Copy 5
--===========================================================================
function Trig_____________________________________001_Copy_5_Actions()
    UnitRemoveAbilityBJ(FourCC('A0N7'), GetTriggerUnit())
    UnitAddAbilityBJ(FourCC('A0N8'), GetTriggerUnit())
    TriggerSleepAction(20.00)
    UnitRemoveAbilityBJ(FourCC('A0N8'), GetTriggerUnit())
    UnitAddAbilityBJ(FourCC('A0N7'), GetTriggerUnit())
end
--===========================================================================
function InitTrig_____________________________________001_Copy_5()
    gg_trg_____________________________________001_Copy_5=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_____________________________________001_Copy_5, EVENT_PLAYER_UNIT_SPELL_EFFECT)
    TriggerAddAction(gg_trg_____________________________________001_Copy_5, function()
        if GetSpellAbilityId() ~= FourCC('A0N6') then return end
        Trig_____________________________________001_Copy_5_Actions()
    end)
end
--===========================================================================
-- Trigger: ?????????? ??????? 001 Copy 2 Copy 3
--===========================================================================
function Trig_____________________________________001_Copy_2_Copy_3_Actions()
    UnitAddAbilityBJ(FourCC('A0NC'), GetTriggerUnit())
    TriggerSleepAction(25.00)
    UnitRemoveAbilityBJ(FourCC('A0NC'), GetTriggerUnit())
end
--===========================================================================
function InitTrig_____________________________________001_Copy_2_Copy_3()
    gg_trg_____________________________________001_Copy_2_Copy_3=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_____________________________________001_Copy_2_Copy_3, EVENT_PLAYER_UNIT_SPELL_EFFECT)
    TriggerAddAction(gg_trg_____________________________________001_Copy_2_Copy_3, function()
        if GetSpellAbilityId() ~= FourCC('A0NB') then return end
        Trig_____________________________________001_Copy_2_Copy_3_Actions()
    end)
end
--===========================================================================
-- Trigger: ArhiTep
--===========================================================================
function Trig_ArhiTep_Func001C()
    return (( ( GetUnitTypeId(GetTrainedUnit()) == FourCC('N02G') ) )) or (( ( GetUnitTypeId(GetTrainedUnit()) == FourCC('N02B') ) ))
end
function Trig_ArhiTep_Conditions()
    return Trig_ArhiTep_Func001C()
end
function Trig_ArhiTep_Actions()
    udg_LocalPosition2=GetRectCenter(gg_rct_ArhiTep)
    SetUnitPositionLoc(GetTriggerUnit(), udg_LocalPosition2)
    RemoveLocation(udg_LocalPosition2)
end
--===========================================================================
function InitTrig_ArhiTep()
    gg_trg_ArhiTep=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_ArhiTep, EVENT_PLAYER_UNIT_TRAIN_FINISH)
    TriggerAddCondition(gg_trg_ArhiTep, Condition(Trig_ArhiTep_Conditions))
    TriggerAddAction(gg_trg_ArhiTep, Trig_ArhiTep_Actions)
end
--===========================================================================
-- Trigger: Summon dummy del
--===========================================================================
function Trig_Summon_dummy_del_Conditions()
    return GetUnitTypeId(GetTriggerUnit()) == FourCC('u018')
end
function Trig_Summon_dummy_del_Actions()
    RemoveUnit(GetSummonedUnit())
end
--===========================================================================
function InitTrig_Summon_dummy_del()
    gg_trg_Summon_dummy_del=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_Summon_dummy_del, EVENT_PLAYER_UNIT_SUMMON)
    TriggerAddCondition(gg_trg_Summon_dummy_del, Condition(Trig_Summon_dummy_del_Conditions))
    TriggerAddAction(gg_trg_Summon_dummy_del, Trig_Summon_dummy_del_Actions)
end
--===========================================================================
-- Trigger: Buildings
--===========================================================================
function Trig_Buildings_Func010C()
    return GetSpellAbilityId() == FourCC('AUin')
end
function Trig_Buildings_Actions()
    udg_Spell=GetSpellTargetLoc()
    AddSpecialEffectLocBJ(udg_Spell, "UnitsDemonInfernalInfernalBirth.mdl")
    BlzSetSpecialEffectTime(GetLastCreatedEffectBJ(), 0.01)
    TriggerSleepAction(0.70)
    AddSpecialEffectLocBJ(udg_Spell, "AbilitiesSpellsUndeadDarksummoningDarkSummonTarget.mdl")
    BlzSetSpecialEffectScale(GetLastCreatedEffectBJ(), 1.80)
    BlzSetSpecialEffectTime(GetLastCreatedEffectBJ(), 1.00)
    udg_effect=GetLastCreatedEffectBJ()
    TriggerSleepAction(1.00)
    if Trig_Buildings_Func010C() then
        DestroyEffectBJ(udg_effect)
        CreateNUnitsAtLoc(1, FourCC('ndmg'), GetOwningPlayer(GetTriggerUnit()), udg_Spell, bj_UNIT_FACING)
        TriggerSleepAction(0.20)
        AddSpecialEffectLocBJ(udg_Spell, "AbilitiesSpellsHumanFlameStrikeFlameStrikeTarget.mdl")
        udg_effect=GetLastCreatedEffectBJ()
        TriggerSleepAction(0.20)
        DestroyEffectBJ(udg_effect)
    end
end
--===========================================================================
function InitTrig_Buildings()
    gg_trg_Buildings=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_Buildings, EVENT_PLAYER_UNIT_SPELL_CAST)
    TriggerAddAction(gg_trg_Buildings, function()
        if GetSpellAbilityId() ~= FourCC('AUin') then return end
        Trig_Buildings_Actions()
    end)
end
--===========================================================================
-- Trigger: StartBuildingDEmon
--===========================================================================
function Trig_StartBuildingDEmon_Conditions()
    local id= GetUnitTypeId(GetConstructingStructure())
    return id == FourCC('h0DU') or id == FourCC('h0DX') or id == FourCC('h02C') or id == FourCC('h0DZ') or id == FourCC('h0DY') or id == FourCC('h0DS') or id == FourCC('h0DS') or id == FourCC('h0DW') or id == FourCC('h0E1') or id == FourCC('h0E0') or id == FourCC('h0DV') or id == FourCC('h0DT')
end
function Trig_StartBuildingDEmon_Actions()
    local pi= GetPlayerId(GetOwningPlayer(GetTriggerUnit()))
    disincome[pi]=disincome[pi] - 6
    udg_UnitsCount[pi]=udg_UnitsCount[pi] - 1
    UpdateGraf(pi)
    Enter(GetTriggerUnit())
end
--===========================================================================
function InitTrig_StartBuildingDEmon()
    gg_trg_StartBuildingDEmon=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_StartBuildingDEmon, EVENT_PLAYER_UNIT_CONSTRUCT_START)
    TriggerAddCondition(gg_trg_StartBuildingDEmon, Condition(Trig_StartBuildingDEmon_Conditions))
    TriggerAddAction(gg_trg_StartBuildingDEmon, Trig_StartBuildingDEmon_Actions)
end
--===========================================================================
-- Trigger: CanselBuilding Copy
--===========================================================================
function Trig_CanselBuilding_Copy_Conditions()
    local id= GetUnitTypeId(GetTriggerUnit())
    return id == FourCC('h0DU') or id == FourCC('h0DX') or id == FourCC('h02C') or id == FourCC('h0DZ') or id == FourCC('h0DY') or id == FourCC('h0DS') or id == FourCC('h0DS') or id == FourCC('h0DW') or id == FourCC('h0E1') or id == FourCC('h0E0') or id == FourCC('h0DV') or id == FourCC('h0DT')
end
function Trig_CanselBuilding_Copy_Actions()
    local pi= GetPlayerId(GetOwningPlayer(GetTriggerUnit()))
    udg_UnitsCount[pi]=udg_UnitsCount[pi] + 1
    disincome[pi]=disincome[pi] + 6
    UpdateGraf(pi)
    Enter(GetTriggerUnit())
end
--===========================================================================
function InitTrig_CanselBuilding_Copy()
    gg_trg_CanselBuilding_Copy=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_CanselBuilding_Copy, EVENT_PLAYER_UNIT_CONSTRUCT_CANCEL)
    TriggerAddCondition(gg_trg_CanselBuilding_Copy, Condition(Trig_CanselBuilding_Copy_Conditions))
    TriggerAddAction(gg_trg_CanselBuilding_Copy, Trig_CanselBuilding_Copy_Actions)
end
--===========================================================================
-- Trigger: ?????????? ??????? 001 Copy
--===========================================================================
function Trig_____________________________________001_Copy_Conditions()
    return GetUnitAbilityLevelSwapped(FourCC('A0MQ'), GetAttackedUnitBJ()) >= 1
end
function Trig_____________________________________001_Copy_Func004Func001Func001Func001C()
    return GetUnitAbilityLevelSwapped(FourCC('A0NC'), GetAttackedUnitBJ()) == 4
end
function Trig_____________________________________001_Copy_Func004Func001Func001C()
    return GetUnitAbilityLevelSwapped(FourCC('A0NC'), GetAttackedUnitBJ()) == 3
end
function Trig_____________________________________001_Copy_Func004Func001C()
    return GetUnitAbilityLevelSwapped(FourCC('A0NC'), GetAttackedUnitBJ()) == 2
end
function Trig_____________________________________001_Copy_Func004C()
    return GetUnitAbilityLevelSwapped(FourCC('A0NC'), GetAttackedUnitBJ()) == 1
end
function Trig_____________________________________001_Copy_Actions()
    udg_Dm[2]=GetUnitStateSwap(UNIT_STATE_MAX_LIFE, GetAttackedUnitBJ())
    udg_Dm[1]=udg_Dm[2] - GetUnitStateSwap(UNIT_STATE_LIFE, GetAttackedUnitBJ())
    if Trig_____________________________________001_Copy_Func004C() then
        UnitDamageTargetBJ(GetAttackedUnitBJ(), GetAttacker(), udg_Dm[1] * 0.01, ATTACK_TYPE_CHAOS, DAMAGE_TYPE_NORMAL)
    else
        if Trig_____________________________________001_Copy_Func004Func001C() then
            UnitDamageTargetBJ(GetAttackedUnitBJ(), GetAttacker(), udg_Dm[1] * 0.02, ATTACK_TYPE_CHAOS, DAMAGE_TYPE_NORMAL)
        else
            if Trig_____________________________________001_Copy_Func004Func001Func001C() then
                UnitDamageTargetBJ(GetAttackedUnitBJ(), GetAttacker(), udg_Dm[1] * 0.03, ATTACK_TYPE_CHAOS, DAMAGE_TYPE_NORMAL)
            else
                if Trig_____________________________________001_Copy_Func004Func001Func001Func001C() then
                    UnitDamageTargetBJ(GetAttackedUnitBJ(), GetAttacker(), udg_Dm[1] * 0.04, ATTACK_TYPE_CHAOS, DAMAGE_TYPE_NORMAL)
                end
            end
        end
    end
end
--===========================================================================
function InitTrig_____________________________________001_Copy()
    gg_trg_____________________________________001_Copy=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_____________________________________001_Copy, EVENT_PLAYER_UNIT_ATTACKED)
    TriggerAddCondition(gg_trg_____________________________________001_Copy, Condition(Trig_____________________________________001_Copy_Conditions))
    TriggerAddAction(gg_trg_____________________________________001_Copy, Trig_____________________________________001_Copy_Actions)
end
--===========================================================================
-- Trigger: AuraStart
--===========================================================================
function Trig_AuraStart_Conditions()
    return GetUnitTypeId(GetTriggerUnit()) == FourCC('h0DT')
end
function Trig_AuraStart_Actions()
    UnitAddAbilityBJ(FourCC('A0LU'), GetTriggerUnit())
end
--===========================================================================
function InitTrig_AuraStart()
    gg_trg_AuraStart=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_AuraStart, EVENT_PLAYER_UNIT_CONSTRUCT_FINISH)
    TriggerAddCondition(gg_trg_AuraStart, Condition(Trig_AuraStart_Conditions))
    TriggerAddAction(gg_trg_AuraStart, Trig_AuraStart_Actions)
end
--===========================================================================
-- Trigger: Pole Astrala Demons
--===========================================================================
function Trig_Pole_Astrala_Demons_Func003A()
    local u
    CreateNUnitsAtLoc(1, FourCC('H0BN'), GetOwningPlayer(GetTriggerUnit()), udg_LocalPosition[14], bj_UNIT_FACING)
    UnitAddAbilityBJ(FourCC('AHbn'), GetLastCreatedUnit())
    SetUnitManaBJ(GetLastCreatedUnit(), 1111111.00)
    SetUnitAbilityLevelSwapped(FourCC('AHbn'), GetLastCreatedUnit(), GetUnitAbilityLevelSwapped(FourCC('A08R'), GetTriggerUnit()))
    IssueTargetOrderBJ(GetLastCreatedUnit(), "banish", GetEnumUnit())
    u=udg_LocalUnit[1]
    UnitApplyTimedLife(u, FourCC('BTLF'), 2)
    u=nil
end
function Trig_Pole_Astrala_Demons_Actions()
    udg_LocalOtrad=GetUnitsInRangeOfLocAll(125.00, GetSpellTargetLoc())
    udg_LocalPosition[14]=GetUnitLoc(GetTriggerUnit())
    ForGroupBJ(udg_LocalOtrad, Trig_Pole_Astrala_Demons_Func003A)
    RemoveLocation(udg_LocalPosition[14])
end
--===========================================================================
function InitTrig_Pole_Astrala_Demons()
    gg_trg_Pole_Astrala_Demons=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_Pole_Astrala_Demons, EVENT_PLAYER_UNIT_SPELL_EFFECT)
    TriggerAddAction(gg_trg_Pole_Astrala_Demons, function()
        if GetSpellAbilityId() ~= FourCC('A0N9') then return end
        Trig_Pole_Astrala_Demons_Actions()
    end)
end
--===========================================================================
-- Trigger: Pole Astrala Demons Copy
--===========================================================================
function Trig_Pole_Astrala_Demons_Copy_Func003A()
    local u
    CreateNUnitsAtLoc(1, FourCC('H0BN'), GetOwningPlayer(GetTriggerUnit()), udg_LocalPosition[14], bj_UNIT_FACING)
    UnitAddAbilityBJ(FourCC('AHbn'), GetLastCreatedUnit())
    SetUnitManaBJ(GetLastCreatedUnit(), 1111111.00)
    SetUnitAbilityLevelSwapped(FourCC('AHbn'), GetLastCreatedUnit(), GetUnitAbilityLevelSwapped(FourCC('A1BY'), GetTriggerUnit()))
    IssueTargetOrderBJ(GetLastCreatedUnit(), "banish", GetEnumUnit())
    u=udg_LocalUnit[1]
    UnitApplyTimedLife(u, FourCC('BTLF'), 2)
    u=nil
end
function Trig_Pole_Astrala_Demons_Copy_Actions()
    udg_LocalOtrad=GetUnitsInRangeOfLocAll(125.00, GetSpellTargetLoc())
    udg_LocalPosition[14]=GetUnitLoc(GetTriggerUnit())
    ForGroupBJ(udg_LocalOtrad, Trig_Pole_Astrala_Demons_Copy_Func003A)
    RemoveLocation(udg_LocalPosition[14])
end
--===========================================================================
function InitTrig_Pole_Astrala_Demons_Copy()
    gg_trg_Pole_Astrala_Demons_Copy=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_Pole_Astrala_Demons_Copy, EVENT_PLAYER_UNIT_SPELL_EFFECT)
    TriggerAddAction(gg_trg_Pole_Astrala_Demons_Copy, function()
        if GetSpellAbilityId() ~= FourCC('A1BY') then return end
        Trig_Pole_Astrala_Demons_Copy_Actions()
    end)
end
--===========================================================================
-- Trigger: Pole Astrala Demons Copy Copy
--===========================================================================
function Trig_Pole_Astrala_Demons_Copy_Copy_Func003A()
    local u
    CreateNUnitsAtLoc(1, FourCC('H0BN'), GetOwningPlayer(GetTriggerUnit()), udg_LocalPosition[14], bj_UNIT_FACING)
    UnitAddAbilityBJ(FourCC('AHbn'), GetLastCreatedUnit())
    SetUnitManaBJ(GetLastCreatedUnit(), 1111111.00)
    SetUnitAbilityLevelSwapped(FourCC('AHbn'), GetLastCreatedUnit(), GetUnitAbilityLevelSwapped(FourCC('A08R'), GetTriggerUnit()))
    IssueTargetOrderBJ(GetLastCreatedUnit(), "banish", GetEnumUnit())
    u=udg_LocalUnit[1]
    UnitApplyTimedLife(u, FourCC('BTLF'), 2)
    u=nil
end
function Trig_Pole_Astrala_Demons_Copy_Copy_Actions()
    udg_LocalOtrad=GetUnitsInRangeOfLocAll(125.00, GetSpellTargetLoc())
    udg_LocalPosition[14]=GetUnitLoc(GetTriggerUnit())
    ForGroupBJ(udg_LocalOtrad, Trig_Pole_Astrala_Demons_Copy_Copy_Func003A)
    RemoveLocation(udg_LocalPosition[14])
end
--===========================================================================
function InitTrig_Pole_Astrala_Demons_Copy_Copy()
    gg_trg_Pole_Astrala_Demons_Copy_Copy=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_Pole_Astrala_Demons_Copy_Copy, EVENT_PLAYER_UNIT_SPELL_EFFECT)
    TriggerAddAction(gg_trg_Pole_Astrala_Demons_Copy_Copy, function()
        if GetSpellAbilityId() ~= FourCC('A1BZ') then return end
        Trig_Pole_Astrala_Demons_Copy_Copy_Actions()
    end)
end
--===========================================================================
-- Trigger: Pole Astrala Demons Copy Copy 2
--===========================================================================
function Trig_Pole_Astrala_Demons_Copy_Copy_2_Func003A()
    local u
    CreateNUnitsAtLoc(1, FourCC('H0BN'), GetOwningPlayer(GetTriggerUnit()), udg_LocalPosition[14], bj_UNIT_FACING)
    UnitAddAbilityBJ(FourCC('AHbn'), GetLastCreatedUnit())
    SetUnitManaBJ(GetLastCreatedUnit(), 1111111.00)
    SetUnitAbilityLevelSwapped(FourCC('AHbn'), GetLastCreatedUnit(), GetUnitAbilityLevelSwapped(FourCC('A08R'), GetTriggerUnit()))
    IssueTargetOrderBJ(GetLastCreatedUnit(), "banish", GetEnumUnit())
    u=udg_LocalUnit[1]
    UnitApplyTimedLife(u, FourCC('BTLF'), 2)
    u=nil
end
function Trig_Pole_Astrala_Demons_Copy_Copy_2_Actions()
    udg_LocalOtrad=GetUnitsInRangeOfLocAll(125.00, GetSpellTargetLoc())
    udg_LocalPosition[14]=GetUnitLoc(GetTriggerUnit())
    ForGroupBJ(udg_LocalOtrad, Trig_Pole_Astrala_Demons_Copy_Copy_2_Func003A)
    RemoveLocation(udg_LocalPosition[14])
end
--===========================================================================
function InitTrig_Pole_Astrala_Demons_Copy_Copy_2()
    gg_trg_Pole_Astrala_Demons_Copy_Copy_2=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_Pole_Astrala_Demons_Copy_Copy_2, EVENT_PLAYER_UNIT_SPELL_EFFECT)
    TriggerAddAction(gg_trg_Pole_Astrala_Demons_Copy_Copy_2, function()
        if GetSpellAbilityId() ~= FourCC('A1C0') then return end
        Trig_Pole_Astrala_Demons_Copy_Copy_2_Actions()
    end)
end
--===========================================================================
-- Trigger: SargerasReturnDamage
--===========================================================================
function Trig_SargerasReturnDamage_Conditions()
    return GetUnitAbilityLevel(GetEventDamageSource(), FourCC('A0MQ')) > 0
end
function Trig_SargerasReturnDamage_Actions()
    local hp_factor= 1 - GetUnitLifePercent(GetTriggerUnit())
    local damage= GetEventDamage() * GetUnitAbilityLevel(GetEventDamageSource(), FourCC('A0MQ')) * 0.03 * ( 1 + hp_factor )
    UnitDamageTarget(GetEventDamageSource(), GetTriggerUnit(), damage, true, false, ATTACK_TYPE_CHAOS, DAMAGE_TYPE_DEATH, WEAPON_TYPE_WHOKNOWS)
    
end
--===========================================================================
function InitTrig_SargerasReturnDamage()
    gg_trg_SargerasReturnDamage=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_SargerasReturnDamage, EVENT_PLAYER_UNIT_DAMAGED)
    TriggerAddCondition(gg_trg_SargerasReturnDamage, Condition(Trig_SargerasReturnDamage_Conditions))
    TriggerAddAction(gg_trg_SargerasReturnDamage, Trig_SargerasReturnDamage_Actions)
end
--===========================================================================
-- Trigger: Blood1
--===========================================================================
function Trig_Blood1_Conditions()
    return GetResearched() == FourCC('R08H')
end
function Trig_Blood1_Actions()
    SetPlayerTechMaxAllowedSwap(FourCC('n026'), 0, GetOwningPlayer(GetTriggerUnit()))
    SetPlayerTechMaxAllowed(GetOwningPlayer(GetTriggerUnit()), FourCC('n02D'), - 1)
end
--===========================================================================
function InitTrig_Blood1()
    gg_trg_Blood1=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_Blood1, EVENT_PLAYER_UNIT_RESEARCH_FINISH)
    TriggerAddCondition(gg_trg_Blood1, Condition(Trig_Blood1_Conditions))
    TriggerAddAction(gg_trg_Blood1, Trig_Blood1_Actions)
end
--===========================================================================
-- Trigger: Blood
--===========================================================================
function Trig_Blood_Conditions()
    return GetResearched() == FourCC('R004')
end
function Trig_Blood_Actions()
    SetPlayerTechMaxAllowedSwap(FourCC('n025'), 0, GetOwningPlayer(GetTriggerUnit()))
    SetPlayerTechMaxAllowed(GetOwningPlayer(GetTriggerUnit()), FourCC('n026'), - 1) --???????? ?????
end
--===========================================================================
function InitTrig_Blood()
    gg_trg_Blood=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_Blood, EVENT_PLAYER_UNIT_RESEARCH_FINISH)
    TriggerAddCondition(gg_trg_Blood, Condition(Trig_Blood_Conditions))
    TriggerAddAction(gg_trg_Blood, Trig_Blood_Actions)
end
--===========================================================================
-- Trigger: Blood2
--===========================================================================
function Trig_Blood2_Conditions()
    return GetResearched() == FourCC('R08I')
end
function Trig_Blood2_Actions()
    SetPlayerTechMaxAllowedSwap(FourCC('n02D'), 0, GetOwningPlayer(GetTriggerUnit()))
    SetPlayerTechMaxAllowed(GetOwningPlayer(GetTriggerUnit()), FourCC('n02E'), - 1)
end
--===========================================================================
function InitTrig_Blood2()
    gg_trg_Blood2=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_Blood2, EVENT_PLAYER_UNIT_RESEARCH_FINISH)
    TriggerAddCondition(gg_trg_Blood2, Condition(Trig_Blood2_Conditions))
    TriggerAddAction(gg_trg_Blood2, Trig_Blood2_Actions)
end
--===========================================================================
-- Trigger: ?????????? ??????? 001
--===========================================================================
function Trig_____________________________________001_Actions()
    UnitAddAbilityBJ(FourCC('A0Y9'), GetTriggerUnit())
    RemoveAbilityTimed(GetTriggerUnit() , FourCC('A0Y9') , 20.00)
end
--===========================================================================
function InitTrig_____________________________________001()
    gg_trg_____________________________________001=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_____________________________________001, EVENT_PLAYER_UNIT_SPELL_EFFECT)
    TriggerAddAction(gg_trg_____________________________________001, function()
        if GetSpellAbilityId() ~= FourCC('A0N6') then return end
        Trig_____________________________________001_Actions()
    end)
end
--===========================================================================
-- Trigger: SomeDemonSpell
--===========================================================================
function Trig_SomeDemonSpell_Actions()
    UnitAddAbilityBJ(FourCC('A0NC'), GetTriggerUnit())
    RemoveAbilityTimed(GetTriggerUnit() , FourCC('A0NC') , 20.00)
end
--===========================================================================
function InitTrig_SomeDemonSpell()
    gg_trg_SomeDemonSpell=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_SomeDemonSpell, EVENT_PLAYER_UNIT_SPELL_EFFECT)
    TriggerAddAction(gg_trg_SomeDemonSpell, function()
        if GetSpellAbilityId() ~= FourCC('A0NB') then return end
        Trig_SomeDemonSpell_Actions()
    end)
end