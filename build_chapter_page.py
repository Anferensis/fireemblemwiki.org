#!/usr/bin/env python
# -*- coding: utf-8 -*- 

"""
Written by Albert"Anferensis"Ong

A program designed to build a chapter page for fireemblemwiki.org.

Note: This program has only been tested for Fire Emblem 5, 6, 7, and 8.
It may not function properly for other titles. 
"""

# A list of items and their prices in various Fire Emblem titles.
# This is used for building shop data.
# Note: these lists are not comprehensive


price_list_fe03 = {"Iron Sword" : "420", 
				   "Steel Sword" : "760",
				    
				   "Iron Lance" : "380", 
				   "Steel Lance" : "560", 
				   "Javelin" : "600",
				    
				   "Iron Bow" : "330", }


# The price list for Fire Emblem: Thracia 776
			  
price_list_fe05 = {"Iron Sword" : "2,200", 
				   "Slim Sword" : "2,600", 
				   "Steel Sword" : "2,900", 
				   "Iron Blade" : "2,000", 
				   "Silver Sword" : "4,200",
				   "Killing Edge" : "3,800", 

				   "Iron Lance" : "1,100", 
				   "Steel Lance" : "3,200",
				   "Slim Lance" : "2,000",
				   "Silver Lance" : "4,000",
				   "Killer Lance" : "3,000", 
				   
				   "Iron Axe" : "2,200", 
				   "Steel Axe" : "1,700",
				   "Silver Axe" : "4,200", 
				   "Hand Axe" : "1,000", 
				   "Hammer" : "1,200", 
				   "Killer Axe" : "2,000", 
				   
				   "Iron Bow" : "2,200", 
				   "Steel Bow" : "3,200",
				   "Silver Bow" : "4,000",
				   "Killer Bow" : "3,200", 
				   				   
				   "Fire" : "2,250", 
				   "Thunder" : "3,200",
				   "Wind" : "2,200", 
				   "Elfire" : "3,200", 
				   "Lightning" : "3,200", 
				   
				   "Heal" : "2,200",
				   "Mend" : "2,300", 
				   
				   "Vulnerary" : "600",
				   "Antitoxin" : "1,500",
				   "Torch" : "500",   
				   "Door Key" : "500", 
				   "Stamina Drink" : "5,000",
				   "Knight Proof" : "8,000", 
				   
				   "Life Ring" : "8,000", 
				   "Speed Ring" : "8,000", 
				   "Skill Ring" : "8,000", 
				   "Energy Ring" : "8,000", 
				   "Shield Ring" : "8,000", }


# Price list for the gba titles. 

price_list_gba = {"Slim Sword" : "480", 
			  "Iron Sword" : "460",
			  "Steel Sword" : "600",
			  "Silver Sword" : "1,500",
			  "Iron Blade" : "980",
			  "Steel Blade" : "1,250",
			  "Silver Blade" : "1,800",
			  "Lancereaver" : "1,800",
			  "Armorslayer" : "1,260",
			  "Longsword" : "1,260",
			  "Killing Edge" : "1,300",
			  "Light Brand" : "1,250",
			  
			  "Slim Lance" : "450", 
			  "Iron Lance" : "360", 
			  "Steel Lance" : "480", 
			  "Silver Lance" : "1,200",
			  "Javelin" : "400", 
			  "Axereaver" : "1,950",
			  "Heavy Spear" : "1,200",
			  "Horseslayer" : "1,040",
			  "Killer Lance" : "1,200",
			  
			  "Iron Axe" : "270", 
			  "Steel Axe" : "270",
			  "Silver Axe" : "1,000", 
			  "Hand Axe" : "300",
			  "Swordreaver" : "2,100",
			  "Hammer" : "800",
			  "Halberd" : "810",
			  "Killer Axe" : "1,000",
			  "Battle Axe" : "1,000",
				  
			  "Iron Bow" : "540", 
			  "Steel Bow" : "720", 
			  "Silver Bow" : "1,600",
			  "Killer Bow" : "1,400",
			  "Short Bow" : "1,760",
			  "Longbow" : "2,000",
			  
			  "Fire" : "420", 
			  "Thunder" : "500",
			  "Elfire" : "800", 
			  "Aircalibur" : "1,100", 
			  "Bolting" : "3,000", 
			  
			  "Lightning" : "540", 
			  "Shine" : "900", 
			  "Divine" : "1,250",
			  "Purge" : "3,500", 
			   
			  "Flux" : "780", 
			  "Nosferatu" : "3,000", 
			  "Eclipse" : "4,000", 
			  
			  "Heal" : "600", 
			  "Mend" : "1,000",
			  "Recover" : "2,250",
			  "Physic" : "3,750",
			  "Torch Staff" : "1,000",
			  "Unlock": "1,500",
			  "Barrier" : "2,250",
			  "Restore" : "2,000",
				  
			  "Vulnerary" : "300", 
			  "Antitoxin" : "450",
			  "Pure Water" : "900", 
			  "Door Key" : "50",
			  "Elixir": "3,000", 
			  "Chest Key": "1,500",
			  "Lockpick" : "2,400", 
			  "Torch" : "500", 
			  
			  "Knight Crest" : "10,000", 
			  "Hero Crest" : "10,000", 
			  "Elysian Whip" : "10,000", 
			  "Orion's Bolt" : "10,000", 
			  "Guiding Ring" : "10,000", 
			  "Ocean Seal" : "50,000",
			  "Fell Contract" : "50,000",
			  "Earth Seal" : "20,000",
			  
			  
			  "Angelic Robe" : "8,000", 
			  "Energy Ring" : "8,000",
			  "Secret Book" : "8,000", 
			  "Speedwings" : "8,000", 
			  "Goddess Icon" : "8,000", 
			  "Dragonshield" : "8,000", 
			  "Talisman" : "8,000", 
			  "Body Ring" : "8,000", 
			  "Boots" : "8,000", 
			  }





