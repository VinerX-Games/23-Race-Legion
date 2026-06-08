
--===========================================================================
-- Trigger: NagaStart
--===========================================================================
function NagaStartLimits_act()
    SetPlayerTechMaxAllowedSwap(FourCC('n054'), 0, GetEnumPlayer())
    SetPlayerTechMaxAllowedSwap(FourCC('n053'), 0, GetEnumPlayer())
    SetPlayerTechMaxAllowedSwap(FourCC('n052'), 0, GetEnumPlayer())
    SetPlayerTechMaxAllowedSwap(FourCC('n050'), 0, GetEnumPlayer())
    
    SetPlayerTechMaxAllowedSwap(FourCC('n051'), 0, GetEnumPlayer())
    SetPlayerTechMaxAllowedSwap(FourCC('n057'), 0, GetEnumPlayer())
    SetPlayerTechMaxAllowedSwap(FourCC('nnsw'), 0, GetEnumPlayer())
    SetPlayerTechMaxAllowedSwap(FourCC('nmyr'), 0, GetEnumPlayer())
    SetPlayerTechMaxAllowedSwap(FourCC('nnrg'), 0, GetEnumPlayer())
    
     SetPlayerTechMaxAllowedSwap(FourCC('N07A'), 1, GetEnumPlayer())
     
     SetPlayerTechMaxAllowedSwap(FourCC('H0OZ'), 0, GetEnumPlayer())
     SetPlayerTechMaxAllowedSwap(FourCC('H0JU'), 0, GetEnumPlayer()) --HERO
    SetPlayerTechMaxAllowedSwap(FourCC('H0JV'), 1, GetEnumPlayer())
 
    --Murloc Grades
    SetPlayerTechMaxAllowedSwap(FourCC('R0FQ'), 0, GetEnumPlayer())
    
end
function NagaStartLimits()
    ForForce(udg_AllPlayers, NagaStartLimits_act)
    ForForce(udg_Bots, NagaStartLimits_act)
end
function Trig_NagaStart_Actions()
    NagaStartLimits()
end
--===========================================================================
function InitTrig_NagaStart()
    gg_trg_NagaStart=CreateTrigger()
    TriggerRegisterTimerEventSingle(gg_trg_NagaStart, 2.00)
    TriggerAddAction(gg_trg_NagaStart, Trig_NagaStart_Actions)
end
--===========================================================================
-- Trigger: Coatl
--===========================================================================
function Trig_Coatl_Conditions()
    gUnit=GetTrainedUnit()
    return GetUnitTypeId(gUnit) == FourCC('nwgs')
end
function Trig_Coatl_Actions()
    UnitAddAbility(gUnit, FourCC('Aave'))
    SetUnitFlyHeightBJ(gUnit, 240.00, 1)
    UnitRemoveAbility(gUnit, FourCC('Aave'))
    
end
--===========================================================================
function InitTrig_Coatl()
    gg_trg_Coatl=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_Coatl, EVENT_PLAYER_UNIT_TRAIN_FINISH)
    TriggerAddCondition(gg_trg_Coatl, Condition(Trig_Coatl_Conditions))
    TriggerAddAction(gg_trg_Coatl, Trig_Coatl_Actions)
end
--===========================================================================
-- Trigger: MurlokCan
--===========================================================================
function Trig_MurlokCan_Conditions()
    return GetResearched() == FourCC('R0FF')
end
function Trig_MurlokCan_Actions()
    SetPlayerTechMaxAllowedSwap(FourCC('R0FE'), 1, GetOwningPlayer(GetTriggerUnit()))
end
--===========================================================================
function InitTrig_MurlokCan()
    gg_trg_MurlokCan=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_MurlokCan, EVENT_PLAYER_UNIT_RESEARCH_CANCEL)
    TriggerAddCondition(gg_trg_MurlokCan, Condition(Trig_MurlokCan_Conditions))
    TriggerAddAction(gg_trg_MurlokCan, Trig_MurlokCan_Actions)
end
--===========================================================================
-- Trigger: MurlokBeg
--===========================================================================
function Trig_MurlokBeg_Conditions()
    return GetResearched() == FourCC('R0FF')
end
function Trig_MurlokBeg_Actions()
    SetPlayerTechMaxAllowedSwap(FourCC('R0FE'), 0, GetOwningPlayer(GetTriggerUnit()))
end
--===========================================================================
function InitTrig_MurlokBeg()
    gg_trg_MurlokBeg=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_MurlokBeg, EVENT_PLAYER_UNIT_RESEARCH_START)
    TriggerAddCondition(gg_trg_MurlokBeg, Condition(Trig_MurlokBeg_Conditions))
    TriggerAddAction(gg_trg_MurlokBeg, Trig_MurlokBeg_Actions)
end
--===========================================================================
-- Trigger: MurlocFin
--===========================================================================
function Trig_MurlocFin_Conditions()
    return GetResearched() == FourCC('R0FF')
