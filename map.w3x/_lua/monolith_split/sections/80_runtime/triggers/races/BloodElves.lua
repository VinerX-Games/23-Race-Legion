
--===========================================================================
-- Trigger: BloodElvesOn
--===========================================================================
function Trig_BloodElvesOn_Actions()
    EnableTrigger(gg_trg_KaelMassAstral)
    --call EnableTrigger( gg_trg_LortemarAddArmor )
    EnableTrigger(gg_trg_LortemarArmorActive)
    EnableTrigger(gg_trg_Arcana)
    EnableTrigger(gg_trg_ArcanaBegin)
    EnableTrigger(gg_trg_ArcanaCansel)
    EnableTrigger(gg_trg_Fel)
    EnableTrigger(gg_trg_FelBegin)
    EnableTrigger(gg_trg_FelCansel)
    EnableTrigger(gg_trg_Void)
    EnableTrigger(gg_trg_VoidBegin)
    EnableTrigger(gg_trg_VoidCansel)
    EnableTrigger(gg_trg_Light)
    EnableTrigger(gg_trg_LightBegin)
    EnableTrigger(gg_trg_LightCansel)
    EnableTrigger(gg_trg_felspell2)
    EnableTrigger(gg_trg_voidspell111)
    EnableTrigger(gg_trg_lightspel)
    EnableTrigger(gg_trg_ArcanaBuild)
    EnableTrigger(gg_trg_FelBuild)
    EnableTrigger(gg_trg_VoidBuild)
    EnableTrigger(gg_trg_LigthBuild)
    
    
    EnableTrigger(gg_trg_FireShielDamageUniversal)
    
    EnableTrigger(gg_trg_Porcha)
    EnableTrigger(gg_trg_FirePodgogStrela)
    EnableTrigger(gg_trg_Souz)
    
    EnableTrigger(gg_trg_ArcanaIscachenie)
    EnableTrigger(gg_trg_ArcanaStrela)
    
    EnableTrigger(gg_trg_AutoMana)
    EnableTrigger(gg_trg_AutoStrelaFire)
    EnableTrigger(gg_trg_AutoStrelaArcana)
    EnableTrigger(gg_trg_AutoStrelaFel)
    EnableTrigger(gg_trg_AutoSummonGonch)
    
    EnableTrigger(gg_trg_FirePodgog)
    EnableTrigger(gg_trg_FirePodgogStrela2)
    EnableTrigger(gg_trg_VedmakF)
    EnableTrigger(gg_trg_VedmakB)
    EnableTrigger(gg_trg_VedmakC)
    
    EnableTrigger(gg_trg_MagsF)
    EnableTrigger(gg_trg_MagsB)
    EnableTrigger(gg_trg_MagsC)
    
    EnableTrigger(gg_trg_StrannikF)
    EnableTrigger(gg_trg_StrannikB)
    EnableTrigger(gg_trg_StrannikC)
    
    EnableTrigger(gg_trg_PaladinF)
    EnableTrigger(gg_trg_PaladinB)
    EnableTrigger(gg_trg_PaladinC)
    
    EnableTrigger(gg_trg_Manasbor)
    EnableTrigger(gg_trg_SpellMassSunAttack)
    EnableTrigger(gg_trg_LiadrinUlta)
    
end
--===========================================================================
function InitTrig_BloodElvesOn()
    gg_trg_BloodElvesOn=CreateTrigger()
    TriggerAddAction(gg_trg_BloodElvesOn, Trig_BloodElvesOn_Actions)
end
--===========================================================================
-- Trigger: Start Elves O
--===========================================================================
function Trig_Start_Elves_O_Func001A()
    SetPlayerAbilityAvailableBJ(false, FourCC('A05J'), GetEnumPlayer())
    SetPlayerAbilityAvailableBJ(false, FourCC('A05K'), GetEnumPlayer())
    -- -----------------------
    SetPlayerAbilityAvailableBJ(false, FourCC('A07K'), GetEnumPlayer())
    SetPlayerAbilityAvailableBJ(false, FourCC('A07L'), GetEnumPlayer())
    -- -----------------------
    SetPlayerAbilityAvailableBJ(false, FourCC('A07M'), GetEnumPlayer())
    SetPlayerAbilityAvailableBJ(false, FourCC('A07S'), GetEnumPlayer())
    SetPlayerAbilityAvailableBJ(false, FourCC('A07T'), GetEnumPlayer())
    -- -----------------------
    SetPlayerAbilityAvailableBJ(false, FourCC('A07D'), GetEnumPlayer())
    SetPlayerAbilityAvailableBJ(false, FourCC('A02G'), GetEnumPlayer())
    SetPlayerAbilityAvailableBJ(false, FourCC('A07O'), GetEnumPlayer())
    SetPlayerAbilityAvailableBJ(false, FourCC('A07N'), GetEnumPlayer())
    SetPlayerAbilityAvailableBJ(false, FourCC('A07P'), GetEnumPlayer())
    SetPlayerAbilityAvailableBJ(false, FourCC('A07Q'), GetEnumPlayer())
    -- -----------------------
    SetPlayerTechMaxAllowedSwap(FourCC('H043'), 1, GetEnumPlayer())
    SetPlayerTechMaxAllowedSwap(FourCC('H044'), 1, GetEnumPlayer())
    SetPlayerTechMaxAllowedSwap(FourCC('H05H'), 1, GetEnumPlayer())
    SetPlayerTechMaxAllowedSwap(FourCC('H05I'), 1, GetEnumPlayer())
    SetPlayerTechMaxAllowedSwap(FourCC('H045'), 1, GetEnumPlayer())
    SetPlayerTechMaxAllowedSwap(FourCC('Hjnd'), 1, GetEnumPlayer())
    SetPlayerTechMaxAllowedSwap(FourCC('Hkal'), 1, GetEnumPlayer())
    --????????? ???????
    SetPlayerTechMaxAllowedSwap(FourCC('h0O6'), 0, GetEnumPlayer())
end
function Trig_Start_Elves_O_Actions()
    ForForce(udg_AllPlayers, Trig_Start_Elves_O_Func001A)
end
--===========================================================================
function InitTrig_Start_Elves_O()
    gg_trg_Start_Elves_O=CreateTrigger()
    TriggerRegisterTimerEventSingle(gg_trg_Start_Elves_O, 5.00)
    TriggerAddAction(gg_trg_Start_Elves_O, Trig_Start_Elves_O_Actions)
end
--===========================================================================
-- Trigger: KaelMassAstral
--===========================================================================
function Trig_KaelMassAstral_Func007A()
    CreateNUnitsAtLoc(1, FourCC('H0BN'), GetOwningPlayer(GetTriggerUnit()), udg_LocalPosition2, bj_UNIT_FACING)
    UnitAddAbilityBJ(FourCC('AHbn'), GetLastCreatedUnit())
    SetUnitManaBJ(GetLastCreatedUnit(), 1111111.00)
    SetUnitAbilityLevelSwapped(FourCC('AHbn'), GetLastCreatedUnit(), GetUnitAbilityLevelSwapped(FourCC('A08R'), GetTriggerUnit()))
    IssueTargetOrderBJ(GetLastCreatedUnit(), "banish", GetEnumUnit())
    RemoveUnitTimed(GetLastCreatedUnit() , 3)
end
function Trig_KaelMassAstral_Actions()
    udg_LocalPosition2=GetSpellTargetLoc()
    udg_LocalPlayer=GetOwningPlayer(GetTriggerUnit())
    GroupEnumUnitsInRangeOfLoc(udg_LocalOtrad2, udg_LocalPosition2, 150, nil)
    RemoveLocation(udg_LocalPosition2)
    udg_LocalPosition2=GetUnitLoc(GetTriggerUnit())
    ForGroupBJ(udg_LocalOtrad2, Trig_KaelMassAstral_Func007A)
    RemoveLocation(udg_LocalPosition2)
    GroupClear(udg_LocalOtrad2)
end
--===========================================================================
function InitTrig_KaelMassAstral()
    gg_trg_KaelMassAstral=CreateTrigger()
    DisableTrigger(gg_trg_KaelMassAstral)
    TriggerRegisterAnyUnitEventBJ(gg_trg_KaelMassAstral, EVENT_PLAYER_UNIT_SPELL_EFFECT)
    TriggerAddAction(gg_trg_KaelMassAstral, function()
        if GetSpellAbilityId() ~= FourCC('A08R') then return end
        Trig_KaelMassAstral_Actions()
    end)
end
--===========================================================================
-- Trigger: LortemarArmorActive
--===========================================================================
function Trig_LortemarArmorActive_Actions()
    local u= GetTriggerUnit()
    UnitAddAbility(u, FourCC('A0DD'))
    UnitAddAbility(u, FourCC('ACmi'))
    
    RemoveAbilityTimed(u , FourCC('A0DD') , 20)
    RemoveAbilityTimed(u , FourCC('ACmi') , 20)
    u=nil
end
--===========================================================================
function InitTrig_LortemarArmorActive()
    gg_trg_LortemarArmorActive=CreateTrigger()
    DisableTrigger(gg_trg_LortemarArmorActive)
    TriggerRegisterAnyUnitEventBJ(gg_trg_LortemarArmorActive, EVENT_PLAYER_UNIT_SPELL_EFFECT)
    TriggerAddAction(gg_trg_LortemarArmorActive, function()
        if GetSpellAbilityId() ~= FourCC('A16M') then return end
        Trig_LortemarArmorActive_Actions()
    end)
end
--===========================================================================
-- Trigger: LiadrinUlta
--===========================================================================
function Trig_LiadrinUlta_Actions()
    local u= GetTriggerUnit()
    UnitAddAbility(u, FourCC('A1KV'))
    RemoveAbilityTimed(u , FourCC('A1KV') , 15)
    u=nil
end
--===========================================================================
function InitTrig_LiadrinUlta()
    gg_trg_LiadrinUlta=CreateTrigger()
    
    TriggerRegisterAnyUnitEventBJ(gg_trg_LiadrinUlta, EVENT_PLAYER_UNIT_SPELL_EFFECT)
    TriggerAddAction(gg_trg_LiadrinUlta, function()
        if GetSpellAbilityId() ~= FourCC('A1KU') then return end
        Trig_LiadrinUlta_Actions()
    end)
