import math
def find_nb_unsuccessful(m):
    sum = 0
    cube = 1
    for i in range(int(math.sqrt(m))):  
        m -= cube**3
        if m == 0:
            return cube  
        cube += 1
    return -1