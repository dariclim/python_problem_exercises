"""
Complete the function/method so that it takes CamelCase string 
and returns the string in snake_case notation. Lowercase characters 
can be numbers. If method gets number, it should return string.

Examples:

# returns test_controller
to_underscore('TestController')

"""

import re
def to_underscore(string):  

	# what this mean?
	# find all nonoverlapping matches of string pattern, returns as list of strings
	# Matches an uppercase letter from A-Z
	# 
    if re.findall('[A-Z][^A-Z]*', str(string)):
        words = re.findall('[A-Z][^A-Z]*', str(string))
        return '_'.join([w.lower() for w in words]) 
    else:
        return str(string)

def to_underscore_complex_re(string):
    return re.sub(r'(.)([A-Z])', r'\1_\2', str(string)).lower()    