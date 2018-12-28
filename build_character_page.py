#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Written by Albert"Anferensis"Ong

Constructs a character page for fireemblemwiki.org

Revision: 23.09.2018
"""

from build_sprite_gallery import build_sprite_gallery
from build_supports_fe05 import build_supports_fe05
from build_supports_gba import build_supports_gba
from utilities import writeTextFile


def build_character_page(isStub, 
                         game, 
                         character_name,
                         character_type, 
                         hatnote, 
                         character_infobox, 
                         quote, 
                         quote_speaker, 
                         character_description, 
                         role, 
                         character_stats, 
                         character_analysis, 
                         character_personality, 
                         character_data, 
                         support_data, 
                         character_endings, 
                         character_quotes, 
                         character_other_appearances, 
                         character_etymology, 
                         trivia, 
                         gallery, 
                         sprite_data):
  
  
  # Adds a stub mark, if the page is a stub. 
  
  if isStub:
    stub_mark = "{{stub}}"
  else:
    stub_mark = None
    
  #=====================================================================
  
  # Creating hatnote, if one is necessary. 
  
  if hatnote != None:
    hatnote_section = ":''" + hatnote + "'' \n" + \
                      "----"
  else:
    hatnote_section = None
  
  #=====================================================================
  
  # Constructs a quote that will go at the top of the page.
  # This is primarily for aethetic purposes. 
  
  if quote != None and quote_speaker != None:
    character_quote = "{{Quote|" + quote + "|" + quote_speaker + "}}"
  else:
    character_quote = None
  
  
  #=====================================================================
  
  # Building the role section.
  
  role_section = "===Role===\n"
  
  if role == None:
    role_section +=  "{{sectstub}}"
  else:
    role_section += role
  
  #=====================================================================
  
  # Building the stats section.
  
  stats_section = "===Starting stats and growth rates===\n"
  
  if character_stats == None:
    stats_section +=  "{{sectstub}} \n"
  else:
    stats_section += character_stats
  
  #=====================================================================
  
  # Building analysis section
  
  analysis_section = "====Analysis====\n" + \
                     "{{analysis}}\n"
  
  if character_analysis != None:
    analysis_section += character_analysis
    
  else:
    analysis_section += "{{sectstub}}\n"
  
  #=====================================================================
  
  # Building personality section
  
  personality_section = "==Personality and character== \n"
  
  if character_personality == None:
    personality_section += "{{sectstub}} \n"
  else:
    personality_section += character_personality
  
  #=====================================================================
  
  # Building supports section
  
  supports_section = build_supports_gba(game, 
                                        character_data, 
                                        support_data)
  
  #=====================================================================
  
  # Building the endings section.
  
  if character_endings != None:
    endings_section = "==Endings== \n" + \
               character_endings
  else:
    endings_section = None
  
  #=====================================================================
  
  # Building the quotes section.
  
  quotes_section = "==Quotes==\n"
  
  if character_quotes == None:
    quotes_section += "{{sectstub}}\n"
  else:
    quotes_section += character_quotes
  
  #=====================================================================
  
  # Building other appearances section
  
  other_appearances_section = "==Other appearances==\n"
  
  if character_other_appearances != None:
    other_appearances_section += character_other_appearances  
  
  
  #=====================================================================
  
  # Building trivia section
  
  trivia_section = "==Trivia==\n"
  
  if trivia != None:
    trivia_section += trivia
    
  #=====================================================================
  
  # Building etymology section
  
  etymology_section = "==Etymology and other languages== \n" + \
                      character_etymology
  
  #=====================================================================
  
  # Building gallery section
  
  gallery_section = "==Gallery== \n"

  sprite_gallery = build_sprite_gallery(character_name, 
                                        character_type, 
                                        game, 
                                        sprite_data)
  
  gallery_section += sprite_gallery  
  
  if gallery == None:
    gallery_section += "{{sectstub}} \n"
  else: 
    gallery_section += gallery
  
  #=====================================================================
  
  # Building chapter navigator and chapter category
  
  chapter_nav_dict = \
    {"fe01" : "{{Nav1}}", 
     "fe02" : "{{Nav2}}", 
     "fe03" : "{{Nav3}}",
     "fe04" : "{{Nav4}}",
     "fe05" : "{{Nav5}}",
     "fe06" : "{{Nav6}}", 
     "fe07" : "{{Nav7}}", 
     "fe08" : "{{Nav8}}", 
     "fe09" : "{{Nav9}}", 
     "fe10" : "{{Nav10}}", 
     "fe11" : "{{Nav11}}", 
     "fe12" : "{{Nav12}}", 
     "fe13" : "{{Nav13}}", 
     "fe14" : "{{Nav14}}", 
     "fe15" : "{{Nav15}}", 
     "ps1" : "{{NavTRS1}}"}
            
  chapter_nav = chapter_nav_dict[game]
  
  title_name_dict = \
    {"fe01" : "Fire Emblem: Shadow Dragon and the Blade of Light",
     "fe02" : "Fire Emblem: Gaiden",
       "fe03" : "Fire Emblem: Mystery of the Emblem",
       "fe04" : "Fire Emblem: Genealogy of the Holy War",
       "fe05" : "Fire Emblem: Thracia 776",
       "fe06" : "Fire Emblem: The Binding Blade",
       "fe07" : "Fire Emblem (GBA)",
       "fe08" : "Fire Emblem: The Sacred Stones",
       "fe09" : "Fire Emblem: Path of Radiance",
       "fe10" : "Fire Emblem: Radiant Dawn",
       "fe11" : "Fire Emblem: Shadow Dragon",
       "fe12" : "Fire Emblem: New Mystery of the Emblem",
       "fe13" : "Fire Emblem: Awakening",
       "fe14" : "Fire Emblem: Fates",
       "fe15" : "Fire Emblem Echos: Shadows of Valentia",
       "ps1" : "TearRingSaga: Yutona Heroes War Chronicles"}
       
  title_name = title_name_dict[game]
  
  character_type_dict = \
    {"playable" : "Playable characters in ", 
     "NPC" : "NPCs in ", 
     "boss" : "Bosses in ", }
     
  category_type = character_type_dict[character_type]
  
  chapter_category = "[[Category:" + category_type + title_name + "]]"
  
  #=====================================================================
  
  # Building final character page
  
  character_page = ""
  
  character_appearance_dict = \
    {"fe01" : "{{FE1}}", 
     "fe02" : "{{FE2}}", 
     "fe03" : "{{FE3}}",
     "fe04" : "{{FE4}}",
     "fe05" : "{{FE5}}",
     "fe06" : "{{FE6}}", 
     "fe07" : "{{FE7}}", 
     "fe08" : "{{FE8}}", 
     "fe09" : "{{FE9}}", 
     "fe10" : "{{FE10}}", 
     "fe11" : "{{FE11}}", 
     "fe12" : "{{FE12}}", 
     "fe13" : "{{FE13}}", 
     "fe14" : "{{FE14}}", 
     "fe15" : "{{FE15}}", 
     "ps1" : "{{TRS1}}"}
     
  character_appearance_title = character_appearance_dict[game]
  character_appearance_line = "==" + character_appearance_title + "=="
  
  for section in (stub_mark, 
                  hatnote_section, 
                  character_infobox,
                  character_quote, 
                  character_description, 
                  character_appearance_line,
                  role_section, 
                  stats_section, 
                  analysis_section, 
                  personality_section, 
                  supports_section,
                  endings_section,  
                  quotes_section,
                  other_appearances_section,
                  trivia_section, 
                  etymology_section,         
                  gallery_section, 
                  "{{ref}}",
                  "{{Project Characters}}", 
                  chapter_nav, 
                  chapter_category):
    
    if section != None:
      character_page += section + "\n"
    
  return character_page
  


#=======================================================================
#
# User input for creating a character page below.   
#
#=======================================================================

# Indicate whether or not the page is a stub. 
isStub = True

hatnote = None

game = "ps1"
character_name = "Afred"

# Insert character type
#  either playable, NPC, or boss

character_type = "playable"

# Insert the character infobox. 
character_infobox = """{{Character Infobox
|name=Alfred
|image=[[File:YHWC Alfred.png|200px]]
|caption=Artwork of Alfred from {{TRS1}}. 
|help_text=
|gender=Male
|race=Human
|age=
|family=
|nationality=
|titles=
|startingclass=
|voice=
|appearances=* {{TRS1}}
}}"""

quote = None
quote_speaker = None

character_description = """
(Japanese: {{hover|	アフリード|Afurīdo}} ''Alfred'') is a playable [[TearRingSaga:Sage|Sage]] in {{TRS1}}.
"""

role = None

character_stats = """
{{CharStats TRS1
|portrait=
|class=
|classname=
|lv=
|HP=
|str=
|mag=
|skill=
|spd=
|luck=
|def=
|wlv=
|move=

|inventory=
|skills=
|HP1=
|str1=
|magic1=
|skill1=
|spd1=
|luck1=
|def1=
|wlv1=
|move1=
|recruit=
}}

