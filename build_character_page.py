#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Written by Albert"Anferensis"Ong

Constructs a character page for fireemblemwiki.org
"""

from build_sprite_gallery import build_sprite_gallery


def build_character_page(isStub, 
						 game, 
						 character_name,
						 character_type, 
						 hatnote, 
						 character_infobox, 
						 quote, 
						 quote_speaker, 
						 character_description, 
						 role, 
						 character_stats, 
						 character_analysis, 
						 character_personality, 
						 character_data, 
						 support_data, 
						 character_endings, 
						 character_quotes, 
						 character_other_appearances, 
						 character_etymology, 
						 trivia, 
						 gallery, 
						 sprite_data):
	
	if isStub:
		stub_mark = "{{stub}}"
		
	else:
		stub_mark = ""
		
		
	#=============================================================
	
	# Creating hatnote
	
	if hatnote != None:
		hatnote_section = ":''" + hatnote + "'' \n" + \
						  "----"
						  
	else:
		hatnote_section = None
	
	#=============================================================
	
	# Building character quote
	
	if quote == None or quote_speaker == None:
		character_quote = ""
	else:
		character_quote = "{{Quote|" + quote + "|" + quote_speaker + "}}"
	
	
	#=============================================================
	
	# Building role section
	
	role_section = "===Role=== \n"
	
	if role == None:
		role_section +=  "{{sectstub}}"
		
	else:
		role_section += role
	
	#=============================================================
	
	# Building stats section
	
	stats_section = "===Starting stats and growth rates==="
	
	if character_stats == None:
		stats_section +=  "{{sectstub}} \n"
		
	else:
		stats_section += character_stats
	
	#=============================================================
	
	# Building analysis section
	
	analysis_section = "====Analysis==== \n"
	
	if character_analysis != None:
		analysis_section += character_analysis
		
	else:
		analysis_section += "{{sectstub}}"
	
	#=============================================================
	
	# Building personality section
	
	personality_section = "==Personality and character== \n"
	
	if character_personality == None:
		personality_section += "{{sectstub}} \n"
		
	else:
		personality_section += character_personality
	
	#=============================================================
	
	# Building supports section
	
	if game in ("fe06", "fe07", "fe08") and support_data != None:
	
		supports_section = "==Supports== \n" + \
						   "{{main|" + character_name + "/Supports}} \n"
		
		support_template = ""
		
		character_name = character_data[0]
		character_class = character_data[1]
		character_affinity = character_data[2]
		
		lowered_name = character_name.lower()
		character_portrait = "[[File:portrait " + lowered_name + " " + game + ".png]]"
		
		support_num_line = "|supports=" + str(len(support_data))
		portrait_line =    "|portrait=" + character_portrait
		character_line =   "|character=" + character_name
		class_line = 	   "|class=" + character_class
		affinity_line =    "|affin=" + character_affinity
		
		
		for line in ("{{SupportSysGBA", 
					 support_num_line, 
					 portrait_line,
					 character_line, 
					 class_line, 
					 affinity_line): 
						 
			support_template += line + "\n"
		
		
		for unit_num, unit_data in enumerate(support_data, 1):
			
			unit_num = str(unit_num)
			unit_name = unit_data[0]
			unit_class = unit_data[1]
			unit_affinity = unit_data[2]
			initial_points = unit_data[3]
			additional_points = unit_data[4]
			
			lowered_unit_name = unit_name.lower()
			unit_portrait = "[[File:small portrait " + lowered_unit_name + " " + game + ".png]]"
			
			name_line = 			 "|support" + unit_num + "=" + unit_name
			class_line = 			 "|class" + unit_num + "=" + unit_class
			portrait_line = 		 "|port" + unit_num + "=" + unit_portrait
			affinity_line = 		 "|affin" + unit_num + "=" + unit_affinity
			initial_points_line = 	 "|initialpoints" + unit_num + "=" + initial_points
			additional_points_line = "|plus" + unit_num + "=" + additional_points		
			
			for line in (name_line, 
						 class_line, 
						 portrait_line, 
						 affinity_line, 
						 initial_points_line, 
						 additional_points_line):
				
				support_template += line + "\n"
			
		
		support_template += "}} \n"
		
		supports_section += support_template
	
	elif game == "fe05" and support_data != None:
		pass
	
		
	else:
		supports_section = None
	
	
	#=============================================================
	
	# Building endings section
	
	if character_endings != None:
		endings_section = "==Endings== \n" + \
						   character_endings
						   
	else:
		endings_section = None
	
	#=============================================================
	
	# Building quotes section
	
	quotes_section = "==Quotes== \n"
	
	if character_quotes == None:
		quotes_section += "{{sectstub}} \n"
		
	else:
		quotes_section += character_quotes
	
	#=============================================================
	
	# Building other appearances section
	
	other_appearances_section = "==Other appearances== \n"
	
	if character_other_appearances != None:
		other_appearances_section += character_other_appearances	
	
	
	#=============================================================
	
	# Building trivia section
	
	trivia_section = "==Trivia== \n"
	
	if trivia != None:
		trivia_section += trivia
		
	#=============================================================
	
	# Building etymology section
	
	etymology_section = "==Etymology and other languages== \n" + \
						character_etymology
	
	#=============================================================
	
	# Building gallery section
	
	gallery_section = "==Gallery== \n"

	sprite_gallery = build_sprite_gallery(character_name, character_type, game, sprite_data)
	
	gallery_section += sprite_gallery	
	
	if gallery == None:
		gallery_section += "{{sectstub}} \n"
		
	else: 
		gallery_section += gallery
	
	#=============================================================
	
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
		 "fe15" : "{{Nav15}}", }
						
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
	     "fe15" : "Fire Emblem Echos: Shadows of Valentia",}
	     
	title_name = title_name_dict[game]
	
	character_type_dict = \
		{"playable" : "Playable characters in ", 
		 "NPC" : "NPCs in ", 
		 "boss" : "Bosses in ", }
		 
	category_type = character_type_dict[character_type]
	
	chapter_category = "[[Category:" + category_type + title_name + "]]"
	
	#=============================================================
	
	# Building final character page
	
	character_page = ""
	
	character_appearance_dict = \
		{"fe01" : "{{FE1}}", 
		 "fe02" : "{{FE2}}", 
		 "fe03" : "{{FE3}}",
		 "fe04" : "{{FE4}}",
		 "fe05" : "{{FE5}}",
		 "fe06" : "{{FE6}}", 
		 "fe07" : "{{FE7}}", 
		 "fe08" : "{{FE8}}", 
		 "fe09" : "{{FE9}}", 
		 "fe10" : "{{FE10}}", 
		 "fe11" : "{{FE11}}", 
		 "fe12" : "{{FE12}}", 
		 "fe13" : "{{FE13}}", 
		 "fe14" : "{{FE14}}", 
		 "fe15" : "{{FE15}}", }
		 
	character_appearance_title = character_appearance_dict[game]
	character_appearance_line = "==" + character_appearance_title + "=="
	
	for section in (stub_mark, 
					hatnote_section, 
					character_infobox,
					character_quote, 
					character_description, 
					character_appearance_line,
					role_section, 
					stats_section, 
					analysis_section, 
					personality_section, 
					supports_section,
					endings_section,  
					quotes_section,
					other_appearances_section,
					trivia_section, 
					etymology_section, 				
					gallery_section, 
					"{{ref}}",
					"{{Project Characters}}", 
					chapter_nav, 
					chapter_category):
		
		if section != None:
			character_page += section + "\n"
		
	return character_page
	
	


#===================================================

isStub = True

game = "fe05"
character_name = "Robert (Thracia 776)"

# Insert character type
#	either playable, NPC, or boss

character_type = "playable"

hatnote = None

character_infobox = """{{Character Infobox
|name=Robert
|image=[[File:FE776 Robert.png|200px]]
|caption=Artwork of Robert from {{title|Thracia 776}}. 
|help_text=
|gender=Male
|race=Human
|age=17<ref>{{Cite web|retrieved=11 April, 2017|url=https://www.nintendo.co.jp/n02/shvc/bfej/data/chara/index.html|title=Character ～登場人物の紹介～|site=ファイアーエムブレム　トラキア７７６}}</ref>
|family=
|nationality=[[Leonster]]
|titles=
|startingclass=[[Arch Knight]]
|voice=
|appearances=*{{title|Thracia 776}}
}}
"""

#<ref>{{Cite web|retrieved=11 April, 2017|url=https://www.nintendo.co.jp/n02/shvc/bfej/data/chara/index.html|title=Character ～登場人物の紹介～|site=ファイアーエムブレム　トラキア７７６}}</ref>

quote = None
quote_speaker = None

character_description = """
'''Robert''' (Japanese: {{hover|ロベルト|Roberuto}} ''Robert'') is a playable [[arch knight]] in {{FE5}}.
"""

role = None

character_stats = """
{{CharStats FE5
|portrait=[[File:Portrait robert fe05.png]]
|class=Arch Knight
|lv=1
|HP=23
|movestars=★
|authority=
|move=8{{hover|-3|while dismounted}}
|str=5
|magic=0
|skill=4
|spd=8
|luck=6
|def=4
|PCC=3
|build=7
|aid=
|bo=E
|inventory=[[File:Is snes03 iron bow.png]] [[Iron Bow]]<br>
|skills=
|recruit=[[The Emblem of Noba|Chapter 9: The Emblem of Noba]], Automatically at the start
|HP1=65
|str1=45
|magic1=10
|skill1=50
|spd1=60
|luck1=70
|def1=25
|build1=20
|move1=1
}}

===Promotion gains===
{{PromotionGains
|class=[[Bow Knight]]
|hp=0
|str=2
|mag=1
|skill=3
|spd=2
|def=2
|con=1
|move=1
|weaponlvl={{BowSNES}}+1
}}
"""


# Blank character stats template

# GBA titles
"""
{{CharStats GBA
|portrait=[[File:Portrait fe06.png]]
|class=
|affin=
|lv=
|HP=
|str=
|skill=
|spd=
|luck=
|def=
|res=
|HP1=
|str1=
|skill1=
|spd1=
|luck1=
|def1=
|res1=
|con=
|aid=
|move=

|inventory
|recruit=
}}
"""

# Thracia 776
# ★★★★★

"""
{{CharStats FE5
|portrait=[[File:Portrait fe05.png]]
|class=
|lv=
|HP=
|movestars=★★★★★
|authority=★★★★★
|move=
|str=
|magic=
|skill=
|spd=
|luck=
|def=
|PCC=
|build=
|aid=

|inventory=[[File:Is snes03 .png]] [[]]<br>
|skills=[[File:Is snes03 .png]] [[]]<br>
|recruit=
|HP1=
|str1=
|magic1=
|skill1=
|spd1=
|luck1=
|def1=
|build1=
|move1=
}}
"""


# Blank promotion gains templates

"""
(GBA titles)
===Promotion gains===
{{PromotionGains
|class= 
|hp=
|str=
|skill=
|spd=
|def=
|res=
|con=
|move=
|weaponlvl=
}}

(Thracia 776)
===Promotion gains===
{{PromotionGains
|class=[[]]
|hp=
|str=
|mag=
|skill=
|spd=
|def=
|con=
|move=
|weaponlvl=
}}
"""

character_analysis = None

character_personality = None

# Insert support data

# Character data is organized:
# 	[name, class, affinity]

character_data = ["Xavier", "General", None]

# GBA unit support data is organized:
#	[name, class, affinity, initial points, additional points]

# Fire Emblem: Thracia 776 unit support data is organized:
#	[name, class, support bonus]

# ["", "", "", "", ""], 

support_data = \
None
				

character_endings = """
'''Robert – Bow Knight of Leonster'''<br>
After his strong requests, Robert was put in the new Kingdom of Thracia’s royal guard. Robert himself was probably trying his best to be a legendary warrior, but he never could fix his timidity. Apparently, more than a few of the female servants in the castle found his sheepish nature cute.
"""

# {{Quote||}}

character_quotes = """
===Death quotes===
{{Quote|Lady Selphina… I wish…I could be of more…use…|Robert}}

===Escape quotes===
{{Quote|Next time…we won’t lose.|Robert}}
"""

character_other_appearances = None

character_etymology = """{{Names
|eng-fan-name=Robert
|eng-fan-mean=--
|jap-name={{hover|ロベルト|Roberuto}}
|jap-mean=
}}
"""

"""{{Names
|eng-name=
|eng-mean=
|jap-name=
|jap-mean=
|fren-mean=
|ger-name=
|ger-mean=
|span-name=
|span-mean=
|ital-name=
|ital-mean=
}}
"""

trivia = None
# Sprite data is organized:
#	[class name, [weapon1, weapon2, weapon3]]

# ["", [""]], 

sprite_data = \
[["Arch Knight", ["Bow", "Bow"]], 
["Bow Knight", ["Bow", "Bow"]],  ]

gallery = """<gallery>
FE776 Robert.png|Artwork of Robert from {{FE5}}.
</gallery>
"""



print(build_character_page(isStub, 
						   game, 
						   character_name, 
						   character_type, 
						   hatnote, 
						   character_infobox, 
						   quote, 
						   quote_speaker, 
						   character_description, 
						   role, 
						   character_stats, 
						   character_analysis, 
						   character_personality, 
						   character_data, 
						   support_data, 
						   character_endings, 
						   character_quotes, 
						   character_other_appearances, 
						   character_etymology, 
						   trivia, 
						   gallery, 
						   sprite_data))



