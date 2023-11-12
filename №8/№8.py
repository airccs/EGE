from itertools import *

numb = 1
for i in product("АДИН", repeat=5):
    s = "".join(i)
    if s == 'ДИАНА':
        print(numb, s)
    numb += 1
