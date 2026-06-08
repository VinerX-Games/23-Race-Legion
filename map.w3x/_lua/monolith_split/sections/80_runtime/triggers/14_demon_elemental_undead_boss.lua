    gg_trg_TrainGreenSpellSteal=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_TrainGreenSpellSteal, EVENT_PLAYER_UNIT_CONSTRUCT_FINISH)
    TriggerAddCondition(gg_trg_TrainGreenSpellSteal, Condition(Trig_TrainGreenSpellSteal_Conditions))
    TriggerAddAction(gg_trg_TrainGreenSpellSteal, Trig_TrainGreenSpellSteal_Actions)
end
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
    udg_Dm[1]=( udg_Dm[2] - GetUnitStateSwap(UNIT_STATE_LIFE, GetAttackedUnitBJ()) )
    if Trig_____________________________________001_Copy_Func004C() then
        UnitDamageTargetBJ(GetAttackedUnitBJ(), GetAttacker(), ( udg_Dm[1] * 0.01 ), ATTACK_TYPE_CHAOS, DAMAGE_TYPE_NORMAL)
    else
        if Trig_____________________________________001_Copy_Func004Func001C() then
            UnitDamageTargetBJ(GetAttackedUnitBJ(), GetAttacker(), ( udg_Dm[1] * 0.02 ), ATTACK_TYPE_CHAOS, DAMAGE_TYPE_NORMAL)
        else
            if Trig_____________________________________001_Copy_Func004Func001Func001C() then
                UnitDamageTargetBJ(GetAttackedUnitBJ(), GetAttacker(), ( udg_Dm[1] * 0.03 ), ATTACK_TYPE_CHAOS, DAMAGE_TYPE_NORMAL)
            else
                if Trig_____________________________________001_Copy_Func004Func001Func001Func001C() then
                    UnitDamageTargetBJ(GetAttackedUnitBJ(), GetAttacker(), ( udg_Dm[1] * 0.04 ), ATTACK_TYPE_CHAOS, DAMAGE_TYPE_NORMAL)
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
--===========================================================================
-- Trigger: Units
--===========================================================================
function Trig_Units_Actions()
    SetPlayerTechMaxAllowedSwap(FourCC('h0F1'), 0, GetOwningPlayer(GetTriggerUnit()))
    SetPlayerTechMaxAllowedSwap(FourCC('n07O'), 0, GetOwningPlayer(GetTriggerUnit()))
    SetPlayerTechMaxAllowedSwap(FourCC('n034'), 0, GetOwningPlayer(GetTriggerUnit()))
    SetPlayerTechMaxAllowedSwap(FourCC('n07N'), 0, GetOwningPlayer(GetTriggerUnit()))
    SetPlayerTechMaxAllowedSwap(FourCC('n07Y'), 0, GetOwningPlayer(GetTriggerUnit()))
    SetPlayerTechMaxAllowedSwap(FourCC('n032'), 0, GetOwningPlayer(GetTriggerUnit()))
    SetPlayerTechMaxAllowedSwap(FourCC('n07T'), 0, GetOwningPlayer(GetTriggerUnit()))
    SetPlayerTechMaxAllowedSwap(FourCC('n035'), 0, GetOwningPlayer(GetTriggerUnit()))
    SetPlayerTechMaxAllowedSwap(FourCC('n031'), 0, GetOwningPlayer(GetTriggerUnit()))
    SetPlayerTechMaxAllowedSwap(FourCC('n07X'), 0, GetOwningPlayer(GetTriggerUnit()))
    SetPlayerTechMaxAllowedSwap(FourCC('n02Z'), 0, GetOwningPlayer(GetTriggerUnit()))
    SetPlayerTechMaxAllowedSwap(FourCC('n033'), 0, GetOwningPlayer(GetTriggerUnit()))
    SetPlayerTechMaxAllowedSwap(FourCC('n02Y'), 0, GetOwningPlayer(GetTriggerUnit()))
    SetPlayerTechMaxAllowedSwap(FourCC('n07S'), 0, GetOwningPlayer(GetTriggerUnit()))
    SetPlayerTechMaxAllowedSwap(FourCC('n07W'), 0, GetOwningPlayer(GetTriggerUnit()))
    SetPlayerTechMaxAllowedSwap(FourCC('n07R'), 0, GetOwningPlayer(GetTriggerUnit()))
    SetPlayerTechMaxAllowedSwap(FourCC('n02P'), 0, GetOwningPlayer(GetTriggerUnit()))
    SetPlayerTechMaxAllowedSwap(FourCC('n07Q'), 0, GetOwningPlayer(GetTriggerUnit()))
    SetPlayerTechMaxAllowedSwap(FourCC('n07Z'), 0, GetOwningPlayer(GetTriggerUnit()))
end
--===========================================================================
function InitTrig_Units()
    gg_trg_Units=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_Units, EVENT_PLAYER_UNIT_SPELL_EFFECT)
    TriggerAddAction(gg_trg_Units, function()
        if GetSpellAbilityId() ~= FourCC('A0QN') then return end
        Trig_Units_Actions()
    end)
end
--===========================================================================
-- Trigger: Fire
--===========================================================================
function Trig_Fire_Actions()
    BlzUnitDisableAbility(GetTriggerUnit(), FourCC('A0W9'), true, true)
    BlzUnitDisableAbility(GetTriggerUnit(), FourCC('A0W7'), true, true)
    BlzUnitDisableAbility(GetTriggerUnit(), FourCC('A0W8'), true, true)
    BlzUnitDisableAbility(GetTriggerUnit(), FourCC('A0WA'), true, true)
    SetPlayerAbilityAvailableBJ(false, FourCC('A0W9'), GetOwningPlayer(GetTriggerUnit()))
    SetPlayerAbilityAvailableBJ(false, FourCC('A0W7'), GetOwningPlayer(GetTriggerUnit()))
    SetPlayerAbilityAvailableBJ(false, FourCC('A0W8'), GetOwningPlayer(GetTriggerUnit()))
    SetPlayerAbilityAvailableBJ(false, FourCC('A0WA'), GetOwningPlayer(GetTriggerUnit()))
    SetPlayerAbilityAvailableBJ(false, FourCC('A0WA'), GetOwningPlayer(GetTriggerUnit()))
    SetPlayerTechMaxAllowedSwap(FourCC('h0F1'), - 1, GetOwningPlayer(GetTriggerUnit()))
    SetPlayerTechMaxAllowedSwap(FourCC('n07O'), - 1, GetOwningPlayer(GetTriggerUnit()))
    SetPlayerTechMaxAllowedSwap(FourCC('n034'), - 1, GetOwningPlayer(GetTriggerUnit()))
    SetPlayerTechMaxAllowedSwap(FourCC('n07N'), - 1, GetOwningPlayer(GetTriggerUnit()))
    SetPlayerTechMaxAllowedSwap(FourCC('n07Y'), 1, GetOwningPlayer(GetTriggerUnit()))
    SetPlayerTechMaxAllowedSwap(FourCC('n02R'), 0, GetOwningPlayer(GetTriggerUnit()))
    SetPlayerTechMaxAllowedSwap(FourCC('n02X'), 0, GetOwningPlayer(GetTriggerUnit()))
end
--===========================================================================
function InitTrig_Fire()
    gg_trg_Fire=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_Fire, EVENT_PLAYER_UNIT_SPELL_EFFECT)
    TriggerAddAction(gg_trg_Fire, function()
        if GetSpellAbilityId() ~= FourCC('A0W9') then return end
        Trig_Fire_Actions()
    end)
end
--===========================================================================
-- Trigger: Water
--===========================================================================
function Trig_Water_Actions()
    BlzUnitDisableAbility(GetTriggerUnit(), FourCC('A0W9'), true, true)
    BlzUnitDisableAbility(GetTriggerUnit(), FourCC('A0W7'), true, true)
    BlzUnitDisableAbility(GetTriggerUnit(), FourCC('A0W8'), true, true)
    BlzUnitDisableAbility(GetTriggerUnit(), FourCC('A0WA'), true, true)
    SetPlayerAbilityAvailableBJ(false, FourCC('A0W9'), GetOwningPlayer(GetTriggerUnit()))
    SetPlayerAbilityAvailableBJ(false, FourCC('A0W7'), GetOwningPlayer(GetTriggerUnit()))
    SetPlayerAbilityAvailableBJ(false, FourCC('A0W8'), GetOwningPlayer(GetTriggerUnit()))
    SetPlayerAbilityAvailableBJ(false, FourCC('A0WA'), GetOwningPlayer(GetTriggerUnit()))
    SetPlayerTechMaxAllowedSwap(FourCC('n032'), - 1, GetOwningPlayer(GetTriggerUnit()))
    SetPlayerTechMaxAllowedSwap(FourCC('n07T'), - 1, GetOwningPlayer(GetTriggerUnit()))
    SetPlayerTechMaxAllowedSwap(FourCC('n035'), - 1, GetOwningPlayer(GetTriggerUnit()))
    SetPlayerTechMaxAllowedSwap(FourCC('n031'), - 1, GetOwningPlayer(GetTriggerUnit()))
    SetPlayerTechMaxAllowedSwap(FourCC('n07X'), 1, GetOwningPlayer(GetTriggerUnit()))
    SetPlayerTechMaxAllowedSwap(FourCC('n02X'), 0, GetOwningPlayer(GetTriggerUnit()))
    SetPlayerTechMaxAllowedSwap(FourCC('n02U'), 0, GetOwningPlayer(GetTriggerUnit()))
end
--===========================================================================
function InitTrig_Water()
    gg_trg_Water=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_Water, EVENT_PLAYER_UNIT_SPELL_EFFECT)
    TriggerAddAction(gg_trg_Water, function()
        if GetSpellAbilityId() ~= FourCC('A0W7') then return end
        Trig_Water_Actions()
    end)
end
--===========================================================================
-- Trigger: Earth
--===========================================================================
function Trig_Earth_Actions()
    BlzUnitDisableAbility(GetTriggerUnit(), FourCC('A0W9'), true, true)
    BlzUnitDisableAbility(GetTriggerUnit(), FourCC('A0W7'), true, true)
    BlzUnitDisableAbility(GetTriggerUnit(), FourCC('A0W8'), true, true)
    BlzUnitDisableAbility(GetTriggerUnit(), FourCC('A0WA'), true, true)
    SetPlayerAbilityAvailableBJ(false, FourCC('A0W9'), GetOwningPlayer(GetTriggerUnit()))
    SetPlayerAbilityAvailableBJ(false, FourCC('A0W7'), GetOwningPlayer(GetTriggerUnit()))
    SetPlayerAbilityAvailableBJ(false, FourCC('A0W8'), GetOwningPlayer(GetTriggerUnit()))
    SetPlayerAbilityAvailableBJ(false, FourCC('A0WA'), GetOwningPlayer(GetTriggerUnit()))
    SetPlayerTechMaxAllowedSwap(FourCC('n02Z'), - 1, GetOwningPlayer(GetTriggerUnit()))
    SetPlayerTechMaxAllowedSwap(FourCC('n033'), - 1, GetOwningPlayer(GetTriggerUnit()))
    SetPlayerTechMaxAllowedSwap(FourCC('n02Y'), - 1, GetOwningPlayer(GetTriggerUnit()))
    SetPlayerTechMaxAllowedSwap(FourCC('n07S'), - 1, GetOwningPlayer(GetTriggerUnit()))
    SetPlayerTechMaxAllowedSwap(FourCC('n07W'), 1, GetOwningPlayer(GetTriggerUnit()))
    SetPlayerTechMaxAllowedSwap(FourCC('n02X'), 0, GetOwningPlayer(GetTriggerUnit()))
    SetPlayerTechMaxAllowedSwap(FourCC('n02W'), 0, GetOwningPlayer(GetTriggerUnit()))
end
--===========================================================================
function InitTrig_Earth()
    gg_trg_Earth=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_Earth, EVENT_PLAYER_UNIT_SPELL_EFFECT)
    TriggerAddAction(gg_trg_Earth, function()
        if GetSpellAbilityId() ~= FourCC('A0W8') then return end
        Trig_Earth_Actions()
    end)
end
--===========================================================================
-- Trigger: Wind
--===========================================================================
function Trig_Wind_Actions()
    BlzUnitDisableAbility(GetTriggerUnit(), FourCC('A0W9'), true, true)
    BlzUnitDisableAbility(GetTriggerUnit(), FourCC('A0W7'), true, true)
    BlzUnitDisableAbility(GetTriggerUnit(), FourCC('A0W8'), true, true)
    BlzUnitDisableAbility(GetTriggerUnit(), FourCC('A0WA'), true, true)
    SetPlayerAbilityAvailableBJ(false, FourCC('A0W9'), GetOwningPlayer(GetTriggerUnit()))
    SetPlayerAbilityAvailableBJ(false, FourCC('A0W7'), GetOwningPlayer(GetTriggerUnit()))
    SetPlayerAbilityAvailableBJ(false, FourCC('A0W8'), GetOwningPlayer(GetTriggerUnit()))
    SetPlayerAbilityAvailableBJ(false, FourCC('A0WA'), GetOwningPlayer(GetTriggerUnit()))
    SetPlayerTechMaxAllowedSwap(FourCC('n07R'), - 1, GetOwningPlayer(GetTriggerUnit()))
    SetPlayerTechMaxAllowedSwap(FourCC('n02P'), - 1, GetOwningPlayer(GetTriggerUnit()))
    SetPlayerTechMaxAllowedSwap(FourCC('n07Q'), - 1, GetOwningPlayer(GetTriggerUnit()))
    SetPlayerTechMaxAllowedSwap(FourCC('n07Z'), 1, GetOwningPlayer(GetTriggerUnit()))
    SetPlayerTechMaxAllowedSwap(FourCC('n02X'), 0, GetOwningPlayer(GetTriggerUnit()))
    SetPlayerTechMaxAllowedSwap(FourCC('n02Q'), 0, GetOwningPlayer(GetTriggerUnit()))
end
--===========================================================================
function InitTrig_Wind()
    gg_trg_Wind=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_Wind, EVENT_PLAYER_UNIT_SPELL_EFFECT)
    TriggerAddAction(gg_trg_Wind, function()
        if GetSpellAbilityId() ~= FourCC('A0WA') then return end
        Trig_Wind_Actions()
    end)
end
--===========================================================================
-- Trigger: FireRageElem
--===========================================================================
function Trig_FireRageElem_Actions()
    local u= GetTriggerUnit()
    UnitAddAbility(u, FourCC('A0OM'))
    RemoveAbilityTimed(u , FourCC('A0OM') , 10)
    u=nil
end
--===========================================================================
function InitTrig_FireRageElem()
    gg_trg_FireRageElem=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_FireRageElem, EVENT_PLAYER_UNIT_SPELL_EFFECT)
    TriggerAddAction(gg_trg_FireRageElem, function()
        if GetSpellAbilityId() ~= FourCC('A0QJ') then return end
        Trig_FireRageElem_Actions()
    end)
end
--===========================================================================
-- Trigger: FireCircleElem
--===========================================================================
function Trig_FireCircleElem_Actions()
    UnitAddAbility(GetTriggerUnit(), FourCC('A0P6'))
    RemoveAbilityTimed(GetTriggerUnit() , FourCC('A0P6') , 30)
end
--===========================================================================
function InitTrig_FireCircleElem()
    gg_trg_FireCircleElem=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_FireCircleElem, EVENT_PLAYER_UNIT_SPELL_EFFECT)
    TriggerAddAction(gg_trg_FireCircleElem, function()
        if GetSpellAbilityId() ~= FourCC('A0P7') then return end
        Trig_FireCircleElem_Actions()
    end)
end
--===========================================================================
-- Trigger: ColossalAttackElem
--===========================================================================
function Trig_ColossalAttackElem_Actions()
    UnitAddAbility(GetTriggerUnit(), FourCC('A0OO'))
    RemoveAbilityTimed(GetTriggerUnit() , FourCC('A0OO') , 25)
end
--===========================================================================
function InitTrig_ColossalAttackElem()
    gg_trg_ColossalAttackElem=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_ColossalAttackElem, EVENT_PLAYER_UNIT_SPELL_EFFECT)
    TriggerAddAction(gg_trg_ColossalAttackElem, function()
        if GetSpellAbilityId() ~= FourCC('A0OP') then return end
        Trig_ColossalAttackElem_Actions()
    end)
end
--===========================================================================
-- Trigger: MultuAttackWater
--
-- ????? ?????????? ?????????
--===========================================================================
function Trig_MultuAttackWater_Actions()
    local u= GetTriggerUnit()
    UnitAddAbility(u, FourCC('A0OS'))
    RemoveAbilityTimed(u , FourCC('A0OS') , 10)
    u=nil
end
--===========================================================================
function InitTrig_MultuAttackWater()
    gg_trg_MultuAttackWater=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_MultuAttackWater, EVENT_PLAYER_UNIT_SPELL_EFFECT)
    TriggerAddAction(gg_trg_MultuAttackWater, function()
        if GetSpellAbilityId() ~= FourCC('A0OR') then return end
        Trig_MultuAttackWater_Actions()
    end)
end
--===========================================================================
-- Trigger: gnev1
--===========================================================================
function Trig_gnev1_Conditions()
    return GetResearched() == FourCC('R05B')
end
function Trig_gnev1_Actions()
    SetPlayerTechMaxAllowedSwap(FourCC('R05K'), 0, GetOwningPlayer(GetTriggerUnit()))
end
--===========================================================================
function InitTrig_gnev1()
    gg_trg_gnev1=CreateTrigger()
    DisableTrigger(gg_trg_gnev1)
    TriggerRegisterAnyUnitEventBJ(gg_trg_gnev1, EVENT_PLAYER_UNIT_RESEARCH_FINISH)
    TriggerRegisterAnyUnitEventBJ(gg_trg_gnev1, EVENT_PLAYER_UNIT_RESEARCH_START)
    TriggerAddCondition(gg_trg_gnev1, Condition(Trig_gnev1_Conditions))
    TriggerAddAction(gg_trg_gnev1, Trig_gnev1_Actions)
end
--===========================================================================
-- Trigger: necropol
--===========================================================================
function Trig_necropol_Conditions()
    return GetResearched() == FourCC('R05K')
end
function Trig_necropol_Actions()
    SetPlayerTechMaxAllowedSwap(FourCC('R05B'), 0, GetOwningPlayer(GetTriggerUnit()))
end
--===========================================================================
function InitTrig_necropol()
    gg_trg_necropol=CreateTrigger()
    DisableTrigger(gg_trg_necropol)
    TriggerRegisterAnyUnitEventBJ(gg_trg_necropol, EVENT_PLAYER_UNIT_RESEARCH_FINISH)
    TriggerRegisterAnyUnitEventBJ(gg_trg_necropol, EVENT_PLAYER_UNIT_RESEARCH_START)
    TriggerAddCondition(gg_trg_necropol, Condition(Trig_necropol_Conditions))
    TriggerAddAction(gg_trg_necropol, Trig_necropol_Actions)
end
--===========================================================================
-- Trigger: gnev2
--===========================================================================
function Trig_gnev2_Conditions()
    return GetResearched() == FourCC('R05B')
end
function Trig_gnev2_Actions()
    SetPlayerTechMaxAllowedSwap(FourCC('R05K'), 1, GetOwningPlayer(GetTriggerUnit()))
end
--===========================================================================
function InitTrig_gnev2()
    gg_trg_gnev2=CreateTrigger()
    DisableTrigger(gg_trg_gnev2)
    TriggerRegisterAnyUnitEventBJ(gg_trg_gnev2, EVENT_PLAYER_UNIT_RESEARCH_CANCEL)
    TriggerAddCondition(gg_trg_gnev2, Condition(Trig_gnev2_Conditions))
    TriggerAddAction(gg_trg_gnev2, Trig_gnev2_Actions)
end
--===========================================================================
-- Trigger: necropol2
--===========================================================================
function Trig_necropol2_Conditions()
    return GetResearched() == FourCC('R05K')
end
function Trig_necropol2_Actions()
    SetPlayerTechMaxAllowedSwap(FourCC('R05B'), 1, GetOwningPlayer(GetTriggerUnit()))
end
--===========================================================================
function InitTrig_necropol2()
    gg_trg_necropol2=CreateTrigger()
    DisableTrigger(gg_trg_necropol2)
    TriggerRegisterAnyUnitEventBJ(gg_trg_necropol2, EVENT_PLAYER_UNIT_RESEARCH_CANCEL)
    TriggerAddCondition(gg_trg_necropol2, Condition(Trig_necropol2_Conditions))
    TriggerAddAction(gg_trg_necropol2, Trig_necropol2_Actions)
end
--===========================================================================
-- Trigger: UndeadOn
--===========================================================================
function Trig_UndeadOn_Actions()
    EnableTrigger(gg_trg_UndeadSell)
    EnableTrigger(gg_trg_ArthasResurrection)
    EnableTrigger(gg_trg_ArthasCoils)
    EnableTrigger(gg_trg_ArthasNova)
    --call EnableTrigger( gg_trg_BloodOpen )
    
    EnableTrigger(gg_trg_DK_Blood_Auto_Attack)
    EnableTrigger(gg_trg_TryToBurrow)
    EnableTrigger(gg_trg_KillSpaned)
    EnableTrigger(gg_trg_SummonSkeleltClad)
    
    EnableTrigger(gg_trg_TowersEcFix)
    EnableTrigger(gg_trg_SpellShieldDK)
    
end
--===========================================================================
function InitTrig_UndeadOn()
    gg_trg_UndeadOn=CreateTrigger()
    TriggerAddAction(gg_trg_UndeadOn, Trig_UndeadOn_Actions)
