local function ScheduleUISetupPass(delay, label)
    local timer = CreateTimer()
    TimerStart(timer, delay, false, function()
        DestroyTimer(timer)
        timer = nil
        ProbeStep("UISetup:" .. label, UISetup)
    end)
end

local function DeferredUISetup()
    ScheduleUISetupPass(0.10, "pass1")
    ScheduleUISetupPass(1.00, "pass2")
end

function main()
    ProbeLogWrite("[MAIN] entered")
    SetCameraBounds(
        - 30720.0 + GetCameraMargin(CAMERA_MARGIN_LEFT),
        - 30720.0 + GetCameraMargin(CAMERA_MARGIN_BOTTOM),
        30720.0 - GetCameraMargin(CAMERA_MARGIN_RIGHT),
        30720.0 - GetCameraMargin(CAMERA_MARGIN_TOP),
        - 30720.0 + GetCameraMargin(CAMERA_MARGIN_LEFT),
        30720.0 - GetCameraMargin(CAMERA_MARGIN_TOP),
        30720.0 - GetCameraMargin(CAMERA_MARGIN_RIGHT),
        - 30720.0 + GetCameraMargin(CAMERA_MARGIN_BOTTOM))
    SetDayNightModels("EnvironmentDNCDNCLordaeronDNCLordaeronTerrainDNCLordaeronTerrain.mdl",
                       "EnvironmentDNCDNCLordaeronDNCLordaeronUnitDNCLordaeronUnit.mdl")
    SetTerrainFogEx(0, 4000.0, 8000.0, 0.500, 0.706, 1.000, 1.000)
    SetWaterBaseColor(190, 190, 160, 255)
    NewSoundEnvironment("Default")
    SetAmbientDaySound("VillageDay")
    SetAmbientNightSound("VillageNight")
    SetMapMusic("Music", true, 0)
    ProbeStep("InitBlizzard", InitBlizzard)
    ProbeStep("InitSounds", InitSounds)
    ProbeStep("CreateRegions", CreateRegions)
    ProbeStep("CreateCameras", CreateCameras)
    ProbeStep("CreateAllUnits", CreateAllUnits)
    -- ProbeLogEnableFlush()  -- disabled: no log spam by default
    -- Everything below is DEFERRED to game start (safe in Lua mode)
    ProbeLogWrite("[MAIN] registering deferred init queue")
    OnInit.fn(Global___Init, "Global___Init")
    OnInit.fn(SpellSleepAOE___onInit, "SpellSleepAOE___onInit")
    OnInit.fn(SanctifiedEnchantment___Init, "SanctifiedEnchantment___Init")
    OnInit.fn(initBoolExprs___Init, "initBoolExprs___Init")
    OnInit.fn(SetupCodexPingChat, "SetupCodexPingChat")
    OnInit.fn(SetupLogChat, "SetupLogChat")
    OnInit.fn(SetupBridgeChat, "SetupBridgeChat")
    OnInit.fn(BridgeStart, "BridgeStart")
    OnInit.fn(DeferredUISetup, "DeferredUISetup")
    OnInit.fn(Face2, "Face2")
    OnInit.fn(SetContinetsBooleprs, "SetContinetsBooleprs")
    OnInit.fn(InitGlobals, "InitGlobals")
    OnInit.fn(InitCustomTriggers, "InitCustomTriggers")
    OnInit.fn(RunInitializationTriggers, "RunInitializationTriggers")
    ProbeLogWrite("[MAIN] starting deferred init queue")
    OnInit._run()
    ProbeLogWrite("[MAIN] completed")
end
--***************************************************************************
--*
--*  Map Configuration
--*
--***************************************************************************
