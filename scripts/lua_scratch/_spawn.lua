local roster = {
    "silitids", "silitids", "silitids", "silitids",
    "alliance", "alliance", "alliance", "alliance",
    "goblins", "gnomes", "horde", "cult",
    "goblins", "gnomes", "horde",
}
local n = 0
for i = 1, #roster do
    createAiPlayer(i, roster[i])
    n = n + 1
end
return "spawned " .. n .. " bots; AiBrainBotList len=" .. #AiBrainBotList
