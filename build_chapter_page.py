#!/usr/bin/env python
# -*- coding: utf-8 -*- 

"""
Written by Albert"Anferensis"Ong
A program designed to build a chapter page for fireemblemwiki.org.

Note: This program has only been tested for Fire Emblem 5, 6, 7, 8, and 9.
	  It may not function properly for other titles. 
"""

# Importing functions from other fireemblemwiki scripts. 
from build_character_data import build_character_data
from build_enemy_data import build_enemy_data
from build_item_data import build_item_data
from build_npc_data import build_npc_data
from build_shop_data import build_shop_data		
from utilities import hyperlink, writeTextFile



def build_chapter_page(hatnote, 
					   platform, 
					   chapter_title, 
					   chapter_infobox,
					   game, 
					   quote,
					   quote_speaker,
					   chapter_desciption, 
					   chapter_plot,
					   beginning_log,
					   chapter_data_infobox,  
					   return_characters,
					   new_units_data,
					   character_data_note,
					   item_data,
					   item_data_note,
					   shop_data_header,
					   shops_info,
					   enemy_data,					   
					   reinforcement_data,
					   enemy_data_note,
					   print_units_total,
					   npc_data,
					   npc_data_note,
					   boss_name,
					   detailed_boss_data,
					   chapter_navigator_section, 
					   strategy,
					   trivia,
					   chapter_etymology,
					   gallery_text,
					   isStub = True):
	"""
	A function designed to build a chapter page for fireemblemwiki.org.
	"""					   
	
	# Creates a stub mark if the page is a stub.
	if isStub:
		stub_mark = "{{stub}}"
		
	# Otherwise, the stub mark is registered as "None"
	else:
		stub_mark = None
	
	#==============================================================
	
	# Building chapter quote
	
	if quote == None or quote_speaker == None:
		chapter_quote = None
		
	else:
		chapter_quote = "{{Quote|" + quote + "|" + quote_speaker + "}} \n"
	
	#==============================================================

	# Building plot section
	
	plot_section = ""
	
	if chapter_plot == None:
		plot_body = "{{sectstub}}"
	else:
		plot_body = chapter_plot
		
	if beginning_log == None:
		beginning_log_section = ""
		
	else:
		beginning_log_section = "===Beginning Log=== \n" + \
								beginning_log
		
	for part in ("==Plot==",
				 "{{main|" + chapter_title + "/Script}}",
				 plot_body + "\n",
				 beginning_log_section):
		
		plot_section += part + "\n"
	
	#==============================================================
	
	# Building chapter data
	
	chapter_data = "==Chapter Data== \n" + \
					chapter_data_infobox
		
	#==============================================================
	
	# Building character data section
	character_data_section = \
		build_character_data(game, 
							 new_units_data, 
							 return_characters, 
							 character_data_note)
					   
	#=============================================================
	
	# Building item data
	item_data_section = build_item_data(platform, 
										item_data, 
										item_data_note)
	
	#=============================================================
	
	# Building shop data
	shop_data_section = build_shop_data(platform, 
										game, 
										shops_info, 
										shop_data_header)
	
	#==============================================================
	
	# Building enemy data
	enemy_data_section = build_enemy_data(platform, 
										  enemy_data, 
										  reinforcement_data, 
										  enemy_data_note,
										  print_units_total)
	
	#==============================================================
	
	# Building NPC data section
	npc_data_section = build_npc_data(npc_data, 
									  npc_data_note)
							  
	#==============================================================
	
	# Building boss data
	
	if boss_name != None:
		boss_redirect_line = "{{Main|" + boss_name + "}}"
		
	else:
		boss_redirect_line = None
	
	
	boss_data_section = ""
						
	for line in ("===Boss Data===", 
				 boss_redirect_line, 
				 detailed_boss_data):
					 
		if line != None:
			boss_data_section += line + "\n"
			
		else:
			boss_data_section = None
											    
	#==============================================================
	
	# Building strategy section
	
	if strategy == None:
		strategy_body = "{{sectstub}}"
		
	else:
		strategy_body = "{{strategy}} \n" + \
						   strategy
		
	strategy_section = ""
	
	for line in ("==Strategy==", 
				 strategy_body):
					 
		strategy_section += line + "\n"
		
	#==============================================================
	
	# Building trivia section
	
	trivia_section = ""
	
	if trivia == None:
		trivia_body = None
	else:
		trivia_body = trivia
		
	for line in ("==Trivia==", 
				 trivia_body):
		
		if line != None:			 
			trivia_section += line + "\n"
		
	#==============================================================
	
	# Building etymology section
	
	etymology_section = "==Etymology and other languages== \n" + \
						chapter_etymology
		
	#==============================================================
	
	# Building gallery section
	
	gallery_section = "==Gallery== \n"
	
	if gallery_text == None:
		gallery_section_text = "{{sectstub}}"
		
	else:
		gallery_section_text = gallery_text
		
	gallery_section += gallery_section_text + "\n"
	
	#==============================================================
	
	# Building chapter navigator and chapter category
	
	chapter_nav_dict = \
		{"fe01" : "{{Nav1}}", 
		 "fe02" : "{{Nav2}}", 
		 "fe03" : "{{Nav3}}",
		 "fe04" : "{{Nav4}}",
		 "fe05" : "{{Nav5}}",
		 "fe06" : "{{Nav6}}", 
		 "fe07" : "{{Nav7}}", 
		 "fe08" : "{{Nav8}}", 
		 "fe09" : "{{Nav9}}", 
		 "fe10" : "{{Nav10}}", 
		 "fe11" : "{{Nav11}}", 
		 "fe12" : "{{Nav12}}", 
		 "fe13" : "{{Nav13}}", 
		 "fe14" : "{{Nav14}}", 
		 "fe15" : "{{Nav15}}",}
						
	chapter_nav = chapter_nav_dict[game]
	
	title_name_dict = \
		{"fe01" : "Fire Emblem: Shadow Dragon and the Blade of Light",
		 "fe02" : "Fire Emblem: Gaiden",
	     "fe03" : "Fire Emblem: Mystery of the Emblem",
	     "fe04" : "Fire Emblem: Genealogy of the Holy War",
	     "fe05" : "Fire Emblem: Thracia 776",
	     "fe06" : "Fire Emblem: The Binding Blade",
	     "fe07" : "Fire Emblem (GBA)",
	     "fe08" : "Fire Emblem: The Sacred Stones",
	     "fe09" : "Fire Emblem: Path of Radiance",
	     "fe10" : "Fire Emblem: Radiant Dawn",
	     "fe11" : "Fire Emblem: Shadow Dragon",
	     "fe12" : "Fire Emblem: New Mystery of the Emblem",
	     "fe13" : "Fire Emblem: Awakening",
	     "fe14" : "Fire Emblem: Fates",
	     "fe15" : "Fire Emblem Echos: Shadows of Valentia"}
	     
	title_name = title_name_dict[game]
	
	chapter_category = "[[Category:Chapters of " + title_name + "]]"

	#==============================================================
	
	# Builds the complete chapter page
	
	chapter_page = ""
	
	for section in (hatnote,
					stub_mark, 
					chapter_infobox, 
					chapter_quote,
					chapter_desciption, 
					plot_section, 
				    chapter_data, 
				    character_data_section,
				    item_data_section, 
				    shop_data_section, 
				    enemy_data_section,
				    npc_data_section,
				    boss_data_section,
				    strategy_section, 
				    trivia_section, 
				    etymology_section, 
				    gallery_section,
					chapter_navigator_section,
					chapter_nav,
					chapter_category):
		
		if section != None:				
			chapter_page += section + "\n"
											 
	return chapter_page
	


