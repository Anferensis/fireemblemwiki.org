
"""
Written by Albert"Anferensis"Ong

Constructs a sprite gallery for fireemblemwiki.org

Note: This program has only been tested for Fire Emblem 4, 5, 6, 7, and 8.
It may not function properly for other titles. 
"""

from utilities import hyperlink 



def build_sprite_gallery(character_name, 
						 character_type, 
						 title_num, 
						 sprite_data):
	"""
	A function designed to build a sprite gallery for fireemblemwiki.org. 
	"""
	
	sprite_gallery = \
"""{| class="mw-collapsible mw-collapsed" style="margin-left: auto; margin-right: auto; width: 75%; border: 2px solid {{Color2}}; background: {{Color1}}; {{round}}"
|-
! style="border: 1px solid {{Color2}}; width: 50%; background: {{Color1}}; {{round}}" align="center" | """
	
	lowered_name = character_name.lower()
	

	
	if title_num in ("fe06", "fe07", "fe08") and character_type in ("playable", "boss"):
		small_character_portrait = \
			"[[File:Small portrait " + lowered_name + " " + title_num + ".png]]"
		first_line = small_character_portrait + "Sprite Gallery"
		
	else:
		first_line = "Sprite Gallery"
	
	
	sprite_gallery += first_line + "\n" + \
					  "|- \n" + \
					  "|"
	
	
	character_portrait = \
		"[[File:Portrait " + lowered_name + " " + title_num + ".png]] \n"
		
	class_columns = """{| style="width: 100%; background: {{Color3}}; {{round}}; border: 1px solid {{Color2}}"
| align="center" rowspan="3" | """ + character_portrait 
	
	
	for num, class_data in enumerate(sprite_data, 2):
		class_name = class_data[0]
		
		column_num = str(len(class_data[1]))

		column_line = """| style="border-left: 1px solid {{Color2}}; border-bottom: 1px solid {{Color2}}" align="center" colspan=""" 		
		column_line += column_num + " | " + hyperlink(class_name)
		
		
		class_columns += column_line + "\n"
	
	class_columns += "|- \n"	
	
	for class_data in sprite_data:
			
		class_name = class_data[0]
		class_weapons = class_data[1]
		

		
		for num, weapon_name in enumerate(class_weapons, 1):
			
			if weapon_name.endswith("(dismounted)"):
				
				dismt_section = "dismt"
				
				weapon_name = weapon_name[:-13]
			
			else:
				dismt_section = None
		
			if num == 1:
				new_line = '| style="border-left: 1px solid {{Color2}}" align="center" | '
			
			else:
				new_line = '| align="center" | '
			
			
			lowered_class = class_name.lower()				
			lowered_weapon = weapon_name.lower()
			
			battle_sprite = ""
			
			for section in ("[[File:Bs " + title_num, 
							lowered_name, 
							dismt_section,
							lowered_class, 
							lowered_weapon + ".png]]"):
				
				if section != None:			
					battle_sprite += section + " "
				
			
			# A dictionary for cases where a weapon name is not the 
			# same as the link name. 
			link_exceptions = \
				{"Lance" : "Lance (weapon)", 
				 "Anima" : "Anima (magic)", 
				 "Light" : "Light (magic)", 
				 "Dark" : "Dark (magic)", 
				 "Magic" : "Magic (element)"}
			
			# If the weapon name is a link exception...
			if weapon_name in link_exceptions:
				
				# Properly formats the link. 
				link = link_exceptions[weapon_name]
				weapon_link = hyperlink(link, weapon_name)
			
			
			# Otherwise simply hyperlinks the weapon. 	
			else:
				weapon_link = hyperlink(weapon_name)
			
			
			new_line += battle_sprite + "<br>" + weapon_link
			
			
			if dismt_section != None:
				new_line += "{{hover|*|dismounted}}"
			
			class_columns += new_line + "\n"
			
	
	sprite_gallery += "\n" + class_columns + "|}\n|}\n"
	
	
	return sprite_gallery



#========================================================================


def main():

	# Enter character name
	character_name = "Fred"

	# Enter character type, either "playable", "boss", or "NPC"
	character_type = "playable"

	# Enter title num
	# 	Such as fe01, fe02, fe03 ...

	title_num = "fe05"


	# Enter sprite data

	# Sprite data is organized
	#	[class, [weapon1, weapon2, weapon3]]

	# ["", [""]], 

	sprite_data = \
	[["Paladin", ["Sword", "Lance", "Sword (dismounted)"]], ]
	
	
	# Builds the sprite gallery. 
	sprite_gallery = build_sprite_gallery(character_name, 
										  character_type, 
										  title_num, 
										  sprite_data)								  
	# Prints out the sprite gallery. 
	print(sprite_gallery)



if __name__ == "__main__":
	main()
		