def hyperlink(link, display_text = None):
	
	if display_text != None:
		formatted_link = "[[" + link + "|" + display_text +"]]"
		
	else:
		formatted_link = "[[" + link + "]]"
	
	return formatted_link



def format_shop_items(platform, game, shop_items):
	
	formatted_shop_items = ""
				  
	for item_name in shop_items:
		
		item_name_lowered = item_name.lower()
		
		
		if game in ("fe06", "fe07", "fe08"):
			item_price = price_list_gba[item_name]
			
		elif game  == "fe05":
			item_price = price_list_fe05[item_name]
			
		elif game == "fe03":
			item_price = price_list_fe03[item_name]
		
		special_cases = {"Fire" : "Fire (tome)", 
						 "Thunder" : "Thunder (tome)", 
						 "Luna" : "Luna (tome)", 
						 "Wind" : "Wind (tome)",
						 "Eclipse" : "Eclipse (tome)",  
						 
						 "Berserk" : "Berserk (staff)",
						 "Sleep" : "Sleep (staff)", 
						 "Warp" : "Warp (staff)", 
						 "Silence" : "Silence (staff)", 
						 "Stone" : "Stone (tome)", 
						 
						 "Torch" : "Torch (item)"}
						 
		if item_name in special_cases:
			
			link = special_cases[item_name]			
			item_link = hyperlink(link, item_name)
			
		else:
			item_link = hyperlink(item_name)
		
		line1 =  "{{!}} style={{roundl}}; {{!}} [[File:Is " + platform + " " + \
				 item_name_lowered + ".png|right]]" 		          
		line2 = "{{!}} " + item_link
		line3 = "{{!}} style={{roundr}}; text-align: center {{!}} " + item_price
		line4 =  "{{!-}}"
		
		formatted_item_data = ""
		
		for line in (line1, line2, line3, line4):
			formatted_item_data += line + "\n"
			
		formatted_shop_items += formatted_item_data
		
	return formatted_shop_items



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
			
			disimbaguation_cases = \
				{"Fire" : "Fire (tome)", 
				 "Thunder" : "Thunder (tome)", 
				 "Luna" : "Luna (tome)", 
				 "Wind" : "Wind (tome)",
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
				 
				 "Adept Manual" : "Skill items"}
				 
			special_cases = \
				{"Beak (raven)" : "Beak", 
				 "Beak (hawk)" : "Beak", 
				 "Claw (cat)" : "Claw", 
				 "Claw (tiger)" : "Claw", }
							 
			if item_name in disimbaguation_cases:
				
				link = disimbaguation_cases[item_name]			
				item_link = hyperlink(link, item_name)
			
			elif item_name in special_cases:
				link = special_cases[item_name]
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



