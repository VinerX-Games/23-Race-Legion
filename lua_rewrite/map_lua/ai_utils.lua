-- ============================================================================
-- 23 Race Legion - Lua Rewrite
-- output/ai_utils.lua — AI utility library (converted from LIBRARY_LibDifferentAiStuff)
-- ============================================================================
-- Sources: war3map.j lines 3411-3724 (main AI utils) +
--          lines 4090-4727 (BloodElves functions)
-- Dependencies: tables.lua (AiData, NumberAdd, etc.), ai_filters.lua, utils.lua, globals.lua
-- ============================================================================

-- ============================================================================
-- Required scratch globals (add to globals.lua if not present)
-- ============================================================================
G.gUnit2 = nil
G.gUnit3 = nil
G.gAttacked = nil
G.gMageTP = FourCC('h07A')
if not G.b_OwnBuldingsInRange then G.b_OwnBuldingsInRange = nil end

-- ============================================================================
-- Dependencies: helper functions from LIBRARY_Races / LIBRARY_common
-- These are used by CheckAndAddBuilding, MakeGrade, etc.
-- ============================================================================

function AddBuilding(buildingId, cnt)
    G.tB = 1
    for _ = 1, cnt do
        G.tArray[0] = G.tArray[0] + 1
        G.tArray[G.tArray[0]] = buildingId
    end
end

function CheckAndAddBuilding(pi, buildingId, limit, power)
    if getAiCount(pi, buildingId) < limit then
        AddBuilding(buildingId, power)
    end
end

function AddUnit(unitId, power)
    for _ = 1, power do
        G.tArray[0] = G.tArray[0] + 1
        G.tArray[G.tArray[0]] = unitId
    end
end

function CheckAndAddUnit(pi, unitId, limit, power)
    if limit == 0 or getAiCount(pi, unitId) < limit then
        AddUnit(unitId, power)
    end
end

function aiOrderUnit(u)
    if G.tArray[0] > 0 then
        IssueImmediateOrderById(u, G.tArray[GetRandomInt(1, G.tArray[0])])
        G.tArray[0] = 0
    end
end

-- Used by MakeGrade
function f_ThisType()
    if GetUnitTypeId(GetFilterUnit()) == G.udg_LocalInteger5 then
        G.Counter = G.Counter + 1
        return true
    end
    return false
end

function MakeGrade(gamer, GradeUnit, Grade)
    local b = Condition(f_ThisType)
    G.udg_LocalInteger5 = GradeUnit
    G.Counter = 0
    GroupEnumUnitsOfPlayer(G.gGroup, gamer, b)
    G.gUnit = BlzGroupUnitAt(G.gGroup, GetRandomInt(0, G.Counter))
    if G.gUnit ~= nil then
        IssueImmediateOrderById(G.gUnit, Grade)
    end
    DestroyBoolExpr(b)
end

function MakeGradeCheckCap(gamer, GradeUnit, Grade, Cap)
    if GetPlayerTechCount(gamer, Grade, true) <= Cap then
        MakeGrade(gamer, GradeUnit, Grade)
    end
end

-- Used by Attacker_BloodElves for fleet units
function Attacker_HumanFleet(id, u, target, x, y)
    if id == FourCC('h00Z') or (id == FourCC('h00Y') and not IsUnitType(target, UNIT_TYPE_STRUCTURE)) then
        G.gInt = GetRandomInt(1, 6)
        if G.gInt == 1 and GetUnitStatePercent(target, UNIT_STATE_LIFE, UNIT_STATE_MAX_LIFE) < GetUnitStatePercent(u, UNIT_STATE_LIFE, UNIT_STATE_MAX_LIFE) then
            if DistanceBetweenUnits(u, target) < 125 then
                IssueTargetOrder(u, "ancestralspirit", target)
            end
        elseif G.gInt == 2 then
            if DistanceBetweenUnits(u, target) < 300 then
                IssuePointOrder(u, "clusterrockets", x, y)
            end
        elseif G.gInt == 3 and GetUnitStatePercent(u, UNIT_STATE_LIFE, UNIT_STATE_MAX_LIFE) < 40 then
            IssueImmediateOrder(u, "tranquility")
        end
    end
end

-- ============================================================================
-- LIBRARY_LibDifferentAiStuff: AI utility functions (lines 3411-3724)
-- ============================================================================

-- AiData operations: getAiCount, aiHasUnit, NumberAdd, NumberRem, NumberReset,
-- NumberResetAll are already defined in tables.lua and verified above.

