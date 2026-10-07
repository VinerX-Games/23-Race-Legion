local first = AiBuildCapProbeSlot or 0
local last = AiBuildCapProbeSlot or 23
local checks, failures = 0, {}

for pi = first, last do
    if udg_AiControl[pi] then
        local race = AiRaceOf(pi)
        if race == nil or race.buildings == nil then
            failures[#failures + 1] = "pi=" .. pi .. " has no building table"
        else
            local caps = {}
            local list = race.buildings
            if list.seed ~= nil then
                caps[list.seed] = AiScaled(list.seedLimit or 1)
            end
            for _, row in ipairs(list) do
                local id = row[1]
                if id ~= nil then
                    local limit = AiScaled(row[2] or 1)
                    caps[id] = math.max(caps[id] or 0, limit)
                end
            end
            for id, limit in pairs(caps) do
                checks = checks + 1
                local count = AiCountBuildingsOfType(pi, id)
                if count > limit then
                    failures[#failures + 1] = "pi=" .. pi .. " " .. tostring(id)
                        .. " count=" .. count .. " limit=" .. limit
                end
            end
        end
    end
end

if #failures > 0 then error("AI_BUILD_CAPS failed: " .. table.concat(failures, "; ")) end
return "AI_BUILD_CAPS passed checks=" .. checks
