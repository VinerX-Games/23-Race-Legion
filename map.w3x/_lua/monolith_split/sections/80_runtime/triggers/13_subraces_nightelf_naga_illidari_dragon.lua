    gg_trg_AreaOfDeath2=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_AreaOfDeath2, EVENT_PLAYER_UNIT_SPELL_EFFECT)
    TriggerAddAction(gg_trg_AreaOfDeath2, function()
        if GetSpellAbilityId() ~= FourCC('A1K1') then return end
        Trig_AreaOfDeath2_Actions()
    end)
end
--===========================================================================
-- Trigger: Global
--===========================================================================
--===========================================================================
-- Trigger: Sanctified Enchantment
--===========================================================================
--===========================================================================
-- Trigger: Kop
--===========================================================================
function Trig_Kop_Func001A()
    SetPlayerTechMaxAllowedSwap(FourCC('n06J'), 0, GetEnumPlayer())
end
function Trig_Kop_Actions()
    ForForce(udg_AllPlayers, Trig_Kop_Func001A)
end
--===========================================================================
function InitTrig_Kop()
    gg_trg_Kop=CreateTrigger()
    TriggerRegisterTimerEventSingle(gg_trg_Kop, 5)
    TriggerAddAction(gg_trg_Kop, Trig_Kop_Actions)
end
--===========================================================================
-- Trigger: Kop3
--===========================================================================
function Trig_Kop3_Func001A()
    SetPlayerTechMaxAllowedSwap(FourCC('n06W'), 0, GetEnumPlayer())
end
function Trig_Kop3_Actions()
    ForForce(udg_AllPlayers, Trig_Kop3_Func001A)
end
--===========================================================================
function InitTrig_Kop3()
    gg_trg_Kop3=CreateTrigger()
    TriggerRegisterTimerEventSingle(gg_trg_Kop3, 5)
    TriggerAddAction(gg_trg_Kop3, Trig_Kop3_Actions)
end
--===========================================================================
-- Trigger: Strel
--===========================================================================
function Trig_Strel_Func001A()
    SetPlayerTechMaxAllowedSwap(FourCC('n06M'), 0, GetEnumPlayer())
end
function Trig_Strel_Actions()
    ForForce(udg_AllPlayers, Trig_Strel_Func001A)
end
--===========================================================================
function InitTrig_Strel()
    gg_trg_Strel=CreateTrigger()
    TriggerRegisterTimerEventSingle(gg_trg_Strel, 5)
    TriggerAddAction(gg_trg_Strel, Trig_Strel_Actions)
end
--===========================================================================
-- Trigger: Strel3
--===========================================================================
function Trig_Strel3_Func001A()
    SetPlayerTechMaxAllowedSwap(FourCC('n06Q'), 0, GetEnumPlayer())
end
function Trig_Strel3_Actions()
    ForForce(udg_AllPlayers, Trig_Strel3_Func001A)
end
--===========================================================================
function InitTrig_Strel3()
    gg_trg_Strel3=CreateTrigger()
    TriggerRegisterTimerEventSingle(gg_trg_Strel3, 5)
    TriggerAddAction(gg_trg_Strel3, Trig_Strel3_Actions)
end
--===========================================================================
-- Trigger: Rub
--===========================================================================
function Trig_Rub_Func001A()
    SetPlayerTechMaxAllowedSwap(FourCC('n06L'), 0, GetEnumPlayer())
end
function Trig_Rub_Actions()
    ForForce(udg_AllPlayers, Trig_Rub_Func001A)
end
--===========================================================================
function InitTrig_Rub()
    gg_trg_Rub=CreateTrigger()
    TriggerRegisterTimerEventSingle(gg_trg_Rub, 5)
    TriggerAddAction(gg_trg_Rub, Trig_Rub_Actions)
end
--===========================================================================
-- Trigger: Rub3
--===========================================================================
function Trig_Rub3_Func001A()
    SetPlayerTechMaxAllowedSwap(FourCC('n06T'), 0, GetEnumPlayer())
end
function Trig_Rub3_Actions()
    ForForce(udg_AllPlayers, Trig_Rub3_Func001A)
end
--===========================================================================
function InitTrig_Rub3()
    gg_trg_Rub3=CreateTrigger()
    TriggerRegisterTimerEventSingle(gg_trg_Rub3, 5)
    TriggerAddAction(gg_trg_Rub3, Trig_Rub3_Actions)
end
--===========================================================================
-- Trigger: Sham
--===========================================================================
function Trig_Sham_Func001A()
    SetPlayerTechMaxAllowedSwap(FourCC('n06S'), 0, GetEnumPlayer())
end
function Trig_Sham_Actions()
    ForForce(udg_AllPlayers, Trig_Sham_Func001A)
end
--===========================================================================
function InitTrig_Sham()
    gg_trg_Sham=CreateTrigger()
    TriggerRegisterTimerEventSingle(gg_trg_Sham, 5)
    TriggerAddAction(gg_trg_Sham, Trig_Sham_Actions)
end
--===========================================================================
-- Trigger: Sham3
--===========================================================================
function Trig_Sham3_Func001A()
    SetPlayerTechMaxAllowedSwap(FourCC('n06O'), 0, GetEnumPlayer())
end
function Trig_Sham3_Actions()
    ForForce(udg_AllPlayers, Trig_Sham3_Func001A)
end
--===========================================================================
function InitTrig_Sham3()
    gg_trg_Sham3=CreateTrigger()
    TriggerRegisterTimerEventSingle(gg_trg_Sham3, 5)
    TriggerAddAction(gg_trg_Sham3, Trig_Sham3_Actions)
end
--===========================================================================
-- Trigger: Chern
--===========================================================================
function Trig_Chern_Func001A()
    SetPlayerTechMaxAllowedSwap(FourCC('n06R'), 0, GetEnumPlayer())
end
function Trig_Chern_Actions()
    ForForce(udg_AllPlayers, Trig_Chern_Func001A)
end
--===========================================================================
function InitTrig_Chern()
    gg_trg_Chern=CreateTrigger()
    TriggerRegisterTimerEventSingle(gg_trg_Chern, 5)
    TriggerAddAction(gg_trg_Chern, Trig_Chern_Actions)
end
--===========================================================================
-- Trigger: Chern3
--===========================================================================
function Trig_Chern3_Func001A()
    SetPlayerTechMaxAllowedSwap(FourCC('n06N'), 0, GetEnumPlayer())
end
function Trig_Chern3_Actions()
    ForForce(udg_AllPlayers, Trig_Chern3_Func001A)
end
--===========================================================================
function InitTrig_Chern3()
    gg_trg_Chern3=CreateTrigger()
    TriggerRegisterTimerEventSingle(gg_trg_Chern3, 5)
    TriggerAddAction(gg_trg_Chern3, Trig_Chern3_Actions)
end
--===========================================================================
-- Trigger: Kodo
--===========================================================================
function Trig_Kodo_Func001A()
    SetPlayerTechMaxAllowedSwap(FourCC('n06I'), 0, GetEnumPlayer())
end
function Trig_Kodo_Actions()
    ForForce(udg_AllPlayers, Trig_Kodo_Func001A)
end
--===========================================================================
function InitTrig_Kodo()
    gg_trg_Kodo=CreateTrigger()
    TriggerRegisterTimerEventSingle(gg_trg_Kodo, 5)
    TriggerAddAction(gg_trg_Kodo, Trig_Kodo_Actions)
end
--===========================================================================
-- Trigger: Kodo3
--===========================================================================
function Trig_Kodo3_Func001A()
    SetPlayerTechMaxAllowedSwap(FourCC('n06V'), 0, GetEnumPlayer())
end
function Trig_Kodo3_Actions()
    ForForce(udg_AllPlayers, Trig_Kodo3_Func001A)
end
--===========================================================================
function InitTrig_Kodo3()
    gg_trg_Kodo3=CreateTrigger()
    TriggerRegisterTimerEventSingle(gg_trg_Kodo3, 5)
    TriggerAddAction(gg_trg_Kodo3, Trig_Kodo3_Actions)
end
--===========================================================================
-- Trigger: Tel
--===========================================================================
function Trig_Tel_Func001A()
    SetPlayerTechMaxAllowedSwap(FourCC('o065'), 0, GetEnumPlayer())
end
function Trig_Tel_Actions()
    ForForce(udg_AllPlayers, Trig_Tel_Func001A)
end
--===========================================================================
function InitTrig_Tel()
    gg_trg_Tel=CreateTrigger()
    TriggerRegisterTimerEventSingle(gg_trg_Tel, 5)
    TriggerAddAction(gg_trg_Tel, Trig_Tel_Actions)
end
--===========================================================================
-- Trigger: Tel3
--===========================================================================
function Trig_Tel3_Func001A()
    SetPlayerTechMaxAllowedSwap(FourCC('o063'), 0, GetEnumPlayer())
end
function Trig_Tel3_Actions()
    ForForce(udg_AllPlayers, Trig_Tel3_Func001A)
end
--===========================================================================
function InitTrig_Tel3()
    gg_trg_Tel3=CreateTrigger()
    TriggerRegisterTimerEventSingle(gg_trg_Tel3, 5)
    TriggerAddAction(gg_trg_Tel3, Trig_Tel3_Actions)
end
--===========================================================================
-- Trigger: Nale
--===========================================================================
function Trig_Nale_Func001A()
    SetPlayerTechMaxAllowedSwap(FourCC('n06U'), 0, GetEnumPlayer())
end
function Trig_Nale_Actions()
    ForForce(udg_AllPlayers, Trig_Nale_Func001A)
end
--===========================================================================
function InitTrig_Nale()
    gg_trg_Nale=CreateTrigger()
    TriggerRegisterTimerEventSingle(gg_trg_Nale, 5)
    TriggerAddAction(gg_trg_Nale, Trig_Nale_Actions)
end
--===========================================================================
-- Trigger: Nale3
--===========================================================================
function Trig_Nale3_Func001A()
    SetPlayerTechMaxAllowedSwap(FourCC('n06K'), 0, GetEnumPlayer())
end
function Trig_Nale3_Actions()
    ForForce(udg_AllPlayers, Trig_Nale3_Func001A)
end
--===========================================================================
function InitTrig_Nale3()
    gg_trg_Nale3=CreateTrigger()
    TriggerRegisterTimerEventSingle(gg_trg_Nale3, 5)
    TriggerAddAction(gg_trg_Nale3, Trig_Nale3_Actions)
end
--===========================================================================
-- Trigger: KodoT3
--===========================================================================
function Trig_KodoT3_Actions()
    SetPlayerTechResearchedSwap(FourCC('R0JJ'), 1, GetOwningPlayer(GetTriggerUnit()))
    SetPlayerAbilityAvailableBJ(false, FourCC('A1IM'), GetOwningPlayer(GetTriggerUnit()))
    DisableTrigger(gg_trg_Kodo3)
end
--===========================================================================
function InitTrig_KodoT3()
    gg_trg_KodoT3=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_KodoT3, EVENT_PLAYER_UNIT_SPELL_FINISH)
    TriggerAddAction(gg_trg_KodoT3, function()
        if GetSpellAbilityId() ~= FourCC('A1IM') then return end
        Trig_KodoT3_Actions()
    end)
end
--===========================================================================
-- Trigger: NaleT3
--===========================================================================
function Trig_NaleT3_Actions()
    SetPlayerTechResearchedSwap(FourCC('R0JL'), 1, GetOwningPlayer(GetTriggerUnit()))
    SetPlayerAbilityAvailableBJ(false, FourCC('A1IO'), GetOwningPlayer(GetTriggerUnit()))
    DisableTrigger(gg_trg_Nale3)
