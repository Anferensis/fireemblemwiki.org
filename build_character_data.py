
"""
Written by Albert"Anferensis"Ong

Builds a character data template for fireemblemwiki.org

Revision: 27.12.2018
"""

from utilities import writeTextFile


# A dictionary for cases where a character's name is not the 
# same as a character's page name. 
link_exceptions = \
	{"Alva"               : "Alva (Thracia 776)", 
	 "Ced"                : "Ced (character)", 
	 "Marth 02"           : "Marth", 
   "Micaiah_light_mage" : "Micaiah", 
	 "Lance"              : "Lance (character)", 
	 "Largo"              : "Largo (Path of Radiance)", 
	 "Robert"             : "Robert (Thracia 776)", 
   "Sothe_rogue"        : "Sothe"}

def build_character_template(game, 
							 new_units_data, 
							 return_characters):
	""" A function designed to build an individual character data
	template for fireemblemwiki.org. 
	"""
	
	character_template = \
		"{{ChapChars \n" + \
		"|game#=" + game[2:] + " \n"
	
	
	# Formatting the new units, if there are any. 				 
	if new_units_data != None:
		
		number_of_new_units = str(len(new_units_data))
		formatted_new_units = "|newunits=" + number_of_new_units + "\n"
		
		for unit_num, new_unit in enumerate(new_units_data, 1):
			
			unit_name = new_unit[0]
			unit_class = new_unit[1]
			unit_HP = new_unit[2]
			unit_level = new_unit[3]
			unit_recruitment = new_unit[4]
			
			lowered_name = unit_name.lower()
			
			if game == "fe02":
				unit_portrait = "[[File:Portrait " + lowered_name + " " + game + ".png]]"
			
			elif game == "fe09":
				unit_portrait = "[[File:Small portrait " + lowered_name + " " + game + ".png]]" 	
				
			elif game == "fe15":
				unit_portrait = "[[File:Portrait " + lowered_name + " status " + game + ".png|128px]]" 	
				
			else:
				unit_portrait = "[[File:Small portrait " + lowered_name + " " + game + ".png]]" 
				
			
			
			new_unit_data = "|newunit" + str(unit_num) +"={{NewUnit \n"
							
			name_line = 	   	"|name=" + unit_name
			portrait_line =     "|portrait=" + unit_portrait
			class_line =  	   	"|class=" + unit_class
			HP_line = 		   	"|HP=" + unit_HP
			level_line = 	   	"|lv=" + unit_level
			recruitment_line = 	"|recruitment method=" + unit_recruitment
			
			
			# If the name of the character is different from the name 
			# of the aritcle...
			if unit_name in link_exceptions:
				
				# Adds an additional line to link the correct acticle. 
				name_article = name_exceptions[unit_name]
				name_article_line = "|namearticle=" + name_article
			
			# Otherwise, assigns the line to "None"
			else:
				name_article_line = None
			
			
			for line in (name_line, 
						 name_article_line, 
						 portrait_line, 
						 class_line, 
						 HP_line, 
						 level_line, 
						 recruitment_line):
				
				if line != None:
					new_unit_data += line + "\n"
			
				
			new_unit_data += "}}" + "\n"
				
			formatted_new_units += new_unit_data
			
		character_template += formatted_new_units
			
	
	# Formatting the return characters, if there are any. 
	if return_characters != None:	
		
		# Uses a for loop to add all returning characters. 			 
		for num, char_name in enumerate(return_characters, 1):
			
			char_num = str(num)
			
			if char_name == "Celica" and game == "fe02":
				char_portrait = "celica 01"
			else:
				char_portrait = char_name.lower()
			
			char_line = "|return" + char_num + "=" + char_portrait
			character_template += char_line + "\n"
			
								  
			if char_name in link_exceptions:
				
				char_article = link_exceptions[char_name]
				article_line = "|return" + char_num + "article=" + char_article
				
				character_template += article_line + "\n"
				
			elif char_name == "Celica" and game == "fe02":
				article_line = "|return" + char_num + "article=Celica"
				
				character_template += article_line + "\n"
	
	character_template += "}} \n"
	
	return character_template



def build_character_data(character_data, 
						 character_data_note):
	
	character_data_section = "===Character data=== \n"
	
	number_of_tabs = len(character_data)
	
	if number_of_tabs == 1:
		
		game = character_data[0][1]
		new_units_data = character_data[0][2]
		return_characters = character_data[0][3]
		
		character_template = build_character_template(game, 
													  new_units_data, 
													  return_characters)
	
		character_data_section += character_template 
	
	elif number_of_tabs > 1:
		
		tabs = "{{Tab \n" + \
			   "|width=1000px \n"
		
		for tab_num, tab_data in enumerate(character_data, 1):
			
			tab_num = str(tab_num)
			tab_name = tab_data[0]
			tab_name_line = "|tab" + tab_num + "=" + tab_name + "\n"
			
			tabs += tab_name_line
			
		
		for tab_num, tab_data in enumerate(character_data, 1):
			
			tab_num = str(tab_num)
			tab_content = "|content" + tab_num + "="
			
			game = tab_data[1]
			character_data = tab_data[2]
			return_characters = tab_data[3]
			
			character_template = build_character_template(game, 
														  character_data, 
														  return_characters)
														  
			tab_content += character_template
			tabs += tab_content
			
		character_data_section += tabs + "}} \n"
	
	
	# If the character data note does not equal "None".
	if character_data_note != None:
		
		# Add the character note to the character data section. 
		character_data_section += character_data_note
	
	
	return character_data_section
	


#========================================================================


def main():
	
	"""
	Insert character data. 
	
	Character data is formatted: 
	[tab_name, 
	 game, 
	 new units data, 
	 returning characters]
	 
	Tab name is for cases where you want more than one tab. 
	If one one tab is needed, input "None". 
	
	Game refers to a tab's game number. 
	Such as fe01, fe02, fe03...
	
	New units data is the data for all new units in a chapter. 
	Such as [unit_data1, unit_data2, unit_data3 ...]
	
	Individual new unit data is formatted:
	   ["unit name", "class", "HP", "level", "recruit method"]
	New unit template: 
		["", "", "", "", ""], 
		
	Returning characters is a list of names of returning characters. 
	Such as [character1, character2, character3,....]
	"""
	
	character_data = \
		[
      # Tab data. 
      [None, 
       "fe10", 
       
       # New character data. 
       [["Meg", "Armored Sword", "21", "3", "View base conversation 'In Town'"], ], 
       
      # Returning characters. 
      ["Micaiah_light_mage", "Sothe_rogue", "Edward", "Leonardo", "Nolan", "Laura", "Ilyana", "Aran"]], 
    ]
	
	"""
	Insert a character data note. 
	If no note is needed, insert "None". 
	
	This is for cases where you want a text note below the
	character data section. 
	"""
	character_data_note = None
	
	
	
	character_data_section = build_character_data(character_data, 
												  character_data_note)
	
	# Prints out the character data section. 
	print(character_data_section)
	
	savetoTextFile = False
	
	if savetoTextFile:
		writeTextFile("character_data_section.txt", character_data_section)
							   
							   
if __name__ == "__main__":
	main()
	
