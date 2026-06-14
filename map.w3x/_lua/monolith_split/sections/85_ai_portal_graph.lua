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
    -- Main continents — MUST mirror ProcessContinentalStuff's order (93_continental_main.lua):
    -- Kalim, Nord, Pandaria, Outland, BrokenIsles, Argus, THEN EasternKingdoms LAST. The EK
    -- rect is huge and overlaps Outland/Nord/Pandaria, so it must be the lowest-priority main
    -- or it steals their overlap zones (live bug: a Horde army physically in Outland read as
    -- "EasternKingdoms" → portal routing broke, army walked direct). The gg_rct_VknotOut
    -- exclusion in Outland ("восточки НЕ запределье") still hands the EK-overlap strip to EK.
    if RectContainsCoords(gg_rct_Kalim, x, y) and not RectContainsCoords(gg_rct_NordNotKalim, x, y) then
        return "Kalimdor"
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
    if (RectContainsCoords(gg_rct_EastenKingdoms, x, y) or RectContainsCoords(gg_rct_VknotOut, x, y)) and not (RectContainsCoords(gg_rct_OkeaniaNoVk, x, y) or RectContainsCoords(gg_rct_KillDalaran, x, y)) then
        return "EasternKingdoms"
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
    -- Fallback: a point inside a main rect but carved out by an EXCLUSION (e.g. an enemy
    -- capital sitting in the OkeaniaNoVk ocean-strip of EK) must NOT return nil — a nil
    -- objective continent makes portal routing give up and walk direct (live: Outland Horde
    -- had its target read nil => route(Outland->nil)=nil => marched out on foot instead of
    -- taking the Outland->EK portal). Exclusions only resolve overlap PRIORITY above; here we
    -- ignore them so any point within a continent's rect still names that continent.
    if RectContainsCoords(gg_rct_Kalim, x, y) then return "Kalimdor" end
    if RectContainsCoords(gg_rct_Nord, x, y) then return "Northrend" end
    if RectContainsCoords(gg_rct_Pandaria, x, y) then return "Pandaria" end
    if RectContainsCoords(gg_rct_Outland, x, y) then return "Outland" end
    if RectContainsCoords(gg_rct_BrokenIsles, x, y) then return "BrokenIsles" end
    if RectContainsCoords(gg_rct_Argus, x, y) then return "Argus" end
    if RectContainsCoords(gg_rct_EastenKingdoms, x, y) then return "EasternKingdoms" end
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

-- Water portal (naval-only) — excluded from land routing, matching the baked graph.
AiPortalWaterType = FourCC('n01D')

-- The old hardcoded AiPortalTypeSet {n003,n006,n01Y,n01Z} MISSED the real land portals
-- between several continents (live scan found n065/n00W = BrokenIsles<->Argus, n01B =
-- Kalimdor<->Argus, n04O, n001 — none were in the set), so AiFindPortal returned nil for
-- BrokenIsles->Argus and a cross-portal squad fell through to walking into the sea. We now
-- detect ANY waygate (non-zero destination) by its destination, excluding water portals —
-- future-proof against new portal unit types.
AiPortalTypeSet = nil  -- deprecated; kept nil so any stale reference fails loudly

function AiBuildPortalCache()
    if AiPortalCacheBuilt then return end
    AiPortalCacheBuilt = true
    AiPortalScanGroup = AiPortalScanGroup or CreateGroup()
    GroupEnumUnitsInRect(AiPortalScanGroup, bj_mapInitialPlayableArea, nil)
    local size = BlzGroupGetSize(AiPortalScanGroup)
    local i = 0
    while i < size do
        local u = BlzGroupUnitAt(AiPortalScanGroup, i)
        if u ~= nil and GetUnitTypeId(u) ~= AiPortalWaterType then
            local dx = WaygateGetDestinationX(u)
            local dy = WaygateGetDestinationY(u)
            if dx ~= 0.0 or dy ~= 0.0 then  -- it's an actual waygate with a destination
                local sx, sy = GetUnitX(u), GetUnitY(u)
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

