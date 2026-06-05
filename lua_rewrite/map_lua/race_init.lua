--===========================================================================
-- Race Selection Triggers - converted from vJASS to Lua
-- All globals accessed via G.*
-- FourCC rawcodes use FourCC()
--===========================================================================

--===========================================================================
-- 1. Race Bezlikie O
--===========================================================================
function Trig_Race_Bezlikie_O_Conditions()
    return GetSpellAbilityId() == FourCC('A0HW')
end

function Trig_Race_Bezlikie_O_Actions()
    G.udg_LocalPosition2 = GetUnitLoc(GetTriggerUnit())
    CreateNUnitsAtLoc(3, FourCC('u02D'), GetOwningPlayer(GetSpellAbilityUnit()), G.udg_LocalPosition2, bj_UNIT_FACING)
    RemoveUnit(GetSpellAbilityUnit())
    SetPlayerTechResearchedSwap(FourCC('R0F9'), 1, GetOwningPlayer(GetTriggerUnit()))
    RemoveLocation(G.udg_LocalPosition2)
end

function InitTrig_Race_Bezlikie_O()
    G.gg_trg_Race_Bezlikie_O = CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(G.gg_trg_Race_Bezlikie_O, EVENT_PLAYER_UNIT_SPELL_FINISH)
    TriggerAddCondition(G.gg_trg_Race_Bezlikie_O, Condition(Trig_Race_Bezlikie_O_Conditions))
    TriggerAddAction(G.gg_trg_Race_Bezlikie_O, Trig_Race_Bezlikie_O_Actions)
end

--===========================================================================
-- 2. Race IceTrols
--===========================================================================
function Trig_Race_IceTrols_Conditions()
    return GetSpellAbilityId() == FourCC('A1EG')
end

function Trig_Race_IceTrols_Actions()
    G.udg_LocalPosition2 = GetUnitLoc(GetTriggerUnit())
    CreateNUnitsAtLoc(5, FourCC('o045'), GetOwningPlayer(GetSpellAbilityUnit()), G.udg_LocalPosition2, bj_UNIT_FACING)
    RemoveUnit(GetSpellAbilityUnit())
    SetPlayerTechResearchedSwap(FourCC('R0L1'), 1, GetOwningPlayer(GetTriggerUnit()))
    RemoveLocation(G.udg_LocalPosition2)
end

function InitTrig_Race_IceTrols()
    G.gg_trg_Race_IceTrols = CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(G.gg_trg_Race_IceTrols, EVENT_PLAYER_UNIT_SPELL_FINISH)
    TriggerAddCondition(G.gg_trg_Race_IceTrols, Condition(Trig_Race_IceTrols_Conditions))
    TriggerAddAction(G.gg_trg_Race_IceTrols, Trig_Race_IceTrols_Actions)
end

--===========================================================================
-- 3. Race Stromgard O
--===========================================================================
function Trig_Race_Stromgard_O_Conditions()
    return GetSpellAbilityId() == FourCC('A0Y0')
end

function Trig_Race_Stromgard_O_Actions()
    G.udg_LocalPosition2 = GetUnitLoc(GetTriggerUnit())
    CreateNUnitsAtLoc(5, FourCC('h0G9'), GetOwningPlayer(GetSpellAbilityUnit()), G.udg_LocalPosition2, bj_UNIT_FACING)
    RemoveUnit(GetSpellAbilityUnit())
    SetPlayerTechResearchedSwap(FourCC('R0H3'), 1, GetOwningPlayer(GetTriggerUnit()))
    SetPlayerTechResearchedSwap(FourCC('R0HY'), 1, GetOwningPlayer(GetTriggerUnit()))
    TriggerExecute(G.gg_trg_StromgardOn)
    RemoveLocation(G.udg_LocalPosition2)
end

function InitTrig_Race_Stromgard_O()
    G.gg_trg_Race_Stromgard_O = CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(G.gg_trg_Race_Stromgard_O, EVENT_PLAYER_UNIT_SPELL_FINISH)
    TriggerAddCondition(G.gg_trg_Race_Stromgard_O, Condition(Trig_Race_Stromgard_O_Conditions))
    TriggerAddAction(G.gg_trg_Race_Stromgard_O, Trig_Race_Stromgard_O_Actions)
end

--===========================================================================
-- 4. Race Dragon O
--===========================================================================
function Trig_Race_Dragon_O_Conditions()
    return GetSpellAbilityId() == FourCC('A0RQ')
end

function Trig_Race_Dragon_O_Actions()
    G.udg_LocalPosition2 = GetUnitLoc(GetTriggerUnit())
    CreateNUnitsAtLoc(1, FourCC('dra1'), GetOwningPlayer(GetSpellAbilityUnit()), G.udg_LocalPosition2, bj_UNIT_FACING)
    SetPlayerTechResearchedSwap(FourCC('R0BY'), 1, GetOwningPlayer(GetTriggerUnit()))
    RemoveUnit(GetSpellAbilityUnit())
    RemoveLocation(G.udg_LocalPosition2)
    DragonsOn()
end

function InitTrig_Race_Dragon_O()
    G.gg_trg_Race_Dragon_O = CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(G.gg_trg_Race_Dragon_O, EVENT_PLAYER_UNIT_SPELL_FINISH)
    TriggerAddCondition(G.gg_trg_Race_Dragon_O, Condition(Trig_Race_Dragon_O_Conditions))
    TriggerAddAction(G.gg_trg_Race_Dragon_O, Trig_Race_Dragon_O_Actions)
end

--===========================================================================
-- 5. Race Dragon2
--===========================================================================
function Trig_Race_Dragon2_Conditions()
    return GetSpellAbilityId() == FourCC('A1MZ')
end

function Trig_Race_Dragon2_Actions()
    G.udg_LocalPosition2 = GetUnitLoc(GetTriggerUnit())
    CreateNUnitsAtLoc(5, FourCC('o01D'), GetOwningPlayer(GetSpellAbilityUnit()), G.udg_LocalPosition2, bj_UNIT_FACING)
    RemoveUnit(GetSpellAbilityUnit())
    RemoveLocation(G.udg_LocalPosition2)
end

function InitTrig_Race_Dragon2()
    G.gg_trg_Race_Dragon2 = CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(G.gg_trg_Race_Dragon2, EVENT_PLAYER_UNIT_SPELL_FINISH)
    TriggerAddCondition(G.gg_trg_Race_Dragon2, Condition(Trig_Race_Dragon2_Conditions))
    TriggerAddAction(G.gg_trg_Race_Dragon2, Trig_Race_Dragon2_Actions)
end

--===========================================================================
-- 6. Race Argvinol O
--===========================================================================
function Trig_Race_Argvinol_O_Conditions()
    return GetSpellAbilityId() == FourCC('A0QQ')
end

function Trig_Race_Argvinol_O_Actions()
    G.udg_LocalPosition2 = GetUnitLoc(GetTriggerUnit())
    CreateNUnitsAtLoc(5, FourCC('e02T'), GetOwningPlayer(GetSpellAbilityUnit()), G.udg_LocalPosition2, bj_UNIT_FACING)
    RemoveUnit(GetSpellAbilityUnit())
    SetPlayerTechResearchedSwap(FourCC('R0BZ'), 1, GetOwningPlayer(GetTriggerUnit()))
    RemoveLocation(G.udg_LocalPosition2)
end

function InitTrig_Race_Argvinol_O()
    G.gg_trg_Race_Argvinol_O = CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(G.gg_trg_Race_Argvinol_O, EVENT_PLAYER_UNIT_SPELL_FINISH)
    TriggerAddCondition(G.gg_trg_Race_Argvinol_O, Condition(Trig_Race_Argvinol_O_Conditions))
    TriggerAddAction(G.gg_trg_Race_Argvinol_O, Trig_Race_Argvinol_O_Actions)
end

