
"""
Written by Albert"Anferensis"Ong
"""

def hyperlink(link, display_text = None):
	
	if display_text != None:
		formatted_link = "[[" + link + "|" + display_text +"]]"
		
	else:
		formatted_link = "[[" + link + "]]"
	
	return formatted_link
	


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
		
		if item_name.endswith(" (drop)"):
			item_name = item_name[:-7]
			lowered_item_name = lowered_item_name[:-7]
			item_link = "{{drop|" + item_name + "}}"
			
		else:
			
			special_cases = {"Fire" : "Fire (tome)", 
							 "Thunder" : "Thunder (tome)", 
							 "Luna" : "Luna (tome)", 
							 "Wind" : "Wind (tome)",
							 "Ballista" : "Ballista (weapon)",
							 
							 "Berserk" : "Berserk (staff)",
							 "Sleep" : "Sleep (staff)", 
							 "Warp" : "Warp (staff)",
							 "Silence" : "Silence (staff)", 
							 "Stone" : "Stone (tome)", 
							 "Forseti" : "Forseti (tome)",
							 "Torch" : "Torch (item)"}
							 
			if item_name in special_cases:
				
				link = special_cases[item_name]			
				item_link = hyperlink(link, item_name)
				
			else:
				item_link = hyperlink(item_name)
		
		# Creates the formatted item data, which includes a link directed 
		# towards the item sprite and a hyperlink to the item itself
		formatted_item = "[[File:Is " + platform + " " + lowered_item_name + ".png]]" + \
						 item_link
		
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
		
		unit_num = str(unit_num)
		
		unit_name = unit_data[0]
		unit_class = unit_data[1]
		unit_level = unit_data[2]
		unit_quantity = unit_data[3]
		unit_inventory = unit_data[4]
		
		# Checks if the inputted unit level is an integer.	
		try: 
			int(unit_level)			
		except ValueError:
			print(unit_data)
			raise ValueError("The inputted unit level was not an integer")
		
		# Checks if the inputted unit quantity is an integer.		
		try: 
			int(unit_quantity)		
		except ValueError:
			print(unit_data)
			raise ValueError("The inputted unit quantity was not an integer")
											  
		name_line_start = "|name"
		class_line_start = "|class"
		level_line_start = "|lv"
		quantity_line_start = "|#"
		
		isLastReinforcement = False
		
		if isReinforcement:
			
			add_letter = "r"
			
			if int(unit_num) == len(units_data):
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
											  
		formatted_unit_data = ""	
		
		for line in (name_line, 
					 class_line, 
					 level_line, 
					 quantity_line, 
					 inventory_line):
					 
			formatted_unit_data += line + "\n"
		
		formatted_units_data += formatted_unit_data + "\n"	
	
	
	return formatted_units_data
			


def build_enemy_data(platform, 
					 enemy_data, 
					 reinforcement_data = None, 
					 print_units_total = False):
	

	formatted_units_data = build_units_data(platform, enemy_data)

	if reinforcement_data != None:
		formatted_reinforcement_data = build_units_data(platform, 
														reinforcement_data, 
														True)
	else:
		formatted_reinforcement_data = ""	
	
	if print_units_total:
		
		enemy_total = 0
		
		for unit_data in enemy_data:
			unit_quantity = int(unit_data[3])
			enemy_total += unit_quantity
			
		reinforcement_total = 0
		
		for unit_data in reinforcement_data:
			reinforcement_quantity = int(unit_data[3])
			reinforcement_total += reinforcement_quantity
			
		print("Enemy total: ", enemy_total)
		print("Reinforcement total: ", reinforcement_total)
	
	
	enemy_data_section = ""
	
	for line in ("===Enemy Data===", 
				 "{{ChapEnemies", 
				 "|platform=" + platform, 
				 formatted_units_data,
				 formatted_reinforcement_data, 
				 "}}"):
					 
		 enemy_data_section += line + "\n"
	
	return enemy_data_section
	
	
	
#======================================================================

platform = "gba"

# Unit data is formatted:
# 	[name, class, level, quantity, [inventory items]]

# Example: ["Bandit", "Brigand", "1", "1", ["Iron Axe", "Vulnerary"]]

enemy_data = \
[["Name1", "Myrmidon", "1", "1", ["Iron Sword"]], 
["Name2", "Soldier", "1", "1", ["Iron Lance"]], 
["Name3", "Brigand", "1", "1", ["Iron Axe"]],
["Boss", "Knight", "5", "1", ["Silver Lance", "Javelin"]]]

reinforcement_data = \
[["Reinforcement1", "Mercenary", "1", "1", ["Iron Sword"]], 
["Reinforcement2", "Cavalier", "1", "1", ["Iron Lance"]], 
["Reinforcement3", "Fighter", "1", "1", ["Iron Axe"]],]

print_units_total = False

print(build_enemy_data(platform, 
					   enemy_data, 
					   reinforcement_data, 
					   print_units_total))

