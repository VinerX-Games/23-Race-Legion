
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
    SetPlayerTechMaxAllowedSwap(FourCC('R0LC'), 0, GetOwningPlayer(GetTriggerUnit()))
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
    SetPlayerTechMaxAllowedSwap(FourCC('R0LC'), 1, GetOwningPlayer(GetTriggerUnit()))
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
    SetPlayerTechMaxAllowedSwap(FourCC('R0LC'), 0, GetOwningPlayer(GetTriggerUnit()))
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
    SetPlayerTechMaxAllowedSwap(FourCC('R0LC'), 1, GetOwningPlayer(GetTriggerUnit()))
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
-- GLOBAL MECHANIC: ПОДЖИГАНИЕ (IGNITE)
--===========================================================================
udg_IgniteData = udg_IgniteData or {}
local IgniteTimer = nil

local function ProcessIgniteTicks()
    local activeCount = 0
    for h, data in pairs(udg_IgniteData) do
        local target = data.target
        if target == nil or not UnitAlive(target) then
            if data.effect then
                DestroyEffect(data.effect)
                data.effect = nil
            end
            udg_IgniteData[h] = nil
        else
            local remainingStacks = {}
            for i = 1, #data.stacks do
                local st = data.stacks[i]
                st.remaining = st.remaining - 0.5
                if st.remaining > 0 then
                    table.insert(remainingStacks, st)
                end
            end
            data.stacks = remainingStacks

            local stackCount = #data.stacks
            if stackCount == 0 then
                if data.effect then
                    DestroyEffect(data.effect)
                    data.effect = nil
                end
                udg_IgniteData[h] = nil
            else
                activeCount = activeCount + 1
                local dmg = stackCount * 1.0
                local src = data.source
                if src == nil or not UnitAlive(src) then
                    src = target
                end
                UnitDamageTarget(src, target, dmg, true, false, ATTACK_TYPE_NORMAL, DAMAGE_TYPE_MAGIC, WEAPON_TYPE_WHOKNOWS)
            end
        end
    end

    if activeCount == 0 and IgniteTimer ~= nil then
        PauseTimer(IgniteTimer)
        DestroyTimer(IgniteTimer)
        IgniteTimer = nil
    end
end

function ApplyIgnite(target, stacks, duration, sourceUnit)
    if target == nil or not UnitAlive(target) then return end
    if IsUnitType(target, UNIT_TYPE_STRUCTURE) or IsUnitType(target, UNIT_TYPE_MECHANICAL) then return end
    if stacks == nil or stacks <= 0 then stacks = 1 end
    if duration == nil or duration <= 0 then duration = 5.0 end

    local h = GetHandleId(target)
    local data = udg_IgniteData[h]
    if not data then
        data = {
            target = target,
            source = sourceUnit,
            stacks = {},
            effect = AddSpecialEffectTarget("Abilities\\Spells\\Other\\BreathOfFire\\BreathOfFireDamage.mdl", target, "chest")
        }
        udg_IgniteData[h] = data
    else
        if sourceUnit ~= nil then
            data.source = sourceUnit
        end
        if data.effect == nil then
            data.effect = AddSpecialEffectTarget("Abilities\\Spells\\Other\\BreathOfFire\\BreathOfFireDamage.mdl", target, "chest")
        end
    end

    for i = 1, stacks do
        if #data.stacks < 3 then
            table.insert(data.stacks, { remaining = duration, source = sourceUnit })
        else
            local minIdx = 1
            local minRem = data.stacks[1].remaining
            for j = 2, #data.stacks do
                if data.stacks[j].remaining < minRem then
                    minRem = data.stacks[j].remaining
                    minIdx = j
                end
            end
            if duration > minRem then
                data.stacks[minIdx].remaining = duration
                data.stacks[minIdx].source = sourceUnit
            end
        end
    end

    if IgniteTimer == nil then
        IgniteTimer = CreateTimer()
        TimerStart(IgniteTimer, 0.5, true, ProcessIgniteTicks)
    end