end
--===========================================================================
-- Trigger: SpellMassSunAttack
--===========================================================================
function Trig_SpellMassSunAttack_Actions()
    local l= GetSpellTargetLoc()
    local caster= GetTriggerUnit()
    local p= GetOwningPlayer(caster)
    --local boolexpr bex
    local dammyAbility= FourCC('A1KY')
    local level= GetUnitAbilityLevel(caster, GetSpellAbilityId())
    local g= CreateGroup()
    local u
    local u2
    local i= 0
    udg_LocalPlayer=p
    --set bex = Condition(function EnemEl) 
    GroupEnumUnitsInRangeOfLoc(g, l, 150, nil)
    
    if FirstOfGroup(g) == nil then
        --???? ??????
        BlzStartUnitAbilityCooldown(caster, dammyAbility, 15)
        SetUnitState(caster, UNIT_STATE_MANA, GetUnitState(caster, UNIT_STATE_MANA) + 100 + 35 * level)
        
    
    else
        RemoveLocation(l)
        l=GetUnitLoc(caster)
        while true do
            u=FirstOfGroup(g)
            if u == nil then break end
            
            u2=CreateUnitAtLoc(p, Dummy, l, bj_UNIT_FACING)
            
            if IsPlayerEnemy(GetOwningPlayer(u), p) then
                dammyAbility=FourCC('A1KZ')
            else
                dammyAbility=FourCC('A1KY')
            end
            
            UnitAddAbility(u2, dammyAbility)
            SetUnitAbilityLevel(u2, dammyAbility, level)
            
            if IsPlayerEnemy(GetOwningPlayer(u), p) then
                IssueTargetOrder(u2, "firebolt", u)
            else
                IssueTargetOrder(u2, "holybolt", u)
            end
            RemoveUnitTimed(u2 , 2)
            i=i + 1
            GroupRemoveUnit(g, u)
            u=nil
        end
    end
    
    u=nil
    DestroyGroup(g)
    g=nil
    RemoveLocation(l)
    p=nil
    --call
    u2=nil
    --set bex = null
end
--===========================================================================
function InitTrig_SpellMassSunAttack()
    gg_trg_SpellMassSunAttack=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_SpellMassSunAttack, EVENT_PLAYER_UNIT_SPELL_EFFECT)
    TriggerAddAction(gg_trg_SpellMassSunAttack, function()
        if GetSpellAbilityId() ~= FourCC('A1KX') then return end
        Trig_SpellMassSunAttack_Actions()
    end)
end
--===========================================================================
-- Trigger: Manasbor
--===========================================================================
function Trig_Manasbor_Conditions()
    gCaster=GetEventDamageSource()
    gTarget=GetEventTargetUnit()
    return GetUnitAbilityLevel(gCaster, FourCC('A1GR')) > 0
end
function Trig_Manasbor_Actions()
    local enemyMana= GetUnitState(GetTriggerUnit(), UNIT_STATE_MANA)
    local k= 0
    if IsUnitType(gTarget, UNIT_TYPE_HERO) then
        if enemyMana > 1 then
            k=1
        else
            return
        end
    else
        if enemyMana > 5 then
            k=5
        else
            return
        end
    end
    if gCaster ~= nil and UnitAlive(gCaster) then
        SetUnitState(gCaster, UNIT_STATE_MANA, RMaxBJ(0, GetUnitState(gCaster, UNIT_STATE_MANA) + k))
    end
end
--===========================================================================
function InitTrig_Manasbor()
    gg_trg_Manasbor=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_Manasbor, EVENT_PLAYER_UNIT_DAMAGING)
    TriggerAddCondition(gg_trg_Manasbor, Condition(Trig_Manasbor_Conditions))
    TriggerAddAction(gg_trg_Manasbor, Trig_Manasbor_Actions)
end
--===========================================================================
-- Trigger: ManaAura
--===========================================================================
function Trig_ManaAura_Conditions()
    return GetUnitTypeId(GetConstructedStructure()) == FourCC('h04F')
end
function Trig_ManaAura_Actions()
    UnitAddAbility(GetConstructedStructure(), FourCC('A1GT'))
end
--===========================================================================
function InitTrig_ManaAura()
    gg_trg_ManaAura=CreateTrigger()
    DisableTrigger(gg_trg_ManaAura)
    TriggerRegisterAnyUnitEventBJ(gg_trg_ManaAura, EVENT_PLAYER_UNIT_CONSTRUCT_FINISH)
    TriggerAddCondition(gg_trg_ManaAura, Condition(Trig_ManaAura_Conditions))
    TriggerAddAction(gg_trg_ManaAura, Trig_ManaAura_Actions)
end
--===========================================================================
-- Trigger: Arcana
--===========================================================================
function Trig_Arcana_Func009C()
    return (( GetResearched() == FourCC('R01D') )) and (( GetPlayerTechCountSimple(FourCC('R01D'), GetOwningPlayer(GetTriggerUnit())) == 3 ))
end
function Trig_Arcana_Conditions()
    return Trig_Arcana_Func009C()
end
function Trig_Arcana_Func002A()
    BlzSetUnitName(GetEnumUnit(), "cff8080ffr")
end
function Trig_Arcana_Actions()
    udg_LocalOtrad=GetUnitsOfPlayerAndTypeId(GetOwningPlayer(GetTriggerUnit()), FourCC('h04F'))
    ForGroupBJ(udg_LocalOtrad, Trig_Arcana_Func002A)
    DestroyGroup(udg_LocalOtrad)
    SetPlayerTechResearchedSwap(FourCC('R01E'), 1, GetOwningPlayer(GetTriggerUnit()))
    SetPlayerTechResearchedSwap(FourCC('R01F'), 1, GetOwningPlayer(GetTriggerUnit()))
    SetPlayerTechMaxAllowedSwap(FourCC('R01G'), 2, GetOwningPlayer(GetTriggerUnit()))
    SetPlayerTechMaxAllowedSwap(FourCC('R01H'), 2, GetOwningPlayer(GetTriggerUnit()))
    SetPlayerTechMaxAllowedSwap(FourCC('R01I'), 2, GetOwningPlayer(GetTriggerUnit()))
end
--===========================================================================
function InitTrig_Arcana()
    gg_trg_Arcana=CreateTrigger()
    DisableTrigger(gg_trg_Arcana)
    TriggerRegisterAnyUnitEventBJ(gg_trg_Arcana, EVENT_PLAYER_UNIT_RESEARCH_FINISH)
    TriggerAddCondition(gg_trg_Arcana, Condition(Trig_Arcana_Conditions))
    TriggerAddAction(gg_trg_Arcana, Trig_Arcana_Actions)
end
--===========================================================================
-- Trigger: ArcanaBegin
--===========================================================================
function Trig_ArcanaBegin_Func004C()
    return (( GetResearched() == FourCC('R01D') )) and (( GetPlayerTechCountSimple(FourCC('R01D'), GetOwningPlayer(GetTriggerUnit())) == 2 ))
end
function Trig_ArcanaBegin_Conditions()
    return Trig_ArcanaBegin_Func004C()
end
function Trig_ArcanaBegin_Actions()
    SetPlayerTechMaxAllowedSwap(FourCC('R01G'), 2, GetOwningPlayer(GetTriggerUnit()))
    SetPlayerTechMaxAllowedSwap(FourCC('R01H'), 2, GetOwningPlayer(GetTriggerUnit()))
    SetPlayerTechMaxAllowedSwap(FourCC('R01I'), 2, GetOwningPlayer(GetTriggerUnit()))
end
--===========================================================================
function InitTrig_ArcanaBegin()
    gg_trg_ArcanaBegin=CreateTrigger()
    DisableTrigger(gg_trg_ArcanaBegin)
    TriggerRegisterAnyUnitEventBJ(gg_trg_ArcanaBegin, EVENT_PLAYER_UNIT_RESEARCH_START)
    TriggerAddCondition(gg_trg_ArcanaBegin, Condition(Trig_ArcanaBegin_Conditions))
    TriggerAddAction(gg_trg_ArcanaBegin, Trig_ArcanaBegin_Actions)
end
--===========================================================================
-- Trigger: ArcanaCansel
--===========================================================================
function Trig_ArcanaCansel_Func004C()
    return (( GetResearched() == FourCC('R01D') )) and (( GetPlayerTechCountSimple(FourCC('R01D'), GetOwningPlayer(GetTriggerUnit())) == 2 ))
end
function Trig_ArcanaCansel_Conditions()
    return Trig_ArcanaCansel_Func004C()
end
function Trig_ArcanaCansel_Actions()
    SetPlayerTechMaxAllowedSwap(FourCC('R01G'), 3, GetOwningPlayer(GetTriggerUnit()))
    SetPlayerTechMaxAllowedSwap(FourCC('R01H'), 3, GetOwningPlayer(GetTriggerUnit()))
    SetPlayerTechMaxAllowedSwap(FourCC('R01I'), 3, GetOwningPlayer(GetTriggerUnit()))
end
--===========================================================================
function InitTrig_ArcanaCansel()
    gg_trg_ArcanaCansel=CreateTrigger()
    DisableTrigger(gg_trg_ArcanaCansel)
    TriggerRegisterAnyUnitEventBJ(gg_trg_ArcanaCansel, EVENT_PLAYER_UNIT_RESEARCH_CANCEL)
    TriggerAddCondition(gg_trg_ArcanaCansel, Condition(Trig_ArcanaCansel_Conditions))
    TriggerAddAction(gg_trg_ArcanaCansel, Trig_ArcanaCansel_Actions)
end
--===========================================================================
-- Trigger: Fel
--===========================================================================
function Trig_Fel_Func007C()
    return (( GetResearched() == FourCC('R01G') )) and (( GetPlayerTechCountSimple(FourCC('R01G'), GetOwningPlayer(GetTriggerUnit())) == 3 ))
end
function Trig_Fel_Conditions()
    return Trig_Fel_Func007C()
end
function Trig_Fel_Func002A()
    BlzSetUnitName(GetEnumUnit(), "cff80ff80r")