--===========================================================================
-- 7. Race Elements O
--===========================================================================
function Trig_Race_Elements_O_Conditions()
    return GetSpellAbilityId() == FourCC('A0QN')
end

function Trig_Race_Elements_O_Actions()
    G.udg_LocalPosition2 = GetUnitLoc(GetTriggerUnit())
    CreateNUnitsAtLoc(5, FourCC('e00F'), GetOwningPlayer(GetSpellAbilityUnit()), G.udg_LocalPosition2, bj_UNIT_FACING)
    RemoveUnit(GetSpellAbilityUnit())
    SetPlayerTechResearchedSwap(FourCC('R0A2'), 1, GetOwningPlayer(GetTriggerUnit()))
    ElemOn()
    RemoveLocation(G.udg_LocalPosition2)
end

function InitTrig_Race_Elements_O()
    G.gg_trg_Race_Elements_O = CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(G.gg_trg_Race_Elements_O, EVENT_PLAYER_UNIT_SPELL_FINISH)
    TriggerAddCondition(G.gg_trg_Race_Elements_O, Condition(Trig_Race_Elements_O_Conditions))
    TriggerAddAction(G.gg_trg_Race_Elements_O, Trig_Race_Elements_O_Actions)
end

--===========================================================================
-- 8. Race Goblins O
--===========================================================================
function Trig_Race_Goblins_O_Conditions()
    return GetSpellAbilityId() == FourCC('A0AC')
end

function Trig_Race_Goblins_O_Actions()
    G.udg_LocalPosition2 = GetUnitLoc(GetTriggerUnit())
    CreateNUnitsAtLoc(5, FourCC('n00V'), GetOwningPlayer(GetSpellAbilityUnit()), G.udg_LocalPosition2, bj_UNIT_FACING)
    SetPlayerTechResearchedSwap(FourCC('R07E'), 1, GetOwningPlayer(GetTriggerUnit()))
    SetPlayerTechResearchedSwap(FourCC('R0J3'), 1, GetOwningPlayer(GetTriggerUnit()))
    RemoveUnit(GetSpellAbilityUnit())
    TriggerExecute(G.gg_trg_GoblinsOn)
    RemoveLocation(G.udg_LocalPosition2)
end

function InitTrig_Race_Goblins_O()
    G.gg_trg_Race_Goblins_O = CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(G.gg_trg_Race_Goblins_O, EVENT_PLAYER_UNIT_SPELL_FINISH)
    TriggerAddCondition(G.gg_trg_Race_Goblins_O, Condition(Trig_Race_Goblins_O_Conditions))
    TriggerAddAction(G.gg_trg_Race_Goblins_O, Trig_Race_Goblins_O_Actions)
end

--===========================================================================
-- 9. Race Demon O
--===========================================================================
function Trig_Race_Demon_O_Conditions()
    return GetSpellAbilityId() == FourCC('A0MY')
end

function Trig_Race_Demon_O_Actions()
    G.udg_LocalPosition2 = GetUnitLoc(GetTriggerUnit())
    CreateNUnitsAtLoc(8, FourCC('e02Y'), GetOwningPlayer(GetSpellAbilityUnit()), G.udg_LocalPosition2, bj_UNIT_FACING)
    SetPlayerTechResearchedSwap(FourCC('R0AO'), 1, GetOwningPlayer(GetTriggerUnit()))
    RemoveUnit(GetSpellAbilityUnit())
    RemoveLocation(G.udg_LocalPosition2)
end

function InitTrig_Race_Demon_O()
    G.gg_trg_Race_Demon_O = CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(G.gg_trg_Race_Demon_O, EVENT_PLAYER_UNIT_SPELL_FINISH)
    TriggerAddCondition(G.gg_trg_Race_Demon_O, Condition(Trig_Race_Demon_O_Conditions))
    TriggerAddAction(G.gg_trg_Race_Demon_O, Trig_Race_Demon_O_Actions)
end

--===========================================================================
-- 10. Race Illidari O
--===========================================================================
function Trig_Race_Illidari_O_Conditions()
    return GetSpellAbilityId() == FourCC('A0OK')
end

function Trig_Race_Illidari_O_Actions()
    G.udg_LocalPosition2 = GetUnitLoc(GetTriggerUnit())
    CreateNUnitsAtLoc(5, FourCC('h0EI'), GetOwningPlayer(GetSpellAbilityUnit()), G.udg_LocalPosition2, bj_UNIT_FACING)
    SetPlayerTechResearchedSwap(FourCC('R07H'), 1, GetOwningPlayer(GetTriggerUnit()))
    SetPlayerTechResearchedSwap(FourCC('R0KZ'), 1, GetOwningPlayer(GetTriggerUnit()))
    SetPlayerTechResearchedSwap(FourCC('R0L0'), 1, GetOwningPlayer(GetTriggerUnit()))
    ConditionalTriggerExecute(G.gg_trg_IllidaryOn)
    RemoveUnit(GetSpellAbilityUnit())
    RemoveLocation(G.udg_LocalPosition2)
end

function InitTrig_Race_Illidari_O()
    G.gg_trg_Race_Illidari_O = CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(G.gg_trg_Race_Illidari_O, EVENT_PLAYER_UNIT_SPELL_FINISH)
    TriggerAddCondition(G.gg_trg_Race_Illidari_O, Condition(Trig_Race_Illidari_O_Conditions))
    TriggerAddAction(G.gg_trg_Race_Illidari_O, Trig_Race_Illidari_O_Actions)
end

--===========================================================================
-- 11. Race Bandits O
--===========================================================================
function Trig_Race_Bandits_O_Conditions()
    return GetSpellAbilityId() == FourCC('A0HR')
end

function Trig_Race_Bandits_O_Actions()
    G.udg_LocalPosition2 = GetUnitLoc(GetTriggerUnit())
    CreateNUnitsAtLoc(5, FourCC('h002'), GetOwningPlayer(GetSpellAbilityUnit()), G.udg_LocalPosition2, bj_UNIT_FACING)
    SetPlayerTechResearchedSwap(FourCC('R00G'), 1, GetOwningPlayer(GetTriggerUnit()))
    TriggerExecute(G.gg_trg_BanditsOn)
    RemoveUnit(GetSpellAbilityUnit())
    RemoveLocation(G.udg_LocalPosition2)
end

function InitTrig_Race_Bandits_O()
    G.gg_trg_Race_Bandits_O = CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(G.gg_trg_Race_Bandits_O, EVENT_PLAYER_UNIT_SPELL_FINISH)
    TriggerAddCondition(G.gg_trg_Race_Bandits_O, Condition(Trig_Race_Bandits_O_Conditions))
    TriggerAddAction(G.gg_trg_Race_Bandits_O, Trig_Race_Bandits_O_Actions)
end

--===========================================================================
-- 12. Race Red Orden O
--===========================================================================
function Trig_Race_Red_Orden_O_Conditions()
    return GetSpellAbilityId() == FourCC('A0HM')
end

function Trig_Race_Red_Orden_O_Actions()
    G.udg_LocalPosition2 = GetUnitLoc(GetTriggerUnit())
    CreateNUnitsAtLoc(5, FourCC('h014'), GetOwningPlayer(GetSpellAbilityUnit()), G.udg_LocalPosition2, bj_UNIT_FACING)
    SetPlayerTechResearchedSwap(FourCC('R07B'), 1, GetOwningPlayer(GetTriggerUnit()))
    RemoveUnit(GetSpellAbilityUnit())
    RemoveLocation(G.udg_LocalPosition2)
end

function InitTrig_Race_Red_Orden_O()
    G.gg_trg_Race_Red_Orden_O = CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(G.gg_trg_Race_Red_Orden_O, EVENT_PLAYER_UNIT_SPELL_FINISH)
    TriggerAddCondition(G.gg_trg_Race_Red_Orden_O, Condition(Trig_Race_Red_Orden_O_Conditions))
    TriggerAddAction(G.gg_trg_Race_Red_Orden_O, Trig_Race_Red_Orden_O_Actions)
