
--===========================================================================
-- Trigger: BanditsOn
--===========================================================================
function Trig_BanditsOn_Actions()
    --call EnableTrigger( gg_trg_VoevodaSpell )
    EnableTrigger(gg_trg_BlinkToUnit_attack)
    EnableTrigger(gg_trg_DelAttackSpel)
    EnableTrigger(gg_trg_BlinkToUnit_Spell)
    EnableTrigger(gg_trg_Edvin_Ult)
    EnableTrigger(gg_trg_AutoChance)
    EnableTrigger(gg_trg_AutoChance_2)
    EnableTrigger(gg_trg_AutoChance_3)
    EnableTrigger(gg_trg_Dovorougenie_Code_O)
    EnableTrigger(gg_trg_Dovorougenie_2t_Code_O)
    EnableTrigger(gg_trg_Dovorougenie_3t_O)
    
    
    EnableTrigger(gg_trg_Voron)
    EnableTrigger(gg_trg_Sindicat)
    EnableTrigger(gg_trg_Bratstwo)
    EnableTrigger(gg_trg_Pirats)
    EnableTrigger(gg_trg_Shesterenka)
    EnableTrigger(gg_trg_Trumnue_vodu)
    
    
    EnableTrigger(gg_trg_AutoSetka)
    EnableTrigger(gg_trg_AutoSetkaHero)
    EnableTrigger(gg_trg_AutoSvita)
    EnableTrigger(gg_trg_AutoStaya)
    EnableTrigger(gg_trg_AutoManaSteal)
    EnableTrigger(gg_trg_AutoShield)
    EnableTrigger(gg_trg_ResearhRobbery)
    EnableTrigger(gg_trg_RobberyTrain)
    
    EnableTrigger(gg_trg_Edvin_Ult)
    EnableTrigger(gg_trg_BlinkToUnit_Spell)
    EnableTrigger(gg_trg_BlinkToUnit_attack)
    
    
    
    
end
--===========================================================================
function InitTrig_BanditsOn()
    gg_trg_BanditsOn=CreateTrigger()
    TriggerAddAction(gg_trg_BanditsOn, Trig_BanditsOn_Actions)
end
--===========================================================================
-- Trigger: StartBandits
--===========================================================================
function Trig_StartBandits_Func001A()
    SetPlayerTechMaxAllowedSwap(FourCC('h03L'), 0, GetEnumPlayer())
    SetPlayerTechMaxAllowedSwap(FourCC('h03K'), 0, GetEnumPlayer())
    SetPlayerTechMaxAllowedSwap(FourCC('h02R'), 0, GetEnumPlayer())
    SetPlayerTechMaxAllowedSwap(FourCC('h02T'), 0, GetEnumPlayer())
    SetPlayerTechMaxAllowedSwap(FourCC('h02Q'), 0, GetEnumPlayer())
    SetPlayerTechMaxAllowedSwap(FourCC('h02U'), 0, GetEnumPlayer())
    SetPlayerTechMaxAllowedSwap(FourCC('h02S'), 0, GetEnumPlayer())
    SetPlayerTechMaxAllowedSwap(FourCC('H048'), 1, GetEnumPlayer())
    SetPlayerTechMaxAllowedSwap(FourCC('H03S'), 1, GetEnumPlayer())
    SetPlayerTechMaxAllowedSwap(FourCC('H047'), 1, GetEnumPlayer())
    SetPlayerTechResearchedSwap(FourCC('R00H'), 1, GetEnumPlayer())
end
function Trig_StartBandits_Actions()
    ForForce(udg_AllPlayers, Trig_StartBandits_Func001A)
end
--===========================================================================
function InitTrig_StartBandits()
    gg_trg_StartBandits=CreateTrigger()
    TriggerRegisterTimerEventSingle(gg_trg_StartBandits, 0.01)
    TriggerAddAction(gg_trg_StartBandits, Trig_StartBandits_Actions)
end
--===========================================================================
-- Trigger: BlinkToUnit attack
--===========================================================================
function Trig_BlinkToUnit_attack_Conditions()
    return GetUnitAbilityLevel(GetAttacker(), FourCC('A0MZ')) >= 1 and BlzGetUnitAbilityCooldownRemaining(GetAttacker(), FourCC('A0MZ')) == 0
end
function Trig_BlinkToUnit_attack_Actions()
    gUnit=GetAttacker()
    local u = gUnit
    local target = GetTriggerUnit()
    local l = GetUnitLoc(GetTriggerUnit())
    local order = "attack"
    local time = 0.1
    local t = CreateTimer()
    TimerStart(t, time, false, function()
        SetUnitPositionLoc(u, l)
        IssueTargetOrder(u, order, target)
        RemoveLocation(l)
        DestroyTimer(t)
    end)
    DummyCastTargetLevel(FourCC('A1MY') , "shadowstrike" , gUnit , GetTriggerUnit() , GetUnitAbilityLevel(gUnit, FourCC('A0MZ')))
    BlzStartUnitAbilityCooldown(gUnit, FourCC('A0MZ'), 3)
end
--===========================================================================
function InitTrig_BlinkToUnit_attack()
    gg_trg_BlinkToUnit_attack=CreateTrigger()
    DisableTrigger(gg_trg_BlinkToUnit_attack)
    TriggerRegisterAnyUnitEventBJ(gg_trg_BlinkToUnit_attack, EVENT_PLAYER_UNIT_ATTACKED)
    TriggerAddCondition(gg_trg_BlinkToUnit_attack, Condition(Trig_BlinkToUnit_attack_Conditions))
    TriggerAddAction(gg_trg_BlinkToUnit_attack, Trig_BlinkToUnit_attack_Actions)