end
_G.ApplyIgnite = ApplyIgnite

--===========================================================================
-- LUNAR WARRIOR: ТАНЕЦ ПОЛУМЕСЯЦА (CRESCENT DANCE)
--===========================================================================
local IsUnitDashing_Crescent = {}

local function IsPointWalkable(px, py)
    -- In Warcraft 3, IsTerrainPathable returns TRUE when BLOCKED, FALSE when WALKABLE
    return not IsTerrainPathable(px, py, PATHING_TYPE_WALKABILITY)
end

function Trig_CrescentDance_Conditions()
    local attacker = GetAttacker()
    if attacker == nil or not UnitAlive(attacker) then return false end
    if GetUnitAbilityLevel(attacker, FourCC('A0EF')) == 0 then return false end
    if GetPlayerTechCount(GetOwningPlayer(attacker), FourCC('R0LC'), true) == 0 then return false end
    local h = GetHandleId(attacker)
    if IsUnitDashing_Crescent[h] then return false end
    if GetRandomInt(1, 100) > 15 then return false end

    local target = GetTriggerUnit()
    if target == nil or not UnitAlive(target) then return false end
    if not IsUnitEnemy(target, GetOwningPlayer(attacker)) then return false end
    if IsUnitType(target, UNIT_TYPE_STRUCTURE) or IsUnitType(target, UNIT_TYPE_FLYING) then return false end

    return true
end