end
function Trig_Fel_Actions()
    udg_LocalOtrad=GetUnitsOfPlayerAndTypeId(GetOwningPlayer(GetTriggerUnit()), FourCC('h04F'))
    ForGroupBJ(udg_LocalOtrad, Trig_Fel_Func002A)
    DestroyGroup(udg_LocalOtrad)
    SetPlayerTechMaxAllowedSwap(FourCC('R01D'), 2, GetOwningPlayer(GetTriggerUnit()))
    SetPlayerTechMaxAllowedSwap(FourCC('R01H'), 2, GetOwningPlayer(GetTriggerUnit()))
    SetPlayerTechMaxAllowedSwap(FourCC('R01I'), 2, GetOwningPlayer(GetTriggerUnit()))
    SetPlayerTechMaxAllowedSwap(FourCC('h0O6'), - 1, GetOwningPlayer(GetTriggerUnit()))
    SetPlayerTechMaxAllowedSwap(FourCC('h03Z'), 0, GetOwningPlayer(GetTriggerUnit()))
end
--===========================================================================
function InitTrig_Fel()
    gg_trg_Fel=CreateTrigger()
    DisableTrigger(gg_trg_Fel)
    TriggerRegisterAnyUnitEventBJ(gg_trg_Fel, EVENT_PLAYER_UNIT_RESEARCH_FINISH)
    TriggerAddCondition(gg_trg_Fel, Condition(Trig_Fel_Conditions))
    TriggerAddAction(gg_trg_Fel, Trig_Fel_Actions)
end
--===========================================================================
-- Trigger: FelBegin
--===========================================================================
function Trig_FelBegin_Func004C()
    return (( GetResearched() == FourCC('R01G') )) and (( GetPlayerTechCountSimple(FourCC('R01G'), GetOwningPlayer(GetTriggerUnit())) == 2 ))
end
function Trig_FelBegin_Conditions()
    return Trig_FelBegin_Func004C()
end
function Trig_FelBegin_Actions()
    SetPlayerTechMaxAllowedSwap(FourCC('R01D'), 2, GetOwningPlayer(GetTriggerUnit()))
    SetPlayerTechMaxAllowedSwap(FourCC('R01H'), 2, GetOwningPlayer(GetTriggerUnit()))
    SetPlayerTechMaxAllowedSwap(FourCC('R01I'), 2, GetOwningPlayer(GetTriggerUnit()))
end
--===========================================================================
function InitTrig_FelBegin()
    gg_trg_FelBegin=CreateTrigger()
    DisableTrigger(gg_trg_FelBegin)
    TriggerRegisterAnyUnitEventBJ(gg_trg_FelBegin, EVENT_PLAYER_UNIT_RESEARCH_START)
    TriggerAddCondition(gg_trg_FelBegin, Condition(Trig_FelBegin_Conditions))
    TriggerAddAction(gg_trg_FelBegin, Trig_FelBegin_Actions)
end
--===========================================================================
-- Trigger: FelCansel
--===========================================================================
function Trig_FelCansel_Func004C()
    return (( GetResearched() == FourCC('R01G') )) and (( GetPlayerTechCountSimple(FourCC('R01G'), GetOwningPlayer(GetTriggerUnit())) == 2 ))
end
function Trig_FelCansel_Conditions()
    return Trig_FelCansel_Func004C()
end
function Trig_FelCansel_Actions()
    SetPlayerTechMaxAllowedSwap(FourCC('R01D'), 3, GetOwningPlayer(GetTriggerUnit()))
    SetPlayerTechMaxAllowedSwap(FourCC('R01H'), 3, GetOwningPlayer(GetTriggerUnit()))
    SetPlayerTechMaxAllowedSwap(FourCC('R01I'), 3, GetOwningPlayer(GetTriggerUnit()))
end
--===========================================================================
function InitTrig_FelCansel()
    gg_trg_FelCansel=CreateTrigger()
    DisableTrigger(gg_trg_FelCansel)
    TriggerRegisterAnyUnitEventBJ(gg_trg_FelCansel, EVENT_PLAYER_UNIT_RESEARCH_CANCEL)
    TriggerAddCondition(gg_trg_FelCansel, Condition(Trig_FelCansel_Conditions))
    TriggerAddAction(gg_trg_FelCansel, Trig_FelCansel_Actions)
end
--===========================================================================
-- Trigger: FelGolemStrike
--===========================================================================
function Trig_FelGolemStrike_Conditions()
    return GetUnitAbilityLevel(GetAttacker(), FourCC('A1LW')) == 1 and Random(1 , 20)
end
function Trig_FelGolemStrike_Actions()
    IssueTargetOrder(GetAttacker(), "forkedlightning", GetTriggerUnit())
end
--===========================================================================
function InitTrig_FelGolemStrike()
    gg_trg_FelGolemStrike=CreateTrigger()
    --call DisableTrigger( gg_trg_FelGolemStrike )
    TriggerRegisterAnyUnitEventBJ(gg_trg_FelGolemStrike, EVENT_PLAYER_UNIT_ATTACKED)
    TriggerAddCondition(gg_trg_FelGolemStrike, Condition(Trig_FelGolemStrike_Conditions))
    TriggerAddAction(gg_trg_FelGolemStrike, Trig_FelGolemStrike_Actions)
end
--===========================================================================
-- Trigger: Void
--===========================================================================
function Trig_Void_Func008C()
    return (( GetResearched() == FourCC('R01H') )) and (( GetPlayerTechCountSimple(FourCC('R01H'), GetOwningPlayer(GetTriggerUnit())) == 3 ))
end
function Trig_Void_Conditions()
    return Trig_Void_Func008C()
end
function Trig_Void_Func002A()
    BlzSetUnitName(GetEnumUnit(), "cffff00ffr")
end
function Trig_Void_Actions()
    udg_LocalOtrad=GetUnitsOfPlayerAndTypeId(GetOwningPlayer(GetTriggerUnit()), FourCC('h04F'))
    ForGroupBJ(udg_LocalOtrad, Trig_Void_Func002A)
    DestroyGroup(udg_LocalOtrad)
    SetPlayerTechMaxAllowedSwap(FourCC('R01D'), 2, GetOwningPlayer(GetTriggerUnit()))
    SetPlayerTechMaxAllowedSwap(FourCC('R01G'), 2, GetOwningPlayer(GetTriggerUnit()))
    SetPlayerTechMaxAllowedSwap(FourCC('R01I'), 2, GetOwningPlayer(GetTriggerUnit()))
    SetPlayerTechResearchedSwap(FourCC('R020'), 1, GetOwningPlayer(GetTriggerUnit()))
end
--===========================================================================
function InitTrig_Void()
    gg_trg_Void=CreateTrigger()
    DisableTrigger(gg_trg_Void)
    TriggerRegisterAnyUnitEventBJ(gg_trg_Void, EVENT_PLAYER_UNIT_RESEARCH_FINISH)
    TriggerAddCondition(gg_trg_Void, Condition(Trig_Void_Conditions))
    TriggerAddAction(gg_trg_Void, Trig_Void_Actions)
end
--===========================================================================
-- Trigger: VoidBegin
--===========================================================================
function Trig_VoidBegin_Func004C()
    return (( GetResearched() == FourCC('R01H') )) and (( GetPlayerTechCountSimple(FourCC('R01H'), GetOwningPlayer(GetTriggerUnit())) == 2 ))
end
function Trig_VoidBegin_Conditions()
    return Trig_VoidBegin_Func004C()
end
function Trig_VoidBegin_Actions()
    SetPlayerTechMaxAllowedSwap(FourCC('R01D'), 2, GetOwningPlayer(GetTriggerUnit()))
    SetPlayerTechMaxAllowedSwap(FourCC('R01G'), 2, GetOwningPlayer(GetTriggerUnit()))
    SetPlayerTechMaxAllowedSwap(FourCC('R01I'), 2, GetOwningPlayer(GetTriggerUnit()))
end
--===========================================================================
function InitTrig_VoidBegin()
    gg_trg_VoidBegin=CreateTrigger()
    DisableTrigger(gg_trg_VoidBegin)
    TriggerRegisterAnyUnitEventBJ(gg_trg_VoidBegin, EVENT_PLAYER_UNIT_RESEARCH_START)
    TriggerAddCondition(gg_trg_VoidBegin, Condition(Trig_VoidBegin_Conditions))
    TriggerAddAction(gg_trg_VoidBegin, Trig_VoidBegin_Actions)
end
--===========================================================================
-- Trigger: VoidCansel
--===========================================================================
function Trig_VoidCansel_Func004C()
    return (( GetResearched() == FourCC('R01H') )) and (( GetPlayerTechCountSimple(FourCC('R01H'), GetOwningPlayer(GetTriggerUnit())) == 2 ))
end
function Trig_VoidCansel_Conditions()
    return Trig_VoidCansel_Func004C()
end
function Trig_VoidCansel_Actions()
    SetPlayerTechMaxAllowedSwap(FourCC('R01D'), 3, GetOwningPlayer(GetTriggerUnit()))
    SetPlayerTechMaxAllowedSwap(FourCC('R01G'), 3, GetOwningPlayer(GetTriggerUnit()))
    SetPlayerTechMaxAllowedSwap(FourCC('R01I'), 3, GetOwningPlayer(GetTriggerUnit()))
end
--===========================================================================
function InitTrig_VoidCansel()
    gg_trg_VoidCansel=CreateTrigger()
    DisableTrigger(gg_trg_VoidCansel)
    TriggerRegisterAnyUnitEventBJ(gg_trg_VoidCansel, EVENT_PLAYER_UNIT_RESEARCH_CANCEL)
    TriggerAddCondition(gg_trg_VoidCansel, Condition(Trig_VoidCansel_Conditions))
    TriggerAddAction(gg_trg_VoidCansel, Trig_VoidCansel_Actions)
end
--===========================================================================
-- Trigger: LightBegin
--===========================================================================
function Trig_LightBegin_Func004C()
    return (( GetResearched() == FourCC('R01I') )) and (( GetPlayerTechCountSimple(FourCC('R01I'), GetOwningPlayer(GetTriggerUnit())) == 2 ))
end
function Trig_LightBegin_Conditions()
    return Trig_LightBegin_Func004C()
end
function Trig_LightBegin_Actions()
    SetPlayerTechMaxAllowedSwap(FourCC('R01D'), 2, GetOwningPlayer(GetTriggerUnit()))
    SetPlayerTechMaxAllowedSwap(FourCC('R01G'), 2, GetOwningPlayer(GetTriggerUnit()))
    SetPlayerTechMaxAllowedSwap(FourCC('R01H'), 2, GetOwningPlayer(GetTriggerUnit()))
