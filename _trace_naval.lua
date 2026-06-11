local pi = 11
local cap = playerCapital[pi]
local wm = { capX = GetUnitX(cap), capY = GetUnitY(cap), tick = AiBrainTickCounter or 0 }
local race = AiRaces[AiRace[pi]]
-- free worker BEFORE
local before = AiFindFreeWorker(pi)
BrainNavalDecision(pi, wm, race)
-- find the worker we just flagged
local flagged = nil
for u, t in pairs(AiNavalBuildUntil) do
    if t and t > (AiBrainTickCounter or 0) then flagged = u end
end
local msg = "freeWorkerExisted=" .. tostring(before ~= nil)
if flagged then
    local t = GetUnitTypeId(flagged)
    msg = msg .. string.format(" flaggedWorker type=%s ord=%d x=%d y=%d alive=%s inBT=%s",
        string.char((t>>24)&255,(t>>16)&255,(t>>8)&255,t&255),
        GetUnitCurrentOrder(flagged), math.floor(GetUnitX(flagged)), math.floor(GetUnitY(flagged)),
        tostring(GetUnitState(flagged, UNIT_STATE_LIFE) > 0.405),
        tostring(IsUnitInGroup(flagged, udg_Ai_buildersT[pi])))
else
    msg = msg .. " NO flagged worker (TryBuildWithType returned false / no worker)"
end
return msg
