#!/usr/bin/env python
# -*- coding: utf-8 -*- 

"""
Written by Albert"Anferensis"Ong
A program designed to build a chapter page for fireemblemwiki.org.

Note: This program has only been tested for Fire Emblem 5, 6, 7, 8, and 9.
	  It may not function properly for other titles. 
	  
Revision: 12-27-2017
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
					   insert_plot_section,
					   chapter_plot,
					   beginning_log,
					   chapter_data_infobox,  
					   character_data, 
					   character_data_note,
					   item_data,
					   item_data_note,
					   shop_data_header,
					   shops_info,
					   include_enemy_data, 
					   enemy_data,					   
					   reinforcement_data,
					   enemy_data_note,
					   print_units_total,
					   npc_data,
					   npc_data_note,
					   boss_name,
					   detailed_boss_data,
					   chapter_navigator_section, 
					   include_strategy_section, 
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
	
	if insert_plot_section:
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
			
	else:
		plot_section = None
	
	#===================================================================
	
	# Building chapter data
	
	chapter_data = chapter_data_infobox
		
	#===================================================================
	
	# Building character data section
	
	character_data_section = \
		build_character_data(character_data, 
							 character_data_note)
					   
	#===================================================================
	
	# Building item data. 
	
	item_data_section = build_item_data(item_data, 
										item_data_note)
	
	#===================================================================
	
	# Building shop data
	shop_data_section = build_shop_data(platform, 
										game, 
										shops_info, 
										shop_data_header)
	
	#===================================================================
	
	# Building enemy data
	
	if include_enemy_data:
		enemy_data_section = build_enemy_data(platform, 
											  enemy_data, 
											  reinforcement_data, 
											  enemy_data_note,
											  print_units_total)
											  
	else:
		enemy_data_section = None
	
	#===================================================================
	
	# Building NPC data section
	npc_data_section = build_npc_data(npc_data, 
									  npc_data_note)
							  
	#===================================================================
	
	# Building boss data
	
	if boss_name != None:
		boss_redirect_line = "{{Main|" + boss_name + "}}"
		
	else:
		boss_redirect_line = None
	
	
	boss_data_section = ""
						
	for line in ("===Boss data===", 
				 boss_redirect_line, 
				 detailed_boss_data):
					 
		if line != None:
			boss_data_section += line + "\n"
			
		else:
			boss_data_section = None
											    
	#===================================================================
	
	# Building strategy section
	
	if include_strategy_section:
		
		if strategy != None:
			strategy_body = "{{strategy}} \n" + \
							   strategy
			
		else:
			strategy_body = "{{sectstub}}"
			
		strategy_section = ""
		
		for line in ("==Strategy==", 
					 strategy_body):
						 
			strategy_section += line + "\n"
			
	else:
		strategy_section = None
		
	#===================================================================
	
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
		
	#===================================================================
	
	# Building etymology section
	
	etymology_section = "==Etymology and other languages== \n" + \
						chapter_etymology
		
	#===================================================================
	
	# Building gallery section
	
	gallery_section = "==Gallery== \n"
	
	if gallery_text == None:
		gallery_section_text = "{{sectstub}}"
		
	else:
		gallery_section_text = gallery_text
		
	gallery_section += gallery_section_text + "\n"
	
	#===================================================================
	
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
	
	if chapter_navigator_section != None:
	
		if game in ("fe02", "fe15"):
			chapter_nav = "{{Nav2}} \n{{Nav15}}"
		else:
			chapter_nav = chapter_nav_dict[game]
			
	else:
		chapter_nav = None
	
	title_name_dict = \
		{"fe01" : "Fire Emblem: Shadow Dragon and the Blade of Light",
		 "fe02" : "Fire Emblem Gaiden",
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
	     "fe15" : "Fire Emblem Echoes: Shadows of Valentia"}
	     
	title_name = title_name_dict[game]
	
	if game in ("fe02", "fe15"):
		chapter_category = "[[Category:Acts of Fire Emblem Gaiden]] \n" + \
						   "[[Category:Acts of Fire Emblem Echoes: Shadows of Valentia]]"
	else:
		chapter_category = "[[Category:Chapters of " + title_name + "]]"

	#===================================================================
	
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

#=======================================================================

# Insert whether or not the page is a stub.
isStub = True


# Insert platform name
platform = "nes02"

# Insert the game number
# Such as fe01, fe02, fe03 ...
game = "fe02"

# Insert chapter title
chapter_title = "Seabound Shrine"

# Insert chapter infobox
chapter_infobox = \
"""{{Chapter Infobox 
|title=Seabound Shrine
|image=[[File:Cm fe02 C2 M07.png|200px]]
|location=Seabound Shrine
|new units=None
|boss=None
}}"""

# Chapter infobox template
"""{{Chapter Infobox 
|title=
|image=[[File:Cm fe __ __.png|200px]]
|location=
|new units=
|boss=
|weather=
}}"""


# Insert a quote and the quote's speaker. 
# This is primarily for aesthetic purposes. 

# If "None" is inputted for either the quote or quote speaker,
# then a quote will not appear

quote = None
quote_speaker = None


# Insert chapter description. 
chapter_desciption = \
"""'''Seabound Shrine''' (Japanese: {{hover|海のほこら|Umi no hokora}} ''Sea Shrine'') is the seventh map of the second act of {{FE2}} and {{FE15}}.
"""

#=======================================================================

# Insert if this page needs a plot section. 
insert_plot_section = False

# Insert chapter plot.
# If "None is inputted", this section will be marked as a stub.
chapter_plot = None

# Insert beginning log
# If there is no beginning log, insert "None"
beginning_log = \
None

#=======================================================================

# Insert chapter infobox data.
chapter_data_box = \
"""==Map data==
{{ChapDataMap
|victory=Rout enemy
|defeat=[[Celica]] dies
|ally=8
|other=0
|enemy={{hover|10|Gaiden}}/{{hover|7|Echoes: Shadoes of Valentia}}
|map=[[File:Cm fe02 C2 M06.png]]
}}
"""

# Chapter databox template. 
"""{{ChapDataMap
|victory=
|defeat=
|ally=
|other=
|enemy=
|map=
}}
"""

#=======================================================================

# Insert character data.

# For full instructions on how to format character_data,  
# see build_character_data.py. 

character_data = \
[["''Gaiden''", 
 "fe02", 
 None,
 ["Celica", "Mae", "Boey", "Genny", "Saber", "Valbar", "Kamui", "Leon"]], 
 
 ["''Echoes: Shadows of Valentia''", 
  "fe15", 
  None,
  ["Celica", "Mae", "Boey", "Genny", "Saber", "Valbar", "Kamui", "Leon"]]
  ]


# Insert a text note under the character data .
# If no note is needed, insert "None".
character_data_note = \
None

#=======================================================================

# Insert item data

# For full instructions on how to format item_data,  
# see build_item_data.py. 

item_data = \
"stub"


# Insert note after under item data. 
# If no note is needed, insert "None".
item_data_note = \
None

#=======================================================================

shop_data_header = "Shop Data"

# Insert shop data. 
# If there are no shops, input "None"

# Shop info is formatted:
#	[shop name, [item1, item2, item3]], 

# ["", ["", "", ""]], 

shops_info = \
None

#=======================================================================

# Insert if this page needs enemy data. 
include_enemy_data = True

# Insert enemy data. 

# Unit data is formatted:
# 	[name, class, level, quantity, inventory]

# ["", "", "", "", None], 

enemy_data = \
[["Bonewalker", "Bonewalker", "1", "2", None], 
["Revenant", "Revenant", "1", "8", None], ]

# Insert reinforcement data. 
# Unit data for reinforcements is formatted the same as enemy data.
# If there are no reinforcements, insert "None".
reinforcement_data = \
None

# Insert note under enemy data.
# If no note is needed, insert "None".
enemy_data_note = \
"""====''Echoes: Shadows of Valentia''====
{{sectstub}}
"""

# Insert whether or not you want to print out the units total. 
# If true, the unit and reinforcements total will print before the chapter page. 
print_units_total = False

#=======================================================================

# Insert NPC data

# For full instructions on how to format npc_data,  
# see build_npc_data.py. 

npc_data = \
None

# Insert a text note under enemy data. 
# If no note is needed, insert "None".
npc_data_note = None

#=======================================================================

# Insert the boss name
# If no boss is present, insert "None".

boss_name = None

# Insert boss data
# If no boss is present, insert "None".
detailed_boss_data = None

#=======================================================================

# Insert if the page needs a strategy section. 
include_strategy_section = True

# Insert strategy section.
# If "None" is inputted, this section will be marked a stub. 
strategy = None

#=======================================================================

# Insert trivia section.
# If "None" is inputted, this section will be left blank. 
trivia = None

#=======================================================================

# Insert etymology section.
chapter_etymology = """{{Names 
|eng-name=Seabound Shrine
|eng-mean=--
|jap-name={{hover|海のほこら|Umi no hokora}}
|jap-mean=Sea Shrine
|span-name=Santuario marino
|span-mean=Marine sanctuary
|fren-name=Sanctuaire marin
|fren-mean=Marine sanctuary
|ger-name=Tempel am Meer
|ger-mean=Temple by the Sea
|ital-name=Tempio del Mare
|ital-mean=Temple of the Sea
|dut-name=Zeekapel
|dut-mean=Sea shrine
|ch-name={{hover|海的祠堂|Mandarin: Hǎi de cítáng; Cantonese: Hoi dik chitong}}
|ch-mean=Sea temple
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
|dut-name=
|dut-mean=
|ch-simp-name={{hover||Mandarin: ; Cantonese: }}
|ch-simp-mean=
|ch-trad-name={{hover||Mandarin: ; Cantonese: }}
|ch-trad-mean=
}}
"""

#=======================================================================

# Insert gallery text.
# If "None" is inputted, this section will be marked a stub. 
gallery_text = None

#=======================================================================

# Insert chapter navigator.
chapter_navigator_section = \
None

# Chapter navigator template.
"""{{ChapterNav
|prechapter=
|prealternate=
|name=
|nextchapter=
|nextalternate=
}}
"""

#=======================================================================

# Takes every variable above and constructs a chapter page.
chapter_page = build_chapter_page(hatnote, 
								  platform, 
								  chapter_title, 
								  chapter_infobox,
								  game,
								  quote,
								  quote_speaker,
								  chapter_desciption,
								  insert_plot_section,
								  chapter_plot,
								  beginning_log,
								  chapter_data_box,  
								  character_data, 
								  character_data_note,
								  item_data,
								  item_data_note, 
								  shop_data_header,
								  shops_info,
								  include_enemy_data, 
								  enemy_data,					   
								  reinforcement_data,
								  enemy_data_note,
								  print_units_total,
								  npc_data,
								  npc_data_note,
								  boss_name,
								  detailed_boss_data,
								  chapter_navigator_section, 
								  include_strategy_section, 
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

