
--===========================================================================
-- Trigger: Red Orden
--===========================================================================
function Trig_Red_Orden_Conditions()
    return GetResearched() == FourCC('R040')
end
function Trig_Red_Orden_Actions()
    SetPlayerTechMaxAllowedSwap(FourCC('R03Z'), 0, GetOwningPlayer(GetTriggerUnit()))
end
--===========================================================================
function InitTrig_Red_Orden()
    gg_trg_Red_Orden=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_Red_Orden, EVENT_PLAYER_UNIT_RESEARCH_FINISH)
    TriggerRegisterAnyUnitEventBJ(gg_trg_Red_Orden, EVENT_PLAYER_UNIT_RESEARCH_START)
    TriggerAddCondition(gg_trg_Red_Orden, Condition(Trig_Red_Orden_Conditions))
    TriggerAddAction(gg_trg_Red_Orden, Trig_Red_Orden_Actions)
end
--===========================================================================
-- Trigger: Red Orden cansel
--===========================================================================
function Trig_Red_Orden_cansel_Conditions()
    return GetResearched() == FourCC('R040')
end
function Trig_Red_Orden_cansel_Actions()
    SetPlayerTechMaxAllowedSwap(FourCC('R03Z'), 1, GetOwningPlayer(GetTriggerUnit()))
end
--===========================================================================
function InitTrig_Red_Orden_cansel()
    gg_trg_Red_Orden_cansel=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_Red_Orden_cansel, EVENT_PLAYER_UNIT_RESEARCH_CANCEL)
    TriggerAddCondition(gg_trg_Red_Orden_cansel, Condition(Trig_Red_Orden_cansel_Conditions))
    TriggerAddAction(gg_trg_Red_Orden_cansel, Trig_Red_Orden_cansel_Actions)
end
--===========================================================================
-- Trigger: Red Onslaught
--===========================================================================
function Trig_Red_Onslaught_Conditions()
    return GetResearched() == FourCC('R03Z')
end
function Trig_Red_Onslaught_Actions()
    SetPlayerTechMaxAllowedSwap(FourCC('R040'), 0, GetOwningPlayer(GetTriggerUnit()))
end
--===========================================================================
function InitTrig_Red_Onslaught()
    gg_trg_Red_Onslaught=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_Red_Onslaught, EVENT_PLAYER_UNIT_RESEARCH_FINISH)
    TriggerRegisterAnyUnitEventBJ(gg_trg_Red_Onslaught, EVENT_PLAYER_UNIT_RESEARCH_START)
    TriggerAddCondition(gg_trg_Red_Onslaught, Condition(Trig_Red_Onslaught_Conditions))
    TriggerAddAction(gg_trg_Red_Onslaught, Trig_Red_Onslaught_Actions)
end
--===========================================================================
-- Trigger: Red Onslaught start
--===========================================================================
function Trig_Red_Onslaught_start_Conditions()
    return GetResearched() == FourCC('R03Z')
end
function Trig_Red_Onslaught_start_Actions()
    SetPlayerTechMaxAllowedSwap(FourCC('R040'), 1, GetOwningPlayer(GetTriggerUnit()))
end
--===========================================================================
function InitTrig_Red_Onslaught_start()
    gg_trg_Red_Onslaught_start=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_Red_Onslaught_start, EVENT_PLAYER_UNIT_RESEARCH_CANCEL)
    TriggerAddCondition(gg_trg_Red_Onslaught_start, Condition(Trig_Red_Onslaught_start_Conditions))
    TriggerAddAction(gg_trg_Red_Onslaught_start, Trig_Red_Onslaught_start_Actions)
end
--===========================================================================
-- Trigger: Short crossbow
--===========================================================================
function Trig_Short_crossbow_Conditions()
    return GetResearched() == FourCC('R03T')
end
function Trig_Short_crossbow_Actions()
    SetPlayerTechMaxAllowedSwap(FourCC('R03S'), 0, GetOwningPlayer(GetTriggerUnit()))
end
--===========================================================================
function InitTrig_Short_crossbow()
    gg_trg_Short_crossbow=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_Short_crossbow, EVENT_PLAYER_UNIT_RESEARCH_FINISH)
    TriggerAddCondition(gg_trg_Short_crossbow, Condition(Trig_Short_crossbow_Conditions))
    TriggerAddAction(gg_trg_Short_crossbow, Trig_Short_crossbow_Actions)
end
--===========================================================================
-- Trigger: AutocastFireArrows
--===========================================================================
function Trig_AutocastFireArrows_Conditions()
    return GetResearched() == FourCC('R03X') and GetPlayerTechCount(GetOwningPlayer(GetTriggerUnit()), FourCC('R03X'), true) == 2
