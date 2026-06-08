
--===========================================================================
-- Trigger: Sluga qqgsarona
--===========================================================================
function Trig_Sluga_qqgsarona_Func010A()
    SetPlayerAbilityAvailableBJ(false, FourCC('A12G'), GetEnumPlayer())
end
function Trig_Sluga_qqgsarona_Func012001002()
    return IsUnitInGroup(GetFilterUnit(), udg_StolicaGroups)
end
function Trig_Sluga_qqgsarona_Func012A()
    GroupRemoveUnitSimple(GetEnumUnit(), udg_StolicaGroups)
    ReplaceUnitBJ(GetEnumUnit(), GetUnitTypeId(GetEnumUnit()), bj_UNIT_STATE_METHOD_RELATIVE)
end
function Trig_Sluga_qqgsarona_Func017A()
    UnitShareVisionBJ(true, gg_unit_n03A_0657, GetEnumPlayer())
end
function Trig_Sluga_qqgsarona_Actions()
    SetUnitOwner(gg_unit_n03A_0657, GetOwningPlayer(GetSpellAbilityUnit()), true)
    RemoveUnit(gg_unit_n03C_0660)
    RemoveUnit(gg_unit_n03C_0661)
    RemoveUnit(gg_unit_n03C_0663)
    RemoveUnit(gg_unit_n03C_0662)
    RemoveUnit(gg_unit_n03B_0664)
    RemoveUnit(gg_unit_n03B_0665)
    RemoveUnit(gg_unit_n03B_0658)
    RemoveUnit(gg_unit_n03B_0659)
    ForForce(GetPlayersAll(), Trig_Sluga_qqgsarona_Func010A)
    -- --
    ForGroupBJ(GetUnitsOfPlayerMatching(GetOwningPlayer(GetTriggerUnit()), Condition(Trig_Sluga_qqgsarona_Func012001002)), Trig_Sluga_qqgsarona_Func012A)
    GroupAddUnitSimple(gg_unit_n03A_0657, udg_StolicaGroups)
    BlzSetUnitStringFieldBJ(gg_unit_n03A_0657, UNIT_SF_NAME, "cffd45e19r" .. GetUnitName(gg_unit_n03A_0657))
    ForForce(GetPlayersAll(), Trig_Sluga_qqgsarona_Func017A)
    DisableTrigger(GetTriggeringTrigger())
end
--===========================================================================
function InitTrig_Sluga_qqgsarona()
    gg_trg_Sluga_qqgsarona=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_Sluga_qqgsarona, EVENT_PLAYER_UNIT_SPELL_EFFECT)
    TriggerAddAction(gg_trg_Sluga_qqgsarona, function()
        if GetSpellAbilityId() ~= FourCC('A12G') then return end
        Trig_Sluga_qqgsarona_Actions()
    end)
end
--===========================================================================
-- Trigger: Sila2
--===========================================================================
function Trig_Sila2_Conditions()
    return GetResearched() == FourCC('R0F7')
end
function Trig_Sila2_Actions()
    SetPlayerTechMaxAllowedSwap(FourCC('R0F8'), 1, GetOwningPlayer(GetTriggerUnit()))
end
--===========================================================================
function InitTrig_Sila2()
    gg_trg_Sila2=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_Sila2, EVENT_PLAYER_UNIT_RESEARCH_CANCEL)
    TriggerAddCondition(gg_trg_Sila2, Condition(Trig_Sila2_Conditions))
    TriggerAddAction(gg_trg_Sila2, Trig_Sila2_Actions)
end
--===========================================================================
-- Trigger: Sila1
--===========================================================================
function Trig_Sila1_Conditions()
    return GetResearched() == FourCC('R0F7')
end
function Trig_Sila1_Actions()
    SetPlayerTechMaxAllowedSwap(FourCC('R0F8'), 0, GetOwningPlayer(GetTriggerUnit()))