#=======================================================================
#
# User input for creating a chapter page. 	
#
#=======================================================================


# Insert a hatnote.
# This is used for cases where a page needs disambiguation.
# If no hatnote is needed, insert "None".

# Hatnote template:
"""
:''Hatnote text''
----
"""

hatnote = None


# Insert whether or not the page is a stub.
isStub = True


# Insert platform name
platform = "gcn"

# Insert the game number
# Such as fe01, fe02, fe03 ...
game = "fe09"

# Insert chapter title
chapter_title = "Repatriation"

# Insert chapter infobox
chapter_infobox = \
"""{{Chapter Infobox 
|title=Repatriation
|image=[[File:Cm fe09 F.png|200px]]
|location=[[Crimea]] Castle
|new units=[[Tibarn]], [[Naesala]], or [[Giffca]]
|boss=[[Ashnard]], [[Bryce]]
|weather=
}}"""

# Chapter infobox template
"""{{Chapter Infobox 
|title=
|image=[[File:Cm fe__ __.png|200px]]
|location
|new units
|boss=
|weather=
}}"""


# Insert a quote and the quote's speaker. 
# This is primarily for aesthetic purposes. 

# If "None" is inputted for either the quote or quote speaker,
# then a quote will not appear

quote = "Our road has been long, but it ends today! Let's liberate Crimea and free our friends...and our families...from Daein's tyranny! Men of Crimea...Laguz of Tellius...Greil Mercenaries...MOVE OUT!!"
quote_speaker = "[[Ike]]"


