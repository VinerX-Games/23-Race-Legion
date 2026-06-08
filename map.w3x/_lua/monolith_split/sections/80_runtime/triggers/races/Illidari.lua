
--===========================================================================
-- Trigger: IllidaryOn
--===========================================================================
function Trig_IllidaryOn_Actions()
    EnableTrigger(gg_trg_IllyFire)
    EnableTrigger(gg_trg_IllyAgile)
    
    EnableTrigger(gg_trg_IllyPain)
    EnableTrigger(gg_trg_IlliKnives)
    EnableTrigger(gg_trg_IllyAttack)
    EnableTrigger(gg_trg_RuvokAutoIlly)
    --call EnableTrigger( gg_trg_SandStrike )
   
end
--===========================================================================
function InitTrig_IllidaryOn()
    gg_trg_IllidaryOn=CreateTrigger()
    TriggerAddAction(gg_trg_IllidaryOn, Trig_IllidaryOn_Actions)
end
--===========================================================================
-- Trigger: flot1 Copy 2
--===========================================================================
function Trig_flot1_Copy_2_Conditions()
    return GetResearched() == FourCC('R099')
end
function Trig_flot1_Copy_2_Actions()
    SetPlayerTechMaxAllowedSwap(FourCC('R09A'), 0, GetOwningPlayer(GetTriggerUnit()))
    SetPlayerTechMaxAllowedSwap(FourCC('R09B'), 0, GetOwningPlayer(GetTriggerUnit()))
end
--===========================================================================
function InitTrig_flot1_Copy_2()
    gg_trg_flot1_Copy_2=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_flot1_Copy_2, EVENT_PLAYER_UNIT_RESEARCH_FINISH)
    TriggerRegisterAnyUnitEventBJ(gg_trg_flot1_Copy_2, EVENT_PLAYER_UNIT_RESEARCH_START)
    TriggerAddCondition(gg_trg_flot1_Copy_2, Condition(Trig_flot1_Copy_2_Conditions))
    TriggerAddAction(gg_trg_flot1_Copy_2, Trig_flot1_Copy_2_Actions)
end
--===========================================================================
-- Trigger: flot2 Copy 2
--===========================================================================
function Trig_flot2_Copy_2_Conditions()
    return GetResearched() == FourCC('R099')
end
function Trig_flot2_Copy_2_Actions()
    SetPlayerTechMaxAllowedSwap(FourCC('R09A'), 1, GetOwningPlayer(GetTriggerUnit()))
    SetPlayerTechMaxAllowedSwap(FourCC('R09B'), 1, GetOwningPlayer(GetTriggerUnit()))
end
--===========================================================================
function InitTrig_flot2_Copy_2()
    gg_trg_flot2_Copy_2=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_flot2_Copy_2, EVENT_PLAYER_UNIT_RESEARCH_CANCEL)
    TriggerAddCondition(gg_trg_flot2_Copy_2, Condition(Trig_flot2_Copy_2_Conditions))
    TriggerAddAction(gg_trg_flot2_Copy_2, Trig_flot2_Copy_2_Actions)
end
--===========================================================================
-- Trigger: arm1 Copy 2
--===========================================================================
function Trig_arm1_Copy_2_Conditions()
    return GetResearched() == FourCC('R09A')
end
function Trig_arm1_Copy_2_Actions()
    SetPlayerTechMaxAllowedSwap(FourCC('R099'), 0, GetOwningPlayer(GetTriggerUnit()))
    SetPlayerTechMaxAllowedSwap(FourCC('R09B'), 0, GetOwningPlayer(GetTriggerUnit()))
end
--===========================================================================
function InitTrig_arm1_Copy_2()
    gg_trg_arm1_Copy_2=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_arm1_Copy_2, EVENT_PLAYER_UNIT_RESEARCH_FINISH)
    TriggerRegisterAnyUnitEventBJ(gg_trg_arm1_Copy_2, EVENT_PLAYER_UNIT_RESEARCH_START)
    TriggerAddCondition(gg_trg_arm1_Copy_2, Condition(Trig_arm1_Copy_2_Conditions))
    TriggerAddAction(gg_trg_arm1_Copy_2, Trig_arm1_Copy_2_Actions)
