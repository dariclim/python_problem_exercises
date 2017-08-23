"""
Write a function that accepts a string, 
and returns true if it is in the form of a phone number. 
Assume that any integer from 0-9 in any of the spots will 
produce a valid phone number.

Only worry about the following format:
(123) 456-7890 (don't forget the space after the close parentheses) 

"""

import re
def my_validPhoneNumber(phoneNumber):
	trial = filter(None, re.split('(\W)', phoneNumber))
	is_number = False
	if trial[0] == '(' and trial[2] == ')' and trial[5] == '-' and trial[1].isdigit() and trial[4].isdigit() and trial[6].isdigit():
		if len(trial[1]) == 3 and len(trial[4]) == 3 and len(trial[6]) == 4:
			is_number = True
	return is_number


def better_validPhoneNumber(phoneNumber):
    if re.match('^\([0-9]{3}\) [0-9]{3}-[0-9]{4}$',phoneNumber):
        return True
    return False

    #lesson learned: I really need to learn about regex!