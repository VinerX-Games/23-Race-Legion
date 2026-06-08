
-- ***************************************************************************
-- *  PlayerUI
---@return nothing
function UISetup()
	-- Local Variables
	local consoleBackdrop = BlzGetFrameByName("ConsoleUIBackdrop", 0)
	local upperButtonBar = BlzGetFrameByName("UpperButtonBarFrame", 0)
	ProbeLogWrite("[UI] ConsoleUIBackdrop=" .. tostring(consoleBackdrop ~= nil) .. " UpperButtonBarFrame=" .. tostring(upperButtonBar ~= nil))
	if consoleBackdrop == nil or upperButtonBar == nil then
		ProbeLogWrite("[UI] skipped: required frames missing")
		return
	end
	framehandlefh = nil
	framehandlechatButton = nil
	framehandlequestButton = nil
	framehandleallyButton = nil
	framehandleMiniMap = nil
	framehandlegridButtons = nil
	framehandleimageTest = BlzCreateFrameByType("BACKDROP", "image", consoleBackdrop, "ButtonBackdropTemplate", 0)
	
	-- Top UI & System Buttons
	fh = upperButtonBar
	BlzFrameSetVisible(fh, true)
	allyButton = BlzGetFrameByName("UpperButtonBarAlliesButton", 0)
	fh = BlzGetFrameByName("UpperButtonBarMenuButton", 0)
	chatButton = BlzGetFrameByName("UpperButtonBarChatButton", 0)
	questButton = BlzGetFrameByName("UpperButtonBarQuestsButton", 0)
	BlzFrameClearAllPoints(fh)
	BlzFrameClearAllPoints(allyButton)
	BlzFrameClearAllPoints(chatButton)
	BlzFrameClearAllPoints(questButton)
	BlzFrameSetAbsPoint(questButton, FRAMEPOINT_TOPLEFT, 0.05, 0.6)
	BlzFrameSetAbsPoint(fh, FRAMEPOINT_TOPLEFT, -0.03, 0.6)
	BlzFrameSetAbsPoint(allyButton, FRAMEPOINT_TOPLEFT, 0.05, 0.583)
	BlzFrameSetAbsPoint(chatButton, FRAMEPOINT_TOPLEFT, -0.03, 0.583)
	
	-- Hiding clock UI and creating new frame bar
	BlzFrameSetTexture(imageTest, "UI\\ResourceBar.tga", 0, true)
	BlzFrameSetPoint(imageTest, FRAMEPOINT_TOP, BlzGetOriginFrame(ORIGIN_FRAME_WORLD_FRAME, 0), FRAMEPOINT_TOP, 0, 0)
	BlzFrameSetSize(imageTest, 0.52, 0.025)
	BlzFrameSetLevel(imageTest, 1)
	
	-- Food
	fh = BlzGetFrameByName("ResourceBarSupplyText", 0)
	BlzFrameSetAbsPoint(fh, FRAMEPOINT_TOPRIGHT, 0.640, 0.5965)
	
	-- Upkeep
	fh = BlzGetFrameByName("ResourceBarUpkeepText", 0)
	BlzFrameSetAbsPoint(fh, FRAMEPOINT_TOPRIGHT, 0.8, 0.6965)
	
	-- Gold
	fh = BlzGetFrameByName("ResourceBarGoldText", 0)
	BlzFrameSetAbsPoint(fh, FRAMEPOINT_TOPRIGHT, 0.329, 0.5965)
	
	-- Lumber
	fh = BlzGetFrameByName("ResourceBarLumberText", 0)
	BlzFrameSetAbsPoint(fh, FRAMEPOINT_TOPRIGHT, 0.546, 0.5965)
	
	-- Bottom UI & Idle Worker Icon
	
	-- set fh = BlzGetFrameByName("ConsoleUI", 0)
	-- set fh = BlzFrameGetChild(fh, 7)
	fh = BlzGetFrameByName("ConsoleBottomBar", 0)
	fh = BlzFrameGetChild(fh, 3)
	BlzFrameClearAllPoints(fh)
	BlzFrameSetAbsPoint(fh, FRAMEPOINT_TOPRIGHT, 0.09, 0.179)
	
	-- Remove Deadspace
	fh = BlzGetFrameByName("ConsoleUI", 0)
	BlzFrameSetVisible(BlzFrameGetChild(fh, 5), false)
	
	-- Minimap
	MiniMap = BlzGetFrameByName("MiniMapFrame", 0)
	BlzFrameSetVisible(MiniMap, true)
	BlzFrameClearAllPoints(MiniMap)
	BlzFrameSetAbsPoint(MiniMap, FRAMEPOINT_BOTTOMLEFT, 0.0525, 0.0)
	BlzFrameSetAbsPoint(MiniMap, FRAMEPOINT_TOPRIGHT, 0.2125, 0.141)
	
	-- Minimap Buttons
	fh = BlzGetFrameByName("MiniMapCreepButton", 0)
	BlzFrameClearAllPoints(fh)
	BlzFrameSetAbsPoint(fh, FRAMEPOINT_BOTTOMLEFT, 0.214, 0.116)
	BlzFrameSetAbsPoint(fh, FRAMEPOINT_TOPRIGHT, 0.234, 0.136)
	BlzFrameSetTexture(fh, "UI\\ButtonBorder.dds", 0, true)
	fh = BlzGetFrameByName("MiniMapAllyButton", 0)
	BlzFrameClearAllPoints(fh)
	BlzFrameSetAbsPoint(fh, FRAMEPOINT_BOTTOMLEFT, 0.234, 0.116)
	BlzFrameSetAbsPoint(fh, FRAMEPOINT_TOPRIGHT, 0.254, 0.136)
	BlzFrameSetTexture(fh, "UI\\ButtonBorder.dds", 0, true)
	fh = BlzGetFrameByName("MiniMapTerrainButton", 0)
	BlzFrameClearAllPoints(fh)
	BlzFrameSetAbsPoint(fh, FRAMEPOINT_BOTTOMLEFT, 0.254, 0.116)
	BlzFrameSetAbsPoint(fh, FRAMEPOINT_TOPRIGHT, 0.274, 0.136)
	BlzFrameSetTexture(fh, "UI\\ButtonBorder.dds", 0, true)
	fh = BlzGetFrameByName("MinimapSignalButton", 0)
	BlzFrameSetVisible(fh, false)
	fh = BlzGetFrameByName("FormationButton", 0)
	BlzFrameClearAllPoints(fh)
	BlzFrameSetAbsPoint(fh, FRAMEPOINT_BOTTOMLEFT, 0.274, 0.116)
	BlzFrameSetAbsPoint(fh, FRAMEPOINT_TOPRIGHT, 0.294, 0.136)
	BlzFrameSetTexture(fh, "UI\\ButtonBorder.dds", 0, true)
	
	-- Minimap Border
	fh = BlzCreateFrameByType("BACKDROP", "MinimapBorder", MiniMap, "", 0)
	BlzFrameSetPoint(fh, FRAMEPOINT_TOPLEFT, MiniMap, FRAMEPOINT_TOPLEFT, 0, 0)
	BlzFrameSetPoint(fh, FRAMEPOINT_BOTTOMRIGHT, MiniMap, FRAMEPOINT_BOTTOMRIGHT, 0, 0)
	BlzFrameSetTexture(fh, "UI\\MiniMapBorder.dds", 0, true)
	
	-- Tooltips
	fh = BlzGetOriginFrame(ORIGIN_FRAME_TOOLTIP, 0)
	BlzFrameSetVisible(fh, true)
	fh = BlzGetOriginFrame(ORIGIN_FRAME_UBERTOOLTIP, 0)
	BlzFrameSetVisible(fh, true)
	BlzFrameClearAllPoints(fh)
	BlzFrameSetAbsPoint(fh, FRAMEPOINT_BOTTOMRIGHT, 0.7725, 0.141)
	
	-- Command Buttons
	gridButtons = BlzGetFrameByName("CommandBarFrame", 0)
	BlzFrameSetVisible(gridButtons, true)
	BlzFrameClearAllPoints(gridButtons)
	BlzFrameSetAbsPoint(gridButtons, FRAMEPOINT_BOTTOMLEFT, 0.5950, 0.005)
	
	-- Backdrop
	fh = BlzGetFrameByName("ConsoleUIBackdrop", 0)
	BlzFrameClearAllPoints(fh)
	BlzFrameSetAbsPoint(fh, FRAMEPOINT_BOTTOMLEFT, 0.052, 0)
	BlzFrameSetAbsPoint(fh, FRAMEPOINT_TOPRIGHT, 0.770, 0.141)
	
	-- Command buttons border
	fh = BlzCreateFrameByType("BACKDROP", "CommandBorder", MiniMap, "", 0)
	BlzFrameSetPoint(fh, FRAMEPOINT_TOPLEFT, gridButtons, FRAMEPOINT_TOPLEFT, -0.007, 0.007)
	BlzFrameSetPoint(fh, FRAMEPOINT_BOTTOMRIGHT, gridButtons, FRAMEPOINT_BOTTOMRIGHT, 0.0025, -0.005)
	BlzFrameSetTexture(fh, "UI\\CommandCard.dds", 0, true)
	
	--  Prevent multiplayer desyncs by forcing the creation of the QuestDialog frame
	-- 	call BlzFrameClick(BlzGetFrameByName("UpperButtonBarQuestsButton", 0))
	-- 	call ForceUICancel()
	
	--  Expand TextArea
	BlzFrameSetPoint(BlzGetFrameByName("QuestDisplay", 0), FRAMEPOINT_TOPLEFT, BlzGetFrameByName("QuestDetailsTitle", 0), FRAMEPOINT_BOTTOMLEFT, 0.003, -0.003)
	BlzFrameSetPoint(BlzGetFrameByName("QuestDisplay", 0), FRAMEPOINT_BOTTOMRIGHT, BlzGetFrameByName("QuestDisplayBackdrop", 0), FRAMEPOINT_BOTTOMRIGHT, -0.003, 0.)
	
	--  Relocate button
	BlzFrameSetPoint(BlzGetFrameByName("QuestDisplayBackdrop", 0), FRAMEPOINT_BOTTOM, BlzGetFrameByName("QuestBackdrop", 0), FRAMEPOINT_BOTTOM, 0., 0.017)
	BlzFrameClearAllPoints(BlzGetFrameByName("QuestAcceptButton", 0))
	BlzFrameSetPoint(BlzGetFrameByName("QuestAcceptButton", 0), FRAMEPOINT_TOPRIGHT, BlzGetFrameByName("QuestBackdrop", 0), FRAMEPOINT_TOPRIGHT, -0.016, -0.016)
	BlzFrameSetText(BlzGetFrameByName("QuestAcceptButton", 0), "?")
	BlzFrameSetSize(BlzGetFrameByName("QuestAcceptButton", 0), 0.03, 0.03)
	
	--  Add back ally resource icons
	BlzFrameSetTexture(BlzGetFrameByName("InfoPanelIconAllyGoldIcon", 7), "UI\\RGReplacement.dds", 0, false)
	BlzFrameSetTexture(BlzGetFrameByName("InfoPanelIconAllyWoodIcon", 7), "UI\\RLReplacement.dds", 0, false)
	BlzFrameSetTexture(BlzGetFrameByName("InfoPanelIconAllyFoodIcon", 7), "UI\\RSReplacement.dds", 0, false)
	
end
--  scope init begins
---@return nothing
function init___Init()
	UISetup()
end