-- ============================================================================
-- HasEnemyNear
-- ============================================================================
function HasEnemyNear(u)
    if u ~= nil then
        G.CheckPlayer = GetOwningPlayer(u)
        GroupEnumUnitsInRange(G.gGroup, GetUnitX(u), GetUnitY(u), 11000, G.udg_B_EnemyUnit)
        if FirstOfGroup(G.gGroup) ~= nil then
            return true
        end
    end
    return false
end

-- ============================================================================
-- ChoseRandomSpot: picks a random owned building near (x,y) for teleport target
-- ============================================================================
function ChoseRandomSpot(pi, x, y)
    G.Counter = 0
    G.CheckPlayer = Player(pi)
    GroupEnumUnitsInRange(G.gGroup, x, y, 3200, G.b_OwnBuldingsInRange)
    return BlzGroupUnitAt(G.gGroup, GetRandomInt(0, G.Counter))
end

-- ============================================================================
-- MakeTPMage: creates a mass teleport mage at dest position, ports to u2
-- ============================================================================
function MakeTPMage(dest, u2, pi)
    G.gX = GetUnitX(dest)
    G.gY = GetUnitY(dest)
    if getAiCount(pi, G.gMageTP) < 10 and GetUnitAbilityLevel(dest, FourCC('A1RD')) == 0 then
        G.gUnit3 = ChoseRandomSpot(pi, G.gX, G.gY)
        if G.gUnit3 ~= nil then
            G.gX = GetUnitX(G.gUnit3)
            G.gY = GetUnitY(G.gUnit3)
        else
            G.gUnit = CreateUnit(Player(pi), FourCC('h07A'), G.gX, G.gY, 0)
        end
        RemoveEffectTimed(AddSpecialEffect("Abilities\\Spells\\Human\\MassTeleport\\MassTeleportCaster.mdl", G.gX, G.gY), 3)
        IssuePointOrder(G.gUnit, "darksummoning", GetUnitX(u2), GetUnitY(u2))
        GroupAddUnit(G.udg_Ai_army[pi], G.gUnit)
        GroupAddUnit(G.AiUnitsToPort[pi], G.gUnit)
        NumberAdd(pi, G.gMageTP)
        AddAbilityTimed(dest, FourCC('A1RD'), 8)
    end
end

-- ============================================================================
-- PortTo: mass teleports army to destination
-- ============================================================================
function PortTo(u)
    G.gPlayer = GetOwningPlayer(u)
    G.gPi = GetPlayerId(G.gPlayer)

    G.LazyCount = 0
    GroupEnumUnitsOfPlayer(G.gGroup, G.gPlayer, G.B_Lazy)
    G.gUnit2 = BlzGroupUnitAt(G.gGroup, GetRandomInt(0, G.LazyCount))

    if IsUnitInGroup(u, G.udg_ZahvatBuildings) then
        UnitAddAbility(u, FourCC('A0Y4'))
        IssuePointOrder(u, "darksummoning", GetUnitX(G.gUnit2), GetUnitY(G.gUnit2))
        if Random(1, 4) then
            MakeTPMage(u, G.gUnit2, G.gPi)
        end
    elseif GetUnitTypeId(u) == G.gMageTP then
        IssuePointOrder(u, "darksummoning", GetUnitX(G.gUnit2), GetUnitY(G.gUnit2))
    else
        MakeTPMage(u, G.gUnit2, G.gPi)
    end
end

-- ============================================================================
-- PortToFast: faster version using InAiArmy filter instead of Lazy
-- ============================================================================
function PortToFast(u)
    G.gPlayer = GetOwningPlayer(u)
    G.gPi = GetPlayerId(G.gPlayer)

    G.LazyCount = 0
    GroupEnumUnitsOfPlayer(G.gGroup, G.gPlayer, G.B_InAiArmy)
    G.gUnit2 = BlzGroupUnitAt(G.gGroup, GetRandomInt(0, G.LazyCount))

    if IsUnitInGroup(G.gAttacked, G.udg_ZahvatBuildings) then
        UnitAddAbility(u, FourCC('A0Y4'))
        IssuePointOrder(u, "darksummoning", GetUnitX(G.gUnit2), GetUnitY(G.gUnit2))
        if Random(1, 4) then
            MakeTPMage(u, G.gUnit2, G.gPi)
        end
    else
        MakeTPMage(u, G.gUnit2, G.gPi)
    end
end

