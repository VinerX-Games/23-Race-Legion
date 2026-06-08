    gg_trg_Aura_Flagmana_Stoikost_O=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_Aura_Flagmana_Stoikost_O, EVENT_PLAYER_UNIT_SPELL_EFFECT)
    TriggerAddAction(gg_trg_Aura_Flagmana_Stoikost_O, function()
        if GetSpellAbilityId() ~= FourCC('A00C') then return end
        if not Trig_Aura_Flagmana_Stoikost_O_Conditions() then return end
        Trig_Aura_Flagmana_Stoikost_O_Actions()
    end)
end
--===========================================================================
-- Trigger: Init
--===========================================================================
function Trig_Init_Actions()
    GroupClear(udg_LoadedGroup)
    GroupClear(udg_TransportingGroup)
    udg_StopOrder=String2OrderIdBJ("stop")
    udg_TransportingIncrement=1
    udg_TransportingMin=udg_TransportingIncrement
end
--===========================================================================
function InitTrig_Init()
    gg_trg_Init=CreateTrigger()
    TriggerAddAction(gg_trg_Init, Trig_Init_Actions)
end
--===========================================================================
-- Trigger: Unit Loaded
--===========================================================================
function Trig_Unit_Loaded_Func001C()
    return IsUnitInGroup(GetTransportUnitBJ(), udg_TransportingGroup)
end
function Trig_Unit_Loaded_Actions()
    if ( Trig_Unit_Loaded_Func001C() ) then
    else
        SetUnitUserData(GetTransportUnitBJ(), udg_TransportingIncrement)
        udg_TransportingUnitArray[udg_TransportingIncrement]=GetTransportUnitBJ()
        GroupAddUnitSimple(GetTransportUnitBJ(), udg_TransportingGroup)
        udg_LoadedGroupArray[udg_TransportingIncrement]=CreateGroup()
        udg_TransportingIncrement=( udg_TransportingIncrement + 1 )
    end
    GroupAddUnitSimple(GetLoadedUnitBJ(), udg_LoadedGroupArray[GetUnitUserData(GetTransportUnitBJ())])
    GroupAddUnitSimple(GetLoadedUnitBJ(), udg_LoadedGroup)
    udg_TempUnit02=GetTransportUnitBJ()
end
--===========================================================================
function InitTrig_Unit_Loaded()
    gg_trg_Unit_Loaded=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_Unit_Loaded, EVENT_PLAYER_UNIT_LOADED)
    TriggerAddAction(gg_trg_Unit_Loaded, Trig_Unit_Loaded_Actions)
end
--===========================================================================
-- Trigger: Unit Death
--===========================================================================
function Trig_Unit_Death_Conditions()
    return IsUnitInGroup(GetDyingUnit(), udg_LoadedGroup)
end
function Trig_Unit_Death_Actions()
    udg_TempUnit01=GetDyingUnit()
    ConditionalTriggerExecute(gg_trg_Remove_Unit_From_LoadedGroup)
end
--===========================================================================
function InitTrig_Unit_Death()
    gg_trg_Unit_Death=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_Unit_Death, EVENT_PLAYER_UNIT_DEATH)
    TriggerAddCondition(gg_trg_Unit_Death, Condition(Trig_Unit_Death_Conditions))
    TriggerAddAction(gg_trg_Unit_Death, Trig_Unit_Death_Actions)
end
--===========================================================================
-- Trigger: Unit Issued Order
--===========================================================================
function Trig_Unit_Issued_Order_Conditions()
    return IsUnitInGroup(GetOrderedUnit(), udg_LoadedGroup) and (( GetIssuedOrderIdBJ() == udg_StopOrder ))
end
function Trig_Unit_Issued_Order_Actions()
    udg_TempUnit01=GetOrderedUnit()
    ConditionalTriggerExecute(gg_trg_Remove_Unit_From_LoadedGroup)
end
--===========================================================================
function InitTrig_Unit_Issued_Order()
    gg_trg_Unit_Issued_Order=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_Unit_Issued_Order, EVENT_PLAYER_UNIT_ISSUED_ORDER)
    TriggerAddCondition(gg_trg_Unit_Issued_Order, Condition(Trig_Unit_Issued_Order_Conditions))
    TriggerAddAction(gg_trg_Unit_Issued_Order, Trig_Unit_Issued_Order_Actions)
end
--===========================================================================
-- Trigger: Remove Unit From LoadedGroup
--===========================================================================
function Trig_Remove_Unit_From_LoadedGroup_Func002Func001C()
    return IsUnitInGroup(udg_TempUnit01, udg_LoadedGroupArray[GetForLoopIndexA()])
end
function Trig_Remove_Unit_From_LoadedGroup_Actions()
    GroupRemoveUnitSimple(udg_TempUnit01, udg_LoadedGroup)
    bj_forLoopAIndex=udg_TransportingMin
    bj_forLoopAIndexEnd=( udg_TransportingIncrement - 1 )
    while true do
        if bj_forLoopAIndex > bj_forLoopAIndexEnd then break end
        if ( Trig_Remove_Unit_From_LoadedGroup_Func002Func001C() ) then
            GroupRemoveUnitSimple(udg_TempUnit01, udg_LoadedGroupArray[GetForLoopIndexA()])
            udg_TempUnit02=udg_TransportingUnitArray[GetForLoopIndexA()]
        end
        bj_forLoopAIndex=bj_forLoopAIndex + 1
    end
end
--===========================================================================
function InitTrig_Remove_Unit_From_LoadedGroup()
    gg_trg_Remove_Unit_From_LoadedGroup=CreateTrigger()
    TriggerAddAction(gg_trg_Remove_Unit_From_LoadedGroup, Trig_Remove_Unit_From_LoadedGroup_Actions)
end
--===========================================================================
-- Trigger: TransportingUnitArray Message
--===========================================================================
function Trig_TransportingUnitArray_Message_Func001C()
    return IsUnitInGroup(udg_TempUnit02, udg_TransportingGroup)
end
function Trig_TransportingUnitArray_Message_Actions()
    if ( Trig_TransportingUnitArray_Message_Func001C() ) then
        DisplayTimedTextToForce(GetPlayersAll(), 8.00, ( ( "" .. GetUnitName(udg_TempUnit02) ) .. ( "" .. I2S(CountUnitsInGroup(udg_LoadedGroupArray[GetUnitUserData(udg_TempUnit02)])) ) ))
    else
        DisplayTimedTextToForce(GetPlayersAll(), 8.00, ( ( "" .. GetUnitName(udg_TempUnit02) ) .. "." ))
    end
    UnitAddIndicatorBJ(udg_TempUnit02, 100, 100, 100, 0)
end
--===========================================================================
function InitTrig_TransportingUnitArray_Message()
    gg_trg_TransportingUnitArray_Message=CreateTrigger()
    TriggerAddAction(gg_trg_TransportingUnitArray_Message, Trig_TransportingUnitArray_Message_Actions)
end
--===========================================================================
-- Trigger: Select Unit
--===========================================================================
function Trig_Select_Unit_Actions()
    udg_TempUnit02=GetTriggerUnit()
    ConditionalTriggerExecute(gg_trg_TransportingUnitArray_Message)
end
--===========================================================================
function InitTrig_Select_Unit()
    gg_trg_Select_Unit=CreateTrigger()
    DisableTrigger(gg_trg_Select_Unit)
    TriggerRegisterPlayerSelectionEventBJ(gg_trg_Select_Unit, Player(0), true)
    TriggerAddAction(gg_trg_Select_Unit, Trig_Select_Unit_Actions)
end
--===========================================================================
-- Trigger: MassPosadka2
--===========================================================================
function Trig_MassPosadka_Copy_Func006002()
    return IsUnitSelected(GetFilterUnit(), GetOwningPlayer(GetTriggerUnit()))
end
function Trig_MassPosadka_Copy_Func008A()
    if GetUnitTypeId(GetTriggerUnit()) == GetUnitTypeId(GetEnumUnit()) then
        GroupAddUnit(udg_LocalOtrad, GetEnumUnit())
        udg_LocalInteger=( udg_LocalInteger + 10 )
        udg_LocalInteger=( udg_LocalInteger - CountUnitsInGroup(udg_LoadedGroupArray[GetUnitUserData(GetEnumUnit())]) )
    end
end
function Trig_MassPosadka_Copy_Func010002()
    return GetOwningPlayer(GetFilterUnit()) == GetOwningPlayer(GetTriggerUnit()) and GetUnitAbilityLevel(GetFilterUnit(), FourCC('A001')) == 0 and not (IsUnitType(GetFilterUnit(), UNIT_TYPE_STRUCTURE)) and GetUnitAbilityLevel(GetFilterUnit(), FourCC('Slo3')) == 0
end
function Trig_MassPosadka_Copy_Func014Func006A()
    udg_LocalUnit[15]=GetEnumUnit()
    --call TriggerExecute( gg_trg_Colision_1_s )
    SetUnitPathing(GetEnumUnit(), false)
    CollisionTimed(GetEnumUnit() , true , 1.0)
    SetUnitPositionLoc(GetEnumUnit(), udg_LocalPosition2)
    IssueTargetOrder(GetEnumUnit(), "smart", udg_LocalUnit2)
    GroupRemoveUnit(udg_LocalOtrad2, GetEnumUnit())
end
function Trig_MassPosadka_Copy_Func014A()
    udg_LocalPosition2=GetUnitLoc(GetEnumUnit())
    udg_LocalUnit2=GetEnumUnit()
    udg_LocalInteger=( 10 - CountUnitsInGroup(udg_LoadedGroupArray[GetUnitUserData(GetEnumUnit())]) )
    -- ??????? ???????? ??????, ? ????? ??????????? ??? ???????.
    udg_LocalOtrad3=GetRandomSubGroup2(udg_LocalInteger , udg_LocalOtrad2)
    ForGroup(udg_LocalOtrad3, Trig_MassPosadka_Copy_Func014Func006A)
    GroupClear(udg_LocalOtrad3)
    GroupRemoveUnit(udg_LocalOtrad, GetEnumUnit())
    RemoveLocation(udg_LocalPosition2)
end
function Trig_MassPosadka2_Actions()
    udg_LocalPosition2=GetSpellTargetLoc()
    GroupAddUnit(udg_LocalOtrad, GetTriggerUnit())
    
    
    
    -- ???????? ??????? (? ??????? ??????) ? ??????, ?????? ????????? ?????
    udg_LocalInteger=0
    udg_LocalPlayer=GetOwningPlayer(GetTriggerUnit())
    udg_Boolexpr = Trig_MassPosadka_Copy_Func006002
    GroupEnumUnitsOfPlayer(udg_LocalOtrad2, udg_LocalPlayer, udg_Boolexpr)
    ForGroup(udg_LocalOtrad2, Trig_MassPosadka_Copy_Func008A)
    
    
    
    -- ????? ?????? ?? ?????? ?? ???????? ? ?? ??????.
    udg_Boolexpr = Trig_MassPosadka_Copy_Func010002
    GroupEnumUnitsInRangeOfLoc(udg_LocalOtrad2, udg_LocalPosition2, 250, udg_Boolexpr)
    RemoveLocation(udg_LocalPosition2)
    
    -- ????????? ???????
    ForGroup(udg_LocalOtrad, Trig_MassPosadka_Copy_Func014A)
    GroupClear(udg_LocalOtrad)
    GroupClear(udg_LocalOtrad2)
    GroupClear(udg_LocalOtrad3)
end
--===========================================================================
function InitTrig_MassPosadka2()
    gg_trg_MassPosadka2=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_MassPosadka2, EVENT_PLAYER_UNIT_SPELL_EFFECT)
    TriggerAddAction(gg_trg_MassPosadka2, function()
        if GetSpellAbilityId() ~= FourCC('A00I') then return end
        Trig_MassPosadka2_Actions()
    end)
end
--===========================================================================
-- Trigger: Linkor reaserch Obstel O
--===========================================================================
function Trig_Linkor_reaserch_Obstel_O_Conditions()
    return ( GetResearched() == FourCC('R005') )
end
function Trig_Linkor_reaserch_Obstel_O_Func001Func002002()
    return ( 0 == 0 )
end
function Trig_Linkor_reaserch_Obstel_O_Func001Func004A()
    SetUnitAbilityLevelSwapped(FourCC('A00G'), GetEnumUnit(), 2)
end
function Trig_Linkor_reaserch_Obstel_O_Func001C()
    return ( GetPlayerTechCountSimple(FourCC('R005'), GetOwningPlayer(GetTriggerUnit())) == 2 )
end
function Trig_Linkor_reaserch_Obstel_O_Func002Func002002()
    return ( 0 == 0 )
end
function Trig_Linkor_reaserch_Obstel_O_Func002Func004A()
    SetUnitAbilityLevelSwapped(FourCC('A00G'), GetEnumUnit(), 3)
end
function Trig_Linkor_reaserch_Obstel_O_Func002C()
    return ( GetPlayerTechCountSimple(FourCC('R005'), GetOwningPlayer(GetTriggerUnit())) == 3 )
end
function Trig_Linkor_reaserch_Obstel_O_Actions()
    if ( Trig_Linkor_reaserch_Obstel_O_Func001C() ) then
        udg_Boolexpr = Trig_Linkor_reaserch_Obstel_O_Func001Func002002
        GroupEnumUnitsOfPlayer(udg_LocalOtrad2, udg_LocalPlayer, udg_Boolexpr)
        ForGroupBJ(udg_LocalOtrad2, Trig_Linkor_reaserch_Obstel_O_Func001Func004A)
        GroupClear(udg_LocalOtrad2)
    end
    if ( Trig_Linkor_reaserch_Obstel_O_Func002C() ) then
        udg_Boolexpr = Trig_Linkor_reaserch_Obstel_O_Func002Func002002
        GroupEnumUnitsOfPlayer(udg_LocalOtrad2, udg_LocalPlayer, udg_Boolexpr)
        ForGroupBJ(udg_LocalOtrad2, Trig_Linkor_reaserch_Obstel_O_Func002Func004A)
        GroupClear(udg_LocalOtrad2)
    end
end
--===========================================================================
function InitTrig_Linkor_reaserch_Obstel_O()
    gg_trg_Linkor_reaserch_Obstel_O=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_Linkor_reaserch_Obstel_O, EVENT_PLAYER_UNIT_RESEARCH_FINISH)
    TriggerAddCondition(gg_trg_Linkor_reaserch_Obstel_O, Condition(Trig_Linkor_reaserch_Obstel_O_Conditions))
    TriggerAddAction(gg_trg_Linkor_reaserch_Obstel_O, Trig_Linkor_reaserch_Obstel_O_Actions)
end
--===========================================================================
-- Trigger: Naim Obstrel O
--===========================================================================
function Trig_Naim_Obstrel_O_Func001C()
    return ( ( GetUnitAbilityLevelSwapped(FourCC('A00G'), GetTrainedUnit()) == 1 ) )
end
function Trig_Naim_Obstrel_O_Conditions()
    return Trig_Naim_Obstrel_O_Func001C()
end
function Trig_Naim_Obstrel_O_Func002C()
    return ( GetPlayerTechCountSimple(FourCC('R005'), GetOwningPlayer(GetTriggerUnit())) == 2 )
end
function Trig_Naim_Obstrel_O_Func003C()
    return ( GetPlayerTechCountSimple(FourCC('R005'), GetOwningPlayer(GetTriggerUnit())) == 3 )
end
function Trig_Naim_Obstrel_O_Actions()
    if ( Trig_Naim_Obstrel_O_Func002C() ) then
        SetUnitAbilityLevelSwapped(FourCC('A00G'), GetTrainedUnit(), 2)
    end
    if ( Trig_Naim_Obstrel_O_Func003C() ) then
        SetUnitAbilityLevelSwapped(FourCC('A00G'), GetTrainedUnit(), 3)
    end
end
--===========================================================================
function InitTrig_Naim_Obstrel_O()
    gg_trg_Naim_Obstrel_O=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_Naim_Obstrel_O, EVENT_PLAYER_UNIT_TRAIN_FINISH)
    TriggerAddCondition(gg_trg_Naim_Obstrel_O, Condition(Trig_Naim_Obstrel_O_Conditions))
    TriggerAddAction(gg_trg_Naim_Obstrel_O, Trig_Naim_Obstrel_O_Actions)
end
--===========================================================================
-- Trigger: Linkor reaserch Parusa O
--===========================================================================
function Trig_Linkor_reaserch_Parusa_O_Conditions()
    return ( GetResearched() == FourCC('R006') )
end
function Trig_Linkor_reaserch_Parusa_O_Func001Func002002()
    return ( 0 == 0 )
end
function Trig_Linkor_reaserch_Parusa_O_Func001Func004A()
    SetUnitAbilityLevelSwapped(FourCC('A00B'), GetEnumUnit(), 2)
end
function Trig_Linkor_reaserch_Parusa_O_Func001C()
    return ( GetPlayerTechCountSimple(FourCC('R006'), GetOwningPlayer(GetTriggerUnit())) == 2 )
end
function Trig_Linkor_reaserch_Parusa_O_Func002Func002002()
    return ( 0 == 0 )
end
function Trig_Linkor_reaserch_Parusa_O_Func002Func004A()
    SetUnitAbilityLevelSwapped(FourCC('A00B'), GetEnumUnit(), 3)
end
function Trig_Linkor_reaserch_Parusa_O_Func002C()
    return ( GetPlayerTechCountSimple(FourCC('R006'), GetOwningPlayer(GetTriggerUnit())) == 3 )