end
--===========================================================================
function InitTrig_Sila1()
    gg_trg_Sila1=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_Sila1, EVENT_PLAYER_UNIT_RESEARCH_FINISH)
    TriggerRegisterAnyUnitEventBJ(gg_trg_Sila1, EVENT_PLAYER_UNIT_RESEARCH_START)
    TriggerAddCondition(gg_trg_Sila1, Condition(Trig_Sila1_Conditions))
    TriggerAddAction(gg_trg_Sila1, Trig_Sila1_Actions)
end
--===========================================================================
-- Trigger: Skorost2
--===========================================================================
function Trig_Skorost2_Conditions()
    return GetResearched() == FourCC('R0F8')
end
function Trig_Skorost2_Actions()
    SetPlayerTechMaxAllowedSwap(FourCC('R0F7'), 1, GetOwningPlayer(GetTriggerUnit()))
end
--===========================================================================
function InitTrig_Skorost2()
    gg_trg_Skorost2=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_Skorost2, EVENT_PLAYER_UNIT_RESEARCH_CANCEL)
    TriggerAddCondition(gg_trg_Skorost2, Condition(Trig_Skorost2_Conditions))
    TriggerAddAction(gg_trg_Skorost2, Trig_Skorost2_Actions)
end
--===========================================================================
-- Trigger: Skorost1
--===========================================================================
function Trig_Skorost1_Conditions()
    return GetResearched() == FourCC('R0F8')
end
function Trig_Skorost1_Actions()
    SetPlayerTechMaxAllowedSwap(FourCC('R0F7'), 0, GetOwningPlayer(GetTriggerUnit()))
end
--===========================================================================
function InitTrig_Skorost1()
    gg_trg_Skorost1=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_Skorost1, EVENT_PLAYER_UNIT_RESEARCH_FINISH)
    TriggerRegisterAnyUnitEventBJ(gg_trg_Skorost1, EVENT_PLAYER_UNIT_RESEARCH_START)
    TriggerAddCondition(gg_trg_Skorost1, Condition(Trig_Skorost1_Conditions))
    TriggerAddAction(gg_trg_Skorost1, Trig_Skorost1_Actions)
end
--===========================================================================
-- Trigger: ZdaniyaBezlik
--===========================================================================
function Trig_ZdaniyaBezlik_Actions()
    udg_Untitled_Variable_001[GetConvertedPlayerId(GetOwningPlayer(GetSpellAbilityUnit()))]=GetSpellTargetLoc()
    CreateNUnitsAtLoc(1, FourCC('n01T'), GetOwningPlayer(GetTriggerUnit()), udg_Untitled_Variable_001[1], bj_UNIT_FACING)
end
--===========================================================================
function InitTrig_ZdaniyaBezlik()
    gg_trg_ZdaniyaBezlik=CreateTrigger()
    DisableTrigger(gg_trg_ZdaniyaBezlik)
    TriggerRegisterAnyUnitEventBJ(gg_trg_ZdaniyaBezlik, EVENT_PLAYER_UNIT_SPELL_EFFECT)
    TriggerAddAction(gg_trg_ZdaniyaBezlik, function()
        if GetSpellAbilityId() ~= FourCC('A0LK') then return end
        Trig_ZdaniyaBezlik_Actions()
    end)
end
--===========================================================================
-- Trigger: ZdaniyaBezlik Copy
--===========================================================================
function Trig_ZdaniyaBezlik_Copy_Actions()
    udg_Untitled_Variable_001[GetConvertedPlayerId(GetOwningPlayer(GetSpellAbilityUnit()))]=GetSpellTargetLoc()
    CreateNUnitsAtLoc(1, FourCC('n01Q'), GetOwningPlayer(GetTriggerUnit()), udg_Untitled_Variable_001[1], bj_UNIT_FACING)
end
--===========================================================================
function InitTrig_ZdaniyaBezlik_Copy()
    gg_trg_ZdaniyaBezlik_Copy=CreateTrigger()
    DisableTrigger(gg_trg_ZdaniyaBezlik_Copy)
    TriggerRegisterAnyUnitEventBJ(gg_trg_ZdaniyaBezlik_Copy, EVENT_PLAYER_UNIT_SPELL_EFFECT)
    TriggerAddAction(gg_trg_ZdaniyaBezlik_Copy, function()
        if GetSpellAbilityId() ~= FourCC('A0LN') then return end
        Trig_ZdaniyaBezlik_Copy_Actions()
    end)
