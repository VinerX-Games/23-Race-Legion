
--===========================================================================
-- Trigger: ForsacenStarrt
--===========================================================================
function Trig_ForsacenStarrt_Func001A()
    SetPlayerTechMaxAllowedSwap(FourCC('N058'), 1, GetEnumPlayer())
    SetPlayerTechMaxAllowedSwap(FourCC('O031'), 1, GetEnumPlayer())
    SetPlayerTechMaxAllowedSwap(FourCC('O030'), 1, GetEnumPlayer())
    SetPlayerTechMaxAllowedSwap(FourCC('N059'), 1, GetEnumPlayer())
end
function Trig_ForsacenStarrt_Actions()
    ForForce(udg_AllPlayers, Trig_ForsacenStarrt_Func001A)
end
--===========================================================================
function InitTrig_ForsacenStarrt()
    gg_trg_ForsacenStarrt=CreateTrigger()
    TriggerRegisterTimerEventSingle(gg_trg_ForsacenStarrt, 0.01)
    TriggerAddAction(gg_trg_ForsacenStarrt, Trig_ForsacenStarrt_Actions)
end
--===========================================================================
-- Trigger: Ult
--===========================================================================
function Trig_Ult_Actions()
    local loc= GetSpellTargetLoc()
    local i= GetRandomInt(1, 4)
    
    if i == 1 then
        CreateItem(FourCC('I01X'), GetLocationX(loc), GetLocationY(loc))
    elseif i == 2 then
        CreateItem(FourCC('I01V'), GetLocationX(loc), GetLocationY(loc))
    elseif i == 3 then
        CreateItem(FourCC('I01Y'), GetLocationX(loc), GetLocationY(loc))
    else
        CreateItem(FourCC('I01W'), GetLocationX(loc), GetLocationY(loc))
    end
    
    RemoveLocation(loc)
    loc=nil
end
--===========================================================================
function InitTrig_Ult()
    gg_trg_Ult=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_Ult, EVENT_PLAYER_UNIT_SPELL_EFFECT)
    TriggerAddAction(gg_trg_Ult, function()
        if GetSpellAbilityId() ~= FourCC('A15B') then return end
        Trig_Ult_Actions()
    end)
end
--===========================================================================
-- Trigger: Banshe
--===========================================================================
function Trig_Banshe_Actions()
    local g= CreateGroup()
    local u
    local i= 0
    local l= GetSpellTargetLoc()
    SetUnitPositionLoc(GetTriggerUnit(), l)
    IssueImmediateOrder(GetTriggerUnit(), "metamorphosis")
    GroupEnumUnitsInRangeOfLoc(g, l, 250, nil)
    BlzStartUnitAbilityCooldown(GetTriggerUnit(), FourCC('A15S'), 30)
    while true do
        u=FirstOfGroup(g)
        if u == nil then break end
        if GetOwningPlayer(u) ~= GetOwningPlayer(GetTriggerUnit()) then
            UnitDamageTargetBJ(GetTriggerUnit(), u, 225, ATTACK_TYPE_NORMAL, DAMAGE_TYPE_DEATH)
        end
        GroupRemoveUnit(g, u)
        u=nil
    end
    DestroyGroup(g)
    RemoveLocation(l)
    l=nil
    g=nil
    u=nil
end
--===========================================================================
function InitTrig_Banshe()
    gg_trg_Banshe=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_Banshe, EVENT_PLAYER_UNIT_SPELL_EFFECT)
    TriggerAddAction(gg_trg_Banshe, function()
        if GetSpellAbilityId() ~= FourCC('A15S') then return end
        Trig_Banshe_Actions()
    end)
end
--===========================================================================
-- Trigger: BansheCop
--===========================================================================
function Trig_BansheCop_Actions()
    BlzStartUnitAbilityCooldown(GetTriggerUnit(), FourCC('A15S'), 30)
end
--===========================================================================
function InitTrig_BansheCop()
    gg_trg_BansheCop=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_BansheCop, EVENT_PLAYER_UNIT_SPELL_EFFECT)
    TriggerAddAction(gg_trg_BansheCop, function()
        if GetSpellAbilityId() ~= FourCC('A15T') then return end
        Trig_BansheCop_Actions()
    end)
end
--===========================================================================
-- Trigger: MassInvis
--===========================================================================
function MI2()
    return GetOwningPlayer(GetFilterUnit()) == udg_LocalPlayer