end
function Trig_Linkor_reaserch_Parusa_O_Actions()
    if ( Trig_Linkor_reaserch_Parusa_O_Func001C() ) then
        udg_Boolexpr = Trig_Linkor_reaserch_Parusa_O_Func001Func002002
        GroupEnumUnitsOfPlayer(udg_LocalOtrad2, udg_LocalPlayer, udg_Boolexpr)
        ForGroupBJ(udg_LocalOtrad2, Trig_Linkor_reaserch_Parusa_O_Func001Func004A)
        GroupClear(udg_LocalOtrad2)
    end
    if ( Trig_Linkor_reaserch_Parusa_O_Func002C() ) then
        udg_Boolexpr = Trig_Linkor_reaserch_Parusa_O_Func002Func002002
        GroupEnumUnitsOfPlayer(udg_LocalOtrad2, udg_LocalPlayer, udg_Boolexpr)
        ForGroupBJ(udg_LocalOtrad2, Trig_Linkor_reaserch_Parusa_O_Func002Func004A)
        GroupClear(udg_LocalOtrad2)
    end
end
--===========================================================================
function InitTrig_Linkor_reaserch_Parusa_O()
    gg_trg_Linkor_reaserch_Parusa_O=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_Linkor_reaserch_Parusa_O, EVENT_PLAYER_UNIT_RESEARCH_FINISH)
    TriggerAddCondition(gg_trg_Linkor_reaserch_Parusa_O, Condition(Trig_Linkor_reaserch_Parusa_O_Conditions))
    TriggerAddAction(gg_trg_Linkor_reaserch_Parusa_O, Trig_Linkor_reaserch_Parusa_O_Actions)
end
--===========================================================================
-- Trigger: Naim Parusa O
--===========================================================================
function Trig_Naim_Parusa_O_Func001C()
    return ( ( GetUnitAbilityLevelSwapped(FourCC('A00B'), GetTrainedUnit()) == 1 ) )
end
function Trig_Naim_Parusa_O_Conditions()
    return Trig_Naim_Parusa_O_Func001C()
end
function Trig_Naim_Parusa_O_Func002C()
    return ( GetPlayerTechCountSimple(FourCC('R006'), GetOwningPlayer(GetTriggerUnit())) == 2 )
end
function Trig_Naim_Parusa_O_Func003C()
    return ( GetPlayerTechCountSimple(FourCC('R006'), GetOwningPlayer(GetTriggerUnit())) == 3 )
end
function Trig_Naim_Parusa_O_Actions()
    if ( Trig_Naim_Parusa_O_Func002C() ) then
        SetUnitAbilityLevelSwapped(FourCC('A00B'), GetTrainedUnit(), 2)
    end
    if ( Trig_Naim_Parusa_O_Func003C() ) then
        SetUnitAbilityLevelSwapped(FourCC('A00B'), GetTrainedUnit(), 3)
    end
end
--===========================================================================
function InitTrig_Naim_Parusa_O()
    gg_trg_Naim_Parusa_O=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_Naim_Parusa_O, EVENT_PLAYER_UNIT_TRAIN_FINISH)
    TriggerAddCondition(gg_trg_Naim_Parusa_O, Condition(Trig_Naim_Parusa_O_Conditions))
    TriggerAddAction(gg_trg_Naim_Parusa_O, Trig_Naim_Parusa_O_Actions)
end
--===========================================================================
-- Trigger: Linkor Repair O
--===========================================================================
function Trig_Linkor_Repair_O_Conditions()
    return ( GetResearched() == FourCC('R007') )
end
function Trig_Linkor_Repair_O_Func001Func002002()
    return ( 0 == 0 )
end
function Trig_Linkor_Repair_O_Func001Func004A()
    SetUnitAbilityLevelSwapped(FourCC('A00A'), GetEnumUnit(), 2)
end
function Trig_Linkor_Repair_O_Func001C()
    return ( GetPlayerTechCountSimple(FourCC('R007'), GetOwningPlayer(GetTriggerUnit())) == 2 )
end
function Trig_Linkor_Repair_O_Func002Func002002()
    return ( 0 == 0 )
end
function Trig_Linkor_Repair_O_Func002Func004A()
    SetUnitAbilityLevelSwapped(FourCC('A00A'), GetEnumUnit(), 3)
end
function Trig_Linkor_Repair_O_Func002C()
    return ( GetPlayerTechCountSimple(FourCC('R007'), GetOwningPlayer(GetTriggerUnit())) == 3 )
end
function Trig_Linkor_Repair_O_Actions()
    if ( Trig_Linkor_Repair_O_Func001C() ) then
        udg_Boolexpr = Trig_Linkor_Repair_O_Func001Func002002
        GroupEnumUnitsOfPlayer(udg_LocalOtrad2, udg_LocalPlayer, udg_Boolexpr)
        ForGroupBJ(udg_LocalOtrad2, Trig_Linkor_Repair_O_Func001Func004A)
        GroupClear(udg_LocalOtrad2)
    end
    if ( Trig_Linkor_Repair_O_Func002C() ) then
        udg_Boolexpr = Trig_Linkor_Repair_O_Func002Func002002
        GroupEnumUnitsOfPlayer(udg_LocalOtrad2, udg_LocalPlayer, udg_Boolexpr)
        ForGroupBJ(udg_LocalOtrad2, Trig_Linkor_Repair_O_Func002Func004A)
        GroupClear(udg_LocalOtrad2)
    end
end
--===========================================================================
function InitTrig_Linkor_Repair_O()
    gg_trg_Linkor_Repair_O=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_Linkor_Repair_O, EVENT_PLAYER_UNIT_RESEARCH_FINISH)
    TriggerAddCondition(gg_trg_Linkor_Repair_O, Condition(Trig_Linkor_Repair_O_Conditions))
    TriggerAddAction(gg_trg_Linkor_Repair_O, Trig_Linkor_Repair_O_Actions)
end
--===========================================================================
-- Trigger: Naim Rapair O
--===========================================================================
function Trig_Naim_Rapair_O_Func001C()
    return ( ( GetUnitAbilityLevelSwapped(FourCC('A00A'), GetTrainedUnit()) == 1 ) )
end
function Trig_Naim_Rapair_O_Conditions()
    return Trig_Naim_Rapair_O_Func001C()
end
function Trig_Naim_Rapair_O_Func002C()
    return ( GetPlayerTechCountSimple(FourCC('R007'), GetOwningPlayer(GetTriggerUnit())) == 2 )
end
function Trig_Naim_Rapair_O_Func003C()
    return ( GetPlayerTechCountSimple(FourCC('R007'), GetOwningPlayer(GetTriggerUnit())) == 3 )
end
function Trig_Naim_Rapair_O_Actions()
    if ( Trig_Naim_Rapair_O_Func002C() ) then
        SetUnitAbilityLevelSwapped(FourCC('A00A'), GetTrainedUnit(), 2)
    end
    if ( Trig_Naim_Rapair_O_Func003C() ) then
        SetUnitAbilityLevelSwapped(FourCC('A00A'), GetTrainedUnit(), 3)
    end
end
--===========================================================================
function InitTrig_Naim_Rapair_O()
    gg_trg_Naim_Rapair_O=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_Naim_Rapair_O, EVENT_PLAYER_UNIT_TRAIN_FINISH)
    TriggerAddCondition(gg_trg_Naim_Rapair_O, Condition(Trig_Naim_Rapair_O_Conditions))
    TriggerAddAction(gg_trg_Naim_Rapair_O, Trig_Naim_Rapair_O_Actions)
end
--===========================================================================
-- Trigger: Abordach D or Ot
--===========================================================================
function Trig_Abordach_D_or_Ot_Func005Func001C()
    return (( ( GetOwningPlayer(GetTriggerUnit()) == GetOwningPlayer(GetSpellTargetUnit()) ) )) or IsPlayerAlly(GetOwningPlayer(GetSpellTargetUnit()), GetOwningPlayer(GetTriggerUnit())) or IsUnitType(GetSpellTargetUnit(), UNIT_TYPE_STRUCTURE)
end
function Trig_Abordach_D_or_Ot_Func005C()
    return Trig_Abordach_D_or_Ot_Func005Func001C()
end
function Trig_Abordach_D_or_Ot_Func018Func003C()
    return true
end
function Trig_Abordach_D_or_Ot_Func018Func017Func005002()
    return IsUnitInTransportBJ(GetFilterUnit(), udg_LocalUnit2)
end
function Trig_Abordach_D_or_Ot_Func018Func017Func009Func001C()
    return IsUnitType(GetEnumUnit(), UNIT_TYPE_HERO) and IsUnitLoadedBJ(GetEnumUnit())
end
function Trig_Abordach_D_or_Ot_Func018Func017Func009A()
    if ( Trig_Abordach_D_or_Ot_Func018Func017Func009Func001C() ) then
        KillUnit(GetEnumUnit())
    end
end
function Trig_Abordach_D_or_Ot_Func018Func017Func011Func004002()
    return ( 0 == 0 )
end
function Trig_Abordach_D_or_Ot_Func018Func017Func011Func010Func001C()
    return ( GetUnitAbilityLevelSwapped(FourCC('A001'), GetEnumUnit()) == 1 )
end
function Trig_Abordach_D_or_Ot_Func018Func017Func011Func010A()
    if ( Trig_Abordach_D_or_Ot_Func018Func017Func011Func010Func001C() ) then
        UnitAddAbilityBJ(FourCC('A009'), GetEnumUnit())
    end
end
function Trig_Abordach_D_or_Ot_Func018Func017Func011C()
    return true
end
function Trig_Abordach_D_or_Ot_Func018Func017C()
    return true
end
function Trig_Abordach_D_or_Ot_Func018Func021Func007Func008002()
    return ( GetUnitAbilityLevelSwapped(FourCC('A001'), GetFilterUnit()) >= 1 )
end
function Trig_Abordach_D_or_Ot_Func018Func021Func007Func012A()
    UnitAddAbilityBJ(FourCC('A009'), GetEnumUnit())
end
function Trig_Abordach_D_or_Ot_Func018Func021Func007C()
    return true
end
function Trig_Abordach_D_or_Ot_Func018Func021Func011002()
    return IsUnitType(GetFilterUnit(), UNIT_TYPE_HERO)
end
function Trig_Abordach_D_or_Ot_Func018Func021Func015Func001C()
    return IsUnitLoadedBJ(GetEnumUnit())
end
function Trig_Abordach_D_or_Ot_Func018Func021Func015A()
    if ( Trig_Abordach_D_or_Ot_Func018Func021Func015Func001C() ) then
        KillUnit(GetEnumUnit())
    end
end
function Trig_Abordach_D_or_Ot_Func018Func021C()
    return true
end
function Trig_Abordach_D_or_Ot_Func018Func027C()
    return true
end
function Trig_Abordach_D_or_Ot_Func018Func028C()
    return true
end
function Trig_Abordach_D_or_Ot_Func018Func029C()
    return true
end
function Trig_Abordach_D_or_Ot_Func018Func030C()
    return true
end
function Trig_Abordach_D_or_Ot_Actions()
    local u = {}
    local p = {}
    local ef = {}
    if ( Trig_Abordach_D_or_Ot_Func005C() ) then
        return
    end
    u[1]=udg_LocalUnit[1]
    u[2]=udg_LocalUnit[2]
    p[1]=udg_LocalPosition[1]
    p[2]=udg_LocalPosition[2]
    for bj_forLoopAIndex = 1, 9 do
        udg_LocalUnit[1]=u[1]
        udg_LocalUnit[2]=u[2]
        if ( (true) ) then -- INLINED!!
            return
        end
        AddSpecialEffectLocBJ(udg_LocalPosition[1], "ObjectsSpawnmodelsHumanHCancelDeathHCancelDeath.mdl")
        udg_LocalspecialEffect[1]=GetLastCreatedEffectBJ()
        ef[1]=udg_LocalspecialEffect[1]
        AddSpecialEffectLocBJ(udg_LocalPosition[2], "ObjectsSpawnmodelsHumanHCancelDeathHCancelDeath.mdl")
        udg_LocalspecialEffect[2]=GetLastCreatedEffectBJ()
        ef[2]=udg_LocalspecialEffect[2]
        RemoveLocation(udg_LocalPosition[1])
        RemoveLocation(udg_LocalPosition[2])
        -- --------
        -- --------
        -- ??????? ??????? 1
        if ( (true) ) then -- INLINED!!
            udg_LocalUnit[1]=u[1]
            udg_LocalUnit[2]=u[2]
            TriggerExecute(gg_trg_AbordachSystemDefence2_O)
            udg_Boolexpr = Trig_Abordach_D_or_Ot_Func018Func017Func005002
            GroupEnumUnitsOfPlayer(udg_LocalOtrad2, udg_LocalPlayer, udg_Boolexpr)
            ForGroupBJ(udg_LocalOtrad2, Trig_Abordach_D_or_Ot_Func018Func017Func009A)
            GroupClear(udg_LocalOtrad2)
            if ( (true) ) then -- INLINED!!
                udg_Boolexpr = Trig_Abordach_D_or_Ot_Func018Func017Func011Func004002
                GroupEnumUnitsOfPlayer(udg_LocalOtrad2, udg_LocalPlayer, udg_Boolexpr)
                udg_LocalText2="cffff0000.r"
                DisplayTextToPlayer(GetOwningPlayer(udg_LocalUnit[2]), 0, 0, udg_LocalText2)
                udg_LocalText2="cff00ff00r not "
                DisplayTextToPlayer(GetOwningPlayer(udg_LocalUnit[1]), 0, 0, udg_LocalText2)
                ForGroupBJ(udg_LocalOtrad2, Trig_Abordach_D_or_Ot_Func018Func017Func011Func010A)
                GroupClear(udg_LocalOtrad2)
            end
            return
        end
        -- --------
        -- --------
        -- ??????? ??????? 2
        if ( (true) ) then -- INLINED!!
            udg_LocalUnit[1]=u[1]
            udg_LocalUnit[2]=u[2]
            TriggerExecute(gg_trg_AbordachSystemDefence1_O)
            if ( (true) ) then -- INLINED!!
                udg_LocalText2="cffff0000.r"
                DisplayTextToPlayer(GetOwningPlayer(udg_LocalUnit[1]), 0, 0, udg_LocalText2)
                udg_LocalText2="cff00ff00r not "
                DisplayTextToPlayer(GetOwningPlayer(udg_LocalUnit[2]), 0, 0, udg_LocalText2)
                udg_Boolexpr = Trig_Abordach_D_or_Ot_Func018Func021Func007Func008002
                GroupEnumUnitsOfPlayer(udg_LocalOtrad2, udg_LocalPlayer, udg_Boolexpr)
                ForGroupBJ(udg_LocalOtrad2, Trig_Abordach_D_or_Ot_Func018Func021Func007Func012A)
                GroupClear(udg_LocalOtrad2)
            end
            udg_Boolexpr = Trig_Abordach_D_or_Ot_Func018Func021Func011002
            GroupEnumUnitsOfPlayer(udg_LocalOtrad2, udg_LocalPlayer, udg_Boolexpr)
            ForGroupBJ(udg_LocalOtrad2, Trig_Abordach_D_or_Ot_Func018Func021Func015A)
            return
        end
        -- --------
        -- --------
        -- ???????? ???????)))
        if ( (true) ) then -- INLINED!!
        else
        end
        if ( (true) ) then -- INLINED!!
        else
        end
        if ( (true) ) then -- INLINED!!
        else
        end
        if ( (true) ) then -- INLINED!!
        else
        end
        -- ????? ???????? ====
        udg_LocalspecialEffect[1]=ef[1]
        udg_LocalspecialEffect[1]=ef[2]
        DestroyEffectBJ(udg_LocalspecialEffect[1])
        DestroyEffectBJ(udg_LocalspecialEffect[2])
        RemoveLocation(udg_LocalPosition[1])
        RemoveLocation(udg_LocalPosition[2])
        TriggerSleepAction(1.00)
        ef[1]=nil
        ef[2]=nil
    end
    udg_LocalUnit[1]=u[1]
    udg_LocalUnit[2]=u[2]
    RemoveLocation(udg_LocalPosition[1])
    RemoveLocation(udg_LocalPosition[2])
    u[1]=nil
    u[2]=nil
    p[1]=nil
    p[2]=nil
end
--===========================================================================
function InitTrig_Abordach_D_or_Ot()
    gg_trg_Abordach_D_or_Ot=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_Abordach_D_or_Ot, EVENT_PLAYER_UNIT_SPELL_CAST)
    TriggerAddAction(gg_trg_Abordach_D_or_Ot, function()
        if GetSpellAbilityId() ~= FourCC('A001') then return end
        Trig_Abordach_D_or_Ot_Actions()
    end)
end
--===========================================================================
-- Trigger: AbordachSystemDefence1 O
--===========================================================================
function Trig_AbordachSystemDefence1_O_Actions()
    local u = {}
    u[1]=udg_LocalUnit[1]
    TriggerSleepAction(3.00)
    udg_LocalUnit[1]=u[1]
    u[1]=nil
end
--===========================================================================
function InitTrig_AbordachSystemDefence1_O()
    gg_trg_AbordachSystemDefence1_O=CreateTrigger()
    TriggerAddAction(gg_trg_AbordachSystemDefence1_O, Trig_AbordachSystemDefence1_O_Actions)
end
--===========================================================================
-- Trigger: AbordachSystemDefence2 O
--===========================================================================
function Trig_AbordachSystemDefence2_O_Actions()
    local u = {}
    u[2]=udg_LocalUnit[2]
    TriggerSleepAction(3.00)
    udg_LocalUnit[2]=u[2]
    u[2]=nil
end
--===========================================================================
function InitTrig_AbordachSystemDefence2_O()
    gg_trg_AbordachSystemDefence2_O=CreateTrigger()
    TriggerAddAction(gg_trg_AbordachSystemDefence2_O, Trig_AbordachSystemDefence2_O_Actions)
end
--===========================================================================
-- Trigger: MageTp
--===========================================================================
function Trig_MageTp_Conditions()
    local id= GetSpellAbilityId()
    return id == FourCC('A0IO') or id == FourCC('A0VT') or id == FourCC('A0Y4') or id == FourCC('A0YK') or id == FourCC('A0I0')