end
--===========================================================================
-- Trigger: ZdaniyaBezlik Copy Copy
--===========================================================================
function Trig_ZdaniyaBezlik_Copy_Copy_Actions()
    udg_Untitled_Variable_001[GetConvertedPlayerId(GetOwningPlayer(GetSpellAbilityUnit()))]=GetSpellTargetLoc()
    CreateNUnitsAtLoc(1, FourCC('n01S'), GetOwningPlayer(GetTriggerUnit()), udg_Untitled_Variable_001[1], bj_UNIT_FACING)
end
--===========================================================================
function InitTrig_ZdaniyaBezlik_Copy_Copy()
    gg_trg_ZdaniyaBezlik_Copy_Copy=CreateTrigger()
    DisableTrigger(gg_trg_ZdaniyaBezlik_Copy_Copy)
    TriggerRegisterAnyUnitEventBJ(gg_trg_ZdaniyaBezlik_Copy_Copy, EVENT_PLAYER_UNIT_SPELL_EFFECT)
    TriggerAddAction(gg_trg_ZdaniyaBezlik_Copy_Copy, function()
        if GetSpellAbilityId() ~= FourCC('A0LM') then return end
        Trig_ZdaniyaBezlik_Copy_Copy_Actions()
    end)
end
--===========================================================================
-- Trigger: ZdaniyaBezlik Copy Copy 2
--===========================================================================
function Trig_ZdaniyaBezlik_Copy_Copy_2_Actions()
    udg_Untitled_Variable_001[GetConvertedPlayerId(GetOwningPlayer(GetSpellAbilityUnit()))]=GetSpellTargetLoc()
    CreateNUnitsAtLoc(1, FourCC('n01R'), GetOwningPlayer(GetTriggerUnit()), udg_Untitled_Variable_001[1], bj_UNIT_FACING)
end
--===========================================================================
function InitTrig_ZdaniyaBezlik_Copy_Copy_2()
    gg_trg_ZdaniyaBezlik_Copy_Copy_2=CreateTrigger()
    DisableTrigger(gg_trg_ZdaniyaBezlik_Copy_Copy_2)
    TriggerRegisterAnyUnitEventBJ(gg_trg_ZdaniyaBezlik_Copy_Copy_2, EVENT_PLAYER_UNIT_SPELL_EFFECT)
    TriggerAddAction(gg_trg_ZdaniyaBezlik_Copy_Copy_2, function()
        if GetSpellAbilityId() ~= FourCC('A0LO') then return end
        Trig_ZdaniyaBezlik_Copy_Copy_2_Actions()
    end)
end
--===========================================================================
-- Trigger: ZdaniyaBezlik Copy Copy 2 Copy
--===========================================================================
function Trig_ZdaniyaBezlik_Copy_Copy_2_Copy_Actions()
    udg_Untitled_Variable_001[GetConvertedPlayerId(GetOwningPlayer(GetSpellAbilityUnit()))]=GetSpellTargetLoc()
    CreateNUnitsAtLoc(1, FourCC('n01U'), GetOwningPlayer(GetTriggerUnit()), udg_Untitled_Variable_001[1], bj_UNIT_FACING)
end
--===========================================================================
function InitTrig_ZdaniyaBezlik_Copy_Copy_2_Copy()
    gg_trg_ZdaniyaBezlik_Copy_Copy_2_Copy=CreateTrigger()
    DisableTrigger(gg_trg_ZdaniyaBezlik_Copy_Copy_2_Copy)
    TriggerRegisterAnyUnitEventBJ(gg_trg_ZdaniyaBezlik_Copy_Copy_2_Copy, EVENT_PLAYER_UNIT_SPELL_EFFECT)
    TriggerAddAction(gg_trg_ZdaniyaBezlik_Copy_Copy_2_Copy, function()
        if GetSpellAbilityId() ~= FourCC('A0LP') then return end
        Trig_ZdaniyaBezlik_Copy_Copy_2_Copy_Actions()
    end)
