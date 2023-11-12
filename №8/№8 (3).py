from itertools import *

numb = 1
for i in product("CLMSU", repeat=5):
    s = "".join(i)
    if s[:1] == 'S':
        print(numb, s)
        break
    numb += 1


