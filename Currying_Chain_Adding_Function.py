"""
We want to create a function that will add 
numbers together when called in succession.

add(1)(2);
// returns 3
We also want to be able to continue to add numbers to our chain.

add(1)(2)(3); // 6
add(1)(2)(3)(4); // 10
add(1)(2)(3)(4)(5); // 15
and so on.

A single call should return the number passed in.

add(1); // 1
We should be able to store the returned values and reuse them.

"""

class add(int):
	def __call__(self, n):
		return add(self+n)

# __call__ is called when instance of class is 'called'

"""
add(1)(2)
1 = self
2 = n
__call__ is activated since it's called
as result, returns another function, add(3)
add(3) again calls __call__, looks for another parameter n next to it, doesn't see one
So it keeps going as add(3)?

Does this have a base case?

Base case: 

LOOK UP: Python Recursion
http://www.python-course.eu/recursive_functions.php

"""