def build_chapter_page(hatnote, 
					   platform, 
					   chapter_title, 
					   image_num,
					   game,
					   location,
					   new_units,
					   bosses,
					   weather,
					   quote,
					   quote_speaker,
					   chapter_desciption, 
					   chapter_plot,
					   beginning_log,
					   chapter_data_infobox,  
					   return_characters,
					   new_units_data,
					   character_data_note,
					   item_data,
					   item_data_note,
					   shop_data_header,
					   shops_info,
					   enemy_data,					   
					   reinforcement_data,
					   enemy_data_note,
					   print_units_total,
					   npc_data,
					   npc_data_note,
					   boss_name,
					   detailed_boss_data,
					   chapter_navigator_section, 
					   strategy,
					   trivia,
					   chapter_etymology,
					   gallery_text,
					   isStub = True):
	"""
	A function designed to build a chapter page for fireemblemwiki.org.
	"""					   
	
		
	if not isStub:
		stub_mark = ""
		
	else:
		stub_mark = "{{stub}}"
	
	#==========================================================
	
	# Building chapter info box.
		
	chapter_infobox = "{{Chapter Infobox \n"
	
	title_line = "|title=" + chapter_title
	image_line = "|image=[[File:Cm " + game + " " + image_num +".png|200px]]"
	
	if location == None:
		formatted_location = ""
	
	elif location.endswith(" (link)"):
		location =  location[:-7]
		formatted_location = hyperlink(location)
		
	else:
		formatted_location = location
	
	location_line = "|location=" + formatted_location
	
	new_units_line = "|new units="
	
	
	if type(new_units) == list:
		
		for unit_num, unit_name in enumerate(new_units, 1):
			formatted_unit_name = "[[" + unit_name + "]]"
			
			if unit_num != len(new_units):
				formatted_unit_name += ", "
				
			new_units_line += formatted_unit_name
		
	elif type(new_units) == str:
		new_units_line += new_units
		
	elif new_units == None:
		new_units_line += "none"
	
		
	bosses_line = "|boss="	
	
	for boss_num, boss_title in enumerate(bosses, 1):
		formatted_boss_name = "[[" + boss_title + "]]"
		
		if boss_num != len(bosses):
			formatted_boss_name += ", "
			
		bosses_line += formatted_boss_name
	
	
	if weather == None:
		weather_line = "|weather="
		
	else:
		weather_line = "|weather=" + weather 
	
	
	for line in (title_line, 
				 image_line, 
				 location_line, 
				 new_units_line, 
				 bosses_line,
				 weather_line):
					 
		chapter_infobox += line + "\n"
	
	chapter_infobox += "}}"
	
	#=========================================================
	
	# Building chapter quote
	
	if quote == None or quote_speaker == None:
		chapter_quote = ""
		
	else:
		chapter_quote = "{{Quote|" + quote + "|" + quote_speaker + "}}"
	
	#=========================================================

	# Building plot section
	
	plot_section = ""
	
	if chapter_plot == None:
		plot_body = "{{sectstub}}"
	else:
		plot_body = chapter_plot
		
	if beginning_log == None:
		beginning_log_section = ""
		
	else:
		beginning_log_section = "===Beginning Log=== \n" + \
								beginning_log
		
	for part in ("==Plot==",
				 "{{main|" + chapter_title + "/Script}} \n",
				 plot_body,
				 beginning_log_section):
		
		plot_section += part + "\n"
	
	#=========================================================
	
	# Building chapter data
	
	chapter_data = "==Chapter Data== \n" + chapter_data_infobox
		
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
			
			if game != "fe09":
				unit_portrait = "[[File:portrait " + unit_name.lower() + " " + game + ".png]]" 
			else:
				unit_portrait = "[[File:Small portrait " + unit_name.lower() + " " + game + ".png]]" 
				
			unit_class = unit_data[0]
			unit_HP = unit_data[1]
			unit_level = unit_data[2]
			unit_recruitment = unit_data[3]
			
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
		
		special_exceptions = {"alva" : "Alva (Thracia 776)", 
							  "robert" : "Robert (Thracia 776)",
							  "ced" : "Ced (character)", 
							  "marth 02" : "Marth", 
							  "lance" : "Lance (character)"}
							  
		if char_name in special_exceptions:
			
			char_article = special_exceptions[char_name]
			article_line = "|return" + char_num + "article=" + char_article
			
			character_data += article_line + "\n"
		
	
	character_data += "}} \n"
	
	if character_data_note == None:
		pass
	else:
		character_data += character_data_note
					   
	#=============================================================
	
	# Building item data
	
	if item_data == None:
		item_data_section = None
	
		
	else:
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
			
			
			item_link_exceptions = \
				{"Berserk" : "Berserk (staff)",
				 "Sleep" : "Sleep (staff)", 
				 "Warp" : "Warp (staff)",
				 "Rescue" : "Rescue (staff)",
				 "Silence" : "Silence (staff)", 
				 
				 "Noba Scroll" : "Crusader Scrolls", 
				 "Counter Scroll" : "Skill items", 
				 "Vantage Scroll" : "Skill items",
				 "Guard Scroll" : "Skill items",
				 
				 "Wind" : "Wind (tome)", 
				 "Torch" : "Torch (item)", 
				 "Eclipse" : "Eclipse (tome)",
				 
				 "Binding Blade" : "Binding Blade (weapon)"}
				 
			if item_name in item_link_exceptions:
				item_link = item_link_exceptions[item_name]
				item_article_line = "|item" + item_num + "article=" + item_link
				 
			else:
				item_article_line = None
			
				
			item_image_exceptions = {"Magic Up" : "m up"}
			
			if item_name in item_image_exceptions:
				item_image = item_image_exceptions[item_name]
				item_image_line = "|item" + item_num + "image=" + item_image
				 
			else:
				item_image_line = None
				
			
			for line in (item_line, 
						 item_article_line, 
						 item_image_line, 
						 obtain_line):
														 
				if line != None:
					formatted_item_data += line + "\n"
		
		
		if item_data_note == None:
			add_note = ""
		else:
			add_note = item_data_note
							
		item_data_section = ""
		
		for section in ("===Item Data=== ", 
						"{{ChapItems ",
						"|platform=" + platform, 
						formatted_item_data + "}}", 
						add_note):
			
			item_data_section += section + "\n"
	
	
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
 
		formatted_items = format_shop_items(platform, game, shop_items)
		
		for part in (shop_data_start, formatted_items, "{{tableend}}", "|}"):
			shop_data_section += part + "\n"

			
	else:
	
		header_line = "|header=" + shop_data_header
		
		for line in ("{{Tab",
					 header_line,
					 "|width=700px",
					 "|height=",
					 "|constyle=text-align:center"):
						 
			shop_data_section += line + "\n"
			
		for shop_num, shop_info in enumerate(shops_info, 1):
			
			shop_num = str(shop_num)
			shop_name = shop_info[0]
			
			shop_tab = ""
			
			for line in ("|tab" + shop_num + "=" + shop_name + "\n", 
						 "|content" + shop_num + "={{clear}}"):
							 
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
			
			formatted_items = format_shop_items(platform, game, shop_items)		
			shop_tab += formatted_items  
						
			shop_tab += "{{tableend}} \n"							 
			shop_data_section += shop_tab + "\n"
				
		shop_data_section += "}}"
	
	
	#==============================================================
	
	# Building enemy data
	
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
		
		if reinforcement_data != None:
			
			for unit_data in reinforcement_data:
				
				try:
					unit_number = int(unit_data[3])
					
					reinforcement_quantity = unit_number
					reinforcement_total += reinforcement_quantity
					
				except ValueError:
					pass
							
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
		 
	if enemy_data_note != None:
		enemy_data_section += enemy_data_note + "\n"
	
	
	#==============================================================
	
	# Building NPC data section
	
	if npc_data == None:
		npc_data_section = ""
		
	elif npc_data == "stub":
		npt_data_section = "===NPC Data=== \n" + \
						   "{{sectstub}} \n"
		
	else:
		npc_data_section = ""
		
		for line in ("===NPC Data===", 
					 "{{ChapOthers", 
					 "|platform=" + platform):
						 
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
			inventory_line = build_unit_inventory(platform, unit_inventory, unit_num)
			
			for line in (name_line, 
						 class_line, 
						 level_line, 
						 quantity_line, 
						 inventory_line):
							 
				npc_data_section += line + "\n"
				
			npc_data_section += "\n"
				
		npc_data_section += "}} \n"
		
	
	if npc_data_note == None:
		pass
		
	else:
		npc_data_section += npc_data_note + "\n"
	
									  
	#==============================================================
	
	# Building boss data
	
	
	if boss_name != None:
		boss_redirect_line = "{{Main|" + boss_name + "}}"
		
	else:
		boss_redirect_line = None
	
	
	boss_data_section = ""
						
	for line in ("===Boss Data===", 
				 boss_redirect_line, 
				 detailed_boss_data):
					 
		if line != None:
			boss_data_section += line + "\n"
											    
	#==============================================================
	
	# Building strategy section
	
	if strategy == None:
		strategy_body = "{{sectstub}}"
		
	else:
		strategy_body = "{{strategy}} \n" + strategy
		
	strategy_section = ""
	
	for line in ("==Strategy==", 
				 strategy_body):
					 
		strategy_section += line + "\n"
		
	#==============================================================
	
	# Building trivia section
	
	trivia_section = ""
	
	if trivia == None:
		trivia_body = ""
	else:
		trivia_body = trivia
		
	for line in ("==Trivia==", 
				 trivia_body):
		trivia_section += line + "\n"
		
	#==============================================================
	
	# Building etymology section
	
	etymology_section = "==Etymology and other languages== \n" + \
						chapter_etymology
		
	#==============================================================
	
	# Building gallery section
	
	gallery_section = "==Gallery== \n"
	
	if gallery_text == None:
		gallery_section_text = "{{sectstub}}"
		
	else:
		gallery_section_text = gallery_text
		
	gallery_section += gallery_section_text + "\n"
	
	#==============================================================
	
	# Building chapter navigator and chapter category
	
	chapter_nav_dict = \
		{"fe01" : "{{Nav1}}", 
		 "fe02" : "{{Nav2}}", 
		 "fe03" : "{{Nav3}}",
		 "fe04" : "{{Nav4}}",
		 "fe05" : "{{Nav5}}",
		 "fe06" : "{{Nav6}}", 
		 "fe07" : "{{Nav7}}", 
		 "fe08" : "{{Nav8}}", 
		 "fe09" : "{{Nav9}}", 
		 "fe10" : "{{Nav10}}", 
		 "fe11" : "{{Nav11}}", 
		 "fe12" : "{{Nav12}}", 
		 "fe13" : "{{Nav13}}", 
		 "fe14" : "{{Nav14}}", 
		 "fe15" : "{{Nav15}}", }
						
	chapter_nav = chapter_nav_dict[game]
	
	title_name_dict = \
		{"fe01" : "Fire Emblem: Shadow Dragon and the Blade of Light",
		 "fe02" : "Fire Emblem: Gaiden",
	     "fe03" : "Fire Emblem: Mystery of the Emblem",
	     "fe04" : "Fire Emblem: Genealogy of the Holy War",
	     "fe05" : "Fire Emblem: Thracia 776",
	     "fe06" : "Fire Emblem: The Binding Blade",
	     "fe07" : "Fire Emblem: Blazing Sword",
	     "fe08" : "Fire Emblem: The Sacred Stones",
	     "fe09" : "Fire Emblem: Path of Radiance",
	     "fe10" : "Fire Emblem: Radiant Dawn",
	     "fe11" : "Fire Emblem: Shadow Dragon",
	     "fe12" : "Fire Emblem: New Mystery of the Emblem",
	     "fe13" : "Fire Emblem: Awakening",
	     "fe14" : "Fire Emblem: Fates",
	     "fe15" : "Fire Emblem Echos: Shadows of Valentia",}
	     
	title_name = title_name_dict[game]
	
	chapter_category = "[[Category:Chapters of " + title_name + "]]"

	#==============================================================
	
	# Builds the complete chapter page
	
	chapter_page = ""
	
	for section in (hatnote,
					stub_mark, 
					chapter_infobox, 
					chapter_quote,
					chapter_desciption, 
					plot_section, 
				    chapter_data, 
				    character_data,
				    item_data_section, 
				    shop_data_section, 
				    enemy_data_section,
				    npc_data_section,
				    boss_data_section,
				    strategy_section, 
				    trivia_section, 
				    etymology_section, 
				    gallery_section,
					chapter_navigator_section,
					chapter_nav,
					chapter_category):
		
		if section != None:				
			chapter_page += section + "\n"
											 
	return chapter_page
	
	
	