end
--===========================================================================
-- Trigger: CreateFFarm
--===========================================================================
function Trig_CreateFFarm_Actions()
    FaselessFarmLimit(GetOwningPlayer(GetTriggerUnit()))
end
--===========================================================================
function InitTrig_CreateFFarm()
    gg_trg_CreateFFarm=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_CreateFFarm, EVENT_PLAYER_UNIT_SPELL_EFFECT)
    TriggerAddAction(gg_trg_CreateFFarm, function()
        if GetSpellAbilityId() ~= FourCC('A11G') then return end
        Trig_CreateFFarm_Actions()
    end)
end
--===========================================================================
-- Trigger: DeadFFarm
--===========================================================================
function Trig_DeadFFarm_Conditions()
    return GetUnitTypeId(GetTriggerUnit()) == FourCC('u02E')
end
function Trig_DeadFFarm_Actions()
    FaselessFarmLimit(GetOwningPlayer(GetTriggerUnit()))
end
--===========================================================================
function InitTrig_DeadFFarm()
    gg_trg_DeadFFarm=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_DeadFFarm, EVENT_PLAYER_UNIT_DEATH)
    TriggerAddCondition(gg_trg_DeadFFarm, Condition(Trig_DeadFFarm_Conditions))
    TriggerAddAction(gg_trg_DeadFFarm, Trig_DeadFFarm_Actions)
end
--===========================================================================
-- Trigger: FinishFaceBuild
--===========================================================================
function Trig_FinishFaceBuild_Conditions()
    return GetUnitTypeId(GetConstructedStructure()) == FourCC('h0HZ')
end
function Trig_FinishFaceBuild_Actions()
    GroupAddUnitSimple(GetConstructedStructure(), udg_FacelessLumberBuildings)
end
--===========================================================================
function InitTrig_FinishFaceBuild()
    gg_trg_FinishFaceBuild=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_FinishFaceBuild, EVENT_PLAYER_UNIT_CONSTRUCT_FINISH)
    TriggerAddCondition(gg_trg_FinishFaceBuild, Condition(Trig_FinishFaceBuild_Conditions))
    TriggerAddAction(gg_trg_FinishFaceBuild, Trig_FinishFaceBuild_Actions)
end
--===========================================================================
-- Trigger: DeadFaceBuild
--===========================================================================
function Trig_DeadFaceBuild_Conditions()
    return GetUnitTypeId(GetDyingUnit()) == FourCC('h0HZ')
end
function Trig_DeadFaceBuild_Actions()
    GroupRemoveUnitSimple(GetTriggerUnit(), udg_FacelessLumberBuildings)
end
--===========================================================================
function InitTrig_DeadFaceBuild()
    gg_trg_DeadFaceBuild=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_DeadFaceBuild, EVENT_PLAYER_UNIT_DEATH)
    TriggerAddCondition(gg_trg_DeadFaceBuild, Condition(Trig_DeadFaceBuild_Conditions))
    TriggerAddAction(gg_trg_DeadFaceBuild, Trig_DeadFaceBuild_Actions)
end
--===========================================================================
-- Trigger: LumberTest
--===========================================================================
function KillTextTag()
    local t= TT
    TriggerSleepAction(3)
    DestroyTextTag(t)
    t=nil
end
function TT2()
    local t= CreateTextTag()
    local p= Player(0)
    local s= I2S(5)
    local f= GetEnumDestructable()
    local l= Location(GetDestructableX(f), GetDestructableY(f))
    
    DisplayTextToPlayer(Player(0), 0, 0, "")
    AdjustPlayerStateBJ(5, p, PLAYER_STATE_RESOURCE_LUMBER)
    
    
    t=CreateTextTagLocBJ(s, l, 0, 10, 0.00, 100, 0.00, 0)
    SetTextTagPermanent(t, false)
    SetTextTagLifespan(t, 3.00)
    SetTextTagVelocity(t, 50.00, 90)
    SetTextTagFadepoint(t, 1.00)
    RemoveLocation(l)
    l=nil
    f=nil
    TT=t
    t=nil
    p=nil
    s=nil
    ExecuteFunc("KillTextTag")
