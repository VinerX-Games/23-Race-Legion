-- ============================================================
-- 23 Race Legion - Lua Rewrite
-- output/tables.lua — Hashtable replacements
-- ============================================================
-- All vJASS hashtables replaced with native Lua tables.
-- GetHandleId() keys become tostring() for Lua table keys.

--- Global_Hash replacement (used by SanctifiedEnchantment + stack template)
--- Key pattern: parent = GetHandleId(h), child = 10000 + JASS_MAX_ARRAY_SIZE * Key + i
G.Global_Hash = {}

--- AiData replacement (AI unit count tracking)
--- Key pattern: parent = playerId, child = unitId → count
G.AiData = {}

--- Hash replacement (timed abilities, effects, TotalProduction)
--- Key pattern: parent = GetHandleId(timer), child = small int (1,2,3...) → value
G.Hash = {}

--- CommonHash replacement (army tier config per player)
G.CommonHash = {}

-- ============================================================
-- AiData operations (from LIBRARY_LibDifferentAiStuff)
-- ============================================================

function getAiCount(pi, id)
    return (G.AiData[pi] and G.AiData[pi][id]) or 0
end

function aiHasUnit(pi, id)
    return getAiCount(pi, id) > 0
end

function NumberAdd(pi, id)
    if not G.AiData[pi] then G.AiData[pi] = {} end
    local count = (G.AiData[pi][id] or 0) + 1
    G.AiData[pi][id] = count
end

function NumberRem(pi, id)
    if not G.AiData[pi] then G.AiData[pi] = {} end
    local count = math.max((G.AiData[pi][id] or 0) - 1, 0)
    G.AiData[pi][id] = count
end

function NumberReset(pi, id)
    if G.AiData[pi] then G.AiData[pi][id] = 0 end
end

function NumberResetAll(pi)
    G.AiData[pi] = {}
end

-- ============================================================
-- Hash operations (timed ability/effects)
-- ============================================================

--- Save unit to hash by timer handle id
function HashSaveUnitHandle(timer, key, unit)
    local id = tostring(GetHandleId(timer))
    if not G.Hash[id] then G.Hash[id] = {} end
    G.Hash[id][key] = unit
end

--- Load unit from hash by timer handle id
function HashLoadUnitHandle(timer, key)
    local id = tostring(GetHandleId(timer))
    if G.Hash[id] then return G.Hash[id][key] end
    return nil
end

--- Save integer to hash
function HashSaveInteger(timer, key, value)
    local id = tostring(GetHandleId(timer))
    if not G.Hash[id] then G.Hash[id] = {} end
    G.Hash[id][key] = value
end

--- Load integer from hash
function HashLoadInteger(timer, key)
    local id = tostring(GetHandleId(timer))
    if G.Hash[id] then return G.Hash[id][key] or 0 end
    return 0
end

--- Save effect to hash
function HashSaveEffectHandle(timer, key, effect)
    local id = tostring(GetHandleId(timer))
    if not G.Hash[id] then G.Hash[id] = {} end
    G.Hash[id][key] = effect
end

--- Load effect from hash
function HashLoadEffectHandle(timer, key)
    local id = tostring(GetHandleId(timer))
    if G.Hash[id] then return G.Hash[id][key] end
    return nil
end

--- Flush child (clear timer's entries)
function HashFlushChild(timer)
    local id = tostring(GetHandleId(timer))
    G.Hash[id] = nil
end

-- ============================================================
-- Global_Hash operations (SanctifiedEnchantment)
-- ============================================================

JASS_MAX_ARRAY_SIZE = 32768

function GlobalHashSaveInteger(handle, key, value)
    local id = tostring(GetHandleId(handle))
    local keyStr = tostring(key)
    if not G.Global_Hash[id] then G.Global_Hash[id] = {} end
    G.Global_Hash[id][keyStr] = value
end

function GlobalHashLoadInteger(handle, key)
    local id = tostring(GetHandleId(handle))
    local keyStr = tostring(key)
    if G.Global_Hash[id] then return G.Global_Hash[id][keyStr] or 0 end
    return 0
end

-- ============================================================
-- CommonHash operations (army tier config)
-- ============================================================

function CommonHashSaveInteger(pi, key, value)
    if not G.CommonHash[pi] then G.CommonHash[pi] = {} end
    G.CommonHash[pi][key] = value
end

function CommonHashLoadInteger(pi, key)
    if G.CommonHash[pi] then return G.CommonHash[pi][key] or 0 end
    return 0
end