function Trig_CrescentDance_Actions()
    local attacker = GetAttacker()
    local target = GetTriggerUnit()
    local h = GetHandleId(attacker)

    local ax, ay = GetUnitX(attacker), GetUnitY(attacker)
    local tx, ty = GetUnitX(target), GetUnitY(target)
    local dx = tx - ax
    local dy = ty - ay
    local dist = math.sqrt(dx * dx + dy * dy)
    if dist < 1.0 then dist = 1.0 end
    local ux = dx / dist
    local uy = dy / dist

    -- Landing point B: behind target by 120 units
    local bx = tx + ux * 120.0
    local by = ty + uy * 120.0

    if not IsPointWalkable(bx, by) then
        return -- Landing spot is blocked; execute normal attack
    end

    -- Perpendicular unit vectors: left (-uy, ux), right (uy, -ux)
    local perpLx, perpLy = -uy, ux
    local perpRx, perpRy = uy, -ux

    local arcOffset = 135.0
    local ctrlLx = tx + perpLx * arcOffset
    local ctrlLy = ty + perpLy * arcOffset
    local ctrlRx = tx + perpRx * arcOffset
    local ctrlRy = ty + perpRy * arcOffset

    local left_ok = IsPointWalkable(ctrlLx, ctrlLy) and IsPointWalkable(0.5 * (ax + ctrlLx), 0.5 * (ay + ctrlLy)) and IsPointWalkable(0.5 * (ctrlLx + bx), 0.5 * (ctrlLy + by))
    local right_ok = IsPointWalkable(ctrlRx, ctrlRy) and IsPointWalkable(0.5 * (ax + ctrlRx), 0.5 * (ay + ctrlRy)) and IsPointWalkable(0.5 * (ctrlRx + bx), 0.5 * (ctrlLy + by))

    local ctrlX, ctrlY
    if left_ok and right_ok then
        if GetRandomInt(1, 2) == 1 then
            ctrlX, ctrlY = ctrlLx, ctrlLy
        else
            ctrlX, ctrlY = ctrlRx, ctrlRy
        end
    elseif left_ok then
        ctrlX, ctrlY = ctrlLx, ctrlLy
    elseif right_ok then
        ctrlX, ctrlY = ctrlRx, ctrlRy
    else
        return -- Neither crescent flank is walkable; execute normal attack
    end

    -- Crescent dance starts: interrupt normal attack
    IssueImmediateOrder(attacker, "stop")
    IsUnitDashing_Crescent[h] = true
    SetUnitAnimation(attacker, "attack")
    DestroyEffect(AddSpecialEffect("Abilities\\Spells\\NightElf\\Blink\\BlinkCaster.mdl", ax, ay))

    local baseDmg = BlzGetUnitBaseDamage(attacker, 0)
    if baseDmg <= 0 then baseDmg = 25 end
    local slashDmg = baseDmg * 0.5

    local step = 0
    local hitTable = {}
    local grp = CreateGroup()
    local dashTimer = CreateTimer()

    TimerStart(dashTimer, 0.03125, true, function()
        step = step + 1
        local t = step / 8.0
        local t0 = 1.0 - t

        if not UnitAlive(attacker) then
            IsUnitDashing_Crescent[h] = nil
            DestroyGroup(grp)
            PauseTimer(dashTimer)
            DestroyTimer(dashTimer)
            return
        end

        local curX = t0 * t0 * ax + 2.0 * t0 * t * ctrlX + t * t * bx
        local curY = t0 * t0 * ay + 2.0 * t0 * t * ctrlY + t * t * by

        SetUnitX(attacker, curX)
        SetUnitY(attacker, curY)

        if step % 2 == 0 then
            DestroyEffect(AddSpecialEffect("Abilities\\Spells\\NightElf\\Blink\\BlinkCaster.mdl", curX, curY))
        end

        GroupEnumUnitsInRange(grp, curX, curY, 130.0, nil)
        while true do
            local enemy = FirstOfGroup(grp)
            if enemy == nil then break end
            GroupRemoveUnit(grp, enemy)
            local eh = GetHandleId(enemy)
            if not hitTable[eh] and UnitAlive(enemy) and IsUnitEnemy(enemy, GetOwningPlayer(attacker)) and not IsUnitType(enemy, UNIT_TYPE_STRUCTURE) and not IsUnitType(enemy, UNIT_TYPE_FLYING) then
                hitTable[eh] = true
                UnitDamageTarget(attacker, enemy, slashDmg, true, false, ATTACK_TYPE_NORMAL, DAMAGE_TYPE_NORMAL, WEAPON_TYPE_WHOKNOWS)
                DestroyEffect(AddSpecialEffectTarget("Abilities\\Spells\\NightElf\\FanOfKnives\\FanOfKnivesTarget.mdl", enemy, "chest"))
            end
        end

        if step >= 8 then
            IsUnitDashing_Crescent[h] = nil
            DestroyGroup(grp)
            PauseTimer(dashTimer)
            DestroyTimer(dashTimer)

            if UnitAlive(target) then
                local finalTx, finalTy = GetUnitX(target), GetUnitY(target)
                local faceAngle = bj_RADTODEG * Atan2(finalTy - curY, finalTx - curX)
                SetUnitFacing(attacker, faceAngle)
                IssueTargetOrder(attacker, "attack", target)
            end
        end
    end)
end

function InitTrig_CrescentDance()
    gg_trg_CrescentDance = CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_CrescentDance, EVENT_PLAYER_UNIT_ATTACKED)
    TriggerAddCondition(gg_trg_CrescentDance, Condition(Trig_CrescentDance_Conditions))
    TriggerAddAction(gg_trg_CrescentDance, Trig_CrescentDance_Actions)

    BlzSetAbilityTooltip(FourCC('A0EF'), "Танец полумесяца", 0)
    BlzSetAbilityExtendedTooltip(FourCC('A0EF'), "С вероятностью 15% при атаке воин совершает стремительный перекат полумесяцем за спину противника, нанося всем врагам на пути 50% от своего базового урона.", 0)
    BlzSetAbilityIcon(FourCC('A0EF'), "ReplaceableTextures\\CommandButtons\\BTNAmbush.blp")
    BlzSetAbilityPosX(FourCC('A0EF'), 1)
    BlzSetAbilityPosY(FourCC('A0EF'), 2)
