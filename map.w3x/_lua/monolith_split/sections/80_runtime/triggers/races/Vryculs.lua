
--===========================================================================
-- Trigger: InitLimitsVryculls
--===========================================================================
function Trig_InitLimitsVryculls_Func001A()
    SetPlayerTechMaxAllowed(GetEnumPlayer(), FourCC('wk01'), 0)
end
function Trig_InitLimitsVryculls_Actions()
    ForForce(udg_AllPlayers, Trig_InitLimitsVryculls_Func001A)
end
--===========================================================================
function InitTrig_InitLimitsVryculls()
    gg_trg_InitLimitsVryculls=CreateTrigger()
    TriggerRegisterTimerEventSingle(gg_trg_InitLimitsVryculls, 5)
    TriggerAddAction(gg_trg_InitLimitsVryculls, Trig_InitLimitsVryculls_Actions)
end
--===========================================================================
-- Trigger: Raiders
--===========================================================================
--function Random takes integer Chance, integer FromAll returns boolean 
  --  local integer i = GetRandomInt(1,FromAll)
    --return i<= Chance
--endfunction
function Trig_Raiders_Conditions()
    return GetUnitTypeId(GetTriggerUnit()) == FourCC('h0AE') and Random(1 , 5)
end
function Trig_Raiders_Actions()
    if Random(1 , 2) then
        CreateUnit(GetOwningPlayer(GetTriggerUnit()), FourCC('wk00'), GetUnitX(GetTriggerUnit()), GetUnitY(GetTriggerUnit()), 0.0)
    else
        CreateUnit(GetOwningPlayer(GetTriggerUnit()), FourCC('wk02'), GetUnitX(GetTriggerUnit()), GetUnitY(GetTriggerUnit()), 0.0)
    end
end
--===========================================================================
function InitTrig_Raiders()
    gg_trg_Raiders=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_Raiders, EVENT_PLAYER_UNIT_DEATH)
    TriggerAddCondition(gg_trg_Raiders, Condition(Trig_Raiders_Conditions))
    TriggerAddAction(gg_trg_Raiders, Trig_Raiders_Actions)
end
--===========================================================================
-- Trigger: km
--===========================================================================
function Trig_km_Conditions()
    return GetResearched() == FourCC('R067')
end
function Trig_km_Actions()
    SetPlayerTechMaxAllowedSwap(FourCC('R068'), 0, GetOwningPlayer(GetTriggerUnit()))
end
--===========================================================================
function InitTrig_km()
    gg_trg_km=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_km, EVENT_PLAYER_UNIT_RESEARCH_FINISH)
    TriggerRegisterAnyUnitEventBJ(gg_trg_km, EVENT_PLAYER_UNIT_RESEARCH_START)
    TriggerAddCondition(gg_trg_km, Condition(Trig_km_Conditions))
    TriggerAddAction(gg_trg_km, Trig_km_Actions)
end
--===========================================================================
-- Trigger: km2
--===========================================================================
function Trig_km2_Conditions()
    return GetResearched() == FourCC('R067')
end
function Trig_km2_Actions()
    SetPlayerTechMaxAllowedSwap(FourCC('R068'), 1, GetOwningPlayer(GetTriggerUnit()))
end
--===========================================================================
function InitTrig_km2()
    gg_trg_km2=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_km2, EVENT_PLAYER_UNIT_RESEARCH_CANCEL)
    TriggerAddCondition(gg_trg_km2, Condition(Trig_km2_Conditions))
    TriggerAddAction(gg_trg_km2, Trig_km2_Actions)
end
--===========================================================================
-- Trigger: Titan
--===========================================================================
function Trig_Titan_Conditions()
    return GetResearched() == FourCC('R068')
end
function Trig_Titan_Actions()
    SetPlayerTechMaxAllowedSwap(FourCC('R067'), 0, GetOwningPlayer(GetTriggerUnit()))
end
--===========================================================================
function InitTrig_Titan()
    gg_trg_Titan=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_Titan, EVENT_PLAYER_UNIT_RESEARCH_FINISH)
    TriggerRegisterAnyUnitEventBJ(gg_trg_Titan, EVENT_PLAYER_UNIT_RESEARCH_START)
    TriggerAddCondition(gg_trg_Titan, Condition(Trig_Titan_Conditions))
    TriggerAddAction(gg_trg_Titan, Trig_Titan_Actions)
end
--===========================================================================
-- Trigger: Titan2
--===========================================================================
function Trig_Titan2_Conditions()
    return GetResearched() == FourCC('R068')
end
function Trig_Titan2_Actions()
    SetPlayerTechMaxAllowedSwap(FourCC('R067'), 1, GetOwningPlayer(GetTriggerUnit()))
end
--===========================================================================
function InitTrig_Titan2()
    gg_trg_Titan2=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_Titan2, EVENT_PLAYER_UNIT_RESEARCH_CANCEL)
    TriggerAddCondition(gg_trg_Titan2, Condition(Trig_Titan2_Conditions))
    TriggerAddAction(gg_trg_Titan2, Trig_Titan2_Actions)
end
--===========================================================================
-- Trigger: IzeraSpell
--===========================================================================
function Trig_IzeraSpell_Actions()
   -- call BJDebugMsg("")
    MassSpell(GetTriggerUnit() , GetSpellAbilityId() , FourCC('A1MW') , "firebolt" , nil , 1000 , 1 , false)
end
--===========================================================================
function InitTrig_IzeraSpell()
    gg_trg_IzeraSpell=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_IzeraSpell, EVENT_PLAYER_UNIT_SPELL_EFFECT)
    TriggerAddAction(gg_trg_IzeraSpell, function()
        if GetSpellAbilityId() ~= FourCC('A1MX') then return end
        Trig_IzeraSpell_Actions()
    end)
end
--===========================================================================
-- Trigger: Navodnenie
--===========================================================================
function Trig_Navodnenie_Actions()
    UnitAddAbilityBJ(FourCC('A0R9'), GetTriggerUnit())
    TriggerSleepAction(25.00)
    UnitRemoveAbilityBJ(FourCC('A0R9'), GetTriggerUnit())
end
--===========================================================================
function InitTrig_Navodnenie()
    gg_trg_Navodnenie=CreateTrigger()
    DisableTrigger(gg_trg_Navodnenie)
    TriggerRegisterAnyUnitEventBJ(gg_trg_Navodnenie, EVENT_PLAYER_UNIT_SPELL_EFFECT)
    TriggerAddAction(gg_trg_Navodnenie, function()
        if GetSpellAbilityId() ~= FourCC('A0R8') then return end
        Trig_Navodnenie_Actions()
    end)
end