end
function Trig_MageTp_Actions()
    local u= GetTriggerUnit()
    UnitAddAbility(u, FourCC('Avul'))
    RemoveAbilityTimed(u , FourCC('Avul') , 1.5)
    u=nil
end
--===========================================================================
function InitTrig_MageTp()
    gg_trg_MageTp=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_MageTp, EVENT_PLAYER_UNIT_SPELL_CHANNEL)
    TriggerAddCondition(gg_trg_MageTp, Condition(Trig_MageTp_Conditions))
    TriggerAddAction(gg_trg_MageTp, Trig_MageTp_Actions)
end
--===========================================================================
-- Trigger: TPrepeat
--===========================================================================
function CommandTp()
    local t= GetExpiredTimer()
    local id= GetHandleId(t)
    local u= LoadUnitHandle(Hash, id, 0)
    if u ~= nil and UnitAlive(u) and GetUnitAbilityLevel(u, FourCC('A1IH')) > 0 then
        IssuePointOrder(u, "darksummoning", LoadReal(Hash, id, 1), LoadReal(Hash, id, 2))
    
    
    else
        DestroyTimer(t)
        FlushChildHashtable(Hash, id)
    
    end
    u=nil
    t=nil
end
function Trig_TPrepeat_Actions()
    local t= CreateTimer()
    local id= GetHandleId(t)
    local u= GetTriggerUnit()
    
    SaveUnitHandle(Hash, id, 0, u)
    SaveReal(Hash, id, 1, GetSpellTargetX())
    SaveReal(Hash, id, 2, GetSpellTargetY())
    
    BlzUnitHideAbility(u, FourCC('A1IG'), true)
    RemoveAbilityTimed(u , FourCC('A1IG') , 1)
    UnitAddAbility(u, FourCC('A1IH'))
    
    TimerStart(t, RMaxBJ(BlzGetUnitAbilityCooldownRemaining(u, FourCC('A0IO')), 15), true, CommandTp)
    t=nil
    u=nil
end
--===========================================================================
function InitTrig_TPrepeat()
    gg_trg_TPrepeat=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_TPrepeat, EVENT_PLAYER_UNIT_SPELL_EFFECT)
    TriggerAddAction(gg_trg_TPrepeat, function()
        if GetSpellAbilityId() ~= FourCC('A1IG') then return end
        Trig_TPrepeat_Actions()
    end)
end
--===========================================================================
-- Trigger: TPrepatStop
--===========================================================================
function Trig_TPrepatStop_Actions()
    local u= GetTriggerUnit()
    BlzUnitHideAbility(u, FourCC('A1IH'), true)
    RemoveAbilityTimed(u , FourCC('A1IH') , 1)
    UnitAddAbility(u, FourCC('A1IG'))
    u=nil
end
--===========================================================================
function InitTrig_TPrepatStop()
    gg_trg_TPrepatStop=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_TPrepatStop, EVENT_PLAYER_UNIT_SPELL_EFFECT)
    TriggerAddAction(gg_trg_TPrepatStop, function()
        if GetSpellAbilityId() ~= FourCC('A1IH') then return end
        Trig_TPrepatStop_Actions()
    end)
end
--===========================================================================
-- Trigger: NoTpNearCapital
--===========================================================================
function CapitalOfEnemy()
    return IsUnitInGroup(GetFilterUnit(), udg_StolicaGroups) and IsPlayerEnemy(GetOwningPlayer(GetFilterUnit()), udg_LocalPlayer)
end
function Trig_NoTpNearCapital_Actions()
    local g= CreateGroup()
    local u= GetTriggerUnit()
   
    udg_LocalPlayer=GetOwningPlayer(u)
    GroupEnumUnitsInRange(g, GetUnitX(u), GetUnitY(u), 1350.00, CapitalOfEnemy)
    if FirstOfGroup(g) ~= nil then
        IssueImmediateOrder(u, "stop")
        DisplayTextToPlayer(GetOwningPlayer(u), 0, 0, " - ")
    end
    
    DestroyGroup(g)
    g=nil
    u=nil
    
end
--===========================================================================
function InitTrig_NoTpNearCapital()
    gg_trg_NoTpNearCapital=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_NoTpNearCapital, EVENT_PLAYER_UNIT_SPELL_CAST)
    TriggerAddAction(gg_trg_NoTpNearCapital, function()
        if GetSpellAbilityId() ~= FourCC('A0IO') then return end
        Trig_NoTpNearCapital_Actions()
    end)
end
--===========================================================================
-- Trigger: ManabombaNewSystem
--
-- ? ??????? ???? ????? ?????????
--===========================================================================
function damageRadious()
    local i= 0
    while true do
        if i >= times then break end
        UnitDamagePointLoc(damager, delay + interval * i, damage, destination, radious, Attacktype, Damagetype)
        i=i + 1
    end
end
  
function ManabombaNuke()
    local t= GetExpiredTimer()
    local tid= GetHandleId(t)
    local destination= LoadLocationHandle(Hash, tid, 0)
    local caster= LoadUnitHandle(Hash, tid, 3)
    RemoveUnit(LoadUnitHandle(Hash, tid, 1))
    RemoveUnit(LoadUnitHandle(Hash, tid, 2))
   -- call BJDebugMsg("")
    RemoveEffectTimed(AddSpecialEffectLocBJ(destination, "war3mapImportedExplosionC.mdx") , 60)
    --call RemoveEffectTimed( AddSpecialEffectLocBJ( destination, "ForceField03.mdx" ) 20)
    
    
    
    
    damageRadious(caster , 0.0 , 375.00 , destination , 70 , 20 , 0.25 , ATTACK_TYPE_CHAOS , DAMAGE_TYPE_MAGIC)
    damageRadious(caster , 5 , 600.00 , destination , 55 , 12 , 0.25 , ATTACK_TYPE_CHAOS , DAMAGE_TYPE_MAGIC)
    damageRadious(caster , 8 , 900.00 , destination , 3 , 160 , 0.25 , ATTACK_TYPE_CHAOS , DAMAGE_TYPE_MAGIC)
    damageRadious(caster , 8 , 375.00 , destination , 5 , 160 , 0.25 , ATTACK_TYPE_CHAOS , DAMAGE_TYPE_MAGIC)
    
    
    UnitRemoveAbility(caster, FourCC('A0TS'))
    
    
    PauseTimer(t)
    DestroyTimer(t)
    t=nil
    FlushChildHashtable(Hash, tid)
    caster=nil
    RemoveLocation(destination)
    destination=nil
end
function ManabombaMissle()
    local t= CreateTimer()
    local tid= GetHandleId(t)
    local l= GetUnitLoc(caster)
    local p= GetOwningPlayer(caster)
    local u1
    local u2
   --call BJDebugMsg("")
     
    -- ?????? ???? ?????????
    UnitRemoveAbility(caster, FourCC('A0TT'))
    -- ???? ??????
    u1=CreateUnitAtLoc(p, FourCC('h05P'), l, bj_UNIT_FACING)
    BlzSetUnitRealFieldBJ(u1, UNIT_RF_FLY_HEIGHT, GetUnitDefaultFlyHeight(caster))
    UnitAddAbilityBJ(FourCC('A0TU'), u1)
    -- ???? ??????
    u2=CreateUnitAtLoc(Player(PLAYER_NEUTRAL_AGGRESSIVE), FourCC('h0GI'), destination, bj_UNIT_FACING)
    BlzSetUnitRealFieldBJ(u2, UNIT_RF_FLY_HEIGHT, GetUnitDefaultFlyHeight(caster))
    
    
    
    SetUnitPathing(u1, false)
    SetUnitPathing(u2, false)
    IssueTargetOrder(u1, "firebolt", u2)
     
    TimerStart(t, ( DistanceBetweenPoints(l, destination) / 600.00 ), false, ManabombaNuke)
    SaveLocationHandle(Hash, tid, 0, destination)
    SaveUnitHandle(Hash, tid, 1, u1)
    SaveUnitHandle(Hash, tid, 2, u2)
    SaveUnitHandle(Hash, tid, 3, caster)
    
    RemoveLocation(l)
    l=nil
    u1=nil
    u2=nil
end
  
--===========================================================================
-- Trigger: ManabobmaStart
--===========================================================================
function Trig_ManabobmaStart_Conditions()
    return (( GetItemTypeId(GetManipulatedItem()) == FourCC('I01U') )) and (( GetUnitTypeId(GetTriggerUnit()) == FourCC('nzep') ))
end
function Trig_ManabobmaStart_Actions()
    UnitAddAbilityBJ(FourCC('A0TS'), GetTriggerUnit())
    UnitAddAbilityBJ(FourCC('A0TT'), GetTriggerUnit())
    BlzSetUnitMaxHP(GetTriggerUnit(), 3000)
    SetUnitLifePercentBJ(GetTriggerUnit(), 100)
    RemoveItem(GetManipulatedItem())
    TriggerRegisterUnitEvent(gg_trg_ManabombaDead, GetTriggerUnit(), EVENT_UNIT_DEATH)
    TriggerRegisterUnitEvent(gg_trg_Manabomba2, GetTriggerUnit(), EVENT_UNIT_SPELL_CHANNEL)
end
--===========================================================================
function InitTrig_ManabobmaStart()
    gg_trg_ManabobmaStart=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_ManabobmaStart, EVENT_PLAYER_UNIT_PICKUP_ITEM)
    TriggerAddCondition(gg_trg_ManabobmaStart, Condition(Trig_ManabobmaStart_Conditions))
    TriggerAddAction(gg_trg_ManabobmaStart, Trig_ManabobmaStart_Actions)
end
--===========================================================================
-- Trigger: ManabombaDead
--
-- ? ??????? ???? ????? ?????????
--===========================================================================
function Trig_ManabombaDead_Actions()
    --call BJDebugMsg("")
    ManabombaMissle(GetTriggerUnit() , GetUnitLoc(GetTriggerUnit()))
end
--===========================================================================
function InitTrig_ManabombaDead()
    gg_trg_ManabombaDead=CreateTrigger()
    TriggerAddAction(gg_trg_ManabombaDead, Trig_ManabombaDead_Actions)
end
--===========================================================================
-- Trigger: Manabomba2
--
-- ? ??????? ???? ????? ?????????
--===========================================================================
function Trig_Manabomba2_Actions()
    --call BJDebugMsg("")
    ManabombaMissle(GetTriggerUnit() , GetSpellTargetLoc())
end
--===========================================================================
function InitTrig_Manabomba2()
    gg_trg_Manabomba2=CreateTrigger()
    TriggerAddAction(gg_trg_Manabomba2, function()
        if GetSpellAbilityId() ~= FourCC('A0TS') then return end
        Trig_Manabomba2_Actions()
    end)
end
--===========================================================================
-- Trigger: Portal Connect
--===========================================================================
function Trig_Portal_Connect_Func008Func004Func001Func002C()
    return not (udg_Portal_active[udg_Portal_INDEX_CASTER]) and not (udg_Portal_active[udg_Portal_INDEX_TARGET])
end
function Trig_Portal_Connect_Func008Func004Func001C()
    return ( GetTriggerUnit() == udg_Portal_portal[udg_Portal_INDEX_TARGET] )
end
function Trig_Portal_Connect_Func008Func004C()
    return udg_Portal_active[udg_Portal_INDEX_TARGET] and (( GetSpellTargetUnit() ~= udg_Portal_portal[udg_Portal_INDEX_CASTER] ))
end
function Trig_Portal_Connect_Func008C()
    return udg_Portal_active[udg_Portal_INDEX_CASTER] and (( GetSpellTargetUnit() ~= udg_Portal_portal[udg_Portal_INDEX_CASTER] )) and not (udg_Portal_active[udg_Portal_INDEX_TARGET])
end
function Trig_Portal_Connect_Actions()
    if udg_Portal_SeverAbility == nil then
    udg_Portal_SeverAbility=FourCC('A0TR')
    end
    -- NB
    -- Portal_portal[Portal_INDEX_CASTER] is the sister portal
    -- Portal_portal[Portal_INDEX_TARGET] is the caster portal
    -- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- --------
    if ( Trig_Portal_Connect_Func008C() ) then
        -- TRAVELLER here is the index of the existing sister portal. Therefore, Portal_portal[Portal_INDEX_TRAVELLER] is the caster portal
        -- Anything else indexed to TRAVELLER, however, is for the currently connected sister portal. TRAVELLER is used here to disengage her from the caster
        udg_Portal_INDEX_TRAVELLER=GetUnitUserData(udg_Portal_portal[udg_Portal_INDEX_CASTER])
        DestroyEffectBJ(udg_Portal_FX[udg_Portal_INDEX_CASTER])
        DestroyEffectBJ(udg_Portal_FX[udg_Portal_INDEX_TRAVELLER])
        UnitRemoveAbilityBJ(udg_Portal_SeverAbility, udg_Portal_portal[udg_Portal_INDEX_CASTER])
        UnitRemoveAbilityBJ(udg_Portal_SeverAbility, udg_Portal_portal[udg_Portal_INDEX_TRAVELLER])
        udg_Portal_active[udg_Portal_INDEX_TRAVELLER]=false
        udg_Portal_portal[udg_Portal_INDEX_TRAVELLER]=nil
        -- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- --------
        -- Portal_portal[Portal_INDEX_CASTER] is set to the new sister portal
        udg_Portal_portal[udg_Portal_INDEX_CASTER]=GetSpellTargetUnit()
        udg_Portal_portal[udg_Portal_INDEX_TARGET]=GetTriggerUnit()
        udg_Portal_active[udg_Portal_INDEX_TARGET]=true
        AddSpecialEffectTargetUnitBJ("origin", udg_Portal_portal[udg_Portal_INDEX_TARGET], udg_Portal_activeFX[udg_Portal_INDEX_CASTER])
        udg_Portal_FX[udg_Portal_INDEX_CASTER]=GetLastCreatedEffectBJ()
        AddSpecialEffectTargetUnitBJ("origin", udg_Portal_portal[udg_Portal_INDEX_CASTER], udg_Portal_activeFX[udg_Portal_INDEX_TARGET])
        udg_Portal_FX[udg_Portal_INDEX_TARGET]=GetLastCreatedEffectBJ()
        -- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- --------
        UnitAddAbilityBJ(udg_Portal_SeverAbility, udg_Portal_portal[udg_Portal_INDEX_TARGET])
        UnitAddAbilityBJ(udg_Portal_SeverAbility, udg_Portal_portal[udg_Portal_INDEX_CASTER])
    else
        if ( Trig_Portal_Connect_Func008Func004C() ) then
        else
            if ( Trig_Portal_Connect_Func008Func004Func001C() ) then
            else
                -- If the targeted Portal, and the cast, are not active, connect them to one another
                if ( Trig_Portal_Connect_Func008Func004Func001Func002C() ) then
                    udg_Portal_active[udg_Portal_INDEX_CASTER]=true
                    udg_Portal_active[udg_Portal_INDEX_TARGET]=true
                    udg_Portal_portal[udg_Portal_INDEX_CASTER]=GetSpellTargetUnit()
                    udg_Portal_portal[udg_Portal_INDEX_TARGET]=GetTriggerUnit()
                    -- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- --------
                    AddSpecialEffectTargetUnitBJ("origin", GetTriggerUnit(), udg_Portal_activeFX[udg_Portal_INDEX_CASTER])
                    udg_Portal_FX[udg_Portal_INDEX_CASTER]=GetLastCreatedEffectBJ()
                    AddSpecialEffectTargetUnitBJ("origin", GetSpellTargetUnit(), udg_Portal_activeFX[udg_Portal_INDEX_TARGET])
                    udg_Portal_FX[udg_Portal_INDEX_TARGET]=GetLastCreatedEffectBJ()
                    -- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- --------
                    UnitAddAbilityBJ(udg_Portal_SeverAbility, udg_Portal_portal[udg_Portal_INDEX_TARGET])
                    UnitAddAbilityBJ(udg_Portal_SeverAbility, udg_Portal_portal[udg_Portal_INDEX_CASTER])
                end
            end
        end
    end
end
--===========================================================================
function InitTrig_Portal_Connect()
    gg_trg_Portal_Connect=CreateTrigger()
    TriggerAddAction(gg_trg_Portal_Connect, Trig_Portal_Connect_Actions)
end
--===========================================================================
-- Trigger: Portal Periodic
--===========================================================================
function Trig_Portal_Periodic_Func001Func006Func001C()
    return udg_Portal_isTeleporting[udg_Portal_INDEX_CASTER]
end
function Trig_Portal_Periodic_Func001Func006Func002Func002C()
    return not (udg_Portal_isTeleporting[udg_Portal_INDEX_CASTER])
end
function Trig_Portal_Periodic_Func001Func006Func002Func011Func003C()
    return IsUnitSelected(udg_Portal_traveller, GetOwningPlayer(udg_Portal_traveller))
end
function Trig_Portal_Periodic_Func001Func006Func002Func011Func004C()
    return udg_Portal_missileTargetable[udg_Portal_INDEX_TARGET]
end
function Trig_Portal_Periodic_Func001Func006Func002Func011Func012Func004C()
    return IsUnitSelected(udg_Portal_traveller, GetOwningPlayer(udg_Portal_traveller))
end
function Trig_Portal_Periodic_Func001Func006Func002Func011Func012Func005C()
    return udg_Portal_missileTargetable[udg_Portal_INDEX_TARGET]
end
function Trig_Portal_Periodic_Func001Func006Func002Func011Func012C()
    return ( udg_Portal_missileSpeed[udg_Portal_INDEX_TARGET] > 0.00 )
end
function Trig_Portal_Periodic_Func001Func006Func002Func011C()
    return udg_Portal_missileUseOwnMovement[udg_Portal_INDEX_TARGET]
end
function Trig_Portal_Periodic_Func001Func006Func002C()
    return ( udg_Portal_delay[udg_Portal_INDEX_CASTER] > 0.00 )
