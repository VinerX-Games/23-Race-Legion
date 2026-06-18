-- HOTFIX: Fix continent detection + prevent bots walking across oceans
-- FIX 1: AiContinentOf — Nord checked BEFORE EK (overlap resolves to Northrend)
-- FIX 2: AiObjScore — capital continent (not army), unreachable ocean penalty

do
    local _cont = AiContinentOf
    function AiContinentOf(x, y)
        if RectContainsCoords(gg_rct_Nord, x, y) or RectContainsCoords(gg_rct_NordNotKalim, x, y) then
            return "Northrend"
        end
        if RectContainsCoords(gg_rct_Kalim, x, y) then
            return "Kalimdor"  -- NordNotKalim already covered above
        end
        if (RectContainsCoords(gg_rct_EastenKingdoms, x, y) or RectContainsCoords(gg_rct_VknotOut, x, y))
           and not (RectContainsCoords(gg_rct_OkeaniaNoVk, x, y) or RectContainsCoords(gg_rct_KillDalaran, x, y)) then
            return "EasternKingdoms"
        end
        if RectContainsCoords(gg_rct_Pandaria, x, y) then return "Pandaria" end
        if (RectContainsCoords(gg_rct_Outland, x, y) or RectContainsCoords(gg_rct_OutNoVk, x, y))
           and not RectContainsCoords(gg_rct_VknotOut, x, y) then
            return "Outland"
        end
        if RectContainsCoords(gg_rct_BrokenIsles, x, y) then return "BrokenIsles" end
        if RectContainsCoords(gg_rct_Argus, x, y) then return "Argus" end
        local subzones = {
            {"Azgel",gg_rct_Azgel},{"Ankirag",gg_rct_Ankirag},{"BlackMountain",gg_rct_BlackMountain},
            {"Orgrimmar",gg_rct_Orgrimmar},{"DeadMines",gg_rct_DeadMines},{"Uldum",gg_rct_Uldum},
            {"Undercity",gg_rct_Undercity},{"Maradon",gg_rct_Maradon},{"Naxramas",gg_rct_Naxramas},
            {"EasternDungeons",gg_rct_EasternDungeons},{"EmeraldDream",gg_rct_EmeraldDream},
        }
        for _,sz in ipairs(subzones) do
            if sz[2] and RectContainsCoords(sz[2],x,y) then return sz[1] end
        end
        return nil
    end

    local _score = AiObjScore
    function AiObjScore(pi, wm, o)
        local cfg = AiBrainCfg(pi)
        local w = cfg.weights or AiBrainDefaults.weights
        local kindBase = (w.kind and w.kind[o.kind]) or 0
        local dx = (wm.cx or 0) - o.x
        local dy = (wm.cy or 0) - o.y
        local dist = math.max(SquareRoot(dx*dx + dy*dy), 100)

        local race = AiRaceOf(pi)
        local isAmphib = race and race.continentalNaga
        local canFly = race and race.canFly
        local capX = (wm.capX ~= nil and wm.capX) or wm.cx or 0
        local capY = (wm.capY ~= nil and wm.capY) or wm.cy or 0
        local capCont = AiContinentOf(capX, capY)
        local objCont = AiContinentOf(o.x, o.y)
        local diffCont = (capCont ~= nil and objCont ~= nil and capCont ~= objCont)

        local waterPenalty = 1.0
        if diffCont and not isAmphib and not canFly then
            local route = AiPortalRoute(capCont, objCont)
            waterPenalty = (route ~= nil) and 0.05 or 0.0001
        end

        if o.kind == "capture" then
            return (kindBase + (w.value or 1)*o.value + 8000/dist) * waterPenalty
        end
        local armyBoost = 1 + math.min((wm.armyCount or 0)/30, 3)
        local armyPush = (wm.armyCount or 0)*20
        return (kindBase*armyBoost + armyPush + (w.value or 1)*o.value - (w.dist or 0.002)*dist) * waterPenalty
    end

    ProbeLogWrite("[HOTFIX] Continent: Nord-first + capCont scoring + unreachable=0.0001")
end

-- Verify
return string.format("Scarlet cap=%s KulTiras=%s",
    tostring(AiContinentOf(7584, 26016)),
    tostring(AiContinentOf(-5472, 25184)))