end
--===========================================================================
-- Trigger: BlinkToUnit Spell
--===========================================================================
function Trig_BlinkToUnit_Spell_Actions()
    local l1= GetUnitLoc(GetSpellTargetUnit())
    local l2= GetUnitLoc(GetTriggerUnit())
    local u = GetTriggerUnit()
    local target = GetSpellTargetUnit()
    local order = "attack"
    local time = DistanceBetweenPoints(l1, l2) / 1200 + 0.4
    local t = CreateTimer()
    TimerStart(t, time, false, function()
        SetUnitPositionLoc(u, l1)
        IssueTargetOrder(u, order, target)
        RemoveLocation(l1)
        DestroyTimer(t)
    end)
    RemoveLocation(l2)
    l1=nil
    l2=nil
end
--===========================================================================
function InitTrig_BlinkToUnit_Spell()
    gg_trg_BlinkToUnit_Spell=CreateTrigger()
    DisableTrigger(gg_trg_BlinkToUnit_Spell)
    TriggerRegisterAnyUnitEventBJ(gg_trg_BlinkToUnit_Spell, EVENT_PLAYER_UNIT_SPELL_CAST)
    TriggerAddAction(gg_trg_BlinkToUnit_Spell, function()
        if GetSpellAbilityId() ~= FourCC('A0N3') then return end
        Trig_BlinkToUnit_Spell_Actions()
    end)
end
--===========================================================================
-- Trigger: Edvin Ult
--
-- ????? ? ????
--===========================================================================
function Trig_Edvin_Ult_Actions()
    local u= GetTriggerUnit()
    local u2
    local g= CreateGroup()
    GroupEnumUnitsInRange(g, GetSpellTargetX(), GetSpellTargetY(), 235.00, nil)
    
    
    
    while true do
        u2=FirstOfGroup(g)
        if u2 == nil then break end
        
        if GetOwningPlayer(u2) ~= GetOwningPlayer(u) then
            
            SetUnitX(u, GetUnitX(u2))
            SetUnitY(u, GetUnitY(u2))
            RemoveEffectTimed(AddSpecialEffect("ObjectsSpawnmodelsHumanHumanBloodHumanBloodLarge1.mdl", GetUnitX(u2), GetUnitY(u2)) , 1)
            UnitDamageTargetBJ(u, u2, 300 * GetUnitAbilityLevel(u, FourCC('A0N4')) + 2 * GetHeroAgi(u, true), ATTACK_TYPE_HERO, DAMAGE_TYPE_FORCE)
                 
            
            
        end
        
        GroupRemoveUnit(g, u2)
    end
    
    
    
    
    UnitAddAbility(u, FourCC('A0N5'))
    BlzUnitDisableAbility(u, FourCC('A0N1'), true, true)
    IssueImmediateOrder(u, "windwalk")
    BlzUnitDisableAbility(u, FourCC('A0N1'), false, false)
    BlzStartUnitAbilityCooldown(u, FourCC('A0N4'), 35)
    
    DestroyGroup(g)
    g=nil
    u=nil
    u2=nil
end
--===========================================================================
function InitTrig_Edvin_Ult()
    gg_trg_Edvin_Ult=CreateTrigger()
    DisableTrigger(gg_trg_Edvin_Ult)
    TriggerRegisterAnyUnitEventBJ(gg_trg_Edvin_Ult, EVENT_PLAYER_UNIT_SPELL_CAST)
    TriggerAddAction(gg_trg_Edvin_Ult, function()
        if GetSpellAbilityId() ~= FourCC('A0N4') then return end
        Trig_Edvin_Ult_Actions()
    end)
end
--===========================================================================
-- Trigger: Del1FromTable C
--===========================================================================
function Trig_Del1FromTable_C_Actions()
    local i= GetPlayerId(udg_LocalPlayer)
    MultiboardSetItemValue(MultiboardItem[MultiboardItemOwnerIndex[i] * 2 + 1], I2S(udg_UnitsCount[i + 1]))
    i=0
end
--===========================================================================
-- Trigger: OnlySelected
--===========================================================================
function Trig_Dovorougenie_3t_O_Copy_Func001C()
    return IsUnitSelected(GetTriggerUnit(), GetOwningPlayer(GetTriggerUnit()))
end
--===========================================================================
-- Trigger: AutoChance
--===========================================================================
function Trig_AutoChance_Func003C()
    return (( GetUnitAbilityLevelSwapped(FourCC('A000'), GetEventDamageSource()) >= 1 )) and IsPlayerEnemy(GetOwningPlayer(GetTriggerUnit()), GetOwningPlayer(GetEventDamageSource()))
end
function Trig_AutoChance_Conditions()
    return Trig_AutoChance_Func003C()
end
function Trig_AutoChance_Func002C()
    return udg_LocalInteger <= ( GetUnitAbilityLevelSwapped(FourCC('A00M'), GetEventDamageSource()) * 1 )
end
function Trig_AutoChance_Actions()
    udg_LocalInteger=GetRandomInt(1, 100)
    if Trig_AutoChance_Func002C() then
        AdjustPlayerStateBJ(150, GetOwningPlayer(GetEventDamageSource()), PLAYER_STATE_RESOURCE_GOLD)
        AdjustPlayerStateBJ(50, GetOwningPlayer(GetEventDamageSource()), PLAYER_STATE_RESOURCE_LUMBER)
        IssueImmediateOrderBJ(GetEventDamageSource(), "berserk")
    end
end
--===========================================================================
function InitTrig_AutoChance()
    gg_trg_AutoChance=CreateTrigger()
    DisableTrigger(gg_trg_AutoChance)
    TriggerRegisterAnyUnitEventBJ(gg_trg_AutoChance, EVENT_PLAYER_UNIT_DAMAGED)
    TriggerAddCondition(gg_trg_AutoChance, Condition(Trig_AutoChance_Conditions))
    TriggerAddAction(gg_trg_AutoChance, Trig_AutoChance_Actions)
end
--===========================================================================
-- Trigger: AutoChance 2
--===========================================================================
function Trig_AutoChance_2_Func001C()
    return (( GetUnitAbilityLevelSwapped(FourCC('A01A'), GetEventDamageSource()) >= 1 )) and IsPlayerEnemy(GetOwningPlayer(GetTriggerUnit()), GetOwningPlayer(GetEventDamageSource()))