#=======================================================================

hatnote = None

# Insert whether or not the page is a stub.
# If true, a stub mark will be placed at the top of the page.

isStub = True

# Insert platform name

platform = "gcn"


# Insert basic chapter info
# Note: New units will accept a list, a string, or "None"

chapter_title = "The Feral Frontier"
image_num = "15"
game = "fe09"
location = "[[Grann Desert]]" 
new_units = ["Stefan", "Muarim"]
bosses = ["Muarim"]
weather = None

# Insert beginning quote and the quote's speaker 
#	(this is primarily for aesthetics)

# if "None" is inputted for either, a quote will not appear

quote = "What? We're facing laguz? I don't like the look of this!"
quote_speaker = "[[Ike]]"


# Insert chapter description. 

chapter_desciption = \
"""'''The Feral Frontier''' (Japanese: {{hover|辺境の獣|Henkyō no kemono}}, ''Frontier of beasts'') is chapter 15 of {{FE9}}."""


# Insert chapter plot
# if "None is inputted", this section will be marked as a stub

chapter_plot = None

# Insert beginning log
# if there is no beginning log, input "None"

beginning_log = \
None

# Insert chapter infobox data

chapter_data_infobox = \
"""{{ChapDataMap
|victory=Defeat [[Muarim]]
|defeat=[[Ike]] dies 
|ally=14{{hover|+1|Stefan}}
|partner=0
|other=0
|enemy=20
|map=<br>{{Tab
|tab1=Map
|tab2=Hidden Items
|content1=[[File:Cm fe09 15.png]]
|content2=[[File:Cm fe09 15 hidden items.png]]
}}
}}
:''For more information on hidden items, see [[hidden items|here]].''"""