end
--===========================================================================
function InitTrig_LightBegin()
    gg_trg_LightBegin=CreateTrigger()
    DisableTrigger(gg_trg_LightBegin)
    TriggerRegisterAnyUnitEventBJ(gg_trg_LightBegin, EVENT_PLAYER_UNIT_RESEARCH_START)
    TriggerAddCondition(gg_trg_LightBegin, Condition(Trig_LightBegin_Conditions))
    TriggerAddAction(gg_trg_LightBegin, Trig_LightBegin_Actions)
end
--===========================================================================
-- Trigger: LightCansel
--===========================================================================
function Trig_LightCansel_Func004C()
    return (( GetResearched() == FourCC('R01I') )) and (( GetPlayerTechCountSimple(FourCC('R01I'), GetOwningPlayer(GetTriggerUnit())) == 2 ))
end
function Trig_LightCansel_Conditions()
    return Trig_LightCansel_Func004C()
end
function Trig_LightCansel_Actions()
    SetPlayerTechMaxAllowedSwap(FourCC('R01D'), 3, GetOwningPlayer(GetTriggerUnit()))
    SetPlayerTechMaxAllowedSwap(FourCC('R01G'), 3, GetOwningPlayer(GetTriggerUnit()))
    SetPlayerTechMaxAllowedSwap(FourCC('R01H'), 3, GetOwningPlayer(GetTriggerUnit()))
end
--===========================================================================
function InitTrig_LightCansel()
    gg_trg_LightCansel=CreateTrigger()
    DisableTrigger(gg_trg_LightCansel)
    TriggerRegisterAnyUnitEventBJ(gg_trg_LightCansel, EVENT_PLAYER_UNIT_RESEARCH_CANCEL)
    TriggerAddCondition(gg_trg_LightCansel, Condition(Trig_LightCansel_Conditions))
    TriggerAddAction(gg_trg_LightCansel, Trig_LightCansel_Actions)
end
--===========================================================================
-- Trigger: Light
--===========================================================================
function Trig_Light_Func008C()
    return (( GetResearched() == FourCC('R01I') )) and (( GetPlayerTechCountSimple(FourCC('R01I'), GetOwningPlayer(GetTriggerUnit())) == 3 ))
end
function Trig_Light_Conditions()
    return Trig_Light_Func008C()
end
function Trig_Light_Func003A()
    BlzSetUnitName(GetEnumUnit(), "cffffff00r")
end
function Trig_Light_Actions()
    udg_LocalOtrad=GetUnitsOfPlayerAndTypeId(GetOwningPlayer(GetTriggerUnit()), FourCC('h04F'))
    ForGroupBJ(udg_LocalOtrad, Trig_Light_Func003A)
    DestroyGroup(udg_LocalOtrad)
    SetPlayerTechMaxAllowedSwap(FourCC('R01D'), 2, GetOwningPlayer(GetTriggerUnit()))
    SetPlayerTechMaxAllowedSwap(FourCC('R01G'), 2, GetOwningPlayer(GetTriggerUnit()))
    SetPlayerTechMaxAllowedSwap(FourCC('R01H'), 2, GetOwningPlayer(GetTriggerUnit()))
end
--===========================================================================
function InitTrig_Light()
    gg_trg_Light=CreateTrigger()
    DisableTrigger(gg_trg_Light)
    TriggerRegisterAnyUnitEventBJ(gg_trg_Light, EVENT_PLAYER_UNIT_RESEARCH_FINISH)
    TriggerAddCondition(gg_trg_Light, Condition(Trig_Light_Conditions))
    TriggerAddAction(gg_trg_Light, Trig_Light_Actions)
end
--===========================================================================
-- Trigger: ArcanaBuild
--===========================================================================
function Trig_ArcanaBuild_Func001C()
    return (( GetUnitTypeId(GetConstructedStructure()) == FourCC('h04F') )) and (( GetPlayerTechCountSimple(FourCC('R01D'), GetOwningPlayer(GetTriggerUnit())) == 3 ))
end
function Trig_ArcanaBuild_Conditions()
    return Trig_ArcanaBuild_Func001C()
end
function Trig_ArcanaBuild_Actions()
    BlzSetUnitName(GetTriggerUnit(), "cff8080ffr")
end
--===========================================================================
function InitTrig_ArcanaBuild()
    gg_trg_ArcanaBuild=CreateTrigger()
    DisableTrigger(gg_trg_ArcanaBuild)
    TriggerRegisterAnyUnitEventBJ(gg_trg_ArcanaBuild, EVENT_PLAYER_UNIT_CONSTRUCT_FINISH)
    TriggerAddCondition(gg_trg_ArcanaBuild, Condition(Trig_ArcanaBuild_Conditions))
    TriggerAddAction(gg_trg_ArcanaBuild, Trig_ArcanaBuild_Actions)
end
--===========================================================================
-- Trigger: FelBuild
--===========================================================================
function Trig_FelBuild_Func001C()
    return (( GetUnitTypeId(GetConstructedStructure()) == FourCC('h04F') )) and (( GetPlayerTechCountSimple(FourCC('R01G'), GetOwningPlayer(GetTriggerUnit())) == 3 ))
end
function Trig_FelBuild_Conditions()
    return Trig_FelBuild_Func001C()
end
function Trig_FelBuild_Actions()
    BlzSetUnitName(GetTriggerUnit(), "cff80ff80r")
end
--===========================================================================
function InitTrig_FelBuild()
    gg_trg_FelBuild=CreateTrigger()
    DisableTrigger(gg_trg_FelBuild)
    TriggerRegisterAnyUnitEventBJ(gg_trg_FelBuild, EVENT_PLAYER_UNIT_CONSTRUCT_FINISH)
    TriggerAddCondition(gg_trg_FelBuild, Condition(Trig_FelBuild_Conditions))
    TriggerAddAction(gg_trg_FelBuild, Trig_FelBuild_Actions)
end
--===========================================================================
-- Trigger: VoidBuild
--===========================================================================
function Trig_VoidBuild_Func001C()
    return (( GetUnitTypeId(GetConstructedStructure()) == FourCC('h04F') )) and (( GetPlayerTechCountSimple(FourCC('R01H'), GetOwningPlayer(GetTriggerUnit())) == 3 ))
end
function Trig_VoidBuild_Conditions()
    return Trig_VoidBuild_Func001C()
end
function Trig_VoidBuild_Actions()
    BlzSetUnitName(GetTriggerUnit(), "cffff00ffrr")
end
--===========================================================================
function InitTrig_VoidBuild()
    gg_trg_VoidBuild=CreateTrigger()
    DisableTrigger(gg_trg_VoidBuild)
    TriggerRegisterAnyUnitEventBJ(gg_trg_VoidBuild, EVENT_PLAYER_UNIT_CONSTRUCT_FINISH)
    TriggerAddCondition(gg_trg_VoidBuild, Condition(Trig_VoidBuild_Conditions))
    TriggerAddAction(gg_trg_VoidBuild, Trig_VoidBuild_Actions)
end
--===========================================================================
-- Trigger: LigthBuild
--===========================================================================
function Trig_LigthBuild_Func001C()
    return (( GetUnitTypeId(GetConstructedStructure()) == FourCC('h04F') )) and (( GetPlayerTechCountSimple(FourCC('R01I'), GetOwningPlayer(GetTriggerUnit())) == 3 ))
end
function Trig_LigthBuild_Conditions()
    return Trig_LigthBuild_Func001C()
end
function Trig_LigthBuild_Actions()
    BlzSetUnitName(GetTriggerUnit(), "cffffff00r")
end
--===========================================================================
function InitTrig_LigthBuild()
    gg_trg_LigthBuild=CreateTrigger()
    DisableTrigger(gg_trg_LigthBuild)
    TriggerRegisterAnyUnitEventBJ(gg_trg_LigthBuild, EVENT_PLAYER_UNIT_CONSTRUCT_FINISH)
    TriggerAddCondition(gg_trg_LigthBuild, Condition(Trig_LigthBuild_Conditions))
    TriggerAddAction(gg_trg_LigthBuild, Trig_LigthBuild_Actions)
end
--===========================================================================
-- Trigger: felspell
--===========================================================================
function Trig_felspell_Actions()
    if UnitAlive(GetSpellTargetUnit()) then
        UnitAddAbility(GetSpellTargetUnit(), FourCC('A1QZ'))
    end
end
--===========================================================================
function InitTrig_felspell()
    gg_trg_felspell=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_felspell, EVENT_PLAYER_UNIT_SPELL_EFFECT)
    TriggerAddAction(gg_trg_felspell, function()
        if GetSpellAbilityId() ~= FourCC('A02D') then return end
        if not (GetPlayerTechCount(GetOwningPlayer(GetTriggerUnit()), FourCC('R01G'), true) == 3 and GetUnitAbilityLevel(GetSpellTargetUnit(), FourCC('A1QZ')) < 1) then return end
        Trig_felspell_Actions()
    end)
end
--===========================================================================
-- Trigger: voidspell
--===========================================================================
function Trig_voidspell_Actions()
    if UnitAlive(GetSpellTargetUnit()) then
        UnitAddAbility(GetSpellTargetUnit(), FourCC('A1R0'))
    end
end
--===========================================================================
function InitTrig_voidspell()
    gg_trg_voidspell=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_voidspell, EVENT_PLAYER_UNIT_SPELL_EFFECT)
    TriggerAddAction(gg_trg_voidspell, function()
        if GetSpellAbilityId() ~= FourCC('A02D') then return end
        if not (GetPlayerTechCount(GetOwningPlayer(GetTriggerUnit()), FourCC('R01H'), true) == 3 and GetUnitAbilityLevel(GetSpellTargetUnit(), FourCC('A1R0')) < 1) then return end
        Trig_voidspell_Actions()
    end)
end
--===========================================================================
-- Trigger: lightspel
--===========================================================================
function Trig_lightspel_Actions()
    if UnitAlive(GetSpellTargetUnit()) then
        UnitAddAbility(GetSpellTargetUnit(), FourCC('A1R1'))
    end
end
--===========================================================================
function InitTrig_lightspel()
    gg_trg_lightspel=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_lightspel, EVENT_PLAYER_UNIT_SPELL_EFFECT)
    TriggerAddAction(gg_trg_lightspel, function()
        if GetSpellAbilityId() ~= FourCC('A02D') then return end
        if not (GetPlayerTechCount(GetOwningPlayer(GetTriggerUnit()), FourCC('R01I'), true) == 3 and GetUnitAbilityLevel(GetSpellTargetUnit(), FourCC('A1R1')) < 1) then return end
        Trig_lightspel_Actions()
    end)
