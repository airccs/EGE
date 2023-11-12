from itertools import *

numb = 1
for i in product("АИЛПС", repeat=5):
    s = "".join(i)
    if numb == 2791 :
        print(numb, s)
        break
    numb += 1
