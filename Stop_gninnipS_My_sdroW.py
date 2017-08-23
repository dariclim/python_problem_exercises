"""
Stop gninnipS My sdroW!
Write a function that takes in a string of one or more words, 
and returns the same string, but with all five or more letter words reversed 
(Just like the name of this Kata). Strings passed in will consist of only letters and spaces. 
Spaces will be included only when more than one word is present.
"""

def my_spin_words(sentence):
    new = []
    for word in sentence.split(' '):
        if len(word) < 4: 
            new.append(word)
        else:
            wl = list(word)
            spun = ''
            c = 1
            while (len(word) - c) >= 0:
                spun += wl[len(word)-c]
                c += 1
            new.append(spun)
    return ' '.join(new)



#	for x in sentence.split(" "):
#		if len(x) >= 5:
#			x[::-1]
#		else:
#			x

def better_spin_words(sentence):
    return " ".join([x[::-1] if len(x) >= 5 else x for x in sentence.split(" ")])

# [::-1] reverses a list, or even a string!
# you can [do an entire for loop into an array just like this.]

print better_spin_words('Welcome to my humble abode.')