end
function Trig_MurlocFin_Actions()
    SetPlayerTechMaxAllowedSwap(FourCC('n053'), - 1, GetOwningPlayer(GetTriggerUnit()))
    SetPlayerTechMaxAllowedSwap(FourCC('n052'), - 1, GetOwningPlayer(GetTriggerUnit()))
    SetPlayerTechMaxAllowedSwap(FourCC('n050'), - 1, GetOwningPlayer(GetTriggerUnit()))
    SetPlayerTechMaxAllowedSwap(FourCC('n054'), - 1, GetOwningPlayer(GetTriggerUnit()))
    
    
    SetPlayerTechMaxAllowedSwap(FourCC('H0OZ'), 1, GetOwningPlayer(GetTriggerUnit())) --HERO TANK
    
    SetPlayerTechMaxAllowedSwap(FourCC('R0FQ'), 3, GetOwningPlayer(GetTriggerUnit()))
end
--===========================================================================
function InitTrig_MurlocFin()
    gg_trg_MurlocFin=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_MurlocFin, EVENT_PLAYER_UNIT_RESEARCH_FINISH)
    TriggerAddCondition(gg_trg_MurlocFin, Condition(Trig_MurlocFin_Conditions))
    TriggerAddAction(gg_trg_MurlocFin, Trig_MurlocFin_Actions)
end
--===========================================================================
-- Trigger: Nagi
--===========================================================================
function Trig_Nagi_Conditions()
    return GetResearched() == FourCC('R0FE')
end
function Trig_Nagi_Actions()
    SetPlayerTechMaxAllowedSwap(FourCC('R0FF'), 1, GetOwningPlayer(GetTriggerUnit()))
end
--===========================================================================
function InitTrig_Nagi()
    gg_trg_Nagi=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_Nagi, EVENT_PLAYER_UNIT_RESEARCH_CANCEL)
    TriggerAddCondition(gg_trg_Nagi, Condition(Trig_Nagi_Conditions))
    TriggerAddAction(gg_trg_Nagi, Trig_Nagi_Actions)
end
--===========================================================================
-- Trigger: Nagi2
--===========================================================================
function Trig_Nagi2_Conditions()
    return GetResearched() == FourCC('R0FE')
end
function Trig_Nagi2_Actions()
    SetPlayerTechMaxAllowedSwap(FourCC('R0FF'), 0, GetOwningPlayer(GetTriggerUnit()))
end
--===========================================================================
function InitTrig_Nagi2()
    gg_trg_Nagi2=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_Nagi2, EVENT_PLAYER_UNIT_RESEARCH_START)
    TriggerAddCondition(gg_trg_Nagi2, Condition(Trig_Nagi2_Conditions))
    TriggerAddAction(gg_trg_Nagi2, Trig_Nagi2_Actions)
end
--===========================================================================
-- Trigger: NagaFinishCode
--===========================================================================
function Trig_NagaFinishCode_Conditions()
    return GetResearched() == FourCC('R0FE')
end
function Trig_NagaFinishCode_Actions()
    SetPlayerTechMaxAllowedSwap(FourCC('n051'), - 1, GetOwningPlayer(GetTriggerUnit()))
    SetPlayerTechMaxAllowedSwap(FourCC('n057'), - 1, GetOwningPlayer(GetTriggerUnit()))
    SetPlayerTechMaxAllowedSwap(FourCC('nnsw'), - 1, GetOwningPlayer(GetTriggerUnit()))
    SetPlayerTechMaxAllowedSwap(FourCC('nmyr'), - 1, GetOwningPlayer(GetTriggerUnit()))
    SetPlayerTechMaxAllowedSwap(FourCC('nnrg'), - 1, GetOwningPlayer(GetTriggerUnit()))
    
    SetPlayerTechResearchedSwap(FourCC('R0KZ'), 1, GetOwningPlayer(GetTriggerUnit())) --Illidary or Nagi
    SetPlayerTechMaxAllowedSwap(FourCC('H0JU'), 1, GetOwningPlayer(GetTriggerUnit())) --HERO
end
--===========================================================================
function InitTrig_NagaFinishCode()
    gg_trg_NagaFinishCode=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_NagaFinishCode, EVENT_PLAYER_UNIT_RESEARCH_FINISH)
    TriggerAddCondition(gg_trg_NagaFinishCode, Condition(Trig_NagaFinishCode_Conditions))
    TriggerAddAction(gg_trg_NagaFinishCode, Trig_NagaFinishCode_Actions)
end
--===========================================================================
-- Trigger: VaishBuria
--===========================================================================
function Trig_VaishBuria_Actions()
    local loc= GetSpellTargetLoc()
    local u2= CreateUnitAtLoc(GetOwningPlayer(GetTriggerUnit()), FourCC('ntor'), loc, bj_UNIT_FACING)
    UnitApplyTimedLife(u2, FourCC('BTLF'), 30.00)
    u2=nil
    RemoveLocation(loc)
    loc=nil