end
function Trig_AutoChance_2_Conditions()
    return Trig_AutoChance_2_Func001C()
end
function Trig_AutoChance_2_Func003C()
    return udg_LocalInteger <= ( GetUnitAbilityLevelSwapped(FourCC('A00M'), GetEventDamageSource()) * 1 )
end
function Trig_AutoChance_2_Actions()
    udg_LocalInteger=GetRandomInt(1, 125)
    if Trig_AutoChance_2_Func003C() then
        AdjustPlayerStateBJ(400, GetOwningPlayer(GetEventDamageSource()), PLAYER_STATE_RESOURCE_GOLD)
        AdjustPlayerStateBJ(75, GetOwningPlayer(GetEventDamageSource()), PLAYER_STATE_RESOURCE_LUMBER)
        IssueImmediateOrderBJ(GetEventDamageSource(), "berserk")
    end
end
--===========================================================================
function InitTrig_AutoChance_2()
    gg_trg_AutoChance_2=CreateTrigger()
    DisableTrigger(gg_trg_AutoChance_2)
    TriggerRegisterAnyUnitEventBJ(gg_trg_AutoChance_2, EVENT_PLAYER_UNIT_DAMAGED)
    TriggerAddCondition(gg_trg_AutoChance_2, Condition(Trig_AutoChance_2_Conditions))
    TriggerAddAction(gg_trg_AutoChance_2, Trig_AutoChance_2_Actions)
end
--===========================================================================
-- Trigger: AutoChance 3
--===========================================================================
function Trig_AutoChance_3_Func003C()
    return (( GetUnitAbilityLevelSwapped(FourCC('A01B'), GetEventDamageSource()) >= 1 )) and IsPlayerEnemy(GetOwningPlayer(GetTriggerUnit()), GetOwningPlayer(GetEventDamageSource()))
end
function Trig_AutoChance_3_Conditions()
    return Trig_AutoChance_3_Func003C()
end
function Trig_AutoChance_3_Func002Func001C()
    return GetUnitAbilityLevelSwapped(FourCC('A01B'), GetEventDamageSource()) == 1
end
function Trig_AutoChance_3_Func002Func002C()
    return GetUnitAbilityLevelSwapped(FourCC('A01B'), GetEventDamageSource()) == 2
end
function Trig_AutoChance_3_Func002Func003C()
    return GetUnitAbilityLevelSwapped(FourCC('A01B'), GetEventDamageSource()) == 3
end
function Trig_AutoChance_3_Func002C()
    return udg_LocalInteger <= ( GetUnitAbilityLevelSwapped(FourCC('A00M'), GetEventDamageSource()) * 1 )
end
function Trig_AutoChance_3_Actions()
    udg_LocalInteger=GetRandomInt(1, 175)
    if Trig_AutoChance_3_Func002C() then
        if Trig_AutoChance_3_Func002Func001C() then
            AdjustPlayerStateBJ(2500, GetOwningPlayer(GetEventDamageSource()), PLAYER_STATE_RESOURCE_GOLD)
            AdjustPlayerStateBJ(1000, GetOwningPlayer(GetEventDamageSource()), PLAYER_STATE_RESOURCE_LUMBER)
        end
        if Trig_AutoChance_3_Func002Func002C() then
            AdjustPlayerStateBJ(1000, GetOwningPlayer(GetEventDamageSource()), PLAYER_STATE_RESOURCE_GOLD)
            AdjustPlayerStateBJ(500, GetOwningPlayer(GetEventDamageSource()), PLAYER_STATE_RESOURCE_LUMBER)
        end
        if Trig_AutoChance_3_Func002Func003C() then
            AdjustPlayerStateBJ(250, GetOwningPlayer(GetEventDamageSource()), PLAYER_STATE_RESOURCE_GOLD)
            AdjustPlayerStateBJ(100, GetOwningPlayer(GetEventDamageSource()), PLAYER_STATE_RESOURCE_LUMBER)
        end
        IssueImmediateOrderBJ(GetEventDamageSource(), "berserk")
    end
end
--===========================================================================
function InitTrig_AutoChance_3()
    gg_trg_AutoChance_3=CreateTrigger()
    DisableTrigger(gg_trg_AutoChance_3)
    TriggerRegisterAnyUnitEventBJ(gg_trg_AutoChance_3, EVENT_PLAYER_UNIT_DAMAGED)
    TriggerAddCondition(gg_trg_AutoChance_3, Condition(Trig_AutoChance_3_Conditions))
    TriggerAddAction(gg_trg_AutoChance_3, Trig_AutoChance_3_Actions)
end
--===========================================================================
-- Trigger: Dovorougenie Code O
--===========================================================================
function Trig_Dovorougenie_Code_Func001C()
    return GetUnitTypeId(GetTriggerUnit()) == FourCC('h003')
end
function Trig_Dovorougenie_Code_Func002C()
    return GetUnitTypeId(GetTriggerUnit()) == FourCC('h00P')
end
function Trig_Dovorougenie_Code_Func003C()
    return GetUnitTypeId(GetTriggerUnit()) == FourCC('h029')
end
function Trig_Dovorougenie_Code_Func004C()
    return GetUnitTypeId(GetTriggerUnit()) == FourCC('n000')