end
--===========================================================================
-- Trigger: arm2 Copy 2
--===========================================================================
function Trig_arm2_Copy_2_Conditions()
    return GetResearched() == FourCC('R09A')
end
function Trig_arm2_Copy_2_Actions()
    SetPlayerTechMaxAllowedSwap(FourCC('R099'), 1, GetOwningPlayer(GetTriggerUnit()))
    SetPlayerTechMaxAllowedSwap(FourCC('R09B'), 1, GetOwningPlayer(GetTriggerUnit()))
end
--===========================================================================
function InitTrig_arm2_Copy_2()
    gg_trg_arm2_Copy_2=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_arm2_Copy_2, EVENT_PLAYER_UNIT_RESEARCH_CANCEL)
    TriggerAddCondition(gg_trg_arm2_Copy_2, Condition(Trig_arm2_Copy_2_Conditions))
    TriggerAddAction(gg_trg_arm2_Copy_2, Trig_arm2_Copy_2_Actions)
end
--===========================================================================
-- Trigger: arm1 Copy 2 Copy
--===========================================================================
function Trig_arm1_Copy_2_Copy_Conditions()
    return GetResearched() == FourCC('R09B')
end
function Trig_arm1_Copy_2_Copy_Actions()
    SetPlayerTechMaxAllowedSwap(FourCC('R099'), 0, GetOwningPlayer(GetTriggerUnit()))
    SetPlayerTechMaxAllowedSwap(FourCC('R09A'), 0, GetOwningPlayer(GetTriggerUnit()))
end
--===========================================================================
function InitTrig_arm1_Copy_2_Copy()
    gg_trg_arm1_Copy_2_Copy=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_arm1_Copy_2_Copy, EVENT_PLAYER_UNIT_RESEARCH_FINISH)
    TriggerRegisterAnyUnitEventBJ(gg_trg_arm1_Copy_2_Copy, EVENT_PLAYER_UNIT_RESEARCH_START)
    TriggerAddCondition(gg_trg_arm1_Copy_2_Copy, Condition(Trig_arm1_Copy_2_Copy_Conditions))
    TriggerAddAction(gg_trg_arm1_Copy_2_Copy, Trig_arm1_Copy_2_Copy_Actions)
end
--===========================================================================
-- Trigger: arm2 Copy 2 Copy
--===========================================================================
function Trig_arm2_Copy_2_Copy_Conditions()
    return GetResearched() == FourCC('R09B')
end
function Trig_arm2_Copy_2_Copy_Actions()
    SetPlayerTechMaxAllowedSwap(FourCC('R099'), 1, GetOwningPlayer(GetTriggerUnit()))
    SetPlayerTechMaxAllowedSwap(FourCC('R09A'), 1, GetOwningPlayer(GetTriggerUnit()))
end
--===========================================================================
function InitTrig_arm2_Copy_2_Copy()
    gg_trg_arm2_Copy_2_Copy=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_arm2_Copy_2_Copy, EVENT_PLAYER_UNIT_RESEARCH_CANCEL)
    TriggerAddCondition(gg_trg_arm2_Copy_2_Copy, Condition(Trig_arm2_Copy_2_Copy_Conditions))
    TriggerAddAction(gg_trg_arm2_Copy_2_Copy, Trig_arm2_Copy_2_Copy_Actions)
end
--===========================================================================
-- Trigger: EnemyPower
--===========================================================================
function Trig_EnemyPower_Conditions()
    return GetUnitAbilityLevel(GetEventDamageSource(), FourCC('A0O5')) > 0 and GetPlayerTechCount(GetOwningPlayer(GetEventDamageSource()), FourCC('R096'), true) > 0
end
function Trig_EnemyPower_Actions()
    --call SetUnitState(GetEventDamageSource(),UNIT_STATE_LIFE,
    if BlzGetEventAttackType() == ATTACK_TYPE_NORMAL then
        SetUnitLifePercentBJ(GetEventDamageSource(), GetUnitLifePercent(GetEventDamageSource()) + 0.25)
    else
        SetUnitLifePercentBJ(GetEventDamageSource(), GetUnitLifePercent(GetEventDamageSource()) + 0.5)
    
    end
    
end
--===========================================================================
function InitTrig_EnemyPower()
    gg_trg_EnemyPower=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_EnemyPower, EVENT_PLAYER_UNIT_DAMAGED)
    TriggerAddCondition(gg_trg_EnemyPower, Condition(Trig_EnemyPower_Conditions))
    TriggerAddAction(gg_trg_EnemyPower, Trig_EnemyPower_Actions)