===Promotion stat gains===
{{PromotionGains
|class=
|hp=
|str=
|mag=
|skill=
|spd=
|def=
|move=
|weaponlvl=
}}
"""

"""
Blank character stats template

GBA titles

{{CharStats GBA
|portrait=[[File:Portrait fe06.png]]
|class=
|affin=
|lv=
|HP=
|str=
|skill=
|spd=
|luck=
|def=
|res=
|HP1=
|str1=
|skill1=
|spd1=
|luck1=
|def1=
|res1=
|con=
|aid=
|move=
|inventory
|recruit=
}}

- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 

Thracia 776

{{CharStats FE5
|portrait=[[File:Portrait fe05.png]]
|class=
|lv=
|HP=
|movestars=★★★★★
|authority=★★★★★
|move=
|str=
|magic=
|skill=
|spd=
|luck=
|def=
|PCC=
|build=
|aid=
|inventory=[[File:Is snes03 .png]] [[]]<br>
|skills=[[File:Is snes03 .png]] [[]]<br>
|recruit=
|HP1=
|str1=
|magic1=
|skill1=
|spd1=
|luck1=
|def1=
|build1=
|move1=
}}
"""

"""
 Blank promotion gains templates

GBA titles
===Promotion gains===
{{PromotionGains
|class= 
|hp=
|str=
|skill=
|spd=
|def=
|res=
|con=
|move=
|weaponlvl=
}}

