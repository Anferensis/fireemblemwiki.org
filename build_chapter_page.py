#!/usr/bin/env python
# -*- coding: utf-8 -*- 

"""
Written by Albert"Anferensis"Ong
A program designed to build a chapter page for fireemblemwiki.org.

Programs imported:
  1. build_character_data.py
  2. build_enemy_data.py
  3. build_item_data.py
  4. build_npc_data.py
  5. build_shop_data.py
  6. utilities.py

Note: This program has only been tested for Fire Emblem 2, 5, 6, 7, 8, and 9.
      It may not function properly for other titles. 
    
Revision: 28.12.2018
"""

# Importing functions from other fireemblemwiki scripts. 
from build_character_data import build_character_data
from build_enemy_data import build_enemy_data
from build_item_data import build_item_data
from build_npc_data import build_npc_data
from build_shop_data import build_shop_data   
from utilities import hyperlink, writeTextFile



def build_chapter_page(hatnote, 
                       platform, 
                       chapter_title, 
                       chapter_infobox,
                       game, 
                       quote,
                       quote_speaker,
                       chapter_desciption, 
                       insert_plot_section,
                       chapter_plot,
                       beginning_log,
                       chapter_data_infobox,  
                       character_data, 
                       character_data_note,
                       item_data,
                       item_data_note,
                       shop_data_header,
                       shops_info,
                       include_enemy_data, 
                       enemy_data,
                       enemy_data_note,
                       print_units_total,
                       npc_data,
                       npc_data_note,
                       boss_data,
                       chapter_navigator_section, 
                       include_strategy_section, 
                       strategy,
                       trivia,
                       chapter_etymology,
                       gallery_text,
                       isStub = True):
  """
  A function designed to build a chapter page for fireemblemwiki.org.
  """            
  
  # Creates a stub mark if the page is a stub.
  if isStub:
    stub_mark = "{{stub}}"
    
  # Otherwise, the stub mark is registered as "None"
  else:
    stub_mark = None
  
  #==============================================================
  
  # Building chapter quote
  
  if quote == None or quote_speaker == None:
    chapter_quote = None
    
  else:
    chapter_quote = "{{Quote|" + quote + "|" + quote_speaker + "}} \n"
  
  #==============================================================

  # Building plot section
  
  if insert_plot_section:
    plot_section = ""
    
    if chapter_plot == None:
      plot_body = "{{sectstub}}"
    else:
      plot_body = chapter_plot
      
    if beginning_log == None:
      beginning_log_section = ""
      
    else:
      beginning_log_section = "===Beginning Log=== \n" + \
                              beginning_log
                  
    for part in ("==Plot==",
                 "{{main|" + chapter_title + "/Script}}",
                 plot_body + "\n",
                 beginning_log_section):
      
      plot_section += part + "\n"
      
  else:
    plot_section = None
    
  #===================================================================
  
  # Building character data section
  
  character_data_section = \
    build_character_data(character_data, character_data_note)
             
  #===================================================================
  
  # Building item data. 
  
  item_data_section = build_item_data(item_data, item_data_note)
  
  #===================================================================
  
  # Building shop data
  shop_data_section = build_shop_data(platform, 
                                      game, 
                                      shops_info, 
                                      shop_data_header)
                    
  #===================================================================
  
  # Building enemy data
  
  if include_enemy_data:
    enemy_data_section = build_enemy_data(enemy_data, 
                                          enemy_data_note,
                                          print_units_total)
  else:
    enemy_data_section = None
  
  #===================================================================
  
  # Building NPC data section.
  npc_data_section = build_npc_data(npc_data, npc_data_note)
                
  #===================================================================
  
  # Building boss data section. 
  
  if boss_data != None:
    
    boss_data_section = \
      "===Boss data===\n" + \
      boss_data
      
  else:
    boss_data_section = None
                          
  #===================================================================
  
  # Building strategy section
  
  if include_strategy_section:
    
    if strategy != None:
      strategy_body = "{{strategy}} \n" + \
                 strategy
      
    else:
      strategy_body = "{{sectstub}}"
      
    strategy_section = \
      "==Strategy==\n" + \
      strategy_body + "\n"
      
  else:
    strategy_section = None
    
  #===================================================================
  
  # Building trivia section
  
  trivia_section = "==Trivia==\n"
  
  # Adds trivia text to the trivia section, if the trivia text
  # is not equal to "None".
  if trivia != None:
    trivia_section += trivia
    
  #===================================================================
  
  # Building etymology section
  
  etymology_section = "==Etymology and other languages==\n" + \
            chapter_etymology
    
  #===================================================================
  
  # Building gallery section
  
  gallery_section = "==Gallery==\n"
  
  if gallery_text == None:
    gallery_section_text = "{{sectstub}}"
    
  else:
    gallery_section_text = gallery_text
    
  gallery_section += gallery_section_text + "\n"
  
  #===================================================================
  
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
     "fe15" : "{{Nav15}}",}
  
  if chapter_navigator_section != None:
  
    if game in ("fe02", "fe15"):
      chapter_nav = "{{Nav2}} \n{{Nav15}}"
    else:
      chapter_nav = chapter_nav_dict[game]
      
  else:
    chapter_nav = None
  
  title_name_dict = \
    {"fe01" : "Fire Emblem: Shadow Dragon and the Blade of Light",
     "fe02" : "Fire Emblem Gaiden",
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
     "fe15" : "Fire Emblem Echoes: Shadows of Valentia"}
       
  title_name = title_name_dict[game]
  
  if game in ("fe02", "fe15"):
    chapter_category = "[[Category:Acts of Fire Emblem Gaiden]] \n" + \
               "[[Category:Acts of Fire Emblem Echoes: Shadows of Valentia]]"
  else:
    chapter_category = "[[Category:Chapters of " + title_name + "]]"

  #===================================================================
  
  # Builds the complete chapter page
  
  # Defines a string that will become the finalized chapter page.
  chapter_page = ""
  
  # Uses a for loop to access every section needed to create
  # the chapter page. 
  for section in (hatnote,
                  stub_mark, 
                  chapter_infobox, 
                  chapter_quote,
                  chapter_desciption, 
                  plot_section, 
                  chapter_data_infobox, 
                  character_data_section,
                  item_data_section, 
                  shop_data_section, 
                  enemy_data_section,
                  npc_data_section,
                  boss_data_section,
                  strategy_section, 
                  trivia_section, 
                  etymology_section, 
                  gallery_section,
                  chapter_navigator_section,
                  chapter_nav,
                  chapter_category):
    
    # Adds each section to the chapter page, if the section exists. 
    if section != None:       
      chapter_page += section + "\n"
  
  # By the end of this for loop, chapter_page will be a large string
  # that represents the text of the chapter page. 
  
  # Returns the finalized chapter page.        
  return chapter_page
  


