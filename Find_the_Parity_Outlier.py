"""
You are given an array (which will have a length of at least 3, 
but could be very large) containing integers.
 The array is either entirely comprised of odd integers 
 or entirely comprised of even integers except 
 for a single integer N. Write a method that takes the array 
 3as an argument and returns N.

For example:

[2, 4, 0, 100, 4, 11, 2602, 36]

Should return: 11
"""

def find_outlier(integers):
    mods = [n % 2 for n in integers]
    if mods.count(0) > mods.count(1):
        return integers[mods.index(1)]
    else:
        return integers[mods.index(0)]

"""
mods = [n % 2 == 0 for n in integers]

when we do mods like this and make a list, we get:
True, False, True, True... etc
True for when n % 2 = 0 etc
"""