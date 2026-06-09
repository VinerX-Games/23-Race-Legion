-- ====================================================================
-- AiPortalGraph: static continent adjacency for inter-continent routing.
-- Baked from ai_portal_graph_probe.lua (73 portals, 37 directed edges).
-- Water portals (n01D) excluded. EmeraldDream nodes have no valid dst.
-- ====================================================================

AiPortalGraph = {
    Ankirag          = { Kalimdor = true },
    Argus            = { BrokenIsles = true, Kalimdor = true },
    Azgel            = { Kalimdor = true, Northrend = true },
    BlackMountain    = { EasternKingdoms = true },
    BrokenIsles      = { Argus = true },
    DeadMines        = { EasternKingdoms = true },
    EasternDungeons  = { EasternKingdoms = true },
    EasternKingdoms  = { BlackMountain = true, BrokenIsles = true, DeadMines = true,
                          EasternDungeons = true, Kalimdor = true, Outland = true,
                          Uldum = true, Undercity = true },
    EmeraldDream     = {},
    Kalimdor         = { Ankirag = true, Argus = true, Azgel = true,
                          EasternKingdoms = true, Maradon = true, Orgrimmar = true,
                          Outland = true },
    Maradon          = { Kalimdor = true },
    Naxramas         = { Northrend = true },
    Northrend        = { Azgel = true },
    Orgrimmar        = { Kalimdor = true },
    Outland          = { EasternKingdoms = true, Kalimdor = true },
    Uldum            = { EasternKingdoms = true },
    Undercity        = { EasternKingdoms = true },
}

-- Continent lookup rects — mirrors ProcessContinentalStuff priority order:
-- 1. Kalimdor (Kalim NOT NordNotKalim)
-- 2. EasternKingdoms (+dungeons) NOT OkeaniaNoVk/KillDalaran
-- 3. Northrend (+Azgel+NordNotKalim)
-- 4. Pandaria
-- 5. Outland (+OutNoVk) NOT VknotOut
-- 6. BrokenIsles
-- 7. Argus
-- Then sub-zone rects for finer classification (checked after main continents
-- so dungeons snap to parent-continent groups during routing when they touch).
AiContinentRects = {
    { "Kalimdor",       gg_rct_Kalim,           gg_rct_NordNotKalim },
    { "EasternKingdoms", gg_rct_EastenKingdoms,  gg_rct_OkeaniaNoVk, gg_rct_KillDalaran,
                         gg_rct_EasternDungeons, gg_rct_BlackMountain, gg_rct_VknotOut },
    { "Northrend",      gg_rct_Nord,             nil, nil, nil, nil, nil,
                         gg_rct_Azgel,           gg_rct_NordNotKalim },
    { "Pandaria",       gg_rct_Pandaria },
    { "Outland",        gg_rct_Outland,          gg_rct_VknotOut, nil, nil,
                         gg_rct_OutNoVk },
    { "BrokenIsles",    gg_rct_BrokenIsles },
    { "Argus",          gg_rct_Argus },
    { "Azgel",          gg_rct_Azgel },
    { "Ankirag",        gg_rct_Ankirag },
    { "BlackMountain",  gg_rct_BlackMountain },
    { "Orgrimmar",      gg_rct_Orgrimmar },
    { "Uldum",          gg_rct_Uldum },
    { "Undercity",      gg_rct_Undercity },
    { "Maradon",        gg_rct_Maradon },
    { "DeadMines",      gg_rct_DeadMines },
    { "Naxramas",       gg_rct_Naxramas },
    { "EasternDungeons", gg_rct_EasternDungeons },
    { "EmeraldDream",   gg_rct_EmeraldDream },
}

-- return 0: index of the last positive-or-nil rect arg (rect count varies per entry)
local function AiContinentRectCount(entry)
    local n = 0
    while n < 8 do
        local v = entry[n + 2]
        if v == nil then break end
        n = n + 1
    end
    return n
end

