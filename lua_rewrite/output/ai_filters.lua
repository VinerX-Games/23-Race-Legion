-- ============================================================================
-- 23 Race Legion - Lua Rewrite
-- output/ai_filters.lua — AI filter library (converted from LIBRARY_AI0)
-- ============================================================================

-- ============================================================================
-- Общие функции
-- ============================================================================

function isUnitInNoWaterArea(x, y)
    return RectContainsCoords(gg_rct_NoWater1, x, y) or RectContainsCoords(gg_rct_NoWater2, x, y) or RectContainsCoords(gg_rct_NoWater3, x, y)
end

function isUnitWaterRelated(u)
    return IsUnitInGroup(u, G.udg_CityNearWater) or IsUnitInGroup(u, G.Navy) or IsUnitInGroup(u, G.Port)
end

-- ============================================================================
-- Функции для фильтров
-- ============================================================================

function f_EnemyUnitP()
    local u = GetFilterUnit()
    local p = GetOwningPlayer(u)
    if (UnitAlive(u) and IsPlayerEnemy(p, G.CheckPlayer)) or (WaygateIsActive(u) and not (IsUnitInGroup(u, G.Navy) or GetUnitAbilityLevel(u, FourCC('A1MS')) > 0)) then -- A1MS Стр точка
        G.Counter = G.Counter + 1
        if IsUnitInGroup(u, G.udg_StolicaGroups) then
            G.EnemyCapital = u
        end
        return true
    else
        return false
    end
end

function f_EnemyUnit()
    local u = GetFilterUnit()
    if UnitAlive(u) and IsPlayerEnemy(GetOwningPlayer(u), G.CheckPlayer) and not (WaygateIsActive(u) or IsUnitInGroup(u, G.Navy) or GetUnitAbilityLevel(u, FourCC('A1MS')) > 0) then
        G.Counter = G.Counter + 1
        if IsUnitInGroup(u, G.udg_StolicaGroups) then
            G.EnemyCapital = u
        end
        return true
    end
    return false
end

-- Цель для флота
function f_EnemyUnitN()
    local u = GetFilterUnit()
    local p = GetOwningPlayer(u)
    local x = GetUnitX(u)
    local y = GetUnitY(u)

    if UnitAlive(u) and IsPlayerEnemy(p, G.CheckPlayer) and isUnitWaterRelated(u) and not (isUnitInNoWaterArea(x, y) or WaygateIsActive(u)) then
        G.Counter = G.Counter + 1
        return true
    else
        return false
    end
end

function f_ToHeal()
    local u = GetFilterUnit()
    if IsPlayerAlly(GetOwningPlayer(u), G.CheckPlayer) and IsUnitIdType(GetUnitTypeId(u), UNIT_TYPE_MECHANICAL) ~= true then
        return true
    else
        return false
    end
end

-- Главный фильтр для войск, кому надо отдать приказ
function f_Lazy()
    G.gUnit = GetFilterUnit()
    G.gInt = GetUnitCurrentOrder(G.gUnit)

    if UnitAlive(G.gUnit) and IsUnitInGroup(G.gUnit, G.udg_Ai_army[GetPlayerId(GetOwningPlayer(G.gUnit))]) and (G.gInt == 851972 or G.gInt == 851976 or G.gInt == 0) and not (IsUnitType(G.gUnit, UNIT_TYPE_PEON) or IsUnitType(G.gUnit, UNIT_TYPE_STRUCTURE)) then -- // and ( gInt ==  851972 or gInt == 851976 or gInt == 0 ) and /*
        G.LazyCount = G.LazyCount + 1
        return true
    else
        return false
    end
end

-- Тоже самое + проверка игрока так как тут для радиуса
function f_LazyF()
    G.gUnit = GetFilterUnit()
    G.gInt = GetUnitCurrentOrder(G.gUnit)
    return UnitAlive(G.gUnit) and IsUnitInGroup(G.gUnit, G.udg_Ai_army[GetPlayerId(G.CheckPlayer)]) and (G.gInt == 851972 or G.gInt == 851976 or G.gInt == 0) and not (IsUnitType(G.gUnit, UNIT_TYPE_PEON) or IsUnitType(G.gUnit, UNIT_TYPE_STRUCTURE)) -- //and ( gInt ==  851972 or gInt == 851976 or gInt == 0 )
end

function f_LazyN()
    G.gUnit = GetFilterUnit()
    G.gInt = GetUnitCurrentOrder(G.gUnit)

    if UnitAlive(G.gUnit) and IsUnitInGroup(G.gUnit, G.udg_Ai_navy[GetPlayerId(G.CheckPlayer)]) and (G.gInt == 851972 or G.gInt == 851976 or G.gInt == 0) then
        G.LazyCount = G.LazyCount + 1
        return true
    else
        return false
    end
end

function f_FixZ()
    return GetUnitCurrentOrder(GetFilterUnit()) == 851983
end

function f_FixUnvul()
    return BlzIsUnitInvulnerable(GetFilterUnit())
    -- return GetUnitAbilityLevel(GetFilterUnit(),'Bvul') > 0
