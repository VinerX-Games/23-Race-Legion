-- ============================================================
-- Core: Safe Init + Error Catching for WC3 Lua
-- Must be FIRST in war3map.lua
-- ============================================================
-- Global error collector (shown on screen at game start)
_G.InitErrors = {}
_G.InitFatal = nil
_G.ProbeLogFile = "23Race_probe_log.pld"
_G.ProbeLogLines = {}
_G.ProbeLogFlushEnabled = false
_G.BridgeSyncPrefix = "23RaceCmd"
_G.BridgeManifestFile = "23race_cmd_manifest.pld"
_G.BridgeCommandFilePrefix = "23race_cmd_"
_G.BridgeCarrierAbilityId = FourCC('ANav')
_G.BridgeCarrierTooltipLevel = 0
_G.BridgeCarrierBaseline = nil
_G.BridgeManifestCount = nil
_G.BridgeManifestRequested = false
_G.BridgeNextLoadSequence = 1
_G.BridgeCommands = {}
_G.BridgeElapsed = 0.0
_G.BridgeTickInterval = 0.25
_G.BridgeDispatchCommand = nil
_G.BridgePollTimer = nil
_G.BridgeDebugTicks = 0
_G.BridgeDebugMaxTicks = 20
local function probeLogSanitize(message)
    local text = tostring(message)
    text = text:gsub("[\r\n]", " | ")
    text = text:gsub('"', "'")
    return text