-- ============================================================================
-- WalkPortTo: walks army to destination (delegates to PortTo)
-- ============================================================================
function WalkPortTo(u)
    PortTo(u)
end

-- ============================================================================
-- TryPort: attempts to teleport idle army
-- ============================================================================
function TryPort(pi)
    G.gUnit = GroupPickRandomUnit2(G.AiUnitsToPort[pi])
    if G.gUnit ~= nil then
        G.CheckPlayer = Player(pi)
        if HasEnemyNear(G.gUnit) then
            PortTo(G.gUnit)
        end
    end
end

-- ============================================================================
-- RequestPort: handles port request (loops up to 4 times)
-- ============================================================================
function RequestPort(u)
    G.gPlayer = GetOwningPlayer(u)
    G.gPi = GetPlayerId(G.gPlayer)
    G.gInt = 0
    while G.gInt <= 3 do
        G.gUnit = GroupPickRandomUnit2(G.AiUnitsToPort[G.gPi])
        if G.gUnit ~= nil then
            G.CheckPlayer = G.gPlayer
            if HasEnemyNear(G.gUnit) then
                PortTo(G.gUnit)
            end
            break
        end
        G.gInt = G.gInt + 1
    end
end

-- ============================================================================
-- warRace: sets tech level based on grades
-- ============================================================================
function warRace(grades, p)
    SetPlayerTechResearched(p, FourCC('R03Q'), math.floor(grades / 75) - 1)
end

-- ============================================================================
-- f_TType: filter function for BuildT, finds units matching LocalInteger5 type
-- ============================================================================
function f_TType()
    if GetUnitTypeId(GetEnumUnit()) == G.udg_LocalInteger5 then
        GroupAddUnit(G.udg_LocalOtrad, GetEnumUnit())
    end
end

-- ============================================================================
-- BuildT: upgrades buildings from 'before' type to 'after' type
-- ============================================================================
function BuildT(p, before, after)
    local u = nil

    GroupClear(G.udg_LocalOtrad)
    GroupEnumUnitsOfPlayer(G.gGroup, p, nil)
    G.udg_LocalInteger5 = before
    ForGroup(G.gGroup, f_TType)

    G.gGroup = G.udg_LocalOtrad
    u = GroupPickRandomUnit2(G.gGroup)
    IssueImmediateOrderById(u, after)

    -- Cleanup
    DestroyGroup(G.udg_LocalOtrad)
    G.udg_LocalOtrad = CreateGroup()

    u = nil
end

-- ============================================================================
-- TryBuy: AI buys items from shops
-- ============================================================================
function TryBuy(p, ePoints)
    local u
    local itemId
    GroupEnumUnitsOfPlayer(G.gGroup, p, G.LiveHero)
    u = GroupPickRandomUnit2(G.gGroup)
    if u ~= nil then
        if UnitInventoryCount(u) >= 6 then
            RemoveItem(UnitItemInSlot(u, GetRandomInt(0, 5)))
        end

        G.gInt = GetRandomInt(1, 6)
        if ePoints < 35 then
            if G.gInt == 1 then
                itemId = FourCC('I02S')
            elseif G.gInt == 2 then
                itemId = FourCC('I030')
            elseif G.gInt == 3 then
                itemId = FourCC('I02Z')
            elseif G.gInt == 4 then
                itemId = FourCC('I02Y')
            elseif G.gInt == 5 then
                itemId = FourCC('I02T')
            elseif G.gInt == 6 then
                itemId = FourCC('I02X')
            end
        elseif ePoints < 150 then
            if G.gInt == 1 then
                itemId = FourCC('I010')
            elseif G.gInt == 2 then
                itemId = FourCC('I01A')
            elseif G.gInt == 3 then
                itemId = FourCC('I02Z')
            elseif G.gInt == 4 then
                itemId = FourCC('I01P')
            elseif G.gInt == 5 then
                itemId = FourCC('I002')
            elseif G.gInt == 6 then
                itemId = FourCC('I003')
            end
        else
            if G.gInt == 1 then
                itemId = FourCC('I00W')
            elseif G.gInt == 2 then
                itemId = FourCC('I030')
            elseif G.gInt == 3 then
                itemId = FourCC('I011')
            elseif G.gInt == 4 then
                itemId = FourCC('I00F')
            elseif G.gInt == 5 then
                itemId = FourCC('I017')
            elseif G.gInt == 6 then
                itemId = FourCC('I01C')
            end
        end

        if GetInventoryIndexOfItemTypeBJ(u, itemId) == 0 then
            UnitAddItemByIdSwapped(itemId, u)
        end
    end
    u = nil