end
--===========================================================================
-- Trigger: AutoStrelaFireIlly
--===========================================================================
function Trig_AutoStrelaFireIlly_Actions()
    IssueTargetOrderBJ(GetTriggerUnit(), "firebolt", GetSpellTargetUnit())
end
--===========================================================================
function InitTrig_AutoStrelaFireIlly()
    gg_trg_AutoStrelaFireIlly=CreateTrigger()
    
    TriggerRegisterAnyUnitEventBJ(gg_trg_AutoStrelaFireIlly, EVENT_PLAYER_UNIT_SPELL_EFFECT)
    TriggerAddAction(gg_trg_AutoStrelaFireIlly, function()
        if GetSpellAbilityId() ~= FourCC('A1KL') then return end
        Trig_AutoStrelaFireIlly_Actions()
    end)
end
--===========================================================================
-- Trigger: AutoStrelaFelllly
--===========================================================================
function Trig_AutoStrelaFelllly_Actions()
    IssueTargetOrderBJ(GetTriggerUnit(), "acidbomb", GetSpellTargetUnit())
end
--===========================================================================
function InitTrig_AutoStrelaFelllly()
    gg_trg_AutoStrelaFelllly=CreateTrigger()
    
    TriggerRegisterAnyUnitEventBJ(gg_trg_AutoStrelaFelllly, EVENT_PLAYER_UNIT_SPELL_EFFECT)
    TriggerAddAction(gg_trg_AutoStrelaFelllly, function()
        if GetSpellAbilityId() ~= FourCC('A1KO') then return end
        Trig_AutoStrelaFelllly_Actions()
    end)
end
--===========================================================================
-- Trigger: IllyFire
--===========================================================================
function Trig_IllyFire_Func001Func001Func002Func001C()
    return GetUnitAbilityLevelSwapped(FourCC('A0NJ'), GetTriggerUnit()) == 4
end
function Trig_IllyFire_Func001Func001Func002C()
    return GetUnitAbilityLevelSwapped(FourCC('A0NJ'), GetTriggerUnit()) == 3
end
function Trig_IllyFire_Func001Func001C()
    return GetUnitAbilityLevelSwapped(FourCC('A0NJ'), GetTriggerUnit()) == 2
end
function Trig_IllyFire_Func001C()
    return GetUnitAbilityLevelSwapped(FourCC('A0NJ'), GetTriggerUnit()) == 1
end
function Trig_IllyFire_Actions()
    if Trig_IllyFire_Func001C() then
        UnitAddAbilityBJ(FourCC('A0NO'), GetTriggerUnit())
        UnitAddAbilityBJ(FourCC('A0NM'), GetTriggerUnit())
        TriggerSleepAction(15.00)
        UnitRemoveAbilityBJ(FourCC('A0NO'), GetTriggerUnit())
        UnitRemoveAbilityBJ(FourCC('A0NM'), GetTriggerUnit())
    else
        if Trig_IllyFire_Func001Func001C() then
            UnitAddAbilityBJ(FourCC('A0NP'), GetTriggerUnit())
            UnitAddAbilityBJ(FourCC('A0NK'), GetTriggerUnit())
            TriggerSleepAction(15.00)
            UnitRemoveAbilityBJ(FourCC('A0NP'), GetTriggerUnit())
            UnitRemoveAbilityBJ(FourCC('A0NK'), GetTriggerUnit())
        else
            if Trig_IllyFire_Func001Func001Func002C() then
                UnitAddAbilityBJ(FourCC('A0NR'), GetTriggerUnit())
                UnitAddAbilityBJ(FourCC('A0NL'), GetTriggerUnit())
                TriggerSleepAction(15.00)
                UnitRemoveAbilityBJ(FourCC('A0NR'), GetTriggerUnit())
                UnitRemoveAbilityBJ(FourCC('A0NL'), GetTriggerUnit())
            else
                if Trig_IllyFire_Func001Func001Func002Func001C() then
                    UnitAddAbilityBJ(FourCC('A0NQ'), GetTriggerUnit())
                    UnitAddAbilityBJ(FourCC('A0NN'), GetTriggerUnit())
                    TriggerSleepAction(15.00)
                    UnitRemoveAbilityBJ(FourCC('A0NQ'), GetTriggerUnit())
                    UnitRemoveAbilityBJ(FourCC('A0NN'), GetTriggerUnit())
                end
            end
        end
    end
