import sys

from bl3hotfixmod.bl3hotfixmod import mod 

mod = Mod('varkid.bl3hotfix',
	'Varkid Evolution Increase',
	'TheGigaMaster',
	[
		"Tired of varkids never leveling up and evolving? Ever think you shouldn't be able to just run over these creatures and worry about having to take them out quick? If so, this mod is for you!"
		"On normal mode, evolution chance is increased by 50%, and on TVHM, evolution chance is doubled. The time of evolution isn't changed, and this is only for single player. This will not affect multiplayer, as those have different spawn values."
		"One interesting thing to note is that after super badass, the game says 'SuperToRaid' for the final evolution stage. In BL2, there was a 3 step process: super badass -> ultimate badass -> Verminvirous/supreme badass, which is absent in BL3." 
		"Digging deeper, it appears that the game decides to go from superbadass -> Verminvirous/supreme badass, omitting an evolution stage."
		"Upon a quick look at the wiki, the spawn chance values for ultimate badass -> Verminvirous/Supreme badass match the vaules for the 'SuperToRaid' chance. This spawn rate is at 0 or normal mode and only a 0.075 chance in TVHM, which matches up with what's in the game data."
		"So, what's this mean?"
		"The game is skipping an evolution step and cone a varakid reaches superbadass, well, IDK. Haven't got there yet."
		""
		""
		"The aim of normal mode is to make badasses more frequent and to rarely fight larva. Becuase let's be honest, no one wants to fight larva. Unless you've just stared a new game or are going into the Jakob's part of the map undergeared, these changes are aimed to make varkid's a good source of fun and XP."
	],
	lic=Mod.CC_BY_SA_40,
	v='0.2',
	cats='enemy''scaling',
	)