end

-- ============================================================================
-- MakeMageTp: spawns a mass teleport mage at the player's altar
-- ============================================================================
function MakeMageTp(pi)
    GroupEnumUnitsOfPlayer(G.gGroup, Player(pi), G.Altars)
    if FirstOfGroup(G.gGroup) ~= nil then
        G.gUnit2 = GroupPickRandomUnit2(G.gGroup)
        G.gUnit = CreateUnit(Player(pi), FourCC('h07A'), GetUnitX(G.gUnit2), GetUnitY(G.gUnit2), 0)
        GroupAddUnit(G.udg_Ai_army[pi], G.gUnit)
        GroupAddUnit(G.AiUnitsToPort[pi], G.gUnit)
        NumberAdd(pi, FourCC('h07A'))
    end
end

-- ============================================================================
-- BLOOD ELVES RACE FUNCTIONS (lines 4090-4727)
-- ============================================================================

-- ============================================================================
-- startBloodElves: initializes Blood Elves AI for a player
-- ============================================================================
function startBloodElves(pi)
    CreateNUnitsAtLoc(8, FourCC('h04K'), Player(pi), G.udg_LocalPoint, bj_UNIT_FACING)
    GroupAddGroup(GetLastCreatedGroup(), G.udg_Ai_units[pi])
    GroupAddGroup(GetLastCreatedGroup(), G.udg_Ai_builders[pi])
    CreateNUnitsAtLoc(1, FourCC('h04C'), Player(pi), G.udg_LocalPoint, bj_UNIT_FACING)
    GroupAddUnit(G.udg_Ai_units[pi], GetLastCreatedUnit())
    GroupAddUnit(G.udg_Ai_buildings[pi], GetLastCreatedUnit())
    if not G.AiData[pi] then G.AiData[pi] = {} end
    G.AiData[pi][FourCC('h04K')] = 8
    G.AiData[pi][FourCC('h04C')] = 1
    SetPlayerName(Player(pi), "Эльфы Крови (" .. (pi + 1) .. ")")
    G.AiData[pi]["Race"] = "BE"
    TriggerExecute(gg_trg_BloodElvesOn)
    G.AiRace[pi] = "BloodElves"
end

-- ============================================================================
-- Join_BloodElves: handles new BloodElves units joining the AI
-- ============================================================================
function Join_BloodElves(id, pi, u)
    if id == FourCC('h04K') then
        GroupAddUnit(G.udg_Ai_builders[pi], u)
    elseif id == FourCC('h00X') or id == FourCC('h00Y') or id == FourCC('h00Z') then
        GroupAddUnit(G.udg_Ai_navy[pi], u)
        NumberAdd(pi, "NumberN")
    elseif aiUnitJoinsCapitalGuard(u, pi) then
        -- Unit joined capital guard, no further action
    else
        aiUnitJoinsArmy(u, pi)
    end

    -- Heroes
    if id == FourCC('H034') then
        G.gInt = GetRandomInt(1, 3)
        if G.gInt == 1 then
            SelectHeroSkill(u, FourCC('AHfs'))
        elseif G.gInt == 2 then
            SelectHeroSkill(u, FourCC('AHbn'))
        else
            SelectHeroSkill(u, FourCC('AHdr'))
        end
    elseif id == FourCC('Hjnd') then
        G.gInt = GetRandomInt(1, 3)
        if G.gInt == 1 then
            SelectHeroSkill(u, FourCC('A07U'))
        elseif G.gInt == 2 then
            SelectHeroSkill(u, FourCC('A0LQ'))
        else
            SelectHeroSkill(u, FourCC('A07V'))
        end
    elseif id == FourCC('H045') then
        G.gInt = GetRandomInt(1, 3)
        if G.gInt == 1 then
            SelectHeroSkill(u, FourCC('A08H'))
        elseif G.gInt == 2 then
            SelectHeroSkill(u, FourCC('A07W'))
        else
            SelectHeroSkill(u, FourCC('AHbh'))
        end
    elseif id == FourCC('h00Z') then
        IssueImmediateOrder(u, "nagabuild")
        IssueImmediateOrder(u, "spellbook")
        G.gInt = GetRandomInt(1, 3)
        if G.gInt == 1 then
            IssueImmediateOrder(u, "nagabuild")
        elseif G.gInt == 2 then
            IssueImmediateOrder(u, "mounthippogryph")
        else
            IssueImmediateOrder(u, "monsoon")
        end
    end