end
function Trig_AutocastFireArrows_Actions()
    GlobalIssue(FourCC('h067') , GetOwningPlayer(GetTriggerUnit()) , "flamingarrows")
    GlobalIssue(FourCC('n008') , GetOwningPlayer(GetTriggerUnit()) , "flamingarrows")
end
--===========================================================================
function InitTrig_AutocastFireArrows()
    gg_trg_AutocastFireArrows=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_AutocastFireArrows, EVENT_PLAYER_UNIT_RESEARCH_FINISH)
    TriggerAddCondition(gg_trg_AutocastFireArrows, Condition(Trig_AutocastFireArrows_Conditions))
    TriggerAddAction(gg_trg_AutocastFireArrows, Trig_AutocastFireArrows_Actions)
end
--===========================================================================
-- Trigger: AutocastInnerFire
--===========================================================================
function Trig_AutocastInnerFire_Conditions()
    return GetResearched() == FourCC('R03Y') and GetPlayerTechCount(GetOwningPlayer(GetTriggerUnit()), FourCC('R03Y'), true) == 2
end
function Trig_AutocastInnerFire_Actions()
    GlobalIssue(FourCC('h067') , GetOwningPlayer(GetTriggerUnit()) , "innerfireon")
    --call GlobalIssue('n008', GetOwningPlayer(GetTriggerUnit()), "flamingarrows")
end
--===========================================================================
function InitTrig_AutocastInnerFire()
    gg_trg_AutocastInnerFire=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_AutocastInnerFire, EVENT_PLAYER_UNIT_RESEARCH_FINISH)
    TriggerAddCondition(gg_trg_AutocastInnerFire, Condition(Trig_AutocastInnerFire_Conditions))
    TriggerAddAction(gg_trg_AutocastInnerFire, Trig_AutocastInnerFire_Actions)
end
--===========================================================================
-- Trigger: Long crossbow
--===========================================================================
function Trig_Long_crossbow_Conditions()
    return GetResearched() == FourCC('R03S')
end
function Trig_Long_crossbow_Actions()
    SetPlayerTechMaxAllowedSwap(FourCC('R03T'), 0, GetOwningPlayer(GetTriggerUnit()))
end
--===========================================================================
function InitTrig_Long_crossbow()
    gg_trg_Long_crossbow=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_Long_crossbow, EVENT_PLAYER_UNIT_RESEARCH_FINISH)
    TriggerAddCondition(gg_trg_Long_crossbow, Condition(Trig_Long_crossbow_Conditions))
    TriggerAddAction(gg_trg_Long_crossbow, Trig_Long_crossbow_Actions)
end
--===========================================================================
-- Trigger: Auto hil Copy 2
--===========================================================================
function Trig_Auto_hil_Copy_2_Actions()
    IssueTargetOrderBJ(GetTriggerUnit(), "holybolt", GetSpellTargetUnit())
end
--===========================================================================
function InitTrig_Auto_hil_Copy_2()
    gg_trg_Auto_hil_Copy_2=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_Auto_hil_Copy_2, EVENT_PLAYER_UNIT_SPELL_EFFECT)
    TriggerAddAction(gg_trg_Auto_hil_Copy_2, function()
        if GetSpellAbilityId() ~= FourCC('A08X') then return end
        Trig_Auto_hil_Copy_2_Actions()
    end)
end
--===========================================================================
-- Trigger: Red korotkiy2
--===========================================================================
function Trig_Red_korotkiy2_Conditions()
    return GetResearched() == FourCC('R03T')
end
function Trig_Red_korotkiy2_Actions()
    SetPlayerTechMaxAllowedSwap(FourCC('R03S'), 1, GetOwningPlayer(GetTriggerUnit()))
end
--===========================================================================
function InitTrig_Red_korotkiy2()
    gg_trg_Red_korotkiy2=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_Red_korotkiy2, EVENT_PLAYER_UNIT_RESEARCH_CANCEL)
    TriggerAddCondition(gg_trg_Red_korotkiy2, Condition(Trig_Red_korotkiy2_Conditions))
    TriggerAddAction(gg_trg_Red_korotkiy2, Trig_Red_korotkiy2_Actions)
end
--===========================================================================
-- Trigger: Red dlinarbalet
--===========================================================================
function Trig_Red_dlinarbalet_Conditions()
    return GetResearched() == FourCC('R03S')
end
function Trig_Red_dlinarbalet_Actions()
    SetPlayerTechMaxAllowedSwap(FourCC('R03T'), 0, GetOwningPlayer(GetTriggerUnit()))
