
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