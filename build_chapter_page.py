
"""
Written by Albert"Anferensis"Ong

A program designed to build a chapter page for fireemblemwiki.org.

This program currently only supports the gameboy advance titles:
Fire Emblem: The Binding Blade, Fire Emblem: The Blazing Sword, and
Fire Emblem: The Sacred Stones. 
"""

# A list of items and their prices
# This is used for building shop data.

# Note: the price list is not comprehensive

price_list = {"Slim Sword" : "480", 
			  "Iron Sword" : "460",
			  "Steel Sword" : "600",
			  "Lancereaver" : "1,800",
			  "Armorslayer" : "1,260",
			  "Longsword" : "1,260",
			  "Killing Edge" : "1,300",
			  
			  "Slim Lance" : "450", 
			  "Iron Lance" : "360", 
			  "Steel Lance" : "480", 
			  "Javelin" : "400", 
			  "Axereaver" : "1,950",
			  "Heavy Spear" : "1,200",
			  "Horseslayer" : "1,040",
			  "Killer Lance" : "1,200",
			  
			  "Iron Axe" : "270", 
			  "Steel Axe" : "360", 
			  "Hand Axe" : "300",
			  "Swordreaver" : "2,100",
			  "Hammer" : "800",
			  "Halberd" : "810",
			  "Killer Axe" : "1,000",
				  
			  "Iron Bow" : "540", 
			  "Steel Bow" : "720", 
			  "Killer Bow" : "1,400",
			  
			  "Fire" : "560", 
			  "Thunder" : "700",
			  "Elfire" : "1,200", 
			  "Lightning" : "630", 
			  "Shine" : "900", 
			  "Flux" : "900", 
			  
			  "Heal" : "600", 
			  "Mend" : "1,000",
			  "Restore": "",
			  "Physic" : "3,750",
			  "Torch" : "1,000",
			  "Unlock": "1,500",
			  "Barrier" : "2,250",
			  "Restore" : "2,000",
				  
			  "Vulnerary" : "300", 
			  "Antitoxin" : "450",
			  "Door Key" : "50",
			  "Elixir": "3,000", 
			  "Chest Key": "1,500",
			  "Lockpick" : "1,200", 
			  
			  "Ocean Seal" : "50,000"
			  }