end
--===========================================================================
function InitTrig_NaleT3()
    gg_trg_NaleT3=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_NaleT3, EVENT_PLAYER_UNIT_SPELL_FINISH)
    TriggerAddAction(gg_trg_NaleT3, function()
        if GetSpellAbilityId() ~= FourCC('A1IO') then return end
        Trig_NaleT3_Actions()
    end)
end
--===========================================================================
-- Trigger: ShamT3
--===========================================================================
function Trig_ShamT3_Actions()
    SetPlayerTechResearchedSwap(FourCC('R0JT'), 1, GetOwningPlayer(GetTriggerUnit()))
    SetPlayerAbilityAvailableBJ(false, FourCC('A1IT'), GetOwningPlayer(GetTriggerUnit()))
    DisableTrigger(gg_trg_Sham3)
end
--===========================================================================
function InitTrig_ShamT3()
    gg_trg_ShamT3=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_ShamT3, EVENT_PLAYER_UNIT_SPELL_FINISH)
    TriggerAddAction(gg_trg_ShamT3, function()
        if GetSpellAbilityId() ~= FourCC('A1IT') then return end
        Trig_ShamT3_Actions()
    end)
end
--===========================================================================
-- Trigger: CherT3
--===========================================================================
function Trig_CherT3_Actions()
    SetPlayerTechResearchedSwap(FourCC('R0JP'), 1, GetOwningPlayer(GetTriggerUnit()))
    SetPlayerAbilityAvailableBJ(false, FourCC('A1IS'), GetOwningPlayer(GetTriggerUnit()))
    DisableTrigger(gg_trg_Chern3)
end
--===========================================================================
function InitTrig_CherT3()
    gg_trg_CherT3=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_CherT3, EVENT_PLAYER_UNIT_SPELL_FINISH)
    TriggerAddAction(gg_trg_CherT3, function()
        if GetSpellAbilityId() ~= FourCC('A1IS') then return end
        Trig_CherT3_Actions()
    end)
end
--===========================================================================
-- Trigger: KopT3
--===========================================================================
function Trig_KopT3_Actions()
    SetPlayerTechResearchedSwap(FourCC('R0JK'), 1, GetOwningPlayer(GetTriggerUnit()))
    SetPlayerAbilityAvailableBJ(false, FourCC('A1IN'), GetOwningPlayer(GetTriggerUnit()))
    DisableTrigger(gg_trg_Kop3)
end
--===========================================================================
function InitTrig_KopT3()
    gg_trg_KopT3=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_KopT3, EVENT_PLAYER_UNIT_SPELL_FINISH)
    TriggerAddAction(gg_trg_KopT3, function()
        if GetSpellAbilityId() ~= FourCC('A1IN') then return end
        Trig_KopT3_Actions()
    end)
end
--===========================================================================
-- Trigger: StrelT3
--===========================================================================
function Trig_StrelT3_Actions()
    SetPlayerTechResearchedSwap(FourCC('R0JN'), 1, GetOwningPlayer(GetTriggerUnit()))
    SetPlayerAbilityAvailableBJ(false, FourCC('A1IQ'), GetOwningPlayer(GetTriggerUnit()))
    DisableTrigger(gg_trg_Strel3)
end
--===========================================================================
function InitTrig_StrelT3()
    gg_trg_StrelT3=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_StrelT3, EVENT_PLAYER_UNIT_SPELL_FINISH)
    TriggerAddAction(gg_trg_StrelT3, function()
        if GetSpellAbilityId() ~= FourCC('A1IQ') then return end
        Trig_StrelT3_Actions()
    end)
end
--===========================================================================
-- Trigger: RubT3
--===========================================================================
function Trig_RubT3_Actions()
    SetPlayerTechResearchedSwap(FourCC('R0JM'), 1, GetOwningPlayer(GetTriggerUnit()))
    SetPlayerAbilityAvailableBJ(false, FourCC('A1IP'), GetOwningPlayer(GetTriggerUnit()))
    DisableTrigger(gg_trg_Rub3)
end
--===========================================================================
function InitTrig_RubT3()
    gg_trg_RubT3=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_RubT3, EVENT_PLAYER_UNIT_SPELL_FINISH)
    TriggerAddAction(gg_trg_RubT3, function()
        if GetSpellAbilityId() ~= FourCC('A1IP') then return end
        Trig_RubT3_Actions()
    end)
end
--===========================================================================
-- Trigger: TelT3
--===========================================================================
function Trig_TelT3_Actions()
    SetPlayerTechResearchedSwap(FourCC('R0JO'), 1, GetOwningPlayer(GetTriggerUnit()))
    SetPlayerAbilityAvailableBJ(false, FourCC('A1IR'), GetOwningPlayer(GetTriggerUnit()))
    DisableTrigger(gg_trg_Tel3)
end
--===========================================================================
function InitTrig_TelT3()
    gg_trg_TelT3=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_TelT3, EVENT_PLAYER_UNIT_SPELL_FINISH)
    TriggerAddAction(gg_trg_TelT3, function()
        if GetSpellAbilityId() ~= FourCC('A1IR') then return end
        Trig_TelT3_Actions()
    end)
end
--===========================================================================
-- Trigger: KodoNale
--===========================================================================
function Trig_KodoNale_Actions()
    SetPlayerTechResearchedSwap(FourCC('R0JF'), 1, GetOwningPlayer(GetTriggerUnit()))
    SetPlayerAbilityAvailableBJ(false, FourCC('A1HW'), GetOwningPlayer(GetTriggerUnit()))
    SetPlayerAbilityAvailableBJ(false, FourCC('A1IO'), GetOwningPlayer(GetTriggerUnit()))
    SetPlayerAbilityAvailableBJ(false, FourCC('A1HY'), GetOwningPlayer(GetTriggerUnit()))
    DisableTrigger(gg_trg_Kodo)
end
--===========================================================================
function InitTrig_KodoNale()
    gg_trg_KodoNale=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_KodoNale, EVENT_PLAYER_UNIT_SPELL_FINISH)
    TriggerAddAction(gg_trg_KodoNale, function()
        if GetSpellAbilityId() ~= FourCC('A1HW') then return end
        Trig_KodoNale_Actions()
    end)
end
--===========================================================================
-- Trigger: NaleKodo
--===========================================================================
function Trig_NaleKodo_Actions()
    SetPlayerTechResearchedSwap(FourCC('R0JE'), 1, GetOwningPlayer(GetTriggerUnit()))
    SetPlayerAbilityAvailableBJ(false, FourCC('A1HW'), GetOwningPlayer(GetTriggerUnit()))
    SetPlayerAbilityAvailableBJ(false, FourCC('A1IM'), GetOwningPlayer(GetTriggerUnit()))
    SetPlayerAbilityAvailableBJ(false, FourCC('A1HY'), GetOwningPlayer(GetTriggerUnit()))
    DisableTrigger(gg_trg_Nale)
end
--===========================================================================
function InitTrig_NaleKodo()
    gg_trg_NaleKodo=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_NaleKodo, EVENT_PLAYER_UNIT_SPELL_FINISH)
    TriggerAddAction(gg_trg_NaleKodo, function()
        if GetSpellAbilityId() ~= FourCC('A1HY') then return end
        Trig_NaleKodo_Actions()
    end)
end
--===========================================================================
-- Trigger: Ritual
--===========================================================================
function Trig_Ritual_Actions()
    SetPlayerTechResearchedSwap(FourCC('R0K9'), 1, GetOwningPlayer(GetTriggerUnit()))
    SetPlayerAbilityAvailableBJ(false, FourCC('A1JI'), GetOwningPlayer(GetTriggerUnit()))
    SetPlayerAbilityAvailableBJ(false, FourCC('A1JH'), GetOwningPlayer(GetTriggerUnit()))
end
--===========================================================================
function InitTrig_Ritual()
    gg_trg_Ritual=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_Ritual, EVENT_PLAYER_UNIT_SPELL_FINISH)
    TriggerAddAction(gg_trg_Ritual, function()
        if GetSpellAbilityId() ~= FourCC('A1JI') then return end
        Trig_Ritual_Actions()
    end)
end
--===========================================================================
-- Trigger: Ritual Copy
--===========================================================================
function Trig_Ritual_Copy_Actions()
    SetPlayerTechResearchedSwap(FourCC('R0K8'), 1, GetOwningPlayer(GetTriggerUnit()))
    SetPlayerAbilityAvailableBJ(false, FourCC('A1JI'), GetOwningPlayer(GetTriggerUnit()))
    SetPlayerAbilityAvailableBJ(false, FourCC('A1JH'), GetOwningPlayer(GetTriggerUnit()))
end
--===========================================================================
function InitTrig_Ritual_Copy()
    gg_trg_Ritual_Copy=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_Ritual_Copy, EVENT_PLAYER_UNIT_SPELL_FINISH)
    TriggerAddAction(gg_trg_Ritual_Copy, function()
        if GetSpellAbilityId() ~= FourCC('A1JH') then return end
        Trig_Ritual_Copy_Actions()
    end)
end
--===========================================================================
-- Trigger: ShamCher
--===========================================================================
function Trig_ShamCher_Actions()
    SetPlayerTechResearchedSwap(FourCC('R0JD'), 1, GetOwningPlayer(GetTriggerUnit()))
    SetPlayerAbilityAvailableBJ(false, FourCC('A1I2'), GetOwningPlayer(GetTriggerUnit()))
    SetPlayerAbilityAvailableBJ(false, FourCC('A1IS'), GetOwningPlayer(GetTriggerUnit()))
    SetPlayerAbilityAvailableBJ(false, FourCC('A1I3'), GetOwningPlayer(GetTriggerUnit()))
    DisableTrigger(gg_trg_Sham)
end
--===========================================================================
function InitTrig_ShamCher()
    gg_trg_ShamCher=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_ShamCher, EVENT_PLAYER_UNIT_SPELL_FINISH)
    TriggerAddAction(gg_trg_ShamCher, function()
        if GetSpellAbilityId() ~= FourCC('A1I3') then return end
        Trig_ShamCher_Actions()
    end)
end
--===========================================================================
-- Trigger: CherSham
--===========================================================================
function Trig_CherSham_Actions()
    SetPlayerTechResearchedSwap(FourCC('R0JC'), 1, GetOwningPlayer(GetTriggerUnit()))
    SetPlayerAbilityAvailableBJ(false, FourCC('A1I2'), GetOwningPlayer(GetTriggerUnit()))
    SetPlayerAbilityAvailableBJ(false, FourCC('A1IT'), GetOwningPlayer(GetTriggerUnit()))
    SetPlayerAbilityAvailableBJ(false, FourCC('A1I3'), GetOwningPlayer(GetTriggerUnit()))
    DisableTrigger(gg_trg_Chern)
end
--===========================================================================
function InitTrig_CherSham()
    gg_trg_CherSham=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_CherSham, EVENT_PLAYER_UNIT_SPELL_FINISH)
    TriggerAddAction(gg_trg_CherSham, function()
        if GetSpellAbilityId() ~= FourCC('A1I2') then return end
        Trig_CherSham_Actions()
    end)