end
--===========================================================================
-- Trigger: UndeadStart
--===========================================================================
function Trig_UndeadStart_Func001A()
    SetPlayerTechMaxAllowedSwap(FourCC('U030'), 1, GetEnumPlayer())
    SetPlayerTechMaxAllowedSwap(FourCC('FL00'), 1, GetEnumPlayer())
    SetPlayerTechMaxAllowedSwap(FourCC('CM00'), 1, GetEnumPlayer())
end
function Trig_UndeadStart_Actions()
    ForForce(udg_AllPlayers, Trig_UndeadStart_Func001A)
end
--===========================================================================
function InitTrig_UndeadStart()
    gg_trg_UndeadStart=CreateTrigger()
    TriggerRegisterTimerEventSingle(gg_trg_UndeadStart, 0.01)
    TriggerAddAction(gg_trg_UndeadStart, Trig_UndeadStart_Actions)
end
--===========================================================================
-- Trigger: SummonSkeleltClad
--===========================================================================
function Trig_SummonSkeleltClad_Conditions()
    return GetUnitTypeId(GetSummoningUnit()) == FourCC('u00L')
end
function Trig_SummonSkeleltClad_Actions()
    gLoc=GetUnitRallyPoint(GetSummoningUnit())
    IssuePointOrderLoc(GetSummonedUnit(), "move", gLoc)
    RemoveLocation(gLoc)
end
--===========================================================================
function InitTrig_SummonSkeleltClad()
    gg_trg_SummonSkeleltClad=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_SummonSkeleltClad, EVENT_PLAYER_UNIT_SUMMON)
    TriggerAddCondition(gg_trg_SummonSkeleltClad, Condition(Trig_SummonSkeleltClad_Conditions))
    TriggerAddAction(gg_trg_SummonSkeleltClad, Trig_SummonSkeleltClad_Actions)
end
--===========================================================================
-- Trigger: SpellShieldDK
--===========================================================================
function Trig_SpellShieldDK_Actions()
    DummyCastTarget(FourCC('A0CG') , "antimagicshell" , GetTriggerUnit() , GetTriggerUnit())
end
--===========================================================================
function InitTrig_SpellShieldDK()
    gg_trg_SpellShieldDK=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_SpellShieldDK, EVENT_PLAYER_UNIT_SPELL_EFFECT)
    TriggerAddAction(gg_trg_SpellShieldDK, function()
        if GetSpellAbilityId() ~= FourCC('A1ND') then return end
        Trig_SpellShieldDK_Actions()
    end)
end
--===========================================================================
-- Trigger: TowersEcFix
--===========================================================================
function Trig_TowersEcFix_Conditions()
    return GetUnitTypeId(GetTriggerUnit()) == FourCC('u00J') or GetUnitTypeId(GetTriggerUnit()) == FourCC('u00I')
end
function Trig_TowersEcFix_Actions()
    local pi= GetPlayerId(GetOwningPlayer(GetTriggerUnit()))
    income[pi]=income[pi] - 40
    UpdateGraf(pi)
end
--===========================================================================
function InitTrig_TowersEcFix()
    gg_trg_TowersEcFix=CreateTrigger()
    DisableTrigger(gg_trg_TowersEcFix)
    TriggerRegisterAnyUnitEventBJ(gg_trg_TowersEcFix, EVENT_PLAYER_UNIT_UPGRADE_FINISH)
    TriggerAddCondition(gg_trg_TowersEcFix, Condition(Trig_TowersEcFix_Conditions))
    TriggerAddAction(gg_trg_TowersEcFix, Trig_TowersEcFix_Actions)
end
--===========================================================================
-- Trigger: DK Blood Auto Attack
--===========================================================================
function Trig_DK_Blood_Auto_Attack_Conditions()
    return ( GetUnitAbilityLevel(GetAttacker(), FourCC('A0CA')) > 0 or GetUnitAbilityLevel(GetAttacker(), FourCC('A0CC')) > 0 ) and IsPlayerEnemy(GetOwningPlayer(GetTriggerUnit()), GetOwningPlayer(GetAttacker())) and Random(1 , 20)
end
function Trig_DK_Blood_Auto_Attack_Actions()
    IssueTargetOrder(GetAttacker(), "thunderbolt", GetTriggerUnit())
end
--===========================================================================
function InitTrig_DK_Blood_Auto_Attack()
    gg_trg_DK_Blood_Auto_Attack=CreateTrigger()
    DisableTrigger(gg_trg_DK_Blood_Auto_Attack)
    TriggerRegisterAnyUnitEventBJ(gg_trg_DK_Blood_Auto_Attack, EVENT_PLAYER_UNIT_ATTACKED)
    TriggerAddCondition(gg_trg_DK_Blood_Auto_Attack, Condition(Trig_DK_Blood_Auto_Attack_Conditions))
    TriggerAddAction(gg_trg_DK_Blood_Auto_Attack, Trig_DK_Blood_Auto_Attack_Actions)
end
--===========================================================================
-- Trigger: TryToBurrow
--===========================================================================
function Trig_TryToBurrow_Conditions()
    return GetUnitAbilityLevel(GetTriggerUnit(), FourCC('A1N8')) > 0 and GetUnitLifePercent(GetTriggerUnit()) <= 18
end
function Trig_TryToBurrow_Actions()
   
    IssueImmediateOrder(GetTriggerUnit(), "burrow")
end
--===========================================================================
function InitTrig_TryToBurrow()
    gg_trg_TryToBurrow=CreateTrigger()
    DisableTrigger(gg_trg_TryToBurrow)
    TriggerRegisterAnyUnitEventBJ(gg_trg_TryToBurrow, EVENT_PLAYER_UNIT_ATTACKED)
    TriggerAddCondition(gg_trg_TryToBurrow, Condition(Trig_TryToBurrow_Conditions))
    TriggerAddAction(gg_trg_TryToBurrow, Trig_TryToBurrow_Actions)
end
--===========================================================================
-- Trigger: ArthasResurrection
--===========================================================================
function Trig_ArthasResurrection_Conditions()
    return GetUnitAbilityLevel(GetKillingUnit(), FourCC('A0WB')) >= 1
end
function Trig_ArthasResurrection_Actions()
   -- call DummyCastImmedate('A0WC',"animatedead",GetTriggerUnit())
   
    DummyCastImmedateOnTarget(FourCC('A0WC') , "animatedead" , GetKillingUnit() , GetTriggerUnit())
--    local unit u
--    
--    
--    set udg_LocalPosition2 = GetUnitLoc(GetTriggerUnit())
--    call CreateNUnitsAtLoc( 1, 'h05P', GetOwningPlayer(GetKillingUnitBJ()), udg_LocalPosition2, bj_UNIT_FACING )
--    
--    set udg_LocalUnit2 = GetLastCreatedUnit()
--    set u = udg_LocalUnit2
--    call UnitAddAbilityBJ( 'A0WC', GetLastCreatedUnit() )
--    call IssueImmediateOrderBJ( GetLastCreatedUnit(), "animatedead" )
--    call TriggerSleepAction( 2 )
--    set udg_LocalUnit2 = u
--    call RemoveUnit( udg_LocalUnit2 )
--    call RemoveLocation(udg_LocalPosition2)
end
--===========================================================================
function InitTrig_ArthasResurrection()
    gg_trg_ArthasResurrection=CreateTrigger()
    DisableTrigger(gg_trg_ArthasResurrection)
    TriggerRegisterAnyUnitEventBJ(gg_trg_ArthasResurrection, EVENT_PLAYER_UNIT_DEATH)
    TriggerAddCondition(gg_trg_ArthasResurrection, Condition(Trig_ArthasResurrection_Conditions))
    TriggerAddAction(gg_trg_ArthasResurrection, Trig_ArthasResurrection_Actions)
end
--===========================================================================
-- Trigger: ArthasCoils
--===========================================================================
function Trig_ArthasCoils_Func002002()
    return 0 == 0
end
function Trig_ArthasCoils_Func007A()
    CreateNUnitsAtLoc(1, FourCC('H0BN'), GetOwningPlayer(GetTriggerUnit()), udg_LocalPosition2, bj_UNIT_FACING)
    udg_LocalUnit2=GetLastCreatedUnit()
    TriggerExecute(gg_trg_ToKill2)
    UnitAddAbilityBJ(FourCC('AUdc'), GetLastCreatedUnit())
    SetUnitManaBJ(GetLastCreatedUnit(), 1111111.00)
    SetUnitAbilityLevelSwapped(FourCC('AUdc'), GetLastCreatedUnit(), GetUnitAbilityLevelSwapped(FourCC('A0WD'), GetTriggerUnit()))
    IssueTargetOrderBJ(GetLastCreatedUnit(), "deathcoil", GetEnumUnit())
end
function Trig_ArthasCoils_Actions()
    udg_LocalPosition2=GetSpellTargetLoc()
    udg_Boolexpr = Trig_ArthasCoils_Func002002
    GroupEnumUnitsInRangeOfLoc(udg_LocalOtrad2, udg_LocalPosition2, 125, udg_Boolexpr)
    RemoveLocation(udg_LocalPosition2)
    udg_LocalPosition2=GetUnitLoc(GetTriggerUnit())
    ForGroupBJ(udg_LocalOtrad2, Trig_ArthasCoils_Func007A)
    RemoveLocation(udg_LocalPosition2)
    GroupClear(udg_LocalOtrad2)
end
--===========================================================================
function InitTrig_ArthasCoils()
    gg_trg_ArthasCoils=CreateTrigger()
    DisableTrigger(gg_trg_ArthasCoils)
    TriggerRegisterAnyUnitEventBJ(gg_trg_ArthasCoils, EVENT_PLAYER_UNIT_SPELL_EFFECT)
    TriggerAddAction(gg_trg_ArthasCoils, function()
        if GetSpellAbilityId() ~= FourCC('A0WD') then return end
        Trig_ArthasCoils_Actions()
    end)
end
--===========================================================================
-- Trigger: ArthasNova
--===========================================================================
function Trig_ArthasNova_Func002002()
    return 0 == 0
end
function Trig_ArthasNova_Func007A()
    CreateNUnitsAtLoc(1, FourCC('H0BN'), GetOwningPlayer(GetTriggerUnit()), udg_LocalPosition2, bj_UNIT_FACING)
    udg_LocalUnit2=GetLastCreatedUnit()
    TriggerExecute(gg_trg_ToKill2)
    UnitAddAbilityBJ(FourCC('A0WF'), GetLastCreatedUnit())
    SetUnitManaBJ(GetLastCreatedUnit(), 1111111.00)
    SetUnitAbilityLevelSwapped(FourCC('A0WF'), GetLastCreatedUnit(), GetUnitAbilityLevelSwapped(FourCC('A0WE'), GetTriggerUnit()))
    IssueTargetOrderBJ(GetLastCreatedUnit(), "frostnova", GetEnumUnit())
end
function Trig_ArthasNova_Actions()
    udg_LocalPosition2=GetUnitLoc(GetTriggerUnit())
    udg_Boolexpr = Trig_ArthasNova_Func002002
    GroupEnumUnitsInRangeOfLoc(udg_LocalOtrad2, udg_LocalPosition2, 240, udg_Boolexpr)
    RemoveLocation(udg_LocalPosition2)
    udg_LocalPosition2=GetUnitLoc(GetTriggerUnit())
    ForGroupBJ(udg_LocalOtrad2, Trig_ArthasNova_Func007A)
    RemoveLocation(udg_LocalPosition2)
    GroupClear(udg_LocalOtrad2)
end
--===========================================================================
function InitTrig_ArthasNova()
    gg_trg_ArthasNova=CreateTrigger()
    DisableTrigger(gg_trg_ArthasNova)
    TriggerRegisterAnyUnitEventBJ(gg_trg_ArthasNova, EVENT_PLAYER_UNIT_SPELL_EFFECT)
    TriggerAddAction(gg_trg_ArthasNova, function()
        if GetSpellAbilityId() ~= FourCC('A0WE') then return end
        Trig_ArthasNova_Actions()
    end)
end
--===========================================================================
-- Trigger: KillSpaned
--===========================================================================
function Trig_KillSpaned_Conditions()
    return GetUnitTypeId(GetSummonedUnit()) == FourCC('n017')
end
function Trig_KillSpaned_Actions()
    KillUnit(GetSummonedUnit())
end
--===========================================================================
function InitTrig_KillSpaned()
    gg_trg_KillSpaned=CreateTrigger()
    DisableTrigger(gg_trg_KillSpaned)
    TriggerRegisterAnyUnitEventBJ(gg_trg_KillSpaned, EVENT_PLAYER_UNIT_SUMMON)
    TriggerAddCondition(gg_trg_KillSpaned, Condition(Trig_KillSpaned_Conditions))
    TriggerAddAction(gg_trg_KillSpaned, Trig_KillSpaned_Actions)
end
--===========================================================================
-- Trigger: AreaOfDeath Copy
--===========================================================================
function Trig_AreaOfDeath_Copy_Actions()
    SpellChannelLevel(GetTriggerUnit() , FourCC('kel0') , FourCC('A1E7') , "deathanddecay" , GetSpellTargetX() , GetSpellTargetY() , 17)
end
--===========================================================================
function InitTrig_AreaOfDeath_Copy()
    gg_trg_AreaOfDeath_Copy=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_AreaOfDeath_Copy, EVENT_PLAYER_UNIT_SPELL_EFFECT)
    TriggerAddAction(gg_trg_AreaOfDeath_Copy, function()
        if GetSpellAbilityId() ~= FourCC('kel0') then return end
        Trig_AreaOfDeath_Copy_Actions()
    end)
end
--===========================================================================
-- Trigger: AutocastShieldOnResearch
--===========================================================================
function Trig_AutocastShieldOnResearch_Conditions()
    return GetResearched() == FourCC('R06Y') and GetPlayerTechCount(GetOwningPlayer(GetTriggerUnit()), FourCC('R06Y'), true) == 2
end
function Trig_AutocastShieldOnResearch_Actions()
    GlobalIssue(FourCC('e01A') , GetOwningPlayer(GetTriggerUnit()) , "manashield")
end
--===========================================================================
function InitTrig_AutocastShieldOnResearch()
    gg_trg_AutocastShieldOnResearch=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_AutocastShieldOnResearch, EVENT_PLAYER_UNIT_RESEARCH_FINISH)
    TriggerAddCondition(gg_trg_AutocastShieldOnResearch, Condition(Trig_AutocastShieldOnResearch_Conditions))
    TriggerAddAction(gg_trg_AutocastShieldOnResearch, Trig_AutocastShieldOnResearch_Actions)
end
--===========================================================================
-- Trigger: TrainAutcastZam
--===========================================================================
function Trig_TrainAutcastZam_Conditions()
    return GetUnitAbilityLevel(GetTrainedUnit(), FourCC('A0GI')) > 0
end
function Trig_TrainAutcastZam_Actions()
    IssueImmediateOrder(GetTrainedUnit(), "slowon")
end
--===========================================================================
function InitTrig_TrainAutcastZam()
    gg_trg_TrainAutcastZam=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_TrainAutcastZam, EVENT_PLAYER_UNIT_TRAIN_FINISH)
    TriggerAddCondition(gg_trg_TrainAutcastZam, Condition(Trig_TrainAutcastZam_Conditions))
    TriggerAddAction(gg_trg_TrainAutcastZam, Trig_TrainAutcastZam_Actions)
end
--===========================================================================
-- Trigger: PassiveTalisra
--===========================================================================
function Trig_PassiveTalisra_Conditions()
    return GetUnitAbilityLevel(GetTriggerUnit(), FourCC('B08J')) + GetUnitAbilityLevel(GetTriggerUnit(), FourCC('B08K')) > 0 and not IsUnitType(GetTriggerUnit(), UNIT_TYPE_HERO) and GetEventDamage() >= GetUnitState(GetTriggerUnit(), UNIT_STATE_LIFE) --?? ????
end
function Talisra()
    return GetUnitAbilityLevel(GetFilterUnit(), FourCC('A1OS')) > 0 --??????
end
function Trig_PassiveTalisra_Actions()
    local g= CreateGroup()
    local u= GetTriggerUnit()
    local u2
    local p= GetOwningPlayer(u)
    local pi= GetPlayerId(p)
    GroupEnumUnitsInRangeCounted(g, GetUnitX(u), GetUnitY(u), 650, Talisra, 1)
    u2=FirstOfGroup(g)
    if GetRandomInt(1, 4) + 0.25 * GetUnitAbilityLevel(u2, FourCC('A1OS')) > 3 and GetUnitState(u2, UNIT_STATE_MANA) > 50 then --??????
        SetUnitManaBJ(u2, GetUnitState(u2, UNIT_STATE_MANA) - 50)
        if playerCapital[pi] == nil then
            MakeFakeCapital(p)
        end
        if playerCapital[pi] ~= nil then
            SetUnitX(u, GetUnitX(playerCapital[pi]))
            SetUnitY(u, GetUnitY(playerCapital[pi]))
            SetUnitLifePercentBJ(u, 10)
            SetUnitLifeBJ(u, GetUnitState(u, UNIT_STATE_LIFE) + GetEventDamage())
            RemoveEffectTimed(AddSpecialEffect("AbilitiesSpellsHumanMassTeleportMassTeleportCaster.mdl", GetUnitX(u), GetUnitY(u)) , 3)
            RemoveEffectTimed(AddSpecialEffect("AbilitiesSpellsHumanMassTeleportMassTeleportCaster.mdl", GetUnitX(playerCapital[pi]), GetUnitY(playerCapital[pi])) , 3)
        end
    end
    
    DestroyGroup(g)
    g=nil
    u=nil
    u2=nil
end
--===========================================================================
function InitTrig_PassiveTalisra()
    gg_trg_PassiveTalisra=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_PassiveTalisra, EVENT_PLAYER_UNIT_DAMAGING)
    TriggerAddCondition(gg_trg_PassiveTalisra, Condition(Trig_PassiveTalisra_Conditions))
    TriggerAddAction(gg_trg_PassiveTalisra, Trig_PassiveTalisra_Actions)
end
--===========================================================================
-- Trigger: IceTrollsStart
--===========================================================================
function IceTrollsStartEach()
    local p= GetEnumPlayer()
    
    SetPlayerTechMaxAllowedSwap(FourCC('n07B'), 0, p) -- ????????? ???
    SetPlayerTechMaxAllowedSwap(FourCC('R09L'), 0, p) -- ??? ?????
    SetPlayerTechMaxAllowedSwap(FourCC('o04T'), 0, p) -- ?????
    SetPlayerTechMaxAllowedSwap(FourCC('R09P'), 0, p) -- Golem grade
    
    
    SetPlayerTechMaxAllowedSwap(FourCC('n05W'), 0, p) -- Mamont
    SetPlayerTechMaxAllowedSwap(FourCC('n05X'), 0, p) -- Magnatavr
    SetPlayerTechMaxAllowedSwap(FourCC('R0I5'), 0, p) -- Grade
    
    --Loa
    SetPlayerTechMaxAllowedSwap(FourCC('n061'), 0, p)
    SetPlayerTechMaxAllowedSwap(FourCC('n062'), 0, p)
    SetPlayerTechMaxAllowedSwap(FourCC('o05B'), 0, p)
    
    --Loa poglosenie
    SetPlayerTechMaxAllowedSwap(FourCC('R0AI'), 0, p)
    SetPlayerTechMaxAllowedSwap(FourCC('R0AJ'), 0, p)
    SetPlayerTechMaxAllowedSwap(FourCC('R0AD'), 0, p)
    
     
    --Loa altars
    SetPlayerTechMaxAllowedSwap(FourCC('o06J'), 0, p)
    SetPlayerTechMaxAllowedSwap(FourCC('o06K'), 0, p)
    SetPlayerTechMaxAllowedSwap(FourCC('o06I'), 0, p)
    
    SetPlayerTechMaxAllowedSwap(FourCC('O06L'), 1, p) -- Malakk
end
function Trig_IceTrollsStart_Actions()
    ForForce(udg_AllPlayers, IceTrollsStartEach)
end
--===========================================================================
function InitTrig_IceTrollsStart()
    gg_trg_IceTrollsStart=CreateTrigger()
    TriggerRegisterTimerEventSingle(gg_trg_IceTrollsStart, 0.01)
    TriggerAddAction(gg_trg_IceTrollsStart, Trig_IceTrollsStart_Actions)
end
--===========================================================================
-- Trigger: KillLoa
--===========================================================================
function Trig_KillLoa_Actions()
    local p= GetOwningPlayer(GetTriggerUnit())
    SetPlayerTechResearchedSwap(FourCC('R0IX'), 1, p)
    SetPlayerAbilityAvailableBJ(false, FourCC('A1FS'), p)
    SetPlayerAbilityAvailableBJ(false, FourCC('A1FR'), p)
    
    
    SetPlayerTechMaxAllowedSwap(FourCC('n07B'), - 1, p) -- ????????? ???
    SetPlayerTechMaxAllowedSwap(FourCC('R09L'), 2, p) -- ??? ?????
    SetPlayerTechMaxAllowedSwap(FourCC('o04T'), - 1, p) -- Golem
    SetPlayerTechMaxAllowedSwap(FourCC('R09P'), 2, p) -- Golem grade
    
    --Loa grades poglosenie
    SetPlayerTechMaxAllowedSwap(FourCC('R0AI'), 3, p)
    SetPlayerTechMaxAllowedSwap(FourCC('R0AJ'), 3, p)
    SetPlayerTechMaxAllowedSwap(FourCC('R0AD'), 3, p)
    
    
end
--===========================================================================
function InitTrig_KillLoa()
    gg_trg_KillLoa=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_KillLoa, EVENT_PLAYER_UNIT_SPELL_FINISH)
    TriggerAddAction(gg_trg_KillLoa, function()
        if GetSpellAbilityId() ~= FourCC('A1FS') then return end
        Trig_KillLoa_Actions()
    end)
