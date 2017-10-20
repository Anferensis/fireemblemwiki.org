
"""
Written by Albert"Anferensis"Ong

Constructs an enemy data table for fireemblemwiki.org
"""

from utilities import hyperlink, writeTextFile
	

def build_unit_inventory(platform, 
						 inventory_data, 
						 unit_num, 
						 isReinforcement = False,
						 isLastReinforcement = False):
	"""
	Properly formats a unit's inventory data.
	
	Accepts a list of strings, where every string is an item name, 
	and string, representing the unit's number.
	
	Converts such that 
	build_unit_inventory(["Iron Sword", "Steel Sword (drop)"], "2")
	returns:
	
	|inventory2=[[File:Is gba iron sword.png]][[Iron Sword]]
				[[File:Is gba steel sword.png]]{{drop|Steel Sword}}
	"""
	
	formatted_inv_start = "|inventory"
	
	add_letter = ""
	
	if isReinforcement:
		add_letter = "r"
	
		if isLastReinforcement:
			add_letter += "l"
			unit_num = ""
	
	formatted_inv_start += add_letter	
	formatted_inv = formatted_inv_start + unit_num + "="
	
	# For loops the list of items
	for item_name in inventory_data:
		
		# The name of the item is put entirely in lower case		
		lowered_item_name = item_name.lower()
		
		special_link_cases = \
				{"Fire" : "Fire (tome)", 
				 "Thunder" : "Thunder (tome)", 
				 "Luna" : "Luna (skill)", 
				 "Wind" : "Wind (tome)",
				 "Light": "Lightning",
				 "Eclipse" : "Eclipse (tome)",
				 "Ballista" : "Ballista (weapon)",
				 
				 "Berserk" : "Berserk (staff)",
				 "Sleep" : "Sleep (staff)", 
				 "Warp" : "Warp (staff)",
				 "Rescue" : "Rescue (staff)",
				 "Silence" : "Silence (staff)", 
				 "Stone" : "Stone (tome)", 
				 "Forseti" : "Forseti (tome)",
				 "Torch" : "Torch (item)",
				 "Poison" : "Poison (tome)", 
				 
				 "Adept Manual" : "Skill items",
				 "Adept Scroll" : "Skill items", 
				 "Occult Scroll" : "Skill items",
				 "Provoke Scroll" : "Skill items",  
				 "Guard Scroll" : "Skill items",
				 "Gamble Scroll" : "Skill items", 
				 
				 "Renewal" : "Renewal (skill)",
				 "Guard" : "Cancel", 
				 "Cancel" : "Pavise"}
				 
		special_image_cases = \
			{"Beak (raven)" : "Beak", 
			 "Beak (hawk)" : "Beak", 
			 "Claw (cat)" : "Claw", 
			 "Claw (tiger)" : "Claw", 
			 
			 "Breath (red)" : "Breath (laguz)", 
			 "Breath (white)": "Breath (laguz)"}
		
		if item_name.endswith(" (drop)"):
			item_name = item_name[:-7]
			lowered_item_name = lowered_item_name[:-7]
			
			if item_name in special_link_cases:
				link = special_link_cases[item_name]
				item_link = "{{drop|" + link + "|" + item_name + "}}"
			else:
				item_link = "{{drop|" + item_name + "}}"		
							 
		elif item_name in special_link_cases:
			
			link = special_link_cases[item_name]			
			item_link = hyperlink(link, item_name)
		
		elif item_name in special_image_cases:
			link = special_image_cases[item_name]
			item_link = hyperlink(link)
			
		else:
			item_link = hyperlink(item_name)
		
		if item_name == "Beak":
			item_image = "[[File:Is " + platform + " " + lowered_item_name + " (raven).png]]"
		else:
			item_image = "[[File:Is " + platform + " " + lowered_item_name + ".png]]"
		
		
		# Creates the formatted item data, which includes a link directed 
		# towards the item sprite and a hyperlink to the item itself
		formatted_item = item_image + item_link
		
		# Adds the formatted item data to the formatted inventory										
		formatted_inv += formatted_item
	
	# By the end of the for loop, the inventory should be
	# properly formatted. 	
	return formatted_inv


