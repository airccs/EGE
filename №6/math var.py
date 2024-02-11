"""from math import *

cnt = 0
for x in range(-1000, 1000):
    for y in range(-1000, 1000):
        if x > 0 and \
                y > tan(radians(30)) * x and \
                y < 111 + tan(radians(150)) * x:
            cnt += 1
print(cnt)
"""

from math import *

cnt = 0
for x in range(-1000, 1000):
    for y in range(-1000, 1000):
        if x > 0 and y > tan(radians(30)) * x and y < tan(radians(150)) * x + 137:
            cnt += 1
print(cnt)