end

-- ============================================================================
-- AttackedBloodElves: handles BloodElves unit behavior when attacked
-- ============================================================================
function AttackedBloodElves(u)
    if GetUnitTypeId(u) == FourCC('h03V') then
        G.gInt = GetRandomInt(1, 5)
        if G.gInt == 1 then
            IssueImmediateOrder(u, "defend")
        elseif G.gInt == 2 then
            IssueImmediateOrder(u, "manashieldon")
        elseif G.gInt == 3 then
            IssueImmediateOrder(u, "undefend")
        end
    elseif GetUnitTypeId(u) == FourCC('h03B') then
        G.gInt = GetRandomInt(1, 3)
        if G.gInt == 1 then
            IssueImmediateOrder(u, "defend")
        elseif G.gInt == 2 then
            IssueImmediateOrder(u, "undefend")
        end
    end
end

-- ============================================================================
-- Attacker_BloodElves: handles BloodElves unit behavior when attacking
-- ============================================================================
function Attacker_BloodElves(id, u, target, p)
    local i
    local x = GetUnitX(target)
    local y = GetUnitY(target)
    local x2
    local y2

    if id == FourCC('H043') then
        i = GetRandomInt(1, 6)
        if i == 1 then
            IssueTargetOrder(u, "banish", target)
        elseif i == 2 then
            IssueTargetOrder(u, "steal", target)
        elseif i == 3 then
            IssuePointOrder(u, "flamestrike", x, y)
        elseif i == 4 then
            IssueImmediateOrder(u, "summonphoenix")
        end
    elseif id == FourCC('Hjnd') then
        i = GetRandomInt(1, 3)
        if i == 1 and not IsUnitType(target, UNIT_TYPE_STRUCTURE) then
            IssueTargetOrder(u, "shadowstrike", target)
        elseif IsUnitType(target, UNIT_TYPE_HERO) then
            IssueTargetOrder(u, "faeriefire", target)
        end
    elseif id == FourCC('H045') then
        i = GetRandomInt(1, 5)
        if i == 1 then
            IssueImmediateOrder(u, "roar")
        elseif i == 2 then
            IssueImmediateOrder(u, "fanofknives")
        elseif i == 3 then
            IssueImmediateOrder(u, "ressurection")
        end
    elseif id == FourCC('H03H') then
        i = GetRandomInt(1, 4)
        if i == 1 then
            IssueImmediateOrder(u, "berserk")
        end
    elseif id == FourCC('n040') then
        i = GetRandomInt(1, 5)
        if i == 1 then
            IssueImmediateOrder(u, "frostarmoron")
            IssueImmediateOrder(u, "curseoff")
        elseif i == 2 then
            IssueImmediateOrder(u, "frostarmoroff")
            IssueImmediateOrder(u, "curseon")
        elseif i == 3 then
            if DistanceBetweenUnits(u, target) < 490 then
                IssueTargetOrder(u, "carrionswarm", target)
            end
        end
    elseif id == FourCC('h041') then
        i = GetRandomInt(1, 3)
        if i == 1 then
            IssueTargetOrder(u, "polymorph", target)
        elseif i == 2 then
            if DistanceBetweenUnits(u, target) < 490 then
                IssueTargetOrder(u, "devourmagic", target)
            end
        end
    elseif id == FourCC('h042') then
        i = GetRandomInt(1, 6)
        if i == 1 then
            IssueImmediateOrder(u, "faeriefireoff")
            IssueImmediateOrder(u, "curseon")
            IssueImmediateOrder(u, "bloodlustoff")
        elseif i == 2 then
            IssueImmediateOrder(u, "faeriefireoff")
            IssueImmediateOrder(u, "curseoff")
            IssueImmediateOrder(u, "bloodluston")
        elseif i == 3 then
            IssueImmediateOrder(u, "faeriefireon")
            IssueImmediateOrder(u, "curseoff")
            IssueImmediateOrder(u, "bloodluston")
        end
    elseif id == FourCC('H03Y') then
        i = GetRandomInt(1, 3)
        if i == 1 then
            G.CheckPlayer = p
            GroupEnumUnitsInRange(G.gGroup, x, y, 550, G.ToHeal)
            G.gUnit2 = GroupPickRandomUnit2(G.gGroup)
            IssueTargetOrder(u, "healingwave", G.gUnit2)
        end
    else
        Attacker_HumanFleet(id, u, target, x, y)
    end
