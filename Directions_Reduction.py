"""
Once upon a time, on a way through the old wild west, a man was given directions 
to go from one point to another. 
The directions were "NORTH", "SOUTH", "WEST", "EAST". 
Clearly "NORTH" and "SOUTH" are opposite, "WEST" and "EAST" too. 
Going to one direction and coming back the opposite direction is a needless effort. 
Since this is the wild west, with dreadfull weather and not much water, 
it's important to save yourself some energy, otherwise you might die of thirst!

Not all paths can be made simpler. 
The path ["NORTH", "WEST", "SOUTH", "EAST"] is not reducible.
"NORTH" and "WEST", "WEST" and "SOUTH", "SOUTH" and "EAST" are not directly 
opposite of each other and can't become such.
Hence the result path is itself : ["NORTH", "WEST", "SOUTH", "EAST"].

"""

def dirReduc(arr):
    opp = { 'NORTH':'SOUTH',
            'SOUTH': 'NORTH',
            'WEST': 'EAST',
            'EAST': 'WEST' }
    new = []
    for i in arr:
        if len(new) == 0:
            new.append(i)
        else:
            if new[len(new)-1] == opp[i]:
                new.pop()
            else:
                new.append(i)
    return new

"""
for each direction in the arr:
if new is empty, we add that new direction into new. Now len(new) is 1.
next direction:
if the element at new[0] is the opposite of the direction:
    we now pop that element out. pop() pops the last item, 
    which will always be the one in question
if not:
    add it to new, it's a completely unrelated direction!
"""    

def dirReduc_simplified(arr):
    opp = { 'NORTH':'SOUTH',
            'SOUTH': 'NORTH',
            'WEST': 'EAST',
            'EAST': 'WEST' }
    new = []
    for i in arr:
        if new and new[-1] == opp[i]:
        # if new: True. new is empty rn, so returns False
        # new[-1] grabs the very last. Reads new from the right
            new.pop()
        else:
            new.append(i)
    return new

def dirReduc_clever(arr):
    dir = " ".join(arr)
    dir2 = dir.replace("NORTH SOUTH",'').replace("SOUTH NORTH",'').replace("EAST WEST",'').replace("WEST EAST",'')
    dir3 = dir2.split()
    print(dir3, arr)
    print(dirReduc(dir3))
    print(len(dir3), len(arr))
    print(len(dirReduc(dir3)), len(arr))
    return dirReduc(dir3) if len(dir3) < len(arr) else dir3

print(dirReduc_clever(["NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST"]))
