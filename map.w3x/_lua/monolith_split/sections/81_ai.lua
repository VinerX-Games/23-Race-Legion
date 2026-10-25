AiRaces = AiRaces or {}
AiRaceTokens = AiRaceTokens or {}
AiRaceOrder = AiRaceOrder or {}
g_AiOrdered = {}

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
    return race == nil or race.usesWaterPoint
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
    tArray[0] = 0
    if list.seed ~= nil and AiCountBuildingOrders(pi, list.seed) < (list.seedLimit or 1) then
        AddBuilding(list.seed, 1)
    end
    local rows = {}
    for _, row in ipairs(list) do
        rows[#rows + 1] = row
    end
    table.sort(rows, function(a, b) return a[1] < b[1] end)
    for _, row in ipairs(rows) do
        local gateOk = true
        if row.gate ~= nil then
            local g = def.gates and def.gates[row.gate]
            gateOk = (g == nil) or g(pi)
        end
        if gateOk and AiCountBuildingOrders(pi, row[1]) < row[2] then
            AddBuilding(row[1], row[3])
        end
    end
    if tArray[0] == 0 then
        return 0
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
AiUnitCap = AiUnitCap or 325

---@param id integer
---@param pi integer
---@param u unit
---@param def table
---@return boolean
function AiRunProduction(id, pi, u, def)
    local prod = def.production
    if not prod then return false end
    -- Global cap: stop training when live army+navy exceeds limit
    if (AiData[pi].wm and AiData[pi].wm.armyCount or 0) + ((udg_Ai_navy[pi] and BlzGroupGetSize(udg_Ai_navy[pi])) or 0) >= AiUnitCap then
        return false
    end
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
                if row.limit then
                    if getAiCount(pi, pick) >= row.limit then goto continue end
                    local key = pi * 1000000 + pick
                    if g_AiOrdered[key] then goto continue end
                end
                AddUnit(pick, row.weight or 1)
            end
        else
            local uid = row[1]
            if uid ~= nil and uid ~= 0 then
                if row.limit then
                    if getAiCount(pi, uid) >= row.limit then goto continue end
                    local key = pi * 1000000 + uid
                    if g_AiOrdered[key] then goto continue end
                end
                AddUnit(uid, row[2] or 1)
            end
        end
        ::continue::
    end
    if tArray[0] > 0 then
        -- P2: steer toward def.compTarget when AiSmartProduce is on; else random.
        local picked
        if AiSmartProduce and def.compTarget ~= nil then
            picked = AiPickByComposition(pi, def)
        end
        if picked == nil then
            picked = tArray[GetRandomInt(1, tArray[0])]
        end
        IssueImmediateOrderById(u, picked)
        g_AiOrdered[pi * 1000000 + picked] = true
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
    if i >= 25 then
        local econTier = MathRound(i / 60)
        local currentTier = GetPlayerTechCount(p, FourCC('R03Q'), false)
        if econTier > currentTier and econTier <= 2 then
            SetPlayerTechResearched(p, FourCC('R03Q'), econTier)
        end
    end
    -- Grade prereq unlock: most races' weapon/armor upgrades were cloned from a vanilla
    -- tech tree and still carry requires = the vanilla tier hall (Keep/Stronghold/Halls
    -- of the Dead/Tree of Ages, etc.) — buildings these custom races never build, so the
    -- upgrade can NEVER be researched and Grades[pi] sticks at 0. The custom race's own
    -- tier buildings already satisfy the higher upgrade levels; only the vanilla level-1
    -- gate blocks it. Grant the vanilla tier prereqs (all four base races) as pure
    -- tech-gate satisfiers — no building is created — so the cloned upgrades unlock at
    -- the matching eco tier. Harmless for races whose upgrades don't reference them.
    local function grantTech(code)
        if GetPlayerTechCount(p, code, false) < 1 then SetPlayerTechResearched(p, code, 1) end
    end
    -- tier 1 (always): Town Hall / Great Hall / Necropolis / Tree of Life
    grantTech(FourCC('htow')); grantTech(FourCC('ogre')); grantTech(FourCC('unpl')); grantTech(FourCC('etol'))
    if i >= 25 then  -- tier 2: Keep / Stronghold / Halls of the Dead / Tree of Ages
        grantTech(FourCC('hkee')); grantTech(FourCC('ostr')); grantTech(FourCC('unp1')); grantTech(FourCC('etoa'))
    end
    if i >= 55 then  -- tier 3: Castle / Fortress / Black Citadel / Tree of Eternity
        grantTech(FourCC('hcas')); grantTech(FourCC('ofrt')); grantTech(FourCC('unp2')); grantTech(FourCC('etoe'))
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
    AiData[pi].researchEconomy = i
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

function AiResearchEconomy(pi, p, race)
    local score = 0
    local weights = race.ecoWeights or {}
    local group = CreateGroup()
    GroupEnumUnitsOfPlayer(group, p, nil)
    for index = 0, BlzGroupGetSize(group) - 1 do
        local u = BlzGroupUnitAt(group, index)
        if IsUnitInGroup(u, udg_ZahvatBuildings) then
            score = score + 8
        else
            score = score + (weights[GetUnitTypeId(u)] or 0)
        end
    end
    DestroyGroup(group)
    AiData[pi].researchEconomy = score
    return score
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
    if AiCombatProtected(u) then return true end
    if tbl.pre ~= nil then
        for _, pre in ipairs(tbl.pre) do
            if GetRandomInt(1, pre.chance or 1) == 1 then
                if pre.terrain == "water" and not IsTerrainPathable(GetUnitX(u), GetUnitY(u), PATHING_TYPE_WALKABILITY) then
                    if pre.notAbil == nil or GetUnitAbilityLevel(u, pre.notAbil) == 0 then
                        local accepted = _castAbility(u, pre, nil, nil)
                        if accepted and pre.ret then
                            return true
                        end
                    end
                end
            end
        end
    end
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
                    if _castAbility(u, entry, target, p) then return true end
                end
            else
                if _castAbility(u, entry, target, p) then return true end
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
    if u == nil or GetUnitTypeId(u) == 0 or GetUnitState(u, UNIT_STATE_LIFE) <= 0.405 then return false end
    if AiCombatProtected(u) then return false end
    if entry.needAbil ~= nil and GetUnitAbilityLevel(u, entry.needAbil) == 0 then return false end
    local tp = entry.type or "target"
    if tp == "draenei_vow" then
        return AiCombatOrderResult(u, DraeneiCombat.AiVow(u))
    elseif tp == "draenei_idol" then
        return AiCombatOrderResult(u, DraeneiCombat.AiIdol(u))
    elseif tp == "silitid_cocoon" then
        return AiCombatOrderResult(u, SilitidRescue.AiCast(u))
    elseif tp == "bear_grip" then
        return AiCombatOrderResult(u, BearGrip.AiCast(u, target))
    elseif tp == "naga_harpoon" then
        return AiCombatOrderResult(u, NagaCombat.AiHarpoon(u))
    elseif tp == "worgen_seed" then
        return AiCombatOrderResult(u, WorgenDruid.AiSeed(u))
    elseif tp == "worgen_curse" then
        return AiCombatOrderResult(u, WorgenDruid.AiCurse(u, target))
    elseif tp == "worgen_moon" then
        return AiCombatOrderResult(u, WorgenDruid.AiMoon(u))
    elseif tp == "immediate" then
        if entry.orderId ~= nil then
            return AiCombatOrderResult(u, IssueImmediateOrderById(u, entry.orderId))
        end
        return AiCombatOrderResult(u, IssueImmediateOrder(u, entry.order))
    elseif tp == "heal" then
        -- Own group and explicit owner: casting can reenter other native callbacks.
        local group = CreateGroup()
        GroupEnumUnitsInRange(group, GetUnitX(u), GetUnitY(u), entry.allyRange or 550, nil)
        local best, lowest = nil, 100
        for i = 0, BlzGroupGetSize(group) - 1 do
            local ally = BlzGroupUnitAt(group, i)
            if ally ~= nil and GetUnitTypeId(ally) ~= 0
                and GetUnitState(ally, UNIT_STATE_LIFE) > 0.405
                and IsUnitAlly(ally, GetOwningPlayer(u))
                and not IsUnitType(ally, UNIT_TYPE_STRUCTURE)
                and (not entry.organicOnly or (not IsUnitType(ally, UNIT_TYPE_MECHANICAL)
                    and not IsUnitType(ally, UNIT_TYPE_WARD) and not IsUnitIllusion(ally)))
                and (entry.minLostHP == nil or GetUnitState(ally, UNIT_STATE_MAX_LIFE)
                    - GetUnitState(ally, UNIT_STATE_LIFE) >= entry.minLostHP) then
                local hp = GetUnitStatePercent(ally, UNIT_STATE_LIFE, UNIT_STATE_MAX_LIFE)
                if hp < lowest then best, lowest = ally, hp end
            end
        end
        DestroyGroup(group)
        if best ~= nil then return AiCombatOrderResult(u, IssueTargetOrder(u, entry.order, best)) end
    elseif tp == "point" and target ~= nil then
        return AiCombatOrderResult(u, IssuePointOrder(u, entry.order, GetUnitX(target), GetUnitY(target)))
    elseif tp == "ally" then
        return AiCombatOrderResult(u, IssueTargetOrder(u, entry.order, u))
    elseif tp == "self" then
        return AiCombatOrderResult(u, IssuePointOrder(u, entry.order, GetUnitX(u), GetUnitY(u)))
    elseif target ~= nil then
        return AiCombatOrderResult(u, IssueTargetOrder(u, entry.order, target))
    end
    return false
end

function _castAbilityEntry(u, id, target, entries)
    for _, entry in ipairs(entries) do
        if entry.needAbil ~= nil and GetUnitAbilityLevel(u, entry.needAbil) == 0 then
            -- skip
        elseif GetRandomInt(1, entry.chance or 4) == 1 then
            if _castAbility(u, entry, target, nil) then return true end
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
            if _castAbility(u, entry, nil, nil) then break end
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
    -- Retry eligible skills until every saved point is spent; a rejected skill
    -- must not strand points until the next level event.
    for _ = 1, GetHeroSkillPoints(u) do
        local spent = false
        local function learn(skill)
            if skill == nil or skill == 0 then return false end
            local before = GetHeroSkillPoints(u)
            SelectHeroSkill(u, skill)
            return GetHeroSkillPoints(u) < before
        end
        if GetHeroLevel(u) >= 6 then spent = learn(cfg.ult) end
        if not spent and cfg.skills ~= nil and #cfg.skills > 0 then
            local first = GetRandomInt(1, #cfg.skills)
            for offset = 0, #cfg.skills - 1 do
                if learn(cfg.skills[(first + offset - 1) % #cfg.skills + 1]) then
                    spent = true
                    break
                end
            end
        end
        if not spent then break end
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

-- Combat state belongs to the bot; spell events distinguish accepted orders
-- from effects that actually fired. No local-player reads or wall-clock timing.
function AiCombatState(u)
    local pi = GetPlayerId(GetOwningPlayer(u))
    AiData[pi] = AiData[pi] or {}
    local d = AiData[pi]
    d.combat = d.combat or {}
    d.combat[u] = d.combat[u] or {}
    return d.combat[u], d
end

function AiCombatProtected(u)
    if u == nil then return false end
    local state, d = AiCombatState(u)
    return state.retreat == true or state.casting == true
        or (state.pending ~= nil and (d.combatTick or 0) < state.pending)
end

function AiCombatOrderResult(u, accepted)
    local state, d = AiCombatState(u)
    d.castOrders = (d.castOrders or 0) + 1
    if accepted then
        d.castAccepted = (d.castAccepted or 0) + 1
        if d.wm ~= nil then state.pending = (d.combatTick or 0) + 2 end
    end
    return accepted == true
end

function AiCombatSpellEvent()
    local u = GetTriggerUnit()
    local pi = GetPlayerId(GetOwningPlayer(u))
    if not udg_AiControl[pi] then return end
    local state, d = AiCombatState(u)
    local event = GetTriggerEventId()
    if event == EVENT_PLAYER_UNIT_SPELL_CHANNEL then
        state.casting = true
    elseif event == EVENT_PLAYER_UNIT_SPELL_EFFECT then
        d.castEffects = d.castEffects or {}
        local id = GetSpellAbilityId()
        d.castEffects[id] = (d.castEffects[id] or 0) + 1
    elseif event == EVENT_PLAYER_UNIT_SPELL_ENDCAST then
        state.casting, state.pending = nil, nil
    elseif event == EVENT_PLAYER_UNIT_DEATH then
        d.combat[u] = nil
    end
end

function AiCombatInit()
    local t = CreateTrigger()
    for _, event in ipairs({EVENT_PLAYER_UNIT_SPELL_CHANNEL, EVENT_PLAYER_UNIT_SPELL_EFFECT,
        EVENT_PLAYER_UNIT_SPELL_ENDCAST, EVENT_PLAYER_UNIT_DEATH}) do
        TriggerRegisterAnyUnitEventBJ(t, event)
    end
    TriggerAddAction(t, AiCombatSpellEvent)
end

function AiHeroCombatTick(pi, u, wm, race)
    local state = AiCombatState(u)
    if race ~= nil then AiRunGetLvl(u, race) end
    local hp = GetUnitStatePercent(u, UNIT_STATE_LIFE, UNIT_STATE_MAX_LIFE)
    if not state.casting then
        for slot = 0, UnitInventorySize(u) - 1 do
            local item = UnitItemInSlot(u, slot)
            if item ~= nil then
                local id = GetItemTypeId(item)
                local heal = id == FourCC('phea') or id == FourCC('pghe')
                local mana = id == FourCC('pman') or id == FourCC('pgma')
                local shield = id == FourCC('pnvu') or id == FourCC('pnvl')
                if (heal and hp < 55) or (shield and hp < 25)
                    or (mana and GetUnitStatePercent(u, UNIT_STATE_MANA, UNIT_STATE_MAX_MANA) < 25) then
                    if UnitUseItem(u, item) then break end
                end
            end
        end
    end
    hp = GetUnitStatePercent(u, UNIT_STATE_LIFE, UNIT_STATE_MAX_LIFE)
    if hp < 30 then state.retreat = true end
    if hp >= 70 then state.retreat = nil end
    if state.retreat and wm.capX ~= nil and wm.capY ~= nil then
        -- Survival may interrupt a channel, but army commands cannot recall this hero.
        IssuePointOrder(u, "move", wm.capX, wm.capY)
    end
end

function AiCombatTick(pi, wm, race)
    local d = AiData[pi]
    d.combatTick = (d.combatTick or 0) + 1
    local army = udg_Ai_army[pi]
    if army == nil then return end
    local size = BlzGroupGetSize(army)
    for i = 0, size - 1 do
        local u = BlzGroupUnitAt(army, i)
        if u ~= nil and GetUnitTypeId(u) ~= 0 and GetUnitState(u, UNIT_STATE_LIFE) > 0.405
            and IsUnitType(u, UNIT_TYPE_HERO) then AiHeroCombatTick(pi, u, wm, race) end
    end
    -- Bounded round-robin sensing also reaches support units which never attack.
    if size == 0 or race == nil or race.attackerData == nil then return end
    local cursor = d.combatCursor or 0
    for offset = 0, math.min(size, 8) - 1 do
        local u = BlzGroupUnitAt(army, (cursor + offset) % size)
        if u ~= nil and GetUnitTypeId(u) ~= 0 and GetUnitState(u, UNIT_STATE_LIFE) > 0.405
            and not AiCombatProtected(u)
            and (race.attackerData[GetUnitTypeId(u)] ~= nil
                or #race.attackerData > 0 or race.attackerData.post ~= nil) then
            local group = CreateGroup()
            GroupEnumUnitsInRange(group, GetUnitX(u), GetUnitY(u), 800, nil)
            local target, score = nil, -1
            for j = 0, BlzGroupGetSize(group) - 1 do
                local enemy = BlzGroupUnitAt(group, j)
                if enemy ~= nil and GetUnitTypeId(enemy) ~= 0
                    and GetUnitState(enemy, UNIT_STATE_LIFE) > 0.405
                    and IsUnitEnemy(enemy, Player(pi)) and IsUnitVisible(enemy, Player(pi))
                    and not IsUnitType(enemy, UNIT_TYPE_STRUCTURE) then
                    local value = 100 - GetUnitStatePercent(enemy, UNIT_STATE_LIFE, UNIT_STATE_MAX_LIFE)
                    if IsUnitType(enemy, UNIT_TYPE_HERO) then value = value + 40 end
                    if GetUnitState(enemy, UNIT_STATE_MAX_MANA) > 0 then value = value + 20 end
                    if value > score then target, score = enemy, value end
                end
            end
            DestroyGroup(group)
            if target ~= nil then
                AiRunAttacker(GetUnitTypeId(u), u, target, Player(pi), race)
            else
                -- Wounded allies still need healing after the last enemy falls.
                for _, entry in ipairs(race.attackerData[GetUnitTypeId(u)] or {}) do
                    if entry.type == "heal" and GetRandomInt(1, entry.chance or 5) == 1
                        and _castAbility(u, entry, nil, Player(pi)) then break end
                end
            end
        end
    end
    d.combatCursor = (cursor + math.min(size, 8)) % size
end