end
function Trig_MassInvis_Actions2()
    CreateNUnitsAtLoc(1, FourCC('H0BN'), GetOwningPlayer(GetTriggerUnit()), udg_LocalPosition2, bj_UNIT_FACING)
    
    RemoveUnitTimed(GetLastCreatedUnit() , 2)
    UnitAddAbilityBJ(FourCC('A159'), GetLastCreatedUnit())
    SetUnitManaBJ(GetLastCreatedUnit(), 1111111.00)
    --call SetUnitAbilityLevelSwapped( 'A159', GetLastCreatedUnit(), GetUnitAbilityLevelSwapped('A158', GetTriggerUnit()) )
    IssueTargetOrderBJ(GetLastCreatedUnit(), "invisibility", GetEnumUnit())
end
function Trig_MassInvis_Actions()
    udg_LocalPosition2=GetUnitLoc(GetTriggerUnit())
    udg_LocalPlayer=GetOwningPlayer(GetTriggerUnit())
    udg_Boolexpr = MI2
    GroupEnumUnitsInRangeOfLoc(udg_LocalOtrad2, udg_LocalPosition2, 650, udg_Boolexpr)
    RemoveLocation(udg_LocalPosition2)
    udg_LocalPosition2=GetUnitLoc(GetTriggerUnit())
    ForGroup(udg_LocalOtrad2, Trig_MassInvis_Actions2)
    RemoveLocation(udg_LocalPosition2)
    GroupClear(udg_LocalOtrad2)
end
--===========================================================================
function InitTrig_MassInvis()
    gg_trg_MassInvis=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_MassInvis, EVENT_PLAYER_UNIT_SPELL_EFFECT)
    TriggerAddAction(gg_trg_MassInvis, function()
        if GetSpellAbilityId() ~= FourCC('A158') then return end
        Trig_MassInvis_Actions()
    end)
end
--===========================================================================
-- Trigger: BansheeAuto
--===========================================================================
function Trig_BansheeAuto_Actions()
    IssueTargetOrderBJ(GetTriggerUnit(), "possession", GetSpellTargetUnit())
end
--===========================================================================
function InitTrig_BansheeAuto()
    gg_trg_BansheeAuto=CreateTrigger()
    DisableTrigger(gg_trg_BansheeAuto)
    TriggerRegisterAnyUnitEventBJ(gg_trg_BansheeAuto, EVENT_PLAYER_UNIT_SPELL_EFFECT)
    TriggerAddAction(gg_trg_BansheeAuto, function()
        if GetSpellAbilityId() ~= FourCC('A14P') then return end
        Trig_BansheeAuto_Actions()
    end)
end
--===========================================================================
-- Trigger: ResGmilDamage
--===========================================================================
function Trig_ResGmilDamage_Conditions()
    return GetResearched() == FourCC('R0FB')
end
function Trig_ResGmilDamage_Actions()
    SetPlayerTechResearchedSwap(FourCC('R0FW'), GetPlayerTechCountSimple(FourCC('R0FB'), GetOwningPlayer(GetTriggerUnit())), GetOwningPlayer(GetTriggerUnit()))
end
--===========================================================================
function InitTrig_ResGmilDamage()
    gg_trg_ResGmilDamage=CreateTrigger()
    DisableTrigger(gg_trg_ResGmilDamage)
    TriggerRegisterAnyUnitEventBJ(gg_trg_ResGmilDamage, EVENT_PLAYER_UNIT_RESEARCH_FINISH)
    TriggerAddCondition(gg_trg_ResGmilDamage, Condition(Trig_ResGmilDamage_Conditions))
    TriggerAddAction(gg_trg_ResGmilDamage, Trig_ResGmilDamage_Actions)
end
--===========================================================================
-- Trigger: Killing
--===========================================================================
function IsAndPlag()
    return GetUnitTypeId(GetFilterUnit()) == FourCC('o02Y')
end
function Trig_Killing_Actions()
    local u= GetTriggerUnit()
    local p= GetOwningPlayer(u)
    local g= CreateGroup()
    GroupEnumUnitsSelected(g, p, b)
    while true do
        u=FirstOfGroup(g)
        if u == nil then break end
        
        UnitRemoveAbility(u, FourCC('A13O'))
        UnitRemoveAbility(u, FourCC('A13N'))
        UnitAddAbility(u, FourCC('A13M'))
        BlzStartUnitAbilityCooldown(u, FourCC('A13M'), 12)
        BlzStartUnitAbilityCooldown(u, FourCC('A13K'), 45)
        GroupRemoveUnit(g, u)
        u=nil
    end
    
    
    DestroyGroup(g)
    g=nil
    p=nil
    u=nil
