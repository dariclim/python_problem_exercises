"""
The word i18n is a common abbreviation of internationalization 
the developer community use instead of typing the whole word and 
trying to spell it correctly. Similarly, a11y is an abbreviation of accessibility.

Write a function that takes a string and turns any and all "words" (see below) 
within that string of length 4 or greater into an abbreviation following the same rules.

Notes:

A "word" is a sequence of alphabetical characters. By this definition, any other 
character like a space or hyphen (eg. "elephant-ride") will split up a series of 
letters into two words (eg. "elephant" and "ride").
The abbreviated version of the word should have the first letter, then the 
number of removed characters, then the last letter (eg. "elephant ride" => "e6t r2e").

"""

import re

def my_abbreviate(s):
	updated = []
	for word in re.split('(\W)', s):
		if len(word) > 3:
			updated.append(word[0] + str(len(word) - 2) + word[len(word) - 1 ])
		else:
			updated.append(word)
	return ''.join(updated)
print abbreviate('elephant-rides are really fun!')



def someone_else_abbreviate(s):
    words = re.split("\W+", s)
    for word in words:
        if len(word) > 3:
            w = word[0] + str(len(word)-2) + word[-1]
            s = s.replace(word, w)				#He replaced the word directly from string
    return s