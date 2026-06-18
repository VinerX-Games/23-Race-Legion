-- Hot-redefine AiContinentOf with EK-last ordering, then re-check pi=11.
function AiContinentOf(x, y)
    if RectContainsCoords(gg_rct_Kalim, x, y) and not RectContainsCoords(gg_rct_NordNotKalim, x, y) then return "Kalimdor" end
    if RectContainsCoords(gg_rct_Nord, x, y) or RectContainsCoords(gg_rct_NordNotKalim, x, y) then return "Northrend" end
    if RectContainsCoords(gg_rct_Pandaria, x, y) then return "Pandaria" end
    if (RectContainsCoords(gg_rct_Outland, x, y) or RectContainsCoords(gg_rct_OutNoVk, x, y)) and not RectContainsCoords(gg_rct_VknotOut, x, y) then return "Outland" end
    if RectContainsCoords(gg_rct_BrokenIsles, x, y) then return "BrokenIsles" end
    if RectContainsCoords(gg_rct_Argus, x, y) then return "Argus" end
    if (RectContainsCoords(gg_rct_EastenKingdoms, x, y) or RectContainsCoords(gg_rct_VknotOut, x, y)) and not (RectContainsCoords(gg_rct_OkeaniaNoVk, x, y) or RectContainsCoords(gg_rct_KillDalaran, x, y)) then return "EasternKingdoms" end
    local subzones = {
        { "Azgel", gg_rct_Azgel }, { "Ankirag", gg_rct_Ankirag }, { "BlackMountain", gg_rct_BlackMountain },
        { "Orgrimmar", gg_rct_Orgrimmar }, { "DeadMines", gg_rct_DeadMines }, { "Uldum", gg_rct_Uldum },
        { "Undercity", gg_rct_Undercity }, { "Maradon", gg_rct_Maradon }, { "Naxramas", gg_rct_Naxramas },
        { "EasternDungeons", gg_rct_EasternDungeons }, { "EmeraldDream", gg_rct_EmeraldDream },
    }
    for _, sz in ipairs(subzones) do
        if sz[2] ~= nil and RectContainsCoords(sz[2], x, y) then return sz[1] end
    end
    return nil
end
local wm = AiData[11].wm
local army = wm.cx and AiContinentOf(wm.cx, wm.cy) or "?"
local cap = wm.capX and AiContinentOf(wm.capX, wm.capY) or "?"
local f = AiBrainPickFocus(11, wm)
local fc = f and AiContinentOf(f.x, f.y) or "nil"
local rt = (army ~= "?" and fc ~= "nil") and AiPortalRoute(army, fc) or nil
return "pi11 NOW: armyCont=" .. army .. " capCont=" .. cap .. " focus@" .. fc
    .. " route(" .. army .. "->" .. tostring(fc) .. ")=" .. (rt and (#rt .. " hops") or "nil")