-- Curated shipyard spots: exact coords where shipyards were hand-placed on open
-- water during live testing (guaranteed buildable). Keyed by continent so a bot
-- only gets spots on its OWN landmass (worker can path there). Deduped @600u.
AiCuratedNavalSpots = {
    Kalimdor = { {-15680,-10816}, {-15936,-9728}, {-20736,-16640}, {-29184,2432}, {-15168,-9024}, {-28416,-4160}, {-27904,-5376}, {-14272,-5312}, {-25856,-16768}, {-26368,-16000}, {-14720,5888}, {-13312,-4608}, {-13696,-5120}, {-16000,768}, {-14208,5376}, {-13376,1088}, {-13440,1792}, {-13760,9536}, {-28160,15040}, {-27392,14848} },
    EasternKingdoms = { {23936,29440}, {22080,19840}, {25408,29184}, {22720,19648}, {29248,10816}, {23360,29888}, {24512,29056}, {28352,21376}, {29184,13568}, {7552,7360}, {8256,22848}, {28224,22016}, {8000,8256}, {9024,21632}, {8896,24768}, {8576,22144}, {12800,-9472}, {27712,-9536}, {13632,-6336}, {15744,-17024}, {12352,-10944}, {26304,4544}, {15360,-14400}, {9664,6144}, {18944,832}, {25088,-16192}, {25600,3840}, {14336,-13312}, {18560,6144}, {17984,5440}, {27840,-5568}, {29888,-128}, {11200,15488}, {10560,14912}, {15616,-16384}, {29376,1024}, {13312,-7104}, {29696,-832}, {17408,-17536}, {18368,-17472}, {11136,10176}, {20928,2688}, {20160,1344}, {28352,-3584}, {27200,-6464}, {30144,-3456}, {26112,-15872}, {29824,-2624}, {19392,5504}, {9536,6848}, {26688,-15616}, {27392,-13120}, {14720,-13824}, {19008,64}, {14656,16192}, {16256,-16448}, {21696,17792}, {12480,-10176}, {26432,5376}, {28160,-10176}, {13824,16320}, {21056,18240} },
    Northrend = { {-768,29440}, {-8320,29696}, {-4672,20672}, {-3072,20672}, {-8896,29376}, {-3840,20608}, {-16256,22080}, {-16256,20160}, {-16384,20864}, {-12224,17856}, {-11584,18368}, {-12928,18240}, {-11264,18944}, {-16192,21440}, {-13376,25664} },
    Pandaria = { {-10112,-13632}, {-7680,-10880}, {-7744,-10240}, {-3328,-10880}, {-1216,-12416}, {1152,-20608}, {-2816,-22912}, {-8768,-20160}, {-896,-14720}, {-9152,-17024}, {-832,-13376}, {-2240,-11072}, {640,-22272}, {-640,-12736}, {-4352,-22656}, {-10112,-10624}, {-3840,-22208}, {-2112,-22912}, {-10048,-9920}, {-2944,-11456}, {64,-21952}, {1664,-20928} },
    BrokenIsles = { {256,11584}, {768,12032}, {1856,12608}, {2432,1344}, {-1088,3520}, {1024,1728} },
}

