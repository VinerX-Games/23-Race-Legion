-- R5c: critical fix — make AiFindFreeWorker pick idle workers from buildersT even with non-expired claim.
-- The claim loop: TryBuildWithType stamps a new claim every tick → claim never expires → worker stuck.
-- With Fix 1 (no-yank of channeling workers), the claim guard in AiFindFreeWorker is redundant:
-- if order==0, the worker is truly idle and should be used.

AiFindFreeWorker = function(pi)
    local function alive(u)
        return u ~= nil and GetUnitState(u, UNIT_STATE_LIFE) > 0.405
    end
    local grp = udg_Ai_builders[pi]
    if grp ~= nil then
        local sz = BlzGroupGetSize(grp)
        for i = 0, sz - 1 do
            local u = BlzGroupUnitAt(grp, i)
            if alive(u) then return u end
        end
    end
    local grpT = udg_Ai_buildersT[pi]
    if grpT ~= nil then
        local sz = BlzGroupGetSize(grpT)
        for i = 0, sz - 1 do
            local u = BlzGroupUnitAt(grpT, i)
            -- Any idle worker in buildersT is available — claim guard is redundant
            -- now that AiRecycleBuilders no longer yanks channeling workers.
            if alive(u) and GetUnitCurrentOrder(u) == 0 then return u end
        end
    end
    local grpH = udg_Ai_harvest[pi]
    if grpH ~= nil then
        local sz = BlzGroupGetSize(grpH)
        for i = 0, sz - 1 do
            local u = BlzGroupUnitAt(grpH, i)
            if alive(u) then return u end
        end
    end
    return nil
end

return "R5c: AiFindFreeWorker — idle buildersT always available (claim check removed)"
