'''# 215*414?
for x in range(127, 10 ** 9 + 1,127):
    if str(x)[:3] == '215' and '414' in str(x):
        print(x, x // 127)'''

# 123*5*
from fnmatch import *

for x in range(2023, 10**9 + 1, 2023):
    if fnmatch(str(x), '1?2139*4'):
        print(x,x//2023)
