
"""
Written by Albert"Anferensis"Ong

A program that builds item data for fireemblemwiki.org
"""

def build_item_data(platform, item_data):
	
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
	
	item_data_section = ""
	
	for section in ("===Item Data===", 
					"{{ChapItems", 
					"|platform=" + platform, 
					formatted_item_data + "}}", ):
					 
		item_data_section += section + "\n"
			
	return item_data_section


					    
#=========================================================================

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

print(build_item_data(platform, item_data))

					    

