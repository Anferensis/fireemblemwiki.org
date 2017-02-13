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
	
	if character_analysis != None:
		analysis_section = "===Analysis=== \n" + \
						   character_analysis
						   
	else:
		analysis_section = None
	
	#=============================================================
	
	# Building personality section
	
	personality_section = "==Personality and character== \n"
	
	if character_personality == None:
		personality_section += "{{sectstub}} \n"
		
	else:
		personality_section += character_personality
	
	#=============================================================
	
	# Building supports section
	
	if support_data != None:
	
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
	
		
	else:
		supports_section = None
	
	
	#=============================================================
	
	# Building endings section
	
	if character_endings != None:
		endings_section = "===Endings=== \n" + \
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
	
	# Building etymology section
	
	etymology_section = "==Etymology and other languages== \n" + \
						character_etymology
	
	#=============================================================
	
	# Building trivia section
	
	trivia_section = "==Trivia== \n"
	
	if trivia != None:
		trivia_section += trivia
	
	#=============================================================
	
	# Building gallery section
	
	gallery_section = "==Gallery== \n"
	
	
	if gallery == None:
		gallery_section += "{{sectstub}} \n"
		
	else: 
		gallery_section += gallery
		
	sprite_gallery = build_sprite_gallery(character_name, character_type, game, sprite_data)
	
	gallery_section += sprite_gallery
		

	
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
	
	for section in (stub_mark, 
					hatnote_section, 
					character_infobox,
					character_quote, 
					character_description, 
					"=={{FE7}}==",
					role_section, 
					stats_section, 
					analysis_section, 
					personality_section, 
					supports_section,
					endings_section,  
					quotes_section,
					other_appearances_section,
					etymology_section, 
					trivia_section, 
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

game = "fe07"
character_name = "Leila"

# Insert character type
#	either playable, NPC, or boss

character_type = "NPC"

hatnote = None

character_infobox = """{{Character Infobox
|name=Leila
|image=[[File:FERK Leila.png|200px]]
|caption=Artwork of Leila from {{FE7}}
|help_text=
|gender=Female
|race=Human
|age=
|family=
|nationality=[[Ostia|Ostian]]
|titles=
|startingclass=
|voice=
|appearances={{FE7}}
}}
"""

quote = "Find quote"
quote_speaker = "Leila"

character_description = """
'''Leila''' (Japanese: {{hover|レイラ|Reira}} ''Leila'') is non-playable character in {{FE7}}. She is a spy for [[Ostia]] and the lover of [[Matthew]]. 
"""

role = None

character_stats = """
{{CharStats GBA
|portrait=[[File:Portrait leila fe07.png]]
|class=Thief
|affin=wind
|lv=14
|HP=24
|str=14
|skill=20
|spd=20
|luck=8
|def=12
|res=15
|HP1=80
|str1=70
|skill1=65
|spd1=0
|luck1=55
|def1=30
|res1=40
|con=5
|aid=
|move=6
|sw=S
|inventory=[[File:Is gba silver sword.png]] [[Silver Sword]]
|recruit=Leila can not be recruited
}}
<small>*Note: These stats are unused. </small>
"""

"""
{{CharStats GBA
|portrait=[[File:Portrait fe07.png]]
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

|inventory=[[File:Is gba .png]] [[]]<br>
|recruit=
}}
"""

character_analysis = None

character_personality = None

# Insert support data

# Character data is organized:
# 	[name, class, affinity]

character_data = ["Leila", "Thief", "wind"]

# Unit support data is organized:
#	[name, class, affinity, initial points, additional points]

# ["", "", "", "", ""], 

support_data = \
None
				

character_endings = None

# {{Quote||}}

character_quotes = """
"""

character_other_appearances = None

character_etymology = """{{Names
|eng-name=Leila
|eng-mean=
|jap-name={{hover|レイラ|Reira}}
|jap-mean=Leila
|fren-mean=
|ger-name=
|ger-mean=
|span-name=
|span-mean=
|ital-name=
|ital-mean=
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

gallery = """<gallery>
FERK Leila.png|Artwork of Leila from {{FE7}}
</gallery>
"""

sprite_data = \
[["Thief", ["Sword"]]]





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