end
--===========================================================================
-- Trigger: ServeLoa
--===========================================================================
function Trig_ServeLoa_Actions()
    local p= GetOwningPlayer(GetTriggerUnit())
    SetPlayerTechResearchedSwap(FourCC('R0IY'), 1, p)
    SetPlayerAbilityAvailableBJ(false, FourCC('A1FS'), p)
    SetPlayerAbilityAvailableBJ(false, FourCC('A1FR'), p)
    
    SetPlayerTechMaxAllowedSwap(FourCC('n05W'), - 1, p) -- Mamont
    SetPlayerTechMaxAllowedSwap(FourCC('n05X'), - 1, p) -- Magnatavr
    SetPlayerTechMaxAllowedSwap(FourCC('R0I5'), 2, p) -- Grade
    
    --Loa
    SetPlayerTechMaxAllowedSwap(FourCC('n061'), 1, p)
    SetPlayerTechMaxAllowedSwap(FourCC('n062'), 1, p)
    SetPlayerTechMaxAllowedSwap(FourCC('o05B'), 1, p)
    
  
       
    --Loa altars
    SetPlayerTechMaxAllowedSwap(FourCC('o06J'), 1, p)
    SetPlayerTechMaxAllowedSwap(FourCC('o06K'), 1, p)
    SetPlayerTechMaxAllowedSwap(FourCC('o06I'), 1, p)
    
end
--===========================================================================
function InitTrig_ServeLoa()
    gg_trg_ServeLoa=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_ServeLoa, EVENT_PLAYER_UNIT_SPELL_FINISH)
    TriggerAddAction(gg_trg_ServeLoa, function()
        if GetSpellAbilityId() ~= FourCC('A1FR') then return end
        Trig_ServeLoa_Actions()
    end)
end
--===========================================================================
-- Trigger: Spell E Copy
--===========================================================================
function Trig_Spell_E_Copy_Actions()
    udg_MUI_E_Glaz=( udg_MUI_E_Glaz + 1 )
    udg_Antibag_E_Glaz[udg_MUI_E_Glaz]=( udg_Antibag_E_Glaz[udg_MUI_E_Glaz] + 1 )
    udg_Cikl_E_Glaz=0
    udg_Dalnost_E_Glaz[udg_MUI_E_Glaz]=0.00
    udg_Caster_E_Glaz[udg_MUI_E_Glaz]=GetTriggerUnit()
    SetUnitPathing(udg_Caster_E_Glaz[udg_MUI_E_Glaz], false)
    PauseUnitBJ(true, udg_Caster_E_Glaz[udg_MUI_E_Glaz])
    SetUnitAnimation(udg_Caster_E_Glaz[udg_MUI_E_Glaz], "attackwalkstandspin")
    udg_Logika_E_Glaz[udg_MUI_E_Glaz]=true
    StartTimerBJ(udg_Timer_E_Glaz, true, 0.03)
end
--===========================================================================
function InitTrig_Spell_E_Copy()
    gg_trg_Spell_E_Copy=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_Spell_E_Copy, EVENT_PLAYER_UNIT_SPELL_EFFECT)
    TriggerAddAction(gg_trg_Spell_E_Copy, function()
        if GetSpellAbilityId() ~= FourCC('A1DA') then return end
        Trig_Spell_E_Copy_Actions()
    end)
end
--===========================================================================
-- Trigger: Spell E Dvij
--===========================================================================
function Trig_Spell_E_Dvij_Func001Func001Func007Func001C()
    return IsUnitEnemy(GetEnumUnit(), GetOwningPlayer(udg_Caster_E_Glaz[udg_Cikl_E_Glaz])) and not (IsUnitAlly(GetEnumUnit(), GetOwningPlayer(udg_Caster_E_Glaz[udg_Cikl_E_Glaz]))) and not (IsUnitInGroup(GetEnumUnit(), udg_Group_E_Glaz[udg_Cikl_E_Glaz])) and not (IsUnitDeadBJ(GetEnumUnit())) and not (IsUnitType(GetEnumUnit(), UNIT_TYPE_STRUCTURE))
end
function Trig_Spell_E_Dvij_Func001Func001Func007A()
    if Trig_Spell_E_Dvij_Func001Func001Func007Func001C() then
        UnitDamageTargetBJ(udg_Caster_E_Glaz[udg_Cikl_E_Glaz], GetEnumUnit(), ( 50.00 * I2R(GetUnitAbilityLevelSwapped(FourCC('A1DA'), udg_Caster_E_Glaz[udg_Cikl_E_Glaz])) ), ATTACK_TYPE_NORMAL, DAMAGE_TYPE_NORMAL)
        GroupAddUnitSimple(GetEnumUnit(), udg_Group_E_Glaz[udg_Cikl_E_Glaz])
    end
end
function Trig_Spell_E_Dvij_Func001Func001Func008Func001C()
    return IsUnitDeadBJ(udg_Caster_E_Glaz[udg_Cikl_E_Glaz]) or (( ( udg_Dalnost_E_Glaz[udg_Cikl_E_Glaz] == 0.20 ) ))
end
function Trig_Spell_E_Dvij_Func001Func001Func008Func008C()
    return udg_Antibag_E_Glaz[udg_MUI_E_Glaz] == 0
end
function Trig_Spell_E_Dvij_Func001Func001Func008C()
    return Trig_Spell_E_Dvij_Func001Func001Func008Func001C()
end
function Trig_Spell_E_Dvij_Func001Func001C()
    return udg_Logika_E_Glaz[udg_Cikl_E_Glaz]
end
function Trig_Spell_E_Dvij_Actions()
    udg_Cikl_E_Glaz=1
    while true do
        if udg_Cikl_E_Glaz > udg_MUI_E_Glaz then break end
        if Trig_Spell_E_Dvij_Func001Func001C() then
            udg_Dalnost_E_Glaz[udg_Cikl_E_Glaz]=( udg_Dalnost_E_Glaz[udg_Cikl_E_Glaz] + 0.02 )
            udg_To4kaCaster_E_Glaz[udg_Cikl_E_Glaz]=GetUnitLoc(udg_Caster_E_Glaz[udg_Cikl_E_Glaz])
            SetUnitPositionLoc(udg_Caster_E_Glaz[udg_Cikl_E_Glaz], PolarProjectionBJ(udg_To4kaCaster_E_Glaz[udg_Cikl_E_Glaz], 60.00, GetUnitFacing(udg_Caster_E_Glaz[udg_Cikl_E_Glaz])))
            AddSpecialEffectLocBJ(udg_To4kaCaster_E_Glaz[udg_Cikl_E_Glaz], "CosmicBall.mdx")
            DestroyEffectBJ(GetLastCreatedEffectBJ())
            bj_wantDestroyGroup=true
            ForGroupBJ(GetUnitsInRangeOfLocAll(150.00, udg_To4kaCaster_E_Glaz[udg_Cikl_E_Glaz]), Trig_Spell_E_Dvij_Func001Func001Func007A)
            if Trig_Spell_E_Dvij_Func001Func001Func008C() then
                GroupClear(udg_Group_E_Glaz[udg_Cikl_E_Glaz])
                SetUnitPathing(udg_Caster_E_Glaz[udg_Cikl_E_Glaz], true)
                PauseUnitBJ(false, udg_Caster_E_Glaz[udg_Cikl_E_Glaz])
                udg_Dalnost_E_Glaz[udg_Cikl_E_Glaz]=0.00
                udg_Logika_E_Glaz[udg_Cikl_E_Glaz]=false
                udg_Antibag_E_Glaz[udg_Cikl_E_Glaz]=( udg_Antibag_E_Glaz[udg_Cikl_E_Glaz] - 1 )
                if Trig_Spell_E_Dvij_Func001Func001Func008Func008C() then
                    PauseTimerBJ(true, udg_Timer_E_Glaz)
                    udg_MUI_E_Glaz=0
                end
            end
            RemoveLocation(udg_To4kaCaster_E_Glaz[udg_Cikl_E_Glaz])
        end
        udg_Cikl_E_Glaz=udg_Cikl_E_Glaz + 1
    end
end
--===========================================================================
function InitTrig_Spell_E_Dvij()
    gg_trg_Spell_E_Dvij=CreateTrigger()
    TriggerRegisterTimerExpireEventBJ(gg_trg_Spell_E_Dvij, udg_Timer_E_Glaz)
    TriggerAddAction(gg_trg_Spell_E_Dvij, Trig_Spell_E_Dvij_Actions)
end
--===========================================================================
-- Trigger: Ini2
--
-- ????????????? ???????????? ?????? ???????? ??? ???? ???????
--===========================================================================
function Trig_Ini2_Actions()
    --call DisplayTextToPlayer(Player(0),0,0,"")
    UnitAddAbility(GetSpellTargetUnit(), FourCC('A0H1'))
end
--===========================================================================
function InitTrig_Ini2()
    gg_trg_Ini2=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_Ini2, EVENT_PLAYER_UNIT_SPELL_EFFECT)
    TriggerAddAction(gg_trg_Ini2, function()
        if GetSpellAbilityId() ~= FourCC('A1DQ') then return end
        Trig_Ini2_Actions()
    end)
end
--===========================================================================
-- Trigger: Spell E2
--===========================================================================
function Trig_Spell_E2_Conditions()
 
    return GetUnitTypeId(GetEventDamageSource()) == FourCC('O04H') and GetUnitAbilityLevel(GetTriggerUnit(), FourCC('A0H1')) > 0
    -- ??? ???????????? ? ???? ????????????
end
function Trig_Spell_E2_Actions()
    local u= GetTriggerUnit()
    DisableTrigger(GetTriggeringTrigger())
    UnitRemoveAbility(u, FourCC('A0H1'))
    --call DisplayTextToPlayer(Player(0),0,0,"")
    udg_To4kaTarget=GetUnitLoc(u)
    UnitDamageTargetBJ(GetEventDamageSource(), u, I2R(GetHeroStatBJ(bj_HEROSTAT_AGI, GetEventDamageSource(), true)), ATTACK_TYPE_HERO, DAMAGE_TYPE_UNIVERSAL)
    AddSpecialEffectLocBJ(udg_To4kaTarget, "AbilitiesSpellsOtherCrushingWaveCrushingWaveDamage.mdl")
    DestroyEffectBJ(GetLastCreatedEffectBJ())
    CreateTextTagLocBJ(( "cff00ff00 .. " .. I2S(GetHeroStatBJ(bj_HEROSTAT_AGI, GetEventDamageSource(), true)) ), udg_To4kaTarget, 140.00, 9.00, 100, 100, 100, 0)
    SetTextTagVelocityBJ(GetLastCreatedTextTag(), 150.00, 90)
    SetTextTagSuspendedBJ(GetLastCreatedTextTag(), false)
    SetTextTagPermanentBJ(GetLastCreatedTextTag(), false)
    SetTextTagLifespanBJ(GetLastCreatedTextTag(), 0.80)
    SetTextTagFadepointBJ(GetLastCreatedTextTag(), 0.80)
    RemoveLocation(udg_To4kaTarget)
    EnableTrigger(GetTriggeringTrigger())
end
--===========================================================================
function InitTrig_Spell_E2()
    gg_trg_Spell_E2=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_Spell_E2, EVENT_PLAYER_UNIT_DAMAGED)
    TriggerAddCondition(gg_trg_Spell_E2, Condition(Trig_Spell_E2_Conditions))
    TriggerAddAction(gg_trg_Spell_E2, Trig_Spell_E2_Actions)
end
--===========================================================================
-- Trigger: HpRegen2
--===========================================================================
function Trig_HpRegen2_Conditions()
    
    return GetUnitAbilityLevel(GetTriggerUnit(), FourCC('A1CA')) > 0 -- ??? ?????? ??????
    
    
end
function Trig_HpRegen2_Actions()
    local u= GetTriggerUnit()
    local spellid= FourCC('A1CY')
    local timerspellid= FourCC('A1CX')
    local lifep= GetUnitLifePercent(u)
    local time= 10
    
    if lifep < 25 then
        UnitAddAbility(u, spellid)
        SetUnitAbilityLevel(u, spellid, 2)
        BlzStartUnitAbilityCooldown(u, timerspellid, 20)
       -- call DisplayTextToPlayer(Player(0),0,0,"25"+R2S(lifep))
    elseif lifep < 50 then
            UnitAddAbility(u, spellid)
            SetUnitAbilityLevel(u, spellid, 1)
            BlzStartUnitAbilityCooldown(u, timerspellid, 20)
     --       call DisplayTextToPlayer(Player(0),0,0,"50"+R2S(lifep))
            
    else
            UnitRemoveAbility(u, spellid)
       --     call DisplayTextToPlayer(Player(0),0,0,""+R2S(lifep))
    end
    UnitAddAbility(u, timerspellid)
    BlzStartUnitAbilityCooldown(u, timerspellid, time)
    TriggerSleepAction(time)
    
    if BlzGetUnitAbilityCooldownRemaining(u, timerspellid) == 0 then
        UnitRemoveAbility(u, spellid)
    end
    
    
    
    u=nil
end
--===========================================================================
function InitTrig_HpRegen2()
    gg_trg_HpRegen2=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_HpRegen2, EVENT_PLAYER_UNIT_ATTACKED)
    TriggerAddCondition(gg_trg_HpRegen2, Condition(Trig_HpRegen2_Conditions))
    TriggerAddAction(gg_trg_HpRegen2, Trig_HpRegen2_Actions)
end
--===========================================================================
-- Trigger: Spell Copy 2 Copy
--===========================================================================
function Trig_Spell_Copy_2_Copy_Conditions()
    return GetLearnedSkillBJ() == FourCC('A1CB')
end
function Trig_Spell_Copy_2_Copy_Actions()
    udg_u=GetLearningUnit()
    TriggerRegisterUnitEvent(gg_trg_Lech, udg_u, EVENT_UNIT_DAMAGED)
    TriggerRegisterUnitEvent(gg_trg_AvtoCast, udg_u, EVENT_UNIT_DAMAGED)
    DisableTrigger(GetTriggeringTrigger())
end
--===========================================================================
function InitTrig_Spell_Copy_2_Copy()
    gg_trg_Spell_Copy_2_Copy=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_Spell_Copy_2_Copy, EVENT_PLAYER_HERO_SKILL)
    TriggerAddCondition(gg_trg_Spell_Copy_2_Copy, Condition(Trig_Spell_Copy_2_Copy_Conditions))
    TriggerAddAction(gg_trg_Spell_Copy_2_Copy, Trig_Spell_Copy_2_Copy_Actions)
end
--===========================================================================
-- Trigger: Lech Copy
--===========================================================================
function Trig_Lech_Copy_Actions()
    SetUnitLifeBJ(udg_u, ( GetUnitStateSwap(UNIT_STATE_LIFE, udg_u) + GetEventDamage() ))
end
--===========================================================================
function InitTrig_Lech_Copy()
    gg_trg_Lech_Copy=CreateTrigger()
    DisableTrigger(gg_trg_Lech_Copy)
    TriggerAddAction(gg_trg_Lech_Copy, Trig_Lech_Copy_Actions)
end
--===========================================================================
-- Trigger: Cast Copy
--===========================================================================
function Trig_Cast_Copy_Actions()
    EnableTrigger(gg_trg_Lech)
    CreateNUnitsAtLoc(1, FourCC('h0ML'), GetOwningPlayer(udg_u), GetUnitLoc(GetSpellAbilityUnit()), bj_UNIT_FACING)
    UnitAddAbilityBJ(FourCC('A1BS'), GetLastCreatedUnit())
    IssueTargetOrderBJ(GetLastCreatedUnit(), "purge", GetSpellAbilityUnit())
    UnitApplyTimedLifeBJ(1.00, FourCC('BTLF'), GetLastCreatedUnit())
    TriggerSleepAction(( 5.00 + ( 1.00 * I2R(GetUnitAbilityLevelSwapped(FourCC('A1CB'), GetSpellAbilityUnit())) ) ))
    DisableTrigger(gg_trg_Lech)
end
--===========================================================================
function InitTrig_Cast_Copy()
    gg_trg_Cast_Copy=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_Cast_Copy, EVENT_PLAYER_UNIT_SPELL_EFFECT)
    TriggerAddAction(gg_trg_Cast_Copy, function()
        if GetSpellAbilityId() ~= FourCC('A1CB') then return end
        Trig_Cast_Copy_Actions()
    end)
end
--===========================================================================
-- Trigger: AvtoCast Copy
--===========================================================================
function Trig_AvtoCast_Copy_Conditions()
    return GetUnitStateSwap(UNIT_STATE_LIFE, udg_u) <= 400.00
end
function Trig_AvtoCast_Copy_Actions()
    IssueImmediateOrderBJ(udg_u, "stomp")
end
--===========================================================================
function InitTrig_AvtoCast_Copy()
    gg_trg_AvtoCast_Copy=CreateTrigger()
    TriggerAddCondition(gg_trg_AvtoCast_Copy, Condition(Trig_AvtoCast_Copy_Conditions))
    TriggerAddAction(gg_trg_AvtoCast_Copy, Trig_AvtoCast_Copy_Actions)
end
--===========================================================================
-- Trigger: DammyDeath Copy
--===========================================================================
function Trig_DammyDeath_Copy_Func001C()
    return GetUnitTypeId(GetDyingUnit()) == FourCC('h0ML')
end
function Trig_DammyDeath_Copy_Actions()
    if Trig_DammyDeath_Copy_Func001C() then
        RemoveUnit(GetDyingUnit())
    end
end
--===========================================================================
function InitTrig_DammyDeath_Copy()
    gg_trg_DammyDeath_Copy=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_DammyDeath_Copy, EVENT_PLAYER_UNIT_DEATH)
    TriggerAddAction(gg_trg_DammyDeath_Copy, Trig_DammyDeath_Copy_Actions)
end
--===========================================================================
-- Trigger: TakenDamage
--===========================================================================
function Trig_TakenDamage_Conditions()
    return GetUnitAbilityLevelSwapped(FourCC('A1CA'), GetTriggerUnit()) == 1
end
function Trig_TakenDamage_Func001Func001C()
    return GetUnitLifePercent(GetTriggerUnit()) < 50.00
end
function Trig_TakenDamage_Func001C()
    return GetUnitLifePercent(GetAttackedUnitBJ()) < 25.00
end
function Trig_TakenDamage_Actions()
    if Trig_TakenDamage_Func001C() then
        UnitAddAbilityBJ(FourCC('A1C9'), GetTriggerUnit())
        SetUnitAbilityLevelSwapped(FourCC('A1C9'), GetTriggerUnit(), 2)
    else
        if Trig_TakenDamage_Func001Func001C() then
            UnitAddAbilityBJ(FourCC('A1C9'), GetTriggerUnit())
            SetUnitAbilityLevelSwapped(FourCC('A1C9'), GetTriggerUnit(), 1)
        else
            UnitRemoveAbilityBJ(FourCC('A1C9'), GetTriggerUnit())
        end
    end
end
--===========================================================================
function InitTrig_TakenDamage()
    gg_trg_TakenDamage=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_TakenDamage, EVENT_PLAYER_UNIT_ATTACKED)
    TriggerAddCondition(gg_trg_TakenDamage, Condition(Trig_TakenDamage_Conditions))
    TriggerAddAction(gg_trg_TakenDamage, Trig_TakenDamage_Actions)
end
--===========================================================================
-- Trigger: LordWave
--===========================================================================
function Trig_LordWave_Func010C()
    return GetSpellAbilityId() == FourCC('NQ02')
end
function Trig_LordWave_Conditions()
    return Trig_LordWave_Func010C()
end
function Trig_LordWave_Func001002003()
    return GetUnitTypeId(GetFilterUnit()) == FourCC('lord')
end
function Trig_LordWave_Func002002003()
    return GetUnitTypeId(GetFilterUnit()) == FourCC('nq01')
end
function Trig_LordWave_Func004A()
    UnitAddAbilityBJ(FourCC('NQ14'), GetEnumUnit())
    SetUnitAbilityLevelSwapped(FourCC('NQ14'), GetEnumUnit(), GetUnitAbilityLevelSwapped(FourCC('NQ14'), GetTriggerUnit()))
    IssuePointOrderLocBJ(GetEnumUnit(), "carrionswarm", GetSpellTargetLoc())
    BlzUnitHideAbility(GetEnumUnit(), FourCC('NQ14'), true)
    DestroyGroup(udg_AllLords)
end
function Trig_LordWave_Func009A()
    UnitRemoveAbilityBJ(FourCC('NQ14'), GetEnumUnit())
    DestroyGroup(udg_AllLords)
end
function Trig_LordWave_Actions()
    udg_AllLords=GetUnitsInRangeOfLocMatching(700.00, GetSpellTargetLoc(), Condition(Trig_LordWave_Func001002003))
    udg_MellLord=GetUnitsInRangeOfLocMatching(700.00, GetSpellTargetLoc(), Condition(Trig_LordWave_Func002002003))
    GroupAddGroup(udg_MellLord, udg_AllLords)
    ForGroupBJ(udg_AllLords, Trig_LordWave_Func004A)
    TriggerSleepAction(6.00)
    udg_AllLords=GetUnitsOfPlayerAndTypeId(GetTriggerPlayer(), FourCC('lord'))
    udg_MellLord=GetUnitsOfPlayerAndTypeId(GetTriggerPlayer(), FourCC('nq01'))
    GroupAddGroup(udg_MellLord, udg_AllLords)
    ForGroupBJ(udg_AllLords, Trig_LordWave_Func009A)
end
--===========================================================================
function InitTrig_LordWave()
    gg_trg_LordWave=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_LordWave, EVENT_PLAYER_UNIT_SPELL_EFFECT)
    TriggerAddCondition(gg_trg_LordWave, Condition(Trig_LordWave_Conditions))
    TriggerAddAction(gg_trg_LordWave, Trig_LordWave_Actions)