end
function Trig_Portal_Periodic_Func001Func006C()
    return ( DistanceBetweenPoints(udg_Portal_loc1, udg_Portal_loc3) <= udg_Portal_range[udg_Portal_INDEX_TARGET] )
end
function Trig_Portal_Periodic_Func001A()
    udg_Portal_traveller=GetEnumUnit()
    udg_Portal_INDEX_CASTER=GetUnitUserData(udg_Portal_traveller)
    udg_Portal_INDEX_TARGET=GetUnitUserData(udg_Portal_targeted[udg_Portal_INDEX_CASTER])
    udg_Portal_loc1=GetUnitLoc(udg_Portal_traveller)
    udg_Portal_loc3=GetUnitLoc(udg_Portal_targeted[udg_Portal_INDEX_CASTER])
    if ( Trig_Portal_Periodic_Func001Func006C() ) then
        if ( Trig_Portal_Periodic_Func001Func006Func002C() ) then
            if ( Trig_Portal_Periodic_Func001Func006Func002Func002C() ) then
                udg_Portal_isTeleporting[udg_Portal_INDEX_CASTER]=true
                udg_Portal_delayFXAbil[udg_Portal_INDEX_CASTER]=udg_Portal_delayFXAbil[udg_Portal_INDEX_TARGET]
                UnitAddAbilityBJ(udg_Portal_delayFXAbil[udg_Portal_INDEX_CASTER], udg_Portal_traveller)
            end
            udg_Portal_delay[udg_Portal_INDEX_CASTER]=( udg_Portal_delay[udg_Portal_INDEX_CASTER] - ( 1.00 / 32.00 ) )
        else
            udg_Portal_isTeleporting[udg_Portal_INDEX_CASTER]=false
            udg_Portal_loc2=GetUnitLoc(udg_Portal_traveller)
            AddSpecialEffectLocBJ(udg_Portal_loc2, udg_Portal_departureFX[udg_Portal_INDEX_TARGET])
            DestroyEffectBJ(GetLastCreatedEffectBJ())
            UnitRemoveAbilityBJ(udg_Portal_delayFXAbil[udg_Portal_INDEX_CASTER], udg_Portal_traveller)
            RemoveLocation(udg_Portal_loc2)
            udg_Portal_loc2=GetUnitLoc(udg_Portal_portal[udg_Portal_INDEX_TARGET])
            -- -------- -------- -------- -------- -------- -------- -------- -------- -------- --------
            if ( Trig_Portal_Periodic_Func001Func006Func002Func011C() ) then
                CreateNUnitsAtLocFacingLocBJ(1, udg_Portal_missileDummy[udg_Portal_INDEX_TARGET], GetOwningPlayer(udg_Portal_traveller), udg_Portal_loc1, udg_Portal_loc2)
                udg_Portal_dummy=GetLastCreatedUnit()
                if ( Trig_Portal_Periodic_Func001Func006Func002Func011Func003C() ) then
                    SelectUnitAddForPlayer(udg_Portal_dummy, GetOwningPlayer(udg_Portal_traveller))
                end
                if ( Trig_Portal_Periodic_Func001Func006Func002Func011Func004C() ) then
                    SetUnitInvulnerable(udg_Portal_dummy, false)
                end
                IssuePointOrderLocBJ(udg_Portal_dummy, "move", udg_Portal_loc2)
                udg_Portal_INDEX_TRAVELLER=GetUnitUserData(udg_Portal_dummy)
                udg_Portal_missileSpeed[udg_Portal_INDEX_TRAVELLER]=0.00
                udg_Portal_portal[udg_Portal_INDEX_TRAVELLER]=udg_Portal_portal[udg_Portal_INDEX_TARGET]
                udg_Portal_targeted[udg_Portal_INDEX_TRAVELLER]=udg_Portal_traveller
                GroupAddUnitSimple(udg_Portal_dummy, udg_Portal_teleMissiles)
                ShowUnitHide(udg_Portal_traveller)
            else
                if ( Trig_Portal_Periodic_Func001Func006Func002Func011Func012C() ) then
                    CreateNUnitsAtLocFacingLocBJ(1, udg_Portal_missileDummy[udg_Portal_INDEX_TARGET], GetOwningPlayer(udg_Portal_traveller), udg_Portal_loc1, udg_Portal_loc2)
                    udg_Portal_dummy=GetLastCreatedUnit()
                    if ( Trig_Portal_Periodic_Func001Func006Func002Func011Func012Func004C() ) then
                        SelectUnitAddForPlayer(udg_Portal_dummy, GetOwningPlayer(udg_Portal_traveller))
                    end
                    if ( Trig_Portal_Periodic_Func001Func006Func002Func011Func012Func005C() ) then
                        SetUnitInvulnerable(udg_Portal_dummy, false)
                    end
                    UnitAddAbilityBJ(udg_Portal_missileFXAbil[udg_Portal_INDEX_TARGET], udg_Portal_dummy)
                    SetUnitFlyHeightBJ(udg_Portal_dummy, udg_Portal_missileHeight[udg_Portal_INDEX_TARGET], 0.00)
                    udg_Portal_INDEX_TRAVELLER=GetUnitUserData(udg_Portal_dummy)
                    udg_Portal_missileSpeed[udg_Portal_INDEX_TRAVELLER]=udg_Portal_missileSpeed[udg_Portal_INDEX_TARGET]
                    udg_Portal_portal[udg_Portal_INDEX_TRAVELLER]=udg_Portal_portal[udg_Portal_INDEX_TARGET]
                    udg_Portal_targeted[udg_Portal_INDEX_TRAVELLER]=udg_Portal_traveller
                    SetUnitPathing(udg_Portal_dummy, false)
                    GroupAddUnitSimple(udg_Portal_dummy, udg_Portal_teleMissiles)
                    ShowUnitHide(udg_Portal_traveller)
                else
                    RemoveLocation(udg_Portal_loc3)
                    udg_Portal_INDEX_TRAVELLER=GetUnitUserData(udg_Portal_portal[udg_Portal_INDEX_TARGET])
                    udg_Portal_loc3=PolarProjectionBJ(udg_Portal_loc2, GetRandomReal(0.00, udg_Portal_range[udg_Portal_INDEX_TRAVELLER]), GetRandomDirectionDeg())
                    SetUnitPositionLoc(udg_Portal_traveller, udg_Portal_loc3)
                    udg_Portal_loc4=GetUnitRallyPoint(udg_Portal_targeted[udg_Portal_INDEX_CASTER])
                    IssuePointOrderLocBJ(udg_Portal_traveller, "attack", udg_Portal_loc4)
                    RemoveLocation(udg_Portal_loc4)
                    AddSpecialEffectLocBJ(udg_Portal_loc3, udg_Portal_arrivalFX[udg_Portal_INDEX_TRAVELLER])
                    DestroyEffectBJ(GetLastCreatedEffectBJ())
                end
            end
            RemoveLocation(udg_Portal_loc2)
            udg_Portal_targeted[udg_Portal_INDEX_CASTER]=nil
            GroupRemoveUnitSimple(udg_Portal_traveller, udg_Portal_group)
        end
    else
        if ( Trig_Portal_Periodic_Func001Func006Func001C() ) then
            -- This is here in case of a unit being knockbacked outside the Portal's reach
            udg_Portal_isTeleporting[udg_Portal_INDEX_CASTER]=false
            IssueTargetOrderBJ(udg_Portal_traveller, "smart", udg_Portal_targeted[udg_Portal_INDEX_CASTER])
        end
    end
    -- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- 
    RemoveLocation(udg_Portal_loc3)
    RemoveLocation(udg_Portal_loc1)
end
function Trig_Portal_Periodic_Func002Func007Func003Func001Func001C()
    return IsUnitAliveBJ(udg_Portal_portal[udg_Portal_INDEX_TRAVELLER])
end
function Trig_Portal_Periodic_Func002Func007Func003Func001Func012C()
    return IsUnitSelected(udg_Portal_traveller, GetOwningPlayer(udg_Portal_traveller))
end
function Trig_Portal_Periodic_Func002Func007Func003Func001C()
    return ( DistanceBetweenPoints(udg_Portal_loc1, udg_Portal_loc2) <= udg_Portal_range[udg_Portal_INDEX_TARGET] )
end
function Trig_Portal_Periodic_Func002Func007Func003Func002Func013C()
    return IsUnitSelected(udg_Portal_traveller, GetOwningPlayer(udg_Portal_traveller))
end
function Trig_Portal_Periodic_Func002Func007Func003Func002Func014C()
    return IsUnitAliveBJ(udg_Portal_portal[udg_Portal_INDEX_TRAVELLER])
end
function Trig_Portal_Periodic_Func002Func007Func003Func002C()
    return ( DistanceBetweenPoints(udg_Portal_loc1, udg_Portal_loc2) <= ( udg_Portal_missileSpeed[udg_Portal_INDEX_TRAVELLER] / 33.00 ) )
end
function Trig_Portal_Periodic_Func002Func007Func003C()
    return ( udg_Portal_missileSpeed[udg_Portal_INDEX_TRAVELLER] > 0.00 )
end
function Trig_Portal_Periodic_Func002Func007Func015C()
    return IsUnitSelected(udg_Portal_traveller, GetOwningPlayer(udg_Portal_traveller))
end
function Trig_Portal_Periodic_Func002Func007C()
    return IsUnitAliveBJ(udg_Portal_traveller)
end
function Trig_Portal_Periodic_Func002A()
    -- In this group, the Portal_traveller is the missile unit, not the actual unit being teleported
    -- The unit is Portal_targeted
    udg_Portal_traveller=GetEnumUnit()
    udg_Portal_INDEX_TRAVELLER=GetUnitUserData(udg_Portal_traveller)
    udg_Portal_INDEX_CASTER=GetUnitUserData(udg_Portal_targeted[udg_Portal_INDEX_TRAVELLER])
    udg_Portal_INDEX_TARGET=GetUnitUserData(udg_Portal_portal[udg_Portal_INDEX_TRAVELLER])
    if ( Trig_Portal_Periodic_Func002Func007C() ) then
        udg_Portal_loc1=GetUnitLoc(udg_Portal_traveller)
        udg_Portal_loc2=GetUnitLoc(udg_Portal_portal[udg_Portal_INDEX_TRAVELLER])
        if ( Trig_Portal_Periodic_Func002Func007Func003C() ) then
            if ( Trig_Portal_Periodic_Func002Func007Func003Func002C() ) then
                ShowUnitShow(udg_Portal_targeted[udg_Portal_INDEX_TRAVELLER])
                udg_Portal_loc3=PolarProjectionBJ(udg_Portal_loc1, GetRandomReal(0.00, udg_Portal_range[GetUnitUserData(udg_Portal_portal[udg_Portal_INDEX_TRAVELLER])]), GetRandomDirectionDeg())
                SetUnitPositionLoc(udg_Portal_targeted[udg_Portal_INDEX_TRAVELLER], udg_Portal_loc3)
                UnitApplyTimedLifeBJ(0.01, FourCC('BTLF'), udg_Portal_traveller)
                GroupRemoveUnitSimple(udg_Portal_traveller, udg_Portal_teleMissiles)
                GroupRemoveUnitSimple(udg_Portal_targeted[udg_Portal_INDEX_TRAVELLER], udg_Portal_group)
                AddSpecialEffectLocBJ(udg_Portal_loc3, udg_Portal_arrivalFX[GetUnitUserData(udg_Portal_portal[udg_Portal_INDEX_TRAVELLER])])
                DestroyEffectBJ(GetLastCreatedEffectBJ())
                udg_Portal_loc4=GetUnitRallyPoint(udg_Portal_portal[udg_Portal_INDEX_TRAVELLER])
                IssuePointOrderLocBJ(udg_Portal_targeted[udg_Portal_INDEX_TRAVELLER], "attack", udg_Portal_loc4)
                RemoveLocation(udg_Portal_loc4)
                RemoveLocation(udg_Portal_loc3)
                if ( Trig_Portal_Periodic_Func002Func007Func003Func002Func013C() ) then
                    SelectUnitAddForPlayer(udg_Portal_targeted[udg_Portal_INDEX_TRAVELLER], GetOwningPlayer(udg_Portal_traveller))
                end
            else
                if ( Trig_Portal_Periodic_Func002Func007Func003Func002Func014C() ) then
                    udg_Portal_loc3=PolarProjectionBJ(udg_Portal_loc1, ( udg_Portal_missileSpeed[udg_Portal_INDEX_TRAVELLER] / 33.00 ), AngleBetweenPoints(udg_Portal_loc1, udg_Portal_loc2))
                    SetUnitPositionLocFacingLocBJ(udg_Portal_traveller, udg_Portal_loc3, udg_Portal_loc2)
                    RemoveLocation(udg_Portal_loc3)
                else
                    UnitApplyTimedLifeBJ(0.01, FourCC('BTLF'), udg_Portal_traveller)
                end
            end
        else
            if ( Trig_Portal_Periodic_Func002Func007Func003Func001C() ) then
                ShowUnitShow(udg_Portal_targeted[udg_Portal_INDEX_TRAVELLER])
                SetUnitPositionLoc(udg_Portal_targeted[udg_Portal_INDEX_TRAVELLER], udg_Portal_loc1)
                UnitApplyTimedLifeBJ(0.01, FourCC('BTLF'), udg_Portal_traveller)
                GroupRemoveUnitSimple(udg_Portal_traveller, udg_Portal_teleMissiles)
                GroupRemoveUnitSimple(udg_Portal_targeted[udg_Portal_INDEX_TRAVELLER], udg_Portal_group)
                AddSpecialEffectLocBJ(udg_Portal_loc1, udg_Portal_arrivalFX[udg_Portal_INDEX_TARGET])
                DestroyEffectBJ(GetLastCreatedEffectBJ())
                udg_Portal_loc4=GetUnitRallyPoint(udg_Portal_portal[udg_Portal_INDEX_TRAVELLER])
                IssuePointOrderLocBJ(udg_Portal_targeted[udg_Portal_INDEX_TRAVELLER], "attack", udg_Portal_loc4)
                RemoveLocation(udg_Portal_loc4)
                if ( Trig_Portal_Periodic_Func002Func007Func003Func001Func012C() ) then
                    SelectUnitAddForPlayer(udg_Portal_targeted[udg_Portal_INDEX_TRAVELLER], GetOwningPlayer(udg_Portal_traveller))
                end
            else
                if ( Trig_Portal_Periodic_Func002Func007Func003Func001Func001C() ) then
                else
                    UnitApplyTimedLifeBJ(0.01, FourCC('BTLF'), udg_Portal_traveller)
                end
            end
        end
        RemoveLocation(udg_Portal_loc2)
        RemoveLocation(udg_Portal_loc1)
    else
        ShowUnitShow(udg_Portal_targeted[udg_Portal_INDEX_TRAVELLER])
        udg_Portal_loc1=GetUnitLoc(udg_Portal_traveller)
        SetUnitPositionLoc(udg_Portal_targeted[udg_Portal_INDEX_TRAVELLER], udg_Portal_loc1)
        RemoveLocation(udg_Portal_loc1)
        SetUnitFlyHeightBJ(udg_Portal_targeted[udg_Portal_INDEX_TRAVELLER], GetUnitFlyHeight(udg_Portal_traveller), 0.00)
        ExplodeUnitBJ(udg_Portal_targeted[udg_Portal_INDEX_TRAVELLER])
        GroupRemoveUnitSimple(udg_Portal_targeted[udg_Portal_INDEX_TRAVELLER], udg_Portal_group)
        GroupRemoveUnitSimple(udg_Portal_traveller, udg_Portal_teleMissiles)
        UnitRemoveAbilityBJ(udg_Portal_delayFXAbil[udg_Portal_INDEX_TRAVELLER], udg_Portal_traveller)
        if ( Trig_Portal_Periodic_Func002Func007Func015C() ) then
            SelectUnitAddForPlayer(udg_Portal_targeted[udg_Portal_INDEX_TRAVELLER], GetOwningPlayer(udg_Portal_traveller))
        end
    end
end
function Trig_Portal_Periodic_Func003C()
    return IsUnitGroupEmptyBJ(udg_Portal_group) and IsUnitGroupEmptyBJ(udg_Portal_teleMissiles)
end
function Trig_Portal_Periodic_Actions()
    ForGroupBJ(udg_Portal_group, Trig_Portal_Periodic_Func001A)
    ForGroupBJ(udg_Portal_teleMissiles, Trig_Portal_Periodic_Func002A)
    if ( Trig_Portal_Periodic_Func003C() ) then
        DisableTrigger(GetTriggeringTrigger())
    end
end
--===========================================================================
function InitTrig_Portal_Periodic()
    gg_trg_Portal_Periodic=CreateTrigger()
    DisableTrigger(gg_trg_Portal_Periodic)
    TriggerRegisterTimerEventPeriodic(gg_trg_Portal_Periodic, ( 1 / 32.00 ))
    TriggerAddAction(gg_trg_Portal_Periodic, Trig_Portal_Periodic_Actions)
end
--===========================================================================
-- Trigger: Portal Target
--===========================================================================
function Trig_Portal_Target_Func006C()
    return (( ( GetIssuedOrderIdBJ() == String2OrderIdBJ("smart") ) )) or (( ( GetIssuedOrderIdBJ() == String2OrderIdBJ("move") ) ))
end
function Trig_Portal_Target_Conditions()
    return udg_Portal_active[GetUnitUserData(GetOrderTargetUnit())] and not (IsUnitInGroup(GetTriggerUnit(), udg_Portal_teleMissiles)) and (Trig_Portal_Target_Func006C()) and IsUnitAlly(GetTriggerUnit(), GetOwningPlayer(GetOrderTargetUnit())) and not (IsUnitType(GetTriggerUnit(), UNIT_TYPE_STRUCTURE))
