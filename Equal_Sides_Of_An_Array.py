"""
You are going to be given an array of integers. 
\Your job is to take that array and find an index N where 
the sum of the integers to the left of N is equal to the 
sum of the integers to the right of N. If there is no index 
that would make this happen, return -1.

For example:

Let's say you are given the array {1,2,3,4,3,2,1}:
Your function will return the index 3, because at 
the 3rd position of the array, the sum of left side of 
the index ({1,2,3}) and the sum of the right side of the 
index ({3,2,1}) both equal 6.

Let's look at another one.
You are given the array {1,100,50,-51,1,1}:
Your function will return the index 1, because at 
the 1st position of the array, the sum of left side
of the index ({1}) and the sum of the right side of 
the index ({50,-51,1,1}) both equal 1.
"""


def find_even_index_mine(arr):
	start_at = -1
	for n in arr:
		loc = arr.index(N, start_at + 1)
		start_at = loc
		if sum(arr[0:loc]) == sum(arr[loc + 1:]):
			return loc
	return -1

"""
Look at what this guy did.
IF THERE ARE DUPLICATE ELEMENTS IN YOUR LIST...
GET THE LENGTH OF THE ARRAY, and MAKE A RANGE OF IT.
COMPLETELY IGNORES THE WORRY OF DUPLICATES!!!
"""	

def find_even_index_better(arr):
	for i in range(len(arr)):
		if sum(arr[:i]) == sum(arr[i+1:]):
			return i
	return -1