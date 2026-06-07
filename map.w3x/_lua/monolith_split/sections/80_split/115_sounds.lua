-- *  Sound Assets
-- 
-- ***************************************************************************
---@return nothing
function InitSounds()
	gg_snd_oep_82_nzothfish_whispers_offset_periodic_ambient_09__2_u = CreateSound("war3mapImported/oep_82_nzothfish_whispers_offset_periodic_ambient_09 (2).mp3", false, false, false, 0, 0, "DefaultEAXON")
	SetSoundDuration(gg_snd_oep_82_nzothfish_whispers_offset_periodic_ambient_09__2_u, 144)
	SetSoundChannel(gg_snd_oep_82_nzothfish_whispers_offset_periodic_ambient_09__2_u, 0)
	SetSoundVolume(gg_snd_oep_82_nzothfish_whispers_offset_periodic_ambient_09__2_u, 127)
	SetSoundPitch(gg_snd_oep_82_nzothfish_whispers_offset_periodic_ambient_09__2_u, 1.0)
	gg_snd_QuestLog = CreateSound("Sound/Interface/QuestLog.flac", false, false, false, 0, 0, "DefaultEAXON")
	SetSoundParamsFromLabel(gg_snd_QuestLog, "QuestUpdate")
	SetSoundDuration(gg_snd_QuestLog, 2275)
	SetSoundVolume(gg_snd_QuestLog, 80)
	gg_snd_BerserkerCaster = CreateSound("Units/Orc/Grunt/BerserkerCaster.flac", false, true, true, 0, 0, "SpellsEAX")
	SetSoundParamsFromLabel(gg_snd_BerserkerCaster, "BerserkerRage")
	SetSoundDuration(gg_snd_BerserkerCaster, 2092)
	SetSoundVolume(gg_snd_BerserkerCaster, 127)
	gg_snd_ImpaleHit = CreateSound("Abilities/Spells/Undead/Impale/ImpaleHit.flac", false, true, true, 0, 0, "SpellsEAX")
	SetSoundParamsFromLabel(gg_snd_ImpaleHit, "ImpaleHit")
	SetSoundDuration(gg_snd_ImpaleHit, 1666)
	SetSoundVolume(gg_snd_ImpaleHit, 127)
end
-- ***************************************************************************
-- 