end
function Trig_Dovorougenie_Code_O_Actions()
    local u = GetTriggerUnit()
    local pi = GetPlayerId(GetOwningPlayer(u))
    if Trig_Dovorougenie_Code_Func001C() then
        aiFixTrainBefore(u, pi)
        ReplaceUnit2(u , FourCC('h005') , bj_UNIT_STATE_METHOD_RELATIVE)
        aiFixTrainAfter(GetLastReplacedUnitBJ(), pi)
        if Trig_Dovorougenie_3t_O_Copy_Func001C() then
            SelectUnitAddForPlayer(GetLastReplacedUnitBJ(), GetOwningPlayer(u))
        end
    end
    if Trig_Dovorougenie_Code_Func002C() then
        aiFixTrainBefore(u, pi)
        ReplaceUnit2(u , FourCC('h00S') , bj_UNIT_STATE_METHOD_RELATIVE)
        aiFixTrainAfter(GetLastReplacedUnitBJ(), pi)
        if Trig_Dovorougenie_3t_O_Copy_Func001C() then
            SelectUnitAddForPlayer(GetLastReplacedUnitBJ(), GetOwningPlayer(u))
        end
    end
    if Trig_Dovorougenie_Code_Func003C() then
        aiFixTrainBefore(u, pi)
        ReplaceUnit2(u , FourCC('h02A') , bj_UNIT_STATE_METHOD_RELATIVE)
        aiFixTrainAfter(GetLastReplacedUnitBJ(), pi)
        if Trig_Dovorougenie_3t_O_Copy_Func001C() then
            SelectUnitAddForPlayer(GetLastReplacedUnitBJ(), GetOwningPlayer(u))
        end
    end
    if Trig_Dovorougenie_Code_Func004C() then
        aiFixTrainBefore(u, pi)
        ReplaceUnit2(u , FourCC('n002') , bj_UNIT_STATE_METHOD_RELATIVE)
        aiFixTrainAfter(GetLastReplacedUnitBJ(), pi)
        if Trig_Dovorougenie_3t_O_Copy_Func001C() then
            SelectUnitAddForPlayer(GetLastReplacedUnitBJ(), GetOwningPlayer(u))
        end
    end
end
--===========================================================================
function InitTrig_Dovorougenie_Code_O()
    gg_trg_Dovorougenie_Code_O=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_Dovorougenie_Code_O, EVENT_PLAYER_UNIT_SPELL_EFFECT)
    TriggerAddAction(gg_trg_Dovorougenie_Code_O, function()
        if GetSpellAbilityId() ~= FourCC('A000') then return end
        if not (IsUnitSelected(GetTriggerUnit(), GetOwningPlayer(GetTriggerUnit()))) then return end
        Trig_Dovorougenie_Code_O_Actions()
    end)
    udg_LocalPlayer=GetOwningPlayer(GetTriggerUnit())
    TriggerAddAction(gg_trg_Dovorougenie_Code_O, Trig_Del1FromTable_C_Actions)
end
--===========================================================================
-- Trigger: Dovorougenie 2t Code O
--===========================================================================
function Trig_Dovorougenie_2t_Code_Func001C()
    return GetUnitTypeId(GetTriggerUnit()) == FourCC('h005')
end
function Trig_Dovorougenie_2t_Code_Func002C()
    return GetUnitTypeId(GetTriggerUnit()) == FourCC('h00S')
end
function Trig_Dovorougenie_2t_Code_Func003C()
    return GetUnitTypeId(GetTriggerUnit()) == FourCC('h02A')
end
function Trig_Dovorougenie_2t_Code_Func004C()
    return GetUnitTypeId(GetTriggerUnit()) == FourCC('n002')
end
function Trig_Dovorougenie_2t_Code_O_Actions()
    local u = GetTriggerUnit()
    local pi = GetPlayerId(GetOwningPlayer(u))
    if Trig_Dovorougenie_2t_Code_Func001C() then
        aiFixTrainBefore(u, pi)
        ReplaceUnit2(u , FourCC('h006') , bj_UNIT_STATE_METHOD_RELATIVE)
        aiFixTrainAfter(GetLastReplacedUnitBJ(), pi)
        if Trig_Dovorougenie_3t_O_Copy_Func001C() then
            SelectUnitAddForPlayer(GetLastReplacedUnitBJ(), GetOwningPlayer(u))
        end
    end
    if Trig_Dovorougenie_2t_Code_Func002C() then
        aiFixTrainBefore(u, pi)
        ReplaceUnit2(u , FourCC('h00U') , bj_UNIT_STATE_METHOD_RELATIVE)
        aiFixTrainAfter(GetLastReplacedUnitBJ(), pi)
        if Trig_Dovorougenie_3t_O_Copy_Func001C() then
            SelectUnitAddForPlayer(GetLastReplacedUnitBJ(), GetOwningPlayer(u))
        end
    end
    if Trig_Dovorougenie_2t_Code_Func003C() then
        aiFixTrainBefore(u, pi)
        ReplaceUnit2(u , FourCC('h02B') , bj_UNIT_STATE_METHOD_RELATIVE)
        aiFixTrainAfter(GetLastReplacedUnitBJ(), pi)
        if Trig_Dovorougenie_3t_O_Copy_Func001C() then
            SelectUnitAddForPlayer(GetLastReplacedUnitBJ(), GetOwningPlayer(u))
        end
    end
    if Trig_Dovorougenie_2t_Code_Func004C() then
        aiFixTrainBefore(u, pi)
        ReplaceUnit2(u , FourCC('n004') , bj_UNIT_STATE_METHOD_RELATIVE)
        aiFixTrainAfter(GetLastReplacedUnitBJ(), pi)
        if Trig_Dovorougenie_3t_O_Copy_Func001C() then
            SelectUnitAddForPlayer(GetLastReplacedUnitBJ(), GetOwningPlayer(u))
        end
    end
end
--===========================================================================
function InitTrig_Dovorougenie_2t_Code_O()
    gg_trg_Dovorougenie_2t_Code_O=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_Dovorougenie_2t_Code_O, EVENT_PLAYER_UNIT_SPELL_EFFECT)
    TriggerAddAction(gg_trg_Dovorougenie_2t_Code_O, function()
        if GetSpellAbilityId() ~= FourCC('A01A') then return end
        if not (IsUnitSelected(GetTriggerUnit(), GetOwningPlayer(GetTriggerUnit()))) then return end
        Trig_Dovorougenie_2t_Code_O_Actions()
    end)
    TriggerAddAction(gg_trg_Dovorougenie_2t_Code_O, Trig_Del1FromTable_C_Actions)
