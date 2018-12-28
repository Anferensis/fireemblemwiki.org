#!/usr/bin/env python
# -*- coding: utf-8 -*- 

"""
Written by Albert"Anferensis"Ong
Formats a web citation for fireemblemwiki.org

Revision: 14.09.2018
"""

import re
from calendar import month_name
from datetime import datetime
from urllib.parse import urlparse
from urllib.request import urlopen


def build_web_reference(url,
                        name = None):
  """
  A function that creates a web reference for fireemblemwiki.org
  
  Accepts two values as inputs:
    1. The url of the citation
       Example: https://www.google.com/
       
    2. The name of the reference. 
       This is only crucial if the reference will be used multiple
       times. Otherwise, input 'None' in this field.
                        
  Input is formatted:
    [url, 
     name]

  Example:
   build_web_reference("https://www.google.com/", None)
  
  Returns:
    <ref>{{cite web |url=https://www.google.com/ |title=Google 
    |site=www.google.com |retrieved=current UTC date}}</ref>    
  """
  
  # The beginning of the formatted references. 
  # This will become the final output. 
  if name != None:
    reference = "<ref name=" + name + ">{{cite web"
  else:
    reference = "<ref>{{cite web"
  
  # Assembles the formatted url line.  
  url_line =   " |url=" + url
  

  #---------------------------------------------------------------------
  # Automatically retrieves and formats the page title. 
  #---------------------------------------------------------------------
  
  # Formats the title if the url is not blank.
  if url != "":
  
    # Reads the html as a byte object. 
    html_bytes = urlopen(url).read()

    # Converts the html byte object to a text object. 
    html_text = str(html_bytes, "utf-8", errors = "ignore")
    
    # Retrieves the title of the html text. 
    pattern = re.compile("<title>(.+?)</title>")
    title = re.findall(pattern, html_text)[0]
    
    # Adds the nowiki tag around the title if the title has a vertical
    # bar. This is because the vertical bar can be rendered by MediaWiki.
    if "|" in title:
      title = "<nowiki>" + title + "</nowiki>"
  
  # Otherwise, the title is blank.
  else: 
    title = ""
  
  # Assembles the title line.
  title_line = " |title=" + title
  
  
  #---------------------------------------------------------------------
  # Automatically retrieves and formats the page site.  
  #---------------------------------------------------------------------
  
  # Formats the site if the url is no blank.
  if url != "":
    
    # Parses the url and retrieves the site name. 
    parsed_url = urlparse(url)
    site = parsed_url.netloc
    
    # Adds 'www.' at the beginning of the site if it does not
    # already include it. 
    if not site.startswith("www."):
      site = "www." + site
    
  # Otherwise the site is blank.
  else:
    site = ""
  
  # Assembles the site line. 
  site_line = " |site=" + site
  
  
  #---------------------------------------------------------------------
  # Automatically retrieves and formats the current UTC time.  
  #---------------------------------------------------------------------
  
  # Retrieves the current UTC time. This is used to assemble the
  # date retrieved line.
  utc_time = datetime.utcnow()

  # Formats the day, month name, and year as strings.
  day_str =      str(utc_time.day) 
  month_name_str = str(month_name[utc_time.month])
  year_str =       str(utc_time.year)

  # Assembles and formats the current UTC time.
  formatted_utc_time = " ".join([day_str, month_name_str, year_str])
  
  # Assembles the date retrieved line. 
  retrieved_line = " |retrieved=" + formatted_utc_time
  
  
  #---------------------------------------------------------------------
  # Formats the complete reference.
  #---------------------------------------------------------------------
  
  # Uses a for loop to add each line to the final output.
  for line in (url_line, 
         title_line, 
         site_line,   
         retrieved_line):
    
    reference += line
  
  # Adds the ending section to the reference.   
  reference += "}}</ref>"
  
  # Returns the formatted reference. 
  return reference



def build_multiple_web_references(reference_data):
  """
  A function that buils multiple web references using the function
  build_reference. 
  
  Input is formatted:
    [[url1, 
      name1], 
      
      [url2, 
      name2], 
      
      ...  (as many references as needed)
      
      ] 
  """
  
  # The string that will become the final output.
  multiple_references = ""
  
  # Uses a for loop to access the data of each reference. 
  for ref_data in reference_data:
    
    # Retrieves each piece of data from the reference data.
    ref_url = ref_data[0]
    ref_name = ref_data[1]
    
    # Uses the build_web_reference function to format the reference.
    formatted_reference = \
      build_web_reference(ref_url, 
                ref_name)
    
    # Adds the formatted reference to the final output.          
    multiple_references += formatted_reference + "\n\n"
    
  # By the end of the for loop, every reference will have been formatted
  # and been added to multiple_refereces.
    
  # Returns the final output.
  return multiple_references



#=======================================================================


def main():
  
  """
  Insert reference data
  
  Reference data is formatted:
    [url, 
     name = None]
  """
  
  reference_data = \
[   
  ["https://kantopia.wordpress.com/2014/10/21/fire-emblem-7-will-artbook-translation/", 
   "artbook"],
   
  ["http://www.thinkbabynames.com/meaning/1/Will", 
   None]
]
  
  # Assembles the references using the input above.
  multiple_references = build_multiple_web_references(reference_data)
  
  # Prints out the references. 
  print(multiple_references)
  

if __name__ == "__main__":
  main()