def format_shop_items(shop_items):
	
	formatted_shop_items = ""
				  
	for item_name in shop_items:
		
		item_name_lowered = item_name.lower()
		item_price = price_list[item_name]
		
		line1 =  "{{!}} style={{roundl}}; {{!}} [[File:Is gba " + \
				 item_name_lowered + ".png|right]]" 		          
		line2 = "{{!}} [[" + item_name + "]]"
		line3 = "{{!}} style={{roundr}}; text-align: center {{!}} " + item_price
		line4 =  "{{!-}}"
		
		formatted_item_data = ""
		
		for line in (line1, line2, line3, line4):
			formatted_item_data += line + "\n"
			
		formatted_shop_items += formatted_item_data
		
	return formatted_shop_items



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
	
	units_total = 0
	reinforcements_total = 0
	
	formatted_units_data = ""
	
	for unit_num, unit_data in enumerate(units_data, start = 1):
		
		unit_num = str(unit_num)
		unit_class = unit_data[0]
		unit_level = unit_data[1]
		unit_quantity = unit_data[2]
		unit_inventory = unit_data[3]
			
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
		
		if isReinforcement:
			reinforcements_total += int(unit_quantity)
		else:
			units_total += int(unit_quantity)
	
	units_total += 1
	#print("units total is: ", units_total)
	#print("reinforcements total is: ", reinforcements_total)
	
		
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
					   chapter_plot,
					   beginning_log,
					   victory_condition,
					   defeat_condition,
					   ally, 
					   other,
					   enemy,
					   return_characters,
					   new_units_data,
					   item_data,
					   shop_data_header,
					   shops_info,
					   enemy_name,
					   enemy_data,
					   boss_data,
					   reinforcement_data,
					   boss_name,
					   detailed_boss_data,
					   prechapter,
					   nextchapter,
					   prealternate,
					   nextalternate,
					   strategy,
					   trivia,
					   isStub = True):
	"""
	A function designed to build a chapter page for fireemblemwiki.org.
	"""					   
		
	if not isStub:
		stub_mark = ""
		
	else:
		stub_mark = "{{Stub}}"
	
	#==========================================================
	
	# Building chapter info box.
		
	chapter_infobox = "{{Chapter Infobox \n"
	
	title_line = "|title=" + chapter_title
	image_line = "|image=[[File:Cm " + game + " " + image_num +".png|200px]]"
	location_line = "|location=[[" + location + "]]"
	
	new_units_line = "|new units="	
	
	if new_units != None:
		for unit_num, unit_name in enumerate(new_units, 1):
			formatted_unit_name = "[[" + unit_name + "]]"
			
			if unit_num != len(new_units):
				formatted_unit_name += ", "
				
			new_units_line += formatted_unit_name
			
	else:
		new_units_line += "none"
	
		
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
	
	#=========================================================

	# Building plot section
	
	plot_section = ""
	
	if chapter_plot == None:
		plot_body = "{{sectstub}}"
	else:
		plot_body = chapter_plot
		
	for part in ("==Plot==",
				 "{{main|" + chapter_title + "/Script}} \n",
				 plot_body,
				 "",
				 "===Beginning Log===",
				 beginning_log):
		
		plot_section += part + "\n"
	
	#=========================================================
	
	# Building chapter data
	
	chapter_data = ""
											 
	victory_line = "|victory=" + victory_condition
	defeat_line = "|defeat=" + defeat_condition
	ally_line = "|ally=" + ally
	other_line = "|other=" + other
	enemy_line = "|enemy=" + enemy
	map_line = "|map=[[File:Cm " + game + " " + image_num + ".png]]"
	
	for line in ("==Chapter data==", "{{ChapDataMap", victory_line, defeat_line, 
				 ally_line, other_line, enemy_line, map_line,"}}"):
		chapter_data += line + "\n"
		
	#==================================================
	
	# Building character data
	
	game_num = game[2:]
	
	character_data = "===Character Data=== \n" + \
					 "{{ChapChars \n" + \
					 "|game#=" + game_num + " \n"
					 
	if new_units_data != None:
		
		number_of_new_units = str(len(new_units_data))
		
		formatted_new_units = "|newunits = " + number_of_new_units + "\n"
		
		for unit_num, new_unit in enumerate(new_units_data, 1):
			
			unit_name = new_unit[0]
			unit_data = new_unit[1]
			
			unit_portrait = "[[File:portrait " + unit_name.lower() + " " + game + ".png]]" 
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
					   
	#=============================================================
	
	# Building item data
	
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
			
	item_data_section = "===Item data=== \n" + \
					    "{{ChapItems \n" + \
					    "|platform=gba \n" + \
					    formatted_item_data + "}}"
	
	#=============================================================
	
	# Building shop data
	
	shop_data_section = "===Shop Data=== \n"
	
	if shops_info == None:
		shop_data_section = ""
	
		
	elif len(shops_info) == 1:
		
		shop_info = shops_info[0]
		
		shop_name = shop_info[0]
		shop_items = shop_info[1]

		shop_data_start = """
{|style="margin-left:auto; margin-right:auto; width: 500px; border: 2px solid {{Color2}}; {{round}}; background: {{Color3}};"
{{!}}<div style="{{round}}; border: 2px solid {{Color2}}; background: {{Color1}}; text-align:center; padding:3px;"><big>'''""" + shop_name +"""'''</big></div>
{{tablebegin}} class=wikitable style="{{round}}; border-collapse:separate; border:none;" align="center"
 !style="{{roundl}}; border: 1px solid {{Color2}}; background: {{Color1}}; width: 5%" {{!}}
 !style="border: 1px solid {{Color2}}; background: {{Color1}}; width: 30%" {{!}} Name
 !style="{{roundr}}; border: 1px solid {{Color2}}; background: {{Color1}}; width: 15%" {{!}} Cost
 {{!-}} """
 
		formatted_items = format_shop_items(shop_items)
		
		for part in (shop_data_start, formatted_items, "{{tableend}}", "|}"):
			shop_data_section += part + "\n"

			
	else:
	
		header_line = "|header = " + shop_data_header
		
		for line in ("{{Tab",
					 header_line,
					 "|width = 700px",
					 "|height = ",
					 "|constyle = text-align:center"):
						 
			shop_data_section += line + "\n"
			
		for shop_num, shop_info in enumerate(shops_info, 1):
			
			shop_num = str(shop_num)
			shop_name = shop_info[0]
			
			shop_tab = ""
			
			for line in ("|tab" + shop_num + " = " + shop_name + "\n", 
						 "|content" + shop_num + " = {{clear}}"):
							 
				shop_tab += line
		
			tab_add = """
{{tablebegin}} class=wikitable style="{{round}}; border-collapse:separate; border:none;" align="center"
 !style="{{roundl}}; border: 1px solid {{Color2}}; background: {{Color1}}; width: 5%" {{!}}
 !style="border: 1px solid {{Color2}}; background: {{Color1}}; width: 30%" {{!}} Name
 !style="{{roundr}}; border: 1px solid {{Color2}}; background: {{Color1}}; width: 15%" {{!}} Cost
 {{!-}}
 """
			shop_tab += tab_add
			
			shop_items = shop_info[1]
			
			formatted_items = format_shop_items(shop_items)		
			shop_tab += formatted_items  
						
			shop_tab += "{{tableend}} \n"							 
			shop_data_section += shop_tab + "\n"
				
		shop_data_section += "}}"
	
	#==============================================================
	
	# Building enemy data
	
	enemy_data = build_enemy_data(enemy_name, 
								  enemy_data, boss_data, 
								  reinforcement_data)
								  
	#==============================================================
	
	# Building boss data
	
	boss_data_section = "===Boss Data=== \n" + \
						"{{Main|" + boss_name + "}}" + \
						detailed_boss_data
	
	#==============================================================
	
	# Building chapter navigator
	
	chapter_navigator_section = ""
	
	if prealternate != None:
		prealternate_line = "|prealternate = " + prealternate
	else:
		prealternate_line = ""
		
	if nextalternate != None:
		nextalternate_line = "|nextalternate = " + nextalternate
	else:
		nextalternate_line = ""
		
												
	for line in ("{{ChapterNav",
				 "|prechapter = " + prechapter,
				  prealternate_line,   
				 "|chapter = " + chapter_title, 
				 "|nextchapter = " + nextchapter, 
				 nextalternate_line,
				 "}}"):
		
		chapter_navigator_section += line + "\n"
											    
	#==============================================================
	
	# Building strategy section
	
	if strategy == None:
		strategy_body = "{{sectstub}}"
		
	else:
		strategy_body = strategy
		
	strategy_section = ""
	
	for part in ("==Strategy==", strategy_body):
		strategy_section += part + "\n"
		
	#==============================================================
	
	# Building trivia section
	
	trivia_section = ""
	
	if trivia == None:
		trivia_body = ""
	else:
		trivia_body = trivia
		
	for part in ("==Trivia==", trivia_body):
		trivia_section += part + "\n"
	
	#==============================================================
	
	chapter_nav_dict = {"fe06" : "{{Nav6}}", 
						"fe07" : "{{Nav7}}", 
						"fe08" : "{{Nav8}}", }
						
	chapter_nav = chapter_nav_dict[game]
	
	chapter_category_dict = {"fe06" : "[[Category:Chapters of Fire Emblem: The Binding Blade]]", 
				"fe07" : "[[Category:Chapters of Fire Emblem: Blazing Sword]]", 
				"fe08" : "[[Category:Chapters of Fire Emblem: The Sacred Stones]]", }
				
	chapter_category = chapter_category_dict[game]
	
	last_section = ""
	
	for line in (strategy_section,
				 trivia_section,
				 "==Gallery==",
				 "{{sectstub}}",
				 "",
				 "==Etymology and other languages==",
				 "{{Names",
				 "|eng-name=" + chapter_title,
				 "|eng-meaning=",
				 "}}",
				 chapter_navigator_section,
				 chapter_nav,
				 chapter_category):
				 
		last_section += line + "\n"
	
	chapter_page = ""
	
	for section in (stub_mark, 
					chapter_infobox, 
					chapter_desciption, 
					plot_section, 
				    chapter_data, 
				    character_data,
				    item_data_section, 
				    shop_data_section, 
				    enemy_data,
				    boss_data_section,
				    last_section):
						
		chapter_page += section + "\n"
											 
	return chapter_page
	
	
	
