
--===========================================================================
-- Trigger: Leave Ot
--===========================================================================
function Trig_Leave_Ot_Func005C()
    return IsTriggerEnabled(gg_trg_FeodalDead2)
end
function Trig_Leave_Ot_Actions()
    local pi= GetPlayerId(GetTriggerPlayer())
    DisplayTextToForce(udg_AllPlayers, ( GetPlayerName(GetTriggerPlayer()) .. "cffff0000 - r" ))
    ClearPlayer(Player(pi))
    FlushChildHashtable(Hash, GetPlayerId(GetTriggerPlayer()))
    if Trig_Leave_Ot_Func005C() then
        ForForce(Vassals[pi], Freedom)
    end
end
--===========================================================================
function InitTrig_Leave_Ot()
    gg_trg_Leave_Ot=CreateTrigger()
    TriggerRegisterPlayerEventLeave(gg_trg_Leave_Ot, Player(0))
    TriggerRegisterPlayerEventLeave(gg_trg_Leave_Ot, Player(1))
    TriggerRegisterPlayerEventLeave(gg_trg_Leave_Ot, Player(2))
    TriggerRegisterPlayerEventLeave(gg_trg_Leave_Ot, Player(3))
    TriggerRegisterPlayerEventLeave(gg_trg_Leave_Ot, Player(4))
    TriggerRegisterPlayerEventLeave(gg_trg_Leave_Ot, Player(5))
    TriggerRegisterPlayerEventLeave(gg_trg_Leave_Ot, Player(6))
    TriggerRegisterPlayerEventLeave(gg_trg_Leave_Ot, Player(7))
    TriggerRegisterPlayerEventLeave(gg_trg_Leave_Ot, Player(8))
    TriggerRegisterPlayerEventLeave(gg_trg_Leave_Ot, Player(9))
    TriggerRegisterPlayerEventLeave(gg_trg_Leave_Ot, Player(10))
    TriggerRegisterPlayerEventLeave(gg_trg_Leave_Ot, Player(11))
    TriggerRegisterPlayerEventLeave(gg_trg_Leave_Ot, Player(12))
    TriggerRegisterPlayerEventLeave(gg_trg_Leave_Ot, Player(13))
    TriggerRegisterPlayerEventLeave(gg_trg_Leave_Ot, Player(14))
    TriggerRegisterPlayerEventLeave(gg_trg_Leave_Ot, Player(15))
    TriggerRegisterPlayerEventLeave(gg_trg_Leave_Ot, Player(16))
    TriggerRegisterPlayerEventLeave(gg_trg_Leave_Ot, Player(17))
    TriggerRegisterPlayerEventLeave(gg_trg_Leave_Ot, Player(18))
    TriggerRegisterPlayerEventLeave(gg_trg_Leave_Ot, Player(19))
    TriggerRegisterPlayerEventLeave(gg_trg_Leave_Ot, Player(20))
    TriggerRegisterPlayerEventLeave(gg_trg_Leave_Ot, Player(21))
    TriggerRegisterPlayerEventLeave(gg_trg_Leave_Ot, Player(22))
    TriggerRegisterPlayerEventLeave(gg_trg_Leave_Ot, Player(23))
    TriggerAddAction(gg_trg_Leave_Ot, Trig_Leave_Ot_Actions)
end
--===========================================================================
-- Trigger: Spell Copy 2
--===========================================================================
function Trig_Spell_Copy_2_Conditions()
    return GetLearnedSkillBJ() == FourCC('A1BR')
end
function Trig_Spell_Copy_2_Actions()
    udg_u=GetLearningUnit()
    TriggerRegisterUnitEvent(gg_trg_Lech, udg_u, EVENT_UNIT_DAMAGED)
    TriggerRegisterUnitEvent(gg_trg_AvtoCast, udg_u, EVENT_UNIT_DAMAGED)
    DisableTrigger(GetTriggeringTrigger())
end
--===========================================================================
function InitTrig_Spell_Copy_2()
    gg_trg_Spell_Copy_2=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_Spell_Copy_2, EVENT_PLAYER_HERO_SKILL)
    TriggerAddCondition(gg_trg_Spell_Copy_2, Condition(Trig_Spell_Copy_2_Conditions))
    TriggerAddAction(gg_trg_Spell_Copy_2, Trig_Spell_Copy_2_Actions)
end
--===========================================================================
-- Trigger: Lech
--===========================================================================
function Trig_Lech_Actions()
    SetUnitLifeBJ(udg_u, ( GetUnitStateSwap(UNIT_STATE_LIFE, udg_u) + GetEventDamage() ))
end
--===========================================================================
function InitTrig_Lech()
    gg_trg_Lech=CreateTrigger()
    DisableTrigger(gg_trg_Lech)
    TriggerAddAction(gg_trg_Lech, Trig_Lech_Actions)
end
--===========================================================================
-- Trigger: Cast
--===========================================================================
function Trig_Cast_Actions()
    EnableTrigger(gg_trg_Lech)
    CreateNUnitsAtLoc(1, FourCC('h0ML'), GetOwningPlayer(udg_u), GetUnitLoc(GetSpellAbilityUnit()), bj_UNIT_FACING)
    UnitAddAbilityBJ(FourCC('A1BS'), GetLastCreatedUnit())
    IssueTargetOrderBJ(GetLastCreatedUnit(), "purge", GetSpellAbilityUnit())
    UnitApplyTimedLifeBJ(1.00, FourCC('BTLF'), GetLastCreatedUnit())
    TriggerSleepAction(( 3.00 + ( 1.00 * I2R(GetUnitAbilityLevelSwapped(FourCC('A0EK'), GetSpellAbilityUnit())) ) ))
    DisableTrigger(gg_trg_Lech)
end
--===========================================================================
function InitTrig_Cast()
    gg_trg_Cast=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_Cast, EVENT_PLAYER_UNIT_SPELL_EFFECT)
    TriggerAddAction(gg_trg_Cast, function()
        if GetSpellAbilityId() ~= FourCC('A1BR') then return end
        Trig_Cast_Actions()
    end)
end
--===========================================================================
-- Trigger: AvtoCast
--===========================================================================
function Trig_AvtoCast_Conditions()
    return GetUnitStateSwap(UNIT_STATE_LIFE, udg_u) <= 400.00
end
function Trig_AvtoCast_Actions()
    IssueImmediateOrderBJ(udg_u, "stomp")