end
function Trig_Portal_Target_Func003Func001Func005C()
    return not (IsTriggerEnabled(gg_trg_Portal_Periodic))
end
function Trig_Portal_Target_Func003Func001C()
    return udg_Portal_preventAllies[udg_Portal_INDEX_TARGET] and (( GetOwningPlayer(GetTriggerUnit()) ~= GetOwningPlayer(GetOrderTargetUnit()) ))
end
function Trig_Portal_Target_Func003C()
    return udg_Portal_active[udg_Portal_INDEX_CASTER]
end
function Trig_Portal_Target_Actions()
    udg_Portal_INDEX_CASTER=GetUnitUserData(GetTriggerUnit())
    udg_Portal_INDEX_TARGET=GetUnitUserData(GetOrderTargetUnit())
    if ( Trig_Portal_Target_Func003C() ) then
        DisplayTimedTextToForce(GetForceOfPlayer(GetOwningPlayer(GetTriggerUnit())), 10.00, "TRIGSTR_19362")
    else
        if ( Trig_Portal_Target_Func003Func001C() ) then
        else
            udg_Portal_targeted[udg_Portal_INDEX_CASTER]=GetOrderTargetUnit()
            GroupAddUnitSimple(GetTriggerUnit(), udg_Portal_group)
            udg_Portal_delay[udg_Portal_INDEX_CASTER]=udg_Portal_delay[udg_Portal_INDEX_TARGET]
            -- -------- -------- -------- -------- -------- -------- -------- -------- -------- --------
            if ( Trig_Portal_Target_Func003Func001Func005C() ) then
                EnableTrigger(gg_trg_Portal_Periodic)
            end
        end
    end
end
--===========================================================================
function InitTrig_Portal_Target()
    gg_trg_Portal_Target=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_Portal_Target, EVENT_PLAYER_UNIT_ISSUED_TARGET_ORDER)
    TriggerAddCondition(gg_trg_Portal_Target, Condition(Trig_Portal_Target_Conditions))
    TriggerAddAction(gg_trg_Portal_Target, Trig_Portal_Target_Actions)
end
--===========================================================================
-- Trigger: Portal Disengage
--===========================================================================
function Trig_Portal_Disengage_Conditions()
    return IsUnitInGroup(GetTriggerUnit(), udg_Portal_group) and (( GetOrderTargetUnit() ~= udg_Portal_targeted[GetUnitUserData(GetTriggerUnit())] ))
end
function Trig_Portal_Disengage_Actions()
    udg_Portal_INDEX_CASTER=GetUnitUserData(GetTriggerUnit())
    udg_Portal_INDEX_TARGET=GetUnitUserData(udg_Portal_targeted[udg_Portal_INDEX_CASTER])
    udg_Portal_delay[udg_Portal_INDEX_CASTER]=0.00
    udg_Portal_isTeleporting[udg_Portal_INDEX_CASTER]=false
    udg_Portal_targeted[udg_Portal_INDEX_CASTER]=nil
    GroupRemoveUnitSimple(GetTriggerUnit(), udg_Portal_group)
    UnitRemoveAbilityBJ(udg_Portal_delayFXAbil[udg_Portal_INDEX_TARGET], GetTriggerUnit())
end
--===========================================================================
function InitTrig_Portal_Disengage()
    gg_trg_Portal_Disengage=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_Portal_Disengage, EVENT_PLAYER_UNIT_ISSUED_TARGET_ORDER)
    TriggerRegisterAnyUnitEventBJ(gg_trg_Portal_Disengage, EVENT_PLAYER_UNIT_ISSUED_POINT_ORDER)
    TriggerRegisterAnyUnitEventBJ(gg_trg_Portal_Disengage, EVENT_PLAYER_UNIT_ISSUED_ORDER)
    TriggerRegisterAnyUnitEventBJ(gg_trg_Portal_Disengage, EVENT_PLAYER_UNIT_DEATH)
    TriggerAddCondition(gg_trg_Portal_Disengage, Condition(Trig_Portal_Disengage_Conditions))
    TriggerAddAction(gg_trg_Portal_Disengage, Trig_Portal_Disengage_Actions)
end
--===========================================================================
-- Trigger: Portal Death
--===========================================================================
function Trig_Portal_Death_Conditions()
    return udg_Portal_active[GetUnitUserData(GetTriggerUnit())]
end
function Trig_Portal_Death_Func004Func004C()
    return ( GetTriggerUnit() == udg_Portal_targeted[udg_Portal_INDEX_TRAVELLER] )
end
function Trig_Portal_Death_Func004Func005C()
    return ( udg_Portal_portal[udg_Portal_INDEX_CASTER] == udg_Portal_targeted[udg_Portal_INDEX_TRAVELLER] )
end
function Trig_Portal_Death_Func004A()
    udg_Portal_traveller=GetEnumUnit()
    udg_Portal_INDEX_TRAVELLER=GetUnitUserData(udg_Portal_traveller)
    UnitRemoveAbilityBJ(udg_Portal_delayFXAbil[udg_Portal_INDEX_CASTER], udg_Portal_traveller)
    if ( Trig_Portal_Death_Func004Func004C() ) then
        udg_Portal_targeted[udg_Portal_INDEX_TRAVELLER]=nil
        udg_Portal_delay[udg_Portal_INDEX_TRAVELLER]=0.00
        udg_Portal_isTeleporting[udg_Portal_INDEX_TRAVELLER]=false
        GroupRemoveUnitSimple(udg_Portal_traveller, udg_Portal_group)
    end
    if ( Trig_Portal_Death_Func004Func005C() ) then
        udg_Portal_targeted[udg_Portal_INDEX_TRAVELLER]=nil
        udg_Portal_delay[udg_Portal_INDEX_TRAVELLER]=0.00
        udg_Portal_isTeleporting[udg_Portal_INDEX_TRAVELLER]=false
        GroupRemoveUnitSimple(udg_Portal_traveller, udg_Portal_group)
    end
end
function Trig_Portal_Death_Actions()
    udg_Portal_INDEX_CASTER=GetUnitUserData(GetTriggerUnit())
    udg_Portal_INDEX_TARGET=GetUnitUserData(udg_Portal_portal[udg_Portal_INDEX_CASTER])
    ForGroupBJ(udg_Portal_group, Trig_Portal_Death_Func004A)
    udg_Portal_active[udg_Portal_INDEX_CASTER]=false
    udg_Portal_active[udg_Portal_INDEX_TARGET]=false
    DestroyEffectBJ(udg_Portal_FX[udg_Portal_INDEX_CASTER])
    DestroyEffectBJ(udg_Portal_FX[udg_Portal_INDEX_TARGET])
    udg_Portal_portal[udg_Portal_INDEX_CASTER]=nil
    udg_Portal_portal[udg_Portal_INDEX_TARGET]=nil
end
--===========================================================================
function InitTrig_Portal_Death()
    gg_trg_Portal_Death=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_Portal_Death, EVENT_PLAYER_UNIT_DEATH)
    TriggerAddCondition(gg_trg_Portal_Death, Condition(Trig_Portal_Death_Conditions))
    TriggerAddAction(gg_trg_Portal_Death, Trig_Portal_Death_Actions)
end
--===========================================================================
-- Trigger: Portal Missile Order
--
-- This prevents killable missiles from deviating from their path since they may only deposit units at the sister portal.
-- Selectable missiles that use thier own movement to go to sister portals should have the Ward classification.
--===========================================================================
function Trig_Portal_Missile_Order_Conditions()
    return IsUnitInGroup(GetTriggerUnit(), udg_Portal_teleMissiles)
end
function Trig_Portal_Missile_Order_Actions()
    DisableTrigger(GetTriggeringTrigger())
    udg_Portal_INDEX_CASTER=GetUnitUserData(GetTriggerUnit())
    udg_Portal_loc1=GetUnitLoc(udg_Portal_portal[udg_Portal_INDEX_CASTER])
    IssuePointOrderLocBJ(GetTriggerUnit(), "move", udg_Portal_loc1)
    RemoveLocation(udg_Portal_loc1)
    EnableTrigger(GetTriggeringTrigger())
end
--===========================================================================
function InitTrig_Portal_Missile_Order()
    gg_trg_Portal_Missile_Order=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_Portal_Missile_Order, EVENT_PLAYER_UNIT_ISSUED_TARGET_ORDER)
    TriggerRegisterAnyUnitEventBJ(gg_trg_Portal_Missile_Order, EVENT_PLAYER_UNIT_ISSUED_POINT_ORDER)
    TriggerRegisterAnyUnitEventBJ(gg_trg_Portal_Missile_Order, EVENT_PLAYER_UNIT_ISSUED_ORDER)
    TriggerAddCondition(gg_trg_Portal_Missile_Order, Condition(Trig_Portal_Missile_Order_Conditions))
    TriggerAddAction(gg_trg_Portal_Missile_Order, Trig_Portal_Missile_Order_Actions)
end
--===========================================================================
-- Trigger: Portal Disconnect
--
-- Copy the Sever Connection ability and then this if you intend to make Portals able to disconnect from one another with a no-target spell. Otherwise you may skip this trigger.
-- Add your various connector spells to the -------- Or - Any (Conditions) are true -------- to give your Portals the Sever Connection spell.
--===========================================================================
function Trig_Portal_Disconnect_Conditions()
    return udg_Portal_active[GetUnitUserData(GetTriggerUnit())]
end
function Trig_Portal_Disconnect_Func001Func005Func004C()
    return ( GetTriggerUnit() == udg_Portal_targeted[udg_Portal_INDEX_TRAVELLER] )
end
function Trig_Portal_Disconnect_Func001Func005Func005C()
    return ( udg_Portal_portal[udg_Portal_INDEX_CASTER] == udg_Portal_targeted[udg_Portal_INDEX_TRAVELLER] )
end
function Trig_Portal_Disconnect_Func001Func005A()
    udg_Portal_traveller=GetEnumUnit()
    udg_Portal_INDEX_TRAVELLER=GetUnitUserData(udg_Portal_traveller)
    UnitRemoveAbilityBJ(udg_Portal_delayFXAbil[udg_Portal_INDEX_CASTER], udg_Portal_traveller)
    if ( Trig_Portal_Disconnect_Func001Func005Func004C() ) then
        udg_Portal_targeted[udg_Portal_INDEX_TRAVELLER]=nil
        udg_Portal_delay[udg_Portal_INDEX_TRAVELLER]=0.00
        udg_Portal_isTeleporting[udg_Portal_INDEX_TRAVELLER]=false
        GroupRemoveUnitSimple(udg_Portal_traveller, udg_Portal_group)
    end
    if ( Trig_Portal_Disconnect_Func001Func005Func005C() ) then
        udg_Portal_targeted[udg_Portal_INDEX_TRAVELLER]=nil
        udg_Portal_delay[udg_Portal_INDEX_TRAVELLER]=0.00
        udg_Portal_isTeleporting[udg_Portal_INDEX_TRAVELLER]=false
        GroupRemoveUnitSimple(udg_Portal_traveller, udg_Portal_group)
    end
end
function Trig_Portal_Disconnect_Func001C()
    return ( GetSpellAbilityId() == udg_Portal_SeverAbility )
end
function Trig_Portal_Disconnect_Actions()
    if ( Trig_Portal_Disconnect_Func001C() ) then
        udg_Portal_INDEX_CASTER=GetUnitUserData(GetTriggerUnit())
        udg_Portal_INDEX_TARGET=GetUnitUserData(udg_Portal_portal[udg_Portal_INDEX_CASTER])
        UnitRemoveAbilityBJ(udg_Portal_SeverAbility, GetTriggerUnit())
        UnitRemoveAbilityBJ(udg_Portal_SeverAbility, udg_Portal_portal[udg_Portal_INDEX_CASTER])
        ForGroupBJ(udg_Portal_group, Trig_Portal_Disconnect_Func001Func005A)
        udg_Portal_active[udg_Portal_INDEX_CASTER]=false
        udg_Portal_active[udg_Portal_INDEX_TARGET]=false
        DestroyEffectBJ(udg_Portal_FX[udg_Portal_INDEX_CASTER])
        DestroyEffectBJ(udg_Portal_FX[udg_Portal_INDEX_TARGET])
        udg_Portal_portal[udg_Portal_INDEX_CASTER]=nil
        udg_Portal_portal[udg_Portal_INDEX_TARGET]=nil
    end
end
--===========================================================================
function InitTrig_Portal_Disconnect()
    gg_trg_Portal_Disconnect=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_Portal_Disconnect, EVENT_PLAYER_UNIT_SPELL_EFFECT)
    TriggerAddCondition(gg_trg_Portal_Disconnect, Condition(Trig_Portal_Disconnect_Conditions))
    TriggerAddAction(gg_trg_Portal_Disconnect, Trig_Portal_Disconnect_Actions)
end
--===========================================================================
-- Trigger: Connect Portal 2
--
-- No Missile, No Delays
--===========================================================================
function Trig_Connect_Portal_2_Func001Func003Func002C()
    return ( GetTriggerUnit() == udg_Portal_portal[udg_Portal_INDEX_TARGET] )
end
function Trig_Connect_Portal_2_Func001Func003C()
    return udg_Portal_active[udg_Portal_INDEX_TARGET] and (( GetSpellTargetUnit() ~= udg_Portal_portal[udg_Portal_INDEX_CASTER] ))
end
function Trig_Connect_Portal_2_Func001C()
    return ( GetUnitTypeId(GetSpellTargetUnit()) == GetUnitTypeId(GetTriggerUnit()) )
end
function Trig_Connect_Portal_2_Actions()
    if ( Trig_Connect_Portal_2_Func001C() ) then
        udg_Portal_INDEX_CASTER=GetUnitUserData(GetTriggerUnit())
        udg_Portal_INDEX_TARGET=GetUnitUserData(GetSpellTargetUnit())
        if ( Trig_Connect_Portal_2_Func001Func003C() ) then
            DisplayTimedTextToForce(GetForceOfPlayer(GetOwningPlayer(GetTriggerUnit())), 10.00, "TRIGSTR_19222")
        else
            if ( Trig_Connect_Portal_2_Func001Func003Func002C() ) then
                DisplayTimedTextToForce(GetForceOfPlayer(GetOwningPlayer(GetTriggerUnit())), 10.00, "TRIGSTR_19228")
            else
                udg_Portal_ConfigIndex[1]=udg_Portal_INDEX_CASTER
                udg_Portal_ConfigIndex[2]=udg_Portal_INDEX_TARGET
                for bj_forLoopAIndex = 1, 2 do
                    -- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- --------
                    -- CONFIGURE HERE
                    -- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- --------
                    udg_Portal_departureFX[udg_Portal_ConfigIndex[GetForLoopIndexA()]]="AbilitiesSpellsHumanMassTeleportMassTeleportCaster.mdl"
                    udg_Portal_arrivalFX[udg_Portal_ConfigIndex[GetForLoopIndexA()]]="AbilitiesSpellsHumanMassTeleportMassTeleportTarget.mdl"
                    udg_Portal_activeFX[udg_Portal_ConfigIndex[GetForLoopIndexA()]]="AbilitiesSpellsOrcVoodooVoodooAura.mdl"
                    udg_Portal_range[udg_Portal_ConfigIndex[GetForLoopIndexA()]]=180.00
                    udg_Portal_delay[udg_Portal_ConfigIndex[GetForLoopIndexA()]]=0.00
                    udg_Portal_missileSpeed[udg_Portal_ConfigIndex[GetForLoopIndexA()]]=0.00
                    udg_Portal_preventAllies[udg_Portal_ConfigIndex[GetForLoopIndexA()]]=false
                    -- The value below here dont matter since the delay and missileSpeed are both 0
                    udg_Portal_missileHeight[udg_Portal_ConfigIndex[GetForLoopIndexA()]]=0.00
                    udg_Portal_missileTargetable[udg_Portal_ConfigIndex[GetForLoopIndexA()]]=false
                    udg_Portal_missileUseOwnMovement[udg_Portal_ConfigIndex[GetForLoopIndexA()]]=false
                    -- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- --------
                    -- //END CONFIGURATION
                    -- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- --------
                end
                udg_Portal_INDEX_CASTER=udg_Portal_ConfigIndex[1]
                udg_Portal_INDEX_TARGET=udg_Portal_ConfigIndex[2]
                -- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- --------
                TriggerExecute(gg_trg_Portal_Connect)
            end
        end
    else
        DisplayTimedTextToForce(GetForceOfPlayer(GetOwningPlayer(GetTriggerUnit())), 10.00, "TRIGSTR_19244")
    end
end
--===========================================================================
function InitTrig_Connect_Portal_2()
    gg_trg_Connect_Portal_2=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_Connect_Portal_2, EVENT_PLAYER_UNIT_SPELL_EFFECT)
    TriggerAddAction(gg_trg_Connect_Portal_2, function()
        if GetSpellAbilityId() ~= FourCC('A0TQ') then return end
        Trig_Connect_Portal_2_Actions()
    end)
end
--===========================================================================
-- Trigger: F2
--===========================================================================
function Trig_F2_Func002A()
    IssuePointOrderLocBJ(GetEnumUnit(), "attack", udg_LocalPosition3)
end
function Trig_F2_Actions()
    udg_LocalPosition3=GetSpellTargetLoc()
    ForGroupBJ(udg_F_Group[GetConvertedPlayerId(GetOwningPlayer(GetTriggerUnit()))], Trig_F2_Func002A)
    RemoveLocation(udg_LocalPosition3)
end
--===========================================================================
function InitTrig_F2()
    gg_trg_F2=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_F2, EVENT_PLAYER_UNIT_SPELL_EFFECT)
    TriggerAddAction(gg_trg_F2, function()
        if GetSpellAbilityId() ~= FourCC('A0IX') then return end
        Trig_F2_Actions()
    end)
