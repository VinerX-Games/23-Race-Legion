
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