end

--===========================================================================
-- DRUID-OWL: АСТРАЛЬНЫЕ ФАЗЫ (СОЛНЦЕ И ЛУНА)
--===========================================================================
Owl_Phase = Owl_Phase or {}
Owl_HeadFX = Owl_HeadFX or {}

function UpdateOwlAstralVisuals(u)
    if u == nil or not UnitAlive(u) then return end
    local h = GetHandleId(u)
    local phase = Owl_Phase[h] or "solar"

    if Owl_HeadFX[h] then
        DestroyEffect(Owl_HeadFX[h])
        Owl_HeadFX[h] = nil
    end

    if phase == "solar" then
        SetUnitVertexColor(u, 255, 210, 180, 255)
        Owl_HeadFX[h] = AddSpecialEffectTarget("Abilities\\Weapons\\FireBall\\FireBallMissile.mdl", u, "overhead")
    else
        SetUnitVertexColor(u, 180, 210, 255, 255)
        Owl_HeadFX[h] = AddSpecialEffectTarget("Abilities\\Weapons\\AvengerMissile\\AvengerMissile.mdl", u, "overhead")
    end
end

function InitOwlUnit(u)
    if u == nil then return end
    local h = GetHandleId(u)
    if Owl_Phase[h] == nil then
        Owl_Phase[h] = "solar"
        UnitAddAbility(u, FourCC('ACfb'))
        UnitRemoveAbility(u, FourCC('Anhe'))
        UpdateOwlAstralVisuals(u)
    end
end

function Trig_DruidOwl_SpellEffect_Actions()
    local spellId = GetSpellAbilityId()
    local caster = GetTriggerUnit()
    local uid = GetUnitTypeId(caster)
    local isOwl = (uid == FourCC('n05D') or uid == FourCC('n05G'))

    if spellId == FourCC('Absk') and isOwl then
        UnitRemoveAbility(caster, FourCC('Bbsk'))
        BlzStartUnitAbilityCooldown(caster, FourCC('Absk'), 2.50)

        local h = GetHandleId(caster)
        if Owl_Phase[h] == "lunar" then
            Owl_Phase[h] = "solar"
            UnitRemoveAbility(caster, FourCC('Anhe'))
            UnitAddAbility(caster, FourCC('ACfb'))
        else
            Owl_Phase[h] = "lunar"
            UnitRemoveAbility(caster, FourCC('ACfb'))
            UnitAddAbility(caster, FourCC('Anhe'))
        end
        UpdateOwlAstralVisuals(caster)

    elseif spellId == FourCC('ACfb') and isOwl then
        local target = GetSpellTargetUnit()
        if target and UnitAlive(target) then
            ApplyIgnite(target, 1, 6.0, caster)
        end
        BlzStartUnitAbilityCooldown(caster, FourCC('ACfb'), 9.00)
        SetUnitState(caster, UNIT_STATE_MANA, GetUnitState(caster, UNIT_STATE_MANA) + 10.0)

    elseif spellId == FourCC('Anhe') and isOwl then
        local target = GetSpellTargetUnit()
        if target and UnitAlive(target) then
            SetWidgetLife(target, GetWidgetLife(target) + 35.0)
            DestroyEffect(AddSpecialEffectTarget("Abilities\\Spells\\NightElf\\Starfall\\StarfallTarget.mdl", target, "origin"))
        end
        BlzStartUnitAbilityCooldown(caster, FourCC('Anhe'), 9.00)
        SetUnitState(caster, UNIT_STATE_MANA, GetUnitState(caster, UNIT_STATE_MANA) - 60.0)

    elseif spellId == FourCC('A164') and isOwl then
        -- Transformation between n05D and n05G
        local morphTimer = CreateTimer()
        TimerStart(morphTimer, 0.15, false, function()
            local t = GetExpiredTimer()
            if UnitAlive(caster) then
                local h = GetHandleId(caster)
                if Owl_Phase[h] == "lunar" then
                    UnitRemoveAbility(caster, FourCC('ACfb'))
                    UnitAddAbility(caster, FourCC('Anhe'))
                else
                    UnitRemoveAbility(caster, FourCC('Anhe'))
                    UnitAddAbility(caster, FourCC('ACfb'))
                end
                UpdateOwlAstralVisuals(caster)
            end
            DestroyTimer(t)
        end)
    end