end
function ProbeLogWrite(message)
    local lines = ProbeLogLines
    lines[#lines + 1] = probeLogSanitize(message)
    if #lines > 300 then
        table.remove(lines, 1)
    end
    if not ProbeLogFlushEnabled then
        return
    end
    pcall(function()
        PreloadGenClear()
        PreloadGenStart()
        for i = 1, #lines do
            Preload(lines[i])
        end
        PreloadGenEnd(ProbeLogFile)
    end)
end
function ProbeLogEnableFlush()
    ProbeLogFlushEnabled = true
    ProbeLogWrite("[LOG] flush-enabled")
end
function ProbeStep(label, fn)
    ProbeLogWrite("[STEP] " .. label .. " :: begin")
    local ok, result = pcall(fn)
    if ok then
        ProbeLogWrite("[STEP] " .. label .. " :: ok")
        return result
    end
    ProbeLogWrite("[STEP] " .. label .. " :: error :: " .. tostring(result))
    error(result, 0)
end
local function bridgeSplit(text, separator)
    local parts = {}
    local start = 1
    local sep_len = string.len(separator)
    while true do
        local pos = string.find(text, separator, start, true)
        if pos == nil then
            parts[#parts + 1] = string.sub(text, start)
            break
        end
        parts[#parts + 1] = string.sub(text, start, pos - 1)
        start = pos + sep_len
    end
    return parts
end
local function bridgeCommandFilename(sequence)
    return string.format("%s%04d.pld", BridgeCommandFilePrefix, sequence)
end
function BridgeQueueCommand(sequence, at_seconds, op, arg)
    if BridgeCommands[sequence] ~= nil then
        ProbeLogWrite("[BRIDGE] duplicate seq=" .. tostring(sequence))
        return
    end
    BridgeCommands[sequence] = {
        sequence = sequence,
        at_seconds = at_seconds,
        op = op,
        arg = arg,
        done = false,
    }
    ProbeLogWrite("[BRIDGE] queued seq=" .. tostring(sequence) .. " at=" .. tostring(at_seconds) .. " op=" .. tostring(op) .. " arg=" .. tostring(arg))
end
function BridgeHandleSyncData(data)
    local parts = bridgeSplit(tostring(data), "|")
    local kind = parts[1]
    if kind == "manifest" then
        local count = tonumber(parts[2])
        if count == nil then
            ProbeLogWrite("[BRIDGE] bad manifest payload=" .. tostring(data))
            return
        end
        BridgeManifestCount = count
        ProbeLogWrite("[BRIDGE] manifest count=" .. tostring(count))
        return
    end
    if kind == "cmd" then
        local sequence = tonumber(parts[2])
        local at_seconds = tonumber(parts[3])
        local op = parts[4]
        local arg = parts[5]
        if sequence == nil or at_seconds == nil or op == nil or op == "" then
            ProbeLogWrite("[BRIDGE] bad cmd payload=" .. tostring(data))
            return
        end
        BridgeQueueCommand(sequence, at_seconds, op, arg)
        return
    end
    ProbeLogWrite("[BRIDGE] unknown payload=" .. tostring(data))
end
function BridgeConsumePayloadFromFile(path)
    local baseline = BridgeCarrierBaseline
    if baseline == nil then
        baseline = BlzGetAbilityTooltip(BridgeCarrierAbilityId, BridgeCarrierTooltipLevel)
        BridgeCarrierBaseline = baseline
        ProbeLogWrite("[BRIDGE] baseline='" .. tostring(baseline) .. "'")
    end
    local preload_ok, preload_err = pcall(function()
        Preloader(path)
    end)
    if not preload_ok then
        ProbeLogWrite("[BRIDGE] preloader-error file=" .. tostring(path) .. " err=" .. tostring(preload_err))
    end
    local current_value = BlzGetAbilityTooltip(BridgeCarrierAbilityId, BridgeCarrierTooltipLevel)
    if current_value == nil or current_value == baseline then
        return false
    end
    BlzSetAbilityTooltip(BridgeCarrierAbilityId, baseline, BridgeCarrierTooltipLevel)
    ProbeLogWrite("[BRIDGE] payload file=" .. tostring(path) .. " data=" .. tostring(current_value))
    BridgeHandleSyncData(current_value)
    return true
end
function BridgeRequestManifest()
    if not BridgeManifestRequested then
        BridgeManifestRequested = true
        ProbeLogWrite("[BRIDGE] request manifest")
    end
    BridgeConsumePayloadFromFile(BridgeManifestFile)
end
function BridgeRequestNextCommand()
    if BridgeManifestCount == nil or BridgeNextLoadSequence > BridgeManifestCount then
        return
    end
    local filename = bridgeCommandFilename(BridgeNextLoadSequence)
    if BridgeConsumePayloadFromFile(filename) then
        ProbeLogWrite("[BRIDGE] loaded file=" .. filename)
        BridgeNextLoadSequence = BridgeNextLoadSequence + 1
    else
        ProbeLogWrite("[BRIDGE] waiting file=" .. filename)
    end
end
function BridgeTick()
    BridgeElapsed = BridgeElapsed + BridgeTickInterval
    BridgeDebugTicks = BridgeDebugTicks + 1
    if BridgeDebugTicks <= BridgeDebugMaxTicks then
        ProbeLogWrite("[BRIDGE] tick #" .. tostring(BridgeDebugTicks) .. " elapsed=" .. tostring(BridgeElapsed))
    end
    if BridgeManifestCount == nil then
        BridgeRequestManifest()
    elseif BridgeNextLoadSequence <= BridgeManifestCount then
        BridgeRequestNextCommand()
    end
    for sequence, command in pairs(BridgeCommands) do
        if not command.done and BridgeElapsed >= command.at_seconds then
            command.done = true
            if type(BridgeDispatchCommand) ~= "function" then
                ProbeLogWrite("[BRIDGE] dispatcher missing seq=" .. tostring(sequence))
            else
                local ok, err = pcall(BridgeDispatchCommand, command.op, command.arg, sequence)
                if ok then
                    ProbeLogWrite("[BRIDGE] ok seq=" .. tostring(sequence) .. " op=" .. tostring(command.op))
                else
                    ProbeLogWrite("[BRIDGE] error seq=" .. tostring(sequence) .. " op=" .. tostring(command.op) .. " :: " .. tostring(err))
                end
            end
        end
    end
end
function BridgeStart()
    ProbeLogWrite("[BRIDGE] start (chat mode)")
end
function SetupBridgeChat()
    local trigger = CreateTrigger()
    for i = 0, 23 do
        TriggerRegisterPlayerChatEvent(trigger, Player(i), "-bridge:", false)
    end
    TriggerAddAction(trigger, function()
        local text = GetEventPlayerChatString()
        local rest = string.sub(text, 9)
        local sep = string.find(rest, ":", 1, true)
        if sep == nil then
            ProbeLogWrite("[BRIDGE] bad chat cmd=" .. tostring(text))
            return
        end
        local op = string.sub(rest, 1, sep - 1)
        local arg = string.sub(rest, sep + 1)
        ProbeLogWrite("[BRIDGE] chat op=" .. tostring(op) .. " arg=" .. tostring(arg))
        if type(BridgeDispatchCommand) == "function" then
            local ok, err = pcall(BridgeDispatchCommand, op, arg, 0)
            if ok then
                ProbeLogWrite("[BRIDGE] ok op=" .. tostring(op))
                DisplayTimedTextToPlayer(GetTriggerPlayer(), 0, 0, 5.00, "|cff00ff00[BRIDGE] ok: " .. op .. "|r")
            else
                ProbeLogWrite("[BRIDGE] error op=" .. tostring(op) .. " :: " .. tostring(err))
                DisplayTimedTextToPlayer(GetTriggerPlayer(), 0, 0, 10.00, "|cffff0000[BRIDGE] error: " .. tostring(err) .. "|r")
            end
        else
            ProbeLogWrite("[BRIDGE] dispatcher missing")
        end
    end)
end
function SetupCodexPingChat()
    local trigger = CreateTrigger()
    for i = 0, 23 do
        TriggerRegisterPlayerChatEvent(trigger, Player(i), "-codexping", true)
    end
    TriggerAddAction(trigger, function()
        local player_name = GetPlayerName(GetTriggerPlayer())
        local chat_text = GetEventPlayerChatString()
        ProbeLogWrite("[PING] player=" .. tostring(player_name) .. " text=" .. tostring(chat_text))
        DisplayTimedTextToPlayer(GetTriggerPlayer(), 0, 0, 10.00, "Codex ping OK: " .. tostring(chat_text))
    end)
end
-- ============================================================
-- Safe callback wrapper (debug.traceback disabled in WC3)
-- ============================================================
local function safeCall(fn, label)
    return function(...)
        local ok, err = pcall(fn, ...)
        if not ok then
            local msg = label .. ": " .. tostring(err)
            InitErrors[#InitErrors + 1] = msg
            InitFatal = InitFatal or msg
            ProbeLogWrite("[CALLBACK-ERR] " .. msg)
        end
    end
end
-- ============================================================
-- Patch print() -> screen after game starts
-- ============================================================
local _origPrint = print
print = function(...)
    local parts = {}
    for i = 1, select("#", ...) do
        local v = select(i, ...)
        if v == nil then parts[#parts+1] = "nil"
        elseif type(v) == "table" then parts[#parts+1] = "{tbl}"
        elseif type(v) == "boolean" then parts[#parts+1] = (v and "true" or "false")
        else parts[#parts+1] = tostring(v) end
    end
    local msg = table.concat(parts, " ")
    _origPrint(msg)
    pcall(function()
        if MarkGameStarted and MarkGameStarted() then
            DisplayTimedTextToPlayer(Player(0), 0, 0, 60, msg)
        end
    end)
end
-- ============================================================
-- Wrap natives that accept callbacks
-- ============================================================
local _orig = {}
local function wrap(name, wrapper)
    _orig[name] = _G[name]
    _G[name] = wrapper
end
wrap("TriggerAddAction", function(t, fn)
    return _orig.TriggerAddAction(t, safeCall(fn, "TriggerAction"))
end)
wrap("TriggerAddCondition", function(t, condFn)
    if type(condFn) == "function" then
        return _orig.TriggerAddCondition(t, Condition(safeCall(condFn, "TriggerCondition")))
    end
    return _orig.TriggerAddCondition(t, condFn)
end)
wrap("TimerStart", function(timer, timeout, periodic, fn)
    if type(fn) == "function" then
        return _orig.TimerStart(timer, timeout, periodic, safeCall(fn, "Timer"))
    end
    return _orig.TimerStart(timer, timeout, periodic, fn)
end)
wrap("ForGroup", function(g, fn)
    return _orig.ForGroup(g, safeCall(fn, "ForGroup"))
end)
wrap("ForForce", function(f, fn)
    return _orig.ForForce(f, safeCall(fn, "ForForce"))
end)
wrap("EnumDestructablesInRect", function(r, filter, fn)
    return _orig.EnumDestructablesInRect(r, filter, safeCall(fn, "EnumDestr"))
end)
wrap("EnumItemsInRect", function(r, filter, fn)
    return _orig.EnumItemsInRect(r, filter, safeCall(fn, "EnumItems"))
end)
-- ============================================================
-- Init queue + MarkGameStarted error display
-- ============================================================
OnInit = { _queue = {} }
function OnInit.fn(fn, label)
    OnInit._queue[#OnInit._queue + 1] = {fn = fn, label = label or "?"}
end
function OnInit._run()
    local total, failed = #OnInit._queue, 0
    print("[INIT] Running " .. total .. " deferred steps...")
    ProbeLogWrite("[INIT] queue-size=" .. total)
    for i, entry in ipairs(OnInit._queue) do
        ProbeLogWrite("[INIT] begin #" .. i .. " " .. entry.label)
        local ok, err = pcall(entry.fn)
        if not ok then
            failed = failed + 1
            local msg = "[INIT] Step " .. i .. " [" .. entry.label .. "]: " .. tostring(err)
            InitErrors[#InitErrors + 1] = msg
            InitFatal = InitFatal or msg
            ProbeLogWrite("[INIT] error #" .. i .. " " .. entry.label .. " :: " .. tostring(err))
        else
            ProbeLogWrite("[INIT] ok #" .. i .. " " .. entry.label)
        end
    end
    print("[INIT] Done: " .. failed .. "/" .. total .. " failed")
    ProbeLogWrite("[INIT] done failed=" .. failed .. "/" .. total)
end
-- Show errors when game starts
do
    local _MarkGameStarted = MarkGameStarted or function() end
    MarkGameStarted = function()
        _MarkGameStarted()
        if InitFatal then
            ProbeLogWrite("[INIT] fatal :: " .. tostring(InitFatal))
            DisplayTimedTextToPlayer(Player(0), 0, 0, 15,
                "|cffffcc00=== INIT ERRORS (" .. #InitErrors .. ") ===")
            for _, msg in ipairs(InitErrors) do
                DisplayTimedTextToPlayer(Player(0), 0, 0, 120,
                    "|cffff0000" .. msg:sub(1, 200) .. "|r")
            end
        else
            ProbeLogWrite("[INIT] ok :: no errors")
            DisplayTimedTextToPlayer(Player(0), 0, 0, 10,
                "|cff00ff00[OK] Init: no errors|r")
        end
    end
end
print("[CORE] Framework loaded")
ProbeLogWrite("[BOOT] Framework loaded v2-bridge-fix")
JASS_MAX_ARRAY_SIZE = 32768 -- vJASS constant, required by SanctifiedEnchantment hash ops