-- ====================================================================
-- WEB-PORTAL MASS-TELEPORT (sell-based network), used by the AI for BIG armies.
-- A walk-on waygate funnels one unit at a time and a large blob collision-jams
-- on the gate tile (observed: 173-unit Horde army stuck at the Dark Portal, 0
-- crossings). The map's real mass-movement is the sell network: buying h0P0 at a
-- portal shop makes it cast "web" -> a per-portal SPELL_FINISH trigger calls
-- TeleportUnits(portal, destRect, R), moving everything within R to destRect.
-- We reuse the SAME (portal -> destRect, radius) data but teleport ONLY the bot's
-- own eligible army (SetUnitPosition), so we don't drag neutrals/enemies and we
-- avoid the map TeleportUnits' bare-function boolexpr fault. See [[portal-sell-teleport]].
--
-- Spec rows are {portalGlobalSuffix, destRectName, radius}. Resolved lazily once
-- (preplaced units/rects are static) into AiWebPortals with src/dst continents.
AiWebPortalSpecs = {
    {"n003_0044","UndecityOutTop",800}, {"n003_0046","UndecityOutBot",800}, {"n003_0050","UndercityInR",800},
    {"n003_0051","UndercityInTop",800}, {"n003_0516","OrgrimmarTopIn",800}, {"n003_0514","OrgrimmarBotIn",800},
    {"n003_0517","OrgrimmarTopOut",800}, {"n003_0518","OrgrimmarBotOut",800}, {"n003_0521","DeadminersOut",800},
    {"n003_0420","DeadminerIn",800}, {"n003_0943","DarkM_4",1200}, {"n003_0942","DarkM_3",1200},
    {"n003_0940","DarkM_1",1200}, {"n003_0941","DarkM_2",1200}, {"n01Y_0889","ED_1",750},
    {"n01Y_1012","ED_1_B",750}, {"n01Y_0934","ED_2",750}, {"n01Y_1013","ED_2_b",750},
    {"n01Y_0896","ED_3",750}, {"n01Y_1014","ED_3_b",750}, {"n01Y_1015","ED_4_b",750},
    {"n01Y_0897","ED_4",750}, {"n01Z_1016","ED_5",750}, {"n01Z_1017","ED_5_B",750},
    {"n006_0023","DarkPortal1",1200}, {"n006_0438","DarkPortal2",1200}, {"n001_0845","Region_009",1200},
    {"n04O_0136","Region_010",1200}, {"n00W_0442","EKportalAlterac",1200}, {"n00W_0589","OutlandNagrand",1200},
    {"n00W_0446","Region_013",1200}, {"n001_0847","Region_014",1200}, {"n065_0125","ArgusShip",1200},
    {"n00W_0848","Broken_Island",1200}, {"n01B_0849","Region_017",1200}, {"n01B_0850","Region_018",1200},
    {"n003_0098","Nord_5",1200}, {"n003_0060","AzNer_5",650}, {"n003_0097","AzNer_2",1200},
    {"n003_1004","Nord4",1200}, {"n003_1002","Nord_1",1200}, {"n003_0995","AzNer1",1200},
    {"n01Y_0578","Teldrasil",1200}, {"n01Y_0580","Darnas",1200}, {"n003_0118","QtunIn",1200},
    {"n003_0117","QtunIn2",1200}, {"n003_0124","QtunOut",1200}, {"n003_0123","QtunOu2",1200},
    {"n003_0308","MarodonOut",900}, {"n003_0311","MarodonOut2",900}, {"n003_0305","MarodonIn",900},
    {"n003_0314","MarodonIn2",900}, {"n003_0025","GnomreganIn",1200}, {"n003_0018","GnomreganOut",1200},
    {"n003_0024","Stalgorn",1200}, {"n003_0019","StalgornOut",1200}, {"n003_0028","TrainIn",1200},
    {"n003_0149","TrainOut",1200}, {"n003_0021","GrimBatolOut",1200}, {"n003_0022","GrimBatolIn",1200},
    {"n003_0027","UldamanIn",1200}, {"n003_0020","UldamanOut",1200}, {"n003_0126","NaxOut",1200},
    {"n003_0588","DalaranOut",1200}, {"n060_0350","Silvermoon",1200}, {"n060_0287","QuelIsland",1200},
    {"n003_0090","TurtleOut",800},
}

AiWebPortals = nil          -- resolved cache: list of {unit,rect,x,y,radius,srcCont,dstCont}
AiWebPortalGraph = nil      -- adjacency over the WEB network: [srcCont][dstCont] = true
AiWebPortalCast = AiWebPortalCast or {}  -- [unit handle string] = tick of last teleport (cooldown)