---@param x real
---@param y real
---@return string|nil continent name (main continents first, sub-zones for uncovered areas)
function AiContinentOf(x, y)
    -- Main continents (ProcessContinentalStuff priority order)
    if RectContainsCoords(gg_rct_Kalim, x, y) and not RectContainsCoords(gg_rct_NordNotKalim, x, y) then
        return "Kalimdor"
    end
    if (RectContainsCoords(gg_rct_EastenKingdoms, x, y) or RectContainsCoords(gg_rct_VknotOut, x, y)) and not (RectContainsCoords(gg_rct_OkeaniaNoVk, x, y) or RectContainsCoords(gg_rct_KillDalaran, x, y)) then
        return "EasternKingdoms"
    end
    if RectContainsCoords(gg_rct_Nord, x, y) or RectContainsCoords(gg_rct_NordNotKalim, x, y) then
        return "Northrend"
    end
    if RectContainsCoords(gg_rct_Pandaria, x, y) then
        return "Pandaria"
    end
    if (RectContainsCoords(gg_rct_Outland, x, y) or RectContainsCoords(gg_rct_OutNoVk, x, y)) and not RectContainsCoords(gg_rct_VknotOut, x, y) then
        return "Outland"
    end
    if RectContainsCoords(gg_rct_BrokenIsles, x, y) then
        return "BrokenIsles"
    end
    if RectContainsCoords(gg_rct_Argus, x, y) then
        return "Argus"
    end
    -- Sub-zones for areas NOT covered by main continental rects.
    -- Azgel (Nord's neighbour), dungeons etc. checked AFTER mains so inland
    -- sub-zones (Orgrimmar/Kalimdor etc.) stay as their parent continent.
    local subzones = {
        { "Azgel",          gg_rct_Azgel },
        { "Ankirag",        gg_rct_Ankirag },
        { "BlackMountain",  gg_rct_BlackMountain },
        { "Orgrimmar",      gg_rct_Orgrimmar },
        { "DeadMines",      gg_rct_DeadMines },
        { "Uldum",          gg_rct_Uldum },
        { "Undercity",      gg_rct_Undercity },
        { "Maradon",        gg_rct_Maradon },
        { "Naxramas",       gg_rct_Naxramas },
        { "EasternDungeons", gg_rct_EasternDungeons },
        { "EmeraldDream",   gg_rct_EmeraldDream },
    }
    for _, sz in ipairs(subzones) do
        if sz[2] ~= nil and RectContainsCoords(sz[2], x, y) then
            return sz[1]
        end
    end
    return nil
end

-- BFS shortest path from src continent to dst continent.
---@param src string
---@param dst string
---@return table|nil ordered list of continent names, or nil if unreachable
function AiPortalRoute(src, dst)
    if src == nil or dst == nil then return nil end
    if src == dst then return { src } end
    local q = { { node = src, path = { src } } }
    local visited = { [src] = true }
    local head = 1
    while head <= #q do
        local cur = q[head]
        head = head + 1
        local neighbors = AiPortalGraph[cur.node]
        if neighbors ~= nil then
            for nb, _ in pairs(neighbors) do
                if nb == dst then
                    local p = {}
                    for _, v in ipairs(cur.path) do p[#p + 1] = v end
                    p[#p + 1] = dst
                    return p
                end
                if not visited[nb] then
                    visited[nb] = true
                    local np = {}
                    for _, v in ipairs(cur.path) do np[#np + 1] = v end
                    np[#np + 1] = nb
                    q[#q + 1] = { node = nb, path = np }
                end
            end
        end
    end
    return nil
end

-- Lazy cache: (srcContinent, dstContinent) -> { portalUnit, ... }
AiPortalUnitCache = AiPortalUnitCache or {}
AiPortalCacheBuilt = AiPortalCacheBuilt or false

-- Portal unit type ids included in the cache
AiPortalTypeSet = {
    [FourCC('n003')] = true,
    [FourCC('n006')] = true,
    [FourCC('n01Y')] = true,
    [FourCC('n01Z')] = true,
}

function AiBuildPortalCache()
    if AiPortalCacheBuilt then return end
    AiPortalCacheBuilt = true
    AiPortalScanGroup = AiPortalScanGroup or CreateGroup()
    GroupEnumUnitsInRect(AiPortalScanGroup, bj_mapInitialPlayableArea, nil)
    local size = BlzGroupGetSize(AiPortalScanGroup)
    local i = 0
    while i < size do
        local u = BlzGroupUnitAt(AiPortalScanGroup, i)
        if u ~= nil then
            local id = GetUnitTypeId(u)
            if AiPortalTypeSet[id] then
                local sx, sy = GetUnitX(u), GetUnitY(u)
                local dx = WaygateGetDestinationX(u)
                local dy = WaygateGetDestinationY(u)
                local src = AiContinentOf(sx, sy)
                local dst = AiContinentOf(dx, dy)
                if src ~= nil and dst ~= nil and src ~= dst then
                    local key = src .. "\t" .. dst
                    local list = AiPortalUnitCache[key]
                    if list == nil then
                        list = {}
                        AiPortalUnitCache[key] = list
                    end
                    list[#list + 1] = u
                end
            end
        end
        i = i + 1
    end
    DestroyGroup(AiPortalScanGroup)
    local n = 0
    for _ in pairs(AiPortalUnitCache) do n = n + 1 end
    ProbeLogWrite("[PORTGRAPH] cache built: " .. tostring(n) .. " directed portal entries")
end

-- Find a portal unit on srcContinent whose waygate leads to dstContinent.
---@param srcContinent string
---@param dstContinent string
---@return unit|nil
function AiFindPortal(srcContinent, dstContinent)
    AiBuildPortalCache()
    local list = AiPortalUnitCache[srcContinent .. "\t" .. dstContinent]
    if list == nil or #list == 0 then return nil end
    for _, u in ipairs(list) do
        if WaygateIsActive(u) then return u end
    end
    return list[1]
end

-- Check if player has a TP-capable unit (mage/captured building) on a continent.
---@param pi integer
---@param continent string
---@return unit|nil
function AiFindMageOnContinent(pi, continent)
    local group = AiUnitsToPort[pi]
    if group == nil then return nil end
    local size = BlzGroupGetSize(group)
    local i = 0
    while i < size do
        local u = BlzGroupUnitAt(group, i)
        if u ~= nil and GetUnitState(u, UNIT_STATE_LIFE) > 0.405 then
            local cont = AiContinentOf(GetUnitX(u), GetUnitY(u))
            if cont == continent then
                return u
            end
        end
        i = i + 1
    end
    return nil
end