end
--===========================================================================
-- Trigger: Dovorougenie 3t O
--===========================================================================
function Trig_Dovorougenie_3t_O_Conditions()
    return IsUnitSelected(GetTriggerUnit(), GetOwningPlayer(GetTriggerUnit()))
end
function Trig_Dovorougenie_3t_O_Func002Func002C()
    return IsUnitSelected(GetTriggerUnit(), GetOwningPlayer(GetTriggerUnit()))
end
function Trig_Dovorougenie_3t_O_Func002C()
    return GetUnitTypeId(GetTriggerUnit()) == FourCC('h006')
end
function Trig_Dovorougenie_3t_O_Actions()
    local u = GetTriggerUnit()
    local i= GetPlayerId(GetOwningPlayer(u))
    if Trig_Dovorougenie_3t_O_Func002C() then
    aiFixTrainBefore(u, i)
    ReplaceUnit2(u , FourCC('h00Q') , bj_UNIT_STATE_METHOD_RELATIVE)
    aiFixTrainAfter(GetLastReplacedUnitBJ(), i)
    if Trig_Dovorougenie_3t_O_Func002Func002C() then
        SelectUnitAddForPlayer(GetLastReplacedUnitBJ(), GetOwningPlayer(u))
    end
end
    MultiboardSetItemValue(MultiboardItem[MultiboardItemOwnerIndex[i] * 2 + 1], I2S(udg_UnitsCount[i]))
    i=0
end
--===========================================================================
function InitTrig_Dovorougenie_3t_O()
    gg_trg_Dovorougenie_3t_O=CreateTrigger()
    DisableTrigger(gg_trg_Dovorougenie_3t_O)
    TriggerRegisterAnyUnitEventBJ(gg_trg_Dovorougenie_3t_O, EVENT_PLAYER_UNIT_SPELL_EFFECT)
    TriggerAddAction(gg_trg_Dovorougenie_3t_O, function()
        if GetSpellAbilityId() ~= FourCC('A01B') then return end
        if not Trig_Dovorougenie_3t_O_Conditions() then return end
        Trig_Dovorougenie_3t_O_Actions()
    end)
end
--===========================================================================
-- Trigger: Voron
--===========================================================================
function Trig_Voron_Conditions()
    return GetResearched() == FourCC('R00A')
end
function Trig_Voron_Actions()
    SetPlayerTechMaxAllowedSwap(FourCC('h02S'), - 1, GetOwningPlayer(GetTriggerUnit()))
    SetPlayerTechMaxAllowedSwap(FourCC('h02U'), 0, GetOwningPlayer(GetTriggerUnit()))
    SetPlayerTechResearchedSwap(FourCC('R00B'), 0, GetOwningPlayer(GetTriggerUnit()))
end
--===========================================================================
function InitTrig_Voron()
    gg_trg_Voron=CreateTrigger()
    DisableTrigger(gg_trg_Voron)
    TriggerRegisterAnyUnitEventBJ(gg_trg_Voron, EVENT_PLAYER_UNIT_RESEARCH_FINISH)
    TriggerAddCondition(gg_trg_Voron, Condition(Trig_Voron_Conditions))
    TriggerAddAction(gg_trg_Voron, Trig_Voron_Actions)
end
--===========================================================================
-- Trigger: Sindicat
--===========================================================================
function Trig_Sindicat_Conditions()
    return GetResearched() == FourCC('R00B')
end
function Trig_Sindicat_Actions()
    SetPlayerTechMaxAllowedSwap(FourCC('h02U'), - 1, GetOwningPlayer(GetTriggerUnit()))
    SetPlayerTechMaxAllowedSwap(FourCC('h02S'), 0, GetOwningPlayer(GetTriggerUnit()))
    SetPlayerTechResearchedSwap(FourCC('R00A'), 0, GetOwningPlayer(GetTriggerUnit()))
end
--===========================================================================
function InitTrig_Sindicat()
    gg_trg_Sindicat=CreateTrigger()
    DisableTrigger(gg_trg_Sindicat)
    TriggerRegisterAnyUnitEventBJ(gg_trg_Sindicat, EVENT_PLAYER_UNIT_RESEARCH_FINISH)
    TriggerAddCondition(gg_trg_Sindicat, Condition(Trig_Sindicat_Conditions))
    TriggerAddAction(gg_trg_Sindicat, Trig_Sindicat_Actions)
end
--===========================================================================
-- Trigger: Bratstwo
--===========================================================================
function Trig_Bratstwo_Conditions()
    return GetResearched() == FourCC('R00F')
end
function Trig_Bratstwo_Actions()
    SetPlayerTechMaxAllowedSwap(FourCC('h02Q'), - 1, GetOwningPlayer(GetTriggerUnit()))
end
--===========================================================================
function InitTrig_Bratstwo()
    gg_trg_Bratstwo=CreateTrigger()
    DisableTrigger(gg_trg_Bratstwo)
    TriggerRegisterAnyUnitEventBJ(gg_trg_Bratstwo, EVENT_PLAYER_UNIT_RESEARCH_FINISH)
    TriggerAddCondition(gg_trg_Bratstwo, Condition(Trig_Bratstwo_Conditions))
    TriggerAddAction(gg_trg_Bratstwo, Trig_Bratstwo_Actions)
end
--===========================================================================
-- Trigger: Pirats
--===========================================================================
function Trig_Pirats_Conditions()
    return GetResearched() == FourCC('R00E')
end
function Trig_Pirats_O_Copy_Func005002()
    return GetUnitTypeId(GetFilterUnit()) == FourCC('h00Y')
end
function Trig_Pirats_O_Copy_Func008A()
    local u = GetEnumUnit()
    local pi = GetPlayerId(GetOwningPlayer(u))
    aiFixTrainBefore(u, pi)
    ReplaceUnit(u , FourCC('h03L') , bj_UNIT_STATE_METHOD_RELATIVE)
    aiFixTrainAfter(GetLastReplacedUnitBJ(), pi)
