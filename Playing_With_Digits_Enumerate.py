"""
Some numbers have funny properties. For example:

89 --> 8¹ + 9² = 89 * 1

695 --> 6² + 9³ + 5⁴= 1390 = 695 * 2

46288 --> 4³ + 6⁴+ 2⁵ + 8⁶ + 8⁷ = 2360688 = 46288 * 51
Given a positive integer n written as abcd... 
(a, b, c, d... being digits) and a positive integer p 
we want to find a positive integer k, if it exists, 
such as the sum of the digits of n taken to the 
successive powers of p is equal to k * n. 

"""

def dig_pow_mine(n, p):
	powed = []
	for d in str(n):
		powed.append(int(d)**p)
		p += 1
	if sum(powed) % n == 0:
		return sum(powed)/n
	return -1

# enumerate: creates a couter for an iterable
# you gotta assign two variables when using enumerate. 
# First one = counter, Second one = your variable

def dig_power_enum(n, p):
	s = 0
	for count, d in enumerate(str(n)):
		s += (int(d)**(p + count))
		# or math.pow(int(d), p + count)
	return s /n if s % n == 0 else -1
