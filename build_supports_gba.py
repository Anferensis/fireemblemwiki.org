#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Written by Albert"Anferensis"Ong

Builds a support template for fireemblemwiki.org
"""


def build_supports_gba(game, 
					   character_data,
					   support_data):

	support_template = "==Supports== \n"
	
	if support_data != None:
		
		character_name = character_data[0]
		character_class = character_data[1]
		character_affinity = character_data[2]
		
		lowered_name = character_name.lower()
		character_portrait = "[[File:portrait " + lowered_name + " " + game + ".png]]"
		
		support_num_line = "|supports=" + str(len(support_data))
		portrait_line =    "|portrait=" + character_portrait
		character_line =   "|character=" + character_name
		class_line = 	     "|class=" + character_class
		affinity_line =    "|affin=" + character_affinity
		
		
		for line in ("{{SupportSysGBA", 
					 support_num_line, 
					 portrait_line,
					 character_line, 
					 class_line, 
					 affinity_line): 
						 
			support_template += line + "\n"
		
		
		for unit_num, unit_data in enumerate(support_data, 1):
			
			unit_num = str(unit_num)
			unit_name = unit_data[0]
			unit_class = unit_data[1]
			unit_affinity = unit_data[2]
			initial_points = unit_data[3]
			additional_points = unit_data[4]
			
			lowered_unit_name = unit_name.lower()
			unit_portrait = "[[File:small portrait " + lowered_unit_name + " " + game + ".png]]"
			
			name_line = "|support" + unit_num + "=" + unit_name
			class_line = "|class" + unit_num + "=" + unit_class
			portrait_line = "|port" + unit_num + "=" + unit_portrait
			affinity_line = "|affin" + unit_num + "=" + unit_affinity
			initial_points_line = "|initialpoints" + unit_num + "=" + initial_points
			additional_points_line = "|plus" + unit_num + "=" + additional_points		
			
			for line in (name_line, 
						 class_line, 
						 portrait_line, 
						 affinity_line, 
						 initial_points_line, 
						 additional_points_line):
				
				support_template += line + "\n"
			
		
		support_template += "}}"
		
		return support_template
		
	else:
		return None
		
	
	
#=======================================================================


def main():
	game = "fe07"

	# Character data is organized:
	# 	[name, class, affinity]

	character_data = ["Karla", "Swordmaster", "dark"]

	# Unit support data is organized:
	#	[name, class, affinity, initial points, additional points]

	support_data = [["Karel", "Swordmaster", "light", "25", "+2"], 
					["Bartre", "Fighter", "thunder", "5", "+4"],
					["Farina", "Pegasus Knight", "anima", "0", "+2"], 
					["Vaida", "Wyvern Lord", "fire", "0", "+2"]]

	supports_section = build_supports_gba(game, 
										  character_data, 
										  support_data)
												  
	print(supports_section)
												  

												  
if __name__ == "__main__":
	main()




