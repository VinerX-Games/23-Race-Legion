-- ============================================================
-- 23 Race Legion - Lua Rewrite
-- war3map.lua — Entry point for WC3 Lua map
-- ============================================================
-- This is the main script loaded by WC3 engine when map uses Lua VM.
-- The engine automatically calls config() and main() functions.

-- ============================================================
-- Module loader
-- In WC3 Lua mode, the map is loaded from the .w3x archive.
-- All Lua files are at root level of the archive.
-- ============================================================

dofile("globals.lua")
dofile("tables.lua")
dofile("utils.lua")
dofile("init.lua")
dofile("economy.lua")
dofile("stolica.lua")
dofile("ai_filters.lua")
dofile("ai_utils.lua")
dofile("spells_common.lua")
dofile("race_init.lua")
dofile("spells_races_1.lua")
dofile("spells_races_2.lua")
dofile("lobby.lua")
dofile("main.lua")

-- config() and main() are defined in main.lua
-- WC3 engine will call them automatically after loading this file.
