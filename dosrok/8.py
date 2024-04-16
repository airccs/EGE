from itertools import *

t = 1
for i in product("АПРСУ", repeat=5):
    s = "".join(i)
    if s.count("У") <= 1 and "АА" not in s:
        print(t)
    t += 1
