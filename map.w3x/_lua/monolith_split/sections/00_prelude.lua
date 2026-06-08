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
_G.LogFilter = {}
_G.LogFilterAll = false
_G.BridgeSyncPrefix = "23RaceCmd"
_G.BridgeManifestFile = "23race_cmd_manifest.pld"
_G.BridgeCommandFilePrefix = "23race_cmd_"
_G.BridgeCarrierAbilityId = FourCC('AHbz')
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
_G.BridgeDebugMaxTicks = 0
_G.BridgeEvalEnabled = true
_G.BridgeEvalSyncPrefix = "23RaceEval"
_G.BridgeEvalSyncTrigger = nil
_G.BridgeEvalLoopPaused = false
_G.BridgeEvalChunks = {}
local function probeLogSanitize(message)
    local text = tostring(message)
    text = text:gsub("[\r\n]", " | ")
    text = text:gsub('"', "'")
    return text
end
local function logExtractTag(message)
    local tag = string.match(tostring(message), "^%[([A-Z][A-Z0-9%-]*)%]")
    return tag
end
function ProbeLogWrite(message)
    local lines = ProbeLogLines
    lines[#lines + 1] = probeLogSanitize(message)
    if #lines > 2000 then
        table.remove(lines, 1)
    end
    local allow = LogFilterAll
    if not allow then
        local tag = logExtractTag(message)
        if tag ~= nil then
            allow = LogFilter[tag]
        end
    end
    if allow then
        pcall(function()
            BJDebugMsg(tostring(message))
        end)
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
function LogEnable(tag)
    LogFilter[tag] = true
end
function LogDisable(tag)
    LogFilter[tag] = false
end
function LogToggle(tag)
    LogFilter[tag] = not LogFilter[tag]
end
function LogList()
    local parts = {}
    for tag, enabled in pairs(LogFilter) do
        parts[#parts + 1] = tag .. "=" .. tostring(enabled)
    end
    local msg = table.concat(parts, " ")
    ProbeLogWrite("[LOG] all=" .. tostring(LogFilterAll) .. " " .. msg)
    return msg
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
-- ============================================================
-- Live Lua eval channel (agent debug): run arbitrary Lua in the
-- running game and return the value. Crash-safe via hex payloads.
--   IN : sequential 23race_eval_NNNN.pld  -> eval|<seq>|<hex-lua>
--   OUT: fixed 23race_eval_out.pld         -> <seq>|<ok 0/1>|<hex-result>
--   SYNC: Player(0) reads .pld -> BlzSendSyncData -> all players execute
-- Driven from agent_bridge.py. See memory live-lua-eval-bridge.
-- ============================================================
function BridgeEvalSetupSync()
    if BridgeEvalSyncTrigger ~= nil then
        return
    end
    local trigger = CreateTrigger()
    BridgeEvalSyncTrigger = trigger
    for i = 0, 23 do
        BlzTriggerRegisterPlayerSyncEvent(trigger, Player(i), BridgeEvalSyncPrefix, false)
    end
    TriggerAddAction(trigger, function()
        local data = BlzGetTriggerSyncData()
        local parts = bridgeSplit(data, "|")
        if #parts < 5 or parts[1] ~= "eval" then
            ProbeLogWrite("[BRIDGE-SYNC] bad header parts=" .. tostring(#parts))
            return
        end
        local seq = tonumber(parts[2])
        local ci = tonumber(parts[3])
        local total = tonumber(parts[4])
        local hexchunk = parts[5] or ""
        if seq == nil or ci == nil or total == nil then
            ProbeLogWrite("[BRIDGE-SYNC] bad numbers")
            return
        end
        if total == 1 then
            ProbeLogWrite("[EVAL] sync-run seq=" .. tostring(seq) .. " bytes=" .. tostring(#hexchunk // 2))
            EvalRun(seq, EvalHexDec(hexchunk))
            return
        end
        local buf = BridgeEvalChunks[seq]
        if buf == nil then
            buf = { total = total, chunks = {}, received = 0, ts = BridgeElapsed }
            BridgeEvalChunks[seq] = buf
        end
        if buf.chunks[ci] ~= nil then
            return
        end
        buf.chunks[ci] = hexchunk
        buf.received = buf.received + 1
        ProbeLogWrite("[EVAL] chunk seq=" .. tostring(seq) .. " " .. tostring(ci) .. "/" .. tostring(total))
        if buf.received >= buf.total then
            local full = {}
            for j = 1, buf.total do
                full[#full + 1] = buf.chunks[j] or ""
            end
            local hex = table.concat(full)
            BridgeEvalChunks[seq] = nil
            ProbeLogWrite("[EVAL] sync-run assembled seq=" .. tostring(seq) .. " bytes=" .. tostring(#hex // 2))
            EvalRun(seq, EvalHexDec(hex))
        end
    end)
    ProbeLogWrite("[BRIDGE] eval-sync registered prefix=" .. tostring(BridgeEvalSyncPrefix) .. " chunked")
end
_G.EvalNextSeq = 1
_G.EvalOutFile = "23race_eval_out.pld"      -- legacy fixed outbox (kept for fallback)
_G.EvalOutPrefix = "23race_eval_out_"        -- per-seq outbox: <prefix>NNNN.pld
_G.EvalHbFile = "23race_eval_hb.pld"         -- heartbeat: tells agent the seq we await
_G.EvalInPrefix = "23race_eval_"
function EvalHexDec(s)
    local out = {}
    for i = 1, #s - 1, 2 do
        out[#out + 1] = string.char(tonumber(string.sub(s, i, i + 1), 16) or 0)
    end
    return table.concat(out)
end
function EvalHexEnc(s)
    local out = {}
    for i = 1, #s do
        out[#out + 1] = string.format("%02x", string.byte(s, i))
    end
    return table.concat(out)
end
function EvalSerialize(v, depth)
    local t = type(v)
    if v == nil then return "nil" end
    if t == "number" or t == "boolean" then return tostring(v) end
    if t == "string" then return v end
    if t == "table" then
        if depth <= 0 then return "{...}" end
        local parts, n = {}, 0
        for k, val in pairs(v) do
            n = n + 1
            if n > 40 then parts[#parts + 1] = "..."; break end
            parts[#parts + 1] = tostring(k) .. "=" .. EvalSerialize(val, depth - 1)
        end
        return "{" .. table.concat(parts, ", ") .. "}"
    end
    return t .. ": " .. tostring(v)
end
function EvalWriteResult(seq, ok, value)
    if GetPlayerId(GetLocalPlayer()) ~= 0 then
        return
    end
    -- WC3 truncates each Preload() string (~259 chars), so chunk the hex result
    -- across multiple lines: <seq>|<ok>|<idx>|<total>|<hexchunk>. Agent reassembles.
    local hex = EvalHexEnc(EvalSerialize(value, 5))
    local chunk = 200
    local total = #hex
    if total < 1 then total = 1 end
    total = math.ceil(total / chunk)
    if total < 1 then total = 1 end
    local okf = ok and "1" or "0"
    -- Per-seq outbox so a later result can never clobber an unread one.
    local outfile = string.format("%s%04d.pld", EvalOutPrefix, seq)
    pcall(function()
        PreloadGenClear()
        PreloadGenStart()
        for i = 1, total do
            local part = string.sub(hex, (i - 1) * chunk + 1, i * chunk)
            Preload(tostring(seq) .. "|" .. okf .. "|" .. i .. "|" .. total .. "|" .. part)
        end
        PreloadGenEnd(outfile)
    end)
    ProbeLogWrite("[EVAL] result seq=" .. tostring(seq) .. " ok=" .. tostring(ok) .. " chunks=" .. total)
end
-- Heartbeat: publish the inbox seq we're currently waiting for, so the agent
-- writes exactly that filename and the two seq counters can never drift apart.
function EvalWriteHeartbeat()
    if GetPlayerId(GetLocalPlayer()) ~= 0 then
        return
    end
    pcall(function()
        PreloadGenClear()
        PreloadGenStart()
        Preload("hb|" .. tostring(EvalNextSeq))
        PreloadGenEnd(EvalHbFile)
    end)
end
function EvalRun(seq, code)
    local chunk, cerr = load("return " .. code)
    if not chunk then chunk, cerr = load(code) end
    if not chunk then
        EvalWriteResult(seq, false, "compile error: " .. tostring(cerr))
        return
    end
    local ok, res = pcall(chunk)
    EvalWriteResult(seq, ok, res)
end
function BridgeConsumeEval()
    if GetPlayerId(GetLocalPlayer()) ~= 0 or not BridgeEvalEnabled then
        return
    end
    local baseline = BridgeCarrierBaseline
    if baseline == nil then
        baseline = BlzGetAbilityTooltip(BridgeCarrierAbilityId, BridgeCarrierTooltipLevel)
        BridgeCarrierBaseline = baseline
    end
    local path = string.format("%s%04d.pld", EvalInPrefix, EvalNextSeq)
    pcall(function() Preloader(path) end)
    local current = BlzGetAbilityTooltip(BridgeCarrierAbilityId, BridgeCarrierTooltipLevel)
    if current == nil or current == baseline then return end
    BlzSetAbilityTooltip(BridgeCarrierAbilityId, baseline, BridgeCarrierTooltipLevel)
    EvalNextSeq = EvalNextSeq + 1
    EvalWriteHeartbeat()  -- publish the new seq we now await
    ProbeLogWrite("[EVAL] loaded seq=" .. tostring(EvalNextSeq - 1) .. " file=" .. path)
end
function BridgeTick()
    if BridgeEvalEnabled and not BridgeEvalLoopPaused then
        pcall(BridgeConsumeEval)
    end
    BridgeElapsed = BridgeElapsed + BridgeTickInterval
    BridgeDebugTicks = BridgeDebugTicks + 1
    -- Re-publish heartbeat ~1s so a freshly-attached/reset agent re-syncs the seq.
    if BridgeEvalEnabled and BridgeDebugTicks % 4 == 0 then
        pcall(EvalWriteHeartbeat)
    end
    if BridgeDebugTicks <= BridgeDebugMaxTicks then
        ProbeLogWrite("[BRIDGE] tick #" .. tostring(BridgeDebugTicks) .. " elapsed=" .. tostring(BridgeElapsed))
    end
    local filename = bridgeCommandFilename(BridgeNextLoadSequence)
    if BridgeConsumePayloadFromFile(filename) then
        ProbeLogWrite("[BRIDGE] loaded file=" .. filename)
        BridgeNextLoadSequence = BridgeNextLoadSequence + 1
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
    for seq, buf in pairs(BridgeEvalChunks) do
        if BridgeElapsed - buf.ts > 30 then
            BridgeEvalChunks[seq] = nil
            ProbeLogWrite("[EVAL] stale chunk buffer dropped seq=" .. tostring(seq))
        end
    end
end
function BridgeStart()
    if BridgePollTimer ~= nil then
        return
    end
    -- Skip stale eval files from previous session: force-read current tooltip
    -- to flush any preloaded payload, then set it as the new baseline.
    -- After this, only NEW tooltip changes will be treated as fresh evals.
    local flushed = BlzGetAbilityTooltip(BridgeCarrierAbilityId, BridgeCarrierTooltipLevel)
    BlzSetAbilityTooltip(BridgeCarrierAbilityId, flushed, BridgeCarrierTooltipLevel)
    BridgeCarrierBaseline = flushed
    -- Disable pre-loaded command files; only live chat commands work
    BridgeManifestCount = 0
    BridgeNextLoadSequence = 999999
    local timer = CreateTimer()
    BridgePollTimer = timer
    ProbeLogWrite("[BRIDGE] start (live-only) baseline-len=" .. tostring(#flushed))
    BridgeEvalSetupSync()
    EvalWriteHeartbeat()  -- publish initial seq so the agent syncs from tick 0
    TimerStart(timer, BridgeTickInterval, true, BridgeTick)
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
        -- Eval toggle commands
        if op == "eval" then
            if arg == "on" then
                BridgeEvalEnabled = true
                ProbeLogWrite("[BRIDGE] eval enabled")
                DisplayTimedTextToPlayer(GetTriggerPlayer(), 0, 0, 5.00, "|cff00ff00[BRIDGE] eval ON|r")
            elseif arg == "off" then
                BridgeEvalEnabled = false
                ProbeLogWrite("[BRIDGE] eval disabled")
                DisplayTimedTextToPlayer(GetTriggerPlayer(), 0, 0, 5.00, "|cffff0000[BRIDGE] eval OFF|r")
            elseif arg == "toggle" then
                BridgeEvalEnabled = not BridgeEvalEnabled
                ProbeLogWrite("[BRIDGE] eval toggled to " .. tostring(BridgeEvalEnabled))
                DisplayTimedTextToPlayer(GetTriggerPlayer(), 0, 0, 5.00, "|cffffcc00[BRIDGE] eval " .. (BridgeEvalEnabled and "ON" or "OFF") .. "|r")
            elseif arg == "status" then
                local msg = "eval=" .. tostring(BridgeEvalEnabled) .. " loop=" .. tostring(not BridgeEvalLoopPaused)
                ProbeLogWrite("[BRIDGE] status " .. msg)
                DisplayTimedTextToPlayer(GetTriggerPlayer(), 0, 0, 8.00, "|cff00ff00[BRIDGE] " .. msg .. "|r")
            end
            return
        end
        -- Loop pause/resume
        if op == "loop" then
            if arg == "off" then
                BridgeEvalLoopPaused = true
                ProbeLogWrite("[BRIDGE] eval loop paused")
                DisplayTimedTextToPlayer(GetTriggerPlayer(), 0, 0, 5.00, "|cffff0000[BRIDGE] eval loop PAUSED|r")
            elseif arg == "on" then
                BridgeEvalLoopPaused = false
                -- NB: never rewind EvalNextSeq here — reusing a consumed filename
                -- hits WC3's Preloader name-cache. Heartbeat syncs the agent.
                ProbeLogWrite("[BRIDGE] eval loop resumed")
                DisplayTimedTextToPlayer(GetTriggerPlayer(), 0, 0, 5.00, "|cff00ff00[BRIDGE] eval loop ACTIVE|r")
            elseif arg == "toggle" then
                BridgeEvalLoopPaused = not BridgeEvalLoopPaused
                -- keep EvalNextSeq monotonic (see note above): pausing/resuming
                -- the loop must not rewind the seq into cached filenames.
                ProbeLogWrite("[BRIDGE] eval loop toggled paused=" .. tostring(BridgeEvalLoopPaused))
                DisplayTimedTextToPlayer(GetTriggerPlayer(), 0, 0, 5.00, "|cffffcc00[BRIDGE] eval loop " .. (BridgeEvalLoopPaused and "PAUSED" or "ACTIVE") .. "|r")
            end
            return
        end
        if op == "restart" then
            -- Restart the LOOP (timer), not the seq. EvalNextSeq stays monotonic;
            -- rewinding it would reuse Preloader-cached filenames and wedge the bridge.
            if BridgePollTimer ~= nil then
                DestroyTimer(BridgePollTimer)
                BridgePollTimer = nil
            end
            BridgeElapsed = 0
            BridgeStart()
            ProbeLogWrite("[BRIDGE] restarted via chat (loop only, seq kept)")
            DisplayTimedTextToPlayer(GetTriggerPlayer(), 0, 0, 5.00, "|cff00ff00[BRIDGE] restarted|r")
            return
        end
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
function SetupLogChat()
    local trigger = CreateTrigger()
    for i = 0, 23 do
        TriggerRegisterPlayerChatEvent(trigger, Player(i), "-log", false)
    end
    TriggerAddAction(trigger, function()
        local text = GetEventPlayerChatString()
        local args = string.sub(text, 5)
        local logOp, logTag = string.match(args, "^%s*(on|off|toggle|allon|alloff|list)%s*(.*)")
        if logOp == nil then
            local msg = "Usage: -log <on|off|toggle|allon|alloff|list> [TAG]"
            DisplayTimedTextToPlayer(GetTriggerPlayer(), 0, 0, 10.00, "|cffffcc00" .. msg .. "|r")
            return
        end
        logTag = string.match(logTag or "", "^(%S+)")
        if logOp == "allon" then
            LogFilterAll = true
            DisplayTimedTextToPlayer(GetTriggerPlayer(), 0, 0, 5.00, "|cff00ff00[LOG] all on|r")
        elseif logOp == "alloff" then
            LogFilterAll = false
            DisplayTimedTextToPlayer(GetTriggerPlayer(), 0, 0, 5.00, "|cffffff00[LOG] all off|r")
        elseif logOp == "list" then
            local parts = {}
            for tag, enabled in pairs(LogFilter) do
                parts[#parts + 1] = tag .. "=" .. tostring(enabled)
            end
            local msg = "all=" .. tostring(LogFilterAll) .. " " .. table.concat(parts, " ")
            ProbeLogWrite("[LOG] " .. msg)
            DisplayTimedTextToPlayer(GetTriggerPlayer(), 0, 0, 10.00, "|cff00ff00[LOG] " .. msg .. "|r")
        elseif logTag == "" or logTag == nil then
            DisplayTimedTextToPlayer(GetTriggerPlayer(), 0, 0, 10.00, "|cffff0000[LOG] tag required|r")
        elseif logOp == "on" then
            LogEnable(logTag)
            DisplayTimedTextToPlayer(GetTriggerPlayer(), 0, 0, 5.00, "|cff00ff00[LOG] on " .. logTag .. "|r")
        elseif logOp == "off" then
            LogDisable(logTag)
            DisplayTimedTextToPlayer(GetTriggerPlayer(), 0, 0, 5.00, "|cffff0000[LOG] off " .. logTag .. "|r")
        elseif logOp == "toggle" then
            LogToggle(logTag)
            local state = LogFilter[logTag] and "on" or "off"
            DisplayTimedTextToPlayer(GetTriggerPlayer(), 0, 0, 5.00, "|cffffcc00[LOG] " .. logTag .. "=" .. state .. "|r")
        end
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
        elseif type(v) == "boolean" then parts[#parts+1] = v and "true" or "false"
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
ProbeLogWrite("[BOOT] Framework loaded v3-aifix")
JASS_MAX_ARRAY_SIZE = 32768 -- vJASS constant, required by SanctifiedEnchantment hash ops
