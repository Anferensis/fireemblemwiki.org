#!/usr/bin/python
# -*- coding: utf-8 -*- 

"""
Written by Albert "Anferensis" Ong

Created: 2022.02.13
"""

def build_heroes_artwork(hero, epithet, heading = False):
  
  output = ""
  
  for num in ("01", "02", "02a", "03"):
    
    file_name = " ".join(["FEH", hero, epithet, num + ".png"])
    file_caption = " ".join(["Artwork of", hero + ":", epithet, "from {{title|Heroes}}.\n"])
    
    output += "".join([file_name, "|", file_caption])
    
  
  if heading: 
    output = "===''Heroes'' artwork===\n<gallery>\n" + output + "</gallery>"
  
  return output


#=======================================================================


for hero, epithet in (("Marth", "Hero-King"), ):

  artwork = build_heroes_artwork(hero, epithet)
  
  print(artwork)
  print()
  