end
--===========================================================================
-- Trigger: F2 2
--===========================================================================
function Trig_F2_2_Actions()
    local pi= GetPlayerId(GetOwningPlayer(GetTriggerUnit()))
    local g= CreateGroup()
    local g0= CreateGroup()
    local u
    local i= 0
    local loc= GetSpellTargetLoc()
    
    --set g = udg_F_Group[pi+1]
    GroupAddGroup(udg_F_Group[pi + 1], g)
    while true do
    
        u=FirstOfGroup(g)
        if u == nil then
            GroupPointOrderLoc(g0, "attack", loc)
            if true then break end
        end
             
        if i == 12 then
            GroupPointOrderLoc(g0, "attack", loc)
            i=0
            GroupClear(g0)
        
        end
        i=i + 1
        GroupAddUnit(g0, u)
        GroupRemoveUnit(g, u)
        u=nil
    end
    DestroyGroup(g)
    DestroyGroup(g0)
    g=nil
    g0=nil
    RemoveLocation(loc)
    loc=nil
end
--===========================================================================
function InitTrig_F2_2()
    gg_trg_F2_2=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_F2_2, EVENT_PLAYER_UNIT_SPELL_EFFECT)
    TriggerAddAction(gg_trg_F2_2, function()
        if GetSpellAbilityId() ~= FourCC('A167') then return end
        Trig_F2_2_Actions()
    end)
end
--===========================================================================
-- Trigger: F2 Attack Point
--
-- ??? ???? ????? ????????? ????????? ?????
--===========================================================================
function OwnUnit()
    return GetOwningPlayer(GetFilterUnit()) == udg_LocalPlayer
end
function IsCityEnemy()
    return GetUnitAbilityLevel(GetFilterUnit(), FourCC('AHad')) >= 0 and GetOwningPlayer(GetFilterUnit()) ~= udg_LocalPlayer
end
function Trig_F2_Attack_Point_Actions()
    local pi= GetPlayerId(GetOwningPlayer(GetTriggerUnit()))
    local g= CreateGroup()
    local points= CreateGroup()
    local g0= CreateGroup()
    local u
    local u2
    local i= 0
    local x
    local y
    --set g = udg_F_Group[pi+1]
    GroupAddGroup(udg_F_Group[pi + 1], g)
    udg_LocalPlayer=GetOwningPlayer(GetTriggerUnit())
    while true do
    
        u=FirstOfGroup(g)
        if u == nil or i >= 25 then break end
        
        x=GetUnitX(u)
        y=GetUnitY(u)
        
        GroupEnumUnitsInRange(g0, x, y, 500, OwnUnit)
        GroupEnumUnitsInRange(points, x, y, 7500, IsCityEnemy)
        if FirstOfGroup(points) ~= nil then
            u2=BlzGroupUnitAt(points, GetRandomInt(0, BlzGroupGetSize(points) - 1))
            GroupPointOrder(g0, "attack", GetUnitX(u2), GetUnitY(u2))
                
        end
        GroupRemoveGroup(g, g0)
        GroupClear(g0)
        GroupRemoveUnit(g, u)
        u=nil
        i=i + 1
    end
    
    DestroyGroup(g)
    DestroyGroup(g0)
    DestroyGroup(points)
    g=nil
    g0=nil
    points=nil
    
    u=nil
    u2=nil
end
--===========================================================================
function InitTrig_F2_Attack_Point()
    gg_trg_F2_Attack_Point=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_F2_Attack_Point, EVENT_PLAYER_UNIT_SPELL_EFFECT)
    TriggerAddAction(gg_trg_F2_Attack_Point, function()
        if GetSpellAbilityId() ~= FourCC('A1L0') then return end
        Trig_F2_Attack_Point_Actions()
    end)
end
--===========================================================================
-- Trigger: F2 Start
--===========================================================================
function Trig_F2_Start_Conditions()
    return ( CountLivingPlayerUnitsOfTypeId(FourCC('h0GR'), GetTriggerPlayer()) == 0 )
end
function Trig_F2_Start_Actions()
    udg_LocalPosition2=GetRectCenter(gg_rct_HostRegion)
    ClearSelectionForPlayer(GetTriggerPlayer())
    CreateNUnitsAtLoc(1, FourCC('h0GR'), GetTriggerPlayer(), udg_LocalPosition2, bj_UNIT_FACING)
    SelectUnitAddForPlayer(GetLastCreatedUnit(), GetTriggerPlayer())
end
--===========================================================================
function InitTrig_F2_Start()
    gg_trg_F2_Start=CreateTrigger()
    TriggerRegisterPlayerChatEvent(gg_trg_F2_Start, Player(0), " - f2", true)
    TriggerRegisterPlayerChatEvent(gg_trg_F2_Start, Player(1), " - f2", true)
    TriggerRegisterPlayerChatEvent(gg_trg_F2_Start, Player(2), " - f2", true)
    TriggerRegisterPlayerChatEvent(gg_trg_F2_Start, Player(3), " - f2", true)
    TriggerRegisterPlayerChatEvent(gg_trg_F2_Start, Player(4), " - f2", true)
    TriggerRegisterPlayerChatEvent(gg_trg_F2_Start, Player(5), " - f2", true)
    TriggerRegisterPlayerChatEvent(gg_trg_F2_Start, Player(6), " - f2", true)
    TriggerRegisterPlayerChatEvent(gg_trg_F2_Start, Player(7), " - f2", true)
    TriggerRegisterPlayerChatEvent(gg_trg_F2_Start, Player(8), " - f2", true)
    TriggerRegisterPlayerChatEvent(gg_trg_F2_Start, Player(9), " - f2", true)
    TriggerRegisterPlayerChatEvent(gg_trg_F2_Start, Player(10), " - f2", true)
    TriggerRegisterPlayerChatEvent(gg_trg_F2_Start, Player(11), " - f2", true)
    TriggerRegisterPlayerChatEvent(gg_trg_F2_Start, Player(12), " - f2", true)
    TriggerRegisterPlayerChatEvent(gg_trg_F2_Start, Player(13), " - f2", true)
    TriggerRegisterPlayerChatEvent(gg_trg_F2_Start, Player(14), " - f2", true)
    TriggerRegisterPlayerChatEvent(gg_trg_F2_Start, Player(15), " - f2", true)
    TriggerRegisterPlayerChatEvent(gg_trg_F2_Start, Player(16), " - f2", true)
    TriggerRegisterPlayerChatEvent(gg_trg_F2_Start, Player(17), " - f2", true)
    TriggerRegisterPlayerChatEvent(gg_trg_F2_Start, Player(18), " - f2", true)
    TriggerRegisterPlayerChatEvent(gg_trg_F2_Start, Player(19), " - f2", true)
    TriggerRegisterPlayerChatEvent(gg_trg_F2_Start, Player(20), " - f2", true)
    TriggerRegisterPlayerChatEvent(gg_trg_F2_Start, Player(21), " - f2", true)
    TriggerRegisterPlayerChatEvent(gg_trg_F2_Start, Player(22), " - f2", true)
    TriggerRegisterPlayerChatEvent(gg_trg_F2_Start, Player(23), " - f2", true)
    TriggerAddCondition(gg_trg_F2_Start, Condition(Trig_F2_Start_Conditions))
    TriggerAddAction(gg_trg_F2_Start, Trig_F2_Start_Actions)
end
--===========================================================================
-- Trigger: F2 Map 2
--===========================================================================
--
--function Trig_F2_Map_2_Func001002001 takes nothing returns boolean
--    return ( IsUnitType(GetFilterUnit(), UNIT_TYPE_STRUCTURE) != true )
--endfunction
--
--function Trig_F2_Map_2_Func001002002001 takes nothing returns boolean
--    return ( IsUnitType(GetFilterUnit(), UNIT_TYPE_HERO) != true )
--endfunction
--
--function Trig_F2_Map_2_Func001002002002001 takes nothing returns boolean
--    return ( GetUnitAbilityLevelSwapped('A001', GetFilterUnit()) == 0 )
--endfunction
--
--function Trig_F2_Map_2_Func001002002002002001 takes nothing returns boolean
--    return ( GetUnitAbilityLevelSwapped('Slo3', GetFilterUnit()) == 0 )
--endfunction
--
--function Trig_F2_Map_2_Func001002002002002002001 takes nothing returns boolean
--    return ( GetUnitAbilityLevelSwapped('ANha', GetFilterUnit()) == 0 )
--endfunction
--
--function Trig_F2_Map_2_Func001002002002002002002001 takes nothing returns boolean
--    return ( GetOwningPlayer(GetTriggerUnit()) == GetOwningPlayer(GetFilterUnit()) )
--endfunction
--
--function Trig_F2_Map_2_Func001002002002002002002002001 takes nothing returns boolean
--    return ( GetUnitAbilityLevelSwapped('Awha', GetFilterUnit()) == 0 )
--endfunction
--
--function Trig_F2_Map_2_Func001002002002002002002002002 takes nothing returns boolean
--    return ( 1 == 1 )
--endfunction
--
--function Trig_F2_Map_2_Func001002002002002002002002 takes nothing returns boolean
--    return GetBooleanAnd( Trig_F2_Map_2_Func001002002002002002002002001(), Trig_F2_Map_2_Func001002002002002002002002002() )
--endfunction
--
--function Trig_F2_Map_2_Func001002002002002002002 takes nothing returns boolean
--    return GetBooleanAnd( Trig_F2_Map_2_Func001002002002002002002001(), Trig_F2_Map_2_Func001002002002002002002002() )
--endfunction
--
--function Trig_F2_Map_2_Func001002002002002002 takes nothing returns boolean
--    return GetBooleanAnd( Trig_F2_Map_2_Func001002002002002002001(), Trig_F2_Map_2_Func001002002002002002002() )
--endfunction
--
--function Trig_F2_Map_2_Func001002002002002 takes nothing returns boolean
--    return GetBooleanAnd( Trig_F2_Map_2_Func001002002002002001(), Trig_F2_Map_2_Func001002002002002002() )
--endfunction
--
--function Trig_F2_Map_2_Func001002002002 takes nothing returns boolean
--    return GetBooleanAnd( Trig_F2_Map_2_Func001002002002001(), Trig_F2_Map_2_Func001002002002002() )
--endfunction
--
--function Trig_F2_Map_2_Func001002002 takes nothing returns boolean
--    return GetBooleanAnd( Trig_F2_Map_2_Func001002002001(), Trig_F2_Map_2_Func001002002002() )
--endfunction
--
--function Trig_F2_Map_2_Func001002 takes nothing returns boolean
--    return GetBooleanAnd( Trig_F2_Map_2_Func001002001(), Trig_F2_Map_2_Func001002002() )
--endfunction
--
--function Trig_F2_Map_2_Func003001002 takes nothing returns boolean
--    return ( GetUnitAbilityLevelSwapped('ANha', GetFilterUnit()) == 1 )
--endfunction
--
--function Trig_F2_Map_2_Func004001002 takes nothing returns boolean
--    return ( GetUnitAbilityLevelSwapped('Ahar', GetFilterUnit()) == 1 )
--endfunction
--
--function Trig_F2_Map_2_Func005001002 takes nothing returns boolean
--    return ( GetUnitAbilityLevelSwapped('A0OY', GetFilterUnit()) == 1 )
--endfunction
--
--function Trig_F2_Map_2_Func006001002 takes nothing returns boolean
--    return ( GetUnitAbilityLevelSwapped('A0MJ', GetFilterUnit()) == 1 )
--endfunction
--
--function Trig_F2_Map_2_Func007001002 takes nothing returns boolean
--    return ( GetUnitAbilityLevelSwapped('A09P', GetFilterUnit()) == 1 )
--endfunction
--
--function Trig_F2_Map_2_Func008001002 takes nothing returns boolean
--    return ( GetUnitAbilityLevelSwapped('Awha', GetFilterUnit()) == 1 )
--endfunction
--
--function Trig_F2_Map_2_Func009001002 takes nothing returns boolean
--    return ( GetUnitAbilityLevelSwapped('Awh2', GetFilterUnit()) == 1 )
--endfunction
--
--function Trig_F2_Map_2_Func010001002 takes nothing returns boolean
--    return ( GetUnitAbilityLevelSwapped('A0SJ', GetFilterUnit()) == 1 )
--endfunction
--
--function Trig_F2_Map_2_Func011001002 takes nothing returns boolean
--    return ( GetUnitTypeId(GetFilterUnit()) == 'e01R' )
--endfunction
--
--function Trig_F2_Map_2_Func012001002 takes nothing returns boolean
--    return ( GetUnitTypeId(GetFilterUnit()) == 'h07A' )
--endfunction
--
--function Trig_F2_Map_2_Func013001002 takes nothing returns boolean
--    return ( GetUnitAbilityLevelSwapped('Ahar', GetFilterUnit()) == 1 )
--endfunction
--
--function Trig_F2_Map_2_Func014001002 takes nothing returns boolean
--    return ( GetUnitAbilityLevelSwapped('Ahr3', GetFilterUnit()) == 1 )
--endfunction
--
--function Trig_F2_Map_2_Func015001002 takes nothing returns boolean
--    return ( GetUnitAbilityLevelSwapped('A0VY', GetFilterUnit()) == 1 )
--endfunction
--
--function Trig_F2_Map_2_Func016001002 takes nothing returns boolean
--    return ( GetUnitAbilityLevelSwapped('A0SJ', GetFilterUnit()) == 2 )
--endfunction
--
--function Trig_F2_Map_2_Func017001002 takes nothing returns boolean
--    return ( GetUnitAbilityLevelSwapped('A0VZ', GetFilterUnit()) == 1 )
--endfunction
--
function F2_targets()
    return GetUnitCurrentOrder(GetFilterUnit()) ~= OrderId("harvest") and not IsUnitType(GetFilterUnit(), UNIT_TYPE_PEON) and GetUnitTypeId(GetFilterUnit()) ~= FourCC('h07A') and GetOwningPlayer(GetFilterUnit()) == udg_LocalPlayer
end
function Trig_F2_Map_2_Actions()
    udg_LocalPlayer=GetOwningPlayer(GetTriggerUnit())
    --set udg_Boolexpr = Condition(function Trig_F2_Map_2_Func001002)
    GroupEnumUnitsInRect(udg_LocalOtrad2, GetPlayableMapRect(), F2_targets)
   
   
--   
--   call GroupRemoveGroup( GetUnitsOfPlayerMatching(GetOwningPlayer(GetTriggerUnit()), Condition(function Trig_F2_Map_2_Func003001002)), udg_LocalOtrad2 )
--    call GroupRemoveGroup( GetUnitsOfPlayerMatching(GetOwningPlayer(GetTriggerUnit()), Condition(function Trig_F2_Map_2_Func004001002)), udg_LocalOtrad2 )
--    call GroupRemoveGroup( GetUnitsOfPlayerMatching(GetOwningPlayer(GetTriggerUnit()), Condition(function Trig_F2_Map_2_Func005001002)), udg_LocalOtrad2 )
--    call GroupRemoveGroup( GetUnitsOfPlayerMatching(GetOwningPlayer(GetTriggerUnit()), Condition(function Trig_F2_Map_2_Func006001002)), udg_LocalOtrad2 )
--    call GroupRemoveGroup( GetUnitsOfPlayerMatching(GetOwningPlayer(GetTriggerUnit()), Condition(function Trig_F2_Map_2_Func007001002)), udg_LocalOtrad2 )
--    call GroupRemoveGroup( GetUnitsOfPlayerMatching(GetOwningPlayer(GetTriggerUnit()), Condition(function Trig_F2_Map_2_Func008001002)), udg_LocalOtrad2 )
--    call GroupRemoveGroup( GetUnitsOfPlayerMatching(GetOwningPlayer(GetTriggerUnit()), Condition(function Trig_F2_Map_2_Func009001002)), udg_LocalOtrad2 )
--    call GroupRemoveGroup( GetUnitsOfPlayerMatching(GetOwningPlayer(GetTriggerUnit()), Condition(function Trig_F2_Map_2_Func010001002)), udg_LocalOtrad2 )
--    call GroupRemoveGroup( GetUnitsOfPlayerMatching(GetOwningPlayer(GetTriggerUnit()), Condition(function Trig_F2_Map_2_Func011001002)), udg_LocalOtrad2 )
--    call GroupRemoveGroup( GetUnitsOfPlayerMatching(GetOwningPlayer(GetTriggerUnit()), Condition(function Trig_F2_Map_2_Func012001002)), udg_LocalOtrad2 )
--    call GroupRemoveGroup( GetUnitsOfPlayerMatching(GetOwningPlayer(GetTriggerUnit()), Condition(function Trig_F2_Map_2_Func013001002)), udg_LocalOtrad2 )
--    call GroupRemoveGroup( GetUnitsOfPlayerMatching(GetOwningPlayer(GetTriggerUnit()), Condition(function Trig_F2_Map_2_Func014001002)), udg_LocalOtrad2 )
--    call GroupRemoveGroup( GetUnitsOfPlayerMatching(GetOwningPlayer(GetTriggerUnit()), Condition(function Trig_F2_Map_2_Func015001002)), udg_LocalOtrad2 )
--    call GroupRemoveGroup( GetUnitsOfPlayerMatching(GetOwningPlayer(GetTriggerUnit()), Condition(function Trig_F2_Map_2_Func016001002)), udg_LocalOtrad2 )
--    call GroupRemoveGroup( GetUnitsOfPlayerMatching(GetOwningPlayer(GetTriggerUnit()), Condition(function Trig_F2_Map_2_Func017001002)), udg_LocalOtrad2 )
    udg_F_Group[GetConvertedPlayerId(GetOwningPlayer(GetTriggerUnit()))]=udg_LocalOtrad2