Thracia 776
===Promotion gains===
{{PromotionGains
|class=[[]]
|hp=
|str=
|mag=
|skill=
|spd=
|def=
|con=
|move=
|weaponlvl=
}}
"""

# Insert analysis section.
character_analysis = None

# Insert personality section. 
character_personality = None

# Insert support data


# Character data is organized:
#   [name, class, affinity]

character_data = ["Xavier", "General", None]

# GBA unit support data is organized:
#  [name, class, affinity, initial points, additional points]

# Fire Emblem: Thracia 776 unit support data is organized:
#  [name, class, support bonus]

# ["", "", "", "", ""], 

support_data = \
None
        

character_endings = """
"""

# Insert quotes section. 
character_quotes = """===Death quotes===
"""

# Insert other appearances section. 
character_other_appearances = None

# Insert etymology section. 
character_etymology = """{{Names
|eng-fan-name=Alfred
|eng-fan-mean=
|jap-name={{hover|	アフリード|Afurīdo}}
|jap-mean=
}}
"""

# Etymology template. 
"""{{Names
|eng-name=
|eng-mean=
|jap-name=
|jap-mean=
|fren-mean=
|ger-name=
|ger-mean=
|span-name=
|span-mean=
|ital-name=
|ital-mean=
}}

{{Names
|eng-fan-name=
|eng-fan-mean=
|jap-name=
|jap-mean=
}}
"""

# Insert trivia section. 
trivia = None


# Sprite data is organized:
#  [class name, [weapon1, weapon2, weapon3]]

# ["", [""]], 

sprite_data = \
[["", [""]], ]

# Insert gallery section. 
gallery = """<gallery>
YHWC Alfred.png|Artwork of Alfred from {{TRS1}}.
</gallery>
"""

def main():
  
  # Takes every variable defined above and assembles a character page.
  character_page = \
    build_character_page(isStub, 
                         game, 
                         character_name,
                         character_type, 
                         hatnote, 
                         character_infobox, 
                         quote, 
                         quote_speaker, 
                         character_description, 
                         role, 
                         character_stats, 
                         character_analysis, 
                         character_personality, 
                         character_data, 
                         support_data, 
                         character_endings, 
                         character_quotes, 
                         character_other_appearances, 
                         character_etymology, 
                         trivia, 
                         gallery, 
                         sprite_data)
  
  
  # Prints the character page.            
  print(character_page)
  
  # Insert whether you want to save the character page as a text file.
  savetoTextFile = False
  
  # Insert the name of the text file, assuming you want to save one. 
  file_name = "character_page.txt"
  
  if savetoTextFile:
    writeTextFile(file_name, character_page)



if __name__ == "__main__":
  main()