end

-- ============================================================================
-- Strateg_BloodElves_EC: early check for building counts in strategy
-- ============================================================================
function Strateg_BloodElves_EC(id)
    if id == FourCC('h04M') then
        G.udg_LocalInteger3 = G.udg_LocalInteger3 + 1
    elseif id == FourCC('h04C') then
        G.udg_LocalInteger3 = G.udg_LocalInteger3 + 2
    elseif id == FourCC('h04B') then
        G.udg_LocalInteger3 = G.udg_LocalInteger3 + 5
    elseif id == FourCC('h04A') then
        G.udg_LocalInteger3 = G.udg_LocalInteger3 + 8
    end
end

-- ============================================================================
-- Strateg_BloodElves: main strategy function for Blood Elves
-- ============================================================================
function Strateg_BloodElves(i, pi, p)
    local r = 0
    if G.Grades[pi] < 100 then
        if i > 17 then
            r = GetRandomInt(1, 3)
            if r == 1 then
                -- Blacksmith
                MakeGradeCheckCap(p, FourCC('h04R'), FourCC('R01L'), 6)
                MakeGradeCheckCap(p, FourCC('h04R'), FourCC('R01J'), 6)
                MakeGradeCheckCap(p, FourCC('h04R'), FourCC('R01K'), 6)
                MakeGradeCheckCap(p, FourCC('h04R'), FourCC('R01M'), 6)
            elseif r == 2 then
                MakeGradeCheckCap(p, FourCC('h04R'), FourCC('R01R'), 6)
                -- Lumber Mill
                MakeGradeCheckCap(p, FourCC('h04Q'), FourCC('R03I'), 6)
                MakeGradeCheckCap(p, FourCC('h04Q'), FourCC('R03J'), 6)
                MakeGradeCheckCap(p, FourCC('h04Q'), FourCC('R01N'), 6)
            else
                MakeGradeCheckCap(p, FourCC('h04Q'), FourCC('R01T'), 6)
                MakeGradeCheckCap(p, FourCC('h04Q'), FourCC('R03E'), 6)
                MakeGradeCheckCap(p, FourCC('h04Q'), FourCC('R03F'), 6)
                -- Barracks
                MakeGradeCheckCap(p, FourCC('h04D'), FourCC('R03K'), 1)
            end
        end

        if i > 35 and (getAiCount(pi, FourCC('h04B')) + getAiCount(pi, FourCC('h04A')) >= 1) then
            r = GetRandomInt(1, 3)
            if r == 1 then
                -- Barracks
                MakeGradeCheckCap(p, FourCC('h04D'), FourCC('R01Y'), 1)
                MakeGradeCheckCap(p, FourCC('h04D'), FourCC('R01X'), 1)
                MakeGradeCheckCap(p, FourCC('h04D'), FourCC('R01W'), 1)
                MakeGradeCheckCap(p, FourCC('h04D'), FourCC('R01W'), 1)
                -- Magic building
                MakeGradeCheckCap(p, FourCC('h04E'), FourCC('R0BU'), 1)
                MakeGradeCheckCap(p, FourCC('h04E'), FourCC('R01O'), 6)
            elseif r == 2 then
                MakeGradeCheckCap(p, FourCC('h04E'), FourCC('R01P'), 6)
                MakeGradeCheckCap(p, FourCC('h04E'), FourCC('R01Q'), 6)
                MakeGradeCheckCap(p, FourCC('h04E'), FourCC('R01S'), 1)
                -- Workshop
                MakeGradeCheckCap(p, FourCC('h04G'), FourCC('R03N'), 6)
                MakeGradeCheckCap(p, FourCC('h04G'), FourCC('R021'), 6)
            else
                MakeGradeCheckCap(p, FourCC('h04G'), FourCC('R021'), 6)
                MakeGradeCheckCap(p, FourCC('h04G'), FourCC('R03Q'), 6)
                MakeGradeCheckCap(p, FourCC('h04G'), FourCC('R021'), 6)
                MakeGradeCheckCap(p, FourCC('h04G'), FourCC('Rhcd'), 6)
            end

            -- Mana Storage
            r = GetRandomInt(0, 4)
            if r == 0 then
                MakeGradeCheckCap(p, FourCC('h04F'), FourCC('R03R'), 3)
            elseif r == 1 then
                MakeGradeCheckCap(p, FourCC('h04F'), FourCC('R01H'), 3)
            elseif r == 2 then
                MakeGradeCheckCap(p, FourCC('h04F'), FourCC('R01I'), 3)
            elseif r == 3 then
                MakeGradeCheckCap(p, FourCC('h04F'), FourCC('R01G'), 3)
            else
                MakeGradeCheckCap(p, FourCC('h04F'), FourCC('R01D'), 3)
            end

            -- Fleet
            if i > 45 then
                MakeGradeCheckCap(p, FourCC('h011'), FourCC('R005'), 6)
                MakeGradeCheckCap(p, FourCC('h011'), FourCC('R006'), 6)
                MakeGradeCheckCap(p, FourCC('h011'), FourCC('R007'), 6)
                MakeGradeCheckCap(p, FourCC('h011'), FourCC('R002'), 6)
                MakeGradeCheckCap(p, FourCC('h011'), FourCC('R003'), 6)
            end
        end
    else
        warRace(G.Grades[pi], p)
    end

    -- Buy simple item
    if i > 20 and GetPlayerState(p, PLAYER_STATE_RESOURCE_GOLD) > 2000 then
        TryBuy(p, i)
    end

    -- Upgrade to T2
    if i > 25 and getAiCount(pi, FourCC('h04B')) < 3 then
        BuildT(p, FourCC('h04C'), FourCC('h04B'))
    end

    -- Upgrade to T3
    if i > 55 and getAiCount(pi, FourCC('h04A')) < 3 then
        BuildT(p, FourCC('h04B'), FourCC('h04A'))
    end

    -- Spawn teleport mage
    if i > 60 and getAiCount(pi, FourCC('h07A')) < 3 then
        MakeMageTp(pi)
    end
