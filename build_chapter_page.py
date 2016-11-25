
"""
Written by Albert"Anferensis"Ong

A program designed to build a chapter page for fireemblemwiki.org
"""



def build_chapter_infobox(title, image_num, game, location, new_units, bosses):
	
	chapter_infobox = "{{Chapter Infobox \n"
	
	title_line = "|title=" + title
	image_line = "|image=[[File:Cm fe07 " + image_num +".png|200px]]"
	location_line = "|location=[[" + location + "]]"
	
	new_units_line = "|new units="	
	
	for unit_num, unit_name in enumerate(new_units, 1):
		formatted_unit_name = "[[" + unit_name + "]]"
		
		if unit_num != len(new_units):
			formatted_unit_name += ", "
			
		new_units_line += formatted_unit_name
	
		
	bosses_line = "|boss="	
	
	for boss_num, boss_name in enumerate(bosses, 1):
		formatted_boss_name = "[[" + boss_name + "]]"
		
		if boss_num != len(bosses):
			formatted_boss_name += ", "
			
		bosses_line += formatted_boss_name
	
	
	for line in (title_line, image_line, location_line, 
				 new_units_line, bosses_line):
					 
		chapter_infobox += line + "\n"
	
	chapter_infobox += "}}"
	
	return chapter_infobox



def build_chapter_data(victory_condition, defeat_condition, ally, other, enemy):
	
	victory_line = "|victory=" + victory_condition
	defeat_line = "|defeat=" + defeat_condition
	ally_line = "|ally=" + ally
	other_line = "|other=" + other
	enemy_line = "|enemy=" + enemy
	
	chapter_data = ""
	
	for line in ("==Chapter data==", "{{ChapData", victory_line, defeat_line, 
				 ally_line, other_line, enemy_line, "}}"):
		chapter_data += line + "\n"
	
	return chapter_data	


	
def build_character_data(return_characters, new_units_data = None):
	character_data = "===Character Data=== \n" + \
					 "{{ChapChars \n" + \
					 "|game#=07 \n"
					 
	if new_units_data != None:
		
		number_of_new_units = str(len(new_units_data))
		
		formatted_new_units = "|newunits = " + number_of_new_units + "\n"
		
		for unit_num, new_unit in enumerate(new_units_data, 1):
			
			unit_name = new_unit[0]
			unit_data = new_unit[1]
			
			unit_portrait = "[[File:portrait " + unit_name.lower() + " fe07.png]]" 
			unit_class = unit_data[0]
			unit_HP = unit_data[1]
			unit_level = unit_data[2]
			unit_recruitment = unit_data[3]
			
			new_unit_data = "| newunit" + str(unit_num) +" = {{NewUnit \n"
							
			name_line = 	   	"| name = " + unit_name
			portrait_line =     "| portrait = " + unit_portrait
			class_line =  	   	"| class = " + unit_class
			HP_line = 		   	"| HP = " + unit_HP
			level_line = 	   	"| lv = " + unit_level
			recruitment_line = 	"| recruitment method = " + unit_recruitment
			
			for line in (name_line, portrait_line, class_line, HP_line, 
						 level_line, recruitment_line):
				
				new_unit_data += line + "\n"
				
			new_unit_data += "}}" + "\n"
				
			formatted_new_units += new_unit_data
			
		character_data += formatted_new_units
			
					 
	for num, char_name in enumerate(return_characters, 1):
		char_num = str(num)
		char_name = char_name.lower()
		
		char_line = "|return" + char_num + "=" + char_name
		character_data += char_line + "\n"
	
	character_data += "}} \n"
	
	return character_data
	


def build_item_data(item_data):
	
	formatted_item_data = ""
	
	for item_num, item in enumerate(item_data, start = 1):
		
		if item_num == len(item_data):
			item_num = "last"
		else:
			item_num = str(item_num)
			
		item_name = item[0]
		obtain_method = item[1]
		
		item_line = "|item" + item_num + "=" + item_name
		obtain_line = "|obtain" + item_num + "=" + obtain_method
		
		for line in (item_line, obtain_line):
			formatted_item_data += line + "\n"
			
	final_item_data = "===Item data=== \n" + \
					  "{{ChapItems \n" + \
					  "|platform=gba \n" + \
					  formatted_item_data + "}}"
		
	return final_item_data