"""{{ChapDataMap
|victory=
|defeat=
|ally=
|partner=
|other=
|enemy=
|map=
}}"""

# Insert returning characters and new units data

return_characters = \
["Ike", "Titania", "Oscar", "Boyd", "Rhys", "Soren", "Mia", "Ilyana", 
"Mist", "Rolf", "Marcia", "Lethe", "Mordecai", "Volke", "Brom",
"Kieran", "Nephenee", "Zihark", "Sothe", "Jill", "Astrid", "Gatrie", 
"Makalov"]

  
# New units data is organized:
#  ["unit name", ["class", "HP", "level", "recruit method"]]

# ["", ["", "", "", ""]], 

# If there are no new units, input "None"

new_units_data = \
[["Stefan", ["Swordmaster", "38", "8", "Have [[Lethe]] or [[Mordecai]] step on one specific space on the map before any other unit does"]], 
["Muarim", ["Tiger", "45", "9", "Automatically at end of chapter"]], ]

# Insert note under character data 
# 	if no note is needed, insert "None"

character_data_note = None

# Insert item data

# Item data is formatted:
#	[item name, obtain method]

# ["", ""], 

item_data = \
[["Gold", "Automatically at preparations (10,000G)"], 
["Vulnerary", "Steal from [[laguz]]"], 
["Vulnerary", "Steal from [[laguz]]"], 
["Vulnerary", "Steal from [[laguz]]"], 
["Vulnerary", "Steal from [[laguz]]"], 
["Coin", "Find in sand"], 
["Coin", "Find in sand"], 
["Physic", "Find in sand"], 
["Shine", "Find in sand"], 
["Guard Scroll", "Find in sand"], 
["Silver Blade", "Find in sand"], 
["Boots", "Find in sand"], 
["Statue Frag", "Find in sand"], 
["White Gem", "Find in sand"], ]