end

-- ============================================================================
-- ChooseBuildings_BloodElves: picks next building to construct
-- ============================================================================
function ChooseBuildings_BloodElves(pi)
    local i

    G.tArray[0] = 1
    G.tArray[1] = FourCC('h04M') -- Farm

    CheckAndAddBuilding(pi, FourCC('h04C'), 4, 4) -- Town Hall
    CheckAndAddBuilding(pi, FourCC('h04M'), 15, 4) -- Additional farms
    CheckAndAddBuilding(pi, FourCC('h04D'), 15, 4) -- Barracks
    CheckAndAddBuilding(pi, FourCC('h04N'), 25, 1) -- Tower
    CheckAndAddBuilding(pi, FourCC('h04Q'), 5, 2)  -- Lumber Mill
    CheckAndAddBuilding(pi, FourCC('h04R'), 6, 2)  -- Blacksmith
    CheckAndAddBuilding(pi, FourCC('h05J'), 3, 8)  -- Altar

    if getAiCount(pi, FourCC('h04B')) + getAiCount(pi, FourCC('h04A')) >= 1 then
        CheckAndAddBuilding(pi, FourCC('h04G'), 15, 8) -- Workshop
        CheckAndAddBuilding(pi, FourCC('h04E'), 15, 8) -- Temple
    end

    CheckAndAddBuilding(pi, FourCC('h04F'), 12, 2) -- Energy Storage

    i = GetRandomInt(1, G.tArray[0])
    return G.tArray[i]
end