end
    
function Trig_LumberTest_Actions()
    local g= CreateGroup()
    local d
    local u= nil
    local l
    local r
    
    local radius
    local centerX
    local centerY
    --call DisplayTextToPlayer(Player(0),0,0,"0")
    GroupAddGroup(udg_FacelessLumberBuildings, g)
    --call DisplayTextToPlayer(Player(0),0,0, I2S(CountUnitsInGroup(g)))
    while true do
        u=FirstOfGroup(g)
        if u == nil then break end
        
        DisplayTextToPlayer(Player(0), 0, 0, "")
        udg_LocalPlayer=GetOwningPlayer(u)
        l=GetUnitLoc(u)
        --call EnumDestructablesInCircleBJ( 500.00, l, function TT2 )
        
        
        radius=650
        
        --set r = GetRectFromCircleBJ(loc, radius)
        --set centerX = GetLocationX(l)
        --set centerY = GetLocationY(l)
        
        bj_enumDestructableCenter=l
        bj_enumDestructableRadius=radius
        r=GetRectFromCircleBJ(l, radius)
        --set r = Rect(centerX - radius, centerY - radius, centerX + radius, centerY + radius)
        DisplayTextToPlayer(Player(0), 0, 0, "2")
        EnumDestructablesInRect(r, filterEnumDestructablesInCircleBJ, TT2)
        RemoveRect(r)
        
        
        
        
        
        
        RemoveLocation(l)
        GroupRemoveUnit(g, u)
        r=nil
        l=nil
        TriggerSleepAction(0.01)
    end
    RemoveRect(r)
    r=nil
    RemoveLocation(l)
    l=nil
    DestroyGroup(g)
    u=nil
    g=nil
end
--===========================================================================
function InitTrig_LumberTest()
    gg_trg_LumberTest=CreateTrigger()
    DisableTrigger(gg_trg_LumberTest)
    TriggerRegisterTimerEventPeriodic(gg_trg_LumberTest, 5.00)
    TriggerAddAction(gg_trg_LumberTest, Trig_LumberTest_Actions)
end
--===========================================================================
-- Trigger: Spell2
--===========================================================================
function Trig_Spell2_Conditions()
    return GetUnitAbilityLevel(GetAttacker(), FourCC('A122')) == 1 and not IsUnitType(GetTriggerUnit(), UNIT_TYPE_STRUCTURE)
end
function Trig_Spell2_Actions()
    UnitDamageTargetBJ(GetAttacker(), GetTriggerUnit(), GetUnitStateSwap(UNIT_STATE_MAX_LIFE, GetTriggerUnit()) * 0.014, ATTACK_TYPE_NORMAL, DAMAGE_TYPE_COLD)
end
--===========================================================================
function InitTrig_Spell2()
    gg_trg_Spell2=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_Spell2, EVENT_PLAYER_UNIT_ATTACKED)
    TriggerAddCondition(gg_trg_Spell2, Condition(Trig_Spell2_Conditions))
    TriggerAddAction(gg_trg_Spell2, Trig_Spell2_Actions)
end
--===========================================================================
-- Trigger: SpellRes
--===========================================================================
function Trig_SpellRes_Conditions()
    return GetUnitAbilityLevelSwapped(FourCC('A123'), GetKillingUnitBJ()) == 1
end
function Trig_SpellRes_Actions()
    BlzEndUnitAbilityCooldown(GetKillingUnitBJ(), FourCC('A123'))
end
--===========================================================================
function InitTrig_SpellRes()
    gg_trg_SpellRes=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_SpellRes, EVENT_PLAYER_UNIT_DEATH)
    TriggerAddCondition(gg_trg_SpellRes, Condition(Trig_SpellRes_Conditions))
    TriggerAddAction(gg_trg_SpellRes, Trig_SpellRes_Actions)
