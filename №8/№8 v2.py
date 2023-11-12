from itertools import *

count = 0
for i in product("БАНДЕРОЛЬ", repeat=7):
    gl = 0
    sogl = 0
    for j in i:
        if j in "БНДРЛ":
            sogl += 1
        elif j in "АЕО":
            gl += 1
    if gl > sogl:
        count += 1
print(count)