#=======================================================================

# Basic chapter info

chapter_title = "Test Chapter"
image_num = "1"
game = "fe07"
location = "Sacae"
new_units = ["Lyn"]
bosses = ["Bazba"]

chapter_desciption = \
"""'''Test Chapter''' is a mock chapter page designed to 
demonstrate the program. 
"""

chapter_plot = """
chapter plot goes here
"""

beginning_log = """ 
beginning log goes here
"""

victory_condition = "Sieze the throne"
defeat_condition = "[[Lyn]] dies"
ally = "1"
other = "0"
enemy = "1"

return_characters = \
[] 



# New units data is organized:
#  ["unit name", ["class", "HP", "level", "recruit method"]]

# ["", ["", "", "", ""]], 

new_units_data = \
[["Lyn", ["Lord", "1", "1", "Automatically at the start"]]]


# Item data is formatted:
#	[item name, obtain method]

# ["", ""], 

item_data = \
[["Mani Katti", "Automatically at the state"], 
["Vulnerary ", "Visit [[village]]"], ]


shop_data_header = "Shop Data"

# Shop info is formatted:
#	[shop name, [item1, item2, item3]], 

# ["", ["", "", ""]], 

shops_info = \
[["Armory",["Slim Lance", "Iron Lance", "Steel Lance"]],
["Vendor", ["Fire", "Thunder", "Lightning"]], ]