end
--===========================================================================
function InitTrig_Killing()
    gg_trg_Killing=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_Killing, EVENT_PLAYER_UNIT_SPELL_EFFECT)
    TriggerAddAction(gg_trg_Killing, function()
        if GetSpellAbilityId() ~= FourCC('A14C') then return end
        Trig_Killing_Actions()
    end)
end
--===========================================================================
-- Trigger: StartAttackKilling
--===========================================================================
function Trig_StartAttackKilling_Conditions()
    return GetUnitAbilityLevel(GetAttacker(), FourCC('A13M')) ~= 0 and ( BlzGetUnitAbilityCooldownRemaining(GetAttacker(), FourCC('A13M')) <= 0.00 )
end
function Trig_StartAttackKilling_Actions()
    local u= GetAttacker()
    UnitAddAbility(u, FourCC('A13T'))
    BlzStartUnitAbilityCooldown(u, FourCC('A13M'), 10.00)
end
--===========================================================================
function InitTrig_StartAttackKilling()
    gg_trg_StartAttackKilling=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_StartAttackKilling, EVENT_PLAYER_UNIT_ATTACKED)
    TriggerAddCondition(gg_trg_StartAttackKilling, Condition(Trig_StartAttackKilling_Conditions))
    TriggerAddAction(gg_trg_StartAttackKilling, Trig_StartAttackKilling_Actions)
end
--===========================================================================
-- Trigger: EndAttackKilling
--===========================================================================
function Trig_EndAttackKilling_Conditions()
    return GetUnitAbilityLevel(GetEventDamageSource(), FourCC('A13T')) > 0
end
function Trig_EndAttackKilling_Actions()
    UnitRemoveAbility(GetEventDamageSource(), FourCC('A13T'))
end
--===========================================================================
function InitTrig_EndAttackKilling()
    gg_trg_EndAttackKilling=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_EndAttackKilling, EVENT_PLAYER_UNIT_DAMAGED)
    TriggerAddCondition(gg_trg_EndAttackKilling, Condition(Trig_EndAttackKilling_Conditions))
    TriggerAddAction(gg_trg_EndAttackKilling, Trig_EndAttackKilling_Actions)
end
--===========================================================================
-- Trigger: Infect
--===========================================================================
function Trig_Infect_Actions()
    local u= GetTriggerUnit()
    local p= GetOwningPlayer(u)
    local g= CreateGroup()
    GroupEnumUnitsSelected(g, p, b)
    while true do
        u=FirstOfGroup(g)
        if u == nil then break end
        UnitRemoveAbility(u, FourCC('A13O'))
        UnitRemoveAbility(u, FourCC('A13M'))
        UnitAddAbility(u, FourCC('A13N'))
        BlzStartUnitAbilityCooldown(u, FourCC('A13N'), 12)
        BlzStartUnitAbilityCooldown(u, FourCC('A13K'), 45)
        GroupRemoveUnit(g, u)
        u=nil
    end
    
    DestroyGroup(g)
    g=nil
    p=nil
    u=nil
end
--===========================================================================
function InitTrig_Infect()
    gg_trg_Infect=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_Infect, EVENT_PLAYER_UNIT_SPELL_EFFECT)
    TriggerAddAction(gg_trg_Infect, function()
        if GetSpellAbilityId() ~= FourCC('A14E') then return end
        Trig_Infect_Actions()
    end)
end
--===========================================================================
-- Trigger: StartAttackInfect
--===========================================================================
function Trig_StartAttackInfect_Conditions()
    return GetUnitAbilityLevel(GetAttacker(), FourCC('A13N')) ~= 0 and ( BlzGetUnitAbilityCooldownRemaining(GetAttacker(), FourCC('A13N')) <= 0.00 )
end
function Trig_StartAttackInfect_Actions()
    local u= GetAttacker()
    UnitAddAbility(u, FourCC('A13S'))
    BlzStartUnitAbilityCooldown(u, FourCC('A13N'), 10.00)