end
--===========================================================================
-- Trigger: KopStrel
--===========================================================================
function Trig_KopStrel_Actions()
    SetPlayerTechResearchedSwap(FourCC('R0JA'), 1, GetOwningPlayer(GetTriggerUnit()))
    SetPlayerAbilityAvailableBJ(false, FourCC('A1HX'), GetOwningPlayer(GetTriggerUnit()))
    SetPlayerAbilityAvailableBJ(false, FourCC('A1IQ'), GetOwningPlayer(GetTriggerUnit()))
    SetPlayerAbilityAvailableBJ(false, FourCC('A1I0'), GetOwningPlayer(GetTriggerUnit()))
    DisableTrigger(gg_trg_Kop)
end
--===========================================================================
function InitTrig_KopStrel()
    gg_trg_KopStrel=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_KopStrel, EVENT_PLAYER_UNIT_SPELL_FINISH)
    TriggerAddAction(gg_trg_KopStrel, function()
        if GetSpellAbilityId() ~= FourCC('A1HX') then return end
        Trig_KopStrel_Actions()
    end)
end
--===========================================================================
-- Trigger: StrelKop
--===========================================================================
function Trig_StrelKop_Actions()
    SetPlayerTechResearchedSwap(FourCC('R0JB'), 1, GetOwningPlayer(GetTriggerUnit()))
    SetPlayerAbilityAvailableBJ(false, FourCC('A1HX'), GetOwningPlayer(GetTriggerUnit()))
    SetPlayerAbilityAvailableBJ(false, FourCC('A1IN'), GetOwningPlayer(GetTriggerUnit()))
    SetPlayerAbilityAvailableBJ(false, FourCC('A1I0'), GetOwningPlayer(GetTriggerUnit()))
    DisableTrigger(gg_trg_Strel)
end
--===========================================================================
function InitTrig_StrelKop()
    gg_trg_StrelKop=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_StrelKop, EVENT_PLAYER_UNIT_SPELL_FINISH)
    TriggerAddAction(gg_trg_StrelKop, function()
        if GetSpellAbilityId() ~= FourCC('A1I0') then return end
        Trig_StrelKop_Actions()
    end)
end
--===========================================================================
-- Trigger: RubTel
--===========================================================================
function Trig_RubTel_Actions()
    SetPlayerTechResearchedSwap(FourCC('R0J9'), 1, GetOwningPlayer(GetTriggerUnit()))
    SetPlayerAbilityAvailableBJ(false, FourCC('A1HZ'), GetOwningPlayer(GetTriggerUnit()))
    SetPlayerAbilityAvailableBJ(false, FourCC('A1IR'), GetOwningPlayer(GetTriggerUnit()))
    SetPlayerAbilityAvailableBJ(false, FourCC('A1I1'), GetOwningPlayer(GetTriggerUnit()))
    DisableTrigger(gg_trg_Rub)
end
--===========================================================================
function InitTrig_RubTel()
    gg_trg_RubTel=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_RubTel, EVENT_PLAYER_UNIT_SPELL_FINISH)
    TriggerAddAction(gg_trg_RubTel, function()
        if GetSpellAbilityId() ~= FourCC('A1HZ') then return end
        Trig_RubTel_Actions()
    end)
end
--===========================================================================
-- Trigger: TelRub
--===========================================================================
function Trig_TelRub_Actions()
    SetPlayerTechResearchedSwap(FourCC('R0JG'), 1, GetOwningPlayer(GetTriggerUnit()))
    SetPlayerAbilityAvailableBJ(false, FourCC('A1HZ'), GetOwningPlayer(GetTriggerUnit()))
    SetPlayerAbilityAvailableBJ(false, FourCC('A1IP'), GetOwningPlayer(GetTriggerUnit()))
    SetPlayerAbilityAvailableBJ(false, FourCC('A1I1'), GetOwningPlayer(GetTriggerUnit()))
    DisableTrigger(gg_trg_Tel)
end
--===========================================================================
function InitTrig_TelRub()
    gg_trg_TelRub=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_TelRub, EVENT_PLAYER_UNIT_SPELL_FINISH)
    TriggerAddAction(gg_trg_TelRub, function()
        if GetSpellAbilityId() ~= FourCC('A1I1') then return end
        Trig_TelRub_Actions()
    end)
end
--===========================================================================
-- Trigger: NerZulPas
--
-- ?? ???? ???? ????, ??? ? ????? ?? ??? ??? - ?????
--===========================================================================
function Trig_NerZulPas_Conditions()
    return GetLearnedSkillBJ() == FourCC('A1IB')
end
function Trig_NerZulPas_Actions()
    UnitAddAbilityBJ(FourCC('A1IC'), GetTriggerUnit())
    SetUnitAbilityLevelSwapped(FourCC('A1IC'), GetTriggerUnit(), GetUnitAbilityLevelSwapped(FourCC('A1IB'), GetTriggerUnit()))
end
--===========================================================================
function InitTrig_NerZulPas()
    gg_trg_NerZulPas=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_NerZulPas, EVENT_PLAYER_HERO_SKILL)
    TriggerAddCondition(gg_trg_NerZulPas, Condition(Trig_NerZulPas_Conditions))
    TriggerAddAction(gg_trg_NerZulPas, Trig_NerZulPas_Actions)
end
--===========================================================================
-- Trigger: NerZulPas Copy
--
-- ?? ???? ???? ????, ??? ? ????? ?? ??? ??? - ?????
--===========================================================================
function Trig_NerZulPas_Copy_Conditions()
    return GetLearnedSkillBJ() == FourCC('A1I5')
end
function Trig_NerZulPas_Copy_Actions()
    UnitAddAbilityBJ(FourCC('A1IE'), GetTriggerUnit())
    SetUnitAbilityLevelSwapped(FourCC('A1IE'), GetTriggerUnit(), GetUnitAbilityLevelSwapped(FourCC('A1I5'), GetTriggerUnit()))
end
--===========================================================================
function InitTrig_NerZulPas_Copy()
    gg_trg_NerZulPas_Copy=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_NerZulPas_Copy, EVENT_PLAYER_HERO_SKILL)
    TriggerAddCondition(gg_trg_NerZulPas_Copy, Condition(Trig_NerZulPas_Copy_Conditions))
    TriggerAddAction(gg_trg_NerZulPas_Copy, Trig_NerZulPas_Copy_Actions)
end
--===========================================================================
-- Trigger: NerZulPas Copy Copy
--
-- ?? ???? ???? ????, ??? ? ????? ?? ??? ??? - ?????
--===========================================================================
function Trig_NerZulPas_Copy_Copy_Conditions()
    return GetLearnedSkillBJ() == FourCC('A1H9')
end
function Trig_NerZulPas_Copy_Copy_Actions()
    UnitAddAbilityBJ(FourCC('A1IF'), GetTriggerUnit())
    SetUnitAbilityLevelSwapped(FourCC('A1IF'), GetTriggerUnit(), GetUnitAbilityLevelSwapped(FourCC('A1H9'), GetTriggerUnit()))
end
--===========================================================================
function InitTrig_NerZulPas_Copy_Copy()
    gg_trg_NerZulPas_Copy_Copy=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_NerZulPas_Copy_Copy, EVENT_PLAYER_HERO_SKILL)
    TriggerAddCondition(gg_trg_NerZulPas_Copy_Copy, Condition(Trig_NerZulPas_Copy_Copy_Conditions))
    TriggerAddAction(gg_trg_NerZulPas_Copy_Copy, Trig_NerZulPas_Copy_Copy_Actions)
end
--===========================================================================
-- Trigger: StartNight
--===========================================================================
function Trig_StartNight_Func001A()
    SetPlayerTechMaxAllowedSwap(FourCC('e00J'), 0, GetEnumPlayer())
    SetPlayerTechMaxAllowedSwap(FourCC('n064'), 0, GetEnumPlayer())
    SetPlayerTechMaxAllowedSwap(FourCC('edot'), 0, GetEnumPlayer())
    SetPlayerTechMaxAllowedSwap(FourCC('edoc'), 0, GetEnumPlayer())
    SetPlayerTechMaxAllowedSwap(FourCC('n05D'), 0, GetEnumPlayer())
    SetPlayerTechMaxAllowedSwap(FourCC('n05H'), 0, GetEnumPlayer())
    SetPlayerTechMaxAllowedSwap(FourCC('E00V'), 1, GetEnumPlayer())
    SetPlayerTechMaxAllowedSwap(FourCC('E011'), 1, GetEnumPlayer())
    SetPlayerTechMaxAllowedSwap(FourCC('E00W'), 1, GetEnumPlayer())
end
function Trig_StartNight_Actions()
    ForForce(udg_AllPlayers, Trig_StartNight_Func001A)
end
--===========================================================================
function InitTrig_StartNight()
    gg_trg_StartNight=CreateTrigger()
    TriggerRegisterTimerEventSingle(gg_trg_StartNight, 5)
    TriggerAddAction(gg_trg_StartNight, Trig_StartNight_Actions)
end
--===========================================================================
-- Trigger: KrugBeg
--===========================================================================
function Trig_KrugBeg_Conditions()
    return GetResearched() == FourCC('R0G1')
end
function Trig_KrugBeg_Actions()
    SetPlayerTechMaxAllowedSwap(FourCC('R0G2'), 0, GetOwningPlayer(GetTriggerUnit()))
    SetPlayerTechMaxAllowedSwap(FourCC('Remk'), 0, GetOwningPlayer(GetTriggerUnit()))
    SetPlayerTechMaxAllowedSwap(FourCC('Remg'), 0, GetOwningPlayer(GetTriggerUnit()))
    SetPlayerTechMaxAllowedSwap(FourCC('Reib'), 0, GetOwningPlayer(GetTriggerUnit()))
    SetPlayerTechMaxAllowedSwap(FourCC('R0G6'), 0, GetOwningPlayer(GetTriggerUnit()))
    SetPlayerTechMaxAllowedSwap(FourCC('R0G7'), 0, GetOwningPlayer(GetTriggerUnit()))
    SetPlayerTechResearchedSwap(FourCC('R0GB'), 1, GetOwningPlayer(GetTriggerUnit()))
end
--===========================================================================
function InitTrig_KrugBeg()
    gg_trg_KrugBeg=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_KrugBeg, EVENT_PLAYER_UNIT_RESEARCH_START)
    TriggerAddCondition(gg_trg_KrugBeg, Condition(Trig_KrugBeg_Conditions))
    TriggerAddAction(gg_trg_KrugBeg, Trig_KrugBeg_Actions)
end
--===========================================================================
-- Trigger: KrugCan
--===========================================================================
function Trig_KrugCan_Conditions()
    return GetResearched() == FourCC('R0G1')
end
function Trig_KrugCan_Actions()
    SetPlayerTechMaxAllowedSwap(FourCC('R0G2'), 1, GetOwningPlayer(GetTriggerUnit()))
    SetPlayerTechMaxAllowedSwap(FourCC('Remk'), 1, GetOwningPlayer(GetTriggerUnit()))
    SetPlayerTechMaxAllowedSwap(FourCC('Remg'), 1, GetOwningPlayer(GetTriggerUnit()))
    SetPlayerTechMaxAllowedSwap(FourCC('Reib'), 1, GetOwningPlayer(GetTriggerUnit()))
end
--===========================================================================
function InitTrig_KrugCan()
    gg_trg_KrugCan=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_KrugCan, EVENT_PLAYER_UNIT_RESEARCH_CANCEL)
    TriggerAddCondition(gg_trg_KrugCan, Condition(Trig_KrugCan_Conditions))
    TriggerAddAction(gg_trg_KrugCan, Trig_KrugCan_Actions)