end
--===========================================================================
-- Trigger: MassBaff
--===========================================================================
function Trig_MassBaff_Func010C()
    return GetSpellAbilityId() == FourCC('NQ07')
end
function Trig_MassBaff_Conditions()
    return Trig_MassBaff_Func010C()
end
function Trig_MassBaff_Func004A()
    UnitAddAbilityBJ(FourCC('NQ08'), GetEnumUnit())
    SetUnitAbilityLevelSwapped(FourCC('NQ08'), GetEnumUnit(), GetUnitAbilityLevelSwapped(FourCC('NQ07'), GetTriggerUnit()))
    IssueImmediateOrderBJ(GetEnumUnit(), "roar")
    BlzUnitHideAbility(GetEnumUnit(), FourCC('NQ08'), true)
    DestroyGroup(udg_AllLords)
end
function Trig_MassBaff_Func009A()
    UnitRemoveAbilityBJ(FourCC('NQ08'), GetEnumUnit())
    DestroyGroup(udg_AllLords)
end
function Trig_MassBaff_Actions()
    udg_AllLords=GetUnitsOfPlayerAndTypeId(GetTriggerPlayer(), FourCC('lord'))
    udg_MellLord=GetUnitsOfPlayerAndTypeId(GetTriggerPlayer(), FourCC('nq01'))
    GroupAddGroup(udg_MellLord, udg_AllLords)
    ForGroupBJ(udg_AllLords, Trig_MassBaff_Func004A)
    TriggerSleepAction(3.00)
    udg_AllLords=GetUnitsOfPlayerAndTypeId(GetTriggerPlayer(), FourCC('lord'))
    udg_MellLord=GetUnitsOfPlayerAndTypeId(GetTriggerPlayer(), FourCC('nq01'))
    GroupAddGroup(udg_MellLord, udg_AllLords)
    ForGroupBJ(udg_AllLords, Trig_MassBaff_Func009A)
end
--===========================================================================
function InitTrig_MassBaff()
    gg_trg_MassBaff=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_MassBaff, EVENT_PLAYER_UNIT_SPELL_EFFECT)
    TriggerAddCondition(gg_trg_MassBaff, Condition(Trig_MassBaff_Conditions))
    TriggerAddAction(gg_trg_MassBaff, Trig_MassBaff_Actions)
end
--===========================================================================
-- Trigger: LordsAssist
--===========================================================================
function Trig_LordsAssist_Func010C()
    return GetSpellAbilityId() == FourCC('NQ03')
end
function Trig_LordsAssist_Conditions()
    return Trig_LordsAssist_Func010C()
end
function Trig_LordsAssist_Func001002003()
    return GetUnitTypeId(GetFilterUnit()) == FourCC('lord')
end
function Trig_LordsAssist_Func002002003()
    return GetUnitTypeId(GetFilterUnit()) == FourCC('nq01')
end
function Trig_LordsAssist_Func004A()
    UnitAddAbilityBJ(FourCC('NQ09'), GetEnumUnit())
    SetUnitAbilityLevelSwapped(FourCC('NQ09'), GetEnumUnit(), GetUnitAbilityLevelSwapped(FourCC('NQ03'), GetTriggerUnit()))
    IssueTargetOrderBJ(GetEnumUnit(), "manaburn", GetSpellTargetUnit())
    BlzUnitHideAbility(GetEnumUnit(), FourCC('NQ09'), true)
    DestroyGroup(udg_AllLords)
end
function Trig_LordsAssist_Func006002003()
    return GetUnitTypeId(GetFilterUnit()) == FourCC('lord')
end
function Trig_LordsAssist_Func007002003()
    return GetUnitTypeId(GetFilterUnit()) == FourCC('nq01')
end
function Trig_LordsAssist_Func009A()
    UnitRemoveAbilityBJ(FourCC('NQ09'), GetEnumUnit())
    DestroyGroup(udg_AllLords)
end
function Trig_LordsAssist_Actions()
    udg_AllLords=GetUnitsInRangeOfLocMatching(512, GetSpellTargetLoc(), Condition(Trig_LordsAssist_Func001002003))
    udg_MellLord=GetUnitsInRangeOfLocMatching(512, GetSpellTargetLoc(), Condition(Trig_LordsAssist_Func002002003))
    GroupAddGroup(udg_MellLord, udg_AllLords)
    ForGroupBJ(udg_AllLords, Trig_LordsAssist_Func004A)
    TriggerSleepAction(3.00)
    udg_AllLords=GetUnitsInRangeOfLocMatching(512, GetSpellTargetLoc(), Condition(Trig_LordsAssist_Func006002003))
    udg_MellLord=GetUnitsInRangeOfLocMatching(512, GetSpellTargetLoc(), Condition(Trig_LordsAssist_Func007002003))
    GroupAddGroup(udg_MellLord, udg_AllLords)
    ForGroupBJ(udg_AllLords, Trig_LordsAssist_Func009A)
end
--===========================================================================
function InitTrig_LordsAssist()
    gg_trg_LordsAssist=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_LordsAssist, EVENT_PLAYER_UNIT_SPELL_EFFECT)
    TriggerAddCondition(gg_trg_LordsAssist, Condition(Trig_LordsAssist_Conditions))
    TriggerAddAction(gg_trg_LordsAssist, Trig_LordsAssist_Actions)
end
--===========================================================================
-- Trigger: Lord
--===========================================================================
function Trig_Lord_Func001Func001Func001C()
    return (( GetUnitAbilityLevelSwapped(FourCC('NQ06'), GetTriggerUnit()) == 2 )) and (( CountLivingPlayerUnitsOfTypeId(FourCC('lord'), GetTriggerPlayer()) < 3 )) and (( GetUnitTypeId(GetSpellTargetUnit()) == FourCC('u019') ))
end
function Trig_Lord_Func001Func001C()
    return Trig_Lord_Func001Func001Func001C()
end
function Trig_Lord_Func001Func002C()
    return (( GetUnitAbilityLevelSwapped(FourCC('NQ06'), GetTriggerUnit()) == 1 )) and (( CountLivingPlayerUnitsOfTypeId(FourCC('lord'), GetTriggerPlayer()) == 0 )) and (( GetUnitTypeId(GetSpellTargetUnit()) == FourCC('u019') ))
end
function Trig_Lord_Func001C()
    return Trig_Lord_Func001Func002C()
end
function Trig_Lord_Actions()
    if Trig_Lord_Func001C() then
        ReplaceUnitBJ(GetSpellTargetUnit(), FourCC('lorE'), bj_UNIT_STATE_METHOD_DEFAULTS)
        UnitApplyTimedLifeBJ(60.00, FourCC('BTLF'), GetLastReplacedUnitBJ())
    else
        if Trig_Lord_Func001Func001C() then
            ReplaceUnitBJ(GetSpellTargetUnit(), FourCC('lorE'), bj_UNIT_STATE_METHOD_DEFAULTS)
            UnitApplyTimedLifeBJ(60.00, FourCC('BTLF'), GetLastReplacedUnitBJ())
        else
            DoNothing()
        end
    end
end
--===========================================================================
function InitTrig_Lord()
    gg_trg_Lord=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_Lord, EVENT_PLAYER_UNIT_SPELL_EFFECT)
    TriggerAddAction(gg_trg_Lord, function()
        if GetSpellAbilityId() ~= FourCC('NQ06') then return end
        Trig_Lord_Actions()
    end)
end
--===========================================================================
-- Trigger: LordBirth
--===========================================================================
function Trig_LordBirth_Conditions()
    return GetUnitTypeId(GetTriggerUnit()) == FourCC('lorE')
end
function Trig_LordBirth_Actions()
    CreateNUnitsAtLoc(1, FourCC('lord'), GetTriggerPlayer(), GetUnitLoc(GetTriggerUnit()), bj_UNIT_FACING)
end
--===========================================================================
function InitTrig_LordBirth()
    gg_trg_LordBirth=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_LordBirth, EVENT_PLAYER_UNIT_DEATH)
    TriggerAddCondition(gg_trg_LordBirth, Condition(Trig_LordBirth_Conditions))
    TriggerAddAction(gg_trg_LordBirth, Trig_LordBirth_Actions)
end
--===========================================================================
-- Trigger: NaxramasKills
--===========================================================================
function Trig_NaxramasKills_Conditions()
    return GetUnitTypeId(GetTriggerUnit()) == FourCC('e00D')
end
function Trig_NaxramasKills_Func003A()
    KillUnit(GetEnumUnit())
end
function Trig_NaxramasKills_Actions()
    DisplayTextToForce(GetPlayersAll(), "TRIGSTR_3138")
    udg_NaxramasKills=GetUnitsInRectAll(gg_rct_DeathNaxramas)
    ForGroupBJ(udg_NaxramasKills, Trig_NaxramasKills_Func003A)
end
--===========================================================================
function InitTrig_NaxramasKills()
    gg_trg_NaxramasKills=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_NaxramasKills, EVENT_PLAYER_UNIT_DEATH)
    TriggerAddCondition(gg_trg_NaxramasKills, Condition(Trig_NaxramasKills_Conditions))
    TriggerAddAction(gg_trg_NaxramasKills, Trig_NaxramasKills_Actions)
end
--===========================================================================
-- Trigger: DalaranKills
--===========================================================================
function Trig_DalaranKills_Conditions()
    return GetUnitTypeId(GetTriggerUnit()) == FourCC('e00C')
end
function Trig_DalaranKills_Func003A()
    KillUnit(GetEnumUnit())
end
function Trig_DalaranKills_Actions()
    DisplayTextToForce(GetPlayersAll(), "TRIGSTR_3139")
    udg_DalaranKills=GetUnitsInRectAll(gg_rct_DeathDalaran)
    ForGroupBJ(udg_DalaranKills, Trig_DalaranKills_Func003A)
end
--===========================================================================
function InitTrig_DalaranKills()
    gg_trg_DalaranKills=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_DalaranKills, EVENT_PLAYER_UNIT_DEATH)
    TriggerAddCondition(gg_trg_DalaranKills, Condition(Trig_DalaranKills_Conditions))
    TriggerAddAction(gg_trg_DalaranKills, Trig_DalaranKills_Actions)
end
--===========================================================================
-- Trigger: StartUlt
--===========================================================================
function Trig_StartUlt_Func002C()
    return (( GetUnitTypeId(GetTriggerUnit()) == FourCC('MIMH') )) and (( GetSpellAbilityId() == FourCC('MIM6') ))
end
function Trig_StartUlt_Conditions()
    return Trig_StartUlt_Func002C()
end
function Trig_StartUlt_Func001Func001C()
    return (( GetPlayerState(GetTriggerPlayer(), PLAYER_STATE_RESOURCE_GOLD) >= 8000 )) and (( GetPlayerState(GetTriggerPlayer(), PLAYER_STATE_RESOURCE_LUMBER) >= 8000 )) and (( CountLivingPlayerUnitsOfTypeId(FourCC('mim1'), GetTriggerPlayer()) < 2 )) and (( GetUnitAbilityLevelSwapped(FourCC('MIM6'), GetTriggerUnit()) == 2 ))
end
function Trig_StartUlt_Func001C()
    return (( GetPlayerState(GetTriggerPlayer(), PLAYER_STATE_RESOURCE_GOLD) >= 8000 )) and (( GetPlayerState(GetTriggerPlayer(), PLAYER_STATE_RESOURCE_LUMBER) >= 8000 )) and (( CountLivingPlayerUnitsOfTypeId(FourCC('mim1'), GetTriggerPlayer()) < 1 )) and (( GetUnitAbilityLevelSwapped(FourCC('MIM6'), GetTriggerUnit()) == 1 ))
end
function Trig_StartUlt_Actions()
    if Trig_StartUlt_Func001C() then
        SetPlayerStateBJ(GetTriggerPlayer(), PLAYER_STATE_RESOURCE_GOLD, ( GetPlayerState(GetTriggerPlayer(), PLAYER_STATE_RESOURCE_GOLD) - 8000 ))
        SetPlayerStateBJ(GetTriggerPlayer(), PLAYER_STATE_RESOURCE_LUMBER, ( GetPlayerState(GetTriggerPlayer(), PLAYER_STATE_RESOURCE_LUMBER) - 8000 ))
        UnitAddAbilityBJ(FourCC('MIM4'), GetTriggerUnit())
        SetUnitAbilityLevelSwapped(FourCC('MIM4'), GetTriggerUnit(), GetUnitAbilityLevelSwapped(FourCC('MIM6'), GetTriggerUnit()))
        BlzUnitHideAbility(GetTriggerUnit(), FourCC('MIM4'), false)
        SetUnitAnimationWithRarity(GetTriggerUnit(), "Attackspell", RARITY_FREQUENT)
        PauseUnitBJ(true, GetTriggerUnit())
        TriggerSleepAction(50.00)
        PauseUnitBJ(false, GetTriggerUnit())
        IssueImmediateOrderBJ(GetTriggerUnit(), "stomp")
    else
        if Trig_StartUlt_Func001Func001C() then
            SetPlayerStateBJ(GetTriggerPlayer(), PLAYER_STATE_RESOURCE_GOLD, ( GetPlayerState(GetTriggerPlayer(), PLAYER_STATE_RESOURCE_GOLD) - 8000 ))
            SetPlayerStateBJ(GetTriggerPlayer(), PLAYER_STATE_RESOURCE_LUMBER, ( GetPlayerState(GetTriggerPlayer(), PLAYER_STATE_RESOURCE_LUMBER) - 8000 ))
            UnitAddAbilityBJ(FourCC('MIM4'), GetTriggerUnit())
            SetUnitAbilityLevelSwapped(FourCC('MIM4'), GetTriggerUnit(), GetUnitAbilityLevelSwapped(FourCC('MIM6'), GetTriggerUnit()))
            BlzUnitHideAbility(GetTriggerUnit(), FourCC('MIM4'), false)
            PauseUnitBJ(true, GetTriggerUnit())
            TriggerSleepAction(50.00)
            PauseUnitBJ(false, GetTriggerUnit())
            IssueImmediateOrderBJ(GetTriggerUnit(), "stomp")
        else
            DoNothing()
        end
    end
end
--===========================================================================
function InitTrig_StartUlt()
    gg_trg_StartUlt=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_StartUlt, EVENT_PLAYER_UNIT_SPELL_EFFECT)
    TriggerAddCondition(gg_trg_StartUlt, Condition(Trig_StartUlt_Conditions))
    TriggerAddAction(gg_trg_StartUlt, Trig_StartUlt_Actions)
end
--===========================================================================
-- Trigger: UltSummon
--===========================================================================
function Trig_UltSummon_Func003C()
    return (( GetUnitTypeId(GetTriggerUnit()) == FourCC('MIMH') )) and (( GetSpellAbilityId() == FourCC('MIM4') ))
end
function Trig_UltSummon_Conditions()
    return Trig_UltSummon_Func003C()
end
function Trig_UltSummon_Func002Func001C()
    return (( GetUnitAbilityLevelSwapped(FourCC('MIM4'), GetTriggerUnit()) == 2 )) and (( CountLivingPlayerUnitsOfTypeId(FourCC('mim1'), GetTriggerPlayer()) < 2 ))
end
function Trig_UltSummon_Func002C()
    return (( GetUnitAbilityLevelSwapped(FourCC('MIM4'), GetTriggerUnit()) == 1 )) and (( CountLivingPlayerUnitsOfTypeId(FourCC('mim1'), GetTriggerPlayer()) == 0 ))
end
function Trig_UltSummon_Actions()
    if Trig_UltSummon_Func002C() then
        CreateNUnitsAtLoc(1, FourCC('mim1'), GetOwningPlayer(GetTriggerUnit()), GetUnitLoc(GetTriggerUnit()), bj_UNIT_FACING)
        SetUnitAnimation(GetLastCreatedUnit(), "birth")
        UnitRemoveAbilityBJ(FourCC('MIM4'), GetTriggerUnit())
    else
        if Trig_UltSummon_Func002Func001C() then
            CreateNUnitsAtLoc(1, FourCC('mim1'), GetOwningPlayer(GetTriggerUnit()), GetUnitLoc(GetTriggerUnit()), bj_UNIT_FACING)
            SetUnitAnimation(GetLastCreatedUnit(), "birth")
            UnitRemoveAbilityBJ(FourCC('MIM4'), GetTriggerUnit())
        else
            DoNothing()
        end
    end
end
--===========================================================================
function InitTrig_UltSummon()
    gg_trg_UltSummon=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_UltSummon, EVENT_PLAYER_UNIT_SPELL_EFFECT)
    TriggerAddCondition(gg_trg_UltSummon, Condition(Trig_UltSummon_Conditions))
    TriggerAddAction(gg_trg_UltSummon, Trig_UltSummon_Actions)
end
--===========================================================================
-- Trigger: MassHEX
--===========================================================================
function Trig_MassHEX_Func001A()
    CreateNUnitsAtLoc(1, FourCC('repD'), GetTriggerPlayer(), GetUnitLoc(GetEnumUnit()), bj_UNIT_FACING)
    UnitAddAbilityBJ(FourCC('VLJ5'), GetLastCreatedUnit())
    SetUnitAbilityLevelSwapped(FourCC('VLJ5'), GetLastCreatedUnit(), GetUnitAbilityLevelSwapped(FourCC('VLJ1'), GetTriggerUnit()))
    IssueTargetOrderBJ(GetLastCreatedUnit(), "hex", GetEnumUnit())
end
function Trig_MassHEX_Actions()
    ForGroupBJ(GetUnitsInRangeOfLocAll(300.00, GetSpellTargetLoc()), Trig_MassHEX_Func001A)
end
--===========================================================================
function InitTrig_MassHEX()
    gg_trg_MassHEX=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_MassHEX, EVENT_PLAYER_UNIT_SPELL_EFFECT)
    TriggerAddAction(gg_trg_MassHEX, function()
        if GetSpellAbilityId() ~= FourCC('VLJ1') then return end
        Trig_MassHEX_Actions()
    end)
end
--===========================================================================
-- Trigger: SomeVoljinSpell
--===========================================================================
function Trig_SomeVoljinSpell_Actions()
    UnitAddAbilityBJ(FourCC('A0OR'), GetTriggerUnit())
    BlzUnitHideAbility(GetTriggerUnit(), FourCC('A0OR'), true)
    RemoveAbilityTimed(GetTriggerUnit() , FourCC('A0OR') , 15)
end
--===========================================================================
function InitTrig_SomeVoljinSpell()
    gg_trg_SomeVoljinSpell=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_SomeVoljinSpell, EVENT_PLAYER_UNIT_SPELL_EFFECT)
    TriggerAddAction(gg_trg_SomeVoljinSpell, function()
        if GetSpellAbilityId() ~= FourCC('VLJ4') then return end
        Trig_SomeVoljinSpell_Actions()
    end)
end
--===========================================================================
-- Trigger: Kill
--===========================================================================
function Trig_Kill_Func002A()
    local id= GetUnitTypeId(GetEnumUnit())
    if not IsUnitInGroup(GetEnumUnit(), udg_ZahvatBuildings) and GetOwningPlayer(GetEnumUnit()) == GetTriggerPlayer() and not IsUnitInGroup(GetEnumUnit(), udg_StolicaGroups) and id ~= FourCC('e00C') and id ~= FourCC('e00D') then
        KillUnit(GetEnumUnit())
    else
        if IsUnitInGroup(GetEnumUnit(), udg_StolicaGroups) and GetOwningPlayer(GetEnumUnit()) == GetTriggerPlayer() then
            
            if udg_GameMode == 2 then
                SetUnitLifePercentBJ(GetEnumUnit(), 15.00)
            else
                KillUnit(GetEnumUnit())
                udg_LocalPlayer=GetTriggerPlayer()
                ConditionalTriggerExecute(gg_trg_StolicaKill)
            end
        end
    end
end
function Trig_Kill_Actions()
    local p= GetTriggerPlayer()
    local g= CreateGroup()
    GroupEnumUnitsSelected(g, p, nil)
    ForGroup(g, Trig_Kill_Func002A)
    DestroyGroup(g)
    g=nil
    p=nil
end
--===========================================================================
function InitTrig_Kill()
    gg_trg_Kill=CreateTrigger()
    TriggerRegisterPlayerChatEvent(gg_trg_Kill, Player(0), " - kill", true)
    TriggerRegisterPlayerChatEvent(gg_trg_Kill, Player(1), " - kill", true)
    TriggerRegisterPlayerChatEvent(gg_trg_Kill, Player(2), " - kill", true)
    TriggerRegisterPlayerChatEvent(gg_trg_Kill, Player(3), " - kill", true)
    TriggerRegisterPlayerChatEvent(gg_trg_Kill, Player(4), " - kill", true)
    TriggerRegisterPlayerChatEvent(gg_trg_Kill, Player(5), " - kill", true)
    TriggerRegisterPlayerChatEvent(gg_trg_Kill, Player(6), " - kill", true)
    TriggerRegisterPlayerChatEvent(gg_trg_Kill, Player(7), " - kill", true)
    TriggerRegisterPlayerChatEvent(gg_trg_Kill, Player(8), " - kill", true)
    TriggerRegisterPlayerChatEvent(gg_trg_Kill, Player(9), " - kill", true)
    TriggerRegisterPlayerChatEvent(gg_trg_Kill, Player(10), " - kill", true)
    TriggerRegisterPlayerChatEvent(gg_trg_Kill, Player(11), " - kill", true)
    TriggerRegisterPlayerChatEvent(gg_trg_Kill, Player(12), " - kill", true)
    TriggerRegisterPlayerChatEvent(gg_trg_Kill, Player(13), " - kill", true)
    TriggerRegisterPlayerChatEvent(gg_trg_Kill, Player(14), " - kill", true)
    TriggerRegisterPlayerChatEvent(gg_trg_Kill, Player(15), " - kill", true)
    TriggerRegisterPlayerChatEvent(gg_trg_Kill, Player(16), " - kill", true)
    TriggerRegisterPlayerChatEvent(gg_trg_Kill, Player(17), " - kill", true)
    TriggerRegisterPlayerChatEvent(gg_trg_Kill, Player(18), " - kill", true)
    TriggerRegisterPlayerChatEvent(gg_trg_Kill, Player(19), " - kill", true)
    TriggerRegisterPlayerChatEvent(gg_trg_Kill, Player(20), " - kill", true)
    TriggerRegisterPlayerChatEvent(gg_trg_Kill, Player(21), " - kill", true)
    TriggerRegisterPlayerChatEvent(gg_trg_Kill, Player(22), " - kill", true)
    TriggerRegisterPlayerChatEvent(gg_trg_Kill, Player(23), " - kill", true)
    TriggerAddAction(gg_trg_Kill, Trig_Kill_Actions)