end
--===========================================================================
function InitTrig_AvtoCast()
    gg_trg_AvtoCast=CreateTrigger()
    TriggerAddCondition(gg_trg_AvtoCast, Condition(Trig_AvtoCast_Conditions))
    TriggerAddAction(gg_trg_AvtoCast, Trig_AvtoCast_Actions)
end
--===========================================================================
-- Trigger: DammyDeath
--===========================================================================
function Trig_DammyDeath_Conditions()
    return GetUnitTypeId(GetDyingUnit()) == FourCC('h0ML')
end
function Trig_DammyDeath_Actions()
    RemoveUnit(GetDyingUnit())
end
--===========================================================================
function InitTrig_DammyDeath()
    gg_trg_DammyDeath=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_DammyDeath, EVENT_PLAYER_UNIT_DEATH)
    TriggerAddCondition(gg_trg_DammyDeath, Condition(Trig_DammyDeath_Conditions))
    TriggerAddAction(gg_trg_DammyDeath, Trig_DammyDeath_Actions)
end
--===========================================================================
-- Trigger: No2SameItems
--===========================================================================
function Trig_No2SameItems_Actions()
    local l= GetUnitLoc(GetTriggerUnit())
    local i=0
    local Item= GetManipulatedItem()
    for bj_forLoopAIndex = 1, 6 do
        if GetItemTypeId(Item) == GetItemTypeId(UnitItemInSlotBJ(GetTriggerUnit(), GetForLoopIndexA())) then
            i=i + 1
        end
    end
    
    if i >= 2 then
        UnitDropItemPointLoc(GetTriggerUnit(), Item, l)
        DisplayTextToPlayer(GetOwningPlayer(GetTriggerUnit()), 0, 0, "TRIGSTR_1254")
    
    end
    RemoveLocation(l)
    l=nil
    Item=nil
end
--===========================================================================
function InitTrig_No2SameItems()
    gg_trg_No2SameItems=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_No2SameItems, EVENT_PLAYER_UNIT_PICKUP_ITEM)
    TriggerAddAction(gg_trg_No2SameItems, Trig_No2SameItems_Actions)
end
--===========================================================================
-- Trigger: RainbowMageDamage
--===========================================================================
function Trig_RainbowMageDamage_Conditions()
    return GetInventoryIndexOfItemTypeBJ(GetEventDamageSource(), FourCC('I01U')) > 0 and GetUnitAbilityLevel(GetTriggerUnit(), FourCC('A1LA')) == 0 and BlzGetEventAttackType() == ATTACK_TYPE_NORMAL
end
function Trig_RainbowMageDamage_Actions()
        UnitAddAbility(GetTriggerUnit(), FourCC('A1LA'))
        
        UnitDamageTargetBJ(GetEventDamageSource(), GetTriggerUnit(), GetEventDamage() * 0.25, ATTACK_TYPE_NORMAL, DAMAGE_TYPE_NORMAL)
        RemoveAbilityTimed(GetTriggerUnit() , FourCC('A1LA') , 0.25)
end
--===========================================================================
function InitTrig_RainbowMageDamage()
    gg_trg_RainbowMageDamage=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_RainbowMageDamage, EVENT_PLAYER_UNIT_DAMAGED)
    TriggerAddCondition(gg_trg_RainbowMageDamage, Condition(Trig_RainbowMageDamage_Conditions))
    TriggerAddAction(gg_trg_RainbowMageDamage, Trig_RainbowMageDamage_Actions)
end
--===========================================================================
-- Trigger: SomeThing
--===========================================================================
function Trig_SomeThing_Actions()
    UnitAddAbilityBJ(FourCC('A0S0'), GetTriggerUnit())
    RemoveAbilityTimed(GetTriggerUnit() , FourCC('A0S0') , 25)
end
--===========================================================================
function InitTrig_SomeThing()
    gg_trg_SomeThing=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_SomeThing, EVENT_PLAYER_UNIT_SPELL_EFFECT)
    TriggerAddAction(gg_trg_SomeThing, function()
        if GetSpellAbilityId() ~= FourCC('A0RZ') then return end
        Trig_SomeThing_Actions()
    end)
end
--===========================================================================
-- Trigger: SomeThing2
--===========================================================================
function Trig_SomeThing2_Actions()
    UnitAddAbilityBJ(FourCC('A0NT'), GetTriggerUnit())
    RemoveAbilityTimed(GetTriggerUnit() , FourCC('A0NT') , 20)
end
--===========================================================================
function InitTrig_SomeThing2()
    gg_trg_SomeThing2=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_SomeThing2, EVENT_PLAYER_UNIT_SPELL_EFFECT)
    TriggerAddAction(gg_trg_SomeThing2, function()
        if GetSpellAbilityId() ~= FourCC('A0KA') then return end
        Trig_SomeThing2_Actions()
    end)
end
--===========================================================================
-- Trigger: Pole astrala Elems
--===========================================================================
function Trig_Pole_astrala_Elems_Func003A()
    CreateNUnitsAtLoc(1, FourCC('H0BN'), GetOwningPlayer(GetTriggerUnit()), udg_LocalPosition[14], bj_UNIT_FACING)
    UnitAddAbilityBJ(FourCC('AHbn'), GetLastCreatedUnit())
    SetUnitManaBJ(GetLastCreatedUnit(), 1111111.00)
    SetUnitAbilityLevelSwapped(FourCC('AHbn'), GetLastCreatedUnit(), GetUnitAbilityLevelSwapped(FourCC('A0OT'), GetTriggerUnit()))
    IssueTargetOrderBJ(GetLastCreatedUnit(), "banish", GetEnumUnit())
    udg_LocalUnit2=GetLastCreatedUnit()
    TriggerExecute(gg_trg_ToKill2)
end
function Trig_Pole_astrala_Elems_Actions()
    udg_LocalOtrad=GetUnitsInRangeOfLocAll(200.00, GetSpellTargetLoc())
    udg_LocalPosition[14]=GetUnitLoc(GetTriggerUnit())
    ForGroupBJ(udg_LocalOtrad, Trig_Pole_astrala_Elems_Func003A)
    RemoveLocation(udg_LocalPosition[14])
end
--===========================================================================
function InitTrig_Pole_astrala_Elems()
    gg_trg_Pole_astrala_Elems=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_Pole_astrala_Elems, EVENT_PLAYER_UNIT_SPELL_EFFECT)
    TriggerAddAction(gg_trg_Pole_astrala_Elems, function()
        if GetSpellAbilityId() ~= FourCC('A0OT') then return end
        Trig_Pole_astrala_Elems_Actions()
    end)