end
--===========================================================================
function InitTrig_Red_dlinarbalet()
    gg_trg_Red_dlinarbalet=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_Red_dlinarbalet, EVENT_PLAYER_UNIT_RESEARCH_FINISH)
    TriggerRegisterAnyUnitEventBJ(gg_trg_Red_dlinarbalet, EVENT_PLAYER_UNIT_RESEARCH_START)
    TriggerAddCondition(gg_trg_Red_dlinarbalet, Condition(Trig_Red_dlinarbalet_Conditions))
    TriggerAddAction(gg_trg_Red_dlinarbalet, Trig_Red_dlinarbalet_Actions)
end
--===========================================================================
-- Trigger: Red dlinarbalet start
--===========================================================================
function Trig_Red_dlinarbalet_start_Conditions()
    return GetResearched() == FourCC('R03S')
end
function Trig_Red_dlinarbalet_start_Actions()
    SetPlayerTechMaxAllowedSwap(FourCC('R03T'), 1, GetOwningPlayer(GetTriggerUnit()))
end
--===========================================================================
function InitTrig_Red_dlinarbalet_start()
    gg_trg_Red_dlinarbalet_start=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_Red_dlinarbalet_start, EVENT_PLAYER_UNIT_RESEARCH_CANCEL)
    TriggerAddCondition(gg_trg_Red_dlinarbalet_start, Condition(Trig_Red_dlinarbalet_start_Conditions))
    TriggerAddAction(gg_trg_Red_dlinarbalet_start, Trig_Red_dlinarbalet_start_Actions)
end
--===========================================================================
-- Trigger: Red korotkiy
--===========================================================================
function Trig_Red_korotkiy_Conditions()
    return GetResearched() == FourCC('R03T')
end
function Trig_Red_korotkiy_Actions()
    SetPlayerTechMaxAllowedSwap(FourCC('R03S'), 0, GetOwningPlayer(GetTriggerUnit()))
end
--===========================================================================
function InitTrig_Red_korotkiy()
    gg_trg_Red_korotkiy=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_Red_korotkiy, EVENT_PLAYER_UNIT_RESEARCH_FINISH)
    TriggerRegisterAnyUnitEventBJ(gg_trg_Red_korotkiy, EVENT_PLAYER_UNIT_RESEARCH_START)
    TriggerAddCondition(gg_trg_Red_korotkiy, Condition(Trig_Red_korotkiy_Conditions))
    TriggerAddAction(gg_trg_Red_korotkiy, Trig_Red_korotkiy_Actions)
end
--===========================================================================
-- Trigger: SpellMassSleep
--===========================================================================
function Trig_SpellMassSleep_Actions()
   -- call BJDebugMsg("")
    local l= GetSpellTargetLoc()
    MassSpell(GetTriggerUnit() , GetSpellAbilityId() , FourCC('A06O') , "sleep" , l , 175 , 1 , false)
    RemoveLocation(l)
end
--===========================================================================
function InitTrig_SpellMassSleep()
    gg_trg_SpellMassSleep=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_SpellMassSleep, EVENT_PLAYER_UNIT_SPELL_EFFECT)
    TriggerAddAction(gg_trg_SpellMassSleep, function()
        if GetSpellAbilityId() ~= FourCC('A06P') then return end
        Trig_SpellMassSleep_Actions()
    end)
end
--===========================================================================
-- Trigger: Ozaren
--===========================================================================
function Trig_Ozaren_Conditions()
    return GetResearched() == FourCC('R02R')
end
function Trig_Ozaren_Actions()
    SetPlayerTechMaxAllowedSwap(FourCC('R02Q'), 0, GetOwningPlayer(GetTriggerUnit()))
end
--===========================================================================
function InitTrig_Ozaren()
    gg_trg_Ozaren=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_Ozaren, EVENT_PLAYER_UNIT_RESEARCH_FINISH)
    TriggerRegisterAnyUnitEventBJ(gg_trg_Ozaren, EVENT_PLAYER_UNIT_RESEARCH_START)
    TriggerAddCondition(gg_trg_Ozaren, Condition(Trig_Ozaren_Conditions))
    TriggerAddAction(gg_trg_Ozaren, Trig_Ozaren_Actions)
end
--===========================================================================
-- Trigger: Ozaren2
--===========================================================================
function Trig_Ozaren2_Conditions()
    return GetResearched() == FourCC('R02R')
end
function Trig_Ozaren2_Actions()
    SetPlayerTechMaxAllowedSwap(FourCC('R02Q'), 1, GetOwningPlayer(GetTriggerUnit()))