end
--===========================================================================
-- Trigger: KrugFin
--===========================================================================
function Trig_KrugFin_Conditions()
    return GetResearched() == FourCC('R0G1')
end
function Trig_KrugFin_Actions()
    SetPlayerTechMaxAllowedSwap(FourCC('e00J'), - 1, GetOwningPlayer(GetTriggerUnit()))
    SetPlayerTechMaxAllowedSwap(FourCC('n064'), - 1, GetOwningPlayer(GetTriggerUnit()))
    SetPlayerTechMaxAllowedSwap(FourCC('edot'), - 1, GetOwningPlayer(GetTriggerUnit()))
    SetPlayerTechMaxAllowedSwap(FourCC('edoc'), - 1, GetOwningPlayer(GetTriggerUnit()))
    SetPlayerTechMaxAllowedSwap(FourCC('n05D'), - 1, GetOwningPlayer(GetTriggerUnit()))
    SetPlayerTechMaxAllowedSwap(FourCC('n05H'), - 1, GetOwningPlayer(GetTriggerUnit()))
    SetPlayerTechMaxAllowedSwap(FourCC('earc'), 0, GetOwningPlayer(GetTriggerUnit()))
    SetPlayerTechMaxAllowedSwap(FourCC('esen'), 0, GetOwningPlayer(GetTriggerUnit()))
    SetPlayerTechMaxAllowedSwap(FourCC('e00I'), 0, GetOwningPlayer(GetTriggerUnit()))
    SetPlayerTechMaxAllowedSwap(FourCC('e00H'), 0, GetOwningPlayer(GetTriggerUnit()))
end
--===========================================================================
function InitTrig_KrugFin()
    gg_trg_KrugFin=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_KrugFin, EVENT_PLAYER_UNIT_RESEARCH_FINISH)
    TriggerAddCondition(gg_trg_KrugFin, Condition(Trig_KrugFin_Conditions))
    TriggerAddAction(gg_trg_KrugFin, Trig_KrugFin_Actions)
end
--===========================================================================
-- Trigger: ElfBegFin
--===========================================================================
function Trig_ElfBegFin_Conditions()
    return GetResearched() == FourCC('R0G2')
end
function Trig_ElfBegFin_Actions()
    SetPlayerTechMaxAllowedSwap(FourCC('R0GB'), 1, GetOwningPlayer(GetTriggerUnit()))
    SetPlayerTechMaxAllowedSwap(FourCC('R0G1'), 0, GetOwningPlayer(GetTriggerUnit()))
    SetPlayerTechMaxAllowedSwap(FourCC('Redc'), 0, GetOwningPlayer(GetTriggerUnit()))
    SetPlayerTechMaxAllowedSwap(FourCC('Reeb'), 0, GetOwningPlayer(GetTriggerUnit()))
    SetPlayerTechMaxAllowedSwap(FourCC('Reec'), 0, GetOwningPlayer(GetTriggerUnit()))
    SetPlayerTechMaxAllowedSwap(FourCC('Redt'), 0, GetOwningPlayer(GetTriggerUnit()))
    SetPlayerTechMaxAllowedSwap(FourCC('R0G9'), 0, GetOwningPlayer(GetTriggerUnit()))
    SetPlayerTechMaxAllowedSwap(FourCC('R0GA'), 0, GetOwningPlayer(GetTriggerUnit()))
    SetPlayerTechMaxAllowedSwap(FourCC('R0G8'), 0, GetOwningPlayer(GetTriggerUnit()))
    SetPlayerTechResearchedSwap(FourCC('R0GB'), 1, GetOwningPlayer(GetTriggerUnit()))
end
--===========================================================================
function InitTrig_ElfBegFin()
    gg_trg_ElfBegFin=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_ElfBegFin, EVENT_PLAYER_UNIT_RESEARCH_FINISH)
    TriggerRegisterAnyUnitEventBJ(gg_trg_ElfBegFin, EVENT_PLAYER_UNIT_RESEARCH_START)
    TriggerAddCondition(gg_trg_ElfBegFin, Condition(Trig_ElfBegFin_Conditions))
    TriggerAddAction(gg_trg_ElfBegFin, Trig_ElfBegFin_Actions)
end
--===========================================================================
-- Trigger: ElfCan
--===========================================================================
function Trig_ElfCan_Conditions()
    return GetResearched() == FourCC('R0G2')
end
function Trig_ElfCan_Actions()
    SetPlayerTechMaxAllowedSwap(FourCC('R0G1'), 1, GetOwningPlayer(GetTriggerUnit()))
end
--===========================================================================
function InitTrig_ElfCan()
    gg_trg_ElfCan=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_ElfCan, EVENT_PLAYER_UNIT_RESEARCH_CANCEL)
    TriggerAddCondition(gg_trg_ElfCan, Condition(Trig_ElfCan_Conditions))
    TriggerAddAction(gg_trg_ElfCan, Trig_ElfCan_Actions)
end
--===========================================================================
-- Trigger: malfurionPas
--
-- ?? ???? ???? ????, ??? ? ????? ?? ??? ??? - ?????
--===========================================================================
function Trig_malfurionPas_Conditions()
    return GetLearnedSkillBJ() == FourCC('A160')
end
function Trig_malfurionPas_Actions()
    UnitAddAbilityBJ(FourCC('A161'), GetTriggerUnit())
    SetUnitAbilityLevelSwapped(FourCC('A161'), GetTriggerUnit(), GetUnitAbilityLevelSwapped(FourCC('A160'), GetTriggerUnit()))
end
--===========================================================================
function InitTrig_malfurionPas()
    gg_trg_malfurionPas=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_malfurionPas, EVENT_PLAYER_HERO_SKILL)
    TriggerAddCondition(gg_trg_malfurionPas, Condition(Trig_malfurionPas_Conditions))
    TriggerAddAction(gg_trg_malfurionPas, Trig_malfurionPas_Actions)
end
--===========================================================================
-- Trigger: StartBuildingTree
--
-- ??? ????????? ??? ???? ??????, ? ??????? ???????????? ????????? ? ??? ????
--===========================================================================
function Trig_StartBuildingTree_Conditions()
    local id= GetUnitTypeId(GetConstructingStructure())
    return id == FourCC('etoa') or id == FourCC('etol') or id == FourCC('etoe') or id == FourCC('eaoe') or id == FourCC('eaom') or id == FourCC('eaow') or id == FourCC('etrp')
end
function Trig_StartBuildingTree_Actions()
    local pi= GetPlayerId(GetOwningPlayer(GetTriggerUnit()))
    disincome[pi]=disincome[pi] - 6
    udg_UnitsCount[pi]=udg_UnitsCount[pi] - 1
    UpdateGraf(pi)
    Enter(GetTriggerUnit())
end
--===========================================================================
function InitTrig_StartBuildingTree()
    gg_trg_StartBuildingTree=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_StartBuildingTree, EVENT_PLAYER_UNIT_CONSTRUCT_START)
    TriggerAddCondition(gg_trg_StartBuildingTree, Condition(Trig_StartBuildingTree_Conditions))
    TriggerAddAction(gg_trg_StartBuildingTree, Trig_StartBuildingTree_Actions)
end
--===========================================================================
-- Trigger: CanselBuildingTree
--
-- ??? ????????? ??? ???? ??????, ? ??????? ???????????? ????????? ? ??? ????
--===========================================================================
function Trig_CanselBuildingTree_Conditions()
    local id= GetUnitTypeId(GetTriggerUnit())
    return id == FourCC('etoa') or id == FourCC('etol') or id == FourCC('etoe') or id == FourCC('eaoe') or id == FourCC('eaom') or id == FourCC('eaow') or id == FourCC('etrp')
end
function Trig_CanselBuildingTree_Actions()
    local pi= GetPlayerId(GetOwningPlayer(GetTriggerUnit()))
    disincome[pi]=disincome[pi] + 6
    udg_UnitsCount[pi]=udg_UnitsCount[pi] + 1
    UpdateGraf(pi)
    Enter(GetTriggerUnit())
end
--===========================================================================
function InitTrig_CanselBuildingTree()
    gg_trg_CanselBuildingTree=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_CanselBuildingTree, EVENT_PLAYER_UNIT_CONSTRUCT_CANCEL)
    TriggerAddCondition(gg_trg_CanselBuildingTree, Condition(Trig_CanselBuildingTree_Conditions))
    TriggerAddAction(gg_trg_CanselBuildingTree, Trig_CanselBuildingTree_Actions)
end
--===========================================================================
-- Trigger: GuadrianSpell
--===========================================================================
function Trig_GuadrianSpell_Actions()
   -- call BJDebugMsg("")
    MassSpell(GetTriggerUnit() , GetSpellAbilityId() , FourCC('A1MW') , "firebolt" , nil , 400 + 200 * GetUnitAbilityLevel(GetTriggerUnit(), GetSpellAbilityId()) , 1 , false)
end
--===========================================================================
function InitTrig_GuadrianSpell()
    gg_trg_GuadrianSpell=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_GuadrianSpell, EVENT_PLAYER_UNIT_SPELL_EFFECT)
    TriggerAddAction(gg_trg_GuadrianSpell, function()
        if GetSpellAbilityId() ~= FourCC('ken0') then return end
        Trig_GuadrianSpell_Actions()
    end)
end
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
--===========================================================================
-- Trigger: StartWorgens
--===========================================================================
function Trig_StartWorgens_Func001A()
    SetPlayerTechMaxAllowedSwap(FourCC('H0J2'), 1, GetEnumPlayer())
    SetPlayerTechMaxAllowedSwap(FourCC('H0J6'), 1, GetEnumPlayer())
    SetPlayerTechMaxAllowedSwap(FourCC('H0J7'), 1, GetEnumPlayer())
    SetPlayerTechMaxAllowedSwap(FourCC('H0J8'), 1, GetEnumPlayer())
end
function Trig_StartWorgens_Actions()
    ForForce(udg_AllPlayers, Trig_StartWorgens_Func001A)
end
--===========================================================================
function InitTrig_StartWorgens()
    gg_trg_StartWorgens=CreateTrigger()
    TriggerRegisterTimerEventSingle(gg_trg_StartWorgens, 0.01)
    TriggerAddAction(gg_trg_StartWorgens, Trig_StartWorgens_Actions)
end
--===========================================================================
-- Trigger: LegGer
--===========================================================================
function Trig_LegGer_Actions()
    local u= GetTriggerUnit()
    
    
    if GetUnitAbilityLevelSwapped(FourCC('A11U'), GetTriggerUnit()) == 1 then
        UnitAddAbilityBJ(FourCC('A11V'), u)
        RemoveAbilityTimed(u , FourCC('A11V') , 15)
    
    elseif GetUnitAbilityLevelSwapped(FourCC('A11U'), GetTriggerUnit()) == 2 then
        UnitAddAbilityBJ(FourCC('A11W'), u)
        RemoveAbilityTimed(u , FourCC('A11W') , 15)
    
    elseif GetUnitAbilityLevelSwapped(FourCC('A11U'), GetTriggerUnit()) == 3 then
        UnitAddAbilityBJ(FourCC('A11X'), u)
        RemoveAbilityTimed(u , FourCC('A11X') , 15)
    
    elseif GetUnitAbilityLevelSwapped(FourCC('A11U'), GetTriggerUnit()) == 4 then
        UnitAddAbilityBJ(FourCC('A11Y'), u)
        RemoveAbilityTimed(u , FourCC('A11Y') , 15)
      
    end
    u=nil
