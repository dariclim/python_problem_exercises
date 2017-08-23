def sum_pairs_failed(ints, s):
    for i in range(len(ints)):
        for c in range(len(ints[i+1:])):
            print [ints[i], ints[i + c + 1]]
            if ints[i] + ints[i + c + 1] == s:
                return [ints[i], ints[i + c + 1]]
    return None

# after googling for a bit

def sum_pairs(ints, s):
	lookup = []
	for num in ints:
		if s - num in lookup:
			return lookup[s - num]
		lookup.append(num)