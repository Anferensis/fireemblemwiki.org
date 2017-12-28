
"""
Written by Albert"Anferensis"Ong

A program that builds item data for fireemblemwiki.org

Revision: 12-27-2017
"""

from utilities import writeTextFile


# A dictionary for cases where a item's name is different
# from an item's page link. 
item_link_exceptions = \
	{ # Status staves. 
	 "Berserk" : "Berserk (staff)",
	 "Sleep" : "Sleep (staff)", 
	 "Warp" : "Warp (staff)",
	 "Rescue" : "Rescue (staff)",
	 "Silence" : "Silence (staff)", 
	 
	 # Skill scrolls from Thracia 776. 
	 "Nihil Scroll" : "Skill items", 
	 "Noba Scroll" : "Crusader Scrolls",
	 "Corrosion Scroll" : "Skill items",  
	 "Counter Scroll" : "Skill items", 
	 "Vantage Scroll" : "Skill items",
	 "Guard Scroll" : "Skill items",
	 "Gamble Scroll" : "Skill items",
	 "Parity Scroll" : "Skill items", 
	 "Provoke Scroll" : "Skill items", 
	 "Savior Scroll" : "Skill items",  
	 "Shade Scroll" : "Skill items", 
	 "Smite Scroll" : "Skill items", 
	 "Renewal Scroll" : "Skill items",
	 "Resolve Scroll" : "Skill items",
	 "Wrath Scroll" : "Skill items", 			  
	 
	 # Common tomes. 
	 "Fire" : "Fire (tome)",
	 "Thunder" : "Thunder (tome)",
	 "Wind" : "Wind (tome)", 
	 "Eclipse" : "Eclipse (tome)",
	 
	 # Other items. 
	 "Torch" : "Torch (item)", 
	 "Binding Blade" : "Binding Blade (weapon)"}


# A dictionary for cases where an item's name is different from
# an item's image name. 
item_image_exceptions = \
	{"Magic Up" : "m up"}


# A dictionary for image exceptions specifically for Fire Emblem Gaiden. 
# This is primarily due to the graphical limitations of the game. 
item_image_exceptions_fe02 = \
	{"Leather Shield" : "Shield", 
	 "Blessed Ring" : "Ring"}



def build_item_template(platform, item_list):
	"""
	Constructs a single item template given two variables
		1. platform - the name of the platform represented as a string. 
		2. item_list - a list of items and their obtainment methods. 
	"""
	
	item_template = "{{ChapItems \n" + \
					"|platform=" + platform + "\n"
	
		
	for item_num, item in enumerate(item_list, start = 1):
		
		if item_num == len(item_list):
			item_num = "last"
		else:
			item_num = str(item_num)
			
		item_name = item[0]
		obtain_method = item[1]
		
		item_line = "|item" + item_num + "=" + item_name
		obtain_line = "|obtain" + item_num + "=" + obtain_method
		
			 
		if item_name in item_link_exceptions:
			item_link = item_link_exceptions[item_name]
			item_article_line = "|item" + item_num + "article=" + item_link
			 
		else:
			item_article_line = None
		
		
		item_image_line = None
		
		if item_name in item_image_exceptions:
			item_image = item_image_exceptions[item_name]
			item_image_line = "|item" + item_num + "image=" + item_image
		
		if platform in ("nes02", "3ds03") and item_name in item_image_exceptions_fe02:
			item_image = item_image_exceptions_fe02[item_name]
			item_image_line = "|item" + item_num + "image=" + item_image


		for line in (item_line, 
					 item_article_line, 
					 item_image_line, 
					 obtain_line):
													 
			if line != None:
				item_template += line + "\n"
		
	item_template += "}} \n"
		
	return item_template



def build_item_data(item_data, item_data_note):
	"""
	A function designed to build an item data template
	for fireemblemwiki.org. 
	"""
	
	# If item data is equal to "None"
	if item_data == None:
		
		# item_data_section is set equal to "None"
		# This is primarily for cases where a chapter page does not
		# need an item data section. 
		item_data_section = None
	
	
	# If item_data is equal to "stub"	
	elif item_data == "stub":
		
		# Creates an item data section that is marked as a stub. 
		item_data_section = "===Item data=== \n" + \
							"{{sectstub}} \n"
	
	
	# For the case where there is only one tab. 	
	elif len(item_data) == 1:
		
		item_tab_data = item_data[0]
		platform = item_tab_data[0]
		item_list = item_tab_data[2]
		
		item_template = build_item_template(platform, item_list)
							
		item_data_section = ""
		
		for section in ("===Item data=== ", 
						item_template, 
						item_data_note):
			
			if section != None:
				item_data_section += section + "\n"
	
	
	# For cases where there is more than one tab. 			
	elif len(item_data) > 1:
		
		item_data_section = "===Item data=== \n" + \
							"{{Tab \n" + \
							"|width=1000px \n"
							
		for tab_num, tab_data in enumerate(item_data, 1):
			
			tab_num = str(tab_num)
			tab_name = tab_data[1]
			
			tab_name_line = "|tab" + tab_num + "=" + tab_name + "\n"
			
			item_data_section += tab_name_line
		
			
		for tab_num, tab_data in enumerate(item_data, 1):
			
			tab_num = str(tab_num)
			tab_platform = tab_data[0]
			tab_item_list = tab_data[2]
			
			item_template = build_item_template(tab_platform, tab_item_list)
			
			item_tab = "|content" + tab_num + "=" + item_template
			
			item_data_section += item_tab
		
		item_data_section += "}} \n"
					
	return item_data_section


					    
#=========================================================================


def main():
	
	"""
	Insert item data. 
	Item data is formatted:
	
	[[platform1, 
	  tab_name1,
	  item_list1],
	  
	  [platform2, 
	  tab_name2,
	  item_list2],
	  
	  (insert as many tabs as needed)
	 ]
	
	Item data template:
	["", 
	 "", 
	 [["", ""], ], ]
	
	
	Item list is formatted:
		[[item1, obtain_method1], 
		 [item2, obtain_method2], 
		 [item3, obtain_method3], ]
		 
	Item list template:
		[["", ""], ]
	"""
	
	item_data = \
	[["nes02", 
	 "''Gaiden''", 
	 [["Blessed Ring", "Dropped by [[necrodragon]]"]]],
	 
	 ["3ds03", 
	 "''Echoes: Shadows of Valentia''", 
	 [["Blessed Ring", "Dropped by [[necrodragon]]"]]]]
	

	# Insert item_data_note
	# 	If no note is needed, insert "None".
	item_data_note = None

	
	# Builds the item data section based on the input above. 
	item_data_section = build_item_data(item_data, 
										item_data_note)
										
	# Prints out the item data section. 
	print(item_data_section)
	
	# Insert whether you want the text to be saved to a text file. 
	saveTextFile = False
	
	# Saves the text to a text file. 
	if saveTextFile:	
		writeTextFile("build_item_data.txt", item_data_section)



if __name__ == "__main__":
	main()
					    