end
--===========================================================================
-- Trigger: Muscules
--===========================================================================
function Trig_Muscules_Actions()
    UnitAddAbility(GetTriggerUnit(), FourCC('A0PQ'))
    TriggerSleepAction(20.00)
    RemoveAbilityTimed(GetTriggerUnit() , FourCC('A0PQ') , 20)
end
--===========================================================================
function InitTrig_Muscules()
    gg_trg_Muscules=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_Muscules, EVENT_PLAYER_UNIT_SPELL_EFFECT)
    TriggerAddAction(gg_trg_Muscules, function()
        if GetSpellAbilityId() ~= FourCC('A0QS') then return end
        Trig_Muscules_Actions()
    end)
end
--===========================================================================
-- Trigger: BuidingThatSellRecruts
--===========================================================================
function Trig_BuidingThatSellRecruts_Conditions()
    return GetUnitTypeId(GetConstructedStructure()) == FourCC('h0NX') -- ????????? ??????, ??????
end
function NewMember()
    
    local t= GetExpiredTimer()
    local id= GetHandleId(t)
    local u= LoadUnitHandle(Hash, id, 1)
    local uid= GetHandleId(u)
    if UnitAlive(u) then
        SaveInteger(Hash, uid, 1, IMaxBJ(LoadInteger(Hash, uid, 1) + 1, 3))
    
    else
        
        DestroyTimer(t)
        FlushChildHashtable(Hash, id)
        FlushChildHashtable(Hash, uid)
    end
    t=nil
    u=nil
end
function Trig_BuidingThatSellRecruts_Actions()
    local u= GetConstructedStructure()
    local t= CreateTimer()
    local id= GetHandleId(t)
    local uid= GetHandleId(u)
    local startCount= 1
    UnitAddAbility(u, FourCC('Asud'))
    AddUnitToStock(u, FourCC('h0NC'), startCount, 3) --???? ??????? ?????????
    AddUnitToStock(u, FourCC('h0NL'), startCount, 3) --???? ??????? ?????????
    
    TimerStart(t, 30, true, NewMember)
    SaveUnitHandle(Hash, id, 1, u)
    SaveInteger(Hash, uid, 1, startCount)
    u=nil
    t=nil
end
--===========================================================================
function InitTrig_BuidingThatSellRecruts()
    gg_trg_BuidingThatSellRecruts=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_BuidingThatSellRecruts, EVENT_PLAYER_UNIT_CONSTRUCT_FINISH)
    TriggerAddCondition(gg_trg_BuidingThatSellRecruts, Condition(Trig_BuidingThatSellRecruts_Conditions))
    TriggerAddAction(gg_trg_BuidingThatSellRecruts, Trig_BuidingThatSellRecruts_Actions)
end
--
--      call AddUnitToStockBJ( 'hfoo', GetTriggerUnit(), 0, 1 )
--    call RemoveUnitFromStockBJ( 'hfoo', GetTriggerUnit() )
--===========================================================================
-- Trigger: BuidingSell
--===========================================================================
function Trig_BuidingSell_Conditions()
    return GetUnitTypeId(GetSellingUnit()) == FourCC('h0NX') -- ????????? ??????, ??????
end
function Trig_BuidingSell_Actions()
    local u= GetSellingUnit()
    local uid= GetHandleId(u)
    local currentCount= LoadInteger(Hash, uid, 1)
    SaveInteger(Hash, uid, 1, currentCount - 1)
    RemoveUnitFromStock(u, FourCC('h0NC')) --???? ??????? ?????????
    RemoveUnitFromStock(u, FourCC('h0NL')) --???? ??????? ?????????
    
    AddUnitToStock(u, FourCC('h0NC'), currentCount - 1, 3) --???? ??????? ?????????
    AddUnitToStock(u, FourCC('h0NL'), currentCount - 1, 3) --???? ??????? ?????????
    
    
end
--===========================================================================
function InitTrig_BuidingSell()
    gg_trg_BuidingSell=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_BuidingSell, EVENT_PLAYER_UNIT_SELL)
    TriggerAddCondition(gg_trg_BuidingSell, Condition(Trig_BuidingSell_Conditions))
    TriggerAddAction(gg_trg_BuidingSell, Trig_BuidingSell_Actions)