end
--===========================================================================
function InitTrig_IllyFire()
    gg_trg_IllyFire=CreateTrigger()
    DisableTrigger(gg_trg_IllyFire)
    TriggerRegisterAnyUnitEventBJ(gg_trg_IllyFire, EVENT_PLAYER_UNIT_SPELL_EFFECT)
    TriggerAddAction(gg_trg_IllyFire, function()
        if GetSpellAbilityId() ~= FourCC('A0NJ') then return end
        Trig_IllyFire_Actions()
    end)
end
--===========================================================================
-- Trigger: IllyAgile
--===========================================================================
function Trig_IllyAgile_Actions()
    
    local u= GetTriggerUnit()
    UnitAddAbility(u, FourCC('A0NI'))
    RemoveAbilityTimed(u , FourCC('A0NI') , 20)
    u=nil
    
    
end
--===========================================================================
function InitTrig_IllyAgile()
    gg_trg_IllyAgile=CreateTrigger()
    DisableTrigger(gg_trg_IllyAgile)
    TriggerRegisterAnyUnitEventBJ(gg_trg_IllyAgile, EVENT_PLAYER_UNIT_SPELL_EFFECT)
    TriggerAddAction(gg_trg_IllyAgile, function()
        if GetSpellAbilityId() ~= FourCC('A0NH') then return end
        Trig_IllyAgile_Actions()
    end)
end
--===========================================================================
-- Trigger: IllyPain
--===========================================================================
function Trig_IllyPain_Actions()
    local u= GetTriggerUnit()
    UnitAddAbility(u, FourCC('A0NT'))
    RemoveAbilityTimed(u , FourCC('A0NT') , 20)
    u=nil
end
--===========================================================================
function InitTrig_IllyPain()
    gg_trg_IllyPain=CreateTrigger()
    DisableTrigger(gg_trg_IllyPain)
    TriggerRegisterAnyUnitEventBJ(gg_trg_IllyPain, EVENT_PLAYER_UNIT_SPELL_EFFECT)
    TriggerAddAction(gg_trg_IllyPain, function()
        if GetSpellAbilityId() ~= FourCC('A0NU') then return end
        Trig_IllyPain_Actions()
    end)
end
--===========================================================================
-- Trigger: IlliKnives
--===========================================================================
function Trig_IlliKnives_Actions()
    local u= GetTriggerUnit()
    UnitAddAbility(u, FourCC('A0NY'))
    RemoveAbilityTimed(u , FourCC('A0NY') , 20)
    u=nil
end
--===========================================================================
function InitTrig_IlliKnives()
    gg_trg_IlliKnives=CreateTrigger()
    DisableTrigger(gg_trg_IlliKnives)
    TriggerRegisterAnyUnitEventBJ(gg_trg_IlliKnives, EVENT_PLAYER_UNIT_SPELL_EFFECT)
    TriggerAddAction(gg_trg_IlliKnives, function()
        if GetSpellAbilityId() ~= FourCC('A0NV') then return end
        Trig_IlliKnives_Actions()
    end)
end
--===========================================================================
-- Trigger: RuvokAutoIlly
--===========================================================================
function Trig_RuvokAutoIlly_Actions()
    IssueTargetOrderBJ(GetTriggerUnit(), "deathcoil", GetSpellTargetUnit())
end
--===========================================================================
function InitTrig_RuvokAutoIlly()
    gg_trg_RuvokAutoIlly=CreateTrigger()
    DisableTrigger(gg_trg_RuvokAutoIlly)
    TriggerRegisterAnyUnitEventBJ(gg_trg_RuvokAutoIlly, EVENT_PLAYER_UNIT_SPELL_EFFECT)
    TriggerAddAction(gg_trg_RuvokAutoIlly, function()
        if GetSpellAbilityId() ~= FourCC('A048') then return end
        Trig_RuvokAutoIlly_Actions()
    end)
