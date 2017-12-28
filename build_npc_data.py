
"""
Written by Albert"Anferensis"Ong

Builds an NPC data section for fireemblemwiki.org

Revision: 12-27-2017
"""

from utilities import hyperlink, writeTextFile
from build_unit_inventory import build_unit_inventory
	

def build_npc_template(platform, npc_data):
	
	npc_template = "{{ChapOthers \n" + \
				   "|platform=" + platform + "\n"
	
	for unit_num, unit_data in enumerate(npc_data, 1):
		
		isLastUnit = unit_num == len(npc_data)
		
		if isLastUnit:
			unit_num = "l"
		else:
			unit_num = str(unit_num)
			
		unit_name = unit_data[0]
		unit_class = unit_data[1]
		unit_level = unit_data[2]
		unit_quantity = unit_data[3]
		unit_inventory = unit_data[4]
		
		name_line = 	 "|name" + unit_num + "=" + unit_name
		class_line = 	 "|class" + unit_num + "=" + unit_class
		level_line = 	 "|lv" + unit_num + "=" + unit_level
		quantity_line =  "|#" + unit_num + "=" + unit_quantity
		inventory_line = build_unit_inventory(platform, unit_inventory, unit_num)
		
		for line in (name_line, 
					 class_line, 
					 level_line, 
					 quantity_line, 
					 inventory_line):
						 
			npc_template += line + "\n"
			
		if not isLastUnit:
			npc_template += "\n"
			
		elif isLastUnit and line != inventory_line:
			npc_template += "\n"
	
	npc_template += "}} \n"
		   
	return npc_template



def build_npc_data(npc_data, npc_data_note):
	
	# If npc_data is equal to "None".
	if npc_data == None:
		
		# Assigns npc_data_section equal to "None".
		npc_data_section = None
	
	# If npc_data is equal to "stub"
	elif npc_data == "stub":
		
		# Creates a NPC data section marked as a stub. 
		npc_data_section = "===NPC data=== \n" + \
						   "{{sectstub}} \n"
	
	
	# If there is only one tab for the NPC data.	
	elif len(npc_data) == 1:
		
		npc_data_section = "===NPC data=== \n"
		
		tab_data = npc_data[0]
		
		platform = tab_data[0]
		npc_data = tab_data[2]
		
		npc_template = build_npc_template(platform, npc_data)
		npc_data_section += npc_template
	
	
	# If there is more than one tab for the npc_data.
	elif len(npc_data) > 1:
		
		npc_data_section = "===NPC data=== \n" + \
						   "{{Tab \n" + \
						   "|width=1000px \n"
						   
		for tab_num, tab_data in enumerate(npc_data, 1):
			
			tab_title = tab_data[1]
			tab_num = str(tab_num)
			
			tab_line = "|tab" + tab_num + "=" + tab_title
			
			npc_data_section += tab_line + "\n"
		
		
		for tab_num, tab_data in enumerate(npc_data, 1):
			
			tab_num = str(tab_num)
			platform = tab_data[0]
			npc_data = tab_data[2]
			
			npc_template = build_npc_template(platform, npc_data)
			
			tab_content = "|content" + tab_num + "=" + npc_template
			
			npc_data_section += tab_content
			
		npc_data_section += "}} \n"
		
	
	
	# Adds the NPC data note to the NPC data section, if the note
	# is not equal no "None".
	if npc_data_note != None:
		npc_data_section += npc_data_note
	
	
	
	return npc_data_section
	
	
	
#=======================================================================


def main():
	
	"""
	Insert NPC data. 
	
	NPC data is formatted:
	
		[[platform1, 
		  tab_name1,
		  npc_list1],
		  
		  [platform2, 
		  tab_name2,
		  npc_list2],
		  
		  (insert as many tabs as needed)
		 ]
	
	NPC data template:
	["", 
	 "", 
	 [["", "", "", "", None]], ]
	
	
	NPC list is formatted:
		[[name1, class1, level1, quantity1, inventory1], 
		 [name2, class2, level2, quantity2, inventory2], 
		 [name3, class3, level3, quantity3, inventory3], ]
		
	NPC list template:
		[["", "", "", "", None], 
		 ["", "", "", "", None], 
		 ["", "", "", "", None], ]
	"""

	npc_data = \
	[["snes02", 
	 "''Gaiden''", 
	[["[[Valbar]]", "Knight", "1", "1", None], 
	["[[Kamui]]", "Mercenary", "3", "1", None], 
	["[[Leon]]", "Archer", "4", "1", None], ]], 
	
	["3ds03", 
	 "''Echoes: Shadows of Valentia''", 
	 [["[[Valbar]]", "Knight", "1", "1", None], 
	 ["[[Kamui]]", "Mercenary", "3", "1", None], 
	 ["[[Leon]]", "Archer", "4", "1", None], ]]]
	

	# Insert NPC data note. If no note is needed, insert "None"
	npc_data_note = None
	
	
	# Build the NPC data section using the input above. 
	npc_data_section = build_npc_data(npc_data, npc_data_note)
	
	# Prints out the NPC data section. 
	print(npc_data_section)
	
	# Choose if you want to save the text to a text file. 
	savetoTextFile = False
	
	# If true, saves the text to a text file. 
	if savetoTextFile:
		writeTextFile("npc_data_section.txt", npc_data_section)



if __name__ == "__main__":
	main()


