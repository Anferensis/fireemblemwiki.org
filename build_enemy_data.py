#!usr/bin/python3

"""
Written by Albert"Anferensis"Ong

Constructs an enemy data table for fireemblemwiki.org

Revision: 27.12.2018
"""

from utilities import hyperlink, writeTextFile
from build_unit_inventory import build_unit_inventory


def build_units_data(platform,
                     units_data,
                     isReinforcement = False):
  """
  Formats the units data for a ChapEnemies template. 
  his is used in build_enemy_template. 
  
  This function takes three arguments:
  
    1. platform
       The name of the game platform. 
       e.g. gba, gcn, wii...
       
    2. units_data
    
    3. isReinforcement
  """
  
  # A string that will become the formatted units data.          
  formatted_units_data = ""
  
  # Uses a for loop to examine each, individual unit's data. 
  for unit_num, unit_data in enumerate(units_data, 1):
    
    # Checks if the unit is the last unit in the list.
    is_last_unit = unit_num == len(units_data)
    
    # Converts the unit num into a string. 
    unit_num = str(unit_num)
    
      
    if is_last_unit and isReinforcement:
      unit_line_num = "rl"
      
    elif isReinforcement:
      unit_line_num = "r" + unit_num
    
    elif is_last_unit:
      unit_line_num = "b"
    
    else:
      unit_line_num = unit_num
    
    # Assemblesm the unit name, class, level, and quantity line.
    name_line      = "|name"  + unit_line_num + "=" + unit_data[0]
    class_line     = "|class" + unit_line_num + "=" + unit_data[1]
    level_line     = "|lv"    + unit_line_num + "=" + unit_data[2]
    quantity_line  = "|#"     + unit_line_num + "=" + unit_data[3]
    
    # Uses the build_unit_inventory function to assembly the 
    # unit inventory line. 
    inventory_line = build_unit_inventory(platform, unit_data[4], unit_line_num)   
    
    # Assembles the unit notes line, if it is needed. 
    unit_notes = unit_data[5]
    
    if unit_notes != None:
      notes_line = "|notes" + unit_line_num + "=" + unit_notes
    else:
      notes_line = None
    
    # A dictionary for cases where the class name if different
    # from the class page. 
    unit_class_exceptions = \
      {"Raven" : "Raven (laguz)", 
       "White Dragon" : "White Dragon (monster)"}
    
    if unit_data[1] in unit_class_exceptions:
      
      class_link = unit_class_exceptions[unit_class]
      class_article_line = "|class" + add_letter + unit_num + "article=" + class_link
    
    else:
      class_article_line = None 
    
    if unit_num == "b":
      quantity_line = None
                        
    formatted_unit_data = ""  
    
    for line in (name_line, 
                 class_line, 
                 class_article_line,
                 level_line, 
                 quantity_line, 
                 notes_line, 
                 inventory_line):
      
      if line != None:     
        formatted_unit_data += line
        
        if not is_last_unit:
          formatted_unit_data += "\n"
          
        elif is_last_unit and line != inventory_line:
          formatted_unit_data += "\n"
        
    formatted_units_data += formatted_unit_data


    # Adds a space between each unit's data if it is not the last unit. 
    if not is_last_unit:
      formatted_units_data += "|-\n"


  
  return formatted_units_data
  


def build_enemy_template(platform, 
                         enemy_data, 
                         reinforcement_data, 
                         print_units_total = False):
  """
  Constructs an individual ChapEnemies template. 
  This is used in build_enemy_data where each template represents
  each tab in the final enemy data. 
  
  This function takes four arguments:
  
    1. platform
       The name of the game platform. 
       e.g. gba, gcn, wii...
       
    2. enemy_data
       A list of all the enemy data. Enemy data is formatted:
       [[name1, class1, level1, quantity1, [item_1a, item_2a, ...]], 
        [name2, class2, level2, quantity2, [item_1b, item_2b, ...]], 
        ... ]
        
    3. reinforcement_data
       A list of all the reinforcement data. Reinforcement data is
       formatted identically to enemy_data:
       [[name1, class1, level1, quantity1, [item_1a, item_2a, ...]], 
        [name2, class2, level2, quantity2, [item_1b, item_2b, ...]], 
        ... ]
       If there are no reinforcements, input None. 
       
    4. print_units_total 
       A boolean variable that determines if the function prints out the
       total number of units. This feature is primarily for utility 
       purposes and does not affect the final output.
       This value is False by default. 
  """
  
  # If print_units_total is True...
  if print_units_total:
    
    # Calculates the total number of enemies. 
    enemy_total = 0
    
    for unit_data in enemy_data:
      unit_quantity = int(unit_data[3])
      enemy_total += unit_quantity
    
    # Calculates the number of reinforcements, if there are any. 
    reinforcement_total = 0
    
    if reinforcement_data != None:
      for unit_data in reinforcement_data:
        reinforcement_quantity = int(unit_data[3])
        reinforcement_total += reinforcement_quantity
    
    # Prints out the total number of enemies and reinforcements. 
    print("Enemy total: ", enemy_total)
    print("Reinforcement total: ", reinforcement_total) 
    
  #-------------------------------------------------------------------
  # Constructs the units data for the initial enemies.

  formatted_units_data = build_units_data(platform, enemy_data)
  
  # Constructs the units data for the reinforcements, if there are any.
  formatted_reinforcement_data = None 
  
  if reinforcement_data != None:
    formatted_reinforcement_data = build_units_data(platform, reinforcement_data, True)
    
  # Assembles the ChapEnemies template using the formatted enemy and
  # reinforcements units data. 
  enemy_template = ""
  
  for section in ("{{ChapEnemies", 
                  "|platform=" + platform, 
                  formatted_units_data,
                  formatted_reinforcement_data,
                  "}}" ): 
    
    # Ignores a section if it does not exist. 
    if section != None:   
      enemy_template += section + "\n"  
  
  # Returns the final ChapEnemies template. 
  return enemy_template



