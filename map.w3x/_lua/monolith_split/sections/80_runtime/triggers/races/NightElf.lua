
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