end
function Trig_Pirats_O_Copy_Func010002()
    return GetUnitTypeId(GetFilterUnit()) == FourCC('h00Z')
end
function Trig_Pirats_O_Copy_Func013A()
    local u = GetEnumUnit()
    local pi = GetPlayerId(GetOwningPlayer(u))
    aiFixTrainBefore(u, pi)
    ReplaceUnit(u , FourCC('h03K') , bj_UNIT_STATE_METHOD_RELATIVE)
    aiFixTrainAfter(GetLastReplacedUnitBJ(), pi)
end
function Trig_Pirats_Actions()
    SetPlayerTechMaxAllowedSwap(FourCC('h03L'), - 1, GetOwningPlayer(GetTriggerUnit()))
    SetPlayerTechMaxAllowedSwap(FourCC('h03K'), - 1, GetOwningPlayer(GetTriggerUnit()))
    SetPlayerTechMaxAllowedSwap(FourCC('h00Y'), 0, GetOwningPlayer(GetTriggerUnit()))
    SetPlayerTechMaxAllowedSwap(FourCC('h00Z'), 0, GetOwningPlayer(GetTriggerUnit()))
    udg_Boolexpr = Trig_Pirats_O_Copy_Func005002
    udg_LocalPlayer=GetOwningPlayer(GetTriggerUnit())
    GroupEnumUnitsOfPlayer(udg_LocalOtrad2, udg_LocalPlayer, udg_Boolexpr)
    ForGroupBJ(udg_LocalOtrad2, Trig_Pirats_O_Copy_Func008A)
    GroupClear(udg_LocalOtrad2)
    udg_Boolexpr = Trig_Pirats_O_Copy_Func010002
    udg_LocalPlayer=GetOwningPlayer(GetTriggerUnit())
    GroupEnumUnitsOfPlayer(udg_LocalOtrad2, udg_LocalPlayer, udg_Boolexpr)
    ForGroupBJ(udg_LocalOtrad2, Trig_Pirats_O_Copy_Func013A)
    GroupClear(udg_LocalOtrad2)
end
--===========================================================================
function InitTrig_Pirats()
    gg_trg_Pirats=CreateTrigger()
    DisableTrigger(gg_trg_Pirats)
    TriggerRegisterAnyUnitEventBJ(gg_trg_Pirats, EVENT_PLAYER_UNIT_RESEARCH_FINISH)
    TriggerAddCondition(gg_trg_Pirats, Condition(Trig_Pirats_Conditions))
    TriggerAddAction(gg_trg_Pirats, Trig_Pirats_Actions)
end
--===========================================================================
-- Trigger: Shesterenka
--===========================================================================
function Trig_Shesterenka_Conditions()
    return GetResearched() == FourCC('R00D')
end
function Trig_Shesterenka_Actions()
    SetPlayerTechMaxAllowedSwap(FourCC('h02R'), - 1, GetOwningPlayer(GetTriggerUnit()))
    SetPlayerTechMaxAllowedSwap(FourCC('h02T'), 0, GetOwningPlayer(GetTriggerUnit()))
    SetPlayerTechResearchedSwap(FourCC('R00C'), 0, GetOwningPlayer(GetTriggerUnit()))
end
--===========================================================================
function InitTrig_Shesterenka()
    gg_trg_Shesterenka=CreateTrigger()
    DisableTrigger(gg_trg_Shesterenka)
    TriggerRegisterAnyUnitEventBJ(gg_trg_Shesterenka, EVENT_PLAYER_UNIT_RESEARCH_FINISH)
    TriggerAddCondition(gg_trg_Shesterenka, Condition(Trig_Shesterenka_Conditions))
    TriggerAddAction(gg_trg_Shesterenka, Trig_Shesterenka_Actions)
end
--===========================================================================
-- Trigger: Trumnue vodu
--===========================================================================
function Trig_Trumnue_vodu_Conditions()
    return GetResearched() == FourCC('R00C')
end
function Trig_Trumnue_vodu_Actions()
    SetPlayerTechMaxAllowedSwap(FourCC('h02T'), - 1, GetOwningPlayer(GetTriggerUnit()))
    SetPlayerTechMaxAllowedSwap(FourCC('h02R'), 0, GetOwningPlayer(GetTriggerUnit()))
    SetPlayerTechResearchedSwap(FourCC('R00D'), 0, GetOwningPlayer(GetTriggerUnit()))
end
--===========================================================================
function InitTrig_Trumnue_vodu()
    gg_trg_Trumnue_vodu=CreateTrigger()
    DisableTrigger(gg_trg_Trumnue_vodu)
    TriggerRegisterAnyUnitEventBJ(gg_trg_Trumnue_vodu, EVENT_PLAYER_UNIT_RESEARCH_FINISH)
    TriggerAddCondition(gg_trg_Trumnue_vodu, Condition(Trig_Trumnue_vodu_Conditions))
    TriggerAddAction(gg_trg_Trumnue_vodu, Trig_Trumnue_vodu_Actions)
end
--===========================================================================
-- Trigger: AutoSetka
--===========================================================================
function Trig_AutoSetka_Actions()
    IssueTargetOrderBJ(GetTriggerUnit(), "ensnare", GetSpellTargetUnit())
end
--===========================================================================
function InitTrig_AutoSetka()
    gg_trg_AutoSetka=CreateTrigger()
    DisableTrigger(gg_trg_AutoSetka)
    TriggerRegisterAnyUnitEventBJ(gg_trg_AutoSetka, EVENT_PLAYER_UNIT_SPELL_EFFECT)
    TriggerAddAction(gg_trg_AutoSetka, function()
        if GetSpellAbilityId() ~= FourCC('A011') then return end
        Trig_AutoSetka_Actions()
    end)
end
--===========================================================================
-- Trigger: AutoSetkaHero
--===========================================================================
function Trig_AutoSetkaHero_Actions()
    UnitAddAbilityBJ(FourCC('A011'), GetTriggerUnit())