end
--===========================================================================
-- Trigger: ItemPoleAstrala
--===========================================================================
function Trig_ItemPoleAstrala_Func003A()
    CreateNUnitsAtLoc(1, FourCC('H0BN'), GetOwningPlayer(GetTriggerUnit()), udg_LocalPosition[14], bj_UNIT_FACING)
    UnitAddAbilityBJ(FourCC('AHbn'), GetLastCreatedUnit())
    SetUnitManaBJ(GetLastCreatedUnit(), 1111111.00)
    IssueTargetOrderBJ(GetLastCreatedUnit(), "banish", GetEnumUnit())
    udg_LocalUnit2=GetLastCreatedUnit()
    TriggerExecute(gg_trg_ToKill2)
end
function Trig_ItemPoleAstrala_Actions()
    udg_LocalOtrad=GetUnitsInRangeOfLocAll(83.00, GetSpellTargetLoc())
    udg_LocalPosition[14]=GetUnitLoc(GetTriggerUnit())
    ForGroupBJ(udg_LocalOtrad, Trig_ItemPoleAstrala_Func003A)
    RemoveLocation(udg_LocalPosition[14])
end
--===========================================================================
function InitTrig_ItemPoleAstrala()
    gg_trg_ItemPoleAstrala=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_ItemPoleAstrala, EVENT_PLAYER_UNIT_SPELL_EFFECT)
    TriggerAddAction(gg_trg_ItemPoleAstrala, function()
        if GetSpellAbilityId() ~= FourCC('A0N9') then return end
        Trig_ItemPoleAstrala_Actions()
    end)
end
--===========================================================================
-- Trigger: AntiMagic Item
--===========================================================================
function Trig_AntiMagic_Item_Func003A()
    CreateNUnitsAtLoc(1, FourCC('H0GB'), GetOwningPlayer(GetTriggerUnit()), udg_LocalPosition[14], bj_UNIT_FACING)
    UnitAddAbilityBJ(FourCC('A0TI'), GetLastCreatedUnit())
    SetUnitManaBJ(GetLastCreatedUnit(), 1111111.00)
    SetUnitAbilityLevelSwapped(FourCC('A0TI'), GetLastCreatedUnit(), GetUnitAbilityLevelSwapped(FourCC('A0TB'), GetTriggerUnit()))
    IssueTargetOrderBJ(GetLastCreatedUnit(), "antimagicshell", GetEnumUnit())
    udg_LocalUnit2=GetLastCreatedUnit()
    TriggerExecute(gg_trg_ToKill2)
end
function Trig_AntiMagic_Item_Actions()
    udg_LocalOtrad=GetUnitsInRangeOfLocAll(200.00, GetSpellTargetLoc())
    udg_LocalPosition[14]=GetUnitLoc(GetTriggerUnit())
    ForGroupBJ(udg_LocalOtrad, Trig_AntiMagic_Item_Func003A)
    RemoveLocation(udg_LocalPosition[14])
end
--===========================================================================
function InitTrig_AntiMagic_Item()
    gg_trg_AntiMagic_Item=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_AntiMagic_Item, EVENT_PLAYER_UNIT_SPELL_EFFECT)
    TriggerAddAction(gg_trg_AntiMagic_Item, function()
        if GetSpellAbilityId() ~= FourCC('A0TB') then return end
        Trig_AntiMagic_Item_Actions()
    end)
end
--===========================================================================
-- Trigger: Spell Copy
--
-- ??????? 3 ???? ??????? ?????? ?????? ????? ?????????? ???? ?? ?? ?? ???????? ??? ?????
-- ???????? ?? ?? ?????? ????? ??????? ?? ???? ? 200 ??? ? ?????? ????????? ????
-- ?????? ?????????? ??? ?????? ?? ?????? ??????????
-- ?????? ?????????? ??? ?????? ?? ?????? ????
-- ?????? ?????????? ??? ?????? ?? ?????? ???????
-- ?? ??????? ??????????? ????? ?? 0 ??? ??? ????? ????
--===========================================================================
function Trig_Spell_Copy_Actions()
    udg_Caster=GetSpellAbilityUnit()
    udg_To4kaCaster=GetUnitLoc(udg_Caster)
    udg_Logika=true
    udg_HisloA[0]=4
    SetPlayerAbilityAvailableBJ(false, FourCC('A1BN'), GetOwningPlayer(udg_Caster))
    SetPlayerAbilityAvailableBJ(true, FourCC('A1BM'), GetOwningPlayer(udg_Caster))
    UnitAddAbilityBJ(FourCC('A1BM'), udg_Caster)
    CreateNUnitsAtLoc(1, FourCC('h0MJ'), GetOwningPlayer(udg_Caster), PolarProjectionBJ(udg_To4kaCaster, 100.00, 0.00), bj_UNIT_FACING)
    udg_Dummy[0]=GetLastCreatedUnit()
    CreateNUnitsAtLoc(1, FourCC('h0MJ'), GetOwningPlayer(udg_Caster), PolarProjectionBJ(udg_To4kaCaster, 100.00, 120.00), bj_UNIT_FACING)
    udg_Dummy[1]=GetLastCreatedUnit()
    CreateNUnitsAtLoc(1, FourCC('h0MJ'), GetOwningPlayer(udg_Caster), PolarProjectionBJ(udg_To4kaCaster, 100.00, 240.00), bj_UNIT_FACING)
    udg_Dummy[2]=GetLastCreatedUnit()
    StartTimerBJ(udg_Timer, true, 0.03)
end
--===========================================================================
function InitTrig_Spell_Copy()
    gg_trg_Spell_Copy=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_Spell_Copy, EVENT_PLAYER_UNIT_SPELL_EFFECT)
    TriggerAddAction(gg_trg_Spell_Copy, function()
        if GetSpellAbilityId() ~= FourCC('A1BN') then return end
        Trig_Spell_Copy_Actions()
    end)
end
--===========================================================================
-- Trigger: Spell Cast
--
-- ??????? 3 ???? ??????? ?????? ?????? ????? ?????????? ???? ?? ?? ?? ???????? ??? ?????
-- ???????? ?? ?? ?????? ????? ??????? ?? ???? ? 200 ??? ? ?????? ????????? ????
-- ?????? ?????????? ??? ?????? ?? ?????? ??????????
-- ?????? ?????????? ??? ?????? ?? ?????? ????
-- ?????? ?????????? ??? ?????? ?? ?????? ???????
-- ?? ??????? ??????????? ????? ?? 0 ??? ??? ????? ????
--===========================================================================
function Trig_Spell_Cast_Actions()
    udg_Target=GetSpellTargetUnit()
    udg_LogikaCast=true
    udg_HisloA[0]=( udg_HisloA[0] - 1 )