enemy_name = "Bandit"

# Unit data is formatted:
# 	[class, level, quantity, inventory]

# Boss data is formatted:
# 	["name", "class", "level", inventory]

# ["", "", "", [""]], 

boss_data = \
["Bazba", "Brigand", "1", ["Steel Axe"]]

enemy_data = \
[["Brigand", "1", "1", ["Iron Axe"]], 
["Brigand", "2", "1", ["Iron Axe"]], ]

reinforcement_data = \
[["Brigand", "3", "1", ["Iron Axe"]], ]


boss_name = "Bazba"

# Insert boss data

detailed_boss_data = """
"""

# Insert prechapter and nextchapter.

prechapter = "A Girl from the Plains"
nextchapter = "Footsteps of Fate"

# Insert prealternate or next alternate if they exist,
# otherwise input "None".

prealternate = None
nextalternate = None

# Insert trivia and strategy

strategy = """
strategy goes here
"""
trivia = """
trivia goes here
"""

# Takes every varaiable and constructs a chapter page.

chapter_page = build_chapter_page(chapter_title, 
								  image_num,
								  game,
								  location,
								  new_units,
								  chapter_desciption,
								  chapter_plot,
								  beginning_log,
								  victory_condition,
								  defeat_condition,
								  ally,other,enemy,
								  return_characters,
								  new_units_data,
								  item_data,
								  shop_data_header,
								  shops_info,
								  enemy_name,
								  enemy_data,
								  boss_data,
								  reinforcement_data,
								  boss_name,
								  detailed_boss_data,
								  prechapter,
								  nextchapter,
								  prealternate,
								  nextalternate,
								  strategy,
								  trivia)

print(chapter_page)