end
--===========================================================================
-- Trigger: Rep
--===========================================================================
function RepConditions()
    if GetOwningPlayer(GetEnumUnit()) == GetTriggerPlayer() and not IsUnitType(GetEnumUnit(), UNIT_TYPE_STRUCTURE) then
        
        ReplaceUnit2(GetEnumUnit() , GetUnitTypeId(GetEnumUnit()) , bj_UNIT_STATE_METHOD_RELATIVE)
    end
end
function Trig_Rep_Actions()
    local p= GetTriggerPlayer()
    local g= CreateGroup()
    GroupEnumUnitsSelected(g, p, nil)
    ForGroup(g, RepConditions)
    DestroyGroup(g)
    g=nil
    p=nil
end
--===========================================================================
function InitTrig_Rep()
    gg_trg_Rep=CreateTrigger()
    TriggerRegisterPlayerChatEvent(gg_trg_Rep, Player(0), " - rep", true)
    TriggerRegisterPlayerChatEvent(gg_trg_Rep, Player(1), " - rep", true)
    TriggerRegisterPlayerChatEvent(gg_trg_Rep, Player(2), " - rep", true)
    TriggerRegisterPlayerChatEvent(gg_trg_Rep, Player(3), " - rep", true)
    TriggerRegisterPlayerChatEvent(gg_trg_Rep, Player(4), " - rep", true)
    TriggerRegisterPlayerChatEvent(gg_trg_Rep, Player(5), " - rep", true)
    TriggerRegisterPlayerChatEvent(gg_trg_Rep, Player(6), " - rep", true)
    TriggerRegisterPlayerChatEvent(gg_trg_Rep, Player(7), " - rep", true)
    TriggerRegisterPlayerChatEvent(gg_trg_Rep, Player(8), " - rep", true)
    TriggerRegisterPlayerChatEvent(gg_trg_Rep, Player(9), " - rep", true)
    TriggerRegisterPlayerChatEvent(gg_trg_Rep, Player(10), " - rep", true)
    TriggerRegisterPlayerChatEvent(gg_trg_Rep, Player(11), " - rep", true)
    TriggerRegisterPlayerChatEvent(gg_trg_Rep, Player(12), " - rep", true)
    TriggerRegisterPlayerChatEvent(gg_trg_Rep, Player(13), " - rep", true)
    TriggerRegisterPlayerChatEvent(gg_trg_Rep, Player(14), " - rep", true)
    TriggerRegisterPlayerChatEvent(gg_trg_Rep, Player(15), " - rep", true)
    TriggerRegisterPlayerChatEvent(gg_trg_Rep, Player(16), " - rep", true)
    TriggerRegisterPlayerChatEvent(gg_trg_Rep, Player(17), " - rep", true)
    TriggerRegisterPlayerChatEvent(gg_trg_Rep, Player(18), " - rep", true)
    TriggerRegisterPlayerChatEvent(gg_trg_Rep, Player(19), " - rep", true)
    TriggerRegisterPlayerChatEvent(gg_trg_Rep, Player(20), " - rep", true)
    TriggerRegisterPlayerChatEvent(gg_trg_Rep, Player(21), " - rep", true)
    TriggerRegisterPlayerChatEvent(gg_trg_Rep, Player(22), " - rep", true)
    TriggerRegisterPlayerChatEvent(gg_trg_Rep, Player(23), " - rep", true)
    TriggerAddAction(gg_trg_Rep, Trig_Rep_Actions)
end
--===========================================================================
-- Trigger: StolicaKill
--===========================================================================
function Trig_StolicaKill_Actions()
    -- ??????? ???????? ??????????. ?? ????????!
end
--===========================================================================
function InitTrig_StolicaKill()
    gg_trg_StolicaKill=CreateTrigger()
    TriggerAddAction(gg_trg_StolicaKill, Trig_StolicaKill_Actions)
end
--===========================================================================
-- Trigger: Camera command O
--===========================================================================
function Trig_Camera_command_O_Actions()
    udg_wawt=S2R(SubStringBJ(GetEventPlayerChatString(), 6, 9))
    SetCameraFieldForPlayer(GetTriggerPlayer(), CAMERA_FIELD_TARGET_DISTANCE, udg_wawt, 1.00)
end
--===========================================================================
function InitTrig_Camera_command_O()
    gg_trg_Camera_command_O=CreateTrigger()
    TriggerRegisterPlayerChatEvent(gg_trg_Camera_command_O, Player(0), " - cam", false)
    TriggerRegisterPlayerChatEvent(gg_trg_Camera_command_O, Player(1), " - cam", false)
    TriggerRegisterPlayerChatEvent(gg_trg_Camera_command_O, Player(2), " - cam", false)
    TriggerRegisterPlayerChatEvent(gg_trg_Camera_command_O, Player(3), " - cam", false)
    TriggerRegisterPlayerChatEvent(gg_trg_Camera_command_O, Player(4), " - cam", false)
    TriggerRegisterPlayerChatEvent(gg_trg_Camera_command_O, Player(5), " - cam", false)
    TriggerRegisterPlayerChatEvent(gg_trg_Camera_command_O, Player(6), " - cam", false)
    TriggerRegisterPlayerChatEvent(gg_trg_Camera_command_O, Player(7), " - cam", false)
    TriggerRegisterPlayerChatEvent(gg_trg_Camera_command_O, Player(8), " - cam", false)
    TriggerRegisterPlayerChatEvent(gg_trg_Camera_command_O, Player(9), " - cam", false)
    TriggerRegisterPlayerChatEvent(gg_trg_Camera_command_O, Player(10), " - cam", false)
    TriggerRegisterPlayerChatEvent(gg_trg_Camera_command_O, Player(11), " - cam", false)
    TriggerRegisterPlayerChatEvent(gg_trg_Camera_command_O, Player(12), " - cam", false)
    TriggerRegisterPlayerChatEvent(gg_trg_Camera_command_O, Player(13), " - cam", false)
    TriggerRegisterPlayerChatEvent(gg_trg_Camera_command_O, Player(14), " - cam", false)
    TriggerRegisterPlayerChatEvent(gg_trg_Camera_command_O, Player(15), " - cam", false)
    TriggerRegisterPlayerChatEvent(gg_trg_Camera_command_O, Player(16), " - cam", false)
    TriggerRegisterPlayerChatEvent(gg_trg_Camera_command_O, Player(17), " - cam", false)
    TriggerRegisterPlayerChatEvent(gg_trg_Camera_command_O, Player(18), " - cam", false)
    TriggerRegisterPlayerChatEvent(gg_trg_Camera_command_O, Player(19), " - cam", false)
    TriggerRegisterPlayerChatEvent(gg_trg_Camera_command_O, Player(20), " - cam", false)
    TriggerRegisterPlayerChatEvent(gg_trg_Camera_command_O, Player(21), " - cam", false)
    TriggerRegisterPlayerChatEvent(gg_trg_Camera_command_O, Player(22), " - cam", false)
    TriggerRegisterPlayerChatEvent(gg_trg_Camera_command_O, Player(23), " - cam", false)
    TriggerAddAction(gg_trg_Camera_command_O, Trig_Camera_command_O_Actions)
end
--===========================================================================
-- Trigger: Name command O
--===========================================================================
function Trig_Name_command_O_Conditions()
    return SubStringBJ(GetEventPlayerChatString(), 1, 6) == " - name"
end
function Trig_Name_command_O_Actions()
    local i= GetPlayerId(GetTriggerPlayer())
    local ownerIndex
    udg_LocalText2=GetEventPlayerChatString()
    udg_LocalText2=SubStringBJ(udg_LocalText2, 7, 50)
    SetPlayerName(GetTriggerPlayer(), udg_LocalText2)
    ownerIndex=EnsureMultiboardPlayerRow(i)
    udg_LocalText2=I2S(GetConvertedPlayerId(GetTriggerPlayer())) .. "." .. udg_LocalText2
    if ownerIndex ~= nil then
        MultiboardSetItemValue(MultiboardItem[ownerIndex * 2 + 0], udg_LocalText2)
    end
    i=0
end
--===========================================================================
function InitTrig_Name_command_O()
    gg_trg_Name_command_O=CreateTrigger()
    TriggerRegisterPlayerChatEvent(gg_trg_Name_command_O, Player(0), " - name", false)
    TriggerRegisterPlayerChatEvent(gg_trg_Name_command_O, Player(1), " - name", false)
    TriggerRegisterPlayerChatEvent(gg_trg_Name_command_O, Player(2), " - name", false)
    TriggerRegisterPlayerChatEvent(gg_trg_Name_command_O, Player(3), " - name", false)
    TriggerRegisterPlayerChatEvent(gg_trg_Name_command_O, Player(4), " - name", false)
    TriggerRegisterPlayerChatEvent(gg_trg_Name_command_O, Player(5), " - name", false)
    TriggerRegisterPlayerChatEvent(gg_trg_Name_command_O, Player(6), " - name", false)
    TriggerRegisterPlayerChatEvent(gg_trg_Name_command_O, Player(7), " - name", false)
    TriggerRegisterPlayerChatEvent(gg_trg_Name_command_O, Player(8), " - name", false)
    TriggerRegisterPlayerChatEvent(gg_trg_Name_command_O, Player(9), " - name", false)
    TriggerRegisterPlayerChatEvent(gg_trg_Name_command_O, Player(10), " - name", false)
    TriggerRegisterPlayerChatEvent(gg_trg_Name_command_O, Player(11), " - name", false)
    TriggerRegisterPlayerChatEvent(gg_trg_Name_command_O, Player(12), " - name", false)
    TriggerRegisterPlayerChatEvent(gg_trg_Name_command_O, Player(13), " - name", false)
    TriggerRegisterPlayerChatEvent(gg_trg_Name_command_O, Player(14), " - name", false)
    TriggerRegisterPlayerChatEvent(gg_trg_Name_command_O, Player(15), " - name", false)
    TriggerRegisterPlayerChatEvent(gg_trg_Name_command_O, Player(16), " - name", false)
    TriggerRegisterPlayerChatEvent(gg_trg_Name_command_O, Player(17), " - name", false)
    TriggerRegisterPlayerChatEvent(gg_trg_Name_command_O, Player(18), " - name", false)
    TriggerRegisterPlayerChatEvent(gg_trg_Name_command_O, Player(20), " - name", false)
    TriggerRegisterPlayerChatEvent(gg_trg_Name_command_O, Player(19), " - name", false)
    TriggerRegisterPlayerChatEvent(gg_trg_Name_command_O, Player(21), " - name", false)
    TriggerRegisterPlayerChatEvent(gg_trg_Name_command_O, Player(22), " - name", false)
    TriggerRegisterPlayerChatEvent(gg_trg_Name_command_O, Player(23), " - name", false)
    TriggerAddCondition(gg_trg_Name_command_O, Condition(Trig_Name_command_O_Conditions))
    TriggerAddAction(gg_trg_Name_command_O, Trig_Name_command_O_Actions)
end
--===========================================================================
-- Trigger: UName command
--===========================================================================
function Trig_UName_command_Conditions()
    return SubStringBJ(GetEventPlayerChatString(), 1, 7) == " - uname"
end
function Trig_UName_command_Actions()
    local i= GetPlayerId(GetTriggerPlayer())
    local u
    local g= CreateGroup()
    udg_LocalText2=GetEventPlayerChatString()
    udg_LocalText2=SubStringBJ(udg_LocalText2, 7, 50)
    
    SyncSelections()
    GroupEnumUnitsSelected(g, GetTriggerPlayer(), nil)
    while true do
        u=FirstOfGroup(g)
        if u == nil then break end
        BlzSetUnitName(u, udg_LocalText2)
        
        GroupRemoveUnit(g, u)
    
    end
    
    
    
    DestroyGroup(g)
    g=nil
    u=nil
end
--===========================================================================
function InitTrig_UName_command()
    local i= 0
    gg_trg_UName_command=CreateTrigger()
    
    while true do
        if i > 23 then break end
        TriggerRegisterPlayerChatEvent(gg_trg_UName_command, Player(i), " - uname", false)
    
        
        
        
        i=i + 1
    end
    TriggerAddCondition(gg_trg_UName_command, Condition(Trig_UName_command_Conditions))
    TriggerAddAction(gg_trg_UName_command, Trig_UName_command_Actions)
end
--===========================================================================
-- Trigger: SecondChance
--===========================================================================
function Trig_SecondChance_Func003Func007001002()
    return IsUnitType(GetFilterUnit(), UNIT_TYPE_HERO)
end
function Trig_SecondChance_Func003Func007A()
    local u= GetEnumUnit()
    local p= GetOwningPlayer(u)
    local id= GetUnitTypeId(u)
    RemoveUnit(u)
    SetPlayerTechMaxAllowed(p, id, GetPlayerTechMaxAllowed(p, id) + 1)
    p=nil
    u=nil
end
function Trig_SecondChance_Func003Func008C()
    if not ( udg_LocalInteger >= 1 ) then
        return false
    end
    if not ( udg_LocalInteger <= 24 ) then
        return false
    end
   
    if IsPlayerInForce(ConvertedPlayer(udg_LocalInteger), Observers) then
        DisplayTimedTextToForce(GetPlayersAll(), 5.00, ( ( "" .. GetPlayerName(GetTriggerPlayer()) ) .. ( "" .. ( GetPlayerName(ConvertedPlayer(udg_LocalInteger)) .. " not " ) ) ))
        return false
    end
    return true
end
function Trig_SecondChance_Func003C()
    return Trig_SecondChance_Func003Func008C()
end
function SecondChanceTimer()
    local t= GetExpiredTimer()
    
    CheckAndCreateCapital(LoadPlayerHandle(Hash, GetHandleId(t), 0))
    FlushChildHashtable(Hash, GetHandleId(t))
    
    DestroyTimer(t)
    t=nil
end
function Trig_SecondChance_Actions()
    local t= SecondChance[GetPlayerId(ConvertedPlayer(udg_LocalInteger))]
    udg_LocalText2=SubStringBJ(GetEventPlayerChatString(), 12, 13)
    udg_LocalInteger=S2I(udg_LocalText2)
    ProbeLogWrite("[CHAT] -raceselect target=" .. tostring(udg_LocalInteger))
    if Trig_SecondChance_Func003C() then
        udg_LocalPosition2=(StartLoc[GetRandomInt(0, StartLocCount - 1)]) -- INLINED!!
        DisplayTimedTextToForce(GetPlayersAll(), 5.00, "???? " .. GetPlayerName(GetTriggerPlayer()) .. " ??? ?????? " .. GetPlayerName(ConvertedPlayer(udg_LocalInteger)) .. " ?????? ????!")
        DisplayTimedTextToPlayer(ConvertedPlayer(udg_LocalInteger), 0, 0, 15.00, "? ??? ???? 15 ????? ?? ??, ????? ????????? ???????!")
        CreateNUnitsAtLoc(1, FourCC('h0HJ'), ConvertedPlayer(udg_LocalInteger), udg_LocalPosition2, bj_UNIT_FACING)
        SetPlayerStateBJ(ConvertedPlayer(udg_LocalInteger), PLAYER_STATE_RESOURCE_GOLD, 5000)
        SetPlayerStateBJ(ConvertedPlayer(udg_LocalInteger), PLAYER_STATE_RESOURCE_LUMBER, 5000)
        
        ForGroupBJ(GetUnitsOfPlayerMatching(ConvertedPlayer(udg_LocalInteger), Condition(Trig_SecondChance_Func003Func007001002)), Trig_SecondChance_Func003Func007A)
    
        if udg_GameMode == 1 or udg_GameMode == 2 then
            if t == nil then
                t=CreateTimer()
                SecondChance[GetPlayerId(ConvertedPlayer(udg_LocalInteger))]=t
            end
            TimerStart(t, 60 * 15, false, SecondChanceTimer)
            SavePlayerHandle(Hash, GetHandleId(t), 0, ConvertedPlayer(udg_LocalInteger))
        end
    end
    t=nil
end
--===========================================================================
function InitTrig_SecondChance()
    gg_trg_SecondChance=CreateTrigger()
    TriggerRegisterPlayerChatEvent(gg_trg_SecondChance, Player(0), "-raceselect", false)
    TriggerAddAction(gg_trg_SecondChance, Trig_SecondChance_Actions)
end
function BridgeRaceSelect(target_index)
    local target_player = ConvertedPlayer(target_index)
    local t = SecondChance[GetPlayerId(target_player)]
    udg_LocalPosition2=(StartLoc[GetRandomInt(0, StartLocCount - 1)])
    DisplayTimedTextToForce(GetPlayersAll(), 5.00, "Bridge gave player " .. GetPlayerName(target_player) .. " race selection")
    DisplayTimedTextToPlayer(target_player, 0, 0, 15.00, "You have 15 minutes to place your capital")
    CreateNUnitsAtLoc(1, FourCC('h0HJ'), target_player, udg_LocalPosition2, bj_UNIT_FACING)
    SetPlayerStateBJ(target_player, PLAYER_STATE_RESOURCE_GOLD, 5000)
    SetPlayerStateBJ(target_player, PLAYER_STATE_RESOURCE_LUMBER, 5000)
    udg_LocalInteger = target_index
    ForGroupBJ(GetUnitsOfPlayerMatching(target_player, Condition(Trig_SecondChance_Func003Func007001002)), Trig_SecondChance_Func003Func007A)
    if udg_GameMode == 1 or udg_GameMode == 2 then
        if t == nil then
            t=CreateTimer()
            SecondChance[GetPlayerId(target_player)]=t
        end
        TimerStart(t, 60 * 15, false, SecondChanceTimer)
        SavePlayerHandle(Hash, GetHandleId(t), 0, target_player)
    end
    ProbeLogWrite("[BRIDGE] race_select target=" .. tostring(target_index))
    target_player = nil
    t = nil
end
--===========================================================================
-- Trigger: GG
--===========================================================================
function Trig_GG_Func004A()
    local u= GetEnumUnit()
    local id= GetUnitTypeId(u)
    local p= GetOwningPlayer(u)
    if IsUnitInGroup(u, udg_ZahvatBuildings) then
        SetUnitOwner(u, Player(25), true)
    else
        KillUnit(u)
        RemoveUnit(u)
        if IsUnitType(GetTriggerUnit(), UNIT_TYPE_HERO) then
            SetPlayerTechMaxAllowed(p, id, GetPlayerTechMaxAllowed(p, id) + 1)
        end
    end
    u=nil
    p=nil
end
function Trig_GG_Actions()
    --local integer pi = GetPlayerId(GetTriggerPlayer())
    DisplayTextToForce(udg_AllPlayers, ( GetPlayerName(GetTriggerPlayer()) .. "cffff0000 - r" ))
    --call GroupEnumUnitsOfPlayer( udg_LocalOtrad2, GetTriggerPlayer(), null )
    --call ForGroupBJ( udg_LocalOtrad2, function Trig_GG_Func004A )
    --call ForForce(Vassals[pi], function Freedom)
    ClearPlayer(GetTriggerPlayer())
    
end
--===========================================================================
function InitTrig_GG()
    gg_trg_GG=CreateTrigger()
    TriggerRegisterPlayerChatEvent(gg_trg_GG, Player(0), " - gg", true)
    TriggerRegisterPlayerChatEvent(gg_trg_GG, Player(1), " - gg", true)
    TriggerRegisterPlayerChatEvent(gg_trg_GG, Player(2), " - gg", true)
    TriggerRegisterPlayerChatEvent(gg_trg_GG, Player(3), " - gg", true)
    TriggerRegisterPlayerChatEvent(gg_trg_GG, Player(4), " - gg", true)
    TriggerRegisterPlayerChatEvent(gg_trg_GG, Player(5), " - gg", true)
    TriggerRegisterPlayerChatEvent(gg_trg_GG, Player(6), " - gg", true)
    TriggerRegisterPlayerChatEvent(gg_trg_GG, Player(7), " - gg", true)
    TriggerRegisterPlayerChatEvent(gg_trg_GG, Player(8), " - gg", true)
    TriggerRegisterPlayerChatEvent(gg_trg_GG, Player(9), " - gg", true)
    TriggerRegisterPlayerChatEvent(gg_trg_GG, Player(10), " - gg", true)
    TriggerRegisterPlayerChatEvent(gg_trg_GG, Player(11), " - gg", true)
    TriggerRegisterPlayerChatEvent(gg_trg_GG, Player(12), " - gg", true)
    TriggerRegisterPlayerChatEvent(gg_trg_GG, Player(13), " - gg", true)
    TriggerRegisterPlayerChatEvent(gg_trg_GG, Player(15), " - gg", true)
    TriggerRegisterPlayerChatEvent(gg_trg_GG, Player(14), " - gg", true)
    TriggerRegisterPlayerChatEvent(gg_trg_GG, Player(16), " - gg", true)
    TriggerRegisterPlayerChatEvent(gg_trg_GG, Player(17), " - gg", true)
    TriggerRegisterPlayerChatEvent(gg_trg_GG, Player(18), " - gg", true)
    TriggerRegisterPlayerChatEvent(gg_trg_GG, Player(19), " - gg", true)
    TriggerRegisterPlayerChatEvent(gg_trg_GG, Player(20), " - gg", true)
    TriggerRegisterPlayerChatEvent(gg_trg_GG, Player(21), " - gg", true)
    TriggerRegisterPlayerChatEvent(gg_trg_GG, Player(22), " - gg", true)
    TriggerRegisterPlayerChatEvent(gg_trg_GG, Player(23), " - gg", true)
    TriggerRegisterPlayerChatEvent(gg_trg_GG, Player(24), " - gg", true)
    
    
    TriggerAddAction(gg_trg_GG, Trig_GG_Actions)