-- ============================================================================
-- PereborBuildings2_BloodElves: decides which unit to train from a building
-- ============================================================================
function PereborBuildings2_BloodElves(id, pi, u)
    local a = {} -- Local table instead of JASS array

    if id == FourCC('h04D') then -- Barracks
        a[0] = 1
        a[1] = FourCC('h03V') -- Infantryman

        -- Archer
        if getAiCount(pi, FourCC('h04R')) >= 1 then
            for _ = 1, 1 do
                a[0] = a[0] + 1
                a[a[0]] = FourCC('n00I')
            end
        end

        -- Cavalry
        if getAiCount(pi, FourCC('h04B')) + getAiCount(pi, FourCC('h04A')) >= 1 then
            for _ = 1, 4 do
                a[0] = a[0] + 1
                a[a[0]] = FourCC('h03X')
            end
        end

        -- Blood Knight
        if getAiCount(pi, FourCC('h04A')) >= 1 then
            for _ = 1, 6 do
                a[0] = a[0] + 1
                a[a[0]] = FourCC('h03Y')
            end
        end

        IssueImmediateOrderById(u, a[GetRandomInt(1, a[0])])

    elseif id == FourCC('h04C') then -- Town Hall
        -- Builder
        if getAiCount(pi, FourCC('h04K')) < 20 then
            IssueImmediateOrderById(u, FourCC('h04K'))
        end

    elseif id == FourCC('h04G') then -- Workshop
        a[0] = 0

        -- Ballista
        if getAiCount(pi, FourCC('h04B')) + getAiCount(pi, FourCC('h04A')) >= 1 then
            for _ = 1, 1 do
                a[0] = a[0] + 1
                a[a[0]] = FourCC('e001')
            end
        end

        -- Elemental
        if getAiCount(pi, FourCC('h04B')) + getAiCount(pi, FourCC('h04A')) >= 1 then
            for _ = 1, 2 do
                a[0] = a[0] + 1
                a[a[0]] = FourCC('h046')
            end
        end

        -- Wagon
        if getAiCount(pi, FourCC('h04B')) + getAiCount(pi, FourCC('h04A')) >= 1 then
            for _ = 1, 1 do
                a[0] = a[0] + 1
                a[a[0]] = FourCC('e030')
            end
        end

        -- Golem
        if getAiCount(pi, FourCC('h04A')) >= 1 then
            for _ = 1, 6 do
                a[0] = a[0] + 1
                a[a[0]] = FourCC('h03Z')
            end
        end

        IssueImmediateOrderById(u, a[GetRandomInt(1, a[0])])

    elseif id == FourCC('h04E') then -- Arcane Sanctuary
        G.udg_LocalInteger3 = GetRandomInt(1, 4)
        if G.udg_LocalInteger3 == 1 then
            IssueImmediateOrderById(u, FourCC('h03W'))
        elseif G.udg_LocalInteger3 == 2 then
            IssueImmediateOrderById(u, FourCC('h040'))
        elseif G.udg_LocalInteger3 == 2 then
            IssueImmediateOrderById(u, FourCC('h041'))
        else
            IssueImmediateOrderById(u, FourCC('h042'))
        end

    elseif id == FourCC('h05J') then -- Altar
        G.udg_LocalInteger3 = GetRandomInt(1, 3)
        if G.udg_LocalInteger3 == 1 then
            IssueImmediateOrderById(u, FourCC('Hjnd'))
        end
        if G.udg_LocalInteger3 == 2 then
            IssueImmediateOrderById(u, FourCC('H043'))
        end
        if G.udg_LocalInteger3 == 3 then
            IssueImmediateOrderById(u, FourCC('H045'))
        end
    end
end

-- ============================================================================
-- UpgradeBloodElves: handles unit count updates on upgrade
-- ============================================================================
function UpgradeBloodElves(pi, id)
    if id == FourCC('h05V') then
        NumberRem(pi, FourCC('h05U'))
    elseif id == FourCC('h05W') then
        NumberRem(pi, FourCC('h05V'))
    end
end

-- ============================================================================
-- GetLvlBloodElves: handles hero skill selection on level up
-- ============================================================================
function GetLvlBloodElves(u)
    if GetUnitTypeId(u) == FourCC('H043') then
        G.gInt = GetRandomInt(1, 3)
        if GetHeroLevel(u) == 6 or GetHeroLevel(u) == 10 then
            SelectHeroSkill(u, FourCC('AHpx'))
        elseif G.gInt == 1 then
            SelectHeroSkill(u, FourCC('AHfs'))
        elseif G.gInt == 2 then
            SelectHeroSkill(u, FourCC('AHdr'))
        else
            SelectHeroSkill(u, FourCC('AHpx'))
        end
    elseif GetUnitTypeId(u) == FourCC('Hjnd') then
        G.gInt = GetRandomInt(1, 3)
        if GetHeroLevel(u) == 6 or GetHeroLevel(u) == 10 then
            SelectHeroSkill(u, FourCC('A07V'))
        elseif G.gInt == 1 then
            SelectHeroSkill(u, FourCC('A07U'))
        elseif G.gInt == 2 then
            SelectHeroSkill(u, FourCC('A0LQ'))
        else
            SelectHeroSkill(u, FourCC('AEar'))
        end
    elseif GetUnitTypeId(u) == FourCC('H045') then
        G.gInt = GetRandomInt(1, 3)
        if GetHeroLevel(u) == 6 or GetHeroLevel(u) == 10 then
            SelectHeroSkill(u, FourCC('AHre'))
        elseif G.gInt == 1 then
            SelectHeroSkill(u, FourCC('A08H'))
        elseif G.gInt == 2 then
            SelectHeroSkill(u, FourCC('A07W'))
        else
            SelectHeroSkill(u, FourCC('AHbh'))
        end
    end
end