# Insert note after under item data 
# 	if no note is needed, insert "None"

item_data_note = \
"""{{ChapBEXP
|req1=Clear in 7 turns or fewer
|easy1=450
|normal1=300
|hard1=150
|req2=For each enemy [[laguz]] alive (maximum 19)
|easy2=60
|normal2=40
|hard2=20
|req3=All enemy [[laguz]] survive
|easy3=450
|normal3=300
|hard3=150
|req4=Clear Bonus
|easy4=150
|normal4=100
|hard4=--
}}
"""

shop_data_header = "Shop Data"

# Insert shop data
# If there are no shops, input "None"

# Shop info is formatted:
#	[shop name, [item1, item2, item3]], 

# ["", ["", "", ""]], 

shops_info = \
None

# Unit data is formatted:
# 	[name, class, level, quantity, inventory]

# ["", "", "", "", [""]], 

enemy_data = \
[ ["Rebel", "Beast Tribe", "1", "1", ["Claw (cat)", "Vulnerary"]], 
["Rebel", "Beast Tribe", "2", "3", ["Claw (cat)"]], 
["Rebel", "Beast Tribe", "3", "1", ["Claw (cat)"]], 
["Rebel", "Beast Tribe", "4", "3", ["Claw (cat)"]], 
["Rebel", "Beast Tribe", "4", "1", ["Claw (cat)", "Vulnerary"]], 
["Rebel", "Beast Tribe", "5", "1", ["Claw (cat)"]], 
["Rebel", "Beast Tribe", "2", "1", ["Claw (tiger)"]], 
["Rebel", "Beast Tribe", "3", "1", ["Claw (tiger)", "Vulnerary"]], 
["Rebel", "Beast Tribe", "4", "1", ["Claw (tiger)"]], 
["Rebel", "Beast Tribe", "4", "1", ["Claw (tiger)", "Vulnerary"]],
["Rebel", "Bird Tribe", "2", "2", ["Beak (hawk)"]], 
["Rebel", "Bird Tribe", "1", "1", ["Beak (raven)"]], 
["Rebel", "Bird Tribe", "2", "2", ["Beak (raven)"]], 
["[[Muarim]]", "Tiger", "9", "1", ["Claw (tiger)", "Demi Band"]], ]

