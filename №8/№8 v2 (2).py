from itertools import *

cnt = 0
for i in set(permutations('012345678', r=5)):
    if i[0] != "0" and (i.count("1") + i.count("3") + i.count("5") + i.count("7") + i.count("9")) == 3:
        cnt += 1
print(cnt)
