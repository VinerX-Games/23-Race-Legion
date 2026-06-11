function AiFindProdBuilding(pi, bldType)
    local grp = udg_Ai_buildings[pi]
    if grp == nil then return nil end
    local sz = BlzGroupGetSize(grp)
    local best, bestPct = nil, -1.0
    for i = 0, sz - 1 do
        local u = BlzGroupUnitAt(grp, i)
        if u ~= nil and GetUnitTypeId(u) == bldType
            and GetUnitState(u, UNIT_STATE_LIFE) > 0.405 then
            local pct = GetUnitStatePercent(u, UNIT_STATE_LIFE, UNIT_STATE_MAX_LIFE)
            if pct >= 99.0 then return u end
            if pct > bestPct then best = u; bestPct = pct end
        end
    end
    return best
end
return "AiFindProdBuilding hot-patched"