end
--===========================================================================
-- Trigger: Observer
--===========================================================================
function Trig_Untitled_Trigger_006_Func003A()
    SetPlayerAllianceStateBJ(GetEnumPlayer(), udg_LocalPlayer, bj_ALLIANCE_UNALLIED)
    SetPlayerAllianceStateBJ(udg_LocalPlayer, GetEnumPlayer(), bj_ALLIANCE_UNALLIED)
end
function Trig_Observer_Actions()
    local pi= GetPlayerId(GetTriggerPlayer())
    DisplayTextToPlayer(GetTriggerPlayer(), 0, 0, "")
    ClearPlayer(GetTriggerPlayer())
    ForceAddPlayer(Observers, GetTriggerPlayer())
    udg_Visibl[pi]=CreateFogModifierRectBJ(true, GetTriggerPlayer(), FOG_OF_WAR_VISIBLE, bj_mapInitialPlayableArea)
    
    udg_LocalPlayer=GetTriggerPlayer()
    ForForce(udg_AllPlayers, Trig_Untitled_Trigger_006_Func003A)
   
end
--===========================================================================
function InitTrig_Observer()
    local i= 0
    gg_trg_Observer=CreateTrigger()
    while true do
        if i > 23 then break end
        
        TriggerRegisterPlayerChatEvent(gg_trg_Observer, Player(i), " - observer", true)
        
        i=i + 1
    end
    TriggerAddAction(gg_trg_Observer, Trig_Observer_Actions)
end
--===========================================================================
-- Trigger: NoChangeAlly
--===========================================================================
function Trig_NoChangeAlly_Conditions()
    return IsPlayerInForce(GetTriggerPlayer(), Observers)
end
function Trig_NoChangeAlly_Actions()
    udg_LocalPlayer=GetTriggerPlayer()
    ForForce(udg_AllPlayers, Trig_Untitled_Trigger_006_Func003A)
end
--===========================================================================
function InitTrig_NoChangeAlly()
    gg_trg_NoChangeAlly=CreateTrigger()
    TriggerRegisterPlayerEventAllianceChanged(gg_trg_NoChangeAlly, Player(0))
    TriggerAddCondition(gg_trg_NoChangeAlly, Condition(Trig_NoChangeAlly_Conditions))
    TriggerAddAction(gg_trg_NoChangeAlly, Trig_NoChangeAlly_Actions)
end
--===========================================================================
-- Trigger: ObserverOff
--===========================================================================
function Trig_ObserverOff_Actions()
    local pi= GetPlayerId(GetTriggerPlayer())
    DisplayTextToPlayer(GetTriggerPlayer(), 0, 0, "")
    
    ForceRemovePlayer(Observers, GetTriggerPlayer())
    FogModifierStop(udg_Visibl[pi])
    DestroyFogModifier(udg_Visibl[pi])
    
   
   
end
--===========================================================================
function InitTrig_ObserverOff()
    local i= 0
    gg_trg_ObserverOff=CreateTrigger()
    while true do
        if i > 23 then break end
        
        TriggerRegisterPlayerChatEvent(gg_trg_ObserverOff, Player(i), " - observeroff", true)
        
        i=i + 1
    end
    TriggerAddAction(gg_trg_ObserverOff, Trig_ObserverOff_Actions)
end
--===========================================================================
-- Trigger: Hunter
--===========================================================================
function Trig_Hunter_Conditions()
    return CountUnitsInGroup(GetUnitsInRectOfPlayer(gg_rct_Region_112, GetTriggerPlayer())) ~= 0
end
function Trig_Hunter_Actions()
    CreateNUnitsAtLoc(1, FourCC('h0NY'), Player(PLAYER_NEUTRAL_AGGRESSIVE), GetRectCenter(gg_rct_Region_112), bj_UNIT_FACING)
    DisplayTextToForce(GetForceOfPlayer(GetTriggerPlayer()), "TRIGSTR_5829")
    DisableTrigger(gg_trg_Hunter)
end
--===========================================================================
function InitTrig_Hunter()
    local i= 0
    gg_trg_Hunter=CreateTrigger()
    while true do
        if i >= 24 then break end
        TriggerRegisterPlayerChatEvent(gg_trg_Hunter, Player(i), " - s", true)
        i=i + 1
    
    end
    
    TriggerAddCondition(gg_trg_Hunter, Condition(Trig_Hunter_Conditions))
    TriggerAddAction(gg_trg_Hunter, Trig_Hunter_Actions)
end
--===========================================================================
-- Trigger: ArchontMode
--===========================================================================
function CorrectNumber()
    return pi2 >= 0 and pi2 <= 24
end
function Trig_ArchontMode_Actions()
    local s= SubStringBJ(GetEventPlayerChatString(), 8, 10)
    local pi2= S2I(s) - 1
    local pi1= GetPlayerId(GetTriggerPlayer())
    if CorrectNumber(pi2) then
        DisplayTextToPlayer(Player(pi1), 0, 0, "" .. GetPlayerName(Player(pi2)) .. "" .. I2S(pi2))
        DisplayTextToPlayer(Player(pi2), 0, 0, "" .. GetPlayerName(Player(pi1)))
        SetPlayerAllianceStateBJ(Player(pi1), Player(pi2), bj_ALLIANCE_ALLIED_ADVUNITS)
    end
    MultiboardAllowDisplayBJ(true)
end
--===========================================================================
function InitTrig_ArchontMode()
    local i= 0
    gg_trg_ArchontMode=CreateTrigger()
    while true do
        if i > 23 then break end
        
        TriggerRegisterPlayerChatEvent(gg_trg_ArchontMode, Player(i), " - arhont", false)
        
        i=i + 1
    end
    
    TriggerAddAction(gg_trg_ArchontMode, Trig_ArchontMode_Actions)
end
--===========================================================================
-- Trigger: Untitled Trigger 001
--===========================================================================
function Trig_Untitled_Trigger_001_Actions()
    MultiboardDisplayBJ(false, GetLastCreatedMultiboard())
    MultiboardDisplayBJ(true, Multiboard)
    TriggerSleepAction(7)
    MultiboardDisplayBJ(true, GetLastCreatedMultiboard())
end
--===========================================================================
function InitTrig_Untitled_Trigger_001()
    gg_trg_Untitled_Trigger_001=CreateTrigger()
    TriggerRegisterPlayerChatEvent(gg_trg_Untitled_Trigger_001, Player(0), "A3", true)
    TriggerAddAction(gg_trg_Untitled_Trigger_001, Trig_Untitled_Trigger_001_Actions)
end
--===========================================================================
-- Trigger: ArchontModeOff
--===========================================================================
function Trig_ArchontModeOff_Actions()
    local s= SubStringBJ(GetEventPlayerChatString(), 8, 10)
    local pi2= S2I(s) - 1
    local pi1= GetPlayerId(GetTriggerPlayer())
    if CorrectNumber(pi2) and DipMode ~= 1 then
        DisplayTextToPlayer(Player(pi1), 0, 0, "" .. GetPlayerName(Player(pi2)) .. "" .. I2S(pi2))
        DisplayTextToPlayer(Player(pi1), 0, 0, "" .. GetPlayerName(Player(pi1)))
        SetPlayerAllianceBJ(Player(pi1), ALLIANCE_SHARED_ADVANCED_CONTROL, false, Player(pi2))
    end
   
end
--===========================================================================
function InitTrig_ArchontModeOff()
    local i= 0
    gg_trg_ArchontModeOff=CreateTrigger()
    while true do
        if i > 23 then break end
        
        TriggerRegisterPlayerChatEvent(gg_trg_ArchontModeOff, Player(i), " - arhoff", false)
        
        i=i + 1
    end
    
    TriggerAddAction(gg_trg_ArchontModeOff, Trig_ArchontModeOff_Actions)
end
--===========================================================================
-- Trigger: ForSoldUnitsSelect
--===========================================================================
function Trig_ForSoldUnitsSelect_Conditions()
    return GetUnitAbilityLevel(GetTriggerUnit(), FourCC('Asud')) > 0 and GetPlayerAlliance(GetOwningPlayer(GetTriggerUnit()), GetTriggerPlayer(), ALLIANCE_SHARED_ADVANCED_CONTROL)
end
function Trig_ForSoldUnitsSelect_Actions()
    local mainplayer= GetOwningPlayer(GetTriggerUnit())
    local general= GetTriggerPlayer()
    local pi= GetPlayerId(general)
    NotOwnRes[pi]=true
    OwnGold[pi]=GetPlayerState(general, PLAYER_STATE_RESOURCE_GOLD)
    OwnLumber[pi]=GetPlayerState(general, PLAYER_STATE_RESOURCE_LUMBER)
    SetPlayerStateBJ(general, PLAYER_STATE_RESOURCE_GOLD, GetPlayerState(mainplayer, PLAYER_STATE_RESOURCE_GOLD))
    SetPlayerStateBJ(general, PLAYER_STATE_RESOURCE_LUMBER, GetPlayerState(mainplayer, PLAYER_STATE_RESOURCE_LUMBER))
    
    
    mainplayer=nil
    general=nil
end
--===========================================================================
function InitTrig_ForSoldUnitsSelect()
    local i= 0
    gg_trg_ForSoldUnitsSelect=CreateTrigger()
    
    
    
    
    while true do
        if i > 23 then break end
        
        TriggerRegisterPlayerSelectionEventBJ(gg_trg_ForSoldUnitsSelect, Player(i), true)
        
        i=i + 1
    end
    
    
    
    TriggerAddCondition(gg_trg_ForSoldUnitsSelect, Condition(Trig_ForSoldUnitsSelect_Conditions))
      
    TriggerAddAction(gg_trg_ForSoldUnitsSelect, Trig_ForSoldUnitsSelect_Actions)
end
--===========================================================================
-- Trigger: ForSoldUnitsDesel
--===========================================================================
function Trig_ForSoldUnitsDesel_Conditions()
    return GetUnitAbilityLevel(GetTriggerUnit(), FourCC('Asud')) > 0 and GetPlayerAlliance(GetOwningPlayer(GetTriggerUnit()), GetTriggerPlayer(), ALLIANCE_SHARED_ADVANCED_CONTROL)
end
function Trig_ForSoldUnitsDesel_Actions()
    local mainplayer= GetOwningPlayer(GetTriggerUnit())
    local general= GetTriggerPlayer()
    local pi= GetPlayerId(general)
   
    if NotOwnRes[pi] then
        SetPlayerStateBJ(general, PLAYER_STATE_RESOURCE_GOLD, OwnGold[pi])
        SetPlayerStateBJ(general, PLAYER_STATE_RESOURCE_LUMBER, OwnLumber[pi])
        
        
        --??? ???
        
        SetPlayerStateBJ(mainplayer, PLAYER_STATE_RESOURCE_GOLD, GetPlayerState(mainplayer, PLAYER_STATE_RESOURCE_GOLD) + GoldDifference[pi])
        SetPlayerStateBJ(mainplayer, PLAYER_STATE_RESOURCE_LUMBER, GetPlayerState(mainplayer, PLAYER_STATE_RESOURCE_LUMBER) + LumberDifference[pi])
        GoldDifference[pi]=0
        LumberDifference[pi]=0
    end
    
    mainplayer=nil
    general=nil
end
--===========================================================================
function InitTrig_ForSoldUnitsDesel()
    local i= 0
    gg_trg_ForSoldUnitsDesel=CreateTrigger()
    
    
    while true do
        if i > 23 then break end
        
        TriggerRegisterPlayerSelectionEventBJ(gg_trg_ForSoldUnitsDesel, Player(i), true)
        
        i=i + 1
    end
    TriggerAddCondition(gg_trg_ForSoldUnitsDesel, Condition(Trig_ForSoldUnitsDesel_Conditions))
    TriggerAddAction(gg_trg_ForSoldUnitsDesel, Trig_ForSoldUnitsDesel_Actions)
end
--set GoldDifference[pi]= GoldDifference[pi] - GetUnitGoldCost(GetUnitTypeId(u))
--set LumberDifference[pi]= LumberDifference[pi] - GetUnitWoodCost(GetUnitTypeId(u))
--===========================================================================
-- Trigger: InitGlobals
--===========================================================================
function Trig_InitGlobals_Actions()
    local i= 0
    while true do
        if i > 23 then break end
        OwnGold[i]=0
        OwnLumber[i]=0
        GoldDifference[i]=0
        LumberDifference[i]=0
        NotOwnRes[i]=false
        
        
        i=i + 1
    end
end
--===========================================================================
function InitTrig_InitGlobals()
    gg_trg_InitGlobals=CreateTrigger()
    TriggerAddAction(gg_trg_InitGlobals, Trig_InitGlobals_Actions)
end
--
-- 
-- From this abyssal portal, deep monsters and nags emerge.
--===========================================================================
--===========================================================================
--===========================================================================
--===========================================================================
--===========================================================================
--===========================================================================
--===========================================================================
--===========================================================================
--===========================================================================
--===========================================================================
--===========================================================================
--===========================================================================
--===========================================================================
--===========================================================================
--===========================================================================
--===========================================================================
--===========================================================================
--===========================================================================
--===========================================================================
--===========================================================================
--===========================================================================
-- Trigger: Dark green color
--===========================================================================
--===========================================================================
--===========================================================================
--===========================================================================
--===========================================================================
--===========================================================================
--===========================================================================
--===========================================================================
--===========================================================================
--===========================================================================
--===========================================================================
--===========================================================================
--===========================================================================
--===========================================================================
--===========================================================================
--===========================================================================
--===========================================================================
--===========================================================================
--===========================================================================
--===========================================================================
--===========================================================================
--===========================================================================
--===========================================================================
--===========================================================================
--===========================================================================
--===========================================================================
--===========================================================================
--===========================================================================
--===========================================================================
-- Trigger: KillTestUnits   OFF ME
--===========================================================================
function Trig_KillTestUnits_O_Copy_Func001002()
    return RectContainsUnit(gg_rct_TestRegion, GetFilterUnit())
end
function Trig_KillTestUnits_O_Copy_Func003A()
    local u= GetEnumUnit()
    local p= GetOwningPlayer(u)
    local id= GetUnitTypeId(u)
    if IsUnitType(u, UNIT_TYPE_HERO) then
        SetPlayerTechMaxAllowed(p, id, GetPlayerTechMaxAllowed(p, id) + 1)
    end
    RemoveUnit(u)
    u=nil
    p=nil
end
function Trig_KillTestUnits___OFF_ME_Actions()
    GroupEnumUnitsInRect(udg_LocalOtrad2, bj_mapInitialPlayableArea, Condition(Trig_KillTestUnits_O_Copy_Func001002))
    ForGroupBJ(GetUnitsInRectAll(gg_rct_TestRegion), Trig_KillTestUnits_O_Copy_Func003A)
    GroupClear(udg_LocalOtrad2)
end
--===========================================================================
function InitTrig_KillTestUnits___OFF_ME()
    gg_trg_KillTestUnits___OFF_ME=CreateTrigger()
    TriggerRegisterTimerEventSingle(gg_trg_KillTestUnits___OFF_ME, 0.01)
    TriggerAddAction(gg_trg_KillTestUnits___OFF_ME, Trig_KillTestUnits___OFF_ME_Actions)
end
--===========================================================================
-- Trigger: Setlvl
--===========================================================================
function Trig_Setlvl_Func001001002()
    return IsUnitType(GetFilterUnit(), UNIT_TYPE_HERO)
end
function Trig_Setlvl_Func001A()
    SetHeroLevelBJ(GetEnumUnit(), S2I(SubStringBJ(GetEventPlayerChatString(), 8, 10)), false)
end
function Trig_Setlvl_Actions()
    ForGroupBJ(GetUnitsOfPlayerMatching(GetTriggerPlayer(), Condition(Trig_Setlvl_Func001001002)), Trig_Setlvl_Func001A)
end
--===========================================================================
function InitTrig_Setlvl()
    gg_trg_Setlvl=CreateTrigger()
    TriggerRegisterPlayerChatEvent(gg_trg_Setlvl, Player(0), " - setlvl", false)
    TriggerRegisterPlayerChatEvent(gg_trg_Setlvl, Player(1), "setlvl", false)
    TriggerRegisterPlayerChatEvent(gg_trg_Setlvl, Player(2), "setlvl", false)
    TriggerAddAction(gg_trg_Setlvl, Trig_Setlvl_Actions)
end
--===========================================================================
-- Trigger: A1
--===========================================================================
function Trig_A1_Func001A()
    UnitAddAbilityBJ(FourCC('A0IQ'), GetEnumUnit())
end
function Trig_A1_Actions()
    ForGroupBJ(GetUnitsSelectedAll(Player(0)), Trig_A1_Func001A)
end
--===========================================================================
function InitTrig_A1()
    gg_trg_A1=CreateTrigger()
    TriggerRegisterPlayerChatEvent(gg_trg_A1, Player(0), "a1", true)
    TriggerAddAction(gg_trg_A1, Trig_A1_Actions)
end
--===========================================================================
-- Trigger: Second O
--===========================================================================
function Trig_Second_O_Func001A()
    CreateNUnitsAtLoc(1, FourCC('h0HJ'), GetEnumPlayer(), GetRectCenter(GetPlayableMapRect()), bj_UNIT_FACING)
end
function Trig_Second_O_Actions()
    ForForce(udg_AllPlayers, Trig_Second_O_Func001A)
end
--===========================================================================
function InitTrig_Second_O()
    gg_trg_Second_O=CreateTrigger()
    TriggerRegisterPlayerChatEvent(gg_trg_Second_O, Player(0), "s2", true)
    TriggerAddAction(gg_trg_Second_O, Trig_Second_O_Actions)
end
--===========================================================================
-- Trigger: KillTestUnits Command
--===========================================================================
function Trig_KillTestUnits_Command_Func001002()
    return RectContainsUnit(gg_rct_TestRegion, GetFilterUnit())
end
function Trig_KillTestUnits_Command_Func003A()
    local u= GetEnumUnit()
    local p= GetOwningPlayer(u)
    local id= GetUnitTypeId(u)
    if IsUnitType(u, UNIT_TYPE_HERO) then
        SetPlayerTechMaxAllowed(p, id, GetPlayerTechMaxAllowed(p, id) + 1)
    end
    RemoveUnit(u)
    u=nil
    p=nil
    
end
function Trig_KillTestUnits_Command_Actions()
    GroupEnumUnitsInRect(udg_LocalOtrad2, bj_mapInitialPlayableArea, Condition(Trig_KillTestUnits_Command_Func001002))
    ForGroupBJ(GetUnitsInRectAll(gg_rct_TestRegion), Trig_KillTestUnits_Command_Func003A)
    GroupClear(udg_LocalOtrad2)
end
--===========================================================================
function InitTrig_KillTestUnits_Command()
    gg_trg_KillTestUnits_Command=CreateTrigger()
    TriggerRegisterPlayerChatEvent(gg_trg_KillTestUnits_Command, Player(0), "kill", true)
    TriggerAddAction(gg_trg_KillTestUnits_Command, Trig_KillTestUnits_Command_Actions)
end
--===========================================================================
-- Trigger: Player2VassalTo1 Back Copy
--===========================================================================
function Trig_Player2VassalTo1_Back_Copy_Conditions()
    return (( S2I(SubStringBJ(GetEventPlayerChatString(), 4, 5)) >= 1 )) and (( S2I(SubStringBJ(GetEventPlayerChatString(), 4, 5)) <= 24 ))
end
function Trig_Player2VassalTo1_Back_Copy_Actions()
    udg_LocalInteger=S2I(SubStringBJ(GetEventPlayerChatString(), 4, 5))
    SetPlayerAllianceStateBJ(ConvertedPlayer(udg_LocalInteger), Player(0), bj_ALLIANCE_UNALLIED)
end
--===========================================================================
function InitTrig_Player2VassalTo1_Back_Copy()
    gg_trg_Player2VassalTo1_Back_Copy=CreateTrigger()
    DisableTrigger(gg_trg_Player2VassalTo1_Back_Copy)
    TriggerRegisterPlayerChatEvent(gg_trg_Player2VassalTo1_Back_Copy, Player(0), " - dv", false)
    TriggerAddCondition(gg_trg_Player2VassalTo1_Back_Copy, Condition(Trig_Player2VassalTo1_Back_Copy_Conditions))
    TriggerAddAction(gg_trg_Player2VassalTo1_Back_Copy, Trig_Player2VassalTo1_Back_Copy_Actions)
end
--===========================================================================
-- Trigger: Player2VassalTo1 Copy
--===========================================================================
function Trig_Player2VassalTo1_Copy_Conditions()
    return (( S2I(SubStringBJ(GetEventPlayerChatString(), 4, 5)) >= 1 )) and (( S2I(SubStringBJ(GetEventPlayerChatString(), 4, 5)) <= 24 ))