end
--===========================================================================
-- Trigger: Porcha
--===========================================================================
function Trig_Porcha_Conditions()
    return GetUnitAbilityLevel(GetAttacker(), FourCC('A02X')) > 0
end
function Trig_Porcha_Actions()
    if Random(1 , 10) then
        UnitAddAbility(GetAttacker(), FourCC('A08I'))
        RemoveAbilityTimed(GetAttacker() , FourCC('A08I') , 9)
    end
end
--===========================================================================
function InitTrig_Porcha()
    gg_trg_Porcha=CreateTrigger()
    DisableTrigger(gg_trg_Porcha)
    TriggerRegisterAnyUnitEventBJ(gg_trg_Porcha, EVENT_PLAYER_UNIT_ATTACKED)
    TriggerAddCondition(gg_trg_Porcha, Condition(Trig_Porcha_Conditions))
    TriggerAddAction(gg_trg_Porcha, Trig_Porcha_Actions)
end
--===========================================================================
-- Trigger: FirePodgogStrela
--===========================================================================
function Trig_FirePodgogStrela_Conditions()
end
function Trig_FirePodgogStrela_Actions()
   
    UnitAddAbility(GetSpellTargetUnit(), FourCC('A08I'))
    RemoveAbilityTimed(GetSpellTargetUnit() , FourCC('A08I') , 9)
end
--===========================================================================
function InitTrig_FirePodgogStrela()
    gg_trg_FirePodgogStrela=CreateTrigger()
    DisableTrigger(gg_trg_FirePodgogStrela)
    TriggerRegisterAnyUnitEventBJ(gg_trg_FirePodgogStrela, EVENT_PLAYER_UNIT_SPELL_EFFECT)
    TriggerAddAction(gg_trg_FirePodgogStrela, function()
        if GetSpellAbilityId() ~= FourCC('A030') then return end
        if not Trig_FirePodgogStrela_Conditions() then return end
        Trig_FirePodgogStrela_Actions()
    end)
end
--===========================================================================
-- Trigger: Souz
--===========================================================================
function Trig_Souz_Actions()
    local u= GetSpellTargetUnit()
    UnitAddAbility(u, FourCC('A16H'))
    RemoveAbilityTimed(u , FourCC('A16H') , 60)
    u=nil
end
--===========================================================================
function InitTrig_Souz()
    gg_trg_Souz=CreateTrigger()
    DisableTrigger(gg_trg_Souz)
    TriggerRegisterAnyUnitEventBJ(gg_trg_Souz, EVENT_PLAYER_UNIT_SPELL_EFFECT)
    TriggerAddAction(gg_trg_Souz, function()
        if GetSpellAbilityId() ~= FourCC('A02Y') then return end
        if not (GetUnitAbilityLevel(GetSpellTargetUnit(), FourCC('A16H')) ~= 1) then return end
        Trig_Souz_Actions()
    end)
end
--===========================================================================
-- Trigger: ArcanaIscachenie
--===========================================================================
function Trig_ArcanaIscachenie_Conditions()
    return GetUnitAbilityLevel(GetAttacker(), FourCC('A02S')) > 0
end
function Trig_ArcanaIscachenie_Actions()
    if Random(1 , 10) then
        UnitAddAbility(GetTriggerUnit(), FourCC('A02T'))
        RemoveAbilityTimed(GetTriggerUnit() , FourCC('A02T') , 9)
    end
    
end
--===========================================================================
function InitTrig_ArcanaIscachenie()
    gg_trg_ArcanaIscachenie=CreateTrigger()
    DisableTrigger(gg_trg_ArcanaIscachenie)
    TriggerRegisterAnyUnitEventBJ(gg_trg_ArcanaIscachenie, EVENT_PLAYER_UNIT_ATTACKED)
    TriggerAddCondition(gg_trg_ArcanaIscachenie, Condition(Trig_ArcanaIscachenie_Conditions))
    TriggerAddAction(gg_trg_ArcanaIscachenie, Trig_ArcanaIscachenie_Actions)
end
--===========================================================================
-- Trigger: ArcanaStrela
--===========================================================================
function Trig_ArcanaStrela_Actions()
    UnitAddAbility(GetSpellTargetUnit(), FourCC('A02T'))
    RemoveAbilityTimed(GetSpellTargetUnit() , FourCC('A02T') , 9)
end
--===========================================================================
function InitTrig_ArcanaStrela()
    gg_trg_ArcanaStrela=CreateTrigger()
    DisableTrigger(gg_trg_ArcanaStrela)
    TriggerRegisterAnyUnitEventBJ(gg_trg_ArcanaStrela, EVENT_PLAYER_UNIT_SPELL_EFFECT)
    TriggerAddAction(gg_trg_ArcanaStrela, function()
        if GetSpellAbilityId() ~= FourCC('A02R') then return end
        if not (GetSpellAbilityId() == FourCC('A02G')) then return end
        Trig_ArcanaStrela_Actions()
    end)
end
--===========================================================================
-- Trigger: FirePodgog
--===========================================================================
function Trig_FirePodgog_Conditions()
    return GetUnitAbilityLevel(GetAttacker(), FourCC('A02N')) > 1
end
function Trig_FirePodgog_Actions()
    if Random(1 , 10) then
        UnitAddAbility(GetTriggerUnit(), FourCC('A02O'))
        RemoveAbilityTimed(GetTriggerUnit() , FourCC('A02O') , 10)
        UnitAddAbility(GetAttacker(), FourCC('A02Q'))
        RemoveAbilityTimed(GetAttacker() , FourCC('A02Q') , 10)
    end
end
--===========================================================================
function InitTrig_FirePodgog()
    gg_trg_FirePodgog=CreateTrigger()
    DisableTrigger(gg_trg_FirePodgog)
    TriggerRegisterAnyUnitEventBJ(gg_trg_FirePodgog, EVENT_PLAYER_UNIT_ATTACKED)
    TriggerAddCondition(gg_trg_FirePodgog, Condition(Trig_FirePodgog_Conditions))
    TriggerAddAction(gg_trg_FirePodgog, Trig_FirePodgog_Actions)
end
--===========================================================================
-- Trigger: FirePodgogStrela2
--===========================================================================
function Trig_FirePodgogStrela2_Conditions()
end
function Trig_FirePodgogStrela2_Actions()
    local u= GetSpellTargetUnit()
    UnitAddAbility(GetSpellTargetUnit(), FourCC('A02O'))
    UnitAddAbility(GetSpellTargetUnit(), FourCC('A02Q'))
    RemoveAbilityTimed(GetSpellTargetUnit() , FourCC('A02O') , 2)
    RemoveAbilityTimed(GetSpellTargetUnit() , FourCC('A02Q') , 2)
    u=nil
end
--===========================================================================
function InitTrig_FirePodgogStrela2()
    gg_trg_FirePodgogStrela2=CreateTrigger()
    DisableTrigger(gg_trg_FirePodgogStrela2)
    TriggerRegisterAnyUnitEventBJ(gg_trg_FirePodgogStrela2, EVENT_PLAYER_UNIT_SPELL_EFFECT)
    TriggerAddAction(gg_trg_FirePodgogStrela2, function()
        if GetSpellAbilityId() ~= FourCC('A07P') then return end
        if not Trig_FirePodgogStrela2_Conditions() then return end
        Trig_FirePodgogStrela2_Actions()
    end)
end
--===========================================================================
-- Trigger: AutoMana
--===========================================================================
function Trig_AutoMana_Actions()
    IssueTargetOrderBJ(GetTriggerUnit(), "drain", GetSpellTargetUnit())
end
--===========================================================================
function InitTrig_AutoMana()
    gg_trg_AutoMana=CreateTrigger()
    DisableTrigger(gg_trg_AutoMana)
    TriggerRegisterAnyUnitEventBJ(gg_trg_AutoMana, EVENT_PLAYER_UNIT_SPELL_EFFECT)
    TriggerAddAction(gg_trg_AutoMana, function()
        if GetSpellAbilityId() ~= FourCC('A02E') then return end
        Trig_AutoMana_Actions()
    end)
end
--===========================================================================
-- Trigger: AutoStrelaFire
--===========================================================================
function Trig_AutoStrelaFire_Func001C()
    return (( ( GetSpellAbilityId() == FourCC('A00W') ) )) or (( ( GetSpellAbilityId() == FourCC('A07Q') ) ))
end
function Trig_AutoStrelaFire_Conditions()
    return Trig_AutoStrelaFire_Func001C()
end
function Trig_AutoStrelaFire_Actions()
    IssueTargetOrderBJ(GetTriggerUnit(), "firebolt", GetSpellTargetUnit())
end
--===========================================================================
function InitTrig_AutoStrelaFire()
    gg_trg_AutoStrelaFire=CreateTrigger()
    DisableTrigger(gg_trg_AutoStrelaFire)
    TriggerRegisterAnyUnitEventBJ(gg_trg_AutoStrelaFire, EVENT_PLAYER_UNIT_SPELL_EFFECT)
    TriggerAddCondition(gg_trg_AutoStrelaFire, Condition(Trig_AutoStrelaFire_Conditions))
    TriggerAddAction(gg_trg_AutoStrelaFire, Trig_AutoStrelaFire_Actions)
end
--===========================================================================
-- Trigger: AutoStrelaArcana
--===========================================================================
function Trig_AutoStrelaArcana_Func001C()
    return (( ( GetSpellAbilityId() == FourCC('A07D') ) )) or (( ( GetSpellAbilityId() == FourCC('A02U') ) ))
end
function Trig_AutoStrelaArcana_Conditions()
    return Trig_AutoStrelaArcana_Func001C()
end
function Trig_AutoStrelaArcana_Actions()
    IssueTargetOrderBJ(GetTriggerUnit(), "firebolt", GetSpellTargetUnit())