end
--===========================================================================
function InitTrig_VaishBuria()
    gg_trg_VaishBuria=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_VaishBuria, EVENT_PLAYER_UNIT_SPELL_EFFECT)
    TriggerAddAction(gg_trg_VaishBuria, function()
        if GetSpellAbilityId() ~= FourCC('A16E') then return end
        Trig_VaishBuria_Actions()
    end)
end
--===========================================================================
-- Trigger: VaishArrow
--===========================================================================
function Trig_VaishArrow_Conditions()
    gTarget=BlzGetEventDamageTarget()
    gCaster=GetEventDamageSource()
    --call BJDebugMsg("Test1"+GetUnitName(gTarget)+GetUnitName(gCaster)+I2S(GetUnitAbilityLevel(gTarget, 'B06P'))+I2S(GetUnitAbilityLevel(gTarget, 'B06Q')) )
    --return GetUnitAbilityLevel(gTarget, 'B06P')>0 and GetUnitAbilityLevel(gTarget, 'B06Q')==0 
    return GetUnitAbilityLevel(gCaster, FourCC('A16C')) > 0 and BlzGetEventAttackType() == ATTACK_TYPE_NORMAL and Random(1 , 10)
end
function Trig_VaishArrow_Actions()
    --call BJDebugMsg("Test2"+GetUnitName(gTarget)+GetUnitName(gCaster))
    DummyCastTargetLevel(FourCC('A16D') , "frostnova" , gCaster , gTarget , GetUnitAbilityLevel(gCaster, FourCC('A16C')))
end
--===========================================================================
function InitTrig_VaishArrow()
    gg_trg_VaishArrow=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_VaishArrow, EVENT_PLAYER_UNIT_DAMAGED)
    TriggerAddCondition(gg_trg_VaishArrow, Condition(Trig_VaishArrow_Conditions))
    TriggerAddAction(gg_trg_VaishArrow, Trig_VaishArrow_Actions)
end
--===========================================================================
-- Trigger: NagaPas
--===========================================================================
function Trig_NagaPas_Conditions()
    return GetLearnedSkillBJ() == FourCC('A13A')
end
function Trig_NagaPas_Func002Func001Func002Func001C()
    return GetUnitAbilityLevelSwapped(FourCC('A13A'), GetTriggerUnit()) == 4
end
function Trig_NagaPas_Func002Func001Func002C()
    return GetUnitAbilityLevelSwapped(FourCC('A13A'), GetTriggerUnit()) == 3
end
function Trig_NagaPas_Func002Func001C()
    return GetUnitAbilityLevelSwapped(FourCC('A13A'), GetTriggerUnit()) == 2
end
function Trig_NagaPas_Func002C()
    return GetUnitAbilityLevelSwapped(FourCC('A13A'), GetTriggerUnit()) == 1
end
function Trig_NagaPas_Actions()
    if Trig_NagaPas_Func002C() then
        UnitAddAbilityBJ(FourCC('A136'), GetTriggerUnit())
    else
        if Trig_NagaPas_Func002Func001C() then
            UnitAddAbilityBJ(FourCC('A137'), GetTriggerUnit())
            UnitRemoveAbilityBJ(FourCC('A136'), GetTriggerUnit())
        else
            if Trig_NagaPas_Func002Func001Func002C() then
                UnitAddAbilityBJ(FourCC('A138'), GetTriggerUnit())
                UnitRemoveAbilityBJ(FourCC('A137'), GetTriggerUnit())
            else
                if Trig_NagaPas_Func002Func001Func002Func001C() then
                    UnitAddAbilityBJ(FourCC('A139'), GetTriggerUnit())
                    UnitRemoveAbilityBJ(FourCC('A138'), GetTriggerUnit())
                end
            end
        end
    end
end
--===========================================================================
function InitTrig_NagaPas()
    gg_trg_NagaPas=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_NagaPas, EVENT_PLAYER_HERO_SKILL)
    TriggerAddCondition(gg_trg_NagaPas, Condition(Trig_NagaPas_Conditions))
    TriggerAddAction(gg_trg_NagaPas, Trig_NagaPas_Actions)
end
--===========================================================================
-- Trigger: NagaCommonSpell
--===========================================================================
function Trig_NagaCommonSpell_Actions()
    UnitAddAbility(GetTriggerUnit(), FourCC('S00E'))
    RemoveAbilityTimed(GetTriggerUnit() , FourCC('S00E') , 180)
end
--===========================================================================
function InitTrig_NagaCommonSpell()
    gg_trg_NagaCommonSpell=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_NagaCommonSpell, EVENT_PLAYER_UNIT_SPELL_EFFECT)
    TriggerAddAction(gg_trg_NagaCommonSpell, function()
        if GetSpellAbilityId() ~= FourCC('A1LT') then return end
        if not (not IsTerrainPathable(GetUnitX(GetTriggerUnit()), GetUnitY(GetTriggerUnit()), PATHING_TYPE_FLOATABILITY)) then return end
        Trig_NagaCommonSpell_Actions()
    end)
end