
"""
Written by Albert"Anferensis"Ong

Builds a character data template for fireemblemwiki.org
"""

from utilities import writeTextFile


def build_character_data(game, 
						 new_units_data, 
						 return_characters, 
						 character_data_note):
	
	game_num = game[2:]
	
	character_data = "===Character Data=== \n" + \
					 "{{ChapChars \n" + \
					 "|game#=" + game_num + " \n"
					 
	if new_units_data != None:
		
		number_of_new_units = str(len(new_units_data))
		
		formatted_new_units = "|newunits=" + number_of_new_units + "\n"
		
		for unit_num, new_unit in enumerate(new_units_data, 1):
			
			unit_name = new_unit[0]
			unit_class = new_unit[1]
			unit_HP = new_unit[2]
			unit_level = new_unit[3]
			unit_recruitment = new_unit[4]
			
			if game != "fe09":
				unit_portrait = "[[File:portrait " + unit_name.lower() + " " + game + ".png]]" 
			else:
				unit_portrait = "[[File:Small portrait " + unit_name.lower() + " " + game + ".png]]" 
				
			
			
			new_unit_data = "|newunit" + str(unit_num) +"={{NewUnit \n"
							
			name_line = 	   	"|name=" + unit_name
			portrait_line =     "|portrait=" + unit_portrait
			class_line =  	   	"|class=" + unit_class
			HP_line = 		   	"|HP=" + unit_HP
			level_line = 	   	"|lv=" + unit_level
			recruitment_line = 	"|recruitment method=" + unit_recruitment
			
			
			name_exceptions = {"Ced" : "Ced (character)"}
			
			if unit_name in name_exceptions:
				name_article = name_exceptions[unit_name]
				name_article_line = "|namearticle=" + name_article
				
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
			
		character_data += formatted_new_units
			
					 
	for num, char_name in enumerate(return_characters, 1):
		char_num = str(num)
		char_name = char_name.lower()
		
		char_line = "|return" + char_num + "=" + char_name
		character_data += char_line + "\n"
		
		# A dictionary for cases where the character name
		# is not the same as the link name
		special_cases = {"alva" : "Alva (Thracia 776)", 
						 "robert" : "Robert (Thracia 776)",
						 "ced" : "Ced (character)", 
						 "marth 02" : "Marth", 
						 "lance" : "Lance (character)", 
						 "largo" : "Largo (Path of Radiance)"}
							  
		if char_name in special_cases:
			
			char_article = special_cases[char_name]
			article_line = "|return" + char_num + "article=" + char_article
			
			character_data += article_line + "\n"
		
	
	character_data += "}} \n"
	
	if character_data_note == None:
		pass
	else:
		character_data += character_data_note
	
	return character_data



#========================================================================


def main():
	
	# Insert game
	# 	Such as fe06, fe07, fe08 ....
	game = "fe05"

	# Insert new units data
	# New units data is organized:
	#   ["unit name", "class", "HP", "level", "recruit method"]
	# New unit template: 
	#	["", "", "", "", ""], 

	new_units_data = \
	[["Ronan", "Bow Fighter", "20", "1", "Visit north western [[village]]"], ]

	# Insert returning characters
	return_characters = \
	["Leif", "Finn", "Eyvel", "Orsin", "Halvan", "Marty", "Dagdar", "Tanya"]  

	# Insert character data note
	# If no note is neede, insert "None"
	character_data_note = None


	character_data_section = \
		build_character_data(game, 
						     new_units_data,
							 return_characters, 
						     character_data_note)
						     
	print(character_data_section)
	
	savetoTextFile = False
	
	if savetoTextFile:
		writeTextFile("character_data_section.txt", character_data_section)
							   
							   
if __name__ == "__main__":
	main()
	