end

function Trig_DruidOwl_Damage_Actions()
    if not BlzGetEventIsAttack() then return end
    local src = GetEventDamageSource()
    if src == nil or not UnitAlive(src) then return end
    local uid = GetUnitTypeId(src)
    if uid ~= FourCC('n05D') and uid ~= FourCC('n05G') then return end

    local target = GetTriggerUnit()
    if target == nil or not UnitAlive(target) then return end

    local sh = GetHandleId(src)
    if Owl_Phase[sh] == nil then
        InitOwlUnit(src)
    end

    if Owl_Phase[sh] == "solar" then
        ApplyIgnite(target, 1, 5.0, src)
    elseif Owl_Phase[sh] == "lunar" then
        local sx, sy = GetUnitX(src), GetUnitY(src)
        local srcPlayer = GetOwningPlayer(src)
        local grp = CreateGroup()
        GroupEnumUnitsInRange(grp, sx, sy, 500.0, nil)

        local lowestAlly = nil
        local lowestMana = 9999999.0

        while true do
            local ally = FirstOfGroup(grp)
            if ally == nil then break end
            GroupRemoveUnit(grp, ally)

            if UnitAlive(ally) and IsUnitAlly(ally, srcPlayer) and not IsUnitType(ally, UNIT_TYPE_STRUCTURE) and not IsUnitType(ally, UNIT_TYPE_MECHANICAL) and not IsUnitType(ally, UNIT_TYPE_DEAD) then
                local maxMana = BlzGetUnitMaxMana(ally)
                if maxMana > 0 then
                    local curMana = GetUnitState(ally, UNIT_STATE_MANA)
                    if curMana < maxMana and curMana < lowestMana then
                        lowestMana = curMana
                        lowestAlly = ally
                    end
                end
            end
        end
        DestroyGroup(grp)

        if lowestAlly ~= nil then
            local newMana = GetUnitState(lowestAlly, UNIT_STATE_MANA) + 10.0
            SetUnitState(lowestAlly, UNIT_STATE_MANA, newMana)
            DestroyEffect(AddSpecialEffectTarget("Abilities\\Spells\\Items\\AIma\\AImaTarget.mdl", lowestAlly, "origin"))
        end
    end
end

function Trig_DruidOwl_Death_Actions()
    local u = GetTriggerUnit()
    local uid = GetUnitTypeId(u)
    if uid == FourCC('n05D') or uid == FourCC('n05G') then
        local h = GetHandleId(u)
        if Owl_HeadFX[h] then
            DestroyEffect(Owl_HeadFX[h])
            Owl_HeadFX[h] = nil
        end
    end
end

function Trig_DruidOwl_Train_Actions()
    local u = GetTrainedUnit()
    if GetUnitTypeId(u) == FourCC('n05D') then
        InitOwlUnit(u)
    end
end