end
--===========================================================================
-- Trigger: SandStrike
--===========================================================================
function Trig_SandStrike_Func001C()
    return udg_SSinteger[0] == 0
end
function Trig_SandStrike_Actions()
    if Trig_SandStrike_Func001C() then
        EnableTrigger(gg_trg_Sand_Strike_Loop)
    end
    udg_SSinteger[0]=udg_SSinteger[0] + 1
    udg_SSinteger[1]=udg_SSinteger[1] + 1
    udg_SScaster[udg_SSinteger[1]]=GetTriggerUnit()
    SetUnitPathing(udg_SScaster[udg_SSinteger[1]], false)
    udg_SSfacing[udg_SSinteger[1]]=GetUnitFacing(udg_SScaster[udg_SSinteger[1]])
    udg_SSpointcaster[udg_SSinteger[1]]=GetUnitLoc(udg_SScaster[udg_SSinteger[1]])
    udg_SSdamage[udg_SSinteger[1]]=5.00 + I2R(GetUnitAbilityLevelSwapped(FourCC('A0NF'), udg_SScaster[udg_SSinteger[1]]))
    udg_SStargetpoint[udg_SSinteger[1]]=GetSpellTargetLoc()
    udg_SSeffect[udg_SSinteger[1]]="AbilitiesWeaponsAncientProtectorMissileAncientProtectorMissile.mdl"
    udg_SS[udg_SSinteger[1]]=GetUnitAbilityLevelSwapped(FourCC('A0NF'), udg_SScaster[udg_SSinteger[1]]) + 30
    PauseUnitBJ(true, GetTriggerUnit())
    RemoveLocation(udg_SSpointcaster[udg_SSinteger[1]])
    RemoveLocation(udg_SStargetpoint[udg_SSinteger[1]])
end
--===========================================================================
function InitTrig_SandStrike()
    gg_trg_SandStrike=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_SandStrike, EVENT_PLAYER_UNIT_SPELL_EFFECT)
    TriggerAddAction(gg_trg_SandStrike, function()
        if GetSpellAbilityId() ~= FourCC('A0NF') then return end
        Trig_SandStrike_Actions()
    end)
end
--===========================================================================
-- Trigger: Sand Strike Loop
--===========================================================================
function Trig_Sand_Strike_Loop_Func001Func001Func003C()
    return IsTerrainPathableBJ(udg_SSpointmovecaster[udg_SSinteger[2]], PATHING_TYPE_WALKABILITY)
end
function Trig_Sand_Strike_Loop_Func001Func001Func004002003001()
    return IsUnitEnemy(GetFilterUnit(), GetOwningPlayer(udg_SScaster[udg_SSinteger[2]]))
end
function Trig_Sand_Strike_Loop_Func001Func001Func004002003002()
    return IsUnitAliveBJ(GetFilterUnit())
end
function Trig_Sand_Strike_Loop_Func001Func001Func004002003()
    return GetBooleanAnd(IsUnitEnemy(GetFilterUnit(), GetOwningPlayer(udg_SScaster[udg_SSinteger[2]])), IsUnitAliveBJ(GetFilterUnit())) -- INLINED!!
end
function Trig_Sand_Strike_Loop_Func001Func001Func007Func004C()
    return not (IsUnitType(udg_SSpicked[udg_SSinteger[2]], UNIT_TYPE_STRUCTURE))