end
--===========================================================================
function InitTrig_Spell_Cast()
    gg_trg_Spell_Cast=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_Spell_Cast, EVENT_PLAYER_UNIT_SPELL_EFFECT)
    TriggerAddAction(gg_trg_Spell_Cast, function()
        if GetSpellAbilityId() ~= FourCC('A1BM') then return end
        Trig_Spell_Cast_Actions()
    end)
end
--===========================================================================
-- Trigger: Spell Dvij
--
-- ??????? 3 ???? ??????? ?????? ?????? ????? ?????????? ???? ?? ?? ?? ???????? ??? ?????
-- ???????? ?? ?? ?????? ????? ??????? ?? ???? ? 200 ??? ? ?????? ????????? ????
-- ?????? ?????????? ??? ?????? ?? ?????? ??????????
-- ?????? ?????????? ??? ?????? ?? ?????? ????
-- ?????? ?????????? ??? ?????? ?? ?????? ???????
-- ?? ??????? ??????????? ????? ?? 0 ??? ??? ????? ????
--===========================================================================
function Trig_Spell_Dvij_Conditions()
    return udg_Logika
end
function Trig_Spell_Dvij_Func002Func004C()
    return IsUnitDeadBJ(udg_Caster) or (( ( udg_HisloA[0] == 0 ) ))
end
function Trig_Spell_Dvij_Func002C()
    return Trig_Spell_Dvij_Func002Func004C()
end
function Trig_Spell_Dvij_Func004Func004Func002C()
    return (( ( udg_HisloA[0] == 2 ) )) or (( ( udg_HisloA[0] == 3 ) )) or (( ( udg_HisloA[0] == 4 ) ))
end
function Trig_Spell_Dvij_Func004Func004C()
    return IsUnitAliveBJ(udg_Dummy[0]) and (Trig_Spell_Dvij_Func004Func004Func002C())
end
function Trig_Spell_Dvij_Func004Func005Func003C()
    return (( ( udg_HisloA[0] == 3 ) )) or (( ( udg_HisloA[0] == 4 ) ))
end
function Trig_Spell_Dvij_Func004Func005C()
    return IsUnitAliveBJ(udg_Dummy[1]) and (Trig_Spell_Dvij_Func004Func005Func003C())
end
function Trig_Spell_Dvij_Func004Func006C()
    return IsUnitAliveBJ(udg_Dummy[2]) and (( udg_HisloA[0] == 4 ))
end
function Trig_Spell_Dvij_Func004Func007Func002Func005Func002Func001C()
    return IsUnitEnemy(GetEnumUnit(), GetOwningPlayer(udg_Caster)) and not (IsUnitAlly(GetEnumUnit(), GetOwningPlayer(udg_Caster))) and not (IsUnitDeadBJ(GetEnumUnit())) and not (IsUnitType(GetEnumUnit(), UNIT_TYPE_STRUCTURE))
end
function Trig_Spell_Dvij_Func004Func007Func002Func005Func002A()
    if Trig_Spell_Dvij_Func004Func007Func002Func005Func002Func001C() then
        GroupAddUnitSimple(GetEnumUnit(), udg_Group)
        UnitDamageTargetBJ(udg_Caster, GetEnumUnit(), ( 100.00 * I2R(GetUnitAbilityLevelSwapped(FourCC('A1BN'), udg_Caster)) ), ATTACK_TYPE_NORMAL, DAMAGE_TYPE_NORMAL)
        udg_To4kaAOE=GetUnitLoc(GetEnumUnit())
        CreateNUnitsAtLoc(1, FourCC('h0MK'), GetOwningPlayer(udg_Caster), udg_To4kaAOE, bj_UNIT_FACING)
        udg_Dummy[4]=GetLastCreatedUnit()
        IssueTargetOrderBJ(udg_Dummy[4], "slow", GetEnumUnit())
        UnitApplyTimedLifeBJ(1.50, FourCC('BTLF'), udg_Dummy[4])
        udg_Dummy[4]=nil
        RemoveLocation(udg_To4kaAOE)
    end
end
function Trig_Spell_Dvij_Func004Func007Func002Func005C()
    return DistanceBetweenPoints(udg_To4kaDummy, udg_To4kaTarget) <= 75.00
end
function Trig_Spell_Dvij_Func004Func007Func002C()
    return udg_HisloA[0] >= 3
end
function Trig_Spell_Dvij_Func004Func007Func004Func006Func002Func001C()
    return IsUnitEnemy(GetEnumUnit(), GetOwningPlayer(udg_Caster)) and not (IsUnitAlly(GetEnumUnit(), GetOwningPlayer(udg_Caster))) and not (IsUnitDeadBJ(GetEnumUnit())) and not (IsUnitType(GetEnumUnit(), UNIT_TYPE_STRUCTURE))
end
function Trig_Spell_Dvij_Func004Func007Func004Func006Func002A()
    if Trig_Spell_Dvij_Func004Func007Func004Func006Func002Func001C() then
        GroupAddUnitSimple(GetEnumUnit(), udg_Group)
        UnitDamageTargetBJ(udg_Caster, GetEnumUnit(), ( 50.00 * I2R(GetUnitAbilityLevelSwapped(FourCC('A1BN'), udg_Caster)) ), ATTACK_TYPE_NORMAL, DAMAGE_TYPE_NORMAL)
        udg_To4kaAOE=GetUnitLoc(GetEnumUnit())
        CreateNUnitsAtLoc(1, FourCC('h0MK'), GetOwningPlayer(udg_Caster), udg_To4kaAOE, bj_UNIT_FACING)
        udg_Dummy[4]=GetLastCreatedUnit()
        IssueTargetOrderBJ(udg_Dummy[4], "polymorph", GetEnumUnit())
        UnitApplyTimedLifeBJ(1.50, FourCC('BTLF'), udg_Dummy[4])
        udg_Dummy[4]=nil
        RemoveLocation(udg_To4kaAOE)
    end
end
function Trig_Spell_Dvij_Func004Func007Func004Func006C()
    return DistanceBetweenPoints(udg_To4kaDummy, udg_To4kaTarget) <= 75.00
end
function Trig_Spell_Dvij_Func004Func007Func004C()
    return udg_HisloA[0] == 2
