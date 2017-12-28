
"""
Written by Albert"Anferensis"Ong

A function that contructs a unit's inventory.
This is used exclusively in build_enemy_data.py and build_npc_data.py.

Revision: 12-27-2017
"""

from utilities import hyperlink, writeTextFile

# A dictionary for cases where an item's name is different
# from an item's page name. 
link_exceptions = \
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


# A dictionary for cases where an item's name is different 
# from an item's image name.  
image_exceptions = \
	{"Beak (raven)" : "Beak", 
	 "Beak (hawk)" : "Beak", 
	 "Claw (cat)" : "Claw", 
	 "Claw (tiger)" : "Claw", 
	 
	 "Breath (red)" : "Breath (laguz)", 
	 "Breath (white)": "Breath (laguz)"}

# A dictionary for image exceptions specifically for Fire Emblem Gaiden. 
# This is primarily due to the graphical limitations of the game. 
image_exceptions_fe02 = \
	{"Leather Shield" : "Shield", 
	 "Dracoshild" : "Shield", 
	 
	 "Miasma" : "Black Magic", 
	 "Incarnation" : "Skill Class", 
	 
	 "Blessed Ring" : "Ring"}



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

	formatted_inv = "|inventory"
	
	add_letter = ""
	
	if isReinforcement:
		add_letter = "r"
	
		if isLastReinforcement:
			add_letter += "l"
			unit_num = ""
	
	formatted_inv += add_letter + unit_num + "="
	
	# If inventory data is equal to "None"
	if inventory_data == None:
		
		# The formatted inventory is just two hypens. 
		# This represents a blank inventory. 
		formatted_inv += "--"
	
	
	# Otherwise, if there is inventory data...
	else:
		
		# For loops the list of items
		for item_name in inventory_data:
			
			# The name of the item is put entirely in lower case		
			lowered_item_name = item_name.lower()
			
			if item_name.endswith(" (drop)"):
				item_name = item_name[:-7]
				lowered_item_name = lowered_item_name[:-7]
				
				if item_name in link_exceptions:
					link = link_exceptions[item_name]
					item_link = "{{drop|" + link + "|" + item_name + "}}"
				else:
					item_link = "{{drop|" + item_name + "}}"		
								 
			elif item_name in link_exceptions:
				
				link = link_exceptions[item_name]			
				item_link = hyperlink(link, item_name)
			
			elif item_name in image_exceptions:
				link = image_exceptions[item_name]
				item_link = hyperlink(link)
				
			else:
				item_link = hyperlink(item_name)
			
			
			if platform in ("nes02", "3ds03") and item_name in image_exceptions_fe02:
				lowered_item_name = image_exceptions_fe02[item_name].lower()
					

			item_image = "[[File:Is " + platform + " " + lowered_item_name + ".png]]"
			
			# Creates the formatted item data, which includes a link directed 
			# towards the item sprite and a hyperlink to the item itself
			formatted_item = item_image + item_link
			
			# Adds the formatted item data to the formatted inventory										
			formatted_inv += formatted_item
	
	# By the end of the for loop, the inventory should be
	# properly formatted. 	
	return formatted_inv



#=======================================================================


def main():
	
	platform = "gba"
	inventory = ["Iron Sword", "Iron Sword (drop)"]
	unit_num = "2"
	
	formatted_inventory = build_unit_inventory(platform, inventory, unit_num)
	
	print(formatted_inventory)
	
	
if __name__ == "__main__":
	main()