end
--===========================================================================
function InitTrig_AutoStrelaArcana()
    gg_trg_AutoStrelaArcana=CreateTrigger()
    DisableTrigger(gg_trg_AutoStrelaArcana)
    TriggerRegisterAnyUnitEventBJ(gg_trg_AutoStrelaArcana, EVENT_PLAYER_UNIT_SPELL_EFFECT)
    TriggerAddCondition(gg_trg_AutoStrelaArcana, Condition(Trig_AutoStrelaArcana_Conditions))
    TriggerAddAction(gg_trg_AutoStrelaArcana, Trig_AutoStrelaArcana_Actions)
end
--===========================================================================
-- Trigger: AutoStrelaFel
--===========================================================================
function Trig_AutoStrelaFel_Func001C()
    return (( ( GetSpellAbilityId() == FourCC('A02Z') ) )) or (( ( GetSpellAbilityId() == FourCC('A07O') ) ))
end
function Trig_AutoStrelaFel_Conditions()
    return Trig_AutoStrelaFel_Func001C()
end
function Trig_AutoStrelaFel_Actions()
    IssueTargetOrderBJ(GetTriggerUnit(), "firebolt", GetSpellTargetUnit())
end
--===========================================================================
function InitTrig_AutoStrelaFel()
    gg_trg_AutoStrelaFel=CreateTrigger()
    DisableTrigger(gg_trg_AutoStrelaFel)
    TriggerRegisterAnyUnitEventBJ(gg_trg_AutoStrelaFel, EVENT_PLAYER_UNIT_SPELL_EFFECT)
    TriggerAddCondition(gg_trg_AutoStrelaFel, Condition(Trig_AutoStrelaFel_Conditions))
    TriggerAddAction(gg_trg_AutoStrelaFel, Trig_AutoStrelaFel_Actions)
end
--===========================================================================
-- Trigger: AutoSummonGonch
--===========================================================================
function Trig_AutoSummonGonch_Actions()
    IssueImmediateOrderBJ(GetTriggerUnit(), "waterelemental")
end
--===========================================================================
function InitTrig_AutoSummonGonch()
    gg_trg_AutoSummonGonch=CreateTrigger()
    DisableTrigger(gg_trg_AutoSummonGonch)
    TriggerRegisterAnyUnitEventBJ(gg_trg_AutoSummonGonch, EVENT_PLAYER_UNIT_SPELL_EFFECT)
    TriggerAddAction(gg_trg_AutoSummonGonch, function()
        if GetSpellAbilityId() ~= FourCC('A032') then return end
        Trig_AutoSummonGonch_Actions()
    end)
end
--===========================================================================
-- Trigger: VedmakF
--===========================================================================
function Trig_VedmakF_Conditions()
    return GetResearched() == FourCC('R025')
end
function Trig_VedmakF_Actions()
    SetPlayerTechResearchedSwap(FourCC('R026'), 0, GetOwningPlayer(GetTriggerUnit()))
    SetPlayerTechResearchedSwap(FourCC('R03C'), 0, GetOwningPlayer(GetTriggerUnit()))
    SetPlayerTechResearchedSwap(FourCC('R03D'), 0, GetOwningPlayer(GetTriggerUnit()))
    --                           
    SetPlayerAbilityAvailableBJ(true, FourCC('A05J'), GetOwningPlayer(GetTriggerUnit()))
    SetPlayerAbilityAvailableBJ(true, FourCC('A05K'), GetOwningPlayer(GetTriggerUnit()))
    SetPlayerAbilityAvailableBJ(false, FourCC('A049'), GetOwningPlayer(GetTriggerUnit()))
    SetPlayerAbilityAvailableBJ(false, FourCC('Asps'), GetOwningPlayer(GetTriggerUnit()))
    --                           
    SetPlayerAbilityAvailableBJ(false, FourCC('A07L'), GetOwningPlayer(GetTriggerUnit()))
    SetPlayerAbilityAvailableBJ(true, FourCC('A037'), GetOwningPlayer(GetTriggerUnit()))
    SetPlayerAbilityAvailableBJ(false, FourCC('A07K'), GetOwningPlayer(GetTriggerUnit()))
    --                           
    SetPlayerAbilityAvailableBJ(false, FourCC('A07P'), GetOwningPlayer(GetTriggerUnit()))
    SetPlayerAbilityAvailableBJ(false, FourCC('A07Q'), GetOwningPlayer(GetTriggerUnit()))
    SetPlayerAbilityAvailableBJ(false, FourCC('A07N'), GetOwningPlayer(GetTriggerUnit()))
    SetPlayerAbilityAvailableBJ(false, FourCC('A07O'), GetOwningPlayer(GetTriggerUnit()))
    SetPlayerAbilityAvailableBJ(false, FourCC('A02G'), GetOwningPlayer(GetTriggerUnit()))
    SetPlayerAbilityAvailableBJ(false, FourCC('A07D'), GetOwningPlayer(GetTriggerUnit()))
    --                           
    SetPlayerAbilityAvailableBJ(false, FourCC('A07M'), GetOwningPlayer(GetTriggerUnit()))
    SetPlayerAbilityAvailableBJ(false, FourCC('A07S'), GetOwningPlayer(GetTriggerUnit()))
    SetPlayerAbilityAvailableBJ(true, FourCC('A07R'), GetOwningPlayer(GetTriggerUnit()))
    SetPlayerAbilityAvailableBJ(false, FourCC('A07T'), GetOwningPlayer(GetTriggerUnit()))
    --                           
    SetPlayerAbilityAvailableBJ(true, FourCC('A02J'), GetOwningPlayer(GetTriggerUnit()))
    SetPlayerAbilityAvailableBJ(true, FourCC('A00W'), GetOwningPlayer(GetTriggerUnit()))
    SetPlayerAbilityAvailableBJ(true, FourCC('A030'), GetOwningPlayer(GetTriggerUnit()))
    SetPlayerAbilityAvailableBJ(true, FourCC('A02Z'), GetOwningPlayer(GetTriggerUnit()))
    SetPlayerAbilityAvailableBJ(true, FourCC('A02R'), GetOwningPlayer(GetTriggerUnit()))
    SetPlayerAbilityAvailableBJ(true, FourCC('A02G'), GetOwningPlayer(GetTriggerUnit()))
    --                           
    SetPlayerTechMaxAllowedSwap(FourCC('R026'), 1, GetOwningPlayer(GetTriggerUnit()))
    SetPlayerTechMaxAllowedSwap(FourCC('R03C'), 1, GetOwningPlayer(GetTriggerUnit()))
    SetPlayerTechMaxAllowedSwap(FourCC('R03D'), 1, GetOwningPlayer(GetTriggerUnit()))
end
--===========================================================================
function InitTrig_VedmakF()
    gg_trg_VedmakF=CreateTrigger()
    DisableTrigger(gg_trg_VedmakF)
    TriggerRegisterAnyUnitEventBJ(gg_trg_VedmakF, EVENT_PLAYER_UNIT_RESEARCH_FINISH)
    TriggerAddCondition(gg_trg_VedmakF, Condition(Trig_VedmakF_Conditions))
    TriggerAddAction(gg_trg_VedmakF, Trig_VedmakF_Actions)
end
--===========================================================================
-- Trigger: VedmakB
--===========================================================================
function Trig_VedmakB_Conditions()
    return GetResearched() == FourCC('R025')
end
function Trig_VedmakB_Actions()
    SetPlayerTechMaxAllowedSwap(FourCC('R026'), 0, GetOwningPlayer(GetTriggerUnit()))
    SetPlayerTechMaxAllowedSwap(FourCC('R03C'), 0, GetOwningPlayer(GetTriggerUnit()))
    SetPlayerTechMaxAllowedSwap(FourCC('R03D'), 0, GetOwningPlayer(GetTriggerUnit()))
end
--===========================================================================
function InitTrig_VedmakB()
    gg_trg_VedmakB=CreateTrigger()
    DisableTrigger(gg_trg_VedmakB)
    TriggerRegisterAnyUnitEventBJ(gg_trg_VedmakB, EVENT_PLAYER_UNIT_RESEARCH_START)
    TriggerAddCondition(gg_trg_VedmakB, Condition(Trig_VedmakB_Conditions))
    TriggerAddAction(gg_trg_VedmakB, Trig_VedmakB_Actions)
end
--===========================================================================
-- Trigger: VedmakC
--===========================================================================
function Trig_VedmakC_Conditions()
    return GetResearched() == FourCC('R025')
end
function Trig_VedmakC_Actions()
    SetPlayerTechMaxAllowedSwap(FourCC('R026'), 1, GetOwningPlayer(GetTriggerUnit()))
    SetPlayerTechMaxAllowedSwap(FourCC('R03C'), 1, GetOwningPlayer(GetTriggerUnit()))
    SetPlayerTechMaxAllowedSwap(FourCC('R03D'), 1, GetOwningPlayer(GetTriggerUnit()))
end
--===========================================================================
function InitTrig_VedmakC()
    gg_trg_VedmakC=CreateTrigger()
    DisableTrigger(gg_trg_VedmakC)
    TriggerRegisterAnyUnitEventBJ(gg_trg_VedmakC, EVENT_PLAYER_UNIT_RESEARCH_CANCEL)
    TriggerAddCondition(gg_trg_VedmakC, Condition(Trig_VedmakC_Conditions))
    TriggerAddAction(gg_trg_VedmakC, Trig_VedmakC_Actions)
end
--===========================================================================
-- Trigger: MagsF
--===========================================================================
function Trig_MagsF_Conditions()
    return GetResearched() == FourCC('R03D')