end

--===========================================================================
-- 13. Race Undead O
--===========================================================================
function Trig_Race_Undead_O_Conditions()
    return GetSpellAbilityId() == FourCC('A0HV')
end

function Trig_Race_Undead_O_Actions()
    G.udg_LocalPosition2 = GetUnitLoc(GetTriggerUnit())
    CreateNUnitsAtLoc(3, FourCC('u00P'), GetOwningPlayer(GetSpellAbilityUnit()), G.udg_LocalPosition2, bj_UNIT_FACING)
    SetPlayerTechResearchedSwap(FourCC('R07I'), 1, GetOwningPlayer(GetTriggerUnit()))
    SetPlayerTechResearchedSwap(FourCC('R0J5'), 1, GetOwningPlayer(GetTriggerUnit()))
    RemoveUnit(GetSpellAbilityUnit())
    ConditionalTriggerExecute(G.gg_trg_UndeadOn)
    RemoveLocation(G.udg_LocalPosition2)
end

function InitTrig_Race_Undead_O()
    G.gg_trg_Race_Undead_O = CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(G.gg_trg_Race_Undead_O, EVENT_PLAYER_UNIT_SPELL_FINISH)
    TriggerAddCondition(G.gg_trg_Race_Undead_O, Condition(Trig_Race_Undead_O_Conditions))
    TriggerAddAction(G.gg_trg_Race_Undead_O, Trig_Race_Undead_O_Actions)
end

--===========================================================================
-- 14. Race Horde
--===========================================================================
function Trig_Race_Horde_Conditions()
    return GetSpellAbilityId() == FourCC('A0YV')
end

function Trig_Race_Horde_Actions()
    G.udg_LocalPosition2 = GetUnitLoc(GetTriggerUnit())
    CreateNUnitsAtLoc(5, FourCC('opeo'), GetOwningPlayer(GetSpellAbilityUnit()), G.udg_LocalPosition2, bj_UNIT_FACING)
    SetPlayerTechResearchedSwap(FourCC('R0DV'), 1, GetOwningPlayer(GetTriggerUnit()))
    SetPlayerTechResearchedSwap(FourCC('R0IR'), 1, GetOwningPlayer(GetTriggerUnit()))
    SetPlayerTechResearchedSwap(FourCC('R0J3'), 1, GetOwningPlayer(GetTriggerUnit()))
    ConditionalTriggerExecute(G.gg_trg_HordeOn)
    ConditionalTriggerExecute(G.gg_trg_StartHorde)
    RemoveUnit(GetSpellAbilityUnit())
    RemoveLocation(G.udg_LocalPosition2)
end

function InitTrig_Race_Horde()
    G.gg_trg_Race_Horde = CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(G.gg_trg_Race_Horde, EVENT_PLAYER_UNIT_SPELL_FINISH)
    TriggerAddCondition(G.gg_trg_Race_Horde, Condition(Trig_Race_Horde_Conditions))
    TriggerAddAction(G.gg_trg_Race_Horde, Trig_Race_Horde_Actions)
end

--===========================================================================
-- 15. Race Blood Elves O
--===========================================================================
function Trig_Race_Blood_Elves_O_Conditions()
    return GetSpellAbilityId() == FourCC('A0HQ')
end

function Trig_Race_Blood_Elves_O_Actions()
    G.udg_LocalPosition2 = GetUnitLoc(GetTriggerUnit())
    CreateNUnitsAtLoc(5, FourCC('h04K'), GetOwningPlayer(GetSpellAbilityUnit()), G.udg_LocalPosition2, bj_UNIT_FACING)
    SetPlayerTechResearchedSwap(FourCC('R07C'), 1, GetOwningPlayer(GetTriggerUnit()))
    SetPlayerTechResearchedSwap(FourCC('R0L0'), 1, GetOwningPlayer(GetTriggerUnit()))
    ConditionalTriggerExecute(G.gg_trg_BloodElvesOn)
    RemoveUnit(GetSpellAbilityUnit())
    RemoveLocation(G.udg_LocalPosition2)
end

function InitTrig_Race_Blood_Elves_O()
    G.gg_trg_Race_Blood_Elves_O = CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(G.gg_trg_Race_Blood_Elves_O, EVENT_PLAYER_UNIT_SPELL_FINISH)
    TriggerAddCondition(G.gg_trg_Race_Blood_Elves_O, Condition(Trig_Race_Blood_Elves_O_Conditions))
    TriggerAddAction(G.gg_trg_Race_Blood_Elves_O, Trig_Race_Blood_Elves_O_Actions)
end

--===========================================================================
-- 16. Race Dalaran O
--===========================================================================
function Trig_Race_Dalaran_O_Conditions()
    return GetSpellAbilityId() == FourCC('A0HN')
end

function Trig_Race_Dalaran_O_Actions()
    G.udg_LocalPosition2 = GetUnitLoc(GetTriggerUnit())
    CreateNUnitsAtLoc(3, FourCC('u001'), GetOwningPlayer(GetSpellAbilityUnit()), G.udg_LocalPosition2, bj_UNIT_FACING)
    SetPlayerTechResearchedSwap(FourCC('R0BW'), 1, GetOwningPlayer(GetTriggerUnit()))
    SetPlayerTechResearchedSwap(FourCC('R0KK'), 1, GetOwningPlayer(GetTriggerUnit()))
    RemoveUnit(GetSpellAbilityUnit())
    RemoveLocation(G.udg_LocalPosition2)
end

function InitTrig_Race_Dalaran_O()
    G.gg_trg_Race_Dalaran_O = CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(G.gg_trg_Race_Dalaran_O, EVENT_PLAYER_UNIT_SPELL_FINISH)
    TriggerAddCondition(G.gg_trg_Race_Dalaran_O, Condition(Trig_Race_Dalaran_O_Conditions))
    TriggerAddAction(G.gg_trg_Race_Dalaran_O, Trig_Race_Dalaran_O_Actions)
end

--===========================================================================
-- 17. Race KulTiras O
--===========================================================================
function Trig_Race_KulTiras_O_Conditions()
    return GetSpellAbilityId() == FourCC('A0HO')
end

function Trig_Race_KulTiras_O_Actions()
    G.udg_LocalPosition2 = GetUnitLoc(GetTriggerUnit())
    CreateNUnitsAtLoc(5, FourCC('h013'), GetOwningPlayer(GetSpellAbilityUnit()), G.udg_LocalPosition2, bj_UNIT_FACING)
    SetPlayerTechResearchedSwap(FourCC('R07D'), 1, GetOwningPlayer(GetTriggerUnit()))
    SetPlayerTechResearchedSwap(FourCC('R0HX'), 1, GetOwningPlayer(GetTriggerUnit()))
    RemoveUnit(GetSpellAbilityUnit())
    RemoveLocation(G.udg_LocalPosition2)
end

function InitTrig_Race_KulTiras_O()
    G.gg_trg_Race_KulTiras_O = CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(G.gg_trg_Race_KulTiras_O, EVENT_PLAYER_UNIT_SPELL_FINISH)
    TriggerAddCondition(G.gg_trg_Race_KulTiras_O, Condition(Trig_Race_KulTiras_O_Conditions))
    TriggerAddAction(G.gg_trg_Race_KulTiras_O, Trig_Race_KulTiras_O_Actions)
end

--===========================================================================
-- 18. Race Nocnorogdennue O
--===========================================================================
function Trig_Race_Nocnorogdennue_O_Conditions()
    return GetSpellAbilityId() == FourCC('A0HU')
end

function Trig_Race_Nocnorogdennue_O_Actions()
    G.udg_LocalPosition2 = GetUnitLoc(GetTriggerUnit())
    CreateNUnitsAtLoc(5, FourCC('h0CJ'), GetOwningPlayer(GetSpellAbilityUnit()), G.udg_LocalPosition2, bj_UNIT_FACING)
    RemoveUnit(GetSpellAbilityUnit())
    SetPlayerTechResearchedSwap(FourCC('R07J'), 1, GetOwningPlayer(GetTriggerUnit()))
    RemoveLocation(G.udg_LocalPosition2)