def build_shop_data(shop_data):
	
	if shop_data == None:
		shop_data = ""
		
	else:
		shop_data = "===Shop Data===" + \
					"{{ChapShop GBA \n }}"
					
		price_list = {"Slim Sword" : "480", 
					  "Iron Sword" : "460",
					  "Steel Sword" : "600",
					  "Iron Axe" : "270", 
					  "Steel Axe" : "360", 
					  "Hand Axe" : "300",
					  "Slim Lance" : "450", 
					  "Iron Lance" : "360", 
					  "Steel Lance" : "480", 
					  "Javelin" : "400", 
					  "Iron Bow" : "540", 
					  "Steel Bow" : "720", 
					  "Fire" : "560", 
					  "Thunder" : "700", 
					  "Lightning" : "630", 
					  "Flux" : "900", 
					  "Heal" : "600", 
					  "Mend" : "1000",
					  "Vulnerary" : "300", 
					  "Door Key" : "50"}
		
		
	return shop_data



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
			item_link = "[[" + item_name + "]]"
		
		# Creates the formatted item data, which includes a link directed 
		# towards the item sprite and a hyperlink to the item itself
		formatted_item = "[[File:Is gba "+ lowered_item_name + ".png]]" + \
						 item_link
		
		# Adds the formatted item data to the formatted inventory										
		formatted_inv += formatted_item
	
	# By the end of the for loop, the inventory should be
	# properly formatted. 	
	return formatted_inv



def build_units_data(units_name, units_data, isReinforcement = False):
	
	formatted_units_data = ""
	
	for unit_num, unit_data in enumerate(units_data, start = 1):
		
		unit_num = str(unit_num)
		unit_class = unit_data[0]
		unit_level = unit_data[1]
		unit_quantity = unit_data[2]
		unit_inventory = unit_data[3]
		
		
		# Checks if the inputted class is viable.
		viable_classes = ("Archer", "Berserker", "Brigand", "Cavalier", 
						  "Druid", "Fighter", "Knight", "Mage", "Mercenary", 
						  "Monk", "Myrmidon", "Nomad", "Nomadic Trooper", 
						  "Paladin", "Pegasus Knight",
						  "Pirate", "Soldier", 
						  "Shaman", "Thief", "Troubadour")			
						  			  
		if unit_class not in viable_classes:
			raise ValueError("The inputted class was not viable")
			
		# Checks if the inputted unit level is an integer.	
		try: 
			int(unit_level)			
		except ValueError:
			raise ValueError("The inputted unit level was not an integer")
		
		# Checks if the inputted unit quantity is an integer.		
		try: 
			int(unit_quantity)		
		except ValueError:
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
			inventory_line = build_unit_inventory(unit_inventory, 
											  unit_num, 
											  isReinforcement,
											  True)											  
		else:
			inventory_line = build_unit_inventory(unit_inventory, 
											  unit_num, 
											  isReinforcement)	
											  
		name_line =     name_line_start + unit_num + "=" + enemy_name
		class_line =    class_line_start + unit_num + "=" + unit_class
		level_line =    level_line_start + unit_num + "=" + unit_level
		quantity_line = quantity_line_start + unit_num + "=" + unit_quantity											  
					  
		
		formatted_unit_data = ""	
		
		for line in (name_line, class_line, level_line, 
					 quantity_line, inventory_line):
						 
			formatted_unit_data += line + "\n"
		
		formatted_units_data += formatted_unit_data + "\n"
	
		
	return formatted_units_data