end
--
--      call AddUnitToStockBJ( 'hfoo', GetTriggerUnit(), 0, 1 )
--    call RemoveUnitFromStockBJ( 'hfoo', GetTriggerUnit() )
--===========================================================================
-- Trigger: JumpSTR
--===========================================================================
-- ?????????? ?????????? ?????? ?????? ???
--===================================================================================================================================
-- ???????? ???????, ??? ?????? ?????? ?? ?????
--===================================================================================================================================
--================================================================================================================================================================================
-- ???? 0 - ??? ???????
--================
function JSTRUgolMT()
    return bj_RADTODEG * Atan2(y2 - y1, x2 - x1)
end
function JSTRRastMT()
    local dx= x2 - x1
    local dy= y2 - y1
    return SquareRoot(dx * dx + dy * dy)
end
function JSTRParabolaZ()
  return ( 4 * h / d ) * ( d - x ) * ( x / d )
end
--h - ???????????? ?????? ? ?????? ?? ???????? ?????????? (x = d / 2),
--d - ????? ?????????? ?? ????
--x - ?????????? ?? ???????? ???? ?? ?????, ??? ??????? ????? ?????? ?? ????????.
--================================================================================================================================================================================
-- ???? 1 - ???????? ????? - ????? ??? ??? ??????)))
--================
function Trig_JumpSTR_Conditions()
end
--================================================================================================================================================================================
-- ???? 3 - ??????? ??????
--================
function Trig_JumpSTR_move_units()
    local t= GetExpiredTimer()
    local h= GetHandleId(t)
    local un= LoadUnitHandle(Hash, h, 1)
    local ugol= LoadReal(Hash, h, 2)
    local kol= LoadInteger(Hash, h, 3)
    local x= GetUnitX(un)
    local y= GetUnitY(un)
    -- ---------
    x=x + 10 * Cos(ugol * bj_DEGTORAD) --????????? ????????? ?
    y=y + 10 * Sin(ugol * bj_DEGTORAD) --????????? ????????? ?
    if kol >= 0 and not IsTerrainPathable(x, y, PATHING_TYPE_FLYABILITY) then
        SetUnitX(un, x)
        SetUnitY(un, y)
        SaveInteger(Hash, h, 3, kol - 1)
    else
        DestroyTimer(t)
        FlushChildHashtable(Hash, h)
    end
    -- ----------
    un=nil
    t=nil