end
--===========================================================================
function InitTrig_F2_Map_2()
    gg_trg_F2_Map_2=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_F2_Map_2, EVENT_PLAYER_UNIT_SPELL_FINISH)
    TriggerAddAction(gg_trg_F2_Map_2, function()
        if GetSpellAbilityId() ~= FourCC('A0V2') then return end
        Trig_F2_Map_2_Actions()
    end)
end
--===========================================================================
-- Trigger: F2 AreaMidBig
--===========================================================================
--
--function Trig_F2_AreaMidBig_Func002002001 takes nothing returns boolean
--    return ( IsUnitType(GetFilterUnit(), UNIT_TYPE_STRUCTURE) != true )
--endfunction
--
--function Trig_F2_AreaMidBig_Func002002002001 takes nothing returns boolean
--    return ( IsUnitType(GetFilterUnit(), UNIT_TYPE_HERO) != true )
--endfunction
--
--function Trig_F2_AreaMidBig_Func002002002002001 takes nothing returns boolean
--    return ( GetUnitAbilityLevelSwapped('A001', GetFilterUnit()) == 0 )
--endfunction
--
--function Trig_F2_AreaMidBig_Func002002002002002001 takes nothing returns boolean
--    return ( GetUnitAbilityLevelSwapped('Slo3', GetFilterUnit()) == 0 )
--endfunction
--
--function Trig_F2_AreaMidBig_Func002002002002002002001 takes nothing returns boolean
--    return ( GetUnitAbilityLevelSwapped('ANha', GetFilterUnit()) == 0 )
--endfunction
--
--function Trig_F2_AreaMidBig_Func002002002002002002002001 takes nothing returns boolean
--    return ( GetOwningPlayer(GetTriggerUnit()) == GetOwningPlayer(GetFilterUnit()) )
--endfunction
--
--function Trig_F2_AreaMidBig_Func002002002002002002002002001 takes nothing returns boolean
--    return ( GetUnitAbilityLevelSwapped('Awha', GetFilterUnit()) == 0 )
--endfunction
--
--function Trig_F2_AreaMidBig_Func002002002002002002002002002 takes nothing returns boolean
--    return ( 1 == 1 )
--endfunction
--
--function Trig_F2_AreaMidBig_Func002002002002002002002002 takes nothing returns boolean
--    return GetBooleanAnd( Trig_F2_AreaMidBig_Func002002002002002002002002001(), Trig_F2_AreaMidBig_Func002002002002002002002002002() )
--endfunction
--
--function Trig_F2_AreaMidBig_Func002002002002002002002 takes nothing returns boolean
--    return GetBooleanAnd( Trig_F2_AreaMidBig_Func002002002002002002002001(), Trig_F2_AreaMidBig_Func002002002002002002002002() )
--endfunction
--
--function Trig_F2_AreaMidBig_Func002002002002002002 takes nothing returns boolean
--    return GetBooleanAnd( Trig_F2_AreaMidBig_Func002002002002002002001(), Trig_F2_AreaMidBig_Func002002002002002002002() )
--endfunction
--
--function Trig_F2_AreaMidBig_Func002002002002002 takes nothing returns boolean
--    return GetBooleanAnd( Trig_F2_AreaMidBig_Func002002002002002001(), Trig_F2_AreaMidBig_Func002002002002002002() )
--endfunction
--
--function Trig_F2_AreaMidBig_Func002002002002 takes nothing returns boolean
--    return GetBooleanAnd( Trig_F2_AreaMidBig_Func002002002002001(), Trig_F2_AreaMidBig_Func002002002002002() )
--endfunction
--
--function Trig_F2_AreaMidBig_Func002002002 takes nothing returns boolean
--    return GetBooleanAnd( Trig_F2_AreaMidBig_Func002002002001(), Trig_F2_AreaMidBig_Func002002002002() )
--endfunction
--
--function Trig_F2_AreaMidBig_Func002002 takes nothing returns boolean
--    return GetBooleanAnd( Trig_F2_AreaMidBig_Func002002001(), Trig_F2_AreaMidBig_Func002002002() )
--endfunction
--
--function Trig_F2_AreaMidBig_Func004001002 takes nothing returns boolean
--    return ( GetUnitAbilityLevelSwapped('ANha', GetFilterUnit()) == 1 )
--endfunction
--
--function Trig_F2_AreaMidBig_Func005001002 takes nothing returns boolean
--    return ( GetUnitAbilityLevelSwapped('A0OY', GetFilterUnit()) == 1 )
--endfunction
--
--function Trig_F2_AreaMidBig_Func006001002 takes nothing returns boolean
--    return ( GetUnitAbilityLevelSwapped('A0MJ', GetFilterUnit()) == 1 )
--endfunction
--
--function Trig_F2_AreaMidBig_Func007001002 takes nothing returns boolean
--    return ( GetUnitAbilityLevelSwapped('A09P', GetFilterUnit()) == 1 )
--endfunction
--
--function Trig_F2_AreaMidBig_Func008001002 takes nothing returns boolean
--    return ( GetUnitAbilityLevelSwapped('Awha', GetFilterUnit()) == 1 )
--endfunction
--
--function Trig_F2_AreaMidBig_Func009001002 takes nothing returns boolean
--    return ( GetUnitAbilityLevelSwapped('Awh2', GetFilterUnit()) == 1 )
--endfunction
--
--function Trig_F2_AreaMidBig_Func010001002 takes nothing returns boolean
--    return ( GetUnitAbilityLevelSwapped('A0SJ', GetFilterUnit()) == 1 )
--endfunction
--
--function Trig_F2_AreaMidBig_Func011001002 takes nothing returns boolean
--    return ( GetUnitTypeId(GetFilterUnit()) == 'e01R' )
--endfunction
--
--function Trig_F2_AreaMidBig_Func012001002 takes nothing returns boolean
--    return ( GetUnitTypeId(GetFilterUnit()) == 'h07A' )
--endfunction
--
--function Trig_F2_AreaMidBig_Func013001002 takes nothing returns boolean
--    return ( GetUnitAbilityLevelSwapped('Ahar', GetFilterUnit()) == 1 )
--endfunction
--
--function Trig_F2_AreaMidBig_Func014001002 takes nothing returns boolean
--    return ( GetUnitAbilityLevelSwapped('Ahr3', GetFilterUnit()) == 1 )
--endfunction
--
--function Trig_F2_AreaMidBig_Func015001002 takes nothing returns boolean
--    return ( GetUnitAbilityLevelSwapped('A0VY', GetFilterUnit()) == 1 )
--endfunction
--
--function Trig_F2_AreaMidBig_Func016001002 takes nothing returns boolean
--    return ( GetUnitAbilityLevelSwapped('A0SJ', GetFilterUnit()) == 2 )
--endfunction
--
--function Trig_F2_AreaMidBig_Func017001002 takes nothing returns boolean
--    return ( GetUnitAbilityLevelSwapped('A0VZ', GetFilterUnit()) == 1 )
--endfunction
function Trig_F2_AreaMidBig_Actions()
    udg_LocalPlayer=GetOwningPlayer(GetTriggerUnit())
    --set udg_Boolexpr = Condition(function Trig_F2_AreaMidBig_Func002002)
    GroupEnumUnitsInRange(udg_LocalOtrad2, GetSpellTargetX(), GetSpellTargetY(), 2500, F2_targets)
--    call GroupRemoveGroup( GetUnitsOfPlayerMatching(GetOwningPlayer(GetTriggerUnit()), Condition(function Trig_F2_AreaMidBig_Func004001002)), udg_LocalOtrad2 )
--    call GroupRemoveGroup( GetUnitsOfPlayerMatching(GetOwningPlayer(GetTriggerUnit()), Condition(function Trig_F2_AreaMidBig_Func005001002)), udg_LocalOtrad2 )
--    call GroupRemoveGroup( GetUnitsOfPlayerMatching(GetOwningPlayer(GetTriggerUnit()), Condition(function Trig_F2_AreaMidBig_Func006001002)), udg_LocalOtrad2 )
--    call GroupRemoveGroup( GetUnitsOfPlayerMatching(GetOwningPlayer(GetTriggerUnit()), Condition(function Trig_F2_AreaMidBig_Func007001002)), udg_LocalOtrad2 )
--    call GroupRemoveGroup( GetUnitsOfPlayerMatching(GetOwningPlayer(GetTriggerUnit()), Condition(function Trig_F2_AreaMidBig_Func008001002)), udg_LocalOtrad2 )
--    call GroupRemoveGroup( GetUnitsOfPlayerMatching(GetOwningPlayer(GetTriggerUnit()), Condition(function Trig_F2_AreaMidBig_Func009001002)), udg_LocalOtrad2 )
--    call GroupRemoveGroup( GetUnitsOfPlayerMatching(GetOwningPlayer(GetTriggerUnit()), Condition(function Trig_F2_AreaMidBig_Func010001002)), udg_LocalOtrad2 )
--    call GroupRemoveGroup( GetUnitsOfPlayerMatching(GetOwningPlayer(GetTriggerUnit()), Condition(function Trig_F2_AreaMidBig_Func011001002)), udg_LocalOtrad2 )
--    call GroupRemoveGroup( GetUnitsOfPlayerMatching(GetOwningPlayer(GetTriggerUnit()), Condition(function Trig_F2_AreaMidBig_Func012001002)), udg_LocalOtrad2 )
--    call GroupRemoveGroup( GetUnitsOfPlayerMatching(GetOwningPlayer(GetTriggerUnit()), Condition(function Trig_F2_AreaMidBig_Func013001002)), udg_LocalOtrad2 )
--    call GroupRemoveGroup( GetUnitsOfPlayerMatching(GetOwningPlayer(GetTriggerUnit()), Condition(function Trig_F2_AreaMidBig_Func014001002)), udg_LocalOtrad2 )
--    call GroupRemoveGroup( GetUnitsOfPlayerMatching(GetOwningPlayer(GetTriggerUnit()), Condition(function Trig_F2_AreaMidBig_Func015001002)), udg_LocalOtrad2 )
--    call GroupRemoveGroup( GetUnitsOfPlayerMatching(GetOwningPlayer(GetTriggerUnit()), Condition(function Trig_F2_AreaMidBig_Func016001002)), udg_LocalOtrad2 )
--    call GroupRemoveGroup( GetUnitsOfPlayerMatching(GetOwningPlayer(GetTriggerUnit()), Condition(function Trig_F2_AreaMidBig_Func017001002)), udg_LocalOtrad2 )
    udg_F_Group[GetConvertedPlayerId(GetOwningPlayer(GetTriggerUnit()))]=udg_LocalOtrad2
end
--===========================================================================
function InitTrig_F2_AreaMidBig()
    gg_trg_F2_AreaMidBig=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_F2_AreaMidBig, EVENT_PLAYER_UNIT_SPELL_EFFECT)
    TriggerAddAction(gg_trg_F2_AreaMidBig, function()
        if GetSpellAbilityId() ~= FourCC('A0VK') then return end
        Trig_F2_AreaMidBig_Actions()
    end)
end
--===========================================================================
-- Trigger: F2 AreaMid
--===========================================================================
--
--function Trig_F2_AreaMid_Func002002001 takes nothing returns boolean
--    return ( IsUnitType(GetFilterUnit(), UNIT_TYPE_STRUCTURE) != true )
--endfunction
--
--function Trig_F2_AreaMid_Func002002002001 takes nothing returns boolean
--    return ( IsUnitType(GetFilterUnit(), UNIT_TYPE_HERO) != true )
--endfunction
--
--function Trig_F2_AreaMid_Func002002002002001 takes nothing returns boolean
--    return ( GetUnitAbilityLevelSwapped('A001', GetFilterUnit()) == 0 )
--endfunction
--
--function Trig_F2_AreaMid_Func002002002002002001 takes nothing returns boolean
--    return ( GetUnitAbilityLevelSwapped('Slo3', GetFilterUnit()) == 0 )
--endfunction
--
--function Trig_F2_AreaMid_Func002002002002002002001 takes nothing returns boolean
--    return ( GetUnitAbilityLevelSwapped('ANha', GetFilterUnit()) == 0 )
--endfunction
--
--function Trig_F2_AreaMid_Func002002002002002002002001 takes nothing returns boolean
--    return ( GetOwningPlayer(GetTriggerUnit()) == GetOwningPlayer(GetFilterUnit()) )
--endfunction
--
--function Trig_F2_AreaMid_Func002002002002002002002002001 takes nothing returns boolean
--    return ( GetUnitAbilityLevelSwapped('Awha', GetFilterUnit()) == 0 )
--endfunction
--
--function Trig_F2_AreaMid_Func002002002002002002002002002 takes nothing returns boolean
--    return ( 1 == 1 )
--endfunction
--
--function Trig_F2_AreaMid_Func002002002002002002002002 takes nothing returns boolean
--    return GetBooleanAnd( Trig_F2_AreaMid_Func002002002002002002002002001(), Trig_F2_AreaMid_Func002002002002002002002002002() )
--endfunction
--
--function Trig_F2_AreaMid_Func002002002002002002002 takes nothing returns boolean
--    return GetBooleanAnd( Trig_F2_AreaMid_Func002002002002002002002001(), Trig_F2_AreaMid_Func002002002002002002002002() )
--endfunction
--
--function Trig_F2_AreaMid_Func002002002002002002 takes nothing returns boolean
--    return GetBooleanAnd( Trig_F2_AreaMid_Func002002002002002002001(), Trig_F2_AreaMid_Func002002002002002002002() )
--endfunction
--
--function Trig_F2_AreaMid_Func002002002002002 takes nothing returns boolean
--    return GetBooleanAnd( Trig_F2_AreaMid_Func002002002002002001(), Trig_F2_AreaMid_Func002002002002002002() )
--endfunction
--
--function Trig_F2_AreaMid_Func002002002002 takes nothing returns boolean
--    return GetBooleanAnd( Trig_F2_AreaMid_Func002002002002001(), Trig_F2_AreaMid_Func002002002002002() )
--endfunction
--
--function Trig_F2_AreaMid_Func002002002 takes nothing returns boolean
--    return GetBooleanAnd( Trig_F2_AreaMid_Func002002002001(), Trig_F2_AreaMid_Func002002002002() )
--endfunction
--
--function Trig_F2_AreaMid_Func002002 takes nothing returns boolean
--    return GetBooleanAnd( Trig_F2_AreaMid_Func002002001(), Trig_F2_AreaMid_Func002002002() )
--endfunction
--
--function Trig_F2_AreaMid_Func004001002 takes nothing returns boolean
--    return ( GetUnitAbilityLevelSwapped('ANha', GetFilterUnit()) == 1 )
--endfunction
--
--function Trig_F2_AreaMid_Func005001002 takes nothing returns boolean
--    return ( GetUnitAbilityLevelSwapped('A0OY', GetFilterUnit()) == 1 )
--endfunction
--
--function Trig_F2_AreaMid_Func006001002 takes nothing returns boolean
--    return ( GetUnitAbilityLevelSwapped('A0MJ', GetFilterUnit()) == 1 )
--endfunction
--
--function Trig_F2_AreaMid_Func007001002 takes nothing returns boolean
--    return ( GetUnitAbilityLevelSwapped('A09P', GetFilterUnit()) == 1 )
--endfunction
--
--function Trig_F2_AreaMid_Func008001002 takes nothing returns boolean
--    return ( GetUnitAbilityLevelSwapped('Awha', GetFilterUnit()) == 1 )
--endfunction
--
--function Trig_F2_AreaMid_Func009001002 takes nothing returns boolean
--    return ( GetUnitAbilityLevelSwapped('Awh2', GetFilterUnit()) == 1 )
--endfunction
--
--function Trig_F2_AreaMid_Func010001002 takes nothing returns boolean
--    return ( GetUnitAbilityLevelSwapped('A0SJ', GetFilterUnit()) == 1 )
--endfunction
--
--function Trig_F2_AreaMid_Func011001002 takes nothing returns boolean
--    return ( GetUnitTypeId(GetFilterUnit()) == 'e01R' )
--endfunction
--
--function Trig_F2_AreaMid_Func012001002 takes nothing returns boolean
--    return ( GetUnitTypeId(GetFilterUnit()) == 'h07A' )
--endfunction
--
--function Trig_F2_AreaMid_Func013001002 takes nothing returns boolean
--    return ( GetUnitAbilityLevelSwapped('Ahar', GetFilterUnit()) == 1 )
--endfunction
--
--function Trig_F2_AreaMid_Func014001002 takes nothing returns boolean
--    return ( GetUnitAbilityLevelSwapped('Ahr3', GetFilterUnit()) == 1 )
--endfunction
--
--function Trig_F2_AreaMid_Func015001002 takes nothing returns boolean
--    return ( GetUnitAbilityLevelSwapped('A0VY', GetFilterUnit()) == 1 )
--endfunction
--
--function Trig_F2_AreaMid_Func016001002 takes nothing returns boolean
--    return ( GetUnitAbilityLevelSwapped('A0SJ', GetFilterUnit()) == 2 )
--endfunction
--
--function Trig_F2_AreaMid_Func017001002 takes nothing returns boolean
--    return ( GetUnitAbilityLevelSwapped('A0VZ', GetFilterUnit()) == 1 )
--endfunction
function Trig_F2_AreaMid_Actions()
    udg_LocalPlayer=GetOwningPlayer(GetTriggerUnit())
    GroupEnumUnitsInRange(udg_LocalOtrad2, GetSpellTargetX(), GetSpellTargetY(), 1000, F2_targets)