# Insert chapter description. 
chapter_desciption = \
"""'''Repatriation''' (Japanese: {{hover|帰還|Kikan}}, ''Repatriation'') is the final chapter of {{FE9}}."""


# Insert chapter plot.
# If "None is inputted", this section will be marked as a stub.
chapter_plot = None

# Insert beginning log
# If there is no beginning log, insert "None"
beginning_log = \
"""The [[Crimea]]n royal palac, located in the center of Melior, is famed for its beautiful  gardens where the world seems at peace. But times have changed. Countless battles have raged in these idyllic confines, and a new dark lord now sits upon the throne. The palace itself has not suffered--it remains a study in dignity and elegance. Yet there is no peace on this day. A grim tension fills the air, engulfing all it touches in deafening silence. Within the heart of the palace sits the author of this war: [[Ashnard]], king of [[Daein]]. <br>
[[Ike]], supreme commander of the [[Crimea]]n army, and [[Elincia]], princess of [[Crimea]], have completed their battle preparations. Now, they spend a tense morning waiting for the decisive battle that will conclude their yearlong odyssey. They wait for the beginning of the end."""


# Insert chapter infobox data.
chapter_data_box = \
"""{{ChapDataMap
|victory=Defeat [[Ashnard]]
|defeat=[[Ike]] or [[Elincia]] dies 
|ally=14{{hover|+1|Tibarn, Naesala, or Giffca}}
|partner=0
|other=0
|enemy=50
|map=[[File:Cm fe09 F.png]]
}}
"""

# Chapter databox template. 
"""{{ChapDataMap
|victory=
|defeat=
|ally=
|partner=
|other=
|enemy=
|map=
}}"""


# Insert returning characters and new units data
return_characters = \
["Ike", "Titania", "Oscar", "Boyd", "Rhys", "Soren", "Mia", "Ilyana", 
"Mist", "Rolf", "Marcia", "Lethe", "Mordecai", "Volke", "Brom",
"Kieran", "Nephenee", "Zihark", "Sothe", "Jill", "Astrid", "Gatrie", 
"Makalov", "Stefan", "Muarim", "Tormod", "Devdan", "Reyson", "Ulki", "Janaff", 
"Tanith", "Shinon", "Calill", "Tauroneo", "Ranulf", "Haar", "Bastian", 
"Lucia", "Geoffrey", "Largo", "Elincia", "Ena", "Nasir"]

  
# New units data is organized:
#  ["unit name", ["class", "HP", "level", "recruit method"]]

# ["", ["", "", "", ""]], 

# If there are no new units, input "None"

new_units_data = \
[["Tibarn", "Hawk (class) {{!}} Hawk", "63", "18", "Select [[Tibarn]] when prompted"], 
["Naesala", "Raven (class) {{!}} Raven", "57", "17", "Select [[Naesala]] when prompted"], 
["Giffca", "Lion", "68", "20", "Select [[Giffca]] when prompted"], ]