end
--===========================================================================
function InitTrig_Ozaren2()
    gg_trg_Ozaren2=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_Ozaren2, EVENT_PLAYER_UNIT_RESEARCH_CANCEL)
    TriggerAddCondition(gg_trg_Ozaren2, Condition(Trig_Ozaren2_Conditions))
    TriggerAddAction(gg_trg_Ozaren2, Trig_Ozaren2_Actions)
end
--===========================================================================
-- Trigger: Slomlen
--===========================================================================
function Trig_Slomlen_Conditions()
    return GetResearched() == FourCC('R02Q')
end
function Trig_Slomlen_Actions()
    SetPlayerTechMaxAllowedSwap(FourCC('R02R'), 0, GetOwningPlayer(GetTriggerUnit()))
end
--===========================================================================
function InitTrig_Slomlen()
    gg_trg_Slomlen=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_Slomlen, EVENT_PLAYER_UNIT_RESEARCH_FINISH)
    TriggerRegisterAnyUnitEventBJ(gg_trg_Slomlen, EVENT_PLAYER_UNIT_RESEARCH_START)
    TriggerAddCondition(gg_trg_Slomlen, Condition(Trig_Slomlen_Conditions))
    TriggerAddAction(gg_trg_Slomlen, Trig_Slomlen_Actions)
end
--===========================================================================
-- Trigger: Slomlen2
--===========================================================================
function Trig_Slomlen2_Conditions()
    return GetResearched() == FourCC('R02Q')
end
function Trig_Slomlen2_Actions()
    SetPlayerTechMaxAllowedSwap(FourCC('R02R'), 1, GetOwningPlayer(GetTriggerUnit()))
end
--===========================================================================
function InitTrig_Slomlen2()
    gg_trg_Slomlen2=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_Slomlen2, EVENT_PLAYER_UNIT_RESEARCH_CANCEL)
    TriggerAddCondition(gg_trg_Slomlen2, Condition(Trig_Slomlen2_Conditions))
    TriggerAddAction(gg_trg_Slomlen2, Trig_Slomlen2_Actions)
end
--===========================================================================
-- Trigger: TP
--===========================================================================
function Trig_TP_Actions()
    IssuePointOrder(GetTriggerUnit(), "blink", GetSpellTargetX(), GetSpellTargetY())
end
--===========================================================================
function InitTrig_TP()
    gg_trg_TP=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_TP, EVENT_PLAYER_UNIT_SPELL_EFFECT)
    TriggerAddAction(gg_trg_TP, function()
        if GetSpellAbilityId() ~= FourCC('A1C4') then return end
        Trig_TP_Actions()
    end)
end
--===========================================================================
-- Trigger: NoDeath
--===========================================================================
function Trig_NoDeath_Conditions()
    return GetUnitAbilityLevel(GetTriggerUnit(), FourCC('A1C6')) ~= 0
end
function BrokenBuilding()
    return GetUnitTypeId(GetFilterUnit()) == FourCC('h05A')
end
function Trig_NoDeath_Actions()
    local g= CreateGroup()
    local u
    local u2
    GroupEnumUnitsOfPlayer(g, GetOwningPlayer(GetTriggerUnit()), Boolexpr)
    
    if Random(1 , 2) then
        u=FirstOfGroup(g)
        if u ~= nil then
            
            u2=CreateUnit(GetOwningPlayer(GetTriggerUnit()), GetUnitTypeId(GetTriggerUnit()), GetUnitX(u), GetUnitY(u), 0)
            SetUnitLifePercentBJ(u2, 10.00)
            RemoveUnit(GetTriggerUnit())
        end
        
        
    end
    --call ForGroupBJ( GetUnitsOfPlayerAndTypeId(Player(0), 'hfoo'), function Trig_NoDeath_Func001A )
    
    DestroyBoolExpr(Boolexpr)
    DestroyGroup(g)
    u=nil
    u2=nil
end
--===========================================================================
function InitTrig_NoDeath()
    gg_trg_NoDeath=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_NoDeath, EVENT_PLAYER_UNIT_DEATH)
    TriggerAddCondition(gg_trg_NoDeath, Condition(Trig_NoDeath_Conditions))
    TriggerAddAction(gg_trg_NoDeath, Trig_NoDeath_Actions)
end
--===========================================================================
-- Trigger: Masterstvo11
--===========================================================================
function Trig_Masterstvo11_Conditions()
    return GetResearched() == FourCC('R02J')
end
function Trig_Masterstvo11_Actions()
    SetPlayerTechMaxAllowedSwap(FourCC('R02K'), 0, GetOwningPlayer(GetTriggerUnit()))
