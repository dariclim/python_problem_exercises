"""
The goal of this exercise is to convert a string to a 
new string where each character in the new string is 
'(' if that character appears only once in the original 
string, or ')' if that character appears more than once 
in the original string. Ignore capitalization when determining 
if a character is a duplicate.

Examples:

"din" => "((("

"recede" => "()()()"
"""

def duplicate_encode(word):
	word = word.lower()
	return ''.join([')' if word.count(c) > 1 else '(' for c in word])


"""
At first, I didn't assign word as word.lower, which made trouble on:
	return ''.join([')' if word.count(c) > 1 else '(' for c in word.lower()])
See error? I didn't count the c from word.lower, I did from word itself which
causes problems for Uppercase words that are turned into Lowercase words. 


"""