end
--================================================================================================================================================================================
-- ???? 2 - ??????? ?????
--================
function Trig_JumpSTR_move_hero()
    local t= GetExpiredTimer()
    local h= GetHandleId(t)
    local GT= LoadUnitHandle(Hash, h, 1)
    local l= LoadReal(Hash, h, 2)
    local g
    local x1= LoadReal(Hash, h, 4)
    local y1= LoadReal(Hash, h, 5)
    local dx= GetUnitX(GT)
    local dy= GetUnitY(GT)
    local un
    local x
    local y
    local uron
    local lvl
    local w
    local ugol= JSTRUgolMT(dx , x1 , dy , y1)
    local t1
    local h1
    local MaxW
    if l <= 500 then
        MaxW=l
    else
        MaxW=500
    end
    ---------
    x=dx + 25 * Cos(ugol * bj_DEGTORAD) --????????? ????????? ?
    y=dy + 25 * Sin(ugol * bj_DEGTORAD) --????????? ????????? ?
    w=JSTRParabolaZ(MaxW , l , JSTRRastMT(x , x1 , y , y1)) --????????? ??????
    
    -- ???? ????? ????
    if JSTRRastMT(x1 , dx , y1 , dy) > 25 then --and not IsTerrainPathable(x, y, PATHING_TYPE_WALKABILITY) then
        -- ??????? ?????
        SetUnitX(GT, x)
        SetUnitY(GT, y)
        SetUnitFacing(GT, ugol)
        SetUnitFlyHeight(GT, w, 0)
    else
        DestroyEffect(LoadEffectHandle(Hash, h, 6))
        DestroyTimer(t)
        FlushChildHashtable(Hash, h)
        SetUnitAnimation(GT, "attack")
        SetUnitFlyHeight(GT, 0, 0)
        DestroyEffect(AddSpecialEffect("AbilitiesSpellsOrcWarStompWarStompCaster.mdl", dx, dy))
        g=CreateGroup()
        GroupEnumUnitsInRange(g, dx, dy, 260, nil)
        while true do
            un=FirstOfGroup(g)
            if un == nil then break end
            lvl=GetUnitAbilityLevel(GT, JSTRSkill)
            
            -- ????? - ???????? ?? ?????
            if IsUnitType(GT, UNIT_TYPE_HERO) then
                uron=JSTRKofDmg1 * lvl * GetHeroStr(GT, true) + lvl * JSTRKofDmg2
            else
                uron=lvl * JSTRKofDmg2 * 4
            end
            
            if not IsUnitType(un, UNIT_TYPE_STRUCTURE) and IsUnitEnemy(un, GetOwningPlayer(GT)) and not IsUnitType(un, UNIT_TYPE_DEAD) and not IsUnitType(un, UNIT_TYPE_FLYING) then
                UnitDamageTarget(GT, un, uron, true, false, ATTACK_TYPE_NORMAL, DAMAGE_TYPE_UNIVERSAL, WEAPON_TYPE_WHOKNOWS)
                DestroyEffect(AddSpecialEffectTarget("AbilitiesSpellsOrcMirrorImageMirrorImageDeathCaster.mdl", un, "orign"))
                ----------
                -- ??????? ????? ? ?????? ??????? ?? ???????
                if JSTRBoolMove then
                    ugol=JSTRUgolMT(dx , GetUnitX(un) , dy , GetUnitY(un))
                    t1=CreateTimer()
                    h1=GetHandleId(t1)
                    SaveUnitHandle(Hash, h1, 1, un)
                    SaveReal(Hash, h1, 2, ugol)
                    SaveInteger(Hash, h1, 3, 17)
                    TimerStart(t1, 0.015, true, Trig_JumpSTR_move_units)
                end
                ---------- 
            end
            GroupRemoveUnit(g, un)
        end
        DestroyGroup(g)
    end
    ---------
    GT=nil
    un=nil
    g=nil
    t=nil
    t1=nil
end
--================================================================================================================================================================================
-- ???? 2 - ???????? ???????
--================
function Trig_JumpSTR_Actions()
    local GT= GetTriggerUnit()
    --local group g = CreateGroup()
    local t= CreateTimer()
    local h= GetHandleId(t)
    local x= GetUnitX(GT)
    local y= GetUnitY(GT)
    local x1= GetSpellTargetX()
    local y1= GetSpellTargetY()
    local l= JSTRRastMT(x , x1 , y , y1)
    
    JSTRSkill=GetSpellAbilityId()
    UnitAddAbility(GT, FourCC('Amrf'))
    UnitRemoveAbility(GT, FourCC('Amrf'))
    ---------
    SaveUnitHandle(Hash, h, 1, GT)
    if l ~= 0 then
        SaveReal(Hash, h, 2, l)
    else
        SaveReal(Hash, h, 2, 1)
    end
    SaveReal(Hash, h, 4, x1)
    SaveReal(Hash, h, 5, y1)
    DestroyEffect(AddSpecialEffect("AbilitiesSpellsOtherVolcanoVolcanoDeath.mdl", x, y))
    TimerStart(t, 0.025, true, Trig_JumpSTR_move_hero) --???????? ???????? ?????
    ---------
    GT=nil
    --set g = null
    t=nil
end
--===========================================================================
function InitTrig_JumpSTR()
    gg_trg_JumpSTR=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_JumpSTR, EVENT_PLAYER_UNIT_SPELL_EFFECT)
    TriggerAddAction(gg_trg_JumpSTR, function()
        if GetSpellAbilityId() ~= FourCC('A1E2') then return end
        if not Trig_JumpSTR_Conditions() then return end
        Trig_JumpSTR_Actions()
    end)
end