end
function Trig_Spell_Dvij_Func004Func007Func006Func005Func002Func001C()
    return IsUnitEnemy(GetEnumUnit(), GetOwningPlayer(udg_Caster)) and not (IsUnitAlly(GetEnumUnit(), GetOwningPlayer(udg_Caster))) and not (IsUnitDeadBJ(GetEnumUnit())) and not (IsUnitType(GetEnumUnit(), UNIT_TYPE_STRUCTURE))
end
function Trig_Spell_Dvij_Func004Func007Func006Func005Func002A()
    if Trig_Spell_Dvij_Func004Func007Func006Func005Func002Func001C() then
        GroupAddUnitSimple(GetEnumUnit(), udg_Group)
        UnitDamageTargetBJ(udg_Caster, GetEnumUnit(), ( 50.00 * I2R(GetUnitAbilityLevelSwapped(FourCC('A1BN'), udg_Caster)) ), ATTACK_TYPE_NORMAL, DAMAGE_TYPE_NORMAL)
        udg_To4kaAOE=GetUnitLoc(GetEnumUnit())
        CreateNUnitsAtLoc(1, FourCC('h0MK'), GetOwningPlayer(udg_Caster), udg_To4kaAOE, bj_UNIT_FACING)
        udg_Dummy[4]=GetLastCreatedUnit()
        IssueTargetOrderBJ(udg_Dummy[4], "curse", GetEnumUnit())
        UnitApplyTimedLifeBJ(1.50, FourCC('BTLF'), udg_Dummy[4])
        udg_Dummy[4]=nil
        RemoveLocation(udg_To4kaAOE)
    end
end
function Trig_Spell_Dvij_Func004Func007Func006Func005C()
    return DistanceBetweenPoints(udg_To4kaDummy, udg_To4kaTarget) <= 75.00
end
function Trig_Spell_Dvij_Func004Func007Func006C()
    return udg_HisloA[0] == 1
end
function Trig_Spell_Dvij_Func004Func007C()
    return udg_LogikaCast
end
function Trig_Spell_Dvij_Func004C()
    return true
end
function Trig_Spell_Dvij_Actions()
    -- ?????????
    if Trig_Spell_Dvij_Func002C() then
        RemoveUnit(udg_Dummy[0])
        RemoveUnit(udg_Dummy[1])
        RemoveUnit(udg_Dummy[2])
        GroupClear(udg_Group)
        SetPlayerAbilityAvailableBJ(false, FourCC('A1BM'), GetOwningPlayer(udg_Caster))
        SetPlayerAbilityAvailableBJ(true, FourCC('A1BN'), GetOwningPlayer(udg_Caster))
        RemoveLocation(udg_To4kaCaster)
        udg_Dummy[0]=nil
        udg_Dummy[1]=nil
        udg_Dummy[2]=nil
        udg_Caster=nil
        udg_Logika=false
        udg_LogikaCast=false
        PauseTimerBJ(true, udg_Timer)
    end
    if true then -- INLINED!!
        udg_To4kaCaster=GetUnitLoc(udg_Caster)
        -- ???????? ???????? ???? ???????? + ?? -  ???? ????? ???????? ? ?????? ???????
        udg_Ygol[1]=( udg_Ygol[1] + 5 )
        if Trig_Spell_Dvij_Func004Func004C() then
            SetUnitPositionLoc(udg_Dummy[0], PolarProjectionBJ(udg_To4kaCaster, 100.00, ( 0.00 + I2R(udg_Ygol[1]) )))
        end
        if Trig_Spell_Dvij_Func004Func005C() then
            SetUnitPositionLoc(udg_Dummy[1], PolarProjectionBJ(udg_To4kaCaster, 100.00, ( 120.00 + I2R(udg_Ygol[1]) )))
        end
        if Trig_Spell_Dvij_Func004Func006C() then
            SetUnitPositionLoc(udg_Dummy[2], PolarProjectionBJ(udg_To4kaCaster, 100.00, ( 240.00 + I2R(udg_Ygol[1]) )))
        end
        if Trig_Spell_Dvij_Func004Func007C() then
            -- ?????? ??????? ???
            if Trig_Spell_Dvij_Func004Func007Func002C() then
                udg_To4kaTarget=GetUnitLoc(udg_Target)
                udg_To4kaDummy=GetUnitLoc(udg_Dummy[2])
                -- ???????? ?????? ???? ?? ?????
                SetUnitPositionLoc(udg_Dummy[2], PolarProjectionBJ(udg_To4kaDummy, 50.00, AngleBetweenPoints(udg_To4kaDummy, udg_To4kaTarget)))
                if Trig_Spell_Dvij_Func004Func007Func002Func005C() then
                    -- ??? ????? ? ?????
                    ForGroupBJ(GetUnitsInRangeOfLocAll(200.00, udg_To4kaTarget), Trig_Spell_Dvij_Func004Func007Func002Func005Func002A)
                    AddSpecialEffectLocBJ(udg_To4kaTarget, "AbilitiesSpellsDemonDarkPortalDarkPortalTarget.mdl")
                    DestroyEffectBJ(GetLastCreatedEffectBJ())
                    RemoveUnit(udg_Dummy[2])
                    udg_Target=nil
                    udg_LogikaCast=false
                end
                RemoveLocation(udg_To4kaDummy)
                RemoveLocation(udg_To4kaTarget)
            end
            -- ?????? ??????? ???
            if Trig_Spell_Dvij_Func004Func007Func004C() then
                udg_To4kaTarget=GetUnitLoc(udg_Target)
                udg_To4kaDummy=GetUnitLoc(udg_Dummy[1])
                -- ???????? ?????? ???? ?? ?????
                SetUnitPositionLoc(udg_Dummy[1], PolarProjectionBJ(udg_To4kaDummy, 50.00, AngleBetweenPoints(udg_To4kaDummy, udg_To4kaTarget)))
                if Trig_Spell_Dvij_Func004Func007Func004Func006C() then
                    -- ??? ????? ? ?????
                    ForGroupBJ(GetUnitsInRangeOfLocAll(200.00, udg_To4kaTarget), Trig_Spell_Dvij_Func004Func007Func004Func006Func002A)
                    AddSpecialEffectLocBJ(udg_To4kaTarget, "AbilitiesSpellsUndeadDarkRitualDarkRitualTarget.mdl")
                    DestroyEffectBJ(GetLastCreatedEffectBJ())
                    RemoveUnit(udg_Dummy[1])
                    udg_Target=nil
                    udg_LogikaCast=false
                end
                RemoveLocation(udg_To4kaDummy)
                RemoveLocation(udg_To4kaTarget)
            end
            -- ?????? ??????? ???
            if Trig_Spell_Dvij_Func004Func007Func006C() then
                udg_To4kaTarget=GetUnitLoc(udg_Target)
                udg_To4kaDummy=GetUnitLoc(udg_Dummy[0])
                -- ???????? ?????? ???? ?? ?????
                SetUnitPositionLoc(udg_Dummy[0], PolarProjectionBJ(udg_To4kaDummy, 50.00, AngleBetweenPoints(udg_To4kaDummy, udg_To4kaTarget)))
                if Trig_Spell_Dvij_Func004Func007Func006Func005C() then
                    -- ??? ????? ? ?????
                    ForGroupBJ(GetUnitsInRangeOfLocAll(200.00, udg_To4kaTarget), Trig_Spell_Dvij_Func004Func007Func006Func005Func002A)
                    AddSpecialEffectLocBJ(udg_To4kaTarget, "AbilitiesSpellsUndeadDeathPactDeathPactTarget.mdl")
                    DestroyEffectBJ(GetLastCreatedEffectBJ())
                    RemoveUnit(udg_Dummy[0])
                    udg_Target=nil
                    udg_LogikaCast=false
                    udg_HisloA[0]=0
                end
                RemoveLocation(udg_To4kaDummy)
                RemoveLocation(udg_To4kaTarget)
            end
        end
    end