def build_units_data(platform,
					 units_data,
					 isReinforcement = False):
					 
	formatted_units_data = ""
	
	for unit_num, unit_data in enumerate(units_data, 1):
		
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
		
		
		
		if unit_class == "Raven":
			class_article_line = "|class" + add_letter + unit_num + "article=" + "Raven (laguz)"
		
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
				formatted_unit_data += line + "\n"
		
		formatted_units_data += formatted_unit_data + "\n"	
	
	return formatted_units_data
	


def build_enemy_data(platform, 
					 enemy_data, 
					 reinforcement_data, 
					 enemy_data_note,
					 print_units_total = False):
	

	formatted_units_data = build_units_data(platform, enemy_data)

	if reinforcement_data != None:
		formatted_reinforcement_data = build_units_data(platform, 
														reinforcement_data, 
														True)
	else:
		formatted_reinforcement_data = None	
	
	
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
	
	
	enemy_data_section = ""
	
	for section in ("===Enemy Data===", 
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
	platform = "gba"

	# Unit data is formatted:
	# 	[name, class, level, quantity, [inventory items]]

	# Example: ["Bandit", "Brigand", "1", "1", ["Iron Axe", "Vulnerary"]]
	# Template: ["", "", "", "", [""]], 

	enemy_data = \
	[["Seihou", "Archer", "9", "1", ["Steel Bow"]],
	["Seihou", "Archer", "11", "1", ["Steel Bow", "Antitoxin"]],
	["Seihou", "Archer", "12", "2", ["Iron Bow"]],
	["Seihou", "Archer", "12", "2", ["Steel Bow"]],
	["Seihou", "Fighter", "9", "1", ["Poison Axe"]],
	["Seihou", "Fighter", "9", "1", ["Steel Axe", "Hand Axe"]],
	["Seihou", "Fighter", "9", "1", ["Hand Axe"]],
	["Seihou", "Fighter", "11", "1", ["Poison Axe"]],
	["Seihou", "Fighter", "12", "1", ["Steel Axe"]],
	["Seihou", "Fighter", "12", "1", ["Steel Axe", "Hand Axe"]],
	["Seihou", "Fighter", "12", "1", ["Halberd"]],
	["Seihou", "Fighter", "12", "1", ["Poison Axe", "Antitoxin"]],
	["Seihou", "Mage", "9", "2", ["Elfire", "Vulnerary"]],
	["Seihou", "Mage", "10", "1", ["Thunder"]],
	["Seihou", "Mercenary", "8", "1", ["Iron Sword", "Antitoxin"]],
	["Seihou", "Mercenary", "10", "1", ["Steel Sword"]],
	["Seihou", "Mercenary", "12", "2", ["Steel Sword"]],
	["Seihou", "Pirate", "8", "1", ["Steel Axe", "Vulnerary"]], 
	["Seihou", "Pirate", "8", "1", ["Hand Axe"]], 
	["Seihou", "Pirate", "10", "1", ["Steel Axe"]], 
	["Seihou", "Pirate", "10", "1", ["Hand Axe"]], 
	["Seihou", "Pirate", "11", "1", ["Poison Axe"]], 
	["[[Scott]]", "Berserker", "5", "1", ["Killer Axe", "Hand Axe"]],]
	
	
	# Insert reinforcement data.
	# Unit data is formatted the same as with the enemy data above. 
	# 	If there are no reinforcements, insert "None"
	
	reinforcement_data = \
	[["[[Fir]]", "Myrmidon", "1", "1", ["Wo Dao", "Vulnerary"]], 
	["[[Sin]]", "Nomad", "5", "1", ["Short Bow"]],
	["Seihou", "Pirate", "10", "5", ["Steel Axe"]],
	["Seihou", "Pirate", "10", "9", ["Hand Axe"]],
	["Seihou", "Pirate", "11", "9", ["Poison Axe", "Antitoxin"]],]

	# Insert enemy data note
	# 	if uneccessary, input "None"
	enemy_data_note = None
	
	
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