end

function InitTrig_Race_Nocnorogdennue_O()
    G.gg_trg_Race_Nocnorogdennue_O = CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(G.gg_trg_Race_Nocnorogdennue_O, EVENT_PLAYER_UNIT_SPELL_FINISH)
    TriggerAddCondition(G.gg_trg_Race_Nocnorogdennue_O, Condition(Trig_Race_Nocnorogdennue_O_Conditions))
    TriggerAddAction(G.gg_trg_Race_Nocnorogdennue_O, Trig_Race_Nocnorogdennue_O_Actions)
end

--===========================================================================
-- 19. Race Draeneis O
--===========================================================================
function Trig_Race_Draeneis_O_Conditions()
    return GetSpellAbilityId() == FourCC('A0HS')
end

function Trig_Race_Draeneis_O_Actions()
    G.udg_LocalPosition2 = GetUnitLoc(GetTriggerUnit())
    CreateNUnitsAtLoc(5, FourCC('h012'), GetOwningPlayer(GetSpellAbilityUnit()), G.udg_LocalPosition2, bj_UNIT_FACING)
    SetPlayerTechResearchedSwap(FourCC('R07G'), 1, GetOwningPlayer(GetTriggerUnit()))
    RemoveUnit(GetSpellAbilityUnit())
    RemoveLocation(G.udg_LocalPosition2)
end

function InitTrig_Race_Draeneis_O()
    G.gg_trg_Race_Draeneis_O = CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(G.gg_trg_Race_Draeneis_O, EVENT_PLAYER_UNIT_SPELL_FINISH)
    TriggerAddCondition(G.gg_trg_Race_Draeneis_O, Condition(Trig_Race_Draeneis_O_Conditions))
    TriggerAddAction(G.gg_trg_Race_Draeneis_O, Trig_Race_Draeneis_O_Actions)
end

--===========================================================================
-- 20. Race Vryculs O
--===========================================================================
function Trig_Race_Vryculs_O_Conditions()
    return GetSpellAbilityId() == FourCC('A0HP')
end

function Trig_Race_Vryculs_O_Actions()
    G.udg_LocalPosition2 = GetUnitLoc(GetTriggerUnit())
    CreateNUnitsAtLoc(5, FourCC('h0C9'), GetOwningPlayer(GetSpellAbilityUnit()), G.udg_LocalPosition2, bj_UNIT_FACING)
    SetPlayerTechResearchedSwap(FourCC('R07F'), 1, GetOwningPlayer(GetTriggerUnit()))
    RemoveUnit(GetSpellAbilityUnit())
    RemoveLocation(G.udg_LocalPosition2)
end

function InitTrig_Race_Vryculs_O()
    G.gg_trg_Race_Vryculs_O = CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(G.gg_trg_Race_Vryculs_O, EVENT_PLAYER_UNIT_SPELL_FINISH)
    TriggerAddCondition(G.gg_trg_Race_Vryculs_O, Condition(Trig_Race_Vryculs_O_Conditions))
    TriggerAddAction(G.gg_trg_Race_Vryculs_O, Trig_Race_Vryculs_O_Actions)
end

--===========================================================================
-- 21. Race Kult Sum Molota O
--===========================================================================
function Trig_Race_Kult_Sum_Molota_O_Conditions()
    return GetSpellAbilityId() == FourCC('A0HX')
end

function Trig_Race_Kult_Sum_Molota_O_Actions()
    G.udg_LocalPosition2 = GetUnitLoc(GetTriggerUnit())
    CreateNUnitsAtLoc(5, FourCC('o00J'), GetOwningPlayer(GetSpellAbilityUnit()), G.udg_LocalPosition2, bj_UNIT_FACING)
    SetPlayerTechResearchedSwap(FourCC('R07K'), 1, GetOwningPlayer(GetTriggerUnit()))
    SetPlayerTechResearchedSwap(FourCC('R0KD'), 1, GetOwningPlayer(GetTriggerUnit()))
    RemoveUnit(GetSpellAbilityUnit())
    RemoveLocation(G.udg_LocalPosition2)
end

function InitTrig_Race_Kult_Sum_Molota_O()
    G.gg_trg_Race_Kult_Sum_Molota_O = CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(G.gg_trg_Race_Kult_Sum_Molota_O, EVENT_PLAYER_UNIT_SPELL_FINISH)
    TriggerAddCondition(G.gg_trg_Race_Kult_Sum_Molota_O, Condition(Trig_Race_Kult_Sum_Molota_O_Conditions))
    TriggerAddAction(G.gg_trg_Race_Kult_Sum_Molota_O, Trig_Race_Kult_Sum_Molota_O_Actions)
end

--===========================================================================
-- 22. Race Nerubs O
--===========================================================================
function Trig_Race_Nerubs_O_Conditions()
    return GetSpellAbilityId() == FourCC('A0HT')
end

function Trig_Race_Nerubs_O_Actions()
    G.udg_LocalPosition2 = GetUnitLoc(GetTriggerUnit())
    CreateNUnitsAtLoc(3, FourCC('h0BE'), GetOwningPlayer(GetSpellAbilityUnit()), G.udg_LocalPosition2, bj_UNIT_FACING)
    SetPlayerTechResearchedSwap(FourCC('R07N'), 1, GetOwningPlayer(GetTriggerUnit()))
    RemoveUnit(GetSpellAbilityUnit())
    RemoveLocation(G.udg_LocalPosition2)
end

function InitTrig_Race_Nerubs_O()
    G.gg_trg_Race_Nerubs_O = CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(G.gg_trg_Race_Nerubs_O, EVENT_PLAYER_UNIT_SPELL_FINISH)
    TriggerAddCondition(G.gg_trg_Race_Nerubs_O, Condition(Trig_Race_Nerubs_O_Conditions))
    TriggerAddAction(G.gg_trg_Race_Nerubs_O, Trig_Race_Nerubs_O_Actions)
end

--===========================================================================
-- 23. Race Silitids O
--===========================================================================
function Trig_Race_Silitids_O_Conditions()
    return GetSpellAbilityId() == FourCC('A0J7')
end

function Trig_Race_Silitids_O_Actions()
    G.udg_LocalPosition2 = GetUnitLoc(GetTriggerUnit())
    CreateNUnitsAtLoc(8, FourCC('e01G'), GetOwningPlayer(GetSpellAbilityUnit()), G.udg_LocalPosition2, bj_UNIT_FACING)
    SetPlayerTechResearchedSwap(FourCC('R0BV'), 1, GetOwningPlayer(GetTriggerUnit()))
    SetPlayerAbilityAvailableBJ(true, FourCC('A1B7'), GetOwningPlayer(GetTriggerUnit()))
    RemoveUnit(GetSpellAbilityUnit())
    ConditionalTriggerExecute(G.gg_trg_SilitidsOn)
    RemoveLocation(G.udg_LocalPosition2)
end

function InitTrig_Race_Silitids_O()
    G.gg_trg_Race_Silitids_O = CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(G.gg_trg_Race_Silitids_O, EVENT_PLAYER_UNIT_SPELL_FINISH)
    TriggerAddCondition(G.gg_trg_Race_Silitids_O, Condition(Trig_Race_Silitids_O_Conditions))
    TriggerAddAction(G.gg_trg_Race_Silitids_O, Trig_Race_Silitids_O_Actions)
end

--===========================================================================
-- 24. Race Gnomes
--===========================================================================
function Trig_Race_Gnomes_Conditions()
    return GetSpellAbilityId() == FourCC('A0SD')
end