end
--===========================================================================
function InitTrig_Spell_Dvij()
    gg_trg_Spell_Dvij=CreateTrigger()
    TriggerRegisterTimerExpireEventBJ(gg_trg_Spell_Dvij, udg_Timer)
    TriggerAddCondition(gg_trg_Spell_Dvij, Condition(Trig_Spell_Dvij_Conditions))
    TriggerAddAction(gg_trg_Spell_Dvij, Trig_Spell_Dvij_Actions)
end
--===========================================================================
-- Trigger: DieDummy
--
-- ??????? 3 ???? ??????? ?????? ?????? ????? ?????????? ???? ?? ?? ?? ???????? ??? ?????
-- ???????? ?? ?? ?????? ????? ??????? ?? ???? ? 200 ??? ? ?????? ????????? ????
-- ?????? ?????????? ??? ?????? ?? ?????? ??????????
-- ?????? ?????????? ??? ?????? ?? ?????? ????
-- ?????? ?????????? ??? ?????? ?? ?????? ???????
-- ?? ??????? ??????????? ????? ?? 0 ??? ??? ????? ????
--===========================================================================
function Trig_DieDummy_Func001Func002A()
    RemoveUnit(GetEnumUnit())
end
function Trig_DieDummy_Func001C()
    return GetUnitTypeId(GetDyingUnit()) == FourCC('h0MK')
end
function Trig_DieDummy_Func002Func002A()
    RemoveUnit(GetEnumUnit())
end
function Trig_DieDummy_Func002C()
    return GetUnitTypeId(GetDyingUnit()) == FourCC('h0MJ')
end
function Trig_DieDummy_Actions()
    if Trig_DieDummy_Func001C() then
        ForGroupBJ(GetUnitsOfTypeIdAll(FourCC('h0MK')), Trig_DieDummy_Func001Func002A)
    end
    if Trig_DieDummy_Func002C() then
        ForGroupBJ(GetUnitsOfTypeIdAll(FourCC('h0MJ')), Trig_DieDummy_Func002Func002A)
    end
end
--===========================================================================
function InitTrig_DieDummy()
    gg_trg_DieDummy=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_DieDummy, EVENT_PLAYER_UNIT_DEATH)
    TriggerAddAction(gg_trg_DieDummy, Trig_DieDummy_Actions)
end
--===========================================================================
-- Trigger: Dammi Dead
--===========================================================================
function Trig_Dammi_Dead_Conditions()
    return GetUnitTypeId(GetTriggerUnit()) == FourCC('H0BN')
end
function Trig_Dammi_Dead_Actions()
    RemoveUnit(GetTriggerUnit())
end
--===========================================================================
function InitTrig_Dammi_Dead()
    gg_trg_Dammi_Dead=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_Dammi_Dead, EVENT_PLAYER_UNIT_DEATH)
    TriggerAddCondition(gg_trg_Dammi_Dead, Condition(Trig_Dammi_Dead_Conditions))
    TriggerAddAction(gg_trg_Dammi_Dead, Trig_Dammi_Dead_Actions)
end
--===========================================================================
-- Trigger: Bolvanka
--===========================================================================
function Trig_Bolvanka_Actions()
    UnitDamageTargetBJ(GetTriggerUnit(), GetTriggerUnit(), ( 1 * I2R(GetHeroStatBJ(bj_HEROSTAT_STR, GetTriggerUnit(), false)) ), ATTACK_TYPE_NORMAL, DAMAGE_TYPE_NORMAL)
end
--===========================================================================
function InitTrig_Bolvanka()
    gg_trg_Bolvanka=CreateTrigger()
    TriggerAddAction(gg_trg_Bolvanka, Trig_Bolvanka_Actions)
end
--===========================================================================
-- Trigger: SpellSleepAOE
--===========================================================================
--===========================================================================
-- Trigger: Fireball
--===========================================================================
function Trig_Fireball_Actions()
    local fireballtarget
    fireballtarget=GetSpellTargetUnit()
    PolledWait(( DistanceBetweenPoints(GetUnitLoc(GetSpellAbilityUnit()), GetUnitLoc(GetSpellTargetUnit())) / 1000.00 ))
    udg_unit=fireballtarget
    UnitDamageTargetBJ(GetSpellAbilityUnit(), udg_unit, I2R(GetHeroStatBJ(bj_HEROSTAT_INT, GetSpellAbilityUnit(), false)), ATTACK_TYPE_NORMAL, DAMAGE_TYPE_COLD)
    fireballtarget=nil
end
--===========================================================================
function InitTrig_Fireball()
    gg_trg_Fireball=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_Fireball, EVENT_PLAYER_UNIT_SPELL_EFFECT)
    TriggerAddAction(gg_trg_Fireball, function()
        if GetSpellAbilityId() ~= FourCC('A043') then return end
        Trig_Fireball_Actions()
    end)
end
--===========================================================================
-- Trigger: Fire Arrow
--===========================================================================
function Trig_Fire_Arrow_Actions()
    local firearrowtarget
    firearrowtarget=GetSpellTargetUnit()
    PolledWait(( DistanceBetweenPoints(GetUnitLoc(GetSpellAbilityUnit()), GetUnitLoc(GetSpellTargetUnit())) / 1500.00 ))
    udg_unit=firearrowtarget
    UnitDamageTargetBJ(GetSpellAbilityUnit(), udg_unit, I2R(GetHeroStatBJ(bj_HEROSTAT_INT, GetSpellAbilityUnit(), false)), ATTACK_TYPE_NORMAL, DAMAGE_TYPE_COLD)
    firearrowtarget=nil
