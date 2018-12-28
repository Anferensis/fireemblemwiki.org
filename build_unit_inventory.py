
"""
Written by Albert"Anferensis"Ong

A function that contructs a unit's inventory.
This is used exclusively in build_enemy_data.py and build_npc_data.py.

Revision: 27.12.2018
"""

from utilities import hyperlink, writeTextFile

# A dictionary for cases where an item's name is different
# from an item's page name. 
link_exceptions = \
  {"Fire" : "Fire (tome)", 
   "Thunder" : "Thunder (tome)", 
   "Luna" : "Luna (skill)", 
   "Wind" : "Wind (tome)",
   "Light": "Lightning",
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
   
   "Adept Manual" : "Skill items",
   "Adept Scroll" : "Skill items", 
   "Occult Scroll" : "Skill items",
   "Provoke Scroll" : "Skill items",  
   "Guard Scroll" : "Skill items",
   "Gamble Scroll" : "Skill items", 
   
   "Renewal" : "Renewal (skill)",
   "Guard" : "Cancel", 
   "Cancel" : "Pavise"}


# A dictionary for cases where an item's name is different 
# from an item's image name.  
image_exceptions = \
  {"Beak (raven)" : "Beak", 
   "Beak (hawk)" : "Beak", 
   "Claw (cat)" : "Claw", 
   "Claw (tiger)" : "Claw", 
   
   "Breath (red)" : "Breath (laguz)", 
   "Breath (white)": "Breath (laguz)"}


# A dictionary for image exceptions specifically for Fire Emblem Gaiden. 
# This is primarily due to the graphical limitations of the game. 
image_exceptions_fe02 = \
  {"Leather Shield" : "Shield", 
   "Dracoshild" : "Shield", 
   "Steel Shield" : "Shield", 
   
   "Brave Sword" : "Sword",
   "Shadow Sword" : "Sword", 
   
   "Javelin" : "Lance", 
   
   "Steel Bow" : "Bow",
   
   "Miasma" : "Black Magic", 
   "Incarnation" : "Skill Class", 
   
   "Blessed Ring" : "Ring", 
   "Angel Ring" : "Ring", 
   "Mage Ring" : "Ring"}



def build_unit_inventory(platform, 
                         inventory_data, 
                         unit_line_num, ):
  """
  Properly formats a unit's inventory data.
  
  Accepts a list of strings, where every string is an item name, 
  and string, representing the unit's number.
  
  Converts such that 
  build_unit_inventory("gba", ["Iron Sword", "Steel Sword (drop)"], "2")
  
  returns:
  |inventory2=[[File:Is gba iron sword.png]][[Iron Sword]] • [[File:Is gba steel sword.png]]{{drop|Steel Sword}}
  """

  formatted_inv = "|inventory" + unit_line_num + "="
  
  # If inventory data is equal to "None"
  if inventory_data == None:
    
    # The formatted inventory is just two hypens, 
    # representing a blank inventory. 
    formatted_inv += "--"
  
  # Otherwise, if there is inventory data...
  else:
    
    # For loops the list of items
    for item_num, item_name in enumerate(inventory_data, 1):
      
      # The name of the item is put entirely in lower case    
      lowered_item_name = item_name.lower()
      
      # Formatting a dropped item. 
      if item_name.endswith(" (drop)"):
        item_name = item_name[:-7]
        lowered_item_name = lowered_item_name[:-7]
        
        # Checks if the game is one of the Tellius games. 
        is_tellius = platform in ("gcn", "wii")
        
        if item_name in link_exceptions and is_tellius:
          link = link_exceptions[item_name]
          item_link = "{{drop|" + item_name + "|article=" + link +"|color=Tellius}}"  
        
        elif is_tellius:
          item_link = "{{drop|" + item_name + "|color=Tellius}}"
        
        elif item_name in link_exceptions:
          link = link_exceptions[item_name]
          item_link = "{{drop|" + item_name + "|article=" + link +"}}"   
           
        else:
          item_link = "{{drop|" + item_name + "}}"    
      
      # Changes the item link if the item's name is different
      # from the item's page link.             
      elif item_name in link_exceptions:
        
        link = link_exceptions[item_name]     
        item_link = hyperlink(link, item_name)
      
      # Changes the item image if the item's image is different
      # from the item's name. 
      elif item_name in image_exceptions:
        link = image_exceptions[item_name]
        item_link = hyperlink(link)
      
      # Otherwise the item link is just the item's name. 
      else:
        item_link = hyperlink(item_name)
      
      
      if platform in ("nes02", "3ds03") and item_name in image_exceptions_fe02:
        lowered_item_name = image_exceptions_fe02[item_name].lower()
          

      item_image = "[[File:Is " + platform + " " + lowered_item_name + ".png]]"
      
      # Creates the formatted item data, which includes a link directed 
      # towards the item sprite and a hyperlink to the item itself
      formatted_item = item_image + item_link
      
      # Checks if the item is the last item. 
      is_last_item = item_num == len(inventory_data)
      
      # Adds the formatted item data to the formatted inventory 
      if not is_last_item:
        formatted_inv += formatted_item + " • "
      else:
        formatted_inv += formatted_item
      
  
  # By the end of the for loop, the inventory should be
  # properly formatted.   
  return formatted_inv



#=======================================================================


def main():
  
  # Sample inventory input. 
  platform = "wii"
  inventory = ["Iron Sword", "Iron Lance", "Iron Axe"]
  unit_line_num = "2"
  
  # Prints out the formatted sample imput. 
  # ~ print(build_unit_inventory(platform, inventory, unit_line_num))
  
  print(build_unit_inventory("gba", ["Iron Sword", "Steel Sword (drop)"], "2"))
  
  
if __name__ == "__main__":
  main()


