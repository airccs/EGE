from itertools import *

numb = 1
for i in product("EMNOY", repeat=5):
    s = "".join(i)
    if numb == 1055:
        print(numb, s)
    numb += 1
