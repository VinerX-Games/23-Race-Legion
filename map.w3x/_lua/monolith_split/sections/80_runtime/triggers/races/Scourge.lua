
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