end

function f_LazyW()
    G.gUnit = GetFilterUnit()
    G.gInt = GetUnitCurrentOrder(G.gUnit)
    return UnitAlive(G.gUnit) and IsUnitInGroup(G.gUnit, G.udg_Ai_builders[GetPlayerId(GetOwningPlayer(G.gUnit))]) and (G.gInt == 851972 or G.gInt == 851976 or G.gInt == 0)
end

function f_LazyT()
    G.gUnit = GetFilterUnit()
    G.gInt = GetUnitCurrentOrder(G.gUnit)
    return UnitAlive(G.gUnit) and IsUnitInGroup(G.gUnit, G.udg_Ai_buildersT[GetPlayerId(GetOwningPlayer(G.gUnit))]) and (G.gInt == 851972 or G.gInt == 851976 or G.gInt == 0)
end

function f_PortB()
    return IsUnitInGroup(GetFilterUnit(), G.AiUnitsToPort[G.CheckId])
end

function f_Worker()
    G.gUnit = GetFilterUnit()
    return UnitAlive(G.gUnit) and IsUnitInGroup(G.gUnit, G.udg_Ai_buildersT[GetPlayerId(GetOwningPlayer(G.gUnit))])
end

function f_Harwest()
    G.gUnit = GetFilterUnit()
    if UnitAlive(G.gUnit) and IsUnitInGroup(G.gUnit, G.udg_Ai_harvest[GetPlayerId(GetOwningPlayer(G.gUnit))]) then
        return true
    else
        return false
    end
end

function f_InAiArmy()
    G.gUnit = GetFilterUnit()
    return UnitAlive(G.gUnit) and IsUnitInGroup(G.gUnit, G.udg_Ai_army[GetPlayerId(GetOwningPlayer(G.gUnit))])
end

function f_InAiNavy()
    G.gUnit = GetFilterUnit()
    return UnitAlive(G.gUnit) and IsUnitInGroup(G.gUnit, G.udg_Ai_navy[GetPlayerId(GetOwningPlayer(G.gUnit))])
end

-- Здания в которых надо делать найм - без работы, в группе, определенного типа
function f_OnlyNeaded()
    G.gUnit = GetFilterUnit()

    if not UnitAlive(G.gUnit) then
        return false
    end

    G.gPi = GetPlayerId(GetOwningPlayer(G.gUnit))
    -- Проверка на принадлежность к группе сразу
    if not IsUnitInGroup(G.gUnit, G.udg_Ai_buildings[G.gPi]) then
        return false
    end

    G.gInt = GetUnitTypeId(G.gUnit)
    -- Алый орден
    if G.AiRace[G.gPi] == "Scarlet" then
        if G.gInt == FourCC('h05Z') or G.gInt == FourCC('h05X') or G.gInt == FourCC('h011') or G.gInt == FourCC('h064') or G.gInt == FourCC('h05U') or G.gInt == FourCC('h068') or G.gInt == FourCC('h061') or G.gInt == FourCC('h05W') then
            G.Counter = G.Counter + 1
            return true
        end
    -- Эльфы крови
    elseif G.AiRace[G.gPi] == "BloodElves" then
        if G.gInt == FourCC('h04C') or G.gInt == FourCC('h04B') or G.gInt == FourCC('h04K') or G.gInt == FourCC('h04D') or G.gInt == FourCC('h05J') or G.gInt == FourCC('h04G') or G.gInt == FourCC('h04E') or G.gInt == FourCC('h011') then
            G.Counter = G.Counter + 1
            return true
        end
    -- Гоблины
    elseif G.AiRace[G.gPi] == "JungleTrolls" then
        if G.gInt == FourCC('h0N5') or G.gInt == FourCC('h0N1') or G.gInt == FourCC('h0N6') or G.gInt == FourCC('h0MY') or G.gInt == FourCC('h0MX') or G.gInt == FourCC('h0MW') or G.gInt == FourCC('h0N0') then
            G.Counter = G.Counter + 1
            return true
        end
    elseif G.AiRace[G.gPi] == "Goblins" then
        if G.gInt == FourCC('h0D7') or G.gInt == FourCC('o016') or G.gInt == FourCC('h070') or G.gInt == FourCC('h079') or G.gInt == FourCC('h074') or G.gInt == FourCC('h073') or G.gInt == FourCC('h076') or G.gInt == FourCC('h075') then
            G.Counter = G.Counter + 1
            return true
        end
    -- Наги
    elseif G.AiRace[G.gPi] == "Naga" then
        if G.gInt == FourCC('n055') or G.gInt == FourCC('h0JW') or G.gInt == FourCC('n04L') or G.gInt == FourCC('nntt') or G.gInt == FourCC('nnsg') or G.gInt == FourCC('nnsa') or G.gInt == FourCC('nnad') then
            G.Counter = G.Counter + 1
            return true
        end
    -- Орда
    elseif G.AiRace[G.gPi] == "Horde" then
        if G.gInt == FourCC('ogre') or G.gInt == FourCC('orbr') or G.gInt == FourCC('obar') or G.gInt == FourCC('oalt') or G.gInt == FourCC('obea') or G.gInt == FourCC('osld') or G.gInt == FourCC('otto') then
            G.Counter = G.Counter + 1
            return true
        end
    end
    return false