end
--===========================================================================
function InitTrig_AutoSetkaHero()
    gg_trg_AutoSetkaHero=CreateTrigger()
    DisableTrigger(gg_trg_AutoSetkaHero)
    TriggerRegisterAnyUnitEventBJ(gg_trg_AutoSetkaHero, EVENT_PLAYER_HERO_SKILL)
    TriggerAddAction(gg_trg_AutoSetkaHero, function()
        if GetSpellAbilityId() ~= FourCC('A01I') then return end
        Trig_AutoSetkaHero_Actions()
    end)
end
--===========================================================================
-- Trigger: AutoSvita
--===========================================================================
function Trig_AutoSvita_Actions()
    IssueImmediateOrderBJ(GetTriggerUnit(), "waterelemental")
end
--===========================================================================
function InitTrig_AutoSvita()
    gg_trg_AutoSvita=CreateTrigger()
    DisableTrigger(gg_trg_AutoSvita)
    TriggerRegisterAnyUnitEventBJ(gg_trg_AutoSvita, EVENT_PLAYER_UNIT_SPELL_EFFECT)
    TriggerAddAction(gg_trg_AutoSvita, function()
        if GetSpellAbilityId() ~= FourCC('A012') then return end
        Trig_AutoSvita_Actions()
    end)
end
--===========================================================================
-- Trigger: AutoStaya
--===========================================================================
function Trig_AutoStaya_Actions()
    IssuePointOrderLocBJ(GetTriggerUnit(), "carrionswarm", GetUnitLoc(GetSpellTargetUnit()))
end
--===========================================================================
function InitTrig_AutoStaya()
    gg_trg_AutoStaya=CreateTrigger()
    DisableTrigger(gg_trg_AutoStaya)
    TriggerRegisterAnyUnitEventBJ(gg_trg_AutoStaya, EVENT_PLAYER_UNIT_SPELL_EFFECT)
    TriggerAddAction(gg_trg_AutoStaya, function()
        if GetSpellAbilityId() ~= FourCC('A00W') then return end
        Trig_AutoStaya_Actions()
    end)
end
--===========================================================================
-- Trigger: AutoManaSteal
--===========================================================================
function Trig_AutoManaSteal_Actions()
    IssueTargetOrderBJ(GetTriggerUnit(), "drain", GetSpellTargetUnit())
end
--===========================================================================
function InitTrig_AutoManaSteal()
    gg_trg_AutoManaSteal=CreateTrigger()
    DisableTrigger(gg_trg_AutoManaSteal)
    TriggerRegisterAnyUnitEventBJ(gg_trg_AutoManaSteal, EVENT_PLAYER_UNIT_SPELL_EFFECT)
    TriggerAddAction(gg_trg_AutoManaSteal, function()
        if GetSpellAbilityId() ~= FourCC('A015') then return end
        Trig_AutoManaSteal_Actions()
    end)
end
--===========================================================================
-- Trigger: AutoShield
--===========================================================================
function Trig_AutoShield_Actions()
    IssueTargetOrderBJ(GetTriggerUnit(), "antimagicshell", GetSpellTargetUnit())
end
--===========================================================================
function InitTrig_AutoShield()
    gg_trg_AutoShield=CreateTrigger()
    DisableTrigger(gg_trg_AutoShield)
    TriggerRegisterAnyUnitEventBJ(gg_trg_AutoShield, EVENT_PLAYER_UNIT_SPELL_EFFECT)
    TriggerAddAction(gg_trg_AutoShield, function()
        if GetSpellAbilityId() ~= FourCC('A016') then return end
        Trig_AutoShield_Actions()
    end)
end
--===========================================================================
-- Trigger: ResearhRobbery
--===========================================================================
function Trig_ResearhRobbery_Conditions()
    return GetResearched() == FourCC('R00I')
end
function Trig_ResearhRobbery_Func001Func001002()
    return GetUnitAbilityLevelSwapped(FourCC('A00M'), GetTriggerUnit()) >= 1
end
function Trig_ResearhRobbery_Func001Func004A()
    SetUnitAbilityLevelSwapped(FourCC('A00M'), GetEnumUnit(), 2)
end
function Trig_ResearhRobbery_Func001C()
    return GetPlayerTechCountSimple(FourCC('R00I'), GetOwningPlayer(GetTriggerUnit())) == 2
end
function Trig_ResearhRobbery_Func002Func001002()
    return GetUnitAbilityLevelSwapped(FourCC('A00M'), GetTriggerUnit()) >= 1
end
function Trig_ResearhRobbery_Func002Func004A()
    SetUnitAbilityLevelSwapped(FourCC('A00M'), GetEnumUnit(), 3)
end
function Trig_ResearhRobbery_Func002C()
    return GetPlayerTechCountSimple(FourCC('R00I'), GetOwningPlayer(GetTriggerUnit())) == 3
end
function Trig_ResearhRobbery_Func003Func001002()
    return GetUnitAbilityLevelSwapped(FourCC('A00M'), GetTriggerUnit()) >= 1
end
function Trig_ResearhRobbery_Func003Func004A()
    SetUnitAbilityLevelSwapped(FourCC('A00M'), GetEnumUnit(), 4)
end
function Trig_ResearhRobbery_Func003C()
    return GetPlayerTechCountSimple(FourCC('R00I'), GetOwningPlayer(GetTriggerUnit())) == 4