mod.newline()
mod.newline()
mod.comment('testing out a new style of code and seeing if I can get this damn thing to work')
mod.comment('increase varkid to adult to 100% chance')
mod.newline()
mod.reg_hotfix(Mod.CHAR, 'MatchAll',
    '/Game/Enemies/Varkid/_Shared/_Design/Attributes/Table_VarkidShared_EvolutionChance',
    'EvolveChance_LarvaToAdult.OnePlayer_PT1',
    """
    (
    	BaseValueConstant=1,
		DataTableValue=(
			DataTable=None,
			RowName="",
			ValueName=""),
		BaseValueAttribute=None,
		AttributeInitializer=None,
		BaseValueScale=1
    )
    """
mod.newline()
mod.newline()
mod.comment('adult to badass 100% chance')
mod.newline()
mod.reg_hotfix(Mod.CHAR, 'MatchAll',
    '/Game/Enemies/Varkid/_Shared/_Design/Attributes/Table_VarkidShared_EvolutionChance',
    'EvolveChance_AdultToBadass.OnePlayer_PT1',
    """
    (
    	BaseValueConstant=1,
			DataTableValue=(
			DataTable=None,
			RowName="",
			ValueName=""),
		BaseValueAttribute=None,
		AttributeInitializer=None,
		BaseValueScale=1
    )
    """
mod.newline()
mod.newline()
mod.comment('badass to superbadass 100% chance')
mod.newline()
mod.reg_hotfix(Mod.CHAR, 'MatchAll',
    '/Game/Enemies/Varkid/_Shared/_Design/Attributes/Table_VarkidShared_EvolutionChance',
    'EvolveChance_BadassToSuper.OnePlayer_PT1',
    """
    (
    	BaseValueConstant=1,
			DataTableValue=(
			DataTable=None,
			RowName="",
			ValueName=""),
		BaseValueAttribute=None,
		AttributeInitializer=None,
		BaseValueScale=1
    )
    """
mod.newline()
mod.newline()
mod.comment('badass to superbadass 100% chance')
mod.newline()
mod.reg_hotfix(Mod.CHAR, 'MatchAll',
    '/Game/Enemies/Varkid/_Shared/_Design/Attributes/Table_VarkidShared_EvolutionChance',
    'EvolveChance_SuperToRaid.OnePlayer_PT1',
    """
    (
    	BaseValueConstant=1,
			DataTableValue=(
			DataTable=None,
			RowName="",
			ValueName=""),
		BaseValueAttribute=None,
		AttributeInitializer=None,
		BaseValueScale=1
    )
    """
mod.close()
###Increase larva to adult from 60% to 90%
###Increase adult to badass from 30% to 45%
###Increase badass to superbadass from 10% to 15%
###Increase superbadass to raid from 0% to 5%
###
###
###
###On TVHM, you'd better be ready. Mama isn't holding your hand anymore, the gloves are coming off. You'd better pray you don't run into a "Raid" level difficulty as soon as you start TVHM. Kill fast or get killed.
#future idea - increase all spawns to make ultimate badass 75%+ and "raid" 50%. daddy has the belt.
###
###Increase larva to adult from 60% to 100% TVHM
###Increase adult to badass from 40% to 80% TVHM
###Increase badass to superbadass from 20% to 40% TVHM
###Increase superbadass to ultimate badass (AKA Raid) from 10% to 20% TVHM 
###
###This is the first time I've ever made a mod, let alone do anything involving code (excpet for printing Hello, World! in 9th grade). So if things don't go quite as expected, don't be shocked when it breaks. Any feedback/tips/advice is appreciated! At some point, I may make variations of this mod to choose how hard you want it to be.

#0.1.2 - using code above and compiled into solid block

#SparkCharacterLoadedEntry,(1,2,0,MatchAll),/Game/Enemies/Varkid/_Shared/_Design/Attributes/Table_VarkidShared_EvolutionChance.Table_VarkidShared_EvolutionChance,EvolveChance_AdultToBadass.OnePlayer_PT1.BaseValueConstant,0,,1
#SparkCharacterLoadedEntry,(1,2,0,MatchAll),/Game/Enemies/Varkid/_Shared/_Design/Attributes/Table_VarkidShared_EvolutionChance.Table_VarkidShared_EvolutionChance,EvolveChance_BadassToSuper.OnePlayer_PT1.BaseValueConstant,0,,1
#SparkCharacterLoadedEntry,(1,2,0,MatchAll),/Game/Enemies/Varkid/_Shared/_Design/Attributes/Table_VarkidShared_EvolutionChance.Table_VarkidShared_EvolutionChance,EvolveChance_SuperToRaid.OnePlayer_PT1.BaseValueConstant,0,,1




###old code but still nice to have
#SparkCharacterLoadedEntry,(1,2,0,MatchAll),/Game/Enemies/Varkid/_Shared/_Design/Attributes/Table_VarkidShared_EvolutionChance.Table_VarkidShared_EvolutionChance,EvolveChance_BadassToSuper.OnePlayer_PT1.BaseValueConstant,0,,5




#here we go
#0.1.1 - removed basevalueconstant from line



#Increase larva to adult from 80% to 100% TVHM

#SparkCharacterLoadedEntry,(1,2,0,MatchAll),/Game/Enemies/Varkid/_Shared/_Design/Attributes/Table_VarkidShared_EvolutionChance.Table_VarkidShared_EvolutionChance,EvolveChance_LarvaToAdult.OnePlayer_PT2.BaseValueConstant,0,,(BaseValueConstant=1,DataTableValue=(DataTable=None,RowName="",ValueName=""),BaseValueAttribute=None,AttributeInitializer=None,BaseValueScale=1)




#Increase adult to badass from 40% to 80% TVHM

#SparkCharacterLoadedEntry,(1,2,0,MatchAll),/Game/Enemies/Varkid/_Shared/_Design/Attributes/Table_VarkidShared_EvolutionChance.Table_VarkidShared_EvolutionChance,EvolveChance_AdultToBadass,OnePlayer_PT2.BaseValueConstant,0,,(BaseValueConstant=.80,DataTableValue=(DataTable=None,RowName="",ValueName=""),BaseValueAttribute=None,AttributeInitializer=None,BaseValueScale=1)




#Increase badass to superbadass from 20% to 40% TVHM

#SparkCharacterLoadedEntry,(1,2,0,MatchAll),/Game/Enemies/Varkid/_Shared/_Design/Attributes/Table_VarkidShared_EvolutionChance.Table_VarkidShared_EvolutionChance,EvolveChance_BadassToSuper.OnePlayer_PT2.BaseValueConstant,0,,(BaseValueConstant=.40,DataTableValue=(DataTable=None,RowName="",ValueName=""),BaseValueAttribute=None,AttributeInitializer=None,BaseValueScale=1)




#Increase superbadass to ultimate badass (AKA Raid) from 7.5% to 15% TVHM 

#SparkCharacterLoadedEntry,(1,2,0,MatchAll),/Game/Enemies/Varkid/_Shared/_Design/Attributes/Table_VarkidShared_EvolutionChance.Table_VarkidShared_EvolutionChance,EvolveChance_SuperToRaid.OnePlayer_PT2.BaseValueConstant,0,,(BaseValueConstant=.15,DataTableValue=(DataTable=None,RowName="",ValueName=""),BaseValueAttribute=None,AttributeInitializer=None,BaseValueScale=1)
