from itertools import *

numb = 1
for i in product("АДНИ", repeat=5):
    s = "".join(i)
    if s == 'ДДДДД':
        print(numb, s)
        break
    numb += 1