end
--===========================================================================
function InitTrig_Masterstvo11()
    gg_trg_Masterstvo11=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_Masterstvo11, EVENT_PLAYER_UNIT_RESEARCH_FINISH)
    TriggerRegisterAnyUnitEventBJ(gg_trg_Masterstvo11, EVENT_PLAYER_UNIT_RESEARCH_START)
    TriggerAddCondition(gg_trg_Masterstvo11, Condition(Trig_Masterstvo11_Conditions))
    TriggerAddAction(gg_trg_Masterstvo11, Trig_Masterstvo11_Actions)
end
--===========================================================================
-- Trigger: Masterstvo12
--===========================================================================
function Trig_Masterstvo12_Conditions()
    return GetResearched() == FourCC('R02J')
end
function Trig_Masterstvo12_Actions()
    SetPlayerTechMaxAllowedSwap(FourCC('R02K'), 1, GetOwningPlayer(GetTriggerUnit()))
end
--===========================================================================
function InitTrig_Masterstvo12()
    gg_trg_Masterstvo12=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_Masterstvo12, EVENT_PLAYER_UNIT_RESEARCH_CANCEL)
    TriggerAddCondition(gg_trg_Masterstvo12, Condition(Trig_Masterstvo12_Conditions))
    TriggerAddAction(gg_trg_Masterstvo12, Trig_Masterstvo12_Actions)
end
--===========================================================================
-- Trigger: Slomlen Copy
--===========================================================================
function Trig_Slomlen_Copy_Conditions()
    return GetResearched() == FourCC('R02K')
end
function Trig_Slomlen_Copy_Actions()
    SetPlayerTechMaxAllowedSwap(FourCC('R02J'), 0, GetOwningPlayer(GetTriggerUnit()))
end
--===========================================================================
function InitTrig_Slomlen_Copy()
    gg_trg_Slomlen_Copy=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_Slomlen_Copy, EVENT_PLAYER_UNIT_RESEARCH_FINISH)
    TriggerRegisterAnyUnitEventBJ(gg_trg_Slomlen_Copy, EVENT_PLAYER_UNIT_RESEARCH_START)
    TriggerAddCondition(gg_trg_Slomlen_Copy, Condition(Trig_Slomlen_Copy_Conditions))
    TriggerAddAction(gg_trg_Slomlen_Copy, Trig_Slomlen_Copy_Actions)
end
--===========================================================================
-- Trigger: Slomlen2 Copy
--===========================================================================
function Trig_Slomlen2_Copy_Conditions()
    return GetResearched() == FourCC('R02K')
end
function Trig_Slomlen2_Copy_Actions()
    SetPlayerTechMaxAllowedSwap(FourCC('R02J'), 1, GetOwningPlayer(GetTriggerUnit()))
end
--===========================================================================
function InitTrig_Slomlen2_Copy()
    gg_trg_Slomlen2_Copy=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_Slomlen2_Copy, EVENT_PLAYER_UNIT_RESEARCH_CANCEL)
    TriggerAddCondition(gg_trg_Slomlen2_Copy, Condition(Trig_Slomlen2_Copy_Conditions))
    TriggerAddAction(gg_trg_Slomlen2_Copy, Trig_Slomlen2_Copy_Actions)
end
--===========================================================================
-- Trigger: Auto hil
--===========================================================================
function Trig_Auto_hil_Actions()
    IssueTargetOrderBJ(GetTriggerUnit(), "holybolt", GetSpellTargetUnit())
end
--===========================================================================
function InitTrig_Auto_hil()
    gg_trg_Auto_hil=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_Auto_hil, EVENT_PLAYER_UNIT_SPELL_EFFECT)
    TriggerAddAction(gg_trg_Auto_hil, function()
        if GetSpellAbilityId() ~= FourCC('A04Y') then return end
        Trig_Auto_hil_Actions()
    end)
end
--===========================================================================
-- Trigger: Auto hil Copy
--===========================================================================
function Trig_Auto_hil_Copy_Actions()
    IssueTargetOrderBJ(GetTriggerUnit(), "hex", GetSpellTargetUnit())
end
--===========================================================================
function InitTrig_Auto_hil_Copy()
    gg_trg_Auto_hil_Copy=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_Auto_hil_Copy, EVENT_PLAYER_UNIT_SPELL_EFFECT)
    TriggerAddAction(gg_trg_Auto_hil_Copy, function()
        if GetSpellAbilityId() ~= FourCC('A050') then return end
        Trig_Auto_hil_Copy_Actions()
    end)
end