end
--===========================================================================
function InitTrig_StartAttackInfect()
    gg_trg_StartAttackInfect=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_StartAttackInfect, EVENT_PLAYER_UNIT_ATTACKED)
    TriggerAddCondition(gg_trg_StartAttackInfect, Condition(Trig_StartAttackInfect_Conditions))
    TriggerAddAction(gg_trg_StartAttackInfect, Trig_StartAttackInfect_Actions)
end
--===========================================================================
-- Trigger: EndAttackInfect
--===========================================================================
function Trig_EndAttackInfect_Conditions()
    return GetUnitAbilityLevel(GetEventDamageSource(), FourCC('A13S')) > 0
end
function Trig_EndAttackInfect_Actions()
    UnitRemoveAbility(GetEventDamageSource(), FourCC('A13S'))
end
--===========================================================================
function InitTrig_EndAttackInfect()
    gg_trg_EndAttackInfect=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_EndAttackInfect, EVENT_PLAYER_UNIT_DAMAGED)
    TriggerAddCondition(gg_trg_EndAttackInfect, Condition(Trig_EndAttackInfect_Conditions))
    TriggerAddAction(gg_trg_EndAttackInfect, Trig_EndAttackInfect_Actions)
end
--===========================================================================
-- Trigger: Zagraz
--===========================================================================
function Trig_Zagraz_Actions()
    local u= GetTriggerUnit()
    local p= GetOwningPlayer(u)
    local g= CreateGroup()
    GroupEnumUnitsSelected(g, p, b)
    while true do
        u=FirstOfGroup(g)
        if u == nil then break end
        UnitRemoveAbility(u, FourCC('A13N'))
        UnitRemoveAbility(u, FourCC('A13M'))
        UnitAddAbility(u, FourCC('A13O'))
        BlzStartUnitAbilityCooldown(u, FourCC('A13O'), 12)
        BlzStartUnitAbilityCooldown(u, FourCC('A13K'), 45)
        GroupRemoveUnit(g, u)
        u=nil
    end
    
    DestroyGroup(g)
    g=nil
    p=nil
    u=nil
end
--===========================================================================
function InitTrig_Zagraz()
    gg_trg_Zagraz=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_Zagraz, EVENT_PLAYER_UNIT_SPELL_EFFECT)
    TriggerAddAction(gg_trg_Zagraz, function()
        if GetSpellAbilityId() ~= FourCC('A14D') then return end
        Trig_Zagraz_Actions()
    end)
end
--===========================================================================
-- Trigger: StartAttackZagraz
--===========================================================================
function Trig_StartAttackZagraz_Conditions()
    return GetUnitAbilityLevel(GetAttacker(), FourCC('A13O')) ~= 0 and ( BlzGetUnitAbilityCooldownRemaining(GetAttacker(), FourCC('A13O')) <= 0.00 )
end
function Trig_StartAttackZagraz_Actions()
    local u= GetAttacker()
    UnitAddAbility(u, FourCC('A13V'))
    BlzStartUnitAbilityCooldown(u, FourCC('A13V'), 10.00)
end
--===========================================================================
function InitTrig_StartAttackZagraz()
    gg_trg_StartAttackZagraz=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_StartAttackZagraz, EVENT_PLAYER_UNIT_ATTACKED)
    TriggerAddCondition(gg_trg_StartAttackZagraz, Condition(Trig_StartAttackZagraz_Conditions))
    TriggerAddAction(gg_trg_StartAttackZagraz, Trig_StartAttackZagraz_Actions)
end
--===========================================================================
-- Trigger: EndAttackZagraz
--===========================================================================
function Trig_EndAttackZagraz_Conditions()
    return GetUnitAbilityLevel(GetEventDamageSource(), FourCC('A13V')) > 0
end
function Trig_EndAttackZagraz_Actions()
    UnitRemoveAbility(GetEventDamageSource(), FourCC('A13V'))
end
--===========================================================================
function InitTrig_EndAttackZagraz()
    gg_trg_EndAttackZagraz=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_EndAttackZagraz, EVENT_PLAYER_UNIT_DAMAGED)
    TriggerAddCondition(gg_trg_EndAttackZagraz, Condition(Trig_EndAttackZagraz_Conditions))
    TriggerAddAction(gg_trg_EndAttackZagraz, Trig_EndAttackZagraz_Actions)
end
--===========================================================================
-- Trigger: StartAttackCorroz2
--===========================================================================
function Trig_StartAttackCorroz2_Conditions()
    return GetUnitTypeId(GetAttacker()) == FourCC('o02X')
