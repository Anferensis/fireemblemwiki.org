
"""
Written by Albert"Anferensis"Ong

Constructs an enemy data table for fireemblemwiki.org

Revision: 12-27-2017
"""

from utilities import hyperlink, writeTextFile
from build_unit_inventory import build_unit_inventory


def build_units_data(platform,
					 units_data,
					 isReinforcement = False):
					 
	formatted_units_data = ""
	
	for unit_num, unit_data in enumerate(units_data, 1):
		
		is_last_unit = unit_num == len(units_data)
		
		if unit_num == len(units_data):
			unit_num = "l"
		else:
			unit_num = str(unit_num)
		
		unit_name = unit_data[0]
		unit_class = unit_data[1]
		unit_level = unit_data[2]
		unit_quantity = unit_data[3]
		unit_inventory = unit_data[4]
											  
		name_line_start = "|name"
		class_line_start = "|class"
		level_line_start = "|lv"
		quantity_line_start = "|#"
		
		isLastReinforcement = False
		
		add_letter = ""
		
		if isReinforcement:
			
			add_letter = "r"
			
			if unit_num == "b":
				isLastReinforcement = True
				add_letter = "rl"

			name_line_start += add_letter
			class_line_start += add_letter
			level_line_start += add_letter
			quantity_line_start += add_letter
			
						
					
		if isLastReinforcement:		
			unit_num = ""	
			inventory_line = build_unit_inventory(platform, 
												  unit_inventory, 
												  unit_num, 
												  isReinforcement,
												  True)											  
		else:
			inventory_line = build_unit_inventory(platform, 
												  unit_inventory, 
												  unit_num, 
												  isReinforcement)	
											  
		name_line =     name_line_start + unit_num + "=" + unit_name
		class_line =    class_line_start + unit_num + "=" + unit_class
		level_line =    level_line_start + unit_num + "=" + unit_level
		quantity_line = quantity_line_start + unit_num + "=" + unit_quantity
		
		
		# A dictionary for cases where the class name if different
		# from the class page. 
		unit_class_exceptions = \
			{"Raven" : "Raven (laguz)"}
		
		if unit_class in unit_class_exceptions:
			
			class_link = unit_class_exceptions[unit_class]
			class_article_line = "|class" + add_letter + unit_num + "article=" + class_link
		
		else:
			class_article_line = None	
		
		if unit_num == "b":
			quantity_line = None
											  
		formatted_unit_data = ""	
		
		for line in (name_line, 
					 class_line, 
					 class_article_line,
					 level_line, 
					 quantity_line, 
					 inventory_line):
			
			if line != None:		 
				formatted_unit_data += line
				
				if not is_last_unit:
					formatted_unit_data += "\n"
					
				elif is_last_unit and line != inventory_line:
					formatted_unit_data += "\n"
				
		formatted_units_data += formatted_unit_data

		
		if not is_last_unit:
			formatted_units_data += "\n"


	
	return formatted_units_data
	


def build_enemy_data(platform, 
					 enemy_data, 
					 reinforcement_data, 
					 enemy_data_note,
					 print_units_total = False):
						 
	# Prints out the units total. 
	if print_units_total:
		
		enemy_total = 0
		
		for unit_data in enemy_data:
			unit_quantity = int(unit_data[3])
			enemy_total += unit_quantity
			
		reinforcement_total = 0
		
		if reinforcement_data != None:
			for unit_data in reinforcement_data:
				reinforcement_quantity = int(unit_data[3])
				reinforcement_total += reinforcement_quantity
			
		print("Enemy total: ", enemy_total)
		print("Reinforcement total: ", reinforcement_total)	
	
	
	
	formatted_units_data = build_units_data(platform, enemy_data)

	if reinforcement_data != None:
		formatted_reinforcement_data = build_units_data(platform, 
														reinforcement_data, 
														True)
	else:
		formatted_reinforcement_data = None	
	
		
	enemy_data_section = ""
	
	for section in ("===Enemy data===", 
					"{{ChapEnemies", 
					"|platform=" + platform, 
					formatted_units_data,
					formatted_reinforcement_data,
					"}}" ):	
		
		if section != None:		
			enemy_data_section += section + "\n"
	
		 
	if enemy_data_note != None:
		enemy_data_section += enemy_data_note
	
	return enemy_data_section
	
	
	
#======================================================================



def main():
	
	# Insert platform name
	# Such as gba, gcn, or wii
	platform = "3ds03"

	# Unit data is formatted:
	# 	[name, class, level, quantity, [inventory items]]

	# Example: ["Bandit", "Brigand", "1", "1", ["Iron Axe", "Vulnerary"]]
	# Template: ["", "", "", "", None], 

	enemy_data = \
	[["Cantor", "Cantor", "5", "1", ["Fruit of Life (drop)", "Miasma", "Incarnation"]],]
	
	# ["Revenant", "Revenant", "1", "varies", None]
	
	# Insert reinforcement data.
	# Unit data is formatted the same as with the enemy data above. 
	# 	If there are no reinforcements, insert "None"
	
	reinforcement_data = \
	None

	# Insert enemy data note.
	# If no note is needed, insert "None".
	enemy_data_note = None
	
	# Insert whether or not you want to print out the units total.
	print_units_total = False

	enemy_data_section = build_enemy_data(platform, 
										   enemy_data, 
										   reinforcement_data, 
										   enemy_data_note, 
										   print_units_total)
										   
	print(enemy_data_section)
						   
	savetoTextFile = False
	
	if savetoTextFile:
		writeTextFile("enemy_data_section.txt", enemy_data_section)
						   

if __name__ == "__main__":
	main()


"""
===Enemy data===
{{Tab
|width=1000px
|tab1=''Gaiden''
|tab2=''Echoes: Shadows of Valentia''
|content1={{ChapEnemies
|platform=nes02
|namel=Cantor
|classl=Cantor
|lvl=1
|#l=1
|inventoryl=--
}}
|content2={{ChapEnemies
|platform=3ds03
|namel=Cantor
|classl=Cantor
|lvl=5
|#l=1
|inventoryl=[[File:Is 3ds03 fruit of life.png]]{{drop|Fruit of Life}}[[File:Is 3ds03 black magic.png]][[Miasma]][[File:Is 3ds03 skill class.png]][[Incarnation]]
}}
}}
"""



