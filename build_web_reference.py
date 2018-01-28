
"""
Written by Albert"Anferensis"Ong
Formats a web citation for fireemblemwiki.org

Revision: 01-27-2018
"""

def build_web_reference(url,
					title, 
					site, 
					date_retrieved):
	"""
	A function that creates a web reference for fireemblemwiki.org
	
	Accepts four string values as inputs:
		1. The url of the citation
			Example: https://www.google.com/
			
		2. The title of the web page
			Example: Google 
			
		3. The name of the site
			Example: www.google.com
			
		4. The date the site was accessed
			Example: 1 January, 2000
			
	Input is formatted:
		[url, 
		 page title, 
		 site, 
		 date retrieved]
	
	
	Example:
	
		build_web_reference("https://www.google.com/", 
							"Google", 
							"www.google.com", 
							"1 January, 2000")
							
		Returns:
			<ref>{{cite web |url=https://www.google.com/ |title=Google 
			|site=www.google.com |retrieved=1 January, 2000}}</ref>		
	"""
	
	# The beginning of the formatted references. 
	# This will become the final output. 
	reference = "<ref>{{cite web "
	
	# Assembles the formatted url, title, site, and date lines. 
	url_line = "|url=" + url
	title_line = " |title=" + title
	site_line = " |site=" + site
	retrieved_line = " |retrieved=" + date_retrieved
	
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
		  date1], 
		  
		  [url2, 
		  title2, 
		  site2, 
		  date2], 
		  
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
		ref_retrieved = ref_data[3]
		
		# Uses the build_web_reference function to format the reference.
		formatted_reference = \
			build_web_reference(ref_url, 
							ref_title, 
							ref_site, 
							ref_retrieved)
		
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
		 date retrieved]
	
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
	[["", 
	  "", 
	  "", 
	  ""], 
	   ]
	   
	
	# Assembles the references using the input above.
	multiple_references = build_multiple_web_references(reference_data)
	
	# Prints out the references. 
	print(multiple_references)
	

if __name__ == "__main__":
	main()