function Trig_Race_Gnomes_Actions()
    G.udg_LocalPosition2 = GetUnitLoc(GetTriggerUnit())
    CreateNUnitsAtLoc(5, FourCC('h0FA'), GetOwningPlayer(GetSpellAbilityUnit()), G.udg_LocalPosition2, bj_UNIT_FACING)
    CreateNUnitsAtLoc(1, FourCC('h0FX'), GetOwningPlayer(GetSpellAbilityUnit()), G.udg_LocalPosition2, bj_UNIT_FACING)
    SetPlayerTechResearchedSwap(FourCC('R0BX'), 1, GetOwningPlayer(GetTriggerUnit()))
    SetPlayerTechResearchedSwap(FourCC('R0HW'), 1, GetOwningPlayer(GetTriggerUnit()))
    RemoveUnit(GetSpellAbilityUnit())
    ConditionalTriggerExecute(G.gg_trg_GnomesOn)
    RemoveLocation(G.udg_LocalPosition2)
end

function InitTrig_Race_Gnomes()
    G.gg_trg_Race_Gnomes = CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(G.gg_trg_Race_Gnomes, EVENT_PLAYER_UNIT_SPELL_FINISH)
    TriggerAddCondition(G.gg_trg_Race_Gnomes, Condition(Trig_Race_Gnomes_Conditions))
    TriggerAddAction(G.gg_trg_Race_Gnomes, Trig_Race_Gnomes_Actions)
end

--===========================================================================
-- 25. Race Gilneas
--===========================================================================
function Trig_Race_Gilneas_Conditions()
    return GetSpellAbilityId() == FourCC('A121')
end

function Trig_Race_Gilneas_Actions()
    G.udg_LocalPosition2 = GetUnitLoc(GetTriggerUnit())
    CreateNUnitsAtLoc(5, FourCC('h0IT'), GetOwningPlayer(GetSpellAbilityUnit()), G.udg_LocalPosition2, bj_UNIT_FACING)
    SetPlayerTechResearchedSwap(FourCC('R0FX'), 1, GetOwningPlayer(GetTriggerUnit()))
    RemoveUnit(GetSpellAbilityUnit())
    RemoveLocation(G.udg_LocalPosition2)
end

function InitTrig_Race_Gilneas()
    G.gg_trg_Race_Gilneas = CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(G.gg_trg_Race_Gilneas, EVENT_PLAYER_UNIT_SPELL_FINISH)
    TriggerAddCondition(G.gg_trg_Race_Gilneas, Condition(Trig_Race_Gilneas_Conditions))
    TriggerAddAction(G.gg_trg_Race_Gilneas, Trig_Race_Gilneas_Actions)
end

--===========================================================================
-- 26. Race Nagi
--===========================================================================
function Trig_Race_Nagi_Conditions()
    return GetSpellAbilityId() == FourCC('A14O')
end

function Trig_Race_Nagi_Actions()
    G.udg_LocalPosition2 = GetUnitLoc(GetTriggerUnit())
    CreateNUnitsAtLoc(5, FourCC('nmpe'), GetOwningPlayer(GetSpellAbilityUnit()), G.udg_LocalPosition2, bj_UNIT_FACING)
    SetPlayerTechResearchedSwap(FourCC('R0FS'), 1, GetOwningPlayer(GetTriggerUnit()))
    RemoveUnit(GetSpellAbilityUnit())
    RemoveLocation(G.udg_LocalPosition2)
end

function InitTrig_Race_Nagi()
    G.gg_trg_Race_Nagi = CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(G.gg_trg_Race_Nagi, EVENT_PLAYER_UNIT_SPELL_FINISH)
    TriggerAddCondition(G.gg_trg_Race_Nagi, Condition(Trig_Race_Nagi_Conditions))
    TriggerAddAction(G.gg_trg_Race_Nagi, Trig_Race_Nagi_Actions)
end

--===========================================================================
-- 27. Race Night Elf
--===========================================================================
function Trig_Race_nightelf_Conditions()
    return GetSpellAbilityId() == FourCC('A0HL')
end

function Trig_Race_nightelf_Actions()
    G.udg_LocalPosition2 = GetUnitLoc(GetTriggerUnit())
    CreateNUnitsAtLoc(6, FourCC('ewsp'), GetOwningPlayer(GetSpellAbilityUnit()), G.udg_LocalPosition2, bj_UNIT_FACING)
    SetPlayerTechResearchedSwap(FourCC('R07L'), 1, GetOwningPlayer(GetTriggerUnit()))
    RemoveUnit(GetSpellAbilityUnit())
    RemoveLocation(G.udg_LocalPosition2)
end

function InitTrig_Race_nightelf()
    G.gg_trg_Race_nightelf = CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(G.gg_trg_Race_nightelf, EVENT_PLAYER_UNIT_SPELL_FINISH)
    TriggerAddCondition(G.gg_trg_Race_nightelf, Condition(Trig_Race_nightelf_Conditions))
    TriggerAddAction(G.gg_trg_Race_nightelf, Trig_Race_nightelf_Actions)
end

--===========================================================================
-- 28. Race Forsaken
--===========================================================================
function Trig_Race_Forsaken_Conditions()
    return GetSpellAbilityId() == FourCC('A155')
end

function Trig_Race_Forsaken_Actions()
    G.udg_LocalPosition2 = GetUnitLoc(GetTriggerUnit())
    CreateNUnitsAtLoc(5, FourCC('h0J5'), GetOwningPlayer(GetSpellAbilityUnit()), G.udg_LocalPosition2, bj_UNIT_FACING)
    SetPlayerTechResearchedSwap(FourCC('R0G3'), 1, GetOwningPlayer(GetTriggerUnit()))
    ForsakenOn()
    RemoveUnit(GetSpellAbilityUnit())
    RemoveLocation(G.udg_LocalPosition2)
end

function InitTrig_Race_Forsaken()
    G.gg_trg_Race_Forsaken = CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(G.gg_trg_Race_Forsaken, EVENT_PLAYER_UNIT_SPELL_FINISH)
    TriggerAddCondition(G.gg_trg_Race_Forsaken, Condition(Trig_Race_Forsaken_Conditions))
    TriggerAddAction(G.gg_trg_Race_Forsaken, Trig_Race_Forsaken_Actions)
end

--===========================================================================
-- 29. Race Ogres
--===========================================================================
function Trig_Race_Ogres_Conditions()
    return GetSpellAbilityId() == FourCC('A17N')
end

function Trig_Race_Ogres_Actions()
    G.udg_LocalPosition2 = GetUnitLoc(GetTriggerUnit())
    CreateNUnitsAtLoc(5, FourCC('o03W'), GetOwningPlayer(GetSpellAbilityUnit()), G.udg_LocalPosition2, bj_UNIT_FACING)
    SetPlayerTechResearchedSwap(FourCC('R0HT'), 1, GetOwningPlayer(GetTriggerUnit()))
    RemoveUnit(GetSpellAbilityUnit())
    RemoveLocation(G.udg_LocalPosition2)
end

function InitTrig_Race_Ogres()
    G.gg_trg_Race_Ogres = CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(G.gg_trg_Race_Ogres, EVENT_PLAYER_UNIT_SPELL_FINISH)
    TriggerAddCondition(G.gg_trg_Race_Ogres, Condition(Trig_Race_Ogres_Conditions))
    TriggerAddAction(G.gg_trg_Race_Ogres, Trig_Race_Ogres_Actions)
end

--===========================================================================
-- 30. Race Alliance
--===========================================================================
function Trig_Race_Alliance_Conditions()
    return GetSpellAbilityId() == FourCC('A02A')
end

