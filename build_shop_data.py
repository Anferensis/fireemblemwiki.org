
"""
Written by Albert"Anferensis"Ong

Builds shop data for fireemblemwiki.org

This program currently only supports the gameboy advance titles:
Fire Emblem: The Binding Blade, Fire Emblem: The Blazing Sword, and
Fire Emblem: The Sacred Stones.  
"""

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



def build_shop_data(shops_info, header = None):

	shop_data_section = "===Shop Data=== \n"
	
	if shops_info == None:
		shop_data_section = ""
		return shop_data_section
	
		
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
		
		return shop_data_section

			
	else:
	
		header_line = "|header = " + header
		
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
		
		return shop_data_section
	
#==================================================================

# A dictionary of puchaseable items in Fire Emblem and the price
# of each item.

# Note: the price list is not comprehensive

price_list = {"Slim Sword" : "480", 
			  "Iron Sword" : "460",
			  "Steel Sword" : "600",
			  "Silver Sword" : "1,500",
			  "Lancereaver" : "1,800",
			  "Armorslayer" : "1,260",
			  "Longsword" : "1,260",
			  "Killing Edge" : "1,300",
			  
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
			  "Steel Axe" : "360",
			  "Silver Axe" : "1,000", 
			  "Hand Axe" : "300",
			  "Swordreaver" : "2,100",
			  "Hammer" : "800",
			  "Halberd" : "810",
			  "Killer Axe" : "1,000",
				  
			  "Iron Bow" : "540", 
			  "Steel Bow" : "720", 
			  "Silver Bow" : "1,600",
			  "Killer Bow" : "1,400",
			  "Short Bow" : "1,760",
			  "Longbow" : "2,000",
			  
			  "Fire" : "560", 
			  "Thunder" : "700",
			  "Elfire" : "1,200", 
			  "Lightning" : "630", 
			  "Shine" : "900", 
			  "Divine" : "2,000", 
			  "Flux" : "900", 
			  
			  "Heal" : "600", 
			  "Mend" : "1,000",
			  "Recover" : "2,250",
			  "Physic" : "3,750",
			  "Torch" : "1,000",
			  "Unlock": "1,500",
			  "Barrier" : "2,250",
			  "Restore" : "2,000",
				  
			  "Vulnerary" : "300", 
			  "Antitoxin" : "450",
			  "Pure Water" : "900", 
			  "Door Key" : "50",
			  "Elixir": "3,000", 
			  "Chest Key": "1,500",
			  "Lockpick" : "1,200", 
			  
			  "Hero Crest" : "10,000", 
			  "Knight Crest" : "10,000", 
			  "Elysian Whip" : "10,000", 
			  "Orion's Bolt" : "10,000", 
			  "Guiding Ring" : "10,000", 
			  "Ocean Seal" : "50,000",
			  "Fell Contract" : "50,000",
			  "Earth Seal" : "20,000",
			  }

header = "Shop Data"

test_shop_data = [["Armory",
			     ["Iron Sword", "Iron Lance", "Iron Axe"]],
			     ["Vendor", 
			     ["Fire", "Thunder", "Heal"]] ]
			  

print(build_shop_data(test_shop_data, header))