end
function Trig_StartAttackCorroz2_Actions()
    local u= GetAttacker()
    if BlzGetUnitAbilityCooldownRemaining(u, FourCC('A13L')) == 0 or BlzGetUnitAbilityCooldownRemaining(u, FourCC('A13Q')) == 0 or BlzGetUnitAbilityCooldownRemaining(u, FourCC('A13F')) == 0 then
    
    else
        BlzUnitInterruptAttack(u)
    end
end
--===========================================================================
function InitTrig_StartAttackCorroz2()
    gg_trg_StartAttackCorroz2=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_StartAttackCorroz2, EVENT_PLAYER_UNIT_ATTACKED)
    TriggerAddCondition(gg_trg_StartAttackCorroz2, Condition(Trig_StartAttackCorroz2_Conditions))
    TriggerAddAction(gg_trg_StartAttackCorroz2, Trig_StartAttackCorroz2_Actions)
end
--===========================================================================
-- Trigger: Usual
--===========================================================================
function IsPlag()
    return GetUnitTypeId(GetFilterUnit()) == FourCC('o02X')
end
function Trig_Usual_Actions()
    local u= GetTriggerUnit()
    local p= GetOwningPlayer(u)
    local g= CreateGroup()
    GroupEnumUnitsSelected(g, p, b)
    while true do
        u=FirstOfGroup(g)
        if u == nil then break end
        UnitRemoveAbility(u, FourCC('A13P'))
        UnitRemoveAbility(u, FourCC('A13Q'))
        UnitAddAbility(u, FourCC('A13L'))
        BlzStartUnitAbilityCooldown(u, FourCC('A13L'), 19.5)
        BlzStartUnitAbilityCooldown(u, FourCC('A13J'), 45)
        u=nil
    end
    
    DestroyGroup(g)
    g=nil
    p=nil
    u=nil
        
end
--===========================================================================
function InitTrig_Usual()
    gg_trg_Usual=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_Usual, EVENT_PLAYER_UNIT_SPELL_EFFECT)
    TriggerAddAction(gg_trg_Usual, function()
        if GetSpellAbilityId() ~= FourCC('A142') then return end
        Trig_Usual_Actions()
    end)
end
--===========================================================================
-- Trigger: StartAttackUsual
--===========================================================================
function Trig_StartAttackUsual_Conditions()
    return GetUnitAbilityLevel(GetAttacker(), FourCC('A13L')) ~= 0 and ( BlzGetUnitAbilityCooldownRemaining(GetAttacker(), FourCC('A13L')) <= 0.00 )
end
function Trig_StartAttackUsual_Actions()
    local u= GetAttacker()
    UnitAddAbility(u, FourCC('A132'))
    BlzStartUnitAbilityCooldown(u, FourCC('A13L'), 10.00)
end
--===========================================================================
function InitTrig_StartAttackUsual()
    gg_trg_StartAttackUsual=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_StartAttackUsual, EVENT_PLAYER_UNIT_ATTACKED)
    TriggerAddCondition(gg_trg_StartAttackUsual, Condition(Trig_StartAttackUsual_Conditions))
    TriggerAddAction(gg_trg_StartAttackUsual, Trig_StartAttackUsual_Actions)
end
--===========================================================================
-- Trigger: EndAttackUsual
--===========================================================================
function Trig_EndAttackUsual_Conditions()
    return GetUnitAbilityLevel(GetEventDamageSource(), FourCC('A132')) > 0
end
function Trig_EndAttackUsual_Actions()
    UnitRemoveAbility(GetEventDamageSource(), FourCC('A132'))
end
--===========================================================================
function InitTrig_EndAttackUsual()
    gg_trg_EndAttackUsual=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_EndAttackUsual, EVENT_PLAYER_UNIT_DAMAGED)
    TriggerAddCondition(gg_trg_EndAttackUsual, Condition(Trig_EndAttackUsual_Conditions))
    TriggerAddAction(gg_trg_EndAttackUsual, Trig_EndAttackUsual_Actions)
