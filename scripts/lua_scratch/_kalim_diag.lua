-- Find brain bots with army in Kalimdor; report group health (size/nil/alive/dead).
local function groupStats(g)
    if g == nil then return 0, 0, 0, 0 end
    local sz = BlzGroupGetSize(g)
    local nilc, alive, dead = 0, 0, 0
    for i = 0, sz - 1 do
        local u = BlzGroupUnitAt(g, i)
        if u == nil then nilc = nilc + 1
        elseif GetUnitState(u, UNIT_STATE_LIFE) > 0.405 then alive = alive + 1
        else dead = dead + 1 end
    end
    return sz, nilc, alive, dead
end
local out = {}
for _, pi in ipairs(AiBrainBotList) do
    local wm = AiData[pi].wm
    local c = (wm and wm.cx) and (AiContinentOf(wm.cx, wm.cy) or "nil") or "?"
    if c == "Kalimdor" then
        local sz, nilc, alive, dead = groupStats(udg_Ai_army[pi])
        local hsz, hnil, halive = groupStats(udg_Ai_harvest[pi])
        out[#out + 1] = "P" .. pi .. " " .. tostring(AiRace[pi])
            .. " | ARMY size=" .. sz .. " nil=" .. nilc .. " alive=" .. alive .. " dead=" .. dead
            .. " | harvest size=" .. hsz .. " nil=" .. hnil .. " alive=" .. halive
            .. " | armyCount=" .. tostring(wm.armyCount)
    end
end
return #out > 0 and table.concat(out, "\n") or "no brain bots with army in Kalimdor"