def build_enemy_data(enemy_data, 
                     enemy_data_note,
                     print_units_total):
  """
  A function that constructs an entire enemy data section on fireemblemwiki.org
  Used in build_chapter_page.py
  
  This function takes three arguments:
    1. 
    2. 
    3. print_units_total
  """
  
  number_of_tabs = len(enemy_data)
  
  # If there is only one tab in the enemy data...
  if number_of_tabs == 1:
    
    tab_data = enemy_data[0]
    
    platform = tab_data[0]
    initial_enemy_data = tab_data[2]
    reinforcement_data = tab_data[3]
    
    enemy_data_template = \
      build_enemy_template(platform, 
                 initial_enemy_data, 
                 reinforcement_data, 
                 print_units_total)
      
    enemy_data_section = \
      "===Enemy data===\n" + \
       enemy_data_template
   
   
  # If there is more than one tab in the enemy data...             
  elif number_of_tabs > 1:
    
    enemy_data_section = \
      "===Enemy data===\n" + \
      "{{Tab\n" + \
      "|width=1000px\n"
    
    
    # Adds the tab names
    for tab_num, tab_data in enumerate(enemy_data, 1):
      
      tab_num = str(tab_num)
      tab_name = tab_data[1]
      
      tab_line = "|tab" + tab_num + "=" + tab_name + "\n"
      enemy_data_section += tab_line
       
     
    # Adds the tab contents. 
    for tab_num, tab_data in enumerate(enemy_data, 1):
      
      tab_num = str(tab_num)
      
      platform = tab_data[0]
      initial_enemy_data = tab_data[2]
      reinforcement_data = tab_data[3]
      
      enemy_data_template = \
        build_enemy_template(platform, 
                   initial_enemy_data, 
                   reinforcement_data, 
                   print_units_total)
                   
      tab_content = "|content" + tab_num + "=" + enemy_data_template
      
      enemy_data_section += tab_content
      
      try:
        tab_note = tab_data[4]
        enemy_data_section += tab_note + "\n"
        
      except IndexError:
        pass
      
    enemy_data_section += "}}\n"

  
  # Adds the enemy data note to the enemy data section, 
  # if a note exists.    
  if enemy_data_note != None:
    enemy_data_section += enemy_data_note
  
  # Returns the finalized enemy_data_section
  return enemy_data_section


  
#======================================================================



def main():
  
  """ 
  Enemy data is formatted:
    [[platform1, 
      tab name2, 
      initial_enemy_data1, 
      reinforcement_data1, ] 
    
     [platform2, 
      tab name2, 
      initial_enemy_data2, 
      reinforcement_data2 ] 
      
      ... (for as many tabs as needed) 
      ]
   
  Initial enemy data and reinforcement data is formatted:
  
    [[name1, class1, level1, quantity1, [item1, item2, ...]]
     [name2, class2, level2, quantity2, [item1, item2, ...]]
     
     ...  (for as many units as needed)
     ]
  
  Sample enemy data:
     [
      # First tab data. 
      ["gba", 
       "Tab1 name", 
       
       # Initial enemy data. 
       [["Bandit", "Brigand", "1", "1", ["Iron Axe"], None], 
        ["Bandit", "Mercenary", "3", "1", ["Iron Sword", "Vulnerary (drop)"], "Does not move"], ], 
        
       # Reinforcement data. 
       None 
      ], 
      
      # Second tab data. 
      ["gba", 
       "Tab2 name", 
       
       # Initial enemy data. 
       [["Bandit", "Archer", "1", "1", ["Iron Bow"], None], 
        ["Bandit", "Mage", "3", "1", ["Fire", "Thunder"], None], ], 
      
       # Reinforcement data. 
       [["Bandit", "Cavalier", "2", "2", ["Iron Lance"], None], ]
      ], 
    ]
  
  Blank enemy data template:
    [
      ["", 
       "", 
       [], 
       None],
     
      ["", 
       "", 
       [], 
       None]
    ]
  """
  
  # Input enemy data. See comment above for formatting guide. 
  enemy_data = \
    [
      ["gba", 
       "Tab1 name", 
       [["Bandit", "Brigand", "1", "1", ["Iron Axe"], None], 
        ["Bandit", "Mercenary", "3", "1", ["Iron Sword", "Vulnerary (drop)"], "Does not move"], ], 
       None 
      ], 
    ]

  # Insert enemy data note.
  # If no note is needed, insert "None".
  enemy_data_note = None
  
  # Insert whether or not you want to print out the units total.
  print_units_total = False

  enemy_data_section = build_enemy_data(enemy_data, 
                                        enemy_data_note, 
                                        print_units_total)
  
  # Prints out the enemy data section.                     
  print(enemy_data_section)
  
  #---------------------------------------------------------------------
  
  # Insert whether you want to save the enemy data as a text file.
  savetoTextFile = False
  
  # Insert the name of the text file, assuming you want to save one. 
  file_name = "enemy_data.txt"
  
  if savetoTextFile:
    writeTextFile(file_name, enemy_data_section)
               

if __name__ == "__main__":
  main()


