-- Pause ALL army AI (brain + legacy) by emptying the round-robin list PlayerArmy reads.
-- Saves the pi values to gSavedBrainList so it can be restored with _ai_resume.lua.
gSavedBrainList = {}
for i, v in ipairs(AiBrainBotList) do gSavedBrainList[i] = v end
for i = #AiBrainBotList, 1, -1 do AiBrainBotList[i] = nil end
AiBrainCursor = 0
-- Also stop in-flight orders so idle workers are fully yours to command.
return "AI paused: " .. tostring(#gSavedBrainList) .. " bots removed from tick loop (saved for resume)"
