
"""
Written by Albert"Anferensis"Ong

Revision: 28.12.2018

A function that constructs a quote template for fireemblemwiki.org
"""


def build_chapter_quote(quote, quote_speaker):
	"""
  Contructs a quote template for fireemblemwiki.org
  
  Takes two string arguments:
    1. The text of the quote itself.
    2. The text of the quote speaker. 
  """

	if quote == None or quote_speaker == None:
		chapter_quote = ""
	else:
		chapter_quote = "{{quote|" + quote + "|" + quote_speaker + "}}"
	
	return chapter_quote


#========================================================================


def main():
  quote = """I fight for my friends."""
  quote_speaker = "[[Ike]]"

  print(build_chapter_quote(quote, quote_speaker))

if __name__ == "__main__":
  main()