end
function Trig_MagsF_Actions()
    SetPlayerTechResearchedSwap(FourCC('R026'), 0, GetOwningPlayer(GetTriggerUnit()))
    SetPlayerTechResearchedSwap(FourCC('R03C'), 0, GetOwningPlayer(GetTriggerUnit()))
    SetPlayerTechResearchedSwap(FourCC('R025'), 0, GetOwningPlayer(GetTriggerUnit()))
    --                           
    SetPlayerAbilityAvailableBJ(false, FourCC('A05J'), GetOwningPlayer(GetTriggerUnit()))
    SetPlayerAbilityAvailableBJ(false, FourCC('A05K'), GetOwningPlayer(GetTriggerUnit()))
    SetPlayerAbilityAvailableBJ(true, FourCC('A049'), GetOwningPlayer(GetTriggerUnit()))
    SetPlayerAbilityAvailableBJ(true, FourCC('Asps'), GetOwningPlayer(GetTriggerUnit()))
    --                           
    SetPlayerAbilityAvailableBJ(false, FourCC('A07L'), GetOwningPlayer(GetTriggerUnit()))
    SetPlayerAbilityAvailableBJ(true, FourCC('A037'), GetOwningPlayer(GetTriggerUnit()))
    SetPlayerAbilityAvailableBJ(false, FourCC('A07K'), GetOwningPlayer(GetTriggerUnit()))
    --                           
    SetPlayerAbilityAvailableBJ(true, FourCC('A07P'), GetOwningPlayer(GetTriggerUnit()))
    SetPlayerAbilityAvailableBJ(true, FourCC('A07Q'), GetOwningPlayer(GetTriggerUnit()))
    SetPlayerAbilityAvailableBJ(true, FourCC('A07N'), GetOwningPlayer(GetTriggerUnit()))
    SetPlayerAbilityAvailableBJ(true, FourCC('A07O'), GetOwningPlayer(GetTriggerUnit()))
    SetPlayerAbilityAvailableBJ(true, FourCC('A02G'), GetOwningPlayer(GetTriggerUnit()))
    SetPlayerAbilityAvailableBJ(true, FourCC('A07D'), GetOwningPlayer(GetTriggerUnit()))
    --                           
    SetPlayerAbilityAvailableBJ(false, FourCC('A07M'), GetOwningPlayer(GetTriggerUnit()))
    SetPlayerAbilityAvailableBJ(false, FourCC('A07S'), GetOwningPlayer(GetTriggerUnit()))
    SetPlayerAbilityAvailableBJ(true, FourCC('A07R'), GetOwningPlayer(GetTriggerUnit()))
    SetPlayerAbilityAvailableBJ(false, FourCC('A07T'), GetOwningPlayer(GetTriggerUnit()))
    --                           
    SetPlayerAbilityAvailableBJ(false, FourCC('A02J'), GetOwningPlayer(GetTriggerUnit()))
    SetPlayerAbilityAvailableBJ(false, FourCC('A00W'), GetOwningPlayer(GetTriggerUnit()))
    SetPlayerAbilityAvailableBJ(false, FourCC('A030'), GetOwningPlayer(GetTriggerUnit()))
    SetPlayerAbilityAvailableBJ(false, FourCC('A02Z'), GetOwningPlayer(GetTriggerUnit()))
    SetPlayerAbilityAvailableBJ(false, FourCC('A02R'), GetOwningPlayer(GetTriggerUnit()))
    SetPlayerAbilityAvailableBJ(false, FourCC('A02U'), GetOwningPlayer(GetTriggerUnit()))
    --                           
    SetPlayerTechMaxAllowedSwap(FourCC('R026'), 1, GetOwningPlayer(GetTriggerUnit()))
    SetPlayerTechMaxAllowedSwap(FourCC('R03C'), 1, GetOwningPlayer(GetTriggerUnit()))
    SetPlayerTechMaxAllowedSwap(FourCC('R025'), 1, GetOwningPlayer(GetTriggerUnit()))
end
--===========================================================================
function InitTrig_MagsF()
    gg_trg_MagsF=CreateTrigger()
    DisableTrigger(gg_trg_MagsF)
    TriggerRegisterAnyUnitEventBJ(gg_trg_MagsF, EVENT_PLAYER_UNIT_RESEARCH_FINISH)
    TriggerAddCondition(gg_trg_MagsF, Condition(Trig_MagsF_Conditions))
    TriggerAddAction(gg_trg_MagsF, Trig_MagsF_Actions)
end
--===========================================================================
-- Trigger: MagsB
--===========================================================================
function Trig_MagsB_Conditions()
    return GetResearched() == FourCC('R03D')
end
function Trig_MagsB_Actions()
    SetPlayerTechMaxAllowedSwap(FourCC('R026'), 0, GetOwningPlayer(GetTriggerUnit()))
    SetPlayerTechMaxAllowedSwap(FourCC('R03C'), 0, GetOwningPlayer(GetTriggerUnit()))
    SetPlayerTechMaxAllowedSwap(FourCC('R025'), 0, GetOwningPlayer(GetTriggerUnit()))
end
--===========================================================================
function InitTrig_MagsB()
    gg_trg_MagsB=CreateTrigger()
    DisableTrigger(gg_trg_MagsB)
    TriggerRegisterAnyUnitEventBJ(gg_trg_MagsB, EVENT_PLAYER_UNIT_RESEARCH_START)
    TriggerAddCondition(gg_trg_MagsB, Condition(Trig_MagsB_Conditions))
    TriggerAddAction(gg_trg_MagsB, Trig_MagsB_Actions)
end
--===========================================================================
-- Trigger: MagsC
--===========================================================================
function Trig_MagsC_Conditions()
    return GetResearched() == FourCC('R03D')
end
function Trig_MagsC_Actions()
    SetPlayerTechMaxAllowedSwap(FourCC('R026'), 1, GetOwningPlayer(GetTriggerUnit()))
    SetPlayerTechMaxAllowedSwap(FourCC('R03C'), 1, GetOwningPlayer(GetTriggerUnit()))
    SetPlayerTechMaxAllowedSwap(FourCC('R025'), 1, GetOwningPlayer(GetTriggerUnit()))
end
--===========================================================================
function InitTrig_MagsC()
    gg_trg_MagsC=CreateTrigger()
    DisableTrigger(gg_trg_MagsC)
    TriggerRegisterAnyUnitEventBJ(gg_trg_MagsC, EVENT_PLAYER_UNIT_RESEARCH_CANCEL)
    TriggerAddCondition(gg_trg_MagsC, Condition(Trig_MagsC_Conditions))
    TriggerAddAction(gg_trg_MagsC, Trig_MagsC_Actions)
end
--===========================================================================
-- Trigger: StrannikF
--===========================================================================
function Trig_StrannikF_Conditions()
    return GetResearched() == FourCC('R03C')
end
function Trig_StrannikF_Actions()
    SetPlayerTechResearchedSwap(FourCC('R026'), 0, GetOwningPlayer(GetTriggerUnit()))
    SetPlayerTechResearchedSwap(FourCC('R03D'), 0, GetOwningPlayer(GetTriggerUnit()))
    SetPlayerTechResearchedSwap(FourCC('R025'), 0, GetOwningPlayer(GetTriggerUnit()))
    --                           
    SetPlayerAbilityAvailableBJ(false, FourCC('A05J'), GetOwningPlayer(GetTriggerUnit()))
    SetPlayerAbilityAvailableBJ(false, FourCC('A05K'), GetOwningPlayer(GetTriggerUnit()))
    SetPlayerAbilityAvailableBJ(true, FourCC('A049'), GetOwningPlayer(GetTriggerUnit()))
    SetPlayerAbilityAvailableBJ(true, FourCC('Asps'), GetOwningPlayer(GetTriggerUnit()))
    --                           
    SetPlayerAbilityAvailableBJ(false, FourCC('A07L'), GetOwningPlayer(GetTriggerUnit()))
    SetPlayerAbilityAvailableBJ(false, FourCC('A07K'), GetOwningPlayer(GetTriggerUnit()))
    SetPlayerAbilityAvailableBJ(true, FourCC('A037'), GetOwningPlayer(GetTriggerUnit()))
    --                           
    SetPlayerAbilityAvailableBJ(false, FourCC('A07P'), GetOwningPlayer(GetTriggerUnit()))
    SetPlayerAbilityAvailableBJ(false, FourCC('A07Q'), GetOwningPlayer(GetTriggerUnit()))
    SetPlayerAbilityAvailableBJ(false, FourCC('A07N'), GetOwningPlayer(GetTriggerUnit()))
    SetPlayerAbilityAvailableBJ(false, FourCC('A07O'), GetOwningPlayer(GetTriggerUnit()))
    SetPlayerAbilityAvailableBJ(false, FourCC('A02G'), GetOwningPlayer(GetTriggerUnit()))
    SetPlayerAbilityAvailableBJ(false, FourCC('A07D'), GetOwningPlayer(GetTriggerUnit()))
    --                           
    SetPlayerAbilityAvailableBJ(true, FourCC('A07M'), GetOwningPlayer(GetTriggerUnit()))
    SetPlayerAbilityAvailableBJ(true, FourCC('A07S'), GetOwningPlayer(GetTriggerUnit()))
    SetPlayerAbilityAvailableBJ(false, FourCC('A07R'), GetOwningPlayer(GetTriggerUnit()))
    SetPlayerAbilityAvailableBJ(true, FourCC('A07T'), GetOwningPlayer(GetTriggerUnit()))
    --                           
    SetPlayerAbilityAvailableBJ(true, FourCC('A02J'), GetOwningPlayer(GetTriggerUnit()))
    SetPlayerAbilityAvailableBJ(true, FourCC('A00W'), GetOwningPlayer(GetTriggerUnit()))
    SetPlayerAbilityAvailableBJ(true, FourCC('A030'), GetOwningPlayer(GetTriggerUnit()))
    SetPlayerAbilityAvailableBJ(true, FourCC('A02Z'), GetOwningPlayer(GetTriggerUnit()))
    SetPlayerAbilityAvailableBJ(true, FourCC('A02R'), GetOwningPlayer(GetTriggerUnit()))
    SetPlayerAbilityAvailableBJ(true, FourCC('A02U'), GetOwningPlayer(GetTriggerUnit()))
    --                           
    SetPlayerTechMaxAllowedSwap(FourCC('R026'), 1, GetOwningPlayer(GetTriggerUnit()))
    SetPlayerTechMaxAllowedSwap(FourCC('R03D'), 1, GetOwningPlayer(GetTriggerUnit()))
    SetPlayerTechMaxAllowedSwap(FourCC('R025'), 1, GetOwningPlayer(GetTriggerUnit()))
end
--===========================================================================
function InitTrig_StrannikF()
    gg_trg_StrannikF=CreateTrigger()
    DisableTrigger(gg_trg_StrannikF)
    TriggerRegisterAnyUnitEventBJ(gg_trg_StrannikF, EVENT_PLAYER_UNIT_RESEARCH_FINISH)
    TriggerAddCondition(gg_trg_StrannikF, Condition(Trig_StrannikF_Conditions))
    TriggerAddAction(gg_trg_StrannikF, Trig_StrannikF_Actions)
end
--===========================================================================
-- Trigger: StrannikB
--===========================================================================
function Trig_StrannikB_Conditions()
    return GetResearched() == FourCC('R03C')
