
"""
Written by Albert "Anferensis" Ong

Miscellaneous utility functions that are used for other
fireemblemwiki scripts. 
"""


def hyperlink(link, display_text = None):
	"""A funtion that converts text, represented as a string, into
	a hyperlink. This is based off of mediawiki, where adding square
	brackets around text, as in linkname ---> [[linkname]], will create a hyperlink. 
	
	Accepts two values:
		1. A link, represented as a string
		2. Optional display text, inputted as a string.
		   Set to "None" otherwise
	
	Functions such that:
		hyperlink("Lyn") ---> [[Lyn]]
		hyperlink("Lyn", "A girl") ---> [[Lyn|A girl]]
		
	Note: Display text is for cases where the display text of a 
		  hyperlink is different from the name of the link itself. 
	"""
	
	# If there is no inputted display text
	if display_text == None:
		
		# Just adds brackets around the link
		formatted_link = "[[" + link + "]]"
	
	# Otherwise...	
	else:
		
		# Formats the hyperlink such that the display text is
		# different from the link name.
		formatted_link = "[[" + link + "|" + display_text +"]]"
	
	# Returns the formatted link. 
	return formatted_link



def writeTextFile(file_name, body):
	"""
	A function that will write a given body of text to a 
	given file name. 
	"""
	file_writer = open(file_name, "w")
	file_writer.write(body)
	file_writer.close()
	
	print("Text saved to file: " + file_name)



#=======================================================================

def main():
	pass

	
if __name__ == "__main__":
	main()


