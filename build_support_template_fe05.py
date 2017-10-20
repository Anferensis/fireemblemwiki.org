#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Written by Albert"Anferensis"Ong

Builds a support template for Fire Emblem: Thracia 776 for fireemblemwiki.org
"""

def format_portrait(character_name):
	
	lowered_name = character_name.lower()
	formatted_portrait = "[[File:Portrait " + lowered_name + " fe05.png]]"
	
	return formatted_portrait


def build_support_template_fe05(character_data, 
								supports_g, 
								supports_o):
	
	support_template = "{{SupportSysFE5 \n"
	
	character_name = character_data[0]
	character_class = character_data[1]
	
	character_portrait = format_portrait(character_name)
	
	portrait_line = "|portrait=" + character_portrait
	name_line = "|character=" + character_name
	class_line = "|class=" + character_class
	
	for line in (portrait_line, 
				 name_line, 
				 class_line):
		
		support_template += line + "\n"
	
	
	if supports_g != None:
	
		supports_g_num = str(len(supports_g))
		support_template += "|supportsg=" + supports_g_num + "\n"
		
		
		for num, support_data in enumerate(supports_g, 1):
			
			support_num = str(num)
			support_name = support_data[0]
			support_class = support_data[1]
			support_bonus = support_data[2]
			
			portrait_line = "|portraitg" + support_num + "=" + format_portrait(support_name)
			name_line = "|supportg" + support_num + "=" + support_name
			class_line = "|classg" + support_num + "=" + support_class
			bonus_line = "|bonusg" + support_num + "=" +  support_bonus
			
			for line in (portrait_line, 
						 name_line, 
						 class_line, 
						 bonus_line):
				
				support_template += line + "\n"
	
	
	if supports_o != None:
		
		supports_o_num = str(len(supports_o))
		support_template += "|supportso=" + supports_o_num + "\n"
				
		for num, support_data in enumerate(supports_o, 1):
			
			support_num = str(num)
			support_name = support_data[0]
			support_class = support_data[1]
			support_bonus = support_data[2]
			
			portrait_line = "|portraito" + support_num + "=" + format_portrait(support_name)
			name_line = "|supporto" + support_num + "=" + support_name
			class_line = "|classo" + support_num + "=" + support_class
			bonus_line = "|bonuso" + support_num + "=" +  support_bonus
			
			for line in (portrait_line, 
						 name_line, 
						 class_line, 
						 bonus_line):
				
				support_template += line + "\n"
		
		
	support_template += "}} \n"
	
	return support_template
	
	
#=======================================================================


# Character data is organized:
#	[name, class]
character_data = ["Robert", "Bow Knight"]

# Support data is organized:
#	[name, class, support bonus]

#	["", "", ""], 

supports_g = \
None

supports_o = \
[["Glade", "Duke Knight", "10"], 
["Selfina", "Arch Knight", "10"], ]

print("==Supports== \n" + build_support_template_fe05(character_data, 
								  supports_g, 
								  supports_o))