end
--===========================================================================
function InitTrig_LegGer()
    gg_trg_LegGer=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_LegGer, EVENT_PLAYER_UNIT_SPELL_EFFECT)
    TriggerAddAction(gg_trg_LegGer, function()
        if GetSpellAbilityId() ~= FourCC('A11U') then return end
        Trig_LegGer_Actions()
    end)
end
--===========================================================================
-- Trigger: SpellOpletenie
--===========================================================================
function Trig_SpellOpletenie_Actions()
   -- call BJDebugMsg("")
    MassSpell(GetTriggerUnit() , GetSpellAbilityId() , FourCC('A1MA') , "firebolt" , nil , 600 , 1 , false)
end
--===========================================================================
function InitTrig_SpellOpletenie()
    gg_trg_SpellOpletenie=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_SpellOpletenie, EVENT_PLAYER_UNIT_SPELL_EFFECT)
    TriggerAddAction(gg_trg_SpellOpletenie, function()
        if GetSpellAbilityId() ~= FourCC('A1M9') then return end
        Trig_SpellOpletenie_Actions()
    end)
end
--===========================================================================
-- Trigger: flot1 Copy O
--===========================================================================
function Trig_flot1_Copy_O_Conditions()
    return GetResearched() == FourCC('R073')
end
function Trig_flot1_Copy_O_Actions()
    SetPlayerTechMaxAllowedSwap(FourCC('R072'), 0, GetOwningPlayer(GetTriggerUnit()))
end
--===========================================================================
function InitTrig_flot1_Copy_O()
    gg_trg_flot1_Copy_O=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_flot1_Copy_O, EVENT_PLAYER_UNIT_RESEARCH_FINISH)
    TriggerRegisterAnyUnitEventBJ(gg_trg_flot1_Copy_O, EVENT_PLAYER_UNIT_RESEARCH_START)
    TriggerAddCondition(gg_trg_flot1_Copy_O, Condition(Trig_flot1_Copy_O_Conditions))
    TriggerAddAction(gg_trg_flot1_Copy_O, Trig_flot1_Copy_O_Actions)
end
--===========================================================================
-- Trigger: flot2 Copy O
--===========================================================================
function Trig_flot2_Copy_O_Conditions()
    return GetResearched() == FourCC('R073')
end
function Trig_flot2_Copy_O_Actions()
    SetPlayerTechMaxAllowedSwap(FourCC('R072'), 1, GetOwningPlayer(GetTriggerUnit()))
end
--===========================================================================
function InitTrig_flot2_Copy_O()
    gg_trg_flot2_Copy_O=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_flot2_Copy_O, EVENT_PLAYER_UNIT_RESEARCH_CANCEL)
    TriggerAddCondition(gg_trg_flot2_Copy_O, Condition(Trig_flot2_Copy_O_Conditions))
    TriggerAddAction(gg_trg_flot2_Copy_O, Trig_flot2_Copy_O_Actions)
end
--===========================================================================
-- Trigger: arm1 Copy O
--===========================================================================
function Trig_arm1_Copy_O_Conditions()
    return GetResearched() == FourCC('R072')
end
function Trig_arm1_Copy_O_Actions()
    SetPlayerTechMaxAllowedSwap(FourCC('R073'), 0, GetOwningPlayer(GetTriggerUnit()))
end
--===========================================================================
function InitTrig_arm1_Copy_O()
    gg_trg_arm1_Copy_O=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_arm1_Copy_O, EVENT_PLAYER_UNIT_RESEARCH_FINISH)
    TriggerRegisterAnyUnitEventBJ(gg_trg_arm1_Copy_O, EVENT_PLAYER_UNIT_RESEARCH_START)
    TriggerAddCondition(gg_trg_arm1_Copy_O, Condition(Trig_arm1_Copy_O_Conditions))
    TriggerAddAction(gg_trg_arm1_Copy_O, Trig_arm1_Copy_O_Actions)
end
--===========================================================================
-- Trigger: arm2 Copy O
--===========================================================================
function Trig_arm2_Copy_O_Conditions()
    return GetResearched() == FourCC('R072')
end
function Trig_arm2_Copy_O_Actions()
    SetPlayerTechMaxAllowedSwap(FourCC('R073'), 1, GetOwningPlayer(GetTriggerUnit()))
end
--===========================================================================
function InitTrig_arm2_Copy_O()
    gg_trg_arm2_Copy_O=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_arm2_Copy_O, EVENT_PLAYER_UNIT_RESEARCH_CANCEL)
    TriggerAddCondition(gg_trg_arm2_Copy_O, Condition(Trig_arm2_Copy_O_Conditions))
    TriggerAddAction(gg_trg_arm2_Copy_O, Trig_arm2_Copy_O_Actions)
end
--===========================================================================
-- Trigger: BuidAltar
--===========================================================================
function Trig_BuidAltar_Conditions()
    return GetUnitTypeId(GetTriggerUnit()) == FourCC('h0CV')
end
function Trig_BuidAltar_Actions()
    UnitAddAbilityBJ(FourCC('Asud'), GetTriggerUnit())
    AddUnitToStockBJ(FourCC('h07A'), GetTriggerUnit(), 1, 1)
end
--===========================================================================
function InitTrig_BuidAltar()
    gg_trg_BuidAltar=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_BuidAltar, EVENT_PLAYER_UNIT_UPGRADE_FINISH)
    TriggerAddCondition(gg_trg_BuidAltar, Condition(Trig_BuidAltar_Conditions))
    TriggerAddAction(gg_trg_BuidAltar, Trig_BuidAltar_Actions)
end
--===========================================================================
-- Trigger: Auto set Copy O
--===========================================================================
function Trig_Auto_set_Copy_O_Actions()
    IssueTargetOrderBJ(GetTriggerUnit(), "ensnare", GetSpellTargetUnit())
end
--===========================================================================
function InitTrig_Auto_set_Copy_O()
    gg_trg_Auto_set_Copy_O=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_Auto_set_Copy_O, EVENT_PLAYER_UNIT_SPELL_EFFECT)
    TriggerAddAction(gg_trg_Auto_set_Copy_O, function()
        if GetSpellAbilityId() ~= FourCC('A09U') then return end
        Trig_Auto_set_Copy_O_Actions()
    end)
end
--===========================================================================
-- Trigger: AutocastSlowOn
--===========================================================================
function Trig_AutocastSlowOn_Conditions()
    return GetResearched() == FourCC('R04S') and GetPlayerTechCount(GetOwningPlayer(GetTriggerUnit()), FourCC('R04S'), true) == 2
end
function Trig_AutocastSlowOn_Actions()
    GlobalIssue(FourCC('A09S') , GetOwningPlayer(GetTriggerUnit()) , "slowon")
end
--===========================================================================
function InitTrig_AutocastSlowOn()
    gg_trg_AutocastSlowOn=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_AutocastSlowOn, EVENT_PLAYER_UNIT_RESEARCH_FINISH)
    TriggerAddCondition(gg_trg_AutocastSlowOn, Condition(Trig_AutocastSlowOn_Conditions))
    TriggerAddAction(gg_trg_AutocastSlowOn, Trig_AutocastSlowOn_Actions)
end
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
--===========================================================================
-- Trigger: Draenei Build Abill
--===========================================================================
function Trig_Draenei_Build_Abill_Conditions()
    return GetUnitAbilityLevel(GetConstructingStructure(), FourCC('A0Z3')) > 0
end
function Trig_Draenei_Build_Abill_Actions()
    local u= GetConstructingStructure()
    --call BJDebugMsg("2")
    if Random(1 , 2) and GetPlayerTechCount(GetOwningPlayer(u), FourCC('R0EB'), true) > 0 then
        TriggerSleepAction(0)
        SetBuildingProgressTimed(u , 20 , 0)
        --call BJDebugMsg("3")
    end
    UnitRemoveAbility(u, FourCC('A0Z3'))
    u=nil
end
--===========================================================================
function InitTrig_Draenei_Build_Abill()
    gg_trg_Draenei_Build_Abill=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_Draenei_Build_Abill, EVENT_PLAYER_UNIT_CONSTRUCT_START)
    TriggerAddCondition(gg_trg_Draenei_Build_Abill, Condition(Trig_Draenei_Build_Abill_Conditions))
    TriggerAddAction(gg_trg_Draenei_Build_Abill, Trig_Draenei_Build_Abill_Actions)
end
--===========================================================================
-- Trigger: flot1
--===========================================================================
function Trig_flot1_Conditions()
    return GetResearched() == FourCC('R027')
end
function Trig_flot1_Actions()
    SetPlayerTechMaxAllowedSwap(FourCC('R02S'), 0, GetOwningPlayer(GetTriggerUnit()))
end
--===========================================================================
function InitTrig_flot1()
    gg_trg_flot1=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_flot1, EVENT_PLAYER_UNIT_RESEARCH_FINISH)
    TriggerRegisterAnyUnitEventBJ(gg_trg_flot1, EVENT_PLAYER_UNIT_RESEARCH_START)
    TriggerAddCondition(gg_trg_flot1, Condition(Trig_flot1_Conditions))
    TriggerAddAction(gg_trg_flot1, Trig_flot1_Actions)
end
--===========================================================================
-- Trigger: flot2
--===========================================================================
function Trig_flot2_Conditions()
    return GetResearched() == FourCC('R027')
end
function Trig_flot2_Actions()
    SetPlayerTechMaxAllowedSwap(FourCC('R02S'), 1, GetOwningPlayer(GetTriggerUnit()))
end
--===========================================================================
function InitTrig_flot2()
    gg_trg_flot2=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_flot2, EVENT_PLAYER_UNIT_RESEARCH_CANCEL)
    TriggerAddCondition(gg_trg_flot2, Condition(Trig_flot2_Conditions))
    TriggerAddAction(gg_trg_flot2, Trig_flot2_Actions)
end
--===========================================================================
-- Trigger: arm1
--===========================================================================
function Trig_arm1_Conditions()
    return GetResearched() == FourCC('R02S')
end
function Trig_arm1_Actions()
    SetPlayerTechMaxAllowedSwap(FourCC('R027'), 0, GetOwningPlayer(GetTriggerUnit()))
end
--===========================================================================
function InitTrig_arm1()
    gg_trg_arm1=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_arm1, EVENT_PLAYER_UNIT_RESEARCH_FINISH)
    TriggerRegisterAnyUnitEventBJ(gg_trg_arm1, EVENT_PLAYER_UNIT_RESEARCH_START)
    TriggerAddCondition(gg_trg_arm1, Condition(Trig_arm1_Conditions))
    TriggerAddAction(gg_trg_arm1, Trig_arm1_Actions)
end
--===========================================================================
-- Trigger: arm2
--===========================================================================
function Trig_arm2_Conditions()
    return GetResearched() == FourCC('R02S')
end
function Trig_arm2_Actions()
    SetPlayerTechMaxAllowedSwap(FourCC('R027'), 1, GetOwningPlayer(GetTriggerUnit()))
end
--===========================================================================
function InitTrig_arm2()
    gg_trg_arm2=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_arm2, EVENT_PLAYER_UNIT_RESEARCH_CANCEL)
    TriggerAddCondition(gg_trg_arm2, Condition(Trig_arm2_Conditions))
    TriggerAddAction(gg_trg_arm2, Trig_arm2_Actions)
end
--===========================================================================
-- Trigger: Auto pohichenie Copy
--===========================================================================
function Trig_Auto_pohichenie_Copy_Actions()
    IssueTargetOrderBJ(GetTriggerUnit(), "banish", GetSpellTargetUnit())
