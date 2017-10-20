
"""
Written by Albert"Anferensis"Ong
"""

from utilities import hyperlink, writeTextFile

	
def build_unit_inventory(inventory_data, unit_num, 
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
							 "Berserk" : "Berserk (staff)",
							 "Sleep" : "Sleep (staff)", 
							 "Warp" : "Warp (staff)",
							 "Silence" : "Silence (staff)", 
							 "Stone" : "Stone (tome)"}
							 
			if item_name in special_cases:
				
				link = special_cases[item_name]			
				item_link = hyperlink(link, item_name)
				
			else:
				item_link = hyperlink(item_name)
		
		# Creates the formatted item data, which includes a link directed 
		# towards the item sprite and a hyperlink to the item itself
		formatted_item = "[[File:Is gba "+ lowered_item_name + ".png]]" + \
						 item_link
		
		# Adds the formatted item data to the formatted inventory										
		formatted_inv += formatted_item
	
	# By the end of the for loop, the inventory should be
	# properly formatted. 	
	return formatted_inv
	
	

def build_npc_data(npc_data, npc_data_note):
	
	if npc_data == None:
		npc_data_section = ""
		
	else:
		npc_data_section = ""
		
		for line in ("===NPC Data===", 
					 "{{ChapOthers", 
					 "|platform=gba"):
						 
			npc_data_section += line + "\n"
			
			
		for unit_num, unit_data in enumerate(npc_data, 1):
			
			if unit_num == len(npc_data):
				unit_num = "l"
			else:
				unit_num = str(unit_num)
			
			
			unit_name = unit_data[0]
			unit_class = unit_data[1]
			unit_level = unit_data[2]
			unit_quantity = unit_data[3]
			unit_inventory = unit_data[4]
			
			name_line = "|name" + unit_num + "=" + unit_name
			class_line = "|class" + unit_num + "=" + unit_class
			level_line = "|lv" + unit_num + "=" + unit_level
			quantity_line = "|#" + unit_num + "=" + unit_quantity
			inventory_line = build_unit_inventory(unit_inventory, unit_num)
			
			for line in (name_line, 
						 class_line, 
						 level_line, 
						 quantity_line, 
						 inventory_line):
							 
				npc_data_section += line + "\n"
				
		npc_data_section += "}} \n"
	
	if npc_data_note != None:
		npc_data_section += npc_data_note
		
	return npc_data_section
	
	
	
#=======================================================================


def main():
	
	# Insert NPC data
	# NPC unit data is organized:
	#	[name, class, level, quantity, [inventory]]

	# ["", "", "", "", [""]]

	npc_data = \
	[["[[Zelots]]", "Paladin", "1", "1", ["Steel Sword", "Steel Lance", "Javelin"]],
	["[[Trec]]", "Cavalier", "4", "1", ["Iron Lance", "Javelin", "Vulnerary"]],
	["[[Noah]]", "Cavalier", "7", "1", ["Steel Sword", "Iron Lance", "Vulnerary"]]]

	# Insert NPC data note
	# If no note is needed, insert "None"
	npc_data_note = None

	npc_data_section = build_npc_data(npc_data, npc_data_note)
	
	print(npc_data_section)
	
	savetoTextFile = False
	
	if savetoTextFile:
		writeTextFile("npc_data_section.txt", npc_data_section)



if __name__ == "__main__":
	main()


