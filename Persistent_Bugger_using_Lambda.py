"""
Write a function, persistence, 
that takes in a positive parameter num and 
returns its multiplicative persistence, 
which is the number of times you must multiply 
the digits in num until you reach a single digit.

For example:

 persistence(39) => 3  # Because 3*9 = 27, 2*7 = 14, 1*4=4
                       # and 4 has only one digit.
"""

def persistence(n):
	c = 0
	while n>= 10:
		n = reduce(lambda x, y: int(x)*int(y), list(str(n)))
		c += 1
	return c

"""
reduce(func, seq)
reduce takes a function and applies it to the seq, returning a single value
doing just:
	lambda x, y: int(x)*int(y), list(str(n))
would give us this funky:
	(<function <lambda> at 0x1007369b0>, ['2', '5'])
that's bc you usually assign lambdas to a variable like
	s = lambda x, y: int(x)*int(y)
	s(1,2)
"""