#=======================================================================
#
# User input for creating a chapter page below.   
#
#=======================================================================

"""
Insert a hatnote. 
This is used for cases where a page needs disambiguation.

Example:
:''This page is about the chapter from <insert fire emblem game>. For other uses, see [[<insert page name>]].''
----


If no hatnote is needed, insert "None".
"""

hatnote = None

# Hatnote template:
""":''Hatnote text''
----"""

#=======================================================================

# Insert whether or not the page is a stub.
isStub = True

# Insert platform name
platform = "nes02"

# Insert the game number
# Such as fe01, fe02, fe03 ...
game = "fe02"

# Insert chapter title
chapter_title = "The Final Battle"

# Insert chapter infobox
chapter_infobox = \
"""{{Chapter Infobox 
|title=The Final Battle
|image=[[File:Cm fe02 c5 02.png|200px]]
|location=[[Duma Tower]]
|new units=None
|boss=[[Duma]], [[Jedah]], [[Gharn]], [[Marla]], [[Hestia]], [[Aurum]], [[Argentum]], [[Hades]], [[Cerberus]], [[Naberius]] 
}}"""

# Chapter infobox template
"""{{Chapter Infobox 
|title=
|image=[[File:Cm fe __ __.png|200px]]
|location=
|new units=
|boss=
|weather=
}}"""