end
--===========================================================================
-- Trigger: Korroz
--===========================================================================
function Trig_Korroz_Actions()
    local u= GetTriggerUnit()
    local p= GetOwningPlayer(u)
    local g= CreateGroup()
    GroupEnumUnitsSelected(g, p, b)
    while true do
        u=FirstOfGroup(g)
        if u == nil then break end
        UnitRemoveAbility(u, FourCC('A13L'))
        UnitRemoveAbility(u, FourCC('A13P'))
        UnitAddAbility(u, FourCC('A13Q'))
        BlzStartUnitAbilityCooldown(u, FourCC('A13Q'), 19.5)
        BlzStartUnitAbilityCooldown(u, FourCC('A13J'), 45)
        u=nil
    end
    
    DestroyGroup(g)
    g=nil
    p=nil
    u=nil
end
--===========================================================================
function InitTrig_Korroz()
    gg_trg_Korroz=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_Korroz, EVENT_PLAYER_UNIT_SPELL_EFFECT)
    TriggerAddAction(gg_trg_Korroz, function()
        if GetSpellAbilityId() ~= FourCC('A143') then return end
        Trig_Korroz_Actions()
    end)
end
--===========================================================================
-- Trigger: StartAttackCorroz
--===========================================================================
function Trig_StartAttackCorroz_Conditions()
    return GetUnitAbilityLevel(GetAttacker(), FourCC('A13Q')) ~= 0 and ( BlzGetUnitAbilityCooldownRemaining(GetAttacker(), FourCC('A13Q')) <= 0.00 )
end
function Trig_StartAttackCorroz_Actions()
    local u= GetAttacker()
    UnitAddAbility(u, FourCC('A13U'))
    UnitAddAbility(u, FourCC('A15H'))
    BlzStartUnitAbilityCooldown(u, FourCC('A13N'), 10.00)
end
--===========================================================================
function InitTrig_StartAttackCorroz()
    gg_trg_StartAttackCorroz=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_StartAttackCorroz, EVENT_PLAYER_UNIT_ATTACKED)
    TriggerAddCondition(gg_trg_StartAttackCorroz, Condition(Trig_StartAttackCorroz_Conditions))
    TriggerAddAction(gg_trg_StartAttackCorroz, Trig_StartAttackCorroz_Actions)
end
--===========================================================================
-- Trigger: EndAttackCorroz
--===========================================================================
function Trig_EndAttackCorroz_Conditions()
    return GetUnitAbilityLevel(GetEventDamageSource(), FourCC('A13U')) > 0
end
function Trig_EndAttackCorroz_Actions()
    UnitRemoveAbility(GetEventDamageSource(), FourCC('A13U'))
    UnitRemoveAbility(GetEventDamageSource(), FourCC('A15H'))
    
end
--===========================================================================
function InitTrig_EndAttackCorroz()
    gg_trg_EndAttackCorroz=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_EndAttackCorroz, EVENT_PLAYER_UNIT_DAMAGED)
    TriggerAddCondition(gg_trg_EndAttackCorroz, Condition(Trig_EndAttackCorroz_Conditions))
    TriggerAddAction(gg_trg_EndAttackCorroz, Trig_EndAttackCorroz_Actions)
end
--===========================================================================
-- Trigger: Safety
--===========================================================================
function Trig_Safety_Actions()
    local u= GetTriggerUnit()
    local p= GetOwningPlayer(u)
    local g= CreateGroup()
    GroupEnumUnitsSelected(g, p, b)
    while true do
        u=FirstOfGroup(g)
        if u == nil then break end
        UnitRemoveAbility(u, FourCC('A13L'))
        UnitRemoveAbility(u, FourCC('A13Q'))
        UnitAddAbility(u, FourCC('A13P'))
        BlzStartUnitAbilityCooldown(u, FourCC('A13P'), 19.5)
        BlzStartUnitAbilityCooldown(u, FourCC('A13J'), 45)
        u=nil
    end
    
    DestroyGroup(g)
    g=nil
    p=nil
    u=nil
end
--===========================================================================
function InitTrig_Safety()
    gg_trg_Safety=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_Safety, EVENT_PLAYER_UNIT_SPELL_EFFECT)
    TriggerAddAction(gg_trg_Safety, function()
        if GetSpellAbilityId() ~= FourCC('A144') then return end
        Trig_Safety_Actions()
    end)
end
--===========================================================================
-- Trigger: StartAttackSafety
--===========================================================================
function Trig_StartAttackSafety_Conditions()
    return GetUnitAbilityLevel(GetAttacker(), FourCC('A13P')) ~= 0 and ( BlzGetUnitAbilityCooldownRemaining(GetAttacker(), FourCC('A13P')) <= 0.00 )
