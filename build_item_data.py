
"""
Written by Albert"Anferensis"Ong

A program that builds item data for fireemblemwiki.org
"""



def build_item_data(platform, item_data, item_data_note):
	"""
	A function designed to build an item data template
	for fireemblemwiki.org. 
	"""
	
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
				 
				 "Fire" : "Fire (tome)",
				 "Thunder" : "Thunder (tome)",
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
					
	return item_data_section


					    
#=========================================================================



def main():
	
	# Insert platform
	# 	such as gba, gcn, or wii

	platform = "wii"

	# Item data is formatted:
	#	[item name, obtain method]

	# ["", ""], 

	item_data = \
	[["Iron Sword", "Obtain method 1"], 
	["Iron Lance", "Obtain method 2"], 
	["Iron Axe", "Obtain method 3"], ]

	# Insert item_data_note
	# 	If no note is needed, insert "None".
	item_data_note = None


	item_data_section = build_item_data(platform, 
										item_data, 
										item_data_note)
										
	print(item_data_section)
	
	saveTextFile = False
	
	if saveTextFile:
		
		file_writer = open("build_item_data.txt", "w")
		file_writer.write(item_data_section)
		file_writer.close()
		
		print("Text saved to file: build_item_data.txt")



if __name__ == "__main__":
	main()
					    