"""
Insert a quote and the quote's speaker. 
This is primarily for aesthetic purposes.

If "None" is inputted for either the quote or quote speaker,
then a quote will not appear
"""

quote = None
quote_speaker = None


# Insert chapter description. 
chapter_desciption = \
"""'''The Final Battle''' (Japanese: {{hover|最終決戦|Saishū kessen}} ''Final Showdown'') is the final map of the final act of {{FE2}} and {{FE15}}. 
"""

#=======================================================================

# Insert if this page needs a plot section. 
insert_plot_section = False

# Insert chapter plot.
# If "None is inputted", this section will be marked as a stub.
chapter_plot = None

# Insert beginning log
# If there is no beginning log, insert "None"
beginning_log = \
None

#=======================================================================

# Insert chapter data template.
chapter_data_box = \
"""==Map data==
{{ChapDataMap
|victory=Defeat [[Duma]]
|defeat=[[Alm]] or [[Celica]] dies
|ally={{hover|20|10 from Alm's party and 10 from Celica's party}}
|other=0
|enemy=20{{hover|+reinforcements|number may vary}}
|map=[[File:Cm fe02 c5 m02.png|200px]]
}}
"""

# Chapter data template. 
"""{{ChapDataMap
|victory=
|defeat=
|ally=
|other=
|enemy=
|map=
}}
"""

#=======================================================================

"""
Insert character data.

For full details on how to format character data, 
see build_character_data.py. 
"""

character_data = \
[
["''Gaiden''", 
 "fe02", 
 None, 
 
 ["Alm", "Celica", "Lukas", "Gray", "Tobin", "Kliff", "Silque", "Clair", 
 "Clive", "Forsyth", "Python", "Luthier", "Mathilda", "Delthea", "Tatiana", 
 "Zeke", "Mycen", "Mae", "Boey", "Genny", "Saber", "Valbar", "Kamui", "Leon", 
  "Palla", "Catria", "Atlas", "Jesse", "Sonya", "Deen", "Est", "Nomah"]], 

  ["''Echoes: Shadows of Valentia''", 
  "fe15", 
   None, 
   
 ["Alm", "Celica", "Lukas", "Gray", "Tobin", "Kliff", "Faye", "Silque", "Clair", 
 "Clive", "Forsyth", "Python", "Luthier", "Mathilda", "Delthea", "Tatiana", 
 "Zeke", "Mycen", "Mae", "Boey", "Genny", "Saber", "Valbar", "Kamui", "Leon", 
  "Palla", "Catria", "Atlas", "Jesse", "Sonya", "Deen", "Est", "Nomah", 
  "Conrad"]], 
  ]


# Insert a text note under the character data .
# If no note is needed, insert "None".
character_data_note = \
None

#=======================================================================

"""
Insert item data

For full details on how to format item_data, see build_item_data.py. 

Item data template:
  [["", 
    "",
    [["", ""], ]],
    
    ["", 
     "",
    [["", ""], ]],
   ]
"""

item_data = \
[["nes02", 
 "''Gaiden''", 
 [["Mage Ring", "Dropped by [[Jedah]]"], ]
 ],
]

# Insert note after under item data. 
# If no note is needed, insert "None".
item_data_note = \
"* <small>Note: There are no items to be found in {{title|Echoes: Shadows of Valentia}}. The following item list is for {{title|Gaiden}}.</small>"

#=======================================================================

shop_data_header = "Shop Data"

"""
Insert shop data. 
If there are no shops, input "None"

Shop info is formatted:
  [shop name, 
   [item1, item2, item3, ...]], 

Template:
  ["", 
  ["", "", ""]], 
"""

shops_info = \
None

#=======================================================================

# Insert if this page needs enemy data. 
include_enemy_data = True

"""
For full details on how to format enemy data, see build_enemy_data.py

Enemy data template:
  [["", 
    "", 
    [], 
    None],
   
   ["", 
    "", 
    [], 
    None]]

    
Unit data template:
  ["", "", "", "", None], 
  
"""

