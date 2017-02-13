
"""
Written by Albert"Anferensis"Ong
"""


def build_chapter_quote(quote, quote_speaker):
	
	if quote == None or quote_speaker == None:
		chapter_quote = ""
	else:
		chapter_quote = "{{Quote|" + quote + "|" + quote_speaker + "}}"
	
	return chapter_quote



#========================================================================

quote = """I fight for my friends."""
quote_speaker = "[[Ike]]"

print(build_chapter_quote(quote, quote_speaker))
