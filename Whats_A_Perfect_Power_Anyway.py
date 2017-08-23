from math import *

def isPP(n):
    for i in range(2,n):
        if round(log(n,i),15).is_integer():
        	#math.log gave me a ridiculous 0.000000000004
            return [i,log(n,i)]
        else:
            continue
    return None
"""
This piece of shit above that I made	
doesn't work.
I didn't think of re-trying the result...
checking if the number to the nth power comes back out to n 
"""

def isPP_1(n):
	for b in range(2, int(sqrt(n)) + 1):
		e = int(round(log(n,b)))
		if b ** e == n:
			return [b, e]
	return None

print isPP_1(216)