# Insert a text note under the character data .
# If no note is needed, insert "None".
character_data_note = "<small>*Note: [[Tibarn]], [[Naesala]], or [[Giffca]] will join either at the beginning of the chapter on easy and medium mode or at the start of the second part of the chapter on hard and maniac mode. </small>"


# Insert item data

# Item data is formatted:
#	[item name, obtain method]

# ["", ""], 

item_data = \
[["Physic", "Dropped by [[bishop]]"],
["Speedwing", "Dropped by [[Bryce]]"], 
["Silence", "Steal from [[bishop]]"], 
["Elixir", "Steal from [[bishop]]"], 
["Sleep", "Steal from [[bishop]]"], 
["Fortify", "Steal from [[bishop]]"], 
["Elixir", "Steal from [[bishop]]"], 
["Rexaura", "Steal from [[bishop]]"], 
["Vulnerary", "Steal from [[paladin]]"], 
["Vulnerary", "Steal from [[paladin]]"], 
["Vulnerary", "Steal from [[paladin]]"], 
["Vulnerary", "Steal from [[paladin]]"], 
["Vulnerary", "Steal from [[paladin]]"], 
["Vulnerary", "Steal from [[paladin]]"], 
["Vulnerary", "Steal from [[paladin]]"], 
["Vulnerary", "Steal from [[paladin]]"], 
["Vulnerary", "Steal from [[paladin]]"], 
["Vulnerary", "Steal from [[paladin]]"], 
["Vulnerary", "Steal from [[paladin]]"], 
["Thoron", "Steal from [[sage]]"], 
["Meteor", "Steal from [[sage]]"], 
["Vulnerary", "Steal from [[sage]]"], 
["Vulnerary", "Steal from [[swordmaster]]"], 
["Steel Sword", "Steal from [[paladin]]"], 
["Steel Lance", "Steal from [[paladin]]"], 
["Killing Edge", "Steal from [[paladin]]"], 
["Silver Lance", "Steal from [[paladin]]"], 
["Silver Sword", "Steal from [[paladin]]"], 
["Iron Axe", "Steal from [[paladin]]"], 
["Iron Axe", "Steal from [[paladin]]"], 
["Iron Axe", "Steal from [[paladin]]"],]


# Insert note after under item data. 
# If no note is needed, insert "None".
item_data_note = \
None


shop_data_header = "Shop Data"

# Insert shop data
# If there are no shops, input "None"

# Shop info is formatted:
#	[shop name, [item1, item2, item3]], 

# ["", ["", "", ""]], 

shops_info = \
None

# Unit data is formatted:
# 	[name, class, level, quantity, inventory]

# ["", "", "", "", [""]], 