reinforcement_data = \
None

# Insert note under enemy data 
# 	if no note is needed, insert "None"

enemy_data_note = None

# A variable that will print the units total
# if true, the unit and reinforcements total will print before the chapter page. 

print_units_total = False

# Insert NPC data
# 	if there are no NPCs, input "None"

# NPC unit data is organized:
#	[name, class, level, quantity, [inventory]]

# ["", "", "", "", [""]], 

npc_data = \
None

# Insert note under enemy data 
# 	if no note is needed, insert "None"

npc_data_note = None


boss_name = "Muarim"

# Insert boss data

detailed_boss_data = """{{BossStats GCN
|portrait=[[File:Small portrait muarim fe09.png|Muarim]]
|class=Tiger
|affin=thunder
|lv=9
|HP=45
|str=23-3
|magic=4
|skill=17-2
|spd=18-1
|luck=11
|def=15-1
|res=8-1
|con=
|wght=44
|move=9
|inventory=[[File:Is gcn claw (tiger).png]] [[Claw]]<br>[[File:Is gcn demi band.png]] [[Demi Band]]
}}"""

strategy = None
trivia = None

chapter_etymology = """{{Names
|eng-name=The Feral Frontier
|eng-mean=--
|jap-name={{hover|辺境の獣|Henkyō no kemono}}
|jap-mean=Frontier of beasts
|span-name=Frontera salvaje
|span-mean=Savage frontier
|fren-name=Frontière sauvage
|fren-mean=Savage frontier
|ger-name=Wilde Tiere
|ger-mean=Wild Animals
|ital-name=Fronte remoto
|ital-mean=Remote front
}}
"""

"""{{Names 
|eng-fan-name=
|eng-fan-mean=
|jap-name=
|jap-mean=
}}
"""

"""{{Names 
|eng-name=
|eng-mean=--
|jap-name={{hover||}}
|jap-mean=
|span-name=
|span-mean=
|fren-name=
|fren-mean=
|ger-name=
|ger-mean=
|ital-name=
|ital-mean=
}}
"""

#~ # Insert gallery text
#~ # 	if "None" is inputted, this section will be marked a stub. 

gallery_text = None

chapter_navigator_section = \
"""{{ChapterNav
|prechapter=Training
|name=The Feral Frontier
|nextchapter=The Atonement
}}
"""

# Takes every varaiable and constructs a chapter page.

chapter_page = build_chapter_page(hatnote, 
								  platform, 
								  chapter_title, 
								  image_num,
								  game,
								  location,
								  new_units,
								  bosses,
								  weather,
								  quote,
								  quote_speaker,
								  chapter_desciption,
								  chapter_plot,
								  beginning_log,
								  chapter_data_infobox,  
								  return_characters,
								  new_units_data,
								  character_data_note,
								  item_data,
								  item_data_note, 
								  shop_data_header,
								  shops_info,
								  enemy_data,					   
								  reinforcement_data,
								  enemy_data_note,
								  print_units_total,
								  npc_data,
								  npc_data_note,
								  boss_name,
								  detailed_boss_data,
								  chapter_navigator_section, 
								  strategy,
								  trivia, 
								  chapter_etymology,
								  gallery_text, 
								  isStub)

print(chapter_page)


