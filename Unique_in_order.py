"""
Implement the function unique_in_order which 
takes as argument a sequence and returns a list 
of items without any elements with the same value 
next to each other and preserving the original 
order of elements.


For example:

unique_in_order('AAAABBBCCDAABBB') == ['A', 'B', 'C', 'D', 'A', 'B']
unique_in_order('ABBCcAD')         == ['A', 'B', 'C', 'c', 'A', 'D']
unique_in_order([1,2,2,3,3])       == [1,2,3]
"""

def unique_in_order_mine(iterable):
    list = []
    if iterable:
        for x in range(len(iterable) - 1):
            if iterable[x] != iterable[x+1]:
                list.append(iterable[x]) 
        list.append(iterable[-1])
        # this is clunky
    return list


def unique_in_order_better(iterable):
	list = []
	prev = None
	for char in iterable:
		if char != prev:
			list.append(char)
			prev = char
	return list

def unique_in_order_alternate(iterable):
	list = []
	for char in iterable:
		if len(list) == 0 or char != list[-1]:
			list.append(char)
	return list
# this one is better because uses the list more