enemy_data = \
[["Soldier", "Bishop", "15", "1", ["Shine", "Silence", "Physic (drop)", "Elixir"]], 
["Soldier", "Bishop", "15", "1", ["Rexaura", "Sleep", "Fortify", "Elixir"]], 
["Feral One", "Cat", "16", "2", ["Claw (cat)"]],
["Soldier", "General", "15", "1", ["Silver Lance"]], 
["Soldier", "General", "15", "1", ["Silver Lance", "Vulnerary"]],
["Soldier", "Halberdier", "14", "1", ["Brave Lance"]], 
["Soldier", "Halberdier", "15", "3", ["Silver Lance"]], 
["Soldier", "Halberdier", "15", "1", ["Killer Lance"]], 
["Soldier", "Paladin", "14", "4", ["Steel Axe"]], 
["Soldier", "Paladin", "14", "3", ["Steel Bow"]], 
["Soldier", "Paladin", "14", "1", ["Killer Axe"]],
["Soldier", "Paladin", "14", "1", ["Silver Bow"]], 
["Soldier", "Paladin", "14", "1", ["Brave Bow"]], 
["Soldier", "Paladin", "14", "3", ["Steel Sword", "Vulnerary"]], 
["Soldier", "Paladin", "14", "1", ["Silver Lance", "Vulnerary"]], 
["Soldier", "Paladin", "14", "1", ["Silver Sword", "Vulnerary"]], 
["Soldier", "Paladin", "14", "1", ["Brave Lance", "Vulnerary"]], 
["Soldier", "Paladin", "14", "1", ["Brave Sword", "Vulnerary"]], 
["Soldier", "Paladin", "14", "1", ["Silver Lance", "Iron Axe", "Vulnerary"]], 
["Soldier", "Paladin", "14", "1", ["Killing Edge", "Iron Axe", "Vulnerary"]], 
["Soldier", "Paladin", "14", "1", ["Steel Sword", "Steel Lance", "Vulnerary"]], 
["Soldier", "Paladin", "14", "1", ["Silver Sword", "Iron Axe", "Vulnerary"]], 
["Feral One", "Red Dragon", "17", "3", ["Breath (red)"]], 
["Soldier", "Sage", "13", "1", ["Bolganone"]], 
["Soldier", "Sage", "13", "1", ["Tornado"]], 
["Soldier", "Sage", "13", "1", ["Thoron", "Meteor", "Vulnerary"]],
["Merenary", "Swordmaster", "13", "1", ["Iron Blade"]], 
["Merenary", "Swordmaster", "13", "1", ["Venin Edge", "Vulnerary"]], 
["Merenary", "Swordmaster", "15", "1", ["Silver Sword"]], 
["Merenary", "Swordmaster", "15", "3", ["Silver Blade"]],
["Feral One", "Tiger", "17", "2", ["Claw (tiger)"]], 
["Mercenary", "Warrior", "13", "2", ["Silver Axe"]], 
["[[Bryce]]", "General", "20", "1", ["Wishblade", "Speedwing (drop)", "Guard", "Daunt"]], 
["[[Ashnard]]", "King Daein", "20", "1", ["Gurgurant", "Renewal", "Daunt"]], ]



# Insert reinforcement data. 
# Unit data for reinforcements is formatted the same as enemy data.
# If there are no reinforcements, insert "None".
reinforcement_data = \
None

# Insert note under enemy data.
# If no note is needed, insert "None".
enemy_data_note = None

# Insert whether or not you want to print out the units total. 
# If true, the unit and reinforcements total will print before the chapter page. 
print_units_total = False


# Insert NPC data
# If there are no NPCs, input "None"

# NPC unit data is organized:
#	[name, class, level, quantity, [inventory]]

# ["", "", "", "", [""]], 

npc_data = \
None

# Insert note under enemy data 
# If no note is needed, insert "None".
npc_data_note = None

# Insert the boss name
# If no boss is present, insert "None".

boss_name = "Ashnard"