function AiBuildWebPortalCache()
    if AiWebPortals ~= nil then return end
    AiWebPortals = {}
    AiWebPortalGraph = {}
    for _, spec in ipairs(AiWebPortalSpecs) do
        local u = _G["gg_unit_" .. spec[1]]
        local r = _G["gg_rct_" .. spec[2]]
        if u ~= nil and r ~= nil then
            local px, py = GetUnitX(u), GetUnitY(u)
            local sc = AiContinentOf(px, py)
            local dc = AiContinentOf(GetRectCenterX(r), GetRectCenterY(r))
            if sc ~= nil and dc ~= nil and sc ~= dc then
                AiWebPortals[#AiWebPortals + 1] = {
                    unit = u, rect = r, x = px, y = py,
                    radius = spec[3], srcCont = sc, dstCont = dc,
                }
                local nb = AiWebPortalGraph[sc]
                if nb == nil then nb = {}; AiWebPortalGraph[sc] = nb end
                nb[dc] = true
            end
        end
    end
    ProbeLogWrite("[WEBPORT] cache built: " .. tostring(#AiWebPortals) .. " cross-zone web-portals")
end

-- BFS over the WEB-portal network (NOT the waygate graph) so every hop is guaranteed
-- to have an actual web-portal we can fire. Returns the continent path {src,...,dst} or nil.
---@return table|nil
function AiWebRoute(src, dst)
    if src == nil or dst == nil then return nil end
    if src == dst then return { src } end
    AiBuildWebPortalCache()
    local q = { { node = src, path = { src } } }
    local visited = { [src] = true }
    local head = 1
    while head <= #q do
        local cur = q[head]; head = head + 1
        local nb = AiWebPortalGraph[cur.node]
        if nb ~= nil then
            for n, _ in pairs(nb) do
                if n == dst then
                    local p = {}
                    for _, v in ipairs(cur.path) do p[#p + 1] = v end
                    p[#p + 1] = dst
                    return p
                end
                if not visited[n] then
                    visited[n] = true
                    local np = {}
                    for _, v in ipairs(cur.path) do np[#np + 1] = v end
                    np[#np + 1] = n
                    q[#q + 1] = { node = n, path = np }
                end
            end
        end
    end
    return nil
end

-- Nearest web-portal on srcCont whose dest == dstCont, to (x,y). nil if none.
---@return table|nil
function AiFindWebPortal(srcCont, dstCont, x, y)
    AiBuildWebPortalCache()
    local best, bestd = nil, nil
    for _, wp in ipairs(AiWebPortals) do
        if wp.srcCont == srcCont and wp.dstCont == dstCont
           and GetUnitState(wp.unit, UNIT_STATE_LIFE) > 0.405 then
            local dx, dy = x - wp.x, y - wp.y
            local d = dx * dx + dy * dy
            if bestd == nil or d < bestd then best, bestd = wp, d end
        end
    end
    return best
end

-- Teleport ONLY player pi's eligible army units within `radius` of the portal into
-- `rect` (scattered). Skips structures, peons (harvesters), and waygate units. Caps
-- at 150 like the map's native. Returns count moved.
---@return integer
function AiPortalTeleport(pi, portal, rect, radius)
    local army = udg_Ai_army and udg_Ai_army[pi]
    if army == nil then return 0 end
    local px, py = GetUnitX(portal), GetUnitY(portal)
    local minx, maxx = GetRectMinX(rect), GetRectMaxX(rect)
    local miny, maxy = GetRectMinY(rect), GetRectMaxY(rect)
    local r2 = radius * radius
    local moved = 0
    local sz = BlzGroupGetSize(army)
    local i = 0
    while i < sz and moved < 150 do
        local u = BlzGroupUnitAt(army, i)
        i = i + 1
        if u ~= nil and GetUnitState(u, UNIT_STATE_LIFE) > 0.405
           and not IsUnitType(u, UNIT_TYPE_STRUCTURE)
           and not IsUnitType(u, UNIT_TYPE_PEON)
           and GetUnitAbilityLevel(u, FourCC('Awrp')) == 0 then
            local dx, dy = GetUnitX(u) - px, GetUnitY(u) - py
            if dx * dx + dy * dy <= r2 then
                SetUnitPosition(u, GetRandomReal(minx, maxx), GetRandomReal(miny, maxy))
                moved = moved + 1
            end
        end
    end
    return moved
end