end
function Trig_Player2VassalTo1_Copy_Actions()
    udg_LocalInteger=S2I(SubStringBJ(GetEventPlayerChatString(), 4, 5))
    SetPlayerAllianceStateBJ(ConvertedPlayer(udg_LocalInteger), Player(0), bj_ALLIANCE_ALLIED_ADVUNITS)
end
--===========================================================================
function InitTrig_Player2VassalTo1_Copy()
    gg_trg_Player2VassalTo1_Copy=CreateTrigger()
    DisableTrigger(gg_trg_Player2VassalTo1_Copy)
    TriggerRegisterPlayerChatEvent(gg_trg_Player2VassalTo1_Copy, Player(0), " - vs", false)
    TriggerAddCondition(gg_trg_Player2VassalTo1_Copy, Condition(Trig_Player2VassalTo1_Copy_Conditions))
    TriggerAddAction(gg_trg_Player2VassalTo1_Copy, Trig_Player2VassalTo1_Copy_Actions)
end
--===========================================================================
-- Trigger: Visible Copy
--===========================================================================
function Trig_Visible_Copy_Actions()
    CreateFogModifierRectBJ(true, Player(0), FOG_OF_WAR_VISIBLE, GetPlayableMapRect())
end
--===========================================================================
function InitTrig_Visible_Copy()
    gg_trg_Visible_Copy=CreateTrigger()
    TriggerRegisterPlayerChatEvent(gg_trg_Visible_Copy, Player(0), " - v", true)
    TriggerAddAction(gg_trg_Visible_Copy, Trig_Visible_Copy_Actions)
end
--===========================================================================
-- Trigger: Player2VassalTo1
--===========================================================================
function Trig_Player2VassalTo1_Actions()
    SetPlayerAllianceStateBJ(Player(1), Player(0), bj_ALLIANCE_ALLIED_ADVUNITS)
end
--===========================================================================
function InitTrig_Player2VassalTo1()
    gg_trg_Player2VassalTo1=CreateTrigger()
    TriggerRegisterPlayerChatEvent(gg_trg_Player2VassalTo1, Player(0), "b1", true)
    TriggerAddAction(gg_trg_Player2VassalTo1, Trig_Player2VassalTo1_Actions)
end
--===========================================================================
-- Trigger: Player2VassalTo1 Back
--===========================================================================
function Trig_Player2VassalTo1_Back_Actions()
    SetPlayerAllianceStateBJ(Player(1), Player(0), bj_ALLIANCE_UNALLIED)
end
--===========================================================================
function InitTrig_Player2VassalTo1_Back()
    gg_trg_Player2VassalTo1_Back=CreateTrigger()
    TriggerRegisterPlayerChatEvent(gg_trg_Player2VassalTo1_Back, Player(0), "b2", true)
    TriggerAddAction(gg_trg_Player2VassalTo1_Back, Trig_Player2VassalTo1_Back_Actions)
end
--===========================================================================
-- Trigger: Player3VassalTo1
--===========================================================================
function Trig_Player3VassalTo1_Actions()
    SetPlayerAllianceStateBJ(Player(2), Player(0), bj_ALLIANCE_ALLIED_ADVUNITS)
end
--===========================================================================
function InitTrig_Player3VassalTo1()
    gg_trg_Player3VassalTo1=CreateTrigger()
    TriggerRegisterPlayerChatEvent(gg_trg_Player3VassalTo1, Player(0), "c1", true)
    TriggerAddAction(gg_trg_Player3VassalTo1, Trig_Player3VassalTo1_Actions)
end
--===========================================================================
-- Trigger: Player3VassalTo1 Back
--===========================================================================
function Trig_Player3VassalTo1_Back_Actions()
    SetPlayerAllianceStateBJ(Player(2), Player(0), bj_ALLIANCE_UNALLIED)
end
--===========================================================================
function InitTrig_Player3VassalTo1_Back()
    gg_trg_Player3VassalTo1_Back=CreateTrigger()
    TriggerRegisterPlayerChatEvent(gg_trg_Player3VassalTo1_Back, Player(0), "c2", true)
    TriggerAddAction(gg_trg_Player3VassalTo1_Back, Trig_Player3VassalTo1_Back_Actions)
end
--===========================================================================
-- Trigger: AnyPlayerVassalToFirst
--===========================================================================
function Trig_AnyPlayerVassalToFirst_Conditions()
    return S2I(SubStringBJ(GetEventPlayerChatString(), 4, 5)) >= 1 and S2I(SubStringBJ(GetEventPlayerChatString(), 4, 5)) <= 24
end
function Trig_AnyPlayerVassalToFirst_Actions()
    local pi
    pi=S2I(SubStringBJ(GetEventPlayerChatString(), 4, 5)) - 1
    SetPlayerAllianceStateBJ(Player(pi), Player(0), bj_ALLIANCE_ALLIED_ADVUNITS)
end
--===========================================================================
function InitTrig_AnyPlayerVassalToFirst()
    gg_trg_AnyPlayerVassalToFirst=CreateTrigger()
    TriggerRegisterPlayerChatEvent(gg_trg_AnyPlayerVassalToFirst, Player(0), " - vs", false)
    TriggerAddAction(gg_trg_AnyPlayerVassalToFirst, Trig_AnyPlayerVassalToFirst_Actions)
    TriggerAddCondition(gg_trg_AnyPlayerVassalToFirst, Condition(Trig_AnyPlayerVassalToFirst_Conditions))
end
--===========================================================================
-- Trigger: AnyPlayerVassalToFirstOff
--===========================================================================
function Trig_AnyPlayerVassalToFirstOff_Conditions()
    return S2I(SubStringBJ(GetEventPlayerChatString(), 7, 8)) >= 1 and S2I(SubStringBJ(GetEventPlayerChatString(), 7, 8)) <= 24
end
function Trig_AnyPlayerVassalToFirstOff_Actions()
    local pi
    pi=S2I(SubStringBJ(GetEventPlayerChatString(), 7, 8)) - 1
    SetPlayerAllianceStateBJ(Player(pi), Player(0), bj_ALLIANCE_UNALLIED)
end
--===========================================================================
function InitTrig_AnyPlayerVassalToFirstOff()
    gg_trg_AnyPlayerVassalToFirstOff=CreateTrigger()
    TriggerRegisterPlayerChatEvent(gg_trg_AnyPlayerVassalToFirstOff, Player(0), " - vsoff", false)
    TriggerAddAction(gg_trg_AnyPlayerVassalToFirstOff, Trig_AnyPlayerVassalToFirstOff_Actions)
    TriggerAddCondition(gg_trg_AnyPlayerVassalToFirstOff, Condition(Trig_AnyPlayerVassalToFirstOff_Conditions))
end
--===========================================================================
-- Trigger: P1 Vs P2 P3 P4
--===========================================================================
function Trig_P1_Vs_P2_P3_P4_Actions()
    SetPlayerAllianceStateBJ(Player(2), Player(1), bj_ALLIANCE_ALLIED_VISION)
    SetPlayerAllianceStateBJ(Player(3), Player(1), bj_ALLIANCE_ALLIED_VISION)
    SetPlayerAllianceStateBJ(Player(1), Player(2), bj_ALLIANCE_ALLIED_VISION)
    SetPlayerAllianceStateBJ(Player(3), Player(2), bj_ALLIANCE_ALLIED_VISION)
    SetPlayerAllianceStateBJ(Player(2), Player(3), bj_ALLIANCE_ALLIED_VISION)
    SetPlayerAllianceStateBJ(Player(1), Player(3), bj_ALLIANCE_ALLIED_VISION)
    DisplayTextToForce(GetPlayersAll(), "TRIGSTR_5704")
end
--===========================================================================
function InitTrig_P1_Vs_P2_P3_P4()
    gg_trg_P1_Vs_P2_P3_P4=CreateTrigger()
    TriggerRegisterPlayerChatEvent(gg_trg_P1_Vs_P2_P3_P4, Player(0), "Pv3C", true)
    TriggerAddAction(gg_trg_P1_Vs_P2_P3_P4, Trig_P1_Vs_P2_P3_P4_Actions)
end
--===========================================================================
-- Trigger: ResO
--===========================================================================
function Trig_ResO_Actions()
    SetMapFlag(MAP_LOCK_RESOURCE_TRADING, false)
    SetMapFlag(MAP_LOCK_ALLIANCE_CHANGES, false)
    SetMapFlag(MAP_ALLIANCE_CHANGES_HIDDEN, false)
end
--===========================================================================
function InitTrig_ResO()
    gg_trg_ResO=CreateTrigger()
    TriggerRegisterPlayerChatEvent(gg_trg_ResO, Player(0), "reso", true)
    TriggerAddAction(gg_trg_ResO, Trig_ResO_Actions)
end
--===========================================================================
-- Trigger: ResO Copy
--===========================================================================
function Trig_ResO_Copy_Actions()
    SetMapFlag(MAP_LOCK_RESOURCE_TRADING, false)
    SetMapFlag(MAP_LOCK_ALLIANCE_CHANGES, false)
    SetMapFlag(MAP_ALLIANCE_CHANGES_HIDDEN, false)
end
--===========================================================================
function InitTrig_ResO_Copy()
    gg_trg_ResO_Copy=CreateTrigger()
    TriggerRegisterPlayerChatEvent(gg_trg_ResO_Copy, Player(0), "reson", true)
    TriggerAddAction(gg_trg_ResO_Copy, Trig_ResO_Copy_Actions)
end
--===========================================================================
-- Trigger: OpemVis
--===========================================================================
function Trig_OpemVis_Func003A()
    FogModifierStop(udg_Visibl[GetConvertedPlayerId(GetEnumPlayer())])
    DestroyFogModifier(udg_Visibl[GetConvertedPlayerId(GetEnumPlayer())])
    CreateFogModifierRectBJ(true, GetEnumPlayer(), FOG_OF_WAR_VISIBLE, GetPlayableMapRect())
end
function Trig_OpemVis_Actions()
    DisplayTextToForce(GetPlayersAll(), "TRIGSTR_4166")
    ForForce(udg_AllPlayers, Trig_OpemVis_Func003A)
end
--===========================================================================
function InitTrig_OpemVis()
    gg_trg_OpemVis=CreateTrigger()
    TriggerRegisterPlayerChatEvent(gg_trg_OpemVis, Player(0), "OpenVis", true)
    TriggerAddAction(gg_trg_OpemVis, Trig_OpemVis_Actions)
end
--===========================================================================
-- Trigger: StartLimit
--===========================================================================
function Trig_StartWorgens_Copy_Func001A()
    SetPlayerTechMaxAllowedSwap(FourCC('h0P7'), 1, GetEnumPlayer())
end
function Trig_StartLimit_Actions()
    ForForce(udg_AllPlayers, Trig_StartWorgens_Copy_Func001A)
end
--===========================================================================
function InitTrig_StartLimit()
    gg_trg_StartLimit=CreateTrigger()
    TriggerRegisterTimerEventSingle(gg_trg_StartLimit, 0.01)
    TriggerAddAction(gg_trg_StartLimit, Trig_StartLimit_Actions)
end
--===========================================================================
-- Trigger: DestroyTrain
--===========================================================================
function Trig_DestroyTrain_Conditions()
    return GetUnitTypeId(GetTrainedUnit()) == FourCC('h0P7')
end
function Trig_DestroyTrain_Func002A()
    KillUnit(GetEnumUnit())
end
function LimitTrainDestroy()
    SetPlayerTechMaxAllowedSwap(FourCC('h0P7'), 0, GetEnumPlayer())
end
function Trig_DestroyTrain_Actions()
    RemoveUnit(GetTrainedUnit())
    ForGroupBJ(GetUnitsInRectAll(gg_rct_TrainArea), Trig_DestroyTrain_Func002A)
    CreateDestructableLoc(FourCC('B01R'), GetRectCenter(gg_rct_Region_143), 0.0, 3, 0)
    CreateDestructableLoc(FourCC('B01S'), GetRectCenter(OffsetRectBJ(gg_rct_Region_143, 0, 200.00)), GetRandomDirectionDeg(), 1, 0)
    CreateDestructableLoc(FourCC('B01S'), GetRectCenter(OffsetRectBJ(gg_rct_Region_143, 0, - 200.00)), GetRandomDirectionDeg(), 1, 0)
    CreateDestructableLoc(FourCC('B01S'), GetRectCenter(OffsetRectBJ(gg_rct_Region_143, 650.00, 200.00)), GetRandomDirectionDeg(), 1, 0)
    CreateDestructableLoc(FourCC('B01S'), GetRectCenter(OffsetRectBJ(gg_rct_Region_143, 650.00, - 200.00)), GetRandomDirectionDeg(), 1, 0)
    
    CreateDestructableLoc(FourCC('B01S'), GetRectCenter(OffsetRectBJ(gg_rct_Region_143, 1300.00, 200.00)), GetRandomDirectionDeg(), 1, 0)
    CreateDestructableLoc(FourCC('B01S'), GetRectCenter(OffsetRectBJ(gg_rct_Region_143, 1300.00, - 200.00)), GetRandomDirectionDeg(), 1, 0)
    
    CreateDestructableLoc(FourCC('B01R'), GetRectCenter(OffsetRectBJ(gg_rct_Region_143, 1300.00, 0.00)), GetRandomDirectionDeg(), 3, 0)
    RemoveUnit(gg_unit_n003_0149)
    RemoveUnit(gg_unit_n003_0028)
    ForForce(udg_AllPlayers, LimitTrainDestroy)
end
--===========================================================================
function InitTrig_DestroyTrain()
    gg_trg_DestroyTrain=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_DestroyTrain, EVENT_PLAYER_UNIT_TRAIN_FINISH)
    TriggerAddCondition(gg_trg_DestroyTrain, Condition(Trig_DestroyTrain_Conditions))
    TriggerAddAction(gg_trg_DestroyTrain, Trig_DestroyTrain_Actions)
end
--===========================================================================
-- Trigger: BeginDestroingTrain
--===========================================================================
function Trig_BeginDestroingTrain_Conditions()
    return GetUnitTypeId(GetTrainedUnit()) == FourCC('h0P7')
end
function Trig_BeginDestroingTrain_Actions()
      DisplayTextToForce(udg_AllPlayers, " - ...")
end
--===========================================================================
function InitTrig_BeginDestroingTrain()
    gg_trg_BeginDestroingTrain=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_BeginDestroingTrain, EVENT_PLAYER_UNIT_TRAIN_START)
    TriggerAddCondition(gg_trg_BeginDestroingTrain, Condition(Trig_BeginDestroingTrain_Conditions))
    TriggerAddAction(gg_trg_BeginDestroingTrain, Trig_BeginDestroingTrain_Actions)
end
--===========================================================================
-- Trigger: KakecCommon
--===========================================================================
function DisableKalec()
    SetPlayerAbilityAvailableBJ(false, FourCC('A12R'), GetEnumPlayer())
end
function EnableKalec()
    SetPlayerAbilityAvailableBJ(true, FourCC('A12R'), GetEnumPlayer())
end
--===========================================================================
-- Trigger: KalecStart
--===========================================================================
function Trig_KalecStart_Actions()
    local u
    local l= GetUnitLoc(GetTriggerUnit())
    u=CreateUnitAtLoc(Player(24), FourCC('n04W'), l, bj_UNIT_FACING)
    TriggerRegisterUnitEvent(gg_trg_KalecDead, u, EVENT_UNIT_DEATH)
    UnitRemoveAbility(GetTriggerUnit(), FourCC('A12R'))
    ForForce(udg_AllPlayers, DisableKalec)
    TriggerSleepAction(245)
    if UnitAlive(u) then
        ShowUnit(u, false)
        RemoveUnit(u)
        DisplayTextToPlayer(GetOwningPlayer(GetTriggerUnit()), 0, 0, "4")
        ForForce(udg_AllPlayers, EnableKalec)
        UnitAddAbility(GetTriggerUnit(), FourCC('A12R'))
    end
    
    RemoveLocation(l)
    l=nil
    u=nil
end
--===========================================================================
function InitTrig_KalecStart()
    gg_trg_KalecStart=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_KalecStart, EVENT_PLAYER_UNIT_SPELL_EFFECT)
    TriggerAddAction(gg_trg_KalecStart, function()
        if GetSpellAbilityId() ~= FourCC('A12R') then return end
        if not (IsUnitSelected(GetTriggerUnit(), GetOwningPlayer(GetTriggerUnit()))) then return end
        Trig_KalecStart_Actions()
    end)
end
--===========================================================================
-- Trigger: KalecDead
--===========================================================================
function Trig_KalecDead_Func004A()
    SetPlayerAbilityAvailableBJ(false, FourCC('A12R'), GetEnumPlayer())
end
function Trig_KalecDead_Actions()
    udg_LocalPosition2=GetUnitLoc(GetTriggerUnit())
    CreateItemLoc(FourCC('I01U'), udg_LocalPosition2)
    DisplayTextToForce(GetPlayersAll(), "TRIGSTR_25200")
    ForForce(udg_AllPlayers, Trig_KalecDead_Func004A)
    DisableTrigger(gg_trg_KalecStart)
end
--===========================================================================
function InitTrig_KalecDead()
    gg_trg_KalecDead=CreateTrigger()
    TriggerAddAction(gg_trg_KalecDead, Trig_KalecDead_Actions)
end
--===========================================================================
-- Trigger: ShaStart
--===========================================================================
function DisableSha()
    SetPlayerAbilityAvailableBJ(false, FourCC('A1ML'), GetEnumPlayer())
end
function Trig_ShaStart_Actions()
    local u
    u=CreateUnit(Player(24), FourCC('n076'), GetUnitX(GetTriggerUnit()), GetUnitY(GetTriggerUnit()), bj_UNIT_FACING)
    TriggerRegisterUnitEvent(gg_trg_ShaDead, u, EVENT_UNIT_DEATH)
    UnitRemoveAbility(GetTriggerUnit(), FourCC('A1ML'))
    ForForce(udg_AllPlayers, DisableSha)
    u=nil
end
--===========================================================================
function InitTrig_ShaStart()
    gg_trg_ShaStart=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_ShaStart, EVENT_PLAYER_UNIT_SPELL_EFFECT)
    TriggerAddAction(gg_trg_ShaStart, function()
        if GetSpellAbilityId() ~= FourCC('A1ML') then return end
        if not (IsUnitSelected(GetTriggerUnit(), GetOwningPlayer(GetTriggerUnit()))) then return end
        Trig_ShaStart_Actions()
    end)
end
--===========================================================================
-- Trigger: ShaDead
--===========================================================================
function Trig_ShaDead_Actions()
    CreateItem(FourCC('I021'), GetUnitX(GetTriggerUnit()), GetUnitY(GetTriggerUnit()))
    DisplayTextToForce(udg_AllPlayers2, ".")
    AdjustPlayerStateBJ(20000, GetOwningPlayer(GetKillingUnit()), PLAYER_STATE_RESOURCE_GOLD)
    AdjustPlayerStateBJ(20000, GetOwningPlayer(GetKillingUnit()), PLAYER_STATE_RESOURCE_LUMBER)
    DisableTrigger(gg_trg_ShaStart)
    DisableTrigger(gg_trg_ShaDead)
end
--===========================================================================
function InitTrig_ShaDead()
    gg_trg_ShaDead=CreateTrigger()
    TriggerAddAction(gg_trg_ShaDead, Trig_ShaDead_Actions)
end
--===========================================================================
-- Trigger: AncientGods add MindControl Copy
--===========================================================================
function Trig_AncientGods_add_MindControl_Copy_Actions()
    UnitAddAbilityBJ(FourCC('A0W4'), gg_unit_n03D_0666)
    DisableTrigger(GetTriggeringTrigger())
end
--===========================================================================
function InitTrig_AncientGods_add_MindControl_Copy()
    gg_trg_AncientGods_add_MindControl_Copy=CreateTrigger()
    TriggerRegisterUnitLifeEvent(gg_trg_AncientGods_add_MindControl_Copy, gg_unit_n03D_0666, LESS_THAN, 15000.00)
    TriggerAddAction(gg_trg_AncientGods_add_MindControl_Copy, Trig_AncientGods_add_MindControl_Copy_Actions)
end
--===========================================================================
-- Trigger: AncienGods Add MassAttak Copy
--===========================================================================
function Trig_AncienGods_Add_MassAttak_Copy_Actions()
    UnitAddAbilityBJ(FourCC('A0T3'), gg_unit_n03D_0666)
    DisableTrigger(GetTriggeringTrigger())
end
--===========================================================================
function InitTrig_AncienGods_Add_MassAttak_Copy()
    gg_trg_AncienGods_Add_MassAttak_Copy=CreateTrigger()
    TriggerRegisterUnitLifeEvent(gg_trg_AncienGods_Add_MassAttak_Copy, gg_unit_n03D_0666, LESS_THAN, 17000.00)
    TriggerAddAction(gg_trg_AncienGods_Add_MassAttak_Copy, Trig_AncienGods_Add_MassAttak_Copy_Actions)
end
--===========================================================================
-- Trigger: Qtun 17k o
--===========================================================================
function Trig_Qtun_17k_o_Actions()
    udg_LocalPosition2=GetRectCenter(gg_rct_Qt1)
    CreateNUnitsAtLoc(1, FourCC('n03J'), Player(PLAYER_NEUTRAL_AGGRESSIVE), udg_LocalPosition2, bj_UNIT_FACING)
    RemoveLocation(udg_LocalPosition2)
    udg_LocalPosition2=GetRectCenter(gg_rct_Qt2)
    CreateNUnitsAtLoc(1, FourCC('n03J'), Player(PLAYER_NEUTRAL_AGGRESSIVE), udg_LocalPosition2, bj_UNIT_FACING)
    RemoveLocation(udg_LocalPosition2)
    udg_LocalPosition2=GetRectCenter(gg_rct_Qt3)
    CreateNUnitsAtLoc(1, FourCC('n03J'), Player(PLAYER_NEUTRAL_AGGRESSIVE), udg_LocalPosition2, bj_UNIT_FACING)
    RemoveLocation(udg_LocalPosition2)
    udg_LocalPosition2=GetRectCenter(gg_rct_Qt4)
    CreateNUnitsAtLoc(1, FourCC('n03J'), Player(PLAYER_NEUTRAL_AGGRESSIVE), udg_LocalPosition2, bj_UNIT_FACING)
    RemoveLocation(udg_LocalPosition2)
    DisableTrigger(GetTriggeringTrigger())