end
function Trig_StrannikB_Actions()
    SetPlayerTechMaxAllowedSwap(FourCC('R026'), 0, GetOwningPlayer(GetTriggerUnit()))
    SetPlayerTechMaxAllowedSwap(FourCC('R03D'), 0, GetOwningPlayer(GetTriggerUnit()))
    SetPlayerTechMaxAllowedSwap(FourCC('R025'), 0, GetOwningPlayer(GetTriggerUnit()))
end
--===========================================================================
function InitTrig_StrannikB()
    gg_trg_StrannikB=CreateTrigger()
    DisableTrigger(gg_trg_StrannikB)
    TriggerRegisterAnyUnitEventBJ(gg_trg_StrannikB, EVENT_PLAYER_UNIT_RESEARCH_START)
    TriggerAddCondition(gg_trg_StrannikB, Condition(Trig_StrannikB_Conditions))
    TriggerAddAction(gg_trg_StrannikB, Trig_StrannikB_Actions)
end
--===========================================================================
-- Trigger: StrannikC
--===========================================================================
function Trig_StrannikC_Conditions()
    return GetResearched() == FourCC('R03C')
end
function Trig_StrannikC_Actions()
    SetPlayerTechMaxAllowedSwap(FourCC('R026'), 1, GetOwningPlayer(GetTriggerUnit()))
    SetPlayerTechMaxAllowedSwap(FourCC('R03D'), 1, GetOwningPlayer(GetTriggerUnit()))
    SetPlayerTechMaxAllowedSwap(FourCC('R025'), 1, GetOwningPlayer(GetTriggerUnit()))
end
--===========================================================================
function InitTrig_StrannikC()
    gg_trg_StrannikC=CreateTrigger()
    DisableTrigger(gg_trg_StrannikC)
    TriggerRegisterAnyUnitEventBJ(gg_trg_StrannikC, EVENT_PLAYER_UNIT_RESEARCH_CANCEL)
    TriggerAddCondition(gg_trg_StrannikC, Condition(Trig_StrannikC_Conditions))
    TriggerAddAction(gg_trg_StrannikC, Trig_StrannikC_Actions)
end
--===========================================================================
-- Trigger: PaladinF
--===========================================================================
function Trig_PaladinF_Conditions()
    return GetResearched() == FourCC('R026')
end
function Trig_PaladinF_Actions()
    SetPlayerTechResearchedSwap(FourCC('R03D'), 0, GetOwningPlayer(GetTriggerUnit()))
    SetPlayerTechResearchedSwap(FourCC('R03C'), 0, GetOwningPlayer(GetTriggerUnit()))
    SetPlayerTechResearchedSwap(FourCC('R025'), 0, GetOwningPlayer(GetTriggerUnit()))
    --                           
    SetPlayerAbilityAvailableBJ(false, FourCC('A05J'), GetOwningPlayer(GetTriggerUnit()))
    SetPlayerAbilityAvailableBJ(false, FourCC('A05K'), GetOwningPlayer(GetTriggerUnit()))
    SetPlayerAbilityAvailableBJ(true, FourCC('A049'), GetOwningPlayer(GetTriggerUnit()))
    SetPlayerAbilityAvailableBJ(true, FourCC('Asps'), GetOwningPlayer(GetTriggerUnit()))
    --                           
    SetPlayerAbilityAvailableBJ(true, FourCC('A07L'), GetOwningPlayer(GetTriggerUnit()))
    SetPlayerAbilityAvailableBJ(false, FourCC('A037'), GetOwningPlayer(GetTriggerUnit()))
    SetPlayerAbilityAvailableBJ(true, FourCC('A07K'), GetOwningPlayer(GetTriggerUnit()))
    --                           
    SetPlayerAbilityAvailableBJ(false, FourCC('A07P'), GetOwningPlayer(GetTriggerUnit()))
    SetPlayerAbilityAvailableBJ(false, FourCC('A07Q'), GetOwningPlayer(GetTriggerUnit()))
    SetPlayerAbilityAvailableBJ(false, FourCC('A07N'), GetOwningPlayer(GetTriggerUnit()))
    SetPlayerAbilityAvailableBJ(false, FourCC('A07O'), GetOwningPlayer(GetTriggerUnit()))
    SetPlayerAbilityAvailableBJ(false, FourCC('A02G'), GetOwningPlayer(GetTriggerUnit()))
    SetPlayerAbilityAvailableBJ(false, FourCC('A07D'), GetOwningPlayer(GetTriggerUnit()))
    --                           
    SetPlayerAbilityAvailableBJ(false, FourCC('A07M'), GetOwningPlayer(GetTriggerUnit()))
    SetPlayerAbilityAvailableBJ(false, FourCC('A07S'), GetOwningPlayer(GetTriggerUnit()))
    SetPlayerAbilityAvailableBJ(true, FourCC('A07R'), GetOwningPlayer(GetTriggerUnit()))
    SetPlayerAbilityAvailableBJ(false, FourCC('A07T'), GetOwningPlayer(GetTriggerUnit()))
    --                           
    SetPlayerAbilityAvailableBJ(true, FourCC('A02J'), GetOwningPlayer(GetTriggerUnit()))
    SetPlayerAbilityAvailableBJ(true, FourCC('A00W'), GetOwningPlayer(GetTriggerUnit()))
    SetPlayerAbilityAvailableBJ(true, FourCC('A030'), GetOwningPlayer(GetTriggerUnit()))
    SetPlayerAbilityAvailableBJ(true, FourCC('A02Z'), GetOwningPlayer(GetTriggerUnit()))
    SetPlayerAbilityAvailableBJ(true, FourCC('A02R'), GetOwningPlayer(GetTriggerUnit()))
    SetPlayerAbilityAvailableBJ(true, FourCC('A02G'), GetOwningPlayer(GetTriggerUnit()))
    --                           
    SetPlayerTechMaxAllowedSwap(FourCC('R03D'), 1, GetOwningPlayer(GetTriggerUnit()))
    SetPlayerTechMaxAllowedSwap(FourCC('R03C'), 1, GetOwningPlayer(GetTriggerUnit()))
    SetPlayerTechMaxAllowedSwap(FourCC('R025'), 1, GetOwningPlayer(GetTriggerUnit()))
end
--===========================================================================
function InitTrig_PaladinF()
    gg_trg_PaladinF=CreateTrigger()
    DisableTrigger(gg_trg_PaladinF)
    TriggerRegisterAnyUnitEventBJ(gg_trg_PaladinF, EVENT_PLAYER_UNIT_RESEARCH_FINISH)
    TriggerAddCondition(gg_trg_PaladinF, Condition(Trig_PaladinF_Conditions))
    TriggerAddAction(gg_trg_PaladinF, Trig_PaladinF_Actions)
end
--===========================================================================
-- Trigger: PaladinB
--===========================================================================
function Trig_PaladinB_Conditions()
    return GetResearched() == FourCC('R026')
end
function Trig_PaladinB_Actions()
    SetPlayerTechMaxAllowedSwap(FourCC('R03D'), 0, GetOwningPlayer(GetTriggerUnit()))
    SetPlayerTechMaxAllowedSwap(FourCC('R03C'), 0, GetOwningPlayer(GetTriggerUnit()))
    SetPlayerTechMaxAllowedSwap(FourCC('R025'), 0, GetOwningPlayer(GetTriggerUnit()))
end
--===========================================================================
function InitTrig_PaladinB()
    gg_trg_PaladinB=CreateTrigger()
    DisableTrigger(gg_trg_PaladinB)
    TriggerRegisterAnyUnitEventBJ(gg_trg_PaladinB, EVENT_PLAYER_UNIT_RESEARCH_START)
    TriggerAddCondition(gg_trg_PaladinB, Condition(Trig_PaladinB_Conditions))
    TriggerAddAction(gg_trg_PaladinB, Trig_PaladinB_Actions)
end
--===========================================================================
-- Trigger: PaladinC
--===========================================================================
function Trig_PaladinC_Conditions()
    return GetResearched() == FourCC('R026')
end
function Trig_PaladinC_Actions()
    SetPlayerTechMaxAllowedSwap(FourCC('R03D'), 1, GetOwningPlayer(GetTriggerUnit()))
    SetPlayerTechMaxAllowedSwap(FourCC('R03C'), 1, GetOwningPlayer(GetTriggerUnit()))
    SetPlayerTechMaxAllowedSwap(FourCC('R025'), 1, GetOwningPlayer(GetTriggerUnit()))
end
--===========================================================================
function InitTrig_PaladinC()
    gg_trg_PaladinC=CreateTrigger()
    DisableTrigger(gg_trg_PaladinC)
    TriggerRegisterAnyUnitEventBJ(gg_trg_PaladinC, EVENT_PLAYER_UNIT_RESEARCH_CANCEL)
    TriggerAddCondition(gg_trg_PaladinC, Condition(Trig_PaladinC_Conditions))
    TriggerAddAction(gg_trg_PaladinC, Trig_PaladinC_Actions)
end
--===========================================================================
-- Trigger: FireShielDamageUniversal
--===========================================================================
function Trig_FireShielDamageUniversal_Conditions()
    local dx
    local dy
    gCaster=GetEventDamageSource() --?? ??? ???
    gTarget=BlzGetEventDamageTarget()
    dx=GetUnitX(gCaster) - GetUnitX(gTarget)
    dy=GetUnitY(gCaster) - GetUnitY(gTarget)
    return GetUnitAbilityLevel(gCaster, FourCC('B00F')) > 0 and SquareRoot(dx * dx + dy * dy) < 200 and gCaster ~= nil and UnitAlive(gCaster) and gTarget ~= nil and UnitAlive(gTarget)
end
function Trig_FireShielDamageUniversal_Actions()
    UnitDamageTargetBJ(GetTriggerUnit(), gCaster, 45, ATTACK_TYPE_NORMAL, DAMAGE_TYPE_FIRE)
end
--===========================================================================
function InitTrig_FireShielDamageUniversal()
    gg_trg_FireShielDamageUniversal=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_FireShielDamageUniversal, EVENT_PLAYER_UNIT_DAMAGED)
    TriggerAddCondition(gg_trg_FireShielDamageUniversal, Condition(Trig_FireShielDamageUniversal_Conditions))
    TriggerAddAction(gg_trg_FireShielDamageUniversal, Trig_FireShielDamageUniversal_Actions)
end