function InitTrig_DruidOwlAstralPhases()
    gg_trg_DruidOwl_Spell = CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_DruidOwl_Spell, EVENT_PLAYER_UNIT_SPELL_EFFECT)
    TriggerAddAction(gg_trg_DruidOwl_Spell, Trig_DruidOwl_SpellEffect_Actions)

    gg_trg_DruidOwl_Damage = CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_DruidOwl_Damage, EVENT_PLAYER_UNIT_DAMAGED)
    TriggerAddAction(gg_trg_DruidOwl_Damage, Trig_DruidOwl_Damage_Actions)

    gg_trg_DruidOwl_Death = CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_DruidOwl_Death, EVENT_PLAYER_UNIT_DEATH)
    TriggerAddAction(gg_trg_DruidOwl_Death, Trig_DruidOwl_Death_Actions)

    gg_trg_DruidOwl_Train = CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_DruidOwl_Train, EVENT_PLAYER_UNIT_TRAIN_FINISH)
    TriggerAddAction(gg_trg_DruidOwl_Train, Trig_DruidOwl_Train_Actions)

    -- Stance button
    BlzSetAbilityTooltip(FourCC('Absk'), "Астральная фаза", 0)
    BlzSetAbilityExtendedTooltip(FourCC('Absk'), "Переключает астральную фазу друида между Солнцем и Луной.|n|n|cffffaa00Фаза Солнца:|r|n• Атаки поджигают врага (до 3 стаков, 1 ед. урона раз в 0.5 сек).|n• Заклинание: «Солнечный ожог» (40 урона + поджигание на 6 сек, 65 маны, 9 сек КД).|n|n|cff99bbffФаза Луны:|r|n• Атаки восполняют 10 маны союзнику с наименьшей маной в радиусе 500.|n• Заклинание: «Звездный луч» (исцеляет 50 ед. здоровья, 65 маны, 9 сек КД).|n|nПерезарядка: 2.5 сек.", 0)
    BlzSetAbilityIcon(FourCC('Absk'), "ReplaceableTextures\\CommandButtons\\BTNMoonStone.blp")
    BlzSetAbilityPosX(FourCC('Absk'), 0)
    BlzSetAbilityPosY(FourCC('Absk'), 2)

    -- Solar Burn
    BlzSetAbilityTooltip(FourCC('ACfb'), "Солнечный ожог", 0)
    BlzSetAbilityExtendedTooltip(FourCC('ACfb'), "Поражает врага сгустком солнечного пламени, нанося 40 единиц магического урона и накладывая 1 эффект поджигания на 6 сек.|n|nЗатраты маны: 65.|nВремя восстановления: 9 сек.", 0)
    BlzSetAbilityIcon(FourCC('ACfb'), "ReplaceableTextures\\CommandButtons\\BTNSearingArrows.blp")
    BlzSetAbilityPosX(FourCC('ACfb'), 1)
    BlzSetAbilityPosY(FourCC('ACfb'), 2)

    -- Star Ray
    BlzSetAbilityTooltip(FourCC('Anhe'), "Звездный луч", 0)
    BlzSetAbilityExtendedTooltip(FourCC('Anhe'), "Направляет чистый свет звезд на раненого союзника, восполняя 50 единиц здоровья.|n|nЗатраты маны: 65.|nВремя восстановления: 9 сек.", 0)
    BlzSetAbilityIcon(FourCC('Anhe'), "ReplaceableTextures\\CommandButtons\\BTNStarfall.blp")
    BlzSetAbilityActivatedTooltip(FourCC('Anhe'), "Звездный луч", 0)
    BlzSetAbilityActivatedExtendedTooltip(FourCC('Anhe'), "Направляет чистый свет звезд на раненого союзника, восполняя 50 единиц здоровья.|n|nЗатраты маны: 65.|nВремя восстановления: 9 сек.", 0)
    BlzSetAbilityActivatedIcon(FourCC('Anhe'), "ReplaceableTextures\\CommandButtons\\BTNStarfall.blp")
    BlzSetAbilityPosX(FourCC('Anhe'), 1)
    BlzSetAbilityPosY(FourCC('Anhe'), 2)
    BlzSetAbilityActivatedPosX(FourCC('Anhe'), 1)
    BlzSetAbilityActivatedPosY(FourCC('Anhe'), 2)
end

