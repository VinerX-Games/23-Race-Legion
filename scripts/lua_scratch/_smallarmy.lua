-- Apply "small but strong" settings to the live game (bots already exist).
AiSizeScale  = 0.5
AiBotAuras   = { {FourCC('aib0'), 10}, {FourCC('aib1'), 10} }
AiBotHPMult  = 1.5
AiBotDmgMult = 1.5
AiMusterTimeout = 20

-- Handicaps are read at createAiPlayer (already ran), so apply directly to existing bots now.
local n = 0
for _, pi in ipairs(AiBrainBotList) do
    local p = Player(pi)
    SetPlayerHandicap(p, 1.5)
    if SetPlayerHandicapDamage ~= nil then SetPlayerHandicapDamage(p, 1.5) end
    n = n + 1
end
return "applied: AiSizeScale=0.5, auras lvl10, handicaps 1.5 to " .. n .. " bots | fsm=" .. tostring(AiSquadFsmEnabled)