end
function Trig_StartAttackSafety_Actions()
    local u= GetAttacker()
    UnitAddAbility(u, FourCC('A13R'))
    BlzStartUnitAbilityCooldown(u, FourCC('A13P'), 10.00)
end
--===========================================================================
function InitTrig_StartAttackSafety()
    gg_trg_StartAttackSafety=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_StartAttackSafety, EVENT_PLAYER_UNIT_ATTACKED)
    TriggerAddCondition(gg_trg_StartAttackSafety, Condition(Trig_StartAttackSafety_Conditions))
    TriggerAddAction(gg_trg_StartAttackSafety, Trig_StartAttackSafety_Actions)
end
--===========================================================================
-- Trigger: EndAttackSafety
--===========================================================================
function Trig_EndAttackSafety_Conditions()
    return GetUnitAbilityLevel(GetEventDamageSource(), FourCC('A13R')) > 0
end
function Trig_EndAttackSafety_Actions()
    UnitRemoveAbility(GetEventDamageSource(), FourCC('A13R'))
end
--===========================================================================
function InitTrig_EndAttackSafety()
    gg_trg_EndAttackSafety=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_EndAttackSafety, EVENT_PLAYER_UNIT_DAMAGED)
    TriggerAddCondition(gg_trg_EndAttackSafety, Condition(Trig_EndAttackSafety_Conditions))
    TriggerAddAction(gg_trg_EndAttackSafety, Trig_EndAttackSafety_Actions)
end
--===========================================================================
-- Trigger: MassMindControl2
--===========================================================================
function Trig_MassMindControl2_Func002002()
    return 0 == 0
end
function Trig_MassMindControl2_Func007A()
    CreateNUnitsAtLoc(1, FourCC('H0BN'), GetOwningPlayer(GetTriggerUnit()), udg_LocalPosition2, bj_UNIT_FACING)
    DisplayTextToForce(GetPlayersAll(), "TRIGSTR_27438")
    udg_LocalUnit2=GetLastCreatedUnit()
    TriggerExecute(gg_trg_ToKill2)
    UnitAddAbilityBJ(FourCC('A15V'), GetLastCreatedUnit())
    UnitAddAbilityBJ(FourCC('ACch'), GetLastCreatedUnit())
    SetUnitManaBJ(GetLastCreatedUnit(), 1111111.00)
    IssueTargetOrderBJ(GetLastCreatedUnit(), "charm", GetEnumUnit())
end
function Trig_MassMindControl2_Actions()
    udg_LocalPosition2=GetSpellTargetLoc()
    udg_Boolexpr = Trig_MassMindControl2_Func002002
    GroupEnumUnitsInRangeOfLoc(udg_LocalOtrad2, udg_LocalPosition2, 225, udg_Boolexpr)
    RemoveLocation(udg_LocalPosition2)
    udg_LocalPosition2=GetUnitLoc(GetTriggerUnit())
    ForGroupBJ(udg_LocalOtrad2, Trig_MassMindControl2_Func007A)
    RemoveLocation(udg_LocalPosition2)
    GroupClear(udg_LocalOtrad2)
end
--===========================================================================
function InitTrig_MassMindControl2()
    gg_trg_MassMindControl2=CreateTrigger()
    DisableTrigger(gg_trg_MassMindControl2)
    TriggerRegisterAnyUnitEventBJ(gg_trg_MassMindControl2, EVENT_PLAYER_UNIT_SPELL_EFFECT)
    TriggerAddAction(gg_trg_MassMindControl2, function()
        if GetSpellAbilityId() ~= FourCC('A15P') then return end
        Trig_MassMindControl2_Actions()
    end)
end
--===========================================================================
-- Trigger: ChangeOwner
--===========================================================================
function Trig_ChangeOwner_Actions()
    local u2= GetTriggerUnit()
    AddCountDis(u2 , GetPlayerId(GetOwningPlayer(u2)))
    DelCountDis(u2 , GetPlayerId(GetChangingUnitPrevOwner()))
end
--===========================================================================
function InitTrig_ChangeOwner()
    gg_trg_ChangeOwner=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_ChangeOwner, EVENT_PLAYER_UNIT_CHANGE_OWNER)
    TriggerAddAction(gg_trg_ChangeOwner, Trig_ChangeOwner_Actions)
end