end
--===========================================================================
function InitTrig_Auto_pohichenie_Copy()
    gg_trg_Auto_pohichenie_Copy=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_Auto_pohichenie_Copy, EVENT_PLAYER_UNIT_SPELL_EFFECT)
    TriggerAddAction(gg_trg_Auto_pohichenie_Copy, function()
        if GetSpellAbilityId() ~= FourCC('A031') then return end
        Trig_Auto_pohichenie_Copy_Actions()
    end)
end
--===========================================================================
-- Trigger: IllidaryOn
--===========================================================================
function Trig_IllidaryOn_Actions()
    EnableTrigger(gg_trg_IllyFire)
    EnableTrigger(gg_trg_IllyAgile)
    
    EnableTrigger(gg_trg_IllyPain)
    EnableTrigger(gg_trg_IlliKnives)
    EnableTrigger(gg_trg_IllyAttack)
    EnableTrigger(gg_trg_RuvokAutoIlly)
    --call EnableTrigger( gg_trg_SandStrike )
   
end
--===========================================================================
function InitTrig_IllidaryOn()
    gg_trg_IllidaryOn=CreateTrigger()
    TriggerAddAction(gg_trg_IllidaryOn, Trig_IllidaryOn_Actions)
end
--===========================================================================
-- Trigger: flot1 Copy 2
--===========================================================================
function Trig_flot1_Copy_2_Conditions()
    return GetResearched() == FourCC('R099')
end
function Trig_flot1_Copy_2_Actions()
    SetPlayerTechMaxAllowedSwap(FourCC('R09A'), 0, GetOwningPlayer(GetTriggerUnit()))
    SetPlayerTechMaxAllowedSwap(FourCC('R09B'), 0, GetOwningPlayer(GetTriggerUnit()))
end
--===========================================================================
function InitTrig_flot1_Copy_2()
    gg_trg_flot1_Copy_2=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_flot1_Copy_2, EVENT_PLAYER_UNIT_RESEARCH_FINISH)
    TriggerRegisterAnyUnitEventBJ(gg_trg_flot1_Copy_2, EVENT_PLAYER_UNIT_RESEARCH_START)
    TriggerAddCondition(gg_trg_flot1_Copy_2, Condition(Trig_flot1_Copy_2_Conditions))
    TriggerAddAction(gg_trg_flot1_Copy_2, Trig_flot1_Copy_2_Actions)
end
--===========================================================================
-- Trigger: flot2 Copy 2
--===========================================================================
function Trig_flot2_Copy_2_Conditions()
    return GetResearched() == FourCC('R099')
end
function Trig_flot2_Copy_2_Actions()
    SetPlayerTechMaxAllowedSwap(FourCC('R09A'), 1, GetOwningPlayer(GetTriggerUnit()))
    SetPlayerTechMaxAllowedSwap(FourCC('R09B'), 1, GetOwningPlayer(GetTriggerUnit()))
end
--===========================================================================
function InitTrig_flot2_Copy_2()
    gg_trg_flot2_Copy_2=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_flot2_Copy_2, EVENT_PLAYER_UNIT_RESEARCH_CANCEL)
    TriggerAddCondition(gg_trg_flot2_Copy_2, Condition(Trig_flot2_Copy_2_Conditions))
    TriggerAddAction(gg_trg_flot2_Copy_2, Trig_flot2_Copy_2_Actions)
end
--===========================================================================
-- Trigger: arm1 Copy 2
--===========================================================================
function Trig_arm1_Copy_2_Conditions()
    return GetResearched() == FourCC('R09A')
end
function Trig_arm1_Copy_2_Actions()
    SetPlayerTechMaxAllowedSwap(FourCC('R099'), 0, GetOwningPlayer(GetTriggerUnit()))
    SetPlayerTechMaxAllowedSwap(FourCC('R09B'), 0, GetOwningPlayer(GetTriggerUnit()))
end
--===========================================================================
function InitTrig_arm1_Copy_2()
    gg_trg_arm1_Copy_2=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_arm1_Copy_2, EVENT_PLAYER_UNIT_RESEARCH_FINISH)
    TriggerRegisterAnyUnitEventBJ(gg_trg_arm1_Copy_2, EVENT_PLAYER_UNIT_RESEARCH_START)
    TriggerAddCondition(gg_trg_arm1_Copy_2, Condition(Trig_arm1_Copy_2_Conditions))
    TriggerAddAction(gg_trg_arm1_Copy_2, Trig_arm1_Copy_2_Actions)
end
--===========================================================================
-- Trigger: arm2 Copy 2
--===========================================================================
function Trig_arm2_Copy_2_Conditions()
    return GetResearched() == FourCC('R09A')
end
function Trig_arm2_Copy_2_Actions()
    SetPlayerTechMaxAllowedSwap(FourCC('R099'), 1, GetOwningPlayer(GetTriggerUnit()))
    SetPlayerTechMaxAllowedSwap(FourCC('R09B'), 1, GetOwningPlayer(GetTriggerUnit()))
end
--===========================================================================
function InitTrig_arm2_Copy_2()
    gg_trg_arm2_Copy_2=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_arm2_Copy_2, EVENT_PLAYER_UNIT_RESEARCH_CANCEL)
    TriggerAddCondition(gg_trg_arm2_Copy_2, Condition(Trig_arm2_Copy_2_Conditions))
    TriggerAddAction(gg_trg_arm2_Copy_2, Trig_arm2_Copy_2_Actions)
end
--===========================================================================
-- Trigger: arm1 Copy 2 Copy
--===========================================================================
function Trig_arm1_Copy_2_Copy_Conditions()
    return GetResearched() == FourCC('R09B')
end
function Trig_arm1_Copy_2_Copy_Actions()
    SetPlayerTechMaxAllowedSwap(FourCC('R099'), 0, GetOwningPlayer(GetTriggerUnit()))
    SetPlayerTechMaxAllowedSwap(FourCC('R09A'), 0, GetOwningPlayer(GetTriggerUnit()))
end
--===========================================================================
function InitTrig_arm1_Copy_2_Copy()
    gg_trg_arm1_Copy_2_Copy=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_arm1_Copy_2_Copy, EVENT_PLAYER_UNIT_RESEARCH_FINISH)
    TriggerRegisterAnyUnitEventBJ(gg_trg_arm1_Copy_2_Copy, EVENT_PLAYER_UNIT_RESEARCH_START)
    TriggerAddCondition(gg_trg_arm1_Copy_2_Copy, Condition(Trig_arm1_Copy_2_Copy_Conditions))
    TriggerAddAction(gg_trg_arm1_Copy_2_Copy, Trig_arm1_Copy_2_Copy_Actions)
end
--===========================================================================
-- Trigger: arm2 Copy 2 Copy
--===========================================================================
function Trig_arm2_Copy_2_Copy_Conditions()
    return GetResearched() == FourCC('R09B')
end
function Trig_arm2_Copy_2_Copy_Actions()
    SetPlayerTechMaxAllowedSwap(FourCC('R099'), 1, GetOwningPlayer(GetTriggerUnit()))
    SetPlayerTechMaxAllowedSwap(FourCC('R09A'), 1, GetOwningPlayer(GetTriggerUnit()))
end
--===========================================================================
function InitTrig_arm2_Copy_2_Copy()
    gg_trg_arm2_Copy_2_Copy=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_arm2_Copy_2_Copy, EVENT_PLAYER_UNIT_RESEARCH_CANCEL)
    TriggerAddCondition(gg_trg_arm2_Copy_2_Copy, Condition(Trig_arm2_Copy_2_Copy_Conditions))
    TriggerAddAction(gg_trg_arm2_Copy_2_Copy, Trig_arm2_Copy_2_Copy_Actions)
end
--===========================================================================
-- Trigger: EnemyPower
--===========================================================================
function Trig_EnemyPower_Conditions()
    return GetUnitAbilityLevel(GetEventDamageSource(), FourCC('A0O5')) > 0 and GetPlayerTechCount(GetOwningPlayer(GetEventDamageSource()), FourCC('R096'), true) > 0
end
function Trig_EnemyPower_Actions()
    --call SetUnitState(GetEventDamageSource(),UNIT_STATE_LIFE,
    if BlzGetEventAttackType() == ATTACK_TYPE_NORMAL then
        SetUnitLifePercentBJ(GetEventDamageSource(), GetUnitLifePercent(GetEventDamageSource()) + 0.25)
    else
        SetUnitLifePercentBJ(GetEventDamageSource(), GetUnitLifePercent(GetEventDamageSource()) + 0.5)
    
    end
    
end
--===========================================================================
function InitTrig_EnemyPower()
    gg_trg_EnemyPower=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_EnemyPower, EVENT_PLAYER_UNIT_DAMAGED)
    TriggerAddCondition(gg_trg_EnemyPower, Condition(Trig_EnemyPower_Conditions))
    TriggerAddAction(gg_trg_EnemyPower, Trig_EnemyPower_Actions)
end
--===========================================================================
-- Trigger: AutoStrelaFireIlly
--===========================================================================
function Trig_AutoStrelaFireIlly_Actions()
    IssueTargetOrderBJ(GetTriggerUnit(), "firebolt", GetSpellTargetUnit())
end
--===========================================================================
function InitTrig_AutoStrelaFireIlly()
    gg_trg_AutoStrelaFireIlly=CreateTrigger()
    
    TriggerRegisterAnyUnitEventBJ(gg_trg_AutoStrelaFireIlly, EVENT_PLAYER_UNIT_SPELL_EFFECT)
    TriggerAddAction(gg_trg_AutoStrelaFireIlly, function()
        if GetSpellAbilityId() ~= FourCC('A1KL') then return end
        Trig_AutoStrelaFireIlly_Actions()
    end)
end
--===========================================================================
-- Trigger: AutoStrelaFelllly
--===========================================================================
function Trig_AutoStrelaFelllly_Actions()
    IssueTargetOrderBJ(GetTriggerUnit(), "acidbomb", GetSpellTargetUnit())
end
--===========================================================================
function InitTrig_AutoStrelaFelllly()
    gg_trg_AutoStrelaFelllly=CreateTrigger()
    
    TriggerRegisterAnyUnitEventBJ(gg_trg_AutoStrelaFelllly, EVENT_PLAYER_UNIT_SPELL_EFFECT)
    TriggerAddAction(gg_trg_AutoStrelaFelllly, function()
        if GetSpellAbilityId() ~= FourCC('A1KO') then return end
        Trig_AutoStrelaFelllly_Actions()
    end)
end
--===========================================================================
-- Trigger: IllyFire
--===========================================================================
function Trig_IllyFire_Func001Func001Func002Func001C()
    return GetUnitAbilityLevelSwapped(FourCC('A0NJ'), GetTriggerUnit()) == 4
end
function Trig_IllyFire_Func001Func001Func002C()
    return GetUnitAbilityLevelSwapped(FourCC('A0NJ'), GetTriggerUnit()) == 3
end
function Trig_IllyFire_Func001Func001C()
    return GetUnitAbilityLevelSwapped(FourCC('A0NJ'), GetTriggerUnit()) == 2
end
function Trig_IllyFire_Func001C()
    return GetUnitAbilityLevelSwapped(FourCC('A0NJ'), GetTriggerUnit()) == 1