function Trig_Race_Alliance_Actions()
    G.udg_LocalPosition2 = GetUnitLoc(GetTriggerUnit())
    CreateNUnitsAtLoc(5, FourCC('hpea'), GetOwningPlayer(GetSpellAbilityUnit()), G.udg_LocalPosition2, bj_UNIT_FACING)
    RemoveUnit(GetSpellAbilityUnit())
    ConditionalTriggerExecute(G.gg_trg_AllyOn)
    SetPlayerTechResearchedSwap(FourCC('R0GZ'), 1, GetOwningPlayer(GetTriggerUnit()))
    SetPlayerTechResearchedSwap(FourCC('R0HX'), 1, GetOwningPlayer(GetTriggerUnit()))
    SetPlayerTechResearchedSwap(FourCC('R0HW'), 1, GetOwningPlayer(GetTriggerUnit()))
    SetPlayerTechResearchedSwap(FourCC('R0HY'), 1, GetOwningPlayer(GetTriggerUnit()))
    SetPlayerTechResearchedSwap(FourCC('R0KK'), 1, GetOwningPlayer(GetTriggerUnit()))
    RemoveLocation(G.udg_LocalPosition2)
end

function InitTrig_Race_Alliance()
    G.gg_trg_Race_Alliance = CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(G.gg_trg_Race_Alliance, EVENT_PLAYER_UNIT_SPELL_FINISH)
    TriggerAddCondition(G.gg_trg_Race_Alliance, Condition(Trig_Race_Alliance_Conditions))
    TriggerAddAction(G.gg_trg_Race_Alliance, Trig_Race_Alliance_Actions)
end

--===========================================================================
-- 31. Race JungleTrolls
--===========================================================================
function Trig_Race_JungleTrolls_Conditions()
    return GetSpellAbilityId() == FourCC('A1DZ')
end

function Trig_Race_JungleTrolls_Actions()
    G.udg_LocalPosition2 = GetUnitLoc(GetTriggerUnit())
    CreateNUnitsAtLoc(5, FourCC('o04Q'), GetOwningPlayer(GetSpellAbilityUnit()), G.udg_LocalPosition2, bj_UNIT_FACING)
    RemoveUnit(GetSpellAbilityUnit())
    SetPlayerTechResearchedSwap(FourCC('R0IH'), 1, GetOwningPlayer(GetTriggerUnit()))
    StartJungleTrolls()
    RemoveLocation(G.udg_LocalPosition2)
end

function InitTrig_Race_JungleTrolls()
    G.gg_trg_Race_JungleTrolls = CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(G.gg_trg_Race_JungleTrolls, EVENT_PLAYER_UNIT_SPELL_FINISH)
    TriggerAddCondition(G.gg_trg_Race_JungleTrolls, Condition(Trig_Race_JungleTrolls_Conditions))
    TriggerAddAction(G.gg_trg_Race_JungleTrolls, Trig_Race_JungleTrolls_Actions)
end

--===========================================================================
-- 32. Race FelOrk
--===========================================================================
function Trig_Race_FelOrk_Conditions()
    return GetSpellAbilityId() == FourCC('A1JL')
end

function Trig_Race_FelOrk_Actions()
    G.udg_LocalPosition2 = GetUnitLoc(GetTriggerUnit())
    CreateNUnitsAtLoc(5, FourCC('n06B'), GetOwningPlayer(GetSpellAbilityUnit()), G.udg_LocalPosition2, bj_UNIT_FACING)
    RemoveUnit(GetSpellAbilityUnit())
    SetPlayerTechResearchedSwap(FourCC('R0KA'), 1, GetOwningPlayer(GetTriggerUnit()))
    SetPlayerTechResearchedSwap(FourCC('R0KC'), 1, GetOwningPlayer(GetTriggerUnit()))
    RemoveLocation(G.udg_LocalPosition2)
end

function InitTrig_Race_FelOrk()
    G.gg_trg_Race_FelOrk = CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(G.gg_trg_Race_FelOrk, EVENT_PLAYER_UNIT_SPELL_FINISH)
    TriggerAddCondition(G.gg_trg_Race_FelOrk, Condition(Trig_Race_FelOrk_Conditions))
    TriggerAddAction(G.gg_trg_Race_FelOrk, Trig_Race_FelOrk_Actions)
end

--===========================================================================
-- 33. Race ForestTrolls
--===========================================================================
function Trig_Race_ForestTrolls_Conditions()
    return GetSpellAbilityId() == FourCC('A1FN')
end

function Trig_Race_ForestTrolls_Actions()
    G.udg_LocalPosition2 = GetUnitLoc(GetTriggerUnit())
    CreateNUnitsAtLoc(5, FourCC('o04V'), GetOwningPlayer(GetSpellAbilityUnit()), G.udg_LocalPosition2, bj_UNIT_FACING)
    RemoveUnit(GetSpellAbilityUnit())
    SetPlayerTechResearchedSwap(FourCC('R0J1'), 1, GetOwningPlayer(GetTriggerUnit()))
    StartForestTrolls()
    RemoveLocation(G.udg_LocalPosition2)
end

function InitTrig_Race_ForestTrolls()
    G.gg_trg_Race_ForestTrolls = CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(G.gg_trg_Race_ForestTrolls, EVENT_PLAYER_UNIT_SPELL_FINISH)
    TriggerAddCondition(G.gg_trg_Race_ForestTrolls, Condition(Trig_Race_ForestTrolls_Conditions))
    TriggerAddAction(G.gg_trg_Race_ForestTrolls, Trig_Race_ForestTrolls_Actions)
end

--===========================================================================
-- 34. Race CultOfDamned
--===========================================================================
function Trig_Race_CultOfDamned_Conditions()
    return GetSpellAbilityId() == FourCC('A1HA')
end

function Trig_Race_CultOfDamned_Actions()
    G.udg_LocalPosition2 = GetUnitLoc(GetTriggerUnit())
    CreateNUnitsAtLoc(3, FourCC('cD02'), GetOwningPlayer(GetSpellAbilityUnit()), G.udg_LocalPosition2, bj_UNIT_FACING)
    RemoveUnit(GetSpellAbilityUnit())
    SetPlayerTechResearchedSwap(FourCC('R0J4'), 1, GetOwningPlayer(GetTriggerUnit()))
    SetPlayerTechResearchedSwap(FourCC('R0J5'), 1, GetOwningPlayer(GetTriggerUnit()))
    CultOn()
    RemoveLocation(G.udg_LocalPosition2)
end

function InitTrig_Race_CultOfDamned()
    G.gg_trg_Race_CultOfDamned = CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(G.gg_trg_Race_CultOfDamned, EVENT_PLAYER_UNIT_SPELL_FINISH)
    TriggerAddCondition(G.gg_trg_Race_CultOfDamned, Condition(Trig_Race_CultOfDamned_Conditions))
    TriggerAddAction(G.gg_trg_Race_CultOfDamned, Trig_Race_CultOfDamned_Actions)
end

--===========================================================================
-- 35. Race Pandarens
--===========================================================================
function Trig_Race_Pandarens_Conditions()
    return GetSpellAbilityId() == FourCC('A1I6')
end

function Trig_Race_Pandarens_Actions()
    G.udg_LocalPosition2 = GetUnitLoc(GetTriggerUnit())
    CreateNUnitsAtLoc(5, FourCC('pa01'), GetOwningPlayer(GetSpellAbilityUnit()), G.udg_LocalPosition2, bj_UNIT_FACING)
    RemoveUnit(GetSpellAbilityUnit())
    SetPlayerTechResearchedSwap(FourCC('R0L3'), 1, GetOwningPlayer(GetTriggerUnit()))
    Pstart(GetOwningPlayer(GetTriggerUnit()))
    RemoveLocation(G.udg_LocalPosition2)
end

function InitTrig_Race_Pandarens()
    G.gg_trg_Race_Pandarens = CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(G.gg_trg_Race_Pandarens, EVENT_PLAYER_UNIT_SPELL_FINISH)
    TriggerAddCondition(G.gg_trg_Race_Pandarens, Condition(Trig_Race_Pandarens_Conditions))
    TriggerAddAction(G.gg_trg_Race_Pandarens, Trig_Race_Pandarens_Actions)
end

