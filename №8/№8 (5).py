from itertools import *

numb = 1
for i in product("АЕКНРС", repeat=6):
    if i.count("А") <= 3 and i.count("Н") == 2:
        print(numb)
        break
    numb += 1