end
function Trig_IllyFire_Actions()
    if Trig_IllyFire_Func001C() then
        UnitAddAbilityBJ(FourCC('A0NO'), GetTriggerUnit())
        UnitAddAbilityBJ(FourCC('A0NM'), GetTriggerUnit())
        TriggerSleepAction(15.00)
        UnitRemoveAbilityBJ(FourCC('A0NO'), GetTriggerUnit())
        UnitRemoveAbilityBJ(FourCC('A0NM'), GetTriggerUnit())
    else
        if Trig_IllyFire_Func001Func001C() then
            UnitAddAbilityBJ(FourCC('A0NP'), GetTriggerUnit())
            UnitAddAbilityBJ(FourCC('A0NK'), GetTriggerUnit())
            TriggerSleepAction(15.00)
            UnitRemoveAbilityBJ(FourCC('A0NP'), GetTriggerUnit())
            UnitRemoveAbilityBJ(FourCC('A0NK'), GetTriggerUnit())
        else
            if Trig_IllyFire_Func001Func001Func002C() then
                UnitAddAbilityBJ(FourCC('A0NR'), GetTriggerUnit())
                UnitAddAbilityBJ(FourCC('A0NL'), GetTriggerUnit())
                TriggerSleepAction(15.00)
                UnitRemoveAbilityBJ(FourCC('A0NR'), GetTriggerUnit())
                UnitRemoveAbilityBJ(FourCC('A0NL'), GetTriggerUnit())
            else
                if Trig_IllyFire_Func001Func001Func002Func001C() then
                    UnitAddAbilityBJ(FourCC('A0NQ'), GetTriggerUnit())
                    UnitAddAbilityBJ(FourCC('A0NN'), GetTriggerUnit())
                    TriggerSleepAction(15.00)
                    UnitRemoveAbilityBJ(FourCC('A0NQ'), GetTriggerUnit())
                    UnitRemoveAbilityBJ(FourCC('A0NN'), GetTriggerUnit())
                end
            end
        end
    end
end
--===========================================================================
function InitTrig_IllyFire()
    gg_trg_IllyFire=CreateTrigger()
    DisableTrigger(gg_trg_IllyFire)
    TriggerRegisterAnyUnitEventBJ(gg_trg_IllyFire, EVENT_PLAYER_UNIT_SPELL_EFFECT)
    TriggerAddAction(gg_trg_IllyFire, function()
        if GetSpellAbilityId() ~= FourCC('A0NJ') then return end
        Trig_IllyFire_Actions()
    end)
end
--===========================================================================
-- Trigger: IllyAgile
--===========================================================================
function Trig_IllyAgile_Actions()
    
    local u= GetTriggerUnit()
    UnitAddAbility(u, FourCC('A0NI'))
    RemoveAbilityTimed(u , FourCC('A0NI') , 20)
    u=nil
    
    
end
--===========================================================================
function InitTrig_IllyAgile()
    gg_trg_IllyAgile=CreateTrigger()
    DisableTrigger(gg_trg_IllyAgile)
    TriggerRegisterAnyUnitEventBJ(gg_trg_IllyAgile, EVENT_PLAYER_UNIT_SPELL_EFFECT)
    TriggerAddAction(gg_trg_IllyAgile, function()
        if GetSpellAbilityId() ~= FourCC('A0NH') then return end
        Trig_IllyAgile_Actions()
    end)
end
--===========================================================================
-- Trigger: IllyPain
--===========================================================================
function Trig_IllyPain_Actions()
    local u= GetTriggerUnit()
    UnitAddAbility(u, FourCC('A0NT'))
    RemoveAbilityTimed(u , FourCC('A0NT') , 20)
    u=nil
end
--===========================================================================
function InitTrig_IllyPain()
    gg_trg_IllyPain=CreateTrigger()
    DisableTrigger(gg_trg_IllyPain)
    TriggerRegisterAnyUnitEventBJ(gg_trg_IllyPain, EVENT_PLAYER_UNIT_SPELL_EFFECT)
    TriggerAddAction(gg_trg_IllyPain, function()
        if GetSpellAbilityId() ~= FourCC('A0NU') then return end
        Trig_IllyPain_Actions()
    end)
end
--===========================================================================
-- Trigger: IlliKnives
--===========================================================================
function Trig_IlliKnives_Actions()
    local u= GetTriggerUnit()
    UnitAddAbility(u, FourCC('A0NY'))
    RemoveAbilityTimed(u , FourCC('A0NY') , 20)
    u=nil
end
--===========================================================================
function InitTrig_IlliKnives()
    gg_trg_IlliKnives=CreateTrigger()
    DisableTrigger(gg_trg_IlliKnives)
    TriggerRegisterAnyUnitEventBJ(gg_trg_IlliKnives, EVENT_PLAYER_UNIT_SPELL_EFFECT)
    TriggerAddAction(gg_trg_IlliKnives, function()
        if GetSpellAbilityId() ~= FourCC('A0NV') then return end
        Trig_IlliKnives_Actions()
    end)
end
--===========================================================================
-- Trigger: RuvokAutoIlly
--===========================================================================
function Trig_RuvokAutoIlly_Actions()
    IssueTargetOrderBJ(GetTriggerUnit(), "deathcoil", GetSpellTargetUnit())
end
--===========================================================================
function InitTrig_RuvokAutoIlly()
    gg_trg_RuvokAutoIlly=CreateTrigger()
    DisableTrigger(gg_trg_RuvokAutoIlly)
    TriggerRegisterAnyUnitEventBJ(gg_trg_RuvokAutoIlly, EVENT_PLAYER_UNIT_SPELL_EFFECT)
    TriggerAddAction(gg_trg_RuvokAutoIlly, function()
        if GetSpellAbilityId() ~= FourCC('A048') then return end
        Trig_RuvokAutoIlly_Actions()
    end)
end
--===========================================================================
-- Trigger: SandStrike
--===========================================================================
function Trig_SandStrike_Func001C()
    return udg_SSinteger[0] == 0
end
function Trig_SandStrike_Actions()
    if Trig_SandStrike_Func001C() then
        EnableTrigger(gg_trg_Sand_Strike_Loop)
    end
    udg_SSinteger[0]=( udg_SSinteger[0] + 1 )
    udg_SSinteger[1]=( udg_SSinteger[1] + 1 )
    udg_SScaster[udg_SSinteger[1]]=GetTriggerUnit()
    SetUnitPathing(udg_SScaster[udg_SSinteger[1]], false)
    udg_SSfacing[udg_SSinteger[1]]=GetUnitFacing(udg_SScaster[udg_SSinteger[1]])
    udg_SSpointcaster[udg_SSinteger[1]]=GetUnitLoc(udg_SScaster[udg_SSinteger[1]])
    udg_SSdamage[udg_SSinteger[1]]=( 5.00 + I2R(GetUnitAbilityLevelSwapped(FourCC('A0NF'), udg_SScaster[udg_SSinteger[1]])) )
    udg_SStargetpoint[udg_SSinteger[1]]=GetSpellTargetLoc()
    udg_SSeffect[udg_SSinteger[1]]="AbilitiesWeaponsAncientProtectorMissileAncientProtectorMissile.mdl"
    udg_SS[udg_SSinteger[1]]=( GetUnitAbilityLevelSwapped(FourCC('A0NF'), udg_SScaster[udg_SSinteger[1]]) + 30 )
    PauseUnitBJ(true, GetTriggerUnit())
    RemoveLocation(udg_SSpointcaster[udg_SSinteger[1]])
    RemoveLocation(udg_SStargetpoint[udg_SSinteger[1]])
end
--===========================================================================
function InitTrig_SandStrike()
    gg_trg_SandStrike=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_SandStrike, EVENT_PLAYER_UNIT_SPELL_EFFECT)
    TriggerAddAction(gg_trg_SandStrike, function()
        if GetSpellAbilityId() ~= FourCC('A0NF') then return end
        Trig_SandStrike_Actions()
    end)
end
--===========================================================================
-- Trigger: Sand Strike Loop
--===========================================================================
function Trig_Sand_Strike_Loop_Func001Func001Func003C()
    return IsTerrainPathableBJ(udg_SSpointmovecaster[udg_SSinteger[2]], PATHING_TYPE_WALKABILITY)
end
function Trig_Sand_Strike_Loop_Func001Func001Func004002003001()
    return IsUnitEnemy(GetFilterUnit(), GetOwningPlayer(udg_SScaster[udg_SSinteger[2]]))
end
function Trig_Sand_Strike_Loop_Func001Func001Func004002003002()
    return IsUnitAliveBJ(GetFilterUnit())
end
function Trig_Sand_Strike_Loop_Func001Func001Func004002003()
    return GetBooleanAnd(IsUnitEnemy(GetFilterUnit(), GetOwningPlayer(udg_SScaster[udg_SSinteger[2]])), IsUnitAliveBJ(GetFilterUnit())) -- INLINED!!
end
function Trig_Sand_Strike_Loop_Func001Func001Func007Func004C()
    return not (IsUnitType(udg_SSpicked[udg_SSinteger[2]], UNIT_TYPE_STRUCTURE))
end
function Trig_Sand_Strike_Loop_Func001Func001Func007A()
    udg_SSpicked[udg_SSinteger[2]]=GetEnumUnit()
    udg_SSpointpicked[udg_SSinteger[2]]=GetUnitLoc(udg_SSpicked[udg_SSinteger[2]])
    udg_SSpointmovepicked[udg_SSinteger[2]]=PolarProjectionBJ(udg_SSpointpicked[udg_SSinteger[2]], I2R(udg_SS[udg_SSinteger[2]]), GetUnitFacing(udg_SSpicked[udg_SSinteger[2]]))
    if Trig_Sand_Strike_Loop_Func001Func001Func007Func004C() then
        SetUnitPositionLoc(udg_SSpicked[udg_SSinteger[2]], udg_SSpointmovepicked[udg_SSinteger[2]])
    end
    UnitDamageTargetBJ(udg_SScaster[udg_SSinteger[2]], udg_SSpicked[udg_SSinteger[3]], udg_SSdamage[udg_SSinteger[2]], ATTACK_TYPE_NORMAL, DAMAGE_TYPE_NORMAL)
    udg_SSpicked[udg_SSinteger[2]]=nil
    RemoveLocation(udg_SSpointpicked[udg_SSinteger[2]])
    RemoveLocation(udg_SSpointmovepicked[udg_SSinteger[2]])
end
function Trig_Sand_Strike_Loop_Func001Func001Func011Func004C()
    return udg_SSinteger[0] == 0
end
function Trig_Sand_Strike_Loop_Func001Func001Func011C()
    return udg_SS[udg_SSinteger[2]] == 0
end
function Trig_Sand_Strike_Loop_Func001Func001C()
    return udg_SS[udg_SSinteger[2]] ~= 0
