-- ====================================================================
-- Portal/continent graph probe (run IN-GAME via the live bridge).
--   cd "C:\Games\23 Race"
--   python agent_bridge.py exec --file "23-Race-Legion/ai_portal_graph_probe.lua"
-- Returns a one-line edge summary; full per-portal detail goes to the probe log
-- under the [PORTGRAPH] tag (enable display with chat `-log on:PORTGRAPH`).
--
-- It walks every unit on the playable map, treats a unit as a portal if it is a
-- known portal type OR a structure with a non-trivial waygate destination, maps
-- the portal's own position and its waygate destination to a continent (same rect
-- tests ProcessContinentalStuff uses), and aggregates continent->continent edges.
-- Use the printed graph to bake a static AiPortalGraph table later. Extend
-- PORTAL_TYPES / CONT below if the discovery list flags missing ids/zones.
-- ====================================================================

-- Continents in macro-classification priority (mirrors ProcessContinentalStuff:
-- Kalim, EK, Nord, Pandaria, Outland, BrokenIsles, Argus, then dungeons/sub-zones).
local CONT = {
    { "Kalimdor",       gg_rct_Kalim },
    { "EasternKingdoms", gg_rct_EastenKingdoms },
    { "Northrend",      gg_rct_Nord },
    { "Pandaria",       gg_rct_Pandaria },
    { "Outland",        gg_rct_Outland },
    { "BrokenIsles",    gg_rct_BrokenIsles },
    { "Argus",          gg_rct_Argus },
    { "Azgel",          gg_rct_Azgel },
    { "Ankirag",        gg_rct_Ankirag },
    -- finer sub-zones / dungeons (optional graph nodes)
    { "BlackMountain",  gg_rct_BlackMountain },
    { "Orgrimmar",      gg_rct_Orgrimmar },
    { "Uldum",          gg_rct_Uldum },
    { "Undercity",      gg_rct_Undercity },
    { "Maradon",        gg_rct_Maradon },
    { "DeadMines",      gg_rct_DeadMines },
    { "Naxramas",       gg_rct_Naxramas },
    { "EasternDungeons", gg_rct_EasternDungeons },
    { "EmeraldDream",    gg_rct_EmeraldDream },
}

-- Known portal unit types (dark portal n006, inter-continent gates n003, water
-- portals n01D, emerald portals n01Y). Add more if the [PORTGRAPH][unknown] log
-- reveals other structure types acting as waygates.
local PORTAL_TYPES = { FourCC('n003'), FourCC('n006'), FourCC('n01D'), FourCC('n01Y') }
local ptset = {}
for _, id in ipairs(PORTAL_TYPES) do ptset[id] = true end

local function contAt(x, y)
    for _, c in ipairs(CONT) do
        if c[2] ~= nil and RectContainsCoords(c[2], x, y) then return c[1] end
    end
    return "?"
end

local g = CreateGroup()
GroupEnumUnitsInRect(g, bj_mapInitialPlayableArea, nil)
local size = BlzGroupGetSize(g)

local edges = {}      -- "src->dst" -> count
local unknownTypes = {} -- typeId -> count (heuristic-detected portals not in ptset)
local unknownPts = {}  -- coords of portals whose src/dst continent is "?"
local lines = {}
local nPortals = 0

local i = 0
while i < size do
    local u = BlzGroupUnitAt(g, i)
    if u ~= nil then
        local id = GetUnitTypeId(u)
        local dx = WaygateGetDestinationX(u)
        local dy = WaygateGetDestinationY(u)
        local known = ptset[id]
        local heuristic = IsUnitType(u, UNIT_TYPE_STRUCTURE) and (dx ~= 0.0 or dy ~= 0.0)
        if known or heuristic then
            local sx, sy = GetUnitX(u), GetUnitY(u)
            local src = contAt(sx, sy)
            local dst = contAt(dx, dy)
            local key = src .. "->" .. dst
            edges[key] = (edges[key] or 0) + 1
            nPortals = nPortals + 1
            if (src == "?" or dst == "?") and #unknownPts < 24 then
                unknownPts[#unknownPts + 1] = (src == "?" and ("S(" .. tostring(R2I(sx)) .. "," .. tostring(R2I(sy)) .. ")") or "")
                    .. (dst == "?" and ("D(" .. tostring(R2I(dx)) .. "," .. tostring(R2I(dy)) .. ")") or "")
                    .. "t" .. tostring(id)
            end
            if not known then
                unknownTypes[id] = (unknownTypes[id] or 0) + 1
            end
            lines[#lines + 1] = src .. "->" .. dst
                .. " type=" .. tostring(id)
                .. " at(" .. tostring(R2I(sx)) .. "," .. tostring(R2I(sy)) .. ")"
                .. " dst(" .. tostring(R2I(dx)) .. "," .. tostring(R2I(dy)) .. ")"
        end
    end
    i = i + 1
end
DestroyGroup(g)

table.sort(lines)
for _, l in ipairs(lines) do
    ProbeLogWrite("[PORTGRAPH] " .. l)
end
for id, c in pairs(unknownTypes) do
    ProbeLogWrite("[PORTGRAPH][unknown] heuristic-portal type=" .. tostring(id) .. " count=" .. tostring(c))
end

local out = {}
for k, c in pairs(edges) do
    out[#out + 1] = k .. "=" .. tostring(c)
end
table.sort(out)
local res = "portals=" .. tostring(nPortals) .. " | edges: " .. table.concat(out, "  ")
ProbeLogWrite("[PORTGRAPH] SUMMARY " .. res)
return res .. " || unknown: " .. table.concat(unknownPts, " ")