end

function f_NavalBases()
    G.gUnit = GetFilterUnit()
    G.gId = GetUnitTypeId(G.gUnit)

    if UnitAlive(G.gUnit) and (G.gId == FourCC('h011') or G.gId == FourCC('h0D7') or G.gId == FourCC('n04L') or G.gId == FourCC('h0HO')) then
        G.Counter = G.Counter + 1
        return true
    else
        return false
    end
end

function f_Hero()
    return IsUnitType(GetFilterUnit(), UNIT_TYPE_HERO)
end

function f_HeroD()
    return IsUnitType(GetFilterUnit(), UNIT_TYPE_HERO) and GetUnitState(GetFilterUnit(), UNIT_STATE_LIFE) <= 0
end

function f_LiveHero()
    return GetUnitState(GetFilterUnit(), UNIT_STATE_LIFE) > 0.6 and IsUnitType(GetFilterUnit(), UNIT_TYPE_HERO)
end

-- Расовые штуки

-- Алый орден
function f_Altars()
    G.gUnit = GetFilterUnit()
    G.gId = GetUnitTypeId(G.gUnit)
    return (UnitAlive(G.gUnit) and G.gId == FourCC('h05X')) or G.gId == FourCC('h05J') or G.gId == FourCC('o016') or G.gId == FourCC('nnad') or G.gId == FourCC('oalt')
end

-- ============================================================================
-- Setup functions
-- ============================================================================

function MakeHash()
    for i = 0, 23 do
        -- call DisplayTimedTextFromPlayer(Player(0),0,0,4, "Залил хеш")
        if not G.AiData[i] then
            G.AiData[i] = {}
        end
        G.AiData[i][FourCC('h05W')] = 0
        G.AiData[i][FourCC('h0ZX')] = 0
        G.AiData[i][FourCC('h064')] = 0
        G.AiData[i][FourCC('h05Z')] = 0
        G.AiData[i][FourCC('h05W')] = 0
        G.AiData[i][FourCC('h05Y')] = 0
        G.AiData[i][FourCC('h05V')] = 0
        G.AiData[i][FourCC('h061')] = 0
        G.AiData[i][FourCC('h068')] = 0
        G.AiData[i][FourCC('h05W')] = 0
        G.AiData[i][FourCC('h062')] = 0
        G.AiData[i][FourCC('h060')] = 0
    end
    -- call DisplayTimedTextFromPlayer(Player(0),0,0,4, "Залил хеш 2")
end

function SetPortalGroup()
    for i = 0, 23 do
        G.AiUnitsToPort[i] = CreateGroup()
        G.AiCapitalGuard[i] = CreateGroup()
        G.AiCapitalBuildigs[i] = CreateGroup()
        G.Grades[i] = 0
    end
end

function AiLimitsSet()
    G.gInt = CountPlayersInForceBJ(G.udg_Bots)
    G.AiLimit = math.max(70, 200 - G.gInt * 5)

    G.AiMass = math.max(8 - G.gInt, 4)
    G.AiRepeat = 2 + math.min(math.floor(G.gInt / 2), 8)
end

function SetBools()
    -- call DisplayTimedTextFromPlayer(Player(1),0,0, 4,"Инициалзиация буллов")

    G.Altars = Condition(f_Altars)
    G.ToHeal = Condition(f_ToHeal)
    G.B_LazyW = Condition(f_LazyW)
    G.B_Worker = Condition(f_Worker)
    G.B_LazyT = Condition(f_LazyT)
    G.B_Lazy = Condition(f_Lazy)
    G.B_LazyN = Condition(f_LazyN)
    G.B_LazyF = Condition(f_LazyF)
    G.Harwest = Condition(f_Harwest)
    G.B_OnlyNeaded = Condition(f_OnlyNeaded)
    G.B_NavalBases = Condition(f_NavalBases)
    G.B_Hero = Condition(f_Hero)
    G.B_HeroD = Condition(f_HeroD)
    G.B_InAiArmy = Condition(f_InAiArmy)
    G.B_InAiNavy = Condition(f_InAiNavy)
    G.udg_B_EnemyUnitN = Condition(f_EnemyUnitN)
    G.udg_B_EnemyUnit = Condition(f_EnemyUnit)
    G.udg_B_EnemyUnitP = Condition(f_EnemyUnitP)
    G.PortB = Condition(f_PortB)
    G.FixZ = Condition(f_FixZ)
    G.LiveHero = Condition(f_LiveHero)

    G.B_FixUnvul = Condition(f_FixUnvul)

    -- call AiPoitsSet()
    SetPortalGroup()
    MakeHash()
end

-- Master init: calls all setup functions in order
function SetBoolsInit()
    MakeHash()
    SetPortalGroup()
    SetBools()
    AiLimitsSet()
end
