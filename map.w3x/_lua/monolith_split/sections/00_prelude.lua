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
ProbeLogWrite("[BOOT] Framework loaded")
JASS_MAX_ARRAY_SIZE = 32768 -- vJASS constant, required by SanctifiedEnchantment hash ops