end
--===========================================================================
function InitTrig_Qtun_17k_o()
    gg_trg_Qtun_17k_o=CreateTrigger()
    TriggerRegisterUnitLifeEvent(gg_trg_Qtun_17k_o, gg_unit_n03D_0666, LESS_THAN, 17000.00)
    TriggerAddAction(gg_trg_Qtun_17k_o, Trig_Qtun_17k_o_Actions)
end
--===========================================================================
-- Trigger: Qtun HP 24k O
--===========================================================================
function Trig_Qtun_HP_24k_O_Actions()
    udg_LocalPosition2=GetRectCenter(gg_rct_Qt1)
    CreateNUnitsAtLoc(1, FourCC('n03J'), Player(PLAYER_NEUTRAL_AGGRESSIVE), udg_LocalPosition2, bj_UNIT_FACING)
    RemoveLocation(udg_LocalPosition2)
    udg_LocalPosition2=GetRectCenter(gg_rct_Qt2)
    CreateNUnitsAtLoc(1, FourCC('n03J'), Player(PLAYER_NEUTRAL_AGGRESSIVE), udg_LocalPosition2, bj_UNIT_FACING)
    RemoveLocation(udg_LocalPosition2)
    udg_LocalPosition2=GetRectCenter(gg_rct_Qt3)
    CreateNUnitsAtLoc(1, FourCC('n03J'), Player(PLAYER_NEUTRAL_AGGRESSIVE), udg_LocalPosition2, bj_UNIT_FACING)
    RemoveLocation(udg_LocalPosition2)
    udg_LocalPosition2=GetRectCenter(gg_rct_Qt4)
    CreateNUnitsAtLoc(1, FourCC('n03J'), Player(PLAYER_NEUTRAL_AGGRESSIVE), udg_LocalPosition2, bj_UNIT_FACING)
    RemoveLocation(udg_LocalPosition2)
    DisableTrigger(GetTriggeringTrigger())
end
--===========================================================================
function InitTrig_Qtun_HP_24k_O()
    gg_trg_Qtun_HP_24k_O=CreateTrigger()
    TriggerRegisterUnitLifeEvent(gg_trg_Qtun_HP_24k_O, gg_unit_n03D_0666, LESS_THAN, 24000.00)
    TriggerAddAction(gg_trg_Qtun_HP_24k_O, Trig_Qtun_HP_24k_O_Actions)
end
--===========================================================================
-- Trigger: Qtun Die
--===========================================================================
function Trig_Qtun_Die_Conditions()
    return (( GetTriggerUnit() == gg_unit_n03D_0666 )) and (( GetOwningPlayer(GetTriggerUnit()) ~= GetOwningPlayer(GetKillingUnitBJ()) ))
end
function Trig_Qtun_Die_Actions()
    udg_LocalPosition2=GetUnitLoc(GetTriggerUnit())
    DisplayTextToForce(GetPlayersAll(), "TRIGSTR_2385")
    AdjustPlayerStateBJ(20000, GetOwningPlayer(GetKillingUnitBJ()), PLAYER_STATE_RESOURCE_GOLD)
    AdjustPlayerStateBJ(20000, GetOwningPlayer(GetKillingUnitBJ()), PLAYER_STATE_RESOURCE_LUMBER)
    CreateItemLoc(FourCC('I01R'), udg_LocalPosition2)
    RemoveLocation(udg_LocalPosition2)
    DisableTrigger(GetTriggeringTrigger())
end
--===========================================================================
function InitTrig_Qtun_Die()
    gg_trg_Qtun_Die=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_Qtun_Die, EVENT_PLAYER_UNIT_DEATH)
    TriggerAddCondition(gg_trg_Qtun_Die, Condition(Trig_Qtun_Die_Conditions))
    TriggerAddAction(gg_trg_Qtun_Die, Trig_Qtun_Die_Actions)
end
--===========================================================================
-- Trigger: SpawnQtun
--===========================================================================
function Trig_SpawnQtun_Func006C()
    return (( GetTriggerUnit() == gg_unit_n03D_0666 )) and (( GetSpellAbilityId() == FourCC('A0W0') )) and (( GetPlayerController(GetOwningPlayer(GetTriggerUnit())) ~= MAP_CONTROL_USER ))
end
function Trig_SpawnQtun_Conditions()
    return Trig_SpawnQtun_Func006C()
end
function Trig_SpawnQtun_Func002Func002C()
    return udg_LocalInteger2 == 1
end
function Trig_SpawnQtun_Func002Func008A()
    UnitApplyTimedLifeBJ(30.00, FourCC('BTLF'), GetEnumUnit())
    IssuePointOrderLocBJ(GetEnumUnit(), "attack", udg_LocalPosition3)
end
function Trig_SpawnQtun_Func002C()
    return GetUnitLifePercent(GetTriggerUnit()) >= 75.00
end
function Trig_SpawnQtun_Func003Func002C()
    return udg_LocalInteger2 == 1
end
function Trig_SpawnQtun_Func003Func008A()
    UnitApplyTimedLifeBJ(30.00, FourCC('BTLF'), GetEnumUnit())
    IssuePointOrderLocBJ(GetEnumUnit(), "attack", udg_LocalPosition3)
end
function Trig_SpawnQtun_Func003C()
    return (( GetUnitLifePercent(GetTriggerUnit()) <= 75.00 )) and (( GetUnitLifePercent(GetTriggerUnit()) >= 50.00 ))
end
function Trig_SpawnQtun_Func004Func002C()
    return udg_LocalInteger2 == 1
end
function Trig_SpawnQtun_Func004Func008A()
    UnitApplyTimedLifeBJ(30.00, FourCC('BTLF'), GetEnumUnit())
    IssuePointOrderLocBJ(GetEnumUnit(), "attack", udg_LocalPosition3)
end
function Trig_SpawnQtun_Func004C()
    return (( GetUnitLifePercent(GetTriggerUnit()) <= 50.00 )) and (( GetUnitLifePercent(GetTriggerUnit()) >= 25.00 ))
end
function Trig_SpawnQtun_Func005Func002C()
    return udg_LocalInteger2 == 1
end
function Trig_SpawnQtun_Func005Func008A()
    UnitApplyTimedLifeBJ(30.00, FourCC('BTLF'), GetEnumUnit())
    IssuePointOrderLocBJ(GetEnumUnit(), "attack", udg_LocalPosition3)
end
function Trig_SpawnQtun_Func005C()
    return GetUnitLifePercent(GetTriggerUnit()) <= 50.00
end
function Trig_SpawnQtun_Actions()
    udg_LocalInteger2=GetRandomInt(1, 2)
    if Trig_SpawnQtun_Func002C() then
        if Trig_SpawnQtun_Func002Func002C() then
            udg_LocalPosition2=GetRectCenter(gg_rct_QtunSp2)
        else
            udg_LocalPosition2=GetRectCenter(gg_rct_QtunSp1)
        end
        udg_LocalInteger=R2I(( ( I2R(BlzGetUnitMaxHP(GetTriggerUnit())) - GetUnitStateSwap(UNIT_STATE_LIFE, GetTriggerUnit()) ) / 1000.00 ))
        udg_LocalInteger2=( udg_LocalInteger * 2 )
        udg_LocalOtrad=GetLastCreatedGroup()
        udg_LocalPosition3=GetUnitLoc(gg_unit_n03D_0666)
        ForGroupBJ(udg_LocalOtrad, Trig_SpawnQtun_Func002Func008A)
        GroupClear(udg_LocalOtrad)
        RemoveLocation(udg_LocalPosition2)
        RemoveLocation(udg_LocalPosition3)
    end
    if Trig_SpawnQtun_Func003C() then
        udg_LocalInteger2=GetRandomInt(1, 2)
        if Trig_SpawnQtun_Func003Func002C() then
            udg_LocalPosition2=GetRectCenter(gg_rct_QtunSp2)
        else
            udg_LocalPosition2=GetRectCenter(gg_rct_QtunSp1)
        end
        udg_LocalInteger=R2I(( ( I2R(BlzGetUnitMaxHP(GetTriggerUnit())) - GetUnitStateSwap(UNIT_STATE_LIFE, GetTriggerUnit()) ) / 1000.00 ))
        udg_LocalInteger2=( udg_LocalInteger * 4 )
        udg_LocalOtrad=GetLastCreatedGroup()
        udg_LocalPosition3=GetUnitLoc(gg_unit_n03D_0666)
        ForGroupBJ(udg_LocalOtrad, Trig_SpawnQtun_Func003Func008A)
        GroupClear(udg_LocalOtrad)
        RemoveLocation(udg_LocalPosition2)
        RemoveLocation(udg_LocalPosition3)
    end
    if Trig_SpawnQtun_Func004C() then
        udg_LocalInteger2=GetRandomInt(1, 2)
        if Trig_SpawnQtun_Func004Func002C() then
            udg_LocalPosition2=GetRectCenter(gg_rct_QtunSp2)
        else
            udg_LocalPosition2=GetRectCenter(gg_rct_QtunSp1)
        end
        udg_LocalInteger=R2I(( ( I2R(BlzGetUnitMaxHP(GetTriggerUnit())) - GetUnitStateSwap(UNIT_STATE_LIFE, GetTriggerUnit()) ) / 1000.00 ))
        udg_LocalInteger2=( udg_LocalInteger * 1 )
        CreateNUnitsAtLoc(udg_LocalInteger2, FourCC('e01Q'), GetOwningPlayer(GetTriggerUnit()), udg_LocalPosition2, bj_UNIT_FACING)
        udg_LocalOtrad=GetLastCreatedGroup()
        udg_LocalPosition3=GetUnitLoc(gg_unit_n03D_0666)
        ForGroupBJ(udg_LocalOtrad, Trig_SpawnQtun_Func004Func008A)
        GroupClear(udg_LocalOtrad)
        RemoveLocation(udg_LocalPosition2)
        RemoveLocation(udg_LocalPosition3)
    end
    if Trig_SpawnQtun_Func005C() then
        udg_LocalInteger2=GetRandomInt(1, 2)
        if Trig_SpawnQtun_Func005Func002C() then
            udg_LocalPosition2=GetRectCenter(gg_rct_QtunSp2)
        else
            udg_LocalPosition2=GetRectCenter(gg_rct_QtunSp1)
        end
        udg_LocalInteger=R2I(( ( I2R(BlzGetUnitMaxHP(GetTriggerUnit())) - GetUnitStateSwap(UNIT_STATE_LIFE, GetTriggerUnit()) ) / 1000.00 ))
        udg_LocalInteger2=( udg_LocalInteger * 1 )
        CreateNUnitsAtLoc(udg_LocalInteger2, FourCC('e01P'), GetOwningPlayer(GetTriggerUnit()), udg_LocalPosition2, bj_UNIT_FACING)
        udg_LocalOtrad=GetLastCreatedGroup()
        udg_LocalPosition3=GetUnitLoc(gg_unit_n03D_0666)
        ForGroupBJ(udg_LocalOtrad, Trig_SpawnQtun_Func005Func008A)
        GroupClear(udg_LocalOtrad)
        RemoveLocation(udg_LocalPosition2)
        RemoveLocation(udg_LocalPosition3)
    end
end
--===========================================================================
function InitTrig_SpawnQtun()
    gg_trg_SpawnQtun=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_SpawnQtun, EVENT_PLAYER_UNIT_SPELL_EFFECT)
    TriggerAddCondition(gg_trg_SpawnQtun, Condition(Trig_SpawnQtun_Conditions))
    TriggerAddAction(gg_trg_SpawnQtun, Trig_SpawnQtun_Actions)
end
--===========================================================================
-- Trigger: Qogg HP 24k O
--===========================================================================
function Trig_Qogg_HP_24k_O_Actions()
    udg_LocalPosition2=GetRectCenter(gg_rct_Yog1_1)
    CreateNUnitsAtLoc(1, FourCC('n04C'), Player(PLAYER_NEUTRAL_AGGRESSIVE), GetRectCenter(gg_rct_Yog1_5), bj_UNIT_FACING)
    RemoveLocation(udg_LocalPosition2)
    udg_LocalPosition2=GetRectCenter(gg_rct_Yog1_2)
    CreateNUnitsAtLoc(1, FourCC('n04C'), Player(PLAYER_NEUTRAL_AGGRESSIVE), GetRectCenter(gg_rct_Yog1_5), bj_UNIT_FACING)
    RemoveLocation(udg_LocalPosition2)
    udg_LocalPosition2=GetRectCenter(gg_rct_Yog1_3)
    CreateNUnitsAtLoc(1, FourCC('n04C'), Player(PLAYER_NEUTRAL_AGGRESSIVE), GetRectCenter(gg_rct_Yog1_5), bj_UNIT_FACING)
    RemoveLocation(udg_LocalPosition2)
    udg_LocalPosition2=GetRectCenter(gg_rct_Yog1_4)
    CreateNUnitsAtLoc(1, FourCC('n04C'), Player(PLAYER_NEUTRAL_AGGRESSIVE), GetRectCenter(gg_rct_Yog1_5), bj_UNIT_FACING)
    RemoveLocation(udg_LocalPosition2)
    DisableTrigger(GetTriggeringTrigger())
end
--===========================================================================
function InitTrig_Qogg_HP_24k_O()
    gg_trg_Qogg_HP_24k_O=CreateTrigger()
    TriggerRegisterUnitLifeEvent(gg_trg_Qogg_HP_24k_O, gg_unit_n03A_0657, LESS_THAN, 24000.00)
    TriggerAddAction(gg_trg_Qogg_HP_24k_O, Trig_Qogg_HP_24k_O_Actions)
end
--===========================================================================
-- Trigger: Qogg HP 17k O
--===========================================================================
function Trig_Qogg_HP_17k_O_Actions()
    udg_LocalPosition2=GetRectCenter(gg_rct_Yog1_5)
    CreateNUnitsAtLoc(1, FourCC('n04C'), Player(PLAYER_NEUTRAL_AGGRESSIVE), GetRectCenter(gg_rct_Yog1_5), bj_UNIT_FACING)
    RemoveLocation(udg_LocalPosition2)
    udg_LocalPosition2=GetRectCenter(gg_rct_Yog1_6)
    CreateNUnitsAtLoc(1, FourCC('n04C'), Player(PLAYER_NEUTRAL_AGGRESSIVE), GetRectCenter(gg_rct_Yog1_6), bj_UNIT_FACING)
    RemoveLocation(udg_LocalPosition2)
    udg_LocalPosition2=GetRectCenter(gg_rct_Yog1_7)
    CreateNUnitsAtLoc(1, FourCC('n04C'), Player(PLAYER_NEUTRAL_AGGRESSIVE), GetRectCenter(gg_rct_Yog1_7), bj_UNIT_FACING)
    RemoveLocation(udg_LocalPosition2)
    udg_LocalPosition2=GetRectCenter(gg_rct_Yog1_8)
    CreateNUnitsAtLoc(1, FourCC('n04C'), Player(PLAYER_NEUTRAL_AGGRESSIVE), GetRectCenter(gg_rct_Yog1_8), bj_UNIT_FACING)
    RemoveLocation(udg_LocalPosition2)
    DisableTrigger(GetTriggeringTrigger())
end
--===========================================================================
function InitTrig_Qogg_HP_17k_O()
    gg_trg_Qogg_HP_17k_O=CreateTrigger()
    TriggerRegisterUnitLifeEvent(gg_trg_Qogg_HP_17k_O, gg_unit_n03A_0657, LESS_THAN, 17000.00)
    TriggerAddAction(gg_trg_Qogg_HP_17k_O, Trig_Qogg_HP_17k_O_Actions)
end
--===========================================================================
-- Trigger: AncienGods Add MassAttak
--===========================================================================
function Trig_AncienGods_Add_MassAttak_Actions()
    UnitAddAbilityBJ(FourCC('A0T3'), gg_unit_n03A_0657)
end
--===========================================================================
function InitTrig_AncienGods_Add_MassAttak()
    gg_trg_AncienGods_Add_MassAttak=CreateTrigger()
    TriggerRegisterUnitLifeEvent(gg_trg_AncienGods_Add_MassAttak, gg_unit_n03A_0657, LESS_THAN, 17000.00)
    TriggerAddAction(gg_trg_AncienGods_Add_MassAttak, Trig_AncienGods_Add_MassAttak_Actions)
end
--===========================================================================
-- Trigger: AncientGods add MindControl
--===========================================================================
function Trig_AncientGods_add_MindControl_Actions()
    UnitAddAbilityBJ(FourCC('A0W4'), gg_unit_n03A_0657)
    DisableTrigger(GetTriggeringTrigger())
end
--===========================================================================
function InitTrig_AncientGods_add_MindControl()
    gg_trg_AncientGods_add_MindControl=CreateTrigger()
    TriggerRegisterUnitLifeEvent(gg_trg_AncientGods_add_MindControl, gg_unit_n03A_0657, LESS_THAN, 15000.00)
    TriggerAddAction(gg_trg_AncientGods_add_MindControl, Trig_AncientGods_add_MindControl_Actions)
end
--===========================================================================
-- Trigger: Qogg Die
--===========================================================================
function Trig_Qogg_Die_Conditions()
    return GetTriggerUnit() == gg_unit_n03A_0657
end
function Trig_Qogg_Die_Actions()
    DisplayTextToForce(GetPlayersAll(), "TRIGSTR_20558")
    AdjustPlayerStateBJ(20000, GetOwningPlayer(GetKillingUnitBJ()), PLAYER_STATE_RESOURCE_GOLD)
    AdjustPlayerStateBJ(20000, GetOwningPlayer(GetKillingUnitBJ()), PLAYER_STATE_RESOURCE_LUMBER)
    CreateItemLoc(FourCC('I01Q'), GetUnitLoc(GetTriggerUnit()))
    DisableTrigger(GetTriggeringTrigger())
end
--===========================================================================
function InitTrig_Qogg_Die()
    gg_trg_Qogg_Die=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_Qogg_Die, EVENT_PLAYER_UNIT_DEATH)
    TriggerAddCondition(gg_trg_Qogg_Die, Condition(Trig_Qogg_Die_Conditions))
    TriggerAddAction(gg_trg_Qogg_Die, Trig_Qogg_Die_Actions)
end
--===========================================================================
-- Trigger: QoggSpawn
--===========================================================================
function Trig_Spell1_Copy_2_Func008C()
    return (( GetTriggerUnit() == gg_unit_n03A_0657 )) and (( GetSpellAbilityId() == FourCC('A0T7') )) and (( GetPlayerController(GetOwningPlayer(GetTriggerUnit())) ~= MAP_CONTROL_USER ))
end
function Trig_QoggSpawn_Conditions()
    return Trig_Spell1_Copy_2_Func008C()
end
function Trig_Spell1_Copy_2_Func003C()
    return udg_LocalInteger == 1
end
function Trig_Spell1_Copy_2_Func004C()
    return udg_LocalInteger == 2
end
function Trig_Spell1_Copy_2_Func005C()
    return udg_LocalInteger == 3
end
function Trig_Spell1_Copy_2_Func006C()
    return udg_LocalInteger == 4
end
function Trig_Spell1_Copy_2_Func007C()
    return udg_LocalInteger == 5
end
function Trig_QoggSpawn_Actions()
    local u= GetTriggerUnit()
    local p= GetOwningPlayer(u)
    udg_LocalPosition2=GetRandomLocInRect(gg_rct_Region_083)
    udg_LocalInteger=GetRandomInt(1, 5)
    if Trig_Spell1_Copy_2_Func003C() then
        CreateNUnitsAtLoc(1, FourCC('n04C'), p, udg_LocalPosition2, bj_UNIT_FACING)
        UnitApplyTimedLifeBJ(60, FourCC('BTLF'), GetLastCreatedUnit())
        return
    end
    if Trig_Spell1_Copy_2_Func004C() then
        CreateNUnitsAtLoc(1, FourCC('n03C'), p, udg_LocalPosition2, bj_UNIT_FACING)
        UnitApplyTimedLifeBJ(60, FourCC('BTLF'), GetLastCreatedUnit())
        return
    end
    if Trig_Spell1_Copy_2_Func005C() then
        CreateNUnitsAtLoc(1, FourCC('n04K'), p, udg_LocalPosition2, bj_UNIT_FACING)
        UnitApplyTimedLifeBJ(60, FourCC('BTLF'), GetLastCreatedUnit())
        return
    end
    if Trig_Spell1_Copy_2_Func006C() then
        CreateNUnitsAtLoc(1, FourCC('n04L'), p, udg_LocalPosition2, bj_UNIT_FACING)
        UnitApplyTimedLifeBJ(60, FourCC('BTLF'), GetLastCreatedUnit())
        return
    end
    if Trig_Spell1_Copy_2_Func007C() then
        CreateNUnitsAtLoc(1, FourCC('n04J'), p, udg_LocalPosition2, bj_UNIT_FACING)
        UnitApplyTimedLifeBJ(60, FourCC('BTLF'), GetLastCreatedUnit())
        return
    end
    
    p=nil
    u=nil
end
--===========================================================================
function InitTrig_QoggSpawn()