--===========================================================================
-- 36. Race HordeW2
--===========================================================================
function Trig_Race_HordeW2_Conditions()
    return GetSpellAbilityId() == FourCC('A1JN')
end

function Trig_Race_HordeW2_Actions()
    G.udg_LocalPosition2 = GetUnitLoc(GetTriggerUnit())
    CreateNUnitsAtLoc(5, FourCC('w200'), GetOwningPlayer(GetSpellAbilityUnit()), G.udg_LocalPosition2, bj_UNIT_FACING)
    RemoveUnit(GetSpellAbilityUnit())
    SetPlayerTechResearchedSwap(FourCC('R0KB'), 1, GetOwningPlayer(GetTriggerUnit()))
    SetPlayerTechResearchedSwap(FourCC('R0KC'), 1, GetOwningPlayer(GetTriggerUnit()))
    SetPlayerTechResearchedSwap(FourCC('R0KD'), 1, GetOwningPlayer(GetTriggerUnit()))
    RemoveLocation(G.udg_LocalPosition2)
    HordeW2On()
end

function InitTrig_Race_HordeW2()
    G.gg_trg_Race_HordeW2 = CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(G.gg_trg_Race_HordeW2, EVENT_PLAYER_UNIT_SPELL_FINISH)
    TriggerAddCondition(G.gg_trg_Race_HordeW2, Condition(Trig_Race_HordeW2_Conditions))
    TriggerAddAction(G.gg_trg_Race_HordeW2, Trig_Race_HordeW2_Actions)
end

--===========================================================================
-- 37. Race Random
--===========================================================================
function Trig_Race_Random_Conditions()
    return GetSpellAbilityId() == FourCC('A12Q')
end