--    call GroupRemoveGroup( GetUnitsOfPlayerMatching(GetOwningPlayer(GetTriggerUnit()), Condition(function Trig_F2_AreaMid_Func004001002)), udg_LocalOtrad2 )
--    call GroupRemoveGroup( GetUnitsOfPlayerMatching(GetOwningPlayer(GetTriggerUnit()), Condition(function Trig_F2_AreaMid_Func005001002)), udg_LocalOtrad2 )
--    call GroupRemoveGroup( GetUnitsOfPlayerMatching(GetOwningPlayer(GetTriggerUnit()), Condition(function Trig_F2_AreaMid_Func006001002)), udg_LocalOtrad2 )
--    call GroupRemoveGroup( GetUnitsOfPlayerMatching(GetOwningPlayer(GetTriggerUnit()), Condition(function Trig_F2_AreaMid_Func007001002)), udg_LocalOtrad2 )
--    call GroupRemoveGroup( GetUnitsOfPlayerMatching(GetOwningPlayer(GetTriggerUnit()), Condition(function Trig_F2_AreaMid_Func008001002)), udg_LocalOtrad2 )
--    call GroupRemoveGroup( GetUnitsOfPlayerMatching(GetOwningPlayer(GetTriggerUnit()), Condition(function Trig_F2_AreaMid_Func009001002)), udg_LocalOtrad2 )
--    call GroupRemoveGroup( GetUnitsOfPlayerMatching(GetOwningPlayer(GetTriggerUnit()), Condition(function Trig_F2_AreaMid_Func010001002)), udg_LocalOtrad2 )
--    call GroupRemoveGroup( GetUnitsOfPlayerMatching(GetOwningPlayer(GetTriggerUnit()), Condition(function Trig_F2_AreaMid_Func011001002)), udg_LocalOtrad2 )
--    call GroupRemoveGroup( GetUnitsOfPlayerMatching(GetOwningPlayer(GetTriggerUnit()), Condition(function Trig_F2_AreaMid_Func012001002)), udg_LocalOtrad2 )
--    call GroupRemoveGroup( GetUnitsOfPlayerMatching(GetOwningPlayer(GetTriggerUnit()), Condition(function Trig_F2_AreaMid_Func013001002)), udg_LocalOtrad2 )
--    call GroupRemoveGroup( GetUnitsOfPlayerMatching(GetOwningPlayer(GetTriggerUnit()), Condition(function Trig_F2_AreaMid_Func014001002)), udg_LocalOtrad2 )
--    call GroupRemoveGroup( GetUnitsOfPlayerMatching(GetOwningPlayer(GetTriggerUnit()), Condition(function Trig_F2_AreaMid_Func015001002)), udg_LocalOtrad2 )
--    call GroupRemoveGroup( GetUnitsOfPlayerMatching(GetOwningPlayer(GetTriggerUnit()), Condition(function Trig_F2_AreaMid_Func016001002)), udg_LocalOtrad2 )
--    call GroupRemoveGroup( GetUnitsOfPlayerMatching(GetOwningPlayer(GetTriggerUnit()), Condition(function Trig_F2_AreaMid_Func017001002)), udg_LocalOtrad2 )
   udg_F_Group[GetConvertedPlayerId(GetOwningPlayer(GetTriggerUnit()))]=udg_LocalOtrad2
end
--===========================================================================
function InitTrig_F2_AreaMid()
    gg_trg_F2_AreaMid=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_F2_AreaMid, EVENT_PLAYER_UNIT_SPELL_EFFECT)
    TriggerAddAction(gg_trg_F2_AreaMid, function()
        if GetSpellAbilityId() ~= FourCC('A0V4') then return end
        Trig_F2_AreaMid_Actions()
    end)
end
--===========================================================================
-- Trigger: F2 AreaSmall
--===========================================================================
--
--function Trig_F2_AreaSmall_Func002002001 takes nothing returns boolean
--    return ( IsUnitType(GetFilterUnit(), UNIT_TYPE_STRUCTURE) != true )
--endfunction
--
--function Trig_F2_AreaSmall_Func002002002001 takes nothing returns boolean
--    return ( IsUnitType(GetFilterUnit(), UNIT_TYPE_HERO) != true )
--endfunction
--
--function Trig_F2_AreaSmall_Func002002002002001 takes nothing returns boolean
--    return ( GetUnitAbilityLevelSwapped('A001', GetFilterUnit()) == 0 )
--endfunction
--
--function Trig_F2_AreaSmall_Func002002002002002001 takes nothing returns boolean
--    return ( GetUnitAbilityLevelSwapped('Slo3', GetFilterUnit()) == 0 )
--endfunction
--
--function Trig_F2_AreaSmall_Func002002002002002002001 takes nothing returns boolean
--    return ( GetUnitAbilityLevelSwapped('ANha', GetFilterUnit()) == 0 )
--endfunction
--
--function Trig_F2_AreaSmall_Func002002002002002002002001 takes nothing returns boolean
--    return ( GetOwningPlayer(GetTriggerUnit()) == GetOwningPlayer(GetFilterUnit()) )
--endfunction
--
--function Trig_F2_AreaSmall_Func002002002002002002002002001 takes nothing returns boolean
--    return ( GetUnitAbilityLevelSwapped('Awha', GetFilterUnit()) == 0 )
--endfunction
--
--function Trig_F2_AreaSmall_Func002002002002002002002002002 takes nothing returns boolean
--    return ( 1 == 1 )
--endfunction
--
--function Trig_F2_AreaSmall_Func002002002002002002002002 takes nothing returns boolean
--    return GetBooleanAnd( Trig_F2_AreaSmall_Func002002002002002002002002001(), Trig_F2_AreaSmall_Func002002002002002002002002002() )
--endfunction
--
--function Trig_F2_AreaSmall_Func002002002002002002002 takes nothing returns boolean
--    return GetBooleanAnd( Trig_F2_AreaSmall_Func002002002002002002002001(), Trig_F2_AreaSmall_Func002002002002002002002002() )
--endfunction
--
--function Trig_F2_AreaSmall_Func002002002002002002 takes nothing returns boolean
--    return GetBooleanAnd( Trig_F2_AreaSmall_Func002002002002002002001(), Trig_F2_AreaSmall_Func002002002002002002002() )
--endfunction
--
--function Trig_F2_AreaSmall_Func002002002002002 takes nothing returns boolean
--    return GetBooleanAnd( Trig_F2_AreaSmall_Func002002002002002001(), Trig_F2_AreaSmall_Func002002002002002002() )
--endfunction
--
--function Trig_F2_AreaSmall_Func002002002002 takes nothing returns boolean
--    return GetBooleanAnd( Trig_F2_AreaSmall_Func002002002002001(), Trig_F2_AreaSmall_Func002002002002002() )
--endfunction
--
--function Trig_F2_AreaSmall_Func002002002 takes nothing returns boolean
--    return GetBooleanAnd( Trig_F2_AreaSmall_Func002002002001(), Trig_F2_AreaSmall_Func002002002002() )
--endfunction
--
--function Trig_F2_AreaSmall_Func002002 takes nothing returns boolean
--    return GetBooleanAnd( Trig_F2_AreaSmall_Func002002001(), Trig_F2_AreaSmall_Func002002002() )
--endfunction
--
--function Trig_F2_AreaSmall_Func004001002 takes nothing returns boolean
--    return ( GetUnitAbilityLevelSwapped('ANha', GetFilterUnit()) == 1 )
--endfunction
--
--function Trig_F2_AreaSmall_Func005001002 takes nothing returns boolean
--    return ( GetUnitAbilityLevelSwapped('A0OY', GetFilterUnit()) == 1 )
--endfunction
--
--function Trig_F2_AreaSmall_Func006001002 takes nothing returns boolean
--    return ( GetUnitAbilityLevelSwapped('A0MJ', GetFilterUnit()) == 1 )
--endfunction
--
--function Trig_F2_AreaSmall_Func007001002 takes nothing returns boolean
--    return ( GetUnitAbilityLevelSwapped('A09P', GetFilterUnit()) == 1 )
--endfunction
--
--function Trig_F2_AreaSmall_Func008001002 takes nothing returns boolean
--    return ( GetUnitAbilityLevelSwapped('Awha', GetFilterUnit()) == 1 )
--endfunction
--
--function Trig_F2_AreaSmall_Func009001002 takes nothing returns boolean
--    return ( GetUnitAbilityLevelSwapped('Awh2', GetFilterUnit()) == 1 )
--endfunction
--
--function Trig_F2_AreaSmall_Func010001002 takes nothing returns boolean
--    return ( GetUnitAbilityLevelSwapped('A0SJ', GetFilterUnit()) == 1 )
--endfunction
--
--function Trig_F2_AreaSmall_Func011001002 takes nothing returns boolean
--    return ( GetUnitTypeId(GetFilterUnit()) == 'e01R' )
--endfunction
--
--function Trig_F2_AreaSmall_Func012001002 takes nothing returns boolean
--    return ( GetUnitTypeId(GetFilterUnit()) == 'h07A' )
--endfunction
--
--function Trig_F2_AreaSmall_Func013001002 takes nothing returns boolean
--    return ( GetUnitAbilityLevelSwapped('Ahar', GetFilterUnit()) == 1 )
--endfunction
--
--function Trig_F2_AreaSmall_Func014001002 takes nothing returns boolean
--    return ( GetUnitAbilityLevelSwapped('Ahr3', GetFilterUnit()) == 1 )
--endfunction
--
--function Trig_F2_AreaSmall_Func015001002 takes nothing returns boolean
--    return ( GetUnitAbilityLevelSwapped('A0VY', GetFilterUnit()) == 1 )
--endfunction
--
--function Trig_F2_AreaSmall_Func016001002 takes nothing returns boolean
--    return ( GetUnitAbilityLevelSwapped('A0SJ', GetFilterUnit()) == 2 )
--endfunction
--
--function Trig_F2_AreaSmall_Func017001002 takes nothing returns boolean
--    return ( GetUnitAbilityLevelSwapped('A0VZ', GetFilterUnit()) == 1 )
--endfunction
--
function Trig_F2_AreaSmall_Actions()
    udg_LocalPlayer=GetOwningPlayer(GetTriggerUnit())
    GroupEnumUnitsInRange(udg_LocalOtrad2, GetSpellTargetX(), GetSpellTargetY(), 500, F2_targets)
--    call GroupRemoveGroup( GetUnitsOfPlayerMatching(GetOwningPlayer(GetTriggerUnit()), Condition(function Trig_F2_AreaSmall_Func004001002)), udg_LocalOtrad2 )
--    call GroupRemoveGroup( GetUnitsOfPlayerMatching(GetOwningPlayer(GetTriggerUnit()), Condition(function Trig_F2_AreaSmall_Func005001002)), udg_LocalOtrad2 )
--    call GroupRemoveGroup( GetUnitsOfPlayerMatching(GetOwningPlayer(GetTriggerUnit()), Condition(function Trig_F2_AreaSmall_Func006001002)), udg_LocalOtrad2 )
--    call GroupRemoveGroup( GetUnitsOfPlayerMatching(GetOwningPlayer(GetTriggerUnit()), Condition(function Trig_F2_AreaSmall_Func007001002)), udg_LocalOtrad2 )
--    call GroupRemoveGroup( GetUnitsOfPlayerMatching(GetOwningPlayer(GetTriggerUnit()), Condition(function Trig_F2_AreaSmall_Func008001002)), udg_LocalOtrad2 )
--    call GroupRemoveGroup( GetUnitsOfPlayerMatching(GetOwningPlayer(GetTriggerUnit()), Condition(function Trig_F2_AreaSmall_Func009001002)), udg_LocalOtrad2 )
--    call GroupRemoveGroup( GetUnitsOfPlayerMatching(GetOwningPlayer(GetTriggerUnit()), Condition(function Trig_F2_AreaSmall_Func010001002)), udg_LocalOtrad2 )
--    call GroupRemoveGroup( GetUnitsOfPlayerMatching(GetOwningPlayer(GetTriggerUnit()), Condition(function Trig_F2_AreaSmall_Func011001002)), udg_LocalOtrad2 )
--    call GroupRemoveGroup( GetUnitsOfPlayerMatching(GetOwningPlayer(GetTriggerUnit()), Condition(function Trig_F2_AreaSmall_Func012001002)), udg_LocalOtrad2 )
--    call GroupRemoveGroup( GetUnitsOfPlayerMatching(GetOwningPlayer(GetTriggerUnit()), Condition(function Trig_F2_AreaSmall_Func013001002)), udg_LocalOtrad2 )
--    call GroupRemoveGroup( GetUnitsOfPlayerMatching(GetOwningPlayer(GetTriggerUnit()), Condition(function Trig_F2_AreaSmall_Func014001002)), udg_LocalOtrad2 )
--    call GroupRemoveGroup( GetUnitsOfPlayerMatching(GetOwningPlayer(GetTriggerUnit()), Condition(function Trig_F2_AreaSmall_Func015001002)), udg_LocalOtrad2 )
--    call GroupRemoveGroup( GetUnitsOfPlayerMatching(GetOwningPlayer(GetTriggerUnit()), Condition(function Trig_F2_AreaSmall_Func016001002)), udg_LocalOtrad2 )
--    call GroupRemoveGroup( GetUnitsOfPlayerMatching(GetOwningPlayer(GetTriggerUnit()), Condition(function Trig_F2_AreaSmall_Func017001002)), udg_LocalOtrad2 )
 udg_F_Group[GetConvertedPlayerId(GetOwningPlayer(GetTriggerUnit()))]=udg_LocalOtrad2
    
end
--===========================================================================
function InitTrig_F2_AreaSmall()
    gg_trg_F2_AreaSmall=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_F2_AreaSmall, EVENT_PLAYER_UNIT_SPELL_EFFECT)
    TriggerAddAction(gg_trg_F2_AreaSmall, function()
        if GetSpellAbilityId() ~= FourCC('A0VL') then return end
        Trig_F2_AreaSmall_Actions()
    end)
end
--===========================================================================
-- Trigger: InFGroup
--===========================================================================
function Trig_InFGroup_Func001A()
    DisplayTextToForce(GetPlayersAll(), BlzGetUnitStringField(GetEnumUnit(), UNIT_SF_NAME))
end
function Trig_InFGroup_Actions()
    ForGroupBJ(udg_F_Group[GetConvertedPlayerId(GetTriggerPlayer())], Trig_InFGroup_Func001A)
end
--===========================================================================
function InitTrig_InFGroup()
    gg_trg_InFGroup=CreateTrigger()
    TriggerRegisterPlayerChatEvent(gg_trg_InFGroup, Player(0), " - f2gr", true)
    TriggerAddAction(gg_trg_InFGroup, Trig_InFGroup_Actions)
end
--===========================================================================
-- Trigger: ToKill2
--
-- ????? ???? ????? ??? ???????, ??????? ?? ????? ?????? LocalUni2
--===========================================================================
function Trig_ToKill2_Actions()
    RemoveUnitTimed(udg_LocalUnit2 , 2)
end
--===========================================================================
function InitTrig_ToKill2()
    gg_trg_ToKill2=CreateTrigger()
    TriggerAddAction(gg_trg_ToKill2, Trig_ToKill2_Actions)
end
--===========================================================================
-- Trigger: RemoveDammySpecial
--===========================================================================
function Trig_RemoveDammySpecial_Conditions()
    return GetUnitTypeId(GetSummonedUnit()) == FourCC('h02F')
end
function Trig_RemoveDammySpecial_Actions()
    RemoveUnit(GetSummonedUnit())
end
--===========================================================================
function InitTrig_RemoveDammySpecial()
    gg_trg_RemoveDammySpecial=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_RemoveDammySpecial, EVENT_PLAYER_UNIT_SUMMON)
    TriggerAddCondition(gg_trg_RemoveDammySpecial, Condition(Trig_RemoveDammySpecial_Conditions))
    TriggerAddAction(gg_trg_RemoveDammySpecial, Trig_RemoveDammySpecial_Actions)
end
--===========================================================================
-- Trigger: MageTpSell
--===========================================================================
function Trig_MageTpSell_Conditions()
    return ( GetUnitTypeId(GetTriggerUnit()) == FourCC('h07A') )
end
function Trig_MageTpSell_Func002Func001C()
    return (( GetOwningPlayer(GetTriggerUnit()) ~= GetOwningPlayer(GetSoldUnit()) )) and GetPlayerAlliance(GetOwningPlayer(GetTriggerUnit()), GetOwningPlayer(GetSoldUnit()), ALLIANCE_SHARED_ADVANCED_CONTROL)
end
function Trig_MageTpSell_Func002Func002C()
    return (( ( GetOwningPlayer(GetTriggerUnit()) == GetOwningPlayer(GetSoldUnit()) ) )) or GetPlayerAlliance(GetOwningPlayer(GetTriggerUnit()), GetOwningPlayer(GetSoldUnit()), ALLIANCE_SHARED_ADVANCED_CONTROL)
end
function Trig_MageTpSell_Func002C()
    return Trig_MageTpSell_Func002Func002C()
end
function Trig_MageTpSell_Actions()
    local pi= GetPlayerId(GetOwningPlayer(GetTriggerUnit()))
    if ( Trig_MageTpSell_Func002C() ) then
        if ( Trig_MageTpSell_Func002Func001C() ) then
            SetUnitOwner(GetSoldUnit(), GetOwningPlayer(GetTriggerUnit()), true)
            AddCountDis(GetSoldUnit() , GetPlayerId(GetOwningPlayer(GetTriggerUnit())))
            DelCountDis(GetSoldUnit() , GetPlayerId(GetOwningPlayer(GetSoldUnit())))
            GoldDifference[pi]=GoldDifference[pi] - GetUnitGoldCost(GetUnitTypeId(GetSoldUnit()))
            LumberDifference[pi]=LumberDifference[pi] - GetUnitWoodCost(GetUnitTypeId(GetSoldUnit()))
        end
        udg_LocalPosition2=GetUnitRallyPoint(GetTriggerUnit())
        IssuePointOrderLocBJ(GetSoldUnit(), "move", udg_LocalPosition2)
        RemoveLocation(udg_LocalPosition2)
    else
        RemoveUnit(GetSoldUnit())
        DelCountDis(GetSoldUnit() , GetPlayerId(GetOwningPlayer(GetSoldUnit())))
    end
end
--===========================================================================
function InitTrig_MageTpSell()
