#!/usr/bin/env python
# -*- coding: utf-8 -*- 

"""
Written by Albert"Anferensis"Ong
Formats a web citation for fireemblemwiki.org

Revision: 08.01.2018
"""

from calendar import month_name
from datetime import datetime


def build_web_reference(url,
						title, 
						site, 
						# date_retrieved, 
						name = None):
	"""
	A function that creates a web reference for fireemblemwiki.org
	
	Accepts four string values as inputs:
		1. The url of the citation
			Example: https://www.google.com/
			
		2. The title of the web page
			Example: Google 
			
		3. The name of the site
			Example: www.google.com
			
		4. The name of the reference. 
		   This is only crucial if the reference will be used multiple
		   times. Otherwise, input 'None' in this criteria.
			
	Input is formatted:
		[url, 
		 page title, 
		 site, 
		 name]
	
	Example:
	
		build_web_reference("https://www.google.com/", 
							"Google", 
							"www.google.com", 
							None)
							
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
	
	# Assembles the formatted url, title, and site lines. 
	url_line =   " |url=" + url
	title_line = " |title=" + title
	site_line =  " |site=" + site
	
	# Retrieves the current UTC time. This is used to assemble the
	# date retrieved line.
	utc_time = datetime.utcnow()

	# Formats the day, month name, and year as strings.
	day_str = 		 str(utc_time.day) 
	month_name_str = str(month_name[utc_time.month])
	year_str =       str(utc_time.year)

	# Assembles and formats the current UTC time.
	formatted_utc_time = " ".join([day_str, month_name_str, year_str])
	
	# Assembles the date retrieved line. 
	retrieved_line = " |retrieved=" + formatted_utc_time
	
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
		  title1, 
		  site1, 
		  name1], 
		  
		  [url2, 
		  title2, 
		  site2, 
		  name2], 
		  
		  ...	(as many references as needed)
		  
		  ] 
	"""
	
	# The string that will become the final output.
	multiple_references = ""
	
	# Uses a for loop to access the data of each reference. 
	for ref_data in reference_data:
		
		# Retrieves each piece of data from the reference data.
		ref_url = ref_data[0]
		ref_title = ref_data[1]
		ref_site = ref_data[2]
		ref_name = ref_data[3]
		
		# Uses the build_web_reference function to format the reference.
		formatted_reference = \
			build_web_reference(ref_url, 
								ref_title, 
								ref_site, 
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
		 title, 
		 site, 
		 name = None]
	
	Reference data template:
		[["", 
		  "", 
		  "", 
		  ""], 
		  
		 ["", 
		  "", 
		  "", 
		  ""], 
		  
		 ["", 
		  "", 
		  "", 
		  ""], ]
	"""
	
	reference_data = \
[ 	
	["", 
	 "<nowiki></nowiki>", 
	 "", 
	 None],
]

	"""
	["", 
	 "<nowiki></nowiki>", 
	 "", 
	 None],

	["", 
	 "<nowiki></nowiki>", 
	 "www.kantopia.wordpress.com", 
	 None], 

	["", 
	 "<nowiki></nowiki>", 
	 "www.behindthevoiceactors.com", 
	 None], 
	"""	
	
	# Assembles the references using the input above.
	multiple_references = build_multiple_web_references(reference_data)
	
	# Prints out the references. 
	print(multiple_references)
	

if __name__ == "__main__":
	main()