# Insert enemy data. 
enemy_data = \
[["nes02", 
  "''Gaiden''", 
  [["Aurum", "Aurum", "10", "2", None, None], 
  ["[[Gharn]]", "Arcanist", "10", "1", None, None], 
  ["[[Jedah]]", "Cantor", "20", "1", ["Mage Ring (drop)"], None], 
  ["Cerberus", "Cerberus", "10", "1", None, None], 
  ["Hades", "Hades", "10", "1", None, None], 
  ["Mogall", "Mogall", "5", "10", None, None], 
  ["Naberius", "Naberius", "10", "1", None, None], 
  ["[[Marla]]", "Witch", "8", "1", None, None], 
  ["[[Hestia]]", "Witch", "8", "1", None, None], 
  ["[[Duma]]", "Fell God", "20", "1", None, None], ], 
  None, ],
]


# Insert note under enemy data.
# If no note is needed, insert "None".
enemy_data_note = \
"""* <small>Note: Because [[Duma]], [[Jedah]], [[Marla]], and [[Hestia]] can [[conjure]] [[monster]]s, the number of reinforcements will vary.</small>
====''Echoes: Shadows of Valentia''====
{{sectstub}}
"""

# Insert whether or not you want to print out the units total. 
# If true, the unit and reinforcements total will print before the chapter page. 
print_units_total = False

#=======================================================================

"""
Insert NPC data below.

For full instructions on how to format npc_data, see build_npc_data.py. 

NPC data template:
  [["", 
   "", 
   [["", "", "", "", None]], ]]
"""

npc_data = \
None

# Insert a text note under enemy data. 
# If no note is needed, insert "None".
npc_data_note = None

"""====''Echoes: Shadows of Valentia''====
{{sectstub}}
"""

#=======================================================================

# Insert boss data
# If no boss is present, insert "None".
boss_data = \
"""{{Main|Duma}} 
{{Tab
|tab1=''Gaiden''
|tab2=''Echoes: Shadows of Valentia'' Normal Mode
|tab3=''Echoes: Shadows of Valentia'' Hard Mode
|content1={{BossStats FE2
|portrait=[[File:Bs fe02 enemy duma fell god 01.png]]
|class=Fell God
|lv=20
|HP=182
|pow=20
|skill=10
|spd=10
|luck=10
|def=20
|res=20
|move=5
|inventory=[[Tentacle]]
|spells=[[Ocular Beam]]<br>[[Oculus]]
}}
|content2={{BossStats FE15
|portrait=[[File:Portrait duma status fe15.png|128px]]
|class=Fell God
|age={{hover|30|May be a placeholder}}
|lv=30
|HP=?? (182)
|str=30
|skill=10
|spd=10
|luck=0
|def=20
|res=20
|move=2
|bm=y
|wm=y
|inventory=--
|skills=[[File:Is 3ds03 black magic forecast.png]] [[Ocular Beam]]<br>[[File:Is 3ds03 black magic forecast.png]] [[Oculus]]<br>[[File:Is 3ds03 white magic forecast.png]] [[Conjure]]<br>[[File:Is 3ds03 monster forecast.png]] [[Tentacle]]<br>[[File:Is 3ds03 skill personal.png]] [[Upheaval]]<br>[[File:Is 3ds03 skill personal.png]] [[Nullify Ailments]]
}}
* <small>Note: In addition to black magic and white magic, Duma also has proficiency in {{Monster15}}Terror weapons.</small>
|content3={{BossStats FE15
|portrait=[[File:Portrait duma status fe15.png|128px]]
|class=Fell God
|age={{hover|30|May be a placeholder}}
|lv=40
|HP=??
|str=32
|skill=15
|spd=10
|luck=0
|def=20
|res=20
|move=3
|bm=y
|wm=y
|inventory=--
|skills=[[File:Is 3ds03 black magic forecast.png]] [[Ocular Beam]]<br>[[File:Is 3ds03 black magic forecast.png]] [[Oculus]]<br>[[File:Is 3ds03 white magic forecast.png]] [[Conjure]]<br>[[File:Is 3ds03 monster forecast.png]] [[Tentacle]]<br>[[File:Is 3ds03 skill personal.png]] [[Upheaval]]<br>[[File:Is 3ds03 skill personal.png]] [[Nullify Ailments]]
}}
* <small>Note: In addition to black magic and white magic, Duma also has proficiency in {{Monster15}}Terror weapons.</small>
}}
"""

