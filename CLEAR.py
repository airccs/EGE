from itertools import *

cnt = 1
for i in product("АЕКНРС", repeat=6):
    s = "".join(i)
    if s.count("А") <= 3 and s.count("Н") == 2:
        print(s, cnt)
        break
    cnt += 1
