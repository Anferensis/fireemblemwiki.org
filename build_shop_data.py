
"""
Written by Albert"Anferensis"Ong

Builds shop data for fireemblemwiki.org

Revision: 08.19.2018
"""

from price_list import gametoPriceList
from utilities import hyperlink, writeTextFile


def format_shop_items(platform, game, shop_items):
	
	formatted_shop_items = ""
				  
	for item_name in shop_items:
		
		item_name_lowered = item_name.lower()
		
		# Retrieves the price list for a given Fire Emblem title	 
		price_list = gametoPriceList[game]
		
		# Retrieves the item price from the price list. 
		item_price = price_list[item_name]

		
		# A dictionary for cases where the item name 
		# is not the same as the page name.
		special_cases = \
			{"Fire" : "Fire (tome)", 
			 "Thunder" : "Thunder (tome)", 
			 "Luna" : "Luna (tome)", 
			 "Wind" : "Wind (tome)",
			 "Eclipse" : "Eclipse (tome)",
			 "Light" : "Light (tome)",  
			 
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
		
		# Adds each line to the formatted shop items. 
		for line in (line1, line2, line3, line4):
			formatted_shop_items += line + "\n"
		
		# ~ formatted_item_data = ""
		
		# ~ for line in (line1, line2, line3, line4):
			# ~ formatted_item_data += line + "\n"
			
		# ~ formatted_shop_items += formatted_item_data
		
	return formatted_shop_items



def build_shop_data(platform, 
					game, 
					shops_info, 
					header = None):

	shop_data_section = "===Shop data=== \n"
	
	if shops_info == None:
		shop_data_section = None
	
		
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
		
		return shop_data_section

			
	else:
	
		header_line = "|header=" + header
		
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
		
		return shop_data_section


	
#======================================================================


def main():
	
	# Insert the platform name and the game
	platform = "snes01"
	game = "fe03"

	# Insert the header.
	# (This will be the name of the table)
	header = "Shop data"

	"""
	Insert the shop data. 
	Shop info is formatted:
		[shop name, 
		 [item1, item2, item3, ...]], 
	
	Template:
		["", 
		["", "", ""]], 
	"""
			 
	shop_data = \
	[["''Mystery of the Emblem''", 
	 ["Iron Sword", "Iron Lance", "Javelin", "Iron Bow"]], 
	
	 ["''New Mystery of the Emblem''", 
	  ["Iron Sword", "Iron Lance", "Javelin", "Iron Axe", "Hand Axe", "Iron Bow"], ]]
				  
	shop_data_section = build_shop_data(platform, game, shop_data, header)
	print(shop_data_section)
	
	
	savetoTextFile = False
	
	if savetoTextFile:
		writeTextFile("shop_data_section.txt", shop_data_section)


if __name__ == "__main__":
	main()
	

