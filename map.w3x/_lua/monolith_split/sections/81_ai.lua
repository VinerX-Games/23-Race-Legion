AiRaces = AiRaces or {}
AiRaceTokens = AiRaceTokens or {}
AiRaceOrder = AiRaceOrder or {}

local function AiNormalizeToken(token)
    if token == nil then
        return nil
    end
    return string.lower(token)
end

---@param key string
---@param def table
function RegisterAiRace(key, def)
    if key == nil or key == "" or def == nil then
        return
    end
    def.key = key
    if AiRaces[key] == nil then
        AiRaceOrder[#AiRaceOrder + 1] = key
    end
    AiRaces[key] = def
    if def.tokens ~= nil then
        for _, token in ipairs(def.tokens) do
            local normalized = AiNormalizeToken(token)
            if normalized ~= nil and normalized ~= "" then
                AiRaceTokens[normalized] = key
            end
        end
    end
end

---@param pi integer
---@return table|nil
function AiRaceOf(pi)
    return AiRaces[AiRace[pi]]
end

---@param token string|nil
---@return table|nil
function AiRaceByToken(token)
    local normalized = AiNormalizeToken(token)
    if normalized == nil or normalized == "" then
        return nil
    end
    local key = AiRaceTokens[normalized]
    if key == nil then
        return nil
    end
    return AiRaces[key]
end

---@return table|nil
function AiRacePickRandom()
    local total = 0
    for _, key in ipairs(AiRaceOrder) do
        local race = AiRaces[key]
        local weight = race and race.weight or 0
        if weight > 0 then
            total = total + weight
        end
    end
    if total <= 0 then
        return nil
    end
    local roll = GetRandomInt(1, total)
    for _, key in ipairs(AiRaceOrder) do
        local race = AiRaces[key]
        local weight = race and race.weight or 0
        if weight > 0 then
            roll = roll - weight
            if roll <= 0 then
                return race
            end
        end
    end
    return nil
end

---@param pi integer
---@param race table|nil
---@return boolean
function AiStartRace(pi, race)
    if race == nil or race.start == nil then
        return false
    end
    race.start(pi)
    return true
end

---@param pi integer
---@param worker unit
---@param x real
---@param y real
---@return boolean
function AiDispatchWallBuild(pi, worker, x, y)
    local race = AiRaceOf(pi)
    if race == nil or race.wall == nil then
        return false
    end
    IssueBuildOrderById(worker, race.wall, x, y)
    return true
end

---@param pi integer
---@return boolean
function AiRaceUsesWaterPoint(pi)
    local race = AiRaceOf(pi)
    return race == nil or race.usesWaterPoint ~= false
end

-- ====================================================================
-- Phase 3: data-driven AI engine (declarative race tables + generic runner).
-- A race may provide `buildings` data; if present the engine is used, else we
-- fall back to the procedural `chooseBuild`. Migrate races one at a time, with
-- the procedural fn kept as a safety net until parity is confirmed.
--
-- def.buildings = {
--   seed = FourCC('h0N2'),                 -- always-present first candidate
--   { FourCC('h0N5'), 4, 4 },              -- { id, limit, power }
--   { FourCC('h0MX'), 8, 6, gate="tier2" },-- optional named gate predicate
-- }
-- def.gates = { tier2 = function(pi) return ... end }   -- race-specific
-- Mirrors ChooseBuildings_* exactly: seed tArray, CheckAndAddBuilding per row
-- (add `power` copies if getAiCount < limit and gate passes), random pick.
-- ====================================================================
---@param pi integer
---@param def table
---@return integer
function AiRunChooseBuildings(pi, def)
    local list = def.buildings
    tArray[0] = 1
    tArray[1] = list.seed
    for _, row in ipairs(list) do
        local gateOk = true
        if row.gate ~= nil then
            local g = def.gates and def.gates[row.gate]
            gateOk = (g == nil) or g(pi)
        end
        if gateOk and getAiCount(pi, row[1]) < row[2] then
            AddBuilding(row[1], row[3])
        end
    end
    return tArray[GetRandomInt(1, tArray[0])]
end

---@param pi integer
---@return integer
function AiDispatchChooseBuild(pi)
    local race = AiRaceOf(pi)
    if race ~= nil then
        if race.chooseBuild ~= nil then
            return race.chooseBuild(pi)
        elseif race.buildings ~= nil then
            return AiRunChooseBuildings(pi, race)
        end
    end
    return 0
end

---@param id integer
---@param pi integer
---@param u unit
function AiDispatchJoin(id, pi, u)
    local race = AiRaceOf(pi)
    if race ~= nil and race.join ~= nil then
        race.join(id, pi, u)
    end
end

-- ====================================================================
-- Phase 3: data-driven production (Perebor) engine.
-- def.production = {
--   [FourCC('h0MY')] = {  -- buildingId → weighted unit pool
--     { FourCC('o04M'), 5 },                      -- { unitId, weight }
--     { FourCC('o05E'), 1, gate = "tier2" },      -- optional named gate
--     { branch = "jt", black = FourCC('o04N'), other = FourCC('o04P'), weight = 4 },
--     { 0, 1 },                                    -- unitId=0 = "train nobody"
--   },
--   worker = { id = FourCC('o04Q'), cap = 18,
--              from = { FourCC('h0N5'), FourCC('h0N1'), FourCC('h0N6') } },
--   pre = function(id, pi, u) ... end,  -- per-building procedural hook
-- }
-- def.branches = { jt = function(pi) return ... end }
-- def.gates   = { tier2 = function(pi) return ... end }
-- ====================================================================
---@param id integer
---@param pi integer
---@param u unit
---@param def table
---@return boolean
function AiRunProduction(id, pi, u, def)
    local prod = def.production
    if not prod then return false end
    local w = prod.worker
    if w and w.from then
        for _, b in ipairs(w.from) do
            if id == b then
                if getAiCount(pi, w.id) < w.cap then
                    IssueImmediateOrderById(u, w.id)
                    return true
                end
                return false
            end
        end
    end
    if prod.pre and prod.pre(id, pi, u) then
        return true
    end
    local rows = prod[id]
    if not rows then return false end
    tArray[0] = 0
    for _, row in ipairs(rows) do
        if row.gate then
            local g = def.gates and def.gates[row.gate]
            if g and not g(pi) then goto continue end
        end
        if row.branch then
            local f = def.branches and def.branches[row.branch]
            local pick = (f and f(pi)) and row.black or row.other
            if pick ~= nil and pick ~= 0 then
                if row.limit and getAiCount(pi, pick) >= row.limit then goto continue end
                AddUnit(pick, row.weight or 1)
            end
        else
            local uid = row[1]
            if uid ~= nil and uid ~= 0 then
                if row.limit and getAiCount(pi, uid) >= row.limit then goto continue end
                AddUnit(uid, row[2] or 1)
            end
        end
        ::continue::
    end
    if tArray[0] > 0 then
        IssueImmediateOrderById(u, tArray[GetRandomInt(1, tArray[0])])
    end
    return true
end

---@param id integer
---@param pi integer
---@param u unit
function AiDispatchPerebor(id, pi, u)
    local race = AiRaceOf(pi)
    if race ~= nil then
        if race.production ~= nil and AiRunProduction(id, pi, u, race) then
            return
        end
        if race.perebor ~= nil then
            race.perebor(id, pi, u)
        end
    end
end

---@param u unit
---@param pi integer
function AiDispatchNaval(u, pi)
    local race = AiRaceOf(pi)
    if race ~= nil and race.naval ~= nil then
        race.naval(u, pi)
    end
end

-- ====================================================================
-- Phase 3: data-driven Strateg (research / techUp) engine.
-- def.strateg = {
--   gradeCap = 100,
--   steps = {
--     { at=17, action="research", rows={{bld,tech,cap},...} },
--     { at=17, action="random", branches={ {{bld,tech,cap},...}, ...} },
--     { at=25, action="techUp", from=bldT1, to=bldT2, cap=3 },
--     { at=45, action="fleet", wall=bldWall },
--     { at=20, action="tryBuy" },
--     { at=60, action="mageTp" },
--     -- gate="name" on any step for conditional execution
--     -- before=N to run when i < N
--   },
-- }
-- def.ecoWeights = { [FourCC('h0N2')]=1, [FourCC('h0N5')]=2, ... }
-- ====================================================================
---@param i integer
---@param pi integer
---@param p player
---@param def table
---@return boolean
function AiRunStrateg(i, pi, p, def)
    local s = def.strategData
    if not s then return false end
    if Grades[pi] >= s.gradeCap then
        warRace(Grades[pi], p)
        return true
    end
    if s.pre and s.pre(i, pi, p) then
    end
    for _, step in ipairs(s.steps) do
        if step.at and i <= step.at then goto cont end
        if step.before and i >= step.before then goto cont end
        if step.gate then
            local g = def.gates and def.gates[step.gate]
            if g and not g(pi) then goto cont end
        end
        local a = step.action
        if a == "research" or a == "random" then
            local rows = step.rows
            if a == "random" and step.branches then
                rows = step.branches[GetRandomInt(1, #step.branches)]
            end
            if rows then
                for _, up in ipairs(rows) do
                    MakeGradeCheckCap(p, up[1], up[2], up[3])
                end
            end
        elseif a == "techUp" then
            if getAiCount(pi, step.to) < step.cap then
                BuildT(p, step.from, step.to)
            end
        elseif a == "fleet" then
            strategFleetGrades(i, p, step.wall)
        elseif a == "tryBuy" then
            if GetPlayerState(p, PLAYER_STATE_RESOURCE_GOLD) > 2000 then
                TryBuy(p, i)
            end
        elseif a == "mageTp" then
            if getAiCount(pi, FourCC('h07A')) < (step.cap or (i / 35)) then
                MakeMageTp(pi)
            end
        end
        ::cont::
    end
    return true
end

---@param id integer
---@param def table
---@return boolean
function AiRunStrategEC(id, def)
    local w = def.ecoWeights
    if not w then return false end
    local add = w[id]
    if add then
        udg_LocalInteger3 = udg_LocalInteger3 + add
        return true
    end
    return false
end

---@param i integer
---@param pi integer
---@param p player
function AiDispatchStrateg(i, pi, p)
    local race = AiRaceOf(pi)
    if race ~= nil then
        if race.strategData ~= nil and AiRunStrateg(i, pi, p, race) then
            return
        end
        if race.strateg ~= nil then
            race.strateg(i, pi, p)
        end
    end
end

---@param id integer
---@param pi integer
function AiDispatchStrategEC(id, pi)
    local race = AiRaceOf(pi)
    if race ~= nil then
        if race.ecoWeights ~= nil and AiRunStrategEC(id, race) then
            return
        end
        if race.strategEC ~= nil then
            race.strategEC(id)
        end
    end
end

---@param id integer
---@param u unit
---@param target unit
---@param p player
---@param def table
---@return boolean
function AiRunAttacker(id, u, target, p, def)
    local tbl = def.attackerData
    if tbl == nil then
        return false
    end
    if tbl.pre ~= nil then
        for _, pre in ipairs(tbl.pre) do
            if GetRandomInt(1, pre.chance or 1) == 1 then
                if pre.terrain == "water" and not IsTerrainPathable(GetUnitX(u), GetUnitY(u), PATHING_TYPE_WALKABILITY) then
                    if pre.notAbil == nil or GetUnitAbilityLevel(u, pre.notAbil) == 0 then
                        _castAbility(u, pre, nil, nil)
                        if pre.ret then
                            return true
                        end
                    end
                end
            end
        end
    end
    local unitAbils = tbl[#tbl] and tbl or tbl -- detect array-or-map
    local entries = tbl[id]
    if entries == nil then
        for _, entry in ipairs(tbl) do
            if entry[id] ~= nil then
                entries = entry[id]
                break
            end
        end
    end
    if entries == nil then
        if tbl.post ~= nil then
            return _castAbilityEntry(u, id, target, tbl.post)
        end
        return false
    end
    for _, entry in ipairs(entries) do
        if GetRandomInt(1, entry.chance or 5) == 1 then
            if entry.notStructure and IsUnitType(target, UNIT_TYPE_STRUCTURE) then
                -- skip
            elseif entry.hp ~= nil and GetUnitStatePercent(u, UNIT_STATE_LIFE, UNIT_STATE_MAX_LIFE) >= entry.hp then
                -- skip: HP too high
            elseif entry.range ~= nil then
                local dx = GetUnitX(u) - GetUnitX(target)
                local dy = GetUnitY(u) - GetUnitY(target)
                if SquareRoot(dx * dx + dy * dy) > entry.range then
                    -- skip: too far
                else
                    _castAbility(u, entry, target, p)
                    break
                end
            else
                _castAbility(u, entry, target, p)
                break
            end
        end
    end
    if tbl.post ~= nil then
        _castAbilityEntry(u, id, target, tbl.post)
    end
    return true
end

---@param u unit
---@param entry table
---@param target unit|nil
---@param p player|nil
function _castAbility(u, entry, target, p)
    local tp = entry.type or "target"
    if tp == "immediate" then
        IssueImmediateOrder(u, entry.order)
    elseif tp == "heal" and p ~= nil then
        gUnit2 = nil
        gGroup = gGroup or CreateGroup()
        GroupEnumUnitsInRange(gGroup, GetUnitX(target), GetUnitY(target), entry.allyRange or 550, ToHeal)
        gUnit2 = GroupPickRandomUnit2(gGroup)
        if gUnit2 ~= nil then
            IssueTargetOrder(u, entry.order, gUnit2)
        end
    elseif tp == "point" and target ~= nil then
        IssuePointOrder(u, entry.order, GetUnitX(target), GetUnitY(target))
    elseif tp == "self" then
        IssuePointOrder(u, entry.order, GetUnitX(u), GetUnitY(u))
    elseif target ~= nil then
        IssueTargetOrder(u, entry.order, target)
    end
end

function _castAbilityEntry(u, id, target, entries)
    for _, entry in ipairs(entries) do
        if entry.needAbil ~= nil and GetUnitAbilityLevel(u, entry.needAbil) == 0 then
            -- skip
        elseif GetRandomInt(1, entry.chance or 4) == 1 then
            _castAbility(u, entry, target, nil)
            break
        end
    end
    return false
end

---@param id integer
---@param u unit
---@param target unit
---@param p player
function AiDispatchAttacker(id, u, target, p)
    local pi = GetPlayerId(p)
    local race = AiRaceOf(pi)
    if race ~= nil then
        if race.attackerData ~= nil and AiRunAttacker(id, u, target, p, race) then
            return
        end
        if race.attacker ~= nil then
            race.attacker(id, u, target, p)
        end
    end
end

---@param u unit
---@param pi integer
---@param def table
---@return boolean
function AiRunAttacked(u, pi, def)
    local tbl = def.attackedData
    if tbl == nil then
        return false
    end
    local id = GetUnitTypeId(u)
    local entries = tbl[id]
    if entries == nil then
        return false
    end
    for _, entry in ipairs(entries) do
        if GetRandomInt(1, entry.chance or 4) == 1 then
            _castAbility(u, entry, nil, nil)
            break
        end
    end
    return true
end

---@param u unit
---@param pi integer
function AiDispatchAttacked(u, pi)
    local race = AiRaceOf(pi)
    if race ~= nil then
        if race.attackedData ~= nil and AiRunAttacked(u, pi, race) then
            return
        end
        if race.attacked ~= nil then
            race.attacked(u)
        end
    end
end

---@param u unit
---@param def table
---@return boolean
function AiRunGetLvl(u, def)
    local tbl = def.getLvlData
    if tbl == nil then
        return false
    end
    local id = GetUnitTypeId(u)
    local cfg = tbl[id]
    if cfg == nil then
        return false
    end
    local lvl = GetHeroLevel(u)
    if lvl == 6 or lvl == 10 then
        SelectHeroSkill(u, cfg.ult or 0)
    elseif cfg.skills ~= nil then
        local i = GetRandomInt(1, #cfg.skills)
        SelectHeroSkill(u, cfg.skills[i])
    end
    return true
end

---@param u unit
---@param pi integer
function AiDispatchGetLvl(u, pi)
    local race = AiRaceOf(pi)
    if race ~= nil then
        if race.getLvlData ~= nil and AiRunGetLvl(u, race) then
            return
        end
        if race.getLvl ~= nil then
            race.getLvl(u)
        end
    end
end

---@param pi integer
---@param id integer
function AiDispatchUpgrade(pi, id)
    local race = AiRaceOf(pi)
    if race ~= nil and race.upgrade ~= nil then
        race.upgrade(pi, id)
    end
end