end
function Trig_Sand_Strike_Loop_Func001Func001Func007A()
    udg_SSpicked[udg_SSinteger[2]]=GetEnumUnit()
    udg_SSpointpicked[udg_SSinteger[2]]=GetUnitLoc(udg_SSpicked[udg_SSinteger[2]])
    udg_SSpointmovepicked[udg_SSinteger[2]]=PolarProjectionBJ(udg_SSpointpicked[udg_SSinteger[2]], I2R(udg_SS[udg_SSinteger[2]]), GetUnitFacing(udg_SSpicked[udg_SSinteger[2]]))
    if Trig_Sand_Strike_Loop_Func001Func001Func007Func004C() then
        SetUnitPositionLoc(udg_SSpicked[udg_SSinteger[2]], udg_SSpointmovepicked[udg_SSinteger[2]])
    end
    UnitDamageTargetBJ(udg_SScaster[udg_SSinteger[2]], udg_SSpicked[udg_SSinteger[3]], udg_SSdamage[udg_SSinteger[2]], ATTACK_TYPE_NORMAL, DAMAGE_TYPE_NORMAL)
    udg_SSpicked[udg_SSinteger[2]]=nil
    RemoveLocation(udg_SSpointpicked[udg_SSinteger[2]])
    RemoveLocation(udg_SSpointmovepicked[udg_SSinteger[2]])
end
function Trig_Sand_Strike_Loop_Func001Func001Func011Func004C()
    return udg_SSinteger[0] == 0
end
function Trig_Sand_Strike_Loop_Func001Func001Func011C()
    return udg_SS[udg_SSinteger[2]] == 0
end
function Trig_Sand_Strike_Loop_Func001Func001C()
    return udg_SS[udg_SSinteger[2]] ~= 0
end
function Trig_Sand_Strike_Loop_Actions()
    udg_SSinteger[2]=1
    while true do
        if udg_SSinteger[2] > udg_SSinteger[1] then break end
        if Trig_Sand_Strike_Loop_Func001Func001C() then
            udg_SSpointcaster[udg_SSinteger[2]]=GetUnitLoc(udg_SScaster[udg_SSinteger[2]])
            udg_SSpointmovecaster[udg_SSinteger[2]]=PolarProjectionBJ(udg_SSpointcaster[udg_SSinteger[2]], I2R(udg_SS[udg_SSinteger[2]]), udg_SSfacing[udg_SSinteger[2]])
            if Trig_Sand_Strike_Loop_Func001Func001Func003C() then
                RemoveLocation(udg_SSpointmovecaster[udg_SSinteger[2]])
                udg_SSpointmovecaster[udg_SSinteger[2]]=PolarProjectionBJ(udg_SSpointcaster[udg_SSinteger[2]], I2R(udg_SS[udg_SSinteger[2]]), udg_SSfacing[udg_SSinteger[2]] - 180.00)
            end
            udg_SSgroup[udg_SSinteger[2]]=GetUnitsInRangeOfLocMatching(150.00, udg_SSpointcaster[udg_SSinteger[2]], Condition(Trig_Sand_Strike_Loop_Func001Func001Func004002003))
            udg_SS[udg_SSinteger[2]]=udg_SS[udg_SSinteger[2]] - 1
            SetUnitPositionLoc(udg_SScaster[udg_SSinteger[2]], udg_SSpointmovecaster[udg_SSinteger[2]])
            ForGroupBJ(udg_SSgroup[udg_SSinteger[2]], Trig_Sand_Strike_Loop_Func001Func001Func007A)
            RemoveLocation(udg_SSpointmovecaster[udg_SSinteger[2]])
            DestroyGroup(udg_SSgroup[udg_SSinteger[2]])
            RemoveLocation(udg_SSpointcaster[udg_SSinteger[2]])
            if Trig_Sand_Strike_Loop_Func001Func001Func011C() then
                SetUnitPathing(udg_SScaster[udg_SSinteger[2]], true)
                PauseUnitBJ(false, udg_SScaster[udg_SSinteger[2]])
                udg_SSinteger[0]=udg_SSinteger[0] - 1
                if Trig_Sand_Strike_Loop_Func001Func001Func011Func004C() then
                    udg_SSinteger[1]=0
                    DisableTrigger(GetTriggeringTrigger())
                end
            end
        end
        udg_SSinteger[2]=udg_SSinteger[2] + 1
    end
end
--===========================================================================
function InitTrig_Sand_Strike_Loop()
    gg_trg_Sand_Strike_Loop=CreateTrigger()
    DisableTrigger(gg_trg_Sand_Strike_Loop)
    TriggerRegisterTimerEventPeriodic(gg_trg_Sand_Strike_Loop, 0.04)
    TriggerAddAction(gg_trg_Sand_Strike_Loop, Trig_Sand_Strike_Loop_Actions)
end