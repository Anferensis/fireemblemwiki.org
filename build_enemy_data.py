
"""
Written by Albert"Anferensis"Ong

Constructs an enemy data table for fireemblemwiki.org

Revision: 05-28-2017
"""

from utilities import hyperlink, writeTextFile
from build_unit_inventory import build_unit_inventory


def build_units_data(platform,
					 units_data,
					 isReinforcement = False):
	"""
	A function that formats the units data. 
	This is used in build_enemy_template. 
	"""
	
	# A string that will become the formatted units data. 				 
	formatted_units_data = ""
	
	# Uses a for loop to examine each, individual unit's data. 
	for unit_num, unit_data in enumerate(units_data, 1):
		
		# Checks if the unit is the last unit in the list. 
		is_last_unit = unit_num == len(units_data)
		
		if unit_num == len(units_data):
			unit_num = "b"
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
			{"Raven" : "Raven (laguz)", 
			 "White Dragon" : "White Dragon (monster)"}
		
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


		# Adds a space between each unit's data if it is not the last unit. 
		if not is_last_unit:
			formatted_units_data += "|-\n"


	
	return formatted_units_data
	


def build_enemy_template(platform, 
						 enemy_data, 
						 reinforcement_data, 
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
	
	#-------------------------------------------------------------------
	
	formatted_units_data = build_units_data(platform, enemy_data)
	
	if reinforcement_data != None:
		formatted_reinforcement_data = build_units_data(platform, 
														reinforcement_data, 
														True)
	else:
		formatted_reinforcement_data = None	
		
	enemy_template = ""
	
	for section in ("{{ChapEnemies", 
					"|platform=" + platform, 
					formatted_units_data,
					formatted_reinforcement_data,
					"}}" ):	
		
		if section != None:		
			enemy_template += section + "\n"	
	
	return enemy_template



def build_enemy_data(enemy_data, 
					 enemy_data_note,
					 print_units_total):
	
	
	number_of_tabs = len(enemy_data)
	
	# If there is only one tab in the enemy data...
	if number_of_tabs == 1:
		
		tab_data = enemy_data[0]
		
		platform = tab_data[0]
		initial_enemy_data = tab_data[2]
		reinforcement_data = tab_data[3]
		
		enemy_data_template = \
			build_enemy_template(platform, 
								 initial_enemy_data, 
								 reinforcement_data, 
								 print_units_total)
			
		enemy_data_section = \
			"===Enemy data===\n" + \
			 enemy_data_template
	 
	 
	# If there is more than one tab in the enemy data...						 
	elif number_of_tabs > 1:
		
		enemy_data_section = \
			"===Enemy data===\n" + \
			"{{Tab\n" + \
			"|width=1000px\n"
		
		
		# Adds the tab names
		for tab_num, tab_data in enumerate(enemy_data, 1):
			
			tab_num = str(tab_num)
			tab_name = tab_data[1]
			
			tab_line = "|tab" + tab_num + "=" + tab_name + "\n"
			enemy_data_section += tab_line
		   
		 
		# Adds the tab contents. 
		for tab_num, tab_data in enumerate(enemy_data, 1):
			
			tab_num = str(tab_num)
			
			platform = tab_data[0]
			initial_enemy_data = tab_data[2]
			reinforcement_data = tab_data[3]
			
			enemy_data_template = \
				build_enemy_template(platform, 
									 initial_enemy_data, 
									 reinforcement_data, 
									 print_units_total)
									 
			tab_content = "|content" + tab_num + "=" + enemy_data_template
			
			enemy_data_section += tab_content
			
			try:
				tab_note = tab_data[4]
				enemy_data_section += tab_note + "\n"
				
			except IndexError:
				pass
			
		enemy_data_section += "}}\n"

	
	# Adds the enemy data note to the enemy data section, 
	# if a note exists. 	 
	if enemy_data_note != None:
		enemy_data_section += enemy_data_note
	
	# Returns the finalized enemy_data_section
	return enemy_data_section


	
#======================================================================



def main():
	
	"""
	Input enemy data below.
	
	Enemy data is formatted:
		[[platform1, 
		  tab name2, 
		  initial_enemy_data1, 
		  reinforcement_data1, ] 
		
		 [platform2, 
		  tab name2, 
		  initial_enemy_data2, 
		  reinforcement_data2 ] 
		  
		  ... (for as many tabs as needed) 
		  ]
	 
	
	Initial enemy data and reinforcement data is formatted:
	
		[unit1, 
		 unit2, 
		 unit3,  
		 ... 	(for as many units as needed)
		 ]
	
	Unit data is formatted:
		[name, class, level, quantity, [item1, item2, ...]]
	Example:
		["Bandit", "Brigand", "1", "1", ["Iron Axe", "Vulnerary"]]
	Template:
		["", "", "", "", None], 
	
	
	Enemy data template:
		[["", 
		  "", 
		  [], 
		  None],
		 
		 ["", 
		  "", 
		  [], 
		  None]]
	"""
	
	
	enemy_data = \
	[["nes02", 
	  "Battle #1", 
	  [["Necrodragon", "Necrodragon", "5", "4", None], 
	  ["Necrodragon", "Necrodragon", "7", "1", None], ], 
	  None],
	  
	  ["nes02", 
	  "Battle #2", 
	  [["Necrodragon", "Necrodragon", "5", "6", None], 
	  ["Necrodragon", "Necrodragon", "8", "1", None], ], 
	  None],
	  
	  ["nes02", 
	  "Battle #3", 
	  [["Necrodragon", "Necrodragon", "5", "9", None], 
	  ["Necrodragon", "Necrodragon", "9", "1", None], ], 
	  None],
	  
	  ["nes02", 
	  "Battle #4", 
	  [["Necrodragon", "Necrodragon", "5", "12", None], 
	  ["Necrodragon", "Necrodragon", "10", "1", None], ], 
	  None],
	  
	  ["nes02", 
	  "Battle #5", 
	  [["Necrodragon", "Necrodragon", "5", "15", None], 
	  ["Necrodragon", "Necrodragon", "10", "1", None], ], 
	  None],
	  
	  ["nes02", 
	  "Battle #6{{hover|*|and all battles afterwards}}", 
	  [["Necrodragon", "Necrodragon", "5", "19", None], 
	  ["Necrodragon", "Necrodragon", "10", "1", None], ], 
	  None],
	  
	  ]

	# Insert enemy data note.
	# If no note is needed, insert "None".
	enemy_data_note = None
	
	# Insert whether or not you want to print out the units total.
	print_units_total = False

	enemy_data_section = \
		build_enemy_data(enemy_data, 
					     enemy_data_note, 
					     print_units_total)
	
	# Prints out the enemy data section. 									   
	print(enemy_data_section)
						   
	# Insert whether you want to save the enemy data as a text file.
	savetoTextFile = False
	
	# Insert the name of the text file, assuming you want to save one. 
	file_name = "enemy_data.txt"
	
	if savetoTextFile:
		writeTextFile(file_name, enemy_data_section)
						   

if __name__ == "__main__":
	main()