def build_enemy_data(enemy_name, 
					  enemy_data, 
					  boss_data, 
					  reinforcement_data = None):
	"""
	A function that will properly format a chapter's enemy data
	given a data of all units, represented as a list, and data for
	the boss, also represented as a list. 
	
	Unit data is formatted:
		[class, level, quantity, inventory]
		
	Boss data is formatted:
		[name, class, level, inventory]
		
	Inventories are represented as a list of strings
	and are formatted:
		[item1, item2, item3]		
	
	"""
	
	formatted_units_data = build_units_data(enemy_name, enemy_data)
	
	if reinforcement_data != None:
		formatted_reinforcement_data = build_units_data(enemy_name, 
														 reinforcement_data, 
														 True)
	else:
		formatted_reinforcement_data = ""
		
	# Retrieving all the boss data and assigning variables to it.
	boss_name = boss_data[0]
	boss_class = boss_data[1]
	boss_level = boss_data[2]
	boss_inv = boss_data[3]
	
	# The boss inventory gets formatted separately.
	formatted_boss_inv = build_unit_inventory(boss_inv, "b")
	
	# Creates the formatted boss data.	
	boss_data = "|nameb=" + boss_name + "\n" + \
				"|classb=" + boss_class + "\n" + \
				"|lvb=" + boss_level +"\n" + \
				  formatted_boss_inv + "\n"
		
	# Assembles the formatted enemy data and boss data into
	# the finalized format. 	
	complete_enemy_data = "===Enemy Data=== \n" + \
						  "{{ChapEnemies \n" + \
					      "|platform = gba \n" + \
					      formatted_units_data + \
					      boss_data + "\n" + \
					      formatted_reinforcement_data + "}}"
	
	return complete_enemy_data



def build_chapter_page(chapter_title, 
					   image_num,
					   game,
					   location,
					   new_units,
					   chapter_desciption, 
					   victory_condition,
					   defeat_condition,
					   ally,
					   other,
					   enemy,
					   return_characters,
					   new_units_data,
					   item_data,
					   shop_data,
					   enemy_name,
					   enemy_data,
					   boss_data,
					   reinforcement_data,
					   isStub = True):
	"""
	A function designed to build a chapter page for fireemblemwiki.org.
	"""					   
	
	
	if not isStub:
		stub_mark = ""
		
	else:
		stub_mark = "{{Stub}}"
	
	chapter_infobox = build_chapter_infobox(chapter_title, 
											image_num, 
											game, 
											location,
											new_units, 
											bosses)
											 
	chapter_data = build_chapter_data(victory_condition, 
									  defeat_condition, 
									  ally, other, enemy)
									  
	character_data = build_character_data(return_characters, 
										  new_units_data)
	
	chapter_plot = "==Plot== \n" + \
				   "{{main|" + chapter_name + "/Script}} \n" + \
				   "{{sectstub}} \n"
	
	item_data = build_item_data(item_data)
	shop_data = build_shop_data(shop_data)
	
	enemy_data = build_enemy_data(enemy_name, enemy_data, boss_data, 
								  reinforcement_data)
	
	chapter_page = ""
	
	for data in (stub_mark, chapter_infobox, chapter_desciption, chapter_plot, 
				 chapter_data, character_data, item_data, shop_data, enemy_data):
		chapter_page += data + "\n"
											 
	return chapter_page
	
	
	
#=======================================================================

chapter_name = "The Dread Isle"

chapter_title = "The Dread Isle"
image_num = "18"
game = "FE7"
location = "Dread Isle"
new_units = ["Dart", "Fiora"]
bosses = ["Uhai"]

chapter_desciption = \
"""'''The Dread Isle''' is chapter 18 of [[Eliwood|Eliwood's]] tale and chapter
19 of [[Hector|Hector's]] tale in {{FE7}}.
"""

victory_condition = "Defeat [[Uhai]]"
defeat_condition = "[[Eliwood]], [[Hector]], or [[Lyn]] dies"
ally = "11{{hover|+2|Dart and Fiora}}"
other = "{{hover|1|Fiora}}"
enemy = "21{{hover|+6|reinforcements}}"

return_characters = \
["Eliwood", "Lowen", "Marcus", "Rebecca", "Dorcas", 
"Bartre", "Hector", "Oswin", "Matthew", "Serra",
"Guy", "Erk", "Priscilla", "Lyn", "Kent", 
"Sain", "Wil", "Florina", "Raven", "Lucius",  
"Canas"] 
					 