function Trig_Race_Random_Actions()
    local racecount = 34
    local racechance
    local l = GetUnitLoc(GetTriggerUnit())
    local p = GetOwningPlayer(GetTriggerUnit())
    RemoveUnit(GetSpellAbilityUnit())
    racechance = GetRandomInt(1, racecount)
    G.icrisingN = 0

    if racechance == G.icrisingN + 1 then
        CreateNUnitsAtLoc(5, FourCC('h0G9'), p, l, bj_UNIT_FACING)
        SetPlayerTechResearchedSwap(FourCC('R0H3'), 1, p)
        SetPlayerTechResearchedSwap(FourCC('R0HY'), 1, p)
        TriggerExecute(G.gg_trg_StromgardOn)
    end
    G.icrisingN = G.icrisingN + 1

    if racechance == G.icrisingN + 1 then
        CreateNUnitsAtLoc(1, FourCC('dra1'), p, l, bj_UNIT_FACING)
        SetPlayerTechResearchedSwap(FourCC('R0BY'), 1, p)
        DragonsOn()
    end
    G.icrisingN = G.icrisingN + 1

    if racechance == G.icrisingN + 1 then
        CreateNUnitsAtLoc(5, FourCC('e00F'), p, l, bj_UNIT_FACING)
        SetPlayerTechResearchedSwap(FourCC('R0A2'), 1, p)
        ElemOn()
    end
    G.icrisingN = G.icrisingN + 1

    if racechance == G.icrisingN + 1 then
        CreateNUnitsAtLoc(5, FourCC('n00V'), p, l, bj_UNIT_FACING)
        SetPlayerTechResearchedSwap(FourCC('R07E'), 1, p)
        SetPlayerTechResearchedSwap(FourCC('R0J3'), 1, p)
        TriggerExecute(G.gg_trg_GoblinsOn)
    end
    G.icrisingN = G.icrisingN + 1

    if racechance == G.icrisingN + 1 then
        CreateNUnitsAtLoc(8, FourCC('e02Y'), p, l, bj_UNIT_FACING)
        SetPlayerTechResearchedSwap(FourCC('R0AO'), 1, p)
    end
    G.icrisingN = G.icrisingN + 1

    if racechance == G.icrisingN + 1 then
        CreateNUnitsAtLoc(5, FourCC('h0EI'), p, l, bj_UNIT_FACING)
        SetPlayerTechResearchedSwap(FourCC('R07H'), 1, p)
        SetPlayerTechResearchedSwap(FourCC('R0KZ'), 1, p)
        SetPlayerTechResearchedSwap(FourCC('R0L0'), 1, p)
        ConditionalTriggerExecute(G.gg_trg_IllidaryOn)
    end
    G.icrisingN = G.icrisingN + 1

    if racechance == G.icrisingN + 1 then
        CreateNUnitsAtLoc(5, FourCC('h002'), p, l, bj_UNIT_FACING)
        SetPlayerTechResearchedSwap(FourCC('R00G'), 1, p)
        TriggerExecute(G.gg_trg_BanditsOn)
    end
    G.icrisingN = G.icrisingN + 1

    if racechance == G.icrisingN + 1 then
        CreateNUnitsAtLoc(5, FourCC('h014'), p, l, bj_UNIT_FACING)
        SetPlayerTechResearchedSwap(FourCC('R07B'), 1, p)
    end
    G.icrisingN = G.icrisingN + 1

    if racechance == G.icrisingN + 1 then
        CreateNUnitsAtLoc(3, FourCC('u00P'), p, l, bj_UNIT_FACING)
        SetPlayerTechResearchedSwap(FourCC('R07I'), 1, p)
        ConditionalTriggerExecute(G.gg_trg_UndeadOn)
    end
    G.icrisingN = G.icrisingN + 1

    if racechance == G.icrisingN + 1 then
        CreateNUnitsAtLoc(5, FourCC('h04K'), p, l, bj_UNIT_FACING)
        SetPlayerTechResearchedSwap(FourCC('R07C'), 1, p)
        SetPlayerTechResearchedSwap(FourCC('R0L0'), 1, p)
        ConditionalTriggerExecute(G.gg_trg_BloodElvesOn)
    end
    G.icrisingN = G.icrisingN + 1

    if racechance == G.icrisingN + 1 then
        CreateNUnitsAtLoc(5, FourCC('opeo'), p, l, bj_UNIT_FACING)
        SetPlayerTechResearchedSwap(FourCC('R0DV'), 1, p)
        SetPlayerTechResearchedSwap(FourCC('R0J3'), 1, p)
        ConditionalTriggerExecute(G.gg_trg_HordeOn)
    end
    G.icrisingN = G.icrisingN + 1

    if racechance == G.icrisingN + 1 then
        CreateNUnitsAtLoc(3, FourCC('u001'), p, l, bj_UNIT_FACING)
        SetPlayerTechResearchedSwap(FourCC('R0BW'), 1, p)
        SetPlayerTechResearchedSwap(FourCC('R0KK'), 1, p)
    end
    G.icrisingN = G.icrisingN + 1

    if racechance == G.icrisingN + 1 then
        CreateNUnitsAtLoc(5, FourCC('h013'), p, l, bj_UNIT_FACING)
        SetPlayerTechResearchedSwap(FourCC('R07D'), 1, p)
        SetPlayerTechResearchedSwap(FourCC('R0HX'), 1, p)
    end
    G.icrisingN = G.icrisingN + 1

    if racechance == G.icrisingN + 1 then
        CreateNUnitsAtLoc(5, FourCC('h0CJ'), p, l, bj_UNIT_FACING)
        SetPlayerTechResearchedSwap(FourCC('R07J'), 1, p)
    end
    G.icrisingN = G.icrisingN + 1

    if racechance == G.icrisingN + 1 then
        CreateNUnitsAtLoc(5, FourCC('h012'), p, l, bj_UNIT_FACING)
        SetPlayerTechResearchedSwap(FourCC('R07G'), 1, p)
    end
    G.icrisingN = G.icrisingN + 1

    if racechance == G.icrisingN + 1 then
        CreateNUnitsAtLoc(5, FourCC('h0C9'), p, l, bj_UNIT_FACING)
        SetPlayerTechResearchedSwap(FourCC('R07F'), 1, p)
    end
    G.icrisingN = G.icrisingN + 1

    if racechance == G.icrisingN + 1 then
        CreateNUnitsAtLoc(5, FourCC('o00J'), p, l, bj_UNIT_FACING)
        SetPlayerTechResearchedSwap(FourCC('R07K'), 1, p)
    end
    G.icrisingN = G.icrisingN + 1

    if racechance == G.icrisingN + 1 then
        CreateNUnitsAtLoc(3, FourCC('h0BE'), p, l, bj_UNIT_FACING)
        SetPlayerTechResearchedSwap(FourCC('R07N'), 1, p)
    end
    G.icrisingN = G.icrisingN + 1

    -- Duplicate Nerubs entry (original has two identical blocks)
    if racechance == G.icrisingN + 1 then
        CreateNUnitsAtLoc(3, FourCC('h0BE'), p, l, bj_UNIT_FACING)
        SetPlayerTechResearchedSwap(FourCC('R07N'), 1, p)
    end
    G.icrisingN = G.icrisingN + 1

    if racechance == G.icrisingN + 1 then
        CreateNUnitsAtLoc(8, FourCC('e01G'), p, l, bj_UNIT_FACING)
        SetPlayerTechResearchedSwap(FourCC('R0BV'), 1, p)
        SetPlayerAbilityAvailableBJ(true, FourCC('A1B7'), p)
        ConditionalTriggerExecute(G.gg_trg_SilitidsOn)
    end
    G.icrisingN = G.icrisingN + 1

    if racechance == G.icrisingN + 1 then
        CreateNUnitsAtLoc(5, FourCC('h0FA'), p, l, bj_UNIT_FACING)
        CreateNUnitsAtLoc(1, FourCC('h0FX'), p, l, bj_UNIT_FACING)
        SetPlayerTechResearchedSwap(FourCC('R0BX'), 1, p)
        SetPlayerTechResearchedSwap(FourCC('R0HW'), 1, p)
        ConditionalTriggerExecute(G.gg_trg_GnomesOn)
    end
    G.icrisingN = G.icrisingN + 1

    -- Duplicate Gnomes entry (original has two identical blocks)
    if racechance == G.icrisingN + 1 then
        CreateNUnitsAtLoc(5, FourCC('h0FA'), p, l, bj_UNIT_FACING)
        CreateNUnitsAtLoc(1, FourCC('h0FX'), p, l, bj_UNIT_FACING)
        SetPlayerTechResearchedSwap(FourCC('R0BX'), 1, p)
        SetPlayerTechResearchedSwap(FourCC('R0HW'), 1, p)
        ConditionalTriggerExecute(G.gg_trg_GnomesOn)
    end
    G.icrisingN = G.icrisingN + 1

    if racechance == G.icrisingN + 1 then
        SetPlayerTechResearchedSwap(FourCC('R0FX'), 1, p)
        CreateNUnitsAtLoc(5, FourCC('h0IT'), p, l, bj_UNIT_FACING)
    end
    G.icrisingN = G.icrisingN + 1

    if racechance == G.icrisingN + 1 then
        CreateNUnitsAtLoc(5, FourCC('nmpe'), p, l, bj_UNIT_FACING)
        SetPlayerTechResearchedSwap(FourCC('R0FS'), 1, p)
    end
    G.icrisingN = G.icrisingN + 1

    if racechance == G.icrisingN + 1 then
        CreateNUnitsAtLoc(6, FourCC('ewsp'), p, l, bj_UNIT_FACING)
        SetPlayerTechResearchedSwap(FourCC('R0G4'), 1, p)
    end
    G.icrisingN = G.icrisingN + 1

    -- Forsaken
    if racechance == G.icrisingN + 1 then
        CreateNUnitsAtLoc(5, FourCC('h0J5'), p, l, bj_UNIT_FACING)
        SetPlayerTechResearchedSwap(FourCC('R0G3'), 1, p)
        ForsakenOn()
    end
    G.icrisingN = G.icrisingN + 1

    if racechance == G.icrisingN + 1 then
        CreateNUnitsAtLoc(5, FourCC('o03W'), p, l, bj_UNIT_FACING)
    end
    G.icrisingN = G.icrisingN + 1

    -- Alliance
    if racechance == G.icrisingN + 1 then
        CreateNUnitsAtLoc(5, FourCC('hpea'), p, l, bj_UNIT_FACING)
        SetPlayerTechResearchedSwap(FourCC('R0GZ'), 1, p)
        SetPlayerTechResearchedSwap(FourCC('R0HX'), 1, p)
        SetPlayerTechResearchedSwap(FourCC('R0HW'), 1, p)
        SetPlayerTechResearchedSwap(FourCC('R0HY'), 1, p)
        SetPlayerTechResearchedSwap(FourCC('R0KK'), 1, p)
    end
    G.icrisingN = G.icrisingN + 1

    -- Horde W2
    if racechance == G.icrisingN + 1 then
        CreateNUnitsAtLoc(5, FourCC('w200'), p, l, bj_UNIT_FACING)
        SetPlayerTechResearchedSwap(FourCC('R0KB'), 1, p)
        SetPlayerTechResearchedSwap(FourCC('R0KC'), 1, p)
        SetPlayerTechResearchedSwap(FourCC('R0KD'), 1, p)
        HordeW2On()
    end
    G.icrisingN = G.icrisingN + 1

    -- Pandarens
    if racechance == G.icrisingN + 1 then
        CreateNUnitsAtLoc(5, FourCC('pa01'), p, l, bj_UNIT_FACING)
        SetPlayerTechResearchedSwap(FourCC('R0L3'), 1, p)
    end
    G.icrisingN = G.icrisingN + 1

    -- Cult of Damned
    if racechance == G.icrisingN + 1 then
        CreateNUnitsAtLoc(3, FourCC('cD02'), p, l, bj_UNIT_FACING)
        SetPlayerTechResearchedSwap(FourCC('R0J4'), 1, p)
        SetPlayerTechResearchedSwap(FourCC('R0J5'), 1, p)
        CultOn()
    end
    G.icrisingN = G.icrisingN + 1

    -- Forest Trolls
    if racechance == G.icrisingN + 1 then
        CreateNUnitsAtLoc(5, FourCC('o04V'), p, l, bj_UNIT_FACING)
        SetPlayerTechResearchedSwap(FourCC('R0J1'), 1, p)
        StartForestTrolls()
    end
    G.icrisingN = G.icrisingN + 1

    -- FellOrc
    if racechance == G.icrisingN + 1 then
        CreateNUnitsAtLoc(5, FourCC('n06B'), p, l, bj_UNIT_FACING)
        SetPlayerTechResearchedSwap(FourCC('R0KA'), 1, p)
        SetPlayerTechResearchedSwap(FourCC('R0KC'), 1, p)
    end
    G.icrisingN = G.icrisingN + 1

    -- Jungle Trolls
    if racechance == G.icrisingN + 1 then
        CreateNUnitsAtLoc(5, FourCC('o04Q'), p, l, bj_UNIT_FACING)
        SetPlayerTechResearchedSwap(FourCC('R0IH'), 1, p)
        StartJungleTrolls()
    end
    G.icrisingN = G.icrisingN + 1

    -- Ice Trolls
    if racechance == G.icrisingN + 1 then
        CreateNUnitsAtLoc(5, FourCC('o045'), p, l, bj_UNIT_FACING)
        SetPlayerTechResearchedSwap(FourCC('R0L1'), 1, p)
    end
    G.icrisingN = G.icrisingN + 1

    RemoveLocation(l)
end

function InitTrig_Race_Random()
    G.gg_trg_Race_Random = CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(G.gg_trg_Race_Random, EVENT_PLAYER_UNIT_SPELL_FINISH)
    TriggerAddCondition(G.gg_trg_Race_Random, Condition(Trig_Race_Random_Conditions))
    TriggerAddAction(G.gg_trg_Race_Random, Trig_Race_Random_Actions)
end