end
function Trig_ResearhRobbery_Actions()
    if Trig_ResearhRobbery_Func001C() then
        udg_Boolexpr = Trig_ResearhRobbery_Func001Func001002
        GroupEnumUnitsOfPlayer(udg_LocalOtrad2, udg_LocalPlayer, udg_Boolexpr)
        ForGroupBJ(udg_LocalOtrad2, Trig_ResearhRobbery_Func001Func004A)
        GroupClear(udg_LocalOtrad2)
    end
    if Trig_ResearhRobbery_Func002C() then
        udg_Boolexpr = Trig_ResearhRobbery_Func002Func001002
        GroupEnumUnitsOfPlayer(udg_LocalOtrad2, udg_LocalPlayer, udg_Boolexpr)
        ForGroupBJ(udg_LocalOtrad2, Trig_ResearhRobbery_Func002Func004A)
        GroupClear(udg_LocalOtrad2)
    end
    if Trig_ResearhRobbery_Func003C() then
        udg_Boolexpr = Trig_ResearhRobbery_Func003Func001002
        GroupEnumUnitsOfPlayer(udg_LocalOtrad2, udg_LocalPlayer, udg_Boolexpr)
        ForGroupBJ(udg_LocalOtrad2, Trig_ResearhRobbery_Func003Func004A)
        GroupClear(udg_LocalOtrad2)
    end
end
--===========================================================================
function InitTrig_ResearhRobbery()
    gg_trg_ResearhRobbery=CreateTrigger()
    DisableTrigger(gg_trg_ResearhRobbery)
    TriggerRegisterAnyUnitEventBJ(gg_trg_ResearhRobbery, EVENT_PLAYER_UNIT_RESEARCH_FINISH)
    TriggerAddCondition(gg_trg_ResearhRobbery, Condition(Trig_ResearhRobbery_Conditions))
    TriggerAddAction(gg_trg_ResearhRobbery, Trig_ResearhRobbery_Actions)
end
--===========================================================================
-- Trigger: RobberyTrain
--===========================================================================
function Trig_RobberyTrain_Conditions()
    return GetUnitAbilityLevelSwapped(FourCC('A00M'), GetTriggerUnit()) == 1
end
function Trig_RobberyTrain_Func002C()
    return GetPlayerTechCountSimple(FourCC('R00I'), GetOwningPlayer(GetTriggerUnit())) == 2
end
function Trig_RobberyTrain_Func003C()
    return GetPlayerTechCountSimple(FourCC('R00I'), GetOwningPlayer(GetTriggerUnit())) == 3
end
function Trig_RobberyTrain_Func004C()
    return GetPlayerTechCountSimple(FourCC('R00I'), GetOwningPlayer(GetTriggerUnit())) == 4
end
function Trig_RobberyTrain_Actions()
    if Trig_RobberyTrain_Func002C() then
        SetUnitAbilityLevelSwapped(FourCC('A00M'), GetTrainedUnit(), 2)
    end
    if Trig_RobberyTrain_Func003C() then
        SetUnitAbilityLevelSwapped(FourCC('A00M'), GetTrainedUnit(), 3)
    end
    if Trig_RobberyTrain_Func004C() then
        SetUnitAbilityLevelSwapped(FourCC('A00M'), GetTrainedUnit(), 4)
    end
end
--===========================================================================
function InitTrig_RobberyTrain()
    gg_trg_RobberyTrain=CreateTrigger()
    DisableTrigger(gg_trg_RobberyTrain)
    TriggerRegisterAnyUnitEventBJ(gg_trg_RobberyTrain, EVENT_PLAYER_UNIT_TRAIN_FINISH)
    TriggerAddCondition(gg_trg_RobberyTrain, Condition(Trig_RobberyTrain_Conditions))
    TriggerAddAction(gg_trg_RobberyTrain, Trig_RobberyTrain_Actions)
end
--===========================================================================
-- Trigger: RobberyOfPlayer
--===========================================================================
function Trig_RobberyOfPlayer_Conditions()
    return GetUnitAbilityLevel(GetEventDamageSource(), FourCC('A00M')) >= 1
end
function Trig_RobberyOfPlayer_Actions()
    local i= GetUnitGoldCost(GetUnitTypeId(GetTriggerUnit()))
    local lvl= GetUnitAbilityLevel(GetEventDamageSource(), FourCC('A00M'))
    
    i=R2I(i * 0.25 * lvl)
    AdjustPlayerStateBJ(- i, GetOwningPlayer(GetEventDamageSource()), PLAYER_STATE_RESOURCE_GOLD)
end
--===========================================================================
function InitTrig_RobberyOfPlayer()
    gg_trg_RobberyOfPlayer=CreateTrigger()
    DisableTrigger(gg_trg_RobberyOfPlayer)
    TriggerRegisterAnyUnitEventBJ(gg_trg_RobberyOfPlayer, EVENT_PLAYER_UNIT_DAMAGED)
    TriggerAddCondition(gg_trg_RobberyOfPlayer, Condition(Trig_RobberyOfPlayer_Conditions))
    TriggerAddAction(gg_trg_RobberyOfPlayer, Trig_RobberyOfPlayer_Actions)
end
--===========================================================================
-- Trigger: AreaOfDeath2
--===========================================================================
function Trig_AreaOfDeath2_Actions()
    local l= GetSpellTargetLoc()
    local p= GetOwningPlayer(GetTriggerUnit())
    local level= GetUnitAbilityLevel(GetTriggerUnit(), FourCC('A1K1'))
    
    local u
    local u2
    local i= 0
   
    
    u2=CreateUnitAtLoc(p, Dummy, l, bj_UNIT_FACING)
    UnitAddAbility(u2, FourCC('ANrf'))
    SetUnitManaBJ(u2, 1111111.00)
    SetUnitAbilityLevel(u2, FourCC('ANrf'), level)
    IssuePointOrderLoc(u2, "rainoffire", l)
    RemoveLocation(l)
    
    RemoveUnitTimed(u2 , 25)
    
    u=nil
    
    p=nil
    u2=nil
end
--===========================================================================
function InitTrig_AreaOfDeath2()
    gg_trg_AreaOfDeath2=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_AreaOfDeath2, EVENT_PLAYER_UNIT_SPELL_EFFECT)
    TriggerAddAction(gg_trg_AreaOfDeath2, function()
        if GetSpellAbilityId() ~= FourCC('A1K1') then return end
        Trig_AreaOfDeath2_Actions()
    end)
end