end
--===========================================================================
function InitTrig_Fire_Arrow()
    gg_trg_Fire_Arrow=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_Fire_Arrow, EVENT_PLAYER_UNIT_SPELL_CAST)
    TriggerAddAction(gg_trg_Fire_Arrow, function()
        if GetSpellAbilityId() ~= FourCC('A044') then return end
        Trig_Fire_Arrow_Actions()
    end)
end
--===========================================================================
-- Trigger: Research Ot
--===========================================================================
function Trig_Research_Ot_Conditions()
    return GetResearched() == FourCC('R00P')
end
function Trig_Research_Ot_Actions()
    udg_LocalPosition2=GetRandomLocInRect(RectFromCenterSizeBJ(GetUnitLoc(GetTriggerUnit()), 15.00, 15.00))
    CreateNUnitsAtLoc(1, FourCC('o00F'), GetOwningPlayer(GetTriggerUnit()), udg_LocalPosition2, bj_UNIT_FACING)
    RemoveLocation(udg_LocalPosition2)
end
--===========================================================================
function InitTrig_Research_Ot()
    gg_trg_Research_Ot=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_Research_Ot, EVENT_PLAYER_UNIT_RESEARCH_FINISH)
    TriggerAddCondition(gg_trg_Research_Ot, Condition(Trig_Research_Ot_Conditions))
    TriggerAddAction(gg_trg_Research_Ot, Trig_Research_Ot_Actions)
end
--===========================================================================
-- Trigger: NO ENOTS
--===========================================================================
function Trig_NO_ENOTS_Func001A()
    RemoveUnit(GetEnumUnit())
end
function Trig_NO_ENOTS_Actions()
    ForGroupBJ(GetUnitsOfTypeIdAll(FourCC('ft02')), Trig_NO_ENOTS_Func001A)
end
--===========================================================================
function InitTrig_NO_ENOTS()
    gg_trg_NO_ENOTS=CreateTrigger()
    TriggerRegisterTimerEventSingle(gg_trg_NO_ENOTS, 30.00)
    TriggerAddAction(gg_trg_NO_ENOTS, Trig_NO_ENOTS_Actions)
end
--===========================================================================
-- Trigger: Sdelat Flagman Ot Copy
--===========================================================================
function Trig_Sdelat_Flagman_Ot_Copy_Func002002()
    return GetUnitAbilityLevelSwapped(FourCC('A009'), GetFilterUnit()) >= 1
end
function Trig_Sdelat_Flagman_Ot_Copy_Func005A()
    UnitRemoveAbilityBJ(FourCC('A009'), GetEnumUnit())
end
function Trig_Sdelat_Flagman_Ot_Copy_Func019C()
    return GetUnitTypeId(GetTriggerUnit()) == FourCC('h06W')
end
function Trig_Sdelat_Flagman_Ot_Copy_Actions()
    udg_FlagmanEst[GetConvertedPlayerId(GetOwningPlayer(GetTriggerUnit()))]=true
    udg_Boolexpr = Trig_Sdelat_Flagman_Ot_Copy_Func002002
    GroupEnumUnitsOfPlayer(udg_LocalOtrad2, udg_LocalPlayer, udg_Boolexpr)
    ForGroupBJ(udg_LocalOtrad2, Trig_Sdelat_Flagman_Ot_Copy_Func005A)
    GroupClear(udg_LocalOtrad2)
    BlzSetUnitWeaponIntegerFieldBJ(GetTriggerUnit(), UNIT_WEAPON_IF_ATTACK_DAMAGE_BASE, 0, ( BlzGetUnitWeaponIntegerField(GetTriggerUnit(), UNIT_WEAPON_IF_ATTACK_DAMAGE_BASE, 0) * 3 ))
    BlzSetUnitStringFieldBJ(GetTriggerUnit(), UNIT_SF_NAME, ( "cffff0000r - " .. GetUnitName(GetTriggerUnit()) ))
    BlzSetUnitIntegerFieldBJ(GetTriggerUnit(), UNIT_IF_TINTING_COLOR_GREEN, 175)
    BlzSetUnitIntegerFieldBJ(GetTriggerUnit(), UNIT_IF_TINTING_COLOR_BLUE, 175)
    UnitAddTypeBJ(UNIT_TYPE_HERO, GetTriggerUnit())
    BlzSetUnitRealFieldBJ(GetTriggerUnit(), UNIT_RF_SCALING_VALUE, ( BlzGetUnitRealField(GetTriggerUnit(), UNIT_RF_SCALING_VALUE) * 1.25 ))
    BlzSetUnitArmor(GetTriggerUnit(), ( BlzGetUnitArmor(GetTriggerUnit()) + 5.00 ))
    BlzSetUnitMaxHP(GetTriggerUnit(), ( BlzGetUnitMaxHP(GetTriggerUnit()) * 3 ))
    BlzSetUnitRealFieldBJ(GetTriggerUnit(), UNIT_RF_HP, I2R(BlzGetUnitMaxHP(GetTriggerUnit())))
    UnitAddAbilityBJ(FourCC('A008'), GetTriggerUnit())
    GroupAddUnitSimple(GetTriggerUnit(), udg_Flagmans)
    if Trig_Sdelat_Flagman_Ot_Copy_Func019C() then
        UnitRemoveAbilityBJ(FourCC('A0LG'), GetTriggerUnit())
    end
end
--===========================================================================
function InitTrig_Sdelat_Flagman_Ot_Copy()
    gg_trg_Sdelat_Flagman_Ot_Copy=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_Sdelat_Flagman_Ot_Copy, EVENT_PLAYER_UNIT_SPELL_CAST)
    TriggerRegisterAnyUnitEventBJ(gg_trg_Sdelat_Flagman_Ot_Copy, EVENT_PLAYER_UNIT_SPELL_ENDCAST)
    TriggerRegisterAnyUnitEventBJ(gg_trg_Sdelat_Flagman_Ot_Copy, EVENT_PLAYER_UNIT_SPELL_EFFECT)
    TriggerAddAction(gg_trg_Sdelat_Flagman_Ot_Copy, function()
        if GetSpellAbilityId() ~= FourCC('A009') then return end
        Trig_Sdelat_Flagman_Ot_Copy_Actions()
    end)