# Insert boss data
# If no boss is present, insert "None".
detailed_boss_data = """{{Tab
|tab1=Easy/Normal/Hard Mode 1st round
|content1={{BossStats GCN
|portrait=[[File:Small portrait ashnard 01 fe09.png|Ashnard]]
|class=King Daein
|affin=fire
|lv=20
|HP=60
|str=35
|magic=16
|skill=27
|spd=27
|luck=0
|def=35
|res=26
|move=10
|con=14
|wght=49
|inventory=[[File:Is gcn gurgurant.png]] [[Gurgurant]]
|skills=[[File:Is gcn renewal.png]] [[Renewal (skill)|Renewal]]<br>[[File:Is gcn daunt.png]] [[Daunt]]
|sw=S
|ax=A
}}
|tab2=Hard Mode 2nd round
|content2={{BossStats GCN
|portrait=[[File:Small portrait ashnard 02 fe09.png|Ashnard]]
|class=King Daein
|affin=fire
|lv=20
|HP=80
|str=40
|magic=25
|skill=30
|spd=28
|luck=10
|def=35
|res=30
|move=10
|wght=49
|con=14
|inventory=[[File:Is gcn gurgurant.png]] [[Gurgurant]]
|skills=[[File:Is gcn renewal.png]] [[Renewal (skill)|Renewal]]<br>[[File:Is gcn daunt.png]] [[Daunt]]
|sw=S
|ax=A
}}
}}
{{Main|Bryce}}
{{Tab
|tab1=Easy/Normal Mode
|tab2=Hard/Maniac Mode
|content1={{BossStats GCN
|portrait=[[File:Small portrait bryce fe09.png]]
|class=General
|affin=earth
|lv=20
|HP=50
|str=23
|magic=12
|skill=21
|spd=18
|luck=17
|def=25
|res=16
|move=6
|con=13
|wght=18
|sw=A
|la=S
|inventory=[[File:Is gcn wishblade.png]] [[Wishblade]]<br>[[File:Is gcn speedwing.png]] {{drop|Speedwing}}
|skills=[[File:Is gcn guard.png]] [[Cancel|Guard]]<br>[[File:Is gcn daunt.png]] [[Daunt]]
}}
|content2={{BossStats GCN
|portrait=[[File:Small portrait bryce fe09.png]]
|class=General
|affin=earth
|lv=20
|HP=54
|str=28
|magic=13
|skill=26
|spd=18
|luck=17
|def=27
|res=18
|move=6
|con=13
|wght=18
|sw=A
|la=S
|inventory=[[File:Is gcn wishblade.png]] [[Wishblade]]<br>[[File:Is gcn elixir.png]] [[Elixir]]<br>[[File:Is gcn speedwing.png]] {{drop|Speedwing}}
|skills=[[File:Is gcn guard.png]] [[Cancel|Guard]]<br>[[File:Is gcn daunt.png]] [[Daunt]]
}}
}}
"""

# Insert strategy section.
# If "None" is inputted, this section will be marked a stub. 
strategy = None

# Insert trivia section.
trivia = None

# Insert etymology section.
chapter_etymology = """{{Names
|eng-name=Repatriation
|eng-mean=--
|jap-name={{hover|帰還|Kikan}}
|jap-mean=Repatriation
|span-name=El retorno
|span-mean=The return
|fren-name=Rapatriement
|fren-mean=Repatriation
|ger-name=Heimkehr
|ger-mean=Return
|ital-name=Il ritorno
|ital-mean=The return
}}
"""

# Etmology section template for non-localized chapters.
"""{{Names 
|eng-fan-name=
|eng-fan-mean=
|jap-name=
|jap-mean=
}}
"""

# Etmology section template for localized chapters.
"""{{Names 
|eng-name=
|eng-mean=--
|jap-name={{hover||}}
|jap-mean=
|span-name=
|span-mean=
|fren-name=
|fren-mean=
|ger-name=
|ger-mean=
|ital-name=
|ital-mean=
}}
"""

# Insert gallery text.
# If "None" is inputted, this section will be marked a stub. 
gallery_text = None

# Insert chapter navigator.
chapter_navigator_section = \
"""{{ChapterNav
|prechapter=Twisted Tower
|name=Repatriation
}}
"""

# Chapter navigator template.
"""{{ChapterNav
|prechapter=
|prealternate=
|name=
|nextchapter=
|nextalternate=
}}
"""

# Takes every variable above and constructs a chapter page.
chapter_page = build_chapter_page(hatnote, 
								  platform, 
								  chapter_title, 
								  chapter_infobox,
								  game,
								  quote,
								  quote_speaker,
								  chapter_desciption,
								  chapter_plot,
								  beginning_log,
								  chapter_data_box,  
								  return_characters,
								  new_units_data,
								  character_data_note,
								  item_data,
								  item_data_note, 
								  shop_data_header,
								  shops_info,
								  enemy_data,					   
								  reinforcement_data,
								  enemy_data_note,
								  print_units_total,
								  npc_data,
								  npc_data_note,
								  boss_name,
								  detailed_boss_data,
								  chapter_navigator_section, 
								  strategy,
								  trivia, 
								  chapter_etymology,
								  gallery_text, 
								  isStub)

if __name__ == "__main__":
	
	print(chapter_page)
	
	savetoTextFile = False
	
	if savetoTextFile:
		writeTextFile("chapter_page.txt", chapter_page)