end
function Trig_Sand_Strike_Loop_Actions()
    udg_SSinteger[2]=1
    while true do
        if udg_SSinteger[2] > udg_SSinteger[1] then break end
        if Trig_Sand_Strike_Loop_Func001Func001C() then
            udg_SSpointcaster[udg_SSinteger[2]]=GetUnitLoc(udg_SScaster[udg_SSinteger[2]])
            udg_SSpointmovecaster[udg_SSinteger[2]]=PolarProjectionBJ(udg_SSpointcaster[udg_SSinteger[2]], I2R(udg_SS[udg_SSinteger[2]]), udg_SSfacing[udg_SSinteger[2]])
            if Trig_Sand_Strike_Loop_Func001Func001Func003C() then
                RemoveLocation(udg_SSpointmovecaster[udg_SSinteger[2]])
                udg_SSpointmovecaster[udg_SSinteger[2]]=PolarProjectionBJ(udg_SSpointcaster[udg_SSinteger[2]], I2R(udg_SS[udg_SSinteger[2]]), ( udg_SSfacing[udg_SSinteger[2]] - 180.00 ))
            end
            udg_SSgroup[udg_SSinteger[2]]=GetUnitsInRangeOfLocMatching(150.00, udg_SSpointcaster[udg_SSinteger[2]], Condition(Trig_Sand_Strike_Loop_Func001Func001Func004002003))
            udg_SS[udg_SSinteger[2]]=( udg_SS[udg_SSinteger[2]] - 1 )
            SetUnitPositionLoc(udg_SScaster[udg_SSinteger[2]], udg_SSpointmovecaster[udg_SSinteger[2]])
            ForGroupBJ(udg_SSgroup[udg_SSinteger[2]], Trig_Sand_Strike_Loop_Func001Func001Func007A)
            RemoveLocation(udg_SSpointmovecaster[udg_SSinteger[2]])
            DestroyGroup(udg_SSgroup[udg_SSinteger[2]])
            RemoveLocation(udg_SSpointcaster[udg_SSinteger[2]])
            if Trig_Sand_Strike_Loop_Func001Func001Func011C() then
                SetUnitPathing(udg_SScaster[udg_SSinteger[2]], true)
                PauseUnitBJ(false, udg_SScaster[udg_SSinteger[2]])
                udg_SSinteger[0]=( udg_SSinteger[0] - 1 )
                if Trig_Sand_Strike_Loop_Func001Func001Func011Func004C() then
                    udg_SSinteger[1]=0
                    DisableTrigger(GetTriggeringTrigger())
                end
            end
        end
        udg_SSinteger[2]=udg_SSinteger[2] + 1
    end
end
--===========================================================================
function InitTrig_Sand_Strike_Loop()
    gg_trg_Sand_Strike_Loop=CreateTrigger()
    DisableTrigger(gg_trg_Sand_Strike_Loop)
    TriggerRegisterTimerEventPeriodic(gg_trg_Sand_Strike_Loop, 0.04)
    TriggerAddAction(gg_trg_Sand_Strike_Loop, Trig_Sand_Strike_Loop_Actions)
end
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
--===========================================================================
-- Trigger: PoleAstralaDragons
--===========================================================================
function Trig_PoleAstralaDragons_Func003002()
    return 0 == 0
end
function Trig_PoleAstralaDragons_Func005A()
    local u
    CreateNUnitsAtLoc(1, FourCC('H0BN'), GetOwningPlayer(GetTriggerUnit()), udg_LocalPosition[14], bj_UNIT_FACING)
    UnitAddAbilityBJ(FourCC('AHbn'), GetLastCreatedUnit())
    SetUnitManaBJ(GetLastCreatedUnit(), 1111111.00)
    SetUnitAbilityLevelSwapped(FourCC('AHbn'), GetLastCreatedUnit(), GetUnitAbilityLevelSwapped(FourCC('A08R'), GetTriggerUnit()))
    IssueTargetOrderBJ(GetLastCreatedUnit(), "banish", GetEnumUnit())
    u=udg_LocalUnit[1]
    UnitApplyTimedLife(u, FourCC('BTLF'), 2)
    u=nil
end
function Trig_PoleAstralaDragons_Actions()
    udg_LocalPosition[14]=GetUnitLoc(GetTriggerUnit())
    udg_LocalPosition2=GetSpellTargetLoc()
    udg_Boolexpr = Trig_PoleAstralaDragons_Func003002
    GroupEnumUnitsInRangeOfLoc(udg_LocalOtrad2, udg_LocalPosition2, 200, udg_Boolexpr)
    ForGroupBJ(udg_LocalOtrad2, Trig_PoleAstralaDragons_Func005A)
    RemoveLocation(udg_LocalPosition[14])
end
--===========================================================================
function InitTrig_PoleAstralaDragons()
    gg_trg_PoleAstralaDragons=CreateTrigger()
    DisableTrigger(gg_trg_PoleAstralaDragons)
    TriggerRegisterAnyUnitEventBJ(gg_trg_PoleAstralaDragons, EVENT_PLAYER_UNIT_SPELL_EFFECT)
    TriggerAddAction(gg_trg_PoleAstralaDragons, function()
        if GetSpellAbilityId() ~= FourCC('A0QV') then return end
        Trig_PoleAstralaDragons_Actions()
    end)
end
--===========================================================================
-- Trigger: Dark Dragon
--===========================================================================
function Trig_Dark_Dragon_Func001A()
    SetPlayerTechMaxAllowedSwap(FourCC('n03O'), 0, GetEnumPlayer())
end
function Trig_Dark_Dragon_Actions()
    ForForce(udg_AllPlayers, Trig_Dark_Dragon_Func001A)
end
--===========================================================================
function InitTrig_Dark_Dragon()
    gg_trg_Dark_Dragon=CreateTrigger()
    TriggerRegisterTimerEventSingle(gg_trg_Dark_Dragon, 5)
    TriggerAddAction(gg_trg_Dark_Dragon, Trig_Dark_Dragon_Actions)
end
--===========================================================================
-- Trigger: Old Dark Dragon
--===========================================================================
function Trig_Old_Dark_Dragon_Func001A()
    SetPlayerTechMaxAllowedSwap(FourCC('n03P'), 0, GetEnumPlayer())
end
function Trig_Old_Dark_Dragon_Actions()
    ForForce(udg_AllPlayers, Trig_Old_Dark_Dragon_Func001A)
end
--===========================================================================
function InitTrig_Old_Dark_Dragon()
    gg_trg_Old_Dark_Dragon=CreateTrigger()
    TriggerRegisterTimerEventSingle(gg_trg_Old_Dark_Dragon, 5)
    TriggerAddAction(gg_trg_Old_Dark_Dragon, Trig_Old_Dark_Dragon_Actions)
end
--===========================================================================
-- Trigger: FlyDragon
--===========================================================================
--================
function Trig_Charge_move_heroD()
    local t= GetExpiredTimer()
    local h= GetHandleId(t)
    local GT= LoadUnitHandle(Hash, h, 1)
    local l= LoadReal(Hash, h, 2)
    local g
    local x1= LoadReal(Hash, h, 4)
    local y1= LoadReal(Hash, h, 5)
    local fl= LoadReal(Hash, h, 6)
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
    x=dx + 6 * Cos(ugol * bj_DEGTORAD) --????????? ????????? ?
    y=dy + 6 * Sin(ugol * bj_DEGTORAD) --????????? ????????? ?
    w=JSTRParabolaZ(MaxW , l , JSTRRastMT(x , x1 , y , y1)) --????????? ??????
    
    -- ???? ????? ????
    if JSTRRastMT(x1 , dx , y1 , dy) > 25 then --and not IsTerrainPathable(x, y, PATHING_TYPE_WALKABILITY) then
        -- ??????? ?????
        SetUnitX(GT, x)
        SetUnitY(GT, y)
        SetUnitFacing(GT, ugol)
        SetUnitFlyHeight(GT, fl + w, 0)
        
    else
        UnitRemoveAbility(GT, FourCC('A16S')) -- ?????? ?????
        DestroyEffect(LoadEffectHandle(Hash, h, 6))
        DestroyTimer(t)
        FlushChildHashtable(Hash, h)
        SetUnitAnimation(GT, "Stand")
        SetUnitFlyHeight(GT, fl, 0)
        --call DestroyEffect(AddSpecialEffect("AbilitiesSpellsOrcWarStompWarStompCaster.mdl", dx, dy))
        g=CreateGroup()
        GroupEnumUnitsInRange(g, dx, dy, 260, nil)
        while true do
            un=FirstOfGroup(g)
            if un == nil then break end
            lvl=GetUnitAbilityLevel(GT, JSTRSkill)
                    
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
function Trig_FlyDragon_Actions()
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
    UnitAddAbility(GT, FourCC('A16S')) -- ?????? ?????
    
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
    SaveReal(Hash, h, 6, GetUnitFlyHeight(GT))
    --call DestroyEffect(AddSpecialEffect("AbilitiesSpellsOtherVolcanoVolcanoDeath.mdl", x, y))
    TimerStart(t, 0.05, true, Trig_Charge_move_heroD) --???????? ???????? ?????
    ---------
    GT=nil
    --set g = null
    t=nil
end
--===========================================================================
function InitTrig_FlyDragon()
    gg_trg_FlyDragon=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_FlyDragon, EVENT_PLAYER_UNIT_SPELL_EFFECT)
    TriggerAddAction(gg_trg_FlyDragon, function()
        if GetSpellAbilityId() ~= FourCC('drA2') then return end
        Trig_FlyDragon_Actions()
    end)
end
--===========================================================================
-- Trigger: DragonUnionStart
--===========================================================================
function Trig_DragonUnionStart_Actions()
    gPlayer=GetOwningPlayer(GetTriggerUnit())
    SetPlayerTechMaxAllowed(gPlayer, FourCC('n044'), 0)
    SetPlayerTechMaxAllowed(gPlayer, FourCC('R0A7'), 0)
    SetPlayerTechMaxAllowed(gPlayer, FourCC('R0AZ'), 0)
end
--===========================================================================
function InitTrig_DragonUnionStart()
    gg_trg_DragonUnionStart=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_DragonUnionStart, EVENT_PLAYER_UNIT_SPELL_EFFECT)
    TriggerAddAction(gg_trg_DragonUnionStart, function()
        if GetSpellAbilityId() ~= FourCC('A1MZ') then return end
        Trig_DragonUnionStart_Actions()
    end)
end
--===========================================================================
-- Trigger: GreenAutoAstral
--===========================================================================
function Trig_GreenAutoAstral_Actions()
    IssueTargetOrder(GetTriggerUnit(), "banish", GetSpellTargetUnit())
end
--===========================================================================
function InitTrig_GreenAutoAstral()
    gg_trg_GreenAutoAstral=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_GreenAutoAstral, EVENT_PLAYER_UNIT_SPELL_EFFECT)
    TriggerAddAction(gg_trg_GreenAutoAstral, function()
        if GetSpellAbilityId() ~= FourCC('drAe') then return end
        Trig_GreenAutoAstral_Actions()
    end)
end
--===========================================================================
-- Trigger: TrainGreenPhase
--===========================================================================
function Trig_TrainGreenPhase_Conditions()
    return GetUnitAbilityLevel(GetTrainedUnit(), FourCC('drAw')) > 0
end
function Trig_TrainGreenPhase_Actions()
    IssueImmediateOrder(GetTrainedUnit(), "phaseshifton")
end
--===========================================================================
function InitTrig_TrainGreenPhase()
    gg_trg_TrainGreenPhase=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_TrainGreenPhase, EVENT_PLAYER_UNIT_CONSTRUCT_FINISH)
    TriggerAddCondition(gg_trg_TrainGreenPhase, Condition(Trig_TrainGreenPhase_Conditions))
    TriggerAddAction(gg_trg_TrainGreenPhase, Trig_TrainGreenPhase_Actions)
end
--===========================================================================
-- Trigger: TrainGreenSpellSteal
--===========================================================================
function Trig_TrainGreenSpellSteal_Conditions()
    return GetUnitAbilityLevel(GetTrainedUnit(), FourCC('A0RM')) > 0
end
function Trig_TrainGreenSpellSteal_Actions()
    IssueImmediateOrder(GetTrainedUnit(), "spellstealon")
end
--===========================================================================
function InitTrig_TrainGreenSpellSteal()