new_units_data = \
[["Dart", ["Pirate", "34", "8", "Automatically at the start"]], 
["Fiora", ["Pegasus Knight", "21", "7", "Talk with [[Florina]]"]]]

item_data = \
[["Mine", "Steal from [[cavalier]] (not in hard mode)"],
["Light Rune", "Steal from [[cavalier]] (not in hard mode)"],
["Torch", "Steal from [[pirate]]"],
["Torch", "Dropped by [[nomad]] (not in hard mode)"],
["Longbow", "Dropped by [[nomad]]"],
["Torch Staff", "Dropped by [[thief]]"],
["Nosferatu", "Dropped by [[shaman]]"],
["Torch", "Dropped by [[nomad]] (hard mode only)"],
["Lightning", "Dropped by [[shaman]] (hard mode only)"],
["Orion's Bolt", "Dropped by boss"]]

shop_data = None

enemy_name = "Black Fang"

# Unit data is formatted:
# 	[class, level, quantity, inventory]

# Boss data is formatted:
# 	["name", "class", "level", inventory]

# ["", "", "", [""]],

boss_data = ["Uhai", "Nomadic Trooper", "7", 
			["Steel Sword", "Longbow", "Short Bow", "Orion's Bolt (drop)"]]
			
# Archer L6 w/Iron Bow
# 2 Cavalier L5 w/Iron Sword
# 2 Cavalier L5 w/Iron Lance, one with Mine
# Cavalier L6 w/Iron Sword
# Cavalier L6 w/Steel Sword, Light Rune
# 2 Cavalier L6 w/Iron Lance, Iron Sword (equipped different weapons)
# Monk L5 w/Lightning
# Myrmidon L12 w/Slim Sword
# Nomad L6 w/Iron Bow
# Nomad L6 w/Short Bow
# Nomad L6 w/Steel Bow
# Nomad L7 w/Iron Bow, Torch DROPPED
# Nomad L8 w/Longbow DROPPED
# Pirate L6 w/Iron Axe
# Pirate L7 w/Steel Axe, Torch
# Shaman L6 w/Nosferatu
# Thief L5 w/Iron Sword, Torch Staff DROPPED	
	
enemy_data = \
[["Archer", "6", "1", ["Iron Bow"]],
["Cavalier", "5", "2", ["Iron Sword"]],
["Cavalier", "5", "1", ["Iron Lance"]],
["Cavalier", "5", "1", ["Iron Lance", "Mine"]],
["Cavalier", "6", "1", ["Iron Sword"]],
["Cavalier", "6", "1", ["Steel Sword", "Light Rune"]],
["Cavalier", "6", "2", ["Iron Lance", "Iron Sword"]],
["Monk", "5", "1", ["Lightning"]],
["Myrmidon", "12", "1", ["Slim Sword"]],
["Nomad", "6", "1", ["Iron Bow"]],
["Nomad", "6", "1", ["Short Bow"]],
["Nomad", "6", "1", ["Steel Bow"]],
["Nomad", "7", "1", ["Iron Bow", "Torch (drop)"]],
["Nomad", "8", "1", ["Longbow (drop)"]],
["Pirate", "6", "1", ["Iron Axe"]],
["Pirate", "7", "1", ["Steel Axe", "Torch"]],
["Shaman", "6", "1", ["Nosferatu (drop)"]],
["Thief", "5", "1", ["Iron Sword", "Torch Staff (drop)"]]]

#~ Turn 2 to 4 from north east corner and north west corner: +2 Pirate L6 w/Iron
#~ Axe (one from each corner)

reinforcement_data = \
[["Pirate", "6", "6", ["Iron Axe"]]]


chapter_page = build_chapter_page(chapter_title, 
								  image_num,
								  game,
								  location,
								  new_units,
								  chapter_desciption,
								  victory_condition,
								  defeat_condition,
								  ally,other,enemy,
								  return_characters,
								  new_units_data,
								  item_data,
								  shop_data,
								  enemy_name,
								  enemy_data,
								  boss_data,
								  reinforcement_data)

print(chapter_page)

#print(build_character_data(return_characters, new_units_data))