#=======================================================================

# Insert if the page needs a strategy section. 
include_strategy_section = True

# Insert strategy section.
# If "None" is inputted, this section will be marked a stub. 
strategy = None

#=======================================================================

# Insert trivia section.
# If "None" is inputted, this section will be left blank. 
trivia = """* The music that plays during this map is titled ''Twilight of the Gods''. 
* This map shares its name with the theme of the second part of the [[Sacred Stone (part 2)|final chapter]] of {{title|The Sacred Stones}}. 
"""

#=======================================================================

# Insert etymology section.
chapter_etymology = """{{Names 
|eng-name=The Final Battle
|eng-mean=--
|jap-name={{hover|最終決戦|Saishū kessen}}
|jap-mean=Final Showdown
|span-name=La batalla final
|span-mean=The final battle
|fren-name=Combat final
|fren-mean=Final battle
|ger-name=Die letzte Schlacht
|ger-mean=The last Battle
|ital-name=Battaglia finale
|ital-mean=Final battle
|dut-name=Het laatste gevecht
|dut-mean=The last battle
|ch-simp-name={{hover|最终决战|Mandarin: Zuìzhōng juézhàn; Cantonese: Juijung kuetjin}}
|ch-simp-mean=Final battle
|ch-trad-name={{hover|最終決戰|Mandarin: Zuìzhōng juézhàn; Cantonese: Juijung kuetjin}}
|ch-trad-mean=Final battle
}}
"""

# Etmology section template for non-localized chapters.
"""{{Names 
|eng-fan-name=
|eng-fan-mean=
|jap-name=
|jap-mean=
}}
"""

# Etmology section template for localized chapters.
"""{{Names 
|eng-name=
|eng-mean=--
|jap-name={{hover||}}
|jap-mean=
|span-name=
|span-mean=
|fren-name=
|fren-mean=
|ger-name=
|ger-mean=
|ital-name=
|ital-mean=
|dut-name=
|dut-mean=
|ch-simp-name={{hover||Mandarin: ; Cantonese: }}
|ch-simp-mean=
|ch-trad-name={{hover||Mandarin: ; Cantonese: }}
|ch-trad-mean=
}}
"""

#=======================================================================

# Insert gallery text.
# If "None" is inputted, this section will be marked a stub. 
gallery_text = \
None

#=======================================================================

# Insert chapter navigator.
chapter_navigator_section = \
None

# Chapter navigator template.
"""{{ChapterNav
|prechapter=
|prealternate=
|name=
|nextchapter=
|nextalternate=
}}
"""


#=======================================================================


def main():
  
  # Takes every variable defined above and constructs a chapter page.
  chapter_page = \
    build_chapter_page(hatnote, 
                       platform, 
                       chapter_title, 
                       chapter_infobox,
                       game,
                       quote,
                       quote_speaker,
                       chapter_desciption,
                       insert_plot_section,
                       chapter_plot,
                       beginning_log,
                       chapter_data_box,  
                       character_data, 
                       character_data_note,
                       item_data,
                       item_data_note, 
                       shop_data_header,
                       shops_info,
                       include_enemy_data, 
                       enemy_data,
                       enemy_data_note,
                       print_units_total,
                       npc_data,
                       npc_data_note,
                       boss_data,
                       chapter_navigator_section, 
                       include_strategy_section, 
                       strategy,
                       trivia, 
                       chapter_etymology,
                       gallery_text, 
                       isStub)
               
  print(chapter_page)
  
  # Insert whether you want to save the chapter page as a text file.
  savetoTextFile = False
  
  # Insert the name of the text file, assuming you want to save one. 
  file_name = "chapter_page.txt"
  
  if savetoTextFile:
    writeTextFile(file_name, chapter_page)


if __name__ == "__main__":
  main()