end
--===========================================================================
-- Trigger: Flagman die Ot
--===========================================================================
function Trig_Flagman_die_Ot_Conditions()
    return IsUnitInGroup(GetTriggerUnit(), udg_Flagmans)
end
function Trig_Flagman_die_Ot_Func003002()
    return GetUnitAbilityLevelSwapped(FourCC('A001'), GetFilterUnit()) >= 1
end
function Trig_Flagman_die_Ot_Func006A()
    UnitAddAbilityBJ(FourCC('A009'), GetEnumUnit())
end
function Trig_Flagman_die_Ot_Actions()
    local u= GetTriggerUnit()
    local p= GetOwningPlayer(u)
    udg_FlagmanEst[GetConvertedPlayerId(p)]=false
    udg_LocalOtrad=GetUnitsOfPlayerAll(p)
    udg_Boolexpr = Trig_Flagman_die_Ot_Func003002
    udg_LocalPlayer=GetOwningPlayer(u)
    GroupEnumUnitsOfPlayer(udg_LocalOtrad2, udg_LocalPlayer, udg_Boolexpr)
    ForGroupBJ(udg_LocalOtrad2, Trig_Flagman_die_Ot_Func006A)
    
    GroupClear(udg_LocalOtrad2)
    DisplayTextToPlayer(( GetOwningPlayer(u) ), 0, 0, ( "cffff0000.r" ))
    SetPlayerAbilityAvailableBJ(true, FourCC('A009'), GetOwningPlayer(u))
    u=nil
end
--===========================================================================
function InitTrig_Flagman_die_Ot()
    gg_trg_Flagman_die_Ot=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_Flagman_die_Ot, EVENT_PLAYER_UNIT_DEATH)
    TriggerAddCondition(gg_trg_Flagman_die_Ot, Condition(Trig_Flagman_die_Ot_Conditions))
    TriggerAddAction(gg_trg_Flagman_die_Ot, Trig_Flagman_die_Ot_Actions)
end
--===========================================================================
-- Trigger: Ne dam flagman Ot
--===========================================================================
function Trig_Ne_dam_flagman_Ot_Func002C()
    return udg_FlagmanEst[GetConvertedPlayerId(GetOwningPlayer(GetTrainedUnit()))] and (( GetUnitAbilityLevelSwapped(FourCC('A009'), GetTrainedUnit()) == 1 ))
end
function Trig_Ne_dam_flagman_Ot_Conditions()
    return Trig_Ne_dam_flagman_Ot_Func002C()
end
function Trig_Ne_dam_flagman_Ot_Actions()
    UnitRemoveAbilityBJ(FourCC('A009'), GetTrainedUnit())
end
--===========================================================================
function InitTrig_Ne_dam_flagman_Ot()
    gg_trg_Ne_dam_flagman_Ot=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_Ne_dam_flagman_Ot, EVENT_PLAYER_UNIT_TRAIN_FINISH)
    TriggerAddCondition(gg_trg_Ne_dam_flagman_Ot, Condition(Trig_Ne_dam_flagman_Ot_Conditions))
    TriggerAddAction(gg_trg_Ne_dam_flagman_Ot, Trig_Ne_dam_flagman_Ot_Actions)
end
--===========================================================================
-- Trigger: Aura Flagmana Vinoslivost O
--===========================================================================
function Trig_Aura_Flagmana_Vinoslivost_O_Conditions()
    return IsUnitSelected(GetTriggerUnit(), GetOwningPlayer(GetTriggerUnit()))
end
function Trig_Aura_Flagmana_Vinoslivost_O_Actions()
    UnitAddAbilityBJ(FourCC('A007'), GetTriggerUnit())
    UnitRemoveAbilityBJ(FourCC('A008'), GetTriggerUnit())
end
--===========================================================================
function InitTrig_Aura_Flagmana_Vinoslivost_O()
    gg_trg_Aura_Flagmana_Vinoslivost_O=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_Aura_Flagmana_Vinoslivost_O, EVENT_PLAYER_UNIT_SPELL_EFFECT)
    TriggerAddAction(gg_trg_Aura_Flagmana_Vinoslivost_O, function()
        if GetSpellAbilityId() ~= FourCC('A00F') then return end
        if not Trig_Aura_Flagmana_Vinoslivost_O_Conditions() then return end
        Trig_Aura_Flagmana_Vinoslivost_O_Actions()
    end)
end
--===========================================================================
-- Trigger: Aura Flagmana Metkost O
--===========================================================================
function Trig_Aura_Flagmana_Metkost_O_Conditions()
    return IsUnitSelected(GetTriggerUnit(), GetOwningPlayer(GetTriggerUnit()))
end
function Trig_Aura_Flagmana_Metkost_O_Actions()
    UnitAddAbilityBJ(FourCC('A006'), GetTriggerUnit())
    UnitRemoveAbilityBJ(FourCC('A008'), GetTriggerUnit())
end
--===========================================================================
function InitTrig_Aura_Flagmana_Metkost_O()
    gg_trg_Aura_Flagmana_Metkost_O=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_Aura_Flagmana_Metkost_O, EVENT_PLAYER_UNIT_SPELL_EFFECT)
    TriggerAddAction(gg_trg_Aura_Flagmana_Metkost_O, function()
        if GetSpellAbilityId() ~= FourCC('A00E') then return end
        if not Trig_Aura_Flagmana_Metkost_O_Conditions() then return end
        Trig_Aura_Flagmana_Metkost_O_Actions()
    end)
end
--===========================================================================
-- Trigger: Aura Flagmana Stoikost O
--===========================================================================
function Trig_Aura_Flagmana_Stoikost_O_Conditions()
    return IsUnitSelected(GetTriggerUnit(), GetOwningPlayer(GetTriggerUnit()))
end
function Trig_Aura_Flagmana_Stoikost_O_Actions()
    UnitAddAbilityBJ(FourCC('A005'), GetTriggerUnit())
    UnitRemoveAbilityBJ(FourCC('A008'), GetTriggerUnit())
end
--===========================================================================
function InitTrig_Aura_Flagmana_Stoikost_O()
    gg_trg_Aura_Flagmana_Stoikost_O=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_Aura_Flagmana_Stoikost_O, EVENT_PLAYER_UNIT_SPELL_EFFECT)
    TriggerAddAction(gg_trg_Aura_Flagmana_Stoikost_O, function()
        if GetSpellAbilityId() ~= FourCC('A00C') then return end
        if not Trig_Aura_Flagmana_Stoikost_O_Conditions() then return end
        Trig_Aura_Flagmana_Stoikost_O_Actions()
    end)
end